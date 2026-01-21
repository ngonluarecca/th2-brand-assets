# Hướng dẫn update lên v1.0.1

## Vấn đề

Tag `v1.0.0` đã được tạo từ trước khi có các file PNG mới (`th2-logo.png`, `th2-logo-text.png`, `logo-tron.png`). Vì vậy các file PNG không thể truy cập qua CDN với tag `v1.0.0`.

## Giải pháp: Tạo tag v1.0.1

### Bước 1: Đảm bảo tất cả file đã được commit

```bash
# Kiểm tra status
git status

# Nếu có file chưa commit, thêm và commit
git add logo/*.png
git add asset-map.json
git commit -m "feat: add PNG logo files and update asset-map to v1.0.1"
```

### Bước 2: Push code lên GitHub

```bash
git push origin main
```

### Bước 3: Tạo tag v1.0.1

```bash
# Tạo tag mới
git tag v1.0.1

# Push tag lên GitHub
git push origin v1.0.1
```

### Bước 4: Verify

Sau khi push tag, đợi 1-2 phút rồi test các URL:

- ✅ Logo PNG: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.1/logo/th2-logo.png`
- ✅ Logo text PNG: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.1/logo/th2-logo-text.png`
- ✅ Logo tròn PNG: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.1/logo/logo-tron.png`
- ✅ Asset map: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.1/asset-map.json`

## Lưu ý

- Tag `v1.0.0` vẫn giữ nguyên (không xóa) để backward compatibility
- Tag `v1.0.1` là patch version (theo semantic versioning)
- Sau khi tạo tag, cập nhật code sử dụng asset để dùng `v1.0.1` thay vì `v1.0.0`

## Checklist

- [ ] File PNG đã được commit
- [ ] `asset-map.json` đã được update với version `v1.0.1`
- [ ] Code đã được push lên `main` branch
- [ ] Tag `v1.0.1` đã được tạo
- [ ] Tag `v1.0.1` đã được push lên GitHub
- [ ] Đã test CDN URLs với `v1.0.1`

