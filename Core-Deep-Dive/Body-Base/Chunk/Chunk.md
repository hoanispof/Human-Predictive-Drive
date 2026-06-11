---
title: Chunk.md v3.0 — Unified Chunk System Reference
created: 2026-03-28 (v1.0 DRAFT)
updated: 2026-05-23 (v2.3 — Concept Cascade)
rewritten: 2026-06-01 (v3.0 — Architecture alignment: 1 Engine reframe, §2 trim→Compile-Taxonomy, §8 rewrite merge §8+§9+§10, §9-§12 renumber, +§0 positioning, +§2.7 Sleep Maintenance)
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
language: English (translated from Vietnamese primary + English technical)
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

## TABLE OF CONTENTS


- §0 — Position in Framework
- §1 — What Is a Chunk
- §2 — Chunk Compile
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
    WHO:  How do experts and beginners differ? (§9)

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

## §1 — What Is a Chunk

### §1.1 — Definition

```
⭐ CHUNK = STRENGTH-WEIGHTED ASSOCIATIVE NETWORK:

  🟢 Hebb (1949): "Neurons that fire together, wire together"

  → Chunk = group of neurons that have wired together → fire as 1 UNIT
  → NOT binary (present/absent) → but GRADIENT (weak → strong)
  → 🟢 Compile-Gradient (F1 04 §6.4): Proto-chunks = weak chunks, NOT "pre-chunks"
    → Behavioral "switch on" = thresholding artifact
    → Strengthen through repetition, emotional peak, multi-modal, sleep

  STRENGTH LEVELS:
    Proto-chunk:  Weak — fires sometimes, partial pattern-match
    Compiled:     Medium-strong — fires reliably, holdable in WM
    Meta-chunk:   Strong — many sub-chunks merged → fire as 1 unit
    → Expert: [DRIVING] = 1 meta-chunk = everything automatic → PFC freed
    → Beginner: [drive]+[brake]+[mirror]+[signal] = 4 chunks → PFC overloaded
    → 🟢 Chase & Simon 1973: expert chess 50,000+ chunk patterns

  → = SUBSTRATE LAYER of cognitive architecture (Chunk-Substrate 🟡🟢)
  → Everything runs on chunks: feeling, thinking, planning, identity

  ENTITY-COMPILED = NEURAL REALITY (Entity-Compiled.md v1.0):
    → When compiled deep enough for 1 entity (40-200h) → hub-and-spoke network
    → Entity EXISTS STRUCTURALLY in the brain (amygdala/hippocampus/PFC per-entity)
    → Dunbar ~150: limit on Entity-Compiled capacity
    → Grief = loss of neural reality, NOT just abstract "sadness"
    → = Chunks compiled deeply enough per-entity → become Entity-Compiled

  ⚠️ NO SOURCE TAG (Drill §10 — GAP 8):
  → Wire = wire. Body treats ALL chunks EQUALLY regardless of origin.
  → Internal compile (self-experience) vs external install (culture/trust)
    = SAME format. NO "origin" field.
  → PFC cannot distinguish → confabulation (PFC-Function §6, Valence-Propagation §7).
  → Details: Valence-Propagation §1 ④ (no source tag), Drill §10.
```

### §1.2 — Multi-modal from birth

```
🟡🟢 CHUNKS = MULTI-MODAL FROM THE START:

  Chunk "mother" = face (visual) + voice (auditory) + embrace (somatic) + warmth (emotional)
  → Fire 1 part (hear voice) → PULLS the whole chunk (recalls face, recalls embrace,...)
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
    → Blind infant smile ~8 weeks via non-visual cues = chunk-based, not mirror-based
    → 🟢 Substrate-level binding from birth (multisensory neurons + DMN)
    → Compiled chunks ADD specificity on top of substrate

  → Details: F1 07-Social-Recognition-Arc.md §6
```

### §1.3 — Pattern Hierarchy: Pattern ⊃ Chunk / Schema / Background-Pattern / Label

```
⭐ PATTERN = MOST GENERAL SUBSTRATE (Drill §18 Q-NEW-1):

  Pattern = any configuration of neural activity (firing + wiring).
  = The MOST GENERAL concept in the framework.
  = Chunk, Schema, Background-Pattern are ALL patterns.
  = NOT concepts at the same parallel level — but CONTAINS subordinate concepts.


HIERARCHY 4 LEVELS:

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
    Chunk ∈ Pattern (chunk is a compiled unit OF pattern)
    Schema ⊂ Pattern (every schema is a pattern, NOT vice versa)
    Label → Chunk/Pattern/Schema (label POINTS TO, is not the content)


RECURSIVE COMPILATION:

    Pattern → compile → Chunk → participates in new Pattern → compile → Meta-chunk → ...
    = Pyramidal compression (PFC-Analysis.md)
    = Core of Blackbox (Blackbox-Map.md §4)


DETAIL ON EACH LEVEL:

  CHUNK = ATOM:
    → 1 associative network unit, compiled, fires as 1 unit
    → Has no purpose of its own
    → Example: chunk [brake]

  SCHEMA = MOLECULE:
    → Many chunks linked → has PURPOSE/FUNCTION
    → Example: schema [driving] = chunk network → PURPOSE: movement
    → Details: Schema.md §1.1

  BACKGROUND PATTERN = OS KERNEL:
    → Accumulated from many experiences → high link density
    → Fires ALL THE TIME but PFC CANNOT SEE it (invisible)
    → Example: "how I react when under pressure" = Background-Pattern
    → Details: Background-Pattern.md

  LABEL = HANDLE:
    → Verbal/symbolic tag ATTACHED to chunk (NOT part of chunk content)
    → Label = retrieval path, NOT 5th modality (Label-As-Handle 🟡)
    → Label does NOT change content — changes ACCESSIBILITY
    → 5 handle systems: gestural, action, image, verbal, internal-only
    → Details: §6, F1 08 §5

  → Pattern = SUBSTRATE. Chunk = COMPILED UNIT. Schema = STRUCTURE.
  → Background-Pattern = INVISIBLE SUBSTRATE. Label = ACCESS PATH.

  🟡 Hierarchy formalization — Drill §18, logic consistent with Hebb + Collins & Loftus
```

