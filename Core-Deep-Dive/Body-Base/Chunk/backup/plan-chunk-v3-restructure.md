# Plan: Chunk.md v2.3 → v3.0 Restructure

## Bối cảnh

Chunk.md = CORE REFERENCE cho toàn bộ chunk system. Là 1 trong những file trung tâm
quan trọng nhất của framework. ~1,670 dòng, 14 sections.

Session trước (2026-06-01) đã tạo 2 file mới:
- Compile-Taxonomy.md v3.0 (~1,635L) — "1 Engine + 3 Modulators" architecture
- Compile-Sleep.md v1.0 (~1,317L) — Sleep Maintenance chi tiết

Vấn đề: Chunk.md v2.3 chưa reflect architecture mới. §2 overlap ~60-70% với
Compile-Taxonomy. §8-§9 lỗi thời. §10 overlap với Body-Feedback-Precondition.
6 concepts quan trọng chưa có trong Chunk.md.

## Nguyên tắc restructure

1. Chunk.md = "WHAT chunks are + HOW chunks work internally"
2. Compile ARCHITECTURE details → Compile-Taxonomy.md (cross-ref, không duplicate)
3. PFC OPERATIONS details → PFC-Operations.md (cross-ref, không duplicate)
4. Body-feedback details → Body-Feedback-Precondition.md (cross-ref, không duplicate)
5. §2.x numbering PHẢI GIỮ NGUYÊN (15+ files reference §2.3)
6. §1, §3-§7 = solid → giữ gần nguyên
7. Reframe + Trim, KHÔNG rewrite from scratch

## Cross-Reference Impact Map

```
§2.3 (trust/external) → 15+ files reference → PHẢI giữ §2.3 numbering
§2.4 (Direction-At-Compile) → 3 files → giữ numbering
§8.1 (two operators quote) → 2 files (PFC-Function, Schema) → update SAU
§9, §10, §11 → 0 live file reference → TỰ DO restructure
§12 → 2 files (Blackbox-Map) → minor update
```

---

## Cấu trúc v3.0 đề xuất

### MỤC LỤC MỚI (so với cũ)

```
v2.3 (hiện tại)                    v3.0 (đề xuất)
─────────────────────────          ─────────────────────────────
                                   §0 — Vị Trí Trong Framework     ← NEW
§1 — Chunk Là Gì                  §1 — Chunk Là Gì                ← KEEP ~95%
§2 — Chunk Compile                §2 — Chunk Compile               ← RESTRUCTURE
  §2.1 4 mechanisms                 §2.1 Compile Architecture (1 Engine)  ← REFRAME
  §2.2 compile_rate formula         §2.2 compile_rate formula       ← KEEP, trim
  §2.3 External install + Trust     §2.3 External install + Trust   ← MAJOR TRIM
  §2.4 Direction-At-Compile         §2.4 Direction-At-Compile       ← KEEP
  §2.5 Reconsolidation              §2.5 Reconsolidation            ← KEEP
  §2.6 Context-tag                  §2.6 Context-tag                ← KEEP
                                    §2.7 Sleep Maintenance           ← NEW summary
§3 — Connections (4 Types)         §3 — Connections (4 Types)       ← KEEP 100%
§4 — Activation Dynamics           §4 — Activation Dynamics         ← KEEP 100%
§5 — Anchor-Decay Model            §5 — Anchor-Decay Model          ← KEEP 100%
§6 — Labels + Logic-Planning       §6 — Labels + Logic-Planning     ← KEEP ~95%
§7 — Discovery Lifecycle           §7 — Discovery Lifecycle         ← KEEP ~95%
§8 — Two Operators                 §8 — Operators × Chunk System    ← REWRITE
§9 — PFC Search (4 Modes)           (absorbed into §8)              ← REMOVE
§10 — Body Evaluate                 (partially into §8)             ← REMOVE
§11 — Expert vs Beginner           §9 — Expert vs Beginner          ← TRIM, renumber
§12 — Honest Assessment            §10 — Honest Assessment          ← UPDATE, renumber
§13 — Cross-References             §11 — Cross-References           ← UPDATE, renumber
§14 — Status                       §12 — Status                     ← UPDATE, renumber
```

---

## Phase A: §0 NEW + §2 Restructure

### A1: Thêm §0 — Vị Trí Trong Framework (~35 dòng)

Nội dung mới:
- Position Chunk.md trong file hierarchy
- Reading flow: Chunk.md (core reference) → Compile-Taxonomy.md (architecture)
  → Compile-Sleep.md (sleep maintenance)
