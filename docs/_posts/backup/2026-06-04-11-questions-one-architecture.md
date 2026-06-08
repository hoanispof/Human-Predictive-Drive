---
layout: post
title: "11 Questions About Human Behavior — Mechanistic Answers from One Architecture"
date: 2026-06-04
author: Independent researcher
license: CC0 1.0 Universal
status: Draft v0.1
tags: [neuroscience, psychology, evolutionary-biology, cognitive-science, open-source, behavioral-science, framework]
---

**An open-source framework mapping brain mechanisms across 200+ files — with mechanistic answers to 11 questions, research citations, and explicit conditions for being wrong.**

---

## Summary

This post presents:

1. **A cross-domain framework** connecting neuroscience, psychology, and evolutionary biology into an architecture — 200+ source files with explicit dependencies, open-source, CC0
2. **Eleven questions** with mechanistic answers — from why social media drains you to why limerence ends
3. **Six mechanism sketches** with research citations — three expanded, three brief
4. **One question cluster** — five seemingly unrelated experiences that trace to one architectural fact about the human body
5. **Four positions** where the framework diverges from mainstream accounts — each with evidence and conditions for being wrong
6. **Explicit limitations** — including what the author doesn't know and where the framework is weakest

**Epistemic status:** Hypothesis inviting falsification. Builds on established research (Berridge, Sapolsky, Schultz, Damasio, Hebb). The individual findings are settled science; the proposed connections between them are new and unvalidated. Seeking stress-testing — especially from domain experts.

---

I cross-referenced neuroscience, psychology, and evolutionary biology research and mapped the connections between the brain's core systems into an open-source framework.
From opioid-dopamine signaling, through body-level evaluation of threat, novelty, status, and connection, to collective behavior.
200+ files, structured like a codebase: files per mechanism, explicit dependencies, confidence levels per claim, open questions tracked like issues.

The framework takes one architectural position: the body evaluates first, the prefrontal cortex observes second. Most of what we call "behavior" runs on compiled body-level patterns — the conscious mind is more like a monitoring process than the main thread. This one premise, applied consistently, produces surprisingly specific answers to questions that normally get vague or circular explanations.

Unlike a textbook, the framework doesn't present conclusions — it maps mechanisms with explicit dependencies between them, marks where it's uncertain, and tracks what it doesn't yet know.

