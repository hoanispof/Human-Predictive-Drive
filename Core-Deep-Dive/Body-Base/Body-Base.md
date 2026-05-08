---
title: Body-Base — Entry Point cho Toàn Bộ Body-Base System
version: 2.0
created: 2026-04-14 (v1.0 BASIC — Phase C)
rewritten: 2026-05-08 (v2.0 — Phase E1 rewrite, incorporates Drill S1-S6 insights)
status: v2.0 REFERENCE FILE
scope: |
  ENTRY POINT cho toàn bộ Body-Base/ folder (~60+ files).
  Body-Base LÀ GÌ + Core Principles + Unified Model 3+1 + L0-L1-L3 Overview
  + Body Compile + 4-Tier Calibration + Circuit Breaker + Body-Feedback Overview.
  v2.0 KEY ADDITIONS từ Drill S1-S6 (70 insights, 26 GAPs):
    ① "Body evaluates PATTERNS, not reality" — principle nền tảng (Drill §6b + §21)
    ② Unified Model 3+1: Vô thức / PFC / Trust / External Tools (Drill §23)
    ③ Body Compile: PFC = director, body = compiler (Drill §19)
    ④ Circuit Breaker mechanism — 3 pathways (Drill §6b)
    ⑤ BB1 + BB2 convergence: compile (structural) + valence (evaluative) = ĐỒNG THỜI (Drill §26)
purpose: |
  Người đọc NÊN ĐỌC FILE NÀY TRƯỚC khi đi vào bất kỳ sub-file nào.
  File này consolidate, KHÔNG duplicate — detail ở sub-files.
  Foundation layer cho TOÀN BỘ framework.
previous_version: backup/Body-Base-v1.md (v1.0 BASIC 2026-04-14)
parent: Core-Deep-Dive/ (foundation file)
dependencies:
  - Why-Body-Knows.md — 4-tier calibration, coherence ≠ truth
  - Body-Feedback/Body-Feedback.md — Dual-Pull, H10, Interface Loop
  - Body-Feedback/01-Foundation.md — body-feedback vs feeling 2-layer
  - Feeling/Feeling.md v2.0 — 7-layer fidelity, PFC observation
  - Chunk/Chunk.md v2.0 — sole substrate, 4 compile mechanisms
  - Valence-Propagation.md v1.3 — per-entity valence, 2-luồng
  - Body-Coupling.md v1.0 — coupling mechanism, extension/entanglement
  - Cortisol-Baseline.md v2.0 — amplifier, direction > level
  - PFC/PFC-Function.md — 24 functions, 95/5 split
  - Neural-Architecture.md — A/B/C/D 4-zone physical map
  - Drill-Draft/Drill-Compile-Short-Collective.md — §6b, §19, §21, §23, §26
  - Drill-Draft/Drill-L2-Phenomenology-Emptiness.md — L2 phenomenology, trống rỗng
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Base — Entry Point cho Toàn Bộ Body-Base System

> **Bạn khát nước → body thiếu hydration.**
> **Bạn cô đơn dù xung quanh đầy người lạ → body thiếu agent depth.**
> **Bạn nghe bài nhạc MỚI → body biết "hay" TRƯỚC PFC.**
> **Bạn bị phản bội → valence flip NGAY dù PFC chưa kịp phân tích.**
> **Bạn "cho đi vô tư" → body ĐANG TÍNH 4 reward chains song song mà PFC không biết.**
>
> Tất cả đều là **body-base** — hệ thống nền tảng mà MỌI THỨ trong framework
> chạy trên đó. Body tính trước. PFC observe sau. Thứ tự KHÔNG bao giờ đảo ngược.
>
> **Core principle (v2.0):**
> Body evaluates PATTERNS, not reality.
> PFC = director. Body = compiler.
> Trust = bridge duy nhất cho complexity vượt 4±1.
> External tools = capacity multiplier ×∞.
>
> **"Con người cần FEEL đúng → AI sẽ giúp PLAN đúng."**

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — BODY-BASE LÀ GÌ
- §2 — CORE PRINCIPLE: Body Evaluates Patterns, Not Reality
- §3 — UNIFIED MODEL: 3 Components + 1 Bridge
- §4 — BODY COMPILE: PFC = Director, Body = Compiler
- §5 — L0-L1-L3 OVERVIEW
- §6 — 4-TIER CALIBRATION
- §7 — CIRCUIT BREAKER MECHANISM
- §8 — BODY-FEEDBACK OVERVIEW
- §9 — READING GUIDE CHO BODY-BASE/ FOLDER
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

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
    [L3 PFC DRIVES]         ← Novelty / Status / Protect (operators)
    [L1 BODY-INPUTS]        ← Body-Base substrate (17 sub-categories)
    [L0 ALIVE THRESHOLD]    ← Survival floor (binary)
    [EVOLUTIONARY SUBSTRATE] ← 2M+ năm calibration


