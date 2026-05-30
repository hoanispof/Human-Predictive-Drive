# Plan: 1A/1B Rename — 1A → Domain-Checked, 1B → Self-Referencing

```
Status:    ✅✅ ALL DONE — 19 files, ~221 replacements COMPLETE
Created:   2026-05-26
Analyzed:  2026-05-29 (deep analysis 4 clusters, all forms verified)
Scope:     19 active files, 221 replacements (Selection Pressure system)
           + 1 collision file SKIP (Imagine-Final-Evaluation.md, 7 occ sub-numbering)
           + 1 mixed file MANUAL (Collective-Body.md, 1 real + 1 "1B+" billion)
           + 20+ backup files SKIP
Approach:  CLUSTER-BY-CLUSTER (Source Definition → PFC → Feeling → Remaining)
Rules:     31 passes (29 compound + 2 standalone), "check"→"verification"
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\b1[AB]\b" = 0 trong Selection Pressure context files
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 3 lý do chính

**① 1A/1B KHÔNG MANG NGHĨA**

```
  "1B trap: Body-Knowing compiled wrong" — ai biết 1B là gì?
  → Phải tra Feeling.md §8.3 hoặc 01c §4 mỗi lần gặp

  "Self-Referencing Trap: Body-Knowing compiled wrong"
  → Ngay lập tức hiểu: chunks self-referencing (no domain verify) → trap
```

**② MỌI LẦN DÙNG ĐỀU PHẢI CHÚ THÍCH KÈM**

```
  Framework LUÔN viết:
  → "1A (domain-checked)" — nếu đủ rõ thì sao không bỏ "1A"?
  → "1B (self-referencing)" — nếu đủ rõ thì sao không bỏ "1B"?
  → "1A vs 1B: 'Mượt Thật' vs 'Mượt Giả'" — title phải dịch code

  Đã LUÔN dùng tên mô tả inline = code thừa.
```

**③ NHẤT QUÁN VỚI CONVENTION "KHÔNG VIẾT TẮT CONCEPT"**

```
  Framework convention (2026-05-23): ~2,280 replacements cho abbreviation cleanup.
  "1A/1B" = code classification, không tự mô tả = cùng vấn đề với abbreviation.
  Body-Knowing.md v1.0 (mới nhất, 2026-05-25) ĐÃ dùng inline → vẫn cần code.
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức

```
  ┌──────────┬─────────────────────┬──────────────────────────────────────────┐
  │ Hiện tại │ Tên mới             │ Lý do                                    │
  ├──────────┼─────────────────────┼──────────────────────────────────────────┤
  │ 1A       │ Domain-Checked      │ Chunks tested against domain reality.    │
  │          │                     │ "Mượt thật." Selection pressure =        │
  │          │                     │ external reality. Accuracy convergence.  │
  ├──────────┼─────────────────────┼──────────────────────────────────────────┤
  │ 1B       │ Self-Referencing    │ Chunks tested against existing chunks    │
  │          │                     │ only. "Mượt giả." Selection pressure =   │
  │          │                     │ internal coherence. NO domain verify.    │
  └──────────┴─────────────────────┴──────────────────────────────────────────┘
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Domain-Checked / Self-Referencing = CAPITALIZED + HYPHENATED (concept names)

  Short forms khi context ĐÃ RÕ:
  → "Domain-Checked" có thể rút gọn thành "checked" NẾU đã nói "domain"
  → KHÔNG viết tắt thành DC/SR

  Trong tables/formulas ngắn:
  → "Checked" / "Self-Ref" = KHÔNG DÙNG — viết đầy đủ
```

### §1.3 — Compound terms

