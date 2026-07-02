---
title: Body-Base — Entry Point cho Toàn Bộ Body-Base System
version: 4.0
created: 2026-04-14 (v1.0 BASIC — Phase C)
rewritten: 2026-05-16 (v3.0 — Phase 4 ALL REWRITE)
refined: 2026-05-17 (v3.1), 2026-05-23 (v3.2), 2026-05-25 (v3.3), 2026-06-01 (v3.4)
rewritten: 2026-06-02 (v4.0 — tích hợp 4 file nền tảng mới: Compile-Taxonomy v3.0, Compile-Sleep v1.0, Trust v1.0, Self-Observation v1.0. §3 Trust REWRITE, §4.2 Compile 1-Engine REWRITE, §0 rút gọn, §9 reduce, versions synced)
previous: backup/Body-Base-v3.4-backup.md
status: v4.0 REFERENCE FILE
scope: |
  ENTRY POINT cho toàn bộ Body-Base/ folder (~70+ files).
  Body-Base LÀ GÌ + 3 Hardware Foundations + Compilable Architecture +
  Core Principles + Unified Model 3+1 + L0-L1 Substrate +
  Body Compile + Compiled/Fresh Axis + Body-Need 2-Source +
  3-Layer Evolution + 2-Tier Calibration + Circuit Breaker +
  Body-Feedback Overview.
  v3.0 KEY CHANGES: 3 Hardware Foundations, Body-Need 2-source, Compiled/Fresh axis,
    3-Layer Evolution, PFC Operators reframe, cross-refs updated.
  v3.1-v3.4: Concept Cascade (~15 new files), Dissonance-Signal-Architecture,
    Agent-Mechanism 11 files, Body-Feedback 17 files, version sync.
    Chi tiết: backup/Body-Base-v3.4-backup.md
  v4.0 KEY CHANGES (tích hợp 4 file nền tảng mới):
    ① §3 Trust REWRITE: +definition, +3 sub-dimensions, +3 functions, +dynamics, +formation
    ② §4.2 Compile REWRITE: 1 Engine + 3 Modulator Configurations (Compile-Taxonomy v3.0)
    ③ §3 PFC: +Self-Observation = APPLICATION-3, keystone, Mức 0-6
    ④ §0 RESTRUCTURE: flow diagram rút gọn (~50→30 dòng)
    ⑤ §9 REDUCE: Body-Feedback overview rút gọn (pointer to Body-Feedback.md v3.1)
    ⑥ §7: +Trust mechanism detail (4 nguồn formation, Compile-Taxonomy v3.0)
    ⑦ Versions synced: Simulation-Engine v1.2, PFC-Operations v1.3, Self-Pattern-Modeling v3.2, Entity-Valence-Dynamics v1.1, PFC-Label v1.1
    ⑧ +2 deps: Self-Observation.md v1.0, Attention-Spectrum.md v2.1
    ⑨ Changelog trimmed (v1.0-v3.3 details → backup)
purpose: |
  Người đọc NÊN ĐỌC FILE NÀY TRƯỚC khi đi vào bất kỳ sub-file nào.
  File này consolidate, KHÔNG duplicate — detail ở sub-files.
  Foundation layer cho TOÀN BỘ framework.
previous_version: backup/Body-Base-v2.1-backup.md
parent: Core-Deep-Dive/ (foundation file)
dependencies:
  - Why-Body-Knows.md v1.2 — 2-tier + 2-pathway calibration, coherence ≠ truth, Simulation-Engine
  - Body-Feedback/Body-Feedback.md v3.1 — Dual-Pull, Body-Feedback-Precondition, Interface Loop, 17 files synthesis
  - Body-Feedback/01-Foundation.md — body-feedback vs feeling 2-layer
  - Body-Feedback/Body-Feedback-Mechanism.md v2.1 — chunk dynamics, Body-Need aggregate
  - Body-Feedback/Gap-Body-Need.md v1.0 — 3 satiation types, ENGINE/ROAD/VEHICLE, entity-gap matching
  - Body-Feedback/Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State, 5 Profiles
  - Body-Feedback/Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State Dissonance, clinical
  - Body-Feedback/Body-Feedback-Precondition.md v1.0 — 5 preconditions, WHEN signal fires
  - Feeling/Feeling.md v3.0 — 7-layer fidelity, PFC observation
  - Feeling/Body-Knowing.md v1.0 — compiled knowing, 3 directions, Dual Check
  - Chunk/Chunk.md v3.0 — sole substrate, 4-phase lifecycle, Compile Architecture
  - Chunk/Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators, 3 Compile Types
  - Chunk/Compile-Sleep.md v1.0 — Sleep Maintenance, 6 mechanisms, offline system
  - Valence-Propagation.md v4.1 — valence definition, formation, propagation qua schema chain
  - Entity-Valence-Dynamics.md v1.1 — per-entity dynamics: structural/current, 3 firing modes, hardware-subsidy
  - Body-Coupling.md v3.0 — coupling mechanism, 4 bond types, hardware-subsidy, Resonance Decline
  - Cortisol-Baseline.md v2.1 — amplifier, direction > level
  - PFC/PFC-Function.md — 24 functions, 95/5 split
  - PFC/Simulation-Engine.md v1.2 — 1 engine, 3 components, 3 axes, N applications
  - PFC/PFC-Operations.md v1.3 — Hold/Suppress, Budget, Compiled Quality
  - PFC/PFC-Label.md v1.1 — vocabulary reference, 13 domains, 3-tier labels
  - PFC/Self-Observation.md v1.0 — APPLICATION-3, Mức 0-6, Keystone, Tool Not Virtue
  - Attention-Spectrum.md v2.1 — attention hardware, COMT/DRD4
  - Neural-Architecture.md — A/B/C/D 4-zone physical map
  - Inter-Body-Mechanism.md v2.0 — 8 drill principles, Compilable Architecture
  - Trust.md v1.0 — trust = compiled prediction about entity's gap-fill reliability, meta-dimension
  - Body-Feedback/Body-Feedback-Label.md v2.1 — vocabulary reference
  - Chunk/Agent-Mechanism/Self-Pattern-Modeling.md v3.2 — solo simulation, 1 mechanism × 3 dimensions
  - Chunk/Agent-Mechanism/Entity-Compiled.md v1.0 — neural reality, formation 40→200h, Dunbar
  - Chunk/Agent-Mechanism/Entity-Access.md v1.2 — gradient model, Mức 0-5, per-entity
  - Chunk/Agent-Mechanism/Bond-Architecture.md v2.0 — 1 mechanism × 4 bond types, Resonance Decline
  - Chunk/Agent-Mechanism/By-Product-Gap-Resonance.md v1.4 — mutual match, 5 drills
  - Chunk/Agent-Mechanism/Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions, 3 modalities
  - Chunk/Agent-Mechanism/By-Product-Scale.md v1.0 — 1 mechanism × 3 scales
  - Chunk/Agent-Mechanism/Resonance-Per-Entity.md v1.0 — per-relationship, hardware-subsidy spectrum
  - Chunk/Agent-Mechanism/Entity-Access-Excess.md v1.0 — excess territory, addiction
  - Chunk/Agent-Mechanism/Entity-Access-Calibration.md v1.0 — self-regulation, hardware-subsidy
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
    → Hardware/sensory + chunk dynamics → body-need (Body-Feedback-Mechanism v2.1 §1)
    → PFC KHÔNG luôn biết body-need hiện tại
    → Chi tiết: Inter-Body-Mechanism.md §2


