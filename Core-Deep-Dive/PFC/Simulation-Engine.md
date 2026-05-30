---
title: Simulation-Engine — 1 Engine, 3 Components, N Applications
version: 1.1
created: 2026-05-22
updated: 2026-05-25 (v1.1 — §3.3 +Simulation-Engine × Dissonance Type output asymmetry, +Dissonance-Signal-Architecture cross-ref)
status: MECHANISM v1.1
scope: |
  ARCHITECTURE file: Brain có 1 general-purpose Simulation-Engine, KHÔNG PHẢI N modules riêng.
  3 Components: Interoception (readout) × Constructive Simulation (CPU) × Self/Other Model (target).
  3 Axes: Target (Self↔Other) × Time (Past↔Future) × Operation (Observe↔Construct).
  Application = tọa độ trong 3D space. Self-Pattern-Modeling, Self-Observation, Imagine-Final = 3 named points.
  Alexithymia = decisive proof cho shared substrate.
  PFC accessibility spectrum, engine use quality, bidirectional loop, training implications.
purpose: |
  Self-Pattern-Modeling.md = APPLICATION-1 (mechanism riêng cho agent prediction).
  Imagine-Final.md = APPLICATION-2 (mechanism riêng cho future simulation).
  Self-Observation = APPLICATION-3 (PFC observe body state; partially described in Feeling.md, chưa có file riêng).
  File NÀY = SHARED ENGINE underneath tất cả — KIẾN TRÚC THỐNG NHẤT.
  Giải thích TẠI SAO: luyện 1 → improve tất cả. Hỏng 1 → degrade tất cả.
  = "Missing architecture file" — mỗi application file mô tả 1 app, file này mô tả ENGINE.
position: |
  Core-Deep-Dive/PFC/ — ngang hàng PFC-Operations.md.
  Engine gồm DMN + mPFC + insula + hippocampus (không thuần PFC),
  nhưng PFC = orchestrator/user → đặt tại PFC/ cho navigation.
  PFC-Operations.md = HOW PFC operates (Hold/Suppress).
  Simulation-Engine.md = WHAT substrate runs ALL simulation applications.
dependencies:
  - Inter-Body-Mechanism.md v1.0 — §3 Compiled/Fresh axis, Compilable Architecture
  - PFC-Operations.md v1.0 — §9 PFC Budget, §10 Compilable Architecture + 3-Cost
  - Self-Pattern-Modeling.md v3.1 — APPLICATION-1, Compiled/Fresh on engine
  - Imagine-Final.md v3.0 — APPLICATION-2, future simulation
  - Feeling.md v3.0 — PFC observation interface (broader than APPLICATION-3; Self-Observation chưa có file riêng)
  - Body-Feedback-Mechanism.md v2.1 — §3 chunk dynamics, body-feedback readout
  - Dissonance-Signal-Architecture.md v1.0 — §7.1 Simulation-Engine × Evaluative Dissonance generator
  - Entity-Access.md v1.1 — Entity-Access gradient = mPFC gradient
  - Entity-Valence-Dynamics.md v2.0 — per-entity valence on engine
  - Connection.md v4.0 — social context for bidirectional loop
sources:
  - Drill-Simulation-Engine v1.0 (809L, 16 insights, 23 citations)
  - Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 (~680L, 13 insights, 22 citations)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Simulation-Engine — 1 Engine, 3 Components, N Applications

> **Brain KHÔNG CÓ module riêng cho mỗi "mental function."**
> **Self-Pattern-Modeling, Self-Observation, Imagine-Final, memory, counterfactual, moral judgment, creativity...**
> **TẤT CẢ = APPLICATIONS chạy trên CÙNG 1 ENGINE.**
>
> **ENGINE = Constructive Simulation Substrate:**
> **DMN + vMPFC + anterior insula + hippocampus.**
>
> **3 COMPONENTS:**
> **① Interoception (anterior insula): ĐỌC body signals.**
> **② Constructive Simulation (DMN + hippocampus): RECOMBINE chunks vào scenarios.**
> **③ Self/Other Model (mPFC gradient): VENTRAL = self+close. DORSAL = distant.**
>
> **3 AXES xác định APPLICATION:**
> **Target (Self ↔ Other) × Time (Past ↔ Future) × Operation (Observe ↔ Construct).**
>
> **Application = TỌA ĐỘ trong không gian 3 trục.**
> **Self-Pattern-Modeling = (Other, Present, Simulate). Self-Observation = (Self, Present, Observe).**
> **Imagine-Final = (Self, Future, Simulate+Construct).**
>
> **Luyện 1 component = luyện TẤT CẢ applications.**
> **Hỏng 1 component = hỏng TẤT CẢ applications.**

---

## Mục lục

- §0 — THESIS + POSITION
- §1 — 1 ENGINE, 3 COMPONENTS
- §2 — 3 AXES: TARGET × TIME × OPERATION
- §3 — APPLICATION TAXONOMY
- §4 — COMPONENT 1: INTEROCEPTION (readout)
- §5 — COMPONENT 2: CONSTRUCTIVE SIMULATION (CPU+RAM)
- §6 — COMPONENT 3: SELF/OTHER MODEL (mPFC gradient)
- §7 — ALEXITHYMIA: COMPONENT FAILURE → ALL APPLICATIONS FAIL
- §8 — PFC ACCESSIBILITY SPECTRUM
- §9 — ENGINE USE QUALITY: REFLECTION vs RUMINATION
- §10 — BIDIRECTIONAL LOOP: SOCIAL ↔ SELF
- §11 — TRAINING: 1 COMPONENT → N IMPROVEMENTS
- §12 — HONEST ASSESSMENT
- §13 — CROSS-REFERENCES
- §14 — RESEARCH CITATIONS

---

## §0 — THESIS + POSITION

### §0.1 — Core thesis

