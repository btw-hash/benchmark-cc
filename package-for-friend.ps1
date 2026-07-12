#!/usr/bin/env pwsh
# Packages benchmark-cc into a zip ready to send to a friend (no git required).
# Excludes: .git, runs/, results/runs_*.jsonl (your data), G_*_personal (your config),
# node_modules, .credentials.

$ErrorActionPreference = "Stop"
$outName = "benchmark-cc-friend.zip"
$outPath = "../$outName"

Write-Host "Packaging benchmark-cc for friend..." -ForegroundColor Cyan

# Build exclusion list
$excludes = @(
    ".git",
    "runs",
    "node_modules",
    "*.credentials.json",
    ".judge-config"
)

# Use Compress-Archive with explicit file list (Get-ChildItem + filter)
$temp = New-Item -ItemType Directory -Path "../.benchmark-cc-staging" -Force
Copy-Item -Path "*" -Destination $temp -Recurse -Exclude $excludes

# Strip your personal results / configs from the staging copy
Remove-Item "$temp/results/runs_*.jsonl" -ErrorAction SilentlyContinue
Remove-Item "$temp/results/judged_*.jsonl" -ErrorAction SilentlyContinue
Remove-Item "$temp/setups/G_*_personal" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$temp/setups/*/.claude/.credentials.json" -ErrorAction SilentlyContinue
Get-ChildItem "$temp/setups" -Recurse -Include ".claude.json","backups","sessions","file-history","session-env","shell-snapshots","projects","todos","cache",".cache","statsig","ide","mcp-needs-auth-cache.json",".last-cleanup","local","__store.db*" -Force | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$temp/runs" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$temp/.judge-config" -Recurse -Force -ErrorAction SilentlyContinue

# Keep results dir but only with .gitkeep
New-Item -ItemType Directory -Path "$temp/results" -Force | Out-Null
New-Item -ItemType File -Path "$temp/results/.gitkeep" -Force | Out-Null

if (Test-Path $outPath) { Remove-Item $outPath }
Compress-Archive -Path "$temp/*" -DestinationPath $outPath -Force
Remove-Item $temp -Recurse -Force

$size = [math]::Round((Get-Item $outPath).Length / 1MB, 2)
Write-Host ""
Write-Host "Created: $outPath ($size MB)" -ForegroundColor Green
Write-Host ""
Write-Host "Send this file to your friend via Telegram / email / drive." -ForegroundColor Cyan
Write-Host "Their instructions are in FRIEND.md inside the zip." -ForegroundColor Cyan
Write-Host ""
Write-Host "When they send you back their results zip, run:" -ForegroundColor Cyan
Write-Host "  ./import-friend-results.ps1 -ZipPath path\to\bob-results.zip" -ForegroundColor White
