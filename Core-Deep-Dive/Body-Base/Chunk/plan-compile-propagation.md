# Plan: Compile Architecture Propagation

**Created**: 2026-06-01
**Status**: PLANNING
**Trigger**: Compile-Taxonomy.md v3.0 DONE → propagate architecture across framework
**Scope**: ~20+ files gate→amplifier terminology + cross-ref updates + section refines

---

## BỐI CẢNH

Compile-Taxonomy.md v3.0 (2026-06-01) reframe CỐT LÕI:
1. ALL compile = 1 Engine (Exposure → Hebbian). 3 Types = modulator configs.
2. Trust = AMPLIFIER (gradient Mức 0-5), KHÔNG phải GATE (binary).
3. Trust scope: VALUE (amplified) vs CONTENT (not amplified).
4. Multi-stream: Content/Value/Entity/Behavior song song.
5. Feedback asymmetry: D→B slow/costly, B→D fast/free.

CÁC THAY ĐỔI CẦN PROPAGATE:
- "trust gate" / "trust-gated" → "trust amplifier" / "trust-amplified"
- "gate cho external install" → "amplifier cho compile rate"
- "TRUST = GATE" → "TRUST = AMPLIFIER (gradient)"
- Compile-Taxonomy version refs: v2.0 → v3.0
- Compile-Sleep.md: PFC-Operations v1.2 → v1.3
- Optional: add architecture context (1 engine + modulators) where relevant

---

## 3 LOẠI THAY ĐỔI

```
TYPE A — TERMINOLOGY FIX (đơn giản):
  gate → amplifier, trust-gated → trust-amplified
  1-5 dòng per file. Search-replace + verify context.

TYPE B — SECTION REFINE (trung bình):
  Update section description + add architecture context.
  10-30 dòng per file. Cần đọc context rồi sửa.

TYPE C — SECTION REWRITE (lớn):
  Restructure section around new architecture.
  50+ dòng per file. Cần đọc kỹ + viết lại.
```

---

## TIER 1: CORE DEFINITION FILES (ưu tiên cao nhất)

### T1.1 — Chunk.md v2.3 §2.3 (TYPE C — rewrite subsection)

```
File: Core-Deep-Dive/Body-Base/Chunk/Chunk.md
Lines: 288-332 (trust gate subsection)
Current: "TRUST = GATE CHO EXTERNAL INSTALL" (binary language)
         + Mức 0-5 gradient table (Entity-Access ref)
Change:
  - Line 288: "TRUST = GATE" → "TRUST = AMPLIFIER (GRADIENT)"
  - Reframe: binary gate language → gradient amplifier model
  - ADD: "Gate = limit case khi multiplier → 0"
  - ADD: Trust scope (VALUE vs CONTENT) clarification
  - KEEP: Mức 0-5 table (already gradient)
  - Cross-ref: → Compile-Taxonomy.md v3.0 §3
Estimate: ~20 dòng thay đổi
```

### T1.2 — Chunk.md v2.3 §2.1 ④ (TYPE A — add reference)

```
File: Core-Deep-Dive/Body-Base/Chunk/Chunk.md
Lines: 235-239 (sleep consolidation 3 dòng)
Current: 3 dòng "Sleep consolidation (Walker 2017)"
Change: ADD "Chi tiết 6 mechanisms: Compile-Sleep.md v1.0"
Estimate: +1 dòng
```

### T1.3 — Why-Body-Knows.md v1.2 (TYPE B — terminology + refine)

```
File: Core-Deep-Dive/Body-Base/Why-Body-Knows.md
Lines: 19, 404, 460, 464, 471, 492, 510, 527, 529, 556 (~10 occurrences)
Current: "trust-gated", "trust gate", "qua trust gate"
Change:
  - "trust gate" → "trust amplifier" hoặc "trust-amplified"
  - "qua trust gate" → "qua trust amplifier"
  - "cổng cho external install" → "amplifier cho external install"
  - Line 19 (scope): update pathway 2b description
  - Line 527 heading: reframe
Estimate: ~10-15 dòng thay đổi
```

### T1.4 — Body-Base.md v3.3 (TYPE B — terminology + ref update)

