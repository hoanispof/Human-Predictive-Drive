# Plan: Logic-Feeling Blog Distribution — Phân Phối Blog Logic-Feeling

> **Mục tiêu:** Đưa blog "Logic Is Not the Opposite of Intuition" tới các cộng đồng
> phù hợp nhất để stress-test claim và thu hút expert verification.
> **Đặc thù:** Blog này CHALLENGE IDENTITY của target audience (rationalists, tech experts
> tự nhận "logical thinker") → framing phải đặc biệt cẩn thận.
> **Nguyên tắc:** Hypothesis inviting falsification. Không marketing, không self-help.
> **Trạng thái:** DRAFT v0.1
> **Ngày tạo:** 2026-06-04
> **Blog file:** docs/_posts/2026-06-04-logic-is-not-the-opposite-of-intuition.md
> **Blog URL:** https://hoanispof.github.io/Human-Predictive-Drive/blog/logic-is-not-the-opposite-of-intuition/
> **Liên kết:**
>   plan-logic-feeling-blog.md — blog content structure + quality guidelines
>   plan-overview-distribution.md — overview blog distribution (tham chiếu pattern)
>   Drill-Logic-Feeling-Blog.md — research verification, objections, tone calibration
>   framing-engagement-value.md — 3-layer value model, W.4 rules
>   short-post-overview.md — overview blog short posts (format reference)

---

## §0 — TẠI SAO PLAN RIÊNG CHO BLOG NÀY

### 0.1 — Blog Này Khác Overview Blog + 3 Neuro Blogs

```
  OVERVIEW BLOG: giới thiệu framework TỔNG QUAN → audience rộng
  3 NEURO BLOGS: challenge 1 claim cụ thể (dopamine, cortisol, ADHD) → domain experts
  BLOG NÀY: challenge perception CỦA CHÍNH AUDIENCE → identity-threatening

  TẠI SAO IDENTITY-THREATENING:
    ① LessWrong tự định nghĩa bằng "rationality"
    ② HN engineers tự định nghĩa bằng "logical thinking"
    ③ Blog nói: "logic compiled của bạn cũng là Body-Knowing,
       cùng mechanism với intuition"
    → Provocation mạnh nhất trong tất cả blog
    → Engagement tiềm năng CAO NHẤT — nhưng risk cũng CAO NHẤT

  KEY DIFFERENCE VỚI OVERVIEW DISTRIBUTION:
    ① Audience HẸP hơn (rationalist + cogsci + philosophy of mind)
    ② Risk CAO hơn (identity challenge → defensive reaction)
    ③ Framing CRITICAL hơn (must NOT read as anti-rationalist)
    ④ Một số platforms KHÔNG phù hợp (Lobsters, r/ML, Alignment Forum)
    ⑤ Một số platforms MỚI phù hợp hơn (ACX Open Thread, LinkedIn, r/AcademicPsychology)
```

### 0.2 — Vị Trí Trong Chiến Lược Tổng Thể

```
  THỨ TỰ PUBLISH:
    3 neuro blogs → overview blog → [BLOG NÀY] → short posts
    (Overview giới thiệu compiled vs fresh →
     blog này deep-dive → reader đã có context)

  BLOG NÀY LÀ DEEP-DIVE THỨ 4:
    Blog 1: Dopamine ≠ reward (neuro)
    Blog 2: Cortisol ≠ stress (neuro)
    Blog 3: ADHD ≠ attention deficit (neuro)
    Blog 4: Logic ≠ opposite of intuition ← BLOG NÀY (PFC/cognitive)

  FOOTER LINKS (phải live trước khi publish):
    → Dopamine blog, Cortisol blog, ADHD blog, Overview blog
```

---

## §1 — PLATFORM MAP: Tất Cả Platforms Cho Blog Này

### 1.1 — Platform Priority Matrix

