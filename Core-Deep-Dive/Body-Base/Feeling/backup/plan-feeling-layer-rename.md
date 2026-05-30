# Plan: Feeling 7-Layer Rename — L1-L7 → Feel-[Name]

```
Status:    ✅✅ COMPLETE (2026-05-26)
Created:   2026-05-26
Completed: 2026-05-26
Scope:     ~65+ active files, ~490+ replacements (actual)
Approach:  PHASE-BY-PHASE (source → core → drill → research)
Depends:   Body-Knowing.md v1.0 COMPLETE (2026-05-25)
Verify:    ✅ grep "L[1-7]" Feeling context = 0 in all active files
```

---

## §0 — TẠI SAO ĐỔI TÊN

```
VẤN ĐỀ: "L" NUMBERING COLLISION — 5 HỆ THỐNG DÙNG CHUNG PREFIX

  "L2" xuất hiện → nghĩa nào?
    Body-Base substrate:     L2 = REMOVED (deprecated)
    Valence-Propagation:     L2 = Valence-Structural (Entity-Compiled stream)
    PFC-Inference Ladder:    L2 = Pattern-match activation
    By-Product-Scale:        L2 = Hub/Serotonin level
    ★ Feeling 7-Layer:       L2 = Integration (insula + ACC, ~95% fidelity)

  → 5 concepts × 1 label = DANGEROUS
  → Body-Knowing.md vừa tạo (2,042L) sẽ được reference RỘNG trong framework
  → Cần đổi tên Feeling layers TRƯỚC KHI propagate thêm

  Plan này CHỈ đổi tên HỆ THỐNG FEELING (System E trong plan-l-label-rename.md).
  4 hệ thống khác = plans riêng (sau).
```

---

## §1 — BẢNG ĐỔI TÊN

### §1.1 — 7 Feeling Layers

```
⭐ RENAME TABLE:

  ┌──────────┬──────────────────────────┬──────────────────────────────────┐
  │ Cũ       │ Mới                      │ Nghĩa (từ Feeling.md §2)        │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L1       │ Feel-RawSignals          │ Body systems fire (100%)         │
  │ Layer 1  │                          │                                  │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L2       │ Feel-Integration         │ Insula + ACC + vmPFC (~95%)      │
  │ Layer 2  │                          │                                  │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L3       │ Feel-Consciousification  │ Body state → PFC-noticeable      │
  │ Layer 3  │                          │ (~90%)                           │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L4       │ Feel-Observation         │ PFC actively attend (~85%)       │
  │ Layer 4  │                          │                                  │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L5       │ Feel-Location            │ PFC locate source (70-90%)       │
  │ Layer 5  │                          │                                  │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L6       │ Feel-Labeling            │ PFC assign word (40-80%)         │
  │ Layer 6  │                          │                                  │
  ├──────────┼──────────────────────────┼──────────────────────────────────┤
  │ L7       │ Feel-Explanation         │ PFC build narrative (20-70%)     │
  │ Layer 7  │                          │                                  │
  └──────────┴──────────────────────────┴──────────────────────────────────┘
```

### §1.2 — Compound Patterns

```
COMPOUND RANGES — CÁC MẪU KẾT HỢP:

  Cũ           → Mới
  ─────────────────────────────────────────────────────────────
  L1-L2        → Feel-RawSignals–Feel-Integration
  L1-L3        → Feel-RawSignals–Feel-Consciousification
  L3→L4        → Feel-Consciousification → Feel-Observation
               (threshold crossing)
  L4-L5        → Feel-Observation–Feel-Location
  L4-L6        → Feel-Observation–Feel-Labeling
  L6-L7        → Feel-Labeling–Feel-Explanation
  L1-L7        → toàn bộ Feeling gradient (7 layers)

  TRONG TABLES — nếu quá dài:
    "Feel-RawSignals + Feel-Integration" (2 dòng trong table cell)
    hoặc gộp: "Feel-RawSignals/Integration" (nếu clear trong context)
    KHÔNG dùng "L1-L2" (mục đích rename = loại bỏ L-number)
```

### §1.3 — KHÔNG đổi tên (exclusions)

