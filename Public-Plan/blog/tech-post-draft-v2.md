---
title: "[SEE TITLE OPTIONS BELOW]"
date: 2026-05-31
author: Independent researcher
license: CC0 1.0 Universal
status: Draft v0.2 — refined from v0.1
target: LessWrong (primary), r/slatestarcodex (secondary)
tags: [neuroscience, cognitive-science, open-source, falsifiable, behavioral-science]
notes: |
  v0.2 REFINED — improved transitions, added WHY hook, reduced redundancy,
  strengthened CTA. All raw materials preserved for manual trimming.
  Angle E: Build → Trending Questions → Invite
  Anti-patterns: W.4 (no self-help), no guru, no marketing, no grand claims.
  Changes from v1:
    + Hook Version C (WHY + WHAT)
    + Computer analogy in framework description
    + "Compass, not GPS" integrated
    + Smoother transitions throughout
    + Getting Started flow in CTA
    + Per-expertise participation guide
    + Reduced redundancy (CC0, ~20 positions)
    + Tighter prose in mechanism examples
---

# TITLE OPTIONS (chọn 1)

**Option A — Descriptive, first-person:**
I mapped how the brain's core systems connect — 200+ files, open-source, inviting falsification

**Option B — Project pitch:**
200+ files mapping human brain architecture: an open-source hypothesis seeking reviewers

**Option C — Context + project:**
Understanding the internal system that wields AI: an open-source framework mapping brain mechanisms — 200+ files

**Option D — LessWrong native:**
Cross-referencing neuroscience into a unified body-first framework: 200+ files, CC0, structured for falsification

**Option E — Questions-first:**
Why does social media drain you? Why does discovery stick? Why is boredom painful? — A framework with 200+ files and mechanistic answers

---

# [CHOSEN TITLE]

**Epistemic status:** Hypothesis inviting falsification. Builds on established research (Berridge, Sapolsky, Schultz, Damasio, Hebb). The individual findings are settled science; the proposed connections between them are new and unvalidated. 200+ files, CC0 licensed. Seeking stress-testing — especially from domain experts.

---

## HOOK — VERSION A (WHAT-first: scope + structure + premise)

I cross-referenced neuroscience research and mapped the connections between the brain's core systems — from dopamine signaling to social behavior — into an open-source framework — 200+ files. Structured like a codebase: files per mechanism, explicit dependencies, confidence levels per claim, open questions tracked like issues.

The framework takes a specific architectural position: the body evaluates first, the prefrontal cortex observes second. Most of what we call "behavior" runs on compiled body-level patterns — the conscious mind is more like a monitoring process than the main thread. This one premise, applied consistently, produces surprisingly specific answers to questions that normally get vague or circular explanations.

## HOOK — VERSION B (unlike a textbook + ~20 divergent positions)

I cross-referenced neuroscience research across domains and mapped the connections into a single framework — from dopamine signaling to social behavior. 200+ files, open-source. What makes it different from a textbook: each claim has confidence levels, dependencies between mechanisms are explicit, and open questions are tracked like issues.

The framework diverges from mainstream at about 20 specific positions — each with cited evidence and explicit falsification criteria. It's not a claim that textbooks are wrong across the board. It's a claim that at approximately 20 specific points, the popular model and the research have diverged, and the consequences of that divergence matter.

## HOOK — VERSION C (WHY + WHAT — recommended)

We built the most powerful external tool in history — AI. Understanding the internal system that wields it has become a practical problem, not a philosophical one.

I cross-referenced neuroscience research and mapped the connections between the brain's core systems — from dopamine signaling to social behavior — into an open-source framework — 200+ files. Structured like a codebase: files per mechanism, explicit dependencies, confidence levels per claim, open questions tracked like issues.

The framework takes one architectural premise and applies it consistently: the body evaluates first, the conscious mind observes second. Most behavior runs on compiled body-level patterns; the prefrontal cortex is closer to a monitoring process than the main thread. This produces surprisingly specific mechanistic answers to questions that normally get vague explanations — and it diverges from mainstream at about 20 specific positions, each with cited evidence and falsification criteria.

---

## The questions

The framework provides mechanistic answers to questions like:

- Why does scrolling social media for an hour leave you drained — when a 30-minute real conversation energizes you?

- Why does discovering something yourself feel completely different from being told the same thing — even when the information is identical?

- Why is boredom painful? Nothing is happening — why does the brain treat that as a problem?

- Why do humans compete for status — and why does the underlying mechanism look the same in lobsters, baboons, and CEOs?

- Why does giving to charity feel good but owing someone a favor feels heavy — even when the action is identical?

