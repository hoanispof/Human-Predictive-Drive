---
title: "OCD Analysis — Through the Lens of Framework v7.8"
version: v1.0-english
source_version: "2.2"
source_created: 2026-03-27
source_refined: 2026-05-15
translated: 2026-06-11
status: "RESEARCH FILE v2.2 — synthesis of framework v7.8 reasoning + established research"
scope: |
  RESEARCH FILE: Analysis of OCD (Obsessive-Compulsive Disorder) through the
  3-line "done" pipeline model. Connects OCD ↔ Love ↔ Serotonin.
  v2.0 KEY CHANGES vs v1.0 (v7.5 era):
    ① Chunk dynamics mapping: OCD through Body-Feedback-Mechanism (Shift/Miss/Gap)
    ② Spreading activation: serotonin ↓ = uninhibited cascade → obsessive loop
    ③ Cortisol 5 Roles applied (Holding/Threat-sustained/Silent)
    ④ PFC-Function mapping: Line 3 = HOLD + PROCESS, override failure mechanism
    ⑤ Love-Romantic v2.2 cross-reference updated
    ⑥ All terminology v7.5 → v7.8
  v2.1 KEY ADDITIONS (2026-04-26):
    ⑦ §4.5 Serotonin ↓ = AMPLIFIER, NOT ROOT CAUSE (feedback loop model)
    ⑧ §4.5b Self-Pattern-Modeling childhood bias × OCD-like in love (anxious attachment mechanism)
    ⑨ §4.6 Cross-species evidence (deer mice, SAPAP3, Hoxb8, dogs, primates)
    ⑩ Updated Honest Assessment + Open Questions with new predictions
  v2.2 KEY ADDITIONS (2026-05-15 — post Health Conditions Drill):
    ⑪ §4.7 Basal ganglia × Parkinson architectural bridge (gate LOCKED vs gate NOISY)
    ⑫ §7.1 PTSD intrusions vs OCD obsessions — mechanism distinction (context-free vs done-pipeline)
    ⑬ §7.2 Autism × OCD co-occurrence (17.4%, cascade not comorbidity, RRBs vs compulsions)
    ⑭ Cross-refs updated: 6 drill files + dependency versions refreshed
  ⚠️ Framework does NOT replace medical diagnosis/treatment.
  Analysis provides SUPPLEMENTARY PERSPECTIVE — if correct, may help
  understand why OCD occurs and why current treatments work.
purpose: |
  Research-level analysis: apply framework v7.8 to failure mode.
  OCD = test case for the "done" detection mechanism:
  when the mechanism for STOPPING BEHAVIOR fails → infinite loop.
  Love uses the SAME circuit but HAS an exit condition (bond compile).
dependencies:
  - Body-Feedback-Mechanism.md v2.0
  - Chunk-Activation-Dynamics.md
  - Chunk.md v2.1
  - Cortisol-Baseline.md v2.1
  - PFC-Function.md v1.2
  - Status.md v2.1
  - Love-Romantic.md v2.4
  - Feeling.md v2.1
  - Threat.md v1.0
  - Connection.md v4.0
  - Protect.md v1.0
  - Dopamine-Is-Not-Reward.md v1.1
  - Autism-Observation.md v1.0
  - PTSD-Analysis.md v1.0
  - Parkinson-Analysis.md v1.1
language: "English translation of Vietnamese source"
confidence: "🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis"
---

# OCD Analysis — Through the Lens of Framework v7.8

> **You wash your hands. Done. Body lightens. Move on.**
> **30 seconds. Entire process: UNCONSCIOUS.**
>
> **A person with OCD washes their hands. Done... but body does NOT lighten.**
> **"Done" signal fires → but NOISY → body: "NOT SURE it's clean."**
> **Wash again. Still NOT SURE. Wash again. 50 times. Hands raw.**
> **PFC: "I KNOW my hands are clean." Body: "DON'T TRUST IT."**
>
> **OCD = "done" pipeline FAILURE.**
> **3 defense lines that stop behavior → 1 or more lines FAIL → infinite loop.**
> **PANDAS proves: break Line 1 hardware → OCD appears IMMEDIATELY → fix → gone.**
> **Love uses the SAME circuit (serotonin ↓40%) but HAS an exit: bond compiles → done.**
> **OCD HAS NO exit: target never "sufficient" → treatment required.**
>
> **⚠️ Framework provides PERSPECTIVE — does not replace medical diagnosis/treatment.**

---

## Table of Contents

