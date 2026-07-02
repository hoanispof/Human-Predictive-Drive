---
title: Entity-Access-Calibration — How Entity-Access Self-Regulates (or Fails To)
version: 1.0
created: 2026-05-22
status: MECHANISM v1.0
scope: |
  CALIBRATION MECHANISM for Entity-Access:
  Entity-access calibration = Reward-Calibration APPLIED to entity access.
  3-Layer Architecture: Body Signal × Engine Simulation × Feedback Integration.
  Exit Cost = Signal Weight: strongest bond = hardest to calibrate.
  Hardware-Subsidy = Calibration Bias: hormone masks excess.
  Compiled vs Fresh: calibration window. Engine use quality: curiosity vs threat.
  Optimal Zone ≠ Zero C. Per bond type dynamics. 5 failure modes.
  Cannot prescribe. Training + spiral. Per-Level gradient difficulty.
purpose: |
  Entity-Access.md = GRADIENT MODEL (Level 0-5, 3-Factor, quality).
  Entity-Access-Excess.md = EXCESS TERRITORY (Level 5, mechanism, manifestation, fix).
  THIS FILE = CALIBRATION MECHANISM: HOW entity-access self-regulates,
  why it is difficult/easy per bond type and per Level, what enables/blocks
  calibration, and why "how much entity-access is enough" CANNOT be prescribed.
  = "Entity-Access shows ACCESS AT WHAT LEVEL. Entity-Access-Excess shows
  WHEN access becomes a problem. This file shows HOW CALIBRATION WORKS,
  WHY it is hard, and HOW IT CAN BE TRAINED."
position: |
  Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/ — same folder as
    Entity-Access, Self-Pattern-Modeling, By-Product-Gap-Resonance.
  Entity-Access.md §8 = summary + cross-ref to this file.
  Entity-Access-Excess.md = WHEN excess territory (companion).
  This file = HOW calibration works (companion).
  Parallel: Reward-Calibration.md = general | This file = applied to entity access.
dependencies:
  - Entity-Access.md v1.1 — PREREQUISITE: 3-Factor Model, Gradient Level 0-5, A:B:C:D
  - Entity-Access-Excess.md v1.0 — COMPANION: excess territory Level 5, fix spectrum
  - Entity-Compiled.md v1.0 — FOUNDATION: brain compiles agent into body-base
  - Simulation-Engine.md v1.0 — FOUNDATION: 1 engine, 3 components, reflection/rumination
  - PFC-Operations.md v1.0 — FOUNDATION: Hold/Suppress, Compiled/Fresh, PFC universal
  - Compiled-Fresh.md v2.0 — FOUNDATION: compiled quality, reversal, PFC shared budget
  - Self-Pattern-Modeling.md v3.1 — FOUNDATION: Self-Pattern-Modeling as Simulation-Engine application
  - Valence-Propagation.md v3.0 §3 — DEFINES Entity-Compiled + 3 subtypes
  - Body-Feedback-Mechanism.md v2.0 §3.3c — FOUNDATION: Gap→Miss baseline
  - Reward-Calibration.md v1.1 — PARALLEL: Goldilocks, cannot prescribe, dynamic equilibrium
  - Logic-Feeling-Balance.md v1.0 — PARALLEL: infinite regress, domain feedback only
  - Connection.md v4.0 — COMPANION: 2-body calibration, bids, mutual phenomenon
  - Social-Calibration.md v1.1 — COMPANION: social system calibration (CHECK function)
  - Empathy.md v2.2 — DOWNSTREAM: burnout as calibration failure
  - Autonomy-Hardware.md v1.1 — FOUNDATION: vmPFC + DRN, autonomy violation detection
  - Gap-Distribution-Profile.md v1.0 — COMPANION: portfolio risk, diversification
  - Self-Created-Threat.md v1.0 — DOWNSTREAM: threat-mode calibration failure
  - AI-Self-Model.md v2.0 — DOWNSTREAM: Dual Check as calibration mechanism
  - Ask-AI.md v3.1 — DOWNSTREAM: body as quality controller = Layer 1 calibration
  - PFC-Label.md v1.0 — VOCABULARY: PFC roles, deprecated terms
  - Body-Feedback-Label.md v2.0 — VOCABULARY: body signal labels
sources:
  - Drill-Entity-Access-Calibration v2.0 (1,159 lines, 20 insights, 25 citations)
  - Entity-Access.md v1.1 §8 (extracted + expanded)
language: English (translated from Vietnamese source v1.0)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Entity-Access-Calibration — How Entity-Access Self-Regulates (or Fails To)

> **Entity-Access Calibration = Reward-Calibration APPLIED to entity access:**
> **"HOW MUCH entity-access IS ENOUGH?"**
>
> **TOO LITTLE → bond atrophy (no bids → no Entity-Compiled formation → drift apart).**
> **TOO MUCH → entity autonomy violated (own drives suppressed).**
> **Goldilocks = the middle zone. NOT FIXED.**
>
> **3-LAYER CALIBRATION ARCHITECTURE:**
> **Layer 1 — Body Signal: "what am I feeling when I want to access?"**
> **Layer 2 — Engine Simulation: "what will entity experience if I access/push?"**
> **Layer 3 — Feedback Integration: "how did entity respond? → adjust?"**
>
> **EXIT COST = SIGNAL WEIGHT:**
> **Close Friends (Level 3): exit easy → "no" = STRONG signal → SELF-CORRECTS.**
> **Parent→Child (Level 4-5): exit impossible → "no" = WEAK signal → INTERNAL calibration only.**
>
> **HARDWARE-SUBSIDY = CALIBRATION BIAS:**
> **Hormone fires → entity-access FEELS justified → C masked as A.**
>
> **Compiled = BELOW PFC → calibration IMPOSSIBLE.**
> **Fresh = PFC active → calibration POSSIBLE.**
>
> **Engine use quality: Curiosity → productive. Threat → rumination → WORSE.**
> **Optimal Zone ≠ Zero C: justified C = NECESSARY (Baumrind, Gottman, Deci & Ryan).**
> **CANNOT PRESCRIBE "how much is enough" — domain feedback = THE ONLY arbiter.**

---

## Table of Contents

- §0 — THESIS + POSITION
- §1 — CALIBRATION = DYNAMIC EQUILIBRIUM
- §2 — 3-LAYER CALIBRATION ARCHITECTURE
- §3 — EXIT COST = SIGNAL WEIGHT
- §4 — HARDWARE-SUBSIDY = CALIBRATION BIAS
- §5 — COMPILED vs FRESH: CALIBRATION WINDOW
- §6 — ENGINE USE QUALITY: CURIOSITY vs THREAT
- §7 — OPTIMAL ZONE: JUSTIFIED C + BIDS
- §8 — PER BOND TYPE CALIBRATION DYNAMICS
- §9 — 5 CALIBRATION FAILURE MODES
- §10 — CANNOT PRESCRIBE
- §11 — TRAINING + VIRTUOUS/VICIOUS SPIRAL
- §12 — CALIBRATION × ENTITY-ACCESS GRADIENT
- §13 — HONEST ASSESSMENT
- §14 — CROSS-REFERENCES
- §15 — RESEARCH CITATIONS

---

## §0 — THESIS + POSITION

