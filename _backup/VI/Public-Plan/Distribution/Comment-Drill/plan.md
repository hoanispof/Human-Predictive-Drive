# Comment Drill — Plan Triển Khai

> **Mục tiêu:** Drill kỹ từng bài post TRƯỚC KHI comment.
> Mỗi session = 1 bài. Chậm mà chắc. Chất lượng > tốc độ.
> **Nguyên tắc:** Comment chỉ tốt khi phân tích THẬT SỰ sâu.
> Không shortcut, không ép framework vào bài post.
> Drill rộng → zoom vào 1 chi tiết → đóng góp cụ thể, có giá trị trực tiếp.
> **Trạng thái:** v1.1
> **Ngày:** 2026-06-07 (v1.0), 2026-06-08 (v1.1 — refine: cụ thể > rộng)
> **Liên kết:**
>   ../distribution-comment.md — comment strategy + cấu trúc comment
>   ../../plan-content-engagement.md — content engagement strategy
>   ../plan-distribution.md — distribution map tổng

---

## §1 — CẤU TRÚC FILE: 3 FILES MỖI BÀI POST

```
  Mỗi bài post có 3 files riêng biệt, mỗi file 1 mục đích rõ ràng:

  ┌─────────────────────────────────────────────────────────────────────┐
  │ FILE                   │ MỤC ĐÍCH              │ KHI NÀO DÙNG      │
  ├─────────────────────────────────────────────────────────────────────┤
  │ post-[slug].md         │ Bài viết gốc FULL     │ Reference material │
  │                        │ Nội dung verbatim +   │ Đọc lại khi drill  │
  │                        │ comments nếu có       │ Không edit          │
  ├─────────────────────────────────────────────────────────────────────┤
  │ drill-[slug].md        │ Workspace phân tích   │ Phase 1-2-3        │
  │                        │ drill questions +     │ Fill dần qua       │
  │                        │ zoom-in + mapping     │ từng session        │
  ├─────────────────────────────────────────────────────────────────────┤
  │ comment-[slug].md      │ Xây dựng comment      │ Phase 3-4-5        │
  │                        │ Synthesis + draft +   │ Sau khi drill xong  │
  │                        │ quality check + post  │                    │
  └─────────────────────────────────────────────────────────────────────┘

  Tại sao tách:
    → post file = source of truth, không bị pha lẫn với phân tích
    → drill file = workspace tự do, có thể messy, iterate nhiều lần
    → comment file = output sạch, focus vào chất lượng cuối cùng
```

---

## §2 — QUY TRÌNH 5 PHASE

```
  Mỗi bài post đi qua 5 phase. Mỗi phase có output cụ thể.
  Một session tập trung drill SÂU 1 bài. Chậm mà chắc.

  ┌─────────────────────────────────────────────────────────────────────┐
  │ PHASE │ TÊN                │ OUTPUT              │ FILE            │
  ├─────────────────────────────────────────────────────────────────────┤
  │   1   │ CAPTURE            │ Nội dung bài gốc    │ post-*.md       │
  │       │ (Lưu bài gốc)     │ full + metadata      │                 │
  ├─────────────────────────────────────────────────────────────────────┤
  │   2   │ DRILL              │ Phân tích sâu từng   │ drill-*.md      │
  │       │ (Phân tích sâu     │ claim, gap, mapping  │                 │
  │       │  + Zoom In)        │ + zoom-in candidate  │                 │
  ├─────────────────────────────────────────────────────────────────────┤
  │   3   │ SYNTHESIZE         │ Chắt lọc 1 đóng góp │ drill-*.md →   │
  │       │ (Tổng hợp)        │ CỤ THỂ nhất          │ comment-*.md    │
  ├─────────────────────────────────────────────────────────────────────┤
  │   4   │ BUILD              │ Draft comment cụ thể  │ comment-*.md    │
  │       │ (Xây comment)      │                      │                 │
  ├─────────────────────────────────────────────────────────────────────┤
  │   5   │ REVIEW + POST      │ Quality check, post  │ comment-*.md    │
  │       │ (Kiểm tra + đăng) │ + theo dõi replies    │                 │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## §3 — CHI TIẾT TỪNG PHASE

### Phase 1: CAPTURE

```
  MỤC TIÊU: Lưu lại bài post đầy đủ, structured, dễ reference.

  CHECKLIST:
    □ Metadata: link, author, platform, ngày post, ngày tìm
    □ Tóm tắt nội dung: core claims + arguments (structured bullets)
    □ Đánh giá sơ bộ: topic gì? audience nào? tone thế nào?
    □ Ghi nhận ấn tượng ban đầu (chưa phân tích sâu)

  OUTPUT: File [platform]-[slug].md với §1 Metadata + §2 Content
  STATUS: □ Done
