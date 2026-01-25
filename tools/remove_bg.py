from PIL import Image
import os
import glob

def remove_white_background(input_path, output_path, tolerance=20):
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            # Check if pixel is close to white
            if item[0] > 255 - tolerance and item[1] > 255 - tolerance and item[2] > 255 - tolerance:
                new_data.append((255, 255, 255, 0)) # Make it transparent
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Processed: {os.path.basename(input_path)}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
import sys

if len(sys.argv) > 1:
    SOURCE_DIR = sys.argv[1]
else:
    SOURCE_DIR = "icons/png_concept"

files = glob.glob(os.path.join(SOURCE_DIR, "*.png"))

print(f"Found {len(files)} images to process...")
for f in files:
    remove_white_background(f, f)
print("Background removal complete.")
