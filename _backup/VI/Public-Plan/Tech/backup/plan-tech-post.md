# Plan: Tech Post — Single Post, Multi-Platform, Route to GitHub

> **Goal:** One tech post, published across multiple forums, all routing to GitHub.
> **Position in strategy:** After neuro posts. Neuro = verify specific claims. Tech = broaden audience + expose full framework.
> **Principle:** "I built this, it explains these questions, here's the evidence, find where it breaks."
> **Status:** PLANNING
> **Created:** 2026-05-26
> **References:**
>   plan-neuro-posts.md — neuro posts go first
>   plan-tech-distribution.md — broader distribution strategy (platforms, audience map, cadence)
>   plan-public.md — framing rules (W.4 anti-self-help, W.5 stakes-based)
>   framing-engagement-value.md — 3-layer value model
>   expert-verification-map.md — 20 expert groups

---

## §1 — Goals

```
  THIS POST DOES:
    ① HOOK: Attract cross-domain experts (tech + neuro + psych + AI + education)
    ② EXPOSE: Introduce framework — enough to be curious, not overwhelmed
    ③ ROUTE: Direct everyone to one GitHub hub
    ④ INVITE: Ask for verification/falsification — counter-evidence > confirmation

  THIS POST DOES NOT:
    ✗ Explain the full framework (that's the repo's job)
    ✗ Convince anyone the framework is correct (evidence speaks for itself)
    ✗ Target mass audience (this is for experts and serious readers)
    ✗ Use self-help framing (W.4)
```

---

## §2 — Approach: Evolution Through Session 2026-05-26

> 4 initial angles explored → refined → chosen direction: Angle E (build → questions → invite)

### Angles Explored and Rejected

```
  ANGLE A: "Misconception → Real Consequences"
    Hook: "The products you build are based on wrong science"
    ❌ REJECTED: Opens with criticism → reader gets defensive → hard to engage.

  ANGLE B: "Open-source for behavioral science"
    Hook: "What if behavioral science worked like open-source software?"
    ⚠️ KEPT FOR REFERENCE: Good tone for body/structure. Weak as hook.

  ANGLE C: "A pattern I found"
    Hook: "Cross-referenced many papers → found a pattern nobody talks about"
    ⚠️ KEPT FOR REFERENCE: Good opening line. Needs trending questions.

  ANGLE D: "What AI is missing"
    Hook: "RLHF assumes dopamine = reward. Neuroscience says otherwise."
    ❌ REJECTED: Too narrow. This post needs broad audience, not AI-only.
```

### ⭐ Angle E: "Build → Trending Questions → Invite" — CHOSEN DIRECTION

```
  FLOW:
    Line 1 — "What I built": cross-referenced research, mapped connections
    Lines 2-5 — "What it explains": list TRENDING QUESTIONS people already have
    Lines 6+ — "Come verify": open-source, invite community

  WHY THIS ANGLE:
    ✓ No criticism → no defensiveness
    ✓ No grand claim → describes WORK DONE, not truth declared
    ✓ Trending questions = reader self-identifies → Layer 1 implicit
    ✓ Invite to verify = peer-level, not lecturing
    ✓ Engineer tone: "I built this, it explains that"

  COMBINED FROM OTHER ANGLES:
    → From C: opening "I cross-referenced research" (discovery, honest)
    → From B: body structure "open-source, invite contribution" (community)
    → Drop A: no criticizing others' products
    → Drop D: not narrowed to AI (but AI can be one of many examples)
```

---

## §3 — Post Structure (Angle E: Build → Questions → Invite)

### Role of Each Section

```
  HOOK = just enough to understand WHAT this post is about.
    → Scope + scale only. Details go in body.
    → Reader decides "interesting, keep reading" or "not for me."

  BODY = give reader enough to be curious, not enough to conclude.
    → Trending questions (reader self-maps)
    → Mechanism examples (show substance)
    → Framework description (show structure)
    → Honest limitations (build trust)

  CLOSE = one clear action.
    → GitHub link. Verify guide. Discussion.
```

