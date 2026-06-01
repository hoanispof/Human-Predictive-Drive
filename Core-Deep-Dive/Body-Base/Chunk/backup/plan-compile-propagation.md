# Plan: Compile Architecture Propagation

**Created**: 2026-06-01
**Refined**: 2026-06-01 (v2.0 — scan toàn bộ framework, verified line numbers, expanded Tier 3+4)
**Completed**: 2026-06-01
**Status**: ✅✅ ALL COMPLETE
**Trigger**: Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0 DONE → propagate across framework
**Scope**: ~35+ files, ~130+ edits. trust gate→amplifier + 60+ version refs + section rewrites

RESULTS:
  Phase 1 (6 core files): Chunk.md, Body-Base.md, Why-Body-Knows.md, Collective.md, Collective-Body.md — TYPE C+B rewrites
  Phase 2 (15 files): Core-Software, Cortisol-Baseline, Blackbox-Map, Gap-Distribution-Profile, AI-Schema-Detection, AI-Self-Model, Social-Calibration, Religion, Self-Created-Threat, Innovation-Geography, Compile-Type-Learning, Expansion-Saturation-Crisis, Collective-Schema-Pressure, Addiction-Analysis, 01-Foundation.md
  Phase 3 (22+ files): Batch v2.0→v3.0 version refs + PFC-Operations v1.2→v1.3 + section number mapping
  Verification: 0 active files with "trust gate" or "Compile-Taxonomy.md v2.0" remaining

---

## BỐI CẢNH

Compile-Taxonomy.md v3.0 (2026-06-01) reframe CỐT LÕI:
1. ALL compile = 1 Engine (Exposure → Hebbian). 3 Types = modulator configs.
2. Trust = AMPLIFIER (gradient Mức 0-5), KHÔNG phải GATE (binary).
3. Trust scope: VALUE (amplified) vs CONTENT (not amplified).
4. Multi-stream: Content/Value/Entity/Behavior song song.
5. Feedback asymmetry: Entity-Valence→PFC fast/free, PFC→Entity-Valence slow/costly.
6. Sleep = Sleep Maintenance (6 offline mechanisms), NOT "exposure source."

CÁC THAY ĐỔI CẦN PROPAGATE:
- "trust gate" / "trust-gated" → "trust amplifier" / "trust-amplified"
- "gate cho external install" → "amplifier cho external compile rate"
- "TRUST = GATE" → "TRUST = AMPLIFIER (GRADIENT)"
- "cổng cho external install" → "amplifier cho external install"
- Compile-Taxonomy version refs: v2.0 → v3.0
- PFC-Operations version refs: v1.2 → v1.3 (where outdated)
- ADD: Compile-Sleep.md v1.0 reference ở Chunk.md §2.1 ④
- ADD: "Compile-Taxonomy.md v3.0" thay cho "E4 — chưa viết" ở Body-Base.md
- Optional: add architecture context (1 engine + modulators) where relevant

---

## 3 LOẠI THAY ĐỔI

```
TYPE A — TERMINOLOGY FIX (đơn giản):
  gate → amplifier, trust-gated → trust-amplified, version refs
  1-5 dòng per file. Search-replace + verify context.

TYPE B — SECTION REFINE (trung bình):
  Update section description + add architecture context.
  5-30 dòng per file. Cần đọc context rồi sửa.

TYPE C — SECTION REWRITE (lớn):
  Restructure section around new architecture.
  30+ dòng per file. Cần đọc kỹ + viết lại.
```

---

## EXCLUSION RULES

```
KHÔNG THAY ĐỔI:
  ① backup/ folders — preserved as historical
  ② Drill-*.md files — sẽ move to backup/, không cần update
  ③ "gate" trong context KHÁC trust:
     - Body-Base.md L806: "gain/speed/gate cho mạch chính" (neural modulation)
     - Connection.md L1471: "Valence = gate cho Resonance" (different concept)
     - Compile-Sleep.md: "thalamic gating" (sleep sensory block)
     - Mọi "gating" trong neurochemistry context (associative gating, etc.)
  ④ plan-*.md files — plan files tự update khi plan hoàn thành
```

---

## PHASE 1: CORE DEFINITION FILES (ưu tiên cao nhất — 6 files)

### P1.1 — Chunk.md §2.3 REWRITE (TYPE C)

