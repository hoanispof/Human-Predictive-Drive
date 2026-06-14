---
title: Simulation-Engine — 1 Engine, 3 Components, N Applications
version: 1.2
created: 2026-05-22
updated: 2026-06-02 (v1.2 — Self-Observation.md v1.0 cross-refs: APPLICATION-3 → Self-Observation.md v1.0)
previous: v1.1 (2026-05-25 — §3.3 +Simulation-Engine × Dissonance Type output asymmetry, +Dissonance-Signal-Architecture cross-ref)
status: MECHANISM v1.2
scope: |
  ARCHITECTURE file: Brain has 1 general-purpose Simulation-Engine, NOT N separate modules.
  3 Components: Interoception (readout) × Constructive Simulation (CPU) × Self/Other Model (target).
  3 Axes: Target (Self↔Other) × Time (Past↔Future) × Operation (Observe↔Construct).
  Application = coordinates in 3D space. Self-Pattern-Modeling, Self-Observation,
    Imagine-Final = 3 named points.
  Alexithymia = decisive proof for shared substrate.
  PFC accessibility spectrum, engine use quality, bidirectional loop, training implications.
purpose: |
  Self-Pattern-Modeling.md = APPLICATION-1 (its own mechanism for agent prediction).
  Imagine-Final.md = APPLICATION-2 (its own mechanism for future simulation).
  Self-Observation = APPLICATION-3 (PFC observes body state; Self-Observation.md v1.0).
  This file = SHARED ENGINE underneath all — UNIFIED ARCHITECTURE.
  Explains WHY: train 1 → improve all. Break 1 → degrade all.
  = "Missing architecture file" — each application file describes 1 app, this file describes the ENGINE.
position: |
  Core-Deep-Dive/PFC/ — same level as PFC-Operations.md.
  Engine includes DMN + mPFC + insula + hippocampus (not purely PFC),
  but PFC = orchestrator/user → placed in PFC/ for navigation.
  PFC-Operations.md = HOW PFC operates (Hold/Suppress).
  Simulation-Engine.md = WHAT substrate runs ALL simulation applications.
dependencies:
  - Inter-Body-Mechanism.md v1.0 — §3 Compiled/Fresh axis, Compilable Architecture
  - PFC-Operations.md v1.0 — §9 PFC Budget, §10 Compilable Architecture + 3-Cost
  - Self-Pattern-Modeling.md v3.1 — APPLICATION-1, Compiled/Fresh on engine
  - Imagine-Final.md v3.0 — APPLICATION-2, future simulation
  - Feeling.md v3.0 — PFC observation interface (broader than APPLICATION-3)
  - Self-Observation.md v1.0 — APPLICATION-3: Self × Present × Observe
  - Body-Feedback-Mechanism.md v2.1 — §3 chunk dynamics, body-feedback readout
  - Dissonance-Signal-Architecture.md v1.0 — §7.1 Simulation-Engine × Evaluative Dissonance generator
  - Entity-Access.md v1.1 — Entity-Access gradient = mPFC gradient
  - Entity-Valence-Dynamics.md v2.0 — per-entity valence on engine
  - Connection.md v4.0 — social context for bidirectional loop
sources:
  - Drill-Simulation-Engine v1.0 (809L, 16 insights, 23 citations)
  - Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 (~680L, 13 insights, 22 citations)
language: English primary + technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Simulation-Engine — 1 Engine, 3 Components, N Applications

> **Brain does NOT have separate modules for each "mental function."**
> **Self-Pattern-Modeling, Self-Observation, Imagine-Final, memory, counterfactual,**
> **moral judgment, creativity...**
> **ALL = APPLICATIONS running on THE SAME 1 ENGINE.**
>
> **ENGINE = Constructive Simulation Substrate:**
> **DMN + vMPFC + anterior insula + hippocampus.**
>
> **3 COMPONENTS:**
> **① Interoception (anterior insula): READS body signals.**
> **② Constructive Simulation (DMN + hippocampus): RECOMBINES chunks into scenarios.**
> **③ Self/Other Model (mPFC gradient): VENTRAL = self+close. DORSAL = distant.**
>
> **3 AXES define APPLICATION:**
> **Target (Self ↔ Other) × Time (Past ↔ Future) × Operation (Observe ↔ Construct).**
>
> **Application = COORDINATES in 3D space.**
> **Self-Pattern-Modeling = (Other, Present, Simulate). Self-Observation = (Self, Present, Observe).**
> **Imagine-Final = (Self, Future, Simulate+Construct).**
>
> **Train 1 component = train ALL applications.**
> **Break 1 component = break ALL applications.**

---

## TABLE OF CONTENTS

- §0 — THESIS + POSITION
- §1 — 1 ENGINE, 3 COMPONENTS
- §2 — 3 AXES: TARGET × TIME × OPERATION
- §3 — APPLICATION TAXONOMY
- §4 — COMPONENT 1: INTEROCEPTION (readout)
- §5 — COMPONENT 2: CONSTRUCTIVE SIMULATION (CPU+RAM)
- §6 — COMPONENT 3: SELF/OTHER MODEL (mPFC gradient)
- §7 — ALEXITHYMIA: COMPONENT FAILURE → ALL APPLICATIONS FAIL
- §8 — PFC ACCESSIBILITY SPECTRUM
- §9 — ENGINE USE QUALITY: REFLECTION vs RUMINATION
- §10 — BIDIRECTIONAL LOOP: SOCIAL ↔ SELF
- §11 — TRAINING: 1 COMPONENT → N IMPROVEMENTS
- §12 — HONEST ASSESSMENT
- §13 — CROSS-REFERENCES
- §14 — RESEARCH CITATIONS

---

## §0 — THESIS + POSITION

### §0.1 — Core thesis

