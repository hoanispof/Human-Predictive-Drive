# Plan: Concept Cascade Refine

```
Status:    ✅✅ COMPLETE
Created:   2026-05-23
Completed: 2026-05-23
Scope:     27 files + 1 index, 12 sessions (merged from 14)
Actual:    ~1,339L new/modified content across 25 files + DMD v2.0 (+233L)
```

---

## 1. BỐI CẢNH

28-session Drill Framework Propagation Plan (2026-05-22/23) đã hoàn thành:
- Phase A: 4 NEW files (PFC-Operations, Simulation-Engine, Entity-Compiled, Entity-Access)
- Phase B: 5 REWRITE (Imagine-Final v3.0, SPM v3.1, BPGR v1.4, Boredom v2.0, VP v3.0)
- Phase T: 8 TÁCH/MỚI (PFC-Label, EAE, EAC, BA, RS, BS, GBN, RPE)
- Phase C: 9 REWRITE/REFINE (Connection v5.0, Empathy v4.0, Body-Coupling v3.0, Love-R v3.0, Love-U v2.0, BP v2.0, GDP v1.1, AM v2.1, CN v1.2 + CB v2.1)
- Phase D: SPM Rename (95 files) + File-Index + Verify

**Vấn đề phát hiện khi rà soát post-plan:**
~15 concept mới từ drill đã integrate vào 9 high-integration files (Phase C) nhưng CHƯA cascade xuống ~27 foundational/overview files. Các file này:
- Thuật ngữ hiện tại (SPM rename đã apply)
- Nội dung substantive (không stale)
- Nhưng KHÔNG reference bất kỳ concept mới nào (Entity-Access, Simulation Engine, Bond-Architecture, Hardware Subsidy, etc.)

---

## 2. CONCEPTS CẦN CASCADE

| Viết tắt | Concept đầy đủ | File nguồn | Đã integrate (Phase C) |
|----------|----------------|-----------|----------------------|
| EA | Entity-Access gradient | Entity-Access.md v1.2 | Connection, Empathy, BC, LR, LU, BP, AM |
| SE | Simulation Engine | Simulation-Engine.md v1.0 | Connection, BC |
| BA | Bond-Architecture (4 bond types) | Bond-Architecture.md v1.0 | Connection, LR, LU, BP |
| HwS | Hardware Subsidy | drill → Phase C | Connection, Empathy, BC, LR, LU |
| M1-M4 | 4 Firing Modes (M1-M4) | drill → T3 | Connection, Empathy, BC, LR |
| Sat | Satiation types (3 types) | drill → T6, GBN | LR, GDP, Connection |
| RS | Resonance-Sustainability (4-layer) | Resonance-Sustainability.md v1.0 | Connection, BP |
| BS | By-Product-Scale (1 mech × 3 scales) | By-Product-Scale.md v1.0 | AM, Connection |
| PFC-B | PFC Budget | drill → T0, PFC-Label | Empathy, GDP |
| RPE | Resonance-Per-Entity | Resonance-Per-Entity.md v1.0 | LR, LU |
| EC | Entity-Compiled | Entity-Compiled.md v1.0 | AM, Connection |
| PFC-Ops | PFC-Operations | PFC-Operations.md v1.0 | (new file, chưa cascaded rộng) |

---

## 3. NGUYÊN TẮC

1. **Chất lượng > tốc độ** — chậm mà chắc
2. **REFINE, không REWRITE** — giữ nguyên nội dung hiện tại, thêm cross-refs + brief sections
3. **Mỗi file cần:** đọc kỹ → xác định insertion points → thêm nội dung → update deps → version bump
4. **Chỉ thêm concept KHI RELEVANT** — không ép concept vào file không liên quan
5. **Ngoại lệ duy nhất:** Domain-Mapping-Drive.md = COMPLETION (viết sections chưa có)

