---
title: Plan — Drill Reward-Feeling → Framework Propagation
created: 2026-05-09
status: PLAN READY — chưa triển khai
purpose: |
  Drill Reward-Feeling đã hoàn thành (Main v1.2 ~6,700L + Cases v1.0 ~2,015L, ALL 20 GAPs).
  Plan này hướng dẫn propagate drill findings vào framework files.
  Tạo để cold-start session sau có thể triển khai trực tiếp.
source_files:
  - Drill-Reward-Feeling-Main.md (v1.2, ~6,700L) — ALL 20 GAPs COMPLETE
  - Drill-Reward-Feeling-Cases.md (v1.0, ~2,015L) — Data + cases companion
principle: "Chậm mà chắc. Quan trọng chất lượng."
language: Tiếng Việt primary + English technical terms
---

# Plan — Drill Reward-Feeling → Framework Propagation

> Drill đã hoàn thành. Giờ cần distill ~8,700L drill findings thành reference files
> trong framework. Plan này là bản đồ đầy đủ cho quá trình đó.
>
> **Nguyên tắc**: Mỗi session chỉ làm 1-2 file, làm kỹ, verify xong mới chuyển.

---

## §0 — Tổng Quan Quyết Định

### Đã phân tích kỹ và quyết định:

| Hành động | File | Ước tính | Lý do |
|-----------|------|----------|-------|
| **TẠO MỚI** | Reward-Signal-Architecture.md | ~1,500-2,000L | Concept mới hoàn toàn, scope khác 03-Reward |
| **TẠO MỚI** | PFC-Configuration.md | ~1,000-1,200L | Concept mới hoàn toàn, scope khác PFC-Function |
| **REFINE LỚN** | PFC-Hardware.md | 547→~1,000L | Extend COMT/DRD4 sang reward domain |
| **REFINE VỪA** | PFC-Function.md | 446→~550L | Thêm sub-region column + cross-refs |
| **REFINE VỪA** | Body-Feedback-Mechanism.md | 960→~1,100L | A/B × source + conditional interaction |
| **REFINE VỪA** | Feeling.md | 1,404→~1,500L | §6 Reward update với A/B + 5 Profiles |
| **REFINE NHẸ** | 03-Reward.md | 2,264→~2,300L | Metadata fix + cross-refs + Step 5 note |
| **REFINE NHẸ** | Compile-Taxonomy.md | 823→~860L | §3 thêm 4-Pathway × P5 Tag cross-ref |
| **REFINE NHẸ** | Dopamine-Reward-Rejection.md | 497→~530L | Type A/B refinement |
| **REFINE NHẸ** | Feeling-Mechanism-Deep.md | 1,291→~1,320L | §4 thêm A/B note |
| **MINOR** | Core-v7.8-Draft.md | +cross-ref | A/B trong architecture overview |
| **MINOR** | ~7 files Tầng 3 | +cross-refs | Terminology + references |
| **UPDATE** | 01-File-Index.md | Full update | Mọi file mới/refine |

### Quyết định KHÔNG làm:
- KHÔNG rewrite 03-Reward.md (nội dung 95% valid, chỉ thiếu cross-refs)
- KHÔNG backup old files (vì refine = extend, không xóa nội dung cũ)
- KHÔNG chèn file mới vào chuỗi P1→P4 trong Body-Feedback/
- KHÔNG tạo file Motor-Urgency riêng (motor urgency = subsection trong §4 Profiles của file mới)

---

## §1 — FILE MỚI #1: Reward-Signal-Architecture.md

### Vị trí: Core-Deep-Dive/Body-Base/Body-Feedback/Reward-Signal-Architecture.md

### Lý do tạo mới (không nhồi vào 03-Reward):
- 03-Reward trả lời: "WHEN reward fires" (H10 preconditions) + "HOW mechanism works" (7-step VTA)
- File mới trả lời: "WHAT KINDS of reward exist" + "HOW they interact"
- Câu hỏi khác → file khác
- 03-Reward đã 2,264L, thêm drill content sẽ quá dài (~4,000L+)
- Body-Feedback/ có convention: files chủ đề ngoài chuỗi P1-P4 (như BFM.md, Gap-Direction.md)

### Cấu trúc dự kiến (~1,500-2,000L):