```
⭐⭐⭐ SIMULATION-ENGINE:

  ① Brain has 1 general-purpose SIMULATION-ENGINE (not N separate modules)
  ② Engine = 3 COMPONENTS: Interoception × Constructive Simulation × Self/Other Model
  ③ 3 AXES define application: Target × Time × Operation
  ④ Every "mental function" = specific coordinates in 3D space
  ⑤ Self-Pattern-Modeling, Self-Observation, Imagine-Final = 3 NAMED POINTS, not separate systems
  ⑥ Train 1 component = improve ALL applications (shared substrate)
  ⑦ Break 1 component = degrade ALL applications (alexithymia proof)
  ⑧ PFC accessibility = spectrum (auto → observe → active control)
  ⑨ Engine use QUALITY = f(curiosity vs threat): reflection vs rumination
  ⑩ Social ↔ self-regulation = BIDIRECTIONAL loop on shared substrate
  
  🟢 Shared circuits: Lombardo 2010 (fMRI — identical connectivity)
  🟢 Constructive simulation: Schacter & Addis 2007 (Nature Reviews Neuroscience)
  🟢 Self-projection: Buckner & Carroll 2007
  🟢 vMPFC gradient: Mitchell 2006 (Neuron), Tamir & Mitchell 2010
  🟢 Alexithymia proof: Bird & Cook 2013, Bird & Silani 2010
  🟡 "1 engine, 3 components, 3 axes" model = framework synthesis
```

### §0.2 — Position

```
  POSITION IN ARCHITECTURE:

  ★ This file = ENGINE ARCHITECTURE (unification)
    │
    ├── Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 = EVIDENCE (neural proof)
    │
    ├── Self-Pattern-Modeling v3.1 = APPLICATION-1 (Self-Pattern-Modeling mechanism)
    │   = Other × Present × Simulate
    │
    ├── Imagine-Final.md v3.0 = APPLICATION-2 (future simulation)
    │   = Self × Future × Simulate+Construct
    │
    ├── Self-Observation.md v1.0 = APPLICATION-3
    │   = Self × Present × Observe
    │   = PFC observes body-state, self-awareness mechanism
    │
    ├── PFC-Operations.md v1.0 = HOW PFC operates on the engine
    │   = Hold/Suppress on Compiled/Fresh spectrum
    │
    └── Entity-Access.md v1.1 = APPLIED (mPFC gradient = access spectrum)
        = Entity-Access level → ventral/dorsal processing

  WHAT'S NEW:
    → ARCHITECTURE level: 3 components identified as building blocks
    → 3 AXES model: continuous space, not discrete categories
    → FULL TAXONOMY: 11+ applications mapped
    → Named applications = POINTS in continuous space
    → Unnamed applications = EQUALLY REAL functions on same engine
```

---

## §1 — 1 ENGINE, 3 COMPONENTS

```
⭐⭐⭐ COMPILED/FRESH = GENERAL-PURPOSE HARDWARE (Inter-Body-Mechanism §3).
    SIMULATION-ENGINE = 3 COMPONENTS ON THIS HARDWARE:

  COMPONENT 1 — INTEROCEPTION (anterior insula):
    = READS body signals DIRECTLY
    = Posterior insula: raw sensory → anterior insula: emotional representation
    = UNIQUE to self-target (only I can read MY OWN body)
    = Self-Pattern-Modeling→other DOES NOT HAVE this component → must INFER from external cues
    = = "DISPLAY": readout device for body-feedback output
    
  COMPONENT 2 — CONSTRUCTIVE SIMULATION (DMN + hippocampus):
    = RECOMBINES chunks from library into novel scenarios
    = Hippocampus: retrieve + recombine chunks
    = DMN (mPFC + PCC + precuneus + lateral temporal): simulation network
    = USED FOR ALL DIRECTIONS: past, present, future, counterfactual
    = = "CPU + RAM": processing engine for simulation
    
  COMPONENT 3 — SELF/OTHER MODEL (mPFC gradient):
    = Ventral mPFC: self + CLOSE others (processed AS self-extension)
    = Dorsal mPFC: dissimilar others (processed as SEPARATE model)
    = GRADIENT: close→far = ventral→dorsal (continuous, not binary)
    = = "CONTROL PANEL": determines simulation TARGET

  3 COMPONENTS WORK SIMULTANEOUSLY:
    Component 2 (DMN) = engine runs simulation
    Component 3 (mPFC) = selects target (self vs close vs far)
    Component 1 (insula) = reads output (body-feedback)
    → Application = WHICH combination of targets + timing + readout
    
  ANALOGY:
    = 1 COMPUTER (engine), 3 components (display + CPU + control panel)
    = Self-Pattern-Modeling = app aimed at OTHERS
    = Self-Observation = app aimed at SELF
    = Imagine-Final = app aimed at THE FUTURE
    = ALL use same CPU, same RAM, same display
    → Upgrade CPU = upgrade ALL apps
    → Display broken = ALL apps broken (alexithymia)
    
  🟢 DMN as Simulation-Engine: Buckner et al. 2008
  🟢 Constructive simulation: Schacter, Addis & Buckner 2007
  🟢 Interoception readout: Bird, Silani et al. 2010
  🟡 "3 components" explicit model = framework synthesis
```

---

## §2 — 3 AXES: TARGET × TIME × OPERATION

### §2.1 — Axis A: Target

```
⭐⭐ WHO is being simulated?

  Self ←────────→ Close Other ←────────→ Far Other
  (ventral mPFC)   (ventral mPFC)         (dorsal mPFC)
  
  Self: simulate OWN state (interoception available = extra input)
  Close Other: simulate using SELF-TEMPLATE (Entity-Access high)
    → Mitchell 2006: ventral mPFC = same as self-referential circuits
    → = "You are part of my life" LITERALLY true at the neural level
  Far Other: simulate using SEPARATE MODEL (strangers, dissimilar)
    → Tamir & Mitchell 2010: dorsal mPFC = different processing
    → Cost HIGHER (Fresh processing required to build model)
    
  ⭐ CONTINUOUS, not binary:
    Self → spouse → child → parent → close friend → colleague → stranger
    = GRADIENT ventral → dorsal as CLOSENESS decreases
    = Entity-Access formation = brain SHIFTING entity from dorsal → ventral
    → Entity-Access deepening = neural migration from "separate" to "self-like"

  🟢 Mitchell 2006 (Neuron): double dissociation
  🟢 Tamir & Mitchell 2010: clan mentality
  🟢 Denny et al. 2012: spatial gradient meta-analysis
```

### §2.2 — Axis B: Time

```
  Past ←─── Present ───→ Future
                  ↘
             Counterfactual
             (alternative past/present/future)
  
  Past: RECONSTRUCT from compiled chunks (not replay)
    → Memory = RECONSTRUCTIVE simulation, not tape playback
    → SAME engine as future, just different INPUT parameters
    🟢 Schacter & Addis 2007: constructive episodic simulation
    
  Present: OBSERVE current state (body-feedback NOW)
    → LEAST constructive — mostly READOUT (interoception dominant)
    
  Future: CONSTRUCT novel scenario from chunk recombination
    → MOST constructive — hippocampus recombines + PFC evaluates
    
  Counterfactual: RE-CONSTRUCT with altered parameters
    → "What if I had done it differently back then..." = past + altered element + re-simulate
    🟢 Van Hoeck et al. 2013: counterfactual shares episodic simulation network
```