```
File: Core-Deep-Dive/Body-Base/Chunk/Chunk.md
Section: §2.3 Trust subsection (Lines 288-331)
Version: v2.3 → giữ v2.3 (internal refine, chưa đủ thay đổi cho v2.4)

CURRENT (L288):
  ⭐ TRUST = GATE CHO EXTERNAL INSTALL (Drill §4, §20 — GAP 6):

REWRITE SCOPE:
  - L288 header: "GATE" → "AMPLIFIER (GRADIENT)"
  - L290-293: reframe "CHỈ compile khi có TRUST" → gradient model
    + Content VẪN compile khi trust thấp (Exposure alone)
    + Trust amplify VALUE compile rate, KHÔNG gate content
  - L309-313: Entity-Access gradient đã đúng — GIỮ nguyên
  - L331: "Trust gate formalization" → "Trust amplifier formalization"
  - ADD: "Gate = limit case khi multiplier → 0" (reconcile với existing text)
  - ADD: Trust scope VALUE vs CONTENT (1-2 dòng)
  - ADD: Cross-ref → Compile-Taxonomy.md v3.0 §3
  - REMOVE: "(Drill §4, §20 — GAP 6)" source tag (drills → backup)
  - KEEP: 5 trust sources (L294-299) — unchanged
  - KEEP: Trust = valence meta-dimension (L301-307) — unchanged
  - KEEP: Entity-Access gradient (L309-314) — unchanged
  - KEEP: Trust compile = cùng 4 cơ chế (L316-321) — unchanged
  - KEEP: Trust break (L322-328) — unchanged

Estimate: ~15 dòng thay đổi trong ~44 dòng section
```

### P1.2 — Chunk.md §2.1 ④ Sleep ref (TYPE A)

```
File: Core-Deep-Dive/Body-Base/Chunk/Chunk.md
Lines: 235-239

CURRENT (L238):
  → "Sáng mai rõ hơn" = vô thức ĐÃ xử lý trong đêm

ADD after L238:
  → Chi tiết 6 mechanisms: Compile-Sleep.md v1.0

Estimate: +1 dòng
```

### P1.3 — Body-Base.md §3 COMPONENT 3 + §4.2 + §7 (TYPE B+)

```
File: Core-Deep-Dive/Body-Base/Body-Base.md
Version: v3.3 → giữ v3.3 (terminology fix, chưa đủ cho v3.4)

LOCATION 1 — §3 COMPONENT 3 header + 3 functions (L487-509):
  CURRENT (L487):
    │ COMPONENT 3 (BRIDGE) — TRUST: GATE + MODULATE + CONNECT         │
  CHANGE:
    │ COMPONENT 3 (BRIDGE) — TRUST: AMPLIFY + MODULATE + CONNECT       │

  CURRENT (L493-494):
    │   3 FUNCTIONS:                                                   │
    │     GATE: trust = cổng cho external install chunks               │
  CHANGE:
    │   3 FUNCTIONS:                                                   │
    │     AMPLIFY: trust = amplifier cho external compile rate (gradient Mức 0-5) │

LOCATION 2 — §4.2 Trust Compile (L617-632):
  CURRENT (L617):
    ⚠️ TRUST = GATE CHO TRUST COMPILE (Drill §4, §20):
  CHANGE:
    ⚠️ TRUST = AMPLIFIER CHO TRUST COMPILE (gradient Mức 0-5):

  CURRENT (L620):
    → Cá nhân NHẬN từ tập thể qua TRUST gate
  CHANGE:
    → Cá nhân NHẬN từ tập thể qua trust amplifier

  CURRENT (L632):
    Chi tiết taxonomy: Compile-Taxonomy.md (E4 — chưa viết)
  CHANGE:
    Chi tiết taxonomy: Compile-Taxonomy.md v3.0

LOCATION 3 — §7 table (L916, L925):
  CURRENT (L916):
    │ trực tiếp            │ qua trust gate           │
  CHANGE:
    │ trực tiếp            │ qua trust amplifier      │

  CURRENT (L925):
    │ KHÔNG cần trust gate │ CẦN trust gate           │
  CHANGE:
    │ KHÔNG cần trust amplifier │ CẦN trust amplifier      │

NOTE: L806 "gain/speed/gate" = neural modulation context → KHÔNG THAY ĐỔI.

Estimate: ~10 dòng thay đổi
```

### P1.4 — Why-Body-Knows.md §scope + §3.2-§3.2b (TYPE B)

