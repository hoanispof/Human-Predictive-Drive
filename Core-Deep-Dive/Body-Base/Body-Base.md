---
title: Body-Base — Entry Point cho Toàn Bộ Body-Base System
version: 3.2
created: 2026-04-14 (v1.0 BASIC — Phase C)
rewritten: 2026-05-16 (v3.0 — Phase 4 ALL REWRITE: 3 Hardware Foundations, Compilable Architecture, Body-Need 2-source, Compiled/Fresh axis, L3→PFC Operators reframe, 3-Layer Evolution, cross-refs updated)
refined: 2026-05-17 (v3.1 — §7 REWRITE: 4-Tier → 2-Tier + 2-Pathway calibration model. Aligned with Why-Body-Knows.md v1.1)
refined: 2026-05-23 (v3.2 — Concept Cascade: +Simulation-Engine, +Entity-Access, +Entity-Compiled, +Bond-Architecture, +Hardware Subsidy, +M1-M4, +Satiation, +Resonance-Sustainability, +By-Product-Scale, +Resonance-Per-Entity. Updated versions + deps + §0 flow + §10 reading guide + §12 cross-refs)
previous: v3.1 (inline — no backup needed, additive changes only)
status: v3.2 REFERENCE FILE
scope: |
  ENTRY POINT cho toàn bộ Body-Base/ folder (~60+ files).
  Body-Base LÀ GÌ + 3 Hardware Foundations + Compilable Architecture +
  Core Principles + Unified Model 3+1 + L0-L1 Substrate +
  Body Compile + Compiled/Fresh Axis + Body-Need 2-Source +
  3-Layer Evolution + 2-Tier Calibration + Circuit Breaker +
  Body-Feedback Overview.
  v3.0 KEY CHANGES từ Inter-Body Drill (8 principles):
    ① 3 Hardware Foundations → Compilable Architecture (WHY body works this way)
    ② Body-Need 2-source aggregate (hardware + chunk dynamics)
    ③ Compiled vs Fresh = Real Axis (NOT Feeling/Logic content)
    ④ 3-Layer Evolution (Hardware → Compiled → Cultural)
    ⑤ L3→PFC Operators: Protect = observation parameter, NOT operator
    ⑥ Updated cross-refs to Phase 1-3 outputs
  v3.1 KEY CHANGE:
    ⑦ §7: 4-Tier → 2-Tier + 2-Pathway (only 2 MECHANISMS: Darwinian + Hebbian)
    ⑧ Aligned with Why-Body-Knows.md v1.1 (2-tầng + 2 đường reframe)
  v3.2 KEY CHANGES (Concept Cascade from 28-session Drill Propagation):
    ⑨ Deps + versions updated for ~15 new/rewritten files
    ⑩ §0 flow diagram: +Simulation-Engine, +Agent-Mechanism sub-files
    ⑪ §1.3: +Satiation types, +Gap-Body-Need reference
    ⑫ §3: +Simulation Engine (PFC), +Entity-Access (Trust), +Bond-Architecture
    ⑬ §4: +Entity-Compiled formal file reference
    ⑭ §10: Reading Guide comprehensive update (Agent-Mechanism/ 11 files)
    ⑮ §12: +15 new cross-references
purpose: |
  Người đọc NÊN ĐỌC FILE NÀY TRƯỚC khi đi vào bất kỳ sub-file nào.
  File này consolidate, KHÔNG duplicate — detail ở sub-files.
  Foundation layer cho TOÀN BỘ framework.
previous_version: backup/Body-Base-v2.1-backup.md
parent: Core-Deep-Dive/ (foundation file)
dependencies:
  - Why-Body-Knows.md v1.1 — 2-tier + 2-pathway calibration, coherence ≠ truth
  - Body-Feedback/Body-Feedback.md — Dual-Pull, H10, Interface Loop
  - Body-Feedback/01-Foundation.md — body-feedback vs feeling 2-layer
  - Body-Feedback/Body-Feedback-Mechanism.md v2.0 — chunk dynamics, Body-Need aggregate
  - Body-Feedback/Gap-Body-Need.md v1.0 — 3 satiation types, ENGINE/ROAD/VEHICLE, entity-gap matching
  - Feeling/Feeling.md v2.0 — 7-layer fidelity, PFC observation
  - Chunk/Chunk.md v2.0 — sole substrate, 4 compile mechanisms
  - Valence-Propagation.md v3.0 — structural/current valence, 3 firing modes, hardware subsidy, per-entity
  - Body-Coupling.md v3.0 — coupling mechanism, 4 bond types, hardware subsidy, M1-M4
  - Cortisol-Baseline.md v2.0 — amplifier, direction > level
  - PFC/PFC-Function.md — 24 functions, 95/5 split
  - PFC/Simulation-Engine.md v1.0 — 1 engine, 3 components, N applications
  - PFC/PFC-Label.md v1.0 — vocabulary reference, 13 domains, 3-tier labels
  - Neural-Architecture.md — A/B/C/D 4-zone physical map
  - Inter-Body-Mechanism.md v1.0 — 8 drill principles
  - Body-Feedback/Body-Feedback-Label.md v2.0 — vocabulary reference
  - Chunk/Agent-Mechanism/Self-Pattern-Modeling.md v3.1 — solo simulation, 1 mech × 3 dims
  - Chunk/Agent-Mechanism/Entity-Compiled.md v1.0 — neural reality, formation 40→200h, Dunbar
  - Chunk/Agent-Mechanism/Entity-Access.md v1.2 — gradient model, Mức 0-5, per-entity
  - Chunk/Agent-Mechanism/Bond-Architecture.md v1.0 — 1 mechanism × 4 bond types, M1-M4
  - Chunk/Agent-Mechanism/By-Product-Gap-Resonance.md v1.4 — mutual match, 5 drills
  - Chunk/Agent-Mechanism/Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions, 3 modalities
  - Chunk/Agent-Mechanism/By-Product-Scale.md v1.0 — 1 mechanism × 3 scales
  - Chunk/Agent-Mechanism/Resonance-Per-Entity.md v1.0 — per-relationship, hardware subsidy spectrum
  - Chunk/Agent-Mechanism/Entity-Access-Excess.md v1.0 — excess territory, addiction
  - Chunk/Agent-Mechanism/Entity-Access-Calibration.md v1.0 — self-regulation, hardware subsidy
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Base — Entry Point cho Toàn Bộ Body-Base System

> **Bạn khát nước → body thiếu hydration.**
> **Bạn cô đơn dù xung quanh đầy người lạ → body thiếu agent depth.**
> **Bạn nghe bài nhạc MỚI → body biết "hay" TRƯỚC PFC.**
> **Bạn bị phản bội → valence flip NGAY dù PFC chưa kịp phân tích.**
> **Bạn "cho đi vô tư" → compiled patterns (trust, coupling, norms) fire tự động — body CÓ lý do, PFC chỉ thấy "vô tư".**
>
> Tất cả đều là **body-base** — hệ thống nền tảng mà MỌI THỨ trong framework
> chạy trên đó. Body phản ứng trước. PFC observe sau. Thứ tự KHÔNG bao giờ đảo ngược.
>
> **Core principles (v3.0):**
> Body evaluates PATTERNS, not reality.
> PFC = director. Body = compiler.
> Trust = bridge duy nhất cho complexity vượt 4±1.
> External tools = capacity multiplier ×∞.
> 3 Hardware Foundations → Compilable Architecture (general-purpose adaptive).
>
> **"Con người cần FEEL đúng → AI sẽ giúp PLAN đúng."**

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — BODY-BASE LÀ GÌ
- §2 — CORE PRINCIPLE: Body Evaluates Patterns, Not Reality
- §3 — UNIFIED MODEL: 3 Components + 1 Bridge
- §4 — BODY COMPILE + COMPILED/FRESH AXIS
- §5 — L0-L1 SUBSTRATE
- §6 — 3-LAYER EVOLUTION
- §7 — 2-TIER CALIBRATION (2 cơ chế + 2 đường vào)
- §8 — CIRCUIT BREAKER MECHANISM
- §9 — BODY-FEEDBACK OVERVIEW
- §10 — READING GUIDE CHO BODY-BASE/ FOLDER
- §11 — HONEST ASSESSMENT
- §12 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
⭐ BODY-BASE = FOUNDATION LAYER CỦA TOÀN BỘ FRAMEWORK:

  Mọi thứ build trên body-base:
    → Chunks compile TRÊN body-base substrate
    → Feelings emerge TỪ body-chunk interaction
    → Drives operate TRÊN body-base signals
    → Schemas serve BODY-BASE (không phải ngược lại)
    → PFC observes BODY-BASE output (không feel trực tiếp)

  Conceptual layer stack:
    [PFC OBSERVATION]       ← Feeling (PFC observe body-chunk interaction)
    [SCHEMAS, CHUNKS]       ← Compiled patterns (sole substrate)
    [L1 BODY-INPUTS]        ← Body-Base substrate (17 sub-categories)
    [L0 ALIVE THRESHOLD]    ← Survival floor (binary)
    [3 HARDWARE FOUNDATIONS] ← General-Purpose Reward + Compilation + Social Hardware

  PFC-mediated drives (Novelty, Status) = OPERATORS on L1 substrate.
    → Shift baselines, create expectations, generate dissonance
    → Operate ON body-base — NOT a separate layer
    → Protect = observation parameter, KHÔNG phải operator (Protect.md §0)

  BODY-NEED = aggregate output CỦA body-base signals:
    → Hardware/sensory + chunk dynamics → body-need (Body-Feedback-Mechanism v2.0 §1)
    → PFC KHÔNG luôn biết body-need hiện tại
    → Chi tiết: Inter-Body-Mechanism.md §2