```
⭐⭐⭐ ENTITY-ACCESS CALIBRATION v1.0:

  ENTITY-ACCESS (Entity-Access.md v1.1):
    3-Factor Model: Compiled Engine Mode × Fresh Gap-Need Profile × F3 Access Confidence
    Gradient: Level 0 (Tool/Service) → Level 5 (Excess)
    Entity-Owned = PFC LABEL for Level 4-5 (observation, not mechanism)

  CALIBRATION = HOW ENTITY-ACCESS SELF-REGULATES:

  ① Calibration = dynamic equilibrium: observe → adjust → observe (LOOP)
  ② 3-Layer Architecture: Body Signal × Engine Simulation × Feedback Integration
  ③ Exit Cost = Signal Weight: friends (Level 3) self-calibrate,
      parent→child = INTERNAL only
  ④ Hardware-Subsidy = Calibration BIAS: hormone → entity-access feels justified →
      C masked
  ⑤ Compiled entity-access behaviors = BELOW PFC → calibration IMPOSSIBLE
      until decompile
  ⑥ Fresh entity-access = PFC ACTIVE → calibration POSSIBLE in real-time
  ⑦ Engine use quality: curiosity → productive calibration. Threat → rumination.
  ⑧ Optimal Zone ≠ Zero C: justified C = NECESSARY (structure + responsiveness)
  ⑨ Bids for connection = mild C expression = bond MAINTENANCE
  ⑩ CANNOT prescribe "how much is enough" — infinite regress, domain feedback only
  ⑪ Calibration itself CAN be Generative reward (curiosity → insight → intriguing)
  ⑫ Per Level: calibration difficulty ↑ with entity-access depth

  QUESTIONS THIS FILE ANSWERS:
    Entity-Access.md: "WHAT IS entity-access? How does the mechanism work?"
    Entity-Access-Excess.md: "When does entity-access BECOME a problem?"
    ★ This file: "HOW does calibration work? Why is it easy/hard per Level?"

  PARALLEL:
    Reward-Calibration.md = "HOW MUCH reward is enough?" (general)
    ★ This file = "HOW MUCH entity-access is enough?" (applied)
    Logic-Feeling-Balance.md = "CANNOT prescribe balance" (epistemological)
    ★ This file = same principle applied to entity-access calibration

  🟢 Baumrind 1966, Deci & Ryan 2000, Gottman 2001, Fonagy 2002
  🟡 3-Layer Architecture + Exit Cost = Signal Weight = framework synthesis
```

---

## §1 — CALIBRATION = DYNAMIC EQUILIBRIUM

```
⭐⭐ ENTITY-ACCESS CALIBRATION = REWARD-CALIBRATION APPLIED TO ENTITY ACCESS:

  Reward-Calibration.md §5 core:
    → Every reward has a GOLDILOCKS — too little = deficit, too much = problem
    → CANNOT prescribe — because person × context × time × gap = ALL dynamic
    → Domain feedback = THE ONLY arbiter
    → Perception-action cycle: observe → adjust → observe → ...

  Entity-Access Calibration FOLLOWS THE SAME PATTERN:

    ┌─────────────┬───────────────────────┬────────────────────────────────┐
    │ Zone        │ Entity-access state   │ Consequence                    │
    ├─────────────┼───────────────────────┼────────────────────────────────┤
    │ UNDER       │ Too little            │ Bond atrophy: no bids →        │
    │             │ access-seeking        │ no Entity-Compiled formation → │
    │             │ "everyone for         │ drift apart                    │
    │             │ themselves"           │                                │
    ├─────────────┼───────────────────────┼────────────────────────────────┤
    │ GOLDILOCKS  │ Calibrated access-    │ Bond maintained: bids →        │
    │             │ seeking. Responsive   │ responses → Entity-Compiled ↑  │
    │             │ to entity feedback.   │ → bond ↑. Entity autonomy      │
    │             │                       │ INTACT.                        │
    ├─────────────┼───────────────────────┼────────────────────────────────┤
    │ OVER        │ Too much access.      │ Entity drives suppressed:      │
    │             │ Ignores entity "no."  │ autonomy violated →            │
    │             │                       │ excess territory (Level 5)     │
    └─────────────┴───────────────────────┴────────────────────────────────┘

    Goldilocks = NOT FIXED:
      Varies per person (hardware, temperament, attachment history)
      Varies per entity (infant vs teen vs adult child vs partner vs friend)
      Varies per context (rested vs depleted, crisis vs routine)
      Varies per time (limerence vs 20 years, child age 2 vs age 18)
      → 4 dimensions ALL dynamic → fixed formula IMPOSSIBLE

  BUT Entity-Access Calibration IS MORE COMPLEX than general reward calibration:

    ① 2 bodies — not just self-regulation (Connection.md §9)
    ② Power asymmetry — affects signal quality (parent > child)
    ③ Hardware-subsidy — creates BIAS (hormone → overestimate need)
    ④ Compiled patterns — resist change (automatic, below PFC)
    ⑤ PFC = the Lawyer — rationalizes C as A+B (McNulty 2013)
    → 5 additional complexity factors BEYOND simple reward calibration

  🟡 Entity-access calibration = reward calibration applied = framework synthesis
  🟢 Reward Goldilocks: Reward-Calibration.md §1
  🟢 Dynamic equilibrium: Reward-Calibration.md §5.2
```

---

## §2 — 3-LAYER CALIBRATION ARCHITECTURE

```
⭐⭐⭐ CALIBRATION REQUIRES ALL 3 LAYERS SIMULTANEOUSLY (★ CORE):

  ┌─────────────────────────────────────────────────────────────────────┐
  │ LAYER 1 — BODY SIGNAL (Interoception)                               │
  │                                                                      │
  │ "What am I actually feeling when I want to access entity?"           │
  │                                                                      │
  │ Curiosity (A+B): "hmm, I wonder how the child is doing?"            │
  │   → opioid preview → approach → GENUINE access desire               │
  │ Anxiety (C): "the child must eat, I'm so worried"                   │
  │   → cortisol high → urgency → SELF-REFERENTIAL gap driving          │
  │ Obligation (D): "I have to look after the child"                    │
  │   → relief-seeking → compliance → SCHEMA gap driving                │
  │                                                                      │
  │ Interoception DETECTS body signal → reveals which gap source        │
  │ is CURRENTLY active                                                  │
  │ = Simulation-Engine Component 1 (anterior insula readout)           │
  │                                                                      │
  │ ⚠️ REQUIRES: interoceptive accuracy (trainable — Fukushima 2011)   │
  │ ⚠️ FAILS when: alexithymia, habituation, depleted state            │
  ├─────────────────────────────────────────────────────────────────────┤
  │ LAYER 2 — ENGINE SIMULATION (Constructive Simulation)               │
  │                                                                      │
  │ "If I access/push, what will entity experience?"                    │
  │                                                                      │
  │ Compiled Agent-mode Self-Pattern-Modeling: model entity's internal  │
  │   state → predict response:                                          │
  │   "child will feel pushed → avoidance tag"                          │
  │ Imagine-Final: simulate outcome                                      │
  │   → "if I force-feed → child will hate eating long-term →           │
  │      bad outcome"                                                    │
  │ = PFC draft prediction BEFORE acting                                 │
  │                                                                      │
  │ ⚠️ REQUIRES: Compiled ≥ Agent-mode (Entity-Access.md §1.1)         │
  │ ⚠️ FAILS when: Compiled = Tool-mode (predicts behavior, not state) │
  │   Tool-mode: "'has the child eaten?'" (function check, no state)   │
  │   Agent-mode: "'is the child actually hungry? what are they         │
  │     feeling?'" (state modeling)                                      │
  │                                                                      │
  │ = Simulation-Engine Component 2 (DMN + hippocampus = CPU)           │
  ├─────────────────────────────────────────────────────────────────────┤
  │ LAYER 3 — FEEDBACK INTEGRATION (Response × Adjustment)              │
  │                                                                      │
  │ "How did entity respond? → prediction delta → adjust?"              │
  │                                                                      │
  │ Entity says "no" → prediction delta → 2 paths:                      │
  │   Path A — Integrate: "ah, child is genuinely full" → adjust →     │
  │     stop pushing                                                     │
  │   Path B — Override: compiled response fires → "'eat more!'" →     │
  │     no adjustment                                                    │
  │                                                                      │
  │ ⚠️ REQUIRES: PFC-Fresh state (Compiled-Fresh.md §10)               │
  │ ⚠️ FAILS when: compiled response overrides (automatic, bypasses    │
  │   PFC)                                                               │
  │                                                                      │
  │ = Simulation-Engine Component 3 (mPFC: adjust self-behavior)        │
  └─────────────────────────────────────────────────────────────────────┘

  CALIBRATION = ALL 3 LAYERS SIMULTANEOUSLY:
    Layer 1: detect own gap source (A/B/C/D)
    Layer 2: predict entity experience (Compiled Agent-mode)
    Layer 3: integrate entity feedback → adjust
    → LOOP: observe → predict → act → entity responds → observe → ...

  FAILURE WHEN ANY LAYER FAILS:

    ┌────────────────┬──────────────────────────────┬────────────────────────┐
    │ Layer fail     │ Consequence                  │ Example                │
    ├────────────────┼──────────────────────────────┼────────────────────────┤
    │ Layer 1        │ Blind to own gap source →    │ Parent "genuinely      │
    │ (interoception)│ C invisible → no adjustment  │ loves" but doesn't     │
    │                │                              │ know they're anxious   │
    ├────────────────┼──────────────────────────────┼────────────────────────┤
    │ Layer 2        │ Cannot predict entity        │ Compiled Tool-mode:    │
    │ (simulation)   │ experience → pushes without  │ "'has the child        │
    │                │ understanding impact         │ eaten?'" (no state)    │
    ├────────────────┼──────────────────────────────┼────────────────────────┤
    │ Layer 3        │ Entity responds but it is    │ Child says "no" →      │
    │ (feedback)     │ not integrated → repeats     │ parent still forces    │
    │                │                              │ (compiled override)    │
    ├────────────────┼──────────────────────────────┼────────────────────────┤
    │ All 3          │ Compiled chain → no          │ Depleted + anxious +   │
    │                │ observation at all           │ compiled → auto-pilot  │
    └────────────────┴──────────────────────────────┴────────────────────────┘

  🟡 3-Layer Calibration Architecture = framework synthesis
  🟢 Interoceptive accuracy → empathic accuracy: Fukushima 2011 (R14)
  🟢 Simulation-Engine 3 Components: Simulation-Engine.md §1
  🟢 PFC-Fresh as universal resource: Compiled-Fresh.md §10
```