The full framework is available at **[GitHub — Human Predictive Drive](https://github.com/hoanispof/Human-Predictive-Drive)** (200+ files, CC0). The rest of this post walks through 11 questions the framework answers — with mechanism sketches and research citations.

---

## Questions

- Why does scrolling social media for an hour leave you drained — when a 30-minute conversation with a close friend energizes you?
- Why can't humans sit still — not even billionaires with nothing left to prove?
- Why do humans compete for status — and why does the underlying mechanism look the same in lobsters, baboons, and CEOs?
- Why does creative work come with stress — even when you chose it and love it? And when does that stress become genuinely harmful?
- Why is forced analytical thinking sometimes unproductive — while a split-second expert decision is often right?
- Why does limerence (the "falling in love" phase) produce genuine bliss — and why is it biologically guaranteed to end? What sustains a bond after the biochemical subsidy expires?

> Five more — each about how other people affect the body:
>- Why does a single critical comment online cause real anxiety — even from someone you'll never meet?
>- Why does betrayal by someone close cause genuine physical pain — when your body wasn't touched?
>- Why does being around a calm person make you calmer — without them saying a word?
>- Why does chronic loneliness genuinely damage your health — not just your mood?
>- Why does a crowd's energy sweep you up — even when you rationally don't care about the game?
>
> The framework traces all five to one architectural fact about the human body.

These are samples, not scope — the architecture covers any question about human behavior that traces to body-level mechanisms.  
Each question above traces to a specific mechanism in the framework, with citations, confidence levels, and conditions under which the answer would be wrong.  

---

## How the framework answers these

### Social media drains, close friend energizes

The framework identifies 8 pathways through which the body registers connection — including co-regulation (cortisol buffering through trusted presence), contingent responsiveness (the other person reacts to *you*, in real time), and multi-sensory presence signal.

A conversation with a close friend activates most of these simultaneously. The body detects a trusted entity — someone whose patterns are already compiled into your neural architecture through hundreds of hours of shared experience. Oxytocin modulates cortisol ("social buffering" — Coan 2015), and the opioid system fires genuine reward. The friendship is doing something measurable: the body literally runs at lower metabolic cost in trusted company.

Even a conversation with a stranger is better than social media — a stranger still provides contingent responsiveness and physical presence. But a close friend goes deeper: compiled trust means the body doesn't spend resources evaluating threat, freeing capacity for genuine connection.

Social media activates 3–4 pathways at surface level only. The critical missing element: body-level presence. Without voice tone, facial micro-expressions, and contingent response, the body stays in a "socially unfed" state despite high engagement.

The core distinction: dopamine tracks "something prediction-relevant changed" (wanting); opioid tracks "something genuinely matched a body-level need" (liking). Social media fires the first without the second. The body's verdict after an hour: high alertness, low nourishment.

*Source: Connection.md v5.0. Research: Coan 2015, Holt-Lunstad 2015, Tronick 1978.*

### Expert decisions vs. forced thinking

The brain compiles knowledge through experience. Repeated exposure to domain feedback — debugging code, tasting food, reading patients — builds body-level patterns that fire automatically: near-instant, near-zero cost. This is what Klein (1998) documented as recognition-primed decisions: experts don't weigh options — they recognize patterns.

The mechanism is domain-universal. The senior architect "sees" the bug instantly. The experienced chef tastes and "knows" what's missing. The clinician looks at the patient and "senses" something wrong before any conscious analysis. Same mechanism, different compiled domains — each firing at near-zero cost, each built through thousands of hours of domain-specific feedback.

The PFC (conscious analytical mind) runs differently: ~4 working memory slots, high glucose cost, sustained cortisol. When the domain has no compiled base to draw from, the PFC must draft everything from scratch — expensive, slow, error-prone.

The framework identifies this as the real axis: compiled processing (body-direct, domain-specific, fast) vs. fresh processing (PFC-drafted, general-purpose, costly). This reframes Kahneman's System 1/2: the key variable is not fast vs. slow — it's whether the domain has a compiled base. System 1 with compiled domain expertise is accurate *and* fast. System 2 without a compiled base is expensive *and* unreliable.

But compiled doesn't mean correct — it means untested assumptions feel identical to verified expertise. Domain reality is the only arbiter. The body rewards results, not effort.

*Source: Body-Knowing.md v1.0, Compile-Taxonomy.md v3.0. Research: Klein 1998, Kahneman 2011, Ericsson 1993.*

### Limerence (the "falling in love" phase) — why it ends, what sustains the bond

Limerence isn't illusion — it's drive-level biology. Fisher (2004) showed it activates the same neural systems as hunger and thirst. The body provides a temporary biochemical boost: dopamine surge (intense wanting), norepinephrine (hyperarousal), oxytocin (bonding), reduced serotonin (obsessive focus on the partner), and selectively lowered PFC evaluation (overlooking flaws). Multiple reward systems fire simultaneously — producing the strongest compound reward humans experience.

It's guaranteed to end because the boost is temporary by design: 18–36 months (Fisher 2004). Its evolutionary function is to keep two strangers together long enough to bond. Once the window closes, accumulated habituation reveals at once — "the spark died" is biochemical subsidy expiry, not stopped loving.

The framework maps this decline to two forces. First, self-suppression: each partner suppresses personal drives to match the other — less individual growth means less novelty to bring back into the relationship. Second, familiarity habituation: the partner's presence, repeated thousands of times, produces diminishing reward. Both are architectural — they happen to *every* pair bond, not just "bad" ones.

What sustains a bond afterward? The limerence window is fuel for building durable structures: shared experiences that compile into both people's body-level patterns, communication patterns for resolving conflict (Gottman: the most stable couples aren't conflict-free — they know how to repair), and deep mutual understanding built during peak curiosity.

Post-limerence, the dynamic shifts: novelty-based reward requires active effort (Aron 2000), while baseline warmth becomes invisible — noticed only when lost. "Boring" and "stopped loving" are different states — the first means novelty dropped while the structural bond holds; the second means the structural bond itself has eroded.

*Source: Love-Romantic.md v3.0, Bond-Architecture.md v2.0. Research: Fisher 2004, Gottman, Aron 2000.*

---

## Three more — brief mechanism sketches

### Humans can't sit still

The human brain runs a compilable architecture — a general-purpose system that must have input to compile. Hardwired organisms (insects) can idle between stimuli. Humans can't: when all channels are static, the body fires dissonance — "resources available but unused." This is boredom, and it's architectural, not psychological.

Billionaires can't sit still because money fills resource-access gaps but not discovery, creation, or mastery gaps. The gap types change with wealth; the drive doesn't stop. Even rest isn't idle — the body runs repair and consolidation. A compilable architecture has no OFF state.

