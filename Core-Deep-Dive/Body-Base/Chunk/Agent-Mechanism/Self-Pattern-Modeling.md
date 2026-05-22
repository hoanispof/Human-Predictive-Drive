---
title: Self-Pattern-Modeling — Solo Forward Simulation Mechanism
version: 3.1
created: 2026-04-15
rewritten: 2026-05-22 (v3.1 — RENAME Match→Modeling, Simulation Engine APPLICATION, 3 dimensions, 42 drill insights integrated)
previous_versions:
  - v3.0 (2026-05-17, 2569L) → backup/Self-Pattern-Match-v3.0-backup.md
  - v2.4 (2292L) → backup/Self-Pattern-Match-v2.4-backup.md
  - v1.0 (1518L) → backup/Self-Pattern-Match-v1.0-forward-backup.md
  - v0 (inward-labeling) → Body-Base/Feeling/backup/Self-Pattern-Match.md
status: v3.1 — CORE MECHANISM FILE
scope: |
  APPLICATION 1 trên Simulation Engine: SPM = (Other, Present, Simulate).
  v3.1 KEY CHANGES:
    ① RENAME: Self-Pattern-Match → Self-Pattern-Modeling (SPM giữ nguyên)
    ② SPM = APPLICATION trên Simulation Engine (shared substrate)
    ③ 1 mechanism × 3 dimensions (not 4 skills)
    ④ Over-clone = observation label, mechanism = compiled suppress gap riêng
    ⑤ 4 conditions ĐỒNG THỜI cho resonance
    ⑥ Abstract entities taxonomy
    ⑦ BP triple bias (retrieval + template + interpretation)
    ⑧ Transfer learning + interference + Freud reframe
    ⑨ 8 failure modes → 3 categories
    ⑩ PFC-Operations + Entity-Access + Entity-Compiled integration
  Giữ nguyên core từ v3.0: F1/F2 Compiled/Fresh, 6 steps, valence gate,
  expert intuition, PFC=Lawyer, 3-cost, per-domain SPM, 30+ citations.
purpose: |
  File NỀN TẢNG cho toàn bộ framework:
  ① SPM là CƠ CHẾ CHÍNH mà não dùng để interact với agents
  ② APPLICATION 1 trên Simulation Engine (Other × Present × Simulate)
  ③ 2 Functions (F1+F2) = Compiled/Fresh spectrum applied to agent prediction
  ④ Context-dependent selection giải thích TẠI SAO cùng 1 người
     ứng xử KHÁC NHAU với mẹ, bạn, kẻ thù
  ⑤ Per-Agent Valence quyết định F1/F2 fire HƯỚNG NÀO
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
  - Body-Coupling.md v2.0 — coupling mechanism (builds ON SPM)
  - Body-Feedback-Mechanism.md v2.0 — 2-source model, chunk dynamics
  - Inter-Body-Mechanism.md v1.0 — Compiled/Fresh axis, 3-cost, Architecture B
  - Empathy.md v3.0 — SPM function applied to other agents
  - Connection.md v4.0 — 3 generative primitives, 2-luồng reward
  - Cortisol-Baseline.md v2.1 — stress cascade, moral injury
  - Background-Pattern.md v1.1 — 2D Depth×Density, §8 self-reinforcing
  - Imagine-Final.md v2.0 — APPLICATION 2, shared engine
sources:
  - Self-Pattern-Match.md v3.0 (2,569L) — previous version
  - Drill-SPM-Mechanism-Analysis v2.2 (17 insights)
  - Drill-Over-SPM-Clarification v1.0 (12 insights)
  - Drill-SPM-Self-Shared-Substrate v1.0 (13 insights)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Self-Pattern-Modeling — Solo Forward Simulation Mechanism

> ⚠️ **QUY ƯỚC**: Tên đầy đủ = **Self-Pattern-Modeling**. Viết tắt = **SPM**.
> Đổi từ "Self-Pattern-Match" vì "Match" = passive so sánh, "Modeling" = active mô hình hóa.
> SPM thật sự = forward simulation (xây model + chạy + predict), không phải tìm-khớp.

> Bạn thấy bạn thân khóc. Body bạn buồn nhẹ — DÙ bạn không bị gì.
> Đó là F1 (Compiled): body SIMULATE trạng thái người khác — automatic, gần vô thức.
>
> Rồi bạn nghĩ: "bạn buồn vì chia tay → chắc muốn ai đó lắng nghe."
> Đó là F2 (Fresh): PFC CHAIN draft predict hành vi tiếp theo — deliberate, tốn effort.
>
> Cùng 1 mechanism. Cùng 1 chunk library. Nhưng 2 OUTPUTS khác nhau.
> "Feeling" và "Logic"? Chỉ là LABELS — Einstein "cảm" toán vì toán đã COMPILED.
> Therapist mới "nghĩ" cảm xúc vì case mới còn FRESH.
> Trục thật: COMPILED ←→ FRESH. Content không quyết định.
>
> Và TẤT CẢ phụ thuộc Per-Agent Valence — body đánh giá agent NÀY thế nào?
> Valence dương: F1 = empathy. Valence âm: F1 = REVERSED (sướng khi kẻ thù đau).
> Cùng mechanism, cùng 6 steps — khác output vì khác valence.

---

## Mục lục

- §0 — Position + Thesis: SPM trên Simulation Engine
- §1 — Definition: 1 Mechanism × 3 Dimensions
- §2 — SPM Scope: Agent Properties + Fire Gradient
- §3 — 2 Functions: F1 Compiled + F2 Fresh
- §4 — 6 Steps (reframed qua Compiled/Fresh)
- §5 — Context-Dependent Selection
- §6 — Clone Spectrum + Over-Clone Reframe
- §7 — SPM → Resonance: 4 Conditions Đồng Thời
- §8 — Abstract Entities Taxonomy
- §9 — Background Pattern × SPM: Triple Bias
- §10 — Multiple Models: Transfer + Interference
- §11 — 8 Failure Modes → 3 Categories
- §12 — Shared Substrate: SPM on Simulation Engine
- §13 — PFC-Operations + Entity-Access Integration
- §14 — Developmental Trajectory
- §15 — Reversed Mapping + Professional SPM + Moral Injury
- §16 — Training + AI Era
- §17 — Honest Assessment
- §18 — Cross-References
- §19 — Research Citations

---

## §0 — Position + Thesis: SPM trên Simulation Engine

### §0.1 — SPM = APPLICATION 1 trên Simulation Engine

```
⭐⭐ SPM TRÊN SIMULATION ENGINE:

  Simulation-Engine.md v1.0: Brain có 1 general-purpose engine:
    3 COMPONENTS: Interoception × Constructive Simulation × Self/Other Model
    3 AXES: Target × Time × Operation

  SPM = APPLICATION 1: tọa độ (Other, Present, Simulate)
    → Target = OTHER entity (bạn, mẹ, kẻ thù, stranger)
    → Time = PRESENT (current/near-future state)
    → Operation = SIMULATE (forward prediction)

  3 Applications trên CÙNG engine:
    ┌──────────────────┬──────────┬──────────┬──────────────────┐
    │ Application      │ Target   │ Time     │ Operation        │
    ├──────────────────┼──────────┼──────────┼──────────────────┤
    │ SPM (file này)   │ OTHER    │ Present  │ Simulate         │
    │ Imagine-Final    │ SELF     │ Future   │ Simulate+Construct│
    │ Self-Observation │ SELF     │ Present  │ Observe          │
    └──────────────────┴──────────┴──────────┴──────────────────┘

  SHARED SUBSTRATE: anterior insula + vMPFC + DMN + hippocampus
  → Luyện 1 application = luyện TẤT CẢ (shared substrate improvement)
  → Hỏng 1 component = hỏng TẤT CẢ (alexithymia = decisive proof)
  → 🟢 Lombardo 2010: IDENTICAL connectivity cho self vs other
  → 🟢 Buckner & Carroll 2007: all = "self-projection" in DMN

  CÁI RIÊNG CỦA SPM (so với 2 apps khác):
    → TARGET = OTHER (không phải self)
    → Accuracy limited by chunk OVERLAP với target
    → Per-Agent VALENCE quyết định direction (không có ở self-obs/Imagine-Final)
    → 6-step mechanism chi tiết (file này)
```

