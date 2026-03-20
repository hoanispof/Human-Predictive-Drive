# Plan: Web Visualization — Framework Interactive

> **Trạng thái:** Ý TƯỞNG — chưa triển khai
> **Khi nào:** SAU v8.0 stable + đã có external feedback
> **Tại sao chờ:** Framework đang draft → thay đổi → sửa html tốn × 2

---

## 1. Kiến Trúc 2 Phần

```
PHẦN 1: .md files (CHO AI + người nghiên cứu)
  → Toàn bộ framework chi tiết (như hiện tại)
  → AI đọc → người dùng hỏi AI → phân tích chuyên sâu bất kỳ chủ đề
  → = "Backend knowledge" — không cần đẹp, cần CHÍNH XÁC + ĐẦY ĐỦ

PHẦN 2: HTML/JSX web (CHO người dùng phổ thông)
  → Trực quan, dễ hiểu, thân thiện
  → Tiếp cận ban đầu → tò mò → muốn tìm hiểu sâu → dẫn tới .md + AI
  → = "Frontend" — cần ĐẸP + DỄ HIỂU + ĐA NGÔN NGỮ
```

---

## 2. Cấu Trúc Web

```
⚠️ NGUYÊN TẮC: HOOK trước, DEPTH sau (giống game casual: fun TRƯỚC, tutorial SAU)
  → Người dùng ĐẾN vì CÂU HỎI CỦA HỌ → không phải vì "xem kiến trúc framework"
  → Landing page = câu hỏi quen thuộc → KHÔNG phải sơ đồ technical
  → Framework architecture = trang PHỤ cho người MUỐN hiểu sâu

⚠️ PHÂN PHỐI: Deep link per audience (không phải 1 landing page cho tất cả)
  → Mỗi NGUỒN marketing → dẫn ĐÚNG trang phù hợp audience đó:
    FB page tâm lý → "/tai-sao-khong-hanh-phuc"
    FB group parenting → "/nuoi-con-hanh-phuc"
    TikTok burnout → "/tai-sao-burnout"
    Google SEO → mỗi bài = 1 URL riêng → SEO per câu hỏi
  → Người dùng VÀO ĐÚNG trang CỦA HỌ → đọc NGAY → không cần navigate
  → Cuối bài: "câu hỏi liên quan" → explore thêm
  → = GIỐNG game casual: người chơi vào thẳng gameplay, không qua menu phức tạp

═══════════════════════════════════════════════════════════
TRANG CHÍNH — "Bạn đang thắc mắc gì?" (HOOK page)
═══════════════════════════════════════════════════════════

  → Tiêu đề: "Bạn đang thắc mắc gì?"
  → CHỈ 3 cards lớn (câu hỏi HOT nhất) + "Xem thêm →" + Search bar
  → 3 giây biết click đâu → KHÔNG chóng mặt
  → Thiết kế: clean, warm, KHÔNG academic, giống blog/magazine
  → (Đa số traffic KHÔNG vào homepage → vào DEEP LINK per source → homepage = fallback)

  TIER 1 — Làm TRƯỚC (max overlap, triệu người thắc mắc):

    ① "Tại sao tôi không hạnh phúc dù có đủ?"
       → LEAD content — hook MẠNH NHẤT
       → Framework: Amplifier Trap (Lớp 2 dominant + Lớp 1 thiếu)
       → "À ha!": "6 thứ cơ thể cần → bạn đang thiếu 2-3 cái"

    ② "Tại sao biết nên làm mà vẫn lười/trì hoãn?"
       → Ai cũng bị → relate NGAY
       → Framework: verbal "biết" ≠ body "muốn" (khác modality)
       → "À ha!": "biết = 1/6 brain → 5/6 CHƯA đồng ý"

    ③ "Tại sao scroll MXH mãi rồi thấy trống rỗng?"
       → Hiện đại, viral potential CAO
       → Framework: Hijacked Empty (dopamine có, opioid = 0)
       → "À ha!": "not broken — bị hack bởi dopamine loop"

    ④ "Tại sao chán nhanh / không tập trung được?"
       → Gen Z + MXH users relate MẠNH
       → Framework: 5 loại chán KHÁC NHAU → khác fix
       → "À ha!": "5 loại chán → bạn thuộc loại NÀO?"

    ⑤ "Làm sao nuôi con hạnh phúc + giỏi?"
       → Phụ huynh = audience SẴN SÀNG đầu tư thời gian đọc
       → Framework: 3 Layers (Pressure + Challenge + Autonomy)
       → "À ha!": "không phải ép HAY thả → cần CẢ 3 đúng tỉ lệ"

  TIER 2 — Làm SAU (phổ biến, specific hơn):

    ⑥ "Tại sao biết sai mà vẫn làm?" (nghiện, thói quen xấu)
    ⑦ "Tại sao relationship cứ lặp pattern cũ?"
    ⑧ "Tại sao burnout dù yêu công việc?"
    ⑨ "Tại sao quarter-life / mid-life crisis?"
    ⑩ "Tìm đam mê / mục đích sống thế nào?"

  TIER 3 — Niche nhưng engagement cao:

    ⑪ "Tại sao người thành công vẫn khổ?"
    ⑫ "Tại sao ghét học dù biết cần?"
    ⑬ "Tại sao 2 anh em cùng nhà khác tính?"
    ⑭ "Thiền / mindfulness có thật sự work?"

  FORMAT mỗi bài:
    → 1 CÂU HỎI quen thuộc = HOOK (tiêu đề)
    → Giải thích NGẮN 500-1000 từ, ngôn ngữ đời thường
    → "À ha!" moment (insight đọc xong "đúng rồi!")
    → Cuối: "muốn hiểu sâu hơn? → xem Framework / hỏi AI"
    → = Bài BLOG chất lượng, KHÔNG phải paper academic

═══════════════════════════════════════════════════════════
TAB "Framework" — Kiến trúc Interactive (cho người tò mò)
═══════════════════════════════════════════════════════════

  → Khung KIẾN TRÚC trực quan:
    Container (Môi Trường) bao quanh
    ┌─ T1: Hardware (body + brain) ─┐
    │  T2: Software (schema gradient) │
    │  T3: Hành Vi (output)           │
    └─────────────────────────────────┘
    Domain (chiều ngang)

  → Mỗi phần: CLICK VÀO → mở chi tiết
  → Thiết kế: clean, minimal, interactive
  → = Cho người ĐÃ đọc bài Tier 1 → muốn hiểu CƠ CHẾ đằng sau

  CLICK VÀO từng phần:
    T1 Hardware → mở: Neurochemistry 3 Lớp + PFC + Modality
    T2 Software → mở: Schema Gradient + Body Baseline + Schema-Drive
    T3 Hành Vi → mở: Drive Equation + 3 con đường fulfill
    Container → mở: 6 nhóm Body-Needs tổng quan
    Domain → mở: Domain clusters + Schema × Domain mapping

  MỖI trang chi tiết:
    → Khung kiến trúc NHỎ (context: đang ở đâu trong tổng thể)
    → Mục lục phần đó
    → Giải thích từng thành phần — ngôn ngữ ĐƠN GIẢN, ví dụ QUEN THUỘC
    → Link → đọc sâu hơn (hoặc dẫn tới .md + AI)

═══════════════════════════════════════════════════════════
TAB "Ứng Dụng" (Applications)
═══════════════════════════════════════════════════════════

  → Hiểu bản thân (Body-Needs self-check)
  → Giáo dục con cái (Parenting qua framework)
  → Cân bằng động lực (Drive Optimization)
  → Phân tích ngành nghề (Industry-Serve)
  → Hiểu cơ chế nghiện (Addiction)

═══════════════════════════════════════════════════════════
TAB "Nghiên Cứu" (Research)
═══════════════════════════════════════════════════════════

  → Công nghệ tín ngưỡng (Religion qua framework)
  → Thiên tài ẩn (Hidden Genius)
  → Cảm xúc con người (Emotion Map)
  → Trí tưởng tượng (Imagination)
  → Phân tích PFC (não bộ ý thức)

═══════════════════════════════════════════════════════════
TAB "Về Framework"
═══════════════════════════════════════════════════════════

  → Lịch sử phát triển (v1→v8)
  → Giới hạn + honest assessment
  → Cách đóng góp / feedback
  → Epistemological Position
```

