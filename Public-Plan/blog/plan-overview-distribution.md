# Plan: Overview Blog Distribution — Phân Phối Blog Tổng Quan Framework

> **Mục tiêu:** Đưa blog overview tới nhiều cộng đồng chất lượng nhất có thể.
> Blog này khác 3 neuro blogs: TỔNG QUAN framework, không deep-dive 1 mechanism.
> **Nguyên tắc:** Stress-test deployment, không phải marketing. Framework sống hay chết bằng evidence.
> **Trạng thái:** DRAFT v0.2 (updated 2026-06-04 — §2 rewritten, approach unified)
> **Ngày tạo:** 2026-06-04
> **Blog file:** docs/_posts/2026-06-04-bridging-neuroscience-psychology.md
> **Blog URL:** https://hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/
> **Short posts:** Public-Plan/blog/short-post-overview.md (4 posts — CẦN REWRITE theo §2.2)
> **Liên kết:**
>   plan-overview-blog.md — blog content structure + quality guidelines
>   Tech/backup/plan-tech-distribution.md — BACKED UP (unique parts extracted → §1.3, github-infrastructure.md, future-topic-ideas.md)
>   plan-neuro-posts.md — neuro blog distribution pattern (2-tier: blog + short)
>   plan-adhd-tech-distribution.md — ADHD × tech specialized distribution
>   framing-engagement-value.md — 3-layer value model, W.4 rules
>   short-post-overview.md — 4 short posts (CẦN REWRITE theo structure mới)

---

## §0 — TẠI SAO PLAN RIÊNG CHO OVERVIEW BLOG

### 0.1 — Blog Này Khác 3 Neuro Blogs

```
  3 NEURO BLOGS:
    Blog A: Dopamine ≠ reward       → 1 claim cụ thể, deep-dive
    Blog B: Cortisol ≠ stress       → 1 claim cụ thể, deep-dive
    Blog C: ADHD ≠ attention deficit → 1 claim cụ thể, deep-dive
    → Audience: domain experts (neuroscientists, psychologists)
    → Short posts: question-hook → blog → verify claim
    → Platforms: r/neuroscience, r/cogsci, r/psychology (+ r/ADHD_Programmers cho Blog C)

  OVERVIEW BLOG:
    Blog D: Framework tổng quan     → nhiều mechanism, overview
    → Audience: tech experts, rationalists, cross-domain thinkers
    → Short posts: framework-first → blog → explore full framework
    → Platforms: RỘNG HƠN — tech + rationalist + academic + social

  KEY DIFFERENCES:
    ① Audience RỘNG hơn (không chỉ domain experts)
    ② Content BROAD hơn (11 questions, 6 sketches, not 1 deep-dive)
    ③ Goal khác: EXPOSE framework, not verify 1 specific claim
    ④ Platforms nhiều hơn và đa dạng hơn
    ⑤ Short posts = framework-first (not question-hook)
    → Cần plan distribution RIÊNG
```

### 0.2 — Vị Trí Trong Chiến Lược Tổng Thể

```
  THỨ TỰ PUBLISH:
    Blog A (Dopamine) → Blog B (Cortisol) → Blog C (ADHD)
    → Blog D (Overview) → Blog E (Logic-Feeling)
    → 3 neuro blogs TRƯỚC = establish credibility qua domain expert verify
    → Overview blog SAU = broaden audience với credibility đã có
    → Logic-Feeling blog SAU CÙNG = deep-dive identity-challenging, cần context
    → Cross-links trong footer = cross-validation signal

  HOẶC:
    Blog D (Overview) CÓ THỂ publish SONG SONG với Blog A
    → Nếu overview publish trước → chưa có neuro blog links trong footer
    → Nhưng: overview KHÔNG phụ thuộc neuro blogs — self-contained
    → Quyết định: flexible — publish khi blog đủ chất lượng

  BLOG D FOOTER hiện tại link tới 3 neuro blogs + 1 logic-feeling blog:
    → Dopamine: https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/
    → Cortisol: https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/
    → ADHD: https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/
    → Logic-Feeling: https://hoanispof.github.io/Human-Predictive-Drive/blog/logic-is-not-the-opposite-of-intuition/
    → Links này PHẢI live trước khi overview blog publish (hoặc remove nếu publish trước)
```

---

## §1 — PLATFORM MAP: Tất Cả Platforms Cho Overview Blog

### 1.1 — Platform Priority Matrix