### §0.2 — Relationship với files khác

```
  KIẾN TRÚC:
    Simulation-Engine.md    = ENGINE (unification architecture)
    PFC-Operations.md       = HOW PFC operates (Hold/Suppress)
    ★ Self-Pattern-Modeling  = APPLICATION 1 (mechanism chi tiết)
    Imagine-Final.md v2.0   = APPLICATION 2 (future simulation)
    Feeling.md v3.0         = APPLICATION 3 (self-observation)

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

  1. SOLO + FORWARD: SPM chạy bên trong self, tạo prediction TRƯỚC verification
  2. APPLICATION 1: SPM = (Other, Present, Simulate) trên Simulation Engine [v3.1]
  3. 1 MECHANISM × 3 DIMENSIONS: Processing Level × Valence × Output Intensity [v3.1]
  4. COMPILED/FRESH = REAL AXIS: "Feeling/Logic" = observer labels
     Expert intuition = compiled, NOT bừa (shareable vs non-shareable)
  5. CONTEXT-DEPENDENT: chunks được retrieve VÔ THỨC tùy agent + context
  6. VALENCE-GATED: Per-Agent Valence quyết định F1/F2 fire hướng nào
  7. 4 CONDITIONS cho Resonance: positive valence + mutual Agent-mode
     + gap overlap + drive riêng maintained [v3.1]
  8. OVER-CLONE = OBSERVATION LABEL: mechanism thật = compiled suppress [v3.1]
  9. BIRD & COOK ARCHITECTURAL: self-awareness là prerequisite
  10. CALIBRATABLE: library refine qua feedback từ Resonance
```

### §0.4 — v3.0 → v3.1: What changed

```
  v3.0 ĐÚNG Ở: F1/F2 Compiled/Fresh, 6 steps, valence gate, context-dependent,
  expert intuition, PFC=Lawyer, 3-cost, per-domain SPM, reversed mapping.
  TẤT CẢ GIỮ NGUYÊN.

  v3.1 THÊM + RESTRUCTURE:
    ① RENAME: Match → Modeling (SPM giữ, chỉ đổi M = Modeling)
    ② Simulation Engine APPLICATION (shared substrate, 3 apps on 1 engine)
    ③ 1 mechanism × 3 dimensions restructure (not "4 skills")
    ④ SPM scope + boundary (4 agent properties, fire gradient, cái gì KHÔNG)
    ⑤ Clone spectrum (predict→mimic→adopt→converge) + gap-clone impossible
    ⑥ Over-clone reframe + 4 mechanisms resonance decline
    ⑦ 4 simultaneous conditions for resonance
    ⑧ Abstract entities (God, fiction, AI, nation, brand)
    ⑨ BP triple bias (retrieval + template + interpretation)
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
SELF-PATTERN-MODELING (SPM) = solo forward simulation mechanism.

⭐ Nói đơn giản: não dùng patterns CỦA MÌNH để MODEL entity KHÁC.
  Predict state. Predict behavior. Forward simulation.

⭐ Kỹ thuật: não retrieve chunks từ self repertoire, apply làm template
  cho target entity, simulate trạng thái target, đọc output,
  và attribute cho target như prediction.

SPM fire trên GRADIENT agent-properties: càng agent-like → SPM càng rich
(F1+F2 full). Ít agent-like → SPM degrade → fallback (schema → logic → physics).

⭐ RENAME (v3.1):
  "Self-Pattern-Match" → "Self-Pattern-Modeling"
  Lý do: "Match" = passive (so sánh/khớp). SPM thật sự = ACTIVE:
  xây model + chạy simulation + predict + calibrate.
  "Modeling" chính xác hơn. Abbreviation SPM GIỮA NGUYÊN.
```

### §1.2 — 1 Mechanism × 3 Dimensions (restructured from "4 skills")

```
⭐⭐ SPM = 1 MECHANISM × 3 DIMENSIONS:

  Drill v0.5 liệt kê "4 skills" (Predict/Mimic/Calibrate/Compile).
  Drill v2.2 chứng minh: đây KHÔNG PHẢI 4 skills riêng biệt.
  → Predict = CORE FUNCTION (bản chất SPM, không phải "1 skill")
  → Mimic/Clone = F1 OUTPUT SPECTRUM (intensity gradient, §6)
  → Calibrate = FEEDBACK PROCESS (tự động, §4 Step 6)
  → Compile = GENERAL brain property (Hebbian, mọi neural activity đều compile)

  CẤU TRÚC THẬT:

  ┌────────────────────────────────────────────────────────────────┐
  │ DIMENSION 1 — PROCESSING LEVEL (Compiled ←→ Fresh)            │
  │   = Inter-Body-Mechanism §3 trục thật                         │
  │   F1 (Compiled): body-level simulation, automatic, cost ≈ 0   │
  │   F2 (Fresh): PFC draft prediction, deliberate, cost > 0      │
  │   Ratio F1/F2 = per-domain, per-target, per-moment            │
  │   Transition: Fresh → Compiled (learning), Compiled → Fresh   │
  │   (disruption)                                                │
  ├────────────────────────────────────────────────────────────────┤
  │ DIMENSION 2 — VALENCE DIRECTION (Positive ←→ Negative)        │
  │   = SPM §3.5 valence gate (chi tiết)                          │
  │   Strong positive → empathy full → connection drive            │
  │   Neutral → surface scan → cautious observe                    │
  │   Strong negative → REVERSED → Schadenfreude / strategic       │
  │   Extreme negative → F1 SUPPRESS → dehumanization              │
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

Self-Pattern-Modeling là cơ chế mình dùng mình làm template để đoán người khác — APPLICATION 1 trên Simulation Engine (Other × Present × Simulate). Không phải mind-reading trực tiếp, không phải hardware mirror module — là simulation-based inference dùng self-chunks làm building blocks. SPM chạy 2 functions song song: F1 compiled body-level simulation (near-automatic, cost ≈ 0), F2 fresh PFC draft prediction (deliberate, costly). Observer gọi F1 là "cảm" và F2 là "nghĩ" — nhưng trục thật là COMPILED ←→ FRESH, không phải content. Per-Agent Valence quyết định F1 fire HƯỚNG NÀO (empathy hay reversed) và F2 chain MỤC ĐÍCH NÀO (giúp hay đối phó). Context quyết định chunks NÀO được retrieve (vô thức tùy chọn). SPM là 1 mechanism trên 3 dimensions (Processing Level × Valence Direction × Output Intensity), không phải 4 skills riêng lẻ.

---

## §2 — SPM Scope: Agent Properties + Fire Gradient

### §2.1 — 4 Agent Properties quyết định SPM fire intensity

```
⭐ SPM FIRE KHI TARGET CÓ "AGENT PROPERTIES":

  ① INTENTIONALITY: target có mục đích/goal riêng?
     → Người: yes (complex). Chó: yes (simple). Đá: no.

  ② STATE-DEPENDENT BEHAVIOR: hành vi phụ thuộc trạng thái nội?
     → Bạn buồn → cư xử KHÁC khi vui → SPM cần simulate state.

  ③ RECIPROCAL CAPACITY: target CÓ THỂ respond based on self's actions?
     → Người: adjust behavior theo mình → cần recursive predict.

  ④ SIMILARITY: template match CÓ KHẢ THI?
     → Mammalian: shared neurotransmitter → F1 CÓ THỂ fire.
     → Côn trùng: quá khác → template match FAIL.

  → SPM intensity = f(how many properties × how strong each)
  → KHÔNG binary "có/không" — GRADIENT liên tục

