# Plan: Generic Label Audit — Cross-File Only

**Ngày tạo**: 2026-05-31
**Nguyên tắc**: Chỉ sửa labels dùng CROSS-FILE (nhiều file, khác nghĩa). Labels local (1-2 file) → GIỮA NGUYÊN.
**Phương pháp**: Phân tích → Plan → Fix từng system → Verify.

---

## §1 — TỔNG QUAN COLLISION MAP

```
CROSS-FILE COLLISION = cùng label, KHÁC nghĩa, xuất hiện ở NHIỀU file.
→ Reader thấy "Mode 3" nhưng KHÔNG BIẾT là Valence hay PFC hay Schema.
→ Reader thấy "L2" nhưng KHÔNG BIẾT là Valence-Propagation hay Scale hay Ladder.
```

### 3 hệ thống CẦN SỬA (cross-file, collision thật sự)

| # | Label | Số hệ thống trùng | Files ảnh hưởng | Ưu tiên |
|---|-------|--------------------|-----------------|---------|
| 1 | **Mode 1-6** | 3 hệ thống cross-file | ~47 files | ⭐⭐⭐ URGENT |
| 2 | **L1/L2 (Valence-Propagation)** | collide với Ladder + Scale | ~30+ files | ⭐⭐⭐ LARGEST |
| 3 | **L1-L3 (By-Product-Scale)** | collide với VP + Ladder | ~8 files | ⭐⭐ |

### ĐÃ RESOLVED hoặc KHÔNG CẦN SỬA

| Label | Lý do giữ nguyên |
|-------|-------------------|
| H10 | ✅ Đã rename → Body-Feedback-Precondition (98 files). Chỉ 9 drill files giữ H10 gốc |
| H1-H12 | Hypothesis provenance labels — exempt per convention |
| NT1-NT7 | Chỉ trong Drill-Chunk/ (25 files). 0 leakage ra framework files |
| MTF1-MTF7 | Chỉ trong Religion.md. User decision: GIỮ NGUYÊN |
| P1-P5 | Context-specific (phases, preconditions, predictions). Không collision |
| L0-L4 PFC-Inference Ladder | Chủ yếu trong Drill-Chunk + Child-Dev (~15 files). Tự consistent, không collision cross-folder |
| L0/L1 Body-Base Substrate | Current framework labels. L0=Alive Threshold, L1=Body-Input. Ít collision vì context rõ |
| M1 Motor Cortex | Neuroscience standard (3 files) |
| M1-M4 Motor Development | Local trong Child-Dev drill (4 files) |
| M1-M4 Resonance Decline | ĐÃ reframe → "2 Forces + 1 Fuel + Gap Drift". Chỉ còn trong changelog |
| M1-M5 Micro Examples | Local 1 file (Anchor-Schema-Example.md) |
| M1-M4 Quote Meta-Insights | Local per file (3 files) |
| Tầng A/B | ✅ ĐÃ DONE → Tầng Hardware/Tầng PFC |
| F1/F2 (SPM) | ✅ ĐÃ DONE → Compiled/Fresh |
| S1/S2 Streams | ✅ ĐÃ DONE → Hardware-Stream/Modeling-Stream |
| Type A/B (Reward) | ✅ ĐÃ DONE → Evaluative/Direct-State |
| Type A/B/C (Compile) | ✅ ĐÃ DONE → Experience/Expertise/Trust |

---

## §2 — SYSTEM 1: MODE LABELS (⭐⭐⭐ URGENT)

### Vấn đề
"Mode 3" có ÍT NHẤT 3 nghĩa khác nhau cross-file:
- Valence: Mode 3 = Context-Trigger (entity absent, cue-triggered firing)
- PFC Drive: Mode 3 = Spinning (rumination, overthinking)
- Schema Override: KHÔNG có Mode 3 (chỉ Mode 1-2)

Body-Coupling.md dùng CẢ Valence Mode VÀ Self-Pattern-Modeling Modes. Empathy.md dùng CẢ Schema Mode VÀ Valence Mode. Collision thật sự trong cùng 1 file.

### 3 hệ thống cross-file

