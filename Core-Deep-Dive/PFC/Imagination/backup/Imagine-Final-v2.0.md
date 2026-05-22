---
title: Imagine-Final — Future Simulation Application trên Simulation Engine
version: 2.0
created: 2026-03-27
updated: 2026-05-22
status: MECHANISM v2.0
scope: |
  APPLICATION file: Imagine-Final = (Self, Future, Simulate+Construct) trên Simulation Engine.
  Reference Pattern: body PRE-FEEL future state → gap tạo drive → PFC check domain.
  3-Layer Hierarchy: Body-Need (WHY) → Imagine-Final (WHERE) → Plan (HOW).
  Lifecycle 5 phases: BUILD → SAVE → BACKGROUND → RELOAD → REFINE.
  Gradient 5 levels (Wish → Obsession). 3 chiều độc lập: Clarity × Quality × Trust.
  PFC Operations integration: Hold/Suppress × Imagine-Final, Compiled/Fresh.
  Entity-Access integration: per-entity Imagine-Final, social scale.
  Engine use quality: Reflection vs Rumination modifier.
purpose: |
  Simulation-Engine.md = SHARED ENGINE underneath tất cả applications.
  SPM.md = APPLICATION 1: simulate OTHER (present).
  Feeling.md = APPLICATION 2: observe SELF (present).
  File NÀY = APPLICATION 3: simulate SELF (future). 
  = MECHANISM file cho future simulation — HOW brain constructs, maintains, uses previews.
  = Giải thích TẠI SAO: cùng "mục tiêu" nhưng body engagement KHÁC → outcome KHÁC.
position: |
  Core-Deep-Dive/PFC/Imagination/ — cùng thư mục với companion files.
  ENGINE at Simulation-Engine.md (PFC/). PFC OPERATIONS at PFC-Operations.md (PFC/).
  Anchor-Schema.md = khi Imagine-Final content THÀNH sync point (committed).
  Imagine-Final-Evaluation.md = QUALITY check (Domain Fit × Hardware Fit).
dependencies:
  - Simulation-Engine.md v1.0 — ENGINE: 3 components, 3 axes, shared substrate
  - PFC-Operations.md v1.0 — Hold/Suppress, Compiled Quality, Architecture B
  - Entity-Access.md v1.0 — gradient Mức 0-5, per-entity dynamics
  - Entity-Compiled.md v1.0 — HOW brain compiles entity vào body-base
  - Body-Feedback-Mechanism.md v2.0 — chunk dynamics, body-feedback readout
  - Body-Input-Enumeration.md v2.0 — L0/L1/L3 taxonomy (body-need layer)
  - Cortisol-Baseline.md v2.1 — cortisol direction tag, activation gating
  - Anchor-Schema.md v1.0 — sync point, Trust, 4 nguồn fill
  - Imagine-Final-Evaluation.md v1.1 — Quality dimension (Domain × Hardware Fit)
  - Boredom.md v1.1 — no Imagine-Final = "chán", Imagine-Final modifier
  - Connection.md v4.0 — social context, 2-tầng reward
  - Meaning.md v2.0 — life-level Anchor-Schema
sources:
  - Drill-Simulation-Engine v1.0 (809L, 16 insights, 23 citations)
  - Drill-SPM-Self-Shared-Substrate v1.0 (~680L, 13 insights, 22 citations)
  - Imagine-Final.md DRAFT (1,494L, 2026-03-27 — file CŨ NHẤT framework)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Imagine-Final — Future Simulation Application trên Simulation Engine

> **Bạn có "mục tiêu", "ước mơ", "tầm nhìn", "lý tưởng"...**
> **Tất cả chỉ là CÁC MỨC KHÁC NHAU của cùng 1 thứ:**
> **Imagine-Final — body PRE-FEEL trạng thái tương lai RÕ và SÂU đến đâu.**
>
> **Imagine-Final = APPLICATION (Self, Future, Simulate+Construct) trên Simulation Engine.**
> **Cùng engine với SPM (simulate other) và Self-Observation (observe self).**
> **Nhưng: MOST PFC-ACCESSIBLE — PFC có thể SET scenario, READ output, ITERATE.**
>
> **3 tầng: Body-Need (TẠI SAO) → Imagine-Final (VỀ ĐÂU) → Plan (BẰNG CÁCH NÀO).**
> **"GPU sẽ có giá trị" = plan parameter (③). Jensen Huang's Imagine-Final = "NVIDIA thành reference computing" (②).**
>
> **Không có nó → "chán". Có nó → cùng khó nhưng "xứng đáng".**
> **RÕ ≠ ĐÚNG ≠ TIN. 3 chiều độc lập: Clarity × Quality × Trust.**

---

## Mục lục

- §0 — THESIS + POSITION
- §1 — SIMULATION ENGINE APPLICATION
- §2 — 2 TẦNG: VÔ THỨC BASE + PFC EXTENSION
- §3 — PFC OPERATIONS × IMAGINE-FINAL
- §4 — LIFECYCLE: 5 PHASES
- §5 — GRADIENT: 5 LEVELS
- §6 — 3 CHIỀU ĐỘC LẬP: CLARITY × QUALITY × TRUST
- §7 — ENTITY-ACCESS × IMAGINE-FINAL
- §8 — ENGINE USE QUALITY: REFLECTION vs RUMINATION
- §9 — HẬU QUẢ + NÂNG CẤP
- §10 — IMAGINE-FINAL × BROADER FRAMEWORK
- §11 — HONEST ASSESSMENT
- §12 — CROSS-REFERENCES
- §13 — RESEARCH CITATIONS

---

## §0 — THESIS + POSITION

### §0.1 — Core thesis

```
⭐⭐⭐ IMAGINE-FINAL:

  ⚠️ QUY ƯỚC: luôn viết "Imagine-Final" đầy đủ, KHÔNG viết tắt "IF"
     (vì "IF" dễ nhầm với "if" trong tiếng Anh hoặc programming)

  ① Imagine-Final = APPLICATION (Self, Future, Simulate+Construct)
    trên Simulation Engine (Simulation-Engine.md)
  ② Body PRE-FEEL trạng thái tương lai = Reference Pattern
    → Mỗi chunk mới PHẢN XẠ với pattern này: "đúng hướng" hay "vô nghĩa"
  ③ 3-Layer Hierarchy: Body-Need → Imagine-Final → Plan
    → Body-Need = TẠI SAO (hardware, luôn tồn tại)
    → Imagine-Final = VỀ ĐÂU (body preview destination)
    → Plan = BẰNG CÁCH NÀO (PFC strategy, thay đổi linh hoạt)
  ④ MOST PFC-ACCESSIBLE application: PFC = DIRECTOR
    → SET scenario + READ output + ITERATE + COMPARE alternatives
  ⑤ Shared substrate với SPM + Self-Observation → luyện 1 = luyện cả 3
  ⑥ Lifecycle: BUILD → SAVE → BACKGROUND → RELOAD → REFINE → loop
  ⑦ Gradient 5 levels: Wish (0-20%) → Obsession (80-100% body fidelity)
  ⑧ 3 chiều ĐỘC LẬP: Clarity (rõ?) × Quality (đúng?) × Trust (tin?)
  ⑨ Dormant khi harmony, FIRE khi dissonance (cortisol gates)
  ⑩ Engine use quality: Reflection (curiosity) → explore vs Rumination (threat) → catastrophize
  
  🟢 Prospection: Seligman et al. 2013, Gilbert & Wilson 2007
  🟢 Constructive simulation: Schacter & Addis 2007 (Nature Reviews Neuroscience)
  🟢 Somatic Marker Hypothesis: Damasio 1994 (body informs decisions)
  🟢 Goal-setting theory: Locke & Latham 1990
  🟡 "Application on Simulation Engine" model = framework synthesis
  🟡 3-Layer Hierarchy = framework synthesis (consistent with SDT + Predictive Processing)
```

### §0.2 — Position

```
  VỊ TRÍ TRONG KIẾN TRÚC:

  ★ Simulation-Engine.md = ENGINE (shared substrate)
    │
    ├── SPM.md = APPLICATION 1: (Other, Present, Simulate)
    │   = Predict other's state/behavior
    │
    ├── Feeling.md = APPLICATION 2: (Self, Present, Observe)
    │   = Observe current body-state
    │
    ├── ★ File NÀY = APPLICATION 3: (Self, Future, Simulate+Construct)
    │   = Preview future state, create gaps, planning tool
    │
    ├── PFC-Operations.md = HOW PFC operates trên engine
    │   = Hold/Suppress on Compiled/Fresh spectrum
    │
    └── Entity-Access.md = APPLIED
        = mPFC gradient → per-entity simulation processing

  COMPANION FILES cùng thư mục:
    Imagine-Final-Evaluation.md = QUALITY check (Domain × Hardware Fit)
    Anchor-Schema.md = khi Imagine-Final content THÀNH sync point (committed)
    Imagination.md = overview
    Somatic-Articulation-Loop.md = body-knowledge → explicit-knowledge

  CÁI MỚI (v2.0 vs DRAFT):
    → Simulation Engine integration (shared substrate, coordinates)
    → PFC Operations integration (Hold/Suppress × Imagine-Final)
    → Entity-Access integration (per-entity Imagine-Final dynamics)
    → Compiled/Fresh spectrum applied to Imagine-Final operations
    → Engine use quality (Reflection vs Rumination)
    → Standard YAML frontmatter + Research Citations format
    → v7.8+ alignment hoàn chỉnh
```