```
⭐⭐⭐ SIMULATION-ENGINE:

  ① Brain có 1 general-purpose SIMULATION-ENGINE (not N separate modules)
  ② Engine = 3 COMPONENTS: Interoception × Constructive Simulation × Self/Other Model
  ③ 3 AXES xác định application: Target × Time × Operation
  ④ Mọi "mental function" = tọa độ cụ thể trong 3D space
  ⑤ Self-Pattern-Modeling, Self-Observation, Imagine-Final = 3 NAMED POINTS, not separate systems
  ⑥ Luyện 1 component = improve ALL applications (shared substrate)
  ⑦ Hỏng 1 component = degrade ALL applications (alexithymia proof)
  ⑧ PFC accessibility = spectrum (auto → observe → active control)
  ⑨ Engine use QUALITY = f(curiosity vs threat): reflection vs rumination
  ⑩ Social ↔ self-regulation = BIDIRECTIONAL loop on shared substrate
  
  🟢 Shared circuits: Lombardo 2010 (fMRI — identical connectivity)
  🟢 Constructive simulation: Schacter & Addis 2007 (Nature Reviews Neuroscience)
  🟢 Self-projection: Buckner & Carroll 2007
  🟢 vMPFC gradient: Mitchell 2006 (Neuron), Tamir & Mitchell 2010
  🟢 Alexithymia proof: Bird & Cook 2013, Bird & Silani 2010
  🟡 "1 engine, 3 components, 3 axes" model = framework synthesis
```

### §0.2 — Position

```
  VỊ TRÍ TRONG KIẾN TRÚC:

  ★ File này = ENGINE ARCHITECTURE (unification)
    │
    ├── Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 = EVIDENCE (neural proof)
    │
    ├── Self-Pattern-Modeling v3.1 = APPLICATION-1 (Self-Pattern-Modeling mechanism)
    │   = Other × Present × Simulate
    │
    ├── Imagine-Final.md v3.0 = APPLICATION-2 (future simulation)
    │   = Self × Future × Simulate+Construct
    │
    ├── Self-Observation = APPLICATION-3 (chưa có file riêng)
    │   = Self × Present × Observe
    │   (partially described in Feeling.md — Feeling scope rộng hơn APPLICATION này)
    │
    ├── PFC-Operations.md v1.0 = HOW PFC operates trên engine
    │   = Hold/Suppress on Compiled/Fresh spectrum
    │
    └── Entity-Access.md v1.1 = APPLIED (mPFC gradient = access spectrum)
        = Entity-Access level → ventral/dorsal processing

  CÁI MỚI:
    → ARCHITECTURE level: 3 components identified as building blocks
    → 3 AXES model: continuous space, not discrete categories
    → FULL TAXONOMY: 11+ applications mapped
    → Named applications = POINTS in continuous space
    → Unnamed applications = EQUALLY REAL functions on same engine
```

---

## §1 — 1 ENGINE, 3 COMPONENTS

```
⭐⭐⭐ COMPILED/FRESH = GENERAL-PURPOSE HARDWARE (Inter-Body-Mechanism §3).
    SIMULATION-ENGINE = 3 COMPONENTS TRÊN HARDWARE NÀY:

  COMPONENT 1 — INTEROCEPTION (anterior insula):
    = ĐỌC body signals TRỰC TIẾP
    = Posterior insula: raw sensory → anterior insula: emotional representation
    = UNIQUE cho self-target (chỉ tôi đọc được body CỦA TÔI)
    = Self-Pattern-Modeling→other KHÔNG CÓ component này → phải INFER từ external cues
    = = "MÀN HÌNH": readout device cho body-feedback output
    
  COMPONENT 2 — CONSTRUCTIVE SIMULATION (DMN + hippocampus):
    = RECOMBINE chunks từ library vào novel scenarios
    = Hippocampus: retrieve + recombine chunks
    = DMN (mPFC + PCC + precuneus + lateral temporal): simulation network
    = DÙNG CHO MỌI HƯỚNG: past, present, future, counterfactual
    = = "CPU + RAM": processing engine cho simulation
    
  COMPONENT 3 — SELF/OTHER MODEL (mPFC gradient):
    = Ventral mPFC: self + CLOSE others (processed AS self-extension)
    = Dorsal mPFC: dissimilar others (processed as SEPARATE model)
    = GRADIENT: close→far = ventral→dorsal (continuous, not binary)
    = = "BẢNG ĐIỀU KHIỂN": xác định simulation TARGET

  3 COMPONENTS HOẠT ĐỘNG CÙNG LÚC:
    Component 2 (DMN) = engine chạy simulation
    Component 3 (mPFC) = chọn target (self vs close vs far)
    Component 1 (insula) = đọc output (body-feedback)
    → Application = WHICH combination of targets + timing + readout
    
  ANALOGY:
    = 1 COMPUTER (engine), 3 thành phần (display + CPU + control panel)
    = Self-Pattern-Modeling = app nhắm vào NGƯỜI KHÁC
    = Self-Observation = app nhắm vào BẢN THÂN
    = Imagine-Final = app nhắm vào TƯƠNG LAI
    = TẤT CẢ dùng cùng CPU, cùng RAM, cùng display
    → Upgrade CPU = upgrade ALL apps
    → Display broken = ALL apps broken (alexithymia)
    
  🟢 DMN as Simulation-Engine: Buckner et al. 2008
  🟢 Constructive simulation: Schacter, Addis & Buckner 2007
  🟢 Interoception readout: Bird, Silani et al. 2010
  🟡 "3 components" explicit model = framework synthesis
```

---

## §2 — 3 AXES: TARGET × TIME × OPERATION

### §2.1 — Trục A: Target

```
⭐⭐ AI đang được simulate?

  Self ←────────→ Close Other ←────────→ Far Other
  (ventral mPFC)   (ventral mPFC)         (dorsal mPFC)
  
  Self: simulate OWN state (interoception available = extra input)
  Close Other: simulate using SELF-TEMPLATE (Entity-Access high)
    → Mitchell 2006: ventral mPFC = same as self-referential circuits
    → = "Con là phần đời tôi" LITERALLY true at neural level
  Far Other: simulate using SEPARATE MODEL (strangers, dissimilar)
    → Tamir & Mitchell 2010: dorsal mPFC = different processing
    → Cost HIGHER (Fresh processing required to build model)
    
  ⭐ CONTINUOUS, not binary:
    Self → vợ/chồng → con → mẹ → bạn thân → colleague → stranger
    = GRADIENT ventral → dorsal as CLOSENESS decreases
    = Entity-Access formation = brain SHIFTING entity from dorsal → ventral
    → Entity-Access deepening = neural migration from "separate" to "self-like"

  🟢 Mitchell 2006 (Neuron): double dissociation
  🟢 Tamir & Mitchell 2010: clan mentality
  🟢 Denny et al. 2012: spatial gradient meta-analysis
```

### §2.2 — Trục B: Time

