---
title: Compile-Taxonomy — 1 Engine + Modulator Configurations
version: 3.0
created: 2026-05-08
updated: 2026-06-01 (v3.0 — Architecture reframe: 1 Engine + 3 Modulators)
status: v3.0
scope: |
  ARCHITECTURE REFRAME: ALL compile = Exposure → Hebbian (1 Engine).
  3 Compile Types (Experience/Expertise/Trust) = labels for dominant modulator configurations.
  Trust = AMPLIFIER (gradient Level 0-5), NOT a GATE (binary).
  Multi-stream compile: Content/Value/Entity/Behavior run IN PARALLEL.
  Feedback loop: bidirectional; PFC→Entity-Valence = slow/costly; Entity-Valence→PFC = fast/free.
  3 Hardware Constraints + 6 Trade-offs + 4 Pathways (carried from v2.0).
  Sleep = offline maintenance system (details → Compile-Sleep.md v1.0).
  Evolutionary gradient: engine conserved, modulators accumulated.
  ~50 research citations. Built on v2.0 + 2 drill sessions (2026-06-01).
purpose: |
  v2.0 organized by OUTPUT (3 separate types — taxonomy-first).
  v3.0 organized by MECHANISM (1 engine + modulator configurations — mechanism-first).
  v2.0 was NOT wrong — patterns were correct. v3.0 = DEEPER layer: WHY the 3 types exist.
  Resolves contradiction: Chunk.md §2.3 "gate" vs Entity-Access "gradient."
  ADDS: architecture, multi-stream, feedback loop, evolutionary gradient.
  KEEPS: 3 hardware constraints, 6 trade-offs, 4 pathways, interactions.
parent: Chunk.md v3.0 (§2 compile mechanisms = foundation)
related: |
  Compile-Sleep.md v1.0 — Sleep Maintenance details (6 mechanisms)
  Body-Base.md v3.3 §4 — summary of 3 Compile Types (references this file)
  Collective-Body.md v2.1 §2 — 4 compile pathways × 3 levels
  PFC-Operations.md v1.3 — Hold/Suppress, PFC budget
  Chunk.md v3.0 §2 — 4 compile mechanisms + compile_rate formula
  Entity-Valence-Dynamics.md v1.1 — Structural/Current valence
  Entity-Access.md v1.2 §2 — gradient Level 0-5
  Valence-Propagation.md v4.1 §2 — Trust = valence meta-dimension
  Simulation-Engine.md v1.1 — PFC imagination substrate (Exposure-Deliberate)
  Background-Pattern.md v2.0 — accumulated gist, Exposure-Spontaneous
sources: |
  Compile-Taxonomy.md v2.0 — foundation (3 types, 4 pathways, 6 trade-offs)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Compile-Taxonomy — 1 Engine + Modulator Configurations

> **4 children "going to study math" — 4 DIFFERENT compile mechanisms.**
> **But ALL run on the SAME 1 ENGINE: Exposure → Hebbian.**
>
> The difference = which MODULATOR is dominant, NOT which engine is running.
> Experience = engine + minimal modulators (direct exposure).
> Trust = engine + Entity-Valence amplifier (Entity-Valence-dominant).
> Expertise = engine + PFC sustained hold (PFC-dominant).
>
> **"If you want your child to learn, first help them love the teacher."**
> (Vietnamese proverb: "Muốn con hay chữ thì yêu lấy thầy")
> = PFC invest → Entity-Valence compile → body auto-receptive → PFC freed.
> = Architecture in one proverb.
>
> This file: ARCHITECTURE underneath taxonomy. WHY the 3 types exist,
> why they interact, why they overlap.

---

## Table of Contents

- §0 — Position in the Framework
- §1 — Core Architecture: 1 Engine + 3 Modulators + Exposure Channels + Sleep
- §2 — Why the Brain Compiles Short: 3 Hardware Constraints
- §3 — Trust Reframe: Amplifier, Not Gate
- §4 — 3 Compile Types = Dominant Modulator Configurations
- §5 — Multi-Stream Compile: Content / Value / Entity / Behavior
- §6 — 4 Compile Pathways: Same Output, Different Mechanisms
- §7 — Feedback Loop: Bidirectional + Asymmetry
- §8 — 6 Trade-offs of Compile Short
- §9 — Interactions: Experience vs Trust, Chain Break, External Tools
- §10 — Evolutionary Gradient
- §11 — Edge Cases Verified (8+)
- §12 — Honest Assessment
- §13 — Cross-References

---

## §0 — Position in the Framework

```
⭐ THIS FILE = ARCHITECTURE UNDERNEATH THE COMPILE TAXONOMY:

  v2.0 (backup/Compile-Taxonomy-v2.0.md):
    Organized by OUTPUT — "3 separate types" (taxonomy-first).
    Described patterns CORRECTLY but did not explain WHY.

  v3.0 (this file):
    Organized by MECHANISM — "1 engine + modulator configurations."
    DEEPER layer: WHY the 3 types exist, interact, and overlap.

  Content IS THE SAME. Organizing principle IS DIFFERENT.
  v2.0 was NOT wrong — v3.0 = deeper understanding.


  POSITION IN FILE HIERARCHY:

    Chunk.md v3.0 §2 (4 compile mechanisms = foundation)
      → [this file] (architecture: 1 engine + modulators + taxonomy)
      → Compile-Sleep.md v1.0 (Sleep Maintenance details)

    Body-Base.md v3.3 §4 (summary) → [this file] (detail)
    Collective-Body.md v2.1 §2 (4 pathways × 3 levels) → [this file] (pathway details)
    PFC-Operations.md v1.3 §2 (Hold/Suppress) → [this file] §1.4 (PFC Modulation)

    Read Chunk.md §2 first → read this file → read Compile-Sleep.md.


  WHAT'S NEW IN v3.0:
    ① Architecture: 1 Engine + 3 Modulators + Exposure Channels + Sleep (§1)
    ② Trust = Amplifier not Gate (§3) — resolves Chunk.md §2.3 vs Entity-Access contradiction
    ③ Multi-Stream Compile (§5) — Content/Value/Entity/Behavior in parallel
    ④ Feedback Loop + Asymmetry (§7) — PFC→Entity-Valence slow, Entity-Valence→PFC fast
    ⑤ Evolutionary Gradient (§10) — engine conserved, modulators accumulated
    ⑥ Edge Cases verified (§11) — 8+ cases stress-tested
```

---

## §1 — Core Architecture: 1 Engine + 3 Modulators + Exposure Channels + Sleep

```
⭐⭐⭐ CORE THESIS:

  ALL compilation passes through ONE single pathway:

    EXPOSURE → HEBBIAN STRENGTHENING → COMPILED CHUNK

  There is no separate "trust compile mechanism."
  There is no separate "expertise compile mechanism."
  THERE IS ONLY 1 ENGINE. The 3 Compile Types = labels for dominant modulator configuration.


  6 CONVERGING OBSERVATIONS:

  ① compile_rate formula (Chunk.md v3.0 §2.2):
     compile_rate ≈ f(exposure × saliency × contingency
                      × peak_valence × multi_modal_richness)
     Exposure = FOUNDATIONAL parameter. The other 4 = QUALITY of exposure.

  ② 4 compile mechanisms (Chunk.md v3.0 §2.1) = 4 FORMS OF EXPOSURE:
     Repetition = repeated exposure. Emotional peak = extreme-intensity exposure.
     Multi-modal = multi-channel exposure. Sleep = offline replay exposure.
     There is NO mechanism outside of exposure.

  ③ "PFC does NOT compile" (PFC-Operations.md v1.3):
     PFC directs attention, holds, imagines, domain-checks, changes environment.
     ALL of these = create/direct exposure. NONE = compile.

  ④ "Imagination = real internal body experience":
     Imagine a lemon → real saliva. Imagine a dog bite → real heart rate.
     Same pathways, same molecules, different intensity.

  ⑤ A child forced to study (no trust) → STILL compiles the content:
     Trust is "closed" but body IS EXPOSED to content → content compiles.
     Trust does NOT gate content compile. Trust amplifies VALUE compile.

  ⑥ Hebbian = conserved across ALL species:
     Aplysia (Kandel 2000). Fish. Dogs (Pavlov 1927). Humans.
     Same engine. Only modulators differ.

  🟢 Hebbian learning: Hebb 1949
  🟢 LTP: Bliss & Lømo 1973
  🟢 Aplysia Hebbian: Kandel 2000
  🟡 "ALL compile = exposure" as unifying principle: framework synthesis
```

### §1.1 — Compile Engine: Exposure → Hebbian → Compile