- [§1 — What Is OCD](#§1--what-is-ocd)
- [§2 — The Normal Mechanism: The "Done" Pipeline](#§2--the-normal-mechanism-the-done-pipeline)
- [§3 — OCD = Multi-Point Failure](#§3--ocd--multi-point-failure)
- [§4 — V7.8 Mapping: Chunk Dynamics + Spreading Activation + Basal Ganglia](#§4--v78-mapping-chunk-dynamics--spreading-activation--basal-ganglia)
- [§5 — Love ↔ OCD: Same Circuit, Different Purpose](#§5--love--ocd-same-circuit-different-purpose)
- [§6 — Serotonin = "Certainty Bias"](#§6--serotonin--certainty-bias)
- [§7 — Spectrum: Beyond OCD + PTSD Distinction + Autism Co-occurrence](#§7--spectrum-beyond-ocd--ptsd-distinction--autism-co-occurrence)
- [§8 — Treatment Map onto the 3 Lines](#§8--treatment-map-onto-the-3-lines)
- [§9 — Tesla Case Study](#§9--tesla-case-study)
- [§10 — Hardware vs Environment](#§10--hardware-vs-environment)
- [§11 — Honest Assessment](#§11--honest-assessment)
- [§12 — Open Questions](#§12--open-questions)
- [§13 — Cross-References + Status](#§13--cross-references--status)

---

## §1 — What Is OCD

```
DEFINITION:
  OCD = Obsessive-Compulsive Disorder
  Obsession = INTRUSIVE thoughts that repeat, UNWANTED but CANNOT BE STOPPED
  Compulsion = REPETITIVE behavior to reduce anxiety from the obsession

  Common examples:
    "Dirty hands" (obsession) → wash hands 50 times/day (compulsion)
    "Door not locked" (obsession) → check 10 times before leaving (compulsion)
    "Odd number = bad luck" (obsession) → do everything in even numbers (compulsion)

  KEY FEATURE:
    → OCD person KNOWS the behavior is irrational (PFC recognizes — A zone)
    → BUT cannot stop (chunks fire in C+D zones that DON'T LISTEN to PFC)
    → = "Ego-dystonic" — PFC observes "this is wrong" but body fires "must do this"
    → ≠ habit (ego-syntonic — PFC agrees → does it because WANTS to)

    Through v7.8: ego-dystonic = PFC OBSERVE (Feeling.md v2.0)
    Body-chunk interaction → PFC sees "irrational" → but PFC is only OBSERVER,
    does NOT directly control C+D zone processing.

  🟢 Prevalence: ~2-3% worldwide (WHO)
  🟢 Heritability: ~47-58% (Pauls 2010) → STRONG hardware component
  🟢 Onset: BIMODAL — 2 peaks:
     Peak 1: Childhood (~8-12 years) — ~25-50% of cases
       → Predominantly MALE
       → Genetic/hardware component STRONG → Line 1 primary failure
       → Typically more severe, more persistent
     Peak 2: Late adolescence / early adult (~18-25)
       → Near-equal gender distribution
       → Environmental triggers more prominent (stress, life transitions)
       → Line 2+3 primary failure (PFC not yet mature + serotonin shift)
     → 2 peaks MAP onto 2 DIFFERENT failure modes in the 3-line model
```

---

## §2 — The Normal Mechanism: The "Done" Pipeline

### §2.1 — Example: Normal Handwashing

```
EXAMPLE — NORMAL HANDWASHING:

  ① Chunks "dirty hands" FIRE (C+D zones, unconscious):
     → Body detects: "something on hands" → compiled chunks trigger → wash hands

  ② Washing action:
     → Water + soap → senses report: "hands smooth, clean, no longer sticky"

  ③ "Done" detector CHECK (OFC-caudate circuit):
     → OFC receives sensory input: "clean"
     → Caudate nucleus: compare "current state" vs "compiled done standard" (baseline)
     → MATCH → fire "DONE" signal

  ④ Body-feedback propagates:
     → "Done" signal → "dirty hands" chunks DEACTIVATE
     → Mild cortisol (from "dirty") → DROPS
     → Mild opioid: body-need met → reward signal
     → Body relaxes → finished

  ⑤ PFC receives the result:
     → PFC DOESN'T KNOW the done detector just fired
     → PFC only observes: "spontaneously stopped wanting to wash" → moves on
     → = Entire process: C+D zones. PFC only sees the OUTPUT.

TIMELINE: 30 seconds → done → immediately forgotten. Normal.
```

### §2.2 — The 3 Defense Lines

```
⭐ THE BRAIN HAS 3 LINES ensuring behavior STOPS at the right time:

┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  LINE 1 — "DONE" DETECTOR (automatic, C+D zones)                │
│  Hardware: OFC (orbitofrontal cortex) + caudate nucleus          │
│  Function: compare current state vs compiled "done standard"     │
│  Output: "DONE" signal → chunks deactivate                       │
│  Speed: fastest (milliseconds)                                   │
│  🟢 Evidence: Saxena et al., Schwartz et al. — fMRI confirmed    │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LINE 2 — SATISFACTION THRESHOLD (neurochemistry)                │
│  Hardware: serotonin system (throughout brain)                   │
│  Function: determines HOW STRONG the "done" signal needs to be   │
│            to be ACCEPTED                                        │
│  High serotonin → LOW threshold → easy to accept "done"         │
│  Low serotonin → HIGH threshold → difficult to accept "done"    │
│  = Serotonin = certainty bias (Status.md v2.1 §9.2)             │
│  🟢 Evidence: SSRIs effective for OCD (Bloch 2008)              │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LINE 3 — PFC OVERRIDE (conscious, slowest)                      │
│  Hardware: dlPFC (dorsolateral prefrontal cortex)                │
│  Function: PFC HOLDS "I KNOW it's done" → biases chunks → STOP  │
│  = Last resort when Lines 1+2 fail                               │
│  Depends on: PFC capacity (PFC-Function.md), cortisol level      │
│  PFC-Function.md: PFC = ~5% operator, HOLD → bias activation    │
│  🟢 Evidence: CBT/ERP effective for OCD (Schwartz 1996)         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

NORMAL: Line 1 fires → Line 2 accepts → done. PFC not needed.
MILD STRESS: Line 1 slightly weak → Line 2 compensates → done. PFC not needed.
HEAVY STRESS: Lines 1+2 slightly weak → PFC overrides → done. A bit tiring but OK.
```

---

## §3 — OCD = Multi-Point Failure

### §3.1 — Failure in Each Line

```
OCD = FAILURE in 1 or MORE lines simultaneously:

LINE 1 FAILS — "Done" detector dysfunctional:
  🟢 OFC-caudate HYPERACTIVE but signal NOT CLEAN
  → Circuit fires CONTINUOUSLY (hyperactive) but output = NOISE
  → Like: a "done" indicator light blinking erratically → body doesn't know "finished?"
  → ≠ Signal MISSING → signal DIRTY (noisy, unreliable)
  → = Hardware problem: wiring defective, not lack of effort

LINE 2 FAILS — Threshold too HIGH:
  → Low serotonin → certainty bias decreases (Status.md v2.1 §9.2)
  → = "Are you SURE it's done?" → DOESN'T BELIEVE IT
  → "Done" signal CAN fire → but DOESN'T CROSS threshold
  → = Like: someone says "it's done" but you DON'T BELIEVE them

LINE 3 FAILS — PFC override fails:
  → PFC HOLDS "I KNOW my hands are clean" → sends "STOP" bias
    (PFC-Function.md: PFC HOLD → bias spreading activation → body responds)
  → BUT: chunks are firing in THREAT DIRECTION
    (Cortisol §7.7 Role ① Compile Direction: compiled AVOIDANCE)
  → Threat-direction chunks > PFC bias authority
  → PFC depleted (high cortisol, sleep deficit) → override EVEN WEAKER
  → = PFC is only ~5% operator — 95% of chunks fire unconsciously
```

### §3.2 — Why "KNOWING" Doesn't Stop It

```
🟡 "KNOWING" AND "STOPPING" OPERATE IN 2 DIFFERENT SYSTEMS:

  "KNOWING" = PFC OBSERVE (A zone — Feeling.md v2.0):
    PFC observes body-chunk interaction → recognizes "irrational"
    = Line 3, conscious, SLOW

  "STOPPING" = chunks DEACTIVATE (C+D zones):
    Requires Line 1 (done detector) or Line 2 (threshold accepts)
    = Unconscious, automatic, FAST

  → PFC says "stop" = PFC HOLDS → biases spreading activation
  → BUT: chunks firing in threat direction = HIGH PRIORITY
    (Threat.md: threat priority > PFC authority — evolutionary design)
  → PFC 5% bias is NOT STRONG ENOUGH to override threat-compiled chunks
  → = "Force stop once → succeeds → but 5 minutes later the loop RETURNS"
    (PFC override = temporary HOLD, chunks fire AGAIN when PFC releases)
  → = Willpower is NOT the solution — problem is in LINES 1+2 (C+D zones)
```

### §3.3 — Spectrum: Mild to Severe

```
┌──────────────┬──────────┬───────────┬───────────┬──────────────────┐
│              │ Line 1   │ Line 2    │ Line 3    │ Presentation     │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Normal       │ OK       │ OK        │ OK        │ Wash → done      │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Personality  │ Slightly │ OK        │ OK        │ "Meticulous"     │
│ trait        │ weak     │           │           │ but can stop     │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Mild OCD     │ Weak     │ Slightly  │ OK        │ Rituals but PFC  │
│              │          │ high      │           │ override works   │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Moderate OCD │ Weak     │ High      │ Tiring    │ Rituals INCREASE,│
│              │          │           │           │ PFC override hard│
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Severe OCD   │ Fails    │ Very high │ Fails     │ Compulsive, can't│
│              │          │           │           │ stop, exhausted  │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Treatment-   │ DBS      │ SSRIs     │ CBT/ERP   │ Each treatment   │
│ resistant    │ (last    │ (not      │ (not      │ targets 1 line → │
│              │ resort)  │ enough)   │ enough)   │ COMBO needed     │
└──────────────┴──────────┴───────────┴───────────┴──────────────────┘
```

### §3.4 — PANDAS/PANS: Causal Evidence for Line 1

```
⭐ PANDAS/PANS = STRONGEST VALIDATION FOR THE 3-LINE MODEL

PANDAS (Pediatric Autoimmune Neuropsychiatric Disorders
        Associated with Streptococcal infections):

  MECHANISM:
    ① Child gets streptococcal infection (strep throat)
    ② Immune system creates antibodies against strep
    ③ Antibodies MISTAKENLY attack basal ganglia (including CAUDATE NUCLEUS)
    ④ Caudate becomes inflamed → "done" detector (OFC-caudate) IS DAMAGED
    ⑤ OCD APPEARS SUDDENLY — within DAYS, not months

  🟢 Evidence: Swedo et al. (1998), NIMH; multiple replications
  🟢 PANS = expanded version (not only strep)

  TIMELINE:
    Week 0: child is COMPLETELY NORMAL
    Week 1: strep infection → fever, sore throat
    Weeks 2-4: antibodies attack caudate
    Weeks 3-6: OCD APPEARS SUDDENLY + tics + anxiety ERUPTS

  TREATMENT:
    → Antibiotics (kill strep) → antibodies DECREASE → caudate recovers
    → OCD DECREASES or DISAPPEARS as inflammation resolves
    → Severe: IVIG or plasmapheresis (filter antibodies)

  THROUGH FRAMEWORK — WHY THIS MATTERS:
    → Damage Line 1 → OCD → fix Line 1 → OCD resolves
    → = CAUSAL EVIDENCE (not just correlation)
    → = "Natural experiment" — break 1 line → observe result
    → = STRONGEST validation for the 3-line model
```

---

## §4 — V7.8 Mapping: Chunk Dynamics + Spreading Activation + Basal Ganglia

> **NEW section v2.0**: Maps OCD onto v7.8 chunk-centric architecture.

### §4.1 — OCD Through Chunk Dynamics (Body-Feedback-Mechanism)

```
🟡 OCD MAPPED ONTO BODY-FEEDBACK-MECHANISM.MD:

  OCD OBSESSION = PATTERN-DRIVEN trigger (Body-Feedback-Mechanism §2.3):
    → Chunks fire INTERNALLY (no real external stimulus needed)
    → "Dirty hands" = chunks fire WITHOUT actually touching something dirty
    → = Pattern-Driven ⓐ REPLAY + ⓔ SPREADING ACTIVATION
    → Different from sensory-driven: no NEW stimulus → only internal loop

  OCD COMPULSION = attempt to create SENSORY-DRIVEN confirmation:
    → Washing hands = creating sensory input "clean" (water, soap, smooth)
    → Purpose: sensory input → "done" detector → STOP
    → BUT Line 1 is noisy → sensory confirmation NOT accepted
    → = Compulsion = CORRECT strategy (create confirmation)
      but FAILS because of hardware (done detector defective)


  OCD = CHUNK-MISS THAT NEVER RESOLVES:

    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │  NORMAL:                                                   │
    │    Body compiled baseline "hands CLEAN" → hands dirty →   │
    │    Chunk-Miss (actual < baseline) → washes →              │
    │    done detector: MATCH → Chunk-Miss RESOLVES → mild opioid│
    │                                                            │
    │  OCD:                                                      │
    │    Body compiled baseline "hands CLEAN" → hands dirty →   │
    │    Chunk-Miss (actual < baseline) → washes →              │
    │    done detector: NOISY → Chunk-Miss DOESN'T RESOLVE →    │
    │    VTA still fires negative delta → washes AGAIN → LOOP   │
    │                                                            │
    │  = Same mechanism. Different: done detector output quality.│
    └────────────────────────────────────────────────────────────┘

    Body-Feedback-Mechanism §5 Quality Baseline Shift also applies:
    → Each additional wash = baseline "clean" RISES further
    → = Threshold of "clean enough" GRADUALLY HIGHER with each compulsion
    → = OCD ESCALATES over time because baseline SHIFTS UP
    → = Crespi SNC 🟢: body compiles NEW baseline → old one "not enough"
```

### §4.2 — Spreading Activation Loop

```
🟡 OCD OBSESSIVE THINKING = UNINHIBITED SPREADING ACTIVATION:

  (Chunk-Activation-Dynamics.md §2)

  NORMAL:
    Chunk X fires → spreading activation → related A, B, C fire weakly
    → Serotonin = INHIBITOR: spreading activation is CONSTRAINED
    → Only chunks with STRONG links fire → rest DO NOT fire
    → = "Think of X → associate A → stop"

  OCD (serotonin ↓):
    Chunk X fires → spreading activation → LESS INHIBITED
    → A, B, C, D, E... fire → cascade WIDER than normal
    → Each chunk fires → triggers more spreading → LOOP
    → = "Think of bacteria → hands → door → desk → everything → WON'T STOP"

  ⭐ SAME MECHANISM AS LIMERENCE (Love-Analysis.md v2.1 §2.1):

    ┌──────────────────────┬──────────────────────┬──────────────────────┐
    │                      │ LIMERENCE            │ OCD                  │
    ├──────────────────────┼──────────────────────┼──────────────────────┤
    │ Serotonin            │ ↓ ~40%               │ ↓ (equivalent)       │
    │ Spreading activation │ UNINHIBITED          │ UNINHIBITED          │
    │ Target               │ Partner chunks       │ Threat chunks        │
    │ Cascade              │ "Think about them    │ "Think about bacteria │
    │                      │  24/7"               │  24/7"               │
    │ Exit condition       │ YES (bond compiles)  │ NO (target ≠ bond)   │
    │ Self-resolves?       │ YES (12-18 months)   │ NO (needs treatment) │
    │ Cortisol role        │ ① Compile APPROACH   │ ③ Threat-sustained   │
    │ PFC agrees?          │ YES (ego-syntonic)   │ NO (ego-dystonic)    │
    └──────────────────────┴──────────────────────┴──────────────────────┘

    = SAME mechanism (uninhibited spreading activation)
    = SAME neurochemistry (serotonin ↓)
    = DIFFERENT target (partner vs threat) → DIFFERENT outcome
    = DIFFERENT direction (approach vs avoidance)
```

### §4.3 — Cortisol 5 Roles in OCD

```
🟡 CORTISOL-BASELINE.MD §7.7 — 5 ROLES APPLIED TO OCD:

  ┌─────────────────┬──────────────────────────────────────────────┐
  │ Cortisol Role    │ In OCD                                       │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ① Compile       │ Chunks "bacteria is dangerous" compiled at   │
  │   Direction     │ AVOIDANCE direction → threat-tagged →        │
  │                 │ HIGH firing priority → PFC hard to override  │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ② Holding       │ "Haven't checked the door" = gap unclosed →  │
  │                 │ mild cortisol holding → PFC forced to revisit │
  │                 │ → "finished yet?" → NO (Line 1 fails)        │
  │                 │ → holding DOESN'T resolve → ESCALATES to ③   │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ③ Threat-       │ OCD anxiety = cortisol sustained because     │
  │   sustained     │ threat NOT GONE (body: "bacteria COULD STILL │
  │                 │ BE THERE"). FEAR element → self-amplifying.  │
  │                 │ = PRIMARY role that SUSTAINS OCD suffering as │
  │                 │   chronic (amplifier, not root cause).        │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ④ Inertia       │ After compulsion: cortisol NOT back at       │
  │                 │ baseline despite just washing. Body still    │
  │                 │ "unsettled" → MISTAKEN for "not clean yet"   │
  │                 │ → triggers loop again                         │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ⑤ Silent        │ Chronic OCD → cortisol CONTINUOUSLY HIGH but │
  │                 │ self-signal atrophy → PFC DOESN'T KNOW       │
  │                 │ it's stressed → damage accumulates silently  │
  │                 │ → PFC dendrite atrophy (Cortisol §9) →       │
  │                 │ Line 3 FURTHER WEAKENED → OCD WORSENS        │
  └─────────────────┴──────────────────────────────────────────────┘

  ⭐ ESCALATION PATH:
    ② Holding ("not done") → ③ Threat-sustained ("FEAR")
    → ⑤ Silent (chronic, atrophy) → Line 3 WEAKER → OCD WORSE
    → = Vicious cycle: OCD → cortisol → PFC damage → OCD worsens
```

### §4.4 — PFC Override Failure Through PFC-Function.md

```
🟡 LINE 3 MAPPED ONTO PFC-FUNCTION.MD:

  PFC 24 functions × 5 categories. Line 3 OCD override uses:

  HOLD: PFC holds "I know hands are clean" = keeps "clean" chunk active
  PROCESS: PFC evaluates evidence "hands smooth, clean, no odor"
  ORCHESTRATE: PFC biases spreading activation → "STOP washing"

  WHY IT FAILS:
    → PFC = ~5% operator (PFC-Function.md)
    → 95% = chunks fire unconsciously in C+D zones
    → OCD chunks compiled in THREAT DIRECTION (Role ①)
    → Threat-direction = HIGH PRIORITY (evolutionary: threat > logic)
    → PFC 5% bias CANNOT override 95% threat-priority chunks
    → PFC processing load EXTREME → Cortisol §6: catecholamine depletion
    → Short-term override OK → long-term = PFC exhausted → loop returns

  = Why CBT/ERP requires MANY sessions:
    → Each session: PFC holds + body sits with anxiety + DOESN'T compulse
    → Body LEARNS BY ITSELF: "anxiety DECREASES by itself even without checking"
    → = RE-COMPILE chunks: "not checking → STILL OK" (new chunk)
    → New chunks compile COMPETITIVELY with old chunks
      (Chunk-Activation-Dynamics.md §3: competitive re-linking)
    → Many sessions = new chunks GRADUALLY STRONGER than old chunks
    → = CBT doesn't "erase" OCD chunks → BUILDS competitive new chunks
```

### §4.5 — Serotonin ↓ = Amplifier, Not Root Cause

```
⭐ CORE QUESTION: Is serotonin ↓ the CAUSE or the CONSEQUENCE?

  MAINSTREAM SIMPLIFIED: serotonin ↓ → OCD/limerence
    = One directional. Serotonin = root cause.

  FRAMEWORK: serotonin ↓ = CONSEQUENCE of uncertainty + AMPLIFIER of loop
    = Feedback loop. Serotonin = amplifier, like cortisol.


  ⭐ FEEDBACK LOOP MODEL:

    [INITIAL TRIGGER] ← DIFFERENT depending on context
         ↓
    [UNCERTAINTY STATE] — body in "NOT SURE" state
         ↓
    [SEROTONIN ↓] — certainty bias DECREASES (= CONSEQUENCE)
         ↓
    [SPREADING ACTIVATION UNINHIBITED] — chunk cascade
         ↓
    [OBSESSIVE THINKING] — continuously monitor target
         ↓
    [STILL NOT RESOLVED] — done detector fails OR bond hasn't compiled
         ↓
    [UNCERTAINTY CONTINUES] → back to top → LOOP
         ↓
    [SEROTONIN EVEN LOWER] → amplifies further → VICIOUS CYCLE


  DIFFERENT INITIAL TRIGGERS:

    Childhood onset OCD:
      → Line 1 hardware FAILS FROM BIRTH → done signal NOISY
      → Body in CHRONIC uncertainty ("finished yet?")
      → Serotonin ↓ = CONSEQUENCE of hardware failure
      → → amplifies loop further

    Adult onset OCD:
      → Chronic stress → cortisol ↑ → serotonin ↓ (environment pathway)
      → BUT root cause = STRESS, not serotonin declining on its own

    Love (limerence):
      → Self-Pattern-Modeling library incomplete (just met) → high prediction-deltas
      → Body has GENUINE uncertainty about partner
      → Serotonin ↓ = ADAPTIVE RESPONSE (monitoring is necessary)
      → + Obligation unknown ("what do I need to give to maintain this?")
      → + Possible childhood Self-Pattern-Modeling bias (§4.5b)
      → = Serotonin ↓ = CONSEQUENCE of real uncertainty


  PARALLEL WITH CORTISOL (Cortisol-Baseline.md):

    Cortisol = "amplifier, NOT cause.
    Pain comes from 3 OTHER sources. Cortisol only accompanies."

    Serotonin = "amplifier of uncertainty loop.
    Uncertainty comes from OTHER sources. Serotonin amplifies."

    BOTH are FEEDBACK AMPLIFIERS, not ROOT CAUSES.


  🟢 EVIDENCE SUPPORTING "AMPLIFIER" MODEL:

    ① PANDAS: fix Line 1 (caudate) → OCD RESOLVES
       → IF serotonin = root cause → fixing caudate SHOULD NOT resolve it
       → IF serotonin = consequence → fix ROOT → uncertainty gone
         → serotonin RECOVERS ON ITS OWN → OCD resolves ✓

    ② SSRIs → stop → relapse ~80%:
       → IF serotonin = root cause already fixed → stopping SHOULDN'T relapse
       → IF serotonin = amplifier → stopping amplifier fix → root cause
         STILL EXISTS → loop returns ✓

    ③ CBT → stop → relapse only ~20-30%:
       → CBT fixes CHUNKS (root level, C+D zones)
       → Root changed → loop DOES NOT return (even if serotonin fluctuates)
       → = Root-level fix > amplifier-level fix ✓

    ④ Love self-resolves 12-18 months:
       → Bond compiles → uncertainty ↓ → serotonin RECOVERS ON ITS OWN
       → Serotonin recovers because ROOT CAUSE resolved (not because of meds)
       → = Serotonin follows uncertainty state ✓


  🟡 FRAMEWORK CLAIM:
    Serotonin ↓ = CONSEQUENCE + AMPLIFIER, NOT ROOT CAUSE
    Like cortisol: participates, amplifies, but doesn't initiate
    Root cause = Line 1 hardware / stress / genuine uncertainty
```

### §4.5b — Self-Pattern-Modeling Childhood Bias × OCD-like in Love

```
🟡 WHY SOME PEOPLE EXPERIENCE "LOVE" MORE INTENSELY → MORE OCD-LIKE:

  Self-Pattern-Modeling LIBRARY BUILT FROM CAREGIVER (Connection §3.2, §7):
    → Child learns Self-Pattern-Modeling FIRST on parents
    → Strict / unpredictable parents:
      → Self-Pattern-Modeling library builds DEEP but THREAT-BIASED
        (Cortisol Role ① Compile Direction: AVOIDANCE)
      → Chunks = "close agent → must MONITOR"

  ADULT → MEETS PARTNER → Self-Pattern-Modeling FIRES SAME LIBRARY:
    → Self-Pattern-Modeling retrieves: "close agent → monitor continuously"
    → "Partner looks sad → DID I DO SOMETHING WRONG?"
      (instead of: "partner is sad for their own reasons")
    → = HYPER-MONITORING — not because partner is problematic
      but because Self-Pattern-Modeling library was compiled FROM ENVIRONMENTS
      THAT REQUIRED monitoring

  HYPER-MONITORING → COMPOUND UNCERTAINTY:
    → Every partner expression → Self-Pattern-Modeling fires → interpret through THREAT lens
    → "They're quiet" → "angry? bored? about to leave?" (frequent mispredictions)
    → More prediction-deltas → HIGHER uncertainty
    → + Obligation overthinking: "am I worthy? how to keep them? what must I give?"
      (Obligation.md: obligation = compiled prediction "cost to pay"
       → new relationship = obligation NOT YET COMPILED → Chunk-Gap)
    → = 2 sources of uncertainty COMPOUND:
      ① Self-Pattern-Modeling: "what do they really feel?"
      ② Obligation: "what must I give to keep them?"
    → → Serotonin ↓ STRONGER → limerence MORE INTENSE + LONGER LASTING

  MAPPED ONTO ATTACHMENT THEORY (🟢 Bowlby 1969):
    → "Anxious attachment" = Self-Pattern-Modeling library compiled THREAT-BIASED
    → Adult: monitoring OVER-ACTIVE → CHRONIC uncertainty
    → Serotonin ↓ CHRONIC → limerence = OCD-like STATE
    → = Framework explains the MECHANISM behind the anxious attachment label

  ⚠️ NOT ONLY CHILDHOOD — PARTNER CAN BE THE SOURCE:
    → Partner genuinely unpredictable → Self-Pattern-Modeling errors HIGH because of PARTNER
    → = SAME mechanism, DIFFERENT source
    → = Childhood bias + unpredictable partner = COMPOUND → worst case
```

### §4.6 — Cross-Species Evidence: OCD = Bug of an Ancient Circuit

```
⭐ OCD-LIKE BEHAVIORS IN MANY SPECIES → ANCIENT CIRCUIT:

  🟢 CAPTIVE RHESUS MACAQUES (Novak et al. 2006):
    → Repetitive behaviors (rocking, pacing, self-harm)
    → Especially in macaques separated from mother early (social deprivation)
    → Serotonergic involvement (Lutz, Well & Novak research program —
      fluoxetine reduces SIB, lower CSF serotonin in SIB macaques)
    → Basal ganglia circuits compromised (Mason & Latham 2004)
    → = SAME region as human OCD (OFC-caudate)

  🟢 DEER MICE (Korff, Stein & Harvey 2008):
    → Spontaneously develop compulsive jumping/somersaulting
    → Respond to fluoxetine (SSRI) ✓ — but DO NOT respond to desipramine
      (= ONLY serotonin pathway, identical to human OCD)
    → Frontal cortex involvement (Korff et al. 2008-2009 research program)
    → = In a species WITHOUT complex PFC

  🟢 SAPAP3 KNOCKOUT MICE (Welch et al. 2007, Nature):
    → Compulsive grooming to the point of fur loss (facial lesions)
    → Respond to fluoxetine ✓
    → Cortico-striatal synaptic defects demonstrated
    → = Genetic manipulation → OCD-like → supports hardware causation
    → = Landmark paper — strongest genetic model

  🟢 HOXB8 MUTANT MICE (Greer & Capecchi 2002, Neuron;
    bone marrow rescue: Chen et al. 2010, Cell):
    → Excessive grooming → repaired by bone marrow transplant
    → Mechanism: microglia replacement → neuroimmune
    → = ECHOES PANDAS mechanism (autoimmune → basal ganglia)!

  🟢 DOGS — Canine Compulsive Disorder:
    → Tail-chasing, flank-sucking, shadow-chasing
    → Respond to fluoxetine (🟢 Irimajiri et al. 2009: RCT, 8.7× improvement)
    → CDH2 gene chromosome 7 (Dodman et al. 2010, Molecular Psychiatry)
    → Bull Terrier compulsive tail chasing (Moon-Fanelli et al. 2011)
    → = Genetic component confirmed in another species


  ⭐ IMPLICATIONS FOR FRAMEWORK:

    ┌───────────────────────────────────────────────────────────────┐
    │                                                               │
    │  IF OCD ONLY IN HUMANS → bug specific to complex PFC         │
    │  IF OCD IN MANY SPECIES → bug of a circuit OLDER than PFC    │
    │                                                               │
    │  Evidence: mice + dogs + primates → CIRCUIT = BASAL GANGLIA  │
    │  (OFC-caudate = Line 1) — circuit ANCIENT, CROSS-SPECIES     │
    │                                                               │
    │  → STRONG support for 3-line model:                           │
    │    Line 1 (OFC-caudate) = ANCIENT HARDWARE, cross-species    │
    │      → Mice HAVE Line 1 → mice CAN develop OCD-like         │
    │    Line 2 (serotonin) = ANCIENT HARDWARE, cross-species      │
    │      → SSRIs help mice + dogs + humans → SAME mechanism      │
    │    Line 3 (PFC override) = STRONG ONLY IN HUMANS             │
    │      → Humans HAVE Line 3 → CBT possible                     │
    │      → Mice/dogs DON'T HAVE Line 3 → ONLY SSRIs/DBS         │
    │                                                               │
    │  → OCD = BUG OF ANCIENT CIRCUIT (Lines 1+2)                  │
    │    PFC (Line 3) = SUPPLEMENTARY SOLUTION ONLY HUMANS HAVE    │
    └───────────────────────────────────────────────────────────────┘


  ⭐ CONNECTION TO "SEROTONIN = AMPLIFIER" (§4.5):

    Deer mice: DO NOT have complex PFC, NO "overthinking"
      → STILL OCD-like + serotonin changes at OFC
      → = In mice: serotonin ↓ closer to HARDWARE CAUSE (genes, wiring)

    Captive macaques: social deprivation → compulsive
      → = In primates: ENVIRONMENT triggers → serotonin ↓ = CONSEQUENCE

    Humans: BOTH + ADDITIONAL PFC complexity
      → Hardware (genes) → Line 1 fails → uncertainty → serotonin ↓
      → Environment (stress/childhood Self-Pattern-Modeling bias) → uncertainty → serotonin ↓
      → Obligation overthinking → uncertainty → serotonin ↓
      → = Humans have MORE PATHWAYS to serotonin ↓ than mice/dogs

    → Serotonin role = SPECTRUM by species complexity:
      Mice: serotonin closer to HARDWARE CAUSE (fewer uncertainty sources)
      Primates: serotonin = MIX of cause + consequence (social component)
      Humans: serotonin closer to CONSEQUENCE + AMPLIFIER (MANY uncertainty sources)
```

### §4.7 — Basal Ganglia × Parkinson: Architectural Bridge

```
⭐ OCD × PARKINSON: SAME BASAL GANGLIA, DIFFERENT FAILURE MODE

  (Cross-ref: Parkinson-Analysis.md v1.1 §2)

  PARKINSON:
    → Basal ganglia = GATE (default CLOSED, dopamine = KEY)
    → SNc neurons DIE → dopamine LOST → gate LOCKED
    → Motor command FROM PFC PRESENT → signal CANNOT PASS THROUGH
    → = KNOWS what to do but CANNOT DO IT

  OCD:
    → OFC-caudate circuit = DONE DETECTOR (basal ganglia component)
    → Done detector output = NOISY (dirty signal, unreliable)
    → "Done" signal fires → but unreliable → body DOESN'T TRUST IT
    → = ALREADY DONE but CANNOT STOP

  ┌────────────────┬──────────────────────┬──────────────────────┐
  │                │ PARKINSON            │ OCD                  │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ Failure mode   │ Gate LOCKED          │ Gate signal NOISY    │
  │                │ (key destroyed)      │ (detector unreliable)│
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ Circuit        │ SNc → Striatum       │ OFC → Caudate        │
  │                │ (nigrostriatal)      │ (orbitofrontal)      │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ Result         │ CAN'T START/EXECUTE  │ CAN'T STOP           │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ DBS target     │ STN (subthalamic)    │ VC/VS (ventral       │
  │                │                      │ capsule/striatum)    │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ DBS mechanism  │ JAM pathological     │ MODULATE done-signal │
  │                │ beta oscillations    │ processing           │
  └────────────────┴──────────────────────┴──────────────────────┘

  ⭐ IMPLICATIONS FOR "ANCIENT CIRCUIT" ARGUMENT (§4.6):
    → BOTH = basal ganglia failure
    → Basal ganglia = GATE for MANY functions (motor + completion + reward)
    → SAME architectural principle, DIFFERENT failure output:
      Parkinson: motor gate locked → CAN'T EXECUTE
      OCD: completion gate noisy → CAN'T STOP
    → DBS for BOTH: same bypass principle (electrical override)
      but DIFFERENT targets (because different sub-circuit)
    → = Basal ganglia = ANCIENT infrastructure, many failure modes possible
```

---

## §5 — Love ↔ OCD: Same Circuit, Different Purpose

> 🟢 Marazziti et al. (1999): People in early romantic love have
> serotonin transporter DECREASED ~40% — THE SAME LEVEL as OCD patients.

### §5.1 — Same Symptoms, Different Label

```
PERSON IN LOVE (limerence, 0-18 months):
  → Thinks about partner CONTINUOUSLY (intrusive thoughts ✓)
  → Cannot stop even when WANTING to concentrate (compulsive ✓)
  → Checks phone constantly (checking ✓)
  → Analyzes every message, gesture (rumination ✓)
  → Serotonin decreases ~40% (🟢 Marazziti 1999)
  → Spreading activation uninhibited → partner chunks cascade

PERSON WITH OCD (contamination type):
  → Thinks about bacteria CONTINUOUSLY (intrusive thoughts ✓)
  → Cannot stop even while KNOWING it's irrational (compulsive ✓)
  → Checks hands constantly (checking ✓)
  → Analyzes every surface touched (rumination ✓)
  → Serotonin low (🟢 established)
  → Spreading activation uninhibited → threat chunks cascade

→ = SAME mechanism. SAME neurochemistry. SAME behavioral pattern.
→ Remove the label → symptoms are IDENTICAL.
```

### §5.2 — Why the Same Circuit (Evolutionary Logic)

```
🟡 EVOLUTION BUILT 1 CIRCUIT:

  "When encountering something IMPORTANT + UNCERTAIN
   → decrease serotonin → decrease certainty bias
   → OBSESS → monitor continuously
   → until SUFFICIENTLY CERTAIN → serotonin recovers → stops"

  Circuit FUNCTIONS CORRECTLY when:
    → Target = potential mate (IMPORTANT + UNCERTAIN)
    → Serotonin ↓ → obsess → monitor every signal
    → Bond compiles → "know enough" → serotonin recovers → obsession fades
    → = "Love" = obsessive-monitoring circuit WORKING FOR ITS PURPOSE

  Circuit FAILS when:
    → Target = something THAT DOESN'T NEED monitoring (clean hands, locked door, even numbers)
    → Serotonin ↓ → obsess → BUT target NEVER "certain enough"
    → "Clean hands" CANNOT be confirmed through bond (unlike "this person is worth loving")
    → = Circuit running CORRECTLY but ON THE WRONG TARGET

  MEDICAL ANALOGY:
    Fever = FEATURE (fights infection) → chronic fever = BUG (autoimmune)
    Love obsession = FEATURE (monitor mate) → OCD obsession = BUG (monitor wrong target)
```

### §5.3 — 3 Key Differences

```
┌─────────────────┬───────────────────────┬───────────────────────┐
│                 │ LOVE (limerence)      │ OCD                   │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Target          │ Partner — HAS VALUE   │ Something that doesn't│
│                 │ bond + exit condition │ need monitoring       │
│                 │                       │ (bacteria, locks)     │
├─────────────────┼───────────────────────┼───────────────────────┤
│ PFC agrees?     │ YES — ego-syntonic    │ NO — ego-dystonic     │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Self-stopping?  │ YES — bond compiles → │ NO — needs treatment  │
│                 │ done detector: DONE   │ done detector: FAILS  │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Reward          │ YES — opioid,         │ NO — only temporary   │
│                 │ oxytocin              │ anxiety reduction      │
│                 │ (body-need genuinely  │                        │
│                 │ met)                  │                        │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Cortisol role   │ ① APPROACH compile    │ ③ Threat-sustained    │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Body-Base Ext   │ Partner → extension   │ NO (target = object)  │
│ (Valence-Propagation §2)       │ (Valence-Structural)  │                       │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Adaptive?       │ YES — monitor mate    │ NO — wastes energy    │
└─────────────────┴───────────────────────┴───────────────────────┘
```

### §5.4 — Timeline: How Love STOPS (But OCD Does Not)

```
LOVE — Serotonin timeline:

  Months 1-3: LIMERENCE
    → Serotonin ↓40% → spreading activation uninhibited → obsession INTENSE
    → "Done" detector: CHECKING → not done yet (bond not compiled)
    → = CORRECT — new bond NEEDS monitoring

  Months 3-12: BONDING
    → More encounters → Self-Pattern-Modeling library builds (Love §3.2) → uncertainty DECREASES
    → Chunks about partner compile GRADUALLY → C+D zones "getting to know" more
    → Serotonin GRADUALLY RECOVERS → spreading activation INHIBITED again
    → = Bond compiling → done detector increasingly recognizes "know enough"

  Months 12-18: ATTACHMENT
    → Chunks about partner HAVE compiled (Self-Pattern-Modeling library DEEP)
    → Serotonin NORMAL → high certainty → obsession ends
    → Valence-Structural body-base extension compiled → structural reward replaces Valence-Momentary
    → = "Early love fades" = OBSESSION ends, ATTACHMENT remains
    → = Circuit SELF-EXTINGUISHES when purpose complete (bond compiled)

OCD — NO similar timeline:
  → Target (bacteria, lock) DOES NOT compile into "bond"
  → "Done" detector NEVER recognizes "sufficient"
  → Serotonin DOES NOT recover on its own
  → = INFINITE LOOP — external intervention required
```

### §5.5 — When Love Doesn't Stop: Extended Limerence

```
🟡 EXTENDED LIMERENCE = "LOVE" STUCK IN AN OCD-LIKE STATE:

  Limerence lasting beyond 18 months → bond DIDN'T COMPILE:
    → Unstable relationship, unrequited, on-off
    → "Done" detector: NEVER recognizes "done" (bond not stable)
    → Serotonin STILL LOW → spreading activation STILL uninhibited
    → = OCD-like state with target = PERSON

  Consequences:
    → Stalking = compulsive checking (OCD checking pattern)
    → Extreme jealousy = uncertainty monitoring overload
    → "Can't let go" = done detector HAS NOT fired (bond not compiled + not failed)
    → = SAME OCD mechanism, target = PERSON instead of OBJECT

  Through v7.8:
    → Extended limerence = Valence-Structural body-base extension IS compiling
      but unstable relationship → compile DOESN'T COMPLETE
    → Cortisol Role ② Holding → escalates to ③ Threat-sustained
    → = If relationship stabilizes → bond compiles → done → stops
    → = If relationship STAYS unstable indefinitely → chronic → like OCD
```

---

## §6 — Serotonin = "Certainty Bias"

```
⭐ FRAMEWORK: SEROTONIN = CERTAINTY BIAS (Status.md v2.1 §9.2)

  POP SCIENCE:  "Serotonin = happiness. Low = sad."
  FRAMEWORK:    Serotonin = certainty/stability. Low = uncertainty/checking.

  IF "happiness":
    → Person in love (serotonin ↓) = SAD? ← WRONG. Extremely intense feeling.
    → Person with OCD (serotonin ↓) = SAD? ← Not exactly. ANXIOUS.
    → SSRIs treat OCD because "happier"? ← WRONG. Because LESS CHECKING.

  IF "certainty bias":
    → Person in love (serotonin ↓) = UNCERTAIN about partner → obsess ← CORRECT
    → Person with OCD (serotonin ↓) = UNCERTAIN "done" → checks again ← CORRECT
    → SSRIs = increase certainty → easier to accept "done" → reduce checking ← CORRECT
    → Tryptophan depletion = reduce certainty → indecision ← CORRECT

  → "Certainty bias" explains MORE than "happiness"
  → Status.md v2.1 §9.2: serotonin = Ratchet (easy up, hard down)
    → OCD = ratchet STUCK at low level → certainty EXTREMELY LOW → checking endlessly


  SEROTONIN IN THE 3 LINES:

    Line 1 — "Done" detector:
      → Serotonin does NOT fix hardware wiring
      → = Why SSRIs HELP but DON'T CURE OCD completely

    Line 2 — Satisfaction threshold:
      → Serotonin DIRECTLY affects:
        High serotonin → LOW threshold → weak "done" STILL ACCEPTED
        Low serotonin → HIGH threshold → "done" must be EXTREMELY STRONG
      → = SSRIs target THIS LINE correctly

    Line 3 — PFC override:
      → Serotonin indirect: stable mood → PFC less cortisol burden → stronger override


  🟢 STRONG VALIDATION:
    → OCD requires SSRI dose 3-4× depression (fluoxetine 60-80mg vs 20mg)
    → = OCD threshold HIGHER → needs MORE serotonin → supports "certainty bias" model
    → Noradrenergic antidepressants (desipramine) → NOT effective for OCD
    → = ONLY serotonin pathway works → certainty bias, NOT general mood elevation
```

---

## §7 — Spectrum: Beyond OCD + PTSD Distinction + Autism Co-occurrence

```
🟡 SAME CIRCUIT, DIFFERENT TARGET:

  ┌──────────────────┬───────────────────────┬────────────┬──────────┐
  │ Phenomenon       │ Monitoring target     │ Adaptive?  │ Self-    │
  │                  │                       │            │ stopping?│
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Love (limerence) │ Potential mate        │ YES        │ YES      │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Extended         │ Unstable partner      │ Partially  │ HARD     │
  │ limerence        │                       │            │          │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Health anxiety   │ Body symptoms         │ NO         │ NO       │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ OCD contamination│ Bacteria, dirt        │ NO         │ NO       │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ OCD checking     │ Locks, stove, doors   │ NO         │ NO       │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Extreme jealousy │ Partner + rivals      │ Partially  │ VARIES   │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ BDD              │ Perceived body flaws  │ NO         │ NO       │
  │ 🟢 DSM-5: OCD   │ (exaggerated)         │            │          │
  │ spectrum         │                       │            │          │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ PTSD intrusions  │ Traumatic event       │ Partially  │ HARD     │
  └──────────────────┴───────────────────────┴────────────┴──────────┘

  COMMON PATTERN:
    → Serotonin ↓ → certainty ↓ → spreading activation uninhibited → obsessive monitor
    → Target HAS exit condition + SELF-RESOLVES → SELF-STOPS (love)
    → Target HAS NO exit condition → DOESN'T STOP (OCD, anxiety)
    → = Pathology = circuit RUNNING CORRECTLY on the WRONG target or no exit
```

### §7.1 — PTSD Intrusions vs OCD Obsessions: Same "Intrusive Thoughts," Different Mechanism

```
⭐ PTSD AND OCD BOTH HAVE "INTRUSIVE THOUGHTS" — BUT COMPLETELY DIFFERENT MECHANISMS:

  (Cross-ref: PTSD-Analysis.md v1.0 §2, §4, §14)

  PTSD INTRUSION:
    → Trauma chunk encoded VIA AMYGDALA (bypassed hippocampus)
    → Chunk has BODY STATE but LACKS 3 metadata: temporal, spatial, causal
    → Trigger (sensory match) → context-free chunk fires → body "RE-LIVES" trauma
    → Body-first temporal: amygdala 12ms → body 50ms → PFC 200ms+
    → PFC arrives LATE — body HAS ALREADY responded before PFC can "know"
    → = CONTEXT-FREE chunk fires in wrong context

  OCD OBSESSION:
    → Chunk compiled NORMALLY (HAS full 4/4 context metadata)
    → "Done" detector output NOISY → completion signal unreliable
    → Chunk-Miss DOESN'T RESOLVE → behavior repeats
    → PFC knows "done" but body DOESN'T TRUST done signal
    → = CONTEXT-INTACT chunk, "DONE" SIGNAL fails

  ┌────────────────┬──────────────────────────┬────────────────────────┐
  │                │ PTSD INTRUSION           │ OCD OBSESSION          │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Chunk type     │ Context-FREE (amygdala)  │ Context-INTACT (normal)│
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Metadata       │ MISSING 3/4 (state only) │ COMPLETE 4/4           │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Failure point  │ ENCODING broken          │ COMPLETION detector    │
  │                │ (hippocampus suppressed) │ noisy (OFC-caudate)    │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Body response  │ FULL threat RE-EXPERIENCE│ UNCERTAINTY "not done" │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ PFC experience │ "This is a memory" (late)│ "I KNOW it's done"     │
  │                │                          │ (overridden)           │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Treatment      │ ADD context metadata     │ LOWER threshold +      │
  │ principle      │ (re-contextualize)       │ RE-COMPILE chunks      │
  └────────────────┴──────────────────────────┴────────────────────────┘

  SAME "PFC knows but body won't listen" — DIFFERENT reasons:
    PTSD: body ACTS 200ms before PFC (temporal sequence problem)
    OCD: body IGNORES done signal (signal quality problem)
    → PTSD = chunk fires → body responds → PFC arrives TOO LATE
    → OCD = chunk fires → done signal fires → body DOESN'T TRUST signal

  ⚠️ CO-OCCURRENCE: PTSD + OCD compound
    → Trauma → chronic cortisol → Lines 2+3 weakened
    → Pre-existing OCD vulnerability + PTSD = OCD ESCALATES
    → Conversely: OCD hypervigilance + trauma = PTSD risk ↑
    → (PTSD §12 cross-ref)
```

### §7.2 — Autism × OCD: Cascade, Not Comorbidity

```
⭐ OCD IN AUTISM: 17.4% — HIGHER THAN GENERAL POPULATION (~2-3%)

  🟢 van Steensel, Bögels & Perrin 2011: 17.4% autistic children
    meet OCD criteria (meta-analysis)
  (Cross-ref: Autism-Observation.md v1.0 §13.1)


  WHY HIGHER — 3 PATHWAYS:

    ① Sensory gain → LARGER prediction-deltas → uncertainty ↑
       → Serotonin ↓ → Line 2 threshold HIGH → hard to accept "done"
       → The sensory world is MORE INTENSE → "not clean enough/not right enough"
         is felt MORE STRONGLY in autistic people

    ② Masking (chronic mismatch) → cortisol ↑ (Autism §6)
       → Line 2 (serotonin ↓) + Line 3 (PFC impaired) BOTH WEAKEN
       → = Like Tesla trajectory (§9) but FROM ENVIRONMENT, not aging

    ③ Predictive coding differences (Autism §4)
       → Prediction-delta LARGER by architecture (not from stress)
       → Done detector needs STRONGER signal to match "done standard"
       → = Line 1 hardware NORMAL but THRESHOLD naturally higher


  ⭐ DISTINCTION: RRBs (Autism) vs OCD Compulsions

    (Cross-ref: Autism-Observation.md v1.0 §8.4)

    ┌──────────────────┬─────────────────────┬──────────────────────┐
    │                  │ RRBs (Autism)       │ OCD Compulsions      │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Core mechanism   │ Regulation / reward │ "Done" detector fail │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Feeling          │ Calming, engaging   │ Anxiety, "must" do   │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Completion       │ Feels done per-step │ NEVER feels done     │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Ego              │ Syntonic (WANTED)   │ Dystonic (UNWANTED)  │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Function         │ BUILDS + REGULATES  │ REDUCES anxiety      │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Intervention     │ SUPPORT             │ ERP + medication     │
    └──────────────────┴─────────────────────┴──────────────────────┘

    EGO-SYNTONIC vs EGO-DYSTONIC = primary distinguishing test:
      → "Do you WANT to do this?" → YES = RRB (regulation, reward)
      → "Do you NOT WANT to but cannot stop?" → OCD (done failure)

  ⚠️ CLINICAL: MUST DISTINGUISH PER-BEHAVIOR
    → Autistic person CAN have BOTH RRBs (functional) + OCD (pathological)
    → Suppressing RRBs as if treating OCD = remove REWARD + COPING + IDENTITY
      (triple loss — Autism §8.5)
    → OCD treatment (ERP + SSRI) ONLY for ego-dystonic behaviors

  🟡 FRAMEWORK: "CASCADE NOT COMORBIDITY" (Autism §13.4):
    → OCD in autism = SAME architecture under MORE load
    → Different configuration → larger prediction-delta → uncertainty cascade
    → Reduce sensory load + reduce masking demand
      → reduce cascade → reduce OCD symptoms
    → = ROOT DIFFERS from standalone OCD: address ENVIRONMENT + LOAD
      alongside (or before) directly treating OCD
```

---

## §8 — Treatment Map onto the 3 Lines

```
EACH TREATMENT TARGETS A SPECIFIC LINE:

┌──────────────────┬───────────┬──────────────────────────────────────┐
│ Treatment        │ Line      │ How it works through framework        │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ SSRIs            │ Line 2    │ Increase serotonin → lower threshold  │
│ (fluoxetine,     │           │ → noisy signal STILL gets accepted →  │
│ fluvoxamine)     │           │ "done" loop stops.                    │
│                  │           │ ⚠️ OCD: 60-80mg (3-4× depression)    │
│                  │           │ 🟢 First-line, effective ~60%         │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ CBT / ERP        │ Line 3    │ Trains PFC HOLD + sit with anxiety   │
│                  │           │ + NOT compulse → body LEARNS         │
│                  │           │ "anxiety decreases even without       │
│                  │           │  checking" = RE-COMPILE chunks        │
│                  │           │ (competitive re-linking —             │
│                  │           │  Chunk-Activation §3)                 │
│                  │           │ 🟢 Effective, especially + SSRIs      │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ SSRIs + CBT      │ 2 + 3     │ SSRIs lower threshold → PFC override │
│ (COMBO)          │           │ EASIER → ERP succeeds MORE →         │
│                  │           │ chunks re-compile FASTER.             │
│                  │           │ 🟢 GOLD STANDARD                      │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ Clomipramine     │ Line 2    │ More serotonergic than SSRIs.        │
│                  │ (stronger)│ More side effects → second-line.     │
│                  │           │ ⭐ Noradrenergic (desipramine) →      │
│                  │           │ NOT effective → ONLY serotonin path  │
│                  │           │ 🟢 Clomipramine Collaborative 1991    │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ Augmentation:    │ Line 3    │ Low-dose antipsychotic → reduces     │
│ Antipsychotics   │ (support) │ dopamine → reduces SALIENCE          │
│                  │           │ (Dopamine-Is-Not-Reward.md) →       │
│                  │           │ threat priority DECREASES →           │
│                  │           │ PFC override EASIER                   │
│                  │           │ 🟢 ~30% treatment-resistant respond  │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ DBS              │ Line 1    │ Direct stimulation of OFC-caudate →  │
│                  │           │ fixes "done" detector at hardware    │
│                  │           │ 🟢 Last resort, invasive but works   │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ PANDAS treatment │ Line 1    │ Antibiotics → caudate recovers →     │
│                  │ (direct)  │ "done" detector fixed at hardware    │
│                  │           │ 🟢 Swedo 1998; only PANDAS/PANS      │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ Mindfulness      │ Line 3    │ "I SEE the obsession → it's just a  │
│                  │ (support) │ thought → don't need to ACT"         │
│                  │           │ = PFC OBSERVE (Feeling.md v2.0)      │
│                  │           │ 🟡 Adjunct, insufficient alone        │
└──────────────────┴───────────┴──────────────────────────────────────┘

⭐ WHY COMBO IS BEST:
  → SSRIs = temporary bridge (lower Line 2 threshold)
  → CBT = fix the road (re-compile chunks, Line 3)
  → SSRIs CREATE CONDITIONS for CBT:
    anxiety ↓ → PFC override EASIER → ERP succeeds → chunks re-compile
  → = Can TAPER SSRIs after CBT has compiled enough new chunks

⚠️ SSRIs ALONE NOT SUFFICIENT:
  → Fixes Line 2 → but Line 1 STILL fails + chunks STILL compiled as threat
  → Stop SSRIs → threshold RISES AGAIN → loop RETURNS
  → 🟢 Relapse: SSRIs alone ~80%, SSRIs+CBT ~30-50%, CBT alone ~20-30%
  → = CBT changes STRUCTURE (chunks) → best long-term outcome
```

---

## §9 — Tesla Case Study

```
🟡 TESLA = NOT BORN WITH OCD. A TRAJECTORY:

PHASE 1 — Functional (youth → middle age):
  → Visual-dominant EXTREMELY STRONG (eidetic imagery)
  → Small rituals: tidy arrangement, patterns = functional
  → "Done" detector: INTACT → stops at right time
  → PFC: STRONG → overrides when needed
  → = "Meticulous" → helped work quality → PRODUCTIVE

PHASE 2 — Escalation (50s-60s):
  → Chronic cortisol: isolation, poverty, being exploited
    (Cortisol §7.7 Role ③ → ⑤ Silent: damage accumulates)
  → Aging: OFC-caudate GRADUALLY WEAKENS → Line 1 decreases
  → PFC aging: dlPFC decreases → Line 3 decreases
  → Serotonin decreases (chronic cortisol → disrupts serotonin) → Line 2 decreases
  → = All 3 lines WEAKENING SIMULTANEOUSLY

PHASE 3 — OCD-like (late life, 1930s-1943):
  → FIXED NUMBERS (divisible by 3) = "done" detector FAILING
  → Rituals RIGID → no flexibility
  → Chunk library EXTREMELY DEEP, EXTREMELY NARROW → cross-domain flexibility LOW
  → = SLID from functional → OCD-like via trajectory

THROUGH FRAMEWORK:
  → Tesla didn't "get" OCD → Tesla SLID INTO OCD-like state
  → All 3 lines weakened SIMULTANEOUSLY + isolation + chronic cortisol
  → If life circumstances had remained stable → POSSIBLY kept functional
  → = OCD-like in late life = TRAJECTORY, not fate
```

---

## §10 — Hardware vs Environment

```
⭐ EACH LINE HAS A DIFFERENT HARDWARE/ENVIRONMENT RATIO:

LINE 1 — "Done" detector (OFC-caudate):
  Hardware:    ████████░░ ~80%
  Environment: ██░░░░░░░░ ~20%
  → Primarily genes + innate wiring
  → PANDAS: damage hardware → OCD → fix → resolves = CAUSAL
  → = Hardest locked of the 3 lines

LINE 2 — Satisfaction threshold (serotonin):
  Hardware:    █████░░░░░ ~50%
  Environment: █████░░░░░ ~50%
  → Baseline serotonin = genes
  → BUT: stress → cortisol → suppresses serotonin (environment)
  → Sleep deprivation → serotonin synthesis decreases
  → Nutrition (tryptophan) → environment factor
  → = Most FLEXIBLE line

LINE 3 — PFC override:
  Hardware:    ███░░░░░░░ ~30%
  Environment: ███████░░░ ~70%
  → PFC capacity baseline = genes
  → BUT: stress → cortisol → PFC impaired (🟢 Arnsten 2009)
  → Training (CBT) → PFC override STRENGTHENS
  → = Most CHANGEABLE line


⭐ WAXING-WANING COURSE (🟢 Skoog & Skoog 1999):

  OCD severity fluctuates with environment:

  ↑ INCREASES with: stress (cortisol ↑ → Lines 2+3 ↓), sleep deprivation (PFC ↓),
    life transitions (uncertainty ↑ → serotonin ↓), inflammation (PANDAS → Line 1)

  ↓ DECREASES with: life stability (cortisol ↓ → Lines 2+3 recover),
    sufficient sleep + exercise (serotonin ↑ + PFC ↑), CBT success,
    SSRIs at correct dose

  → = OCD = hardware vulnerability + environment TRIGGERS/MODULATES
  → = Like diabetes: genes = vulnerability, lifestyle = trigger + severity


⭐ "COMPLETE CURE":

  🟢 Longitudinal data:
  ┌───────────────────────┬──────────┬───────────────────────────────┐
  │ Outcome               │ Rate     │ Through framework             │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Full remission        │ ~25-30%  │ Line 1 mild + Lines 2+3 fixed│
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Significant improve   │ ~40-50%  │ Lines 2+3 improve, Line 1    │
  │                       │          │ still weak → residual         │
  │                       │          │ symptoms under stress         │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Partial response      │ ~15-20%  │ Only 1 line responds          │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Treatment-resistant   │ ~10-15%  │ Line 1 severely fails → needs │
  │                       │          │ DBS                           │
  └───────────────────────┴──────────┴───────────────────────────────┘

  Relapse (🟢):
    SSRIs alone → stop → ~80% relapse (threshold RISES again)
    SSRIs + CBT → stop → ~30-50% relapse
    CBT alone → after → ~20-30% relapse (chunks re-compiled = structural)

  → CBT = changes STRUCTURE (re-compiles chunks) → best long-term outcome
  → COMBO: SSRIs create conditions → CBT re-compiles → taper SSRIs → maintain gains
  → OCD is NOT "weak willpower" — it is a medical condition requiring treatment
```

---

## §11 — Honest Assessment

### §11.1 — Established (🟢)

```
🟢 ESTABLISHED:
  → OFC-caudate hyperactive in OCD — fMRI replicated
  → SSRIs effective, require dose 3-4× depression — APA guidelines
  → CBT/ERP effective — randomized controlled trials
  → SSRIs+CBT > either alone — gold standard, multiple RCTs
  → Relapse: SSRIs alone ~80%, CBT alone ~20-30%
  → Serotonin ↓40% when in love ≈ OCD — Marazziti 1999
  → Heritability ~47-58% — twin studies (Pauls 2010)
  → Bimodal onset: childhood + late adolescence
  → PANDAS/PANS: antibodies → caudate → OCD — Swedo 1998
  → Noradrenergic antidepressants NOT effective for OCD
  → Clomipramine (serotonergic) > noradrenergic
  → Waxing-waning course — Skoog & Skoog 1999
  → ~25-30% full remission
  → Spreading activation — Collins & Loftus 1975
  → Reward prediction error — Schultz 1997
  → SNC effect — Crespi 1942, Flaherty 1996
  → Cross-species OCD-like: deer mice (Korff, Stein & Harvey 2008),
    SAPAP3 mice (Welch et al. 2007, Nature), Hoxb8 mice (Greer & Capecchi 2002;
    Chen et al. 2010 bone marrow rescue), CCD dogs (Dodman et al. 2010;
    Irimajiri et al. 2009 fluoxetine RCT)
  → Captive primate stereotypies — basal ganglia (Mason & Latham 2004)
  → Primate SIB + serotonergic (Novak et al. 2006; Lutz research program)
  → Anxious attachment (Bowlby 1969, Ainsworth 1978)
  → OCD in autism ~17.4% — van Steensel, Bögels & Perrin 2011 (meta-analysis)
```

### §11.2 — Framework Synthesis (🟡)

```
🟡 FRAMEWORK SYNTHESIS:
  → 3-line "done" pipeline: each line HAS independent evidence
    (PANDAS = Line 1, SSRIs = Line 2, CBT = Line 3)
  → Serotonin = "certainty bias": consistent, explains more than "happiness"
    (Status.md v2.1 §9.2 Serotonin Ratchet)
  → ⭐ Serotonin ↓ = AMPLIFIER, NOT ROOT CAUSE (§4.5):
    parallel with cortisol (amplifier, not cause). 4 evidence points:
    PANDAS (fix root → resolves), relapse pattern (SSRI vs CBT),
    love self-resolves (bond compiles → serotonin recovers naturally),
    cross-species variation (mice=hardware, primates=mix, humans=consequence)
  → ⭐ Cross-species OCD (§4.6): deer mice + SAPAP3 mice + dogs + primates
    → circuit ANCIENT (basal ganglia), NOT PFC-specific bug.
    Lines 1+2 = cross-species. Line 3 = ONLY HUMANS.
  → ⭐ Self-Pattern-Modeling childhood bias × OCD-like in love (§4.5b):
    anxious attachment = Self-Pattern-Modeling library threat-biased → hyper-monitoring →
    compound uncertainty (Self-Pattern-Modeling + obligation) → serotonin ↓ amplified
  → Love ↔ OCD same circuit: supported by Marazziti, strong logic
  → Spreading activation uninhibited: serotonin ↓ = less inhibition → cascade
    (Chunk-Activation-Dynamics.md §2 + Collins & Loftus 1975 🟢)
  → Chunk-Miss not resolving: OCD through Body-Feedback-Mechanism (§4.1) — consistent
  → Baseline Shift escalation: Body-Feedback-Mechanism §5 applied — consistent with OCD worsening
  → 5 Cortisol Roles in OCD: Role ②→③→⑤ escalation path
  → PFC 5% operator override failure: consistent with CBT evidence
  → Competitive re-linking (CBT): new chunks vs old chunks
  → Hardware/environment ratio per line: model, not directly measured
  → Spectrum (BDD, health anxiety, jealousy): BDD confirmed DSM-5
  → Tesla trajectory: functional → OCD-like via 3-line degradation
  → Extended limerence = OCD-like: consistent, not formally tested
  → ⭐ Basal ganglia × Parkinson bridge (§4.7): Parkinson = gate LOCKED,
    OCD = gate signal NOISY — same architectural principle, different failure mode.
    DBS for both: same bypass principle, different targets. Strengthens "ancient circuit."
  → ⭐ PTSD intrusions vs OCD obsessions (§7.1): PTSD = context-FREE chunk
    (amygdala-encoded, missing 3/4 metadata). OCD = context-INTACT chunk
    (done signal noisy). Same "PFC knows" but: PTSD = body BEFORE PFC
    (temporal), OCD = body DOESN'T TRUST done signal (quality).
  → ⭐ Autism × OCD cascade (§7.2): 17.4% prevalence. 3 pathways
    (sensory gain → uncertainty, masking → cortisol, predictive coding → threshold).
    RRBs ≠ OCD (ego-syntonic vs dystonic). "Cascade not comorbidity."
```

### §11.3 — Hypothesis (🔴)

```
🔴 TESTABLE PREDICTIONS:

  ⭐ SEROTONIN = AMPLIFIER TEST (§4.5):
    → PANDAS: measure serotonin transporter BEFORE and AFTER caudate treatment
      IF recovers → serotonin = consequence (root fixed → serotonin follows)
      IF doesn't recover → serotonin has independent component
    → Anxious vs secure attachment: measure serotonin when in love
      IF anxious ↓ MORE strongly → Self-Pattern-Modeling bias → compound uncertainty → support

  ⭐ CROSS-SPECIES PREDICTIONS (§4.6):
    → Deer mice OCD-like: test with environmental enrichment
      IF enrichment reduces OCD-like → environment component confirmed
      IF not → pure hardware → consistent with Line 1 ~80% hardware
    → Hoxb8 mice neuroimmune: extend to adult human inflammatory conditions?

  ⭐ BASAL GANGLIA COMPARISON (§4.7):
    → Parkinson DBS (STN) vs OCD DBS (VC/VS): different targets, same principle
      IF mechanism overlaps → DBS parameter optimization cross-informs?
    → Parkinson + OCD co-occurrence: dopamine medication → OCD symptoms?

  ⭐ AUTISM CASCADE (§7.2):
    → Sensory accommodation → reduces OCD symptoms in autistic people?
      IF reduces → supports "cascade" model (root = load, not independent OCD)
      IF not → OCD = independent co-occurring condition
    → RRBs vs OCD: ego-syntonic/dystonic test reliable cross-culturally?

  EXISTING PREDICTIONS (retained):
    → Tryptophan depletion → increases CHECKING behavior (not just mood)?
    → "Done" detector trainable? PANDAS: caudate recovery = partially plastic?
    → Love → OCD risk? Repeated unstable relationships → chronic serotonin ↓?
    → Mild chronic inflammation in adults → subclinical OCD? (extend PANDAS)
    → Lifestyle → measure lines: Sleep → Line 3, Exercise → Line 2
    → OCD target selection: hardware or compiled chunks?
    → AI as external "done" validator: helpful or new compulsion?
```

---

## §12 — Open Questions

```
OCD-Q1: Can the "done" detector be TRAINED?
  → Line 1 = hardware → if fixed → NO
  → BUT PANDAS: caudate recovers after inflammation → partially plastic?
  → CBT targets Line 3 or also repairs Line 1? → unclear

OCD-Q2: Bimodal onset = 2 failure modes?
  → Peak 1 (~8-12): Line 1 hardware primary
  → Peak 2 (~18-25): Lines 2+3 environment primary
  → Testable: childhood onset RESPONDS DIFFERENTLY to treatment?

OCD-Q3: Love circuit overlap → clinical implications?
  → Do OCD patients love DIFFERENTLY? (serotonin ALREADY low baseline)
  → Many unstable relationships → chronic serotonin ↓ → OCD risk?

OCD-Q4: Mild chronic inflammation → subclinical OCD in adults?
  → Extend PANDAS: gut inflammation, mild autoimmune
  → → slight caudate effects → "gradually becoming more meticulous"?

OCD-Q5: Aging × OCD prevention?
  → Tesla trajectory: knowing the mechanism → can prevent?
  → Maintain serotonin + PFC training + cortisol management?

OCD-Q6: AI in OCD treatment?
  → AI = external done validator? (helpful or new compulsion?)
  → AI + CBT = guided ERP at home?

OCD-Q7: Serotonin causal direction — species gradient?
  → Mice: serotonin closer to hardware cause (genes, wiring, less cognitive)
  → Primates: mix cause + consequence (social deprivation component)
  → Humans: closer to consequence + amplifier (many uncertainty sources)
  → = Serotonin ROLE changes with species complexity?
  → Testable: interventions target ROOT vs SEROTONIN → compare outcome

OCD-Q8: Self-Pattern-Modeling childhood bias → adult OCD-like in love?
  → Strict parenting → Self-Pattern-Modeling threat-biased → adult hyper-monitors partner
  → + Obligation overthinking compound
  → = Anxious attachment mechanism EXPLAINED through framework
  → Testable: attachment style × serotonin levels × relationship stability

OCD-Q9: Hoxb8 mice neuroimmune × PANDAS × adult chronic inflammation?
  → Mice: bone marrow transplant fixes OCD-like (neuroimmune)
  → Children: PANDAS = autoimmune attack on caudate
  → Adults: chronic low-grade inflammation (gut, autoimmune)
    → subclinical caudate impact? → "gradually becoming more meticulous"?
  → = SAME principle at 3 levels: mice / children / adults

OCD-Q10: Autism × OCD — cascade model testable? (§7.2)
  → 17.4% autistic children have OCD — higher than ~2-3% general population
  → IF sensory accommodation + reduce masking → OCD symptoms ↓
    → = CASCADE confirmed (root = architecture + load)
  → IF OCD persists despite reduced load → independent co-occurring OCD
  → Testable: compare OCD response to SSRIs+CBT in autistic vs NT

OCD-Q11: PTSD + OCD compound — bidirectional risk? (§7.1)
  → PTSD chronic cortisol → Lines 2+3 weakened → OCD ESCALATES?
  → Pre-existing OCD hypervigilance + trauma = PTSD risk ↑?
  → Treatment order: stabilize PTSD first (cortisol) → then OCD?
  → Testable: PTSD veterans with pre-existing OCD traits → outcome comparison
```

---

## §13 — Cross-References + Status

### §13.1 — Cross-References v7.8

```
MECHANISM FILES:
  → Body-Feedback-Mechanism.md v2.0 — Chunk-Shift/Miss/Gap, §4 Compound, §5 Baseline Shift
  → Chunk-Activation-Dynamics.md — spreading activation, probability, trigger surface
  → Chunk.md v2.1 — substrate, compilation, competitive re-linking
  → Cortisol-Baseline.md v2.1 — 5 Cortisol Roles §7.7, cascade, PFC damage §9
  → PFC-Function.md v1.2 — 24 functions, HOLD + PROCESS, ~5% operator
  → Status.md v2.1 — §9.2 Serotonin Ratchet, certainty bias

OBSERVATION PARAMETERS:
  → Threat.md v1.0 — threat priority > PFC, 3 origin sources
  → Connection.md v4.0 — social buffering (co-regulation reduces cortisol)
  → Feeling.md v2.1 — PFC observation interface (ego-dystonic = PFC observes "wrong")

RESEARCH FILES:
  → Love-Romantic.md v2.4 — §2.1 serotonin mechanism, §4.2 spreading activation
  → Hijack/Addiction-Analysis.md v3.0 — OCD loop vs addiction loop
  → Autism-Observation.md v1.0 — §8.4 Special Interests vs OCD, §13.1 OCD 17.4% (v2.2 §7.2)
  → PTSD-Analysis.md v1.0 — §14 context-tag model, §4 body-first temporal (v2.2 §7.1)
  → Parkinson-Analysis.md v1.1 — §2 basal ganglia gate mechanism (v2.2 §4.7)

CLARIFICATION:
  → Dopamine-Is-Not-Reward.md v1.1 — dopamine = salience (augmentation rationale)
  → Cortisol-Amplifier-Not-Cause.md — cortisol ≠ stress hormone
```

### §13.2 — File Status

```
⭐ STATUS:

  Version: v2.2 (enriched post Health Conditions Drill)
  Date: 2026-05-15
  Lines: ~1,450+
  Backup: backup/OCD-Analysis-v75-era.md (896L, 2026-03-27)

  v2.0 CHANGES:
    ① ADDED §4: Chunk dynamics + spreading activation mapping
    ② UPDATED: All terminology v7.5 → v7.8
    ③ ADDED: 5 Cortisol Roles applied to OCD (§4.3)
    ④ ADDED: PFC-Function mapping for Line 3 (§4.4)
    ⑤ UPDATED: Love ↔ OCD reference Love-Romantic v2.2
    ⑥ ADDED: Competitive re-linking for CBT mechanism
    ⑦ UPDATED: All cross-references → v7.8 files
    ⑧ KEPT: Core 3-line model, PANDAS, treatment map, spectrum, Tesla

  v2.1 ADDITIONS (2026-04-26):
    ⑨ §4.5: Serotonin = AMPLIFIER, NOT ROOT CAUSE (key insight)
    ⑩ §4.5b: Self-Pattern-Modeling childhood bias × love OCD-like (anxious attachment mechanism)
    ⑪ §4.6: Cross-species evidence (mice, dogs, primates)
    ⑫ Updated §11 Honest Assessment + §12 Open Questions

  v2.2 ADDITIONS (2026-05-15 — post Health Conditions Drill):
    ⑬ §4.7: Basal ganglia × Parkinson bridge (gate LOCKED vs NOISY)
    ⑭ §7.1: PTSD intrusions vs OCD obsessions mechanism distinction
    ⑮ §7.2: Autism × OCD co-occurrence (17.4%, RRBs vs compulsions, cascade)
    ⑯ Cross-refs: 6 drill files added, dependency versions refreshed
    ⑰ §11-§12: New synthesis items, predictions, open questions (Q10-Q11)
```

---

> *OCD = "done" pipeline failure in 1 or more lines.*
> *PANDAS/PANS = causal evidence: damage caudate (Line 1) → OCD → fix → resolves.*
> *Love uses THE SAME circuit (serotonin ↓40% → uninhibited spreading activation)*
> *but SELF-STOPS when bond compiles → done detector: DONE.*
> *OCD DOES NOT SELF-STOP because target has no exit condition.*
> *Serotonin ↓ = AMPLIFIER, NOT ROOT CAUSE — like cortisol.*
> *Root cause = Line 1 hardware / stress / genuine uncertainty.*
> *Cross-species evidence (mice, dogs, primates): circuit ANCIENT (basal ganglia), NOT PFC bug.*
> *Lines 1+2 = cross-species. Line 3 (PFC override) = HUMANS ONLY.*
> *v2.2: Parkinson = gate LOCKED, OCD = gate NOISY — same basal ganglia, different failure.*
> *PTSD intrusions = context-FREE chunks. OCD obsessions = context-INTACT, done-signal failure.*
> *Autism × OCD 17.4%: cascade not comorbidity. RRBs ≠ OCD (ego-syntonic vs dystonic).*
> *Treatment: SSRIs = break amplifier loop (Line 2), CBT = fix root chunks (Line 3).*
> *⚠️ Framework provides PERSPECTIVE — does not replace medical diagnosis/treatment.*
>
> *v1.0-english — translated 2026-06-11 from source v2.2 (2026-05-15)*

<!-- END -->