```
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║ TIER S — STRESS-TEST ĐẦU TIÊN (expert engagement, chất lượng cao nhất) ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                         ║
  ║ ① LessWrong                                                             ║
  ║   Size: ~50K active                                                     ║
  ║   Audience: rationalist, Bayesian, cognitive science, dual-process aware ║
  ║   Fit: EXCELLENT — đã có wiki tag "dual-process theory" + existing      ║
  ║        posts critique System 1/2 framing → topic quen thuộc             ║
  ║   Posting rules: 5+ karma để post tự do; <5 karma = max 2 posts/tuần   ║
  ║   Format: long-form essay (4000+ words ok, audience đọc sâu)            ║
  ║   Risk: "anti-rationalist" alarm → defensive rejection trước khi đọc    ║
  ║   Tại sao ĐẦU TIÊN: hardest audience = best stress-test                ║
  ║   ⚠️ PHẢI address Evans & Stanovich — audience biết dual-process        ║
  ║                                                                         ║
  ║ ② r/slatestarcodex (~90K+)                                              ║
  ║   Audience: intellectual long-form, cross-domain, psychiatry-aware       ║
  ║   Fit: VERY GOOD — SSC audience quen Kahneman, Klein, predictive       ║
  ║        processing. Long-form cognitive science = natural fit.            ║
  ║   Format: discussion post + blog link (2000+ words ok)                  ║
  ║   Risk: có thể bị bury nếu hook không engaging                         ║
  ║                                                                         ║
  ║ ③ ACX Open Thread (Astral Codex Ten)                             [MỚI]  ║
  ║   URL: https://www.astralcodexten.com/ (Open Thread ~weekly, #436+)     ║
  ║   Audience: = LW + r/SSC overlap, intellectual generalists              ║
  ║   Fit: GOOD — free access to ideal audience qua comment                 ║
  ║   Format: comment (~150-200 words) + blog link                          ║
  ║   Risk: rất thấp (comment, không phải post riêng)                      ║
  ║   ⚠️ Không thể guest-post — chỉ comment trong Open Thread              ║
  ║                                                                         ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║ TIER A — SAU KHI TIER S ĐÃ STRESS-TEST                                 ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                         ║
  ║ ④ Hacker News (~500K daily)                                              ║
  ║   Audience: tech-intellectual, engineering mindset                       ║
  ║   Fit: STRONG — cogsci posts citing Kahneman thường xuyên lên frontpage ║
  ║   Format: submit blog LINK trực tiếp (KHÔNG "Show HN:" — chỉ cho       ║
  ║           runnable projects). Title = blog title, factual.               ║
  ║   Risk: TRUNG (frontpage → 300K views → kiểm soát khó)                 ║
  ║   ⚠️ Post WEEKDAY (weekend traffic thấp)                                ║
  ║   ⚠️ Respond comments NHANH trong 2h đầu (algorithm boost)             ║
  ║                                                                         ║
  ║ ⑤ r/cogsci (~129K)                                                      ║
  ║   Audience: cognitive science, bridge tech + neuro + philosophy          ║
  ║   Fit: GOOD — dual-process theory reframe = on-topic                    ║
  ║   Format: discussion post + blog link, academic-accessible tone         ║
  ║   Risk: thấp nhưng thiếu citations = bị dismiss                        ║
  ║   ⚠️ Cần academic tone + explicit research citations                    ║
  ║                                                                         ║
  ║ ⑥ Bluesky                                                               ║
  ║   Size: 43M+ registered, 1.5-3M DAU (2026)                             ║
  ║   Audience: 20,000+ neuroscientists đã migrate từ X/Twitter              ║
  ║   Fit: EXCELLENT — neuroscience community ĐÃ Ở ĐÂY                     ║
  ║   Format: 300 chars/post × 4-5 post thread + blog link                  ║
  ║   Risk: thấp (academic tone, neuroscience-native)                       ║
  ║   Hashtags: #neuroscience #CognitiveScience #psychology #decisionmaking  ║
  ║   ⚠️ Build presence nhẹ trước (follow neuro starter packs)              ║
  ║                                                                         ║
  ║ ⑦ LinkedIn                                                       [MỚI]  ║
  ║   Audience: tech leaders, decision-makers, engineering managers          ║
  ║   Fit: STRONG — decision-making topic appeals to tech leaders            ║
  ║        Long-form articles get 3x views vs external links.               ║
  ║        Dwell-time = primary algorithm signal (2026).                     ║
  ║   Format: shortened article (1,900-2,200 words) HOẶC newsletter         ║
  ║   Risk: thấp (professional context, không identity-threatening)         ║
  ║   ⚠️ Cần SHORTENED VERSION — full 4,600 words quá dài                  ║
  ║   ⚠️ Frame: "decision-making under uncertainty", KHÔNG pure cogsci      ║
  ║                                                                         ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║ TIER B — SAU KHI CÓ TRACTION                                            ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                         ║
  ║ ⑧ EA Forum                                                              ║
  ║   Audience: rationalist, researchers, AI safety adjacent                ║
  ║   Fit: MODERATE — cần connect tới EA-relevant outcomes                  ║
  ║   Format: long-form essay, LLM-generated content phải disclose          ║
  ║   ⚠️ Frame: "how cognitive architecture affects rationalist decisions"  ║
  ║                                                                         ║
  ║ ⑨ r/psychology (~1.5M+)                                                 ║
  ║   Audience: broader, less technical                                     ║
  ║   Fit: MODERATE — accessible framing needed                             ║
  ║   Format: discussion post + blog link                                   ║
  ║                                                                         ║
  ║ ⑩ r/AcademicPsychology (~200K)                                   [MỚI]  ║
  ║   Audience: academic psychology, research-focused                       ║
  ║   Fit: MODERATE — frame as theoretical discussion, not promotion        ║
  ║   Format: discussion post                                               ║
  ║   ⚠️ Cần participation history trước khi post                          ║
  ║                                                                         ║
  ║ ⑪ Substack (cognitive science newsletters)                        [MỚI]  ║
  ║   Targets: Tommy Blanchard, Nature-Nurture-Nietzsche                    ║
  ║            (Steve Stewart-Williams), Extended Brain                      ║
  ║   Fit: GOOD cho engagement — guest-post/comment trên established        ║
  ║        newsletters. Building own Substack from zero = slow.             ║
  ║   Format: engagement qua comments + Substack Notes                      ║
  ║                                                                         ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║ TIER C — DÀI HẠN (infrastructure + passive discovery)                    ║
  ╠═══════════════════════════════════════════════════════════════════════════╣
  ║                                                                         ║
  ║ ⑫ ResearchGate                                                          ║
  ║   Register as "Independent Researcher" (no affiliation required).       ║
  ║   Upload blog as preprint. Zero friction. Recommendation engine push.   ║
  ║                                                                         ║
  ║ ⑬ Academia.edu                                                          ║
  ║   independent.academia.edu supports independent researchers.            ║
  ║   Good search indexing → organic discovery.                             ║
  ║                                                                         ║
  ║ ⑭ Discord servers                                                       ║
  ║   Theoretical Neuroscience Discord, Cognitive Sciences Discord.          ║
  ║   ⚠️ Lurk 1-2 tuần, contribute value TRƯỚC khi share                   ║
  ║                                                                         ║
  ║ ⑮ Medium                                                                ║
  ║   Tốt nếu publish trong relevant publication.                           ║
  ║   Contrarian evidence-based style được algorithm reward (2026).          ║
  ║   ⚠️ Low priority — chỉ nếu có relevant publication mời                ║
  ║                                                                         ║
  ║ ⑯ CogSci Stack Exchange                                                 ║
  ║   Activity thấp (<5 questions/day). Chỉ TRẢ LỜI câu hỏi có sẵn        ║
  ║   về dual-process theory, link blog trong answer.                       ║
  ║                                                                         ║
  ╚═══════════════════════════════════════════════════════════════════════════╝
```