### §0.3 — 3-Layer Hierarchy

```
⭐⭐ PHÂN BIỆT 3 TẦNG mà ngôn ngữ thường TRỘN LẪN:

  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG ①: BODY-BASE NEED (nguồn gốc — "TẠI SAO")               │
  │                                                                 │
  │   = Nhu cầu vô thức LUÔN tồn tại, drive MỌI hành vi           │
  │   = L0 Alive (binary) / L1 Body-inputs (graded) / L3 PFC drive│
  │   = KHÔNG BAO GIỜ là Imagine-Final — là NGUỒN sinh ra          │
  │                                                                 │
  │   VD: "Cần kết nối" (L1) / "Cần chứng minh giá trị" (L3)     │
  ├─────────────────────────────────────────────────────────────────┤
  │ TẦNG ②: IMAGINE-FINAL (reference pattern — "VỀ ĐÂU")          │
  │                                                                 │
  │   = Body's PRE-FELT preview of END STATE that satisfies ①      │
  │   = File NÀY mô tả chi tiết tầng NÀY                          │
  │   = BRIDGE giữa body-need (muốn gì) và domain (thật ra sao)   │
  │                                                                 │
  │   VD: "THẤY TRƯỚC mình đạt thành tựu" / "THẤY TRƯỚC buổi gặp"│
  ├─────────────────────────────────────────────────────────────────┤
  │ TẦNG ③: PLAN + PARAMETERS (công cụ — "BẰNG CÁCH NÀO")         │
  │                                                                 │
  │   = PFC strategy + domain knowledge chunks hỗ trợ              │
  │   = Có thể thay đổi hoàn toàn mà ② vẫn giữ nguyên            │
  │                                                                 │
  │   VD: "GPU sẽ có giá trị" (domain prediction = parameter)      │
  └─────────────────────────────────────────────────────────────────┘

  FLOW: ① → ② → ③ → action → domain feedback → update ②③

  TẠI SAO PHÂN BIỆT NÀY QUAN TRỌNG:
    → Cùng ② có thể có NHIỀU ③ khác nhau (nhiều plans cho 1 mục tiêu)
    → Cùng ① có thể sinh NHIỀU ② (nhiều Imagine-Finals cho 1 body-need)
    → ③ thay đổi LINH HOẠT NHẤT. ② ổn định HƠN. ① ổn định NHẤT.
    → "Bỏ plan" ≠ "bỏ mục tiêu" ≠ "bỏ nhu cầu"

  MỌI IMAGINE-FINAL PHỤC VỤ BODY-BASE:

  ┌─────────────┬──────────────────────────┬──────────────────────┐
  │ Scale       │ Imagine-Final (②)        │ Body-need gốc (①)   │
  ├─────────────┼──────────────────────────┼──────────────────────┤
  │ Micro       │ "Ăn xong → no"           │ L1 nutrition         │
  │ Short       │ "Gặp bạn → vui"          │ L1 connection        │
  │ Medium      │ "Xong project → reward"   │ L3 Novelty + Status │
  │ Long        │ "NVIDIA thành công"       │ L3 Status + Novelty  │
  └─────────────┴──────────────────────────┴──────────────────────┘
  
  🟢 SDT basic needs → goals → strategies: Deci & Ryan 2000
  🟡 3-Layer explicit formalization = framework synthesis
```

---

## §1 — SIMULATION ENGINE APPLICATION

### §1.1 — Coordinates in 3D space

```
⭐⭐ IMAGINE-FINAL = POINT IN APPLICATION SPACE:

  Simulation Engine 3 trục (Simulation-Engine.md §2):
    Trục A (Target):    SELF (ventral mPFC)
    Trục B (Time):      FUTURE (construct novel scenario)
    Trục C (Operation): SIMULATE + CONSTRUCT (PFC active)

  → Imagine-Final = (Self, Future, Simulate+Construct)

  SO SÁNH VỚI CÁC APPLICATION KHÁC:
  ┌──────────────────┬──────────────┬───────────┬──────────┐
  │ Application      │ Target       │ Time      │ Operation│
  ├──────────────────┼──────────────┼───────────┼──────────┤
  │ SPM              │ Other        │ Present   │ Simulate │
  │ Self-Observation │ Self         │ Present   │ Observe  │
  │ ★ Imagine-Final  │ Self         │ Future    │ Sim+Cons │
  │ Memory Recall    │ Self         │ Past      │ Simulate │
  │ Counterfactual   │ Self/Other   │ Alt-Past  │ Sim+Cons │
  │ Decision Branch  │ Self         │ Future×N  │ Sim×N    │
  │ Predict Other    │ Other        │ Future    │ Simulate │
  └──────────────────┴──────────────┴───────────┴──────────┘

  → TẤT CẢ chạy trên CÙNG engine (DMN + mPFC + insula + hippocampus)
  → Khác nhau ở COORDINATES, không phải ở hardware
  → Decision Branch = Imagine-Final run N times + compare
  → Predict Other's Future = SPM + Imagine-Final combined
    = "Con sẽ thế nào nếu tôi ép?" (Entity-Access §9)

  🟢 Buckner & Carroll 2007: all = "self-projection" in DMN
  🟢 Schacter & Addis 2007: constructive episodic simulation
  🟡 Coordinate model = framework synthesis
```

### §1.2 — 3 Components × Imagine-Final

```
⭐⭐ SIMULATION ENGINE 3 COMPONENTS (Simulation-Engine.md §1):

  COMPONENT 1 — INTEROCEPTION (anterior insula) = "MÀN HÌNH":
    → Imagine-Final: đọc body-feedback từ simulated future state
    → "Nếu tôi bỏ việc → body feel gì?" = insula readout
    → QUALITY CỦA READOUT → quyết định accuracy of preview
    → Alexithymia (broken readout) → cannot PRE-FEEL future
      → Imagine-Final DEGRADED: "biết sẽ tốt" nhưng không FEEL
    → 🟢 Bird & Silani 2010: anterior insula = shared readout
    → 🟢 Fukushima 2011: interoceptive accuracy → empathic accuracy

  COMPONENT 2 — CONSTRUCTIVE SIMULATION (DMN + hippocampus) = "CPU":
    → Imagine-Final: hippocampus RETRIEVE chunks + DMN RECOMBINE
    → Chunks AVAILABLE quyết định WHAT futures imaginable
    → Ít chunks = Imagine-Final generic/mờ (Level 1-2)
    → Nhiều experience chunks = Imagine-Final vivid (Level 4-5)
    → = WHY "nạp chunks thật" > "nghĩ tích cực" cho nâng level
    → 🟢 Hassabis et al. 2007: hippocampal amnesia → cannot imagine
    → 🟢 Schacter, Addis & Buckner 2007: constructive simulation

  COMPONENT 3 — SELF/OTHER MODEL (mPFC gradient) = "BẢNG ĐIỀU KHIỂN":
    → Imagine-Final: target = FUTURE SELF (ventral mPFC)
    → "Tôi SẼ thế nào" = simulate SELF → interoception AVAILABLE
    → "Bạn SẼ thế nào" = simulate OTHER → interoception INFERRED
    → Entity-Access integration: close entity → vMPFC → simulate AS self
      → "Mẹ simulate con's future" = Entity-Access high → vMPFC process
    → 🟢 Mitchell 2006: vMPFC/dMPFC dissociation
    → 🟢 Denny et al. 2012: spatial gradient meta-analysis
```

### §1.3 — MOST PFC-ACCESSIBLE application

```
⭐ PFC ACCESSIBILITY SPECTRUM (Simulation-Engine.md §8):

  ┌──────────────┬────────────────────────────────────────────┐
  │ APPLICATION  │ PFC ROLE                                    │
  ├──────────────┼────────────────────────────────────────────┤
  │ SPM F1       │ LEAST: compiled, automatic, invisible       │
  │ Dream/Mind W.│ ZERO: engine free-run during sleep          │
  │ Self-Obs     │ MIDDLE: PFC observe, cannot manipulate      │
  │ SPM F2       │ MODERATE: PFC draft model deliberately      │
  │ ★ Imagine-F. │ MOST: PFC SET scenario + READ + ITERATE    │
  │ Decision     │ HIGHEST: Imagine-Final ×N + COMPARE         │
  └──────────────┴────────────────────────────────────────────┘

  IMAGINE-FINAL = RICHEST APPLICATION vì:
    → PFC CAN OBSERVE output (unlike SPM F1 = invisible)
    → PFC CAN MANIPULATE input ("nếu thay đổi X thì sao?")
    → PFC CAN COMPARE multiple simulations ("option A vs B")
    → PFC CAN ITERATE ("thêm condition → feel gì?")
    → = CONSCIOUS SIMULATION TOOL (planning, decision, risk assessment)

  UNIQUE CAPABILITIES (beyond shared engine):
    → SCENARIO COMPARISON: simulate A vs B → compare body-feedback
    → TIMELINE PROJECTION: simulate tomorrow vs next year vs retirement
    → RISK ASSESSMENT: simulate threat → body pre-feel → avoid/approach
    → GAP CREATION: simulate desired state → gap CREATED → drive GENERATED
      = Body-Feedback-Mechanism §3.3c: Imagine-Final preview → compile baseline → gap→miss
    → EMPATHY EXTENSION: "nếu TÔI là HỌ trong TƯƠNG LAI"
      = SPM + Imagine-Final combined → parenting, mentoring

  🟢 Drill-SPM-Self-Shared-Substrate §9: Imagine-Final = PFC-observable output
  🟡 "Most PFC-accessible application" = framework synthesis
```

