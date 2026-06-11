---
title: Drill — Evolutionary Sensor Architecture — Why Body-Feedback MUST Be This Way
version: 1.0
created: 2026-05-25
status: DRILL v1.0
scope: |
  FIRST-PRINCIPLES analysis: WHY evolution designed body-feedback architecture
  the way it did. Not from neuroscience observation (bottom-up) —
  from evolutionary CONSTRAINTS (top-down).
  8 insights: (1) can't make bidirectional sensor, (2) multiple one-way strategy,
  (3) brain integration levels, (4) baseline emergent, (5) WHY Evaluative MUST exist,
  (6) universal approach/avoid, (7) symmetry = functional requirement,
  (8) asymmetric speed in Evaluative layer.
purpose: |
  Dissonance-Signal-Architecture v1.0 answers: WHAT KINDS of dissonance exist (Evaluative/Direct-State).
  Reward-Signal-Architecture v2.0 answers: WHAT KINDS of reward exist (Evaluative/Direct-State).
  Inter-Body-Mechanism.md §9 answers: HOW evolution creates 3-layer stack.
  This file answers: WHY the architecture MUST be this way — from evolutionary design constraints.
  = "If you were DESIGNING a body, what would you NEED?" → deduce architecture.
position: |
  Body-Feedback/ folder — alongside Reward-Signal-Architecture + Dissonance-Signal-Architecture.
  Drill file — stored analysis, complements Reward-Signal-Architecture/Dissonance-Signal-Architecture.
  NOT overlapping with Inter-Body §9 (3-Layer macro) — this file covers sensor-level micro constraints.
dependencies:
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃
  - Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State for dissonance
  - Body-Feedback-Mechanism.md v2.0 — 2 sources, 3 dynamics
  - Inter-Body-Mechanism.md v2.0 — Compilable Architecture, 3-Layer Evolution
  - Body-Base.md v3.2 — L0, L1, 3 genuine sources, adaptive baseline
  - Cortisol-Baseline.md v2.1 — amplifier, direction > level
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Drill — Evolutionary Sensor Architecture: Why Body-Feedback MUST Be This Way

> **Standard approach (bottom-up):** Observe the brain → describe architecture → note patterns.
> **This file's approach (top-down):** If you were designing a body, WHAT WOULD YOU NEED?
> → deduce architecture → check against data.
>
> 3 root questions:
> ① Why did evolution NOT create a bidirectional sensor with a fixed zero-point?
> ② Why MUST the Evaluative layer exist?
> ③ Why MUST reward and dissonance share the same architecture?
>
> Answer: Everything follows from the CONSTRAINTS of evolution — random mutation + selection.
> Evolution has no engineer, no specification, no fixed zero-point.
> → Everything about body-feedback architecture = CONSEQUENCE of these constraints.

---

## §0 — SCOPE + READING GUIDE

```
This file DRILLS 8 insights from first-principles reasoning:

  §1: Evolution's Design Constraint — can't make bidirectional sensor
  §2: Multiple One-Way Strategy — TRP channels, CT, nociceptors
  §3: Brain Integration Levels — receptor → spinal → insula
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

### §1.1 — Why evolution CANNOT create a bidirectional sensor

```
⭐ ENGINEER vs EVOLUTION — FUNDAMENTALLY DIFFERENT:

  ENGINEER (designing a machine):
    → Has specification: "thermometer measures -40°C → +100°C"
    → Has reference standard: water freezes = 0°C
    → Has material control: choose mercury, design the scale
    → Result: 1 sensor, bidirectional, fixed zero-point

  EVOLUTION (random mutation + selection):
    → NO specification — only "live or die"
    → NO reference standard — nobody defined "0°C"
    → NO material control — only random protein mutations
    → Protein receptor: fires or doesn't fire (threshold-based)
    → CANNOT "design" 1 receptor with a negative→0→positive axis

  → Evolution can ONLY create: threshold sensors
    → Receptor protein: inactive when stimulus < threshold
    → Active when stimulus > threshold
    → = ONE-WAY signal — reports "threshold exceeded,"
      does NOT report "how far below threshold"
