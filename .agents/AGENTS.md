# Quy tắc Phát triển và Kiểm định Slide Y khoa (Nova Hospital Project Rules)

Tệp này chứa các hướng dẫn và ràng buộc bắt buộc áp dụng cho toàn bộ dự án thiết kế slide bài giảng Nova Hospital.

---

## 1. Quy trình Phát triển Bắt buộc (Developer Agent Rules)
- **Kiểm định trước khi hoàn tất:** Mỗi khi tạo mới slide, thay đổi hoặc cập nhật mã nguồn HTML (`index.html`), lập trình viên/agent phát triển **bắt buộc** phải chạy công cụ kiểm tra viết hoa hoặc yêu cầu `html_slide_qa_agent` chạy quy trình QA.
- **Giải quyết triệt để lỗi trước khi chuyển giao:** Không bàn giao hoặc đóng gói dự án nếu công cụ kiểm tra hoặc QA Agent phát hiện thấy lỗi viết hoa, chính tả, hay ngữ pháp.

---

## 2. Vai trò và Ràng buộc của QA Agent (`html_slide_qa_agent`)
- **Tên Agent:** `html_slide_qa_agent`
- **Mô tả:** Chuyên viên kiểm định chất lượng slide, chịu trách nhiệm rà soát lỗi viết hoa đầu dòng, lỗi chính tả tiếng Việt và lỗi cấu trúc ngữ pháp.
- **Quy trình làm việc:**
  1. Chạy kịch bản Python `.agents/skills/html_slide_qa/scripts/check_capitalization.py` để tìm lỗi viết hoa đầu dòng và trích xuất text sạch.
  2. Rà soát lỗi chính tả và ngữ pháp tiếng Việt dựa trên tệp `.agents/temp_slide_text.txt` đã được trích xuất.
  3. Xuất bảng báo cáo QA Report chi tiết (Slide ID, số dòng, loại lỗi, đề xuất sửa).
  4. Nếu có lỗi, yêu cầu sửa đổi cụ thể cho đến khi toàn bộ lỗi được khắc phục.
  5. Kiểm soát viết hoa sau số thứ tự/danh sách (như `1. Sơ cứu`): Phải viết hoa ký tự chữ cái đầu tiên đứng sau ký số thứ tự và dấu chấm/gạch đầu dòng.
  6. Đồng bộ hóa chữ viết thường giữa câu: Nghiêm cấm viết hoa ngẫu hứng từ ngữ chuyên ngành ở giữa câu (ví dụ: cấm viết `"Uốn ván"`, phải viết là `"uốn ván"` khi đứng giữa câu).

---

## 3. Quy tắc Chuyển đổi Thiết kế Lesson Design sang Slide Chi tiết (Slide Flow & Game Rules)
- **Nguyên tắc "Không Trình bày sau Game":** Khi chuyển đổi hoạt động game/trắc nghiệm/khảo sát số hóa (TH01) có kèm kết quả đáp án chuẩn y khoa (ĐA01), tuyệt đối không chèn slide trình bày/phản biện (TB01) ở giữa. Học sinh chơi game xong sẽ được điều hướng trực tiếp tới slide đáp án chuẩn để đối chiếu kết quả tức thời, tăng tính liền mạch và hiệu quả sư phạm.
- **Tiêu chuẩn thiết kế Game nối SVG:** Đối với các hoạt động phân tích/chẩn đoán kết nối cặp thông tin, ưu tiên sử dụng cơ chế game nối (chạm chọn thẻ ở hai cột) được biểu diễn trực quan bằng đường vẽ SVG động thay cho kéo thả. Giao diện này đảm bảo độ nhạy 100% trên bảng thông minh cảm ứng (Touch Smartboard), không bị lỗi trượt mục tiêu kéo thả và phải tự động cập nhật lại tọa độ khi màn hình co giãn (`window.resize`).
