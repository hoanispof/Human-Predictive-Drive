---
title: Drill — Evolutionary Sensor Architecture — Why Body-Feedback MUST Be the Way It Is
version: 1.0
created: 2026-05-25
source_version: Vietnamese v1.0
english_created: 2026-06-06
status: DRILL v1.0
scope: |
  FIRST-PRINCIPLES analysis: WHY evolution designed body-feedback architecture the way it did.
  Not from neuroscience observation (bottom-up) — from evolutionary CONSTRAINTS (top-down).
  8 insights: (1) can't make bidirectional sensor, (2) multiple one-way strategy,
  (3) brain integration levels, (4) baseline emergent, (5) WHY Evaluative MUST exist,
  (6) universal approach/avoid, (7) symmetry = functional requirement,
  (8) asymmetric speed in Evaluative layer.
purpose: |
  Dissonance-Signal-Architecture v1.0 answers: WHAT KINDS of dissonance exist (Evaluative/Direct-State).
  Reward-Signal-Architecture v2.0 answers: WHAT KINDS of reward exist (Evaluative/Direct-State).
  Inter-Body-Mechanism.md §9 answers: HOW evolution creates the 3-layer stack.
  This file answers: WHY the architecture MUST be the way it is — from evolutionary design constraints.
  = "If you were DESIGNING a body, what would you NEED?" → deduce architecture.
dependencies:
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃
  - Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State for dissonance
  - Body-Feedback-Mechanism.md v2.0 — 2 sources, 3 dynamics
  - Inter-Body-Mechanism.md v2.0 — Compilable Architecture, 3-Layer Evolution
  - Body-Base.md v3.2 — L0, L1, 3 genuine sources, adaptive baseline
  - Cortisol-Baseline.md v2.1 — amplifier, direction > level
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Drill — Evolutionary Sensor Architecture: Why Body-Feedback MUST Be the Way It Is

> **Conventional approach (bottom-up):** Observe the brain → describe the architecture → note patterns.
> **This file's approach (top-down):** If you were designing a body, WHAT WOULD YOU NEED? → deduce architecture → check against data.
>
> 3 foundational questions:
> ① Why does evolution NOT create a bidirectional sensor with a fixed zero-axis?
> ② Why MUST the Evaluative layer exist?
> ③ Why MUST reward and dissonance share the same architecture?
>
> Answer: All of it follows from CONSTRAINTS of evolution — random mutation + selection.
> Evolution has no engineer, no specification, no fixed zero-point.
> → Everything about body-feedback architecture = CONSEQUENCE of these constraints.

---

## §0 — SCOPE + READING GUIDE

```
This file DRILLS 8 insights from first-principles reasoning:

  §1: Evolution's Design Constraint — can't make bidirectional sensor
  §2: Multiple One-Way Strategy — TRP channels, CT, nociceptors
  §3: Brain Integration Levels — receptor → spinal cord → insula
  §4: Baseline is Emergent — adaptive zero, not designed zero
  §5: WHY Evaluative MUST Exist — evolutionary constraint → compilation
  §6: Universal Approach/Avoid — bacteria → humans
  §7: Symmetry = Functional Requirement — information theory
  §8: Asymmetric Speed — survival-first in Evaluative layer
  §9: Connection to Framework Concepts
  §10: Honest Assessment
  §11: Cross-references
```

---

## §1 — EVOLUTION'S DESIGN CONSTRAINT

### §1.1 — Why evolution CANNOT Create a Bidirectional Sensor

```
⭐ ENGINEER vs EVOLUTION — FUNDAMENTALLY DIFFERENT:

  ENGINEER (designing machines):
    → Has specification: "thermometer measures -40°C → +100°C"
    → Has reference standard: water freezes = 0°C
    → Has material control: choose mercury, design the scale
    → Result: 1 sensor, bidirectional, fixed zero-point

  EVOLUTION (random mutation + selection):
    → NO specification — only "survive or die"
    → NO reference standard — nobody defines "0°C"
    → NO material control — only random protein mutation
    → Protein receptor: fires or doesn't fire (threshold-based)
    → CANNOT "design" a receptor with a negative→0→positive axis

  → Evolution CAN ONLY create: threshold sensors
    → Receptor protein: inactive when stimulus < threshold
    → Active when stimulus > threshold
    → = ONE-WAY signal — reports "threshold crossed", NOT "how far below threshold"
```

