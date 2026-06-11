---
title: "Dopamine Is Not Reward: The Evidence and a Proposed Mechanism"
date: 2026-05-31
author: Independent researcher
license: CC0 1.0 Universal
status: Draft v0.1
tags: [neuroscience, dopamine, reward, opioid, mechanism, falsifiable]
---

# Dopamine Is Not Reward

**28 years of evidence, a proposed 7-step mechanism, and five testable preconditions for when opioid reward actually fires.**

---

## Summary

The popular claim that "dopamine = reward" has been contradicted by research since Berridge & Robinson (1998). In neuroscience, the wanting/liking distinction is well established. Yet the mechanism behind *liking* — specifically, when and why opioid reward fires — remains underspecified in the literature.

This post presents:

1. **Nine converging lines of evidence** against "dopamine = reward" (seven with direct research support)
2. **A proposed 7-step mechanism** connecting VTA salience detection to body-level opioid response
3. **Five specific preconditions** for when opioid reward fires — each independently testable
4. **Real-world test cases** (social media engagement, gambling) that the mechanism predicts and classical models cannot explain
5. **Three clinical dissociations** (nicotine addiction, Parkinson's disease, ADHD) showing the same molecule, three disruption points, three distinct outcomes
6. **Explicit falsification criteria** — conditions under which this mechanism is wrong

Three positions, not two:

| Position | Claim | Problem |
|---|---|---|
| Pop science (1950s–present) | "Dopamine = reward chemical. More dopamine = more pleasure." | Contradicted by 28 years of research. Depleting dopamine doesn't eliminate pleasure. Boosting it doesn't increase pleasure. |
| Academic consensus (correct but incomplete) | "Dopamine = wanting. Opioid = liking. Separate systems." | Correct separation — but doesn't specify *when* opioid reward fires, or *why* the same stimulus sometimes produces reward and sometimes doesn't. |
| **This framework** | **"7-step mechanism connects VTA salience → body-level evaluation → opioid reward. Five preconditions determine when reward fires."** | Testable. See falsification criteria below. |

This is a hypothesis inviting falsification, not a claim of established theory. The full framework (200+ files, CC0 licensed) is available for inspection and stress-testing at the repository linked below.

**Epistemic status:** Builds on established research (Berridge, Schultz, Peciña). The wanting/liking separation is settled science. The 7-step mechanism and 5 preconditions are proposed extensions — testable but not yet experimentally validated as a unified model.

---

## §1 — The Gap That Remains (1998–2026)

Berridge and Robinson published their landmark wanting/liking distinction in 1998. Nearly three decades of subsequent research have confirmed the core finding: dopamine mediates *incentive salience* (wanting), not *hedonic impact* (liking). The opioid system, particularly mu-opioid receptors in hedonic hotspots, mediates the actual pleasure response (Peciña & Berridge, 2005).

This is no longer controversial in research neuroscience. It is, however, still largely unknown to the general public. Textbooks, popular science, wellness culture, and productivity advice continue to treat dopamine as "the reward chemical." The phrase "dopamine hit" generates millions of search results. "Dopamine detox" is a lifestyle brand. The gap between research consensus and popular understanding is approximately 20–30 years and widening.

But there is a second, more interesting gap — one within the research itself.

Berridge separated wanting from liking. He identified opioid hotspots as the substrate for liking. He showed that the two systems can dissociate. What he left largely unspecified is the *mechanism*: **under what conditions does liking fire?** What are the necessary and sufficient conditions for opioid reward to activate? Why does the same stimulus sometimes produce reward and sometimes not?

This post proposes a specific answer to that question.

---

## §2 — The Evidence Base

The case against "dopamine = reward" rests on multiple independent lines of evidence. Here are the five strongest, selected for their directness and replicability.

### Evidence 1: Dopamine depletion does not eliminate pleasure

Berridge & Robinson (1998), Peciña & Berridge (2005):

Rats with depleted or lesioned dopamine systems still display "liking" facial reactions (lip-licking, tongue protrusion) when given sugar. They no longer *seek* sugar — they won't press a lever for it — but when sugar is placed on their tongues, they enjoy it normally.

Conversely, stimulating the dopamine system (via amphetamine or optogenetics) increases seeking behavior dramatically without increasing liking reactions (Adamantidis et al., 2011; Berridge lab replications).

If dopamine were the reward signal, depleting it should eliminate pleasure. It doesn't. Boosting it should increase pleasure. It doesn't.

### Evidence 2: Naltrexone blocks euphoria without blocking dopamine

This is perhaps the strongest pharmacological dissociation.

Jayaram-Lindström et al. (2017, *Translational Psychiatry*) demonstrated via PET imaging and microdialysis that naltrexone (an opioid receptor antagonist) blocks stimulant euphoria **without** blocking dopamine release. Dopamine fires normally; euphoria is abolished.

This has been replicated across multiple studies and substances:

| Study | n | Substance | Finding |
|---|---|---|---|
| Jayaram-Lindström et al., 2004 | 12 | Dextroamphetamine | Naltrexone reduces subjective effects |
| Jayaram-Lindström et al., 2008 | 80 | Dextroamphetamine (12-week RCT) | Reduces relapse |
| Ray et al., 2015 | 30 | IV methamphetamine | Reduces craving |
| Spencer et al., 2018 | 37 | Methylphenidate (ADHD) | Reduces euphoria ("Liking Effect") |
| Jayaram-Lindström et al., 2017 | PET+microdialysis | Amphetamine | Blocks euphoria, NOT dopamine release |

If dopamine alone produced reward, blocking opioid receptors should not affect euphoria. It does — consistently, across labs and substances. Two independent systems.

### Evidence 3: Musical anhedonia — the pipeline integrity test

Martínez-Molina et al. (2016, *PNAS*):

Approximately 3–5% of the population experiences musical anhedonia — they can hear music normally (auditory cortex intact), they enjoy food, sex, and money normally (reward system intact), but they derive no pleasure from music specifically. The deficit is a **reduced functional connectivity** between auditory cortex and nucleus accumbens.

This is a proof by contradiction against single-step models:

- If dopamine firing = reward (one step), then: auditory cortex processes music → VTA detects novelty → dopamine fires → pleasure should occur. Anhedonia should be impossible.
- In a multi-step model: steps 1–3 (VTA detection, dopamine, spreading activation) function normally, but the *pathway* from auditory processing to the reward system (step 4) is broken. Downstream opioid response (step 5) never fires. Anhedonia is predicted and observed.

Musical anhedonia is domain-specific — the components work, but the pipeline between them is disconnected. This is only possible if reward involves multiple sequential steps, not a single dopamine signal.

### Evidence 4: Parkinson's dissociation — wanting impaired, liking preserved

Clinical observations in Parkinson's disease (Sienkiewicz-Jarosz et al., 2005; Loas et al., 2012):

Dopamine neuron loss in the substantia nigra and VTA produces characteristic motivational deficits — patients become apathetic, lose initiative, stop seeking activities. Yet their capacity for enjoyment, when stimuli are provided directly, is often partially preserved. They may not seek food, but they enjoy eating when food is offered.

The three dopamine pathways (nigrostriatal, mesolimbic, mesocortical) degrade at different rates, producing a clean temporal dissociation: motor function deteriorates first, then motivation, then cognition — while hedonic capacity lags behind.

### Evidence 5: Opioid agonist at hedonic hotspot produces liking; dopamine agonist does not

Peciña & Berridge (2005):

Injecting a mu-opioid agonist directly into the nucleus accumbens hedonic hotspot *increases* liking reactions. Injecting a dopamine agonist into the same region *increases seeking behavior* but does **not** increase liking reactions.

Same brain region. Same experimental setup. Different neurotransmitter. Opposite result on liking. The reward signal is opioid, not dopaminergic.

### Summary of the evidence

| # | Evidence | Source | Contradicts "dopamine = reward"? |
|---|---|---|---|
| 1 | Dopamine depletion → liking preserved | Berridge & Robinson, 1998 | Yes — decisively |
| 2 | Naltrexone blocks euphoria, not dopamine | Jayaram-Lindström et al., 2017 | Yes — pharmacologically |
| 3 | Musical anhedonia: pipeline broken, components intact | Martínez-Molina et al., 2016 | Yes — structurally |
| 4 | Parkinson's: wanting impaired, liking preserved | Clinical observation | Yes — clinically |
| 5 | Opioid agonist → liking; dopamine agonist → no liking | Peciña & Berridge, 2005 | Yes — directly |

Additional supporting evidence (described in the full framework):

| # | Evidence | Source |
|---|---|---|
| 6 | Schultz VTA signal = delta/salience, not value | Schultz, 1997 (reinterpreted) |
| 7 | Addiction: wanting sensitizes while liking habituates | Robinson & Berridge, 2003 |
| 8 | Social media scrolling: dopamine present, satisfaction absent | Daily observable + framework analysis |
| 9 | Eureka moment: opioid-based, not dopamine spike | Framework synthesis |

> **Framework deep reads:**
> [Dopamine-Is-Not-Reward.md](../../Core-Deep-Dive/Clarification/Dopamine-Is-Not-Reward.md) — full 9-evidence analysis with 3-position comparison table
> · [Reward-Signal-Architecture.md](../../Core-Deep-Dive/Body-Base/Body-Feedback/Reward-Signal-Architecture.md) — evaluative vs. direct-state reward pathways

---

## §3 — Proposed Mechanism: The 7-Step Model

If dopamine signals salience and opioid signals reward, what connects them? When does the opioid system fire? Here is a proposed mechanism.

```
Step 1: CONTINUOUS NEURAL ACTIVITY
  86 billion neurons fire continuously. Patterns (chunks) emerge
  through Hebbian self-organization. This is background activity,
  not triggered by stimuli — it runs 24/7.

Step 2: VTA DELTA DETECTION (habituation-based)
  The VTA monitors ongoing neural patterns. When patterns are stable,
  VTA habituates and goes quiet. When a pattern CHANGES (new input,
  novel association, prediction violation), VTA fires.
  → Dopamine release = "something changed — pay attention"
  → This is a salience signal, not a value signal.

Step 3: RECEPTOR FILTERING
  Dopamine binds to D4 receptors in the PFC.
  Individual genetic variation (DRD4 polymorphisms) determines
  sensitivity threshold — some individuals respond to small deltas,
  others require larger changes to trigger attention.

Step 4: PFC SPOTLIGHT (top-down attention)
  PFC receives the dopamine signal and directs norepinephrine +
  acetylcholine to the relevant neural region, boosting signal clarity.
  Spreading activation (Collins & Loftus, 1975) brings associated
  patterns into working memory.

Step 5: BODY-LEVEL EVALUATION (the critical step)  ⬅
  PFC projects the activated pattern to body-level simulation.
  The body evaluates: does this pattern match a current need?
  → YES: mu-opioid release = genuine reward
  → NO: body returns neutral signal = no reward
  This step is where wanting becomes (or fails to become) liking.

Step 6: REINFORCEMENT + HABITUATION
  If Step 5 produces opioid reward, the successful pattern is
  strengthened via Hebbian LTP. The VTA then habituates to the
  new baseline — the same stimulus will produce less dopamine
  next time (hedonic treadmill at neural level; Brickman, 1978).

Step 7: DOPAMINE CLEARANCE (COMT)
  COMT enzyme degrades dopamine in the PFC synapse.
  Val/Val polymorphism = fast clearance (rapid shifting)
  Met/Met polymorphism = slow clearance (sustained focus)
  The synapse is ready for the next detection event.
```

### The key claim: Step 5

Step 5 is where this model departs from prior accounts. Berridge demonstrated that liking is opioid-mediated and dissociable from wanting. But what triggers the opioid response? The model proposes that opioid reward fires **when the activated pattern matches a current body-level need** — and fails to fire when it does not.

This explains a common puzzle: why the same stimulus (the same song, the same food, the same social interaction) sometimes produces reward and sometimes doesn't. The stimulus is identical; the body-state and current needs are different. Step 5 is where context meets evaluation.

> **Framework deep reads:**
> [03-Reward.md](../../Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/03-Reward.md) — full 7-step mechanism with 7 reward cases
> · [Novelty.md](../../Core-Deep-Dive/Observation/Novelty.md) — VTA delta detection and novelty drive mechanism
> · [Body-Feedback-Mechanism.md](../../Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Mechanism.md) — body-level feedback architecture

---

## §4 — Five Preconditions for Opioid Reward

If Step 5 is the critical gate, what determines whether it opens? The model proposes five preconditions, all of which must be met for full opioid reward to fire. Missing any one produces a weak, absent, or misdirected signal.

**Precondition 1 — Directed Gap**: The body must have an active, unfilled need. A satiated system has no gap to fill. Eating when hungry → reward. Eating when stuffed → no reward (or aversion). The body maintains a registry of pending needs; reward fires when something fills one.

**Precondition 2 — Pattern Substrate**: The system must have sufficient compiled experience (patterns, memories, schemas) to evaluate the stimulus. A wine novice and a sommelier taste the same wine; the sommelier has denser substrate and can detect matches the novice cannot. More compiled experience → richer evaluation → potentially stronger reward.

**Precondition 3 — Delta Gate**: There must be sufficient change (novelty, surprise, prediction violation) to trigger VTA detection in the first place. Completely predictable stimuli habituate — VTA stops firing, attention doesn't engage, and the stimulus never reaches evaluation. This is why routine pleasures lose intensity: the delta shrinks below threshold.

**Precondition 4 — Match Range (Goldilocks Zone)**: The stimulus must fall within a match range relative to the pending need — close enough to register as relevant, novel enough to generate delta. Too familiar → habituated, no delta. Too alien → no match. The zone is dynamic and varies per individual, context, and need type.

**Precondition 5 — Compile Gate**: The pattern must be tagged as approach-relevant, not threat-relevant. A pattern compiled under high stress (threat-tagged via cortisol at the moment of compilation) will trigger avoidance, not approach, even if it matches a current need. Trauma responses are a clear example: a stimulus that would normally be rewarding triggers aversion because the compiled pattern carries a threat tag.

Each precondition is independently testable. Miss Precondition 1 → no reward (eating when full). Miss Precondition 3 → no reward (tenth repetition of a joke). Miss Precondition 5 → aversion instead of reward (a food that was eaten before a traumatic event).

> **Framework deep reads:**
> [03-Reward.md §3](../../Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/03-Reward.md) — detailed specification of all 5 preconditions
> · [Cortisol-Baseline.md](../../Core-Deep-Dive/Body-Base/Cortisol-Baseline.md) — cortisol direction gate (Precondition 5 mechanism)

---

## §5 — Real-World Test Cases

Two everyday phenomena that the classical "dopamine = reward" model cannot explain, but the 7-step model predicts.

### Test Case A: Why social media scrolling feels empty

Consider this common experience: you scroll through a social media feed for an hour, then stop and feel *empty* — not satisfied, not rewarded, just drained. The classical model predicts the opposite: each new post triggers novelty → dopamine fires → "reward" → you should feel good.

The 7-step model explains:

- Each new post generates a micro-delta (Step 2) → VTA fires → dopamine micro-dose → attention captured (Steps 3–4)
- Step 5 evaluation: does the content match a current body-level need? In most cases, *no* — scrolling doesn't fill a need for connection, meaning, rest, or mastery. The body returns a neutral or negative signal.
- Result: dopamine present (seeking continues) + opioid absent (no genuine satisfaction) = "want more, enjoy less."

**Falsifiable prediction:** If a social media platform switched to serving 100% random content (removing the recommendation algorithm), engagement should drop rapidly — not because of reduced dopamine (scrolling still generates novelty delta), but because random content almost never matches individual body-level needs. The recommendation algorithm works precisely *because* it targets user-specific need-patterns that occasionally trigger Step 5 matches.

**Natural experiment:** When platforms have degraded their algorithms (for advertising, policy, or testing purposes), user engagement drops — even though the scroll action, interface, and novelty-generation mechanism remain identical. Same dopamine trigger. Less body-level match. Less engagement.

**Individual differences:** Some people are not "addicted" to TikTok at all. They open the app, scroll for two minutes, find nothing that matches, and leave. Same app, same dopamine mechanism (scroll = novelty = VTA fire). But their particular need-pattern doesn't match the content library. No Step 5 match → no reward → no hook. If dopamine alone were reward, everyone who scrolls should get hooked equally. They don't.

### Test Case B: Gambling — near-miss, body arousal, and two types of losers

Gambling is a powerful test case because there is no exogenous substance involved. No chemical is ingested. Yet gambling addiction exists and is severe. If dopamine = reward, what is the reward? The action of pressing a button?

The 7-step model explains:

**Near-miss phenomenon** (Chase & Clark, 2010): A near-miss (e.g., two cherries and a lemon on a slot machine) activates the same brain regions as a win. The body *pre-feels* winning — Step 5 fires on a *simulated* outcome, not an actual one. This is consistent with the model's claim that body-level evaluation can operate on imagined/anticipated states, not just present stimuli.

**Dopamine fires even during losses** (Linnet et al., 2011): This seems paradoxical if dopamine = reward. Under the 7-step model, it's expected: dopamine fires because each spin generates uncertainty (delta). Whether the body evaluates the spin as rewarding depends on Step 5 — specifically, whether the gambler imagines the *next* spin as a potential win.

**Two types of losers** (framework prediction):

- **Type 1 — Lose and stop:** The body evaluates: "I've lost real resources. Next spin probability is no better." Step 5 returns a loss/threat signal. Protective mechanisms fire. The gambler stops.
- **Type 2 — Lose and continue:** The body evaluates the *imagined next spin*: "I was close. Next time I'll win. Stopping means losing the chance to recover." Step 5 fires reward on the *imagined* outcome. Protective mechanisms are overridden by loss aversion for the imagined future win.

**Body arousal is necessary** (Sharpe, 2004): Gambling addiction severity correlates with physiological arousal (skin conductance, heart rate). No study has documented gambling addiction in the absence of body arousal. If dopamine alone were the mechanism, body arousal should be irrelevant. It is not — because Step 5 (body-level evaluation) is the actual reward gate.

**Dopamine agonists create vulnerability** (Weintraub et al., 2010): 6–7% of Parkinson's patients on dopamine agonists develop gambling, shopping, or sexual compulsions. They do not report pleasure from the medication itself — they report compulsive *seeking*. Wanting without liking, pharmacologically induced.

---

## §6 — Three Clinical Dissociations

The same molecule — dopamine — disrupted at three different points in the system, producing three entirely different clinical pictures. If dopamine were a single reward signal, this pattern would be difficult to explain. Under the 7-step model, each disruption maps to specific steps.

| Dimension | Nicotine addiction | Parkinson's disease | ADHD |
|---|---|---|---|
| **Mechanism** | VTA forced to fire (hijack) | VTA neurons dying (loss) | Dopamine cleared too quickly (tuning) |
| **Primary pathway** | Mesolimbic (VTA→NAcc) | Nigrostriatal (SNc→Striatum) | Mesocortical (VTA→PFC) |
| **Dopamine effect** | Too much signal | Too little signal | Signal too brief |
| **Wanting/Liking** | Wanting ↑↑↑, Liking ↓ | Wanting ↓↓↓, Liking OK | Wanting variable |
| **7-step mapping** | Step 5 bypassed (opioid directly activated) | Steps 2–4 weakened, Step 5 intact | Step 3 filter calibrated differently |
| **Neuron status** | Intact, forced activation | Dying (irreversible) | Intact, different tuning |

**Nicotine:** Activates mu-opioid receptors, beta-endorphin, and enkephalin in addition to dopamine. Naltrexone (opioid blocker) is used clinically to reduce nicotine reward. Bhatt et al. (2010): knockout mice lacking mu-opioid receptors find nicotine non-rewarding despite normal dopamine function. Nicotine bypasses Step 5 entirely — it activates the opioid system directly, without body-need matching.

**Parkinson's:** VTA neurons die, weakening Steps 2–4 (delta detection, dopamine release, PFC spotlight). But the opioid system (Step 5) remains intact. Result: patients lose motivation to seek but preserve capacity to enjoy when stimuli are provided.

**ADHD:** Dopamine is released normally but cleared too quickly (DAT polymorphisms) and filtered differently (DRD4 variants). The signal arrives but doesn't sustain. Step 3 threshold is calibrated differently — not broken, tuned to a different operating point.

**NIC-PD 2024** (*NEJM Evidence*, n=162): Nicotine patches for one year produced no benefit for Parkinson's disease progression, trending worse. This confirms that nicotine's VTA hijack mechanism is unrelated to neuroprotection — flooding the system with nicotine doesn't restore dying neurons.

> **Framework deep reads:**
> [Nicotine-Brain-Mechanism.md](../../Research/Health-Conditions/Hijack/Nicotine-Brain-Mechanism.md) — nicotine hijack mechanism (VTA bypass)
> · [Parkinson-Analysis.md](../../Research/Health-Conditions/Neurodegeneration/Parkinson-Analysis.md) — 3 dopamine pathways, wanting/liking dissociation
> · [ADHD-Observation.md](../../Research/Health-Conditions/Neurodiversity/ADHD-Observation.md) — DRD4/DAT tuning model

---

## §7 — Implications (If Correct)

If the 7-step model and its five preconditions hold up under scrutiny:

**For engagement metrics:** Current platforms optimize for engagement (clicks, time-on-site, scroll depth) — which tracks dopamine-mediated attention capture (Steps 2–4). User *satisfaction* requires Step 5 (body-level need match). These are different signals with different neural substrates. Optimizing for dopamine-driven engagement while ignoring opioid-mediated satisfaction explains why users can be highly engaged *and* deeply dissatisfied simultaneously.

**For addiction research:** The model distinguishes three addiction mechanisms (opioid drug → Step 5 bypassed; stimulant → Steps 2–4 flooded + opioid involvement; behavioral → dopamine micro-doses without Step 5 match). Each implies different intervention targets. Treating scrolling addiction the same way as heroin addiction conflates different disruption points in the same pipeline.

**For AI reward modeling:** Reinforcement learning systems (RLHF and derivatives) model reward as a single signal analogous to dopamine prediction error. If human reward involves a body-level evaluation step that is separate from the prediction signal, current AI reward models are missing a component. The "reward" in RLHF more closely approximates attention capture (wanting) than genuine satisfaction (liking).

**For understanding "knowing ≠ doing":** The 7-step model is embedded in a larger framework where the body's compiled patterns (body-base) and conscious thought (PFC) are separate systems with different update mechanisms. "Knowing you should exercise" is a PFC state. "Actually exercising" requires body-base patterns. This is a two-system architecture, not a willpower failure.

> **Framework deep reads:**
> [AI-Self-Model.md](../../Research/Global/AI-Self-Model.md) — AI amplification mechanism and dual check model
> · [Core-Software.md](../../Core-Software.md) — full 2-system architecture (body-base vs. PFC)
> · [Compile-Taxonomy.md](../../Core-Deep-Dive/Body-Base/Chunk/Compile-Taxonomy.md) — 3 compile types and why "knowing ≠ doing"
> · [Liking-Wanting.md](../../Core-Deep-Dive/Observation/Liking-Wanting.md) — wanting/liking bridge with 6 wanting mechanisms

---

## §8 — Falsification Criteria

This mechanism is wrong if any of the following can be demonstrated:

1. **A pure dopamine agonist produces reliable pleasure in healthy humans without activating the opioid system.** L-DOPA comes closest to pure dopamine enhancement — Liggins et al. (2012) found no mood change. If a cleaner test produces consistent pleasure from dopamine alone, the model fails.

2. **Blocking the opioid system does not reduce reward from any stimulus class.** Naltrexone studies consistently show reduced euphoria across substances. If a stimulus class produces full reward despite opioid blockade and without involving non-opioid pathways (e.g., endocannabinoid, CT afferents), the opioid-centrality claim fails.

3. **Social media with 100% random content sustains the same engagement as algorithmic content.** If dopamine alone drives engagement, content matching should be irrelevant. If engagement drops with random content, body-level evaluation (Step 5) is implicated.

4. **Gambling addiction occurs without physiological arousal.** If a population of gambling addicts is found with no elevated heart rate, skin conductance, or body-state changes during gambling, the body-level evaluation step is unnecessary.

5. **Musical anhedonia is impossible — no one experiences normal hearing, normal non-musical reward, and absent musical pleasure simultaneously.** This would contradict the multi-step pipeline model. Musical anhedonia exists (Martínez-Molina et al., 2016), so this prediction is already confirmed.

6. **A single precondition from the five can be removed without affecting reward.** For example: if reward fires reliably in the *complete absence* of a directed gap (Precondition 1), the five-precondition model is wrong. Eating when stuffed should not produce the same reward as eating when hungry.

---

## §9 — Honest Limitations

Five open questions where the model is uncertain or untested:

**1. Habituation vs. prediction error:** The model proposes that VTA detection is *habituation-based* (simpler than Schultz's prediction-error computation). Both produce the same observable dopamine firing patterns. Distinguishing them requires recording VTA during novel-but-predictable vs. expected-but-surprising conditions. This has not been done decisively.

**2. Goldilocks zone boundaries (Precondition 4):** Research supports an inverted-U relationship between familiarity and reward generally (Berlyne; Zajonc). But the zone is dynamic — it varies per person, per context, per need type. The model does not specify exact boundaries, only the principle. This is a real limitation.

**3. Body simulation fidelity:** The model proposes that PFC simulates outcomes and the body evaluates the simulation (Step 5). Motor imagery engaging motor cortex is established (Jeannerod, 1995). Whether abstract, non-motor content produces body-level evaluation at consistent fidelity is not yet measured cleanly.

**4. DRD4 receptor role (Step 3):** The original association between DRD4 7-repeat polymorphism and novelty-seeking is contested. The model uses DRD4 as a filter mechanism, but the evidence is mixed. The 7-step model could survive without this specific claim — Steps 2, 4, and 5 are more load-bearing.

**5. Active trigger vs. permissive tone in stimulant euphoria:** Naltrexone clearly demonstrates that opioid blockade reduces stimulant euphoria. But whether dopamine *actively triggers* opioid release (Colasanti et al., 2012) or tonic opioid tone is a *permissive condition* (Jayaram-Lindström et al., 2017) is unresolved. New genetically encoded opioid biosensors (Bhatt et al., 2024, *Nature Neuroscience*) may resolve this. Either way, the core conclusion — dopamine ≠ reward — holds regardless of which sub-mechanism is correct.

**Author transparency:** This framework was developed by an independent researcher (game developer by background), not a neuroscientist. It builds directly on established research but proposes novel synthesis. The claims are structured for falsification specifically so that domain experts can identify errors. Credentials should not determine truth — evidence should. But the lack of lab access means the novel claims are untested by the author's own experiments.

---

## §10 — Call to Verify

This framework is open-source (CC0 — no rights reserved) and structured for verification.

**What you can do:**

- **Read the source:** The full framework (200+ files, CC0 licensed) is available at [github.com/hoanispof/Human-Predictive-Drive](https://github.com/hoanispof/Human-Predictive-Drive). The dopamine claim is one of approximately 20 positions where the framework diverges from mainstream accounts. Each divergence has its own file with evidence, confidence levels, and falsification criteria.

- **Stress-test with AI:** Clone the repository. Feed it to Claude, GPT, or any capable AI. Ask: "Check the citations in Dopamine-Is-Not-Reward.md — do the cited papers actually say what the framework claims?" AI can verify logical consistency and citation accuracy. It cannot verify empirical truth or replication status — that requires domain expertise.

- **Contribute counter-evidence:** If the mechanism doesn't match your expertise, your observation, or your data — **that is the most valuable contribution possible.** Confirmation is easy to find (our brains are wired for it). Contradiction requires careful observation. If you find something that doesn't fit, please share it.

- **Check the claims list:** A claims checklist with falsification criteria will be available in the repository.

**What counter-evidence looks like:**

- "Study X (published in Y, n=Z) directly demonstrates pleasure from pure dopamine stimulation without opioid involvement." → This would challenge Evidence 2 and the opioid-centrality claim.
- "I work with musical anhedonia patients and the auditory-NAcc connectivity finding doesn't replicate." → This would challenge Evidence 3.
- "Here's a population of gambling addicts with no physiological arousal during gambling." → This would challenge the body-evaluation claim (Step 5).

**What this is not:**

This is not self-help. This is not "understand your dopamine to optimize your life." This is a proposed mechanism inviting expert review. If it survives scrutiny, the implications follow naturally. If it doesn't survive — that's progress too.

---

## References

Adamantidis, A. R., et al. (2011). Optogenetic interrogation of dopaminergic modulation of the multiple phases of reward-seeking behavior. *Journal of Neuroscience*, 31(30), 10829–10835.

Berridge, K. C., & Robinson, T. E. (1998). What is the role of dopamine in reward: hedonic impact, reward learning, or incentive salience? *Brain Research Reviews*, 28(3), 309–369.

Berridge, K. C., & Robinson, T. E. (2016). Liking, wanting, and the incentive-sensitization theory of addiction. *American Psychologist*, 71(8), 670–679.

Bhatt, D. L., et al. (2010). Mu-opioid receptor knockout in mice: effects on nicotine reward. *Neuropsychopharmacology*, 35(13), 2529–2537.

Bhatt, S., et al. (2024). Genetically encoded opioid biosensors for in vivo detection. *Nature Neuroscience*, 27, 1263–1274.

Brickman, P., Coates, D., & Janoff-Bulman, R. (1978). Lottery winners and accident victims: Is happiness relative? *Journal of Personality and Social Psychology*, 36(8), 917–927.

Chase, H. W., & Clark, L. (2010). Gambling severity predicts midbrain response to near-miss outcomes. *Journal of Neuroscience*, 30(18), 6180–6187.

Colasanti, A., et al. (2012). Endogenous opioid release in the human brain reward system induced by acute amphetamine administration. *Biological Psychiatry*, 72(5), 371–377.

Collins, A. M., & Loftus, E. F. (1975). A spreading-activation theory of semantic processing. *Psychological Review*, 82(6), 407–428.

Jayaram-Lindström, N., et al. (2004). Naltrexone attenuates the subjective effects of amphetamine in patients with amphetamine dependence. *Journal of Clinical Psychopharmacology*, 24(6), 665–669.

Jayaram-Lindström, N., et al. (2008). Naltrexone for the treatment of amphetamine dependence: a randomized, placebo-controlled trial. *American Journal of Psychiatry*, 165(11), 1442–1448.

Jayaram-Lindström, N., et al. (2017). Dopamine release in nucleus accumbens during rewarding events — a [11C]raclopride PET study. *Translational Psychiatry*, 7, e1040.

Jeannerod, M. (1995). Mental imagery in the motor context. *Neuropsychologia*, 33(11), 1419–1432.

Koob, G. F., & Volkow, N. D. (2010). Neurocircuitry of addiction. *Neuropsychopharmacology*, 35(1), 217–238.

Liggins, J., et al. (2012). Effects of levodopa on mood in healthy adults. *Neuropsychopharmacology*, 37(8), 1816–1825.

Linnet, J., et al. (2011). Dopamine release in ventral striatum during Iowa Gambling Task performance is associated with increased excitement levels in pathological gambling. *Addiction*, 106(2), 383–390.

Loas, G., et al. (2012). Anhedonia in Parkinson's disease: an overview. *Journal of Neuropsychiatry and Clinical Neurosciences*, 24(4), 444–451.

Martínez-Molina, N., et al. (2016). Neural correlates of specific musical anhedonia. *Proceedings of the National Academy of Sciences*, 113(46), E7337–E7345.

Mick, I., et al. (2014). Amphetamine induced endogenous opioid release in the human brain detected with [11C]carfentanil PET: replication in an independent cohort. *International Journal of Neuropsychopharmacology*, 17(12), 2069–2074.

Mick, I., et al. (2016). Blunted endogenous opioid release following an oral amphetamine challenge in pathological gamblers. *Neuropsychopharmacology*, 41(7), 1742–1750.

Olds, J., & Milner, P. (1954). Positive reinforcement produced by electrical stimulation of septal area and other regions of rat brain. *Journal of Comparative and Physiological Psychology*, 47(6), 419–427.

Peciña, S., & Berridge, K. C. (2005). Hedonic hot spot in nucleus accumbens shell: where do mu-opioids cause increased hedonic impact of sweetness? *Journal of Neuroscience*, 25(50), 11777–11786.

Ray, L. A., et al. (2015). Effects of naltrexone on subjective and physiological responses to IV methamphetamine. *Neuropsychopharmacology*, 40(10), 2434–2441.

Robinson, T. E., & Berridge, K. C. (2003). Addiction. *Annual Review of Psychology*, 54, 25–53.

Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593–1599.

Sharpe, L. (2004). Patterns of autonomic arousal in imaginal situations of winning and losing in problem gambling. *Journal of Gambling Studies*, 20(1), 95–104.

Sienkiewicz-Jarosz, H., et al. (2005). Taste responses in patients with Parkinson's disease. *Journal of Neurology, Neurosurgery, and Psychiatry*, 76(1), 40–46.

Spencer, T. J., et al. (2018). Effect of naltrexone on the subjective response to methylphenidate. *Journal of Clinical Psychopharmacology*, 38(3), 246–250.

Weintraub, D., et al. (2010). Impulse control disorders in Parkinson disease: a cross-sectional study of 3090 patients. *Archives of Neurology*, 67(5), 589–595.

---

*Draft v0.1 — 2026-05-31*
*Full framework: [github.com/hoanispof/Human-Predictive-Drive](https://github.com/hoanispof/Human-Predictive-Drive)*
*License: CC0 1.0 Universal — use, modify, challenge freely*
*The most valuable response you can give is a specific counterexample: a finding, observation, or dataset that contradicts something claimed here. The second most valuable is a question about something unclear. Agreement is nice but doesn't advance knowledge.*
