# Plan: L-Label Rename — 5 Systems × Descriptive Names

```
Status:    🔲 NOT STARTED
Created:   2026-05-23
Scope:     ~146 active files, ~3,700 replacements (5 colliding L-systems)
Approach:  SYSTEM-BY-SYSTEM (identify → rename per system)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\bL[0-7]\b" = 0 trong active files (trừ legitimate uses)
Special:   LARGEST + MOST COMPLEX rename plan. 5 systems share "L" prefix.
           MOSTLY MANUAL — nhiều files dùng 2+ L-systems.
```

---

## §0 — TẠI SAO ĐỔI TÊN

**① "L2" CÓ 5 NGHĨA KHÁC NHAU — TỆ NHẤT TRONG FRAMEWORK**

```
  "L2" xuất hiện → nghĩa nào?

  File Body-Base.md:     L2 = REMOVED (old substrate layer — DEPRECATED)
  File VP.md:            L2 = Valence-Structural (Entity-Compiled stream)
  File Ladder files:     L2 = Pattern-match activation (PFC inference)
  File By-Product-Scale: L2 = Hub/Serotonin level
  File Feeling.md:       L2 = Integration (insula + ACC, ~95% fidelity)

  → 5 concepts × 1 label = DANGEROUS
  → Reader PHẢI biết file context mới hiểu
```

**② MỘT SỐ FILES DÙNG 2-3 L-SYSTEMS CÙNG LÚC**

```
  Valence-Propagation.md: L1/L2 (luồng) + L0/L1 (substrate) + "L2 removed"
  Resonance-Per-Entity.md: L1/L2 (luồng) + old L references
  → Trong CÙNG FILE, "L1" có 2 nghĩa
```

---

## §1 — 5 HỆ THỐNG L-LABELS

### §1.1 — System A: Body-Base Substrate (CURRENT v3.0+)

```
  Source: Body-Base.md v3.2 §5

  ┌──────────┬──────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới              │ Nghĩa                            │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ L0       │ Substrate-Alive      │ Alive Threshold (binary).        │
  │          │                      │ Brainstem/D-zone. Oxygen,        │
  │          │                      │ temperature, injury, starvation. │
  │          │                      │ Suppresses all other processing. │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ L1       │ Substrate-Inputs     │ 17 Body-Input Categories with    │
  │          │                      │ adaptive baselines. 5 extero +   │
  │          │                      │ 3 proprio + 9 intero.            │
  └──────────┴──────────────────────┴──────────────────────────────────┘

  ⚠️ L2 = REMOVED (absorbed into L1 + PFC operators)
  ⚠️ L3 = REFRAMED as "PFC Operators on L1" (not separate layer)
  → Files vẫn dùng old L2/L3 = DEPRECATED → cần UPDATE nội dung

  Scope: ~19 files use current L0/L1 substrate labels
```

### §1.2 — System A-old: Body-Base Substrate (DEPRECATED v7.5)

```
  ⚠️ CÒN ~30 FILES dùng old 4-layer L0-L3:
  → L0 = Threat Channel (amygdala, survival)
  → L1 = Physiological / Interoceptive
  → L2 = Experience / Novelty (VTA dopamine) → REMOVED in v3.0
  → L3 = Mastery / Meaning / Status (PFC-mediated) → REFRAMED in v3.0

  CÁC FILES CÒN DÙNG OLD SYSTEM:
  → Feeling-Sources.md (DRAFT v1.0) — 30+ occ
  → Self-Created-Threat.md v1.0 — 12 occ
  → Emergent-Patterns.md — 21+ occ
  → Various Research/ and Observation/ files

  ACTION: KHÔNG chỉ rename — phải UPDATE NỘI DUNG để match v3.0+
  → Đây là CONTENT FIX, không chỉ label rename
  → Có thể cần plan riêng cho content update
```

### §1.3 — System B: Valence-Propagation 2-Luồng

```
  Source: Valence-Propagation.md v3.0 §5

  ┌──────────┬──────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới              │ Nghĩa                            │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ L1       │ Valence-Momentary    │ Self-Pattern-Modeling-owned.      │
  │ (luồng)  │                      │ Per-episode, transient. Has      │
  │          │                      │ metabolic cost.                  │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ L2       │ Valence-Structural   │ Entity-Compiled. Sustained,      │
  │ (luồng)  │                      │ persistent. Cost ≈ 0 (compiled). │
  └──────────┴──────────────────────┴──────────────────────────────────┘

  Formula: Burnout = f(Valence-Momentary cost / Valence-Structural compensation)

  Scope: ~22 files use L1/L2 in 2-luồng context
  Grouped: "2-luồng" → "2-luồng" (GIỮ — Vietnamese term đã established)
```

