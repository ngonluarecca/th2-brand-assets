# TH2 Brand Assets

Repository tập trung quản lý tất cả logo, icon, và hình ảnh tĩnh cho hệ thống TH2.

## 📋 Mục đích

Repo này cung cấp:
- **Logo** cho toàn hệ thống (main, mark, white, mono, favicon)
- **Icon** thống nhất theo module nghiệp vụ
- **Hình ảnh** tĩnh (banner, empty state, panel)
- **CDN URLs** qua jsDelivr để sử dụng trong web forms, AppSheet, và dashboard

## 🚀 Cách sử dụng

### Lấy link jsDelivr

#### Cách 1: Dùng asset-map.json (Khuyến nghị)

```javascript
// Fetch asset map từ CDN
const assetMap = await fetch('https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/asset-map.json')
  .then(res => res.json());

// Sử dụng
const logoUrl = assetMap.logo.main;
const cuttingIcon = assetMap.icons.cutting.scissors;
```

#### Cách 2: Link trực tiếp

Format: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@[version]/[path]`

Ví dụ:
- Logo chính: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo.svg`
- Logo mark: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo-mark.svg`
- Icon cutting: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/icons/cutting/scissors.svg`

#### Cách 3: Dùng trong HTML/React

```html
<!-- HTML -->
<img src="https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo.svg" alt="TH2 Logo" />
```

```jsx
// React
<img src={`https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo.svg`} alt="TH2 Logo" />
```

### Versioning

Repo sử dụng Git tags để versioning:
- `v1.0.0` - Version đầu tiên
- `v1.1.0` - Thêm icon mới, không breaking change
- `v2.0.0` - Thay đổi logo lớn, breaking change

**Luôn pin version cụ thể trong production!**

## 📁 Cấu trúc thư mục

```
th2-brand-assets/
├── logo/
│   ├── th2-logo.svg          # Logo chính (có text "THÁI HÀ GARMENT")
│   ├── th2-logo-mark.svg     # Logo mark (chỉ TH với thread/needle, không text)
│   ├── th2-logo-white.svg    # Logo trắng (dark mode/glass door)
│   ├── th2-logo-mono.svg     # Logo mono (embossed style)
│   └── favicon.svg           # Favicon (circular/square app icon)
├── icons/
│   ├── cutting/              # Module Cutting
│   │   ├── scissors.svg
│   │   ├── fabric.svg
│   │   └── pattern.svg
│   ├── production/           # Module Production
│   │   ├── sewing-machine.svg
│   │   ├── quality-check.svg
│   │   └── production-line.svg
│   ├── hr/                   # Module HR
│   │   ├── users.svg
│   │   ├── employee-card.svg
│   │   └── attendance.svg
│   ├── warehouse/            # Module Warehouse
│   │   ├── box.svg
│   │   ├── inventory.svg
│   │   └── delivery.svg
│   ├── finance/              # Module Finance
│   │   ├── calculator.svg
│   │   ├── invoice.svg
│   │   └── chart.svg
│   └── system/               # Module System
│       ├── settings.svg
│       ├── dashboard.svg
│       └── user-profile.svg
├── images/
│   ├── banner/
│   │   ├── welcome-banner.svg
│   │   └── maintenance-banner.svg
│   ├── empty-state/
│   │   ├── no-data.svg
│   │   └── empty-list.svg
│   └── panel/
│       ├── info-panel.svg
│       └── warning-panel.svg
├── asset-map.json            # Mapping KEY → CDN URL
├── generate-asset-map.js     # Script generate asset-map.json
└── README.md
```

## 📝 Quy tắc đặt tên file

1. **Không dấu**: `thiet-ke.svg` ✅ | `thiết-kế.svg` ❌
2. **Kebab-case**: `production-line.svg` ✅ | `productionLine.svg` ❌
3. **Mô tả rõ ràng**: `scissors.svg` ✅ | `icon1.svg` ❌
4. **Tiếng Anh**: Ưu tiên tiếng Anh, nếu không có thì dùng tiếng Việt không dấu

## 🎨 Quy chuẩn Icon

- **Format**: SVG outline
- **Icon set**: Tabler Icons (hoặc tương đương)
- **Kích thước**: 24x24px viewBox (có thể scale)
- **Style**: Outline, stroke-width: 2px
- **Color**: CurrentColor (để có thể đổi màu qua CSS)

## ⚠️ Những điều KHÔNG được làm

### ❌ KHÔNG được:
1. **Hotlink từ web bên ngoài** - Tất cả asset phải trong repo này
2. **Gắn asset trực tiếp vào repo web form** - Chỉ dùng CDN link
3. **Thay đổi file đã release** - Tạo file mới và bump version
4. **Dùng version `latest` hoặc `main` trong production** - Luôn pin version cụ thể
5. **Commit file binary lớn** - Chỉ SVG, PNG nhỏ (< 100KB)
6. **Đổi tên file đã có** - Tạo file mới, giữ file cũ để backward compatibility

