# Plan: F1/F2 Function Rename — F1/F2 → Compiled/Fresh

```
Status:    ✅ COMPLETE (Sessions 1-7, 2026-05-24)
Created:   2026-05-23
Scope:     ~83 active files, ~1,357 replacements (Self-Pattern-Modeling F1/F2)
Approach:  CLUSTER-BY-CLUSTER (Source Definition → Deep-Dive → Research → Application)
Depends:   KHÔNG. Chạy ĐỘC LẬP với plan-reward-type-rename.md và plan-compile-type-rename.md
Verify:    grep "\bF1\b" + "\bF2\b" = 0 trong SPM-context files sau mỗi session
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 3 lý do chính

**① F1/F2 LÀ GENERIC LABEL KHÔNG MANG NGHĨA**

```
  "F1" — function gì? compiled? fast? first?
  "F2" — function gì? cái nào trong framework?
  → Phải tra bảng mỗi lần gặp

  "Compiled" — ngay lập tức hiểu: body-level automatic, cost ≈ 0, milliseconds
  "Fresh" — ngay lập tức hiểu: PFC deliberate prediction chain, costly, seconds
  → Tự giải thích, không cần tra bảng
```

**② TRÙNG KÝ HIỆU VỚI NHIỀU HỆ THỐNG F-LABELS KHÁC**

```
  Framework hiện tại có ÍT NHẤT 3 hệ thống F-labels:

  SPM FUNCTIONS:                 CHUNK DRILL FOLDERS:           MELODY-TECHNOLOGY FUNCTIONS:
  ──────────────                 ──────────────────             ────────────────────────────
  F1 = Compiled function         F1 = Child-Chunk-Dev           F1 = Life-Level Anchor
  F2 = Fresh function            F3 = Chunk-External-Dev        F2 = Compiled Compliance
                                 F4 = Chunk-Internal-Proc       F3 = Structured Connection
                                 R-F1-* = recommendation        F4 = Dissonance Resolution
                                                                F5-F7 = (other functions)

  → Cùng "F1" — 3 concept KHÁC NHAU HOÀN TOÀN
  → Người đọc gặp "F1" phải suy context
  → Rename SPM F1/F2 → Compiled/Fresh → PHÂN BIỆT NGAY LẬP TỨC
```

**③ TÊN THAY THẾ ĐÃ ĐƯỢC DÙNG RỘNG RÃI**

```
  Framework ĐÃ CÓ:
  → Compiled-Fresh.md (file riêng define Compiled/Fresh spectrum)
  → "Compiled Quality" (concept đã define)
  → "F1 Compiled" / "F2 Fresh" (luôn đi kèm label trong hầu hết files)

  → Chỉ cần BỎ prefix "F1"/"F2", GIỮ lại "Compiled"/"Fresh"
  → 100% nhất quán với vocabulary hiện tại — KHÔNG tạo từ mới
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức

```
  ┌──────────────────┬─────────────────┬──────────────────────────────────┐
  │ Hiện tại         │ Tên mới         │ Lý do                            │
  ├──────────────────┼─────────────────┼──────────────────────────────────┤
  │ F1               │ Compiled        │ Body-level automatic simulation. │
  │                  │                 │ Hebbian-reinforced. Cost ≈ 0.    │
  │                  │                 │ Milliseconds. Đã dùng            │
  │                  │                 │ "F1 Compiled" xuyên suốt.        │
  ├──────────────────┼─────────────────┼──────────────────────────────────┤
  │ F2               │ Fresh           │ PFC deliberate prediction chain. │
  │                  │                 │ Effortful. Seconds. "Fresh" =    │
  │                  │                 │ chưa compiled, cần PFC draft     │
  │                  │                 │ mỗi lần. Đã dùng "F2 Fresh".    │
  └──────────────────┴─────────────────┴──────────────────────────────────┘

  TÊN TRÙNG VỚI COMPILED-FRESH.MD:
  → "Compiled" VÀ "Fresh" ĐÃ LÀ framework vocabulary
  → Compiled-Fresh.md define the spectrum
  → Sau rename: "Compiled fire" = "hàm Compiled fire" — tự giải thích
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Compiled / Fresh = CAPITALIZED khi nói về Self-Pattern-Modeling function
  → Nhất quán với: Evaluative Reward, Direct-State Reward, Entity-Compiled

  Lowercase "compiled" khi dùng như verb/adjective bình thường:
  → "chunk compiled" = chunk ĐÃ được compile (verb)
  → "Compiled fire" = hàm Compiled fire (concept name)
  → Context quyết định — capitalize khi rõ ràng là Self-Pattern-Modeling function

  KHÔNG bao giờ viết tắt:
  → KHÔNG: C/F, Comp/Fr, CF, C1/C2
  → LUÔN: Compiled/Fresh (đầy đủ)
```

