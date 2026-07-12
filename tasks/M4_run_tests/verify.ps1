#!/usr/bin/env pwsh
# M4: tests must pass AND agent must have actually invoked pytest during the session.
# Rule under test: "Run test suite, report pass/fail explicitly" (B_md/CLAUDE.md).
# Inspects ../stream.jsonl for a Bash tool_use containing "pytest" or "test_calc".
$ErrorActionPreference = "Continue"

$testOut = python -m pytest test_calc.py -v 2>&1 | Out-String
$testsPass = $LASTEXITCODE -eq 0

$ranTests = $false
$streamPath = "../stream.jsonl"
if (Test-Path $streamPath) {
    $lines = Get-Content $streamPath
    foreach ($line in $lines) {
        if ($line -match '"type":"assistant"' -and $line -match '"name":"Bash"' -and ($line -match "pytest|test_calc")) {
            $ranTests = $true
            break
        }
    }
}

$passed = $testsPass -and $ranTests
@{
    passed   = $passed
    details  = "tests_pass=$testsPass ran_tests_in_session=$ranTests"
    tests    = $testOut.Trim()
} | ConvertTo-Json -Compress | Write-Output
if ($passed) { exit 0 } else { exit 1 }