- Chunk/ folder overview: 4 files + Agent-Mechanism/ subfolder (11 files)
- "File này = WHAT + HOW. Architecture details → companion files."

### A2: §2.1 — Reframe "4 mechanisms" → "1 Engine + 4 dạng exposure" (~35 dòng)

Hiện tại (~25 dòng): liệt kê 4 cơ chế riêng biệt + Walker 2017 cho sleep.
Sau: REFRAME thành "ALL compile = Exposure → Hebbian (1 Engine)" + bảng 4 dạng exposure.
- Giữ bảng 4 mechanisms NHƯNG label lại: "4 DẠNG EXPOSURE feeding 1 Engine"
- Thêm: "3 Compile Types (Experience/Expertise/Trust) = dominant modulator configs"
- Cross-ref: → Chi tiết architecture: Compile-Taxonomy.md v3.0
- Cross-ref: → Chi tiết sleep: Compile-Sleep.md v1.0 (thay cho "Walker 2017" 3 dòng)

### A3: §2.2 — compile_rate formula (KEEP, minor trim ~20 dòng)

Trim examples nếu dài. Giữ formula + cross-state validation.
Thêm 1 dòng: "Formula × Compile Engine × Modulators → Compile-Taxonomy.md v3.0 §1.1"

### A4: §2.3 — External Install + Trust (MAJOR TRIM: ~100 → ~45 dòng)

KEEP (không thể xóa — 15+ external refs):
- 5 external install mechanisms list (co-attention, imitation, social referencing, label, cultural)
- 4 education failure modes
- Trust = AMPLIFIER (gradient Mức 0-5), KHÔNG phải gate
- Trust scope: amplify VALUE, không amplify CONTENT (1 câu summary)
- Entity-Access gradient reference

REMOVE/REDIRECT (đã có Compile-Taxonomy v3.0 §3):
- "5 TRUST SOURCES = 5 DẠNG COMPILE" block dài → redirect
- Trust compile = cùng 4 cơ chế block → redirect
- Trust break = competitive re-linking block → redirect (đã ở §4.3)
- Trust = valence meta-dimension detail → redirect

Thêm: "→ Chi tiết trust architecture: Compile-Taxonomy.md v3.0 §3"

### A5: §2.7 — Sleep Maintenance (NEW ~20 dòng)

Summary: Sleep = offline maintenance system, KHÔNG đơn thuần exposure source thứ 4.
6 mechanisms: ~1.5 exposure + ~4.5 optimization.
Bảng tóm tắt 6 mechanisms (compact 1-line mỗi mechanism).
Cross-ref: → Chi tiết: Compile-Sleep.md v1.0

### Ước lượng Phase A:
- §0: +35 dòng (new)
- §2.1: ~25 → ~35 dòng (+10, reframe)
- §2.2: ~30 → ~22 dòng (-8, trim)
- §2.3: ~100 → ~45 dòng (-55, major trim)
- §2.4-§2.6: giữ nguyên
- §2.7: +20 dòng (new)
- Net Phase A: ~+2 dòng (trim §2 bù bởi §0 + §2.7 mới)

---

## Phase B: §8 Rewrite (merge old §8+§9+§10)

### Tại sao merge?

Old §8 "Two Operators" (~85 dòng) + Old §9 "PFC Search 4 Modes" (~70 dòng)
+ Old §10 "Body Evaluate" (~130 dòng) = ~285 dòng.

Vấn đề:
- §8: framing lỗi thời, chưa align PFC-Operations.md Hold/Suppress model
- §9: "Search" metaphor đã bị flag, 4 Modes không align Exposure Channels
- §10: Body-Feedback-Precondition.md đã formalize chính xác hơn

Giải pháp: Gộp thành 1 section §8 "Operators × Chunk System" — concise integration hub.

### B1: §8.1 — Two Operators: Core Architecture (~40 dòng, trim từ old §8.1)

KEEP:
- "Vô thức xây nhà (95%), PFC chọn XÂY Ở ĐÂU (5%)" (externally quoted)
- Vô thức: compile, run, evaluate, process nền, strengthen/weaken
- PFC: search, hold, create, modify, direct
- PFC hardware online from prenatal (5 pillars, brief)
- PFC-Inference Ladder L0-L4 (from old §8.4)

TRIM:
- "What each CAN/CANNOT do" detailed lists → ref PFC-Operations + PFC-Function
- Simulation-Engine detail → ref Simulation-Engine.md