### Section Breakdown

```
  ① HOOK (2-3 sentences)
     → Describe what was built: scope + scale
     → Engineer tone: project description, not guru declaration
     → Hook does NOT need to carry everything — body follows

  ② TRENDING QUESTIONS (pick 5-7 from pool below)
     → "The framework provides mechanistic answers to questions like:"
     → Each question = reader self-recognizes "oh, I wonder about that too"
     → DO NOT say "you have this problem" — let reader self-map
     → See §3.1 for full question pool with mechanism analysis

  ③ MECHANISM EXAMPLES (2-3 examples, 2-3 sentences each)
     → Pick 2-3 questions from above → explain briefly with mechanism
     → Enough to intrigue, NOT enough to conclude → drives to repo
     → See §3.1 for mechanism strength per question

  ④ FRAMEWORK DESCRIPTION (brief)
     → How many files, what it covers (neuro → behavior → social)
     → Open-source (CC0), citations, confidence levels
     → Structured like a codebase (files, dependencies, open issues)
     → DO NOT explain in detail — that's the repo's job

  ⑤ HONEST LIMITATIONS
     → "I'm not a neuroscientist"
     → "This is a hypothesis, not a theory"
     → "Domain expert review needed — that's why this post exists"

  ⑥ CALL TO ACTION
     → Verify: "Find where it breaks" — link to VERIFY.md
     → Engage: GitHub Discussions
     → Full framework: GitHub repo link
     → Standard footer (framing-engagement-value.md)
```

---

## §3.1 — Trending Questions Pool (pick 5-7 for final post)

> Analyzed session 2026-05-26. Each question mapped to framework mechanism.
> Tier 1 = mechanism very strong (clear, cited, surprising).
> Tier 2 = mechanism solid (clear, needs light synthesis).
> Final selection: after drafting. Choose questions that are cross-domain,
> surprising, and framework answers convincingly.

### Tier 1 — Framework Explains Very Strong (★★★★★)

