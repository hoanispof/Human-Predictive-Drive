# Plan: Distribution — Bản Đồ Phân Phối Tổng Hợp

> **Mục tiêu:** 1 file = biết ngay: blog nào → platform nào → thứ tự nào → file nào.
> **Nguyên tắc:** Chậm mà chắc. Max 1 post/tuần. Đợi feedback trước khi post tiếp.
> **Trạng thái:** v2.0
> **Ngày:** 2026-06-06

---

## §1 — 5 BLOGS

```
  ┌────┬──────────────────────────────────┬───────────┬───────────────────────────────────────────────────────────┐
  │  #  │ TITLE                           │ TRẠNG THÁI│ FILES                                                    │
  ├────┼──────────────────────────────────┼───────────┼───────────────────────────────────────────────────────────┤
  │  A │ Dopamine Signals Salience,       │ Drafted   │ Blog:  docs/_posts/2026-05-31-dopamine-signals-           │
  │    │ Not Reward                       │           │        salience-not-reward.md                             │
  │    │                                  │           │ Short: blog/short-posts-dopamine.md                      │
  │    │                                  │           │ Plan:  Expert/plan-neuro-posts.md §2                     │
  ├────┼──────────────────────────────────┼───────────┼───────────────────────────────────────────────────────────┤
  │  B │ Cortisol Is Not Your             │ Drafted   │ Blog:  docs/_posts/2026-05-31-cortisol-is-not-stress.md   │
  │    │ Stress Hormone                   │           │ Short: blog/short-posts-cortisol.md                      │
  │    │                                  │           │ Plan:  Expert/plan-neuro-posts.md §3                     │
  ├────┼──────────────────────────────────┼───────────┼───────────────────────────────────────────────────────────┤
  │  C │ ADHD Is Not Attention Deficit    │ Drafted   │ Blog:  docs/_posts/2026-05-31-adhd-is-not-attention-      │
  │    │                                  │           │        deficit.md                                        │
  │    │                                  │           │ Short: blog/short-posts-adhd.md                          │
  │    │                                  │           │ Plan:  Expert/plan-neuro-posts.md §4                     │
  ├────┼──────────────────────────────────┼───────────┼───────────────────────────────────────────────────────────┤
  │  D │ Bridging Neuroscience &          │ Drafted   │ Blog:  docs/_posts/2026-06-04-bridging-neuroscience-      │
  │    │ Psychology (Overview)            │           │        psychology.md                                      │
  │    │                                  │           │ Short: blog/short-post-overview.md                       │
  │    │                                  │           │        blog/short-post-overview-main.md                   │
  │    │                                  │           │ Plan:  Tech/plan-overview-blog.md                        │
  │    │                                  │           │        blog/plan-overview-distribution.md                 │
  ├────┼──────────────────────────────────┼───────────┼───────────────────────────────────────────────────────────┤
  │  E │ Logic Is Not the Opposite        │ Drafted   │ Blog:  docs/_posts/2026-06-04-logic-is-not-the-opposite-  │
  │    │ of Intuition                     │ v0.2      │        of-intuition.md                                   │
  │    │                                  │           │ Short: blog/short-posts-logic-feeling.md                  │
  │    │                                  │           │ Plan:  blog/plan-logic-feeling-blog.md                   │
  │    │                                  │           │        blog/plan-logic-feeling-distribution.md            │
  └────┴──────────────────────────────────┴───────────┴───────────────────────────────────────────────────────────┘

  Paths tương đối từ Public-Plan/.
  Blog URLs: hoanispof.github.io/Human-Predictive-Drive/blog/{slug}/
```

---

## §2 — 9 PLATFORMS + 3 INFRASTRUCTURE

### 2.1 — Platforms × Bài Post

