$OutputDir = "icons\review_batch"
if (-not (Test-Path -Path $OutputDir)) {
    New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
}

# --- Design System V2: Soft Lineal Color ---
$StrokeColor = "#1A1A1A" # Darker black-gray for softer contrast
$StrokeWidth = "4.5"     # Bold stroke
$StrokeLinecap = "round"
$StrokeLinejoin = "round"

# Pastel Palette (Backgrounds) & Vivid Accents
$Colors = @{
    "blue_bg" = "#E1F5FE"; "blue_accent" = "#4FC3F7"
    "green_bg" = "#E8F5E9"; "green_accent" = "#81C784"
    "yellow_bg" = "#FFFDE7"; "yellow_accent" = "#FDD835"
    "orange_bg" = "#FFF3E0"; "orange_accent" = "#FFB74D"
    "red_bg" = "#FFEBEE"; "red_accent" = "#E57373"
    "purple_bg" = "#F3E5F5"; "purple_accent" = "#BA68C8"
    "gray_bg" = "#F5F5F5"; "gray_accent" = "#9E9E9E"
    "white" = "#FFFFFF"
}

function Create-Svg {
    param (
        [string]$Filename,
        [string]$Content
    )

    $SvgTemplate = @"
<svg width="150" height="150" viewBox="0 0 150 150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      /* Base Stroke Style */
      path, circle, rect, line, polyline, ellipse, polygon {
        stroke: $StrokeColor;
        stroke-width: $StrokeWidth;
        stroke-linecap: $StrokeLinecap;
        stroke-linejoin: $StrokeLinejoin;
        fill: none; /* Default no fill */
      }
      /* Fills */
      .bg-blue { fill: $($Colors["blue_bg"]); }
      .bg-green { fill: $($Colors["green_bg"]); }
      .bg-yellow { fill: $($Colors["yellow_bg"]); }
      .bg-orange { fill: $($Colors["orange_bg"]); }
      .bg-red { fill: $($Colors["red_bg"]); }
      .bg-purple { fill: $($Colors["purple_bg"]); }
      .bg-gray { fill: $($Colors["gray_bg"]); }
      .bg-white { fill: $($Colors["white"]); }

      /* Accents (Stronger Colors) */
      .accent-blue { fill: $($Colors["blue_accent"]); }
      .accent-green { fill: $($Colors["green_accent"]); }
      .accent-yellow { fill: $($Colors["yellow_accent"]); }
      .accent-orange { fill: $($Colors["orange_accent"]); }
      .accent-red { fill: $($Colors["red_accent"]); }
      .accent-purple { fill: $($Colors["purple_accent"]); }
      .accent-gray { fill: $($Colors["gray_accent"]); }
      
      /* Utilities */
      .no-stroke { stroke: none; }
      .fill-none { fill: none; }
    </style>
  </defs>
  <g transform="translate(15, 15) scale(0.8)">
    $Content
  </g>
</svg>
"@
    
    $FilePath = Join-Path $OutputDir $Filename
    Set-Content -Path $FilePath -Value $SvgTemplate -Encoding UTF8
    Write-Host "Generated $Filename"
}

# --- BATCH 1: CORE / SALES ---

# KhachHang: Avatar Profile with verified badge
Create-Svg "KhachHang.svg" @"
  <!-- Background Shape/Card -->
  <rect x="20" y="20" width="110" height="110" rx="15" class="bg-blue" />
  <!-- Person -->
  <path d="M75 110 C75 110 105 110 105 90 C105 70 95 70 95 70" class="bg-white" />
  <path d="M75 110 C75 110 45 110 45 90 C45 70 55 70 55 70" class="bg-white" />
  <path d="M35 130 C35 130 75 135 115 130 L115 90 C105 100 75 100 45 90 L35 130 Z" class="accent-blue" />
  <circle cx="75" cy="55" r="22" class="bg-yellow" />
  <!-- Badge -->
  <circle cx="110" cy="110" r="15" class="accent-yellow" />
  <path d="M103 110 L108 115 L117 106" class="fill-none" />
"@

