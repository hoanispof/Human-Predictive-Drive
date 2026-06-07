---
title: Compile-Sleep — Sleep Maintenance (Offline System)
version: 1.0
created: 2026-06-01
source_version: Vietnamese v1.0
english_created: 2026-06-06
status: v1.0
scope: |
  Sleep = Sleep Maintenance in Compile Architecture.
  6 mechanisms: ~1.5 exposure-based, ~4.5 optimization-based.
  Sleep ≠ "simply an exposure source." Sleep = OFFLINE MAINTENANCE SYSTEM.
  Classifying each mechanism: IS exposure / NOT exposure / PARTIAL.
  Sleep × Architecture interaction (Compile Engine, Entity-Valence Bias, Exposure Channels, PFC Modulation).
  Sleep deprivation = architecture degradation (PFC degrades FIRST).
  Waking rest = complement (~30%), NOT replacement.
  ~40 research citations, 6+1 mechanisms.
purpose: |
  Chunk.md v3.0 §2.1 ④ "Sleep consolidation" = 3-line summary (Walker 2017).
  This file = DETAIL: 6 mechanisms, exposure classification, architecture interaction.
  Learning-Cycle.md §4 has formalized 6+1 mechanisms individually.
  This file ADDS: exposure vs optimization classification + position in Compile Architecture.
parent: Chunk.md v3.0 (§2.1 ④ sleep consolidation = summary → this file = detail)
related: |
  Compile-Taxonomy.md v3.0 — 3 Compile Types (Sleep Maintenance = offline maintenance)
  Learning-Cycle.md §4 — 6+1 sleep mechanisms (primary research source)
  PFC-Operations.md v1.3 §8.3 — PFC budget recharges via sleep
  Cortisol-Baseline.md v2.2 — Sleep = PRIMARY cortisol recovery
  Background-Pattern.md v2.0 §3 — Gist Extraction → Background-Pattern formation
  Body-Base.md v3.3 §2 — Compilable Architecture (+ Sleep Maintenance)
  Reward-Signal-Architecture.md v2.1 — Evaluative vs Direct-State vulnerability
dependencies:
  - Chunk.md v3.0 — §2.1 ④ sleep, §2.2 compile_rate formula
  - Compile-Taxonomy.md v3.0 — 3 Compile Types + architecture context
  - PFC-Operations.md v1.3 — Hold/Suppress, PFC budget
  - Entity-Valence-Dynamics.md v1.1 — Structural/Current valence
  - Body-Base.md v3.3 — Compilable Architecture
  - Cortisol-Baseline.md v2.2 — Cortisol × sleep interaction
  - Background-Pattern.md v2.0 — Gist extraction → Background-Pattern
  - Simulation-Engine.md v1.1 — PFC offline during sleep
  - Reward-Signal-Architecture.md v2.1 — Reward vulnerability under deprivation
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
sources: |
  Learning-Cycle.md §4 (6+1 mechanisms) — secondary research source
---

# Compile-Sleep — Sleep Maintenance (Offline System)

> **Sleep is NOT simply the 4th "exposure source."**
>
> Sleep has 6 mechanisms — only ~1.5 exposure-based, ~4.5 optimization.
> Most of sleep = OPTIMIZATION on EXISTING compiled chunks.
>
> Compile Engine (Hebbian) = BUILDS the house (while awake).
> Sleep = MAINTAINS the house (while sleeping):
>   Clears debris (SHY). Moves temporary to permanent storage (Active Consolidation).
>   Repaints (Emotional Decoupling). Condenses the blueprint (Gist Extraction).
>   Connects new rooms to old (Creative Linking). Tests the system (Replay).
>
> MAINTENANCE ≠ NEW CONSTRUCTION. But WITHOUT maintenance → the house FALLS APART.

---

## Table of Contents

- §0 — Position in Framework
- §1 — Core Thesis: Sleep ≠ Exposure Source
- §2 — Sleep Stages: SWS vs REM
- §3 — 6 Mechanisms: Exposure vs Optimization
- §4 — Sleep × Compile Architecture
- §5 — Sleep Deprivation = Architecture Degradation
- §6 — Waking Rest: Complement, Not Replacement
- §7 — Honest Assessment
- §8 — Open Questions
- §9 — Cross-References

---

## §0 — Position in Framework

```
⭐ THIS FILE EXPANDS CHUNK.MD §2.1 ④ "SLEEP CONSOLIDATION":

  Chunk.md §2.1 ④: 3 lines — "Hippocampus REPLAY → strengthen or prune.
  Sleep consolidation (Walker 2017). Clearer next morning = unconscious HAS ALREADY processed."

  Those 3 lines = summary. This file = detail:
    6 distinct mechanisms (not just "replay")
    Exposure vs optimization classification
    Sleep Maintenance's position in Compile Architecture
    Interaction with Compile Engine, Entity-Valence Bias, Exposure Channels, PFC Modulation
    Sleep deprivation = architecture degradation model


  POSITION IN COMPILE ARCHITECTURE:

    Compile Architecture (Compile-Taxonomy.md):
      Compile Engine (Hebbian) + Entity-Valence Bias + Exposure Channels (External+Deliberate+Spontaneous)
      + PFC Modulation → compile chunks while AWAKE.

    Sleep Maintenance (this file):
      Sleep = OFFLINE MAINTENANCE SYSTEM.
      Interacts with Compile Engine, Entity-Valence Bias, Exposure Channels,
      PFC Modulation but INDEPENDENTLY — runs when waking is off.


  FILE HIERARCHY:

    Chunk.md §2.1 ④ (3-line summary)
      → [this file] (detail: 6 mechanisms + architecture interaction)
      → Learning-Cycle.md §4 (primary research source for 6+1 mechanisms)

    Body-Base.md §2 (Compilable Architecture)
      → [this file] (Sleep Maintenance = offline maintenance)

    Read Chunk.md §2 first → read this file → read Compile-Taxonomy.md.


  READING GUIDE:

    §1-§2: thesis + sleep stages — background
    §3: 6 mechanisms — MAIN CONTENT (exposure vs optimization classification)
    §4: architecture interaction — interaction with compile system while awake
    §5-§6: deprivation + waking rest — consequences + alternatives
    §7-§9: assessment + questions + references
```

---

## §1 — Core Thesis: Sleep ≠ Exposure Source

