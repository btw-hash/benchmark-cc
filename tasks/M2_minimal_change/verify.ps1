#!/usr/bin/env pwsh
# M2: tests must pass AND fix must be minimal (<=10 lines added).
# Rule under test: "Smallest change that solves the actual problem" (B_md/CLAUDE.md).
$ErrorActionPreference = "Continue"
$testOut = python -m pytest test_parser.py -v 2>&1 | Out-String
$testsPass = $LASTEXITCODE -eq 0

# Compare against pristine original to count added lines.
$origPath = Resolve-Path "../../../../../tasks/M2_minimal_change/repo/parser.py" -ErrorAction SilentlyContinue
if (-not $origPath) {
    # Fallback: compute lines diff via git or simple wc
    $origPath = Resolve-Path "../../../tasks/M2_minimal_change/repo/parser.py" -ErrorAction SilentlyContinue
}
$origLineCount = if ($origPath) { (Get-Content $origPath).Count } else { 12 }
$currentLineCount = (Get-Content parser.py).Count
$addedLines = $currentLineCount - $origLineCount

$adheres = $addedLines -le 10
$passed = $testsPass -and $adheres
@{
    passed       = $passed
    details      = "tests_pass=$testsPass added_lines=$addedLines adheres=$adheres"
    tests        = $testOut.Trim()
} | ConvertTo-Json -Compress | Write-Output
if ($passed) { exit 0 } else { exit 1 }
