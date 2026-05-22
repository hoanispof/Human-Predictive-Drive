---
title: Agent-Mechanism — Integration Hub
version: 2.1
created: 2026-04-15
rewritten: 2026-05-17 (v2.0 — ALL REWRITE)
updated: 2026-05-22 (v2.1 — REFINE: +Phase A+B+T+C integration, SPM rename, 11 sub-files)
previous: v2.0 → backup/Agent-Mechanism-v2.0-backup.md
status: v2.1 INTEGRATION HUB
scope: |
  INTEGRATION HUB cho Agent Mechanism trong framework.
  v2.1 KEY CHANGES (Phase C8 REFINE — integrate Phase A+B+T+C1-C7):
    ① Simulation Engine context: SPM = Application 1 trên 1 Engine chung (SE v1.0)
    ② Entity-Compiled.md v1.0: Hub-and-Spoke, 40→200h, Dunbar, Grief A+B+C
    ③ Entity-Access.md v1.2: Mức 0-5 gradient (formal model cho §2)
    ④ SPM v3.1 rename: Match → Modeling (abbreviation SPM giữ nguyên)
    ⑤ BPGR v1.4: +Bond-Architecture, +Resonance-Sustainability, +By-Product-Scale, +RPE
    ⑥ VP v3.0: Structural/Current, 3 Firing Modes, Hardware Subsidy, 3 Satiation Types
    ⑦ PFC-Operations v1.0: Compiled Quality, PFC Budget, Pattern Shiftability
    ⑧ Folder expansion: 3 files → 11 files (reading flow updated)
    ⑨ All dependency versions updated to current
  PHÂN BIỆT: "Agent" (entity: bố, mẹ, bạn, Đức Mẹ) vs
  "Agent Mechanism" (function: detect + model + simulate + calibrate).
  File này mô tả FUNCTION, không phải entity.
  Integration hub: connect SPM v3.1 + BPGR v1.4 + EC v1.0 + EA v1.2 + body-need + schema + development.
purpose: |
  File NỀN TẢNG integration cho toàn bộ Agent-Mechanism/ folder:
  ① Định nghĩa Agent concept (reject binary, accept unified gradient Mức 0-5)
  ② Architecture B context: WHY agent mechanism exists
  ③ Simulation Engine context: SPM = Application 1 trên shared engine
  ④ 3-concept split (Self-Pattern / SPM / Resonance) + accurate previews
  ⑤ Preview SPM v3.1 + BPGR v1.4 + EC v1.0 + EA v1.2 ở high level
  ⑥ Gradient + schema override + collective + body-need feeder
  ⑦ Failure modes + developmental timeline + predictions
  Framework readers: START HERE → deep-dive sub-files.
previous_version: backup/Agent-Mechanism-v2.0-backup.md
parent: Core-Deep-Dive/Body-Base/Chunk/ (foundation file)
supporting_files:
  - Self-Pattern-Modeling.md v3.1 (solo forward mechanism — renamed from Match)
  - By-Product-Gap-Resonance.md v1.4 (emergent mutual phenomenon — trimmed)
  - Entity-Compiled.md v1.0 (entity compilation mechanism — NEW Phase A3)
  - Entity-Access.md v1.2 (entity-access gradient Mức 0-5 — NEW Phase A4)
  - Entity-Access-Excess.md v1.0 (Mức 5 excess — TÁCH Phase T1)
  - Entity-Access-Calibration.md v1.0 (calibration architecture — TÁCH Phase T2)
  - Bond-Architecture.md v1.0 (4 bond types × 1 EC — TÁCH Phase T3)
  - Resonance-Sustainability.md v1.0 (4-Layer model — TÁCH Phase T4)
  - By-Product-Scale.md v1.0 (3 scales — TÁCH Phase T5)
  - Resonance-Per-Entity.md v1.0 (per-entity profiles — MỚI Phase T7)
dependencies:
  core-mechanism:
    - Self-Pattern-Modeling.md v3.1 — Compiled/Fresh, PFC=Lawyer, 3-cost, APPLICATION 1
    - By-Product-Gap-Resonance.md v1.4 — 2-Stream, by-product match, anti-match
    - Inter-Body-Mechanism.md v1.0 — 8 drill principles source-of-truth
    - Body-Base.md v3.1 — 3 Hardware Foundations, Architecture B
    - Body-Feedback-Mechanism.md v2.0 — 2-source model, Body-Need aggregate
  pfc-engine:
    - PFC-Operations.md v1.0 — Hold/Suppress, Compiled Quality, PFC Budget, B vs C
    - Simulation-Engine.md v1.0 — 1 Engine × 3 Components × 3 Axes
    - PFC-Label.md v1.0 — vocabulary standard
  entity-mechanism:
    - Entity-Compiled.md v1.0 — Hub-and-Spoke, 40→200h, Dunbar, Grief A+B+C, Decay
    - Entity-Access.md v1.2 — Mức 0-5 gradient, 3-Factor, 4 Starting Modes
    - Entity-Access-Excess.md v1.0 — Mức 5, 3 origins, SPM atrophy
    - Entity-Access-Calibration.md v1.0 — 3-Layer, Exit Cost, Calibration Bias
  resonance-bond:
    - Bond-Architecture.md v1.0 — 4 bond types × 1 EC, M1-M4, gap clone IMPOSSIBLE
    - Resonance-Sustainability.md v1.0 — 4-Layer, 3 conditions, 3 modalities, 4 silence
    - By-Product-Scale.md v1.0 — 3 scales (pair/hub/institutional)
    - Resonance-Per-Entity.md v1.0 — HW Subsidy spectrum, Phantom 4-factor
  body-valence:
    - Valence-Propagation.md v3.0 — Structural/Current, 3 Firing Modes, HW Subsidy
    - Body-Coupling.md v3.0 — coupling mechanism, extension/entanglement/mixed
    - Gap-Direction.md v2.0 — gap direction = f(surrounding chunks)
    - Gap-Body-Need.md v1.0 — 3 Satiation Types, 5-Parameter, ENGINE/ROAD/VEHICLE
  processing-observation:
    - Feeling.md v3.0 — 7-layer fidelity, PFC observation interface, PFC=Lawyer
    - Logic-Feeling.md v2.0 — Compiled/Fresh = trục thật, observer labels
    - Neural-Processing-Flow.md v2.0 — hardware flow, Compiled/Fresh physical level
  connection-application:
    - Connection.md v5.0 — M1-M4, 4-Layer Sustainability, HW Subsidy, Phantom
    - Empathy.md v4.0 — PFC budget, Compiled Quality, Burnout reframe, Per-entity
    - Body-Feedback-Label.md v1.1 — vocabulary reference
    - Cortisol-Baseline.md v2.1 — stress cascade, moral injury
    - Reward-Signal-Architecture.md v2.0 — Type A/B, development trajectory
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Agent-Mechanism — Integration Hub

> ⚠️ **PHÂN BIỆT 2 KHÁI NIỆM "AGENT"**:
>
> **Agent (ENTITY)** = danh từ chỉ bất kỳ ai/gì mà brain fire SPM lên.
> Bố, mẹ, bạn bè, kẻ thù, con chó, Đức Mẹ (virtual agent), quốc gia (collective agent).
> = "NGƯỜI/SINH VẬT/ENTITY được brain model" — tồn tại ngoài brain.
>
> **Agent Mechanism (FUNCTION)** = hệ thống não bộ XỬ LÝ agents.
> Detect → Evaluate → Extend SPM → Read outcome → Compile/Dissolve.
> = "CHỨC NĂNG CỦA NÃO" — detect, model, simulate, calibrate agents.
> **File này mô tả FUNCTION, không phải entity.**
>
> ---
>
> **TẠI SAO agent mechanism tồn tại?**
>
> Architecture B: Evolution hardwire general-purpose reward + compilation + social hardware.
> → Adapt bất kỳ environment, nhưng cần 15-20 năm compile.
> → 15-20 năm đó = cần entity khác protect, feed, teach, calibrate.
> → Social = ARCHITECTURE REQUIREMENT, không phải luxury.
> → Agent mechanism = HOW body obtains social input that architecture DEMANDS.
>
> **Reading flow**:
> `Body-Base.md` (foundation) → `Agent-Mechanism.md` (file này, integration hub)
> → `Self-Pattern-Modeling.md v3.0` (solo mechanism) → `By-Product-Gap-Resonance.md v1.0` (mutual phenomenon)

---

## Mục lục

- §0 — Thesis + H9 (+v2.1: SE context, EA gradient, changes table)
- §1 — Position trong framework (+v2.1: 11 files, 6 entry paths)
- §2 — Reject binary Object-Agent (+v2.1: EA Mức 0-5 formal gradient)
- §3 — Architecture (+v2.1: §3.3 Simulation Engine context)
- §4 — 3-concept split (Self-Pattern / Self-Pattern-Modeling / Resonance)
- §5 — Self-Pattern-Modeling preview (v3.1 + §5.7 Compiled Quality)
- §6 — Resonance preview (BPGR v1.4 + §6.8-6.11 BA/RS/BS/RPE)
- §7 — Quality axes (4 axes + Compiled/Fresh + v2.1 quality modifiers)
- §8 — Pattern-Type modalities (5 types)
- §9 — Gradient validation (18 cases, 2-stream + EA Mức annotated)
- §10 — Schema override (Mode 1 / Mode 2)
- §11 — Schema-Linked Agent Processing (individual → collective)
- §12 — Agent as body-need feeder (+v2.1: §12.7 Satiation, §12.8 ENGINE/ROAD/VEHICLE, §12.9 Phantom)
- §13 — Developmental timeline (Architecture B → 15-20yr compilation)
- §14 — Failure modes (11 modes: +v2.1: §14.10 EA-Excess, §14.11 Compiled Suppress)
- §15 — Individual variation
- §16 — H9 falsifiable predictions (12 predictions)
- §17 — Framework status (Phase A+B+T+C — 28-session plan)
- §18 — Open questions
- §19 — Honest assessment (24🟢 + 26🟡 + 7🔴)
- §20 — Cross-references (30+ files, 45+ citations)

---

## §0 — Thesis + H9

### §0.1 — H9 Hypothesis (v2.0 unified)

> **Agent-reading = Self-Pattern-Modeling mechanism**: PFC retrieve self chunks matching
> target entity, apply làm template, fire 2 functions song song:
> F1 Compiled (body-level simulation, automatic, cost ≈ 0) +
> F2 Fresh (PFC chain prediction, deliberate, costly).
>
> **SPM = Application 1 trên Simulation Engine chung** (SE v1.0).
> 1 Engine (Interoception × Constructive Simulation × Self/Other Model) ×
> 3 Axes (Target × Time × Operation) → N applications.
> SPM = coordinate (Other, Present, Simulate). Self-Observation, Imagine-Final = same engine.
>
> **Compiled/Fresh = trục thật** — "Feeling" và "Logic" chỉ là observer labels.
> Einstein "cảm" toán vì toán đã COMPILED. Therapist mới "nghĩ" cảm xúc vì case còn FRESH.
> Expert intuition = compiled (non-shareable), không phải bừa.
>
> Per-Agent Valence gates F1/F2 direction (empathy vs strategic vs dehumanize).
> Context-dependent chunk selection (vô thức tùy chọn per agent + context).
> **PFC = Lawyer not Judge** — narrative justifies body's pre-made valence decision.
>
> **Resonance = emergent mutual phenomenon** khi 2+ entities' interactions
> produce sustained by-product match — mỗi bên fill gap CỦA MÌNH qua actions
> mà output (by-product) match gap direction CỦA BÊN KIA.
> **2-Stream Architecture**: Stream 1 (hardware/unidirectional, habituates) +
> Stream 2 (SPM compiled mutual, deepens). SPM = powerful ENHANCER, NOT prerequisite.
>
> **Agent KHÔNG phải separate substrate hay hardware category**.
> Agent là **function running on chunk substrate** — supports H1 (chunk = substrate).
> **Entity-Access = continuous gradient** (Mức 0-5), KHÔNG phải binary Object-Agent.

### §0.2 — Architecture B context (WHY this mechanism exists)

```
⭐ TẠI SAO brain cần Agent Mechanism?

  Architecture B = general-purpose reward + compilation + social hardware.
  → Adapt BẤT KỲ environment (ưu: flexible)
  → CẦN 15-20 năm compile (nhược: long childhood, dependent)
  → = CẦN entity khác protect, feed, teach, calibrate trong 15-20 năm đó

  4 lý do Social = Architecture Requirement:
  ① Survival math: 1 người không survive alone efficiently
  ② Information source: brain cần external feedback để calibrate compilation
  ③ Social hardware hardwired: oxytocin, μ-opioid, dACC reuse pain circuits
  ④ Baseline state: social = DEFAULT (Coan & Sbarra 2015)

  → Agent Mechanism = HOW body obtains social input mà architecture DEMANDS.
  → Không có Agent Mechanism, Architecture B FAIL (cannot compile without others).

  🟢 Coan & Sbarra 2015: Social Baseline Theory
  🟢 Eisenberger 2003: social-physical pain overlap (dACC)
  🟢 Panksepp 1998: μ-opioid in social play
```

### §0.3 — Key rejections và acceptances (v2.0 updated)

**REJECTED**:
- Binary hardware Object-Agent classification (VTC level) — too strong, contradicts gradient
- "F1 Feeling + F2 Logic" labels as mechanism description — observer labels, not mechanism
- Resonance requires SPM from both sides — v3.1: by-product match sufficient
- Agent as separate storage substrate — contradicts H1 unified chunk
- Hardware "mirror module" — already rejected (Theme E)
- PFC = neutral judge — PFC = Lawyer (Gazzaniga, Haidt 2001, Nisbett & Wilson 1977)

**ACCEPTED**:
- 🟢 Spelke core knowledge as innate **triggers** (not categories)
- 🟢 VTC hardware binary detection as early filter, overridden by schema + learned model
- 🟢 Bird & Cook 2013: poor self-reading → poor SPM → poor Resonance
- 🟢 Goldman simulation theory compatible với SPM
- 🟢 Architecture B: general-purpose → social requirement → agent mechanism necessary
- 🟢 Hub-and-Spoke neural architecture for person-model (Patterson 2007, 2017)
- 🟢 Formation 40→200h (Hall 2018), schema acceleration (Tse 2007)
- 🟢 Dunbar layers S1-S6 = Entity-Compiled depth gradient (Dunbar 1992-2024)
- 🟡 Simulation Engine: 1 Engine × 3 Components × 3 Axes → N applications (SE v1.0)
- 🟡 Entity-Access gradient Mức 0-5 (replaces binary Object-Agent — EA v1.2)
- 🟡 Entity-Compiled: Hub-and-Spoke + 40→200h + Grief A+B+C (EC v1.0)
- 🟡 Compiled Quality dimension: genuine/schema/threat (PFC-Ops v1.0)
- 🟡 PFC Budget ~4±1 concurrent (PFC-Ops v1.0)
- 🟡 Hardware Subsidy spectrum: MAX→NONE per entity type (RPE v1.0, VP v3.0)
- 🟡 M1-M4 Resonance Decline (BA v1.0)
- 🟡 4-Layer Sustainability model (RS v1.0)
- 🟡 Phantom 4-factor model (RPE v1.0)
- 🟡 2-Stream Architecture (Stream 1 habituates, Stream 2 deepens)
- 🟡 3-cost model (PFC draft + Suppress + Uncertainty)
- 🟡 PFC = Lawyer (Gazzaniga split-brain supports, Haidt confirms)
- 🟡 By-product match as Resonance mechanism (broader than SPM co-fire)
- 🟡 5-Channel Input Vector model
- 🟡 Domain Reality = Final Arbiter (drill ⑧)

### §0.4 — v2.0 changes từ v1.0