```
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║ TIER S — POST ĐẦU TIÊN (stress-test, chất lượng cao nhất)              ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                           ║
  ║ ① LessWrong                                                              ║
  ║   Size: ~50K active                                                       ║
  ║   Audience: rationalist, Bayesian, cognitive science, AI safety           ║
  ║   Fit: PERFECT — cross-domain framework, falsification, epistemic status ║
  ║   Format: long-form essay ok (3000-8000 words)                           ║
  ║   Short post: ĐÃ CÓ (short-post-overview.md Post A, ~300 words)            ║
  ║   Demo: System 1/2 reframe (compiled vs fresh processing)                ║
  ║   Risk: thấp (nhỏ, stress-test kỹ nhất)                                ║
  ║   Tại sao ĐẦU TIÊN: audience đọc sâu nhất, challenge kỹ nhất           ║
  ║                                                                           ║
  ║ ② r/slatestarcodex (~129K)                                               ║
  ║   Audience: intellectual long-form, cross-domain, psychiatry-aware        ║
  ║   Fit: overview framework, body-first architecture, divergence from      ║
  ║        mainstream — chính xác topic SSC audience quan tâm                 ║
  ║   Format: long-form (2000-5000 words)                                    ║
  ║   Short post: CẦN TẠO MỚI (adapt từ LW post, intellectual tone)         ║
  ║   Risk: thấp-trung                                                       ║
  ║                                                                           ║
  ║ ③ EA Forum (Effective Altruism)                                    [MỚI] ║
  ║   URL: https://forum.effectivealtruism.org/                               ║
  ║   Audience: rationalist, researchers, AI safety — overlap LW nhưng RIÊNG║
  ║   Fit: cross-domain framework + human cognition → relevant cho AI safety ║
  ║        + decision-making + human flourishing                              ║
  ║   Format: long-form essay, no karma threshold to post                    ║
  ║   Short post: CẦN TẠO MỚI (adapt từ LW post, EA framing)               ║
  ║   Risk: thấp (nhỏ, intellectual)                                         ║
  ║                                                                           ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║ TIER A — SAU KHI TIER S ĐÃ STRESS-TEST (vừa, reach tốt)               ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                           ║
  ║ ④ Hacker News (~500K daily)                                               ║
  ║   Audience: tech-intellectual, engineering mindset                         ║
  ║   Fit: "structured like a codebase" angle, open-source, CC0              ║
  ║   Format: link tới blog post (Show HN: prefix)                           ║
  ║   Short post: CẦN REWRITE (Post B = text post, HN = link aggregator)      ║
  ║   Demo: Expert decisions — senior dev sees bug (tech-native)              ║
  ║   ⚠️ FORMAT: submit blog LINK, short post = author COMMENT (không body)  ║
  ║   Risk: TRUNG (frontpage → 300K views → kiểm soát khó)                  ║
  ║   ⚠️ Post SAU KHI Tier S đã refine content                               ║
  ║                                                                           ║
  ║ ⑤ r/cogsci (~129K)                                                       ║
  ║   Audience: cognitive science (bridge tech + neuro + psych)               ║
  ║   Fit: cross-domain synthesis, research citations, bridge platform       ║
  ║   Format: academic-accessible tone, cite studies                          ║
  ║   Short post: ĐÃ CÓ (short-post-overview.md Post C, ~280 words)            ║
  ║   Demo: Social cluster (5 questions → 1 architectural fact)               ║
  ║   Risk: thấp (nhỏ, academic)                                             ║
  ║                                                                           ║
  ║ ⑥ Bluesky                                                          [MỚI] ║
  ║   URL: https://bsky.app/                                                  ║
  ║   Audience: 20,000+ neuroscientists đã migrate từ X/Twitter               ║
  ║             400%+ tăng daily neuroscience posts                           ║
  ║             257+ neuroscience starter packs                               ║
  ║   Fit: neuroscience community ĐÃ CHUYỂN tới đây — bắt buộc có mặt      ║
  ║   Format: 300 chars/post + threads cho content dài. Link blog.           ║
  ║   Short post: CẦN TẠO MỚI (micro-format: 3-5 post thread)              ║
  ║   Risk: thấp (academic tone, neuroscience-native)                        ║
  ║   ⚠️ Build presence nhẹ trước (follow neuro starter packs)               ║
  ║                                                                           ║
  ║ ⑦ Lobsters                                                         [MỚI] ║
  ║   URL: https://lobste.rs/                                                 ║
  ║   Audience: invite-only tech community, signal/noise > HN                ║
  ║   Fit: "framework as codebase" angle, technical substance                ║
  ║   Format: link aggregator (submit blog link + brief description)         ║
  ║   Short post: KHÔNG CẦN (submit blog link trực tiếp)                     ║
  ║   Risk: thấp (nhỏ, chất lượng rất cao)                                  ║
  ║   ⚠️ Cần invitation từ existing member                                   ║
  ║                                                                           ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║ TIER B — MỞ RỘNG (sau khi có traction)                                  ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                           ║
  ║ ⑧ r/psychology (~1.5M+)                                                  ║
  ║   Short post: ĐÃ CÓ (short-post-overview.md Post D, ~250 words)            ║
  ║   Demo: Limerence mechanism (Fisher, Gottman, Aron)                      ║
  ║   ⚠️ Post SAU Tier A — broader, less technical audience                  ║
  ║                                                                           ║
  ║ ⑨ r/MachineLearning (~3.5M)                                              ║
  ║   Fit: prediction error ≠ reward, dopamine × RL reward modeling          ║
  ║   Format: [D] Discussion tag                                              ║
  ║   Short post: CẦN TẠO MỚI (ML-specific framing)                         ║
  ║   ⚠️ Low-effort posts bị delete — cần substantial content               ║
  ║                                                                           ║
  ║ ⑩ r/neuroscience (~500K+)                                                ║
  ║   Fit: domain expert verification                                        ║
  ║   ⚠️ Post CÂU HỎI CỤ THỂ, không full framework overview                ║
  ║   ⚠️ Đã có qua 3 neuro blogs — overview blog là BỔ SUNG                 ║
  ║                                                                           ║
  ║ ⑪ Mastodon academic                                                [MỚI] ║
  ║   Instances: fediscience.social, scholar.social, scicomm.xyz              ║
  ║   Audience: researchers trên decentralized platform                      ║
  ║   Format: 500 chars + threads. Link blog.                                ║
  ║   Short post: CẦN TẠO MỚI (micro-format, giống Bluesky)                 ║
  ║   Risk: thấp (nhỏ, academic)                                            ║
  ║                                                                           ║
  ║ ⑫ Discord neuroscience/cogsci servers                               [MỚI] ║
  ║   Servers: Prefrontal, r/consciousness, Noetica (40K members)            ║
  ║   Fit: ongoing discussion + feedback loops                               ║
  ║   Format: forum threads, share blog link                                 ║
  ║   ⚠️ Lurk trước, contribute value trước, promote sau                    ║
  ║                                                                           ║
  ║ ⑬ r/PhilosophyofMind                                               [MỚI] ║
  ║   Fit: consciousness component, body-first architecture                  ║
  ║   Short post: CẦN TẠO MỚI (philosophy framing)                          ║
  ║                                                                           ║
  ║ ⑭ Cognitive Sciences Stack Exchange                                 [MỚI] ║
  ║   URL: https://cogsci.stackexchange.com/                                  ║
  ║   Fit: Q&A format — trả lời câu hỏi bằng framework evidence             ║
  ║   Format: KHÔNG post framework trực tiếp. Trả lời CÂU HỎI có sẵn.      ║
  ║   ⚠️ Build authority qua answers trước, reference framework sau          ║
  ║                                                                           ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║ TIER C — DÀI HẠN (passive discovery + academic presence)                ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                           ║
  ║ ⑮ GitHub Awesome Lists                                              [MỚI] ║
  ║   Repos: awesome-neuroscience, open-computational-neuroscience-resources  ║
  ║          awesome-computational-neuroscience                               ║
  ║   Action: PR thêm framework vào list → passive discovery lâu dài         ║
  ║                                                                           ║
  ║ ⑯ Substack collaboration                                           [MỚI] ║
  ║   Targets: Simply Neuroscience, Dr. Tommy Blanchard, Shane O'Mara        ║
  ║   Action: engage qua comments trước, pitch collaboration sau             ║
  ║                                                                           ║
  ║ ⑰ Manifold Markets                                                 [MỚI] ║
  ║   URL: https://manifold.markets/                                          ║
  ║   Audience: rationalist prediction market community                      ║
  ║   Action: tạo prediction markets cho framework claims                    ║
  ║   VD: "Will dopamine ≠ reward be confirmed in next major review?"        ║
  ║   ⚠️ Creative engagement tool, không phải primary distribution          ║
  ║                                                                           ║
  ╚═══════════════════════════════════════════════════════════════════════════╝
```