FILE NÀY TRONG FLOW:

  ┌───────────────────────────────────────────────────────────────┐
  │ BODY-BASE.MD (FILE NÀY) — ENTRY POINT                        │
  │                                                                │
  │  Đọc file này TRƯỚC → chọn hướng đi sâu:                     │
  │                                                                │
  │  Mechanism files (HOW):                                        │
  │    Chunk/Chunk.md v2.0     — chunk system (sole substrate)     │
  │    Valence-Propagation.md  — body đánh giá + truyền valence   │
  │    Body-Coupling.md        — coupling sâu với entity           │
  │    Cortisol-Baseline.md    — amplifier mechanism               │
  │                                                                │
  │  Observation files (WHAT PFC SEES):                            │
  │    Feeling/Feeling.md      — PFC observation interface          │
  │    Body-Feedback/          — signal architecture                │
  │                                                                │
  │  Foundation files (WHY):                                       │
  │    Why-Body-Knows.md       — tại sao body đáng tin             │
  │    Neural-Architecture.md  — physical brain map                │
  │                                                                │
  │  Operator files (WHAT DRIVES):                                 │
  │    PFC/PFC-Function.md     — 24 PFC functions                  │
  │    PFC/PFC-Hardware.md     — hardware variation                 │
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

### §1.2 — Substrate Reframe (v7.8)

```
🟡 SUBSTRATE REFRAME (2026-04-14 Phase R, confirmed Drill S1-S6):

  Trước Phase R: channel-based model (~19 channels categorized)
  Sau Phase R: substrate model (3 layers, mechanism-based)

  L0 — ALIVE THRESHOLD:
    Binary. Crossed = death.
    Oxygen (minutes), critical injury (immediate),
    extreme temperature (hours), water (days), starvation (weeks).
    Suppresses ALL other processing khi threatened.

  L1 — BODY-INPUTS VỚI ADAPTIVE BASELINE:
    17 sub-categories (§5 below).
    Each input: evolved baseline + individual baseline (shifted by development).
    Deviation below → dissonance. Deviation above → reward → baseline shifts up.
    3 nhóm: Exteroception (5) + Proprioception (3) + Interoception (9).

  L3 — PFC DRIVES AS OPERATORS:
    Novelty / Status / Protect = operators ON L1 substrate.
    KHÔNG phải layer of needs — là operators điều chỉnh L1 baselines.
    Novelty shifts baselines up (explore). Protect defends baselines (conserve).

  L2 REMOVED (v7.8 reframe):
    Old "Quality layer" collapses into L1 (Novelty-shifted baseline).
    15/15 test cases PASS. 2 parsimony gains.

  Chi tiết substrate: backup/Body-Base-v1.md, Body-Input-Enumeration.md (8,418L)
```