### 1.2 — Platforms SKIP (khác với overview blog distribution)

```
  ┌───────────────────────────────────────────────────────────────────────┐
  │ PLATFORM               │ LÝ DO SKIP                                  │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Lobsters               │ Không có cognitive science tag. Computing-   │
  │                        │ only. Off-topic → sẽ bị xóa.               │
  ├───────────────────────────────────────────────────────────────────────┤
  │ r/MachineLearning      │ Off-topic: blog không có ML connection       │
  │                        │ trực tiếp. r/ML focus papers + benchmarks.  │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Alignment Forum        │ Invite-only, AI-safety only.                │
  │                        │ Non-AI cogsci không pass review.            │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Twitter/X              │ Academic community ĐÃ EVACUATED sang        │
  │                        │ Bluesky (arXiv paper May 2025 documents).   │
  ├───────────────────────────────────────────────────────────────────────┤
  │ r/philosophy           │ Rules cực strict. Non-academic original      │
  │                        │ frameworks thường bị xóa.                   │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Metaculus              │ Prediction questions only, không cho essays. │
  ├───────────────────────────────────────────────────────────────────────┤
  │ OSF Preprints          │ SUSPENDED nhận submissions từ Aug 2025.      │
  │                        │ Dùng PsyArXiv hoặc ResearchGate thay thế.  │
  ├───────────────────────────────────────────────────────────────────────┤
  │ r/neuroscience         │ THẤP cho blog này: focus neuro domain       │
  │                        │ (đã có 3 neuro blogs). Blog này = PFC/      │
  │                        │ cognitive, phù hợp r/cogsci hơn.           │
  ├───────────────────────────────────────────────────────────────────────┤
  │ r/PhilosophyofMind     │ Nhỏ, moderate fit. Có thể thử nhưng        │
  │                        │ priority thấp. Không tạo short post riêng.  │
  └───────────────────────────────────────────────────────────────────────┘

  MANIFOLD MARKETS: CÓ THỂ dùng cho prediction question
    VD: "Will compilation-level predict decision quality better than
    content-type by 2030?"
    → Creative engagement tool, không phải primary distribution.
    → Optional. Chỉ làm nếu có thời gian.
```

---

## §2 — FRAMING + TONE: Strategy Per-Platform

> **Core challenge:** Blog nói "logic của bạn cũng là Body-Knowing."
> Audience rationalist/tech tự nhận "logical."
> → PHẢI frame thành "this DEEPENS your understanding of rationality"
> → KHÔNG ĐƯỢC frame thành "you think you're logical, but you're not"

### 2.1 — ① LessWrong — Rationalist Tone

```
  AUDIENCE PROFILE:
    → Biết Kahneman System 1/2
    → Biết Evans & Stanovich (một số)
    → Tự identify là "rationalist"
    → Value: Bayesian reasoning, falsification, epistemic status
    → Red flags: guru tone, overclaim, anti-rationalist framing

  HOOK STRATEGY:
    → Lead with Evans & Stanovich address — shows homework done
    → System 1/2 reframe = topic họ đã nghĩ về
    → Einstein + Hadamard = interesting anecdote (not proof — say so)
    → "Compilation level as the key variable" = technical enough cho audience

  FRAMING RULES:
    ✓ "This reframes what separates S1/S2 — compilation stage, not mechanism type"
    ✓ "If anything, this framework is PRO-expertise and PRO-verification"
    ✓ "Here are 4 conditions that would prove us wrong"
    ✓ "🟡 Framework synthesis — not proven, seeking stress-test"
    ✗ "You think you're logical, but actually..."
    ✗ "Science has been wrong about rationality..."
    ✗ "Trust your gut instead of logic"

  TONE:
    → Assert confidently where evidence is strong (Tier 1 citations)
    → Qualify explicitly where evidence is limited (🟡 synthesis)
    → Use tech analogies: compiled code vs interpreted code
    → Acknowledge limitations of each study
    → Invite falsification as CHALLENGE, not disclaimer

  TARGET REACTION:
    "Huh, interesting reframe. Let me check the citations."
    "I can see how this is consistent with Klein and Kahneman..."
    "But what about Evans & Stanovich?" → (we addressed it)

  ESTIMATED WORD COUNT: ~400 words (short post) → blog link
  FORMAT: Short post text + full blog link
```