---

## §3 — EXIT COST = SIGNAL WEIGHT

```
⭐⭐⭐ WHY FRIENDSHIPS SELF-CALIBRATE BUT PARENT→CHILD DOES NOT (★ CORE):

  CORE INSIGHT:
    Entity's "no" = CALIBRATION SIGNAL
    Signal WEIGHT = f(exit cost × alternative availability)

    High exit cost → entity's "no" = WEAK signal → can be IGNORED
    Low exit cost → entity's "no" = STRONG signal → MUST adjust or lose them

  PER LEVEL (Entity-Access.md §2):

    ┌───────────────────┬───────────┬──────────────┬────────────────────────────┐
    │ Bond type         │ Exit cost │ Entity "no"  │ Calibration mechanism      │
    │ (Level)           │           │ signal weight│                            │
    ├───────────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Close Friends     │ LOW       │ HIGH         │ EXTERNAL sufficient:       │
    │ (Level 3)         │           │ (effective)  │ ignore → friend exits →    │
    │                   │           │              │ environment FORCES adjust  │
    ├───────────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Romantic          │ MODERATE  │ MODERATE     │ MIX external + internal:   │
    │ (Level 4)         │           │              │ some room for excess       │
    │                   │           │              │ before correction kicks in │
    ├───────────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Parent→Young      │ VERY HIGH │ LOW          │ INTERNAL ONLY:             │
    │ Child (Level 4-5) │ (child    │ (ineffective)│ child cannot exit →        │
    │                   │ can't     │              │ Self-Awareness (Axis 2)    │
    │                   │ exit)     │              │ = ONLY calibration source  │
    ├───────────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Parent→Adult      │ MODERATE  │ MOD→HIGH     │ EXTERNAL returns:          │
    │ Child (Level 4)   │ (can exit)│ (effective)  │ "'I'm busy'" = signal.     │
    │                   │           │              │ Adult child CAN exit →     │
    │                   │           │              │ signal weight ↑            │
    ├───────────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Professional      │ MOD→HIGH  │ MODERATE     │ Structural: contract,      │
    │ (Level 2-3)       │ (career)  │              │ HR, norms = external frame │
    └───────────────────┴───────────┴──────────────┴────────────────────────────┘

  CRITICAL INSIGHT FOR PARENTING:
    Parent→Young Child = THE ONLY bond type where:
      Power asymmetry = MAXIMUM
      Exit cost for entity = IMPOSSIBLE
      Entity's feedback signal = WEAKEST
      → External calibration = DISABLED
      → ONLY Self-Awareness (internal, Axis 2) can correct excess

    → WHY parenting requires the MOST Self-Awareness:
      Not because it is "harder"
      But because the EXTERNAL FEEDBACK MECHANISM is DISABLED by power asymmetry
      → Must rely ENTIRELY on internal observation (Axis 2)

    → Close Friends (Level 3) DO NOT NEED as much Self-Awareness:
      Environment self-corrects (friend exits if you are too much)
      → Entity-access naturally stays in Goldilocks zone
      → = Self-correcting mechanism

  LIFECYCLE SHIFT (parent→child):
    Young child (0-6): exit cost = INFINITE → signal weight ≈ 0
    Older child (12-18): exit cost ↓ (teen rebellion = PARTIAL exit) →
      signal ↑
    Adult child (18+): exit cost = MODERATE → signal = EFFECTIVE
    → "Absence reveals love" = ALSO:
      Adult child's ability to exit → parent's entity-access
        FORCED to recalibrate

  🟡 Exit Cost = Signal Weight = framework synthesis
  🟢 Power asymmetry in parenting: Maccoby 1992 (R21)
  🟢 Autonomy support in power-asymmetric relationships: Deci & Ryan 2000 (R2)
```

---

## §4 — HARDWARE-SUBSIDY = CALIBRATION BIAS

```
⭐⭐ HARDWARE-SUBSIDY = ANTI-HABITUATION + CALIBRATION BIAS:

  Entity-Access.md §5: Hardware-Subsidy = ANTI-HABITUATION.
  Parent→Child MAXIMUM subsidy → entity-access DURABLE.

  BUT THE SAME MECHANISM = CALIBRATION BIAS:

    Mechanism:
      Hormone fires (oxytocin, vasopressin) → entity-access FEELS justified
      → "'I genuinely love them'" = PARTIALLY TRUE (A hormone = genuine)
      → PFC uses A (genuine) to JUSTIFY C (self-referential)
      → = Compound signal: A+C fire SIMULTANEOUSLY → PFC CANNOT SEPARATE THEM

    Example:
      Parent looking at child:
        A fires: oxytocin (existence reward) → genuine → "'I love my child'"
        C fires: anxiety ("'the child must eat, I can't stop worrying'")
          → self-referential
        → Body signal = MIXED (opioid + cortisol SIMULTANEOUSLY)
        → PFC interprets EVERYTHING as "'I love my child'" (A explains it all)
        → C is INVISIBLE because A provides the "cover story"
        → = Hardware-subsidy MASKS excess entity-access

  COMPARISON PER BOND TYPE:

    ┌──────────────────┬───────────────┬───────────────┬───────────────────────┐
    │ Bond type        │ Hardware-     │ Bias level    │ Detection difficulty  │
    │                  │ subsidy       │               │                       │
    ├──────────────────┼───────────────┼───────────────┼───────────────────────┤
    │ Parent→Child     │ MAXIMUM       │ MAXIMUM       │ HARDEST: A always     │
    │ (Level 4-5)      │               │               │ present → always      │
    │                  │               │               │ provides "cover"      │
    ├──────────────────┼───────────────┼───────────────┼───────────────────────┤
    │ Child→Parent     │ MODERATE      │ MODERATE      │ Moderate: attachment  │
    │ (Level 4)        │               │               │ drive present but ↓   │
    ├──────────────────┼───────────────┼───────────────┼───────────────────────┤
    │ Romantic         │ TEMPORARY     │ HIGH→LOW      │ Limerence: VERY HARD  │
    │ (limerence)      │ (hormone)     │ (fades)       │ Post-limerence: EASIER│
    ├──────────────────┼───────────────┼───────────────┼───────────────────────┤
    │ Close Friends    │ ZERO          │ ZERO          │ EASIEST: no hormone = │
    │ (Level 3)        │               │               │ clear signal.         │
    │                  │               │               │ C = obvious           │
    ├──────────────────┼───────────────┼───────────────┼───────────────────────┤
    │ Professional     │ ZERO          │ ZERO          │ EASIEST: D is clear   │
    │ (Level 2-3)      │               │               │ (contract/obligation) │
    └──────────────────┴───────────────┴───────────────┴───────────────────────┘

  PARADOX — STRONGEST BOND = HARDEST TO CALIBRATE:
    Parent→Child: Hardware-subsidy MAXIMUM + Exit cost MAXIMUM + Power MAXIMUM
    → 3 factors ALL conspire AGAINST calibration
    → Strongest, most durable bond = most vulnerable to excess
    → = Trivers 1972: parental investment = HIGHEST → bias HIGHEST

    Close Friends (Level 3): Hardware-subsidy ZERO + Exit cost LOW +
      Power PARITY
    → 3 factors ALL SUPPORT calibration
    → Most fragile bond = most naturally calibrated
    → = WHY friendship rarely becomes "toxic" (self-correcting)

  🟡 Hardware-subsidy = calibration bias = framework synthesis
  🟢 Oxytocin × parental bias: Feldman 2012 (R17), Strathearn 2009 (R18)
  🟢 Parental investment theory: Trivers 1972 (R16)
```