```
§0 — POSITION + SCOPE
  - Complement 03-Reward (HOW → file này WHAT KINDS)
  - Source: Drill-Reward-Feeling-Main.md v1.2 (distilled)
  - Reading order: sau 03-Reward.md

§1 — TYPE A/B ORTHOGONAL DIMENSION
  - Type A = Evaluative (cortical evaluation → opioid)
    - Vulnerable to learning, context, PFC
    - VTA habituation (central) → hedonic treadmill
    - Naltrexone BLOCKS
  - Type B = Direct State Confirm (peripheral → non-opioid)
    - CT afferents → posterior insula
    - Receptor adaptation (modality-specific) → hedonic FLOOR
    - Naltrexone NO EFFECT (touch, exercise)
  - A/B = orthogonal to 5 Profiles (mỗi profile có A/B ratio riêng)
  - A/B = spectrum, not binary
  - Source: R1, R13 (Drill §3.7)
  - 🟢 Berridge, Loseth 2019, Fuss 2015, Siebers 2021

§2 — A₀→A₃ COMPLEXITY GRADIENT
  - A₀: Hardware-installed binary (neonate sweet = opioid, anencephalic confirm)
  - A₁: Basic compiled (familiar food preference)
  - A₂: Complex compiled (music, art appreciation)
  - A₃: Deep abstract (math beauty, Poincaré equivalence)
  - Gradient properties: onset latency, preview fidelity, compilation depth
  - A₀ = evolutionary shortcut (pre-compiled simplest evaluation)
  - Source: R19 (Drill §3.10)
  - 🟢 Steiner 1973, Blass 1991/1994, Berridge 2003

§3 — A GATES B MECHANISM
  - NOT single locus — posterior-to-anterior INSULA GRADIENT
  - 5-step process:
    1. B signal arrives (raw body state, posterior insula)
    2. A evaluation fires in parallel (cortical)
    3. Mid-insula context enrichment
    4. Anterior insula integration (A modulates B)
    5. ACC flags mismatch, OFC assigns value
  - 4 modulation outcomes: suppress / amplify / raw / mixed
  - Source: R18 (Drill §3.13)
  - 🟢 Craig 2002, 2009, 2013

§4 — 5 REWARD PROFILES ("hương vị" reward)
  - ① Sensory: opioid + specific receptor. Location: body area. Duration: WHILE
  - ② Coherence: opioid + ACC resolve + right aSTG. Location: diffuse. Duration: BURST+GLOW
    - Poincaré Equivalence: math=art=music beauty (Zeki 2014 mOFC shared)
    - Motor urgency = 3-component compound (fragility + arousal + verification) [R4]
    - Compulsive recheck behavior [Wiles pattern]
  - ③ Social: opioid + mirror + status update. Location: chest warmth. Duration: DURING+AFTERGLOW
  - ④ Relief: cortisol DROP dominant (NOT opioid-led). ≠ pleasure. = absence of pain
    - Eureka compounds: ② + ④ = double reward (Archimedes)
  - ⑤ Preview: opioid REDUCED (~20-60% fidelity). Replay of ①②③④
    - Fidelity gradient follows A₀→A₃ (B ~5-15%, A₃ ~60-80%) [R17]
  - Profile × A/B ratio: orthogonal dimension
  - Each profile = same opioid circuit + different INPUT SOURCES + CONCURRENT BODY SIGNALS
  - Source: R1, R4, R5, R17 (Drill §2-§3)

§5 — TEMPORAL STACK MODEL
  - Onset follows A₀→A₃ gradient:
    B direct ~20ms → A₀ binary ~50ms → A₁ ~100-300ms → A₂ ~500ms-1s → A₃ ~1-5s
  - A₃ afterglow = 4 overlapping curves:
    ① Consolidation (chunk strengthening)
    ② Relief (dissonance resolved)
    ③ Background cascade (spreading activation continues)
    ④ Verification (compulsive recheck motor urgency)
  - Compound envelope = subjective experience
  - Source: R5 (Drill §3.14)

§6 — CONDITIONAL INTERACTION MODEL
  - NOT additive, NOT multiplicative — CONDITIONAL on 4 variables:
    ① Substrate overlap (shared neural substrate → subadditive, not 1+1=2)
    ② A gate direction (A suppress B, amplify B, or raw B)
    ③ Relief presence (multiplier effect when ④ compounds with ①②③)
    ④ Temporal overlap (simultaneous → compound quality, sequential → distinct)
  - Eureka = ② + ④ compound (not just ② alone)
  - Source: R7 (Drill §3.15)

§7 — 3 TYPES STATE DEPENDENCE (Cabanac Refined)
  - Type 1: Sensor-level (physics) — B territory
    Temperature adaptation, receptor saturation
  - Type 2: Evaluation-level (classical alliesthesia) — A territory
    Full vs hungry, context changes A evaluation
  - Type 3: Gate-level (A modulates B) — A×B interaction
    Same B input, different A context → different integrated experience
  - Cabanac 1971 alliesthesia = primarily Type 2 (A territory)
  - Source: R14 (Drill §3.9)

§8 — DEVELOPMENT + INDIVIDUAL DIFFERENCES OVERVIEW
  §8.1 — Development Lifecycle:
    Neonate (95% B + 5% A₀) → Childhood (B dominant, A building)
    → Adult (A peaks, B stable) → Old age (A declines, B resurfaces)
  §8.2 — 4 Sensitive Periods (NOT critical — reconsolidation possible):
    Foundation(0-3), Exploration(3-7), Deepening(7-12), Identity(12-18)
  §8.3 — Compound Tag Accumulation:
    Bidirectional snowball, negative > positive asymmetry
    Overjustification = P5 Tag Overwrite (Lepper 1973)
  §8.4 — 4-Pathway × P5 Tag Model (→ Compile-Taxonomy §3):
    HW Fit→approach, Trust→moderate, Social→neutral, Threat→avoidance
  §8.5 — 5-Axis Individual Differences:
    ① Hardware Architecture, ② Childhood Compilation, ③ Domain Exposure,
    ④ Channel Balance, ⑤ Current State
    Type B = "democratic reward" (less hardware-dependent)
    COMT × DRD4 interaction → 4 compound types (→ PFC-Hardware)
    4 Departure Patterns: precocious/extended/arrested/reversed
  Source: R6 (§3.21), R8 (§3.22), R3ext (§3.20)

§9 — KEY EVIDENCE TABLE
  - Naltrexone evidence (8 modalities): blocks A, no effect B
  - Endocannabinoid multi-role: amplifier (Type A NAcc) vs primary (Type B exercise)
  - A/B development gradient cases (6 stages)
  - Source: Cases v1.0 §9

§10 — 5 FORCES HOLDING MODEL (long creative arcs)
  - F1 Meaning/Anchor-Schema (macro direction)
  - F2 Gap-Direction P1 (specific pending)
  - F3 ② Micro-Rewards (continuous opioid drip)
  - F4 Trust Thái Độ (body-base smooth với collective, ≠ trust nội dung)
  - F5 Recognition (status = resource access → material reward)
  - Source: R3 extended (Drill §3.20)

§11 — HONEST ASSESSMENT + PREDICTIONS
  - Strength: 50+ 🟢 research citations integrated
  - Framework synthesis: 60+ 🟡 items consistent but framework-specific
  - Testable: 40+ 🔴 numbered predictions (P-R1a through P-R20d)
  - Limitations: A/B ratios illustrative, A₀→A₃ organizing framework,
    onset latencies estimated, interaction model qualitative
  - Source: Drill §11

§12 — CROSS-REFERENCES
  - 03-Reward.md — HOW (preconditions) → file này WHAT KINDS
  - Body-Feedback-Mechanism.md — chunk dynamics + A/B mapping
  - Feeling.md — feeling = PFC observation of reward signal
  - PFC-Configuration.md — 6 modes × reward interaction
  - PFC-Hardware.md — COMT/DRD4 × reward patterns
  - Compile-Taxonomy.md — 4 pathways × P5 tag
  - Dopamine-Reward-Rejection.md — dopamine = alert, Type A opioid = reward
  - Liking-Wanting.md — bridge Berridge
  - Cortisol-Baseline.md — relief profile ④
  - Drill-Reward-Feeling-Main.md — full drill source
  - Drill-Reward-Feeling-Cases.md — data + cases source
```

