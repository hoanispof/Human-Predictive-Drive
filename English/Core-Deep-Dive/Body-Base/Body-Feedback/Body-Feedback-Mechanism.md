---
title: Body-Feedback Mechanism — Chunk Dynamics Classification
version: 2.1
status: REFERENCE v2.1
scope: |
  CORE MECHANISM FILE: HOW body-feedback arises from chunk dynamics.
  NEW v2.0: Body-need aggregate framing + Complexity Spectrum.
  2 input sources (Sensory-Driven / Pattern-Driven).
  3 chunk dynamics (Chunk-Shift / Chunk-Miss / Chunk-Gap).
  Compound mechanism. Quality Baseline Shift.
  Research anchors: Crespi 1942, Schultz 1997, Berridge 2003, Amsel, Flaherty 1996.
purpose: |
  Existing files classify body-feedback by INTENSITY (02-Dissonance.md, 14 levels),
  SOURCE (02-Dissonance.md §3, 3 Genuine Discomfort Sources), and PRECONDITION (5 Body-Feedback-Preconditions).
  This file adds a 4th axis: CHUNK MECHANISM — HOW chunks fire to produce signal.
  This axis matches the v7.8 "chunk-centric" principle: everything runs on chunks,
  classification must be chunk-based.
  v2.0 NEW: Body-need aggregate concept — chunk dynamics = mechanism,
  body-need = aggregate OUTPUT. Complexity Spectrum (Simple→Social→Meta)
  shows SAME mechanism, DIFFERENT substrate level.
dependencies:
  - Chunk.md v2.2 — chunk substrate, context-tag model
  - Chunk-Activation-Dynamics.md — probability, re-linking, trigger surface
  - Valence-Propagation.md v1.4 — valence per-entity + chain propagation
  - Body-Feedback.md v1.1 — Body-Feedback-Precondition, dual-pull, interface loop
  - Body-Feedback-Precondition.md v1.0 — 5 preconditions formal definitions (§6.2 mapping)
  - Body-Feedback-Label.md v2.0 — vocabulary reference (3-tier labels)
  - 02-Dissonance.md — intensity levels, source taxonomy, case analyses
  - Core-v7.8-Draft.md — cycle architecture, A/B/C/D zones
  - Cortisol-Baseline.md v2.0 — amplifier, holding signal
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles
  - Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State Dissonance, Mismatch Splitting, Evaluative Gates
  - Inter-Body-Mechanism.md v1.0 — Body-need aggregate, 3-cost, 5-channel
  - Gap-Direction.md v1.1 — gap has direction = f(surrounding chunks)
source_version: Vietnamese v2.1 (REFERENCE v2.1)
english_created: 2026-06-05
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Mechanism — Chunk Dynamics Classification

> **Same event: "losing $100."**
> Accidentally dropped it → regret. Scammed → regret + anger. Scammed by a close friend → regret + anger + bitterness.
>
> Same monetary loss. But chunk patterns fire DIFFERENTLY.
> Each additional chunk layer adds another "flavor" of dissonance.
>
> Body-feedback is not just direction (reward/dissonance) and magnitude (mild→extreme).
> Body-feedback also has **chunk dynamics** — HOW chunks fire to produce the signal.
>
> These signals AGGREGATE into **body-need** — the current state the body is demanding be met.
> Body-need = aggregate output of chunk dynamics.
>
> This file formalizes that classification axis + the body-need aggregate framing.

---

## Table of Contents

- §0 — THESIS + POSITION IN FRAMEWORK
- §1 — BODY-NEED: AGGREGATE OUTPUT
- §2 — 2 INPUT SOURCES (Sensory-Driven / Pattern-Driven)
- §3 — 3 CHUNK DYNAMICS (Chunk-Shift / Chunk-Miss / Chunk-Gap)
- §4 — COMPOUND MECHANISM
- §5 — QUALITY BASELINE SHIFT
- §6 — FRAMEWORK MAP (v7.8 Cycle + Body-Feedback-Precondition)
- §7 — RESEARCH ANCHORS
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES

---

## §0 — THESIS + POSITION IN FRAMEWORK

```
⭐ 4 CLASSIFICATION AXES FOR BODY-FEEDBACK:

  Body-feedback signal has 4 ORTHOGONAL classification axes:

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
  │  AXIS 4 — CHUNK DYNAMICS (chunk mechanism) ← THIS FILE          │
  │    HOW chunks fire to produce signal                            │
  │    2 input sources × 3 dynamics × compound                      │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  4 ORTHOGONAL axes = each describes a DIFFERENT dimension:
    → Same signal can be: reward (axis 1) + mild (axis 2)
      + social (axis 3) + Chunk-Shift (axis 4)
    → 4 axes do NOT replace each other — they COMPLEMENT each other


⭐ v2.0 ADDITION: BODY-NEED AGGREGATE FRAMING

  This file NOT ONLY classifies signals (axis 4).
  It ALSO shows: signals AGGREGATE into BODY-NEED.

  Body-need = aggregate output = synthesis of ALL signals currently
  demanding the body's response.
  §1 defines body-need. §2-§5 explain HOW body-need arises.
  = Missing link: "chunks fire" → "what does the body need" → "behavior"


  FILE POSITION IN FLOW:

    Chunk.md v2.2 (sole substrate)
         │
         ▼
    Chunk-Activation-Dynamics (HOW chunks fire: probability, re-linking)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ BODY-FEEDBACK-MECHANISM.MD v2.0 (THIS FILE)                  │
    │                                                              │
    │  §1:  BODY-NEED = aggregate output                           │
    │  §2:  Input: 2 sources (Sensory-Driven / Pattern-Driven)    │
    │  §3:  Dynamics: 3 types (Chunk-Shift / Chunk-Miss / Gap)    │
    │  §4:  Compound: multiple dynamics simultaneous               │
    │  §5:  Baseline Shift: quality re-habituation                 │
    │                                                              │
    │  Output: body-feedback signal (direction + magnitude)         │
    │  = HOW chunk dynamics PRODUCE body-feedback → body-need       │
    │  = Missing layer between "chunks fire" and "body needs what" │
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
⭐ BODY-NEED = AGGREGATE CURRENT STATE OF DEMAND:

  Body-need = aggregate of ALL signals currently demanding the body's response.

  NOT a single signal → it is the SYNTHESIS of many parallel signals.
  NOT created by PFC → body-need exists BEFORE PFC awareness.
  NOT only survival → ANY compiled gap-fill (Compilable Architecture).

  Body-need = OUTPUT OF THE MECHANISM this file describes:
    2 input sources (§2) → 3 chunk dynamics (§3) → compound (§4)
    → quality baseline shift (§5) → body-need aggregate

  (Inter-Body-Mechanism.md §2: Body-need full definition + inter-body context)
```

### §1.2 — 2 genuine sources

