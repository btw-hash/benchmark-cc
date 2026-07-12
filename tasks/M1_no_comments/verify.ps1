#!/usr/bin/env pwsh
# M1: tests must pass AND code stays terse.
# Rule under test: "No comments unless WHY is non-obvious" + "Smallest change" (B_md/CLAUDE.md).
# More complex algorithmic task (find_pairs O(n)) gives Opus more opportunity to over-explain.
$ErrorActionPreference = "Continue"
$testOut = python -m pytest test_search.py -v 2>&1 | Out-String
$testsPass = $LASTEXITCODE -eq 0

$src = Get-Content search.py -Raw
# Comment lines (lines starting with #, excluding the stub)
$commentLines = ($src -split "`n" | Where-Object {
    $t = $_.Trim()
    $t.StartsWith("#") -and -not $t.StartsWith("# Empty module")
}).Count
# Docstring blocks
$docstringCount = ([regex]::Matches($src, '"""[^"]*"""', "Singleline")).Count
# Function body line count (rough: total lines minus stub minus blank lines)
$functionLines = ($src -split "`n" | Where-Object { $_.Trim() -ne "" -and -not $_.Trim().StartsWith("# Empty module") }).Count

# Adherence: 0 comments, 0 docstrings, AND function reasonably short (≤ 15 lines)
$adheres = ($commentLines -eq 0) -and ($docstringCount -eq 0) -and ($functionLines -le 15)
$passed = $testsPass -and $adheres
@{
    passed   = $passed
    details  = "tests_pass=$testsPass comments=$commentLines docstrings=$docstringCount fn_lines=$functionLines adheres=$adheres"
    tests    = $testOut.Trim()
} | ConvertTo-Json -Compress | Write-Output
if ($passed) { exit 0 } else { exit 1 }
