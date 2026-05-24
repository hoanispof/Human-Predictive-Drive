---
title: Body-Feedback — Synthesis of Body Signal Architecture
version: 3.0
created: 2026-04-15 (N+3, drill P0-P5)
refined: 2026-04-20 (v1.1 — add Mechanism file, cleanup refs)
rewritten: 2026-05-17 (v2.0 — folder rebuild complete, +3 files, Compilable Architecture, updated reading guide)
refined: 2026-05-17 (v2.0a — Why-Body-Knows v1.1 ref: 4-tier → 2-tầng calibration)
rewritten: 2026-05-24 (v3.0 — FULL REWRITE: 14 files/~23,900L, +pipeline visualization, +Gap System, +Quality/Calibration, trimmed cases, all versions updated)
previous: v2.0a → backup/Body-Feedback-v2.0a-backup.md
status: SYNTHESIS v3.0
scope: |
  Unified model of body signal generation (dissonance + reward + neutral).
  Entry point for Body-Feedback/ folder (14 files, ~23,900L).
  Synthesizes folder into single reference + reading guide.
  v3.0: Folder expanded from 10→14 files.
  +Gap-Body-Need v1.0, +Gap-Distribution-Profile v1.1, +Action-Space v1.0, +Hidden-Quality-Perception v1.0.
  +Full 6-layer pipeline visualization (hardware → PFC + inter-body).
  +Gap System section (direction + 3 satiation + distribution + behavioral prediction).
  +Quality + Calibration section (reward calibration + hidden quality).
  +Trimmed case details (~200L → ~60L pointers to drill files).
  +All external cross-ref versions updated.
purpose: |
  WHY and HOW body generates affective signals.
  H10 5 preconditions for body signals.
  Chunk dynamics classification (4th axis).
  Gap system (direction + dynamics + distribution + supply-side).
  Quality perception + reward calibration.
  Unique contributions not absorbed elsewhere.
  READING GUIDE for navigating 14-file, ~23,900L folder.
parent: Body-Base/
position: Body-Feedback/ (synthesis file, entry point for folder)
dependencies: |
  Body-Feedback-Mechanism.md v2.0 (chunk dynamics, 2-source, Body-Need, compound)
  Body-Feedback-Label.md v2.0 (vocabulary reference, 3-tier labels, ALL new terms)
  Gap-Direction.md v2.0 (gap has direction, 2-layer, by-product match)
  Gap-Body-Need.md v1.0 (3 Satiation Profiles, 5-Parameter, ENGINE/ROAD/VEHICLE)
  Gap-Distribution-Profile.md v1.1 (per-person gap landscape, 4 trục, 4 tầng)
  Reward-Signal-Architecture.md v2.0 (Evaluative/Direct-State, 5 Profiles, Evaluative Gates Direct-State)
  Reward-Calibration.md v1.1 (Goldilocks per-gap, 6 mechanisms, dynamic equilibrium)
  Action-Space.md v1.0 (supply-side, 4 trục, Gap-Distribution × Action-Space)
  Hidden-Quality-Perception.md v1.0 (compilation depth → quality visibility, 2 types)
  Drill-Body-Feedback/01-Foundation.md (dual-pull, interface loop, body-feedback vs feeling)
  Drill-Body-Feedback/02-Dissonance.md (3 Genuine Discomfort Sources, threat matrix, trauma loop, hedonic trap)
  Drill-Body-Feedback/03-Reward.md (VTA + opioid, H10 preconditions, ô tô paradox, Van Gogh)
  Drill-Body-Feedback/04-Integration.md (unified loop, case walkthroughs, H10 v3, recommendations)
  Inter-Body-Mechanism.md v2.0 (Compilable Architecture, Compiled/Fresh, domain arbiter)
language: Tiếng Việt primary + English technical
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback — Synthesis of Body Signal Architecture

> **File này là ENTRY POINT** cho Body-Feedback/ folder.
> 14 files, ~23,900L: Mechanism + Gap System + Reward Architecture +
> Aggregate Observation + Case Analyses.
>
> **Đọc file này TRƯỚC**. Đi sâu vào từng file nếu cần detail.
>
> **Core claims:**
> 1. Body signal = function of 5 preconditions (H10) on interface loop
> 2. Body-feedback arises from 2 input sources × 3 chunk dynamics → Body-Need
> 3. Reward has 2 types (Evaluative / Direct-State) × 5 profiles × interaction model
> 4. Gap has DIRECTION + 3 SATIATION PROFILES + per-person DISTRIBUTION
> 5. Behavior = f(Gap-Distribution DEMAND × Action-Space SUPPLY)

---

## Mục lục

- §1 — Folder Overview + Reading Guide
- §2 — ⭐ Full Pipeline Visualization (6 layers)
- §3 — Dual-Pull + Interface Loop + 3 Genuine Discomfort Sources
- §4 — Signal Generation + Body-Need
- §5 — Signal Architecture + H10
- §6 — ⭐ Gap System (direction + satiation + distribution + supply)
- §7 — ⭐ Quality + Calibration
- §8 — Case Analyses + Special Mechanisms (pointers)
- §9 — Absorbed Content Map
- §10 — Honest Assessment + Cross-References

---

## §1 — Folder Overview + Reading Guide

### §1.1 — Files in this folder (v3.0 updated)

```
Body-Feedback/
│
├── Body-Feedback.md             ← THIS FILE (entry point, synthesis)
│
├── VOCABULARY:
│   └── Body-Feedback-Label.md   (1,119L) — ⭐ VOCABULARY REFERENCE v2.0
│         3-tier labels, ALL framework terms formalized
│
├── MECHANISM:
│   └── Body-Feedback-Mechanism.md (1,519L) — ⭐ MECHANISM v2.0
│         2-source model, Body-Need aggregate, 3 chunk dynamics, compound
│
├── GAP SYSTEM:
│   ├── Gap-Direction.md         (2,681L) — ⭐ GAP DIRECTION v2.0
│   │     Gap has direction = f(surrounding chunks), 2-layer model,
│   │     by-product match, "chưa biết = không có gap"
│   ├── Gap-Body-Need.md         (1,388L) — GAP DYNAMICS v1.0
│   │     3 Satiation Profiles (Cyclic/Tonic/Generative),
│   │     5-Parameter per-gap model, ENGINE/ROAD/VEHICLE architecture
│   └── Gap-Distribution-Profile.md (2,370L) — GAP LANDSCAPE v1.1
│         Per-person gap aggregate, 4 trục, 4-tầng formation,
│         resonance prediction
│
├── REWARD ARCHITECTURE:
│   ├── Reward-Signal-Architecture.md (1,987L) — ⭐ REWARD TYPES v2.0
│   │     Evaluative/Direct-State distinction, E₀→E₃ gradient,
│   │     Evaluative Gates Direct-State, 5 Reward Profiles
│   └── Reward-Calibration.md    (1,356L) — CALIBRATION v1.1
│         Goldilocks per-gap, 6 over-reward mechanisms,
│         dynamic equilibrium
│
├── AGGREGATE OBSERVATION:
│   ├── Action-Space.md          (1,729L) — SUPPLY SIDE v1.0
│   │     4 trục (Compiled Capacity × Resource Access × Freedom × Awareness),
│   │     Gap-Distribution × Action-Space = behavioral prediction
│   └── Hidden-Quality-Perception.md (1,738L) — QUALITY VISIBILITY v1.0
│         "Chưa biết = không có gap" × quality, 2 types (Expert + Leader),
│         Dunning-Kruger = meta-level application
│
├── CASE ANALYSES:
│   └── Drill-Body-Feedback/
│       ├── 01-Foundation.md     (1,126L) — dual-pull, loop, architecture
│       ├── 02-Dissonance.md     (1,846L) — 3 nguồn, threat, trauma, hedonic
│       ├── 03-Reward.md         (2,280L) — VTA+opioid, H10, ô tô, Van Gogh
│       └── 04-Integration.md    (1,856L) — unified cycle, walkthroughs, H10 v3
│
└── backup/                      (historical versions)

FOLDER TOTAL: 14 content files, ~23,900L
```

