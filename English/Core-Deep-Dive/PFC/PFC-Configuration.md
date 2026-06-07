---
title: PFC-Configuration — Dynamic Function Configurations
version: 1.1
created: 2026-05-10
updated: 2026-05-15 (v1.1 — §2.1 PTSD ④↔⑤ oscillation + ADHD DMN interference + Parkinson gate, Health Conditions Drill)
status: REFERENCE v1.1
scope: |
  HOW PFC functions COMBINE in different brain states.
  6 Configuration Modes: Normal → Reallocation → Reconfigured → Disconnected →
    Hyperactivated → Disintegrated.
  PFC Control Spectrum: Overcontrol ↔ Balanced ↔ Undercontrol.
  24 Functions × 6 Sub-Regions Mapping (many-to-many, dlPFC hub).
  Configuration × Function Survival Matrix (which functions survive in which mode).
  Participation × Configuration: 2 orthogonal taxonomies.
  Strategy A→B Transition (defense strategy switch).
  System Reconsolidation (Config ⑥ × Function ⑭).
purpose: |
  PFC-Function.md answers: WHAT can PFC do? (24 functions, static listing)
  This file answers: HOW do functions COMBINE in different states? (dynamic configurations)
  Complement, not replacement. Different questions → different files.
  Source: Distilled from Drill-Reward-Feeling-Main.md v1.2 §3.18 (R2), §5b (R11-R12),
    §3.16 (R15), §3.17 (R16).
position: |
  PFC/ folder — alongside PFC-Function, PFC-Hardware, PFC-Development, PFC-Hold-Dimensions.
  Reading order: AFTER PFC-Function.md (need to know 24 functions) + PFC-Hardware.md (need to know hardware).
dependencies:
  - PFC-Function.md v1.1 — 24 functions, 5 categories, PFC offline cases
  - PFC-Hardware.md v1.0 — COMT, DRD4, NE α2/α1, PFC-Quality
  - Neural-Architecture.md §2 — 6 PFC sub-regions physical map
  - Drive.md v1.1 §2 — 6 PFC participation modes
  - Cortisol-Baseline.md v2.0 — cortisol triggers config ④
  - Reward-Signal-Architecture.md v1.0 — reward × config interaction
  - Threat.md — threat strategies × PFC configurations
  - Body-Coupling.md v1.0 — entanglement, caregiver paradox
drill_source: |
  Drill-Reward-Feeling-Main.md v1.2:
    §3.18 (R2) — PFC Sub-Region × Function × Mode Mapping
    §5b (R11+R12) — PFC Control Spectrum, 2 taxonomy orthogonal
    §3.16 (R15) — System Reconsolidation
    §3.17 (R16) — Strategy A→B Transition
language: English
source_version: Vietnamese v1.1
english_created: 2026-06-06
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# PFC Configuration — Dynamic Function Configurations

> **PFC-Function.md: 24 functions PFC CAN do (static).**
> **This file: HOW 24 functions COMBINE differently in different states (dynamic).**
>
> PFC is not a simple ON/OFF switch.
> PFC = a complex system with 6 CONFIGURATION MODES —
> each mode enables/disables/distorts DIFFERENT FUNCTIONS.
>
> Same PFC, same hardware, same 24 functions:
>   Flow (config ②): task-serving ON, self-monitoring OFF — effortless.
>   Threat (config ④): ALL PFC functions OFF — subcortical takeover.
>   Dissociation (config ⑤): 4 functions WEAPONIZED — emotional numbness.
>   Psychedelic (config ⑥): nearly ALL OFF, ⑭ Modify ENHANCED — structural change.
>
> Configuration ≠ Participation (Drive.md §2). Orthogonal but constrained.
> "How BUSY is PFC" (participation) ≠ "How is PFC WIRED" (configuration).
>
> This file: HOW combines. PFC-Function.md: WHAT. Neural-Architecture.md §2: WHERE.

---

## Table of Contents

- §0 — Position + Scope
- §1 — Why Not Just ON/OFF
- §2 — 6 Configuration Modes
- §3 — PFC Control Spectrum
- §4 — 24 Functions × 6 Sub-Regions Mapping
- §5 — Configuration × Function Survival Matrix
- §6 — Participation × Configuration: 2 Orthogonal Taxonomies
- §7 — Strategy A→B Transition (Defense Strategy Switch)
- §8 — System Reconsolidation (Config ⑥ × Function ⑭)
- §9 — Honest Assessment
- §10 — Cross-References

---

## §0 — Position + Scope

```
⭐ THIS FILE ANSWERS A DIFFERENT QUESTION:

  PFC-Function.md — WHAT (24 functions, individual listing):
    "PFC can observe, hold, process, orchestrate, strategize."
    = STATIC listing — functions exist REGARDLESS of brain state.

  PFC-Configuration.md — HOW COMBINE (6 modes, dynamic):
    "In flow, which functions are ACTIVE? In threat, which functions are LOST?"
    = DYNAMIC listing — configuration changes WITH brain state.

  PFC-Hardware.md — WHY DIFFERENT (COMT, DRD4, NE):
    "Why do 2 people with the same config produce different output?"
    = Hardware parameters affect QUALITY per-function.

  Neural-Architecture.md §2 — WHERE (6 sub-regions physical):
    "Where is dlPFC? What does vmPFC connect to?"
    = PHYSICAL MAP — anatomy.


  WHY CREATE A NEW FILE (not merge into PFC-Function):
  ┌──────────────────────────────────────────────────────────┐
  │ PFC-Function.md = 446L, compact, well-structured.        │
  │ 6 modes + survival matrix + control spectrum = ~800L+.   │
  │ Merging in → 446L → ~1,200L+ → loses focus.             │
  │                                                           │
  │ Different ABSTRACTION LAYER:                               │
  │   PFC-Function = "the car can turn, brake, accelerate"    │
  │   PFC-Configuration = "the car in sport, eco, off-road"   │
  │   → Each mode enables/limits DIFFERENT CAPABILITIES        │
  └──────────────────────────────────────────────────────────┘

  Source: Distilled from Drill-Reward-Feeling-Main.md v1.2 §3.18 (R2), §5b (R11-R12),
          §3.16 (R15), §3.17 (R16). DISTILLED, not copied.
```

---

## §1 — Why Not Just ON/OFF

```
⭐ PFC-FUNCTION §7 CURRENTLY ONLY HAS "OFFLINE CASES":

  PFC-Function.md §7 lists 4 cases of PFC going offline:
    Alcohol intoxication → GABA suppress → PFC lost
    Deep sleep → NREM → PFC off
    NE α1 flood → circuit breaker → PFC disconnect
    Cortisol extreme → PFC dendrite damage

  = 1 SINGLE MODE: ON vs OFF.
  = "The car either runs or the engine is off."


  REALITY: 6 DIFFERENT CONFIGURATIONS:

  PFC is not just ON/OFF. There are at least 6 distinct configurations,
  each enabling/disabling/distorting DIFFERENT FUNCTIONS.

  ┌────────────────────────────────────────────────────────────┐
  │ Config ④ = current PFC-Function.md §7 ("offline cases")    │
  │                                                             │
  │ BUT 5 MORE CONFIGS EXIST:                                   │
  │                                                             │
  │ ① Normal: ALL 24 functions available — baseline.            │
  │ ② Reallocation: task-ON, self-OFF — flow.                   │
  │ ③ Reconfigured: suggestion-guided — meditation, hypnosis.  │
  │ ⑤ Hyperactivated: 4 functions WEAPONIZED — dissociation.    │
  │ ⑥ Disintegrated: nearly all OFF, ⑭ ENHANCED — psychedelic. │
  │                                                             │
  │ → Config ④ ≠ "PFC broken." Config ④ = 1/6 functional modes.│
  │ → Config ⑤ ≠ "PFC strong." Config ⑤ = pathological overuse.│
  │ → Config ⑥ ≠ "PFC random." Config ⑥ = unique access ⑭.    │
  └────────────────────────────────────────────────────────────┘


  🟡 EVOLUTIONARY LOGIC:

  Each configuration = DESIGN FEATURE, not a flaw:
    ① Normal: all functions ready → flexible processing
    ② Reallocation: focused → deep performance
    ③ Reconfigured: meditation/hypnosis state → learning mode
    ④ Disconnected: PFC slow (~200ms+) → subcortical fast (~12ms) → survival
    ⑤ Hyperactivated: when escape impossible → disconnect pain → survive
    ⑥ Disintegrated: structural change possible → reconsolidation window

  → Config ④ = current §7 PFC-Function.md (offline cases).
  → Details on the 5 remaining configs: §2 below.
  → Source: Drill §5b + §3.18
```

---

## §2 — 6 Configuration Modes

