# Plan: Overview Blog + Short Posts — Framework Overview cho Tech Expert Audience

> **Goal:** 1 blog đầy đủ + short posts per-platform. Giới thiệu framework cho tech experts.
> **Strategy change:** plan-neuro-posts.md §1 ghi "Tech post = POST ONLY (không có blog)."
>   → NAY THAY ĐỔI: Tech cũng có blog riêng + short posts, giống pattern 3 bài neuro.
>   → Lý do: v3 content quá chất lượng để compress vào 300-word forum post. Blog cho phép
>     trình bày đầy đủ mà không bị giới hạn format forum.
> **Position in strategy:** SAU 3 neuro blogs. Neuro = verify claims cụ thể. Tech = broaden audience + expose framework.
> **Principle:** Substance description — đây là gì, chứa gì, evidence, find where it breaks.
> **Status:** PLANNING (updated 2026-06-04)
> **Created:** 2026-06-04
> **Renamed from:** plan-tech-blog.md (2026-06-04)
> **References:**
>   drill-tech-post-v2.md — drill phân tích 7 câu hỏi (mechanism chains, formulations, audience)
>   tech-post-draft-v3.md — draft hiện tại (~1,750 words), foundation cho blog
>   Tech/backup/plan-tech-post.md — strategy gốc (Angle E, anti-patterns — BACKED UP, key content absorbed here)
>   plan-neuro-posts.md — neuro blog pattern (2-tier: blog + short posts)
>   plan-overview-distribution.md — distribution plan cho overview blog (17 platforms)
>   short-posts-dopamine.md — short post template reference

---

## §1 — GOALS

```
  BLOG DOES:
    ① PRESENT: Framework overview — đủ để thấy substance, không overwhelming
    ② DEMONSTRATE: 6 mechanism sketches + 1 cluster = "framework giải thích được NHIỀU thứ"
    ③ BRIDGE: Questions (relatable) → Mechanisms (substance) → GitHub (full framework)
    ④ TRUST: Honest limitations, falsification criteria, CC0

  SHORT POSTS DO:
    ⑤ HOOK: 3-4 câu hỏi compelling + 1 mechanism tease
    ⑥ ROUTE: Dẫn traffic tới blog (và blog dẫn tới GitHub)
    ⑦ FIT: Đúng tone per-platform (LW, HN, Reddit)

  NEITHER DOES:
    ✗ Giải thích đầy đủ framework (đó là job của repo)
    ✗ Deep-dive 1 mechanism (đó là job của 3 neuro blogs)
    ✗ Self-help framing (W.4)
    ✗ Convince — let evidence speak
```

---

## §2 — AUDIENCE: TECH EXPERTS

```
  WHO:
    → Software engineers, AI/ML practitioners, data scientists
    → LessWrong / Hacker News / r/cogsci readers
    → Cross-domain thinkers (tech + psychology intersection)

  WHY THIS IS THE HIGHEST-POTENTIAL AUDIENCE:
    ① Biết dùng AI → navigate 200+ files bằng AI (barrier thấp nhất)
    ② "Codebase" analogy ngay lập tức relatable → structure = trust signal
    ③ Compiled vs Fresh → map trực tiếp vào experience (senior vs junior dev)
    ④ CC0 + open-source = ngôn ngữ tự nhiên
    ⑤ Xác suất biết psychology/behavioral science cao (đặc biệt LW, HN)
    ⑥ Culture: "show me the code" = framework's approach (show mechanism, not claim)

  WHAT THEY ALREADY KNOW:
    → Kahneman System 1/2 (table-stakes)
    → Basic neuroscience (dopamine, serotonin — surface level)
    → Bayesian updating, prediction error
    → Open-source culture, code review norms

  WHAT WILL SURPRISE THEM:
    → "Compiled vs Fresh" = better axis than "System 1 vs System 2"
    → Cortisol = amplifier, not stress
    → Status = resource access map (350 million years)
    → Limerence = temporary hardware subsidy with timeline
    → CC0 + explicit confidence levels + tracked open questions
```

---

## §3 — BLOG STRUCTURE (detailed)