```
⭐ BODY-NEED COMES FROM ONLY 2 GENUINE SOURCES:

  ┌─────────────────────────────────────────────────────────────┐
  │ ① HARDWARE / SENSORY-DRIVEN (pre-chunk possible):           │
  │                                                             │
  │   Homeostatic: hunger, thirst, temperature, oxygen, sleep   │
  │   Nociceptive: pain, injury, reflex                         │
  │   Hormonal: social isolation hardware, sexual drive          │
  │                                                             │
  │   → Domain stimulus → receptors → body signal               │
  │   → Does NOT require compiled chunks (animals included)     │
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

  ⭐ 2 sources are NOT mutually exclusive — 1 event can activate BOTH ①+②:
    Example: eating food (① sensory) + remembering it tasted better before (② Miss)
    Example: social isolation (① hardware oxytocin deficit + ② compiled friend Miss)

  Details for each source: §2 of this file.
```

### §1.3 — Cross-cutting: What is NOT a source

```
🟡 OBSERVATION PARAMETERS AND STATE MODIFIERS = CROSS-CUTTING, NOT SOURCES:

  OBSERVATION PARAMETERS (named patterns, v7.8 — Protect.md §0):
    Protect = ownership chunks + loss aversion + avoidance direction
    Threat  = urgency tag + priority override (from ANY source)
    Status  = relative position pattern
    Novelty = gap-fill drive + approach direction
    → Emerge FROM ①+② in specific combinations
    → NOT a separate source — they are LABELS for observable patterns
    → Intervene at mechanism level (①②), not at the label level

  STATE MODIFIERS:
    Cortisol: amplifies negative signals (Cortisol-Baseline.md v2.0)
    Urgency: overrides priority ranking
    Energy/fatigue: shifts threshold for all signals
    → Do NOT create new body-need — SHIFT priority/intensity of existing needs

  WHY THE DISTINCTION MATTERS:
    "Protect" is NOT a 3rd source → "Protect" = Chunk-Miss (losing something compiled)
                                    + Chunk-Shift (threat to owned) + avoidance tag
    "Status drop" is NOT a 3rd source → = Chunk-Miss (compiled position lost)
    Correct intervention = intervene at ①② mechanism
    Wrong intervention = treating the label as an independent cause → miss root mechanism

  (Inter-Body-Mechanism.md §2.3: cross-cutting clarification)
```

### §1.4 — 7 properties of Body-Need

```
BODY-NEED HAS 7 PROPERTIES:

  ① ALWAYS EXISTS (never = 0)
     → "Relaxing on the beach" still has: sunlight on skin = sensory gap-fill
     → If 0 gap → 0 drive → 0 behavior → organism dies

  ② MULTIPLE simultaneously (parallel)
     → Hungry + bored + lonely + career anxiety = 4 body-needs in parallel

  ③ HAS PRIORITY (intensity × urgency × state)
     → "House fire" overrides "bored" (survival > novelty)
     → Priority = dynamic, shifts with state

  ④ HAS DIRECTION (from chunk network topology — Gap-Direction.md)
     → Only filling the right direction produces reward
     → Direction = f(surrounding chunks) → unique per person

  ⑤ PFC DOESN'T ALWAYS KNOW (exists before awareness)
     → "Bored but don't know what I need" = body-need exists, PFC hasn't identified it
     → PFC guessing wrong direction = scrolling social media instead of exercising

  ⑥ CAN CONFLICT (internal tension)
     → "Eat well vs stay fit" = 2 body-needs, opposite directions
     → PFC arbitrates → suppresses 1 → cost (Inter-Body §4)
     → Internal conflict = NORMAL, not pathological

  ⑦ CAN BE HIJACKED (temporary distortion)
     → Hormone (limerence): amplify 1 body-need → override all others
     → Scam: control input channels → direction distorted
     → Propaganda: collective fear → priority override
     → Domain Reality = final arbiter ALWAYS

  (Inter-Body-Mechanism.md §2.4: 7 properties full context)
```

### §1.5 — 4 types by immediacy

```
┌─────────────────────────────────────────────────────┐
│ IMMEDIATE (seconds-minutes):           [① dominant] │
│   Hunger, pain, heat. PFC clearly aware.            │
│   Direction is clear.                               │
├─────────────────────────────────────────────────────┤
│ SHORT-TERM (hours-days):              [①+② mix]    │
│   Boredom, loneliness, fatigue.                     │
│   PFC MAY NOT know clearly                          │
│   (scrolling social media but actually need to move).│
├─────────────────────────────────────────────────────┤
│ LONG-TERM (months-years):          [② meta dominant]│
│   Career, Imagine-Final, relationship direction.    │
│   PFC builds direction over many years.             │
├─────────────────────────────────────────────────────┤
│ STRUCTURAL (always running):   [①hardware + ②structural] │
│   Social belonging. Autonomy. Coherence.             │
│   PFC usually NOT aware (until violated).           │
└─────────────────────────────────────────────────────┘

  (Inter-Body-Mechanism.md §2.5: 4 immediacy types full context)
```

---

## §2 — 2 INPUT SOURCES

### §2.1 — Why distinguish 2 sources

```
🟡 BODY-FEEDBACK CAN ARISE FROM 2 DIFFERENT SOURCES:

  ① Domain changes → body-input changes → chunks fire REACTIVELY
  ② Chunks fire INTERNALLY (replay, preview, comparison) → body responds

  Same output (body-feedback signal).
  But DIFFERENT input pathway → different timing, different zones,
  different species capability.

  The distinction matters because:
  → Identifies WHERE to intervene (fix environment vs fix internal patterns)
  → Explains WHY animals also have body-feedback (sensory-driven)
  → Explains WHY humans have richer body-feedback (pattern-driven stronger)
```

### §2.2 — Sensory-Driven (from body-input)