### §1.3 — Compound terms

```
  ┌───────────────────────────────────┬────────────────────────────────┐
  │ Hiện tại                          │ Sau rename                     │
  ├───────────────────────────────────┼────────────────────────────────┤
  │ F1/F2                             │ Compiled/Fresh                 │
  │ F1 fire / F2 fire                 │ Compiled fire / Fresh fire     │
  │ F1 output / F2 output             │ Compiled output / Fresh output │
  │ F1 suppress                       │ Compiled suppress              │
  │ F1 OFF / F2 OFF                   │ Compiled OFF / Fresh OFF       │
  │ F1 Compiled                       │ Compiled (bỏ redundant "F1")   │
  │ F2 Fresh                          │ Fresh (bỏ redundant "F2")      │
  │ F1 Compiled + F2 Fresh            │ Compiled + Fresh               │
  │ F1 Compiled/F2 Fresh              │ Compiled/Fresh                 │
  │ F1/F2 = Compiled/Fresh            │ Compiled/Fresh (bỏ "F1/F2 =") │
  │ F1/F2 Compiled/Fresh              │ Compiled/Fresh (bỏ "F1/F2")   │
  │ F1 DEVELOPING                     │ Compiled DEVELOPING            │
  │ F1 rich / F1 near-automatic       │ Compiled rich / Compiled near-automatic │
  │ F2 empathy / F2 predict           │ Fresh empathy / Fresh predict  │
  │ F2 chain predict                  │ Fresh chain predict            │
  │ F2 deliberate / F2 only           │ Fresh deliberate / Fresh only  │
  │ (F1+F2)                           │ (Compiled+Fresh)               │
  │ Self-Pattern-Modeling F1/F2       │ Self-Pattern-Modeling Compiled/Fresh │
  │ 2 Functions F1/F2                 │ 2 Functions Compiled/Fresh     │
  │ 2 Functions: F1 Compiled + F2 ... │ 2 Functions: Compiled + Fresh  │
  └───────────────────────────────────┴────────────────────────────────┘
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — THỨ TỰ REPLACE_ALL (9 passes, PER FILE)

```
  ⭐ THỨ TỰ RẤT QUAN TRỌNG — sai order → "Compiled Compiled" hoặc miss

  PHASE A — XỬ LÝ DEFINITION PATTERNS (tránh redundancy):
  Pass 1: "F1/F2 = Compiled/Fresh" → "Compiled/Fresh"
  Pass 2: "F1/F2 Compiled/Fresh"   → "Compiled/Fresh"

  PHASE B — XỬ LÝ LABELED PATTERNS (tránh "Compiled Compiled"):
  Pass 3: "F1 Compiled" → "Compiled"     (capital C)
  Pass 4: "F1 compiled" → "Compiled"     (lowercase c)
  Pass 5: "F2 Fresh"    → "Fresh"        (capital F)
  Pass 6: "F2 fresh"    → "Fresh"        (lowercase f)

  PHASE C — XỬ LÝ PAIRED REFERENCE:
  Pass 7: "F1/F2" → "Compiled/Fresh"

  PHASE D — XỬ LÝ STANDALONE (catch phần còn lại):
  Pass 8: "F1" → "Compiled"
  Pass 9: "F2" → "Fresh"

  ⚠️ PHASE D CHỈ DÙNG CHO FILES "SAFE" (pure SPM context)
  → Files MIXED (Religion.md, Chunk.md, ...) phải MANUAL cho pass 8-9
```

### §2.2 — SAU REPLACE_ALL: KIỂM TRA

```
  Sau 9 passes, kiểm tra:
  ① grep "Compiled Compiled" — phải = 0 (nếu có = order sai)
  ② grep "Fresh Fresh" — phải = 0
  ③ grep "\bF1\b" hoặc "\bF2\b" — phải = 0 trong file đã xử lý
  ④ Đọc lại context xung quanh thay đổi — capitalization hợp lý không?
