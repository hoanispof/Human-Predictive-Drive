# Plan: H-Label Rename — H10 → Body-Signal-Precondition (+ H11 secondary)

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~87 active files, ~522 replacements (H10 primary)
           + H11 secondary (~38 files if confirmed)
Approach:  SINGLE CONCEPT (H10 is the only H-label used cross-file as concept name)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\bH10\b" = 0 trong active files
Special:   H10 đã CÓ inline description hầu hết nơi — risk thấp
```

---

## §0 — TẠI SAO ĐỔI TÊN

**① "H10" LÀ HYPOTHESIS NUMBER, KHÔNG MANG NGHĨA**

```
  "H10 5 preconditions" — ai biết H10 nghĩa gì?
  → Phải tra 99-Master-Synthesis.md hoặc Body-Feedback/ files

  "Body-Signal-Precondition (5 factors)" — tự giải thích
  → Body phát signal → 5 preconditions quyết định signal nào
```

**② H10 XUẤT HIỆN Ở 87 FILES — quá rộng cho 1 hypothesis number**

```
  H10 không còn là provenance marker — nó ĐÃ THÀNH concept name.
  → Dùng như: "H10 Precondition", "H10 check", "H10 5 factors"
  → Đáng có tên riêng.
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — H10 → Body-Signal-Precondition

```
  Source: Body-Feedback/04-Integration.md §9, Body-Feedback.md §6

  ┌──────────┬───────────────────────────┬──────────────────────────────┐
  │ Hiện tại │ Tên mới                   │ Nghĩa                        │
  ├──────────┼───────────────────────────┼──────────────────────────────┤
  │ H10      │ Body-Signal-Precondition  │ Body signal (reward/         │
  │          │                           │ dissonance/neutral) là       │
  │          │                           │ deterministic function của    │
  │          │                           │ 5 preconditions:             │
  │          │                           │ P1: Schema pending state     │
  │          │                           │ P2: Chunks base adequacy     │
  │          │                           │ P3: Prediction-delta         │
  │          │                           │ P4: Coherence/beauty         │
  │          │                           │ P5: Chunk association tag    │
  └──────────┴───────────────────────────┴──────────────────────────────┘

  Compound terms:
  → "H10 5 preconditions" → "5 Body-Signal-Preconditions"
  → "H10 Precondition Hypothesis" → "Body-Signal-Precondition Hypothesis"
  → "H10 check" → "Body-Signal-Precondition check"
  → "H10" standalone → "Body-Signal-Precondition"
```

### §1.2 — H11 (secondary) → Receptive-Productive-Gap

```
  Source: 99-Master-Synthesis.md, = NT5

  ┌──────────┬──────────────────────────┬──────────────────────────────┐
  │ Hiện tại │ Tên mới                  │ Nghĩa                        │
  ├──────────┼──────────────────────────┼──────────────────────────────┤
  │ H11      │ Receptive-Productive-Gap │ Productive bundle ≈ 3×       │
  │          │                          │ receptive bundle. Asymmetry  │
  │          │                          │ giữa hiểu và nói/làm.       │
  └──────────┴──────────────────────────┴──────────────────────────────┘

  ⚠️ H11 có collision risk: "\bH11\b" có thể match non-hypothesis text
  → Cần verify actual H11 count trước khi thực hiện
  → Priority THẤP hơn H10
```

### §1.3 — H1-H9, H12: SCOPE RIÊNG

```
  H1-H9, H12 chủ yếu dùng LOCAL trong Chunk drill files.
  → Ít cross-file references
  → Collision HIGH (H1-H9 match markdown headers, HTML, etc.)
  → KHÔNG trong scope plan này — plan riêng nếu cần
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — Replace_all passes (per file)

```
  ⭐ THỨ TỰ:

  Pass 1: "H10 5 preconditions"     → "5 Body-Signal-Preconditions"
  Pass 2: "H10 Precondition"        → "Body-Signal-Precondition"
  Pass 3: "H10 preconditions"       → "Body-Signal-Preconditions"
  Pass 4: "H10 precondition"        → "Body-Signal-Precondition"
  Pass 5: "H10"                     → "Body-Signal-Precondition"

  ⚠️ SAU replace_all: check redundancy
  → "Body-Signal-Precondition Precondition" → sửa
  → "Body-Signal-Precondition hypothesis" → OK (keep)
```

### §2.2 — KHÔNG thay

```
  ① H1-H9, H12 — SEPARATE SCOPE
  ② Backup files — SKIP
  ③ "H10" khi nói về thứ KHÁC (nếu có) — verify context
```

---

## §3 — FILE INVENTORY (tóm tắt)

```
  ~87 active files, ~522 occurrences.
  Pattern consistent (H10 luôn = Body-Signal-Precondition).
  KHÔNG có collision (H10 chỉ có 1 nghĩa).
  → Replace_all SAFE cho TẤT CẢ files.

  HEAVY files (>10 occ): ~8 files
  → 04-Integration.md (~55), Gap-Direction.md (~24),
     Body-Feedback.md (~23), Liking-Wanting.md (~21),
     Addiction-Analysis.md (~19), ...

  LIGHT files (1-5 occ): ~60 files

  → 3-4 sessions (grouped by folder)
```
