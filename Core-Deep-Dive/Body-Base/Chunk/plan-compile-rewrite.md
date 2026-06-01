# Plan: Compile-Sleep.md v1.0 + Compile-Taxonomy.md v3.0

**Created**: 2026-06-01
**Status**: PHASE B COMPLETE (Compile-Taxonomy.md v3.0 — 1,232L, 2026-06-01)
**Prerequisite**: 3 drill files đã COMPLETE (Drill-Compile-Architecture, Drill-10, Drill-11)
**Approach**: Sleep trước → Taxonomy sau → Propagation → Cleanup

---

## BỐI CẢNH

Session 2026-06-01 drill 3 file phát hiện architecture unification lớn:

1. **ALL compile = 1 Engine** (Exposure → Hebbian). 3 Compile Types = labels cho dominant modulator config.
2. **Trust = AMPLIFIER** (gradient Mức 0-5), KHÔNG phải GATE (binary). Contradicts Chunk.md §2.3.
3. **Trust scope**: amplify VALUE compile, KHÔNG amplify CONTENT compile. Giải thích "giỏi nhưng ghét học."
4. **Multi-stream compile**: Content/Value/Entity/Behavior chạy SONG SONG, ĐỘC LẬP.
5. **Sleep = Component S**: offline maintenance ĐỘC LẬP. 6 mechanisms, chỉ ~1.5 exposure-based.
6. **Feedback asymmetry**: D→B slow/costly, B→D fast/free. Giải thích "yêu lấy thầy."
7. **Evolutionary gradient**: engine conserved (Aplysia → human), modulators accumulated.

3 Drill sources:
- `Drill-Compile-Architecture.md` (1,665L) — raw drill, chi tiết Source C, Multi-stream
- `Drill-10-Compile-Architecture.md` (1,160L) — refined drill, Trust Reframe, Feedback MAP, Honest Assessment
- `Drill-11-Compile-Sleep.md` (1,231L) — sleep as Component S, 6 mechanisms

Phân tích cho thấy Drill-10 có CẤU TRÚC TỐT HƠN, Drill (không số) có NỘI DUNG CHI TIẾT HƠN.
→ Merge tốt nhất của cả hai khi formalize.

---

## THỨ TỰ TRIỂN KHAI

```
Phase A: Compile-Sleep.md v1.0         ← FILE MỚI (session riêng)
Phase B: Compile-Taxonomy.md v3.0      ← REWRITE (session riêng)
Phase C: Propagation                   ← Chunk.md, Body-Base.md fixes
Phase D: Cleanup                       ← Drill files → backup/
```

Lý do Sleep trước Taxonomy:
- Sleep = file ĐỘC LẬP, không phụ thuộc Taxonomy
- Taxonomy CẦN reference Compile-Sleep.md (§ Component S)
- Viết Sleep trước → Taxonomy cross-ref ngay, không cần placeholder

---

## PHASE A: Compile-Sleep.md v1.0

### A.0 — Thông tin cơ bản

```
File: Core-Deep-Dive/Body-Base/Chunk/Compile-Sleep.md
Version: 1.0
Estimated: ~1,000-1,200L
Primary source: Drill-11-Compile-Sleep.md (1,231L)
Secondary source: Learning-Cycle.md §4 (6+1 mechanisms)
Parent: Chunk.md v2.3 (§2.1 ④ sleep consolidation = summary → file này = chi tiết)
Related: Compile-Taxonomy.md (Component S), PFC-Operations.md §8.3 (PFC budget recharge)
```

### A.1 — Cấu trúc dự kiến