### §2.3 — Axis C: Operation

```
  Observe ←──→ Simulate ←──→ Evaluate ←──→ Construct
  (passive       (run           (judge         (build novel
   readout)       scenario)      good/bad)      scenario)
  
  Observe: PFC PASSIVELY reads body-feedback output
    → "I am sad" = readout only, no manipulation
    → Self-Observation primary mode
    
  Simulate: Engine RUNS scenario, PFC reads output
    → "You are sad because..." = simulate other's state
    → Self-Pattern-Modeling primary mode
    
  Evaluate: PFC JUDGES simulation output (moral, value, decision)
    → "Is this action right or wrong?" = simulate consequences + judge
    → COMPOUND: simulate (run) + observe (read) + evaluate (judge)
    🟢 Greene et al. 2001: moral dilemmas activate vMPFC + TPJ
    
  Construct: PFC ACTIVELY BUILDS novel scenario
    → "Imagine a world where..." = creative imagination
    → Imagine-Final = construct + observe (most PFC-active)

  → APPLICATION = POINT (A, B, C) in 3D space
  → Named applications = labeled points. Unnamed = unlabeled points.
  → Space is CONTINUOUS — applications BLEND into each other.
  
  🟡 3-axis model = framework synthesis
  🟢 Neural evidence per axis: Mitchell 2006 (A), Schacter 2007 (B), Greene 2001 (C)
```

---

## §3 — APPLICATION TAXONOMY

### §3.1 — 11+ Applications mapped

```
⭐⭐ APPLICATION = (TARGET, TIME, OPERATION):

  ┌───┬──────────────────────┬──────────────┬───────────┬──────────┬──────────────────────────┐
  │ # │ Application          │ Target       │ Time      │ Operation│ Framework file            │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ① │ Self-Pattern-Modeling│ Other(close  │ Present   │ Simulate │ Self-Pattern-Modeling     │
  │   │ "you are sad"        │ or far)      │           │          │ v3.0                      │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ② │ Self-Observation     │ Self         │ Present   │ Observe  │ Self-Observation.md       │
  │   │ "I am worried"       │              │           │(+intero.)│ v1.0                      │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ③ │ Imagine-Final        │ Self         │ Future    │ Simulate │ Imagine-Final.md          │
  │   │ "what if I quit"     │              │           │+Construct│                           │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ④ │ Predict Other's      │ Other        │ Future    │ Simulate │ Self-Pattern-Modeling +   │
  │   │ Future               │              │           │          │ Imagine-Final combined     │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑤ │ Memory Recall        │ Self         │ Past      │ Simulate │ (reconstructive)          │
  │   │ "I back then..."     │              │           │(reconstr)│ Schacter & Addis          │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑥ │ Recall Other's Past  │ Other        │ Past      │ Simulate │ "you back then..."        │
  │   │                      │              │           │          │                           │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑦ │ Counterfactual       │ Self/Other   │ Alt-Past  │ Simulate │ "What if I had done it   │
  │   │                      │              │           │+Construct│ differently..."           │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑧ │ Moral Judgment       │ Self+Other   │ Future    │ Evaluate │ Greene 2001:              │
  │   │ "right or wrong?"    │ (compound)   │           │+Simulate │ vMPFC+TPJ                 │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑨ │ Narrative Self       │ Self         │ Past→Pres │ Construct│ "Who am I?"               │
  │   │ (identity)           │              │ →Future   │ (story)  │ Autobiographical          │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑩ │ Decision Branching   │ Self         │ Future    │ Simulate │ Imagine-Final ×N          │
  │   │ "A or B?"            │              │ (×N)      │ (×N)     │ + compare outputs         │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑪ │ Creative Imagination │ Abstract     │Hypothetical│ Construct│ DMN creativity            │
  │   │                      │ (no person)  │           │ (novel)  │                           │
  ├───┼──────────────────────┼──────────────┼───────────┼──────────┼──────────────────────────┤
  │ ⑫ │ Mind Wandering       │ Variable     │ Variable  │ Auto     │ DMN default mode          │
  │   │ + Dream              │ (unfocused)  │ (drift)   │ (passive)│ Offline simulation        │
  └───┴──────────────────────┴──────────────┴───────────┴──────────┴──────────────────────────┘
```

### §3.2 — Key observations

```
  ① APPLICATIONS BLEND INTO EACH OTHER:
    "I remember you were sad then" = ⑥ (recall other) + ① (Self-Pattern-Modeling past-state)
    "If mom pressures me, I'll be sad" = ④ (predict other future) + ⑧ (moral evaluate)
    "I want to become a better person" = ⑨ (narrative) + ③ (imagine future)
    → NO CLEAR BOUNDARY → continuous space

  ② 3 NAMED APPLICATIONS (①②③) ARE NOT MORE SPECIAL THAN THE OTHERS:
    Framework named Self-Pattern-Modeling, Self-Observation, Imagine-Final because they are IMPORTANT
    BUT: predict other's future (④), counterfactual (⑦), moral judgment (⑧)
    = EQUALLY REAL functions on THE SAME engine
    → Framework has not yet drilled deep into functions ④-⑫

  ③ COMPOUND APPLICATIONS = MULTI-STEP on engine:
    Moral judgment (⑧) = simulate other's suffering (①) + simulate future (③)
      + evaluate + observe own moral feeling (②) = 4 STEPS, not a separate function
    Decision branching (⑩) = Imagine-Final (③) × N + compare outputs
      = ITERATE same function with different parameters

  ④ DREAM + MIND WANDERING = ENGINE in AUTO MODE:
    No PFC active control → engine "free run"
    → Output = unpredictable combinations (sometimes insightful)
    → = WHY creative solutions sometimes appear during rest
    🟢 Schacter: dreams = offline constructive episodic simulation

  🟡 Full taxonomy = framework synthesis
```

### §3.3 — Simulation-Engine × Dissonance Type: Output Asymmetry