```
⭐⭐ CORE THESIS:

  Sleep is NOT simply the 4th "exposure source."

  If sleep = only an exposure source:
    → Sleep = additional Spontaneous (automatic internal exposure)
    → Sole value = "repeating patterns"
    → Sleep deprivation = merely "less repetition"

  REALITY: sleep has 6 mechanisms — only ~1.5 exposure-based:
    → Sleep PRUNES     (SHY — cuts weak connections)
    → Sleep REPLAYS    (Hippocampal Replay — compressed re-firing)
    → Sleep TRANSFERS  (Active Consolidation — hippocampus → cortex)
    → Sleep LINKS      (Creative Linking — creates remote associations)
    → Sleep DECOUPLES  (Emotional Decoupling — strips emotional tag)
    → Sleep ABSTRACTS  (Gist Extraction — generalizes)

  Most = OPTIMIZATION on EXISTING compiled chunks.
  NOT "adding new exposure."


  POSITION IN ARCHITECTURE — SLEEP MAINTENANCE:

    ┌─────────────────────────────────────────┐
    │  WAKING                                  │
    │                                         │
    │  Compile Engine ← Exposure              │
    │                   (External+Deliberate  │
    │                    +Spontaneous)        │
    │               ← Entity-Valence Bias    │
    │               ← PFC Modulation         │
    │               → Compiled Chunks        │
    └─────────────────┬───────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────┐
    │  SLEEP — Sleep Maintenance              │
    │                                         │
    │  Compiled Chunks → 6 mechanisms:        │
    │    ① SHY (prune)                        │
    │    ② Replay (re-expose)                 │
    │    ③ Active Consolidation (transfer)    │
    │    ④ Creative Linking (new links)       │
    │    ⑤ Emotional Decoupling (strip tag)   │
    │    ⑥ Gist Extraction (abstract)         │
    │  → Optimized Chunks                     │
    └─────────────────┬───────────────────────┘
                      │
                      ▼
    ┌─────────────────────────────────────────┐
    │  NEXT WAKING                            │
    │                                         │
    │  Optimized Chunks = starting material   │
    │  for Compile Engine to continue         │
    │  compiling                              │
    │  PFC catecholamine RESTORED             │
    │  Cortisol effects PARTIALLY cleared     │
    └─────────────────────────────────────────┘

  = CYCLE: Waking (build) → Sleep (maintain) → Waking (build on maintained)
  = Learning-Cycle.md H8: "Learning is a cycle, not an event."


  WHY THIS DISTINCTION MATTERS:

    "Sleep = exposure source" → sleep deprivation = "less repetition"
    "Sleep = maintenance system" → sleep deprivation = "NO pruning, NO transfer,
      NO decoupling, NO abstraction, NO linking + less replay"
    → DIFFERENT consequences. Different model → different prediction → different intervention.

    Sleep deprivation IN REALITY: PFC degrades + emotional reactivity + memory fragile
    + creativity down + noise accumulates = CONSISTENT with 6-mechanism model.
    NOT consistent with "just less repetition."


  🟡 Sleep as Sleep Maintenance in compile architecture: framework synthesis
  🟢 Multi-mechanism sleep model: Diekelmann & Born 2010
  🟢 Sleep ≠ single function: established sleep neuroscience
```

---

## §2 — Sleep Stages: SWS vs REM

```
🟢 2 PRIMARY SLEEP TYPES — DIFFERENT NEUROCHEMISTRY, DIFFERENT FUNCTION:


  NREM (Non-REM), especially SWS (Slow Wave Sleep, stage N3):
    EEG: slow oscillations (< 1 Hz) + spindles (~12-16 Hz) + sharp-wave ripples
    Chemistry: low acetylcholine, low norepinephrine
    Dominant in FIRST HALF of night
    Functions: SHY, Replay, Active Consolidation, Gist Extraction

  REM (Rapid Eye Movement):
    EEG: desynchronized (similar to waking)
    Chemistry: HIGH acetylcholine, LOW norepinephrine, theta rhythms
    Muscles: paralyzed (atonia)
    Dominant in SECOND HALF of night
    Functions: Creative Linking, Emotional Decoupling


  Cycle: ~4-6 NREM/REM cycles per night, each cycle ~90 minutes.


  WHY 2 STAGES EXIST:

    If sleep had only 1 function → 1 stage would suffice.
    2 stages = 2 SETS of distinct mechanisms:
      SWS = strengthen + transfer + prune (declarative memory dominant)
      REM = creative link + emotional calibrate (procedural + emotional dominant)

    Stage-specific disruption → SPECIFIC deficits:
      SWS disruption → memory impairment
      REM disruption → emotional dysregulation
    = 2 independent maintenance systems sharing sleep time.


  ┌────────────┬────────────────────┬──────────────────────┐
  │ Stage      │ SWS (NREM deep)    │ REM                  │
  ├────────────┼────────────────────┼──────────────────────┤
  │ When       │ First half of      │ Second half of       │
  │            │ night              │ night                │
  │ EEG        │ Slow oscillations  │ Desynchronized       │
  │ NE         │ Low                │ Very low             │
  │ ACh        │ Low                │ High                 │
  │ Muscles    │ Relaxed            │ Paralyzed            │
  │ Dreams     │ Rare, abstract     │ Vivid, narrative     │
  │ Mechanisms │ SHY, Replay,       │ Creative Linking,    │
  │            │ Consolidation,     │ Emotional            │
  │            │ Gist Extraction    │ Decoupling           │
  │ Primary    │ Declarative memory │ Emotional + creative │
  └────────────┴────────────────────┴──────────────────────┘


  🟢 Sleep architecture: Walker 2017, Diekelmann & Born 2010
  🟢 SWS dominant early, REM dominant late: established polysomnography
  🟢 Stage-specific deficits: Gais et al. 2000, Wagner et al. 2001
```

---

## §3 — 6 Mechanisms: Exposure vs Optimization

```
⭐ CLASSIFYING EACH MECHANISM — EXPOSURE OR OPTIMIZATION:

  ┌────┬─────────────────────┬─────────────┬──────────────────────────┐
  │ #  │ Mechanism           │ Exposure?   │ Primary function         │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  1 │ SHY Homeostasis     │ ❌ NOT      │ Prune weak, preserve     │
  │    │                     │             │ strong (signal/noise)    │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  2 │ Hippocampal Replay  │ ✅ YES      │ Re-fire sequences        │
  │    │                     │ (internal)  │ (internal exposure)      │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  3 │ Active Consolidation│ ❌ NOT      │ Transfer hippocampus     │
  │    │                     │             │ → cortex (relocate)      │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  4 │ REM Creative Linking│ 🟡 PARTIAL  │ New remote associations  │
  │    │                     │ (new links) │ (cross-domain connect)   │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  5 │ Emotional Decoupling│ ❌ NOT      │ Strip emotional charge   │
  │    │                     │             │ (preserve content)       │
  ├────┼─────────────────────┼─────────────┼──────────────────────────┤
  │  6 │ Gist Extraction     │ 🟡 PARTIAL  │ Abstract pattern from    │
  │    │                     │ (abstract)  │ specific (generalize)    │
  └────┴─────────────────────┴─────────────┴──────────────────────────┘

  EXPOSURE COUNT: 1 full (Replay) + 2 partial (Creative Linking, Gist) = ~1.5 exposure-based.
  OPTIMIZATION: 3 full (SHY, Consolidation, Decoupling) + 2 partial (Creative Linking, Gist) = ~4.5 optimization.
  → MAJORITY of sleep = OPTIMIZATION, not exposure.

  "~1.5 / ~4.5" = estimates because Creative Linking and Gist Extraction are PARTIAL —
  the boundary of exposure/optimization is not binary. Core point: the majority of sleep
  does NOT create new exposure but OPTIMIZES existing compile.

  🟡 Exposure vs optimization classification: framework synthesis
  🟢 6 mechanisms individually: established (citations per section below)
```

### §3.1 — Synaptic Homeostasis Hypothesis (SHY) — NOT exposure

