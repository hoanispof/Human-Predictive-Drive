# Plan: Neuroscience Posts — 2 Blog + 2 Short Posts

> **Mục tiêu:** Tạo 2 bài blog neuroscience + 2 short post dẫn link. Phục vụ VERIFY từ chuyên gia.
> **Vị trí trong chiến lược:** Đây là content ĐẦU TIÊN ra ngoài. Neuro posts đi trước tech post.
> **Nguyên tắc:** hypothesis inviting falsification. Giọng ngang hàng, không giảng dạy.
> **Trạng thái:** PLANNING
> **Ngày tạo:** 2026-05-26
> **Liên kết:**
>   plan-public.md — framing rules (W.4, W.5)
>   plan-tech-distribution.md — broader distribution strategy
>   framing-engagement-value.md — 3-tầng value model
>   01-Dopamine-Not-Reward.md — draft có sẵn cho Topic 1
>   expert-verification-map.md — routing claims tới đúng expert group

---

## §1 — 4 BÀI, 2 TẦNG

```
  TẦNG 1: BLOG POST (dài, chi tiết, có citation)
    → Blog A: Dopamine Is Not Reward
    → Blog B: Cortisol — Optimize the Inverted-U, Not Eliminate It

  TẦNG 2: SHORT POST (ngắn, dẫn link tới blog)
    → Short A: dẫn → Blog A
    → Short B: dẫn → Blog B

  LOGIC:
    Short post = HOOK + 1 insight cụ thể + link
    Blog post = FULL argument + evidence + falsification criteria
    Chuyên gia đọc short → tò mò → click blog → verify → engage

  THỨ TỰ XUẤT BẢN:
    Blog A trước → Short A → Blog B → Short B
    (Blog phải sẵn TRƯỚC short post, vì short dẫn link)
```

---

## §2 — BLOG A: DOPAMINE IS NOT REWARD

### 2.1 — Mục tiêu

```
  CLAIM CHÍNH: Dopamine = salience signal, KHÔNG PHẢI reward.
  AUDIENCE: neuroscientists, psychologists, cognitive scientists
  KẾT QUẢ MONG MUỐN:
    → Chuyên gia verify: "evidence checks out" hoặc "sai ở chỗ X"
    → CẢ HAI = outcome tốt (verify HOẶC falsify = đều có giá trị)
  DRAFT CÓ SẴN: 01-Dopamine-Not-Reward.md (refine từ đây)
```

### 2.2 — Cấu trúc blog

```
  ① HOOK: Misconception phổ biến + tại sao nó tồn tại
     → "Dopamine = reward chemical" xuất hiện ở đâu? Textbook nào? Pop science nào?
     → Tại sao belief này persistent dù research nói khác?

  ② EVIDENCE: Research cứng
     → 4 direct manipulation tests (Liggins 2012, dopamine agonist, optogenetics, Berridge 2007)
     → Wanting vs liking distinction (Berridge & Robinson)
     → Naltrexone evidence (opioid block → reward block, dù dopamine còn)

  ③ REFRAME: Dopamine = salience alert
     → "Something prediction-relevant changed"
     → Giải thích tại sao dopamine fire cho CẢ positive và negative stimuli
     → = Alarm bell, không phải reward delivery

  ④ IMPLICATIONS: Nếu đúng thì sao?
     → Engagement metrics đo attention capture, không phải satisfaction
     → Addiction research cần reframe (wanting system, không phải pleasure system)
     → AI reward modeling (RLHF) có thể target sai signal

  ⑤ FALSIFICATION: Framework sai nếu...
     → Direct dopamine increase → reliable pleasure increase (chưa ai tìm thấy)
     → Opioid block → dopamine vẫn tạo reward (ngược evidence hiện tại)
     → Nêu rõ: "đây là condition để BÁC BỎ claim này"

  ⑥ CALL TO VERIFY:
     → "Bạn là chuyên gia — evidence này có đứng vững không?"
     → Link tới framework source file
     → Link tới discussion
```

### 2.3 — Expert routing

```
  PRIMARY: ① Neurochemistry — verify dopamine mechanism
  SECONDARY: ③ Computational Neuroscience — verify prediction model
  TERTIARY: ⑮ Psychiatry — verify clinical implications
  (Tham chiếu: expert-verification-map.md)
```

---

## §3 — BLOG B: CORTISOL — OPTIMIZE THE INVERTED-U

### 3.1 — Mục tiêu

```
  CLAIM CHÍNH: Cortisol = change-readiness amplifier, KHÔNG PHẢI "stress hormone."
  Inverted-U = operating spec → tối ưu = tìm optimum, không phải giảm cortisol.
  AUDIENCE: neuroscientists, endocrinologists, psychologists
  KẾT QUẢ MONG MUỐN: verify/falsify (giống Blog A)
  SOURCE: Cortisol-Baseline.md v2.0
```

### 3.2 — Cấu trúc blog