### 1.2 — Infrastructure Platforms (Song Song, Không Phải Community)

```
  ┌───────────────────────────────────────────────────────────────────────┐
  │ PLATFORM          │ MỤC ĐÍCH                      │ KHI NÀO          │
  ├───────────────────────────────────────────────────────────────────────┤
  │ OSF (osf.io)      │ Host project + DOI assignment  │ TRƯỚC publish     │
  │                   │ → academic citable, FAIR       │                   │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Zenodo (CERN)     │ Permanent archive + DOI        │ TRƯỚC publish     │
  │                   │ → long-term preservation       │                   │
  ├───────────────────────────────────────────────────────────────────────┤
  │ ResearchGate      │ Upload framework as project    │ Song song publish  │
  │                   │ → academic discoverability     │                   │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Academia.edu      │ Upload → discoverability       │ Song song publish  │
  │                   │ 266M users                     │                   │
  ├───────────────────────────────────────────────────────────────────────┤
  │ ORCID             │ Researcher profile             │ TRƯỚC publish     │
  │                   │ → link tất cả outputs          │ (đã trong prereq) │
  ├───────────────────────────────────────────────────────────────────────┤
  │ PsyArXiv/bioRxiv  │ Preprint cho specific claims   │ SAU overview blog  │
  │                   │ → academic peer review         │ (separate effort)  │
  └───────────────────────────────────────────────────────────────────────┘
```