### §1.4 — Shared substrate implications

```
⭐ 3 APPLICATIONS TRÊN 1 HARDWARE → IMPLICATIONS:

  LUYỆN 1 = LUYỆN CẢ 3:
    → Interoception training (meditation, Focusing) → improve:
      ① Self-Observation: "biết mình feel gì" clearer
      ② SPM: "biết người khác feel gì" more accurate
      ③ Imagine-Final: "feel trước tương lai" more vivid
    → = 1 training → ≥3 applications improved

  HỎNG 1 = HỎNG CẢ 3:
    → Alexithymia (broken interoception readout) →
      Self-Obs FAIL + SPM FAIL + Imagine-Final DEGRADED
    → 🟢 Bird & Cook 2013: decisive proof for shared substrate

  SOCIAL ↔ SELF BIDIRECTIONAL:
    → SPM practice (diverse interactions) → sharper self-model
    → Sharper self-model → better future simulation
    → Better future prediction → better social decisions → more practice
    → = VIRTUOUS SPIRAL (Connection.md §3)
    → Isolation → NO practice → ALL applications atrophy → VICIOUS SPIRAL

  🟢 Lombardo 2010: identical connectivity SPM↔Self
  🟢 Lopes et al. 2003: regulation ↔ interaction bidirectional
  🟡 Bidirectional spiral model = framework synthesis
```

---

## §2 — 2 TẦNG: VÔ THỨC BASE + PFC EXTENSION

### §2.1 — Tầng 1: Vô thức (BASE)

```
⭐⭐ VÔ THỨC = GỐC, LUÔN CHẠY, PFC KHÔNG CẦN BIẾT:

  Body-base LUÔN CÓ expectation patterns ở MỌI scale:

    Micro (giây→phút):
      → Đang ăn → body preview "no" → tiếp tục ăn
      → Gặp ai đó → body preview "thoải mái" → approach
      → = Mọi hành vi đều có micro-Imagine-Final VÔ THỨC

    Short (phút→giờ):
      → "Gặp người này → melody mượt hơn" → seek connection
      → "Ăn xong → thoải mái" → chịu đợi

    Medium (ngày→tháng):
      → "Xong project → body reward" → chịu dissonance hàng ngày
      → "Học skill → sẽ dùng được" → chịu investment cost

    Long (năm→đời):
      → Compiled DEEP → body feel "hướng này ĐÚNG" mà PFC không name
      → "Tiếng gọi", "passion" = body ĐÃ CÓ long-Imagine-Final

  VÔ THỨC LÀ PHẦN CHÍNH:
    → ~95% Imagine-Final hoạt động HOÀN TOÀN vô thức
    → Body liên tục: compare hiện tại vs expectation
    → Thiếu → body signal dissonance. Đủ → opioid.
    → PFC chỉ "biết" những Imagine-Final ĐỦ LỚN / đủ dissonance

  🟢 Predictive Processing: Clark 2013, Friston 2010
  🟡 "95% vô thức" = framework estimate, consistent with PP
```

### §2.2 — Tầng 2: PFC (EXTENSION)

```
⭐⭐ PFC = SERIAL PROCESSOR, REACTIVE (không proactive):

  ⚠️ Working memory ~4±1 dimensions (🟢 Cowan 2001)
  → 1 Imagine-Final actively refined tại 1 thời điểm
  → Others SAVED → reload khi cần (§4 Lifecycle)

  PFC KHÔNG TẠO RA Imagine-Final — PFC LÀM 3 VIỆC:

    ① CONSCIOUS HÓA: gọi tên Imagine-Final vô thức đã có
       → Body đã feel "muốn hướng này" → PFC: "à, tôi muốn làm X"
       → = PFC PHÁT HIỆN, không phải PFC TẠO

    ② SIMULATE DOMAIN: check Imagine-Final có đúng thực tế không
       → Body muốn X → PFC: "X có khả thi? Domain có cho phép?"
       → = PFC = THẨM ĐỊNH VIÊN duy nhất check domain accuracy
       → (Chunk.md §3: vô thức không check domain)

    ③ CHỌN THỰC THI: giữa competing Imagine-Finals
       → Body muốn ăn ngay (micro) vs body muốn khỏe (long-term)
       → PFC quyết: "chịu đói bây giờ VÌ sức khỏe dài hạn"
       → = WHY PFC yếu (mệt, say) → chọn ngắn hạn

  → = PFC QUAN TRỌNG — nhưng là EXTENSION, không phải SOURCE
  → = Không có PFC: vô thức VẪN có Imagine-Final (động vật CÓ)
  → = Có PFC: Imagine-Final được CHECK domain + CHỌN chiến lược

  🟢 Working memory: Cowan 2001
  🟢 PFC = executive selection: Miller & Cohen 2001
```

### §2.3 — Trigger model: Khi nào PFC bật

```
⭐ PFC KHÔNG TỰ KHỞI ĐỘNG → BODY GỌI PFC KHI CẦN:

  Body MET (expectation ≈ reality) → PFC KHÔNG engage:
    → "Autopilot" — vô thức chạy, PFC để yên

  Body UNMET (reality < expectation) → dissonance → PFC BẬT:
    → Đói → PFC: "đồ ăn ở đâu?" → scan + plan
    → Cô đơn → PFC: "gặp ai sẽ bớt?" → scan người
    → Chán việc → PFC: "có gì tốt hơn?" → scan options

  4 KẾT QUẢ KHI PFC SCAN:

    ① TÌM ĐƯỢC + KHẢ THI → hành động → hết dissonance
    ② TÌM ĐƯỢC + KHÔNG KHẢ THI → frustrated / stuck
    ③ TÌM SAI TARGET → thử mãi không hết (scroll phone, ăn vặt)
    ④ KHÔNG TÌM ĐƯỢC → "chán" dạng nặng (Imagine-Final DƯỚI ngưỡng PFC)

  CORTISOL GATES IMAGINE-FINAL ACTIVATION:

    Cortisol THẤP (thoải mái): Imagine-Final NGỦ — mọi thứ ổn, không cần compass
    Cortisol VỪA (daily life): Imagine-Final ACTIVE NHẸ — bridge daily dissonance
    Cortisol CAO (khủng hoảng): Imagine-Final CRITICAL — "tôi chịu VÌ CÁI NÀY"
      → CÓ Imagine-Final: "đau nhưng CÓ Ý NGHĨA" → chịu được
      → KHÔNG Imagine-Final: "đau VÀ VÔ NGHĨA" → sụp đổ

    → Cortisol-Baseline.md §3.7: cortisol GATES Imagine-Final activation level
    → Existential boredom = cortisol CAO + Imagine-Final KHÔNG CÓ
      = "đau VÀ vô nghĩa" — dạng nặng nhất (Boredom.md §6)

  🟡 Trigger model = framework synthesis
  🟢 Cortisol effects on cognition: Sapolsky 2004
```

### §2.4 — Imagine-Final → Anchor-Schema transition

```
⭐ KHI NÀO IMAGINE-FINAL CONTENT THÀNH SYNC POINT:

  Imagine-Final = CONTENT mà PFC build (file NÀY)
  Anchor-Schema = khi content đó ĐƯỢC CHỌN + COMMITTED (Anchor-Schema.md)

  TRANSITION:
    PFC build Imagine-Final → body-base ACCEPT (preview confirm) →
    Imagine-Final THÀNH Anchor-Schema → vô thức SYNC theo → actions EMERGE

  NHƯNG: Anchor-Schema KHÔNG CHỈ từ PFC Imagine-Final:
    → Compiled schemas đủ mạnh → TỰ thành Anchor ("tiếng gọi")
    → Hippocampus simulation → basic Anchor (động vật CÓ)
    → External inject (tôn giáo, xã hội) → compile → thành Anchor
    → = PFC Imagine-Final chỉ là 1 trong 4 NGUỒN fill anchor
    → Chi tiết: Anchor-Schema.md §3

  🟡 Transition model = framework synthesis
```

---

## §3 — PFC OPERATIONS × IMAGINE-FINAL

### §3.1 — Hold + Suppress applied to Imagine-Final