### §1.2 — What a Bidirectional Sensor Needs That Evolution Cannot Provide

```
🟡 TO CREATE A BIDIRECTIONAL SENSOR YOU NEED:

  ① FIXED ZERO-POINT — a stable reference standard
    → Machine: 0°C = water freezing (defined BY THE ENGINEER)
    → Biology: NOBODY defines "baseline" — baseline EMERGES from system state

  ② LINEAR RESPONSE — output proportional to deviation from zero
    → Machine: thermometer rises/falls linearly
    → Biology: receptor proteins fire ALL-OR-NONE or sigmoid
      → No "negative firing rate" (neurons don't fire "less than 0")

  ③ NEGATIVE ENCODING — a way to report "below baseline"
    → Machine: thermometer drops → column shrinks
    → Biology: neuron CANNOT fire negatively — only fires or is silent
      → Silent is NOT a "negative signal" — silent = "no signal"
      → → A SEPARATE SENSOR is needed to report "below baseline"

  → Conclusion: evolution is FORCED to use multiple one-way sensors
  → NOT a design choice — it is a CONSTRAINT of the mechanism
```

---

## §2 — MULTIPLE ONE-WAY SENSOR STRATEGY

### §2.1 — Temperature: 3+ Separate Receptor Types

```
🟢 TEMPERATURE SENSING — THE MOST WELL-STUDIED CASE:

  ┌────────────────┬──────────────┬───────────────────────────┐
  │ Receptor       │ Range        │ Reports                   │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPM8          │ <26°C        │ "COLD" — one-way          │
  │ 🟢 McKemy 2002 │              │ (menthol receptor)        │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPV3, TRPV4   │ 33-39°C     │ "WARM" — one-way          │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPV1          │ >43°C        │ "HOT/PAIN" — one-way      │
  │ 🟢 Caterina 97 │              │ (capsaicin receptor)      │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPA1          │ <17°C        │ "VERY COLD/PAIN" — one-way│
  └────────────────┴──────────────┴───────────────────────────┘

  → 4+ SEPARATE receptor types — different proteins, different genes
  → Each one = threshold sensor (fires when stimulus falls within its range)
  → NOT 1 thermometer — rather 4 "alert buttons" for 4 different zones
  → Brain integrates 4 signals → creates unified "temperature sensation"
```

### §2.2 — Touch: 3 Independent Systems

```
🟢 TOUCH SENSING — 3 INDEPENDENT SYSTEMS:

  CT afferents: ONLY fire for slow gentle touch (1-10 cm/s)
    → "Pleasant touch" sensor — ONE-WAY (reports only "good")
    → 🟢 Löken et al. 2009: optimal velocity curve
    → 🟢 Olausson et al. 2002: unmyelinated C fibers

  Nociceptors (A-delta, C fibers): ONLY fire for tissue damage or intense pressure
    → "Pain" sensor — ONE-WAY (reports only "bad")
    → Threshold-based: below threshold = silent

  Aβ mechanoreceptors: fire for ALL touch (discriminative)
    → "Information" sensor — neutral (not good/bad)
    → Meissner, Pacinian, Merkel, Ruffini — 4 subtypes

  → 3 INDEPENDENT systems for the SAME modality
  → Evolution created: 1 "good" sensor + 1 "bad" sensor + 1 "information" sensor
  → Brain integrates 3 systems → unified touch experience
```

### §2.3 — Taste: Sweet vs Bitter = Entirely Separate

```
🟢 TASTE — SEPARATE RECEPTOR FAMILIES:

  T1R2/T1R3 heterodimer: SWEET receptor
    → "Caloric, approach" — ONE-WAY
    → 🟢 Nelson et al. 2001

  T2R family (~25 variants): BITTER receptors
    → "Poison, reject" — ONE-WAY
    → Many variants because: many types of poisons → many detectors needed

  → ENTIRELY SEPARATE — different proteins, different genes, different pathways
  → Evolution did NOT create a "taste-o-meter" with a pleasant→0→unpleasant axis
  → Created 2 systems: 1 to detect "caloric" + 1 to detect "poison"
```

