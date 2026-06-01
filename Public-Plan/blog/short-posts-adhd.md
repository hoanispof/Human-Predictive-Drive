---
title: Short Posts — ADHD Is Not Attention Deficit
date: 2026-05-31
purpose: Short posts (~150-300 words) for Reddit/forums, linking to the full blog post
status: Draft v0.1
blog_link: adhd-is-not-attention-deficit.md
platforms: r/neuroscience, r/psychology, r/cogsci, r/ADHD_Programmers
references:
  plan-neuro-posts.md §4 — short post format
  plan-adhd-tech-distribution.md — ADHD-like × tech strategy
  framing-engagement-value.md — 3-layer value model
---

# Short Posts: ADHD Is Not Attention Deficit

> Each short post = AUDITION. The blog = FULL PERFORMANCE.
> If the audition fails (no engagement) → framing needs work.
> If the audition passes → traffic to blog → deeper engagement.

---

## Short Post A — r/neuroscience (academic tone)

**Title:** ADHD as threshold tuning, not attention deficit: a unified mechanism for hyperfocus, the anxiety chain, and the stimulant paradox

**Body:**

"Attention Deficit" has been the label since DSM-III-R (1987), but the mechanism it describes is not a deficit. The same person who cannot sustain attention on a routine task for five minutes can hyperfocus on a novel problem for six hours. Same brain. Same day. A deficit model cannot produce both outputs.

I've developed an open-source framework that proposes: **DRD4 receptor sensitivity + DAT clearance speed function as a hardware threshold**. Input below threshold is filtered (inattention). Input above threshold captures all processing (hyperfocus). One mechanism, opposite behaviors depending on input magnitude.

Key evidence the model synthesizes:

- Gaze cueing selectively impaired: eyes fail, arrows intact (Marotta et al., 2017, Psychiatry Research). Not general inattention — social-specific threshold.
- Alpha modulation inverse in ADHD parieto-occipital (PMC6969336, 2019, n=45 EEG). Neural processing is *different*, not weaker.
- Social cognition deficit closes with age (meta-analysis, 49 studies, n=2,449). Delayed compilation, not fixed deficit.
- Stimulants calm ADHD (Volkow 2012): PFC under-fueled → add fuel → PFC regulates → calm. Threshold model resolves the paradox.

The model also proposes a testable 6-step mechanism for why 47% develop comorbid anxiety: threshold filters social micro-cues → surprise threats compile → "unpredictable world" schema → chronic anticipatory worry.

Falsifiable: if attention training eliminates ADHD without changing receptor sensitivity, the threshold model fails.

Full analysis with 50+ citations, six paradoxes resolved, and explicit limitations:
https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/

Full framework (200+ files, CC0 licensed):
https://github.com/hoanispof/Human-Predictive-Drive

Where does the threshold model break? What evidence would convince you that ADHD is better described as a deficit than a threshold difference?

---

## Short Post B — r/psychology (accessible tone)

**Title:** Why "just try harder" makes ADHD worse — and what the mechanism actually is

**Body:**

"Just try harder."

If you have ADHD, you've heard this thousands of times. Here's what the research shows about what that advice actually does to the brain:

**Each "try harder → fail" doesn't compile harder-trying.** It compiles a pattern: [effort → not enough]. Repeat daily for years → the pattern fires automatically before every task: "I'll fail anyway." Self-esteem data confirms: ADHD self-esteem deficit increases with age, not decreases (Betancourt 2024, meta-analysis, n=11,948, effect size 0.46–0.67).

**The mechanism isn't willpower.** DRD4 receptors in ADHD have reduced sensitivity to dopamine. DAT clears dopamine faster. Result: small signals don't register. Not "can't pay attention" — threshold calibrated differently.

This explains the paradoxes:
- **Can't focus 5 min + hyperfocus 6 hours** = same threshold, different input size
- **Stimulants calm instead of excite** = PFC under-fueled, stimulant adds fuel, PFC *regulates* everything else down
- **"Motivated but can't start"** = motivation (mesolimbic) works fine; activation (mesocortical PFC) is under-fueled. Two separate systems (Plichta & Scheres 2014: anticipation impaired, delivery normal).

I've written a detailed analysis proposing that one hardware parameter — receptor sensitivity threshold — resolves six paradoxes that the "deficit" label cannot explain. With inverted-U evidence (subclinical creativity g=0.36, clinical = no benefit), three-tier persistence model, and "here's how to prove this wrong" criteria:

https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/

The full framework is open-source (CC0): https://github.com/hoanispof/Human-Predictive-Drive

Does the threshold model match your experience? Where does it fail?

---

## Short Post C — r/cogsci (bridge tone)

**Title:** One dopamine system, three disruptions, three conditions: ADHD as threshold tuning alongside nicotine hijack and Parkinson's loss

**Body:**

Dopamine is not "the reward chemical" — it's a salience signal. Three conditions disrupt the same system at three different points, producing three completely different clinical pictures:

| | Nicotine | Parkinson's | ADHD |
|---|---|---|---|
| Disruption | External substance FORCES VTA to fire | Dopamine neurons DIE | Signal cleared too FAST + receptor less SENSITIVE |
| Pathway | Mesolimbic (VTA→NAcc) | Nigrostriatal (SNc→Striatum) | Mesocortical (VTA→PFC) |
| Reversible? | Yes (quit → restore) | No (neurons dead) | N/A (not damage) |

I've been developing an open-source framework that proposes ADHD is best understood as **threshold tuning** — DRD4 receptor sensitivity + DAT clearance speed function as a hardware parameter that determines what signals reach conscious processing.

The model makes specific predictions:

- Hyperfocus + inattention = SAME mechanism, different input magnitude (not two separate systems)
- Gaze cueing should be selectively impaired for social but not symbolic cues (confirmed: Marotta et al. 2017, Psychiatry Research — eyes fail, arrows work)
- 47% anxiety comorbidity should arise from micro-cue filtering → surprise threats (testable via gaze-cueing × anxiety rate correlation)
- Inverted-U: subclinical = creative advantage (g=0.36), severe = impairment (Tran 2026, 17,000+)
- Prevalence should be stable regardless of cultural change (confirmed: Polanczyk 2014, 3 decades)

The model is structured for falsification: five explicit conditions under which the framework is wrong, plus five acknowledged limitations.

Full analysis (50+ citations, honest limitations, optimization hierarchy):
https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/

Framework (200+ files, CC0):
https://github.com/hoanispof/Human-Predictive-Drive

Where does the threshold model fail? Counter-evidence is more valuable than confirmation.

---

## Short Post D — r/ADHD_Programmers (tech + personal tone)

**Title:** Your event listener isn't broken — its threshold is set differently. A mechanism model for why you can debug for 6 hours but can't answer a 3-sentence email.

**Body:**

You know the experience. Three-sentence email: impossible. Novel debugging problem: four hours vanish.

I've been building an open-source framework (~170 files) that models human cognition, and the ADHD analysis proposes a specific mechanism:

**DRD4 receptor sensitivity = your event listener's `minThreshold`.**

Input below threshold → event DROPPED (not processed → "inattentive"). Input above threshold → event CAPTURED → full processing chain fires (hyperfocus). Medication = adjusting the threshold parameter → more events captured.

This explains things the "deficit" label can't:

- **"Motivated but can't start"** = You know the right API to call. Your client just doesn't SEND the request. Motivation (mesolimbic) works. Activation (mesocortical PFC) is under-fueled. Deadline = timeout handler: "if no response by X → force send."

- **"Try harder" = feeding more data to a biased model.** Each "try harder → fail" compiles [effort → not enough]. You don't fix a biased ML model by training MORE on biased data. You fix the training pipeline.

- **47% anxiety comorbidity** = Your social signal threshold filters micro-cues (subtle facial expressions, tone shifts). Others' frustration accumulates invisibly. When it explodes, it's a surprise at maximum intensity. Repeat → compile "world is unpredictable" → chronic anticipatory worry.

The model predicts an inverted-U: subclinical ADHD = creative advantage (g=0.36). Clinical = no creativity benefit. Severe = real impairment. "ADHD is a superpower" conflates positions on the spectrum.

Full mechanism analysis with 50+ citations and explicit "here's how this model is wrong" criteria:
https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/

Full framework (CC0): https://github.com/hoanispof/Human-Predictive-Drive

Does the threshold model match your experience as a programmer with ADHD? Where does it break?

---

## Posting Rules (from plan files)

```
ORDER: Post Blog FIRST → then Short Post (blog must exist before linking)

CADENCE:
  → Post 1 subreddit → wait 3-5 days → gauge → refine → post next
  → NEVER post multiple subreddits on the same day (spam detection)
  → Max 1 post/week across all platforms

PRIORITY ORDER:
  1. r/ADHD_Programmers (Tier S — ADHD × tech intersection)
  2. r/neuroscience (primary expert target)
  3. r/cogsci (bridge between disciplines)
  4. r/psychology (broader, more accessible)

NOTE: r/ADHD_Programmers is NEW addition for Blog C.
Blog A and B do not have this platform.
Blog C's audience profile uniquely matches this sub.

RESPONDING:
  → Reply to all substantive comments within 24h
  → Welcome challenges: "Good point. Here's the evidence: [citation]"
  → Honest gaps: "We don't know. That's a genuine gap."
  → If falsified: update blog, credit challenger
  → If resonance-only ("this changed my life!"): redirect to verification
    "Glad it resonates. But resonance ≠ truth. Here's how to test it."

PRE-POST CHECKLIST:
  □ Blog live and accessible via GitHub Pages
  □ All links working (blog, repo)
  □ Re-read short post: tone matches subreddit norms?
  □ Not self-help framing (W.4)
  □ Not "superpower" framing (explicit inverted-U mention)
  □ Counter-evidence invited explicitly
  □ Disclaimer: "mechanism analysis, not medical advice"
  □ Ready for anticipated challenges:
    - "Who are you to explain us?"
    - "This is just another superpower narrative"
    - "DAT findings are inconsistent"
    - "RSD isn't validated"
```

---

## Blog Link

All short posts link to:
`https://hoanispof.github.io/Human-Predictive-Drive/blog/adhd-is-not-attention-deficit/`
