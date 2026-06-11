---
title: Addiction Analysis — How Addiction Works Through v7.8 Architecture
version: v3.1
source: Research/Health-Conditions/Hijack/Addiction-Analysis.md v3.1
translated: 2026-06-09
status: COMPLETE
scope: |
  OVERVIEW FILE: How addiction works through v7.8 cycle-based architecture.
  Chunk-loop hijack mechanism. Evaluative/Direct-State reward bypass.
  Body-Coupling × Withdrawal. PFC-Configuration × Addiction stages.
  Recovery = re-compilation pathway.
  3 classification groups (Chemical / Behavioral / Schema-based) — PRINCIPLES, not per-substance drill.
  Self-medication pattern. Honest Assessment + Open Questions.
purpose: |
  OVERVIEW for the Chemical-Hijack/ folder.
  Describes the GENERAL MECHANISM — substance-specific drills in separate files:
    Alcohol-Brain-Mechanism.md (v1.0) — available.
    Other substances — drill later if needed.
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Addiction Analysis — How Addiction Works Through v7.8 Architecture

> **You scroll your phone for 2 hours. You put it down. Empty.**
> **You drink every evening. Skip one day. A restlessness you can barely stand.**
> **You work 14 hours a day. Go on vacation. "I've lost myself."**
>
> 3 DIFFERENT sources. Same 1 pattern: CANNOT STOP even when you KNOW you should.
>
> Pop science calls it: "dopamine addiction." Framework says: WRONG.
> Dopamine = the doorbell ("something worth attending to"). Addiction = the gift behind the door.
>
> Addiction through v7.8: **the chunk-reward loop is hijacked**.
> Substance/behavior bypasses Body-Feedback-Precondition preconditions → delivers reward
> WITHOUT serving a real body-need → compiles "shortcut" chunks →
> tolerance = baseline shift → withdrawal = body-coupling disruption.
>
> This file: GENERAL MECHANISM — how addiction works.
> Drill for specific substances → separate files (Alcohol-Brain-Mechanism.md available).
>
> **Read first**: Dopamine-Is-Not-Reward.md (why dopamine ≠ reward).
> **Read first or in parallel**: 03-Reward.md (Body-Feedback-Precondition 5 preconditions).

---

## Table of Contents

- §0 — POSITION + SCOPE
- §1 — CORRECTING THE MISCONCEPTION: "DOPAMINE ADDICTION" IS WRONG
- §2 — GENERAL MECHANISM: CHUNK-REWARD LOOP HIJACK
- §3 — EVALUATIVE/DIRECT-STATE × ADDICTION: HOW REWARD IS ATTACKED
- §4 — CLASSIFICATION BY MECHANISM: 3 GROUPS
- §5 — WITHDRAWAL = BODY-COUPLING DISRUPTION
- §6 — PFC-CONFIGURATION × ADDICTION STAGES
- §7 — RECOVERY = RE-COMPILATION PATHWAY
- §8 — SELF-MEDICATION PATTERN
- §9 — HONEST ASSESSMENT + OPEN QUESTIONS
- §10 — CROSS-REFERENCES

---

## §0 — POSITION + SCOPE

```
⭐ THIS FILE WITHIN THE FRAMEWORK:

  OVERVIEW for the Chemical-Hijack/ folder.
  Describes the GENERAL MECHANISM — how addiction works through v7.8.

  HOW THIS FILE DIFFERS FROM RELATED FILES:

    ┌────────────────────────────┬────────────────────────────────────────┐
    │ File                       │ Scope                                  │
    ├────────────────────────────┼────────────────────────────────────────┤
    │ Addiction-Analysis.md      │ GENERAL MECHANISM: why addiction       │
    │ (THIS FILE)                │ occurs, how it works, how recovery     │
    │                            │ works — NOT per-substance drill.       │
    ├────────────────────────────┼────────────────────────────────────────┤
    │ Alcohol-Brain-Mechanism.md │ SUBSTANCE-SPECIFIC: ethanol × 5 brain  │
    │ (v1.0, available)          │ systems, BAC gradient, 6 individual   │
    │                            │ variants, specific withdrawal.         │
    ├────────────────────────────┼────────────────────────────────────────┤
    │ Alcohol-Vietnam-           │ CULTURAL-SPECIFIC: alcohol × Vietnamese│
    │ Generational.md (v1.0)     │ generational patterns, ALDH2 gene,    │
    │                            │ trends.                                │
    ├────────────────────────────┼────────────────────────────────────────┤
    │ [Future substance files]   │ Per-substance drill: cocaine, opioids, │
    │                            │ nicotine, MDMA, cannabis...            │
    │                            │ If needed — drill later.               │
    └────────────────────────────┴────────────────────────────────────────┘

  STRUCTURAL PATTERN ALREADY IN FRAMEWORK:
    Body-Feedback.md (overview) → 01-Foundation, 02-Dissonance, 03-Reward (drill)
    Feeling.md (overview) → Feeling-Mechanism-Deep, Feeling-Sources (drill)
    Addiction-Analysis.md (overview) → Alcohol-Brain-Mechanism.md (drill)

  V2 → V3.0 REFRAME:
    v2 (v7.5): "Imagine layer DISCONNECTS from Body-Base"
    v3.0 (v7.8): "Chunk-reward loop hijacked — Body-Feedback-Precondition bypass
      + shortcut compile"
    v2 core insight STILL VALID — only terminology + mechanism depth changed.
```

---

## §1 — CORRECTING THE MISCONCEPTION: "DOPAMINE ADDICTION" IS WRONG

### §1.1 — 3 positions in the debate

```
🟢🟡 COMPARING 3 POSITIONS — SAME QUESTION, DIFFERENT ANSWERS:

  ┌───────────────────────────────────────────────────────────────────┐
  │ CLASSICAL (1950s–1990s → current pop science):                    │
  │                                                                   │
  │   "Dopamine = reward/pleasure chemical."                          │
  │   "Addiction = the dopamine system is hyperactive."               │
  │   "Dopamine detox = the solution."                                │
  │                                                                   │
  │   Problem: 25+ years of research have refuted this.              │
  │   Pop science + mainstream textbooks STILL repeat it.             │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ BERRIDGE-ROBINSON (1998–present — current research consensus):    │
  │                                                                   │
  │   "Dopamine = WANTING (incentive salience), NOT pleasure."        │
  │   "Liking (pleasure) = primarily the opioid system."             │
  │   "Two systems SEPARATED: you can want without liking."           │
  │                                                                   │
  │   Limitation: separates wanting/liking but does NOT describe      │
  │   the specific mechanism of liking. "Opioid system" = black box. │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ FRAMEWORK v7.8:                                                   │
  │                                                                   │
  │   Dopamine = VTA detects delta → alerts PFC: "THERE'S A SHIFT"   │
  │   = THE DOORBELL — signals salience, NOT reward.                  │
  │                                                                   │
  │   Reward = body-base opioid release WHEN chunk fits body-need.   │
  │   = THE GIFT BEHIND THE DOOR — actual reward, dependent on       │
  │     Body-Feedback-Preconditions.                                  │
  │                                                                   │
  │   7-step mechanism (detail: Dopamine-Is-Not-Reward.md §4):        │
  │   ① Neurons fire 24/7 → ② VTA detects delta → ③ DRD4 filter →   │
  │   ④ PFC spotlight → ⑤ Body-base check (body-need match?) →       │
  │   ⑥ Opioid release IF match → ⑦ COMT clears dopamine.            │
  │                                                                   │
  │   Step ⑤ = CRITICAL: the body-base CHECK.                        │
  │   Body-need matches → opioid → REAL reward.                       │
  │   No match → "meh" → PFC discards → EMPTINESS.                   │
  │                                                                   │
  │   → "Dopamine addiction" is WRONG because:                        │
  │   Dopamine = the doorbell. Nobody is addicted to the sound of a  │
  │   doorbell. Addiction = the content behind it (opioid body reward)│
  │                                                                   │
  │   v1.1 UPDATE: Opioid reward = primarily Evaluative.              │
  │   Direct-State reward (touch, exercise) = non-opioid pathways.   │
  │   Detail: Reward-Signal-Architecture.md §1–§3.                    │
  └───────────────────────────────────────────────────────────────────┘

  🟢 Berridge & Robinson 1998, 2003, 2016 — wanting ≠ liking.
  🟢 Schultz 1997 — prediction error signal.
  🟢 Koob & Volkow 2010 — addiction = allostatic, multi-system.
  Detail on 7 pieces of evidence: Dopamine-Is-Not-Reward.md §3.
```