### Nguồn để viết:
- Drill Main: §2 (5 Profiles), §3.7-§3.22 (ALL drilled sections), §5b (PFC Spectrum)
- Drill Cases: §2, §5, §9, §10
- KHÔNG copy drill text — DISTILL thành reference format

### Quality checklist:
- [ ] Mỗi claim có confidence tag (🟢🟡🔴)
- [ ] Mỗi section có source reference (Drill §X.Y)
- [ ] Cross-refs verify đúng file names + section numbers hiện tại
- [ ] Terminology consistent với framework v7.8
- [ ] Không dùng personal info (memory rule)
- [ ] "Imagine-Final" không viết tắt

---

## §2 — FILE MỚI #2: PFC-Configuration.md

### Vị trí: Core-Deep-Dive/PFC/PFC-Configuration.md

### Lý do tạo mới (không nhồi vào PFC-Function):
- PFC-Function = WHAT (24 functions, individual) — 446L, compact, well-structured
- PFC-Configuration = HOW functions COMBINE in different states — tầng abstraction khác
- PFC folder convention: Function/Hardware/Development/Hold — thêm Configuration tự nhiên
- 6 modes + survival matrix + control spectrum = ~800L+ content mới
- Nhồi vào PFC-Function sẽ gấp 3 lần kích thước, vỡ focus