```
🟢 SHY = GLOBAL SYNAPTIC DOWNSCALING:

  Research: Tononi & Cirelli 2003, 2014 "Sleep and the price of plasticity"

  MECHANISM:
    While awake: synapses NET-POTENTIATE (Hebbian → Compile Engine increases connections)
    → Metabolically UNSUSTAINABLE — if only increasing → brain saturates
    → Sleep (SWS): ALL synapses weaken PROPORTIONALLY
    → Result: total network strength → baseline, RELATIVE strengths PRESERVED

  CONSEQUENCE:
    Synapses that fire FREQUENTLY → still RELATIVELY strong → PRESERVED
    Synapses that fire RARELY → relatively weaker → may fall below threshold → PRUNED
    = "Pruning is not deletion — it's competitive preservation"

  EVIDENCE:
    Slow oscillation amplitude decreases across night (progressive downscaling)
    GluA1 AMPA receptors decrease after sleep (molecular evidence)
    Dendritic spine turnover: waking ADD, sleep PRUNE (Maret 2011, Yang 2014)
    Cross-species: fly brain shows similar downscaling (Gilestro 2009)


  WHY NOT EXPOSURE:

    SHY does NOT fire specific patterns.
    SHY does NOT re-activate learned content.
    SHY = GLOBAL process — ALL synapses affected.
    = No "contact with pattern" → not exposure.

    SHY = SIGNAL-TO-NOISE OPTIMIZER:
      Eliminates noise (weak random connections)
      Preserves signal (strong repeated patterns)
      → Next morning: "see more clearly" = noise REDUCED, signal relatively INCREASED


  IN COMPILE ARCHITECTURE:

    Compile Engine (Hebbian) while awake → creates MANY connections (both strong + weak)
    SHY during sleep → prunes weak → preserves strong
    = Quality control AFTER compile. Does NOT create new compile.

    Analogy: finish writing → re-read → delete redundant sentences.
    Deleting redundant sentences ≠ writing new sentences.


  🟢 Tononi & Cirelli 2003, 2014
  🟢 Maret 2011, Yang 2014 (dendritic spine evidence)
  🟢 Gilestro 2009 (cross-species drosophila)
  🟡 SHY = not exposure classification: framework synthesis
```

### §3.2 — Hippocampal Replay — IS exposure (internal)

```
🟢 REPLAY = PATTERN RE-FIRE COMPRESSED:

  Research: Wilson & McNaughton 1994 (seminal), O'Neill et al. 2010

  MECHANISM:
    While awake: hippocampal cells fire A→B→C→D (experience sequence)
    During sleep (SWS): cells RE-FIRE A→B→C→D at 10-20x compressed speed
    → Within sharp-wave ripples (SWRs: ~100-250 Hz bursts, ~50-100ms)
    → Each replay = 1 Hebbian strengthening event
    → 1 night = MANY replays = MANY Hebbian events

  EVIDENCE:
    Wilson & McNaughton 1994: rat hippocampus replay matches daytime navigation
    Lee & Wilson 2002: replay can be FORWARD or REVERSE
    O'Neill 2010: disrupting ripples → memory consolidation IMPAIRED
    Human analog: fMRI replay during rest (Tambini 2010, Schuck 2019)

  COMPRESSED SPEED:
    10-20x = 1 night replays the equivalent of SEVERAL DAYS of repetition
    Different plasticity rules at compressed speed (Staresina 2015)
    Spindle-ripple coupling coordinates replay × cortex transfer (Active Consolidation)


  WHY IT IS EXPOSURE:

    Replay = neurons FIRE TOGETHER → Hebbian → STRENGTHEN
    = COMPILE ENGINE operating on REPLAYED patterns
    = Internal exposure (Spontaneous variant during sleep)

    BUT: replay ≠ NEW exposure.
    Replay = RE-exposes what WAS ALREADY LEARNED.
    Does not create NEW patterns — only STRENGTHENS old ones.


  IN COMPILE ARCHITECTURE:

    Replay = the ONLY fully exposure-based mechanism in the sleep system.
    Replay feeds into Compile Engine (Hebbian) → strengthens existing compiled chunks.
    = Spontaneous sleep variant: automatic internal exposure, PFC offline.

    Different from Exposure-Spontaneous while awake:

    ┌──────────────────┬──────────────────────┬────────────────────┐
    │                  │ Spontaneous (awake)  │ Replay (sleep)     │
    ├──────────────────┼──────────────────────┼────────────────────┤
    │ Trigger          │ Context, random      │ Hippocampus-driven │
    │ Speed            │ Normal               │ 10-20x compressed  │
    │ Organization     │ Unstructured         │ Systematic (SWRs)  │
    │ PFC influence    │ Possible (partial)   │ None (offline)     │
    │ External input   │ Possible (External)  │ None (blocked)     │
    │ Efficiency       │ Low                  │ High               │
    └──────────────────┴──────────────────────┴────────────────────┘

    → Replay = "industrial-grade Spontaneous" — same principle, different execution.


  🟢 Wilson & McNaughton 1994
  🟢 Lee & Wilson 2002
  🟢 O'Neill et al. 2010
  🟢 Staresina et al. 2015 (spindle-ripple coupling)
  🟡 Replay = Spontaneous sleep variant: framework synthesis
```

### §3.3 — Active Systems Consolidation — NOT exposure

```
🟢 ACTIVE CONSOLIDATION = HIPPOCAMPUS → CORTEX TRANSFER:

  Research: Born & Wilhelm 2012, Diekelmann & Born 2010

  MECHANISM:
    New memories start HIPPOCAMPUS-DEPENDENT (hippocampus needed for recall)
    → Through sleep (SWS): memories TRANSFER to NEOCORTEX-DEPENDENT
    → Hippocampus "teaches" cortex via spindle-ripple coupling
    → Cortex builds OWN representation, independent of hippocampus
    → Weeks to months for full transfer (complex memories)

  DISTINCT FROM REPLAY:
    Replay = firing event (neurons fire)
    Active Consolidation = long-term TRANSFER that replay enables
    Replay = necessary SUBSTRATE. Consolidation = the RESULT.
    → Replay WITHIN Consolidation, but Consolidation ≠ Replay.

  EVIDENCE:
    Squire 1992: hippocampal damage → anterograde amnesia (new)
                                    but spares old memories (already consolidated)
    Takashima 2006: fMRI shows decreasing hippocampal + increasing cortical activation
    Rasch & Born 2013: sleep-dependent nature confirmed


  WHY NOT EXPOSURE:

    Active Consolidation = RELOCATES, not STRENGTHENS.
    Pattern moves from hippocampus → cortex.
    = Architectural reorganization, not re-activation for Hebbian.

    Analogy: move a file from USB (temporary) to hard drive (permanent).
    Moving a file ≠ writing a new file.
    File content does NOT change — location changes.


  IN COMPILE ARCHITECTURE:

    Active Consolidation interacts with Compile Engine INDIRECTLY:
    → Replay → Hebbian strengthen (Compile Engine)
    → Consolidation USES replay output to transfer location
    → After Consolidation: chunk accessible WITHOUT hippocampus
    → = "Permanent installation" — from RAM (hippocampus) to ROM (cortex)

    IMPLICATION:
      While awake: newly learned = hippocampus-dependent = FRAGILE
      After sleep Consolidation: cortex-dependent = STABLE
      → "Clearer recall tomorrow morning" = Consolidation successfully transferred
      → "Simple things take one night, complex things take weeks"
        = complex → many Consolidation cycles for full transfer


  🟢 Born & Wilhelm 2012
  🟢 Squire 1992 (hippocampal amnesia)
  🟢 Takashima 2006 (fMRI evidence)
  🟢 Rasch & Born 2013 (review)
  🟡 Active Consolidation = not exposure (relocation): framework synthesis
```