```
File: Core-Deep-Dive/Body-Base/Body-Base.md
Lines: 487, 593, 632, 916, 925
Current: "trust gate" in table, "E4 — chưa viết" references
Change:
  - "trust gate" → "trust amplifier" (table columns)
  - "E4 — chưa viết" → "Compile-Taxonomy.md v3.0" reference
  - §4.2: update summary to reflect v3.0 architecture
Estimate: ~10 dòng thay đổi
```

### T1.5 — Collective-Body.md v2.1 (TYPE B — terminology)

```
File: Core-Deep-Dive/Collective/Collective-Body.md
Lines: 267, 984, 1348
Current: "trust gate", "trust-gated SHORT"
Change:
  - "gate cho external install" → "amplifier cho compile rate"
  - "trust-gated" → "trust-amplified"
Estimate: ~5 dòng thay đổi
```

### T1.6 — Collective.md (TYPE B — terminology)

```
File: Core-Deep-Dive/Collective/Collective.md
Lines: 269, 291, 371, 696
Current: "TRUST GATE", "trust gate → cá nhân compile"
Change:
  - "TRUST GATE" → "TRUST AMPLIFIER"
  - "trust gate → compile" → "trust amplifier → compile"
  - Line 696: Body-Base ref update
Estimate: ~5 dòng thay đổi
```

---

## TIER 2: CORE FRAMEWORK FILES (ưu tiên cao)

### T2.1 — Core-Software.md (TYPE A — terminology)

```
File: Core-Software.md
Lines: 19, 534, 548, 1614
Current: "trust gate" references
Change: gate → amplifier at each location
Estimate: ~4 dòng
```

### T2.2 — Cortisol-Baseline.md v2.2 (TYPE A — terminology)

```
File: Core-Deep-Dive/Body-Base/Cortisol-Baseline.md
Line: 314
Current: "Trust-Injected (dạy/share qua trust gate)"
Change: "qua trust gate" → "qua trust amplifier"
Estimate: 1 dòng
```

### T2.3 — Blackbox-Map.md (TYPE A — terminology)

```
File: Core-Deep-Dive/Blackbox-Map.md
Line: 507
Current: "trust gate → compile"
Change: gate → amplifier
Estimate: 1 dòng
```

### T2.4 — Gap-Distribution-Profile.md (TYPE A — terminology)

```
File: Core-Deep-Dive/Body-Base/Body-Feedback/Gap-Distribution-Profile.md
Line: 1290
Current: "DIRECT install qua trust gate"
Change: gate → amplifier
Estimate: 1 dòng
```

### T2.5 — Compile-Sleep.md v1.0 (TYPE A — version fix)

```
File: Core-Deep-Dive/Body-Base/Chunk/Compile-Sleep.md
Lines: 864, 1225
Current: "PFC-Operations.md v1.2" (should be v1.3)
         "Compile-Taxonomy.md v2.0" (should be v3.0)
Change: version numbers update
Estimate: 2-3 dòng
```

### T2.6 — Learning-Cycle.md §4.10 (TYPE A — cross-ref)

```
File: Drill-Chunk/09-Learning-Cycle.md
Current: Recommends expanding Chunk.md §2 mode 4
Change: ADD "Implemented → Compile-Sleep.md v1.0"
Estimate: +1 dòng
```

---

## TIER 3: RESEARCH APPLICATION FILES (ưu tiên trung bình)

### T3.1 — AI-Schema-Detection.md (TYPE A — terminology + version)

```
Lines: 47, 707, 1648
Change: "trust gate" → "trust amplifier", Chunk.md v2.1 → v2.3
Estimate: ~3 dòng
```

### T3.2 — AI-Self-Model.md (TYPE A — terminology + version)

```
Lines: 203, 287, 558, 1481
Change: "trust gate" → "trust amplifier", v2.0 → v3.0
Estimate: ~4 dòng
```

### T3.3 — Social-Calibration.md (TYPE A — terminology)

```
Lines: 209, 324, 1321, 1421
Change: "trust gate" → "trust amplifier"
Estimate: ~4 dòng
```

### T3.4 — Religion.md v2.6 (TYPE A — terminology)

```
Lines: 205, 1952
Change: "trust gate" → "trust amplifier"
Estimate: ~2 dòng
```

### T3.5 — Self-Created-Threat.md (TYPE A — terminology + version)

