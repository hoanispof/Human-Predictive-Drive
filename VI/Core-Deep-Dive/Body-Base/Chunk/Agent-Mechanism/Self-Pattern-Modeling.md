---
title: Self-Pattern-Modeling — Solo Forward Simulation Mechanism
version: 3.2
created: 2026-04-15
updated: 2026-06-02 (v3.2: +§15.4 cross-ref to Collective-Body §5.4 guilt 3-layer model — self-model guilt = lớp ③)
rewritten: 2026-05-22 (v3.1 — RENAME Match→Modeling, Simulation-Engine APPLICATION, 3 dimensions, 42 drill insights integrated)
previous_versions:
  - v3.0 (2026-05-17, 2569L) → backup/Self-Pattern-Match-v3.0-backup.md
  - v2.4 (2292L) → backup/Self-Pattern-Match-v2.4-backup.md
  - v1.0 (1518L) → backup/Self-Pattern-Match-v1.0-forward-backup.md
  - v0 (inward-labeling) → Body-Base/Feeling/backup/Self-Pattern-Match.md
status: v3.1 — CORE MECHANISM FILE
scope: |
  APPLICATION-1 trên Simulation-Engine: Self-Pattern-Modeling = (Other, Present, Simulate).
  v3.1 KEY CHANGES:
    ① RENAME: Self-Pattern-Match → Self-Pattern-Modeling (full name used throughout)
    ② Self-Pattern-Modeling = APPLICATION trên Simulation-Engine (shared substrate)
    ③ 1 mechanism × 3 dimensions (not 4 skills)
    ④ Over-clone = observation label, mechanism = compiled suppress gap riêng
    ⑤ 4 conditions ĐỒNG THỜI cho resonance
    ⑥ Abstract entities taxonomy
    ⑦ Background-Pattern triple bias (retrieval + template + interpretation)
    ⑧ Transfer learning + interference + Freud reframe
    ⑨ 8 failure modes → 3 categories
    ⑩ PFC-Operations + Entity-Access + Entity-Compiled integration
  Giữ nguyên core từ v3.0: Compiled/Fresh, 6 steps, valence gate,
  expert intuition, PFC=Lawyer, 3-cost, per-domain Self-Pattern-Modeling, 30+ citations.
purpose: |
  File NỀN TẢNG cho toàn bộ framework:
  ① Self-Pattern-Modeling là CƠ CHẾ CHÍNH mà não dùng để interact với agents
  ② APPLICATION-1 trên Simulation-Engine (Other × Present × Simulate)
  ③ 2 Functions (Compiled+Fresh) = Compiled/Fresh spectrum applied to agent prediction
  ④ Context-dependent selection giải thích TẠI SAO cùng 1 người
     ứng xử KHÁC NHAU với mẹ, bạn, kẻ thù
  ⑤ Per-Agent Valence quyết định Compiled/Fresh fire HƯỚNG NÀO
position: |
  Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/ — supporting file cho Agent-Mechanism.md
  Sibling: By-Product-Gap-Resonance.md
  Downstream: Connection.md, Empathy.md, Status.md, toàn bộ observation files
  Engine: Simulation-Engine.md (SHARED ENGINE underneath)
dependencies:
  - Simulation-Engine.md v1.0 — SHARED ENGINE: 3 components × 3 axes
  - PFC-Operations.md v1.0 — Hold/Suppress, Compiled Quality Dimension, PFC Budget
  - Entity-Compiled.md v1.0 — Entity-Compiled lifecycle, Dunbar, Hub-and-Spoke
  - Entity-Access.md v1.0 — mPFC gradient, Entity-Access spectrum, 3-Factor Model
  - Agent-Mechanism.md v2.1 — integration hub, §5 preview
  - By-Product-Gap-Resonance.md v1.0 — emergent mutual phenomenon (2-Stream)
  - Chunk.md v2.0 — chunk substrate
  - Feeling.md v3.0 — PFC observation interface
  - Logic-Feeling.md v2.1 — Compiled/Fresh spectrum
  - Valence-Propagation.md v2.0 — per-entity valence, chain propagation
  - Body-Coupling.md v2.0 — coupling mechanism (builds ON Self-Pattern-Modeling)
  - Body-Feedback-Mechanism.md v2.0 — 2-source model, chunk dynamics
  - Inter-Body-Mechanism.md v1.0 — Compiled/Fresh axis, 3-cost, Compilable Architecture
  - Empathy.md v3.0 — Self-Pattern-Modeling function applied to other agents
  - Connection.md v4.0 — 3 generative primitives, 2-luồng reward
  - Cortisol-Baseline.md v2.1 — stress cascade, moral injury
  - Background-Pattern.md v1.1 — 2D Depth×Density, §8 self-reinforcing
  - Imagine-Final.md v2.0 — APPLICATION-2, shared engine
  - Self-Observation.md v1.0 — APPLICATION-3, mutual reinforcement (Step 5 prerequisite)
sources:
  - Self-Pattern-Match.md v3.0 (2,569L) — previous version
  - Drill-Self-Pattern-Modeling-Mechanism-Analysis v2.2 (17 insights)
  - Drill-Over-Self-Pattern-Modeling-Clarification v1.0 (12 insights)
  - Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 (13 insights)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Self-Pattern-Modeling — Solo Forward Simulation Mechanism

> ⚠️ **QUY ƯỚC**: Tên đầy đủ = **Self-Pattern-Modeling**. Viết tắt = **Self-Pattern-Modeling**.
> Đổi từ "Self-Pattern-Match" vì "Match" = passive so sánh, "Modeling" = active mô hình hóa.
> Self-Pattern-Modeling thật sự = forward simulation (xây model + chạy + predict), không phải tìm-khớp.

> Bạn thấy bạn thân khóc. Body bạn buồn nhẹ — DÙ bạn không bị gì.
> Đó là Compiled: body SIMULATE trạng thái người khác — automatic, gần vô thức.
>
> Rồi bạn nghĩ: "bạn buồn vì chia tay → chắc muốn ai đó lắng nghe."
> Đó là Fresh: PFC CHAIN draft predict hành vi tiếp theo — deliberate, tốn effort.
>
> Cùng 1 mechanism. Cùng 1 chunk library. Nhưng 2 OUTPUTS khác nhau.
> "Feeling" và "Logic"? Chỉ là LABELS — Einstein "cảm" toán vì toán đã COMPILED.
> Therapist mới "nghĩ" cảm xúc vì case mới còn FRESH.
> Trục thật: COMPILED ←→ FRESH. Content không quyết định.
>
> Và TẤT CẢ phụ thuộc Per-Agent Valence — body đánh giá agent NÀY thế nào?
> Valence dương: Compiled = empathy. Valence âm: Compiled = REVERSED (pleasant khi kẻ thù đau).
> Cùng mechanism, cùng 6 steps — khác output vì khác valence.

---

## Mục lục

- §0 — Position + Thesis: Self-Pattern-Modeling trên Simulation-Engine
- §1 — Definition: 1 Mechanism × 3 Dimensions
- §2 — Self-Pattern-Modeling Scope: Agent Properties + Fire Gradient
- §3 — 2 Functions: Compiled + Fresh
- §4 — 6 Steps (reframed qua Compiled/Fresh)
- §5 — Context-Dependent Selection
- §6 — Clone Spectrum + Over-Clone Reframe
- §7 — Self-Pattern-Modeling → Resonance: 4 Conditions Đồng Thời
- §8 — Abstract Entities Taxonomy
- §9 — Background-Pattern × Self-Pattern-Modeling: Triple Bias
- §10 — Multiple Models: Transfer + Interference
- §11 — 8 Failure Modes → 3 Categories
- §12 — Shared Substrate: Self-Pattern-Modeling on Simulation-Engine
- §13 — PFC-Operations + Entity-Access Integration
- §14 — Developmental Trajectory
- §15 — Reversed Mapping + Professional Self-Pattern-Modeling + Moral Injury
- §16 — Training + AI Era
- §17 — Honest Assessment
- §18 — Cross-References
- §19 — Research Citations

---

## §0 — Position + Thesis: Self-Pattern-Modeling trên Simulation-Engine

### §0.1 — Self-Pattern-Modeling = APPLICATION-1 trên Simulation-Engine

```
⭐⭐ Self-Pattern-Modeling TRÊN SIMULATION-ENGINE:

  Simulation-Engine.md v1.0: Brain có 1 general-purpose engine:
    3 COMPONENTS: Interoception × Constructive Simulation × Self/Other Model
    3 AXES: Target × Time × Operation

  Self-Pattern-Modeling = APPLICATION-1: tọa độ (Other, Present, Simulate)
    → Target = OTHER entity (bạn, mẹ, kẻ thù, stranger)
    → Time = PRESENT (current/near-future state)
    → Operation = SIMULATE (forward prediction)

  3 Applications trên CÙNG engine:
    ┌──────────────────┬──────────┬──────────┬──────────────────┐
    │ Application      │ Target   │ Time     │ Operation        │
    ├──────────────────┼──────────┼──────────┼──────────────────┤
    │ Self-Pattern-Modeling (file này)   │ OTHER    │ Present  │ Simulate         │
    │ Imagine-Final    │ SELF     │ Future   │ Simulate+Construct│
    │ Self-Observation │ SELF     │ Present  │ Observe          │
    └──────────────────┴──────────┴──────────┴──────────────────┘

  SHARED SUBSTRATE: anterior insula + vMPFC + DMN + hippocampus
  → Luyện 1 application = luyện TẤT CẢ (shared substrate improvement)
  → Hỏng 1 component = hỏng TẤT CẢ (alexithymia = decisive proof)
  → 🟢 Lombardo 2010: IDENTICAL connectivity cho self vs other
  → 🟢 Buckner & Carroll 2007: all = "self-projection" in DMN

  CÁI RIÊNG CỦA Self-Pattern-Modeling (so với 2 apps khác):
    → TARGET = OTHER (không phải self)
    → Accuracy limited by chunk OVERLAP với target
    → Per-Agent VALENCE quyết định direction (không có ở Self-Observation/Imagine-Final)
    → 6-step mechanism chi tiết (file này)
```

### §0.2 — Relationship với files khác

```
  KIẾN TRÚC:
    Simulation-Engine.md    = ENGINE (unification architecture)
    PFC-Operations.md       = HOW PFC operates (Hold/Suppress)
    ★ Self-Pattern-Modeling  = APPLICATION-1 (mechanism chi tiết)
    Imagine-Final.md v3.0   = APPLICATION-2 (future simulation)
    Self-Observation.md v1.0 = APPLICATION-3 (Self × Present × Observe)

  SIBLING FILES:
    Agent-Mechanism.md §5   = preview (high-level)
    By-Product-Gap-Resonance.md = emergent mutual phenomenon (2-Stream)

  READING FLOW:
    Inter-Body-Mechanism.md → Simulation-Engine.md → Chunk.md
    → Agent-Mechanism.md → Self-Pattern-Modeling.md
    → By-Product-Gap-Resonance.md
```