🟡 4 agent properties as SPM fire determinants = framework synthesis.
🟢 Consistent: Theory of Mind research attributes intentionality as key trigger.
```

### §2.2 — SPM fire gradient

```
⭐ SPM FIRE THEO GRADIENT — TỪ MAXIMUM ĐẾN ZERO:

  MAXIMUM SPM (F1 full + F2 full):
    → Bạn thân lâu năm, mẹ-con: compiled SÂU + composite modality

  HIGH SPM (F1 moderate + F2 active):
    → Đồng nghiệp thân, người quen: domain overlap + regular interaction

  MODERATE SPM (F1 nhẹ + F2 dominant):
    → Người lạ, cross-cultural: thin chunks → schema fallback + F2 fresh

  LOW SPM (F1 minimal + F2 coarse):
    → Chó, mèo: mammalian overlap MỘT PHẦN
    → 🟢 Proto-resonance khả thi (By-Product-Gap-Resonance §1.4)

  MINIMAL SPM (F1 ≈ 0 + F2 weak schema):
    → Côn trùng: minimal similarity → template match FAIL

  ZERO SPM:
    → Cục đá, cái bàn: NO agent properties → SPM KHÔNG fire
```

### §2.3 — Cái gì KHÔNG PHẢI SPM (dù dùng cùng hardware)

```
⭐ COMPILED/FRESH = GENERAL-PURPOSE HARDWARE.
   SPM = 1 APPLICATION CỤ THỂ CHO AGENTS.

  ┌─────────────────────┬─────────────────┬────────────────────────┐
  │ Application          │ Target          │ SPM?                   │
  ├─────────────────────┼─────────────────┼────────────────────────┤
  │ Predict NGƯỜI        │ Agent có states │ ✅ SPM full            │
  │ "Feel" toán          │ Math pattern    │ ❌ Domain-compiled     │
  │ "Feel" nhạc          │ Sound pattern   │ ❌ Sensory-compiled    │
  │ Predict TƯƠNG LAI    │ Future self     │ ❓ Imagine-Final (§12) │
  │ Predict VẬT LÝ      │ Object          │ ❌ Physics/logic       │
  │ Body observe NOW     │ Current self    │ ❌ Self-Observation    │
  └─────────────────────┴─────────────────┴────────────────────────┘

  6 CÁI KHÔNG PHẢI SPM:
    ❌ ① AROUSAL CONTAGION: bé nghe khóc → khóc lây (pre-SPM)
    ❌ ② SCHEMA-BASED PREDICTION: "con gái thì dịu dàng" (compiled RULE)
    ❌ ③ DOMAIN EXPERTISE: Einstein "feel" toán (compiled math, not agent)
    ❌ ④ PHYSICS PREDICTION: "bóng rơi xuống" (deterministic)
    ❌ ⑤ SELF-OBSERVATION: "tôi đang buồn" (current read, not forward)
    ❌ ⑥ PARASOCIAL ILLUSION: SPM CÓ fire (body simulate celebrity/AI)
         NHƯNG: no feedback → library distortion → FAILED SPM

🟡 SPM = agent-directed application of compiled/fresh hardware.
```

### §2.4 — SPM fire conditions (necessary + sufficient)

```
  SPM FIRE KHI VÀ CHỈ KHI 3 CONDITIONS:
    ① Target có AGENT PROPERTIES (≥1 trong 4 properties §2.1)
    ② Self có CHUNKS applicable cho target (library ≥ threshold)
    ③ Hướng = FORWARD (predict future state/behavior)

  Thiếu ① → domain processing hoặc physics
  Thiếu ② → schema fallback hoặc give up
  Thiếu ③ → self-observation / feeling (khác mechanism)
```

---

## §3 — 2 Functions: F1 Compiled + F2 Fresh

### §3.1 — Compiled/Fresh = Trục thật

```
⭐ TRỤC THẬT CỦA SPM: COMPILATION LEVEL — KHÔNG PHẢI CONTENT

  F1 = COMPILED processing (automatic, body-feedback direct, cost ≈ 0)
  F2 = FRESH PFC draft (deliberate, costly, not yet compiled)

  → "Feeling" và "Logic" = LABELS from OBSERVER perspective
  → Inside body: chỉ có COMPILED ←→ FRESH spectrum
  → Content (emotion/reasoning) KHÔNG quyết định F1/F2
  → COMPILATION LEVEL quyết định

  EVIDENCE (content ≠ processing level):
    ① Einstein + toán quen = COMPILED → automatic → "cảm thấy"
    ② Người lạ đoán cảm xúc stranger = FRESH → deliberate → "phải suy luận"
    ③ Chef nếm → biết ngay thiếu muối = COMPILED → "trực giác"
    ④ Therapist gặp case mới = FRESH → PFC draft → "phải phân tích"

  TRANSITION (both directions):
    FRESH → COMPILED (Learning): lặp + verify → Hebbian → automatic
    COMPILED → FRESH (Disruption): error/trauma/context change → phải FRESH lại

  🟡 F1/F2 = Compiled/Fresh reframe = framework synthesis.
  🟢 Consistent: Kahneman System 1/2, Klein 1998 expert intuition.
  Source: Inter-Body-Mechanism.md §3
```

### §3.2 — F1: Compiled body-level simulation

```
⭐ F1 = COMPILED SIMULATION:

  Body THẬT SỰ fire bản sao yếu trạng thái target.
  Biochemistry THẬT: opioid / cortisol / oxytocin / NE / VTA.

  ĐẶC TÍNH:
    ① NEAR-AUTOMATIC — PFC gần như không tham gia
    ② BODY-LEVEL — không phải "tưởng tượng" (Empathy.md §4.2)
    ③ KHÔNG THỂ TẮT 100% — chỉ dampen (trừ dehumanize → F1 suppress)
    ④ BIẾN THIÊN INTENSITY — zero → rất mạnh (gradient liên tục)
    ⑤ COST ≈ 0 PER FIRING (compiled) — nhưng biochemistry thật
       → Tích lũy nhiều episode = empathy fatigue

  ⭐ F1 = "LUỒNG 1" TRONG CONNECTION CONTEXT (Connection.md §3.3):
    F1 body-feedback = Luồng 1 (momentary, per-episode)
    Luồng 1 INDEPENDENT với Luồng 2 (Entity-Compiled structural)
    → CÓ THỂ CONFLICT: mẹ chăm con ốm (L1 negative + L2 positive)

  ⭐ SELF-TEMPLATE ≠ EMPATHY:
    F1 fire dùng SELF-TEMPLATE (compiled chunks CỦA MÌNH)
    "Tức hơn chính nó" = COMPOUND: empathy × L2 + self-template
    → F1 output CÓ THỂ > target's actual experience

  🟢 Singer 2004: shared activation areas
  🟢 Dimberg 2000: facial EMG mimicry, 300ms, pre-conscious
