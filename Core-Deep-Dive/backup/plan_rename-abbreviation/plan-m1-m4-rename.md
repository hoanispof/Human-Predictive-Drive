# Plan: M1-M4 Rename — M1-M4 → Compiled-Suppress / Habituation / Prediction-Completion / Entity-Saturation

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~40 active files, ~500 replacements (Resonance Decline system)
           + ~3 collision fixes (Entity Profile, Firing Modes, Motor Arcs)
Approach:  CLUSTER-BY-CLUSTER (Source Definition → Consumers → Collision Fixes)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\bM[1-4]\b" = 0 trong Resonance Decline context files
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 3 lý do chính

**① M1-M4 KHÔNG MANG NGHĨA**

```
  "M1 ACCELERATE M2+M3+M4" — ai biết M1 là gì?
  → Phải tra Bond-Architecture.md §4 mỗi lần gặp

  "Compiled-Suppress ACCELERATE Habituation+Prediction-Completion+Entity-Saturation"
  → Ngay lập tức hiểu: suppress drive riêng → 3 cơ chế kia tăng tốc
```

**② TRÙNG KÝ HIỆU VỚI ÍT NHẤT 4 HỆ THỐNG KHÁC**

```
  Framework hiện tại có ÍT NHẤT 5 hệ thống M-labels:

  ① RESONANCE DECLINE (Bond-Architecture §4):
     M1 = Compiled suppress gap riêng
     M2 = Habituation (Weber-Fechner)
     M3 = Prediction completion
     M4 = Entity-Compiled saturation
     → 40+ files, ~500 occ — PLAN NÀY RENAME

  ② ENTITY PROFILE PARAMETERS (Resonance-Per-Entity §3):
     M1 = Hardware subsidy level
     M2 = Compilation path
     M3 = Cost profile
     M4 = 2-tầng proportion
     M5 = 2-luồng proportion
     → 1 file, ~30 occ — COLLISION FIX

  ③ PFC FIRING MODES (Domain-Mapping-Drive v2.0):
     M1 = Structural/Tonic
     M2 = Current-Shift/Phasic
     M3 = Peak/Compound
     M4 = Cascade
     → 2 files, ~22 occ — ⚠️ ERROR: cross-ref Bond-Architecture M1-M4 SAI

  ④ MOTOR DEVELOPMENT EVENTS (Child-Chunk-Development arcs):
     M1 = Palmar grasp, M2 = Rooting, M3 = Hand-to-mouth, M4 = Reaching
     → 4+ files — MODALITY ARC CODE (V1/A1/M1/B1), SKIP

  ⑤ PFC DAMAGE MECHANISMS (02-Dissonance):
     M1 = Temporary recovery, M2 = Neural wear
     → 1 file — SEPARATE SCOPE
```

**③ TÊN THAY THẾ ĐÃ ĐƯỢC DÙNG INLINE**

```
  Framework ĐÃ LUÔN viết kèm inline label:
  → "M1 compiled suppress" → chỉ cần bỏ "M1"
  → "M2 habituation" → chỉ cần bỏ "M2"
  → "M3 prediction completion" → chỉ cần bỏ "M3"
  → "M4 Entity-Compiled saturation" → chỉ cần bỏ "M4"
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức (Resonance Decline)

```
  ┌──────────┬─────────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới                 │ Lý do                            │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M1       │ Compiled-Suppress       │ Suppress drive riêng → mất       │
  │          │                         │ nguồn by-products. STRONGEST.   │
  │          │                         │ Accelerator cho 3 cơ chế kia.   │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M2       │ Habituation             │ Weber-Fechner. Cùng stimulus    │
  │          │                         │ → VTA giảm fire → reward giảm.  │
  │          │                         │ Hardware tự nhiên. ĐỘC LẬP.     │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M3       │ Prediction-Completion   │ Self-Pattern-Modeling quá        │
  │          │                         │ accurate → delta = 0 → hết     │
  │          │                         │ novelty. Gap vẫn CÓ nhưng      │
  │          │                         │ không fill MỚI.                 │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M4       │ Entity-Saturation       │ Entity-Compiled formation       │
  │          │                         │ 40→200h diminishing returns.    │
  │          │                         │ Ít chunks MỚI về partner.       │
  └──────────┴─────────────────────────┴──────────────────────────────────┘

  Grouped label:
  → "M1-M4" → "4 Decline mechanisms"
  → "M1-M4 Resonance Decline" → "4 Resonance-Decline mechanisms"
  → Short context: "Compiled-Suppress through Entity-Saturation"
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Compiled-Suppress / Habituation / Prediction-Completion / Entity-Saturation
  = CAPITALIZED + HYPHENATED (concept names)

  Short forms khi context ĐÃ RÕ (trong formulas, tables):
  → "Suppress" / "Habituation" / "Completion" / "Saturation"
  → KHÔNG viết tắt thành CS/H/PC/ES

  Formulas:
  → "Compiled-Suppress ACCELERATE Habituation+Prediction-Completion+Entity-Saturation"
  → Hoặc ngắn: "Suppress ACCELERATE Habituation+Completion+Saturation"