```
File: Core-Deep-Dive/Body-Base/Why-Body-Knows.md
Version: v1.2 → giữ v1.2

10 OCCURRENCES — thay lần lượt:

  L19 (scope):
    OLD: + 2b Trust-Injected (external sources): trust-gated, thinner, faster
    NEW: + 2b Trust-Injected (external sources): trust-amplified, thinner, faster

  L404:
    OLD: 2b: Trust-Injected — entities khác TRUYỀN chunks qua trust gate
    NEW: 2b: Trust-Injected — entities khác TRUYỀN chunks qua trust amplifier

  L460 (table cell):
    OLD: │ trực tiếp            │ qua trust gate           │
    NEW: │ trực tiếp            │ qua trust amplifier      │

  L464 (table cell):
    OLD: │ KHÔNG cần trust gate │ CẦN trust gate           │
    NEW: │ KHÔNG cần trust amplifier │ CẦN trust amplifier      │

  L471:
    OLD: → KHÁC ở: multi-modal richness × domain-verify count × trust-gate.
    NEW: → KHÁC ở: multi-modal richness × domain-verify count × trust amplifier.

  L492:
    OLD: → KHÔNG cần trust gate (domain nói TRỰC TIẾP qua sensory)
    NEW: → KHÔNG cần trust amplifier (domain nói TRỰC TIẾP qua sensory)

  L510:
    OLD: → KHÔNG CẦN trust gate (observed pattern, not claim cần evaluate)
    NEW: → KHÔNG CẦN trust amplifier (observed pattern, not claim cần evaluate)

  L527 (heading):
    OLD: ⭐ 2b = ENTITY KHÁC TRUYỀN CHUNKS → BODY COMPILE QUA TRUST GATE:
    NEW: ⭐ 2b = ENTITY KHÁC TRUYỀN CHUNKS → BODY COMPILE QUA TRUST AMPLIFIER:

  L529:
    OLD: Ai đó EXPLICITLY communicate "X là Y" → body nhận → trust gate evaluate
    NEW: Ai đó EXPLICITLY communicate "X là Y" → body nhận → trust amplifier evaluate

  L556:
    OLD: → CẦN trust gate (Chunk.md §2.3: trust = cổng cho external install)
    NEW: → CẦN trust amplifier (Chunk.md §2.3: trust = amplifier cho external compile rate)

  L568:
    OLD: 🟡 Trust-gate as 2b mechanism = framework synthesis (Chunk.md §2.3)
    NEW: 🟡 Trust amplifier as 2b mechanism = framework synthesis (Chunk.md §2.3)

Estimate: 11 dòng thay đổi
```

### P1.5 — Collective.md §3.1 + §6 (TYPE B)

```
File: Core-Deep-Dive/Collective/Collective.md

  L269 (heading):
    OLD: ⭐ COLLECTIVE INSTALL CHUNKS VÀO CÁ NHÂN QUA TRUST GATE:
    NEW: ⭐ COLLECTIVE INSTALL CHUNKS VÀO CÁ NHÂN QUA TRUST AMPLIFIER:

  L291:
    OLD: → = INSTALL mechanism: collective → trust gate → cá nhân compile SHORT
    NEW: → = INSTALL mechanism: collective → trust amplifier → cá nhân compile SHORT

  L371:
    OLD: → TẤT CẢ 5 yêu cầu trust gate (Collective-Body.md §5)
    NEW: → TẤT CẢ 5 yêu cầu trust amplifier (Collective-Body.md §5)

  L696:
    OLD: Body-Base.md §3 Component 3: Trust = gate cho external install.
    NEW: Body-Base.md §3 Component 3: Trust = amplifier cho external compile rate.

Estimate: 4 dòng thay đổi
```

### P1.6 — Collective-Body.md §3 + §5.2 + §8 (TYPE B)

```
File: Core-Deep-Dive/Collective/Collective-Body.md

  L267:
    OLD: Trust: gate cho external install (Trust Compile)
    NEW: Trust: amplifier cho external compile rate (Trust Compile)

  L984:
    OLD: Individual compile: [học → tốt] (trust-gated SHORT)
    NEW: Individual compile: [học → tốt] (trust-amplified SHORT)

  L1348:
    OLD: → AI CÓ THỂ detect compile source (internal? external? trust-gated?)
    NEW: → AI CÓ THỂ detect compile source (internal? external? trust-amplified?)

Estimate: 3 dòng thay đổi
```

---

## PHASE 2: CORE FRAMEWORK + RESEARCH FILES (20+ files, mostly TYPE A)

### TIER 2 — Core Framework (6 files)