```
§0 — Vị Trí Trong Framework
  - Chunk.md §2.1 ④ "sleep consolidation" = 3 dòng summary → file này = chi tiết
  - Component S trong Compile Architecture (Engine A + Mod B + Source C + Mod D + Component S)
  - Reading guide: đọc Chunk.md §2 + Compile-Taxonomy.md trước

§1 — Core Thesis: Sleep ≠ Exposure Source
  - Sleep có 6 mechanisms — chỉ ~1.5 exposure-based, ~4.5 optimization
  - Sleep = OFFLINE MAINTENANCE SYSTEM (Component S)
  - Analogy: Engine A (Hebbian) = XÂY nhà. Sleep = BẢO TRÌ nhà.
  - Vị trí diagram: Waking (build) → Sleep (maintain) → Next Waking (build on maintained)
  - SOURCE: Drill-11 §0

§2 — Sleep Stages: SWS vs REM
  - 2 stages = 2 sets of distinct mechanisms
  - SWS dominant nửa đầu đêm: S1, S2, S3, S6
  - REM dominant nửa sau đêm: S4, S5
  - ~4-6 cycles per đêm, mỗi cycle ~90 phút
  - Bảng: SWS vs REM (EEG, NE, ACh, muscles, dreams, key mechanisms)
  - SOURCE: Drill-11 §1 + Learning-Cycle §4.0

§3 — 6 Mechanisms: Exposure vs Optimization
  - Bảng tổng hợp mở đầu: 6 mechanisms × (stage / exposure? / function / confidence)

  §3.1 — S1: SHY Homeostasis (NOT exposure)
    - Tononi & Cirelli 2003, 2014
    - Global synaptic downscaling, prune weak, preserve strong
    - Quality control SAU compile, KHÔNG tạo compile mới
    - Evidence: dendritic spine (Maret 2011, Yang 2014), cross-species (Gilestro 2009)
    - SOURCE: Drill-11 §2.1 + Learning-Cycle §4.1

  §3.2 — S2: Hippocampal Replay (IS exposure)
    - Wilson & McNaughton 1994
    - Re-fire sequences 10-20x compressed trong sharp-wave ripples
    - = Engine A offline: replayed patterns → Hebbian strengthen
    - Khác C3 thức: systematic, compressed, PFC offline, hippocampus-driven
    - SOURCE: Drill-11 §2.2 + Learning-Cycle §4.2

  §3.3 — S3: Active Consolidation (NOT exposure)
    - Born & Wilhelm 2012
    - Transfer hippocampus → cortex (relocate, not strengthen)
    - S2 = substrate, S3 = result. "RAM → ROM"
    - SOURCE: Drill-11 §2.3 + Learning-Cycle §4.3

  §3.4 — S4: REM Creative Linking (PARTIAL exposure)
    - Cai 2009, Wagner 2004
    - Remote associations via altered neurochemistry
    - CÓ Hebbian element (concepts fire together → new link)
    - NHƯNG mechanism KHÁC typical exposure (random + weak gating)
    - = Exploration hơn là exposure
    - SOURCE: Drill-11 §2.4 + Learning-Cycle §4.4

  §3.5 — S5: Emotional Decoupling (NOT exposure)
    - Walker 2017, van der Helm 2011
    - Strip emotional charge, preserve content
    - = EDITING compiled chunk, NOT creating new
    - Failure mode: chronic REM disruption → emotional tags ACCUMULATE → burnout, PTSD
    - EMDR connection (🟡 debated mechanism nhưng clinical efficacy established)
    - SOURCE: Drill-11 §2.5 + Learning-Cycle §4.5

  §3.6 — S6: Gist Extraction (PARTIAL exposure)
    - Payne 2009, Stickgold 2013
    - Abstract pattern from specific, detail fades
    - = Creation BY destruction (new gist replaces old details)
    - Connection: S6 = PRIMARY mechanism tạo Background-Pattern
    - SOURCE: Drill-11 §2.6 + Learning-Cycle §4.6

  §3.7 — S7: Dreaming as Simulation (DEBATED — excluded from core)
    - Revonsuo 2000 — ghi nhận nhưng KHÔNG đưa vào architecture chính
    - SOURCE: Drill-11 §2.7 + Learning-Cycle §4.7

§4 — Sleep × Compile Architecture
  - Mỗi component: Sleep tương tác thế nào

  §4.1 — Sleep × Engine A
    - S2 = bonus exposure cycles (strengthen existing)
    - S1 = improve SNR → Engine A runs cleaner next day
    - S6 = create abstract material → Engine A builds on top

  §4.2 — Sleep × Modulator B (Entity-Valence)
    - S5 = calibrate emotional intensity per entity
    - S6 = contribute to Entity-Compiled formation (40→200h)

  §4.3 — Sleep × Sources C
    - C1 BLOCKED (thalamic gating), C2 OFFLINE (PFC), C3 DIFFERENT mode (S2)
    - S2 ≈ "industrial-grade C3" — organized, fast, efficient

  §4.4 — Sleep × Modulator D (PFC)
    - PFC OFFLINE khi ngủ
    - Sleep RESTORES PFC: catecholamine restoration, cortisol effects clear, SHY efficiency
    - PFC degrades FIRST khi mất ngủ (most metabolically expensive)

§5 — Sleep Deprivation = Architecture Degradation
  - Bảng: 6 mechanisms disrupted → consequences
  - Architecture collapse order: D first → S missed → A dirty → B unchecked
  - Cortisol interaction: "phá nhanh, xây chậm" (sleep debt compounds)
  - Reward vulnerability: Evaluative degrades first, Direct-State persists
  - SOURCE: Drill-11 §4

§6 — Waking Rest: Complement, Not Replacement
  - DMN, incubation, walking, meditation
  - Bảng: 6 mechanisms × waking rest (partial/none)
  - ~30% overlap, ~70% irreplaceable
  - Napping = intermediate
  - SOURCE: Drill-11 §5 + Learning-Cycle §5

§7 — Honest Assessment
  - 🟢 Established: từng mechanism individually (Tononi, Wilson, Born, Cai, Walker, Payne)
  - 🟡 Framework synthesis: Component S model, exposure classification, collapse order
  - 🔴 Needs research: mechanism interaction sequence, napping quantification, age variation

§8 — Open Questions
  - Q1: 6 mechanisms sequential hay concurrent trong 1 đêm?
  - Q2: Napping — mechanism nào active?
  - Q3: Age-related sleep architecture → compile quality decline?
  - Q4: DEC2 short sleepers — efficient mechanisms hay skip?
  - Q5: S5 current vs structural Entity-Valence effect
  - Q6: Sleep as compile_rate parameter hay maintenance?
  - SOURCE: Drill-11 §6

§9 — Cross-References
  - Primary source: Learning-Cycle.md §4
  - Compile architecture: Compile-Taxonomy.md (Component S)
  - Core: Chunk.md §2.1 ④ (summary), PFC-Operations.md §8.3 (budget recharge)
  - Related: Cortisol-Baseline.md, Background-Pattern.md §3, Body-Base.md §2
```

