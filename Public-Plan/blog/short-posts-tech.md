---
title: Short Posts — Framework Overview for Tech Experts
date: 2026-06-04
purpose: Short posts (~300-400 words) for forums, linking to the full blog post
status: Draft v0.1
blog_link: 2026-06-04-bridging-neuroscience-psychology.md
blog_url: https://hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/
platforms: LessWrong, Hacker News, r/cogsci, r/psychology
references:
  plan-tech-blog.md §4 — short post structure per-platform
  short-posts-dopamine.md — template pattern
  framing-engagement-value.md — 3-layer value model
  plan-tech-distribution.md §5 — posting cadence
---

# Short Posts: Framework Overview — Tech Expert Audience

> Each short post = AUDITION. The blog = FULL PERFORMANCE.
> If the audition fails (no engagement) → framing needs work.
> If the audition passes → traffic to blog → deeper engagement.

---

## Short Post A — LessWrong (~400 words, rationalist tone)

**Title:** Why can't you sit still? Why does criticism hurt physically? Why does limerence end? — A framework with mechanistic answers

**Body:**

I cross-referenced neuroscience, psychology, and evolutionary biology research and mapped the connections between the brain's core systems into an open-source framework — 200+ files, structured like a codebase: files per mechanism, explicit dependencies, confidence levels per claim, open questions tracked like issues. CC0 licensed.

The framework takes one architectural position: the body evaluates first, the prefrontal cortex observes second. Most of what we call "behavior" runs on compiled body-level patterns — the conscious mind is more like a monitoring process than the main thread.

This one premise, applied consistently, produces mechanistic answers to questions like:

- **Why does scrolling social media drain you — when a close friend energizes?** The framework identifies 8 pathways through which the body registers connection. Social media activates 3–4 at surface level. A close friend activates most simultaneously. Core distinction: dopamine tracks "something changed" (wanting); opioid tracks "something matched a body-level need" (liking). Social media fires wanting without liking.

- **Why is forced analytical thinking sometimes unproductive — while a split-second expert decision is often right?** Compiled processing (body-direct, domain-specific, near-zero cost) vs. fresh processing (PFC-drafted, general-purpose, expensive). This reframes Kahneman's System 1/2: the key variable is not fast vs. slow — it's whether the domain has a compiled base.

- **Why does limerence end?** A temporary hardware subsidy — dopamine, norepinephrine, oxytocin, reduced serotonin — lasting 18–36 months (Fisher 2004). Subsidy expiry, not stopped loving. The framework maps what sustains bonds afterward: compiled shared experience, conflict-repair patterns (Gottman), and active novelty (Aron 2000).

Five more questions — including a cluster of five seemingly unrelated experiences that the framework traces to one architectural fact about the human body — are in the full post.

The framework diverges from mainstream at approximately 20 specific points. Each divergence has the mainstream claim, the framework's position, cited evidence, and conditions for being wrong.

Full blog post (6 mechanism sketches, divergence points, honest limitations):
https://hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/

Full framework (200+ files, CC0):
https://github.com/hoanispof/Human-Predictive-Drive

Counter-evidence is more valuable than confirmation. The framework includes ~20 divergence points from mainstream, each with falsification criteria. Where does it break?

---

## Short Post B — Hacker News (~300 words, tech-native tone)

**Title:** Open-source framework mapping brain mechanisms: 200+ files, CC0, structured like a codebase

**Body:**

I built an open-source framework mapping how the brain's core systems connect — from dopamine signaling to social behavior. 200+ files. Structured like a codebase: each mechanism has its own file, dependencies are explicit, every claim has a confidence level (research-supported / framework synthesis / hypothesis), open questions are tracked like issues. CC0 licensed.

Core architectural position: the body evaluates first, the PFC observes second. Think monitoring process vs. main thread. Compiled body-level patterns run ~95% of behavior; the conscious mind orchestrates, it doesn't compile directly.

Applied consistently, this produces specific mechanistic answers to questions like:

- **Expert decisions vs. forced thinking:** Compiled processing (body-direct, domain-specific, near-zero cost) vs. fresh processing (PFC-drafted, ~4 working memory slots, high glucose cost). The senior dev "sees" the bug; the junior debugs for hours. Same codebase, different compiled base.

- **Creative stress:** Cortisol is a change-readiness amplifier, not damage. Creativity opens gaps → cortisol mobilizes. The Inverted-U marks the boundary. Past the peak, "trying harder" produces worse performance.

- **Social media drain:** Dopamine (wanting) fires without opioid (liking). The body's verdict: high alertness, low nourishment.

The framework diverges from mainstream at ~20 specific points — each documented with evidence and falsification criteria. Four examples: dopamine ≠ reward (Berridge 1998), cortisol ≠ stress (Reyes 2020), conscious mind ≠ controller (Libet 1983), prediction error ≠ reward (framework position).

Navigation: clone the repo, drop it into a large-context AI, start with Ask-AI.md.

Full blog post (11 questions, 6 mechanism sketches, limitations):
https://hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/

Framework (200+ files, CC0):
https://github.com/hoanispof/Human-Predictive-Drive