```

### §2.3 — PHẢI thay

```
  ① "F1" khi nói về SELF-PATTERN-MODELING Compiled function → "Compiled"
  ② "F2" khi nói về SELF-PATTERN-MODELING Fresh function → "Fresh"
  ③ "F1/F2" paired reference → "Compiled/Fresh"
  ④ Headers/frontmatter chứa SPM "F1/F2" → đổi tương ứng
  ⑤ "Self-Pattern-Modeling F1" → "Self-Pattern-Modeling Compiled"
```

### §2.4 — KHÔNG thay

```
  ① F1/F2/F3/F4 khi là CHUNK DRILL FOLDER labels → GIỮ NGUYÊN
     (Child-Chunk-Development/, Chunk-External-Development/,
      Chunk-Internal-Processing/, 99-Master-Synthesis.md)
  ② F1-F7 khi là MELODY-TECHNOLOGY FUNCTION labels → GIỮ NGUYÊN
     (Religion.md §2.1-§2.4, Melody-Technology-Overview.md tables)
  ③ R-F1-* recommendation labels → GIỮ NGUYÊN
  ④ "P-F10" trong Feeling.md → prediction label, KHÔNG phải SPM F1
  ⑤ Backup files (backup/, _backup/) → KHÔNG SỬA
```

### §2.5 — CẦN REVIEW CẨN THẬN (MIXED context)

```
  ⚠️ Một số files dùng "F1" cho NHIỀU concepts:

  ⚠️ Religion.md — F1-F4 = section labels (§2.1-§2.4) + SPM F1/F2 (§3, §4)
     → Chỉ thay khi CONTEXT là Self-Pattern-Modeling
     → GIỮ NGUYÊN khi context là Religion function numbering
     → "Self-Pattern-Modeling F1 fire" → "Self-Pattern-Modeling Compiled fire" ✓
     → "§2.1 — F1: Life-Level Anchor" → GIỮ NGUYÊN ✗ (section label)

  ⚠️ Chunk.md — F1 = folder cross-reference + possibly SPM
     → Hầu hết F1 ở đây = folder label → cần đọc từng occurrence
     → KHÔNG dùng replace_all pass 8-9

  ⚠️ 01-File-Index.md (Core-Deep-Dive) — R-F1-* + SPM refs
     → Protect R-F1-* patterns first
     → Manual cho pass 8-9

  ⚠️ Feeling.md — "P-F10" prediction label (line 1851)
     → replace_all "F1" sẽ biến "P-F10" → "P-Compiled0" = SAI
     → Giải pháp: sau replace_all, sửa lại "P-Compiled0" → "P-F10"
```

---

## §3 — PHÂN BIỆT: SPM F1/F2 vs OTHER F-LABELS

### §3.1 — 3 hệ thống F-labels trong framework

```
  ┌─────────────┬────────────────────────┬──────────────────────────────┐
  │ Hệ thống    │ Ý nghĩa F1/F2         │ Files sử dụng               │
  ├─────────────┼────────────────────────┼──────────────────────────────┤
  │ SPM         │ F1 = Compiled function │ ~80 files across framework   │
  │ Functions   │ F2 = Fresh function    │ → ĐỔI thành Compiled/Fresh  │
  ├─────────────┼────────────────────────┼──────────────────────────────┤
  │ Chunk Drill │ F1 = Child-Chunk-Dev   │ Child-Chunk-Development/     │
  │ Folders     │ F3 = Chunk-External    │ Chunk-External-Development/  │
  │             │ F4 = Chunk-Internal    │ Chunk-Internal-Processing/   │
  │             │ R-F1-* = recommen.     │ 99-Master-Synthesis.md       │
  │             │                        │ Chunk.md (cross-ref)         │
  │             │                        │ → KHÔNG ĐỔI (plan này)      │
  ├─────────────┼────────────────────────┼──────────────────────────────┤
  │ Melody-Tech │ F1 = Life-Level Anchor │ Religion.md (§2.1-§2.4)     │
  │ Functions   │ F2 = Compiled Compli.  │ Melody-Technology-Overview   │
  │ (7 hàm)     │ F3 = Struct. Connect.  │ Idol-Phenomenon.md (partial) │
  │             │ F4 = Dissonance Resol. │ → KHÔNG ĐỔI (plan này)      │
  │             │ F5-F7 = others         │                              │
  └─────────────┴────────────────────────┴──────────────────────────────┘
