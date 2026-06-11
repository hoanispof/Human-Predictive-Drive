# Plan: Neuroscience Posts — 3 Blog + 3 Short Posts

> **Mục tiêu:** Tạo 3 bài blog neuroscience + 3 short post dẫn link. Phục vụ VERIFY từ chuyên gia.
> **Vị trí trong chiến lược:** Đây là content ĐẦU TIÊN ra ngoài. Neuro posts đi trước tech post.
> **Nguyên tắc:** hypothesis inviting falsification. Giọng ngang hàng, không giảng dạy.
> **Trạng thái:** PLANNING
> **Ngày tạo:** 2026-05-26
> **Liên kết:**
>   plan-public.md — framing rules (W.4, W.5)
>   plan-overview-distribution.md — overview blog distribution (thay thế plan-tech-distribution.md)
>   framing-engagement-value.md — 3-tầng value model
>   01-Dopamine-Not-Reward.md — draft có sẵn cho Topic 1
>   expert-verification-map.md — routing claims tới đúng expert group

---

## §1 — 6 BÀI, 2 TẦNG

```
  TẦNG 1: BLOG POST (dài, chi tiết, có citation)
    → Blog A: Dopamine Is Not Reward                              ✅ DRAFTED
    → Blog B: Cortisol — Not Your Stress Hormone                   ✅ DRAFTED
    → Blog C: ADHD — Not Attention Deficit (tech-neuro crossover)  ✅ DRAFTED

  TẦNG 2: SHORT POST (ngắn, dẫn link tới blog)
    → Short A: dẫn → Blog A                                       ✅ DRAFTED
    → Short B: dẫn → Blog B                                       ✅ DRAFTED
    → Short C: dẫn → Blog C                                       ✅ DRAFTED
    → Short D: dẫn → Blog C (r/ADHD_Programmers)                   ✅ DRAFTED

  LOGIC:
    Short post = HOOK + 1 insight cụ thể + link
    Blog post = FULL argument + evidence + falsification criteria
    Chuyên gia đọc short → tò mò → click blog → verify → engage

  THỨ TỰ XUẤT BẢN:
    Blog A trước → Short A → Blog B → Short B → Blog C → Short C
    (Blog phải sẵn TRƯỚC short post, vì short dẫn link)

  LƯU Ý:
    Tech overview (plan-overview-blog.md) = NAY CÓ blog riêng + short posts
    → Đã thay đổi: tech cũng có blog, giống pattern neuro
    → plan-tech-post.md đã backup (key content absorbed vào plan-overview-blog.md)
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

## §3b — BLOG C: ADHD — NOT ATTENTION DEFICIT (⬜ PLANNED)

### 3b.1 — Mục tiêu

```
  CLAIM CHÍNH: "Attention Deficit" là tên gọi SAI.
  ADHD = dopamine CLEARANCE quá nhanh + RECEPTOR kém nhạy (DAT + DRD4 + COMT).
  Không thiếu attention — REGULATE khác. Hyperfocus + inattention = CÙNG mechanism, khác threshold.
  AUDIENCE: neuroscientists, psychiatrists, psychologists, tech (ADHD-aware community lớn)
  KẾT QUẢ MONG MUỐN: verify/falsify (giống Blog A/B)
  SOURCE: ADHD-Observation.md v1.3 + ADHD-Trade-Off.md v1.0 + ADHD-Attention-Optimization.md v1.0