```
T2.1 — Core-Software.md (4 occurrences):
  L19:  "trust gate" → "trust amplifier"
  L534: "TRUST GATE" → "TRUST AMPLIFIER"
  L548: "trust gate → compile" → "trust amplifier → compile"
  L1614: "trust gate" → "trust amplifier"

T2.2 — Cortisol-Baseline.md (1 occurrence):
  L314: "qua trust gate" → "qua trust amplifier"

T2.3 — Blackbox-Map.md (1 occurrence):
  L507: "trust gate → compile" → "trust amplifier → compile"

T2.4 — Gap-Distribution-Profile.md (1 occurrence):
  L1290: "qua trust gate" → "qua trust amplifier"

T2.5 — Compile-Sleep.md v1.0 (version refs only):
  (Verify: no "trust gate" occurrences — confirmed by scan)
  (PFC-Operations v1.2 refs already at v1.3 in file — verify)

T2.6 — Learning-Cycle.md (cross-ref add):
  (Verify location, ADD "→ Implemented: Compile-Sleep.md v1.0")
```

### TIER 3 — Research + Application Files (16+ files)

```
GROUP A — TRUST GATE TERMINOLOGY:

T3.1 — AI-Schema-Detection.md (3 occ):
  L47, L707, L1648: "trust gate/trust-gated" → "trust amplifier/trust-amplified"

T3.2 — AI-Self-Model.md (4 occ):
  L47, L203, L287, L558, L1481: "trust gate" → "trust amplifier"

T3.3 — Social-Calibration.md (4 occ):
  L209, L324, L1391, L1921: "trust gate" → "trust amplifier"

T3.4 — Religion.md v2.6 (2 occ):
  L205: "Trust = gate cho install" → "Trust = amplifier cho install"
  L1952: "trust-gated" → "trust-amplified"

T3.5 — Self-Created-Threat.md (2 occ + version):
  L31, L153, L939: "trust gate" → "trust amplifier", v2.0 → v3.0

T3.6 — Innovation-Geography.md (2 occ):
  L818, L1151: "trust gate" → "trust amplifier"

T3.7 — Compile-Type-Learning.md (6 occ + version):
  L45, L767, L774, L886, L1134, L1168: "trust gate" → "trust amplifier"
  L44, L1167: Compile-Taxonomy v2.0 → v3.0

T3.8 — Expansion-Saturation-Crisis.md (2 occ):
  L155: "trust-gated" → "trust-amplified"
  L1710: "trust-gated" → "trust-amplified"

T3.9 — Collective-Schema-Pressure.md (1 occ):
  L125: "TRUST GATE" → "TRUST AMPLIFIER"

T3.10 — Addiction-Analysis.md (1 occ + version):
  L26: "trust gate" → "trust amplifier"
  L32: Compile-Taxonomy v2.0 → v3.0

T3.11 — Body-Feedback Drill 01-Foundation.md (3 occ):
  L444, L451, L462: "trust gate/TRUST GATE" → "trust amplifier/TRUST AMPLIFIER"
  NOTE: Drill file — cân nhắc skip nếu sắp move backup.


GROUP B — VERSION REF ONLY (NO trust gate):

  (These files have Compile-Taxonomy v2.0 refs but NO trust gate terminology)
  → Defer to Phase 3 batch update.
```

---

## PHASE 3: BATCH VERSION REFS + CLEANUP (~35+ files)