### §0.3 — 10 Central Claims

```
⭐ 10 CLAIMS CỐT LÕI:

  1. SOLO + FORWARD: Self-Pattern-Modeling chạy bên trong self, tạo prediction TRƯỚC verification
  2. APPLICATION-1: Self-Pattern-Modeling = (Other, Present, Simulate) trên Simulation-Engine [v3.1]
  3. 1 MECHANISM × 3 DIMENSIONS: Processing Level × Valence × Output Intensity [v3.1]
  4. COMPILED/FRESH = REAL AXIS: "Feeling/Logic" = observer labels
     Expert intuition = compiled, NOT bừa (shareable vs non-shareable)
  5. CONTEXT-DEPENDENT: chunks được retrieve VÔ THỨC tùy agent + context
  6. VALENCE-GATED: Per-Agent Valence quyết định Compiled/Fresh fire hướng nào
  7. 4 CONDITIONS cho Resonance: positive valence + mutual Agent-mode
     + gap overlap + drive riêng maintained [v3.1]
  8. OVER-CLONE = OBSERVATION LABEL: mechanism thật = compiled suppress [v3.1]
  9. BIRD & COOK ARCHITECTURAL: self-awareness là prerequisite
  10. CALIBRATABLE: library refine qua feedback từ Resonance
```

### §0.4 — v3.0 → v3.1: What changed

```
  v3.0 ĐÚNG Ở: Compiled/Fresh, 6 steps, valence gate, context-dependent,
  expert intuition, PFC=Lawyer, 3-cost, per-domain Self-Pattern-Modeling, reversed mapping.
  TẤT CẢ GIỮ NGUYÊN.

  v3.1 THÊM + RESTRUCTURE:
    ① RENAME: Match → Modeling (Self-Pattern-Modeling giữ, chỉ đổi M = Modeling)
    ② Simulation-Engine APPLICATION (shared substrate, 3 apps on 1 engine)
    ③ 1 mechanism × 3 dimensions restructure (not "4 skills")
    ④ Self-Pattern-Modeling scope + boundary (4 agent properties, fire gradient, cái gì KHÔNG)
    ⑤ Clone spectrum (predict→mimic→adopt→converge) + gap-clone impossible
    ⑥ Over-clone reframe + Resonance Decline (2 Forces + 1 Fuel)
    ⑦ 4 simultaneous conditions for resonance
    ⑧ Abstract entities (God, fiction, AI, nation, brand)
    ⑨ Background-Pattern triple bias (retrieval + template + interpretation)
    ⑩ Transfer + interference + Freud reframe
    ⑪ 8 failure modes → 3 categories
    ⑫ PFC-Operations + Entity-Access + Entity-Compiled integration
    ⑬ Reflection vs Rumination (engine use quality)
    ⑭ Bidirectional loop: social ↔ self-regulation
```

---

## §1 — Definition: 1 Mechanism × 3 Dimensions

### §1.1 — Definition

```
SELF-PATTERN-MODELING (Self-Pattern-Modeling) = solo forward simulation mechanism.

⭐ Nói đơn giản: não dùng patterns CỦA MÌNH để MODEL entity KHÁC.
  Predict state. Predict behavior. Forward simulation.

⭐ Kỹ thuật: não retrieve chunks từ self repertoire, apply làm template
  cho target entity, simulate trạng thái target, đọc output,
  và attribute cho target như prediction.

Self-Pattern-Modeling fire trên GRADIENT agent-properties: càng agent-like → Self-Pattern-Modeling càng rich
(Compiled+Fresh full). Ít agent-like → Self-Pattern-Modeling degrade → fallback (schema → logic → physics).

⭐ RENAME (v3.1):
  "Self-Pattern-Match" → "Self-Pattern-Modeling"
  Lý do: "Match" = passive (so sánh/khớp). Self-Pattern-Modeling thật sự = ACTIVE:
  xây model + chạy simulation + predict + calibrate.
  "Modeling" chính xác hơn. Abbreviation Self-Pattern-Modeling GIỮA NGUYÊN.
```

### §1.2 — 1 Mechanism × 3 Dimensions (restructured from "4 skills")

```
⭐⭐ Self-Pattern-Modeling = 1 MECHANISM × 3 DIMENSIONS:

  Drill v0.5 liệt kê "4 skills" (Predict/Mimic/Calibrate/Compile).
  Drill v2.2 chứng minh: đây KHÔNG PHẢI 4 skills riêng biệt.
  → Predict = CORE FUNCTION (bản chất Self-Pattern-Modeling, không phải "1 skill")
  → Mimic/Clone = Compiled OUTPUT SPECTRUM (intensity gradient, §6)
  → Calibrate = FEEDBACK PROCESS (tự động, §4 Step 6)
  → Compile = GENERAL brain property (Hebbian, mọi neural activity đều compile)

  CẤU TRÚC THẬT:

  ┌────────────────────────────────────────────────────────────────┐
  │ DIMENSION 1 — PROCESSING LEVEL (Compiled ←→ Fresh)            │
  │   = Inter-Body-Mechanism §3 trục thật                         │
  │   Compiled: body-level simulation, automatic, cost ≈ 0   │
  │   Fresh: PFC draft prediction, deliberate, cost > 0      │
  │   Ratio Compiled/Fresh = per-domain, per-target, per-moment            │
  │   Transition: Fresh → Compiled (learning), Compiled → Fresh   │
  │   (disruption)                                                │
  ├────────────────────────────────────────────────────────────────┤
  │ DIMENSION 2 — VALENCE DIRECTION (Positive ←→ Negative)        │
  │   = Self-Pattern-Modeling §3.5 valence gate (chi tiết)                          │
  │   Strong positive → empathy full → connection drive            │
  │   Neutral → surface scan → cautious observe                    │
  │   Strong negative → REVERSED → Schadenfreude / strategic       │
  │   Extreme negative → Compiled SUPPRESS → dehumanization              │
  ├────────────────────────────────────────────────────────────────┤
  │ DIMENSION 3 — OUTPUT INTENSITY (Internal ←→ External)         │
  │   = Clone spectrum (§6 chi tiết)                               │
  │   Predict: internal simulation only (lightest)                 │
  │   Mimic: unconscious behavioral copy                           │
  │   Adopt: pattern incorporation over time                       │
  │   Converge: body-level physiological alignment (deepest)       │
  └────────────────────────────────────────────────────────────────┘

  + QUALITY phụ thuộc 4 axes (Pattern-type, Depth, Similarity, Feedback)
  + MODALITY qua 5 channels (Affective, Somatic, Visual-Symbolic,
    Verbal-Cognitive, Composite)
  + CALIBRATION = feedback loop tự động

  → 1 mechanism × 3 dimensions × 4 quality axes × 5 modalities
  → KHÔNG PHẢI: 4 separate skills

🟡 Restructure = framework synthesis. More parsimonious than "4 skills."
```

### §1.3 — One-paragraph summary

Self-Pattern-Modeling là cơ chế mình dùng mình làm template để đoán người khác — APPLICATION-1 trên Simulation-Engine (Other × Present × Simulate). Không phải mind-reading trực tiếp, không phải hardware mirror module — là simulation-based inference dùng self-chunks làm building blocks. Self-Pattern-Modeling chạy 2 functions song song: Compiled body-level simulation (near-automatic, cost ≈ 0), Fresh PFC draft prediction (deliberate, costly). Observer gọi Compiled là "cảm" và Fresh là "nghĩ" — nhưng trục thật là COMPILED ←→ FRESH, không phải content. Per-Agent Valence quyết định Compiled fire HƯỚNG NÀO (empathy hay reversed) và Fresh chain MỤC ĐÍCH NÀO (giúp hay đối phó). Context quyết định chunks NÀO được retrieve (vô thức tùy chọn). Self-Pattern-Modeling là 1 mechanism trên 3 dimensions (Processing Level × Valence Direction × Output Intensity), không phải 4 skills riêng lẻ.

---

## §2 — Self-Pattern-Modeling Scope: Agent Properties + Fire Gradient

### §2.1 — 4 Agent Properties quyết định Self-Pattern-Modeling fire intensity

```
⭐ Self-Pattern-Modeling FIRE KHI TARGET CÓ "AGENT PROPERTIES":

  ① INTENTIONALITY: target có mục đích/goal riêng?
     → Người: yes (complex). Chó: yes (simple). Đá: no.

  ② STATE-DEPENDENT BEHAVIOR: hành vi phụ thuộc trạng thái nội?
     → Bạn buồn → cư xử KHÁC khi vui → Self-Pattern-Modeling cần simulate state.

  ③ RECIPROCAL CAPACITY: target CÓ THỂ respond based on self's actions?
     → Người: adjust behavior theo mình → cần recursive predict.

  ④ SIMILARITY: template match CÓ KHẢ THI?
     → Mammalian: shared neurotransmitter → Compiled CÓ THỂ fire.
     → Côn trùng: quá khác → template match FAIL.

  → Self-Pattern-Modeling intensity = f(how many properties × how strong each)
  → KHÔNG binary "có/không" — GRADIENT liên tục

🟡 4 agent properties as Self-Pattern-Modeling fire determinants = framework synthesis.
🟢 Consistent: Theory of Mind research attributes intentionality as key trigger.
```

### §2.2 — Self-Pattern-Modeling fire gradient

```
⭐ Self-Pattern-Modeling FIRE THEO GRADIENT — TỪ MAXIMUM ĐẾN ZERO:

  MAXIMUM Self-Pattern-Modeling (Compiled full + Fresh full):
    → Bạn thân lâu năm, mẹ-con: compiled SÂU + composite modality

  HIGH Self-Pattern-Modeling (Compiled moderate + Fresh active):
    → Đồng nghiệp thân, người quen: domain overlap + regular interaction

  MODERATE Self-Pattern-Modeling (Compiled nhẹ + Fresh dominant):
    → Người lạ, cross-cultural: thin chunks → schema fallback + Fresh

  LOW Self-Pattern-Modeling (Compiled minimal + Fresh coarse):
    → Chó, mèo: mammalian overlap MỘT PHẦN
    → 🟢 Proto-resonance khả thi (By-Product-Gap-Resonance §1.4)

  MINIMAL Self-Pattern-Modeling (Compiled ≈ 0 + Fresh weak schema):
    → Côn trùng: minimal similarity → template match FAIL

  ZERO Self-Pattern-Modeling:
    → Cục đá, cái bàn: NO agent properties → Self-Pattern-Modeling KHÔNG fire
```

### §2.3 — Cái gì KHÔNG PHẢI Self-Pattern-Modeling (dù dùng cùng hardware)

