# Core-Hardware — Physical Architecture (Hardware Map)

> **Status:** v1.1 — 1 of 2 Core v8.0 maps
> **Date:** 2026-05-25 (v1.1 — Core-Interface.md → backup, 3→2 maps, Ask-AI.md = dynamic interface)
> **v1.0:** 2026-05-10
> **This map:** HARDWARE MAP — WHAT IS WHERE (physical architecture)
> **Other map:** Core-Software.md (HOW IT RUNS)
> **Interface:** Ask-AI.md (AI generates dynamic interface per user)
> **Supersedes:** Core-v7.8-Draft.md v0.2 §1.2 + §6.3 (split into 3 files)
> **Principles:**
> - 4 zones A/B/C/D by PFC accessibility gradient
> - Every claim verifiable via fMRI, lesion studies, tractography
> - Physical map — does NOT describe mechanism (→ Core-Software.md)
> - does NOT describe observer experience (→ Ask-AI.md: AI generates dynamic interface per user)
> **Prerequisites:** None — file is self-contained
> **Read deeper:** Neural-Architecture.md v1.0 (detail on each brain region)
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Language:** English

---

## Table of Contents

- §0 — THREE MAPS + WHAT THIS FILE DESCRIBES
- §1 — HARDWARE MAP — PHYSICAL ARCHITECTURE
- §2 — PFC REACH GRADIENT
- §3 — TIMING HIERARCHY
- §4 — RECEPTOR SYSTEM OVERVIEW
- §5 — HARDWARE PROFILE — INDIVIDUAL SPECS
- §6 — HARDWARE SETS RANGE, CHUNKS CHOOSE POSITION
- §7 — CROSS-REFERENCES

---

## §0 — THREE MAPS + WHAT THIS FILE DESCRIBES

### §0.1 Three Core Maps v8.0

The framework describes the body-brain system from 2 perspectives, each as a separate map:

| # | Map | Perspective | For | File |
|---|---|---|---|---|
| 1 | **Hardware Map** | **WHAT is WHERE** | **Neuroscience researcher** | **This file** |
| 2 | Software Map | HOW IT RUNS | Framework researcher | Core-Software.md |

Both maps describe the SAME system from different angles. Each can be read independently.
Like a computer: circuit diagram (Hardware) / code architecture (Software).
Framework interface: Ask-AI.md — AI reads the framework and adapts explanations to each person's level of understanding.

### §0.2 What This File Describes

A PHYSICAL MAP: WHAT is WHERE, what connects to what, individual specs.
For specialists who want to VERIFY the framework via fMRI, lesion studies, tractography.

This file does NOT describe:
- Mechanism (HOW things RUN) → Core-Software.md
- Observer experience (INTERACTION) → Ask-AI.md (AI generates dynamic interface per user)

---

## §1 — HARDWARE MAP — PHYSICAL ARCHITECTURE