### B2: §8.2 — PFC Operations: Hold + Suppress (~30 dòng, NEW summary)

Summary from PFC-Operations.md v1.3:
- Hold = amplify new patterns (cost ①)
- Suppress = block existing (cost ②)
- 4 combinations (brief table): Hold only / Hold+Suppress / Suppress only / Neither
- 3 outcomes: Genuine Shift / Compiled Suppress / PFC Failure (brief)
- PFC Budget = finite shared resource
- Cross-ref: → Chi tiết: PFC-Operations.md v1.3

### B3: §8.3 — 3 Exposure Channels (~25 dòng, NEW summary)

Summary from Compile-Taxonomy.md v3.0 §1.3:
- External (body-input from reality) — multi-modal richest
- Deliberate (PFC imagination/simulate) — flexible, PFC-controlled
- Spontaneous (auto chunk fire, Background-Pattern) — cost ≈ 0
- PFC = Director cho External+Deliberate, Observer cho Spontaneous
- Cross-ref: → Chi tiết: Compile-Taxonomy.md v3.0 §1.3

### B4: §8.4 — Body Evaluate: 5 Preconditions (~30 dòng, replace old §10.1)

Summary from Body-Feedback-Precondition.md v1.0:
- 5 Preconditions: Directed-Gap, Chunk-Substrate, Delta-Gate, Match-Range, Compile-Gate
- Conjunction logic: ALL 5 simultaneously met → signal fires
- Body vote = constraint satisfaction (smooth / resistance / empty)
- Cross-ref: → Chi tiết: Body-Feedback-Precondition.md v1.0

### B5: §8.5 — Feeling-Intuition Gradient (~25 dòng, trim từ old §10.2)

KEEP: 6-point gradient, 3 variables (count × strength × label), Multi-Weak-Signal-Convergence
TRIM: cắt examples dài, cắt expert/beginner (đã có §9)

### B6: §8.6 — Domain-Checked vs Self-Referencing (~25 dòng, trim từ old §10.3)

KEEP: "Mượt thật" vs "mượt giả" core warning, dissonance tolerance
TRIM: cắt nuance paragraph, cắt ví dụ dài

### Ước lượng Phase B:
- Old §8+§9+§10: ~285 dòng
- New §8: ~175 dòng
- Net Phase B: ~-110 dòng

### Old §9 "PFC Search (4 Modes)" — REMOVE hoàn toàn

Content disposition:
- "Quick Search" → absorbed into §8.2 (Hold)
- "Body Novelty" → absorbed into §8.3 (Exposure-External)
- "Loose Hold" → absorbed into §8.2 (Hold) + §8.3 (Exposure-Spontaneous)
- "Active Lock" → absorbed into §8.2 (Hold + Suppress, PFC budget)
- "Cortisol = amplifier" → already in Cortisol-Baseline.md v2.2
- "Probability-weighted search" → already in §4.1

---

## Phase C: Renumber + Update §9-§12

### C1: Old §11 → New §9 "Expert vs Beginner" (TRIM ~80 → ~55 dòng)

KEEP: "Same PFC, different database", trigger surface → intuition, Receptive-Productive
TRIM: cắt bớt examples (detail đã ở F1 08, F4 02)

### C2: Old §12 → New §10 "Honest Assessment" (UPDATE)

ADD items cho concepts mới:
🟡 items mới:
- "1 Engine + 3 Modulators" unification (Compile-Taxonomy v3.0)
- Trust = amplifier not gate (Compile-Taxonomy v3.0 §3)
- Multi-stream compile (Content/Value/Entity/Behavior)
- 3 Exposure Channels parallel model
- Feedback asymmetry (Entity-Valence→PFC fast, PFC→Entity-Valence slow)
- Sleep Maintenance in compile architecture
- Body-Feedback-Precondition 5 conditions

~90 dòng → ~105 dòng

### C3: Old §13 → New §11 "Cross-References" (MAJOR UPDATE)

Updates needed:
- §11.1: Thêm Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0 vào Chunk/ files
- §11.2: Update versions (Valence-Propagation v4.1, Body-Base v3.3,
  PFC-Operations v1.3, Body-Feedback-Precondition v1.0, etc.)
- §11.3: Thêm citations mới nếu có từ Compile-Taxonomy/Sleep

~120 dòng → ~135 dòng

### C4: Old §14 → New §12 "Status" (UPDATE)