# BanHang: Shopping Cart with Items
Create-Svg "BanHang.svg" @"
  <circle cx="75" cy="75" r="55" class="bg-orange no-stroke" opacity="0.2" />
  <path d="M20 30 H40 L55 95 H115 L130 45 H50" class="bg-white" />
  <path d="M60 45 L60 30 L80 15 L100 30 L100 45" class="accent-green" /> <!-- Item inside -->
  <circle cx="65" cy="115" r="10" class="bg-gray" />
  <circle cx="110" cy="115" r="10" class="bg-gray" />
"@

# DonHang: Clipboard with Checkmarks (Detailed)
Create-Svg "DonHang.svg" @"
  <rect x="30" y="20" width="90" height="110" rx="8" class="bg-white" />
  <path d="M50 20 V10 H100 V20" class="accent-orange" /> <!-- Top Clip -->
  <circle cx="75" cy="15" r="3" class="fill-none" />
  
  <!-- Content Lines -->
  <rect x="45" y="40" width="15" height="15" rx="3" class="accent-green" />
  <path d="M48 48 L50 51 L56 44" class="fill-none" stroke="white" stroke-width="3" />
  <line x1="70" y1="48" x2="105" y2="48" />
  
  <rect x="45" y="65" width="15" height="15" rx="3" class="accent-green" />
  <path d="M48 73 L50 76 L56 69" class="fill-none" stroke="white" stroke-width="3" />
  <line x1="70" y1="73" x2="105" y2="73" />
  
  <rect x="45" y="90" width="15" height="15" rx="3" class="bg-gray" />
  <line x1="70" y1="98" x2="90" y2="98" />
"@

# ChiTietBanHang: Receipt/Bill
Create-Svg "ChiTietBanHang.svg" @"
  <rect x="35" y="15" width="80" height="120" rx="5" class="bg-white" />
  <path d="M35 115 L45 125 L55 115 L65 125 L75 115 L85 125 L95 115 L105 125 L115 115" class="bg-white" /> <!-- Jagged edge -->
  <line x1="50" y1="40" x2="100" y2="40" stroke-width="6" class="accent-blue no-stroke" /> <!-- Header bar -->
  <line x1="50" y1="60" x2="100" y2="60" />
  <line x1="50" y1="80" x2="100" y2="80" />
  <line x1="50" y1="100" x2="80" y2="100" />
  <rect x="90" y="95" width="10" height="10" class="accent-red" />
"@


# --- BATCH 2: SUPPLY CHAIN ---

# NhaCungCap: Detailed Factory
Create-Svg "NhaCungCap.svg" @"
  <!-- Factory Body -->
  <path d="M20 120 V60 L50 40 L50 60 L80 40 L80 60 L110 40 L110 120 H20 Z" class="bg-blue" />
  <!-- Windows -->
  <rect x="35" y="80" width="20" height="20" class="accent-blue" />
  <rect x="75" y="80" width="20" height="20" class="accent-blue" />
  <!-- Chimney & Smoke -->
  <rect x="110" y="50" width="20" height="70" class="accent-gray" />
  <path d="M110 50 H130" />
  <path d="M115 20 C115 20 110 10 130 10 C140 10 145 20 135 30" class="bg-white" opacity="0.8" />
"@

# GiaoHang: Delivery Truck (Fast)
Create-Svg "GiaoHang.svg" @"
  <!-- Truck Body -->
  <path d="M10 60 H90 V100 H10 V60 Z" class="accent-orange" />
  <path d="M90 75 H120 L135 100 H90 V60" class="bg-yellow" />
  <!-- Wheels -->
  <circle cx="35" cy="100" r="14" class="bg-gray" />
  <circle cx="105" cy="100" r="14" class="bg-gray" />
  <circle cx="35" cy="100" r="5" class="fill-none" />
  <circle cx="105" cy="100" r="5" class="fill-none" />
  <!-- Motion Lines -->
  <path d="M5 70 H-10 M5 80 H-15" stroke-dasharray="5 5" />
"@

# SanPham: Open Box with Item
Create-Svg "SanPham.svg" @"
  <!-- Back Flap -->
  <path d="M25 50 L75 20 L125 50" class="bg-orange" /> 
  <!-- Product Inside -->
  <circle cx="75" cy="50" r="20" class="accent-green" />
  <!-- Front Box -->
  <path d="M25 50 V110 L75 130 L125 110 V50 L75 70 L25 50 Z" class="accent-orange" />
  <path d="M75 70 V130" />