```
  ┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
  │  #  │ PLATFORM          │ SIZE       │ POST GÌ                              │ GHI CHÚ          │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │     │                   │            │                                      │                  │
  │     │  ── TIER S: STRESS-TEST ĐẦU TIÊN ──                                                    │
  │     │                   │            │                                      │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  1  │ r/neuroscience    │ ~500K      │ A. Dopamine ≠ Reward                 │ Domain expert    │
  │     │                   │            │ B. Cortisol ≠ Stress                 │ verify. Challenge│
  │     │                   │            │ C. ADHD ≠ Attention Deficit          │ MẠNH NHẤT cho    │
  │     │                   │            │                                      │ biological claims│
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  2  │ r/cogsci          │ ~129K      │ A. Dopamine ≠ Reward                 │ Bridge platform. │
  │     │                   │            │ B. Cortisol ≠ Stress                 │ Mọi blog đều fit.│
  │     │                   │            │ C. ADHD ≠ Attention Deficit          │ Audience quen    │
  │     │                   │            │ D. Overview (Bridging)               │ unified models.  │
  │     │                   │            │ E. Logic ≠ Opposite of Intuition     │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  3  │ LessWrong         │ ~50K       │ D. Overview (Bridging)               │ Rationalist      │
  │     │                   │ active     │ E. Logic ≠ Opposite of Intuition     │ stress-test.     │
  │     │                   │            │                                      │ Đọc sâu nhất,   │
  │     │                   │            │                                      │ challenge kỹ nhất│
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  4  │ r/slatestarcodex  │ ~129K      │ D. Overview (Bridging)               │ Intellectual     │
  │     │                   │            │ E. Logic ≠ Opposite of Intuition     │ long-form.       │
  │     │                   │            │                                      │ Cross-domain.    │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  5  │ r/ADHD_Programmers│ ~100K      │ C. ADHD ≠ Attention Deficit          │ ADHD × tech      │
  │     │                   │            │                                      │ giao điểm.       │
  │     │                   │            │                                      │ Personal stakes. │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  6  │ Bluesky           │ 43M+ reg   │ A. Dopamine ≠ Reward                 │ 20K+ neuro-      │
  │     │                   │ 1.5-3M DAU │ B. Cortisol ≠ Stress                 │ scientists đã    │
  │     │                   │            │ C. ADHD ≠ Attention Deficit          │ migrate từ X.    │
  │     │                   │            │ E. Logic ≠ Opposite of Intuition     │ Micro-threads.   │
  │     │                   │            │                                      │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │     │                   │            │                                      │                  │
  │     │  ── TIER A: SAU KHI TIER S ĐÃ STRESS-TEST ──                                           │
  │     │                   │            │                                      │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  7  │ Hacker News       │ ~500K      │ D. Overview (Bridging)               │ Submit blog LINK.│
  │     │                   │ daily      │                                      │ Tech audience    │
  │     │                   │            │                                      │ LỚN NHẤT.       │
  │     │                   │            │                                      │ Post WEEKDAY.    │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │     │                   │            │                                      │                  │
  │     │  ── TIER B: MỞ RỘNG (bài đã refined từ Tier S feedback) ──                              │
  │     │                   │            │                                      │                  │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  8  │ r/psychology      │ ~1.5M      │ D. Overview (Bridging)               │ Broader reach.   │
  │     │                   │            │                                      │ Accessible       │
  │     │                   │            │                                      │ language.        │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │  9  │ r/philosophy      │ ~18M       │ D. Overview (Bridging)               │ Frame: "philo-   │
  │     │                   │            │                                      │ sophical impli-  │
  │     │                   │            │                                      │ cations." ⚠️ Có │
  │     │                   │            │                                      │ thể bị xóa.     │
  ├─────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ 10  │ r/ADHD            │ ~2M        │ C. ADHD ≠ Attention Deficit          │ General ADHD.    │
  │     │                   │            │                                      │ SAU r/ADHD_Prog  │
  │     │                   │            │                                      │ có traction.     │
  │     │                   │            │                                      │ Disclaimer BẮT   │
  │     │                   │            │                                      │ BUỘC.            │
  └─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 — Infrastructure (làm 1 lần, song song)

```
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ PLATFORM        │ MỤC ĐÍCH                          │ KHI NÀO          │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ ORCID           │ Researcher ID — 5 phút, free      │ Phase 0          │
  │                 │ orcid.org/register                 │                  │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ Zenodo (CERN)   │ GitHub → archive → DOI (citable)  │ Phase 0          │
  │                 │ zenodo.org                         │ (sau GitHub tag) │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ ResearchGate    │ Academic profile + discoverability │ Phase 0 hoặc     │
  │                 │ Upload framework as project        │ song song Phase 1│
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## §3 — THỨ TỰ TRIỂN KHAI

### Phase 0 — Chuẩn Bị

```
  □ Tạo ORCID iD (orcid.org, "Independent Researcher")
  □ GitHub Release tag + Release notes
  □ Zenodo kết nối GitHub → nhận DOI
  □ ResearchGate profile + upload project
  □ Tạo Bluesky account + follow neuroscience starter packs
  □ Verify tất cả blog URLs live + footer cross-links hoạt động
  □ Review short posts: tone, W.4 compliance, links đúng
```

### Phase 1 — Neuro Blogs (A, B, C): Domain Expert Verify

```
  MỤC ĐÍCH: Verify biological claims TRƯỚC khi broaden audience.
  LOGIC: Nếu bị falsify ở đây → sửa TRƯỚC khi ra LW/HN/SSC.

  Blog A (Dopamine) → r/neuroscience → r/cogsci → Bluesky
  Blog B (Cortisol) → r/neuroscience → r/cogsci → Bluesky
  Blog C (ADHD)     → r/neuroscience → r/cogsci → r/ADHD_Programmers → Bluesky
                    → r/ADHD (SAU r/ADHD_Programmers có traction, disclaimer bắt buộc)

  Mỗi post cách nhau 1 tuần. Đợi feedback 3-5 ngày trước khi post tiếp.

  ⏸ CHECKPOINT (~10 tuần):
    □ Có feedback từ domain experts? Falsification nào cần xử lý?
    □ Nếu bị falsify nghiêm trọng → DỪNG, sửa framework
    □ Nếu OK → tiếp Phase 2
```

### Phase 2 — Overview Blog (D): Broaden Audience

