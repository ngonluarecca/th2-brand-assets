import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, 'icons')
ASSET_MAP_FILE = os.path.join(BASE_DIR, 'asset-map.json')

NEW_VERSION = "v2.1.0"
CDN_BASE = f"https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@{NEW_VERSION}"

def main():
    # Read existing map
    with open(ASSET_MAP_FILE, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        
    # Update Metadata
    data['version'] = NEW_VERSION
    data['cdnBase'] = CDN_BASE
    data['generatedAt'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')
    
    # Scan Icons
    icons_map = {}
    
    # Get all subdirectories in icons/
    categories = [d for d in os.listdir(ICONS_DIR) 
                 if os.path.isdir(os.path.join(ICONS_DIR, d)) 
                 and not d.startswith('.') and d != 'temp_review' and d != 'temp_final']
    
    categories.sort()
    
    for category in categories:
        cat_dir = os.path.join(ICONS_DIR, category)
        icons_map[category] = {}
        
        files = sorted(os.listdir(cat_dir))
        for filename in files:
            if not filename.lower().endswith('.png'):
                continue
                
            name = os.path.splitext(filename)[0]
            # Construct URL
            # Note: Using forward slashes for URL
            url = f"{CDN_BASE}/icons/{category}/{filename}"
            icons_map[category][name] = url
            
    data['icons'] = icons_map
    
    # Update Logos (Keep existing logic but update version in URLs)
    if 'logo' in data:
        for key, url in data['logo'].items():
            # Replace old version with new version in URL
            # Regex or simple replace? Simple replace if structure is consistent.
            # Assuming format ...@{VERSION}/...
            import re
            new_url = re.sub(r'@[^/]+/', f'@{NEW_VERSION}/', url)
            data['logo'][key] = new_url

    # Write back
    with open(ASSET_MAP_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"Updated {ASSET_MAP_FILE} to version {NEW_VERSION}")
    print(f"Total categories: {len(icons_map)}")

if __name__ == "__main__":
    main()