"@

# MuaHang: Shopping Basket
Create-Svg "MuaHang.svg" @"
  <path d="M20 60 L30 120 H120 L130 60 H20 Z" class="bg-red" />
  <path d="M25 60 H125" class="fill-none" stroke-width="2" />
  <path d="M40 120 V60 M75 120 V60 M110 120 V60" class="fill-none" opacity="0.3" />
  <!-- Handle -->
  <path d="M40 60 C40 20 110 20 110 60" class="fill-none" stroke-width="6" />
"@

# ChiTietMuaHang: Similar to ChiTietBanHang but Green
Create-Svg "ChiTietMuaHang.svg" @"
  <rect x="35" y="15" width="80" height="120" rx="5" class="bg-white" />
  <line x1="50" y1="40" x2="100" y2="40" stroke-width="6" class="accent-green no-stroke" />
  <line x1="50" y1="60" x2="100" y2="60" />
  <line x1="50" y1="80" x2="100" y2="80" />
  <circle cx="95" cy="100" r="12" class="accent-red" />
  <path d="M90 95 L100 105 M100 95 L90 105" class="fill-none" stroke="white" stroke-width="3" />
"@

# HoaDon: Invoice with $
Create-Svg "HoaDon.svg" @"
  <rect x="30" y="15" width="90" height="120" rx="5" class="bg-yellow" />
  <circle cx="75" cy="60" r="25" class="accent-green" />
  <text x="65" y="70" font-family='Arial' font-size='30' font-weight='bold' fill='white' stroke='none'>$</text>
  <line x1="50" y1="100" x2="100" y2="100" />
  <line x1="50" y1="115" x2="80" y2="115" />
"@

# HoaDonVAT: Invoice with %
Create-Svg "HoaDonVAT.svg" @"
  <rect x="30" y="15" width="90" height="120" rx="5" class="bg-red" /> <!-- Red for VAT -->
  <rect x="55" y="45" width="40" height="40" class="bg-white" />
  <text x="60" y="75" font-family='Arial' font-size='30' font-weight='bold' fill='black' stroke='none'>%</text>
  <line x1="50" y1="100" x2="100" y2="100" stroke="white" />
"@

# --- BATCH 3: HR & STAFF ---

# NhanVien: ID Card
Create-Svg "NhanVien.svg" @"
  <rect x="35" y="30" width="80" height="100" rx="8" class="bg-white" />
  <path d="M55 30 V10 H95 V30" class="accent-blue" stroke-width="6" /> <!-- Lanyard -->
  <circle cx="75" cy="65" r="20" class="bg-gray" /> <!-- Photo -->
  <path d="M60 85 C60 85 90 85 90 85" opacity="0.5" />
  <rect x="50" y="100" width="50" height="10" class="accent-blue" rx="2" stroke="none" />
"@

# ChamCong: Calendar/Clock Hybrid
Create-Svg "ChamCong.svg" @"
  <rect x="25" y="30" width="100" height="100" rx="10" class="bg-white" />
  <path d="M25 60 H125" class="fill-none" />
  <path d="M45 20 V40 M105 20 V40" class="accent-red" stroke-width="6" />
  <!-- Clock Face -->
  <circle cx="75" cy="95" r="25" class="accent-yellow" />
  <path d="M75 95 V85 M75 95 L82 95" class="fill-none" />
"@

# Lich: Calendar
Create-Svg "Lich.svg" @"
  <rect x="25" y="30" width="100" height="100" rx="10" class="bg-white" />
  <path d="M25 60 H125" class="fill-none" />
  <path d="M25 30 H125 V60 H25 Z" class="accent-red" stroke="none" /> <!-- Red Header -->
  <path d="M25 30 H125 V60 H25 Z" class="fill-none" /> <!-- Header outline -->
  <path d="M45 20 V40 M105 20 V40" class="fill-none" stroke-width="6" stroke="#1A1A1A" />
  
  <rect x="45" y="80" width="15" height="15" class="bg-gray" stroke="none" rx="2" />
  <rect x="70" y="80" width="15" height="15" class="bg-gray" stroke="none" rx="2" />
  <rect x="95" y="80" width="15" height="15" class="accent-green" stroke="none" rx="2" /> <!-- Marked day -->
  <rect x="45" y="105" width="15" height="15" class="bg-gray" stroke="none" rx="2" />
