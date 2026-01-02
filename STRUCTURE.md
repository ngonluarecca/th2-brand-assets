# Cấu trúc thư mục th2-brand-assets

## Sơ đồ cấu trúc hoàn chỉnh

```
th2-brand-assets/
│
├── 📁 logo/                          # Logo hệ thống
│   ├── th2-logo.svg                  # Logo chính
│   ├── th2-logo-white.svg            # Logo trắng (dark mode)
│   ├── th2-logo-mono.svg             # Logo mono
│   └── favicon.svg                   # Favicon
│
├── 📁 icons/                         # Icon theo module nghiệp vụ
│   ├── 📁 cutting/                   # Module Cutting
│   │   ├── scissors.svg
│   │   ├── fabric.svg
│   │   └── pattern.svg
│   │
│   ├── 📁 production/                # Module Production
│   │   ├── sewing-machine.svg
│   │   ├── quality-check.svg
│   │   └── production-line.svg
│   │
│   ├── 📁 hr/                        # Module HR
│   │   ├── users.svg
│   │   ├── employee-card.svg
│   │   └── attendance.svg
│   │
│   ├── 📁 warehouse/                 # Module Warehouse
│   │   ├── box.svg
│   │   ├── inventory.svg
│   │   └── delivery.svg
│   │
│   ├── 📁 finance/                   # Module Finance
│   │   ├── calculator.svg
│   │   ├── invoice.svg
│   │   └── chart.svg
│   │
│   └── 📁 system/                    # Module System
│       ├── settings.svg
│       ├── dashboard.svg
│       └── user-profile.svg
│
├── 📁 images/                        # Hình ảnh tĩnh
│   ├── 📁 banner/                    # Banner
│   │   ├── welcome-banner.svg
│   │   └── maintenance-banner.svg
│   │
│   ├── 📁 empty-state/               # Empty state
│   │   ├── no-data.svg
│   │   └── empty-list.svg
│   │
│   └── 📁 panel/                     # Panel
│       ├── info-panel.svg
│       └── warning-panel.svg
│
├── 📄 asset-map.json                 # Mapping KEY → CDN URL
├── 📄 generate-asset-map.js          # Script generate asset-map.json
├── 📄 README.md                      # Tài liệu chính
├── 📄 NAMING-CONVENTIONS.md          # Quy chuẩn đặt tên
├── 📄 VERSIONING.md                  # Quy trình versioning
├── 📄 STRUCTURE.md                   # File này
├── 📄 package.json                   # Package config
└── 📄 .gitignore                     # Git ignore rules
```

## Mô tả từng thư mục

### `/logo`
Chứa tất cả logo của hệ thống TH2:
- **th2-logo.svg**: Logo chính, dùng cho light mode
- **th2-logo-white.svg**: Logo trắng, dùng cho dark mode
- **th2-logo-mono.svg**: Logo mono (single color), dùng khi cần đổi màu
- **favicon.svg**: Favicon cho browser

### `/icons`
Chứa icon theo từng module nghiệp vụ. Mỗi module có thư mục riêng:
- **cutting/**: Icon cho module cắt vải
- **production/**: Icon cho module sản xuất
- **hr/**: Icon cho module nhân sự
- **warehouse/**: Icon cho module kho
- **finance/**: Icon cho module kế toán
- **system/**: Icon cho hệ thống chung

### `/images`
Chứa hình ảnh tĩnh dùng chung:
- **banner/**: Banner cho các trang
- **empty-state/**: Hình ảnh khi không có dữ liệu
- **panel/**: Hình ảnh cho các panel thông báo

## Quy tắc tổ chức

1. **Mỗi module có thư mục riêng** trong `/icons`
2. **File đặt tên kebab-case, không dấu**
3. **Không có file trùng tên** trong cùng thư mục
4. **SVG là format chính**, PNG chỉ dùng khi cần thiết

## Thêm asset mới

### Thêm icon mới
```bash
# Ví dụ: Thêm icon mới cho module cutting
# 1. Tạo file SVG
touch icons/cutting/new-icon.svg

# 2. Generate asset-map.json
node generate-asset-map.js v1.1.0

# 3. Commit và tag
git add .
git commit -m "feat: add new-icon for cutting module"
git tag v1.1.0
```

### Thêm module mới
```bash
# Ví dụ: Thêm module mới "quality"
# 1. Tạo thư mục
mkdir icons/quality

# 2. Thêm icon vào thư mục
touch icons/quality/check.svg

# 3. Generate và commit
node generate-asset-map.js v1.1.0
git add .
git commit -m "feat: add quality module icons"
git tag v1.1.0
```

## CDN URL Structure

Sau khi generate `asset-map.json`, cấu trúc CDN URL sẽ là:

```
https://cdn.jsdelivr.net/gh/[username]/th2-brand-assets@[version]/[path]
```

Ví dụ:
- Logo: `https://cdn.jsdelivr.net/gh/user/th2-brand-assets@v1.0.0/logo/th2-logo.svg`
- Icon: `https://cdn.jsdelivr.net/gh/user/th2-brand-assets@v1.0.0/icons/cutting/scissors.svg`
- Banner: `https://cdn.jsdelivr.net/gh/user/th2-brand-assets@v1.0.0/images/banner/welcome-banner.svg`

## Asset Map Structure

File `asset-map.json` có cấu trúc:

```json
{
  "version": "v1.0.0",
  "cdnBase": "https://cdn.jsdelivr.net/gh/...",
  "generatedAt": "2024-01-01T00:00:00.000Z",
  "logo": {
    "th2-logo": "https://cdn.jsdelivr.net/gh/.../logo/th2-logo.svg",
    ...
  },
  "icons": {
    "cutting": {
      "scissors": "https://cdn.jsdelivr.net/gh/.../icons/cutting/scissors.svg",
      ...
    },
    ...
  },
  "images": {
    "banner": {
      "welcome-banner": "https://cdn.jsdelivr.net/gh/.../images/banner/welcome-banner.svg",
      ...
    },
    ...
  }
}
```

## Maintenance

### Kiểm tra cấu trúc
```bash
# List tất cả file SVG
find . -name "*.svg" -type f

# Kiểm tra file trùng tên
find . -name "*.svg" -type f | xargs basename | sort | uniq -d
```

### Cleanup
```bash
# Xóa file placeholder (nếu cần)
# Chỉ xóa sau khi đã thay thế bằng file thật
```

