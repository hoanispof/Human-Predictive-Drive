# Plan: Body-Feedback.md v3.0 REWRITE

> **Mục tiêu**: Rewrite Body-Feedback.md từ v2.0a → v3.0.
> Entry point cho Body-Feedback/ folder — phản ánh chính xác trạng thái hiện tại
> (14 files, ~23,900L) thay vì trạng thái cũ (10 files, ~16,500L).
>
> **Nguyên tắc**: Chậm mà chắc. Chất lượng nội dung.
> **Ngày tạo plan**: 2026-05-24.

---

## §0 — TẠI SAO CẦN REWRITE (không chỉ refine)

### A. File listing SAI (factual)

```
v2.0a ghi:   10 content files, ~16,500L
Thực tế:     14 content files, ~23,889L

4 FILES THIẾU HOÀN TOÀN:
  Gap-Body-Need.md         (1,388L) — 3 Satiation, ENGINE/ROAD/VEHICLE, 5-Parameter
  Gap-Distribution-Profile.md (2,370L) — per-person aggregate, 4 trục, 4 tầng
  Hidden-Quality-Perception.md (1,738L) — Expert + Leader, Dunning-Kruger
  Action-Space.md           (1,729L) — supply side, DEMAND × SUPPLY

Tổng thiếu: ~7,225L nội dung KHÔNG ĐƯỢC acknowledge.

Drill files path SAI:
  v2.0a ghi:  01-Foundation.md (root level)
  Thực tế:    Drill-Body-Feedback/01-Foundation.md (subfolder)
```

### B. Cấu trúc lạc hậu (structural)

```
v2.0a organize NỘI DUNG theo drill file structure (01→04):
  §2-§3: từ 01-Foundation
  §4:    từ 01 + Mechanism
  §5:    từ 02-Dissonance
  §6:    từ 03-Reward
  §7:    từ 03-Reward (cases)
  §8:    từ 02-Dissonance (trauma/hedonic)

KHÔNG organize theo mechanism hierarchy hiện tại:
  Hardware → Signal Generation → Signal Architecture → Gap System → Aggregate → PFC

§7 Cases (~100L) + §8 Trauma/Hedonic (~100L) = ~200L case details
  → Chiếm ~22% synthesis file cho content thuộc drill files
```

### C. Post-drill concepts thiếu

```
❌ 3 Satiation Profiles (Cyclic/Tonic/Generative)
❌ ENGINE/ROAD/VEHICLE architecture
❌ 5-Parameter per-gap model
❌ DEMAND × SUPPLY behavioral prediction (4 quadrants)
❌ Gap Distribution 4 trục + 4 tầng formation
❌ Hidden Quality Perception (2 types, Dunning-Kruger)
❌ Full pipeline visualization (hardware → collective)
❌ Compiled/Fresh deeper integration (chỉ mention ngắn)
```

### D. Cái gì VẪN ĐÚNG (giữ lại)

```
✅ §1.3 Compilable Architecture framing
✅ §2   Dual-Pull Architecture
✅ §3   Interface Loop 6-Step
✅ §4   Chunk Dynamics 2×3 summary
✅ §5   3 Genuine Discomfort Sources
✅ §6   H10 v3 + Evaluative/Direct-State × H10
✅ §9   Absorbed Content Map (concept hữu ích)
✅ §10  Research citations (vẫn valid)
```

---

## §1 — CẤU TRÚC v3.0

### Target: ~1,000-1,200L (so với v2.0a 894L)

```
Tăng ~20-30% vì cover 14 files thay vì 10.
Nhưng KHÔNG tăng nhiều vì TRIM case details.
```

### Section-by-section design