### §1.2 — Reading guide (4-tier navigation)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 1: VOCABULARY + ENTRY (~2,000L — read ALWAYS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① This file (Body-Feedback.md) — overview, pipeline, reading guide
  ② Body-Feedback-Label.md v2.0 — ⭐ MUST-READ VOCABULARY
     → 3-tier label system (General → Direction → Specific)
     → 100% framework vocabulary formalized
     → prediction-delta ≠ body-base reward (detection ≠ evaluation)
     → Body-feedback (mechanism) ≠ Feeling (PFC observation)
     → Entity-Compiled subtypes, Compiled/Fresh labels,
       By-product match/anti-match, 2-Stream, 3-cost, 5-Channel

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 2: MECHANISM + ARCHITECTURE (~7,575L — read for UNDERSTANDING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ③ Body-Feedback-Mechanism.md v2.0 — HOW body creates signals
     → 2 input sources (Sensory-Driven / Pattern-Driven)
     → 3 chunk dynamics (Shift / Miss / Gap)
     → Body-Need = 2-source aggregate, 7 properties, 4 immediacy types
     → Compound mechanism + Quality Baseline Shift

  ④ Gap-Direction.md v2.0 — WHY signals are personal
     → Gap direction = f(surrounding chunk network structure)
     → "Chưa biết = không có gap" (foundational principle)
     → 2-layer model: signal mechanism × direction content
     → By-product match × gap direction, Compiled/Fresh connection

  ⑤ Reward-Signal-Architecture.md v2.0 — WHAT kinds of reward
     → Evaluative Reward (opioid) vs Direct-State Reward (non-opioid)
     → E₀→E₃ complexity gradient (compilation depth)
     → Evaluative Gates Direct-State (insula gradient, 4 outcomes)
     → 5 Reward Profiles, Temporal Stack, Conditional Interaction

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 3: GAP DYNAMICS + OBSERVATION (~7,193L — read for DEPTH)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⑥ Gap-Body-Need.md v1.0 — HOW gaps consume + compete
     → 3 Satiation Profiles (Cyclic/Tonic/Generative)
     → 5-Parameter per-gap model (Source × Satiation × Reward × Chain × Dependency)
     → ENGINE/ROAD/VEHICLE architecture
     → Technology fill, entity-gap matching, gap lifecycle

  ⑦ Gap-Distribution-Profile.md v1.1 — WHERE gaps cluster per person
     → 4 trục (Domain Center × Origin Balance × Depth × Stability)
     → 4-tầng formation (Collective → Schemas → Family → Hardware)
     → Resonance prediction: gap overlap → by-product match probability

  ⑧ Reward-Calibration.md v1.1 — HOW MUCH reward is enough
     → Goldilocks per-gap, per-person, per-context
     → 6 over-reward mechanisms
     → Dynamic equilibrium (CANNOT prescribe)

  ⑨ Action-Space.md v1.0 — WHAT options available per person
     → 4 trục (Compiled Capacity × Resource Access × Freedom × Awareness)
     → Gap-Distribution × Action-Space = behavioral prediction (4 quadrants)

  ⑩ Hidden-Quality-Perception.md v1.0 — WHY experts SEE differently
     → "Chưa biết = không có gap" × quality visibility
     → 2 types: Domain Expert + Leader/Coordinator
     → Dunning-Kruger = meta-level application

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TIER 4: CASES (~7,108L — read for SPECIFIC EXAMPLES)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⑪ 01-Foundation.md — dual-pull principle, interface loop
  ⑫ 02-Dissonance.md — 15+ cases, 3 nguồn, trauma mechanism
  ⑬ 03-Reward.md — ô tô paradox, Van Gogh gradient, C5 latency
  ⑭ 04-Integration.md — Einstein/hedonic/trauma walkthroughs, H10 v3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ABSORBED ELSEWHERE (authoritative versions in other files):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  → Feeling-Mechanism-Deep-Draft.md §4 — reward mechanism (dopamine ≠ reward)
  → Feeling-Mechanism-Deep-Draft.md §3 — 8-step operational flow
  → Feeling-Chunk-Bridge-Draft.md §2  — body vote feedback mechanisms
```

### §1.3 — Compilable Architecture: WHY body-feedback system this complex

```
🟡 COMPILABLE ARCHITECTURE = TẠI SAO FOLDER NÀY CẦN ~23,900 LINES:

  Côn trùng (Hardwired Architecture):
    Hardwired reward circuits: food→approach, pain→avoid.
    Body-feedback system = SIMPLE (few signals, few dynamics).

  Humans (Compilable Architecture — Inter-Body-Mechanism.md v2.0 §1):
    ① General-Purpose Reward — fire cho BẤT KỲ gap fill đúng direction
    ② Compilation — Hebbian: repeat + verify → automatic
    ③ Social Hardware — oxytocin, μ-opioid, dACC reuse

  → General-purpose = body CAN evaluate ANYTHING
  → Compilation = evaluation grows increasingly complex (E₀→E₃)
  → Social = body-feedback includes SOCIAL signals natively
  → Trade-off: 15-20 năm compile → RICH signal architecture

  CONSEQUENCE cho folder này:
    Mechanism:   2 sources × 3 dynamics (general-purpose creates variety)
    Gap System:  direction + satiation + distribution (compiled differently per person)
    Reward:      Evaluative/Direct-State + 5 Profiles (evaluation diversity)
    Calibration: Goldilocks (personal, dynamic)
    Supply:      Action-Space (options determine behavior)
    Quality:     Hidden perception (compilation depth → visibility)
    Cases:       01-04 (body-feedback OPERATES in domain reality)

  Without Compilable Architecture: folder = 2 files (pain/pleasure simple circuits).
  WITH Compilable Architecture: folder = 14 files, ~23,900L (complex adaptive system).

  Cross-ref: Inter-Body-Mechanism.md v2.0 §1 (Compilable Architecture full detail).
```

---

## §2 — ⭐ Full Pipeline Visualization (6 layers)

```
⭐⭐ BODY-FEEDBACK PIPELINE — TỪ HARDWARE ĐẾN PFC + INTER-BODY:

  ┌─────────────────────────────────────────────────────────────────┐
  │  LAYER 1: HARDWARE FOUNDATION                                   │
  │                                                                 │
  │  3 foundations → Compilable Architecture:                       │
  │    ① General-Purpose Reward (fire cho BẤT KỲ gap fill)          │
  │    ② Compilation Capability (Hebbian → automatic evaluation)   │
  │    ③ Social Hardware (oxytocin, μ-opioid, dACC reuse)           │
  │                                                                 │
  │  Ref: Inter-Body-Mechanism.md v2.0 §1, Body-Base.md v3.2 §1    │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 2: SIGNAL GENERATION                                     │
  │                                                                 │
  │  2 sources:                                                     │
  │    ① Sensory-Driven (domain → body → chunks fire reactive)     │
  │    ② Pattern-Driven (chunks fire nội bộ → body respond)        │
  │  × 3 dynamics:                                                  │
  │    ① Chunk-Shift (cùng chunks, KHÁC valence)                   │
  │    ② Chunk-Miss (compiled pattern KHÔNG fire)                   │
  │    ③ Chunk-Gap (network detect pattern THIẾU)                   │
  │  + Compound (1 event → nhiều dynamics)                          │
  │  → Body-Need = aggregate output                                 │
  │                                                                 │
  │  Ref: Body-Feedback-Mechanism.md v2.0                           │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 3: SIGNAL ARCHITECTURE                                   │
  │                                                                 │
  │  2 loại reward (orthogonal dimension):                          │
  │    Evaluative Reward (μ-opioid, requires H10 full)              │
  │    Direct-State Reward (CT afferents, eCB, hardware-based)      │
  │  × E₀→E₃ complexity gradient (compilation depth)               │
  │  × 5 Profiles ("hương vị" reward)                               │
  │  H10 = 5 preconditions → signal fire/not fire                  │
  │                                                                 │
  │  Ref: Reward-Signal-Architecture.md v2.0, 03-Reward.md         │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 4: GAP SYSTEM                                            │
  │                                                                 │
  │  Gap Direction = f(surrounding chunks) — WHY reward personal   │
  │  3 Satiation Profiles (Cyclic/Tonic/Generative) — HOW gaps feed │
  │  5-Parameter per-gap model — integrated observation             │
  │  ENGINE/ROAD/VEHICLE architecture — hardware/collective/compile │
  │  Gap Distribution = per-person aggregate landscape              │
  │                                                                 │
  │  Ref: Gap-Direction, Gap-Body-Need, Gap-Distribution-Profile    │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 5: AGGREGATE OBSERVATION                                  │
  │                                                                 │
  │  Gap-Distribution = DEMAND ("muốn gì")                         │
  │  Action-Space = SUPPLY ("có thể gì")                            │
  │  Behavior = f(DEMAND × SUPPLY) — 4 quadrants                   │
  │  Reward Calibration = Goldilocks per-gap, dynamic equilibrium  │
  │  Hidden Quality = compilation depth → quality visibility        │
  │                                                                 │
  │  Ref: Action-Space, Gap-Distribution-Profile,                   │
  │       Reward-Calibration, Hidden-Quality-Perception              │
  ├─────────────────────────────────────────────────────────────────┤
  │  LAYER 6: PFC OBSERVATION + INTER-BODY                           │
  │                                                                 │
  │  Feeling = PFC observation of body-feedback (7-layer)           │
  │  Body-feedback (mechanism) ≠ Feeling (PFC observation)          │
  │  Inter-body: by-product match, Entity-Compiled, 5-Channel      │
  │  Body-Coupling: 4 bond types, firing modes                     │
  │                                                                 │
  │  Ref: Feeling.md v3.0, Inter-Body-Mechanism.md v2.0,            │
  │       Body-Coupling.md v3.0                                      │
  └─────────────────────────────────────────────────────────────────┘

  NOTE: Layers = conceptual hierarchy, không phải temporal sequence.
  Signal generation (Layer 2) + architecture (Layer 3) xảy ra near-parallel.
  Gap system (Layer 4) = accumulated structure shaping real-time signals.
  PFC observation (Layer 6) = SEPARATE process, không phải "output" của pipeline.
```

---

## §3 — Dual-Pull + Interface Loop + 3 Genuine Discomfort Sources

### §3.1 — Dual-Pull Architecture

```
⭐ DUAL-PULL = KIẾN TRÚC NỀN TẢNG CỦA BODY SIGNAL:

  Schema (chunks) bị kéo ĐỒNG THỜI bởi 2 lực:

  ① HARDWARE PULL (nội, bảo thủ, muốn smooth):
     → Hebbian LTP: patterns quen càng mạnh
     → Habituation: VTA quen → không fire → smooth
     → Metabolic efficiency: compiled = low cost
     → Feature: comfort zone, routine, contentment
     → Dark side: stagnation, evolution lag

  ② DOMAIN PULL (ngoại, đòi adapt, map reality):
     → Novelty drive: genetic drive explore
     → prediction-delta: pattern mới → dopamine → attention
     → Evolutionary: không map reality → không sống sót
     → Feature: learning, growth, curiosity
     → Dark side: burnout, neural wear

  ⭐ TENSION = EVOLUTIONARY FEATURE, NOT BUG:
     → Chỉ Hardware → stagnation → domain thay đổi → chết
     → Chỉ Domain → burnout → resource exhausted → chết
     → CẢ HAI → oscillation consolidation ↔ exploration → thrive

  → Reward fires khi 2 lực ALIGN ("passion" = body thích + domain cần)
  → Dissonance fires khi 2 lực CONFLICT

  Compiled/Fresh connection (Inter-Body-Mechanism.md v2.0 §3):
  → Hardware pull = toward COMPILED (efficient, low cost)
  → Domain pull = toward FRESH evaluation when reality shifts
  → Dual-pull = Compiled/Fresh tension at SYSTEM level

  "Melody hay" 4 criteria (Personal-Melody.md v2.0 §5):
  ① Mượt trên hardware ② Map domain chính xác ③ Cover rộng ④ Bền vững

  See: Drill-Body-Feedback/01-Foundation.md §2 for full detail.
```

### §3.2 — Interface Loop 6-Step

```
⭐ 6-STEP INTERFACE LOOP — HOW BODY-DOMAIN INTERACTION RUNS:

  Step 1: DOMAIN → BODY sensory (external reality → neural transduction)
       ↓
  Step 2: BODY → FEEDBACK (vô thức 95% OR PFC 5% — match? coherence?)
       ↓
  Step 3: FEEDBACK → SCHEMA UPDATE (compile new / modify / reconsolidate)
       ↓
  Step 4: SCHEMA → ACTION (compiled schemas fire → motor output)
       ↓
  Step 5: ACTION → DOMAIN (body affects world)
       ↓
  Step 6: DOMAIN → BODY feedback (reality responds → loop closure → Step 1)

  NOTE: Feeling-Mechanism-Deep-Draft.md §3 has DIFFERENT 8-step model:
    → 8-step = MICRO process (within body, per feeling episode)
    → 6-step = MACRO loop (organism ↔ environment)
    → COMPLEMENTARY, not competing. Different zoom level.

  Domain Reality = Final Arbiter (Inter-Body-Mechanism.md v2.0 §1):
  → Step 6 = WHERE domain confirms/rejects body's action
  → Body compiles from Step 6 outcome (not from Step 4 intention)
  → = WHY "thử đi" works: body learns from domain feedback, not PFC plan

  See: Drill-Body-Feedback/01-Foundation.md §3 for full detail.
```

### §3.3 — 3 Genuine Discomfort Sources

```
⭐ CRITICAL REFRAME: CORTISOL KHÔNG GÂY ĐAU.

  🟢 Cortisol injection (healthy subjects): cortisol ↑ → NO pain
  🟢 Addison's disease (cortisol ≈ 0): patients VERY uncomfortable
  → "Reduce cortisol" = wrong strategy. "Fix mismatch" = right strategy.

  3 GENUINE DISCOMFORT SOURCES (Cortisol-Baseline.md v2.1 §2.5):

  ① NOCICEPTION: tissue damage → nociceptors → pain.
     Cortisol arrives AFTER. Fix: protect + repair source.

  ② MISMATCH: schema expects X, reality ≠ X.
     Signal fires FIRST → cortisol SECOND (support fix).
     Fix: update schema OR change reality. = CORE of almost ALL dissonance.

  ③ RECALIBRATION: mismatch detected → body activates pattern change.
     Temporarily unstable = discomfort. Analogy: muscle soreness from gym.
     Fix: endure — process ends when new pattern stable.

  ⭐ TREATMENT IMPLICATION:
    Target MISMATCH (root): solve problem, update expectations, accept unchangeable
    ONLY reducing cortisol (symptom): substance, dissociation, distraction
    → Risk: mismatch continues → body fires again → escalation

  See: Drill-Body-Feedback/02-Dissonance.md §3 for full detail.
```

---

## §4 — Signal Generation + Body-Need

```
⭐ 4TH CLASSIFICATION AXIS — HOW CHUNKS FIRE TẠO RA SIGNAL:

  Body-feedback có 4 trục phân loại ORTHOGONAL:
    Trục 1: Direction (reward/dissonance/neutral)
    Trục 2: Magnitude (14 levels)
    Trục 3: Source (nociception/mismatch/recalibration)
    Trục 4: CHUNK DYNAMICS ← core mechanism

  2 NGUỒN ĐẦU VÀO (Body-Feedback-Mechanism.md v2.0 §2):

    ① SENSORY-DRIVEN: Domain → body-input → chunks fire reactive
       → Animals đầy đủ. No PFC needed. Timing: ms→seconds.
       → VD: kim đâm, đồ ăn ngon, nhạc hay, trời nóng

    ② PATTERN-DRIVEN: Chunks fire nội bộ → body respond theo
       → Replay, preview, comparison, gap detect, spreading activation
       → VD: nhớ lại, Imagine-Final preview, social comparison

  3 CHUNK DYNAMICS (Body-Feedback-Mechanism.md v2.0 §3):

    ① CHUNK-SHIFT: cùng chunks, KHÁC valence (đánh giá thay đổi)
       → VD: phản bội → chunks người yêu vẫn đó, valence flip
       → 🟢 Evaluative conditioning (De Houwer 2007)

    ② CHUNK-MISS: pattern đã compiled KHÔNG FIRE (absent/degraded)
       → VD: TikTok quen → máy hỏng → bứt rứt
       → 🟢 Successive Negative Contrast (Crespi 1942, Flaherty 1996)

    ③ CHUNK-GAP: pattern CHƯA CÓ nhưng network detect thiếu
       → VD: Einstein → vật lý mâu thuẫn → drive giải
       → Gap-Direction.md v2.0: gap có DIRECTION = f(surrounding chunks)
       → 🟢 Information gap theory (Loewenstein 1994)

  COMPOUND: 1 event → nhiều dynamics cùng lúc
    → Rơi 100k = Chunk-Miss (tiếc)
    → Bị lừa 100k = Miss + Shift (tiếc + tức)
    → Bị bạn thân lừa 100k = Miss + Shift + Gap (tiếc + tức + cay đắng)

  QUALITY BASELINE SHIFT (SNC research):
    → Body compile quality X → habituate → quality giảm = Chunk-Miss
    → 🟢 SNC: rats downshift good→normal → eat LESS than always-normal rats
    → Asymmetric: loss hurts ~2x gain (🟢 Kahneman & Tversky 1979)

  BODY-NEED = 2-SOURCE AGGREGATE (Body-Feedback-Mechanism.md v2.0 §1):
    → Body-need = hardware signals + chunk dynamics COMBINED
    → 7 properties: dynamic, multi-source, not fully PFC-accessible,
      partially compilable, has immediacy, can conflict internally, aggregate
    → 4 immediacy types: Acute / Chronic / Background / Emergent
    → Complexity Spectrum: Simple→Social→Meta (cùng mechanism, khác substrate)

  See: Body-Feedback-Mechanism.md v2.0 for full detail (1,519L).
```

---

## §5 — Signal Architecture + H10

### §5.1 — Evaluative/Direct-State Reward

```
🟡 REWARD SIGNAL CÓ 2 LOẠI — ORTHOGONAL DIMENSION:

  ┌────────────────────────────────────────────────────────────┐
  │  EVALUATIVE REWARD                                         │
  │                                                            │
  │  Circuit: Hedonic hotspot (NAcc shell, VP, mOFC)          │
  │  Signal: μ-opioid + endocannabinoid (dependent)           │
  │  H10: Full 5 preconditions required                       │
  │  Requires: Compiled chunks (P2) + body-need gap (P1)     │
  │  Learned: YES — quality depends on chunk library          │
  │  Examples: Food appreciation, music, insight, social praise│
  ├────────────────────────────────────────────────────────────┤
  │  DIRECT-STATE REWARD                                       │
  │                                                            │
  │  Circuit: Interoceptive / body-state (VARIES by modality) │
  │  Signal: CT afferents (🟢 Löken 2009), eCB (🟢 Fuss 2015)│
  │  H10: Simplified (P1 basic, P2-P5 reduced/N/A)           │
  │  Requires: Hardware pathways (minimal compiled chunks)    │
  │  Learned: MINIMAL — hardware from birth                   │
  │  Examples: Touch comfort, runner's high, warmth, stretching│
  └────────────────────────────────────────────────────────────┘

  → Evaluative = RICH but CONDITIONAL on compilation
  → Direct-State = RELIABLE, always-available baseline ("evolutionary floor")
  → Loss of Evaluative (burnout) → Direct-State remains ("touch still good")
  → Evaluative × Direct-State CẮT NGANG mọi profile:
    Profile ① Sensory: food = Evaluative, touch = Direct-State
    Profile ③ Social: praise = Evaluative, proximity = Direct-State
  → 5 Profiles = "hương vị" reward (Sensory/Coherence/Social/Relief/Mastery)
  → E₀→E₃ gradient = compilation depth applied to evaluation

  See: Reward-Signal-Architecture.md v2.0 for full detail (1,987L).
```

### §5.2 — H10 Body Signal Precondition Hypothesis

```
⭐ H10 v3 — 5 PRECONDITIONS FOR BODY SIGNAL:

  Body signal (reward hoặc dissonance) = function of 5 PRECONDITIONS
  đồng thời trên interface loop:

  ┌───┬──────────────────────┬──────────────────────────┐
  │ # │ Precondition         │ Failure → subjective     │
  ├───┼──────────────────────┼──────────────────────────┤
  │P1 │ Schema pending       │ "Không cần" / "không     │
  │   │ (body-need gap open) │  muốn" → polite no       │
  ├───┼──────────────────────┼──────────────────────────┤
  │P2 │ Chunks base adequate │ "Chả hiểu" / confusion   │
  │   │ (đủ substrate)       │                          │
  ├───┼──────────────────────┼──────────────────────────┤
  │P3 │ prediction-delta     │ "Bình thường" / "quen"   │
  │   │ threshold            │                          │
  ├───┼──────────────────────┼──────────────────────────┤
  │P4 │ Goldilocks zone      │ Too alien: "lạ quá"      │
  │   │ (~40-70% match)      │ Too familiar: "chán"     │
  ├───┼──────────────────────┼──────────────────────────┤
  │P5 │ Chunk association tag│ "Ghét dù hiểu" /         │
  │   │ (opioid vs cortisol) │  avoidance despite fit   │
  └───┴──────────────────────┴──────────────────────────┘

  ALL 5 REQUIRED for full signal. Missing ANY → signal absent or wrong direction.

  ⭐ 2-LAYER INTERPRETATION (Gap-Direction.md v2.0 §6):
    P2→P1 = Layer 2 prerequisites: gap direction phải TỒN TẠI
    P3 = Layer 1: signal mechanism fire (VTA detect delta)
    P4→P5 = Layer 2 quality: direction match evaluation
    "Chưa biết = không có gap" = TRƯỚC cả P1:
      Không có chunks → gap chưa hình thành → desire chưa tồn tại

  ⭐ H10 × EVALUATIVE/DIRECT-STATE (Reward-Signal-Architecture.md v2.0 §1.3):
    Evaluative: ALL 5 preconditions required (full evaluation)
    Direct-State: P1 simplified, P2-P5 reduced/N/A (hardware pathways)
    → Direct-State = RELIABLE (not gated by chunks)
    → Evaluative = RICH but CONDITIONAL on compilation

  H10 PREDICTS:
    → Reward variation across individuals (same stimulus, different chunks)
    → Hedonic adaptation (baseline shift → Goldilocks target moves)
    → Flow state (all 5 aligned + continuous feed)
    → Art appreciation gradient (chunks build → match enters Goldilocks)
    → Per-person reward (same object → different reward per chunks base)

  See: Drill-Body-Feedback/03-Reward.md §3 + 04-Integration.md §9 for full detail.
```

---

## §6 — ⭐ Gap System

### §6.1 — Gap Direction

```
⭐ GAP DIRECTION = f(SURROUNDING CHUNK NETWORK STRUCTURE):

  Gap = hole in chunk network nơi structure PREDICT pattern C nên tồn tại
        nhưng C CHƯA COMPILED. Surrounding chunks define "borders" of hole.

  "Chưa biết = không có gap":
    → Without chunks → no borders → no hole → NO GAP
    → Bạn KHÔNG THỂ thiếu thứ bạn không biết tồn tại
    → E=mc² cho Einstein = direction match (years of physics chunks predict)
    → E=mc² cho học sinh lớp 3 = no direction match (insufficient borders)
    → CÙNG information, KHÁC gap landscape → KHÁC reward

  Reward = DIRECTION MATCH quality:
    → prediction-delta (Schultz 1997) = detect mechanism (CÓ GÌ ĐÓ KHÁC)
    → Gap direction = content (KHÁC CÁI GÌ CỤ THỂ)
    → Cần CẢ HAI để giải thích tại sao reward là PERSONAL

  2-layer model:
    Layer 1: signal mechanism (VTA detection — SAME cho all humans)
    Layer 2: direction content (chunk network — UNIQUE per person)

  By-product match connection: gap direction = WHY by-product match works
    → B's output match A's gap DIRECTION → A's body reward fires
    → Gap overlap → by-product match probability

  See: Gap-Direction.md v2.0 for full detail (2,681L).
```

### §6.2 — 3 Satiation Profiles

```
🟡 3 SATIATION PROFILES — HOW DIFFERENT GAPS CONSUME:

  ① CYCLIC: fill → satiation CLEAR → gap DORMANT → return after interval
     → Examples: hunger (fill→satisfied→dormant 4-6h→return), safety checking
     → Hormone-linked: ghrelin/leptin cycle, cortisol circadian
     → Body KNOWS "đủ rồi" — clear stop signal

  ② TONIC: fill ongoing → habituate SLOW → background satisfaction
     → Examples: social touch (CT afferents), ambient comfort, companionship
     → Weber-Fechner: logarithmic habituation (chậm, không abrupt)
     → ONGOING fill = ONGOING reward (khác Cyclic clear stop)

  ③ GENERATIVE: fill → CREATE NEW gaps → perpetual expansion
     → Examples: curiosity (answer → new questions), mastery (learn → see more gaps)
     → Self-sustaining: satisfaction = source of next gap
     → Aron & Aron 1996: self-expansion model
     → "Càng biết nhiều càng biết mình chưa biết" = Generative in action

  TRANSITIONS possible:
    Cyclic → Generative: food → culinary exploration
    Generative → Tonic: intense curiosity → settled expertise maintenance

  5-PARAMETER per-gap model:
    ① Source (hardware sensor/hormone/coherence?)
    ② Satiation (Cyclic/Tonic/Generative?)
    ③ Reward (Evaluative : Direct-State ratio?)
    ④ Chain (fill trực tiếp hay qua bao nhiêu bước?)
    ⑤ Dependency (cần bao nhiêu infrastructure?)

  ENGINE/ROAD/VEHICLE architecture:
    ENGINE (Hardware) = source of ALL drives. Luôn running.
    ROAD (Collective-Arc) = infrastructure to fill. NOT opposing force.
    VEHICLE (Compilation) = individual's compiled chains. 15-20 năm build.

  See: Gap-Body-Need.md v1.0 for full detail (1,388L).
```

### §6.3 — Gap Distribution Profile

```
🟡 GAP DISTRIBUTION = PER-PERSON GAP LANDSCAPE:

  Mỗi người = 1 GAP DISTRIBUTION riêng — tổng thể các gap đang active.

  4 TRỤC QUAN SÁT:
    ① Domain Center: gaps cluster ở domain NÀO? (arts/science/social/practical)
    ② Origin Balance: hardware-origin vs compiled-origin ratio?
    ③ Depth Profile: shallow-broad hay narrow-deep?
    ④ Stability: đang stable hay đang shift?

  4-TẦNG FORMATION (gap landscape HÌNH THÀNH bởi):
    Tầng 1: Collective-Arc (era, culture → install baseline gaps)
    Tầng 2: Schemas (education, media → shape gap directions)
    Tầng 3: Family/Micro-environment (gia đình, bạn bè → specific gaps)
    Tầng 4: Hardware + Experience (genes, personal events → unique gaps)

  RESONANCE PREDICTION:
    → 2 người overlap gap distribution → by-product match probability CAO
    → "Hợp tính" = gap distribution overlap (By-Product-Gap-Resonance.md v1.4)
    → Collective installs SAME baseline → tầng 1 overlap dễ → "đồng bào"
    → Domain-specific gaps → tầng 2-3 overlap → "đồng nghiệp", "tri kỷ"

  See: Gap-Distribution-Profile.md v1.1 for full detail (2,370L).
```

### §6.4 — Behavioral Prediction: DEMAND × SUPPLY

```
⭐ HÀNH VI THỰC TẾ = f(Gap-Distribution × Action-Space):

  Gap-Distribution (DEMAND): "Tôi MUỐN gì?" — gaps cluster ở đâu
  Action-Space (SUPPLY): "Tôi CÓ THỂ gì?" — options available ở đâu
  Behavior: GIAO CỦA HAI — chỉ nơi gap VÀ option GẶP NHAU → action

  Action-Space 4 trục:
    ① Compiled Capacity (biết gì, kỹ năng gì)
    ② Resource Access (tiền, network, công cụ)
    ③ Freedom (được phép gì, nghĩa vụ nào ràng buộc)
    ④ Awareness (NHẬN THỨC được bao nhiêu options — invisible = nguy hiểm nhất)

  4 QUADRANTS:
    ┌────────────────────────────────┬────────────────────────────────┐
    │ DEMAND cao + SUPPLY cao        │ DEMAND cao + SUPPLY thấp       │
    │ = ACTIVE PURSUIT               │ = FRUSTRATION / STUCK          │
    │ Muốn + có thể → hành động     │ Muốn + không thể → đau khổ    │
    ├────────────────────────────────┼────────────────────────────────┤
    │ DEMAND thấp + SUPPLY cao       │ DEMAND thấp + SUPPLY thấp      │
    │ = DRIFT / WASTE                │ = SIMPLE / TRAPPED             │
    │ Có thể + không muốn → no drive│ Không muốn + không thể → hẹp  │
    └────────────────────────────────┴────────────────────────────────┘

  See: Action-Space.md v1.0 (1,729L) + Gap-Distribution-Profile.md v1.1 (2,370L).
```

---

## §7 — ⭐ Quality + Calibration

### §7.1 — Reward Calibration

```
🟡 GOLDILOCKS PER-GAP: BAO NHIÊU REWARD LÀ ENOUGH?

  3 ZONES:
    Under-reward: gap fill insufficient → dissonance persists
    Match (Goldilocks): gap fill proportional → clean reward
    Over-reward: gap fill excessive → 6 degradation mechanisms

  6 OVER-REWARD MECHANISMS:
    ① Threshold Adaptation (baseline shifts UP → need MORE)
    ② Overjustification (external reward erodes intrinsic — 🟢 Deci 1971)
    ③ Bridge Dependency (depend on external source for fill)
    ④ Baseline Shift (compiled quality X → habituate → X = new normal)
    ⑤ Competence-Reward Mismatch (rewarded despite low quality)
    ⑥ Evaluative/Direct-State Imbalance (one type dominant)

  ⭐ CANNOT PRESCRIBE — ONLY OBSERVE + ADJUST:
    → Goldilocks = per-gap, per-person, per-context
    → No universal "correct amount" of reward
    → Dynamic equilibrium (parallel Logic-Feeling-Balance.md)
    → Domain feedback = only arbiter of calibration quality

  See: Reward-Calibration.md v1.1 for full detail (1,356L).
```

### §7.2 — Hidden Quality Perception

```
🟡 HIDDEN QUALITY = "Chưa biết = không có gap" × QUALITY:

  Core mechanism:
    Chunks_about_quality_dimension_X = ∅
    → Gap_about_quality_of_X = IMPOSSIBLE
    → Body-feedback about X = SILENT
    → X bị bỏ qua — KHÔNG vì cẩu thả, mà vì CƠ CHẾ

  2 TYPES:
    ① DOMAIN EXPERT: đi qua mọi layer → THẤY technical quality ẩn
       → Bác sĩ THẤY bất thường X-ray 200ms (🟢 Reingold 2001)
       → Lập trình viên senior THẤY code smell mà junior miss
       → "Mặt lưng cái tủ" (Steve Jobs)

    ② LEADER/COORDINATOR: đi qua mọi vị trí → THẤY organizational quality ẩn
       → CEO bottom-up THẤY team kiệt sức dù metrics đẹp
       → 🟢 Goodall 2009: physician-CEOs outperform
       → 🟢 Benson, Li & Shue 2019: Peter Principle empirical (N=38,843)

  COPIER vs EXPERT: "giống hệt" nhưng DIVERGES over time
    → Copier thiếu chunks về hidden dimensions → no gap → no body signal
    → Expert HAS chunks → HAS gap → body SIGNALS when quality drops
    → Short term: indistinguishable. Long term: copier output degrades.

  DUNNING-KRUGER = META-LEVEL APPLICATION:
    → "Chưa biết = không có gap" áp dụng lên CHÍNH năng lực đánh giá
    → Người kém KHÔNG BIẾT mình kém (vì thiếu chunks để detect kém)
    → 🟢 Kruger & Dunning 1999: metacognitive deficit

  See: Hidden-Quality-Perception.md v1.0 for full detail (1,738L).
```

---

## §8 — Case Analyses + Special Mechanisms (pointers)

### §8.1 — Case Pointers

```
KEY CASES (full analysis in drill files):

  → Ô tô Paradox (5 scenarios): H10 preconditions × same gift → opposite reward
    See: Drill-Body-Feedback/03-Reward.md §5

  → Van Gogh Appreciation Gradient: chunks base growth → Goldilocks → reward
    See: Drill-Body-Feedback/03-Reward.md §6

  → Schema Update Latency (C5): positive event → mini dissonance → delayed reward
    See: Drill-Body-Feedback/03-Reward.md §8

  → Mini Dissonance is CONSTANT: 3 sources (historical/Imagine-Final/social comparison)
    See: Drill-Body-Feedback/02-Dissonance.md §2.6

  → Effort-Proportional Reward: more effort → more dissonance → larger opioid at resolution
    See: Drill-Body-Feedback/03-Reward.md §4.7
```

### §8.2 — Trauma Loop + Hedonic Trap (key insights)

```
TRAUMA LOOP 4-STAGE (Drill-Body-Feedback/02-Dissonance.md §8):
  → Stage 1: trauma event → emotional peak compile → cortisol-tagged chunks
  → Stage 2: PFC = Lawyer — creates narrative nhưng body KHÔNG tin
  → Stage 3: chronic cortisol → sleep quality degradation → recovery broken
  → Stage 4: PFC damage (🟢 Arnsten 2009) → worse solving → LOOP
  → Recovery: new chunks COMPETE with old trauma chunks for probability share

HEDONIC TRAP (Drill-Body-Feedback/02-Dissonance.md §9):
  → Schema maintenance cost: each active schema requires rehearsal
  → Pursue single goal → OTHER schemas unmaintained → DRIFT
  → Achievement → body check against CURRENT (drifted) schemas → mismatch → "trống rỗng"
  → Hedonic adaptation: baseline shifts → Goldilocks zone moves → need MORE
  → Prevention: maintain schema portfolio diversity = dual-pull balance
```

---

## §9 — Absorbed Content Map

```
CONTENT ABSORBED ELSEWHERE (authoritative versions in other files):

  ┌──────────────────────────────┬──────────────────────────────────────┐
  │ Body-Feedback-Draft content  │ Now authoritative in                 │
  ├──────────────────────────────┼──────────────────────────────────────┤
  │ Dopamine ≠ reward            │ Feeling-Mechanism-Deep-Draft.md §4.1 │
  │ VTA 7-step detection loop    │ Feeling-Mechanism-Deep-Draft.md §3.2 │
  │ H10 5 preconditions (table)  │ Feeling-Mechanism-Deep-Draft.md §4.3 │
  │ Eureka 4 cases               │ Feeling-Mechanism-Deep-Draft.md §4.4 │
  │ Body-feedback vs Feeling     │ Feeling-Mechanism-Deep-Draft.md §1   │
  │ Trauma feeling distortion    │ Feeling-Mechanism-Deep-Draft.md §6.4 │
  │ Body vote mechanism          │ Feeling-Chunk-Bridge-Draft.md §2.1   │
  │ Reward as feeling type       │ Feeling-Mechanism-Deep-Draft.md §4.5 │
  └──────────────────────────────┴──────────────────────────────────────┘

CONTENT UNIQUE TO THIS FOLDER (not absorbed):

  ┌──────────────────────────────┬──────────────────────────────────────┐
  │ Unique contribution          │ File + Section                       │
  ├──────────────────────────────┼──────────────────────────────────────┤
  │ ⭐ Body-Need 2-source model  │ Body-Feedback-Mechanism v2.0 §1     │
  │ ⭐ Chunk dynamics (4th axis) │ Body-Feedback-Mechanism v2.0 §2-§3  │
  │ ⭐ Gap direction model       │ Gap-Direction v2.0 (2-layer, 22 ex) │
  │ ⭐ 3 Satiation Profiles      │ Gap-Body-Need v1.0 §2              │
  │ ⭐ 5-Parameter per-gap model │ Gap-Body-Need v1.0 §6              │
  │ ⭐ ENGINE/ROAD/VEHICLE       │ Gap-Body-Need v1.0 §9              │
  │ ⭐ Gap distribution 4 trục   │ Gap-Distribution-Profile v1.1 §2    │
  │ ⭐ Reward architecture       │ Reward-Signal-Architecture v2.0 §1-§3│
  │   (Evaluative/Direct-State)  │ E₀→E₃, Evaluative Gates Direct-State│
  │ ⭐ 5 Reward Profiles         │ Reward-Signal-Architecture v2.0 §4  │
  │ ⭐ Reward calibration        │ Reward-Calibration v1.1 (Goldilocks)│
  │ ⭐ DEMAND × SUPPLY           │ Action-Space v1.0 §1.3+§8          │
  │ ⭐ Hidden Quality Perception │ Hidden-Quality-Perception v1.0 §1   │
  │ 2 input sources              │ Body-Feedback-Mechanism v2.0 §2     │
  │ Compound mechanism           │ Body-Feedback-Mechanism v2.0 §4     │
  │ Quality Baseline Shift       │ Body-Feedback-Mechanism v2.0 §5     │
  │ Technology fill dimension    │ Gap-Body-Need v1.0 §10              │
  │ Entity-gap matching          │ Gap-Body-Need v1.0 §11              │
  │ Gap lifecycle                │ Gap-Body-Need v1.0 §14              │
  │ Conditional Interaction Model│ Reward-Signal-Architecture v2.0 §6  │
  │ 5 Forces Holding Model       │ Reward-Signal-Architecture v2.0 §10 │
  │ 6 over-reward mechanisms     │ Reward-Calibration v1.1 §3          │
  │ Spiral dynamics supply-side  │ Action-Space v1.0 §4                │
  │ Copier vs Expert divergence  │ Hidden-Quality-Perception v1.0 §4   │
  │ Dunning-Kruger meta-level    │ Hidden-Quality-Perception v1.0 §5   │
  │ Dual-pull architecture       │ 01-Foundation §2                     │
  │ 6-step interface loop        │ 01-Foundation §3                     │
  │ "Melody hay" 4 criteria      │ 01-Foundation §2.5                   │
  │ 3 Genuine Discomfort Sources  │ 02-Dissonance §3                    │
  │ Mini dissonance 5 daily cases│ 02-Dissonance §2                    │
  │ Trauma loop 4-stage          │ 02-Dissonance §8                    │
  │ Hedonic trap mechanism       │ 02-Dissonance §9                    │
  │ Schema maintenance cost      │ 02-Dissonance §9                    │
  │ Ô tô paradox 5 scenarios    │ 03-Reward §5                        │
  │ Van Gogh appreciation grad.  │ 03-Reward §6                        │
  │ Schema update latency (C5)   │ 03-Reward §8                        │
  │ Effort-proportional reward   │ 03-Reward §4.7                      │
  │ H10 v3 full formalization    │ 04-Integration §9                   │
  │ 11 framework recommendations │ 04-Integration §12                  │
  └──────────────────────────────┴──────────────────────────────────────┘
```

---

## §10 — Honest Assessment + Cross-References

### §10.1 — Confidence breakdown

```
🟢 HIGH CONFIDENCE:

  ✓ Dopamine ≠ reward (Berridge & Robinson 1998, 2003)
  ✓ Cortisol = response/amplifier, not pain cause (Cortisol-Baseline evidence)
  ✓ Nociception mechanism established (Melzack & Wall gate control)
  ✓ Social pain uses physical pain pathway (Eisenberger 2003)
  ✓ Hedonic adaptation (Brickman 1978)
  ✓ Flashbulb memory / emotional peak compile (Brown & Kulik 1977)
  ✓ PFC damage from chronic stress (Arnsten 2009, McEwen 2007)
  ✓ Reconsolidation window (Nader 2000)
  ✓ Hebbian learning (Hebb 1949)
  ✓ Sleep consolidation mechanisms (Walker 2017)
  ✓ Evaluative opioid pathway (Berridge 2003, Mallik 2017)
  ✓ Direct-State non-opioid (Loseth 2019, Fuss 2015)
  ✓ Insula gradient (Craig 2002, 2013)
  ✓ SNC — Successive Negative Contrast (Crespi 1942, Flaherty 1996)
  ✓ Information gap theory (Loewenstein 1994)
  ✓ Perceptual learning as differentiation (Gibson & Gibson 1955)
  ✓ Expert recognition (Klein 1998, Chase & Simon 1973)
  ✓ Self-expansion model (Aron & Aron 1996, 2000)
  ✓ Capability Approach (Sen 1999)


🟡 MEDIUM CONFIDENCE:

  ⚠ Dual-pull as architectural principle (each pull established,
    integration as 2-force model = framework synthesis)
  ⚠ H10 5-precondition matrix (each precondition grounded,
    ALL-5-required claim = framework synthesis)
  ⚠ 3 Genuine Discomfort Sources taxonomy (each source established,
    3-category organizing = framework synthesis)
  ⚠ Schema maintenance cost (concept plausible, not directly measured)
  ⚠ Compilable Architecture = WHY folder complexity (framework organizing)
  ⚠ Compiled/Fresh × Dual-Pull mapping (logical, not tested)
  ⚠ Evaluative/Direct-State × H10 precondition mapping (framework synthesis)
  ⚠ 3 Satiation Profiles taxonomy (patterns observed, taxonomy = framework)
  ⚠ ENGINE/ROAD/VEHICLE architecture (each component grounded,
    3-component model = framework synthesis)
  ⚠ DEMAND × SUPPLY behavioral prediction (logical model,
    each side established, integration = framework)
  ⚠ Hidden Quality = gap landscape consequence (mechanism established,
    quality application = framework synthesis)
  ⚠ Dunning-Kruger as meta-level "chưa biết = không gap" (🟢 K&D 1999
    replicated, meta-level interpretation = framework)
  ⚠ 5-Parameter per-gap model (each parameter grounded,
    integrated model = framework synthesis)


🔴 LOW CONFIDENCE:

  ⚠ Goldilocks 40-70% specific percentages (inverted-U established,
    cutoffs = approximation)
  ⚠ Vô thức 95% / PFC 5% ratio (qualitative split established,
    specific percentages = heuristic)
```

### §10.2 — Cross-references

```
📚 WITHIN BODY-FEEDBACK/ FOLDER:

  Body-Feedback-Label.md v2.0    → vocabulary anchor (MUST-READ)
  Body-Feedback-Mechanism.md v2.0 → 2-source, Body-Need, 3 dynamics
  Gap-Direction.md v2.0          → gap direction, 2-layer, by-product match
  Gap-Body-Need.md v1.0          → 3 Satiation, 5-Parameter, ENGINE/ROAD/VEHICLE
  Gap-Distribution-Profile.md v1.1 → 4 trục, 4-tầng formation, resonance
  Reward-Signal-Architecture.md v2.0 → Evaluative/Direct-State, 5 Profiles
  Reward-Calibration.md v1.1     → Goldilocks per-gap, calibration
  Action-Space.md v1.0           → supply-side, DEMAND × SUPPLY
  Hidden-Quality-Perception.md v1.0 → quality visibility, 2 types
  Drill-Body-Feedback/01-Foundation.md → dual-pull, 6-step loop
  Drill-Body-Feedback/02-Dissonance.md → 3 Genuine Discomfort Sources, threat, trauma, hedonic
  Drill-Body-Feedback/03-Reward.md     → H10, ô tô paradox, Van Gogh
  Drill-Body-Feedback/04-Integration.md → walkthroughs, H10 v3


📚 BODY-BASE/ CONNECTIONS:

  Inter-Body-Mechanism.md v2.0   → Compilable Architecture, 3 foundations,
                                    Compiled/Fresh, 3-cost, domain arbiter
  Body-Base.md v3.2              → entry point, Compilable Architecture
  Body-Coupling.md v3.0          → coupling mechanism, firing modes, bond types
  Valence-Propagation.md v3.0    → structural/current, hardware subsidy, per-entity
  Cortisol-Baseline.md v2.1      → amplifier, 3 Genuine Discomfort Sources, chunk tag, 5 roles


📚 AGENT-MECHANISM/ CONNECTIONS:

  Self-Pattern-Modeling.md v3.1  → Compiled/Fresh, per-domain, 3 dimensions
  By-Product-Gap-Resonance.md v1.4 → 2-Stream, by-product match, 4 conditions
  Entity-Compiled.md v1.0        → Hub-and-Spoke, Formation, Grief A+B+C


📚 FEELING/ + PFC/ CONNECTIONS:

  Feeling.md v3.0                → 7-layer model, PFC observation
  Feeling-Mechanism-Deep-Draft.md → 8-step flow, reward definitive
  Feeling-Chunk-Bridge-Draft.md  → bidirectional mapping
  Imagine-Final.md v3.0          → constructive simulation, Gap→Miss
  PFC-Hardware.md v1.1           → COMT, DRD4, NE, VTA circuit


📚 OTHER FRAMEWORK FILES:

  Why-Body-Knows.md v1.2         → 2-tầng calibration, Dual Check
  Personal-Melody.md v2.0        → "Melody hay" 4 criteria
  Anchor-Schema.md               → 6-step flow, trust, 4 nguồn fill
  Ask-AI.md v3.1                 → Dual Check (body=QC, domain=arbiter)
  Logic-Feeling-Balance.md       → cannot prescribe balance, domain feedback


📚 KEY RESEARCH REFERENCES:

  Berridge K. & Robinson T. (1998, 2003) — wanting ≠ liking
  Brickman P. et al. (1978) — hedonic adaptation
  Eisenberger N. (2003) — social pain = physical pain circuits
  Arnsten A. (2009) — chronic stress → PFC damage
  McEwen B. (2007) — stress → brain structural changes
  Nader K. (2000) — memory reconsolidation
  Craig A.D. (2002, 2013) — interoceptive insula gradient
  Löken L. et al. (2009) — CT afferents
  Fuss J. et al. (2015) — exercise endocannabinoid
  Schultz W. (1997) — reward prediction error
  Crespi L. (1942) — successive negative contrast
  Kahneman D. & Tversky A. (1979) — loss aversion
  Loewenstein G. (1994) — information gap theory
  Gibson J. & Gibson E. (1955) — perceptual learning differentiation
  Klein G. (1998) — recognition-primed decision
  Sen A. (1999) — Capability Approach
  Kruger J. & Dunning D. (1999) — metacognitive deficit
  Aron A. & Aron E. (1996, 2000) — self-expansion model
  Kahneman D. & Deaton A. (2010) — income-wellbeing plateau
```

---

> **END OF Body-Feedback.md v3.0**
>
> **Summary:** Synthesis entry point for Body-Feedback/ folder (v3.0):
>   §1: Folder overview — 14 files, ~23,900L, 4-tier reading guide
>       +Compilable Architecture framing (WHY system this complex)
>   §2: ⭐ Full 6-layer pipeline: Hardware → Signal → Evaluate → Gap → Aggregate → PFC
>   §3: Dual-pull + 6-step interface loop + 3 Genuine Discomfort Sources (condensed)
>   §4: Chunk dynamics (2 sources × 3 dynamics × compound) + Body-Need
>   §5: Evaluative/Direct-State + H10 5-precondition hypothesis
>   §6: ⭐ Gap System (direction + 3 satiation + distribution + DEMAND×SUPPLY)
>   §7: ⭐ Quality + Calibration (reward calibration + hidden quality perception)
>   §8: Case analyses + special mechanisms (pointers to drill files)
>   §9: Absorbed content map (updated for 14 files, new unique contributions)
>   §10: Honest assessment + cross-references (all versions updated)
>
> **v2.0a → v3.0 changes:**
>   +§1.1: 10→14 files, Drill-Body-Feedback/ subfolder path corrected
>   +§1.2: 3-tier→4-tier reading guide (Gap Dynamics + Observation separated)
>   +§2: FULL 6-layer pipeline visualization (ALL NEW)
>   +§3: Dual-Pull + Loop + 3 Nguồn CONDENSED into 1 section
>   +§5.1: Evaluative/Direct-State summary (NEW section)
>   +§6: Gap System 4 subsections (ALL NEW — Gap-Direction, Satiation, Distribution, DEMAND×SUPPLY)
>   +§7: Quality + Calibration 2 subsections (ALL NEW — Reward-Calibration, Hidden-Quality)
>   +§8: Cases TRIMMED (~200L → ~60L pointers to drill files)
>   +§9: Unique contributions table EXPANDED (12 new ⭐ entries)
>   +§10.1: New 🟢 items (Gibson, Klein, Sen, Aron) + new 🟡 items (6 new framework synthesis claims)
>   +§10.2: ALL cross-refs updated — 14 internal files + external versions corrected
>   ALL research citations preserved + expanded (19→24)
>
> **Folder total:** 14 files, ~23,900L
> **Phiên bản:** v3.0, 2026-05-24.