### Cấu trúc dự kiến (~1,000-1,200L):

```
§0 — POSITION + SCOPE
  - Complement PFC-Function (WHAT → HOW combines in different states)
  - Source: Drill R2 (§3.18), R11-R12, R15-R16
  - PFC-Function = 24 functions static. File này = dynamic configurations.

§1 — TẠI SAO KHÔNG CHỈ ON/OFF
  - PFC hiện tại (PFC-Function §7) chỉ có "offline cases" (mode ④)
  - Thực tế: 6 distinct configurations, mỗi cái cho phép/tắt functions khác nhau
  - Not damage — FUNCTIONAL configurations với evolutionary purposes

§2 — 6 CONFIGURATION MODES
  ① Normal (baseline): tất cả 24 functions available, moderate intensity
  ② Focused (flow): dlPFC task-ON + self-OFF, ACC minimal
  ③ Creative (loose): dlPFC reduced, default mode + spreading activation
  ④ Threat (survival): dlPFC offline, amygdala dominant, subcortical takeover
     = PFC-Function §7 current "offline cases"
  ⑤ Dissociation (defense): PFC HYPERACTIVATION (opposite of ④)
     4 functions weaponized: inhibit MAX + meta-cognition excessive
     + active lock chronic + override chronic
  ⑥ Psychedelic/Reconsolidation: DMN disintegration, schema destabilization
     Config ⑥ × function ⑭ (Modify) = system reconsolidation mechanism

§3 — PFC CONTROL SPECTRUM
  Overcontrol ↔ Balanced ↔ Undercontrol
  - Overcontrol = ⑤ territory (dissociation, depersonalization)
  - Balanced = ①②③ range (normal operation)
  - Undercontrol = ⑥ territory (psychedelic ego dissolution)
  - NOT linear scale — qualitatively different states
  - 🟢 Lanius 2010 (dissociation = hyperactivation)
  - 🟢 Carhart-Harris & Friston 2019 (REBUS model)

§4 — 24 FUNCTIONS × 6 SUB-REGIONS MAPPING
  - dlPFC: 15/24 functions → HUB + BOTTLENECK
  - ACC: 8/24 → quality controller
  - vmPFC: 6/24 → emotional bridge
  - OFC: 5/24 → value assignment
  - mPFC: 5/24 → self + social
  - vlPFC: 3/24 → inhibition specialist
  - Many-to-many mapping (NOT 1:1)
  - Implications: dlPFC damage = most devastating, vlPFC = most focused

§5 — CONFIGURATION × FUNCTION SURVIVAL MATRIX
  - Table: 24 functions × 6 configs → which survive in which mode
  - Key patterns:
    Config ② (flow): task functions survive, self-monitoring reduces
    Config ④ (threat): only ①⑧⑱ survive (observe + lock + inhibit)
    Config ⑤ (dissociation): ④⑱⑲⑳ weaponized (meta + inhibit + override + lock)
    Config ⑥ (reconsolidation): ⑭ enhanced (modify chunks) → lasting change
  - dlPFC bottleneck: if dlPFC goes offline → 15 functions lost simultaneously

§6 — PARTICIPATION × CONFIGURATION: 2 ORTHOGONAL TAXONOMIES
  - Drive.md §2 has 6 PFC PARTICIPATION modes (how much PFC engages)
  - This file has 6 CONFIGURATION modes (which functions active)
  - These are ORTHOGONAL but CONSTRAINED (not all combinations possible)
  - Natural pairings: participation ① + config ①, participation ⑤ + config ②
  - Unnatural: participation ① (sleep) + config ⑤ (dissociation) = rare

§7 — STRATEGY A→B TRANSITION (Defense Strategy Switch)
  - Active defense (Strategy A): fight/flight → config ④ (PFC offline)
  - Passive defense (Strategy B): freeze/dissociate → config ⑤ (PFC hyper)
  - Transition A→B = f(escape possibility × compiled history × developmental window)
    NOT intensity threshold
  - Caregiver trauma = triple impossibility (can't fight + can't flee + can't resolve)
  - B→A reversion possible but never complete
  - Source: R16 (Drill §3.17)

§8 — SYSTEM RECONSOLIDATION (Config ⑥ × Function ⑭)
  - EMERGENT from individual reconsolidation
  - Individual: recall chunk → labile → modify → re-compile (Nader 2000)
  - System: destabilize TOPOLOGY → reorganize → new structure
  - Config ⑥ (psychedelic) provides unique access to ⑭ in enhanced mode
  - 4 conditions for positive outcome:
    ① Sufficient destabilization, ② Safe context,
    ③ New experience available, ④ Integration support
  - Mirror of trauma: same power (structural change), opposite direction
  - Source: R15 (Drill §3.16)
  - 🟢 Griffiths 2006, Carhart-Harris 2012, Nader 2000

§9 — HONEST ASSESSMENT
  - 🟢 Strong: flow deactivation (Limb & Braun), dissociation hyperactivation (Lanius),
    psychedelic DMN (Carhart-Harris), reconsolidation (Nader)
  - 🟡 Framework: 6 discrete modes (brain may have more continuous space),
    survival matrix (inference from lesion + imaging, not direct measurement),
    orthogonal taxonomies (confirmed by different brain mechanisms)
  - 🔴 Predictions: P-R2a through P-R2d (testable via combined fMRI + behavioral)

§10 — CROSS-REFERENCES
  - PFC-Function.md — 24 functions (WHAT) → file này (HOW combines)
  - PFC-Hardware.md — hardware affects which configs accessible
  - Drive.md §2 — 6 participation modes (orthogonal taxonomy)
  - Reward-Signal-Architecture.md — reward × config interaction
  - Cortisol-Baseline.md — cortisol triggers config ④
  - Neural-Architecture.md — physical sub-region map
  - Drill-Reward-Feeling-Main.md §3.18 — full drill source
```