> **Target: ~3,000-3,500 words.**
> So sánh: 3 neuro blogs = 5,000-6,000 words (deep-dive 1 mechanism).
> Tech blog = broad overview (nhiều mechanism, ít depth hơn per-topic).
> Nguyên tắc: đủ để thấy substance, KHÔNG lan man làm mất hứng đọc.

### §3.1 — Section-by-section

```
  ① TITLE + EPISTEMIC STATUS                              ~60 words
     Title (chốt): "A concept bridging neuroscience and psychology into a
       connected model — estimating the direction of human drive"
     Epistemic status: hypothesis inviting falsification, 200+ files, CC0
     SOURCE: v3 — giữ nguyên

  ② SUMMARY                                                ~120 words    [NEW]
     Following neuro blog pattern (dopamine blog mở bằng summary list).
     Numbered list: what this post presents.
       1. Cross-domain framework (neuro + psych + evolution)
       2. 11 questions with mechanistic answers
       3. 6 mechanism sketches with research citations
       4. 1 question cluster tracing to one architectural fact
       5. 4 positions where framework diverges from mainstream
       6. Explicit limitations and falsification criteria
     SOURCE: new (tổng hợp từ v3 content)

  ③ HOOK                                                   ~150 words
     Hook A (chốt) — expand thêm 1-2 câu so với v3.
     P1: Cross-referenced research → 200+ files → codebase structure
     P2: One premise (body > PFC) → monitoring process vs main thread
     P3 (optional expand): "Unlike a textbook..." differentiator
     SOURCE: v3 hook — expand nhẹ

  ④ THE QUESTIONS                                          ~280 words
     Same as v3: 6 single questions + cluster (5 sub-questions)
     Ordering: ①③④⑤⑥⑦ (singles) → ② cluster (cuối)
     Cluster format: "These five questions seem unrelated:" → 5 bullets →
       "The framework traces all five to one architectural fact..."
     Bridge paragraph: "These aren't rhetorical..."
     SOURCE: v3 — giữ nguyên

  ⑤ MECHANISM SKETCHES                                     ~1,400 words  [EXPAND]
     3 expanded + 3 brief — same questions as v3, nhưng EXPAND:

     EXPANDED (mỗi sketch ~250 words, tăng từ v3's ~160):
       ① Social media drain vs close friend    [+thêm ví dụ, +nuance]
       ⑥ Expert decisions vs forced thinking    [+thêm cross-domain examples]
       ⑦ Limerence → marriage                  [+Resonance Decline detail]

     BRIEF (mỗi sketch ~100 words, tăng từ v3's ~75):
       ③ Humans can't sit still                [+hardwired vs compilable contrast]
       ④ Status cross-species                  [+human layer complexity]
       ⑤ Creative stress                       [+when harmful expanded]

     GUIDELINES:
       → Mỗi sketch tự chứa (self-contained) — không assume đọc sketch khác
       → Kết thúc bằng *Source + Research* citation
       → W.4 check: mechanism description, KHÔNG phải advice
       → Blog format cho phép paragraph breaks, quotes — tận dụng

     SOURCE: v3 sketches — expand dựa trên drill-tech-post-v2.md mechanism chains

  ⑥ THE CLUSTER EXPLAINED                                 ~250 words    [NEW]
     Reveal "one architectural fact" ở SUMMARY level:
       → Social = body-base REQUIREMENT (not preference)
       → dACC reuse: social pain = physical pain circuits (Eisenberger 2003)
       → Social Baseline Theory: body DEFAULT = with others (Coan 2015)
       → Entity-Compiled: close people = body-base EXTENSIONS
       → Loneliness = architectural deviation → measurable health impact

     KHÔNG deep-dive — đó là job của Connection.md, Inter-Body-Mechanism.md
     Closing: "The five questions above are five expressions of this one fact.
       The source files map the full mechanism."

     SOURCE: drill-tech-post-v2.md §1.2 (cluster mechanism analysis)

  ⑦ WHAT THIS FRAMEWORK IS                                ~150 words
     Same as v3, slight expand:
       Computer analogy, scale, structure, core cycle, philosophy, language
     SOURCE: v3 — giữ nguyên, có thể expand nhẹ

  ⑧ WHERE THIS DIVERGES                                   ~250 words
     4 examples: dopamine, cortisol, conscious mind, prediction error
     Same as v3 — strong section, không cần thay đổi
     SOURCE: v3 — giữ nguyên

  ⑨ HONEST LIMITATIONS                                    ~120 words
     5 points: not neuroscientist, hypothesis not theory,
       substrate blackbox, Vietnamese primary, confirmation bias
     SOURCE: v3 — giữ nguyên

  ⑩ GETTING STARTED                                       ~300 words    [EXPAND]
     Expand from v3 CTA:
       → AI starter prompt (full version — v2 có 8 files, blog có không gian)
       → Step-by-step: Clone → Drop vào AI → Read Ask-AI.md → Ask
       → Per-expertise guide (expanded — mỗi expertise 1-2 câu)
       → "Find where it breaks" (strongest line)
       → Counter-evidence > confirmation

     SOURCE: v3 CTA + v2 AI starter prompt (expand)

  ⑪ FOOTER                                                ~80 words
     GitHub link
     3 neuro blog links (with real URLs)
     Closing: "This is a hypothesis inviting falsification. What would break it?"
     SOURCE: v3 footer — giữ nguyên

  ─────────────────────────────────────────────────
  TỔNG BLOG: ~3,160 words (range 2,800-3,500)
  ĐỌC: ~14-16 phút
  SO SÁNH: Neuro blogs ~5,700 words trung bình. Tech blog ngắn hơn vì overview, không deep-dive.
```

