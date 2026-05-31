# Plan: Table Abbreviation Fix — Full Names in All Tables

**Ngày tạo**: 2026-05-31
**Nguyên tắc**: Framework hạn chế TỐI ĐA viết tắt. Bảng KHÔNG được phép cắt ngắn concept names.
**Nguyên nhân**: 100% violations nằm trong box-drawing tables (``` code blocks) — cột quá hẹp.
**Phương pháp**: Mở rộng cột bảng hoặc tách multi-line cell. KHÔNG dùng abbreviation + legend.

---

## §1 — PHÂN TÍCH VẤN ĐỀ

```
2 loại bảng trong framework:

  ① PIPE TABLE (| col | col |)
     → Markdown renderer auto-resize theo nội dung
     → Viết full name = TỰ ĐỘNG vừa
     → Hiện tại KHÔNG có violation ở loại bảng này

  ② BOX-DRAWING TABLE (│ col │ col │) trong ``` code blocks
     → FIXED-WIDTH — tác giả PHẢI TỰ ĐẾM ký tự
     → Cột hẹp → cắt ngắn chữ cho vừa → viết tắt
     → 100% violations thuộc loại này

GIẢI PHÁP PER TABLE:

  Option A: MỞ RỘNG CỘT
    → Thêm padding (spaces) vào cột bị hẹp
    → Sửa ───── separator cho khớp width mới
    → Sửa TẤT CẢ rows trong bảng đó
    → Ưu: giữ nguyên aesthetics. Nhược: tedious nhưng mechanical.

  Option B: TÁCH MULTI-LINE CELL
    → Viết full name trên 2 dòng trong cùng ô
    → Đã dùng ở nhiều nơi (VD: Bond-Architecture line 836-837)
    → Ưu: không tăng width. Nhược: bảng cao hơn.

  Option C: CHUYỂN SANG PIPE TABLE (chỉ cho bảng phù hợp)
    → Thay box-drawing → pipe markdown table
    → Ưu: auto-resize, dễ maintain. Nhược: mất visual aesthetics.
    → CHỈ dùng cho bảng đơn giản (≤5 cột, ≤10 rows, không cần alignment đẹp).

  Ưu tiên: A > B > C (giữ box-drawing khi có thể)
```

---

## §2 — DANH SÁCH ĐẦY ĐỦ VIOLATIONS

### TIER 1 — Framework Concept Name (26 vị trí, 10 files) — PHẢI SỬA

| # | File | Line | Viết tắt | Full form |
|---|------|------|----------|-----------|
| 1 | Coordination-Node.md | 1961 | `Scale-Instit.` | Scale-Institutional |
| 2 | Collective.md | 622 | `Scale-Instit.` | Scale-Institutional |
| 3 | Coordination-Node.md | 433 | `Scale-Pair equiv.` | Scale-Pair equivalent |
| 4 | Coordination-Node.md | 206 | `Social-coord.` | Social-coordination |
| 5 | Resonance-Per-Entity.md | 994 | `→Struct.` | →Structural |
| 6 | Bond-Architecture.md | 837 | `Struct.` | Structural |
| 7 | Connection.md | 2568 | `GENERAT.` (×2) | GENERATIVE |
| 8 | Connection.md | 2568 | `TONIC+CYC` | TONIC+CYCLIC |
| 9 | Connection.md | 2568 | `Dom. phantom` | Dominant phantom |
| 10 | Empathy.md | 615 | `③ Schema Simul.` | ③ Schema Simulation |
| 11 | Liking-Wanting.md | 95 | `Valence-Prop. v3.0` | Valence-Propagation v3.0 |
| 12 | Liking-Wanting.md | 96 | `Direct-St.` | Direct-State |
| 13 | Reward-Signal-Architecture.md | 452 | `✅Direct-St.` | ✅Direct-State |
| 14 | Reward-Signal-Architecture.md | 456 | `✅Eval.` | ✅Evaluative |
| 15 | Work-Comparison-Thief-Of-Joy.md | 641 | `Social-Cal.` | Social-Calibration |
| 16 | Work-Comparison-Thief-Of-Joy.md | 645 | `Backgr. Pattern` | Background-Pattern |
| 17 | Work-Comparison-Thief-Of-Joy.md | 646-647 | `BG-P` (×2) | Background-Pattern |
| 18 | Threat.md | 102 | `Body-feedback diss.` | Body-feedback dissonance |
| 19 | Obligation.md | 1456 | `Oblig.` | Obligation |
| 20 | Domain-Mapping-Drive.md | 2798 | `Chunk assoc.` | Chunk association |
| 21 | Autonomy-Hardware.md | 158 | `AUTONOMY PREF.` | AUTONOMY PREFERENCE |
| 22 | Core-Software.md | 1096 | `Simulate+Constr.` | Simulate+Constructive |
| 23 | Simulation-Engine.md | 328 | `Creative Imagin.` | Creative Imagination |
| 24 | Simulation-Engine.md | 328 | `Hypothet.` | Hypothetical |
| 25 | PFC-Label.md | 347 | `Direct-State Disson.` | Direct-State Dissonance |
| 26 | Logic-Feeling.md | 1211 | `BODY-KNOWING-dom.` | BODY-KNOWING-dominant |

### TIER 2 — PFC Function/Config truncated (10 vị trí, 2 files) — NÊN SỬA

| # | File | Line | Viết tắt | Full form |
|---|------|------|----------|-----------|
| 27 | PFC-Configuration.md | 568 | `Accept Temp. Disson.` | Accept Temporary Dissonance |
| 28 | PFC-Configuration.md | 684 | `Accept Disson.` | Accept Dissonance |
| 29 | PFC-Configuration.md | 685 | `Hijack Body-In` | Hijack Body-Input |
| 30 | PFC-Configuration.md | 692 | `Enhanc.` | Enhanced |
| 31 | PFC-Configuration.md | 695 | `② Reallo` | ② Reallocation |
| 32 | PFC-Configuration.md | 696 | `③ Reconf` | ③ Reconfiguration |
| 33 | PFC-Configuration.md | 697 | `④ Discon` | ④ Disconnected |
| 34 | PFC-Configuration.md | 698 | `⑤ Hyper` | ⑤ Hyperactivated |
| 35 | PFC-Configuration.md | 699 | `⑥ Disint` | ⑥ Disintegration |
| 36 | PFC-Operations.md | 421 | `Cortisol dir.` | Cortisol direction |

### TIER 3 — Neuroscience/General terms (14 vị trí, 7 files) — XÉT CẦN

| # | File | Line | Viết tắt | Full form |
|---|------|------|----------|-----------|
| 37 | Domain-Mapping-Drive.md | 2798 | `Positive-neut.` | Positive-neutral |
| 38 | Threat.md | 340 | `Emerg.` | Emergency |
| 39 | Connection.md | 2234 | `Acquaint.` | Acquaintance |
| 40 | Connection.md | 2569 | `DEVASTAT.` | DEVASTATING |
| 41 | Core-Software.md | 267 | `interoc.` | interoception |
| 42 | Anchor-Schema-Example.md | 902 | `Unfalsif.` | Unfalsifiable |
| 43 | PTSD-Analysis.md | 1784 | `body-feedback amp.` | body-feedback amplification |
| 44 | PTSD-Analysis.md | 1789 | `Reconsol.` | Reconsolidation |
| 45 | PTSD-Analysis.md | 2214 | `DMN interfer.` | DMN interference |
| 46 | PTSD-Analysis.md | 2215 | `Emotional react.` / `Amygdala react.` | reactivity |
| 47 | OCD-Analysis.md | 402 | `Spreading activ.` | Spreading activation |
| 48 | Alzheimer-Analysis.md | 1744 | `Synaptic plast.` | Synaptic plasticity |
| 49 | Parkinson-Analysis.md | 1373 | `MAO-B inh.` / `oxidat.` / `Neuroprotect.` | terms |
| 50 | Gratitude.md | 872 | `Comp.` | Comparison |

### TIER 4 — VN-Cultural-Factors bảng + legend (3 vị trí, 1 file) — XÉT RIÊNG

| # | File | Line | Code | Full form | Note |
|---|------|------|------|-----------|------|
| 51 | VN-Cultural-Factors.md | 786 | `ImgF` | Imagine-Final | Legend defined |
| 52 | VN-Cultural-Factors.md | 786 | `3ORI` | 3 ORIGIN | Legend defined |
| 53 | VN-Cultural-Factors.md | 791 | `③Collect.` | ③Collective | Legend defined |

---

## §3 — PHƯƠNG ÁN FIX PER TABLE

```
NGUYÊN TẮC CHỌN FIX:

  1. Bảng ≤5 cột + CÓ THỂ mở rộng → Option A (widen columns)
  2. Bảng nhiều cột + 1 ô bị hẹp → Option B (multi-line cell)
  3. Bảng summary nhỏ → Option C (pipe table) CHỈ khi ≤5 cột, ≤10 rows
  4. VN-Cultural-Factors → giữ legend nhưng SỬA ③Collect. → ③Collective

THIẾT KẾ BẢNG TỐT (guideline cho tương lai):
  - Cột chứa concept name: TỐI THIỂU 22 ký tự (dài nhất: "Scale-Institutional" = 19)
  - Cột chứa PFC function: TỐI THIỂU 30 ký tự (dài nhất: "Accept Temporary Dissonance" = 27)
  - Nếu không vừa: TÁCH dòng hoặc CHUYỂN pipe table
  - KHÔNG BAO GIỜ viết tắt framework concept name để fit cột
```

---

## §4 — EXECUTION PHASES

```
Phase 1: TIER 1 files dễ (1 bảng/file, sửa nhanh)
  - Collective.md (1 fix)
  - Obligation.md (1 fix)
  - Autonomy-Hardware.md (1 fix)
  - Logic-Feeling.md (1 fix)
  - Threat.md (1 fix)
  - Domain-Mapping-Drive.md (2 fixes)
  - Core-Software.md (1 fix)
  - Liking-Wanting.md (2 fixes — diagram box, not table)
  → ~10 fixes, ~8 files

Phase 2: TIER 1 files phức tạp (nhiều fixes/bảng rộng)
  - Coordination-Node.md (3 fixes, 2 bảng khác nhau)
  - Connection.md (4 fixes, 2 bảng)
  - Empathy.md (1 fix)
  - Resonance-Per-Entity.md (1 fix — bảng rất rộng, phức tạp)
  - Bond-Architecture.md (1 fix — bảng rộng)
  - Reward-Signal-Architecture.md (2 fixes)
  - Work-Comparison-Thief-Of-Joy.md (4 fixes — 1 bảng)
  - Simulation-Engine.md (2 fixes — bảng 11 applications)
  - PFC-Label.md (1 fix)
  → ~19 fixes, ~9 files

Phase 3: TIER 2 — PFC-Configuration.md
  - 9 fixes all in 2 bảng
  - PFC-Operations.md: 1 fix
  → 10 fixes, 2 files

Phase 4: TIER 3 — Neuroscience terms (NẾU quyết định sửa)
  - 14 fixes across 7 files
  - Priority: Health-Conditions files (PTSD, OCD, Alzheimer, Parkinson)
  → Optional phase

Phase 5: TIER 4 — VN-Cultural-Factors (NẾU quyết định sửa)
  - 3 fixes, 1 file
  - Đặc biệt: bảng CỰC HẸP (8 cột × 5 chars) + có legend
  → Có thể cần redesign hoàn toàn

Phase 6: VERIFY
  - Grep tất cả patterns đã sửa
  - Confirm 0 remaining violations
```

---

## §5 — THẢO LUẬN MỞ

```
CÂU HỎI CẦN QUYẾT ĐỊNH TRƯỚC KHI SỬA:

  Q1: Tier 3 (neuroscience terms) có sửa không?
      → "Synaptic plasticity", "Reconsolidation", "interoception"
      → Đây là mainstream neuroscience terms, không phải framework concepts
      → Nhưng user nói "hạn chế tối đa viết tắt"

  Q2: VN-Cultural-Factors: giữ legend approach hay redesign?
      → Legend giải thích codes = CHO PHÉP nhưng hạn chế?
      → Hay phải viết full mỗi cell?

  Q3: Box-drawing → pipe table: bao nhiêu bảng nên chuyển?
      → Bảng mà chỉ có 2-4 cột, ≤10 rows: có thể chuyển pipe table
      → Giúp tương lai: KHÔNG CẦN đếm ký tự nữa

  Q4: Thiết kế guideline: đặt vào đâu?
      → Thêm vào CLAUDE.md? Hay ghi note ở 01-File-Index.md?
```

---

## §6 — STATUS

```
Phase 1: ✅ DONE (10 fixes, 8 files)
Phase 2: ✅ DONE (19 fixes, 9 files)
Phase 3: ✅ DONE (10 fixes, 2 files — PFC-Configuration + PFC-Operations)
Phase 4: ✅ DONE (14 fixes, 8 files — all Tier 3 neuroscience terms fixed)
         + BONUS: ADHD-Observation.md (3 fixes — same PTSD×ADHD table)
Phase 5: ✅ DONE (1 fix — ③Collect.→③Collective, legend codes kept)
Phase 6: ✅ VERIFIED — grep confirms 0 violations in active files
         (remaining matches only in backup/ and plan file itself)

TOTAL: ~57 fixes across ~20 active files. Plan CLOSED 2026-05-31.
```