```
⚠️ KHÔNG ĐỔI NHỮNG THỨ NÀY:

  ① Ladder system (PFC-Inference): L0, L1, L2, L3, L4
     → Files: Child-Chunk-Development/, Event-Chunks-Inference-Matrix
     → NHẬN BIẾT: "L4" trong Ladder context = "Ladder-Execution"
     → Sẽ có plan RIÊNG cho Ladder rename (→ Ladder-[Name])

  ② Valence-Propagation 2-luồng: L1, L2
     → Files: Valence-Propagation.md, related
     → NHẬN BIẾT: "L1/L2 luồng" context
     → Sẽ có plan RIÊNG (→ Valence-Momentary/Structural)

  ③ Body-Base substrate: L0, L1 (current), old L2/L3 (deprecated)
     → NHẬN BIẾT: "L0 Alive Threshold", "L1 Substrate-Inputs"
     → Sẽ có plan RIÊNG (→ Substrate-[Name])

  ④ By-Product-Scale: Level 1, Level 2, Level 3
     → NHẬN BIẾT: "Scale-Pair/Hub/Institutional"
     → Sẽ có plan RIÊNG

  ⑤ backup/ directories — KHÔNG đổi (archived)

  ⑥ Fidelity percentages (100%, ~95%, ~90%, ~85%, 70-90%, 40-80%, 20-70%)
     → GIỮ NGUYÊN — chỉ đổi TÊN layer, không đổi metrics
```

---

## §2 — DANH SÁCH FILES (55 active, phân tier)

### Tier 0 — Source of Truth (ĐỔI ĐẦU TIÊN)

```
1. Feeling.md v3.0
   → §2 (7-Layer definition = GỐC), §2.5 (Compiled/Fresh mapping)
   → ~50+ occurrences (Layer 1-7, L1-L7, L1-L3, L4-L5, L6-L7...)
   → QUAN TRỌNG NHẤT: đổi ở đây = define convention cho toàn framework
```

### Tier 1 — Core Framework (đổi ngay sau Tier 0)

```
2. Body-Knowing.md v1.0
   → §3 (7-Layer mapping), §6 (Cases), throughout
   → ~52 occurrences

3. Logic-Feeling.md v3.0
   → §1 (Body-Knowing def), §3 (flow)
   → ~15-20 occurrences

4. Body-Feedback-Label.md v2.1
   → §8 (Compiled/Fresh labels reference layers)
   → ~10-15 occurrences

5. PFC-Label.md v1.1
   → Layer vocabulary
   → ~5-10 occurrences

6. Body-Feedback-Mechanism.md v2.0
   → Body-feedback × layer references
   → ~10 occurrences

7. Core-Software.md
   → §12.4 (calibration anchors reference fidelity %)
   → ~8-10 occurrences

8. Logic-Feeling-Balance.md v2.1
   → Layer references in meta-principle
   → ~5-8 occurrences

9. Body-Base.md
   → Layer references (CAUTION: also has Substrate L0/L1)
   → ~5-8 occurrences, MANUAL review needed

10. PFC-Function.md v1.2
    → ~3-5 occurrences
```

### Tier 2 — Core-Deep-Dive Support Files

```
11. Logic-Planning.md (L6 Label 3-tier reference)
12. Connection.md v5.0 (L4-L6 references)
13. Valence-Propagation.md v3.0 (CAUTION: also 2-luồng L1/L2)
14. Body-Feedback.md
15. Blackbox-Map.md
16. Schema.md
17. Chunk.md v2.0
18. Agent-Mechanism.md v2.1
19. Cortisol-Baseline.md v2.0
20. Liking-Wanting.md
21. Gratitude.md
22. AI-Schema-Detection.md
23. Neural-Processing-Flow.md
24. Imagine-Final-Evaluation.md
25. Logic-Feeling-Failure-Examples.md (PFC/ folder)

→ ~80-120 occurrences total (est. 5-10 per file)
→ Mỗi file cần MANUAL review: L nào là Feeling, L nào là hệ thống khác
```

### Tier 3 — Drill + Draft Files

```
26. Feeling-Literacy-Training-Draft.md
27. Feeling-Mechanism-Deep-Draft.md
28. Feeling-Sources-Draft.md
29. Feeling-Chunk-Bridge-Draft.md
30. Feeling-Accuracy-Draft.md
31. Feel-Example-Draft.md
32. Feel-Development.md
33-38. Drill-Feeling-Knowning/ (6 files: 00-Reading-Notes, 01-Theme-A,
       03-Theme-B, 99-Overview-Synthesis, + others)
39-41. Drill-Body-Feedback/ (01-Foundation, 02-Dissonance, 03-Reward, 04-Integration)
42-44. Chunk-Internal-Processing/ (00-Overview, 02-Feeling-Gradient, 04-Right-Wrong)
45. 99-Master-Synthesis.md

→ ~100-150 occurrences total
→ Draft files = lower priority nhưng vẫn cần update
```

### Tier 4 — Research + Education + Other

```
46. Mother-Optimization.md
47. Natural-Development.md
48. Child-Development-Mechanism.md
49. Religion.md
50. AI-Self-Model.md v2.0
51. expert-verification-map.md

→ ~20-30 occurrences total
```

### Tier 5 — Child-Chunk-Development (MIXED — cần manual)