### 1.3 — Audience KHÔNG Target (dù là tech)

```
  ✗ Productivity / self-help tech community
    → Risk: take framework → làm app "dopamine tracker" → SAI mechanism → damage
  ✗ Startup/growth hacker community
    → Risk: dùng framework → "exploit body-reward" → ĐẢO NGƯỢC mục đích
  ✗ Mass programmer community (r/programming general)
    → Risk: đọc title → không đọc sâu → oversimplify → "dopamine tip" level
  ✗ "Tech bro" self-optimization
    → Risk: "biohack dopamine" → đúng cái mà framework PHẢN BÁC

  → Source: plan-tech-distribution.md §1.2 (extracted trước khi backup)
```

---

## §2 — SHORT POST STRATEGY

### 2.1 — Approach: 1 Core Message, Format-Adapted

```
  LOGIC:
    → Tất cả posts dẫn về CÙNG 1 blog overview
    → Mục đích posts = DISTRIBUTION (đưa tới nhiều cộng đồng)
    → Nhiều người CHỈ hoạt động ở 1 platform → thấy 1 post DUY NHẤT
    → Posts na ná = ĐÚNG. Không phải bug, là feature.
    → Khác biệt chỉ ở FORMAT + tinh chỉnh nhẹ câu chữ

  NGUYÊN TẮC:
    → Trình bày thẳng: đây là gì, chứa gì (substance description)
    → KHÔNG question-hook (gây lệch pha: question cục bộ ↔ blog toàn diện)
    → KHÔNG feature list ("200+ files, structured like..." = anti-pattern)
    → KHÔNG "I built..." opener (self-promotional)
    → Tinh chỉnh FORMAT per platform, KHÔNG rewrite content
    → Chi tiết cấu trúc: xem plan-overview-blog.md §4

  TẠI SAO KHÔNG QUESTION-HOOK (khác neuro posts):
    Neuro: question-hook → blog deep-dive 1 claim = MATCH (cùng scope)
    Overview: question-hook → blog overview 11 questions = MISMATCH
    → Reader click vì tò mò 1 question → vào blog thấy framework rộng → lệch pha
    → Trình bày thẳng "đây là framework, chứa X" = honest, đúng expectation
```

### 2.2 — Post Structure Chuẩn (tóm tắt từ plan-overview-blog.md §4.1)

```
  ① WHAT: framework connecting neuro + psych + evolution (1-2 câu)
  ② CONTAINS: 11 questions, 6 mechanism sketches, citations, falsification (2-3 câu)
  ③ POSITION: body first, PFC second (1 câu)
  ④ MECHANISM TEASE: 1 ví dụ — phần duy nhất tinh chỉnh nhẹ (2-3 câu)
  ⑤ EPISTEMIC: hypothesis inviting falsification (1 câu)
  ⑥ LINKS: blog + GitHub
  ⑦ CLOSE: invitation to challenge (1-2 câu)

  KHÔNG CÓ TRONG SHORT POSTS (thuộc blog):
    → Full divergences list
    → Full question list (tease 2-3 trong CONTAINS)
    → Cluster explanation
    → Limitations
    → AI starter prompt
```

### 2.3 — Format Groups

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │ FORMAT             │ PLATFORMS                       │ GHI CHÚ       │
  ├──────────────────────────────────────────────────────────────────────┤
  │ A: Text post       │ LessWrong, r/slatestarcodex,    │ Full body     │
  │    (full body)     │ EA Forum, r/cogsci, r/psychology,│ as post text  │
  │                    │ r/MachineLearning,               │ ~250-400 words│
  │                    │ r/PhilosophyofMind, r/neuroscience│              │
  ├──────────────────────────────────────────────────────────────────────┤
  │ B: Link + comment  │ Hacker News, Lobsters            │ Submit blog   │
  │    (link post)     │                                  │ URL, body =   │
  │                    │                                  │ author comment│
  │                    │                                  │ ~150-250 words│
  ├──────────────────────────────────────────────────────────────────────┤
  │ C: Micro-thread    │ Bluesky (300 chars/post),        │ Thread 3-5    │
  │                    │ Mastodon (500 chars/post)         │ posts         │
  └──────────────────────────────────────────────────────────────────────┘
