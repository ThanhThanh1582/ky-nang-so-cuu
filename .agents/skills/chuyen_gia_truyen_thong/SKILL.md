---
name: chuyen_gia_truyen_thong
description: Skill for designing and developing highly interactive, large-font medical presentation slides with smartboard compatibility, dynamic matching games, Web Audio API synthesis, and strict Vietnamese capitalization checks.
---

# Kỹ năng Thiết kế Slide Tương tác Chuyên gia Truyền thông (Tiết 3)

Tài liệu này đúc kết toàn bộ phương pháp luận, tiêu chuẩn lập trình và thiết kế giao diện tương tác số hóa áp dụng cho Tiết 3: Chuyên gia tuyên truyền sức khỏe.

---

## 1. Nguyên tắc Thiết kế Tương tác Bảng Thông minh (Smartboard Optimization)
*   **Cơ chế Chạm Chọn (Click-Select):** Hạn chế tối đa kéo thả HTML5 do dễ bị trượt mục tiêu trên màn hình cảm ứng Smartboard lớn. Sử dụng cơ chế chạm chọn thẻ ở danh sách nguồn, sau đó chạm chọn ô đích để điền dữ liệu.
*   **Vẽ Liên kết SVG Động:** Sử dụng thẻ `<svg>` nền để vẽ đường nối trực quan giữa các thẻ. Lập trình sự kiện `window.addEventListener('resize', ...)` để tính toán lại tọa độ tuyệt đối của các phần tử và cập nhật lại đường vẽ tức thời khi thay đổi độ phân giải màn hình.
*   **Tích hợp Chấm điểm thời gian thực:** Thiết kế bảng kiểm đánh giá chéo (Peer-assessment) đi kèm hệ thống sao động (Stars rating) và nhận xét tự động để học sinh trực tiếp chấm điểm lẫn nhau trên Smartboard.

---

## 2. Hệ thống Đa phương tiện Không phụ thuộc Tài nguyên ngoài (Zero-Asset Multimedia)
*   **Tổng hợp Âm thanh Nhân tạo (Web Audio API):** Lập trình các bộ dao động (Oscillators) và bộ lọc (Filters) bằng JavaScript thuần để sinh âm thanh trực tiếp, ngăn ngừa lỗi mất file âm thanh (404 Not Found) khi chuyển giao bài giảng:
    *   *Tiếng còi hú khẩn cấp (Siren):* Dùng dạng sóng sawtooth kết hợp sine quét tần số từ 440Hz lên 580Hz.
    *   *Tiếng đóng dấu cam kết (Stamp):* Dùng dạng sóng triangle quét nhanh tần số từ 100Hz xuống 10Hz trong 0.3s.
    *   *Tiếng lật tài liệu (Document):* Dùng sóng triangle quét tần số từ 300Hz lên 600Hz trong 0.15s.
    *   *Tiếng chuông hết giờ (Bell):* Dùng sóng sine tần số cao 980Hz suy giảm dần trong 1.0s.
    *   *Tiếng vỗ tay khen thưởng (Applause):* Dùng bộ đệm tạo tiếng ồn ngẫu nhiên (White Noise) kết hợp bộ lọc bandpass tần số 1000Hz và giảm âm lượng dần trong 2.0s.
*   **Đồng hồ Monospace không giật chữ:** Thiết lập font chữ đơn rộng (`Courier New` hoặc `monospace`) cho bộ đếm ngược để chiều rộng ký tự không thay đổi khi chữ số nhảy, loại bỏ hiện tượng giật lắc bố cục xung quanh.

---

## 3. Quy chuẩn Cỡ chữ Lớp học lớn (Classroom Typography)
*   **Phân cấp Kích thước Chữ tối thiểu:**
    *   *Tiêu đề slide chính:* **36px - 44px** (chữ đậm, viết hoa).
    *   *Tiêu đề phụ / Slogan:* **22px - 26px**.
    *   *Văn bản thân / Mô tả hoạt động / Nhãn thẻ:* **20px - 24px**.
    *   *Nội dung chi tiết bảng biểu:* **18px - 20px**.
    *   *Sidebar menu điều hướng:* **15px - 18px** (vừa đủ Legible nhưng không chiếm dụng không gian hiển thị slide).
*   **Phóng to Khung chứa (.slide-frame):** Tăng kích thước tối đa lên **`1180px`** và đặt `overflow-y: auto` để tự động thêm thanh cuộn dọc khi font chữ phóng to làm tràn nội dung, ngăn ngừa chữ bị đè chéo hay mất thông tin.

---

## 4. Kiểm định Chất lượng và Kiểm soát Viết hoa (Vietnamese QA Rules)
*   **Quy tắc số thứ tự:** Viết hoa chữ cái đầu tiên ngay sau số thứ tự hoặc ký tự đầu dòng (ví dụ: `1. Nói to, rõ ràng` thay vì `1. nói to, rõ ràng`).
*   **Từ chuyên ngành giữa câu:** Chỉ viết thường các từ chỉ bệnh học, vết thương hoặc kỹ thuật y khoa khi đứng giữa câu (ví dụ: `uốn ván`, `sơ cứu`, `chảy máu cam` không được viết hoa ngẫu hứng).
*   **Đối chiếu trực quan:** Trình bày rõ ràng hai trạng thái đối lập **❌ Sai lầm nguy hiểm** ➔ **✅ Sơ cứu đúng chuẩn** bằng các bảng thẻ có màu sắc tương phản mạnh (Đỏ nhạt vs Xanh lục nhạt) để học sinh dễ ghi nhớ cơ chế sinh lý bị tàn phá.