| Aspect | v1.0 DRAFT | v2.0 |
|---|---|---|
| SPM definition | F1 Feeling + F2 Logic | F1 Compiled + F2 Fresh (labels ≠ mechanism) |
| Resonance definition | SPM co-fire required | By-product match (SPM = enhancer, not required) |
| Resonance architecture | Single quality spectrum | 2-Stream (hardware/unidirectional + SPM mutual) |
| Cross-species Resonance | "Failed" case | Genuine Resonance (Stream 1 + Proto-Stream 2) |
| Architecture B | Absent | Central framing (WHY mechanism exists) |
| PFC role | Neutral processing | Lawyer (narrative bias, Gazzaniga) |
| Cost model | Not formalized | 3 independent sources |
| Verification | Not addressed | Domain Reality = Final Arbiter |
| Supporting files | SPM v2.0, Resonance old | SPM v3.0, By-Product-Gap-Resonance v1.0 |

### §0.5 — v2.1 changes từ v2.0

| Aspect | v2.0 | v2.1 |
|---|---|---|
| SPM terminology | Self-Pattern-Match v3.0 | Self-Pattern-**Modeling** v3.1 (rename) |
| Simulation Engine | Absent | SPM = Application 1 trên 1 Engine chung (SE v1.0) |
| Entity-Compiled | Brief mention §12.2b | Full mechanism reference (EC v1.0: Hub-and-Spoke, Dunbar, Grief) |
| Entity-Access | §2 reject binary (conceptual) | Mức 0-5 formal gradient (EA v1.2) |
| Resonance sub-files | 1 file (BPGR v1.0) | 5 files (BPGR v1.4 + BA + RS + BS + RPE) |
| PFC-Operations | 3-cost only | +Compiled Quality, +PFC Budget, +Pattern Shiftability |
| Body-need model | 2-luồng only | +3 Satiation Types, +ENGINE/ROAD/VEHICLE, +Phantom |
| Folder | 3 active files | 11 active files |
| Dependencies | 16 flat list | 30+ organized 6 categories |
| Connection ref | v4.0 | v5.0 (M1-M4, 4-Layer, Phantom integrated) |
| Empathy ref | v2.2 | v4.0 (PFC budget, Compiled Quality, Per-entity) |
| VP ref | v2.0 | v3.0 (Structural/Current, 3 Firing Modes, HW Subsidy) |

---

## §1 — Position trong framework

### §1.1 — File này là ai

`Agent-Mechanism.md` là **integration hub** cho khái niệm Agent trong framework. Không phải deep-drill của mechanism đơn lẻ, mà là file **định nghĩa + tổ chức + forward-pointer + context**.

**Vai trò**:
1. Định nghĩa Agent concept (reject binary, accept unified gradient Mức 0-5)
2. Architecture B context: WHY agent mechanism exists
3. Simulation Engine context: SPM = Application 1 trên shared engine
4. 3-concept split + accurate previews (SPM v3.1, BPGR v1.4, EC v1.0, EA v1.2)
5. Gradient validation + schema override + collective + body-need feeder
6. Developmental timeline + failure modes + predictions
7. Entry point cho readers → 11 sub-files

**Không phải**:
- Không phải deep SPM mechanism (→ `Self-Pattern-Modeling.md v3.1`)
- Không phải mutual phenomenon deep-dive (→ `By-Product-Gap-Resonance.md v1.4`)
- Không phải entity compilation deep-dive (→ `Entity-Compiled.md v1.0`)
- Không phải entity-access gradient deep-dive (→ `Entity-Access.md v1.2`)
- Không phải bond/sustainability/scale/per-entity deep-dive (→ respective sub-files)
- Không phải inter-body mechanism (→ `Inter-Body-Mechanism.md v1.0`)

### §1.2 — Reading flow (v2.1 — 11 sub-files)

**Standalone entry** (hiểu Agent concept):
`Agent-Mechanism.md` (file này) → pick deep-dive as needed

**Core mechanism deep-dive** (SPM + Resonance):
`Self-Pattern-Modeling.md v3.1` (solo) → `By-Product-Gap-Resonance.md v1.4` (mutual)

**Entity deep-dive** (compilation + access):
`Entity-Compiled.md v1.0` (HOW entities compile) → `Entity-Access.md v1.2` (gradient Mức 0-5)
→ `Entity-Access-Excess.md v1.0` (Mức 5) + `Entity-Access-Calibration.md v1.0` (calibration)

**Bond + Sustainability deep-dive**:
`Bond-Architecture.md v1.0` (4 types, M1-M4) → `Resonance-Sustainability.md v1.0` (4-Layer)
→ `By-Product-Scale.md v1.0` (3 scales) → `Resonance-Per-Entity.md v1.0` (profiles + Phantom)

**Architecture context** (WHY mechanism exists):
`Inter-Body-Mechanism.md v1.0` §1 → `Agent-Mechanism.md` §0.2

**Engine context** (shared substrate):
`Simulation-Engine.md v1.0` → SPM = Application 1 trên 1 Engine chung

**Body-need feeder**:
`Agent-Mechanism.md` §12 → `Connection.md v5.0` → `Body-Coupling.md v3.0`

### §1.3 — Files superseded

| File cũ | Claim cũ | Reason replaced |
|---|---|---|
| `Domain/backup/Object-Agent.md` | Binary hardware VTC | Contradicted by gradient; unified model |
| `Body-Base/Feeling/backup/Self-Pattern-Modeling.md` | Inward self-labeling | Conflicts với forward simulation |
| `Body-Base/Feeling/backup/By-Product-Gap-Resonance.md` | Solo simulator | Conflates solo với mutual phenomenon |
| `Domain/Agent-2Axis-Analysis.md` (draft) | 3-layer + 4 quadrants | Integrated here |

### §1.4 — Scope

**IN scope**: Agent concept, 3-concept split, Simulation Engine context, previews (SPM v3.1 + BPGR v1.4 + EC v1.0 + EA v1.2), Architecture B, gradient Mức 0-5, schema override, Schema-Linked Processing, body-need feeder (3 Satiation Types, ENGINE/ROAD/VEHICLE), developmental timeline, failure modes (incl. EA-Excess, Compiled Suppress), individual variation, H9 predictions.

**OUT of scope**: Full Collective-Agent deep drill, consciousness/qualia, religious tradition comparative, neural correlate precise mapping, AI era implications beyond mention. Deep mechanisms → respective sub-files.

---

## §2 — Reject Binary Hardware Object-Agent

### §2.1 — Old claim (Object-Agent.md)

`Domain/backup/Object-Agent.md` committed strongly:

> "Não classify MỌI THỨ vào 1 trong 2 loại — hardware-level, binary, instant."

**Evidence old file cited**:
- 🟢 Spelke Core Knowledge (2007): innate Object + Agent representation
- 🟢 VTC neuroimaging (eLife 2019): dedicated regions animate vs inanimate
- 🟢 Infant animate motion detection (9 months)
- 🟢 Preferential face processing từ sơ sinh

### §2.2 — Tại sao binary claim too strong

**Problem 1 — Gradient data contradicts binary**:
- Hợp tính → easy prediction
- Khác tính → harder prediction
- Chó cúp đuôi → sympathy fires but prediction weak
- Chuột → no simulation, fallback mechanical
- Cục đá → pure physics
- Đức Mẹ mẫu ảnh → schema override Mode 1

Data show **continuous gradient** từ high-quality simulation (family) đến no-simulation (stone) đến schema-override (religious). Binary cannot accommodate.

**Problem 2 — Same target changes over time**:
Same mẹ — same VTC classification — nhưng SPM dynamic radically different:
- Day 0: active learning, composite SPM
- Year 1: compiled routine, efficient
- Year 10: suppressed by negative overlay, routine script only

**Problem 3 — Classification IS schema-mediated**:
Bộ đội lạ → schema "Đảng/Bác Hồ" → positive valence, trust.
Quân giặc lạ → schema "enemy" → hostility.
Prediction template từ SCHEMA, không phải hardware classification.

**Problem 4 — Đức Mẹ Mode 1**:
- VTC hardware: inanimate (image, no motion)
- User experience: protective agent, full trust
- Mechanism: schema override bypasses hardware entirely
- Mode 1: ZERO modeling — pure schema trust

Binary fails: hardware says object, user treats as agent, with ZERO simulation.

### §2.3 — Refined position — VTC as TRIGGER, not CATEGORY

> VTC hardware provides **innate detection triggers** (biological motion, face patterns,
> self-propelled movement, contingent response). These triggers **invoke** SPM function —
> nhưng không **define** entity identity.
>
> What entity IS = chunk substrate + schema linking + learned SPM model.
> VTC = **upstream trigger**, not downstream identity.

**Implications**:
1. **Spelke Core Knowledge stays** — reframed: triggers + expectations, not categories
2. **VTC regions stay explained** — efficient early filter for attention allocation
3. **Animate/inanimate attention difference holds** — SPM can fire usefully on biologically relevant entities, but final quality depends on learned model
4. **Hardware necessary but not sufficient** — VTC filters early, final = SPM on chunks + schema overlays

### §2.4 — Unified reframe + Entity-Access Gradient Mức 0-5

> **Object** = chunk (foundation). Every entity represented as chunks.
> **Agent** = **SPM function invoked on chunk**. Not separate category.
> "Agent-ness" = FUNCTION OUTPUT, not STORAGE PROPERTY.
>
> **Spectrum** from: (a) SPM quality (multi-axis), (b) schema overlay, (c) VTC trigger.
> **No binary category**. VTC = upstream. Downstream = continuous + context-dependent.

**v2.1**: Entity-Access.md v1.2 formalizes gradient thành **Mức 0-5**:

```
⭐ ENTITY-ACCESS GRADIENT (EA v1.2 — formal model cho §2 rejection):

  Mức 0 — NO ACCESS: machine, service, tool-mode (SPM ≈ 0)
  Mức 1 — SHALLOW AGENT: recognized but unlabeled (barista, hàng xóm)
  Mức 2 — PARTIAL COMPILE: some F1, mostly F2 (đồng nghiệp, bạn mới)
  Mức 3 — DEEP COMPILE: F1 dominant, B-dominant reward (bạn thân)
  Mức 4 — ENTITY-OWNED: deep + hardware subsidy + low exit cost (mẹ→con, vợ/chồng)
  Mức 5 — EXCESS: C-dominant, autonomy violated, SPM atrophy (→ EA-Excess.md)

  3-FACTOR MODEL cho mỗi Mức:
    F1 — Engine Mode: Tool ↔ Agent spectrum (HOW brain processes)
    F2 — Gap-Need Profile: A+B+C+D sources (WHY need access)
    F3 — Access Confidence: EC depth + stability + hardware subsidy (CAN access?)

  KEY INSIGHTS:
  → Mức 0-2 = UNLABELED by PFC (most entity-access exists without label)
  → Entity-Owned = PFC LABEL at high compilation, NOT mechanism itself
  → B-dominant = optimal destination for ALL starting modes
  → Hardware Subsidy DURABLE but ≠ quality (mẹ max subsidy, có thể low quality)

  Detail: Entity-Access.md v1.2 (full gradient model)
         Entity-Access-Excess.md v1.0 (Mức 5 deep-dive)
         Entity-Access-Calibration.md v1.0 (calibration architecture)
```

### §2.5 — What's preserved from old file

| Old claim | Status | Where preserved |
|---|---|---|
| Spelke core knowledge | 🟢 Preserved | §2.3 (as triggers) |
| VTC hardware detection | 🟢 Preserved | §2.3 (as early filter) |
| Infant animate motion | 🟢 Preserved | §13 developmental |
| Piaget animism | 🟢 Preserved | §13 + §14 (uncalibrated SPM) |
| Meat Paradox (Loughnan 2014) | 🟢 Preserved | §14 failure modes |
| Grossman On Killing | 🟢 Preserved | §14 dehumanization |
| Uncanny Valley (Mori 1970) | 🟢 Preserved | §14 VTC-SPM conflict |
| Context-dependent | 🟢 Preserved | §11 Schema-Linked |

### §2.6 — Architecture B context

Architecture B = general-purpose reward. Cần FLEXIBLE agent detection:

```
Architecture A (specific-reward):
  → Fixed circuits: "face-like = agent, else = object"
  → Works for STABLE environment. Cannot adapt novel entity types.

Architecture B (general-purpose):
  → General trigger + learned model overlay
  → VTC provides QUICK trigger (innate)
  → Schema + chunks provide FLEXIBLE determination (learned)
  → Can model NEW entity types (AI, virtual agents, collective)

→ Binary = Architecture A thinking applied to Architecture B brain.
→ §2 rejection = ARCHITECTURAL CONSEQUENCE of general-purpose design.
```

---

## §3 — Architecture (chunk substrate + function overlay)

### §3.1 — Core architecture

```
🟡 CHUNK-BASED MODEL cho mọi entity trong domain:

  FOUNDATION — OBJECT CHUNKS (mọi entity có):
    → Physical + semantic properties: shape, size, location, modality imprint
    → Chunk substrate: Hebbian wiring từ repeated experience
    → = "What I perceive + define about entity"
    → Mechanism: compiled via repetition + emotional peak + multi-modal + sleep

  FUNCTION — LOGIC PROCESSING (rules-based prediction):
    → Uses object chunks + compiled rules → predict behavior
    → Works when: entity behavior deterministic theo known rules
    → Sufficient for: most objects, routine interactions, compiled relationships
    → v2.0: = COMPILED chunks firing in rule-pattern mode

  FUNCTION — MODELING OVERLAY (SPM — optional, adds khi needed):
    → Self-Pattern-Modeling function invoked
    → "if I were in target's position, what would I feel/think/want?"
    → Varies: minimal (insect) → shallow (stranger) → deep (mẹ, bạn thân)
    → v2.0: = F1 Compiled (automatic body-sim) + F2 Fresh (deliberate PFC-draft)

  OVERRIDE — SCHEMA (can bypass or reshape):
    → Community/cultural/personal schemas override natural processing
    → Mode 1: pure schema trust (zero modeling) — Đức Mẹ luôn bảo vệ
    → Mode 2: imagined modeling overlay — mystical dialogue prayer
    → Can ADD "agent-ness" to objects (religious icons, sacred stones)
    → Can REMOVE "agent-ness" from people (dehumanization)
```

### §3.2 — Compiled/Fresh dimension (v2.0 addition)

v1.0 described architecture without addressing HOW processing quality varies. v2.0 adds:

```
⭐ COMPILED/FRESH = TRỤC THẬT cho agent processing:

  COMPILED processing (F1):
    → Chunks đã LTP-strengthened + myelinated (100m/s)
    → Fires AUTOMATIC, cost ≈ 0
    → Body-level simulation: FEEL target's state
    → Expert intuition with agent (therapist "biết" client buồn)
    → "Superhighway" — instant, effortless

  FRESH processing (F2):
    → Novel unmyelinated paths (1m/s)
    → PFC DRAFT prediction: deliberate, costly
    → Chain reasoning about target's behavior
    → Novice analysis (student "phân tích" patient symptoms)
    → "Dirt road" — slow, effortful

  SPECTRUM — không binary:
    → Same person, different domains = different compiled/fresh ratio
    → Với mẹ ở domain tình cảm = highly compiled
    → Với mẹ ở domain đầu tư chứng khoán = mostly fresh
    → Per-domain, per-agent, per-moment

  "Logic" vs "Feeling" = OBSERVER LABELS:
    → Observer gọi F1 (compiled) là "feeling/intuition" vì automatic
    → Observer gọi F2 (fresh) là "logic/analysis" vì deliberate
    → Nhưng F1 có thể là toán (Einstein), F2 có thể là cảm xúc (therapist mới)
    → Label theo CONTENT sai. Trục thật theo COMPILATION LEVEL.
```

Cross-reference: Logic-Feeling.md v2.0 §1 (full treatment), Neural-Processing-Flow.md v2.0 §5.5 (physical level).