### §3.4 — REM Creative Linking — PARTIAL exposure

```
🟢 CREATIVE LINKING = NEW REMOTE ASSOCIATIONS:

  Research: Cai et al. 2009, Wagner et al. 2004

  MECHANISM:
    REM features: HIGH acetylcholine + LOW norepinephrine + theta oscillations
    → "Associative gating" WEAKENED:
      While awake: strong associations dominate (focused thinking)
      During REM: weak associations CAN fire (unfocused, cross-domain)
    → Concepts from DIFFERENT DOMAINS fire together
    → Weak novel combinations that MATCH schemas → strengthened
    → Result: next morning = new creative links available

  EVIDENCE:
    Cai 2009: Remote Associates Test (RAT) improvement after REM
      (not just quiet rest or NREM — REM SPECIFICALLY)
    Wagner 2004: Number Reduction Task — sleep doubles hidden pattern discovery
      (8% → 23% find hidden shortcut)
    Cross-species: REM present in all mammals + birds → evolutionary conserved
    Stickgold 1999: sleep improves emotionally salient recall, REM specifically


  WHY PARTIAL EXPOSURE:

    HAS exposure element: concepts FIRE TOGETHER → Hebbian → new link
    = TECHNICALLY Compile Engine operating on novel combinations

    BUT mechanism DIFFERENT from typical exposure:
    ① Random activation (not intentional exposure)
    ② Weak gating (not normal associative gating)
    ③ Only SOME combinations strengthen (match schema = survive)
    ④ No external input, no PFC direction
    → = "Exploration" rather than "exposure"

    = PARTIALLY exposure: Compile Engine involved, but MECHANISM different.


  IN COMPILE ARCHITECTURE:

    Creative Linking = the ONLY form of compile in sleep that creates NEW connections.
    (Replay only strengthens OLD connections.)

    Creative Linking interacts with Exposure-Spontaneous:
    → Creative Linking in REM creates new links
    → Next morning: new links CAN fire automatically (Spontaneous)
    → "Eureka on waking" = Creative Linking output fires for the first time when conscious


  🟢 Cai et al. 2009
  🟢 Wagner et al. 2004
  🟢 Stickgold 1999
  🟡 Creative Linking = partial exposure (novel mechanism): framework synthesis
```

### §3.5 — Emotional Decoupling — NOT exposure

```
🟢 EMOTIONAL DECOUPLING = STRIPS EMOTIONAL TAG, PRESERVES CONTENT:

  Research: Walker 2017, van der Helm et al. 2011

  MECHANISM:
    REM: LOW noradrenaline + HIGH amygdala reactivation
    → Amygdala "fires WITHOUT stress chemistry"
    → Repeated REM cycles → decouple amygdala response from memory retrieval
    → CONTENT preserved (you remember the event)
    → EMOTIONAL TAG reduced (it feels "less intense")

  = "Sleep on it" = emotional charge DECREASES, knowledge PRESERVED.

  EVIDENCE:
    van der Helm 2011: REM reduces amygdala reactivity to emotional stimuli
    Walker 2005: sleep-deprived → heightened amygdala reactivity
    Germain 2013: disrupted REM correlates with PTSD emotional memory problems


  WHY NOT EXPOSURE:

    Decoupling does NOT fire patterns for Hebbian strengthening.
    Decoupling MODIFIES existing compiled chunk:
      Strip emotional tag ← chunk remains
      = EDITING, not CREATING.

    Analogy: adjusting the color temperature of a photo.
    The photo (content) does NOT change. The color (emotional tag) changes.
    Adjusting a photo ≠ taking a new photo.


  IN COMPILE ARCHITECTURE:

    Emotional Decoupling interacts with Entity-Valence:
    → Emotional tag = part of valence profile
    → Decoupling reduces emotional intensity → Entity-Valence UPDATE
    → Next morning: event still has valence, but INTENSITY reduced

    FAILURE MODE:
      Chronic REM disruption (insomnia, alcohol, PTSD):
      → Decoupling fails → emotional tags ACCUMULATE
      → Every day adds emotional charge WITHOUT decoupling
      → = Burnout, emotional exhaustion, PTSD escalation
      → Cortisol-Baseline.md v2.2: "break fast, build slow"

    CONNECTION TO TRAUMA THERAPY:
      EMDR: hypothesized to partially simulate Decoupling mechanism while awake
      → Bilateral stimulation may mimic REM-related processing
      → 🟡 Mechanism debated but clinical efficacy established (Stickgold 2002)

      Exposure therapy (Foa & Kozak 1986):
      → Different mechanism: create NEW exposure (PFC Modulation → Entity-Valence Bias indirect)
      → Decoupling = STRIP old emotional tag (sleep-specific, no new exposure)
      → Both reduce emotional reactivity, but via DIFFERENT paths


  🟢 Walker 2017
  🟢 van der Helm et al. 2011
  🟢 Walker 2005 (sleep deprivation → amygdala)
  🟢 Germain 2013 (PTSD × REM)
  🟡 Emotional Decoupling × Entity-Valence Bias interaction: framework synthesis
  🟡 EMDR × Emotional Decoupling analogy: hypothesized (Stickgold 2002)
```

### §3.6 — Gist Extraction — PARTIAL exposure

```
🟢 GIST EXTRACTION = ABSTRACTS, DISCARDS DETAIL:

  Research: Payne et al. 2009, Stickgold 2013, Tamminen 2010

  MECHANISM:
    Replay re-fires sequences many times
    → Shared features ACROSS SIMILAR experiences = REINFORCED
    → Unique surface details of EACH experience = NOT reinforced
    → Relative contrast → GIST dominant in later recall
    → = Abstract pattern emerges, specific details fade

  EVIDENCE:
    Payne 2009: sleep increases false memory for gist-consistent items
      (DRM paradigm — evidence that gist is being extracted)
    Stickgold 2013: sleep abstracts "rules" from examples
    Tamminen 2010: sleep necessary for integrating new words into semantic network
    Lutz 2017: gist extraction scales with sleep duration


  WHY PARTIAL EXPOSURE:

    HAS exposure element:
    → Gist Extraction relies on Replay as substrate
    → Shared features fire TOGETHER across replays → Hebbian → gist
    → = Compile Engine operating on ABSTRACTED patterns

    BUT:
    → Primary function = EXTRACT (generalize), not STRENGTHEN specific
    → TRADE-OFF: gist preserved, detail LOST
    → = Net effect: DIFFERENT kind of compile (abstract, not specific)

    Analogy: read 100 articles → summarize into 1 paragraph.
    The summary = new content (gist). But 100 articles = LOST.
    = Creation BY destruction. New (gist) replaces old (details).


  IN COMPILE ARCHITECTURE:

    Gist Extraction interacts with BACKGROUND-PATTERN formation:
    → Background-Pattern.md v2.0 §3: sleep gist extraction abstracts
      repeated events into single pattern
    → Gist Extraction = PRIMARY MECHANISM creating Background-Pattern
    → Background-Pattern = accumulated gist over YEARS of Gist Extraction cycles

    Gist Extraction → Background-Pattern → Exposure-Spontaneous:
    → Gist Extraction creates gist → gist becomes part of Background-Pattern
    → Background-Pattern fires continuously (Spontaneous)
    → Spontaneous → Compile Engine → reinforces gist further → snowball

    = Why "optimistic people" see EVERYTHING in a positive light:
      Years of positive experiences
      → Gist Extraction extracts positive gist
      → Background-Pattern = positive-dominant
      → Spontaneous fires positive → biases ALL new exposure
      → = Self-reinforcing via Gist Extraction → Spontaneous → Compile Engine loop


  🟢 Payne et al. 2009
  🟢 Stickgold 2013
  🟢 Tamminen 2010
  🟢 Lutz 2017
  🟡 Gist Extraction → Background-Pattern formation link: framework synthesis
```

