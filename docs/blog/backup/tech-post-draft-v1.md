---
title: "[SEE TITLE OPTIONS BELOW]"
date: 2026-05-31
author: Independent researcher
license: CC0 1.0 Universal
status: Draft v0.1
target: LessWrong (primary), r/slatestarcodex (secondary)
tags: [neuroscience, cognitive-science, open-source, falsifiable, behavioral-science]
notes: |
  FULL DRAFT — all raw materials included at maximum quality.
  User will trim manually for final version.
  Angle E: Build → Trending Questions → Invite
  Anti-patterns checked: W.4 (no self-help), no guru tone, no marketing, no grand claims.
---

# TITLE OPTIONS (chọn 1)

**Option A — Descriptive:**
> I mapped how the brain's core systems connect — 200+ files, open-source, inviting falsification

**Option B — Question-led:**
> An open-source framework mapping brain mechanisms — from dopamine signaling to social behavior. Seeking stress-testing.

**Option C — Project pitch:**
> 200+ files mapping human brain architecture: an open-source hypothesis seeking reviewers

**Option D — LessWrong native:**
> Cross-referencing neuroscience research into a unified framework: 200+ files, CC0, structured for falsification

---

# [CHOSEN TITLE]

**Epistemic status:** Hypothesis inviting falsification. Builds on established research (Berridge, Sapolsky, Schultz, Damasio, Hebb). The individual findings are settled science; the proposed connections between them are new and unvalidated. 200+ files, CC0. Seeking stress-testing — especially from domain experts.

---

## HOOK — VERSION A (V3-hybrid: scope + structure + differentiators)

I cross-referenced neuroscience research and mapped the connections between the brain's core systems — from dopamine signaling to social behavior — into a 200+-file open-source framework. Structured like a codebase: files per mechanism, explicit dependencies, confidence levels per claim, open questions tracked like issues. CC0 licensed.

The framework takes a specific architectural position: the body evaluates first, the prefrontal cortex observes second. Most of what we call "behavior" runs on compiled body-level patterns — the conscious mind is more like a monitoring process than the main thread. This one premise, applied consistently, produces surprisingly specific answers to questions that normally get vague or circular explanations.

## HOOK — VERSION B (V1i: scope + "unlike a textbook")

I cross-referenced neuroscience research across domains and mapped the connections into a single framework — from dopamine signaling to social behavior. 200+ files, open-source. What makes it different from a textbook: each claim has confidence levels, dependencies between mechanisms are explicit, and open questions are tracked like issues.

The framework diverges from mainstream at about 20 specific positions — each with cited evidence and explicit falsification criteria. It's not a claim that textbooks are wrong across the board. It's a claim that at approximately 20 specific points, the popular model and the research have diverged, and the consequences of that divergence matter.

---

## The questions

The framework provides mechanistic answers to questions like:

**Why does scrolling social media for an hour leave you drained — when a 30-minute real conversation energizes you?**

**Why does discovering something yourself feel completely different from being told the same thing — even when the information is identical?**

**Why is boredom painful? Nothing is happening — why does the brain treat that as a problem?**

**Why do humans compete for status — and why does the underlying mechanism look the same in lobsters, baboons, and CEOs?**

**Why does giving to charity feel good but owing someone a favor feels heavy — even when the action is identical?**

**Why does creative work come with stress — even when you chose it and love it?**

These aren't rhetorical. Each has a specific mechanistic answer in the framework, with citations, confidence levels, and conditions under which the answer would be wrong.

Here's what three of those answers look like.

---

## How the framework answers these — three examples

### Social media drains, conversation energizes

The framework identifies 8 specific pathways through which the body registers connection: empathy simulation, co-regulation (cortisol buffering through trusted physical presence), shared problem-solving, giving, being seen (contingent responsiveness), presence signal (multi-sensory body-level data), shared direction, and knowledge exchange.

A real conversation activates most of these simultaneously. The body detects contingent responsiveness — the other person reacts to YOU specifically, in real time — and the opioid system fires genuine reward. Oxytocin modulates cortisol, creating what the literature calls "social buffering" (Coan 2015, Social Baseline Theory).