```

### §3.3 — F2: Fresh PFC draft prediction

```
⭐ F2 = FRESH PFC DRAFT:

  PFC chain draft predict hành vi target tiếp theo.
  "Target feel X → target thường do Y → kết quả Z → plan cho tôi."

  ĐẶC TÍNH:
    ① DELIBERATE — PFC PHẢI tham gia (sequential processing)
    ② CÓ THỂ CHẠY KHÔNG CẦN F1 — nhưng accuracy GIẢM
    ③ CÓ THỂ BỊ TẮT KHI F1 QUÁ MẠNH — "giận quá mất khôn"
       🟢 Arnsten 2009: PFC disconnect under NE surge
    ④ CÓ THỂ OVERRIDE F1 — qua training (bác sĩ, therapist)
    ⑤ COST > 0 MỖI LẦN (fresh)
       Cost = f(chain_length × novelty_degree)
       PFC-Operations §9: PFC Budget = shared, finite

  ⭐ F2 → F1 TRANSITION (Fresh → Compiled):
    F2 chain lặp đủ nhiều → Hebbian → automatic → trở thành F1
    = "Logic trở thành feeling" cho person đó, ở domain đó
    VD: therapist mới F2 dominant → experienced F1 dominant

  🟢 Dual Process Theory (Kahneman 2011): System 1 ≈ F1, System 2 ≈ F2
```

### §3.4 — Song song mặc định + 3 Modes

```
⭐ F1 + F2 CHẠY SONG SONG mặc định. 3 MODES tùy context:

  ┌─────────────┬───────────────┬───────────────┬──────────────────┐
  │ Mode        │ F1 (Compiled) │ F2 (Fresh)    │ Best for         │
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
⭐ PER-AGENT VALENCE QUYẾT ĐỊNH F1/F2 FIRE HƯỚNG NÀO:

  ┌──────────────────┬────────────────────┬────────────────────┐
  │ Per-Agent Valence │ F1 (Compiled)      │ F2 (Fresh)         │
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
  │ EXTREME NEGATIVE │ ⭐ F1 SUPPRESS     │ Logic THUẦN        │
  │ (dehumanized)    │ SPM tắt           │ Mechanical predict  │
  └──────────────────┴────────────────────┴────────────────────┘

  Valence là GATE, không phải input:
    Cùng 1 target cue (người khóc):
      Valence positive → F1 empathy + F2 help
      Valence negative → F1 reversed + F2 exploit
    → CÙNG cue, CÙNG mechanism, KHÁC output — vì KHÁC valence

  Valence DYNAMIC — thay đổi qua experience:
    Du lịch Việt Nam: neutral → positive (người thân thiện)
    Bị lừa đảo: neutral → negative (bị cướp)
    → Valence UPDATE liên tục qua interaction
    🟢 Fear conditioning: one-trial learning (LeDoux 1996)

  MIXED VALENCE (Body-Coupling.md §2.4):
    Mẹ: L1++ nhưng autonomy-- → F1 mixed, F2 multiple plans
    Sếp: status++ nhưng threat++ → highest cost (3-cost ALL apply)

  2 VAI TRÒ VALENCE:
    Vai trò 1 — GATE cho SPM (ảnh hưởng TỪNG episode)
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
  → Toán gia: years compile → "thấy" lời giải = F1 compiled
  → Therapist: years compile → "thấy" pattern = F1 compiled
  → KHÁC shareability. KHÔNG KHÁC quality of processing.

  🟢 Expert intuition = compiled patterns (Kahneman 2011, Klein 1998)
  🟡 "Shareable vs non-shareable" as organizing principle = framework synthesis
  Source: Inter-Body-Mechanism.md §3.4
```

### §3.7 — Per-Domain SPM + PFC=Lawyer

```
⭐ CÙNG 1 NGƯỜI → KHÁC DOMAIN → KHÁC F1/F2 RATIO:

  Einstein: toán = F1 dominant ("cảm thấy"), chính trị = F2 dominant ("suy luận")
  Therapist: tâm lý = F1 dominant ("thấy pattern"), toán = F2 dominant ("phải nghĩ")
  → "Feeling person" vs "Thinking person" = f(compilation level ở domain ĐANG HOẠT ĐỘNG)

⭐ PFC = LAWYER NOT JUDGE (Inter-Body-Mechanism §7):
  PFC build narrative AFTER body-need đã fire.
  SPM output qua PFC → PFC có thể:
    RATIONALIZE: "tôi giúp vì tốt bụng" (thật: L2 structural drive)
    CONFABULATE: "tôi ghét vì lý do X" (thật: compiled valence negative)
  → Stated reason cho SPM output ≠ actual body-need
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
  │ [4] SIMULATION — fire template ← ⭐ F1 CORE (compiled fire) │
  │      ↓                                                       │
  │ [5] OUTPUT READ — PFC observe ← BRIDGE (F1 → F2 handoff)   │
  │      ↓                                                       │
  │ [6] ATTRIBUTION — assign + chain ← ⭐ F2 CORE (fresh draft) │
  └──────────────────────────────────────────────────────────────┘

  Steps 1-3 = CHUẨN BỊ (chung cho cả 2 functions)
  Step 4 = F1 CORE (body simulate — compiled)
  Step 5 = BRIDGE (PFC observe → feed cả F1 lẫn F2)
  Step 6 = F2 CORE (attribute + chain draft — fresh)

  STEP 1 — RETRIEVE:
    Per-Agent Valence GATE → positive: empathy chunks, negative: threat chunks
    Schema priors bias retrieval. Recency + salience. State-dependent.
    ⭐ Context-dependent selection (§5): VÔ THỨC tùy agent + context

  STEP 4 — SIMULATION (F1 CORE):
    Body fire template as-if-self-were-target
    → Biochemistry THẬT: opioid, cortisol, oxytocin, NE
    → Intensity biến thiên: zero → very strong (gradient liên tục)
    🟢 Singer 2004: shared activation areas
    🟢 Dimberg 2000: facial EMG, 300ms

  STEP 5 — OUTPUT READ (BRIDGE):
    PFC observe simulation output. ⚠️ BIRD & COOK BOTTLENECK:
    → Step 5 REQUIRES self-awareness → alexithymia = FAIL here
    → F1 vẫn fire nhưng PFC cannot READ output
    → Feeling.md v3.0 §3: "PFC observation of body-chunk interaction"
    = Step 5 chính là Feeling mechanism applied to SPM context

  STEP 6 — ATTRIBUTION (F2 CORE + PFC=Lawyer):
    PFC assign "target feels X" → chain "target do Y → kết quả Z → plan A"
    ⚠️ PFC = Lawyer: stated reason ≠ actual body-need

  SPEED: F1 (ms-seconds) LUÔN nhanh hơn F2 (seconds-minutes)
    → "Cảm trước, hiểu sau" = compiled fires before fresh drafts
    → 6 steps là analytical scaffolding, không claim serial execution

  🟡 6-step mechanism: novel formalization, conceptually coherent