"@

# BangLuong: Money Envelope
Create-Svg "BangLuong.svg" @"
  <rect x="20" y="40" width="110" height="70" rx="5" class="bg-green" />
  <path d="M20 40 L75 80 L130 40" class="fill-none" />
  <circle cx="75" cy="80" r="15" class="accent-yellow" />
  <text x="68" y="88" font-family='Arial' font-size='20' font-weight='bold' fill='#1A1A1A' stroke='none'>$</text>
"@

# TrainingDocs: Books & Cap (Detailed)
Create-Svg "TrainingDocs.svg" @"
  <!-- Bottom Book -->
  <path d="M30 130 H120 C125 130 125 115 120 115 H30 V130 Z" class="bg-red" />
  <!-- Middle Book -->
  <path d="M30 115 H120 C125 115 125 100 120 100 H30 V115 Z" class="bg-blue" />
  <!-- Top Book -->
  <path d="M30 100 H120 C125 100 125 85 120 85 H30 V100 Z" class="bg-green" />
  
  <!-- Content Lines -->
  <line x1="35" y1="122" x2="110" y2="122" stroke-width="2" class="fill-none" opacity="0.3" />
  <line x1="35" y1="107" x2="110" y2="107" stroke-width="2" class="fill-none" opacity="0.3" />

  <!-- Graduation Cap -->
  <path d="M20 50 L75 25 L130 50 L75 75 Z" class="accent-yellow" />
  <path d="M40 60 V75 C40 85 110 85 110 75 V60" class="bg-yellow" />
  <path d="M130 50 V70" />
  <circle cx="130" cy="75" r="5" class="accent-red" />
"@

# HoSo: Folder
Create-Svg "HoSo.svg" @"
  <path d="M20 40 L60 40 L75 30 H130 V120 H20 Z" class="bg-orange" />
  <rect x="40" y="60" width="70" height="40" class="bg-white" />
  <line x1="50" y1="75" x2="100" y2="75" />
  <line x1="50" y1="90" x2="80" y2="90" />
"@


# --- BATCH 4: PRODUCTION ---

# NhatKySanXuat: Clipboard with Gear
Create-Svg "NhatKySanXuat.svg" @"
  <rect x="30" y="20" width="90" height="110" rx="8" class="bg-gray" />
  <circle cx="75" cy="75" r="30" class="accent-orange" /> <!-- Gear Body -->
  <circle cx="75" cy="75" r="10" class="bg-white" /> <!-- Gear Hole -->
  <path d="M75 40 V50 M75 100 V110 M40 75 H50 M100 75 H110" stroke-width="6" /> <!-- Gear Teeth hint -->
  <path d="M75 20 V10 H90" class="fill-none" /> <!-- Hook -->
"@

# KeHoachSanXuat: Calendar with Chart
Create-Svg "KeHoachSanXuat.svg" @"
  <rect x="20" y="20" width="110" height="110" rx="8" class="bg-white" />
  <path d="M20 50 H130" />
  <path d="M20 20 H130 V50 H20 Z" class="accent-blue no-stroke" />
  <path d="M20 20 H130 V50 H20 Z" class="fill-none" />
  <path d="M40 10 V30 M110 10 V30" stroke-width="6" />
  
  <!-- Chart Bars -->
  <rect x="40" y="80" width="15" height="30" class="bg-blue" stroke="none" />
  <rect x="65" y="60" width="15" height="50" class="accent-blue" stroke="none" />
  <rect x="90" y="90" width="15" height="20" class="bg-blue" stroke="none" />
  <path d="M35 110 H115" />
"@

# QuanLyTacNghiepCat: Scissors
Create-Svg "QuanLyTacNghiepCat.svg" @"
  <circle cx="50" cy="100" r="20" class="bg-gray" />
  <circle cx="100" cy="100" r="20" class="bg-gray" />
  <path d="M65 85 L110 30" stroke-width="8" class="fill-none" />
  <path d="M85 85 L40 30" stroke-width="8" class="fill-none" />
  <circle cx="75" cy="70" r="6" class="accent-red" />
"@