FILE NÀY TRONG FLOW:

  ┌───────────────────────────────────────────────────────────────┐
  │ BODY-BASE.MD (FILE NÀY) — ENTRY POINT                        │
  │                                                                │
  │  Đọc file này TRƯỚC → chọn hướng đi sâu:                     │
  │                                                                │
  │  Mechanism files (HOW):                                        │
  │    Chunk/Chunk.md v2.0             — chunk system (sole substrate)│
  │    Body-Feedback-Mechanism.md v2.0 — chunk dynamics, Body-Need│
  │    Valence-Propagation.md v3.0     — structural/current valence, 3 firing modes│
  │    Body-Coupling.md v3.0           — coupling, 4 bond types, hardware subsidy│
  │    Cortisol-Baseline.md v2.0       — amplifier mechanism       │
  │    Inter-Body-Mechanism.md v1.0    — inter-body 8 principles  │
  │                                                                │
  │  Agent-Mechanism files (PER-ENTITY):                           │
  │    Self-Pattern-Modeling.md v3.1   — solo simulation, 1 mech × 3 dims│
  │    Entity-Compiled.md v1.0         — neural reality, formation, Dunbar│
  │    Entity-Access.md v1.2           — gradient model, Mức 0-5  │
  │    Bond-Architecture.md v1.0       — 1 mechanism × 4 bond types│
  │    By-Product-Gap-Resonance.md v1.4 — mutual match, sustainability│
  │    Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions   │
  │    Resonance-Per-Entity.md v1.0    — per-relationship dynamics │
  │    By-Product-Scale.md v1.0        — 1 mech × 3 scales        │
  │                                                                │
  │  Observation files (WHAT PFC SEES):                            │
  │    Feeling/Feeling.md v2.0         — PFC observation interface │
  │    Body-Feedback/                  — signal architecture        │
  │    Body-Feedback/Gap-Body-Need.md v1.0 — 3 satiation types    │
  │                                                                │
  │  Foundation files (WHY):                                       │
  │    Why-Body-Knows.md               — tại sao body đáng tin     │
  │    Neural-Architecture.md          — physical brain map         │
  │                                                                │
  │  PFC files (WHAT DIRECTS):                                     │
  │    PFC/PFC-Function.md             — 24 PFC functions          │
  │    PFC/PFC-Hardware.md             — hardware variation         │
  │    PFC/Simulation-Engine.md v1.0   — 1 engine, 3 components   │
  │    PFC/PFC-Label.md v1.0           — vocabulary, 3-tier labels │
  └───────────────────────────────────────────────────────────────┘
```

---

## §1 — BODY-BASE LÀ GÌ

### §1.1 — Formal Definition

```
⭐ BODY-BASE = HỆ THỐNG NỀN TẢNG MÀ MỌI PROCESSING CHẠY TRÊN ĐÓ:

  Body-Base bao gồm:
    → L0: Alive threshold (binary — sống hoặc chết)
    → L1: 17 body-input substrates với adaptive baseline
    → Trên L0+L1: chunks compile, schemas form, feelings emerge

  Body-Base KHÔNG phải "physical needs" narrow:
    → KHÔNG chỉ đói/khát/ngủ (Maslow hierarchy)
    → BAO GỒM: social inputs, aesthetic inputs, cognitive inputs
    → "Cô đơn" = body-base signal thật (L1 social input deficit)
    → "Chán" = body-base signal thật (L1 novelty baseline unmet)
    → "Nhạc hay" = body-base coherence reward thật

  Body-Base là SOURCE:
    → Schema phục vụ body-base (Drill §23, PFC-Function §9)
    → Reward = body decides, PFC observes
    → PFC KHÔNG tạo feeling — PFC observe body-chunk interaction
    → = Feeling.md v2.0: "Feeling = WHAT PFC SEES"
```

### §1.2 — 3 Hardware Foundations → Compilable Architecture

```
⭐ MỌI THỨ TRONG BODY-BASE EMERGE TỪ 3 FOUNDATIONS (Inter-Body §1):

┌─────────────────────────────────────────────────────────┐
│ ① GENERAL-PURPOSE REWARD                                │
│                                                         │
│   VTA/dopamine + opioid system.                         │
│   Fire cho BẤT KỲ gap fill đúng direction.              │
│   KHÔNG check content ("edible?" → irrelevant).         │
│   Chỉ check: "gap direction matched?"                   │
│                                                         │
│   → Einstein solve equation = body reward THẬT           │
│   → Vì body-need KHÔNG chỉ survival                    │
│   → Body-need = ANY compiled gap fill                   │
│                                                         │
│   🟢 Schultz 1997: VTA prediction error                  │
│   🟢 Berridge 2003: opioid = liking mechanism            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ② COMPILATION CAPABILITY                                │
│                                                         │
│   Hebbian: "whatever works → strengthen → automatic"    │
│   Fresh → repeat + verify → compile → "cảm thấy"       │
│   Body LEARN from experience, without conscious plan    │
│                                                         │
│   → Skill: lái xe ngày 1 vs ngày 1,000                  │
│   → Social: stranger → bạn thân qua 10 năm             │
│   → Expert: therapist 1,000 cases → "trực giác"         │
│     (= compiled patterns, Klein 1998)                    │
│                                                         │
│   🟢 Hebb 1949: Hebbian learning                         │
│   🟢 Klein 1998: recognition-primed decisions            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ③ SOCIAL HARDWARE                                       │
│                                                         │
│   Oxytocin: fire khi touch, eye contact, trust          │
│   μ-opioid: social play reward = same system as food    │
│   dACC reuse: social pain = physical pain circuits      │
│   Social = DEFAULT state (body RELAXES with others)     │
│   Alone = DEVIATION → extra energy required             │
│                                                         │
│   🟢 Eisenberger 2003: social-physical pain overlap      │
│   🟢 Panksepp 1998: μ-opioid in social play             │
│   🟢 Coan & Sbarra 2015: Social Baseline Theory         │
└─────────────────────────────────────────────────────────┘


KẾT HỢP ①②③ = COMPILABLE ARCHITECTURE:

  HARDWIRED ARCHITECTURE (specific-reward — côn trùng, đơn giản):
    Hardwired circuits: food→reward, mate→reward, escape→reward
    ƯU: nhanh, chính xác cho environment ổn định
    NHƯỢC: environment thay đổi → species die

  COMPILABLE ARCHITECTURE (general-purpose — humans):
    Hardwired: CHỈ reward MECHANISM + compilation + social + PFC
    Content: LEARN from environment/culture → compile → body-need
    ƯU: adapt BẤT KỲ environment
    NHƯỢC: cần 15-20 NĂM compile (long childhood)

  → Trade-off: CẦN parents + group protect trong 15-20 năm compile
  → = TẠI SAO social = architecture requirement, NOT luxury

  4 LÝ DO social = requirement:
    ① Survival math: alone → phải tự làm ALL → die
    ② Compilation: child alone = chậm + nguy hiểm; in group = nhanh + an toàn
    ③ Neural circuit reuse: dACC social = physical pain (Eisenberger 2003)
    ④ Social Baseline: alone = deviation, with others = baseline (Coan 2015)

🟡 Hardwired/Compilable Architecture naming = framework synthesis.
   Underlying neuroscience (general-purpose reward, Hebbian, social circuits) = 🟢.

Chi tiết: Inter-Body-Mechanism.md §1
```

### §1.3 — Body-Need: 2-Source Aggregate

```
⭐ BODY-NEED = TỔNG HỢP TRẠNG THÁI CẦN HIỆN TẠI (Body-Feedback-Mechanism v2.0 §1):

  2 GENUINE SOURCES:
    ① Hardware/Sensory-Driven: đói, khát, đau, nhiệt, oxy, ngủ
    ② Pattern-Driven (chunk dynamics): Shift/Miss/Gap + compound

  Cross-cutting (KHÔNG phải source — modify, không tạo):
    → Observation parameters: Novelty, Status, Protect
    → State modifiers: cortisol, sleep debt, hormones

  7 PROPERTIES:
    ① Multi-source aggregate   ② Always-on (24/7)
    ③ PFC KHÔNG luôn biết     ④ General-purpose (Compilable Architecture)
    ⑤ Driven by gap direction  ⑥ State-dependent intensity
    ⑦ Có thể bị hijack (hormone, scam)

  Body-need = WHY body drives behavior.
  PFC observes body-need SAU khi nó đã form.
  Nhiều hành vi "vô tư" = body-need running mà PFC chưa đặt tên.

  SATIATION — 3 TYPES (Gap-Body-Need.md v1.0):
    Body-need KHÔNG chỉ "có hoặc không" — có 3 kiểu satiation khác nhau:
    ① ENGINE satiation: cơ chế tạo gap mệt/giảm (VD: dopamine receptor downregulation)
    ② ROAD satiation: đường gap fill quen quá → cần path mới (VD: nhạc cũ nhàm)
    ③ VEHICLE satiation: entity cụ thể bão hòa (VD: ăn phở 7 ngày liên tiếp)
    → Mỗi type → khác intervention. Nhầm type = fix sai.
    → Entity-gap matching: mỗi gap có entity phù hợp riêng (Gap-Body-Need.md §4)