```

---

## §5 — Context-Dependent Selection

```
⭐ CÙNG 1 NGƯỜI, KHÁC CONTEXT → SPM TỰ CHỌN CHUNKS KHÁC:

  VỚI MẸ: retrieve "ngoan, quan tâm sức khỏe, xưng con-mẹ"
    → F1: fire respect + warmth (compiled từ years)
    → F2: chain "mẹ cần gì → giúp" (helping orientation)

  VỚI NHÓM BẠN: retrieve "thoải mái, sở thích, xưng mày-tao"
    → F1: fire casual warmth + fun
    → F2: chain "chơi gì tiếp → đề xuất" (peer negotiation)

  VỚI SẾP: retrieve "chuyên nghiệp, report, deadline"
    → F1: fire mix respect + caution (status uncertainty)
    → F2: chain "sếp cần gì → deliver" (professional)

  VỚI KẺ THÙ: retrieve "cảnh giác, điểm yếu đối thủ"
    → F1: fire tension + alertness
    → F2: chain "kẻ thù sẽ làm gì → phòng thủ" (strategic)

  → CÙNG 1 NGƯỜI (TÔI) nhưng SPM output KHÁC HOÀN TOÀN
  → VÔ THỨC — COMPILED qua years of interaction

  SCHEMA FALLBACK KHI CHUNKS THIẾU:
    1. SPM with thin chunks (best available)
    2. Schema template ("con gái thì dịu dàng")
    3. Pure logic (deterministic prediction)
    4. Avoid / give up

  VÍ DỤ — "PHỤ NỮ KHÓ HIỂU":
    Đàn ông A SPM chunks cho "phụ nữ" = THIN → SPM fire COARSE
    → Fallback schema → prediction thường SAI → "khó hiểu"
    → PFC=Lawyer: "phụ nữ KHÓ HIỂU" (blame target)
    → Thực tế: "SPM library CỦA TÔI thiếu" (library gap)
    🟡 "Khó hiểu" = confession about OWN library gap

  DOMAIN-SPECIFIC OVERLAP:
    5% overlap ở domain CRITICAL → SPM tốt ở domain đó
    95% overlap ở domain IRRELEVANT → SPM vẫn FAIL cho task hiện tại
    Einstein × Grossmann: khác personality nhưng DOMAIN overlap → deep connection
    🟢 Consistent: interpersonal synchrony research (Feldman 2007)
```

---

## §6 — Clone Spectrum + Over-Clone Reframe

### §6.1 — Clone = F1 output intensity gradient

```
⭐ CLONE = F1 FIRE ĐỦ MẠNH → OUTPUT LEAK RA BEHAVIOR:

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
  ⚠️ Clone ≠ deliberate. Clone = F1 OUTPUT automatic.
```

### §6.2 — ⚠️ Over-clone = OBSERVATION LABEL (Reframed)

```
⭐⭐ REFRAME (Drill-Over-SPM-Clarification v1.0):

  OBSERVATION: SPM rất sâu trên 1 entity → resonance GIẢM dần.
  "Over-clone kills resonance" = LABEL cho observation này.

  ⚠️ NHƯNG: MECHANISM ban đầu mô tả ĐÃ SAI:
    CŨ: "Own patterns REPLACED by target's patterns" → SAI
    CŨ: "Own gap direction CONVERGE" → SAI (gap-clone impossible)

  GAP-CLONE = IMPOSSIBLE (5-step proof):
    ① Gap = f(toàn bộ chunk network) — emergent, không copy được
    ② SPM chỉ THÊM chunks, không XÓA (Hebbian: wired = wired)
    ③ Entity-Compiled cho 1 partner = fraction nhỏ trong tổng network
    ④ Background Pattern RESIST (years, high link density)
    ⑤ Twin test: 100% DNA → gap VẪN KHÁC → SPM càng không thể
    🟢 Bouchard 1990: twins apart → similar but NOT identical
    🟡 "SPM cannot shift gap" = framework conclusion from proof

  MECHANISM THẬT — 4 mechanisms resonance decline:
    M1. Compiled suppress gap riêng (★ PRIMARY, nhân tạo, schema/fear)
    M2. Habituation (tự nhiên, Weber-Fechner → VTA giảm fire)
    M3. Prediction completion (tự nhiên, no novelty → no prediction-delta)
    M4. Entity-Compiled saturation (tự nhiên, plateau)

    M1 = ACCELERATOR cho M2+M3+M4. Fix M1 = fix hầu hết.
    M2-M4 = TỰ NHIÊN, có fix tự nhiên (grow riêng + shared novelty).

  TRUE UNDERSTANDING = ANTI-COMPILED-SUPPRESS:
    Shallow: "phải giống nhau" → suppress → resonance dies
    Deep: "khác nhau là giá trị" → support drives → resonance thrives
    → Khi partner MẤT → gap riêng QUAY LẠI = proof gap chỉ bị suppress

  SPM COST = CHỈ 2:
    ① Fresh processing mỗi lần tích lũy mới (metabolic, giảm khi compile)
    ② Compiled space per agent (Dunbar ceiling)
    → "Over-SPM thì mệt cái đầu thôi" — SPM càng sâu càng TỐT

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
    ② BACKGROUND PATTERN RESISTANCE: BP compiled sâu → resist suppress
    ③ AUTONOMY HARDWARE (vmPFC/DRN): detect controllability loss → signal

  Resistance = f(BP strength × Autonomy hardware × Age):
    Teen: BP forming + vmPFC immature → resistance THẤP (feature for social learning)
    Adult: BP stable + vmPFC mature → resistance TĂNG
    Post-trauma: BP disrupted + vmPFC depleted → resistance HẠ LẠI

  🟢 Efference copy: established neuroscience
```

---

## §7 — SPM → Resonance: 4 Conditions Đồng Thời

### §7.1 — SPM tăng xác suất resonance (KHÔNG tạo)

```
⭐ SPM KHÔNG TẠO RESONANCE. SPM TĂNG XÁC SUẤT.

  SPM → better action → match probability TĂNG → clone trust signal
  → calibrate → compile → Entity-Compiled → automatic
  = POSITIVE SPIRAL: SPM → match → reward → more SPM → compile
```

### §7.2 — 4 conditions ĐỒNG THỜI

```
⭐⭐ SPM → RESONANCE REQUIRES 4 CONDITIONS SIMULTANEOUSLY:

  ① POSITIVE VALENCE (hoặc neutral-to-positive):
     F1 fire empathy direction → approach behavior
     Negative → anti-resonance hoặc strategic only

  ② MUTUAL AGENT-MODE:
     CẢ HAI entities SPM fire toward NHAU
     1-way = parasocial (not resonance)
     Tool-mode = no resonance

  ③ BY-PRODUCT MATCH (Gap overlap đủ):
     SPM giúp TĂNG probability nhưng KHÔNG đảm bảo
     2 người SPM tốt nhưng gap KHÔNG overlap → no resonance

  ④ DRIVE RIÊNG MAINTAINED:
     ⚠️ v3.1 reframe: KHÔNG phải "clone within window"
     SPM cần đủ sâu (shallow → predict poorly)
     Drive riêng cần maintained (compiled suppress → lose by-product)
     "Đủ hiểu + GIỮ drive riêng" (not "đừng hiểu quá")

  → Thiếu BẤT KỲ 1 → KHÔNG CÓ resonance bền vững
  → Giải thích TẠI SAO resonance RARE dù SPM COMMON
  → SPM is NECESSARY but NOT SUFFICIENT for resonance