```
🟡 PHYSICAL MAP — "WHAT IS WHERE, WHAT CONNECTS TO WHAT":

  PFC at top — because every observer observes via PFC.
  Domain wraps outside — body exists WITHIN domain.
  Gradient top-down: PFC reach DECREASES progressively.

  ┌─ DOMAIN (actual environment — exists objectively, domain does NOT lie) ────┐
  │                                                                              │
  │  ┌─ BODY (neural systems — physical architecture) ─────────────────────┐   │
  │  │                                                                      │   │
  │  │  ┌─ A: PFC ── observer + orchestrator ──────────────────────────┐   │   │
  │  │  │  dlPFC ── working memory (~4±1 slots), planning, control      │   │   │
  │  │  │  vlPFC ── response inhibition, rule maintenance               │   │   │
  │  │  │  OFC ── value computation, reward expectation                 │   │   │
  │  │  │  vmPFC ── emotion regulation, amygdala bridge (uncinate)      │   │   │
  │  │  │  mPFC ── self-referential, social cognition, DMN hub          │   │   │
  │  │  │  ACC* ── conflict monitoring (*PFC/limbic overlap)            │   │   │
  │  │  │  Online from birth (PFC-From-Prenatal). ⏱ ~200-500ms (SLOWEST)             │   │   │
  │  │  └─────────────────────────┬────────────────────────────────────┘   │   │
  │  │     Layer 2/3 connections — PFC reach: STRONG                       │   │
  │  │  ┌─────────────────────────┴────────────────────────────────────┐   │   │
  │  │  │  B: CORTICAL MODALITY ── PFC trainable ────────────────────   │   │   │
  │  │  │  Visual (V1→IT, FFA)  Auditory (A1)  Language (Broca+W)       │   │   │
  │  │  │    ⭐ Language dissociable from PFC (Fedorenko 2024)           │   │   │
  │  │  │  Somatosensory (S1/S2)  Motor (M1+premotor)                   │   │   │
  │  │  │  Cerebellum (motor+cognitive+prediction)                       │   │   │
  │  │  │  Insula (⭐ anterior = interoception integration, Craig 2002)  │   │   │
  │  │  │  Parietal (spatial, cross-modal)  Temporal (objects, social)    │   │   │
  │  │  │  ⏱ ~150-200ms cortical processing                             │   │   │
  │  │  └─────────────────────────┬────────────────────────────────────┘   │   │
  │  │     thalamocortical + BG loops — PFC reach: VARIABLE                │   │
  │  │  ┌─────────────────────────┴────────────────────────────────────┐   │   │
  │  │  │  C: SUBCORTICAL ── PFC reach limited ────────────────────     │   │   │
  │  │  │  Amygdala ── threat/reward ── vmPFC direct (uncinate)         │   │   │
  │  │  │  Hippocampus ── encoding gateway ── sleep replay → cortex     │   │   │
  │  │  │  Thalamus + TRN ── sensory gateway ── PFC can gate            │   │   │
  │  │  │  Hypothalamus ── HPA axis, homeostasis ── PFC indirect        │   │   │
  │  │  │  Basal Ganglia ── habit loops (associative → sensorimotor)    │   │   │
  │  │  │  Brainstem: VTA (dopamine), LC (NE, α1→PFC offline),         │   │   │
  │  │  │    Raphe (serotonin), PAG (pain/defense), NTS (visceral)      │   │   │
  │  │  │  DMN cross-cuts: mPFC(A) + PCC + angular + MTG               │   │   │
  │  │  │  ⏱ ~12ms amygdala (subcortical shortcut)                      │   │   │
  │  │  └─────────────────────────┬────────────────────────────────────┘   │   │
  │  │     vagus (80% afferent), spinal paths — PFC reach: WEAK           │   │
  │  │  ┌─────────────────────────┴────────────────────────────────────┐   │   │
  │  │  │  D: PERIPHERAL ── outside brain, PFC reach ≈ 0 ────────────  │   │   │
  │  │  │  ENS "second brain" (~100-500M neurons, 95% serotonin)        │   │   │
  │  │  │  Spinal cord (reflex, pain: A-delta + C-fiber)                │   │   │
  │  │  │  ANS (sympathetic / parasympathetic)                           │   │   │
  │  │  │    Breathing = UNIQUE voluntary-involuntary bridge             │   │   │
  │  │  │  Cardiac plexus (~40K neurons)                                 │   │   │
  │  │  │  ⏱ ~50ms spinal reflex (FASTEST — before brain)               │   │   │
  │  │  └──────────────────────────────────────────────────────────────┘   │   │
  │  │                                                                      │   │
  │  └──────────────────────────────────────────────────────────────────────┘   │
  │                                                                              │
  └──────────────────────────────────────────────────────────────────────────────┘
```

---

## §2 — PFC REACH GRADIENT

