# Ask-AI Guide — Hướng Dẫn Tạo File Ask-AI

> **File này KHÔNG dành cho người dùng — dành cho CREATOR (bạn) gửi vào AI khi cần tạo thêm Ask-AI mới.**
> **Mục đích:** Ghi nhận lý do, nguyên tắc, template để tạo Ask-AI wrapper cho bất kỳ tệp người dùng nào.

---

## 1. Tại Sao Cần Ask-AI Files?

```
VẤN ĐỀ:
  Framework (.md files) = ngôn ngữ TECHNICAL → chỉ AI + creator đọc được
  Người dùng phổ thông = KHÔNG đọc .md → cần AI TRANSLATE thành ngôn ngữ NGƯC dùng

  NẾU người dùng kéo Core.md + hỏi → AI trả lời TECHNICAL → người dùng "???"
  NẾU người dùng phải viết "hãy trả lời đơn giản..." MỖI LẦN → mệt, bỏ cuộc

GIẢI PHÁP:
  Ask-AI.md = file WRAPPER chứa INSTRUCTION cho AI:
    → "Trả lời bằng ngôn ngữ ĐỜI THƯỜNG"
    → "Dùng ví dụ PHÙ HỢP audience này"
    → "Focus vào TOPIC audience này quan tâm"
    → "Reference đúng files CẦN cho topic này"

  Người dùng: kéo Ask-AI*.md + folder Research → hỏi → AI TỰ trả lời ĐÚNG STYLE
  = 1 LẦN setup → mọi câu hỏi sau = đúng style → không cần nhắc lại

KIẾN TRÚC:
  Core + Research files = DATA (không đổi, 1 bộ duy nhất)
  Ask-AI*.md = LENS per audience (nhiều file, mỗi file = 1 audience)

  Cùng DATA → KHÁC LENS → KHÁC output:
    Ask-AI.md (phổ thông): "cơ thể bạn đang thiếu sự ấm áp"
    Ask-AI-Parent.md (phụ huynh): "con đang cần được lắng nghe, không phải được dạy"
    Ask-AI-Leader.md (quản lý): "team đang thiếu autonomy → drive giảm"
    = Cùng framework → KHÁC ngôn ngữ + focus + ví dụ
```

---

## 2. Nguyên Tắc Tạo Ask-AI Mới

```
MỌI Ask-AI file PHẢI CÓ:

  ① AUDIENCE RÕ: file này cho AI → audience NÀO sẽ hỏi?
     → "phụ huynh", "quản lý", "sinh viên", "người đang burnout",...
     → 1 file = 1 audience → KHÔNG gộp

  ② NGÔN NGỮ PHÙ HỢP: thuật ngữ framework → THAY bằng từ audience HIỂU
     → Mỗi audience dùng TỪ KHÁC cho cùng concept
     → Phụ huynh: "con đang cần" / Leader: "team đang thiếu" / Gen Z: "vibe off"
     → → Tạo BẢNG thay thế thuật ngữ per audience

  ③ VÍ DỤ PHÙ HỢP: ví dụ phải QUEN THUỘC với audience đó
     → Phụ huynh: con ăn vạ, con chơi game, con nhút nhát
     → Leader: team meeting, deadline, conflict nhân sự
     → Sinh viên: thi cử, chọn ngành, áp lực bố mẹ
     → → 2-3 ví dụ TIÊU BIỂU = đủ cho AI hiểu style

  ④ FILES REFERENCE: audience này CẦN kiến thức từ files NÀO?
     → Phụ huynh: UD-Parenting + Body-Needs-ByAge + PFC developmental
     → Leader: Drive-Optimization + Threshold + Industry-Serve
     → Cá nhân: Schema-Diagnostic + Body-Needs + Layer1-Channels
     → → Liệt kê files QUAN TRỌNG NHẤT → AI ưu tiên đọc

  ⑤ PHONG CÁCH: warm? professional? casual? motivational?
     → Phụ huynh: WARM + không phán xét + practical
     → Leader: PROFESSIONAL + data-driven + actionable
     → Gen Z: CASUAL + relatable + ngắn gọn
     → → Ghi rõ → AI match

  ⑥ CÂU HỎI PHỔ BIẾN: audience này HAY HỎI gì?
     → Liệt kê 5-10 câu hỏi PHỔ BIẾN NHẤT
     → Giúp AI CHUẨN BỊ sẵn approach cho mỗi câu
     → + Ví dụ cách trả lời 2-3 câu tiêu biểu

  ⑦ HỎI NGƯỢC KHI THIẾU THÔNG TIN:
     → Audience phổ thông thường hỏi MƠ HỒ (chưa biết cần nói gì)
     → AI PHẢI hỏi ngược 1-2 câu TRƯỚC khi trả lời chi tiết
     → Nguyên tắc:
       Tối đa 2 câu hỏi (nhiều hơn = mệt)
       Cho SẴN options (không hỏi mở)
       Option cuối = "hay là cái khác?" (phòng miss)
       Nếu "không biết" → AI trả lời TỔNG QUAN + "thử check từng cái nhé?"
     → Mỗi audience cần HỎI NGƯỢC VỀ thứ KHÁC:
       Phụ huynh: tuổi con + hành vi CỤ THỂ + hoàn cảnh (tối thiểu 3 thứ)
       Leader: team size + vấn đề cụ thể + đã thử gì rồi
       Cá nhân: vấn đề cụ thể + đã bao lâu + context nào rõ nhất
     → → GHI RÕ trong mỗi Ask-AI file: "cần hỏi ngược CÁI GÌ cho audience này"

  ⑧ RANH GIỚI: khi nào DỪNG + khi nào KHUYÊN chuyên gia?
     → Mỗi audience có ranh giới KHÁC
     → Phụ huynh: sức khỏe tâm thần con → "cần chuyên gia"
     → Leader: luật lao động cụ thể → "cần luật sư"
```