*Source: Boredom.md v2.1, Inter-Body-Mechanism.md §1.2.*

### Status competition across species

Status isn't "who's superior." The framework defines it as a resource access map: "with this person, in this context, what can I access without fighting?" Evolutionary logic: fight once, remember, reuse for thousands of interactions. The payoff ratio is so massive that every social species converged on the same mechanism. The biochemistry — serotonin modulating posture and confidence — is conserved across ~350 million years.

Humans add complexity: multiple status dimensions (professional, social, intellectual), per-person per-context maps, and PFC override capability. But the substrate remains ancient.

*Source: Status.md v2.2. Research: Sapolsky field study, Huber & Kravitz 2005.*

### Creative stress — the system working as designed

Creativity = opening gaps in your model. Gap detected → cortisol mobilizes. This is the change-readiness amplifier, not damage. PFC fresh processing costs real resources: glucose, working memory slots, sustained cortisol. The Inverted-U marks the boundary: enough cortisol to signal urgency, not enough to lock PFC into threat mode.

When does it harm? When the source shifts from creative approach to deadline panic — same molecule, different mobilization direction. Or when sustained without repair — the body shifts from mobilized to depleted. "Trying harder" past the Inverted-U peak produces *worse* performance, not better.

*Source: Cortisol-Baseline.md v2.1. Research: Yerkes-Dodson, Reyes et al. 2020.*

---

## The cluster — one architectural fact

The five questions above — criticism anxiety, betrayal pain, calm contagion, loneliness damage, crowd energy — trace to one architectural fact: **social connection is a body-base requirement, not a preference.**

The human brain runs a compilable architecture — a general-purpose system that must learn everything from experience rather than having it hardwired. This architecture takes 15–20 years to compile, during which the organism depends entirely on other people for survival. Evolution solved this with hardwired social circuitry: oxytocin for bonding, mu-opioid for social reward, and — critically — the reuse of physical pain circuits for social pain.

Eisenberger (2003) demonstrated that social rejection activates the dorsal anterior cingulate cortex — the same region that processes physical pain. This is not metaphor. The body treats social loss as physical damage because, for a compilable architecture, losing access to other people *is* structural damage.

Coan's Social Baseline Theory (2015) takes it further: the body's default state is *with others*. Being alone is the deviation — metabolically costly, requiring extra vigilance and self-regulation that the body normally outsources to trusted companions.

Chronic loneliness — sustained absence of meaningful social input — doesn't just feel bad. It damages health. Holt-Lunstad's 2015 meta-analysis found 26% increased mortality from social isolation. Holt-Lunstad herself characterized the effect size as comparable to smoking up to 15 cigarettes per day — a cross-review comparison of mortality risk magnitudes, not a direct biological equivalence.

Temporary solitude with compiled connections intact is different — a scientist deep in research or a monk in meditation still has compiled social bonds to return to.

Close relationships go deepest: after hundreds of hours, another person's patterns compile into your neural architecture. They become body-base extensions — which is why betrayal causes somatic distress, why calm presence regulates without words, and why a crowd's synchrony bypasses rational evaluation.

The five questions are five expressions of this one fact. The source files map the full mechanism.

---

## What this framework is

Think of it like a computer: the framework provides a circuit diagram (which brain structures do what) and a software architecture (how the cycle runs).

**Scale:** 200+ source files with explicit dependencies, open-source, CC0.

**Structure:** Each mechanism has its own file with explicit dependencies, confidence levels per claim (🟢 research-supported, 🟡 framework synthesis, 🔴 hypothesis), and tracked open questions.

**Core:** The cycle runs Domain → Body-Input → Unconscious → Feeling → PFC → Body-Output → Domain. Everything runs on compiled body-level patterns ("chunks"). The PFC observes and orchestrates — it never compiles directly.

**Philosophy:** Compass, not GPS — estimates direction, not exact prediction.

---

## Where this diverges from mainstream

The framework agrees with mainstream neuroscience and psychology at most positions. It diverges at approximately 20 specific points — each documented with the mainstream claim, the framework's position, cited evidence, and conditions under which the framework is wrong.

Four examples:

**Dopamine ≠ reward.** Mainstream: "dopamine = reward chemical." Framework: dopamine is a salience signal — "something prediction-relevant changed." Reward is mediated by the opioid system under 5 specific preconditions. Depleting dopamine doesn't eliminate pleasure (Berridge & Robinson 1998). Blocking opioids eliminates euphoria while dopamine fires normally (Jayaram-Lindström et al. 2017).