```
⭐ SENSORY-DRIVEN — DOMAIN COMES FIRST, CHUNKS FIRE REACTIVELY:

  FLOW:
    Domain stimulus → receptors (17 categories) → neural signal
    → compiled chunks MATCH/MISMATCH → body-feedback fires

  CHARACTERISTICS:
    ① Body-input COMES FIRST — chunks fire REACTIVELY (responsive)
    ② D+C zones primary (peripheral + subcortical)
    ③ Animals included — no PFC required
    ④ Timing: 50ms (nociception reflex) → seconds (sensory processing)
    ⑤ BOTH reward AND dissonance

  DISSONANCE EXAMPLES:
    → Needle prick on skin → nociceptors fire → pain (D zone reflex)
    → Hot weather → thermoreceptors → discomfort
    → Cockroach → visual pattern match "disgusting" → disgust (C zone compiled)
    → Rough fabric on skin → somatosensory mismatch → discomfort
    → Garbage pile → olfactory → disgust

  REWARD EXAMPLES:
    → Good food → taste receptors → opioid (body-need met)
    → Beautiful music → auditory pattern → opioid (Goldilocks match)
    → Pleasant scent → olfactory → pleasant
    → Soft shirt put on → somatosensory match → comfortable
    → Beautiful painting → visual Goldilocks → aesthetic reward

  KEY FEATURES:
    → No PFC needed, no Imagine-Final needed
    → A dog eating tastier food still enjoys it — same mechanism
    → Body-input DIRECTLY drives chunk matching
    → Signal strength depends on delta between input and compiled baseline

  EVALUATIVE/DIRECT-STATE DIMENSION (Reward-Signal-Architecture §1 + Dissonance-Signal-Architecture §1):
    → Sensory-Driven ≈ DIRECT-STATE territory — BOTH DIRECTIONS:
      REWARD: Touch (CT afferents), warmth, taste = hardware-level
      DISSONANCE: Nociception, temperature deviation, hunger, itch = hardware-level
      Non-opioid/non-evaluative pathways, below PFC, minimal cortical involvement
    → Sensory-Driven CAN HAVE Evaluative component when cortical evaluation occurs:
      Reward: Beautiful music = auditory + cortical → Evaluative Reward
      Dissonance: "Cockroach on the plate" = visual + compiled disgust → Evaluative Dissonance
      Good food = taste + hedonic evaluation → Evaluative + Direct-State compound
    → "Pure sensory" = mostly Direct-State (BOTH reward and dissonance).
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
    ① Chunks fire INTERNALLY — no new domain stimulus required
    ② B+C zones primary (cortical + subcortical), A (PFC) optional
    ③ Animals have it (hippocampal replay), humans have it MUCH RICHER
    ④ Timing: seconds → years
    ⑤ BOTH reward AND dissonance
    ⑥ REQUIRES compiled chunks as prerequisite

  6 TRIGGER MECHANISMS (internal chunk firing):

    ⓐ REPLAY — hippocampus replays old experiences
       → Sleep replay (🟢 Walker 2017)
       → Awake replay (spontaneous recall)
       → "Remembering getting bitten by a dog" → body responds with fear

    ⓑ PREVIEW — PFC or hippocampus simulates the future
       → Imagine-Final preview: "what would it be like to buy a car?"
       → Body pre-feels: ~20-60% fidelity (Imagination.md §2)
       → Rats also do this: hippocampal preplay before navigation
         (🟢 Pfeiffer & Foster 2013)

    ⓒ COMPARISON — 2+ chunk patterns compared internally
       → Social comparison: "Person B is better than me at this"
       → Quality comparison: "yesterday's meal was better than today's"
       → Both PFC and unconscious can compare

    ⓓ GAP DETECT — ACC/insula detects inconsistency in the network
       → "Newtonian physics has contradictions" (Einstein)
       → "This framework feels like it's missing something" (felt sense)
       → Does NOT require PFC — ACC detects autonomously

    ⓔ SPREADING ACTIVATION — 1 chunk fires → cascade through the network
       → Person B boasts about her child → chunks about one's OWN child fire
       → Collins & Loftus 1975 🟢
       → Cascade can activate patterns that create new dissonance

    ⓕ CONTEXT-FREE CHUNK FIRE — trauma chunk fires without context:
       → Chunk.md §2.6: context-free chunks = ④ state only, MISSING ①②③
       → Sensory cue → amygdala low road match (~12ms) → chunk fires INTERNALLY
       → Body responds AS IF in original trauma (full state metadata fires)
       → = Pattern-Driven because the chunk fires INTERNALLY, not from an external threat
       → BUT the chunk LACKS temporal/spatial context → body DOESN'T KNOW it's the past
       → PFC arrives ~200ms LATER → corrective signal LATE + may be OFFLINE
       → = Flashback mechanism (PTSD-Analysis.md §4)
       → DIFFERS FROM ⓐ Replay: replay = hippocampal, HAS context → "remembering"
         ⓕ Context-free = amygdala, NO context → "reliving"
       → 🟢 LeDoux 1996: low road ~12ms, 🟢 Brewin 2010: S-rep

  DISSONANCE EXAMPLES:
    → Person A hears Person B brag about her child → comparison → wistful pang
    → Einstein sees physics contradiction → restless unease (gap detect)
    → Remembering being betrayed → pain (replay)
    → Imagine-Final of owning something not yet achieved → sense of lack (preview)

  REWARD EXAMPLES:
    → Imagine-Final "I'll solve this problem" → mini opioid (preview)
    → Recalling a beautiful memory → warmth (replay)
    → Comparing "I'm better than before" → confidence (comparison)
    → Gap fill: "Ah, I understand now!" → opioid burst (gap filled)

  EVALUATIVE/DIRECT-STATE DIMENSION (Reward-Signal-Architecture §1 + Dissonance-Signal-Architecture §1):
    → Pattern-Driven = primarily EVALUATIVE territory — BOTH DIRECTIONS:
      REWARD: Cortical pattern match → OFC/vmPFC → opioid (if match)
        Insight, coherence, preview = all require cortical processing
      DISSONANCE: Social comparison → dACC, moral injury → vmPFC + ACC,
        anxiety preview → CRH → amygdala = all EVALUATIVE Dissonance
        (Dissonance-Signal-Architecture.md §1.3: MOST adult suffering = Evaluative)
    → Pattern-Driven CAN activate Direct-State:
      Reward: Replay of touch → body re-simulates → B partial activation
      Dissonance: Replay of pain → body re-simulates → Direct-State trace
    → Evaluative Gates Direct-State = GENERAL mechanism (both directions):
      Reward: A evaluation MODULATES B body-state reward response
      Dissonance: Placebo/Nocebo = PROOF (Wager 2004, Zubieta 2005)
        PFC evaluation MODULATES Direct-State pain (Dissonance-Signal-Architecture §3)
      = WHY "thinking about a hug" ≠ "actually being hugged" AND
        "fearing pain" amplifies actual pain

  🟢 RESEARCH:
    → Hippocampal replay/preplay: Pfeiffer & Foster 2013, Wilson & McNaughton 1994
    → Spreading activation: Collins & Loftus 1975
    → Social comparison: Festinger 1954
    → ACC error detection: Bush et al. 2000
```

### §2.4 — Comparing the 2 sources

```
┌──────────────────────┬──────────────────────┬──────────────────────┐
│                      │ SENSORY-DRIVEN       │ PATTERN-DRIVEN       │
├──────────────────────┼──────────────────────┼──────────────────────┤
│ Trigger              │ Domain stimulus      │ Internal chunk fire  │
│ Direction            │ Outside → In         │ Inside → Body        │
│ Primary zones        │ D + C                │ B + C (A optional)   │
│ Reward type          │ Mostly Direct-State  │ Mostly Evaluative    │
│ Dissonance type      │ Mostly Direct-State  │ Mostly Evaluative    │
│ Animals              │ FULL capacity        │ Have it but limited  │
│ PFC needed?          │ NO                   │ Optional             │
│ Timing               │ ms → seconds         │ seconds → years      │
│ Prerequisite         │ Receptors active     │ Compiled chunks      │
│ Dissonance examples  │ Needle, heat, insect │ Comparison, recall   │
│ Reward examples      │ Good food, music     │ Insight, preview     │
│ Intervention         │ Fix environment      │ Fix internal pattern │
└──────────────────────┴──────────────────────┴──────────────────────┘

⭐ BOTH SOURCES → SAME OUTPUT: body-feedback signal (direction + magnitude)
⭐ BOTH SOURCES → can trigger ANY chunk dynamics (§3)
⭐ NOT MUTUALLY EXCLUSIVE: 1 event can activate BOTH sources simultaneously
   Example: eating (sensory) + remembering it tasted better before (pattern)
```

### §2.5 — Complexity Spectrum (same mechanism, different substrate)

