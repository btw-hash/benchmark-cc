#!/usr/bin/env pwsh
# T6: schema.prisma must validate AND have required structures.
$ErrorActionPreference = "Continue"

if (-not (Test-Path "node_modules")) {
    npm install --no-audit --no-fund 2>&1 | Out-Null
}

$validateOut = npx prisma validate --schema=schema.prisma 2>&1 | Out-String
$valid = $LASTEXITCODE -eq 0

$src = Get-Content schema.prisma -Raw
$hasPostModel        = $src -match "(?ms)^model\s+Post\s*\{"
$hasUserPostsField   = $src -match "posts\s+Post\["
$hasAuthorRelation   = $src -match "author\s+User\s+@relation"
$hasAuthorIdIndex    = $src -match "@@index\(\[authorId\]\)|@@index\(\[authorId,"
$hasPublishedIndex   = $src -match "@@index\(\[published\]\)|@@index\(\[published,"
$hasTimestamps       = ($src -match "createdAt\s+DateTime") -and ($src -match "updatedAt\s+DateTime")

$allChecks = $valid -and $hasPostModel -and $hasUserPostsField -and $hasAuthorRelation `
             -and $hasAuthorIdIndex -and $hasPublishedIndex -and $hasTimestamps

@{
    passed  = $allChecks
    details = "valid=$valid post_model=$hasPostModel user_posts_field=$hasUserPostsField author_relation=$hasAuthorRelation authorId_index=$hasAuthorIdIndex published_index=$hasPublishedIndex timestamps=$hasTimestamps"
    validate_output = $validateOut.Trim()
} | ConvertTo-Json -Compress | Write-Output
if ($allChecks) { exit 0 } else { exit 1 }