---

## §2 — Chunk Compile

### §2.1 — Compile Architecture: 1 Engine + Modulators

```
⭐⭐ CORE THESIS (Compile-Taxonomy.md v3.0):

  ALL compile goes through 1 single pathway:

    EXPOSURE → HEBBIAN STRENGTHENING → COMPILED CHUNK

  There is no separate "trust compile mechanism."
  There is no separate "expertise compile mechanism."
  THERE IS ONLY 1 ENGINE (Hebbian LTP). Differences = which MODULATOR is dominant.

  4 COMPILE MECHANISMS = 4 FORMS OF EXPOSURE (same 1 Engine):

  ┌────────────────┬──────────────────────┬─────────────────────────┐
  │ Mechanism      │ = Exposure form      │ Why it compiles         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ① Repetition   │ Repeated exposure    │ Co-fire many times      │
  │                │ many times           │ → connections strengthen │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ② Emotional    │ Exposure at          │ Amygdala + NE → wire    │
  │    peak        │ EXTREME intensity    │ EXTREMELY FAST          │
  │                │ (once is enough)     │                         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ③ Multi-modal  │ Exposure across      │ Cross-cortex co-fire    │
  │                │ MANY CHANNELS        │ → richer binding        │
  │                │ simultaneously       │                         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ④ Sleep        │ OFFLINE replay       │ Hippocampus replay      │
  │                │ exposure (6 mechs)   │ → strengthen/prune      │
  └────────────────┴──────────────────────┴─────────────────────────┘

  3 COMPILE TYPES = DOMINANT MODULATOR CONFIGURATIONS:
    Experience = Engine + minimal modulators (direct exposure)
    Trust      = Engine + Entity-Valence amplifier (Entity-Valence-dominant)
    Expertise  = Engine + PFC sustained hold (PFC-dominant)

  3 MODULATORS:
    Entity-Valence Bias — automatic, cost ≈ 0, trust = multiplier per-entity
    PFC Modulation — Hold + Suppress, costly, finite budget
    3 Exposure Channels — External / Deliberate / Spontaneous (in parallel)

  NO SOURCE TAG = EVIDENCE FOR 1 ENGINE (§1.1):
    Compiled chunks have NO tag for origin.
    ALL go through the same 1 engine → products are EQUAL in the body.

  🟢 Hebbian learning: Hebb 1949
  🟢 LTP: Bliss & Lømo 1973
  🟢 Aplysia conserved: Kandel 2000
  🟡 "ALL compile = exposure" unifying principle: Compile-Taxonomy.md v3.0
  → Details architecture: Compile-Taxonomy.md v3.0 §1
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
    ③ Social referencing — "how does caregiver feel about this?"
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

  → Details: F3 00-External-Mechanism.md, F3 01-External-Synthesis.md


⭐ TRUST = AMPLIFIER (GRADIENT), NOT A GATE (BINARY):

  CONTENT compiles through exposure ALONE — does NOT require trust.
  Trust amplifies VALUE compile rate from external source.
  "Gate" = limit case when multiplier → 0.
  Compile = "Body receives experience → unconscious automatically wires." Trust amplifies, not gates.

  TRUST SCOPE — VALUE vs CONTENT (Compile-Taxonomy.md v3.0 §3.3):
    Content compile: Trust does NOT amplify (Compile Engine alone is sufficient)
    Value compile:   Trust AMPLIFIES ([X → good/bad] installs faster)
    Entity compile:  Trust weight itself = product of compile from experience
    → "Skilled but hates studying" = content ✓, value ✗ = architecture prediction

  ENTITY-ACCESS GRADIENT (Entity-Access.md v1.2):
    Level 0 (stranger, multiplier ≈ 0) → Level 5 (self/child, multiplier MAX)
    Trust = 1 dimension WITHIN valence profile per-entity (Valence-Propagation v4.1 §2)
    → Details calibration: Entity-Access-Calibration.md v1.0
    → Details excess: Entity-Access-Excess.md v1.0

  → Details trust architecture: Compile-Taxonomy.md v3.0 §3
  → Details trust mechanism: Valence-Propagation v4.1 §2
  → Details trust break: §4.3 (competitive re-linking)

  🟡 Trust amplifier — Compile-Taxonomy.md v3.0 §3
```

### §2.4 — Body-state at compile (direction matters)

```
🟡🟢 Direction-At-Compile (F1 06a §7 + 06b §6.3):

  ⭐ NOT "stress is good/bad" — BUT "which DIRECTION":

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
  → "Cortisol is NOT the enemy" — novelty-cortisol is BENEFICIAL

  4-THRESHOLD GRADIENT:
    Mild:     Body adapts quickly → minimal impact
    Moderate: Optimal zone → strongest compile
    Heavy:    Hardware stress → compiles BUT with damage risk
    Extreme:  Overwhelming → shutdown → minimal useful compile

  NEURAL WEAR compounds MULTIPLICATIVELY:
    → ACE dose-response (🟢 Felitti 1998)
    → Physical × social × anticipation sources
    → Domain × peer × imposed-adult × self-generated origins

  → Details: F1 06a-Interoceptive-Bladder.md §7, F1 06b §6.3
```

### §2.5 — Reconsolidation + No deletion

