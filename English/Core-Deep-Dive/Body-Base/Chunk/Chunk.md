---
title: Chunk.md v3.0 — Unified Chunk System Reference
created: 2026-03-28 (v1.0 DRAFT)
updated: 2026-05-23 (v2.3 — Concept Cascade)
rewritten: 2026-06-01 (v3.0 — Architecture alignment: 1 Engine reframe, §2 trim→Compile-Taxonomy, §8 rewrite merge §8+§9+§10, §9-§12 renumber, +§0 positioning, +§2.7 Sleep Maintenance)
source_version: Vietnamese v3.0
english_created: 2026-06-06
status: v3.0
scope: |
  CORE REFERENCE FILE for the entire chunk system.
  WHAT chunks are + HOW chunks work internally.
  Compile ARCHITECTURE details → Compile-Taxonomy.md v3.0.
  Sleep MAINTENANCE details → Compile-Sleep.md v1.0.
  PFC OPERATIONS details → PFC-Operations.md v1.3.
  Synthesizes essence from 44+ files of deep analysis + 28-session drill propagation.
previous_version: backup/Chunk-v2.3-backup.md
parent: 99-Master-Synthesis.md (synthesis file), plan.md (master plan)
related:
  - Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators architecture
  - Compile-Sleep.md v1.0 — Sleep Maintenance (6 mechanisms)
  - Background-Pattern.md v2.0 — accumulated chunk bias
  - Agent-Mechanism/ (11 files) — per-entity chunk dynamics
  - Body-Base.md v3.3 — entry point, Compilable Architecture
  - PFC-Operations.md v1.3 — Hold/Suppress, PFC budget
  - Body-Feedback-Precondition.md v1.0 — 5 preconditions for body-feedback
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Speculative
---

# Chunk.md v3.0 — Unified Chunk System

> **Chunk = strength-weighted associative network compiled through experience.**
> The brain does NOT compute — the brain SEARCHES a database.
> Database = chunks. Operators = unconscious (95%) + PFC (5%).
>
> This file = CORE REFERENCE for the entire chunk system.
> WHAT chunks are + HOW chunks work internally.
> Architecture details → Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0.
>
> **4-Phase Lifecycle:** Compile → Install → Process → Plan
> "Humans need to FEEL correctly → AI will help PLAN correctly."

---

## Table of Contents

- §0 — Position in Framework
- §1 — What is a Chunk
- §2 — Chunk Compilation
- §3 — Chunk Connections (4 Types)
- §4 — Activation Dynamics (Core Mechanism)
- §5 — Anchor-Decay Model
- §6 — Labels + Logic-Planning Enablement
- §7 — Discovery Lifecycle (7 Steps)
- §8 — Operators × Chunk System
- §9 — Expert vs Beginner
- §10 — Honest Assessment
- §11 — Cross-References

---

## §0 — Position in Framework

```
⭐ CHUNK.MD = CORE REFERENCE — WHAT + HOW:

  This file answers:
    WHAT: What is a chunk? (§1)
    HOW:  How do chunks compile, connect, activate, decay, label, lifecycle? (§2-§7)
    WHO:  Who operates on chunks? (§8)
    WHO:  How does expert differ from beginner? (§9)

  Architecture details → COMPANION FILES:
    Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators + 3 Compile Types
    Compile-Sleep.md v1.0 — Sleep Maintenance (6 mechanisms, offline system)
    PFC-Operations.md v1.3 — Hold/Suppress, 4 combinations, PFC budget
    Body-Feedback-Precondition.md v1.0 — 5 preconditions for body-feedback signal

  CHUNK/ FOLDER (4 files + 1 subfolder):
    Chunk.md (this file) — core reference
    Compile-Taxonomy.md — compile architecture
    Compile-Sleep.md — sleep maintenance
    Background-Pattern.md — accumulated invisible bias
    Agent-Mechanism/ (11 files) — per-entity chunk dynamics

  READING FLOW:
    Chunk.md (core) → Compile-Taxonomy.md (architecture) → Compile-Sleep.md (sleep)
    Parallel: Agent-Mechanism/ for entity dynamics, Background-Pattern for bias
```

---

## §1 — What is a Chunk

### §1.1 — Definition

```
⭐ CHUNK = STRENGTH-WEIGHTED ASSOCIATIVE NETWORK:

  🟢 Hebb (1949): "Neurons that fire together, wire together"

  → Chunk = group of neurons already wired together → fire as 1 UNIT
  → NOT binary (present/absent) → but GRADIENT (weak → strong)
  → 🟢 Compile-Gradient (F1 04 §6.4): Proto-chunks = weak chunks, NOT "pre-chunks"
    → Behavioral "switch on" = thresholding artifact
    → Strengthen through repetition, emotional peak, multi-modal, sleep

  STRENGTH LEVELS:
    Proto-chunk:  Weak — fire sometimes, partial pattern-match
    Compiled:     Medium-strong — fire reliably, holdable in WM
    Meta-chunk:   Strong — many sub-chunks merged → fire as 1 unit
    → Expert: [DRIVING] = 1 meta-chunk = all automatic → PFC freed
    → Beginner: [steering]+[braking]+[mirror]+[signaling] = 4 chunks → PFC overloaded
    → 🟢 Chase & Simon 1973: expert chess 50,000+ chunk patterns

  → = SUBSTRATE LAYER of cognitive architecture (Chunk-Substrate 🟡🟢)
  → Everything runs on chunks: feeling, thinking, planning, identity

  ENTITY-COMPILED = NEURAL REALITY (Entity-Compiled.md v1.0):
    → When compiled deeply enough for 1 entity (40–200h) → hub-and-spoke network
    → Entity IS REAL in the brain (amygdala/hippocampus/PFC per-entity)
    → Dunbar ~150: limit of Entity-Compiled capacity
    → Grief = loss of neural reality, NOT abstract "sadness"
    → = Chunks compiled strongly enough per-entity → become Entity-Compiled

  ⚠️ NO SOURCE TAG (Drill §10 — GAP 8):
  → Wire = wire. The body treats ALL chunks EQUALLY regardless of where they were compiled.
  → Internal compile (self-experience) vs external install (culture/trust)
    = SAME format. NO "source origin" field.
  → PFC cannot distinguish → confabulation (PFC-Function §6, Valence-Propagation §7).
  → Detail: Valence-Propagation §1 ④ (no source tag), Drill §10.
```

### §1.2 — Multi-modal from birth

```
🟡🟢 CHUNKS = MULTI-MODAL FROM THE START:

  The "mother" chunk = face (visual) + voice (auditory) + embrace (somatic) + warmth (emotional)
  → Fire 1 part (hearing the voice) → PULLS the whole chunk (recalls the face, the embrace,...)
  → 🟢 Distributed representations (Rumelhart & McClelland 1986)

  MULTI-MODAL BINDING = emergent, NO single binder module:
    🟡 Emergent-Binding (F1 07 §6): 4 concurrent mechanisms:
      ① Temporal co-occurrence + Hebbian binding (🟢 Bliss & Lømo 1973)
      ② Multisensory neurons (🟢 Stein & Meredith 1993)
      ③ Default Mode Network scaffolding (🟡 Doria 2010)
      ④ Amygdala emotional tagging (🟡 LeDoux 2012)

    → NO single binder module (🟢 negative claim — F1 rejects dedicated binding module)
    → Binding = system property, not a step
    → Analogy: "chord sounds harmonious" — no "harmony step", system property

  NEWBORNS ALREADY HAVE multi-modal binding:
    → E12 social smile 6-8 weeks = requires all 4 mechanisms
    → Blind infant smile ~8 weeks via non-visual cues = chunks-based, not mirror-based
    → 🟢 Substrate-level binding from birth (multisensory neurons + DMN)
    → Compiled chunks ADD specificity on top of substrate

  → Detail: F1 07-Social-Recognition-Arc.md §6
```

### §1.3 — Pattern Hierarchy: Pattern ⊃ Chunk / Schema / Background-Pattern / Label

