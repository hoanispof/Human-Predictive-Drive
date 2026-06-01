---
title: Short Posts — Dopamine Signals Salience, Not Reward
date: 2026-05-31
purpose: Short posts (~150-300 words) for Reddit/forums, linking to the full blog post
status: Draft v0.1
blog_link: dopamine-signals-salience-not-reward.md
platforms: r/neuroscience, r/psychology, r/cogsci
references:
  plan-neuro-posts.md §4 — short post format
  framing-engagement-value.md — 3-layer value model
  plan-tech-distribution.md §5 — posting cadence
---

# Short Posts: Dopamine Signals Salience, Not Reward

> Each short post = AUDITION. The blog = FULL PERFORMANCE.
> If the audition fails (no engagement) → framing needs work.
> If the audition passes → traffic to blog → deeper engagement.

---

## Short Post A — r/neuroscience (academic tone)

**Title:** Dopamine as salience signal, not reward: a proposed 7-step mechanism for when opioid reward fires

**Body:**

The wanting/liking distinction (Berridge & Robinson, 1998) is approaching its third decade, yet "dopamine = reward" persists in textbooks and popular science. More importantly, the mechanism behind *liking* — specifically, *when* opioid reward fires — remains underspecified.

I've developed an open-source framework that proposes a specific answer: a 7-step mechanism connecting VTA habituation-based delta detection to body-level opioid response, with five independently testable preconditions for when reward fires.

Key evidence the model synthesizes:

- Naltrexone blocks stimulant euphoria without blocking dopamine release (Jayaram-Lindström et al., 2017 — PET + microdialysis)
- Musical anhedonia: auditory cortex intact, reward system intact, but domain-specific connectivity broken → anhedonia for music only (Martínez-Molina et al., 2016, PNAS)
- Same molecule (dopamine), three disruption points (nicotine hijack / Parkinson's loss / ADHD tuning), three distinct clinical outcomes

The model is falsifiable: if a pure dopamine agonist reliably produces pleasure without opioid involvement, it's wrong.

Full analysis with 30 citations, test cases, and explicit limitations:
https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/

Full framework (200+ files, CC0 licensed):
https://github.com/hoanispof/Human-Predictive-Drive

What would convince you that dopamine alone is insufficient for reward? Where does this break?

---

## Short Post B — r/psychology (accessible tone)

**Title:** Why scrolling feels empty: dopamine isn't your reward chemical — and 30 years of research agrees

**Body:**

You've probably heard: "Scrolling releases dopamine, that's why it's addictive." But here's what three decades of neuroscience research actually shows:

Dopamine ≠ pleasure. Dopamine = "hey, something changed — look!" It's a doorbell, not the gift behind the door.

The actual reward signal comes from your opioid system — but *only* when what you find matches something you currently need. This is why:

- Sometimes you scroll for an hour and feel GOOD (found things that matched)
- Sometimes you scroll for an hour and feel EMPTY (nothing matched)
- Same app. Same scrolling. Same dopamine. Different result.

The strongest evidence: when researchers gave L-DOPA (which directly increases dopamine) to healthy people, their mood didn't change at all (Liggins et al., 2012). More dopamine, zero extra pleasure.

Even more striking: blocking the opioid system with naltrexone reduces euphoria from stimulants — even though dopamine keeps firing normally (Jayaram-Lindström et al., 2017). Two separate systems.

I've written a detailed analysis proposing a specific mechanism for *when* reward fires (and when it doesn't), with test cases, clinical evidence, and explicit "here's how to prove this wrong" criteria:

https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/

The full framework is open-source (CC0): https://github.com/hoanispof/Human-Predictive-Drive

Does this match your experience? What doesn't fit?

---

## Short Post C — r/cogsci (bridge tone)

**Title:** Beyond wanting vs. liking: a proposed 7-step mechanism for when opioid reward fires

**Body:**

Berridge & Robinson separated wanting (dopamine) from liking (opioid) in 1998. The separation is well established. What's less specified is the *mechanism*: under what conditions does liking fire?

I've been developing an open-source framework that proposes a specific answer — a 7-step mechanism from VTA delta detection to body-level opioid response, with five preconditions that determine whether a given stimulus produces genuine reward or just attention capture.

The model makes specific predictions:

- Social media scrolling should feel empty when content doesn't match body-level needs (dopamine fires, opioid doesn't)
- Musical anhedonia (Martínez-Molina 2016) should be possible only if reward is multi-step (it is — confirmed)
- Gambling addiction should require physiological arousal, not just dopamine (Sharpe 2004 — it does)
- Naltrexone should block stimulant euphoria without blocking dopamine (Jayaram-Lindström 2017 — it does)

The model is structured for falsification: five preconditions, each independently testable, with explicit conditions for disproving the mechanism.

Full analysis (30 citations, honest limitations, clinical dissociations):
https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/

Framework (200+ files, CC0):
https://github.com/hoanispof/Human-Predictive-Drive

Counter-evidence is more valuable than confirmation. Where does this break?

---

## Posting Rules (from plan files)

```
ORDER: Post Blog FIRST → then Short Post (blog must exist before linking)

CADENCE:
  → Post 1 subreddit → wait 3-5 days → gauge → refine → post next
  → NEVER post multiple subreddits on the same day (spam detection)
  → Max 1 post/week across all platforms

PRIORITY ORDER:
  1. r/neuroscience (primary expert target)
  2. r/cogsci (bridge between tech and neuro)
  3. r/psychology (broader, more accessible)

RESPONDING:
  → Reply to all substantive comments within 24h
  → Welcome challenges: "Good point. Here's the evidence: [citation]"
  → Honest gaps: "We don't know. That's a genuine gap."
  → If falsified: update blog, credit challenger

PRE-POST CHECKLIST:
  □ Blog live and accessible via GitHub Pages
  □ All links working (blog, repo)
  □ Re-read short post: tone matches subreddit norms?
  □ Not self-help framing (W.4)
  □ Counter-evidence invited explicitly
  □ Ready for 8 anticipated challenges (see 01-Dopamine-Not-Reward.md §3.3)
```

---

## Blog Link

All short posts link to:
`https://hoanispof.github.io/Human-Predictive-Drive/blog/dopamine-signals-salience-not-reward/`