### 2.2 — ② r/slatestarcodex — Intellectual Depth

```
  AUDIENCE PROFILE:
    → Overlap LW nhưng broader intellectual interests
    → Quen Scott Alexander's long-form style
    → Biết Kahneman, psychiatry, cross-domain synthesis
    → Value: intellectual curiosity, nuance, long arguments

  HOOK STRATEGY:
    → "Compiled expertise IS what rationalists call good reasoning"
    → Cross-domain synthesis angle: same mechanism in math, medicine, coding
    → Senior dev + therapist parallel = vivid, recognizable

  FRAMING RULES:
    ✓ "Cross-domain synthesis — same mechanism, different labels"
    ✓ Acknowledge complexity, show multiple angles
    ✓ PFC = Lawyer examples (tech stack choice, hiring decisions)
    ✗ Reductive framing ("it's all just one thing")
    ✗ Dismissive of existing frameworks

  TONE:
    → Intellectual exploration, not proclamation
    → "Here's what we found, and here's what could break it"
    → Longer hook than LW (this audience reads more)

  ESTIMATED WORD COUNT: ~350 words (short post) → blog link
```

### 2.3 — ③ ACX Open Thread — Brief Hook

```
  AUDIENCE PROFILE:
    → = LW + r/SSC overlap
    → Browsing Open Thread casually

  FRAMING:
    → Very brief: 150-200 words max
    → 1 key insight + 1 surprising claim + blog link
    → Casual but intellectual tone
    → "Wrote a deep-dive on X. TL;DR: Y. Full argument: [link].
       Where does it break?"

  ESTIMATED WORD COUNT: ~150-200 words (comment)
```

### 2.4 — ④ Hacker News — Tech-Native Dry

```
  AUDIENCE PROFILE:
    → Engineers, tech leaders, startup founders
    → Value: substance, technical depth, no BS
    → Red flags: clickbait, self-promotion, marketing language
    → Know Kahneman from pop science (less technical than LW)

  HOOK STRATEGY:
    → Senior dev "sees" bug = compiled processing (THEY LIVE THIS)
    → Tech stack holy wars = PFC lawyering (they'll laugh and nod)
    → "Structured like a codebase" angle for framework
    → CC0 + open-source = HN values

  FRAMING RULES:
    ✓ Lead with tech-native example (senior dev)
    ✓ "Compiled vs Fresh" maps to compiled code vs interpreted code
    ✓ Factual title — HN editors WILL change clickbait titles
    ✓ Open-source, CC0 — tech values
    ✗ "Show HN:" prefix (NOT a runnable project)
    ✗ Marketing language, "star the repo"
    ✗ Self-help framing

  TONE:
    → Dry, factual, evidence-first
    → Let the argument speak
    → No enthusiasm markers ("amazing!", "groundbreaking!")

  ESTIMATED WORD COUNT: submit blog link directly
  TITLE: blog title as-is (factual, not clickbait)
  RESPONDING: reply comments FAST trong 2h đầu (algorithm boost)
```

### 2.5 — ⑤ r/cogsci — Academic Bridge

```
  AUDIENCE PROFILE:
    → Cognitive scientists, grad students, interdisciplinary researchers
    → KNOW dual-process theory literature
    → Value: citations, methodology, acknowledged limitations
    → Red flags: pop science oversimplification, missing citations

  HOOK STRATEGY:
    → "Compilation stage vs mechanism type — a proposed reframe"
    → Cite Evans & Stanovich 2013 directly
    → Learning trajectory evidence (Schneider & Shiffrin 1977, Logan 1988)
    → Shareability insight as novel contribution

  FRAMING RULES:
    ✓ Academic-accessible (not full jargon, but cite everything)
    ✓ "Proposed reframe" — not "we proved"
    ✓ Epistemic status upfront
    ✓ "Seeking domain expert review"
    ✗ Pop science shorthand ("System 1 = fast")
    ✗ Dropping citations → immediate credibility loss

  TONE:
    → Academic-accessible: clear prose, full citations
    → Humble but specific
    → "Here's the evidence. Here's what we synthesize. Here's what could break it."

  ESTIMATED WORD COUNT: ~300 words (short post) → blog link
```

### 2.6 — ⑥ Bluesky — Micro-Thread

```
  AUDIENCE PROFILE:
    → 20,000+ neuroscientists migrated from X/Twitter
    → Academic, research-active
    → Dùng threads cho content dài

  HOOK STRATEGY:
    → Thread 4-5 posts, mỗi post = 1 key insight
    → Post 1: Hook ("Logic and intuition — same mechanism?")
    → Post 2: Evidence snapshot (Klein, Chase & Simon)
    → Post 3: Shareability insight (why observer sees 2 modes)
    → Post 4: PFC = Lawyer (1 vivid example)
    → Post 5: Blog link + "Find where it breaks"

  FRAMING RULES:
    ✓ Academic tone — neuroscientists ARE the audience
    ✓ Each post = standalone insight (readers may not read full thread)
    ✓ Hashtags: #neuroscience #CognitiveScience #DualProcess
    ✗ Pop science oversimplification
    ✗ Thread quá dài (>6 posts = lost readers)

  CHAR LIMIT: 300 chars/post
  ESTIMATED: 5 posts × 250-300 chars
```