```
Q1: Why do humans compete for status — and why does it feel
    so similar across species?
  MECHANISM: Status = Resource Access Map — not "who's superior" but
    "who gets what without fighting." Evolution: repeated fights too
    costly → establish hierarchy once, reuse. Body gives genuine reward
    (opioid + serotonin) when status rises = actual access improvement.
    Cross-species: same serotonin baseline mechanism from lobster
    pecking order to human social dynamics.
  SOURCE: Status.md v2.2
  WHY STRONG: evolutionary foundation clear, cross-species spectrum,
    body-mechanism (serotonin) directly supported by Sapolsky research.

Q2: Why do we feel drained after social media but energized
    after a real conversation?
  MECHANISM: Connection has 3 Generative Primitives + Body-Coupling.
    Real conversation: all 3 + hardware subsidy (oxytocin, cortisol
    buffering) + reciprocal loop. Social media: dopamine alert (novelty)
    but NO opioid reward (genuine connection). Body stays in "lonely"
    state despite high engagement.
  SOURCE: Connection.md v5.0
  WHY STRONG: 3 primitives, Resonance Decline model (2 Forces + 1 Fuel), hardware subsidy
    distinction. Universal experience everyone recognizes.

Q3: Why is boredom painful? It's literally "nothing happening"
    — why does the brain treat it as a problem?
  MECHANISM: Compilable Architecture MUST have input to process. When
    all channels static → idle state → body fires dissonance: "resources
    available but unused." 6 sources of dissonance, all manifest as one
    "bored" feeling. Not lack of stimulation — it's by-product match
    stopping + system designed to compile, not idle.
  SOURCE: Boredom.md v2.0
  WHY STRONG: counterintuitive (why pain from nothing?), 6-source
    unified model, Compilable Architecture is framework's core insight.

Q4: Why does charity feel good but obligation feels heavy
    — even when the action is identical?
  MECHANISM: Charity = pure reward pathway (oxytocin + opioid + status).
    No cost-prediction fired. Obligation = compiled prediction of cost
    to maintain access (5-factor formula, 6 types from explicit-bounded
    to implicit-unbounded). Same action, different system activated.
    Body tracks social exchange mechanically.
  SOURCE: Obligation.md v1.2, Gratitude.md v2.1
  WHY STRONG: very surprising (same action, different feeling), mechanism
    thorough (5-factor, 6-type spectrum), testable.

Q5: Why does physical pain and social rejection activate
    overlapping brain regions?
  MECHANISM: Shared neural hardware (anterior cingulate cortex).
    Evolution: social exclusion = survival threat for social species
    → co-opted same alarm system as physical damage. Not metaphor
    — literally overlapping circuits. Broken bone and broken trust
    both trigger "something wrong, fix now."
  SOURCE: Connection.md, Body-Feedback-Mechanism.md
  WHY STRONG: research well-established (Eisenberger 2003), very
    surprising to non-experts, cross-domain (neuro + psych + evolution).

Q6: What is expert intuition? Do psychologists have it?
    Do mathematicians have it?
  MECHANISM: Expert intuition = compiled chunks firing automatically,
    body-direct, cost ≈ 0. Same mechanism across ALL domains — 3
    directions (Outward/Inward/Social). Formation: 5 stages from vague
    hunch → clear knowing → shareable knowledge. Quality matters:
    genuine-compiled (body-confirmed) vs schema-compiled (may be wrong).
    Dual Check: test intuition against fresh logic.
  SOURCE: Body-Knowing.md v1.0
  WHY STRONG: research-established (Klein 1998, Damasio somatic markers),
    cross-domain (any expert), addresses common confusion about "gut feeling."

Q7: Why do humans need "meaning"? Other species survive fine
    without it — what mechanism makes us different?
  MECHANISM: Meaning = life-level Anchor-Schema — a sync point that
    organizes all chunk patterns. When present + body-accepted → chunks
    self-organize → felt as "meaningful." When absent → fragments →
    internal conflict. 5 anchor types (GOAL/STATE/IDENTITY/FAITH/ROLE).
    Frankl's concentration camp observation as evidence.
  SOURCE: Meaning.md v2.2
  WHY STRONG: mechanism clear (anchor-as-sync-point), Frankl example
    powerful, addresses philosophical question with concrete mechanism.
```

### Tier 2 — Framework Explains Solid (★★★★)

