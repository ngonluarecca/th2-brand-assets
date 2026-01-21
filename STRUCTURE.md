# Cấu trúc Dự án (Project Structure)

Tài liệu này mô tả chi tiết cách tổ chức thư mục va tập tin trong repository `th2-brand-assets`. Việc tuân thủ cấu trúc này giúp đảm bảo tính nhất quán và dễ dàng bảo trì khi mở rộng hệ thống Assets.

## 1. Cây thư mục (Directory Tree)

```
th2-brand-assets/
├── assets-map.json         # File định nghĩa đường dẫn CDN và mapping assets
├── preview_all.html        # File xem trước toàn bộ Assets (được tạo tự động)
├── README.md               # Hướng dẫn tổng quan dự án
├── STRUCTURE.md            # (File này) Quy tắc tổ chức cấu trúc dự án
├── 00_overview.md          # Quy chuẩn thiết kế (Design System & AI Prompts)
├── icons/                  # Chứa toàn bộ ICON (dạng hình vuông, kích thước nhỏ)
│   ├── admin/              # Icon quản trị (Lịch, Báo cáo...)
│   ├── cutting/            # Icon bộ phận Cắt (Vải, Rập, Kéo...)
│   ├── finance/            # Icon Tài chính - Kế toán
│   ├── hr/                 # Icon Nhân sự
│   ├── logistic/           # Icon Vận chuyển
│   ├── production/         # Icon Sản xuất (Máy may, Chuyền...)
│   ├── purchase/           # Icon Mua hàng
│   ├── sales/              # Icon Kinh doanh
│   ├── system/             # Icon Hệ thống (Cài đặt, Database...)
│   └── warehouse/          # Icon Kho
├── images/                 # Chứa hình ảnh minh họa (Banner, Panel...)
│   ├── banner/             # Ảnh bìa, ảnh tiêu đề
│   ├── panel/              # Ảnh thông báo, cảnh báo (Alerts)
│   └── empty-state/        # Ảnh trạng thái rỗng (No data)
├── logo/                   # Chứa Logo thương hiệu
└── tools/                  # Các công cụ hỗ trợ (Scripts)
    ├── generate_preview.py # Script tạo file preview_all.html
    └── remove_bg.py        # Script xóa nền trắng cho ảnh
```

## 2. Quy tắc Tổ chức & Đặt tên

### 2.1. Icons (`/icons`)
- **Định dạng**: `.png` (bắt buộc).
- **Kích thước chuẩn**: 150x150px (hoặc tỉ lệ 1:1).
- **Quy tắc đặt tên file**: `kebab-case` (chữ thường, gạch nối).
    - Ví dụ đúng: `sewing-machine.png`, `quality-check.png`.
    - Ví dụ sai: `SewingMachine.png`, `may_may.png`.
- **Tên tiếng Anh**: Ưu tiên sử dụng tên tiếng Anh chuẩn để dễ map với code.

### 2.2. Images (`/images`)
- **Định dạng**: `.png`.
- **Phân loại**:
    - `banner/`: Hình chữ nhật ngang.
    - `panel/`: Icon/Hình minh họa cho các khối thông báo.
    - `empty-state/`: Hình minh họa cho trạng thái không có dữ liệu.

### 2.3. Logo (`/logo`)
- Chứa các biến thể logo chính thức.
- **Lưu ý**: Chỉ sử dụng các file gốc đã được duyệt. Không tự ý chỉnh sửa logo.

## 3. Quy trình Thêm/Sửa/Xóa (Workflow)

### 3.1. Thêm Asset mới
1.  Tạo asset theo quy chuẩn thiết kế trong `00_overview.md`.
2.  Chạy script xóa nền (nếu asset được tạo từ AI nền trắng):
    ```bash
    py tools/remove_bg.py <đường_dẫn_thư_mục_chứa_ảnh_gốc>
    ```
3.  Đặt tên file theo quy chuẩn `kebab-case`.
4.  Copy vào thư mục con tương ứng trong `icons/` hoặc `images/`.
5.  Chạy script cập nhật preview:
    ```bash
    py tools/generate_preview.py
    ```
6.  Cập nhật file `asset-map.json` nếu cần dùng CDN.

### 3.2. Sửa/Thay thế Asset
- Ghi đè file cũ bằng file mới cùng tên.
- **Lưu ý**: Giữ nguyên tên file để không làm hỏng các liên kết trong App đang sử dụng.

### 3.3. Xóa Asset
- Chỉ xóa khi chắc chắn Asset không còn được sử dụng ở bất kỳ đâu.
- Xóa mục tương ứng trong `asset-map.json`.