### §1.3 — Architectural Claim: Schema Phục Vụ Body-Base

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

    → Body đúng ~90%+ (patterns calibrated qua 4 tiers — §6 below)
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
  │   24 functions chi tiết: PFC-Function.md                         │
  ├─────────────────────────────────────────────────────────────────┤
  │ COMPONENT 3 (BRIDGE) — TRUST: GATE + MODULATE + CONNECT         │
  │                                                                  │
  │   Trust = per-entity meta-tag trên chunks (VP §2).               │
  │   MỌI trust sources (bản thân, cha mẹ, thầy, tập thể, hệ thống)│
  │   dùng IDENTICAL mechanism — khác verification path.             │
  │                                                                  │
  │   3 FUNCTIONS:                                                   │
  │     GATE: trust = cổng cho external install chunks               │
  │     MODULATE: trust modulate TOÀN BỘ valence profile             │
  │     CONNECT: trust = ONLY mechanism cho complexity > 4±1          │
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
    Framework-Boundaries.md (cần update — E3a).
```

---

## §4 — BODY COMPILE: PFC = Director, Body = Compiler

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

### §4.2 — 3 Loại Compile

```
🟡 3 LOẠI COMPILE (Drill §3 — chi tiết: Compile-Taxonomy.md E4):

  LOẠI A — DIRECT SHORT (~90% daily behavior):
    → Body experience → body compile → chunks form
    → PFC KHÔNG hoặc ÍT tham gia direction
    → VD: habit, skill, routine, emotional conditioning
    → = Phần lớn cuộc sống = Loại A

  LOẠI B — COMPILED EXPERTISE (~5%):
    → PFC-directed compile qua nhiều năm
    → PFC chọn domain + hold + imagine + domain-check
    → Body compile THROUGH PFC direction
    → VD: Einstein physics, chess grandmaster, surgeon skill
    → = Expertise = Loại B

  LOẠI C — INSTALLED + COLLECTIVE:
    → Chunks installed TỪ BÊN NGOÀI (cha mẹ, thầy, sách, AI, văn hóa)
    → 5 external install mechanisms (Chunk.md §2.3):
      Co-attention, Imitation, Social referencing,
      Label installation, Cultural transmission
    → = PHẦN LỚN behavior hàng ngày mà framework CHƯA nhận ra đủ
    → VD: ngôn ngữ, đạo đức, skill xã hội, world knowledge
    → = Loại C = collective hold chain dài, individual compile short

  ⚠️ TRUST = GATE CHO LOẠI C (Drill §4, §20):
    → Cá nhân KHÔNG tự compile chain dài (PFC 4±1 constraint)
    → Tập thể HOLD chain dài (distributed across many individuals)
    → Cá nhân NHẬN từ tập thể qua TRUST gate
    → Trust cao → chunks install. Trust thấp → chunks reject.
    → = GAP 6 (IMPORTANT): Trust gate chưa formalize đủ trong Chunk.md §2.3

  Chi tiết taxonomy: Compile-Taxonomy.md (E4 — chưa viết)
```

---

## §5 — L0-L1-L3 OVERVIEW

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
    → Novelty operator (L3): shifts baselines UP → body cần MORE
    → Loss of elevated baseline → dissonance AT NEW FLOOR
    → Asymmetric: loss hurts ~2x gain (🟢 Kahneman & Tversky 1979)

  Chi tiết substrate: Body-Input-Enumeration.md (8,418L)
```

### §5.3 — L3 PFC Drives as Operators

```
🟡 L3 — 3 DRIVES = OPERATORS ON L1 SUBSTRATE:

  ① NOVELTY DRIVE:
    → Shifts L1 baselines UPWARD (explore, expand)
    → VTA delta detection (🟢 Schultz 1997)
    → Cortisol LOW-MODERATE, domain-pull direction
    → Chi tiết: Observation/Novelty.md

  ② PROTECT DRIVE:
    → DEFENDS L1 baselines (conserve, maintain)
    → Loss aversion (🟢 Kahneman & Tversky 1979)
    → f(replaceability × attachment chunks)
    → Chi tiết: Observation/Protect.md

  ③ STATUS DRIVE:
    → Resource Access Map (evolutionary grounded)
    → Status = PROXY for body-base resource access
    → 350M+ years cross-species
    → Chi tiết: Observation/Status.md

  Drives = OPERATORS, không phải needs:
    → Drives operate ON L1 body-inputs
    → Drives SHIFT baselines, CREATE expectations, GENERATE dissonance
    → Drives KHÔNG phải "tầng riêng biệt" — là functions acting on L1
    → Chi tiết drive integration: Observation/Drive.md
```

