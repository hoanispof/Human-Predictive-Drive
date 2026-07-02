---
title: Short Posts — Cortisol Is Not Your Stress Hormone
date: 2026-05-31
purpose: Short posts (~150-300 words) for Reddit/forums, linking to the full blog post
status: Draft v0.1
blog_link: cortisol-is-not-stress.md
platforms: r/neuroscience, r/psychology, r/cogsci
references:
  plan-neuro-posts.md §4 — short post format
  framing-engagement-value.md — 3-layer value model
  plan-overview-distribution.md §3 — posting cadence
---

# Short Posts: Cortisol Is Not Your Stress Hormone

> Each short post = AUDITION. The blog = FULL PERFORMANCE.
> If the audition fails (no engagement) → framing needs work.
> If the audition passes → traffic to blog → deeper engagement.

---

## Short Post A — r/neuroscience (academic tone)

**Title:** Cortisol as change-readiness amplifier, not stress hormone: why source direction matters more than level

**Body:**

The "stress hormone" label for cortisol has persisted since Selye (1936), and Selye's own eustress/distress distinction (1976) identified the problem without specifying the mechanism. Fifty years later, we still lack a clear mechanistic account of why the same cortisol level produces opposite outcomes.

I've developed an open-source framework that proposes a specific answer: **source direction matters more than level**. The same cortisol concentration can produce approach-tagged or avoidance-tagged neural compilation depending on body-state context at the moment of encoding (consistent with Cahill & McGaugh, 1998; Dolcos et al., 2017).

Key evidence the model synthesizes:

- McEwen (2007): chronic cortisol → PFC dendritic retraction. BUT Vyas et al. (2002): same conditions → amygdala dendritic *growth*. Same molecule, opposite effects — amplifier, not toxin.
- Yehuda (1990, 2001): established PTSD = cortisol baseline LOW, not high. Reconciled via two-phase model (encoding HIGH → maintenance LOW with GR upregulation).
- Addison's disease: cortisol ≈ 0 = fatigue, cognitive impairment, potentially fatal — not the "zero stress" the label predicts.

The model proposes the inverted-U (Yerkes-Dodson, 1908) is emergent from repair × damage balance, not an arbitrary empirical law. Peak is personalized across six parameters.

Falsifiable: if cortisol injection reliably produces subjective stress in healthy subjects, the amplifier model fails.

Full analysis with 28 citations, test cases, and explicit limitations:
https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/

Full framework (200+ files, CC0 licensed):
https://github.com/hoanispof/Human-Predictive-Drive

Where does Source > Level break? What evidence would convince you that cortisol level alone is sufficient to predict outcome?

---

## Short Post B — r/psychology (accessible tone)

**Title:** Why "lower your cortisol" is probably the wrong advice — and what 90 years of research actually shows

**Body:**

You've heard it everywhere: "Cortisol is the stress hormone. Lower it. Detox it. Fight it."

But here's what the research actually shows:

**Zero cortisol is dangerous, not peaceful.** People with Addison's disease (near-zero cortisol) experience chronic fatigue, cognitive fog, and potentially fatal crisis. They need cortisol *replacement* to function. If cortisol = stress, zero should feel amazing. It doesn't.

**Cortisol peaks when you're having a great time.** Exercise, morning waking, sex, solving a challenging puzzle — all raise cortisol. Same molecule. Same level. Opposite experience.

**The same cortisol level can feel like flow or dread.** 15 μg/dL during a fascinating problem = energized, engaged. 15 μg/dL under a threatening boss = anxious, defensive. The level didn't change. The *source* did.

The strongest evidence: chronic stress makes your PFC (thinking brain) *shrink* — but your amygdala (threat detector) *grow* (McEwen, 2007; Vyas, 2002). Same cortisol, opposite effects on different brain regions. That's not a toxin. That's an amplifier.

I've written a detailed analysis proposing that *source direction* and *repair balance* (mainly: sleep quality) determine whether cortisol helps or harms — with test cases, clinical evidence, and "here's how to prove this wrong" criteria:

https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/

The full framework is open-source (CC0): https://github.com/hoanispof/Human-Predictive-Drive

Does this match your experience? When has "just reduce your stress" missed the point?

---

## Short Post C — r/cogsci (bridge tone)

**Title:** Beyond eustress vs. distress: why source direction and repair balance determine when cortisol helps vs. harms

**Body:**

Selye separated eustress from distress in 1976. The distinction is well accepted. What's less specified is the *mechanism*: under what conditions does cortisol support adaptation vs. cause damage?

I've been developing an open-source framework that proposes a specific answer — the **Source > Level principle**: the direction of body-state context during cortisol exposure determines neural compilation tags (approach vs. avoidance), not the cortisol level itself. The framework also proposes that the Yerkes-Dodson inverted-U is *emergent* from a repair × damage balance, with a personalized peak that shifts based on six measurable parameters.

The model makes specific predictions:

- Cortisol injection in healthy subjects should NOT produce subjective stress (current evidence: it doesn't)
- PTSD should show LOW cortisol baseline, not high — two-phase model (Yehuda 1990 — confirmed)
- PFC and amygdala should show OPPOSITE responses to same chronic cortisol (McEwen 2007 + Vyas 2002 — confirmed: PFC shrinks, amygdala grows)
- Post-project "blues" duration should correlate with prior cortisol elevation duration (testable)

The model is structured for falsification: five explicit conditions under which the framework is wrong, plus five acknowledged limitations.

Full analysis (28 citations, honest limitations, clinical dissociations):
https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/

Framework (200+ files, CC0):
https://github.com/hoanispof/Human-Predictive-Drive

Counter-evidence is more valuable than confirmation. Where does Source > Level fail?

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
  2. r/cogsci (bridge between disciplines)
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
  □ Ready for anticipated challenges (see Phase 2 expert challenge map)
```

---

## Blog Link

All short posts link to:
`https://hoanispof.github.io/Human-Predictive-Drive/blog/cortisol-is-not-stress/`