```
Q8: Why does creative work often come with stress?
  MECHANISM: Creativity = opening gaps (prediction-delta). Gap detected
    → cortisol mobilizes for gap-closing (change-readiness, not damage).
    PFC Fresh processing (drafting novel solutions) costs glucose +
    sustained cortisol. Inverted-U: enough cortisol to signal urgency,
    not enough to lock PFC. Stress isn't side effect — it's the
    system working as designed.
  SOURCE: Body-Feedback-Mechanism.md, Cortisol-Baseline.md v2.0
  WHY SOLID: gap-direction + cortisol mechanism clear. Relatable
    to every maker/builder in tech audience.

Q9: Why do billionaires keep working when they don't need money?
  MECHANISM: Gap-Direction — money fills resource-access gaps, NOT
    discovery/creation gaps. Brain optimizes for gap-closing, not
    "having." Rich person still has gaps (curiosity, mastery, novelty,
    status in new domains). Money as technology fills one gap type,
    leaves others untouched.
  SOURCE: Gap-Direction.md, Money-Analysis.md
  WHY SOLID: explains economics puzzle with mechanism, universally
    curious. Billionaire ≠ driven by status (already saturated) —
    driven by remaining gap types.

Q10: Why does being told the right answer feel different from
     discovering it yourself — even when the information is
     exactly the same?
  MECHANISM: Compiled/Fresh Spectrum. Discovery = PFC-Fresh pathway
    (cost > 0, conscious effort) → Hebbian compilation through personal
    effort → genuine-compiled (durable). Being told = trust-compile
    (PFC accepts externally) → fragile, not body-verified. Same
    information, different compilation path = different neural
    persistence and embodied confidence.
  SOURCE: Drill-Compiled-Fresh-Mechanics.md v2.0
  WHY SOLID: framework core distinction (3 compile types), explains
    learning and education directly. Cross-domain: education + AI + UX.

Q11: Why do people defend beliefs MORE aggressively when shown
     counter-evidence — not less?
  MECHANISM: Beliefs = compiled chunk-networks. Challenge triggers
    autonomy-hardware firing (body recognizes external override attempt).
    PFC=Lawyer: rationalizes defense rather than paying uncompile cost.
    3-cost model: re-compiling requires (1) PFC draft new understanding,
    (2) suppress old compiled patterns (cortisol cost), (3) tolerance
    for uncertainty until new pattern stabilizes. Defending is cheaper
    than unlearning.
  SOURCE: Schema.md v2.0, Inter-Body-Mechanism.md
  WHY SOLID: mechanism clear (schema + autonomy + 3-cost). But topic
    can be politically sensitive — use neutral examples.

Q12: Why does learning from AI explanations feel like understanding
     but fail in application?
  MECHANISM: AI explanation = trust-compile pathway (PFC accepts,
    body doesn't compile through experience). Real application needs
    experience-compile (body-verified through doing). Compiled vs Fresh
    distinction: reading AI output = fresh processing, feels like
    understanding because PFC processes it, but body-base hasn't
    installed the pattern.
  SOURCE: Compiled-Fresh.md, AI-Self-Model.md
  WHY SOLID: very relevant for tech audience. Explains why AI tutoring
    has limits. Directly testable by anyone who uses AI daily.

Q13: Why can't you "just stop" an anxious thought loop even
     when you know it's irrational?
  MECHANISM: Prediction-protection — body fires threat signal → PFC
    tries to resolve → can't find actionable gap → loop continues.
    "Knowing it's irrational" = PFC assessment, but body-base runs
    on compiled threat patterns that PFC can't override by logic alone.
    Two separate systems: PFC says "stop," body says "danger."
  SOURCE: OCD-Analysis.md v2.2, Schema.md
  WHY SOLID: 2-system architecture explains it directly. Relatable
    to everyone. But mechanism more case-study than primary framework
    contribution.

Q14: Why does practice + learning work better than learning alone?
  MECHANISM: Experience Compile (body-verified through domain feedback)
    vs Trust Compile (PFC-only, externally accepted). Practice =
    domain gives feedback → body confirms or rejects → compilation
    is durable and context-appropriate. Learning alone = PFC processes
    but body-base doesn't install the pattern. Same content, different
    compilation quality.
  SOURCE: Compile-Taxonomy.md v3.0
  WHY SOLID: overlaps with Q10 mechanism (Compiled/Fresh). Can be
    merged with Q10 or used as supporting example.

Q15: Why does cramming work for exams but not for real expertise
     — even when the content is identical?
  MECHANISM: 3 Compile Types + hardware constraints. Cramming = fresh
    learning (PFC draft, high cost, fragile — decays fast). Real
    expertise = install chunks into body-base through repetition +
    domain verification. PFC ~4±1 slots = physics limit. Chain > 4
    nodes = sustained PFC lock = metabolic wear. Cramming keeps
    everything in PFC (working memory) instead of compiling to
    body-base (long-term, automatic).
  SOURCE: Compile-Taxonomy.md v3.0
  WHY SOLID: hardware constraints (PFC slot limit) are novel.
    Overlaps with Q10/Q14 — consider grouping as one "learning"
    example in the post.
```

### Selection Notes

```
  OVERLAP WARNING:
    Q10, Q14, Q15 share the same core mechanism (Compiled/Fresh).
    → Pick ONE for the post, or group as one "learning" example.
    → Q10 recommended (most surprising framing of the three).

  RECOMMENDED TOP 7 (cross-domain, surprising, strong mechanism):
    ① Q1 — Status cross-species (evolution + economics + biology)
    ② Q2 — Social media drain vs conversation (universal, mechanism clear)
    ③ Q10 — Discovering vs being told (learning + education + AI)
    ④ Q3 — Boredom is painful (counterintuitive, surprising mechanism)
    ⑤ Q4 — Charity vs obligation (same action, different feeling)
    ⑥ Q9 — Billionaires keep working (economics + drive)
    ⑦ Q8 — Creative work + stress (relatable to makers/builders)

  FINAL SELECTION: after drafting full post. These are starting points.
```