# BaoCaoSanLuong: Line Chart with Dots
Create-Svg "BaoCaoSanLuong.svg" @"
  <rect x="20" y="20" width="110" height="110" rx="5" class="bg-white" />
  <polyline points="40,100 60,70 90,80 110,40" stroke="red" stroke-width="5" class="fill-none" />
  <circle cx="40" cy="100" r="4" class="accent-blue" stroke="none"/>
  <circle cx="60" cy="70" r="4" class="accent-blue" stroke="none"/>
  <circle cx="90" cy="80" r="4" class="accent-blue" stroke="none"/>
  <circle cx="110" cy="40" r="4" class="accent-blue" stroke="none"/>
  
  <line x1="30" y1="110" x2="120" y2="110" />
  <line x1="30" y1="110" x2="30" y2="30" />
"@

# QuanLyMaCan: Scale
Create-Svg "QuanLyMaCan.svg" @"
  <path d="M30 100 L120 100 L110 120 H40 L30 100 Z" class="bg-gray" />
  <rect x="70" y="50" width="10" height="50" class="accent-gray" />
  <path d="M20 50 H130" stroke-width="6" />
  <path d="M20 50 L40 80 M130 50 L110 80" />
  <circle cx="75" cy="50" r="5" class="fill-white" />
"@

# --- BATCH 5: SYSTEM & ADMIN ---

# CaiDat: Cog/Settings
Create-Svg "CaiDat.svg" @"
  <circle cx="75" cy="75" r="35" class="bg-gray" />
  <circle cx="75" cy="75" r="15" class="bg-white" />
  <!-- Teeth -->
  <path d="M75 25 V40" stroke-width="12" />
  <path d="M75 110 V125" stroke-width="12" />
  <path d="M25 75 H40" stroke-width="12" />
  <path d="M110 75 H125" stroke-width="12" />
  <path d="M40 40 L50 50" stroke-width="12" />
  <path d="M100 100 L110 110" stroke-width="12" />
  <path d="M110 40 L100 50" stroke-width="12" />
  <path d="M50 100 L40 110" stroke-width="12" />
"@

# Database: Server Rack
Create-Svg "Database.svg" @"
  <path d="M35 30 H115 V120 H35 Z" class="bg-white" /> <!-- Rack -->
  <rect x="45" y="40" width="60" height="20" rx="3" class="accent-blue" />
  <rect x="45" y="70" width="60" height="20" rx="3" class="accent-blue" />
  <rect x="45" y="100" width="60" height="20" rx="3" class="accent-blue" />
  <circle cx="55" cy="50" r="3" class="bg-white" stroke="none" />
  <circle cx="55" cy="80" r="3" class="bg-white" stroke="none" />
  <circle cx="55" cy="110" r="3" class="bg-white" stroke="none" />
"@

# Dashboard: Computer Monitor with Pie Chart
Create-Svg "Dashboard.svg" @"
  <!-- Monitor Stand -->
  <path d="M50 125 H100 L95 105 H55 Z" class="bg-gray" />
  <!-- Screen -->
  <rect x="15" y="25" width="120" height="80" rx="5" class="bg-white" />
  <!-- Pie Chart -->
  <circle cx="55" cy="65" r="25" class="accent-orange" />
  <path d="M55 65 L55 40 A 25 25 0 0 1 80 65 Z" class="accent-green" /> <!-- Segment -->
  <!-- Bar Chart -->
  <rect x="95" y="55" width="10" height="20" class="accent-blue" stroke="none" />
  <rect x="110" y="45" width="10" height="30" class="accent-blue" stroke="none" />
  <path d="M90 75 H125" />
"@

# QuyTrinh: Flowchart
Create-Svg "QuyTrinh.svg" @"
  <rect x="20" y="60" width="35" height="30" rx="3" class="accent-blue" />
  <rect x="95" y="60" width="35" height="30" rx="3" class="accent-green" />
  <line x1="55" y1="75" x2="95" y2="75" stroke-dasharray="5 5" />
  <path d="M85 65 L95 75 L85 85" class="fill-none" />
"@

# Video: Play Button/Screen
Create-Svg "Video.svg" @"
  <rect x="20" y="35" width="110" height="80" rx="10" class="accent-red" />
  <path d="M65 55 L95 75 L65 95 Z" class="bg-white" />
"@

# ThuMuc: Folder
Create-Svg "ThuMuc.svg" @"
  <path d="M20 40 L60 40 L75 30 H130 V120 H20 Z" class="bg-yellow" />