```

### 3b.2 — Cấu trúc blog (dự kiến)

```
  ① HOOK: "Attention Deficit" misconception
     → "Không tập trung" + "hyperfocus 6 giờ" = CÙNG mechanism
     → Tên gọi sai DẪN TỚI hiểu sai → can thiệp sai hướng

  ② EVIDENCE: 3-way dopamine comparison
     → Nicotine = VTA forced fire (hijack)
     → Parkinson = SNc degeneration (loss)
     → ADHD = DAT + DRD4 tuning (clearance + receptor sensitivity)
     → Cùng phân tử, 3 disruption points, 3 clinical outcomes

  ③ REFRAME: Regulation variation, not deficit
     → DAT clearance speed → threshold khác cho sustained attention
     → DRD4 sensitivity → novelty-seeking pattern
     → Hyperfocus = GAP strong enough to exceed threshold
     → Inattention = GAP too weak to exceed threshold

  ④ TRADE-OFF: Tại sao ADHD tồn tại (5-7% stable prevalence)
     → Inverted-U: subclinical = creative advantage, severe = executive deficit
     → Environment dịch chuyển peak → environment FIT matters more than hardware

  ⑤ FALSIFICATION: Framework sai nếu...
     → Pure attention training eliminates ADHD (without changing threshold)
     → ADHD prevalence NOT stable across populations
     → Nêu rõ conditions

  ⑥ CALL TO VERIFY: (giống Blog A/B format)
```

### 3b.3 — Expert routing

```
  PRIMARY: ① Neurochemistry — verify dopamine mechanism (DAT/DRD4/COMT)
  SECONDARY: ⑮ Psychiatry — verify clinical reframe
  TERTIARY: ⑨ Cognitive Psychology — verify attention model
  BONUS: Tech community (HN, r/ADHD) — ADHD-aware audience, high engagement potential
```

---

## §4 — SHORT POSTS (3 bài)

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
  Phase 1: DRAFT                                                    ✅ ALL DONE
    → Draft Blog A — sử dụng 01-Dopamine-Not-Reward.md làm base      ✅
    → Draft Blog B — từ Cortisol-Baseline.md v2.0                     ✅
    → Draft Blog C — từ ADHD-Observation.md v1.3 + companion files    ✅ DRAFTED
    → Draft Short A + Short B + Short C + Short D(ADHD_Programmers)    ✅ ALL DONE
    → KHÔNG rush. Mỗi session = 1-2 versions.

  Phase 2: SELECT                                                   ✅ DONE
    → So sánh 3 blogs → 7 inconsistencies identified                  ✅
    → Quyết định: template chung + biến thể hợp lý cho Blog C         ✅
    → Consistency fixes applied (Batch 1 + Batch 2)                    ✅

  Phase 3: REFINE                                                    ✅ ALL DONE
    → Structural consistency (section order, tables, format)           ✅ DONE
    → Cross-linking between blogs                                      ✅ DONE
    → Verify citations against primary sources                         ✅ DONE
      Blog A: 26 refs — all clean, proper format                        ✅
      Blog B: 27→28 refs — all clean + Reyes 2020 ADDED for Ev.1       ✅
      Blog C: 3 floating citations FIXED                                ✅
        Gaze cueing: Marotta et al. (2017) PMID 28199914
        Social cognition: Bora & Pantelis (2016) PMID 26707895
        Exercise meta: Liang et al. (2021) PMC8141166 (year 2025→2021)
    → Cross-check falsification criteria                               ✅ DONE
      16 criteria total (A:6 + B:5 + C:5) — no cross-blog contradictions
      1 tension (DRD4 centrality: A=optional, C=central) — transparent
    → Content quality review (per-section)                             ✅ DONE
      Blog B Ev.1 strengthened with specific study (was "clinical obs")
      Blog B genius paradox already softened (prev session)

  Phase 4: PUBLISH (Blog A → Short A → Blog B → Short B → Blog C → Short C)
    → Blog lên trước (GitHub Pages / Medium / blog riêng)
    → Short post sau (Reddit / forum)
    → Monitor engagement → learn → adjust

  SONG SONG: Tech overview blog (plan-overview-blog.md)
    → NAY CÓ blog riêng + short posts (giống pattern neuro)
    → plan-overview-distribution.md = distribution plan
    → Có thể publish song song hoặc sau Blog C

  KHÔNG ĐẶT DEADLINE CỨ THỂ.
  Chất lượng > tốc độ. Mỗi bài phải đứng vững trước chuyên gia.
```
