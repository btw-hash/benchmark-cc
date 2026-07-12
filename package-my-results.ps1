#!/usr/bin/env pwsh
# After running runner.mjs, packages YOUR results to send back.
# Use this if you're the second runner (friend) sending back to whoever gave you the zip.

param(
    [Parameter(Mandatory=$true)] [string]$Runner
)

$ErrorActionPreference = "Stop"

if ($Runner -notmatch "^[a-z0-9_-]+$") {
    throw "Runner name must be lowercase alphanumeric (got: $Runner)"
}

$resultFile = "results/runs_${Runner}.jsonl"
if (-not (Test-Path $resultFile)) {
    throw "No $resultFile found. Run 'node runner.mjs --runner $Runner --samples 5' first."
}

$rowCount = (Get-Content $resultFile).Count
Write-Host "Found $rowCount runs in $resultFile" -ForegroundColor Green

$outName = "benchmark-results-${Runner}.zip"
$outPath = "../$outName"

# Bundle: results jsonl + runs artifacts (diffs + streams)
$paths = @($resultFile)
if (Test-Path "runs/$Runner") {
    $paths += "runs/$Runner"
}

if (Test-Path $outPath) { Remove-Item $outPath }
Compress-Archive -Path $paths -DestinationPath $outPath -Force

$size = [math]::Round((Get-Item $outPath).Length / 1MB, 2)
Write-Host ""
Write-Host "Created: $outPath ($size MB)" -ForegroundColor Green
Write-Host "Send this back to whoever shared the benchmark with you." -ForegroundColor Cyan