```

### Phase 2: DRILL

```
  MỤC TIÊU: Phân tích sâu bài post qua framework lens.
  ĐÂY LÀ PHASE QUAN TRỌNG NHẤT — dành nhiều thời gian nhất.

  5 CÂU HỎI DRILL + ZOOM IN (trả lời từng cái):

    ① BÀI POST NÓI GÌ?
      → Tách riêng: claims vs evidence vs opinion vs assumption
      → Author đang giải thích WHAT hay WHY?
      → Author có acknowledge limitations không?
      → Đọc kỹ — không strawman, không đơn giản hóa

    ② GAP NÀO TỒN TẠI?
      → Bài post giải thích A nhưng CHƯA giải thích WHY A?
      → Trường hợp nào bài post chưa cover?
      → Assumption nào bài post take for granted?
      → ⚠️ CHỈ GHI NHẬN gap THẬT — không tạo gap giả

    ③ FRAMEWORK MAP VÀO ĐÂU?
      → Mechanism nào giải thích gap?
      → File framework nào relevant nhất?
      → Evidence nào support framework explanation?
      → ⚠️ KHÔNG ÉP — nếu framework không giải thích được → ghi rõ

    ④ DỰ ĐOÁN GÌ?
      → Nếu framework mechanism đúng → ta sẽ thấy gì?
      → Prediction phải TESTABLE + SPECIFIC
      → Khi nào prediction SAI? (falsification condition)
      → ⚠️ KHÔNG dự đoán mơ hồ ("things will improve")

    ⑤ FRAMEWORK CÓ THỂ SAI Ở ĐÂU?
      → Bài post có evidence nào CHỐNG framework không?
      → Author expertise có vượt framework ở điểm nào?
      → Nếu framework sai → sai ở claim nào cụ thể?
      → = Honest assessment. Không defensive.

    ⑥ ZOOM IN — TÌM ĐIỂM ĐÓNG GÓP CỤ THỂ (v1.1):
      → Từ gaps ở ②③: gap nào chứa 1 chi tiết mà framework
        thêm được giá trị TRỰC TIẾP?
      → "Giá trị trực tiếp" = reader đọc xong ĐƯỢC:
        góc nhìn mới, phân biệt quan trọng, cách nghĩ khác,
        giải pháp cụ thể, hoặc câu hỏi đúng mà chưa ai đặt
      → KHÔNG chọn gap chỉ vì framework "giải thích mạnh"
      → Chọn gap vì framework ĐỀ XUẤT được thứ CỤ THỂ + HỮU ÍCH
      → Output: 1 chi tiết cụ thể + 1 đóng góp rõ ràng
      → ⚠️ Nếu không zoom in được → gap quá rộng hoặc framework
        chỉ giải thích chung → chưa đủ để comment (quality gate)

  OUTPUT: §3 Drill Workspace filled + §3.6 Zoom-in candidate
  STATUS: □ Done