### §3.2 — Blog format decisions

```
  FILENAME: docs/_posts/YYYY-MM-DD-bridging-neuroscience-psychology.md
    (date = ngày publish thực tế)

  URL: hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/

  YAML FRONTMATTER (following neuro blog pattern):
    layout: post
    title: [same as v3 title]
    date: [publish date]
    author: Independent researcher
    license: CC0 1.0 Universal
    status: Draft v0.1
    tags: [neuroscience, psychology, evolutionary-biology, cognitive-science,
           open-source, falsifiable, behavioral-science, framework]

  LINK TỪ TECH POST FOOTER (v3) CẦN UPDATE:
    → Hiện tại v3 footer chỉ link 3 neuro blogs
    → Sau khi có tech blog: tech blog = primary destination
    → Short posts link tới tech blog
    → Tech blog footer link tới 3 neuro blogs + GitHub
```

---

## §4 — SHORT POSTS STRUCTURE

> KHÁC VỚI NEURO SHORT POSTS:
>   Neuro posts: question-hook → blog deep-dive 1 claim = MATCH (cùng scope)
>   Overview posts: straight presentation → blog overview framework = MATCH (cùng scope)
>   Question-hook cho overview = MISMATCH (question cục bộ ↔ blog toàn diện)
>
> NGUYÊN TẮC:
>   ① Trình bày thẳng: đây là gì, chứa gì (substance description)
>   ② Na ná giữa các platforms (cùng 1 blog → cùng 1 core message)
>   ③ Tinh chỉnh FORMAT per platform (text post vs link+comment vs micro-thread)
>   ④ KHÔNG question-hook (gây lệch pha), KHÔNG feature list (anti-pattern §6.3)
>
> FILENAME: Public-Plan/blog/short-post-overview.md

### §4.1 — Core Structure (áp dụng mọi platform)