### 2.7 — ⑦ LinkedIn — Decision-Making Professional

```
  AUDIENCE PROFILE:
    → Tech leaders, engineering managers, product managers
    → Quan tâm: decision-making, leadership, expertise development
    → Value: actionable insight, professional relevance
    → Read long-form if topic relevant to work

  HOOK STRATEGY:
    → "Why your best decisions probably aren't as 'logical' as you think"
    → Decision-making under uncertainty angle
    → Expert vs novice — relevant cho hiring, tech leadership, strategy
    → PFC = Lawyer examples: hiring decisions, tech stack choices

  FRAMING RULES:
    ✓ Professional framing — "understanding decision-making better"
    ✓ "Expert compiled patterns" = what makes senior engineers valuable
    ✓ Actionable insight: "domain feedback is the only arbiter"
    ✗ Pure academic jargon (Body-Knowing, PFC, etc.)
    ✗ Anti-rational framing
    ✗ Self-help ("this will change how you decide")

  TONE:
    → Professional but intellectually honest
    → Slightly warmer than LW/HN (LinkedIn norm)
    → Evidence-backed but accessible

  FORMAT: SHORTENED article (1,900-2,200 words)
    → Cut: Evans & Stanovich detailed response, some citations
    → Keep: senior dev example, PFC = Lawyer, domain feedback arbiter,
            falsification criteria (shows intellectual honesty)
    → Add: more workplace examples (hiring, strategy, tech stack)

  ESTIMATED WORD COUNT: 1,900-2,200 (shortened from 4,600)
```

### 2.8 — ⑧ EA Forum — Decision-Improvement

```
  AUDIENCE PROFILE:
    → Rationalist, researchers, AI safety adjacent
    → Overlap LW nhưng focus "making the world better"
    → Value: actionable for EA goals, rigorous reasoning

  HOOK STRATEGY:
    → "How cognitive architecture affects the quality of rationalist decisions"
    → Connect tới: understanding human bias → better AI alignment,
      better cause prioritization, better personal effectiveness

  FRAMING RULES:
    ✓ Frame: "improving how rationalists understand their own cognition"
    ✓ Connect to EA-relevant outcomes
    ✓ LLM-generated content disclosure (nếu có)
    ✗ Pure cognitive science without EA connection → off-topic
    ✗ Self-promotion without substance

  ESTIMATED WORD COUNT: ~350 words → blog link
```

### 2.9 — ⑨ r/psychology — Accessible

```
  AUDIENCE PROFILE:
    → Broader, less technical than r/cogsci
    → Students, enthusiasts, some professionals
    → Know Kahneman from pop science

  HOOK STRATEGY:
    → "What if logic and intuition aren't opposites?"
    → PFC = Lawyer everyday examples (quit for career growth, car purchase)
    → Accessible language, minimal jargon

  FRAMING RULES:
    ✓ Accessible but not dumbed down
    ✓ Everyday examples readers recognize
    ✓ "Hypothesis inviting testing" (not established fact)
    ✗ Academic jargon overload
    ✗ Pop science oversimplification

  ESTIMATED WORD COUNT: ~250-300 words → blog link
```

### 2.10 — ⑩ r/AcademicPsychology — Academic Discussion

```
  AUDIENCE PROFILE:
    → Academics, grad students, researchers
    → Expect theoretical rigor
    → Self-promotion sensitive

  HOOK STRATEGY:
    → "Theoretical discussion: compilation stage vs mechanism type
       in dual-process theory"
    → Frame as DISCUSSION, not promotion
    → Reference Evans & Stanovich 2013 as starting point

  FRAMING RULES:
    ✓ Frame: "seeking academic feedback on a theoretical argument"
    ✓ Cite all primary sources
    ✓ Acknowledge novelty of synthesis
    ✗ Blog promotion framing
    ✗ Marketing language

  ESTIMATED WORD COUNT: ~300 words (discussion prompt)
  ⚠️ Cần participation history trước khi post
```

---

## §3 — SHORT POST MAP

### 3.1 — Template Grouping Strategy

