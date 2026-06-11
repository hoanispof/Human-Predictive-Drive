---
title: Body-Feedback Mechanism — Chunk Dynamics Classification
version: 2.1
created: 2026-04-20
updated: 2026-05-25 (v2.1 — §2.2-§2.4 Evaluative/Direct-State mapping extended for dissonance direction, Dissonance-Signal-Architecture v1.0 integration)
previous: v1.3 → backup/Body-Feedback-Mechanism-v1.3-backup.md
status: REFERENCE v2.1
scope: |
  CORE MECHANISM FILE: HOW body-feedback arises from chunk dynamics.
  NEW v2.0: Body-Need aggregate framing + Complexity Spectrum.
  2 input sources (Sensory-Driven / Pattern-Driven).
  3 chunk dynamics (Chunk-Shift / Chunk-Miss / Chunk-Gap).
  Compound mechanism. Quality Baseline Shift.
  Research anchors: Crespi 1942, Schultz 1997, Berridge 2003, Amsel, Flaherty 1996.
purpose: |
  Existing files classify body-feedback by INTENSITY (02-Dissonance.md, 14 levels),
  SOURCE (02-Dissonance.md §3, 3 Genuine Discomfort Sources), and PRECONDITION (5 Body-Feedback-Preconditions).
  This file adds Axis 4: CHUNK DYNAMICS — HOW chunks fire produces a signal.
  This axis matches the v7.8 "chunk-centric" principle: everything runs on chunks;
  classification must be chunk-based.
  v2.0 NEW: Body-Need aggregate concept — chunk dynamics = mechanism,
  body-need = aggregate OUTPUT. Complexity Spectrum (Simple→Social→Meta)
  shows SAME mechanism, DIFFERENT substrate level.
position: |
  Body-Feedback/ folder — peer with Body-Feedback.md (synthesis entry point).
  This file = MECHANISM reference (HOW body-feedback arises).
  Body-Feedback.md = ARCHITECTURE reference (WHAT body-feedback does + Body-Feedback-Precondition).
  01-04 files = CASE ANALYSES (apply mechanism to specific scenarios).
dependencies:
  - Chunk.md v2.2 — chunk substrate, context-tag model
  - Chunk-Activation-Dynamics.md — probability, re-linking, trigger surface
  - Valence-Propagation.md v1.4 — valence per-entity + chain propagation
  - Body-Feedback.md v1.1 — Body-Feedback-Precondition, dual-pull, interface loop
  - Body-Feedback-Precondition.md v1.0 — 5 preconditions formal definitions (§6.2 mapping)
  - Body-Feedback-Label.md v2.0 — vocabulary reference (3-tier labels)
  - 02-Dissonance.md — intensity levels, source taxonomy, case analyses
  - Core-Software.md — cycle architecture, A/B/C/D zones
  - Cortisol-Baseline.md v2.0 — amplifier, holding signal
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles
  - Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State Dissonance, Mismatch Splitting, Evaluative Gates
  - Inter-Body-Mechanism.md v1.0 — Body-Need aggregate, 3-cost, 5-channel
  - Gap-Direction.md v1.1 — gap has direction = f(surrounding chunks)
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Mechanism — Chunk Dynamics Classification

> **Same event: "lost 100k."**
> Dropped it accidentally → regret. Scammed → regret + anger. Scammed by a close friend → regret + anger + bitterness.
>
> Same monetary loss. But chunk patterns fire DIFFERENTLY.
> Each additional chunk layer adds another "flavor" of dissonance.
>
> Body-feedback isn't just direction (reward/dissonance) and magnitude (mild → extreme).
> Body-feedback also has **chunk dynamics** — HOW chunks fire produces the signal.
>
> These signals INTEGRATE into **body-need** — the current STATE OF NEED
> that the body demands be met. Body-need = aggregate output of chunk dynamics.
>
> This file formalizes that classification axis + body-need aggregate framing.

---

## Table of Contents

- §0 — THESIS + POSITION IN FRAMEWORK
- §1 — BODY-NEED: AGGREGATE OUTPUT
- §2 — 2 INPUT SOURCES (Sensory-Driven / Pattern-Driven)
- §3 — 3 CHUNK DYNAMICS (Chunk-Shift / Chunk-Miss / Chunk-Gap)
- §4 — COMPOUND MECHANISM
- §5 — QUALITY BASELINE SHIFT
- §6 — MAP TO FRAMEWORK (v7.8 Cycle + Body-Feedback-Precondition)
- §7 — RESEARCH ANCHORS
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES

---

## §0 — THESIS + POSITION IN FRAMEWORK

```
⭐ 4 AXES OF BODY-FEEDBACK CLASSIFICATION:

  Body-feedback signal has 4 ORTHOGONAL (independent) classification axes:

  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  AXIS 1 — DIRECTION:                                            │
  │    Reward (opioid) / Dissonance (mismatch) / Neutral            │
  │    → Body-Feedback.md §2 dual-pull                              │
  │                                                                 │
  │  AXIS 2 — MAGNITUDE (intensity):                                │
  │    14 levels: nagging unease → emergency → shutdown             │
  │    → 02-Dissonance.md (case-based intensity spectrum)           │
  │                                                                 │
  │  AXIS 3 — SOURCE (external origin):                             │
  │    3 Genuine Discomfort Sources: nociception, mismatch,         │
  │    recalibration                                                │
  │    → 02-Dissonance.md §3 + Body-Feedback.md §5                  │
  │                                                                 │
  │  AXIS 4 — CHUNK DYNAMICS (chunk mechanism) ← THIS FILE         │
  │    HOW chunks fire produces the signal                          │
  │    2 input sources × 3 dynamics × compound                      │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  4 ORTHOGONAL axes = each axis DESCRIBES A DIFFERENT ASPECT:
    → Same signal can be: reward (axis 1) + mild (axis 2)
      + social (axis 3) + Chunk-Shift (axis 4)
    → 4 axes do NOT replace each other — they COMPLEMENT each other


⭐ v2.0 ADDITION: BODY-NEED AGGREGATE FRAMING

  This file does NOT just classify signals (axis 4).
  This file ALSO shows: signals INTEGRATE into BODY-NEED.

  Body-Need = aggregate output = the sum of ALL signals currently
  demanding to be met.
  §1 defines body-need. §2-§5 explain HOW body-need arises.
  = Missing link: "chunks fire" → "what the body needs" → "behavior"


  THIS FILE IN THE FLOW:

    Chunk.md v2.2 (sole substrate)
         │
         ▼
    Chunk-Activation-Dynamics (HOW chunks fire: probability, re-linking)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ BODY-FEEDBACK-MECHANISM.MD v2.0 (THIS FILE)                  │
    │                                                              │
    │  §1:  BODY-NEED = aggregate output                          │
    │  §2:  Input: 2 sources (Sensory-Driven / Pattern-Driven)   │
    │  §3:  Dynamics: 3 types (Chunk-Shift / Chunk-Miss / Gap)   │
    │  §4:  Compound: multiple dynamics simultaneous              │
    │  §5:  Baseline Shift: quality re-habituate                  │
    │                                                              │
    │  Output: body-feedback signal (direction + magnitude)        │
    │  = HOW chunk dynamics PRODUCE body-feedback → body-need      │
    │  = Missing layer between "chunks fire" and "what body needs" │
    └─────────────────────────────────────────────────────────────┘
         │
         ▼
    Body-Feedback.md (Body-Feedback-Precondition, dual-pull, interface loop)
    Feeling.md v2.0 (PFC observation of body-feedback)
    02-Dissonance.md (intensity spectrum + source taxonomy + case analyses)
    Inter-Body-Mechanism.md v1.0 (5-channel, 3-cost, entity interaction)
```

---

## §1 — BODY-NEED: AGGREGATE OUTPUT

### §1.1 — Definition

```
⭐ BODY-NEED = INTEGRATED CURRENT STATE OF NEED:

  Body-Need = aggregate of ALL signals currently demanding the body respond.

  NOT a single signal → it's the INTEGRATION of many parallel signals.
  NOT PFC-generated → body-need exists BEFORE PFC awareness.
  NOT only survival → ANY compiled gap fill (Compilable Architecture).

  Body-Need = OUTPUT OF THE MECHANISM this file describes:
    2 input sources (§2) → 3 chunk dynamics (§3) → compound (§4)
    → quality baseline shift (§5) → body-need aggregate

  (Inter-Body-Mechanism.md §2: Body-Need full definition + inter-body context)
```

### §1.2 — 2 genuine sources

```
⭐ BODY-NEED COMES FROM ONLY 2 GENUINE SOURCES:

  ┌─────────────────────────────────────────────────────────────┐
  │ ① HARDWARE / SENSORY-DRIVEN (pre-chunk possible):           │
  │                                                             │
  │   Homeostatic: hunger, thirst, temperature, oxygen, sleep  │
  │   Nociceptive: pain, injury, reflex                         │
  │   Hormonal: social isolation hardware, sexual drive         │
  │                                                             │
  │   → Domain stimulus → receptors → body signal              │
  │   → Does NOT require compiled chunks (animals have this)   │
  │   → D+C zones primary                                       │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │ ② CHUNK DYNAMICS / PATTERN-DRIVEN:                          │
  │                                                             │
  │   3 dynamics: Gap / Miss / Shift (+ Compound)               │
  │   → Internal chunk fire → body responds                     │
  │   → REQUIRES compiled chunks as prerequisite                │
  │   → Human-dominant (rich chunk network)                     │
  └─────────────────────────────────────────────────────────────┘

  ⭐ 2 sources are NOT mutually exclusive — 1 event activates BOTH ①+②:
    E.g.: eating food (① sensory) + recalling previous meal was better (② Miss)
    E.g.: social isolation (① hardware oxytocin deficit + ② compiled friend Miss)

  Details on each source: §2 of this file.
```