```
  ① WHAT (1-2 câu):
     Đây là framework connecting [domains]. Mô tả SUBSTANCE, không features.
     → CÓ: "A framework connecting neuroscience, psychology, and evolutionary
            biology into a single architecture."
     → KHÔNG: "I built..." (self-promotional — feature-list opener)
     → KHÔNG: "Why does scrolling..." (question-hook → scope mismatch)
     → KHÔNG: "200+ files, structured like a codebase..." (feature list §6.3)

  ② CONTAINS (2-3 câu):
     Nội dung blog — reader biết CHÍNH XÁC sẽ tìm thấy gì khi click.
     → "Proposes mechanistic answers to 11 questions — from why social
        media drains to why limerence ends."
     → "Each with research citations and explicit conditions for being wrong."
     → "200+ files, open-source, CC0." (scale = ở đây, KHÔNG phải ở WHAT)

  ③ POSITION (1 câu):
     Core premise: body evaluates first, PFC observes second.
     → Ngắn gọn. Không giải thích. Blog sẽ giải thích.

  ④ MECHANISM TEASE (2-3 câu):
     1 ví dụ cụ thể of how framework answers a question.
     → Phần DUY NHẤT có thể tinh chỉnh nhẹ per platform group
     → Shows HOW framework thinks, không chỉ WHAT it covers
     → Ví dụ mặc định: compiled vs fresh processing
       (senior dev "sees" bug = compiled; junior debugs hours = fresh)
     → Platform alternatives: social cluster, limerence, ML prediction error

  ⑤ EPISTEMIC STATUS (1 câu):
     "Hypothesis inviting falsification. Individual findings = established
      science; proposed connections = new and unvalidated."

  ⑥ LINKS:
     Blog URL + GitHub URL

  ⑦ CLOSE (1-2 câu):
     Mời challenge. Cụ thể hơn generic "where does this break."
     → "Counter-evidence is more valuable than confirmation."
     → Optional: câu hỏi cụ thể tied to mechanism tease

  TẠI SAO STRUCTURE NÀY:
    → WHAT + CONTAINS = reader expectation MATCH blog content (không lệch pha)
    → MECHANISM TEASE = shows substance (không chỉ claim, mà DEMONSTRATE)
    → EPISTEMIC = honest framing (W.4 compliant)
    → Không divergences list trong short post (thuộc blog — xem §5.2)
    → Không full question list (tease 2-3 trong CONTAINS, full list thuộc blog)
```

### §4.2 — Format Groups

```
  NHÓM A: TEXT POST (Reddit subs, LessWrong, EA Forum)
    → Full body as post text
    → Title = descriptive statement (KHÔNG question-first)
    → Follow core structure §4.1
    → ~250-400 words tùy platform

  NHÓM B: LINK + AUTHOR COMMENT (Hacker News, Lobsters)
    → Submit blog URL as link
    → Post body = KHÔNG CÓ (HN/Lobsters = link aggregator)
    → Author comment đầu tiên = condensed core structure §4.1
    → Title: blog title hoặc "Show HN: [description]"
    → ⚠️ HN KHÔNG phải text post platform — format phải đúng
    → Author comment ~150-250 words

  NHÓM C: MICRO-THREAD (Bluesky 300 chars, Mastodon 500 chars)
    → Thread 3-5 posts:
      Post 1: WHAT + CONTAINS (condensed)
      Post 2: POSITION + MECHANISM TEASE
      Post 3: EPISTEMIC + LINKS
      Post 4: CLOSE (+ hashtags)
    → Hashtags: #Neuroscience #CogSci #OpenScience
    → CamelCase hashtags (accessibility — đặc biệt Mastodon)
```

### §4.3 — Platform-Specific Adjustments (NHẸ)

```
  Adjustments = tinh chỉnh câu chữ, KHÔNG phải rewrite.
  Core message GIỐNG NHAU. Chỉ sửa:

  LESSWRONG:
    → Thêm [Epistemic status: hypothesis inviting falsification] ở đầu
    → Mechanism tease: compiled vs fresh (rationalist-relevant, Kahneman reframe)
    → Có thể dài hơn (~350-400 words — LW accepts long-form)

  r/SLATESTARCODEX:
    → Giống LW, thêm nhẹ: psychiatry/neuroscience angle
    → SSC readers biết Kahneman, predictive processing

  EA FORUM:
    → Giống LW, thêm nhẹ: human cognition → AI safety angle
    → "Understanding human reward system → better AI alignment"

  HACKER NEWS:
    → Format B: submit blog link + author comment
    → "Show HN:" prefix
    → Author comment condensed (~200 words)
    → Tech vocabulary: "codebase", "open-source", "CC0"

  LOBSTERS:
    → Format B: submit blog link (invite-only)
    → Không cần separate short post

  r/COGSCI:
    → Citations prominent hơn trong mechanism tease
    → Mechanism tease: social cluster (Eisenberger 2003, Coan 2015)

  r/PSYCHOLOGY:
    → Accessible language
    → Mechanism tease: limerence (Fisher 2004 — relatable)
    → Tránh jargon (PFC → "prefrontal cortex", etc.)

  r/MACHINELEARNING:
    → [D] Discussion tag
    → Mechanism tease: prediction error ≠ reward, dopamine × RL
    → Technical ML terminology: reward shaping, curiosity-driven learning
    → Connect framework → existing ML concepts

  BLUESKY + MASTODON:
    → Format C: micro-thread
    → Academic tone (neuroscientists đã migrate tới Bluesky)
    → Bluesky: 300 chars/post, Mastodon: 500 chars/post
```