```
  NGUYÊN TẮC: Nhóm theo tone/audience → base template per nhóm.
  KHÔNG copy-paste 1 bài cho mọi nơi.

  ┌──────────────────────────────────────────────────────────────────────┐
  │ NHÓM           │ PLATFORMS                 │ TONE          │ WORDS  │
  ├──────────────────────────────────────────────────────────────────────┤
  │ ① Rationalist  │ LessWrong (A)             │ Bayesian,     │ ~400   │
  │                │ r/slatestarcodex (B)       │ falsifiable   │ ~350   │
  │                │ EA Forum (C)               │ EA-connected  │ ~350   │
  │                │ ACX Open Thread (D)        │ brief hook    │ ~180   │
  ├──────────────────────────────────────────────────────────────────────┤
  │ ② Tech-native  │ Hacker News               │ dry, factual  │ link   │
  │                │ (submit blog link directly, không short post)       │
  ├──────────────────────────────────────────────────────────────────────┤
  │ ③ Academic     │ r/cogsci (E)              │ academic-     │ ~300   │
  │                │ r/AcademicPsychology (F)   │ accessible    │ ~300   │
  ├──────────────────────────────────────────────────────────────────────┤
  │ ④ Accessible   │ r/psychology (G)          │ accessible,   │ ~280   │
  │                │                            │ everyday      │        │
  ├──────────────────────────────────────────────────────────────────────┤
  │ ⑤ Micro-thread │ Bluesky (H)               │ academic,     │ 5×300  │
  │                │                            │ compressed    │ chars  │
  ├──────────────────────────────────────────────────────────────────────┤
  │ ⑥ Professional │ LinkedIn (I)              │ professional, │ 1,900- │
  │                │                            │ decision-     │ 2,200  │
  │                │                            │ making angle  │ words  │
  └──────────────────────────────────────────────────────────────────────┘

  TỔNG:
    Cần tạo: 9 items (A-I)
    4 rationalist group (A-D) — shared base, adapt tone
    2 academic group (E-F) — shared base, adapt framing
    1 accessible (G) — standalone
    1 micro-thread (H) — standalone format
    1 professional article (I) — shortened version of blog
    + HN = submit blog link trực tiếp (không cần short post)
```

### 3.2 — Hook Ideas Per Platform

```
  ① LW / r/SSC / EA / ACX (Rationalist group):
    HOOK: "Evans & Stanovich define System 1/2 by working memory dependence.
    We agree this is real. We argue it reflects compilation STAGE, not
    mechanism TYPE. The evidence: learning trajectory research shows
    specific skills transition from Type 2 → Type 1 through practice.
    If they were different mechanisms, this shouldn't happen."

    DEMO: "The same chess position that required deliberate analysis from
    Klein's fireground trainees became instant pattern recognition for
    Klein's experienced commanders. Same mechanism, different compilation."

  ② HN:
    HOOK: (title) "Logic Is Not the Opposite of Intuition"
    → Let the blog speak for itself. No editorializing.

  ③ r/cogsci / r/AcademicPsychology (Academic group):
    HOOK: "A proposed reframe of dual-process theory: the Type 1/Type 2
    distinction reflects compilation stage, not mechanism type. Key evidence:
    the controlled-to-automatic transition documented across domains
    (Schneider & Shiffrin 1977, Logan 1988, Anderson 1982, Fitts & Posner 1967).
    Shareability of domain output as the variable determining observer labels."

  ④ r/psychology (Accessible):
    HOOK: "What if 'logic' and 'intuition' aren't two different modes of
    thinking? A senior developer who 'sees' a bug instantly and a therapist
    who 'reads' a patient are doing the same thing: compiled patterns firing
    automatically. We call the first 'technical skill' and the second
    'intuition.' Same mechanism inside — different label outside."

  ⑤ Bluesky (Micro-thread):
    POST 1: "Logic and intuition: same mechanism? Thread 🧵
    Evidence suggests expert 'logic' and expert 'intuition' are both
    compiled body-direct pattern recognition. The label depends on
    domain shareability, not what the brain does."

  ⑥ LinkedIn (Professional):
    HOOK: "The best decision you made last quarter probably wasn't
    as 'logical' as you think. Three independent lines of evidence
    suggest the prefrontal cortex primarily constructs narratives for
    decisions already made — not the other way around. Here's what
    that means for how we think about expertise, hiring, and
    technical leadership."
```

---

## §4 — POSTING CADENCE

```
⚠️ KHÔNG POST TẤT CẢ CÙNG LÚC.

TUẦN 1: Tier S — Stress-test
  → Post LessWrong (Post A)
  → Đợi 3-5 ngày → đọc feedback → refine
  → Post r/slatestarcodex (Post B) + ACX Open Thread comment (Post D)
  → Đợi 3-5 ngày → đọc feedback → refine
  → (EA Forum có thể song song hoặc đợi thêm 1 tuần)

TUẦN 2-3: Tier A — Broaden
  → Refine content từ Tier S feedback
  → Post Hacker News (submit blog link) — WEEKDAY only
  → Đợi 3-5 ngày
  → Post r/cogsci (Post E)
  → Đợi 3-5 ngày
  → Post Bluesky thread (Post H)
  → Post LinkedIn article (Post I) — có thể song song với Bluesky

TUẦN 4-6: Tier B — Expand
  → EA Forum (Post C) — nếu chưa post ở Tuần 1
  → Post r/psychology (Post G)
  → Post r/AcademicPsychology (Post F)
  → Engage Substack newsletters qua comments

TUẦN 6+: Tier C — Long-term
  → Upload ResearchGate + Academia.edu
  → Join + participate Discord servers
  → Trả lời câu hỏi CogSci SE
  → Medium nếu có relevant publication

RULES:
  → Max 1 community post / tuần (không count infrastructure uploads)
  → KHÔNG post multiple subreddits cùng ngày (Reddit spam detection)
  → Đợi feedback trước khi post tiếp
  → Nếu post bị ignore → refine framing, KHÔNG spam lại
  → Nếu post có traction → respond comments → THEN post tiếp
```

---

## §5 — RESPONDING PROTOCOL (Adapted for Identity-Challenge)