FILE NÀY TRONG FLOW:

  ┌────────────────────────────────────────────────────────────────────────┐
  │ BODY-BASE.MD (FILE NÀY) — ENTRY POINT                                 │
  │                                                                        │
  │  Đọc file này TRƯỚC → chọn hướng đi sâu:                             │
  │                                                                        │
  │  Mechanism (HOW — 10 files):                                           │
  │    Chunk/ (Chunk v3.0, Compile-Taxonomy v3.0, Compile-Sleep v1.0)      │
  │    Valence-Propagation v4.1, Entity-Valence-Dynamics v1.1,             │
  │      Body-Coupling v3.0                                                │
  │    Trust.md v1.0, Cortisol v2.1, Inter-Body v2.0                       │
  │                                                                        │
  │  Agent-Mechanism (PER-ENTITY — 11 files):                              │
  │    Self-Pattern-Modeling v3.2, Entity-Compiled v1.0,                   │
  │      Entity-Access v1.2                                                │
  │    Bond-Architecture v2.0, Resonance (3 files), Scale v1.0             │
  │                                                                        │
  │  Observation (WHAT PFC SEES):                                          │
  │    Feeling/ (Feeling v3.0, Body-Knowing v1.0)                          │
  │    Body-Feedback/ (17 files, ~27,500L)                                 │
  │                                                                        │
  │  Foundation + PFC (WHY + WHAT DIRECTS):                                │
  │    Why-Body-Knows v1.2, Neural-Architecture                            │
  │    PFC/ (PFC-Function, Simulation-Engine v1.2,                         │
  │      PFC-Operations v1.3, PFC-Label v1.1)                              │
  │    PFC/Self-Observation.md v1.0 — APPLICATION-3 (keystone)             │
  │    Attention-Spectrum.md v2.1 — attention hardware                     │
  │                                                                        │
  │  Chi tiết đầy đủ: §10 Reading Guide                                   │
  └────────────────────────────────────────────────────────────────────────┘
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
    → = Feeling.md v3.0: "Feeling = WHAT PFC SEES"
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
⭐ BODY-NEED = TỔNG HỢP TRẠNG THÁI CẦN HIỆN TẠI (Body-Feedback-Mechanism v2.1 §1):

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
    ① ENGINE satiation: cơ chế tạo gap mệt/giảm (Ví dụ: dopamine receptor downregulation)
    ② ROAD satiation: đường gap fill quen quá → cần path mới (Ví dụ: nhạc cũ nhàm)
    ③ VEHICLE satiation: entity cụ thể bão hòa (Ví dụ: ăn phở 7 ngày liên tiếp)
    → Mỗi type → khác intervention. Nhầm type = fix sai.
    → Entity-gap matching: mỗi gap có entity phù hợp riêng (Gap-Body-Need.md §4)

  SLEEP MAINTENANCE IMPACT (Compile-Sleep.md v1.0):
    Sleep deprivation → body-need DISTORTED:
    → Pruning thiếu → noise tích tụ → baseline thresholds sai
    → PFC degrades FIRST → direction selection kém → wrong gaps pursued
    → Body-need vẫn fire nhưng MẤT ĐỘ CHÍNH XÁC (signal integrity giảm)