```

### §1.3 — Compound terms

```
  ┌────────────────────────────────────┬──────────────────────────────────────┐
  │ Hiện tại                           │ Sau rename                           │
  ├────────────────────────────────────┼──────────────────────────────────────┤
  │ M1-M4                              │ 4 Decline mechanisms                 │
  │ M1-M4 Resonance Decline            │ 4 Resonance-Decline mechanisms       │
  │ M1 ACCELERATE M2+M3+M4            │ Compiled-Suppress ACCELERATE         │
  │                                    │ Habituation+Prediction-Completion    │
  │                                    │ +Entity-Saturation                   │
  │ M1 compiled suppress               │ Compiled-Suppress (bỏ M1)            │
  │ M1+M2+M3+M4 COMPOUND              │ All 4 Decline mechanisms COMPOUND    │
  │ Fix M1                             │ Fix Compiled-Suppress                │
  │ which M1-M4 attack?                │ which Decline mechanisms attack?     │
  │ M1 + M2                            │ Compiled-Suppress + Habituation      │
  │ §4 — M1-M4                         │ §4 — 4 RESONANCE-DECLINE MECHANISMS │
  └────────────────────────────────────┴──────────────────────────────────────┘
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — Replace_all passes (per SAFE file)

```
  ⭐ THỨ TỰ:

  PHASE A — GROUPED LABELS (trước standalone):
  Pass 1: "M1-M4"           → "4 Decline mechanisms"
  Pass 2: "M1+M2+M3+M4"    → "Compiled-Suppress+Habituation+Prediction-Completion+Entity-Saturation"

  PHASE B — LABELED PATTERNS (tránh redundancy):
  Pass 3: "M1 compiled suppress"  → "Compiled-Suppress"
  Pass 4: "M1 Compiled suppress"  → "Compiled-Suppress"
  Pass 5: "M2 habituation"        → "Habituation"
  Pass 6: "M2 Habituation"        → "Habituation"
  Pass 7: "M3 prediction completion" → "Prediction-Completion"
  Pass 8: "M3 Prediction completion" → "Prediction-Completion"
  Pass 9: "M4 Entity-Compiled saturation" → "Entity-Saturation"

  PHASE C — STANDALONE (catch remaining):
  Pass 10: "M1" → "Compiled-Suppress"
  Pass 11: "M2" → "Habituation"
  Pass 12: "M3" → "Prediction-Completion"
  Pass 13: "M4" → "Entity-Saturation"

  ⚠️ PHASE C CHỈ DÙNG CHO FILES "SAFE" (pure Resonance Decline context)
  → Files MIXED phải MANUAL cho pass 10-13
```

### §2.2 — PHẢI thay

```
  ① M1/M2/M3/M4 khi nói về RESONANCE DECLINE → đổi tương ứng
  ② "M1-M4" grouped reference → "4 Decline mechanisms"
  ③ Headers chứa M1-M4 → đổi tương ứng
  ④ Formulas/tables chứa M1-M4 → đổi, adjust width
```

### §2.3 — KHÔNG thay

```
  ① M1-M5 ENTITY PROFILE PARAMETERS (Resonance-Per-Entity §3):
     "M1. Hardware subsidy", "M2. Compilation path", ...
     → KHÁC CONCEPT — GIỮ HOẶC RENAME RIÊNG (xem §5.1)

  ② M1-M4 FIRING MODES (Domain-Mapping-Drive, Discovery-vs-Expansion):
     → ⚠️ ĐÂY LÀ LỖI — cross-ref Bond-Architecture §M1-M4 nhưng
        define KHÁC concepts hoàn toàn
     → CẦN SỬA LỖI, KHÔNG PHẢI RENAME (xem §5.2)

  ③ M1-M4 MOTOR ARC EVENTS (Child-Chunk-Development):
     "M1 = Palmar grasp", "M2 = Rooting"
     → MODALITY ARC CODE (V1/A1/M1/B1/I1) — SEPARATE SYSTEM
     → SKIP (Child-Dev files = separate plan scope)

  ④ M1-M2 PFC DAMAGE (02-Dissonance.md):
     → SEPARATE SCOPE — only 1 file
     → SKIP hoặc rename riêng

  ⑤ Backup files → SKIP
```