```
┌──────────────────────────────────────────────────────────────────┐
│ §0 — CORE CLAIMS + POSITION (~50L)                               │
│                                                                    │
│   5 core claims (v3.0 updated):                                   │
│   ① Body signal = f(5 preconditions H10) on interface loop        │
│   ② Body-feedback arises from 2 sources × 3 dynamics → Body-Need │
│   ③ Reward has 2 types (Evaluative/Direct-State) × 5 profiles     │
│   ④ Gap has DIRECTION + 3 SATIATION PROFILES + DISTRIBUTION      │
│   ⑤ Behavior = f(Gap-Distribution DEMAND × Action-Space SUPPLY)  │
│                                                                    │
│   + Position in framework (Body-Base/ entry point)                │
│   + v2.0a → v3.0 changelog summary                               │
│                                                                    │
│   SOURCE: New synthesis. Claims ①②③ từ v2.0a, ④⑤ NEW.           │
├──────────────────────────────────────────────────────────────────┤
│ §1 — FOLDER OVERVIEW + READING GUIDE (~180L)                     │
│                                                                    │
│   §1.1 — File listing (14 files, actual line counts)             │
│     Cấu trúc ĐÚNG:                                               │
│       Body-Feedback/                                              │
│       ├── Body-Feedback.md           (THIS FILE, entry point)     │
│       ├── VOCABULARY:                                             │
│       │   └── Body-Feedback-Label.md (1,119L) v2.0               │
│       ├── MECHANISM:                                              │
│       │   └── Body-Feedback-Mechanism.md (1,519L) v2.0           │
│       ├── GAP SYSTEM:                                 ← NEW TIER │
│       │   ├── Gap-Direction.md       (2,681L) v2.0               │
│       │   ├── Gap-Body-Need.md       (1,388L) v1.0  ← NEW FILE  │
│       │   └── Gap-Distribution-Profile.md (2,370L) v1.1 ← NEW   │
│       ├── REWARD ARCHITECTURE:                                    │
│       │   ├── Reward-Signal-Architecture.md (1,987L) v2.0        │
│       │   └── Reward-Calibration.md  (1,356L) v1.1               │
│       ├── AGGREGATE OBSERVATION:                      ← NEW TIER │
│       │   ├── Action-Space.md        (1,729L) v1.0  ← NEW FILE  │
│       │   └── Hidden-Quality-Perception.md (1,738L) v1.0 ← NEW  │
│       ├── CASE ANALYSES:                                          │
│       │   └── Drill-Body-Feedback/                   ← SUBFOLDER │
│       │       ├── 01-Foundation.md   (1,126L)                    │
│       │       ├── 02-Dissonance.md   (1,846L)                    │
│       │       ├── 03-Reward.md       (2,280L)                    │
│       │       └── 04-Integration.md  (1,856L)                    │
│       └── backup/                                                 │
│                                                                    │
│       FOLDER TOTAL: 14 content files, ~23,889L                    │
│                                                                    │
│   §1.2 — 4-Tier Reading Guide                                    │
│     TIER 1 VOCABULARY+ENTRY (~2,013L): This file + Label          │
│     TIER 2 MECHANISM+ARCHITECTURE (~7,575L):                      │
│       Mechanism + Gap-Direction + Gap-Body-Need +                 │
│       Reward-Signal-Architecture                                  │
│     TIER 3 OBSERVATION+AGGREGATE (~7,193L):                       │
│       Reward-Calibration + Gap-Distribution-Profile +             │
│       Action-Space + Hidden-Quality-Perception                    │
│     TIER 4 CASES (~7,108L):                                      │
│       Drill-Body-Feedback/ 01-04                                  │
│                                                                    │
│   §1.3 — Compilable Architecture: WHY folder needs 14 files      │
│     KEPT from v2.0a §1.3, CONDENSED (remove redundancy with §3)  │
│                                                                    │
│   SOURCE: §1.1 NEW (14-file listing). §1.2 RESTRUCTURED          │
│   (3-tier → 4-tier). §1.3 CONDENSED from v2.0a.                  │
├──────────────────────────────────────────────────────────────────┤
│ §2 — ⭐ FULL PIPELINE VISUALIZATION (~100L)          ← ALL NEW   │
│                                                                    │
│   Hardware → Signal → Evaluate → Aggregate → PFC → Inter-Body    │
│                                                                    │
│   LAYER 1: HARDWARE FOUNDATION                                    │
│     3 foundations (General-Purpose Reward + Compilation + Social)  │
│     → Compilable Architecture                                     │
│     Ref: Inter-Body-Mechanism.md §1, Body-Base.md §1              │
│                                                                    │
│   LAYER 2: SIGNAL GENERATION                                     │
│     2 sources (Sensory-Driven / Pattern-Driven)                   │
│     × 3 dynamics (Chunk-Shift / Chunk-Miss / Chunk-Gap)           │
│     + Compound → Body-Need aggregate                              │
│     Ref: Body-Feedback-Mechanism.md v2.0                          │
│                                                                    │
│   LAYER 3: SIGNAL ARCHITECTURE                                   │
│     Evaluative/Direct-State × E₀→E₃ × 5 Profiles                │
│     H10 5 preconditions → signal fire/not fire                    │
│     Ref: Reward-Signal-Architecture.md v2.0, 03-Reward.md        │
│                                                                    │
│   LAYER 4: GAP SYSTEM                                             │
│     Gap Direction = f(surrounding chunks)                         │
│     3 Satiation Profiles (Cyclic/Tonic/Generative)               │
│     Gap Distribution = per-person aggregate landscape             │
│     Ref: Gap-Direction, Gap-Body-Need, Gap-Distribution-Profile   │
│                                                                    │
│   LAYER 5: AGGREGATE OBSERVATION                                  │
│     Gap-Distribution = DEMAND ("muốn gì")                        │
│     Action-Space = SUPPLY ("có thể gì")                          │
│     Behavior = f(DEMAND × SUPPLY)                                 │
│     Reward Calibration = Goldilocks per-gap                       │
│     Hidden Quality = compilation depth → quality visibility       │
│     Ref: Action-Space, Gap-Distribution-Profile,                  │
│          Reward-Calibration, Hidden-Quality-Perception             │
│                                                                    │
│   LAYER 6: PFC OBSERVATION + INTER-BODY                           │
│     Feeling = PFC observation of body-feedback (7-layer)          │
│     Body-feedback (mechanism) ≠ Feeling (PFC observation)         │
│     Inter-body: by-product match, Entity-Compiled, 5-Channel     │
│     Ref: Feeling.md, Inter-Body-Mechanism.md, Body-Coupling.md   │
│                                                                    │
│   Diagram: ASCII pipeline flow showing all 6 layers              │
│                                                                    │
│   SOURCE: ALL NEW. Synthesis từ phân tích tổng thể 2026-05-24.   │
├──────────────────────────────────────────────────────────────────┤
│ §3 — DUAL-PULL + INTERFACE LOOP (~120L)               ← KEPT    │
│                                                                    │
│   §3.1 — Dual-Pull Architecture                                  │
│     CONDENSED từ v2.0a §2 (~75L → ~60L)                          │
│     Hardware Pull (bảo thủ) × Domain Pull (adapt)                │
│     + Compiled/Fresh connection (v2.0a đã có)                    │
│     + "Melody hay" 4 criteria (pointer to 01-Foundation)          │
│                                                                    │
│   §3.2 — Interface Loop 6-Step                                   │
│     CONDENSED từ v2.0a §3 (~55L → ~40L)                          │
│     6-step diagram KEPT (core contribution)                       │
│     + Domain Reality = Final Arbiter note                         │
│     + Relationship với 8-step micro (Feeling-Mechanism-Deep)      │
│     CẮT: chi tiết giải thích từng step (đã có ở 01-Foundation)   │
│                                                                    │
│   §3.3 — 3 Genuine Discomfort Sources                             │
│     CONDENSED từ v2.0a §5 (~70L → ~50L)                          │
│     ① Nociception ② Mismatch ③ Recalibration                    │
│     + "Cortisol KHÔNG GÂY ĐAU" (core reframe)                   │
│     + Treatment implication (fix mismatch, not reduce cortisol)   │
│     CẮT: research detail (đã có ở 02-Dissonance §3)             │
│                                                                    │
│   SOURCE: CONDENSED from v2.0a §2+§3+§5.                        │
│   Gộp 3 sections unique contributions thành 1 section.            │
│   Giữ core insight, cắt detail đã có ở drill files.              │
├──────────────────────────────────────────────────────────────────┤
│ §4 — SIGNAL GENERATION + BODY-NEED (~100L)            ← KEPT    │
│                                                                    │
│   CONDENSED từ v2.0a §4 (~100L → ~80L)                           │
│   4 trục orthogonal: Direction × Magnitude × Source × Dynamics   │
│   2 nguồn: Sensory-Driven / Pattern-Driven (bảng so sánh giữ)   │
│   3 dynamics: Chunk-Shift / Chunk-Miss / Chunk-Gap               │
│   Compound mechanism (100k example giữ — iconic)                 │
│   Quality Baseline Shift (SNC reference)                         │
│   + Body-Need = aggregate output (v2.0a đã có, giữ)             │
│   + Body-Need 7 properties summary (pointer to Mechanism §1.4)   │
│   + Complexity Spectrum (Simple→Social→Meta) pointer             │
│                                                                    │
│   THÊM v3.0:                                                     │
│   + Gap → Miss transition qua Imagine-Final (pointer to §3.3c)  │
│   + Gap decomposition mini-arc (pointer to §3.3d)                │
│                                                                    │
│   SOURCE: CONDENSED from v2.0a §4 + minor additions from         │
│   Body-Feedback-Mechanism v2.0 §1 + §3.3c-d.                    │
├──────────────────────────────────────────────────────────────────┤
│ §5 — SIGNAL ARCHITECTURE + H10 (~120L)                ← KEPT    │
│                                                                    │
│   §5.1 — Evaluative/Direct-State (summary)                      │
│     Core distinction table (Evaluative vs Direct-State)          │
│     E₀→E₃ gradient mention                                       │
│     5 Reward Profiles list (Sensory/Coherence/Social/Relief/     │
│     Mastery)                                                      │
│     Evaluative Gates Direct-State mention                        │
│     Pointer: Reward-Signal-Architecture.md v2.0 for full detail  │
│     ~50L                                                          │
│                                                                    │
│   §5.2 — H10 Body Signal Precondition Hypothesis                │
│     CONDENSED từ v2.0a §6 (~120L → ~70L)                        │
│     5-precondition table KEPT (definitive — this is the best     │
│     single-table summary in the framework)                        │
│     + H10 × Evaluative/Direct-State mapping (v2.0a đã có, giữ)  │
│     + H10 × 2-Layer interpretation (v2.0a đã có)                │
│     + H10 PREDICTS list (condensed from 8 → 5 key predictions)  │
│     CẮT: research citation detail (pointer to 03-Reward)        │
│                                                                    │
│   SOURCE: §5.1 NEW synthesis. §5.2 CONDENSED from v2.0a §6.     │
├──────────────────────────────────────────────────────────────────┤
│ §6 — GAP SYSTEM (~120L)                               ← ALL NEW │
│                                                                    │
│   §6.1 — Gap Direction summary (~30L)                            │
│     Gap direction = f(surrounding chunk network structure)        │
│     "Chưa biết = không có gap" (foundational principle)          │
│     Reward = DIRECTION MATCH quality                             │
│     2-layer model: signal mechanism × direction content          │
│     By-product match connection (inter-body)                     │
│     Pointer: Gap-Direction.md v2.0 for full detail               │
│                                                                    │
│   §6.2 — 3 Satiation Profiles summary (~30L)                    │
│     Cyclic: fill → off → return (hunger, safety)                 │
│     Tonic: fill ongoing → habituate chậm (touch, comfort)        │
│     Generative: fill → CREATE new gaps → perpetual (curiosity)   │
│     + transitions + compounds pointer                            │
│     + 5-Parameter per-gap model pointer                          │
│     + ENGINE/ROAD/VEHICLE architecture pointer                   │
│     Pointer: Gap-Body-Need.md v1.0 for full detail               │
│                                                                    │
│   §6.3 — Gap Distribution Profile summary (~30L)                │
│     Per-person gap landscape (4 trục):                           │
│       ① Domain Center × ② Origin Balance × ③ Depth × ④ Stability│
│     4-tầng formation: Collective Arc → Schemas → Family → Hw     │
│     Resonance prediction: overlap → by-product match probability │
│     Pointer: Gap-Distribution-Profile.md v1.1 for full detail    │
│                                                                    │
│   §6.4 — Behavioral Prediction summary (~30L)                   │
│     DEMAND = Gap-Distribution ("muốn gì")                        │
│     SUPPLY = Action-Space ("có thể gì")                          │
│     Behavior = f(DEMAND × SUPPLY)                                │
│     4 quadrants: Active Pursuit / Frustration / Drift / Simple   │
│     Pointer: Action-Space.md v1.0 for full detail                │
│                                                                    │
│   SOURCE: ALL NEW. Synthesis từ 3 new files.                     │
├──────────────────────────────────────────────────────────────────┤
│ §7 — QUALITY + CALIBRATION (~80L)                     ← ALL NEW │
│                                                                    │
│   §7.1 — Reward Calibration summary (~40L)                      │
│     Goldilocks per-gap: 3 zones (Under/Match/Over)              │
│     6 over-reward mechanisms list                                │
│     Dynamic equilibrium: KHÔNG THỂ prescribe                    │
│     Pointer: Reward-Calibration.md v1.1 for full detail          │
│                                                                    │
│   §7.2 — Hidden Quality Perception summary (~40L)               │
│     Core: "chưa biết = không có gap" × quality                  │
│     2 types: Domain Expert + Leader/Coordinator                  │
│     Dunning-Kruger = meta-level application                      │
│     Copier vs Expert: "giống hệt" diverges over time            │
│     Pointer: Hidden-Quality-Perception.md v1.0 for full detail   │
│                                                                    │
│   SOURCE: ALL NEW. Synthesis từ 2 files.                         │
├──────────────────────────────────────────────────────────────────┤
│ §8 — CASE ANALYSES + SPECIAL MECHANISMS (~60L)        ← TRIMMED │
│                                                                    │
│   §8.1 — Case Pointers (thay vì full detail) (~30L)             │
│     Ô tô Paradox 5 scenarios → 03-Reward.md §5                  │
│     Van Gogh gradient → 03-Reward.md §6                          │
│     Schema Update Latency (C5) → 03-Reward.md §8                │
│     Effort-Proportional Reward → 03-Reward.md §4.7              │
│     Mini Dissonance is CONSTANT → 02-Dissonance.md §2.6         │
│     MỖI case = 1-2 dòng pointer, KHÔNG duplicate detail         │
│                                                                    │
│   §8.2 — Trauma Loop + Hedonic Trap pointers (~30L)             │
│     Trauma Loop 4-stage → 02-Dissonance.md §8                   │
│       KEY INSIGHT ONLY: PFC = Lawyer, body KHÔNG tin             │
│       + chronic cortisol → PFC damage → loop                    │
│     Hedonic Trap → 02-Dissonance.md §9                           │
│       KEY INSIGHT ONLY: schema maintenance cost → drift          │
│       + baseline adaptation → need MORE                          │
│                                                                    │
│   SOURCE: TRIMMED from v2.0a §7 (~100L) + §8 (~100L).           │
│   ~200L → ~60L. Key insights kept, detail → pointers.            │
├──────────────────────────────────────────────────────────────────┤
│ §9 — ABSORBED CONTENT MAP (~80L)                      ← KEPT    │
│                                                                    │
│   KEPT from v2.0a §9, UPDATED:                                   │
│   + Bảng "absorbed elsewhere" giữ nguyên (Feeling-Mechanism-Deep)│
│   + Bảng "unique to this folder" UPDATED:                        │
│     ADD: Gap-Body-Need unique contributions                      │
│     ADD: Action-Space unique contributions                       │
│     ADD: Hidden-Quality-Perception unique contributions          │
│     ADD: Gap-Distribution-Profile unique contributions           │
│                                                                    │
│   SOURCE: UPDATED from v2.0a §9.                                │
├──────────────────────────────────────────────────────────────────┤
│ §10 — HONEST ASSESSMENT + CROSS-REFERENCES (~150L)    ← UPDATED │
│                                                                    │
│   §10.1 — Confidence breakdown                                   │
│     🟢 KEPT from v2.0a (all still valid)                         │
│     🟡 UPDATED: add new framework synthesis claims:              │
│       + 3 Satiation Profiles taxonomy                            │
│       + ENGINE/ROAD/VEHICLE architecture                         │
│       + DEMAND × SUPPLY behavioral prediction                    │
│       + Hidden Quality = gap landscape consequence               │
│     🔴 KEPT from v2.0a (all still valid)                         │
│                                                                    │
│   §10.2 — Cross-references                                      │
│     FULL UPDATE for 14 files + versions                          │
│     + Gap-Body-Need.md v1.0                                      │
│     + Gap-Distribution-Profile.md v1.1                           │
│     + Action-Space.md v1.0                                       │
│     + Hidden-Quality-Perception.md v1.0                          │
│     + Drill-Body-Feedback/ subfolder path                        │
│     + Inter-Body-Mechanism.md v2.0 (version update)              │
│     + All other version updates from concept cascade             │
│                                                                    │
│   SOURCE: UPDATED from v2.0a §10.                                │
└──────────────────────────────────────────────────────────────────┘
```