### §3.7 — Dreaming as Simulation — DEBATED (excluded from core)

```
🟡 THREAT SIMULATION THEORY (DEBATED):

  Research: Revonsuo 2000, Nielsen & Levin 2007
  Status: 🟡 Debated — NOT reliable enough to include in core architecture

  Claim: REM dreams = simulations of threat/life-relevant scenarios.
  Evidence for: dreams bias negative (Schredl 2010), cross-cultural consistency
  Evidence against: many dreams mundane/positive/bizarre, random-activation viable

  FRAMEWORK POSITION:
    → Noted for completeness but NOT relied upon.
    → If dreaming is correct = adds 1 mechanism to Sleep Maintenance.
    → If dreaming is wrong = 6 remaining mechanisms still sufficient.
    → Awaiting future research before formalizing.

  🟡 Revonsuo 2000
  🟡 Not included in core architecture (insufficient evidence)
```

### §3.8 — Summary table: 6 mechanisms × architecture role

```
⭐ SUMMARY:

  ┌────┬──────────────────────┬───────────┬─────────────────┬──────────────────────────┐
  │ #  │ Mechanism             │ Stage     │ Exposure?       │ Architecture role        │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  1 │ SHY Homeostasis       │ SWS       │ ❌ NOT          │ Quality control          │
  │    │                       │           │                 │ (prune weak)             │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  2 │ Hippocampal Replay    │ SWS       │ ✅ YES          │ Strengthen existing      │
  │    │                       │           │ (internal,      │ (Compile Engine offline)  │
  │    │                       │           │  compressed)    │                          │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  3 │ Active Consolidation  │ SWS       │ ❌ NOT          │ Relocate                 │
  │    │                       │           │                 │ (RAM → ROM)              │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  4 │ Creative Linking      │ REM       │ 🟡 PARTIAL      │ Create new links         │
  │    │                       │           │ (novel combos)  │ (exploration)            │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  5 │ Emotional Decoupling  │ REM       │ ❌ NOT          │ Calibrate valence        │
  │    │                       │           │                 │ (strip emotional tag)    │
  ├────┼──────────────────────┼───────────┼─────────────────┼──────────────────────────┤
  │  6 │ Gist Extraction       │ SWS+REM   │ 🟡 PARTIAL      │ Abstract + generalize    │
  │    │                       │           │ (new abstract)  │ (→ Background-Pattern)   │
  └────┴──────────────────────┴───────────┴─────────────────┴──────────────────────────┘

  ~1.5 exposure-based. ~4.5 optimization-based.
  → MAJORITY of sleep = optimization of EXISTING compile.
  → Sleep ≠ "just more repetition."


  WHY MULTI-MECHANISM IS THE CORRECT FRAMING (Learning-Cycle.md §4.9):

    Single-mechanism view ("sleep consolidates memory") does NOT explain:
    ① Why 2 sleep stages exist (SWS vs REM distinct chemistry)
    ② Why SPECIFIC disruption causes SPECIFIC deficit
    ③ Why evolution maintains ~1/3 of lifespan in sleep if only 1 function
    ④ Why "next morning" = pleasant + comfortable + seeing new connections
       = 3 distinct improvements simultaneously

    Multi-mechanism view explains all 4.
```

---

## §4 — Sleep × Compile Architecture

```
⭐ SLEEP INTERACTS WITH EACH COMPONENT OF COMPILE ARCHITECTURE:

  Sleep Maintenance does NOT operate INDEPENDENTLY.
  Sleep ENHANCES, CALIBRATES, or RESTORES each component.
```

### §4.1 — Sleep × Compile Engine (Hebbian)

```
🟡 SLEEP ENHANCES COMPILE ENGINE VIA 3 PATHWAYS:

  ① Replay = Compile Engine operating OFFLINE:
     Replayed patterns → Hebbian strengthen → same mechanism as waking
     BUT: COMPRESSED speed (10-20x) = efficient
     BUT: NO external input = only strengthens WHAT WAS ALREADY LEARNED
     BUT: SYSTEMATIC (hippocampus-driven, not random)

     Net effect: Compile Engine gets "bonus exposure cycles" during sleep.
     = Why "clearer recall next morning" = more Hebbian cycles occurred.

  ② SHY IMPROVES Compile Engine efficiency:
     Prune weak connections → next day Compile Engine runs on CLEANER network
     → Signal-to-noise ratio BETTER → compile quality HIGHER next day
     → = "Fresh start" effect — not new knowledge, but cleaner processing.

  ③ Gist Extraction creates NEW inputs for Compile Engine:
     Gist = abstract pattern = new compiled chunk
     → Tomorrow's Compile Engine can build ON TOP of abstracted knowledge
     → = Expertise Compile: each night compresses → pyramidal stacking


  🟡 Sleep enhances Compile Engine via 3 mechanisms: framework synthesis
  🟢 Replay = Hebbian during sleep: Wilson & McNaughton 1994
  🟢 SHY improves signal-to-noise ratio: Tononi & Cirelli 2014
```

### §4.2 — Sleep × Entity-Valence Bias

```
🟡 SLEEP CALIBRATES ENTITY-VALENCE BIAS:

  Emotional Decoupling directly affects Entity-Valence:
  → Reduces emotional INTENSITY of entity associations
  → Entity-Valence profile: content preserved, peak valence reduced
  → Next morning: entity still has valence, but less REACTIVE

  MECHANISM:
    While awake: encounter entity → emotional peak → Compile Engine compiles
    During sleep: Decoupling strips emotional peak → same entity, lower intensity
    → Next encounter: entity triggers LESS extreme response
    → = Entity-Valence Bias CALIBRATED: not removed, but TUNED

  EXAMPLE:
    Argument with a friend last night → emotional peak: angry + hurt
    Decoupling during REM: amygdala reactivates WITHOUT noradrenaline
    → Emotional tag REDUCED
    → Next morning: still remember the argument, but feel "less angry"
    → = Entity-Valence [friend] updated: anger REDUCED, content PRESERVED

  Gist Extraction also affects Entity-Valence Bias indirectly:
  → Abstracts PATTERNS from entity interactions
  → Long-term: entity structural valence built from gist of MANY interactions
  → = Entity-Compiled.md: 40→200 hours formation time
    = MANY Gist Extraction cycles abstracting entity gist over months


  🟡 Emotional Decoupling calibrates Entity-Valence Bias: framework synthesis
  🟢 Emotional decoupling: van der Helm 2011
  🟢 Amygdala reactivity reduced after sleep: Walker 2005
```

### §4.3 — Sleep × Exposure Channels