🟡 4-condition model = framework synthesis from SPM + BPGR + EC.
```

### §7.3 — SPM outcome phụ thuộc configuration

```
  ┌──────────────────────┬──────────────────────────────────────┐
  │ SPM configuration    │ Outcome                              │
  ├──────────────────────┼──────────────────────────────────────┤
  │ Positive + mutual    │ → TOWARD resonance (empathy pathway) │
  │ Positive + 1-way     │ → PARASOCIAL (fan → idol)            │
  │ Negative + mutual    │ → ANTI-RESONANCE (Schadenfreude)     │
  │ Strategic only       │ → TOOL-USE (no resonance intended)   │
  │ F1 suppress          │ → DEHUMANIZATION (F1 off)            │
  │ Compiled suppress    │ → Gap riêng suppressed → resonance   │
  │ (obs. "over-clone")  │ dies (§6.2)                          │
  └──────────────────────┴──────────────────────────────────────┘

→ SPM = TOOL. Resonance = 1 POSSIBLE OUTCOME.
```

---

## §8 — Abstract Entities Taxonomy

```
⭐ SPM FIRE DỰA TRÊN CHUNKS COMPILED — KHÔNG CHECK "CÓ THẬT KHÔNG":

  ┌─────────────────┬──────────────┬──────────────┬─────────────┐
  │ Entity          │ Compiled as  │ SPM fire?    │ Resonance?  │
  │                 │ agent?       │              │             │
  ├─────────────────┼──────────────┼──────────────┼─────────────┤
  │ Bạn thân        │ ✅ Yes       │ ✅ Full      │ ✅ Possible │
  │ Chó             │ ✅ Partial   │ 🟡 Limited   │ 🟡 Proto    │
  │ Thiên Chúa      │ ✅ Yes       │ ✅ Full      │ ❌ 1-way    │
  │ Harry Potter    │ ✅ Yes       │ ✅ Full      │ ❌ 1-way    │
  │ Quốc gia        │ ✅ Partial   │ 🟡 Moderate  │ ❌ Concept  │
  │ Thương hiệu     │ 🟡 Weak     │ 🟡 F2 only  │ ❌ Tool     │
  │ Cục đá          │ ❌ No       │ ❌ Zero     │ ❌ No       │
  │ AI hiện tại     │ ✅ Yes*     │ ✅ Full*    │ ❌ 1-way    │
  └─────────────────┴──────────────┴──────────────┴─────────────┘

  * AI: brain compiles as agent vì coherent responses → SPM fire THẬT
    NHƯNG AI KHÔNG có gap riêng → resonance KHÔNG khả thi
    = Risk: persistent parasocial investment

  THIÊN CHÚA: body respond THẬT (oxytocin, cortisol drop)
    = Religion's POWER. NHƯNG no feedback → calibration broken.
    🟢 Religion.md §2: 7-function analysis

  HARRY POTTER: body empathy THẬT (cry at fictional death)
    = Parasocial — brain KHÔNG phân biệt fiction/reality ở F1 level

🟡 SPM fires on compiled chunks, not ontology.
🟢 Parasocial: Horton & Wohl 1956. Fiction empathy: established.
```

---

## §9 — Background Pattern × SPM: Triple Bias

```
⭐⭐ BP BIAS SPM QUA 3 CƠ CHẾ ĐỒNG THỜI:

  CƠ CHẾ 1 — RETRIEVAL BIAS (Step 1):
    BP chunks = highest link density → fire TRƯỚC TẤT CẢ
    BP [cảnh giác] → retrieve "nguy hiểm" TRƯỚC → F1 tension TRƯỚC warmth
    BP [thoải mái] → retrieve "thú vị" TRƯỚC → F1 open TRƯỚC tension
    → CÙNG target, CÙNG cues → KHÁC prediction → vì KHÁC BP

  CƠ CHẾ 2 — TEMPLATE BIAS (Step 2-3):
    BP QUYẾT ĐỊNH "TÔI" trong template "nếu TÔI ở vị trí họ"
    BP [high anxiety] → "nếu tôi → tôi sẽ LO" → over-project anxiety
    BP [high confidence] → "nếu tôi → tôi sẽ OK" → under-detect distress

  CƠ CHẾ 3 — INTERPRETATION BIAS (Step 5-6):
    BP bias cách PFC interpret F1 output
    F1 "slight tension" + BP [suspicious] → "X đang giấu gì"
    F1 "slight tension" + BP [secure] → "chắc X hơi mệt"
    → PFC = Lawyer cho BP (rationalize theo BP direction)

  ⭐ SELF-FULFILLING PROPHECY:
    BP bias → biased prediction → biased action → biased outcome
    → CONFIRM BP → STRENGTHEN BP → VÒNG LẶP ĐÓNG KÍN

    VD: BP [người ta sẽ phản bội]:
      → SPM predict betrayal → defensive behavior → target withdraw
      → Withdrawal confirm BP → BP strengthen → next SPM MORE biased
    FIX: External feedback BREAK loop (therapy, trusted friend)

  → "Nhìn đời qua kính màu" = CHÍNH XÁC literal description

🟢 Confirmation bias: Nickerson 1998
🟢 Projection bias: Krueger 2007
🟢 Self-fulfilling prophecy: Merton 1948, Rosenthal & Jacobson 1968
🟡 Triple bias mechanism = framework synthesis from BP + SPM
```

---

## §10 — Multiple Models: Transfer + Interference

### §10.1 — SPM library = collection of agent-specific models

```
  S1 (~5 agents):   Model SÂU — nghìn chunks per agent
  S2 (~15 agents):  Model TRUNG BÌNH — trăm chunks per agent
  S3 (~50 agents):  Model NÔNG — chục chunks per agent
  S4 (~150 agents): Model CỰC NÔNG — vài chunks, F2 only
  Total: ~220 "models" tồn tại đồng thời (🟢 Dunbar 1992, 2024)
```

### §10.2 — Transfer learning = chunk sharing giữa models

```
⭐ "KINH NGHIỆM MẸ → PREDICT BẠN GÁI" = TRANSFER LEARNING:

  Mẹ compiled: "khi phụ nữ nói 'không sao' + mặt buồn = CÓ SAO"
  SPM on bạn gái MỚI → chunks specific ÍT → brain FALLBACK
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
⭐ 8 CÁCH SPM CHẠY NHƯNG RESONANCE KHÔNG EMERGE:

  CATEGORY A — PREDICTION ERROR (SPM chạy nhưng sai):
    FM1: OVER-PREDICTION — compiled model KHÔNG update
         "Mẹ tưởng hiểu con nhưng con đã thay đổi"
         FIX: re-open calibration loop (ask, listen, update)
    FM2: MODEL INTERFERENCE — chunks model A fire cho target B
         FIX: awareness + deliberate F2 override
    FM5: BP SYSTEMATIC BIAS — triple bias → self-fulfilling
         FIX: external feedback BREAK loop

  CATEGORY B — OUTPUT MALFUNCTION (SPM output bị lỗi):
    FM3: COMPILED SUPPRESS GAP RIÊNG — obs. "over-clone" (§6.2)
         Gap KHÔNG bị clone, chỉ bị suppress (M1)
         FIX: maintain own domains/interests
    FM6: ALEXITHYMIA BOTTLENECK — Step 5 fail
         🟢 Bird & Cook 2013 (DECISIVE): self-chunks thiếu → both fail
         FIX: build self-chunks FIRST (Focusing, labeling therapy)
    FM7: F1 OVERWHELM — cảm xúc quá → PFC offline
         🟢 Arnsten 2009: NE surge → PFC disconnect
         FIX: self-regulation training

  CATEGORY C — INTENTIONAL BLOCK (SPM bị chặn cố ý):
    FM4: STRATEGIC MODE — Tool giả Agent (sale smile)
         FIX: honest about own processing mode
    FM8: SCHEMA DEHUMANIZE — F1 suppress → target = object
         🟢 Bandura 1999: Moral Disengagement
         🟢 Grossman 1995: harder to kill face-to-face
         FIX: restore target as agent (exposure, narrative)