### Line count estimates

```
§0  Core Claims + Position          ~50L
§1  Folder Overview + Reading Guide ~180L
§2  Full Pipeline Visualization     ~100L   ← NEW
§3  Dual-Pull + Loop + 3 Nguồn     ~120L   ← CONDENSED
§4  Signal Generation + Body-Need   ~100L   ← CONDENSED
§5  Signal Architecture + H10      ~120L   ← CONDENSED
§6  Gap System                     ~120L   ← NEW
§7  Quality + Calibration           ~80L   ← NEW
§8  Cases + Special Mechanisms      ~60L   ← TRIMMED
§9  Absorbed Content Map            ~80L   ← UPDATED
§10 Honest Assessment + Cross-Refs ~150L   ← UPDATED
                                  ─────
TOTAL ESTIMATE:                  ~1,160L

v2.0a hiện tại: 894L
Tăng: ~266L (~30%)
Lý do tăng: cover 14 files (thay vì 10) + pipeline visualization
Lý do KHÔNG tăng nhiều hơn: trim ~140L case details
```

---

## §2 — PHÂN BIỆT: GIỮ / MỚI / CẮT / CẬP NHẬT

### A. GIỮ (content đúng, cần condensed)

```
① Dual-Pull Architecture (v2.0a §2)
   → v3.0 §3.1. Condensed ~75L → ~60L.
   → CẮT: giải thích dài. GIỮ: diagram + key insight + Compiled/Fresh note.

② Interface Loop 6-Step (v2.0a §3)
   → v3.0 §3.2. Condensed ~55L → ~40L.
   → CẮT: step-by-step explanation. GIỮ: ASCII diagram + domain=arbiter.

③ Chunk Dynamics 2×3 + Body-Need (v2.0a §4)
   → v3.0 §4. Condensed ~100L → ~80L.
   → CẮT: research detail. GIỮ: taxonomy + compound example (100k).

④ 3 Genuine Discomfort Sources (v2.0a §5)
   → v3.0 §3.3. Condensed ~70L → ~50L.
   → CẮT: research evidence. GIỮ: 3 categories + "cortisol ≠ pain" reframe.

⑤ H10 5-Precondition table (v2.0a §6)
   → v3.0 §5.2. Condensed ~120L → ~70L.
   → CẮT: 8→5 predictions, citation detail. GIỮ: definitive table + mappings.

⑥ Absorbed Content Map (v2.0a §9)
   → v3.0 §9. Expanded for 4 new files.

⑦ Research citations (v2.0a §10)
   → v3.0 §10. Updated versions.

⑧ Compilable Architecture framing (v2.0a §1.3)
   → v3.0 §1.3. Condensed (remove overlap with §2 pipeline).
```