```
🟢🟡 COMPILE ENGINE = THE SOLE COMPILE MECHANISM:

  ┌───────────────────────────────────────────────────────┐
  │                  COMPILE ENGINE                       │
  │                                                       │
  │  [Exposure] → [Neural Activation] → [Hebbian]        │
  │       ↓               ↓                 ↓             │
  │  Pattern reaches  Neurons fire      LTP/LTD           │
  │  the brain        together          strengthen/       │
  │                                     weaken            │
  │                          ↓                            │
  │                   [Compiled Chunk]                    │
  │                   (auto-fires when triggered)         │
  └───────────────────────────────────────────────────────┘

  The Compile Engine ALWAYS operates THE SAME WAY regardless of:
    Who provides the exposure (mother, teacher, self, reality)
    Where the exposure comes from (external, PFC imagination, spontaneous)
    Whether trust is present (trust only AMPLIFIES, does not change mechanism)
    Whether PFC is involved (PFC only DIRECTS; body still compiles)


  4 COMPILE MECHANISMS = 4 FORMS OF EXPOSURE (Chunk.md v3.0 §2.1):

  ┌────────────────┬──────────────────────┬─────────────────────────┐
  │ Mechanism      │ = Exposure form      │ Why it compiles         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ① Repetition   │ Many repeated        │ Co-fire many times      │
  │                │ exposures            │ → connections strengthen │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ② Emotional    │ EXTREME-intensity    │ Amygdala + NE → wire    │
  │    peak        │ exposure (once is    │ EXTREMELY FAST          │
  │                │ enough)              │                         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ③ Multi-modal  │ Exposure across MANY │ Cross-cortex co-fire    │
  │                │ channels at once     │ → richer binding        │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ④ Sleep        │ OFFLINE replay       │ Hippocampus replay      │
  │                │ exposure             │ → strengthen/prune      │
  └────────────────┴──────────────────────┴─────────────────────────┘


  NO SOURCE TAG = EVIDENCE FOR 1 ENGINE (Chunk.md v3.0 §1.1):

    Compiled chunks have NO tag indicating their origin.
    Chunks from experience = chunks from trust = chunks from PFC-directed exposure.
    = EQUAL in the body.
    WHY: because all pass through the SAME 1 engine (Hebbian LTP).
    Same product → same mechanism.

  🟢 Bliss & Lømo 1973 (LTP)
  🟢 Brown & Kulik 1977 (emotional peak)
  🟢 Stein & Meredith 1993 (multi-modal)
  🟢 Walker 2017 (sleep consolidation)
  🟢 Johnson et al. 1993 (source monitoring — no source tag)
  🟡 4 mechanisms = 4 exposure types: framework synthesis
```

### §1.2 — Entity-Valence Bias (automatic)

```
🟡🟢 ENTITY-VALENCE BIAS = AUTOMATIC VALENCE MODULATOR:

  Entity-Compiled per-entity:
    Structural Valence Profile × Trust dimension
    (Entity-Valence-Dynamics.md v1.1, Valence-Propagation.md v4.1 §2)


  2 MODULATION MODES:

    ① AMPLIFY COMPILE RATE (quality):
       Same exposure from a trusted entity → compiles STRONGER.
       Mother saying "fire is hot" = auditory + emotional contagion + coupling = RICH.
       Stranger saying "fire is hot" = auditory only = thin.
       Trust adds nothing MAGICAL — trust makes THE SAME external event
       produce RICHER internal exposure inside the body.

    ② BIAS EXPOSURE PROBABILITY (quantity):
       High entity-valence → body AUTO-ATTENDS that entity → MORE exposure.
       Low entity-valence → body AUTO-AVOIDS → LESS exposure.


  CHARACTERISTICS:
    AUTOMATIC: compiled, fires without PFC involvement
    COST ≈ 0: compiled patterns run for free
    FAST: fires in milliseconds (subcortical, pre-PFC)
    GRADIENT: Level 0-5 per entity (Entity-Access.md v1.2), NOT binary
    CAN OVERRIDE PFC: Entity-Valence → PFC (direct, fast)

  Trust = VALENCE META-DIMENSION (Valence-Propagation.md v4.1 §2):
    Trust is NOT a separate system.
    Trust = 1 dimension WITHIN the per-entity valence profile.
    Trust = MULTIPLIER for the entire profile.

  → Trust Reframe details: §3.

  🟢 Social learning modulated by trust: Bandura 1977
  🟢 Emotional contagion: Hatfield et al. 1994
  🟢 Amygdala/subcortical response ~100ms: established neuroscience
  🟡 Entity-Valence as exposure modulator: framework synthesis
```

### §1.3 — 3 Exposure Channels (parallel)

```
🟡🟢 EXPOSURE ARRIVES FROM 3 CHANNELS RUNNING IN PARALLEL:


  EXPOSURE-EXTERNAL (body-input from reality):
    Sensory exposure from environment: visual, auditory, tactile, olfactory, gustatory.
    + Social: facial expressions, prosody, gestures.
    + Actions: motor feedback, proprioception.
    = Body-Feedback-Mechanism.md v2.1 §1.2 ① Hardware/Sensory-Driven.
    CHARACTERISTICS: most MULTI-MODAL, domain-checked, DEEPEST compile.
    No PFC required. Available to ALL species.
    5 external install mechanisms (Chunk.md v3.0 §2.3) = variants of Exposure-External.

  EXPOSURE-DELIBERATE (PFC imagination/simulate):
    PFC actively creates internal exposure: imagine scenarios, mentally rehearse,
    run thought experiments, plan deliberately, recall with intention.
    = Simulation-Engine.md v1.1: Constructive Simulation.
    Body REACTS to imagination GENUINELY (saliva, heart rate, mild opioid).
    CHARACTERISTICS: flexible, PFC-controlled, accessible for abstract domains (math, physics, philosophy).
    LIMITS: less multi-modal rich than Exposure-External, self-referencing risk, PFC budget cost.
    Human-dominant (requires developed PFC).

  EXPOSURE-SPONTANEOUS (automatic chunk fire):
    Compiled chunks fire on their own (WITHOUT PFC direction):
    ① Background-Pattern continuous baseline (Background-Pattern.md v2.0)
    ② Spontaneous memory resurface (context trigger → old chunk fires)
    ③ Association chains (chunk A → chunk B → chunk C cascade)
    ④ Mind wandering (DMN activates → 30-50% of waking time)
    ⑤ Intrusive patterns (trauma replay, rumination — negative Exposure-Spontaneous)
    = Body-Feedback-Mechanism.md v2.1 §1.2 ② Pattern-Driven.
    CHARACTERISTICS: cost ≈ 0, self-reinforcing (strong → fires → stronger).
    REQUIRES compiled chunks (Exposure-Spontaneous is absent in newborns).


  3 CHANNELS × PARALLEL, VARIABLE RATIO:

  ┌─────────────────────────┬──────────┬───────────┬─────────────┐
  │ Situation               │ External │Deliberate │ Spontaneous │
  ├─────────────────────────┼──────────┼───────────┼─────────────┤
  │ 6-month-old playing     │ 90%      │  2%       │  8%         │
  │ Child forced to study   │ 60%      │  5%       │ 35%         │
  │ Student reading a book  │ 40%      │ 40%       │ 20%         │
  │ Expert thinking through │ 10%      │ 60%       │ 30%         │
  │ REM sleep               │  0%      │  0%       │100%         │
  └─────────────────────────┴──────────┴───────────┴─────────────┘
  (% = ILLUSTRATIVE ESTIMATES, NOT precise measurements.)


  PFC × EXPOSURE CHANNELS:
    PFC CAN amplify External (actively listen, go practice) + Deliberate (mentally rehearse, imagine).
    PFC CANNOT directly control Spontaneous (Background-Pattern fires automatically).
    PFC suppressing Spontaneous = PFC Modulation cost — CANNOT turn off the Spontaneous source.
    → PFC = DIRECTOR for External+Deliberate, RECEIVER for Spontaneous.

  External + Deliberate + Spontaneous → ALL feed into the SAME Compile Engine.
  Compile Engine does NOT distinguish source (Chunk.md v3.0 §1.1: NO SOURCE TAG).

  🟢 Mind wandering 30-50%: Smallwood & Schooler 2006
  🟢 Motor imagery → body response: Jeannerod 2001
  🟢 DMN activation: Raichle et al. 2001
  🟢 Ironic process (suppressing Spontaneous → rebound): Wegner 1987
  🟢 Input hypothesis: Krashen 1982
  🟡 3-channel parallel model: framework synthesis
```

### §1.4 — PFC Modulation: PFC Hold + Suppress (deliberate)

```
🟡🟢 PFC MODULATION = PFC OPERATIONS (PFC-Operations.md v1.3):


  2 OPERATIONS:

  HOLD = PFC Amplify
    Top-down signal → amplify target pattern → INCREASES exposure quality.
    CAN lead to compilation (Hold → repeat → Hebbian → automatic → PFC freed).
    Cost: ① PFC load (processing cost). Brain: dlPFC, FEF.

  SUPPRESS = PFC Inhibit
    Inhibitory signal → block output route.
    DECREASES exposure for a specific pattern.
    CANNOT compile "not X" (can only block, not build — Wegner 1987).
    Cost: ② Efference mismatch. Brain: rIFG, vlPFC.


  4 COMBINATIONS Hold × Suppress (PFC-Operations.md v1.3 §3):

    ① Hold only         → compile new (easiest path)
    ② Hold + Suppress   → override old + build new (double cost)
    ③ Suppress only     → block only, no replacement (ALWAYS fails)
    ④ Neither           → compiled auto-fire (PFC not involved)


  PFC = DIRECTOR, BODY = COMPILER:

    ❌ "PFC compiles" = WRONG (PFC does not compile)
    ✅ "PFC-directed body compile" = CORRECT

    PFC's 5 roles (PFC-Operations.md v1.3):
      ① Direct attention    ② Hold in working memory
      ③ Imagine/simulate    ④ Domain-check
      ⑤ Change environment
    EACH role = modulate exposure. NO role = compile.


  SPECIAL — PFC MODULATION = THE ONLY MODULATOR WITH COST:
    Entity-Valence Bias: cost ≈ 0 (compiled, automatic)
    PFC Modulation (Hold/Suppress): cost ① + ② (active, fatigable)
    PFC budget = finite → PFC Modulation is TEMPORARY
    Goal: Hold → compile → release (transfer to automatic)

  🟢 PFC Hold: Baddeley 2003, Miller & Cohen 2001
  🟢 PFC Suppress: Anderson & Green 2001, Aron 2007
  🟢 Suppress fails alone: Wegner 1987
  🟡 Hold/Suppress as PFC Modulation: framework synthesis


  ⭐ PREDICTION-DELTA AS ENABLING CONDITION FOR PFC MODULATION:

    Prediction-delta level determines which modulators are AVAILABLE:
      → High prediction-delta → VTA fires → dopamine → PFC Modulation ENABLED
        → Explicit Compilation Pathway available (+ Implicit still running)
      → Low/zero prediction-delta → VTA silent → PFC Modulation OFF
        → Implicit Compilation Pathway only (DEFAULT)

    = Prediction-delta is the ENABLING CONDITION for explicit pathway.
    = Implicit Pathway (Hebbian engine alone) = default, always running.
    = Explicit Pathway (engine + PFC Modulation) = additional when
      prediction-delta provides dopamine fuel.

    Trust Compile crosses BOTH pathways:
      → Value install = implicit (Entity-Valence dominant)
      → Content from trusted teacher = can be explicit (PFC holds)

    🟡 Prediction-delta → pathway selection = framework synthesis
    Cross-ref: Consciousness.md §7.3, Drill-Consciousness-Bridge.md §1
```