```
🟢 PFC REACH — GRADIENT, NOT BINARY:

  PFC "reach" = degree to which PFC can influence activity in a given zone.
  Determined by physical connectivity: axon pathways + synaptic relays.

  A → B: STRONG
    → Layer 2/3 direct connections (top-down bias)
    → PFC holds chunk → cortical area activates + runs
    → TRN (thalamic reticular nucleus) = attention gate PFC can control
    → Example: PFC holds "write text" → motor cortex executes
    → 🟢 Miller & Cohen 2001 — top-down control mechanism

  A → C: VARIABLE
    → vmPFC → amygdala DIRECT via uncinate fasciculus — emotion regulation
    → PFC → Basal Ganglia (indirect cortico-striatal loops) — habit influence
    → PFC → PAG/NTS (limited, multi-relay) — pain modulation, autonomic
    → BUT: PFC does NOT have direct access to hippocampal encoding process
    → BUT: PFC does NOT directly control VTA dopamine firing
    → 🟢 Ghashghaei et al. 2007 — prefrontal-amygdala connectivity

  A → D: WEAK
    → Minimum 2 synaptic relays (PFC → brainstem → peripheral)
    → PFC reach is nearly zero: ENS (gut), cardiac plexus, spinal reflex
    → UNIQUE EXCEPTION: Breathing
      → Voluntary: hold breath, deep breath (motor cortex → diaphragm)
      → Involuntary: brainstem controls (sleep, reflex, CO2 response)
      → = ONLY zone D system PFC can directly influence
    → 🟢 Del Negro et al. 2018 — respiratory rhythm generation

  ⭐ IMPLICATIONS:
    → PFC = observer + orchestrator → but the orchestra is ONLY strong in zones A+B
    → Zone C: PFC influence via INDIRECT pathways only
    → Zone D: PFC is nearly powerless (except breathing)
    → "Willpower" = PFC holds → biases zone B → hopes for cascade to C, D
    → = Why "control yourself" is fundamentally limited — PFC physical reach is limited
    → Mechanism detail: Core-Software.md §6.1-§6.2
```

---

## §3 — TIMING HIERARCHY

```
🟢 TIMING — PFC ALWAYS KNOWS LAST:

  ┌──────┬──────────┬───────────────────────────────────────────────────┐
  │ Zone │ Timing   │ What happens                                      │
  ├──────┼──────────┼───────────────────────────────────────────────────┤
  │ D    │ ~50ms    │ Spinal reflex (FASTEST — before brain)            │
  │ C    │ ~12ms    │ Amygdala subcortical shortcut (thalamus→amygdala) │
  │ B    │ ~150ms   │ Cortical processing (visual, auditory, motor)     │
  │ A    │ ~200ms+  │ PFC deliberate (SLOWEST — observer arrives LAST)  │
  └──────┴──────────┴───────────────────────────────────────────────────┘

  EVOLUTIONARY LOGIC:
    → D fastest: hand pulls back BEFORE the brain registers "hot" (survival reflex)
    → C fast: amygdala fires BEFORE PFC is aware (threat detection)
    → B medium: cortical integration → recognize object/pattern
    → A slowest: PFC evaluate + plan → only AFTER the body has already processed

  IMPLICATIONS:
    → Body processes FIRST → PFC ALWAYS knows LAST
    → The feeling "I decided" is actually PFC observing a decision ALREADY FORMED
    → 🟢 Libet 1983: readiness potential 300ms BEFORE conscious will
    → = Timing hierarchy supports "PFC = observer, not controller"

  CROSS-REFERENCE:
    → NE α1 FREEZE (Cortisol-Baseline.md §9.1):
      Threat → NE flood → PFC OFFLINE (ms) — design feature, NOT malfunction
      Shuts off PFC (slow) → yields to subcortical (fast) for survival
    → Mechanism detail: Core-Software.md §4.3
```

---

## §4 — RECEPTOR SYSTEM OVERVIEW