### MỨC ĐỘ REFINE
- **LIGHT** = +30-80L: thêm cross-refs trong deps, 1-2 brief paragraphs tại insertion points
- **MODERATE** = +100-300L: thêm sub-sections mới, mở rộng nội dung, update structure
- **COMPLETION** = +500-2,000L: viết sections hoàn toàn mới

---

## 4. ORDERED SESSION LIST

### Phase A: Core Overview Cascade (2 sessions)

Lý do làm trước: Body-Base.md và Chunk.md là entry points cho toàn bộ framework. Cần reference ~15 new files từ Phase A/B/T mà chưa được mention.

```
A1. Body-Base.md                    [MODERATE REFINE] v3.1 → v3.2
    Folder: Body-Base/
    Lines:  1,298L → ~1,500L
    Công việc:
    - Update folder structure description (thêm ~15 new files)
    - Thêm brief mentions: SE, EA gradient, BA, HwS, M1-M4
    - Update deps table với Phase A/B/T files
    - Ensure folder navigation reflects current structure
    Concepts: EA, SE, BA, HwS, BS, RS, RPE, EC

A2. Chunk.md                       [MODERATE REFINE] v2.2 → v2.3
    Folder: Body-Base/Chunk/
    Lines:  1,608L → ~1,800L
    Công việc:
    - Update Agent-Mechanism/ folder description (+EAE, +EAC, +BA, +RS, +BS, +RPE, +EC)
    - Thêm brief section linking to new sub-files
    - Update deps table
    - Cross-ref SE as PFC mechanism
    Concepts: EA, EC, BA, RS, BS, RPE, SE
```

### Phase B: Observation Parameter Cascade (4 sessions)

Lý do: 10 core observation files + 1 bridge file = backbone của framework. Tất cả KHÔNG CÓ reference nào đến concepts mới. LIGHT refine — thêm cross-refs và brief linking paragraphs.

```
B1. Drive.md + Novelty.md + Threat.md              [LIGHT REFINE]
    Folder: Observation/
    Drive v1.1 → v1.2 (~50L added)
    - +SE: drive prediction uses simulation
    - +EA: drive directed at entities along gradient
    - +Sat: different drives have different satiation profiles
    Novelty v1.1 → v1.2 (~50L added)
    - +SE: novelty = prediction mismatch in simulation
    - +Sat: novelty satiation dynamics
    - +PFC-B: novelty seeking limited by PFC budget
    Threat v1.1 → v1.2 (~50L added)
    - +SE: simulated threat (Imagine-Final v3.0 boundary)
    - +EA: threat FROM entities (access-based framing)
    - +BA: threat to bond → protect response

B2. Status.md + Meaning.md                         [LIGHT-MODERATE REFINE]
    Folder: Observation/
    Status v2.1 → v2.2 (~100L added)
    - +EA gradient: status hierarchy = access gradient reframe
    - +HwS: status hardware (serotonin, cortisol)
    - +BS: status across 3 scales (individual→collective)
    - +M1-M4: status display per firing mode
    Meaning v2.1 → v2.2 (~60L added)
    - +BA: meaning through bond architecture
    - +RS: meaning sustainability (4-layer)
    - +RPE: meaning per-entity dynamics

B3. Gratitude.md + Obligation.md + Protect.md      [LIGHT REFINE]
    Folder: Observation/
    Gratitude v2.0 → v2.1 (~50L added)
    - +BA: gratitude as bond-strengthening signal
    - +BS: gratitude across scales
    - +RS: gratitude sustainability
    Obligation v1.1 → v1.2 (~50L added)
    - +EA: obligation = perceived access cost
    - +BA: obligation within bond types
    - +HwS: obligation hardware basis
    Protect v1.1 → v1.2 (~50L added)
    - +EA: protect = maintain entity access
    - +BA: protect bond integrity
    - +M1-M4: protect response per firing mode

B4. Autonomy.md + Autonomy-Hardware.md + Liking-Wanting.md  [LIGHT-MODERATE]
    Folder: Observation/
    Autonomy v1.1 → v1.2 (~40L added)
    - +EA: autonomy = control over own access gradient
    - +SE: autonomous simulation capacity
    Autonomy-Hardware v1.1 → v1.2 (~40L added)
    - +EA: vmPFC/DRN hardware supports access calibration
    - +HwS: autonomy hardware subsidy
    Liking-Wanting v1.0 → v1.1 (~100L added)
    - Bridge file cần alignment check với:
      +BA (6 wanting mechanisms ↔ 4 bond types)
      +Sat (liking satiation = opioid dynamics)
      +HwS (wanting hardware subsidy)
    - Review §2-§3 cho consistency với new frameworks
```