#### System A: Valence Firing Modes (20 files)
```
Mode 1 → Firing-Maintenance    (entity present, baseline valence)
Mode 2 → Firing-Chunk-Miss     (entity absent, acute pain/loss)
Mode 3 → Firing-Context-Trigger (entity absent, cue-triggered firing)
```
✅ CONFIRMED 2026-05-31: Full descriptive names. Source: EVD.md §4.

**Files**: Entity-Valence-Dynamics, Background-Pattern, Connection, Body-Coupling, Gap-Distribution-Profile, Love-Romantic, Love-Unified, Sound drill files, + ~12 more

#### System B: PFC Drive Modes (19 files)
```
Mode 1 → Drive-PFC-Absent     (no PFC engagement)
Mode 2 → Drive-PFC-Monitor    (passive awareness)
Mode 3 → Drive-PFC-Spinning   (rumination, overthinking)
Mode 4 → Drive-PFC-Resolve    (active problem-solving)
Mode 5 → Drive-PFC-Strategic  (long-term planning)
Mode 6 → Drive-PFC-Override   (forced suppression)
```
✅ CONFIRMED 2026-05-31: Full descriptive names. Source: Drive.md §2.

**Files**: Drive, PFC-Configuration, Boredom, Meaning, Body-Feedback-Mechanism, Human-AI-Future, Addiction-Analysis, Alcohol files, ADHD-Observation, Self-Created-Threat, Quote-Analysis files, + more

#### System C: Schema Override Modes (15 files)
```
Mode 1 → Schema-Pure-Trust    (zero modeling, 100% schema-driven)
Mode 2 → Schema-Imagined-Overlay (modeling overlay trên schema)
```
✅ CONFIRMED 2026-05-31: Full descriptive names. Source: Agent-Mechanism.md §10.

**Files**: Agent-Mechanism, Valence-Propagation, Empathy, Gratitude, Obligation, Anchor-Schema, Mirror-Neuron-Rejection, Uncanny-Valley, Drill files, + more

#### Local systems (SKIP — 1-2 files mỗi cái)
- Learning Modes (09-Learning-Cycle.md)
- Vague Detection Modes (04-Right-Wrong-Vague.md)
- Failure Modes (Feeling-Literacy-Training-Draft.md)
- Self-Pattern-Modeling Modes (Body-Coupling.md local)
- Music Perception Modes (Sound drill files)

### Scope ước tính (UPDATED 2026-05-31 — scan thực tế)
- System A: ~276 occ, ~20 files
- System B: ~65 occ, ~19 files
- System C: ~42 occ, ~15 files
- **Tổng Mode: ~383 occ, ~47 files**
- 100% MANUAL (collision trong cùng file)

---

## §3 — SYSTEM 2: L1/L2 VALENCE-PROPAGATION 2-LUỒNG (⭐⭐⭐ LARGEST)

### Vấn đề
L2 có 6 nghĩa khác nhau. 3 nghĩa cross-file tạo collision thật sự:
- L2 = Valence-Structural (Entity-compiled) — 30+ files, DOMINANT
- L2 = Scale-Hub (By-Product-Scale) — 8+ files
- L2 = Ladder-Pattern-match (PFC-Inference) — 15+ files

Agent-Mechanism.md dùng CẢ L2=Entity-compiled VÀ L2=Hub TRONG CÙNG FILE.

### Rename proposal — ✅ CONFIRMED 2026-05-31

#### Valence-Propagation 2-Luồng (11-13 files, ~796 occ)
```
L1 → Valence-Momentary   (Self-Pattern-Modeling-owned, per-episode)
L2 → Valence-Structural  (Entity-compiled, persistent, body-base extension)

Các compound: "L1 cost" → "Valence-Momentary cost", "L2 ceiling" → "Valence-Structural ceiling"
Formulas: "f(L1/L2)" → "f(Valence-Momentary/Valence-Structural)"
```

> User chọn Valence-Momentary/Valence-Structural thay vì Luồng 1/Luồng 2.
> English descriptive, rõ nghĩa hơn, consistent với framework naming convention.

### Scope ước tính (UPDATED 2026-05-31 — scan thực tế)
- **~796 occ, 11-13 production files**
- Top files: Love-Unified (281), Empathy (184), Body-Coupling (117), EVD (100), Love-Romantic (75)
- "Luồng 1/2" đã dùng 32 nơi, "2-luồng" 81 nơi
- Mixed auto/manual (cần phân biệt VP L1/L2 vs Body-Base L0/L1 vs Scale L1/L2/L3)