Social media activates 3–4 of these pathways, at surface level only. The critical missing element: body-level presence signal. Without multi-sensory input — voice tone, facial micro-expressions, physical proximity — the body remains in a "socially unfed" state despite high engagement. Your feed optimizes for dopamine (novelty detection, salience). But the body measures satisfaction through the opioid system — which requires depth and contingent responsiveness, not volume and novelty.

The distinction maps directly to the framework's core separation: dopamine tracks "something prediction-relevant changed" (wanting); opioid tracks "something genuinely matched a body-level need" (liking). Social media fires the first without the second. The body's assessment after an hour: high alertness, low nourishment.

*Source: Connection.md v5.0 — 3 Generative Primitives, 8 pathways, Hardware Subsidy model. Research: Coan 2015, Holt-Lunstad 2015, Tronick 1978.*

### Discovering vs. being told

The brain compiles knowledge through at least three distinct pathways — and the pathway determines durability, not the content.

**Experience Compile:** You encounter something directly. The body wires it through multiple sensory channels simultaneously — visual, proprioceptive, emotional. The amygdala pathway begins encoding at ~12ms, before conscious awareness (LeDoux 1996). Co-firing across channels creates lasting synaptic strength (Hebb 1949). The result: durable, automatic, context-triggered. Debugging a production crash teaches you something permanent.

**Trust Compile:** Someone tells you; you believe them. One or two channels active (typically auditory, maybe visual credibility of the source). The body installs a short chain — [told → accept] — without verifying the full causal reasoning. Fast and efficient, but fragile. It works until the authority source changes, the context shifts, or an edge case appears.

**Expertise Compile:** Deliberate practice — PFC directs attention, body repeatedly encounters domain feedback, patterns crystallize over years. This is the slowest but most precisely calibrated pathway (Ericsson 1993).

Discovery = Experience Compile. Being told = Trust Compile. Same information, different encoding pathway, different durability. The body doesn't tag where knowledge came from (the framework calls this "no source tag" — Chunk.md §1.1). So trust-compiled knowledge *feels* exactly like experience-compiled knowledge — until it's tested under pressure.

This explains a phenomenon every programmer knows: Stack Overflow copy-paste works until the edge case. A production incident is never forgotten. Same concept, different compile pathway, different persistence.

*Source: Compile-Taxonomy.md v2.0 — 3 Compile Types, 4 pathways, 6 trade-offs. Research: Hebb 1949, LeDoux 1996, Ericsson 1993, Squire 1992.*

### Boredom is painful

The human brain is a compilable architecture — a general-purpose system that needs input to process and compile into patterns. Hardwired organisms (insects with fixed stimulus-response) don't experience boredom. They don't have a general-purpose system that can be idle.

When all your input channels are static — no active gap to fill, no novelty to process, no problem to solve — the compilable system has nothing to compile. The body fires dissonance: "resources available but unused." This is boredom.

The framework identifies 6 specific sources of this dissonance: sensory channels monotonous, motor system unused, social input absent, forced activity mismatch, direction lacking, and expected reward from a specific source stopped. All six produce the same body signal, which is why the same word — "bored" — covers everything from "bored alone on a Sunday" to "bored in a relationship" to "bored at work." Different source, same body-feedback pattern.

The unified formula: Boredom = body-feedback dissonance + Imagine-Final insufficient (no clear direction the body is willing to commit to). Remove either component and it's no longer boredom — it's either drive (dissonance + clear direction) or contentment (no dissonance).

The civilization implication is structural: pre-modern humans rarely experienced boredom because survival demands continuously filled hardware-level gaps. Modern abundance satisfies basic gaps, leaving the compilable system idle — which generates higher-level gaps (career meaning, creative expression, relational novelty) that are harder and slower to fill. Boredom increases with civilization. This is architectural, not a character flaw.

*Source: Boredom.md v2.0 — 6 sources, Compilable Architecture, threshold model, abundance hypothesis. Research: body-feedback mechanism → Inter-Body-Mechanism.md v1.0 §1.2.*

---

## Three more questions — brief mechanism sketches

These are shorter — enough to see the framework has a specific answer, not enough to evaluate it fully. The full mechanism with citations is in the linked files.

### Status competition looks the same across species

Status is not "who's superior." The framework defines it as a resource access map: "with this person, in this context, what can I access without fighting?"

The evolutionary logic is cost-benefit: 20 monkeys eating 20 times a day = 400 potential fights daily. Solution: fight once, remember the result, reuse that calibration for thousands of interactions. The payoff ratio is so massive that every social species — from lobsters to chickens to baboons to humans — has converged on the same basic mechanism.