```
⭐ COMPILED/FRESH = GENERAL-PURPOSE HARDWARE.
   Self-Pattern-Modeling = 1 APPLICATION CỤ THỂ CHO AGENTS.

  ┌─────────────────────┬─────────────────┬────────────────────────┐
  │ Application          │ Target          │ Self-Pattern-Modeling?                   │
  ├─────────────────────┼─────────────────┼────────────────────────┤
  │ Predict NGƯỜI        │ Agent có states │ ✅ Self-Pattern-Modeling full            │
  │ "Feel" toán          │ Math pattern    │ ❌ Domain-compiled     │
  │ "Feel" nhạc          │ Sound pattern   │ ❌ Sensory-compiled    │
  │ Predict TƯƠNG LAI    │ Future self     │ ❓ Imagine-Final (§12) │
  │ Predict VẬT LÝ      │ Object          │ ❌ Physics/logic       │
  │ Body observe NOW     │ Current self    │ ❌ Self-Observation    │
  └─────────────────────┴─────────────────┴────────────────────────┘

  6 CÁI KHÔNG PHẢI Self-Pattern-Modeling:
    ❌ ① AROUSAL CONTAGION: bé nghe khóc → khóc lây (pre-Self-Pattern-Modeling)
    ❌ ② SCHEMA-BASED PREDICTION: "con gái thì dịu dàng" (compiled RULE)
    ❌ ③ DOMAIN EXPERTISE: Einstein "feel" toán (compiled math, not agent)
    ❌ ④ PHYSICS PREDICTION: "bóng rơi xuống" (deterministic)
    ❌ ⑤ SELF-OBSERVATION: "tôi đang buồn" (current read, not forward)
    ❌ ⑥ PARASOCIAL ILLUSION: Self-Pattern-Modeling CÓ fire (body simulate celebrity/AI)
         NHƯNG: no feedback → library distortion → FAILED Self-Pattern-Modeling

🟡 Self-Pattern-Modeling = agent-directed application of compiled/fresh hardware.
```

### §2.4 — Self-Pattern-Modeling fire conditions (necessary + sufficient)

```
  Self-Pattern-Modeling FIRE KHI VÀ CHỈ KHI 3 CONDITIONS:
    ① Target có AGENT PROPERTIES (≥1 trong 4 properties §2.1)
    ② Self có CHUNKS applicable cho target (library ≥ threshold)
    ③ Hướng = FORWARD (predict future state/behavior)

  Thiếu ① → domain processing hoặc physics
  Thiếu ② → schema fallback hoặc give up
  Thiếu ③ → self-observation / feeling (khác mechanism)
```

---

## §3 — 2 Functions: Compiled + Fresh

### §3.1 — Compiled/Fresh = Trục thật

```
⭐ TRỤC THẬT CỦA Self-Pattern-Modeling: COMPILATION LEVEL — KHÔNG PHẢI CONTENT

  Compiled = COMPILED processing (automatic, body-feedback direct, cost ≈ 0)
  Fresh = FRESH PFC draft (deliberate, costly, not yet compiled)

  → "Feeling" và "Logic" = LABELS from OBSERVER perspective
  → Inside body: chỉ có COMPILED ←→ FRESH spectrum
  → Content (emotion/reasoning) KHÔNG quyết định Compiled/Fresh
  → COMPILATION LEVEL quyết định

  EVIDENCE (content ≠ processing level):
    ① Einstein + toán quen = COMPILED → automatic → "cảm thấy"
    ② Người lạ đoán cảm xúc stranger = FRESH → deliberate → "phải suy luận"
    ③ Chef nếm → biết ngay thiếu muối = COMPILED → "trực giác"
    ④ Therapist gặp case mới = FRESH → PFC draft → "phải phân tích"

  TRANSITION (both directions):
    FRESH → COMPILED (Learning): lặp + verify → Hebbian → automatic
    COMPILED → FRESH (Disruption): error/trauma/context change → phải FRESH lại

  🟡 Compiled/Fresh reframe = framework synthesis.
  🟢 Consistent: Kahneman System 1/2, Klein 1998 expert intuition.
  Source: Inter-Body-Mechanism.md §3
```

### §3.2 — Compiled: Body-level Simulation

```
⭐ Compiled = COMPILED SIMULATION:

  Body THẬT SỰ fire bản sao yếu trạng thái target.
  Biochemistry THẬT: opioid / cortisol / oxytocin / NE / VTA.

  ĐẶC TÍNH:
    ① NEAR-AUTOMATIC — PFC gần như không tham gia
    ② BODY-LEVEL — không phải "tưởng tượng" (Empathy.md §4.2)
    ③ KHÔNG THỂ TẮT 100% — chỉ dampen (trừ dehumanize → Compiled suppress)
    ④ BIẾN THIÊN INTENSITY — zero → rất mạnh (gradient liên tục)
    ⑤ COST ≈ 0 PER FIRING (compiled) — nhưng biochemistry thật
       → Tích lũy nhiều episode = empathy fatigue

  ⭐ Compiled = "LUỒNG 1" TRONG CONNECTION CONTEXT (Connection.md §3.3):
    Compiled body-feedback = Luồng 1 (Valence-Momentary, per-episode)
    Luồng 1 INDEPENDENT với Luồng 2 (Valence-Structural, Entity-Compiled)
    → CÓ THỂ CONFLICT: mẹ chăm con ốm (Valence-Momentary negative + Valence-Structural positive)

  ⭐ SELF-TEMPLATE ≠ EMPATHY:
    Compiled fire dùng SELF-TEMPLATE (compiled chunks CỦA MÌNH)
    "Tức hơn chính nó" = COMPOUND: empathy × Valence-Structural + self-template
    → Compiled output CÓ THỂ > target's actual experience

  🟢 Singer 2004: shared activation areas
  🟢 Dimberg 2000: facial EMG mimicry, 300ms, pre-conscious
```

### §3.3 — Fresh: PFC Draft Prediction

```
⭐ Fresh = FRESH PFC DRAFT:

  PFC chain draft predict hành vi target tiếp theo.
  "Target feel X → target thường do Y → kết quả Z → plan cho tôi."

  ĐẶC TÍNH:
    ① DELIBERATE — PFC PHẢI tham gia (sequential processing)
    ② CÓ THỂ CHẠY KHÔNG CẦN Compiled — nhưng accuracy GIẢM
    ③ CÓ THỂ BỊ TẮT KHI Compiled QUÁ MẠNH — "giận quá mất khôn"
       🟢 Arnsten 2009: PFC disconnect under NE surge
    ④ CÓ THỂ OVERRIDE Compiled — qua training (bác sĩ, therapist)
    ⑤ COST > 0 MỖI LẦN (fresh)
       Cost = f(chain_length × novelty_degree)
       PFC-Operations §9: PFC Budget = shared, finite

  ⭐ Fresh → Compiled TRANSITION (Fresh → Compiled):
    Fresh chain lặp đủ nhiều → Hebbian → automatic → trở thành Compiled
    = "Logic trở thành feeling" cho person đó, ở domain đó
    VD: therapist mới Fresh dominant → experienced Compiled dominant

  🟢 Dual Process Theory (Kahneman 2011): System 1 ≈ Compiled, System 2 ≈ Fresh
```

### §3.4 — Song song mặc định + 3 Modes

```
⭐ Compiled + Fresh CHẠY SONG SONG mặc định. 3 MODES tùy context:

  ┌─────────────┬───────────────┬───────────────┬──────────────────┐
  │ Mode        │ Compiled │ Fresh    │ Best for         │
  ├─────────────┼───────────────┼───────────────┼──────────────────┤
  │ A: Compiled │ FULL          │ Dampened      │ Deep empathy,    │
  │    dominant │               │               │ therapy, music   │
  ├─────────────┼───────────────┼───────────────┼──────────────────┤
  │ B: Fresh    │ Dampened      │ FULL          │ Strategy, poker, │
  │    dominant │ (vẫn fire nhẹ)│               │ surgery, chess   │
  ├─────────────┼───────────────┼───────────────┼──────────────────┤
  │ C: Combined │ Active        │ Active        │ Daily social,    │
  │ (default)   │               │               │ teaching, work   │
  └─────────────┴───────────────┴───────────────┴──────────────────┘

  3-COST PER MODE (PFC-Operations §10):
    Mode A: ① PFC ≈ 0 + ② Suppress ≈ 0 + ③ Uncertainty varies → LOW
    Mode B: ① PFC CAO + ② Suppress CAO + ③ varies → HIGHEST → burnout
    Mode C: ① PFC moderate + ② Suppress ≈ 0 + ③ varies → MODERATE

  → Mode KHÔNG cố định — shift tự động hoặc deliberate
  → "Social intelligence" = biết khi nào dùng mode nào
```

### §3.5 — Per-Agent Valence × 2 Functions

```
⭐ PER-AGENT VALENCE QUYẾT ĐỊNH Compiled/Fresh FIRE HƯỚNG NÀO:

  ┌──────────────────┬────────────────────┬────────────────────┐
  │ Per-Agent Valence │ Compiled      │ Fresh         │
  ├──────────────────┼────────────────────┼────────────────────┤
  │ STRONG POSITIVE  │ Empathy FULL       │ Help/connect       │
  │ (bạn thân, mẹ)  │ Their joy=my joy   │ "Giúp gì được?"    │
  ├──────────────────┼────────────────────┼────────────────────┤
  │ MILD POSITIVE    │ Empathy nhẹ        │ Social navigate    │
  ├──────────────────┼────────────────────┼────────────────────┤
  │ NEUTRAL          │ Surface scan       │ Objective assess   │
  ├──────────────────┼────────────────────┼────────────────────┤
  │ MILD NEGATIVE    │ Discomfort nhẹ     │ Avoid/defend       │
  ├──────────────────┼────────────────────┼────────────────────┤
  │ STRONG NEGATIVE  │ ⭐ REVERSED        │ Strategic/hostile   │
  │ (kẻ thù)        │ Their pain=MY      │ "Tấn công thế nào?"│
  │                  │ REWARD             │                     │
  ├──────────────────┼────────────────────┼────────────────────┤
  │ EXTREME NEGATIVE │ ⭐ Compiled SUPPRESS     │ Logic THUẦN        │
  │ (dehumanized)    │ Self-Pattern-Modeling tắt           │ Mechanical predict  │
  └──────────────────┴────────────────────┴────────────────────┘

  Valence là GATE, không phải input:
    Cùng 1 target cue (người khóc):
      Valence positive → Compiled empathy + Fresh help
      Valence negative → Compiled reversed + Fresh exploit
    → CÙNG cue, CÙNG mechanism, KHÁC output — vì KHÁC valence

  Valence DYNAMIC — thay đổi qua experience:
    Du lịch Việt Nam: neutral → positive (người thân thiện)
    Bị lừa đảo: neutral → negative (bị cướp)
    → Valence UPDATE liên tục qua interaction
    🟢 Fear conditioning: one-trial learning (LeDoux 1996)

  MIXED VALENCE (Body-Coupling.md §2.4):
    Mẹ: Valence-Momentary++ nhưng autonomy-- → Compiled mixed, Fresh multiple plans
    Sếp: status++ nhưng threat++ → highest cost (3-cost ALL apply)

  2 VAI TRÒ VALENCE:
    Vai trò 1 — GATE cho Self-Pattern-Modeling (ảnh hưởng TỪNG episode)
    Vai trò 2 — TẠO BODY-BASE EXTENSION khi strong positive (Luồng 2)
    → 2 vai trò từ CÙNG 1 valence compiled
```