### §1.3 — Cross-cutting: NOT sources

```
🟡 OBSERVATION PARAMETERS AND STATE MODIFIERS = CROSS-CUTTING, NOT SOURCES:

  OBSERVATION PARAMETERS (named patterns, v7.8 — Protect.md §0):
    Protect = ownership chunks + loss aversion + avoidance direction
    Threat  = urgency tag + priority override (from ANY source)
    Status  = relative position pattern
    Novelty = gap-fill drive + approach direction
    → Emerge FROM ①+② in specific combinations
    → NOT separate sources — they are NAMES for observable patterns
    → Intervene at the mechanism level (①②), not at the label level

  STATE MODIFIERS:
    Cortisol: amplifies negative signals (Cortisol-Baseline.md v2.0)
    Urgency: overrides priority ranking
    Energy/fatigue: shifts threshold for all signals
    → Do NOT create new body-need — SHIFT priority/intensity of existing

  WHY THE DISTINCTION MATTERS:
    "Protect" is NOT a third source → "Protect" = Chunk-Miss (losing something compiled)
                                       + Chunk-Shift (threat to owned) + avoidance tag
    "Status drop" is NOT a third source → = Chunk-Miss (compiled position lost)
    Correct intervention = intervene at ①② mechanism
    Wrong intervention = treat label as independent cause → miss root mechanism

  (Inter-Body-Mechanism.md §2.3: cross-cutting clarification)
```

### §1.4 — 7 Properties of Body-Need

```
BODY-NEED HAS 7 PROPERTIES:

  ① ALWAYS EXISTS (never = 0)
     → "Lying relaxed on the beach" still has: sunlight = sensory gap fill
     → If gap = 0 → drive = 0 → behavior = 0 → death

  ② MULTIPLE simultaneous (parallel)
     → Hungry + bored + missing friends + career anxiety = 4 parallel body-needs

  ③ HAS PRIORITY (intensity × urgency × state)
     → "House on fire" overrides "boredom" (survival > novelty)
     → Priority = dynamic, shifts with state

  ④ HAS DIRECTION (from chunk network topology — Gap-Direction.md)
     → Only filling the correct direction produces reward
     → Direction = f(surrounding chunks) → unique per person

  ⑤ PFC DOES NOT ALWAYS KNOW (exists before awareness)
     → "Bored but don't know what's needed" = body-need present, PFC hasn't identified it
     → PFC guesses wrong direction = "TikTok" instead of "movement"

  ⑥ CAN CONFLICT (internal tension)
     → "Eat something delicious vs stay in shape" = 2 body-needs, opposite directions
     → PFC arbitrates → suppresses 1 → cost (Inter-Body §4)
     → Internal conflict = NORMAL, not pathological

  ⑦ CAN BE HIJACKED (temporary distortion)
     → Hormones (limerence): amplify 1 body-need → override all others
     → Scams: control input channels → direction distorted
     → Propaganda: collective fear → priority override
     → Domain Reality = final arbiter ALWAYS

  (Inter-Body-Mechanism.md §2.4: 7 properties full context)
```

### §1.5 — 4 Types by Immediacy

```
┌─────────────────────────────────────────────────┐
│ IMMEDIATE (seconds-minutes):    [① dominant]    │
│   Hunger, pain, heat. PFC knows clearly.        │
│   Direction is obvious.                         │
├─────────────────────────────────────────────────┤
│ SHORT-TERM (hours-days):        [①+② mix]      │
│   Boredom, loneliness, fatigue.                 │
│   PFC MAY NOT know clearly                      │
│   (scrolling TikTok when the actual need        │
│    is movement).                                │
├─────────────────────────────────────────────────┤
│ LONG-TERM (months-years):  [② meta dominant]   │
│   Career, Imagine-Final, relationship direction.│
│   PFC BUILDS direction over many years.         │
├─────────────────────────────────────────────────┤
│ STRUCTURAL (always running): [①hardware + ②structural] │
│   Social belonging. Autonomy. Coherence.        │
│   PFC usually NOT aware (until violated).       │
└─────────────────────────────────────────────────┘

  (Inter-Body-Mechanism.md §2.5: 4 immediacy types full context)
```

---

## §2 — 2 INPUT SOURCES

### §2.1 — Why distinguish 2 sources

```
🟡 BODY-FEEDBACK CAN ARISE FROM 2 DIFFERENT SOURCES:

  ① Domain changes → body-input changes → chunks fire IN RESPONSE
  ② Chunks fire INTERNALLY (replay, preview, comparison) → body responds IN RESPONSE

  Same output (body-feedback signal).
  But DIFFERENT input pathway → different timing, different zones, different species capability.

  Distinction matters because:
  → Identifies WHERE TO INTERVENE (fix environment vs fix internal patterns)
  → Explains WHY animals also have body-feedback (sensory-driven)
  → Explains WHY humans are richer (pattern-driven more powerful)
```

### §2.2 — Sensory-Driven (from body-input)

```
⭐ SENSORY-DRIVEN — DOMAIN COMES FIRST, CHUNKS FIRE IN RESPONSE:

  FLOW:
    Domain stimulus → receptors (17 categories) → neural signal
    → compiled chunks MATCH/MISMATCH → body-feedback fires

  CHARACTERISTICS:
    ① Body-input COMES FIRST — chunks fire REACTIVELY
    ② D+C zones primary (peripheral + subcortical)
    ③ Animals have this fully — PFC not required
    ④ Timing: 50ms (nociception reflex) → seconds (sensory processing)
    ⑤ BOTH reward AND dissonance

  DISSONANCE EXAMPLES:
    → Needle piercing skin → nociceptors fire → pain (D zone reflex)
    → Hot weather → thermoreceptors → discomfort
    → Cockroach → visual pattern match "disgust" → revulsion (C zone compiled)
    → Stiff clothing rubbing skin → somatosensory mismatch → discomfort
    → Trash pile → olfactory → revulsion

  REWARD EXAMPLES:
    → Good food → taste receptors → opioid (body-need met)
    → Captivating music → auditory pattern → opioid (Goldilocks match)
    → Pleasant scent → olfactory → pleasant
    → Soft clothing put on → somatosensory match → comfortable
    → Beautiful painting → visual Goldilocks → aesthetic reward

  IMPORTANT PROPERTY:
    → No PFC needed, no Imagine-Final needed
    → A dog enjoying better food — same mechanism
    → Body-input DIRECTLY drives chunk matching
    → Signal strength depends on delta between input and compiled baseline

  EVALUATIVE/DIRECT-STATE DIMENSION (Reward-Signal-Architecture §1 + Dissonance-Signal-Architecture §1):
    → Sensory-Driven ≈ DIRECT-STATE territory — BOTH DIRECTIONS:
      REWARD: Touch (CT afferents), warmth, taste = hardware-level
      DISSONANCE: Nociception, temperature deviation, hunger, itch = hardware-level
      Non-opioid/non-evaluative pathways, below PFC, minimal cortical involvement
    → Sensory-Driven CAN have Evaluative component when cortical evaluation present:
      Reward: Captivating music = auditory + cortical → Evaluative Reward
      Dissonance: "Cockroach on the plate" = visual + compiled disgust → Evaluative Dissonance
      Good food = taste + hedonic evaluation → Evaluative + Direct-State compound
    → "Pure sensory" = mostly Direct-State (BOTH reward AND dissonance).
      "Sensory + evaluation" = Evaluative + Direct-State compound.
    → Dissonance-Signal-Architecture.md §1: parallel distinction for dissonance direction.

  🟢 RESEARCH:
    → Sensory processing pathways: established neuroscience
    → Hedonic responses in animals: Berridge facial coding (tongue protrusion)
    → Taste preference without cognition: Berridge 2003 (dopamine-depleted rats
      still show liking reactions to sucrose placed in mouth)
    → Pain 2-component: Melzack & Casey 1968 (sensory-discriminative vs affective-motivational)
```

### §2.3 — Pattern-Driven (from internal chunk network)