### §2.4 — General Pattern

```
🟡 EVOLUTION'S UNIVERSAL STRATEGY:

  ① Multiple SIMPLE sensors (cheap to evolve: 1 protein = 1 gene)
  ② Each sensor = ONE-WAY, threshold-based (fires or silent)
  ③ Brain INTEGRATES multiple signals → unified representation
  ④ Brain LEARNS baseline from integrated signals (= compilation)

  = "Many simple sensors + 1 integrating brain"
  > "1 complex super-sensor"

  WHY THIS STRATEGY WINS:
    → 1 gene mutation → 1 new receptor → detects 1 new thing
    → Simple, incremental, each mutation small
    → Brain integration = GENERAL-PURPOSE (Compilable Architecture)
    → → No need to evolve new integration for each new sensor
    → → Add sensor → brain automatically integrates

  WHY SUPER-SENSOR LOSES:
    → Requires multiple coordinated mutations simultaneously
    → Requires internal reference standard (impossible to evolve)
    → Requires linear encoding (proteins don't work this way)
    → → Evolutionary dead end
```

---

## §3 — BRAIN INTEGRATION LEVELS

```
⭐ MANY ONE-WAY INPUTS → ONE BIDIRECTIONAL REPRESENTATION:

  ┌──────────────────┬────────────────────────┬──────────────────┐
  │ Level            │ Processing             │ Representation   │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ RECEPTOR         │ Threshold detection    │ Multiple         │
  │ (skin, tongue)   │ Each: "above MY range" │ one-way signals  │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ SPINAL CORD      │ Gate control           │ Begin merging    │
  │                  │ (Aβ inhibit C fiber)   │ good/bad signals │
  │                  │ 🟢 Melzack & Wall 1965 │                  │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ BRAINSTEM        │ Converging pathways    │ Multi-modal      │
  │ + THALAMUS       │ Homeostatic regulation │ integration      │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ POSTERIOR INSULA │ First-order body map   │ Raw interoceptive│
  │                  │ 🟢 Craig 2002          │ (still Direct-St)│
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ ANTERIOR INSULA  │ + context + evaluation │ Unified          │
  │                  │ 🟢 Craig 2009          │ BIDIRECTIONAL    │
  │                  │                        │ (Eval + Direct-St│
  │                  │                        │  integrated)     │
  └──────────────────┴────────────────────────┴──────────────────┘

  → Bidirectional experience = CREATED by the brain, NOT by the receptor
  → Receptor: "TRPM8 is firing" (fact). Brain: "COLDER than baseline" (evaluation)
  → "Prediction-delta" = brain-level concept (does not exist at the receptor level)
  → The framework describes what happens from the brainstem upward — correct level
```

---

## §4 — BASELINE IS EMERGENT, NOT DESIGNED

### §4.1 — Machine Zero vs Body Zero

```
⭐ 2 FUNDAMENTALLY DIFFERENT KINDS OF "ZERO":

  MACHINE ZERO (designed):
    → 0°C = water freezing (defined by Celsius, universal)
    → 0V = no potential difference (defined by physics)
    → Fixed, universal, unchanging
    → Created BY the engineer WITH specification

  BODY ZERO (emergent):
    → 37°C = where warm-sensitive + cold-sensitive neurons fire BALANCED
    → NOBODY "defined" 37°C — it happens to be where the system equilibrates
    → Adaptive, per-person, shifts over time
    → EMERGES from system dynamics, NOT designed
```

### §4.2 — Adaptive Baseline