Chi tiết: Body-Feedback-Mechanism.md v2.1 §1, Inter-Body-Mechanism.md §2, Gap-Body-Need.md v1.0
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
    → "Ô tô paradox" (Body-Feedback.md §8.1): same car → 5 opposite reactions
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
    → ⚠️ Tất cả % trong file = calibration anchor, KHÔNG phải đo lường chính xác. Xem §11.


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
  │   SIMULATION-ENGINE = formalized PFC mechanism:                  │
  │     Interoception × Simulation × Self/Other Model = 1 engine    │
  │     APPLICATION-1: Self-Pattern-Modeling                         │
  │       (Other, Present, Simulate)                                 │
  │     APPLICATION-2: Imagine-Final                                 │
  │       (Self, Future, Simulate+Construct)                         │
  │     APPLICATION-3: Self-Observation (Self, Present, Observe)     │
  │     ⭐ KEYSTONE: Self-Observation fail → cascade 5+ systems     │
  │     Chi tiết: Simulation-Engine.md v1.2, Self-Observation.md v1.0│
  │                                                                  │
  │   ATTENTION HARDWARE: COMT/DRD4 variation per person             │
  │     Chi tiết: Attention-Spectrum.md v2.1                         │
  │                                                                  │
  │   24 functions chi tiết: PFC-Function.md                         │
  ├─────────────────────────────────────────────────────────────────┤
  │ COMPONENT 3 (BRIDGE) — TRUST: AMPLIFY + MODULATE + CONNECT       │
  │                                                                  │
  │   DEFINITION (Trust.md v1.0):                                    │
  │     Trust = compiled prediction about entity's gap-fill RELIABILITY│
  │     Trust ≠ Valence: trust = PREDICTION (tương lai)              │
  │                       valence = ASSESSMENT (hiện tại)            │
  │     2 chiều ĐỘC LẬP: high-trust + negative-valence CÓ THỂ      │
  │       (Ví dụ: sợ Chúa nhưng TIN Chúa toàn năng)                    │
  │     🟢 Colquitt 2007: trust separable from liking               │
  │                                                                  │
  │   3 SUB-DIMENSIONS (independent — Trust.md v1.0 §1):            │
  │     ① Trust-Authority: entity CÓ QUYỀN trong domain? (structural)│
  │     ② Trust-Competence: entity CÓ NĂNG LỰC? (calibrated via experience)│
  │     ③ Trust-Intention: entity CÓ Ý TỐT cho tôi? (fastest collapse)│
  │     3 chiều ĐỘC LẬP — high ở 1, low ở 2 có thể xảy ra         │
  │     🟢 Mayer, Davis & Schoorman 1995 (framework ADDS authority)  │
  │                                                                  │
  │   3 FUNCTIONS:                                                   │
  │     AMPLIFY: trust = Entity-Valence amplifier cho compile rate   │
  │       (gradient Mức 0-5, NOT binary gate — Compile-Taxonomy v3.0)│
  │     MODULATE: trust modulate TOÀN BỘ valence profile             │
  │     CONNECT: trust = ONLY mechanism cho complexity > 4±1          │
  │                                                                  │
  │   DYNAMICS (Trust.md v1.0 §4):                                   │
  │     Build: CHẬM (months/years — cần consistency, not 1 lần tốt) │
  │     Maintain: ỔN ĐỊNH (compiled = persistent, không cần daily)   │
  │     Collapse: NHANH (1 betrayal — negativity bias override ALL)  │
  │     → Asymmetry = evolutionary design: quick detect danger       │
  │     🟢 Slovic 1993, Baumeister 2001, Freyd 1996                 │
  │                                                                  │
  │   FORMATION: 4 nguồn (Trust.md v1.0 §2):                        │
  │     ① Direct experience: chậm nhất (months), chính xác nhất     │
  │     ② Observed experience: trung bình (weeks)                    │
  │     ③ Schema inheritance: nhanh nhất (hours), kém chính xác nhất │
  │     ④ Context inference: nhanh (seconds), dễ bị exploit          │
  │     = TẠI SAO trẻ tin thầy TRƯỚC khi đi học (installed trust ③) │
  │     🟢 Lewicki 2006, Csibra & Gergely 2009, Bandura 1977       │
  │                                                                  │
  │   ENTITY-ACCESS GRADIENT = formalized trust model:               │
  │     Mức 0 (stranger) → Mức 5 (self/child)                       │
  │     Trust ≠ binary → gradient per-entity                         │
  │     Chi tiết: Entity-Access.md v1.2                              │
  │                                                                  │
  │   BOND-ARCHITECTURE = 4 bond types qua 1 mechanism:             │
  │     Proximity / Shared-Experience / Reciprocal / Identity        │
  │     Entity-Compiled = neural reality, KHÔNG phải metaphor        │
  │     Chi tiết: Bond-Architecture.md v2.0, Entity-Compiled.md v1.0│
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


  BLACKBOX-1 + BLACKBOX-2 CONVERGENCE (Drill §26):

    Blackbox-1 (chunk substrate) + Blackbox-2 (valence complexity)
    = KHÔNG PHẢI 2 blackbox riêng biệt.
    = CÙNG 1 mechanism ở behavioral level:
      Compile = structural aspect (patterns form)
      Valence = evaluative aspect (patterns get tagged)
      → XẢY RA ĐỒNG THỜI, không tuần tự.

    Blackbox-2 = Blackbox-1 + collective scale + hardware variance.
    Blackbox-1 ⊂ Blackbox-2 ⊂ Model 3+1.

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

  BODY COMPILE qua 4 mechanisms (Chunk.md v3.0 §2):
    ① Repetition — lặp lại nhiều lần (LTP, Bliss & Lømo 1973 🟢)
    ② Emotional peak — 1 lần cảm xúc cực mạnh (Brown & Kulik 1977 🟢)
    ③ Multi-modal — nhiều kênh cùng lúc (wire across cortex)
    ④ Sleep consolidation — offline integration (Walker 2017 🟢)
       Chi tiết sleep: Compile-Sleep.md v1.0 (6 mechanisms, offline system)

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

### §4.2 — Compile Architecture: 1 Engine + 3 Modulator Configurations