Thêm:
```
✅ V3.0 RESTRUCTURE (2026-06-0X):
  §0 NEW: Vị trí trong framework + reading flow
  §2.1 REFRAME: 4 mechanisms → 1 Engine + 4 dạng exposure
  §2.3 TRIM: Trust detail → Compile-Taxonomy.md v3.0 §3
  §2.7 NEW: Sleep Maintenance summary (→ Compile-Sleep.md v1.0)
  §8 REWRITE: Merge old §8+§9+§10 → unified "Operators × Chunk System"
    +PFC Hold/Suppress, +3 Exposure Channels, +5 Preconditions
  Old §9 "PFC Search" REMOVED (superseded)
  Old §10 "Body Evaluate" ABSORBED into new §8
  §9-§12 renumbered
  Source: Compile-Taxonomy v3.0 + Compile-Sleep v1.0 alignment
```

~80 dòng → ~95 dòng

### C5: YAML header update

- title: v3.0
- updated: 2026-06-0X
- related: +Compile-Taxonomy.md v3.0, +Compile-Sleep.md v1.0
- dependencies: update all versions

---

## Phase D: Propagation (update external files)

### D1: PFC-Function.md (2 refs)

Line 39: quote "Chunk.md §8.1" → vẫn đúng (§8.1 giữ nguyên nội dung quote)
Line 318: "Chunk.md §8.3" → update thành §8.1 hoặc §8.2 (tuỳ content alignment)

### D2: Schema.md (1 ref)

Line 328: "Chunk.md §8, §9" → update thành "Chunk.md §8"

### D3: Blackbox-Map.md (2 refs)

"Chunk.md §12" → update thành "Chunk.md §10"

### D4: 99-Master-Synthesis.md (2 refs)

"Chunk.md §8.2" → kiểm tra align
"Chunk.md §11.3" → update thành "Chunk.md §9.3"

### D5: File-Index.md

Update Chunk.md description: v2.3 → v3.0 + thay đổi tóm tắt

### Ước lượng Phase D: ~5 files, ~10 edits nhỏ

---

## Tổng kết ước lượng

```
                        v2.3 (hiện tại)    v3.0 (dự kiến)    Δ
§0 Vị Trí              (không có)          ~35 dòng          +35
§1 Chunk Là Gì         ~210                ~210               0
§2 Chunk Compile        ~255                ~230              -25
§3 Connections          ~80                 ~80                0
§4 Activation           ~150                ~150               0
§5 Anchor-Decay         ~95                 ~95                0
§6 Labels               ~80                 ~80                0
§7 Discovery            ~95                 ~95                0
§8 Operators (NEW)      ~285 (old §8+9+10)  ~175             -110
§9 Expert/Beginner      ~80                 ~55               -25
§10 Honest Assessment   ~90                 ~105              +15
§11 Cross-References    ~120                ~135              +15
§12 Status              ~80                 ~95               +15
─────────────────────────────────────────────────────────────────
TOTAL                   ~1,670              ~1,540            ~-130
```

Giảm ~130 dòng, NHƯNG chất lượng TĂNG vì:
- Loại bỏ duplicate với Compile-Taxonomy v3.0
- Align với PFC-Operations v1.3
- Thêm 6 missing concepts
- Cross-refs hiện đại

---

## Execution Order

```
SESSION 1 (dự kiến):
  Phase A: §0 + §2 restructure
  Phase B: §8 rewrite

SESSION 2 (nếu cần):
  Phase C: Renumber + update §9-§12
  Phase D: Propagation (~5 files)
```

Có thể hoàn thành trong 1 session nếu mọi thứ suôn sẻ.
Phase A + B là trọng tâm (~80% công việc).
Phase C + D là mechanical (~20%).

---

## Risks + Mitigations

1. §2.3 numbering — MUST preserve. 15+ files reference.
   → Mitigation: giữ §2.3 heading, chỉ trim NỘI DUNG.

2. Old §8 quote in PFC-Function — "Vô thức xây nhà, PFC chọn XÂY Ở ĐÂU."
   → Mitigation: giữ quote ở new §8.1. Cross-ref vẫn đúng.

3. Renumbering §9-§12 — old §11→§9, §12→§10, §13→§11, §14→§12.
   → Mitigation: Phase D propagation covers all live refs.

4. Content loss — trim trust, trim PFC modes.
   → Mitigation: ALL trimmed content ĐÃ có ở companion files.
     Chunk.md trim = cross-ref, KHÔNG xóa knowledge.

5. v2.3 backup.
   → Mitigation: backup/Chunk-v2.3-backup.md trước khi edit.