```
🟢🟡 17 RECEPTOR CATEGORIES — BODY-DOMAIN INTERFACE:

  Receptors = gateways for the body to receive input from domain.
  3 standard neuroscience taxonomy categories:

  EXTEROCEPTION — sensing the external world (5):
    ① Vision     — retina, V1→IT pathway, FFA (faces)
    ② Audition   — cochlea, A1, voice processing
    ③ Olfaction   — ~400 receptor types, DIRECT limbic (bypasses thalamus)
    ④ Gustation   — 5+1 basic tastes, chemoreceptors tongue/palate
    ⑤ Tactile     — mechanoreceptors + CT affective touch fibers

  PROPRIOCEPTION — sensing body position (3):
    ⑥ Proprioception — muscle spindles + joint receptors
    ⑦ Vestibular     — inner ear semicircular canals + otoliths
    ⑧ Kinesthetic    — muscle dynamics, exertion, fatigue sensing

  INTEROCEPTION — sensing internal state (9):
    ⑨ Thermoreception   — hypothalamic, ~37°C set point
    ⑩ Nociception       — A-delta (fast sharp) + C-fiber (slow dull)
    ⑪ Respiratory       — CO2 chemoreception, vagal afferents
    ⑫ Cardiovascular    — baroreceptors, HR, HRV, vagal tone
    ⑬ Visceral          — ENS (~100-500M neurons), gut-brain axis
    ⑭ Metabolic         — glucose, hydration, ghrelin/leptin
    ⑮ Hormonal-sensed   — cortisol, testosterone, oxytocin (downstream effects)
    ⑯ Sleep/Circadian   — SCN master clock, melatonin, REM/NREM
    ⑰ Self-signal interoception (META, KEYSTONE) ⭐

  ⭐ SELF-SIGNAL INTEROCEPTION = KEYSTONE:
    → Body's capacity to READ its own internal state
    → Hub: anterior insula (zone B, Craig 2002, 2009) + ACC
    → WITHOUT this: other inputs fire but body "cannot hear itself"
    → Explains alexithymia (~10% population, 🟢 Bird & Cook 2013)
    → Developmental foundation: caregiver mirroring → child learns self-reading

  HARDWARE PATHWAYS:
    → Exteroception: receptor → thalamus (zone C) → cortical area (zone B)
    → Exception: olfaction → DIRECT limbic (zone C, bypasses thalamus)
    → Interoception: vagus (80% afferent) + spinal → insula (zone B)
    → Nociception: dual pathway (A-delta fast via zone C, C-fiber slow)

  DETAIL: Body-Input-Enumeration.md (8-field schema per input)
  MECHANISM (delta rule, baseline adaptation): Core-Software.md §3
```

---

## §5 — HARDWARE PROFILE — INDIVIDUAL SPECS

```
🟢🟡 INDIVIDUAL HARDWARE SPECS — SLOW TO CHANGE:

  Each person has a different hardware profile.
  Hardware = RANGE. Chunks choose POSITION within the range (§6).
  Changes very slowly (genetic + epigenetic + structural development).

  ── PFC PARAMETERS ──

    WM CAPACITY: ~4±1 slots (🟢 Cowan 2001)
      → Beginner: slot = small chunk → little info
      → Expert: slot = meta-chunk → enormous info
      → = "Same 4 slots, different SIZE per slot"

    PFC-CLEAR-SPEED: COMT gene
      → Val/Val: clears dopamine fast → WM refreshes fast → good for switching
      → Met/Met: clears slowly → WM holds longer → good for sustained attention
      → 🟢 Egan et al. 2001 — COMT-WM relationship

    PFC-ATTENTION: DRD4 gene
      → 7R: longer receptor → higher novelty-seeking tendency
      → 4R: shorter receptor → higher attention stability
      → 🟢 Swanson et al. 2007

    PFC ONLINE FROM BIRTH (🟢 PFC-From-Prenatal):
      → 5 empirical pillars:
        Huttenlocher 1979: synaptic density at birth
        Doria 2010: functional networks at term
        Kouider 2013: frontal signatures at 5 months
        Grossmann 2009: fNIRS early PFC activity
        Hodel 2018: rapid plasticity
      → OLD claim: "PFC offline until age X"
      → CORRECTED: "PFC hardware online from birth, development = CHUNKS MISSING"

    PFC CONNECTIVITY LIMITS:
      → PFC connections primarily to cortical areas (zone B)
      → LIMITED direct connections to brainstem, ENS, amygdala
      → PFC CAN: fire patterns in zone B via top-down bias
      → PFC CANNOT: force fire in zone D (ENS) or directly in zone C (VTA)
      → PFC orchestration scope = f(physical connectivity)
      → 🟢 Measurable via fMRI, tractography — large individual variation

    PFC-INFERENCE LADDER (Chunk.md §8.4):
      L0: Reflex (no PFC involvement)
      L1: Orienting (PFC receives alert from body)
      L2: Pattern-match (PFC recognizes compiled pattern)
      L3: Deliberate comparison (Type 4 PFC chain)
      L4: Coordinated execution (multi-step PFC plan)
      → EVENT property, not AGE property

  ── BODY-WIDE PARAMETERS ──

    MOOD-STABILITY: MAO-A gene
      → Whole brain, not PFC-specific
      → Affects monoamine metabolism (serotonin, dopamine, NE)
      → 🟢 Caspi et al. 2002 — interaction with early adversity

    RECEPTOR VARIANTS:
      → OXTR: oxytocin receptor sensitivity (social bonding range)
      → TAS2R: bitter taste receptor (taste sensitivity range)
      → CT-fiber density: affective touch sensitivity
      → = Individual variation → different body-input sensitivity profiles

    MODALITY BALANCE:
      → Visual / auditory / somatic / motor / emotional processing mix
      → Property of the WHOLE brain, not PFC or subcortical alone
      → Influences: how chunks compile (multi-modal richness)
        and how PFC observes (which modality is dominant)
      → 🟡 Mainstream has not clearly defined the PFC vs subcortical
           boundary for modality
      → Framework position: modality = brain-wide hardware property

  DETAIL ON PFC FUNCTIONS: PFC-Function.md v1.1 (24 functions, sub-region mapping)
  DETAIL ON PFC MODES: PFC-Configuration.md v1.0 (6 dynamic configuration modes)
```