```
  Past ←─── Present ───→ Future
                  ↘
             Counterfactual
             (alternative past/present/future)
  
  Past: RECONSTRUCT từ compiled chunks (not replay)
    → Memory = RECONSTRUCTIVE simulation, not tape playback
    → SAME engine as future, just different INPUT parameters
    🟢 Schacter & Addis 2007: constructive episodic simulation
    
  Present: OBSERVE current state (body-feedback NOW)
    → LEAST constructive — mostly READOUT (interoception dominant)
    
  Future: CONSTRUCT novel scenario from chunk recombination
    → MOST constructive — hippocampus recombine + PFC evaluate
    
  Counterfactual: RE-CONSTRUCT with altered parameters
    → "Nếu lúc đó tôi làm khác..." = past + altered element + re-simulate
    🟢 Van Hoeck et al. 2013: counterfactual shares episodic simulation network
```

### §2.3 — Trục C: Operation

```
  Observe ←──→ Simulate ←──→ Evaluate ←──→ Construct
  (passive       (run           (judge         (build novel
   readout)       scenario)      good/bad)      scenario)
  
  Observe: PFC PASSIVELY reads body-feedback output
    → "Tôi đang buồn" = readout only, no manipulation
    → Self-Observation primary mode
    
  Simulate: Engine RUNS scenario, PFC reads output
    → "Bạn đang buồn vì..." = simulate other's state
    → Self-Pattern-Modeling primary mode
    
  Evaluate: PFC JUDGES simulation output (moral, value, decision)
    → "Hành động này đúng hay sai?" = simulate consequences + judge
    → COMPOUND: simulate (run) + observe (read) + evaluate (judge)
    🟢 Greene et al. 2001: moral dilemmas activate vMPFC + TPJ
    
  Construct: PFC ACTIVELY BUILDS novel scenario
    → "Tưởng tượng 1 thế giới nơi..." = creative imagination
    → Imagine-Final = construct + observe (most PFC-active)

  → APPLICATION = POINT (A, B, C) trong 3D space
  → Named applications = labeled points. Unnamed = unlabeled points.
  → Space is CONTINUOUS — applications BLEND into each other.
  
  🟡 3-axis model = framework synthesis
  🟢 Neural evidence per axis: Mitchell 2006 (A), Schacter 2007 (B), Greene 2001 (C)
```

---

## §3 — APPLICATION TAXONOMY

### §3.1 — 11+ Applications mapped

```
⭐⭐ APPLICATION = (TARGET, TIME, OPERATION):

  ┌───┬──────────────────┬──────────────┬───────────┬──────────┬──────────────────────┐
  │ # │ Application      │ Target       │ Time      │ Operation│ Framework file       │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ① │ Self-Pattern-Modeling              │ Other(close) │ Present   │ Simulate │ Self-Pattern-Modeling │
  │   │ "bạn đang buồn"  │ or far       │           │          │ v3.0                 │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ② │ Self-Observation  │ Self         │ Present   │ Observe  │ (chưa có file riêng) │
  │   │ "tôi đang lo"    │              │           │(+intero.)│ cf. Feeling.md v3.0  │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ③ │ Imagine-Final     │ Self         │ Future    │ Simulate │ Imagine-Final.md     │
  │   │ "nếu tôi bỏ việc"│              │           │+Construct│                      │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ④ │ Predict Other's   │ Other        │ Future    │ Simulate │ Self-Pattern-Modeling + Imagine-Final  │
  │   │ Future            │              │           │          │ combined             │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑤ │ Memory Recall     │ Self         │ Past      │ Simulate │ (reconstructive)     │
  │   │ "tôi lúc đó..."  │              │           │(reconstr)│ Schacter & Addis     │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑥ │ Recall Other's   │ Other        │ Past      │ Simulate │ "bạn lúc đó..."     │
  │   │ Past             │              │           │          │                      │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑦ │ Counterfactual    │ Self/Other   │ Alt-Past  │ Simulate │ "Nếu lúc đó làm     │
  │   │                  │              │           │+Construct│ khác..."             │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑧ │ Moral Judgment    │ Self+Other   │ Future    │ Evaluate │ Greene 2001:         │
  │   │ "đúng hay sai?"  │ (compound)   │           │+Simulate │ vMPFC+TPJ            │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑨ │ Narrative Self    │ Self         │ Past→Pres │ Construct│ "Tôi là ai?"        │
  │   │ (identity)       │              │ →Future   │ (story)  │ Autobiographical     │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑩ │ Decision Branch   │ Self         │ Future    │ Simulate │ Imagine-Final ×N     │
  │   │ "A hay B?"       │              │ (×N)      │ (×N)     │ + compare outputs    │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑪ │ Creative Imagin.  │ Abstract     │ Hypothet. │ Construct│ DMN creativity       │
  │   │                  │ (no person)  │           │ (novel)  │                      │
  ├───┼──────────────────┼──────────────┼───────────┼──────────┼──────────────────────┤
  │ ⑫ │ Mind Wandering    │ Variable     │ Variable  │ Auto     │ DMN default mode     │
  │   │ + Dream          │ (unfocused)  │ (drift)   │ (passive)│ Offline simulation   │
  └───┴──────────────────┴──────────────┴───────────┴──────────┴──────────────────────┘
```

### §3.2 — Key observations

```
  ① CÁC APPLICATION BLEND VÀO NHAU:
    "Tôi nhớ lúc đó bạn buồn" = ⑥ (recall other) + ① (Self-Pattern-Modeling past-state)
    "Nếu mẹ ép, con sẽ buồn" = ④ (predict other future) + ⑧ (moral evaluate)
    "Tôi muốn trở thành người tốt hơn" = ⑨ (narrative) + ③ (imagine future)
    → KHÔNG CÓ RANH GIỚI RÕ → continuous space

  ② 3 NAMED APPLICATIONS (①②③) KHÔNG ĐẶC BIỆT HƠN CÁC CÁI KHÁC:
    Framework đặt tên Self-Pattern-Modeling, Self-Observation, Imagine-Final vì chúng QUAN TRỌNG
    NHƯNG: predict other's future (④), counterfactual (⑦), moral judgment (⑧)
    = EQUALLY REAL functions trên CÙNG engine
    → Framework chưa drill deep các function ④-⑫

  ③ COMPOUND APPLICATIONS = MULTI-STEP trên engine:
    Moral judgment (⑧) = simulate other's suffering (①) + simulate future (③)
      + evaluate + observe own moral feeling (②) = 4 STEPS, not separate function
    Decision branch (⑩) = Imagine-Final (③) × N + compare outputs
      = ITERATE same function with different parameters

  ④ DREAM + MIND WANDERING = ENGINE ở CHẾ ĐỘ TỰ ĐỘNG:
    Không có PFC active control → engine "free run"
    → Output = unpredictable combinations (sometimes insightful)
    → = WHY creative solutions sometimes appear during rest
    🟢 Schacter: dreams = offline constructive episodic simulation

  🟡 Full taxonomy = framework synthesis
```