```
🟡 SLEEP = INDEPENDENT OF NORMAL SOURCE CHANNELS:

  During sleep:
    Exposure-External = BLOCKED (thalamic gating, sensory input suppressed)
    Exposure-Deliberate = OFFLINE (PFC minimal activity, no deliberate thought)
    Exposure-Spontaneous = ACTIVE but in DIFFERENT mode (Replay)

  → Sleep operates INDEPENDENT of normal External/Deliberate/Spontaneous channels.
  → Sleep has its OWN internal activation system (hippocampus-driven replay).
  → = Why sleep = SEPARATE Sleep Maintenance, not a variant of Exposure.


  Replay ≈ Spontaneous VARIANT but DIFFERENT:
    Replay = organized, compressed, systematic, PFC offline
    Spontaneous (awake) = unstructured, normal speed, PFC possible
    → Replay = "industrial-grade Spontaneous" — same principle, different execution.

  Creative Linking interacts with Spontaneous THE NEXT DAY:
    Creative Linking creates new links in REM
    → Next morning: new links CAN fire automatically (Spontaneous)
    → "Eureka on waking" = Creative Linking output fires for the first time when conscious


  🟡 Sleep independent of External/Deliberate/Spontaneous: framework synthesis
  🟢 Thalamic gating during sleep: established polysomnography
  🟢 PFC reduced activity during SWS: established neuroimaging
```

### §4.4 — Sleep × PFC Modulation

```
🟡🟢 SLEEP RESTORES PFC MODULATION:

  During sleep: PFC = OFFLINE.
  → PFC Modulation does NOT operate
  → No Hold, no Suppress = "PFC rest mode"

  BUT: sleep RESTORES PFC function for the next day:

  ① Catecholamine restoration:
     PFC-Operations.md v1.3: PFC budget recharges via sleep
     → Dopamine + Norepinephrine pools REFILL during sleep
     → Next morning: PFC FULL of catecholamine = OPTIMAL performance

  ② Cortisol effects CLEAR:
     Cortisol-Baseline.md v2.2: sustained cortisol → gene expression → neural wear
     → Sleep = recovery window → cortisol effects PARTIALLY cleared
     → "Morning: catecholamine FULL + cortisol effects LOW = PFC optimal"
     → "Evening: catecholamine DEPLETED + cortisol effects HIGH = PFC weakened"

  ③ Synaptic efficiency restored (SHY):
     → PFC synapses also downscaled → more efficient processing
     → = PFC "refreshed" — same hardware, cleaner connections


  IMPLICATION:
    Sleep deprivation → PFC Modulation degrades FIRST:
    → PFC = most metabolically expensive brain region
    → PFC = most sensitive to catecholamine depletion
    → = Why sleep deprivation → impulsive, emotional, poor judgment
    → = PFC Modulation OFFLINE → Entity-Valence Bias UNCHECKED
    → = Detail: §5 (Sleep Deprivation).


  🟢 Catecholamine restoration during sleep: Arnsten 2009
  🟢 PFC sensitivity to sleep deprivation: Yoo et al. 2007
  🟡 PFC degrades first under sleep deprivation: framework synthesis
```

---

## §5 — Sleep Deprivation = Architecture Degradation

```
⭐⭐ SLEEP DEPRIVATION = ALL 6 MECHANISMS DISRUPTED SIMULTANEOUSLY:


  ┌───────────────────────┬──────────────────────────────────────────┐
  │ MECHANISM DISRUPTED   │ CONSEQUENCE                              │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ SHY absent            │ Synapses not pruned → noise ACCUMULATES  │
  │                       │ → Signal-to-noise ratio DECREASES        │
  │                       │ → Next day learning IMPAIRED             │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Replay absent         │ Patterns not strengthened → FRAGILE      │
  │                       │ → Memory WORSE than pre-sleep            │
  │                       │ → What was learned → not consolidated    │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Consolidation miss    │ Hippocampus → cortex transfer STALLED    │
  │                       │ → Knowledge stuck in "temporary storage" │
  │                       │ → Hippocampus FULL → new learning blocked│
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Creative Linking miss │ No remote associations formed            │
  │                       │ → No "eureka moments" next day           │
  │                       │ → Problem-solving capacity REDUCED       │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Decoupling miss       │ Emotional tags NOT stripped              │
  │                       │ → Emotions ACCUMULATE day-over-day       │
  │                       │ → Reactivity INCREASES                   │
  │                       │ → Trajectory: burnout, PTSD escalation   │
  ├───────────────────────┼──────────────────────────────────────────┤
  │ Gist absent           │ No abstraction → details overwhelm      │
  │                       │ → Can't see "big picture"                │
  │                       │ → Background-Pattern formation slowed    │
  └───────────────────────┴──────────────────────────────────────────┘


  ARCHITECTURE COLLAPSE ORDER:

    1st: PFC Modulation → depleted catecholamine
         → PFC = most expensive, most sensitive
    2nd: all 6 mechanisms missed → chunks degrade
    3rd: Compile Engine still runs but on DIRTY network
    4th: Entity-Valence Bias unchecked → emotional amplification
    → = Compound degradation

    "Tired → irritable → don't want to see anyone → poor decisions"
    = PFC down → Entity-Valence unchecked → emotional reactivity ↑
      → social avoidance → poor judgment


  CORTISOL INTERACTION (Cortisol-Baseline.md v2.2):

    Sleep deprivation → cortisol baseline DRIFT UP
    → Cortisol = gene expression effects → neural wear
    → "Break fast, build slow":
      Cortisol elevation: hours to days
      Recovery: weeks to months
    → = Sleep debt COMPOUNDS: each night of lost sleep = damage > 1 night to recover

    Chronic sleep deprivation → cortisol chronically elevated
    → All 6 Sleep mechanisms degraded + cortisol damage
    → = Double hit: no maintenance + active damage


  REWARD VULNERABILITY (Reward-Signal-Architecture.md v2.1):

    Sleep deprivation degrades Evaluative Reward FIRST
      (complex, compilation-dependent, VTA habituation stacks)
    Direct-State Reward PERSISTS as "hedonic floor"
      (hardware-based, CT afferents, simple comfort)

    → Sleep deprivation: "just want to eat well, lie comfortably"
      = Evaluative reward GONE, Direct-State still accessible
    → = Why sleep-deprived people → comfort food, simple pleasures


  🟢 Sleep deprivation → memory impairment: Walker & Stickgold 2004
  🟢 Sleep deprivation → amygdala hyperactivity: Yoo et al. 2007
  🟢 Sleep deprivation → PFC impairment: Killgore 2010
  🟢 Cortisol × sleep deprivation: Leproult & Van Cauter 2010
  🟢 Arnsten 2009 (catecholamine inverted-U)
  🟡 Architecture collapse order model: framework synthesis
  🟡 Evaluative vs Direct-State vulnerability: framework synthesis
```

---

## §6 — Waking Rest: Complement, Not Replacement