### B. MỚI (nội dung chưa có trong v2.0a)

```
① §2 Full Pipeline Visualization (~100L)
   6-layer ASCII diagram: Hardware → Signal → Evaluate → Aggregate → PFC → Inter-Body
   Mỗi layer: 2-3 dòng mô tả + pointer to file(s)
   = "Bức tranh toàn cảnh" mà reader CẦN NHẤT ở entry point

② §6 Gap System (~120L)
   §6.1 Gap Direction summary (từ Gap-Direction.md v2.0)
   §6.2 3 Satiation Profiles summary (từ Gap-Body-Need.md v1.0)
   §6.3 Gap Distribution Profile summary (từ Gap-Distribution-Profile.md v1.1)
   §6.4 Behavioral Prediction summary (từ Action-Space.md v1.0)

③ §7 Quality + Calibration (~80L)
   §7.1 Reward Calibration summary (từ Reward-Calibration.md v1.1)
   §7.2 Hidden Quality Perception summary (từ Hidden-Quality-Perception.md v1.0)

④ §5.1 Evaluative/Direct-State summary (~50L)
   Tổng hợp từ Reward-Signal-Architecture.md v2.0
   v2.0a chỉ mention trong H10 mapping, chưa có section riêng
```

### C. CẮT (content move to pointers)