### §3.3 — Simulation-Engine × Dissonance Type: Output Asymmetry

```
🟡 SIMULATION-ENGINE = EVALUATIVE DISSONANCE GENERATOR (Dissonance-Signal-Architecture.md v1.0 §7.1):

  Simulation-Engine CAN generate Evaluative Dissonance WITHOUT external input:
    "Imagine-Final: công ty phá sản" → body pre-feel → Evaluative Dissonance
    "Preview: bị đuổi việc" → body simulate → Evaluative Dissonance
    "Self-model: mình không xứng đáng" → schema mismatch → Evaluative Dissonance
    → Applications ③④⑦⑧⑨⑩ ALL có thể generate Evaluative Dissonance

  Simulation-Engine KHÔNG generate Direct-State Dissonance:
    Cannot create real tissue damage through simulation.
    Cannot create real hunger, real pain, real temperature change.
    → Direct-State Dissonance requires HARDWARE activation — not simulation.

  NHƯNG: Simulation-Engine CAN CASCADE Evaluative → Direct-State body symptoms:
    "Imagine-Final: hổ tấn công" → cortisol spike → heart rate up → body symptoms
    = Evaluative TRIGGER → Direct-State CASCADE (not Direct-State origin)
    → Anxiety disorder = Simulation-Engine over-generates Evaluative → cascades to body symptoms

  → Animals: Simulation-Engine limited → Evaluative Dissonance limited → less "worry"
  → Humans: Simulation-Engine rich → Evaluative Dissonance VAST → "suffering from thoughts alone"
  → = WHY Compilable Architecture = more suffering types (Dissonance-Signal-Architecture §0.3)

  🟡 Simulation-Engine × dissonance type asymmetry = framework synthesis.
  🟢 Simulation generates anticipatory distress: Grupe & Nitschke 2013 (uncertainty and anticipatory anxiety).
```

---

## §4 — COMPONENT 1: INTEROCEPTION (readout)

### §4.1 — Mechanism

```
⭐⭐ INTEROCEPTION = "MÀN HÌNH" — READOUT DEVICE:

  CƠ CHẾ (anterior insula hierarchy):
    Posterior insula: map RAW sensory (heart rate, gut, temperature)
    → Successive integrations →
    Anterior insula: EMOTIONAL representation ("tôi đang lo," "tôi vui")
    → = Raw signal → processed signal → PFC-readable output
    
  UNIQUE CHO SELF-TARGET:
    Self-Observation: interoception = DIRECT READ (body CỦA TÔI)
    Self-Pattern-Modeling→other: interoception = INFERRED (external cues → simulate → readout)
    → Self-Observation có THÊM 1 kênh input mà Self-Pattern-Modeling→other không có
    → = WHY self-observation SHOULD be more accurate
```

### §4.2 — Interoception paradox

```
  PARADOX — NHƯNG THỰC TẾ CÓ THỂ NGƯỢC LẠI:
    Self signals ALWAYS ON → HABITUATE → PFC IGNORES
    Other signals CHANGE → NOVEL → PFC NOTICES
    → Self có NHIỀU data nhưng PROCESS ÍT (habituated)
    → Other có ÍT data nhưng PROCESS KỸ (novel)
    → = WHY "mẹ biết con buồn" (novel external cue)
      nhưng "không biết mình lo" (habituated internal signal)
    
  🟡 Habituation paradox = framework synthesis
```

### §4.3 — Interoception as bottleneck

```
  INTEROCEPTION QUALITY = BOTTLENECK CHO MỌI APPLICATION:
  
    🟢 Fukushima et al. 2011: interoceptive accuracy PREDICTS empathic accuracy
    🟢 Bird & Silani 2010: anterior insula active for BOTH self AND other
    🟢 Terasawa et al. 2021: interoception ↔ empathy BIDIRECTIONAL
    
    → Good interoception → good at ② (self) AND ① (other) AND ③ (future)
    → Poor interoception → poor at ALL applications
    → = 1 bottleneck, N affected functions
    
    PRACTICAL: training interoception (body awareness, meditation, Focusing)
    → Improve quality of ALL engine applications simultaneously
    → Xem §11 Training cho chi tiết.
```

---

## §5 — COMPONENT 2: CONSTRUCTIVE SIMULATION (CPU+RAM)

### §5.1 — Mechanism

```
⭐⭐ DMN + HIPPOCAMPUS = "CPU + RAM" — SIMULATION-ENGINE:

  🟢 Schacter & Addis 2007 (Nature Reviews Neuroscience):
    "Constructive Episodic Simulation Hypothesis":
    → Brain uses SAME hippocampal-cortical system to:
      → Reconstruct past episodes (memory)
      → Construct future scenarios (prospection)
      → Imagine other perspectives (mentalizing)
    → = 1 engine, 3 functions — neuroscience independently discovered same concept

  CƠ CHẾ:
    ① Hippocampus RETRIEVE chunks from compiled library
    ② DMN RECOMBINE chunks into novel configuration
    ③ Anterior insula READOUT body-feedback from simulation
    ④ PFC ATTRIBUTE output to target (self/other, past/future)
    → = Framework's Compiled/Fresh spectrum = engine's operating modes
    → Compiled: fast recombination from well-worn patterns
    → Fresh: slow, deliberate recombination with novel elements
```

### §5.2 — Memory = reconstruction

```
  MEMORY = RECONSTRUCTION (not replay):
  
    🟢 Schacter 2001: "Seven Sins of Memory"
    Brain KHÔNG lưu video → lưu CHUNKS
    Recall = REASSEMBLE chunks vào coherent narrative
    
    → Same engine as future simulation, just DIFFERENT CONSTRAINTS:
      Memory: constrain to "past chunks" → reconstruct
      Future: constrain to "possible chunks" → construct
      Counterfactual: constrain to "past + altered element" → re-construct
      Creative: MINIMAL constraints → free construct
    → = CÙNG ENGINE, KHÁC CONSTRAINTS = KHÁC OUTPUT
    
    🟢 Hassabis et al. 2007 (PNAS):
    Hippocampal amnesia patients → CANNOT imagine new experiences
    → Hippocampus required for CONSTRUCTIVE simulation, not just memory
    → Without it: no new scenarios possible (past OR future)
```