---

## §5 — CONTENT MAPPING: V3 → BLOG + SHORT POSTS

### §5.1 — V3 → Blog

```
  V3 SECTION                    BLOG ACTION              NOTES
  ───────────────────────────────────────────────────────────────
  Title + Epistemic             KEEP nguyên              Chốt rồi
  Hook (2 paragraphs)           KEEP + slight expand     +1-2 câu optional
  Questions (11)                KEEP nguyên              Ordering giữ
  Bridge paragraph              KEEP nguyên
  ① Social media sketch         EXPAND ~250 words        +ví dụ, +nuance
  ⑥ Expert decisions sketch     EXPAND ~250 words        +cross-domain examples
  ⑦ Limerence sketch            EXPAND ~250 words        +Resonance Decline
  ③ Always active sketch        EXPAND ~100 words        +contrast detail
  ④ Status sketch               EXPAND ~100 words        +human complexity
  ⑤ Creative stress sketch      EXPAND ~100 words        +when harmful
  Cluster explanation           NEW ~250 words           Reveal "one fact" summary
  Summary section               NEW ~120 words           Following neuro pattern
  Framework description         KEEP nguyên
  Divergences (4)               KEEP nguyên
  Limitations (5)               KEEP nguyên
  CTA                           EXPAND ~300 words        +full AI starter prompt
  Footer                        KEEP + update            +tech blog self-link
```

### §5.2 — V3 → Short Posts

```
  V3 CONTENT USED IN SHORT POSTS (xem §4.1 — core structure):
    → Substance description: đây là gì (1-2 câu — KHÔNG feature list)
    → Content scope: 11 questions, 6 sketches, citations (2-3 câu)
    → Core position: body first, PFC second (1 câu)
    → 1 mechanism tease (from sketch ①, ⑥, or ⑦ — 2-3 câu)
    → Epistemic status (1 câu)
    → Links (blog + GitHub)
    → Close: invitation to challenge (1-2 câu)

  V3 CONTENT NOT IN SHORT POSTS:
    → Tất cả mechanism sketches (→ blog)
    → Full divergences list (→ blog)
    → Cluster explanation (→ blog)
    → Detailed question list (→ blog — short posts tease 2-3, không list 11)
    → Limitations (→ blog)
    → AI starter prompt (→ blog)

  THAY ĐỔI SO VỚI V0.1:
    → BỎ: question-hook opening (gây lệch pha: question cục bộ ↔ blog toàn diện)
    → BỎ: "I built..." opener (self-promotional)
    → BỎ: divergences paragraph trong short post (thuộc blog)
    → THÊM: substance description (đây là gì, chứa gì)
    → THÊM: epistemic status explicit
    → Lý do: overview blog = broad, short post phải set đúng expectation
```

### §5.3 — Cluster handling

```
  IN SHORT POSTS:
    → KHÔNG có cluster. Quá dài cho 300-word post.
    → Có thể tease 1 câu: "The framework also identifies why 5 seemingly
      unrelated social experiences trace to one architectural fact."

  IN BLOG:
    → Questions section: cluster GIỮA nguyên (5 sub-questions + tease closing)
    → NEW section ⑥: "The Cluster Explained" — reveal "one fact" ở summary level
    → KHÔNG deep-dive — link source files (Connection.md, Inter-Body-Mechanism.md)
    → Reader journey: see questions → "they're connected?" → read explanation →
      "I want to understand the full mechanism" → clicks source files

  IN GITHUB:
    → Full mechanism in Connection.md v5.0, Inter-Body-Mechanism.md §1
```