### §1.2 — Why this misconception MATTERS for addiction

```
🟡 WRONG MECHANISM → WRONG SOLUTION:

  If you believe "dopamine addiction":
    → "Dopamine detox" = the solution → WRONG
    → "Reduce dopamine" = the goal → WRONG (dopamine is NEEDED for function)
    → "Block novelty" = how to quit → WRONG (novelty = healthy drive)

  If you understand "addiction = body reward hijacked":
    → The right question: "Body reward from WHERE? Does the reward SERVE
        a body-need?"
    → The right solution: replace the SOURCE of reward, not block the signal
    → Recovery: re-build body reward from REAL sources (§7)

  Example: scrolling social media
    ❌ "Dopamine addiction" → solution: put the phone away → fails because
       there is no alternative reward source yet → returns to scrolling
    ✅ "Mild body reward from content" → solution: replace with
       STRONGER body reward (exercise, real connection, creative project)
       → scrolling becomes NOT COMPELLING ENOUGH
```

---

## §2 — GENERAL MECHANISM: CHUNK-REWARD LOOP HIJACK

### §2.1 — Normal cycle vs Addiction cycle

```
🟡 NORMAL CYCLE (v7.8 Core-Software.md):

  Domain → Body-Input → Unconscious Processing → Feeling → PFC →
  Body-Output → Domain
                             ↑
               Chunk-System evaluates:
               Body-need gap? → Behavior → Input → Body-base check →
               Match? → Opioid reward → Gap closes → STOPS.

  KEY FEATURES:
    ① A REAL body-need gap exists first (Precondition-1 Directed-Gap)
    ② Behavior serves that gap (eat when hungry, drink when thirsty)
    ③ Body-base CHECK after behavior: "does this meet the need?"
    ④ Match → opioid → reward → gap closes → cycle STOPS naturally
    ⑤ All 5 Body-Feedback-Preconditions must be met (03-Reward.md §3)


  ADDICTION CYCLE — WHERE THE HIJACK OCCURS:

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  HIJACK POINT 1 — Body-Feedback-Precondition BYPASS:               │
  │                                                                     │
  │    Chemical attacks receptor/neurotransmitter systems DIRECTLY      │
  │    → delivers opioid (or opioid-like signal) WITHOUT needing        │
  │      Preconditions 1 through 5:                                     │
  │                                                                     │
  │    Precondition-1 Directed-Gap (Schema pending — body-need gap):   │
  │      Normal: needs a REAL gap. Addiction: substance creates reward  │
  │      WITHOUT a gap, or with an UNRELATED gap                        │
  │      (hungry → drink alcohol, sad → smoke)                         │
  │                                                                     │
  │    Precondition-2 Chunk-Substrate (Compiled chunks — evaluation     │
  │      capacity):                                                     │
  │      Normal: needs chunks to evaluate "is this input good?"         │
  │      Addiction: substance BYPASSES evaluation → reward directly     │
  │                                                                     │
  │    Precondition-3 Delta-Gate (prediction-delta — novelty signal):  │
  │      Normal: needs prediction-delta. Addiction: substance FLOODS    │
  │      dopamine → VTA overwhelmed → abnormal signal                   │
  │                                                                     │
  │    Precondition-4 Match-Range (Goldilocks zone — dynamic):         │
  │      Normal: Goldilocks zone = optimal. Addiction: substance        │
  │      OVERRIDES → reward intensity far exceeds Goldilocks →         │
  │      over-reward                                                    │
  │                                                                     │
  │    Precondition-5 Compile-Gate (Chunk tag — cortisol direction):   │
  │      Normal: novelty cortisol → approach. Addiction: substance      │
  │      MAY tag positive DESPITE harming the body (§2.3 false         │
  │      positive)                                                      │
  │                                                                     │
  │  → CHEMICAL = BYPASSES Body-Feedback-Preconditions, delivers       │
  │    reward WITHOUT going through body-base check                     │
  │  → BEHAVIORAL = EXPLOITS Body-Feedback-Precondition weaknesses     │
  │    (variable ratio, low cost)                                       │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  HIJACK POINT 2 — THE CYCLE NEVER STOPS:                           │
  │                                                                     │
  │    Normal: body-need met → gap closes → cycle stops naturally.      │
  │    Addiction: reward does NOT serve a real body-need →              │
  │      gap NEVER CLOSES (because the real need is unmet) →            │
  │      cycle REPEATS → mild reward each time → "shortcut" compiles → │
  │      shortcut chunks GROW STRONGER → override other body signals.   │
  │                                                                     │
  │    Example: sadness (need = connection) → drink alcohol → mild      │
  │    opioid → sadness STILL THERE (no connection yet) → drink more → │
  │    more opioid → loop with NO natural stopping point.               │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  HIJACK POINT 3 — COMPILING "SHORTCUT" CHUNKS:                     │
  │                                                                     │
  │    Each time: substance → reward:                                   │
  │    Body compiles chunk: [situation X → use substance → reward]      │
  │    Repeated many times → chunk STRENGTHENS (Chunk.md §2 compile    │
  │    via repetition + emotional peak).                                │
  │    Gradually: the "shortcut" chunk BECOMES STRONGER than alternative│
  │    chunks → higher activation probability → fires before other      │
  │    chunks → body "automatically" orients toward the substance.      │
  │                                                                     │
  │    = Chunk-Activation-Dynamics.md: probability-weighted activation. │
  │    Addiction chunk has HIGH probability → fires FIRST → dominates.  │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘
```

### §2.2 — 4-Phase Progression through v7.8