```

### Phase 3: SYNTHESIZE

```
  MỤC TIÊU: Từ drill → chắt lọc 1 đóng góp CỤ THỂ NHẤT cho comment.

  TIÊU CHÍ CHỌN (v1.1 — 4 điều kiện đồng thời):

    □ CỤ THỂ: 1 chi tiết, 1 vấn đề, 1 đóng góp
      (không phải broad mechanism covering toàn bài)
    □ GIÁ TRỊ TRỰC TIẾP: reader đọc xong ĐƯỢC gì?
      (insight mới, góc nhìn mới, phân biệt quan trọng, giải pháp)
    □ CHÍNH XÁC: framework evidence đủ mạnh cho claim CỤ THỂ này
      (không phải "framework suggests..." mơ hồ)
    □ GỌN: nói được trong vài câu mà không mất chất
      (nếu phải giải thích dài → chưa đủ cụ thể, zoom in hơn)

  CHECKLIST:
    □ Xác định 1 chi tiết cụ thể + 1 đóng góp rõ ràng (từ ⑥)
    □ Dịch framework terms → mainstream language
      (ref: plan-content-engagement.md §6.2 bảng dịch)
    □ Xác định điểm nối trong bài post (nối vào CHI TIẾT nào?)
    □ Xác định implication / prediction CỤ THỂ
    □ Xác định câu mời thảo luận CỤ THỂ (về chi tiết đang bàn)

  QUALITY GATE:
    → Nếu không tìm được đóng góp CỤ THỂ + GIÁ TRỊ TRỰC TIẾP
      → KHÔNG COMMENT
    → "Framework giải thích mechanism chung" ≠ đủ để comment
    → "Không comment" = kết quả hợp lệ
    → Framework không đóng góp cụ thể được mọi bài
      — đó là tín hiệu tốt

  OUTPUT: Synthesis Summary (comment-*.md §1)
  STATUS: □ Done
```

### Phase 4: BUILD

```
  MỤC TIÊU: Viết comment theo cấu trúc distribution-comment.md §4.

  CẤU TRÚC COMMENT (v1.1):
    ① NỐI VÀO CHI TIẾT CỤ THỂ (1 câu)
    ② INSIGHT / ĐỀ XUẤT TRỰC TIẾP (2-4 câu) — phần CHÍNH
    ③ TẠI SAO ĐIỀU NÀY MATTERS (1-2 câu)
    ④ MỜI THẢO LUẬN (1 câu)

  QUALITY CHECKLIST (v1.1):
    □ 1 chi tiết cụ thể, không cover toàn bài?
    □ Reader ĐƯỢC GÌ trực tiếp? (insight, góc nhìn, phân biệt)
    □ Rõ ràng, đầy đủ, chính xác? (không mơ hồ, không half-baked)
    □ Gọn? (không lan man gây loãng — mỗi câu earn chỗ đứng)
    □ Cho giá trị, không quảng cáo?
    □ Ngôn ngữ mainstream, không jargon?
    □ Bổ sung, không sửa?
    □ Không mention "framework" hay "my research"?
    □ Tone phù hợp platform?
    □ Độ dài phù hợp? (~100-200 words)

  OUTPUT: Draft Comment (comment-*.md §2)
  STATUS: □ Done
```

### Phase 5: REVIEW + POST

```
  MỤC TIÊU: Final check → post → theo dõi.

  REVIEW:
    □ Đọc lại comment sau 1 khoảng nghỉ (fresh eyes)
    □ Check: có đang ép framework không?
    □ Check: reader KHÔNG biết framework có thấy hay không?
    □ Check: author bài post đọc sẽ feel respected không?
    □ Refine nếu cần

  POST:
    □ Post comment trên platform
    □ Ghi lại: ngày post, link comment (nếu có)

  THEO DÕI:
    □ Check replies sau 24-48h
    □ Nếu có reply thú vị → cùng thảo luận
    □ Ghi lại kết quả: engagement level, feedback nhận được

  OUTPUT: §5 Post Status updated
  STATUS: □ Done