```
🟡 3 DYNAMICS (§3) OPERATE AT ALL SUBSTRATE LEVELS:

  ┌─────────────────────────────────────────────────────────────────┐
  │ SIMPLE (physical objects, sensory patterns):                     │
  │   Chunk-Miss: soft fabric baseline → stiff fabric = "worse"     │
  │   Chunk-Shift: familiar food → discovered it's expired = valence flip│
  │   Chunk-Gap: recipe missing 1 ingredient → "something feels off"│
  ├─────────────────────────────────────────────────────────────────┤
  │ SOCIAL (entities, relationships):                                │
  │   Chunk-Miss: close friend absent = "I miss them"               │
  │   Chunk-Shift: close friend betrays = valence flip on entity chunks│
  │   Chunk-Gap: "they seem upset about something" = gap in Self-Pattern-Modeling model│
  ├─────────────────────────────────────────────────────────────────┤
  │ META (abstract compiled structures):                             │
  │   Chunk-Miss: Imagine-Final not achieved = compiled preview missed│
  │               Status drop = compiled position lost               │
  │               Obligation violated = compiled prediction broken   │
  │   Chunk-Shift: Identity challenge = self-schema valence shift    │
  │   Chunk-Gap: "Life feels like it lacks meaning" = meta-gap in coherence│
  └─────────────────────────────────────────────────────────────────┘

  ⭐ KEY INSIGHT — TIER ③ COLLAPSE:

    Imagine-Final, Obligation, Identity, Status:
    = SAME chunk dynamics (Gap/Miss/Shift)
    = Only differ in SUBSTRATE LEVEL (meta-compiled structures)
    = Different timescale + PFC involvement + intervention approach
    = NOT a separate mechanism — NO new classification tier needed

    Why meta FEELS different:
    → Network size larger (identity = hundreds of chunks)
    → Timescale longer (career gap = years)
    → More PFC involvement (abstract requires cortical)
    → But BODY-FEEDBACK MECHANISM = SAME: Gap/Miss/Shift

    → Parsimony: 3 dynamics explain ALL levels
    → Intervention: identify WHICH dynamic + WHICH substrate
    → "Life lost its meaning" = Meta Chunk-Gap = ACC detects
      inconsistency in coherence network → body signal "restless unease"
      → same mechanism as "physics has contradictions" but different substrate

  (Inter-Body-Mechanism.md §2.2: complexity spectrum defined)
```

---

## §3 — 3 CHUNK DYNAMICS

### §3.0 — Overview

```
🟡 WHEN BODY-FEEDBACK FIRES, THE CHUNK NETWORK HAS 3 TYPES OF CHANGES:

  Chunk dynamics DESCRIBE: what happens INSIDE the chunk network when a signal is generated.

  ① CHUNK-SHIFT — VALENCE of chunks changes (content stays the same)
  ② CHUNK-MISS  — a compiled pattern is NOT FIRED (absent)
  ③ CHUNK-GAP   — a pattern NEVER EXISTED but the network detects it missing

  3 dynamics:
  → NOT mutually exclusive — 1 event can trigger 2-3 dynamics simultaneously (§4)
  → Apply to BOTH reward AND dissonance (different direction, same mechanism)
  → Can be triggered by BOTH sensory-driven AND pattern-driven (§2)
  → Operate at ALL substrate levels: Simple / Social / Meta (§2.5)
```

### §3.1 — Chunk-Shift (valence changes)

```
⭐ CHUNK-SHIFT — SAME CHUNKS, DIFFERENT EVALUATION:

  DEFINITION:
    The VALENCE (evaluation) of the chunk network CHANGES.
    Chunk CONTENT remains the same — EVALUATION changes.
    Can be sudden (1 event) or gradual (many events).

  MECHANISM:
    New information (1 new chunk or 1 new experience)
    → Re-evaluate valence of connected chunks
    → Valence propagates through network (Valence-Propagation.md §4)
    → Body-feedback fires according to NEW valence

  DIRECTION:
    Shift NEGATIVE (dissonance):
      → Betrayal: chunks about the person STILL THERE, valence FLIPS negative
      → Discovering counterfeit goods: product chunks still there, valence drops
      → Receiving bad news about someone: chunks still there, valence shifts

    Shift POSITIVE (reward):
      → Successful exposure therapy: fear chunks → safety association grows
      → Learning to use a new tool: fear valence → utility valence
      → Getting a misunderstanding explained: negative valence → positive restored

  WHY "SHIFT" NOT "FLIP":
    → "Flip" implies binary (+ → -), but reality is a GRADIENT
    → Can shift slightly (mild disappointment) or strongly (betrayal)
    → Can shift at MULTIPLE channels at different magnitudes (Valence-Propagation §2)
    → "Shift" captures partial change too

  CHARACTERISTICS:
    ① Chunk CONTENT doesn't change — memories remain the same
    ② Only VALENCE (evaluation) changes
    ③ Propagation through network: 1 chunk shifts → pulls many chunks along
    ④ Intensity depends on: network size × shift magnitude × surprise level
    ⑤ Underlying mechanism: competitive re-linking (Chunk-Activation-Dynamics §3)

  ANALYZED EXAMPLE — BETRAYAL:

    Before discovery:
      Chunks [romantic partner] = {
        Visual: face, posture, smile — content
        Auditory: voice — content
        Somatic: embrace, touch — content
        Emotional: love, trust, safety — VALENCE (positive)
      }

    After discovering "betrayal":
      1 NEW chunk compiles: [betrayal] (emotional peak, 1 occurrence enough)
      → Valence propagation: [betrayal] → re-evaluates ALL connected chunks
      → Chunks [romantic partner] = {
        Visual: SAME face, posture, smile — content UNCHANGED
        Auditory: SAME voice — content UNCHANGED
        Somatic: SAME feelings — content UNCHANGED
        Emotional: pain, anger, loss, betrayed — VALENCE SHIFTED
      }

    → Same memories. Same content. DIFFERENT evaluation.
    → "Looking at old photos and feeling pain" = content trigger → new valence fires → dissonance

  🟢 RESEARCH:
    → Evaluative conditioning: valence transfer via association (De Houwer 2007)
    → Fear conditioning: rapid valence assignment (LeDoux 1996)
    → Extinction ≠ erasure: old valence suppressed, not deleted (Bouton 2004)
    → Reconsolidation: valence CAN be modified during window (Nader 2000)
```

### §3.2 — Chunk-Miss (compiled pattern absent)