### §1.5 — Sleep Maintenance: Sleep Offline Maintenance

```
🟡🟢 SLEEP MAINTENANCE = SLEEP OFFLINE MAINTENANCE SYSTEM:

  Sleep is NOT simply the "4th exposure source."
  Sleep has 6 mechanisms — only ~1.5 are exposure-based; ~4.5 are optimization.

  ┌────┬──────────────────────┬─────────────┬──────────────────────┐
  │ #  │ Mechanism             │ Exposure?   │ Primary function     │
  ├────┼──────────────────────┼─────────────┼──────────────────────┤
  │  1 │ SHY Homeostasis       │ ❌ NOT      │ Prune weak (SNR)     │
  │  2 │ Hippocampal Replay    │ ✅ YES      │ Strengthen existing  │
  │  3 │ Active Consolidation  │ ❌ NOT      │ Transfer (RAM→ROM)   │
  │  4 │ Creative Linking      │ 🟡 PARTIAL  │ New remote links     │
  │  5 │ Emotional Decoupling  │ ❌ NOT      │ Strip emotional tag  │
  │  6 │ Gist Extraction       │ 🟡 PARTIAL  │ Abstract + generalize│
  └────┴──────────────────────┴─────────────┴──────────────────────┘

  Cycle: Waking (build) → Sleep (maintain) → Waking (build on maintained).

  → DETAILS: Compile-Sleep.md v1.0 (6 mechanisms, architecture interaction,
    sleep deprivation, waking rest comparison, ~40 citations).

  🟢 Multi-mechanism sleep model: Diekelmann & Born 2010
  🟡 Sleep Maintenance in compile architecture: framework synthesis
```

---

## §2 — Why the Brain Compiles Short: 3 Hardware Constraints

```
🟢🟡 3 INDEPENDENT CONSTRAINTS ALL POINT TOWARD SHORT COMPILE:


  ① PFC ~4±1 SLOTS = PHYSICS LIMIT:

     PFC-Hold-Dimensions.md §2: 6 INDEPENDENT forces converge at ~4:
       Combinatorics: marginal gain peaks at 3→4
       World structure: ~2-4 main causal variables per situation
       False positives: >4 dimensions → signal-to-noise COLLAPSE
       Interference: >4 → oscillations collide
       Energy: maintaining each dimension = processing load COST
       Evolution: no sufficient selection pressure for >4

     → Chain > 4 nodes = EXCEEDS single PFC processing capacity
     → = Hardware limit, NOT "laziness"

     🟢 Working memory ~4±1: Cowan 2001 (highly cited meta-analysis)


  ② PROCESSING SPEED: PFC ~200ms+, AMYGDALA ~12ms:

     PFC is ALWAYS slower than subcortical response.
     Long chain = PFC processes SLOWLY → body has ALREADY responded.
     Evolution favors FAST for survival.
     Short compile = faster = survival advantage.

     🟢 Amygdala response ~12ms: LeDoux 1996
     🟢 PFC response ~200ms+: established neuroscience


  ③ CORTISOL COST: LONG CHAIN = ACTIVE LOCK → SUSTAINED CORTISOL:

     PFC holding chunks → Active Lock → cortisol.
     Cortisol-Baseline.md v2.2: sustained cortisol → neural wear.
     Long chain → PFC holds LONGER → cortisol LONGER → biologically EXPENSIVE.
     Short compile → PFC holds LESS → less cortisol → biological savings.

     🟢 Cortisol + sustained cognitive load: Lupien et al. 2009


  ⭐ CONVERGENCE — 3 CONSTRAINTS POINT THE SAME DIRECTION:

    PFC capacity:      long chain = EXCEEDS limit
    Processing speed:  long chain = TOO SLOW
    Energy cost:       long chain = TOO EXPENSIVE
    → Brain IS FORCED to compile short = NOT a choice

    Analogy: the human eye has only 3 cone types (RGB).
    Light spectrum = continuous. But survival only NEEDS 3 axes.
    → PFC ~4 slots: survival causality only needs ~4 dimensions → no more needed.

  🟡 3-constraint convergence model: framework synthesis
  🟢 Components individually established (Cowan 2001, LeDoux 1996, Lupien 2009)
```

---

## §3 — Trust Reframe: Amplifier, Not Gate

### §3.1 — Contradiction detected

```
🟡 CONTRADICTION WITHIN THE FRAMEWORK:

  SOURCE 1 — Chunk.md v2.3 §2.3 (OLD text, already resolved → AMPLIFIER):
    "TRUST = GATE FOR EXTERNAL INSTALL"
    → Language of "gate" = BINARY (open/closed).

  SOURCE 2 — Entity-Access.md v1.2 §2:
    "gradient Level 0-5 per-entity"
    → Language of "gradient" = CONTINUOUS (0→1→2→3→4→5).

  SOURCE 3 — Child forced to study:
    Trust is "closed" (child doesn't believe studying is good).
    BUT content STILL compiles through forced exposure.
    → "Gate" = wrong for content compile.

  → "GATE" and "GRADIENT" contradict.
  → "GATE" and "content compiles without trust" contradict.
```

### §3.2 — Resolution: Amplifier model (Level 0-5)

```
🟡 TRUST = AMPLIFIER (GRADIENT), NOT A GATE (BINARY):

  ┌────────────┬──────────────────────────────────────┐
  │ Level 0    │ Multiplier ≈ 0 → compile rate        │
  │ (stranger) │ EXTREMELY LOW from this entity       │
  │            │ (LOOKS like gate = off)               │
  ├────────────┼──────────────────────────────────────┤
  │ Level 1    │ Multiplier low → needs MUCH MORE     │
  │ (acquaint) │ exposure to compensate               │
  ├────────────┼──────────────────────────────────────┤
  │ Level 2-3  │ Multiplier medium → normal           │
  │ (friend)   │ compile rate                         │
  ├────────────┼──────────────────────────────────────┤
  │ Level 4    │ Multiplier high → few exposures      │
  │ (partner)  │ still compile                        │
  ├────────────┼──────────────────────────────────────┤
  │ Level 5    │ Multiplier MAX → 1-2 exposures       │
  │ (self/     │ = deep compile                       │
  │  child)    │                                      │
  └────────────┴──────────────────────────────────────┘

  "Gate" = LIMIT CASE of the amplifier when multiplier → 0.
  Gate behavior IS CORRECT at Level 0. But NOT correct for the full spectrum.
  "Amplifier" encompasses BOTH gate behavior AND gradient behavior.

  VERIFICATION EXAMPLES:
    Mother says "keep studying" → trust Level 4-5 → few repetitions → compiles [study → good]
    Stranger says "you should train for career X" → trust Level 0-1 → needs MANY people saying it
    Close friend says "try jazz" → trust Level 2-3 → a few times + direct experience

  🟢 Entity-Access gradient Level 0-5: Entity-Access.md v1.2 §2
  🟢 Trust = valence meta-dimension: Valence-Propagation.md v4.1 §2
  🟡 Trust = amplifier (not gate): framework synthesis
```

### §3.3 — Trust scope: VALUE vs CONTENT

```
⭐ IMPORTANT DISTINCTION:

  ┌────────────────────┬────────────────────┬─────────────────────────┐
  │ Compile stream     │ Trust role         │ Example                 │
  ├────────────────────┼────────────────────┼─────────────────────────┤
  │ CONTENT compile    │ Does NOT amplify   │ Child is forced →       │
  │ (knowledge, skill) │ (exposure alone    │ still compiles math.    │
  │                    │ = sufficient for   │ No need to trust mom.   │
  │                    │ content)           │                         │
  ├────────────────────┼────────────────────┼─────────────────────────┤
  │ VALUE compile      │ AMPLIFIES          │ Mom says "studying is   │
  │ ([X → good/bad])   │ (trust = multiplier│ good" → trust mom →     │
  │                    │ for value install) │ compiles [study → good] │
  │                    │                    │ QUICKLY.                │
  ├────────────────────┼────────────────────┼─────────────────────────┤
  │ ENTITY compile     │ IS the trust weight│ The trust weight itself │
  │ (trust itself)     │ being compiled     │ = product of compile    │
  │                    │                    │ from direct experience. │
  └────────────────────┴────────────────────┴─────────────────────────┘

  ⭐ "GOOD AT IT BUT HATES STUDYING IT" = ARCHITECTURE PREDICTION:
    Content stream: compiled successfully (exposure → knowledge) ✓
    Value stream: compile failed (amplifier ≈ 0 for [study → good]) ✗
    → Has knowledge, DOES NOT have [study → good] value compiled.
    → Architecture predicts this. The "gate" model cannot.

  → Trust amplifies VALUE install, does NOT amplify content compile.
  → Multi-stream details: §5.

  🟡 Trust scope (Value vs Content): framework synthesis
  🟢 Hebbian indifferent to source: established neuroscience
```