```

### §3.2 — Cách phân biệt nhanh

```
  CONTEXT CLUEs:
  ① "Self-Pattern-Modeling F1" / "Self-Pattern-Modeling F2" → SPM → ĐỔI
  ② "F1 fire" / "F1 output" / "F1 suppress" → SPM action verbs → ĐỔI
  ③ "F1 Compiled" / "F2 Fresh" → SPM labeled → ĐỔI (bỏ F1/F2)
  ④ "F1 Child-Chunk-Development" → Chunk Drill folder → GIỮ
  ⑤ "F1 NT6" / "F1 08 §5" → Chunk Drill file ref → GIỮ
  ⑥ "§2.1 — F1: Life-Level Anchor" → Melody-Tech section → GIỮ
  ⑦ "R-F1-10" → Chunk recommendation label → GIỮ

  ⭐ QUY TẮC:
  → Nếu F1/F2 ĐI KÈM Self-Pattern-Modeling context → SPM → ĐỔI
  → Nếu F1 ĐI KÈM file number / folder name / section label → KHÁC → GIỮ
  → Nếu KHÔNG RÕ → đọc 3-5 dòng context → quyết định
```

### §3.3 — Chunk Drill F1/F3/F4: SCOPE RIÊNG

```
  ⚠️ Chunk Drill folder labels (F1/F3/F4) là vấn đề RIÊNG:
  → ~39 active files, ~1,336 occurrences (F1 as folder label)
  → + R-F1-* recommendation labels: 331 occurrences, 24 files
  → + F3/F4 labels: ~1,123 occurrences, ~90 files

  → KHÔNG nằm trong scope plan này
  → Cần plan riêng nếu muốn rename (F1 → Child-Dev, F3 → External, F4 → Internal)
  → Phức tạp hơn vì gắn với file numbering system
```

---

## §4 — FILE INVENTORY (ACTIVE FILES ONLY — SPM CONTEXT)

### §4.1 — Tổng quan

```
  Total active files cần sửa:  ~80 files
  Total estimated replacements: ~1,350 (SPM F1/F2 only)
  Backup files (SKIP):          ~100+ files
  Chunk Drill files (SKIP):     ~39 files
  Melody-Tech Overview (SKIP):  1 file

  KHÔNG SỬA:
  → Mọi file trong Child-Chunk-Development/ (F1 = folder label)
  → Mọi file trong Chunk-External-Development/ (F1 = folder cross-ref)
  → Mọi file trong Chunk-Internal-Processing/ (F1 = folder cross-ref)
  → 99-Master-Synthesis.md (F1 = folder label)
  → Melody-Technology-Overview.md (F1-F7 = section labels)
  → Mọi file trong backup/, _backup/
```

### §4.2 — Cluster 1: AGENT-MECHANISM (Session 1)

```
  ⭐ PRIORITY HIGHEST — Establish new names tại SOURCE DEFINITION.
  Self-Pattern-Modeling.md DEFINE F1/F2 — phải sửa TRƯỚC.

  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ Agent-Mechanism/Self-Pattern-Modeling.md       │ ~121  │ SOURCE   │
  │ 2 │ Agent-Mechanism/Agent-Mechanism.md             │ ~46   │          │
  │ 3 │ Agent-Mechanism/Entity-Compiled.md             │ ~36   │          │
  │ 4 │ Agent-Mechanism/Resonance-Per-Entity.md        │ ~33   │          │
  │ 5 │ Agent-Mechanism/Entity-Access.md               │ ~32   │          │
  │ 6 │ Agent-Mechanism/Entity-Access-Excess.md        │ ~20   │          │
  │ 7 │ Agent-Mechanism/Entity-Access-Calibration.md   │ ~20   │          │
  │ 8 │ Agent-Mechanism/By-Product-Gap-Resonance.md    │ ~9    │          │
  │ 9 │ Agent-Mechanism/Resonance-Sustainability.md    │ ~9    │          │
  │10 │ Agent-Mechanism/Bond-Architecture.md           │ ~7    │          │
  │11 │ Agent-Mechanism/By-Product-Scale.md            │ ~4    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~337  │ 11 files │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §4.3 — Cluster 2: OBSERVATION — Heavy (Session 2)