```
52-55. Files có CẢ Ladder L4 VÀ Feeling layers:
  → 06a-Interoceptive-Bladder-Keystone.md (+ VI version)
  → 00-Chunk-System-Sketch.md (+ VI version)
  → PHẢI manual review TỪNG occurrence: Ladder hay Feeling?
  → Nếu L4 = PFC-Inference Ladder → KHÔNG đổi
  → Nếu L4 = Feeling Observation → ĐỔI

→ ~20-40 occurrences cần manual review
```

### Plans (update reference only)

```
→ plan-body-knowing.md, plan-body-knowing-v2.md
→ Chỉ update references, KHÔNG đổi nội dung plan
```

---

## §3 — EXECUTION PHASES

### Phase 1: Feeling.md — Source of Truth (~50+ occ)

```
MỤC TIÊU: Define convention mới tại source of truth.

BƯỚC:
  ① Đọc Feeling.md §2 toàn bộ
  ② Đổi §2.1 Overview diagram: Layer 1-7 → Feel-[Name]
  ③ Đổi §2.2 (Layer 1-3 body domain)
  ④ Đổi §2.2b (threshold crossing L3→L4)
  ⑤ Đổi §2.3 (Layer 4-7 PFC domain)
  ⑥ Đổi §2.4 (fidelity loss diagram)
  ⑦ Đổi §2.5 (Compiled/Fresh mapping)
  ⑧ Đổi TẤT CẢ các section khác có reference L1-L7
  ⑨ Verify: grep "L[1-7]" trong Feeling.md context = 0
  ⑩ THÊM: §2.0 mới "Naming Convention" (table §1.1 trên)

CAUTION:
  → Feeling.md CÓ references tới Body-Base L0/L1 substrate
  → KHÔNG đổi những cái đó — chỉ đổi Feeling layers
  → Nhận biết: "L0" = always substrate (Feeling không có L0)
    "L1-L2 raw signals" = Feeling (đổi)
    "L1 substrate" = Body-Base (KHÔNG đổi)

QUALITY CHECK:
  - [ ] §2 diagram shows Feel-[Name] consistently
  - [ ] All "Layer N" → "Feel-[Name]" in §2
  - [ ] All "LN" shorthand → "Feel-[Name]" throughout
  - [ ] Body-Base L0/L1 substrate references UNTOUCHED
  - [ ] Fidelity percentages preserved
  - [ ] Cross-references to other files still accurate
```

### Phase 2: Body-Knowing.md (~52 occ)

```
MỤC TIÊU: Update file mới nhất (2,042L, vừa tạo).

BƯỚC:
  ① §3.1 table: L1-L2/L3/L4-L5/L6/L7 → Feel-[Name]
  ② §3.2 "Body-Knowing = L4-L6 COMPILED" → "Feel-Observation–Feel-Labeling COMPILED"
  ③ §3.3 training reframe
  ④ §4 Formation Process (SAL stage references với layer context)
  ⑤ §6 Case table (L1-L2, L3-L4, etc.)
  ⑥ Toàn bộ file: mọi "L[1-7]" Feeling context

QUALITY CHECK:
  - [ ] §3.1 table accurate với tên mới
  - [ ] §3.2 Body-Knowing zone defined bằng tên mới
  - [ ] §6 Case table consistent
  - [ ] No "L[1-7]" Feeling references remain
```

### Phase 3: Core Framework Files (~60-80 occ, ~8 files)

```
MỤC TIÊU: Logic-Feeling, Body-Feedback-Label, PFC-Label, BFM, Core-Software, LFB, Body-Base, PFC-Function.

BƯỚC — mỗi file:
  ① Đọc file, identify Feeling layer references
  ② PHÂN BIỆT Feeling L vs Other L (nếu file có nhiều hệ thống)
  ③ Đổi Feeling layers → Feel-[Name]
  ④ Verify per file

⚠️ CAUTION files:
  → Body-Base.md: also has Substrate L0/L1
  → Valence-Propagation.md (Tier 2): also has 2-luồng L1/L2
  → Cần MANUAL review per occurrence
```

### Phase 4: Core-Deep-Dive Support (~80-120 occ, ~15 files)

```
MỤC TIÊU: Tier 2 files — broader Core-Deep-Dive.

→ Same process: read → identify → rename → verify per file.
→ Lower risk (most files have few occurrences).
→ Can batch similar files.
```

### Phase 5: Drill + Draft (~100-150 occ, ~20 files)

```
MỤC TIÊU: Tier 3 files — drafts and drill outputs.

→ Same process.
→ Draft files = lower priority nhưng vẫn rename for consistency.
→ Drill files often have MANY L references — cẩn thận.
```

### Phase 6: Research + Education + Mixed (~40-70 occ, ~10 files)