```

### 2.4 — Platform Adjustments (NHẸ — chi tiết tại plan-overview-blog.md §4.3)

```
  Core message GIỐNG NHAU. Chỉ tinh chỉnh nhẹ:

  LessWrong:       + [Epistemic status], compiled vs fresh tease
  r/slatestarcodex:+ psychiatry angle nhẹ
  EA Forum:        + AI safety angle nhẹ
  HN:              Format B: "Show HN:", link + author comment
  Lobsters:        Format B: submit link only (invite-only)
  r/cogsci:        + citations prominent, social cluster tease
  r/psychology:    Accessible language, limerence tease
  r/ML:            [D] tag, prediction error ≠ reward, RL terminology
  r/PhilosophyofMind: consciousness angle nhẹ
  r/neuroscience:  Domain expert framing nhẹ
  Bluesky:         Format C: micro-thread + #Neuroscience
  Mastodon:        Format C: micro-thread + CamelCase hashtags
```

### 2.5 — Post Status

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ PLATFORM           │ FORMAT │ STATUS                              │
  ├────────────────────────────────────────────────────────────────────┤
  │ LessWrong          │ A      │ CẦN REWRITE (Post A — structure cũ) │
  │ Hacker News        │ B      │ CẦN REWRITE (Post B — sai format)   │
  │ r/cogsci           │ A      │ CẦN REWRITE (Post C — structure cũ) │
  │ r/psychology       │ A      │ CẦN REWRITE (Post D — structure cũ) │
  │ r/slatestarcodex   │ A      │ CẦN TẠO (adapt từ base)             │
  │ EA Forum           │ A      │ CẦN TẠO (adapt từ base)             │
  │ Bluesky            │ C      │ CẦN TẠO (micro-thread)              │
  │ r/MachineLearning  │ A      │ CẦN TẠO (ML framing)                │
  │ Mastodon           │ C      │ CẦN TẠO (adapt Bluesky thread)      │
  │ r/PhilosophyofMind │ A      │ CẦN TẠO (adapt base)                │
  │ r/neuroscience     │ A      │ CẦN TẠO (domain adapt)              │
  │ Lobsters           │ B      │ KHÔNG CẦN (submit link only)         │
  │ Discord servers    │ —      │ Share link (contribute first)         │
  │ CogSci SE          │ —      │ Answer questions (build authority)    │
  └────────────────────────────────────────────────────────────────────┘

  VÌ POSTS NA NÁ — THỰC TẾ CẦN VIẾT:
    → 1 base post (core message theo §4.1)
    → Adapt format: 3 variants (text post, link+comment, micro-thread)
    → Tinh chỉnh per platform: mechanism tease swap + câu chữ nhẹ
    → Hiệu quả hơn nhiều so với viết 10+ bài riêng biệt

  PRIORITY:
    1. Rewrite base post + 4 core platforms (LW, HN, r/cogsci, r/psychology)
    2. Adapt Tier S: r/slatestarcodex, EA Forum
    3. Tạo micro-thread: Bluesky, Mastodon
    4. Tạo ML-specific: r/MachineLearning
    5. Adapt còn lại: r/PhilosophyofMind, r/neuroscience
```

### 2.6 — Consistency Check

```
  Short posts PHẢI tuân thủ:
    □ plan-overview-blog.md §4.1 (core structure — 7 components)
    □ plan-overview-blog.md §6.2 (tone — substance description, not hook)
    □ plan-overview-blog.md §6.3 (anti-patterns — no feature list, no grand claim)
    □ plan-overview-blog.md §6.4 (W.4 checkpoint — mechanism, not advice)
    □ KHÔNG feature list opening
    □ KHÔNG question-hook opening
    □ KHÔNG divergences list (thuộc blog)
    □ KHÔNG "I built..." opener
```

---

## §3 — POSTING CADENCE

### 3.1 — Thứ Tự Execution

```
⚠️ KHÔNG POST TẤT CẢ CÙNG LÚC.

TUẦN 1: Tier S — Stress-test
  → Post LessWrong (Post A)
  → Đợi 3-5 ngày → đọc feedback → refine
  → Post r/slatestarcodex (Post E)
  → Đợi 3-5 ngày → đọc feedback → refine
  → Post EA Forum (Post F)

TUẦN 2-3: Tier A — Broaden
  → Refine content từ Tier S feedback
  → Post Hacker News (Post B) — "Show HN:" prefix
  → Đợi 3-5 ngày
  → Post r/cogsci (Post C)
  → Đợi 3-5 ngày
  → Post Bluesky thread (Post G)
  → Nếu có Lobsters invitation → submit blog link

TUẦN 4-5: Tier B — Expand
  → Post r/psychology (Post D)
  → Post r/MachineLearning (Post H) — nếu relevant
  → Post Mastodon thread (Post I)
  → Post r/PhilosophyofMind (Post J)
  → Join Discord servers + share trong forum threads

TUẦN 6+: Tier C — Long-term
  → PR vào GitHub Awesome Lists
  → Engage Substack newsletters qua comments
  → Tạo Manifold Markets cho framework claims (optional)
  → Trả lời câu hỏi trên Cognitive Sciences SE

SONG SONG (khi nào cũng được):
  → Setup OSF + Zenodo (infrastructure, không phải community)
  → Upload ResearchGate + Academia.edu
  → Update ORCID profile

RULES:
  → Max 1 post / tuần across all platforms
  → KHÔNG post multiple platforms cùng ngày (spam detection)
  → Đợi feedback trước khi post tiếp
  → Nếu post bị ignore → refine framing, KHÔNG spam lại
  → Nếu post có traction → respond comments → THEN post tiếp
```