```
⭐ PATTERN-DRIVEN — CHUNKS FIRE FIRST, BODY RESPONDS:

  FLOW:
    Internal chunk activity (replay, preview, comparison, gap detect)
    → body-base simulate/respond → body-feedback fires

  CHARACTERISTICS:
    ① Chunks fire INTERNALLY — NO new domain stimulus required
    ② B+C zones primary (cortical + subcortical), A(PFC) optional
    ③ Animals have this (hippocampal replay), humans are MUCH richer
    ④ Timing: seconds → years
    ⑤ BOTH reward AND dissonance
    ⑥ REQUIRES compiled chunks as prerequisite

  6 TRIGGER MECHANISMS (internal chunk fire):

    ⓐ REPLAY — hippocampus replays old experience
       → Sleep replay (🟢 Walker 2017)
       → Awake replay (spontaneous recall)
       → "Remembering being bitten by a dog" → body responds with fear

    ⓑ PREVIEW — PFC or hippocampus simulates future
       → Imagine-Final preview: "what if I had the car"
       → Body pre-feel: ~20-60% fidelity (Imagination.md §2)
       → Mice also do this: hippocampal preplay before navigation
         (🟢 Pfeiffer & Foster 2013)

    ⓒ COMPARISON — 2+ chunk patterns compared internally
       → Social comparison: "friend C is better than me"
       → Quality comparison: "yesterday's food was better"
       → PFC or unconscious can both do this

    ⓓ GAP DETECT — ACC/insula detect inconsistency in network
       → "Newtonian physics has contradictions" (Einstein)
       → "This framework is still missing something" (felt sense)
       → NO PFC required — ACC detects independently

    ⓔ SPREADING ACTIVATION — 1 chunk fires → cascade through network
       → Sister-B brags about her child → chunks about MY OWN child fire
       → Collins & Loftus 1975 🟢
       → Cascade can activate patterns that generate new dissonance

    ⓕ CONTEXT-FREE CHUNK FIRE — trauma chunk fires without context:
       → Chunk.md §2.6: context-free chunks = ④ state only, LACKING ①②③
       → Sensory cue → amygdala low road match (~12ms) → chunk fires INTERNALLY
       → Body responds AS IF in original trauma (full state metadata fires)
       → = Pattern-Driven because chunk fires INTERNALLY, not from external threat
       → BUT chunk LACKS temporal/spatial context → body DOESN'T KNOW it's the past
       → PFC arrives ~200ms LATER → corrective signal LATE + may be OFFLINE
       → = Flashback mechanism (PTSD-Analysis.md §4)
       → = Differs from ⓐ Replay: replay = hippocampal, HAS context → "remembering"
         ⓕ Context-free = amygdala, NO context → "reliving"
       → 🟢 LeDoux 1996: low road ~12ms, 🟢 Brewin 2010: S-rep

  DISSONANCE EXAMPLES:
    → Sister-A hears Sister-B brag about her child → comparison → heart twinge (comparison)
    → Einstein sees physics contradictions → restless unease (gap detect)
    → Remembering being betrayed → pain (replay)
    → Imagine-Final "beautiful car but don't have one yet" → lack (preview)

  REWARD EXAMPLES:
    → Imagine-Final "I'll solve this problem" → mini opioid (preview)
    → Remembering a beautiful memory → warmth (replay)
    → Comparison "I'm better than before" → confidence (comparison)
    → Gap fill: "Aha, I get it!" → opioid burst (gap filled)

  EVALUATIVE/DIRECT-STATE DIMENSION (Reward-Signal-Architecture §1 + Dissonance-Signal-Architecture §1):
    → Pattern-Driven = primarily EVALUATIVE territory — BOTH DIRECTIONS:
      REWARD: Cortical pattern match → OFC/vmPFC → opioid (if match)
        Insight, coherence, preview = all require cortical processing
      DISSONANCE: Social comparison → dACC, moral injury → vmPFC + ACC,
        anxiety preview → CRH → amygdala = all EVALUATIVE Dissonance
        (Dissonance-Signal-Architecture.md §1.3: MOST adult suffering = Evaluative)
    → Pattern-Driven CAN activate Direct-State:
      Reward: Replay of touch → body re-simulate → B partial activation
      Dissonance: Replay of pain → body re-simulate → Direct-State trace
    → Evaluative Gates Direct-State = GENERAL mechanism (both directions):
      Reward: A evaluation MODULATES B body-state reward response
      Dissonance: Placebo/Nocebo = PROOF (Wager 2004, Zubieta 2005)
        PFC evaluation MODULATES Direct-State pain (Dissonance-Signal-Architecture §3)
      = WHY "thinking about a hug" ≠ "actual hug" AND "fearing pain" amplifies actual pain

  🟢 RESEARCH:
    → Hippocampal replay/preplay: Pfeiffer & Foster 2013, Wilson & McNaughton 1994
    → Spreading activation: Collins & Loftus 1975
    → Social comparison: Festinger 1954
    → ACC error detection: Bush et al. 2000
```

### §2.4 — Comparing the 2 Sources

```
┌──────────────────────┬──────────────────────┬──────────────────────┐
│                      │ SENSORY-DRIVEN       │ PATTERN-DRIVEN       │
├──────────────────────┼──────────────────────┼──────────────────────┤
│ Trigger              │ Domain stimulus      │ Internal chunk fire  │
│ Direction            │ Outside → In         │ Inside → Body        │
│ Primary zones        │ D + C                │ B + C (A optional)   │
│ Reward type          │ Mostly Direct-State  │ Mostly Evaluative    │
│ Dissonance type      │ Mostly Direct-State  │ Mostly Evaluative    │
│ Animals              │ Yes, complete        │ Yes but limited      │
│ PFC required?        │ NO                   │ Optional             │
│ Timing               │ ms → seconds         │ seconds → years      │
│ Prerequisite         │ Receptors active     │ Compiled chunks      │
│ Dissonance example   │ Needle, heat, cockroach│ Comparison, recall  │
│ Reward example       │ Good food, captivating music│ Insight, preview│
│ Intervention         │ Fix environment      │ Fix internal pattern │
└──────────────────────┴──────────────────────┴──────────────────────┘

⭐ BOTH SOURCES → SAME OUTPUT: body-feedback signal (direction + magnitude)
⭐ BOTH SOURCES → can trigger ANY chunk dynamic (§3)
⭐ NOT mutually exclusive: 1 event can activate BOTH sources simultaneously
   E.g.: eating food (sensory) + recalling previous meal was better (pattern)
```

### §2.5 — Complexity Spectrum (same mechanism, different substrate)

```
🟡 3 DYNAMICS (§3) OPERATE AT ALL SUBSTRATE LEVELS:

  ┌─────────────────────────────────────────────────────────────────┐
  │ SIMPLE (physical objects, sensory patterns):                    │
  │   Chunk-Miss: soft clothing baseline → stiff clothing = "worse  │
  │               than usual"                                       │
  │   Chunk-Shift: familiar food → discover it's expired = valence  │
  │                flip                                             │
  │   Chunk-Gap: recipe missing one ingredient → "feels like        │
  │              something's off"                                   │
  ├─────────────────────────────────────────────────────────────────┤
  │ SOCIAL (entities, relationships):                               │
  │   Chunk-Miss: close friend absent = "missing them"              │
  │   Chunk-Shift: close friend betrays = valence flip entity chunks │
  │   Chunk-Gap: "they seem sad about something" = gap detected in  │
  │              Self-Pattern-Modeling model                        │
  ├─────────────────────────────────────────────────────────────────┤
  │ META (abstract compiled structures):                            │
  │   Chunk-Miss: Imagine-Final not reached = compiled preview missed│
  │               Status drop = compiled position lost              │
  │               Obligation violated = compiled prediction broken   │
  │   Chunk-Shift: Identity challenge = self-schema valence shift   │
  │   Chunk-Gap: "Life lacks meaning" = meta-gap in coherence       │
  └─────────────────────────────────────────────────────────────────┘

  ⭐ KEY INSIGHT — LEVEL 3 (META) COLLAPSE:

    Imagine-Final, Obligation, Identity, Status:
    = SAME chunk dynamics (Gap/Miss/Shift)
    = Only differ in SUBSTRATE LEVEL (meta-compiled structures)
    = Different timescale + PFC involvement + intervention approach
    = NOT separate mechanisms — NO new classification tier needed

    Why meta FEELS different:
    → Network size is larger (identity = hundreds of chunks)
    → Timescale is longer (career gap = years)
    → PFC involvement is higher (abstract requires cortical)
    → But BODY-FEEDBACK MECHANISM = SAME: Gap/Miss/Shift

    → Parsimony: 3 dynamics explain ALL levels
    → Intervention: identify WHICH dynamic + WHICH substrate
    → "Loss of life meaning" = Meta Chunk-Gap = ACC detects
      inconsistency in coherence network → body signal "restless unease"
      → same mechanism as "physics has contradictions" but different substrate

  (Inter-Body-Mechanism.md §2.2: complexity spectrum defined)
```

---

## §3 — 3 CHUNK DYNAMICS

### §3.0 — Overview

```
🟡 WHEN BODY-FEEDBACK FIRES, THE CHUNK NETWORK SHOWS 3 TYPES OF CHANGE:

  Chunk dynamics DESCRIBE: what happens INSIDE the chunk network when a signal is generated.

  ① CHUNK-SHIFT — valence OF chunks changes (content stays same)
  ② CHUNK-MISS  — an already-compiled pattern IS NOT FIRED (absent)
  ③ CHUNK-GAP   — a pattern NEVER EXISTED but network detects it's missing

  3 dynamics:
  → NOT mutually exclusive — 1 event can trigger 2-3 dynamics at once (§4)
  → Apply to BOTH reward AND dissonance (different direction, same mechanism)
  → Can be triggered by BOTH sensory-driven AND pattern-driven (§2)
  → Operate at ALL substrate levels: Simple / Social / Meta (§2.5)
```

### §3.1 — Chunk-Shift (valence changes)