```
⭐⭐ 6 PFC CONFIGURATION MODES — qualitative states:

  Configuration = "How is PFC WIRED?" (qualitative)
  ≠ Participation = "How BUSY is PFC?" (quantitative, Drive.md §2)
  2 taxonomies ORTHOGONAL — details: §6.


  ═══════════════════════════════════════════════════
  CONFIG ① — NORMAL (baseline)
  ═══════════════════════════════════════════════════

  All 24 functions AVAILABLE, moderate intensity.
  PFC coordinates normally — observe, hold, process, orchestrate, strategize.

  Characteristics:
    → dlPFC: full access (15/24 functions available)
    → ACC: conflict monitoring active
    → vmPFC: emotional bridge working
    → All sub-regions: coordinate normally
    → Self-monitoring: ON
    → Task-processing: ON

  When: ~60-70% of waking time, safe context, no threat/flow/trauma.
  (⚠️ % = calibration anchor, not precise measurement)
  = "Default operating system." All functions AVAILABLE but NONE optimal
    (jack of all trades).

  Drive participation: can combine with Drive-PFC-Absent through Override (Drive.md §2).


  ═══════════════════════════════════════════════════
  CONFIG ② — REALLOCATION (flow)
  ═══════════════════════════════════════════════════

  🟢 dlPFC SPLIT: task-serving ON, self-monitoring OFF.

  Characteristics:
    → dlPFC task functions: ✅ active (⑤ Hold, ⑥ Quick Search, ⑨ Linking)
    → dlPFC self-monitoring: ❌ off (④ Meta-cognition, ⑰ Self-Pattern-Modeling suppressed)
    → ACC: minimal — conflict monitoring reduced (everything smooth)
    → Result: PFC bandwidth REALLOCATED 100% into task
    → Self-reference SILENT → "time flies", no self-consciousness

  🟢 Limb & Braun 2008:
    → fMRI of jazz musicians improvising:
    → dlPFC deactivation = PARTIAL, not uniform
    → Task-serving active, self-monitoring inactive
    → = SELECTIVE within single sub-region

  Framework interpretation:
    → Flow = PFC reallocation, NOT PFC offline
    → Csikszentmihalyi "loss of self-consciousness" = self-monitoring OFF
    → "Effortless" feeling = ACC quiet (no conflict detected)
    → "Time flies" = temporal monitoring OFF (mPFC self-reference off)

  When: flow state — expertise + challenge + no interruption.
  Flow prerequisites details: Drill §6.1
  Drive participation: typically Drive-PFC-Resolve — scan → match → act.
  🟢 Csikszentmihalyi 1990, Limb & Braun 2008, Dietrich 2004


  ═══════════════════════════════════════════════════
  CONFIG ③ — RECONFIGURED (meditation, hypnosis)
  ═══════════════════════════════════════════════════

  🟡 dlPFC reduced, DMN altered, suggestion-guided processing.

  Characteristics:
    → dlPFC: reduced — less executive control
    → mPFC/DMN: ALTERED (not default, not suppressed — reconfigured)
    → Suggestion/intention: guides which functions active
    → Some functions enhanced, some suppressed — depends on practice type

  Meditation variants:
    Focused attention (Samatha): ⑮ Gate Attention enhanced, ⑦ Loose Hold off
    Open monitoring (Vipassana): ④ Meta-cognition enhanced, ⑨ Linking reduced
    Loving-kindness: ⑰ Self-Pattern-Modeling enhanced, dlPFC task-functions reduced

  Hypnosis:
    → ACC: conflict monitoring REDUCED (suggestions not checked)
    → dlPFC: executive control reduced → suggestions bypass normal filters
    → 🟢 Raz et al. 2005: Stroop interference eliminated under hypnosis
    → = ACC not flagging conflicting signals

  When: deliberate practice, trained states, guided contexts.
  Drive participation: typically Drive-PFC-Resolve/Strategic in training context.
  🟢 Lutz et al. 2008 (meditation neuroscience), Raz et al. 2005 (hypnosis)
  🟡 Meditation as "reconfigured" (not just "reduced") = framework


  ═══════════════════════════════════════════════════
  CONFIG ④ — DISCONNECTED (acute threat)
  ═══════════════════════════════════════════════════

  🟢 PFC OFFLINE — ALL functions lost. Subcortical takeover.
  = Current PFC-Function.md §7 ("PFC Offline Cases").

  Characteristics:
    → ALL PFC sub-regions: disconnected (NE α1 floods)
    → Amygdala: DOMINANT (threat processing)
    → Basal ganglia: compiled responses READY
    → = ALL 24 functions LOST

  Mechanism (PFC-Hardware.md §6):
    → Threat detected → amygdala → LC → NE flood
    → NE high → α1 receptors activate → PFC networks disconnect
    → Subcortical faster (~12ms amygdala vs ~200ms+ PFC)
    → = Design feature: survival DOES NOT NEED deliberation

  Recovery: seconds after threat passes (NE drops → PFC reconnects).
  ≠ Damage (chronic cortisol = REAL damage).
  = Strategy A defense — "fight/flight" pathway. Details: §7.

  When: acute threat (real or perceived).
  Drive participation: Drive-PFC-Absent — PFC absent BECAUSE disconnected.
  🟢 Arnsten 2009, LeDoux 1996, Mobbs et al. 2007


  ═══════════════════════════════════════════════════
  CONFIG ⑤ — HYPERACTIVATED (dissociation)
  ═══════════════════════════════════════════════════

  🟢 PFC HYPERACTIVATED — 4 functions WEAPONIZED.
  OPPOSITE of config ④: PFC OVERACTIVE, not offline.

  Characteristics:
    → vlPFC: ⑱ Inhibit = ⭐MAXIMUM → suppress amygdala → emotional NUMBNESS
    → mPFC: ④ Meta-cognition = ⚠️EXCESSIVE → "watching self from outside"
      = depersonalization (🟢 Sierra & Berrios 1998)
    → dlPFC: ⑧ Active Lock = ⚠️CHRONIC → hypervigilance (cannot release)
    → vlPFC+dlPFC: ⑲ Override = ⚠️CHRONIC → "going through the motions"

  4 functions designed for SHORT-TERM use → CHRONIC = damage:
    → ⑱ Inhibit: normally = "don't say that" (seconds)
      Weaponized = emotional numbness CHRONIC (months-years)
    → ④ Meta-cognition: normally = "what am I thinking?" (useful)
      Weaponized = "I watch myself live" → depersonalization
    → ⑧ Active Lock: normally = Zeigarnik unfinished task (hours)
      Weaponized = hypervigilance 24/7
    → ⑲ Override: normally = "tolerating hunger for a deadline" (temporary)
      Weaponized = "going through life without feeling" (chronic)

  Config ⑤ = Drive-PFC-Override AUTOMATIC + CHRONIC:
    → Drive-PFC-Override normally: deliberate, temporary, costly but purposeful
    → Config ⑤: body auto-activates, chronic, EXTREMELY HIGH cost
    → = Strategy B defense — "freeze/dissociate" pathway. Details: §7.

  🟢 Lanius et al. 2010: dissociative PTSD subtype:
    → PFC hyperactive, amygdala suppressed
    → MORE COMMON in early childhood trauma
    → = Strategy A failed (inescapable) → Strategy B compiled as DEFAULT

  When: inescapable threat, caregiver trauma, chronic unsafe context.
  Drive participation: Drive-PFC-Override — stuck in override.
  🟢 Lanius 2010, Sierra & Berrios 1998
  🟡 "4 functions weaponized" taxonomy = framework


  ═══════════════════════════════════════════════════
  CONFIG ⑥ — DISINTEGRATED (psychedelic / reconsolidation)
  ═══════════════════════════════════════════════════

  🟢 DMN DISINTEGRATED. Hierarchy flat. ⑭ Modify Chunks ENHANCED.

  Characteristics:
    → DMN: DISINTEGRATED (not suppressed — collapsed)
      🟢 Carhart-Harris et al. 2012, Tagliazucchi et al. 2016
    → Top-down priors: RELAXED
      🟢 REBUS model (Carhart-Harris & Friston 2019)
    → Nearly ALL functions: ❌ offline (no quality control)
    → EXCEPT ⑭ Modify Existing Chunks: ⭐ENHANCED

  ⑭ ENHANCED = reconsolidation window:
    → Normally: recall chunk → labile → modify → re-compile (per-chunk)
    → Config ⑥: MANY chunks simultaneously labile → TOPOLOGY modifiable
    → = Not just modify 1 chunk — modify RELATIONSHIP STRUCTURE between chunks
    → = System reconsolidation (details: §8)

  Differs from meditation (config ③):
    → Meditation: DMN SUPPRESSED → intact but quiet → peaceful
    → Psychedelic: DMN DISINTEGRATED → collapsed → ego dissolution
    → = Suppress vs disintegrate = qualitatively different

  When: psychedelic session, deep meditation states (rare), near-death.
  Drive participation: N/A — modes break down (no coherent participation).
  🟢 Griffiths et al. 2006, Carhart-Harris 2012, 2019
  🟡 Config ⑥ as distinct mode (not just "intense config ③") = framework


  ═══════════════════════════════════════════════════
  6 MODES SUMMARY:
  ═══════════════════════════════════════════════════

  ┌────────┬──────────────────┬────────────────────┬──────────────────────┐
  │ Config │ Name             │ PFC State          │ Key Feature          │
  ├────────┼──────────────────┼────────────────────┼──────────────────────┤
  │ ①      │ Normal           │ All available      │ Baseline operation   │
  │ ②      │ Reallocation     │ Task ON, self OFF  │ Flow, deep perform.  │
  │ ③      │ Reconfigured     │ Altered, guided    │ Meditation, hypnosis │
  │ ④      │ Disconnected     │ ALL offline        │ Acute threat (Str.A) │
  │ ⑤      │ Hyperactivated   │ 4 func. weaponized │ Dissociation (Str.B) │
  │ ⑥      │ Disintegrated    │ ALL off, ⑭ enhance │ Reconsolidation      │
  └────────┴──────────────────┴────────────────────┴──────────────────────┘

  Source: Drill §5b (R11+R12 synthesis) + §3.18 (R2 mapping).
```