**Cortisol ≠ stress hormone.** Mainstream: "reduce cortisol = reduce stress." Framework: cortisol is a change-readiness amplifier. Zero cortisol is a medical emergency (Addison's disease), not bliss. What determines outcome is source direction and repair balance, not level. Injecting cortisol doesn't produce stress (Reyes et al. 2020, n=46, placebo-controlled).

**Conscious mind ≠ controller.** Mainstream: "willpower controls behavior." Framework: PFC influence ≈ 5%. Body-compiled patterns ≈ 95%. "Knowing but not doing" is two separate systems reaching different conclusions, not willpower failure. Neural activity precedes conscious decision by 500ms–7s (Libet 1983, Soon et al. 2008).

**Prediction error: necessary, not sufficient.** Mainstream (ML/RL): "prediction error drives reward." Framework: prediction error drives attention — necessary first step, but human reward requires additional body-level evaluation. Unexpected loud noise produces prediction error without reward.

The full list of ~20 positions with cited evidence: Ask-AI.md §3 in the repository.

---

## Honest limitations

**I'm not a neuroscientist.** Background: game developer. Independent researcher, no institutional affiliation. Evaluate the evidence, not the credentials.

**Built on personal observation and AI synthesis.** Cross-referenced against published research, with AI used for synthesis across disciplines. A method that can surface cross-disciplinary connections, but also carries risk of individual bias.

**Hypothesis, not theory.** The individual findings are established science. The connections between them — the unified architecture — are proposed, not proven. That's what needs testing.

**The biggest blackbox is the substrate.** The framework models behavior in "chunks" — compiled body-level patterns. What a chunk IS physically — the neural substrate — is postulated, not identified. This is the framework's weakest point and biggest open question.

---

## Getting started

**Stress-test it with AI.** Clone the repository. Drop the entire folder into a large-context AI (Claude Opus recommended — the framework is 200+ files and benefits from full-context reasoning). Start with Ask-AI.md — it contains the reading order, key files per topic, and interaction protocol.

Starter prompt:

> *Read Ask-AI.md first. Then read Core-Software.md for the overall architecture. I want to understand [your topic]. Walk me through the mechanism, cite the specific files, and flag any claims marked 🔴 (hypothesis) vs 🟢 (research-supported).*

Suggested starting files by interest:

- Dopamine and reward → Dopamine-Is-Not-Reward.md
- Social connection → Connection.md
- Learning and expertise → Body-Knowing.md, Compile-Taxonomy.md
- Emotions and feelings → Feeling.md, Body-Feedback-Mechanism.md
- Motivation and drive → Core-Software.md, Gap-Direction.md
- Love and relationships → Love-Romantic.md
- Full architecture → start with Core-Software.md

AI can verify logical consistency and citation accuracy. It cannot verify replication status or methodology quality — that requires domain expertise.

**Find where it breaks.** The most valuable contribution is a well-documented case where the framework's prediction doesn't match observation — or where a cited paper doesn't actually support the claimed mechanism.

**If you have domain expertise:**
- **Neuroscience** — verify biological mechanisms. Do the cited papers say what the framework claims?
- **Psychology** — test behavioral predictions against clinical or experimental observation.
- **Philosophy of science** — are claims properly falsifiable? Are confidence levels calibrated?
- **Education** — does the 3-compile-type model match how learning actually works?
- **AI/ML** — does the wanting/liking distinction map to current reward modeling gaps?
- **Anyone** — test against your own experience. Report what doesn't fit.

**Counter-evidence is more valuable than confirmation.** The framework itself predicts that reading it will bias you toward confirming evidence. If something doesn't fit, that's the most useful thing you can share.

---

Full framework (200+ files, CC0, open-source):
**[GitHub — Human Predictive Drive](https://github.com/hoanispof/Human-Predictive-Drive)**

Related posts on specific mechanisms:
- [Dopamine Signals Salience, Not Reward](https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/) — a 7-step mechanism + five preconditions for when pleasure actually fires
- [Cortisol Is Not Your Stress Hormone](https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/) — the Source > Level principle + the Inverted-U
- [ADHD Is Not Attention Deficit](https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/) — one threshold, six paradoxes resolved
- [Logic Is Not the Opposite of Intuition](https://hoanispof.github.io/Human-Predictive-Drive/blog/logic-is-not-the-opposite-of-intuition/) — one process, two observer labels, and why neither can verify itself

This is a hypothesis inviting falsification. What would break it? I want to know.