```
⭐ CHUNK-SHIFT — SAME CHUNKS, DIFFERENT EVALUATION:

  DEFINITION:
    The valence (evaluation) of a chunk network IS CHANGED.
    Chunk content remains the same — the evaluation CHANGES.
    Can happen abruptly (1 event) or gradually (many events).

  MECHANISM:
    New information (1 new chunk or 1 new experience)
    → Re-evaluate valence of related chunks
    → Valence propagates through network (Valence-Propagation.md §4)
    → Body-feedback fires according to NEW valence

  DIRECTION:
    Shift NEGATIVE (dissonance):
      → Betrayal: chunks about the person STILL THERE, valence FLIPS negative
      → Counterfeit discovery: chunks about the product still there, valence drops
      → Bad news received about someone: chunks still there, valence shifts

    Shift POSITIVE (reward):
      → Successful exposure therapy: fear chunks → safety association grows
      → Learning to use a knife: fear valence → utility valence
      → Misunderstanding resolved: negative valence → positive restored

  WHY "SHIFT," NOT "FLIP":
    → "Flip" implies binary (+ → -), but it's actually a GRADIENT
    → Can shift slightly (mild disappointment) or sharply (betrayal)
    → Shift can be at DIFFERENT magnitudes across channels (Valence-Propagation §2)
    → "Shift" captures partial change

  CHARACTERISTICS:
    ① Chunk CONTENT doesn't change — memories remain intact
    ② Only VALENCE (evaluation) changes
    ③ Propagation through network: 1 chunk shifts → pulls others along
    ④ Intensity depends on: network size × shift magnitude × surprise level
    ⑤ Underlying mechanism: competitive re-linking (Chunk-Activation-Dynamics §3)

  EXAMPLE ANALYSIS — BETRAYAL:

    Before discovery:
      Chunks [partner] = {
        Visual: face, figure, smile — content
        Auditory: voice — content
        Somatic: embrace, kiss — content
        Emotional: love, trust, safety — VALENCE (positive)
      }

    After discovering "betrayal":
      1 NEW chunk compiles: [betrayal] (emotional peak, once is enough)
      → Valence propagation: [betrayal] → re-evaluate ALL connected chunks
      → Chunks [partner] = {
        Visual: SAME face, figure, smile — content UNCHANGED
        Auditory: SAME voice — content UNCHANGED
        Somatic: SAME sensations — content UNCHANGED
        Emotional: pain, anger, loss, betrayed — VALENCE SHIFTED
      }

    → Same memories. Same content. DIFFERENT evaluation.
    → "Looking at old photos and feeling pain" = content trigger → new valence fires → dissonance

  🟢 RESEARCH:
    → Evaluative conditioning: valence transfer through association (De Houwer 2007)
    → Fear conditioning: rapid valence assignment (LeDoux 1996)
    → Extinction ≠ erasure: old valence suppressed, not deleted (Bouton 2004)
    → Reconsolidation: valence CAN be modified during window (Nader 2000)
```

### §3.2 — Chunk-Miss (pattern absent)

```
⭐ CHUNK-MISS — COMPILED PATTERN NOT FIRED (ABSENT):

  DEFINITION:
    Body-base has compiled pattern X into baseline.
    Pattern X is not firing (absent, degraded, or quality reduced).
    VTA detects: actual < compiled baseline → negative prediction-delta.
    Body signal: "worse than expected."

  MECHANISM:
    ① Body compiles chunks at quality X (through repetition, experience)
    ② VTA habituates to pattern X → X = new baseline
    ③ Pattern X becomes absent or quality drops
    ④ VTA fires NEGATIVE prediction-delta (dopamine SUPPRESSED)
       → 🟢 Schultz 1997: reward < predicted → dopamine dip below baseline
    ⑤ Body signal: dissonance ("worse than expected")

  ⭐ BODY-BASE DOES NOT "REMEMBER" THE WAY PFC RECALLS:
    → Compiled baseline = Hebbian LTP that has wired the pattern
    → Pattern exists at BODY LEVEL (C+D zones)
    → PFC recall NOT required — compiled pattern FIRES AUTOMATICALLY on mismatch
    → Similar to: wearing soft clothing for years, then putting on stiff clothing →
      body signals IMMEDIATELY BEFORE PFC has time to "remember" the soft clothing

  4 VARIANTS:

    ⓐ CLEAR MISS — PFC knows what's missing:
       → Habitual TikTok → phone breaks → "want to watch TikTok but can't"
       → Soft clothing → stiff clothing → "this clothing is too stiff"
       → Good rice → cheap rice → "food doesn't taste as good today"
       → PFC HAS label: knows the source, knows what it wants

    ⓑ VAGUE MISS — delta accumulates, PFC doesn't detect:
       → Sitting at home watching movies for days → listlessness → "bored but don't know why"
       → Gradually insufficient movement → body restlessness → PFC confused
       → Delta each day too small → doesn't exceed PFC attention threshold
       → Connection: Boredom-Analysis.md core mechanism
       → PARTICULARLY DANGEROUS: accumulates silently → erupts when threshold crossed
       → ⭐ Self-Observation connection (Self-Observation.md §2):
         Prediction-delta exceeds threshold → Self-Observation triggered
         Vague miss accumulates → Self-Observation DELAYED (delta < threshold each day)
         = Micro-negative delta (sankhara-dukkha): Self-Observation Trigger Type ②

    ⓒ UNCONSCIOUS MISS — body knows, PFC doesn't:
       → Moved from countryside to city for work years ago → returning to countryside
         suddenly feels refreshing
       → "Don't know why I like hiking, going into the forest feels comfortable"
       → Body has compiled patterns (air, greenery, movement)
         at C+D level → PFC has NO verbal label
       → When pattern fires again → opioid → "comfortable without knowing why"
       → Personal preferences = compiled patterns per individual experience

    ⓓ IRRESOLVABLE MISS — hardware prevents resolution:
       → Normal miss (ⓐⓑⓒ): miss → adjust → resolve (seconds-days)
       → Irresolvable miss: hardware BLOCKS resolution
       → Parkinson-Analysis.md §5.2: PFC predicts "taking a step"
         → gate LOCKED → body CANNOT step → MISMATCH
         → Adjust → try harder → STILL fail → CANNOT resolve
       → = Chronic prediction-delta where EVERY attempt creates a new miss
       → Accumulation: frustration + helplessness + chronic elevated cortisol
       → UNIQUE: no other condition creates irresolvable miss as clearly as Parkinson
         (Addiction: execution OK. Depression: IF forced → may work. Parkinson: CAN'T.)
       → 🟡 Framework: irresolvable miss = new Chunk-Miss variant (from drill)

  MISS REWARD (opposite direction):
    → Reuniting: meeting an old friend → pattern fires again → opioid
    → Returning home: compiled nature patterns fire → reward
    → Recovery after illness: body patterns restored → relief + reward

  🟢 RESEARCH — SUCCESSIVE NEGATIVE CONTRAST (SNC):

    Crespi 1942, Flaherty 1996:
    → Setup: Group A eats 32% sucrose (good) for many meals → switch to 4% (average)
    → Control: Group B eats 4% sucrose from the start
    → Result: Group A after switch → eats LESS THAN even Group B
    → = Body doesn't just feel "slightly disappointed" — reacts MORE STRONGLY than neutral
    → = Compiled baseline violated → NEGATIVE signal actively fires

    → Amsel frustration theory: SNC = PRIMARY FRUSTRATION
      = aversive emotion triggered when expected-actual discrepancy occurs
    → = Chunk-Miss mechanism at ANIMAL level — PFC NOT required

    Schultz 1997 — neural mechanism:
    → Expected reward = X (compiled baseline)
    → Actual reward = Y
    → Y > X → dopamine INCREASES ("better than expected")
    → Y = X → dopamine NORMAL ("exactly as expected")
    → Y < X → dopamine SUPPRESSED ("worse than expected") ⭐
    → Dopamine suppression = ACTIVE SIGNAL: "worse than expected"

  BASELINE SHIFT DYNAMICS (details in §5):
    → 1 experience is not enough to strongly shift baseline
    → Many experiences → Hebbian wiring firms up → baseline shifts clearly
    → Miss after 1 time = mild. Miss after 100 times = strong.
    → Recovery possible: if lower quality sustained long enough → re-habituates
```

### §3.3 — Chunk-Gap (pattern never existed)

#### §3.3a — Core: Definition + Mechanism