```
BATCH 1 — "Compile-Taxonomy.md v2.0" → "Compile-Taxonomy.md v3.0":

  Known files (from scan):
    Ask-AI.md (L776)
    PFC-Operations.md (L34, L1102)
    PFC-Hardware.md (L975)
    PFC-Configuration.md (L1295)
    Core-Software.md (L36, L538, L1615) — may overlap Phase 2
    Body-Feedback-Precondition.md (L40, L832, L1398)
    Reward-Signal-Architecture.md (L35, L1996)
    Hidden-Quality-Perception.md (L45, L1706)
    AI-Schema-Detection.md (L36, L497, L561, L1662-1663, L1746)
    AI-Collective-Detection.md (L395, L723)
    AI-Self-Model.md (L47, L1481) — overlap Phase 2
    Social-Calibration.md — overlap Phase 2
    Self-Created-Threat.md (L31, L939) — overlap Phase 2
    Religion.md (L52, L1126, L2095)
    ADHD-Attention-Optimization.md (L35, L725, L933, L1180)
    ADHD-Trade-Off.md (L29, L254, L356, L383, L429, L585, L1262)
    Expansion-Saturation-Crisis.md (L45, L164, L1714)
    Addiction-Analysis.md (L32, L1135)
    Alzheimer-Analysis.md (L2972)
    Compile-Type-Learning.md (L44, L1167) — overlap Phase 2
    Money-Education.md (L59)
    Money-Analysis.md (L56)
    Collective-Schema-Pressure.md (L22, L729)
    Quote-Analysis/Work-Think-Act-Become-Cluster.md (L30)
    plan-tech-post.md (L314, L327)

  APPROACH:
    PowerShell grep "Compile-Taxonomy.md v2.0" (exclude backup/) → replace v3.0
    Sau replace: verify mỗi file → no broken context.

BATCH 2 — "PFC-Operations.md v1.2" → "PFC-Operations.md v1.3":

  Known files:
    Auditory-Hardware.md (L714)
    Body-Feedback-Mechanism.md (L1473)
  (2 files only — manual replace)

BATCH 3 — "Chunk.md v2.1" → "Chunk.md v2.3" (where outdated):

  Known files with v2.1 refs:
    AI-Schema-Detection.md (L47, L1648)
    Compile-Type-Learning.md (L45, L1168)
    Addiction-Analysis.md (L26)
  APPROACH: Verify context trước khi update — some refs may be intentional historical.

CLEANUP:
  □ Move plan file → backup/ khi hoàn thành
  □ Verify File-Index.md (01-File-Index.md) version refs
  □ Final grep "trust gate" (exclude backup/) → should return 0
  □ Final grep "Compile-Taxonomy.md v2.0" (exclude backup/) → should return 0
```

---

## THỨ TỰ THỰC HIỆN

```
Phase 1 (session này): TIER 1 — 6 core definition files
  P1.1 Chunk.md §2.3 (TYPE C — rewrite trust section)
  P1.2 Chunk.md §2.1 ④ (TYPE A — add sleep ref)
  P1.3 Body-Base.md §3+§4.2+§7 (TYPE B+ — trust component + refs)
  P1.4 Why-Body-Knows.md (TYPE B — 11 occurrences)
  P1.5 Collective.md (TYPE B — 4 occurrences)
  P1.6 Collective-Body.md (TYPE B — 3 occurrences)

Phase 2 (session này hoặc sau): TIER 2 + TIER 3 — 20+ files TYPE A/B
  Mostly 1-5 dòng per file. Can execute in batches.

Phase 3 (session sau): TIER 4 — batch version refs + cleanup
  PowerShell scripted for version ref updates.
  Final verification grep.
```

---

## TỔNG QUAN SỐ LIỆU (REFINED)

```
Phase 1: 6 files, ~45 dòng thay đổi (1 TYPE C, 4 TYPE B, 1 TYPE A)
Phase 2: 17+ files, ~45 dòng thay đổi (mostly TYPE A)
Phase 3: 25+ files, 60+ version ref updates (batch) + cleanup

TOTAL: ~55+ files, ~150+ thay đổi
```

---

## QUALITY CHECKLIST (per phase)

```
□ Mỗi "gate" thay đổi verified in context (không phải "gate" kỹ thuật khác)
□ "trust-gated" → "trust-amplified" consistent
□ Version refs accurate (v3.0, v2.3, v1.3, etc.)
□ Mỗi file changed → verify no broken cross-refs
□ Không add content mới ngoài scope (chỉ propagate)
□ Compile-Taxonomy.md v3.0 §3 referenced where trust reframe explained
□ "Gate = limit case of amplifier" noted where helpful (Chunk.md §2.3 only)
□ Tables: column widths still align after changes
□ No substring collision (verify "trust amplifier" not creating duplicates)
```

---

## LƯU Ý QUAN TRỌNG

```
1. Drill files (Drill-*.md) — cân nhắc skip nếu sắp move backup.
   Exception: 01-Foundation.md nếu vẫn active reference.
2. Backup files KHÔNG cần update — preserved as historical.
3. "gate" trong context KHÁC → KHÔNG thay đổi (xem EXCLUSION RULES).
4. "trust-gated" như compound adjective → "trust-amplified."
5. Nếu phát hiện file cần rewrite section lớn hơn dự kiến,
   ghi nhận vào plan + defer sang session riêng.
6. Compile-Taxonomy.md v3.0 CHÍNH NÓ references "TRUST = GATE" trong §3.1
   (as "contradiction detected") — đây là HISTORICAL QUOTE, KHÔNG thay đổi.
```

---

**STATUS**: ✅✅ ALL COMPLETE (2026-06-01)