```
🟡 SIMULATION-ENGINE = EVALUATIVE DISSONANCE GENERATOR (Dissonance-Signal-Architecture.md v1.0 §7.1):

  Simulation-Engine CAN generate Evaluative Dissonance WITHOUT external input:
    "Imagine-Final: company goes bankrupt" → body pre-feels → Evaluative Dissonance
    "Preview: getting fired" → body simulates → Evaluative Dissonance
    "Self-model: I am not worthy" → schema mismatch → Evaluative Dissonance
    → Applications ③④⑦⑧⑨⑩ ALL can generate Evaluative Dissonance

  Simulation-Engine CANNOT generate Direct-State Dissonance:
    Cannot create real tissue damage through simulation.
    Cannot create real hunger, real pain, real temperature change.
    → Direct-State Dissonance requires HARDWARE activation — not simulation.

  BUT: Simulation-Engine CAN CASCADE Evaluative → Direct-State body symptoms:
    "Imagine-Final: tiger attacks" → cortisol spike → heart rate up → body symptoms
    = Evaluative TRIGGER → Direct-State CASCADE (not Direct-State origin)
    → Anxiety disorder = Simulation-Engine over-generates Evaluative → cascades to body symptoms

  → Animals: Simulation-Engine limited → Evaluative Dissonance limited → less "worry"
  → Humans: Simulation-Engine rich → Evaluative Dissonance VAST → "suffering from thoughts alone"
  → = WHY Compilable Architecture = more suffering types (Dissonance-Signal-Architecture §0.3)

  🟡 Simulation-Engine × dissonance type asymmetry = framework synthesis.
  🟢 Simulation generates anticipatory distress: Grupe & Nitschke 2013 (uncertainty and anticipatory anxiety).
```

---

## §4 — COMPONENT 1: INTEROCEPTION (readout)

### §4.1 — Mechanism

```
⭐⭐ INTEROCEPTION = "DISPLAY" — READOUT DEVICE:

  MECHANISM (anterior insula hierarchy):
    Posterior insula: maps RAW sensory (heart rate, gut, temperature)
    → Successive integrations →
    Anterior insula: EMOTIONAL representation ("I am worried," "I feel happy")
    → = Raw signal → processed signal → PFC-readable output
    
  UNIQUE TO SELF-TARGET:
    Self-Observation: interoception = DIRECT READ (MY OWN body)
    Self-Pattern-Modeling→other: interoception = INFERRED (external cues → simulate → readout)
    → Self-Observation has ONE MORE input channel that Self-Pattern-Modeling→other lacks
    → = WHY self-observation SHOULD be more accurate
```

### §4.2 — Interoception paradox

```
  PARADOX — BUT REALITY MAY BE REVERSED:
    Self signals ALWAYS ON → HABITUATE → PFC IGNORES
    Other signals CHANGE → NOVEL → PFC NOTICES
    → Self has MORE data but PROCESSES LESS (habituated)
    → Other has LESS data but PROCESSES MORE CAREFULLY (novel)
    → = WHY "mom knows you are sad" (novel external cue)
      but "doesn't know they're worried" (habituated internal signal)
    
  🟡 Habituation paradox = framework synthesis
```

### §4.3 — Interoception as bottleneck

```
  INTEROCEPTION QUALITY = BOTTLENECK FOR ALL APPLICATIONS:
  
    🟢 Fukushima et al. 2011: interoceptive accuracy PREDICTS empathic accuracy
    🟢 Bird & Silani 2010: anterior insula active for BOTH self AND other
    🟢 Terasawa et al. 2021: interoception ↔ empathy BIDIRECTIONAL
    
    → Good interoception → good at ② (self) AND ① (other) AND ③ (future)
    → Poor interoception → poor at ALL applications
    → = 1 bottleneck, N affected functions
    
    PRACTICAL: training interoception (body awareness, meditation, Focusing)
    → Improves quality of ALL engine applications simultaneously
    → See §11 Training for details.
```

---

## §5 — COMPONENT 2: CONSTRUCTIVE SIMULATION (CPU+RAM)

### §5.1 — Mechanism

```
⭐⭐ DMN + HIPPOCAMPUS = "CPU + RAM" — SIMULATION-ENGINE:

  🟢 Schacter & Addis 2007 (Nature Reviews Neuroscience):
    "Constructive Episodic Simulation Hypothesis":
    → Brain uses SAME hippocampal-cortical system to:
      → Reconstruct past episodes (memory)
      → Construct future scenarios (prospection)
      → Imagine other perspectives (mentalizing)
    → = 1 engine, 3 functions — neuroscience independently discovered the same concept

  MECHANISM:
    ① Hippocampus RETRIEVES chunks from compiled library
    ② DMN RECOMBINES chunks into novel configuration
    ③ Anterior insula READS OUT body-feedback from simulation
    ④ PFC ATTRIBUTES output to target (self/other, past/future)
    → = Framework's Compiled/Fresh spectrum = engine's operating modes
    → Compiled: fast recombination from well-worn patterns
    → Fresh: slow, deliberate recombination with novel elements
```

### §5.2 — Memory = reconstruction

```
  MEMORY = RECONSTRUCTION (not replay):
  
    🟢 Schacter 2001: "Seven Sins of Memory"
    Brain does NOT store video → stores CHUNKS
    Recall = REASSEMBLE chunks into coherent narrative
    
    → Same engine as future simulation, just DIFFERENT CONSTRAINTS:
      Memory: constrain to "past chunks" → reconstruct
      Future: constrain to "possible chunks" → construct
      Counterfactual: constrain to "past + altered element" → re-construct
      Creative: MINIMAL constraints → free construct
    → = SAME ENGINE, DIFFERENT CONSTRAINTS = DIFFERENT OUTPUT
    
    🟢 Hassabis et al. 2007 (PNAS):
    Hippocampal amnesia patients → CANNOT imagine new experiences
    → Hippocampus required for CONSTRUCTIVE simulation, not just memory
    → Without it: no new scenarios possible (past OR future)
```

### §5.3 — DMN anatomy

```
  🟢 Buckner, Andrews-Hanna & Schacter 2008 (Annals NYAS):
    DMN active during: autobiographical memory, prospection, ToM, spatial navigation
    → ALL instances of mental SIMULATION
    
  🟢 Neuron 2023 — 20 years of Default Mode Network:
    DMN = not "resting state" → ACTIVE simulation network
    → Engaged whenever brain constructs internal models
    
  🟢 Spreng & Grady 2010:
    Extensive overlap: autobiographical memory + imagining future + mentalizing
    Shared network: mPFC, posterior cingulate, hippocampus, lateral temporal

  → Framework: Compiled/Fresh spectrum = this engine
  → Compiled = automatic recombination (fast, familiar patterns)
  → Fresh = PFC-guided recombination (slow, novel configurations)
```