---

## §6 — HARDWARE SETS RANGE, CHUNKS CHOOSE POSITION

```
🟡 KEY PRINCIPLE — HARDWARE ≠ DESTINY:

  Hardware = RANGE of possible positions.
  Chunks (accumulated through experience) = ACTUAL POSITION within that range.

  EXAMPLE:
    WM capacity ~4±1 → beginner: 4 small items | expert: 4 meta-chunks
    COMT Val/Val → fast clear → but only useful when chunks for task-switching are compiled
    DRD4 7R → novelty-seeking tendency → but which direction depends on environmental exposure

  = NOT "PFC is strong/weak"
  = BUT "how many chunks are compiled for that situation"

  Different hardware → different optimal environments → different compiled chunks.
  SAME hardware + DIFFERENT environment → entirely DIFFERENT outcomes.
  DIFFERENT hardware + SAME environment → DIFFERENT adaptation strategies.

  FRAMEWORK POSITION:
    → Individual variation = hardware × environment × time
    → Talent = early compile advantage (environment happens to match hardware)
    → Not fixed destiny — chunks continue to compile throughout life
    → Critical periods: some hardware windows close
      (phoneme discrimination ~7-10yr, attachment style ~1-3yr)

  MECHANISM DETAIL: Core-Software.md §4.1 (compile rate, 3 Compile Types)
```

---

## §7 — CROSS-REFERENCES

### §7.1 Other Maps + Interface

```
  Core-Software.md   — HOW IT RUNS: cycle mechanism, chunk dynamics, body-feedback
  Ask-AI.md v3.1     — INTERFACE: AI generates dynamic interface per user (protocol + navigation)
```

### §7.2 Hardware ↔ Software Mapping

```
  Core-Software.md §1.3: mapping table (Software function → Hardware location)
  = "Body-Input at Receptors→D+C+B, PFC observes at A, Cortisol amplifier at C→cross-cutting"
```

### §7.3 Hardware Deep-Dive Files

```
  Neural-Architecture.md v1.0      — detail on each brain region, 4 zones A/B/C/D expanded
  Body-Input-Enumeration.md        — 17 body-inputs, 8-field schema per input
  Cortisol-Baseline.md v2.0        — HPA axis (zone C), NE mechanism, 7 modes
  PFC-Function.md v1.1             — 24 PFC functions, sub-region mapping
  PFC-Configuration.md v1.0        — 6 dynamic modes, survival matrix
```

### §7.4 Superseded Content

```
  Core-v7.8-Draft.md v0.2 §1.2     → replaced by this file §1 (Hardware Map diagram)
  Core-v7.8-Draft.md v0.2 §6.3     → replaced by this file §5 (Hardware Profile)
  Backup: _backup/Core-v7.8-Draft-pre-3maps.md
```

---

## Closing Note

**Core-Hardware v1.1** — 1 of 2 Core v7.8 maps.

Physical map: WHAT is WHERE, what connects to what, individual specs.
The shortest of the 2 files — intentionally brief.
Specialists can verify each brain region via fMRI, lesion studies, tractography.

Want to know HOW IT RUNS → Core-Software.md.
Want to INTERACT with the framework → Ask-AI.md (AI generates dynamic interface per user).

> *Core-Hardware — "4 zones A/B/C/D. PFC reach gradient: A→B strong, A→C variable,
> A→D weak. Timing: D fastest (50ms) → A slowest (200ms+). 17 receptor categories.
> Hardware sets RANGE, chunks choose POSITION. Hardware ≠ destiny.
> PFC hardware online from birth — development = chunks missing."*