```
⭐⭐ PFC-Operations.md §2 APPLIED TO IMAGINE-FINAL:

  HOLD × IMAGINE-FINAL:
    → PFC sustain Imagine-Final trong working memory → refine, simulate, compare
    → Cost: ① PFC draft (metabolic — glucose consumption)
    → Mệt → PFC release → Imagine-Final drops (nếu chưa compiled)
    → Lặp đủ → Hebbian compile → Imagine-Final self-sustain → "calling"
    → VD: "Mỗi ngày nghĩ về project → dần compiled → tự fire"
    → = Hold trajectory: conscious → automatic → compiled passion

  SUPPRESS × IMAGINE-FINAL:
    → PFC block competing Imagine-Finals khi focus 1 Imagine-Final cụ thể
    → "Muốn chơi nhưng phải học" = suppress play-Imagine-Final, hold study-Imagine-Final
    → Cost: ② Efference mismatch ("tôi KHÔNG ĐANG LÀM cái tôi muốn")
    → PFC yếu → suppress FAIL → Imagine-Final bị chặn REBOUND
    → = WHY stress → "sudden urge" to do suppressed thing
    → VD: Diet → suppress food-Imagine-Final → stress → binge (rebound)

  CRITICAL DIFFERENCE:
    Hold → CAN compile → Imagine-Final becomes automatic (sustainable)
    Suppress → CANNOT compile "not wanting" → cost PERSISTS
    → Suppress alone = ALWAYS temporary (PFC budget finite)
    → = WHY "ép bản thân" without genuine interest = unsustainable

  🟢 Miller & Cohen 2001: PFC top-down amplification
  🟢 Anderson & Green 2001: Think/No-Think paradigm
  🟢 Wegner 1987: ironic process theory (suppress → rebound)
```

### §3.2 — Compiled/Fresh spectrum × Imagine-Final

```
⭐ IMAGINE-FINAL HOẠT ĐỘNG TRÊN COMPILED/FRESH SPECTRUM:

  COMPILED IMAGINE-FINAL (F1):
    → Body ĐÃ compile hướng này → tự fire → PFC không cần active
    → VD: "Tiếng gọi" — body BIẾT trước PFC label
    → Cost ≈ 0 (đã compiled → automatic)
    → Mạnh nhất: body + PFC + domain cùng confirm
    → = Level 4-5 trong Gradient (§5)

  FRESH IMAGINE-FINAL (F2):
    → PFC ACTIVELY construct new future scenario
    → Chunks mới + novel combination + domain check
    → VD: "Nếu tôi chuyển nghề thì sao?" (chưa experience)
    → Cost CAO (PFC draft required)
    → = Level 1-3 trong Gradient (§5)

  COMPILED QUALITY DIMENSION (PFC-Operations.md §5):
    Genuine-compiled Imagine-Final: body confirmed qua experience → STABLE, AUTHENTIC
      → "Tôi biết mình yêu nghề này vì ĐÃ LÀM 10 năm"
    Schema-compiled Imagine-Final: PFC-driven / xã hội install → FUNCTIONAL but HOLLOW
      → "Tôi phải giàu vì xã hội nói thành công = giàu"
    Threat-compiled Imagine-Final: bị ép / trauma → RIGID, AVOIDANCE-tagged
      → "Tôi phải giỏi vì sợ bị bỏ rơi"
    → CÙNG "compiled Imagine-Final" nhưng KHÁC tag → KHÁC body-feedback quality
    → = WHY "thành công mà trống rỗng" (schema-compiled, body không genuine)

  🟡 Compiled/Fresh applied to Imagine-Final = framework synthesis
  🟢 Compiled Quality: PFC-Operations.md §5 (7 factors)
```

### §3.3 — Architecture B × Imagine-Final

```
⭐ ARCHITECTURE B (Inter-Body-Mechanism.md §4):
  Body = PRODUCER (gaps generate drive).
  PFC = CONSUMER (check domain, select strategy).

  APPLIED TO IMAGINE-FINAL:
    Body = NGUỒN (gap → "body muốn hướng nào")
    PFC = KIỂM TRA (domain → "hướng này có thật không?")
    Domain = TRỌNG TÀI CUỐI CÙNG (results confirm or deny)

  IMAGINE-FINAL HOÀN CHỈNH = BODY × PFC × DOMAIN:
    Body muốn + domain KHÔNG confirm = ẢO TƯỞNG (delusion)
    Body KHÔNG muốn + domain confirm = ÉP BUỘC (external inject)
    Body muốn + domain confirm = HOÀN CHỈNH → passion, calling

  REFERENCE PATTERN — cơ chế cốt lõi:
    → PFC simulate: "nếu CÓ chunks NÀY → trạng thái sẽ THẾ NÀY"
    → Body PRE-FEEL: "trạng thái đó CÓ VẺ mượt hơn hiện tại?"
    → Nếu body: "CÓ VẺ mượt hơn" → preview opioid → "MUỐN"
    → Mỗi chunk mới PHẢN XẠ với reference pattern:
      Phù hợp → "đúng hướng!" → chịu dissonance
      Không phù hợp → "vô nghĩa" → irritated

  PFC COST-BENEFIT LIÊN TỤC:
    → Mỗi moment: "dissonance HIỆN TẠI vs delta tiềm năng?"
    → Imagine-Final RÕ = delta lớn = PFC "xứng" = chịu LÂU hơn
    → Imagine-Final MỜ = delta nhỏ = PFC "không xứng" = bỏ sớm

  ⚠️ PREVIEW OPIOID ≠ ACTUAL OPIOID:
    → Preview = body "thử feel" → YẾU, có thể sai
      = Wanting mechanism ① (Liking-Wanting.md §2.1)
    → Actual = kết quả THẬT → cần H10 5 preconditions
      (Dopamine-Is-Not-Reward.md §4)
    → Preview fidelity phụ thuộc chunk quality + Trust vào Imagine-Final

  🟢 Somatic Marker Hypothesis: Damasio 1994
  🟢 Berridge: wanting ≠ liking distinction
  🟡 Architecture B applied to Imagine-Final = framework synthesis
```

---

## §4 — LIFECYCLE: 5 PHASES

### §4.1 — 3 Foundations

```
⭐ 3 NỀN TẢNG TRƯỚC KHI VÀO 5 PHASES:

  NỀN TẢNG 1 — PFC LÀ SERIAL PROCESSOR:
    → Working memory ~4±1 dimensions (🟢 Cowan 2001)
    → 1 ACTIVE focus tại 1 thời điểm
    → Chỉ 1 Imagine-Final được PFC ACTIVELY refine tại 1 lúc
    → Others SAVED → reload khi cần

  NỀN TẢNG 2 — DRAFT vs RESULT:
    DRAFT (process): PFC simulate options, build, modify, discard
      → Vô hạn cách, cá nhân hóa — framework KHÔNG phân tích
    IMAGINE-FINAL (result): "best draft so far" tại thời điểm hiện tại
      → Cái body PRE-FEEL preview = SẢN PHẨM của draft
    → Framework focus vào RESULT, không phải process

  NỀN TẢNG 3 — MULTIPLE IMAGINE-FINALS TRONG STORAGE:
    1 người KHÔNG chỉ có 1 Imagine-Final:
      Career / Health / Relationship / Hobby / Daily / Micro / ...
    TẠI 1 THỜI ĐIỂM: chỉ 1 ACTIVE trong PFC workspace
    Others = SAVED, dormant → body trigger reload khi dissonance fire

  🟢 Working memory: Cowan 2001
  🟡 Draft vs Result distinction = framework synthesis
```

### §4.2 — 5 Phases

```
⭐⭐ 5 PHASES CỦA IMAGINE-FINAL LIFECYCLE:

  PHASE 1 — BUILD (PFC active, draft + simulate):
    Trigger: body dissonance → PFC engaged
    → Pull related chunks → simulate possible futures
    → Body PRE-FEEL mỗi simulation → PFC compare → select "best so far"
    → Chunks available quyết định what futures imaginable
    → Chunks compiled under threat cortisol → avoidance scenarios
    → Duration: giây → giờ (PFC bandwidth có hạn)
    → VD: Đói → PFC scan → "phở vs cơm" → body preview → "phở" → act

  PHASE 2 — SAVE (PFC switches away):
    Trigger: PFC bandwidth cần cho task khác
    → Imagine-Final move from workspace → memory storage
    → Hippocampus encode → "proto-schema state" (dormant, not lost)
    → SAVE ≠ FORGET. SAVE = inactive but intact.
    → KHÁC Anchor-Schema: Anchor = compiled deep, persistent ACTIVE.
      Saved Imagine-Final = proto-schema, dormant, cần PFC reload.

  PHASE 3 — BACKGROUND PROCESSING (vô thức, PFC busy):
    ⭐ PHASE QUAN TRỌNG NHẤT mà ít người ý thức.
    Khi PFC focus task khác → vô thức KHÔNG dừng:
      ① Sleep consolidation (🟢 Tononi & Cirelli): REM = hippocampus → cortex
      ② Spreading activation (🟢): semantic priming → auto re-organize
      ③ DMN processing (🟢 Raichle 2001, Buckner 2008): background "thinking"
      ④ Body trigger random (🟡): đi tắm → DMN dominant → eureka
    → Khi PFC reload → Imagine-Final có thể SHIFT (context mới)
    → "Đã thay đổi mà không biết" = background processing, not PFC edit
    → Duration: phút → ngày → tuần

  PHASE 4 — RELOAD (PFC pulls back):
    Trigger: dissonance / decision needed / external event / DMN resurface
    → PFC pull Imagine-Final từ storage + chunks mới đã integrate
    → 3 OUTCOMES:
      A. UNCHANGED: không chunks mới significant → act hoặc save lại
      B. CLEARER: background tích hợp → vision sharper → level tăng
      C. SHIFTED: insights mới → realize hướng cũ không đúng → pivot
    → "Aha moment" thường ở RELOAD, không phải khi PFC cố nghĩ

  PHASE 5 — REFINE → LOOP VỀ PHASE 1:
    → PFC re-build Imagine-Final với new context → thực tế là BUILD tiếp
    → Loop tiếp tục cho đến 1 trong 3 outcomes dài hạn

  🟢 REM consolidation: Walker 2017
  🟢 DMN: Raichle 2001, Buckner 2008
  🟡 5-phase lifecycle model = framework synthesis
```