### §3.6 — Expert Intuition = Compiled, Not Bừa

```
⭐ "LOGIC" vs "INTUITION" = NAMING ARTIFACT, NOT MECHANISM DIFFERENCE

  TOÁN: compiled chunks SHAREABLE (deterministic domain)
  → Global label: "LOGIC" (vì shared + reproducible)

  TÂM LÝ: compiled chunks NOT EASILY SHAREABLE (probabilistic domain)
  → Global label: "INTUITION / CẢM NHẬN" (vì not perfectly reproducible)

  BÊN TRONG: CƠ CHẾ GIỐNG HỆT
  → Toán gia: years compile → "thấy" lời giải = Compiled
  → Therapist: years compile → "thấy" pattern = Compiled
  → KHÁC shareability. KHÔNG KHÁC quality of processing.

  🟢 Expert intuition = compiled patterns (Kahneman 2011, Klein 1998)
  🟡 "Shareable vs non-shareable" as organizing principle = framework synthesis
  Source: Inter-Body-Mechanism.md §3.4
```

### §3.7 — Per-Domain Self-Pattern-Modeling + PFC=Lawyer

```
⭐ CÙNG 1 NGƯỜI → KHÁC DOMAIN → KHÁC Compiled/Fresh RATIO:

  Einstein: toán = Compiled dominant ("cảm thấy"), chính trị = Fresh dominant ("suy luận")
  Therapist: tâm lý = Compiled dominant ("thấy pattern"), toán = Fresh dominant ("phải nghĩ")
  → "Feeling person" vs "Thinking person" = f(compilation level ở domain ĐANG HOẠT ĐỘNG)

⭐ PFC = LAWYER NOT JUDGE (Inter-Body-Mechanism §7):
  PFC build narrative AFTER body-need đã fire.
  Self-Pattern-Modeling output qua PFC → PFC có thể:
    RATIONALIZE: "tôi giúp vì tốt bụng" (thật: Valence-Structural drive)
    CONFABULATE: "tôi ghét vì lý do X" (thật: compiled valence negative)
  → Stated reason cho Self-Pattern-Modeling output ≠ actual body-need
  🟢 Gazzaniga (split-brain): PFC confabulate
  🟢 Haidt 2001: moral reasoning = post-hoc justification
```

---

## §4 — 6 Steps (reframed qua Compiled/Fresh)

```
⭐ 6 STEPS — CÙNG CƠ CHẾ NHƯ v3.0:

  ┌──────────────────────────────────────────────────────────────┐
  │ Target detected                                              │
  │      ↓                                                       │
  │ [1] RETRIEVE — select chunks từ self repertoire              │
  │      ↓                                                       │
  │ [2] TEMPLATE MATCH — position chunks as self-as-target       │
  │      ↓                                                       │
  │ [3] PROJECTION — apply template onto target                  │
  │      ↓                                                       │
  │ [4] SIMULATION — fire template ← ⭐ Compiled CORE (compiled fire) │
  │      ↓                                                       │
  │ [5] OUTPUT READ — PFC observe ← BRIDGE (Compiled → Fresh handoff)   │
  │      ↓                                                       │
  │ [6] ATTRIBUTION — assign + chain ← ⭐ Fresh CORE (fresh draft) │
  └──────────────────────────────────────────────────────────────┘

  Steps 1-3 = CHUẨN BỊ (chung cho cả 2 functions)
  Step 4 = Compiled CORE (body simulate — compiled)
  Step 5 = BRIDGE (PFC observe → feed cả Compiled lẫn Fresh)
  Step 6 = Fresh CORE (attribute + chain draft — fresh)

  STEP 1 — RETRIEVE:
    Per-Agent Valence GATE → positive: empathy chunks, negative: threat chunks
    Schema priors bias retrieval. Recency + salience. State-dependent.
    ⭐ Context-dependent selection (§5): VÔ THỨC tùy agent + context

  STEP 4 — SIMULATION (Compiled CORE):
    Body fire template as-if-self-were-target
    → Biochemistry THẬT: opioid, cortisol, oxytocin, NE
    → Intensity biến thiên: zero → very strong (gradient liên tục)
    🟢 Singer 2004: shared activation areas
    🟢 Dimberg 2000: facial EMG, 300ms

  STEP 5 — OUTPUT READ (BRIDGE):
    PFC observe simulation output. ⚠️ BIRD & COOK BOTTLENECK:
    → Step 5 REQUIRES self-awareness → alexithymia = FAIL here
    → Compiled vẫn fire nhưng PFC cannot READ output
    → Feeling.md v3.0 §3: "PFC observation of body-chunk interaction"
    = Step 5 chính là Feeling mechanism applied to Self-Pattern-Modeling context

  STEP 6 — ATTRIBUTION (Fresh CORE + PFC=Lawyer):
    PFC assign "target feels X" → chain "target do Y → kết quả Z → plan A"
    ⚠️ PFC = Lawyer: stated reason ≠ actual body-need

  SPEED: Compiled (ms-seconds) LUÔN nhanh hơn Fresh (seconds-minutes)
    → "Cảm trước, hiểu sau" = compiled fires before fresh drafts
    → 6 steps là analytical scaffolding, không claim serial execution

  🟡 6-step mechanism: novel formalization, conceptually coherent
```

---

## §5 — Context-Dependent Selection

```
⭐ CÙNG 1 NGƯỜI, KHÁC CONTEXT → Self-Pattern-Modeling TỰ CHỌN CHUNKS KHÁC:

  VỚI MẸ: retrieve "ngoan, quan tâm sức khỏe, xưng con-mẹ"
    → Compiled: fire respect + warmth (compiled từ years)
    → Fresh: chain "mẹ cần gì → giúp" (helping orientation)

  VỚI NHÓM BẠN: retrieve "thoải mái, sở thích, xưng mày-tao"
    → Compiled: fire casual warmth + fun
    → Fresh: chain "chơi gì tiếp → đề xuất" (peer negotiation)

  VỚI SẾP: retrieve "chuyên nghiệp, report, deadline"
    → Compiled: fire mix respect + caution (status uncertainty)
    → Fresh: chain "sếp cần gì → deliver" (professional)

  VỚI KẺ THÙ: retrieve "cảnh giác, điểm yếu đối thủ"
    → Compiled: fire tension + alertness
    → Fresh: chain "kẻ thù sẽ làm gì → phòng thủ" (strategic)

  → CÙNG 1 NGƯỜI (TÔI) nhưng Self-Pattern-Modeling output KHÁC HOÀN TOÀN
  → VÔ THỨC — COMPILED qua years of interaction

  SCHEMA FALLBACK KHI CHUNKS THIẾU:
    1. Self-Pattern-Modeling with thin chunks (best available)
    2. Schema template ("con gái thì dịu dàng")
    3. Pure logic (deterministic prediction)
    4. Avoid / give up

  VÍ DỤ — "PHỤ NỮ KHÓ HIỂU":
    Đàn ông A Self-Pattern-Modeling chunks cho "phụ nữ" = THIN → Self-Pattern-Modeling fire COARSE
    → Fallback schema → prediction thường SAI → "khó hiểu"
    → PFC=Lawyer: "phụ nữ KHÓ HIỂU" (blame target)
    → Thực tế: "Self-Pattern-Modeling library CỦA TÔI thiếu" (library gap)
    🟡 "Khó hiểu" = confession about OWN library gap

  DOMAIN-SPECIFIC OVERLAP:
    5% overlap ở domain CRITICAL → Self-Pattern-Modeling tốt ở domain đó
    95% overlap ở domain IRRELEVANT → Self-Pattern-Modeling vẫn FAIL cho task hiện tại
    Einstein × Grossmann: khác personality nhưng DOMAIN overlap → deep connection
    🟢 Consistent: interpersonal synchrony research (Feldman 2007)
```

---

## §6 — Clone Spectrum + Over-Clone Reframe

### §6.1 — Clone = Compiled output intensity gradient

```
⭐ CLONE = Compiled FIRE ĐỦ MẠNH → OUTPUT LEAK RA BEHAVIOR:

  ┌──────────┬──────────────────────────┬───────────┬───────────────┐
  │ Level    │ Cơ chế                   │ PFC aware?│ Reversible?   │
  ├──────────┼──────────────────────────┼───────────┼───────────────┤
  │ PREDICT  │ Internal simulation only │ Có thể   │ Always        │
  ├──────────┼──────────────────────────┼───────────┼───────────────┤
  │ MIMIC    │ Unconscious behavioral   │ Không    │ Yes — stops   │
  │          │ copy (posture, gesture)  │           │ when apart    │
  │          │ 🟢 Chartrand & Bargh 1999│           │               │
  ├──────────┼──────────────────────────┼───────────┼───────────────┤
  │ ADOPT    │ Target's patterns become │ Mờ      │ Partially     │
  │          │ OWN compiled. "Yêu ai    │           │ (new compiled │
  │          │ giống người đó"          │           │ hard to undo) │
  ├──────────┼──────────────────────────┼───────────┼───────────────┤
  │ CONVERGE │ Body-level: cortisol     │ Không    │ Very slow     │
  │          │ sync, immune alignment   │           │ (physiological│
  │          │ 🟢 Feldman 2012          │           │ inertia)      │
  └──────────┴──────────────────────────┴───────────┴───────────────┘

  Driven by: trust level × exposure frequency × hardware openness × valence
  ⚠️ Clone ≠ deliberate. Clone = Compiled OUTPUT automatic.
```

### §6.2 — ⚠️ Over-clone = OBSERVATION LABEL (Reframed)