```
① v2.0a §7 Unique Case Analyses (~100L → ~15L pointers)
   5 cases (Ô tô, Van Gogh, C5, Mini Dissonance, Effort)
   → Mỗi case = 1 dòng pointer thay vì full analysis
   → Detail vẫn ở 02-Dissonance.md + 03-Reward.md

② v2.0a §8 Trauma Loop + Hedonic Trap (~100L → ~30L key insights)
   → GIỮ key mechanism insights (PFC=Lawyer, maintenance cost)
   → CẮT detailed walkthrough → pointer to 02-Dissonance.md §8-§9

TỔNG CẮT: ~200L → ~45L (tiết kiệm ~155L cho nội dung mới)
```

### D. CẬP NHẬT (content đúng nhưng cần update)

```
① §1.1 File listing: 10 → 14 files, paths corrected
② §1.2 Reading guide: 3-tier → 4-tier
③ §9 Absorbed Content Map: add 4 new files' unique contributions
④ §10.1 Confidence: add new 🟡 claims
⑤ §10.2 Cross-refs: add 4 new files + update versions
⑥ Frontmatter: version, scope, dependencies, dates
```

---

## §3 — EXECUTION PHASES

### Phase 0: Backup (5 min)

```
① Copy Body-Feedback.md → backup/Body-Feedback-v2.0a-backup.md
② Verify backup readable
```