```
⚠️ BÀI NÀY CHALLENGE IDENTITY → responding protocol đặc biệt quan trọng.

KHI CÓ "THIS IS ANTI-RATIONALIST" PUSHBACK:
  → "The framework is PRO-expertise and PRO-verification.
     Compiled domain knowledge is the most reliable processing mode.
     Domain feedback is the only arbiter.
     These are deeply rationalist positions.
     What the framework challenges: the HIERARCHY that places 'rational'
     above 'intuitive' as a processing mode — both are partial."
  → KHÔNG: defensive. KHÔNG: "you didn't read carefully."
  → Welcome pushback = credibility signal.

KHI CÓ "YOU'RE CONFLATING SYSTEM 1 AND SYSTEM 2":
  → "We address Evans & Stanovich directly in §4.
     We agree WM dependence is real. We argue it reflects compilation
     STAGE, not mechanism TYPE. The decisive evidence is the transition:
     Schneider & Shiffrin 1977, Logan 1988, Anderson 1982.
     If they were truly different mechanisms, the controlled-to-automatic
     transition through mere practice should not be possible."

KHI CÓ "EXPERT INTUITION ≠ GUT FEELING":
  → "Exactly — that's our point. The MECHANISM is the same (compiled
     patterns firing body-direct). The QUALITY differs based on
     compilation conditions (Kahneman & Klein 2009). Expert intuition
     is compiled on valid domain feedback. Unreliable gut feeling is
     compiled on insufficient or wrong data. Same mechanism,
     different compilation base."

KHI CÓ "LOGIC CAN BE FORMALLY VERIFIED":
  → "That's the shareability insight. Formal verification is possible
     in deterministic domains where Body-Knowing converges.
     'Verifiable' ≠ 'different mechanism.' The mathematician uses
     compiled pattern recognition to navigate the formal system.
     Einstein: 'words sought laboriously in a secondary stage.'"

KHI AI HỎI CREDENTIALS:
  → "Independent researcher. Game developer background.
     Framework is CC0 — test the claims, not the credentials.
     Here's the evidence: [links]"

KHI CÓ SUBSTANTIVE COUNTER-EVIDENCE:
  → Reply trong 24h
  → "Good point. Here's the evidence: [citation]"
  → Nếu counter-evidence mạnh hơn → acknowledge + cập nhật
```

---

