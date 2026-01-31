import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, 'icons')
OUTPUT_DIR = os.path.join(ICONS_DIR, 'app-icons')

TARGET_SIZE = (180, 180)
BG_COLOR = (255, 255, 255, 255) # White

FILES_TO_PROCESS = [
    'icons/admin/report.png',
    'icons/cutting/cutting-operation.png',
    'icons/cutting/red-scissors.png',
    'icons/hr/profile.png',
    'icons/hr/users.png',
    'icons/production/output-report.png',
    'icons/production/production-report.png',
    'icons/system/dashboard.png',
    'icons/ui/home.png',
    'icons/warehouse/inventory-report.png'
]

def create_app_icon(rel_path, save_dir):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return

    try:
        img = Image.open(full_path).convert("RGBA")
        
        # Trim transparent pixels to get actual icon content
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            
        new_img = Image.new("RGBA", TARGET_SIZE, BG_COLOR)
        
        # Resize logic: Fit inside 156x156 to leave 12px padding
        # 180 - 156 = 24 => 12px padding
        INNER_SIZE = (156, 156)
        
        img.thumbnail(INNER_SIZE, Image.Resampling.LANCZOS)
        
        # Center position
        x = (TARGET_SIZE[0] - img.size[0]) // 2
        y = (TARGET_SIZE[1] - img.size[1]) // 2
        
        new_img.paste(img, (x, y), img)
        
        # Filename: original-app.png
        filename = os.path.basename(rel_path)
        base_name = os.path.splitext(filename)[0]
        out_name = f"{base_name}-app.png"
        out_path = os.path.join(save_dir, out_name)
        
        new_img.save(out_path)
        print(f"Generated: {out_name}")
        return out_path
        
    except Exception as e:
        print(f"Error processing {rel_path}: {e}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for p in FILES_TO_PROCESS:
        create_app_icon(p, OUTPUT_DIR)

if __name__ == "__main__":
    main()