### §2.1 — Clinical Illustrations: PTSD + ADHD + Parkinson (v1.1)

```
⭐ HEALTH CONDITIONS DRILL VALIDATES CONFIGURATION MODEL:

  PTSD: ④ ↔ ⑤ OSCILLATION (PTSD-Analysis.md §4.4):
    → Flashback/hyperarousal = Config ④ (PFC offline, amygdala dominant)
    → Dissociative episodes = Config ⑤ (PFC hyperactive → numbness)
    → Patient OSCILLATES between 2 configs ← body-feedback drives switch:
      Cue → amygdala fire → ④ (flooding) → overwhelm → body switch → ⑤ (numbing)
    → Dissociative subtype (🟢 Lanius 2010): Config ⑤ compiled as DEFAULT
      = Strategy B compiled because Strategy A was INESCAPABLE (caregiver trauma)
    → = ④↔⑤ oscillation = clinical VALIDATION of 2 distinct defense modes
    → Cross-ref: §7 Strategy A→B Transition

  ADHD: DMN INTERFERENCE → Config ① UNSTABLE (ADHD-Observation.md §8):
    → Normal: Config ① = DMN suppressed, TPN active (clean switch)
    → ADHD: DMN-TPN anticorrelation REDUCED (🟢 Sonuga-Barke & Castellanos 2007)
    → = Config ① UNSTABLE → micro-lapses toward DMN
    → PFC dopamine too brief (DAT fast clear) → cannot MAINTAIN suppression
    → = PFC naturally DRIFTS when out of fuel (NOT "lazy" — hardware fuel issue)
    → Methylphenidate: block DAT → dopamine sustain → Config ① stable
    → 🟢 Liddle 2011: methylphenidate modulates DMN anticorrelation in ADHD

  PARKINSON: MASKED FACE = Config ① with execution BLOCKED (Parkinson-Analysis §5.4):
    → PFC = Config ① (all functions AVAILABLE, emotions FELT)
    → Basal ganglia gate LOCKED → facial/vocal expression BLOCKED
    → = Configuration INTACT but body-output GATE problem
    → Others model patient via Self-Pattern-Modeling → "why such a cold face?" → MISATTRIBUTE
    → = Config vs Execution distinction: PFC state ≠ body-output
    → Framework: Config ④ = PFC offline. Parkinson ≠ Config ④ (PFC online!)

  🟡 3 conditions × 3 configuration insights = framework synthesis
  → PTSD validates ④↔⑤. ADHD validates ① instability. Parkinson validates config≠execution.
```

---

## §3 — PFC Control Spectrum

```
⭐⭐ 3 ZONES ON THE PFC CONTROL SPECTRUM:

  Config ④⑤⑥ = 3 ATYPICAL states.
  Arranged along a CONTROL SPECTRUM:


  OVERCONTROL ←←←←←←←←← BALANCED →→→→→→→→→ UNDERCONTROL
       ⑤                 ①②③                    ⑥
  Dissociation          Normal range           Psychedelic
  PFC SUPPRESS          PFC coordinate         PFC DISINTEGRATE
  emotion               processing              hierarchy


  ┌────────────────────┬──────────────────┬────────────────────┐
  │ OVERCONTROL (⑤)    │ BALANCED (①②③)   │ UNDERCONTROL (⑥)   │
  ├────────────────────┼──────────────────┼────────────────────┤
  │ Emotion: NUMB      │ Emotion: FELT    │ Emotion: FLOOD     │
  │ Self: EMPTY        │ Self: PRESENT    │ Self: DISSOLVED    │
  │ Perception: intact │ Perception:      │ Perception:        │
  │  but colorless     │  normal          │  altered/intense   │
  │ PFC: HYPERACTIVE   │ PFC: balanced    │ PFC: DISINTEGRATED │
  │ vmPFC ↑↑ suppress  │ Balance          │ 5-HT2A disrupt     │
  │  amygdala          │                  │  Layer V pyramids  │
  │ Duration: chronic  │ Duration:        │ Duration: hours    │
  │  (months-years)    │  default         │  (acute)           │
  ├────────────────────┼──────────────────┼────────────────────┤
  │ Therapeutic:       │                  │ Therapeutic:       │
  │  re-connect body   │                  │  schema destabil.  │
  │  (somatic therapy) │                  │  + guided recomp.  │
  │  Direct-State      │                  │  set & setting     │
  │  "backdoor"        │                  │  = compile direct. │
  │  = body-level      │                  │                    │
  └────────────────────┴──────────────────┴────────────────────┘


  ⭐ 3 KEY INSIGHTS:

  ① Dissociation (⑤) and Psychedelic (⑥) = 2 OPPOSITE EXTREMES:
    → Dissociation: TOO MUCH PFC control → emotional emptiness
    → Psychedelic: TOO LITTLE PFC control → emotional flood
    → NOT 2 diseases → 2 EXTREMES ON THE SAME SPECTRUM
    → Therapeutic implications ARE OPPOSITE:
      Overcontrol → needs to REDUCE control (somatic therapy, body reconnect)
      Undercontrol → needs GUIDED control (therapist, integration)

  ② Config ④ (Disconnected) STANDS OUTSIDE this spectrum:
    → ④ = PFC NO LONGER EXISTS (completely offline, NE α1)
    → ⑤ = PFC TOO ACTIVE (hyperactivated)
    → ⑥ = PFC DISINTEGRATED
    → ④ = another dimension entirely (present/absent), not a degree of control

  ③ NOT linear scale — qualitatively different states:
    → Overcontrol: vlPFC inhibit MAX + meta-cognition excessive
    → Undercontrol: 5-HT2A agonism + DMN disintegration
    → = DIFFERENT neurochemical mechanisms, not "more/less of same thing"
    → = WHY you can't "gradually slide" from ⑤ to ⑥ along spectrum
      (different entry mechanisms, different neurochemistry)


  EVALUATIVE/DIRECT-STATE REWARD × CONTROL SPECTRUM:

  Overcontrol (⑤): Evaluative SUPPRESSED (evaluation numb), Direct-State PARTIALLY intact
    → Touch, exercise = may penetrate numbness (CT afferents below PFC level)
    → = "Backdoor" for therapy (body-level, bypasses PFC overcontrol)
    → Source: Reward-Signal-Architecture.md §1

  Balanced (①②③): Both Evaluative and Direct-State operational, Evaluative/Direct-State ratio varies.

  Undercontrol (⑥): Evaluative DISRUPTED (evaluation circuits disintegrated),
    Direct-State LESS AFFECTED (hardware-level, below disruption)
    → Touch, body grounding = STABLE across PFC states
    → = Safety anchor during psychedelic session

  → Direct-State = potentially STABLE across entire spectrum
  → Evaluative = VARIES dramatically with PFC state
  → 🟡 Framework synthesis: Direct-State stability across PFC configs


  🟢 Research:
    Lanius et al. 2010 — dissociation = PFC hyperactivation (⑤)
    Carhart-Harris & Friston 2019 — REBUS model, psychedelic = undercontrol (⑥)
    Sierra & Berrios 1998 — depersonalization phenomenology
    Griffiths et al. 2006 — psychedelic lasting change

  Source: Drill §5b.2 (PFC Control Spectrum).
```

---