```
🟢 RECONSOLIDATION (Nader 2000):
  → Chunk recalled → TEMPORARILY unstable (~4-6 hours)
  → Within window → CAN modify → re-compile
  → = Therapy mechanism: recall → reframe → re-compile

  ⚠️ Recall WITHOUT modification → chunk STRENGTHENS → WORSE
  → 🟢 Rumination worsens depression (Nolen-Hoeksema 2000)

🟢 NO ONE CAN DELETE A CHUNK:
  → No mechanism for active "unwiring"
  → Chunk only: STRENGTHENS / WEAKENS / MODIFIES — does NOT delete
  → "Breaking an old habit" = NEW chunk compiled STRONGLY ENOUGH → OVERRIDES old chunk
  → Stress → PFC weakens → old chunk CAN fire again ("relapse when exhausted")

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
  │  METADATA        │ ASKS WHAT   │ BRAIN REGION  │ EXAMPLE     │
  ├──────────────────────────────────────────────────────────────┤
  │ ① TEMPORAL       │ WHEN?       │ Hippocampus   │ "Year 2020" │
  │   (time stamp)   │             │ (CA1,         │             │
  │                  │             │ Entity-       │             │
  │                  │             │ Compiled)     │             │
  │ ② SPATIAL        │ WHERE?      │ Hippocampus   │ "Intersection│
  │   (location)     │             │ (place cells) │  X"         │
  │ ③ CAUSAL         │ WHY?        │ Hippocampus   │ "Car ran a  │
  │   (narrative)    │ HOW?        │ + PFC         │  red light" │
  │ ④ STATE          │ BODY STATE? │ Amygdala +    │ "Fear, pain,│
  │   (body state)   │             │ Insula        │  heart↑"    │
  └──────────────────────────────────────────────────────────────┘

  HIPPOCAMPUS attaches ①②③. AMYGDALA attaches ④.

  ⭐ CHUNK CONTENT ≠ CHUNK CONTEXT-TAG:
    Content = what happened (sensory, motor, emotional fragments)
    Context-tag = when/where/why/body-state (metadata)
    → Content determines WHAT fires
    → Context-tag determines HOW retrieval FEELS:
      4/4 metadata → "remembering" (bounded, past)
      State only → "re-experiencing" (unbounded, present)

  2 CHUNK TYPES (based on context-tag quality):

    CONTEXTUAL CHUNK (hippocampal pathway):
      → 4/4 metadata → bounded, declarative, malleable
      → Supports reconsolidation (§2.5) and extinction learning
      → = Normal emotional memory. "Remembering."
      → 🟢 Brewin 2010: C-rep (contextualized representation)

    CONTEXT-FREE CHUNK (amygdala pathway):
      → ④ State only → unbounded, implicit, RESISTANT, cue-bound
      → Resistant to extinction (🟢 Bouton 2004: extinction ≠ erasure)
      → Amygdala low road ~12ms → body responds BEFORE PFC arrives (~200ms+)
      → = Trauma memory. "Re-experiencing."
      → 🟢 Brewin 2010: S-rep (sensation-based representation)

  CONTEXT-TAG QUALITY = SPECTRUM (not binary):
    Full (4/4) = normal → Partial (1-3) = stressful → State only = trauma
    → Treatment = SHIFT LEFT: hippocampus RE-ATTACHES missing metadata
    → Content UNCHANGED. Metadata CHANGED. Body response CHANGED.

  RELATIONSHIP TO §1.1 — NO SOURCE TAG:
    Source tag ("who created the chunk?") = DOES NOT EXIST (§1.1 — still correct)
    Context tag ("when/where compiled?") = EXISTS (hippocampal metadata)
    → 2 different questions. Body doesn't know SOURCE. Body HAS/DOESN'T HAVE CONTEXT.

  RELATIONSHIP TO §4.2 — link strength factors:
    §4.2 ⑤ CONTEXT MATCH = retrieval-time: current context ~ compile context → boosted
    §2.6 context-tag = compile-time: metadata ATTACHED during encoding
    → §4.2 ⑤ = "chunk is EASIER to find when context matches"
    → §2.6 = "chunk HAS or DOESN'T HAVE context from the start"

  🟢 Kim & Diamond 2002: hippocampal suppression under extreme stress
  🟢 LeDoux 1996/2000: dual pathway (low road ~12ms vs high road ~200ms)
  🟢 Brewin 2010: Dual Representation Theory (C-rep vs S-rep)
  🟢 Tulving 2002: hippocampus binds "what-where-when"
  🟡 4 metadata types as formal taxonomy = framework synthesis
  🔴 Context-free chunk as explicit chunk TYPE = hypothesis (testable)
  → Details: PTSD-Analysis.md §2-§3, §14
```

### §2.7 — Sleep Maintenance (Offline System)

```
⭐ SLEEP ≠ "4th EXPOSURE SOURCE" — SLEEP = OFFLINE MAINTENANCE SYSTEM:

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
  "Clearer in the morning" = unconscious has ALREADY pruned + consolidated + abstracted.

  🟢 Multi-mechanism sleep: Diekelmann & Born 2010
  🟡 Sleep Maintenance in compile architecture: Compile-Sleep.md v1.0
  → Details 6 mechanisms + architecture interaction: Compile-Sleep.md v1.0
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
  → UNCONSCIOUS, automatic, no PFC needed
  → 🟢 Spreading activation (Collins & Loftus 1975)
  → Healthy: [love → heart racing → excitement]
  → Pathological: [love → heart racing → fear of abandonment] (trauma contamination)

TYPE 2 — AHA MOMENT:
  → Chunks SIMMERING in background → suddenly LINK in NEW ways
  → Cannot be forced — only CONDITIONS can be created (incubation)
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
    → Smooth: "connects, coherent" (coherent overlap)
    → Resistance: "something's wrong, contradictory" (ACC conflict)
    → Empty: "unrelated" (no overlap)
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

  → Details: F4 01-Chunk-Connection-Logical.md
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

    → Chunk that receives ENOUGH activation (exceeds threshold) → fires
    → Chunk that receives INSUFFICIENT → partial activation
      (contributes to Multi-Weak-Signal-Convergence but doesn't fire alone)

  → = "When thinking about X, most often I think of A"
  → = NOT that X→A is the ONLY link
  → = But X→A is the STRONGEST link → most probable activation
  → 🟢 Spreading activation probability-weighted (Collins & Loftus 1975)
  → 🟢 Priming (Meyer & Schvaneveldt 1971, Neely 1977)
```

### §4.2 — 7-factor link strength

