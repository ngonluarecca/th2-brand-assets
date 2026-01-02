# Quy chuẩn đặt tên file

## Nguyên tắc chung

1. **Không dấu**: Tất cả file phải không có dấu tiếng Việt
   - ✅ `thiet-ke.svg`
   - ❌ `thiết-kế.svg`

2. **Kebab-case**: Dùng dấu gạch ngang để phân cách từ
   - ✅ `production-line.svg`
   - ❌ `productionLine.svg`
   - ❌ `production_line.svg`

3. **Mô tả rõ ràng**: Tên file phải mô tả được nội dung
   - ✅ `scissors.svg`
   - ❌ `icon1.svg`
   - ❌ `cutting-icon.svg` (thừa suffix `-icon`)

4. **Tiếng Anh ưu tiên**: Ưu tiên dùng tiếng Anh, nếu không có từ tương đương thì dùng tiếng Việt không dấu
   - ✅ `sewing-machine.svg`
   - ✅ `may-vai.svg` (nếu không có từ tiếng Anh tương đương)

5. **Không viết hoa**: Tất cả chữ thường
   - ✅ `th2-logo.svg`
   - ❌ `TH2-Logo.svg`

## Cấu trúc theo module

### Logo
```
logo/
├── th2-logo.svg          # Logo chính
├── th2-logo-white.svg    # Logo trắng (dark mode)
├── th2-logo-mono.svg     # Logo mono
└── favicon.svg           # Favicon
```

### Icons theo module

#### Cutting
```
icons/cutting/
├── scissors.svg
├── fabric.svg
├── pattern.svg
└── [tên-icon].svg
```

#### Production
```
icons/production/
├── sewing-machine.svg
├── quality-check.svg
├── production-line.svg
└── [tên-icon].svg
```

#### HR
```
icons/hr/
├── users.svg
├── employee-card.svg
├── attendance.svg
└── [tên-icon].svg
```

#### Warehouse
```
icons/warehouse/
├── box.svg
├── inventory.svg
├── delivery.svg
└── [tên-icon].svg
```

#### Finance
```
icons/finance/
├── calculator.svg
├── invoice.svg
├── chart.svg
└── [tên-icon].svg
```

#### System
```
icons/system/
├── settings.svg
├── dashboard.svg
├── user-profile.svg
└── [tên-icon].svg
```

### Images
```
images/
├── banner/
│   ├── welcome-banner.svg
│   └── [tên-banner].svg
├── empty-state/
│   ├── no-data.svg
│   └── [tên-empty-state].svg
└── panel/
    ├── info-panel.svg
    └── [tên-panel].svg
```

## Ví dụ đặt tên

### ✅ ĐÚNG
- `scissors.svg` - Rõ ràng, ngắn gọn
- `sewing-machine.svg` - Mô tả đầy đủ
- `quality-check.svg` - Dùng kebab-case
- `employee-card.svg` - Mô tả rõ ràng
- `no-data.svg` - Ngắn gọn, dễ hiểu

### ❌ SAI
- `scissors-icon.svg` - Thừa suffix `-icon`
- `SewingMachine.svg` - Viết hoa, không dùng kebab-case
- `quality_check.svg` - Dùng underscore thay vì kebab-case
- `icon1.svg` - Không mô tả được nội dung
- `thiết-kế.svg` - Có dấu tiếng Việt
- `TH2-Logo.svg` - Viết hoa

## Quy tắc đặc biệt

1. **Logo**: Luôn có prefix `th2-` để phân biệt với icon khác
2. **Favicon**: Tên file là `favicon.svg` (không cần prefix)
3. **Banner/Panel**: Có thể có suffix `-banner`, `-panel` để phân loại
4. **Empty state**: Có thể có prefix `empty-` hoặc `no-` để phân loại

## Checklist trước khi commit

- [ ] Tên file không có dấu tiếng Việt
- [ ] Tên file dùng kebab-case
- [ ] Tên file mô tả rõ ràng nội dung
- [ ] Tên file viết thường
- [ ] File đặt đúng thư mục module
- [ ] Không có suffix `-icon` thừa (trừ khi cần phân biệt)