```
⭐ PATTERN = MOST GENERAL SUBSTRATE (Drill §18 Q-NEW-1):

  Pattern = any configuration of neural activity (firing + wiring).
  = The MOST GENERAL concept in the framework.
  = Chunk, Schema, Background-Pattern are ALL patterns.
  = NOT parallel concepts — but CONTAINS the concepts below.


HIERARCHY — 4 TIERS:

  ┌────────────────────────────────────────────────────────────────┐
  │  CONCEPT           │ DEFINITION               │ ANALOGY       │
  ├────────────────────────────────────────────────────────────────┤
  │  PATTERN           │ Any configuration of     │ Sound         │
  │  (most general)    │ neural activity           │               │
  │                    │ (firing + wiring)         │               │
  ├────────────────────────────────────────────────────────────────┤
  │  CHUNK             │ Compiled pattern unit     │ Function      │
  │  (atom)            │ = neurons wired together  │ (compiled,    │
  │                    │ fire as 1 unit            │  reusable)    │
  ├────────────────────────────────────────────────────────────────┤
  │  SCHEMA            │ Named chunk-network       │ Module / API  │
  │  (observation      │ + purpose                 │               │
  │   label)           │ = observation label       │               │
  ├────────────────────────────────────────────────────────────────┤
  │  BACKGROUND        │ Accumulated pattern,      │ OS kernel     │
  │  PATTERN           │ high link density,        │ (invisible    │
  │  (invisible)       │ invisible to PFC          │  processes)   │
  ├────────────────────────────────────────────────────────────────┤
  │  LABEL             │ Retrieval tag for         │ Function name │
  │  (access path)     │ chunk/pattern/schema      │               │
  └────────────────────────────────────────────────────────────────┘


FORMAL RELATIONSHIPS:

    Pattern ⊃ {Chunk, Schema, Background-Pattern, ...}
    Chunk ∈ Pattern (chunk is the compiled unit OF pattern)
    Schema ⊂ Pattern (every schema is a pattern, NOT vice versa)
    Label → Chunk/Pattern/Schema (label POINTS TO, not the content itself)


RECURSIVE COMPILATION:

    Pattern → compile → Chunk → participates in new Pattern → compile → Meta-chunk → ...
    = Pyramidal compression (PFC-Analysis.md)
    = Core of Blackbox (Blackbox-Map.md §4)


DETAIL PER LEVEL:

  CHUNK = ATOM:
    → 1 unit of associative network, compiled, fires as 1 unit
    → No purpose of its own
    → Example: chunk [brake press]

  SCHEMA = MOLECULE:
    → Multiple chunks linked → with PURPOSE/FUNCTION
    → Example: schema [driving] = chunk network → PURPOSE: moving
    → Detail: Schema.md §1.1

  BACKGROUND PATTERN = OS KERNEL:
    → Accumulated from many experiences → high link density
    → Fires ALL THE TIME but PFC CANNOT see it (invisible)
    → Example: "how I react under pressure" = Background-Pattern
    → Detail: Background-Pattern.md

  LABEL = HANDLE:
    → Verbal/symbolic tag ATTACHED to chunk (NOT part of chunk content)
    → Label = retrieval path, NOT 5th modality (Label-As-Handle 🟡)
    → Label does NOT change content — changes ACCESSIBILITY
    → 5 handle systems: gestural, action, image, verbal, internal-only
    → Detail: §6, F1 08 §5

  → Pattern = SUBSTRATE. Chunk = COMPILED UNIT. Schema = STRUCTURE.
  → Background-Pattern = INVISIBLE SUBSTRATE. Label = ACCESS PATH.

  🟡 Hierarchy formalization — Drill §18, logic consistent with Hebb + Collins & Loftus
```

---

## §2 — Chunk Compilation

### §2.1 — Compile Architecture: 1 Engine + Modulators

```
⭐⭐ CORE THESIS (Compile-Taxonomy.md v3.0):

  ALL compilation goes through 1 single pathway:

    EXPOSURE → HEBBIAN STRENGTHENING → COMPILED CHUNK

  There is no separate "trust compile mechanism."
  There is no separate "expertise compile mechanism."
  ONLY 1 ENGINE (Hebbian LTP). Differences = which MODULATOR is dominant.

  4 COMPILE MECHANISMS = 4 FORMS OF EXPOSURE (same 1 Engine):

  ┌────────────────┬──────────────────────┬─────────────────────────┐
  │ Mechanism      │ = Exposure form      │ Why it compiles         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ① Repetition   │ Repeated exposure    │ Co-fire many times      │
  │                │ many times           │ → connections strengthen │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ② Emotional    │ EXTREME intensity    │ Amygdala + NE → wire    │
  │    peak        │ exposure (once is   │ EXTREMELY FAST          │
  │                │ enough)              │                         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ③ Multi-modal  │ Exposure across      │ Cross-cortex co-fire    │
  │                │ MANY CHANNELS        │ → richer binding        │
  │                │ at once              │                         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ④ Sleep        │ Replay exposure      │ Hippocampus replay      │
  │                │ OFFLINE (6 mechs)    │ → strengthen/prune      │
  └────────────────┴──────────────────────┴─────────────────────────┘

  3 COMPILE TYPES = DOMINANT MODULATOR CONFIGURATIONS:
    Experience = Engine + minimal modulators (direct exposure)
    Trust      = Engine + Entity-Valence amplifier (Entity-Valence-dominant)
    Expertise  = Engine + PFC sustained hold (PFC-dominant)

  3 MODULATORS:
    Entity-Valence Bias — automatic, cost ≈ 0, trust = multiplier per-entity
    PFC Modulation — Hold + Suppress, costly, finite budget
    3 Exposure Channels — External / Deliberate / Spontaneous (parallel)

  NO SOURCE TAG = EVIDENCE FOR 1 ENGINE (§1.1):
    Compiled chunks have NO source origin tag.
    ALL go through the same 1 engine → products are EQUAL in the body.

  🟢 Hebbian learning: Hebb 1949
  🟢 LTP: Bliss & Lømo 1973
  🟢 Aplysia conserved: Kandel 2000
  🟡 "ALL compile = exposure" unifying principle: Compile-Taxonomy.md v3.0
  → Detail architecture: Compile-Taxonomy.md v3.0 §1
```

### §2.2 — 5-parameter compile rate formula

```
🟡🟢 Compile-Rate-Formula EXTENDED (F1 06a §6 + 07 §6.4):

  compile_rate ≈ f(exposure × saliency × contingency
                   × peak_valence × multi_modal_richness)

  → Cross-state 5-for-5 ordinal validation (bladder/hunger/pain/thermal/emotional)
  → Formula correctly predicts EVERY body state's development timing
  → No inversions observed

  EXAMPLES:
    Hunger:  High contingency + valence → fast compile (~18mo L4)
    Bladder: Moderate across all → moderate (~22mo L4)
    Thermal: All parameters low → truncated (rarely L4 by 24mo)

  → = Individual variation EXPLAINED:
    Different environments → different parameter values → different outcomes
  → = NOT "innate talent" → but "different compile environments"
```

### §2.3 — External install + Trust = Amplifier

```
🟡 BEYOND 4 internal mechanisms, chunks ALSO installed from OUTSIDE:

  5 EXTERNAL INSTALL MECHANISMS (F3):
    ① Co-attention — joint focus on same object/event
    ② Imitation — observe and reproduce
    ③ Social referencing — "caregiver feels how about this?"
    ④ Label installation — verbal label attaches to existing chunk
    ⑤ Cultural transmission — vertical/horizontal/oblique channels

  → Age-independent: same mechanisms at 9 months and 40 years
  → = Direction B: culture → individual
  → = Education = BATCH Direction B installation

  4 EDUCATION FAILURE MODES:
    ① Shallow compile (repetition without multi-modal)
    ② Threat context (cortisol direction wrong → Direction-At-Compile)
    ③ No Imagine-Final (no body-need connection → no motivation)
    ④ Conflict (installed chunks contradict existing chunks)

  → Detail: F3 00-External-Mechanism.md, F3 01-External-Synthesis.md


⭐ TRUST = AMPLIFIER (GRADIENT), NOT A GATE (BINARY):

  CONTENT compiles through exposure ALONE — trust NOT required.
  Trust amplifies VALUE compile rate from external source.
  "Gate" = limit case when multiplier → 0.
  Compile = "Body receives experience → unconscious auto-wires." Trust amplifies, does not gate.

  TRUST SCOPE — VALUE vs CONTENT (Compile-Taxonomy.md v3.0 §3.3):
    Content compile: Trust does NOT amplify (Compile Engine alone is sufficient)
    Value compile:   Trust AMPLIFIES ([X → good/bad] installs faster)
    Entity compile:  Trust weight itself = product of compile from experience
    → "Good at it but hates studying" = content ✓, value ✗ = architecture prediction

  ENTITY-ACCESS GRADIENT (Entity-Access.md v1.2):
    Level 0 (stranger, multiplier ≈ 0) → Level 5 (self/child, multiplier MAX)
    Trust = 1 dimension WITHIN the valence profile per-entity (Valence-Propagation v4.1 §2)
    → Detail calibration: Entity-Access-Calibration.md v1.0
    → Detail excess: Entity-Access-Excess.md v1.0

  → Detail trust architecture: Compile-Taxonomy.md v3.0 §3
  → Detail trust mechanism: Valence-Propagation v4.1 §2
  → Detail trust break: §4.3 (competitive re-linking)

  🟡 Trust amplifier — Compile-Taxonomy.md v3.0 §3
```

### §2.4 — Body-state at compile (direction matters)

