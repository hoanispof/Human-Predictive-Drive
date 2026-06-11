---
title: Short Post — Framework Overview (Canonical)
date: 2026-06-07
purpose: 1 canonical post for all platforms. Per-platform adaptation done directly when posting.
status: Draft v0.1
overview_blog_url: https://hoanispof.github.io/Human-Predictive-Drive/blog/framework-overview/
github_url: https://github.com/hoanispof/Human-Predictive-Drive
detail_blog_urls:
  dopamine: https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/
  cortisol: https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/
  adhd: https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/
  logic_feeling: https://hoanispof.github.io/Human-Predictive-Drive/blog/logic-is-not-the-opposite-of-intuition/
platforms: LessWrong, r/slatestarcodex, EA Forum, Hacker News, r/cogsci, r/psychology, r/MachineLearning, r/PhilosophyofMind, r/neuroscience, Bluesky, Mastodon
references:
  plan-distribution.md — execution order, phases, cadence, responding protocol
  plan-overview-distribution.md — Blog D platform details + per-platform rules
  plan-overview-blog.md §4 — short post structure origin (7-component)
  framing-engagement-value.md — 3-layer value model, W.4 rules
supersedes:
  blog/backup/short-post-overview.md — 9 posts per-platform, different tease per platform
  blog/backup/short-post-overview-main.md — 2-version canonical + reformat plan
---

# Short Post: Framework Overview — Canonical

> APPROACH: 1 bài post duy nhất, chất lượng cao nhất.
>
> Framework = cross-disciplinary (neuroscience + psychology + evolutionary biology).
> Không thuộc chuyên môn nào cụ thể → không cần adapt nội dung theo từng platform.
>
> 4 blog chi tiết đã tồn tại → 4 blog titles trong post tự hook từng audience segment.
> Thay thế mechanism tease cũ (1 ví dụ cho 1 segment) bằng 4 entry points (hook tất cả).
> Pull-based: reader TỰ CHỌN entry point phù hợp.
>
> NỘI DUNG: giống nhau 100%.
> FORMAT: adapt trực tiếp per platform khi post (không pre-write trong file này).
>
> Structure:
>   ① WHAT → ② POSITION → ③ DEEP-DIVES (4 blog links) →
>   ④ EPISTEMIC → ⑤ LINKS → ⑥ CLOSE
>
> Tại sao ④ DEEP-DIVES thay ④ MECHANISM TEASE:
>   Cũ: 1 ví dụ (compiled vs fresh) → hook 1 segment → cần nhiều posts cho nhiều segments
>   Mới: 4 blog titles → mỗi title = 1 hook → cover tất cả segments trong 1 post
>   Mỗi blog title BẢN THÂN ĐÃ LÀ 1 TEASE — compelling hơn bất kỳ tóm tắt 2 câu nào.
>
> NOTE: Mỗi detail blog có short posts RIÊNG (short-posts-dopamine.md,
> short-posts-cortisol.md, short-posts-adhd.md, short-posts-logic-feeling.md).
> Những file đó target domain-specific platforms với tone riêng per audience.
> File NÀY là overview — giới thiệu FRAMEWORK, không phải 1 claim cụ thể.
> 4 blog links trong post = entry points, không phải thay thế cho per-blog short posts.

---

## Canonical Post (~320 words)

**Title:** A concept bridging neuroscience and psychology into an architecture — estimating the direction of human drive

**Body:**

[Epistemic status: hypothesis inviting falsification. Individual findings are established science; proposed connections are new and unvalidated.]

A framework connecting neuroscience, psychology, and evolutionary biology into an architecture — mapping how the brain's core systems produce behavior, 
from opioid-dopamine signaling through body-level evaluation of threat, novelty, social status, and connection — to collective behavior. 200+ source files with explicit dependencies, open-source, CC0.

Core premise: the body evaluates first, the prefrontal cortex observes second. Most behavior runs on compiled body-level patterns — the conscious mind is the observer, not the executor.  
When you're thirsty, the conscious mind sets one goal: get water. Everything after — walking, reaching for the cup, pouring, drinking — executes automatically.  
You speak your native language fluently — grammar, intonation, coordination of throat and tongue, all running automatically with high precision. Yet your conscious mind cannot describe the grammatical rules you're using.

Applying this premise consistently reframes several commonly misunderstood mechanisms:

- [Dopamine Signals Salience, Not Reward](https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/) — a 7-step mechanism + five preconditions for when pleasure actually fires
- [Cortisol Is Not Your Stress Hormone](https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/) — the Source > Level principle + the Inverted-U
- [ADHD Is Not Attention Deficit](https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/) — one threshold, six paradoxes resolved
- [Logic Is Not the Opposite of Intuition](https://hoanispof.github.io/Human-Predictive-Drive/blog/logic-is-not-the-opposite-of-intuition/) — one process, two observer labels, and why neither can verify itself

Built through personal observation cross-referenced against published research, with AI-assisted synthesis — a method that can surface cross-disciplinary connections, but also carries risk of individual bias.

A starting point for verification: the neuroscience foundations — opioid, dopamine, cortisol mechanisms — are grounded in cited research and falsifiable against established literature. If those hold, test the behavioral mechanisms next: does the framework predict what you actually observe — in yourself and in others? If the architecture is sound, these mechanisms connect individual experience to collective patterns.

If something contradicts your observation or expertise, that's the most valuable feedback. Where does this break?

Full framework with explicit dependencies (200+ source files, CC0): https://github.com/hoanispof/Human-Predictive-Drive

---

## Format Adaptation Notes

> Canonical post = source of truth.
> Khi post lên platform cụ thể, tinh chỉnh FORMAT trực tiếp — không pre-write ở đây.
> Dưới đây là hướng dẫn cần nhớ cho mỗi format group.

### Format A: Text Post — canonical nguyên bản

```
PLATFORMS: LessWrong, r/slatestarcodex, EA Forum, r/cogsci, r/neuroscience,
           r/psychology, r/PhilosophyofMind

THAY ĐỔI: KHÔNG. Title + body y hệt canonical.

EXCEPTION:
  r/MachineLearning → thêm [D] tag đầu title:
    "[D] A concept bridging neuroscience and psychology into an architecture
     — estimating the direction of human drive"
  Body: canonical nguyên bản.
```

### Format B: Link + Author Comment — Hacker News

```
PLATFORM: Hacker News

SUBMIT TYPE: Link submission
  → URL: https://hoanispof.github.io/Human-Predictive-Drive/blog/framework-overview/
  → Title: Show HN: Framework mapping brain mechanisms into an architecture (CC0)

AUTHOR COMMENT (~180 words):
  → Condensed từ canonical body
  → Bỏ [Epistemic status] tag ở đầu (HN không dùng convention này)
  → Dời epistemic status xuống cuối comment (1 câu)
  → Giữ: ① WHAT, ② POSITION, ④ DEEP-DIVES, ⑦ CLOSE
  → Blog link đã là submission URL → chỉ cần GitHub link trong comment
```

### Format C: Micro-thread — Bluesky (300 chars) / Mastodon (500 chars)

```
PLATFORMS: Bluesky, Mastodon

FORMAT: Thread 4 posts
GUIDE:
  Post 1 — ① WHAT + ② POSITION (condensed)
            [Attach: overview blog URL as link card]
  Post 2 — ③ OVERVIEW (condensed) + 2 blog titles
  Post 3 — 2 blog titles còn lại + ⑤ EPISTEMIC + ⑥ LINKS (GitHub)
  Post 4 — ⑦ CLOSE + hashtags

NOTES:
  Bluesky: 300 chars/post, link cards KHÔNG count vào limit
  Mastodon: 500 chars/post, URLs = 23 chars regardless of length
  Bluesky hashtags: lowercase (#neuroscience, #cogsci, #openscience)
  Mastodon hashtags: CamelCase (#Neuroscience, #CognitiveScience, #OpenScience)
```

---

## Quality Verification

```
BLOG STRUCTURE (updated 2026-06-08):
  Overview blog:   docs/_posts/2026-06-08-framework-overview.md
                   = canonical post + full "Stress-test it with AI"
                   URL: .../blog/framework-overview/
  Backup:          docs/_posts/backup/2026-06-04-11-questions-one-architecture.md
                   = 11 questions, 6 mechanism sketches (archived — content reusable)

VERIFY CANONICAL POST:
  ✓ Core premise: "body evaluates first, PFC observes second"
  ✓ "monitoring process than the main thread"
  ✓ 2 illustrations (thirst, language) — everyday experiences consistent with
    Core-Software.md §1.2 (PFC = observer + orchestrator, CANNOT override strong signals)
    Body-Knowing.md §1.1 (~95% compiled, cost ≈ 0)
  ✓ "200+ source files with explicit dependencies, open-source, CC0"

VERIFY 4 BLOG LINKS:
  ✓ Descriptions match mechanism blog footer — consistent language
  ✓ URLs match actual blog file slugs in docs/_posts/
  ✓ All 4 blog files exist:
    docs/_posts/2026-05-31-dopamine-signals-salience-not-reward.md
    docs/_posts/2026-05-31-cortisol-is-not-stress.md
    docs/_posts/2026-05-31-adhd-is-not-attention-deficit.md
    docs/_posts/2026-06-04-logic-is-not-the-opposite-of-intuition.md

ANTI-PATTERN CHECK:
  ✓ No "I built..." opener
  ✓ No question-hook opening
  ✓ No feature list opening (200+ files in WHAT, not as opener)
  ✓ No self-help framing (W.4) — 2 illustrations describe mechanism, not advice
  ✓ No marketing language ("star the repo", "share this")
  ✓ No guru tone
  ✓ No divergences list in short post (belongs in mechanism blog)
  ✓ Counter-evidence invited explicitly
  ✓ Epistemic status present
```

---

## Posting Rules (condensed)

```
ORDER: All blogs live FIRST → then short post (all links must work before posting)

CADENCE:
  → Max 1 post / tuần. KHÔNG post nhiều platforms cùng ngày.
  → Đợi feedback 3-7 ngày trước khi post tiếp.
  → Post bị ignore → refine framing, KHÔNG spam lại.

PRIORITY: xem plan-distribution.md §3 Phase 2

RESPONDING: xem plan-distribution.md §3 Phase 4

PRE-POST CHECKLIST:
  □ Overview blog live + accessible
  □ 4 detail blogs live + accessible
  □ All links working (overview blog, 4 detail blogs, GitHub)
  □ Re-read post: does it represent the framework accurately?
  □ Not self-help framing (W.4 check)
  □ Counter-evidence invited explicitly
  □ No marketing language
  □ Platform rules checked (mỗi sub có rules riêng)
```