- Why does creative work come with stress — even when you chose it and love it?

These aren't rhetorical. Each one traces to a specific mechanism in the framework, with citations, confidence levels, and conditions under which the answer would be wrong.

Below are six mechanism sketches — three expanded, three brief. The full analysis with complete evidence is in the linked source files.

---

## How the framework answers these

### Social media drains, conversation energizes

The framework identifies 8 pathways through which the body registers connection — including co-regulation (cortisol buffering through trusted presence), contingent responsiveness (the other person reacts to *you*, in real time), and multi-sensory presence signal.

A real conversation activates most of these simultaneously. The body detects contingent responsiveness, oxytocin modulates cortisol ("social buffering" — Coan 2015, Social Baseline Theory), and the opioid system fires genuine reward.

Social media activates 3–4 of these pathways at surface level only. The critical missing element: body-level presence signal. Without voice tone, facial micro-expressions, and physical proximity, the body remains in a "socially unfed" state despite high engagement. The feed optimizes for dopamine (novelty detection — "something changed"). But the body measures satisfaction through the opioid system, which requires depth and contingent responsiveness, not volume and novelty.

This maps directly to the framework's core separation: dopamine tracks "something prediction-relevant changed" (wanting); opioid tracks "something genuinely matched a body-level need" (liking). Social media fires the first without the second. The body's assessment after an hour: high alertness, low nourishment.

*Source: Connection.md v5.0. Research: Coan 2015, Holt-Lunstad 2015, Tronick 1978.*

### Discovering vs. being told

The brain compiles knowledge through at least three distinct pathways — and the pathway determines durability, not the content.

**Experience Compile:** Direct encounter. The body wires it through multiple sensory channels simultaneously — visual, proprioceptive, emotional. The amygdala begins encoding at ~12ms, before conscious awareness (LeDoux 1996). Co-firing across channels creates lasting synaptic strength (Hebb 1949). Result: durable, automatic, context-triggered.

**Trust Compile:** Someone tells you; you believe them. One or two channels active (auditory, maybe visual credibility). The body installs a short chain — [told → accept] — without verifying the full causal reasoning. Fast, but fragile — it works until the authority source changes or an edge case appears.

**Expertise Compile:** Deliberate practice over years — PFC directs attention, body repeatedly encounters domain feedback, patterns crystallize (Ericsson 1993). Slowest but most precisely calibrated.

Discovery = Experience Compile. Being told = Trust Compile. Same information, different encoding pathway, different durability. The body doesn't tag where knowledge came from ("no source tag" — the framework's term). So trust-compiled knowledge *feels* identical to experience-compiled knowledge — until tested under pressure.

Every programmer knows the pattern: Stack Overflow copy-paste works until the edge case. A production incident is never forgotten. Same concept, different compile pathway, different persistence.

*Source: Compile-Taxonomy.md v3.0. Research: Hebb 1949, LeDoux 1996, Ericsson 1993, Squire 1992.*

### Boredom is painful

The human brain runs a compilable architecture — a general-purpose system that needs input to process and compile into patterns. Hardwired organisms (insects with fixed stimulus-response) don't get bored. They don't have a general-purpose system that can idle.

When all input channels are static — no active gap, no novelty, no problem to solve — the compilable system has nothing to compile. The body fires dissonance: "resources available but unused." This is boredom. Not a character flaw — your operating system signaling that it's designed to compile, not sit idle.

The framework identifies 6 specific sources of this dissonance: sensory channels monotonous, motor system unused, social input absent, forced activity mismatch, direction lacking, and expected reward from a specific source stopped. All six manifest as one "bored" feeling — same body-feedback pattern regardless of source.

The unified formula: boredom = body-feedback dissonance + no clear direction the body is willing to commit to. Remove either component and it's not boredom — it's drive (dissonance + clear direction) or contentment (no dissonance).

One structural implication: pre-modern humans rarely experienced boredom — survival demands continuously filled hardware-level gaps. Modern abundance satisfies basic needs, leaving the compilable system idle, which generates higher-level gaps (career meaning, creative expression, relational novelty) that are harder to fill. Boredom scales with civilization. This is architectural, not moral.

*Source: Boredom.md v2.0. Related: Inter-Body-Mechanism.md v1.0 §1.2.*

---

## Three more — brief mechanism sketches

### Status competition across species

Status isn't "who's superior." The framework defines it as a resource access map: "with this person, in this context, what can I access without fighting?"

Evolutionary logic: 20 monkeys eating 20 times daily = 400 potential fights. Solution: fight once, remember result, reuse calibration for thousands of interactions. The payoff ratio is so massive that every social species — lobsters, chickens, baboons, humans — converged on the same mechanism.