```
LINK STRENGTH = f(7 factors):

  ① REPETITION COUNT — how many times fired together (🟢 Hebbian)
  ② RECENCY — how long ago the last co-fire (🟢 recency effect)
  ③ EMOTIONAL WEIGHT AT COMPILE — emotional peak → EXTRA STRONG
     → 1 traumatic event CAN outweigh 100 neutral repetitions
  ④ MULTI-MODAL RICHNESS — more modalities → more neurons → stronger
  ⑤ CONTEXT MATCH — current context ~ compile context → BOOSTED
     → 🟢 Context-dependent memory (Godden & Baddeley 1975)
  ⑥ EMOTIONAL STATE MATCH — current emotion ~ compile emotion → BOOSTED
     → 🟢 Mood-congruent memory (Bower 1981)
     → Currently afraid → fear-compiled links boosted → "see danger everywhere"
  ⑦ ANCHOR STRENGTH — active anchor → link MAINTAINED
     → Weak/no anchor → link gradually DECAYS (§5)

  ⭐ FACTORS INTERACT MULTIPLICATIVELY:
    High all → EXTREMELY strong (nearly permanent): mother's name, driving skill
    Low all → EXTREMELY weak (rapid decay): phone number heard once
    High emotion + low anchor → STRONG initially but DECAYING
```

### §4.3 — Competitive re-linking

```
🟡 HOW NEW LINKS COMPETE WITH OLD LINKS (F4 01b §3):

  NOT "erase old link, replace with new link":
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
    → = "Vague fear of something without knowing what exactly"

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
    → "Still slightly uncomfortable but can handle it" = success

  ⚠️ TRIGGER SURFACE GROWTH OVER TIME (Link Density):
    → Trigger surface is NOT ONLY determined at compile time
    → Pattern persists LONG ENOUGH → NEW chunks link in → TS GROWS GRADUALLY
    → Chronic patterns: TS grows over years even without new events
    → = "Background-Pattern" — accumulated bias invisible to PFC
    → Details: Background-Pattern.md (2D model: Depth × Link Density)

  → Details activation dynamics: F4 01b-Chunk-Activation-Dynamics.md
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
    → PFC: "was scared of dogs as a child, fine now, just stay alert"
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

  → "Forgotten" = retrieval path WEAK (chunk still exists)
  → "Lost" = substrate damage (rare — traumatic brain injury, neurodegeneration)
  → "Never existed" = chunk never compiled
  → 3-way distinction: forgotten ≠ lost ≠ never existed
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
    → Re-exposure → "oh I REMEMBER now!" = path reactivates
    → = "Forgotten" in common sense = retrieval loss

  SUBSTRATE DECAY (Ebbinghaus does NOT apply):
    → Actual neural pattern degradation
    → MUCH slower (years-decades for compiled chunks)
    → Emotional peak compiled = almost no substrate decay
    → Requires biological damage for rapid loss
    → = "Lost" in true sense = content gone

  → Meaning crisis = ANCHOR crisis (Vervaeke):
    When anchors COLLECTIVELY weaken → lose access to meaningful chunks
    → Chunks still exist → but cannot reach them
    → = "Know I once knew it but can't recall it"

  → Details: F4 03-Chain-Anchor-Decay.md
```

### §5.4 — Compile depth × resistance: Alzheimer clinical validation

```
🟢 CLINICAL VALIDATION — "LAST IN FIRST OUT":

  Alzheimer-Analysis §5-§6: Alzheimer destroys chunk substrate → reveals pattern:
    → Recently compiled chunks (SHALLOW compile) lost FIRST
    → Childhood chunks (DEEP compile) resist LAST
    → = Ribot's Law (1881) EXPLAINED by compile depth

  5 INDEPENDENT MECHANISMS all predicting the same pattern:
    ① Memory consolidation: recent = hippocampus-dependent → destroyed first
    ② Compile depth × distribution: deep = more links = resistant
    ③ Activity-dependent tau: active connections release MORE tau → destroyed first
    ④ Multiple Trace Theory: old = 100+ traces, recent = 2 (🟢 Nadel 1997)
    ⑤ Myelination order: late-myelinating = thin → vulnerable (🟢 Bartzokis 2004)

  = OVERDETERMINED: any 1 mechanism correct → pattern STILL THE SAME
  = "Regardless of where the fire starts, the building collapses from the top floor."
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
  → Details: Alzheimer-Analysis.md §5-§6, §17
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
    → Label does NOT change chunk content
    → Label DOES shape access patterns + reasoning paths
    → = Having the word "saudade" doesn't CREATE the feeling
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

  ⭐ LABEL = "ENTRY TICKET" for the planning system:
    BEFORE label: chunk influence via body ONLY (Direction A)
    AFTER label:  chunk influence via body + logic (Direction A + B)
    → = Label UNLOCKS PFC access, does not change content

  WHY LABEL NEEDS TO BE "CORRECT":
    → WRONG label → wrong link → misleads future reasoning
    → Example: calling "cortisol" a "stress hormone" → links [cortisol → bad]
    → WRONG: cortisol is a sustainer, novelty-cortisol is BENEFICIAL
    → Label SHAPES future chunk connections (moderate Whorfian)
    → Choosing the right label = critical for framework quality

  → Details: F4 01c §2.6-§2.7, §3
```

### §6.3 — Anchor/Label 3-tier system

```
  Tier 1: INDIVIDUAL anchors (only 1 person knows)
    → Rich but non-shareable
    → Example: "that feeling that day" — only you know

  Tier 2: GROUP anchors (shared within community)
    → Lossy but shareable
    → Example: "melancholic mood" — group understands approximately

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

    Cycle self-reinforces: each loop = deeper + wider
    Same mechanism at ALL scales: child, scientist, civilization
```

### §7.2 — Steps explained