```
🟡🟢 WAKING REST OVERLAPS WITH SLEEP BUT DOES NOT REPLACE IT:

  Learning-Cycle.md §5:
    "Sleep is one path for refinement. Waking rest is another.
     Different hardware, different neurochemistry, different strengths."


  WAKING REST MECHANISMS:

  ① DMN activation (Raichle et al. 2001):
     PFC releases → Default Mode Network activates
     → Mind-wandering + autobiographical memory + future simulation
     → Some integration of disparate information
     → = Partial Consolidation + partial Creative Linking

  ② Incubation effect (Sio & Ormerod 2009 meta-analysis):
     Pause on problem → solution emerges "spontaneously"
     → DMN + subconscious processing continues in background
     → = Partial Creative Linking (while awake)

  ③ Walking boosts creativity (Oppezzo & Schwartz 2014):
     Divergent thinking +~60% vs sitting
     → Rhythmic gait + low cognitive load + sensory input
     → = Partial Creative Linking + External exposure (novel environment)

  ④ Meditation (Tang et al. 2015):
     Reduces DMN hyperactivity, enhances PFC-DMN coupling
     → Less rumination (negative Spontaneous reduced)
     → Background integration without wandering interference
     → = Partial Decoupling (emotional regulation) + partial Consolidation (integration)


  WAKING REST vs SLEEP — COMPARISON:

  ┌────────────────────────┬───────────────────┬────────────────────────────┐
  │ Mechanism              │ Waking Rest       │ Sleep                      │
  ├────────────────────────┼───────────────────┼────────────────────────────┤
  │ SHY (prune)            │ ❌ NOT available  │ ✅ Full                    │
  │ Replay (Hebbian)       │ 🟡 Partial (DMN)  │ ✅ Full (SWR)              │
  │ Consolidation          │ 🟡 Partial (slow)  │ ✅ Full (fast)             │
  │ Creative Linking       │ 🟡 Partial         │ ✅ Full (REM)              │
  │ Emotional Decoupling   │ 🟡 Very partial    │ ✅ Full (REM NE↓)          │
  │ Gist Extraction        │ 🟡 Partial          │ ✅ Full                    │
  │ PFC restoration        │ ❌ NOT (PFC ON)    │ ✅ Full (catecholamine)    │
  │ Cortisol recovery      │ ❌ NOT             │ ✅ Partial                 │
  └────────────────────────┴───────────────────┴────────────────────────────┘


  ⭐ KEY INSIGHT:

  Waking rest CAN do ~30% of what sleep does:
    → Some replay (DMN), some creative links (incubation), some emotional regulation
    → USEFUL for mid-day breaks between learning sessions

  Waking rest CANNOT do ~70%:
    → NO SHY (prune) → noise accumulates
    → NO full REM mechanisms → emotional tags stay, creative links limited
    → NO PFC restoration → catecholamine still depleting
    → NO cortisol recovery → wear continues

  → Waking rest = COMPLEMENT, not substitute.
  → Nap (20-90 min) = INTERMEDIATE — some SWS but limited REM.
  → Full night sleep = IRREPLACEABLE for complete Sleep Maintenance function.

  "~30% / ~70%" = illustrative estimates, NOT precise measurements.
  Core point: waking rest CANNOT replace sleep for the majority of mechanisms.


  🟢 DMN: Raichle et al. 2001
  🟢 Incubation: Sio & Ormerod 2009
  🟢 Walking: Oppezzo & Schwartz 2014
  🟢 Meditation: Tang et al. 2015
  🟢 Napping benefits: Mednick et al. 2003
  🟡 Waking rest as partial sleep (~30%): framework synthesis
```

---

## §7 — Honest Assessment

```
🟢 ESTABLISHED (strong research support):

  INDIVIDUAL MECHANISMS:
    SHY: Tononi & Cirelli 2003, 2014 (molecular + cross-species evidence)
    Replay: Wilson & McNaughton 1994 (seminal, replicated extensively)
    Active Consolidation: Born & Wilhelm 2012 (hippocampus → cortex transfer)
    Creative Linking: Cai 2009, Wagner 2004 (REM-specific creative improvement)
    Emotional Decoupling: Walker 2017, van der Helm 2011 (amygdala reactivity)
    Gist Extraction: Payne 2009, Stickgold 2013 (DRM paradigm evidence)

  SLEEP ARCHITECTURE:
    2 stages (SWS vs REM) with distinct functions: established polysomnography
    Stage-specific disruption → specific deficits: Gais 2000, Wagner 2001
    Sleep deprivation → PFC impairment: Yoo 2007, Killgore 2010
    Sleep deprivation → amygdala hyperactivity: Yoo 2007
    Cortisol × sleep: Leproult & Van Cauter 2010

  WAKING REST:
    DMN: Raichle 2001, Incubation: Sio & Ormerod 2009
    Walking: Oppezzo & Schwartz 2014, Meditation: Tang 2015


🟡 FRAMEWORK SYNTHESIS (logic consistent, built on established):

  Sleep Maintenance model:
    Sleep as separate component in Compile Architecture.
    Components individually established. Positioning = synthesis.

  Exposure vs Optimization classification:
    Novel classification. "Is this mechanism exposure?" = novel question.
    TESTABLE: if classification correct, disrupting Replay (exposure) should impair
    memory differently from disrupting SHY (optimization).

  "~1.5 exposure / ~4.5 optimization" count:
    Approximate. Creative Linking and Gist Extraction = PARTIAL → exact boundary subjective.
    Core insight (majority = optimization) robust regardless of exact count.

  Architecture collapse order (PFC first):
    Consistent with established PFC sensitivity to sleep deprivation.
    Specific sequential model = novel synthesis.

  Gist Extraction → Background-Pattern formation link:
    Consistent with Background-Pattern.md §3 + gist extraction research.
    Specific mechanism chain = novel framework claim.

  Waking rest ~30% overlap:
    Approximate. Based on mechanism-by-mechanism comparison.
    Individual overlaps established. Aggregate estimate = synthesis.


🔴 NEEDS MORE RESEARCH:

  Quantitative mechanism interaction: do 6 mechanisms run sequentially or concurrently in 1 night?
  Napping: which mechanisms are active at 20-min vs 90-min nap?
  Age-related sleep architecture → compile quality decline?
  DEC2 short sleepers: efficient mechanisms or skip some?
  Emotional Decoupling current vs structural Entity-Valence effect: how many cycles?
  Sleep as compile_rate parameter or maintenance?
  Cross-cultural variation in sleep practices × compile quality
```

---

## §8 — Open Questions

