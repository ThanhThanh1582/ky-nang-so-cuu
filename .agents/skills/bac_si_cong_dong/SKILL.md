---
name: bac_si_cong_dong
description: Skill for designing and developing Lesson 2 (Bác sĩ Cộng đồng Concept) medical slides, featuring interactive patient grids, touch-friendly smartboard matching games, Web Audio API alarms, and strict compliance with the Nova Hospital project rules.
---

# Kỹ năng Thiết kế Slide Tương tác Bác sĩ Cộng đồng (Tiết 2)

Tài liệu này đúc kết toàn bộ phương pháp luận, tiêu chuẩn lập trình, và hướng dẫn thiết kế giao diện tương tác số hóa áp dụng cho **Tiết 2: Bác sĩ Cộng đồng**.

---

## 1. Phương pháp luận & Ý tưởng Chủ đạo (Doctor Concept)
*   **Vai trò học sinh:** Học sinh đóng vai các *Đại sứ Sức khỏe Cộng đồng* thực hiện chiến dịch khảo sát, bài trừ ngộ nhận dân gian tại trường học.
*   **Luồng hoạt động sư phạm:**
    *   **Khởi động & Ôn tập (Slide 1 - 6):** Đối chiếu các lỗi sai sơ cứu thường gặp thông qua thảo luận phản biện chéo và đối chiếu kết quả đáp án chuẩn.
    *   **Nhận nhiệm vụ chiến dịch (Slide 7 - 10):** Giao nhiệm vụ khảo sát thực trạng sức khỏe học đường.
    *   **Khảo sát & Phân tích nguy cơ (Slide 11 - 16):** Đọc ca lâm sàng thực tế, chơi game kết nối nguyên nhân sơ cứu sai với các biến chứng sinh lý tương ứng.
    *   **Thiết kế cẩm nang & Diễn tập (Slide 17 - 22):** Thiết kế poster truyền thông bỏ túi và huấn luyện quấn băng gạc tĩnh mạch hướng tim.
    *   **Tổng kết & Vinh danh (Slide 23 - 26):** Bản cam kết y đức của Đại sứ và lễ phong tặng chứng nhận vinh danh.

---

## 2. Tiêu chuẩn Lập trình các Linh kiện Tương tác (Interactive Components)

### A. Lưới hồ sơ bệnh án điện tử (Interactive Patient Grid)
*   Sử dụng thẻ `div` với lớp `.nv01-tablet-card` hiển thị tên, giường bệnh và nút xem chi tiết.
*   Gắn sự kiện `onclick="openPatientModal('patientId')"` để hiển thị hộp thoại pop-up chứa thông tin bệnh án chi tiết từ đối tượng dữ liệu tĩnh (`patientData`).
*   Hộp thoại modal sử dụng cấu trúc `.modal-overlay` có nền mờ đục phủ toàn màn hình, đóng lại khi nhấp ngoài vùng `.modal-content` hoặc nhấp nút đóng `&times;`.

### B. Game kết nối chẩn đoán / phân tích biến chứng
*   **Hỗ trợ Smartboard kép:** Cung cấp cả sự kiện kéo thả tiêu chuẩn (`ondragstart`, `ondrop`, `ondragover`) và sự kiện click tương đương (`selectCardTouch(this)` và `handleSlotTouch(this, 'diag')`) để tránh lỗi trượt mục tiêu kéo thả trên màn hình lớn.
*   **Đồng bộ logic kiểm tra:** Hàm `checkDiagGameT2()` đối chiếu các giá trị lưu trữ trong đối tượng `diagData` của từng ô thả (`drop-14-...`) với các ID thẻ tương ứng:
    *   *Nguyễn Gia An:* Sơ cứu sai (`diag-s1` - nhái lá bàng) ➔ Biến chứng (`diag-b1` - uốn ván kị khí).
    *   *Phạm Bình Minh:* Sơ cứu sai (`diag-s2` - kem đánh răng) ➔ Biến chứng (`diag-b2` - hoại tử tích nhiệt).
    *   *Trần Hoàng Nam:* Sơ cứu sai (`diag-s3` - ngửa cổ nhét giấy) ➔ Biến chứng (`diag-b3` - sặc máu phổi).

### C. Quy trình băng bó hướng tim & capillary refill (Slide t2-20)
*   **Kỹ thuật quấn băng gạc:** Huấn luyện nguyên tắc quấn từ ngọn chi (xa tim) ngược dần về gốc chi (gần tim) để hỗ trợ tuần hoàn máu trở về tim hiệu quả.
*   **Kiểm tra thắt nghẹt:** Nhấn nhẹ đầu móng tay bị quấn, đạt chuẩn an toàn y khoa khi móng tay hồng hào trở lại sau **tối đa 2 giây** (Capillary Refill Test).

---

## 3. Hệ thống Cảnh báo & Âm thanh Nhân tạo (Web Audio API)
*   **Báo động đỏ (Siren Alarm):** Kích hoạt hiệu ứng nhấp nháy đỏ trên màn hình hiển thị `.flash-red` kèm còi hú báo động sinh từ Web Audio API oscillators:
    ```javascript
    function playSiren() {
        let osc1 = audioCtx.createOscillator();
        let osc2 = audioCtx.createOscillator();
        let gainNode = audioCtx.createGain();
        // Quét tần số lặp từ 800Hz lên 1200Hz và ngược lại trong 2.5 giây
        ...
    }
    ```
*   **Kích hoạt tương tác:** Tránh tự động chạy âm thanh khi tải trang do chính sách bảo mật của trình duyệt. Chỉ khởi tạo hoặc phục hồi `AudioContext` sau sự kiện nhấp chuột của người dùng.

---

## 4. Ràng buộc Kiểm định Chất lượng Slide (Vietnamese QA Compliance)
*   **Không trình bày sau Game:** Sau khi hoàn thành hoạt động thực hành hoặc game tương tác, chuyển hướng trực tiếp học sinh tới slide đáp án để đối chiếu kết quả y khoa chuẩn, tuyệt đối không chèn các slide giải thích trung gian rườm rà.
*   **Nhất quán chính tả:** Viết đúng các từ ngữ chuyên môn:
    *   Sử dụng chữ viết thường cho từ chuyên ngành đứng giữa câu (ví dụ: `uốn ván`, `sơ cứu`, `bỏng`, `chảy máu cam`).
    *   Đồng bộ cách viết chữ `y` dài trong từ `kỹ thuật` (tránh viết `kĩ thuật` không nhất quán).
*   **Đồng bộ thông tin nhân vật:** Đảm bảo giới tính nhân vật và biểu tượng cảm xúc (emoji) đồng bộ trên tất cả các slide (ví dụ: `Lê Minh Quân` luôn đi kèm emoji bé trai `👦`).