```
⭐ CHUNK-GAP — NETWORK DETECTS SOMETHING MISSING THAT NEVER EXISTED:

  DEFINITION:
    Chunk network topology has HOLES or CONFLICTS.
    Pattern SHOULD exist (based on network structure) but DOESN'T.
    ACC/insula detects inconsistency → body signal "something is missing/contradictory."
    DIFFERS FROM Chunk-Miss: Miss = HAD IT, then lost. Gap = NEVER HAD IT.

  MECHANISM:
    ① Chunk network compiles through experience → network topology forms
    ② Network has internal structure (connections, patterns, expectations)
    ③ Structure predicts: "if A and B are true, then C must exist"
    ④ But C has NEVER been compiled → HOLE in network
    ⑤ ACC detects inconsistency → body signal "restless unease, something not right"
    ⑥ Signal drives behavior: search, explore, resolve → fill gap

  CHARACTERISTICS:
    ① PFC may or may NOT be able to articulate specifically what's missing
    ② Felt sense = body detecting gap BEFORE PFC verbal label
       (Somatic-Articulation-Loop.md: implicit → transitional → explicit)
    ③ Signal persistent — doesn't self-resolve (gap must be filled)
    ④ Filling gap → opioid reward (effort-proportional: 03-Reward.md §4.7)
    ⑤ ⭐ FOUNDATION FOR NOVELTY DRIVE
       Gap detected → restless unease → drive to explore/fill → discovery → opioid
    ⑥ ⭐ GAP HAS A SPECIFIC DIRECTION (Gap Direction):
       "Structure predicts C" → C has a SHAPE = f(surrounding chunks)
       → Gap direction = what SPECIFICALLY is predicted missing
       → Reward fires ONLY when fill MATCHES direction, not just "any gap fill"
       → "Don't know it exists = no gap" (no chunks → no boundary → no hole)
       → Details: Gap-Direction.md (4 properties, 2-layer model, unified Tier 1-4)

  GAP vs MISS:

    ┌───────────────────────────┬──────────────────────┐
    │ CHUNK-MISS                │ CHUNK-GAP            │
    ├───────────────────────────┼──────────────────────┤
    │ HAD IT → lost             │ NEVER HAD IT         │
    │ Body "remembers" baseline │ Network "predicts"   │
    │ Negative prediction error │ Inconsistency detect │
    │ VTA mechanism             │ ACC mechanism        │
    │ "Want back what was there"│ "Want what isn't yet"│
    │ Resolution = restore      │ Resolution = create  │
    │ E.g.: TikTok app breaks   │ E.g.: Einstein E=mc²  │
    └───────────────────────────┴──────────────────────┘

  EXAMPLES:

    Einstein:
      → Chunk network about physics: Newton + Maxwell + thought experiments
      → Network internal structure: "if both are true, there must be a unified framework"
      → Unified framework DOESN'T EXIST YET → GAP
      → Body signal: "restless unease, physics isn't coherent" → drives research
      → Fill gap (E=mc²) → extremely strong opioid burst (years of pending)

    This framework:
      → Chunk network about cognitive science being built
      → "Vaguely feel something's missing" → GAP (body detects before PFC articulates)
      → Drive to drill → fill gap → "ah, chunk dynamics classification!"
      → Insight = gap filled → opioid

    Chunk-Gap + CONFLICT (sub-type):
      → 2 patterns fire CONTRADICTORY → both cannot be true
      → GAP = no RESOLUTION between the 2 patterns
      → E.g.: cognitive dissonance (Festinger 1957)
      → E.g.: "Stay or go?" — 2 Imagine-Finals compete, gap = no resolution

  🟢 RESEARCH:
    → ACC error/conflict detection: Bush, Luu, Posner 2000
    → Cognitive dissonance: Festinger 1957
    → Curiosity as information gap: Loewenstein 1994 (information gap theory)
    → Aha moments and ACC: Kounios & Beeman 2009
    → Felt sense: Gendlin 1978 (body detects before verbal)
```

#### §3.3b — Gap → Novelty Drive Loop

```
⭐ GAP → NOVELTY DRIVE = PERPETUAL GAP-FILL CYCLE:

  ┌─────────────────────────────────────────┐
  │                                         │
  │  Gap detected (ACC/insula)              │
  │       ↓                                 │
  │  Body signal: "restless unease,         │
  │  something missing"                     │
  │       ↓                                 │
  │  Drive: explore, research, try          │
  │       ↓                                 │
  │  Fill gap (new chunks compile)          │
  │       ↓                                 │
  │  Opioid reward (effort-proportional)    │
  │       ↓                                 │
  │  VTA habituates → new baseline          │
  │       ↓                                 │
  │  Network detects NEW gap                │
  │       ↓                                 │
  │  [LOOP continues]                       │
  │                                         │
  │  = Novelty drive = perpetual gap-fill   │
  │  = "Curiosity" = body detecting gaps    │
  │  = Science = systematic gap-filling     │
  │  = Art = aesthetic gap-filling          │
  └─────────────────────────────────────────┘
```

#### §3.3c — Gap → Miss Transition

```
⭐ GAP CAN TRANSITION INTO CHUNK-MISS:

  Pure Chunk-Gap: ACC detects "missing" → body restlessness → drives searching.
  BUT Gap can TRANSITION into Chunk-Miss through the following mechanism:


  ① CORE MECHANISM — Imagine-Final preview compiles into baseline:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  Gap detected (ACC) → PFC builds Imagine-Final preview      │
  │    ↓                                                        │
  │  Imagine-Final stabilizes + repeats many times             │
  │    ↓                                                        │
  │  Body compiles preview into expectation baseline            │
  │  (§5 Quality Baseline Shift: repeated preview = new normal) │
  │    ↓                                                        │
  │  Body now EXPECTS something that never-existed             │
  │    ↓                                                        │
  │  Reality STILL doesn't have it → VTA: actual < baseline    │
  │    ↓                                                        │
  │  = Chunk-Gap (ACC, vague) → Chunk-Miss (VTA, specific)    │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

    Condition: Imagine-Final must be STABLE (unchanged) + REPEATED enough.
    If Imagine-Final CHANGES → gap also changes → body fires NEW pattern → different path.


  ② WHY PREVIEW REPEATS — Cortisol holding signal:

    Gap persists + unresolved → cortisol fires "still need change"
    (Cortisol-Baseline.md §3.8: holding signal keeps imagination loop active)
    → PFC is FORCED to return to Imagine-Final → preview repeats INVOLUNTARILY
    → Compile baseline FASTER than voluntary preview
    → = "Can't stop thinking about it" = cortisol holding loop
    → = Cortisol = ACCELERATOR for Gap→Miss transition


  ③ DIRECTION TAG — Same transition, DIFFERENT outcome:

    Cortisol direction (Cortisol-Baseline.md §3.5) determines QUALITY:

    Gap + Novelty cortisol (curiosity body state):
      → Baseline compiles with opioid tag
      → Miss = "want it + don't have it yet" → DRIVE to seek → productive
      → = "Excited expectation"

    Gap + Threat cortisol (anxiety body state):
      → Baseline compiles with cortisol tag
      → Miss = "afraid + don't have it" → ANXIETY loop → destructive
      → = "Anxious expectation"

    → Same Gap→Miss mechanism, DIFFERENT direction → COMPLETELY DIFFERENT outcome


  ④ APPLICATION — "The higher the expectation, the greater the disappointment":

    This folk wisdom = Gap→Miss transition:

      Preview VIVID + repeated MANY times + Imagine-Final STABLE
        → Body compiles HIGH baseline
          → Reality < baseline → Chunk-Miss delta LARGE → "great disappointment"

      Preview LOW or NO preview
        → Low baseline → Reality ≥ baseline → "comfortably surprised"

    EXAMPLES:
      → Child sees friend being hugged by their mother → PFC preview "if I were hugged"
        → Preview repeats → baseline shifts → lacking = specific Chunk-Miss
        → Started as Gap (vague) → becomes Miss (clear, painful)

      → Showroom car: preview "having the car" repeats for months
        → Body compiles into expectation → not having it = Miss
        → Different from "didn't know the car existed" (pure Gap)


  ⑤ WHEN TRANSITION DOESN'T HAPPEN:

    If Imagine-Final UPDATES CLOSELY WITH REALITY → baseline tracks reality
    → Small delta → does NOT become strong Miss.

    Imagine-Final updates when:
      → Domain feedback loop: ACTION → receive feedback → update
      → Background processing: sufficient sleep + cortisol not too high
      → Related chunks large enough: raw material for background processing

    Most people: stable chunks → stable Imagine-Final → preview repeats
    → transition is nearly guaranteed when gap persists.
```

#### §3.3d — Gap Decomposition (Mini-Arc Dynamics)

```
⭐ GAP DECOMPOSITION — MINI-ARC DYNAMICS:

  Big Gap exists for YEARS (e.g., Einstein unified physics).
  Body CANNOT sustain constant Gap signal without reward.
  → IF gap doesn't decompose → burnout / giving up OR Gap→Miss transition.

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  BIG GAP: "unified physics framework"                       │
  │    ↓                                                        │
  │  Decompose into MINI GAPS (naturally or PFC-directed):     │
  │    → Mini gap 1: photoelectric effect → FILL → mini opioid  │
  │    → Mini gap 2: Brownian motion → FILL → mini opioid       │
  │    → Mini gap 3: special relativity → FILL → bigger opioid  │
  │    → BIG GAP FILL: E=mc² → compound opioid burst           │
  │                                                             │
  │  Each mini fill:                                            │
  │    → Opioid reward (effort-proportional: 03-Reward.md §4.7) │
  │    → VTA resets → detects NEXT mini gap → sustains drive    │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  Applications:
    → PhD: big gap "thesis" → mini gaps (chapters, experiments)
    → Game design: "win game" → mini gaps (levels, quests)
    → Education: "understand physics" → mini gaps (exercises, lab)
    → Startup: "build product" → mini gaps (sprints, milestones)

  Gap that doesn't decompose → persists → CAN transition to Miss (§3.3c).
  Gap that decomposes well → sustained drive + regular reward.
  = Drive-PFC-Strategic (Drive.md §2): plan decomposition.

  🟢 RESEARCH:
    → Goal gradient effect: Hull 1932 (effort increases near goal = mini-arc)
    → Progress principle: Amabile & Kramer 2011
      (small wins = most powerful motivator in creative work)
```

---

## §4 — COMPOUND MECHANISM