---

## §6 — COMPONENT 3: SELF/OTHER MODEL (mPFC gradient)

### §6.1 — Double dissociation

```
⭐⭐ mPFC = "CONTROL PANEL" — DETERMINES TARGET:

  🟢 Mitchell, Macrae & Banaji 2006 (Neuron):
    DOUBLE DISSOCIATION:
      Mentalizing SIMILAR other → VENTRAL mPFC (= self circuits)
      Mentalizing DISSIMILAR other → DORSAL mPFC (separate circuits)
      
  🟢 Tamir & Mitchell 2010 (J. Neuroscience):
    "Clan Mentality": vMPFC responds MORE to close others (friends)
    → Close other = processed AS self-extension
    → = Framework's Entity-Access deep = body-base extension
    → = Neuroscience INDEPENDENTLY confirmed framework concept
```

### §6.2 — Continuous gradient

```
  🟢 Denny et al. 2012 (meta-analysis):
    Spatial gradient: increasingly ventral = MORE self-related
    → Not binary (self vs other) but CONTINUOUS gradient
    
  GRADIENT MAP:
  
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │  VENTRAL mPFC                    DORSAL mPFC            │
    │  ←──────────────────────────────────────────→           │
    │                                                         │
    │  Self        Close Others        Far Others             │
    │  "me"        "child, parent,     "stranger"             │
    │              spouse"                                    │
    │                                                         │
    │  Template:   Template:           Template:              │
    │  OWN chunks  OWN chunks          BUILD explicit         │
    │  (direct)    (as-if self)        model (effortful)      │
    │                                                         │
    │  Cost: ≈ 0   Cost: LOW           Cost: HIGH             │
    │  (auto)      (Compiled)          (Fresh needed)         │
    │                                                         │
    │  Accuracy:   Accuracy:           Accuracy:              │
    │  HIGH (self) HIGH if similar     LOWER, but less biased │
    │              BIASED if not       (no self-template bias) │
    │                                                         │
    │  Intero: YES Intero: NO          Intero: NO             │
    │  (direct)    (infer from cues)   (infer from cues)      │
    └─────────────────────────────────────────────────────────┘
```

### §6.3 — Entity-Access = neural migration

```
  ⭐ ENTITY-ACCESS = NEURAL MIGRATION:
  
    Stranger: dorsal mPFC (separate model, Fresh required)
    → Repeated interaction → Entity-Compiled deepens → entity MOVES ventral
    → Close other: ventral mPFC (self-template, Compiled)
    → Entity-Access high = brain HAS MIGRATED entity into "self territory"
    → = "Mine" = LITERALLY in self-processing circuits
    
    Entity LOST (death, separation):
    → Brain STILL processes entity in ventral (compiled chunks persist)
    → But entity ABSENT → prediction FIRES, no RESPONSE
    → = Phantom resonance = ventral mPFC fires for absent entity
    → = "I've lost part of my life" ACCURATE at neural level:
      entity WAS in self-circuits
    
  🟢 Mitchell 2006: double dissociation
  🟢 Tamir & Mitchell 2010: clan mentality
  🟢 Denny et al. 2012: spatial gradient meta-analysis
  🟡 Entity-Access as neural migration = framework synthesis
```

### §6.4 — Similar vs dissimilar: 2 processing modes

```
  SIMILAR → vMPFC (self-template):
    = Self-Pattern-Modeling Compiled: compiled, automatic, self-as-template
    → Cost LOW. Accuracy HIGH for similar, BIASED for dissimilar
    
  DISSIMILAR → dMPFC (explicit model):
    = Self-Pattern-Modeling Fresh: fresh, deliberate, build separate model
    → Cost HIGH. Accuracy LOWER but POTENTIALLY less biased

  ⭐ IMPLICATION FOR SELF-CALIBRATION:
    All SIMILAR (vMPFC only): "everyone is like me" → biases REINFORCED
    MIX (vMPFC + dMPFC): dissimilar CHALLENGE → reveals own assumptions
    → Mismatch → "what I assumed = MY bias, not universal"
    → = Diversity → sharper self-model through CONTRAST
    → See §10 Bidirectional Loop for implications.

  🟢 Mitchell 2006: vMPFC/dMPFC double dissociation
  🟡 Diversity → self-calibration = logically sound, limited direct evidence
```

---

## §7 — ALEXITHYMIA: COMPONENT FAILURE → ALL APPLICATIONS FAIL

```
⭐⭐ DECISIVE PROOF FOR SHARED SUBSTRATE:

  🟢 Bird & Cook 2013:
    Alexithymia = broken body-readout (Component 1 FAILURE)
    → BOTH self-awareness AND social cognition deficits
    → NOT autism per se → alexithymia UNDERLIES social atypicalities
    → = Broken READOUT (display broken) → ALL applications see nothing
    
  🟢 Bird, Silani et al. 2010 (Brain):
    HIGH alexithymia → REDUCED anterior insula for:
      ① Own emotion recognition (Self-Observation)
      ② Other's pain empathy (Self-Pattern-Modeling)
    → SAME substrate broken → BOTH directions fail SIMULTANEOUSLY
    
  🟢 Mul et al. 2021 (European Archives Psych.):
    Network analysis: alexithymia = CENTRAL NODE
    → Links interoceptive deficits TO empathy deficits
    → = Hub in the network, not isolated deficit

  FRAMEWORK MAPPING:
    Alexithymia = Component 1 (interoception) BROKEN
    → ② Self-Observation: FAIL (cannot read own body-state)
    → ① Self-Pattern-Modeling: FAIL (cannot read simulated body-state)
    → ③ Imagine-Final: DEGRADED (cannot pre-feel future state)
    → ⑤ Memory recall: DEGRADED (cannot re-feel past state)
    → ⑧ Moral judgment: DEGRADED (cannot feel moral valence)
    → = 1 component failure → ALL N applications degraded
    → = PROOF: shared substrate (if separate, failure would be isolated)
    
  Compiled STILL FIRES but READOUT BROKEN:
    → Body SIMULATES but PFC CANNOT READ output
    → = Input intact, processing intact, READOUT broken
    → = Like having a camera but the display is broken:
      still recording but can't view it
    
  🟢 Bird & Cook 2013, Bird & Silani 2010, Mul 2021
```