---

## §4 — SYSTEM 3: L1-L3 BY-PRODUCT-SCALE (⭐⭐)

### Rename proposal — ✅ CONFIRMED 2026-05-31
```
L1 / Level 1 → Scale-Pair         (oxytocin, 1-5 entities)
L2 / Level 2 → Scale-Hub          (serotonin, 20-150+)
L3 / Level 3 → Scale-Institutional (trust infrastructure, millions+)
```

### Files (8+)
By-Product-Scale, Agent-Mechanism, Collective, Coordination-Node, Core-Software, Religion, Connection-Education, Glossary

### Scope ước tính
- ~8 production files
- ~50-80 replacements
- Mostly auto (ít collision vì thường kèm context "Hub"/"Pair"/"Institutional")

---

## §5 — TIẾN TRÌNH ĐỀ XUẤT

### Thứ tự ưu tiên

```
Phase 1: System 3 — By-Product-Scale L1-L3 — ✅✅ COMPLETE
  → 10 files, ~85 repl. Verify: 0 old labels.

Phase 2: System 1A — Valence Firing Modes — ✅✅ COMPLETE
  → 9 files, ~106 repl. 3 collision files manual. Verify: 0 old labels.

Phase 3: System 1B — PFC Drive Modes — ✅✅ COMPLETE
  → 16 files, ~100 repl. 0 collision. Verify: 0 old labels.

Phase 4: System 1C — Schema Override Modes — ✅✅ COMPLETE
  → 13 files, ~65 repl. 0 collision. Verify: 0 old labels.

Phase 5: System 2 — Valence-Propagation L1/L2 — ✅✅ COMPLETE
  → ~34 files, ~900+ repl. 3-tier (manual+agent+straggler). Verify: 0 VP-specific L2.

Phase 6: Verify — ✅✅ COMPLETE
  → 5 Scale misses FIXED + all 5 systems verified clean
```

### Ước tính tổng (UPDATED 2026-05-31)
- ~7-10 sessions
- ~50+ files
- ~1,200+ replacements
- Quy trình: Refine file gốc → Propagate → Verify

---

## §6 — M1-M4 ENTITY-ACCESS (BORDERLINE)

```
M1 = Blind Mode, M2 = Tool-Mode, M3 = Override, M4 = Depleted
Chỉ 2 files (Entity-Access.md + Entity-Access-Calibration.md)
```

Collision với M1 Motor Cortex (neuroscience, 3 files) và M1-M4 Motor Development (drill, 4 files).
NHƯNG: context rất rõ (Entity-Access vs neuroscience) → collision risk THẤP.
**Recommend: SKIP** (2 files = gần local). User quyết định.

---

## §7 — PFC-INFERENCE LADDER L0-L4 (BORDERLINE)

```
L0=Reflex, L1=Post-hoc, L2=Pattern-match, L3=Deliberate, L4=Coordinated
15+ files, chủ yếu trong Drill-Chunk + Child-Dev + Core-Hardware
```

Collide với VP L1/L2 và Scale L1-L3.
NHƯNG: hầu hết nằm trong Drill-Chunk folder (self-contained).
Core-Hardware.md và Chunk.md là 2 file duy nhất ngoài drill dùng Ladder labels.

**Recommend: SỬA NẾU Phase 5 (VP L1/L2) được triển khai** — vì khi VP L1/L2 đổi tên, Ladder L0-L4 sẽ ít collision hơn. Nhưng nếu muốn triệt để: đổi thành Ladder-[Name].

---

## §8 — LOG

### 2026-05-31 — Session 2: Analysis + Confirm
- ✅ Scan thực tế: Scale ~80-100 occ, Mode ~383 occ, VP ~796 occ (tổng ~1,200+)
- ✅ User confirm ALL rename mappings:
  - Scale: L1→Scale-Pair, L2→Scale-Hub, L3→Scale-Institutional
  - Firing: Mode 1→Firing-Maintenance, Mode 2→Firing-Chunk-Miss, Mode 3→Firing-Context-Trigger
  - Drive: Mode 1-6 → Drive-PFC-[Absent/Monitor/Spinning/Resolve/Strategic/Override]
  - Schema: Mode 1→Schema-Pure-Trust, Mode 2→Schema-Imagined-Overlay
  - VP: L1→Valence-Momentary, L2→Valence-Structural