```
🔴 UNANSWERED QUESTIONS:


  Q1: SLEEP MECHANISMS — SEQUENTIAL OR CONCURRENT?

     Within 1 night: do 6 mechanisms run sequentially or in parallel?
     Evidence suggests: SWS mechanisms (SHY, Replay, Consolidation, Gist) mostly sequential with overlap
     REM mechanisms (Creative Linking, Decoupling) concurrent within REM episode
     BUT: cross-cycle interactions not yet clear
     → Implications: alcohol suppresses SWS (Ebrahim 2013), SSRIs suppress REM
       (Wilson & Argyropoulos 2005) → stage-specific mechanism loss

     🟢 Alcohol suppresses SWS: Ebrahim et al. 2013
     🟢 SSRIs suppress REM: Wilson & Argyropoulos 2005
     🔴 Cross-mechanism interaction during night: needs more research


  Q2: NAPPING — WHICH MECHANISMS ARE ACTIVE?

     20-min nap: mainly SHY (partial) + Replay (partial)
     90-min nap: 1 full NREM/REM cycle → all 6 mechanisms (all partial)
     → Napping research supports memory improvement (Mednick et al. 2003)
     → BUT: napping ≠ full night (fewer cycles, less accumulation)

     🟢 Napping benefits: Mednick et al. 2003
     🔴 Quantitative nap vs full night: needs measurement


  Q3: AGE-RELATED SLEEP ARCHITECTURE CHANGES:

     Children: MORE SWS → more SHY/Replay/Consolidation/Gist → faster consolidation
     Elderly: LESS SWS + LESS REM → all 6 mechanisms ALL reduced
     → = Age-related compile quality decline PARTIALLY explained by sleep?

     🟢 Sleep architecture changes with age: Ohayon et al. 2004
     🔴 Sleep mechanism degradation → compile quality: needs analysis


  Q4: INDIVIDUAL VARIATION IN SLEEP MECHANISMS:

     Genetic: DEC2 mutation → "short sleepers" (6h sufficient)
     → Do short sleepers have MORE EFFICIENT Sleep mechanisms?
     → Or do they simply SKIP some mechanisms?

     🟢 DEC2 mutation: He et al. 2009
     🔴 Short sleep → compile quality: unknown


  Q5: EMOTIONAL DECOUPLING × STRUCTURAL VALENCE:

     Decoupling strips emotional tag PER NIGHT (current valence).
     BUT: Structural Entity-Valence = accumulated over YEARS.
     → Decoupling only strips CURRENT emotional peak, NOT structural valence?
     → How many Decoupling cycles to shift structural valence measurably?
     → = Why "it's been a long time since the break-up but still sad" —
       Decoupling works on current, but structural valence = deep, slow,
       needs MANY Decoupling cycles

     🔴 Emotional Decoupling current vs structural effect: needs analysis


  Q6: COMPILE_RATE FORMULA × SLEEP:

     Current formula: f(exposure × saliency × contingency
                        × peak_valence × multi_modal_richness)
     → Sleep adds exposure (Replay) + modifies peak_valence (Decoupling)
       + modifies richness? (Creative Linking)
     → Should sleep be an ADDITIONAL parameter in formula?
     → Or: sleep = maintenance of existing parameters, not new parameter?

     🟡 Sleep as parameter vs maintenance: framework decision needed


  Q7: DREAMING (Dreaming as Simulation):

     Revonsuo 2000 Threat Simulation Theory — debated.
     If correct: adds 1 mechanism to Sleep Maintenance.
     If wrong: 6 mechanisms sufficient.
     → Awaiting future research.

     🟡 Revonsuo 2000 — insufficient evidence for architecture commitment
```

---

## §9 — Cross-References

### §9.1 — Framework files referenced

```
PRIMARY SOURCE:
  Learning-Cycle.md §4 — 6+1 sleep mechanisms, detailed evidence
  Learning-Cycle.md §5 — waking rest mechanisms

COMPILE ARCHITECTURE:
  Compile-Taxonomy.md v3.0 — 3 Compile Types (this file = Sleep Maintenance)

CORE FILES:
  Chunk.md v3.0 §2.1 ④ — Sleep consolidation (summary → this file = detail)
  Chunk.md v3.0 §2.2 — compile_rate formula (sleep × formula interaction)
  PFC-Operations.md v1.3 — PFC budget recharges via sleep
  Cortisol-Baseline.md v2.2 — Sleep = PRIMARY cortisol recovery
  Background-Pattern.md v2.0 §3 — Gist Extraction → Background-Pattern
  Entity-Valence-Dynamics.md v1.1 — VTA habituation × emotional dynamics
  Reward-Signal-Architecture.md v2.1 — Evaluative vs Direct-State vulnerability
  Simulation-Engine.md v1.1 — PFC offline during sleep
  Body-Base.md v3.3 §2 — Compilable Architecture (+ Sleep Maintenance)
```

### §9.2 — Research citations

```
ESTABLISHED (🟢):

  SLEEP MECHANISMS:
  Tononi & Cirelli 2003, 2014 — SHY (Synaptic Homeostasis Hypothesis)
  Wilson & McNaughton 1994 — Hippocampal replay (seminal)
  Lee & Wilson 2002 — Forward and reverse replay
  O'Neill et al. 2010 — SWR disruption → memory impairment
  Staresina et al. 2015 — Spindle-ripple coupling
  Born & Wilhelm 2012 — Active Systems Consolidation
  Diekelmann & Born 2010 — Sleep and memory consolidation review
  Squire 1992 — Hippocampal amnesia (classical evidence)
  Takashima 2006 — fMRI hippocampus → cortex transfer
  Rasch & Born 2013 — Sleep-dependent consolidation review
  Cai et al. 2009 — REM creative linking (RAT improvement)
  Wagner et al. 2004 — Sleep doubles insight discovery
  Stickgold 1999 — Sleep × emotional memory
  Walker 2017 — Emotional decoupling
  van der Helm et al. 2011 — REM reduces amygdala reactivity
  Walker 2005 — Sleep deprivation → amygdala hyperactivity
  Germain 2013 — PTSD × REM disruption
  Payne et al. 2009 — Gist extraction (DRM paradigm)
  Stickgold 2013 — Sleep abstracts rules
  Tamminen 2010 — Sleep integrates new words into semantic network
  Lutz 2017 — Gist extraction scales with sleep duration

  SLEEP STAGES:
  Gais et al. 2000 — SWS × declarative memory
  Wagner et al. 2001 — REM × emotional memory
  Ohayon et al. 2004 — Age-related sleep architecture changes

  SLEEP DEPRIVATION:
  Yoo et al. 2007 — Sleep deprivation → amygdala hyperactivity
  Killgore 2010 — Sleep deprivation → PFC impairment
  Leproult & Van Cauter 2010 — Cortisol × sleep deprivation
  Walker & Stickgold 2004 — Sleep deprivation → memory
  Arnsten 2009 — Catecholamine inverted-U

  SLEEP DISRUPTION:
  Ebrahim et al. 2013 — Alcohol suppresses SWS
  Wilson & Argyropoulos 2005 — SSRIs suppress REM
  Raskind et al. 2003 — Prazosin for PTSD nightmares

  DENDRITIC EVIDENCE:
  Maret 2011, Yang 2014 — Dendritic spine turnover
  Gilestro 2009 — Drosophila sleep downscaling

  INDIVIDUAL VARIATION:
  He et al. 2009 — DEC2 short sleep mutation

  WAKING REST:
  Raichle et al. 2001 — Default Mode Network
  Sio & Ormerod 2009 — Incubation meta-analysis
  Oppezzo & Schwartz 2014 — Walking × creativity
  Tang et al. 2015 — Meditation neuroscience review
  Mednick et al. 2003 — Napping benefits


FRAMEWORK SYNTHESIS (🟡):
  Sleep as Sleep Maintenance in compile architecture — 2026-06-01
  6 mechanisms × exposure classification — 2026-06-01
  Emotional Decoupling calibrates Entity-Valence Bias — 2026-06-01
  Gist Extraction → Background-Pattern formation link — 2026-06-01
  Architecture collapse order (PFC first) — 2026-06-01
  Waking rest = complement not replacement — 2026-06-01
  Replay = industrial-grade Spontaneous — 2026-06-01

DEBATED (🟡):
  Revonsuo 2000 — Threat Simulation Theory (dreaming)
  Stickgold 2002 — EMDR × REM analogy
```

---

> **PARENT**: Chunk.md v3.0 §2.1 ④ (summary → this file = detail)
> **COMPANION**: Compile-Taxonomy.md (1 Compile Engine + 3 Modulators + Sleep Maintenance)
> **SOURCE**: Learning-Cycle.md §4 (6+1 mechanisms research source)