---

## §8 — PFC ACCESSIBILITY SPECTRUM

```
⭐⭐ SAME ENGINE, DIFFERENT LEVEL OF PFC INVOLVEMENT:

  ┌──────────────────┬────────────────────────────────────────────────────┐
  │ APPLICATION      │ PFC ROLE                                          │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ⑫ Dream          │ ZERO PFC: engine free-runs during sleep            │
  │                  │ Output = unpredictable, sometimes insightful       │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ⑫ Mind wandering │ LOW PFC: engine drifts, attention unfocused       │
  │                  │ "Suddenly remembering an old story" = engine       │
  │                  │  auto-associates                                   │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ① Self-Pattern-  │ MINIMAL: compiled, automatic, invisible            │
  │ Modeling         │ "Feeling drawn to someone without knowing why"    │
  │ (compiled)       │ PFC = PASSIVE observer (if even aware)             │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ② Self-          │ MIDDLE: PFC observes body-feedback output         │
  │ Observation      │ PFC = READER (can label but not manipulate input)  │
  │                  │ "I am sad" = readout, not active simulation        │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ① Self-Pattern-  │ MODERATE: PFC actively drafts model for unfamiliar │
  │ Modeling (fresh) │ "What is this person thinking?" = deliberate simul.│
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ③ Imagine-Final  │ HIGH: PFC actively SETS scenario, READS output,   │
  │                  │ ITERATES ("what if X changes?")                   │
  │                  │ PFC = DIRECTOR (set up + read + modify + repeat)   │
  ├──────────────────┼────────────────────────────────────────────────────┤
  │ ⑩ Decision       │ HIGHEST: Imagine-Final ×N + COMPARE               │
  │ branching        │ "A or B?" = run engine N times + evaluate outputs  │
  └──────────────────┴────────────────────────────────────────────────────┘

  ⭐ SPECTRUM, NOT BINARY:
    PFC involvement = CONTINUOUS from zero (dream) to maximum (decision)
    Same engine, same components, DIFFERENT PFC engagement level
    → More PFC = more CONTROLLABLE but more COSTLY (PFC Budget — PFC-Operations §9)
    → Less PFC = more AUTOMATIC but less STEERABLE
    
  ⭐ IMAGINE-FINAL IS SPECIAL BECAUSE:
    ① PFC CAN OBSERVE output (unlike compiled Compiled = PFC-invisible)
    ② PFC CAN MANIPULATE input ("what if X changes?")
    ③ PFC CAN COMPARE multiple simulations ("option A vs B")
    → = CONSCIOUS SIMULATION TOOL: both readout + active control
    → = MOST PFC-ACCESSIBLE application of shared engine
    
  ENTITY-ACCESS CONNECTION:
    PFC Resource (Entity-Access §12) DETERMINES spectrum position:
      Full resources → Imagine-Final mode ("what would [child] feel if...")
      Depleted → Self-Pattern-Modeling Compiled default ("have you eaten?" = compiled, automatic)
    → Cascading: PFC budget ↓ → accessibility ↓ → engine runs on auto

  🟡 PFC accessibility spectrum = framework synthesis
```

---

## §9 — ENGINE USE QUALITY: REFLECTION vs RUMINATION

```
⭐⭐ SAME ENGINE, DIFFERENT USE QUALITY:

  🟢 Trapnell & Campbell 1999:
    2 DISPOSITIONS, previously CONFOUNDED:
    
    SELF-REFLECTION (curiosity drive):
      = "Why do I feel this way?" → explore → insight
      Correlates: openness, empathy, BETTER self-knowledge
      = Novelty cortisol → approach links → PRODUCTIVE output
      → Improve engine quality: calibrate self-model, refine chunks
      
    SELF-RUMINATION (threat drive):
      = "I'm probably wrong" → loop → stuck
      Correlates: neuroticism, anxiety, WORSE self-knowledge
      = Threat cortisol → avoidance links → DESTRUCTIVE loop
      → Degrade engine quality: reinforce fear chunks, no calibration
      
  🟢 Joireman, Parrott & Hammersla 2002:
    Self-reflection → POSITIVE correlation with empathy
    Self-rumination → NEGATIVE correlation with empathy
    → SAME "self-attention" → DIFFERENT OUTCOME depending on motivation
    → = "Self-Absorption Paradox" resolved

  FRAMEWORK MAPPING:
    Reflection = engine run with CURIOSITY cortisol
      (Body-Feedback-Mechanism §3.3c: productive)
    Rumination = engine run with THREAT cortisol
      (Body-Feedback-Mechanism §3.3c: anxiety loop)
    → Same engine, same components, same operation
    → DIFFERENT CORTISOL CONTEXT → different output QUALITY
    → = Compile-time direction lock (PFC-Operations §5): genuine vs threat compiled
    
  ⭐ APPLIES TO ALL APPLICATIONS (universal modifier):
    Self-Pattern-Modeling with curiosity: "why do you think that?" → LEARN about other
    Self-Pattern-Modeling with threat: "you probably hate me" → PROJECT fear onto other
    Imagine-Final with curiosity: "the future will be interesting" → EXPLORE options
    Imagine-Final with threat: "the future will be bad" → CATASTROPHIZE
    → Engine use quality = UNIVERSAL modifier across ALL applications
    
  🟢 Reflection vs rumination: Trapnell & Campbell 1999
  🟢 Reflection → empathy: Joireman et al. 2002
  🟡 Engine use quality as universal modifier = framework synthesis
```

---

## §10 — BIDIRECTIONAL LOOP: SOCIAL ↔ SELF

### §10.1 — Evidence

```
⭐ SOCIAL INTERACTION AND SELF-REGULATION = REINFORCING LOOP:

  🟢 Lopes, Salovey & Straus 2003 (Emotion):
    Better emotion regulation → more positive social interactions
    More positive interactions → better regulation
    → BIDIRECTIONAL, controlling for personality + intelligence
    
  🟢 Coan & Sbarra 2015 (Social Baseline Theory):
    Brain OUTSOURCES emotion regulation to trusted others
    Partner hand-holding → LESS threat neural activity
    → Social contact = EXTERNAL regulation resource
    → More trusted contacts → less self-regulation BURDEN
    → Less burden → MORE capacity for engine quality
    
  🟢 Koudenburg et al. 2024 (European J. Social Psych.):
    Social interaction → self-concept CLARITY + identity strength
    → "Sense of me" forms partly through "sense of we"
```