```
  Empathy.md = HEAVIEST file trong toàn bộ plan (223 occ).
  Connection.md cũng dense (85 occ). Cần session riêng.

  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │12 │ Observation/Empathy.md                         │ ~223  │ HEAVIEST │
  │13 │ Observation/Connection.md                      │ ~85   │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~308  │ 2 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §4.4 — Cluster 3: OBSERVATION — Remaining + Background-Pattern (Session 3)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │14 │ Observation/Gratitude.md                       │ ~22   │          │
  │15 │ Observation/Obligation.md                      │ ~21   │          │
  │16 │ Chunk/Background-Pattern.md                    │ ~21   │ VERIFY   │
  │17 │ Observation/Status.md                          │ ~12   │          │
  │18 │ Observation/Drive.md                           │ ~6    │          │
  │19 │ Observation/Protect.md                         │ ~4    │          │
  │20 │ Observation/Threat.md                          │ ~4    │          │
  │21 │ Observation/Novelty.md                         │ ~3    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~93   │ 8 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §4.5 — Cluster 4: BODY-BASE + BODY-FEEDBACK + FEELING (Session 4)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │22 │ Body-Base/Body-Coupling.md                     │ ~30   │          │
  │23 │ Body-Base/Inter-Body-Mechanism.md              │ ~28   │          │
  │24 │ Body-Feedback/Hidden-Quality-Perception.md     │ ~27   │          │
  │25 │ Feeling/Feeling-Literacy-Training.md           │ ~14   │          │
  │26 │ Body-Feedback/Gap-Direction.md                 │ ~10   │          │
  │27 │ Body-Base/Body-Base.md                         │ ~9    │          │
  │28 │ Body-Feedback/Reward-Signal-Architecture.md    │ ~9    │          │
  │29 │ Feeling/Feeling.md                             │ ~6    │ ⚠️ P-F10│
  │30 │ Body-Base/Valence-Propagation.md               │ ~6    │          │
  │31 │ Feeling/Feeling-Mechanism-Deep.md              │ ~6    │          │
  │32 │ Body-Feedback/Gap-Body-Need.md                 │ ~5    │          │
  │33 │ Body-Feedback/Body-Feedback.md                 │ ~1    │          │
  │34 │ Feeling/Feeling-Accuracy.md                    │ ~1    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~152  │ 13 files │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘

  ⚠️ Feeling.md line 1851: "P-F10" = prediction label
  → replace_all "F1" sẽ biến thành "P-Compiled0"
  → Sau replace_all: grep "Compiled0" → sửa lại "P-F10"
```

### §4.6 — Cluster 5: PFC + COLLECTIVE + CORE MISC (Session 5)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │35 │ PFC/Simulation-Engine.md                       │ ~16   │          │
  │36 │ Collective/Compliance-Floor.md                 │ ~13   │          │
  │37 │ PFC/Logic-Planning.md                          │ ~9    │          │
  │38 │ Collective/Coordination-Node.md                │ ~9    │          │
  │39 │ PFC/PFC-Operations.md                          │ ~6    │          │
  │40 │ PFC/Logic-Feeling-Failure-Examples.md          │ ~6    │          │
  │41 │ PFC/Imagination/Imagine-Final.md               │ ~6    │          │
  │42 │ PFC/Logic-Feeling.md                           │ ~3    │          │
  │43 │ Domain/Emergent-Patterns.md                    │ ~3    │          │
  │44 │ Core-Software.md (root)                        │ ~3    │          │
  │45 │ Ask-AI.md (root)                               │ ~2    │          │
  │46 │ plan-architecture-rename.md                    │ ~2    │          │
  │47 │ Neural-Processing-Flow.md                      │ ~1    │          │
  │48 │ Collective/Collective-Body.md                  │ ~1    │          │
  │49 │ 01-File-Index.md (Core-Deep-Dive)              │ ~5    │ ⚠️ MIXED│
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~85   │ 15 files │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘

  ⚠️ 01-File-Index.md: chứa 1 R-F1-* reference
  → KHÔNG dùng replace_all pass 8 ("F1" → "Compiled")
  → Manual: chỉ thay SPM context, giữ R-F1-*