---

## §6 — 4-TIER CALIBRATION

```
⭐ TẠI SAO BODY ĐÁNG TIN: 4 TẦNG CALIBRATE CHỒNG LẬP
   (Why-Body-Knows.md — consolidated):

  TIER 1 — EVOLUTION (triệu năm — gen wired):
    🟢 Chọn lọc tự nhiên = trial-error CỰC LỚN.
    → Gen "reward pattern đúng" → truyền. Gen "reward sai" → chủ nhân chết.
    → Body HIỆN TẠI = survivor's GPS — đã test triệu route, giữ route đúng.
    → VD: lửa=đau, ngọt=nutrition, rắn=nguy hiểm (wired)
    → LIMIT: calibrate CHẬM (nghìn-triệu năm). Evolution lag.

  TIER 2 — DEVELOPMENT (suốt đời — experience):
    🟢 + 🟡: Mỗi trải nghiệm = 1 vòng "thử → domain feedback → body calibrate."
    → Chunks tích lũy → body tách chi tiết hơn
    → Ít kinh nghiệm: evaluate "tốt/xấu" (binary, thô)
    → Nhiều kinh nghiệm: evaluate "chỗ này tốt, chỗ kia xấu" (chi tiết)
    → = "Chuyên gia" = body có NHIỀU thước đo hơn, không "thông minh hơn"

  TIER 3 — CULTURE (qua thế hệ — share calibration):
    🟡: Tri thức tích lũy: 1 người thử → mọi người biết.
    → Cha mẹ dạy "đừng chạm lửa" → trẻ biết TRƯỚC khi tự thử
    → Mechanism: External inject (Anchor-Schema §3 nguồn ④) → compile vào chunks
    → LIMIT: culture có thể transmit cả truth VÀ error

  TIER 4 — AI (hiện tại — chunks unlimited):
    🟡: AI = boost Tier 3 × 1000 (speed + breadth + access).
    → AI cho CHUNKS → body VẪN phải check
    → Body check = TẦNG CUỐI luôn cần (AI CÓ THỂ sai)


  ⭐ COHERENCE ≠ TRUTH (3 failure modes):

    Body check COHERENCE (pattern mới khớp cái đã biết?), KHÔNG check TRUTH.

    ① EVOLUTION LAG: body reward ĐÚNG cho environment CŨ, SAI cho MỚI
       → Đường: evolution hiếm → reward "ngọt=quý" → modern dễ → nghiện
       → MXH: ancestral approval hiếm → reward "likes" → modern vô hạn → scroll

    ② CHUNKS NỀN SAI: coherence khớp nhưng nền sai
       → Flat Earth: nhìn thẳng=phẳng → coherent → body "đúng" → SAI domain
       → "Cortisol = stress hormone" → coherent với pop science → SAI actual mechanism

    ③ SCHEMA OVERRIDE: biết sai mà VẪN follow
       → Nghiện: body "biết" xấu → schema "reward" compiled quá mạnh → override
       → Procrastinate: PFC biết cần làm → "scroll=reward" override

    → Body đúng ~90%+ (4 tiers calibrate). Sai ~10% (3 failure modes).
    → EXTERNAL CHECK cần thiết cho 10%: người khác, AI, experiment, domain thật.

  Chi tiết: Why-Body-Knows.md
```

---

## §7 — CIRCUIT BREAKER MECHANISM

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
     → Deep schema collapse (VP §3: violent flip mechanism)
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