---

## §5 — COMPILED vs FRESH: CALIBRATION WINDOW

```
⭐⭐ COMPILED ENTITY-ACCESS = BELOW PFC → CALIBRATION IMPOSSIBLE:

  Compiled-Fresh.md §6 Quality Dimension:
    Genuine-compiled → approach tag → Self-Pattern-Modeling expansive
    Schema-compiled → neutral tag → Self-Pattern-Modeling limited
    Threat-compiled → avoidance tag → Self-Pattern-Modeling biased

  APPLIED TO ENTITY-ACCESS BEHAVIORS:

    ┌───────────────────┬───────────────────────┬──────────────────────────────┐
    │                   │ COMPILED               │ FRESH                        │
    │                   │ (automatic)            │ (deliberate)                 │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ PFC role          │ PASSIVE or ZERO        │ ACTIVE (receive + adjust)    │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ Calibration       │ IMPOSSIBLE (below PFC) │ POSSIBLE (PFC accessible)    │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ Trigger           │ Entity cue → compiled  │ Deliberate: "hmm, let me    │
    │                   │ response fires auto    │ check what I'm feeling"      │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ Typical           │ "'Eat more!'" (auto)   │ "'Is the child actually      │
    │                   │                        │ hungry?'"                    │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ Quality           │ Locked (cannot shift)  │ Shiftable in real-time       │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ Cost              │ ≈ 0 (habituated)       │ > 0 (PFC budget required)    │
    ├───────────────────┼───────────────────────┼──────────────────────────────┤
    │ When dominant     │ Depleted, stressed,    │ Rested, curious, practiced   │
    │                   │ routinized             │                              │
    └───────────────────┴───────────────────────┴──────────────────────────────┘

  PFC-FRESH = SHARED BUDGET (Compiled-Fresh.md §10):
    PFC = universal resource for ALL activities
    Exhausted from work → PFC budget for entity-access calibration = REDUCED
    → Compiled entity-access behaviors take over (auto-pilot)
    → = Mikolajczak 2019: burnout → overcontrol OR emotional distance
    → Both outcomes = calibration FAIL (excess OR under)

  CASCADING EFFECT (Entity-Access.md §9: 4-Axis):
    Axis 4 depleted
    → PFC budget ↓ → Compiled shifts toward Tool-mode
    → Layer 1 (interoception) ↓: body signal ignored
    → Layer 2 (simulation) ↓: Compiled Tool-mode default
    → Layer 3 (feedback integration) ↓: compiled override
    → ALL 3 calibration layers FAIL SIMULTANEOUSLY
    → Entity-access = auto-pilot = excess or withdrawal territory

  DECOMPILE PATH (changing compiled entity-access behaviors):
    Compiled-Fresh.md §9: 6-step reversal
    → Requires: sustained PFC engagement + body re-experience + new tag
    → Timeline: months to years (therapy-level)
    → = WHY attachment style change IS POSSIBLE but SLOW (Fraley & Shaver 1998)

    Fresh practice → gradually compiles NEW patterns:
    → "Observe first, then act" practiced enough → compiles as default
    → = Mentalization training (Bateman & Fonagy 2006): teachable,
        compiles over time

  🟡 Compiled vs Fresh applied to entity-access calibration = framework synthesis
  🟢 PFC as shared resource: Compiled-Fresh.md §10
  🟢 Parental burnout → outcomes: Mikolajczak et al. 2019 (R10)
  🟢 Attachment change possible but slow: Fraley & Shaver 1998 (R19)
  🟢 Mentalization-Based Therapy: Bateman & Fonagy 2006 (R6)
```

---

## §6 — ENGINE USE QUALITY: CURIOSITY vs THREAT

```
⭐⭐ SAME "OBSERVE OWN ENTITY-ACCESS," DIFFERENT MODE → DIFFERENT OUTCOME:

  Simulation-Engine.md §9 (Trapnell & Campbell 1999):
    Reflection (curiosity cortisol) → insight → productive
    Rumination (threat cortisol) → loop → stuck

  APPLIED TO ENTITY-ACCESS CALIBRATION:

  CURIOSITY MODE (productive calibration):
    "Hmm, why do I want the child to eat more?"
    → Observe body: "ah, I'm anxious — the child isn't actually hungry"
    → INSIGHT fires → novelty reward (Generative gap fill)
    → Adjust behavior: "ok, the child said no, so that's fine"
    → Good outcome → confirms approach → MORE curiosity → LOOP
    → = Calibration BECOMES source of Generative reward
    → = "Intriguing" — observation itself IS rewarding

    Cortisol direction: NOVELTY → approach tag
    Body state: relaxed, open, exploratory
    Compiled: Agent-mode (curious about entity's actual state)
    PFC role: receive + simulate + compare + adjust

  THREAT MODE (destructive calibration):
    "'Am I controlling too much? Am I a bad parent?'"
    → Self-judgment → threat cortisol → ruminate
    → NO insight (threat BLOCKS exploration — Compiled-Fresh.md §6.2)
    → Paradox: attempting to calibrate → anxiety → calibration FAILS
    → 3 possible outcomes:
      A) Over-correct: permissive ("let it go, afraid to push") → under → bond atrophy
      B) Freeze: cannot act → compiled takes over → forces anyway
      C) Guilt loop: "'I'm terrible'" → ruminate → no adjustment
    → = Self-Created-Threat mechanism applied to parenting

    Cortisol direction: THREAT → avoidance tag
    Body state: tense, contracted, defensive
    Compiled: biased (projects fear onto entity)
    PFC role: judge + loop + stuck

  ⭐ WHY THIS MATTERS:
    All "parenting advice" of the type "'don't force the child'"
      without MODE context:
    → Parent receives as THREAT: "'I'm forcing = I'm a bad parent'"
    → Switch to threat mode → calibration WORSE not better
    → = Parenting guilt epidemic: advice intended to help →
        triggers threat mode

    EFFECTIVE approach: encourage CURIOSITY about own patterns:
    → "'Why do I want this?'" (curiosity)
        > "'I was wrong!'" (threat)
    → = Fonagy 2002: mentalization training focuses on curiosity,
        not judgment
    → = Simulation-Engine.md §11: reflection practice =
        cultivate curiosity

  🟢 Reflection vs Rumination: Trapnell & Campbell 1999 (R7)
  🟢 Reflection → empathy: Joireman, Parrott & Hammersla 2002 (R8)
  🟢 Mentalization as curiosity: Fonagy 2002 (R5)
  🟡 Curiosity vs Threat mode applied to entity-access = framework synthesis
```

