#!/usr/bin/env pwsh
# Runs from the task's worktree dir. Returns 0 on pass, 1 on fail.
# Stdout contains JSON: { "passed": bool, "details": "..." }
$ErrorActionPreference = "Continue"
$out = python -m pytest test_moving_avg.py -v 2>&1 | Out-String
$passed = $LASTEXITCODE -eq 0
$result = @{
    passed  = $passed
    details = $out.Trim()
} | ConvertTo-Json -Compress
Write-Output $result
if ($passed) { exit 0 } else { exit 1 }