### §2.4 — CẦN REVIEW CẨN THẬN (MIXED context)

```
  ⚠️ Resonance-Per-Entity.md (~58 M-label occ):
  → ~28 occ = Resonance Decline M1-M4 → ĐỔI
  → ~30 occ = Entity Profile Parameters M1-M5 → GIỮ (or rename separately)
  → KHÔNG dùng replace_all pass 10-13
  → MANUAL: đọc từng occurrence, phân biệt context

  ⚠️ Body-Base.md (~14 M-label occ):
  → Verify: Resonance Decline vs other systems

  ⚠️ Neural-Architecture.md (~5 M-label occ):
  → Verify: có thể là neuroscience M1 (primary motor cortex)
```

---

## §3 — FILE INVENTORY (ACTIVE FILES — RESONANCE DECLINE CONTEXT)

### §3.1 — Tổng quan

```
  Total active files cần sửa:  ~40 files
  Total estimated replacements: ~500 (Resonance Decline only)
  Collision fix files:           ~4 files (separate sessions)
  Backup files (SKIP):          ~15+ files

  KHÔNG SỬA:
  → Child-Chunk-Development/ motor arcs (M = Motor modality)
  → Mọi file trong backup/
```

### §3.2 — Cluster 1: SOURCE DEFINITION (Session 1)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ Agent-Mechanism/Bond-Architecture.md           │ ~42   │ SOURCE   │
  │ 2 │ Agent-Mechanism/By-Product-Scale.md            │ ~5    │          │
  │ 3 │ Agent-Mechanism/Resonance-Sustainability.md    │ ~18   │          │
  │ 4 │ Agent-Mechanism/Self-Pattern-Modeling.md       │ ~8    │          │
  │ 5 │ Agent-Mechanism/Entity-Access.md               │ ~1    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~74   │ 5 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.3 — Cluster 2: OBSERVATION (Session 2)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │ 6 │ Observation/Boredom.md                         │ ~50   │ HEAVY    │
  │ 7 │ Observation/Connection.md                      │ ~42   │ HEAVY    │
  │ 8 │ Observation/Empathy.md                         │ ~28   │          │
  │ 9 │ Observation/Status.md                          │ ~12   │          │
  │10 │ Observation/Protect.md                         │ ~8    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~140  │ 5 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.4 — Cluster 3: BODY-BASE + CORE (Session 3)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │11 │ Body-Coupling.md                               │ ~22   │          │
  │12 │ Body-Base.md                                   │ ~14   │ VERIFY   │
  │13 │ Inter-Body-Mechanism.md                        │ ~5    │          │
  │14 │ Anchor-Schema-Example.md                       │ ~11   │          │
  │15 │ Neural-Architecture.md                         │ ~5    │ VERIFY   │
  │16 │ Valence-Propagation.md                         │ ~3    │          │
  │17 │ Gap-Distribution-Profile.md                    │ ~2    │          │
  │18 │ Gap-Body-Need.md                               │ ~1    │          │
  │19 │ Chunk.md                                       │ ~3    │          │
  │20 │ Core-Hardware.md (root)                        │ ~1    │          │
  │21 │ Neural-Processing-Flow.md                      │ ~1    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~68   │ 11 files │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.5 — Cluster 4: RESEARCH + MISC (Session 4)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │22 │ Love-Unified.md                                │ ~35   │          │
  │23 │ Love-Romantic.md                               │ ~29   │          │
  │24 │ Coordination-Node.md                           │ ~2    │          │
  │25 │ Collective-Body.md                             │ ~2    │          │
  │26 │ Emergent-Patterns.md                           │ ~2    │          │
  │27 │ Quote-Analysis files (~3 files)                │ ~12   │          │
  │28 │ 01-File-Index.md (Core-Deep-Dive)              │ ~9    │          │
  │29 │ Research/01-File-Index.md                      │ ~2    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~93   │ ~10 files│
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.6 — Cluster 5: MIXED + COLLISION FIXES (Session 5)