---

## §7 — OPTIMAL ZONE: JUSTIFIED C + BIDS

```
⭐⭐⭐ OPTIMAL ENTITY-ACCESS ≠ ZERO C (★ CORE CORRECTION):

  3 RESEARCH LINES CONFIRM justified C = NECESSARY:

  ① BAUMRIND 1966, 1991 — AUTHORITATIVE PARENTING:
    4 styles: Authoritative / Authoritarian / Permissive / Neglectful
    BEST OUTCOMES: Authoritative = HIGH demand + HIGH responsiveness
    NOT Permissive (low demand + high responsiveness)

    Framework mapping:
      Authoritative = justified C + Compiled Agent-mode
        (demands BUT is responsive)
      Authoritarian = C+D dominant + Compiled Tool-mode
        (demands, no responsiveness)
      Permissive = zero C → under entity-access → child lacks structure
      Neglectful = zero everything → no bond

    → Structure (justified C) IS NECESSARY for child development
    → C itself is not the problem. C WITHOUT RESPONSIVENESS = problem.

  ② DECI & RYAN 2000 — SELF-DETERMINATION THEORY:
    Autonomy support ≠ absence of structure
    Structure + autonomy support = OPTIMAL
    Structure WITHOUT autonomy support = controlling

    Framework mapping:
      Structure = justified C (parent sets boundary)
      Autonomy support = Compiled Agent-mode
        (observes entity state, respects their drive)
      Control = C without Agent-mode
        (ignores entity state, imposes my gap direction)

    → Insisting on medicine (child cannot decide) + explain + acknowledge
        = structure + autonomy
    → Insisting on medicine without explanation = control
    → SAME behavior, DIFFERENT mode → DIFFERENT outcome

  ③ GOTTMAN & DECLAIRE 2001 — BIDS FOR CONNECTION:
    Partners continuously make "bids" (requests for attention/connection)
    "Turning toward" (respond to bid) → relationship THRIVES
    "Turning away" (ignore bid) → relationship DETERIORATES

    Framework mapping:
      Bid = mild C expression:
        "I want to connect → I reach out / I ask"
      Partner responds → calibration signal → adjust
      ZERO bids = ZERO interaction = bond DIES

    → Mild entity-access expression = NECESSARY for bond maintenance
    → ZERO entity-access = relationship death
        (no bids → no interaction → Entity-Compiled decay)

  ENTITY-ACCESS SPECTRUM REFINED:

    ┌─────────────┬──────────────────────────┬─────────────────┬─────────────────────┐
    │ Level       │ Behavior                 │ Gap Source      │ Entity Autonomy     │
    ├─────────────┼──────────────────────────┼─────────────────┼─────────────────────┤
    │ UNDER       │ No bids, no interaction. │ Suppress all    │ "Intact" but        │
    │             │ "Everyone for themselves"│                 │ NEGLECTED (no bond) │
    ├─────────────┼──────────────────────────┼─────────────────┼─────────────────────┤
    │ MILD        │ Calls to check in; if    │ A+B dominant    │ INTACT              │
    │             │ friend is busy, accepts  │                 │ (entity says no →   │
    │             │ it easily                │                 │ accepted)           │
    ├─────────────┼──────────────────────────┼─────────────────┼─────────────────────┤
    │ MODERATE    │ Offers soup; if child    │ A+B + justified │ INTACT              │
    │             │ doesn't want it, makes   │ C               │ (adjusts to entity) │
    │             │ something else           │                 │                     │
    ├─────────────┼──────────────────────────┼─────────────────┼─────────────────────┤
    │ JUSTIFIED   │ Making child take        │ Justified C     │ Temporarily         │
    │ OVERRIDE    │ medicine (child cannot   │ (entity cannot  │ OVERRIDDEN for      │
    │             │ self-determine yet)      │ self-process)   │ entity's benefit    │
    │             │ + explain + empathy      │                 │                     │
    ├─────────────┼──────────────────────────┼─────────────────┼─────────────────────┤
    │ EXCESSIVE   │ Forcing food when child  │ C dominant      │ VIOLATED            │
    │ (Level 5)   │ is full: "'eat more!'"   │ (my anxiety)    │ (entity's "no"      │
    │             │ ignores child's signal   │                 │ ignored)            │
    ├─────────────┼──────────────────────────┼─────────────────┼─────────────────────┤
    │ EXTREME     │ "'The child MUST study   │ C+D dominant    │ SUPPRESSED          │
    │ (Level 5+)  │ medicine'" — monitor,    │ (my gap +       │ (entity's drive     │
    │             │ punish                   │ schema override)│ replaced by mine)   │
    └─────────────┴──────────────────────────┴─────────────────┴─────────────────────┘

  ⭐ JUSTIFIED OVERRIDE vs EXCESSIVE:
    Boundary: can the child's body ADEQUATELY self-process already?
    (Entity-Access.md §5.3)

    CANNOT self-process → C justified (medicine, safety, basic hygiene)
    CAN self-process → C problematic
      (career choice, friend choice, food preference)

    Lifecycle: justified C GRADUALLY DECREASES as entity develops
    Skilled parent: shifts C→B in step with entity's development
      (→ Compilable-dominant destination)
    Parent who gets STUCK: C stays high even when entity is capable →
      excess (Level 5)

  🟢 Authoritative parenting: Baumrind 1966, 1991 (R1)
  🟢 Structure + autonomy support: Deci & Ryan 2000 (R2)
  🟢 Bids for connection: Gottman & DeClaire 2001 (R3)
  🟡 Optimal Zone ≠ Zero C = framework synthesis
```

---

## §8 — PER BOND TYPE CALIBRATION DYNAMICS