- ✅ Approach: 1 plan chung + refine file gốc trước → propagate
- NEXT: Phase 1 — Scale L1-L3 (By-Product-Scale.md gốc → propagate)

### 2026-05-31 — Phase 1: Scale L1-L3 — ✅✅ COMPLETE
- ✅ By-Product-Scale.md: ~50 "Level 1/2/3" + 2 "L1/L2/L3" → Scale-Pair/Scale-Hub/Scale-Institutional. Bảng box-drawing fixed (2 bảng).
- ✅ Core-Software.md: 3 lines fixed
- ✅ Religion.md: 3 lines fixed
- ✅ Agent-Mechanism.md: 4 lines fixed (bảng + hardware shift)
- ✅ Coordination-Node.md: ~20 occ fixed (bảng + evolution + hardware)
- ✅ Collective-Body.md: ~15 Scale-context occ fixed (2 bảng + changelog). VP L2 refs KEPT.
- ✅ Collective.md: 7 occ fixed (bảng + text + cross-ref)
- ✅ Connection-Education.md: 3 lines fixed
- ✅ 01-File-Index.md (Core): 3 lines fixed
- ✅ 00-Glossary.md: 1 line fixed
- Verify scan: 0 Scale "L1/L2/L3" hoặc "Level 1/2/3" trong production files
- TOTAL: ~10 files, ~85+ replacements
- NEXT: Phase 2 — Valence Firing Modes (refine EVD.md gốc → propagate)

### 2026-05-31 — Phase 2: Valence Firing Modes — ✅✅ COMPLETE
- ✅ Entity-Valence-Dynamics.md (SOURCE): ~26 refs. 3 definitions (MODE 1/2/3) + all references → Firing-Maintenance/Chunk-Miss/Context-Trigger.
- ✅ Background-Pattern.md: ~34 refs. §7.3+§9.3 full section renames. "Mode 2/3" compound → split. "3 MODES" → "3 FIRING MODES".
- ✅ Love-Romantic.md: ~23 refs. §10.3+§11.7. "MODE 1 MAINTENANCE" definitions + all plain refs. PFC Config Mode ①③④ (circled numbers) KEPT.
- ✅ Connection.md: ~11 refs. §3.3 definitions + all refs. "3 MODES" → "3 FIRING MODES".
- ✅ 02-Sound-Background-Pattern.md: 1 ref. "Mode 2 Chunk-Miss" → "Firing-Chunk-Miss".
- ✅ Gap-Distribution-Profile.md: 1 ref. "Mode 2" → "Firing-Chunk-Miss".
- ✅ Love-Unified.md (COLLISION): ~17 Valence Firing refs renamed. SPM Modes (14 refs: Mode 1=template, Mode 2=schema, Mode 3=effortful) KEPT.
- ✅ Empathy.md (COLLISION): ~8 Valence Firing refs renamed. Schema Override Mode 1/2 (3 refs) + SPM Failure Mode 1 (2 refs) KEPT.
- ✅ Body-Coupling.md (COLLISION): ~8 Valence Firing refs renamed. SPM Modes (5 refs) + Schema Override Mode 1/2 (1 ref) KEPT.
- Verify scan: 0 Valence Firing "Mode 1/2/3" remaining in production files
- ⚠️ FLAGGED: Core-Software.md line 866 — "3 Firing Modes: Tonic/Phasic/Compound" = WRONG (should be Maintenance/Chunk-Miss/Context-Trigger). Satiation Types ≠ Firing Modes.
- TOTAL: 9 files, ~106 replacements
- NEXT: Phase 3 — PFC Drive Modes (refine Drive.md gốc → propagate)