---

## §4 — 3 Compile Types = Dominant Modulator Configurations

### §4.1 — Experience Compile: Compile Engine + Minimal Modulators

```
🟡🟢 EXPERIENCE COMPILE — DIRECT EXPOSURE → HEBBIAN → COMPILE:

  MODULATOR CONFIGURATION:
    Compile Engine: ✅ Full (Hebbian direct)
    Entity-Valence Bias: Minimal (direct verification; trust optional)
    Exposure: External dominant (body-input from reality)
    PFC Modulation: Minimal (body acts directly, PFC not needed)

  = "Engine alone" — modulators at background level.

  MECHANISM:
    [action → sensory result → body evaluation → compile]
    Body experiences directly → body self-wires → chunk forms.

  EXAMPLES:
    [give → recipient happy → warmth]     → compiled [giving → warmth]
    [touch fire → hot → pain]             → compiled [fire → avoid]
    [delicious food → opioid]             → compiled [this place → good]

  CHARACTERISTICS:
    ✅ STRONGEST: multi-modal (see + hear + touch + feel → wire deep)
    ✅ FASTEST: no PFC deliberation, amygdala ~12ms
    ❌ NARROW SCOPE: only compiles what has been DIRECTLY experienced

  ~90% of daily behavior = Experience-compiled patterns firing automatically.

  🟢 Hebbian learning: Hebb 1949
  🟢 Positive/negative reinforcement: Skinner 1953, Rescorla & Wagner 1972
  🟡 ~90% estimate: framework approximation
```

### §4.2 — Trust Compile: Compile Engine + Entity-Valence Bias Dominant

```
🟡 TRUST COMPILE — ENTITY-VALENCE AMPLIFIES VALUE INSTALL:

  MODULATOR CONFIGURATION:
    Compile Engine: ✅ Full (Hebbian — same engine)
    Entity-Valence Bias: ⭐ DOMINANT (trust = multiplier amplifying value)
    Exposure: External from trusted source
    PFC Modulation: Low (choosing who to trust + post-hoc confabulation)

  = "Engine + auto-turbo from Entity-Valence."

  MECHANISM:
    Trusted source → body receives input → compiles [action→result] SHORT.
    Long chain LIVES IN the collective (Level 2), NOT in the individual (Level 1).

  EXAMPLES:
    Child: trusts mother → compiles [study → good]
      Collective holds: [study → university → job → income → body-base feed]
    Language: trusts environment → compiles [word → meaning]
      Collective holds: [grammar system + vocabulary + pragmatics]

  5 TRUST SOURCE TYPES:
    ① Mother / caregiver: FOUNDATIONAL trust (Level 4-5)
    ② Teacher: DELEGATED trust (trust inherited via mother)
    ③ Community: CONSENSUS trust (social proof — Cialdini 1984)
    ④ Scripture / system: COMPILED trust (unfalsifiable)
    ⑤ Leader: COUPLING trust (Body-Coupling.md v3.0)

  CHARACTERISTICS:
    ✅ FAST: bypass chain verification through trust
    ✅ WIDE: access collective knowledge without individual experience
    ❌ COLLECTIVE-DEPENDENT: collective chain breaks → individual bears the cost
    ❌ EXPLOITABLE: trust wrong source → compiled wrong

  ⭐ TRUST COMPILE = MOST OF SOCIAL BEHAVIOR:
    Language, ethics, social skills, world knowledge, religious beliefs,
    political views, career expectations = ALL installed via Trust Compile.

  🟢 Cultural transmission: Boyd & Richerson 1985
  🟢 Social learning: Bandura 1977
  🟢 Social proof: Cialdini 1984
  🟡 Trust Compile dominance insight: framework synthesis
```

### §4.3 — Expertise Compile: Compile Engine + PFC Modulation Dominant

```
🟡🟢 EXPERTISE COMPILE — PFC-DIRECTED SUSTAINED EXPOSURE:

  MODULATOR CONFIGURATION:
    Compile Engine: ✅ Full (Hebbian — same engine)
    Entity-Valence Bias: Low (self-verify via Domain-Checked)
    Exposure: External + Deliberate balanced (practice + imagination)
    PFC Modulation: ⭐ DOMINANT (PFC sustained hold × years)

  = "Engine + manual turbo from PFC (costly, slow)."

  MECHANISM:
    Many repetitions of experience → chunks → meta-chunks → pyramidal compression.
    PFC DIRECTS attention across many years → subconscious compiles DEEP.

  EXAMPLES:
    Expert chess player: 50,000+ patterns → "feel" of the position
    Doctor with 20 years of experience: "one look at the patient and I know"
    Einstein: decades → E=mc² = 1 meta-chunk (inside = decades of compile)

  PFC DIRECTS via 5 roles (NOT one of which IS compile):
    ① Direct attention toward a specific domain
    ② Hold ~4 chunks active → co-fire → body wires
    ③ Imagine/simulate scenarios → body reacts + compiles
    ④ Domain-check: verify smooth against reality
    ⑤ Change environment → new body-input

  External tools EXTEND (Collective-Body.md v2.1 §3.3):
    PFC holds 4 → writes down → PFC freed → holds 4 more → STACK
    = "Level 2 Individual": paper, computer, database, AI

  CHARACTERISTICS:
    ✅ MOST ACCURATE: calibrated through domain feedback
    ❌ SLOWEST: requires YEARS in a single domain (Chase & Simon 1973: ~10 years)
    ❌ DOMAIN-SPECIFIC: Einstein = expert in physics + novice in cooking

  ~5% of behavior = when the individual operates WITHIN their expert domain.

  🟢 Expert chess 50,000+: Chase & Simon 1973
  🟢 Neural efficiency: Haier 1992, Neubauer & Fink 2009
  🟢 Deliberate practice ~10 years: Ericsson et al. 1993
  🟢 Extended mind: Clark & Chalmers 1998
  🟡 "PFC-directed body compile": framework terminology
```

### §4.4 — Comparison Table: 1 Engine + 3 Configurations

```
🟡 COMPARISON TABLE — 3 CONFIGURATIONS OF THE SAME 1 ENGINE:

  ┌──────────────────┬──────────┬──────────┬──────────────┬────────────┐
  │ COMPILE TYPE     │ Compile  │ Entity-  │ Exposure      │ PFC        │
  │                  │ Engine   │ Valence  │ Channels      │ Modulation │
  ├──────────────────┼──────────┼──────────┼──────────────┼────────────┤
  │ EXPERIENCE       │ ✅ Full   │ Minimal  │ External     │ Minimal    │
  │ (~90%)           │          │ (direct  │ dominant     │ (body      │
  │                  │          │ verify)  │              │ direct)    │
  ├──────────────────┼──────────┼──────────┼──────────────┼────────────┤
  │ TRUST            │ ✅ Full   │ ⭐ HIGH  │ External from│ Low        │
  │ (overlap)        │          │ (amplify │ trusted      │ (choose    │
  │                  │          │ value)   │ source       │ trust)     │
  ├──────────────────┼──────────┼──────────┼──────────────┼────────────┤
  │ EXPERTISE        │ ✅ Full   │ Low      │ External +   │ ⭐ HIGH    │
  │ (~5%)            │          │ (self-   │ Deliberate   │ (PFC       │
  │                  │          │ verify)  │ balanced     │ years)     │
  └──────────────────┴──────────┴──────────┴──────────────┴────────────┘

  COMPILE ENGINE = ALWAYS FULL. The difference = which MODULATOR is DOMINANT.

  ⚠️ IMPORTANT NOTE:
    ~90% + ~5% + Trust = do NOT add to 100% because they OVERLAP.
    The Experience/Trust boundary is NOT binary → it's a SPECTRUM.
    Example: [delicious food → warmth] = Experience (direct) + Trust (cultural "delicious").
    Most real-world compile = MIX of multiple modulators.

  WHY KEEPING THE 3 LABELS IS STILL USEFUL:
    "Experience" = shorthand for: engine dominant, direct exposure.
    "Trust" = shorthand for: Entity-Valence dominant.
    "Expertise" = shorthand for: PFC dominant.
    = Labels for DOMINANT configuration, not separate mechanisms.
    = Like "walking / running / climbing" = useful labels even though same mechanism.

  🟡 3 types as modulator configurations: framework synthesis
  🟡 Percentage estimates: framework approximation, not precise
```

---

## §5 — Multi-Stream Compile: Content / Value / Entity / Behavior

### §5.1 — 4 Streams running simultaneously

```
⭐⭐ EVERY SITUATION = MULTIPLE COMPILE STREAMS RUNNING SIMULTANEOUSLY:

  ┌───────────────┬─────────────────────┬────────────────────┐
  │ STREAM        │ WHAT COMPILES       │ DOMINANT MODULATOR │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ① CONTENT     │ Content, knowledge  │ Compile Engine only│
  │               │ Facts, skills       │ (Experience type)  │
  │               │ Procedures, data    │ Minimal modulators │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ② VALUE       │ Good/bad evaluation │ Entity-Valence     │
  │               │ Approach/avoid tag  │ Trust-amplified    │
  │               │ "Is this good?"     │                    │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ③ ENTITY      │ Entity-Valence      │ Entity-Valence     │
  │               │                     │ (update weights)   │
  │               │ Trust update        │ Per-entity compile │
  │               │ "Is this person     │                    │
  │               │  trustworthy?"      │                    │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ④ BEHAVIOR    │ Approach/avoidance  │ Direction-At-      │
  │               │ Motor-association   │ Compile            │
  │               │ Habit formation     │ (Chunk.md §2.4)    │
  │               │                     │ Valence direction  │
  └───────────────┴─────────────────────┴────────────────────┘

  Content stream ALWAYS = Experience Compile (Compile Engine, direct exposure).
  Value stream = Trust-modulated (Entity-Valence amplify/suppress).
  → "Trust Compile" = primarily VALUE stream (Entity-Valence-dominant), NOT content.
  → Content STILL compiles through Experience (Compile Engine alone).
```