---

## 3. Ngôn Ngữ

```
NGUYÊN TẮC:

  Thuật ngữ FRAMEWORK giữ tiếng Anh (xuyên suốt mọi ngôn ngữ):
    → Dopamine, Cortisol, Opioid, Oxytocin, Serotonin
    → Experience, Connection, Novelty, Status
    → Schema, Schema-Drive, PFC, ACC, vmPFC
    → Body Baseline, Threshold, Modality
    → → Lý do: ổn định verbal, dễ trao đổi quốc tế, tránh dịch sai

  Nội dung giải thích: NGÔN NGỮ BẢN ĐỊA
    → Mô tả, ví dụ, giải thích → tiếng Việt / English / etc.
    → Ưu tiên: đơn giản, quen thuộc, KHÔNG academic
    → "Schema là cách não bạn tổ chức kinh nghiệm" (dễ hiểu)
    → KHÔNG: "Schema is a cognitive representational framework" (academic)

  Hỗ trợ ngôn ngữ ban đầu:
    → Tiếng Việt (primary — tác giả)
    → English (secondary — reach rộng nhất)
    → Thêm sau: JP, KR, CN, ... (nếu demand)
```

---

## 4. Quy Trình Triển Khai

```
BƯỚC 1 (hiện tại): GHI NHẬN ý tưởng → file này ✅
BƯỚC 2 (v8.0): Framework stable → review lần cuối
BƯỚC 3 (sau v8.0): Design mockup trang chính (1 trang, static)
BƯỚC 4: Build prototype HTML/JSX (trang chính + 1-2 sub-pages)
BƯỚC 5: Test: cho 5-10 người dùng thử → feedback
BƯỚC 6: Iterate → mở rộng thêm sub-pages
BƯỚC 7: Thêm ngôn ngữ (EN → VN song song → rồi thêm)

TECH STACK (dự kiến):
  → React/Next.js (JSX, component-based, dễ maintain)
  → i18n (multi-language support)
  → Markdown rendering (có thể embed .md content vào web)
  → Interactive diagrams (D3.js hoặc tương tự cho kiến trúc)
  → Responsive (mobile + desktop)

⚠️ KHÔNG làm bây giờ → framework ĐANG thay đổi → html sẽ phải sửa liên tục
→ Chờ stable → build 1 lần → chất lượng cao
→ = Đúng nguyên tắc framework: "chậm mà chắc"
```

---

> *Plan Web Visualization — ghi nhận ý tưởng, triển khai SAU v8.0*