```
  ① ACCUMULATE: Body-input + social install → chunks library grows
     → Need ENOUGH chunks → trigger surface large enough → convergence CAN happen

  ② VAGUE EMERGENCE (Convergence Zone):
     → Many chunks fire → activation OVERLAPS at a "zone"
     → This zone = NOT 1 chunk → but intersection of many paths
     → PFC detects "there's something" but CANNOT identify "what it is"
     → = Gendlin "felt sense" at mechanism level
     → = Multi-Weak-Signal-Convergence at concept level
     → Body: "vague", "something feels off", "there's something"

  ③ CURIOSITY DRIVE:
     → Convergence zone detected → NOVELTY signal (VTA)
     → Dopamine → approach motivation → "want to know!"
     → ⚠️ IF threat-compiled → BLOCKS cycle (fear, not curiosity)
     → = Direction-At-Compile determines whether cycle CONTINUES or STOPS

  ④ CLARIFY:
     → Strategy A: Deliberate search (Type 4 — try connections → body vote)
     → Strategy B: Describe boundaries (triangulation from surrounding chunks)
     → Strategy C: External catalyst (AI/collaborator organize fragments)
     → = "Re-reading makes it clearer" = same chunks, better organized → coherent firing

  ⑤ LABEL / ANCHOR:
     → PFC searches verbal library → metaphor / description / coins new term
     → Body checks each candidate → smooth = keep, resistance = try another
     → 🟡 Gap2-Language-Evolution: Gap 2 drives language evolution (coins words for unlabeled experiences)

  ⑥ LOGIC-PLANNING ENABLEMENT:
     → Label = "entry ticket" → chunk enters planning system (§6.2)
     → AI era: AI amplifies step ⑥ (plan with labeled chunks at high speed)
     → BUT: AI CANNOT do steps ①-⑤ for humans (cannot feel the convergence zone)

  ⑦ REPEAT (deeper + wider):
     → New labeled chunk → new trigger surface → new convergence zones CAN emerge
     → Stronger, deeper, wider with each loop
     → = "Standing on the shoulders of giants" = inherit labeled chunks → extend the frontier
```

### §7.3 — 2 fates of unlabeled convergence zone

```
  FATE A — PERSISTENT VAGUE (surrounding chunks still active):
    → Body INSISTS "there's something here" → will NOT let go
    → Dissonance maintained → motivates KEEP SEARCHING
    → = Einstein: years of vague wrongness → eventually "spacetime"

  FATE B — FORGOTTEN (surrounding chunks deactivate):
    → Activation too weak → below PFC threshold
    → "Forgotten" = retrieval paths decay (NOT content lost)
    → CAN return later if reactivated

  → LABEL PREVENTS BOTH FATES:
    → Label = INDEPENDENT retrieval path
    → Even if surrounding chunks deactivate → label remains accessible
    → = Insurance against Fate B

  → Details: F4 01c-Chunk-Discovery-Lifecycle.md
```

---

## §8 — Operators × Chunk System

### §8.1 — Two Operators: Unconscious + PFC

```
🟡 CHUNK = DATA. Two operators work with the SAME database:

  ⭐ UNCONSCIOUS = PRIMARY OPERATOR (~95% of processing):
    → COMPILE automatically: experience → neurons wire → chunk forms
    → RUN compiled schemas: trigger match → automatic behavior
    → EVALUATE through body signals: reward / dissonance / satisfaction
    → BACKGROUND PROCESSING: walking while sorting thoughts, sleep consolidating
    → STRENGTHEN/WEAKEN automatically (Hebbian)

  ⭐ PFC = SECONDARY OPERATOR (~5% — but determines DIRECTION):
    → HOLD: keep chunks active in WM (~4±1)
    → SUPPRESS: block compiled patterns that are firing
    → CREATE: imagine new chunk → body check → compile
    → MODIFY: recall → reconsolidation window → change → re-compile
    → DIRECT: choose attention → decide which chunks fire

  → = "Unconscious builds the house (95%), PFC chooses WHERE TO BUILD (5%)"

  PFC HARDWARE ONLINE FROM PRENATAL (🟢 F1 01):
    5 pillars: Huttenlocher 1979, Doria 2010, Kouider 2013, Grossmann 2009, Hodel 2018.
    OLD: "PFC offline until age X." NEW: "PFC hardware online from birth — chunks missing."

  PFC-INFERENCE LADDER (🟡🟢 F1 01 + F1 10):
    L0 Reflex → L1 Orienting → L2 Pattern-match → L3 Deliberate → L4 Coordinated
    = EVENT property, not AGE property. Same person at different L-levels per domain.

  SIMULATION-ENGINE = FORMALIZED PFC MECHANISM (Simulation-Engine.md v1.1):
    → 1 Engine, 3 Components: Interoceptive Model × Simulation × Self-Pattern-Modeling
    → Details: Simulation-Engine.md v1.1, PFC-Operations.md v1.3
```

### §8.2 — PFC Operations: Hold + Suppress

```
🟡🟢 PFC-OPERATIONS.MD v1.3 — FORMALIZED MODEL:

  2 OPERATIONS:
    HOLD = amplify target pattern → INCREASES exposure quality
      Cost: ① PFC draft (processing load). CAN compile → sustainable.
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
    → "Exhausted at work → no patience with children at home" = budget exhausted
    → Sleep RESTORES catecholamine → budget recharges (Compile-Sleep.md §4.4)

  → Details: PFC-Operations.md v1.3
```

### §8.3 — 3 Exposure Channels

```
🟡🟢 EXPOSURE COMES FROM 3 CHANNELS RUNNING IN PARALLEL (Compile-Taxonomy.md v3.0 §1.3):

  EXPOSURE-EXTERNAL (body-input from reality):
    Sensory + social + motor feedback. Multi-modal RICHEST.
    Does NOT require PFC. Available to ALL species.
    5 external install mechanisms (§2.3) = variants of External.

  EXPOSURE-DELIBERATE (PFC imagination/simulate):
    PFC actively creates internal exposure: imagine, rehearse, mental practice.
    Body REACTS FOR REAL (saliva, heartbeat). Simulation-Engine substrate.
    Flexible but less multi-modal than External.

  EXPOSURE-SPONTANEOUS (automatic chunk fire):
    Background-Pattern + spontaneous memory + association chains + mind wandering.
    Cost ≈ 0. Self-reinforcing (strong → fires → stronger).
    PFC = OBSERVER for Spontaneous (cannot direct it).

  3 Channels → ALL feed into SAME Compile Engine (Hebbian).
  Compile Engine does NOT distinguish source (§1.1: NO SOURCE TAG).

  🟢 Mind wandering 30-50%: Smallwood & Schooler 2006
  🟢 DMN activation: Raichle et al. 2001
  → Details: Compile-Taxonomy.md v3.0 §1.3
```