### §5.2 — Test case: Child forced to study (4 streams visible)

```
🟡 TEST CASE — CHILD FORCED BY MOTHER TO STUDY MATH:

  ① Content:  [2+2=4], [multiplication], [formulas]
     → Compile Engine through Exposure-External (sitting reading a book) → compile ✓
     → Trust has NO effect (content = direct exposure)

  ② Value:    [study → fear of being scolded → avoid being scolded → "must do it"]
     → Compile Engine + context: threat direction → compile ✓ but AVOIDANCE
     → Trust for "study = good" does NOT compile ✗ (amplifier ≈ 0)

  ③ Entity:   [mother + coercion] → Entity-Valence updates
     → [mother] structural valence: mixed (love + coercion)
     → compile ✓ (direct experience)

  ④ Behavior: [listen to mother → sit down → open book]
     → Motor-association compile: avoidance-driven habit → compile ✓

  = 4 streams INDEPENDENT. 3/4 compile. 1/4 doesn't (value).
  = "Good at it but hates studying it" = ①✓ ②✗.
  = "Afraid of mother but doesn't love her" = ④✓ ③mixed.
```

### §5.3 — Test case: Student who loves the professor (4 streams positive)

```
🟡 TEST CASE — STUDENT WHO LOVES THE PROFESSOR AND THE SUBJECT:

  ① Content:  [theory], [methodology], [terminology]
     → Compile Engine through External (attending lectures) + Deliberate (working through problems) → compile ✓

  ② Value:    [this subject = interesting → approach]
     → Trust amplified: professor says "this part is important" → body amplifies → compile ✓

  ③ Entity:   [professor] → Entity-Valence STRENGTHENED positive
     → Trust increases → future value amplification INCREASES → compile ✓

  ④ Behavior: [arrive on time → sit in front row → ask questions]
     → Approach-driven habit → compile ✓

  = 4 streams ALL positive. = Ideal.
  = Approach direction → sustainable, low cortisol cost.
```

### §5.4 — Implication: Know which stream is failing

```
🟡 IMPLICATION:

  Educational intervention MUST identify WHICH STREAM is failing:
    Content ✗: need more exposure (time, practice)
    Value ✗: need to build trust FIRST (entity-valence toward teacher/subject)
    Entity ✗: need to fix the relationship (teacher-student dynamic)
    Behavior ✗: need to change direction (approach, not avoidance)

  Targeting the wrong stream → wrong intervention → "try harder" with no effect.

  🟡 4-stream multi-stream model: framework synthesis
  🟢 Hebbian concurrent: multiple patterns strengthen simultaneously
  🟢 Direction-At-Compile: Chunk.md v3.0 §2.4
```

---

## §6 — 4 Compile Pathways: Same Output, Different Mechanisms

```
🟡 4 PATHWAYS — TEST CASE: "4 CHILDREN GOING TO STUDY MATH":

  REALITY — 4 children, 4 DIFFERENT compile pathways:


  ① HARDWARE FIT (Experience Compile — direct, short):

     [math → brain fires → Goldilocks zone → VTA → opioid]
     = "Naturally finds it interesting." Level 1 direct.
     MODULATOR CONFIGURATION: Compile Engine + minimal Entity-Valence/PFC, External, novelty direction.
     Trust: NOT NEEDED. Chain length: 1 node.

     Novelty.md: Goldilocks zone = task difficulty ≈ current capacity
     → VTA fires → dopamine → body pursues → opioid
     → = Hardware fit, NOT "born talented"


  ② TRUST + MODERATE FIT (Trust + Experience — compound):

     Parents say "studying matters" → trust → compiles [study → good]
     + Studying by self → fits hardware → moderate cost → status
     = Level 1: [study → mom approves + grade + status → body warmth] (2 nodes)
     = Level 2: parents hold long chain [study → future → body-base feed]
     MODULATOR CONFIGURATION: Compile Engine + Entity-Valence + partial PFC, External.
     Trust: HIGH (parents). Verify: PARTIAL (direct experience confirms).

     → COMPOUND: Trust install + Experience confirm = EXTREMELY DURABLE.
     → = Most common? Many students = MIX of pathways ①②


  ③ SOCIAL DEFAULT (Trust Compile — installed pure):

     "Everyone studies → of course I do too"
     = Level 1: [everyone studies → normal → I should too] (1 node)
     MODULATOR CONFIGURATION: Compile Engine + Entity-Valence social proof, External, minimal PFC.
     Trust source: QUANTITY (social proof — Cialdini 1984).

     → Compile does NOT even require strong body experience
     → Just needs social environment → body auto-conforms


  ④ THREAT AVOIDANCE (Experience Compile — direct, short):

     [not studying → scolded / hit → threat → study to avoid it]
     = Level 1 direct. Chain length: 1-2 nodes.
     MODULATOR CONFIGURATION: Compile Engine + minimal Entity-Valence, External, threat direction.
     Trust: NOT NEEDED (direct threat experience).

     → Chunk.md v3.0 §2.4: threat direction → compile WITH avoidance
     → Cortisol-tagging: compiled [not studying → dangerous]


  ⭐ CONVERGENCE — 4 PATHWAYS, 1 OUTPUT:

     4 DIFFERENT pathways → same output: "goes to study"
     ALL compile SHORT at Level 1 (1-2 nodes)
     Long chain lives at Level 2 (collective)
     → Same engine. Different modulator configurations. Different direction.


  PRACTICAL VALUE OF 4 PATHWAYS:

    ① Understand why THE SAME behavior = DIFFERENT mechanism
       → Educational intervention MUST know which pathway the student follows
    ② Pathway ④ (threat) = compiles well but HIGH cortisol cost
    ③ Pathways ①② = more sustainable (approach direction)
    ④ Good education = creates conditions for pathways ①② instead of ④

  🟡 REWARD IMPLICATION (Reward-Signal-Architecture.md v2.1 §8.4):
    4 pathways → different Precondition-5 tags → different reward capacity in adulthood:
    ① Hardware Fit → approach tag → flow accessible
    ② Trust + moderate → depends on collective chain
    ③ Social Default → neutral tag → relief dominant
    ④ Threat Avoidance → avoidance tag → burnout trajectory

  🟡 4 compile pathways model: framework synthesis
  🟢 Social proof: Cialdini 1984
  🟢 Approach vs avoidance motivation: Elliot 2006
```

---

## §7 — Feedback Loop: Bidirectional + Asymmetry

### §7.1 — Interaction map: 10 paths

```
⭐⭐ THE COMPONENTS ARE NOT INDEPENDENT — THEY INTERACT BIDIRECTIONALLY:

  ┌───────────────────────────┬─────────────────────────────────────────────────────────┐
  │ Path                      │ Mechanism                                               │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ PFC → Entity-Valence      │ PFC creates positive exposure with entity               │
  │                           │ → compile → Entity-Valence updates (INDIRECT, SLOW)     │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Entity-Valence → PFC      │ Entity-Valence biases PFC attention (DIRECT, FAST)      │
  │                           │ Ex: hate teacher → body auto-rejects → PFC must         │
  │                           │ suppress → PFC fatigues → body wins                     │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ PFC → Exposure            │ PFC creates imagination (→Deliberate) or changes        │
  │                           │ environment (→External). PFC directs attention →         │
  │                           │ filters External salience.                               │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Exposure → PFC            │ Body-input (dissonance signals) can wake PFC.           │
  │                           │ Ex: stomach pain → PFC wakes → engages problem-solving  │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Entity-Valence → Exposure │ Entity-Valence biases exposure channel selection:       │
  │                           │ body auto-attends high-valence entity → more External   │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Entity-Valence → Engine   │ Entity-Valence amplifies compile RATE from that entity. │
  │                           │ Trust = multiplier. Same exposure → compiles STRONGER.  │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Engine → Entity-Valence   │ Compiled chunks update Entity-Valence profile.          │
  │                           │ Ex: newly learn teacher is brilliant → [teacher →       │
  │                           │ positive] increases                                     │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Engine → Exposure         │ Compiled patterns change salience filters +             │
  │                           │ material for Deliberate (imagination) + Spontaneous.    │
  ├───────────────────────────┼─────────────────────────────────────────────────────────┤
  │ Engine → PFC              │ Compiled expertise gives PFC better material.           │
  │                           │ Compiled pattern → PFC freed (Hold → auto).             │
  └───────────────────────────┴─────────────────────────────────────────────────────────┘

  = NOT hierarchy (top-down). = FEEDBACK SYSTEM (bidirectional loop).
  Every component influences every other component.

  🟡 Feedback system model: framework synthesis
```

### §7.2 — Critical Asymmetry: PFC→Entity-Valence slow/costly, Entity-Valence→PFC fast/free