```
⭐ CHUNK-MISS — A COMPILED PATTERN IS NOT FIRING:

  DEFINITION:
    Body-base has compiled pattern X into its baseline.
    Pattern X stops firing (absent, degraded, or reduced quality).
    VTA detects: actual < compiled baseline → negative prediction-delta.
    Body signal: "worse than expected."

  MECHANISM:
    ① Body compiles chunks at quality X (through repetition, experience)
    ② VTA habituates to pattern X → X = new baseline
    ③ Pattern X becomes absent or quality drops
    ④ VTA fires NEGATIVE prediction-delta (dopamine SUPPRESSED)
       → 🟢 Schultz 1997: reward < predicted → dopamine dip below baseline
    ⑤ Body signal: dissonance ("worse than expected")

  ⭐ BODY-BASE DOESN'T "REMEMBER" IN THE PFC RECALL SENSE:
    → Compiled baseline = Hebbian LTP has wired the pattern
    → Pattern exists at BODY LEVEL (C+D zones)
    → Does NOT require PFC to recall — compiled pattern SELF-FIRES when mismatch
    → Similar to: having worn soft fabric for years, then putting on stiff fabric
      → body signal fires BEFORE PFC "remembers" the soft fabric

  4 VARIANTS:

    ⓐ CLEAR MISS — PFC knows what's missing:
       → Accustomed to scrolling social media → phone breaks → "want to scroll but can't"
       → Soft fabric → stiff fabric → "this shirt feels rough"
       → High-quality food → lower quality → "today's meal isn't as good"
       → PFC HAS label: knows the source, knows what it wants

    ⓑ DIFFUSE MISS — delta accumulates, PFC doesn't detect:
       → Staying home watching videos for days → sluggishness → "bored but don't know why"
       → Gradually reducing physical movement → body gets restless → PFC confused
       → Each day's delta too small → doesn't cross PFC attention threshold
       → Connection: Boredom-Analysis.md core mechanism
       → ESPECIALLY DANGEROUS: accumulates silently → erupts when threshold exceeded
       → ⭐ Self-Observation connection (Self-Observation.md §2):
         Prediction-delta exceeds threshold → Self-Observation triggered
         Diffuse Miss accumulates → Self-Observation DELAYED (delta < threshold each day)
         = Micro-negative delta (sankhara-dukkha): Self-Observation Trigger Type ②

    ⓒ UNCONSCIOUS MISS — body knows, PFC doesn't:
       → Living in a city for years → returning to countryside → suddenly invigorated
       → "Don't know why I like hiking, why forests feel comfortable"
       → Body compiled patterns (air, trees, movement) at C+D level
         → PFC has NO verbal label
       → When pattern fires again → opioid → "comfortable, don't know why"
       → Individual preferences = compiled patterns unique to individual experience

    ⓓ IRRESOLVABLE MISS — hardware prevents resolution:
       → Normal miss (ⓐⓑⓒ): miss → adjust → resolve (seconds-days)
       → Irresolvable miss: hardware PREVENTS resolution
       → Parkinson-Analysis.md §5.2: PFC predicts "take a step"
         → gate LOCKED → body CANNOT step → MISMATCH
         → Adjust → try harder → STILL fail → CANNOT resolve
       → = Chronic prediction-delta where EVERY attempt creates a new miss
       → Accumulation: frustration + helplessness + chronic↑ cortisol
       → UNIQUE: no condition creates irresolvable miss as clearly as Parkinson's
         (Addiction: execution OK. Depression: IF pushed → POSSIBLE. Parkinson: CAN'T.)
       → 🟡 Framework: irresolvable miss = new Chunk-Miss variant (from drill)

  MISS → REWARD (reverse direction):
    → Reunion: meeting an old friend → pattern fires again → opioid
    → Returning home: compiled nature patterns fire → reward
    → Recovery after illness: body patterns restore → relief + reward

  🟢 RESEARCH — SUCCESSIVE NEGATIVE CONTRAST (SNC):

    Crespi 1942, Flaherty 1996:
    → Setup: Group A eats 32% sucrose (excellent) many trials → switch to 4% (ordinary)
    → Control: Group B eats 4% sucrose from the start
    → Result: Group A after switch → eats LESS than Group B
    → = Body doesn't just "feel slightly disappointed" — reaction is STRONGER than neutral
    → = Compiled baseline being violated → ACTIVE NEGATIVE signal

    → Amsel frustration theory: SNC = PRIMARY FRUSTRATION
      = aversive emotion triggered when expected-actual discrepancy occurs
    → = Chunk-Miss mechanism at ANIMAL level — no PFC needed

    Schultz 1997 — neural mechanism:
    → Expected reward = X (compiled baseline)
    → Actual reward = Y
    → Y > X → dopamine INCREASES ("better than expected")
    → Y = X → dopamine NORMAL ("exactly expected")
    → Y < X → dopamine SUPPRESSED ("worse than expected") ⭐
    → Dopamine suppression = ACTIVE SIGNAL: "worse than expected"

  BASELINE SHIFT DYNAMICS (see §5 for details):
    → 1 experience not enough to strongly shift baseline
    → Many experiences → Hebbian wire hardens → baseline shifts clearly
    → Miss after 1 experience = mild. Miss after 100 experiences = strong.
    → Recovery possible: if lower quality sustained long enough → re-habituates
```

### §3.3 — Chunk-Gap (pattern doesn't yet exist)

#### §3.3a — Core: Definition + Mechanism

```
⭐ CHUNK-GAP — PATTERN NEVER EXISTED BUT NETWORK DETECTS IT MISSING:

  DEFINITION:
    Chunk network topology has HOLES or CONFLICTS.
    Pattern SHOULD exist (based on network structure) but DOESN'T.
    ACC/insula detects inconsistency → body signal "something is missing / contradictory."
    DIFFERS FROM Chunk-Miss: Miss = EXISTED then lost. Gap = NEVER EXISTED.

  MECHANISM:
    ① Chunk network compiles through experience → network topology forms
    ② Network has internal structure (connections, patterns, expectations)
    ③ Structure predicts: "if A and B are true, C must exist"
    ④ But C hasn't compiled → HOLE in the network
    ⑤ ACC detects inconsistency → body signal "restless unease, something's off"
    ⑥ Signal drives behavior: search, explore, resolve → fill gap

  CHARACTERISTICS:
    ① PFC may or may NOT be able to articulate what's missing
    ② Felt sense = body detecting gap before PFC verbal label
       (Somatic-Articulation-Loop.md: implicit → transitional → explicit)
    ③ Signal persistent — doesn't self-resolve (gap must be filled)
    ④ Filling gap → opioid reward (effort-proportional: 03-Reward.md §4.7)
    ⑤ ⭐ FOUNDATION FOR NOVELTY DRIVE
       Gap detect → restless unease → drive to explore/fill → discovery → opioid
    ⑥ ⭐ GAP HAS A SPECIFIC DIRECTION (Gap Direction):
       "Structure predicts C" → C has a SHAPE = f(surrounding chunks)
       → Gap direction = what SPECIFICALLY is predicted missing
       → Reward fires ONLY when fill MATCHES direction, not just "fill any gap"
       → "Not knowing something = no gap" (no chunks → no boundary → no hole)
       → Details: Gap-Direction.md (4 properties, 2-layer model, unified Tier 1-4)

  GAP vs MISS:

    ┌───────────────────────────┬──────────────────────┐
    │ CHUNK-MISS                │ CHUNK-GAP            │
    ├───────────────────────────┼──────────────────────┤
    │ EXISTED → lost            │ NEVER EXISTED        │
    │ Body "remembers" baseline │ Network "predicts"   │
    │ Negative prediction-delta │ Inconsistency detect │
    │ VTA mechanism             │ ACC mechanism        │
    │ "Want back what was lost" │ "Want what's missing"│
    │ Resolution = restore      │ Resolution = create  │
    │ Example: phone broken     │ Example: Einstein E=mc²│
    └───────────────────────────┴──────────────────────┘

  EXAMPLES:

    Einstein:
      → Chunk network about physics: Newton + Maxwell + thought experiments
      → Network internal structure: "if both are correct there must be a unified framework"
      → Unified framework DOESN'T EXIST → GAP
      → Body signal: "restless unease, physics isn't coherent" → drives research
      → Fill gap (E=mc²) → extremely powerful opioid burst (years of pending)

    A framework in development:
      → Chunk network about cognitive science being built
      → "Vaguely sense something's missing" → GAP (body detects before PFC articulates)
      → Drives drilling → fills gap → "Ah, chunk dynamics classification!"
      → Insight = gap filled → opioid

    Chunk-Gap + CONFLICT (sub-type):
      → 2 patterns fire CONTRADICTORY → both can't be true simultaneously
      → GAP = missing RESOLUTION between the 2 patterns
      → Example: cognitive dissonance (Festinger 1957)
      → Example: "should I stay or should I go?" — 2 Imagine-Finals compete,
        gap = no resolution

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
  │  Body signal: "restless, something's    │
  │  missing"                               │
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
  │  = Science = systematic gap-filling      │
  │  = Art = aesthetic gap-filling           │
  └─────────────────────────────────────────┘
```