```
  MỤC ĐÍCH: Expose framework tới tech + rationalist + broader audience.
  PREREQUISITES: Phase 1 không bị falsify nghiêm trọng.

  Blog D (Overview) → LessWrong → r/slatestarcodex → Hacker News
                    → r/cogsci → r/psychology → r/philosophy

  LessWrong = stress-test ĐẦU TIÊN cho overview (audience đọc sâu nhất).
  HN = submit blog LINK, post WEEKDAY, respond nhanh 2h đầu.
  r/psychology = accessible language, mechanism tease limerence.
  r/philosophy = frame "philosophical implications of empirical findings."
    ⚠️ Strict moderation — có thể bị xóa. Worst case mất 10 phút.

  ⏸ CHECKPOINT (~17 tuần):
    □ LW/SSC/HN có traction? Credibility established?
    □ r/psychology: mechanism discussion hay self-help pickup?
    □ r/philosophy: post còn hay bị xóa?
    □ Nếu OK → tiếp Phase 3
```

### Phase 3 — Logic-Feeling Blog (E): Deep-Dive

```
  MỤC ĐÍCH: Deep-dive position MẠNH NHẤT + PROVOCATIVE nhất.
  PREREQUISITES: Overview blog đã publish → reader có context compiled vs fresh.
  ⚠️ Blog này CHALLENGE IDENTITY audience (rationalist tự nhận "logical").
     Chi tiết framing: plan-logic-feeling-distribution.md §2 + §5.

  Blog E (Logic-Feeling) → LessWrong → r/slatestarcodex → r/cogsci → Bluesky

  ⏸ CHECKPOINT (~21 tuần):
    □ Framework đã có community engage?
    □ Falsification nào cần update?
```

### Phase 4 — Engage + Exit (ongoing)

```
  RESPONDING PROTOCOL (mọi platform):
    Khi challenge:       "Good point. Here's the evidence: [citation]"
    Khi gap:             "We don't know. That's a genuine gap."
    Khi counter-evidence: acknowledge nếu mạnh → cập nhật framework
    Khi khen:            redirect → "we need MORE challenge, not less"
    Khi hỏi credentials: "Independent researcher. Test claims, not credentials."
    Khi personal story:  "The model predicts [X]. Does that match?"
    Tone luôn:           "we" inclusive — ngang hàng, không guru, không xin xỏ

  Chi tiết per audience type:
    General:           plan-public.md §4.1
    Identity-challenge: blog/plan-logic-feeling-distribution.md §5

  EXIT CONDITION:
    → ≥3 independent researchers đã engage
    → Discussion xảy ra MÀ KHÔNG CẦN tác giả khởi xướng
    → Community members tự tạo content cho audience CỦA HỌ
```

---

## §4 — RULES

```
  CADENCE:
    → Max 1 post / tuần. KHÔNG post nhiều platform cùng ngày.
    → Đợi feedback 3-7 ngày trước khi post tiếp.
    → Post bị ignore → refine framing, KHÔNG spam lại.

  FRAMING (W.4 — mọi post):
    → Evidence + mechanism TRƯỚC → stakes SAU
    → "Here's the mechanism. Here's the evidence. Test it yourself."
    → "We all need to know whether this holds up." (inclusive, ngang hàng)
    → Mỗi post kết thúc: falsification criteria + "what would break this?"

  KHÔNG BAO GIỜ:
    → Self-help framing ("this will help you...")
    → Grand claims ("comprehensive theory of...")
    → Marketing ("star the repo", "share this")
    → Guru tone ("mọi người đã sai suốt...")

  Chi tiết đầy đủ: plan-public.md §W.4 + framing-engagement-value.md
```

---

## §5 — PLAN GỐC (tham chiếu khi cần chi tiết sâu)

```
  STRATEGY + FRAMING:
    plan-public.md                            → Framing rules W.4, W.5, overall strategy
    framing-engagement-value.md               → 3-layer value model
    plan-content-engagement.md                → Comment strategy trên expert content
    Expert/expert-verification-map.md         → 20 expert groups routing table

  BLOG CONTENT:
    Expert/plan-neuro-posts.md                → 3 neuro blog structure + expert routing
    Tech/plan-overview-blog.md                → Blog D content structure
    blog/plan-logic-feeling-blog.md           → Blog E content structure

  PER-BLOG DISTRIBUTION (chi tiết per-platform):
    blog/plan-overview-distribution.md        → Blog D: 17 platforms chi tiết
    blog/plan-logic-feeling-distribution.md   → Blog E: 16 platforms chi tiết

  INFRASTRUCTURE:
    Tech/github-infrastructure.md             → GitHub hub-and-spoke setup
    Tech/future-topic-ideas.md                → Topics T3-T5 (sau core publish)
    Expert/summary-paper-outline.md           → Academic summary paper (dài hạn)
```

---

> **v2.0 (2026-06-06):** Rewrite gọn từ v1.1 (887 dòng → ~250 dòng).
> Bỏ: ma trận trùng lặp, skip list, chi tiết per-post, ADHD topics A1-A4 (Blog C đã cover).
> Giữ: blog list + file map, platform table, phase flow + checkpoints, respond protocol.