```
⭐⭐ EACH BOND TYPE HAS ITS OWN CALIBRATION DYNAMICS:

  CLOSE FRIENDS (Level 3) — SELF-CALIBRATING:
    Gap source: B dominant (by-product resonance)
    Exit cost: LOW → friend's "no" = effective signal
    Hardware-subsidy: ZERO → no bias, clear signal
    Entity-access: naturally in Goldilocks (environment corrects)
    Calibration needed: MINIMAL (external mechanism sufficient)

    Example: invite a friend for coffee; friend is busy →
      "'ok, some other time'"
    → Mild C expressed → entity responded → accepted → Goldilocks
    → If you insist → friend annoyed → signal CLEAR →
        adjust or lose friend

  ROMANTIC (Level 4) — BIDIRECTIONAL CALIBRATION:
    Gap source: A (hormone, temporary) + B (resonance) + C variable + D variable
    Exit cost: MODERATE → partner's "no" = moderate signal
    Hardware-subsidy: TEMPORARY (limerence) → fades → clearer calibration
    Entity-access: needs ACTIVE calibration from BOTH sides

    Gottman insight: BOTH partners make bids + BOTH respond →
      mutual calibration
    → Relationship health = f(bid → response ratio)
        (Gottman: 5:1 positive:negative)

    Demand-Withdraw pattern (Christensen & Heavey 1990):
      When bids escalate → demands → partner WITHDRAWS →
        demands ↑ → LOOP
      = Entity-access excess from one side → partner's feedback = withdrawal
      = Calibration signal EXISTS but IGNORED (escalation override)

    Healthy romantic: a gentle bid → partner responds →
      mutual Entity-Compiled ↑
    → Boundary: partner CAN say "'not now'" → ACCEPTED → calibrated

  PARENT→CHILD (Level 4-5) — INTERNAL CALIBRATION ONLY:
    Gap source: A+B+C+D compound (Entity-Access.md §5.2)
    Exit cost: VERY HIGH (child cannot leave)
    Hardware-subsidy: MAXIMUM (hormone bias → C masked)
    Entity-access: needs MOST calibration but has LEAST external correction

    TRIPLE CHALLENGE:
      ① Exit cost max → entity's "no" = weak signal (child cannot leave)
      ② Hardware-subsidy max → C masked as A
          (hormone provides cover story)
      ③ Power max → CAN override entity → excess persists without correction
      → 3 factors ALL conspire against calibration
      → ONLY Self-Awareness (Axis 2) + sufficient PFC resource (Axis 4) can help

    BUT ALSO: Parent→Child = MOST PRACTICE opportunity
      → Daily interaction = constant calibration opportunities
      → IF curiosity mode → each day = micro-adjustment → gradual improvement
      → = Mentalization in practice: daily life AS training ground (Fonagy 2002)

  PROFESSIONAL (Level 2-3) — STRUCTURED CALIBRATION:
    Gap source: D dominant (obligation, contract)
    Exit cost: MODERATE (career consequences)
    Hardware-subsidy: ZERO
    Entity-access: LOW (mostly Compiled Tool-mode)
    Calibration: EXTERNAL structures (HR, norms, contracts) → prescribed

    Example: employer's entity-access toward employee
    → Overtime demands = C (employer's gap filled through employee's time)
    → Labor law = external calibration mechanism (prescribes limits)

  🟡 Per bond type calibration dynamics = framework synthesis
  🟢 Demand-Withdraw: Christensen & Heavey 1990 (R4)
  🟢 Bid-response ratio: Gottman & DeClaire 2001 (R3)
  🟢 Mentalization training: Fonagy 2002 (R5)
```

---

## §9 — 5 CALIBRATION FAILURE MODES

```
⭐⭐ 5 FAILURE MODES — DIFFERENT SOURCE, DIFFERENT FIX:

  MODE 1 — BLIND (Layer 1 fail):
    Cannot detect own gap source → entity-access feels "all genuine"
    Source: low interoceptive accuracy, alexithymia, habituated signals
    Looks like: "'but I genuinely love them!'"
      (PFC cannot receive C beneath A)
    Fix: interoception training, body awareness practice,
      Focusing (Gendlin 1978)
    Timeline: months (body-readout skill, trainable — Fukushima 2011)

  MODE 2 — TOOL-MODE (Layer 2 fail):
    Compiled = Tool → cannot model entity's internal state →
      acts without predicting impact
    Source: Compiled never developed for this entity, or degraded by depletion
    Looks like: "'has the child eaten?'" (function check, not
      "'what is the child feeling?'")
    Fix: Agent-mode practice, deliberate curiosity about entity's state
    Timeline: weeks-months (Compiled shift, requires sustained Fresh practice)

  MODE 3 — OVERRIDE (Layer 3 fail):
    Entity responds but compiled pattern fires → feedback NOT integrated
    Source: deeply compiled entity-access behaviors,
      anxiety-compiled chains
    Looks like: child says "'no'" → parent: "'eat more!'"
      (automatic, no pause)
    Fix: decompile (Compiled-Fresh.md §9), therapy, sustained new practice
    Timeline: months-years (decompile + recompile is SLOW)

  MODE 4 — DEPLETED (Cascading fail):
    PFC resource gone → all 3 layers drop → auto-pilot
    Source: work stress, sleep deprivation, burnout, chronic load
    Looks like: "'home in the evening = exhausted → compiled →
      force → guilt → more stress'"
    Fix: resource restoration (sleep, support, reduce load)
    Timeline: days-weeks (if temporary), months (if chronic burnout)
    → = Mikolajczak 2019: burnout intervention = restore resource first

  MODE 5 — THREAT-MODE (Engine quality fail):
    Calibration ATTEMPTED with threat cortisol → rumination → worse
    Source: parenting guilt, "'am I controlling?'" anxiety, perfectionism
    Looks like: "'am I a bad parent?'" → freeze OR overcompensate
    Fix: mode switch (threat → curiosity), normalize imperfection
    Timeline: variable (mode switch can be fast IF recognized)
    → = Most FIXABLE failure mode (just change HOW you observe, not WHAT)

  COMPOUND FAILURE (most common in reality):
    Modes combine: depleted (M4) → blind (M1) + tool-mode (M2) +
      override (M3)
    = 4-Axis cascading (Entity-Access.md §9):
      Axis 4 depleted → Axis 1 DROP → Axis 2 DROP → Axis 3 shifts C → FORCES
    Fix: must address RESOURCE first (M4); then other modes become accessible

  🟡 5 failure modes taxonomy = framework synthesis
  🟢 Burnout intervention: Mikolajczak et al. 2019 (R10)
  🟢 Interoception training: Fukushima 2011 (R14), Gendlin 1978 (R15)
```

---

## §10 — CANNOT PRESCRIBE

```
⭐⭐ ENTITY-ACCESS CALIBRATION = CANNOT PRESCRIBE:

  Logic-Feeling-Balance.md §6-7:
    → Attempt to prescribe → every rule has a blind spot
    → Attempt meta-rule → meta-rule also has a blind spot
    → = Infinite regress → NO stopping point

  Applied to entity-access:
    Attempt to prescribe "entity-access should be at level X for bond type Y"
    → Fails because:
      ① Different person → different threshold
          (hardware, temperament, history)
      ② Different entity → different need
          (infant vs teen vs adult vs partner)
      ③ Different context → different capacity
          (rested vs depleted)
      ④ Different time → different stage
          (limerence vs 20 years)
      → 4 dimensions ALL dynamic → fixed formula IMPOSSIBLE

  AND THIS IS NORMAL (Reward-Calibration.md §5.3):
    IF entity-access calibration COULD be perfectly prescribed:
      → No need to observe entity's response
      → No need to adjust behavior
      → No need for relationship (= automaton)
      → No need to LIVE through experience
    = Perfect prescription = omniscience
    = Dynamic calibration = CORRECT, NORMAL, EXPECTED

  WHAT THIS FILE OFFERS (without prescribing):
    → IDENTIFY: which of the 3 Layers is failing? (§2)
    → UNDERSTAND: why is this bond type harder to calibrate? (§3, §4, §8)
    → IDENTIFY: which mode is running — curiosity or threat? (§6)
    → IDENTIFY: which zone — under/Goldilocks/over? (§7)
    → AVOID: which failure mode is currently active? (§9)
    → = DESCRIBE, NOT prescribe (Logic-Feeling-Balance.md §8.1)

  🟡 Cannot prescribe applied to entity-access = framework synthesis
  🟢 Infinite regress: Logic-Feeling-Balance.md §6-7
  🟢 Domain feedback = only arbiter: Reward-Calibration.md §5.2
```

---

## §11 — TRAINING + VIRTUOUS/VICIOUS SPIRAL