```
⭐ COMPOUND — MULTIPLE DYNAMICS FIRE SIMULTANEOUSLY:

  PRINCIPLE:
    3 chunk dynamics are NOT mutually exclusive.
    1 event can trigger 2-3 dynamics at once.
    Each dynamic added = another "flavor" of body-feedback.
    = Why dissonance/reward HAS SO MANY SHADES.


  EXAMPLE ANALYSIS — LOSING 100K:

  ┌──────────────────────┬──────────────────┬──────────────────┬──────────────────┐
  │ Event                │ Chunk-Shift      │ Chunk-Miss       │ Chunk-Gap        │
  ├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
  │ Dropped it (lost)    │                  │ ✅ resource       │                  │
  │                      │                  │ decreases        │                  │
  │ Subjective:          │                  │ "regret"         │                  │
  ├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
  │ Scammed (lost)       │ ✅ trust          │ ✅ resource       │                  │
  │                      │ shifts           │ decreases        │                  │
  │ Subjective:          │ "anger"          │ "regret"         │                  │
  ├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
  │ Scammed by close     │ ✅ trust          │ ✅ resource       │ ✅ identity gap:  │
  │ friend (lost)        │ FLIPS hard       │ decreases        │ "who am I that   │
  │                      │ + connection     │                  │ my close friend  │
  │                      │ damaged          │                  │ would betray me?"│
  │ Subjective:          │ "anger + pain"   │ "regret"         │ "bitterness"     │
  └──────────────────────┴──────────────────┴──────────────────┴──────────────────┘

  → Same 100k loss. 1 dynamic → 2 → 3 = more complex, more painful, longer to resolve.


  EXAMPLE ANALYSIS — SISTER-A / SISTER-B:

    Sister-A feeling smooth, chatting comfortably
    → Sister-B brags about her child's achievement (sensory input: auditory)
    → Spreading activation: chunks about MY OWN CHILD fire
    → Chunk dynamics:
      Chunk-Gap: my child vs Sister-B's child → gap "my child hasn't achieved this yet"
      Chunk-Shift (mild): valence of the meeting shifts from pleasant → heart twinge
    → Compound: Gap + Shift → "heart twinge, goes quiet"
    → NOTE: body-input did NOT change — only internal chunk fires changed


  EXAMPLE COMPOUND REWARD — EINSTEIN BREAKTHROUGH:

    Fill Chunk-Gap: E=mc² resolves physics contradiction → gap filled → STRONG opioid
    Chunk-Shift: self-schema shifts ("I = the one who solved this") → positive
    Chunk-Miss (reverse): years of "lacking the solution" → IT'S HERE → relief + reward
    → Compound 3 dynamics → extreme euphoria


  ⭐ COMPOUND PRINCIPLE:

    Signal_total = Σ (dynamics_i × intensity_i × network_size_i)

    → More dynamics = STRONGER total signal
    → Larger network_size = further propagation = affects more chunks = STRONGER
    → Intensity of each dynamic depends on delta magnitude
    → = Why "close friend betrayal" > "stranger scam" > "accidentally dropped"
      (same loss, different compound level)


  🟡 CONDITIONAL INTERACTION MODEL (Reward-Signal-Architecture.md §6):

    ⚠️ COMPOUND ≠ ADDITIVE.
    The Σ formula above = APPROXIMATION. In practice: CONDITIONAL.

    Reward compound NOT simply A + B. 4 VARIABLES determine interaction:

    ① Substrate Overlap:
       → Same receptor system (opioid + opioid) → SUPERADDITIVE
       → Different systems (opioid + endocannabinoid) → ADDITIVE
       → Competing (opioid + cortisol) → SUBTRACTIVE

    ② A Gate Direction (Reward-Signal-Architecture.md §3):
       → A evaluates → AMPLIFY B → superadditive
       → A evaluates → SUPPRESS B → subtractive
       → A absent → B RAW (no evaluation)

    ③ Relief Presence:
       → If threat pending resolved → cortisol DROP = MULTIPLIER
       → If no threat → opioid only, no relief bonus
       → Relief + reward = STRONGEST compound (Archimedes "Eureka!")

    ④ Temporal Overlap:
       → Simultaneous → compound (most powerful)
       → Sequential (seconds) → cascade (moderate)
       → Sequential (hours+) → independent (no compound)

    → Diagnostic: unexpected compound emotion = check 4 variables
    → Details: Reward-Signal-Architecture.md §6 (Conditional Interaction Model)
```

---

## §5 — QUALITY BASELINE SHIFT

```
⭐ QUALITY BASELINE SHIFT — MECHANISM CONNECTING SENSORY-DRIVEN WITH CHUNK-MISS:

  DEFINITION:
    Body compiles chunks at quality X through repeated experience.
    VTA habituates → X = new baseline.
    Quality increases to Z > X → positive prediction-delta → reward.
    Quality decreases to Y < X → negative prediction-delta → dissonance (Chunk-Miss).
    = Baseline "drifts" with experience.


  4-STEP MECHANISM:

    ① COMPILE:
       Repeated experience at quality X → Hebbian LTP → neurons wire pattern
       → Pattern compiled into C+D zones (subcortical + peripheral)
       → PFC NOT required to maintain (body-level compile)

    ② HABITUATE:
       VTA habituates to pattern X → X = "normal" → doesn't fire
       → Like a thermostat set at 25°C: no signal when exactly 25°C

    ③ DETECT DELTA:
       Actual quality changes:
       → Actual > baseline → positive prediction-delta → reward
       → Actual < baseline → negative prediction-delta → Chunk-Miss
       → Actual = baseline → no signal → neutral

    ④ RE-HABITUATE:
       If new quality sustained long enough → baseline SHIFTS:
       → New lower quality sustained → body re-habituates → baseline drops
       → New higher quality sustained → body re-habituates → baseline rises
       → = Hedonic adaptation (🟢 Brickman 1978)


  TIMELINE + COMPILE STRENGTH:

    ┌──────────────────────────────────────────────────────────────┐
    │                                                              │
    │  1 experience (high quality):                                │
    │    → Proto-chunk weak → MILD baseline shift                  │
    │    → PFC has Imagine-Final preview                           │
    │    → Body-base NOT yet clearly shifted                       │
    │    → If quality drops → PFC "let down" > body-base dissonance│
    │                                                              │
    │  A few times (3-10):                                         │
    │    → Chunk strengthening → baseline starting to shift        │
    │    → SNC effect appears (Crespi: rats downshift)             │
    │    → Body-base dissonance CLEAR when quality drops           │
    │                                                              │
    │  Many times (50-100+):                                       │
    │    → Chunk fully compiled → baseline FIRMLY SHIFTED          │
    │    → Quality drop = STRONG dissonance (SNC effect maximum)   │
    │    → Re-habituating downward is slow (strong compile = slow  │
    │      decay)                                                  │
    │                                                              │
    │  → compile_rate ≈ f(repetition × saliency × peak_valence    │
    │                     × multi_modal × contingency)             │
    │  → Chunk.md v2.2 §2.2: same 5-parameter formula             │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘


  ANIMALS HAVE BASELINE SHIFT:

    🟢 Crespi 1942 / Flaherty 1996 (SNC in rats):
    → Rats trained on high reward → downshift → WORSE than control
    → = Compiled baseline + negative prediction-delta
    → = Chunk-Miss mechanism at animal level
    → PFC NOT required — mechanism at body-base level

    Dog accustomed to good food → rejects cheap food:
    → Baseline shift: high quality = new normal
    → Cheap food = Chunk-Miss → body signal refuses
    → Retraining: sustained lower quality → re-habituates → accepts
    → = Same mechanism as rat SNC


  IMPORTANT PROPERTIES:

    ① BIDIRECTIONAL: baseline shifts UP and DOWN
    ② ASYMMETRIC: shifting UP easier than shifting DOWN
       → 🟢 Loss aversion (Kahneman & Tversky 1979): losing hurts ~2x gaining
       → Body resists quality decrease MORE STRONGLY than accepting quality increase
    ③ DOMAIN-SPECIFIC: baseline shifts INDEPENDENTLY per domain
       → Food baseline and clothing baseline shift SEPARATELY
       → Can be accustomed to good food but not to nice clothing yet
    ④ INDIVIDUAL: each person's baseline DIFFERS because experience DIFFERS
       → Same quality → Person A: "normal," Person B: "good"
       → = Per-person reward (03-Reward.md §5.9)
```

---

## §6 — MAP TO FRAMEWORK

### §6.1 — v7.8 Cycle Architecture

