---
title: "A concept bridging neuroscience and psychology into a connected model — estimating the direction of human drive"
date: 2026-06-03
author: Independent researcher
license: CC0 1.0 Universal
status: Draft v0.3
target: LessWrong (primary), r/slatestarcodex (secondary)
tags: [neuroscience, cognitive-science, open-source, falsifiable, behavioral-science]
notes: |
  v0.3 — Rewritten from drill-tech-post-v2.md analysis.
  Angle E: Build → Trending Questions → Invite.
  Anti-patterns: W.4 (no self-help), no guru, no marketing, no grand claims.
  Changes from v2:
    + 7 questions (6 single + 1 collective cluster with 5 sub-questions)
    + Hook A (WHAT-first, direct engineer tone)
    + Title chốt
    + New sketches: Expert decisions (expanded), Limerence (expanded), Always active (brief)
    + Collective cluster = constellation format (no mechanism sketch — tease only)
    + Compressed supporting sections
    + Removed: Boredom standalone, Discovery vs told, Charity vs obligation
  Source: drill-tech-post-v2.md (full analysis), tech-post-draft-v2.md (reference)
---

# A concept bridging neuroscience and psychology into a connected model — estimating the direction of human drive

**Epistemic status:** Hypothesis inviting falsification. Builds on established research (Berridge, Sapolsky, Schultz, Damasio, Hebb). The individual findings are settled science; the proposed connections between them are new and unvalidated. 200+ files, CC0 licensed. Seeking stress-testing — especially from domain experts.

---

I cross-referenced neuroscience, psychology, and evolutionary biology research and mapped the connections between the brain's core systems — from dopamine signaling to social behavior — into an open-source framework — 200+ files. Structured like a codebase: files per mechanism, explicit dependencies, confidence levels per claim, open questions tracked like issues.

The framework takes one architectural position: the body evaluates first, the prefrontal cortex observes second. Most of what we call "behavior" runs on compiled body-level patterns — the conscious mind is more like a monitoring process than the main thread. This one premise, applied consistently, produces surprisingly specific answers to questions that normally get vague or circular explanations.

---

## The questions

The framework provides mechanistic answers to questions like:

- Why does scrolling social media for an hour leave you drained — when a 30-minute conversation with a close friend energizes you?
- Why can't humans sit still — not even billionaires with nothing left to prove?
- Why do humans compete for status — and why does the underlying mechanism look the same in lobsters, baboons, and CEOs?
- Why does creative work come with stress — even when you chose it and love it? And when does that stress become genuinely harmful?
- Why is forced analytical thinking sometimes unproductive — while a split-second expert decision is often right?
- Why does limerence produce genuine bliss — and why is it biologically guaranteed to end? What mechanism sustains a marriage after the hardware subsidy expires?

These five questions seem unrelated:

- Why does a single critical comment online cause real anxiety — even from someone you'll never meet?
- Why does betrayal by someone close cause genuine physical pain — when your body wasn't touched?
- Why does being around a calm person make you calmer — without them saying a word?
- Why does chronic loneliness damage your health as much as smoking 15 cigarettes a day?
- Why does a crowd's energy sweep you up — even when you rationally don't care about the game?

The framework traces all five to one architectural fact about the human body. The source files explain what it is.

These aren't rhetorical. Each one traces to a specific mechanism in the framework, with citations, confidence levels, and conditions under which the answer would be wrong.

Below are six mechanism sketches — three expanded, three brief. The cluster above points to its own mechanism in the source files.

---

## How the framework answers these

### Social media drains, close friend energizes

The framework identifies 8 pathways through which the body registers connection — including co-regulation (cortisol buffering through trusted presence), contingent responsiveness (the other person reacts to *you*, in real time), and multi-sensory presence signal.

A conversation with a close friend activates most of these simultaneously. The body detects a trusted entity — oxytocin modulates cortisol ("social buffering" — Coan 2015), and the opioid system fires genuine reward. A close friend means deeper: compiled trust, shared history, reward circuits already primed.

Social media activates 3–4 pathways at surface level only. The critical missing element: body-level presence. Without voice tone, facial micro-expressions, and contingent response, the body stays in a "socially unfed" state despite high engagement.

The core distinction: dopamine tracks "something prediction-relevant changed" (wanting); opioid tracks "something genuinely matched a body-level need" (liking). Social media fires the first without the second. The body's verdict after an hour: high alertness, low nourishment.

*Source: Connection.md v5.0. Research: Coan 2015, Holt-Lunstad 2015, Tronick 1978.*

### Expert decisions vs. forced thinking

The brain compiles knowledge through experience. Repeated exposure to domain feedback — debugging code, tasting food, reading patients — builds body-level patterns that fire automatically: near-instant, near-zero cost. This is what Klein (1998) documented as recognition-primed decisions: experts don't weigh options — they recognize patterns.

The PFC (conscious analytical mind) runs differently: ~4 working memory slots, high glucose cost, sustained cortisol. When the domain has no compiled base to draw from, the PFC must draft everything from scratch — expensive, slow, error-prone.

The framework identifies this as the real axis: compiled processing (body-direct, domain-specific, fast) vs. fresh processing (PFC-drafted, general-purpose, costly). Every programmer knows the pattern: the senior architect "sees" the bug instantly; the junior developer debugs for hours. Same codebase. Different compiled base.

But compiled doesn't mean correct — it means untested assumptions feel identical to verified expertise. Domain feedback is the only arbiter. The body rewards results, not effort.

*Source: Body-Knowing.md v1.0, Compile-Taxonomy.md v3.0. Research: Klein 1998, Kahneman 2011, Ericsson 1993.*

### Limerence — why it ends, what sustains the bond