## §6 — RISK MANAGEMENT (Blog-Specific)

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ RISK                      │ SEVERITY │ MITIGATION                 │
  ├────────────────────────────────────────────────────────────────────┤
  │ R1: "Crank alarm"         │ CAO      │ Falsification criteria      │
  │   (Title sounds like anti-│          │ upfront. Evans & Stanovich  │
  │    science clickbait)     │          │ addressed explicitly.       │
  │                           │          │ Epistemic status clear.     │
  ├────────────────────────────────────────────────────────────────────┤
  │ R2: "Anti-rationalist"    │ CAO      │ Blog says "PRO-expertise,   │
  │   (LW/HN interpret as    │          │ PRO-verification." Explicit  │
  │    attack on rationality) │          │ "we do not claim" list.     │
  │                           │          │ PFC has genuine processing.  │
  ├────────────────────────────────────────────────────────────────────┤
  │ R3: Defensive reaction    │ CAO      │ Tone: "here's what we found"│
  │   (identity-threatening   │          │ not "you're wrong."         │
  │    → dismiss before read) │          │ Tech analogies as bridge.    │
  │                           │          │ Compiled code analogy.       │
  ├────────────────────────────────────────────────────────────────────┤
  │ R4: "Trust your gut"      │ TRUNG    │ Blog explicitly says:       │
  │   misinterpretation       │          │ "gut can be Self-Referencing.│
  │   (opposite of intended)  │          │ Neither can verify itself."  │
  ├────────────────────────────────────────────────────────────────────┤
  │ R5: Self-help pickup      │ TRUNG    │ W.4 strict. No prescriptions│
  │   (blog used as "trust    │          │ No "this will change how    │
  │    your intuition" advice)│          │ you decide." Mechanism only. │
  ├────────────────────────────────────────────────────────────────────┤
  │ R6: HN viral too early    │ TRUNG    │ Tier S before HN.           │
  │                           │          │ If viral → redirect tới     │
  │                           │          │ falsification criteria.      │
  ├────────────────────────────────────────────────────────────────────┤
  │ R7: Cross-post spam flag  │ THẤP     │ Max 1 post/tuần.            │
  │                           │          │ Each post UNIQUE per         │
  │                           │          │ platform (tone, hook khác).  │
  └────────────────────────────────────────────────────────────────────┘
```

---

## §7 — SUCCESS + FAILURE SIGNALS

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ TÍN HIỆU THÀNH CÔNG                                              │
  ├────────────────────────────────────────────────────────────────────┤
  │ → "Interesting reframe. Let me check the citations." = IDEAL      │
  │ → Counter-evidence: "But study X says..." = HIGH-VALUE            │
  │ → Evans & Stanovich discussion → people actually read §4          │
  │ → Cognitive scientists engage (not just tech) = VERY HIGH         │
  │ → Someone tests: "In my domain, compilation level DID predict..." │
  │ → Cross-platform mention (someone links from another community)   │
  │ → GitHub stars + discussions on framework files                   │
  │ → Blog click-through > 10% from short posts                      │
  ├────────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU CẦN REFINE                                              │
  ├────────────────────────────────────────────────────────────────────┤
  │ → "This is anti-rationalist" = framing needs adjust               │
  │ → "Crank alarm" → title/opening needs soften OR more evidence     │
  │ → Only "cool!" comments → consumption, not verification           │
  │ → "Trust your gut" takeaway → W.4 framing needs strengthen        │
  │ → Ignored on LW → hook not engaging enough cho audience           │
  ├────────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU THẤT BẠI (reassess)                                     │
  ├────────────────────────────────────────────────────────────────────┤
  │ → Multiple cogsci experts: "compilation stage ≠ same mechanism"   │
  │ → Evans & Stanovich response: "you misread our framework"         │
  │ → Falsification criteria met by existing research we missed       │
  │ → All platforms ignore → fundamental framing/quality problem      │
  └────────────────────────────────────────────────────────────────────┘
```

---

## §8 — PRE-REQUISITES

### 8.1 — Trước Khi Publish Blog

```
PHẢI CÓ:
  □ Blog live và accessible trên GitHub Pages
  □ Tất cả footer links hoạt động (4 blog links + repo link)
  □ Blog status: v0.1 → finalized (remove Draft marker)
  □ Short posts A-D đã reviewed (Tier S)

NÊN CÓ (trước Tier S):
  □ Short posts E, G drafted (r/cogsci, r/psychology)
  □ Bluesky account created + follow neuro starter packs
  □ LinkedIn article shortened version drafted

CÓ THỂ LÀM SAU:
  □ ResearchGate + Academia.edu upload
  □ Discord presence
  □ Substack engagement
  □ Medium publication submission
```

### 8.2 — Pre-Post Checklist (Mọi Platform)

```
TRƯỚC MỖI POST:
  □ Blog live và accessible
  □ All links working (blog, repo)
  □ Re-read short post: tone matches platform norms?
  □ Not self-help framing (W.4 check)
  □ Not anti-rationalist framing
  □ Counter-evidence invited explicitly
  □ No marketing language ("star the repo", "share this")
  □ Platform-specific rules checked
  □ Previous platform feedback incorporated (nếu có)
  □ "We do not claim" list present or reflected in tone
```

---

## §9 — RELATION TO OTHER PLANS

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │ PLAN                          │ RELATIONSHIP                        │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-logic-feeling-blog.md    │ = Blog CONTENT structure + quality   │
  │                               │   Plan này = blog DISTRIBUTION      │
  │                               │   2 plans BỔ SUNG nhau              │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-overview-distribution.md │ = Overview blog distribution         │
  │                               │   Plan này ADAPTED nhiều chỗ:       │
  │                               │   -Lobsters, -r/ML, -Alignment Forum│
  │                               │   +ACX, +LinkedIn, +r/AcademicPsych │
  │                               │   Dùng chung platform rules cơ bản  │
  │                               │   KHÔNG double-post cùng platform    │
  ├──────────────────────────────────────────────────────────────────────┤
  │ Drill-Logic-Feeling-Blog.md   │ = Research verification + objections │
  │                               │   Plan này dùng objections (§7)      │
  │                               │   và tone calibration (§8.3)         │
  ├──────────────────────────────────────────────────────────────────────┤
  │ framing-engagement-value.md   │ = 3-layer value model + W.4 rules    │
  │                               │   Áp dụng cho mọi post              │
  ├──────────────────────────────────────────────────────────────────────┤
  │ plan-public.md                │ = General strategy, framing rules    │
  │                               │   W.4, W.5 ÁP DỤNG cho plan này    │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## §10 — TỔNG KẾT

```
  TỔNG: 16 platforms (đã filter từ 17 của overview plan)

  SKIP (so với overview plan): Lobsters, r/ML, Alignment Forum, X/Twitter,
    r/philosophy, Metaculus, OSF Preprints, r/neuroscience (thấp cho blog này)

  MỚI THÊM: ACX Open Thread, LinkedIn, r/AcademicPsychology, Substack

  CẦN TẠO SHORT POST (9): LW (A), r/SSC (B), EA Forum (C),
    ACX comment (D), r/cogsci (E), r/AcademicPsych (F), r/psychology (G),
    Bluesky thread (H), LinkedIn article (I)

  KHÔNG CẦN SHORT POST: HN (submit link), Discord (share),
    CogSci SE (answer), ResearchGate/Academia.edu (upload preprint)

  SHORT POST GROUPS:
    Rationalist (A-D) → shared base, 4 adaptations
    Academic (E-F) → shared base, 2 adaptations
    Accessible (G) → standalone
    Micro-thread (H) → standalone format
    Professional (I) → shortened blog version

  IDENTITY-CHALLENGE MITIGATION:
    → Blog already has: "we do not claim" list, PFC qualifier,
      Evans & Stanovich address, falsification criteria
    → Short posts: lead with "PRO-expertise, PRO-verification"
    → Responding: prepared responses cho 6 predicted objections
```

---

> **Plan v0.1 — sẽ refine dần.**
> Bước tiếp:
>   1. Draft short posts A-D (Tier S — rationalist group)
>   2. Draft short posts E-G (Tier A/B — academic + accessible)
>   3. Draft Bluesky thread H (Tier A — micro-format)
>   4. Draft LinkedIn shortened article I (Tier A — professional)
>   5. Blog publish → execute Tier S → gauge → Tier A → Tier B