```

### §1.2 — What a bidirectional sensor requires that evolution doesn't have

```
🟡 TO CREATE 1 BIDIRECTIONAL SENSOR YOU NEED:

  ① FIXED ZERO-POINT — a stable reference standard
    → Machine: 0°C = water freezes (defined BY THE ENGINEER)
    → Biology: nobody defines "baseline" — baseline EMERGES from system state

  ② LINEAR RESPONSE — output proportional to deviation from zero
    → Machine: thermometer rises/falls linearly
    → Biology: receptor proteins fire ALL-OR-NONE or sigmoid
      → No "negative firing rate" (neurons cannot fire "less than 0")

  ③ NEGATIVE ENCODING — a way to signal "below baseline"
    → Machine: thermometer drops → column shrinks
    → Biology: neuron CANNOT fire negative — only fires or is silent
      → Silent is NOT "negative signal" — silent = "no signal"
      → → Needs a SEPARATE SENSOR to report "below baseline"

  → Conclusion: evolution is FORCED to use multiple one-way sensors
  → NOT a design choice — it is a CONSTRAINT of the mechanism
```

---

## §2 — MULTIPLE ONE-WAY SENSOR STRATEGY

### §2.1 — Temperature: 3+ separate receptor types

```
🟢 TEMPERATURE SENSING — THE BEST-STUDIED CASE:

  ┌────────────────┬──────────────┬──────────────────────────────┐
  │ Receptor       │ Range        │ Reports                      │
  ├────────────────┼──────────────┼──────────────────────────────┤
  │ TRPM8          │ <26°C        │ "COLD" — one-way             │
  │ 🟢 McKemy 2002 │              │ (menthol receptor)           │
  ├────────────────┼──────────────┼──────────────────────────────┤
  │ TRPV3, TRPV4   │ 33-39°C      │ "WARM" — one-way             │
  ├────────────────┼──────────────┼──────────────────────────────┤
  │ TRPV1          │ >43°C        │ "HOT/PAINFUL" — one-way      │
  │ 🟢 Caterina 97 │              │ (capsaicin receptor)         │
  ├────────────────┼──────────────┼──────────────────────────────┤
  │ TRPA1          │ <17°C        │ "VERY COLD/PAINFUL" — one-way│
  └────────────────┴──────────────┴──────────────────────────────┘

  → 4+ SEPARATE receptor types — different proteins, different genes
  → Each = threshold sensor (fires when stimulus is in range)
  → NOT 1 thermometer — 4 "alert buttons" for 4 different zones
  → Brain integrates 4 signals → creates unified "temperature sensation"
```

### §2.2 — Touch: 3 independent systems

```
🟢 TOUCH SENSING — 3 INDEPENDENT SYSTEMS:

  CT afferents: fire ONLY for slow gentle touch (1-10 cm/s)
    → "Pleasant touch" sensor — ONE-WAY (only signals "good")
    → 🟢 Löken et al. 2009: optimal velocity curve
    → 🟢 Olausson et al. 2002: unmyelinated C fibers

  Nociceptors (A-delta, C fibers): fire ONLY on tissue damage/intense pressure
    → "Pain" sensor — ONE-WAY (only signals "bad")
    → Threshold-based: below threshold = silent

  Aβ mechanoreceptors: fire for ALL touch (discriminative)
    → "Information" sensor — neutral (not good/bad)
    → Meissner, Pacinian, Merkel, Ruffini — 4 subtypes

  → 3 INDEPENDENT systems for the SAME modality
  → Evolution created: 1 sensor "good" + 1 sensor "bad" + 1 sensor "information"
  → Brain integrates all 3 → unified touch experience
```

### §2.3 — Taste: sweet vs bitter = completely separate

```
🟢 TASTE — SEPARATE RECEPTOR FAMILIES:

  T1R2/T1R3 heterodimer: SWEET receptor
    → "Caloric, approach" — ONE-WAY
    → 🟢 Nelson et al. 2001

  T2R family (~25 variants): BITTER receptors
    → "Poison, reject" — ONE-WAY
    → Many variants because: many types of poison → many detectors needed

  → Completely SEPARATE — different proteins, different genes, different pathways
  → Evolution did NOT create 1 "taste-o-meter" with a pleasant→0→unpleasant axis
  → Created 2 systems: 1 to detect "caloric" + 1 to detect "poison"