### A.2 — Nguồn chính cho từng section

```
§0 — Drill-11 §0 (thesis) + file hierarchy knowledge
§1 — Drill-11 §0 (thesis + analogy + diagram)
§2 — Drill-11 §1 (SWS vs REM) + Learning-Cycle §4.0
§3 — Drill-11 §2 (6 mechanisms) + Learning-Cycle §4.1-§4.7
§4 — Drill-11 §3 (4 interactions)
§5 — Drill-11 §4 (deprivation)
§6 — Drill-11 §5 (waking rest) + Learning-Cycle §5
§7 — Drill-11 §12 analogy (honest assessment)
§8 — Drill-11 §6 (open questions)
§9 — Drill-11 §8 (cross-refs)
```

### A.3 — Quyết định content

```
KEEP 100% từ drill:
  - 6 mechanisms descriptions + evidence
  - Exposure vs Optimization classification
  - Sleep × Architecture interactions (4 components)
  - Sleep deprivation collapse order
  - Waking rest comparison
  - All research citations

TRIM từ drill:
  - Drill-specific language ("session nào", "observation nào") → framework language
  - Redundant examples (keep 1-2 best per mechanism)
  - Drill §7 implications → absorbed into §0 + §9

ADD so với drill:
  - §0 Vị trí rõ hơn (file hierarchy, reading order)
  - §7 Honest Assessment formal (drill có nhưng ngắn)
  - Cross-refs cập nhật (drill chưa biết Compile-Taxonomy v3.0)

DEFER:
  - S7 dreaming (DEBATED) → ghi nhận, không đưa vào architecture
  - Quantitative sleep dose (bao nhiêu giờ = optimal) → 🔴 needs research
```

