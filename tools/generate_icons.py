import os

OUTPUT_DIR = "icons/review_batch"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Common Design Tokens
STROKE_COLOR = "#000000"
STROKE_WIDTH = "4"
STROKE_LINECAP = "round" 
STROKE_LINEJOIN = "round"

# Palette
COLORS = {
    "yellow": "#FFD700", # Gold
    "orange": "#FFA500",
    "blue": "#87CEEB", # SkyBlue
    "green": "#90EE90", # LightGreen
    "red": "#FF6B6B",
    "brown": "#D2B48C", # Tan
    "purple": "#CE93D8",
    "gray": "#E0E0E0",
    "white": "#FFFFFF"
}

def create_svg(filename, content):
    svg_template = f"""<svg width="150" height="150" viewBox="0 0 150 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .stroke-main {{ fill: none; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-yellow {{ fill: {COLORS['yellow']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-orange {{ fill: {COLORS['orange']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-blue {{ fill: {COLORS['blue']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-green {{ fill: {COLORS['green']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-red {{ fill: {COLORS['red']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-brown {{ fill: {COLORS['brown']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-purple {{ fill: {COLORS['purple']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-gray {{ fill: {COLORS['gray']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
      .fill-white {{ fill: {COLORS['white']}; stroke: {STROKE_COLOR}; stroke-width: {STROKE_WIDTH}; stroke-linecap: {STROKE_LINECAP}; stroke-linejoin: {STROKE_LINEJOIN}; }}
    </style>
  </defs>
  <g transform="translate(15, 15) scale(0.8)"> <!-- Padding 15px, Scale to fit 120x120 content box -->
    {content}
  </g>
</svg>"""
    
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg_template)
    print(f"Generated {filename}")

# --- Icon Definitions (Batch 1 & 2 & 3 Sample) ---

# 1. Khách hàng (Person/User) - Blue shirt
icon_khach_hang = """
  <!-- Body -->
  <path d="M75 120 C75 120 110 120 110 90 C110 70 95 70 95 70" class="stroke-main" /> <!-- Right Shoulder Partial -->
  <path d="M75 120 C75 120 40 120 40 90 C40 70 55 70 55 70" class="stroke-main" /> <!-- Left Shoulder Partial -->
  <path d="M30 130 Q75 140 120 130 L120 100 Q110 110 75 110 Q40 110 30 100 Z" class="fill-blue" /> <!-- Shirt Base -->
  <circle cx="75" cy="50" r="25" class="fill-yellow" /> <!-- Head -->
"""

# 2. Bán hàng (Shopping Cart) - Orange/Green
icon_ban_hang = """
  <path d="M10 20 L30 20 L45 90 H110 L125 40 H35" class="fill-orange" />
  <circle cx="50" cy="110" r="10" class="fill-gray" />
  <circle cx="105" cy="110" r="10" class="fill-gray" />
"""

# 3. Chi tiết bán hàng (Bill/List) - White paper, Blue header
icon_chi_tiet_ban_hang = """
  <rect x="35" y="10" width="80" height="110" rx="5" class="fill-white" />
  <line x1="50" y1="30" x2="100" y2="30" class="stroke-main" />
  <line x1="50" y1="50" x2="100" y2="50" class="stroke-main" />
  <line x1="50" y1="70" x2="80" y2="70" class="stroke-main" />
  <rect x="90" y="80" width="30" height="30" rx="2" class="fill-green" /> <!-- Small stamp/check -->
"""

# 4. Đơn hàng (Clipboard) - Brown board, White paper
icon_don_hang = """
  <rect x="30" y="20" width="90" height="110" rx="5" class="fill-brown" />
  <rect x="40" y="30" width="70" height="90" class="fill-white" />
  <rect x="55" y="10" width="40" height="15" rx="2" class="fill-gray" /> <!-- Clip -->
  <line x1="50" y1="50" x2="100" y2="50" class="stroke-main" />
  <line x1="50" y1="70" x2="100" y2="70" class="stroke-main" />
  <line x1="50" y1="90" x2="80" y2="90" class="stroke-main" />
"""

# 5. Nhà cung cấp (Truck) - Blue/Red
icon_nha_cung_cap = """
  <rect x="10" y="40" width="80" height="60" class="fill-blue" />
  <rect x="90" y="60" width="40" height="40" class="fill-blue" />
  <circle cx="35" cy="110" r="12" class="fill-gray" />
  <circle cx="105" cy="110" r="12" class="fill-gray" />
  <rect x="95" y="65" width="25" height="15" class="fill-white" /> <!-- Window -->
"""