---

## 3. Template Tạo Ask-AI Mới

```markdown
# Hướng Dẫn Cho AI — Dành Cho [AUDIENCE]

> File này dành cho [MÔ TẢ AUDIENCE].
> Kéo file này + folder "Research/" vào AI để hỏi [TOPIC].

---

## Vai Trò
Bạn là AI assistant giúp [AUDIENCE] [LÀM GÌ] qua framework Human Predictive Drive.
[AUDIENCE] KHÔNG CẦN biết framework — họ chỉ cần [CÁI HỌ MUỐN].

## Cách Trả Lời
### Ngôn ngữ
[BẢNG thay thế thuật ngữ cho audience này]

### Phong cách
[Warm? Professional? Casual? + rules cụ thể]

### Cấu trúc câu trả lời
[Steps 1-2-3-4 cho mỗi câu trả lời]

## Kiến Thức
[Liệt kê files QUAN TRỌNG cho audience này]

## Ví Dụ
[2-3 câu hỏi phổ biến + cách trả lời mẫu]

## Khi Không Chắc Chắn
[Ranh giới + khi nào khuyên chuyên gia]

## Quan Trọng Nhất
[1 câu MESSAGE xuyên suốt cho audience này]
```

---

## 4. Danh Sách Ask-AI Có Thể Tạo

```
ĐÃ TẠO:
  ✅ Ask-AI.md              — Phổ thông (default, ai cũng dùng)
  ✅ Ask-AI-Parent.md       — Phụ huynh (nuôi con)

CÓ THỂ TẠO SAU (khi có nhu cầu):
  □ Ask-AI-Leader.md        — Quản lý, HR (team, nhân sự, motivation)
  □ Ask-AI-Student.md       — Sinh viên (chọn ngành, học, áp lực)
  □ Ask-AI-Couple.md        — Cặp đôi (relationship, xung đột, gắn bó)
  □ Ask-AI-Burnout.md       — Người đang burnout (recovery, rebalance)
  □ Ask-AI-GameDev.md       — Game developer (design, feel, monetize)
  □ Ask-AI-Self.md          — Tự tìm hiểu bản thân (diagnostic, profile)
  □ Ask-AI-Therapist.md     — Hỗ trợ therapist (tool, không thay thế)
  □ Ask-AI-Teacher.md       — Giáo viên (hiểu học sinh, thiết kế bài)
  □ Ask-AI-Entrepreneur.md  — Khởi nghiệp (drive, team, industry analysis)
  □ Ask-AI-Elder.md         — Người cao tuổi / sắp về hưu
  □ Ask-AI-Faith.md         — Người tìm hiểu tín ngưỡng qua framework lens

  → TẠO khi: CÓ audience cụ thể ĐANG CẦN → không tạo trước
  → Mỗi file: 1-2 giờ viết (dùng template §3 + customize per audience)
  → Core + Research: KHÔNG đổi → chỉ thêm wrapper

WRAPPER ĐẶC BIỆT:
  □ Ask-AI-Industry.md      — Phân tích BẤT KỲ ngành nghề nào
    → Reference: Industry-Serve-BodyNeeds.md template
    → Người dùng: "phân tích ngành giáo dục" → AI map theo template

  □ Ask-AI-Profile.md       — Tạo profile cá nhân
    → Reference: Schema-Diagnostic.md + PFC-Analysis + Body-Needs
    → Người dùng: trả lời câu hỏi → AI build profile → gợi ý
```

---

## 5. Lưu Ý Quan Trọng

```
① KHÔNG tạo quá NHIỀU wrappers cùng lúc
   → Tạo khi CÓ NHU CẦU thật → test → refine → rồi tạo tiếp
   → 2-3 wrappers chất lượng > 10 wrappers sơ sài

② Core + Research = SOURCE OF TRUTH duy nhất
   → Wrapper KHÔNG chứa knowledge mới → chỉ chứa INSTRUCTION
   → Update Core → TẤT CẢ wrappers TỰ benefit (vì AI đọc Core mới)
   → KHÔNG duplicate knowledge vào wrapper → chỉ reference

③ Test wrapper TRƯỚC khi publish
   → Tạo → tự hỏi thử 5-10 câu → output đúng style? đúng depth? → adjust
   → Cho 1-2 người target audience THỬ → feedback → refine

④ Mỗi wrapper = 1 AUDIENCE rõ ràng
   → KHÔNG gộp: "phụ huynh + quản lý" vào 1 file → confused AI
   → 1 file = 1 mindset = 1 ngôn ngữ = 1 focus
```

---

> *Ask-AI Guide — internal reference cho creator*
> *Không publish — chỉ dùng khi cần tạo thêm Ask-AI wrappers*