## §4 — 24 Functions × 6 Sub-Regions Mapping

```
⭐⭐ MANY-TO-MANY MAPPING — 24 functions × 6 sub-regions:

  Each function = PRIMARY sub-region + SECONDARY support.
  Each sub-region serves MULTIPLE functions.
  NOT 1:1 — 1 sub-region can serve 15 functions.


  OBSERVE (4):
  ┌────────────────────────┬────────────┬──────────────┬───────────────────┐
  │ Function               │ Primary    │ Secondary    │ Evidence          │
  ├────────────────────────┼────────────┼──────────────┼───────────────────┤
  │ ① Observe Feeling      │ vmPFC      │ ant. insula  │ 🟢 Damasio 1994   │
  │ ② Observe Body Vote    │ ACC        │ OFC          │ 🟢 Botvinick 2004 │
  │ ③ Observe Chunk Active │ dlPFC      │ mPFC         │ 🟡                │
  │ ④ Meta-cognition       │ mPFC       │ ACC          │ 🟢 Fleming 2012   │
  └────────────────────────┴────────────┴──────────────┴───────────────────┘

  HOLD (4):
  ┌────────────────────────┬────────────┬──────────────┬───────────────────┐
  │ ⑤ Hold ~4±1            │ dlPFC      │ —            │ 🟢 Goldman-R 1995 │
  │ ⑥ Quick Search         │ dlPFC      │ —            │ 🟢 Fuster 1973    │
  │ ⑦ Loose Hold           │ dlPFC ↓    │ mPFC/DMN ↑   │ 🟡 DMN creativity │
  │ ⑧ Active Lock          │ dlPFC      │ ACC (unresol)│ 🟢 Zeigarnik 1927 │
  └────────────────────────┴────────────┴──────────────┴───────────────────┘

  PROCESS (6):
  ┌────────────────────────┬────────────┬──────────────┬───────────────────┐
  │ ⑨ Type 4 Linking       │ dlPFC      │ ACC          │ 🟡                │
  │ ⑩ Imagination          │ dlPFC+mPFC │ OFC          │ 🟢 Hassabis 2007  │
  │ ⑪ Domain-Check         │ dlPFC+ACC  │ OFC          │ 🟡                │
  │ ⑫ Label Creation       │ dlPFC+vlPFC│ Broca's      │ 🟡                │
  │ ⑬ Create New Chunks    │ dlPFC      │ ACC          │ 🟡                │
  │ ⑭ Modify Existing      │ dlPFC      │ vmPFC        │ 🟢 Nader 2000     │
  └────────────────────────┴────────────┴──────────────┴───────────────────┘

  ORCHESTRATE (6):
  ┌──────────────────────────────┬────────────┬──────────────┬───────────────────┐
  │ ⑮ Gate Attention TRN         │ dlPFC→TRN  │ —            │ 🟢 McAlonan 2008  │
  │ ⑯ Bias Spreading Activation  │ dlPFC      │ cortical     │ 🟡                │
  │ ⑰ Invoke Self-Pattern-Modeling│ mPFC+vmPFC │ TPJ          │ 🟢 Saxe 2006      │
  │ ⑱ Inhibit Compiled           │ vlPFC      │ —            │ 🟢 Aron 2004      │
  │ ⑲ Override Satisfaction      │ vlPFC+dlPFC│ ACC          │ 🟡                │
  │ ⑳ Change Environment         │ dlPFC      │ vmPFC+OFC    │ 🟡                │
  └──────────────────────────────┴────────────┴──────────────┴───────────────────┘

  STRATEGIC (4):
  ┌──────────────────────────────┬────────────┬──────────────┬───────────────────┐
  │ ㉑ Smooth Melody              │ ACC+dlPFC  │ vmPFC        │ 🟡                │
  │ ㉒ Choose Between Goals       │ OFC+dlPFC  │ vmPFC        │ 🟢 Padoa-S 2011   │
  │ ㉓ Accept Temporary Dissonance│ ACC+dlPFC  │ vmPFC        │ 🟡                │
  │ ㉔ Hijack Body-Input          │ dlPFC      │ motor cortex │ 🟡                │
  └──────────────────────────────┴────────────┴──────────────┴───────────────────┘


  ⭐ dlPFC AS HUB + BOTTLENECK:

  Sub-region involvement count (primary + secondary):

  ┌──────────┬──────────┬──────────────────────────────────────┐
  │ Region   │ Count    │ Role                                 │
  ├──────────┼──────────┼──────────────────────────────────────┤
  │ dlPFC    │ 15/24    │ HUB — working memory + cognitive     │
  │          │          │ control. Shared across TOO MANY      │
  │          │          │ functions → bottleneck.              │
  ├──────────┼──────────┼──────────────────────────────────────┤
  │ ACC      │  8/24    │ QUALITY CONTROLLER — conflict/error  │
  │          │          │ across all processes.                │
  ├──────────┼──────────┼──────────────────────────────────────┤
  │ vmPFC    │  6/24    │ EMOTIONAL BRIDGE — body-signal       │
  │          │          │ integration, somatic markers.        │
  ├──────────┼──────────┼──────────────────────────────────────┤
  │ OFC      │  5/24    │ VALUE COMPUTER — reward/value        │
  │          │          │ evaluation, flexible updating.       │
  ├──────────┼──────────┼──────────────────────────────────────┤
  │ mPFC     │  5/24    │ SELF + SOCIAL — self-reference,      │
  │          │          │ social modeling, DMN hub.            │
  ├──────────┼──────────┼──────────────────────────────────────┤
  │ vlPFC    │  3/24    │ INHIBITION SPECIALIST — stop-signal  │
  │          │          │ + rule. FEW functions but HIGH impact.│
  └──────────┴──────────┴──────────────────────────────────────┘


  ⭐ IMPLICATIONS:

  ① dlPFC 15/24 = WM ~4±1 EXPLAINED:
    → dlPFC = shared resource across TOO MANY functions
    → 15 functions competing for SAME workspace → capacity limit
    → = PFC-Hold-Dimensions.md: why ~4±1 (physics constraint)

  ② Flow requires dlPFC REALLOCATION:
    → 15 competing functions → config ②: task-serving ONLY
    → Self-monitoring OFF → bandwidth freed → deep performance
    → = Limb & Braun 2008: dlPFC SPLIT, not uniform deactivation

  ③ Cortisol damages dlPFC → 15/24 impaired:
    → 🟢 McEwen 2007: chronic cortisol → dlPFC dendrite retraction
    → dlPFC is bottleneck → damage = cascading impairment
    → = WHY chronic stress "impairs everything PFC" — hub damage

  ④ vlPFC only 3/24 BUT high-impact:
    → vlPFC damage = disinhibition (🟢 Phineas Gage case)
    → ⑱ Inhibit = critical for social functioning
    → 3 functions, MASSIVE behavioral impact

  ⑤ WITHIN-REGION FUNCTION SPLITTING:
    → dlPFC serves BOTH task-functions AND self-monitoring
    → Config ②: task ON, self OFF — WITHIN same sub-region
    → 🟢 Limb & Braun 2008: selective deactivation, not uniform
    → = WHY flow = "effortless but effective"

  Source: Drill §3.18 ❶❷ (R2 drill).
```

---

## §5 — Configuration × Function Survival Matrix