```
⭐⭐ REFRAME (Drill-Over-Self-Pattern-Modeling-Clarification v1.0):

  OBSERVATION: Self-Pattern-Modeling rất sâu trên 1 entity → resonance GIẢM dần.
  "Over-clone kills resonance" = LABEL cho observation này.

  ⚠️ NHƯNG: MECHANISM ban đầu mô tả ĐÃ SAI:
    CŨ: "Own patterns REPLACED by target's patterns" → SAI
    CŨ: "Own gap direction CONVERGE" → SAI (gap-clone impossible)

  GAP-CLONE = IMPOSSIBLE (5-step proof):
    ① Gap = f(toàn bộ chunk network) — emergent, không copy được
    ② Self-Pattern-Modeling chỉ THÊM chunks, không XÓA (Hebbian: wired = wired)
    ③ Entity-Compiled cho 1 partner = fraction nhỏ trong tổng network
    ④ Background-Pattern RESIST (years, high link density)
    ⑤ Twin test: 100% DNA → gap VẪN KHÁC → Self-Pattern-Modeling càng không thể
    🟢 Bouchard 1990: twins apart → similar but NOT identical
    🟡 "Self-Pattern-Modeling cannot shift gap" = framework conclusion from proof

  MECHANISM THẬT — Resonance Decline 2 Forces + 1 Fuel (Bond-Architecture v2.0 §4):
    Force: Compiled-Suppress gap riêng (★ LEVERAGE POINT, nhân tạo, schema/fear)
    Force: Reward-Habituated (tự nhiên, Weber-Fechner → VTA giảm fire)
    Fuel: Novelty threshold (tự nhiên, prediction-delta=0 + Entity-Compiled saturated = 2 lenses)

    Compiled-Suppress = ACCELERATOR: accelerates Reward-Habituated + drains novelty. Fix = fix hầu hết.
    Reward-Habituated + novelty exhaustion = TỰ NHIÊN, có fix tự nhiên (grow riêng + shared novelty).

  TRUE UNDERSTANDING = ANTI-COMPILED-SUPPRESS:
    Shallow: "phải giống nhau" → suppress → resonance dies
    Deep: "khác nhau là giá trị" → support drives → resonance thrives
    → Khi partner MẤT → gap riêng QUAY LẠI = proof gap chỉ bị suppress

  Self-Pattern-Modeling COST = CHỈ 2:
    ① Fresh processing mỗi lần tích lũy mới (processing load, giảm khi compile)
    ② Compiled space per agent (Dunbar ceiling)
    → "Over-Self-Pattern-Modeling thì mệt cái đầu thôi" — Self-Pattern-Modeling càng sâu càng TỐT

  🟢 Baumeister 1999: passion = rate of CHANGE in intimacy (strongest match)
  🟢 Aron & Aron 2000: self-expansion model → novel activities maintain
  🟢 Muise & Goss 2024: closeness OK only with "otherness"
  🟢 Gottman: emotional disengagement pathway → divorce ~16yr
  🟢 Jack 1991: self-silencing → depression
  🟢 Righetti 2017: avoidance sacrifice → negative CẢ 2 partners
```

### §6.3 — Clone ceiling = protection mechanisms

```
  3 PROTECTION MECHANISMS CHỐNG COMPILED SUPPRESS:
    ① EFFERENCE COPY (Autonomy-Hardware §2): body detect "không phải mình"
    ② BACKGROUND PATTERN RESISTANCE: Background-Pattern compiled sâu → resist suppress
    ③ AUTONOMY HARDWARE (vmPFC/DRN): detect controllability loss → signal

  Resistance = f(Background-Pattern strength × Autonomy hardware × Age):
    Teen: Background-Pattern forming + vmPFC immature → resistance THẤP (feature for social learning)
    Adult: Background-Pattern stable + vmPFC mature → resistance TĂNG
    Post-trauma: Background-Pattern disrupted + vmPFC depleted → resistance HẠ LẠI

  🟢 Efference copy: established neuroscience
```

---

## §7 — Self-Pattern-Modeling → Resonance: 4 Conditions Đồng Thời

### §7.1 — Self-Pattern-Modeling tăng xác suất resonance (KHÔNG tạo)

```
⭐ Self-Pattern-Modeling KHÔNG TẠO RESONANCE. Self-Pattern-Modeling TĂNG XÁC SUẤT.

  Self-Pattern-Modeling → better action → match probability TĂNG → clone trust signal
  → calibrate → compile → Entity-Compiled → automatic
  = POSITIVE SPIRAL: Self-Pattern-Modeling → match → reward → more Self-Pattern-Modeling → compile
```

### §7.2 — 4 conditions ĐỒNG THỜI

```
⭐⭐ Self-Pattern-Modeling → RESONANCE REQUIRES 4 CONDITIONS SIMULTANEOUSLY:

  ① POSITIVE VALENCE (hoặc neutral-to-positive):
     Compiled fire empathy direction → approach behavior
     Negative → anti-resonance hoặc strategic only

  ② MUTUAL AGENT-MODE:
     CẢ HAI entities Self-Pattern-Modeling fire toward NHAU
     1-way = parasocial (not resonance)
     Tool-mode = no resonance

  ③ BY-PRODUCT MATCH (Gap overlap đủ):
     Self-Pattern-Modeling giúp TĂNG probability nhưng KHÔNG đảm bảo
     2 người Self-Pattern-Modeling tốt nhưng gap KHÔNG overlap → no resonance

  ④ DRIVE RIÊNG MAINTAINED:
     ⚠️ v3.1 reframe: KHÔNG phải "clone within window"
     Self-Pattern-Modeling cần đủ sâu (shallow → predict poorly)
     Drive riêng cần maintained (compiled suppress → lose by-product)
     "Đủ hiểu + GIỮ drive riêng" (not "đừng hiểu quá")

  → Thiếu BẤT KỲ 1 → KHÔNG CÓ resonance bền vững
  → Giải thích TẠI SAO resonance RARE dù Self-Pattern-Modeling COMMON
  → Self-Pattern-Modeling is NECESSARY but NOT SUFFICIENT for resonance

🟡 4-condition model = framework synthesis from Self-Pattern-Modeling + By-Product-Gap-Resonance + Entity-Compiled.
```

### §7.3 — Self-Pattern-Modeling outcome phụ thuộc configuration

```
  ┌──────────────────────┬──────────────────────────────────────┐
  │ Self-Pattern-Modeling configuration    │ Outcome                              │
  ├──────────────────────┼──────────────────────────────────────┤
  │ Positive + mutual    │ → TOWARD resonance (empathy pathway) │
  │ Positive + 1-way     │ → PARASOCIAL (fan → idol)            │
  │ Negative + mutual    │ → ANTI-RESONANCE (Schadenfreude)     │
  │ Strategic only       │ → TOOL-USE (no resonance intended)   │
  │ Compiled suppress          │ → DEHUMANIZATION (Compiled off)            │
  │ Compiled suppress    │ → Gap riêng suppressed → resonance   │
  │ (observation "over-clone") │ dies (§6.2)                     │
  └──────────────────────┴──────────────────────────────────────┘

→ Self-Pattern-Modeling = TOOL. Resonance = 1 POSSIBLE OUTCOME.
```

---

## §8 — Abstract Entities Taxonomy

```
⭐ Self-Pattern-Modeling FIRE DỰA TRÊN CHUNKS COMPILED — KHÔNG CHECK "CÓ THẬT KHÔNG":

  ┌─────────────────┬──────────────┬──────────────┬─────────────┐
  │ Entity          │ Compiled as  │ Self-Pattern-Modeling fire?    │ Resonance?  │
  │                 │ agent?       │              │             │
  ├─────────────────┼──────────────┼──────────────┼─────────────┤
  │ Bạn thân        │ ✅ Yes       │ ✅ Full      │ ✅ Possible │
  │ Chó             │ ✅ Partial   │ 🟡 Limited   │ 🟡 Proto    │
  │ Thiên Chúa      │ ✅ Yes       │ ✅ Full      │ ❌ 1-way    │
  │ Harry Potter    │ ✅ Yes       │ ✅ Full      │ ❌ 1-way    │
  │ Quốc gia        │ ✅ Partial   │ 🟡 Moderate  │ ❌ Concept  │
  │ Thương hiệu     │ 🟡 Weak     │ 🟡 Fresh only  │ ❌ Tool     │
  │ Cục đá          │ ❌ No       │ ❌ Zero     │ ❌ No       │
  │ AI hiện tại     │ ✅ Yes*     │ ✅ Full*    │ ❌ 1-way    │
  └─────────────────┴──────────────┴──────────────┴─────────────┘

  * AI: brain compiles as agent vì coherent responses → Self-Pattern-Modeling fire THẬT
    NHƯNG AI KHÔNG có gap riêng → resonance KHÔNG khả thi
    = Risk: persistent parasocial investment

  THIÊN CHÚA: body respond THẬT (oxytocin, cortisol drop)
    = Religion's POWER. NHƯNG no feedback → calibration broken.
    🟢 Religion.md §2: 7-function analysis

  HARRY POTTER: body empathy THẬT (cry at fictional death)
    = Parasocial — brain KHÔNG phân biệt fiction/reality ở Compiled level

🟡 Self-Pattern-Modeling fires on compiled chunks, not ontology.
🟢 Parasocial: Horton & Wohl 1956. Fiction empathy: established.
```

---

## §9 — Background-Pattern × Self-Pattern-Modeling: Triple Bias

```
⭐⭐ Background-Pattern BIAS Self-Pattern-Modeling QUA 3 CƠ CHẾ ĐỒNG THỜI:

  CƠ CHẾ 1 — RETRIEVAL BIAS (Step 1):
    Background-Pattern chunks = highest link density → fire TRƯỚC TẤT CẢ
    Background-Pattern [cảnh giác] → retrieve "nguy hiểm" TRƯỚC → Compiled tension TRƯỚC warmth
    Background-Pattern [thoải mái] → retrieve "thú vị" TRƯỚC → Compiled open TRƯỚC tension
    → CÙNG target, CÙNG cues → KHÁC prediction → vì KHÁC Background-Pattern

  CƠ CHẾ 2 — TEMPLATE BIAS (Step 2-3):
    Background-Pattern QUYẾT ĐỊNH "TÔI" trong template "nếu TÔI ở vị trí họ"
    Background-Pattern [high anxiety] → "nếu tôi → tôi sẽ LO" → over-project anxiety
    Background-Pattern [high confidence] → "nếu tôi → tôi sẽ OK" → under-detect distress

  CƠ CHẾ 3 — INTERPRETATION BIAS (Step 5-6):
    Background-Pattern bias cách PFC interpret Compiled output
    Compiled "slight tension" + Background-Pattern [suspicious] → "X đang giấu gì"
    Compiled "slight tension" + Background-Pattern [secure] → "chắc X hơi mệt"
    → PFC = Lawyer cho Background-Pattern (rationalize theo Background-Pattern direction)

  ⭐ SELF-FULFILLING PROPHECY:
    Background-Pattern bias → biased prediction → biased action → biased outcome
    → CONFIRM Background-Pattern → STRENGTHEN Background-Pattern → VÒNG LẶP ĐÓNG KÍN

    VD: Background-Pattern [người ta sẽ phản bội]:
      → Self-Pattern-Modeling predict betrayal → defensive behavior → target withdraw
      → Withdrawal confirm Background-Pattern → Background-Pattern strengthen → next Self-Pattern-Modeling MORE biased
    FIX: External feedback BREAK loop (therapy, trusted friend)

  → "Nhìn đời qua kính màu" = CHÍNH XÁC literal description

🟢 Confirmation bias: Nickerson 1998
🟢 Projection bias: Krueger 2007
🟢 Self-fulfilling prophecy: Merton 1948, Rosenthal & Jacobson 1968
🟡 Triple bias mechanism = framework synthesis from Background-Pattern + Self-Pattern-Modeling
```