### Phase 1: Frontmatter + §0-§1 (30 min)

```
① Write v3.0 frontmatter (title, version, scope, dependencies updated)
② Write §0 Core Claims + Position (~50L)
③ Write §1.1 File listing (14 files, correct paths, line counts) (~80L)
④ Write §1.2 4-Tier Reading Guide (~70L)
⑤ Write §1.3 Compilable Architecture (condensed) (~30L)

QUALITY CHECK Phase 1:
  → Verify all 14 files listed with correct names + line counts
  → Verify Drill-Body-Feedback/ path correct
  → Verify 4-tier covers all 14 files
  → Verify line counts match actual (wc -l)
```

### Phase 2: §2 Pipeline (20 min)

```
① Write §2 Full Pipeline Visualization (~100L)
② ASCII diagram: 6 layers with file pointers

QUALITY CHECK Phase 2:
  → Verify every file in folder appears in at least 1 layer
  → Verify layer order makes mechanism sense
  → Verify pointers to correct file names + versions
```

### Phase 3: §3-§5 Core Content (40 min)

```
① Write §3.1 Dual-Pull (condensed from v2.0a §2)
② Write §3.2 Interface Loop (condensed from v2.0a §3)
③ Write §3.3 3 Nguồn (condensed from v2.0a §5)
④ Write §4 Signal Generation + Body-Need (condensed from v2.0a §4)
⑤ Write §5.1 Evaluative/Direct-State summary (NEW)
⑥ Write §5.2 H10 (condensed from v2.0a §6)

QUALITY CHECK Phase 3:
  → Verify Dual-Pull: hardware pull × domain pull clear
  → Verify Interface Loop: 6-step diagram intact
  → Verify 3 Nguồn: nociception/mismatch/recalibration + "cortisol ≠ pain"
  → Verify chunk dynamics: 2×3 + compound clear
  → Verify H10 table: 5 preconditions correct
  → Verify Evaluative/Direct-State: core distinction clear
  → Vocabulary check: Body-Feedback-Label v2.0 compliance
```