```
🟡 COMPILE ARCHITECTURE (Compile-Taxonomy.md v3.0):

  ⭐ ALL compile = 1 ENGINE: Exposure → Hebbian → Compiled Chunk (Hebb 1949).
  Không có "trust compile mechanism" riêng hay "expertise mechanism" riêng.
  CHỈ CÓ 1 engine. 3 Compile Types = labels cho dominant modulator configuration.

  3 MODULATORS:
    ① Entity-Valence Bias (automatic, cost≈0): trust amplify compile rate + bias exposure
    ② 3 Exposure Channels SONG SONG:
       External (body-input from reality — richest, domain-checked)
       Deliberate (PFC imagination/simulate — flexible, abstract domains)
       Spontaneous (automatic chunk fire — Background-Pattern, mind wandering)
    ③ PFC Modulation (deliberate, costly): Hold = amplify, Suppress = block

  3 COMPILE TYPES = MODULATOR CONFIGURATIONS:

    ┌──────────────┬──────────────────────────┬──────────────┐
    │ Type         │ Engine + Dominant Modulator│ % behavior  │
    ├──────────────┼──────────────────────────┼──────────────┤
    │ Experience   │ Engine + minimal modulators│ ~90%        │
    │ Expertise    │ Engine + PFC sustained hold│ ~5%         │
    │ Trust        │ Engine + Entity-Valence Bias│ ~5%        │
    └──────────────┴──────────────────────────┴──────────────┘

  ⚠️ TRUST = AMPLIFIER (gradient Mức 0-5), KHÔNG PHẢI GATE (binary):
    → Trẻ bị ÉP HỌC (no trust) → VẪN compile kiến thức (engine chạy)
    → Trust "đóng" → body EXPOSED to content → content compile
    → Trust KHÔNG gate content compile. Trust amplify VALUE compile.
    → Entity-Access.md v1.2: trust = gradient per-entity
    → Entity-Access-Calibration.md v1.0: self-regulation mechanism

  SLEEP MAINTENANCE (Compile-Sleep.md v1.0):
    → Sleep ≠ exposure source thứ 4. Sleep = OFFLINE MAINTENANCE SYSTEM.
    → 6 mechanisms: ~1.5 exposure-based + ~4.5 optimization.
    → Cycle: Waking (build) → Sleep (maintain) → Waking (build on maintained)

  MULTI-STREAM: Content / Value / Entity / Behavior compile SONG SONG.
    → Cùng 1 engine, khác stream → giải thích tại sao trust amplify VALUE
      mà không gate CONTENT (Compile-Taxonomy.md v3.0 §5).

  ENTITY-COMPILED = NEURAL REALITY (Entity-Compiled.md v1.0):
    → Khi compile đủ sâu (40-200h), entity CÓ THẬT trong não
    → Hub-and-spoke: amygdala/hippocampus/PFC form per-entity network
    → Dunbar ~150: giới hạn Entity-Compiled capacity
    → Grief Type A/B/C: mất Entity-Compiled = mất neural reality
    → Entity-Compiled = mechanism chung cho CẢ 3 Compile Types

  Chi tiết architecture: Compile-Taxonomy.md v3.0
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

Chi tiết: Inter-Body-Mechanism.md §3, Self-Pattern-Modeling.md v3.2 §2
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

  HARDWARE-SUBSIDY (Entity-Valence-Dynamics.md v1.1 §5, Body-Coupling.md v3.0):
    → Body hardware cung cấp baseline support "miễn phí" cho operators
    → Ví dụ: oxytocin system → social reward KHÔNG cần PFC effort
    → Hardware-Subsidy = TẠI SAO một số drives mạnh hơn hẳn
    → Khác nhau theo entity type: con > bạn thân > đồng nghiệp > stranger
    → = Evolutionary investment per-relationship

  4 FIRING MODES:
    → Tonic: low-intensity, liên tục, duy trì baseline
    → Phasic: burst cụ thể, response to event
    → Compound: nhiều hệ fire ĐỒNG THỜI (Ví dụ: reunion = oxytocin+dopamine+opioid)
    → Cascade: 1 event trigger chain nhiều systems theo thứ tự
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
   (Why-Body-Knows.md v1.2 — consolidated):

  CHỈ 2 CƠ CHẾ THẬT SỰ KHÁC NHAU:

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TẦNG 1 — DARWINIAN SELECTION (gen-level, triệu năm):
    🟢 Triệu sinh vật × triệu năm × triệu thử nghiệm.
    → Gen "reward pattern đúng" → truyền. Gen "reward sai" → chủ nhân chết.
    → Body HIỆN TẠI = survivor's GPS — đã test triệu route, giữ route đúng.
    → Ví dụ: lửa=đau, ngọt=nutrition, rắn=nguy hiểm, social=reward (wired)
    → Unit: SPECIES population. Speed: nghìn-triệu năm.
    → = Cái bạn CÓ khi sinh ra, TRƯỚC mọi trải nghiệm.
    → LIMIT: calibrate CHẬM → evolution lag.
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TẦNG 2 — HEBBIAN COMPILATION (individual-level, suốt đời):
    🟢 + 🟡: TẤT CẢ learning suốt đời = CƠ CHẾ NÀY.
    → Experience → body-feedback → Hebbian strengthen → compiled.
    → BẤT KỂ input source (tự thử, được dạy, absorb vô thức).

    2 ĐƯỜNG VÀO cho cùng 1 cơ chế Hebbian:

    ┌───────────────────────────┬───────────────────────────┐
    │ 2a DOMAIN CONTACT         │ 2b TRUST-INJECTED         │
    ├───────────────────────────┼───────────────────────────┤
    │ Body tiếp xúc domain      │ Entity khác truyền chunks │
    │ trực tiếp                 │ qua trust amplifier       │
    │                           │                           │
    │ Active: chạm lửa,        │ Bố mẹ dạy, thầy dạy,    │
    │   lái xe, therapist       │   sách, tôn giáo, AI     │
    │ Passive: giọng vùng,     │                           │
    │   norms, gu thẩm mỹ      │                           │
    │                           │                           │
    │ Multi-modal (5 kênh)      │ Thường 1-2 kênh (verbal) │
    │ Domain verify MỖI lần     │ Verify: CHƯA (on trust)  │
    │ KHÔNG cần trust amplifier │ CẦN trust amplifier       │
    │ Compile: THICK            │ Compile: THINNER          │
    │ Speed: CHẬM               │ Speed: NHANH              │
    └───────────────────────────┴───────────────────────────┘

    → 2b inject SEED → 2a verify + DEEPEN = tối ưu (education design)
    → Recursive: existing chunks filter + amplify domain contact
      (expert thấy cái beginner KHÔNG thấy — cùng domain input)

    TRUST MECHANISM CHI TIẾT (Trust.md v1.0, Compile-Taxonomy.md v3.0):
      2b = Trust Compile = Engine + Entity-Valence Bias dominant.
      Trust formation: 4 nguồn (Direct > Observed > Schema > Context).
      Trust = AMPLIFIER, NOT gate: amplify VALUE compile, NOT content compile.
      → 2b CẦN trust vì chunks chưa qua domain verify → body dựa vào
        prediction about entity's reliability (= trust compiled aggregate).
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


  "CULTURE" VÀ "AI" = TÊN GỌI, KHÔNG PHẢI CƠ CHẾ RIÊNG:
    Culture = 2a passive (social environment → compile vô thức) + 2b (accumulated transmission)
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

  Chi tiết: Why-Body-Knows.md v1.2 §3
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
     → Ví dụ: công thức kinh doanh → thất bại nhiều lần → body dần bỏ
     → Timeline: weeks-months

  ② VIOLENT FLIP (fast, traumatic):
     → Betrayal / extreme experience → valence FLIP immediately
     → Deep schema collapse (Valence-Propagation v4.1 §3: violent flip mechanism)
     → Ví dụ: phản bội → chunks person VẪN ĐÓ, valence flip từ + sang -
     → Timeline: instant (1 trial — emotional peak compile)

  ③ BODY DEFENSE (3 automatic circuit breakers):
     → Detachment: cut empathy connection → Valence-Structural decoupling
     → Numbness: threshold habituated → signal no longer registers
     → Avoidance behavior: compiled "tránh xa" pattern
     → = Body self-protect khi override quá nhiều lần


  VALENCE-STRUCTURAL CEILING MECHANISM:

    Có Valence-Structural entities (con, bạn thân = body-level feedback):
      → Valence-Structural entities = natural circuit breaker
      → Override chains bị CHẶN bởi Valence-Structural body-feedback
      → Ví dụ: cha quá mê công việc → con ốm → body-feedback CẮT

    Không có Valence-Structural:
      → Override chains KHÔNG CÓ ceiling tự nhiên
      → Burnout emerges (no body-level signal to stop)
      → Ví dụ: workaholic độc thân → nothing stops the chain

    → Valence-Structural entities = built-in circuit breaker cho complex behavior
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

  Body-Feedback/ folder (17 files, ~27,500L) chứa chi tiết.
  Section này = overview. Chi tiết đầy đủ: Body-Feedback/Body-Feedback.md v3.1


  DUAL-PULL ARCHITECTURE (01-Foundation §2):
    🟡 Schema bị kéo ĐỒNG THỜI bởi 2 lực:
      ① HARDWARE PULL (bảo thủ, muốn smooth): comfort zone, routine
      ② DOMAIN PULL (đòi adapt, map reality): learning, curiosity
    Tension = EVOLUTIONARY FEATURE, not bug.
    CẢ HAI → oscillation → thrive. Chỉ 1 → stagnation hoặc burnout.


  5 Body-Feedback-Preconditions FOR EVALUATIVE SIGNAL (Body-Feedback-Precondition.md v1.0):
    🟡 Evaluative body signal = function of 5 preconditions ĐỒNG THỜI:

    ┌───┬──────────────────────┬──────────────────────────┐
    │ # │ Precondition         │ Failure → subjective     │
    ├───┼──────────────────────┼──────────────────────────┤
    │ 1 │ Directed-Gap         │ "Không cần"              │
    │ 2 │ Chunk-Substrate      │ "Chả hiểu"              │
    │ 3 │ Delta-Gate           │ "Bình thường"            │
    │ 4 │ Match-Range          │ "Quá lạ" / "quá quen"   │
    │ 5 │ Compile-Gate         │ "Ghét dù hiểu"           │
    └───┴──────────────────────┴──────────────────────────┘
    ALL 5 REQUIRED. Direct-State signals KHÔNG cần Body-Feedback-Precondition.


  3 GENUINE DISCOMFORT SOURCES (Body-Feedback §3.3):
    ⭐ CORTISOL KHÔNG GÂY ĐAU. 3 nguồn đau THẬT:
    ① Nociception (physical damage)
    ② Mismatch (schema ≠ reality) — CORE of almost ALL dissonance
       → Split: hardware mismatch → Direct-State, compiled → Evaluative
    ③ Recalibration (neurons adjusting pattern — "gym for neurons")
    → "Reduce cortisol" = WRONG strategy. "Fix mismatch" = RIGHT strategy.
```