### Phase C: Domain Cascade (2 sessions)

Lý do: 5 Domain files (4 substantive + 1 entry point) đều thiếu references đến new concepts. Nội dung chất lượng cao nhưng cần cross-linking. 3 files cần YAML header standardization (hiện là DRAFT format).

```
C1. Domain.md + Conflict-Dynamics.md + Knowledge-Flow.md   [LIGHT REFINE]
    Folder: Domain/
    Domain.md DRAFT → v1.0 (~60L added + YAML header)
    - +SE: domain simulation in §4 (Imagine-Final bridge)
    - +EA: domain access in §2 (resource access = gradient)
    - +PFC-B: domain mapping limited by PFC budget
    - Standardize YAML header
    Conflict-Dynamics.md v1.0 → v1.1 (~60L added)
    - +EA: overlap reframe (accessing same point on gradient)
    - +SE: security dilemma = simulated threat
    - +Sat: scarcity as engine ↔ satiation dynamics
    Knowledge-Flow.md DRAFT → v1.0 (~60L added + YAML header)
    - +SE: PFC draft process = simulation engine
    - +PFC-B: bandwidth limits arc parallelism
    - +HwS: why compression works (hardware does heavy lifting)
    - Standardize YAML header

C2. Discovery-vs-Expansion.md + Emergent-Patterns.md       [LIGHT REFINE]
    Folder: Domain/
    Discovery-vs-Expansion.md DRAFT → v1.0 (~60L added + YAML header)
    - +SE: Phase 2 "thử ghép" = simulation engine
    - +M1-M4: discovery scatter/converge ↔ firing modes
    - +Sat: mapping-drive satiation ≠ consumption satiation
    - Standardize YAML header
    Emergent-Patterns.md v1.1 → v1.2 (~50L added)
    - +BA: emergent bond patterns
    - +BS: by-product match across scales
    - +RS: pattern resonance sustainability
```

### Phase D: Mechanism + Collective Cascade (2 sessions)

Lý do: Overview/mechanism files cần reference formal files tạo từ Phase A/B/T. Collective files (3 chưa updated) cần alignment.

```
D1. Inter-Body-Mechanism.md + Why-Body-Knows.md + Neural-Architecture.md
    [MODERATE REFINE]
    Folder: Body-Base/ + Core-Deep-Dive/
    Inter-Body-Mechanism.md v1.0 → v1.1 (~150L added)
    - Overview file cho drill → cần reference ALL formal files
    - +refs đến: BA v1.0, RS v1.0, BS v1.0, RPE v1.0, EC v1.0
    - +refs đến: EAE v1.0, EAC v1.0, GBN v1.0
    - Update "formal files created" section
    Why-Body-Knows.md v1.1 → v1.2 (~60L added)
    - +HwS: hardware subsidy as body mechanism
    - +SE: body knows via simulation feedback
    - +Sat: body satiation signals
    Neural-Architecture.md v1.0 → v1.1 (~80L added)
    - +SE: simulation engine neural basis (PFC+hippocampus)
    - +EA: entity-access neural correlates
    - +Modality mapping refinement

D2. Collective-Purpose.md + Compliance-Floor.md + Collective-Arc-Dynamics.md
    [LIGHT REFINE]
    Folder: Collective/
    Collective-Purpose.md v1.1 → v1.2 (~50L added)
    - +BA: collective bond architecture
    - +RS: collective resonance sustainability
    - +BS: by-product match at collective scale
    Compliance-Floor.md v2.0 → v2.1 (~40L added)
    - +EA: compliance = minimum access requirement
    - +HwS: compliance hardware basis
    Collective-Arc-Dynamics.md v1.1 → v1.2 (~50L added)
    - +BA: bond dynamics in arc shifts
    - +RS: arc sustainability factors
    - +BS: scale-dependent by-product
```