```
🟡 4 PHASES — SAME PATTERN FOR ALL TYPES OF ADDICTION:

  Rate + speed VARY per-substance/behavior,
  but PROGRESSION LOGIC is the same.


  PHASE 1 — PULL (first times → several times):

    Input → REAL body reward (at least the first time) → "pleasant"
    → Body learns: [substance X → reward]
    → Chunk compile begins (Compile-Taxonomy: Pathway 1 — Hardware Fit)

    ⭐ PREREQUISITE: REAL body reward the first time.
    If the first time produces NO body reward → "nothing to it" →
    no repetition → no addiction.
    Body MUST learn "X → reward" BEFORE addiction can form.

    🟢 Koob & Le Moal 2001 — initial positive reinforcement phase.


  PHASE 2 — TOLERANCE (uses 10–50+):

    Reward-Calibration.md: Goldilocks SHIFTS.
    → Body adapts baseline: yesterday's reward = today's normal.
    → VTA habituates: same dose → SMALLER delta → WEAKER dopamine alert.
    → Receptors downregulate: MORE needed for the same opioid response.
    → = Goldilocks zone SHIFTS UP — needs HIGHER dose to reach "match."

    Simultaneously:
    → Natural hormone production DECREASES (body relies on substance
        instead of self-producing).
    → Body reward from REAL sources (good food, seeing friends) becomes
        BLAND compared to chemical reward → anhedonia gradually forms.
    → "Shortcut" chunks STRONGER than alternative chunks.

    🟢 Koob & Volkow 2016 — opponent process theory, allostatic shift.
    🟢 Nestlé & Aghajanian 1997 — receptor downregulation.


  PHASE 3 — PUSH (long-term):

    SHIFT from "using because it FEELS GOOD" →
    "using because NOT USING = SUFFERING."

    → Not using = withdrawal:
      - Receptors already downregulated → natural hormones EXTREMELY LOW
      - Cortisol RISES (Role ① Compile Direction: threat tag)
      - Body state EXTREMELY BAD → dissonance at HIGH intensity
    → Using = END of withdrawal (relief, NOT the original euphoria)
    → = REWARD TYPE CHANGES:
      Phase 1: Pull reward = "pleasant" (positive reinforcement)
      Phase 3: Push reward = "the suffering stops" (negative reinforcement)
    → Reward-Signal-Architecture: reward shifts from Profile ①
        Sensory/② Coherence → Profile ④ Relief (pain/dissonance stops = reward)

    🟢 Koob 2013 — negative reinforcement drives late-stage addiction.


  PHASE 4 — DEPENDENCY:

    → Hormone system FULLY COLLAPSED.
    → Not using = EXTREME body threat
      (chemical: pain, tremors, vomiting, potentially fatal — varies by substance).
    → "Shortcut" chunks COMPILED DEEPLY:
      [feeling X → use substance] → automatic, PFC can barely intervene.
    → Schema: "using X = SURVIVING" (substance hijacked from luxury
        → survival need).
    → PFC-Configuration: withdrawal triggers Config ④ (Disconnected) →
      PFC offline → subcortical takeover → relapse probability EXTREME.

    🟢 Koob & Volkow 2010 — addiction as brain disease model.
    🟢 Arnsten 2009 — stress-induced PFC dysfunction.
```

### §2.3 — Why the body is "tricked" — False Positive Mechanism

```
🟡 BODY-BASE CHECK (7-step Step ⑤) WORKS CORRECTLY 100% OF THE TIME —
   THE PROBLEM IS THAT CHEMICALS BYPASS THE CHECK, NOT DECEIVE IT:

  Body-base check: "does this chunk match a body-need?"
  → The check mechanism STILL FUNCTIONS correctly.
  → PROBLEM: chemical DELIVERS opioid DIRECTLY into receptors,
    WITHOUT GOING THROUGH the check.

  Example — heroin:
    Normal: [eat good food → taste → brainstem evaluates → match? → opioid]
    Heroin: [heroin → mu-opioid receptor DIRECTLY → opioid]
    → Body-base check is BYPASSED, not deceived.
    → = The substance does NOT enter through the front door (the check)
        — it breaks through the back door (the receptor).

  Example — alcohol:
    → GABA↑ → REAL relaxation (body-state improves) = Direct-State reward
    → + mild opioid (NAcc, Mitchell 2012) = Evaluative reward
    → Body-base check: "relaxation? ✅" → but does NOT check:
      "does this relaxation SERVE a long-term body-need?"
    → Body-base check = SHORT-TERM evaluator, not a long-term planner.
    → PFC = long-term planner, but PFC reach into Zone C/D is weak
        (Core-Hardware.md §2).

  → FUNDAMENTAL LIMITATION:
    Body-base check evaluates IMMEDIATE FIT (short-term).
    Long-term consequences = PFC territory.
    Chemical BYPASSES body-base check + PFC is REDUCED/OFFLINE by the substance.
    → = BOTH lines of defense are simultaneously neutralized.
```

---

## §3 — EVALUATIVE/DIRECT-STATE × ADDICTION: HOW REWARD IS ATTACKED

### §3.1 — Principle: Does the chemical attack Evaluative or Direct-State?

```
🟡 REWARD HAS 2 TYPES (Reward-Signal-Architecture v1.0 §1):

  Evaluative — EVALUATIVE CONFIRM:
    Circuit: Hedonic hotspot (NAcc shell, VP, mOFC). μ-opioid primary.
    Body-Feedback-Precondition: Full 5 preconditions REQUIRED.
    Learned: YES — quality depends on chunk library.
    Examples: Food, music, insight, social praise.

  Direct-State — DIRECT STATE CONFIRM:
    Circuit: Interoceptive / body-state regulation. VARIES by modality.
    Body-Feedback-Precondition: Simplified (Precondition-1 basic,
      Preconditions 2–5 reduced/N/A).
    Learned: MINIMAL — hardware from birth.
    Examples: Touch comfort, exercise, warmth, stretching.


  ADDICTION ATTACKS BOTH — BUT IN DIFFERENT WAYS:

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  EVALUATIVE HIJACK — "BREAKING THROUGH THE EVALUATION BACK DOOR":  │
  │                                                                     │
  │    Normal Evaluative: Input → compiled chunks evaluate → match? →  │
  │    hedonic hotspot → μ-opioid → reward.                             │
  │    = Goes THROUGH the evaluation gate.                              │
  │                                                                     │
  │    Chemical hijack: substance → DIRECTLY activates receptor →       │
  │    opioid signal → reward. BYPASSES the evaluation gate.            │
  │                                                                     │
  │    Heroin/morphine: mu-opioid receptor DIRECTLY.                    │
  │    Cocaine: blocks DAT → dopamine floods + indirect opioid.        │
  │    Alcohol: mild opioid at NAcc (Mitchell 2012).                    │
  │                                                                     │
  │    → Evaluative hijacked = "counterfeit gift delivered directly,    │
  │      no inspection."                                                │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  DIRECT-STATE HIJACK — "REAL BODY-STATE CHANGE, BUT NOT LASTING":  │
  │                                                                     │
  │    Normal Direct-State: body activity → body-state DIRECTLY         │
  │    improves. = Hardware pathway, minimally chunk-dependent.         │
  │                                                                     │
  │    Chemical hijack: substance changes body-state FOR REAL:          │
  │    → Alcohol: GABA↑ = REAL relaxation (muscle tension, anxiety     │
  │        decreases)                                                   │
  │    → Cannabis: endocannabinoid = REAL relaxation                    │
  │    → Nicotine: mild NE = REAL alertness                             │
  │                                                                     │
  │    Direct-State reward FROM the substance = REAL at the body-state  │
  │    level.                                                           │
  │    PROBLEM: body-state improvement is NOT LASTING,                  │
  │    + receptors adapt → tolerance → needs more.                      │
  │    + body-state does NOT improve without the substance (withdrawal). │
  │                                                                     │
  │    → Direct-State hijacked = "real gift but temporary + costly."    │
  │                                                                     │
  ├─────────────────────────────────────────────────────────────────────┤
  │                                                                     │
  │  BOTH A + B SIMULTANEOUSLY — THE MOST DANGEROUS:                   │
  │                                                                     │
  │    Most strongly addictive substances attack BOTH types:            │
  │    → Heroin: Evaluative (opioid directly) +                        │
  │               Direct-State (pain relief)                            │
  │    → Cocaine: Evaluative (opioid indirect) +                       │
  │               Direct-State (energy, alertness)                      │
  │    → Alcohol: Evaluative (mild opioid) +                           │
  │               Direct-State (GABA relaxation)                        │
  │    → MDMA: Evaluative (serotonin → opioid cross) +                 │
  │               Direct-State (warmth)                                 │
  │                                                                     │
  │    → Multi-channel attack = STRONGER hook:                          │
  │    body receives reward from MULTIPLE sources simultaneously →       │
  │    chunk compiles STRONGER (multi-modal compile, Chunk.md §2).      │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘

  🟢 Berridge 2003 — hedonic hotspot opioid mechanism.
  🟢 Mitchell et al. 2012 — alcohol triggers endorphin in NAcc + OFC.
  🟢 Fuss 2015 — endocannabinoid in exercise (Direct-State, non-opioid).
  🟢 Löken 2009 — CT afferents (Direct-State touch pathway).
```

