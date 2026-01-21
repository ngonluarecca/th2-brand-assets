# TH2 Brand Assets

Chào mừng bạn đến với kho lưu trữ tài nguyên thương hiệu (Brand Assets) của hệ thống TH2. Repository này chứa toàn bộ icon, hình ảnh minh họa, và logo được chuẩn hóa để sử dụng thống nhất trên các ứng dụng (AppSheet, Web App, Reports).

## 1. Mục đích & Ý nghĩa
Dự án này nhằm giải quyết các vấn đề:
- **Đồng bộ nhận diện**: Đảm bảo tất cả icon/hình ảnh tuân theo một phong cách thiết kế nhất quán ("Soft Lineal Color").
- **Quản lý tập trung**: Dễ dàng tìm kiếm và tái sử dụng tài nguyên.
- **Tối ưu hóa**: Assets được lưu trữ dưới dạng PNG trong suốt, tối ưu dung lượng và hiển thị.
- **CDN Ready**: Cung cấp file `asset-map.json` để tích hợp nhanh vào các ứng dụng thông qua CDN.

## 2. Hướng dẫn Sử dụng

### 2.1. Cấu trúc đường dẫn CDN
Để sử dụng asset trong ứng dụng, bạn có thể dùng đường dẫn trực tiếp từ GitHub qua jsDelivr:

- **Base URL**: `https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@<TAG>/`
    - `<TAG>`: Phiên bản release (ví dụ: `v2.0.1`, `main`...). Khuyên dùng version tag cụ thể để tránh lỗi cache hoặc thay đổi bất ngờ.

Ví dụ:
```
https://cdn.jsdelivr.net/gh/ngonluarecca/th2-brand-assets@v2.0.1/icons/production/sewing-machine.png
```

### 2.2. Asset Map (`asset-map.json`)
File `asset-map.json` cung cấp một từ điển key-value mapping toàn bộ assets. Các ứng dụng nên fetch file này về để lấy đường dẫn assets thay vì hard-code link.

```json
{
  "icons": {
    "production": {
      "sewing-machine": "https://cdn.../sewing-machine.png"
    }
  }
}
```

## 3. Quy chuẩn Thiết kế
Chi tiết về phong cách thiết kế, bảng màu, và mẫu câu lệnh AI (Prompt) để tạo asset mới được mô tả trong tài liệu:
👉 **[00_overview.md](./00_overview.md)**

## 4. Quy trình Cập nhật & Bảo trì

### Cập nhật File Preview
Mỗi khi thêm hoặc xóa asset, bạn cần cập nhật file `preview_all.html` để dễ dàng kiểm tra trực quan.
Chạy file script Python sau:

```bash
python tools/generate_preview.py
```

### Release Phiên bản mới
Để release một phiên bản mới (tạo tag GitHub và cập nhật CDN):
Sử dụng script `tools/release.ps1` với tham số là version mới. Script này sẽ tự động:
1.  Cập nhật file `asset-map.json` (thay thế version cũ bằng version mới trong config và tất cả URLs).
2.  Cập nhật ngày build (`generatedAt`).
3.  Tạo lại file Preview.
4.  Git Commit, Push code, Tạo Tag và Push Tag.

**Cú pháp:**
```powershell
.\tools\release.ps1 -Version v2.0.2
```

### Kiểm tra (Testing)
Trước khi release phiên bản mới:
1.  **Check cấu trúc**: Đảm bảo file nằm đúng thư mục quy định trong [STRUCTURE.md](./STRUCTURE.md).
2.  **Check hiển thị**: Mở `preview_all.html` để xem có hình ảnh nào bị lỗi, vỡ, hoặc nền chưa trong suốt không.
3.  **Check JSON**: Dùng các tool online (như jsonlint.com) để đảm bảo `asset-map.json` đúng cú pháp.

## 5. Tài liệu tham khảo
- **Design Style**: Soft Lineal Color.
- **Tools**:
    - remove_bg.py: Tool xóa nền (sử dụng thư viện `Pillow`).
    - generate_preview.py: Tool tạo danh mục hiển thị.

---
*Phiên bản hiện tại: v2.0.1*