```
🟡🟢 Direction-At-Compile (F1 06a §7 + 06b §6.3):

  ⭐ NOT "good stress/bad stress" — BUT "WHICH DIRECTION":

  NOVELTY DIRECTION (positive):
    → Curiosity, exploration, positive challenge
    → Cortisol present but body interprets = "interesting, want to know more"
    → Chunks compile WITH approach association
    → = Expert formation, creativity, growth

  THREAT DIRECTION (negative):
    → Fear, avoidance, imposed stress
    → Cortisol present AND body interprets = "dangerous, avoid"
    → Chunks compile WITH avoidance association
    → = Trauma formation, phobia, learned helplessness

  → SAME cortisol level → DIFFERENT direction → COMPLETELY DIFFERENT outcome
  → "Cortisol is NOT the enemy" — novelty-cortisol IS BENEFICIAL

  4-THRESHOLD GRADIENT:
    Mild:     Body adapts quickly → minimal impact
    Moderate: Optimal zone → strongest compile
    Heavy:    Hardware stress → compile BUT with damage risk
    Extreme:  Overwhelming → shutdown → minimal useful compile

  NEURAL WEAR compounds MULTIPLICATIVELY:
    → ACE dose-response (🟢 Felitti 1998)
    → Physical × social × anticipation sources
    → Domain × peer × imposed-adult × self-generated origins

  → Detail: F1 06a-Interoceptive-Bladder.md §7, F1 06b §6.3
```

### §2.5 — Reconsolidation + No deletion

```
🟢 RECONSOLIDATION (Nader 2000):
  → Chunk recalled → TEMPORARILY unstable (~4–6 hours)
  → Within window → CAN modify → re-compile
  → = Therapy mechanism: recall → reframe → re-compile

  ⚠️ Recall WITHOUT modifying → chunk STRENGTHENS → WORSE
  → 🟢 Rumination worsens depression (Nolen-Hoeksema 2000)

🟢 NO ONE CAN DELETE A CHUNK:
  → There is no active "unwire" mechanism
  → Chunks only: STRENGTHEN / WEAKEN / MODIFY — CANNOT delete
  → "Breaking old habits" = NEW chunk compiled STRONG ENOUGH → SUPPRESSES the old chunk
  → Stress → PFC weakens → old chunk CAN fire again ("relapse under fatigue")

GRADIENT COMPILE (Compile-Gradient + R-F1-10):
  → Compile is gradient, not discrete
  → Non-uniform progression across arcs
  → Each chunk = different compile stage at any given time
  → Proto-chunks = legitimate intermediate states
```

### §2.6 — Context-tag: 4 metadata types at compile

```
⭐ FRAMEWORK FORMALIZATION — CHUNK CONTEXT-TAG:

  When a chunk compiles, hippocampus + amygdala attach 4 METADATA TYPES:

  ┌──────────────────────────────────────────────────────────────┐
  │  METADATA        │ QUESTION    │ BRAIN REGION  │ EXAMPLE    │
  ├──────────────────────────────────────────────────────────────┤
  │ ① TEMPORAL       │ WHEN?       │ Hippocampus   │ "Year 2020"│
  │   (time stamp)   │             │ (CA1)         │            │
  │ ② SPATIAL        │ WHERE?      │ Hippocampus   │ "Intersection X"│
  │   (location)     │             │ (place cells) │            │
  │ ③ CAUSAL         │ WHY?        │ Hippocampus   │ "Car ran   │
  │   (narrative)    │ HOW?        │ + PFC         │  red light"│
  │ ④ STATE          │ BODY STATE? │ Amygdala +    │ "Fear, pain│
  │   (body state)   │             │ Insula        │  heart↑"   │
  └──────────────────────────────────────────────────────────────┘

  HIPPOCAMPUS attaches ①②③. AMYGDALA attaches ④.

  ⭐ CHUNK CONTENT ≠ CHUNK CONTEXT-TAG:
    Content = what happened (sensory, motor, emotional fragments)
    Context-tag = when/where/why/body-state (metadata)
    → Content determines WHAT fires
    → Context-tag determines HOW retrieval FEELS:
      4/4 metadata → "recalling" (remembering — bounded, past)
      State only → "reliving" (re-experiencing — unbounded, present)

  2 CHUNK TYPES (based on context-tag quality):

    CONTEXTUAL CHUNK (hippocampal pathway):
      → 4/4 metadata → bounded, declarative, malleable
      → Supports reconsolidation (§2.5) and extinction learning
      → = Normal emotional memory. "Recalling."
      → 🟢 Brewin 2010: C-rep (contextualized representation)

    CONTEXT-FREE CHUNK (amygdala pathway):
      → ④ State only → unbounded, implicit, RESISTANT, cue-bound
      → Resistant to extinction (🟢 Bouton 2004: extinction ≠ erasure)
      → Amygdala low road ~12ms → body responds BEFORE PFC arrives (~200ms+)
      → = Trauma memory. "Reliving."
      → 🟢 Brewin 2010: S-rep (sensation-based representation)

  CONTEXT-TAG QUALITY = SPECTRUM (not binary):
    Full (4/4) = normal → Partial (1-3) = stressful → State only = trauma
    → Treatment = SHIFT LEFT: hippocampus RE-ATTACHES missing metadata
    → Content UNCHANGED. Metadata CHANGED. Body response CHANGED.

  RELATIONSHIP TO §1.1 — NO SOURCE TAG:
    Source tag ("who created chunk?") = ABSENT (§1.1 — still holds)
    Context tag ("when/where compiled?") = PRESENT (hippocampal metadata)
    → 2 different questions. Body does not know SOURCE. Body HAS or LACKS CONTEXT.

  RELATIONSHIP TO §4.2 — link strength factors:
    §4.2 ⑤ CONTEXT MATCH = retrieval-time: current context ~ compile context → boosted
    §2.6 context-tag = compile-time: metadata ATTACHED during encoding
    → §4.2 ⑤ = "chunk EASIER to find when context matches"
    → §2.6 = "chunk HAS or LACKS context from the start"

  🟢 Kim & Diamond 2002: hippocampal suppression under extreme stress
  🟢 LeDoux 1996/2000: dual pathway (low road ~12ms vs high road ~200ms)
  🟢 Brewin 2010: Dual Representation Theory (C-rep vs S-rep)
  🟢 Tulving 2002: hippocampus binds "what-where-when"
  🟡 4 metadata types as formal taxonomy = framework synthesis
  🔴 Context-free chunk as explicit chunk TYPE = hypothesis (testable)
  → Detail: PTSD-Analysis.md §2-§3, §14
```

### §2.7 — Sleep Maintenance (Offline System)

```
⭐ SLEEP ≠ "4TH EXPOSURE SOURCE" — SLEEP = OFFLINE MAINTENANCE SYSTEM:

  Sleep has 6 mechanisms — only ~1.5 are exposure-based, ~4.5 are optimization:

  ┌────┬──────────────────────┬─────────────┬──────────────────────┐
  │ #  │ Mechanism             │ Exposure?   │ Primary function     │
  ├────┼──────────────────────┼─────────────┼──────────────────────┤
  │  1 │ SHY Homeostasis       │ ❌ NOT      │ Prune weak (SNR)     │
  │  2 │ Hippocampal Replay    │ ✅ YES      │ Strengthen existing  │
  │  3 │ Active Consolidation  │ ❌ NOT      │ Transfer (RAM→ROM)   │
  │  4 │ Creative Linking      │ 🟡 PARTIAL  │ New remote links     │
  │  5 │ Emotional Decoupling  │ ❌ NOT      │ Strip emotional tag  │
  │  6 │ Gist Extraction       │ 🟡 PARTIAL  │ Abstract+generalize  │
  └────┴──────────────────────┴─────────────┴──────────────────────┘

  Cycle: Waking (build) → Sleep (maintain) → Waking (build on maintained).
  Sleep deprivation = ALL 6 mechanisms disrupted → PFC degrades FIRST.
  "Clearer tomorrow morning" = unconscious HAS ALREADY pruned + consolidated + abstracted.

  🟢 Multi-mechanism sleep: Diekelmann & Born 2010
  🟡 Sleep Maintenance in compile architecture: Compile-Sleep.md v1.0
  → Detail 6 mechanisms + architecture interaction: Compile-Sleep.md v1.0
```

---

## §3 — Chunk Connections (4 Types)

### §3.1 — Complete taxonomy