```
⭐⭐ ASYMMETRY EXPLAINS MANY PHENOMENA:

  ┌──────────┬───────────────────────────┬────────────────────────────┐
  │          │ PFC → Entity-Valence      │ Entity-Valence → PFC       │
  ├──────────┼───────────────────────────┼────────────────────────────┤
  │ Speed    │ SLOW (weeks/months)       │ FAST (milliseconds)        │
  │ Cost     │ HIGH (PFC holds           │ LOW (compiled =            │
  │          │ continuously +            │ cost ≈ 0)                  │
  │          │ creates exposure)         │                            │
  │ Path     │ INDIRECT (PFC→Exposure→   │ DIRECT (Entity-Valence     │
  │          │ Engine→Entity-Valence)    │ → PFC)                     │
  │ Sustain  │ Durable IF compiled       │ Very durable (compiled)    │
  └──────────┴───────────────────────────┴────────────────────────────┘

  ANALOGY:
    Entity-Valence = "gravity" — always pulls toward the compiled direction.
    PFC = "rocket" — CAN escape, but USES FUEL.
    Fuel (PFC budget) = FINITE → must reach orbit (compile) before running out.
    If compiled in time → flies free. If fuel runs out first → falls back.

  IMPLICATIONS:
    → "Knowing but not doing" = PFC rocket ran out of fuel, Entity-Valence pulled back.
    → Therapy takes months = PFC→Entity-Valence indirect path.
    → Forced learning is unsustainable = PFC fights Entity-Valence continuously, PFC exhausted.
    → "Love the teacher" = invest PFC once → compile Entity-Valence → Entity-Valence runs free (§7.3).

  🟡 PFC→Entity-Valence vs Entity-Valence→PFC asymmetry: framework synthesis
  🟢 PFC slower than subcortical: LeDoux 1996
  🟢 PFC budget finite: PFC-Operations.md v1.3 §8
  🟢 CBT mechanism = gradual recompilation: Beck 1979, Foa & Kozak 1986
```

### §7.3 — Virtuous loop: "Love the teacher → learn the lesson"

```
⭐ PROVERB = ARCHITECTURE IN ONE SENTENCE:
  "If you want your child to learn, first help them love the teacher."

  Step 1: PFC frames [teacher → trying to help me]
          → PFC: Hold positive frame. Cost: ① PFC load (initial investment).

  Step 2: PFC directs positive interactions
          → PFC → External: create positive body-input with teacher
          (engage, participate, express gratitude)

  Step 3: Body experiences positive interactions
          → External → Compile Engine: exposure → Hebbian → compile [teacher → positive]
          Multi-modal: see face + hear voice + feel warmth.

  Step 4: Entity-Valence [teacher] INCREASES
          → Engine → Entity-Valence: compiled chunks update entity-valence profile.

  Step 5: Body AUTO-RECEPTIVE to teacher's knowledge
          → Entity-Valence → Engine: amplifies ALL exposure from teacher.
          Same lesson → compiles DEEPER (trust = multiplier).

  Step 6: Knowledge compiles FASTER
          → Engine output: content chunks accumulate faster.

  Step 7: PFC FREED
          → Entity-Valence runs automatically (compiled, cost ≈ 0)
          → PFC budget available for other tasks. SUSTAINABLE.

  = VIRTUOUS LOOP: invest PFC → compile Entity-Valence → Entity-Valence runs free → PFC freed.

  "Love the teacher" = build Entity-Valence toward entity target
  "Want your child to learn" = PFC intention initiates the process
  "Learn" = content compile amplified by Entity-Valence
  Sequence: PFC invest (want) → Entity-Valence compile (love) → content amplified (learn)

  🟡 Proverb as virtuous loop illustration: framework synthesis
  🟢 Positive teacher-student relationship → learning: established
  🟢 Emotional context affects learning: Immordino-Yang & Damasio 2007
```

### §7.4 — Vicious loop: "Hate the teacher"

```
🟡 REVERSE — "HATE THE TEACHER → AUTOMATIC REJECTION":

  Step 1: Entity-Valence [teacher → negative] compiled
          (past: scolded, humiliated, treated unfairly) → Entity-Valence negative.

  Step 2: Teacher speaks → Entity-Valence ATTENUATES exposure
          Body auto-filters: reduces attention, reduces receptivity.
          Same lesson → compiles WEAKER (trust = near-zero multiplier).

  Step 3: PFC tries to override → Suppress negative entity-valence
          PFC Suppress: cost ② efference mismatch. PFC-Operations.md v1.3 §2.2.

  Step 4: PFC fatigues → releases → Entity-Valence reasserts
          Entity-Valence compiled, automatic, fast → body rejects teacher's input AGAIN.

  Step 5: Less compile → fall behind → more frustration → Entity-Valence MORE negative
          "Hate teacher → fail subject → hate more" = VICIOUS self-reinforcing loop.

  Step 6: BREAKING THE LOOP — MUST inject positive Exposure-External:
          → Replace teacher (new entity, reset Entity-Valence to neutral)
          → Old teacher changes approach (create new positive External exposure)
          → Third party mediates (context for positive interaction)
          → BUT: old Entity-Valence is NEVER deleted, only competitive re-linking (Chunk.md §2.5)

  🟡 Vicious loop model: framework synthesis
  🟢 Ironic rebound: Wegner 1987
```

---

## §8 — 6 Trade-offs of Compile Short

```
🟡 COMPILE SHORT = DOMINANT MODE AND HAS 6 CLEAR TRADE-OFFS:


  T1 — FAST BUT EASY TO DECEIVE (trust wrong source):

    Short compile + trust = bypass verification.
    High trust amplifier → body acts on trust without verifying.
    → If source is WRONG → compiled WRONG → body acts on a wrong pattern.

    Examples:
      Parents: "women don't need higher education" → trust → compile DEEP
        → At 30: body compiled [education = not needed] → HARD to change
      Cult: install chain through trust → compile DEEP → weaponized trust

    Root cause: High trust amplifier = bypass verification.
    Correct trust → correct compile → savings. Wrong trust → expensive.

    🟢 Cult persuasion: Cialdini 2006


  T2 — PFC CANNOT SELF-CORRECT (confabulation):

    PFC explains post-hoc → label ≠ mechanism → fix applied in WRONG PLACE → loop persists.

    Examples:
      "Why did I marry this person?" (marriage stress)
        PFC: "was manipulated" / ACTUAL: body compiled [partner → warmth] from experience
        Context changed → pattern doesn't MATCH → confused

    ⭐ This trade-off ONLY REVEALS ITSELF when context changes or chain breaks.
    When everything is smooth → trade-off is INVISIBLE.

    🟢 Confabulation: Nisbett & Wilson 1977


  T3 — COMPILED PATTERN MORE DURABLE THAN CONTEXT (lag):

    Compile = Hebbian LTP → CANNOT be deleted (Chunk.md §2.5).
    Context changes FAST → compiled pattern changes SLOWLY → LAG.

    Examples:
      HTML deeply compiled → HTML becomes obsolete → body STILL fires "I'm good at HTML"
      After a breakup → body STILL fires [evening → call partner] → Chunk-Miss

    Root cause: chunks have NO active "unwiring" mechanism.
    "Breaking old habits" = NEW chunk compiles STRONG ENOUGH → OVERRIDES old chunk.


  T4 — "WHY DID I DO THAT?" = NO SINGLE CORRECT ANSWER:

    Body compiles as compound (many sources), PFC does NOT tag source → confabulation.

    Examples:
      "Why do I want to have children?"
        PFC: "instinct" / ACTUAL: hormones + collective + Structural-Valence
        + identity + meaning = COMPOUND → PFC picks one → MISSES the compound

    Root cause: NO SOURCE TAG (Chunk.md §1.1) + confabulation.


  T5 — COLLECTIVE-DEPENDENT (collective breaks → individual bears the cost):

    Trust Compile = individual SHORT + collective LONG.
    → When collective chain BREAKS → individual suffers WITHOUT KNOWING WHY.

    Examples:
      AI disruption: [field X → job X] BREAKS → "what am I studying for?"
        Chain breaks at collective level, NOT the individual's fault.
        PFC usually blames SELF (because PFC only sees Level 1).

    Root cause: Trust Compile = individual does NOT hold chain → does NOT know where it broke.


  T6 — "KNOWING BUT NOT DOING" (PFC logic ≠ compiled pattern):

    PFC chains logic "should do X" →
    BUT body compiled [NOT X → comfortable] (Experience Compile).

    Examples:
      "Know I should exercise" → body: compiled [morning → sleep → comfortable]
        PFC chain = TRUST (installed). Body = EXPERIENCE (direct).
        EXPERIENCE wins (multi-modal, direct > verbal install).

    Root cause: 2 Compile Types competing. Experience > Trust in most cases.
    = Asymmetry §7.2: Experience compile = Entity-Valence self (Level 5 multiplier).
      Trust compile = Entity-Valence external (Level 2-3 multiplier). Self > external.
    → INTERVENTION: shift from TRUST → EXPERIENCE (direct experience).
    → Ex: want to exercise → GO EXERCISE → body compiles [exercise → warmth] → overrides.


  ⭐ 6 TRADE-OFFS = NOT A BUG, BUT A FEATURE:

    Short compile + trust = OPTIMAL for survival environment:
      Fast (ms, not days). Wide (access collective). Cheap (low cortisol).

    Trade-offs = THE PRICE OF OPTIMIZATION:
      T1: fast → easy to deceive
      T2: automatic → hard to self-correct
      T3: durable → lag when context changes
      T4: compound → PFC confused
      T5: dependent → collective breaks = individual bears it
      T6: Experience > Trust → "knowing but not doing"

    → Evolution MAXIMIZES survival probability, does NOT minimize trade-offs.

  🟡 6 trade-offs framework: drill synthesis
  🟢 Components individually established (see references above)
```

---

## §9 — Interactions: Experience vs Trust, Chain Break, External Tools

### §9.1 — Experience vs Trust: Competition, synergy, override