---

## §10 — READING GUIDE CHO BODY-BASE/ FOLDER

```
BODY-BASE/ FOLDER OVERVIEW (~70+ files):

  Body-Base.md (THIS FILE)           — Entry point
  ├── Why-Body-Knows.md v1.2         — META: tại sao body đáng tin
  ├── Cortisol-Baseline.md v2.1      — Amplifier mechanism (3,059L)
  ├── Valence-Propagation.md v4.1    — Valence definition + formation + propagation (~918L)
  ├── Entity-Valence-Dynamics.md v1.1 — Per-entity dynamics, 3 firing modes, hardware-subsidy (~1,545L)
  ├── Body-Coupling.md v3.0          — Coupling, 4 bond types, hardware-subsidy, Resonance Decline
  ├── Inter-Body-Mechanism.md v2.0   — 8 principles, Compilable Architecture
  ├── Trust.md v1.0                  — Trust = compiled prediction, meta-dimension (~1,134L)
  │
  ├── Body-Feedback/                 — Signal architecture (17 files, ~27,500L)
  │   ├── Body-Feedback.md v3.1      — Synthesis entry point
  │   ├── Body-Feedback-Mechanism.md v2.1 — Chunk dynamics, Body-Need aggregate
  │   ├── Body-Feedback-Label.md v2.1 — Vocabulary reference (3-tier)
  │   ├── Body-Feedback-Precondition.md v1.0 — 5 preconditions, WHEN signal fires
  │   ├── Gap-Direction.md v2.0      — Gap có hướng cụ thể
  │   ├── Gap-Body-Need.md v1.0      — 3 satiation types, ENGINE/ROAD/VEHICLE
  │   ├── Gap-Distribution-Profile.md v1.1 — 5-parameter, technology fill
  │   ├── Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State, 5 Profiles
  │   ├── Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State Dissonance
  │   ├── Reward-Calibration.md v1.1 — Goldilocks per-gap, 6 mechanisms
  │   ├── Hidden-Quality-Perception.md v1.0 — 2 types, Dunning-Kruger meta
  │   ├── Action-Space.md v1.0       — Supply-side, 4 trục, DEMAND × SUPPLY
  │   ├── Drill-Evolutionary-Sensor-Architecture.md v1.0 — WHY architecture
  │   ├── Drill-Body-Feedback/01-Foundation.md — Dual-Pull, Interface Loop
  │   ├── Drill-Body-Feedback/02-Dissonance.md — 14 levels, trauma loop
  │   ├── Drill-Body-Feedback/03-Reward.md — Body-Feedback-Precondition, ô tô paradox
  │   └── Drill-Body-Feedback/04-Integration.md — Unified cycle, walkthroughs
  │
  ├── Feeling/                       — PFC observation system (~7,700L)
  │   ├── Feeling.md v3.0            — Central reference (WHAT + HOW)
  │   ├── Body-Knowing.md v1.0       — Compiled knowing, 3 directions, Dual Check
  │   ├── Feeling-Mechanism-Deep-Draft.md  — 8-step flow, reward
  │   ├── Feeling-Sources-Draft.md         — 10+ channels, 50+ examples
  │   ├── Feeling-Accuracy-Draft.md        — Error modes, literacy
  │   ├── Feeling-Chunk-Bridge-Draft.md    — Bidirectional mapping
  │   ├── Feeling-Literacy-Training-Draft.md — 5-stage training
  │   ├── Feeling-Research.md        — Research foundation
  │   ├── Drill-Feeling-Dev/         — 124 examples trajectory
  │   └── Drill-Feeling-Knowning/    — 6 themes + synthesis
  │
  ├── Chunk/                         — Chunk system (~55,000L)
  │   ├── Chunk.md v3.0              — Core reference (4-phase lifecycle)
  │   ├── Compile-Taxonomy.md v3.0   — 1 Engine + 3 Modulators, 3 Compile Types
  │   ├── Compile-Sleep.md v1.0      — Sleep Maintenance (6 mechanisms, offline)
  │   ├── Background-Pattern.md v2.0 — Triple Bias, valence system, shiftability
  │   │
  │   ├── Drill-Chunk/               — Deep analysis drills
  │   │   ├── 99-Master-Synthesis.md — Unified lifecycle
  │   │   ├── 09-Learning-Cycle.md   — Chu kỳ học
  │   │
  │   ├── Agent-Mechanism/           — Per-entity mechanism (11 files)
  │   │   ├── Agent-Mechanism.md v2.1 — Master: 10 dimensions
  │   │   ├── Self-Pattern-Modeling.md v3.2 — Solo simulation, 1 mechanism × 3 dimensions
  │   │   ├── Entity-Compiled.md v1.0 — Neural reality, formation, Dunbar
  │   │   ├── Entity-Access.md v1.2   — Gradient Mức 0-5
  │   │   ├── Entity-Access-Excess.md v1.0 — Excess territory, addiction
  │   │   ├── Entity-Access-Calibration.md v1.0 — Self-regulation, hardware-subsidy
  │   │   ├── Bond-Architecture.md v2.0 — 1 mechanism × 4 bond types
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
  │   └── Anchor-Schema-Extreme-Example.md — Failure modes
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
    2. Chunk/Chunk.md v3.0
    3. Valence-Propagation.md v4.1
    3b. Entity-Valence-Dynamics.md v1.1 (companion)
    4. Body-Coupling.md v3.0
    5. Cortisol-Baseline.md v2.1
    6. Inter-Body-Mechanism.md v2.0

  Trust + Compile Architecture deep dive (~3-4 giờ):
    1. Trust.md v1.0 (trust mechanism — 3 sub-dimensions, formation, dynamics)
    2. Compile-Taxonomy.md v3.0 (1 Engine + 3 Modulators)
    3. Compile-Sleep.md v1.0 (Sleep Maintenance, 6 mechanisms)
    4. Chunk/Chunk.md v3.0 (chunk substrate)

  Agent-Mechanism deep dive (~4-6 giờ):
    1. THIS FILE §3-§4 (Model 3+1, compile)
    2. Entity-Compiled.md v1.0 (neural reality)
    3. Entity-Access.md v1.2 (gradient model)
    4. Bond-Architecture.md v2.0 (4 bond types)
    5. By-Product-Gap-Resonance.md v1.4 (mutual match)
    6. Resonance-Sustainability.md v1.0 (sustainability)
    7. Self-Pattern-Modeling.md v3.2 (solo simulation)

  Feeling system (~2-3 giờ):
    1. THIS FILE §1-§2
    2. Feeling/Feeling.md v3.0
    3. Body-Feedback/01-Foundation.md §5 (body-feedback vs feeling)
    4. PFC/Self-Observation.md v1.0 (APPLICATION-3, keystone)

  Framework theory (~2 giờ):
    1. THIS FILE §1-§4 (foundations + core principles + compile)
    2. PFC/PFC-Function.md
    3. PFC/Simulation-Engine.md v1.2
    4. Neural-Architecture.md
    5. Why-Body-Knows.md

  Inter-Body deep dive (~2 giờ):
    1. THIS FILE §1.2-§1.3 (3 foundations + body-need)
    2. Inter-Body-Mechanism.md v2.0
    3. Body-Feedback-Mechanism.md v2.1
    4. Entity-Valence-Dynamics.md v1.1 §2 (Entity-Compiled)
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
  ✓ Pain 2-component (Melzack & Casey 1968, Rainville 1997, Price 2000) [v3.3]
  ✓ Placebo/Nocebo mechanism (Wager 2004, Zubieta 2005, Colloca & Benedetti 2005) [v3.3]
  ✓ Negativity bias (Baumeister 2001, Rozin & Royzman 2001) [v3.3]
  ✓ Amygdala fast path ~12ms (LeDoux 1996) [v3.3]
  ✓ Trust 3 antecedents: ability, benevolence, integrity (Mayer, Davis & Schoorman 1995) [v4.0]
  ✓ Trust separable from liking (Colquitt et al. 2007, meta-analysis) [v4.0]
  ✓ Trust builds through repeated interactions (Lewicki et al. 2006) [v4.0]
  ✓ Trust asymmetry: hard to gain, easy to lose (Slovic 1993) [v4.0]
  ✓ Betrayal trauma (Freyd 1996) [v4.0]
  ✓ Epistemic trust in children (Csibra & Gergely 2009) [v4.0]


🟡 MEDIUM CONFIDENCE (Framework Synthesis):

  ⚠ "Body evaluates patterns not reality" as UNIFIED principle
    (each case established, unifying integration = novel)
  ⚠ Model 3+1 (components established, 3+1 organization = novel)
  ⚠ "PFC = director, body = compiler" framing
    (roles established, metaphor = novel)
  ⚠ Trust as BRIDGE component (mechanism established, positioning = novel)
  ⚠ L0-L1 substrate model (components established, organization = novel)
  ⚠ 2-tier + 2-pathway calibration model (each component established, integration = novel)
  ⚠ Blackbox-1 + Blackbox-2 convergence (novel insight from Drill §26)
  ⚠ Circuit breaker 3 pathways (mechanisms established, taxonomy = novel)
  ⚠ Dual-pull as architectural principle (each pull established, 2-force = novel)
  ⚠ 5 Body-Feedback-Preconditions model (each precondition grounded, ALL-5 = novel)
  ⚠ 3 Loại compile taxonomy (components established, taxonomy = novel)
  ⚠ Valence-Structural ceiling mechanism (mechanism plausible, not directly tested)
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
  ⚠ Hardware-Subsidy as named mechanism (oxytocin/opioid 🟢, concept = 🟡) [v3.2]
  ⚠ 4 firing modes Tonic/Phasic/Compound/Cascade (neurochemistry 🟢, 4-mode taxonomy = 🟡) [v3.2]
  ⚠ 3 Satiation types ENGINE/ROAD/VEHICLE (receptor dynamics 🟢, metaphor = 🟡) [v3.2]
  ⚠ Simulation-Engine 3-component model (PFC sim research 🟢, formalization = 🟡) [v3.2]
  ⚠ Evaluative/Direct-State Dissonance = orthogonal dimension (pain 2-comp 🟢, unification = 🟡) [v3.3]
  ⚠ Mismatch Splitting: hardware vs compiled sub-types (each grounded, splitting = 🟡) [v3.3]
  ⚠ Numbness-Proof ↔ Burnout-Proof symmetry (each side grounded, symmetric framing = 🟡) [v3.3]
  ⚠ Asymmetric Transition Speed: reward→dissonance FAST, reverse SLOW (negativity bias 🟢, localization = 🟡) [v3.3]
  ⚠ E₀→E₃ applied to BOTH reward + dissonance (evaluation complexity, not reward-specific = 🟡) [v3.3]
  ⚠ Clinical mappings: dissociation/alexithymia/anxiety/chronic pain via 2-type (clinical 🟢, mapping = 🟡) [v3.3]
  ⚠ Placebo/Nocebo = Evaluative Gates Direct-State proof for dissonance (placebo 🟢, architecture = 🟡) [v3.3]
  ⚠ Trust = compiled prediction about reliability (Mayer 🟢, framing = 🟡) [v4.0]
  ⚠ Trust 3 sub-dimensions: Authority/Competence/Intention (Mayer 🟢, Authority addition = 🟡) [v4.0]
  ⚠ 1 Engine + 3 Modulators compile architecture (Hebbian 🟢, architecture unification = 🟡) [v4.0]
  ⚠ Trust = Amplifier NOT Gate (Hebbian 🟢, gate/amplifier distinction = 🟡) [v4.0]
  ⚠ Sleep = 6-mechanism maintenance system (Walker 🟢, 6-mechanism taxonomy = 🟡) [v4.0]
  ⚠ Self-Observation gradient Mức 0-6 (interoception 🟢, gradient formalization = 🟡) [v4.0]
  ⚠ Self-Observation Keystone Property: fail → cascade 5+ systems (alexithymia 🟢, cascade model = 🟡) [v4.0]
  ⚠ Multi-Stream compile: Content/Value/Entity/Behavior (neuroscience 🟢, 4-stream taxonomy = 🟡) [v4.0]


🔴 LOW CONFIDENCE:

  ⚠ Body accuracy "~90%" estimate (qualitative, not measurable)
  ⚠ Vô thức "~95%" / PFC "~5%" ratio (heuristic, not measured)
  ⚠ Goldilocks zone boundaries (inverted-U established, dynamic per person/context)
  ⚠ "Melody hay" sustainability prediction (logical but untested)
```