```
🟡 BODY BASELINE = ADAPTIVE ZERO — SHIFTS OVER TIME:

  ① HABITUATION: repetition → baseline shifts UP
    → Coffee every morning → body compiles "having coffee" = new baseline
    → Day without coffee → deviation FROM THE NEW BASELINE → dissonance

  ② SNC (Successive Negative Contrast):
    → Baseline "already has something good" → downshift → overreaction
    → 🟢 Crespi 1942, Flaherty 1996

  ③ COMPILATION DEPTH:
    → Expert baseline DIFFERS from novice baseline (different compiled patterns)
    → A musician hears dissonance that a non-musician misses

  ④ PER-PERSON VARIATION:
    → COMT genotype → dopamine clearance speed → different sensitivity baseline
    → DRD4 genotype → different novelty threshold
    → → "Zero" IS DIFFERENT per person

  → Machine: 1 thermometer = 1 zero, universal
  → Body: each channel × each person × each moment = DIFFERENT zero
  → → Brain MUST continuously RECALIBRATE zero
  → → Recalibration = compilation (learning the new baseline)
```

---

## §5 — WHY EVALUATIVE LAYER MUST EXIST

```
⭐ EVALUATIVE LAYER = CONSEQUENCE OF EVOLUTIONARY CONSTRAINT:

  PROBLEM:
    Evolution CANNOT hardcode a zero-point (§1)
    → Sensors only report "threshold crossed" — NOT "deviation from baseline"
    → Baseline = emergent (§4) — differs per person, shifts over time
    → → SOMETHING must figure out "what is MY baseline"
    → → SOMETHING must evaluate "how much deviation, in which direction"

  SOLUTION:
    BRAIN learns baseline through COMPILATION:
    → Experience → body-feedback → Hebbian → compiled pattern = learned baseline
    → New input → compare vs compiled baseline → evaluate deviation
    → = EVALUATIVE PROCESSING

  THEREFORE:
    → Evaluative layer MUST exist
    → NOT optional feature — it is the NECESSARY SOLUTION to "no hardcoded zero"
    → Compilable Architecture = the brain's answer to evolution's limitation

  DIRECT-STATE = what evolution CAN hardcode:
    → Nociception: tissue damage IS bad (no baseline needed — damage = always bad)
    → CT afferents: gentle touch IS pleasant (no baseline needed — CT pathway = always)
    → Hardware from birth — does NOT need to learn a baseline
    → = THESE are what evolution can do WITHOUT compilation

  EVALUATIVE = what evolution CANNOT hardcode → brain must learn:
    → "Is morning coffee good?" → depends on MY compiled baseline
    → "Does being scolded hurt?" → depends on MY Entity-Compiled depth
    → "Is company bankruptcy frightening?" → depends on MY career compilation
    → = THESE require a LEARNED baseline → require Evaluative processing

  → Direct-State = evolution's DIRECT solution (hardcode what is universal)
  → Evaluative = evolution's INDIRECT solution (compile what is individual)
  → 2 types = NECESSARY, not accidental
```

---

## §6 — UNIVERSAL APPROACH/AVOID

### §6.1 — Bacteria → Humans: Same Principle

```
⭐ ALL LIVING ORGANISMS NEED APPROACH/AVOID:

  ┌──────────────┬────────────┬──────────────────────────────────┐
  │ Organism     │ Neurons    │ Mechanism                        │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ E. coli      │ 0          │ Chemoreceptors on membrane       │
  │ (bacteria)   │            │ → swim toward glucose (approach) │
  │              │            │ → tumble away from acid (avoid)  │
  │              │            │ = Direct chemical response       │
  │              │            │ 🟢 Berg & Brown 1972             │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ C. elegans   │ 302        │ Simple circuits                  │
  │ (nematode)   │            │ → learned avoidance              │
  │              │            │ → habituation (proto-compile!)   │
  │              │            │ 🟢 Rankin et al. 1990            │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Drosophila   │ ~100K      │ Mushroom body (learning center)  │
  │ (fruit fly)  │            │ → conditioned preference/aversion│
  │              │            │ → dopamine reward pathways       │
  │              │            │ 🟢 Waddell 2013                  │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Fish         │ ~10M       │ Pallium (proto-cortex)           │
  │              │            │ → learned fear, social hierarchy │
  │              │            │ → opioid reward system           │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Dog/Cat      │ ~500M-2B   │ Cortex + limbic                  │
  │              │            │ → Social bonding, learned fear   │
  │              │            │ → E₀-E₂ (food pref, social eval)│
  │              │            │ → Compilation: present but limited│
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Human        │ ~86B       │ Massive cortex + PFC             │
  │              │            │ → E₀-E₃ (abstract, existential) │
  │              │            │ → Compilation: DEEP (decades)    │
  │              │            │ → "Life is meaningless" = E₃ only│
  └──────────────┴────────────┴──────────────────────────────────┘

  → Approach/avoid = UNIVERSAL across ALL life
  → NOT a feature of neurons — it is a feature of BEING ALIVE
  → Bacteria: chemical gradient. Nematode: 302-neuron circuit.
  → Human: 86 billion neurons. SAME PRINCIPLE.
```