### §10.2 — Virtuous vs vicious spiral

```
  VIRTUOUS SPIRAL:
    Social interaction → engine PRACTICE (Self-Pattern-Modeling fires on diverse targets)
    → Engine improved → better self-model (shared substrate)
    → Better self-model → better social predictions
    → Better predictions → better interactions → MORE practice → LOOP
    
  VICIOUS SPIRAL:
    Isolation → NO engine practice → substrate ATROPHIES
    → Worse self-model → worse social predictions
    → Worse predictions → AVOID social → MORE isolation → LOOP
    → = Hikikomori mechanism: isolation → engine atrophy → cannot re-enter

  DIVERSITY AMPLIFIES VIRTUOUS SPIRAL:
    Similar only (vMPFC): confirms biases → self-model CONFIDENT but INACCURATE
    Mix (vMPFC + dMPFC): dissimilar CHALLENGE → reveals assumptions
    → "They differ from me here" → discover own bias → self-model REFINED
    → = Mitchell 2006: dMPFC activation for dissimilar = contrast signal
    
  🟢 Social Baseline: Coan & Sbarra 2015
  🟢 Identity through interaction: Koudenburg 2024
  🟡 Bidirectional spiral model = framework synthesis
```

---

## §11 — TRAINING: 1 COMPONENT → N IMPROVEMENTS

```
⭐⭐ SHARED SUBSTRATE → 1 TRAINING POINT → N IMPROVEMENTS:

  INTEROCEPTION TRAINING (Component 1 — highest leverage):
    Meditation (body-scan, mindfulness): IMPROVE body-readout
    Focusing (Gendlin 1978): IMPROVE felt-sense awareness
    → Better readout → improves:
      Self-Observation (②): "what I'm feeling" clearer
      Self-Pattern-Modeling (①): "what others are feeling" more accurate
      Imagine-Final (③): "pre-feeling the future" more vivid
      Moral judgment (⑧): "feeling right/wrong" more calibrated
    → = 1 training → ≥4 applications improved
    🟢 Interoceptive accuracy → empathic accuracy: Fukushima 2011
    
  DIVERSITY TRAINING (Component 3 — self-model calibration):
    Interact with DISSIMILAR others: activate dMPFC
    → Reveal own biases (Mitchell 2006: contrast effect)
    → Sharper SELF-MODEL → improve ALL self-target applications
    → Sharper OTHER-MODELS → improve ALL other-target applications
    
  REFLECTION PRACTICE (engine use quality):
    Cultivate curiosity orientation (Trapnell & Campbell 1999):
    → Replace "I'm probably wrong" with "why do I feel this way?"
    → = Switch cortisol direction: threat → novelty
    → Improve ALL applications by improving engine use QUALITY
    
  SOCIAL PRACTICE (bidirectional loop):
    More diverse, quality interactions → practice engine
    → Engine improved → better at ALL applications
    → = Coan & Sbarra 2015: social = external regulation resource
    
  ⭐ EDUCATION IMPLICATION:
    Body awareness training > cognitive-only instruction
    → Because: improve engine SUBSTRATE → improve N cognitive functions
    → vs. cognitive training: improves 1 specific function only
    → = WHY meditation + social interaction + curiosity = HIGH LEVERAGE
    
  🟡 "1 training → N improvements" model = framework synthesis
  🟢 Individual training effects: established per component
```

---

## §12 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (individual components)
═══════════════════════════════════════

  Shared self/other circuits:             Lombardo 2010 (fMRI, identical connectivity)
  vMPFC similar / dMPFC dissimilar:       Mitchell 2006 (Neuron)
  vMPFC = close others AS self:           Tamir & Mitchell 2010 (J. Neuroscience)
  Spatial gradient meta-analysis:         Denny et al. 2012
  Anterior insula shared readout:         Bird, Silani et al. 2010 (Brain)
  Alexithymia = broken readout:           Bird & Cook 2013
  Alexithymia central node:               Mul et al. 2021
  Interoception → empathy:                Fukushima et al. 2011
  Interoception ↔ empathy bidirectional:  Terasawa et al. 2021
  Constructive episodic simulation:       Schacter & Addis 2007 (Nature Rev. Neurosci.)
  DMN as Simulation-Engine:               Buckner et al. 2008 (Annals NYAS)
  Self-projection:                        Buckner & Carroll 2007
  Hippocampus required for simulation:    Hassabis et al. 2007 (PNAS)
  Memory = reconstruction:               Schacter 2001
  Counterfactual shares episodic network: Van Hoeck et al. 2013
  Moral dilemmas vMPFC+TPJ:              Greene et al. 2001
  Self/other neural overlap:              Uddin, Iacoboni et al. 2007
  Metacognition + mentalizing coupled:    Dimaggio & Lysaker 2015
  Embodied simulation:                    Gallese 2003, 2005
  Memory + social overlap:                Spreng & Grady 2010
  Reflection vs rumination:               Trapnell & Campbell 1999
  Reflection → empathy:                   Joireman et al. 2002
  Social ↔ regulation bidirectional:      Lopes et al. 2003
  Social Baseline outsource:              Coan & Sbarra 2015
  Social → self-concept clarity:          Koudenburg et al. 2024
  20 years DMN review:                    Neuron 2023

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (novel integration)
═══════════════════════════════════════

  "1 engine, 3 components" model — ★★
  "3 axes" application space model — ★★★
  Full 11+ application taxonomy — ★
  Named applications = points in continuous space — ★★
  Interoception habituation paradox — ★★
  PFC accessibility as spectrum — ★
  Entity-Access = neural migration (dorsal→ventral) — ★
  Engine use quality as universal modifier — ★
  1 training → N improvements model — ★
  Bidirectional spiral model — ★

═══════════════════════════════════════
🔴 HYPOTHESIS (testable but unverified)
═══════════════════════════════════════

  Exact number of distinct applications (11? more? fewer?)
  3-axis model completeness (are there more axes?)
  Interoception training → Self-Pattern-Modeling improvement (quantifiable?)
  Diversity threshold for self-model calibration
  Entity-Access migration speed along mPFC gradient
  Dream function as offline engine optimization