---

## §4 — Hook Candidates

> All hooks drafted session 2026-05-26.
> Style: objective, project-focused, scope + scale, let the work speak.
> Hook only needs to establish WHAT this post is about.
> Details (structure, license, falsification) go in body.

### Selected Candidates (9 versions)

```
V1a — Straight engineer
  "I cross-referenced neuroscience research and mapped how the brain's
   core systems actually connect — from neurochemistry to behavior.
   170+ files, open-source. It turns out a lot of everyday questions
   have surprisingly clear mechanistic answers."

V1c — Scope first, number second
  "I mapped the connections between the brain's core systems —
   neurochemistry, behavior, learning, social dynamics — by
   cross-referencing primary research. The result is a 170+ file
   open-source framework where each mechanism has its own file
   with citations and confidence levels."

V1f — Dry tech, repo-style
  "I built an open-source knowledge base that maps human brain
   architecture — from neurochemistry to social behavior. 170+ files,
   structured like a codebase: each mechanism has its own file,
   dependencies are explicit, open questions are tracked. CC0 licensed."

V1g — Scope + structure + 1 example
  "I mapped how the brain's core systems connect — neurochemistry,
   behavior, learning, social dynamics — into a structured open-source
   framework. 170+ files, each with citations and confidence levels.
   Example: the framework traces why 'knowing you should exercise'
   and 'actually doing it' involve two separate systems with different
   update mechanisms."

V1h — Repo pitch, minimal
  "Open-source framework mapping human brain architecture. 170+ files
   covering neurochemistry, behavior, learning, and social dynamics.
   Each mechanism has its own file, cross-references are explicit,
   every claim cites primary research. CC0 licensed. Looking for
   reviewers."

V1i — Scope + what's different
  "I cross-referenced neuroscience research across domains and mapped
   the connections into a single framework — from dopamine signaling
   to social behavior. What makes it different from a textbook: each
   claim has confidence levels, dependencies between mechanisms are
   explicit, and open questions are tracked like issues."

V1n — One-sentence scope + one-sentence structure
  "I mapped the connections between the brain's core systems into a
   170+ file open-source framework — from dopamine signaling to social
   behavior. Structured like a codebase: files per mechanism, explicit
   cross-references, tracked open questions, CC0 licensed."

V1o — What it covers + what it doesn't claim
  "I built an open-source framework mapping how the brain's core
   systems connect — neurochemistry, prediction, behavior, learning,
   social dynamics. 170+ files with citations and confidence levels.
   It's a hypothesis, not a theory — structured for review and
   falsification."

V1q — Scope + 1 differentiator + structure
  "I cross-referenced neuroscience research and mapped how the brain's
   core systems connect — into a 170+ file open-source framework.
   Unlike a textbook, every claim has a confidence level, dependencies
   between mechanisms are explicit, and the framework is structured
   for falsification."
```

### Hook Style Guide

```
  WHAT THESE HOOKS SHARE:
    ✓ Objective — describes work done, not truth claimed
    ✓ Project-focused — engineer introducing a project
    ✓ Scope + scale — reader knows domain and size immediately
    ✓ No criticism — doesn't say others are wrong
    ✓ No grand claim — doesn't say "comprehensive theory of the brain"
    ✓ Lets work speak — substance over style

  WHAT THESE HOOKS DO NOT DO:
    ✗ Tell a personal story ("I started because...")
    ✗ Open with questions ("Have you ever wondered...")
    ✗ Criticize existing work ("Products are built on wrong science")
    ✗ Use attention-grabbing language ("SHOCKING", "everything you know")
    ✗ Carry too much (structure, license, limitations — those go in body)

  HOOK WEIGHT CATEGORIES:
    Light (scope + scale only, body does the rest):
      → V1a, V1c, V1n
    Medium (scope + 1 differentiator):
      → V1g, V1i, V1q
    Heavy (scope + structure + license + stance):
      → V1f, V1h, V1o
    → Light or Medium preferred since body follows.

  FINAL SELECTION: after drafting full post with each hook.
```