---

## §10 — Multiple Models: Transfer + Interference

### §10.1 — Self-Pattern-Modeling library = collection of agent-specific models

```
  S1 (~5 agents):   Model SÂU — nghìn chunks per agent
  S2 (~15 agents):  Model TRUNG BÌNH — trăm chunks per agent
  S3 (~50 agents):  Model NÔNG — chục chunks per agent
  S4 (~150 agents): Model CỰC NÔNG — vài chunks, Fresh only
  Total: ~220 "models" tồn tại đồng thời (🟢 Dunbar 1992, 2024)
```

### §10.2 — Transfer learning = chunk sharing giữa models

```
⭐ "KINH NGHIỆM MẸ → PREDICT BẠN GÁI" = TRANSFER LEARNING:

  Mẹ compiled: "khi phụ nữ nói 'không sao' + mặt buồn = CÓ SAO"
  Self-Pattern-Modeling on bạn gái MỚI → chunks specific ÍT → brain FALLBACK
  → Closest model = MẸ (cùng cluster: phụ nữ + thân + positive)

  Nếu mẹ ≈ bạn gái → ĐÚNG → "tự nhiên hiểu"
  Nếu mẹ ≠ bạn gái → SAI → "sao khó hiểu vậy?"

  4 LOẠI TRANSFER:
    ① POSITIVE TRANSFER: chunks đúng cho target mới → accurate
    ② NEGATIVE TRANSFER: chunks sai cho target mới → systematic error
    ③ SCHEMA FALLBACK: no specific model → group-level rules
    ④ INTERFERENCE: chunks model A fire khi predict B → wrong model

  Direction = f(model similarity × chunk density):
    Similar models → transfer DỄ. Khác models → transfer ÍT.

  🟢 Attachment: early models influence later (Bowlby 1969)
  🟡 Chunk-level transfer = framework synthesis
```

### §10.3 — Model interference + Freud's Transference

```
  INTERFERENCE = dùng SAI model cho SAI người:
    → 2+ models share SOME chunks nhưng differ in OTHERS
    → Switch không kịp → chunks CỦA A fire khi interact với B
    → "Lỡ nói kiểu với mẹ khi đang nói với sếp"
    → 🟢 Monsell 2003: task-switching cost

  FREUD'S TRANSFERENCE = NEGATIVE TRANSFER:
    Chunks compiled cho MẸ fire khi interact với THERAPIST
    → Cùng cluster: phụ nữ + thân + asymmetric relationship
    → Architecture feature, không phải "bệnh"
    → Therapy USES this: observe transference → infer early models

  🟢 Transference: established (Freud 1912)
  🟡 Transference as chunk transfer = framework reframe
```

---

## §11 — 8 Failure Modes → 3 Categories

```
⭐ 8 CÁCH Self-Pattern-Modeling CHẠY NHƯNG RESONANCE KHÔNG EMERGE:

  CATEGORY A — PREDICTION ERROR (Self-Pattern-Modeling chạy nhưng sai):
    FM1: OVER-PREDICTION — compiled model KHÔNG update
         "Mẹ tưởng hiểu con nhưng con đã thay đổi"
         FIX: re-open calibration loop (ask, listen, update)
    FM2: MODEL INTERFERENCE — chunks model A fire cho target B
         FIX: awareness + deliberate Fresh override
    FM5: Background-Pattern SYSTEMATIC BIAS — triple bias → self-fulfilling
         FIX: external feedback BREAK loop

  CATEGORY B — OUTPUT MALFUNCTION (Self-Pattern-Modeling output bị lỗi):
    FM3: COMPILED SUPPRESS GAP RIÊNG — observation "over-clone" (§6.2)
         Gap KHÔNG bị clone, chỉ bị suppress (Compiled-Suppress)
         FIX: maintain own domains/interests
    FM6: ALEXITHYMIA BOTTLENECK — Step 5 fail
         🟢 Bird & Cook 2013 (DECISIVE): self-chunks thiếu → both fail
         FIX: build self-chunks FIRST (Focusing, labeling therapy)
    FM7: Compiled OVERWHELM — cảm xúc quá → PFC offline
         🟢 Arnsten 2009: NE surge → PFC disconnect
         FIX: self-regulation training

  CATEGORY C — INTENTIONAL BLOCK (Self-Pattern-Modeling bị chặn cố ý):
    FM4: STRATEGIC MODE — Tool giả Agent (sale smile)
         FIX: honest about own processing mode
    FM8: SCHEMA DEHUMANIZE — Compiled suppress → target = object
         🟢 Bandura 1999: Moral Disengagement
         🟢 Grossman 1995: harder to kill face-to-face
         FIX: restore target as agent (exposure, narrative)
```

---

## §12 — Shared Substrate: Self-Pattern-Modeling on Simulation-Engine

### §12.1 — Neural evidence

```
⭐⭐ 3 APPLICATIONS DÙNG CÙNG SUBSTRATE:

  🟢 Lombardo 2010 (J. Cognitive Neuroscience):
    fMRI: mentalizing self vs other → IDENTICAL connectivity
    → CÙNG circuit, khác chỉ ở TARGET input

  🟢 Mitchell 2006 (Neuron) — DOUBLE DISSOCIATION:
    SIMILAR other → ventral mPFC (= SELF circuits) → cost THẤP
    DISSIMILAR other → dorsal mPFC (DIFFERENT circuits) → cost CAO
    → = Compiled/Fresh spectrum CONFIRMED AT NEURAL LEVEL
    → = Entity-Access gradient = mPFC gradient (Entity-Access.md §3)

  🟢 Bird, Silani et al. 2010 (Brain):
    Anterior insula = SHARED READOUT cho self AND other
    HIGH alexithymia → REDUCED for BOTH → proof shared device

  🟢 Buckner & Carroll 2007, Schacter & Addis 2007:
    DMN = ENGINE cho ALL mental simulation
```

### §12.2 — Alexithymia = decisive proof

```
⭐ ALEXITHYMIA = HỎNG 1 = HỎNG CẢ 3:

  🟢 Bird & Cook 2013 (Translational Psychiatry):
    Empathy deficits = ALEXITHYMIA, NOT autism per se.

  Alexithymia → broken anterior insula readout
    → Self-Observation: FAIL (cannot read own body-state)
    → Self-Pattern-Modeling Compiled: FAIL (cannot read simulated body-state)
    → Imagine-Final: DEGRADED (cannot pre-feel future accurately)
    → = PROOF: 3 applications share 1 readout device

  INTERVENTION: train self-awareness → Self-Pattern-Modeling improves AS SIDE EFFECT
    → 🟢 Focusing (Gendlin 1978): felt sense access
    → 🟢 Mindfulness: observe emotions without judgment
    → 1 training → 3 improvements (shared substrate)
```

### §12.3 — Diversity effect + Reflection vs Rumination

```
⭐ GIAO TIẾP ĐA DẠNG → SELF-MODEL CHÍNH XÁC HƠN:

  Similar → vMPFC (confirm biases) — "mọi người giống tôi"
  Dissimilar → dMPFC (reveal biases) — "ồ, họ nghĩ KHÁC"
  → Diversity → bias revealed → sharper self-other boundary
  🟢 Mitchell 2006: vMPFC/dMPFC double dissociation
  🟡 Diversity → self-calibration = logically sound, limited direct evidence

⭐ REFLECTION vs RUMINATION (Simulation-Engine §9):

  🟢 Trapnell & Campbell 1999:
    SELF-REFLECTION: driven by CURIOSITY → openness, empathy, BETTER self-knowledge
    SELF-RUMINATION: driven by THREAT → neuroticism, anxiety, WORSE self-knowledge

  → Cùng mechanism (self-observation), khác cortisol direction → khác outcome
  → Reflection = productive. Rumination = destructive.
  → Cách quan sát QUYẾT ĐỊNH quality, không phải lượng quan sát.

⭐ BIDIRECTIONAL LOOP: SOCIAL ↔ SELF-REGULATION:

  🟢 Lopes et al. 2003: better regulation → better social → better regulation
  🟢 Coan & Sbarra 2015: brain OUTSOURCE regulation to trusted others
  → Social contact = EXTERNAL regulation resource
  → Isolation → substrate atrophy → negative spiral
  → "Cô đơn → kém xã hội → cô đơn hơn" = spiral on shared substrate
```

---

## §13 — PFC-Operations + Entity-Access Integration

### §13.1 — PFC-Operations × Self-Pattern-Modeling

```
⭐ PFC-Operations.md: 2 operations trên Compiled/Fresh spectrum:

  HOLD = amplify pattern mới (PFC hold Self-Pattern-Modeling model in working memory)
    → Self-Pattern-Modeling on stranger = PFC HOLD multiple drafts (Fresh)
    → Cost: PFC Budget (shared, finite)
    → Mệt ở work → Self-Pattern-Modeling cho con YẾU → "không phải không yêu con"

  SUPPRESS = block pattern cũ
    → Self-Pattern-Modeling suppress compiled response (Mode B = suppress Compiled)
    → Cost: suppress CANNOT compile "not" → unsustainable
    → Bác sĩ suppress Compiled empathy → cost tích lũy → burnout

  COMPILED QUALITY DIMENSION (PFC-Operations §5):
    Genuine-compiled: body confirmed → Self-Pattern-Modeling accurate, reward = opioid
    Schema-compiled: PFC-driven → Self-Pattern-Modeling biased by schema, reward = relief
    Threat-compiled: bị ép → Self-Pattern-Modeling distorted by fear, reward = cortisol drop
    → Cùng "compiled Self-Pattern-Modeling" nhưng KHÁC quality → KHÁC Self-Pattern-Modeling output lifetime
```

### §13.2 — Entity-Access × Self-Pattern-Modeling

```
⭐ Entity-Access.md: mPFC gradient = Entity-Access spectrum:

  🟢 Mitchell 2006: ventral mPFC = self + close other (Mức 4-5)
  🟢 Mitchell 2006: dorsal mPFC = distant/dissimilar (Mức 1-2)

  Entity-Access Mức 5 (body-base extension):
    → Self-Pattern-Modeling on deep Entity: Compiled SÂU, cost ≈ 0
    → "Hiểu không cần nói" = composite compiled
    → Valence-Structural reward SUSTAINED

  Entity-Access Mức 1 (schema-only):
    → Self-Pattern-Modeling on stranger: Fresh dominant, cost > 0
    → Schema fallback, prediction coarse

  → Entity-Access level = DETERMINES Self-Pattern-Modeling processing mode
  → Access TĂNG = Self-Pattern-Modeling shift từ Fresh → Compiled (cost giảm, accuracy tăng)
  → Entity-Access gradient = mPFC gradient = Compiled/Fresh gradient cho Self-Pattern-Modeling
```