### §5.3 — DMN anatomy

```
  🟢 Buckner, Andrews-Hanna & Schacter 2008 (Annals NYAS):
    DMN active during: autobiographical memory, prospection, ToM, spatial navigation
    → ALL instances of mental SIMULATION
    
  🟢 Neuron 2023 — 20 years of Default Mode Network:
    DMN = not "resting state" → ACTIVE simulation network
    → Engaged whenever brain constructs internal models
    
  🟢 Spreng & Grady 2010:
    Extensive overlap: autobiographical memory + imagining future + mentalizing
    Shared network: mPFC, posterior cingulate, hippocampus, lateral temporal

  → Framework: Compiled/Fresh spectrum = this engine
  → Compiled = automatic recombination (fast, familiar patterns)
  → Fresh = PFC-guided recombination (slow, novel configurations)
```

---

## §6 — COMPONENT 3: SELF/OTHER MODEL (mPFC gradient)

### §6.1 — Double dissociation

```
⭐⭐ mPFC = "BẢNG ĐIỀU KHIỂN" — XÁC ĐỊNH TARGET:

  🟢 Mitchell, Macrae & Banaji 2006 (Neuron):
    DOUBLE DISSOCIATION:
      Mentalizing SIMILAR other → VENTRAL mPFC (= self circuits)
      Mentalizing DISSIMILAR other → DORSAL mPFC (separate circuits)
      
  🟢 Tamir & Mitchell 2010 (J. Neuroscience):
    "Clan Mentality": vMPFC responds MORE to close others (friends)
    → Close other = processed AS self-extension
    → = Framework's Entity-Access deep = body-base extension
    → = Neuroscience INDEPENDENTLY confirmed framework concept
```

### §6.2 — Continuous gradient

```
  🟢 Denny et al. 2012 (meta-analysis):
    Spatial gradient: increasingly ventral = MORE self-related
    → Not binary (self vs other) but CONTINUOUS gradient
    
  GRADIENT MAP:
  
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │  VENTRAL mPFC                    DORSAL mPFC            │
    │  ←──────────────────────────────────────────→           │
    │                                                         │
    │  Self        Close Others        Far Others             │
    │  "tôi"       "con, mẹ, vợ"      "stranger"             │
    │                                                         │
    │  Template:   Template:           Template:              │
    │  OWN chunks  OWN chunks          BUILD explicit         │
    │  (direct)    (as-if self)        model (effortful)      │
    │                                                         │
    │  Cost: ≈ 0   Cost: LOW           Cost: HIGH             │
    │  (auto)      (Compiled)       (Fresh needed)      │
    │                                                         │
    │  Accuracy:   Accuracy:           Accuracy:              │
    │  HIGH (self) HIGH if similar     LOWER, but less biased │
    │              BIASED if not       (no self-template bias) │
    │                                                         │
    │  Intero: YES Intero: NO          Intero: NO             │
    │  (direct)    (infer from cues)   (infer from cues)      │
    └─────────────────────────────────────────────────────────┘
```

### §6.3 — Entity-Access = neural migration

```
  ⭐ ENTITY-ACCESS = NEURAL MIGRATION:
  
    Stranger: dorsal mPFC (separate model, Fresh required)
    → Repeated interaction → Entity-Compiled deepens → entity MOVES ventral
    → Close other: ventral mPFC (self-template, Compiled)
    → Entity-Access high = brain HAS MIGRATED entity into "self territory"
    → = "Của tôi" = LITERALLY in self-processing circuits
    
    Entity LOST (death, separation):
    → Brain VẪN process entity in ventral (compiled chunks persist)
    → But entity ABSENT → prediction FIRE, no RESPONSE
    → = Phantom resonance = ventral mPFC fire for absent entity
    → = "Mất phần đời tôi" ĐÚNG ở mức neural: entity WAS in self-circuits
    
  🟢 Mitchell 2006: double dissociation
  🟢 Tamir & Mitchell 2010: clan mentality
  🟢 Denny et al. 2012: spatial gradient meta-analysis
  🟡 Entity-Access as neural migration = framework synthesis
```

### §6.4 — Similar vs dissimilar: 2 processing modes

```
  SIMILAR → vMPFC (self-template):
    = Self-Pattern-Modeling Compiled: compiled, automatic, self-as-template
    → Cost THẤP. Accuracy CAO cho similar, BIASED cho dissimilar
    
  DISSIMILAR → dMPFC (explicit model):
    = Self-Pattern-Modeling Fresh: fresh, deliberate, build separate model
    → Cost CAO. Accuracy LOWER but POTENTIALLY less biased

  ⭐ IMPLICATION CHO SELF-CALIBRATION:
    Toàn SIMILAR (vMPFC only): "mọi người giống tôi" → biases REINFORCED
    MIX (vMPFC + dMPFC): dissimilar CHALLENGE → reveal own assumptions
    → Mismatch → "điều tôi assume = MY bias, not universal"
    → = Diversity → sharper self-model through CONTRAST
    → Xem §10 Bidirectional Loop cho implications.

  🟢 Mitchell 2006: vMPFC/dMPFC double dissociation
  🟡 Diversity → self-calibration = logically sound, limited direct evidence
```

---

## §7 — ALEXITHYMIA: COMPONENT FAILURE → ALL APPLICATIONS FAIL