### Nguồn để viết:
- Drill Main: §3.18 (R2 PFC mapping), §5b (PFC Control Spectrum), §3.16-§3.17 (R15-R16)
- Drill Cases: §4 (Loss of Self expansion)
- PFC-Function.md hiện tại (24 functions list)
- Neural-Architecture.md (sub-regions physical map)

### Quality checklist:
- [ ] 24 functions × 6 sub-regions mapping verified against Neural-Architecture.md
- [ ] 6 modes consistent với Drive.md §2 participation modes
- [ ] Survival matrix logically consistent (no function surviving in impossible config)
- [ ] Research citations verified (Lanius, Carhart-Harris, Limb & Braun, etc.)

---

## §3 — REFINE LỚN: PFC-Hardware.md

### Vị trí: Core-Deep-Dive/PFC/PFC-Hardware.md (547L → ~1,000L)

### Nội dung cần thêm (extend existing sections):

```
§3 COMT — THÊM:
  - §3.NEW: COMT × Reward Pattern
    Val/Val: many-shallow rewards, short duration, improviser reward style
    Met/Met: fewer-deeper rewards, long duration, specialist reward style
  - §3.NEW: COMT × Childhood Compilation (4 combos):
    Met/approach = DEEP FLOW (intense + direction)
    Met/avoidance = RIGID ANXIETY (intense + stuck)
    Val/approach = CREATIVE EXPLORER (light + broad)
    Val/avoidance = SCATTERED ANXIETY (light + stuck)

§4 DRD4 — THÊM:
  - §4.NEW: DRD4 × Reward Profile interaction
    7R: rare+intense reward bursts, need large delta
    4R: frequent+mild rewards, notice small delta
  - §4.NEW: COMT × DRD4 Interaction (4 compound types):
    Val/Val + 7R = "thrill seeker" (fast clear + high threshold)
    Met/Met + 7R = "obsessive expert" (slow clear + high threshold → deep lock)
    Val/Val + 4R = "social butterfly" (fast clear + low threshold → many light)
    Met/Met + 4R = "frustrated genius" (slow clear + low threshold → overwhelm risk)

§NEW — 4 Receptor Systems × 5 Reward Profiles mapping
  - Table: COMT / DRD4 / MAO-A / NE / μ-Opioid × 5 profiles
  - Type B = "democratic reward" — LESS affected by hardware variation
  - Implication: hardware counseling should focus on Type A patterns

§NEW — 3-Variable Shorthand
  - A/B Ratio × Dominant Profile × Breadth
  - Practical descriptor cho individual reward signature
  - Cannot MEASURE precisely yet — organizing framework

§9 Honest Assessment — UPDATE:
  - 🟡 COMT × Reward = extension from cognition, reward-specific data limited
  - 🔴 COMT × DRD4 interaction = framework synthesis, needs empirical testing
  - 🟡 "Democratic reward" (Type B less variable) = inference, not directly tested
```