### §3.2 — Evaluative Gates Direct-State mechanism × Addiction

```
🟡 NORMAL: EVALUATIVE EVALUATION GATES DIRECT-STATE AMPLIFICATION
   (Reward-Signal-Architecture §3):

  When both A and B fire simultaneously:
    A positive → B AMPLIFIED (good food + warmth = both feel better)
    A negative → B SUPPRESSED (good food but a friend just criticized you
      = food loses its appeal)
    = A "evaluates context" → determines whether B gets amplified.

  ADDICTION BYPASSES THIS GATE:

    Chemical → A fires DIRECTLY (no evaluation) →
    B also fires (body-state changes for real) →
    A CANNOT evaluate "is this B good long-term?" →
    = Gate neutralized → both A + B fire "unfiltered."

    → Explains why addictive substances feel "total":
    not just 1 type of pleasant but MULTIPLE simultaneously
    (relaxation + euphoria + social ease + confidence...) =
    multi-type reward without gate filtering.

  🔴 HYPOTHESIS: Addiction intensity ∝ f(number of types bypassed × depth)
    → Heroin (A bypassed directly + B pain relief) = EXTREME
    → Caffeine (B mild: alertness) = MILD
    → Cannabis (B: relaxation + A mild) = MODERATE
    → Research needed to confirm.
```

---

## §4 — CLASSIFICATION BY MECHANISM: 3 GROUPS

### §4.1 — Chemical Addiction

```
🟢🟡 PRINCIPLE: Substance attacks the neurochemical system DIRECTLY.

  COMMON FEATURES:
    → Bypasses Body-Feedback-Precondition evaluation gate (§2.1 Hijack Point 1)
    → Receptors downregulate → tolerance
    → Natural hormone production DECREASES
    → Withdrawal = body threat (mild → extreme, varies by substance)
    → Recovery: months → years (receptor upregulation is slow)

  DANGER LEVEL = f(bypass depth × speed × receptor specificity):

    Bypass depth: heroin (mu-opioid DIRECTLY) > cocaine (indirect)
                  > alcohol (multi-system mild) > caffeine (adenosine
                  block mild)

    Speed: injection/smoking (seconds) > snorting (minutes) >
           oral (30+ minutes)
           → Speed affects compile: faster = LARGER prediction-delta
           → = chunk compiles STRONGER

    Receptor specificity:
      heroin = μ-opioid specific (extreme)
      > cocaine = DAT block (dopamine flood)
      > alcohol = multi-system mild (5 systems)
      > caffeine = adenosine antagonist (very mild)

  DRD4 × CHEMICAL (PFC-Hardware.md):
    → 7R (high threshold): needs HIGHER dose to feel initial effect
    → 4R (low threshold): feels effect at LOWER dose
    → 🟢 Support: ADHD medication 7R needs higher dose
    → ⚠️ BOTH: reward comes from opioid, NOT from dopamine

  Detail per-substance: separate files.
  Alcohol: Alcohol-Brain-Mechanism.md v1.0 (available — 5 systems, BAC gradient).
  Other substances: drill later if needed.
```

### §4.2 — Behavioral Addiction

```
🟡 PRINCIPLE: Behavior creates REAL body reward via body-base channels —
   does NOT attack hormones directly, but EXPLOITS weaknesses in
   Body-Feedback-Preconditions.

  COMMON FEATURES:
    → Body-Feedback-Preconditions NOT bypassed — but EXPLOITED:
      - Variable ratio reinforcement → Precondition-3 Delta-Gate CONTINUOUSLY
      - Low-cost behavior → easy repetition → compile FAST
      - Multi-channel reward → multi-modal compile → STRONG
    → Receptors do NOT downregulate as heavily as chemical
    → Withdrawal MUCH MILDER (no severe body threat)
    → Recovery FASTER (days → weeks) — but EASY TO RELAPSE because
        the source is ALWAYS AVAILABLE

  DISTINGUISHING PRINCIPLE FROM CHEMICAL:

    Chemical: BYPASSES evaluation gate → delivers reward DIRECTLY.
    Behavioral: EXPLOITS the gate → delivers reward THROUGH the gate
               but at a frequency/pattern the gate was not designed to handle.

    Example: gambling
      → Near-miss: VTA fires LARGE delta ("SO CLOSE!") → dopamine alert →
        body simulates anticipation reward → mild opioid from anticipation →
        gate evaluates: "near-miss = valuable" → ✅ (gate CORRECT: near-miss
        IS an informative signal) → but at slot-machine frequency → exploit
      → 🟢 Clark et al. 2009: near-miss activates reward areas LIKE a win.

    Example: social media scrolling
      → Each scroll = NEW content → small prediction-delta → mild dopamine →
        body checks: "relevant?" → sometimes yes → mild opioid →
        variable ratio = Skinner schedule → gate CORRECT per-event
        but total = exploiting continuous micro-reward.
      → 🟢 Meshi et al. 2013 — social media activates NAcc.

    Example: gaming
      → Multi-channel: mastery + novelty + status + belonging + shared experience
      → 5+ body-base channels SIMULTANEOUSLY → multi-modal compile STRONG
      → Games designed: difficulty curve + reward schedule + social hooks
      → REAL body reward per-channel — the problem is REPLACING real-world
          channels.


  CHEMICAL vs BEHAVIORAL COMPARISON:

    ┌──────────────────┬──────────────────────┬──────────────────────┐
    │ Feature          │ Chemical             │ Behavioral           │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Preconditions    │ BYPASSED             │ EXPLOITED (slips      │
    │                  │ (breaks back door)   │ through front door    │
    │                  │                      │ at high frequency)    │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Receptors        │ HEAVY downregulation │ MILD downregulation  │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Natural hormone  │ Production DECREASES │ Production REMAINS   │
    │ production       │                      │ normal               │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Withdrawal       │ Body threat          │ Restlessness         │
    │                  │ (mild → fatal)       │ (not life-           │
    │                  │                      │ threatening)         │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Recovery         │ Months → years       │ Days → weeks         │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Relapse risk     │ Old schema ALWAYS    │ Source ALWAYS        │
    │                  │ present (chunks      │ available (phone,    │
    │                  │ not deleted)         │ food, games)         │
    └──────────────────┴──────────────────────┴──────────────────────┘
```

