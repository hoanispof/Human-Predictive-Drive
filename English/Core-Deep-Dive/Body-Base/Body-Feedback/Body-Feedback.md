---
title: Body-Feedback — Synthesis of Body Signal Architecture
version: 3.1
created: 2026-04-15 (N+3, drill P0-P5)
refined: 2026-04-20 (v1.1 — add Mechanism file, cleanup refs)
rewritten: 2026-05-17 (v2.0 — folder rebuild complete, +3 files, Compilable Architecture, updated reading guide)
refined: 2026-05-17 (v2.0a — Why-Body-Knows v1.1 ref: 4-tier → 2-layer calibration)
rewritten: 2026-05-24 (v3.0 — FULL REWRITE: 14 files/~23,900L, +pipeline visualization, +Gap System, +Quality/Calibration, trimmed cases, all versions updated)
refined: 2026-05-25 (v3.1 — +Dissonance-Signal-Architecture.md v1.0 integration, +Drill-Evolutionary-Sensor-Architecture.md v1.0, 14→16 files, versions updated: Body-Feedback-Mechanism v2.1, Body-Feedback-Label v2.1, Reward-Signal-Architecture v2.1)
source_version: Vietnamese v3.1
english_created: 2026-06-06
status: SYNTHESIS v3.1
scope: |
  Unified model of body signal generation (dissonance + reward + neutral).
  Entry point for Body-Feedback/ folder (17 files, ~27,500L).
  Synthesizes folder into single reference + reading guide.
  v3.0: Folder expanded from 10→14 files.
  +Gap-Body-Need v1.0, +Gap-Distribution-Profile v1.1, +Action-Space v1.0, +Hidden-Quality-Perception v1.0.
  +Full 6-layer pipeline visualization (hardware → PFC + inter-body).
  +Gap System section (direction + 3 satiation + distribution + behavioral prediction).
  +Quality + Calibration section (reward calibration + hidden quality).
  +Trimmed case details (~200L → ~60L pointers to drill files).
  +All external cross-ref versions updated.
  v3.1: +Dissonance-Signal-Architecture.md v1.0, +Drill-Evolutionary-Sensor-Architecture.md v1.0.
  +Reading guide Tier 2 updated. +Pipeline Layer 3 updated.
  +Unique contributions: Dissonance-Signal-Architecture. +Versions: Body-Feedback-Mechanism v2.1, Body-Feedback-Label v2.1, Reward-Signal-Architecture v2.1.
purpose: |
  WHY and HOW body generates affective signals.
  5 Body-Feedback-Preconditions for body signals.
  Chunk dynamics classification (4th axis).
  Gap system (direction + dynamics + distribution + supply-side).
  Quality perception + reward calibration.
  Unique contributions not absorbed elsewhere.
  READING GUIDE for navigating 16-file, ~26,100L folder.
parent: Body-Base/
dependencies: |
  Body-Feedback-Mechanism.md v2.1 (chunk dynamics, 2-source, Body-Need, compound)
  Body-Feedback-Label.md v2.1 (vocabulary reference, 3-tier labels, ALL new terms)
  Gap-Direction.md v2.0 (gap has direction, 2-layer, by-product match)
  Gap-Body-Need.md v1.0 (3 Satiation Profiles, 5-Parameter, ENGINE/ROAD/VEHICLE)
  Gap-Distribution-Profile.md v1.1 (per-person gap landscape, 4 axes, 4 layers)
  Reward-Signal-Architecture.md v2.1 (Evaluative/Direct-State, 5 Profiles, Evaluative Gates Direct-State)
  Dissonance-Signal-Architecture.md v1.0 (Evaluative/Direct-State Dissonance, Mismatch Splitting, Clinical)
  Reward-Calibration.md v1.1 (Goldilocks per-gap, 6 mechanisms, dynamic equilibrium)
  Action-Space.md v1.0 (supply-side, 4 axes, Gap-Distribution × Action-Space)
  Hidden-Quality-Perception.md v1.0 (compilation depth → quality visibility, 2 types)
  Drill-Evolutionary-Sensor-Architecture.md v1.0 (first-principles WHY body-feedback architecture)
  Drill-Body-Feedback/01-Foundation.md (dual-pull, interface loop, body-feedback vs feeling)
  Drill-Body-Feedback/02-Dissonance.md (3 Genuine Discomfort Sources, threat matrix, trauma loop, hedonic trap)
  Drill-Body-Feedback/03-Reward.md (VTA + opioid, Body-Feedback-Preconditions, car paradox, Van Gogh)
  Drill-Body-Feedback/04-Integration.md (unified loop, case walkthroughs, Body-Feedback-Precondition v3, recommendations)
  Inter-Body-Mechanism.md v2.0 (Compilable Architecture, Compiled/Fresh, domain arbiter)
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback — Synthesis of Body Signal Architecture

> **This file is the ENTRY POINT** for the Body-Feedback/ folder.
> 17 files, ~27,500L: Mechanism + Gap System + Signal Architecture +
> Aggregate Observation + Case Analyses + Drills.
>
> **Read this file FIRST**. Go deeper into individual files as needed.
>
> **Core claims:**
> 1. Body signal = function of 5 Body-Feedback-Preconditions on interface loop
> 2. Body-feedback arises from 2 input sources × 3 chunk dynamics → Body-Need
> 3. Reward has 2 types (Evaluative / Direct-State) × 5 profiles × interaction model
> 4. Gap has DIRECTION + 3 SATIATION PROFILES + per-person DISTRIBUTION
> 5. Behavior = f(Gap-Distribution DEMAND × Action-Space SUPPLY)

---

## Table of Contents

- §1 — Folder Overview + Reading Guide
- §2 — ⭐ Full Pipeline Visualization (6 layers)
- §3 — Dual-Pull + Interface Loop + 3 Genuine Discomfort Sources
- §4 — Signal Generation + Body-Need
- §5 — Signal Architecture + Body-Feedback-Precondition
- §6 — ⭐ Gap System (direction + satiation + distribution + supply)
- §7 — ⭐ Quality + Calibration
- §8 — Case Analyses + Special Mechanisms (pointers)
- §9 — Absorbed Content Map
- §10 — Honest Assessment + Cross-References

---

## §1 — Folder Overview + Reading Guide

### §1.1 — Files in this folder (v3.1 updated)