```
⭐⭐ WHICH FUNCTIONS SURVIVE IN WHICH CONFIGURATION?

  Legend: ✅ = active  ⚠️ = altered  ❌ = offline  ⭐ = enhanced


  OBSERVE (4):
  ┌──────────────────┬────────┬────────┬────────┬────────┬────────┬────────┐
  │ Function         │①Normal │②Reallo │③Reconf │④Discon │⑤Hyper  │⑥Disint │
  ├──────────────────┼────────┼────────┼────────┼────────┼────────┼────────┤
  │ ① Observe Feel   │ ✅     │ ⚠️task │ ⚠️alt  │ ❌     │ ⚠️over │ ❌flood│
  │ ② Body Vote      │ ✅     │ ✅task │ ⚠️sugg │ ❌     │ ❌supp │ ❌     │
  │ ③ Chunk Active   │ ✅     │ ✅task │ ⚠️     │ ❌     │ ⚠️narr │ ❌chao │
  │ ④ Meta-cognition │ ✅     │ ❌     │ ✅trn  │ ❌     │ ⚠️exc  │ ❌     │
  └──────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘

  HOLD (4):
  ┌──────────────────┬────────┬────────┬────────┬────────┬────────┬────────┐
  │ ⑤ Hold ~4±1      │ ✅     │ ✅task │ ⚠️     │ ❌     │ ⚠️rig  │ ❌     │
  │ ⑥ Quick Search   │ ✅     │ ✅fast │ ✅     │ ❌     │ ✅     │ ❌     │
  │ ⑦ Loose Hold     │ ✅     │ ❌     │ ✅     │ ❌     │ ❌     │ ❌     │
  │ ⑧ Active Lock    │ ✅     │ ❌flow │ ✅     │ ❌     │ ⚠️chr  │ ❌     │
  └──────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘

  PROCESS (6):
  ┌──────────────────┬────────┬────────┬────────┬────────┬────────┬────────┐
  │ ⑨ Type 4 Link    │ ✅     │ ✅task │ ⚠️     │ ❌     │ ⚠️narr │ ❌     │
  │ ⑩ Imagination    │ ✅     │ ✅task │ ⚠️sugg │ ❌     │ ⚠️dist │ ❌     │
  │ ⑪ Domain-Check   │ ✅     │ ✅cont │ ⚠️     │ ❌     │ ⚠️bias │ ❌     │
  │ ⑫ Label          │ ✅     │ ✅     │ ✅     │ ❌     │ ✅     │ ❌     │
  │ ⑬ Create Chunks  │ ✅     │ ✅     │ ❌     │ ❌     │ ❌     │ ❌     │
  │ ⑭ Modify Chunks  │ ✅     │ ❌     │ ❌     │ ❌     │ ❌     │ ⭐wind │
  └──────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘

  ORCHESTRATE (6):
  ┌──────────────────┬────────┬────────┬────────┬────────┬────────┬────────┐
  │ ⑮ Gate Attention │ ✅     │ ✅task │ ⚠️redir│ ❌     │ ⚠️narr │ ❌     │
  │ ⑯ Bias Activ.    │ ✅     │ ✅strg │ ⚠️redir│ ❌     │ ⚠️rig  │ ❌     │
  │ ⑰ Invoke SPM     │ ✅     │ ❌     │ ❌     │ ❌     │ ❌     │ ❌     │
  │ ⑱ Inhibit        │ ✅     │ ❌     │ ✅     │ ❌     │ ⭐MAX  │ ❌     │
  │ ⑲ Override Sat.  │ ✅     │ ❌     │ ❌     │ ❌     │ ⚠️chr  │ ❌     │
  │ ⑳ Change Environ │ ✅     │ ❌foc  │ ✅     │ ❌     │ ❌froz │ ❌     │
  └──────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘

  STRATEGIC (4):
  ┌────────────────────┬────────┬────────┬────────┬────────┬────────┬────────┐
  │ ㉑ Smooth Melody    │ ✅     │ ✅task │ ⚠️     │ ❌     │ ❌rig  │ ❌     │
  │ ㉒ Choose Goals     │ ✅     │ ❌one  │ ❌     │ ❌     │ ❌stck │ ❌     │
  │ ㉓ Accept Dissonan.│ ✅     │ ❌     │ ❌     │ ❌     │ ❌     │ ❌     │
  │ ㉔ Hijack Body-In. │ ✅     │ ✅task │ ❌     │ ❌     │ ❌     │ ❌     │
  └────────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘


  ⭐ CONFIGURATION PROFILES (approximate counts):

  ┌────────────────────┬─────────────────────────┬────────┬────────┬─────────┐
  │ Config             │ Description             │ Active │ Altered│ Enhanced│
  ├────────────────────┼─────────────────────────┼────────┼────────┼─────────┤
  │ ① Normal           │ All available           │  24    │   0    │   0     │
  │ ② Reallocation     │ Task-serving subset     │  ~14   │   0    │   0     │
  │ ③ Reconfiguration  │ Suggestion-guided       │  ~10   │  ~4    │   0     │
  │ ④ Disconnected     │ ALL PFC offline         │   0    │   0    │   0     │
  │ ⑤ Hyperactivated   │ 4 func. weaponized      │  ~3    │  ~8    │   1     │
  │ ⑥ Disintegration   │ Only ⑭ enhanced         │   0    │   0    │   1     │
  └────────────────────┴─────────────────────────┴────────┴────────┴─────────┘


  ⭐ KEY PATTERNS FROM SURVIVAL MATRIX:

  ① Config ② (flow):
    → Task functions SURVIVE (⑤⑥⑨⑪⑫⑯⑳㉑㉔)
    → Self-monitoring functions CUT (④⑰⑲㉒㉓)
    → ⑭ Modify OFF → flow CANNOT modify deep schemas (safe)
    → = "Deep performance WITHOUT structural change"

  ② Config ④ (threat):
    → ALL 24 functions OFFLINE → subcortical takeover
    → Most EXTREME config — zero PFC involvement
    → Recovery: fast (seconds, NE drops)

  ③ Config ⑤ (dissociation):
    → ⑱ Inhibit = ⭐ENHANCED → emotional suppression
    → ④⑧⑲ = ⚠️WEAPONIZED (chronic misuse)
    → ⑰ Self-Pattern-Modeling OFF → CANNOT model others → social disconnect
    → ㉑ Smooth Melody OFF → CANNOT reduce dissonance → stuck
    → = "Functions that should PROTECT become PRISON"

  ④ Config ⑥ (reconsolidation):
    → Nearly ZERO functions active
    → ⑭ Modify Chunks = ⭐ENHANCED — UNIQUE access
    → ⑪ Domain-Check OFF → no quality control → risk
    → = BOTH opportunity (modify) AND risk (no quality control)
    → = WHY therapist/guide REQUIRED: provides EXTERNAL quality control
      when INTERNAL quality control (⑪⑬⑱) all offline

  ⑤ ⑫ Label + ⑥ Quick Search = MOST RESILIENT:
    → Survive in 4-5/6 configs (lost only in ④ disconnect + ⑥ disintegrate)
    → = Basic language + basic search = deeply embedded functions
    → = WHY people can talk during dissociation, during meditation

  Source: Drill §3.18 ❸ (R2 survival matrix).
```

---

## §6 — Participation × Configuration: 2 Orthogonal Taxonomies

```
⭐⭐ 2 TAXONOMIES — ORTHOGONAL BUT CONSTRAINED:

  Drive.md §2 — PFC PARTICIPATION (quantitative):
    "How BUSY is PFC?" → 6 Drive-PFC modes: Absent → Monitor → Spinning →
    Resolve → Strategic → Override. = HOW MUCH PFC engages.

  PFC-Configuration.md §2 — PFC CONFIGURATION (qualitative):
    "How is PFC WIRED?" → Config ①-⑥: Normal → Reallocation →
    Reconfigured → Disconnected → Hyperactivated → Disintegrated.
    = WHAT KIND of PFC state.

  → 2 DIFFERENT, COMPLEMENTARY AXES:
    Participation = activation level (0-95%)
    Configuration = wiring pattern (which functions on/off/altered)


  COMPATIBILITY MATRIX — not all combinations possible:

  ┌─────────────────────┬────────┬────────┬────────┬────────┬────────┬────────┐
  │ Participation       │①Normal │②Reallo │③Reconf │④Discon │⑤Hyper  │⑥Disint │
  ├─────────────────────┼────────┼────────┼────────┼────────┼────────┼────────┤
  │ Drive-PFC-Absent    │ —      │ —      │ —      │ ✅     │ —      │ —      │
  │ Drive-PFC-Monitor   │ ✅     │ —      │ ⚠️rare │ —      │ —      │ —      │
  │ Drive-PFC-Spinning  │ ✅     │ —      │ —      │ —      │ ⚠️chr  │ —      │
  │ Drive-PFC-Resolve   │ ✅     │ ✅flow │ ✅trn  │ —      │ —      │ —      │
  │ Drive-PFC-Strategic │ ✅     │ —      │ ✅trn  │ —      │ —      │ —      │
  │ Drive-PFC-Override  │ ✅     │ —      │ —      │ —      │ ✅diss │ —      │
  └─────────────────────┴────────┴────────┴────────┴────────┴────────┴────────┘


  ⭐ NATURAL PAIRINGS:

  Drive-PFC-Absent + Config ④ (Disconnected):
    = Acute threat. PFC absent BECAUSE disconnected.
    → NE α1 flood → PFC offline → subcortical takeover.

  Drive-PFC-Spinning + Config ⑤ (Hyperactivated):
    = Anxious dissociation. PFC spinning + hyperactivated.
    → Try solutions → fail → try → fail → weaponized inhibit.
    → = WHY anxious dissociation feels "stuck AND numb."

  Drive-PFC-Resolve + Config ② (Reallocation):
    = Flow state. PFC resolving + reallocated to task.
    → Expertise + challenge → resolve cycle → reallocation amplifies.
    → = Csikszentmihalyi flow = this exact pairing.

  Drive-PFC-Override + Config ⑤ (Hyperactivated):
    = Clinical dissociation. Override + hyperactivated.
    → Body says stop → PFC overrides → chronic → damage.
    → = Lanius dissociative PTSD subtype.

  Config ⑥ (Disintegrated) = OUTSIDE participation spectrum:
    → All participation modes break down.
    → No coherent "Mode X" possible — hierarchy disintegrated.
    → = Psychedelic state is genuinely OUTSIDE normal PFC operation.


  ⭐ IMPOSSIBLE COMBINATIONS (follow from sub-region requirements):

  Drive-PFC-Absent + Config ⑤ (Hyperactivated):
    → Can't hyperactivate PFC AND have PFC absent.
    → Mutually exclusive by definition.

  Drive-PFC-Resolve + Config ④ (Disconnected):
    → Can't resolve problems with PFC disconnected.
    → dlPFC offline → ⑤ Hold lost → resolve impossible.

  Drive-PFC-Strategic + Config ⑥ (Disintegrated):
    → Can't be strategic when hierarchy disintegrated.
    → Meta-cognition requires coherent self-model → collapsed in ⑥.

  → Constraints = INFORMATIVE: impossible combos reveal which
    sub-regions each participation mode REQUIRES.


  REAL-WORLD MAPPING:

  ┌──────────────────────────┬──────────────────────────────────────────────┐
  │ Experience               │ Participation × Configuration                │
  ├──────────────────────────┼──────────────────────────────────────────────┤
  │ Normal daily life        │ Drive-PFC-Absent/Monitor + Config ①         │
  │ Problem-solving          │ Drive-PFC-Resolve + Config ①                │
  │ Flow state               │ Drive-PFC-Resolve + Config ②                │
  │ Meditation (focused)     │ Drive-PFC-Resolve/Strategic + Config ③      │
  │ Panic attack             │ Drive-PFC-Absent + Config ④                 │
  │ Anxious rumination       │ Drive-PFC-Spinning + Config ⑤ (partial)     │
  │ Dissociative episode     │ Drive-PFC-Override + Config ⑤               │
  │ Psychedelic session      │ N/A + Config ⑥                              │
  │ Strategic planning       │ Drive-PFC-Strategic + Config ①              │
  │ Override (deadline push) │ Drive-PFC-Override + Config ①               │
  └──────────────────────────┴──────────────────────────────────────────────┘

  Source: Drill §3.18 ❻ (R2 orthogonal taxonomies).
```