---

## §6 — QUALITY GUIDELINES

### §6.1 — Blog length principle

```
  "ĐỦ ĐỂ THẤY SUBSTANCE, KHÔNG LAN MAN LÀM MẤT HỨNG ĐỌC"

  TARGET: 3,000-3,500 words (~14-16 phút đọc)
  SO SÁNH:
    Neuro blogs: 5,000-6,000 words (deep-dive 1 mechanism → dài hơn hợp lý)
    Tech blog: overview nhiều mechanism → mỗi cái ngắn hơn → tổng vừa phải

  RULE: Mỗi paragraph phải earn its place.
    → Đọc lại paragraph. Bỏ đi → reader mất gì?
    → Nếu mất = nothing → cắt.
    → Nếu mất = important context → giữ.

  MECHANISM SKETCH LENGTH:
    Expanded: ~250 words MAX. Enough to show mechanism, not enough to explain fully.
    Brief: ~100 words MAX. Core insight + 1 surprising implication + source.
    Cluster explanation: ~250 words MAX. Summary level only.
```

### §6.2 — Tone

```
  BLOG:
    = Engineer presenting system architecture
    = "The framework identifies..." (not "I discovered...")
    = "This produces..." (not "You feel...")
    = Mechanism-first, experience-second
    = Mỗi sketch kết thúc bằng *Source + Research citation*

  SHORT POSTS:
    = 1 core message, adapt FORMAT (not content) per platform
    = Substance description: đây là gì, chứa gì (not question-hook, not feature list)
    = Na ná giữa các platforms (mục đích = distribution, không differentiation)
    = Tinh chỉnh nhẹ per platform group: format, mechanism tease, câu chữ
    = ALL share: no hype, no guru, no marketing
    = Close with invitation to falsify, not to confirm
    = KHÔNG question-hook (gây lệch pha giữa post cục bộ và blog toàn diện)
    = KHÔNG feature list opening ("200+ files, structured like..." = anti-pattern §6.3)
```

### §6.3 — Anti-patterns (originally from plan-tech-post.md §7, now absorbed here)

```
  ✗ Feature listing: "Framework has 200+ files, covers X Y Z..." → boring
  ✗ Grand claim: "Comprehensive theory of the human brain" → grandiose
  ✗ Self-help: "Understanding this framework will help you..." → W.4 violation
  ✗ Marketing: "Star the repo" / "Share this post" → push, not pull
  ✗ Too much detail per-mechanism: deep-dive thuộc về source files, không phải blog
  ✗ Criticism opener: "Products are built on wrong science" → defensive
  ✗ Overexplaining cluster: if cluster explanation > 250 words → đang deep-dive, CẮT
```

### §6.4 — W.4 checkpoint (per sketch)

```
  TEST: Đọc sketch. Nếu đọc giống Psychology Today → REWRITE.

  ⑦ Limerence sketch = HIGHEST RISK:
    ✓ "The framework predicts WHY limerence ends" → mechanism = OK
    ✗ "4 tips for lasting love" → advice = W.4 VIOLATION
    ✓ Kết thúc bằng mechanism distinction ("boring ≠ stopped loving") = OK
    ✗ Kết thúc bằng prescription ("so you should do X") = W.4 VIOLATION

  CHECK EVERY SKETCH: "The framework identifies..." / "The mechanism predicts..."
  NEVER: "You should..." / "This means you need to..." / "Try doing..."
```

---

## §7 — IMPLEMENTATION PHASES