### §8.4 — Body Evaluate: 5 Preconditions

```
🟡🟢 BODY-FEEDBACK-PRECONDITION.MD v1.0 — FORMALIZED MODEL:

  Body-feedback signal fires IF AND ONLY IF all 5 are met SIMULTANEOUSLY:

    Precondition-1: DIRECTED-GAP — active gap has a clear direction
    Precondition-2: CHUNK-SUBSTRATE — sufficient compiled chunks to form gap + decode
    Precondition-3: DELTA-GATE — VTA detects change > habituation threshold
    Precondition-4: MATCH-RANGE — match falls within Goldilocks zone (not alien, not familiar)
    Precondition-5: COMPILE-GATE — chunk association tags (approach/avoidance) permit firing

  CONJUNCTION LOGIC: strict AND-gate. Missing ANY 1 → signal does NOT fire fully.
  Each failure mode → distinct experience (saturation, confused, habituated, mismatch, aversion).

  BODY VOTE = CONSTRAINT SATISFACTION:
    Smooth: "connects, coherent" (opioid micro-dose)
    Resistance: "something's wrong, contradictory" (ACC alert + cortisol)
    Empty: "unrelated" (no signal)
    → Body vote FIRST, PFC interpretation SECOND
    → 🟡 Consistent with Damasio somatic markers (🟢 1994)

  → Details: Body-Feedback-Precondition.md v1.0
```

### §8.5 — Feeling-Intuition Gradient

```
🟡 Multi-Weak-Signal-Convergence (F4 02):

  6-POINT GRADIENT:

    CLEAR ◄────────────────────────────────────────► VAGUE

    ① Body Signal (pain, heat, hunger) — 1 strong signal, <100ms
    ② Emotion (sadness, joy, fear) — few strong signals, 100-500ms
    ③ Gut Feeling ("gut says no") — multi-chunk, 500ms-3s
    ④ Intuition ("something doesn't feel right") — many weak signals, 3-30s
    ⑤ Hunch ("not sure...") — very weak signals
    ⑥ Pre-monition ("something feels off...") — pre-verbal sense, hours

  3 VARIABLES: Signal COUNT × STRENGTH × LABEL availability.
  NOT 6 discrete types — CONTINUOUS spectrum, SAME mechanism.
  Expert intuition = ④ but HIGH accuracy. Beginner = ③ but LOW accuracy.
```

### §8.6 — "Genuinely smooth" vs "Falsely smooth"

```
⭐ Domain-Checked vs Self-Referencing (F4 01c §4):

  ⚠️⚠️⚠️ "FEELS SMOOTH" ≠ "CORRECT":

  DOMAIN-CHECKED:
    → Chunks tested against EXTERNAL REALITY regularly
    → Body vote ACCURATE: smooth = actually correct
    → = "GENUINELY smooth" — calibrated against reality
    → = Scientist, craftsman, calibrated expert

  SELF-REFERENCING:
    → Chunks tested against EXISTING CHUNKS only
    → Body vote MISLEADING: smooth = consistent with self (NOT reality)
    → = "FALSELY smooth" — circular validation
    → = Echo chamber, rigid expert, ideologue
    → 🟢 Confirmation bias (Wason 1960, Nickerson 1998)

  NOT binary: most people = MIX across domains.
  CAN shift: Self-Referencing → Domain-Checked by introducing real-checking habit.
  Dissonance tolerance: Domain-Checked HIGH, Self-Referencing LOW.
  → Details: PFC-Operations.md v1.3 §5 (Compiled Quality Dimension)
```

---

## §9 — Expert vs Beginner

### §9.1 — Same PFC, different database

```
🟡 "Intelligence" = RICH database + GOOD query:

  BEGINNER: SMALL database + VAGUE query → SLOW, NARROW
  EXPERT:   LARGE database + SPECIFIC query → FAST, ACCURATE
  GENIUS:   CROSS-DOMAIN database + NEW query → hits WHAT NO ONE HAS TRIED

  SAME PFC (~4 slots):
    Beginner: slot = SMALL chunk → little info
    Expert: slot = META-CHUNK → ENORMOUS info
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
    "Understand" before "can do" = receptive compiled, productive not yet.
    Expert teaching: must have BOTH receptive + productive chunks compiled.

  → Details: F1 08-Verbal-Production-Arc.md §6
```

---

## §10 — Honest Assessment

> **⚠️ BLACKBOX 1**: Chunk substrate — HOW chunks fire/store/distribute
> at the neural level — is a fundamental blackbox of the framework. The framework operates
> ON TOP OF this blackbox (predicts patterns), does not need to decode it.
> Details: Blackbox-Map.md §4 (supersedes Framework-Boundaries.md v2.0).

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
  🟡 Trauma = expertise same mechanism diff direction — novel insight
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
  🟡 Multi-stream compile (Content/Value/Entity/Behavior in parallel)
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
    01 → ⭐ F3 Synthesis (Grammar-Versatile-Anchor 🟡 + Abstract-Metaphysical-Grounding 🟡 + Valence-Chunk-Interaction 🟡 + Gap2-Language-Evolution (partial) 🟡 + R-F3-1→6)

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
    Logic-Planning.md → packaged logic + AI amplifier
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
    Collective/Collective-Body.md v2.1 → 3-level Model
    Body-Base/Body-Base.md v3.3 → entry point for Body-Base system
    AI-Schema-Detection.md v2.1 → AI-assisted schema detection

  MECHANISM FILES:
    Schema/Schema.md v1.1 → schema = chunk network with purpose
    Schema/Anchor-Schema.md → anchor + trust (Clarity × Quality × Trust)
    Observation/Boredom.md v2.0 → by-product match stops, Resonance Decline
    Agent-Mechanism/Agent-Mechanism.md v2.1 → 10 dimensions per-entity
    PFC/Simulation-Engine.md v1.1 → 1 engine, 3 components, N applications
    PFC/PFC-Label.md v1.0 → vocabulary reference, 13 domains
    Logic-Feeling.md v4.0 → Body-Knowing + observer labels, Compiled/Fresh
    Somatic-Articulation-Loop.md → body → explicit knowledge

  ANALYSIS FILES:
    PFC/PFC-Function.md v1.2 → 24 functions, 95/5 split
    Imagination/Imagine-Final.md v3.0 → hardware prediction ≠ Imagine-Final

  HEALTH CONDITIONS DRILL (reverse propagation):
    PTSD-Analysis.md v1.0 → §2 context-tag model, §14 formalization
    Alzheimer-Analysis.md v1.1 → §5 synapse loss, §6 "last in first out"
    → Informed: §2.6 (context-tag), §5.4 (compile depth validation)