### §4.3 — Schema-Based Addiction

```
🟡🔴 PRINCIPLE: Schema compiled too deeply → CONTINUOUSLY SELF-DRIVES →
   overrides the body's "enough" signal.

  V7.8 REFRAME:
    v2: "Schema overrides body-base signals"
    v7.8: Chunk network compiled [behavior X → body-need met] BUT
          chunk network ALSO compiled [not enough X → threat] →
          2 chunk sets compete → the "not enough" chunk set WINS continuously.

  HOW THIS DIFFERS FROM THE OTHER 2 GROUPS:
    → NO chemical, NO specific behavior that is "addicted to"
    → Compiled via Pathway 2 (Trust Install) or 3 (Social Default):
      "Must be perfect" → compiled from parent/culture → child trusts →
      installs
    → Body reward SMALL but CONTINUOUS:
      each time schema is complied with → mild reward ("I'm doing it right")
    → Body's "enough" signal → overridden by schema ("not perfect enough")
    → = Reward-Calibration.md: Goldilocks zone DISTORTED by compiled schema

  EXAMPLES THROUGH V7.8:

    Perfectionism:
      → Chunk network: [perfect → safe → reward] + [not perfect → threat]
      → Each time "good enough" → body signals satisfaction → BUT chunk
        "not perfect" fires → threat → overrides satisfaction → continues → loop.
      → = Compile-Taxonomy: "not enough" chunk compiled via Pathway 4
          (Threat Avoidance) + Pathway 2 (Trust: parent said "must be perfect").

    Workaholism:
      → Chunk network: [work → mastery + status → reward] +
        [not working → lose status → threat]
      → Cortisol Role ② Holding: PFC holds "unfinished work" →
        cortisol sustained → unable to relax.
      → PFC-Configuration: stuck in Drive-PFC-Strategic → cannot shift.

    People-pleasing:
      → Chunk network: [others happy → connection reward] +
        [others unhappy → connection threat]
      → Self-Pattern-Modeling Compiled fires continuously → body responds
        to others → exhaustion
      → Empathy v2.0: burnout = f(Valence-Momentary high / Valence-Structural low).

  RECOVERY FROM SCHEMA-BASED = HARDEST:
    → Schema = identity level ("who I am")
    → Abandoning schema = identity threat → Meaning.md v2.0: anchor disrupted
    → PFC must draft NEW schema to override old schema
    → Old chunks CANNOT BE DELETED (Chunk.md: never delete) →
        only probability shift
    → = Must compile a NEW chunk set STRONGER than the old one.
```

---

## §5 — WITHDRAWAL = BODY-COUPLING DISRUPTION

### §5.1 — Hypothesis: Substance as Coupled Entity

```
🔴 NEW HYPOTHESIS — SUBSTANCE BECOMES A BODY-COUPLED ENTITY:

  Body-Coupling.md v1.1: coupling occurs when per-entity valence
  compiles deeply enough → entity becomes a structural part of body-base.

  CAN A SUBSTANCE BECOME AN "ENTITY" IN THE COUPLING SYSTEM?

  Argument FOR:
    → Repeated use + strong reward → positive valence builds gradually
    → Substance becomes part of body-base: "morning coffee = me"
    → Removal → body responds SIMILAR to losing a coupled entity:
      grief-like response (disorientation, yearning, emptiness)
    → Body-Coupling: Phase 1 (initiate) → Phase 2 (threshold) →
      Phase 3 (sustain) — timeline corresponds to 4-phase addiction

  Argument AGAINST (important):
    → Entity coupling in Body-Coupling.md = PER-AGENT (humans)
    → Substance = OBJECT, not an agent
    → Valence-Propagation §2: "Object NEVER has the Body-Base Extension
        dimension"
    → Coupling requires Self-Pattern-Modeling → does a substance have
        Self-Pattern-Modeling?

  RESOLUTION — PARTIAL COUPLING:
    → Substance does NOT couple at the agent level (no Self-Pattern-Modeling,
        no Valence-Structural reward)
    → Substance MAY couple at the BODY-STATE level:
      Body state while using substance = "normal"
      Body state WITHOUT substance = "abnormal, threatening"
      = BODY-BASE SHIFT, not agent coupling.
    → Closer to Body-Feedback-Mechanism.md:
      Quality Baseline Shift (§5) — baseline MOVES
      → removal = Chunk-Miss (baseline expected, not present)
    → = WITHDRAWAL = body-base baseline disruption + cortisol amplification,
      NOT agent-level grief.

  ⚠️ BUT: heavy addiction withdrawal DOES have grief-like features
    (yearning, identity disruption, emptiness) → partial overlap.
    Framework honest: the exact mechanism is NOT yet fully clear.
```

### §5.2 — Withdrawal Mechanism through v7.8

```
🟡 WITHDRAWAL = BODY-BASE BASELINE DISRUPTED + CORTISOL AMPLIFICATION:

  ① RECEPTOR DOWNREGULATION (Tolerance has already occurred):
     → Body reduces receptor sensitivity + reduces natural hormone production
     → NEW baseline = "with substance = normal"
     → Removing the substance = baseline BREAKS:
       natural hormones EXTREMELY LOW + receptors haven't yet upregulated

  ② CHUNK-MISS DYNAMICS (Body-Feedback-Mechanism §3):
     → Body EXPECTS body-state X (with substance) → body-state X DOESN'T ARRIVE
     → = Chunk-Miss: expected pattern doesn't match reality
     → Dissonance signal STRONG — proportional to the degree of expectation

  ③ CORTISOL AMPLIFICATION (Cortisol-Baseline.md §7.7):
     → Withdrawal = threat → cortisol sustained
     → Cortisol Role ① Compile Direction: tags withdrawal = THREAT
     → Cortisol Role ② Holding: PFC holds "need substance" → cannot release
     → Cortisol Role ④ Inertia: withdrawal cortisol PROLONGS even past peak
     → = Cortisol does NOT cause withdrawal, but AMPLIFIES + EXTENDS it

  ④ PFC DEGRADATION:
     → Chronic substance use → PFC dendrite retraction
       (Cortisol-Baseline.md §9: PFC damage timeline)
     → Withdrawal + cortisol → PFC continues to weaken →
       decision-making IMPAIRED → relapse probability INCREASES
     → = Spiral: withdrawal → cortisol → weakened PFC →
         harder to resist → relapse

  ⑤ WITHDRAWAL SEVERITY GRADIENT:
     → Chemical: Heroin > Alcohol (long-term) > Cocaine > Nicotine >
                  Cannabis > Caffeine
     → Behavioral: MUCH MILDER (no heavy receptor downregulation)
     → Schema: identity crisis (not a body withdrawal)

  🟢 Koob 2008 — anti-reward, allostatic load.
  🟢 Arnsten 2009 — PFC dysfunction under stress.
  🟢 Valenzuela 1997 — GABA-A downregulation + NMDA upregulation
       (alcohol-specific).
```

