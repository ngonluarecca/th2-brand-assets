param (
    [Parameter(Mandatory=$true)]
    [string]$Version
)

$ErrorActionPreference = "Stop"
$AssetMapPath = Join-Path $PSScriptRoot "..\asset-map.json"

Write-Host "Starting Release Process for version: $Version" -ForegroundColor Cyan
Write-Host ""

# 1. Update asset-map.json
Write-Host "Updating asset-map.json..." -ForegroundColor Yellow

if (Test-Path $AssetMapPath) {
    $content = Get-Content $AssetMapPath -Raw
    
    $newVersionStr = '"version": "{0}"' -f $Version
    $newCdnBaseStr = '"cdnBase": "https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@{0}"' -f $Version
    $newUrlStr = 'jsdelivr.net/gh/ngonluarecca/th2-brand-assets@{0}' -f $Version
    $newDateStr = '"generatedAt": "{0}"' -f (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.000Z")

    $content = $content -replace '"version":\s*"v\d+\.\d+\.\d+"', $newVersionStr
    $content = $content -replace '"cdnBase":\s*".*?"', $newCdnBaseStr
    $content = $content -replace 'jsdelivr\.net/gh/ngonluarecca/th2-brand-assets@(v\d+\.\d+\.\d+|main)', $newUrlStr
    $content = $content -replace '"generatedAt":\s*".*?"', $newDateStr

    Set-Content -Path $AssetMapPath -Value $content -Encoding UTF8
    Write-Host "Updated version and URLs." -ForegroundColor Green
} else {
    Write-Host "Error: Asset map file not found." -ForegroundColor Red
    exit 1
}

Write-Host ""

# 2. Update Preview
Write-Host "Updating Preview HTML..." -ForegroundColor Yellow
$PreviewScript = Join-Path $PSScriptRoot "generate_preview.py"
py $PreviewScript
Write-Host "Preview updated." -ForegroundColor Green
Write-Host ""

# 3. Git Operations
if (-not (Test-Path ".git")) {
    Write-Host "Error: Not a git repository." -ForegroundColor Red
    exit 1
}

Write-Host "Git Status:" -ForegroundColor Yellow
git status --short

$proceed = Read-Host "Do you want to commit these changes and release $Version ? (y/n)"
if ($proceed -ne 'y') {
    Write-Host "Release cancelled." -ForegroundColor Red
    exit 0
}

Write-Host "Committing..." -ForegroundColor Yellow
git add .
git commit -m "chore(release): bump version to $Version"

Write-Host "Pushing to main..." -ForegroundColor Yellow
git push origin main

# Check if tag exists
if (git tag -l $Version) {
    Write-Host "Tag $Version already exists. Please delete it manualy or choose another version." -ForegroundColor Red
    exit 1
}

Write-Host "Creating Tag $Version..." -ForegroundColor Yellow
git tag $Version

Write-Host "Pushing Tag..." -ForegroundColor Yellow
git push origin $Version

Write-Host ""
Write-Host "Release $Version completed successfully!" -ForegroundColor Green
Write-Host "CDN URL: https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@$Version/asset-map.json" -ForegroundColor Cyan