### Phase E: Domain-Mapping-Drive COMPLETION (2 sessions)

Lý do: File duy nhất CHƯA HOÀN THÀNH trong framework. Hiện chỉ có §0-§1 (~400L, Phase 1/6). Cần viết §2-§7. Nền tảng chất lượng cao (research-backed), cần maintain quality khi complete.

```
E1. Domain-Mapping-Drive.md        [COMPLETION] §2-§4
    Folder: Domain/
    Lines:  ~400L → ~1,200L (+800L)
    Công việc:
    - §2: Mechanism formalization — WHY mapping-drive exists
      (+SE: mapping = simulation exercise)
      (+Sat: mapping-drive satiation ≠ consumption satiation)
      (+PFC-B: mapping limited by budget)
    - §3: 3-way balance (Body-Need × Domain-Feedback × Social-Context)
      (+EA: mapping as access expansion)
      (+HwS: hardware supports mapping-drive)
    - §4: Implications — WHAT happens when mapping blocked/excessive
      (+BA: mapping within bond context)
      (+M1-M4: mapping intensity per firing mode)
    Maintain: citation discipline (🟢/🟡/🔴), research grounding

E2. Domain-Mapping-Drive.md        [COMPLETION] §5-§7
    Lines:  ~1,200L → ~2,000L (+800L)
    Công việc:
    - §5: Education design implications
      (+M1-M4: teaching aligned with firing modes)
      (+Sat: course design for satiation prevention)
      Cross-ref: Education-Mechanism.md, Expansion-Saturation-Crisis.md
    - §6: Cosmic loop — mapping-drive across scales
      (+BA: bond architecture at scale)
      (+RS: mapping sustainability)
      (+BS: by-product match at scale)
    - §7: Honest assessment + open questions
      Confidence levels, falsifiable predictions, limitations
    Version: v1.0 → v2.0 [COMPLETION]
```

### Phase F: Verify + Index Update (1 session)

```
F1. File-Index + Verify
    Công việc:
    - Core-Deep-Dive/01-File-Index.md: update versions cho ~25 files
    - Research/01-File-Index.md: check nếu cần update
    - Cross-ref spot-check: verify new refs point to correct files
    - Terminology consistency check
    - DMD v2.0 verify
```

---

## 5. SESSION SUMMARY TABLE

| Session | Files | Mức độ | ~Lines added | Concepts chính |
|---------|-------|--------|-------------|---------------|
| A1 | Body-Base.md | MODERATE | ~200 | EA, SE, BA, HwS, BS, RS, RPE, EC |
| A2 | Chunk.md | MODERATE | ~200 | EA, EC, BA, RS, BS, RPE, SE |
| B1 | Drive + Novelty + Threat | LIGHT | ~150 | SE, EA, Sat, PFC-B, BA |
| B2 | Status + Meaning | LIGHT-MOD | ~160 | EA, HwS, BS, M1-M4, BA, RS, RPE |
| B3 | Gratitude + Obligation + Protect | LIGHT | ~150 | BA, BS, RS, EA, HwS, M1-M4 |
| B4 | Autonomy + Auto-Hw + Liking-Wanting | LIGHT-MOD | ~180 | EA, SE, HwS, BA, Sat |
| C1 | Domain + Conflict + Knowledge-Flow | LIGHT | ~180 | SE, EA, PFC-B, Sat, HwS |
| C2 | Discovery-vs-Exp + Emergent-Pat | LIGHT | ~110 | SE, M1-M4, Sat, BA, BS, RS |
| D1 | IBM + WBK + Neural-Arch | MODERATE | ~290 | ALL refs, SE, HwS, EA, Sat |
| D2 | Coll-Purpose + Comp-Floor + CAD | LIGHT | ~140 | BA, RS, BS, EA, HwS |
| E1 | DMD §2-§4 | COMPLETION | ~800 | SE, Sat, PFC-B, EA, HwS, BA, M1-M4 |
| E2 | DMD §5-§7 | COMPLETION | ~800 | M1-M4, Sat, BA, RS, BS |
| F1 | File-Index + Verify | VERIFY | ~100 | — |
| | **TỔNG** | | **~3,460L** | |