### Nguồn: Drill Main §3.22 (R8), Cases §10.3

### KHÔNG thay đổi:
- §1-§2 (existing hardware overview) — giữ nguyên
- §5-§6 (MAO-A, NE) — giữ nguyên (drill không thêm gì mới)
- §7 VTA Detection Loop — giữ nguyên

---

## §4 — REFINE VỪA: PFC-Function.md

### Vị trí: Core-Deep-Dive/PFC/PFC-Function.md (446L → ~550L)

### Nội dung cần thêm:

```
Mỗi function (①-㉔) — THÊM tag [sub-region]:
  Ví dụ: "① OBSERVE FEELING [anterior insula → vmPFC → PFC]"
  Ví dụ: "⑨ TYPE 4 DELIBERATE LINKING [dlPFC primary]"
  → Không viết lại function description, chỉ thêm 1 dòng location

§7 PFC OFFLINE CASES — UPDATE:
  - Hiện: chỉ có mode ④ (threat offline)
  - Thêm note: "4 thêm modes khác ngoài offline → chi tiết: PFC-Configuration.md"
  - Cross-ref PFC-Configuration.md

§8 HARDWARE PROFILE — THÊM:
  - SUB-REGIONS: thêm "chi tiết mapping 24×6: PFC-Configuration.md §4"

§11 CROSS-REFERENCES — THÊM:
  - PFC-Configuration.md — 6 modes, survival matrix, control spectrum
```

### KHÔNG thay đổi:
- 24 functions descriptions — giữ nguyên (valid)
- 5 categories structure — giữ nguyên
- §6 Limitations — giữ nguyên

---

## §5 — REFINE VỪA: Body-Feedback-Mechanism.md

### Vị trí: Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Mechanism.md (960L → ~1,100L)

### Nội dung cần thêm:

```
§2 2 INPUT SOURCES — THÊM note:
  - Sensory-Driven ≈ Type B territory (direct state signals)
  - Pattern-Driven = can be Type A or Type B (depends on cortical involvement)
  - Cross-ref: Reward-Signal-Architecture.md §1

§4 COMPOUND MECHANISM — UPDATE:
  - Hiện: additive model
  - Thêm: Conditional Interaction Model (Drill R7)
    NOT additive — CONDITIONAL on 4 variables:
    substrate overlap × A gate direction × relief presence × temporal overlap
  - Cross-ref: Reward-Signal-Architecture.md §6

§10 CROSS-REFERENCES — THÊM:
  - Reward-Signal-Architecture.md — A/B × source mapping + conditional interaction
```

---

## §6 — REFINE VỪA: Feeling.md

### Vị trí: Core-Deep-Dive/Body-Base/Feeling/Feeling.md (1,404L → ~1,500L)

### Nội dung cần thêm:

```
§6 REWARD TRONG FEELING — UPDATE:
  - Hiện: "Dopamine ≠ Reward" basic
  - Thêm: 5 Reward Profiles summary (1 paragraph mỗi profile)
  - Thêm: Type A/B dimension — same feeling system observes BOTH types
  - Thêm: Quality = f(chunk library × compile context × current state × A/B ratio)
  - Cross-ref: Reward-Signal-Architecture.md (full detail)
  - Cross-ref: 03-Reward.md (H10 preconditions)

§11 CROSS-REFERENCES — THÊM:
  - Reward-Signal-Architecture.md
```

---

## §7 — REFINE NHẸ: 03-Reward.md

### Vị trí: Core-Deep-Dive/Body-Base/Body-Feedback/03-Reward.md (2,264L → ~2,300L)

### Nội dung cần thêm:

```
METADATA — FIX:
  - status: hiện nói "P3a complete, P3b to be appended" nhưng thực tế P3 COMPLETE
  - Update: "P3 COMPLETE — §1-§12 all drilled. See Reward-Signal-Architecture.md for A/B dimension."

§2.7 Step 5 BODY-BASE CHECK — THÊM note:
  - "Step 5 opioid check = primarily TYPE A pathway."
  - "Type B (direct state) bypasses cortical evaluation → different pathway."
  - "Chi tiết A/B dimension: Reward-Signal-Architecture.md §1-§3"

§3.6 Precondition 5 (P5 Chunk Tag) — THÊM note:
  - "P5 extends to reward QUALITY (not just direction)"
  - "4-Pathway × P5 Tag Model: Reward-Signal-Architecture.md §8.4"

§12 CROSS-REFERENCES — THÊM:
  - Reward-Signal-Architecture.md — WHAT KINDS (complement file)
  - PFC-Configuration.md — PFC modes × reward
```

---

## §8 — REFINE NHẸ: Compile-Taxonomy.md

### Vị trí: Core-Deep-Dive/Body-Base/Chunk/Compile-Taxonomy.md (823L → ~860L)

```
§3 (4 Compile Pathways) — THÊM cross-ref note:
  - "4 pathways tạo DIFFERENT P5 tags → khác reward capacity ở người lớn"
  - "HW Fit → approach tag → coherence natural"
  - "Trust Install → moderate tag → depends on collective chain"
  - "Social Default → neutral tag → relief dominant"
  - "Threat Avoidance → avoidance tag → relief ONLY, burnout trajectory"
  - "Chi tiết: Reward-Signal-Architecture.md §8.4"
```

---

## §9 — REFINE NHẸ: Dopamine-Reward-Rejection.md

### Vị trí: Core-Deep-Dive/Clarification/Dopamine-Reward-Rejection.md (497L → ~530L)

```
§2 3 Vị Trí — THÊM note tại Framework position:
  - "Framework REFINES: opioid = primarily TYPE A (evaluative) reward"
  - "Type B (direct state) uses non-opioid pathways (CT afferents, endocannabinoid)"
  - "Naltrexone blocks Type A but NOT Type B (Loseth 2019, Siebers 2021)"

§4 7-Step — THÊM note:
  - "7-step = primarily Type A pathway. Type B has shorter path."
  - Cross-ref: Reward-Signal-Architecture.md §1
```

---

## §10 — REFINE NHẸ: Feeling-Mechanism-Deep.md

### Vị trí: Core-Deep-Dive/Body-Base/Feeling/Feeling-Mechanism-Deep.md (1,291L → ~1,320L)

```
§4 REWARD MECHANISM — THÊM:
  - "Reward mechanism operates via 2 orthogonal types: A (evaluative) + B (direct state)"
  - "Feeling system observes BOTH but A = more accessible to PFC labeling"
  - Cross-ref: Reward-Signal-Architecture.md
```

---

## §11 — MINOR UPDATES (Tầng 3)

Sau khi Tầng 1-2 hoàn thành, update cross-refs cho:

| File | Cần thêm |
|------|----------|
| Core-v7.8-Draft.md | §body-feedback: thêm A/B dimension reference |
| Cortisol-Baseline.md | Cross-ref Profile ④ Relief = cortisol DROP |
| Novelty.md | Cross-ref VTA delta refined |
| Drive.md | §2 participation modes → link PFC-Configuration orthogonal |
| Threat.md | 2 defense strategies A→④, B→⑤ reference |
| Connection.md | Reward pathway alignment với A/B |
| Body-Coupling.md | A/B × Coupling cross-ref |
| Valence-Propagation.md | A/B × valence note |