---

## §7 — Strategy A→B Transition (Defense Strategy Switch)

```
⭐⭐ 2 DEFENSE STRATEGIES = 2 PFC CONFIGURATIONS:

  Strategy A — Active (Fight/Flight):
    → Config ④ (Disconnected): PFC offline, amygdala rules, escape
    → NE α1 flood → subcortical takeover → compiled fight/flight
    → 500M+ years. DEFAULT. Most ancient defense.
    → Recovery: FAST (seconds, NE drops → PFC reconnects)

  Strategy B — Passive (Freeze/Dissociate):
    → Config ⑤ (Hyperactivated): PFC hyperactive, amygdala suppressed
    → 4 functions weaponized (⑱⑧⑲④) → disconnect pain
    → When A fails (inescapable). NEWER mechanism.
    → Recovery: SLOW (months-years, if at all)

  → A and B = DIFFERENT CONFIGURATIONS, not different intensities.
  → SAME neurochemical cocktail (high NE, high cortisol)
  → DIFFERENT PFC configuration selected by escape assessment.


  ⭐ A→B TRANSITION ≠ INTENSITY THRESHOLD:

  ❌ WRONG interpretation: "stronger threat → A escalates → B"
    → If intensity only: higher threat → A MORE intense
    → → amygdala stronger → Strategy A ESCALATES, not switches

  ✅ Correct: A→B = ESCAPE POSSIBILITY ASSESSMENT
    → Can I fight or flee? → YES → Strategy A (config ④)
    → Can I fight or flee? → NO → Strategy B (config ⑤)
    → = Qualitatively DIFFERENT variable, not intensity gradient


  3 VARIABLES DETERMINING A→B TRANSITION:

  ┌─────────────────────────┬───────────────────────────────────────┐
  │ Variable                │ Effect                                │
  ├─────────────────────────┼───────────────────────────────────────┤
  │ ① ESCAPE POSSIBILITY    │ CORE variable.                        │
  │   (body-level assess.)  │ CAN escape → A. CANNOT → B.          │
  │                         │ NOT a conscious PFC decision.         │
  │                         │ Subcortical: ~100-500ms.              │
  ├─────────────────────────┼───────────────────────────────────────┤
  │ ② COMPILED A HISTORY    │ Past A success → A fires DEFAULT.     │
  │   (schema × outcomes)   │ Past A failed once → B for similar.   │
  │                         │ Past A failed repeatedly → B DEFAULT  │
  │                         │ for ANY threat (generalized).         │
  ├─────────────────────────┼───────────────────────────────────────┤
  │ ③ AGE AT FIRST TRAUMA   │ 0-3: A PHYSICALLY impossible → B     │
  │   (developmental)       │   compiled as FOUNDATION (primary).   │
  │                         │ 3-7: A attempted, fails → B secondary.│
  │                         │ Adult: A possible → B = backup only.  │
  └─────────────────────────┴───────────────────────────────────────┘

  KEY CASES:
    → Child hit LIGHTLY but CHRONICALLY → dissociates (B)
      (cannot escape parent — escape possibility = NO)
    → Adult robbed at gunpoint → fight/flight (A)
      (CAN potentially escape — escape possibility = YES)
    → = Threat INTENSITY ≠ predictor. ESCAPE POSSIBILITY = predictor.


  ⭐ ATTACHMENT PARADOX — CAREGIVER TRAUMA = MAXIMUM DISSOCIATION:

  Normal threat: source ≠ attachment figure
    → Strategy A: fight/flee FROM threat → TOWARD attachment → safe
    → = Designed pathway. Works for ALL external threats.

  Caregiver threat: source = attachment figure
    → TRIPLE IMPOSSIBILITY:
      ❶ CANNOT fight/flee FROM caregiver (would lose ONLY safe base)
      ❷ CANNOT fight/flee TOWARD caregiver (they ARE the threat)
      ❸ B must be PARTIAL (must maintain approaching = survival)

  Body's "impossible solution":
    → Dissociate pain → maintain approaching → survive
    → = "Holding the one causing pain without feeling the pain"
    → = Functional but COSTLY: emotional processing SHUT DOWN

  What COMPILES:
    → "Relationship = pain disconnected from awareness"
    → Adult pattern: maintain relationships but CANNOT feel fully
    → = Body-Coupling.md: entanglement with negative coupling

  🟢 Main & Hesse 1990 — disorganized attachment:
    → Infant: approach + freeze + look away SIMULTANEOUSLY
    → = Body expressing BOTH "seek attachment" AND "dissociate threat"
    → = Observable evidence of triple impossibility mechanism


  4 HARDWARE FACTORS AFFECTING A/B TENDENCY:

  ┌─────────────────────────┬────────────────────────────────────────┐
  │ Factor                  │ Effect                                 │
  ├─────────────────────────┼────────────────────────────────────────┤
  │ ① HPA axis sensitivity  │ More reactive → overwhelmed sooner    │
  │   (genetic)             │ → B threshold LOWER.                  │
  │                         │ 🟢 Yehuda 2016                        │
  ├─────────────────────────┼────────────────────────────────────────┤
  │ ② PFC-amygdala          │ Stronger inhibitory pathway → easier  │
  │   connectivity          │ to suppress amygdala → B more access. │
  │                         │ 🟡 Consistent with connectivity lit.  │
  ├─────────────────────────┼────────────────────────────────────────┤
  │ ③ Vagal tone            │ High vagal → FREEZE accessible        │
  │                         │ (parasympathetic override of          │
  │                         │ sympathetic).                         │
  │                         │ 🟢🟡 Porges polyvagal (core verified) │
  ├─────────────────────────┼────────────────────────────────────────┤
  │ ④ Epigenetic            │ Parental trauma → offspring HPA       │
  │   calibration           │ pre-calibrated → B threshold lower.   │
  │                         │ 🟢 Yehuda 2016 transgenerational      │
  └─────────────────────────┴────────────────────────────────────────┘

  → "Weakness" = CALIBRATION for ancestors' environment.
  → Mismatch when offspring environment actually safe → B fires unnecessarily.


  ⭐ B→A REVERSION: POSSIBLE BUT NEVER COMPLETE:

  3 pathways for B→A expansion:

  ① Safe environment (months-years):
    → Body learns "A is possible" → competitive re-linking
    → New "A → safe outcome" chunks compile alongside "A → futile"

  ② Somatic therapy (body-oriented):
    → Body RE-LEARNS physical capacity: "I CAN push, I CAN run"
    → Deliberately activate A pathway in SAFE context
    → Direct-State reward (touch, movement) as "backdoor"
    → 🟢 Van der Kolk 2014: body-oriented therapy effective

  ③ Gradual exposure (progressive):
    → Small threats where A SUCCEEDS → compile "A works"
    → Goldilocks: threat small enough that A handles it

  CONSTRAINT:
    → Complete reversal UNLIKELY for early childhood B foundation
    → B compiled FIRST → deepest chunks → persists underneath
    → FUNCTIONAL reversal: A becomes ACCESSIBLE, B remains as backup
    → = "I CAN fight now, but extreme stress → still dissociate"
    → = Not "cure" but expanded repertoire (A+B, not just B)

  Source: Drill §3.17 (R16 Strategy A→B Transition).
  🟢 Lanius 2010, Main & Hesse 1990, Van der Kolk 2014, Yehuda 2016
```