```

### §4.7 — Cluster 6: RESEARCH — Heavy (Session 6)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │50 │ Love-Romantic.md                               │ ~84   │ DENSE    │
  │51 │ Uncanny-Valley.md                              │ ~57   │          │
  │52 │ Religion.md                                    │ ~53   │ ⚠️ MIXED│
  │53 │ Autism-Observation.md                          │ ~36   │          │
  │54 │ Love-Unified.md                                │ ~35   │          │
  │55 │ Idol-Phenomenon.md                             │ ~35   │ CHECK    │
  │56 │ Alzheimer-Analysis.md                          │ ~23   │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~323  │ 7 files  │
  └───┴────────────────────────────────────────────────┴───────┴──────────┘

  ⚠️ Religion.md: F1-F4 = section labels (§2.1-§2.4) + SPM F1/F2 (§3+)
  → KHÔNG dùng replace_all pass 8-9
  → Manual: chỉ thay khi CONTEXT là "Self-Pattern-Modeling F1/F2"

  CHECK Idol-Phenomenon.md: chủ yếu SPM, nhưng verify F1-F7 section usage
```

### §4.8 — Cluster 7: RESEARCH REMAINING + APPLICATIONS + MISC (Session 7)

```
  ┌───┬────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                           │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │57 │ Child-Development-Mechanism.md                 │ ~18   │          │
  │58 │ Sensitivity-Classification.md                  │ ~5    │          │
  │59 │ Social-Calibration.md                          │ ~4    │          │
  │60 │ Human-AI-Future.md                             │ ~3    │          │
  │61 │ Creator-Lens.md                                │ ~3    │          │
  │62 │ Research/01-File-Index.md                      │ ~3    │          │
  │63 │ Meta-Impact/Meta-Impact.md                     │ ~2    │          │
  │64 │ ADHD-Observation.md                            │ ~2    │          │
  │65 │ Addiction-Analysis.md                          │ ~2    │          │
  │66 │ Natural-Development.md                         │ ~2    │          │
  │67 │ Money-Analysis.md                              │ ~1    │          │
  │68 │ PTSD-Analysis.md                               │ ~1    │          │
  │69 │ AI-Self-Model.md                               │ ~1    │          │
  │70 │ Epistemological-Position.md                    │ ~1    │          │
  │71 │ Collective-Schema-Pressure.md                  │ ~1    │          │
  │   │ ──── Applications ────                         │       │          │
  │72 │ Education/Hardware-Calibration.md              │ ~7    │          │
  │73 │ Education/Curriculum-Framework.md              │ ~5    │          │
  │74 │ Education/Era-Analysis-2025.md                 │ ~4    │          │
  │75 │ Education/Education-System.md                  │ ~2    │          │
  │76 │ Education/00_Overview.md                       │ ~2    │          │
  │77 │ Education/Country/VN/VN-Recommendations.md     │ ~1    │          │
  │78 │ Education/Country/VN/VN-Education-Status.md    │ ~1    │          │
  │   │ ──── Quote-Analysis ────                       │       │          │
  │79 │ Work-Chunk-Dependent-Visibility-Cluster.md     │ ~26   │          │
  │80+│ Other Quote-Analysis files (~3 files)          │ ~5    │          │
  ├───┼────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                       │ ~102  │ ~25 files│
  └───┴────────────────────────────────────────────────┴───────┴──────────┘
```

### §4.9 — SKIPPED FILES SUMMARY

```
  ┌───────────────────────────────────────────────┬───────┬──────────────┐
  │ Folder/File                                   │ ~occ  │ Reason SKIP  │
  ├───────────────────────────────────────────────┼───────┼──────────────┤
  │ Child-Chunk-Development/ (~20 files)          │ ~800+ │ F1=folder    │
  │ Chunk-External-Development/ (~8 files)        │ ~100+ │ F1=cross-ref │
  │ Chunk-Internal-Processing/ (~10 files)        │ ~200+ │ F1=cross-ref │
  │ 99-Master-Synthesis.md                        │ ~82   │ F1=folder    │
  │ Chunk.md                                      │ ~23   │ F1=folder    │
  │ Melody-Technology-Overview.md                 │ ~34   │ F1-F7=section│
  │ All backup/ files (~100+ files)               │ ~2800+│ historical   │
  ├───────────────────────────────────────────────┼───────┼──────────────┤
  │ TOTAL SKIP                                    │ ~4000+│              │
  └───────────────────────────────────────────────┴───────┴──────────────┘

  ⚠️ Chunk Drill F1/F3/F4 rename = SEPARATE PLAN nếu muốn
  → Scope riêng: ~39 files, ~1,336+ occ
  → Phức tạp hơn: gắn với file numbering (F1 NT6, F1 08 §5, R-F1-*)
  → Cần define tên mới: F1→?, F3→?, F4→?
```

