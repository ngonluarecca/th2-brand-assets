import os
import collections
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, 'icons')

def rename_duplicates():
    files_map = collections.defaultdict(list)
    
    # categories
    categories = [d for d in os.listdir(ICONS_DIR) 
                 if os.path.isdir(os.path.join(ICONS_DIR, d)) 
                 and not d.startswith('.') and d != 'app-icons']
    
    for category in categories:
        cat_dir = os.path.join(ICONS_DIR, category)
        files = os.listdir(cat_dir)
        for f in files:
            if f.endswith('.png'):
                files_map[f].append(category)
                
    duplicates = {k: v for k, v in files_map.items() if len(v) > 1}
    
    if not duplicates:
        print("No duplicates found.")
        return

    print(f"Renaming {len(duplicates)} duplicates...")
    
    for filename, cats in duplicates.items():
        base_name = os.path.splitext(filename)[0]
        
        for category in cats:
            old_path = os.path.join(ICONS_DIR, category, filename)
            new_filename = f"{base_name}-{category}.png"
            new_path = os.path.join(ICONS_DIR, category, new_filename)
            
            # Rename
            shutil.move(old_path, new_path)
            print(f"Renamed: {category}/{filename} -> {category}/{new_filename}")

if __name__ == "__main__":
    rename_duplicates()