```
⭐⭐ DECISIVE PROOF CHO SHARED SUBSTRATE:

  🟢 Bird & Cook 2013:
    Alexithymia = broken body-readout (Component 1 FAILURE)
    → BOTH self-awareness AND social cognition deficits
    → NOT autism per se → alexithymia UNDERLIES social atypicalities
    → = Broken READOUT (display hỏng) → ALL applications see nothing
    
  🟢 Bird, Silani et al. 2010 (Brain):
    HIGH alexithymia → REDUCED anterior insula for:
      ① Own emotion recognition (Self-Observation)
      ② Other's pain empathy (Self-Pattern-Modeling)
    → CÙNG substrate hỏng → CÙNG lúc mất cả 2 directions
    
  🟢 Mul et al. 2021 (European Archives Psych.):
    Network analysis: alexithymia = CENTRAL NODE
    → Links interoceptive deficits TO empathy deficits
    → = Hub trong mạng lưới, not isolated deficit

  FRAMEWORK MAPPING:
    Alexithymia = Component 1 (interoception) BROKEN
    → ② Self-Observation: FAIL (cannot read own body-state)
    → ① Self-Pattern-Modeling: FAIL (cannot read simulated body-state)
    → ③ Imagine-Final: DEGRADED (cannot pre-feel future state)
    → ⑤ Memory recall: DEGRADED (cannot re-feel past state)
    → ⑧ Moral judgment: DEGRADED (cannot feel moral valence)
    → = 1 component failure → ALL N applications degraded
    → = PROOF: shared substrate (if separate, failure would be isolated)
    
  Compiled VẪN FIRE nhưng READOUT BROKEN:
    → Body SIMULATE nhưng PFC CANNOT READ output
    → = Input intact, processing intact, READOUT broken
    → = Giống có camera nhưng màn hình hỏng: vẫn quay nhưng không xem được
    
  🟢 Bird & Cook 2013, Bird & Silani 2010, Mul 2021
```

---

## §8 — PFC ACCESSIBILITY SPECTRUM

```
⭐⭐ CÙNG ENGINE, KHÁC MỨC ĐỘ PFC CAN THIỆP:

  ┌──────────────┬────────────────────────────────────────────────────┐
  │ APPLICATION  │ PFC ROLE                                          │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ⑫ Dream      │ ZERO PFC: engine free-run during sleep            │
  │              │ Output = unpredictable, sometimes insightful       │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ⑫ Mind wander│ LOW PFC: engine drift, attention unfocused        │
  │              │ "Bỗng nhớ chuyện cũ" = engine auto-associate      │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ① Self-Pattern-Modeling Compiled     │ MINIMAL: compiled, automatic, invisible           │
  │ (compiled)   │ "Thấy thích bạn mà không biết vì sao"            │
  │              │ PFC = PASSIVE observer (if even aware)             │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ② Self-Obs   │ MIDDLE: PFC observe body-feedback output          │
  │              │ PFC = READER (can label but not manipulate input)  │
  │              │ "Tôi đang buồn" = readout, not active simulation  │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ① Self-Pattern-Modeling Fresh     │ MODERATE: PFC actively draft model for unfamiliar │
  │ (fresh)      │ "Người này nghĩ gì nhỉ?" = deliberate simulation  │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ③ Imagine-   │ HIGH: PFC actively SET scenario, READ output,     │
  │ Final        │ ITERATE ("nếu đổi X thì sao?")                   │
  │              │ PFC = DIRECTOR (set up + read + modify + repeat)   │
  ├──────────────┼────────────────────────────────────────────────────┤
  │ ⑩ Decision   │ HIGHEST: Imagine-Final ×N + COMPARE               │
  │ branching    │ "A hay B?" = run engine N times + evaluate outputs │
  └──────────────┴────────────────────────────────────────────────────┘

  ⭐ SPECTRUM, NOT BINARY:
    PFC involvement = CONTINUOUS from zero (dream) to maximum (decision)
    Same engine, same components, DIFFERENT PFC engagement level
    → More PFC = more CONTROLLABLE but more COSTLY (PFC Budget — PFC-Operations §9)
    → Less PFC = more AUTOMATIC but less STEERABLE
    
  ⭐ IMAGINE-FINAL ĐẶC BIỆT VÌ:
    ① PFC CAN OBSERVE output (unlike compiled Compiled = PFC-invisible)
    ② PFC CAN MANIPULATE input ("nếu thay đổi X thì sao?")
    ③ PFC CAN COMPARE multiple simulations ("option A vs B")
    → = CONSCIOUS SIMULATION TOOL: both readout + active control
    → = MOST PFC-ACCESSIBLE application of shared engine
    
  ENTITY-ACCESS CONNECTION:
    PFC Resource (Entity-Access §12) DETERMINES spectrum position:
      Full resources → Imagine-Final mode ("con sẽ cảm thấy gì nếu...")
      Depleted → Self-Pattern-Modeling Compiled default ("con ăn chưa?" = compiled, automatic)
    → Cascading: PFC budget ↓ → accessibility ↓ → engine runs on auto

  🟡 PFC accessibility spectrum = framework synthesis
```

---

## §9 — ENGINE USE QUALITY: REFLECTION vs RUMINATION

```
⭐⭐ CÙNG ENGINE, KHÁC CHẤT LƯỢNG SỬ DỤNG:

  🟢 Trapnell & Campbell 1999:
    2 DISPOSITIONS, previously CONFOUNDED:
    
    SELF-REFLECTION (curiosity drive):
      = "Tại sao tôi cảm thấy vậy?" → explore → insight
      Correlates: openness, empathy, BETTER self-knowledge
      = Novelty cortisol → approach tag → PRODUCTIVE output
      → Improve engine quality: calibrate self-model, refine chunks
      
    SELF-RUMINATION (threat drive):
      = "Tôi chắc sai rồi" → loop → stuck
      Correlates: neuroticism, anxiety, WORSE self-knowledge
      = Threat cortisol → avoidance tag → DESTRUCTIVE loop
      → Degrade engine quality: reinforce fear chunks, no calibration
      
  🟢 Joireman, Parrott & Hammersla 2002:
    Self-reflection → POSITIVE correlation với empathy
    Self-rumination → NEGATIVE correlation với empathy
    → CÙNG "self-attention" → KHÁC OUTCOME tùy motivation
    → = "Self-Absorption Paradox" resolved

  FRAMEWORK MAPPING:
    Reflection = engine run with CURIOSITY cortisol (Body-Feedback-Mechanism §3.3c: productive)
    Rumination = engine run with THREAT cortisol (Body-Feedback-Mechanism §3.3c: anxiety loop)
    → Same engine, same components, same operation
    → DIFFERENT CORTISOL CONTEXT → different output QUALITY
    → = Compile-time direction lock (PFC-Operations §5): genuine vs threat compiled
    
  ⭐ APPLIES TO ALL APPLICATIONS (universal modifier):
    Self-Pattern-Modeling with curiosity: "tại sao bạn nghĩ vậy?" → LEARN about other
    Self-Pattern-Modeling with threat: "bạn chắc ghét tôi" → PROJECT fear onto other
    Imagine-Final with curiosity: "tương lai sẽ thú vị" → EXPLORE options
    Imagine-Final with threat: "tương lai sẽ tệ" → CATASTROPHIZE
    → Engine use quality = UNIVERSAL modifier across ALL applications
    
  🟢 Reflection vs rumination: Trapnell & Campbell 1999
  🟢 Reflection → empathy: Joireman et al. 2002
  🟡 Engine use quality as universal modifier = framework synthesis
```