```
  PHASE 1: WRITE BLOG                                     [MAIN WORK]
    Input: tech-post-draft-v3.md + drill-tech-post-v2.md
    Output: docs/_posts/YYYY-MM-DD-bridging-neuroscience-psychology.md
    Steps:
      1a. Start from v3 content
      1b. Add Summary section (following neuro blog pattern)
      1c. Expand mechanism sketches (using drill mechanism chains)
      1d. Write Cluster Explained section (using drill §1.2)
      1e. Expand Getting Started / CTA (add full AI starter prompt)
      1f. Quality check: W.4, tone, flow, word count
      1g. Verify all research citations match drill sources

  PHASE 2: WRITE SHORT POSTS
    Input: blog (completed) + short-posts-dopamine.md (template)
    Output: Public-Plan/blog/short-post-overview.md
    Steps:
      2a. LW version first (primary target)
      2b. HN version
      2c. Reddit r/cogsci version
      2d. Reddit r/psychology version
      2e. Include posting rules + cadence (from short-posts-dopamine.md pattern)

  PHASE 3: DEPLOY
    3a. Blog → commit to docs/_posts/ → GitHub Pages auto-deploy
    3b. Verify blog URL live
    3c. Update tech-post-draft-v3.md footer → add tech blog link
    3d. Update neuro blog footers → add tech blog link (cross-promotion)

  PHASE 4: POST SHORT POSTS
    Following plan-neuro-posts.md cadence:
    4a. LessWrong first (primary stress-test)
    4b. Wait 3-5 days → gauge engagement → refine
    4c. HN second
    4d. Reddit tiers after HN feedback
    4e. NEVER post multiple platforms same day
```

---

## §8 — KEY DECISIONS (đã chốt)

```
  ✅ Title: "A concept bridging neuroscience and psychology into a connected model
     — estimating the direction of human drive"
  ✅ Hook: Version A (WHAT-first, direct engineer tone)
  ✅ Questions: 7 items (6 single + 1 cluster with 5 sub-questions)
  ✅ Question ordering: ①③④⑤⑥⑦ (singles) → ② cluster (cuối)
  ✅ Sketch allocation: 3 expanded (①⑥⑦) + 3 brief (③④⑤)
  ✅ Cluster: giữ "hardware subsidy" jargon trong question ⑦
  ✅ Cluster in blog: reveal "one fact" ở summary level (NEW section)
  ✅ Pattern: blog + short posts (giống 3 neuro blogs)
  ✅ Audience: tech experts (highest-potential)
```

---

## §9 — SUCCESS SIGNALS (originally from plan-tech-post.md §8, now absorbed here)

```
  ✓ GOOD:
    → Comments asking about specific mechanisms
    → Counter-evidence: "Research Z says the opposite" = HIGH-QUALITY
    → Domain experts engage (not just tech)
    → GitHub: issues / discussions / forks
    → Blog traffic from short post > 10% click-through

  ✗ BAD:
    → Completely ignored → framing problem
    → Only "cool!" comments → consumption, not verification
    → Self-help community picks it up → W.4 failure
    → Stars without engagement → vanity metric
```

---

## §10 — REFERENCES

```
  DRILL (mechanism analysis):
    drill-tech-post-v2.md — 7 question drills, mechanism chains, formulations, audience

  CURRENT DRAFT:
    tech-post-draft-v3.md — ~1,750 words, foundation cho blog (expand từ đây)

  STRATEGY:
    Tech/backup/plan-tech-post.md — Angle E, question pool, hooks (BACKED UP — key content absorbed in §6, §9)
    plan-neuro-posts.md — 2-tier pattern (blog + short posts), posting cadence

  TEMPLATES:
    short-posts-dopamine.md — short post format per-platform
    docs/_posts/2026-05-31-dopamine-signals-salience-not-reward.md — blog format

  FRAMEWORK SOURCES (for expanding mechanism sketches):
    Connection.md v5.0 — 8 pathways, social pain, co-regulation
    Body-Knowing.md v1.0 — compiled chunks, cost ≈ 0, 3 directions
    Love-Romantic.md v3.0 — limerence §9, transition §10, bonding §11
    Bond-Architecture.md v2.0 — Resonance Decline: 2 Forces + 1 Fuel
    Inter-Body-Mechanism.md — Compilable Architecture, social = requirement
    Boredom.md v2.1 — 6 sources, compilable idle = dissonance
    Status.md v2.2 — Resource Access Map
    Cortisol-Baseline.md v2.1 — amplifier not cause, Inverted-U
    Core-Software.md v3.0 — cycle never stops
```