### A.4 — Checklist quality

```
□ Mỗi section có research citations (🟢/🟡/🔴)
□ 6 mechanisms consistent với Learning-Cycle.md §4
□ Exposure vs Optimization classification CLEAR
□ Component S vị trí trong architecture CLEAR
□ Không suy đoán ngoài drill evidence
□ Cross-refs cập nhật
□ Honest Assessment đầy đủ
□ File hierarchy description chính xác
```

---

## PHASE B: Compile-Taxonomy.md v3.0

### B.0 — Thông tin cơ bản

```
File: Core-Deep-Dive/Body-Base/Chunk/Compile-Taxonomy.md
Version: v2.0 → v3.0 REWRITE
Estimated: ~1,400-1,600L (v2.0 = 1,174L)
Primary source: Compile-Taxonomy.md v2.0 + Drill-10 + Drill (không số)
Parent: Chunk.md v2.3 §2 (compile mechanisms = foundation)
Related: Body-Base.md §4.2, Compile-Sleep.md v1.0
v2.0: backup/ trước khi rewrite
```

### B.1 — REFRAME CỐT LÕI

```
v2.0 organizing principle: "3 separate types" (taxonomy-first)
v3.0 organizing principle: "1 engine + modulator configurations" (mechanism-first)

KHÔNG PHẢI v2.0 SAI — v2.0 describe patterns ĐÚNG.
v3.0 = DEEPER layer underneath: tại sao 3 types exist,
tại sao chúng interact, tại sao chúng overlap.

Content GIỐNG, organizing principle KHÁC.
```

### B.2 — Cấu trúc dự kiến v3.0

