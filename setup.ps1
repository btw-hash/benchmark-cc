#!/usr/bin/env pwsh
# Verify prerequisites before any run.
$ErrorActionPreference = "Stop"

Write-Host "=== benchmark-cc setup check ===" -ForegroundColor Cyan

# claude
$ccVer = (claude --version 2>&1) -replace '[^\d\.].*$', ''
if (-not $ccVer) { throw "Claude Code not found. Install: https://docs.claude.com/claude-code" }
$ccVerObj = [version]($ccVer -split ' ')[0]
$minVer = [version]"2.1.119"
if ($ccVerObj -lt $minVer) {
    Write-Warning "Claude Code $ccVer < $minVer recommended. Known quality regression in 2.1.98-2.1.115. Proceed anyway? (Ctrl+C to abort)"
    Start-Sleep -Seconds 3
}
Write-Host "  claude: $ccVer OK"

# node
$nodeVer = node --version
if ([version]($nodeVer.TrimStart('v')) -lt [version]"20.0.0") {
    throw "Node.js 20+ required, found $nodeVer"
}
Write-Host "  node:   $nodeVer OK"

# git
$gitVer = (git --version) -replace '^git version ', ''
Write-Host "  git:    $gitVer OK"

# directories
$req = @("setups", "tasks", "results", "runs")
foreach ($d in $req) {
    if (-not (Test-Path $d)) { throw "Missing dir: $d. Run from repo root." }
}
Write-Host "  dirs:   OK"

# setups present
$setups = Get-ChildItem -Path setups -Directory | Select-Object -ExpandProperty Name
Write-Host "  setups: $($setups -join ', ')"

# tasks present
$tasks = Get-ChildItem -Path tasks -Directory | Select-Object -ExpandProperty Name
Write-Host "  tasks:  $($tasks -join ', ')"

Write-Host "`nReady. Run: ./runner.mjs --runner <yourname>" -ForegroundColor Green
