#!/usr/bin/env pwsh
# M5: cross-turn memory probe. Did the agent recall facts from turn 1 when writing notes.md in turn 2?
# This is a REAL multi-turn test (turn 2 invoked via --resume).
$ErrorActionPreference = "Continue"

if (-not (Test-Path notes.md)) {
    @{ passed = $false; details = "notes.md missing" } | ConvertTo-Json -Compress | Write-Output
    exit 1
}
$src = Get-Content notes.md -Raw

# Each fact = a separate check. All 5 must appear (case-insensitive substring match).
$facts = @(
    @{ name = "codename";    pattern = "saturn[\s-]?echo" }
    @{ name = "python_uv";   pattern = "\buv\b" }
    @{ name = "python_312";  pattern = "python\s*3\.?12|3\.12" }
    @{ name = "aws_arm64";   pattern = "aws\s*lambda|lambda.*arm64|arm64.*lambda" }
    @{ name = "epoch_time";  pattern = "epoch|unix\s*time|unix\s*timestamp" }
    @{ name = "pytest_hyp";  pattern = "hypothesis" }
)

$results = @{}
$score = 0
foreach ($f in $facts) {
    $found = $src -match $f.pattern
    $results[$f.name] = $found
    if ($found) { $score++ }
}

$passed = $score -ge 5  # tolerate 1 miss out of 6 (e.g. agent paraphrases "lambda" without "arm64")
@{
    passed  = $passed
    details = "recall_score=$score/6 " + (($results.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }) -join " ")
    notes_preview = $src.Substring(0, [Math]::Min(500, $src.Length))
} | ConvertTo-Json -Compress | Write-Output
if ($passed) { exit 0 } else { exit 1 }