### 2026-05-31 — Phase 3: PFC Drive Modes — ✅✅ COMPLETE
- ✅ Drive.md (SOURCE): ~35 refs. 6 definition headers (═══), 2-axis diagram, summary table rebuilt, all inline refs. Mode 1-6 → Drive-PFC-[Absent/Monitor/Spinning/Resolve/Strategic/Override].
- ✅ PFC-Configuration.md: ~30 refs. §2 Drive participation lines (6x), §6 Compatibility Matrix table rebuilt, Natural Pairings (4x), Impossible Combinations (3x), Real-World Mapping table rebuilt. Cross-ref version updated.
- ✅ Meaning.md: 2 refs (Mode 3 → Drive-PFC-Spinning).
- ✅ Body-Feedback-Mechanism.md: 1 ref (Mode 5 → Drive-PFC-Strategic). PFC-Operations 2-Mode Engagement (line 1474) KEPT.
- ✅ Human-AI-Future.md: 3 refs (MODE 3→4 SHIFT header + 2 inline → Drive-PFC-Spinning/Resolve).
- ✅ Addiction-Analysis.md: 1 ref (Mode 5 → Drive-PFC-Strategic).
- ✅ Boredom.md: 3 refs (Mode 3 → Drive-PFC-Spinning). Version updated v1.1→v1.2.
- ✅ Work-Move-Fast-Break-Things.md: ~14 refs (Mode 3/4 → Drive-PFC-Spinning/Resolve).
- ✅ Work-Adversity-Fear-Cluster.md: 3 refs (Mode 3 → Drive-PFC-Spinning).
- ✅ Work-Journey-Destination-Cluster.md: 5 refs (Mode 3 → Drive-PFC-Spinning).
- ✅ Work-Goal-And-Why.md: 2 refs (Mode 3 → Drive-PFC-Spinning).
- ✅ Work-Stay-Hungry-Stay-Foolish.md: 3 refs (Mode 3 → Drive-PFC-Spinning).
- ✅ Alcohol-Brain-Mechanism.md: 1 ref (Mode 3 → Drive-PFC-Spinning).
- ✅ Alcohol-Vietnam-Generational.md: 2 refs (Mode 3 → Drive-PFC-Spinning).
- ✅ 10-Synthesis.md: PFC-Operations 2-Mode Enjoyment (lines 277-278) KEPT — local system.
- ✅ Self-Created-Threat.md: 1 ref (Mode 5 → Drive-PFC-Strategic, backup cross-ref).
- ✅ 01-File-Index.md: 1 Phase 2 leftover fixed (Mode 1 → Firing-Maintenance).
- NON-PFC-DRIVE systems KEPT unchanged:
  - Schema Override Mode 1/2: ~39 refs across 9 files (Agent-Mechanism, Empathy, Gratitude, Anchor-Schema, etc.)
  - PFC Configuration ①-⑥: ~12 refs across 3 files (ADHD, PFC-Operations, Music drills)
  - SPM Modes: ~14 refs across 3 files (Love-Unified, Body-Coupling, Connection)
  - Local systems: ~16 refs (Failure Modes, Entity-Access Modes, Learning Modes, Vague Detection Modes, Error Modes)
- Verify scan: 0 PFC Drive "Mode [1-6]" remaining in production files
- TOTAL: 16 files, ~100 replacements
- NEXT: Phase 4 — Schema Override Modes (refine Agent-Mechanism.md §10 gốc → propagate)

### 2026-05-31 — Phase 4: Schema Override Modes — ✅✅ COMPLETE
- ✅ Agent-Mechanism.md (SOURCE): ~50 refs. §10 section headers (§10.1/§10.2/§10.3), summary table (9 rows), inline definitions, examples, body-need feeder section, version notes. Pre-fixed compounds + redundancy, then replace_all. Mode 1→Schema-Pure-Trust, Mode 2→Schema-Imagined-Overlay.
- ✅ Empathy.md: 3 refs (§2.4 Schema Simulation mapping + 2 mode definitions).
- ✅ Gratitude.md: 2 refs (Schema Simulation Mode 1/2 → Schema-Pure-Trust/Imagined-Overlay).
- ✅ Valence-Propagation.md: 3 refs (Agent-Mechanism cross-refs, version updated v2.0→v2.1).
- ✅ Anchor-Schema.md: 1 ref (Schema override Mode 1/Mode 2 → Schema-Pure-Trust/Imagined-Overlay).
- ✅ Body-Coupling.md: 1 ref (Schema-agent Mode 1/2 → Schema-Pure-Trust/Imagined-Overlay).
- ✅ Obligation.md: 1 ref (§12.4 Mode 1/2 virtual agents).
- ✅ Mirror-Neuron-Rejection.md: 1 ref (Mode 1/2 religious agents).
- ✅ Uncanny-Valley.md: 3 refs (Mode 2 schema override + Mode 1 schema trust + table cell).
- ✅ Collective-Body.md: 1 ref (SCHEMA-AGENT MODE 1/2).
- ✅ Feeling-Sources-Draft.md: 1 ref (Mode 1: pure logic-as-schema).
- ✅ 00-Reading-Notes.md: 1 ref (Đức Mẹ Mode 1).
- ✅ 06-Theme-F-Logic-Feeling-Check.md: 1 ref (Đức Mẹ Mode 1).
- NON-Schema systems KEPT unchanged:
  - PFC-Operations 2-Mode Engagement: ~7 refs (local system, Mode 1=Flow, Mode 2=Analytical)
  - SPM Modes: ~14 refs across 3 files (Love-Unified, Body-Coupling, Connection)
  - SPM Failure Mode: ~4 refs (Empathy, Bond-Architecture)