---

## §10 — BIDIRECTIONAL LOOP: SOCIAL ↔ SELF

### §10.1 — Evidence

```
⭐ SOCIAL INTERACTION VÀ SELF-REGULATION = REINFORCING LOOP:

  🟢 Lopes, Salovey & Straus 2003 (Emotion):
    Better emotion regulation → more positive social interactions
    More positive interactions → better regulation
    → BIDIRECTIONAL, controlling for personality + intelligence
    
  🟢 Coan & Sbarra 2015 (Social Baseline Theory):
    Brain OUTSOURCE emotion regulation to trusted others
    Partner hand-holding → LESS threat neural activity
    → Social contact = EXTERNAL regulation resource
    → More trusted contacts → less self-regulation BURDEN
    → Less burden → MORE capacity for engine quality
    
  🟢 Koudenburg et al. 2024 (European J. Social Psych.):
    Social interaction → self-concept CLARITY + identity strength
    → "Sense of me" forms partly through "sense of we"
```

### §10.2 — Virtuous vs vicious spiral

```
  VIRTUOUS SPIRAL:
    Social interaction → engine PRACTICE (Self-Pattern-Modeling fire on diverse targets)
    → Engine improved → better self-model (shared substrate)
    → Better self-model → better social predictions
    → Better predictions → better interactions → MORE practice → LOOP
    
  VICIOUS SPIRAL:
    Isolation → NO engine practice → substrate ATROPHY
    → Worse self-model → worse social predictions
    → Worse predictions → AVOID social → MORE isolation → LOOP
    → = Hikikomori mechanism: isolation → engine atrophy → cannot re-enter

  DIVERSITY AMPLIFIES VIRTUOUS SPIRAL:
    Similar only (vMPFC): confirm biases → self-model CONFIDENT but INACCURATE
    Mix (vMPFC + dMPFC): dissimilar CHALLENGE → reveal assumptions
    → "Họ KHÁC tôi ở đây" → discover own bias → self-model REFINED
    → = Mitchell 2006: dMPFC activation for dissimilar = contrast signal
    
  🟢 Social Baseline: Coan & Sbarra 2015
  🟢 Identity through interaction: Koudenburg 2024
  🟡 Bidirectional spiral model = framework synthesis
```

---

## §11 — TRAINING: 1 COMPONENT → N IMPROVEMENTS

```
⭐⭐ SHARED SUBSTRATE → 1 TRAINING POINT → N IMPROVEMENTS:

  INTEROCEPTION TRAINING (Component 1 — highest leverage):
    Meditation (body-scan, mindfulness): IMPROVE body-readout
    Focusing (Gendlin 1978): IMPROVE felt-sense awareness
    → Better readout → improve:
      Self-Observation (②): "biết mình đang feel gì" clearer
      Self-Pattern-Modeling (①): "biết người khác đang feel gì" more accurate
      Imagine-Final (③): "feel trước tương lai" more vivid
      Moral judgment (⑧): "feel đúng/sai" more calibrated
    → = 1 training → ≥4 applications improved
    🟢 Interoceptive accuracy → empathic accuracy: Fukushima 2011
    
  DIVERSITY TRAINING (Component 3 — self-model calibration):
    Interact with DISSIMILAR others: activate dMPFC
    → Reveal own biases (Mitchell 2006: contrast effect)
    → Sharper SELF-MODEL → improve ALL self-target applications
    → Sharper OTHER-MODELS → improve ALL other-target applications
    
  REFLECTION PRACTICE (engine use quality):
    Cultivate curiosity orientation (Trapnell & Campbell 1999):
    → Replace "tôi sai rồi" with "tại sao tôi feel vậy?"
    → = Switch cortisol direction: threat → novelty
    → Improve ALL applications by improving engine use QUALITY
    
  SOCIAL PRACTICE (bidirectional loop):
    More diverse, quality interactions → practice engine
    → Engine improved → better at ALL applications
    → = Coan & Sbarra 2015: social = external regulation resource
    
  ⭐ EDUCATION IMPLICATION:
    Body awareness training > cognitive-only instruction
    → Because: improve engine SUBSTRATE → improve N cognitive functions
    → vs. cognitive training: improve 1 specific function only
    → = WHY meditation + social interaction + curiosity = HIGH LEVERAGE
    
  🟡 "1 training → N improvements" model = framework synthesis
  🟢 Individual training effects: established per component
```

---

## §12 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (individual components)
═══════════════════════════════════════

  Shared self/other circuits:             Lombardo 2010 (fMRI, identical connectivity)
  vMPFC similar / dMPFC dissimilar:       Mitchell 2006 (Neuron)
  vMPFC = close others AS self:           Tamir & Mitchell 2010 (J. Neuroscience)
  Spatial gradient meta-analysis:         Denny et al. 2012
  Anterior insula shared readout:         Bird, Silani et al. 2010 (Brain)
  Alexithymia = broken readout:           Bird & Cook 2013
  Alexithymia central node:               Mul et al. 2021
  Interoception → empathy:                Fukushima et al. 2011
  Interoception ↔ empathy bidirectional:  Terasawa et al. 2021
  Constructive episodic simulation:       Schacter & Addis 2007 (Nature Rev. Neurosci.)
  DMN as Simulation-Engine:               Buckner et al. 2008 (Annals NYAS)
  Self-projection:                        Buckner & Carroll 2007
  Hippocampus required for simulation:    Hassabis et al. 2007 (PNAS)
  Memory = reconstruction:               Schacter 2001
  Counterfactual shares episodic network: Van Hoeck et al. 2013
  Moral dilemmas vMPFC+TPJ:              Greene et al. 2001
  Self/other neural overlap:              Uddin, Iacoboni et al. 2007
  Metacognition + mentalizing coupled:    Dimaggio & Lysaker 2015
  Embodied simulation:                    Gallese 2003, 2005
  Memory + social overlap:                Spreng & Grady 2010
  Reflection vs rumination:               Trapnell & Campbell 1999
  Reflection → empathy:                   Joireman et al. 2002
  Social ↔ regulation bidirectional:      Lopes et al. 2003
  Social Baseline outsource:              Coan & Sbarra 2015
  Social → self-concept clarity:          Koudenburg et al. 2024
  20 years DMN review:                    Neuron 2023

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (novel integration)
═══════════════════════════════════════

  "1 engine, 3 components" model — ★★
  "3 axes" application space model — ★★★
  Full 11+ application taxonomy — ★
  Named applications = points in continuous space — ★★
  Interoception habituation paradox — ★★
  PFC accessibility as spectrum — ★
  Entity-Access = neural migration (dorsal→ventral) — ★
  Engine use quality as universal modifier — ★
  1 training → N improvements model — ★
  Bidirectional spiral model — ★