### §4.3 — 3 Long-term outcomes

```
⭐ SAU NHIỀU CYCLES:

  OUTCOME 1 — COMPILE (long-term success):
    → Nhiều cycles → Imagine-Final có structure stable + body confirm + results
    → Compile dần thành SCHEMA → tự fire → thành ANCHOR-SCHEMA
    → VD: Jensen Huang — ~30 năm cycles → genuine compiled Imagine-Final

  OUTCOME 2 — ACHIEVE & FORGET (short-term success):
    → Imagine-Final hoàn thành nhanh (micro/short scale)
    → Chunks chi tiết FORGET, chỉ giữ kinh nghiệm
    → VD: giải bài toán → quên cách, nhớ method

  OUTCOME 3 — ABANDON (failure or replace):
    → Domain feedback ✗ → trust giảm → bỏ
    → Hoặc Imagine-Final mới hấp dẫn hơn → replace
    → Imagine-Final cũ stay trong storage nhưng không reload → decay

  KEY INSIGHTS:
    → "Cố nghĩ" thường KÉM HƠN "để tự thấm" (block Phase 3)
    → "Ngủ một đêm" = mechanism NORMAL (REM consolidation)
    → Imagine-Final "thay đổi" ≠ PFC edit — phần lớn shift ở Phase 3
    → Focus deep > switching (PFC serial + switching cost)
```

---

## §5 — GRADIENT: 5 LEVELS

### §5.1 — 5 Levels of body simulation fidelity

```
⭐⭐ MỌI TỪ chỉ "mục tiêu" = CÙNG CƠ CHẾ, KHÁC body fidelity:

  ╔═══════════════════════════════════════════════════════════════════╗
  ║  LEVEL 5 — BODY FIRE NHƯ THẬT (80-100% fidelity)               ║
  ║                                                                   ║
  ║  Obsession (~95-100%): "KHÔNG THỂ ngừng nghĩ" — fire 24/7       ║
  ║    Body treat Imagine-Final as real. MẠNH NHẤT + NGUY HIỂM NHẤT.           ║
  ║    VD: Einstein + vật lý. ⚠️ Sai hướng = self-destruction.      ║
  ║                                                                   ║
  ║  Calling (~80-95%): "Bị KÉO về phía này — không phải tôi chọn" ║
  ║    Hardware + body-base MATCH → gần như tự chạy.                 ║
  ║    = Compiled genuine Imagine-Final. Cost ≈ 0.                              ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║  LEVEL 4 — BODY SIMULATE THƯỜNG XUYÊN (60-80% fidelity)        ║
  ║                                                                   ║
  ║  Vision (~65-80%): "THẤY tương lai — hình ảnh, âm thanh"        ║
  ║    PFC multi-modal: visual + emotional + context. Strong preview.║
  ║                                                                   ║
  ║  Mission (~60-70%): "PHẢI hoàn thành — lớn hơn cá nhân"         ║
  ║    Purpose + action plan CỤ THỂ → body: urgency + meaning.      ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║  LEVEL 3 — BODY FEEL RÕ, CÓ HƯỚNG (40-60% fidelity)           ║
  ║                                                                   ║
  ║  Purpose (~50-60%): "ĐÂY là lý do tôi làm MỌI THỨ"            ║
  ║    Per-life compass. Body feel alignment.                        ║
  ║                                                                   ║
  ║  Ambition (~40-50%): "QUYẾT TÂM đạt được — chịu khó"           ║
  ║    Body feel drive + direction rõ + sẵn sàng chịu dissonance.   ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║  LEVEL 2 — BODY BẮT ĐẦU FEEL, CHƯA RÕ (20-40% fidelity)      ║
  ║                                                                   ║
  ║  Goal (~30-40%): "SẼ đạt X trước Y" — biết SỐ, chưa feel SỐNG ║
  ║    ⚠️ Level phổ biến nhất khi "đặt mục tiêu".                   ║
  ║    "Viết mục tiêu" ≠ "SỐNG trong mục tiêu."                    ║
  ║                                                                   ║
  ║  Interest (~20-30%): "Thú vị — muốn tìm hiểu thêm"            ║
  ║    Curiosity fire → explore → chưa commit.                      ║
  ╠═══════════════════════════════════════════════════════════════════╣
  ║  LEVEL 1 — PFC BIẾT, BODY KHÔNG FEEL (0-20% fidelity)          ║
  ║                                                                   ║
  ║  Dream (~10-20%): "Mơ ước một ngày nào đó..."                   ║
  ║    PFC imagine → body feel nhẹ → KHÔNG action plan.             ║
  ║                                                                   ║
  ║  Wish (~0-10%): "Giá mà..." → nghĩ 3 giây → quên.             ║
  ║                                                                   ║
  ║  NONE (0%): "Không biết muốn gì" → melody trôi.                ║
  ╚═══════════════════════════════════════════════════════════════════╝

  ⚠️ CÙNG 1 NGƯỜI có thể ở NHIỀU LEVEL cho NHIỀU THỨ:
    Career: Level 4 (vision rõ). Health: Level 1 (wish).
    = Imagine-Final KHÔNG phải 1 con số — là MAP nhiều domain.

  🟢 Goal-setting → higher performance: Locke & Latham 1990
  🟢 Mental simulation = same pathways: Jeannerod 1995, Kosslyn 1994
  🟢 Intrinsic > extrinsic: Deci & Ryan 2000
  🔴 Body simulation fidelity % = metaphor, chưa có measurement protocol
```

### §5.2 — Level-up mechanism

```
⭐ CÁCH NÂNG LEVEL:

  ❌ KHÔNG phải "nghĩ nhiều hơn" (PFC alone không tăng fidelity)
  ✅ MÀ LÀ "experience nhiều hơn" (body CẦN chunks thật để simulate rõ)

  Wish → Dream: thêm THỜI GIAN nghĩ (từ 3 giây → 10 phút hình dung)
  Dream → Interest: thêm BODY EXPERIENCE (đi xem, đi thử, đi cảm nhận)
  Interest → Goal: thêm CỤ THỂ + DEADLINE
  Goal → Ambition: thêm COMMITMENT + mini-arcs → momentum
  Ambition → Purpose: thêm MEANING (kết nối body-base THẬT)
  Purpose → Vision: thêm MULTI-MODAL simulation (thấy, nghe, cảm nhận)
  Vision → Calling: KHÔNG THỂ "tạo" — chỉ NHẬN RA (hardware match)

  = "Nâng Imagine-Final = NẠP CHUNKS THẬT" — không phải "nghĩ tích cực hơn"
  = WHY motivational speaker KHÔNG giúp lâu dài
    (PFC inspiration Level 1-2 → body KHÔNG CÓ chunks → 3 ngày quên)
  = WHY "đi thực tập" MẠNH HƠN "đọc sách ngành"
    (body experience → chunks THẬT → simulate RÕ → Imagine-Final TĂNG)

  🟢 Expertise = experience-based: Ericsson 1993
  🟡 Level-up by chunk accumulation = framework synthesis
  🟡 Motivational speaker effect short-term: Latham & Pinder 2005
```

### §5.3 — Bootstrap mechanism

```
⭐ IMAGINE-FINAL CÓ THỂ TỰ NÂNG CẤP ("fake it till you make it"):

  Bước 1: PFC TẠO Imagine-Final (chưa body confirm) → Level 2-3
  Bước 2: ACT theo Imagine-Final → kết quả NHỎ → body: "có vẻ đúng" → Level 3
  Bước 3: Kết quả TĂNG → body compile → Imagine-Final MẠNH hơn → Level 4
  Bước 4: Kết quả ĐỦ → body THẬT SỰ tin → Imagine-Final genuine → Level 4-5

  → Bootstrap WORK khi: direction ĐÚNG + results ĐẾN
  → Bootstrap FAIL khi: direction SAI + results KHÔNG → delusion
  → Real-check phân biệt bootstrap vs delusion

  VD Jensen Huang (bootstrap ~30 năm):
    Body-need (①): significance + mastery + impact
    Imagine-Final (②): "NVIDIA thành reference computing"
    Plan parameter (③): "GPU sẽ quan trọng"
    ~1993: PFC tạo Imagine-Final chiến lược (body chưa chắc)
    ~2000s: GPU gaming thành công → body confirm → Imagine-Final tăng
    ~2012: GPU cho deep learning → bất ngờ → genuine reward → jump
    ~2023: AI boom → Imagine-Final 100% genuine (body + PFC + market confirm)

  🟡 Bootstrap model = framework synthesis
  🟢 Self-efficacy → performance → self-efficacy loop: Bandura 1997
```

