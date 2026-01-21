import os
import glob
from pathlib import Path

# Configuration
ROOT_DIR = Path(__file__).parent.parent
Preview_File = ROOT_DIR / "preview_all.html"
ASSET_DIRS = ["icons", "images", "logo"]

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TH2 Brand Assets Preview</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f5f5f5; padding: 20px; }
        h1 { color: #333; }
        h2 { color: #555; border-bottom: 2px solid #ddd; padding-bottom: 10px; margin-top: 30px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 20px; }
        .card { background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; transition: transform 0.2s; }
        .card:hover { transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.15); }
        .img-container { height: 120px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; background-image: linear-gradient(45deg, #eee 25%, transparent 25%), linear-gradient(-45deg, #eee 25%, transparent 25%), linear-gradient(45deg, transparent 75%, #eee 75%), linear-gradient(-45deg, transparent 75%, #eee 75%); background-size: 20px 20px; background-position: 0 0, 0 10px, 10px -10px, -10px 0px; }
        img { max-width: 100%; max-height: 100%; }
        .name { font-size: 14px; color: #666; word-break: break-word; }
        .path { font-size: 11px; color: #999; margin-top: 5px; }
        .badge { display: inline-block; padding: 2px 6px; border-radius: 4px; font-size: 10px; font-weight: bold; margin-bottom: 5px; }
        .badge-icon { background: #e3f2fd; color: #1565c0; }
        .badge-image { background: #e8f5e9; color: #2e7d32; }
        .badge-logo { background: #fff3e0; color: #ef6c00; }
    </style>
</head>
<body>
    <h1>TH2 Brand Assets Library</h1>
    <p>Generated index of all available assets.</p>
"""

HTML_FOOTER = """
    <script>
        // Simple search functionality could be added here
    </script>
</body>
</html>
"""

def generate_html():
    html_content = HTML_HEADER
    
    for category in ASSET_DIRS:
        category_path = ROOT_DIR / category
        if not category_path.exists():
            continue
            
        html_content += f"<h2>{category.upper()}</h2>"
        
        # Get all subdirectories
        subdirs = [x for x in category_path.iterdir() if x.is_dir()]
        
        # Also check root of category
        root_files = list(category_path.glob("*.png"))
        if root_files:
            html_content += f"<h3>/</h3>"
            html_content += '<div class="grid">'
            for file_path in root_files:
                rel_path = file_path.relative_to(ROOT_DIR)
                html_content += create_card(file_path, rel_path, category)
            html_content += '</div>'

        for subdir in subdirs:
            html_content += f"<h3>{subdir.name}</h3>"
            html_content += '<div class="grid">'
            files = list(subdir.glob("*.png"))
            for file_path in files:
                rel_path = file_path.relative_to(ROOT_DIR)
                html_content += create_card(file_path, rel_path, category)
            html_content += '</div>'
            
    html_content += HTML_FOOTER
    
    with open(Preview_File, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Preview generated at: {Preview_File}")

def create_card(file_path, rel_path, category):
    name = file_path.name
    badge_class = f"badge-{category}" if category in ["icons", "images", "logo"] else "badge-icon"
    
    # Use relative path for src so it works locally
    return f"""
        <div class="card">
            <span class="badge {badge_class}">{category}</span>
            <div class="img-container">
                <img src="{rel_path}" alt="{name}" loading="lazy">
            </div>
            <div class="name">{name}</div>
            <div class="path">{rel_path}</div>
        </div>
    """

if __name__ == "__main__":
    generate_html()
