#!/usr/bin/env pwsh
# Unpacks a friend's results zip into your local benchmark-cc dir.
# Run this when they send you back benchmark-results-<name>.zip.

param(
    [Parameter(Mandatory=$true)] [string]$ZipPath
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $ZipPath)) {
    throw "File not found: $ZipPath"
}

Write-Host "Importing $ZipPath..." -ForegroundColor Cyan

# Extract to a temp location, verify structure, then merge in
$temp = "../.import-staging"
if (Test-Path $temp) { Remove-Item $temp -Recurse -Force }
Expand-Archive -Path $ZipPath -DestinationPath $temp

# Find the results jsonl file
$jsonl = Get-ChildItem -Path "$temp/results" -Filter "runs_*.jsonl" -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $jsonl) {
    throw "No results/runs_*.jsonl found in zip — wrong file?"
}

$friendName = ($jsonl.Name -replace '^runs_', '' -replace '\.jsonl$', '')
Write-Host "Found runs for: $friendName ($((Get-Content $jsonl.FullName).Count) rows)" -ForegroundColor Green

# Copy jsonl
Copy-Item $jsonl.FullName "results/" -Force
Write-Host "  imported results/$($jsonl.Name)"

# Copy runs/ artifacts if present
$runsDir = "$temp/runs/$friendName"
if (Test-Path $runsDir) {
    if (-not (Test-Path "runs")) { New-Item -ItemType Directory -Path "runs" -Force | Out-Null }
    Copy-Item $runsDir "runs/" -Recurse -Force
    Write-Host "  imported runs/$friendName/"
}

Remove-Item $temp -Recurse -Force

Write-Host ""
Write-Host "Done. Now run:" -ForegroundColor Cyan
Write-Host "  node judge.mjs       # judges both your data and theirs" -ForegroundColor White
Write-Host "  node merge.mjs       # produces report.md with combined analysis" -ForegroundColor White
