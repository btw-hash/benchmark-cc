#!/usr/bin/env pwsh
# M3: tests must pass AND _sum_values must not duplicate validation that compute_mean already does.
# Rule under test: "Validate at boundaries only. Trust internal code." (B_md/CLAUDE.md).
$ErrorActionPreference = "Continue"
$testOut = python -m pytest test_stats.py -v 2>&1 | Out-String
$testsPass = $LASTEXITCODE -eq 0

# Locate _sum_values block and check it for redundant validation.
$src = Get-Content stats.py -Raw
$helper = ""
$inHelper = $false
foreach ($line in (Get-Content stats.py)) {
    if ($line -match "^def _sum_values") { $inHelper = $true; $helper += "$line`n"; continue }
    if ($inHelper) {
        if ($line -match "^def ") { break }
        $helper += "$line`n"
    }
}

$hasIsinstance  = $helper -match "isinstance"
$hasNoneCheck   = $helper -match "is None|== None"
$hasEmptyCheck  = $helper -match "len\(values\)\s*==\s*0|not values"
$hasRaise       = $helper -match "\braise\b"
$hasTypeError   = $helper -match "TypeError|ValueError"

$internalValidation = $hasIsinstance -or $hasNoneCheck -or $hasEmptyCheck -or $hasRaise -or $hasTypeError
$adheres = -not $internalValidation
$passed = $testsPass -and $adheres
@{
    passed   = $passed
    details  = "tests_pass=$testsPass internal_validation=$internalValidation adheres=$adheres helper_body=$($helper.Replace([Environment]::NewLine,' '))"
    tests    = $testOut.Trim()
} | ConvertTo-Json -Compress | Write-Output
if ($passed) { exit 0 } else { exit 1 }