```
🟡 EXPERIENCE × TRUST INTERACTIONS:


  ⭐ SYNERGY — when Experience confirms Trust:

    Trust installs [study → good] + Experience confirms [study → mom approves → warmth]
    = COMPOUND STRONG. Both configurations aligned → pattern extremely durable.
    = "Educated + enjoys it" case. Ideal.


  ⭐ COMPETITION — when Experience contradicts Trust:

    Trust installs [alcohol → bad] + Experience compiles [alcohol → fun → warmth]
    = Competing chains → STRONGER chain wins (Valence-Propagation.md v4.1 §5).
    Experience usually wins (multi-modal, direct > verbal install).
    = "Knows alcohol is bad but still drinks."


  ⭐ TRUST OVERRIDES EXPERIENCE — rare but does happen:

    Condition: Trust install VERY DEEP + Experience compile SHALLOW.
    Ex: Strong religious prohibition (deep trust + community reinforces + repeated)
      → Body compiled [alcohol → sin] EXTREMELY DEEP over MANY YEARS
      → Direct experience [alcohol → fun] = once → SHALLOW → Trust wins.

    → Trust overriding Experience REQUIRES: deep trust + repetition + emotional reinforcement.
    → = Why education + culture CAN work, but needs TIME + INTENSITY.


  ⭐ OVERLAPPING — blurred boundaries:

    [delicious food → warmth] = Experience (direct) + Trust (cultural "delicious").
    → Most adult behavior = Experience × Trust overlap, NOT purely 1 type.

  🟡 Experience × Trust interaction dynamics: framework synthesis
```

### §9.2 — Chain Break: Collective breaks, individual detects

```
🟡 WHEN THE COLLECTIVE CHAIN BREAKS — BODY DETECTS BEFORE PFC:

  Collective chain: [study → university → job → income → body-base feed]
  Individual compile: [study → good] (Trust Compile SHORT)

  PFC does NOT spontaneously think "the chain broke."
  BODY circuit-breaks FIRST → PFC wakes AFTER (Body-Base.md v3.3 §7).


  ① COST INCREASES:
     Baseline compiled = "study → reasonable"
     New reality = "study → exhausted" → cost >> baseline
     Body-Feedback-Mechanism.md v2.1 §3 Chunk-Miss:
     VTA negative delta → dissonance signal.

  ② LINK BREAKS:
     Collective chain BREAKS at [university → GOOD job]
     Trust collapse → entire chain AFFECTED
     "Studying is pointless" = chain broken → valence of "study" FLIPS negative.

  ③ COMPOUND:
     Cost INCREASES + link BREAKS + trust COLLAPSES
     = Body-Feedback-Mechanism.md v2.1 §4 COMPOUND
     → PFC wakes STRONGLY → "what am I studying for?" = PFC RE-EVALUATES

  ⭐ KEY INSIGHT:
    "What am I studying for?" is NOT PFC spontaneously doing philosophical reflection.
    = Collective chain BREAKS → body DETECTS → PFC engages.
    Individual doesn't know WHERE the chain broke (because they don't hold the chain).
    → PFC usually blames SELF instead of detecting collective chain break.

  🟡 Chain break detection model: framework synthesis
  🟢 Circuit breaker concept: established neuroscience (NE α1 disconnect)
```

### §9.3 — Expertise × External Tools: Level 2 Individual

```
🟡 EXPERTISE COMPILE EXTENDS THROUGH EXTERNAL TOOLS:

  THE EINSTEIN MODEL:

    ① WRITE DOWN = external memory
       PFC holds 4 → writes down → PFC freed → holds 4 more
    ② TRUST PAST SELF
       "Formula X I already verified" → trust tag → build on top
    ③ ITERATIVE RECURSIVE
       Verify A → trust A → build B → verify B → trust B → stack
    ④ SLEEP CONSOLIDATES between steps

  HIERARCHY:
    PFC 4±1 (hardware limit)
    → ×4 pyramidal compression (subconscious — Valence-Propagation.md v4.1 §5b)
    → ×∞ external tools (paper, computer, database, AI)

  → External tools = "Level 2 Individual" (Collective-Body.md v2.1 §3.3)
  → EXTENDS individual compile BEYOND hardware limit

  🟢 Extended mind thesis: Clark & Chalmers 1998
  🟢 Epistemic actions: Kirsh & Maglio 1994
  🟡 "Level 2 Individual": framework synthesis
```

---

## §10 — Evolutionary Gradient

```
⭐ MODULATORS WERE ADDED THROUGH EVOLUTION — ENGINE CONSERVED:


  ┌──────────────┬──────────┬──────────────┬───────────┬──────────────┐
  │ Species      │ Compile  │ Exposure     │ Entity-   │ PFC          │
  │              │ Engine   │ Channels     │ Valence   │ Modulation   │
  ├──────────────┼──────────┼──────────────┼───────────┼──────────────┤
  │ Aplysia      │ Hebbian  │ External     │ ✗         │ ✗            │
  │ (sea slug)   │ basic    │ only         │           │              │
  │              │          │ (tactile)    │           │              │
  ├──────────────┼──────────┼──────────────┼───────────┼──────────────┤
  │ Fish,        │ Hebbian  │ External     │ Basic     │ ✗ minimal    │
  │ reptiles     │          │ (multi-      │ (friend/  │              │
  │              │          │ sensory)     │ foe)      │              │
  ├──────────────┼──────────┼──────────────┼───────────┼──────────────┤
  │ Dogs, cats   │ Hebbian  │ External +   │ Basic     │ Limited      │
  │ (social      │          │ Spontaneous  │ (attach-  │ (inhibitory) │
  │ mammals)     │          │ basic        │ ment)     │              │
  ├──────────────┼──────────┼──────────────┼───────────┼──────────────┤
  │ Primates     │ Hebbian  │ External +   │ Rich      │ Moderate     │
  │              │          │ Spontaneous  │ (social   │ (planning)   │
  │              │          │ + Deliberate │ complex)  │              │
  │              │          │ basic        │           │              │
  ├──────────────┼──────────┼──────────────┼───────────┼──────────────┤
  │ Humans       │ Hebbian  │ External +   │ Full      │ Full         │
  │              │          │ Deliberate + │ (Entity-  │ (5 roles,    │
  │              │          │ Spontaneous  │ Compiled, │ Simulation-  │
  │              │          │ FULL         │ Level 0-5)│ Engine)      │
  │              │          │ (imagine,    │           │              │
  │              │          │ tools, AI)   │           │              │
  └──────────────┴──────────┴──────────────┴───────────┴──────────────┘


  PATTERN:
    Compile Engine (Hebbian) = CONSERVED from Aplysia → humans.
    Evolution ADDED modulators + Exposure Channels, did NOT change the engine.
    EACH STEP = ADD A MODULATOR, NOT CHANGE THE ENGINE.

  IMPLICATIONS:
    ① Dog training = pure Compile Engine + minimal Entity-Valence (repetition × reward).
    ② Human education = Compile Engine + Entity-Valence + Deliberate + PFC (MORE COMPLEX, MORE POWERFUL).
    ③ Compilable Architecture (Body-Base.md v3.3 §2):
       = Compile Engine + full modulator suite → CAN learn ANYTHING (general-purpose).
       BUT: no pre-wired content → requires 15-20 years to calibrate.

  🟢 Aplysia Hebbian: Kandel 2000
  🟢 PFC evolution: Semendeferi et al. 2002
  🟢 Attachment system in mammals: Bowlby 1969
  🟡 Modulator additive evolution model: framework synthesis
```

---

## §11 — Edge Cases Verified (8+)

```
⭐ 8 EDGE CASES — ALL CONSISTENT WITH ARCHITECTURE:


  ① TRAUMA (emotional peak):
     Compile Engine: 1 exposure × EXTREME peak_valence → immediate compile.
     Exposure: External. Entity-Valence: [dog] flips negative instantly. PFC: BYPASSED (~12ms).
     → Compile Engine compiles WITHOUT PFC Modulation.
     🟢 LeDoux 1996

  ② CULT (Entity-Valence overrides PFC):
     Compile Engine: multi-modal + emotional peak + repetition → deep compile.
     Entity-Valence: [leader → positive++++] = DOMINANT. PFC: WEAKENED.
     → Entity-Valence maximized + PFC minimized + Exposure enriched = deep install.
     🟢 Cialdini 2006

  ③ THERAPY (PFC-guided recompile):
     Compile Engine: new exposure (Deliberate imagination + controlled External exposure).
     PFC: Holds new frame. Entity-Valence: gradually UPDATES (indirect PFC → Entity-Valence).
     → Reconsolidation window: recall → modify → re-compile.
     🟢 Foa & Kozak 1986, Nader 2000

  ④ CHILD FORCED TO STUDY (multi-stream):
     Content compile ✓ (Compile Engine + forced External). Value ✗ (trust ≈ 0).
     Entity: mixed. Behavior: avoidance habit ✓.
     → Multi-stream: content STILL compiles even with low trust.

  ⑤ "KNOWING BUT NOT DOING":
     Trust value installed thinly. Experience compiled deeply.
     Compile Engine products COMPETE: Experience > Trust.
     → Compile DEPTH difference + Entity-Valence asymmetry (self > external).
     🟢 Elliot 2006

  ⑥ IMMERSION LANGUAGE LEARNING:
     Compile Engine: massive External exposure. Entity-Valence: minimal. PFC: moderate.
     → Pure Compile Engine + External = immersion learning (slow but DEEP).
     🟢 Krashen 1982

  ⑦ EXPERT BLIND SPOT:
     Expert: decades of PFC-compiled → pyramidal compression → "sees 4."
     Novice: not yet compiled → needs External + Deliberate + time.
     → Trust amplifies VALUE, does NOT amplify CONTENT (§3.3).

  ⑧ "LOVE THE TEACHER" (full feedback cycle):
     PFC invests → positive External → Engine compiles → Entity-Valence updates
     → Entity-Valence auto → PFC freed.
     = Virtuous loop (§7.3). PFC one-time cost → permanent benefit.


  8/8 CASES CONSISTENT.
  Architecture explains EVERYTHING the 3-type taxonomy explains,
  PLUS explains additional cases the taxonomy could NOT clearly explain:
    → "Good at it but hates studying it" (multi-stream: content ✓ value ✗)
    → "Knowing but not doing" (compile depth + Entity-Valence asymmetry)
    → Immersion > classroom (source richness > PFC effort)

  🟡 Edge case stress-testing: framework synthesis
  🟢 Individual cases: citations listed per case above
```