### Phase 4: §6-§7 New Content (30 min)

```
① Write §6.1 Gap Direction summary
② Write §6.2 3 Satiation Profiles summary
③ Write §6.3 Gap Distribution Profile summary
④ Write §6.4 Behavioral Prediction summary
⑤ Write §7.1 Reward Calibration summary
⑥ Write §7.2 Hidden Quality Perception summary

QUALITY CHECK Phase 4:
  → Verify Gap Direction: f(surrounding chunks) + "chưa biết = không có gap"
  → Verify 3 Satiation: Cyclic/Tonic/Generative definitions correct
  → Verify Gap Distribution: 4 trục listed correctly
  → Verify Action-Space: DEMAND × SUPPLY framework
  → Verify Reward Calibration: Goldilocks + 6 mechanisms
  → Verify Hidden Quality: core mechanism + 2 types
  → Cross-check: summaries match source files
```

### Phase 5: §8-§10 Closing (30 min)

```
① Write §8.1 Case pointers (trimmed from v2.0a §7)
② Write §8.2 Trauma + Hedonic pointers (trimmed from v2.0a §8)
③ Write §9 Absorbed Content Map (updated from v2.0a §9)
④ Write §10.1 Confidence breakdown (updated)
⑤ Write §10.2 Cross-references (full update for 14 files)
⑥ Write END summary block

QUALITY CHECK Phase 5:
  → Verify all case pointers have correct file + section references
  → Verify Absorbed map: 2 tables updated
  → Verify confidence: new 🟡 claims added
  → Verify cross-refs: all 14 files + correct versions
  → Verify END summary: reflects v3.0 content accurately
```

### Phase 6: Final Quality Review (20 min)

```
① Read entire v3.0 file top-to-bottom
② Check: does every file in folder appear somewhere?
③ Check: are all version numbers current?
④ Check: does pipeline (§2) match content sections (§3-§7)?
⑤ Check: vocabulary consistent with Body-Feedback-Label v2.0?
⑥ Check: frontmatter dependencies complete?
⑦ Check: no orphaned cross-references
⑧ Check: line count within target range (~1,000-1,200L)
⑨ Compare v2.0a → v3.0: nothing important lost?
⑩ Verify backup exists and is intact
```

---

## §4 — VOCABULARY COMPLIANCE (Body-Feedback-Label v2.0)

```
PHẢI DÙNG:
  "body-feedback" (mechanism) — KHÔNG dùng "cảm xúc", "feeling" cho mechanism
  "body-base reward" (general) — KHÔNG dùng "opioid confirm" (chỉ Evaluative)
  "dissonance" — KHÔNG dùng "stress", "discomfort" cho technical contexts
  "prediction-delta" — KHÔNG dùng "prediction error" (Schultz term, narrower)
  "Evaluative Reward" / "Direct-State Reward" — KHÔNG dùng reward types khác
  "Chunk-Shift / Chunk-Miss / Chunk-Gap" — 3 dynamics
  "Body-Need" — KHÔNG dùng "nhu cầu" (too vague)
  "Compiled / Fresh" — KHÔNG dùng "Logic / Feeling" cho mechanism description
  "By-product match" — KHÔNG abbreviate
  "Cyclic / Tonic / Generative" — 3 satiation profiles
  "Self-Pattern-Modeling" — full name (KHÔNG SPM)
  "By-Product-Gap-Resonance" — full name (KHÔNG BPGR)
  "Imagine-Final" — full name (KHÔNG IF, Imagine Final)

KHÔNG VIẾT TẮT concepts:
  Framework convention: 0 abbreviations.
  Exception: H10 (accepted as label, not abbreviation).
  Exception: E₀→E₃ (accepted as gradient notation).
  Exception: P1-P5 (H10 precondition numbering).
```

---

## §5 — CROSS-REFERENCE ACCURACY CHECK

