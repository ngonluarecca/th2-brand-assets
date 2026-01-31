import os
import collections

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, 'icons')

def scan_duplicates():
    files_map = collections.defaultdict(list)
    
    # categories
    categories = [d for d in os.listdir(ICONS_DIR) 
                 if os.path.isdir(os.path.join(ICONS_DIR, d)) 
                 and not d.startswith('.') and d != 'app-icons'] # Exclude app-icons from "conflict" check? Or include?
                 # App icons have -app suffix usually, so they won't conflict with source unless source has -app suffix.
                 # User said "tìm kiếm dễ dàng", implies searching by name.
                 # Let's exclude app-icons from renaming logic for now, or check them separately.
                 # Actually, let's include all to see what's what.
    
    for category in categories:
        cat_dir = os.path.join(ICONS_DIR, category)
        files = os.listdir(cat_dir)
        for f in files:
            if f.endswith('.png'):
                files_map[f].append(category)
                
    duplicates = {k: v for k, v in files_map.items() if len(v) > 1}
    
    if not duplicates:
        print("No duplicates found.")
    else:
        print(f"Found {len(duplicates)} duplicate filenames:")
        for filename, cats in duplicates.items():
            print(f"  {filename}: {', '.join(cats)}")

if __name__ == "__main__":
    scan_duplicates()