```

### §2.4 — The general pattern

```
🟡 EVOLUTION'S UNIVERSAL STRATEGY:

  ① Multiple SIMPLE sensors (cheap to evolve: 1 protein = 1 gene)
  ② Each sensor = ONE-WAY, threshold-based (fires or silent)
  ③ Brain INTEGRATES multiple signals → unified representation
  ④ Brain LEARNS baseline from integrated signals (= compilation)

  = "Many simple sensors + 1 integrating brain"
  > "1 complex super-sensor"

  WHY this strategy WINS:
    → 1 gene mutation → 1 new receptor → detect 1 new thing
    → Simple, incremental, each mutation small
    → Brain integration = GENERAL-PURPOSE (Compilable Architecture)
    → → No need to evolve new integration for each new sensor
    → → Add a sensor → brain automatically integrates

  WHY super-sensor LOSES:
    → Requires multiple coordinated mutations simultaneously
    → Requires internal reference standard (no way to evolve)
    → Requires linear encoding (proteins don't work this way)
    → → Evolutionary dead end
```

---

## §3 — BRAIN INTEGRATION LEVELS

```
⭐ MANY ONE-WAY INPUTS → ONE BIDIRECTIONAL REPRESENTATION:

  ┌──────────────────┬────────────────────────┬──────────────────────────┐
  │ Level            │ Processing             │ Representation           │
  ├──────────────────┼────────────────────────┼──────────────────────────┤
  │ RECEPTOR         │ Threshold detection    │ Multiple                 │
  │ (skin, tongue)   │ Each: "above MY range" │ one-way signals          │
  ├──────────────────┼────────────────────────┼──────────────────────────┤
  │ SPINAL CORD      │ Gate control           │ Begin merging            │
  │                  │ (Aβ inhibit C fiber)   │ good/bad signals         │
  │                  │ 🟢 Melzack & Wall 1965 │                          │
  ├──────────────────┼────────────────────────┼──────────────────────────┤
  │ BRAINSTEM        │ Converging pathways    │ Multi-modal              │
  │ + THALAMUS       │ Homeostatic regulation │ integration              │
  ├──────────────────┼────────────────────────┼──────────────────────────┤
  │ POSTERIOR INSULA │ First-order body map   │ Raw interoceptive        │
  │                  │ 🟢 Craig 2002          │ (still Direct-State)     │
  ├──────────────────┼────────────────────────┼──────────────────────────┤
  │ ANTERIOR INSULA  │ + context + evaluation │ Unified                  │
  │                  │ 🟢 Craig 2009          │ BIDIRECTIONAL            │
  │                  │                        │ (Evaluative + Direct-    │
  │                  │                        │  State integrated)       │
  └──────────────────┴────────────────────────┴──────────────────────────┘

  → Bidirectional experience = CREATED by the brain, NOT by the receptor
  → Receptor: "TRPM8 is firing" (fact). Brain: "COLDER than baseline" (evaluation)
  → "Prediction-delta" = brain-level concept (does not exist at the receptor level)
  → The framework describes what happens from the brainstem upward — correct level
```

---

## §4 — BASELINE IS EMERGENT, NOT DESIGNED

### §4.1 — Machine zero vs Body zero

```
⭐ 2 FUNDAMENTALLY DIFFERENT KINDS OF "ZERO":

  MACHINE ZERO (designed):
    → 0°C = water freezes (defined by Celsius, universal)
    → 0V = no potential difference (defined by physics)
    → Fixed, universal, doesn't change
    → Created BY an engineer WITH a specification

  BODY ZERO (emergent):
    → 37°C = where warm-sensitive + cold-sensitive neurons fire BALANCED
    → Nobody "defined" 37°C — it happens to be where the system equilibrates
    → Adaptive, per-person, shifts over time
    → EMERGES from system dynamics, NOT designed
```

### §4.2 — Adaptive baseline

```
🟡 BODY BASELINE = ADAPTIVE ZERO — SHIFTS OVER TIME:

  ① HABITUATION: repetition → baseline shifts UP
    → Coffee every day → body compiles "having coffee" = new baseline
    → Day without coffee → deviation FROM NEW baseline → dissonance

  ② SNC (Successive Negative Contrast):
    → Baseline "already had something good" → downshift → overreact
    → 🟢 Crespi 1942, Flaherty 1996

  ③ COMPILATION depth:
    → Expert baseline DIFFERS from novice baseline (different compiled patterns)
    → Musician hears dissonance that a non-musician misses

  ④ PER-PERSON variation:
    → COMT genotype → dopamine clearance speed → different sensitivity baseline
    → DRD4 genotype → different novelty threshold
    → → "Zero" IS DIFFERENT per person

  → Machine: 1 thermometer = 1 zero, universal
  → Body: each channel × each person × each moment = DIFFERENT zero
  → → Brain MUST continuously RECALIBRATE zero
  → → Recalibration = compilation (learning new baseline)
```

---

## §5 — WHY EVALUATIVE LAYER MUST EXIST

```
⭐ EVALUATIVE LAYER = CONSEQUENCE OF EVOLUTIONARY CONSTRAINT:

  PROBLEM:
    Evolution CANNOT hardcode a zero-point (§1)
    → Sensors only report "threshold exceeded" — NOT "deviation from baseline"
    → Baseline = emergent (§4) — differs per person, shifts over time
    → → SOMETHING must figure out "what is MY baseline"
    → → SOMETHING must evaluate "how much deviation, in which direction"

  SOLUTION:
    BRAIN learns baseline through COMPILATION:
    → Experience → body-feedback → Hebbian → compiled pattern = learned baseline
    → New input → compare against compiled baseline → evaluate deviation
    → = EVALUATIVE PROCESSING

  THEREFORE:
    → Evaluative layer MUST exist
    → NOT an optional feature — it is the NECESSARY SOLUTION for "no hardcoded zero"
    → Compilable Architecture = the brain's answer to evolution's limitation

  DIRECT-STATE = what evolution CAN hardcode:
    → Nociception: tissue damage IS bad (no baseline needed — damage = always bad)
    → CT afferents: gentle touch IS pleasant (no baseline needed — CT pathway = always)
    → Hardware from birth — no baseline learning required
    → = THESE are what evolution can do WITHOUT compilation

  EVALUATIVE = what evolution CANNOT hardcode → brain must learn:
    → "Is morning coffee good?" → depends on MY compiled baseline
    → "Does being criticized by a parent hurt?" → depends on MY Entity-Compiled depth
    → "Is a company failure frightening?" → depends on MY career compilation
    → = THESE require LEARNED baseline → require Evaluative processing

  → Direct-State = evolution's DIRECT solution (hardcode what is universal)
  → Evaluative = evolution's INDIRECT solution (compile what is individual)
  → 2 types = NECESSARY, not accidental
```

---

## §6 — UNIVERSAL APPROACH/AVOID

### §6.1 — Bacteria → humans: same principle

```
⭐ ALL LIVING ORGANISMS NEED APPROACH/AVOID:

  ┌──────────────┬────────────┬──────────────────────────────────────┐
  │ Organism     │ Neurons    │ Mechanism                            │
  ├──────────────┼────────────┼──────────────────────────────────────┤
  │ E. coli      │ 0          │ Chemoreceptors on membrane           │
  │ (bacteria)   │            │ → swim toward glucose (approach)     │
  │              │            │ → tumble away from acid (avoid)      │
  │              │            │ = Direct chemical response           │
  │              │            │ 🟢 Berg & Brown 1972                  │
  ├──────────────┼────────────┼──────────────────────────────────────┤
  │ C. elegans   │ 302        │ Simple circuits                      │
  │ (worm)       │            │ → learned avoidance                  │
  │              │            │ → habituation (proto-compile!)       │
  │              │            │ 🟢 Rankin et al. 1990                 │
  ├──────────────┼────────────┼──────────────────────────────────────┤
  │ Drosophila   │ ~100K      │ Mushroom body (learning center)      │
  │ (fruit fly)  │            │ → conditioned preference/aversion    │
  │              │            │ → dopamine reward pathways           │
  │              │            │ 🟢 Waddell 2013                       │
  ├──────────────┼────────────┼──────────────────────────────────────┤
  │ Fish         │ ~10M       │ Pallium (proto-cortex)               │
  │              │            │ → learned fear, social hierarchy     │
  │              │            │ → opioid reward system               │
  ├──────────────┼────────────┼──────────────────────────────────────┤
  │ Dog/Cat      │ ~500M-2B   │ Cortex + limbic system               │
  │              │            │ → Social bonding, learned fear       │
  │              │            │ → E₀-E₂ (food pref, social eval)    │
  │              │            │ → Compilation: present but limited   │
  ├──────────────┼────────────┼──────────────────────────────────────┤
  │ Human        │ ~86B       │ Massive cortex + PFC                 │
  │              │            │ → E₀-E₃ (abstract, existential)     │
  │              │            │ → Compilation: DEEP (decades)        │
  │              │            │ → "A meaningless life" = E₃ only    │
  └──────────────┴────────────┴──────────────────────────────────────┘

  → Approach/avoid = UNIVERSAL across ALL life
  → NOT a feature of neurons — it is a feature of BEING ALIVE
  → Bacteria: chemical gradient. Worm: 302-neuron circuit.
  → Human: 86 billion neurons. SAME PRINCIPLE.
```

### §6.2 — Evaluative/Direct-State across the evolutionary spectrum

```
🟡 DIRECT-STATE = UNIVERSAL. EVALUATIVE = SCALES WITH COMPILATION:

  Bacteria: Direct-State only (chemical sensor → immediate response)
  Worm (302n): Direct-State + proto-Evaluative (habituation = basic baseline learning)
  Insects: Direct-State + E₀ (hardwired evaluation, mushroom body)
  Fish: Direct-State + E₀-E₁ (opioid pathway, learned preferences)
  Dogs/Cats: Direct-State + E₀-E₂ (social evaluation, entity recognition)
  Humans: Direct-State + E₀-E₃ (abstract, existential, decades of compilation)

  → Direct-State = evolutionary FLOOR — every organism with a nervous system has it
  → Evaluative = scales with COMPILATION CAPACITY
  → More neurons → more compilation → deeper Evaluative
    → more "types" of suffering AND reward
  → = Trade-off: Compilable Architecture = more adaptation BUT more vulnerability
  → = WHY humans "suffer from thoughts alone" (E₃ Evaluative Dissonance)
    and insects don't (only Direct-State)
```

---

## §7 — SYMMETRY = FUNCTIONAL REQUIREMENT

### §7.1 — Information theory argument

```
⭐ ONE-WAY SENSOR = ZERO USEFUL INFORMATION (Shannon 1948):

  A sensor that only signals "cool = pleasant" but NOT "hot = problem":
    → Outside in intense heat: NO signal
    → Stepping into a cool room: signal "pleasant"
    → BUT: without a signal for "hot" → no way to know cool DIFFERS from hot
    → → "Cool = pleasant" only means something IF "hot = uncomfortable" provides reference

  Information = requires CONTRAST:
    → Shannon: a signal that never changes = zero information
    → Signal goes only 1 direction = half information
    → Signal goes both directions = full information
    → → Body NEEDS bidirectional feedback for each channel

  → CANNOT have a reward channel WITHOUT a corresponding dissonance channel
  → CANNOT have a dissonance channel WITHOUT a corresponding reward channel
  → → 2 directions = functional REQUIREMENT, not coincidence
```

### §7.2 — Body needs a smooth improve/maintain/degrade axis

```
🟡 AN ORGANISM NEEDS 3 STATES FOR EACH PARAMETER:

  ┌──────────────┬───────────────────────────────────────┐
  │ State        │ Organism's need                       │
  ├──────────────┼───────────────────────────────────────┤
  │ IMPROVING    │ "Getting better" → continue behavior  │
  │ (approach)   │ = reward signal                       │
  ├──────────────┼───────────────────────────────────────┤
  │ MAINTAINING  │ "Stable" → stay the course            │
  │ (baseline)   │ = no signal / low signal              │
  ├──────────────┼───────────────────────────────────────┤
  │ DEGRADING    │ "Getting worse" → change behavior     │
  │ (avoid)      │ = dissonance signal                   │
  └──────────────┴───────────────────────────────────────┘

  Missing ANY state → system BREAKS:
    Only approach (reward only): doesn't know when degrading → dies from ignoring threats
    Only avoid (dissonance only): doesn't know when improving → cannot learn what works
    Only maintain (no feedback): zombie → no adaptation possible

  → ALL 3 states MUST exist for EVERY parameter
  → → Reward + dissonance MUST coexist for EVERY channel
  → → Architecture for reward MUST be symmetric with dissonance
    (because same channel, same sensors, same integration machinery)
```

### §7.3 — Why they share the SAME architecture

```
🟡 REWARD AND DISSONANCE USE THE SAME INFRASTRUCTURE:

  Same insula gradient: posterior → anterior (🟢 Craig 2002)
  Same ACC conflict monitoring (🟢 Botvinick 2004)
  Same evaluation machinery (anterior insula + OFC/vmPFC)

  WHY evolution did NOT create 2 separate systems:
    → 2 separate systems = 2× cost (double the neural machinery)
    → 2 separate systems = synchronization problem (need to coordinate 2 systems)
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
    Pain offset ≈ touch offset (when stimulus is removed)
    → Hardware: symmetric — because same mechanism, same receptor dynamics

  EVALUATIVE: STRONGLY ASYMMETRIC speed
    Threat detection: FAST (amygdala ~12ms, bypasses PFC)
    Reward evaluation: SLOW (5 Body-Feedback-Preconditions, PFC verifies)
    Threat clearance: SLOW (cortisol half-life 60-90 min)
    Reward deactivation: FAST (opioid off in seconds)

  WHY ASYMMETRIC IF SAME ARCHITECTURE:
    → Architecture = symmetric (same hardware, same integration)
    → TIMING = asymmetric (DIFFERENT evolutionary pressures)
    → Evolution TUNED speed independently for each direction:

    Miss threat (false negative) → DEATH → gene eliminated
    False alarm threat (false positive) → wastes energy → survives
    → → Threat detection: OPTIMIZED for SPEED (better wrong than slow)

    Miss reward (false negative) → missed opportunity → survives, finds another
    False alarm reward (false positive) → approaches danger → DEATH
    → → Reward evaluation: OPTIMIZED for ACCURACY (verify before approaching)

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
🟡 8 INSIGHTS MAP ONTO THE FRAMEWORK:

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
    = WHY SNC works: baseline CAN shift UP → downshift = overreact

  §5 (WHY Evaluative MUST exist) →
    Evaluative = brain's answer to "no hardcoded zero"
    Evaluative = compilation applied to baseline learning + deviation evaluation
    Compilable Architecture = ENABLES Evaluative layer
    = WHY insects (Hardwired Architecture) = Direct-State only

  §6 (universal approach/avoid) →
    Framework's body-feedback system = HUMAN VERSION of universal principle
    Same principle as bacteria chemotaxis — DIFFERENT depth
    E₀→E₃ = compilation depth gradient

  §7 (symmetry required) →
    Reward-Signal-Architecture + Dissonance-Signal-Architecture = 2 counterpart files = CORRECT
    Reward Evaluative/Direct-State ↔ Dissonance Evaluative/Direct-State
    = SAME architecture, different direction
    = Functional requirement, not coincidence

  §8 (asymmetric speed) →
    Asymmetry in EVALUATIVE (compiled = tunable), not Direct-State (hardware = fixed)
    = WHY "calming down" takes time (Evaluative clearance slow)
    = WHY 1 negative ruins a positive experience
      (Evaluative threat: fast-on, slow-off)
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
  → Bacteria chemotaxis — 🟢 Berg & Brown 1972
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

> *"Evolution had no engineer. No specification. No fixed zero-point.*
> *→ Forced to use multiple one-way sensors + brain integration.*
> *→ Brain must LEARN baseline = compilation = Evaluative layer.*
> *→ Evaluative layer MUST be bidirectional (reward + dissonance) because information theory.*
> *→ Architecture symmetric because shared infrastructure;*
>   *speed asymmetric because different survival cost.*
> *→ From bacteria to humans: same principle, different depth.*
> *→ The framework didn't 'design' this architecture — it DERIVED it from evolutionary constraints."*
