#!/usr/bin/env node

/**
 * Script để generate asset-map.json
 * Mapping KEY → CDN URL (jsDelivr)
 * 
 * Usage: node generate-asset-map.js [version]
 * Example: node generate-asset-map.js v1.0.0
 */

const fs = require('fs');
const path = require('path');

// Lấy version từ argument hoặc từ package.json hoặc default
const version = process.argv[2] || process.env.VERSION || 'v1.0.0';
const githubUser = process.env.GITHUB_USER || 'ngonluarecca';
const repoName = 'th2-brand-assets';

// Base CDN URL
const CDN_BASE = `https://cdn.jsdelivr.net/gh/${githubUser}/${repoName}@${version}`;

/**
 * Convert file path to kebab-case key
 */
function pathToKey(filePath) {
  return filePath
    .replace(/\\/g, '/')
    .replace(/\.(svg|png|jpg|jpeg|webp)$/i, '')
    .split('/')
    .filter(Boolean)
    .join('.');
}

/**
 * Recursively scan directory and build asset map
 */
function scanDirectory(dir, baseDir, map = {}) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    const relativePath = path.relative(baseDir, fullPath).replace(/\\/g, '/');

    if (entry.isDirectory()) {
      // Recursively scan subdirectories
      scanDirectory(fullPath, baseDir, map);
    } else if (entry.isFile()) {
      // Only process image files
      const ext = path.extname(entry.name).toLowerCase();
      if (['.svg', '.png', '.jpg', '.jpeg', '.webp'].includes(ext)) {
        const key = pathToKey(relativePath);
        const cdnUrl = `${CDN_BASE}/${relativePath}`;
        
        // Build nested structure
        const parts = relativePath.split('/');
        let current = map;
        
        // Skip filename for nesting
        for (let i = 0; i < parts.length - 1; i++) {
          const part = parts[i].replace(/\.(svg|png|jpg|jpeg|webp)$/i, '');
          if (!current[part]) {
            current[part] = {};
          }
          current = current[part];
        }
        
        // Add file
        const fileName = path.basename(relativePath, ext);
        current[fileName] = cdnUrl;
      }
    }
  }

  return map;
}

/**
 * Main function
 */
function generateAssetMap() {
  const rootDir = __dirname;
  const assetMap = {
    version,
    cdnBase: CDN_BASE,
    generatedAt: new Date().toISOString(),
    logo: {},
    icons: {},
    images: {}
  };

  // Scan logo directory
  const logoDir = path.join(rootDir, 'logo');
  if (fs.existsSync(logoDir)) {
    assetMap.logo = scanDirectory(logoDir, logoDir);
  }

  // Scan icons directory
  const iconsDir = path.join(rootDir, 'icons');
  if (fs.existsSync(iconsDir)) {
    assetMap.icons = scanDirectory(iconsDir, iconsDir);
  }

  // Scan images directory
  const imagesDir = path.join(rootDir, 'images');
  if (fs.existsSync(imagesDir)) {
    assetMap.images = scanDirectory(imagesDir, imagesDir);
  }

  // Write to file
  const outputPath = path.join(rootDir, 'asset-map.json');
  fs.writeFileSync(
    outputPath,
    JSON.stringify(assetMap, null, 2),
    'utf8'
  );

  console.log(`✅ Generated asset-map.json`);
  console.log(`   Version: ${version}`);
  console.log(`   CDN Base: ${CDN_BASE}`);
  console.log(`   Output: ${outputPath}`);
}

// Run
try {
  generateAssetMap();
} catch (error) {
  console.error('❌ Error generating asset-map.json:', error.message);
  process.exit(1);
}