"@

# CongViec: Tasks
Create-Svg "CongViec.svg" @"
  <rect x="30" y="20" width="90" height="110" rx="5" class="bg-white" />
  <line x1="45" y1="40" x2="105" y2="40" class="accent-gray" stroke-width="4" />
  <line x1="45" y1="60" x2="105" y2="60" class="accent-gray" stroke-width="4" />
  <path d="M45 90 L60 105 L105 50" class="fill-none" stroke="green" stroke-width="6" /> <!-- Big Check -->
"@

# ThuChi: Dollar Up/Down
Create-Svg "ThuChi.svg" @"
  <circle cx="75" cy="75" r="50" class="bg-white" />
  <text x="65" y="85" font-family='Arial' font-size='40' font-weight='bold' fill='#1A1A1A' stroke='none'>$</text>
  
  <path d="M130 40 V90" stroke="green" stroke-width="5" />
  <path d="M130 40 L115 55 M130 40 L145 55" stroke="green" stroke-width="5" /> <!-- Up -->

  <path d="M20 60 V110" stroke="red" stroke-width="5" />
  <path d="M20 110 L5 95 M20 110 L35 95" stroke="red" stroke-width="5" /> <!-- Down -->
"@

# ThongTinVanChuyen: Map Pin
Create-Svg "ThongTinVanChuyen.svg" @"
  <path d="M75 125 C75 125 35 70 35 50 A 40 40 0 0 1 115 50 C115 70 75 125 75 125 Z" class="accent-red" />
  <circle cx="75" cy="50" r="15" class="bg-white" />
"@

# BaoCaoNXT: Bar Chart (Detailed)
Create-Svg "BaoCaoNXT.svg" @"
  <rect x="25" y="30" width="100" height="100" rx="5" class="bg-white" />
  <rect x="35" y="60" width="15" height="60" class="accent-blue" stroke="none" />
  <rect x="67" y="40" width="15" height="80" class="accent-green" stroke="none" />
  <rect x="100" y="80" width="15" height="40" class="accent-orange" stroke="none" />
  <path d="M25 120 H125" />
"@

# ShaoSat: Question Mark Form
Create-Svg "KhaoSat.svg" @"
   <rect x="35" y="20" width="80" height="110" rx="5" class="bg-white" />
   <circle cx="75" cy="60" r="20" class="accent-blue" />
   <text x="68" y="70" font-family='Arial' font-size='30' font-weight='bold' fill='white' stroke='none'>?</text>
   
   <rect x="45" y="95" width="25" height="15" class="accent-green" rx="2" stroke="none" /> <!-- Yes -->
   <rect x="80" y="95" width="25" height="15" class="accent-red" rx="2" stroke="none" /> <!-- No -->
"@

# PhieuKhaoSat: Checklist
Create-Svg "PhieuKhaoSat.svg" @"
   <rect x="35" y="20" width="80" height="110" rx="5" class="bg-white" />
   <line x1="50" y1="40" x2="100" y2="40" stroke-width="4" />
   
   <rect x="50" y="60" width="12" height="12" class="fill-none" /> 
   <line x1="70" y1="66" x2="100" y2="66" />
   
   <rect x="50" y="80" width="12" height="12" class="fill-none" /> 
   <line x1="70" y1="86" x2="100" y2="86" />
   
   <path d="M52 84 L56 88 L60 81" class="fill-none" stroke="green" /> <!-- Tick -->
"@

# SaoKeNganHang: Bank Statement
Create-Svg "SaoKeNganHang.svg" @"
   <rect x="20" y="30" width="110" height="90" rx="5" class="bg-white" />
   <path d="M20 50 H130" />
   <path d="M30 40 L50 40 L60 30 H100" class="accent-green" stroke="none" /> <!-- Bank Logo hint -->
   <path d="M30 40 L50 40 L60 30 H100" class="fill-none" />
   
   <line x1="30" y1="70" x2="120" y2="70" />
   <line x1="30" y1="90" x2="80" y2="90" />
   <text x="90" y="95" font-family='Arial' font-size='20' font-weight='bold' stroke='none' fill='red'>-$$</text>
"@

Write-Host "Done generating Soft Lineal Color icons."