```
🟡 CHUNK DYNAMICS IN V7.8 PERCEPTION-ACTION CYCLE:

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  ① DOMAIN → BODY-INPUT (L0 + L1 receptors)                    │
  │     → SENSORY-DRIVEN input enters here                        │
  │                                                                │
  │  ② BODY-INPUT → UNCONSCIOUS (B + C + D zones)                 │
  │     → Chunks match against input                               │
  │     → PATTERN-DRIVEN input originates here (replay, preview)   │
  │                                                                │
  │     ⭐ CHUNK DYNAMICS FIRE HERE:                                │
  │     → Chunk-Shift: valence re-evaluated based on new info      │
  │     → Chunk-Miss: compiled baseline vs actual → delta          │
  │     → Chunk-Gap: network topology → inconsistency detected     │
  │     → Compound: multiple dynamics simultaneous                 │
  │                                                                │
  │  ③ UNCONSCIOUS → FEELING (integrated signal emerges)           │
  │     → Body-feedback signal (direction + magnitude)             │
  │     → Chunk dynamics determine QUALITY of signal               │
  │                                                                │
  │  ④ FEELING → PFC (observe, label, choose)                      │
  │     → PFC observes signal but may NOT know which dynamic       │
  │     → "Heart twinge" = PFC label for Chunk-Gap + Chunk-Shift  │
  │                                                                │
  │  ⑤ PFC → BODY-OUTPUT → DOMAIN → LOOP                          │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘


  ZONE MAP:

    D (Peripheral, PFC near-zero reach):
      → Sensory-driven input primary pathway
      → Chunk-Miss: gut baseline shift, cardiac patterns
      → Baseline shift compiled HERE → body signal WITHOUT PFC

    C (Subcortical, PFC limited reach):
      → Amygdala: Chunk-Shift (fear conditioning, valence flip)
      → VTA: Chunk-Miss detection (prediction-delta)
      → ACC: Chunk-Gap detection (inconsistency)
      → Hippocampus: Pattern-driven input (replay, preplay)

    B (Cortical, PFC trainable):
      → Complex chunk networks → all 3 dynamics
      → Chunk-Gap rich here (knowledge gaps, skill gaps)
      → Cortical modality areas hold compiled baselines

    A (PFC):
      → OBSERVE chunk dynamics output (feeling layer)
      → CAN bias: hold chunks → influence which dynamics fire
      → CANNOT directly cause dynamics (dynamics emerge from B+C+D)
      → PFC role: observe, label, choose response, orchestrate
```

### §6.2 — Body-Feedback-Preconditions

```
🟡 CHUNK DYNAMICS × 5 BODY-FEEDBACK-PRECONDITIONS:

  Body-Feedback-Precondition: Signal fires when ALL 5 preconditions met.
  Chunk dynamics DESCRIBE HOW signal arises — Body-Feedback-Precondition describes WHEN.

  ┌────────────────────────────────┬─────────────┬─────────────┬─────────────┐
  │ Body-Feedback-Precondition     │ Chunk-Shift │ Chunk-Miss  │ Chunk-Gap   │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-1 Directed-Gap    │ Shift       │ Miss = body │ Gap = body  │
  │ (body-need gap)                │ creates NEW │ -need lost  │ -need       │
  │                                │ pending     │ quality     │ lacking     │
  │                                │ (betrayal → │             │ pattern     │
  │                                │ need fix)   │             │             │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-2 Chunk-Substrate │ Needs       │ Needs       │ Needs enough│
  │ (sufficient substrate)         │ chunks to   │ compiled    │ network to  │
  │                                │ evaluate    │ baseline    │ DETECT gap  │
  │                                │ new info    │ (no compile │             │
  │                                │             │ = no miss)  │             │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-3 Delta-Gate      │ Shift =     │ Miss = neg. │ Gap detect  │
  │ (sufficient change)            │ valence     │ prediction  │ = ACC       │
  │                                │ delta       │ error       │ signal      │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-4 Match-Range     │ Shift occurs│ N/A (body   │ Gap must be │
  │ (dynamic zone)                 │ at ANY      │ already     │ detectable  │
  │                                │ match level │ knows)      │ (not too    │
  │                                │             │             │ alien)      │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-5 Compile-Gate    │ NEW valence │ Compiled    │ Compiled    │
  │ (Direction-At-Compile)         │ tag from    │ baseline    │ surrounding │
  │                                │ shift event │ carries tag │ chunks tag  │
  └────────────────────────────────┴─────────────┴─────────────┴─────────────┘

  INSIGHTS:
  → Chunk-Miss does NOT need Precondition-4 (Match-Range) — body already has baseline
  → Chunk-Gap NEEDS Precondition-2 (enough network to detect gap)
  → Chunk-Shift NEEDS Precondition-3 (delta large enough to register)
  → Compound = Precondition-1–Precondition-5 checked MULTIPLE TIMES per dynamic
```

---

## §7 — RESEARCH ANCHORS

```
🟢 HIGH CONFIDENCE (each component well-established):

  CHUNK-MISS MECHANISM:
    🟢 Successive Negative Contrast: Crespi 1942, Flaherty 1996
    🟢 Reward prediction error: Schultz, Dayan, Montague 1997
    🟢 Frustration theory: Amsel 1958, 1992
    🟢 Wanting vs liking: Berridge & Robinson 1998, 2003
    🟢 Loss aversion ~2x: Kahneman & Tversky 1979
    🟢 Hedonic adaptation: Brickman, Coates, Janoff-Bulman 1978

  CHUNK-SHIFT MECHANISM:
    🟢 Fear conditioning: LeDoux 1996
    🟢 Evaluative conditioning: De Houwer 2007
    🟢 Extinction ≠ erasure: Bouton 2004
    🟢 Memory reconsolidation: Nader, Schafe, LeDoux 2000
    🟢 Spreading activation: Collins & Loftus 1975

  CHUNK-GAP MECHANISM:
    🟢 ACC error/conflict detection: Bush, Luu, Posner 2000
    🟢 Cognitive dissonance: Festinger 1957
    🟢 Information gap theory (curiosity): Loewenstein 1994
    🟢 Aha moment + ACC: Kounios & Beeman 2009
    🟢 Felt sense: Gendlin 1978

  INPUT SOURCES:
    🟢 Sensory processing: established neuroscience
    🟢 Hippocampal replay: Wilson & McNaughton 1994
    🟢 Hippocampal preplay: Pfeiffer & Foster 2013
    🟢 Social comparison: Festinger 1954

  GAP DYNAMICS:
    🟢 Goal gradient effect: Hull 1932
    🟢 Progress principle: Amabile & Kramer 2011


🟡 FRAMEWORK SYNTHESIS (novel integration):

  🟡 2-source classification (Sensory-Driven / Pattern-Driven):
     Components established. Classification = framework contribution.

  🟡 3-dynamic classification (Shift / Miss / Gap):
     Each mechanism established individually.
     Unified taxonomy as ORTHOGONAL chunk dynamics = framework contribution.

  🟡 Compound mechanism:
     Multi-signal co-occurrence recognized in affect research.
     Formalization via chunk dynamics = framework contribution.

  🟡 Quality Baseline Shift as bridge (Sensory → Miss):
     SNC + hedonic adaptation established.
     Framing as chunk compile mechanism = framework contribution.

  🟡 Gap → Novelty drive foundation:
     Curiosity research established (Loewenstein).
     Formalization via chunk network topology = framework contribution.

  🟡 Gap → Miss transition via Imagine-Final preview:
     Hedonic adaptation + preview compile established individually.
     Transition mechanism = framework contribution.

  🟡 Gap decomposition / mini-arc dynamics:
     Goal gradient (Hull 1932) + progress principle (Amabile 2011) established.
     Formalization as gap decomposition = framework contribution.

  🟡 3+1 Chunk-Miss variants (clear / vague / unconscious / irresolvable):
     Each observable. Taxonomy = framework contribution.
     v1.3→v2.0: ⓓ irresolvable = hardware prevents resolution (Parkinson drill).

  🟡 Context-free chunk as Pattern-Driven variant:
     PTSD drill: flashback = ⓕ context-free chunk fires internally.
     Consistent Brewin 2010 DRT + Chunk.md §2.6 context-tag model.

  🟡 v2.0 NEW — Body-Need as aggregate output:
     Body-need concept established in motivation research.
     Framing as aggregate of 2-source × 3-dynamics = framework contribution.

  🟡 v2.0 NEW — Complexity Spectrum (Simple → Social → Meta):
     Each substrate level observable. Unified taxonomy = framework contribution.
     Meta-level collapse: meta = same dynamics, different substrate.

  🟡 v2.0 NEW — Cross-cutting clarification:
     Observation parameters + state modifiers ≠ sources.
     Conceptual clarification = framework contribution.


🔴 SPECULATIVE:

  🔴 Exact compound signal summation formula
  🔴 Precise timeline for baseline shift (1 vs 10 vs 100 exposures)
  🔴 ACC as primary Gap detector (vs other conflict detection circuits)
  🔴 Chunk-Miss variant boundaries (clear threshold between clear/vague/unconscious)
  🔴 Gap → Miss transition: exact preview repetition count for baseline shift
  🔴 Gap decomposition: optimal mini-gap size for sustained drive
```

---

## §8 — HONEST ASSESSMENT