═══════════════════════════════════════
🔴 HYPOTHESIS (testable but unverified)
═══════════════════════════════════════

  Exact number of distinct applications (11? more? fewer?)
  3-axis model completeness (are there more axes?)
  Interoception training → Self-Pattern-Modeling improvement (quantifiable?)
  Diversity threshold for self-model calibration
  Entity-Access migration speed along mPFC gradient
  Dream function as offline engine optimization
```

---

## §13 — CROSS-REFERENCES

| File | Sections | Relationship |
|------|----------|-------------|
| Drill-Self-Pattern-Modeling-Self-Shared-Substrate v1.0 | Full file | EVIDENCE file for this ARCHITECTURE |
| Self-Pattern-Modeling v3.1 | §2 (Compiled/Fresh), §10 (Self-Pattern-Modeling×Imagine-Final) | APPLICATION-1: Self-Pattern-Modeling mechanism |
| Imagine-Final.md v3.0 | Full file | APPLICATION-2: future simulation |
| Feeling.md v3.0 | §3 (PFC observation) | Broader than APPLICATION-3; Self-Observation chưa có file riêng |
| Inter-Body-Mechanism.md v1.0 | §3 (Compiled/Fresh), §1 (Compilable Architecture) | SOURCE-OF-TRUTH for spectrum |
| PFC-Operations.md v1.0 | §5 (Compiled Quality), §9 (PFC Budget) | HOW PFC operates on engine |
| Entity-Access.md v1.1 | §3 (gradient model) | mPFC gradient = Entity-Access spectrum |
| Entity-Valence-Dynamics.md v2.0 | §4 (per-entity table) | Valence modulates engine output |
| Body-Feedback-Mechanism.md v2.1 | §3 (chunk dynamics, readout) | FOUNDATION: body-feedback |
| Dissonance-Signal-Architecture v1.0 | §7.1 (Simulation-Engine × dissonance type) | Simulation-Engine generates Evaluative Dissonance only |
| Connection.md v4.0 | §3 (3 primitives) | SOCIAL context for bidirectional loop |
| Compiled-Fresh.md v2.0 | §6.2 (compile-time direction lock) | MECHANISM: reflection vs rumination |
| Body-Coupling.md v2.0 | §2 (depth × direction) | Coupling uses engine for synchronization |

---

## §14 — RESEARCH CITATIONS

| # | Citation | Used in | Evidence |
|---|----------|---------|----------|
| R1 | Lombardo et al. 2010 — Shared self/other mentalizing circuits (J. Cog. Neurosci.) | §0, §6 | 🟢 fMRI |
| R2 | Mitchell, Macrae & Banaji 2006 — vMPFC/dMPFC dissociation (Neuron) | §2, §6 | 🟢 fMRI |
| R3 | Tamir & Mitchell 2010 — Clan mentality: vMPFC for close others (J. Neurosci.) | §2, §6 | 🟢 fMRI |
| R4 | Denny et al. 2012 — Spatial gradient meta-analysis mPFC | §2, §6 | 🟢 Meta |
| R5 | Bird, Silani et al. 2010 — Anterior insula shared readout (Brain) | §4, §7 | 🟢 fMRI |
| R6 | Bird & Cook 2013 — Alexithymia underlies social deficits | §7 | 🟢 |
| R7 | Mul et al. 2021 — Network analysis alexithymia central node (Eur. Arch. Psych.) | §7 | 🟢 |
| R8 | Fukushima, Terasawa et al. 2011 — Interoception → empathic accuracy | §4, §11 | 🟢 |
| R9 | Terasawa et al. 2021 — Interoception ↔ empathy bidirectional (Frontiers) | §4 | 🟢 |
| R10 | Schacter & Addis 2007 — Constructive episodic simulation (Nature Rev. Neurosci.) | §2, §5 | 🟢 ★ |
| R11 | Buckner, Andrews-Hanna & Schacter 2008 — DMN anatomy (Annals NYAS) | §5 | 🟢 |
| R12 | Buckner & Carroll 2007 — Self-projection and the brain | §0, §5 | 🟢 |
| R13 | Hassabis et al. 2007 — Hippocampal amnesia → cannot imagine (PNAS) | §5 | 🟢 |
| R14 | Schacter 2001 — Seven Sins of Memory: reconstructive recall | §5 | 🟢 |
| R15 | Van Hoeck et al. 2013 — Counterfactual shares episodic network | §2 | 🟢 fMRI |
| R16 | Greene et al. 2001 — Moral dilemmas activate vMPFC + TPJ | §2, §3 | 🟢 fMRI |
| R17 | Trapnell & Campbell 1999 — Self-reflection vs self-rumination | §9 | 🟢 |
| R18 | Joireman, Parrott & Hammersla 2002 — Reflection → empathy | §9 | 🟢 |
| R19 | Lopes, Salovey & Straus 2003 — Emotion regulation ↔ social interaction | §10 | 🟢 |
| R20 | Coan & Sbarra 2015 — Social Baseline Theory | §10 | 🟢 |
| R21 | Koudenburg et al. 2024 — Social → self-concept clarity (Eur. J. Soc. Psych.) | §10 | 🟢 |
| R22 | Gendlin 1978 — Focusing: body-readout improvement | §11 | 🟢 Clinical |
| R23 | Neuron 2023 — 20 years of the Default Mode Network (review) | §5 | 🟢 Review |
| R24 | Spreng & Grady 2010 — Memory + social cognition overlap (J. Cog. Neurosci.) | §5 | 🟢 fMRI |
| R25 | Gallese 2003, 2005 — Embodied simulation, shared manifold | §0 | 🟢 |
| R26 | Dimaggio & Lysaker 2015 — Metacognition + mentalizing coupled | §0 | 🟢 |
| R27 | Uddin, Iacoboni et al. 2007 — Self/other neural overlap | §6 | 🟢 fMRI |

---