#### §3.3c — Gap → Miss Transition

```
⭐ A GAP CAN TRANSITION INTO CHUNK-MISS:

  Pure Chunk-Gap: ACC detects "missing" → body restless → drives searching.
  BUT Gap can TRANSITION into Chunk-Miss via the following mechanism:


  ① CORE MECHANISM — Imagine-Final preview compiles into baseline:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  Gap detected (ACC) → PFC builds Imagine-Final preview      │
  │    ↓                                                        │
  │  Imagine-Final stabilizes + repeated many times             │
  │    ↓                                                        │
  │  Body compiles preview into expectation baseline            │
  │  (§5 Quality Baseline Shift: repeated preview = new normal) │
  │    ↓                                                        │
  │  Body now EXPECTS what never-yet-existed                    │
  │    ↓                                                        │
  │  Reality still DOESN'T have it → VTA: actual < baseline     │
  │    ↓                                                        │
  │  = Chunk-Gap (ACC, vague) → Chunk-Miss (VTA, specific)     │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

    Condition: Imagine-Final must be STABLE (unchanging) + REPEATED enough.
    If Imagine-Final CHANGES → gap also changes → body fires NEW pattern → different path.


  ② WHY PREVIEW REPEATS — Cortisol holding signal:

    Gap persists + unresolved → cortisol fires "still need change"
    (Cortisol-Baseline.md §3.8: holding signal keeps imagination loop active)
    → PFC is FORCED to return to Imagine-Final → preview repeats COMPULSIVELY
    → Baseline compiles FASTER than voluntary preview
    → = "Can't stop thinking about it" = cortisol holding loop
    → = Cortisol = ACCELERATOR for Gap→Miss transition


  ③ DIRECTION TAG — Same transition, DIFFERENT outcome:

    Cortisol direction (Cortisol-Baseline.md §3.5) determines QUALITY:

    Gap + Novelty cortisol (curiosity body state):
      → Baseline compiles with opioid tag
      → Miss = "want + don't have yet" → DRIVES seeking → productive
      → = "Eager expectation"

    Gap + Threat cortisol (anxiety body state):
      → Baseline compiles with cortisol tag
      → Miss = "fear + don't have yet" → ANXIETY loop → destructive
      → = "Anxious expectation"

    → Same Gap→Miss mechanism, DIFFERENT direction → COMPLETELY different outcome


  ④ APPLICATION — "The higher the expectation, the greater the disappointment":

    This folk wisdom = Gap→Miss transition:

      Preview VIVID + repeated MANY TIMES + Imagine-Final STABLE
        → Body compiles HIGH baseline
          → Reality < baseline → Chunk-Miss delta LARGE → "big disappointment"

      Preview LOW or NO preview
        → Low baseline → Reality ≥ baseline → "comfortable surprise"

    EXAMPLES:
      → A child sees another child getting hugged → PFC previews "what if I get hugged"
        → Preview repeats → baseline shifts → lacking = specific Chunk-Miss
        → Starts as Gap (vague) → later becomes Miss (clear, painful)

      → Showroom car: preview "having the car" repeats for months
        → Body compiles into expectation → not having it = Miss
        → Different from "not knowing the car exists" (pure Gap)


  ⑤ WHEN TRANSITION DOES NOT OCCUR:

    If Imagine-Final UPDATES CLOSE TO REALITY → baseline tracks reality
    → Delta small → does NOT become a strong Miss.

    Imagine-Final updates when:
      → Domain feedback loop: ACTION → receive feedback → update
      → Background processing: sufficient sleep + cortisol not too high
      → Sufficient related chunks: raw material for background processing

    Most people: stable chunks → stable Imagine-Final → preview repeats
    → Transition almost certain when gap persists.
```

#### §3.3d — Gap Decomposition (Mini-Arc Dynamics)