- Verify scan: 0 Schema Override "Mode 1/2" remaining in production files
- TOTAL: 13 files, ~65 replacements
- NEXT: Phase 5 — VP L1/L2 (largest system, ~796 occ, 11-13 files)

### 2026-05-31 — Phase 5: VP L1/L2 — ✅✅ COMPLETE
Strategy: Read→analyze→pre-fix redundancy→replace_all L2 FIRST→L1→fix Body-Base back.
Collision types: VP L2 vs Body-Base L0+L1 (same file), VP L2 vs Ladder L0-L4 (Chunk.md).
Source file first (Entity-Valence-Dynamics.md) → propagate by tiers.

**TIER 1 — Manual (12 files):**
- ✅ Entity-Valence-Dynamics.md (SOURCE): 26 VM + 79 VS. 4 Body-Base L0+L1 preserved. 2 tables rebuilt.
- ✅ Love-Unified.md: 8 VM + 252 VS. 10 Body-Base L1 preserved. 6+ tables rebuilt/widened.
- ✅ Empathy.md: 109 VM + 133 VS. 4 Luồng definitions annotated.
- ✅ Body-Coupling.md (agent): 31 VM + 96 VS. 2 Body-Base L1 preserved. 5 file name refs preserved.
- ✅ Resonance-Per-Entity.md: comparison table rebuilt. 0 remaining.
- ✅ Connection.md: 27 repl (agent) + table fix (Val-Struct abbreviation corrected).
- ✅ Obligation.md (agent): 5 VM + 78 VS. 0 remaining.
- ✅ Love-Romantic.md (agent): 39 VM + 59 VS. 2 tables + 2 Luồng defs.
- ✅ Chunk.md: 1 targeted VP L2 edit. Ladder L2 (1037-1095) KEPT. Body-Base (1491) KEPT.
- ✅ Body-Base.md: 11 targeted VP L2 edits in §8. ALL L1 = Body-Base KEPT.
- ✅ Core-Software.md: 0 VP labels. Fixed Phase 2 leftover (Tonic/Phasic/Compound→Firing names).
- ✅ Imagine-Final-Evaluation.md: 0 VP labels. ALL = old layer system.

**TIER 2 — Agent batches (15 files):**
- ✅ Batch A: Idol-Phenomenon (18), Gratitude (13), Inter-Body-Mechanism (9), Religion (10). 1 Body-Base L1 preserved.
- ✅ Batch B: Agent-Mechanism (13), Self-Pattern-Modeling (7), Domain-Mapping-Drive (8), Addiction-Analysis (7). 2 Sustainability L1/L2 preserved.
- ✅ Batch C: Alzheimer (8), PFC-Function (3), Background-Pattern (2), Bond-Architecture (1), Entity-Access (5), OCD-Analysis (4). Feeling-Sources-Draft SKIPPED (Body-Base channels).

**TIER 3 — Stragglers caught by verification sweep (7 files):**
- ✅ Collective.md: 6 VP L2 → Valence-Structural
- ✅ Compile-Taxonomy.md: 4 VP L2 → Valence-Structural
- ✅ Social-Calibration.md: 1 VP L2 → Valence-Structural
- ✅ Reward-Signal-Architecture.md: 4 VP L1/L2 (cross-refs) → Valence-Momentary/Structural
- ✅ Connection-Education.md: 1 VP L2 → Valence-Structural
- ✅ Collective-Schema-Pressure.md: 1 VP L1 + 1 VP L2 → Valence-Momentary/Structural
- ✅ summary-paper-outline.md: 1 VP L2 → Valence-Structural
- ✅ 01-File-Index.md (Research): 2 VP L1/L2 (Idol desc + Money desc)