The biochemistry is conserved across ~350 million years. Winner lobster: serotonin increases, posture expands, confident behavior (Huber & Kravitz 2005). Winner baboon: serotonin up, cortisol down, access to food and mates increases (Sapolsky, 30+ year field study). Humans add complexity — multiple dimensions, per-person per-context maps, conscious override — but the substrate is ancient.

*Source: Status.md v2.2 — Resource Access Map, evolutionary cost-benefit, cross-species spectrum.*

### Charity feels good, obligation feels heavy — same action

Same action (giving $100), different prediction pathway. Charity: body predicts zero future obligation — pure reward fires (opioid + positive valence update). No cost-tracking activated. Fire and forget.

Obligation: body predicts uncertain future cost. Cortisol holding fires. PFC allocates a "pending obligation" monitoring slot. The framework identifies a 5-factor formula driving obligation intensity — and the key insight is that *unclear* cost and *unclear* endpoint make it heavier than large but explicit costs. An implicit social debt ("I owe you one") often feels heavier than a financial loan with a number and a deadline.

The body tracks social exchange mechanically, not morally. This is why the same person doing the same kind act can feel entirely different depending on whether you asked for it, expected it, or were surprised by it.

*Source: Obligation.md v1.2 — 5-factor formula, 6 obligation types. Gratitude.md v2.1 — pure reward pathway.*

### Creative work comes with stress

Creativity means opening gaps — your model has a hole and you're building something to fill it. Gap detected → cortisol mobilizes. But this is the change-readiness amplifier, not damage.

PFC Fresh processing — drafting novel solutions, holding multiple options, suppressing premature closure — costs real metabolic resources: glucose, sustained cortisol, working memory slots. The Inverted-U (Yerkes-Dodson, with a proposed mechanism: repair × damage balance) explains the sweet spot: enough cortisol to signal urgency, not enough to lock PFC into threat mode. That sweet spot is what productive creative tension feels like.

Stress during creative work is the system working as designed. Same cortisol molecule, different source direction: creativity (approach) vs. deadline panic (avoidance) produce measurably different outcomes — not because the chemistry differs, but because what the cortisol is *mobilizing for* differs.

*Source: Cortisol-Baseline.md v2.2 — change-readiness amplifier, Source > Level principle. Body-Feedback-Mechanism.md v2.0.*

---

## What this framework is

**Scale:** 200+ analysis files, version 7.8 (2026). One author, iterated across 60+ sessions.

**Coverage:** The framework maps a path from neurochemistry (dopamine, cortisol, opioid, serotonin, oxytocin) through individual behavior (learning, motivation, emotion, decision-making) to social dynamics (connection, status, obligation, empathy, collective patterns) and applied domains (education, AI interaction, addiction, OCD, religion, climate cognition).

**Structure:** Each mechanism has its own file. Dependencies between mechanisms are explicit (file headers list what each file depends on). Confidence levels are marked per claim: 🟢 = research-supported, 🟡 = framework synthesis (consistent with evidence but not independently validated), 🔴 = hypothesis. Open questions are tracked within each file, like issues.

**Architecture:** The framework takes a body-first position. The cycle runs: Domain → Body-Input → Unconscious Processing → Feeling → PFC → Body-Output → Domain. Everything runs on "chunks" — compiled body-level patterns that fire automatically. The PFC observes and orchestrates indirectly but never compiles directly. Conscious effort accounts for roughly 5% of behavioral influence; compiled body-level patterns account for the rest.

**License:** CC0 1.0 — Public Domain. Use, share, adapt freely. No permission needed. No credit required.

**Language:** Primary language is Vietnamese with English technical terminology. The README and blog posts are in English. For the full framework, you can navigate via AI — drop the folder into a large-context AI (Claude Opus recommended, 1M context) and ask questions in any language.

---

## Where this diverges from mainstream

The framework agrees with mainstream neuroscience and psychology at most positions. It diverges at approximately 20 specific points — each documented with the mainstream position, the framework's position, cited evidence, and falsification criteria.

Four examples:

**Dopamine ≠ reward.** Mainstream: "dopamine = the reward chemical." Framework: dopamine is a salience signal — "something prediction-relevant changed." Reward is mediated by the opioid system under 5 specific preconditions. Evidence: depleting dopamine doesn't eliminate pleasure (Berridge & Robinson 1998); blocking opioids eliminates euphoria while dopamine fires normally (Jayaram-Lindström et al. 2017).

**Cortisol ≠ stress hormone.** Mainstream: "reduce cortisol = reduce stress." Framework: cortisol is a change-readiness amplifier. Zero cortisol is dangerous (Addison's disease), not blissful. What matters is source direction and repair balance, not level. Evidence: injecting cortisol doesn't produce stress (Reyes et al. 2020, n=46, placebo-controlled).

**PFC ≠ controller.** Mainstream: "willpower controls behavior." Framework: PFC accounts for ~5% of behavioral influence. Body-level compiled patterns account for ~95%. "Knowing but not doing" is not willpower failure — it's two separate systems (PFC assessment vs. body-compiled behavior) reaching different conclusions. Evidence: neural activity precedes conscious decision by 500ms–7s (Libet 1983, Soon et al. 2008).

**Prediction error = necessary but insufficient for human reward.** Mainstream (in ML/RL): "prediction error drives reward." Framework: prediction error drives attention shifts — necessary first step, but human reward requires additional body-level evaluation under specific conditions. This is why unexpected loud noise produces prediction error but not reward.

The full list of ~20 divergent positions, with evidence and falsification criteria for each, is in the framework's Ask-AI.md §3.

---

## Honest limitations

**I'm not a neuroscientist.** My background is game development. I'm an independent researcher with no institutional affiliation. The framework should be evaluated on its evidence and internal consistency, not on credentials — but you should know the credentials.

**This is a hypothesis, not a theory.** The individual research findings it builds on are established science. The connections between them — the unified architecture — are proposed, not proven. That's what needs testing.

**The biggest blackbox is the substrate.** The framework models behavior in terms of "chunks" — compiled body-level patterns. But what a chunk IS physically — the neural substrate — is postulated, not identified. This is the framework's weakest point and its biggest open question.

**Primary language is Vietnamese.** The README, blog posts, and key documentation are in English. The full 200+-file framework is in Vietnamese with English technical terms. For English-speaking readers, AI navigation works well: drop the folder into Claude Opus and ask questions in English.

**Numbers are calibration anchors, not measurements.** When the framework says "PFC ~5%," this means: the direction is clear (PFC influence is small relative to body-compiled patterns) and the order of magnitude is indicative, but the exact percentage varies by person and context. The insight is in the direction and proportion, not the precise number.

**Crowd-sourced verification ≠ peer review.** AI can check logical consistency and citation accuracy. It cannot check replication status, methodology quality, or whether the interpretation of data is correct. AI verification is useful but insufficient — domain expert review is what this framework needs most.

**Confirmation bias applies here too.** The framework predicts that reading it will make you notice confirming evidence more often (attention filtered by newly installed chunk patterns). Counter-evidence is more valuable than confirmation precisely because confirmation is easy to find.

---

## What I'm looking for

**Stress-test it.** Clone the repo. Drop it into a large-context AI. Ask the AI to check specific claims against the cited research. A verification guide is available in the repository.

**Find where it breaks.** The most valuable contribution is a well-documented case where the framework's prediction doesn't match your observation — or where a cited paper doesn't support the claimed mechanism. Every falsification sharpens the model.

**Domain experts:** The framework makes specific claims about neurochemistry, behavioral psychology, learning mechanisms, and social dynamics. Each domain has claims flagged for review. If you have expertise in any of these areas, the framework needs your scrutiny more than your agreement.

**Counter-evidence is more valuable than confirmation.** Confirmation is easy to find — our brains are wired for it. If you find something that doesn't fit, that's the most useful thing you can share.

---

Full framework (200+ files, CC0, open-source):
[GitHub — Human Predictive Drive](https://github.com/hoanispof/Human-Predictive-Drive)

Three detailed blog posts on specific mechanisms:
- [Dopamine Is Not Reward](link) — 28 years of evidence + a proposed 7-step mechanism
- [Cortisol Is Not Your Stress Hormone](link) — Source > Level principle + the Inverted-U
- [ADHD Is Not Attention Deficit](link) — One threshold, six paradoxes resolved

This is a hypothesis inviting falsification. What would break it? I want to know.