### 3.2 — Platform-Specific Rules

```
LESSWRONG:
  → [Epistemic status: hypothesis, inviting falsification]
  → Crosspost tới Alignment Forum nếu AI-relevant
  → Acknowledge uncertainty, steelman counterarguments
  → ⚠️ Bad epistemics = downvote nhanh = mất credibility

HACKER NEWS:
  → Submit LINK (tới blog), không text post
  → Title: factual, KHÔNG clickbait (HN editors sẽ đổi clickbait title)
  → Respond comments NHANH trong 2h đầu (algorithm boost)
  → "Show HN:" prefix phù hợp cho open-source project
  → ⚠️ KHÔNG post weekend (traffic thấp)

EA FORUM:
  → Frame: human cognition relevant cho AI safety + decision-making
  → Be accurate, kind, relevant
  → Focus: understanding human reward system → better AI alignment
  → Link tới LW post nếu đã có traction (cross-validation)

r/SLATESTARCODEX:
  → Long-form welcome, intellectual depth expected
  → Psychiatry/neuroscience topic = natural fit cho community
  → Scott Alexander's readership biết Kahneman, Berridge, predictive processing

BLUESKY:
  → Follow neuroscience starter packs TRƯỚC (build minimal presence)
  → Thread format: 3-5 posts, mỗi post 1 key insight
  → Last post = blog link + "Find where it breaks"
  → Use hashtags: #neuroscience #cogsci #openscience
  → ⚠️ Đây là nơi neuroscientists ĐÃ MIGRATE — cần academic tone

LOBSTERS:
  → Invite-only — cần invitation từ existing member
  → Submit blog link trực tiếp (không tạo short post)
  → Transparent moderation — substance matters

r/MACHINELEARNING:
  → [D] Discussion tag
  → Technical language: prediction error, reward signal, RL terminology
  → Connect tới existing ML concepts (reward shaping, curiosity-driven)
  → ⚠️ Low-effort bị delete — cần substantial content

DISCORD SERVERS:
  → Lurk 1-2 tuần trước khi post
  → Contribute value (trả lời câu hỏi) trước khi share framework
  → KHÔNG vào drop link rồi đi — contribute to community

MASTODON:
  → CamelCase hashtags (accessibility)
  → Academic tone trên fediscience.social, scholar.social
  → Thread format giống Bluesky nhưng 500 chars/post (dài hơn)
```

---

## §4 — RESPONDING PROTOCOL

```
MỌI PLATFORM, CÙNG NGUYÊN TẮC:

KHI CÓ CHALLENGE (substantive):
  → Reply trong 24h
  → "Good point. Here's the evidence: [citation]"
  → KHÔNG defensive. Welcome challenge = credibility.

KHI CÓ GAP:
  → "We don't know. That's a genuine gap."
  → Ghi lại gap → cập nhật framework → credit người challenge

KHI CÓ COUNTER-EVIDENCE:
  → "The evidence suggests otherwise: [3 studies]"
  → Nhưng: acknowledge nếu counter-evidence mạnh hơn
  → Nếu bị falsify → CẬP NHẬT framework → public note

KHI AI HỎI CREDENTIALS:
  → "Independent researcher. Game developer by background.
     Framework is CC0 — test the claims, not the credentials.
     Here's the evidence: [links]"

KHI AI KHEN:
  → Redirect tới verification
  → "Thanks — we need MORE challenge, not less.
     Here's what we're LEAST confident about: [gaps].
     Can you find holes?"

KHI AI SHARE PERSONAL EXPERIENCE:
  → Listen + redirect tới mechanism
  → "That's a meaningful observation. The model predicts
     [mechanism]. Does that match?"
  → KHÔNG: "Your experience is explained by X" (condescending)
```

---

## §5 — PRE-REQUISITES

### 5.1 — Trước Khi Publish Blog