---

## §5 — Platform Strategy

```
  ONE POST, MULTIPLE PLATFORMS (same content, minor per-platform adjustments)

  TIER S (stress-test first):
    → LessWrong — rationalist community, deep reading, rigorous stress-test
    → r/slatestarcodex — similar to LessWrong, Reddit-native

  TIER A (expand after Tier S feedback):
    → Hacker News — broad tech, high traffic
    → r/MachineLearning — AI/ML focused
    → r/cogsci — cognitive science

  TIER B (expand if Tier A gains traction):
    → Medium — long-form
    → Dev.to — developer community
    → Twitter/X — thread format

  ORDER:
    Tier S FIRST → refine based on feedback → Tier A → Tier B
    DO NOT post everywhere at once. Each tier = one iteration.

  (Details: plan-tech-distribution.md §3)
```

---

## §6 — Drafting Process

### 6.1 — Iterative Drafting

```
  STEP 1: Draft multiple full versions (different hooks, same body structure)
    → Each version = separate file (drafts/tech-post-v1a.md, ...)
    → Try: V1a hook + body, V1c hook + body, V1n hook + body, etc.

  STEP 2: Compare
    → Criteria:
      - Hook clarity: read first 2 sentences — do you know what this is about?
      - Scope match: broad enough for multi-domain, not so broad it's vague
      - Tone match: W.4 (anti-self-help) + W.5 (stakes-based)
      - Honest signal: does the reader trust the author after reading?
      - Action clarity: does the reader know exactly what to do next?

  STEP 3: Select one or mix
    → Option: one version for all platforms
    → Option: different version for Tier S vs Tier A (Tier S = more technical)
    → Decide AFTER having concrete drafts to compare

  STEP 4: Refine → Publish
```

### 6.2 — Relationship with Neuro Posts

```
  NEURO POSTS go first → TECH POST follows.

  WHY:
    → Neuro posts = micro-verification (one specific claim × expert community)
    → If neuro claim HOLDS → tech post can reference:
      "Claim A was discussed at r/neuroscience: [link]"
    → If neuro claim is CHALLENGED → adjust tech post before publishing
    → = Neuro posts are SCOUTING RUNS. Tech post is MAIN DEPLOYMENT.

  BUT: No need to wait for neuro posts to "succeed."
    → Zero engagement is also a signal (framing needs work, not content wrong)
    → Tech post has independent value
```

---

## §7 — Anti-Patterns

```
  ✗ Feature listing: "Framework has 170 files, covers X Y Z..." → boring
  ✗ Grand claim: "Comprehensive theory of the human brain" → grandiose
  ✗ Humble brag: "I'm just a regular person but..." → fake humility
  ✗ Self-help: "Understanding this framework will help you..." → W.4 violation
  ✗ Marketing: "Star the repo" / "Share this post" → push, not pull
  ✗ Too much detail: Blog-length post on a forum → nobody reads it all
  ✗ Too little evidence: Claims without citations → dismissed
  ✗ Criticism opener: "Your products are built on wrong science" → defensive

  RIGHT TONE: Engineer introducing an architecture + evidence + open issues.
  Honest, specific, verifiable.
```

---

## §8 — Success Signals

```
  ✓ GOOD SIGNALS:
    → Comments asking about specific mechanisms ("claim X in file Y — what evidence?")
    → Counter-evidence: "Research Z says the opposite" → HIGH-QUALITY engagement
    → Domain experts engage (not just tech)
    → GitHub: issues / discussions / forks (meaningful, not just stars)

  ✗ BAD SIGNALS:
    → Completely ignored at Tier S → framing has a problem
    → Only "cool!" comments → consumption, not verification
    → Self-help community picks it up → framing was misread
    → Stars without engagement → vanity metric
```