```
  ┌────────────────────────────────────┬──────────────────────────────────────────┐
  │ Hiện tại                           │ Sau rename                               │
  ├────────────────────────────────────┼──────────────────────────────────────────┤
  │ 1A vs 1B                           │ Domain-Checked vs Self-Referencing       │
  │ 1A/1B                              │ Domain-Checked/Self-Referencing          │
  │ 1B trap                            │ Self-Referencing Trap                    │
  │ 1B Trap                            │ Self-Referencing Trap                    │
  │ 1B TRAP                            │ SELF-REFERENCING TRAP                    │
  │ 1B smooth                          │ Self-Referencing smooth                  │
  │ 1B pattern                         │ Self-Referencing pattern                 │
  │ 1A melody                          │ Domain-Checked melody                   │
  │ 1A (domain-checked)                │ Domain-Checked (bỏ annotation thừa)     │
  │ 1B (self-referencing)              │ Self-Referencing (bỏ annotation thừa)   │
  │ 1A (Domain-Real)                   │ Domain-Checked (bỏ annotation thừa)     │
  │ (1A)                               │ (Domain-Checked)                        │
  │ (1B)                               │ (Self-Referencing)                      │
  │ 1A: Domain-real selection          │ Domain-Checked selection                │
  │ 1B: Self-referencing selection     │ Self-Referencing selection              │
  │ §8.3 1A vs 1B                      │ §8.3 Domain-Checked vs Self-Referencing │
  │ §10.3 ... (1A vs 1B)               │ §10.3 ... (Domain-Checked vs            │
  │                                    │   Self-Referencing)                     │
  │ 1A — DOMAIN-REAL CHECKED           │ DOMAIN-CHECKED (bỏ code prefix)         │
  │ 1B — SELF-REFERENCING              │ SELF-REFERENCING (bỏ code prefix)       │
  └────────────────────────────────────┴──────────────────────────────────────────┘

  ĐẶC BIỆT:
  → "1A vs 1B selection pressure" → "Domain-Checked vs Self-Referencing selection pressure"
  → "1B → 1A by introducing real-checking habit"
    → "Self-Referencing → Domain-Checked by introducing real-checking habit"
```

---

## §2 — QUY TẮC THAY THẾ (REFINED 2026-05-29)

### §2.1 — Thứ tự replace (per file)

```
  ⭐ THỨ TỰ — DÀI TRƯỚC, NGẮN SAU — 30 passes total.
  ⭐ "check" → "verification" (tránh lặp check/checked).
  ⭐ Compound adjectives giữ hyphen: Domain-Checked-pattern, Self-Referencing-trained.

  ══════════════════════════════════════════════════════════════════
  PHASE A — COMPOUND (tránh partial match, longest first):
  ══════════════════════════════════════════════════════════════════

  ── A1: Paired comparisons ──
  Pass 1:  "1A vs 1B"                               → "Domain-Checked vs Self-Referencing"
  Pass 2:  "1A/1B CHECK"                             → "DOMAIN-CHECKED/SELF-REFERENCING VERIFICATION"
  Pass 3:  "1A/1B check"                             → "Domain-Checked/Self-Referencing verification"
  Pass 4:  "1A/1B distinction"                       → "Domain-Checked/Self-Referencing distinction"
  Pass 5:  "1A/1B"                                   → "Domain-Checked/Self-Referencing"

  ── A2: Trap family ──
  Pass 6:  "1B TRAP"                                 → "SELF-REFERENCING TRAP"
  Pass 7:  "1B Trap"                                 → "Self-Referencing Trap"
  Pass 8:  "1B trap"                                 → "Self-Referencing Trap"

  ── A3: Parenthetical (extended first) ──
  Pass 9:  "1B (self-referencing, no domain verify)" → "Self-Referencing (no domain verify)"
  Pass 10: "1B (self-referencing, no reality check)" → "Self-Referencing (no reality check)"
  Pass 11: "1B (self-referencing: no domain verify)" → "Self-Referencing (no domain verify)"
  Pass 12: "1A (domain-checked)"                     → "Domain-Checked"
  Pass 13: "1A (Domain-Real)"                        → "Domain-Checked"
  Pass 14: "1A (domain-real)"                        → "Domain-Checked"
  Pass 15: "1B (self-referencing)"                   → "Self-Referencing"
  Pass 16: "1B (Self-Reference)"                     → "Self-Referencing"

  ── A4: Header labels (em-dash) ──
  Pass 17: "1A — DOMAIN-REAL CHECKED:"               → "DOMAIN-CHECKED:"
  Pass 18: "1A — DOMAIN-REAL SELECTION:"              → "DOMAIN-CHECKED SELECTION:"
  Pass 19: "1A — TÍCH LŨY + CHECK REAL THƯỜNG XUYÊN:" → "DOMAIN-CHECKED — TÍCH LŨY + CHECK REAL THƯỜNG XUYÊN:"
  Pass 20: "1B — SELF-REFERENCING:"                   → "SELF-REFERENCING:"
  Pass 21: "1B — SELF-REFERENCING SELECTION:"          → "SELF-REFERENCING SELECTION:"
  Pass 22: "1B — TÍCH LŨY NHƯNG KHÔNG CHECK REAL:"   → "SELF-REFERENCING — TÍCH LŨY NHƯNG KHÔNG CHECK REAL:"

  ── A5: Compound adjectives (hyphenated) ──
  Pass 23: "1A-pattern"                              → "Domain-Checked-pattern"
  Pass 24: "1B-pattern"                              → "Self-Referencing-pattern"
  Pass 25: "1A-trained"                              → "Domain-Checked-trained"
  Pass 26: "1B-trained"                              → "Self-Referencing-trained"
  Pass 27: "1B-trapped"                              → "Self-Referencing-trapped"

  ── A6: Other compound ──
  Pass 28: "1A check"                                → "Domain-Checked verification"
  Pass 29: "Tier 1A"                                 → "Tier Domain-Checked"

  ══════════════════════════════════════════════════════════════════
  PHASE B — STANDALONE (catch remaining):
  ══════════════════════════════════════════════════════════════════
  Pass 30: "1A" → "Domain-Checked"       ⚠️ CHỈ trong Selection Pressure context
  Pass 31: "1B" → "Self-Referencing"     ⚠️ CHỈ trong Selection Pressure context

  ⚠️ PHASE B: MANUAL cho Collective-Body.md (1B+ = billion, SKIP)
  ⚠️ PHASE B: Kiểm tra kết quả trong code blocks/tables cho alignment
```