```
⭐ GAP DECOMPOSITION — MINI-ARC DYNAMICS:

  A Big Gap exists for YEARS (e.g., Einstein unified physics).
  The body CANNOT sustain Gap signal continuously without reward.
  → IF gap doesn't decompose → burnout / giving up OR Gap→Miss transition.

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  BIG GAP: "unified physics framework"                       │
  │    ↓                                                        │
  │  Decompose into MINI GAPS (naturally or PFC-directed):      │
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
⭐ COMPOUND — MULTIPLE DYNAMICS FIRING SIMULTANEOUSLY:

  PRINCIPLE:
    3 chunk dynamics are NOT mutually exclusive.
    1 event can trigger 2-3 dynamics at the same time.
    Each additional dynamic adds another "flavor" to body-feedback.
    = Why dissonance/reward HAS MANY NUANCES.


  ANALYZED EXAMPLE — LOSING $100:

  ┌──────────────────────┬──────────────────┬──────────────────┬──────────────────┐
  │ Event                │ Chunk-Shift      │ Chunk-Miss       │ Chunk-Gap        │
  ├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
  │ Accidentally dropped │                  │ ✅ resource loss  │                  │
  │ $100                 │                  │                  │                  │
  │ Subjective feeling:  │                  │ "regret"         │                  │
  ├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
  │ Scammed out of $100  │ ✅ trust shift    │ ✅ resource loss  │                  │
  │                      │                  │                  │                  │
  │ Subjective feeling:  │ "anger"          │ "regret"         │                  │
  ├──────────────────────┼──────────────────┼──────────────────┼──────────────────┤
  │ Scammed by a close   │ ✅ trust FLIP     │ ✅ resource loss  │ ✅ identity gap:  │
  │ friend, $100         │ strong + connec- │                  │ "who am I that   │
  │                      │ tion damage      │                  │ my best friend   │
  │                      │                  │                  │ would do this?"  │
  │ Subjective feeling:  │ "anger + pain"   │ "regret"         │ "bitterness"     │
  └──────────────────────┴──────────────────┴──────────────────┴──────────────────┘

  → Same $100 loss. 1 dynamic → 2 → 3 = more complex, more painful, longer to resolve.


  ANALYZED EXAMPLE — PERSON A / PERSON B:

    Person A feeling smooth, enjoying social time
    → Person B brags about her child's achievement (sensory input: auditory)
    → Spreading activation: chunks about ONE'S OWN CHILD fire
    → Chunk dynamics:
      Chunk-Gap: own child vs Person B's child → gap "my child hasn't achieved that"
      Chunk-Shift (mild): valence of the gathering shifts from enjoyable → wistful
    → Compound: Gap + Shift → "a pang of wistfulness, becomes quiet"
    → NOTE: body-input did NOT change — only internal chunk firing changed


  COMPOUND REWARD EXAMPLE — EINSTEIN BREAKTHROUGH:

    Fill Chunk-Gap: E=mc² resolves physics contradiction → gap filled → STRONG opioid
    Chunk-Shift: self-schema shifts ("I = the person who solved it") → positive
    Chunk-Miss (reversed): years of "missing a solution" → HERE IT IS → relief + reward
    → Compound 3 dynamics → extreme euphoria


  ⭐ COMPOUND PRINCIPLE:

    Signal_total = Σ (dynamics_i × intensity_i × network_size_i)

    → More dynamics = STRONGER total signal
    → Larger network_size = wider propagation = affects more chunks = STRONGER
    → Intensity of each dynamic depends on delta magnitude
    → = Why "best friend betraying you" > "stranger scamming you" > "accidentally losing money"
      (same loss, different compound level)


  🟡 CONDITIONAL INTERACTION MODEL (Reward-Signal-Architecture.md §6):

    ⚠️ COMPOUND ≠ ADDITIVE.
    Formula above = APPROXIMATION. Reality: CONDITIONAL.

    Reward compound is NOT simply A + B. 4 VARIABLES determine interaction:

    ① Substrate Overlap:
       → Same receptor system (opioid + opioid) → SUPERADDITIVE
       → Different systems (opioid + endocannabinoid) → ADDITIVE
       → Competing (opioid + cortisol) → SUBTRACTIVE

    ② A Gate Direction (Reward-Signal-Architecture.md §3):
       → A evaluates → AMPLIFY B → superadditive
       → A evaluates → SUPPRESS B → subtractive
       → A absent → B RAW (no evaluation)

    ③ Relief Presence:
       → If pending threat resolved → cortisol DROP = MULTIPLIER
       → If no threat → opioid only, no relief bonus
       → Relief + reward = STRONGEST compound (Archimedes "Eureka!")

    ④ Temporal Overlap:
       → Simultaneous → compound (most powerful)
       → Sequential (seconds) → cascade (moderate)
       → Sequential (hours+) → independent (no compound)

    → Diagnostic: unexpectedly intense emotional compound → check 4 variables
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
    Quality drops to Y < X → negative prediction-delta → dissonance (Chunk-Miss).
    = Baseline "drifts" with experience.


  4-STEP MECHANISM:

    ① COMPILE:
       Repeated experience at quality X → Hebbian LTP → neurons wire the pattern
       → Pattern compiled into C+D zones (subcortical + peripheral)
       → Does NOT require PFC to maintain (body-level compile)

    ② HABITUATE:
       VTA habituates to pattern X → X = "normal" → no signal fires
       → Like a thermostat set at 25°C: no signal when temperature is exactly 25°C

    ③ DETECT DELTA:
       Actual quality changes:
       → Actual > baseline → positive prediction-delta → reward
       → Actual < baseline → negative prediction-delta → Chunk-Miss
       → Actual = baseline → no signal → neutral

    ④ RE-HABITUATE:
       If NEW quality sustained long enough → baseline SHIFTS again:
       → New quality LOWER sustained → body re-habituates → baseline drops
       → New quality HIGHER sustained → body re-habituates → baseline rises
       → = Hedonic adaptation (🟢 Brickman 1978)


  TIMELINE + COMPILE STRENGTH:

    ┌──────────────────────────────────────────────────────────────┐
    │                                                              │
    │  1 experience (high quality):                                │
    │    → Proto-chunk weak → baseline shift SLIGHT                │
    │    → PFC has Imagine-Final preview                           │
    │    → Body-base hasn't clearly shifted                        │
    │    → If quality drops → PFC "let down" > body-base dissonance│
    │                                                              │
    │  A few times (3-10):                                         │
    │    → Chunk strengthening → baseline starts to shift          │
    │    → SNC effect appears (Crespi: rats in downshift)          │
    │    → Body-base dissonance CLEAR when quality drops           │
    │                                                              │
    │  Many times (50-100+):                                       │
    │    → Chunk fully compiled → baseline SHIFT HARDENED          │
    │    → Quality drop = STRONG dissonance (SNC effect maximum)   │
    │    → Re-habituating downward is slow (strong compile = slow decay) │
    │                                                              │
    │  → compile_rate ≈ f(repetition × saliency × peak_valence    │
    │                     × multi_modal × contingency)             │
    │  → Chunk.md v2.2 §2.2: same 5-parameter formula             │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘


  ANIMALS HAVE BASELINE SHIFT:

    🟢 Crespi 1942 / Flaherty 1996 (SNC in rats):
    → Rats trained on high reward → downshift → WORSE than control group
    → = Compiled baseline + negative prediction-delta
    → = Chunk-Miss mechanism at animal level
    → Does NOT require PFC — mechanism operates at body-base level

    A dog accustomed to better food that rejects cheaper food:
    → Baseline shift: high quality = new normal
    → Cheaper food = Chunk-Miss → body signal of refusal
    → Retraining: sustained lower quality → re-habituates → accepts
    → = Same mechanism as rat SNC


  KEY FEATURES:

    ① BIDIRECTIONAL: baseline shifts UP and DOWN
    ② ASYMMETRIC: shift UP is easier than shift DOWN
       → 🟢 Loss aversion (Kahneman & Tversky 1979): losing hurts ~2x gaining
       → Body resists quality decrease MORE strongly than it accepts quality increase
    ③ DOMAIN-SPECIFIC: baseline shifts INDEPENDENTLY per domain
       → Food baseline and clothing baseline shift SEPARATELY
       → Can be habituated to better food but not yet to better clothing
    ④ INDIVIDUAL: each person's baseline DIFFERS due to different experiences
       → Same quality level → Person A experiences as "normal," Person B as "excellent"
       → = Per-person reward (03-Reward.md §5.9)
```

---

## §6 — FRAMEWORK MAP

### §6.1 — v7.8 Cycle Architecture