```

---

## §4 — FRAMEWORK FILES REFERENCE

```
  Quick reference: files thường dùng nhất khi drill.

  KIẾN TRÚC TỔNG:
    Core-Software.md              — cycle-based architecture, PFC observer
    Body-Base.md                  — PFC vs body-base (knowing vs doing)
    Neural-Architecture.md        — hardware/software 2-map

  COMPILATION MECHANISM:
    Chunk/Chunk.md                — chunk substrate, activation, compilation
    Chunk/Compile-Taxonomy.md     — 1 Engine + 3 Modulators
    Chunk/Compile-Sleep.md        — offline consolidation (6 mechanisms)
    Chunk/Background-Pattern.md   — compiled bias invisible to PFC

  BODY-FEEDBACK:
    Body-Feedback/Body-Feedback.md — dual-pull architecture
    Body-Feedback/Hidden-Quality-Perception.md — expertise blind spots
    Why-Body-Knows.md             — body calibration, knowing vs doing

  PREDICTION + SIGNALS:
    PFC/Simulation-Engine.md      — 1 engine, 3 components, 3 axes
    PFC/PFC-Operations.md         — hold/suppress, compiled vs fresh
    Cortisol-Baseline.md          — amplifier + direction gate

  AGENT + AI:
    Agent-Mechanism/Self-Pattern-Modeling.md — modeling other agents
    Agent-Mechanism/Entity-Compiled.md — agent compilation into body-base
    Agent-Mechanism/Entity-Access.md — mPFC gradient, access confidence
    Research/Global/AI-Self-Model.md — AI as amplifier
    Research/Global/Human-AI-Future.md — AI alignment via human mechanism

  NGÔN NGỮ DỊCH:
    plan-content-engagement.md §6.2 — bảng dịch framework → mainstream

  Tất cả paths tương đối từ Core-Deep-Dive/ (trừ Research/ và Core-Software.md).