```
§0 — Vị Trí Trong Framework
  - File hierarchy: Chunk.md §2 → file này → Compile-Sleep.md
  - WHAT'S NEW in v3.0: architecture underneath taxonomy
  - Reading guide

§1 — Core Architecture: 1 Engine + 3 Modulators + Sources + Sleep
  - ⭐ THESIS: ALL compile = Exposure → Hebbian. Không có ngoại lệ.
  - 6 observations hội tụ (Drill-10 §1.1)
  - 6 verify cases bảng (Drill (không số) §1.2)

  §1.1 — Engine A: Exposure → Hebbian → Compile
    - Cơ chế duy nhất thay đổi neural wiring
    - compile_rate formula: exposure = tham số FIRST
    - 4 compile mechanisms = 4 dạng exposure (reframe)
    - NO SOURCE TAG = evidence cho 1 engine
    - SOURCE: Drill-10 §2, Drill (không số) §2

  §1.2 — Modulator B: Entity-Valence Bias (automatic)
    - Automatic, cost ≈ 0, pre-PFC
    - 2 cách modulate: amplify rate + bias probability
    - Trust = multiplier (gradient), KHÔNG phải gate (binary)
    - SOURCE: Drill-10 §3, Drill (không số) §3

  §1.3 — Source C: 3 Exposure Sources (song song)
    - C1: External body-input (richest, domain-checked)
    - C2: Internal-deliberate PFC imagination (flexible, abstract domains)
    - C3: Internal-automatic spontaneous chunk fire (cost ≈ 0, self-reinforcing)
    - Bảng tỉ lệ C1:C2:C3 theo tình huống
    - PFC amplify C1+C2, observe C3
    - SOURCE: Drill (không số) §4 (chi tiết nhất)

  §1.4 — Modulator D: PFC Hold + Suppress (deliberate)
    - Hold = amplify exposure (CAN compile)
    - Suppress = block output (CANNOT compile "not")
    - 4 combinations: Hold only, Hold+Suppress, Suppress only, Neither
    - Finite budget, fatigable, evolutionary mới nhất
    - SOURCE: Drill-10 §3.3, Drill (không số) §5

  §1.5 — Component S: Sleep Offline Maintenance
    - 6 mechanisms, ~1.5 exposure + ~4.5 optimization
    - Cycle: Waking (build) → Sleep (maintain) → Next Waking
    - → Chi tiết: Compile-Sleep.md v1.0
    - SOURCE: Drill-11 §0 (summary only, detail in Compile-Sleep.md)

§2 — Tại Sao Compile Ngắn: 3 Hardware Constraints
  - KEEP 100% từ v2.0 §1
  - 3 constraints: PFC ~4±1 slots, processing speed, cortisol cost
  - Convergence: brain BUỘC compile ngắn
  - SOURCE: v2.0 §1 (giữ nguyên)

§3 — Trust Reframe: Amplifier, Not Gate
  - §3.1 — Contradiction detected: Chunk.md §2.3 "gate" vs Entity-Access "gradient"
  - §3.2 — Resolution: amplifier model (Mức 0-5 gradient)
  - §3.3 — Trust scope: VALUE vs CONTENT
    - Trust amplify VALUE install, KHÔNG amplify content compile
    - Trẻ bị ép học = content compile (experience), value NOT compile (no trust)
    - "Giỏi nhưng ghét học" = content ✓ value ✗
  - SOURCE: Drill-10 §6, Drill (không số) §3.1-§3.3

§4 — 3 Compile Types = Dominant Modulator Configurations
  - §4.1 — Experience Compile (Engine A + minimal modulators)
    - KEEP core từ v2.0 §2.1 + add modulator config description
  - §4.2 — Trust Compile (Engine A + Modulator B dominant)
    - REWRITE từ v2.0 §2.3: trust = amplifier, not gate
    - Trust scope clarification (value vs content)
  - §4.3 — Expertise Compile (Engine A + Modulator D dominant)
    - KEEP core từ v2.0 §2.2 + add modulator config description
  - §4.4 — Bảng so sánh
    - UPDATE từ v2.0 §2.4: add Engine/Mod B/Source/Mod D columns
  - SOURCE: Drill-10 §5, Drill (không số) §8 + v2.0 §2

§5 — Multi-Stream Compile
  - §5.1 — 4 Streams: Content / Value / Entity / Behavior
    - Content = LUÔN Experience (Engine A, direct exposure)
    - Value = trust-modulated (Mod B amplify/suppress)
    - Entity = Entity-Valence compile (update weights)
    - Behavior = direction-at-compile (approach/avoidance)
  - §5.2 — Test case: trẻ bị ép học (4 streams visible)
  - §5.3 — Test case: trẻ học với thầy yêu quý (4 streams all positive)
  - §5.4 — Implication: can thiệp giáo dục CẦN biết stream nào thất bại
  - SOURCE: Drill-10 §7, Drill (không số) §6

§6 — 4 Compile Pathways: Cùng Output, Khác Cơ Chế
  - KEEP core từ v2.0 §3
  - ADD modulator config description per pathway
  - ① Hardware Fit = Experience (A, C1, novelty direction)
  - ② Trust + Moderate = Trust+Experience (A + B + partial D, C1)
  - ③ Social Default = Trust (A + B social proof, C1, minimal D)
  - ④ Threat Avoidance = Experience (A, C1, threat direction)
  - Reward implication (v2.0 có, KEEP)
  - SOURCE: v2.0 §3 + Drill (không số) §8.1

§7 — Feedback Loop: Bidirectional + Asymmetry
  - §7.1 — Interaction map (10 paths: D→B, B→D, D→C, C→D, B→C, B→A, A→B, A→C, A→D)
  - §7.2 — Critical asymmetry: D→B slow/costly, B→D fast/free
    - "Tên lửa vs trọng trường" analogy
    - Giải thích: forced learning unsustainable, "yêu lấy thầy" works
  - §7.3 — Virtuous loop: "Yêu lấy thầy" (7 steps)
  - §7.4 — Vicious loop: "Ghét giáo viên" (6 steps + break strategies)
  - SOURCE: Drill-10 §4, Drill (không số) §7 + §10

§8 — 6 Trade-offs Của Compile Ngắn
  - KEEP core từ v2.0 §6 (T1-T6)
  - Minor refine: T6 "biết mà không làm" → add compile depth explanation

§9 — Experience × Trust Interactions
  - KEEP từ v2.0 §7.1 (hợp lực, cạnh tranh, override, overlapping)
  - KEEP từ v2.0 §7.2 (chain break detection)
  - KEEP từ v2.0 §7.3 (expertise × external tools)

§10 — Evolutionary Gradient
  - Engine A conserved (Aplysia → human)
  - Modulators accumulated: insects → fish → mammals → primates → humans
  - Bảng: species × Engine/ModB/SourceC/ModD
  - Compilable Architecture = engine + full modulator suite
  - SOURCE: Drill-10 §9, Drill (không số) §9

§11 — Edge Cases (8+)
  - Trauma, Cult, Therapy, Trẻ bị ép, "Biết mà không làm",
    Immersion, Expert blind spot, "Yêu lấy thầy"
  - Tất cả consistent với 1-engine architecture
  - SOURCE: Drill-10 §8, Drill (không số) §10

§12 — Honest Assessment
  - 🟢: Hebbian, LTP, PFC operations, sleep, trust as valence dimension
  - 🟡: 1 engine + 3 modulators unification, multi-stream, trust = amplifier not gate
  - 🔴: quantitative weights, multi-stream resource competition, cross-cultural variation
  - SOURCE: Drill-10 §12 + v2.0 §8

§13 — Cross-References
  - SOURCE: v2.0 §9 + updates
```