---

## §5 — SESSION PLAN

```
  ┌─────┬─────────────────────────────┬───────┬───────┬──────────────────┐
  │ Ses │ Cluster                     │ Files │ ~Occ  │ Note             │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │ S1  │ Agent-Mechanism (source)    │  11   │ ~337  │ SOURCE DEFINITION│
  │ S2  │ Observation (heavy)         │   2   │ ~308  │ Empathy HEAVIEST │
  │ S3  │ Observation (rest) + BgPat  │   8   │  ~93  │                  │
  │ S4  │ Body-Base/Feedback/Feeling  │  13   │ ~152  │ ⚠️ P-F10        │
  │ S5  │ PFC + Collective + Misc     │  15   │  ~85  │ ⚠️ R-F1-*       │
  │ S6  │ Research (heavy)            │   7   │ ~323  │ ⚠️ Religion MIXED│
  │ S7  │ Research + Apps + Quote     │  ~25  │ ~102  │ many light files │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │     │ TOTAL                       │ ~80   │~1,400 │ 7 sessions       │
  └─────┴─────────────────────────────┴───────┴───────┴──────────────────┘

  ⭐ SESSION WORKFLOW (per session):
  ① Read plan cluster → identify files
  ② Per file: read → 9-pass replace_all → verify grep = 0
  ③ MIXED files: manual per-occurrence review (no replace_all pass 8-9)
  ④ After all files: folder-wide verification grep
  ⑤ Cross-check: "Compiled Compiled", "Fresh Fresh" = 0

  ⭐ VERIFICATION (per session):
  → grep "\bF1\b" across processed folder → only Chunk Drill / Melody-Tech should remain
  → grep "Compiled Compiled" = 0
  → grep "Fresh Fresh" = 0
```

---

## §6 — GHI CHÚ BỔ SUNG

### §6.1 — So sánh với plan-reward-type-rename

```
  ┌──────────────────────┬─────────────────────┬─────────────────────┐
  │                      │ Reward Rename        │ F1/F2 Rename        │
  ├──────────────────────┼─────────────────────┼─────────────────────┤
  │ Scope                │ ~60 files, ~800 occ │ ~80 files, ~1,350   │
  │ Disambiguation       │ Reward vs Compile   │ SPM vs Chunk vs     │
  │                      │ (2 systems)         │ Melody (3 systems)  │
  │ Standalone risk      │ "A", "B" = common   │ "F1", "F2" = less   │
  │                      │ letters → HIGH risk │ common → LOWER risk │
  │ replace_all safety   │ Often safe          │ Safe EXCEPT MIXED   │
  │ Version bump         │ KHÔNG (rename only) │ KHÔNG (rename only) │
  │ Backup files         │ SKIP                │ SKIP                │
  └──────────────────────┴─────────────────────┴─────────────────────┘
```

### §6.2 — Chunk Drill F-labels: separate concern

```
  Nếu bạn muốn đổi F1/F3/F4 folder labels (sau plan này):
  → F1 → Child-Dev? Child-Chunk? Foundation?
  → F3 → External? External-Dev?
  → F4 → Internal? Internal-Processing?
  → R-F1-* → R-ChildDev-*? R-CD-*?
  → Cần plan riêng vì:
     ① Gắn với file numbering system (F1 08, F1 NT6)
     ② R-F1-* label format phải redesign
     ③ ~39 files + 90 files cross-ref = ~129 files
     ④ KHÔNG gấp — folder labels ÍT nhầm hơn SPM F1/F2
```

### §6.3 — Melody-Technology F1-F7: separate concern

```
  Religion.md, Melody-Technology-Overview.md dùng F1-F7 cho 7 functions.
  → Plan này chỉ đổi SPM F1/F2 trong Religion (MIXED context).
  → F1-F7 section labels GIỮ NGUYÊN.
  → Nếu muốn đổi → cần define tên mới cho 7 functions:
     F1=Life-Level Anchor → Anchor?
     F2=Compiled Compliance → Compliance?
     ...
  → Scope nhỏ (~3 files) nhưng cần define 7 tên mới.
```