---

## §12 — Honest Assessment

```
🟢 ESTABLISHED (strong research support):

  Hebbian learning / LTP: Hebb 1949, Bliss & Lømo 1973
  PFC ~4±1 working memory: Cowan 2001
  PFC response slower than subcortical: LeDoux 1996
  Cortisol cost of sustained load: Lupien 2009
  Expert patterns 50,000+: Chase & Simon 1973
  Neural efficiency (experts fire less): Haier 1992, Neubauer & Fink 2009
  Deliberate practice ~10 years: Ericsson 1993
  No chunk deletion / reconsolidation: Nader 2000
  Confabulation: Nisbett & Wilson 1977
  Social proof: Cialdini 1984
  Cultural transmission: Boyd & Richerson 1985
  Social learning: Bandura 1977
  Extended mind: Clark & Chalmers 1998
  PFC Hold/Suppress: Miller & Cohen 2001, Baddeley 2003, Aron 2007
  Suppress → rebound: Wegner 1987
  Sleep multi-mechanism: Diekelmann & Born 2010
  Aplysia Hebbian conserved: Kandel 2000
  Motor imagery → body response: Jeannerod 2001
  Emotional context → learning: Immordino-Yang & Damasio 2007


🟡 FRAMEWORK SYNTHESIS (logic consistent, based on established research):

  "1 Engine + 3 Modulators" unification:
    Components individually established. Architecture = synthesis.
    TESTABLE: predict content compiles without trust → measurable.

  Trust = AMPLIFIER (not GATE):
    Resolves internal contradiction (gate vs gradient Level 0-5).
    TESTABLE: measure compile rate at different trust levels.

  Multi-stream compile (4 streams):
    Novel concept. Components individually recognized.
    TESTABLE: "good at it but hates studying it" = content ✓ value ✗.

  3 Compile Types = dominant modulator:
    Novel reframe. Preserves existing taxonomy. Adds architecture.

  PFC→Entity-Valence slow/costly vs Entity-Valence→PFC fast/free asymmetry:
    Consistent with established PFC/subcortical speed differences.

  Evolutionary gradient (engine conserved, modulators added):
    Consistent with comparative neuroscience.

  PFC accuracy per pathway (§6):
    Speculative estimates. Needs testing.


🔴 NEEDS MORE RESEARCH:

  Precise % breakdown across 3 Compile Types
  Quantitative trust amplifier weights (Level 0-5 = what multiplier?)
  Multi-stream resource competition (independent or shared?)
  Cross-cultural variation in 4 compile pathways
  Whether Trust → Experience conversion rate is measurable
  Neural signature differences between 3 Compile Types
  Compile_rate formula mathematical form (multiplicative? additive?)
```

---

## §13 — Cross-References

### §13.1 — Framework files referenced

```
COMPILE ARCHITECTURE:
  Compile-Sleep.md v1.0 — Sleep Maintenance details (6 mechanisms)
  Chunk.md v3.0 §2 — 4 compile mechanisms, compile_rate formula, trust, no source tag
  PFC-Operations.md v1.3 — Hold/Suppress, 4 combinations, PFC budget
  Entity-Valence-Dynamics.md v1.1 — Structural/Current valence, trust meta-dimension
  Entity-Access.md v1.2 §2 — gradient Level 0-5 (supports amplifier model)
  Simulation-Engine.md v1.1 — PFC imagination substrate (Exposure-Deliberate)
  Background-Pattern.md v2.0 — accumulated gist (Exposure-Spontaneous)

BODY-BASE + BODY-FEEDBACK:
  Body-Base.md v3.3 §2 — Compilable Architecture, §4 summary, §7 circuit breaker
  Body-Feedback-Mechanism.md v2.1 — 2 sources, Chunk-Miss, Compound dynamics
  Cortisol-Baseline.md v2.2 — sustained cortisol → neural wear
  Why-Body-Knows.md v1.2 — 2-tier calibration
  Body-Coupling.md v3.0 — entity coupling mechanism

VALENCE + REWARD:
  Valence-Propagation.md v4.1 §2 — trust = valence meta-dimension
  Reward-Signal-Architecture.md v2.1 §8.4 — 4-Pathway × Precondition-5

COLLECTIVE + OBSERVATION:
  Collective-Body.md v2.1 §2 — 4 compile pathways × 3 levels, §3.3 external tools
  Meaning.md v2.0 — Anchor disrupted = T5 chain break × identity
  Religion.md v2.6 §2.1 — External inject bypasses PFC = Trust mechanism
  Status.md v2.0 — Resource Access Map = Experience (evolutionary direct)

PFC DETAIL:
  PFC-Hold-Dimensions.md — 6 forces converging at 4±1
  PFC-Hardware.md — Individual variance (COMT, DRD4, NE)
  PFC-Function.md v1.2 — 24 PFC functions
  Inter-Body-Mechanism.md v2.1 — Compilable Architecture, 3-Layer Evolution
```

### §13.2 — Research citations

```
ESTABLISHED (🟢):

  CORE NEUROSCIENCE:
  Hebb 1949 — Hebbian learning
  Bliss & Lømo 1973 — LTP discovery
  Dudek & Bear 1992 — LTD
  Kandel 2000 — Aplysia universal Hebbian
  Nader 2000 — Reconsolidation
  McGaugh 2004 — Emotional arousal enhances consolidation

  PFC + WORKING MEMORY:
  Cowan 2001 — Working memory ~4±1
  LeDoux 1996 — Amygdala fast pathway
  Miller & Cohen 2001 — PFC top-down attentional control
  Baddeley 2003 — Working memory model
  Curtis & D'Esposito 2003 — PFC sustained firing
  Anderson & Green 2001 — Think/No-Think paradigm
  Aron 2007 — rIFG inhibitory control
  Arnsten 2009 — PFC impaired under stress
  Lupien et al. 2009 — Cortisol + cognitive load

  LEARNING + MEMORY:
  Brown & Kulik 1977 — Flashbulb memories
  Skinner 1953 — Reinforcement
  Rescorla & Wagner 1972 — Conditioning model
  Stein & Meredith 1993 — Multi-modal integration
  Walker 2017 — Sleep consolidation
  Kolb 1984 — Experiential learning
  Jeannerod 2001 — Motor imagery
  Driskell et al. 1994 — Mental rehearsal meta-analysis

  EXPERTISE:
  Chase & Simon 1973 — Expert chess patterns 50,000+
  Haier 1992 — Neural efficiency
  Neubauer & Fink 2009 — Neural efficiency review
  Ericsson et al. 1993 — Deliberate practice

  SOCIAL + CULTURAL:
  Bandura 1977 — Social learning theory
  Boyd & Richerson 1985 — Cultural transmission
  Cialdini 1984, 2006 — Social proof, persuasion
  Hatfield et al. 1994 — Emotional contagion
  Nisbett & Wilson 1977 — Confabulation
  Johnson et al. 1993 — Source monitoring / reality monitoring
  Tajfel 1979 — In-group favoritism
  Nickerson 1998 — Confirmation bias
  Immordino-Yang & Damasio 2007 — Emotion and learning

  COGNITION:
  Wegner 1987 — Ironic process theory
  Smallwood & Schooler 2006 — Mind wandering
  Raichle et al. 2001 — DMN
  Krashen 1982 — Input hypothesis
  Clark & Chalmers 1998 — Extended mind
  Kirsh & Maglio 1994 — Epistemic actions
  Elliot 2006 — Approach vs avoidance

  THERAPY:
  Beck 1979 — CBT
  Foa & Kozak 1986 — Exposure therapy

  EVOLUTION:
  Pavlov 1927 — Classical conditioning
  Bowlby 1969 — Attachment theory
  Semendeferi et al. 2002 — PFC evolution

  SLEEP:
  Diekelmann & Born 2010 — Sleep and memory review
  (Full sleep citations → Compile-Sleep.md v1.0 §9.2)


FRAMEWORK SYNTHESIS (🟡):
  "1 Engine + 3 Modulators" unification — 2026-06-01
  Trust = amplifier (not gate) — 2026-06-01
  Trust scope VALUE vs CONTENT — 2026-06-01
  3-Exposure-Channel parallel model (External/Deliberate/Spontaneous) — 2026-06-01
  Multi-stream compile (4 streams) — 2026-06-01
  Feedback asymmetry (Entity-Valence→PFC direct, PFC→Entity-Valence indirect) — 2026-06-01
  3 Compile Types = modulator configurations — 2026-06-01
  Evolutionary modulator gradient — 2026-06-01
  Sleep Maintenance in compile architecture — 2026-06-01
  Gate = limit case of amplifier — 2026-06-01
  4 compile pathways model — Drill-Compile-Short-Collective.md
  6 trade-offs framework — Drill-Compile-Short-Collective.md
```

---

> **PARENT**: Chunk.md v3.0 §2 (4 compile mechanisms = foundation)
> **COMPANION**: Compile-Sleep.md v1.0 (Sleep Maintenance details)
> **BACKUP**: backup/Compile-Taxonomy-v2.0.md (v2.0 preserved)