```
STRENGTHS:
  ✅ Matches v7.8 chunk-centric principle
  ✅ Each dynamic grounded in established research
  ✅ Explains phenomena the current framework describes but doesn't MECHANIZE:
     → Compound dissonance (100k example)
     → Social dissonance without body-input change (Sister-A/Sister-B)
     → Animal body-feedback (SNC without PFC)
     → Felt sense gap detection (Gendlin, before PFC verbal)
  ✅ Provides foundation for Novelty drive (Chunk-Gap loop)
  ✅ Orthogonal to existing 3 axes — COMPLEMENTS, does NOT REPLACE
  ✅ v2.0: Body-Need aggregate framing connects dynamics → behavior
  ✅ v2.0: Complexity Spectrum shows parsimony (3 dynamics → all levels)

LIMITATIONS:
  ⚠ 3 dynamics boundary: some cases COULD be classified differently
     → Betrayal: is it Shift (valence change) or Gap (trust resolution gap)?
     → Answer: COMPOUND — both fire. Boundary is soft.
  ⚠ Exact neural pathways for each dynamic not fully mapped
  ⚠ Compound summation is conceptual, not quantified
  ⚠ Baseline shift timeline lacks precise dose-response data
  ⚠ Body-Need aggregate concept = framework synthesis, not independently tested
  ⚠ Complexity Spectrum levels (Simple/Social/Meta) = useful heuristic,
     not sharp categories — actual substrate is continuous

WHAT THIS FILE DOES NOT DO:
  ✗ Replace intensity classification (02-Dissonance.md)
  ✗ Replace source classification (02-Dissonance.md §3)
  ✗ Replace Body-Feedback-Preconditions (Body-Feedback.md §5)
  ✗ Replace case analyses (01-04 files)
  ✗ Replace inter-body mechanism (Inter-Body-Mechanism.md)
  → This file ADDS a classification axis + aggregate framing, removes nothing
```

---

## §9 — CROSS-REFERENCES

```
📚 INTER-BODY MECHANISM (v2.0 NEW):
  → Inter-Body-Mechanism.md v1.0 — Body-Need §2, 3-cost §4, 5-channel §6
    → §2 Body-Need aggregate: full 7 properties + 4 immediacy types
    → §2.3 Cross-cutting: observation parameters + state modifiers ≠ sources
    → §2.2 Complexity spectrum: Simple→Social→Meta
    → §4 3-cost model: PFC draft + suppress + uncertainty
    → §6 5-channel input vector: trigger = vector, not single source

📚 REWARD ARCHITECTURE:
  → Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State dimension, 5 Profiles, Interaction Model
    → §2 Evaluative/Direct-State maps to: Sensory-Driven ≈ Direct-State, Pattern-Driven ≈ Evaluative
    → §3 Evaluative Gates Direct-State = evaluation modulates body-state
    → §6 Conditional Interaction Model = replaces simple additive compound

📚 WITHIN BODY-FEEDBACK FOLDER:
  → Body-Feedback.md v1.1 — §2 dual-pull, §5 5 Body-Feedback-Preconditions
  → Body-Feedback-Label.md v2.0 — 3-tier vocabulary reference
  → 01-Foundation.md §3 — 6-step interface loop
  → 01-Foundation.md §5 — body-feedback vs feeling 7-layer
  → 02-Dissonance.md §2 — 5 mini dissonance cases (per dynamics relabel)
  → 02-Dissonance.md §3 — 3 Genuine Discomfort Sources
  → 02-Dissonance.md §8 — trauma loop (compound Shift + Miss + Gap)
  → 02-Dissonance.md §9 — hedonic trap (Chunk-Miss from schema decay)
  → 03-Reward.md §2 — VTA 7-step loop
  → 03-Reward.md §4 — 7 reward cases (per dynamics relabel)
  → 03-Reward.md §5 — Car paradox (per-person Chunk-Miss/Gap)
  → 04-Integration.md §6-8 — Einstein/hedonic/trauma walkthroughs

📚 HEALTH CONDITIONS (v1.3 preserved):
  → PTSD-Analysis.md v1.0 §4 — flashback = context-free chunk fire (→ §2.3 ⓕ)
  → Parkinson-Analysis.md v1.1 §5.2 — chronic irresolvable prediction-delta (→ §3.2 ⓓ)
  → Chunk.md v2.2 §2.6 — context-tag model (4 metadata types, 2 chunk types)

📚 CHUNK SYSTEM:
  → Chunk.md v2.2 §1-§4 — substrate, compile, connections, activation
  → Chunk-Activation-Dynamics.md §2 — probability distribution
  → Chunk-Activation-Dynamics.md §3 — competitive re-linking (Shift mechanism)
  → Chunk-Activation-Dynamics.md §4 — trigger surface

📚 VALENCE + FEELING:
  → Valence-Propagation.md v1.4 — valence per-entity + chain propagation
  → Feeling.md v2.0 — PFC observation of body-feedback (output of dynamics)
  → Somatic-Articulation-Loop.md — felt sense = Gap detection pre-verbal
  → Self-Observation.md v1.0 — APPLICATION-3: prediction-delta → Self-Observation trigger (§2)
    → Vague miss ⓑ = Self-Observation Trigger Type ② (micro-negative, sankhara-dukkha)
    → §3.2 Chunk-Miss → Self-Observation delay when delta accumulates silently

📚 GAP + DIRECTION:
  → Gap-Direction.md v1.1 — gap has direction = f(surrounding chunks)
    → 4 properties, 2-layer model, unified Tier 1-4
    → "Don't know it exists = no gap" principle
  → Cortisol-Baseline.md v2.0 §3.5 — chunk association tag (Shift mechanism)
  → Cortisol-Baseline.md v2.0 §3.8 — holding signal (Gap→Miss accelerator)

📚 OTHER FRAMEWORK:
  → Core-Software.md §1 — perception-action cycle
  → Core-Software.md §4 — unconscious processing (where dynamics fire)
  → Observation/Boredom.md — Vague Chunk-Miss variant ⓑ + 2-direction formula
  → Observation/Novelty.md — Chunk-Gap = foundation mechanism
  → Observation/Connection.md §1.3 — 4 Cases mapped to chunk dynamics
     (Enough=Chunk-Miss, Loss=Chunk-Miss++, Lacking=Chunk-Gap, Toxic=Chunk-Shift)
  → PFC/Imagination/Imagination.md — preview = Pattern-Driven source
  → PFC/PFC-Operations.md v1.3 §9.3 — 2-Mode Engagement: body-feedback operates
     PARALLEL (dominant in Mode 1/Flow), PFC adds cognitive channel in Mode 2

📚 KEY RESEARCH (30+ citations):
  🟢 Amabile & Kramer 2011 — progress principle
  🟢 Amsel 1958, 1992 — frustration theory
  🟢 Berridge & Robinson 1998, 2003 — wanting vs liking
  🟢 Bouton 2004 — extinction ≠ erasure
  🟢 Brewin 2010 — Dual Representation Theory (S-rep/C-rep)
  🟢 Brickman et al. 1978 — hedonic adaptation
  🟢 Bush, Luu, Posner 2000 — ACC conflict detection
  🟢 Collins & Loftus 1975 — spreading activation
  🟢 Crespi 1942, 1944 — successive contrast
  🟢 De Houwer 2007 — evaluative conditioning
  🟢 Festinger 1954 — social comparison
  🟢 Festinger 1957 — cognitive dissonance
  🟢 Flaherty 1996 — consummatory successive contrast
  🟢 Gendlin 1978 — focusing, felt sense
  🟢 Hull 1932 — goal gradient effect
  🟢 Kahneman & Tversky 1979 — loss aversion
  🟢 Kounios & Beeman 2009 — aha moments, ACC
  🟢 LeDoux 1996 — fear conditioning, low road
  🟢 Loewenstein 1994 — information gap theory of curiosity
  🟢 Nader, Schafe, LeDoux 2000 — reconsolidation
  🟢 Pfeiffer & Foster 2013 — hippocampal preplay
  🟢 Schultz, Dayan, Montague 1997 — reward prediction error
  🟢 Walker 2017 — sleep consolidation
  🟢 Wilson & McNaughton 1994 — hippocampal replay
```

---

> **END OF Body-Feedback-Mechanism.md v2.1 (English)**
>
> **CHANGELOG v1.3 → v2.0:**
>   ✅ NEW §1: Body-Need aggregate output (definition, 2 sources, cross-cutting,
>      7 properties, 4 immediacy). Bridges "dynamics fire" → "what body needs."
>   ✅ NEW §2.5: Complexity Spectrum (Simple→Social→Meta) + Meta-level collapse.
>      3 dynamics explain ALL substrate levels → parsimony.
>   ✅ §1.3: Cross-cutting clarification (observation parameters + state modifiers ≠ sources).
>   ✅ §3.3 restructured: sub-sections (core/novelty/transition/decomposition).
>   ✅ §6: Merged v7.8 map + Body-Feedback-Precondition map into single section.
>   ✅ §8-§9: Updated assessment + cross-refs for new content + Inter-Body ref.
>   ✅ All v1.3 content preserved: 2-source, 3 dynamics, compound, baseline shift,
>      context-free chunk ⓕ, irresolvable miss ⓓ, ALL 30+ research citations.
>
> **Summary:** Core mechanism reference for body-feedback chunk dynamics:
>   §1: Body-Need = aggregate output (NEW v2.0)
>   §2: 2 input sources + Complexity Spectrum (NEW v2.0)
>   §3: 3 chunk dynamics (restructured Gap sub-sections)
>   §4: Compound mechanism (Conditional Interaction Model)
>   §5: Quality Baseline Shift (SNC bridge)
>   §6: Framework maps (v7.8 + Body-Feedback-Precondition)
>   §7-§9: Research + Assessment + Cross-refs
>
> **Axis 4**: orthogonal to existing 3 axes (direction, magnitude, source).
> **Foundation**: Chunk-Gap = Novelty drive mechanism.
> **Key research**: SNC (Crespi 1942) proves Chunk-Miss at animal level.
> **v2.0 core additions**: Body-Need aggregate + Complexity Spectrum +
>   Cross-cutting clarification. All 3 derive from Inter-Body drill insights.
>
> **Version:** v2.1, 2026-05-25.