```
MỤC TIÊU: Tier 4 + Tier 5 files.

→ Tier 4 (Research): straightforward rename.
→ Tier 5 (Mixed Ladder/Feeling): MANUAL per-occurrence review.
  → Child-Chunk-Development files: L4 could be Ladder or Feeling
  → Must check context for EACH occurrence
```

### Phase 7: Final Verification

```
BƯỚC:
  ① grep "\bL[1-7]\b" across TOÀN BỘ active .md files
  ② Mỗi remaining hit: verify = NOT Feeling system (Ladder, Valence, Scale, etc.)
  ③ 0 Feeling L-labels remaining = DONE
  ④ Update plan-l-label-rename.md: mark System E = COMPLETE
  ⑤ Update MEMORY
```

---

## §4 — PRACTICAL CONSIDERATIONS

### §4.1 — Table Formatting

```
VẤN ĐỀ: tên mới DÀI hơn nhiều (L4 = 2 chars → Feel-Observation = 16 chars)

  CŨ (compact):
  ┌────────┬──────────────────────┐
  │ L4-L5  │ Observation + Loc.   │
  └────────┴──────────────────────┘

  MỚI (option A — full name, 2 rows):
  ┌──────────────────────────┬──────────────────────┐
  │ Feel-Observation +       │ PFC attend + locate   │
  │ Feel-Location            │                       │
  └──────────────────────────┴──────────────────────┘

  MỚI (option B — header indicates system):
  ┌───────────────────┬──────────────────────┐
  │ Observation +     │ PFC attend + locate   │
  │ Location          │                       │
  └───────────────────┴──────────────────────┘
  (khi table header đã nói rõ = Feeling Layers)

→ RECOMMEND: Option A cho lần đầu trong file (establish context).
  Option B cho tables sau (khi context đã rõ).
  KHÔNG dùng L-number.
```

### §4.2 — Search Patterns for Each Phase

```
GREP PATTERNS (per file):

  UNIQUE Feeling (safe to replace):
    "L5", "L6", "L7" → ALWAYS Feeling (no other system has L5-L7)
    "Layer 5", "Layer 6", "Layer 7" → ALWAYS Feeling
    "L4-L5", "L4-L6", "L6-L7", "L1-L7" → ALWAYS Feeling

  SHARED (need context check):
    "L1" → Feeling? Substrate? Valence? Ladder? Scale?
    "L2" → Feeling? Substrate(old)? Valence? Ladder? Scale?
    "L3" → Feeling? Substrate(old)? Ladder? Scale?
    "L4" → Feeling? Ladder?

  HOW TO DISTINGUISH:
    → Near "feeling", "fidelity", "gradient", "layer" → Feeling
    → Near "substrate", "body-base", "L0" → Body-Base
    → Near "luồng", "valence", "structural", "momentary" → Valence
    → Near "ladder", "inference", "chunk development" → Ladder
    → Near "scale", "pair", "hub", "institutional" → By-Product-Scale
```

---

## §5 — ESTIMATES

```
  Phase 1: Feeling.md         ~50-60 occ    ~1 session phần
  Phase 2: Body-Knowing.md    ~52 occ       ~1 session phần
  Phase 3: Core Framework     ~60-80 occ    ~1 session
  Phase 4: Support Files      ~80-120 occ   ~1-2 sessions
  Phase 5: Drill + Draft      ~100-150 occ  ~1-2 sessions
  Phase 6: Research + Mixed   ~40-70 occ    ~1 session
  Phase 7: Verification       ~30 min

  TOTAL: ~400-530 occurrences, ~55 files, ~4-7 sessions
  (phụ thuộc tốc độ — mỗi session = 1-2 phases)
```

---

## §6 — EXECUTION ORDER

```
BƯỚC 1: Đọc plan này
BƯỚC 2: Phase 1 — Feeling.md (source of truth)
BƯỚC 3: Phase 2 — Body-Knowing.md (mới nhất, most occurrences)
BƯỚC 4: Phase 3 — Core Framework (8 files)
         → Có thể gộp Phase 2+3 trong cùng session
BƯỚC 5: Phase 4 — Support Files (15 files)
BƯỚC 6: Phase 5 — Drill + Draft (20 files)
         → Có thể gộp Phase 4+5 trong cùng session
BƯỚC 7: Phase 6 — Research + Mixed (10 files)
BƯỚC 8: Phase 7 — Final Verification
```

---

## §7 — SAU KHI HOÀN THÀNH

```
① Update plan-l-label-rename.md: System E = COMPLETE
② Update Body-Knowing.md Phase 2 cascade:
   → 2A: Feeling.md refine (add Body-Knowing.md reference)
   → 2B: Logic-Feeling.md trim §1.1
   → 2C: Cross-ref updates
③ Bắt đầu plan cho System A (Substrate), C (Ladder), B (Valence), D (Scale)
   nếu muốn đóng toàn bộ L-collision
```