### §6.2 — Evaluative/Direct-State Across the Evolutionary Spectrum

```
🟡 DIRECT-STATE = UNIVERSAL. EVALUATIVE = SCALES WITH COMPILATION:

  Bacteria:       Direct-State only (chemical sensor → immediate response)
  Nematode (302n): Direct-State + proto-Evaluative (habituation = basic baseline learning)
  Insects:        Direct-State + E₀ (hardwired evaluation, mushroom body)
  Fish:           Direct-State + E₀-E₁ (opioid pathway, learned preferences)
  Dog/Cat:        Direct-State + E₀-E₂ (social evaluation, entity recognition)
  Humans:         Direct-State + E₀-E₃ (abstract, existential, decades of compilation)

  → Direct-State = evolutionary FLOOR — every organism with a nervous system has it
  → Evaluative = scales with COMPILATION CAPACITY
  → More neurons → more compilation → deeper Evaluative → more "types" of suffering AND reward
  → = Trade-off: Compilable Architecture = more adaptation BUT more vulnerability
  → = WHY humans "suffer from thoughts alone" (E₃ Evaluative Dissonance)
    while insects do not (Direct-State only)
```

---

## §7 — SYMMETRY = FUNCTIONAL REQUIREMENT

### §7.1 — Information Theory Argument

```
⭐ ONE-WAY SENSOR = ZERO USEFUL INFORMATION (Shannon 1948):

  Sensor ONLY reports "cool = pleasant" but CANNOT report "hot = problem":
    → Step into harsh sunlight: NO signal
    → Step into cool shade: signal "pleasant"
    → BUT: if there's no signal for "hot" → can't know cool is DIFFERENT from hot
    → → "Cool = pleasant" only has meaning IF "hot = discomfort" exists as reference

  Information requires CONTRAST:
    → Shannon: a signal that never changes = zero information
    → Signal going only 1 direction = half information
    → Signal going both directions = full information
    → → Body NEEDS bidirectional feedback for each channel

  → CANNOT have a reward channel WITHOUT a corresponding dissonance channel
  → CANNOT have a dissonance channel WITHOUT a corresponding reward channel
  → → 2 directions = functional REQUIREMENT, not coincidence
```

### §7.2 — The Organism Needs a 3-State Axis: Improve / Maintain / Degrade

```
🟡 ORGANISM NEEDS 3 STATES FOR EACH PARAMETER:

  ┌──────────────┬──────────────────────────────────────┐
  │ State        │ Organism's need                      │
  ├──────────────┼──────────────────────────────────────┤
  │ IMPROVING    │ "Getting better" → continue behavior │
  │ (approach)   │ = reward signal                      │
  ├──────────────┼──────────────────────────────────────┤
  │ MAINTAINING  │ "Stable" → keep behavior the same    │
  │ (baseline)   │ = no signal / low signal             │
  ├──────────────┼──────────────────────────────────────┤
  │ DEGRADING    │ "Getting worse" → change behavior    │
  │ (avoid)      │ = dissonance signal                  │
  └──────────────┴──────────────────────────────────────┘

  Missing ANY state → system BREAKS:
    Only approach (reward only): doesn't know when degrading → dies from ignoring threats
    Only avoid (dissonance only): doesn't know when improving → cannot learn what works
    Only maintain (no feedback): zombie → no adaptation possible

  → ALL 3 states MUST exist for EVERY parameter
  → → Reward + dissonance MUST coexist for EVERY channel
  → → Architecture for reward MUST be symmetric with dissonance
    (same channel, same sensors, same integration machinery)
```