```

### §11.3 — Key academic references

```
  CHUNK FOUNDATION:
    🟢 Hebb 1949 — Hebbian learning
    🟢 Miller 1956 — Chunking, WM capacity
    🟢 Bliss & Lømo 1973 — Long-term potentiation
    🟢 Ebbinghaus 1885 — Forgetting curve
    🟢 Rumelhart & McClelland 1986 — Distributed representations
    🟢 Chase & Simon 1973 — Expert chess patterns

  PFC + DEVELOPMENT:
    🟢 Cowan 2001 — WM ~4 items
    🟢 Huttenlocher 1979 — Synaptic density at birth
    🟢 Doria 2010 — Functional networks at term
    🟢 Kouider et al. 2013 — Frontal signatures 5mo
    🟢 Fuster 1973 — PFC sustained activity

  ACTIVATION + MEMORY:
    🟢 Collins & Loftus 1975 — Spreading activation
    🟢 Nader 2000 — Memory reconsolidation
    🟢 Anderson et al. 1994 — Retrieval-induced forgetting
    🟢 Schiller et al. 2010 — Reconsolidation-based extinction
    🟢 Godden & Baddeley 1975 — Context-dependent memory
    🟢 Bower 1981 — Mood-congruent memory

  EXPERTISE + INTUITION:
    🟢 Klein 1998 — Recognition-primed decision
    🟢 Kahneman & Klein 2009 — Expert intuition environments
    🟢 Gendlin 1978 — Focusing, felt sense
    🟢 Damasio 1994 — Somatic marker hypothesis

  TRAUMA + STRESS:
    🟢 Felitti 1998 — ACE study
    🟢 Sinha 2001 — Stress-induced relapse
    🟢 Nolen-Hoeksema 2000 — Rumination

  COGNITION + LEARNING:
    🟢 Festinger 1957 — Cognitive dissonance
    🟢 Walker 2017 — Sleep consolidation
    🟢 Vygotsky 1978 — Zone of Proximal Development
    🟢 Kounios & Beeman 2009 — Neural basis of insight
    🟢 Botvinick et al. 2004 — ACC conflict monitoring

  BIAS + SOCIAL:
    🟢 Wason 1960 — Confirmation bias
    🟢 Dunning & Kruger 1999 — Unskilled and unaware
    🟢 Berridge 2003 — Dopamine = wanting, opioid = liking

  CONTEXT-TAG + COMPILE DEPTH (v2.2):
    🟢 Kim & Diamond 2002 — Hippocampal suppression under extreme stress
    🟢 LeDoux 1996/2000 — Dual pathway architecture (amygdala)
    🟢 Brewin 2010 — Dual Representation Theory (C-rep vs S-rep)
    🟢 Tulving 2002 — Hippocampus binds "what-where-when"
    🟢 Bouton 2004 — Extinction ≠ erasure
    🟢 Terry 1991 — Synapse loss r=0.96 (Alzheimer)
    🟢 Ribot 1881 — Temporal gradient retrograde amnesia
    🟢 Nadel & Moscovitch 1997 — Multiple Trace Theory
    🟢 Bartzokis 2004/2011 — Myelination order + vulnerability

  (Full reference lists in individual source files)
```

---

## §12 — Status

```
✅ CHUNK.MD V2.0 COMPLETE (2026-04-17)

  UPGRADE FROM V1:
    v1 (2026-03-28): ~435L, 9 sections, DRAFT
    v2 (2026-04-17): ~1,800L, 14 sections, incorporates 44+ files deep analysis

  MAJOR ADDITIONS:
    → §1: Gradient architecture (Compile-Gradient) + multi-modal binding (Emergent-Binding)
    → §2: 5-parameter formula (Compile-Rate-Formula) + external install (F3) + Direction-At-Compile
    → §3: 4-type connection taxonomy (Static-Logical-Linking) — entirely NEW
    → §4: Activation dynamics (01b CORE) — entirely NEW
    → §5: Anchor-Decay model — entirely NEW
    → §6: Labels + logic-planning enablement (Label-As-Handle + 01c) — entirely NEW
    → §7: Discovery lifecycle 7 steps (01c) — entirely NEW
    → §8: PFC reframe (PFC-From-Prenatal) + PFC-Inference Ladder — MAJOR UPDATE
    → §10: Feeling-intuition gradient (Multi-Weak-Signal-Convergence) + Domain-Checked/Self-Referencing — MAJOR UPDATE
    → §11: Trigger surface + Receptive-Productive-Asymmetry — MAJOR UPDATE
    → §12: All 15 hypotheses aggregated — MAJOR UPDATE

  PRESERVED FROM V1:
    → "Brain = database + 2 operators" framing
    → 4 compile mechanisms
    → 4 PFC search modes
    → "Smooth ≠ correct" warning
    → Cortisol = amplifier
    → Expert vs beginner database metaphor

  SOURCES:
    44+ files, ~48,600L deep analysis across 13 sessions (Planning → N+13)
    15 hypotheses, all at 🟡 or higher
    ~60+ falsifiable predictions
    16 framework update recommendations (R-F1: 10, R-F3: 6)

  4-PHASE LIFECYCLE:
    ① COMPILE (§2) → ② INSTALL (§2.3) → ③ PROCESS (§3-§7) → ④ PLAN (§6, §9)
    Full loop: Compile → Install → Process → Plan → [Action] → [New Experience] → Compile
    = Self-reinforcing spiral at ALL scales

  NEXT:
    → Feeling.md v2.0 (N+15) — incorporate 3 deep files + existing 7-layer
    → R-F1/R-F3 framework updates (16 recommendations pending)