```

---

## §12 — Shared Substrate: SPM on Simulation Engine

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
    → SPM F1: FAIL (cannot read simulated body-state)
    → Imagine-Final: DEGRADED (cannot pre-feel future accurately)
    → = PROOF: 3 applications share 1 readout device

  INTERVENTION: train self-awareness → SPM improves AS SIDE EFFECT
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

### §13.1 — PFC-Operations × SPM

```
⭐ PFC-Operations.md: 2 operations trên Compiled/Fresh spectrum:

  HOLD = amplify pattern mới (PFC hold SPM model in working memory)
    → SPM on stranger = PFC HOLD multiple drafts (F2 fresh)
    → Cost: PFC Budget (shared, finite)
    → Mệt ở work → SPM cho con YẾU → "không phải không yêu con"

  SUPPRESS = block pattern cũ
    → SPM suppress compiled response (Mode B = suppress F1)
    → Cost: suppress CANNOT compile "not" → unsustainable
    → Bác sĩ suppress F1 empathy → cost tích lũy → burnout

  COMPILED QUALITY DIMENSION (PFC-Operations §5):
    Genuine-compiled: body confirmed → SPM accurate, reward = opioid
    Schema-compiled: PFC-driven → SPM biased by schema, reward = relief
    Threat-compiled: bị ép → SPM distorted by fear, reward = cortisol drop
    → Cùng "compiled SPM" nhưng KHÁC quality → KHÁC SPM output lifetime
```

### §13.2 — Entity-Access × SPM

```
⭐ Entity-Access.md: mPFC gradient = Entity-Access spectrum:

  🟢 Mitchell 2006: ventral mPFC = self + close other (Mức 4-5)
  🟢 Mitchell 2006: dorsal mPFC = distant/dissimilar (Mức 1-2)

  Entity-Access Mức 5 (body-base extension):
    → SPM on deep Entity: F1 compiled SÂU, cost ≈ 0
    → "Hiểu không cần nói" = composite compiled
    → Luồng 2 structural reward SUSTAINED

  Entity-Access Mức 1 (schema-only):
    → SPM on stranger: F2 fresh dominant, cost > 0
    → Schema fallback, prediction coarse

  → Entity-Access level = DETERMINES SPM processing mode
  → Access TĂNG = SPM shift từ Fresh → Compiled (cost giảm, accuracy tăng)
  → Entity-Access gradient = mPFC gradient = Compiled/Fresh gradient cho SPM
```

### §13.3 — Entity-Compiled × SPM

```
  Entity-Compiled.md: SPM → Entity-Compiled lifecycle:
    SPM fire repeated → Hebbian → Entity-Compiled forms
    Entity-Compiled = agent → body-base extension
    → Hub-and-Spoke model (5 S1 agents maximum)
    → 🟢 Dunbar 1992, 2024: Social Brain Hypothesis

  GRIEF = Entity-Compiled disruption:
    Entity MẤT → compiled model STILL EXISTS → SPM still fires
    → F1 fire on ABSENT entity → body respond → pain THẬT
    → = Tại sao grief CÓ cost thật (not "just sad")
```

---

## §14 — Developmental Trajectory

```
⭐ SPM LIFECYCLE = TRADEOFF DEPTH vs FLEXIBILITY:

  ┌────────────┬──────────────────────┬───────────────────────────┐
  │ Giai đoạn  │ SPM state            │ Resonance capability      │
  ├────────────┼──────────────────────┼───────────────────────────┤
  │ 0-6 tháng  │ NO SPM (contagion)   │ Hardware ONLY (oxytocin)  │
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

## §15 — Reversed Mapping + Professional SPM + Moral Injury

### §15.1 — Schadenfreude: F1 REVERSED khi valence negative

```
  Khi Per-Agent Valence ÂM → F1 output BỊ ĐẢO:
    Bình thường: "bạn buồn → tôi buồn" = empathy
    Reversed: "kẻ thù đau → tôi SƯỚNG" = Schadenfreude

  TẠI SAO REWARD: ① L0 safety TĂNG ② justice satisfied ③ relative status TĂNG
  F1 VẪN FIRE — cùng compiled simulation, valence đảo hướng interpretation
  🟢 Takahashi 2009: ventral striatum khi misfortune befalls envied person
  🟢 Cikara 2014: counter-empathy in competitive contexts
```

### §15.2 — Sadism vs Dehumanization

```
  DEHUMANIZATION: F1 SUPPRESS → target = object → no simulation → giết COLD
  SADISM: F1 FIRE STRONG + REVERSED → active creation of suffering
    → REQUIRES empathy mechanism HOẠT ĐỘNG (để simulate)
    → REQUIRES target remain AGENT (nếu dehumanize → mất reward)
  → 2 paths KHÁC NHAU từ cùng extreme negative valence
  🟢 Bandura 1999: Moral Disengagement
```

### §15.3 — Professional SPM conflicts

```
  BÁC SĨ: F2 FULL (surgery) + F1 cost tích lũy → burnout
  THERAPIST: F1 HIGH (empathize) + overload → compassion fatigue
    🟢 Figley 2002: compassion fatigue
  SOLDIER: F2 strategic + F1 suppress → post-combat F1 REBOUNDS → PTSD
    🟢 Milgram 1963: extreme distress
```

### §15.4 — Moral injury = 3-cost model

```
⭐ MORAL INJURY: F1 BỊ BUỘC FIRE TRÊN ACTIONS MÂU THUẪN VỚI VALUES:

  3-COST ALL FIRING SIMULTANEOUSLY:
    ① PFC Draft: process complex moral reasoning
    ② Suppress: suppress F1 empathy response (chronic)
    ③ Uncertainty: "tôi đang đúng hay sai?" (unresolvable)
  → Total cost CỰC CAO. Duration chronic → UNSUSTAINABLE.

  2-LUỒNG GIẢI THÍCH KHÁC OUTCOME:
    Bác sĩ + bệnh nhân lạ: L1 negative + L2 ≈ 0 → burnout
    Mẹ chăm con ốm (CÙNG F1): L1 negative + L2 STRONG → KHÔNG burnout
    → Biến số = Luồng 2 bù Luồng 1 hay không

  KHÁC PTSD: PTSD = threat TO self. Moral injury = threat FROM self.
  🟢 Litz 2009: moral injury — distinct from PTSD
```

### §15.5 — Strategic SPM: suppress + fake cues + meta-SPM

```
  3 CHIẾN LƯỢC GIA:
    ① POKER FACE: suppress cues → starve đối thủ's F1 input
    ② FAKE CUES: feed wrong cues → đối thủ F1 fire on giả
       🟢 DePaulo et al. 2003: deception detection ≈ 54% (near chance)
       VD: "Thành không kế" — Gia Cát Lượng hack Tư Mã Ý's SPM
    ③ META-SPM: SPM on opponent's SPM process → control entire chain
       Level 1: đọc đối thủ. Level 2: đối thủ đang đọc tôi.
       Level 3: predict đối thủ's SPM. Level 4: control cues.

  TẤT CẢ dùng CÙNG mechanism — chỉ HƯỚNG khác
  "Biết địch biết ta, trăm trận trăm thắng" = compiled meta-SPM
  🟢 Ekman 2003: micro-expressions leak even when suppressed
```