---

## §12 — CROSS-REFERENCES

```
WITHIN BODY-BASE/ FOLDER:
  Why-Body-Knows.md v1.2    — 2-tier + 2-pathway calibration, coherence ≠ truth, Simulation-Engine
  Cortisol-Baseline.md v2.1 — amplifier mechanism, 10 touchpoints, direction > level
  Valence-Propagation.md v4.1 — valence definition, formation, propagation (companion: Entity-Valence-Dynamics.md v1.1)
  Body-Coupling.md v3.0     — coupling, 4 bond types, hardware-subsidy, Resonance Decline, anti-suppress
  Trust.md v1.0              — compiled prediction, 3 sub-dimensions, formation 4 nguồn, dynamics asymmetry, 29 citations
  Body-Feedback/            — signal architecture, Dual-Pull, Body-Feedback-Precondition, trauma loop
  Body-Feedback-Mechanism.md v2.1 — chunk dynamics, Body-Need aggregate, 3 dynamics
  Body-Feedback-Label.md v2.1 — vocabulary reference, 3-tier labels
  Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State Dissonance, mismatch split, clinical
  Body-Feedback-Precondition.md v1.0 — 5 preconditions, WHEN signal fires, conjunction logic
  Gap-Body-Need.md v1.0     — 3 satiation types, ENGINE/ROAD/VEHICLE, entity-gap matching
  Gap-Distribution-Profile.md v1.1 — 5-parameter, technology fill, PFC budget
  Hidden-Quality-Perception.md v1.0 — 2 types (Expert+Leader), Dunning-Kruger meta
  Reward-Signal-Architecture.md v2.1 — Evaluative:Direct-State ratio, reward calibration
  Feeling/                  — PFC observation interface, 7-layer fidelity
  Feeling/Body-Knowing.md v1.0 — compiled knowing, 3 directions, Dual Check
  Chunk/Chunk.md v3.0       — sole substrate, 4-phase lifecycle, Compile Architecture
  Chunk/Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators, 3 Compile Types
  Chunk/Compile-Sleep.md v1.0 — Sleep Maintenance, 6 mechanisms, offline system
  Background-Pattern.md v2.0 — Triple Bias, valence system, pattern shiftability
  Schema/                   — observation parameter, Anchor-Schema
  Melody Lens/              — metaphor system, Personal-Melody

AGENT-MECHANISM/ FOLDER (11 files):
  Agent-Mechanism.md v2.1   — master: 10 dimensions per-entity
  Self-Pattern-Modeling.md v3.2 — solo simulation, 1 mechanism × 3 dimensions
  Entity-Compiled.md v1.0   — neural reality, formation 40→200h, Dunbar ~150, grief A+B+C
  Entity-Access.md v1.2     — gradient Mức 0-5, per-entity access model
  Entity-Access-Excess.md v1.0 — excess territory, when access becomes addiction
  Entity-Access-Calibration.md v1.0 — self-regulation, hardware-subsidy, failure modes
  Bond-Architecture.md v2.0 — 1 mechanism × 4 bond types, Resonance Decline, gap-clone proof
  By-Product-Gap-Resonance.md v1.4 — mutual match, 5 drills, sustainability bridge
  Resonance-Sustainability.md v1.0 — 4-layer, 3 conditions, 3 modalities, U-curve
  Resonance-Per-Entity.md v1.0 — per-relationship dynamics, hardware-subsidy spectrum
  By-Product-Scale.md v1.0  — 1 mechanism × 3 scales (pair/hub/institutional)

INTER-BODY:
  Inter-Body-Mechanism.md v2.0 — 8 principles, Compilable Architecture, 5-channel, 3-cost
  (Drill files → Core-Deep-Dive/backup/Drill-Inter-Body-Mechanism/)

PFC/ FOLDER:
  PFC-Function.md           — 24 functions, 95/5 split, "PFC tạo context"
  PFC-Operations.md v1.3    — Hold/Suppress, Budget, Compiled Quality
  Simulation-Engine.md v1.2 — 1 engine, 3 components, 3 axes, N applications
  Self-Observation.md v1.0  — APPLICATION-3 (Self, Present, Observe), Mức 0-6, Keystone
  PFC-Label.md v1.1         — vocabulary reference, 13 domains, 3-tier labels
  PFC-Hardware.md           — COMT, DRD4, NE, hardware variation
  Attention-Spectrum.md v2.1 — attention hardware, COMT/DRD4
  PFC-Development.md        — lifecycle, training
  PFC-Hold-Dimensions.md    — tại sao ~4±1 (6 convergent forces)
  Logic-Feeling.md          — Body-Knowing + observer labels, Compiled/Fresh spectrum
  Logic-Feeling-Balance.md  — meta-principle, infinite regress, mỗi người tự cân bằng
  Imagination/              — Imagine-Final v3.1, Somatic-Articulation-Loop

OBSERVATION/ FOLDER:
  Novelty.md, Threat.md, Boredom.md v2.0, Drive.md — observation parameters
  Empathy.md v4.0, Connection.md v5.0, Status.md, Protect.md — social parameters
  Meaning.md, Autonomy.md, Gratitude.md, Obligation.md — higher-order parameters
  Liking-Wanting.md         — bridge file, 6 wanting mechanisms

NEURAL + DOMAIN:
  Neural-Architecture.md    — A/B/C/D 4-zone physical map
  Neural-Processing-Flow.md — signal pathway detail
  Domain/Domain.md          — domain reality, lean epistemological
  Collective/               — Coordination-Node v1.2, Collective-Body v2.2, etc.

DRILL SOURCES:
  Drill-Draft/Drill-Compile-Short-Collective.md — §6b, §19, §21, §23, §26
  Drill-Draft/Drill-L2-Phenomenology-Emptiness.md — L2, emptiness, 2 cơ chế nền
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
  Mayer, Davis & Schoorman (1995) — trust 3 antecedents [v4.0]
  Colquitt et al. (2007) — trust separable from liking [v4.0]
  Lewicki et al. (2006) — trust builds through repeated interactions [v4.0]
  Slovic (1993) — trust asymmetry [v4.0]
  Freyd (1996) — betrayal trauma [v4.0]
  Csibra & Gergely (2009) — epistemic trust [v4.0]
```