### §7.3 — Why the SAME Architecture

```
🟡 REWARD AND DISSONANCE USE THE SAME INFRASTRUCTURE:

  Same insula gradient: posterior → anterior (🟢 Craig 2002)
  Same ACC conflict monitoring (🟢 Botvinick 2004)
  Same evaluation machinery (anterior insula + OFC/vmPFC)

  WHY EVOLUTION DIDN'T CREATE 2 SEPARATE SYSTEMS:
    → 2 separate systems = 2× cost (double the neural machinery)
    → 2 separate systems = synchronization problem (must coordinate 2 systems)
    → 2 separate systems = evolution must evolve BOTH in parallel

  1 bidirectional system = cheaper, simpler, auto-synchronized:
    → Same sensors → different direction → different output
    → Same evaluation machinery → applied to both directions
    → Evolution only needs to evolve 1 integration system
    → → Natural selection STRONGLY favors 1 symmetric system over 2 separate ones
```

---

## §8 — ASYMMETRIC SPEED IN EVALUATIVE LAYER

```
⭐ ARCHITECTURE SYMMETRIC — BUT SPEED ASYMMETRIC — WHY?

  DIRECT-STATE: relatively SYMMETRIC speed
    Pain onset ≈ touch onset (same hardware speed)
    Pain offset ≈ touch offset (when stimulus removed)
    → Hardware: symmetric — because same mechanism, same receptor dynamics

  EVALUATIVE: STRONGLY ASYMMETRIC speed
    Threat detection: FAST (amygdala ~12ms, bypasses PFC)
    Reward evaluation: SLOW (5 Body-Feedback-Preconditions, PFC verify)
    Threat clearance: SLOW (cortisol half-life 60-90 min)
    Reward deactivation: FAST (opioid off in seconds)

  WHY ASYMMETRIC IF SAME ARCHITECTURE:
    → Architecture = symmetric (same hardware, same integration)
    → TIMING = asymmetric (DIFFERENT evolutionary pressures)
    → Evolution TUNES speed independently for each direction:

    Miss a threat (false negative) → DIE → gene eliminated
    False alarm for threat (false positive) → wastes energy → survive
    → → Threat detection: OPTIMIZE for SPEED (better to be wrong fast than slow)

    Miss a reward (false negative) → miss out → survive, find it later
    False alarm for reward (false positive) → approach danger → DIE
    → → Reward evaluation: OPTIMIZE for ACCURACY (verify before approaching)

  → Architecture: symmetric (same sensors, same brain integration)
  → Speed: asymmetric (different survival cost → different optimization)
  → = Evolution CAN tune speed WITHOUT changing architecture
    (like same car, different gear ratios)

  🟢 Baumeister et al. 2001: "Bad is stronger than good"
  🟢 Kahneman & Tversky 1979: Loss aversion ~2×
  🟢 Rozin & Royzman 2001: Negativity dominance
```

---

## §9 — CONNECTION TO FRAMEWORK CONCEPTS

