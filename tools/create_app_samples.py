import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, 'icons')
OUTPUT_DIR = os.path.join(ICONS_DIR, 'app-icons')

# Target Size: iPhone 12 Pro Max is 180x180 (@3x). 1024x1024 is App Store.
# User mentioned iPhone 12 Pro Max priority.
# Let's generate 1024x1024 for high res, and maybe result in better quality if downscaled later.
# But if source is 150x150, scaling to 1024 will be blurry.
# Best approach: Create 180x180 canvas, center the 150x150 icon (or resize slightly), white background.
# 150 is close to 180. 15px padding on each side.
# Let's try 180x180 first.
TARGET_SIZE = (180, 180)
BG_COLOR = (255, 255, 255, 255) # White

FILES_TO_PROCESS = [
    'icons/ui/home.png',
    'icons/system/dashboard.png',
    # We will add others later if approved
]

def create_app_icon(rel_path, save_dir):
    full_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        return

    try:
        img = Image.open(full_path).convert("RGBA")
        
        # Create new image
        new_img = Image.new("RGBA", TARGET_SIZE, BG_COLOR)
        
        # Center the icon
        # Calculate position to center
        # If icon is larger than target, resize it?
        # If icon is smaller, center it?
        
        # Source size
        w, h = img.size
        
        # If source is 1024 (AI generated), resize down to fit 180 with padding?
        # If source is 150 (standard here), center it.
        
        # Let's assume some padding is good. 10% padding?
        # Safe area for app icons is usually central.
        
        # Logic: 
        # 1. Resize source to be at most 80% of target? Or just use as is if it fits?
        # Use 150 inside 180 -> perfect fit with padding.
        
        if w > TARGET_SIZE[0] or h > TARGET_SIZE[1]:
            # Scale down
            ratio = min(TARGET_SIZE[0]/w, TARGET_SIZE[1]/h)
            new_w = int(w * ratio)
            new_h = int(h * ratio)
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Center position
        x = (TARGET_SIZE[0] - img.size[0]) // 2
        y = (TARGET_SIZE[1] - img.size[1]) // 2
        
        new_img.paste(img, (x, y), img)
        
        # Save
        filename = os.path.basename(rel_path)
        base_name = os.path.splitext(filename)[0]
        out_name = f"{base_name}-app.png"
        out_path = os.path.join(save_dir, out_name)
        
        new_img.save(out_path)
        print(f"Generated: {out_path}")
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