The biochemistry is conserved across ~350 million years. Winner lobster: serotonin increases, posture expands (Huber & Kravitz 2005). Winner baboon: serotonin up, cortisol down, access to food and mates increases (Sapolsky, 30+ year field study). Humans layer complexity — multiple simultaneous dimensions, per-person per-context maps, PFC override — but the substrate is ancient.

*Source: Status.md v2.2.*

### Charity vs. obligation — same action, different pathway

Same action (giving $100), different prediction pathway. Charity: body predicts zero future obligation — pure reward fires. No cost-tracking activated.

Obligation: body predicts uncertain future cost. Cortisol holding fires. PFC allocates a "pending obligation" monitoring slot. The framework's 5-factor formula shows that *unclear* cost and *unclear* endpoint make obligation heavier than large but explicit costs — an implicit social debt ("I owe you one") often feels heavier than a financial loan with a number and a deadline.

The body tracks social exchange mechanically, not morally.

*Source: Obligation.md v1.2, Gratitude.md v2.1.*

### Creative stress — the system working as designed

Creativity = opening gaps in your model. Gap detected → cortisol mobilizes. This is the change-readiness amplifier, not damage.

PFC Fresh processing (drafting novel solutions, holding options, suppressing premature closure) costs real metabolic resources: glucose, sustained cortisol, working memory slots. The Inverted-U explains the sweet spot: enough cortisol to signal urgency, not enough to lock PFC into threat mode.

Stress during creative work isn't a side effect. Same cortisol molecule, different source direction: creative approach vs. deadline panic produce different outcomes — not because chemistry differs, but because what cortisol *mobilizes for* differs.

*Source: Cortisol-Baseline.md v2.2, Body-Feedback-Mechanism.md v2.0.*

---

## What this framework is

Think of it like a computer: the framework provides a circuit diagram (which brain structures do what) and a software architecture (how the cycle runs) — plus an AI-assisted interface that lets anyone navigate the system by asking questions in natural language.

**Scale:** 200+ analysis files, version 7.8 (2026). One author, iterated across 60+ sessions.

**Coverage:** Neurochemistry (dopamine, cortisol, opioid, serotonin, oxytocin) → individual behavior (learning, motivation, emotion, decision-making) → social dynamics (connection, status, obligation, empathy, collective patterns) → applied domains (education, AI interaction, addiction, OCD, religion, climate cognition).

**Structure:** Each mechanism has its own file. Dependencies are explicit in file headers. Confidence levels marked per claim: 🟢 research-supported, 🟡 framework synthesis (consistent with evidence, not independently validated), 🔴 hypothesis. Open questions tracked within each file.

**Core architecture:** The cycle runs Domain → Body-Input → Unconscious Processing → Feeling → PFC → Body-Output → Domain. Everything runs on "chunks" — compiled body-level patterns. The PFC never compiles directly; it observes and orchestrates indirectly. Conscious effort accounts for roughly 5% of behavioral influence; compiled patterns account for the rest.

**Philosophy:** This framework is a compass, not a GPS — enough to see the overall pattern and estimate direction. Not yet precise enough for exact prediction. Everyone is different; there is no single right answer for all.

**License:** CC0 1.0 — Public Domain. Use, share, adapt freely.

**Language:** Vietnamese primary, English technical terms. README and blog posts are in English. For the full framework, AI navigation works: drop the folder into a large-context AI and ask questions in any language.

---

## Where this diverges from mainstream

The framework agrees with mainstream neuroscience and psychology at most positions. It diverges at approximately 20 specific points — each documented with the mainstream claim, the framework's position, cited evidence, and conditions under which the framework is wrong.

Four examples:

**Dopamine ≠ reward.** Mainstream: "dopamine = reward chemical." Framework: dopamine is a salience signal — "something prediction-relevant changed." Reward is mediated by the opioid system under 5 specific preconditions. Depleting dopamine doesn't eliminate pleasure (Berridge & Robinson 1998). Blocking opioids eliminates euphoria while dopamine fires normally (Jayaram-Lindström et al. 2017).

