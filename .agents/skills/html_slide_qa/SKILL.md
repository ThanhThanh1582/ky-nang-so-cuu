---
name: html_slide_qa
description: Skill for automatically validating HTML slides capitalization (via python check script) and auditing Vietnamese spelling & grammar (via LLM check on extracted slide texts) to ensure medical lesson slides look professional and correct.
---

# Quy trình kiểm định chất lượng Slide HTML (HTML Slide QA Skill)

Skill này hướng dẫn quy trình kiểm tra tự động và thẩm định thủ công chất lượng nội dung slide HTML về viết hoa chữ cái đầu dòng, chính tả tiếng Việt, và ngữ pháp.

## 1. Mục tiêu kiểm tra
- **Viết hoa đầu dòng:** Đảm bảo tất cả các thẻ lá (như `<li>`, `<p>`, `<h1>`-`<h6>`, `<td>`, và `<div>` chứa dòng văn bản đơn lẻ) đều phải viết hoa chữ cái đầu dòng.
  - *Ví dụ sai:* `<li>sát trùng mép vết thương</li>`
  - *Ví dụ đúng:* `<li>Sát trùng mép vết thương</li>`
- **Chính tả tiếng Việt:** Phát hiện các từ gõ sai, thiếu ký tự, nhầm lẫn dấu (hỏi/ngã, sắc/nặng), hoặc gõ sai phụ âm đầu/cuối.
  - *Ví dụ sai:* `sơ kứu`, `bng gạc`, `vết thươg`
  - *Ví dụ đúng:* `sơ cứu`, `bông gạc`, `vết thương`
- **Ngữ pháp & Cú pháp:** Đảm bảo câu văn rõ ràng, mạch lạc, đúng cấu trúc câu tiếng Việt chuẩn y khoa học đường.

## 2. Quy trình thực hiện của QA Agent
1. **Bước 1: Chạy công cụ kiểm tra tự động (Capitalization & Text Extraction)**
   - Chạy script Python:
     ```powershell
     python .agents/skills/html_slide_qa/scripts/check_capitalization.py
     ```
   - Script này sẽ:
     - In ra các dòng vi phạm viết hoa đầu dòng trực tiếp trên terminal.
     - Trích xuất toàn bộ văn bản sạch của slide lưu tại `.agents/temp_slide_text.txt`.

2. **Bước 2: Phân tích chính tả và ngữ pháp**
   - Đọc nội dung tệp `.agents/temp_slide_text.txt`.
   - Sử dụng mô hình ngôn ngữ để đọc qua từng dòng văn bản sạch, phát hiện các từ sai chính tả hoặc câu văn lủng củng, sai ngữ pháp.

3. **Bước 3: Lập báo cáo lỗi tổng hợp (QA Report)**
   - Tổng hợp tất cả các lỗi tìm thấy (cả viết hoa từ script Python và chính tả/ngữ pháp từ mô hình) thành một bảng báo cáo có định dạng sau:

   | Slide ID | Dòng (Line) | Loại lỗi | Nội dung hiện tại | Đề xuất sửa đổi | Ghi chú |
   |---|---|---|---|---|---|
   | S8 | 579 | Viết hoa | `sát trùng mép vết thương` | `Sát trùng mép vết thương` | Thiếu viết hoa chữ cái đầu dòng `s` |
   | S8B | 220 | Chính tả | `Bng gạc vô trùng` | `Bông gạc vô trùng` | Sai lỗi chính tả từ `Bng` |

4. **Bước 4: Yêu cầu sửa đổi**
   - Nếu phát hiện bất kỳ lỗi nào, QA Agent phải báo cáo và hướng dẫn Developer Agent hoặc người dùng thực hiện sửa đổi cụ thể trong tệp `index.html`.