```
FILES TO VERIFY VERSIONS (at rewrite time):

  Body-Feedback-Label.md        → verify current version (v2.0)
  Body-Feedback-Mechanism.md    → verify current version (v2.0)
  Gap-Direction.md              → verify current version (v2.0)
  Gap-Body-Need.md              → verify current version (v1.0)
  Gap-Distribution-Profile.md   → verify current version (v1.1)
  Reward-Signal-Architecture.md → verify current version (v2.0)
  Reward-Calibration.md         → verify current version (v1.1)
  Action-Space.md               → verify current version (v1.0)
  Hidden-Quality-Perception.md  → verify current version (v1.0)
  01-04 drill files             → verify versions in Drill-Body-Feedback/

EXTERNAL CROSS-REFS TO VERIFY:
  Inter-Body-Mechanism.md       → verify current version (v2.0)
  Body-Base.md                  → verify current version (v3.2)
  Feeling.md                    → verify current version
  Feeling-Mechanism-Deep.md     → verify current version
  Cortisol-Baseline.md          → verify current version (v2.0)
  Body-Coupling.md              → verify current version
  Valence-Propagation.md        → verify current version (v3.0)
  Self-Pattern-Modeling.md      → verify current version (v3.1)
```

---

## §6 — DEPENDENCIES: FILES CẦN ĐỌC TRƯỚC KHI REWRITE

```
MUST-READ (đã đọc trong session 2026-05-24):
  ✅ Body-Feedback.md v2.0a (full)
  ✅ Body-Feedback-Mechanism.md v2.0 (full)
  ✅ Gap-Direction.md v2.0 (§0-§1, ~300L)
  ✅ Gap-Body-Need.md v1.0 (§0-§3, ~300L)
  ✅ Gap-Distribution-Profile.md v1.1 (§0, ~200L)
  ✅ Hidden-Quality-Perception.md v1.0 (§0-§1, ~200L)
  ✅ Action-Space.md v1.0 (§0-§1, ~300L)
  ✅ Reward-Signal-Architecture.md v2.0 (§0-§2, ~400L)
  ✅ Reward-Calibration.md v1.1 (§0-§1, ~150L)
  ✅ Body-Base.md v3.2 (§0-§1, ~200L)
  ✅ Inter-Body-Mechanism.md v2.0 (§0-§1, ~200L)
  ✅ 01-Foundation.md (header, ~30L)

OPTIONAL (đọc nếu cần clarify during rewrite):
  □ Body-Feedback-Label.md v2.0 — nếu cần verify vocabulary
  □ Feeling.md — nếu cần verify PFC observation layer
  □ Cortisol-Baseline.md — nếu cần verify 3 nguồn + roles
```

---

## §7 — RISK + MITIGATION

```
RISK 1: Mất unique contributions khi condensed
  → MITIGATION: Checklist verify §3 giữ tất cả: Dual-Pull, Loop, 3 Nguồn.
  → Mỗi unique contribution PHẢI xuất hiện ở ít nhất 1 section.

RISK 2: New file summaries (§6-§7) inaccurate
  → MITIGATION: Cross-check mỗi summary vs source file §0 thesis.
  → KHÔNG paraphrase — extract core claims trực tiếp.

RISK 3: Pipeline (§2) không consistent với content sections (§3-§7)
  → MITIGATION: After Phase 2, verify mỗi layer trong pipeline
  → maps to ít nhất 1 content section.

RISK 4: Version numbers outdated at rewrite time
  → MITIGATION: Phase 6 checks ALL versions via file headers.

RISK 5: Vocabulary drift (dùng từ cũ thay vì Label v2.0)
  → MITIGATION: §4 checklist. Search file after rewrite cho violations.
```

---

## §8 — TIMELINE

```
Session chuẩn bị (session hiện tại 2026-05-24):
  ✅ Đọc + phân tích tất cả files liên quan
  ✅ Xác định gap giữa v2.0a và trạng thái hiện tại
  ✅ Viết plan chi tiết (file này)

Session rewrite (session tiếp theo):
  Phase 0: Backup                    ~5 min
  Phase 1: Frontmatter + §0-§1      ~30 min
  Phase 2: §2 Pipeline              ~20 min
  Phase 3: §3-§5 Core               ~40 min
  Phase 4: §6-§7 New                ~30 min
  Phase 5: §8-§10 Closing           ~30 min
  Phase 6: Final Review             ~20 min
                                    ─────────
  ESTIMATED TOTAL:                  ~175 min (~3 hours)

  Có thể chia thành 2 sub-sessions nếu cần:
    Sub-session A: Phase 0-3 (§0-§5, ~95 min)
    Sub-session B: Phase 4-6 (§6-§10 + review, ~80 min)
```

---

> **END OF PLAN**
>
> **Summary**: Body-Feedback.md v2.0a → v3.0 REWRITE.
> 14 files (từ 10), ~23,900L (từ ~16,500L).
> +Pipeline visualization, +Gap System 4 files, +Quality/Calibration 2 files.
> −Case details (~155L trimmed → pointers).
> Target: ~1,160L (từ 894L, +30%).
> 6 phases + quality checks.
> Vocabulary compliance: Body-Feedback-Label v2.0.