```
⭐⭐ CALIBRATION = TRAINABLE SKILL → COMPOUND IMPROVEMENT:

  Simulation-Engine.md §11: training 1 component → N applications improve.
  Entity-access calibration = SPECIFIC application of same principle.

  TRAINING TARGETS:

    ① INTEROCEPTION (Layer 1):
      Body-scan meditation, Focusing (Gendlin 1978)
      → Better body-readout → detect gap source earlier
      → "'I am anxious'" detectable BEFORE behavior fires
      → 🟢 Fukushima 2011: interoceptive accuracy → empathic accuracy

    ② Compiled DEPTH (Layer 2):
      Deliberate curiosity: "'what is the entity actually feeling?'"
      → Practice Agent-mode (model internal state, not just behavior)
      → More diverse interaction → sharper models (Mitchell 2006)
      → 🟢 Fonagy 2002: mentalization training improves relationship quality

    ③ REFLECTION PRACTICE (Engine use quality):
      Cultivate curiosity orientation (Trapnell & Campbell 1999):
      → Replace "'I was wrong'" with "'why do I feel this way?'"
      → = Switch cortisol direction: threat → novelty
      → 🟢 Joireman et al. 2002: self-reflection → empathy correlation

    ④ DECOMPILE + RECOMPILE (Layer 3):
      Therapy (MBT: Bateman & Fonagy 2006)
      → Decompile old compiled patterns → recompile with better tags
      → Timeline: months-years
      → BUT: daily practice compounds (small shifts → gradual recompile)

  VIRTUOUS SPIRAL:
    Calibrate well → better outcome (entity thrives + bond strong)
    → Confirms approach → curiosity about more nuances
    → Calibrate better → even better outcomes → ...
    → = Entity-access calibration becomes MASTERY domain
    → = Generative gap: "'understanding a little more each day'"
        → novelty reward
    → = Self-reinforcing loop (Lopes, Salovey & Straus 2003)

  VICIOUS SPIRAL:
    Calibrate poorly → bad outcome (entity suffers or drifts)
    → Self-blame (threat mode) → worse calibration
    → OR denial (blind mode) → no adjustment → ...
    → Break point: external intervention
        (therapy, trusted feedback, crisis event)

  SOCIAL BASELINE EFFECT (Coan & Sbarra 2015):
    Brain OUTSOURCES emotion regulation to trusted others
    → Partner hand-holding → LESS threat neural activity
    → More trusted contacts → MORE PFC budget available →
        better calibration
    → = Social support ↑ → Axis 4 ↑ → calibration capacity ↑
    → Isolation → Axis 4 depleted → calibration capacity ↓

  🟢 Interoception training: Fukushima 2011 (R14), Gendlin 1978 (R15)
  🟢 Mentalization training: Fonagy 2002 (R5), Bateman & Fonagy 2006 (R6)
  🟢 Reflection practice: Trapnell & Campbell 1999 (R7)
  🟢 Emotion regulation ↔ social: Lopes, Salovey & Straus 2003 (R11)
  🟢 Social Baseline Theory: Coan & Sbarra 2015 (R9)
```

---

## §12 — CALIBRATION × ENTITY-ACCESS GRADIENT

```
⭐⭐⭐ CALIBRATION DIFFICULTY SCALES WITH ENTITY-ACCESS LEVEL (★ KEY):

  CORE INSIGHT:
    Calibration mechanism DIFFERS per Level on Entity-Access Gradient
    Higher Level = MORE entity-access depth = HARDER to calibrate
    Lower Level = LESS depth = self-correcting OR irrelevant

  ┌──────────┬──────────────┬──────────────┬───────────────────────────────────┐
  │ Level    │ Calibration  │ Primary      │ Why                               │
  │          │ difficulty   │ mechanism    │                                   │
  ├──────────┼──────────────┼──────────────┼───────────────────────────────────┤
  │ 0a-0b    │ N/A          │ N/A          │ No entity-access → nothing        │
  │ (service)│              │              │ to calibrate                      │
  ├──────────┼──────────────┼──────────────┼───────────────────────────────────┤
  │ 0c       │ TRIVIAL      │ Context      │ Tool-mode toward individual, no   │
  │ (tool)   │              │              │ state modeling → no C             │
  ├──────────┼──────────────┼──────────────┼───────────────────────────────────┤
  │ Level 1-2│ LOW          │ NATURAL      │ Shallow compile → easy to let go. │
  │ (unlabel)│              │ DRIFT        │ No hardware bias. Entity-Compiled │
  │          │              │              │ weak. "'barista switches cafes'"  │
  │          │              │              │ = natural                         │
  ├──────────┼──────────────┼──────────────┼───────────────────────────────────┤
  │ Level 3  │ LOW-MOD      │ EXTERNAL     │ Exit easy → friend's "no" =       │
  │ (friend) │              │ (exit cost)  │ strong signal → self-corrects     │
  │          │              │              │ Hardware=0 → no bias → C visible  │
  ├──────────┼──────────────┼──────────────┼───────────────────────────────────┤
  │ Level 4  │ HIGH         │ INTERNAL     │ Exit cost ↑ + hardware-subsidy →  │
  │ (Entity- │              │ (self-       │ C MASKED. PFC: "part of my life"  │
  │ Owned)   │              │ awareness +  │ → rationalizes. Needs 3-Layer     │
  │          │              │ Axis 2)      │ actively.                         │
  ├──────────┼──────────────┼──────────────┼───────────────────────────────────┤
  │ Level 5  │ MAXIMUM      │ EXTERNAL     │ By definition: calibration is     │
  │ (Excess) │              │ INTERVENTION │ ALREADY FAILING → that's WHY      │
  │          │              │ (therapy,    │ Level 5. Internal mechanisms      │
  │          │              │ crisis)      │ exhausted or compiled-overridden. │
  └──────────┴──────────────┴──────────────┴───────────────────────────────────┘

  ⭐ KEY OBSERVATIONS:

    Level 1-3: SELF-CORRECTING
      → Exit cost low → environment provides calibration signals
      → Hardware-subsidy = zero or low → C/D visible → easy to detect
      → 3-Layer Architecture = useful but not CRITICAL
      → "'barista is too familiar → switch cafes'" = natural calibration
          at Level 1
      → "'friend controls too much → friend exits'" = natural
          calibration at Level 3

    Level 4: CRITICAL ZONE
      → Exit cost rising → entity's "no" = weakening signal
      → Hardware-subsidy present → C masked as A → hard to detect
      → 3-Layer Architecture = ESSENTIAL
      → Self-Awareness (Axis 2) = THE DIFFERENCE MAKER
      → This is WHERE calibration matters most AND is hardest
      → = WHY this file focuses on Level 4 dynamics
          (parenting, romantic)

    Level 5: CALIBRATION ALREADY FAILED
      → Person AT Level 5 = calibration mechanisms already overwhelmed
      → Internal observation insufficient → needs EXTERNAL input
      → Therapy, crisis event, trusted friend's honest feedback
      → = Entity-Access-Excess.md §10: fix spectrum

  ⭐ PARENTING LIFECYCLE × CALIBRATION:
    Young Child (0-6) — Level 4-5 entity-access for parent:
      → Child = highest entity-access depth → hardest to calibrate
      → Child's own calibration = N/A (does not understand mechanism)
      → Parent ALONE must calibrate → Internal ONLY → Axis 2 critical

    Older Child (12-18) — Level 4 ↓, child begins own calibration:
      → Teen rebellion = child's FIRST calibration attempts
      → "'I hate you'" = child testing: "can I say no?" = exit signal FORMING
      → Parent who RECEIVES this signal → recalibrates → healthy
      → Parent who OVERRIDES → signal weight stays low → excess persists

    Adult Child (18+) — Level 3-4, external calibration RETURNS:
      → Adult child CAN exit → signal weight ↑
      → "'I'm busy'" = effective calibration signal
      → Parent→Adult Child dynamics SHIFT toward friendship (Level 3)
      → = Compilable-dominant destination (Entity-Access.md §3.2+§3.3):
          C→B trajectory

  🟡 Calibration × Level gradient = framework synthesis
  🟡 Level 4 = critical calibration zone = framework synthesis
  🟡 Teen rebellion as calibration signal = framework synthesis
```

---

