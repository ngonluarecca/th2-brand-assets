import os
import shutil
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(BASE_DIR, 'icons')
TEMP_DIRS = ['temp_review', 'temp_final']

# Category Mappings
# Dictionary format: 'filename_pattern': 'destination_folder'
# Keys can be exact names (without extension) or regex? Let's use exact names or startswith for simplicity, 
# but mostly exact mapping based on our analysis.

CATEGORY_MAP = {
    # UI
    'add': 'ui', 'edit': 'ui', 'delete': 'ui', 'close': 'ui', 'check': 'ui',
    'next': 'ui', 'previous': 'ui', 'back': 'ui', 'plus': 'ui', 'minus': 'ui',
    'undo': 'ui', 'redo': 'ui', 'home': 'ui', 'menu': 'ui', 'settings': 'system', # Settings moved to system as per existing
    'female-avatar': 'ui', 'male-avatar': 'ui',
    'camera': 'ui', 'qr-code': 'ui',
    'info-panel': 'ui', 'warning-panel': 'ui', 'empty-list': 'ui', 
    'no-data': 'ui', 'maintenance-banner': 'ui', 'welcome-banner': 'ui',
    
    # Documents
    'folder': 'documents', 'video': 'documents',
    'training-docs': 'documents', 'training_docs': 'documents',
    
    # Finance
    'bank_statement': 'finance', 'bank-statement': 'finance',
    'income_expense': 'finance', 'income-expense': 'finance',
    'purchase_invoice': 'finance', 'purchase-invoice': 'finance',
    'vat_invoice': 'finance', 'vat-invoice': 'finance',
    'calculator': 'finance',
    
    # HR
    'calendar': 'hr', 'employee': 'hr', 'payroll': 'hr', 'task': 'hr', 'timekeeping': 'hr',
    'profile': 'hr', 'profile_resume': 'hr', 'profile-resume': 'hr',
    
    # Sales
    'customer': 'sales', 'delivery': 'sales', 'order': 'sales', 'product': 'sales', 'sales': 'sales',
    'sales-detail': 'sales', 'sales_detail': 'sales',
    'survey': 'sales', 'survey-form': 'sales', 'survey_form': 'sales',
    'supplier': 'sales', # Supplier is often 'purchase' or 'sales', let's check asset map. 'supplier' was in 'sales' in previous map. Wait, usually supplier is purchase.
    # In provided asset-map.json: "supplier": ".../temp_review/supplier.png" inside "sales" category? 
    # Actually lines 6-15 in old map had "supplier" in "sales". Okay.
    
    # Production
    'production-log': 'production', 'production_log': 'production',
    'production-plan': 'production', 'production_plan': 'production',
    'output-report': 'production', 'output_report': 'production',
    'inventory-report': 'production', 'inventory_report': 'production',
    'shipping-info': 'production', 'shipping_info': 'production',
    'weight-scale': 'production', 'weight_scale': 'production',
    'production-line': 'production', 'quality-check': 'production', 
    'sewing-machine': 'production', 'fabric': 'production', 'pattern': 'production',
    
    # Cutting
    'cutting-operation': 'cutting', 'cutting_operation': 'cutting',
    'scissors': 'cutting',
    
    # Warehouse
    'inventory': 'warehouse', 'box': 'warehouse',
    
    # System
    'dashboard': 'system', 'database': 'system', 'workflow': 'system',
    'purchasing': 'finance', # Or purchase? There is a 'purchase' folder.
}

# Special handling for 'purchase' category which exists in directory structure but maybe mixed in map.
# Let's verify 'purchase' folder items.
# 'purchasing', 'purchase-detail', 'purchase_detail', 'supplier'
# In standard business, supplier is purchase. I will move them to 'purchase' folder if it fits better, 
# but user wants to match asset-map? 
# The user said "bổ sung nếu cái nào còn thiếu", "cho đồng nhất".
# I'll stick to 'purchase' folder for purchase items if they exist.
CATEGORY_MAP.update({
    'purchasing': 'purchase',
    'purchase-detail': 'purchase', 'purchase_detail': 'purchase',
    'supplier': 'purchase', # Moving supplier to purchase where it belongs logically
    'provider': 'purchase', # If exists
})

def to_kebab_case(name):
    # Replace underscore with hyphen
    return name.replace('_', '-')

def main():
    # Ensure target dirs exist
    target_dirs = ['ui', 'documents', 'finance', 'hr', 'sales', 'production', 'cutting', 'warehouse', 'system', 'purchase']
    for d in target_dirs:
        path = os.path.join(ICONS_DIR, d)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {d}")

    moved_count = 0
    
    for temp_dir_name in TEMP_DIRS:
        temp_path = os.path.join(ICONS_DIR, temp_dir_name)
        if not os.path.exists(temp_path):
            continue
            
        files = os.listdir(temp_path)
        for f in files:
            if not f.lower().endswith('.png'):
                continue
                
            name_no_ext = os.path.splitext(f)[0]
            
            # Determine category
            category = CATEGORY_MAP.get(name_no_ext)
            
            # If not in map, try to guess or leave it?
            # Startswith check for variations
            if not category:
                if 'purchase' in name_no_ext: category = 'purchase'
                elif 'sales' in name_no_ext: category = 'sales'
                elif 'production' in name_no_ext: category = 'production'
                elif 'inventory' in name_no_ext: category = 'production' # or warehouse
            
            if not category:
                print(f"Skipping unknown file: {f}")
                continue
                
            # Target name (kebab-case)
            new_name = to_kebab_case(name_no_ext) + '.png'
            dest_dir = os.path.join(ICONS_DIR, category)
            dest_path = os.path.join(dest_dir, new_name)
            
            src_path = os.path.join(temp_path, f)
            
            # Move (Copy then delete to be safe, or just move)
            # shutil.move(src_path, dest_path) 
            # Use copy2 to preserve metadata, allow overwrite
            shutil.copy2(src_path, dest_path)
            print(f"Moved {f} -> {category}/{new_name}")
            moved_count += 1
            
            # Remove original if successful
            os.remove(src_path)

    print(f"Total moved: {moved_count}")
    
    # Cleanup empty temp dirs
    for temp_dir_name in TEMP_DIRS:
        temp_path = os.path.join(ICONS_DIR, temp_dir_name)
        if os.path.exists(temp_path) and not os.listdir(temp_path):
            os.rmdir(temp_path)
            print(f"Removed empty directory: {temp_dir_name}")

if __name__ == "__main__":
    main()
