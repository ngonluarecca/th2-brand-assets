# Script PowerShell để generate asset-map.json
# Mapping KEY → CDN URL (jsDelivr)
# 
# Usage: .\generate-asset-map.ps1 [version]
# Example: .\generate-asset-map.ps1 v1.0.0

param(
    [string]$Version = "v1.0.0"
)

$GithubUser = if ($env:GITHUB_USER) { $env:GITHUB_USER } else { "ngonluarecca" }
$RepoName = "th2-brand-assets"
$CdnBase = "https://cdn.jsdelivr.net/gh/$GithubUser/$RepoName@$Version"
$RootDir = $PSScriptRoot

# Function to convert file path to kebab-case key
function Convert-PathToKey {
    param([string]$FilePath)
    
    $key = $FilePath -replace '\\', '/' `
                    -replace '\.(svg|png|jpg|jpeg|webp)$', '' `
                    -replace '^logo/', '' `
                    -replace '^icons/', '' `
                    -replace '^images/', ''
    
    $parts = $key -split '/'
    return ($parts | Where-Object { $_ }) -join '.'
}

# Function to scan directory and build asset map
function Scan-Directory {
    param(
        [string]$Dir,
        [string]$BaseDir,
        [hashtable]$Map = @{}
    )
    
    if (-not (Test-Path $Dir)) {
        return $Map
    }
    
    $entries = Get-ChildItem -Path $Dir -Recurse -File
    
    foreach ($entry in $entries) {
        $ext = [System.IO.Path]::GetExtension($entry.Name).ToLower()
        
        if ($ext -in @('.svg', '.png', '.jpg', '.jpeg', '.webp')) {
            # Get relative path from base directory
            $relativePath = $entry.FullName.Substring($BaseDir.Length + 1) -replace '\\', '/'
            
            # Determine the base path prefix (logo/, icons/, images/)
            $basePath = ""
            if ($BaseDir -like "*\logo" -or $BaseDir -like "*/logo") {
                $basePath = "logo/"
            } elseif ($BaseDir -like "*\icons" -or $BaseDir -like "*/icons") {
                $basePath = "icons/"
            } elseif ($BaseDir -like "*\images" -or $BaseDir -like "*/images") {
                $basePath = "images/"
            }
            
            $fullPath = $basePath + $relativePath
            $cdnUrl = "$CdnBase/$fullPath"
            
            # Build nested structure
            $parts = $relativePath -split '/'
            $current = $Map
            
            # Navigate/create nested structure
            for ($i = 0; $i -lt ($parts.Length - 1); $i++) {
                $part = $parts[$i] -replace '\.(svg|png|jpg|jpeg|webp)$', ''
                
                if (-not $current.ContainsKey($part)) {
                    $current[$part] = @{}
                }
                $current = $current[$part]
            }
            
            # Add file
            $fileName = [System.IO.Path]::GetFileNameWithoutExtension($entry.Name)
            $current[$fileName] = $cdnUrl
        }
    }
    
    return $Map
}

# Main function
function Generate-AssetMap {
    $assetMap = @{
        version = $Version
        cdnBase = $CdnBase
        generatedAt = (Get-Date -Format "yyyy-MM-ddTHH:mm:ss.fffZ")
        logo = @{}
        icons = @{}
        images = @{}
    }
    
    # Scan logo directory
    $logoDir = Join-Path $RootDir "logo"
    if (Test-Path $logoDir) {
        $assetMap.logo = Scan-Directory -Dir $logoDir -BaseDir $logoDir
    }
    
    # Scan icons directory
    $iconsDir = Join-Path $RootDir "icons"
    if (Test-Path $iconsDir) {
        $assetMap.icons = Scan-Directory -Dir $iconsDir -BaseDir $iconsDir
    }
    
    # Scan images directory
    $imagesDir = Join-Path $RootDir "images"
    if (Test-Path $imagesDir) {
        $assetMap.images = Scan-Directory -Dir $imagesDir -BaseDir $imagesDir
    }
    
    # Convert hashtable to JSON
    $json = $assetMap | ConvertTo-Json -Depth 10
    
    # Write to file
    $outputPath = Join-Path $RootDir "asset-map.json"
    $json | Out-File -FilePath $outputPath -Encoding UTF8
    
    Write-Host "✅ Generated asset-map.json" -ForegroundColor Green
    Write-Host "   Version: $Version" -ForegroundColor Cyan
    Write-Host "   CDN Base: $CdnBase" -ForegroundColor Cyan
    Write-Host "   Output: $outputPath" -ForegroundColor Cyan
}

# Run
try {
    Generate-AssetMap
} catch {
    Write-Host "❌ Error generating asset-map.json: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

