#!/usr/bin/env pwsh
# Copies your live ~/.claude into setups/G_<runner>_personal/.claude/
# Run BEFORE runner.mjs if you want your personal config in the comparison matrix.
#
# Usage: ./bootstrap-personal.ps1 -Runner alice
#
# Privacy: by default the resulting folder is gitignored. You can opt-in to
# committing it (so friend can also run AGAINST your config) via:
#   ./bootstrap-personal.ps1 -Runner alice -Commit
# This will scan for secrets first and prompt before committing.

param(
    [Parameter(Mandatory=$true)] [string]$Runner,
    [switch]$Commit
)

$ErrorActionPreference = "Stop"

if ($Runner -notmatch "^[a-z0-9_-]+$") {
    throw "Runner name must be lowercase alphanumeric (got: $Runner)"
}

$dst = "setups/G_${Runner}_personal/.claude"
$src = "$env:USERPROFILE\.claude"

if (-not (Test-Path $src)) {
    throw "$src not found. Run 'claude' once to initialize."
}

Write-Host "Bootstrapping personal setup G_${Runner}_personal..." -ForegroundColor Cyan

if (Test-Path $dst) {
    Write-Host "  removing existing $dst"
    Remove-Item -Recurse -Force $dst
}
New-Item -ItemType Directory -Path $dst -Force | Out-Null

# Copy what's relevant for benchmark; skip runtime state
$include = @("CLAUDE.md", "settings.json", "agents", "skills", "hooks", "projects")
foreach ($item in $include) {
    $itemSrc = "$src\$item"
    if (Test-Path $itemSrc) {
        if ((Get-Item $itemSrc) -is [System.IO.DirectoryInfo]) {
            Copy-Item $itemSrc $dst -Recurse
        } else {
            Copy-Item $itemSrc $dst
        }
        Write-Host "  + $item"
    }
}

# Strip transient stuff from projects/ (keep only memory/*.md and CLAUDE.md files)
$proj = "$dst\projects"
if (Test-Path $proj) {
    Get-ChildItem $proj -Recurse -File | Where-Object {
        $_.Name -notmatch '\.md$' -and $_.Name -ne 'MEMORY.md'
    } | Remove-Item -Force -ErrorAction SilentlyContinue
    Get-ChildItem $proj -Recurse -Directory | Where-Object {
        @($_.GetFiles("*.md")).Count -eq 0
    } | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
}

# Scan for secrets
Write-Host ""
Write-Host "Scanning for secrets in $dst..." -ForegroundColor Yellow
$secretPatterns = "sk-ant-oat01-[A-Za-z0-9_-]{40,}|sk-ant-ort01-[A-Za-z0-9_-]{40,}|sk-proj-[A-Za-z0-9_-]{40,}|ntn_[A-Za-z0-9]{40,}|ghp_[A-Za-z0-9]{36}|gho_[A-Za-z0-9]{36}|AKIA[0-9A-Z]{16}|-----BEGIN[A-Z ]*PRIVATE KEY-----"
$leaks = Select-String -Path "$dst\*","$dst\**\*" -Pattern $secretPatterns -List 2>$null
if ($leaks) {
    Write-Host "SECRETS FOUND in personal setup:" -ForegroundColor Red
    $leaks | ForEach-Object { Write-Host "  ! $($_.Path)" -ForegroundColor Red }
    Write-Host "Delete those files before committing, or run without -Commit (folder is gitignored by default)." -ForegroundColor Red
    if ($Commit) {
        throw "Refusing to commit with detected secrets."
    }
} else {
    Write-Host "  no secret patterns detected"
}

if ($Commit) {
    Write-Host ""
    Write-Host "Committing $dst (you opted in via -Commit)" -ForegroundColor Yellow
    Write-Host "Friend will be able to clone and run against your personal config." -ForegroundColor Yellow
    $confirm = Read-Host "Type 'yes' to confirm"
    if ($confirm -ne "yes") {
        Write-Host "Aborted. Folder remains local-only (gitignored)." -ForegroundColor Yellow
        exit 0
    }
    git add -f $dst
    git commit -m "personal: add G_${Runner}_personal config"
    Write-Host "Committed. Don't forget 'git push'." -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Setup is local-only (gitignored)." -ForegroundColor Green
    Write-Host "Re-run with -Commit if you want to share it via the private repo." -ForegroundColor Gray
}

Write-Host ""
Write-Host "Now run: node runner.mjs --runner $Runner --samples 5" -ForegroundColor Cyan