```
🟡 Static-Logical-Linking SUPPORTED (F4 01):

  ┌───────────────────────────────────────────────────────────────────┐
  │ TYPE │ NAME                │ MECHANISM            │ PFC ROLE     │
  ├───────────────────────────────────────────────────────────────────┤
  │  1   │ Shared              │ Overlapping neurons  │ None         │
  │      │ Contamination       │ fire into each other │ (automatic)  │
  ├───────────────────────────────────────────────────────────────────┤
  │  2   │ Aha Moment          │ DMN incubation →     │ Observer     │
  │      │ (Insight)           │ sudden burst link    │ (surprised)  │
  ├───────────────────────────────────────────────────────────────────┤
  │  3   │ Meta-chunk          │ Repeated co-firing → │ Weak         │
  │      │ Compile             │ merge into unit      │ (repetition) │
  ├───────────────────────────────────────────────────────────────────┤
  │  4   │ Static Logical      │ PFC hold + overlap   │ Active       │
  │      │ Linking              │ check + body vote    │ (intentional)│
  └───────────────────────────────────────────────────────────────────┘

  8-DIMENSION DISTINCTION (trigger, PFC role, tempo, awareness,
    body signal, output, reversible, trainable):
    → Type 4 differs from ALL 3 types on MOST dimensions
    → Type 4 = ONLY type where PFC ACTIVELY drives the process
```

### §3.2 — Type details

```
TYPE 1 — SHARED CONTAMINATION:
  → 2 chunks SHARE neurons → fire into each other
  → UNCONSCIOUS, automatic, no PFC required
  → 🟢 Spreading activation (Collins & Loftus 1975)
  → Healthy: [love → excitement → eagerness]
  → Pathological: [love → excitement → fear of abandonment] (trauma contamination)

TYPE 2 — AHA MOMENT:
  → Chunks SIMMERING in background → suddenly LINK in a NEW way
  → Cannot be forced — can only CREATE CONDITIONS (incubation)
  → 🟢 Gamma burst (Kounios & Beeman 2009)
  → Reward = opioid (body-need match), NOT dopamine
    → Dopamine = salience alert ("doorbell")
    → Opioid = actual reward ("gift behind the door")
    → 🟢 Berridge 2003: dopamine = wanting, opioid = liking
  → Intensity ∝ (schemas resolved × threat relief if present)

TYPE 3 — META-CHUNK COMPILE:
  → Many chunks fire together MANY TIMES → merge into 1 UNIT
  → 🟢 Hebbian: "fire together, wire together"
  → Expert: 50,000+ patterns = meta-chunks → PFC freed
  → Gradual, through repetition → hierarchy: chunks → meta → schemas

TYPE 4 — STATIC LOGICAL LINKING (Static-Logical-Linking 🟡):
  → PFC DELIBERATELY holds chunk A + chunk B → checks overlap → body vote
  → = "THINKING" = chaining Type 4 connections
  → Body vote 3 outcomes:
    → Smooth: "connects, relevant" (coherent overlap)
    → Resistance: "something's off, contradiction" (ACC conflict)
    → Empty: "not related" (no overlap)
  → CAN trigger Type 2 (deliberate search → sudden insight)
  → CAN lead to Type 3 (repeated linking → compilation)
  → 5 failure modes: confirmation bias, WM overload, trauma noise,
    false smoothness (beginner), premature closure
```

### §3.3 — Interaction ecosystem

```
  4 TYPES = ECOSYSTEM, not isolated mechanisms:

    Type 1 → provides substrate for → Type 4 (spreading activation = search tool)
    Type 4 → can trigger → Type 2 (deliberate search → sudden insight)
    Type 4 → can lead to → Type 3 (repeated linking → compilation)
    Type 2 → strengthens → Type 1 (new link = new co-firing potential)
    Type 3 → frees capacity for → Type 4 (compiled chunks = more WM space)

  → Detail: F4 01-Chunk-Connection-Logical.md
```

---

## §4 — Activation Dynamics (Core Mechanism)

### §4.1 — Activation probability distribution

```
🟡 FRAMEWORK SYNTHESIS from established neuroscience (F4 01b §2):

  ⭐ ACTIVATION = PROBABILITY-WEIGHTED, not binary:

  When chunk X fires:
    → Spreading activation propagates OUTWARD along ALL links
    → Each link has DIFFERENT STRENGTH
    → Activation DISTRIBUTES according to strength:

    Chunk X fires →
      40% → Chunk A (strong link: many times, recent, multi-modal)
      25% → Chunk B (medium link)
      15% → Chunk C (medium link)
      10% → Chunk D (weak link: old, rarely used)
       5% → Chunk E (very weak link)
       5% → scattered (noise, sub-threshold)

    → Chunks that receive ENOUGH activation (exceed threshold) → fire
    → Chunks that receive INSUFFICIENT → partial activation
      (contribute to Multi-Weak-Signal-Convergence but do not fire independently)

  → = "When thinking about X, I mostly think of A"
  → = NOT because X→A is the ONLY link
  → = But because X→A is the STRONGEST link → most probable activation
  → 🟢 Spreading activation probability-weighted (Collins & Loftus 1975)
  → 🟢 Priming (Meyer & Schvaneveldt 1971, Neely 1977)
```

### §4.2 — 7-factor link strength

```
LINK STRENGTH = f(7 factors):

  ① REPETITION COUNT — how many times fired together (🟢 Hebbian)
  ② RECENCY — how long ago it last fired (🟢 recency effect)
  ③ EMOTIONAL WEIGHT AT COMPILE — emotional peak → EXTRA STRONG
     → 1 trauma event CAN be > 100 neutral repetitions
  ④ MULTI-MODAL RICHNESS — more modalities → more neurons → stronger
  ⑤ CONTEXT MATCH — current context ~ compile context → BOOSTED
     → 🟢 Context-dependent memory (Godden & Baddeley 1975)
  ⑥ EMOTIONAL STATE MATCH — current emotion ~ compile emotion → BOOSTED
     → 🟢 Mood-congruent memory (Bower 1981)
     → Currently afraid → fear-compiled links boosted → "seeing danger everywhere"
  ⑦ ANCHOR STRENGTH — active anchor → link MAINTAINED
     → Weak/no anchor → link gradually DECAYS (§5)

  ⭐ FACTORS INTERACT MULTIPLICATIVELY:
    High all → EXTREMELY strong (nearly permanent): mother's name, driving skill
    Low all → EXTREMELY weak (rapid decay): a phone number heard once
    High emotion + low anchor → STRONG initially but DECAYING
```

### §4.3 — Competitive re-linking

```
🟡 HOW NEW LINKS COMPETE WITH OLD LINKS (F4 01b §3):

  NOT "delete old link, replace with new link":
  BUT "new link COMPETES with old link":

  ① New link forms (via any compile mechanism)
  ② New link strengthens with repetition
  ③ Old link weakens (Ebbinghaus decay + lateral inhibition)
     → 🟢 Retrieval-induced forgetting (Anderson et al. 1994)
  ④ Probability crossover: P(new) > P(old)
     → New pathway DOMINATES body signal
  ⑤ Stabilization: old pathway fires so weakly → mostly sub-threshold
     → BUT NEVER fully gone → stress can REACTIVATE
     → 🟢 Stress-induced relapse (Sinha 2001)

  RECONSOLIDATION AS COMPETITION ENABLER (🟢 Nader 2000):
    → Trigger old chunk → window opens (~4-6h)
    → In window: provide NEW experience → new links integrate
    → = Faster, more effective probability shift
    → = THIS IS WHY EXPOSURE THERAPY WORKS
    → 🟢 Schiller et al. 2010: reconsolidation-based extinction

  3 RE-LINKING STRATEGIES (same mechanism, different speed):
    Strategy 1 — Re-associate: gradual positive experience → SLOW, LOW risk
    Strategy 2 — Novelty hijack: curiosity context → FAST, MODERATE risk
    Strategy 3 — Therapy-assisted: professional reconsolidation → DEEPEST, HIGHEST risk
```

### §4.4 — Trigger surface

```
🟡 TRIGGER SURFACE = total entry points that can activate a chunk (F4 01b §4):

  TRIGGER SURFACE SIZE = f(4 factors):
    ① Number of MODALITIES in chunk
    ② Number of ASSOCIATED chunks
    ③ EMOTIONAL INTENSITY at compile
    ④ GENERALITY vs specificity of pattern

  ⭐ TRAUMA = LARGE trigger surface + THREAT direction:
    → Multi-modal + emotional peak + generalized pattern
    → Many entry points → high random activation → frequent intrusions
    → = "Vaguely afraid of something without knowing exactly what"

  ⭐ EXPERTISE = LARGE trigger surface + NOVELTY direction:
    → Multi-modal + deep engagement + many cross-links
    → Many entry points → high domain-relevant activation → accurate intuition
    → = Klein 1998 firefighter: large trigger surface → many chunks fire → gut feeling

  ⭐ TRAUMA = EXPERTISE = SAME MECHANISM, DIFFERENT DIRECTION:
    Trauma:    large trigger surface + threat → fear/avoidance
    Expertise: large trigger surface + novelty → insight/competence
    → = Direction-At-Compile confirmed: DIRECTION matters, not mechanism

  TRIGGER SURFACE REDUCTION:
    → Natural: new environment + positive chunks → narrows over time
    → Therapeutic: systematic safe experience at each entry point
    → NEVER reaches zero — goal is SUFFICIENT probability shift
    → "Still slightly uncomfortable but manageable" = success

  ⚠️ TRIGGER SURFACE GROWTH OVER TIME (Link Density):
    → Trigger surface is NOT ONLY determined at compile time
    → Pattern exists LONG ENOUGH → NEW chunks link in → TS GRADUALLY GROWS
    → Chronic patterns: TS grows over years even without new events
    → = "Background-Pattern" — accumulated bias invisible to PFC
    → Detail: Background-Pattern.md (2D model: Depth × Link Density)

  → Detail activation dynamics: F4 01b-Chunk-Activation-Dynamics.md
```