Limerence isn't illusion — it's drive-level biology. Fisher (2004) showed it activates the same neural systems as hunger and thirst. The body provides a temporary hardware subsidy: dopamine surge, norepinephrine, oxytocin, reduced serotonin (producing obsessive focus), and selectively lowered PFC evaluation. All three reward channels fire simultaneously — novelty, warmth, and episodic peaks — producing the strongest compound reward humans experience.

It's guaranteed to end because the subsidy is temporary by design: 18–36 months (Fisher 2004). Its evolutionary function is to keep two strangers together long enough to bond. Once the window closes, accumulated habituation reveals at once — "the spark died" is subsidy expiry, not stopped loving.

What sustains a bond afterward? The framework identifies the limerence window as fuel for building durable structures: shared experience chunks that compile into both people, communication patterns for resolving conflict (Gottman: the most stable couples aren't conflict-free — they know how to repair), and deep mutual understanding built during peak curiosity.

Post-limerence, the mechanism shifts: novelty-based reward requires active effort (Aron 2000), while baseline warmth becomes invisible — noticed only when lost. "Boring" and "stopped loving" are mechanistically different states.

*Source: Love-Romantic.md v3.0. Research: Fisher 2004, Gottman, Aron 2000.*

---

## Three more — brief mechanism sketches

### Humans can't sit still

The human brain runs a compilable architecture — a general-purpose system that must have input to compile. Hardwired organisms (insects) can idle between stimuli. Humans can't: when all channels are static, the body fires dissonance — "resources available but unused." This is boredom, and it's architectural. Billionaires can't sit still because money fills resource-access gaps but not discovery, creation, or mastery gaps. The gap types change; the drive doesn't stop.

*Source: Boredom.md v2.1, Inter-Body-Mechanism.md §1.2.*

### Status competition across species

Status isn't "who's superior." The framework defines it as a resource access map: "with this person, in this context, what can I access without fighting?" Evolutionary logic: fight once, remember, reuse for thousands of interactions. The payoff ratio is so massive that every social species converged on the same mechanism. The biochemistry is conserved across ~350 million years.

*Source: Status.md v2.2. Research: Sapolsky field study, Huber & Kravitz 2005.*

### Creative stress — the system working as designed

Creativity = opening gaps in your model. Gap detected → cortisol mobilizes. This is the change-readiness amplifier, not damage. PFC Fresh processing costs real resources: glucose, working memory slots, sustained cortisol. The Inverted-U marks the boundary: enough cortisol to signal urgency, not enough to lock PFC into threat mode.

When does it harm? When the source shifts from creative approach to deadline panic — same molecule, different mobilization direction. Or when sustained without repair.

*Source: Cortisol-Baseline.md v2.1. Research: Yerkes-Dodson, Reyes et al. 2020.*

---

## What this framework is

Think of it like a computer: the framework provides a circuit diagram (which brain structures do what) and a software architecture (how the cycle runs).

**Scale:** 200+ analysis files, CC0 licensed. One author, iterated across 60+ sessions.

**Structure:** Each mechanism has its own file with explicit dependencies, confidence levels per claim (🟢 research-supported, 🟡 framework synthesis, 🔴 hypothesis), and tracked open questions.

**Core:** The cycle runs Domain → Body-Input → Unconscious → Feeling → PFC → Body-Output → Domain. Everything runs on compiled body-level patterns ("chunks"). The PFC observes and orchestrates — it never compiles directly.

**Philosophy:** Compass, not GPS — estimates direction, not exact prediction.

**Language:** Vietnamese primary with English technical terms. For navigation, drop the folder into a large-context AI and ask questions in any language.

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

**I'm not a neuroscientist.** Background: game development. Independent researcher, no institutional affiliation. Evaluate the evidence, not the credentials.

**Hypothesis, not theory.** The individual findings are established science. The connections between them — the unified architecture — are proposed, not proven. That's what needs testing.

**The biggest blackbox is the substrate.** The framework models behavior in "chunks" — compiled body-level patterns. What a chunk IS physically — the neural substrate — is postulated, not identified. This is the framework's weakest point and biggest open question.

**Vietnamese primary language.** The full framework (200+ files) is in Vietnamese with English technical terms. AI navigation bridges the gap effectively.

**Confirmation bias applies here too.** The framework itself predicts that reading it will bias you toward confirming evidence.

---

## What I'm looking for

**Stress-test it with AI.** Clone the repository. Drop the entire folder into a large-context AI (Claude Opus recommended). Start with Ask-AI.md — it contains the reading order and interaction protocol. Then check specific claims against cited research, or ask personal questions and see whether the mechanism-level answers match your experience.

**Find where it breaks.** The most valuable contribution is a well-documented case where the framework's prediction doesn't match observation — or where a cited paper doesn't actually support the claimed mechanism.

**If you have domain expertise:** Neuroscience — verify biological mechanisms. Psychology — test behavioral predictions. Philosophy of science — are claims properly falsifiable? Education — does the 3-compile-type model match observations? Anyone — test against your own experience, report what doesn't fit.

**Counter-evidence is more valuable than confirmation.** Our brains are wired to confirm. If something doesn't fit, that's the most useful thing you can share.

---

Full framework (200+ files, CC0, open-source):
**[GitHub — Human Predictive Drive](https://github.com/hoanispof/Human-Predictive-Drive)**

Three detailed blog posts on specific mechanisms:
- [Dopamine Signals Salience, Not Reward](https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/) — a 7-step mechanism + five preconditions for when pleasure actually fires
- [Cortisol Is Not Your Stress Hormone](https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/) — the Source > Level principle + the Inverted-U
- [ADHD Is Not Attention Deficit](https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/) — one threshold, six paradoxes resolved

This is a hypothesis inviting falsification. What would break it? I want to know.
