#!/usr/bin/env python3
"""
Hướng dẫn sử dụng hệ thống AHP với ma trận 6x6
"""

def print_instructions():
    """In hướng dẫn sử dụng"""
    print("🚀 HƯỚNG DẪN SỬ DỤNG HỆ THỐNG AHP VỚI MA TRẬN 6x6")
    print("=" * 70)
    
    print("\n📁 CÁC FILE ĐÃ TẠO:")
    print("   📊 Ma trận tiêu chí:")
    print("      - test_criteria_matrix_6x6.xlsx (Ma trận 6x6 với 6 tiêu chí)")
    
    print("\n   👥 Ma trận ứng viên (3x3 cho mỗi tiêu chí):")
    matrices = [
        ("test_candidate_matrix_3x3_kinh_nghiem.xlsx", "Kinh nghiệm"),
        ("test_candidate_matrix_3x3_thai_do.xlsx", "Thái độ"),
        ("test_candidate_matrix_3x3_giao_tiep.xlsx", "Kỹ năng giao tiếp"),
        ("test_candidate_matrix_3x3_hoc_hoi.xlsx", "Khả năng học hỏi"),
        ("test_candidate_matrix_3x3_lam_viec_nhom.xlsx", "Làm việc nhóm"),
        ("test_candidate_matrix_3x3_sang_tao.xlsx", "Sáng tạo")
    ]
    
    for file_name, criterion in matrices:
        print(f"      - {file_name} (cho tiêu chí: {criterion})")
    
    print("\n🔧 QUY TRÌNH SỬ DỤNG:")
    print("\n1️⃣  KHỞI ĐỘNG HỆ THỐNG:")
    print("      python app.py")
    
    print("\n2️⃣  TẠO ĐỢT TUYỂN DỤNG:")
    print("      - Truy cập: http://localhost:5000")
    print("      - Nhập tên đợt tuyển dụng: 'Test AHP 6 tiêu chí'")
    print("      - Nhập vị trí: 'Nhân viên IT'")
    print("      - Nhập mô tả: 'Thử nghiệm hệ thống AHP với 6 tiêu chí'")
    
    print("\n3️⃣  THIẾT LẬP SỐ LƯỢNG TIÊU CHÍ:")
    print("      - Chọn số lượng tiêu chí: 6")
    
    print("\n4️⃣  IMPORT MA TRẬN TIÊU CHÍ:")
    print("      - Nhấn 'Import Ma Trận từ Excel'")
    print("      - Chọn file: test_criteria_matrix_6x6.xlsx")
    print("      - ✅ Hệ thống sẽ tự động:")
    print("        • Đọc ma trận 6x6")
    print("        • Điền tên 6 tiêu chí vào các ô input")
    print("        • Tính toán trọng số và CR")
    
    print("\n5️⃣  THIẾT LẬP SỐ LƯỢNG ỨNG VIÊN:")
    print("      - Chọn số lượng ứng viên: 3")
    
    print("\n6️⃣  NHẬP TÊN ỨNG VIÊN:")
    print("      - Ứng viên 1: 'Ứng viên A'")
    print("      - Ứng viên 2: 'Ứng viên B'")
    print("      - Ứng viên 3: 'Ứng viên C'")
    print("      (Hoặc import từ file Excel)")
    
    print("\n7️⃣  IMPORT MA TRẬN ỨNG VIÊN CHO TỪNG TIÊU CHÍ:")
    print("      Cho mỗi tiêu chí, nhấn 'Import Ma Trận từ Excel' và chọn file tương ứng:")
    
    for i, (file_name, criterion) in enumerate(matrices, 1):
        print(f"      • Tiêu chí {i} ({criterion}):")
        print(f"        → {file_name}")
    
    print("\n8️⃣  XEM KẾT QUẢ:")
    print("      - Hệ thống sẽ tính toán điểm tổng hợp")
    print("      - Hiển thị xếp hạng ứng viên")
    print("      - Xuất báo cáo Excel")
    
    print("\n🎯 KẾT QUẢ DỰ KIẾN:")
    print("      Dựa trên ma trận đã thiết kế:")
    print("      📊 Trọng số tiêu chí (cao → thấp):")
    print("         1. Kinh nghiệm (32.2%)")
    print("         2. Làm việc nhóm (25.6%)")
    print("         3. Kỹ năng giao tiếp (16.9%)")
    print("         4. Thái độ & Sáng tạo (9.7% mỗi cái)")
    print("         5. Khả năng học hỏi (5.9%)")
    
    print("\n      👥 Ưu thế ứng viên theo tiêu chí:")
    print("         • Kinh nghiệm: A > B > C")
    print("         • Thái độ: B > A > C")
    print("         • Giao tiếp: C > B > A")
    print("         • Học hỏi: A > C > B")
    print("         • Làm việc nhóm: C > B > A")
    print("         • Sáng tạo: C > A > B")
    
    print("\n💡 LƯU Ý QUAN TRỌNG:")
    print("      - Tất cả ma trận đều có CR < 0.1 (nhất quán)")
    print("      - Hệ thống sẽ tự động đọc tên tiêu chí và ứng viên từ file")
    print("      - Nếu có lỗi, kiểm tra định dạng file Excel")
    
    print("\n🔍 KIỂM TRA LẠI:")
    print("      Nếu import không đúng, chạy:")
    print("      python test_6x6_import.py")
    
    print("\n" + "=" * 70)
    print("✨ CHÚC BẠN THÀNH CÔNG VỚI HỆ THỐNG AHP! ✨")

if __name__ == "__main__":
    print_instructions()