---

## §6 — 3 CHIỀU ĐỘC LẬP: CLARITY × QUALITY × TRUST

```
⭐⭐ 3 CHIỀU ĐÁNH GIÁ IMAGINE-FINAL — ĐỘC LẬP VỚI NHAU:

  CHIỀU 1 — CLARITY (file NÀY):
    "Imagine-Final RÕ đến đâu?" (5 levels, §5)
    = Body simulation fidelity — state variable thay đổi khi build chunks

  CHIỀU 2 — QUALITY (Imagine-Final-Evaluation.md):
    "Hướng đi TỐT hay XẤU?"
    = 2 trục: Domain Fit (có thật?) × Hardware Fit (mình đi được + muốn?)
    = 4 góc: Sweet Spot / Mismatch / Delusion / Fantasy

  CHIỀU 3 — TRUST (Anchor-Schema.md §2):
    "COMMIT bao nhiêu?"
    = Mức độ hệ thống BIND vào Anchor-Schema qua dissonance
    = Phổ: 0 (không bind) → ∞ (unfalsifiable faith)

  INTERACTION PATTERNS:

  ┌────────────────────────┬────────────────────────────────────────┐
  │ Combination            │ Result                                  │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Clarity↑ Quality↑      │ MẠNH NHẤT — productive passion         │
  │ Trust↑                 │ (Jensen Huang)                          │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Clarity↑ Quality↑      │ "Biết nhưng không dám"                 │
  │ Trust↓                 │ = CẦN build trust qua small wins       │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Clarity↓ Trust↑        │ Faith ("tin dù chưa thấy rõ")         │
  │                        │ = Tôn giáo, ideology                   │
  ├────────────────────────┼────────────────────────────────────────┤
  │ Clarity↑ Quality↓      │ NGUY HIỂM NHẤT — delusion locked       │
  │ Trust↑                 │ = Drive mạnh + sai hướng + không sửa  │
  ├────────────────────────┼────────────────────────────────────────┤
  │ All LOW                │ "Trôi không đích" — no compass          │
  └────────────────────────┴────────────────────────────────────────┘

  → Clarity CAO + Quality TỐT = SWEET SPOT (productive)
  → Clarity CAO + Quality XẤU = NGUY HIỂM NHẤT
    (Obsession sai hướng > Wish đúng hướng)
  → = "Nâng clarity" KHÔNG ĐỦ — cần CHECK quality cùng lúc

  🟡 3D framework (Clarity × Quality × Trust) = framework synthesis
```

---

## §7 — ENTITY-ACCESS × IMAGINE-FINAL

### §7.1 — Per-entity Imagine-Final

```
⭐ IMAGINE-FINAL KHÔNG CHỈ CHO DOMAIN/CAREER — CÓ CHO MỖI ENTITY:

  Mỗi entity trong Entity-Access gradient (Entity-Access.md §2) →
  brain có IMAGINE-FINAL RIÊNG cho relationship đó:

  Mức 0 (stranger): Imagine-Final không có (no prediction needed)
  Mức 1-2 (unlabeled): Imagine-Final mờ ("hope gặp lại" / "hope vui")
  Mức 3 (B-dominant): Imagine-Final rõ ("bạn thân → cùng chia sẻ lâu dài")
  Mức 4-5 (Entity-Owned): Imagine-Final deep ("con → thrive" / "partner → cùng già")

  SCHEMA-DRIVEN vs GENUINE:
    Schema Imagine-Final: "con PHẢI giỏi vì xã hội nói thành công = điểm cao"
      → PFC-installed, body không genuine → Entity-Access §4 Gap Source C
    Genuine Imagine-Final: "con THRIVE theo cách CỦA CON"
      → Body-confirmed, authentic → Gap Source A+B

  → Compiled Quality Dimension (PFC-Operations §5) APPLIES:
    Genuine-compiled Imagine-Final for child → healthy parenting
    Schema-compiled Imagine-Final for child → tiger parent (functional but hollow)
    Threat-compiled Imagine-Final for child → overprotective (fear-based)

  🟡 Per-entity Imagine-Final dynamics = framework synthesis
```

### §7.2 — Social scale: Imagine-Final alignment = relationship depth

```
⭐ 2 NGƯỜI "HỢP NHAU" = body detect CÙNG Imagine-Final ở scale nào đó:

  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Scale            │ Quan hệ                                      │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Micro Imagine-Final         │ Xã giao (phút→giờ): cả 2 preview "dễ chịu" │
  │ Normal Imagine-Final        │ Bạn thân (tháng→năm): share hướng sống      │
  │ Big Imagine-Final           │ Co-founder (năm→thập kỷ): share mission     │
  │ Life Imagine-Final          │ "Tri kỷ" (cả đời): cùng life direction      │
  └──────────────────┴──────────────────────────────────────────────┘

  KHÁC MELODY, CÙNG Imagine-Final = VẪN HỢP (thậm chí BỔ SUNG):
    → 1 code, 1 design → CÙNG "sản phẩm đẹp" → complement
    → Diverse teams: khác pattern + cùng Imagine-Final = stronger
    → By-Product-Gap-Resonance.md: resonance = mutual agent-mode + gap overlap

  Imagine-Final ALIGNMENT THAY ĐỔI GIẢI THÍCH QUAN HỆ THAY ĐỔI:
    → Bạn thân drift apart: Imagine-Final dần LỆCH → body feel "xa"
    → Đồng nghiệp bỗng thân: shared project → Imagine-Final aligned → "gần"
    → Vợ chồng "hết yêu": Imagine-Final diverge từ từ

  BODY DETECT Imagine-Final COMPATIBILITY VÔ THỨC:
    → "Cảm giác click" = body detect Imagine-Final aligned TRƯỚC PFC biết
    → PFC rationalize SAU: "vì cùng sở thích"
    → Gốc: 2 body preview CÙNG HƯỚNG → oxytocin → "thích"

  🟡 Imagine-Final alignment = relationship depth = framework synthesis
  🟢 Self-expansion: Aron & Aron 1986 (shared activities → closeness)
```

### §7.3 — Shared Imagine-Final = collaborate. Lệch + scarce = conflict.

```
⭐ IMAGINE-FINAL LÀ BIẾN QUYẾT ĐỊNH:

  CÙNG Imagine-Final + KHÁC melody = BỔ SUNG (mạnh nhất):
    VD: vợ chồng nuôi con — chồng logic (dạy tư duy) + vợ cảm xúc (chăm khỏe)
    → 2 melody KHÁC → 2 Imagine-Final CÙNG: "con thrive"
    → Kết quả VƯỢT mong đợi — tổng > từng phần

  XUNG ĐỘT CHỈ KHI:
    ① Imagine-Final THẬT SỰ LỆCH (khác ĐÍCH, không chỉ khác ĐƯỜNG):
      Chồng: "con PHẢI giỏi" vs Vợ: "con PHẢI vui"
      → CÓ THỂ "tưởng lệch mà không" (reframe = resolve)
    ② CÙNG Imagine-Final + RESOURCE SCARCE:
      Cùng "kiếm tiền" nhưng lợi nhuận FINITE → tranh giành
      (Conflict-Dynamics.md §1: Overlap × Scarcity × Commitment)

  TÓM TẮT:
    Cùng Imagine-Final + đủ resource = collaborate (win-win)
    Cùng Imagine-Final + thiếu resource = compete (zero-sum)
    Khác Imagine-Final = không liên quan (peace)
    Lệch Imagine-Final + cùng domain = conflict

  🟡 Imagine-Final as relationship predictor = framework synthesis
```

---

## §8 — ENGINE USE QUALITY: REFLECTION vs RUMINATION

```
⭐⭐ CÙNG ENGINE, CÙNG APPLICATION, KHÁC CHẤT LƯỢNG SỬ DỤNG:

  Imagine-Final with REFLECTION (curiosity drive):
    → "Tương lai sẽ thú vị" → EXPLORE options
    → Cortisol direction: NOVELTY → approach tag
    → Body-Feedback-Mechanism §3.3c: gap + novelty → productive
    → Output: creative planning, risk assessment, scenario comparison
    → = ENGINE USE QUALITY: HIGH

  Imagine-Final with RUMINATION (threat drive):
    → "Tương lai sẽ tệ" → CATASTROPHIZE
    → Cortisol direction: THREAT → avoidance tag
    → BFM §3.3c: gap + threat → anxiety loop
    → Output: worry, worst-case fixation, decision paralysis
    → = ENGINE USE QUALITY: LOW

  CÙNG MECHANISM:
    Engine chạy simulation → body-feedback → PFC observe
    KHÁC CORTISOL CONTEXT → KHÁC OUTPUT:
      Reflection: "nếu tôi thử X → gì sẽ xảy ra?" (open exploration)
      Rumination: "nếu X xảy ra → tôi sẽ chết" (closed catastrophe)
    → = Compiled-Fresh §6.2: compile-time direction lock

  UNIVERSAL MODIFIER:
    Reflection/Rumination KHÔNG chỉ ảnh hưởng Imagine-Final:
    → SPM with curiosity: "tại sao bạn nghĩ vậy?" → LEARN
    → SPM with threat: "bạn chắc ghét tôi" → PROJECT fear
    → Self-Obs with curiosity: "tại sao tôi feel vậy?" → insight
    → Self-Obs with threat: "tôi chắc sai rồi" → stuck
    → = Engine use quality = modifier cho TẤT CẢ applications
    → (Simulation-Engine.md §9)

  SELF-ASSESSMENT:
    "Mình có ảo không nhỉ?" = REFLECTION (curiosity, explore) → productive
    "Mình chắc chắn ảo" = RUMINATION (threat, stuck) → destructive
    → = Test: BẠN CÓ KIỂM TRA formulations không? → reflection
    → = Nếu chỉ lo mà không test → rumination

  🟢 Trapnell & Campbell 1999: self-reflection vs self-rumination
  🟢 Joireman et al. 2002: reflection → empathy, rumination → anxiety
  🟡 Engine use quality as universal modifier = framework synthesis
```