---

## §8 — System Reconsolidation (Config ⑥ × Function ⑭)

```
⭐⭐ SYSTEM RECONSOLIDATION = EMERGENT from individual reconsolidation:

  Individual reconsolidation (🟢 Nader et al. 2000):
    → Recall 1 chunk → labile state → modify → re-compile
    → = Per-chunk mechanism: 1 chunk at a time
    → CONSTRAINT: top-down priors STILL ACTIVE
    → Surrounding hierarchy PULLS modified chunk BACK → change LIMITED
    → Analogy: rearrange 1 piece of furniture — room unchanged

  System reconsolidation (config ⑥):
    → MANY chunks simultaneously labile (DMN disintegrated)
    → Top-down hierarchy temporarily FLAT
    → RELATIONSHIP STRUCTURE between chunks becomes modifiable
    → = Not just individual mountains reshapable — TOPOLOGY can shift
    → Analogy: earthquake → entire landscape can resettle


  ⭐ WHY "SYSTEM" ≠ "MANY INDIVIDUAL":

  Phase transition, not just "many things at once":
    → Individual: modify 1 chunk → hierarchy pulls back → revert
    → System: hierarchy ITSELF flat → new configuration CAN STABILIZE
    → = Water → steam ≠ "many hot molecules"
    → = Qualitative state change when enough elements simultaneously labile

  ┌──────────────────────────┬──────────────────┬──────────────────────┐
  │ Mechanism                │ Scope            │ Lasting Change?      │
  ├──────────────────────────┼──────────────────┼──────────────────────┤
  │ Individual reconsolid.   │ 1 chunk per      │ LIMITED (hierarchy   │
  │ (🟢 Nader 2000)          │ retrieval        │ pulls back)          │
  ├──────────────────────────┼──────────────────┼──────────────────────┤
  │ Competitive re-linking   │ Per-chunk (build │ MODERATE (months-    │
  │ (therapy standard)       │ alongside)       │ years, gradual)      │
  ├──────────────────────────┼──────────────────┼──────────────────────┤
  │ System reconsolidation   │ HIERARCHY-WIDE   │ HIGH (topology       │
  │ (psychedelic)            │ (topology change)│ shift, new default)  │
  ├──────────────────────────┼──────────────────┼──────────────────────┤
  │ Trauma compilation       │ HIERARCHY-WIDE   │ HIGH but NEGATIVE    │
  │ (violent flip)           │ (but negative)   │ direction            │
  └──────────────────────────┴──────────────────┴──────────────────────┘


  ⭐ 3-STEP MECHANISM:

  Step 1 — DESTABILIZE (session onset):
    → 5-HT2A agonism → DMN network disintegration
    → Top-down priors lose constraint power
    → Chunks labile, chunk-to-chunk relationships modifiable
    → = "Ground becomes soft"

  Step 2 — REORGANIZE (during session, hours):
    → Body receives unprecedented signal combinations
    → Body-Feedback-Mechanism 3 dynamics SIMULTANEOUSLY + UNCOORDINATED:
      Chunk-Shift: valence re-evaluate EN MASSE
      Chunk-Miss: baseline patterns fire DIFFERENTLY → miss signals
      Chunk-Gap: ACC detects EVERYWHERE (all patterns disrupted)
    → Under safe context: new chunk-to-chunk links compile
    → Guide/therapist provides framework for reorganization
    → = "Landscaping while the ground is soft"

  Step 3 — CONSOLIDATE (post-session, days-weeks):
    → Sleep: new configuration consolidates (🟢 Walker 2017)
    → Integration therapy: PFC processes new configuration
    → New hierarchy stabilizes → becomes NEW default
    → WITHOUT proper consolidation → revert OR chaotic patterns
    → = WHY integration sessions CRITICAL for lasting change


  ⭐ MIRROR MECHANISM — System Reconsolidation ↔ Trauma Compilation:

  SAME mechanism, DIFFERENT direction:

  ┌──────────────────────────┬──────────────────────────────────────┐
  │ Trauma Compilation       │ System Reconsolidation (therapeutic) │
  ├──────────────────────────┼──────────────────────────────────────┤
  │ Single extreme event     │ Psychedelic session                  │
  │ Emotional peak           │ Emotional intensity                  │
  │ → Deep compilation       │ → Deep compilation                  │
  │ UNSAFE context           │ SAFE context                        │
  │ → Cortisol tag           │ → Opioid tag                        │
  │ → AVOIDANCE direction    │ → APPROACH direction                │
  │ Lasting NEGATIVE change  │ Lasting POSITIVE change             │
  │ Hierarchy → around threat│ Hierarchy → toward flexibility      │
  └──────────────────────────┴──────────────────────────────────────┘

  → SAME POWER: single event → lasting structural change
  → DIFFERENT DIRECTION: set & setting determines
  → Set & setting = "ensuring compilation direction = APPROACH
    during hierarchy-flat window"
  → = WHY set & setting is not optional — it IS the mechanism


  ⭐ 4 CONDITIONS FOR POSITIVE OUTCOME:

  ┌──────────────────────┬───────────────────────┬──────────────────────┐
  │ Condition            │ Met → IMPROVEMENT     │ Not met → RISK       │
  ├──────────────────────┼───────────────────────┼──────────────────────┤
  │ ① Sufficient         │ Hierarchy flat enough │ Too little: surface  │
  │   destabilization    │ for structural change │ Too much: overwhelm  │
  ├──────────────────────┼───────────────────────┼──────────────────────┤
  │ ② Safe context       │ Compilation direction │ Unsafe: avoidance    │
  │   (set & setting)    │ = APPROACH → positive │ tag → re-traumatize  │
  ├──────────────────────┼───────────────────────┼──────────────────────┤
  │ ③ Guided recompil.   │ Therapist provides    │ No guide: chaotic    │
  │                      │ external quality      │ reorganization →     │
  │                      │ control (replaces     │ unstable config      │
  │                      │ ⑪ Domain-Check, off   │                      │
  │                      │ in config ⑥)          │                      │
  ├──────────────────────┼───────────────────────┼──────────────────────┤
  │ ④ Post-session       │ Sleep + integration   │ No integration:      │
  │   consolidation      │ → new config stable   │ patterns don't hold  │
  └──────────────────────┴───────────────────────┴──────────────────────┘

  GOLDILOCKS PRINCIPLE (Body-Feedback-Precondition Precondition-4 Match-Range):
    Too little destabilization → no structural change
    Too much → overwhelming → body defense
    Just right → structural change → lasting improvement
    = WHY dosing matters, WHY set & setting matters


  ⭐ R15↔R16 BRIDGE — System Reconsolidation × B Default:

  Problem: Childhood B default (§7) = compiled DEEP → resistant to
    normal therapy (competitive re-linking = months-years, partial).

  System reconsolidation addresses this:
    → During config ⑥: hierarchy FLAT → B FOUNDATION accessible
    → Under safe context: A pathways can compile AT FOUNDATION LEVEL
    → = Not building A on top of B — modifying B FOUNDATION itself
    → = WHY psychedelic-assisted therapy shows promise for
      treatment-resistant PTSD (B default too deep for standard therapy)

  CAUTION:
    → B foundation = SURVIVAL strategy → removing without replacement = DANGEROUS
    → MUST provide safe context + guided A recompilation DURING destabilization
    → Condition ② = ESPECIALLY critical for trauma population
    → System reconsolidation without safety → re-traumatization risk HIGH

  Source: Drill §3.16 (R15 System Reconsolidation).
  🟢 Nader et al. 2000, Carhart-Harris 2012/2019, Griffiths 2006, Walker 2017
  🟡 Mirror mechanism (same power, opposite direction) = framework
  🟡 Config ⑥ × ⑭ as mechanism explanation = framework
```

---

## §9 — Honest Assessment

