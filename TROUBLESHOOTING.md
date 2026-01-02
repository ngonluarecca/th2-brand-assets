# Troubleshooting Guide

## Lỗi "Failed to fetch version info"

### Nguyên nhân

Lỗi này xảy ra khi jsDelivr không thể lấy thông tin version từ GitHub repository. Có thể do:

1. Repository chưa được push lên GitHub
2. Tag chưa được tạo hoặc chưa được push
3. Repository là private (jsDelivr chỉ hỗ trợ public repos)
4. jsDelivr chưa kịp index repository mới

### Giải pháp

#### 1. Kiểm tra repository visibility

jsDelivr **chỉ hỗ trợ public repositories**. Đảm bảo repo `ngonluarecca/th2-brand-assets` là **Public** trên GitHub.

**Cách kiểm tra:**
- Vào https://github.com/ngonluarecca/th2-brand-assets
- Nếu thấy badge "Public" ở góc trên bên phải → OK
- Nếu thấy "Private" → Cần đổi sang Public

**Cách đổi sang Public:**
1. Vào Settings của repository
2. Scroll xuống phần "Danger Zone"
3. Click "Change visibility" → "Make public"

#### 2. Kiểm tra tag đã được push chưa

```bash
# Kiểm tra tag trên remote
git ls-remote --tags origin

# Nếu không thấy v1.0.0, push tag
git push origin v1.0.0
```

#### 3. Đợi jsDelivr index (1-5 phút)

Sau khi push tag mới, jsDelivr cần thời gian để index repository. Thử lại sau 1-5 phút.

#### 4. Dùng `@main` tạm thời (chỉ để test)

```javascript
// ❌ Không dùng trong production
const logoUrl = 'https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@main/logo/th2-logo.svg';

// ✅ Dùng trong production
const logoUrl = 'https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo.svg';
```

⚠️ **Lưu ý**: `@main` có thể thay đổi bất ngờ, không dùng trong production!

#### 5. Kiểm tra file có tồn tại không

Truy cập trực tiếp trên GitHub:
```
https://github.com/ngonluarecca/th2-brand-assets/blob/v1.0.0/logo/th2-logo.svg
```

Nếu file không có:
1. Kiểm tra file đã được commit chưa
2. Kiểm tra file path có đúng không (case-sensitive)
3. Commit và push lại:
   ```bash
   git add logo/th2-logo.svg
   git commit -m "fix: add logo file"
   git push origin main
   git tag -f v1.0.0
   git push origin v1.0.0 --force
   ```

### Test CDN URL

Sau khi đảm bảo các bước trên, test URL này trong browser:

```
https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/logo/th2-logo-mark.svg
```

**Kết quả mong đợi:**
- ✅ Thấy nội dung SVG → CDN hoạt động
- ❌ Lỗi "Failed to fetch" → Xem lại các bước trên

### Checklist

Trước khi báo lỗi, đảm bảo:

- [ ] Repository là **Public**
- [ ] Tag `v1.0.0` đã được push lên GitHub
- [ ] File SVG tồn tại trong repository
- [ ] Đã đợi ít nhất 5 phút sau khi push tag
- [ ] URL đúng format: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v1.0.0/[path]`
- [ ] File path đúng case-sensitive

### Các lỗi khác

#### Lỗi 404 Not Found

**Nguyên nhân:** File không tồn tại hoặc path sai

**Giải pháp:**
1. Kiểm tra file có trong repo không
2. Kiểm tra path có đúng case-sensitive không
3. Kiểm tra tag có đúng không

#### Lỗi CORS

**Nguyên nhân:** jsDelivr hỗ trợ CORS, nhưng có thể bị block bởi browser

**Giải pháp:**
- Kiểm tra browser console
- Thử browser khác
- Kiểm tra network tab

#### Logo không hiển thị

**Nguyên nhân:** SVG có lỗi hoặc không hợp lệ

**Giải pháp:**
1. Mở file SVG trực tiếp trên GitHub
2. Validate SVG tại: https://validator.w3.org/
3. Kiểm tra SVG có đúng format không

### Liên hệ

Nếu vẫn gặp vấn đề sau khi thử tất cả các bước trên, tạo issue trên GitHub:
https://github.com/ngonluarecca/th2-brand-assets/issues