# 6. Sản phẩm (Box) - Brown
icon_san_pham = """
  <path d="M25 40 L75 15 L125 40 L125 95 L75 120 L25 95 Z" class="fill-brown" />
  <path d="M25 40 L75 65 L125 40" class="stroke-main" />
  <path d="M75 65 L75 120" class="stroke-main" />
"""

# 7. Mua hàng (Basket) - Red
icon_mua_hang = """
  <path d="M20 50 L130 50 L110 110 H40 L20 50 Z" class="fill-red" />
  <path d="M40 50 A 35 35 0 0 1 110 50" class="stroke-main" /> <!-- Handle -->
  <line x1="20" y1="50" x2="130" y2="50" class="stroke-main" />
  <line x1="45" y1="50" x2="55" y2="110" class="stroke-main" />
  <line x1="75" y1="50" x2="75" y2="110" class="stroke-main" />
  <line x1="105" y1="50" x2="95" y2="110" class="stroke-main" />
"""

# 8. Training Docs (Graduation Cap + Books) - Yellow Cap, Colored Books
icon_training_docs = """
  <!-- Books Stack -->
  <path d="M30 90 L120 90 L120 105 L30 105 Z" class="fill-blue" />
  <path d="M30 105 L120 105 L120 120 L30 120 Z" class="fill-green" />
  <path d="M30 120 L120 120 L120 135 L30 135 Z" class="fill-orange" />
  
  <!-- Content lines on books spine -->
  <line x1="105" y1="90" x2="105" y2="135" class="stroke-main" /> 
  <line x1="95" y1="95" x2="95" y2="100" class="stroke-main" />
  <line x1="95" y1="110" x2="95" y2="115" class="stroke-main" />
  <line x1="95" y1="125" x2="95" y2="130" class="stroke-main" />

  <!-- Graduation Cap -->
  <path d="M25 45 L75 25 L125 45 L75 65 Z" class="fill-yellow" />
  <path d="M125 45 L125 65" class="stroke-main" /> <!-- Tassel Holder -->
  <circle cx="125" cy="70" r="5" class="fill-red" /> <!-- Tassel end -->
  <path d="M45 55 L45 75 A 30 10 0 0 0 105 75 L105 55" class="fill-yellow" /> <!-- Cap Body -->
"""

# 9. Hóa đơn (Invoice) - Similar to Bill but with dollar sign
icon_hoa_don = """
  <rect x="35" y="10" width="80" height="110" rx="5" class="fill-white" />
  <circle cx="75" cy="65" r="20" class="fill-green" />
  <path d="M75 55 V75 M70 55 H78 M70 75 H78 M70 65 H80" class="stroke-main" /> <!-- Fake Dollar -->
  <line x1="50" y1="95" x2="100" y2="95" class="stroke-main" />
"""

# Check for Batch 3 placeholders roughly
icon_nhan_vien = """
  <rect x="40" y="40" width="70" height="90" rx="5" class="fill-white" /> <!-- Card -->
  <path d="M60 40 V20 H90 V40" class="stroke-main" /> <!-- Strap -->
  <circle cx="75" cy="70" r="15" class="fill-gray" /> <!-- Photo -->
  <line x1="55" y1="100" x2="95" y2="100" class="stroke-main" />
"""

icon_cham_cong = """
  <rect x="25" y="30" width="100" height="90" rx="5" class="fill-white" />
  <path d="M25 50 H125" class="stroke-main" />
  <path d="M45 20 V40" class="stroke-main" />
  <path d="M105 20 V40" class="stroke-main" />
  <circle cx="75" cy="85" r="5" class="fill-red" /> <!-- Date marker -->
"""

# Execute Generation
create_svg("KhachHang.svg", icon_khach_hang)
create_svg("BanHang.svg", icon_ban_hang)
create_svg("ChiTietBanHang.svg", icon_chi_tiet_ban_hang)
create_svg("DonHang.svg", icon_don_hang)
create_svg("NhaCungCap.svg", icon_nha_cung_cap)
create_svg("SanPham.svg", icon_san_pham)
create_svg("MuaHang.svg", icon_mua_hang)
create_svg("TrainingDocs.svg", icon_training_docs)
create_svg("HoaDon.svg", icon_hoa_don)
create_svg("NhanVien.svg", icon_nhan_vien)
create_svg("ChamCong.svg", icon_cham_cong)
create_svg("Lich.svg", icon_cham_cong) # Lich similar to ChamCong