```
  ① HOOK: "Cortisol = stress hormone" misconception
     → Wellness industry: "giảm cortisol = giảm stress"
     → Thực tế: cortisol QUÁ THẤP cũng = vấn đề (Addison's, chronic fatigue)

  ② EVIDENCE: Inverted-U research
     → Yerkes-Dodson (1908) → modern reinterpretations
     → Sapolsky: chronic vs acute cortisol (cùng chất, khác pattern = khác kết quả)
     → HPA axis: cortisol = mobilization signal, không phải damage signal
     → Cortisol cho CÙNG situation = khác nhau giữa người (individual baseline)

  ③ REFRAME: Change-readiness amplifier
     → Cortisol chuẩn bị cơ thể ĐỐI MẶT thay đổi (energy mobilization)
     → Quá thấp = không mobilize → underperform
     → Quá cao = system overload → damage
     → Optimum = GIỮA, và KHÁC NHAU mỗi người

  ④ IMPLICATIONS: Optimize, not eliminate
     → Wellness apps nói "giảm cortisol" = có thể GIẢM QUÁ → worse
     → Stress management cần reframe: tìm OPTIMUM, không phải MINIMUM
     → Per-person calibration cần body-feedback (không có universal target)

  ⑤ FALSIFICATION: Framework sai nếu...
     → Cortisol = 0 → optimal performance (chưa ai tìm thấy — Addison's = ngược lại)
     → Inverted-U không replicate (nhưng đã replicate nhiều lần)
     → Nêu rõ conditions

  ⑥ CALL TO VERIFY: (giống Blog A format)
```

### 3.3 — Expert routing

```
  PRIMARY: ⑤ Endocrinology — verify cortisol mechanism
  SECONDARY: ② Systems Neuroscience — verify HPA axis model
  TERTIARY: ⑥ Clinical Psychology — verify stress reframe
```

---

## §4 — SHORT POSTS (2 bài)

### 4.1 — Đặc điểm chung

```
  ĐỘ DÀI: ~150-300 từ (đọc < 2 phút)
  CẤU TRÚC:
    → 1 câu hook (misconception)
    → 2-3 câu evidence snapshot (1 study cụ thể, không phải tổng quan)
    → 1 câu reframe
    → Link tới blog post: "Full evidence + falsification criteria: [link]"
    → 1 câu mời verify: "Nếu bạn có expertise — tôi muốn biết chỗ nào sai."

  PLATFORM: r/neuroscience, r/cogsci, r/psychology
  TONE: Academic nhưng accessible. Ngắn gọn. Không clickbait.
```

### 4.2 — Tại sao short + blog thay vì chỉ blog

```
  Chuyên gia trên Reddit/forum:
    → Không click link dài từ stranger
    → NHƯNG: nếu short post có 1 insight đủ interesting → tò mò → click
    → Short post = AUDITION. Blog = FULL PERFORMANCE.
    → Nếu audition fail (no engagement) → biết cần sửa framing
    → Nếu audition pass → traffic tới blog → deeper engagement
```

---

## §5 — QUY TRÌNH DRAFT + CHỌN VERSION

### 5.1 — Iterative drafting

```
  BƯỚC 1: Draft nhiều VERSION cho mỗi bài (khác góc, khác tone, khác hook)
    → Mỗi version = 1 file riêng (drafts/blog-A-v1.md, blog-A-v2.md, ...)
    → Thử nghiệm: academic tone, discovery tone, challenge tone

  BƯỚC 2: So sánh versions
    → Tiêu chí: hook strength, evidence clarity, falsifiability rõ ràng
    → Tuân thủ W.4 (anti-self-help) + W.5 (stakes-based)
    → Body-feedback: đọc lại — bài nào TỰ NHIÊN nhất?

  BƯỚC 3: Chọn 1 mẫu HOẶC mix
    → Có thể: 1 mẫu duy nhất cho cả 4 bài (consistency)
    → Có thể: mẫu khác cho blog vs short (khác format = khác tone hợp lý)
    → Quyết định SAU KHI có drafts cụ thể để so

  BƯỚC 4: Refine version chọn
    → Polish language, verify citations, check falsification criteria
    → Cross-check với framework source files
```

### 5.2 — Anti-patterns (TRÁNH)

```
  ✗ Self-help framing: "Hiểu dopamine sẽ thay đổi cuộc đời bạn"
  ✗ Guru tone: "Tôi đã tìm ra sự thật mà ai cũng bỏ lỡ"
  ✗ Clickbait: "SHOCKING: Everything you know about dopamine is WRONG"
  ✗ Overclaim: "Framework giải thích TOÀN BỘ hành vi con người"
  ✗ Marketing: "Star repo / share bài này"
  (Chi tiết: framing-engagement-value.md §3 — 7 anti-patterns)
```

---

## §6 — TIMELINE + MILESTONES

```
  Phase 1: DRAFT
    → Draft Blog A (nhiều versions) — sử dụng 01-Dopamine-Not-Reward.md làm base
    → Draft Blog B (nhiều versions) — từ Cortisol-Baseline.md v2.0
    → Draft Short A + Short B
    → KHÔNG rush. Mỗi session = 1-2 versions.

  Phase 2: SELECT
    → So sánh versions → chọn hoặc mix
    → Xác định: 1 mẫu chung hay mẫu riêng cho blog vs short?

  Phase 3: REFINE
    → Polish final versions
    → Verify citations against primary sources
    → Cross-check falsification criteria

  Phase 4: PUBLISH (Blog A → Short A → Blog B → Short B)
    → Blog lên trước (GitHub Pages / Medium / blog riêng)
    → Short post sau (Reddit / forum)
    → Monitor engagement → learn → adjust

  KHÔNG ĐẶT DEADLINE CỨ THỂ.
  Chất lượng > tốc độ. Mỗi bài phải đứng vững trước chuyên gia.
```