```
🟡 CHUNK DYNAMICS IN V7.8 PERCEPTION-ACTION CYCLE:

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  ① DOMAIN → BODY-INPUT (L0 + L1 receptors)                    │
  │     → SENSORY-DRIVEN input enters here                         │
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
  │     → PFC observes signal but may NOT know which dynamic        │
  │     → "Wistful pang" = PFC label for Chunk-Gap + Chunk-Shift   │
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

  Body-Feedback-Precondition: Signal fires when ALL 5 preconditions are met.
  Chunk dynamics describe HOW signal arises — Body-Feedback-Precondition describes WHEN.

  ┌────────────────────────────────┬─────────────┬─────────────┬─────────────┐
  │ Body-Feedback-Precondition     │ Chunk-Shift │ Chunk-Miss  │ Chunk-Gap   │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-1 Directed-Gap    │ Shift creates│ Miss = body-│ Gap = body- │
  │ (body-need gap)                │ NEW pending  │ need lost   │ need missing│
  │                                │ (betrayal → │ quality     │ pattern     │
  │                                │ need repair) │             │             │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-2 Chunk-Substrate │ Needs chunks │ Needs       │ Needs enough│
  │ (sufficient substrate)         │ to evaluate  │ compiled    │ network to  │
  │                                │ new info     │ baseline    │ DETECT gap  │
  │                                │              │ (no compile │             │
  │                                │              │ = no miss)  │             │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-3 Delta-Gate      │ Shift =      │ Miss = neg. │ Gap detect  │
  │ (sufficient delta)             │ valence      │ prediction  │ = ACC       │
  │                                │ delta        │ error       │ signal      │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-4 Match-Range     │ Shift occurs │ N/A (body   │ Gap must be │
  │ (dynamic zone)                 │ at ANY match │ already     │ detectable  │
  │                                │ level        │ knows)      │ (not too    │
  │                                │              │             │ alien)      │
  ├────────────────────────────────┼─────────────┼─────────────┼─────────────┤
  │ Precondition-5 Compile-Gate    │ NEW valence  │ Compiled    │ Compiled    │
  │ (Direction-At-Compile)         │ tag from     │ baseline    │ surrounding │
  │                                │ shift event  │ carries tag │ chunks' tag │
  └────────────────────────────────┴─────────────┴─────────────┴─────────────┘

  INSIGHTS:
  → Chunk-Miss does NOT require Precondition-4 (Match-Range) — body already has baseline
  → Chunk-Gap REQUIRES Precondition-2 (enough network to detect gap)
  → Chunk-Shift REQUIRES Precondition-3 (delta large enough to register)
  → Compound = Precondition-1 through Precondition-5 checked MULTIPLE TIMES per dynamic
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

  🟡 3+1 Chunk-Miss variants (clear / diffuse / unconscious / irresolvable):
     Each observable. Taxonomy = framework contribution.
     v1.3→v2.0: ⓓ irresolvable = hardware prevents resolution (Parkinson drill).

  🟡 Context-free chunk as Pattern-Driven variant:
     PTSD drill: flashback = ⓕ context-free chunk fires internally.
     Consistent with Brewin 2010 DRT + Chunk.md §2.6 context-tag model.

  🟡 v2.0 NEW — Body-need as aggregate output:
     Body-need concept established in motivation research.
     Framing as aggregate of 2-source × 3-dynamics = framework contribution.

  🟡 v2.0 NEW — Complexity Spectrum (Simple → Social → Meta):
     Each substrate level observable. Unified taxonomy = framework contribution.
     Tier ③ collapse: meta-level = same dynamics, different substrate.

  🟡 v2.0 NEW — Cross-cutting clarification:
     Observation parameters + state modifiers ≠ sources.
     Conceptual clarification = framework contribution.


🔴 SPECULATIVE:

  🔴 Exact compound signal summation formula
  🔴 Precise timeline for baseline shift (1 vs 10 vs 100 exposures)
  🔴 ACC as primary Gap detector (vs other conflict detection circuits)
  🔴 Chunk-Miss variant boundaries (clear threshold between clear/diffuse/unconscious)
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
     → Compound dissonance ($100 example)
     → Social dissonance without body-input change (Person A/B)
     → Animal body-feedback (SNC without PFC)
     → Felt sense gap detection (Gendlin, before PFC verbal)
  ✅ Provides foundation for Novelty drive (Chunk-Gap loop)
  ✅ Orthogonal to existing 3 axes — COMPLEMENTS, doesn't REPLACE
  ✅ v2.0: Body-need aggregate framing connects dynamics → behavior
  ✅ v2.0: Complexity Spectrum shows parsimony (3 dynamics → all levels)

LIMITATIONS:
  ⚠ Boundaries between 3 dynamics: some cases COULD be classified differently
     → Betrayal: is it Shift (valence change) or Gap (trust resolution gap)?
     → Answer: COMPOUND — both fire. Boundary is soft.
  ⚠ Exact neural pathways for each dynamic not fully mapped
  ⚠ Compound summation is conceptual, not quantified
  ⚠ Baseline shift timeline lacks precise dose-response data
  ⚠ Body-need aggregate concept = framework synthesis, not independently tested
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
  → Inter-Body-Mechanism.md v1.0 — Body-need §2, 3-cost §4, 5-channel §6
    → §2 Body-need aggregate: full 7 properties + 4 immediacy types
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
  → 03-Reward.md §5 — Car Paradox (per-person Chunk-Miss/Gap)
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
    → Diffuse Miss ⓑ = Self-Observation Trigger Type ② (micro-negative, sankhara-dukkha)
    → §3.2 Chunk-Miss → Self-Observation delay when delta accumulates silently

📚 GAP + DIRECTION:
  → Gap-Direction.md v1.1 — gap has direction = f(surrounding chunks)
    → 4 properties, 2-layer model, unified Tier 1-4
    → "Not knowing something = no gap" principle
  → Cortisol-Baseline.md v2.0 §3.5 — chunk association tag (Shift mechanism)
  → Cortisol-Baseline.md v2.0 §3.8 — holding signal (Gap→Miss accelerator)

📚 OTHER FRAMEWORK:
  → Core-v7.8-Draft.md §1 — perception-action cycle
  → Core-v7.8-Draft.md §4 — unconscious processing (where dynamics fire)
  → Observation/Boredom.md — Chunk-Miss variant ⓑ (diffuse miss) + 2-direction formula
  → Observation/Novelty.md — Chunk-Gap = foundation mechanism
  → Observation/Connection.md §1.3 — 4 cases mapped to chunk dynamics
     (Sufficient=Chunk-Miss, Lost=Chunk-Miss++, Missing=Chunk-Gap, Toxic=Chunk-Shift)
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

> **END OF Body-Feedback-Mechanism.md v2.1**
>
> **Core mechanism reference for body-feedback chunk dynamics:**
>   §1: Body-need = aggregate output (v2.0)
>   §2: 2 input sources + Complexity Spectrum (v2.0)
>   §3: 3 chunk dynamics (restructured Gap sub-sections)
>   §4: Compound mechanism (Conditional Interaction Model)
>   §5: Quality Baseline Shift (SNC bridge)
>   §6: Framework maps (v7.8 + Body-Feedback-Precondition)
>   §7-§9: Research + Assessment + Cross-refs
>
> **Axis 4**: orthogonal to existing 3 axes (direction, magnitude, source).
> **Foundation**: Chunk-Gap = Novelty drive mechanism.
> **Key research**: SNC (Crespi 1942) proves Chunk-Miss at animal level.
> **v2.0 core additions**: Body-need aggregate + Complexity Spectrum +
>   Cross-cutting clarification.
