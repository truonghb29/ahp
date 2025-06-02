# Hướng Dẫn Sử Dụng Chức Năng Import Excel - AHP Recruitment System

## Tổng Quan
Hệ thống AHP Recruitment đã được bổ sung chức năng import dữ liệu từ file Excel, giúp người dùng nhập liệu nhanh chóng và chính xác hơn.

## Các Chức Năng Import

### 1. Import Danh Sách Ứng Viên

**Vị trí**: Trang "Bước 3: Xác định Số Lượng Ứng Viên"
**Nút**: "Import Ứng Viên từ Excel"

**Định dạng file Excel yêu cầu**:
- Cột A: Tên ứng viên
- Hàng 1: Tiêu đề (có thể bỏ qua)
- Từ hàng 2 trở đi: Danh sách ứng viên
- Ít nhất 2 ứng viên

**Ví dụ**:
```
A1: Tên ứng viên
A2: Nguyễn Văn A
A3: Trần Thị B
A4: Lê Văn C
A5: Phạm Thị D
```

### 2. Import Ma Trận So Sánh Tiêu Chí

**Vị trí**: Trang "Bước 2: Nhập Tên và So Sánh Cặp Tiêu Chí"
**Nút**: "Import Ma Trận từ Excel"

**Định dạng file Excel yêu cầu**:
- Ma trận vuông NxN (N = số lượng tiêu chí)
- Đường chéo chính = 1
- Nếu a[i,j] = x thì a[j,i] = 1/x
- Sử dụng thang đo Saaty (1-9)
- Tất cả giá trị > 0

**Ví dụ ma trận 3x3**:
```
    A    B    C
A   1    3    5
B  0.33  1    3
C  0.2  0.33  1
```

### 3. Import Ma Trận So Sánh Ứng Viên

**Vị trí**: Trang so sánh ứng viên cho từng tiêu chí
**Nút**: "Import Ma Trận từ Excel"

**Định dạng file Excel yêu cầu**:
- Ma trận vuông MxM (M = số lượng ứng viên)
- Đường chéo chính = 1
- Nếu a[i,j] = x thì a[j,i] = 1/x
- Sử dụng thang đo Saaty (1-9)
- Tất cả giá trị > 0

## Thang Đo Saaty

| Giá trị | Ý nghĩa |
|---------|---------|
| 1 | Quan trọng bằng nhau |
| 3 | Quan trọng hơn một chút |
| 5 | Quan trọng hơn |
| 7 | Quan trọng hơn nhiều |
| 9 | Quan trọng hơn tuyệt đối |
| 2, 4, 6, 8 | Các mức trung gian |

## Lưu Ý Quan Trọng

### Tính Nhất Quán Ma Trận
- Hệ thống sẽ tự động tính toán chỉ số nhất quán (CR - Consistency Ratio)
- CR < 0.1: Ma trận nhất quán (được chấp nhận)
- CR >= 0.1: Ma trận không nhất quán (cần điều chỉnh)

### Định Dạng File
- Chỉ chấp nhận file .xlsx và .xls
- Kích thước file tối đa: 16MB
- Đảm bảo file không bị lỗi hoặc corrupt

### Xử Lý Lỗi
- Hệ thống sẽ thông báo lỗi cụ thể nếu file không đúng định dạng
- File upload sẽ được tự động xóa sau khi xử lý
- Dữ liệu lỗi sẽ không được lưu vào hệ thống

## File Mẫu

Hệ thống cung cấp các file Excel mẫu:
- **Danh sách ứng viên**: Tải từ nút "Tải File Mẫu Excel"
- **Ma trận tiêu chí**: Tự động tạo theo số lượng tiêu chí đã chọn
- **Ma trận ứng viên**: Tự động tạo theo số lượng ứng viên và tên tiêu chí

## Quy Trình Sử Dụng

1. **Tải file mẫu** từ hệ thống
2. **Điền dữ liệu** vào file Excel theo đúng định dạng
3. **Kiểm tra** tính nhất quán của ma trận (nếu áp dụng)
4. **Upload file** vào hệ thống
5. **Xem kết quả** và chỉnh sửa nếu cần

## Ví Dụ Thực Tế

### Ma Trận Tiêu Chí Tuyển Dụng (4 tiêu chí)
```
Tiêu chí: [Kiến thức, Kinh nghiệm, Kỹ năng mềm, Thái độ]

         KT   KN   KNM  TD
KT       1    2    3    4
KN      0.5   1    2    3
KNM    0.33  0.5   1    2
TD     0.25 0.33  0.5   1
```

### Ma Trận Ứng Viên cho Tiêu Chí "Kiến Thức"
```
Ứng viên: [An, Bình, Cường]

       An   Bình  Cường
An     1     3      2
Bình  0.33   1     0.5
Cường 0.5    2      1
```

## Hỗ Trợ và Khắc Phục Sự Cố

### Lỗi Thường Gặp
1. **"Ma trận không phải ma trận vuông"**: Số hàng và số cột không bằng nhau
2. **"Ma trận chứa giá trị không hợp lệ"**: Có giá trị ≤ 0 hoặc không phải số
3. **"File Excel không chứa ứng viên nào"**: Cột A trống hoặc không có dữ liệu
4. **"CR >= 0.1"**: Ma trận không nhất quán, cần điều chỉnh

### Khắc Phục
- Kiểm tra định dạng file Excel
- Đảm bảo ma trận đối xứng nghịch đảo
- Sử dụng thang đo Saaty đúng cách
- Tham khảo file mẫu từ hệ thống

## Cập Nhật và Phát Triển

Các tính năng sẽ được bổ sung:
- Export kết quả ra Excel
- Import/Export cả quy trình AHP
- Validation nâng cao cho ma trận
- Hỗ trợ nhiều định dạng file khác