```
Lines: 31, 153, 939
Change: "trust gate" → "trust amplifier", v2.0 → v3.0
Estimate: ~3 dòng
```

### T3.6 — Innovation-Geography.md (TYPE A — terminology)

```
Lines: 818, 1151
Change: "trust gate" → "trust amplifier"
Estimate: ~2 dòng
```

### T3.7 — Compile-Type-Learning.md (TYPE B — terminology)

```
Lines: 45, 767, 774, 886, 1134, 1168
Change: "trust gate" → "trust amplifier" (6 occurrences)
Note: Education file — may benefit from architecture context
Estimate: ~6 dòng
```

### T3.8 — Body-Feedback Drill 01-Foundation.md (TYPE A)

```
Lines: 451, 462
Change: "trust gate" → "trust amplifier"
Estimate: ~2 dòng
```

---

## TIER 4: VERSION REFERENCE UPDATES (ưu tiên thấp)

```
Các file reference "Compile-Taxonomy.md v2.0" → update to "v3.0":
  - 01-File-Index.md
  - Ask-AI.md
  - PFC-Operations.md (nếu có ref)
  - Reward-Signal-Architecture.md
  - Hidden-Quality-Perception.md
  - Và ~30+ files khác

APPROACH: Batch search-replace sau khi Tier 1-3 done.
Có thể dùng PowerShell script cho batch update.
```

---

## THỨ TỰ THỰC HIỆN

```
Session 1: TIER 1 (6 files — core definitions)
  T1.1 Chunk.md §2.3 (TYPE C — rewrite trust section)
  T1.2 Chunk.md §2.1 ④ (add sleep ref)
  T1.3 Why-Body-Knows.md (TYPE B — 10 occurrences)
  T1.4 Body-Base.md (TYPE B — table + refs)
  T1.5 Collective-Body.md (TYPE B)
  T1.6 Collective.md (TYPE B)

Session 2: TIER 2 + TIER 3 (14 files — terminology fixes)
  T2.1-T2.6 (6 files, mostly TYPE A)
  T3.1-T3.8 (8 files, mostly TYPE A)

Session 3: TIER 4 + CLEANUP
  Batch version ref updates (~30+ files)
  Move drill + plan files → backup/
  Verify cross-refs
  Final quality check

ALTERNATIVE: Nếu Tier 1 nhanh, có thể merge Session 1+2.
```

---

## TỔNG QUAN SỐ LIỆU

```
Tier 1: 6 files, ~55 dòng thay đổi (1 TYPE C, 4 TYPE B, 1 TYPE A)
Tier 2: 6 files, ~10 dòng thay đổi (all TYPE A)
Tier 3: 8 files, ~26 dòng thay đổi (mostly TYPE A)
Tier 4: ~30+ files, version ref updates (batch)

TOTAL: ~50+ files, ~90+ dòng thay đổi + batch version updates
```

---

## QUALITY CHECKLIST (per session)

```
□ Mỗi "gate" thay đổi verified in context (không phải "gate" kỹ thuật khác)
□ "trust-gated" → "trust-amplified" consistent
□ Version refs accurate (v3.0, v2.3, v1.3, etc.)
□ Mỗi file changed → verify no broken cross-refs
□ Không add content mới ngoài scope (chỉ propagate)
□ Compile-Taxonomy.md v3.0 §3 referenced where trust reframe explained
□ "Gate = limit case of amplifier" noted where helpful
```

---

## LƯU Ý QUAN TRỌNG

```
1. Drill files (Drill-*.md) KHÔNG cần update — sẽ move to backup/ trong Phase D.
2. Backup files KHÔNG cần update — preserved as historical.
3. "gate" trong context KHÁC (ví dụ: "thalamic gating" cho sleep) KHÔNG thay đổi.
   Chỉ thay đổi "gate" trong context TRUST + COMPILE.
4. Một số file dùng "trust-gated" như compound adjective.
   → Thay bằng "trust-amplified" hoặc rewrite phrase tùy context.
5. Nếu phát hiện file cần rewrite section lớn hơn dự kiến,
   ghi nhận và defer sang session riêng.
```

---

**NEXT**: Compact session → Session 1: Tier 1 (6 core files)