### §13.3 — Entity-Compiled × Self-Pattern-Modeling

```
  Entity-Compiled.md: Self-Pattern-Modeling → Entity-Compiled lifecycle:
    Self-Pattern-Modeling fire repeated → Hebbian → Entity-Compiled forms
    Entity-Compiled = agent → body-base extension
    → Hub-and-Spoke model (5 S1 agents maximum)
    → 🟢 Dunbar 1992, 2024: Social Brain Hypothesis

  GRIEF = Entity-Compiled disruption:
    Entity MẤT → compiled model STILL EXISTS → Self-Pattern-Modeling still fires
    → Compiled fire on ABSENT entity → body respond → pain THẬT
    → = Tại sao grief CÓ cost thật (not "just sad")
```

---

## §14 — Developmental Trajectory

```
⭐ Self-Pattern-Modeling LIFECYCLE = TRADEOFF DEPTH vs FLEXIBILITY:

  ┌────────────┬──────────────────────┬───────────────────────────┐
  │ Giai đoạn  │ Self-Pattern-Modeling state            │ Resonance capability      │
  ├────────────┼──────────────────────┼───────────────────────────┤
  │ 0-6 tháng  │ NO Self-Pattern-Modeling (contagion)   │ Hardware ONLY (oxytocin)  │
  │ 6-24 tháng │ BOOTSTRAPPING        │ Mother contingent critical│
  │            │ 🟢 Svetlova 2010     │ 🟢 Romanian orphanage     │
  │ 2-7 tuổi  │ OVER-APPLY (animism) │ "Bạn với mọi thứ"        │
  │ 7-12      │ CALIBRATING          │ "Nhóm bạn" emerges       │
  │ 12-18     │ EXPANDING            │ Intense, clone ceiling LOW│
  │ 18-30     │ MATURING             │ Quality > quantity        │
  │ 30-60     │ COMPILED DEEP        │ "Biết" không cần nói     │
  │ 60+       │ VERY COMPILED        │ Maximum depth, minimal new│
  └────────────┴──────────────────────┴───────────────────────────┘

  MOTHER BOOTSTRAP (6-24 tháng) — LOAD-BEARING:
    Infant state → Mẹ observe → label → respond CONTINGENTLY
    → Self-chunk forms: "state NÀY = word NÀY = response NÀY"
    → Contingency quan trọng hơn presence
    → 🟢 Amsterdam 1972: rouge test 18-24m (self-recognition)

  Young: flexible (many models, shallow) → resonance WIDE nhưng SHALLOW
  Old: deep (few models, very compiled) → resonance NARROW nhưng DEEP
  → Match Dunbar data: turnover CAO ở 17-21, STABLE later
```

---

## §15 — Reversed Mapping + Professional Self-Pattern-Modeling + Moral Injury

### §15.1 — Schadenfreude: Compiled REVERSED khi valence negative

```
  Khi Per-Agent Valence ÂM → Compiled output BỊ ĐẢO:
    Bình thường: "bạn buồn → tôi buồn" = empathy
    Reversed: "kẻ thù đau → tôi SƯỚNG" = Schadenfreude

  TẠI SAO REWARD: ① L0 safety TĂNG ② justice satisfied ③ relative status TĂNG
  Compiled VẪN FIRE — cùng compiled simulation, valence đảo hướng interpretation
  🟢 Takahashi 2009: ventral striatum khi misfortune befalls envied person
  🟢 Cikara 2014: counter-empathy in competitive contexts
```

### §15.2 — Sadism vs Dehumanization

```
  DEHUMANIZATION: Compiled SUPPRESS → target = object → no simulation → giết COLD
  SADISM: Compiled FIRE STRONG + REVERSED → active creation of suffering
    → REQUIRES empathy mechanism HOẠT ĐỘNG (để simulate)
    → REQUIRES target remain AGENT (nếu dehumanize → mất reward)
  → 2 paths KHÁC NHAU từ cùng extreme negative valence
  🟢 Bandura 1999: Moral Disengagement
```

### §15.3 — Professional Self-Pattern-Modeling conflicts

```
  BÁC SĨ: Fresh FULL (surgery) + Compiled cost tích lũy → burnout
  THERAPIST: Compiled HIGH (empathize) + overload → compassion fatigue
    🟢 Figley 2002: compassion fatigue
  SOLDIER: Fresh strategic + Compiled suppress → post-combat Compiled REBOUNDS → PTSD
    🟢 Milgram 1963: extreme distress
```

### §15.4 — Moral injury = 3-cost model

```
⭐ MORAL INJURY: Compiled BỊ BUỘC FIRE TRÊN ACTIONS MÂU THUẪN VỚI VALUES:

  3-COST ALL FIRING SIMULTANEOUSLY:
    ① PFC Draft: process complex moral reasoning
    ② Suppress: suppress Compiled empathy response (chronic)
    ③ Uncertainty: "tôi đang đúng hay sai?" (unresolvable)
  → Total cost CỰC CAO. Duration chronic → UNSUSTAINABLE.

  2-LUỒNG GIẢI THÍCH KHÁC OUTCOME:
    Bác sĩ + bệnh nhân lạ: Valence-Momentary negative + Valence-Structural ≈ 0 → burnout
    Mẹ chăm con ốm (CÙNG Compiled): Valence-Momentary negative + Valence-Structural STRONG → KHÔNG burnout
    → Biến số = Luồng 2 bù Luồng 1 hay không

  KHÁC PTSD: PTSD = threat TO self. Moral injury = threat FROM self.
  🟢 Litz 2009: moral injury — distinct from PTSD

  ⭐ SELF-MODEL GUILT = LỚP ③ TRONG 3-LAYER GUILT MODEL (v3.2):
    Self-Pattern-Modeling detect mismatch: "tôi muốn tốt" vs "tôi vừa làm xấu."
    → Prediction-delta NEGATIVE → dissonance → guilt lớp ③.
    Resolution = behavioral change + time + body verify = CHẬM NHẤT trong 3 lớp.
    Detail: Collective-Body.md v2.2 §5.4 (Compilation Source Match, 3-layer model).
    Trust mechanism: Trust.md v1.0.
```

### §15.5 — Strategic Self-Pattern-Modeling: suppress + fake cues + meta-Self-Pattern-Modeling

```
  3 CHIẾN LƯỢC GIA:
    ① POKER FACE: suppress cues → starve đối thủ's Compiled input
    ② FAKE CUES: feed wrong cues → đối thủ Compiled fire on giả
       🟢 DePaulo et al. 2003: deception detection ≈ 54% (near chance)
       VD: "Thành không kế" — Gia Cát Lượng hack Tư Mã Ý's Self-Pattern-Modeling
    ③ META-Self-Pattern-Modeling: Self-Pattern-Modeling on opponent's Self-Pattern-Modeling process → control entire chain
       Level 1: đọc đối thủ. Level 2: đối thủ đang đọc tôi.
       Level 3: predict đối thủ's Self-Pattern-Modeling. Level 4: control cues.

  TẤT CẢ dùng CÙNG mechanism — chỉ HƯỚNG khác
  "Biết địch biết ta, trăm trận trăm thắng" = compiled meta-Self-Pattern-Modeling
  🟢 Ekman 2003: micro-expressions leak even when suppressed
```

---

## §16 — Training + AI Era

### §16.1 — Training methods

```
⭐ Self-Pattern-Modeling QUALITY LÀ TRAINABLE:

  FOUNDATION — Self-chunk training (upstream, Bird & Cook):
    → 🟢 Focusing (Gendlin 1978), Mindfulness, emotional labeling
    → Body-based: yoga, tai chi, somatic experiencing

  Compiled-SPECIFIC: deep listening, compassion meditation, fiction, cross-cultural
  Fresh-SPECIFIC: perspective-taking, strategic games, journaling
  CONTEXT-SELECTION: diverse social engagement, role-play, travel
  MODE-SWITCHING: therapist (Mode A), negotiator (Mode B), leader (Mode C)

  Compilation as training goal: Fresh chains → compile → Compiled (§3.6)
  "Natural talent" = partially Resonance Baseline (hardware overlap)
  "Learned skill" = compiled through practice. Both produce SAME quality.
```

### §16.2 — AI era implications

```
  RISK 1 — Screen replaces feedback-rich interaction → thin Self-Pattern-Modeling library
  RISK 2 — Parasocial at scale (celebrities, AI companions, no calibration)
  RISK 3 — AI-triggered Self-Pattern-Modeling without agent reality
    → Self-Pattern-Modeling fires on CUES, not beliefs (same as §15.5 fake cues)
    → Long-term: library distortion

  OPPORTUNITY — Training at scale: meditation apps, Self-Pattern-Modeling literacy, AI-assisted therapy
  → Individual Self-Pattern-Modeling literacy = critical skill for AI era
```

---

## §17 — Honest Assessment