---

## §9 — HẬU QUẢ + NÂNG CẤP

### §9.1 — Hậu quả sai level

```
⭐ MỖI LEVEL CÓ RỦI RO RIÊNG:

  LEVEL 1-2 QUÁ LÂU — "Mãi mơ mà không làm":
    → Body enjoy IMAGINE (preview opioid) mà không chịu DISSONANCE
    → = "Mơ mộng viển vông" = body lấy reward từ imagine, not action
    → Fix: ép bản thân TRẢI NGHIỆM thật → nâng level

  LEVEL 2-3 + SAI HƯỚNG — "Chạy nhanh sai đường":
    → Goal/Ambition RÕ + MẠNH → nhưng hướng SAI (xã hội chọn)
    → Đạt được → body KHÔNG harmony → "thành công mà trống rỗng"
    → = Schema-compiled Imagine-Final: PFC-driven, body không genuine
    → Fix: real-check body: "body TÔI có reward? hay chỉ PFC?"

  LEVEL 4 + KHÔNG REAL-CHECK — "Tầm nhìn mù":
    → Vision MẠNH → body treat Imagine-Final as real → dismiss feedback
    → "Thế giới sai, tôi đúng" → nhiều năm sai hướng
    → Fix: mandatory real-check intervals (domain = arbiter)

  LEVEL 5 + KHÔNG BODY-BASE MAINTENANCE — "Cháy sáng rồi tắt":
    → Obsession → hy sinh sleep, food, connection → cortisol stack → crash
    → Fix: body-base maintenance = NON-NEGOTIABLE dù obsession nói "không cần"

  LEVEL 0 + LÂU — "Trôi không đích":
    → Không Imagine-Final → sống bằng social bridge → quarter/midlife crisis
    → Fix: thử NHIỀU domain → body cho biết cái nào reward → build từ đó

  → §9 đo hậu quả theo CLARITY LEVEL
  → Imagine-Final-Evaluation.md đo hậu quả theo QUALITY (4 góc)
  → 2 chiều BỔ SUNG nhau
```

### §9.2 — Training: improve engine → improve Imagine-Final

```
⭐ VÌ SHARED SUBSTRATE → training 1 component = improve ALL:

  INTEROCEPTION TRAINING (Component 1 — highest leverage):
    → Meditation, body-scan, Focusing (Gendlin 1978)
    → Better body-readout → more vivid future preview
    → = Nâng fidelity của Imagine-Final từ bên trong
    → 🟢 Fukushima 2011: interoceptive accuracy → empathic accuracy

  DIVERSITY TRAINING (Component 3):
    → Interact with dissimilar others → activate dMPFC
    → Reveal own biases → sharper self-model
    → Sharper self-model → more accurate future self-simulation
    → 🟢 Mitchell 2006: vMPFC/dMPFC dissociation

  REFLECTION PRACTICE (Engine use quality):
    → Replace "tôi sẽ fail" with "nếu tôi thử thì sao?"
    → = Switch cortisol direction: threat → novelty
    → 🟢 Trapnell & Campbell 1999

  SOCIAL PRACTICE (Bidirectional loop):
    → Quality interactions → engine PRACTICE → substrate improved
    → Improved substrate → better at ALL applications including Imagine-Final
    → 🟢 Lopes et al. 2003, Coan & Sbarra 2015

  EXPERIENCE ACCUMULATION (Level-up specific):
    → ĐI THỬ, ĐI XEM, ĐI CẢM NHẬN → body CÓ chunks thật
    → Chunks thật → simulate rõ → Imagine-Final level tăng
    → Body awareness training > cognitive-only instruction
    → 🟢 Ericsson 1993: expertise = deliberate practice
```

---

## §10 — IMAGINE-FINAL × BROADER FRAMEWORK

```
⭐ IMAGINE-FINAL × CÁC CƠ CHẾ KHÁC:

  Imagine-Final × BOREDOM (Boredom.md):
    → L1 đói + KHÔNG CÓ Imagine-Final → PFC không biết fix gì → "chán"
    → L1 đói + CÓ Imagine-Final rõ → "investment cost" (khó nhưng xứng đáng)
    → Imagine-Final biến "chán vô hướng" thành "đầu tư có mục đích"
    → Existential boredom = cortisol CAO + Imagine-Final KHÔNG CÓ

  Imagine-Final × MEANING (Meaning.md):
    → Meaning = life-level Anchor-Schema (Meaning.md §1)
    → Imagine-Final cho domain/career + Imagine-Final cho relationships + Imagine-Final cho values
    → Khi compiled vào coherent direction → = "meaning"
    → Meaning mất = Anchor-Schema sụp → Imagine-Final landscape collapse

  Imagine-Final × EDUCATION:
    → Bố mẹ inject Imagine-Final cho con:
      Tốt: "Con thử hình dung khi biết bơi..." (giúp con BUILD Imagine-Final riêng)
      Xấu: "Con PHẢI làm bác sĩ" (inject Imagine-Final CỦA BỐ MẸ)
    → Mentor GIÚP thấy đích rõ hơn (not inject đích CỦA MÌNH)
    → Education: exposure + experience > injection
    → (Education-Mechanism.md, Empathy-Education.md)

  Imagine-Final × AI ERA:
    → AI boost Level 1-3: cung cấp chunks verbal/visual
    → AI CÓ THỂ giúp simulate cụ thể: "nếu bạn đạt X → cuộc sống sẽ..."
    → AI KHÔNG THỂ cho body experience thật → Level 4-5 CẦN body tự nạp
    → Ask-AI.md §6: body = quality controller, domain = final arbiter
    → AI = tool cho ③ (plan), human essential cho ②① (Imagine-Final + need)

  Imagine-Final × CULTURAL PATTERNS:
    → "Dream big" (Mỹ) = push toward Level 3-4
    → "Gaman" chịu đựng (Nhật) = Level 3 nhưng khác flavor
    → "Ai cũng thế" (VN collectivist) = pull toward Level 0-1
    → Cultural Imagine-Final ≠ personal Imagine-Final — collision → identity crisis
    → (Social-Calibration.md §3.4, Entity-Access §10)

  Imagine-Final × FRACTAL PATTERN:
    → Cá nhân: Imagine-Final mờ → dissonance → thử → verify → sharper
    → Nhân loại: "triết học" mờ → tranh cãi → thử → verify → khoa học
    → = Cùng cơ chế, khác scale
    → (Discovery-vs-Expansion.md §2)
```

---

## §11 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED
═══════════════════════════════════════

  Goal-setting → higher performance:          Locke & Latham 1990
  Mental simulation = same neural pathways:   Jeannerod 1995, Kosslyn 1994
  Prospection (humans simulate future):       Seligman et al. 2013, Gilbert 2006
  Somatic Marker Hypothesis:                  Damasio 1994
  Self-Determination Theory (intrinsic>ext):  Deci & Ryan 2000
  Constructive episodic simulation:           Schacter & Addis 2007
  Shared self/other circuits:                 Lombardo 2010 (fMRI)
  vMPFC/dMPFC dissociation:                   Mitchell 2006 (Neuron)
  Anterior insula shared readout:             Bird & Silani 2010
  Alexithymia = broken readout:               Bird & Cook 2013
  Interoceptive accuracy → empathic accuracy: Fukushima 2011
  DMN as simulation engine:                   Buckner et al. 2008
  Self-projection:                            Buckner & Carroll 2007
  Self-reflection vs self-rumination:         Trapnell & Campbell 1999
  Reflection → empathy:                       Joireman et al. 2002
  REM consolidation:                          Walker 2017, Tononi & Cirelli
  PFC top-down amplification:                 Miller & Cohen 2001
  Working memory capacity:                    Cowan 2001
  Social Baseline Theory:                     Coan & Sbarra 2015
  Hippocampal constructive simulation:        Hassabis et al. 2007
  Expertise = deliberate practice:            Ericsson 1993
  Wanting ≠ Liking:                           Berridge 2003
  Self-efficacy spiral:                       Bandura 1997

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS
═══════════════════════════════════════

  "Application on Simulation Engine" model: coordinates trong 3D space
  3-Layer Hierarchy: Body-Need → Imagine-Final → Plan
  "Reference pattern body pre-feel": consistent with Somatic Marker
  "Most PFC-accessible application": logical from PFC involvement spectrum
  Lifecycle 5 phases: BUILD → SAVE → BACKGROUND → RELOAD → REFINE
  Gradient 5 levels: Wish → Obsession (body fidelity spectrum)
  3 chiều độc lập: Clarity × Quality × Trust
  Level-up = nạp chunks thật (consistent with expertise research)
  Bootstrap: PFC → action → results → genuine (consistent with Bandura)
  Per-entity Imagine-Final dynamics
  Imagine-Final alignment = relationship depth predictor
  Engine use quality as universal modifier (Reflection vs Rumination)
  Cortisol gates Imagine-Final activation level
  Dormant when harmony, fire when dissonance
  Bidirectional social ↔ self improvement spiral
  Architecture B applied: Body=producer, PFC=consumer, Domain=arbiter