## §8 — BODY-FEEDBACK OVERVIEW

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
         Novelty drive, VTA delta, prediction error
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
    │ 3 │ VTA delta threshold  │ "Bình thường"            │
    │ 4 │ Goldilocks zone      │ "Quá lạ" / "quá quen"   │
    │ 5 │ Chunk association tag│ "Ghét dù hiểu"           │
    └───┴──────────────────────┴──────────────────────────┘
    ALL 5 REQUIRED. Missing ANY → signal absent or wrong direction.


  3 NGUỒN KHÓ CHỊU THẬT (Body-Feedback §5):
    ⭐ CORTISOL KHÔNG GÂY ĐAU. 3 nguồn đau THẬT:
    ① Nociception (physical damage)
    ② Mismatch (schema ≠ reality) — CORE of almost ALL dissonance
    ③ Recalibration (neurons adjusting pattern — "gym for neurons")
    → "Reduce cortisol" = WRONG strategy. "Fix mismatch" = RIGHT strategy.


  Chi tiết: Body-Feedback/Body-Feedback.md (entry point cho folder)
```

---

## §9 — READING GUIDE CHO BODY-BASE/ FOLDER

```
BODY-BASE/ FOLDER OVERVIEW (~60+ files):

  Body-Base.md (THIS FILE)           — Entry point
  ├── Why-Body-Knows.md              — META: tại sao body đáng tin
  ├── Cortisol-Baseline.md v2.0      — Amplifier mechanism (3,059L)
  ├── Valence-Propagation.md v1.3    — Per-entity valence + propagation
  ├── Body-Coupling.md v1.0          — Coupling mechanism (1,534L)
  │
  ├── Body-Feedback/                 — Signal architecture (~9,050L)
  │   ├── Body-Feedback.md           — Synthesis entry point
  │   ├── Body-Feedback-Mechanism.md — 4th axis (chunk dynamics)
  │   ├── Gap-Direction.md           — Gap có hướng cụ thể
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
  ├── Chunk/                         — Chunk system (~48,600L)
  │   ├── Chunk.md v2.0              — Core reference
  │   ├── 99-Master-Synthesis.md     — Unified lifecycle
  │   ├── Background-Pattern.md      — 2D: Depth × Density
  │   ├── 09-Learning-Cycle.md       — Chu kỳ học
  │   ├── Agent-Mechanism/           — SPM, Pattern-Resonance
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
    3. Valence-Propagation.md
    4. Body-Coupling.md
    5. Cortisol-Baseline.md

  Feeling system (~2-3 giờ):
    1. THIS FILE §1-§2
    2. Feeling/Feeling.md v2.0
    3. Body-Feedback/01-Foundation.md §5 (body-feedback vs feeling)
    4. Feeling/Feeling-Mechanism-Deep.md

  Framework theory (~2 giờ):
    1. THIS FILE §2-§3 (core principles + unified model)
    2. PFC/PFC-Function.md
    3. Neural-Architecture.md
    4. Why-Body-Knows.md

  Drill insights (~2 giờ):
    1. Drill-Draft/Drill-Compile-Short-Collective.md (§6b, §19, §21, §23)
    2. Drill-Draft/Drill-L2-Phenomenology-Emptiness.md
```

---

## §10 — HONEST ASSESSMENT

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


🟡 MEDIUM CONFIDENCE (Framework Synthesis):

  ⚠ "Body evaluates patterns not reality" as UNIFIED principle
    (each case established, unifying integration = novel)
  ⚠ Model 3+1 (components established, 3+1 organization = novel)
  ⚠ "PFC = director, body = compiler" framing
    (roles established, metaphor = novel)
  ⚠ Trust as BRIDGE component (mechanism established, positioning = novel)
  ⚠ 3-layer substrate model L0/L1/L3 (components established, organization = novel)
  ⚠ 4-tier calibration stacking (each tier established, stacking = novel)
  ⚠ BB1+BB2 convergence (novel insight from Drill §26)
  ⚠ Circuit breaker 3 pathways (mechanisms established, taxonomy = novel)
  ⚠ Dual-pull as architectural principle (each pull established, 2-force = novel)
  ⚠ H10 5-precondition model (each precondition grounded, ALL-5 = novel)
  ⚠ 3 Loại compile taxonomy (components established, taxonomy = novel)
  ⚠ L2 ceiling mechanism (mechanism plausible, not directly tested)


🔴 LOW CONFIDENCE:

  ⚠ Body accuracy "~90%" estimate (qualitative, not measurable)
  ⚠ Vô thức "~95%" / PFC "~5%" ratio (heuristic, not measured)
  ⚠ Goldilocks "40-70%" specific percentages (inverted-U established, cutoffs approximate)
  ⚠ "Melody hay" sustainability prediction (logical but untested)
```