### §4.5 — Probability is dynamic

```
⭐ DISTRIBUTION SHIFTS OVER TIME (not static):

  T=0 (trauma event):
    [dog] fires → 85% [bite, pain, fear] / 10% [fur, soft] / 5% noise

  T=5 years (gradual positive exposure):
    [dog] fires → 50% threat / 30% positive / 20% other

  T=15 years (resolved):
    [dog] fires → 20% old threat / 55% positive / 25% other
    → PFC: "afraid of dogs as a child, fine now, just be careful"
    → Body: mostly calm, slight alertness (old link fires weakly)
    → = FUNCTIONAL RESOLUTION (not deletion)

  → SAME mechanism for: learning, therapy, habit change, creativity,
    identity change, cultural change
  → = PROBABILITY SHIFT is THE fundamental chunk operation
```

---

## §5 — Anchor-Decay Model

### §5.1 — Anchor = retrieval path (not content)

```
🟡 Anchor-Decay SUPPORTED WITH REFINEMENT (F4 03):

  ⭐ CRITICAL DISTINCTION:
    Anchor = RETRIEVAL PATH to chunk (not part of chunk content)
    Chunk = content (neural pattern)
    Anchor = pointer (how to FIND that pattern)

  → "Forgetting" = retrieval path WEAK (chunk still exists)
  → "Losing" = substrate damage (rare — traumatic brain injury, neurodegeneration)
  → "Never had it" = chunk never compiled
  → 3-way distinction: forgetting ≠ losing ≠ never having
```

### §5.2 — 5 anchor types

```
  ┌──────────────┬────────────────────┬──────────────┬──────────────────┐
  │ Anchor Type  │ Mechanism          │ Versatility  │ Decay Rate       │
  ├──────────────┼────────────────────┼──────────────┼──────────────────┤
  │ Verbal       │ Word/label         │ HIGHEST      │ Moderate         │
  │              │ attached           │ (Grammar-    │ (needs rehearsal)│
  │              │                    │  Versatile-  │                  │
  │              │                    │  Anchor)     │                  │
  ├──────────────┼────────────────────┼──────────────┼──────────────────┤
  │ Contextual   │ Place/setting/     │ Moderate     │ Fast without     │
  │              │ people present     │              │ revisit          │
  ├──────────────┼────────────────────┼──────────────┼──────────────────┤
  │ Ritual       │ Action sequence    │ Low          │ SLOWEST          │
  │              │ + timing           │              │ (motor memory)   │
  ├──────────────┼────────────────────┼──────────────┼──────────────────┤
  │ Emotional    │ Feeling state      │ Moderate     │ Moderate         │
  │              │ at compile         │ (involuntary)│ (mood-dependent) │
  ├──────────────┼────────────────────┼──────────────┼──────────────────┤
  │ Multi-anchor │ 2+ types combined  │ VARIES       │ SLOWEST          │
  │              │                    │              │ (redundancy)     │
  └──────────────┴────────────────────┴──────────────┴──────────────────┘

  → Verbal = most VERSATILE (wins most dimensions)
  → Context = most POWERFUL per single activation
  → Ritual = most STABLE (motor memory slow decay)
  → Multi-anchor = most ROBUST (redundancy protects)
  → 🟡 Grammar = most versatile external anchor (Grammar-Versatile-Anchor — ~100K years refinement)
```

### §5.3 — Retrieval decay vs substrate decay

```
🟡 Anchor-Decay REFINEMENT:

  RETRIEVAL DECAY (Ebbinghaus applies):
    → Anchor weakens over time without rehearsal
    → 🟢 Ebbinghaus 1885 forgetting curve
    → Re-exposure → "oh I remember now!" = path reactivates
    → = "Forgetting" in common sense = retrieval loss

  SUBSTRATE DECAY (Ebbinghaus does NOT apply):
    → Actual neural pattern degradation
    → MUCH slower (years-decades for compiled chunks)
    → Emotional peak compiled = almost no substrate decay
    → Requires biological damage for rapid loss
    → = "Losing" in true sense = content gone

  → Meaning crisis = ANCHOR crisis (Vervaeke):
    When anchors COLLECTIVELY weaken → lose access to meaningful chunks
    → Chunks still exist → but cannot reach them
    → = "Knowing you once knew but can no longer recall"

  → Detail: F4 03-Chain-Anchor-Decay.md
```

### §5.4 — Compile depth × resistance: Alzheimer clinical validation

```
🟢 CLINICAL VALIDATION — "LAST IN FIRST OUT":

  Alzheimer-Analysis §5-§6: Alzheimer destroys chunk substrate → reveals pattern:
    → Recent chunks (SHALLOW compile) lost FIRST
    → Childhood chunks (DEEP compile) resist LAST
    → = Ribot's Law (1881) EXPLAINED by compile depth

  5 INDEPENDENT MECHANISMS all predict the same pattern:
    ① Memory consolidation: recent = hippocampus-dependent → destroyed first
    ② Compile depth × distribution: deep = more links = resistant
    ③ Activity-dependent tau: active connections release MORE tau → damaged first
    ④ Multiple Trace Theory: old = 100+ traces, recent = 2 (🟢 Nadel 1997)
    ⑤ Myelination order: late-myelinating = thin → vulnerable (🟢 Bartzokis 2004)

  = OVERDETERMINED: any 1 mechanism being correct → pattern REMAINS THE SAME
  = "Regardless of where the fire starts, the building collapses from the top floors."
  = Pattern = ARCHITECTURAL PROPERTY of the brain, not a specific cause
  = Alzheimer = reverse-engineering lens: erosion reveals chunk compile architecture

  COMPILE DEPTH = f(§2.2 formula) → predicts RESISTANCE:
    compile_depth ≈ f(exposure × saliency × contingency
                     × peak_valence × multi_modal_richness)
    → HIGH depth (childhood: many repetitions × emotional peak × multi-modal)
      → Many synaptic links × distributed across many regions → RESISTANT
    → LOW depth (recent: few repetitions × neutral × single-modal)
      → Few links × concentrated → VULNERABLE

  🟢 Terry 1991: synapse loss r=0.96 with cognitive decline
  🟢 Ribot 1881: temporal gradient of retrograde amnesia
  🟢 Nadel & Moscovitch 1997: Multiple Trace Theory
  🟢 Bartzokis 2004/2011: myelination order predicts vulnerability
  🟡 Compile depth = primary predictor of resistance = framework synthesis
  → Detail: Alzheimer-Analysis.md §5-§6, §17
```

---

## §6 — Labels + Logic-Planning Enablement

### §6.1 — Label = retrieval path + symbolic compression

```
🟡 Label-As-Handle (F1 08 §5):

  LABEL = verbal/symbolic tag attached to chunk:
    → NOT 5th modality (label ≠ part of chunk content)
    → NOT constitutive of chunks (chunks exist without labels)
    → = Enhancement layer: retrieval path + symbolic compression

  5 HANDLE SYSTEMS:
    ① Gestural (pointing, sign language)
    ② Action (procedural — "show me")
    ③ Image (visual representation)
    ④ Verbal (word/phrase — most versatile for general cognition)
    ⑤ Internal-only (felt sense, no external expression)

  MODERATE WHORFIAN CLAIM (Label-As-Handle §5.6):
    → Label DOES NOT change chunk content
    → Label DOES shape access patterns + reasoning paths
    → = Having word "saudade" doesn't CREATE the feeling
    → = But HAVING the word → easier to access, communicate, reason about

  PFC-LABEL VOCABULARY (PFC-Label.md v1.0):
    → 13 domains × 3-tier label system (framework vocabulary)
    → Companion to Body-Feedback-Label.md v2.0
    → = Standardized labels for the entire framework
```

### §6.2 — Label = logic-planning prerequisite