```
  ⚠️ Session đặc biệt — MANUAL REVIEW cho mỗi occurrence.

  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │30 │ Agent-Mechanism/Resonance-Per-Entity.md        │ ~58   │ ⚠️ MIXED│
  │   │   (~28 Decline + ~30 Entity Profile M1-M5)    │       │          │
  │31 │ Domain/Domain-Mapping-Drive.md                 │ ~12   │ ⚠️ ERROR│
  │32 │ Domain/Discovery-vs-Expansion.md               │ ~10   │ ⚠️ ERROR│
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~80   │ 3 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

---

## §4 — SESSION PLAN

```
  ┌─────┬─────────────────────────────┬───────┬───────┬──────────────────┐
  │ Ses │ Cluster                     │ Files │ ~Occ  │ Note             │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │ S1  │ Source + Agent-Mechanism    │   5   │  ~74  │ SOURCE DEFINITION│
  │ S2  │ Observation                 │   5   │ ~140  │ Boredom HEAVY    │
  │ S3  │ Body-Base + Core            │  11   │  ~68  │ VERIFY 2 files   │
  │ S4  │ Research + Misc             │  ~10  │  ~93  │                  │
  │ S5  │ MIXED + Collision Fixes     │   3   │  ~80  │ ⚠️ ALL MANUAL   │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │     │ TOTAL                       │ ~34   │ ~455  │ 5 sessions       │
  └─────┴─────────────────────────────┴───────┴───────┴──────────────────┘
```

---

## §5 — COLLISION FIXES (Session 5)

### §5.1 — Entity Profile Parameters M1-M5 (Resonance-Per-Entity.md)

```
  HIỆN TẠI:
  → M1. Hardware subsidy level
  → M2. Compilation path
  → M3. Cost profile
  → M4. 2-tầng proportion
  → M5. 2-luồng proportion

  VẤN ĐỀ:
  → Sau Decline rename, "M1" trong file này = ambiguous
  → Entity Profile dùng "M1." (with dot) — có thể phân biệt
  → NHƯNG vẫn confusing cho reader

  GIẢI PHÁP ĐỀ XUẤT:
  → Bỏ M-prefix, dùng descriptive headers:
     "M1. Hardware subsidy" → "① Hardware subsidy" (hoặc bullet list)
  → HOẶC rename parameters riêng:
     "M1" → "P1" (Parameter 1) — vẫn generic nhưng ít collision
  → HOẶC remove numbering entirely — chỉ dùng descriptive labels
  → Quyết định khi thực hiện S5
```

### §5.2 — Domain-Mapping "Firing Modes" M1-M4 (ERROR FIX)

```
  ⚠️ ĐÂY LÀ LỖI TỪ CONCEPT CASCADE REFINE (2026-05-23 v2.0):

  Domain-Mapping-Drive.md line 944-951 DEFINE:
    "M1 (Structural) — baseline, steady, low-resource"
    "M2 (Current-Shift) — medium, VTA fire khi có delta"
    "M3 (Peak) — high, opioid + dopamine cùng fire"
    "M4 (Compound) — mixed valence, nhiều systems cùng fire"

  Line 951: "→ Xem Bond-Architecture.md v1.0 §M1-M4"
  → SAI! Bond-Architecture M1-M4 = Resonance DECLINE, không phải Firing Modes

  Discovery-vs-Expansion.md line 1036-1043: SAME ERROR.

  GIẢI PHÁP:
  ① Xóa cross-ref sai: "→ Xem Bond-Architecture.md v1.0 §M1-M4"
  ② Rename firing modes labels — KHÔNG dùng M1-M4:
     → Option A: dùng descriptive names trực tiếp:
       "Structural firing / Current-Shift firing / Peak firing / Compound firing"
     → Option B: dùng prefix khác: "FM-1/FM-2/FM-3/FM-4" (Firing Mode)
     → KHUYẾN NGHỊ: Option A (descriptive, nhất quán framework style)
  ③ Sửa cross-ref đúng: point to Valence-Propagation hoặc define locally
```

### §5.3 — Motor Arc Codes (Child-Chunk-Development) — SKIP

```
  V1/A1/M1/B1/I1 = modality arc codes (Visual/Auditory/Motor/Bladder/Interoceptive)
  → "M1" ở đây = "Motor event #1" (Palmar grasp)
  → KHÁC SYSTEM hoàn toàn — arc labeling convention
  → SKIP: không rename trong plan này
  → Nếu muốn rename → plan riêng cho toàn bộ arc code system
```