```
🟡 8 INSIGHTS MAP TO THE FRAMEWORK:

  §1 (can't make bidirectional) →
    Framework's "prediction-delta" = BRAIN-LEVEL concept
    (not receptor-level — receptors don't compute delta)

  §2 (multiple one-way) →
    Body-Base.md L1 "17 categories" = multiple one-way sensor channels
    Brain integrates → "body-feedback" = INTEGRATED signal

  §3 (brain integration) →
    Craig's insula gradient = FROM one-way TO bidirectional
    Posterior insula = still one-way (Direct-State)
    Anterior insula = bidirectional (Evaluative + Direct-State integrated)

  §4 (baseline emergent) →
    Body-Base.md: "adaptive baseline" = LEARNED, per-person, shifts
    NOT hardcoded — COMPILED through experience
    = WHY SNC works: baseline CAN shift UP → downshift = overreaction

  §5 (WHY Evaluative MUST exist) →
    Evaluative = brain's answer to "no hardcoded zero"
    Evaluative = compilation applied to baseline learning + deviation evaluation
    Compilable Architecture = ENABLES the Evaluative layer
    = WHY insects (Hardwired Architecture) = Direct-State only

  §6 (universal approach/avoid) →
    Framework's body-feedback system = HUMAN VERSION of universal principle
    Same principle as bacterial chemotaxis — DIFFERENT depth
    E₀→E₃ = compilation depth gradient

  §7 (symmetry required) →
    Reward-Signal-Architecture + Dissonance-Signal-Architecture = 2 counterpart files = CORRECT
    Reward Evaluative/Direct-State ↔ Dissonance Evaluative/Direct-State
    = SAME architecture, different direction
    = Functional requirement, not coincidence

  §8 (asymmetric speed) →
    Asymmetry in EVALUATIVE (compiled = tunable), not Direct-State (hardware = fixed)
    = WHY "calming down" takes time (Evaluative clearance slow)
    = WHY 1 negative ruins a positive experience (Evaluative threat: fast-on, slow-off)
```

---

## §10 — HONEST ASSESSMENT

```
🟢 ESTABLISHED:
  → TRP channels as separate receptor types — 🟢 Caterina 1997, McKemy 2002
  → CT afferents separate from nociceptors — 🟢 Löken 2009
  → Sweet/bitter separate receptors — 🟢 Nelson 2001
  → Insula gradient — 🟢 Craig 2002, 2009
  → Gate control theory — 🟢 Melzack & Wall 1965
  → "Bad is stronger than good" — 🟢 Baumeister 2001
  → Bacterial chemotaxis — 🟢 Berg & Brown 1972
  → C. elegans habituation — 🟢 Rankin 1990

🟡 FRAMEWORK SYNTHESIS:
  → "Evolution can't make bidirectional sensor" = synthesis from known constraints
  → "Evaluative MUST exist because no hardcoded zero" = novel derivation
  → "Symmetry = functional requirement" from information theory = novel
  → "Asymmetry in Evaluative, not Direct-State" = framework insight
  → Spectrum bacteria→humans with E₀→E₃ mapping = framework

🔴 HYPOTHESIS:
  → Exact E₀→E₃ boundaries across species
  → Whether C. elegans habituation truly = proto-Evaluative
  → Precise evolutionary selection mechanism for speed asymmetry tuning
```

---

## §11 — CROSS-REFERENCES

```
PRIMARY:
  → Reward-Signal-Architecture.md v2.0 — reward Evaluative/Direct-State
  → Dissonance-Signal-Architecture.md v1.0 — dissonance Evaluative/Direct-State
  → Body-Feedback-Mechanism.md v2.0 — 2 sources, 3 dynamics
  → Inter-Body-Mechanism.md v2.0 — Compilable Architecture (§1), 3-Layer Evolution (§9)

BODY-BASE:
  → Body-Base.md v3.2 — L0, L1 (17 categories = multiple one-way sensors), adaptive baseline
  → Cortisol-Baseline.md v2.1 — amplifier, direction > level, sustainer
  → Body-Feedback-Label.md v2.0 — vocabulary standard

EVIDENCE:
  → Threat.md — 3 sources, amygdala fast path
  → 02-Dissonance.md — 3 genuine sources (nociception ≈ Direct-State)
  → 03-Reward.md — Body-Feedback-Preconditions, 7-step VTA
```

---

> *"Evolution has no engineer. No specification. No fixed zero-point.
> → Forced to use multiple one-way sensors + brain integration.
> → Brain must LEARN the baseline = compilation = Evaluative layer.
> → Evaluative layer MUST be bidirectional (reward + dissonance) — information theory requires it.
> → Architecture symmetric because same infrastructure; speed asymmetric because different survival costs.
> → From bacteria to humans: same principle, different depth.
> → The framework does not 'design' the architecture — it DERIVES it from evolutionary constraints."*
