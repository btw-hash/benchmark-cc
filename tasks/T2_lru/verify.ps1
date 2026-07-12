#!/usr/bin/env pwsh
$ErrorActionPreference = "Continue"
$out = (npm test 2>&1) | Out-String
$passed = $LASTEXITCODE -eq 0
@{ passed = $passed; details = $out.Trim() } | ConvertTo-Json -Compress | Write-Output
if ($passed) { exit 0 } else { exit 1 }