```
PHẢI CÓ:
  □ Blog live và accessible trên GitHub Pages
  □ Tất cả links hoạt động (blog URL, repo URL, 3 neuro blog URLs)
  □ Framework core files dịch EN (hoặc đang dịch)
  □ GitHub Discussions enabled
  □ ORCID iD registered
  □ Base post rewritten theo structure mới (plan-overview-blog.md §4.1)
  □ 4 core platform posts ready (LW, HN, r/cogsci, r/psychology)

NÊN CÓ (trước Tier S):
  □ Tier S platform posts adapted (r/slatestarcodex, EA Forum)
  □ OSF project created + DOI
  □ Zenodo archive + DOI
  □ Bluesky account created + follow neuro starter packs

CÓ THỂ LÀM SAU:
  □ Remaining platform adapts (Tier A/B — khi cần)
  □ Lobsters invitation
  □ Discord presence
  □ ResearchGate + Academia.edu profiles
  □ Substack engagement
  □ Manifold Markets
```

### 5.2 — Pre-Post Checklist (Áp Dụng MỌI Platform)

```
TRƯỚC MỖI POST:
  □ Blog live và accessible
  □ All links working (blog, repo)
  □ Re-read short post: tone matches platform norms?
  □ Not self-help framing (W.4 check)
  □ Counter-evidence invited explicitly
  □ No marketing language ("star the repo", "share this")
  □ Platform rules checked (mỗi sub có rules riêng)
  □ Previous platform feedback incorporated (nếu có)
```

---

## §6 — SUCCESS + FAILURE SIGNALS

```
  ┌────────────────────────────────────────────────────────────────┐
  │ TÍN HIỆU THÀNH CÔNG                                          │
  ├────────────────────────────────────────────────────────────────┤
  │ → Comments hỏi về mechanism CỤ THỂ (not just "cool!")        │
  │ → Counter-evidence: "Research Z says otherwise" = HIGH-VALUE  │
  │ → Domain experts engage (not just tech)                       │
  │ → GitHub: stars + discussions + forks (engagement, not vanity)│
  │ → Blog traffic from short posts > 10% click-through          │
  │ → Cross-platform mentions (someone links từ platform khác)   │
  │ → Someone tests framework predictions → reports match/break  │
  │ → Tech bloggers viết independent analysis                    │
  ├────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU CẦN REFINE                                          │
  ├────────────────────────────────────────────────────────────────┤
  │ → Ignored ở Tier S → framing/tone cần adjust                 │
  │ → Only "cool!" comments → consumption, not verification      │
  │ → Stars without engagement → vanity metric                   │
  │ → Self-help community picks up → W.4 framing cần strengthen  │
  ├────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU THẤT BẠI (cần reassess)                             │
  ├────────────────────────────────────────────────────────────────┤
  │ → Multiple domain experts: "fundamentally wrong"              │
  │ → Specific falsifications không trả lời được                 │
  │ → All platforms ignore → framework/framing problem            │
  └────────────────────────────────────────────────────────────────┘
```

---

## §7 — RISK MANAGEMENT

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ RISK                      │ SEVERITY │ MITIGATION                 │
  ├────────────────────────────────────────────────────────────────────┤
  │ R1: Viral trước khi ready │ CAO      │ Tier S trước. Nếu viral → │
  │     (HN frontpage quá sớm)│          │ respond bình tĩnh,         │
  │                           │          │ redirect tới VERIFY.md     │
  ├────────────────────────────────────────────────────────────────────┤
  │ R2: "Tech bro science"   │ TRUNG    │ Post r/cogsci song song.  │
  │     (domain expert dismiss│          │ Frame: "inviting domain    │
  │      vì tech adopted)     │          │ expert review"             │
  ├────────────────────────────────────────────────────────────────────┤
  │ R3: Echo chamber          │ TRUNG    │ Mỗi post kết thúc:        │
  │     (tech all agree,      │          │ "What breaks this?"        │
  │      no challenge)        │          │ Thank challenges > agrees  │
  ├────────────────────────────────────────────────────────────────────┤
  │ R4: AI-mediated Dunning-  │ TRUNG    │ Blog + VERIFY.md phân biệt│
  │     Kruger (tech dùng AI  │          │ "AI can check: logic"      │
  │     verify → think done)  │          │ "AI CANNOT check: empirical│
  │                           │          │  truth, methodology"       │
  ├────────────────────────────────────────────────────────────────────┤
  │ R5: Cross-post spam flag  │ THẤP     │ Max 1 post/tuần.           │
  │                           │          │ KHÔNG multiple subs/ngày.  │
  │                           │          │ Posts na ná nhưng adapt    │
  │                           │          │ format + mechanism tease   │
  ├────────────────────────────────────────────────────────────────────┤
  │ R6: Self-help misuse      │ TRUNG    │ W.4 strict. Mechanism-only.│
  │     (overview blog bị lấy │          │ No advice, no prescription.│
  │      làm self-help)       │          │ Blog has "Honest limits"   │
  └────────────────────────────────────────────────────────────────────┘