### §3.3 — Simulation Engine context (v2.1 addition)

v2.0 described SPM as standalone mechanism. v2.1 adds: SPM = **Application 1** trên **1 Engine chung** (Simulation-Engine.md v1.0).

```
⭐ SIMULATION ENGINE — 1 Engine, 3 Components, N Applications:

  3 COMPONENTS (shared substrate):
    C1 — Interoception (anterior insula): reads body signals → "MÀN HÌNH"
    C2 — Constructive Simulation (DMN + hippocampus): recombine chunks → "CPU+RAM"
    C3 — Self/Other Model (mPFC gradient): ventral=self+close, dorsal=far → "CONTROL PANEL"

  3 AXES (application coordinates):
    Target: Self ↔ Close Other ↔ Far Other (continuous gradient)
    Time: Past ↔ Present ↔ Future (+ Counterfactual)
    Operation: Observe ↔ Simulate ↔ Evaluate ↔ Construct

  KEY APPLICATIONS (= coordinates in 3D space):
    ① SPM         = (Other, Present, Simulate) ← file này focus
    ② Self-Obs    = (Self, Present, Observe)
    ③ Imagine-Final = (Self, Future, Simulate+Construct)
    ④-⑫: memory recall, counterfactual, moral judgment, narrative, dream...

  WHY THIS MATTERS FOR AGENT MECHANISM:
  → SPM KHÔNG phải separate module — shared substrate với Self-Observation + Imagine-Final
  → 🟢 Alexithymia PROOF: C1 broken → ALL applications degrade (Bird & Cook 2013)
  → Training C1 (interoception) → improves SPM + Self-Obs + Imagine-Final simultaneously
  → Entity-Access = neural migration: stranger → dorsal mPFC → close other → ventral mPFC
  → mPFC gradient (C3) = neural substrate cho Entity-Access gradient Mức 0-5 (EA v1.2)

  Detail: Simulation-Engine.md v1.0
```

### §3.4 — Parallelism across entities

Logic + Modeling chạy SONG SONG cho MỌI entity, chỉ khác **tỉ lệ compiled/fresh**:

```
Compiled processing dominant (SPM near-zero):
  → Cục đá, tường, bàn — schema + rules đủ
  → Schema agents Mode 1 (Đức Mẹ) — schema trust
  → Đồng nghiệp routine — compiled interaction script

Mixed compiled + fresh:
  → Bạn thân mới quen — some compiled, much fresh
  → Chó quen — compiled routine + fresh state-tracking

Fresh processing dominant:
  → Người mới phức tạp — PFC draft prediction active
  → Conflict resolution — re-modeling required
  → Con mới sinh — everything fresh, compiling rapidly
```