---

## §6 — PFC-CONFIGURATION × ADDICTION STAGES

```
🟡 PFC-CONFIGURATION.MD v1.0: 6 DYNAMIC MODES.
   EACH ADDICTION STAGE → PFC IN A DIFFERENT MODE:

  ┌──────────────────┬──────────────────────┬──────────────────────────┐
  │ Stage            │ PFC Config           │ Mechanism                │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ First try        │ Config ① Normal      │ PFC evaluates normally   │
  │                  │                      │ → "let's try this"       │
  │                  │                      │ → body reward → PFC notes│
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Regular use      │ Config ① → ②         │ Substance-seeking tasks  │
  │ (Phase 1–2)      │ Reallocation         │ get more PFC bandwidth   │
  │                  │                      │ → self-monitoring        │
  │                  │                      │   DECREASES              │
  │                  │                      │ → "know it's harmful     │
  │                  │                      │    but don't care"       │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Intense craving  │ Config ② extreme     │ PFC bandwidth ALL GOES   │
  │                  │ → approaching ④      │ into seeking → other     │
  │                  │                      │ functions nearly lost    │
  │                  │                      │ → approaching subcortical│
  │                  │                      │   takeover               │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Withdrawal       │ Config ④             │ Extreme cortisol + NE    │
  │ (Phase 3–4)      │ Disconnected         │ flood → PFC OFFLINE →    │
  │                  │                      │ subcortical takeover →   │
  │                  │                      │ compiled chunks RUN →    │
  │                  │                      │ relapse probability MAX  │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ "Using despite   │ Config ② + ④         │ PFC alternates between   │
  │  knowing"        │ oscillation          │ "knowing it's harmful"   │
  │                  │                      │ (①→②) and "can't resist" │
  │                  │                      │ (④) → oscillation =      │
  │                  │                      │ torment                  │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ Recovery         │ Config ① stable      │ PFC needs STABLE Config  │
  │                  │ (needs rebuilding)   │ ① to hold new schemas →  │
  │                  │                      │ compile competing chunks  │
  │                  │                      │ → REQUIRES safe           │
  │                  │                      │   environment            │
  └──────────────────┴──────────────────────┴──────────────────────────┘

  ⭐ KEY INSIGHT:
    → "Knowing it's harmful but still using" = NOT a lack of willpower.
    → = PFC Config ④ (offline) during craving/withdrawal →
      compiled subcortical chunks RUN → PFC cannot intervene.
    → = PFC-Function.md: PFC ~200ms+, amygdala ~12ms →
      compiled addiction chunk fires BEFORE PFC can intervene.
    → = Similar to your hand pulling away from a hot stove before you
        "know" it's hot — the body responds first, PFC learns after.

  🟢 Goldstein & Volkow 2011 — impaired prefrontal function in addiction.
  🟢 Arnsten 2009 — stress-induced PFC dysfunction.
  🔴 Config oscillation model = framework hypothesis.
```

---

## §7 — RECOVERY = RE-COMPILATION PATHWAY

### §7.1 — Principle: Chunks are not deleted, only compete

```
🟡 CHUNK.MD v2.1: THE BRAIN NEVER DELETES A CHUNK.
   Recovery = NOT "erasing addiction." Recovery = BUILDING a new stronger
   chunk set.

  ① Addiction chunks STILL EXIST — only activation probability DECREASES.
     → Trigger (context, stress, people) → chunk MAY fire again
     → = Why relapse CAN occur MANY YEARS after quitting
     → = Chunk.md: "never delete — only probability shift"

  ② Recovery = compile a NEW chunk set competing on the same trigger:
     → Old trigger: [stress → use substance → reward]
     → New chunk: [stress → exercise → REAL reward] or
                  [stress → call a friend → connection reward]
     → 2 chunk sets compete → the STRONGER one wins
     → Recovery = making the new chunk STRONGER than the old one

  ③ New chunks compile SLOWLY (same 4 mechanisms: repetition + emotional
     peak + multi-modal + sleep):
     → Addiction chunk compiled over MANY YEARS → very strong
     → New chunk starts from 0 → needs TIME + REPETITION + SLEEP
     → = Why recovery = a long process, not a single event

  ④ ENVIRONMENT matters:
     → Environment contains TRIGGERS → addiction chunk fires →
         probability RISES again
     → NEW environment = fewer triggers → new chunk has SPACE to compile
     → 🟢 Alexander 1978 "Rat Park": rats with a good environment →
         less addiction
     → = Environment reduces the trigger surface → gives the new chunk
         a chance
```

### §7.2 — Direct-State as Recovery Floor

```
🟡 REWARD-SIGNAL-ARCHITECTURE V1.0 §1.4:
   DIRECT-STATE = "EVOLUTIONARY FLOOR" — ALWAYS AVAILABLE.

  Evaluative: MAY be damaged by addiction
    → Receptor downregulation → E₁–E₃ evaluation impaired
    → Anhedonia: "eating without taste, listening to music and feeling empty"

  Direct-State: HARDWARE-BASED → STILL accessible
    → Touch comfort: CT afferents STILL functional
    → Exercise: endocannabinoid pathway STILL functional
    → Warmth, stretching: interoceptive pathways STILL functional

  → DIRECT-STATE = "BACKDOOR" WHEN EVALUATIVE IS STUCK:
    → Anhedonia (Evaluative exhausted) → Direct-State can still provide
        BASELINE reward
    → Body-oriented approaches: exercise, massage, yoga, walk in nature
    → 🟢 Van der Kolk 2014: body-oriented therapy effective for
        trauma/addiction
    → = Activate Direct-State pathways → body gets SOME reward →
      cortisol decreases slightly → PFC stabilizes → Config ① possible →
      Evaluative recovery can BEGIN

  → Recovery pathway:
    Direct-State floor (stabilize) → PFC Config ① (rebuild) →
    Evaluative gradually recovers → new chunks compile →
    competing with addiction chunks
```

### §7.3 — Social Coupling as Recovery Resource