---

## 6. DEPENDENCIES

```
Phase A (overview) ← không phụ thuộc gì
Phase B (observation) ← không phụ thuộc Phase A
Phase C (domain) ← không phụ thuộc Phase A/B
Phase D (mechanism + collective) ← không phụ thuộc Phase A/B/C
Phase E (DMD completion) ← C1 nên làm trước (Domain.md context)
Phase F (verify) ← tất cả Phase A-E phải xong
```

Các Phase A-D có thể làm THEO BẤT KỲ THỨ TỰ NÀO.
Thứ tự đề xuất (A→B→C→D→E→F) là logical flow, không phải dependency.

---

## 7. FILES KHÔNG CẦN LÀM (đã xác nhận OK)

### Đã update trong 28-session plan:
Connection v5.0, Empathy v4.0, Body-Coupling v3.0, Boredom v2.0, Love-Romantic v3.0,
Love-Unified v2.0, Background-Pattern v2.0, GDP v1.1, Agent-Mechanism v2.1,
Coordination-Node v1.2, Collective-Body v2.1, Imagine-Final v3.0, SPM v3.1,
BPGR v1.4, VP v3.0, + 11 NEW files (PFC-Ops, SE, EC, EA, EAE, EAC, BA, RS, BS, GBN, RPE, PFC-Label)

### Self-contained / không cần cascade:
- Body-Feedback DRAFTs (01, 02, 04): working documents, complementary to v2.0 files
- Feeling/ files (7 files): substantive, recently maintained, self-contained
- Schema/ files (4 files): foundational definitions, self-contained
- Melody Lens/ files (4 files): v2.0, self-contained lens
- Clarification/ files (4 files): factual corrections, ít affected
- Chunk-Internal-Processing (9 files): v1.0, self-contained analysis
- Chunk-External-Development (3 files + 5 Language): v1.0, self-contained
- Child-Chunk-Development (22 files): v7.8 aligned, separate project
- Body-Feedback v2.0 files (BF, BFM, BFL, GD, RSA, RC, AS): recently updated
- Health-Conditions (10 files): đã qua Drill-Reverse Propagation
- Meta-Impact (3 files): v2.1-v2.2, recently updated
- Education Research (7 files): có plan riêng (Education App Restructure)
- Applications (8 files): có plan riêng
- Birth-Rate-Decline (8 files): standalone research
- PFC files đã OK: Logic-Feeling v2.0, LFB v2.1, PFC-Function v1.2, PFC-Hw v1.1,
  PFC-Config v1.1, Attention-Spectrum v2.1, Imagine-Final-Eval v1.2, SAL v1.0
- Core-Hardware v1.0, Core-Software v1.0: overview files, recent (2026-05-10)
- Other Research: Climate-Cognition, Fidgeting, Relativity, Self-Created-Threat,
  Sensitivity, Money-Analysis, AI-Self-Model, Human-AI-Future, Innovation-Geography,
  Social-Calibration, Uncanny-Valley, Idol, Melody-Tech-Overview, Religion,
  Collective-Schema-Pressure, OCD-Analysis, Addiction-Analysis

### Special cases — DEFERRED:
- AI-Schema-Detection-update-draft.md: planning outline, chờ collective files mature
- PFC-Hold-Dimensions.md v1.0: optional enrichment, không urgent
- Imagination.md v1.0: overview for Imagination/, self-contained
- PFC-Development.md v1.0: self-contained development guide
- 09-Learning-Cycle.md: self-contained, formal level
- 99-Master-Synthesis.md v1.0: integration hub cho Chunk-Analysis drills