```
🟢 ESTABLISHED (research-supported):

  Flow deactivation:
    Limb & Braun 2008 — dlPFC selective deactivation during jazz improvisation
    Csikszentmihalyi 1990 — flow state characteristics (loss of self-consciousness)
    Dietrich 2004 — transient hypofrontality during flow

  Dissociation hyperactivation:
    Lanius et al. 2010 — 2 PTSD subtypes (re-experiencing vs dissociative)
    Sierra & Berrios 1998 — depersonalization phenomenology
    Van der Kolk 2014 — body-oriented therapy for trauma

  Psychedelic / Reconsolidation:
    Carhart-Harris & Friston 2019 — REBUS model (relaxed priors)
    Carhart-Harris et al. 2012 — DMN disintegration under psilocybin
    Griffiths et al. 2006 — single session → lasting personality change
    Nader et al. 2000 — reconsolidation mechanism (per-chunk)
    Walker 2017 — sleep-dependent memory consolidation

  Threat / PFC disconnect:
    Arnsten 2009, 2015 — NE α2/α1 dual effect on PFC
    LeDoux 1996 — amygdala low road (~12ms)
    Mobbs et al. 2007 — threat gradient PFC→PAG
    Yehuda 2016 — transgenerational HPA calibration

  Attachment:
    Main & Hesse 1990 — disorganized attachment
    Porges — polyvagal theory (core mechanisms verified)

  Sub-region functions:
    Goldman-Rakic 1995 (dlPFC WM), Damasio 1994 (vmPFC somatic markers),
    Botvinick 2004 (ACC conflict), Fleming 2012 (mPFC metacognition),
    Aron 2004 (vlPFC inhibition), Saxe 2006 (mPFC/TPJ ToM),
    Padoa-Schioppa 2011 (OFC value), McAlonan 2008 (TRN gating)


🟡 FRAMEWORK SYNTHESIS (consistent but novel organization):

  6 configuration modes taxonomy:
    → Novel organization. Components established individually.
    → Brain may have MORE continuous space (6 discrete modes = simplification).
    → But 6 modes capture the QUALITATIVELY DIFFERENT states well.

  24 × 6 sub-region mapping:
    → Inference from lesion + imaging + connectivity, not direct measurement.
    → Primary/secondary assignments = best current evidence, not definitive.
    → dlPFC 15/24 hub finding = robust (follows from dlPFC's known centrality).

  Survival matrix (24 functions × 6 configs):
    → Large-scale inference: which functions survive in which state.
    → Individual cells = varying confidence (some 🟢, many 🟡).
    → PATTERN is informative even if individual cells uncertain.

  2 orthogonal taxonomies (participation × configuration):
    → Novel distinction. Supported by different brain mechanisms.
    → Impossible combinations = logical constraints, not empirical tests.

  Mirror mechanism (trauma ↔ reconsolidation):
    → "Same mechanism, different direction" = framework insight.
    → Both = emotional peak + deep compilation. Direction = context.
    → Consistent with research, not directly tested as unified concept.

  4 functions weaponized (config ⑤):
    → Novel taxonomy for dissociation at function level.
    → Consistent with Lanius 2010 hyperactivation finding.
    → Specific function assignments = framework contribution.

  §2.1 Clinical illustrations (v1.1 — Health Conditions Drill):
    → PTSD ④↔⑤ oscillation validates 2 distinct defense modes
    → ADHD DMN interference validates Config ① instability
    → Parkinson masked face validates config≠execution distinction


🔴 TESTABLE PREDICTIONS:

  P-R2a: Flow (config ②) should show dlPFC SPLIT —
    task-serving active, self-monitoring inactive —
    NOT uniform dlPFC change.
    → Testable: high-resolution fMRI during flow + sub-region analysis

  P-R2b: Dissociation (config ⑤) should show
    vlPFC + ACC hyperactivated while most other sub-regions reduced.
    → Testable: sub-region analysis dissociative vs re-experiencing PTSD

  P-R2c: Psychedelic (config ⑥) should show ⑭ Modify Chunks ENHANCED
    while ⑤ Hold + ⑱ Inhibit + ⑪ Domain-Check impaired.
    → Testable: reconsolidation + WM + inhibition tasks during psilocybin

  P-R2d: dlPFC overload should predict WM failure at LOWER loads when
    multiple competing functions demanded simultaneously.
    → Testable: dual-task paradigm (WM + inhibition + social modeling)

  P-R16a: A→B transition correlates with ESCAPE POSSIBILITY,
    not threat INTENSITY.
    → 🟢 Partially supported: Lanius 2010

  P-R16b: Childhood trauma (< 3 years) → higher dissociative response ratio.
    → 🟢 Partially supported: Lanius 2010, Van der Kolk research

  P-R15a: System reconsolidation effect ∝ degree of DMN disruption.
    → Testable: fMRI DMN change × lasting personality change

  P-R15b: Lasting change REQUIRES post-session consolidation (sleep quality).
    → Testable: sleep quality post-session × outcome at 6 months
```

---

## §10 — Cross-References

```
PFC FOLDER (companion files):
  PFC-Function.md v1.1 — 24 functions (WHAT PFC does)
    → This file EXTENDS with dynamic configurations
  PFC-Hardware.md v1.0 — Hardware parameters (COMT, DRD4, NE)
    → Hardware affects which configs accessible + quality per-config
  PFC-Development.md — Life stages, training
    → Development affects config repertoire
  PFC-Hold-Dimensions.md — Why ~4±1
    → dlPFC hub + 15/24 functions → capacity explained

PHYSICAL MAP:
  Neural-Architecture.md §2 — 6 PFC sub-regions physical anatomy
    → §4 mapping verified against this reference

DRIVE INTEGRATION:
  Drive.md v1.2 §2 — 6 Drive-PFC participation modes (orthogonal taxonomy)
    → §6 compatibility matrix links both taxonomies

REWARD:
  Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State × config interaction
    → §3 control spectrum × reward types
  03-Reward.md — Body-Feedback-Precondition preconditions, 7-step VTA
    → Config affects WHICH preconditions can be met

BODY SYSTEMS:
  Body-Feedback-Mechanism.md v1.1 — 3 chunk dynamics
    → System reconsolidation = 3 dynamics uncoordinated (§8)
  Cortisol-Baseline.md v2.0 — Cortisol triggers config ④
    → Chronic cortisol → dlPFC damage → 15/24 impaired
  Body-Coupling.md v1.0 — Entanglement, caregiver paradox
    → §7 attachment paradox → body-coupling mechanism

FEELING:
  Feeling.md v2.0 — Feeling = PFC observation of body-feedback
    → Config determines WHAT PFC can observe
  Feeling-Mechanism-Deep.md — §4 reward mechanism
    → Config affects reward observation fidelity

THREAT:
  Threat.md — Threat strategies × PFC configurations
    → §7 Strategy A (config ④) vs Strategy B (config ⑤)

COMPILATION:
  Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators
    → Trauma compilation = config ⑤ foundation (§7 age variable)
  Chunk.md v2.0 — Chunk substrate PFC operates on
    → Reconsolidation = chunk modification (⑭) mechanism

CORE:
  Core-v7.8-Draft.md — PFC position in cycle architecture
    → 6 configs = PFC's dynamic range within cycle

DRILL SOURCE:
  Drill-Reward-Feeling-Main.md v1.2 — Full drill source
    §3.18 (R2), §5b (R11+R12), §3.16 (R15), §3.17 (R16)

HEALTH CONDITIONS DRILL (v1.1):
  PTSD-Analysis.md v1.0 §4.4 — ④↔⑤ oscillation (→ §2.1)
  ADHD-Observation.md v1.2 §8 — DMN interference, Config ① unstable (→ §2.1)
  Parkinson-Analysis.md v1.1 §5.4 — masked face, config≠execution (→ §2.1)
```

---

> **PFC-Configuration.md v1.1**
>
> 6 Configuration Modes: Normal → Reallocation → Reconfigured →
>   Disconnected → Hyperactivated → Disintegrated.
> v1.1: §2.1 PTSD ④↔⑤ oscillation + ADHD DMN interference + Parkinson gate.
> PFC Control Spectrum: Overcontrol (⑤) ↔ Balanced (①②③) ↔ Undercontrol (⑥).
> 24 Functions × 6 Sub-Regions: dlPFC hub (15/24), vlPFC specialist (3/24 high-impact).
> Survival Matrix: which functions survive in which configuration.
> Participation × Configuration: 2 orthogonal taxonomies, constrained pairings.
> Strategy A→B: escape possibility (not intensity), caregiver triple impossibility.
> System Reconsolidation: config ⑥ × function ⑭, mirror of trauma, 4 conditions.
>
> ✅ English primary throughout
>
> Version: v1.1, 2026-05-10.