Find where it breaks.

---

## Short Post C — Reddit r/cogsci (~350 words, bridge tone)

**Title:** A proposed framework connecting neurochemistry, behavior, and social dynamics — 200+ files, open-source, seeking falsification

**Body:**

I've developed an open-source framework that maps connections between the brain's core systems — neurochemistry, behavior, learning, social dynamics — into a structured architecture. 200+ files, each with citations, confidence levels per claim, and tracked open questions. CC0 licensed.

The framework takes one architectural position: the body evaluates first, the prefrontal cortex observes second. Applied consistently, this produces mechanistic answers to questions that normally get vague explanations.

Three examples:

**Why does social media drain while a close friend energizes?** The framework identifies 8 pathways for registering connection. Social media activates 3–4 at surface level — dopamine (wanting) fires, but opioid (liking) requires contingent responsiveness, multi-sensory presence, and co-regulation (Coan 2015, Social Baseline Theory). Without these, the body stays "socially unfed" despite high engagement.

**Why does limerence end?** Fisher (2004) showed limerence activates drive-level systems (hunger, thirst level). The body provides a temporary hardware subsidy lasting 18–36 months. Subsidy expiry, not stopped loving. The framework maps what sustains bonds afterward — shared compiled experience, conflict-repair patterns (Gottman), active novelty (Aron 2000).

**A cluster of five questions** — criticism anxiety, betrayal pain, calm contagion, loneliness damage, crowd energy — trace to one architectural fact: social connection is a body-base requirement, not a preference. The evidence: social rejection activates dorsal ACC (Eisenberger 2003, same circuits as physical pain), chronic loneliness → 26% increased mortality (Holt-Lunstad 2015 meta-analysis).

The framework diverges from mainstream at approximately 20 specific points — including dopamine ≠ reward (Berridge 1998), cortisol ≠ stress hormone (Reyes 2020), and conscious mind ≠ controller (Libet 1983, Soon 2008). Each documented with evidence and falsification criteria.

Full blog post (6 mechanism sketches, divergence analysis, honest limitations):
https://hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/

Full framework (200+ files, CC0):
https://github.com/hoanispof/Human-Predictive-Drive

Counter-evidence is more valuable than confirmation. Where does this break?

---

## Short Post D — Reddit r/psychology (~300 words, accessible tone)

**Title:** Why does scrolling social media drain you? Why does criticism hurt physically? Why does limerence end? A framework with mechanistic answers

**Body:**

Why does scrolling social media for an hour leave you drained — when a conversation with a close friend energizes you? Why does a single critical comment online cause real anxiety — even from someone you'll never meet? Why does limerence produce genuine bliss — and why is it biologically guaranteed to end?

These questions normally get vague or circular answers. I've developed a framework that maps them to specific mechanisms.

The key distinction in the social media question: dopamine tracks "something changed" (wanting) — it fires with every new post. But the opioid system tracks "something matched a body-level need" (liking) — and requires contingent responsiveness, physical presence, and co-regulation that social media cannot provide. Result: wanting without liking. High alertness, low nourishment.

The criticism question connects to something deeper. The framework traces five seemingly unrelated experiences — online criticism anxiety, betrayal pain, calm contagion, loneliness health damage, crowd energy — to one architectural fact: social connection is a body-base requirement. Eisenberger (2003) showed that social rejection activates the same brain region as physical pain. Not metaphor — the same circuits.

Limerence: Fisher (2004) showed it activates drive-level systems — same level as hunger and thirst. A temporary biological subsidy lasting 18–36 months. "The spark died" is subsidy expiry, not stopped loving. The framework maps what sustains bonds afterward.

The full framework is 200+ files, open-source (CC0 licensed), with citations and explicit conditions for being wrong.

Full blog post with 6 mechanism sketches and honest limitations:
https://hoanispof.github.io/Human-Predictive-Drive/blog/bridging-neuroscience-psychology/

Framework:
https://github.com/hoanispof/Human-Predictive-Drive

Does this match your experience? What doesn't fit?

---

## Posting Rules

```
ORDER: Post Blog FIRST → then Short Post (blog must exist before linking)

CADENCE:
  → Post 1 platform → wait 3-5 days → gauge → refine → post next
  → NEVER post multiple platforms on the same day (spam detection)
  → Max 1 post/week across all platforms

PRIORITY ORDER:
  1. LessWrong (primary stress-test — rationalist community)
  2. Hacker News (broad tech, high traffic)
  3. r/cogsci (bridge between tech and neuro)
  4. r/psychology (broader, more accessible)

RESPONDING:
  → Reply to all substantive comments within 24h
  → Welcome challenges: "Good point. Here's the evidence: [citation]"
  → Honest gaps: "We don't know. That's a genuine gap."
  → If falsified: update blog, credit challenger

PRE-POST CHECKLIST:
  □ Blog live and accessible via GitHub Pages
  □ All links working (blog URL, repo URL)
  □ Re-read short post: tone matches platform norms?
  □ Not self-help framing (W.4 check)
  □ Counter-evidence invited explicitly
  □ No marketing language ("star the repo", "share this")
```