```
⭐ FORMALIZED (F4 01c §3):

  CHUNK BEFORE HAVING A LABEL:
    → Exists at neural level
    → CAN: influence body vote (Direction A), fire weakly, vague feeling
    → CANNOT: hold clearly in WM, Type 4 chain, communicate, cross-reference
    → = Functional status: BODY-ONLY influence

  CHUNK AFTER HAVING A LABEL:
    → Same content (label ≠ new content)
    → CAN: WM hold, Type 4 chain, communicate, cross-reference, PFC manipulate
    → = Functional status: BODY + LOGIC influence

  ⭐ LABEL = "TICKET OF ENTRY" to the planning system:
    WITHOUT label: chunk influences via body ONLY (Direction A)
    WITH label:    chunk influences via body + logic (Direction A + B)
    → = Label UNLOCKS PFC access, does not change content

  WHY LABELS NEED TO BE "CORRECT":
    → Wrong label → wrong link → misleads future reasoning
    → Example: calling "cortisol" = "stress hormone" → link [cortisol → bad]
    → WRONG: cortisol is a sustainer, novelty-cortisol is also positive
    → Label SHAPES future chunk connections (moderate Whorfian)
    → Choosing right label = critical for framework quality

  → Detail: F4 01c §2.6-§2.7, §3
```

### §6.3 — Anchor/Label 3-tier system

```
  Tier 1: INDIVIDUAL anchors (only 1 person knows)
    → Rich but non-shareable
    → Example: "that feeling that day" — only you know

  Tier 2: GROUP anchors (shared within community)
    → Lossy but shareable
    → Example: "feeling a bit sad" — group understands approximately

  Tier 3: GLOBAL anchors (cross-cultural, formal notation)
    → Abstract but universal
    → Example: "depression" — clinical definition, cross-cultural

  FIDELITY GRADIENT: Individual (rich) → Group (lossy) → Global (abstract)
  → Each level LOSES body-level detail but GAINS shareability
  → = Logic-Planning.md: 3-tier anchor system
```

---

## §7 — Discovery Lifecycle (7 Steps)

### §7.1 — Full lifecycle model

```
🟡 FRAMEWORK SYNTHESIS (F4 01c §2):

  ⭐ 7-STEP DISCOVERY CYCLE:

    ① ACCUMULATE ──→ ② VAGUE EMERGENCE ──→ ③ CURIOSITY DRIVE
         ↑                                         │
         │                                         ↓
    ⑦ REPEAT        ④ CLARIFY ←────────────────────┘
    (deeper)              │
         ↑                ↓
         │           ⑤ LABEL / ANCHOR
         │                │
         │                ↓
         └────────── ⑥ LOGIC-PLANNING ENABLEMENT

    Self-reinforcing cycle: each iteration = deeper + wider
    Same mechanism at ALL scales: child, scientist, civilization
```

### §7.2 — Steps explained

```
  ① ACCUMULATE: Body-input + social install → chunks library grows
     → Needs ENOUGH chunks → trigger surface large enough → convergence CAN happen

  ② VAGUE EMERGENCE (Convergence Zone):
     → Many chunks fire → activation OVERLAPS in a "zone"
     → This zone = NOT 1 chunk → but intersection of many paths
     → PFC detects "something is there" but CANNOT identify "what"
     → = Gendlin "felt sense" at mechanism level
     → = Multi-Weak-Signal-Convergence at concept level
     → Body: "vague", "something feels off", "there's something"

  ③ CURIOSITY DRIVE:
     → Convergence zone detected → NOVELTY signal (VTA)
     → Dopamine → approach motivation → "want to know!"
     → ⚠️ IF threat-compiled → BLOCK cycle (fear, not curiosity)
     → = Direction-At-Compile determines whether cycle CONTINUES or STOPS

  ④ CLARIFY:
     → Strategy A: Deliberate search (Type 4 — try connections → body vote)
     → Strategy B: Describe boundaries (triangulation from surrounding chunks)
     → Strategy C: External catalyst (AI/collaborator organize fragments)
     → = "Re-reading makes it clearer" = same chunks, better organized → coherent firing

  ⑤ LABEL / ANCHOR:
     → PFC searches verbal library → metaphor / description / coin new term
     → Body checks each candidate → smooth = keep, resist = try another
     → 🟡 Gap2-Language-Evolution: Gap 2 drives language evolution (coin words for unlabeled experiences)

  ⑥ LOGIC-PLANNING ENABLEMENT:
     → Label = "ticket of entry" → chunk enters planning system (§6.2)
     → AI era: AI amplifies step ⑥ (plan with labeled chunks at high speed)
     → BUT: AI CANNOT do steps ①-⑤ for human (cannot feel convergence zone)

  ⑦ REPEAT (deeper + wider):
     → New labeled chunk → new trigger surface → new convergence zones CAN emerge
     → Stronger, deeper, wider each iteration
     → = "Standing on the shoulders of giants" = inherit labeled chunks → extend frontier
```

### §7.3 — 2 fates of unlabeled convergence zone

```
  FATE A — PERSISTENT VAGUE (surrounding chunks still active):
    → Body INSISTS "there's something here" → will NOT let go
    → Dissonance persists → motivates KEEP SEARCHING
    → = Einstein: years of vague wrongness → eventually "spacetime"

  FATE B — FORGOTTEN (surrounding chunks deactivate):
    → Activation too weak → below PFC threshold
    → "Forgotten" = retrieval paths decay (NOT content lost)
    → CAN return later if reactivated

  → LABEL PREVENTS BOTH FATES:
    → Label = INDEPENDENT retrieval path
    → Even if surrounding chunks deactivate → label remains accessible
    → = Insurance against Fate B

  → Detail: F4 01c-Chunk-Discovery-Lifecycle.md
```

---

## §8 — Operators × Chunk System

### §8.1 — Two Operators: Unconscious + PFC

```
🟡 CHUNK = DATA. Two operators work with the SAME database:

  ⭐ UNCONSCIOUS = PRIMARY OPERATOR (~95% processing):
    → AUTO-COMPILE: experience → neurons wire → chunk forms
    → RUN compiled schemas: trigger match → automatic behavior
    → EVALUATE via body signals: reward / dissonance / satisfaction
    → BACKGROUND PROCESS: organizing while walking, consolidating during sleep
    → STRENGTHEN/WEAKEN automatically (Hebbian)

  ⭐ PFC = SECONDARY OPERATOR (~5% — but determines DIRECTION):
    → HOLD: keeps chunks active in WM (~4±1)
    → SUPPRESS: blocks compiled patterns currently firing
    → CREATE: imagine new chunk → body check → compile
    → MODIFY: recall → reconsolidation window → change → re-compile
    → DIRECT: choose attention → decides WHICH chunks fire

  → = "Unconscious builds the house (95%), PFC chooses WHERE TO BUILD (5%)"

  PFC HARDWARE ONLINE FROM PRENATAL (🟢 F1 01):
    5 pillars: Huttenlocher 1979, Doria 2010, Kouider 2013, Grossmann 2009, Hodel 2018.
    OLD: "PFC offline until X age." NEW: "PFC hardware online from birth — chunks missing."

  PFC-INFERENCE LADDER (🟡🟢 F1 01 + F1 10):
    L0 Reflex → L1 Orienting → L2 Pattern-match → L3 Deliberate → L4 Coordinated
    = EVENT property, not AGE property. Same person at different L-levels per domain.

  SIMULATION-ENGINE = FORMALIZED PFC MECHANISM (Simulation-Engine.md v1.1):
    → 1 Engine, 3 Components: Interoceptive Model × Simulation × Self-Pattern-Modeling
    → Detail: Simulation-Engine.md v1.1, PFC-Operations.md v1.3
```

### §8.2 — PFC Operations: Hold + Suppress

```
🟡🟢 PFC-OPERATIONS.MD v1.3 — FORMALIZED MODEL:

  2 OPERATIONS:
    HOLD = amplify target pattern → INCREASES exposure quality
      Cost: ① PFC draft (processing load). CAN compile into automatic.
    SUPPRESS = block existing pattern → REDUCES exposure for specific pattern
      Cost: ② Efference mismatch. CANNOT compile "not" (Wegner 1987).

  4 COMBINATIONS (PFC-Operations.md v1.3 §3):
    ① Hold only         → easiest, body open → Genuine Shift
    ② Hold + Suppress   → double cost → 3 possible outcomes
    ③ Suppress only     → worst strategy, ALWAYS fails long-term
    ④ Neither           → compiled auto-fire, PFC not involved

  3 OUTCOMES of Hold+Suppress:
    A: Genuine Shift — new compiles, old decays. Sustainable.
    B: Compiled Suppress — suppress itself becomes automatic. Flat affect.
    C: PFC Failure — PFC depleted, pattern breaks through. Negative spiral.

  PFC BUDGET = FINITE SHARED RESOURCE:
    → ALL PFC activities share 1 budget (learning, suppress, social, self-monitor)
    → "Exhausted at work → impatient with children at home" = budget exhausted
    → Sleep RESTORES catecholamine → budget recharges (Compile-Sleep.md §4.4)

  → Detail: PFC-Operations.md v1.3
```

### §8.3 — 3 Exposure Channels