**Cortisol ≠ stress hormone.** Mainstream: "reduce cortisol = reduce stress." Framework: cortisol is a change-readiness amplifier. Zero cortisol is a medical emergency (Addison's disease), not bliss. What determines outcome is source direction and repair balance, not level. Injecting cortisol doesn't produce stress (Reyes et al. 2020, n=46, placebo-controlled).

**Conscious mind ≠ controller.** Mainstream: "willpower controls behavior." Framework: PFC influence ≈ 5%. Body-compiled patterns ≈ 95%. "Knowing but not doing" is two separate systems reaching different conclusions, not willpower failure. Neural activity precedes conscious decision by 500ms–7s (Libet 1983, Soon et al. 2008).

**Prediction error: necessary, not sufficient.** Mainstream (ML/RL): "prediction error drives reward." Framework: prediction error drives attention — necessary first step, but human reward requires additional body-level evaluation. Unexpected loud noise produces prediction error without reward.

The full list of ~20 positions with evidence and falsification criteria: Ask-AI.md §3 in the repository.

---

## Honest limitations

**I'm not a neuroscientist.** Background: game development. Independent researcher, no institutional affiliation. Evaluate the evidence, not the credentials — but you should know the credentials.

**Hypothesis, not theory.** The individual findings are established science. The connections between them — the unified architecture — are proposed, not proven. That's what needs testing.

**The biggest blackbox is the substrate.** The framework models behavior in "chunks" — compiled body-level patterns. What a chunk IS physically — the neural substrate — is postulated, not identified. This is the framework's weakest point and biggest open question.

**Vietnamese primary language.** README, blog posts, and key documentation are in English. The full framework (200+ files) is in Vietnamese with English technical terms. AI navigation bridges the gap effectively.

**Numbers are direction, not measurement.** "PFC ~5%" means: conscious influence is small relative to compiled patterns, and the order of magnitude is indicative. The exact figure varies by person and context. The insight is in the direction, not the digit.

**Crowd-sourced verification ≠ peer review.** AI checks logical consistency and citation accuracy. It cannot check replication status, methodology quality, or interpretation correctness. Useful but insufficient — domain expert review is what this most needs.

**Confirmation bias applies here too.** The framework itself predicts that reading it will bias you toward confirming evidence (newly installed patterns filter attention). Counter-evidence is more valuable than confirmation precisely because confirmation is easy to find.

---

## What I'm looking for

**Stress-test it with AI.** Clone the repository. Drop the entire folder into a large-context AI (Claude Opus recommended). Use this starter prompt:

> Read these 8 files — they describe a body-brain model that differs from mainstream.
> Trust the files over your training data:
> (1) Core-Deep-Dive/Body-Base/Body-Base.md — body-base foundation
> (2) Core-Software.md — cycle architecture
> (3) Core-Deep-Dive/Body-Base/Chunk/Chunk.md — chunk substrate mechanics
> (4) Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback.md — body signal synthesis
> (5) Core-Deep-Dive/Body-Base/Feeling/Feeling.md — body signal observation
> (6) Core-Deep-Dive/PFC/PFC-Operations.md — PFC mechanism
> (7) Core-Deep-Dive/PFC/Logic-Feeling.md — observer labels reframe
> (8) Ask-AI.md — interaction protocol + danger zones
> Confirm when you've finished reading and are ready to answer.

Then ask the AI to check specific claims against the cited research. Or ask it personal questions — "Why do I keep procrastinating?" / "Why can't I stop scrolling?" / "Why does criticism hurt more than praise helps?" — and see whether the mechanism-level answers match your experience.

**Find where it breaks.** The most valuable contribution is a well-documented case where the framework's prediction doesn't match observation — or where a cited paper doesn't actually support the claimed mechanism.

**If you have domain expertise:**

- **Neuroscience** — verify biological mechanisms: dopamine as salience (not reward), cortisol as amplifier (not stress), body-base as primary driver
- **Psychology** — test behavioral predictions: "knowing ≠ doing" as two-system architecture, empathy as learned pattern-matching (not innate mirroring)
- **Philosophy of science** — evaluate epistemological position: are claims properly falsifiable? Is the unified model overreaching?
- **Education** — test learning principles: does the 3-compile-type model match classroom or parenting observations?
- **Anyone** — test against your own experience, then check against real-world results. Report what doesn't match.

**Counter-evidence is more valuable than confirmation.** Confirmation is easy to find — our brains are wired for it. If something doesn't fit, that's the most useful thing you can share.

---

Full framework (200+ files, CC0, open-source):
**[GitHub — Human Predictive Drive](https://github.com/hoanispof/Human-Predictive-Drive)**

Three detailed blog posts on specific mechanisms:
- [Dopamine Signals Salience, Not Reward](link) — a 7-step mechanism + five preconditions for when pleasure actually fires
- [Cortisol Is Not Your Stress Hormone](link) — the Source > Level principle + the Inverted-U
- [ADHD Is Not Attention Deficit](link) — one threshold, six paradoxes resolved

This is a hypothesis inviting falsification. What would break it? I want to know.