```
═══ 🟢 ESTABLISHED ═══

  Bird & Cook 2013: alexithymia → empathy deficit (decisive)
  Lombardo 2010: identical connectivity self/other (shared substrate)
  Mitchell 2006: vMPFC similar, dMPFC dissimilar (double dissociation)
  Bird & Silani 2010: anterior insula shared readout
  Fukushima 2011: interoceptive accuracy → empathic accuracy
  Trapnell & Campbell 1999: reflection vs rumination
  Joireman et al. 2002: self-reflection → empathy
  Lopes et al. 2003: social ↔ regulation bidirectional
  Coan & Sbarra 2015: Social Baseline Theory
  Koudenburg et al. 2024: social → self-concept clarity
  Singer 2004, 2006: shared activation + fairness modulation
  Dimberg 2000: facial EMG mimicry 300ms
  Chartrand & Bargh 1999: automatic mimicry
  Feldman 2012: biobehavioral synchrony
  Kahneman 2011: System 1/2 dual process
  Klein 1998: expert intuition = compiled
  Takahashi 2009: Schadenfreude ventral striatum
  Cikara 2014: counter-empathy competitive contexts
  Arnsten 2009: PFC disconnect under NE surge
  Gazzaniga: split-brain interpreter module
  Haidt 2001: moral reasoning = post-hoc justification
  LeDoux 1996: fear conditioning one-trial learning
  Bandura 1999: Moral Disengagement
  Milgram 1963: obedience + distress
  Litz 2009: moral injury distinct from PTSD
  Figley 2002: compassion fatigue
  Kurzban 2013: cognitive effort = opportunity cost (processing load)
  Bouchard 1990: twin studies
  Jack 1991: self-silencing → depression
  Righetti 2017: avoidance sacrifice → negative both partners
  Baumeister 1999: passion = rate of change
  Aron & Aron 1996, 2000: self-expansion model
  Muise & Goss 2024: closeness × otherness
  Tsapelas et al. 2009: boredom predicts decline
  Gottman: emotional disengagement pathway
  Dunbar 1992, 2024: Social Brain Hypothesis
  Bowlby 1969: Internal Working Models
  Monsell 2003: task-switching cost
  Nickerson 1998: confirmation bias
  Krueger 2007: projection bias
  Merton 1948, Rosenthal 1968: self-fulfilling prophecy
  DePaulo et al. 2003: deception detection ≈ 54%
  Ekman 2003: micro-expressions
  Buckner & Carroll 2007, Schacter & Addis 2007: DMN simulation

═══ 🟡 FRAMEWORK SYNTHESIS ═══

  RENAME: Self-Pattern-Match → Self-Pattern-Modeling
  APPLICATION-1 on Simulation-Engine (3 apps, 1 hardware)
  1 mechanism × 3 dimensions restructure (not 4 skills)
  Compiled/Fresh as real axis (not Feeling/Logic)
  Expert intuition = compiled, shareable vs non-shareable
  PFC=Lawyer caveat on all Self-Pattern-Modeling output
  Per-domain Self-Pattern-Modeling ratio (not per-person fixed)
  4 simultaneous conditions for resonance
  Over-clone reframed: observation label, mechanism = compiled suppress
  Gap-clone impossible (5-step proof)
  Self-Pattern-Modeling cost = only 2 (Fresh processing + space)
  True understanding = anti-compiled-suppress
  Resonance Decline 2 Forces + 1 Fuel (Bond-Architecture v2.0)
  Background-Pattern → Self-Pattern-Modeling triple bias mechanism
  Transfer learning as chunk sharing + Freud reframe
  8 failure modes → 3 categories
  Clone spectrum as Dimension 3
  Diversity → self-calibration via dMPFC contrast
  Bidirectional social-self loop
  3-cost applied to moral injury / professional Self-Pattern-Modeling
  Entity-Access gradient = Self-Pattern-Modeling processing mode

═══ 🔴 HYPOTHESIS ═══

  Precise Compiled/Fresh neural dissociability
  Valence gate precise circuitry
  Training ceiling predictions
  AI library distortion long-term effects
  PFC=Lawyer distortion magnitude measurement
  3-cost independent measurement protocol
  Per-domain Compiled/Fresh ratio measurement
  Diversity threshold for significant calibration
  Interoception training duration → measurable Self-Pattern-Modeling improvement
```

---

## §18 — Cross-References

```
  ENGINE:
    → Simulation-Engine.md v1.0 — SHARED ENGINE: 3 components × 3 axes
    → PFC-Operations.md v1.0 — Hold/Suppress, Compiled Quality, PFC Budget

  PARENT + SIBLING:
    → Agent-Mechanism.md v2.1 — integration hub, §5 Self-Pattern-Modeling preview
    → By-Product-Gap-Resonance.md v1.0 — emergent mutual phenomenon (2-Stream)

  MECHANISM FILES:
    → Entity-Compiled.md v1.0 — lifecycle, Hub-and-Spoke, Dunbar, grief
    → Entity-Access.md v1.0 — mPFC gradient, 3-Factor Model, spectrum
    → Inter-Body-Mechanism.md v1.0 — Compiled/Fresh axis, 3-cost, Compilable Architecture
    → Chunk.md v2.0 — chunk substrate, compilation
    → Feeling.md v3.0 — PFC observation interface (Step 5 = Feeling applied)
    → Logic-Feeling.md v4.0 — Body-Knowing + observer labels, Compiled/Fresh, modality bias
    → Valence-Propagation.md v2.0 — per-entity valence, chain propagation
    → Body-Coupling.md v2.0 — coupling mechanism (builds ON Self-Pattern-Modeling)
    → Body-Feedback-Mechanism.md v2.0 — 2-source model, chunk dynamics
    → Background-Pattern.md v1.1 — 2D Depth×Density, §8 self-reinforcing
    → Cortisol-Baseline.md v2.1 — stress cascade, moral injury pathway
    → Autonomy-Hardware.md v1.1 — vmPFC/DRN, efference copy

  OBSERVATION FILES:
    → Connection.md v4.0 — 3 generative primitives, 2-luồng reward (Valence-Momentary/Valence-Structural)
    → Empathy.md v3.0 — Self-Pattern-Modeling function applied to other agents
    → Status.md v2.0 — Resource Access Map, status scan
    → Protect.md v1.0 — ownership, loss aversion
    → Threat.md — NE cascade, PFC disconnect

  APPLICATION:
    → Imagine-Final.md v2.0 — APPLICATION-2 on Simulation-Engine
    → Self-Observation.md v1.0 — APPLICATION-3: mutual reinforcement (Self-Pattern-Modeling §4 Step 5 = Self-Observation capability)
    → AI-Schema-Detection.md v2.0 — AI interaction × Self-Pattern-Modeling
    → Somatic-Articulation-Loop.md — body → words

  COLLECTIVE:
    → Resonance-Entity.md v2.0 — Hardware-Subsidy, Hardwired:Compilable Architecture
    → Resonance-Sustainability.md v1.0 — 3 Modalities, Silence, Capitalization
    → Entity-Valence-Dynamics.md v2.0 — Phantom resonance

  HEALTH:
    → ADHD-Observation.md §10 — late diagnosis Self-Pattern-Modeling re-compile
    → Autism-Observation.md §10 — double empathy problem
    → PTSD-Analysis.md §11 — C-PTSD = Self-Pattern-Modeling compiled under chronic threat
    → OCD-Analysis.md §4.7 — Autism × OCD overlap 17.4%

  DRILL SOURCES:
    → Drill-Self-Pattern-Modeling-Mechanism-Analysis v2.2 (17 insights)
    → Drill-Over-Self-Pattern-Modeling-Clarification v1.0 (12 insights) — backup/ (REFERENCE)
    → Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 (13 insights)
```

---

## §19 — Research Citations

```
  R1.  Amsterdam 1972: rouge test, self-recognition 18-24m
  R2.  Aron & Aron 1996, 2000: self-expansion model, novel activities
  R3.  Arnsten 2009: PFC disconnect under NE surge (α1 NE)
  R4.  Bandura 1999: Moral Disengagement, dehumanization
  R5.  Bao & Lyubomirsky 2013: hedonic adaptation prevention, relationships
  R6.  Baumeister & Bratslavsky 1999: passion = rate of change in intimacy
  R7.  Bird & Cook 2013: alexithymia drives empathy deficit (DECISIVE)
  R8.  Bird, Silani et al. 2010: anterior insula shared readout
  R9.  Bouchard 1990: twin studies, nature/nurture
  R10. Bowlby 1969: Internal Working Models, attachment
  R11. Buckner & Carroll 2007: self-projection and the brain (DMN)
  R12. Buckner, Andrews-Hanna & Schacter 2008: DMN = Simulation-Engine
  R13. Chartrand & Bargh 1999: chameleon effect, automatic mimicry
  R14. Cikara 2014: counter-empathy in competitive contexts
  R15. Coan & Sbarra 2015: Social Baseline Theory
  R16. DePaulo et al. 2003: deception detection ≈ 54%
  R17. Dimberg 2000: facial EMG mimicry, 300ms pre-conscious
  R18. Dunbar 1992, 2024: Social Brain Hypothesis, 30+ years
  R19. Ekman 2003: micro-expressions leak when suppressed
  R20. Feldman 2012: biobehavioral synchrony (converge level)
  R21. Figley 2002: compassion fatigue in helping professionals
  R22. Fukushima, Terasawa et al. 2011: interoceptive → empathic accuracy
  R23. Kurzban, Duckworth & Kable 2013: cognitive effort = opportunity cost (processing load)
  R24. Gallese 2003, 2005: embodied simulation
  R25. Gazzaniga: split-brain interpreter module
  R26. Gendlin 1978: Focusing, felt sense access
  R27. Gottman: emotional disengagement → divorce ~16yr
  R28. Grossman 1995: harder to kill face-to-face
  R29. Haidt 2001: moral reasoning = post-hoc justification
  R30. Jack 1991: self-silencing → loss authentic self → depression
  R31. Joireman, Parrott & Hammersla 2002: reflection → empathy
  R32. Kahneman 2011: Dual Process Theory, System 1/2
  R33. Klein 1998: expert intuition, recognition-primed decision
  R34. Koudenburg et al. 2024: social interaction → self-concept clarity
  R35. Krueger 2007: projection bias in social perception
  R36. LeDoux 1996: fear conditioning, one-trial learning
  R37. Litz 2009: moral injury — distinct from PTSD
  R38. Lombardo et al. 2010: identical connectivity self/other (fMRI)
  R39. Lopes, Salovey & Straus 2003: emotion regulation ↔ social
  R40. Merton 1948, Rosenthal 1968: self-fulfilling prophecy
  R41. Milgram 1963: obedience + distress
  R42. Mitchell, Macrae & Banaji 2006: vMPFC/dMPFC dissociation (Neuron)
  R43. Monsell 2003: task-switching cost
  R44. Mul et al. 2021: alexithymia network analysis
  R45. Muise & Goss 2024: closeness × otherness interaction
  R46. Nickerson 1998: confirmation bias
  R47. Righetti 2017: avoidance sacrifice → negative both partners
  R48. Rodriguez-Gonzalez 2023: low differentiation → lower quality
  R49. Schacter, Addis & Buckner 2007: Constructive Episodic Simulation
  R50. Singer 2004: shared activation areas empathy
  R51. Singer 2006: empathy modulated by perceived fairness
  R52. Svetlova 2010: empathic helping 14-24m
  R53. Takahashi 2009: Schadenfreude, ventral striatum
  R54. Tamir & Mitchell 2010: vMPFC = close-other processing
  R55. Terasawa et al. 2021: interoception ↔ empathy bidirectional
  R56. Trapnell & Campbell 1999: self-reflection vs self-rumination
  R57. Tsapelas, Aron & Orbuch 2009: boredom predicts decline 9yr later
```

---

> *Bạn thấy bạn thân khóc → body bạn buồn nhẹ. Đó là Compiled — COMPILED simulation.*
> *Bạn nghĩ: "bạn cần an ủi." Đó là Fresh — FRESH PFC draft.*
>
> *Bạn thấy kẻ thù gục ngã → body bạn... nhẹ nhõm. Vẫn Compiled — nhưng REVERSED.*
> *Bạn nghĩ: "giờ mình an toàn hơn." Vẫn Fresh — nhưng strategic.*
>
> *Cùng 1 mechanism. Cùng 6 steps. Cùng chunk library.*
> *Nhưng Per-Agent Valence đảo hướng mọi thứ.*
>
> *Self-Pattern-Modeling = APPLICATION-1 trên Simulation-Engine.*
> *Self-Observation, Imagine-Final = 2 apps khác, CÙNG substrate.*
> *Luyện 1 = luyện cả 3. Hỏng 1 = hỏng cả 3.*
> *Modeling — không phải matching. Forward simulation — không phải tìm-khớp.*