```
🟡🟢 EXPOSURE COMES FROM 3 PARALLEL CHANNELS (Compile-Taxonomy.md v3.0 §1.3):

  EXPOSURE-EXTERNAL (body-input from reality):
    Sensory + social + motor feedback. Multi-modal RICHEST.
    No PFC required. Available to ALL species.
    5 external install mechanisms (§2.3) = variants of External.

  EXPOSURE-DELIBERATE (PFC imagination/simulate):
    PFC actively creates internal exposure: imagine, rehearse mentally.
    Body RESPONDS REALLY (saliva, heartbeat). Simulation-Engine substrate.
    Flexible but poorer in multi-modal than External.

  EXPOSURE-SPONTANEOUS (automatic chunk fire):
    Background-Pattern + spontaneous memory + association chains + mind wandering.
    Cost ≈ 0. Self-reinforcing (strong → fire → stronger).
    PFC = OBSERVER for Spontaneous (cannot direct it).

  3 Channels → ALL feed into the SAME Compile Engine (Hebbian).
  Compile Engine does NOT distinguish source (§1.1: NO SOURCE TAG).

  🟢 Mind wandering 30-50%: Smallwood & Schooler 2006
  🟢 DMN activation: Raichle et al. 2001
  → Detail: Compile-Taxonomy.md v3.0 §1.3
```

### §8.4 — Body Evaluate: 5 Preconditions

```
🟡🟢 BODY-FEEDBACK-PRECONDITION.MD v1.0 — FORMALIZED MODEL:

  Body-feedback signal fires WHEN AND ONLY WHEN all 5 are met SIMULTANEOUSLY:

    Precondition-1: DIRECTED-GAP — active gap with clear direction
    Precondition-2: CHUNK-SUBSTRATE — sufficient compiled chunks to form gap + decode
    Precondition-3: DELTA-GATE — VTA detect change > habituation threshold
    Precondition-4: MATCH-RANGE — match falls within Goldilocks zone (not alien, not familiar)
    Precondition-5: COMPILE-GATE — chunk association tags (approach/avoidance) permit firing

  CONJUNCTION LOGIC: strict AND-gate. Missing ANY 1 → signal does NOT fire fully.
  Each failure mode → distinct subjective experience (satiated, confused, habituated, mismatch, aversion).

  BODY VOTE = CONSTRAINT SATISFACTION:
    Smooth: "connects, coherent" (opioid micro-dose)
    Resistance: "something's off, contradiction" (ACC alert + cortisol)
    Empty: "not relevant" (no signal)
    → Body vote FIRST, PFC interpretation SECOND
    → 🟡 Consistent with Damasio somatic markers (🟢 1994)

  → Detail: Body-Feedback-Precondition.md v1.0
```

### §8.5 — Feeling-Intuition Gradient

```
🟡 Multi-Weak-Signal-Convergence (F4 02):

  6-POINT GRADIENT:

    CLEAR ◄────────────────────────────────────────► VAGUE

    ① Body Signal (pain, heat, hunger) — 1 strong signal, <100ms
    ② Emotion (sadness, joy, fear) — few strong signals, 100-500ms
    ③ Gut Feeling ("gut says no") — multi-chunk, 500ms-3s
    ④ Intuition ("something's not right") — many weak signals, 3-30s
    ⑤ Hunch ("I'm not sure...") — very weak signals
    ⑥ Pre-monition ("something's off somehow...") — pre-verbal sense, hours

  3 VARIABLES: Signal COUNT × STRENGTH × LABEL availability.
  NOT 6 discrete types — CONTINUOUS spectrum, SAME mechanism.
  Expert intuition = ④ but HIGH accuracy. Beginner = ③ but LOW accuracy.
```

### §8.6 — "True Smooth" vs "False Smooth" (Domain-Checked vs Self-Referencing)

```
⭐ Domain-Checked vs Self-Referencing (F4 01c §4):

  ⚠️⚠️⚠️ "FEELS SMOOTH" ≠ "CORRECT":

  DOMAIN-CHECKED:
    → Chunks tested against EXTERNAL REALITY regularly
    → Body vote ACCURATE: smooth = actually correct
    → = "TRUE SMOOTH" — calibrated against reality
    → = Scientist, craftsman, calibrated expert

  SELF-REFERENCING:
    → Chunks tested against EXISTING CHUNKS only
    → Body vote MISLEADING: smooth = consistent with self (NOT reality)
    → = "FALSE SMOOTH" — circular validation
    → = Echo chamber, rigid expert, ideologue
    → 🟢 Confirmation bias (Wason 1960, Nickerson 1998)

  NOT binary: most people = MIX across domains.
  CAN shift: Self-Referencing → Domain-Checked by introducing real-checking habit.
  Dissonance tolerance: Domain-Checked HIGH, Self-Referencing LOW.
  → Detail: PFC-Operations.md v1.3 §5 (Compiled Quality Dimension)
```

---

## §9 — Expert vs Beginner

### §9.1 — Same PFC, different database

```
🟡 "Intelligence" = RICH database + GOOD query:

  BEGINNER: SMALL database + VAGUE query → SLOW, NARROW
  EXPERT:   LARGE database + SPECIFIC query → FAST, ACCURATE
  GENIUS:   CROSS-DOMAIN database + NEW query → hits NEVER-TRIED-BEFORE

  SAME PFC (~4 slots):
    Beginner: slot = SMALL chunk → little info
    Expert:   slot = META-CHUNK → EXTREMELY MUCH info
    → = "Same 4 slots — different SIZE per slot"

  → "Intelligence" = database + compiled depth + query skill
  → = ALL TRAINABLE (not fixed talent)
```

### §9.2 — Trigger surface → expert intuition

```
  EXPERT HAS LARGE TRIGGER SURFACE IN DOMAIN (§4.4):
    → Thousands of chunks compiled over years
    → Multi-modal + deep emotional engagement + many cross-links
    → = Multi-Weak-Signal-Convergence → ACCURATE "gut feeling"
    → 🟢 Klein 1998: firefighter intuition = pattern recognition
    → 🟢 Kahneman & Klein 2009: reliable intuition requires "kind environment"

  BEGINNER PITFALL:
    → Few chunks → few conflicts → feels "smooth"
    → = Dunning-Kruger at body level: few chunks → few conflicts → feels simple
    → 🟢 Dunning & Kruger 1999
```

### §9.3 — Receptive-Productive Asymmetry

```
🟡 Receptive-Productive-Asymmetry (F1 08 §6):

  → Receptive chunk formation PRECEDES productive by ~6-12 months
  → Productive bundle ~3× receptive bundle (more chunks required)
  → 7 converging lines of evidence, 7 falsifiable predictions

  → Applied to ANY skill, not just language:
    "Understanding" precedes "being able to do it" = receptive compiled, productive not yet.
    Expert teaching: must have BOTH receptive + productive chunks compiled.

  → Detail: F1 08-Verbal-Production-Arc.md §6
```

---

## §10 — Honest Assessment

> **⚠️ BLACKBOX 1**: Chunk substrate — HOW chunks fire/store/distribute
> at the neural level — is the fundamental blackbox of the framework. Framework
> operates ON TOP OF this blackbox (predicts patterns), without needing to decode it.
> Detail: Blackbox-Map.md §4 (supersedes Framework-Boundaries.md v2.0).

### §10.1 — Established claims (🟢)

```
  🟢 Hebbian learning (Hebb 1949)
  🟢 Long-term potentiation (Bliss & Lømo 1973)
  🟢 Flashbulb memories (Brown & Kulik 1977)
  🟢 Memory reconsolidation (Nader 2000)
  🟢 Chunking + WM limits (Miller 1956, Chase & Simon 1973, Cowan 2001)
  🟢 Spreading activation (Collins & Loftus 1975)
  🟢 Expert intuition = pattern recognition (Klein 1998)
  🟢 Distributed representations (Rumelhart & McClelland 1986)
  🟢 Sleep consolidation (Walker 2017)
  🟢 Savings in relearning (Ebbinghaus 1885)
  🟢 Context-dependent memory (Godden & Baddeley 1975)
  🟢 Mood-congruent memory (Bower 1981)
  🟢 ACC conflict monitoring (Botvinick et al. 2004)
  🟢 Somatic marker hypothesis (Damasio 1994)
  🟢 Retrieval-induced forgetting (Anderson et al. 1994)
  🟢 Stress-induced relapse (Sinha 2001)
  🟢 Reconsolidation-based extinction (Schiller et al. 2010)
  🟢 Confirmation bias (Wason 1960, Nickerson 1998)
  🟢 PFC hardware from prenatal (Huttenlocher 1979, Doria 2010, Kouider 2013)
  🟢 ACE dose-response (Felitti 1998)
```

### §10.2 — Framework synthesis claims (🟡)