═══════════════════════════════════════
🔴 HYPOTHESIS
═══════════════════════════════════════

  Body simulation fidelity CÓ THỂ đo bằng % — hiện tại = metaphor
  5 levels là COMPLETE list — có thể overlap hoặc missing sub-types
  Gradient là LINEAR — có thể có jumps, branches, non-linear paths
  NONE (0%) có tồn tại thật? — hay LUÔN có ít nhất Wish-level?
  AI boost Level 1-3 only — empirical test chưa có
  "Motivational speaker short-term only" — limited meta-analysis
  Social scale (Micro→Life Imagine-Final) = framework categorization, not measured
```

---

## §12 — CROSS-REFERENCES

| File | Sections | Relationship |
|------|----------|-------------|
| Simulation-Engine.md v1.0 | Full file | ENGINE: 3 components, 3 axes, shared substrate |
| PFC-Operations.md v1.0 | §2 Hold/Suppress, §5 Quality, §6 7-Factors | HOW PFC operates on Imagine-Final |
| Entity-Access.md v1.0 | §2 Gradient, §4 Gap Source, §5 Per-entity | Per-entity Imagine-Final dynamics |
| Entity-Compiled.md v1.0 | §3 Formation, §7 Grief, §8 Love↔Hate | Entity compilation × Imagine-Final |
| Self-Pattern-Match.md v3.0 | §2 F1/F2, §10 SPM×Imagine-Final overlap | SIBLING APPLICATION on engine |
| Feeling.md v3.0 | PFC observation interface | SIBLING APPLICATION on engine |
| Anchor-Schema.md v1.0 | §2 Trust, §3 4-nguồn fill | Imagine-Final → Anchor-Schema transition |
| Imagine-Final-Evaluation.md v1.1 | 2 trục × 4 góc, Quality dimension | COMPANION: quality check |
| Body-Feedback-Mechanism.md v2.0 | §3 chunk dynamics, §3.3c gap creation | Foundation: body-feedback readout |
| Body-Input-Enumeration.md v2.0 | L0/L1/L3 taxonomy | Body-need layer (3-Layer Hierarchy ①) |
| Cortisol-Baseline.md v2.1 | §3.7 gates, §3.3 direction tag | Cortisol modulates Imagine-Final activation |
| Boredom.md v1.1 | §3 Imagine-Final modifier, §6 existential | No Imagine-Final = "chán" |
| Meaning.md v2.0 | §1 life-level Anchor-Schema | Meaning = compiled Imagine-Final landscape |
| Connection.md v4.0 | §3 3-primitives, §7 Imagine-Final per layer | Social context |
| Liking-Wanting.md v1.0 | §2.1 wanting mechanism ① | Preview opioid = wanting mechanism |
| Dopamine-Is-Not-Reward.md v1.0 | §4 7-step, H10 | Preview vs actual reward |
| By-Product-Gap-Resonance.md v1.0 | 4 conditions, resonance decline | Resonance × Imagine-Final alignment |
| Love-Romantic.md v2.2 | §1 body evaluate first, §7 Type A/B | Relationship Imagine-Final dynamics |
| Education-Mechanism.md v2.0 | Exposure, per-age guide | Imagine-Final injection vs facilitation |
| Ask-AI.md v3.1 | §6 Dual Check | AI × Imagine-Final interaction |
| Background-Pattern.md v1.1 | §2 2D model, §8 self-reinforcing | Background × Imagine-Final compile |
| Somatic-Articulation-Loop.md v1.0 | Body-knowledge → explicit | Complement: body knows → PFC labels |

---

## §13 — RESEARCH CITATIONS

| # | Citation | Used in | Evidence |
|---|----------|---------|----------|
| R1 | Schacter & Addis 2007 — Constructive Episodic Simulation (Nature Rev Neuroscience) | §0, §1, §4 | 🟢 |
| R2 | Seligman, Railton, Baumeister & Sripada 2013 — Navigating the future | §0 | 🟢 |
| R3 | Gilbert & Wilson 2007 — Prospection: experiencing the future | §0 | 🟢 |
| R4 | Damasio 1994 — Somatic Marker Hypothesis | §0, §3 | 🟢 |
| R5 | Locke & Latham 1990 — Goal-setting theory | §0, §5 | 🟢 |
| R6 | Deci & Ryan 2000 — Self-Determination Theory | §0, §5 | 🟢 |
| R7 | Buckner & Carroll 2007 — Self-projection and the brain | §1 | 🟢 |
| R8 | Buckner, Andrews-Hanna & Schacter 2008 — DMN anatomy (Annals NYAS) | §1, §4 | 🟢 |
| R9 | Bird & Silani et al. 2010 — Anterior insula shared readout (Brain) | §1 | 🟢 |
| R10 | Bird & Cook 2013 — Alexithymia hypothesis | §1 | 🟢 |
| R11 | Fukushima et al. 2011 — Interoceptive accuracy → empathic accuracy | §1, §9 | 🟢 |
| R12 | Mitchell, Macrae & Banaji 2006 — vMPFC/dMPFC dissociation (Neuron) | §1, §9 | 🟢 |
| R13 | Denny et al. 2012 — mPFC spatial gradient (meta-analysis) | §1 | 🟢 |
| R14 | Hassabis et al. 2007 — Hippocampal amnesia → cannot imagine (PNAS) | §1, §4 | 🟢 |
| R15 | Lombardo et al. 2010 — Shared self/other mentalizing (J Cog Neurosci) | §1 | 🟢 |
| R16 | Lopes, Salovey & Straus 2003 — Regulation ↔ interaction (Emotion) | §1, §9 | 🟢 |
| R17 | Coan & Sbarra 2015 — Social Baseline Theory | §1, §9 | 🟢 |
| R18 | Clark 2013 — Predictive Processing | §2 | 🟢 |
| R19 | Friston 2010 — Free Energy Principle | §2 | 🟢 |
| R20 | Cowan 2001 — Working memory capacity | §2, §4 | 🟢 |
| R21 | Miller & Cohen 2001 — PFC top-down attention | §2, §3 | 🟢 |
| R22 | Anderson & Green 2001 — Think/No-Think paradigm | §3 | 🟢 |
| R23 | Wegner 1987 — Ironic process theory | §3 | 🟢 |
| R24 | Berridge 2003 — Wanting ≠ Liking distinction | §3 | 🟢 |
| R25 | Walker 2017 — Why We Sleep (REM consolidation) | §4 | 🟢 |
| R26 | Raichle 2001 — Default Mode Network discovery | §4 | 🟢 |
| R27 | Jeannerod 1995 — Mental simulation = motor pathways | §5 | 🟢 |
| R28 | Kosslyn 1994 — Image and Brain (visual simulation) | §5 | 🟢 |
| R29 | Bandura 1997 — Self-efficacy: spiral model | §5 | 🟢 |
| R30 | Ericsson 1993 — Deliberate practice | §5, §9 | 🟢 |
| R31 | Latham & Pinder 2005 — Work motivation meta-analysis | §5 | 🟢 |
| R32 | Trapnell & Campbell 1999 — Self-reflection vs self-rumination | §8 | 🟢 |
| R33 | Joireman, Parrott & Hammersla 2002 — Self-absorption paradox | §8 | 🟢 |
| R34 | Sapolsky 2004 — Why Zebras Don't Get Ulcers (cortisol effects) | §2 | 🟢 |
| R35 | Aron & Aron 1986 — Self-expansion model | §7 | 🟢 |
| R36 | Gendlin 1978 — Focusing: felt sense technique | §9 | 🟢 |

---

> *Imagine-Final — Application (Self, Future, Simulate+Construct) trên Simulation Engine.*
> *Body PRE-FEEL trạng thái tương lai = Reference Pattern.*
> *3 tầng: Body-Need (tại sao) → Imagine-Final (về đâu) → Plan (bằng cách nào).*
> *MOST PFC-ACCESSIBLE application: SET scenario + READ output + ITERATE.*
> *Shared substrate với SPM + Self-Observation → luyện 1 = luyện cả 3.*
> *Lifecycle: BUILD → SAVE → BACKGROUND → RELOAD → REFINE → loop.*
> *5 levels: Wish → Obsession. Nâng level = NẠP CHUNKS THẬT, không phải nghĩ nhiều.*
> *3 chiều độc lập: Clarity × Quality × Trust. RÕ ≠ ĐÚNG ≠ TIN.*
> *Engine use quality: Reflection → explore. Rumination → catastrophize.*
> *Không có nó → "chán". Có nó → cùng khó nhưng "xứng đáng".*