---

## §11 — CROSS-REFERENCES

```
WITHIN BODY-BASE/ FOLDER:
  Why-Body-Knows.md         — 4-tier calibration, coherence ≠ truth, 3 failure modes
  Cortisol-Baseline.md v2.0 — amplifier mechanism, 10 touchpoints, direction > level
  Valence-Propagation.md    — per-entity valence, chain propagation, 2-luồng
  Body-Coupling.md          — coupling mechanism, extension/entanglement, 2D model
  Body-Feedback/            — signal architecture, Dual-Pull, H10, trauma loop
  Feeling/                  — PFC observation interface, 7-layer fidelity
  Chunk/Chunk.md v2.0       — sole substrate, 4 compile mechanisms, 4 connection types
  Schema/                   — observation parameter, Anchor-Schema
  Melody Lens/              — metaphor system, Personal-Melody

PFC/ FOLDER:
  PFC-Function.md           — 24 functions, 95/5 split, "PFC tạo context"
  PFC-Hardware.md           — COMT, DRD4, NE, hardware variation
  PFC-Development.md        — lifecycle, training
  PFC-Hold-Dimensions.md    — tại sao ~4±1 (6 convergent forces)
  Logic-Feeling.md          — 2 processing modes song song
  Logic-Feeling-Balance.md  — meta-principle, infinite regress, mỗi người tự cân bằng
  Imagination/              — Imagine-Final, Somatic-Articulation-Loop

OBSERVATION/ FOLDER:
  Novelty.md, Threat.md, Boredom.md, Drive.md — observation parameters
  Empathy.md, Connection.md, Status.md, Protect.md — social parameters
  Meaning.md, Autonomy.md, Gratitude.md, Obligation.md — higher-order parameters

NEURAL + DOMAIN:
  Neural-Architecture.md    — A/B/C/D 4-zone physical map
  Neural-Processing-Flow.md — signal pathway detail
  Domain/Domain.md          — domain reality, lean epistemological
  Domain/Collective-Purpose.md — cosmic loop

DRILL (source for v2.0):
  Drill-Draft/Drill-Compile-Short-Collective.md — §6b, §19, §21, §23, §26
  Drill-Draft/Drill-L2-Phenomenology-Emptiness.md — L2, trống rỗng, 2 cơ chế nền
  plan-Phase-E-Refinement.md — E1-E5 sequence

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
```

---

> **Body-Base.md v2.0**
>
> Entry point cho toàn bộ Body-Base system.
> Foundation layer: mọi thứ trong framework build trên body-base.
>
> Core principles (v2.0 — from Drill S1-S6):
>   §2: Body evaluates PATTERNS, not reality (Treisman 1977 + 6 cases)
>   §3: Unified Model 3+1 (Vô thức / PFC / Trust / External Tools)
>   §4: PFC = director, body = compiler (PFC 5 roles, 3 loại compile)
>   §5: L0-L1-L3 substrate (17 body-inputs, adaptive baseline)
>   §6: 4-tier calibration (evolution + development + culture + AI)
>   §7: Circuit breaker (3 pathways, L2 ceiling)
>   §8: Body-feedback overview (Dual-Pull, H10, 3 nguồn khó chịu)
>
> Schema phục vụ body-base. Body is final arbiter of value.
> Body đúng ~90%+. External check cho 10% gap.
>
> Phiên bản: v2.0, 2026-05-08.
> Source: Drill S1-S6 (70 insights, 26 GAPs). Phase E1 rewrite.