```
  CHUNK SYSTEM CORE:
  🟡 "Brain = search engine" — consistent with connectionist models
  🟡 4-type connection taxonomy (Static-Logical-Linking) — components established, taxonomy novel
  🟡 Activation probability distribution model — novel formalization
  🟡 Competitive re-linking as unified mechanism — novel integration
  🟡 Trigger surface concept — novel name, mechanism established
  🟡 Trauma = expertise same mechanism different direction — novel insight
  🟡 7-factor link strength model — framework formalization
  🟡 7-step discovery lifecycle — novel, components established
  🟡 Convergence zone as structural concept — novel name, Gendlin felt sense = same
  🟡 Label = logic-planning prerequisite — novel formalization
  🟡 Domain-Checked vs Self-Referencing selection pressure — novel framing
  🟡 5-parameter compile rate formula — ordinal validated, not quantitative
  🟡 Multi-modal binding = 4 concurrent mechanisms (Emergent-Binding)
  🟡 6-point feeling-intuition gradient (Multi-Weak-Signal-Convergence)
  🟡 5 anchor types with ranking — framework model
  🟡 Retrieval decay vs substrate decay distinction — novel formalization
  🟡 Context-tag as chunk metadata model (§2.6) — consistent Brewin DRT
  🟡 2 chunk types (contextual vs context-free) — framework formalization
  🟡 Compile depth predicts resistance to substrate damage (§5.4) — Alzheimer confirms

  COMPILE ARCHITECTURE (v3.0 — Compile-Taxonomy.md):
  🟡 "ALL compile = exposure → Hebbian" unifying principle
  🟡 1 Engine + 3 Modulators architecture
  🟡 Trust = amplifier (gradient Level 0-5), NOT gate (binary)
  🟡 Trust scope: amplify VALUE, NOT content
  🟡 Multi-stream compile (Content/Value/Entity/Behavior parallel)
  🟡 3 Exposure Channels parallel model (External/Deliberate/Spontaneous)
  🟡 Feedback asymmetry (Entity-Valence→PFC fast/free, PFC→Entity-Valence slow/costly)
  🟡 Sleep Maintenance in compile architecture (6 mechanisms, ~1.5 exposure / ~4.5 optimization)
  🟡 Body-Feedback-Precondition 5 conditions conjunction logic
```

### §10.3 — Speculative claims (🔴)

```
  🔴 Specific probability percentages — illustrative, not measured
  🔴 Trigger surface SIZE quantification — concept valid, numbers speculative
  🔴 ~95%/5% unconscious/PFC split — estimate, not precisely measured
  🔴 "NO true computation at chunk level" — debate ongoing
  🔴 Convergence zone as literal neural intersection — plausible, not measured
  🔴 7 discovery steps always in this order — likely variable in practice
  🔴 Probability crossover timelines — approximate, highly individual
  🔴 "21 days habit" crossover — folk wisdom, actual timing varies
  🔴 4 metadata types as formal taxonomy (§2.6) — testable, not yet tested
  🔴 Context-free chunk as explicit chunk TYPE (§2.6) — hypothesis
```

### §10.4 — Hypothesis summary

```
  ALL HYPOTHESES ACROSS CHUNK SYSTEM:

  TOTAL: 15 hypothesis entries (12 main hypotheses + 7 verdicts)

  CONFIDENCE DISTRIBUTION:
    🟢  : 2  (Compile-Gradient, PFC-From-Prenatal reframe)
    🟡🟢: 3  (Chunk-Substrate, Compile-Rate-Formula, Direction-At-Compile)
    🟡  : 10 (all remaining — framework synthesis with evidence)
    🔴  : 0  (no hypothesis remained at speculative level)

  → EVERY hypothesis reached committable confidence
  → Framework methodology: honest assessment prevents overclaiming
  → ~60+ falsifiable predictions across F1+F3+F4
```

---

## §11 — Cross-References

### §11.1 — Within Chunk/ folder + Chunk-Analysis

```
  CHUNK/ COMPANION FILES:
    Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators + 3 Compile Types + 4 Pathways
    Compile-Sleep.md v1.0 — Sleep Maintenance (6 mechanisms, offline system)
    Background-Pattern.md v2.0 — accumulated invisible bias (2D Depth×Density)

  F1 CHILD-CHUNK-DEVELOPMENT (12 files, ~11,596L):
    00 → F1 orientation
    01 → PFC-From-Prenatal reframe (🟢)
    02 → t=0 baseline
    03-05 → Visual, Auditory (Compile-Gradient 🟢), Motor arcs
    06a-06b → Interoceptive (Compile-Rate-Formula 🟡🟢 keystone + Direction-At-Compile 🟡🟢)
    07 → Social (Emergent-Binding 🟡)
    08 → Verbal (Receptive-Productive-Asymmetry 🟡 + Receptive-Productive-Gap + Label-As-Handle 🟡)
    09 → Event matrix (80+ events, 10 arcs)
    10 → ⭐ F1 Synthesis (verdicts + R-F1-1→10)

  F3 CHUNK-EXTERNAL-DEVELOPMENT (2 files, ~1,286L):
    00 → 5 mechanisms + threads
    01 → ⭐ F3 Synthesis (Grammar-Versatile-Anchor 🟡 + Abstract-Metaphysical-Grounding 🟡
          + Valence-Chunk-Interaction 🟡 + Gap2-Language-Evolution (partial) 🟡 + R-F3-1→6)

  F4 CHUNK-INTERNAL-PROCESSING (9 files, ~7,464L):
    00 → F4 sketch
    01 → Static-Logical-Linking 4-type connections (🟡)
    01b → ⭐ CORE mechanism (probability, re-linking, trigger surface)
    01c → ⭐ MACRO lifecycle (7-step, convergence zone, Domain-Checked/Self-Referencing)
    02 → Multi-Weak-Signal-Convergence feeling-intuition gradient (🟡)
    03 → Anchor-Decay (🟡)
    04 → T10 vague detection + ACC (🟡)
    05 → Gap2-Language-Evolution + insight + tacit (🟡)
    06 → ⭐ F4 Synthesis (verdicts + contracts)

  ALREADY-DRILLED:
    Learning-Cycle.md → Learning-Dissonance-Cycle
    Body-Feedback-Draft/ (5 files) → 5 Body-Feedback-Preconditions (Precondition-1–Precondition-5)

  AGENT-MECHANISM/ (11 files — formerly Agent/ 4 files):
    Agent-Mechanism.md v2.1     — master: 10 dimensions per-entity
    Self-Pattern-Modeling.md v3.1 — solo simulation, 1 mech × 3 dims
    Entity-Compiled.md v1.0     — neural reality, formation 40→200h, Dunbar
    Entity-Access.md v1.2       — gradient Level 0-5, per-entity access
    Entity-Access-Excess.md v1.0 — excess territory, addiction
    Entity-Access-Calibration.md v1.0 — self-regulation, hardware-subsidy
    Bond-Architecture.md v2.0   — 1 mechanism × 4 bond types, Resonance Decline
    By-Product-Gap-Resonance.md v1.4 — mutual match, 5 drills
    Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions, 3 modalities
    Resonance-Per-Entity.md v1.0 — per-relationship dynamics
    By-Product-Scale.md v1.0    — 1 mechanism × 3 scales

  N+5 OUTPUTS:
    Logic-Planning.md → logic packaging + AI amplifier
    Language-Structure-Analysis/ (5 files) → format references
    Neural-Processing-Flow.md → hardware foundation

  99-Master-Synthesis.md → unified lifecycle + all verdicts
```

### §11.2 — Core framework files

```
  ⚠️ Updated 2026-06-01 to align with Compile-Taxonomy v3.0 + Compile-Sleep v1.0.

  COMPILE ARCHITECTURE:
    Compile-Taxonomy.md v3.0 → 1 Engine + 3 Modulators + 3 Compile Types
    Compile-Sleep.md v1.0 → Sleep Maintenance (6 mechanisms)
    PFC-Operations.md v1.3 → Hold/Suppress, 4 combinations, PFC budget
    Body-Feedback-Precondition.md v1.0 → 5 preconditions for body-feedback signal

  REFERENCE FILES (current versions):
    Body-Base/Feeling/Feeling.md v3.0 → feeling = PFC observation, 7-layer
    Body-Base/Valence-Propagation.md v4.1 → structural/current valence, 3 firing modes
    Body-Base/Entity-Valence-Dynamics.md v1.1 → per-entity valence dynamics
    Body-Base/Body-Coupling.md v3.0 → coupling, 4 bond types, Hardware-Subsidy
    Collective/Collective-Body.md v2.1 → 3-tier Model
    Body-Base/Body-Base.md v3.3 → entry point for Body-Base system
    AI-Schema-Detection.md v2.1 → AI-assisted schema detection

  MECHANISM FILES:
    Schema/Schema.md v1.1 → schema = chunk network with purpose
    Schema/Anchor-Schema.md → anchor + trust (Clarity × Quality × Trust)
    Observation/Boredom.md v2.0 → by-product match stops, Resonance Decline
    Agent-Mechanism/Agent-Mechanism.md v2.1 → 10 dimensions per-entity
```