### B.3 — Content decisions (KEEP / REWRITE / ADD / REMOVE)

```
KEEP 100% từ v2.0:
  - §1 (3 hardware constraints) → v3.0 §2
  - §6 (6 trade-offs) → v3.0 §8
  - §7 (interactions) → v3.0 §9
  - §8 (honest assessment) → v3.0 §12 (extend)
  - §9 (cross-refs) → v3.0 §13 (update)

REWRITE từ v2.0:
  - §0 (vị trí) → v3.0 §0 (add architecture context)
  - §2 (3 compile types) → v3.0 §4 (reframe as modulator configs)
  - §3 (4 pathways) → v3.0 §6 (add modulator config per pathway)
  - §4 (trust 5 bước) → v3.0 §3 (trust = amplifier, scope VALUE vs CONTENT)
  - §5 (PFC=director) → absorbed into §1.4 Modulator D

ADD MỚI (từ drill):
  - §1 Architecture (Engine + Modulators + Sources + Sleep)
  - §3 Trust Reframe (contradiction + resolution + scope)
  - §5 Multi-Stream Compile
  - §7 Feedback Loop + Asymmetry
  - §10 Evolutionary Gradient
  - §11 Edge Cases (consolidated)

REMOVE:
  - v2.0 §4 (trust 5 bước chi tiết) → trim, core absorbed into §3
  - v2.0 §5 (PFC=director standalone) → absorbed into §1.4

MOVE to backup/:
  - Compile-Taxonomy.md v2.0 → backup/Compile-Taxonomy-v2.0.md
```

### B.4 — Merge strategy (2 drill files)

```
Từ Drill-10 (cấu trúc TỐT HƠN):
  - Trust Reframe riêng section (§6 → v3.0 §3)
  - Feedback interaction MAP table (§4.1 → v3.0 §7.1)
  - Honest Assessment (§12 → v3.0 §12)
  - "Yêu lấy thầy" step-by-step (§10 → v3.0 §7.3 + §7.4)

Từ Drill (không số) (nội dung CHI TIẾT HƠN):
  - Bảng tỉ lệ C1:C2:C3 (§4.1 → v3.0 §1.3)
  - C3 5 nguồn chi tiết (§4.4 → v3.0 §1.3)
  - Multi-stream 2 ví dụ full (§6 → v3.0 §5.2 + §5.3)
  - Modulator B×D interaction detail (§5.1 → v3.0 §7)
  - PFC 4 cách modulate exposure (§3.3 → v3.0 §1.4)
```

### B.5 — Checklist quality