---

## §16 — Training + AI Era

### §16.1 — Training methods

```
⭐ SPM QUALITY LÀ TRAINABLE:

  FOUNDATION — Self-chunk training (upstream, Bird & Cook):
    → 🟢 Focusing (Gendlin 1978), Mindfulness, emotional labeling
    → Body-based: yoga, tai chi, somatic experiencing

  F1-SPECIFIC: deep listening, compassion meditation, fiction, cross-cultural
  F2-SPECIFIC: perspective-taking, strategic games, journaling
  CONTEXT-SELECTION: diverse social engagement, role-play, travel
  MODE-SWITCHING: therapist (Mode A), negotiator (Mode B), leader (Mode C)

  Compilation as training goal: F2 chains → compile → F1 (§3.6)
  "Natural talent" = partially Resonance Baseline (hardware overlap)
  "Learned skill" = compiled through practice. Both produce SAME quality.
```

### §16.2 — AI era implications

```
  RISK 1 — Screen replaces feedback-rich interaction → thin SPM library
  RISK 2 — Parasocial at scale (celebrities, AI companions, no calibration)
  RISK 3 — AI-triggered SPM without agent reality
    → SPM fires on CUES, not beliefs (same as §15.5 fake cues)
    → Long-term: library distortion

  OPPORTUNITY — Training at scale: meditation apps, SPM literacy, AI-assisted therapy
  → Individual SPM literacy = critical skill for AI era
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
  Gailliot & Baumeister 2007: cognitive effort = metabolic cost
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
  APPLICATION 1 on Simulation Engine (3 apps, 1 hardware)
  1 mechanism × 3 dimensions restructure (not 4 skills)
  F1/F2 = Compiled/Fresh as real axis (not Feeling/Logic)
  Expert intuition = compiled, shareable vs non-shareable
  PFC=Lawyer caveat on all SPM output
  Per-domain SPM ratio (not per-person fixed)
  4 simultaneous conditions for resonance
  Over-clone reframed: observation label, mechanism = compiled suppress
  Gap-clone impossible (5-step proof)
  SPM cost = only 2 (Fresh processing + space)
  True understanding = anti-compiled-suppress
  4 mechanisms resonance decline (M1-M4)
  BP → SPM triple bias mechanism
  Transfer learning as chunk sharing + Freud reframe
  8 failure modes → 3 categories
  Clone spectrum as Dimension 3
  Diversity → self-calibration via dMPFC contrast
  Bidirectional social-self loop
  3-cost applied to moral injury / professional SPM
  Entity-Access gradient = SPM processing mode

═══ 🔴 HYPOTHESIS ═══

  Precise F1/F2 neural dissociability
  Valence gate precise circuitry
  Training ceiling predictions
  AI library distortion long-term effects
  PFC=Lawyer distortion magnitude measurement
  3-cost independent measurement protocol
  Per-domain F1/F2 ratio measurement
  Diversity threshold for significant calibration
  Interoception training duration → measurable SPM improvement
```

---

## §18 — Cross-References

```
  ENGINE:
    → Simulation-Engine.md v1.0 — SHARED ENGINE: 3 components × 3 axes
    → PFC-Operations.md v1.0 — Hold/Suppress, Compiled Quality, PFC Budget

  PARENT + SIBLING:
    → Agent-Mechanism.md v2.1 — integration hub, §5 SPM preview
    → By-Product-Gap-Resonance.md v1.0 — emergent mutual phenomenon (2-Stream)

  MECHANISM FILES:
    → Entity-Compiled.md v1.0 — lifecycle, Hub-and-Spoke, Dunbar, grief
    → Entity-Access.md v1.0 — mPFC gradient, 3-Factor Model, spectrum
    → Inter-Body-Mechanism.md v1.0 — Compiled/Fresh axis, 3-cost, Architecture B
    → Chunk.md v2.0 — chunk substrate, compilation
    → Feeling.md v3.0 — PFC observation interface (Step 5 = Feeling applied)
    → Logic-Feeling.md v2.1 — 2 processing modes, parallel, modality bias
    → Valence-Propagation.md v2.0 — per-entity valence, chain propagation
    → Body-Coupling.md v2.0 — coupling mechanism (builds ON SPM)
    → Body-Feedback-Mechanism.md v2.0 — 2-source model, chunk dynamics
    → Background-Pattern.md v1.1 — 2D Depth×Density, §8 self-reinforcing
    → Cortisol-Baseline.md v2.1 — stress cascade, moral injury pathway
    → Autonomy-Hardware.md v1.1 — vmPFC/DRN, efference copy

  OBSERVATION FILES:
    → Connection.md v4.0 — 3 generative primitives, 2-luồng reward (L1/L2)
    → Empathy.md v3.0 — SPM function applied to other agents
    → Status.md v2.0 — Resource Access Map, status scan
    → Protect.md v1.0 — ownership, loss aversion
    → Threat.md — NE cascade, PFC disconnect

  APPLICATION:
    → Imagine-Final.md v2.0 — APPLICATION 2 on Simulation Engine
    → AI-Schema-Detection.md v2.0 — AI interaction × SPM
    → Somatic-Articulation-Loop.md — body → words

  COLLECTIVE:
    → Resonance-Entity.md v2.0 — Hardware Subsidy, RSA A:B
    → Resonance-Sustainability.md v1.0 — 3 Modalities, Silence, Capitalization
    → Entity-Valence-Dynamics.md v2.0 — Phantom resonance

  HEALTH:
    → ADHD-Observation.md §10 — late diagnosis SPM re-compile
    → Autism-Observation.md §10 — double empathy problem
    → PTSD-Analysis.md §11 — C-PTSD = SPM compiled under chronic threat
    → OCD-Analysis.md §4.7 — Autism × OCD overlap 17.4%

  DRILL SOURCES:
    → Drill-SPM-Mechanism-Analysis v2.2 (17 insights)
    → Drill-Over-SPM-Clarification v1.0 (12 insights) — backup/ (REFERENCE)
    → Drill-SPM-Self-Shared-Substrate v1.0 (13 insights)
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
  R12. Buckner, Andrews-Hanna & Schacter 2008: DMN = simulation engine
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
  R23. Gailliot & Baumeister 2007: cognitive effort = metabolic cost
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

> *Bạn thấy bạn thân khóc → body bạn buồn nhẹ. Đó là F1 — COMPILED simulation.*
> *Bạn nghĩ: "bạn cần an ủi." Đó là F2 — FRESH PFC draft.*
>
> *Bạn thấy kẻ thù gục ngã → body bạn... nhẹ nhõm. Vẫn F1 — nhưng REVERSED.*
> *Bạn nghĩ: "giờ mình an toàn hơn." Vẫn F2 — nhưng strategic.*
>
> *Cùng 1 mechanism. Cùng 6 steps. Cùng chunk library.*
> *Nhưng Per-Agent Valence đảo hướng mọi thứ.*
>
> *SPM = APPLICATION 1 trên Simulation Engine.*
> *Self-Observation, Imagine-Final = 2 apps khác, CÙNG substrate.*
> *Luyện 1 = luyện cả 3. Hỏng 1 = hỏng cả 3.*
> *Modeling — không phải matching. Forward simulation — không phải tìm-khớp.*