---

## 8. PROGRESS TRACKING

```
Phase A: Core Overview
✅ A1. Body-Base.md              v3.1 → v3.2  [MODERATE] — DONE 2026-05-23 (+146L)
✅ A2. Chunk.md                  v2.2 → v2.3  [MODERATE] — DONE 2026-05-23 (+55L)

Phase B: Observation Cascade
✅ B1. Drive + Novelty + Threat  3 files      [LIGHT] — DONE 2026-05-23 (+110L)
✅ B2. Status + Meaning          2 files      [LIGHT-MODERATE] — DONE 2026-05-23 (+117L)
✅ B3. Gratitude + Obligation + Protect  3 files  [LIGHT] — DONE 2026-05-23 (+102L)
✅ B4. Autonomy + Auto-Hw + LW  3 files      [LIGHT-MODERATE] — DONE 2026-05-23 (+102L)

Phase C: Domain Cascade
✅ C1. Domain + Conflict + K-Flow  3 files    [LIGHT] — DONE 2026-05-23 (+186L, +YAML headers)
✅ C2. DvE + Emergent-Patterns   2 files      [LIGHT] — DONE 2026-05-23 (+124L, +YAML headers)

Phase D: Mechanism + Collective
✅ D1. IBM + WBK + Neural-Arch   3 files      [MODERATE] — DONE 2026-05-23 (+69L)
✅ D2. CP + CF + CAD             3 files      [LIGHT] — DONE 2026-05-23 (+95L)

Phase E: DMD Concept Cascade (REFRAMED — file already 3,433L complete)
✅ E1-E3. DMD v1.0 → v2.0        1 file       [MODERATE REFINE] — DONE 2026-05-23 (+233L)
    NOTE: Plan originally assumed DMD had only §0-§1 (~400L).
    Actual: §0-§10 complete (3,433L). Reframed to CONCEPT CASCADE:
    - YAML header standardized + version v2.0
    - 7 concept notes added (§1.7, §2.1-Sat, §2.2-PFC/M1-M4, §2.3-EC,
      §2.4-SE, §3-RS/EA, §4-Sat/EA, §5-BA/RPE, §6-BS/RS, §7-mapping)
    - §10 cross-ref overhaul (all old file names → current)
    - 5 stale references fixed (PFC-Analysis, Reward-Dual-System, etc.)
    - Footer updated v1.0 → v2.0

Phase F: Verify
✅ F1. File-Index + Verify       3 index files [VERIFY] — DONE 2026-05-23
    - Core-Deep-Dive/01-File-Index.md: 13 entries updated (BB v3.2, Chunk v2.3,
      WBK v1.2, IBM v1.1, NA v1.1, CP v1.2, CF v2.1, CAD v1.2,
      Domain v1.0, CD v1.1, KF v1.0, DvE v1.0, EP v1.2, DMD v2.0)
    - Header line updated with cascade summary
    - Research/01-File-Index.md: checked, no updates needed
    - Applications/01-File-Index.md: checked, no updates needed

TOTAL: 27 files + 1 index, 12 sessions
Done:  12/12 ✅✅ ALL COMPLETE
```

---

## 9. SO SÁNH VỚI PLAN TRƯỚC

| | 28-Session Plan | Cascade Refine Plan |
|---|----------------|-------------------|
| Scope | 18 drill files → framework | Cascade concepts → foundational files |
| Files | ~130 touched | ~27 files |
| Sessions | 28 | 13 |
| New content | ~35,000L | ~3,500L |
| Work type | NEW + REWRITE + TÁCH | REFINE + 1 COMPLETION |
| Complexity | High (create new content) | Medium (integrate existing concepts) |
| Risk | Medium (new content quality) | Low (adding cross-refs to solid files) |