```
□ Organizing principle = 1 engine + modulators (CLEAR từ §0 + §1)
□ 3 Compile Types PRESERVED as labels, REFRAMED as configs
□ Trust = amplifier (not gate) — consistent, no "gate" language
□ Multi-stream compile: 4 streams rõ ràng
□ Feedback asymmetry: diagram + examples
□ All v2.0 content accounted for (KEEP/REWRITE/absorbed)
□ Cross-refs accurate (Compile-Sleep.md, Chunk.md, Body-Base.md)
□ Honest Assessment đầy đủ
□ All research citations preserved + new citations added
□ v2.0 → backup/ trước khi rewrite
```

---

## PHASE C: Propagation (sau cả Sleep + Taxonomy done)

### C.1 — Chunk.md §2.3 terminology fix

```
Target: Chunk.md v2.3 line 288-290
Current: "TRUST = GATE CHO EXTERNAL INSTALL"
Fix: "TRUST = AMPLIFIER (GRADIENT) CHO COMPILE RATE"
+ Add: "Gate = limit case khi multiplier → 0"
+ Cross-ref: Compile-Taxonomy.md v3.0 §3 (Trust Reframe)
```

### C.2 — Chunk.md §2.1 ④ sleep expand reference

```
Target: Chunk.md v2.3 §2.1 mechanism ④
Current: 3 dòng "Sleep consolidation (Walker 2017)"
Fix: Add "Chi tiết 6 mechanisms: Compile-Sleep.md v1.0"
```

### C.3 — Body-Base.md §4.2 reference update

```
Target: Body-Base.md v3.3 line 593, 632
Current: "(E4 — chưa viết)" references
Fix: Update to "Compile-Taxonomy.md v3.0" reference
```

### C.4 — Body-Base.md §4 minor additions

```
Optional: Add note in §4.1 about 1-engine architecture
Optional: Add Compilable Architecture = Engine A + B + C + D + S
Source: Drill (không số) §12 ④
```

### C.5 — Learning-Cycle.md §4.10 cross-ref

```
Target: Learning-Cycle.md §4.10 (framework update recommendation)
Current: Recommends expanding Chunk.md §2 mode 4
Fix: Add "Implemented → Compile-Sleep.md v1.0"
```

---

## PHASE D: Cleanup (sau propagation done)

### D.1 — Drill files → backup/

```
Move to backup/:
  - Drill-Compile-Architecture.md → backup/Drill-Compile-Architecture.md
  - Drill-10-Compile-Architecture.md → backup/Drill-10-Compile-Architecture.md
  - Drill-11-Compile-Sleep.md → backup/Drill-11-Compile-Sleep.md
  - plan-compile-drill.md → backup/plan-compile-drill.md
  - plan-compile-rewrite.md → backup/plan-compile-rewrite.md (plan này)
```

### D.2 — Verify

```
□ Compile-Sleep.md v1.0 tồn tại
□ Compile-Taxonomy.md v3.0 tồn tại
□ v2.0 backup tồn tại
□ Chunk.md §2.3 "amplifier" not "gate"
□ Chunk.md §2.1 ④ references Compile-Sleep.md
□ Body-Base.md §4.2 references Compile-Taxonomy.md v3.0
□ All drill files in backup/
□ No broken cross-refs
```

---

## EXECUTION NOTES

```
SESSION FLOW:
  Session 1: phân tích + plan ✅
  Session 2: Phase A — Compile-Sleep.md v1.0 ✅ (992L, 2026-06-01)
  Session 3: Phase B — Compile-Taxonomy.md v3.0 ✅ (1,232L, 2026-06-01)
  Session 4: Phase C + D — Propagation + Cleanup ← NEXT

  Mỗi session: compact trước → đọc drill + plan → triển khai.
  Plan này + 3 drill files = đủ context cho cold start.

CRITICAL FILES TO READ mỗi session:
  - plan-compile-rewrite.md (file này)
  - Drill source tương ứng (11 cho Sleep, 10 + không số cho Taxonomy)
  - Các file liên quan (Chunk.md §2, Body-Base.md §4)
```

---

**NEXT**: Session 4: Phase C (Propagation) + Phase D (Cleanup)