### ✅ ĐƯỢC làm:
1. Thêm file mới
2. Tạo version mới khi cần
3. Cập nhật asset-map.json
4. Sửa README khi cần

## 🔄 Quy trình cập nhật asset

### Thêm asset mới (không breaking change)

```bash
# 1. Thêm file mới vào thư mục tương ứng
# 2. Chạy script generate asset-map.json
# PowerShell (Windows):
.\generate-asset-map.ps1 v1.1.0

# Hoặc Node.js:
node generate-asset-map.js v1.1.0

# 3. Commit và push
git add .
git commit -m "feat: add new icon for cutting module"
git push

# 4. Tạo tag mới (bump minor)
git tag v1.1.0
git push origin v1.1.0
```

### Thay đổi logo lớn (breaking change)

```bash
# 1. Thay đổi logo
# 2. Update asset-map.json
# PowerShell (Windows):
.\generate-asset-map.ps1 v2.0.0

# Hoặc Node.js:
node generate-asset-map.js v2.0.0

# 3. Commit
git add .
git commit -m "feat: update main logo (breaking change)"

# 4. Tạo tag mới (bump major)
git tag v2.0.0
git push origin v2.0.0

# 5. Thông báo team về breaking change
```

### Sửa lỗi nhỏ (patch)

```bash
# 1. Sửa file
# 2. Update asset-map.json nếu cần
# PowerShell (Windows):
.\generate-asset-map.ps1 v1.0.1

# Hoặc Node.js:
node generate-asset-map.js v1.0.1

# 3. Commit
git add .
git commit -m "fix: correct icon path in asset-map"

# 4. Bump patch version
git tag v1.0.1
git push origin v1.0.1
```

## 🔧 Scripts

### Generate asset-map.json

#### Cách 1: Dùng PowerShell (Windows - Khuyến nghị)

```powershell
.\generate-asset-map.ps1 v1.0.0
```

#### Cách 2: Dùng Node.js (nếu đã cài Node.js)

```bash
node generate-asset-map.js v1.0.0
```

Script này sẽ:
- Quét tất cả file trong `logo/`, `icons/`, `images/`
- Tạo mapping KEY → CDN URL
- Ghi vào `asset-map.json`

**Lưu ý**: Script tự động detect file `.svg`, `.png`, `.jpg`, `.jpeg`, `.webp`

## 📦 Dependencies

Không có dependencies. Chỉ cần Node.js để chạy script generate asset-map.

## 🤝 Contributing

1. Tạo branch mới từ `main`
2. Thêm/sửa asset
3. Chạy `node generate-asset-map.js`
4. Commit và push
5. Tạo Pull Request
6. Sau khi merge, tạo Git tag mới

## 📚 Tài liệu tham khảo

- [NAMING-CONVENTIONS.md](./NAMING-CONVENTIONS.md) - Quy chuẩn đặt tên file
- [VERSIONING.md](./VERSIONING.md) - Quy trình versioning chi tiết
- [STRUCTURE.md](./STRUCTURE.md) - Cấu trúc thư mục đầy đủ
- [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) - Hướng dẫn xử lý lỗi

## ⚠️ Troubleshooting

### Lỗi "Failed to fetch version info"

Nếu gặp lỗi này khi truy cập CDN URL:

1. **Kiểm tra repository có public không**
   - jsDelivr chỉ hỗ trợ public repositories
   - Đảm bảo repo `ngonluarecca/th2-brand-assets` là public trên GitHub

2. **Đợi jsDelivr index repository**
   - Sau khi push tag mới, jsDelivr cần 1-5 phút để index
   - Thử refresh lại sau vài phút

3. **Dùng `@main` thay vì `@v1.0.0` (tạm thời)**
   ```javascript
   // Thay vì
   https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo.svg
   
   // Dùng tạm
   https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@main/logo/th2-logo.svg
   ```
   ⚠️ **Lưu ý**: Không dùng `@main` trong production, chỉ dùng để test. Luôn pin version cụ thể.

4. **Kiểm tra tag đã được push chưa**
   ```bash
   git ls-remote --tags origin
   ```
   Nếu tag chưa có, push tag:
   ```bash
   git push origin v1.0.0
   ```

5. **Kiểm tra file có tồn tại không**
   - Truy cập trực tiếp: `https://github.com/ngonluarecca/th2-brand-assets/blob/v1.0.0/logo/th2-logo.svg`
   - Nếu file không có, cần commit và push lại

### Test CDN URL

Sau khi push tag, test URL này trong browser:
```
https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo-mark.svg
```

Nếu vẫn lỗi sau 5-10 phút, kiểm tra:
- Repository visibility (phải là Public)
- Tag name (phải chính xác: `v1.0.0`)
- File path (phải đúng case-sensitive)

## 📞 Liên hệ

Nếu có thắc mắc về asset hoặc cần thêm icon mới, liên hệ team Frontend.

---

**GitHub Repository**: https://github.com/ngonluarecca/th2-brand-assets