```
Body-Feedback/
│
├── Body-Feedback.md             ← THIS FILE (entry point, synthesis)
│
├── VOCABULARY:
│   └── Body-Feedback-Label.md   (1,119L) — ⭐ VOCABULARY REFERENCE v2.1
│         3-tier labels, ALL framework terms formalized
│
├── MECHANISM:
│   └── Body-Feedback-Mechanism.md (1,519L) — ⭐ MECHANISM v2.1
│         2-source model, Body-Need aggregate, 3 chunk dynamics, compound
│
├── PRECONDITION:
│   └── Body-Feedback-Precondition.md (1,420L) — ⭐ PRECONDITION v1.0
│         5 preconditions for signal fire (Directed-Gap, Chunk-Substrate,
│         Delta-Gate, Match-Range, Compile-Gate), conjunction logic,
│         developmental arc, dissonance application
│
├── GAP SYSTEM:
│   ├── Gap-Direction.md         (2,681L) — ⭐ GAP DIRECTION v2.0
│   │     Gap has direction = f(surrounding chunks), 2-layer model,
│   │     by-product match, "unknown = no gap"
│   ├── Gap-Body-Need.md         (1,388L) — GAP DYNAMICS v1.0
│   │     3 Satiation Profiles (Cyclic/Tonic/Generative),
│   │     5-Parameter per-gap model, ENGINE/ROAD/VEHICLE architecture
│   └── Gap-Distribution-Profile.md (2,370L) — GAP LANDSCAPE v1.1
│         Per-person gap aggregate, 4 axes, 4-layer formation,
│         resonance prediction
│
├── SIGNAL ARCHITECTURE:
│   ├── Reward-Signal-Architecture.md (1,987L) — ⭐ REWARD TYPES v2.1
│   │     Evaluative/Direct-State distinction, E₀→E₃ gradient,
│   │     Evaluative Gates Direct-State, 5 Reward Profiles
│   ├── Dissonance-Signal-Architecture.md (1,571L) — ⭐ DISSONANCE TYPES v1.0
│   │     Evaluative/Direct-State Dissonance, E₀→E₃ applied,
│   │     Mismatch Splitting, Placebo/Nocebo proof, Clinical implications,
│   │     Asymmetric Transition Speed, Numbness-Proof
│   └── Reward-Calibration.md    (1,356L) — CALIBRATION v1.1
│         Goldilocks per-gap, 6 over-reward mechanisms,
│         dynamic equilibrium
│
├── AGGREGATE OBSERVATION:
│   ├── Action-Space.md          (1,729L) — SUPPLY SIDE v1.0
│   │     4 axes (Compiled Capacity × Resource Access × Freedom × Awareness),
│   │     Gap-Distribution × Action-Space = behavioral prediction
│   └── Hidden-Quality-Perception.md (1,738L) — QUALITY VISIBILITY v1.0
│         "Unknown = no gap" × quality, 2 types (Expert + Leader),
│         Dunning-Kruger = meta-level application
│
├── CASE ANALYSES + DRILLS:
│   ├── Drill-Evolutionary-Sensor-Architecture.md (636L) — DRILL v1.0
│   │     First-principles WHY: body-feedback architecture MUST be this way
│   └── Drill-Body-Feedback/
│       ├── 01-Foundation.md     (1,126L) — dual-pull, loop, architecture
│       ├── 02-Dissonance.md     (1,846L) — 3 sources, threat, trauma, hedonic
│       ├── 03-Reward.md         (2,280L) — VTA+opioid, Body-Feedback-Precondition, car paradox, Van Gogh
│       └── 04-Integration.md    (1,856L) — unified cycle, walkthroughs, Body-Feedback-Precondition v3
│
└── backup/                      (historical versions)

FOLDER TOTAL: 17 content files, ~26,100L
```