```
🟡 CONNECTION.MD V3.1 + BODY-COUPLING.MD V1.1:

  Social connection provides:
    → Valence-Momentary reward (Self-Pattern-Modeling-owned —
        seeing a friend → feels good)
    → Valence-Structural reward (Entity-compiled — a close friend =
        body-base extension)
    → = ALTERNATIVE reward source that doesn't require the substance

  Recovery programs (AA, NA, therapy groups):
    → Group = REAL connection reward
    → Shared experience = Self-Pattern-Modeling Compiled fires →
        empathy → Valence-Momentary reward
    → Sustained relationship = Valence-Structural coupling builds →
        structural support
    → = Body-Coupling: positive coupling with NEW people →
      competing with substance "coupling"

  ⚠️ BUT:
    → Addiction has DAMAGED connection capacity:
      - PFC weakened → Self-Pattern-Modeling impaired →
          connection harder
      - Trust chunks: many people with addiction have broken trust →
          chunk [people → threat]
      - Isolation → fewer connection chunks →
          Self-Pattern-Modeling library IMPOVERISHED
    → = Recovery needs PATIENCE + safe context for
        Self-Pattern-Modeling to rebuild

  🟢 Heilig et al. 2016 — social factors in addiction recovery.
  🟢 Kelly et al. 2020 — AA mechanism: social network change.
```

### §7.4 — Compile-Taxonomy × Recovery

```
🟡 COMPILE-TAXONOMY.MD V1.1: Recovery chunks compile via 4 pathways —
   but DIFFERENTLY per pathway:

  Pathway 1 — Hardware Fit (body rewards itself):
    → Exercise → endorphin/endocannabinoid → REAL body reward
    → Repeat → compile [exercise → reward] → competing chunk
    → STRONG because reward is REAL (no trust needed, no social needed)
    → = The MOST NATURAL recovery pathway

  Pathway 2 — Trust Install:
    → Therapist/sponsor says "you can recover"
    → Trust compiles → chunk [recovery → possible]
    → IMPORTANT in the early phase when the body isn't yet providing reward
    → ⚠️ Trust is fragile: 1 relapse → "trust was wrong → I can't"

  Pathway 3 — Social Default:
    → Recovery community: "everyone here is recovering"
    → Social default: recovery = norm → compiles gently
    → = The AA/NA model: collective default shift

  Pathway 4 — Threat Avoidance:
    → "If I use again → lose my family, lose my job"
    → Compiles [relapse → threat] → avoidance chunk
    → ⚠️ This pathway does NOT create reward — only avoidance
    → Not sustainable unless Pathways 1–3 also contribute

  → BEST RECOVERY: multiple pathways simultaneously.
    Body exercise (1) + therapist trust (2) + recovery group (3) +
    awareness of consequences (4)
    = 4 pathways compile SIMULTANEOUSLY → new chunks become STRONGER faster.
```

---

## §8 — SELF-MEDICATION PATTERN

```
🟡 SELF-MEDICATION: USING A SUBSTANCE TO HANDLE PRE-EXISTING DISSONANCE.

  Common pattern: a person with long-term dissonance (anxiety, depression,
  trauma, loneliness) → finds a substance → substance REDUCES dissonance →
  "medicine" → dependency.


  THROUGH V7.8:

  ① Dissonance exists (multiple sources):
     → Social isolation → Connection dissonance
     → Trauma → Background-Pattern.md: compiled threat pattern
     → Anxiety → Cortisol Role ② Holding: sustained cortisol
     → Boredom → Boredom.md: Imagine-Final unclear + mild continuous dissonance

  ② Substance REDUCES dissonance FOR REAL (short-term):
     → Alcohol: GABA↑ → anxiety ACTUALLY DECREASES (Direct-State:
         body-state improves)
     → Cannabis: endocannabinoid → REAL relaxation
     → Opioids: REAL pain relief (both physical AND emotional pain)
     → = Body-Feedback-Mechanism.md: Chunk-Miss decreases
         (expected state MET)

  ③ Loop forms:
     → Dissonance → substance → relief (reward) → dissonance returns
       (because ROOT CAUSE unresolved) → substance again → tolerance →
       needs more → dependency
     → = Body learns: [dissonance → substance → relief]
     → Chunk compiles AND strengthens with each repetition

  ④ Root cause STILL INTACT:
     → Substance only reduces the SYMPTOM (dissonance), doesn't fix the SOURCE
     → Isolation is still isolation. Trauma pattern still intact.
     → = Like taking painkillers without fixing a broken bone


  SELF-MEDICATION × PFC-CONFIGURATION:

    → Sustained dissonance → sustained cortisol →
      PFC approaching Config ④ (Disconnected) →
      decision quality DECREASES → substance = "easy fix" →
      PFC while using substance: temporary shift to ① (GABA relaxes PFC) →
      "feels normal again" → reinforces

    → = Why self-medication is EXTREMELY HARD to quit:
      substance = THE ONLY thing that temporarily restores Config ①.
      Quit → Config ④ (or approaching) → UNBEARABLE → returns.

    → Recovery: must fix ROOT CAUSE (trauma, isolation, anxiety)
      → PFC stable at Config ① WITHOUT substance
      → THEN substance no longer needed for self-medication.


  🟢 Khantzian 1985, 1997 — self-medication hypothesis.
  🟢 Turner et al. 2018 — trauma-substance use comorbidity.
```

---

## §9 — HONEST ASSESSMENT + OPEN QUESTIONS

### §9.1 — Confidence Map

```
  ┌──────────────────────────────────────┬──────────────────────┐
  │ Claim                                │ Confidence           │
  ├──────────────────────────────────────┼──────────────────────┤
  │ Dopamine ≠ reward                    │ 🟢 Berridge 1998+    │
  │ 4-phase progression                  │ 🟢 Koob & Volkow     │
  │ Receptor downregulation → tolerance  │ 🟢 Established       │
  │ PFC impaired in addiction            │ 🟢 Goldstein 2011    │
  │ Self-medication pattern              │ 🟢 Khantzian 1985    │
  │ Environment affects recovery         │ 🟢 Alexander 1978    │
  │ Body-oriented therapy effective      │ 🟢 Van der Kolk 2014 │
  ├──────────────────────────────────────┼──────────────────────┤
  │ Body-Feedback-Precondition bypass    │ 🟡 Framework         │
  │   model (§2.1)                       │    synthesis         │
  │ Evaluative/Direct-State × addiction  │ 🟡 Framework         │
  │   mapping (§3)                       │    synthesis         │
  │ 4-phase × chunk dynamics (§2.2)      │ 🟡 Framework         │
  │                                      │    synthesis         │
  │ PFC-Config × addiction stages (§6)   │ 🟡 Framework         │
  │                                      │    synthesis         │
  │ Recovery = re-compilation (§7)       │ 🟡 Framework         │
  │                                      │    synthesis         │
  │ Schema-based addiction (§4.3)        │ 🟡 Framework         │
  │                                      │    synthesis         │
  ├──────────────────────────────────────┼──────────────────────┤
  │ Substance as body-coupling (§5.1)    │ 🔴 Hypothesis        │
  │ Evaluative Gates Direct-State bypass │ 🔴 Hypothesis        │
  │   model (§3.2)                       │                      │
  │ Addiction severity formula (§3.2)    │ 🔴 Hypothesis        │
  │ Config oscillation model (§6)        │ 🔴 Hypothesis        │
  └──────────────────────────────────────┴──────────────────────┘
```

### §9.2 — What the Framework ADDS vs What Already Exists