### §2.2 — PHẢI thay

```
  ① 1A/1B khi nói về Selection Pressure (domain-checked vs self-referencing)
  ② "1B Trap" / "1B trap" → "Self-Referencing Trap" (mọi file)
  ③ Headers chứa 1A/1B → đổi tương ứng
  ④ Cross-ref labels chứa 1A/1B → đổi
  ⑤ Bỏ annotation thừa: "(domain-checked)" / "(self-referencing)" sau tên mới
```

### §2.3 — KHÔNG thay

```
  ① Imagine-Final-Evaluation.md (7 occ):
     "1A. Domain Reality", "1B. Knowledge Layer", "1C. Measurability"
     → SUB-NUMBERING for evaluation dimensions → KHÁC CONCEPT HOÀN TOÀN
     → SKIP

  ② Collective-Body.md line ~595: "(1B+)"
     → = "1 BILLION+ population" → SỐ LIỆU, không phải concept
     → SKIP (chỉ rename 1 occ khác ở line ~1442)

  ③ Tất cả backup/ files → SKIP

  ④ Plan files (plan-body-knowing*.md) → LOW PRIORITY, có thể skip
```

### §2.4 — CẦN REVIEW CẨN THẬN

```
  ⚠️ Collective-Body.md (2 occ):
  → 1 occ = "1B+" (billion) → SKIP
  → 1 occ = "(1A)" domain feedback → ĐỔI
  → MANUAL: không dùng replace_all

  ⚠️ Files có "1A"/"1B" standalone (Phase B):
  → Đọc context trước khi replace
  → Especially: headers, formulas, tables
```

---

## §3 — FILE INVENTORY (ACTIVE FILES)

### §3.1 — Tổng quan

```
  Total active files cần sửa:  19 files
  Total estimated replacements: ~221
  Collision files (SKIP):       1 file (Imagine-Final-Evaluation.md)
  Plan files (LOW PRIORITY):    2 files (~11 occ)
  Backup files (SKIP):          ~10+ files

  KHÔNG SỬA:
  → Imagine-Final-Evaluation.md (sub-numbering 1A/1B/1C)
  → Mọi file trong backup/
```

### §3.2 — Session 1: SOURCE (Chunk system)

```
  ┌───┬────────────────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                                       │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │ 1 │ Chunk/Drill-Chunk/Chunk-Internal-Processing/               │  38   │ SOURCE   │
  │   │   01c-Chunk-Discovery-Lifecycle.md                         │       │          │
  │ 2 │ Chunk/Chunk.md                                             │  15   │ §10.3    │
  │ 3 │ Chunk/Drill-Chunk/Chunk-Internal-Processing/               │  12   │          │
  │   │   99-Master-Synthesis.md                                   │       │          │
  │ 4 │ Chunk/Compile-Taxonomy.md                                  │   8   │          │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                                   │  73   │ 4 files  │
  └───┴────────────────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.3 — Session 2: PFC/

```
  ┌───┬────────────────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                                       │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │ 5 │ PFC/Logic-Feeling.md                                       │  22   │          │
  │ 6 │ PFC/Logic-Feeling-Balance.md                               │  22   │          │
  │ 7 │ PFC/PFC-Function.md                                        │   4   │          │
  │ 8 │ PFC/Logic-Feeling-Failure-Examples.md                      │   3   │          │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                                   │  51   │ 4 files  │
  └───┴────────────────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.4 — Session 3: Feeling/

```
  ┌───┬────────────────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                                       │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │ 9 │ Feeling/Feeling-Literacy-Training-Draft.md                 │  27   │ Draft    │
  │10 │ Feeling/Body-Knowing.md                                    │  20   │          │
  │11 │ Feeling/Feeling-Mechanism-Deep-Draft.md                    │  16   │ Draft    │
  │12 │ Feeling/Feeling.md                                         │  16   │          │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                                   │  79   │ 4 files  │
  └───┴────────────────────────────────────────────────────────────┴───────┴──────────┘
```