**Luồng definition annotations (5 files):**
- ✅ Empathy.md: Luồng 1/2 headers annotated (Valence-Momentary/Structural)
- ✅ Love-Romantic.md: Luồng 1/2 section headers annotated
- ✅ Love-Unified.md: Luồng 1/2 definitions annotated
- ✅ Body-Coupling.md: Luồng 1/2 definitions annotated
- ✅ Agent-Mechanism.md: Luồng 1/2 definitions annotated (dropped redundant descriptors)
- ✅ Self-Pattern-Modeling.md: Luồng annotations added + redundant "structural" dropped

**SKIPPED (non-VP L2 systems — verified correct):**
- Body-Base L0+L1: ~40+ files (substrate, nutrition, comfort, touch, presence — ALL preserved)
- Ladder L0-L4: ~20+ files (Child-Chunk-Development, Language-Structure-Analysis, Core-Hardware, Curriculum-Framework)
- Linguistics L1/L2: Compile-Type-Learning (first/second language)
- Scenario labels: Anchor-Schema-Example (L1=story, L2=startup)
- Intensity gradient: Cortisol-Baseline line 695 (L1/L2/L3 = proximity to body-base)
- Sustainability model: Agent-Mechanism §12.5 (L1=Proximity, L2=Duration)
- Confidence levels: ADHD blog (L1, L2 = uncertainty tiers)
- Old layer references: Self-Created-Threat, Birth-Rate-Decline files, Feeling-Research
- Case labels: Logic-Feeling-Failure-Examples (Case L1, Case L2)
- Depth levels: Education-System (L2 = EXPLAIN depth)
- File name references: "Drill-L2-Phenomenology-Emptiness.md" — preserved

**Verification:** Full grep `\bL2\b` → 237 files, ALL remaining = non-VP (backup, Ladder, Body-Base, other systems).
VP-specific patterns grep → 0 matches in production files.

- TOTAL: ~34 production files, ~900+ replacements

### 2026-05-31 — Phase 6: Final Verify — ✅✅ COMPLETE
Re-scan ALL 5 systems across production files.

**Sub-check 1: Scale L1-L3** — Found 5 MISSES from Phase 1:
- ✅ By-Product-Gap-Resonance.md: 6 "Level 1/2/3" → Scale-Pair/Hub/Institutional
- ✅ Love-Unified.md: 1 cross-ref + 8 §11.5 Scale references → Scale-Pair/Hub/Institutional
- ✅ Love-Romantic.md: 4 §4.3 Scale references → Scale-Pair/Hub/Institutional
- ✅ Body-Coupling.md: 10 §5.2 Scale references → Scale-Pair/Hub/Institutional
- ✅ 04-Sound-Social-Resonance.md: 1 Scale reference → Scale-Hub
All fixed. Non-Scale "Level 1/2/3" verified: Child-Dev parenting quality levels, education depth levels, math/language levels = all legitimate, KEPT.

**Sub-check 2: Valence Firing Modes** — CLEAN. 0 remaining "Mode [123]" in Firing context across all 9 renamed files.

**Sub-check 3: PFC Drive Modes** — CLEAN. 0 remaining "Mode [1-6]" in Drive context across all 16 renamed files.

**Sub-check 4: Schema Override Modes** — CLEAN. 0 remaining "Mode [12]" in Schema context across all 13 renamed files.

**Sub-check 5: VP L1/L2** — CLEAN (verified earlier this session). 0 VP-specific L2 patterns in production files.

**Remaining "Mode [1-6]" in production (62 files):** ALL verified = non-renamed systems:
- SPM Modes (Love-Unified, Body-Coupling, Connection)
- PFC-Operations 2-Mode Engagement (PFC-Operations, Music drills)
- SPM Failure Mode (Empathy, Bond-Architecture)
- Local systems (Status Modes, Learning Modes, Vague Detection Modes, Error Modes, Entity-Access Modes)

**GENERIC LABEL AUDIT — ALL 6 PHASES COMPLETE.**
Total: ~1,280+ replacements, ~87 production files, 5 systems renamed.
Plan CLOSED.