## §13 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 RESEARCH-GROUNDED (established)
═══════════════════════════════════════

  Baumrind parenting styles (1966, 1991) — ~60 years of research
  Self-Determination Theory (Deci & Ryan 2000) — ~45 years
  Gottman bids for connection (2001) — ~25 years longitudinal
  Demand-withdraw pattern (Christensen & Heavey 1990) — replicated
  Reflection vs rumination (Trapnell & Campbell 1999) — established
  Mentalization (Fonagy 2002) — clinical evidence base
  Social Baseline Theory (Coan & Sbarra 2015) — neural evidence
  Parental burnout (Mikolajczak 2019) — replicated cross-culturally
  Interoception → empathy (Fukushima 2011) — established
  Parental investment theory (Trivers 1972) — foundational

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (novel combinations)
═══════════════════════════════════════

  3-Layer Calibration Architecture
    (maps to Simulation-Engine, novel application)
  Exit Cost = Signal Weight
    (novel framing of established dynamics)
  Hardware-Subsidy = Calibration Bias
    (novel angle on known hormone effects)
  Cannot prescribe applied to entity-access
    (parallel from Reward-Calibration)
  Calibration as Generative reward source
    (novel extension)
  5 failure modes taxonomy
    (novel organization of known phenomena)
  Calibration × Entity-Access Gradient per-Level analysis
  Level 4 = critical calibration zone
  Teen rebellion as calibration signal

═══════════════════════════════════════
🔴 HYPOTHESIS (testable but unverified)
═══════════════════════════════════════

  Exact mapping of 3 calibration layers to Simulation-Engine components
    (conceptually clean but neural correspondence not directly demonstrated)
  "Calibration as Generative reward" — mechanism plausible
    but no direct study
  "Parenting advice as threat trigger" — anecdotally common,
    no formal study
  Calibration difficulty × Level quantification
    (no empirical measure yet)

WHAT THE FRAMEWORK ADDS vs WHAT ALREADY EXISTED:
  WHAT RESEARCH ALREADY KNEW: authoritative parenting = best, mentalization
    trainable, burnout hurts parenting, bids maintain bonds.
  WHAT THE FRAMEWORK ADDS: unifying model explaining WHY (3-layer +
    exit cost + hardware bias + per-Level analysis), connecting to the
    broader architecture.
  = Organizing principle, not new discovery.
```

---

## §14 — CROSS-REFERENCES

| File | Sections | Relationship |
|------|----------|-------------|
| Entity-Access.md v1.1 | §1-§3, §5, §8-§9 | PREREQUISITE: entity-access definition + 3-Factor + gradient |
| Entity-Access-Excess.md v1.0 | §1-§10 | COMPANION: excess (Level 5) — this file covers calibration |
| Entity-Compiled.md v1.0 | §1-§8 | FOUNDATION: brain compiles agent into body-base |
| Compiled-Fresh.md v2.0 | §6, §9, §10 | FOUNDATION: compiled quality + PFC budget + reversal |
| Simulation-Engine.md v1.0 | §1, §9, §11 | FOUNDATION: 3 components + reflection/rumination + training |
| PFC-Operations.md v1.0 | §1-§7 | FOUNDATION: Hold/Suppress, Compiled/Fresh, PFC universal |
| Self-Pattern-Modeling.md v3.1 | §0-§3 | FOUNDATION: Self-Pattern-Modeling as Simulation-Engine application |
| Reward-Calibration.md v1.1 | §1, §5 | PARALLEL: general reward calibration principle |
| Logic-Feeling-Balance.md v1.0 | §6-§7 | PARALLEL: cannot prescribe + infinite regress |
| Connection.md v4.0 | §9 | COMPANION: 2-body calibration dynamic equilibrium |
| Social-Calibration.md v1.1 | §2.5 | COMPANION: social system calibration (CHECK function) |
| Empathy.md v2.2 | §5 | DOWNSTREAM: burnout as calibration failure |
| Autonomy-Hardware.md v1.1 | §2 | FOUNDATION: vmPFC + DRN → autonomy violation detection |
| Self-Created-Threat.md v1.0 | §3 | DOWNSTREAM: threat-mode calibration failure |
| AI-Self-Model.md v2.0 | §4, §5 | DOWNSTREAM: Dual Check as calibration mechanism |
| Ask-AI.md v3.1 | §6 | DOWNSTREAM: body as quality controller = Layer 1 calibration |
| Education-Mechanism.md v1.0 | §3 | DOWNSTREAM: bridge reward calibration |
| Gap-Distribution-Profile.md v1.0 | §8 | COMPANION: portfolio risk, diversification |

---

## §15 — RESEARCH CITATIONS

| # | Citation | Used in | Evidence |
|---|----------|---------|----------|
| R1 | Baumrind 1966, 1991 — Parenting styles: Authoritative/Authoritarian/Permissive/Neglectful. Authoritative = best outcomes. | §7 | 🟢 |
| R2 | Deci & Ryan 2000 — Self-Determination Theory. Autonomy support + structure = optimal. | §3, §7 | 🟢 |
| R3 | Gottman & DeClaire 2001 — Bids for connection. Turning toward vs turning away. Bid-response ratio predicts outcomes. | §7, §8 | 🟢 |
| R4 | Christensen & Heavey 1990 — Demand-Withdraw interaction pattern. Escalation cycle. | §8 | 🟢 |
| R5 | Fonagy 2002 — Mentalization: capacity to understand behavior in terms of mental states. Trainable. | §6, §8, §11 | 🟢 |
| R6 | Bateman & Fonagy 2006 — Mentalization-Based Therapy (MBT). Clinical evidence for training. | §5, §11 | 🟢 |
| R7 | Trapnell & Campbell 1999 — Self-Reflection vs Self-Rumination. 2 dispositions, opposite correlates. | §6, §11 | 🟢 |
| R8 | Joireman, Parrott & Hammersla 2002 — Self-reflection → positive empathy correlation. | §6, §11 | 🟢 |
| R9 | Coan & Sbarra 2015 — Social Baseline Theory. Brain outsources emotion regulation. Neural evidence. | §11 | 🟢 |
| R10 | Mikolajczak et al. 2019 — Parental burnout: depleted → overcontrol OR emotional distance. Cross-cultural. | §5, §9 | 🟢 |
| R11 | Lopes, Salovey & Straus 2003 — Emotion regulation ↔ social interactions. Bidirectional. | §11 | 🟢 |
| R12 | Koudenburg et al. 2024 — Social interaction → self-concept clarity. "Sense of me" through "sense of we." | §11 | 🟢 |
| R13 | McNulty et al. 2013 — Implicit vs explicit partner attitudes. PFC rationalization. Science. | §1 | 🟢 |
| R14 | Fukushima et al. 2011 — Interoceptive accuracy → empathic accuracy correlation. Trainable. | §2, §9, §11 | 🟢 |
| R15 | Gendlin 1978 — Focusing. Body-felt sense awareness technique. | §9, §11 | 🟢 |
| R16 | Trivers 1972 — Parental investment theory. Highest investment → highest bias. | §4 | 🟢 |
| R17 | Feldman 2012 — Bio-behavioral synchrony. Oxytocin × parent-child. | §4 | 🟢 |
| R18 | Strathearn et al. 2009 — Maternal brain reward: own infant face. | §4 | 🟢 |
| R19 | Fraley & Shaver 1998 — Avoidant suppress but physiology elevated. Attachment change possible but slow. | §5 | 🟢 |
| R20 | Zeki & Romaya 2008 — Hate vs Love circuits. Shared: putamen + insula. Hate retains judgment. | §8 | 🟢 |
| R21 | Maccoby 1992 — Power asymmetry in parent-child relationships. | §3 | 🟢 |
| R22 | Hall 2018 — Friendship formation: 40-60h casual → 200+h close. | §8 | 🟢 |
| R23 | Segrin et al. 2013 — Parental anxiety → overparenting, not child need. | §9 | 🟢 |
| R24 | Soenens et al. 2015 — Self-worth contingency → psychological control. | §9 | 🟢 |
| R25 | Mitchell 2006 — Diverse interaction → sharper mental models. | §11 | 🟢 |

---

**END OF FILE — Entity-Access-Calibration v1.0 (25 citations, 15 sections)**
**Source: Drill-Entity-Access-Calibration v2.0**