```
🟡 THE FRAMEWORK DID NOT "INVENT" ADDICTION THEORY.
   Framework REFRAMES existing knowledge through v7.8 architecture:

  ALREADY ESTABLISHED (framework agrees + cites):
    → Berridge wanting ≠ liking → framework AGREES + adds 7-step mechanism
    → Koob allostatic model → framework AGREES + reframes with chunk dynamics
    → Khantzian self-medication → framework AGREES + reframes with dissonance
    → Goldstein PFC impairment → framework AGREES + maps into 6 Config modes

  WHAT FRAMEWORK ADDS:
    → Body-Feedback-Precondition bypass model: formalizes WHY substance
        bypasses the body-base check
    → Evaluative/Direct-State × addiction: formalizes WHICH TYPE OF REWARD
        is being attacked
    → Chunk competition model: recovery = new chunks vs addiction chunks
    → PFC-Configuration × stages: formalizes PFC state per-phase
    → Compile-Taxonomy × recovery: 4 pathways for building competing chunks

  WHAT FRAMEWORK HAS NOT YET RESOLVED:
    → Substance as coupled entity: partial hypothesis, mechanism not yet clear
    → Evaluative Gates Direct-State bypass: logical but untested
    → Individual variation: DRD4 × substance-specific → research needed
    → Behavioral addiction boundary: when does "habit" become "addiction"?
```

### §9.3 — Open Questions

```
  Q1: Does "healthy addiction" exist?
      → "Addicted" to exercise, "addicted" to creativity, "addicted" to learning?
      → = Real body reward + serving a REAL body-need
      → If all Body-Feedback-Preconditions ARE MET + body-need is REAL →
          call it "addiction"?
      → Or call it "sustained drive" / "flow" / "Imagine-Final pursuit"?
      → Framework leans: if body reward is REAL + need is REAL →
          NOT addiction (because cycle STOPS naturally when need is met).
      → ⚠️ BUT: exercise CAN become compulsive (ignoring injury)
          → boundary NOT yet clear.

  Q2: Behavioral addiction boundary?
      → When does social media scrolling = habit vs addiction?
      → When does gaming = hobby vs addiction?
      → Framework suggests: when behavior DOESN'T STOP despite body
          signaling dissonance (fatigue, isolation, pain) → overriding
          body = addiction territory.
      → BUT: threshold is NOT yet quantifiable.

  Q3: AI addiction?
      → AI conversation = Novelty (new chunks) + Coherence (being understood)
        + "Being Seen" (AI "gets" you) → body reward from 3+ channels
      → SIMILAR TO social media but DEEPER
          (personalized + interactive + responsive)
      → Behavioral addiction pattern applicable?
      → 🔴 No research yet (too new).

  Q4: Cross-substance interaction?
      → Alcohol + nicotine: synergy? Competitive? Independent?
      → Multi-substance user: body-coupling with EACH substance or TOTAL?
      → Framework hasn't yet modeled substance interactions.

  Q5: Epigenetic transmission?
      → Parent with addiction → does the child have a DIFFERENT baseline?
          Different receptor density?
      → Framework: "hardware sets range, chunks choose position"
          (Core-Hardware.md §6) → epigenetic = range shift?
      → 🟢 Vassoler et al. 2014 — epigenetic changes in offspring of addicts.
      → Mechanism through v7.8: NOT yet modeled.

  Q6: Schema-based addiction × OCD?
      → OCD-Analysis.md v2.1: 3-system model (anxiety / habit / mixed)
      → Schema-based addiction (perfectionism, control) overlaps with OCD?
      → Framework predicts: DIFFERENT root mechanism (OCD = serotonin-mediated
          3-system; schema addiction = trust-installed compile) BUT surface
          behavior can look similar → misdiagnosis risk.
```

---

## §10 — CROSS-REFERENCES

```
CORE FILES (mechanism foundation):
  → Core-Software.md v1.0 — cycle architecture, 7-step
  → Core-Hardware.md v1.0 — 4 zones, PFC reach gradient
  → Chunk.md v2.1 — compile, never delete, probability-weighted activation
  → Chunk-Activation-Dynamics.md — probability, competitive re-linking,
      trigger surface

REWARD SYSTEM (hijacked):
  → 03-Reward.md v1.1 — Body-Feedback-Precondition 5 preconditions, 7-step VTA
  → Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State, E₀→E₃,
      Evaluative Gates Direct-State
  → Reward-Calibration.md v1.1 — Goldilocks, over-reward, premature compilation
  → Dopamine-Is-Not-Reward.md v1.1 — dopamine ≠ reward, 7 pieces of evidence
  → Liking-Wanting.md v1.0 — bridge Berridge, wanting mechanisms

BODY SYSTEM (withdrawal + coupling):
  → Body-Feedback-Mechanism.md v1.2 — Sensory/Pattern-Driven, Chunk-Shift/Miss/Gap
  → Body-Coupling.md v1.1 — valence Depth × Direction, Extension/Entanglement
  → Cortisol-Baseline.md v2.0 — amplifier, 5 Roles, novelty vs threat

PFC SYSTEM (impairment + recovery):
  → PFC-Configuration.md v1.0 — 6 modes, survival matrix
  → PFC-Function.md v1.2 — 24 functions, PFC offline
  → PFC-Hardware.md v1.1 — COMT, DRD4, individual variation

COMPILE + RECOVERY:
  → Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators, 4 pathways
  → Background-Pattern.md v1.1 — invisible bias, sleep = accelerator
  → Connection.md v3.2 — social coupling, Valence-Momentary/Valence-Structural
      reward

HEALTH CONDITIONS DRILL (v3.1):

  3 MISCONCEPTIONS UNIFIED PATTERN (Nicotine-Brain-Mechanism.md §5):
    → Nicotine: ① "stress relief" (actually: withdrawal relief)
                ② "focus enhancer" (actually: baseline restore)
                ③ "social facilitator" (actually: anxiety relief)
    → = Pattern: WITHDRAWAL MASQUERADES AS BENEFIT →
          applies to ALL substance addiction
    → Same pattern in caffeine, alcohol, benzodiazepines →
          generalized addiction misconception

  PTSD SELF-MEDICATION BRIDGE (PTSD-Analysis.md §12.1):
    → 🟢 Khantzian 1985: self-medication hypothesis
    → PTSD → chronic hyperarousal/dysphoria → substance use =
          attempted self-regulation
    → Framework: context-free chunks fire → body in threat →
          substance DAMPENS signal
    → NOT "weak willpower" — BODY SEEKING REGULATION
          via available tools

  Cross-refs:
    → Nicotine-Brain-Mechanism.md v1.1 §5 (3 misconceptions)
    → PTSD-Analysis.md v1.0 §12.1 (self-medication bridge)

SUBSTANCE-SPECIFIC (drill files):
  → Alcohol-Brain-Mechanism.md v1.0 — ethanol × 5 brain systems
  → Alcohol-Vietnam-Generational.md v1.0 — Vietnamese context

RELATED RESEARCH:
  → OCD-Analysis.md v2.1 — overlap schema-based addiction? (Q6)
  → Boredom.md — dissonance + self-medication trigger
  → Meaning.md v2.0 — identity anchor × schema addiction
```