### §1.4 — System C: PFC-Inference Ladder (Child-Chunk-Development)

```
  Source: 09-Event-Chunks-Inference-Matrix.md §1.2

  ┌──────────┬──────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới              │ Nghĩa                            │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ L0       │ Ladder-Reflex        │ Pure reflex (0 chunks)           │
  │ L1       │ Ladder-Differentiated│ Reflex modulation (1-2 chunks)   │
  │ L2       │ Ladder-PatternMatch  │ Chunk fires on recognition       │
  │ L3       │ Ladder-Response      │ Pattern + crude action (3-5)     │
  │ L4       │ Ladder-Execution     │ Full plan + prediction (5-8+)    │
  └──────────┴──────────────────────┴──────────────────────────────────┘

  Scope: ~32 files (across Child-Chunk-Development/, both EN + VI)
  Note: Mostly CONTAINED within Chunk drill ecosystem
```

### §1.5 — System D: By-Product-Scale Levels

```
  Source: By-Product-Scale.md v1.0 §2-§4

  ┌──────────┬──────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới              │ Nghĩa                            │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ Level 1  │ Scale-Pair           │ A↔B. Oxytocin. Direct,           │
  │ (L1)     │                      │ personal. Max ~150 entities.     │
  │ Level 2  │ Scale-Hub            │ Node↔Collective. Serotonin.      │
  │ (L2)     │                      │ Trust bypass. Scale: millions.   │
  │ Level 3  │ Scale-Institutional  │ Distributed trust infrastructure.│
  │ (L3)     │                      │ No single node. Scale: 8B.       │
  └──────────┴──────────────────────┴──────────────────────────────────┘

  Scope: ~8 files use L-shorthand for Scale levels
  Note: Source file uses "Level 1/2/3" — collision only in cross-refs
```

### §1.6 — System E: Feeling 7-Layer Fidelity Gradient

```
  Source: Feeling.md v2.0 §2

  ┌──────────┬──────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới              │ Nghĩa                            │
  ├──────────┼──────────────────────┼──────────────────────────────────┤
  │ Layer 1  │ Feel-RawSignals      │ Body systems fire (100%)         │
  │ Layer 2  │ Feel-Integration     │ Insula + ACC + vmPFC (~95%)      │
  │ Layer 3  │ Feel-Awareness       │ Body state noticeable (~90%)     │
  │ Layer 4  │ Feel-Observation     │ "Something is happening" (~85%)  │
  │ Layer 5  │ Feel-Location        │ "Where is this feeling" (70-90%) │
  │ Layer 6  │ Feel-Labeling        │ "What is this called" (40-80%)   │
  │ Layer 7  │ Feel-Explanation     │ "Why does this exist" (20-70%)   │
  └──────────┴──────────────────────┴──────────────────────────────────┘

  Scope: ~12 files use L-shorthand for Feeling layers
  Note: Source uses "Layer 1-7" — collision only in cross-refs
```

---

## §2 — EXECUTION STRATEGY

### §2.1 — PHASE ORDER (system by system)

```
  ⭐ EXECUTION PHẢI THEO SYSTEM, KHÔNG THEO FILE:

  Phase 1: VALENCE 2-LUỒNG (L1/L2 → Valence-Momentary/Structural)
  → HIGHEST IMPACT — 22 files, most cross-referenced
  → L1/L2 here is DISTINCT from other systems (always in entity/valence context)
  → Can do replace_all in PURE valence files

  Phase 2: BODY-BASE SUBSTRATE (L0/L1 → Substrate-Alive/Inputs)
  → 19 files with current definitions
  → ⚠️ COLLISION with Phase 1: both use "L1"
  → MUST disambiguate per-occurrence

  Phase 3: OLD SUBSTRATE FIX (L2/L3 deprecated → update content)
  → ~30 files using old v7.5 definitions
  → NOT just rename — CONTENT UPDATE needed
  → May need separate plan for content

  Phase 4: SCALE LEVELS (L1/L2/L3 → Scale-Pair/Hub/Institutional)
  → 8 files, small scope

  Phase 5: LADDER (L0-L4 → Ladder-Reflex through Ladder-Execution)
  → 32 files, mostly Child-Chunk-Development/
  → CONTAINED — can do independently

  Phase 6: FEELING LAYERS (L1-L7 → Feel-RawSignals through Feel-Explanation)
  → 12 files, mostly Feeling/ + cross-refs
```