✅ V2.2 UPDATE (2026-05-15) — HEALTH CONDITIONS DRILL REVERSE PROPAGATION:

  §2.6 NEW — Context-tag: 4 metadata types at compile
    → PTSD-Analysis §2-§3: hippocampus attaches ①②③, amygdala attaches ④
    → 2 chunk types: contextual (4/4) vs context-free (state only)
    → Extends §1.1 NO SOURCE TAG (still correct — context tag = separate mechanism)
    → Brewin 2010 DRT mapping (C-rep = contextual, S-rep = context-free)

  §5.4 NEW — Compile depth × resistance: Alzheimer clinical validation
    → "Last in first out" = 5 overdetermined mechanisms
    → Terry 1991 r=0.96, Bartzokis 2004, Nadel 1997
    → "Architecture determines pattern, NOT cause"

  §12 UPDATED — 3 synthesis + 2 speculative claims added
  §13 UPDATED — PTSD + Alzheimer drill files added + 9 new references

  Source: Health Conditions Drill (6 files, ~12,000L)
  Plan: Research/Health-Conditions/plan-drill-reverse-propagation.md Phase 1

✅ V2.3 UPDATE (2026-05-23) — CONCEPT CASCADE (28-session Drill Propagation):

  §1.1: +Entity-Compiled reference (neural reality, formation 40→200h, Dunbar)
  §2.3: +Entity-Access gradient (Level 0-5), +Entity-Access-Calibration, +Entity-Access-Excess references
  §6.1: +PFC-Label.md v1.0 vocabulary reference
  §8.3: +Simulation-Engine (1 engine, 3 components — formalized PFC mechanism)
  §13.1: Agent-Mechanism/ expanded (4 → 11 files, folder renamed)
  §13.2: Major version updates (Valence-Propagation v1.4→v3.0, Body-Base v2.0→v3.2, Collective-Body v2.0→v2.1,
          AI-Schema v1.0→v2.0, Imagine-Final→v3.0). Folder paths updated (Drive/→Observation/,
          Agent/→Agent-Mechanism/). +Simulation-Engine, +PFC-Label, +PFC-Operations, +Boredom v2.0.

  Source: plan-concept-cascade-refine.md Phase A2

✅ V3.0 RESTRUCTURE (2026-06-01):

  ARCHITECTURE ALIGNMENT with Compile-Taxonomy v3.0 + Compile-Sleep v1.0:

  §0 NEW: Position in framework + reading flow + folder overview
  §2.1 REFRAME: "4 separate mechanisms" → "1 Engine + 4 forms of exposure"
    + 3 Compile Types = dominant modulator configurations
    + 3 Modulators (Entity-Valence Bias, PFC Modulation, 3 Exposure Channels)
  §2.3 TRIM: Trust detail (~100→~45 lines) → Compile-Taxonomy.md v3.0 §3
    + Trust scope VALUE vs CONTENT distinction
  §2.7 NEW: Sleep Maintenance summary (6 mechanisms table)
    → Details: Compile-Sleep.md v1.0
  §8 REWRITE: Merge old §8+§9+§10 (~285→~175 lines) → "Operators × Chunk System"
    §8.1: Two Operators (keep core + PFC-Inference Ladder + Simulation-Engine ref)
    §8.2: PFC Operations Hold/Suppress (new, from PFC-Operations.md v1.3)
    §8.3: 3 Exposure Channels (new, from Compile-Taxonomy.md v3.0 §1.3)
    §8.4: Body Evaluate 5 Preconditions (new, from Body-Feedback-Precondition.md v1.0)
    §8.5: Feeling-Intuition Gradient (keep, trimmed)
    §8.6: Domain-Checked vs Self-Referencing (keep, trimmed)
  Old §9 "PFC Search (4 Modes)" REMOVED: superseded by §8.2+§8.3
  Old §10 "Body Evaluate" ABSORBED into §8.4-§8.6
  §9-§12 renumbered (old §11→§9, §12→§10, §13→§11, §14→§12)
  §10 Honest Assessment: +9 new 🟡 items (compile architecture concepts)
  §11 Cross-References: +Compile-Taxonomy v3.0, +Compile-Sleep v1.0,
    version updates throughout

  NET: ~1,670 → ~1,540 lines (~-130). Quality INCREASED:
    Remove duplicates with Compile-Taxonomy v3.0
    Align PFC-Operations v1.3 (Hold/Suppress/Budget)
    Align Body-Feedback-Precondition v1.0 (5 preconditions)
    +6 missing concepts integrated
    Cross-refs modernized

  Source: plan-chunk-v3-restructure.md
  Backup: backup/Chunk-v2.3-backup.md
```

---

> **Chunk.md v3.0 — "Brain = database + 2 operators."**
>
> Chunk = strength-weighted associative network compiled through experience.
> ALL compile = Exposure → Hebbian (1 Engine). 3 Compile Types = modulator configs.
> 4 connection types: contamination + aha + meta-chunk + deliberate linking.
> Core mechanism: probability distribution + competitive re-linking + trigger surface.
> Trauma = expertise = SAME mechanism, DIFFERENT direction.
> Entity-Compiled = neural reality when compiled deeply enough per-entity.
> PFC Operations: Hold + Suppress, 4 combinations, 3 outcomes, finite budget.
> 3 Exposure Channels: External / Deliberate / Spontaneous (in parallel).
> Body-feedback: 5 Preconditions conjunction (all met → signal fires).
> Context-tag: 4 metadata types → contextual vs context-free chunks.
> Compile depth predicts resistance — Alzheimer "last in first out" confirms.
> 7-step discovery: Accumulate → Vague → Curious → Clarify → Label → Plan → Repeat.
> "Humans need to FEEL correctly → AI will help PLAN correctly."
>
> Architecture details → Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0.
> Version: v3.0, 2026-06-01.