---

> **Body-Base.md v4.0**
>
> Entry point cho toàn bộ Body-Base system.
> Foundation layer: mọi thứ trong framework build trên body-base.
>
> v4.0 tích hợp 4 file nền tảng mới:
>   Compile-Taxonomy v3.0 (1 Engine + 3 Modulators), Compile-Sleep v1.0 (Sleep Maintenance),
>   Trust v1.0 (compiled prediction, 3 sub-dimensions, dynamics), Self-Observation v1.0 (APPLICATION-3, keystone).
>
> Core principles (v4.0):
>   §1: 3 Hardware Foundations → Compilable Architecture
>   §2: Body evaluates PATTERNS, not reality (Treisman 1977 + 6 cases)
>   §3: Model 3+1 — Trust REWRITE: definition + 3 sub-dimensions + dynamics + formation
>   §4: 1 Engine + 3 Modulator Configurations + Compiled/Fresh axis
>   §5: L0-L1 substrate + Hardware-Subsidy + 4 firing modes
>   §6: 3-Layer Evolution (Hardware → Compiled → Cultural)
>   §7: 2-tier calibration + Trust mechanism detail
>   §8: Circuit breaker (3 pathways, Valence-Structural ceiling)
>   §9: Body-feedback overview (rút gọn — pointer to Body-Feedback.md v3.1)
>
> Schema phục vụ body-base. Body is final arbiter of value.
>
> Phiên bản: v4.0, 2026-06-02.
> Changelog v1.0-v3.4: backup/Body-Base-v3.4-changelog.md