---

## §12 — 01-File-Index.md UPDATE

Sau khi TẤT CẢ files hoàn thành:
- Thêm entry cho Reward-Signal-Architecture.md
- Thêm entry cho PFC-Configuration.md
- Update descriptions cho mọi file đã refine
- Update version numbers

---

## §13 — THỨ TỰ THỰC HIỆN

### Phase 1 — Foundations (2 files mới)
```
Session A: Reward-Signal-Architecture.md (TẠO MỚI)
  → Đây là gốc rễ, nhiều file khác reference đến
  → Cần đọc kỹ Drill Main trước khi viết
  → Ước tính: 1 session đầy đủ

Session B: PFC-Configuration.md (TẠO MỚI)
  → Độc lập với Reward-Signal-Architecture
  → Cần đọc kỹ Drill Main §3.18, §5b, §3.16-§3.17
  → Ước tính: 1 session đầy đủ
```

### Phase 2 — Major Refine (1 file)
```
Session C: PFC-Hardware.md (REFINE LỚN)
  → Phụ thuộc: PFC-Configuration.md đã có (cross-ref)
  → Ước tính: 0.5-1 session
```

### Phase 3 — Moderate Refines (4 files)
```
Session D: Body-Feedback-Mechanism.md + Feeling.md (REFINE VỪA)
  → Phụ thuộc: Reward-Signal-Architecture.md đã có (cross-ref)
  → 2 files cùng session vì mỗi cái chỉ thêm ~100-150L
  → Ước tính: 0.5-1 session

Session E: PFC-Function.md + Feeling-Mechanism-Deep.md (REFINE VỪA/NHẸ)
  → Phụ thuộc: PFC-Configuration.md đã có
  → Ước tính: 0.5 session
```

### Phase 4 — Light Refines (3 files)
```
Session F: 03-Reward.md + Compile-Taxonomy.md + Dopamine-Rej.md (REFINE NHẸ)
  → Chủ yếu metadata + cross-refs
  → Ước tính: 0.5 session
```

### Phase 5 — Minor Updates + Index
```
Session G: Tầng 3 (~8 files) + 01-File-Index.md
  → Cross-ref updates only
  → Ước tính: 0.5-1 session
```

### Tổng ước tính: ~5-7 sessions (mỗi session 1 task chính)

---

## §14 — COLD START INSTRUCTIONS

Khi bắt đầu session mới để triển khai plan này:

1. Đọc file plan này (plan-propagation.md)
2. Đọc memory file: project_drill_reward_feeling.md
3. Xác định đang ở Phase nào, Session nào
4. Đọc Drill Main sections relevant cho task hiện tại
5. Đọc file target (file cần tạo/refine)
6. Triển khai
7. Verify quality checklist
8. Update plan status (đánh dấu DONE)
9. Update memory file nếu cần

---

## §15 — STATUS LOG

| Phase | Session | Task | Status |
|-------|---------|------|--------|
| 1 | A | Reward-Signal-Architecture.md (TẠO MỚI) | ✅ DONE (2026-05-09, ~1,864L) |
| 1 | B | PFC-Configuration.md (TẠO MỚI) | ✅ DONE (2026-05-10, ~1,278L) |
| 2 | C | PFC-Hardware.md (REFINE LỚN) | ✅ DONE (2026-05-10, 690→1,004L) |
| 3 | D | BFM.md + Feeling.md (REFINE VỪA) | ✅ DONE (2026-05-10, BFM 1188→1249L, Feeling 1788→1862L) |
| 3 | E | PFC-Function.md + FMD.md (REFINE VỪA/NHẸ) | ✅ DONE (2026-05-10, PFC-F 545→567L, FMD 1593→1636L) |
| 4 | F | 03-Reward + Compile-Tax + Dopamine-Rej (NHẸ) | ✅ DONE (2026-05-10) |
| 5 | G | Tầng 3 + 01-File-Index (MINOR) | ✅ DONE (2026-05-10, 8 files + Index) |