### §2.2 — Replace approach

```
  ⭐ MOSTLY MANUAL vì nhiều files dùng 2+ L-systems:

  PURE files (only 1 L-system) → replace_all OK
  MIXED files (2+ L-systems) → manual per-occurrence

  CONTEXT CLUES cho disambiguation:
  → "2-luồng", "luồng", "stream", "entity", "L2 structural" → Valence
  → "substrate", "body-base", "alive", "17 inputs" → Substrate
  → "inference", "ladder", "chunks required", "motor" → Ladder
  → "scale", "pair", "hub", "institutional", "Dunbar" → Scale
  → "layer", "fidelity", "feeling", "labeling" → Feeling
  → "L2 removed", "L3 collapsed" → Old substrate reference → UPDATE
```

---

## §3 — FILE INVENTORY (tóm tắt per system)

```
  ┌──────────────────┬───────┬───────┬──────────────────────────────────┐
  │ System           │ Files │ ~Occ  │ Approach                         │
  ├──────────────────┼───────┼───────┼──────────────────────────────────┤
  │ A. Valence 2-L   │  ~22  │ ~400  │ replace_all + manual MIXED      │
  │ B. Substrate     │  ~19  │ ~300  │ manual (overlaps Valence files)  │
  │ C. Old Substrate │  ~30  │ ~500  │ CONTENT UPDATE (not just rename) │
  │ D. Scale         │   ~8  │ ~100  │ replace_all (small scope)        │
  │ E. Ladder        │  ~32  │ ~900  │ replace_all (contained in Chunk) │
  │ F. Feeling       │  ~12  │ ~200  │ mixed approach                   │
  │ (overlap across) │       │       │                                  │
  ├──────────────────┼───────┼───────┼──────────────────────────────────┤
  │ UNIQUE FILES     │ ~146  │~3,700 │ ~10-12 sessions                  │
  └──────────────────┴───────┴───────┴──────────────────────────────────┘

  ⚠️ OVERLAP: ~20-30 files appear in 2+ systems → manual review
```

---

## §4 — SESSION PLAN

```
  ┌─────┬─────────────────────────────┬───────┬───────┬──────────────────┐
  │ Ses │ Cluster                     │ Files │ ~Occ  │ Note             │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │ S1  │ Valence source (VP.md)      │   1   │  ~30  │ DEFINE names     │
  │ S2  │ Valence consumers           │  ~20  │ ~370  │ replace+manual   │
  │ S3  │ Substrate source (BB.md)    │   1   │  ~20  │ DEFINE names     │
  │ S4  │ Substrate consumers         │  ~18  │ ~280  │ mostly manual    │
  │ S5  │ Scale (By-Product-Scale)    │   8   │ ~100  │ small scope      │
  │ S6  │ Old substrate fix           │  ~30  │ ~500  │ CONTENT UPDATE   │
  │ S7  │ Ladder source + EN files    │  ~16  │ ~450  │ Chunk/ contained │
  │ S8  │ Ladder VI files             │  ~16  │ ~450  │ Chunk/VI/        │
  │ S9  │ Feeling layers              │  ~12  │ ~200  │ mixed approach   │
  │ S10 │ Verification + edge cases   │  all  │   -   │ grep sweep       │
  ├─────┼─────────────────────────────┼───────┼───────┼──────────────────┤
  │     │ TOTAL                       │ ~146  │~3,700 │ 10 sessions      │
  └─────┴─────────────────────────────┴───────┴───────┴──────────────────┘
```

---

## §5 — GHI CHÚ QUAN TRỌNG

```
  ⚠️ OLD SUBSTRATE (Phase 3 / S6):
  → ~30 files còn dùng L2/L3 substrate từ v7.5 era
  → KHÔNG CHỈ RENAME — phải UPDATE NỘI DUNG:
     "L2 Experience/Novelty" → đã absorbed vào L1 + PFC operators
     "L3 Mastery/Status" → đã reframed thành PFC Operators
  → Có thể cần PLAN RIÊNG cho content update (lớn hơn scope rename)
  → Flag cho bạn quyết định: rename labels chỉ vs full content fix

  ⚠️ PLAN NÀY LÀ LỚN NHẤT:
  → 146 files, ~3,700 occ, 10 sessions
  → Nên execute CUỐI CÙNG sau khi tất cả plans khác xong
  → Hoặc chia nhỏ: execute Valence (Phase 1-2) trước, còn lại sau
```