```

---

## §5 — DANH SÁCH BÀI POST

```
  ══════════════════════════════════════════════════════════════
  LESSWRONG (3 bài — 2× Phase 4 BUILD DONE, 1× Phase 4 BUILD DONE)
  ══════════════════════════════════════════════════════════════

  ┌────┬──────────────────────────────────┬───────────┬────────────┐
  │  # │ BÀI POST                         │ PLATFORM  │ STATUS     │
  ├────┼──────────────────────────────────┼───────────┼────────────┤
  │  1 │ Why Software Automation Is Hard  │ LessWrong │ Phase 4:   │
  │    │ (silentbob)                      │           │ BUILD DONE │
  │    │                                  │           │            │
  │    │ FILES:                           │           │            │
  │    │   post-lw-software-automation.md │           │            │
  │    │   drill-lw-software-automation.md│           │            │
  │    │   comment-lw-software-automation │           │            │
  │    │     .md                          │           │            │
  ├────┼──────────────────────────────────┼───────────┼────────────┤
  │  2 │ Computational Cognitive Neuro-   │ LessWrong │ Phase 4:   │
  │    │ science Perspective on Alignment │           │ BUILD DONE │
  │    │ (Seth Herd)                      │           │            │
  │    │                                  │           │            │
  │    │ FILES:                           │           │            │
  │    │   post-lw-comp-cog-neuro-        │           │            │
  │    │     alignment.md                 │           │            │
  │    │   drill-lw-comp-cog-neuro-       │           │            │
  │    │     alignment.md                 │           │            │
  │    │   comment-lw-comp-cog-neuro-     │           │            │
  │    │     alignment.md                 │           │            │
  ├────┼──────────────────────────────────┼───────────┼────────────┤
  │  8 │ How Valuable Are Weak AI Safety  │ LessWrong │ Phase 4:   │
  │    │ Regulations?                     │           │ BUILD DONE │
  │    │ (MichaelDickens)                 │           │            │
  │    │                                  │           │            │
  │    │ FILES:                           │           │            │
  │    │   post-lw-weak-ai-safety-        │           │            │
  │    │     regulations.md               │           │            │
  │    │   drill-lw-weak-ai-safety-       │           │            │
  │    │     regulations.md               │           │            │
  │    │   comment-lw-weak-ai-safety-     │           │            │
  │    │     regulations.md               │           │            │
  │    │                                  │           │            │
  │    │ ANGLE: "Ban until proven safe"   │           │            │
  │    │   circularity — safety knowledge │           │            │
  │    │   requires building the thing.   │           │            │
  │    │   Weak regs = iterative safety   │           │            │
  │    │   infrastructure, not Overton    │           │            │
  │    │   window shift.                  │           │            │
  └────┴──────────────────────────────────┴───────────┴────────────┘

  ══════════════════════════════════════════════════════════════
  REDDIT (5 bài — mixed status)
  ══════════════════════════════════════════════════════════════

  ┌────┬──────────────────────────────────┬─────────────────┬────────────┐
  │  # │ BÀI POST                         │ PLATFORM         │ STATUS     │
  ├────┼──────────────────────────────────┼─────────────────┼────────────┤
  │  3 │ Antidepressants and Talk Therapy │ r/psychology     │ Phase 4:   │
  │    │ Show Similar Results             │ 444 upvotes      │ BUILD DONE │
  │    │ (u/mvea)                         │                  │            │
  │    │                                  │                  │            │
  │    │ FILES:                           │                  │            │
  │    │   post-reddit-antidepressants-   │                  │            │
  │    │     therapy.md                   │                  │            │
  │    │   drill-reddit-antidepressants-  │                  │            │
  │    │     therapy.md                   │                  │            │
  │    │   comment-reddit-antidepressants-│                  │            │
  │    │     therapy.md                   │                  │            │
  │    │                                  │                  │            │
  │    │ ANGLE: Asymmetric structural     │                  │            │
  │    │   shift — PFC weakens while      │                  │            │
  │    │   amygdala strengthens. WHY      │                  │            │
  │    │   therapy blocked for severe.    │                  │            │
  │    │   Reply to u/isaac-screwton.     │                  │            │
  ├────┼──────────────────────────────────┼─────────────────┼────────────┤
  │  4 │ How Do You Deal With Apathy?     │ r/ADHD_          │ Phase 4:   │
  │    │ (u/mrNineMan)                    │ Programmers      │ BUILD DONE │
  │    │                                  │ 19 upvotes       │            │
  │    │ FILES:                           │                  │            │
  │    │   post-reddit-adhd-apathy.md     │                  │            │
  │    │   drill-reddit-adhd-apathy.md    │                  │            │
  │    │   comment-reddit-adhd-apathy.md  │                  │            │
  │    │                                  │                  │            │
  │    │ ANGLE: Force-start conditional   │                  │            │
  │    │   (task properties). 2-type      │                  │            │
  │    │   distinction: "can't start" vs  │                  │            │
  │    │   "don't want anything."         │                  │            │
  │    │ ⚠️ Tone: peer-to-peer only      │                  │            │
  ├────┼──────────────────────────────────┼─────────────────┼────────────┤
  │  5 │ Young Children With Autism Tend  │ r/psychology     │ Phase 4:   │
  │    │ to Look Less at Faces            │ 136 upvotes      │ BUILD DONE │
  │    │ (u/mvea)                         │                  │            │
  │    │                                  │                  │            │
  │    │ FILES:                           │                  │            │
  │    │   post-reddit-autism-gaze.md     │                  │            │
  │    │   drill-reddit-autism-gaze.md    │                  │            │
  │    │   comment-reddit-autism-gaze.md  │                  │            │
  │    │                                  │                  │            │
  │    │ ANGLE: gaze vs comprehension     │                  │            │
  │    │   trade-off. Hadjikhani 2017:    │                  │            │
  │    │   eye avoidance = active self-   │                  │            │
  │    │   protection. Study missing      │                  │            │
  │    │   comprehension measure.         │                  │            │
  │    │ REPLY TO: u/WhitespringTownship  │                  │            │
  │    │ ⚠️ Community hostile to study.   │                  │            │
  │    │   Comment validates ND view.     │                  │            │
  ├────┼──────────────────────────────────┼─────────────────┼────────────┤
  │  6 │ Brain Appropriation: The Coming  │ r/cogsci         │ Phase 4:   │
  │    │ Labor Crisis                     │ 50 upvotes       │ BUILD DONE │
  │    │ (u/Illustrious-Way-3891)         │                  │            │
  │    │                                  │                  │            │
  │    │ FILES:                           │                  │            │
  │    │   post-reddit-brain-             │                  │            │
  │    │     appropriation.md             │                  │            │
  │    │   drill-reddit-brain-            │                  │            │
  │    │     appropriation.md             │                  │            │
  │    │   comment-reddit-brain-          │                  │            │
  │    │     appropriation.md             │                  │            │
  │    │                                  │                  │            │
  │    │ ANGLE: generation vs evaluation  │                  │            │
  │    │   — math proof sharpens          │                  │            │
  │    │   embodiment argument.           │                  │            │
  │    │   Embodiment = evaluation        │                  │            │
  │    │   architecture, not data.        │                  │            │
  │    │ ⚠️ Thin discussion + overlap     │                  │            │
  │    │   with LW drafts.               │                  │            │
  ├────┼──────────────────────────────────┼─────────────────┼────────────┤
  │  7 │ Andy Clark: Extended Mind +     │ r/cogsci         │ Phase 4:   │
  │    │ Generative AI (Clark 2025,      │ 139 upvotes      │ BUILD      │
  │    │ Nature Communications)          │                  │ DONE       │
  │    │ (u/Altruistic-Dirt-2791)        │                  │            │
  │    │                                  │                  │            │
  │    │ FILES:                           │                  │            │
  │    │   Reddit/post-reddit-extended-  │                  │            │
  │    │     mind-ai.md                  │                  │            │
  │    │   Reddit/s41467-025-59906-9.pdf │                  │            │
  │    │                                  │                  │            │
  │    │ FILES:                           │                  │            │
  │    │   Reddit/drill-reddit-extended- │                  │            │
  │    │     mind-ai.md                  │                  │            │
  │    │   Reddit/comment-reddit-        │                  │            │
  │    │     extended-mind-ai.md         │                  │            │
  │    │                                  │                  │            │
  │    │ ANGLE: Invisible degradation    │                  │            │
  │    │   — expert error-detection      │                  │            │
  │    │   signal depends on SAME        │                  │            │
  │    │   substrate as expertise.       │                  │            │
  │    │   Offload → weaken → signal     │                  │            │
  │    │   fades → can't feel decline.   │                  │            │
  │    │   "Dunning-Kruger on the way    │                  │            │
  │    │   down."                        │                  │            │
  │    │ REPLY TO: u/Koringvias          │                  │            │
  └────┴──────────────────────────────────┴─────────────────┴────────────┘

  THỨ TỰ DRILL:
    #3 trước (gap rõ nhất, risk thấp, engagement cao nhất)
    → #4 (ADHD mechanism strong, tone cần cẩn thận)
    → #5 (framework mạnh nhưng community dynamics khó)
    → #6 (backup — thin discussion, overlap)
    → #7 (strong candidate, needs drill to confirm)