```

---

## §8 — RELATION TO OTHER PLANS

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │ PLAN                          │ RELATIONSHIP                        │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-overview-blog.md          │ = Blog CONTENT structure (§§1-10)   │
  │                               │   Plan này = blog DISTRIBUTION      │
  │                               │   2 plans BỔ SUNG nhau              │
  ├──────────────────────────────────────────────────────────────────────┤
  │ Tech/backup/plan-tech-          │ = BACKED UP. Unique parts extracted:│
  │   distribution.md              │   §1.2 → §1.3 (anti-target)        │
  │                               │   §4 → github-infrastructure.md     │
  │                               │   T3-T5 → future-topic-ideas.md    │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-neuro-posts.md           │ = Neuro blog distribution (A/B/C)   │
  │                               │   Plan này = Overview blog (D)      │
  │                               │   Cùng pattern: blog + short posts  │
  │                               │   Khác: substance-first vs hook     │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-logic-feeling-            │ = Logic-Feeling blog distribution   │
  │   distribution.md             │   (E) — 16 platforms, identity-     │
  │                               │   challenge specific framing        │
  │                               │   SAU overview blog trong sequence  │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-adhd-tech-distribution.md│ = ADHD × tech specialized           │
  │                               │   Plan này KHÔNG cover ADHD subs    │
  │                               │   ADHD plan SAU overview plan       │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-public.md                │ = General strategy, framing rules   │
  │                               │   W.4, W.5 ÁP DỤNG cho plan này   │
  ├──────────────────────────────────────────────────────────────────────┤
  │ short-post-overview.md           │ = 4 short posts (A-D) — CẦN REWRITE│
  │                               │   theo structure mới (§4.1)         │
  │                               │   Plan này track + map all posts    │
  ├──────────────────────────────────────────────────────────────────────┤
  │ framing-engagement-value.md   │ = 3-layer value model               │
  │                               │   Áp dụng cho mọi post             │
  └──────────────────────────────────────────────────────────────────────┘

  EXECUTION ORDER (across plans):
    1. plan-neuro-posts → 3 neuro blogs publish
    2. plan-overview-distribution (file này) → overview blog publish
    3. plan-adhd-tech-distribution → ADHD × tech posts
    4. future-topic-ideas.md → remaining T-topics (T3, T4, T5)
    
    HOẶC: overview blog CÓ THỂ publish SONG SONG với neuro blogs
    (xem §0.2 — quyết định flexible)
```

---

## §9 — TỔNG KẾT PLATFORM

```
  TỔNG: 17 platforms (+ infrastructure)

  CẦN REWRITE (4):           LessWrong, HN, r/cogsci, r/psychology
                              (Posts A-D không tuân thủ structure mới §2.2)
  CẦN TẠO (7):               r/slatestarcodex, EA Forum, Bluesky,
                              r/MachineLearning, Mastodon, r/PhilosophyofMind,
                              r/neuroscience
  KHÔNG CẦN SHORT POST (3):  Lobsters (link), CogSci SE (answers), Discord (share)
  INFRASTRUCTURE (4):         OSF, Zenodo, ResearchGate, Academia.edu

  ĐÃ CÓ TRONG PLAN CŨ (8):  LessWrong, r/slatestarcodex, HN, r/ML,
                              r/cogsci, r/neuroscience, r/psychology, Medium
  MỚI TỪ KHẢO SÁT (9):      EA Forum, Bluesky, Lobsters, Mastodon,
                              Discord servers, r/PhilosophyofMind,
                              CogSci SE, Manifold Markets, Substack collab
  INFRASTRUCTURE MỚI (4):    OSF, Zenodo, ResearchGate, Academia.edu

  APPROACH: 1 core message → adapt format per platform (xem §2)
  VÌ POSTS NA NÁ: viết 1 base + 3 format variants + minor adjustments
```

---

> **Plan v0.2 — updated 2026-06-04.**
> Thay đổi từ v0.1:
>   - §2 rewritten: template grouping → format grouping + substance description
>   - Post structure: KHÔNG question-hook, KHÔNG feature list
>   - Approach: 1 core message, na ná, adapt format per platform
>   - Posts A-D: cần rewrite theo structure mới
>   - References: plan-tech-blog.md → plan-overview-blog.md
>
> Bước tiếp:
>   1. Rewrite base post + 4 core platforms (LW, HN, r/cogsci, r/psychology)
>   2. Adapt Tier S: r/slatestarcodex, EA Forum
>   3. Tạo micro-thread: Bluesky, Mastodon
>   4. Setup infrastructure: OSF, Zenodo, ORCID
>   5. Blog publish → execute Tier S → gauge → Tier A → Tier B