### §1.2 — Reading guide (4-tier navigation)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 1: VOCABULARY + ENTRY (~2,000L — read ALWAYS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① This file (Body-Feedback.md) — overview, pipeline, reading guide
  ② Body-Feedback-Label.md v2.1 — ⭐ MUST-READ VOCABULARY
     → 3-tier label system (General → Direction → Specific)
     → 100% framework vocabulary formalized
     → prediction-delta ≠ body-base reward (detection ≠ evaluation)
     → Body-feedback (mechanism) ≠ Feeling (PFC observation)
     → Entity-Compiled subtypes, Compiled/Fresh labels,
       By-product match/anti-match, 2-Stream, 3-cost, 5-Channel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 2: MECHANISM + ARCHITECTURE (~9,150L — read for UNDERSTANDING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ③ Body-Feedback-Mechanism.md v2.1 — HOW body creates signals
     → 2 input sources (Sensory-Driven / Pattern-Driven)
     → 3 chunk dynamics (Shift / Miss / Gap)
     → Body-Need = 2-source aggregate, 7 properties, 4 immediacy types
     → Compound mechanism + Quality Baseline Shift

  ③b Body-Feedback-Precondition.md v1.0 — WHEN signals fire
     → 5 preconditions: Directed-Gap × Chunk-Substrate × Delta-Gate × Match-Range × Compile-Gate
     → Conjunction logic: signal fires if and only if all 5 met
     → Evaluative vs Direct-State scope difference
     → Developmental arc + dissonance application

  ④ Gap-Direction.md v2.0 — WHY signals are personal
     → Gap direction = f(surrounding chunk network structure)
     → "Unknown = no gap" (foundational principle)
     → 2-layer model: signal mechanism × direction content
     → By-product match × gap direction, Compiled/Fresh connection

  ⑤ Reward-Signal-Architecture.md v2.1 — WHAT kinds of reward
     → Evaluative Reward (opioid) vs Direct-State Reward (non-opioid)
     → E₀→E₃ complexity gradient (compilation depth)
     → Evaluative Gates Direct-State (insula gradient, 4 outcomes)
     → 5 Reward Profiles, Temporal Stack, Conditional Interaction

  ⑤b Dissonance-Signal-Architecture.md v1.0 — WHAT kinds of dissonance
     → Evaluative Dissonance (compiled) vs Direct-State Dissonance (hardware)
     → E₀→E₃ applied to dissonance (same gradient, different direction)
     → Evaluative Gates Direct-State for dissonance (Placebo/Nocebo proof)
     → Mismatch Splitting: hardware vs compiled sub-types
     → Clinical: dissociation, alexithymia, anxiety, chronic pain
     → Asymmetric Transition Speed: reward→dissonance FAST, reverse SLOW

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 3: GAP DYNAMICS + OBSERVATION (~7,193L — read for DEPTH)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⑥ Gap-Body-Need.md v1.0 — HOW gaps consume + compete
     → 3 Satiation Profiles (Cyclic/Tonic/Generative)
     → 5-Parameter per-gap model (Source × Satiation × Reward × Chain × Dependency)
     → ENGINE/ROAD/VEHICLE architecture
     → Technology fill, entity-gap matching, gap lifecycle

  ⑦ Gap-Distribution-Profile.md v1.1 — WHERE gaps cluster per person
     → 4 axes (Domain Center × Origin Balance × Depth × Stability)
     → 4-layer formation (Collective → Schemas → Family → Hardware)
     → Resonance prediction: gap overlap → by-product match probability

  ⑧ Reward-Calibration.md v1.1 — HOW MUCH reward is enough
     → Goldilocks per-gap, per-person, per-context
     → 6 over-reward mechanisms
     → Dynamic equilibrium (CANNOT prescribe)

  ⑨ Action-Space.md v1.0 — WHAT options available per person
     → 4 axes (Compiled Capacity × Resource Access × Freedom × Awareness)
     → Gap-Distribution × Action-Space = behavioral prediction (4 quadrants)

  ⑩ Hidden-Quality-Perception.md v1.0 — WHY experts SEE differently
     → "Unknown = no gap" × quality visibility
     → 2 types: Domain Expert + Leader/Coordinator
     → Dunning-Kruger = meta-level application

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 4: CASES + DRILLS (~7,744L — read for SPECIFIC EXAMPLES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⑪ 01-Foundation.md — dual-pull principle, interface loop
  ⑫ 02-Dissonance.md — 15+ cases, 3 sources, trauma mechanism
  ⑬ 03-Reward.md — car paradox, Van Gogh gradient, C5 latency
  ⑭ 04-Integration.md — Einstein/hedonic/trauma walkthroughs, Body-Feedback-Precondition v3
  ⑮ Drill-Evolutionary-Sensor-Architecture.md — first-principles WHY:
     body-feedback system MUST be structured this way (bidirectional sensor impossibility)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ABSORBED ELSEWHERE (authoritative versions in other files):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  → Feeling-Mechanism-Deep-Draft.md §4 — reward mechanism (dopamine ≠ reward)
  → Feeling-Mechanism-Deep-Draft.md §3 — 8-step operational flow
  → Feeling-Chunk-Bridge-Draft.md §2  — body vote feedback mechanisms
```

### §1.3 — Compilable Architecture: WHY body-feedback system this complex

```
🟡 COMPILABLE ARCHITECTURE = WHY THIS FOLDER NEEDS ~26,100 LINES:

  Insects (Hardwired Architecture):
    Hardwired reward circuits: food→approach, pain→avoid.
    Body-feedback system = SIMPLE (few signals, few dynamics).

  Humans (Compilable Architecture — Inter-Body-Mechanism.md v2.0 §1):
    ① General-Purpose Reward — fires for ANY gap fill in the right direction
    ② Compilation — Hebbian: repeat + verify → automatic
    ③ Social Hardware — oxytocin, μ-opioid, dACC reuse

  → General-purpose = body CAN evaluate ANYTHING
  → Compilation = evaluation grows increasingly complex (E₀→E₃)
  → Social = body-feedback includes SOCIAL signals natively
  → Trade-off: 15-20 years of compilation → RICH signal architecture

  CONSEQUENCE for this folder:
    Mechanism:   2 sources × 3 dynamics (general-purpose creates variety)
    Gap System:  direction + satiation + distribution (compiled differently per person)
    Reward:      Evaluative/Direct-State + 5 Profiles (evaluation diversity)
    Calibration: Goldilocks (personal, dynamic)
    Supply:      Action-Space (options determine behavior)
    Quality:     Hidden perception (compilation depth → visibility)
    Cases:       01-04 (body-feedback OPERATES in domain reality)

  Without Compilable Architecture: folder = 2 files (pain/pleasure simple circuits).
  WITH Compilable Architecture: folder = 17 files, ~27,500L (complex adaptive system).

  Cross-ref: Inter-Body-Mechanism.md v2.0 §1 (Compilable Architecture full detail).
```

---

## §2 — ⭐ Full Pipeline Visualization (6 layers)

```
⭐⭐ BODY-FEEDBACK PIPELINE — FROM HARDWARE TO PFC + INTER-BODY:

  ┌─────────────────────────────────────────────────────────────────┐
  │  LAYER 1: HARDWARE FOUNDATION                                   │
  │                                                                 │
  │  3 foundations → Compilable Architecture:                       │
  │    ① General-Purpose Reward (fires for ANY gap fill)            │
  │    ② Compilation Capability (Hebbian → automatic evaluation)   │
  │    ③ Social Hardware (oxytocin, μ-opioid, dACC reuse)           │
  │                                                                 │
  │  See: Inter-Body-Mechanism.md v2.0 §1, Body-Base.md v3.3 §1    │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 2: SIGNAL GENERATION                                     │
  │                                                                 │
  │  2 sources:                                                     │
  │    ① Sensory-Driven (domain → body → chunks fire reactive)     │
  │    ② Pattern-Driven (chunks fire internally → body responds)   │
  │  × 3 dynamics:                                                  │
  │    ① Chunk-Shift (same chunks, DIFFERENT valence)               │
  │    ② Chunk-Miss (compiled pattern DOES NOT FIRE)                │
  │    ③ Chunk-Gap (network detects MISSING pattern)                │
  │  + Compound (1 event → multiple dynamics)                       │
  │  → Body-Need = aggregate output                                 │
  │                                                                 │
  │  See: Body-Feedback-Mechanism.md v2.1                           │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 3: SIGNAL ARCHITECTURE                                   │
  │                                                                 │
  │  2 types of reward (orthogonal dimension):                      │
  │    Evaluative Reward (μ-opioid, requires full Body-Feedback-    │
  │    Precondition)                                                │
  │    Direct-State Reward (CT afferents, eCB, hardware-based)      │
  │  2 types of dissonance (SAME architecture, DIFFERENT direction):│
  │    Evaluative Dissonance (dACC, compiled, PFC CAN modulate)     │
  │    Direct-State Dissonance (nociceptors, hardware, NUMBNESS-PROOF)│
  │  × E₀→E₃ complexity gradient (BOTH reward + dissonance)        │
  │  × 5 Profiles ("characters" of reward)                          │
  │  Body-Feedback-Precondition = 5 preconditions → signal fires or │
  │  does not                                                       │
  │                                                                 │
  │  See: Reward-Signal-Architecture.md v2.1, 03-Reward.md,         │
  │       Dissonance-Signal-Architecture.md v1.0                     │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 4: GAP SYSTEM                                            │
  │                                                                 │
  │  Gap Direction = f(surrounding chunks) — WHY reward is personal │
  │  3 Satiation Profiles (Cyclic/Tonic/Generative) — HOW gaps feed │
  │  5-Parameter per-gap model — integrated observation             │
  │  ENGINE/ROAD/VEHICLE architecture — hardware/collective/compile │
  │  Gap Distribution = per-person aggregate landscape              │
  │                                                                 │
  │  See: Gap-Direction, Gap-Body-Need, Gap-Distribution-Profile    │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 5: AGGREGATE OBSERVATION                                  │
  │                                                                 │
  │  Gap-Distribution = DEMAND ("what do I WANT")                   │
  │  Action-Space = SUPPLY ("what CAN I do")                        │
  │  Behavior = f(DEMAND × SUPPLY) — 4 quadrants                   │
  │  Reward Calibration = Goldilocks per-gap, dynamic equilibrium  │
  │  Hidden Quality = compilation depth → quality visibility        │
  │                                                                 │
  │  See: Action-Space, Gap-Distribution-Profile,                   │
  │       Reward-Calibration, Hidden-Quality-Perception              │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 6: PFC OBSERVATION + INTER-BODY                           │
  │                                                                 │
  │  Feeling = PFC observation of body-feedback (7-layer)           │
  │  Body-feedback (mechanism) ≠ Feeling (PFC observation)          │
  │  Inter-body: by-product match, Entity-Compiled, 5-Channel      │
  │  Body-Coupling: 4 bond types, firing modes                     │
  │                                                                 │
  │  See: Feeling.md v3.0, Inter-Body-Mechanism.md v2.0,            │
  │       Body-Coupling.md v3.0                                      │
  └─────────────────────────────────────────────────────────────────┘

  NOTE: Layers = conceptual hierarchy, not temporal sequence.
  Signal generation (Layer 2) + architecture (Layer 3) happen near-parallel.
  Gap system (Layer 4) = accumulated structure shaping real-time signals.
  PFC observation (Layer 6) = SEPARATE process, not the "output" of the pipeline.
```

---

## §3 — Dual-Pull + Interface Loop + 3 Genuine Discomfort Sources

### §3.1 — Dual-Pull Architecture

```
⭐ DUAL-PULL = FOUNDATIONAL ARCHITECTURE OF BODY SIGNAL:

  Schemas (chunks) are pulled SIMULTANEOUSLY by 2 forces:

  ① HARDWARE PULL (internal, conservative, seeks smooth):
     → Hebbian LTP: familiar patterns grow stronger
     → Habituation: VTA habituates → stops firing → smooth
     → Metabolic efficiency: compiled = low cost
     → Feature: comfort zone, routine, contentment
     → Dark side: stagnation, evolutionary lag

  ② DOMAIN PULL (external, demands adaptation, maps reality):
     → Novelty drive: genetic drive to explore
     → prediction-delta: new pattern → dopamine → attention
     → Evolutionary: fail to map reality → fail to survive
     → Feature: learning, growth, curiosity
     → Dark side: burnout, neural wear

  ⭐ TENSION = EVOLUTIONARY FEATURE, NOT BUG:
     → Only Hardware → stagnation → domain changes → death
     → Only Domain → burnout → resources exhausted → death
     → BOTH TOGETHER → oscillation consolidation ↔ exploration → thrive

  → Reward fires when 2 forces ALIGN ("passion" = body likes + domain needs)
  → Dissonance fires when 2 forces CONFLICT

  Compiled/Fresh connection (Inter-Body-Mechanism.md v2.0 §3):
  → Hardware pull = toward COMPILED (efficient, low cost)
  → Domain pull = toward FRESH evaluation when reality shifts
  → Dual-pull = Compiled/Fresh tension at SYSTEM level

  "Good melody" 4 criteria (Personal-Melody.md v2.0 §5):
  ① Smooth on hardware ② Maps domain accurately ③ Wide coverage ④ Durable

  See: Drill-Body-Feedback/01-Foundation.md §2 for full detail.
```

### §3.2 — Interface Loop 6-Step

```
⭐ 6-STEP INTERFACE LOOP — HOW BODY-DOMAIN INTERACTION RUNS:

  Step 1: DOMAIN → BODY sensory (external reality → neural transduction)
       ↓
  Step 2: BODY → FEEDBACK (unconscious 95% OR PFC 5% — match? coherence?)
       ↓
  Step 3: FEEDBACK → SCHEMA UPDATE (compile new / modify / reconsolidate)
       ↓
  Step 4: SCHEMA → ACTION (compiled schemas fire → motor output)
       ↓
  Step 5: ACTION → DOMAIN (body affects world)
       ↓
  Step 6: DOMAIN → BODY feedback (reality responds → loop closes → Step 1)

  NOTE: Feeling-Mechanism-Deep-Draft.md §3 has a DIFFERENT 8-step model:
    → 8-step = MICRO process (within body, per feeling episode)
    → 6-step = MACRO loop (organism ↔ environment)
    → COMPLEMENTARY, not competing. Different zoom level.

  Domain Reality = Final Arbiter (Inter-Body-Mechanism.md v2.0 §1):
  → Step 6 = WHERE domain confirms/rejects body's action
  → Body compiles from Step 6 outcome (not from Step 4 intention)
  → = WHY "just try it" works: body learns from domain feedback, not PFC plan

  See: Drill-Body-Feedback/01-Foundation.md §3 for full detail.
```

### §3.3 — 3 Genuine Discomfort Sources

```
⭐ CRITICAL REFRAME: CORTISOL DOES NOT CAUSE PAIN.

  🟢 Cortisol injection (healthy subjects): cortisol ↑ → NO pain
  🟢 Addison's disease (cortisol ≈ 0): patients are VERY uncomfortable
  → "Reduce cortisol" = wrong strategy. "Fix mismatch" = right strategy.

  3 GENUINE DISCOMFORT SOURCES (Cortisol-Baseline.md v2.1 §2.5):

  ① NOCICEPTION: tissue damage → nociceptors → pain.
     Cortisol arrives AFTER. Fix: protect + repair the source.

  ② MISMATCH: schema expects X, reality ≠ X.
     Signal fires FIRST → cortisol SECOND (supports the fix).
     Fix: update schema OR change reality. = CORE of almost ALL dissonance.

  ③ RECALIBRATION: mismatch detected → body activates pattern change.
     Temporarily unstable = discomfort. Analogy: muscle soreness from training.
     Fix: endure — process ends when new pattern is stable.

  ⭐ TREATMENT IMPLICATION:
    Target MISMATCH (root): solve problem, update expectations, accept unchangeable
    ONLY reducing cortisol (symptom): substances, dissociation, distraction
    → Risk: mismatch continues → body fires again → escalation

  ⭐ DISSONANCE TYPE × 3 SOURCES (Dissonance-Signal-Architecture.md v1.0 §4):
    ① Nociception = PURE Direct-State Dissonance (hardware, from birth)
    ② Mismatch NEEDS SPLITTING: hardware mismatch → Direct-State, compiled mismatch → Evaluative
    ③ Recalibration = MOSTLY Direct-State (hardware process)
    → Source × Type = ORTHOGONAL — both needed to classify accurately.

  See: Drill-Body-Feedback/02-Dissonance.md §3 for full detail.
  See: Dissonance-Signal-Architecture.md v1.0 for dissonance type detail.
```

---

## §4 — Signal Generation + Body-Need

```
⭐ 4TH CLASSIFICATION AXIS — HOW CHUNKS FIRE AND CREATE SIGNALS:

  Body-feedback has 4 ORTHOGONAL classification axes:
    Axis 1: Direction (reward/dissonance/neutral)
    Axis 2: Magnitude (14 levels)
    Axis 3: Source (nociception/mismatch/recalibration)
    Axis 4: CHUNK DYNAMICS ← core mechanism

  2 INPUT SOURCES (Body-Feedback-Mechanism.md v2.1 §2):

    ① SENSORY-DRIVEN: Domain → body input → chunks fire reactively
       → Full animals. No PFC needed. Timing: ms→seconds.
       → Examples: needle prick, good food, beautiful music, heat

    ② PATTERN-DRIVEN: Chunks fire internally → body responds accordingly
       → Replay, preview, comparison, gap detect, spreading activation
       → Examples: memory recall, Imagine-Final preview, social comparison

  3 CHUNK DYNAMICS (Body-Feedback-Mechanism.md v2.1 §3):

    ① CHUNK-SHIFT: same chunks, DIFFERENT valence (evaluation changes)
       → Example: betrayal → chunks about the person still exist, valence flips
       → 🟢 Evaluative conditioning (De Houwer 2007)

    ② CHUNK-MISS: compiled pattern DOES NOT FIRE (absent/degraded)
       → Example: habituated to a routine → routine disrupted → restlessness
       → 🟢 Successive Negative Contrast (Crespi 1942, Flaherty 1996)

    ③ CHUNK-GAP: pattern DOESN'T EXIST YET but network detects the absence
       → Example: physicist notices contradiction → drive to resolve
       → Gap-Direction.md v2.0: gap has DIRECTION = f(surrounding chunks)
       → 🟢 Information gap theory (Loewenstein 1994)

  COMPOUND: 1 event → multiple dynamics simultaneously
    → Losing money: Chunk-Miss (regret)
    → Being deceived into losing money: Miss + Shift (regret + anger)
    → Being deceived by a close friend: Miss + Shift + Gap (regret + anger + bitterness)

  QUALITY BASELINE SHIFT (SNC research):
    → Body compiles quality X → habituates → quality drops = Chunk-Miss
    → 🟢 SNC: rats downshift from good to normal → eat LESS than always-normal rats
    → Asymmetric: loss hurts ~2x gain (🟢 Kahneman & Tversky 1979)

  BODY-NEED = 2-SOURCE AGGREGATE (Body-Feedback-Mechanism.md v2.1 §1):
    → Body-need = hardware signals + chunk dynamics COMBINED
    → 7 properties: dynamic, multi-source, not fully PFC-accessible,
      partially compilable, has immediacy, can conflict internally, aggregate
    → 4 immediacy types: Acute / Chronic / Background / Emergent
    → Complexity Spectrum: Simple→Social→Meta (same mechanism, different substrate)

  See: Body-Feedback-Mechanism.md v2.1 for full detail (1,519L).
```

---

## §5 — Signal Architecture + Body-Feedback-Precondition

### §5.1 — Evaluative/Direct-State Reward

```
🟡 REWARD SIGNAL HAS 2 TYPES — ORTHOGONAL DIMENSION:

  ┌────────────────────────────────────────────────────────────┐
  │  EVALUATIVE REWARD                                         │
  │                                                            │
  │  Circuit: Hedonic hotspot (NAcc shell, VP, mOFC)          │
  │  Signal: μ-opioid + endocannabinoid (dependent)           │
  │  Body-Feedback-Precondition: Full 5 preconditions required │
  │  Requires: Compiled chunks (P2) + body-need gap (P1)      │
  │  Learned: YES — quality depends on chunk library          │
  │  Examples: Food appreciation, music, insight, social praise│
  ├────────────────────────────────────────────────────────────┤
  │  DIRECT-STATE REWARD                                       │
  │                                                            │
  │  Circuit: Interoceptive / body-state (VARIES by modality) │
  │  Signal: CT afferents (🟢 Löken 2009), eCB (🟢 Fuss 2015)│
  │  Body-Feedback-Precondition: Simplified (P1 basic,        │
  │  P2–P5 reduced/N/A)                                       │
  │  Requires: Hardware pathways (minimal compiled chunks)    │
  │  Learned: MINIMAL — hardware from birth                   │
  │  Examples: Touch comfort, runner's high, warmth, stretching│
  └────────────────────────────────────────────────────────────┘

  → Evaluative = RICH but CONDITIONAL on compilation
  → Direct-State = RELIABLE, always-available baseline ("evolutionary floor")
  → Loss of Evaluative (burnout) → Direct-State remains ("touch still good")
  → Evaluative × Direct-State cuts ACROSS all profiles:
    Profile ① Sensory: food = Evaluative, touch = Direct-State
    Profile ③ Social: praise = Evaluative, proximity = Direct-State
  → 5 Profiles = "characters" of reward (Sensory/Coherence/Social/Relief/Preview)
  → E₀→E₃ gradient = compilation depth applied to evaluation

  See: Reward-Signal-Architecture.md v2.1 for full detail (1,987L).

  ⭐ DISSONANCE COUNTERPART — SAME ARCHITECTURE, DIFFERENT DIRECTION:

    Dissonance ALSO HAS Evaluative/Direct-State — same insula gradient:
    → Evaluative Dissonance: dACC + anterior insula (social pain, moral injury)
      Compiled, conditional. PFC CAN modulate. Develops with age.
    → Direct-State Dissonance: nociceptors, thermoreceptors, visceral signals
      Hardware, from birth. PFC MINIMAL. NUMBNESS-PROOF.
    → Reward = burnout-proof (Direct-State Reward remains).
      Dissonance = numbness-proof (Direct-State Dissonance remains).
    → = 2 evolutionary floors, BOTH DIRECTIONS.

    See: Dissonance-Signal-Architecture.md v1.0 for full detail.
```

### §5.2 — Body-Feedback-Precondition Hypothesis

```
⭐ 5 BODY-FEEDBACK-PRECONDITIONS (v3) FOR BODY SIGNAL:

  Body signal (reward or dissonance) = function of 5 PRECONDITIONS
  simultaneously on the interface loop:

  ┌────────────────────────────────────┬──────────────────────────┐
  │ Body-Feedback-Precondition         │ Failure → subjective     │
  ├────────────────────────────────────┼──────────────────────────┤
  │ P1 Directed-Gap                    │ "Don't need it" /        │
  │   (body-need gap open)            │  "don't want it"         │
  ├────────────────────────────────────┼──────────────────────────┤
  │ P2 Chunk-Substrate                 │ "Don't get it" /         │
  │   (sufficient substrate)          │  confusion               │
  ├────────────────────────────────────┼──────────────────────────┤
  │ P3 Delta-Gate                      │ "Normal" / "routine" /   │
  │   (prediction-delta threshold)    │  "same old thing"        │
  ├────────────────────────────────────┼──────────────────────────┤
  │ P4 Match-Range                     │ Too alien: "too strange" │
  │   (Goldilocks zone — dynamic)     │ Too familiar: "boring"   │
  ├────────────────────────────────────┼──────────────────────────┤
  │ P5 Compile-Gate                    │ "Dislike despite fitting"│
  │   (chunk tag opioid vs cortisol)  │  avoidance despite match │
  └────────────────────────────────────┴──────────────────────────┘

  ALL 5 REQUIRED for full signal. Missing ANY → signal absent or wrong direction.

  ⭐ 2-LAYER INTERPRETATION (Gap-Direction.md v2.0 §6):
    P2→P1 = Layer 2 prerequisites: gap direction must EXIST
    P3 = Layer 1: signal mechanism fires (VTA detects delta)
    P4→P5 = Layer 2 quality: direction match evaluation
    "Unknown = no gap" = PRIOR to P1:
      No chunks → gap not yet formed → desire does not yet exist

  ⭐ Body-Feedback-Precondition × EVALUATIVE/DIRECT-STATE (RSA v2.1 §1.3):
    Evaluative: ALL 5 preconditions required (full evaluation)
    Direct-State: P1 simplified, P2–P5 reduced/N/A (hardware pathways)
    → Direct-State = RELIABLE (not gated by chunks)
    → Evaluative = RICH but CONDITIONAL on compilation

  Body-Feedback-Precondition PREDICTS:
    → Reward variation across individuals (same stimulus, different chunks)
    → Hedonic adaptation (baseline shift → Goldilocks target moves)
    → Flow state (all 5 aligned + continuous feed)
    → Art appreciation gradient (chunks build → match enters Goldilocks)
    → Per-person reward (same object → different reward per chunk base)

  See: Drill-Body-Feedback/03-Reward.md §3 + 04-Integration.md §9 for full detail.
```

---

## §6 — ⭐ Gap System

### §6.1 — Gap Direction

```
⭐ GAP DIRECTION = f(SURROUNDING CHUNK NETWORK STRUCTURE):

  Gap = hole in chunk network where the structure PREDICTS pattern C should exist
        but C is NOT YET COMPILED. Surrounding chunks define the "borders" of the hole.

  "Unknown = no gap":
    → Without chunks → no borders → no hole → NO GAP
    → You CANNOT miss something you don't know exists
    → E=mc² for a physicist = direction match (years of physics chunks predict it)
    → E=mc² for a child = no direction match (insufficient borders)
    → SAME information, DIFFERENT gap landscape → DIFFERENT reward

  Reward = DIRECTION MATCH quality:
    → prediction-delta (Schultz 1997) = detection mechanism (SOMETHING IS DIFFERENT)
    → Gap direction = content (DIFFERENT IN WHICH SPECIFIC WAY)
    → Both are needed to explain why reward is PERSONAL

  2-layer model:
    Layer 1: signal mechanism (VTA detection — SAME for all humans)
    Layer 2: direction content (chunk network — UNIQUE per person)

  By-product match connection: gap direction = WHY by-product match works
    → B's output matches A's gap DIRECTION → A's body reward fires
    → Gap overlap → by-product match probability

  See: Gap-Direction.md v2.0 for full detail (2,681L).
```

### §6.2 — 3 Satiation Profiles

```
🟡 3 SATIATION PROFILES — HOW DIFFERENT GAPS CONSUME:

  ① CYCLIC: fill → satiation CLEAR → gap DORMANT → returns after interval
     → Examples: hunger (fill→satisfied→dormant 4-6h→returns), safety checking
     → Hormone-linked: ghrelin/leptin cycle, cortisol circadian
     → Body KNOWS "enough" — clear stop signal

  ② TONIC: fill ongoing → habituates SLOWLY → background satisfaction
     → Examples: social touch (CT afferents), ambient comfort, companionship
     → Weber-Fechner: logarithmic habituation (slow, not abrupt)
     → ONGOING fill = ONGOING reward (different from Cyclic's clear stop)

  ③ GENERATIVE: fill → CREATES NEW gaps → perpetual expansion
     → Examples: curiosity (answer → new questions), mastery (learn → see more gaps)
     → Self-sustaining: satisfaction = source of next gap
     → Aron & Aron 1996: self-expansion model
     → "The more you know the more you know you don't know" = Generative in action

  TRANSITIONS possible:
    Cyclic → Generative: food → culinary exploration
    Generative → Tonic: intense curiosity → settled expertise maintenance

  5-PARAMETER per-gap model:
    ① Source (hardware sensor/hormone/coherence?)
    ② Satiation (Cyclic/Tonic/Generative?)
    ③ Reward (Evaluative : Direct-State ratio?)
    ④ Chain (direct fill or how many steps away?)
    ⑤ Dependency (how much infrastructure required?)

  ENGINE/ROAD/VEHICLE architecture:
    ENGINE (Hardware) = source of ALL drives. Always running.
    ROAD (Collective-Arc) = infrastructure to fill. NOT an opposing force.
    VEHICLE (Compilation) = individual's compiled chains. 15-20 years to build.

  See: Gap-Body-Need.md v1.0 for full detail (1,388L).
```

### §6.3 — Gap Distribution Profile

```
🟡 GAP DISTRIBUTION = PER-PERSON GAP LANDSCAPE:

  Each person = their own GAP DISTRIBUTION — the totality of currently active gaps.

  4 OBSERVATION AXES:
    ① Domain Center: gaps cluster in WHICH domain? (arts/science/social/practical)
    ② Origin Balance: hardware-origin vs compiled-origin ratio?
    ③ Depth Profile: shallow-broad or narrow-deep?
    ④ Stability: currently stable or currently shifting?

  4-LAYER FORMATION (gap landscape IS FORMED by):
    Layer 1: Collective-Arc (era, culture → install baseline gaps)
    Layer 2: Schemas (education, media → shape gap directions)
    Layer 3: Family/Micro-environment (family, friends → specific gaps)
    Layer 4: Hardware + Experience (genes, personal events → unique gaps)

  RESONANCE PREDICTION:
    → 2 people overlap in gap distribution → by-product match probability HIGH
    → "Compatibility" = gap distribution overlap (By-Product-Gap-Resonance.md v1.4)
    → Collective installs SAME baseline → Layer 1 overlap easy → "fellow citizens"
    → Domain-specific gaps → Layer 2-3 overlap → "colleagues", "kindred spirits"

  See: Gap-Distribution-Profile.md v1.1 for full detail (2,370L).
```

### §6.4 — Behavioral Prediction: DEMAND × SUPPLY

```
⭐ ACTUAL BEHAVIOR = f(Gap-Distribution × Action-Space):

  Gap-Distribution (DEMAND): "What do I WANT?" — where gaps cluster
  Action-Space (SUPPLY): "What CAN I do?" — where options are available
  Behavior: INTERSECTION OF BOTH — only where gap AND option MEET → action

  Action-Space 4 axes:
    ① Compiled Capacity (what you know, what skills you have)
    ② Resource Access (money, network, tools)
    ③ Freedom (what you're permitted to do, which obligations constrain you)
    ④ Awareness (HOW MUCH of your options you're AWARE OF — invisible = most dangerous)

  4 QUADRANTS:
    ┌────────────────────────────────┬────────────────────────────────┐
    │ HIGH DEMAND + HIGH SUPPLY      │ HIGH DEMAND + LOW SUPPLY       │
    │ = ACTIVE PURSUIT               │ = FRUSTRATION / STUCK          │
    │ Want + can → action            │ Want + can't → suffering       │
    ├────────────────────────────────┼────────────────────────────────┤
    │ LOW DEMAND + HIGH SUPPLY       │ LOW DEMAND + LOW SUPPLY        │
    │ = DRIFT / WASTE                │ = SIMPLE / TRAPPED             │
    │ Can + don't want → no drive    │ Don't want + can't → narrow    │
    └────────────────────────────────┴────────────────────────────────┘

  See: Action-Space.md v1.0 (1,729L) + Gap-Distribution-Profile.md v1.1 (2,370L).
```

---

## §7 — ⭐ Quality + Calibration

### §7.1 — Reward Calibration

```
🟡 GOLDILOCKS PER-GAP: HOW MUCH REWARD IS ENOUGH?

  3 ZONES:
    Under-reward: gap fill insufficient → dissonance persists
    Match (Goldilocks): gap fill proportional → clean reward
    Over-reward: gap fill excessive → 6 degradation mechanisms

  6 OVER-REWARD MECHANISMS:
    ① Threshold Adaptation (baseline shifts UP → need MORE)
    ② Overjustification (external reward erodes intrinsic — 🟢 Deci 1971)
    ③ Bridge Dependency (depends on external source for fill)
    ④ Baseline Shift (compiled quality X → habituates → X = new normal)
    ⑤ Competence-Reward Mismatch (rewarded despite low quality)
    ⑥ Evaluative/Direct-State Imbalance (one type dominant)

  ⭐ CANNOT PRESCRIBE — ONLY OBSERVE + ADJUST:
    → Goldilocks = per-gap, per-person, per-context
    → No universal "correct amount" of reward
    → Dynamic equilibrium (parallel to Logic-Feeling-Balance.md)
    → Domain feedback = only arbiter of calibration quality

  See: Reward-Calibration.md v1.1 for full detail (1,356L).
```

### §7.2 — Hidden Quality Perception

```
🟡 HIDDEN QUALITY = "Unknown = no gap" × QUALITY:

  Core mechanism:
    Chunks_about_quality_dimension_X = ∅
    → Gap_about_quality_of_X = IMPOSSIBLE
    → Body-feedback about X = SILENT
    → X is overlooked — NOT from carelessness, but from MECHANISM

  2 TYPES:
    ① DOMAIN EXPERT: went through every layer → SEES hidden technical quality
       → Physician SEES X-ray anomaly in 200ms (🟢 Reingold 2001)
       → Senior programmer SEES code smell that a junior misses
       → "The back panel of the cabinet" (Steve Jobs)

    ② LEADER/COORDINATOR: went through every position → SEES hidden organizational quality
       → Bottom-up CEO SEES team burning out despite clean metrics
       → 🟢 Goodall 2009: physician-CEOs outperform
       → 🟢 Benson, Li & Shue 2019: Peter Principle empirical (N=38,843)

  COPIER vs EXPERT: "looks identical" but DIVERGES over time
    → Copier lacks chunks about hidden dimensions → no gap → no body signal
    → Expert HAS chunks → HAS gap → body SIGNALS when quality drops
    → Short term: indistinguishable. Long term: copier output degrades.

  DUNNING-KRUGER = META-LEVEL APPLICATION:
    → "Unknown = no gap" applied to ONE'S OWN evaluation capability
    → The incompetent DON'T KNOW they're incompetent (lack chunks to detect incompetence)
    → 🟢 Kruger & Dunning 1999: metacognitive deficit

  See: Hidden-Quality-Perception.md v1.0 for full detail (1,738L).
```

---

## §8 — Case Analyses + Special Mechanisms (pointers)

### §8.1 — Case Pointers

```
KEY CASES (full analysis in drill files):

  → Car Paradox (5 scenarios): Body-Feedback-Preconditions × same gift → opposite reward
    See: Drill-Body-Feedback/03-Reward.md §5

  → Van Gogh Appreciation Gradient: chunk base growth → Goldilocks → reward
    See: Drill-Body-Feedback/03-Reward.md §6

  → Schema Update Latency (C5): positive event → mini dissonance → delayed reward
    See: Drill-Body-Feedback/03-Reward.md §8

  → Mini Dissonance is CONSTANT: 3 sources (historical/Imagine-Final/social comparison)
    See: Drill-Body-Feedback/02-Dissonance.md §2.6

  → Effort-Proportional Reward: more effort → more dissonance → larger opioid at resolution
    See: Drill-Body-Feedback/03-Reward.md §4.7
```

### §8.2 — Trauma Loop + Hedonic Trap (key insights)

```
TRAUMA LOOP 4-STAGE (Drill-Body-Feedback/02-Dissonance.md §8):
  → Stage 1: trauma event → emotional peak compile → cortisol-tagged chunks
  → Stage 2: PFC = Lawyer — creates narrative but body DOESN'T TRUST IT
  → Stage 3: chronic cortisol → sleep quality degradation → recovery broken
  → Stage 4: PFC damage (🟢 Arnsten 2009) → worse problem-solving → LOOP
  → Recovery: new chunks COMPETE with old trauma chunks for probability share

HEDONIC TRAP (Drill-Body-Feedback/02-Dissonance.md §9):
  → Schema maintenance cost: each active schema requires rehearsal
  → Pursue single goal → OTHER schemas unmaintained → DRIFT
  → Achievement → body checks against CURRENT (drifted) schemas → mismatch → "emptiness"
  → Hedonic adaptation: baseline shifts → Goldilocks zone moves → need MORE
  → Prevention: maintain schema portfolio diversity = dual-pull balance
```

---

## §9 — Absorbed Content Map

```
CONTENT ABSORBED ELSEWHERE (authoritative versions in other files):

  ┌──────────────────────────────┬──────────────────────────────────────┐
  │ Body-Feedback-Draft content  │ Now authoritative in                 │
  ├──────────────────────────────┼──────────────────────────────────────┤
  │ Dopamine ≠ reward            │ Feeling-Mechanism-Deep-Draft.md §4.1 │
  │ VTA 7-step detection loop    │ Feeling-Mechanism-Deep-Draft.md §3.2 │
  │ 5 Body-Feedback-Preconditions│ Feeling-Mechanism-Deep-Draft.md §4.3 │
  │ (table)                     │                                      │
  │ Eureka 4 cases               │ Feeling-Mechanism-Deep-Draft.md §4.4 │
  │ Body-feedback vs Feeling     │ Feeling-Mechanism-Deep-Draft.md §1   │
  │ Trauma feeling distortion    │ Feeling-Mechanism-Deep-Draft.md §6.4 │
  │ Body vote mechanism          │ Feeling-Chunk-Bridge-Draft.md §2.1   │
  │ Reward as feeling type       │ Feeling-Mechanism-Deep-Draft.md §4.5 │
  └──────────────────────────────┴──────────────────────────────────────┘

CONTENT UNIQUE TO THIS FOLDER (not absorbed):

  ┌──────────────────────────────┬──────────────────────────────────────┐
  │ Unique contribution          │ File + Section                       │
  ├──────────────────────────────┼──────────────────────────────────────┤
  │ ⭐ Body-Need 2-source model  │ Body-Feedback-Mechanism v2.1 §1     │
  │ ⭐ Chunk dynamics (4th axis) │ Body-Feedback-Mechanism v2.1 §2-§3  │
  │ ⭐ Gap direction model       │ Gap-Direction v2.0 (2-layer, 22 ex) │
  │ ⭐ 3 Satiation Profiles      │ Gap-Body-Need v1.0 §2              │
  │ ⭐ 5-Parameter per-gap model │ Gap-Body-Need v1.0 §6              │
  │ ⭐ ENGINE/ROAD/VEHICLE       │ Gap-Body-Need v1.0 §9              │
  │ ⭐ Gap distribution 4 axes   │ Gap-Distribution-Profile v1.1 §2    │
  │ ⭐ Reward architecture       │ Reward-Signal-Architecture v2.1 §1-§3│
  │   (Evaluative/Direct-State)  │ E₀→E₃, Evaluative Gates Direct-State│
  │ ⭐ 5 Reward Profiles         │ Reward-Signal-Architecture v2.1 §4  │
  │ ⭐ Dissonance architecture   │ Dissonance-Signal-Architecture v1.0 §1│
  │   (Evaluative/Direct-State)  │ Same architecture, different direction│
  │ ⭐ Mismatch Splitting        │ Dissonance-Signal-Architecture v1.0 §4│
  │   (hardware vs compiled)     │ Source ② requires 2 sub-types        │
  │ ⭐ Numbness-Proof            │ Dissonance-Signal-Architecture v1.0 §1.5│
  │   (↔ Burnout-Proof reward)   │ Direct-State = evolutionary floor   │
  │ ⭐ Asymmetric Transition     │ Dissonance-Signal-Architecture v1.0 §7.5│
  │   (reward→diss FAST, ↩ SLOW)│ Evaluative layer asymmetry          │
  │ ⭐ Reward calibration        │ Reward-Calibration v1.1 (Goldilocks)│
  │ ⭐ DEMAND × SUPPLY           │ Action-Space v1.0 §1.3+§8          │
  │ ⭐ Hidden Quality Perception │ Hidden-Quality-Perception v1.0 §1   │
  │ 2 input sources              │ Body-Feedback-Mechanism v2.1 §2     │
  │ Compound mechanism           │ Body-Feedback-Mechanism v2.1 §4     │
  │ Quality Baseline Shift       │ Body-Feedback-Mechanism v2.1 §5     │
  │ Technology fill dimension    │ Gap-Body-Need v1.0 §10              │
  │ Entity-gap matching          │ Gap-Body-Need v1.0 §11              │
  │ Gap lifecycle                │ Gap-Body-Need v1.0 §14              │
  │ Conditional Interaction Model│ Reward-Signal-Architecture v2.1 §6  │
  │ 5 Forces Holding Model       │ Reward-Signal-Architecture v2.1 §10 │
  │ Placebo/Nocebo proof         │ Dissonance-Signal-Architecture v1.0 §3.3│
  │ E₀→E₃ applied to dissonance │ Dissonance-Signal-Architecture v1.0 §2│
  │ Entity × Evaluative Diss.    │ Dissonance-Signal-Architecture v1.0 §6│
  │ Clinical implications (5)    │ Dissonance-Signal-Architecture v1.0 §10│
  │ Development trajectory       │ Dissonance-Signal-Architecture v1.0 §9│
  │ Chunk dynamics × 2 types     │ Dissonance-Signal-Architecture v1.0 §5│
  │ 6 over-reward mechanisms     │ Reward-Calibration v1.1 §3          │
  │ Spiral dynamics supply-side  │ Action-Space v1.0 §4                │
  │ Copier vs Expert divergence  │ Hidden-Quality-Perception v1.0 §4   │
  │ Dunning-Kruger meta-level    │ Hidden-Quality-Perception v1.0 §5   │
  │ Dual-pull architecture       │ 01-Foundation §2                     │
  │ 6-step interface loop        │ 01-Foundation §3                     │
  │ "Good melody" 4 criteria     │ 01-Foundation §2.5                   │
  │ 3 Genuine Discomfort Sources │ 02-Dissonance §3                    │
  │ Mini dissonance 5 daily cases│ 02-Dissonance §2                    │
  │ Trauma loop 4-stage          │ 02-Dissonance §8                    │
  │ Hedonic trap mechanism       │ 02-Dissonance §9                    │
  │ Schema maintenance cost      │ 02-Dissonance §9                    │
  │ Car paradox 5 scenarios      │ 03-Reward §5                        │
  │ Van Gogh appreciation grad.  │ 03-Reward §6                        │
  │ Schema update latency (C5)   │ 03-Reward §8                        │
  │ Effort-proportional reward   │ 03-Reward §4.7                      │
  │ Body-Feedback-Precondition   │ 04-Integration §9                   │
  │ v3 full formalization       │                                     │
  │ 11 framework recommendations │ 04-Integration §12                  │
  └──────────────────────────────┴──────────────────────────────────────┘
```

---

## §10 — Honest Assessment + Cross-References

### §10.1 — Confidence breakdown

```
🟢 HIGH CONFIDENCE:

  ✓ Dopamine ≠ reward (Berridge & Robinson 1998, 2003)
  ✓ Cortisol = response/amplifier, not pain cause (Cortisol-Baseline evidence)
  ✓ Nociception mechanism established (Melzack & Wall gate control)
  ✓ Social pain uses physical pain pathway (Eisenberger 2003)
  ✓ Hedonic adaptation (Brickman 1978)
  ✓ Flashbulb memory / emotional peak compile (Brown & Kulik 1977)
  ✓ PFC damage from chronic stress (Arnsten 2009, McEwen 2007)
  ✓ Reconsolidation window (Nader 2000)
  ✓ Hebbian learning (Hebb 1949)
  ✓ Sleep consolidation mechanisms (Walker 2017)
  ✓ Evaluative opioid pathway (Berridge 2003, Mallik 2017)
  ✓ Direct-State non-opioid (Loseth 2019, Fuss 2015)
  ✓ Insula gradient (Craig 2002, 2013)
  ✓ SNC — Successive Negative Contrast (Crespi 1942, Flaherty 1996)
  ✓ Information gap theory (Loewenstein 1994)
  ✓ Perceptual learning as differentiation (Gibson & Gibson 1955)
  ✓ Expert recognition (Klein 1998, Chase & Simon 1973)
  ✓ Self-expansion model (Aron & Aron 1996, 2000)
  ✓ Capability Approach (Sen 1999)
  ✓ Pain 2-component (Melzack & Casey 1968, Rainville 1997, Price 2000)
  ✓ Placebo/Nocebo mechanism (Wager 2004, Zubieta 2005, Colloca & Benedetti 2005)
  ✓ Social pain = physical pain (Eisenberger 2003, Master 2009, Younger 2010)
  ✓ Negativity bias (Baumeister 2001, Rozin & Royzman 2001)
  ✓ Amygdala fast path (LeDoux 1996)


🟡 MEDIUM CONFIDENCE:

  ⚠ Dual-pull as architectural principle (each pull established,
    integration as 2-force model = framework synthesis)
  ⚠ 5 Body-Feedback-Preconditions matrix (each precondition grounded,
    ALL-5-required claim = framework synthesis)
  ⚠ 3 Genuine Discomfort Sources taxonomy (each source established,
    3-category organizing = framework synthesis)
  ⚠ Schema maintenance cost (concept plausible, not directly measured)
  ⚠ Compilable Architecture = WHY folder complexity (framework organizing)
  ⚠ Compiled/Fresh × Dual-Pull mapping (logical, not tested)
  ⚠ Evaluative/Direct-State × Body-Feedback-Precondition mapping (framework synthesis)
  ⚠ 3 Satiation Profiles taxonomy (patterns observed, taxonomy = framework)
  ⚠ ENGINE/ROAD/VEHICLE architecture (each component grounded,
    3-component model = framework synthesis)
  ⚠ DEMAND × SUPPLY behavioral prediction (logical model,
    each side established, integration = framework)
  ⚠ Hidden Quality = gap landscape consequence (mechanism established,
    quality application = framework synthesis)
  ⚠ Dunning-Kruger as meta-level "unknown = no gap" (🟢 K&D 1999
    replicated, meta-level interpretation = framework)
  ⚠ 5-Parameter per-gap model (each parameter grounded,
    integrated model = framework synthesis)
  ⚠ Evaluative/Direct-State Dissonance = orthogonal dimension
    (pain research 🟢 has similar split, unification = framework)
  ⚠ Mismatch Splitting: hardware vs compiled sub-types
    (each type grounded, splitting = framework synthesis)
  ⚠ Numbness-Proof ↔ Burnout-Proof symmetry
    (each side grounded, symmetric framing = framework)
  ⚠ Asymmetric Transition Speed: reward→dissonance FAST, reverse SLOW
    (negativity bias 🟢, mechanism localization = framework)
  ⚠ Clinical mappings: dissociation, alexithymia, anxiety, chronic pain
    (clinical data 🟢, 2-type interpretation = framework)
  ⚠ E₀→E₃ applied to BOTH directions (evaluation complexity, not reward-specific)
    (E₀→E₃ for reward established, dissonance application = framework)


🔴 LOW CONFIDENCE:

  ⚠ Goldilocks zone boundaries (inverted-U established,
    specific cutoffs = approximation, dynamic per person/context)
  ⚠ Unconscious 95% / PFC 5% ratio (qualitative split established,
    specific percentages = heuristic)
```

### §10.2 — Cross-references

```
📚 WITHIN BODY-FEEDBACK/ FOLDER:

  Body-Feedback-Label.md v2.1    → vocabulary anchor (MUST-READ)
  Body-Feedback-Mechanism.md v2.1 → 2-source, Body-Need, 3 dynamics
  Gap-Direction.md v2.0          → gap direction, 2-layer, by-product match
  Gap-Body-Need.md v1.0          → 3 Satiation, 5-Parameter, ENGINE/ROAD/VEHICLE
  Gap-Distribution-Profile.md v1.1 → 4 axes, 4-layer formation, resonance
  Reward-Signal-Architecture.md v2.1 → Evaluative/Direct-State, 5 Profiles
  Dissonance-Signal-Architecture.md v1.0 → Evaluative/Direct-State Dissonance, Mismatch Splitting, Clinical
  Reward-Calibration.md v1.1     → Goldilocks per-gap, calibration
  Action-Space.md v1.0           → supply-side, DEMAND × SUPPLY
  Hidden-Quality-Perception.md v1.0 → quality visibility, 2 types
  Drill-Evolutionary-Sensor-Architecture.md v1.0 → first-principles WHY architecture
  Drill-Body-Feedback/01-Foundation.md → dual-pull, 6-step loop
  Drill-Body-Feedback/02-Dissonance.md → 3 Genuine Discomfort Sources, threat, trauma, hedonic
  Drill-Body-Feedback/03-Reward.md     → Body-Feedback-Precondition, car paradox, Van Gogh
  Drill-Body-Feedback/04-Integration.md → walkthroughs, Body-Feedback-Precondition v3


📚 BODY-BASE/ CONNECTIONS:

  Inter-Body-Mechanism.md v2.0   → Compilable Architecture, 3 foundations,
                                    Compiled/Fresh, 3-cost, domain arbiter
  Body-Base.md v3.3              → entry point, Compilable Architecture
  Body-Coupling.md v3.0          → coupling mechanism, firing modes, bond types
  Valence-Propagation.md v3.0    → structural/current, hardware-subsidy, per-entity
  Cortisol-Baseline.md v2.1      → amplifier, 3 Genuine Discomfort Sources, chunk tag, 5 roles


📚 AGENT-MECHANISM/ CONNECTIONS:

  Self-Pattern-Modeling.md v3.1  → Compiled/Fresh, per-domain, 3 dimensions
  By-Product-Gap-Resonance.md v1.4 → 2-Stream, by-product match, 4 conditions
  Entity-Compiled.md v1.0        → Hub-and-Spoke, Formation, Grief A+B+C


📚 FEELING/ + PFC/ CONNECTIONS:

  Feeling.md v3.0                → 7-layer model, PFC observation
  Feeling-Mechanism-Deep-Draft.md → 8-step flow, reward definitive
  Feeling-Chunk-Bridge-Draft.md  → bidirectional mapping
  Imagine-Final.md v3.0          → constructive simulation, Gap→Miss
```