```

---

## §6 — NGUYÊN TẮC XUYÊN SUỐT

```
  ① CHẬM MÀ CHẮC:
    → 1 session = 1 bài, 1-2 phases
    → Không rush để "xong cho nhanh"
    → Nếu drill chưa đủ sâu → thêm 1 session nữa

  ② HONEST ASSESSMENT:
    → Nếu framework không fit → ghi rõ, không ép
    → Nếu author đúng hơn framework → acknowledge
    → "Không comment" = kết quả hợp lệ

  ③ READER-FIRST:
    → Comment phải hay cho READER, không phải cho framework
    → Reader không biết framework tồn tại → vẫn thấy comment có giá trị
    → Nếu bỏ hết framework reference mà comment vẫn hay → đúng hướng

  ④ RESPECT AUTHOR:
    → Đọc kỹ, không strawman
    → Bổ sung, không sửa
    → Author là người đã bỏ công viết → respect that

  ⑤ TRACK EVERYTHING:
    → Mỗi phase có output + status
    → Session sau đọc file → biết ngay đang ở đâu
    → Feedback sau khi post → ghi lại → learn for next time
```

---

> **v1.1 (2026-06-08):** Refine: cụ thể > rộng. Phase 2 +⑥ ZOOM IN, Phase 3 tiêu chí mới, Phase 4 cấu trúc mới.
> v1.0 (2026-06-07): Plan cơ bản.