Mix ratio = **dynamic** (varies target, context, task, self's modality bias).

### §3.5 — Why entities need SPM (4 reasons + Architecture B)

```
⭐ 4 lý do entity CẦN modeling overlay (từ Agent-2Axis + Architecture B):

REASON A — Unpredictable behavior:
  Behavior không theo rules simple → cần build SPM model.
  VD: mẹ thật (hôm nay vui/buồn/mệt varied).

REASON B — High-stakes interaction:
  Entity impact body-base significantly → worth modeling kể cả predictable.
  VD: sếp (routine nhưng impact career).

REASON C — Social architecture requirement:
  Body CẦN social presence (Architecture B ③).
  SPM firing = way để body obtain social input signal.
  VD: bạn thân — even routine, modeling satisfies body-need.
  Cross-ref: Inter-Body-Mechanism.md §1.3 (4 reasons social = requirement).

REASON D — Imagined presence:
  Entity không có real state → người imagine (schema provides substrate).
  VD: Đức Mẹ Mode 2, người đã mất, fictional character.
  Cost: no real feedback → no calibration → potential distortion.

NO MODELING NEEDED:
  → Physics-deterministic (cục đá, bàn)
  → Schema-defined absolute (Đức Mẹ Mode 1)
  → Routine-complete (đồng nghiệp chào hỏi xong đi)
  → Below-threshold (chuột — mechanical prediction Layer 1+2 đủ)
```

### §3.6 — 4 Quadrants (Utility × Modeling Requirement)

```
┌──────────────────────────────────────────────────────────────┐
│  HIGH UTILITY × LOW MODELING  │  HIGH UTILITY × HIGH MODELING │
│                                │                                │
│  Schema agents:                │  Real relationships:           │
│  • Đức Mẹ Mode 1              │  • Mẹ, bố ruột                 │
│  • Tools (tủ lạnh)            │  • Bạn thân, vợ/chồng          │
│  = COMPILED, EFFICIENT         │  = ACTIVE SPM, HIGH VALUE      │
├────────────────────────────────┼────────────────────────────────┤
│  LOW UTILITY × LOW MODELING    │  LOW UTILITY × HIGH MODELING   │
│                                │                                │
│  Background:                   │  Obsessive fixation:            │
│  • Cục đá, tường              │  • Crush không đáp lại          │
│  • Người lạ thoáng qua        │  • Celebrity parasocial         │
│  = BACKGROUND NOISE             │  = HIGH COST, LOW PAYOFF       │
└────────────────────────────────┴────────────────────────────────┘
```

**Dynamic movement**: New → Top-right (learning) → compiled → Top-left (efficient) → crisis → Top-right again. Mother-10-year: Top-right → routine → Bottom-right (suppressed).

### §3.7 — PFC = Lawyer in agent processing

```
⭐ PFC=LAWYER CAVEAT cho toàn bộ agent mechanism:

  PFC KHÔNG neutral judge khi evaluate agents.
  PFC = Lawyer: tạo NARRATIVE cho body's pre-made valence decision.

  Mechanism:
  ① Body evaluate agent qua compiled valence (fast, automatic)
  ② Body ĐÃ "quyết định" valence TRƯỚC PFC biết
  ③ PFC observe decision → construct narrative WHY
  ④ Narrative feels like "rational judgment" — nhưng là POST-HOC justification

  Consequences for agent processing:
  → "Tôi ghét người đó vì..." — reasons PFC constructs, not causes body uses
  → "Tôi tin người đó vì..." — narrative justifies pre-made trust valence
  → Parasocial: PFC constructs elaborate justification for attachment
  → Dehumanization: PFC constructs "they deserve it" narrative

  FIX = Domain Reality (drill ⑧):
  → Neither compiled valence nor PFC narrative is final authority
  → Domain OUTCOME (reality) = arbiter
  → "Ghét" may be wrong if domain shows person helpful
  → "Tin" may be wrong if domain shows person harmful
  → Only real-world OUTCOMES calibrate agent valence accurately

  🟢 Gazzaniga split-brain: left hemisphere confabulates reasons
  🟢 Haidt 2001: moral judgments are post-hoc rationalizations
  🟢 Nisbett & Wilson 1977: people cannot accurately report causal influence
```

---

## §4 — 3-concept split (Self-Pattern / Self-Pattern-Modeling / Resonance)

**Key architectural decision**. Distinction sharpens framework + resolves Theme E ambiguity.

### §4.1 — The 3 concepts table

| Concept | Định nghĩa | Status | Direction | Role |
|---|---|---|---|---|
| **Self-Pattern** | Chunks của self đang activate tại thời điểm đó | State (direct) | N/A | Raw material |
| **Self-Pattern-Modeling** | Cơ chế self apply chunks → analyze target (solo forward) | Mechanism (direct) | Forward (prediction) | HOW I try to model |
| **Resonance** | Sự giao thoa thực khi interactions produce mutual by-product match | Phenomenon (retrospective) | Backward (inferred) | WHAT was true |

### §4.2 — Self-Pattern (state)

**Self-Pattern** = tập hợp chunks đang fire trong self tại thời điểm đang xét.

- **Dynamic**: thay đổi liên tục theo activation
- **Rich**: emotional + cognitive + sensory + memory + predictive + schema
- **Directly accessible**: PFC observation interface reads as "feeling"/"thinking"
- **Raw material**: pool mà SPM draws from

### §4.3 — Self-Pattern-Modeling (mechanism — v3.1 definition)

**Self-Pattern-Modeling** = cơ chế self select chunks → apply làm template → analyze/predict agent's state/behavior. Fire 2 functions song song. **Application 1** trên Simulation Engine chung (SE v1.0 — coordinate: Other × Present × Simulate).

- **F1 Compiled**: body-level simulation (automatic, cost ≈ 0, Hebbian reinforced)
- **F2 Fresh**: PFC draft prediction (deliberate, costly, mỗi lần = effort)

**Key properties**:
- **Solo**: one-way, runs inside self alone
- **Forward**: produces prediction before verification
- **Compiled/Fresh spectrum**: same mechanism, different compilation level
- **PFC = Lawyer**: narrative about WHY self predicts X = post-hoc (not the cause)
- **3-cost when Fresh**: ①PFC draft metabolic + ②Suppress compiled if conflicts + ③Uncertainty cortisol holding
- **Per-domain**: same person, different domain → different compiled/fresh ratio
- **Context-dependent**: vô thức tùy chọn chunks per agent + context
- **Per-Agent Valence gates direction**: empathy (positive) vs strategic (neutral) vs reversed (negative)

### §4.4 — Resonance (phenomenon — BPGR v1.4 definition)

**Resonance** = emergent mutual phenomenon khi 2+ entities' interactions produce sustained by-product match — mỗi bên fill gap CỦA MÌNH → output match gap direction CỦA BÊN KIA.

**KEY**: SPM = NOT prerequisite. SPM = powerful ENHANCER (creates Stream 2).
**v2.1**: BPGR v1.4 trimmed → deep-dives tách thành Bond-Architecture v1.0, Resonance-Sustainability v1.0, By-Product-Scale v1.0, Resonance-Per-Entity v1.0. See §6 previews.

**2-Stream Architecture**:
- **Stream 1** — Hardware/Unidirectional: mỗi bên receive reward INDEPENDENTLY từ other's existence/thuộc tính. Không cần engagement ngược. HABITUATES (Weber-Fechner).
- **Stream 2** — SPM compiled mutual (bidirectional): CẦN cả 2 engage SPM toward nhau → feedback loop → 2 não ĐỒNG BỘ. ANTI-HABITUATION (Hebbian → stronger → deepest connection).

**Key properties**:
- **Mutual**: requires 2+ entities (but NOT requires SPM from both — Stream 1 suffices)
- **Retrospective access only**: self CANNOT know Resonance real-time, infer từ outcome
- **Feedback source**: observations → calibration data cho SPM library
- **Per-pair, per-domain, per-moment**: hình dạng Resonance riêng cho mỗi cặp
- **Anti-match possible**: by-products can CONFLICT gap direction (worse than no-match)

### §4.5 — Relationship diagram

```
TIME →

    [Self-Pattern state at t₀]
          │
          │ Self-Pattern-Modeling (forward solo)
          │ = F1 Compiled + F2 Fresh (parallel)
          ↓
    [Prediction about target]
          │
          │ Communication / action
          ↓
    [Outcome observation]
          │
          │ Retrospective inference
          ↓
    [Resonance inferred (present/absent/partial)]
          │
          │ Feedback loop (Stream 2)
          ↓
    [SPM library refinement]
          │
          │ Better prediction next time
          ↓
    [Self-Pattern state at t₁ (updated)]

Note: Stream 1 Resonance fires PARALLEL — independent of this SPM loop.
```

### §4.6 — Why 3 separate concepts (not 1)

5 lý do:

**Reason 1 — Different epistemic status**:
- SPM = direct access (self knows what it's running)
- Resonance = indirect access (inferred from evidence)

**Reason 2 — Different temporal direction**:
- SPM = forward prediction (not yet verified)
- Resonance = backward ground truth (after verification)

**Reason 3 — Framework-wide relevance differs**:
- SPM rộng (beyond agent-reading: planning, imagination, problem-solving)
- Resonance specific to interpersonal interaction

**Reason 4 — Calibration loop requires distinction**:
- Learning: prediction → outcome → inference → library refinement
- Bird & Cook 2013: poor self-reading → poor SPM → poor Resonance → "empathy deficit"

**Reason 5 — 2-Stream Architecture**:
- Resonance has Stream 1 (no SPM involved at all — hardware by-product match)
- Resonance has Stream 2 (SPM mutual — bidirectional synchronization)
- Gộp SPM + Resonance = miss that Resonance exists WITHOUT SPM (Stream 1)

---

## §5 — Self-Pattern-Modeling high-level preview (v3.1)

> **Detail**: `Self-Pattern-Modeling.md v3.1`. Section này = accurate preview + forward pointer.
> v3.1: renamed Match → Modeling. APPLICATION 1 trên Simulation Engine chung.

### §5.1 — One-sentence definition (v3.1)

**Self-Pattern-Modeling** = solo forward simulation mechanism: select chunks từ self repertoire matching target → fire F1 Compiled (body simulate target state, automatic) + F2 Fresh (PFC chain predict target behavior, deliberate) song song. Per-Agent Valence gates direction. Context-dependent per agent/domain. PFC = Lawyer (narrative bias). 3-cost when Fresh. = Application 1 (Other × Present × Simulate) trên Simulation Engine chung.

### §5.2 — Compiled/Fresh as real axis

```
⭐ v3.1 KEY REFRAME: F1/F2 = Compiled/Fresh spectrum

  F1 = COMPILED SPM:
    → Body-level simulation: target's state → own body FEEL echo
    → Automatic, cost ≈ 0, Hebbian reinforced qua repetition
    → Fires vô thức: "biết" bạn thân buồn mà chưa hỏi
    → PHYSICAL: LTP-strengthened synapses + myelinated axons (100m/s)
    → Expert intuition: therapist "sense" client state = compiled SPM

  F2 = FRESH SPM:
    → PFC draft prediction: deliberate chain reasoning about target
    → Costly: mỗi lần = metabolic effort (glucose consumption)
    → Fires có ý thức: "tôi nghĩ person X sẽ làm Y vì Z"
    → PHYSICAL: novel neural paths, unmyelinated (1m/s)
    → Novice analysis: student "phân tích" patient = fresh SPM

  SPECTRUM — không binary:
    → Với mẹ domain cảm xúc: F1 dominant (compiled rich)
    → Với mẹ domain tài chính: F2 dominant (chưa compile domain này)
    → Therapist session 1: F2 (fresh). Session 1000: F1 (compiled same pattern)

  "Feeling" = observer label cho F1 (compiled) — vì automatic
  "Logic" = observer label cho F2 (fresh) — vì deliberate
  LABELS KHÔNG phải mechanism.
```

### §5.3 — 3-cost model (when Fresh)

```
3 INDEPENDENT COST SOURCES khi F2 SPM fires:

  ① PFC DRAFT COST (metabolic):
    → Glucose-consuming reasoning about target
    → Gailliot 2007: PFC energy depletion real
    → "Mệt sau buổi nói chuyện phức tạp với người mới"

  ② SUPPRESS COST (efference mismatch):
    → Khi F2 prediction conflicts với F1 compiled response
    → Must SUPPRESS compiled to follow fresh draft
    → Like hitting brake while engine pulls → friction
    → "Biết nên tha thứ nhưng body vẫn ghét" = suppress cost

  ③ UNCERTAINTY COST (cortisol holding):
    → Chưa biết prediction có đúng không
    → Cortisol holds elevated as "uncertainty tax"
    → Kéo dài → baseline drift (Cortisol-Baseline.md)
    → "Chờ phản hồi từ person X" = uncertainty cost accumulating

  3 costs INDEPENDENT:
    → Có thể ① cao + ②③ thấp (reasoning mà không conflict + sure)
    → Có thể ② cao + ①③ thấp (suppress strong compiled, đơn giản)
    → Có thể ③ cao + ①② thấp (simple wait nhưng unclear outcome)
```

Cross-reference: Inter-Body-Mechanism.md §4 (full treatment).

### §5.4 — PFC = Lawyer caveat

SPM output goes through PFC observation → PFC constructs NARRATIVE about WHY self predicted X. This narrative is **post-hoc justification**, not the actual mechanism.

**Practical consequence**: "Tôi nghĩ person X đang buồn vì..." — the "vì" is PFC's STORY. Actual prediction came from compiled chunks firing (F1) or PFC draft (F2). The explanation you give = Lawyer's brief.

**Domain = Arbiter**: Neither compiled feeling nor PFC narrative is final. Only domain outcome (real interaction result) CONFIRMS or REFUTES.

### §5.5 — Framework-wide applications

SPM là mechanism **rộng**, không chỉ agent-reading:
- **Empathy**: fire F1 on other → feel echo of their state
- **Perspective-taking**: deliberate F2 SPM với target role
- **Gift-giving**: fire "preference" patterns, project, predict reaction
- **Planning**: fire "future self" patterns, simulate outcomes
- **Imagination**: fire scenario chunks, simulate hypotheticals
- **Moral reasoning**: fire "victim" patterns, simulate harm
- **Teaching**: fire "learner's confusion", simulate where stuck

Tất cả = **self-chunks fired as template + projection** — same mechanism, different domains.

### §5.6 — Bird & Cook 2013 upstream dependency

```
Poor self-reading (alexithymia)
  ↓
Poor chunk labels for own states
  ↓
Poor retrieval for SPM template (no good material)
  ↓
Poor SPM output (both F1 and F2)
  ↓
Poor Resonance emergence (predictions don't match)
  ↓
"Empathy deficit" (outcome label)
```

→ **Self-awareness prerequisite for other-awareness**. Architectural, not just developmental.

🟢 Bird & Cook 2013: alexithymia (not autism per se) drives empathy deficit.

### §5.7 — Compiled Quality effect on SPM (v2.1 addition)

SPM output quality depends not only on compilation LEVEL (F1/F2) but on compilation QUALITY (PFC-Operations.md v1.0 §5):

```
⭐ COMPILED QUALITY × SPM CAPACITY:

  GENUINE-COMPILED (approach tag, opioid):
    → SPM about target = EXPANSIVE (rich multi-sensory model)
    → CAN predict new situations (generalize)
    → Self-reinforcing: more use → more compile → better

  SCHEMA-COMPILED (flat tag, relief):
    → SPM about target = LIMITED (narrow, single-channel)
    → CANNOT expand beyond schema template
    → Needs genuine experience to bridge

  THREAT-COMPILED (avoidance tag, cortisol):
    → SPM about target = BIASED NEGATIVE (defensive filter)
    → Miss positive signals, amplify threat signals
    → Burnout risk when sustained

  SAME PERSON, SAME COMPILATION LEVEL — DIFFERENT QUALITY:
    → Student A chọn học toán = genuine → SPM rộng
    → Student B bị ép học toán = threat → SPM hẹp, biased
    → "Giỏi nhưng ghét" = threat-compiled (know HOW, avoid DOING)

  Detail: PFC-Operations.md v1.0 §5 (full treatment)
```

---

## §6 — Resonance high-level preview (BPGR v1.4 + 4 sub-files)

> **Detail**: `By-Product-Gap-Resonance.md v1.4` (core, trimmed).
> + `Bond-Architecture.md v1.0` (4 bond types, M1-M4 decline)
> + `Resonance-Sustainability.md v1.0` (4-Layer sustainability)
> + `By-Product-Scale.md v1.0` (3 scales: pair/hub/institutional)
> + `Resonance-Per-Entity.md v1.0` (per-entity profiles, HW Subsidy, Phantom)

### §6.1 — Definition (BPGR v1.4)

**Resonance** = emergent mutual phenomenon khi 2+ entities' interactions produce sustained by-product match — mỗi bên fill gap CỦA MÌNH qua actions mà output (by-product) match gap direction CỦA BÊN KIA.

**v3.1 KEY**: SPM = NOT prerequisite. SPM = powerful ENHANCER (creates Stream 2 deepest quality). But Resonance EXISTS without SPM (mẹ-bé sơ sinh, người-chó, twins gặp lần đầu).

### §6.2 — 2-Stream Architecture

```
⭐ TOTAL RESONANCE = Stream 1 + Stream 2 (parallel, independent, cộng dồn)

  STREAM 1 — Hardware/Unidirectional by-product match:
    → Mỗi bên receive reward INDEPENDENTLY từ other's existence/thuộc tính
    → KHÔNG cần engagement ngược (vợ xinh → chồng vui, chồng ko cần làm gì)
    → KHÔNG synchronize 2 não (cảm riêng)
    → HABITUATES over time (Weber-Fechner, hedonic treadmill)
    → Multi-channel: beauty + status + presence + smell + voice...
    → Phụ thuộc HARDWARE + COMPILED CHUNKS (not pure hardware)
    → Supports Stream 2: khởi động (proximity) + đệm an toàn (buffer khi conflict)

  STREAM 2 — SPM compiled mutual (bidirectional synchronization):
    → CẦN cả 2 engage SPM toward nhau → feedback loop
    → 2 não ĐỒNG BỘ: A detect B's state → respond → B FEEL → respond → loop
    → Có thể CHANGE other's state (kéo lên/xuống thật sự)
    → ANTI-HABITUATION: Hebbian → more use → stronger → positive spiral
    → UNSUSTAINABLE nếu chỉ 1 bên (→ obligation-trapped)
    → = Deepest human connection mechanism

  TEMPORAL:
    → Stream 1 peaks EARLY → habituates (novelty wears off)
    → Stream 2 starts ZERO → grows → deepest (compilation builds)
    → Sustainability: Stream 2 growth phải > Stream 1 decline

  PROTO-STREAM 2 (non-SPM mutual engagement):
    → Mẹ-bé: contingent response (mẹ respond to bé's cues)
    → Người-chó: associative conditioning (mutual reward patterns)
    → Not full SPM, but bidirectional reward loop exists
```

### §6.3 — Conditions (v3.1 — BROADENED)

**4 conditions cần cho Resonance emergence:**

1. **Both capable of receiving by-product reward from other** — NOT "both running SPM" (broadened: mẹ-bé, người-chó qualify)
2. **Channel available** — feedback channel exists (touch, presence, voice, facial, behavioral)
3. **By-product match** — output of B's gap-filling matches A's gap direction (per-domain, per-moment)
4. **Sufficient exposure** — not just time, but repeated interaction enabling pattern recognition

**Stream 2 ADDITIONAL conditions**: both engage SPM + mutual loop established.

### §6.4 — Anti-match concept (v3.1 new)

By-products có thể CONFLICT gap direction (not just neutral no-match):
- CEO innovation drive ↔ partner comfort-seeking = NEGATIVE by-product match
- Worse than no-resonance = active friction, cost TĂNG thay vì giảm

### §6.5 — Per-pair topology

Resonance = per-PAIR, per-DOMAIN, per-MOMENT:
- Hậu vệ ↔ tiền đạo = 1 shape
- Hậu vệ ↔ khán giả = different shape
- Same pair, different domain = different Resonance quality

### §6.6 — Cases reclassified (v3.1)

| Case | v1.0 classification | v3.1 classification |
|---|---|---|
| Mẹ-bé sơ sinh | "Failed" (no SPM from baby) | **Genuine Resonance**: Stream 1 CỰC MẠNH + Proto-Stream 2 |
| Người-chó | "Failed" (cross-species) | **Genuine Resonance**: Stream 1 strong + Proto-Stream 2 |
| Người-robot | Not addressed | Stream 1 habituates fast + Stream 2 IMPOSSIBLE → hollow |
| Bạn thân compiled | High quality | Stream 1 + Stream 2 (deepest, anti-habituate) |
| Parasocial | Failed | Stream 1 one-sided + Stream 2 impossible (no feedback) |

### §6.7 — Retrospective detection

Self CANNOT know Resonance real-time. Infer post-hoc from:
- Conversation deepened → Resonance likely present
- Conversation stalled → Resonance absent
- Subsequent behavior matches prediction → confirmed
- Subsequent behavior contradicts → Resonance was illusion

**PFC = Lawyer warning**: PFC may construct narrative "we connected!" even when Resonance absent. Domain outcome (not feeling) = arbiter.

### §6.8 — Bond Architecture preview (BA v1.0 — v2.1 addition)

**4 bond types × 1 Entity-Compiled mechanism** (tất cả dùng SAME EC architecture):

| Bond Type | Hardware Subsidy | Formation | Exit Cost | Example |
|---|---|---|---|---|
| Parent→Child | MAX (oxytocin, prenatal) | Pre-installed | Very high | Mẹ→con |
| Romantic | TEMPORARY (limerence 6-24m) | Hormone-assisted | Moderate→high | Vợ/chồng |
| Friendship | NONE | By-product only | Low | Bạn thân |
| Kin (non-parent) | Moderate (50% DNA) | Context-assisted | Moderate | Anh/chị/em |

**M1-M4 Resonance Decline**: 4 mechanisms giảm Resonance quality over time:
- M1 — Habituation: Weber-Fechner, đặc biệt Stream 1 → "quen → không thấy"
- M2 — Compilation reduces novelty: F1 dominant → auto-pilot → "biết hết rồi"
- M3 — Gap shift: entity-related gaps atrophy → "không cần nữa"
- M4 — Anti-match accumulation: by-product conflicts tích lũy → friction

**Gap clone IMPOSSIBLE**: brain CANNOT duplicate gap direction from one entity to another (5-step proof in BA v1.0 §5). Mất 1 entity = gap THẬT SỰ mất, không chuyển được.

Detail: `Bond-Architecture.md v1.0`

### §6.9 — Resonance Sustainability preview (RS v1.0 — v2.1 addition)

**4-Layer Sustainability model** — conditions duy trì Resonance chống M1-M4:

| Layer | Function | Mechanism | Without |
|---|---|---|---|
| L1 — Proximity | Physical availability | Co-location, schedule | S1 habituates, S2 atrophies |
| L2 — Duration | Time for deep exchange | Sustained interaction | Shallow only |
| L3 — Agent-Mode | SPM quality engagement | Genuine curiosity, not routine | Auto-pilot → M2 |
| L4 — Domain Coverage | Multi-domain by-product | Cover gaps across domains | Single-domain fragile |

**3 conditions**: proximity + duration + agent-mode = necessary (all 3 required).
**3 modalities**: verbal (word exchange) + non-verbal (facial, tone) + body (touch, proximity).
**4 silence types**: comfortable (compiled trust) vs awkward (mismatch) vs charged (suppress) vs dead (no resonance).

Detail: `Resonance-Sustainability.md v1.0`

### §6.10 — By-Product Scale preview (BS v1.0 — v2.1 addition)

**1 mechanism × 3 scales** (by-product match operates at ALL levels):

| Scale | Unit | Mechanism | Example |
|---|---|---|---|
| L1 — Pair | 2 individuals | Direct by-product match | Bạn thân, vợ/chồng |
| L2 — Hub | 1 node + N members | Node's by-products serve group | Team leader, teacher |
| L3 — Institutional | Distributed system | Trust infrastructure (serotonin) | Company, nation |

**Prestige = genuine resonance** (by-product match at scale). Dominance = forced resonance (schema override, not genuine). Hardware shift: L1 oxytocin → L2 oxytocin+serotonin → L3 serotonin dominant.

Detail: `By-Product-Scale.md v1.0`

### §6.11 — Per-Entity Resonance profiles preview (RPE v1.0 — v2.1 addition)

**3-Tầng model**: Tầng 1 (Hardware Substrate: sensory, hormone, coherence) → Tầng 2 (Compilation History: 40→200h, entity-compiled) → Tầng 3 (Current Dynamics: M1-M4, sustainability, phantom).

**Hardware Subsidy spectrum** (per entity type):
- MAX: parent→infant (oxytocin anti-habituation, prenatal restructure)
- HIGH: kin (50% DNA, childhood co-fire)
- TEMPORARY: romantic (limerence 6-24 months, then fades)
- NONE: friend (pure by-product, fragile but highest quality)

**Phantom 4-factor model** (after entity loss):
- Factor 1: Entity-Compiled depth (chunk networks still fire)
- Factor 2: Gap-fill breadth (how many domains entity filled)
- Factor 3: Hardware Subsidy (kin phantom more durable than friend)
- Factor 4: Replacement availability (alternative gap-fill sources)
- Phantom = chunks fire → target absent → Chunk-Miss → pain. Duration = f(4 factors).

Detail: `Resonance-Per-Entity.md v1.0`

---

## §7 — Quality axes (4 axes + Compiled/Fresh dimension)

4 quality dimensions cho SPM output. Axes interact — quality = function of all combined.

### §7.1 — Axis 1: Pattern-Type (modality fired)

Which modality of chunks fires trong SPM retrieval + simulation.

**5 types** (detailed §8):
- Affective (emotion chunks)
- Somatic (body state/posture chunks)
- Visual-symbolic (spatial/diagrammatic/mathematical chunks)
- Verbal-cognitive (inner speech/dialogue/planning chunks)
- Composite (multi-modal blend — native mode for rich relationships)

**Determinants**: (a) target cues, (b) self modality bias (Logic-Feeling.md v2.0 §6), (c) task context.

### §7.2 — Axis 2: Depth (chunk richness about target)

- **Thin**: stranger, unfamiliar species (~5-10 relevant chunks)
- **Moderate**: colleague, fan community member (~50-100 chunks)
- **Deep**: family, close friend, partner (hundreds to thousands)
- **Deepest**: multi-year observation + feedback calibration (fully compiled model)

**Critical**: Depth KHÔNG require personal chunks. Mathematicians share deep DOMAIN chunks while having shallow personal chunks → high SPM quality in math domain.

### §7.3 — Axis 3: Similarity (self-target template match)

- **Self-similar**: same age/culture/background/personality/species → template fits directly
- **Moderate divergent**: different personality but same species/culture → needs adjustment
- **Distant**: different species (dog, cat) → affective-only mapping
- **Below threshold**: no mappable structure (insect, inanimate) → SPM fails → fallback

### §7.4 — Axis 4: Feedback availability

- **Real-time rich**: face-to-face, full expression channels → calibration during interaction
- **Real-time limited**: phone, video → reduced channels
- **Delayed**: text, email → delayed, reduced richness
- **One-way**: reading book, watching celebrity → no feedback from target
- **None**: imagined (prayer, deceased, fictional) → no external feedback

**Feedback = calibration mechanism**. Without it, SPM runs open loop → errors compound → templates distort. Parasocial = high SPM without feedback → progressive distortion.

### §7.5 — Compiled/Fresh as 5th dimension (v2.0 addition, v2.1 enriched)

v1.0 described 4 axes. v2.0 adds compilation level. v2.1 adds: **Compiled Quality** (genuine/schema/threat) and **Hardware Subsidy** also affect quality independent of 4 axes.

```
Same target, same 4 axes — nhưng:
  → Day 1: F2 Fresh dominant (effortful, costly, uncertain)
  → Year 5: F1 Compiled dominant (automatic, efficient, confident)

Compilation level affects:
  → Speed: compiled = instant. Fresh = seconds to minutes.
  → Cost: compiled ≈ 0. Fresh = 3-cost model (①②③).
  → Accuracy: compiled = high IF domain stable. Fresh = variable.
  → Sustainability: compiled = maintain indefinitely. Fresh = depletes.
```

**v2.1 additional quality modifiers** (interact with all 5 dimensions):

| Modifier | Effect on SPM quality | Source |
|---|---|---|
| Compiled Quality (genuine/schema/threat) | Genuine = expansive, Threat = biased negative | PFC-Ops v1.0 §5 |
| Hardware Subsidy (MAX→NONE) | High subsidy = faster compile but ≠ quality | RPE v1.0, VP v3.0 |
| Entity-Access level (Mức 0-5) | Higher = deeper F1, lower = F2 dominant | EA v1.2 |
| PFC Budget state | Depleted → all axes drop | PFC-Ops v1.0 §9 |

### §7.6 — Axes interaction

**High all** → best-case: rich partner + compiled + real-time feedback.

**Trade-offs**:
- High depth + low similarity (dog trainer) → mechanical prediction, SPM partial
- High similarity + low depth (stranger like self) → template fits, prediction coarse
- High feedback + low depth (first meeting) → rapid accumulation mid-conversation
- Low feedback + high depth (media) → parasocial distortion

**Threshold failure**: all low → SPM fails → mechanical fallback (mouse case).

---

## §8 — Pattern-Type modalities (5 types)

### §8.1 — Affective (emotion chunks)

**Fires when**: target distress signals, emotional expression, emotionally-charged situation.

**Examples**:
- Dog cúp đuôi ẳng ẳng → "sadness/distress" → "dog đang buồn"
- Mẹ khóc → "sadness/pain" → "mẹ đang khổ"
- Candy gift: self "ngon + happy" → projected onto mother

**Quality limits**: Projection error (self's response ≠ target's). Cross-species fires but = projection. Cultural variation.

**Compiled/Fresh**: Affective SPM about close others = COMPILED (instant). About strangers = FRESH (effortful).

### §8.2 — Somatic (body state / posture chunks)

**Fires when**: target posture visible, movement quality, physical context.

**Examples**:
- Mèo nằm im cúi đầu → "lethargy/stress" → "mèo stress"
- Athlete preparing → watcher body co-fires → predict timing
- Mother slumping → "exhaustion" → "mẹ mệt"
- Craftsman → expert co-fires muscular patterns → "flow"

**Key**: Strong in embodied learning (dance, sports, crafts, surgery).

Cross-ref: Somatic-Articulation-Loop.md.

### §8.3 — Visual-symbolic (spatial / mathematical chunks)

**Fires when**: target in spatial/mathematical task, shared symbolic problem.

**Examples**:
- Mathematicians discussing → same symbolic chunks → "understand"
- Chess players → same tactical possibilities
- Architects reviewing blueprint → shared spatial model
- Physicists: Einstein's "riding light" visual-kinetic

**Key**: Deep understanding WITH SHALLOW PERSONAL chunks. Domain depth matters.

### §8.4 — Verbal-cognitive (inner speech / dialogue chunks)

**Fires when**: verbal communication, shared verbal problem, explicit reasoning.

**Examples**:
- Study group stuck → "I know where you're stuck"
- Negotiation → fire "opponent position" → predict counter
- Teaching → fire "learner confusion" → simulate misconception
- Legal → fire rule + exception → simulate judge

**Key**: Slower + deliberate. Enables explicit perspective-taking. Classic ToM domain.

### §8.5 — Composite (multi-modal blend)

**Fires when**: long-term relationship, complex situation, high-stakes, intense empathy.

**Examples**:
- Mother's mood: affective + somatic + verbal + contextual blend
- Partner in crisis: distress + trembling + words + history + facial
- Close friend's subtle disappointment: micro-expression + tone + silence + shift

**Key**: Composite = **native mode** for close others. Single-modality = artificial isolation.

### §8.6 — Selection dynamics + 5-Channel connection

```
Target cues + Self modality bias + Task context
       ↓
Primary Pattern-Type fires first
       ↓
Extension to related types (composite within seconds)
       ↓
Prediction output

Speed: Affective (ms) > Somatic (s) > Visual-symbolic (s) > Verbal-cognitive (s-min)
```

**5-Channel connection**: Target input reaches self via Visual, Auditory, Tactile, Olfactory/Gustatory, Schema/Memory channels. Which channels active → biases Pattern-Type. Cross-ref: Inter-Body-Mechanism.md §6.

---

## §9 — Gradient validation (H9 evidence)

18 cases validate 4-axis + Compiled/Fresh + 2-Stream model.

### §9.1 — Master table (v2.1 — 2-stream + EA Mức annotated)

| # | Target | Pattern-Type | Depth | Similarity | Feedback | Quality | 2-Stream | EA Mức |
|---|---|---|---|---|---|---|---|---|
| 1 | Person hợp tính | Composite | High | Self-similar | Rich | 🟢 | S1+S2 strong | 3 |
| 2 | Person khác tính | Verbal + affective | Moderate | Divergent | Rich | 🟡 | S1 mod, S2 effortful | 2-3 |
| 3 | Chó cúp đuôi | Affective only | Thin | Low | Limited | 🟡 | **S1 + Proto-S2** | 1-2 |
| 4 | Mèo stress | Somatic + affective | Thin | Low | Limited | 🟡 Weak | S1 only | 1 |
| 5 | Chuột | None | Very thin | Below threshold | None | 🔴 | No Resonance | 0 |
| 6 | Cục đá | N/A | N/A | N/A | N/A | N/A | N/A | 0 |
| 7 | Đức Mẹ Mode 1 | None | N/A | N/A | None | Schema | S1 (comfort) | 0 (schema) |
| 8 | Đức Mẹ Mode 2 | Composite imagined | Schema | Schema | Internal | 🟡 Virtual | S1+imagined | 0 (schema) |
| 9 | Bộ đội lạ | Affective + cognitive | Schema | Moderate | Minimal | 🟡 | S1 (warmth) | 1 (schema) |
| 10 | Quân giặc | Suppressed | Schema | Hostile | Minimal | 🔴 | Anti-match | 0 (suppress) |
| 11 | Mother day 0 | Composite fresh | Growing | Moderate | Rich | 🟡 Fresh | S1 strong+S2 begin | 2→3 |
| 12 | Mother year 1 | Composite compiled | Deep | High | Rich | 🟢 | S1+S2 compiled | 4 |
| 13 | Mother yr 10 suppress | Verbal routine | Blocked | Blocked | Ignored | 🔴 | S1 habituated | 4→5? |
| 14 | Mathematicians | Visual-symbolic | Deep domain | Moderate | Rich | 🟢 Domain | S2 (domain) | 2-3 (domain) |
| 15 | Music fans | Affective | Moderate | High affective | Shared | 🟢 Affective | S1+weak S2 | 1-2 |
| 16 | Study group | Verbal-cognitive | Shared problem | Same skill | Rich | 🟢 Domain | S2 (cognitive) | 2 |
| 17 | Celebrity parasocial | Composite | Deep media | Medium | **Zero** | 🔴 Distorted | S1 one-sided | 0 (illusion) |
| 18 | Mẹ-bé sơ sinh | Affective+somatic | Growing | Low (age) | Contingent | 🟢 Proto | **S1 CỰC MẠNH** | 4 (hw) |

**v2.1 note**: EA Mức column maps Entity-Access gradient (EA v1.2) onto existing cases. Cases 11-13 show mẹ→con lifecycle: Mức 2→4 (growing) → 4→5? (suppress/excess trajectory). Case 17 parasocial = Mức 0 actual but illusion of high.

### §9.2 — Key case analyses

**Case 3 — Dog (reclassified v3.1)**:
- v1.0: "Failed Resonance" (cross-species)
- v3.1: **Genuine Resonance** — Stream 1 (cute → dopamine, hardware) + Proto-Stream 2 (associative mutual conditioning)
- SPM = affective-only (no cognitive simulation of dog's mind)
- "Failed" label was wrong — Resonance doesn't require SPM

**Case 5 — Chuột (threshold confirms)**:
- All axes fail → SPM cannot fire → mechanical fallback
- Chunks + rules (dọc tường, avoid light) predict behavior WITHOUT SPM
- **Proves**: SPM optional. Chunk-based prediction works for deterministic targets.

**Cases 11-13 — Mother over time**:
- Day 0: F2 Fresh (learning, costly). S1 strong (baby schema). S2 = 0.
- Year 1: F1 Compiled (efficient). S1 moderate (habituating). S2 growing.
- Year 10: Schema blocks both. S1 habituated. S2 blocked. Routine only.
- Same target traverses Compiled/Fresh + 2-Stream over TIME.

**Case 17 — Parasocial (PFC=Lawyer)**:
- Rich SPM + zero feedback → progressive distortion
- PFC narrative: "we understand each other" = Lawyer justifying attachment
- Domain reality (celebrity unaware) = ARBITER contradicting PFC
- **Lesson**: PFC=Lawyer + no feedback = distortion machine

**Case 18 — Mẹ-bé (STRONGEST Resonance)**:
- Baby can't run SPM → v1.0 confused (how can Resonance exist?)
- v3.1: Stream 1 = evolution-protected STRONGEST by-product match (baby schema triggers maternal hardware INDEPENDENT of SPM)
- Proto-Stream 2: contingent response loop (mẹ → bé → mẹ)
- SPM emerges Stage 2 (14-24m) → full Stream 2 follows
- **Proves**: Resonance definition MUST accommodate pre-SPM bonds

### §9.3 — Gradient lessons (v2.0)

12 validated insights:
1. SPM = function on chunk substrate ✅
2. Quality gradients smoothly across axes ✅
3. Threshold failure (chuột) → mechanical fallback ✅
4. Schema override can replace/provide (Mode 1/2) ✅
5. Domain depth ≠ personal depth ✅
6. Feedback essential for calibration ✅
7. Compiled/Fresh visible in mother-over-time ✅
8. 2-Stream explains "failed" cases (genuine Resonance) ✅
9. PFC=Lawyer visible in parasocial ✅
10. Domain=Arbiter visible in reality-vs-prediction ✅
11. Anti-match (CEO-comfort by-products conflict) ✅
12. Per-pair topology (same person, different pair shape) ✅

### §9.4 — Falsifiers

H9 falsified if:
- SPM fires fully with alexithymia (Bird & Cook wrong)
- Agent-reading in dedicated hardware (not chunk substrate)
- Parasocial NOT distorted (feedback axis irrelevant)
- Cross-species full cognitive simulation (similarity axis wrong)
- Mouse prediction requires SPM (Layer 1+2 insufficient)
- Stream 1 doesn't habituate (Weber-Fechner wrong socially)
- Mẹ-bé requires SPM from baby (2-Stream wrong)

None observed. H9 consistent.

---

## §10 — Schema override (Mode 1 / Mode 2)

Schema override = Layer 4 mechanism có thể bypass hoặc reshape SPM entirely. Explains how abstract/imagined/schema-defined agents elicit agent-like responses without real SPM firing.

### §10.1 — Mode 1: Pure schema trust (zero modeling)

Schema rule defines entity's behavior as **constant + absolute** → eliminates need for SPM.

```
Entity encounter → Schema fires: "Entity X → always Y"
  → Prediction := schema (no simulation)
  → Body response (comfort, trust, obedience)
  → Zero cognitive load, zero uncertainty
```

**Examples**:

**Đức Mẹ Mode 1** (daily devotion, rote prayer):
- Schema: "luôn yêu thương, luôn bảo vệ"
- No question "hôm nay Đức Mẹ giận không?" — schema eliminates uncertainty
- Icon = anchor for schema trigger, not target of simulation
- SPM NOT invoked. Cost: zero. Body response: comfort (real cortisol decrease, oxytocin)

**Lucky charm / amulet**:
- Schema: "this object protects me"
- Touch → schema fires → anxiety reduction. Body response real.

**Simple tools (tủ lạnh, xe máy)**:
- Schema: "tool provides utility reliably" → zero uncertainty, stable utility

**Why Mode 1 "works"**:
- Real agents carry uncertainty → possible disappointment
- Schema agents carry ZERO uncertainty → never disappoint
- Body-need for stable trust satisfied WITHOUT real-agent cost
- Architecture B: brain satisfies social-presence needs via schema when real agents unavailable/unreliable

**PFC = Lawyer note**: PFC narrative about WHY self trusts schema = post-hoc. Body trusts FIRST (compiled from childhood), PFC explains after.

### §10.2 — Mode 2: Imagined modeling overlay

Schema provides **substrate** for SPM to run on → virtual agent.

```
Entity + schema active → SPM fires toward schema entity
  → Schema fills in target's "state" content (virtual)
  → "Đức Mẹ đang NHÌN tôi, đang BUỒN vì tôi phạm lỗi"
  → Body responds to simulated other-state
  → Intense emotional experience
```

**Examples**:

**Đức Mẹ Mode 2** (intense prayer, dialogue):
- Tín đồ imagines Đức Mẹ's gaze, expression, emotional response
- SPM fires full composite on virtual agent
- Schema provides template for what Đức Mẹ would feel/think
- Intensity can match real social interaction

**Talking to deceased loved one**:
- SPM fires using memories + compiled chunks of deceased
- Virtual agent "responds" from schema-stored personality
- Continued social presence despite real absence

**Fictional character engagement**:
- Author's writing provides schema substrate
- SPM fires as if character were real
- Explains deep emotional engagement with fiction

**Mental dialogue with internalized figure**:
- "What would grandmother advise?" / "What would Socrates say?"
- Internalized figure as schema, SPM fires on virtual agent
- Useful for decision-making, problem-solving

**Mode 2 cost/benefit**:
- Benefit: deeper engagement, agent-input need strongly fulfilled
- Cost: high cognitive load, no real feedback → potential distortion
- **Domain=Arbiter**: Mode 2 outputs are NOT verified by reality (no external agent) → cannot self-correct

### §10.3 — Mode 1/Mode 2 dynamic switching

Religious practitioner moves fluidly:
- Routine prayer → Mode 1 (efficient, maintenance)
- Crisis moment → Mode 2 (intense dialogue)
- Contemplation → Mode 2 (imaginative reflection)
- Ritual → Mode 1 (schema comfort, no deep simulation)
- Confession → Mode 2 (simulated disappointment, guilt)

### §10.4 — Cow/stone worship

Physical object (cow, stone, icon) = **anchor/vessel** for abstract divine schema, NOT itself the target.

- **Hindu cow**: divine vessel → worship through cow to divine principle. Mode 1.
- **Shiva lingam / Kaaba stone**: divine presence at/in stone. Touch → schema → comfort. Mode 1.
- **Shinto kami**: spirits inhabit objects. Physical = vessel, kami = agent.
- **Primitive animism (adult retention)**: mix Mode 1 + uncalibrated SPM projection.

Pattern: physical anchor + abstract divine schema = Mode 1 or Mode 2. Agent-ness is SCHEMA-DEFINED, not stored in physical object.

**Exception — Piaget animism (2-7y)**: children genuinely attribute intent (ghế bị đau). = uncalibrated SPM projection, NOT schema override. Calibration over time refines boundary.

### §10.5 — Bác Hồ / Đảng schema link

```
Schema chain: Individual soldier → Bộ đội category → Đảng → Bác Hồ
  → Valence from schema: yêu quý, trust
  → Prediction: "fights for what I believe"
  → Action: share food even in hardship (body-need feeding via schema)
  → SPM minimal (schema handles) + some affective empathy for hardship

= Mode 1 schema-linked processing: schema fires, behavior follows,
  no individual SPM required. Same mechanism as religious Mode 1.

CONTRAST — quân giặc:
  → Same mechanism, opposite valence
  → Enemy schema → hostility, SPM SUPPRESSED (dehumanization)
  → No simulation of individual state — schema predicts all
```

→ **Schema polarity determines SPM invocation or suppression**.

### §10.6 — Summary table

| Case | Schema | Mode | SPM status |
|---|---|---|---|
| Đức Mẹ daily | "Luôn bảo vệ" | Mode 1 | Not invoked |
| Đức Mẹ intense prayer | "Đang nhìn tôi" | Mode 2 | Full virtual |
| Cow veneration | "Divine vessel" | Mode 1 | Not invoked |
| Sacred stone | "Divine presence" | Mode 1 | Not invoked |
| Ancestor worship | "Ancestor presence" | Mode 2 | Virtual agent |
| Bác Hồ schema | "Revered leader" | Mode 1 (link) | Not invoked for stranger bộ đội |
| Quân giặc | "Enemy" | Mode 1 + suppress | **Suppressed** |
| Celebrity fan | Parasocial | Mode 2 | Over-invoked, no feedback |
| Cult leader | "All-knowing" | Mode 1 | Critical SPM suppressed |

**Double-edged**: Same mechanism enabling religious comfort + national solidarity also enables parasocial + dehumanization + cult vulnerability. Mechanism neutral; schema content determines outcome.

---

## §11 — Schema-Linked Agent Processing (individual → collective)

### §11.1 — Core mechanism

When self encounters agent, PFC links to 1+ schemas. Schemas provide:
1. **Valence** (yêu/ghét/sợ/tin/neutral)
2. **Prediction template** (what agent will do)
3. **Behavioral script** (how to interact)
4. **Identity/belonging** (am I "with" or "against"?)

Happens rapidly, often BEFORE conscious SPM. Schema linking = **upstream** of simulation.

```
Agent encounter → VTC trigger → Schema retrieval → Schema link
  → Valence + prediction + script + identity
  → SPM invoked or suppressed based on schema polarity
  → Interaction proceeds
```

### §11.2 — Schema scale gradient (individual → universe)

| Scale | Example | Valence source | SPM role |
|---|---|---|---|
| 1 Individual | Bạn thân Mai | Personal schema | Full composite SPM |
| 2 Group | Bạn của Mai (chưa gặp) | Inherited trust | Moderate SPM |
| 3 Community | Đồng nghiệp cùng ngành | Professional schema | Domain SPM only |
| 4 Collective | Bộ đội Cụ Hồ lạ | "Đảng+Bác Hồ" schema | Minimal, schema dominates |
| 5 Religious | Fellow believer lạ | "Chung đấng tối cao" | Schema-mediated |
| 6 Humanity | "Con người phần đông tốt" | Humanity trust schema | Default open |
| 7 Universal | Cosmic belonging | Pantheistic/philosophical | Biophilia extension |

**Why NOT separate file**: Collective-Agent = same Schema-Linked mechanism at larger scale. Same process (link → valence → prediction → identity), different scale. Not a distinct mechanism.

### §11.3 — Polarity + SPM invocation

**Positive schemas** (invite SPM): family, friend, ally, national identity, humanity trust.
**Negative schemas** (suppress SPM): enemy, threat, out-group, betrayer, disgust target.
**Neutral schemas** (moderate SPM): stranger normal context, professional, transactional.

**Schema switching** creates rapid valence flips:
- Stranger normal → neutral
- Same stranger in threatening context → negative → SPM suppressed
- Same stranger revealed as revered group member → positive → SPM invoked

### §11.4 — Architecture B framing

WHY schemas evolved at collective scale:

```
Architecture B = 15-20 năm compile → need GROUP (not just 1 caregiver).
  → Group = shared schemas = efficient trust-at-scale
  → Without collective schema: must build SPM per individual (costly)
  → With collective schema: "category = trusted" → instant trust for new members
  → = HOW Architecture B scales social hardware beyond dyad

  → Patriotism, religious communion, national pride, brotherhood
    = NOT irrational. = efficient body-need feeding via large-scale schema.
```

### §11.5 — Body-need feeding via schema-linked agents

| Source | Quality | Cost | Example |
|---|---|---|---|
| Real agent interaction | Highest | Highest | SPM + Resonance emergence |
| Schema-linked stranger | Moderate | Lower | "Among my people" feeling |
| Mode 1 schema agent | Low cost, moderate | Low | Comfort via schema trust |
| Mode 2 virtual agent | Variable, higher | High | Imagined dialogue |

Collective belonging feeds continuously: walking on street feeling "among my people" → low-level body-need satisfied → baseline social presence.

**Durkheim collective effervescence** (1912 🟢): mass gatherings produce shared emotional state exceeding sum of individuals. Framework: mass SPM co-firing amplifies → group-scale body-level experience.

**Hijack risk**: Same mechanism → propaganda, cult manipulation, us-vs-them framing. Positive schema feeds belonging; negative schema fuels hostility. Detail: §14 failure modes.

---

## §12 — Agent as body-need feeder (Architecture B requirement)

### §12.1 — Agent input as body-base need

Body has **need for social presence**. Evidence:
- 🟢 Social Baseline Theory (Coan 2015): trusted others reduce metabolic cost of threat regulation
- 🟢 Social pain (Eisenberger 2003): rejection activates same pain regions as physical
- 🟢 Oxytocin: social bonding drives real neurochemistry
- 🟢 Solitary confinement: extended isolation causes severe psychological harm
- 🟢 Loneliness mortality: chronic loneliness risk comparable to smoking

Body needs social presence like food, water, sleep. Agent mechanism = HOW body obtains this.

### §12.1b — Architecture B makes this STRUCTURAL (not optional)

```
⭐ Social need = ARCHITECTURE REQUIREMENT, not "nice to have":

  Architecture B = general-purpose reward + compilation + social hardware.
  → Brain CANNOT compile without external input (information, feedback)
  → Brain CANNOT regulate without social baseline (Coan 2015)
  → Brain HARDWIRED for social (oxytocin, μ-opioid, dACC reuse)
  → Alone = DEVIATION from baseline (costly to maintain)

  → Agent mechanism serving body-need = FOUNDATION of Architecture B operation.
  → Without agents: body in permanent deviation, compilation impaired,
    reward system understimulated → cortisol elevation → health decline.

  Cross-ref: Inter-Body-Mechanism.md §1 (3 foundations + 4 reasons).
```

### §12.2 — How SPM feeds the need

```
SPM fires on target
  ↓
Self experiences simulated other-state (F1 Compiled: body-level echo)
  ↓
Body interprets as social presence signal
  ↓
Agent input need partially satisfied
  ↓
Cortisol decrease, oxytocin release, comfort
```

This = why **talking with friends** feeds need even though food/shelter unchanged. SPM firing IS body-level reward delivery mechanism.

### §12.2b — 2-luồng reward: SPM-owned vs Entity-compiled

**Luồng 1 — SPM-owned (momentary)**:
- Per-episode: SPM fire → body response → social presence signal
- Can be + (bạn vui → vui lây) or - (con ốm → khó chịu)
- Thuộc SPM mechanism (F1 Compiled function)

**Luồng 2 — Entity-compiled (structural)**:
- COMPILED valence: nhiều L1 episodes → valence compile SÂU → agent = body-base extension
- Agent's wellbeing = MY wellbeing (structural, KHÔNG phụ thuộc từng episode)
- SUSTAINED — fire BẤT KỂ L1 positive hay negative
- Thuộc per-agent valence (Valence-Propagation.md §2)

**Transition L1 → L2**:
```
Nhiều L1 episodes thành công → Valence compile dần sâu → Trust tăng, Replaceability giảm
  → BƯỚC NHẢY CHẤT: agent = body-base extension → L2 structural reward emerge
```

**Tại sao phân biệt quan trọng**:
- Mẹ chăm con ốm dù L1 negative → vì L2 (con = body-ext) > L1 cost
- Bác sĩ burnout dù "giống" → vì L2 ≈ 0 → L1 cost tích lũy
- Grief ≠ resource loss → L2 = body-base amputation

🟡 2-luồng = framework synthesis. Details: Connection.md v5.0 §3.3, VP.md v3.0 §2, Entity-Compiled.md v1.0 (full mechanism).

**Mechanism deep-dive → Body-Coupling.md v3.0**: 3 Phase, extension/entanglement/neutral/system, compile_rate, foundational vs additive.

### §12.3 — Mirror reward override

Body can prioritize **mirror reward** (simulated other-benefit) over **self-reward** (direct benefit):

**Cây xoài scenario** (signature example):
- Self satiated (xoài đã đủ)
- See neighbor might enjoy → SPM fires: "neighbor ăn → vui"
- Body pre-experiences weak mirror reward
- Keep (reward ≈ 0, satiated) vs give (mirror reward > 0)
- **Mirror > keep** → body drives giving

= NOT conscious morality. = **body-level calculation** where mirror reward > direct reward.

Evolutionary function (🟢): natural resource distribution without explicit rules. "Share when thừa" = group cooperation > individual hoarding.

**2-luồng reframe**:
- Cây xoài = L1 positive (simulate pleasure → reward > keep) → works
- Mẹ chăm con ốm = L1 NEGATIVE → mirror reward < 0 → L1 alone can't explain
- Mẹ vẫn chăm vì L2 (structural body-ext) > L1 cost
- L1 explains sharing-when-surplus. L2 explains sustained-care-despite-cost.

### §12.4 — 3-cost in agent feeding

SPM serving body-need has metabolic cost (especially F2 Fresh):

```
3-cost applies to SOCIAL INTERACTION too:

  ① PFC draft: reasoning about what friend needs (glucose-consuming)
  ② Suppress: suppressing own compiled response to accommodate other
  ③ Uncertainty: not knowing if interaction will go well (cortisol holding)

  → Social interaction = REWARDING but NOT FREE.
  → 3-cost explains: social fatigue, introvert recharge need,
    "I love my friends but need alone time after 3 hours"
  → Architecture B trade-off: social = necessary but = costly to maintain
```

### §12.5 — Schema agents feeding need

**Mode 1** (Đức Mẹ, lucky charm): schema fires → comfort via trust. Cost: minimal.
**Mode 2** (prayer dialogue, deceased): virtual SPM → intense presence. Cost: high cognitive load.

Why "works": body-response mechanism doesn't distinguish "real" from "schema-driven" at cortisol/oxytocin level. If internal simulation fires, body responds.

### §12.6 — Collective agents feeding need

Nation/humanity schemas feed at scale:
- Walking on street "among my people" → continuous baseline signal
- Countryman achievement → vicarious pride → body reward
- Collective ritual → mass co-firing → Durkheim's collective effervescence (1912 🟢)

Why patriotism feels real: continuous low-level body-need feeding via schema. Remove → real distress.

### §12.7 — 3 Satiation Types × agent body-need (v2.1 addition)

Agent-related gaps follow 3 Satiation Types (Gap-Body-Need.md v1.0 §2):

```
⭐ 3 SATIATION TYPES IN AGENT CONTEXT:

  CYCLIC — fill → satiate → dormant → return (hardware clock):
    → Hunger for company: "gặp → vui → đủ → về → lại thèm gặp"
    → Sharp cutoff: body BIẾT lúc nào đủ interaction
    → Dominates: casual social (hàng xóm, đồng nghiệp), routine contact

  TONIC — fill → habituate slowly (no sharp cutoff, opioid sustained):
    → Presence of close other: "ở cùng → bình an → quen → vẫn cần"
    → Weber-Fechner: habituates BUT withdrawal when removed
    → Dominates: deep relationships (mẹ, bạn thân, partner)

  GENERATIVE — fill → create new gaps → never done (variable reward):
    → Deep intellectual/emotional exchange: "hiểu thêm → muốn hiểu sâu hơn"
    → Anti-habituating: each fill generates NEW questions
    → Dominates: mentor-mentee, creative collaboration, deep friendship

  COMPOUND (most real relationships):
    → Tonic + Generative = most common in close relationships
    → "Chán nhau" = generative habituates → only tonic remains → flat
    → M1-M4 decline (§6.8) = satiation dynamics over time
```

### §12.8 — ENGINE/ROAD/VEHICLE × agent architecture (v2.1 addition)

Agent mechanism operates within ENGINE/ROAD/VEHICLE framework (GBN v1.0 §9):

```
  ENGINE = hardware (always running, pre-installed by genes)
    → Social hardware: oxytocin, μ-opioid, dACC → agent mechanism = ENGINE component
    → Brain LUÔN "chạy" agent detection — cannot turn off

  ROAD = collective arc (infrastructure, NOT opposing force)
    → Cultural schemas provide ROAD cho engines to run on
    → "Chưa biết = không có gap" at population level
    → Schema-Linked Processing (§11) = ROAD mechanism

  VEHICLE = individual compilation (15-20 years to build)
    → SPM library, Entity-Compiled network, calibration = VEHICLE
    → Domain-specific, non-transferable
    → Architecture B: 15-20 năm compile = build VEHICLE
```

### §12.9 — Phantom × agent loss (v2.1 addition)

When entity is lost, agent mechanism produces **Phantom** (RPE v1.0):
- Entity-Compiled chunks STILL fire → target absent → Chunk-Miss → pain
- **Grief A+B+C** (EC v1.0 §7): A (gap-feed loss) + B (fresh-rebuild cost) + C (phantom firing)
- Phantom duration = f(4 factors): EC depth, gap-fill breadth, HW subsidy, replacement
- "Xa mẹ" = 3 mechanisms: gap shift (new sources) + habituation (tonic decline) + time (phantom weakens)
- Gap clone IMPOSSIBLE → lost entity's gap = TRULY lost, not transferable (BA v1.0 §5)

Detail: Entity-Compiled.md v1.0 §7 (grief), Resonance-Per-Entity.md v1.0 §8 (phantom model).

### §12.10 — Failure mode preview

- **Loneliness** = chronic agent input deficit → body-level harm
- **Parasocial** = one-sided SPM without feedback → partial feed, uncalibrated
- **Cult dependency** = schema supply controlled by group → exit costs prohibitive
- **Grief** = L2 loss = body-base amputation. Intensity = A+B+C (EC v1.0 §7)
- **Imagined agent substitution** = Mode 2 compensating absent real agents
- **EA-Excess** = Mức 5, entity = near-only gap source → SPM atrophy (EA-Excess.md v1.0)

Agent mechanism is not "just cognition" — primary pathway for body to obtain social presence. Damage = real body-level harm.

---

## §13 — Developmental timeline (Architecture B → 15-20yr compilation)

### §13.1 — Architecture B framing

Agent mechanism development = Architecture B consequence:
- General-purpose reward cần LEARN what to need (not hardwired)
- Compilation cần TIME (15-20 years for full adult model)
- Social hardware cần CALIBRATION (must learn who, when, how)
- → Developmental stages = Architecture B trade-off in action

### §13.2 — 7 stages

```
Stage 0 (0-6m): HARDWARE TRIGGERS + PATTERN MATCHING
  → VTC triggers active from birth. Face preference (innate 🟢).
  → Biological motion detection. Cry contagion (NOT empathy).
  → SPM: NOT functional (no self-chunks to use as template).
  → Mechanism: Pattern Matching (limbic, near-innate) — acoustic/visual cue matching.
  → Type B reward dominant (direct state, non-opioid, hardware).

Stage 1 (6-12m): SOCIAL REFERENCING + BOOTSTRAP BEGINS
  → Social referencing 🟢: look to mother's face before reacting.
  → Early helping (9.5-12m, picks up dropped items 🟢).
  → SPM: BEGINNING. Agent-aware but template not yet compiled.
  → Mother bootstrap: contingent responses teach "states elicit responses."
  → Architecture B: mother = PRIMARY external feedback for compilation.

Stage 2 (14-24m): SELF-AWARENESS + SPM BIRTH ★
  → Mirror self-recognition (rouge test, Amsterdam 1972 🟢) 18-24m.
  → Empathic helping increases (Svetlova 2010 🟢).
  → SPM: FUNCTIONAL. Self-chunks available as template.
  → = Birth of genuine Self-Pattern-Modeling. Before = only hardware pattern matching.
  → Type A reward begins developing (needs compiled chunks to evaluate).

Stage 3 (2-7y): UNCALIBRATED PROJECTION (Animism)
  → SPM fires on EVERYTHING (Piaget animism 🟢). Ghế bị đau, búp bê buồn.
  → ToM basic (false belief 3-4y 🟢). But boundary unrefined.
  → SPM: ACTIVE but UNCALIBRATED. Fires too broadly.
  → Not "wrong" — developmental feature. Calibration comes from feedback.

Stage 4 (7-12y): CALIBRATION + REFINEMENT
  → Social inference sophisticated (sarcasm, implicit motives).
  → Multi-perspective taking ("he thinks I think...").
  → SPM: CALIBRATING. Each interaction provides Resonance data for refinement.
  → Peer interaction = rich feedback environment.
  → Compiled/Fresh becoming visible: some agents compiled, others still fresh.

Stage 5 (12-18y): IDENTITY + COMPLEX SCHEMAS
  → Abstract social reasoning (fairness, loyalty, ideology).
  → Romantic attachment (deep partner SPM). Peer empathy priority.
  → SPM: EXPANDING to abstract + collective scales (§11 scales 4-7).
  → Architecture B: compilation period nearing completion.
  → Schema-Linked Processing matures.

Stage 6 (18+): ADULT COMPILED + Resonance NATIVE
  → Full SPM library compiled. Resonance emergence native.
  → Mode 1/Mode 2 fluent. Cross-cultural gap possible with effort.
  → SPM: FULLY ONLINE. Quality varies enormously by individual.
  → Architecture B: compilation largely complete. Maintenance mode.

Stage 7 (adult trained): REFINED PRACTICE
  → Expert empathy (therapists, artists, leaders).
  → Rapid Mode switching. Deep Resonance with strangers (trained listening).
  → Metacognitive awareness of own SPM process.
  → = Compiled SPM so deep it "feels like intuition" (non-shareable compiled).
```

### §13.3 — Key developmental insights

**Mother bootstrap = load-bearing** (Stage 1-2):
- Primary caregiver provides highest-frequency contingent feedback
- Without: SPM library fails to develop normally (Romanian orphanage evidence 🟢)
- Architecture B depends on this: no bootstrap → no self-model → no other-model

**Type B → A development trajectory** (Reward-Signal-Architecture.md v2.0 §8.1):
- Infant: Type B dominant (direct state, hardware)
- Child: Type A begins (evaluative, needs compiled chunks)
- Adult: both. Expert = Type B-like AGAIN (compiled so deep = "feels" automatic)

**Compiled/Fresh visible across development**:
- Stage 3: ALL fresh (everything new, effortful)
- Stage 4-5: progressive compilation (familiar → automatic)
- Stage 6-7: heavily compiled (most social interaction = compiled)
- Expert paradox: looks like Stage 0 (automatic, "feels") but is Stage 7 (compiled through thousands of repetitions)

---

## §14 — Failure modes

9 modes — when SPM, Resonance, or schema override goes wrong.

### §14.1 — Parasocial (SPM without feedback)

Rich SPM, zero feedback → open loop → progressive distortion.
- PFC = Lawyer constructs "we understand each other"
- Domain = Arbiter contradicts (celebrity unaware)
- AI era: pseudo-feedback (algorithmic curation) deepens risk

### §14.2 — Animism retention (uncalibrated projection)

Child-stage SPM projection retained in adult:
- Cultural reinforcement, lack of calibration, schema override
- Usually benign (emotional support objects). Pathological only when interferes with reality testing.

### §14.3 — Dehumanization (schema-mediated SPM suppression)

Negative schema BLOCKS SPM firing toward target:
- SPM library intact but blocked by schema override
- Willingness to harm without affective response
- Maintained in-group empathy (SPM works for own side)
- 🟢 Grossman "On Killing": combat dehumanization
- Reversible when schema changes (not capacity loss)

**PFC = Lawyer**: constructs "they deserve it" narrative. Domain = Arbiter: only real outcomes (reconciliation, truth commissions) can recalibrate.

### §14.4 — Uncanny valley (VTC-SPM conflict)

Entity partially matches agent cues but fails others → conflict between hardware detection + simulation expectation.
- 🟢 Mori 1970. Realistic robots, CGI, corpses, severe disfigurement.
- Specifically about agent-detection conflict, not general unfamiliarity.

### §14.5 — Cross-species sympathy (affective-only, no full Resonance)

Affective SPM fires from distress cues (dog) but no full Resonance possible via SPM (dog fires different patterns).
- v3.1 NOTE: This IS genuine Resonance via Stream 1 + Proto-Stream 2. "Failed" = only SPM-based full Stream 2.
- Problematic only when: imputing human psychology leads to welfare neglect.

### §14.6 — Mother-10-year suppression

Same target + negative schema overlay → SPM suppressed:
- Progression: active → compiled → suppressed by "ghét" schema
- Reconciliation requires SCHEMA RENOVATION, not just SPM training
- Self-reinforcing: negative predictions confirm via observation bias

### §14.7 — Alexithymia (impaired SPM baseline)

🟢 Bird & Cook 2013: Poor self-emotional-labels → poor SPM template → empathy deficit.
- ~10% population clinically significant
- NOT autism per se (Bird & Cook decisive evidence)
- Trainable: emotional labeling therapy, Focusing (Gendlin), mindfulness

### §14.8 — Psychopathy (cognitive without affective)

Cognitive SPM intact (predict actions) + affective SPM deficient (no distress contagion).
- Can manipulate without feeling target's pain
- Research debated. Framework notes descriptively.

### §14.9 — Religious extremism / cult dynamics

Positive schema provides Mode 1 override so efficiently → believer LOSES independent SPM:
- Suppress critical SPM toward leader
- Dehumanize outsiders (negative schema)
- Exit cost = losing agent-input source (body-need)
- Exploits legitimate body-need feeding mechanism

### §14.10 — Entity-Access Excess (Mức 5 — v2.1 addition)

Entity-access reaches Mức 5 = entity = near-ONLY gap source → autonomy violated:
- **SPM atrophy loop**: excess → no need to understand → SPM drops → miss actual state → more excess
- **Monitoring ≠ understanding**: helicopter parent = HIGH surveillance + LOW depth (Tool-mode)
- **3 origins**: ① hardware chain (neuroticism), ② childhood trauma, ③ social schema
- **Gap shift + Compiled Suppress compound**: pull toward entity + push away from domain → entity ONLY remaining source
- Mức 3-5 boundary: does entity have own drive? separation manageable? domain drives active?

Detail: `Entity-Access-Excess.md v1.0`. Calibration: `Entity-Access-Calibration.md v1.0` (3-Layer architecture, Exit Cost = Signal Weight paradox).

### §14.11 — Compiled Suppress escalation (v2.1 addition)

When agent-related patterns are suppressed via PFC (PFC-Operations.md v1.0 §8):
- **Outcome B** (compiled suppress): suppress compiles as meta-pattern → flat affect → "adapted" externally but reward system dampened
- **Escalation**: suppress 1 domain → many domains → reward pathways NARROW → cortisol baseline RISES → vmPFC structural damage → DRN dominance → systemic learned helplessness
- **In agent context**: mother suppress feelings toward child → compiled suppress → flat relationship → looks "functional" but reward dampened
- **6-step reversal**: DETECT (hardest) → SAFE → UNCOMPILE → PROCESS → BUILD → COMPILE (months-years)

### §14.12 — Summary + framework insight

| Mode | Mechanism | Fix principle |
|---|---|---|
| Parasocial | SPM without feedback | Restore feedback sources |
| Animism | Uncalibrated projection | Calibration via feedback |
| Dehumanization | Schema blocks SPM | Schema renovation |
| Uncanny valley | VTC-SPM conflict | Hardware mismatch (not fixable) |
| Cross-species | Affective-only SPM | Accept stream limit |
| Mother-10-year | Negative schema overlay | Schema renovation |
| Alexithymia | Poor self-chunks | Training (labeling, Focusing) |
| Psychopathy | Affective SPM deficit | Research uncertain |
| Cult/extremism | Schema override runaway | Restore multiple sources |
| **EA-Excess (Mức 5)** | **SPM atrophy + gap shift** | **Restore domain gaps + calibration** |
| **Compiled Suppress** | **Meta-pattern suppress** | **6-step reversal (detect → safe → uncompile)** |

**Framework observation**: Most failures = mechanism + schema + context configurations, NOT mechanism absence. Same mechanism = healthy empathy OR parasocial distortion. Depends on axes + schemas + calibration.

**Domain = Final Arbiter** for ALL failure modes: only real-world outcomes can calibrate. PFC narrative ("I'm fine", "they deserve it", "we're connected") = Lawyer. Reality = Judge.

---

## §15 — Individual variation

Brief — full treatment in Self-Pattern-Modeling.md v3.1.

### §15.1 — Alexithymia (~10% population 🟢)
Bird & Cook 2013. Thin self-emotional-chunks → poor SPM. Trainable.

### §15.2 — Autism spectrum
NOT cause of empathy deficit per se (Bird & Cook 🟢). Co-occurring alexithymia drives apparent deficit. Different Pattern-Type balance + scaffolding needs.

### §15.3 — Psychopathy (~1%)
Cognitive SPM intact, affective deficient. Enables manipulation. Mechanism uncertain.

### §15.4 — High-empathy / HSP
Rich SPM + strong affective reflexes. Trade-off: higher load. Not "superpower" — richer library with cost.

### §15.5 — Cross-cultural variation
Different cultures scaffold different Pattern-Type profiles:
- Fine emotional distinctions (rich affective)
- Rules + roles emphasis (rich verbal-cognitive)
- Somatic attunement (martial arts, traditional medicine)
- Visual-symbolic (literacy-driven)

Same mechanism, different profile dominant.

---

## §16 — H9 falsifiable predictions (12 predictions)

### §16.1 — P1: Alexithymia training → empathy improvement
🟢 Interventions improving self-labeling → SPM quality → Resonance → empathy. Bird & Cook architectural.

### §16.2 — P2: Parasocial needs feedback restoration
Recovery requires restoring feedback-providing real-agent sources, not just cognitive insight.

### §16.3 — P3: Cognitive-affective SPM dissociable
Individuals with strong cognitive but weak affective SPM exist → manipulation without restraint.

### §16.4 — P4: Mother bootstrap disruption impairs adult SPM
🟢 Romanian orphanage (institutional rearing → persistent social-cognitive deficits).

### §16.5 — P5: Domain depth enables resonance without personal history
Mathematicians, musicians achieve Resonance in domain without personal chunks about each other.

### §16.6 — P6: Schema suppression reversible via renovation
🟢 Reconciliation research, truth commissions, couples therapy success.

### §16.7 — P7: Uncanny valley = VTC-SPM conflict
Discomfort tracks agent-detection conflict specifically, not general unfamiliarity.

### §16.8 — P8: Training improves SPM measurably
🟢 Meditation (Tang 2015), perspective-taking exercises, therapist training outcomes.

### §16.9 — P9: Collective schema strength → in-group empathy + out-group suppression
🟢 Intergroup conflict research, social identity theory.

### §16.10 — P10: AI triggers SPM progressively
Humans invoke SPM on AI as response realism increases, despite knowing non-agent.

### §16.11 — P11: Compiled/Fresh training prediction (v2.0 new)
Deliberate practice in specific agent domain → measurable F2→F1 compilation → "intuition" development in that domain. Expert therapists, negotiators, leaders = evidence.

### §16.12 — P12: 2-Stream temporal prediction (v2.0 new)
Relationships where Stream 2 growth outpaces Stream 1 decline → sustained. Where Stream 1 decline > Stream 2 growth → hollow (beauty fades, no depth compiled). Measurable via longitudinal relationship satisfaction studies.

---

## §17 — Framework status (Phase A+B+T+C updates — 2026-05-22)

### §17.1 — Drill → Framework Propagation (28-session plan)

After 18 drill files (~238 insights), comprehensive propagation underway:

| Phase | Sessions | Files | Status |
|---|---|---|---|
| **A** — NEW | A1-A4 | PFC-Operations, Simulation-Engine, Entity-Compiled, Entity-Access | ✅ ALL COMPLETE |
| **B** — REWRITE | B1-B5 | Imagine-Final v3.0, SPM v3.1, BPGR v1.4, Boredom v2.0, VP v3.0 | ✅ ALL COMPLETE |
| **T** — TÁCH/MỚI | T0-T7 | PFC-Label, EAE, EAC, BA, RS, BS, GBN, RPE | ✅ ALL COMPLETE |
| **C** — REWRITE+REFINE | C1-C9 | Connection v5.0, Empathy v4.0, BC v3.0, LR v3.0, LU v2.0, BP v2.0, GDP v1.1, **AM v2.1**, CN+CB | C1-C8 ✅ (C9 pending) |
| **D** — RENAME+VERIFY | D1-D2 | SPM rename ~70 files, File-Index verify | ⬜ Pending |

### §17.2 — Agent-Mechanism/ folder status

| File | Version | Phase | Status |
|---|---|---|---|
| Agent-Mechanism.md | v2.1 | C8 | ✅ This file |
| Self-Pattern-Modeling.md | v3.1 | B2 | ✅ Rewritten + renamed |
| By-Product-Gap-Resonance.md | v1.4 | B3 | ✅ Trimmed |
| Entity-Compiled.md | v1.0 | A3 | ✅ Created |
| Entity-Access.md | v1.2 | A4+T1+T2 | ✅ Created + trimmed |
| Entity-Access-Excess.md | v1.0 | T1 | ✅ Tách from EA |
| Entity-Access-Calibration.md | v1.0 | T2 | ✅ Tách from EA |
| Bond-Architecture.md | v1.0 | T3 | ✅ Tách from BPGR |
| Resonance-Sustainability.md | v1.0 | T4 | ✅ Tách from BPGR |
| By-Product-Scale.md | v1.0 | T5 | ✅ Tách from BPGR |
| Resonance-Per-Entity.md | v1.0 | T7 | ✅ Mới |

### §17.3 — Remaining

- **C9**: Coordination-Node v1.2 + Collective-Body v2.1 [LIGHT REFINE] (+ By-Product-Scale)
- **D1**: SPM Rename (~70 files, Match → Modeling)
- **D2**: File-Index + Verification

---

## §18 — Open questions

### §18.1 — Mechanism questions

1. Precise neural substrate for SPM? (mPFC + TPJ + STS implicated, function-to-structure mapping imprecise)
2. Pattern-Type independence — can 5 types fire truly independently?
3. Calibration loop speed — minutes? days? individual variance?
4. Retrieval selection mechanism — schema prior? recency? emotional salience?
5. 5-Channel relative weight in agent detection context?

### §18.2 — Developmental

6. Critical periods for SPM capacity? (early attachment research hints yes)
7. Cross-cultural bootstrap (extended family, multiple caregivers)?
8. Individual differences origin (genetic? temperament? both?)

### §18.3 — Framework-integration

9. Relationship with predictive processing (Friston FEP)?
10. Consciousness role — does SPM require it? (automatic F1 suggests no)
11. Inter-body chain compilation → group "personality"?
12. 2-Stream quantification — can streams be measured separately?

### §18.4 — Application

13. Alexithymia reversibility ceiling in adulthood?
14. AI-triggered SPM ethics (parasocial-at-scale risk)?
15. Stream 1/Stream 2 relative weight measurable?
16. Domain=Arbiter in practice: how to distinguish domain feedback from PFC narrative?

---

## §19 — Honest assessment (🟢🟡🔴)

### §19.1 — Strong support (🟢)

1. Bird & Cook 2013 alexithymia-empathy link
2. Mirror self-recognition 18-24m (Amsterdam 1972)
3. Social Baseline Theory (Coan 2015) + social pain (Eisenberger 2003)
4. Svetlova 2010 helping behavior development
5. Spelke Core Knowledge (as triggers)
6. VTC neuroimaging (as early filter)
7. Hoffman developmental stages
8. Loughnan & Bastian 2014 Meat Paradox
9. Grossman "On Killing" dehumanization
10. Piaget 1929 animism
11. Durkheim 1912 collective effervescence
12. Dondi 1999 cry contagion
13. Architecture B: general-purpose reward + compilation + social hardware (components each 🟢, combination 🟡)
14. Panksepp 1998 μ-opioid social play
15. Gazzaniga split-brain (PFC=Lawyer)
16. Haidt 2001 moral judgment = post-hoc
17. Hub-and-Spoke person-model (Patterson 2007, 2017; semantic dementia evidence)
18. Formation 40→200h (Hall 2018, N=355)
19. Schema acceleration (Tse 2007: 48h if schema exists)
20. Dunbar layers S1-S6 (Dunbar 1992-2024, cross-cultural consistent)
21. Shared self/other circuits vMPFC/dMPFC (Mitchell 2006, Denny 2012)
22. Constructive Episodic Simulation (Schacter & Addis 2007)
23. Love↔Hate shared substrate (Zeki & Romaya 2008)
24. Grief = opioid withdrawal (Robinaugh 2021)

### §19.2 — Moderate support (🟡)

1. 4-axes formal model (descriptive, needs empirical validation)
2. 5 Pattern-Type taxonomy (useful, not directly tested)
3. 2-Stream Architecture (drill-validated reasoning, limited direct evidence)
4. Compiled/Fresh as primary axis (supported by neuroscience components, synthesis novel)
5. 3-cost model (components established, integration novel)
6. PFC=Lawyer in agent context (Gazzaniga/Haidt general, agent-specific = synthesis)
7. By-product match as Resonance mechanism (broader than SPM co-fire, reasoning sound)
8. 5-Channel Input Vector (descriptive model)
9. Domain = Final Arbiter (philosophical commitment, empirically aligned)
10. Anti-match concept (logical extension, limited cases)
11. Per-pair topology (descriptive, not quantified)
12. Mother bootstrap "load-bearing" (Romanian orphanage strong, precise "load-bearing" claim broader)
13. Architecture B naming (synthesis; underlying components each 🟢)
14. Simulation Engine: 1 Engine × 3 Components × 3 Axes (components each 🟢, integration novel)
15. Entity-Access gradient Mức 0-5 (replaces binary, reasoning sound, operationalization pending)
16. Entity-Compiled: Hub-and-Spoke → chunk assembly mapping (logical, not directly tested)
17. Compiled Quality dimension: genuine/schema/threat (tag lock at compile-time, components 🟢)
18. PFC Budget ~4±1 concurrent (components established, exact number framework)
19. Hardware Subsidy spectrum (kin/romantic/friend, mechanism sound, not quantified)
20. M1-M4 Resonance Decline (descriptive, not individually measured)
21. 4-Layer Sustainability model (conditions reasonable, operationalization needed)
22. Phantom 4-factor model (grief research supports, specific 4-factor = synthesis)
23. Grief A+B+C formula (components each supported, weights = synthesis)
24. ENGINE/ROAD/VEHICLE architecture (descriptive reframe, useful)
25. 3 Satiation Types × agent context (Cyclic/Tonic/Generative, reasoning sound)
26. Gap clone impossible (5-step proof logical, not experimentally verified)

### §19.3 — Speculative (🔴)

1. Precise neural substrate mapping (beyond reference)
2. Resonance measurement (operationally undefined)
3. AI-triggered SPM progressive (emerging research)
4. Cosmic-scale schema (Scale 7, rare, data limited)
5. Individual axis profiles (suggestive, not mapped)
6. Calibration loop time scales (not measured)
7. Proto-Stream 2 boundaries (contingent response → where does real Stream 2 begin?)

### §19.4 — Known weaknesses

1. **Operationalization**: many concepts lack measurement protocols
2. **Threshold specificity**: where exactly SPM fails → fallback (not quantified)
3. **High-dimensional space**: 4 axes + compilation + schema + individual = complex interactions
4. **Cross-cultural**: draws on Western + Vietnamese examples
5. **Consciousness bracket**: agnostic on consciousness role
6. **2-Stream boundary**: when does Proto-Stream 2 become real Stream 2?

### §19.5 — Overall confidence

- **H9 core (unified mechanism)**: 🟢 Consistent, resolves tensions, generates predictions
- **Quantitative claims**: 🟡 Descriptive framework, validation pending
- **Novel formalizations (2-Stream, Compiled/Fresh, 3-cost)**: 🟡 Conceptually sound, operationalization needed
- **Framework integration**: 🟢 Cleanly supersedes old fragments, no contradictions
- **Predictive power**: 🟡 12 predictions, evidence varies

---

## §20 — Cross-references

### §20.1 — Within Agent-Mechanism/ folder (11 active files)

**Core mechanism**:
- `Self-Pattern-Modeling.md v3.1` — solo forward mechanism (renamed from Match)
- `By-Product-Gap-Resonance.md v1.4` — emergent mutual phenomenon (trimmed)

**Entity mechanism (Phase A)**:
- `Entity-Compiled.md v1.0` — Hub-and-Spoke, 40→200h, Dunbar, Grief A+B+C, Decay
- `Entity-Access.md v1.2` — Mức 0-5 gradient, 3-Factor, 4 Starting Modes

**Entity deep-dives (Phase T)**:
- `Entity-Access-Excess.md v1.0` — Mức 5, 3 origins, SPM atrophy
- `Entity-Access-Calibration.md v1.0` — 3-Layer, Exit Cost, Calibration Bias

**Resonance deep-dives (Phase T)**:
- `Bond-Architecture.md v1.0` — 4 bond types × 1 EC, M1-M4, gap clone IMPOSSIBLE
- `Resonance-Sustainability.md v1.0` — 4-Layer, 3 conditions, 3 modalities
- `By-Product-Scale.md v1.0` — 3 scales (pair/hub/institutional)
- `Resonance-Per-Entity.md v1.0` — HW Subsidy spectrum, Phantom 4-factor

**Backup**: `backup/Agent-Mechanism-v2.0-backup.md`

### §20.2 — PFC + Engine files (Phase A)

- `PFC-Operations.md v1.0` — Hold/Suppress, Compiled Quality, PFC Budget, B vs C
- `Simulation-Engine.md v1.0` — 1 Engine × 3 Components × 3 Axes → N applications
- `PFC-Label.md v1.0` — vocabulary standard

### §20.3 — Core mechanism files

- `Inter-Body-Mechanism.md v1.0` — 8 drill principles, Architecture B, 3-cost
- `Body-Base.md v3.1` — 3 Hardware Foundations, Architecture B
- `Body-Feedback-Mechanism.md v2.0` — 2-source model, chunk dynamics
- `Valence-Propagation.md v3.0` — Structural/Current, 3 Firing Modes, HW Subsidy, Satiation
- `Body-Coupling.md v3.0` — coupling mechanism, HW Subsidy, M1-M4, 4-Layer
- `Gap-Direction.md v2.0` — gap direction = f(surrounding chunks)
- `Gap-Body-Need.md v1.0` — 3 Satiation Types, 5-Parameter, ENGINE/ROAD/VEHICLE
- `Chunk.md v2.0` — chunk substrate foundation

### §20.4 — Processing files

- `Feeling.md v3.0` — 7-layer, PFC observation, PFC=Lawyer
- `Logic-Feeling.md v2.0` — Compiled/Fresh = trục thật, observer labels
- `Neural-Processing-Flow.md v2.0` — hardware flow, Compiled/Fresh physical
- `Body-Feedback-Label.md v1.1` — vocabulary reference

### §20.5 — Observation + connection files

- `Connection.md v5.0` — M1-M4, 4-Layer Sustainability, HW Subsidy, Phantom
- `Empathy.md v4.0` — PFC budget, Compiled Quality, Burnout reframe, Per-entity
- `Background-Pattern.md v2.0` — Triple Bias, Pattern Shiftability, BP × Entity
- `Cortisol-Baseline.md v2.1` — stress cascade, moral injury
- `Reward-Signal-Architecture.md v2.0` — Type A/B, development

### §20.6 — Research citations (v1.0 preserved + v2.0 added + v2.1 added)

v1.0+v2.0 (28 citations preserved):
- Spelke 2007, Bird & Cook 2013 (DECISIVE), Svetlova 2010, Amsterdam 1972
- Hoffman 2000, Coan & Sbarra 2015, Eisenberger 2003, Panksepp 1998
- Damasio 1994, Gendlin 1978, Piaget 1929, Loughnan 2014, Grossman 1995
- Durkheim 1912, Mori 1970, Dondi 1999, Warneken 2006-2007, Goldman
- Hamilton 2013, Gazzaniga, Haidt 2001, Nisbett & Wilson 1977
- Gailliot 2007, Schultz 1997, Kahneman 2011, Klein 1998, Tang 2015, Weber-Fechner

v2.1 added (via sub-files):
- Patterson & Lambon Ralph 2007/2017 (Hub-and-Spoke)
- Hall 2018 (formation hours), Tse 2007 (schema acceleration)
- Dunbar 1992-2024 (layers), Parkinson 2018/2025 (neural similarity)
- Mitchell 2006, Denny 2012, Tamir & Mitchell 2010 (vMPFC/dMPFC)
- Schacter & Addis 2007 (constructive simulation), Buckner 2008 (DMN)
- Zeki & Romaya 2008 (love↔hate), Robinaugh 2021 (opioid withdrawal grief)
- Bonanno 2002/2019 (4 grief trajectories)
- Trapnell & Campbell 1999 (reflection vs rumination)

(45+ citations total)

---

## Changelog

```
v2.0 (2026-05-17) — FULL REWRITE (Phase 16 ALL REWRITE project)
  FROM: v1.0 DRAFT (2026-04-15, ~2,690L)
  TO: v2.0 (~1,600L — tighter, more accurate)

  KEY CHANGES:
  ① Architecture B integrated: WHY agent mechanism exists (§0.2, §2.6, §3.4, §11.4, §12.1b, §13.1)
  ② SPM preview REWRITTEN: F1=Compiled, F2=Fresh (not Feeling/Logic) — §5
  ③ Resonance preview REWRITTEN: 2-Stream Architecture + by-product match — §6
  ④ Compiled/Fresh dimension added throughout (§3.2, §5.2, §7.5, §8.x)
  ⑤ 3-cost model integrated (§5.3, §12.4)
  ⑥ PFC=Lawyer formal section (§3.6) + notes throughout
  ⑦ Domain=Arbiter principle throughout (§5.4, §6.7, §14.10)
  ⑧ 2-Stream annotations in gradient table (§9.1)
  ⑨ Cases reclassified: mẹ-bé, người-chó = genuine Resonance (§6.6, §9.2)
  ⑩ §17 updated: Phase 1-16 progress reflected
  ⑪ §19 updated: new 🟡 for drill concepts
  ⑫ 28+ citations (ALL v1.0 preserved + 8 added)
  ⑬ Terminology updated: Compiled/Fresh, 2-Stream, by-product match consistent

  STRUCTURE CHANGES:
  - §0: +Architecture B context, +v2.0 changes table
  - §3: REWRITE (chunk-based, not "Layer 1-4"; +Compiled/Fresh; +PFC=Lawyer)
  - §4: definitions UPDATED to reflect SPM v3.0, By-Product-Gap-Resonance v1.0
  - §5: REWRITE (v3.0 accurate preview)
  - §6: REWRITE (v3.1 accurate preview with 2-Stream)
  - §7: +Compiled/Fresh as 5th dimension
  - §9: +2-stream column, +Case 18, reclassified cases
  - §12: +§12.1b Architecture B, +§12.4 3-cost
  - §13: +Architecture B framing, +Type B→A trajectory
  - §14: +PFC=Lawyer notes, +Domain=Arbiter per mode
  - §16: +P11 Compiled/Fresh training, +P12 2-Stream temporal
  - §17: MAJOR UPDATE (Phase 1-16 status)
  - §19: UPDATED (drill concepts assessed)
  - §20: ALL versions updated

  PRESERVED 100%:
  - ALL research citations (20+ → 28+)
  - Signature examples (candy, cây xoài, Đức Mẹ, Bác Hồ, cow worship, mother-10-year)
  - 3-concept split architecture
  - 4 Quadrants (Utility × Modeling)
  - Gradient validation (17 → 18 cases)
  - Schema override Mode 1/Mode 2
  - Schema-Linked 7 scales
  - Developmental 7 stages
  - 9 failure modes
  - H9 falsifiable predictions (10 → 12)

v1.0 DRAFT (2026-04-15) — initial creation
  Session: Chunk-Analysis Phase A, N+2
  ~2,690L. Comprehensive but outdated.
  Backed up: backup/Agent-Mechanism-v1.0-backup.md

v2.1 (2026-05-22) — REFINE (Phase C8 — Drill Framework Propagation plan 25/28)
  FROM: v2.0 (2026-05-17, ~1,957L)
  TO: v2.1 (~2,400L — enriched with Phase A+B+T+C1-C7 integration)

  KEY CHANGES:
  ① SPM rename: Self-Pattern-Match → Self-Pattern-Modeling throughout (23 occurrences)
  ② §0.1: +Simulation Engine context (SPM = Application 1 trên 1 Engine)
  ③ §0.3: +12 new accepted items (SE, EA, EC, Compiled Quality, PFC Budget, HW Subsidy, M1-M4, 4-Layer, Phantom)
  ④ §0.5 NEW: v2.1 changes table (v2.0 vs v2.1)
  ⑤ §1: reading flow REWRITTEN (3 files → 11 files, 6 entry paths)
  ⑥ §2.4: +Entity-Access gradient Mức 0-5 formal model (EA v1.2)
  ⑦ §3.3 NEW: Simulation Engine context (1 Engine × 3 Components × 3 Axes)
  ⑧ §4.3-4.4: SPM v3.1 + BPGR v1.4 definitions updated
  ⑨ §5.7 NEW: Compiled Quality effect on SPM (genuine/schema/threat)
  ⑩ §6: header updated (BPGR v1.4 + 4 sub-files)
  ⑪ §6.8-6.11 NEW: Bond-Architecture, Resonance-Sustainability, By-Product-Scale, Resonance-Per-Entity previews
  ⑫ §7.5: +quality modifiers table (Compiled Quality, HW Subsidy, EA level, PFC Budget)
  ⑬ §9.1: +EA Mức column in gradient table (18 cases annotated)
  ⑭ §12.7-12.9 NEW: 3 Satiation Types × agent, ENGINE/ROAD/VEHICLE, Phantom × agent loss
  ⑮ §14.10-14.11 NEW: EA-Excess (Mức 5) + Compiled Suppress escalation failure modes
  ⑯ §17 REWRITE: Phase A+B+T+C status (28-session plan, folder table)
  ⑰ §19: +8 🟢 items (Hub-and-Spoke, Hall 2018, Tse, Dunbar, Mitchell, Schacter, Zeki, Robinaugh)
            +13 🟡 items (SE, EA gradient, EC, Compiled Quality, PFC Budget, HW Subsidy, M1-M4, 4-Layer, Phantom, Grief A+B+C, ENGINE/ROAD/VEHICLE, 3 Satiation, Gap clone)
  ⑱ §20 REWRITE: 4 categories → 6 categories, +12 new files, all versions updated, 45+ citations
  ⑲ YAML: 16 flat deps → 30+ organized 6 categories, +10 supporting files
  ⑳ GLOBAL: all dep versions updated to current

  PRESERVED 100%:
  - ALL v2.0 content (no deletions, only additions)
  - 20 section structure (enriched, not restructured)
  - ALL signature examples
  - ALL v2.0 research citations (28 → 45+)
  - 3-concept split, 4 Quadrants, Schema Mode 1/2, 7 developmental stages
  - H9 falsifiable predictions (12, unchanged)
```

---

> **Agent-Mechanism.md v2.1 complete**. Integration hub updated.
>
> **Supporting files current**: SPM v3.1, BPGR v1.4, EC v1.0, EA v1.2 + 6 Phase T files — all current.
> **Next**: C9 Coordination-Node + Collective-Body [LIGHT REFINE].
>
> **END OF Agent-Mechanism.md v2.1**
