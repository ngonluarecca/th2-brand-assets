# Quy trình Versioning

## Semantic Versioning

Repo sử dụng [Semantic Versioning](https://semver.org/) với format: `MAJOR.MINOR.PATCH`

- **MAJOR** (v2.0.0): Breaking changes - Thay đổi logo lớn, đổi cấu trúc thư mục
- **MINOR** (v1.1.0): Thêm asset mới, không breaking change
- **PATCH** (v1.0.1): Sửa lỗi nhỏ, sửa typo trong asset-map.json

## Khi nào bump version?

### Bump MAJOR (v1.0.0 → v2.0.0)

Khi có **breaking changes**:
- Thay đổi logo chính (màu sắc, thiết kế lớn)
- Đổi tên file logo đã có
- Thay đổi cấu trúc thư mục
- Xóa file đã release

**Ví dụ:**
```bash
# Thay đổi logo chính
git commit -m "feat: redesign main logo (breaking change)"
git tag v2.0.0
```

### Bump MINOR (v1.0.0 → v1.1.0)

Khi **thêm asset mới** mà không breaking:
- Thêm icon mới
- Thêm banner mới
- Thêm empty state mới
- Cập nhật asset-map.json với key mới

**Ví dụ:**
```bash
# Thêm icon mới
git commit -m "feat: add new icons for cutting module"
git tag v1.1.0
```

### Bump PATCH (v1.0.0 → v1.0.1)

Khi **sửa lỗi nhỏ**:
- Sửa typo trong asset-map.json
- Sửa đường dẫn CDN sai
- Sửa metadata trong asset-map.json
- Sửa lỗi nhỏ trong SVG (không thay đổi thiết kế)

**Ví dụ:**
```bash
# Sửa typo
git commit -m "fix: correct icon path in asset-map.json"
git tag v1.0.1
```

## Quy trình bump version

### 1. Thêm/sửa asset

```bash
# Làm việc trên branch mới
git checkout -b feat/add-new-icon
```

### 2. Cập nhật asset-map.json

```bash
# Chạy script generate
node generate-asset-map.js v1.1.0

# Hoặc set version qua environment variable
export VERSION=v1.1.0
node generate-asset-map.js
```

### 3. Commit và push

```bash
git add .
git commit -m "feat: add new icon for production module"
git push origin feat/add-new-icon
```

### 4. Tạo Pull Request

Tạo PR trên GitHub, review và merge vào `main`.

### 5. Tạo Git tag

Sau khi merge vào `main`:

```bash
# Pull latest main
git checkout main
git pull origin main

# Tạo tag
git tag v1.1.0

# Push tag lên GitHub
git push origin v1.1.0
```

### 6. Verify trên jsDelivr

Kiểm tra CDN URL hoạt động:
```
https://cdn.jsdelivr.net/gh/[username]/th2-brand-assets@v1.1.0/asset-map.json
```

## Best Practices

### ✅ NÊN làm

1. **Luôn pin version cụ thể trong production**
   ```javascript
   // ✅ ĐÚNG
   const assetMap = await fetch('https://cdn.jsdelivr.net/gh/user/th2-brand-assets@v1.0.0/asset-map.json')
   
   // ❌ SAI - Không dùng latest
   const assetMap = await fetch('https://cdn.jsdelivr.net/gh/user/th2-brand-assets@latest/asset-map.json')
   ```

2. **Test version mới trước khi deploy**
   - Test trên staging environment
   - Verify tất cả asset load đúng
   - Check asset-map.json structure

3. **Thông báo team về breaking changes**
   - Tạo issue/PR với label `breaking-change`
   - Thông báo trong team chat
   - Update migration guide nếu cần

4. **Giữ backward compatibility khi có thể**
   - Không xóa file cũ ngay
   - Thêm file mới, giữ file cũ 1-2 version
   - Deprecate trong README trước khi xóa

### ❌ KHÔNG nên làm

1. **Không bump version cho mọi thay đổi nhỏ**
   - Không cần bump nếu chỉ sửa README
   - Không cần bump nếu chỉ sửa comment trong code

2. **Không dùng `latest` hoặc `main` trong production**
   - Luôn pin version cụ thể
   - `latest` có thể thay đổi bất ngờ

3. **Không thay đổi file đã release**
   - Tạo file mới thay vì sửa file cũ
   - Giữ file cũ để backward compatibility

4. **Không tạo tag trước khi merge vào main**
   - Luôn merge PR trước
   - Tạo tag từ main branch

## Version History Template

Khi tạo tag mới, có thể thêm release notes:

```markdown
## v1.1.0 (2024-01-15)

### Added
- New icons for cutting module: fabric.svg, pattern.svg
- New empty state: empty-list.svg

### Changed
- Updated asset-map.json structure

## v1.0.0 (2024-01-01)

### Added
- Initial release
- Main logo set (logo, white, mono, favicon)
- Icon sets for all modules
- Banner and empty state images
```

## Migration Guide

Khi có breaking change (MAJOR bump), tạo migration guide:

```markdown
## Migration from v1.x to v2.0

### Breaking Changes

1. **Logo path changed**
   - Old: `logo/th2-logo.svg`
   - New: `logo/th2-logo-new.svg`
   
2. **Icon structure changed**
   - Old: `icons/cutting/scissors.svg`
   - New: `icons/cutting/scissors-new.svg`

### Migration Steps

1. Update version in your code:
   ```javascript
   // Old
   const version = 'v1.0.0';
   
   // New
   const version = 'v2.0.0';
   ```

2. Update asset paths:
   ```javascript
   // Old
   const logo = assetMap.logo['th2-logo'];
   
   // New
   const logo = assetMap.logo['th2-logo-new'];
   ```

3. Test thoroughly before deploying
```