### §3.5 — Session 4: Remaining + Verify

```
  ┌───┬────────────────────────────────────────────────────────────┬───────┬──────────┐
  │ # │ File                                                       │ ~occ  │ Note     │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │13 │ Chunk/Background-Pattern.md                                │   9   │          │
  │14 │ Collective/Collective-Arc-Dynamics.md                      │   4   │          │
  │15 │ Collective/Collective-Body.md                              │   1   │ ⚠️ MIXED│
  │16 │ Neural-Architecture.md                                     │   1   │          │
  │17 │ Collective/Coordination-Node.md                            │   1   │          │
  │18 │ Observation/AI-Schema-Detection.md                         │   1   │          │
  │19 │ Chunk/Drill-Chunk/Chunk-Internal-Processing/               │   1   │          │
  │   │   06-Internal-Synthesis.md                                 │       │          │
  ├───┼────────────────────────────────────────────────────────────┼───────┼──────────┤
  │   │ SUBTOTAL                                                   │  18   │ 7 files  │
  └───┴────────────────────────────────────────────────────────────┴───────┴──────────┘

  VERIFY trong session này:
  → Imagine-Final-Evaluation.md (7 occ) — confirm SKIP (sub-numbering)
  → Collective-Body.md (2 occ) — confirm 1 real + 1 "billion" false positive
```

---

## §4 — SESSION PLAN

```
  ┌─────┬───────────────────────────┬───────┬───────┬──────────────────────┐
  │ Ses │ Cluster                   │ Files │ ~Occ  │ Note                 │
  ├─────┼───────────────────────────┼───────┼───────┼──────────────────────┤
  │ S1  │ SOURCE (Chunk system)     │   4   │  ~73  │ SOURCE DEFINITION    │
  │ S2  │ PFC/                      │   4   │  ~51  │                      │
  │ S3  │ Feeling/                  │   4   │  ~79  │ 2 Draft files        │
  │ S4  │ Remaining + Verify        │   7   │  ~18  │ ⚠️ MIXED 1 file     │
  ├─────┼───────────────────────────┼───────┼───────┼──────────────────────┤
  │     │ TOTAL                     │  19   │ ~221  │ 4 sessions           │
  └─────┴───────────────────────────┴───────┴───────┴──────────────────────┘

  Estimated: 1-2 sessions thực tế (nhỏ hơn M1-M4 plan ~500 occ).
  Có thể gộp S1+S2 và S3+S4 thành 2 sessions.
```

---

## §5 — COLLISION FILES

### §5.1 — Imagine-Final-Evaluation.md (SKIP ENTIRELY)

```
  HIỆN TẠI (7 occ):
  → "1A. Domain Reality (cố định)"
  → "1B. Knowledge Layer (thay đổi, tăng tiến)"
  → "1C. Measurability (khả năng đo lường)"

  VẤN ĐỀ:
  → Đây là SUB-NUMBERING cho evaluation dimensions (1A, 1B, 1C, 2A, 2B...)
  → KHÔNG PHẢI Selection Pressure concept
  → HOÀN TOÀN KHÁC SYSTEM

  GIẢI PHÁP:
  → SKIP — không thay đổi gì
  → Sub-numbering 1A/1B/1C là convention phổ biến, không gây nhầm
     vì context hoàn toàn khác (evaluation framework vs chunk quality)
```

### §5.2 — Collective-Body.md (MIXED — 1 real, 1 false positive)

```
  Line ~595: "│ NATION (1M-    │ ... │"
             "│  1B+)          │     │"
  → "1B+" = "1 billion+ population" → SỐ LIỆU → SKIP

  Line ~1442: "domain feedback (1A) VẪN LÀ final arbiter"
  → OUR CONCEPT → ĐỔI thành "(Domain-Checked)"

  GIẢI PHÁP:
  → MANUAL: chỉ sửa line ~1442, KHÔNG dùng replace_all
```

---

## §6 — POST-RENAME VERIFY

```
  ① grep "\b1A\b" trong 19 active files = 0 (trừ Imagine-Final-Evaluation.md)
  ② grep "\b1B\b" trong 19 active files = 0 (trừ Collective-Body.md "1B+")
  ③ grep "Domain-Checked" = confirm present in renamed files
  ④ grep "Self-Referencing" = confirm present in renamed files
  ⑤ Spot-check 5 headers: confirm readable without needing to look up codes
  ⑥ Spot-check compound terms: "Self-Referencing Trap" reads naturally
```