Chi tiết: Body-Feedback-Mechanism.md v2.0 §1, Inter-Body-Mechanism.md §2, Gap-Body-Need.md v1.0
```

### §1.4 — Architectural Claim: Schema Phục Vụ Body-Base

```
🟡 FRAMEWORK COMMITMENT (PFC-Function §9, Drill §23):

  Schema phục vụ body-base. Body-base là NGUỒN GỐC reward/dissonance.

  KHÔNG phải:
    ❌ "Schema drives behavior, body is output"
    ❌ "PFC decides, body follows"
    ❌ "Rational agent với body as constraint"

  LÀ:
    ✅ "Body drives, schemas serve"
    ✅ "Vô thức primary, PFC observer + director"
    ✅ "Embodied agent với PFC as extended capability"

  Evidence:
    → VTA/Opioid split: VTA = chuông cửa (attention). Opioid = quà thật (body-base match).
    → PFC send chunks → body verify → opioid release nếu match body-need.
    → Body is FINAL ARBITER of value. PFC is gateway, not source.
    → 🟢 Berridge 2003: wanting (dopamine) ≠ liking (opioid)
    → 🟢 Damasio 1994: somatic markers guide decisions

  Corollary: Reward = PERSONALIZED
    → Same stimulus → different person → different chunks base → different reward
    → "Ô tô paradox" (Body-Feedback.md §7.1): same car → 5 opposite reactions
    → Reward = f(object, person's chunks, pending needs, history)
```

---

## §2 — CORE PRINCIPLE: Body Evaluates Patterns, Not Reality

```
⭐ BODY RESPONDS TO f(PATTERN FIRE), NOT f(INPUT CAUSE):

  Drill §21 — "Body Responds to Patterns, Not Causes" — 7 converging cases:

  NEUROSCIENCE FOUNDATION:
    🟢 Treisman 1977 "poison theory":
      Motion sickness = nausea mechanism triggered BY WRONG INPUT.
      Vestibular ≠ vision → same Area Postrema fires as ACTUAL poison.
      Body KHÔNG biết "đây là xe chạy, không phải chất độc."
      Body biết: "PATTERN nausea đang fire → respond."

    🟢 Sensory conflict theory:
      Mismatch signals (tai nói động, mắt nói tĩnh) → activate CÙNG
      chemoreceptor zone + nucleus → CÙNG nausea response.
      → = CÙNG neural pathway cho poison VÀ motion sickness.

  6 SUPPORTING CASES:
    ① Phantom limb pain: KHÔNG có chân → pattern VẪN fire → đau thật
    ② Placebo nausea: đường → installed pattern fire → nôn thật
    ③ Moral disgust: KHÔNG có độc → same insula fire → "buồn nôn" thật
    ④ Anxiety nausea: KHÔNG có chất độc → fear pattern → nôn thật
    ⑤ Vicarious nausea: empathy pattern → nôn thật khi NHÌN người khác nôn
    ⑥ Morning sickness: PREDICTIVE pattern fire TRƯỚC actual toxin

  3 CƠ CHẾ CỤ THỂ:
    ① Habituation/compilation: repeated exposure → compile [mismatch] = normal → no signal
    ② Threshold modulation: hungry/tired → lower threshold → same mismatch = stronger nausea
    ③ Conditioned valence: smell of car → conditioned nausea TRƯỚC actual motion (Pavlovian)


  ⭐ UNIFIED PRINCIPLE:

    Body evaluate PATTERNS (compiled chunks fire), KHÔNG evaluate REALITY (actual causes).

    Drill §6b + §21 = CÙNG PRINCIPLE, 2 góc nhìn:
      §6b: Body checks OUTPUT (hành vi → body-feedback), not CHAIN LOGIC
      §21: Body responds to PATTERN FIRE, not INPUT CAUSE

    → = Body = pattern evaluator. NOT reality checker.
    → = TẠI SAO body "biết" (phần lớn patterns align reality qua evolution)
    → = TẠI SAO body "sai" (khi patterns misalign reality — evolution lag, chunks nền sai)
    → = Coherence ≠ Truth (Why-Body-Knows.md §3)

    → Body đúng ~90%+ (patterns calibrated qua 2 cơ chế — §7 below)
    → Body sai ở ~10% (evolution lag, chunks nền sai, schema override)
    → External check cần thiết cho 10% gap: người khác, AI, domain thật


🟢 Research support:
  Treisman 1977 (poison theory), Reason & Brand 1975 (sensory conflict),
  Ramachandran & Rogers-Ramachandran 1996 (phantom limb),
  Benedetti 2014 (placebo/nocebo), Chapman & Anderson 2012 (moral disgust insula)

🟡 Framework synthesis:
  "Body evaluates patterns not reality" = unifying principle across all domains
  (music, empathy, morality, threat, coupling) — novel integration.
```

---

## §3 — UNIFIED MODEL: 3 Components + 1 Bridge

```
⭐ MODEL 3+1 (Drill §23 — Unified Model):

  Toàn bộ framework phenomena = COMBINATIONS của 3 components + 1 amplifier.
  Không cần mechanism mới. Mọi thứ = variation/scale/combination.


  ┌─────────────────────────────────────────────────────────────────┐
  │ COMPONENT 1 — VÔ THỨC: COMPILE + FIRE + EVALUATE               │
  │                                                                  │
  │   CÓ THỂ:                                                       │
  │     → Compile patterns từ experience                             │
  │     → Fire compiled schemas tự động                              │
  │     → Evaluate body state (coherence check)                      │
  │     → Create expectancy patterns (prediction)                    │
  │     → Deliver rewards (opioid) / punishments (cortisol signal)   │
  │                                                                  │
  │   KHÔNG THỂ:                                                     │
  │     → Chain novel logic (chỉ fire compiled sequences)            │
  │     → Check domain accuracy (chỉ check coherence)               │
  │     → Simulate future intentionally (PFC does this)              │
  │     → Compare memories intentionally (PFC hold + compare)        │
  │                                                                  │
  │   ~95% behavior. 24/7. No novel chaining.                        │
  │   3 things LOOK like chaining (thực ra không phải):              │
  │     ① Compiled sequence replay (single meta-chunk)               │
  │     ② Associative spreading (follow strongest links)             │
  │     ③ Incubation (parallel combination + coherence eval)         │
  ├─────────────────────────────────────────────────────────────────┤
  │ COMPONENT 2 — PFC: DIRECT + SEQUENCE + OBSERVE                  │
  │                                                                  │
  │   DIRECT: allocate attention, active lock (hold+cortisol),       │
  │           hijack body-input                                      │
  │   SEQUENCE: plan (arrange chunks), compare (hold 2+ options),    │
  │             choose (select competing paths)                      │
  │   HOLD: working memory 4±1 slots                                 │
  │   OBSERVE: monitor body state, verify, domain-check              │
  │   FACILITATE: imagination, creation (combine chunks mới)         │
  │   INHIBIT: impulse control (suppress compiled responses)         │
  │                                                                  │
  │   ~5% behavior. NONE process content.                            │
  │   PFC = conductor (không chơi nhạc cụ, chỉ điều phối dàn nhạc). │
  │   Specialty: novel sequencing (sắp xếp tổ hợp chưa compiled).   │
  │                                                                  │
  │   SIMULATION ENGINE = formalized PFC mechanism:                  │
  │     Interoceptive Model × Simulation × Self-Pattern-Modeling = 1 engine           │
  │     Chi tiết: Simulation-Engine.md v1.0                          │
  │                                                                  │
  │   24 functions chi tiết: PFC-Function.md                         │
  ├─────────────────────────────────────────────────────────────────┤
  │ COMPONENT 3 (BRIDGE) — TRUST: GATE + MODULATE + CONNECT         │
  │                                                                  │
  │   Trust = per-entity meta-tag trên chunks (Valence-Propagation v3.0 §2).         │
  │   MỌI trust sources (bản thân, cha mẹ, thầy, tập thể, hệ thống)│
  │   dùng IDENTICAL mechanism — khác verification path.             │
  │                                                                  │
  │   3 FUNCTIONS:                                                   │
  │     GATE: trust = cổng cho external install chunks               │
  │     MODULATE: trust modulate TOÀN BỘ valence profile             │
  │     CONNECT: trust = ONLY mechanism cho complexity > 4±1          │
  │                                                                  │
  │   ENTITY-ACCESS GRADIENT = formalized trust model:               │
  │     Mức 0 (stranger) → Mức 5 (self/child)                       │
  │     Trust ≠ binary → gradient per-entity                         │
  │     Chi tiết: Entity-Access.md v1.2                              │
  │                                                                  │
  │   BOND-ARCHITECTURE = 4 bond types qua 1 mechanism:             │
  │     Proximity / Shared-Experience / Reciprocal / Identity        │
  │     Entity-Compiled = neural reality, KHÔNG phải metaphor        │
  │     Chi tiết: Bond-Architecture.md v1.0, Entity-Compiled.md v1.0│
  │                                                                  │
  │   Tại sao Trust = Bridge, không phải component:                  │
  │     → Trust KHÔNG process — trust ENABLE processing              │
  │     → Verify một số → trust phần còn lại → build recursively    │
  │     → Không có trust → mỗi người stuck ở ~4±1 per session       │
  ├─────────────────────────────────────────────────────────────────┤
  │ AMPLIFIER — EXTERNAL TOOLS: ×∞ CAPACITY                         │
  │                                                                  │
  │   Paper, pen, books, computers, AI = extend BEYOND:              │
  │     → PFC capacity (4±1) → ×∞ via external storage              │
  │     → Trust range → ×∞ via accumulated collective knowledge      │
  │                                                                  │
  │   Hierarchy: PFC 4±1 → ×4 via vô thức compression →             │
  │              ×∞ via external tools                                │
  │                                                                  │
  │   Civilization = compound stacking of 3+1.                       │
  └─────────────────────────────────────────────────────────────────┘


  BB1 + BB2 CONVERGENCE (Drill §26 D1):

    Blackbox 1 (chunk substrate) + Blackbox 2 (valence complexity)
    = KHÔNG PHẢI 2 blackbox riêng biệt.
    = CÙNG 1 mechanism ở behavioral level:
      Compile = structural aspect (patterns form)
      Valence = evaluative aspect (patterns get tagged)
      → XẢY RA ĐỒNG THỜI, không tuần tự.

    BB2 = BB1 + collective scale + hardware variance.
    BB1 ⊂ BB2 ⊂ Model 3+1.

    Chi tiết convergence: Drill-Compile-Short-Collective.md §26,
    Blackbox-Map.md §4.2 (supersedes Framework-Boundaries.md v2.0).
```

---

## §4 — BODY COMPILE + COMPILED/FRESH AXIS

### §4.1 — PFC ≠ Compiler

```
⭐ PFC KHÔNG COMPILE. BODY LUÔN LÀ COMPILER (Drill §19):

  PFC CÓ 5 VAI TRÒ (KHÔNG vai trò nào là compile):

    ① DIRECT attention: chọn focus vào đâu
    ② HOLD ~4 chunks: giữ active trong working memory
    ③ IMAGINE scenarios: combine chunks → simulate chưa xảy ra
    ④ DOMAIN-CHECK: verify body-smooth vs reality
    ⑤ CHANGE ENVIRONMENT: thay đổi context → body-input thay đổi

  BODY COMPILE qua 4 mechanisms (Chunk.md §2):
    ① Repetition — lặp lại nhiều lần (LTP, Bliss & Lømo 1973 🟢)
    ② Emotional peak — 1 lần cảm xúc cực mạnh (Brown & Kulik 1977 🟢)
    ③ Multi-modal — nhiều kênh cùng lúc (wire across cortex)
    ④ Sleep consolidation — offline integration (Walker 2017 🟢)

  IMAGINATION = NỘI BỘ BODY EXPERIENCE (Drill §19 key insight):
    → Imagine chanh → tiết nước bọt THẬT (body respond)
    → Imagine solving → opioid THẬT (reward thật)
    → Imagination IS body experience, chỉ THẤP HƠN direct input
    → = Boundary "PFC create" vs "body compile" KHÔNG tồn tại
    → = PFC direct + body compile = always collaborative, never separate

  EINSTEIN TEST CASE:
    → PFC directed attention (vật lý Newton mâu thuẫn ở ĐÂU)
    → PFC held chunks (đồng hồ, ánh sáng, khung tham chiếu)
    → PFC imagined scenarios (ngồi trên tia sáng)
    → NHƯNG: compilation = body mechanisms (sleep, incubation, coherence eval)
    → Body coherence evaluation → "E=mc² ĐÚNG" → opioid → eureka
    → PFC directed. Body compiled.

  SPECTRUM:
    Infant:   pure body compile, minimal PFC direction
    Adult:    body compile + PFC direction ~5%
    Expert:   body compile + PFC direction refined + compiled meta-chunks
    Einstein: body compile + PFC direction CỰC refined
    → MỌI mức = body compile. PFC chỉ thay đổi QUALITY of direction.

  🟡 Principle: "PFC tạo CONTEXT, B+C+D tự học" (PFC-Function §9)
```

### §4.2 — 3 Compile Types

```
🟡 3 COMPILE TYPES (Drill §3 — chi tiết: Compile-Taxonomy.md E4):

  EXPERIENCE COMPILE — DIRECT SHORT (~90% daily behavior):
    → Body experience → body compile → chunks form
    → PFC KHÔNG hoặc ÍT tham gia direction
    → VD: habit, skill, routine, emotional conditioning
    → = Phần lớn cuộc sống = Experience Compile

  EXPERTISE COMPILE (~5%):
    → PFC-directed compile qua nhiều năm
    → PFC chọn domain + hold + imagine + domain-check
    → Body compile THROUGH PFC direction
    → VD: Einstein physics, chess grandmaster, surgeon skill
    → = Expertise Compile

  TRUST COMPILE — INSTALLED + COLLECTIVE:
    → Chunks installed TỪ BÊN NGOÀI (cha mẹ, thầy, sách, AI, văn hóa)
    → 5 external install mechanisms (Chunk.md §2.3):
      Co-attention, Imitation, Social referencing,
      Label installation, Cultural transmission
    → = PHẦN LỚN behavior hàng ngày mà framework CHƯA nhận ra đủ
    → VD: ngôn ngữ, đạo đức, skill xã hội, world knowledge
    → = Trust Compile = collective hold chain dài, individual compile short

  ⚠️ TRUST = GATE CHO TRUST COMPILE (Drill §4, §20):
    → Cá nhân KHÔNG tự compile chain dài (PFC 4±1 constraint)
    → Tập thể HOLD chain dài (distributed across many individuals)
    → Cá nhân NHẬN từ tập thể qua TRUST gate
    → Trust cao → chunks install. Trust thấp → chunks reject.
    → Entity-Access.md v1.2: trust = gradient Mức 0-5 per-entity
    → Entity-Access-Calibration.md v1.0: self-regulation mechanism

  ENTITY-COMPILED = NEURAL REALITY (Entity-Compiled.md v1.0):
    → Khi compile đủ sâu (40-200h), entity CÓ THẬT trong não
    → Hub-and-spoke: amygdala/hippocampus/PFC form per-entity network
    → Dunbar ~150: giới hạn Entity-Compiled capacity
    → Grief Type A/B/C: mất Entity-Compiled = mất neural reality
    → Entity-Compiled = mechanism chung cho CẢ 3 Compile Types trên

  Chi tiết taxonomy: Compile-Taxonomy.md (E4 — chưa viết)
```

### §4.3 — Compiled vs Fresh = Real Axis

```
⭐ TRỤC THẬT: COMPILATION LEVEL (Inter-Body §3)

  Framework uses Compiled = "Feeling", Fresh = "Logic."
  Deeper reality:
    Compiled = automatic processing (body-feedback direct, cost ≈ 0)
    Fresh = PFC deliberate draft (costly, not yet compiled)

  "Feeling" và "Logic" = LABELS from observer perspective.
  Inside body: chỉ có COMPILED ←→ FRESH spectrum.
  Content (emotion/reasoning) KHÔNG quyết định Compiled/Fresh.
  COMPILATION LEVEL quyết định.

  ┌──────────────────────┬──────────────────────────┐
  │ COMPILED                   │ FRESH                       │
  ├──────────────────────┼──────────────────────────┤
  │ Automatic            │ Deliberate               │
  │ Body-direct feedback │ PFC-mediated             │
  │ Cost ≈ 0             │ Cost > 0                 │
  │ "Cảm thấy"          │ "Nghĩ ra"                │
  │ Hebbian reinforced   │ Mỗi lần = effort         │
  │ Tức thời             │ Cần thời gian            │
  └──────────────────────┴──────────────────────────┘

  Evidence — content ≠ processing level:
    ① Einstein + toán quen = COMPILED (content "logic" nhưng automatic)
    ② Stranger đoán cảm xúc người lạ = FRESH (content "feeling" nhưng deliberate)
    ③ Chef nếm → biết ngay thiếu muối = COMPILED (complex content, instant)
    ④ Therapist gặp case mới = FRESH (content "feeling" nhưng phải phân tích)

  Transition cả 2 chiều:
    FRESH → COMPILED (Learning): lặp + verify → Hebbian → automatic
    COMPILED → FRESH (Unlearning): disrupted → phải suy nghĩ lại

  "Logic" vs "Intuition" = naming artifact:
    → "Logic" = compiled chunks SHAREABLE (toán: mọi người cùng kết quả)
    → "Intuition" = compiled chunks NON-SHAREABLE (therapy: mỗi chuyên gia khác)
    → BÊN TRONG: CƠ CHẾ GIỐNG HỆT (compiled automatic processing)

🟡 Compiled/Fresh reframe = framework synthesis.
   Consistent with Kahneman 2011 System 1/2, Klein 1998 (🟢).

Chi tiết: Inter-Body-Mechanism.md §3, Self-Pattern-Modeling.md v2.4 §2
```

---

## §5 — L0-L1 SUBSTRATE

### §5.1 — L0 Alive Threshold

```
🟢 L0 — BINARY SURVIVAL FLOOR:

  Threats that cross L0 = death:
    Oxygen deprivation     — minutes
    Critical injury        — immediate
    Extreme temperature    — hours
    Water deprivation      — days
    Starvation            — weeks

  L0 properties:
    → BINARY (có/không). Không graded.
    → Suppresses ALL other processing khi threatened
    → Single-track survival response
    → Spinal cord + brainstem handle (D zone — fastest)
    → PFC offline (NE α1 flood — circuit breaker design feature)
```

### §5.2 — L1 Body-Inputs với Adaptive Baseline

```
🟡 L1 — 17 SUB-CATEGORIES CỦA BODY-INPUTS:

  Mỗi input: evolved baseline (gen) + individual baseline (experience).
  Deviation below → dissonance. Above → reward → baseline shifts up.

  EXTEROCEPTION (5 inputs — external world):
    Vision, Audition, Olfaction, Gustation, Tactile

  PROPRIOCEPTION (3 inputs — body position):
    Proprioception, Vestibular, Kinesthetic

  INTEROCEPTION (9 inputs — internal state):
    Thermoreception (core temp), Nociception (pain),
    Respiratory, Cardiovascular, Visceral,
    Metabolic (đói/khát/năng lượng),
    Hormonal-sensed (cycle, cortisol subjective),
    Sleep/Circadian,
    ⭐ Self-signal interoception (META — keystone)

  ⭐ SELF-SIGNAL INTEROCEPTION = KEYSTONE (01-Foundation §5.4):
    → Body's capacity to READ its own internal state
    → Prerequisite cho feeling layer development
    → Compromise → silent deficit (alexithymia ~10% population)
    → TRAINABLE: meditation, Focusing, somatic therapy
    → 🟢 Craig 2002/2009, Garfinkel et al. 2015

  BASELINE ADAPTATION:
    → Hedonic treadmill (🟢 Brickman 1978): baseline shifts WITH sustained exposure
    → Novelty operator: shifts baselines UP → body cần MORE
    → Loss of elevated baseline → dissonance AT NEW FLOOR
    → Asymmetric: loss hurts ~2x gain (🟢 Kahneman & Tversky 1979)

  Chi tiết substrate: Body-Input-Enumeration.md (8,418L)
```

### §5.3 — PFC-Mediated Operators on L1

```
🟡 PFC DRIVES = OPERATORS ON L1 (không phải separate layer):

  v2.1 gọi "L3 PFC Drives" gồm Novelty/Status/Protect.
  v3.0 REFRAME: drives = PFC-mediated OPERATORS trên L1 substrate.
  Protect = observation parameter, KHÔNG phải operator.

  2 PRIMARY OPERATORS:

  ① NOVELTY:
    → Shifts L1 baselines UPWARD (explore, expand)
    → prediction-delta detection (🟢 Schultz 1997)
    → Cortisol LOW-MODERATE, domain-pull direction
    → Chi tiết: Observation/Novelty.md

  ② STATUS:
    → Resource Access Map (evolutionary grounded)
    → Status = PROXY for body-base resource access
    → 350M+ years cross-species
    → Chi tiết: Observation/Status.md

  ⚠️ PROTECT = OBSERVATION PARAMETER (Protect.md §0):
    → Protect = named pattern emergent từ compiled ownership chunks
      + asymmetric prediction-delta khi mất
    → KHÔNG phải operator — là TÊN GỌI cho patterns
    → v2.1 listed Protect as "L3 drive" → CORRECTED in v3.0

  HARDWARE SUBSIDY (Valence-Propagation v3.0 §5, Body-Coupling.md v3.0):
    → Body hardware cung cấp baseline support "miễn phí" cho operators
    → VD: oxytocin system → social reward KHÔNG cần PFC effort
    → Hardware Subsidy = TẠI SAO một số drives mạnh hơn hẳn
    → Khác nhau theo entity type: con > bạn thân > đồng nghiệp > stranger
    → = Evolutionary investment per-relationship

  M1-M4: 4 FIRING MODES (Bond-Architecture.md v1.0):
    → M1 Tonic: low-intensity, liên tục, duy trì baseline
    → M2 Phasic: burst cụ thể, response to event
    → M3 Compound: nhiều hệ fire ĐỒNG THỜI (VD: reunion = oxytocin+dopamine+opioid)
    → M4 Cascade: 1 event trigger chain nhiều systems theo thứ tự
    → Operators fire KHÁC NHAU tùy mode → cùng stimulus, khác response

  Operators ≠ layer:
    → Operate ON L1 body-inputs, SHIFT baselines
    → CREATE expectations, GENERATE dissonance
    → Chi tiết integration: Observation/Drive.md
```

### §5.4 — Modulatory vs Processing neurons: Parkinson validation

```
🟡 2 NHÓM NEURONS × FRAMEWORK LAYERS (Parkinson-Analysis.md §2):

  PROCESSING NEURONS (mạch CHÍNH):
    → Glutamate (excitatory) + GABA (inhibitory)
    → Xử lý thông tin + điều khiển hành vi
    → Vị trí: PFC, motor cortex, sensory cortex, hippocampus
    → = DÀN NHẠC (instruments chơi nhạc)

  MODULATORY NEURONS (mạch PHỤ):
    → Dopamine, Serotonin, NE, Acetylcholine
    → ĐIỀU CHỈNH gain/speed/gate cho mạch chính
    → Vị trí: SNc, VTA, raphe, locus coeruleus, basal forebrain
    → = AMPLIFIER + VOLUME CONTROL + NHẠC TRƯỞNG

  MAP VÀO L0-L1:
    L0 (Alive threshold):    brainstem = cả processing VÀ modulatory
    L1 (Body-inputs):        modulatory hệ regulate sensory processing
    PFC operators:           modulatory = operators (dopamine, NE, serotonin)
    PFC (observation):       processing neurons compute, modulatory fuel

  BRAAK STAGING VALIDATES ARCHITECTURE (Parkinson-Analysis.md §4.2):
    → α-synuclein ascending: gut → brainstem → midbrain → cortex
    → = L0 → L1 → PFC = CÙNG HƯỚNG ĐI LÊN
    → Stages 1-4: modulatory neurons chết (mạch phụ)
    → Stages 5-6: processing neurons bị (mạch chính)
    → = Mạch PHỤ chết TRƯỚC → mạch chính CÒN nhưng KHÔNG ĐƯỢC modulate
    → Parkinson: "BIẾT nhưng KHÔNG LÀM ĐƯỢC" = processing intact, gate locked

  🟢 Braak et al. 2003: 6-stage ascending pattern
  🟡 Modulatory/Processing × L0-L1 mapping = framework synthesis
```

---

## §6 — 3-LAYER EVOLUTION

```
⭐ 3 LAYERS STACKED, MỖI LAYER NHANH HƠN LAYER DƯỚI (Inter-Body §9):

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 1 — HARDWARE (genetic evolution):
  Speed: hàng nghìn → triệu năm
  Changes: sensory, muscle, brain size, hormone, neural circuits
  Examples: social pain circuits (dACC), oxytocin system, PFC expansion
  Mechanism: mutation → selection → reproduction
  = Foundation. Slow. Irreversible per generation.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 2 — COMPILED (individual learning):
  Speed: months → years (within 1 lifetime)
  Changes: chunk compilation, gap directions, valence profiles, skills
  Examples: Einstein compile physics, therapist compile patterns
  Mechanism: experience → body-feedback → Hebbian → compiled
  = Built ON hardware. Medium speed. Individual-specific.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 3 — CULTURAL (collective invention):
  Speed: days → decades (across generations, CUMULATIVE)
  Changes: knowledge, tools, institutions, symbols, norms
  Examples: language, money, writing, law, education, awards
  Mechanism: invention → transmission → adoption → accumulate
  = Built ON hardware + compiled. FASTEST. Cumulative across generations.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  "BOOST FEATURES" — Layer 3 accelerate Layers 1-2:
    Language ×100 — truyền chunks qua verbal
    Teaching ×10  — structured transmission → compile efficient
    Writing ×1000 — persist chunks BEYOND individual lifetime
    Money ×∞      — convert ANY contribution → survival resource
    Newton: "standing on shoulders of giants" = Layer 3 cumulative.

  MONEY = BRIDGE TECHNOLOGY:
    Doctor skill → money → food. Engineer → money → shelter.
    = WHY humans CAN pursue non-survival gap → still survive.
    Einstein: solve physics gap CỦA ÔNG → by-product = human knowledge
    → Collective benefit → pay back (salary, status)
    → Money BRIDGE: non-edible contribution → survival resources flow back

  DOUBLE INHERITANCE: genes (Layer 1) + culture (Layer 3)
    Group A: no cooperation → weak. Group B: Layer 3 tools → strong.
    10,000 years → MASSIVE Layer 3 stack.
    Modern professions (doctor, engineer, artist) = NONE genetically encoded.
    All = Layer 3 enabling Layer 2.

🟢 Boyd & Richerson 2005: dual inheritance (genes + culture).
🟢 Tomasello 2009: cumulative cultural evolution uniquely human.
🟡 3-layer model as unified framework = framework synthesis.

Chi tiết: Inter-Body-Mechanism.md §9
```

---

## §7 — 2-TIER CALIBRATION (2 cơ chế + 2 đường vào)

```
⭐ TẠI SAO BODY ĐÁNG TIN: 2 CƠ CHẾ CALIBRATE + 2 ĐƯỜNG VÀO
   (Why-Body-Knows.md v1.1 — consolidated):

  CHỈ 2 CƠ CHẾ THẬT SỰ KHÁC NHAU:

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TẦNG 1 — DARWINIAN SELECTION (gen-level, triệu năm):
    🟢 Triệu sinh vật × triệu năm × triệu thử nghiệm.
    → Gen "reward pattern đúng" → truyền. Gen "reward sai" → chủ nhân chết.
    → Body HIỆN TẠI = survivor's GPS — đã test triệu route, giữ route đúng.
    → VD: lửa=đau, ngọt=nutrition, rắn=nguy hiểm, social=reward (wired)
    → Unit: SPECIES population. Speed: nghìn-triệu năm.
    → = Cái bạn CÓ khi sinh ra, TRƯỚC mọi trải nghiệm.
    → LIMIT: calibrate CHẬM → evolution lag.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TẦNG 2 — HEBBIAN COMPILATION (individual-level, suốt đời):
    🟢 + 🟡: TẤT CẢ learning suốt đời = CƠ CHẾ NÀY.
    → Experience → body-feedback → Hebbian strengthen → compiled.
    → BẤT KỂ input source (tự thử, được dạy, absorb vô thức).

    2 ĐƯỜNG VÀO cho cùng 1 cơ chế Hebbian:

    ┌──────────────────────┬──────────────────────────┐
    │ 2a DOMAIN CONTACT    │ 2b TRUST-INJECTED        │
    ├──────────────────────┼──────────────────────────┤
    │ Body tiếp xúc domain │ Entity khác truyền chunks│
    │ trực tiếp            │ qua trust gate           │
    │                      │                          │
    │ Active: chạm lửa,   │ Bố mẹ dạy, thầy dạy,   │
    │   lái xe, therapist  │   sách, tôn giáo, AI    │
    │ Passive: giọng vùng, │                          │
    │   norms, gu thẩm mỹ │                          │
    │                      │                          │
    │ Multi-modal (5 kênh) │ Thường 1-2 kênh (verbal)│
    │ Domain verify MỖI lần│ Verify: CHƯA (on trust) │
    │ KHÔNG cần trust gate │ CẦN trust gate           │
    │ Compile: THICK       │ Compile: THINNER         │
    │ Speed: CHẬM          │ Speed: NHANH             │
    └──────────────────────┴──────────────────────────┘

    → 2b inject SEED → 2a verify + DEEPEN = tối ưu (education design)
    → Recursive: existing chunks filter + amplify domain contact
      (expert thấy cái beginner KHÔNG thấy — cùng domain input)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


  "CULTURE" VÀ "AI" = TÊN GỌI, KHÔNG PHẢI CƠ CHẾ RIÊNG:
    Culture = 2a passive (social env → compile vô thức) + 2b (accumulated transmission)
    AI = newest 2b input source (inject chunks, body vẫn phải check)
    Cumulative stacking = emergent property (2b × thế hệ), not separate mechanism


  §6 ↔ §7 RELATIONSHIP:
    §6 (3-Layer) = WHAT thay đổi (hardware / chunks / tools)
    §7 (2-Tầng) = HOW body LEARNS (Darwinian / Hebbian)
    → Bổ sung nhau, không mâu thuẫn.


  ⭐ COHERENCE ≠ TRUTH (3 failure modes):

    Body check COHERENCE (pattern mới khớp cái đã biết?), KHÔNG check TRUTH.

    ① EVOLUTION LAG: body reward ĐÚNG cho environment CŨ, SAI cho MỚI
       → Đường: evolution hiếm → reward "ngọt=quý" → modern dễ → nghiện
       → MXH: ancestral novelty + social cues hiếm → reward "info mới=quý"
         → modern feed vô hạn + đa dạng (mỗi post feed mini gap khác) → scroll

    ② CHUNKS NỀN SAI: coherence khớp nhưng nền sai
       → Flat Earth: nhìn thẳng=phẳng → coherent → body "đúng" → SAI domain
       → "Cortisol = stress hormone" → coherent với pop science → SAI actual mechanism

    ③ SCHEMA OVERRIDE: biết sai mà VẪN follow
       → Nghiện: body "biết" xấu → schema "reward" compiled quá mạnh → override
       → Procrastinate: PFC biết cần làm → "scroll=reward" override

    → Body đúng ~90%+ (2 cơ chế calibrate). Sai ~10% (3 failure modes).
    → EXTERNAL CHECK cần thiết cho 10%: người khác, AI, experiment, domain thật.

  Chi tiết: Why-Body-Knows.md v1.1 §3
```

---

## §8 — CIRCUIT BREAKER MECHANISM

```
⭐ BODY = CIRCUIT BREAKER TỰ NHIÊN (Drill §6b):

  Body KHÔNG check chain logic (truth).
  Body CHECK output: hành vi → body-feedback → PATTERN đánh giá.

  3 BREAK PATHWAYS:

  ① GRADUAL REVISION (slow, most common):
     → Output fails repeatedly → valence shifts slowly
     → Compiled pattern weakens over multiple episodes
     → VD: công thức kinh doanh → thất bại nhiều lần → body dần bỏ
     → Timeline: weeks-months

  ② VIOLENT FLIP (fast, traumatic):
     → Betrayal / extreme experience → valence FLIP immediately
     → Deep schema collapse (Valence-Propagation v2.0 §4: violent flip mechanism)
     → VD: phản bội → chunks person VẪN ĐÓ, valence flip từ + sang -
     → Timeline: instant (1 trial — emotional peak compile)

  ③ BODY DEFENSE (3 automatic circuit breakers):
     → Detachment: cut empathy connection → L2 decoupling
     → Numbness: threshold habituated → signal no longer registers
     → Avoidance behavior: compiled "tránh xa" pattern
     → = Body self-protect khi override quá nhiều lần


  L2 CEILING MECHANISM:

    Có L2 entities (con, bạn thân = body-level feedback):
      → L2 entities = natural circuit breaker
      → Override chains bị CHẶN bởi L2 body-feedback
      → VD: cha quá mê công việc → con ốm → body-feedback CẮT

    Không có L2:
      → Override chains KHÔNG CÓ ceiling tự nhiên
      → Burnout emerges (no body-level signal to stop)
      → VD: workaholic độc thân → nothing stops the chain

    → L2 entities = built-in circuit breaker cho complex behavior
    → = TẠI SAO connection matters beyond "feeling good"


  TIMING HIERARCHY:
    ① Body check (automatic, fast) — FIRST checkpoint
    ② PFC observe (khi body signal problem) — SECOND checkpoint
    ③ Chain analysis (diagnostic) — THIRD (post-break, framework level)

    → Body is ALWAYS first responder
    → PFC only engages WHEN body signals significant dissonance
    → Framework analysis = explanatory (understanding), not processing


  CONNECTION TO MODEL 3+1:
    Circuit breaker = Component 1 (vô thức evaluate)
    operating on compiled patterns tự động.
    PFC (Component 2) only gets involved SAU body has already flagged.

  Chi tiết: Drill-Compile-Short-Collective.md §6b
```

---

## §9 — BODY-FEEDBACK OVERVIEW

```
⭐ BODY-FEEDBACK = SIGNAL ARCHITECTURE CỦA BODY-BASE:

  Body-Feedback/ folder (6 files, ~9,050L) chứa chi tiết.
  Section này = overview entry point.


  DUAL-PULL ARCHITECTURE (01-Foundation §2):
    🟡 Schema bị kéo ĐỒNG THỜI bởi 2 lực:
      ① HARDWARE PULL (nội, bảo thủ, muốn smooth):
         Hebbian LTP, habituation, metabolic efficiency, homeostasis
         Feature: comfort zone, routine, contentment
         Dark side: stagnation, evolution lag

      ② DOMAIN PULL (ngoại, đòi adapt, map reality):
         Novelty drive, prediction-delta
         Feature: learning, growth, curiosity
         Dark side: burnout, neural wear

    Tension = EVOLUTIONARY FEATURE, not bug.
    Chỉ Hardware → stagnation → chết.
    Chỉ Domain → burnout → chết.
    CẢ HAI → oscillation → thrive.

    "Melody hay" 4 criteria (Personal-Melody §5):
      ① Mượt trên hardware (per-person)
      ② Map domain chính xác
      ③ Map domain rộng nhất có thể
      ④ Chơi lâu dài nhất (bền vững)


  INTERFACE LOOP 6-STEP (01-Foundation §3):
    Step 1: Domain → Body sensory
    Step 2: Body → Feedback (vô thức 95% / PFC 5%)
    Step 3: Feedback → Schema update
    Step 4: Schema → Action
    Step 5: Action → Domain
    Step 6: Domain → Body feedback (loop closure)
    → Cycle CONTINUOUS. Không có điểm bắt đầu/kết thúc.


  H10 — 5 PRECONDITIONS FOR BODY SIGNAL (Body-Feedback §6):
    🟡 Body signal (reward hoặc dissonance) = function of 5 preconditions ĐỒNG THỜI:

    ┌───┬──────────────────────┬──────────────────────────┐
    │ # │ Precondition         │ Failure → subjective     │
    ├───┼──────────────────────┼──────────────────────────┤
    │ 1 │ Schema pending       │ "Không cần"              │
    │ 2 │ Chunks base adequate │ "Chả hiểu"              │
    │ 3 │ prediction-delta threshold  │ "Bình thường"            │
    │ 4 │ Goldilocks zone      │ "Quá lạ" / "quá quen"   │
    │ 5 │ Chunk association tag│ "Ghét dù hiểu"           │
    └───┴──────────────────────┴──────────────────────────┘
    ALL 5 REQUIRED. Missing ANY → signal absent or wrong direction.


  3 GENUINE DISCOMFORT SOURCES (Body-Feedback §5):
    ⭐ CORTISOL KHÔNG GÂY ĐAU. 3 nguồn đau THẬT:
    ① Nociception (physical damage)
    ② Mismatch (schema ≠ reality) — CORE of almost ALL dissonance
    ③ Recalibration (neurons adjusting pattern — "gym for neurons")
    → "Reduce cortisol" = WRONG strategy. "Fix mismatch" = RIGHT strategy.


  Chi tiết: Body-Feedback/Body-Feedback.md (entry point cho folder)
```

---

## §10 — READING GUIDE CHO BODY-BASE/ FOLDER

```
BODY-BASE/ FOLDER OVERVIEW (~70+ files):

  Body-Base.md (THIS FILE)           — Entry point
  ├── Why-Body-Knows.md v1.1         — META: tại sao body đáng tin
  ├── Cortisol-Baseline.md v2.0      — Amplifier mechanism (3,059L)
  ├── Valence-Propagation.md v3.0    — Structural/current valence, 3 firing modes, per-entity
  ├── Body-Coupling.md v3.0          — Coupling, 4 bond types, hardware subsidy, M1-M4
  │
  ├── Drill-Inter-Body-Mechanism/    — Inter-Body drill + mechanism
  │   ├── Inter-Body-Mechanism.md v1.0 — 8 principles, Compilable Architecture
  │   ├── Drill-Inter-Body-Main.md   — Raw drill (2,768L)
  │   └── Architecture-Summary.md    — Drill summary (571L)
  │
  ├── Body-Feedback/                 — Signal architecture (~12,000L)
  │   ├── Body-Feedback.md           — Synthesis entry point
  │   ├── Body-Feedback-Mechanism.md v2.0 — Chunk dynamics, Body-Need aggregate
  │   ├── Body-Feedback-Label.md v2.0 — Vocabulary reference (3-tier)
  │   ├── Gap-Direction.md           — Gap có hướng cụ thể
  │   ├── Gap-Body-Need.md v1.0      — 3 satiation types, ENGINE/ROAD/VEHICLE
  │   ├── Gap-Distribution-Profile.md v1.1 — 5-parameter, technology fill
  │   ├── Reward-Signal-Architecture.md — Evaluative:Direct-State ratio, calibration
  │   ├── Hidden-Quality-Perception.md v1.0 — 2 types, Dunning-Kruger meta
  │   ├── Action-Space.md            — By-Product-Gap-Resonance action context
  │   ├── 01-Foundation.md           — Dual-Pull, Interface Loop
  │   ├── 02-Dissonance.md           — 14 levels, trauma loop
  │   ├── 03-Reward.md               — H10, ô tô paradox
  │   └── 04-Integration.md          — Unified cycle, walkthroughs
  │
  ├── Feeling/                       — PFC observation system (~6,924L)
  │   ├── Feeling.md v2.0            — Central reference (WHAT + HOW)
  │   ├── Feeling-Mechanism-Deep.md  — 8-step flow, reward
  │   ├── Feeling-Sources.md         — 10+ channels, 50+ examples
  │   ├── Feeling-Accuracy.md        — Error modes, literacy
  │   ├── Feeling-Chunk-Bridge.md    — Bidirectional mapping
  │   ├── Feeling-Literacy-Training  — 5-stage training
  │   ├── Feeling-Research.md        — Research foundation
  │   ├── 01 - Feel-Analysis-Draft/  — 124 examples trajectory
  │   └── 02 - Deep-Analysis-Draft/  — 6 themes + synthesis
  │
  ├── Chunk/                         — Chunk system (~55,000L)
  │   ├── Chunk.md v2.0              — Core reference
  │   ├── 99-Master-Synthesis.md     — Unified lifecycle
  │   ├── Background-Pattern.md v2.0 — Triple Bias, valence system, shiftability
  │   ├── 09-Learning-Cycle.md       — Chu kỳ học
  │   │
  │   ├── Agent-Mechanism/           — Per-entity mechanism (11 files)
  │   │   ├── Agent-Mechanism.md v2.1 — Master: 10 dimensions
  │   │   ├── Self-Pattern-Modeling.md v3.1 — Solo simulation, 1 mech × 3 dims
  │   │   ├── Entity-Compiled.md v1.0 — Neural reality, formation, Dunbar
  │   │   ├── Entity-Access.md v1.2   — Gradient Mức 0-5
  │   │   ├── Entity-Access-Excess.md v1.0 — Excess territory, addiction
  │   │   ├── Entity-Access-Calibration.md v1.0 — Self-regulation, hardware subsidy
  │   │   ├── Bond-Architecture.md v1.0 — 1 mechanism × 4 bond types
  │   │   ├── By-Product-Gap-Resonance.md v1.4 — Mutual match, 5 drills
  │   │   ├── Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions
  │   │   ├── Resonance-Per-Entity.md v1.0 — Per-relationship dynamics
  │   │   └── By-Product-Scale.md v1.0 — 1 mechanism × 3 scales
  │   │
  │   ├── Child-Chunk-Development/   — F1: 12 files
  │   ├── Chunk-External-Development/— F3: external install
  │   └── Chunk-Internal-Processing/ — F4: 9 files
  │
  ├── Schema/                        — Schema system
  │   ├── Schema.md                  — Schema = observation parameter
  │   ├── Anchor-Schema.md           — Sync point + 4 nguồn
  │   ├── Anchor-Schema-Example.md   — 24 healthy examples
  │   └── Anchor-Schema-Extreme.md   — Failure modes
  │
  └── Melody Lens/                   — Metaphor system
      ├── Personal-Melody.md         — Per-person melody
      ├── Personal-Melody-Example.md — 3 profiles
      ├── Melody-Arc.md              — Build cycle
      └── Global-Melody.md           — Collective melody


READING PATHS:

  Quick orientation (~1 giờ):
    1. THIS FILE (Body-Base.md)
    2. Body-Feedback/Body-Feedback.md
    3. Why-Body-Knows.md

  Core mechanism deep dive (~3-5 giờ):
    1. THIS FILE
    2. Chunk/Chunk.md v2.0
    3. Valence-Propagation.md v3.0
    4. Body-Coupling.md v3.0
    5. Cortisol-Baseline.md v2.0
    6. Inter-Body-Mechanism.md v1.0

  Agent-Mechanism deep dive (~4-6 giờ):
    1. THIS FILE §3-§4 (Model 3+1, compile)
    2. Entity-Compiled.md v1.0 (neural reality)
    3. Entity-Access.md v1.2 (gradient model)
    4. Bond-Architecture.md v1.0 (4 bond types)
    5. By-Product-Gap-Resonance.md v1.4 (mutual match)
    6. Resonance-Sustainability.md v1.0 (sustainability)
    7. Self-Pattern-Modeling.md v3.1 (solo simulation)

  Feeling system (~2-3 giờ):
    1. THIS FILE §1-§2
    2. Feeling/Feeling.md v2.0
    3. Body-Feedback/01-Foundation.md §5 (body-feedback vs feeling)
    4. Feeling/Feeling-Mechanism-Deep.md

  Framework theory (~2 giờ):
    1. THIS FILE §1-§4 (foundations + core principles + compile)
    2. PFC/PFC-Function.md
    3. PFC/Simulation-Engine.md v1.0
    4. Neural-Architecture.md
    5. Why-Body-Knows.md

  Inter-Body deep dive (~2 giờ):
    1. THIS FILE §1.2-§1.3 (3 foundations + body-need)
    2. Inter-Body-Mechanism.md v1.0
    3. Body-Feedback-Mechanism.md v2.0
    4. Valence-Propagation.md v3.0 §3 (Entity-Compiled)
```

---

## §11 — HONEST ASSESSMENT

```
🟢 HIGH CONFIDENCE:

  ✓ Evolution calibration (Darwin, established)
  ✓ Mere exposure effect (Zajonc 1968)
  ✓ Prediction error signals (Schultz 1997)
  ✓ Wanting ≠ liking (Berridge & Robinson 1998, 2003)
  ✓ Somatic markers (Damasio 1994)
  ✓ PFC sub-regions + functions (decades of research)
  ✓ WM ~4±1 (Cowan 2001)
  ✓ Hebbian learning (Hebb 1949)
  ✓ Sleep consolidation (Walker 2017)
  ✓ Reconsolidation window (Nader 2000)
  ✓ Motion sickness = poison defense (Treisman 1977)
  ✓ Phantom limb pain, placebo nausea (Ramachandran, Benedetti)
  ✓ Anterior insula interoception (Craig 2002, 2009)
  ✓ NE α1 PFC disconnect (Arnsten 2009)
  ✓ Hedonic adaptation (Brickman 1978)
  ✓ Loss aversion ~2x (Kahneman & Tversky 1979)
  ✓ Social-physical pain overlap (Eisenberger 2003) [v3.0]
  ✓ μ-opioid in social play (Panksepp 1998) [v3.0]
  ✓ Social Baseline Theory (Coan & Sbarra 2015) [v3.0]
  ✓ Dual inheritance genes + culture (Boyd & Richerson 2005) [v3.0]
  ✓ Cumulative cultural evolution (Tomasello 2009) [v3.0]


🟡 MEDIUM CONFIDENCE (Framework Synthesis):

  ⚠ "Body evaluates patterns not reality" as UNIFIED principle
    (each case established, unifying integration = novel)
  ⚠ Model 3+1 (components established, 3+1 organization = novel)
  ⚠ "PFC = director, body = compiler" framing
    (roles established, metaphor = novel)
  ⚠ Trust as BRIDGE component (mechanism established, positioning = novel)
  ⚠ L0-L1 substrate model (components established, organization = novel)
  ⚠ 2-tier + 2-pathway calibration model (each component established, integration = novel)
  ⚠ BB1+BB2 convergence (novel insight from Drill §26)
  ⚠ Circuit breaker 3 pathways (mechanisms established, taxonomy = novel)
  ⚠ Dual-pull as architectural principle (each pull established, 2-force = novel)
  ⚠ H10 5-precondition model (each precondition grounded, ALL-5 = novel)
  ⚠ 3 Loại compile taxonomy (components established, taxonomy = novel)
  ⚠ L2 ceiling mechanism (mechanism plausible, not directly tested)
  ⚠ Modulatory vs Processing × L0-L1 mapping (Parkinson drill validates)
  ⚠ Braak staging confirms bottom-up architecture
  ⚠ 3 Hardware Foundations → Compilable Architecture (neuroscience 🟢, synthesis = 🟡) [v3.0]
  ⚠ Hardwired/Compilable Architecture naming (mechanism established, naming = novel) [v3.0]
  ⚠ Body-Need as named aggregate (mechanism established, naming = novel) [v3.0]
  ⚠ Compiled/Fresh reframe (consistent w/ Kahneman, reframe = novel) [v3.0]
  ⚠ 3-Layer Evolution model (dual inheritance 🟢, 3-layer organization = 🟡) [v3.0]
  ⚠ Protect = observation parameter, NOT operator (reframe, consistent) [v3.0]
  ⚠ Money = bridge technology (function established, naming = novel) [v3.0]
  ⚠ Entity-Access gradient Mức 0-5 (trust research 🟢, gradient model = 🟡) [v3.2]
  ⚠ Entity-Compiled = neural reality (neuroscience 🟢, naming = 🟡) [v3.2]
  ⚠ Bond-Architecture 4 types (attachment research 🟢, taxonomy = 🟡) [v3.2]
  ⚠ Hardware Subsidy as named mechanism (oxytocin/opioid 🟢, concept = 🟡) [v3.2]
  ⚠ M1-M4 firing modes (neurochemistry 🟢, 4-mode taxonomy = 🟡) [v3.2]
  ⚠ 3 Satiation types ENGINE/ROAD/VEHICLE (receptor dynamics 🟢, metaphor = 🟡) [v3.2]
  ⚠ Simulation Engine 3-component model (PFC sim research 🟢, formalization = 🟡) [v3.2]


🔴 LOW CONFIDENCE:

  ⚠ Body accuracy "~90%" estimate (qualitative, not measurable)
  ⚠ Vô thức "~95%" / PFC "~5%" ratio (heuristic, not measured)
  ⚠ Goldilocks "40-70%" specific percentages (inverted-U established, cutoffs approximate)
  ⚠ "Melody hay" sustainability prediction (logical but untested)
```

---

## §12 — CROSS-REFERENCES

```
WITHIN BODY-BASE/ FOLDER:
  Why-Body-Knows.md v1.1    — 2-tier + 2-pathway calibration, coherence ≠ truth, 3 failure modes
  Cortisol-Baseline.md v2.0 — amplifier mechanism, 10 touchpoints, direction > level
  Valence-Propagation.md v3.0 — structural/current valence, 3 firing modes, hardware subsidy, per-entity
  Body-Coupling.md v3.0     — coupling, 4 bond types, hardware subsidy, M1-M4, anti-suppress
  Body-Feedback/            — signal architecture, Dual-Pull, H10, trauma loop
  Body-Feedback-Mechanism.md v2.0 — chunk dynamics, Body-Need aggregate, 3 dynamics
  Body-Feedback-Label.md v2.0 — vocabulary reference, 3-tier labels
  Gap-Body-Need.md v1.0     — 3 satiation types, ENGINE/ROAD/VEHICLE, entity-gap matching
  Gap-Distribution-Profile.md v1.1 — 5-parameter, technology fill, PFC budget
  Hidden-Quality-Perception.md v1.0 — 2 types (Expert+Leader), Dunning-Kruger meta
  Reward-Signal-Architecture.md — Evaluative:Direct-State ratio, reward calibration
  Feeling/                  — PFC observation interface, 7-layer fidelity
  Chunk/Chunk.md v2.0       — sole substrate, 4 compile mechanisms, 4 connection types
  Background-Pattern.md v2.0 — Triple Bias, valence system, pattern shiftability
  Schema/                   — observation parameter, Anchor-Schema
  Melody Lens/              — metaphor system, Personal-Melody

AGENT-MECHANISM/ FOLDER (11 files):
  Agent-Mechanism.md v2.1   — master: 10 dimensions per-entity
  Self-Pattern-Modeling.md v3.1 — solo simulation, 1 mechanism × 3 dimensions
  Entity-Compiled.md v1.0   — neural reality, formation 40→200h, Dunbar ~150, grief A+B+C
  Entity-Access.md v1.2     — gradient Mức 0-5, per-entity access model
  Entity-Access-Excess.md v1.0 — excess territory, when access becomes addiction
  Entity-Access-Calibration.md v1.0 — self-regulation, hardware subsidy, failure modes
  Bond-Architecture.md v1.0 — 1 mechanism × 4 bond types, M1-M4, gap-clone proof
  By-Product-Gap-Resonance.md v1.4 — mutual match, 5 drills, sustainability bridge
  Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions, 3 modalities, U-curve
  Resonance-Per-Entity.md v1.0 — per-relationship dynamics, hardware subsidy spectrum
  By-Product-Scale.md v1.0  — 1 mechanism × 3 scales (pair/hub/institutional)

INTER-BODY DRILL:
  Inter-Body-Mechanism.md v1.0 — 8 principles, Compilable Architecture, 5-channel, 3-cost
  Architecture-Summary.md v1.1 — drill summary (571L, 8 principles)
  Drill-Inter-Body-Main.md v1.6 — raw drill (2,768L, 6 rounds)

PFC/ FOLDER:
  PFC-Function.md           — 24 functions, 95/5 split, "PFC tạo context"
  PFC-Operations.md v1.0    — operational mechanisms
  Simulation-Engine.md v1.0 — 1 engine, 3 components (interoception × simulation × Self-Pattern-Modeling)
  PFC-Label.md v1.0         — vocabulary reference, 13 domains, 3-tier labels
  PFC-Hardware.md           — COMT, DRD4, NE, hardware variation
  PFC-Development.md        — lifecycle, training
  PFC-Hold-Dimensions.md    — tại sao ~4±1 (6 convergent forces)
  Logic-Feeling.md          — 2 processing modes song song
  Logic-Feeling-Balance.md  — meta-principle, infinite regress, mỗi người tự cân bằng
  Imagination/              — Imagine-Final v3.0, Somatic-Articulation-Loop

OBSERVATION/ FOLDER:
  Novelty.md, Threat.md, Boredom.md v2.0, Drive.md — observation parameters
  Empathy.md v4.0, Connection.md v5.0, Status.md, Protect.md — social parameters
  Meaning.md, Autonomy.md, Gratitude.md, Obligation.md — higher-order parameters
  Liking-Wanting.md         — bridge file, 6 wanting mechanisms

NEURAL + DOMAIN:
  Neural-Architecture.md    — A/B/C/D 4-zone physical map
  Neural-Processing-Flow.md — signal pathway detail
  Domain/Domain.md          — domain reality, lean epistemological
  Collective/               — Coordination-Node v1.2, Collective-Body v2.1, etc.

DRILL SOURCES:
  Drill-Draft/Drill-Compile-Short-Collective.md — §6b, §19, §21, §23, §26
  Drill-Draft/Drill-L2-Phenomenology-Emptiness.md — L2, trống rỗng, 2 cơ chế nền
  plan-Phase-E-Refinement.md — E1-E5 sequence

HEALTH CONDITIONS:
  Parkinson-Analysis.md v1.1 — §2 modulatory vs processing, §4.2 Braak staging

KEY RESEARCH:
  Berridge & Robinson (1998, 2003) — wanting ≠ liking
  Damasio (1994) — somatic markers
  Treisman (1977) — motion sickness poison theory
  Schultz (1997) — VTA prediction error
  Craig (2002, 2009) — anterior insula interoception
  Arnsten (2009) — NE α1 PFC disconnect
  Brickman (1978) — hedonic adaptation
  Kahneman & Tversky (1979) — loss aversion, prospect theory
  Hebb (1949) — Hebbian learning
  Walker (2017) — sleep consolidation
  Nader (2000) — reconsolidation
  Cowan (2001) — WM ~4±1
  Zajonc (1968) — mere exposure
  Berlyne (1960) — optimal novelty
  Eisenberger (2003) — social-physical pain overlap [v3.0]
  Panksepp (1998) — μ-opioid social play [v3.0]
  Coan & Sbarra (2015) — Social Baseline Theory [v3.0]
  Boyd & Richerson (2005) — dual inheritance [v3.0]
  Tomasello (2009) — cumulative cultural evolution [v3.0]
  Klein (1998) — recognition-primed decisions [v3.0]
  Kahneman (2011) — System 1/2 ≈ Compiled/Fresh [v3.0]
```

---

> **Body-Base.md v3.2**
>
> Entry point cho toàn bộ Body-Base system.
> Foundation layer: mọi thứ trong framework build trên body-base.
>
> Core principles (v3.2):
>   §1: 3 Hardware Foundations → Compilable Architecture (general-purpose adaptive)
>   §2: Body evaluates PATTERNS, not reality (Treisman 1977 + 6 cases)
>   §3: Unified Model 3+1 + Simulation Engine + Entity-Access + Bond-Architecture
>   §4: PFC = director, body = compiler + Entity-Compiled + Compiled/Fresh axis
>   §5: L0-L1 substrate + Hardware Subsidy + M1-M4 firing modes
>   §6: 3-Layer Evolution (Hardware → Compiled → Cultural)
>   §7: 2-tier calibration (Darwinian + Hebbian, 2a domain + 2b trust-inject)
>   §8: Circuit breaker (3 pathways, L2 ceiling)
>   §9: Body-feedback overview (Dual-Pull, H10, 3 Genuine Discomfort Sources)
>
> Schema phục vụ body-base. Body is final arbiter of value.
> Body đúng ~90%+. External check cho 10% gap.
>
> Phiên bản: v3.2, 2026-05-23.
> Source: Inter-Body Drill (8 principles) + 28-session Drill Propagation concept cascade.
>
> Changelog:
>   v1.0 (2026-04-14): Phase C basic structure
>   v2.0 (2026-05-08): Phase E1 rewrite (Drill S1-S6 insights)
>   v2.1 (2026-05-15): +§5.4 Modulatory/Processing, Braak validation
>   v3.0 (2026-05-16): Phase 4 ALL REWRITE
>     — §0: Layer stack fix (remove L3, add 3 Hardware Foundations)
>     — §1.2 NEW: 3 Hardware Foundations → Compilable Architecture
>     — §1.3 NEW: Body-Need 2-Source Aggregate
>     — §4.3 NEW: Compiled vs Fresh = Real Axis (Compiled/Fresh reframe)
>     — §5.3 REWRITE: PFC Operators on L1 (Protect removed as operator)
>     — §5.4 UPDATE: Modulatory mapping updated (L3 refs removed)
>     — §6 NEW: 3-Layer Evolution (Hardware → Compiled → Cultural)
>     — §8 UPDATE: Valence-Propagation cross-ref updated to v2.0
>     — §10 UPDATE: Reading Guide + folder overview versions
>     — §11 UPDATE: +7 🟡 items, +5 🟢 items for new content
>     — §12 UPDATE: +7 research citations, all versions updated
>   v3.1 (2026-05-17): §7 REWRITE — aligned with Why-Body-Knows v1.1
>     — §7 REWRITE: 4-Tier → 2-Tier + 2-Pathway calibration model
>       (only 2 MECHANISMS: Darwinian selection + Hebbian compilation)
>       (Culture/AI = input sources for Hebbian, not separate tiers)
>       (2a Domain Contact + 2b Trust-Injected = 2 pathways for Tầng 2)
>     — §6↔§7 relationship clarified (WHAT changes vs HOW body learns)
>     — All "4-tier" references updated throughout file
>     — §11: "4-tier stacking" → "2-tier + 2-pathway model"
>     — §12: Why-Body-Knows.md → v1.1 reference
>   v3.2 (2026-05-23): Concept Cascade — integrate 28-session drill outputs
>     — YAML deps: +13 new files, Valence-Propagation v2.0→v3.0, Body-Coupling v2.0→v3.0
>     — §0: flow diagram +Agent-Mechanism (11 files), +PFC (Simulation-Engine, PFC-Label)
>     — §1.3: +Satiation 3 types (ENGINE/ROAD/VEHICLE), +Gap-Body-Need ref
>     — §3: +Simulation Engine (PFC component), +Entity-Access gradient, +Bond-Architecture
>     — §4.2: +Entity-Compiled neural reality, Entity-Access gradient refs
>     — §5.3: +Hardware Subsidy mechanism, +M1-M4 firing modes
>     — §10: comprehensive folder update (Agent-Mechanism/ 11 files, Body-Feedback/ 13 files)
>     — §10: +Agent-Mechanism reading path, versions updated throughout
>     — §11: +7 🟡 items for new concepts
>     — §12: +Agent-Mechanism/ section (11 refs), +PFC (3 refs), versions updated