```

---

## §13 — CROSS-REFERENCES

| File | Sections | Relationship |
|------|----------|-------------|
| Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 | Full file | EVIDENCE file for this ARCHITECTURE |
| Self-Pattern-Modeling v3.1 | §2 (Compiled/Fresh), §10 (Self-Pattern-Modeling×Imagine-Final) | APPLICATION-1: Self-Pattern-Modeling mechanism |
| Imagine-Final.md v3.0 | Full file | APPLICATION-2: future simulation |
| Feeling.md v3.0 | §3 (PFC observation) | UMBRELLA — Feeling ⊃ Self-Observation |
| Self-Observation.md v1.0 | Full file | APPLICATION-3: Self × Present × Observe |
| Inter-Body-Mechanism.md v1.0 | §3 (Compiled/Fresh), §1 (Compilable Architecture) | SOURCE-OF-TRUTH for spectrum |
| PFC-Operations.md v1.0 | §5 (Compiled Quality), §9 (PFC Budget) | HOW PFC operates on engine |
| Entity-Access.md v1.1 | §3 (gradient model) | mPFC gradient = Entity-Access spectrum |
| Entity-Valence-Dynamics.md v2.0 | §4 (per-entity table) | Valence modulates engine output |
| Body-Feedback-Mechanism.md v2.1 | §3 (chunk dynamics, readout) | FOUNDATION: body-feedback |
| Dissonance-Signal-Architecture v1.0 | §7.1 (Simulation-Engine × dissonance type) | Simulation-Engine generates Evaluative Dissonance only |
| Connection.md v4.0 | §3 (3 primitives) | SOCIAL context for bidirectional loop |
| Compiled-Fresh.md v2.0 | §6.2 (compile-time direction lock) | MECHANISM: reflection vs rumination |
| Body-Coupling.md v2.0 | §2 (depth × direction) | Coupling uses engine for synchronization |

---

## §14 — RESEARCH CITATIONS

| # | Citation | Used in | Evidence |
|---|----------|---------|----------|
| R1 | Lombardo et al. 2010 — Shared self/other mentalizing circuits (J. Cog. Neurosci.) | §0, §6 | 🟢 fMRI |
| R2 | Mitchell, Macrae & Banaji 2006 — vMPFC/dMPFC dissociation (Neuron) | §2, §6 | 🟢 fMRI |
| R3 | Tamir & Mitchell 2010 — Clan mentality: vMPFC for close others (J. Neurosci.) | §2, §6 | 🟢 fMRI |
| R4 | Denny et al. 2012 — Spatial gradient meta-analysis mPFC | §2, §6 | 🟢 Meta |
| R5 | Bird, Silani et al. 2010 — Anterior insula shared readout (Brain) | §4, §7 | 🟢 fMRI |
| R6 | Bird & Cook 2013 — Alexithymia underlies social deficits | §7 | 🟢 |
| R7 | Mul et al. 2021 — Network analysis alexithymia central node (Eur. Arch. Psych.) | §7 | 🟢 |
| R8 | Fukushima, Terasawa et al. 2011 — Interoception → empathic accuracy | §4, §11 | 🟢 |
| R9 | Terasawa et al. 2021 — Interoception ↔ empathy bidirectional (Frontiers) | §4 | 🟢 |
| R10 | Schacter & Addis 2007 — Constructive episodic simulation (Nature Rev. Neurosci.) | §2, §5 | 🟢 ★ |
| R11 | Buckner, Andrews-Hanna & Schacter 2008 — DMN anatomy (Annals NYAS) | §5 | 🟢 |
| R12 | Buckner & Carroll 2007 — Self-projection and the brain | §0, §5 | 🟢 |
| R13 | Hassabis et al. 2007 — Hippocampal amnesia → cannot imagine (PNAS) | §5 | 🟢 |
| R14 | Schacter 2001 — Seven Sins of Memory: reconstructive recall | §5 | 🟢 |
| R15 | Van Hoeck et al. 2013 — Counterfactual shares episodic network | §2 | 🟢 fMRI |
| R16 | Greene et al. 2001 — Moral dilemmas activate vMPFC + TPJ | §2, §3 | 🟢 fMRI |
| R17 | Trapnell & Campbell 1999 — Self-reflection vs self-rumination | §9 | 🟢 |
| R18 | Joireman, Parrott & Hammersla 2002 — Reflection → empathy | §9 | 🟢 |
| R19 | Lopes, Salovey & Straus 2003 — Emotion regulation ↔ social interaction | §10 | 🟢 |
| R20 | Coan & Sbarra 2015 — Social Baseline Theory | §10 | 🟢 |
| R21 | Koudenburg et al. 2024 — Social → self-concept clarity (Eur. J. Soc. Psych.) | §10 | 🟢 |
| R22 | Gendlin 1978 — Focusing: body-readout improvement | §11 | 🟢 Clinical |
| R23 | Neuron 2023 — 20 years of the Default Mode Network (review) | §5 | 🟢 Review |
| R24 | Spreng & Grady 2010 — Memory + social cognition overlap (J. Cog. Neurosci.) | §5 | 🟢 fMRI |
| R25 | Gallese 2003, 2005 — Embodied simulation, shared manifold | §0 | 🟢 |
| R26 | Dimaggio & Lysaker 2015 — Metacognition + mentalizing coupled | §0 | 🟢 |
| R27 | Uddin, Iacoboni et al. 2007 — Self/other neural overlap | §6 | 🟢 fMRI |

---

> **Simulation-Engine.md v1.2**
>
> 1 general-purpose Simulation-Engine (not N separate modules).
> 3 Components: Interoception (display) × Constructive Simulation (CPU+RAM) × Self/Other Model (control panel).
> 3 Axes: Target × Time × Operation → application = coordinates in 3D space.
> 11+ applications mapped: Self-Pattern-Modeling / Self-Observation / Imagine-Final = 3 named points.
> Alexithymia = component failure → ALL applications fail = decisive shared-substrate proof.
> PFC accessibility spectrum: dream (zero) → decision-branching (maximum).
> Engine use quality: reflection (curiosity) vs rumination (threat) = universal modifier.
> Bidirectional loop: social ↔ self-regulation on shared substrate.
> Train 1 component → N improvements. 1 training → ≥4 applications improved.
> v1.2: Self-Observation.md v1.0 cross-refs.
>
> Version: v1.2, 2026-06-02.
