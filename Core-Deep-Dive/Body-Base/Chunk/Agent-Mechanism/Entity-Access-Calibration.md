---
title: Entity-Access-Calibration — How Entity-Access Self-Regulates (or Fails To)
version: 1.0
created: 2026-05-22
status: MECHANISM v1.0
scope: |
  CALIBRATION MECHANISM cho Entity-Access:
  Entity-access calibration = Reward-Calibration APPLIED to entity access.
  3-Layer Architecture: Body Signal × Engine Simulation × Feedback Integration.
  Exit Cost = Signal Weight: strongest bond = hardest to calibrate.
  Hardware-Subsidy = Calibration Bias: hormone masks excess.
  Compiled vs Fresh: calibration window. Engine use quality: curiosity vs threat.
  Optimal Zone ≠ Zero C. Per bond type dynamics. 5 failure modes.
  Cannot prescribe. Training + spiral. Per-Mức gradient difficulty.
purpose: |
  Entity-Access.md = GRADIENT MODEL (Mức 0-5, 3-Factor, quality).
  Entity-Access-Excess.md = EXCESS TERRITORY (Mức 5, cơ chế, biểu hiện, fix).
  File NÀY = CALIBRATION MECHANISM: HOW entity-access tự điều chỉnh,
  tại sao khó/dễ per bond type và per Mức level, what enables/blocks calibration,
  và tại sao KHÔNG THỂ prescribe "bao nhiêu entity-access là đủ."
  = "Entity-Access cho biết ACCESS ở MỨC NÀO. Entity-Access-Excess cho biết
  KHI NÀO access trở thành vấn đề. File này cho biết CALIBRATION HOẠT ĐỘNG
  thế nào, TẠI SAO khó, và CÓ THỂ TRAIN."
position: |
  Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/ — cùng folder Entity-Access, Self-Pattern-Modeling, By-Product-Gap-Resonance.
  Entity-Access.md §8 = summary + cross-ref đến file này.
  Entity-Access-Excess.md = WHEN excess territory (companion).
  File này = HOW calibration works (companion).
  Parallel: Reward-Calibration.md = general | File này = applied to entity access.
dependencies:
  - Entity-Access.md v1.1 — PREREQUISITE: 3-Factor Model, Gradient Mức 0-5, A:B:C:D
  - Entity-Access-Excess.md v1.0 — COMPANION: excess territory Mức 5, fix spectrum
  - Entity-Compiled.md v1.0 — FOUNDATION: brain compile agent vào body-base
  - Simulation-Engine.md v1.0 — FOUNDATION: 1 engine, 3 components, reflection/rumination
  - PFC-Operations.md v1.0 — FOUNDATION: Hold/Suppress, Compiled/Fresh, PFC universal
  - Compiled-Fresh.md v2.0 — FOUNDATION: compiled quality, reversal, PFC shared budget
  - Self-Pattern-Modeling.md v3.1 — FOUNDATION: Compiled/Fresh, Self-Pattern-Modeling as Simulation-Engine application
  - Valence-Propagation.md v3.0 §3 — DEFINES Entity-Compiled + 3 subtypes
  - Body-Feedback-Mechanism.md v2.0 §3.3c — FOUNDATION: Gap→Miss baseline
  - Reward-Calibration.md v1.1 — PARALLEL: Goldilocks, cannot prescribe, dynamic equilibrium
  - Logic-Feeling-Balance.md v1.0 — PARALLEL: infinite regress, domain feedback only
  - Connection.md v4.0 — COMPANION: 2-body calibration, bids, mutual phenomenon
  - Social-Calibration.md v1.1 — COMPANION: social system calibration (CHECK function)
  - Empathy.md v2.2 — DOWNSTREAM: burnout as calibration failure
  - Autonomy-Hardware.md v1.1 — FOUNDATION: vmPFC + DRN, autonomy violation detection
  - Gap-Distribution-Profile.md v1.0 — COMPANION: portfolio risk, diversification
  - Self-Created-Threat.md v1.0 — DOWNSTREAM: threat-mode calibration failure
  - AI-Self-Model.md v2.0 — DOWNSTREAM: Dual Check as calibration mechanism
  - Ask-AI.md v3.1 — DOWNSTREAM: body as quality controller = Layer 1 calibration
  - PFC-Label.md v1.0 — VOCABULARY: PFC roles, deprecated terms
  - Body-Feedback-Label.md v2.0 — VOCABULARY: body signal labels
sources:
  - Drill-Entity-Access-Calibration v2.0 (1,159L, 20 insights, 25 citations)
  - Entity-Access.md v1.1 §8 (được tách ra + mở rộng)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Entity-Access-Calibration — How Entity-Access Self-Regulates (or Fails To)

> **Entity-Access Calibration = Reward-Calibration APPLIED to entity access:**
> **"BAO NHIÊU entity-access là ENOUGH?"**
>
> **Quá ít → bond atrophy (no bids → no Entity-Compiled → drift apart).**
> **Quá nhiều → entity autonomy violated (suppress drive riêng).**
> **Goldilocks = vùng giữa. KHÔNG CỐ ĐỊNH.**
>
> **3-LAYER CALIBRATION ARCHITECTURE:**
> **Layer 1 — Body Signal: "tôi đang cảm gì khi muốn access?"**
> **Layer 2 — Engine Simulation: "entity sẽ experience gì nếu tôi access/ép?"**
> **Layer 3 — Feedback Integration: "entity respond thế nào? → adjust?"**
>
> **EXIT COST = SIGNAL WEIGHT:**
> **Bạn bè (Mức 3): exit dễ → "no" = signal mạnh → TỰ calibrate.**
> **Parent→child (Mức 4-5): exit impossible → "no" = signal yếu → chỉ INTERNAL calibration.**
>
> **HARDWARE-SUBSIDY = CALIBRATION BIAS:**
> **Hormone fires → entity-access FEELS justified → C masked as A.**
>
> **Compiled = BELOW PFC → calibration IMPOSSIBLE.**
> **Fresh = PFC active → calibration POSSIBLE.**
>
> **Engine use quality: Curiosity → productive. Threat → rumination → WORSE.**
> **Optimal Zone ≠ Zero C: justified C = NECESSARY (Baumrind, Gottman, Deci & Ryan).**
> **KHÔNG THỂ PRESCRIBE "bao nhiêu là đủ" — domain feedback = trọng tài DUY NHẤT.**

---

## Mục lục

- §0 — THESIS + POSITION
- §1 — CALIBRATION = DYNAMIC EQUILIBRIUM
- §2 — 3-LAYER CALIBRATION ARCHITECTURE
- §3 — EXIT COST = SIGNAL WEIGHT
- §4 — HARDWARE-SUBSIDY = CALIBRATION BIAS
- §5 — COMPILED vs FRESH: CALIBRATION WINDOW
- §6 — ENGINE USE QUALITY: CURIOSITY vs THREAT
- §7 — OPTIMAL ZONE: JUSTIFIED C + BIDS
- §8 — PER BOND TYPE CALIBRATION DYNAMICS
- §9 — 5 CALIBRATION FAILURE MODES
- §10 — CANNOT PRESCRIBE
- §11 — TRAINING + VIRTUOUS/VICIOUS SPIRAL
- §12 — CALIBRATION × ENTITY-ACCESS GRADIENT
- §13 — HONEST ASSESSMENT
- §14 — CROSS-REFERENCES
- §15 — RESEARCH CITATIONS

---

## §0 — THESIS + POSITION

```
⭐⭐⭐ ENTITY-ACCESS CALIBRATION v1.0:

  ENTITY-ACCESS (Entity-Access.md v1.1):
    3-Factor Model: Compiled Engine Mode × Fresh Gap-Need Profile × F3 Access Confidence
    Gradient: Mức 0 (Tool/Service) → Mức 5 (Excess)
    Entity-Owned = PFC LABEL for Mức 4-5 (observation, not mechanism)

  CALIBRATION = HOW ENTITY-ACCESS SELF-REGULATES:

  ① Calibration = dynamic equilibrium: observe → adjust → observe (LOOP)
  ② 3-Layer Architecture: Body Signal × Engine Simulation × Feedback Integration
  ③ Exit Cost = Signal Weight: bạn bè (Mức 3) self-calibrate, parent→child INTERNAL only
  ④ Hardware-Subsidy = Calibration BIAS: hormone → entity-access feels justified → C masked
  ⑤ Compiled entity-access behaviors = BELOW PFC → calibration IMPOSSIBLE until decompile
  ⑥ Fresh entity-access = PFC ACTIVE → calibration POSSIBLE in real-time
  ⑦ Engine use quality: curiosity → productive calibration. Threat → rumination.
  ⑧ Optimal Zone ≠ Zero C: justified C = NECESSARY (structure + responsiveness)
  ⑨ Bids for connection = mild C expression = bond MAINTENANCE
  ⑩ CANNOT prescribe "bao nhiêu là đủ" — infinite regress, domain feedback only
  ⑪ Calibration itself CAN be Generative reward (curiosity → insight → thú vị)
  ⑫ Per Mức level: calibration difficulty ↑ with entity-access depth

  CÂU HỎI FILE NÀY TRẢ LỜI:
    Entity-Access.md: "Entity-access LÀ GÌ? Mechanism thế nào?"
    Entity-Access-Excess.md: "Khi nào entity-access TRỞ THÀNH vấn đề?"
    ★ File này: "Calibration HOẠT ĐỘNG thế nào? Tại sao khó/dễ per Mức level?"

  PARALLEL:
    Reward-Calibration.md = "BAO NHIÊU reward là enough?" (general)
    ★ File này = "BAO NHIÊU entity-access là enough?" (applied)
    Logic-Feeling-Balance.md = "KHÔNG THỂ prescribe balance" (epistemological)
    ★ File này = same principle applied to entity-access calibration

  🟢 Baumrind 1966, Deci & Ryan 2000, Gottman 2001, Fonagy 2002
  🟡 3-Layer Architecture + Exit Cost = Signal Weight = framework synthesis
```

---

## §1 — CALIBRATION = DYNAMIC EQUILIBRIUM

```
⭐⭐ ENTITY-ACCESS CALIBRATION = REWARD-CALIBRATION APPLIED TO ENTITY ACCESS:

  Reward-Calibration.md §5 core:
    → Mọi reward có GOLDILOCKS — quá ít = thiếu, quá nhiều = vấn đề
    → KHÔNG THỂ prescribe — vì person × context × time × gap = ALL dynamic
    → Domain feedback = trọng tài DUY NHẤT
    → Perception-action cycle: observe → adjust → observe → ...

  Entity-Access Calibration CÙNG PATTERN:

    ┌─────────────┬───────────────────────┬────────────────────────────┐
    │ Vùng        │ Entity-access state   │ Hệ quả                    │
    ├─────────────┼───────────────────────┼────────────────────────────┤
    │ UNDER       │ Quá ít access-seeking │ Bond atrophy: no bids →   │
    │             │ "mặc kệ, ai lo nấy" │ no Entity-Compiled formation → drift    │
    ├─────────────┼───────────────────────┼────────────────────────────┤
    │ GOLDILOCKS  │ Access-seeking vừa đủ │ Bond maintained: bids →   │
    │             │ Responsive to entity  │ responses → Entity-Compiled ↑ → bond ↑ │
    │             │ feedback              │ Entity autonomy INTACT     │
    ├─────────────┼───────────────────────┼────────────────────────────┤
    │ OVER        │ Quá nhiều access      │ Entity drive suppressed:   │
    │             │ Ignore entity "no"    │ autonomy violated →        │
    │             │                       │ excess territory (Mức 5)   │
    └─────────────┴───────────────────────┴────────────────────────────┘

    Goldilocks = KHÔNG CỐ ĐỊNH:
      Khác per person (hardware, temperament, attachment history)
      Khác per entity (infant vs teen vs adult child vs partner vs bạn)
      Khác per context (rested vs depleted, crisis vs routine)
      Khác per time (limerence vs 20 years, child 2 tuổi vs 18 tuổi)
      → 4 dimensions ALL dynamic → fixed formula IMPOSSIBLE

  NHƯNG Entity-Access Calibration PHỨC TẠP HƠN general reward calibration:

    ① 2 bodies — not just self-regulation (Connection.md §9)
    ② Power asymmetry — affects signal quality (parent > child)
    ③ Hardware-subsidy — creates BIAS (hormone → overestimate need)
    ④ Compiled patterns — resist change (automatic, below PFC)
    ⑤ PFC = Lawyer — rationalize C as A+B (McNulty 2013)
    → 5 additional complexity factors BEYOND simple reward calibration

  🟡 Entity-access calibration = reward calibration applied = framework synthesis
  🟢 Reward Goldilocks: Reward-Calibration.md §1
  🟢 Dynamic equilibrium: Reward-Calibration.md §5.2
```

---

## §2 — 3-LAYER CALIBRATION ARCHITECTURE

```
⭐⭐⭐ CALIBRATION CẦN 3 LAYERS ĐỒNG THỜI (★ CORE):

  ┌─────────────────────────────────────────────────────────────────────┐
  │ LAYER 1 — BODY SIGNAL (Interoception)                              │
  │                                                                     │
  │ "Tôi đang cảm gì khi muốn access entity?"                         │
  │                                                                     │
  │ Curiosity (A+B): "hmm, con đang thế nào nhỉ?"                     │
  │   → opioid preview → approach → GENUINE access desire              │
  │ Anxiety (C): "con phải ăn, tôi lo quá"                            │
  │   → cortisol high → urgency → SELF-REFERENTIAL gap driving        │
  │ Obligation (D): "mẹ phải lo cho con"                               │
  │   → relief-seeking → compliance → SCHEMA gap driving               │
  │                                                                     │
  │ Interoception DETECT body signal → biết gap source ĐANG active     │
  │ = Simulation-Engine Component 1 (anterior insula readout)          │
  │                                                                     │
  │ ⚠️ REQUIRES: interoceptive accuracy (trainable — Fukushima 2011)  │
  │ ⚠️ FAILS when: alexithymia, habituation, depleted                 │
  ├─────────────────────────────────────────────────────────────────────┤
  │ LAYER 2 — ENGINE SIMULATION (Constructive Simulation)              │
  │                                                                     │
  │ "Nếu tôi access/ép, entity sẽ experience gì?"                     │
  │                                                                     │
  │ Compiled Agent-mode Self-Pattern-Modeling: model entity's internal state                   │
  │   → predict response: "con sẽ feel bị ép → avoidance tag"         │
  │ Imagine-Final: simulate outcome                                     │
  │   → "nếu ép ăn → con ghét ăn dài hạn → bad outcome"              │
  │ = PFC draft prediction BEFORE acting                               │
  │                                                                     │
  │ ⚠️ REQUIRES: Compiled ≥ Agent-mode (Entity-Access.md §1.1)             │
  │ ⚠️ FAILS when: Compiled = Tool-mode (predict behavior, not state)       │
  │   Tool-mode: "con ăn chưa?" (function check, no state model)      │
  │   Agent-mode: "con có đói thật không? con feel gì?" (state model) │
  │                                                                     │
  │ = Simulation-Engine Component 2 (DMN + hippocampus = CPU)          │
  ├─────────────────────────────────────────────────────────────────────┤
  │ LAYER 3 — FEEDBACK INTEGRATION (Response × Adjustment)             │
  │                                                                     │
  │ "Entity respond thế nào? → prediction delta → adjust?"             │
  │                                                                     │
  │ Entity says "no" → prediction delta → 2 paths:                     │
  │   Path A — Integrate: "à, con thật sự no" → adjust → không ép    │
  │   Path B — Override: compiled response fires → "ăn thêm!" → no adj│
  │                                                                     │
  │ ⚠️ REQUIRES: PFC-Fresh state (Compiled-Fresh.md §10)              │
  │ ⚠️ FAILS when: compiled response override (automatic, bypass PFC) │
  │                                                                     │
  │ = Simulation-Engine Component 3 (mPFC model: adjust self-behavior) │
  └─────────────────────────────────────────────────────────────────────┘

  CALIBRATION = ALL 3 LAYERS ĐỒNG THỜI:
    Layer 1: detect own gap source (A/B/C/D)
    Layer 2: predict entity experience (Compiled Agent-mode)
    Layer 3: integrate entity feedback → adjust
    → LOOP: observe → predict → act → entity responds → observe → ...

  FAILURE KHI BẤT KỲ LAYER NÀO FAIL:

    ┌────────────────┬──────────────────────────┬────────────────────────┐
    │ Layer fail     │ Hệ quả                  │ VD                     │
    ├────────────────┼──────────────────────────┼────────────────────────┤
    │ Layer 1        │ Blind to own gap source  │ Mẹ "thương thật" mà   │
    │ (interoception)│ → C invisible → no adjust│ không biết đang anxious│
    ├────────────────┼──────────────────────────┼────────────────────────┤
    │ Layer 2        │ Cannot predict entity    │ Compiled Tool-mode: "con ăn │
    │ (simulation)   │ experience → ép without  │ chưa?" (no state model)│
    │                │ understanding impact     │                        │
    ├────────────────┼──────────────────────────┼────────────────────────┤
    │ Layer 3        │ Entity responds nhưng    │ Con nói "no" → mẹ vẫn │
    │ (feedback)     │ không integrate → repeat │ ép (compiled override) │
    ├────────────────┼──────────────────────────┼────────────────────────┤
    │ All 3          │ Compiled chain → no      │ Mệt + anxious +       │
    │                │ observation at all       │ compiled → auto-pilot  │
    └────────────────┴──────────────────────────┴────────────────────────┘

  🟡 3-Layer Calibration Architecture = framework synthesis
  🟢 Interoceptive accuracy → empathic accuracy: Fukushima 2011 (R14)
  🟢 Simulation-Engine 3 Components: Simulation-Engine.md §1
  🟢 PFC-Fresh universal resource: Compiled-Fresh.md §10
```

---

## §3 — EXIT COST = SIGNAL WEIGHT

```
⭐⭐⭐ TẠI SAO BẠN BÈ TỰ CALIBRATE NHƯNG PARENT→CHILD THÌ KHÔNG (★ CORE):

  CORE INSIGHT:
    Entity's "no" = CALIBRATION SIGNAL
    Signal WEIGHT = f(exit cost × alternative availability)

    Exit cost CAO → entity's "no" = WEAK signal → có thể IGNORE
    Exit cost THẤP → entity's "no" = STRONG signal → PHẢI adjust hoặc mất

  PER MỨC LEVEL (Entity-Access.md §2):

    ┌──────────────┬───────────┬──────────────┬────────────────────────────┐
    │ Bond type    │ Exit cost │ Entity "no"  │ Calibration mechanism     │
    │ (Mức level)  │           │ signal weight│                            │
    ├──────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Bạn bè      │ LOW       │ HIGH         │ EXTERNAL sufficient:       │
    │ (Mức 3)      │           │ (effective)  │ ignore → friend exits →    │
    │              │           │              │ environment FORCES adjust  │
    ├──────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Romantic     │ MODERATE  │ MODERATE     │ MIX external + internal:   │
    │ (Mức 4)      │           │              │ some room for excess       │
    │              │           │              │ before correction kicks in │
    ├──────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Parent→child │ VERY HIGH │ LOW          │ INTERNAL ONLY:             │
    │ nhỏ (Mức 4-5)│ (child    │ (ineffective)│ child can't leave →        │
    │              │ can't exit│              │ Self-Awareness (Trục 2)    │
    │              │           │              │ = ONLY calibration source  │
    ├──────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Parent→adult │ MODERATE  │ MOD→HIGH     │ EXTERNAL returns:          │
    │ child (Mức 4)│ (can exit)│ (effective)  │ "mẹ ơi con busy" = signal │
    │              │           │              │ Adult child CAN exit →     │
    │              │           │              │ signal weight ↑            │
    ├──────────────┼───────────┼──────────────┼────────────────────────────┤
    │ Professional │ MOD→HIGH  │ MODERATE     │ Structural: contract,     │
    │ (Mức 2-3)    │ (career)  │              │ HR, norms = external frame │
    └──────────────┴───────────┴──────────────┴────────────────────────────┘

  CRITICAL INSIGHT FOR PARENTING:
    Parent→child (nhỏ) = ONLY bond type where:
      Power asymmetry = MAXIMUM
      Exit cost for entity = IMPOSSIBLE
      Entity's feedback signal = WEAKEST
      → External calibration = DISABLED
      → ONLY Self-Awareness (internal, Trục 2) can correct excess

    → WHY parenting needs MOST Self-Awareness:
      Not because it's "harder"
      But because EXTERNAL feedback mechanism is DISABLED by power asymmetry
      → Must rely ENTIRELY on internal observation (Trục 2)

    → Bạn bè (Mức 3) KHÔNG CẦN nhiều Self-Awareness:
      Environment tự correct (friend exits if you're too much)
      → Entity-access naturally stays in Goldilocks zone
      → = Self-correcting mechanism

  LIFECYCLE SHIFT (parent→child):
    Con nhỏ (0-6): exit cost = INFINITE → signal weight ≈ 0
    Con lớn (12-18): exit cost ↓ (teen rebellion = PARTIAL exit) → signal ↑
    Con trưởng thành (18+): exit cost = MODERATE → signal = EFFECTIVE
    → "Xa mẹ mới biết thương" = CŨNG LÀ:
      Adult child's ability to exit → mẹ's entity-access FORCED to recalibrate

  🟡 Exit Cost = Signal Weight = framework synthesis
  🟢 Power asymmetry in parenting: Maccoby 1992 (R21)
  🟢 Autonomy support in power-up relationships: Deci & Ryan 2000 (R2)
```

---

## §4 — HARDWARE-SUBSIDY = CALIBRATION BIAS

```
⭐⭐ HARDWARE-SUBSIDY = ANTI-HABITUATION + CALIBRATION BIAS:

  Entity-Access.md §5: Hardware-Subsidy = ANTI-HABITUATION.
  Mẹ→con MAXIMUM subsidy → entity-access DURABLE.

  NHƯNG CÙNG CƠ CHẾ = CALIBRATION BIAS:

    Mechanism:
      Hormone fires (oxytocin, vasopressin) → entity-access FEELS justified
      → "Tôi thương thật" = PARTIALLY TRUE (A hormone = genuine)
      → PFC dùng A (genuine) để JUSTIFY C (self-referential)
      → = Compound signal: A+C fire CÙNG LÚC → PFC KHÔNG TÁCH ĐƯỢC

    VD:
      Mẹ nhìn con:
        A fires: oxytocin (existence reward) → genuine → "thương con"
        C fires: anxiety ("con phải ăn cho mẹ yên") → self-referential
        → Body signal = MIXED (opioid + cortisol CÙNG LÚC)
        → PFC interpret TOÀN BỘ as "thương con" (A explains everything)
        → C INVISIBLE vì A provides "cover story"
        → = Hardware-subsidy MASKS excess entity-access

  SO SÁNH PER BOND TYPE:

    ┌──────────────┬───────────┬───────────────┬─────────────────────────┐
    │ Bond type    │ Hardware-subsidy│ Bias level    │ Detection difficulty     │
    ├──────────────┼───────────┼───────────────┼─────────────────────────┤
    │ Mẹ→con      │ MAXIMUM   │ MAXIMUM       │ HARDEST: A always       │
    │ (Mức 4-5)    │           │               │ present → always "cover" │
    ├──────────────┼───────────┼───────────────┼─────────────────────────┤
    │ Con→mẹ      │ MODERATE  │ MODERATE      │ Moderate: attachment    │
    │ (Mức 4)      │           │               │ drive present but ↓      │
    ├──────────────┼───────────┼───────────────┼─────────────────────────┤
    │ Romantic     │ TEMPORARY │ HIGH→LOW      │ Limerence: VERY HARD    │
    │ (limerence)  │ (hormone) │ (fades)       │ Post-limerence: EASIER  │
    ├──────────────┼───────────┼───────────────┼─────────────────────────┤
    │ Bạn bè      │ ZERO      │ ZERO          │ EASIEST: no hormone =   │
    │ (Mức 3)      │           │               │ clear signal. C = obvious│
    ├──────────────┼───────────┼───────────────┼─────────────────────────┤
    │ Professional │ ZERO      │ ZERO          │ EASIEST: D clear        │
    │ (Mức 2-3)    │           │               │ (contract/obligation)    │
    └──────────────┴───────────┴───────────────┴─────────────────────────┘

  PARADOX — STRONGEST BOND = HARDEST TO CALIBRATE:
    Mẹ→con: Hardware-subsidy MAXIMUM + Exit cost MAXIMUM + Power MAXIMUM
    → 3 factors ALL conspire AGAINST calibration
    → Strongest, most durable bond = most vulnerable to excess
    → = Trivers 1972: parental investment = HIGHEST → bias HIGHEST

    Bạn bè (Mức 3): Hardware-subsidy ZERO + Exit cost LOW + Power PARITY
    → 3 factors ALL SUPPORT calibration
    → Most fragile bond = most naturally calibrated
    → = WHY friendship rarely becomes "toxic" (self-correcting)

  🟡 Hardware-subsidy = calibration bias = framework synthesis
  🟢 Oxytocin × parental bias: Feldman 2012 (R17), Strathearn 2009 (R18)
  🟢 Parental investment theory: Trivers 1972 (R16)
```

---

## §5 — COMPILED vs FRESH: CALIBRATION WINDOW

```
⭐⭐ COMPILED ENTITY-ACCESS = BELOW PFC → CALIBRATION IMPOSSIBLE:

  Compiled-Fresh.md §6 Quality Dimension:
    Genuine-compiled → approach tag → Self-Pattern-Modeling expansive
    Schema-compiled → neutral tag → Self-Pattern-Modeling limited
    Threat-compiled → avoidance tag → Self-Pattern-Modeling biased

  APPLIED TO ENTITY-ACCESS BEHAVIORS:

    ┌───────────────────┬───────────────────────┬──────────────────────────┐
    │                   │ COMPILED              │ FRESH                    │
    │                   │ (automatic)           │ (deliberate)             │
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ PFC role          │ PASSIVE or ZERO       │ ACTIVE (observe+adjust)  │
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ Calibration       │ IMPOSSIBLE (below PFC)│ POSSIBLE (PFC accessible)│
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ Trigger           │ Entity cue → compiled │ Deliberate: "hmm, let me│
    │                   │ response fires auto   │ think about what I feel" │
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ Typical           │ "Ăn thêm!" (auto)    │ "Con có đói thật không?" │
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ Quality           │ Locked (can't shift)  │ Shiftable in real-time   │
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ Cost              │ ≈ 0 (habituated)      │ > 0 (PFC budget needed)  │
    ├───────────────────┼───────────────────────┼──────────────────────────┤
    │ When dominant     │ Depleted, stressed,   │ Rested, curious,        │
    │                   │ routinized            │ practiced                │
    └───────────────────┴───────────────────────┴──────────────────────────┘

  PFC-FRESH = SHARED BUDGET (Compiled-Fresh.md §10):
    PFC = universal resource for ALL activities
    Mệt ở work → PFC budget cho entity-access calibration = GIẢM
    → Compiled entity-access behaviors take over (auto-pilot)
    → = Mikolajczak 2019: burnout → overcontrol OR emotional distance
    → Cả 2 outcomes = calibration FAIL (excess OR under)

  CASCADING EFFECT (Entity-Access.md §9: 4-Trục):
    Trục 4 depleted
    → PFC budget ↓ → Compiled shifts toward Tool-mode
    → Layer 1 (interoception) ↓: body signal ignored
    → Layer 2 (simulation) ↓: Compiled Tool-mode default
    → Layer 3 (feedback integration) ↓: compiled override
    → ALL 3 calibration layers FAIL SIMULTANEOUSLY
    → Entity-access = auto-pilot = excess hoặc withdrawal territory

  DECOMPILE PATH (change compiled entity-access behaviors):
    Compiled-Fresh.md §9: 6-step reversal
    → Require: sustained PFC engagement + body re-experience + new tag
    → Timeline: months to years (therapy-level)
    → = WHY attachment style change IS POSSIBLE but SLOW (Fraley & Shaver 1998)

    Fresh practice → gradually compile NEW patterns:
    → "Observe first, then act" practiced enough → compiles as default
    → = Mentalization training (Bateman & Fonagy 2006): teachable, compiles over time

  🟡 Compiled vs Fresh applied to entity-access calibration = framework synthesis
  🟢 PFC as shared resource: Compiled-Fresh.md §10
  🟢 Parental burnout → outcomes: Mikolajczak et al. 2019 (R10)
  🟢 Attachment change possible: Fraley & Shaver 1998 (R19)
  🟢 Mentalization-Based Therapy: Bateman & Fonagy 2006 (R6)
```

---

## §6 — ENGINE USE QUALITY: CURIOSITY vs THREAT

```
⭐⭐ CÙNG "SELF-OBSERVE ENTITY-ACCESS," KHÁC MODE → KHÁC OUTCOME:

  Simulation-Engine.md §9 (Trapnell & Campbell 1999):
    Reflection (curiosity cortisol) → insight → productive
    Rumination (threat cortisol) → loop → stuck

  APPLIED TO ENTITY-ACCESS CALIBRATION:

  CURIOSITY MODE (productive calibration):
    "Hmm, tại sao mình muốn con ăn thêm nhỉ?"
    → Observe body: "à, mình đang lo, không phải con đang đói"
    → INSIGHT fires → novelty reward (Generative gap fill)
    → Adjust behavior: "ok, con nói no thì thôi"
    → Outcome tốt → confirms approach → MORE curiosity → LOOP
    → = Calibration BECOMES source of Generative reward
    → = "Thú vị" — observation itself IS rewarding

    Cortisol direction: NOVELTY → approach tag
    Body state: relaxed, open, exploratory
    Compiled: Agent-mode (curious about entity's actual state)
    PFC role: observe + simulate + compare + adjust

  THREAT MODE (destructive calibration):
    "Mình có đang kiểm soát quá không? Mình có phải bad parent?"
    → Self-judgment → threat cortisol → ruminate
    → NO insight (threat BLOCKS exploration — Compiled-Fresh.md §6.2)
    → Paradox: trying to calibrate → anxiety → calibration FAILS
    → 3 possible outcomes:
      A) Over-correct: permissive ("mặc kệ, sợ ép") → under → bond atrophy
      B) Freeze: can't act → compiled takes over → ép anyway
      C) Guilt loop: "mình tệ quá" → ruminate → no adjustment
    → = Self-Created-Threat mechanism applied to parenting

    Cortisol direction: THREAT → avoidance tag
    Body state: tense, contracted, defensive
    Compiled: biased (project fear onto entity)
    PFC role: judge + loop + stuck

  ⭐ WHY THIS MATTERS:
    Mọi "parenting advice" kiểu "đừng ép con" without MODE context:
    → Parent receive as THREAT: "tôi đang ép = tôi bad parent"
    → Switch to threat mode → calibration WORSE not better
    → = Parenting guilt epidemic: advice intended to help → triggers threat mode

    EFFECTIVE approach: encourage CURIOSITY about own patterns:
    → "Tại sao mình muốn vậy?" (curiosity) > "mình sai rồi!" (threat)
    → = Fonagy 2002: mentalization training focuses on curiosity, not judgment
    → = Simulation-Engine.md §11: reflection practice = cultivate curiosity

  🟢 Reflection vs Rumination: Trapnell & Campbell 1999 (R7)
  🟢 Reflection → empathy: Joireman, Parrott & Hammersla 2002 (R8)
  🟢 Mentalization as curiosity: Fonagy 2002 (R5)
  🟡 Curiosity vs Threat mode applied to entity-access = framework synthesis
```

---

## §7 — OPTIMAL ZONE: JUSTIFIED C + BIDS

```
⭐⭐⭐ OPTIMAL ENTITY-ACCESS ≠ ZERO C (★ CORE CORRECTION):

  3 RESEARCH LINES CONFIRM justified C = NECESSARY:

  ① BAUMRIND 1966, 1991 — AUTHORITATIVE PARENTING:
    4 styles: Authoritative / Authoritarian / Permissive / Neglectful
    BEST OUTCOMES: Authoritative = HIGH demand + HIGH responsiveness
    NOT Permissive (low demand + high responsiveness)

    Framework mapping:
      Authoritative = justified C + Compiled Agent-mode (demand BUT responsive)
      Authoritarian = C+D dominant + Compiled Tool-mode (demand, no responsiveness)
      Permissive = zero C → under entity-access → child lacks structure
      Neglectful = zero everything → no bond

    → Structure (justified C) IS NECESSARY for child development
    → C itself not problem. C WITHOUT RESPONSIVENESS = problem.

  ② DECI & RYAN 2000 — SELF-DETERMINATION THEORY:
    Autonomy support ≠ absence of structure
    Structure + autonomy support = OPTIMAL
    Structure WITHOUT autonomy support = controlling

    Framework mapping:
      Structure = justified C (parent sets boundary)
      Autonomy support = Compiled Agent-mode (observe entity state, respect drive)
      Control = C without Agent-mode (ignore entity state, impose my gap direction)

    → "Ép uống thuốc" + explain + acknowledge = structure + autonomy
    → "Ép uống thuốc" without explanation = control
    → SAME behavior, DIFFERENT mode → DIFFERENT outcome

  ③ GOTTMAN & DECLAIRE 2001 — BIDS FOR CONNECTION:
    Partners liên tục make "bids" (requests for attention/connection)
    "Turning toward" (respond to bid) → relationship THRIVES
    "Turning away" (ignore bid) → relationship DETERIORATES

    Framework mapping:
      Bid = mild C expression: "tôi muốn access → chủ động hỏi/đề nghị"
      Partner response → calibration signal → adjust
      ZERO bids = ZERO interaction = bond DIES

    → Mild entity-access expression = NECESSARY for bond maintenance
    → ZERO entity-access = relationship death (no bids → no interaction → Entity-Compiled decay)

  ENTITY-ACCESS SPECTRUM REFINED:

    ┌─────────┬──────────────────────┬────────────────┬───────────────────┐
    │ Level   │ Behavior             │ Gap Source      │ Entity Autonomy   │
    ├─────────┼──────────────────────┼────────────────┼───────────────────┤
    │ Under   │ Mặc kệ, không bid   │ Suppress all   │ "Intact" nhưng    │
    │         │ "ai lo nấy"         │                │ NEGLECTED (no bond)│
    ├─────────┼──────────────────────┼────────────────┼───────────────────┤
    │ Mild    │ Call hỏi thăm, bạn  │ A+B dominant   │ INTACT             │
    │         │ bận thì thôi        │                │ (entity says no → │
    │         │                      │                │ accept)            │
    ├─────────┼──────────────────────┼────────────────┼───────────────────┤
    │ Moderate│ Đưa soup, con không │ A+B + justified│ INTACT             │
    │         │ thích thì nấu khác  │ C              │ (adjust to entity) │
    ├─────────┼──────────────────────┼────────────────┼───────────────────┤
    │Justified│ Ép uống thuốc (con  │ Justified C    │ Temporarily        │
    │override │ chưa tự quyết được)│ (entity can't  │ OVERRIDDEN for     │
    │         │ + explain + empathy │ process yet)   │ entity's benefit   │
    ├─────────┼──────────────────────┼────────────────┼───────────────────┤
    │Excessive│ Ép ăn khi con no    │ C dominant     │ VIOLATED           │
    │ (Mức 5) │ "ăn thêm!" no listen│ (my anxiety)   │ (entity's "no"    │
    │         │                      │                │ ignored)           │
    ├─────────┼──────────────────────┼────────────────┼───────────────────┤
    │ Extreme │ Con PHẢI học bác sĩ │ C+D dominant   │ SUPPRESSED         │
    │ (Mức 5+)│ monitor, punish     │ (my gap+schema │ (entity's drive    │
    │         │                      │ override all)  │ replaced by mine)  │
    └─────────┴──────────────────────┴────────────────┴───────────────────┘

  ⭐ JUSTIFIED OVERRIDE vs EXCESSIVE:
    Ranh giới: con's body CÓ THỂ tự xử lý ĐỦ TỐT chưa?
    (Entity-Access.md §5.3)

    CAN'T self-process → C justified (thuốc, safety, basic hygiene)
    CAN self-process → C problematic (career choice, friend choice, food pref.)

    Lifecycle: C justified GIẢM DẦN as entity develops
    Parent GIỎI: shift C→B theo entity's development (→ Compilable-dominant destination)
    Parent STUCK: C stays high dù entity đã capable → excess (Mức 5)

  🟢 Authoritative parenting: Baumrind 1966, 1991 (R1)
  🟢 Structure + autonomy support: Deci & Ryan 2000 (R2)
  🟢 Bids for connection: Gottman & DeClaire 2001 (R3)
  🟡 Optimal Zone ≠ Zero C = framework synthesis
```

---

## §8 — PER BOND TYPE CALIBRATION DYNAMICS

```
⭐⭐ MỖI BOND TYPE CÓ CALIBRATION DYNAMICS RIÊNG:

  BẠN BÈ (Mức 3) — SELF-CALIBRATING:
    Gap source: B dominant (by-product resonance)
    Exit cost: LOW → friend's "no" = effective signal
    Hardware-subsidy: ZERO → no bias, clear signal
    Entity-access: naturally in Goldilocks (environment corrects)
    Calibration needed: MINIMAL (external mechanism sufficient)

    VD: Bạn rủ đi cafe, bạn busy → "ok, lúc khác"
    → Mild C expressed → entity responded → accepted → Goldilocks
    → Nếu insist → bạn annoyed → signal CLEAR → adjust hoặc lose friend

  ROMANTIC (Mức 4) — BIDIRECTIONAL CALIBRATION:
    Gap source: A (hormone, temporary) + B (resonance) + C variable + D variable
    Exit cost: MODERATE → partner's "no" = moderate signal
    Hardware-subsidy: TEMPORARY (limerence) → fades → clearer calibration
    Entity-access: needs ACTIVE calibration from BOTH sides

    Gottman insight: BOTH partners make bids + BOTH respond → mutual calibration
    → Relationship health = f(bid → response ratio) (Gottman: 5:1 positive:negative)

    Demand-Withdraw pattern (Christensen & Heavey 1990):
      When bids escalate → demands → partner WITHDRAWS → demands ↑ → LOOP
      = Entity-access excess from 1 side → partner's feedback = withdrawal
      = Calibration signal EXISTS but IGNORED (escalation override)

    Healthy romantic: "đòi chút" = bid → partner responds → mutual Entity-Compiled ↑
    → Ranh giới: partner CAN say "not now" → ACCEPTED → calibrated

  PARENT→CHILD (Mức 4-5) — INTERNAL CALIBRATION ONLY:
    Gap source: A+B+C+D compound (Entity-Access.md §5.2)
    Exit cost: VERY HIGH (child can't leave)
    Hardware-subsidy: MAXIMUM (hormone bias → C masked)
    Entity-access: needs MOST calibration but has LEAST external correction

    TRIPLE CHALLENGE:
      ① Exit cost max → entity's "no" = weak signal (child can't leave)
      ② Hardware-subsidy max → C masked as A (hormone provides cover story)
      ③ Power max → CAN override entity → excess persists without correction
      → 3 factors ALL conspire against calibration
      → ONLY Self-Awareness (Trục 2) + sufficient PFC resource (Trục 4) can help

    NHƯNG ALSO: parent→child = MOST PRACTICE opportunity
      → Daily interaction = constant calibration opportunities
      → IF curiosity mode → each day = micro-adjustment → gradual improvement
      → = Mentalization in practice: daily life AS training ground (Fonagy 2002)

  PROFESSIONAL (Mức 2-3) — STRUCTURED CALIBRATION:
    Gap source: D dominant (obligation, contract)
    Exit cost: MODERATE (career consequences)
    Hardware-subsidy: ZERO
    Entity-access: LOW (mostly Compiled Tool-mode)
    Calibration: EXTERNAL structures (HR, norms, contracts) → prescribed

    VD: Boss entity-access toward employee
    → Overtime demands = C (boss's gap through employee's time)
    → Labor law = external calibration mechanism (prescribe limits)

  🟡 Per bond type calibration dynamics = framework synthesis
  🟢 Demand-Withdraw: Christensen & Heavey 1990 (R4)
  🟢 Bid-response ratio: Gottman & DeClaire 2001 (R3)
  🟢 Mentalization training: Fonagy 2002 (R5)
```

---

## §9 — 5 CALIBRATION FAILURE MODES

```
⭐⭐ 5 FAILURE MODES — KHÁC SOURCE, KHÁC FIX:

  MODE 1 — BLIND (Layer 1 fail):
    Cannot detect own gap source → entity-access feels "all genuine"
    Source: low interoceptive accuracy, alexithymia, habituated signals
    Looks like: "Tôi thương thật mà!" (PFC cannot observe C beneath A)
    Fix: interoception training, body awareness practice, Focusing (Gendlin 1978)
    Timeline: months (body-readout skill, trainable — Fukushima 2011)

  MODE 2 — TOOL-MODE (Layer 2 fail):
    Compiled = Tool → cannot model entity's internal state → act without predicting impact
    Source: Compiled never developed for this entity, or degraded by depletion
    Looks like: "Con ăn chưa?" (function check, not "con feel gì?")
    Fix: Agent-mode practice, deliberate curiosity about entity's state
    Timeline: weeks-months (Compiled shift, requires sustained Fresh practice)

  MODE 3 — OVERRIDE (Layer 3 fail):
    Entity responds but compiled pattern fires → feedback NOT integrated
    Source: deeply compiled entity-access behaviors, anxiety-compiled chains
    Looks like: Con says "no" → mẹ "ăn thêm đi!" (automatic, no pause)
    Fix: decompile (Compiled-Fresh.md §9), therapy, sustained new practice
    Timeline: months-years (decompile + recompile is SLOW)

  MODE 4 — DEPLETED (Cascading fail):
    PFC resource gone → all 3 layers drop → auto-pilot
    Source: work stress, sleep deprivation, burnout, chronic load
    Looks like: "Tối về = mệt → compiled → ép → guilt → more stress"
    Fix: resource restoration (sleep, support, reduce load)
    Timeline: days-weeks (if temporary), months (if chronic burnout)
    → = Mikolajczak 2019: burnout intervention = restore resource first

  MODE 5 — THREAT-MODE (Engine quality fail):
    Calibration ATTEMPTED with threat cortisol → rumination → worse
    Source: parenting guilt, "am I controlling?" anxiety, perfectionism
    Looks like: "Mình có phải bad parent không?" → freeze OR overcompensate
    Fix: mode switch (threat → curiosity), normalize imperfection
    Timeline: variable (mode switch can be fast IF recognized)
    → = Most FIXABLE failure mode (just change how you observe, not what)

  COMPOUND FAILURE (most common in reality):
    Modes combine: depleted (M4) → blind (M1) + tool-mode (M2) + override (M3)
    = 4-Trục cascading (Entity-Access.md §9):
      Trục 4 depleted → Trục 1 DROP → Trục 2 DROP → Trục 3 shift C → ÉP
    Fix: must address RESOURCE first (M4), then other modes become accessible

  🟡 5 failure modes taxonomy = framework synthesis
  🟢 Burnout intervention: Mikolajczak et al. 2019 (R10)
  🟢 Interoception training: Fukushima 2011 (R14), Gendlin 1978 (R15)
```

---

## §10 — CANNOT PRESCRIBE

```
⭐⭐ ENTITY-ACCESS CALIBRATION = CANNOT PRESCRIBE:

  Logic-Feeling-Balance.md §6-7:
    → Thử prescribe → mỗi rule có blind spot
    → Thử meta-rule → meta-rule cũng có blind spot
    → = Infinite regress → KHÔNG CÓ điểm dừng

  Applied to entity-access:
    Thử prescribe "entity-access nên ở mức X cho bond type Y"
    → Fail vì:
      ① Person khác → threshold khác (hardware, temperament, history)
      ② Entity khác → need khác (infant vs teen vs adult vs partner)
      ③ Context khác → capacity khác (rested vs depleted)
      ④ Time khác → stage khác (limerence vs 20 years)
      → 4 dimensions ALL dynamic → fixed formula IMPOSSIBLE

  VÀ ĐÂY LÀ BÌNH THƯỜNG (Reward-Calibration.md §5.3):
    Nếu entity-access calibration CÓ THỂ prescribe hoàn hảo:
      → Không cần observe entity's response
      → Không cần adjust behavior
      → Không cần relationship (= automaton)
      → Không cần SỐNG qua trải nghiệm
    = Prescribe hoàn hảo = omniscience
    = Dynamic calibration = ĐÚNG, BÌNH THƯỜNG, EXPECTED

  FILE NÀY GIÚP GÌ (dù không prescribe):
    → NHẬN DIỆN: 3-Layer nào đang fail? (§2)
    → HIỂU: tại sao bond type này khó calibrate hơn? (§3, §4, §8)
    → NHẬN DIỆN: mode nào đang chạy? curiosity hay threat? (§6)
    → NHẬN DIỆN: entity-access đang ở vùng nào? under/Goldilocks/over (§7)
    → TRÁNH: failure mode nào đang active? (§9)
    → = DESCRIBE, KHÔNG prescribe (Logic-Feeling-Balance.md §8.1)

  🟡 Cannot prescribe applied to entity-access = framework synthesis
  🟢 Infinite regress: Logic-Feeling-Balance.md §6-7
  🟢 Domain feedback = only arbiter: Reward-Calibration.md §5.2
```

---

## §11 — TRAINING + VIRTUOUS/VICIOUS SPIRAL

```
⭐⭐ CALIBRATION = TRAINABLE SKILL → COMPOUND IMPROVEMENT:

  Simulation-Engine.md §11: 1 component training → N applications improve.
  Entity-access calibration = SPECIFIC application of same principle.

  TRAINING TARGETS:

    ① INTEROCEPTION (Layer 1):
      Body-scan meditation, Focusing (Gendlin 1978)
      → Better body-readout → detect gap source earlier
      → "Tôi đang anxious" detectable BEFORE behavior fires
      → 🟢 Fukushima 2011: interoceptive accuracy → empathic accuracy

    ② Compiled DEPTH (Layer 2):
      Deliberate curiosity: "entity đang feel gì nhỉ?"
      → Practice Agent-mode (model internal state, not just behavior)
      → More diverse interaction → sharper models (Mitchell 2006)
      → 🟢 Fonagy 2002: mentalization training improves relationship quality

    ③ REFLECTION PRACTICE (Engine use quality):
      Cultivate curiosity orientation (Trapnell & Campbell 1999):
      → Replace "mình sai rồi" with "tại sao mình feel vậy?"
      → = Switch cortisol direction: threat → novelty
      → 🟢 Joireman et al. 2002: self-reflection → empathy correlation

    ④ DECOMPILE + RECOMPILE (Layer 3):
      Therapy (MBT: Bateman & Fonagy 2006)
      → Decompile old compiled patterns → recompile with better tags
      → Timeline: months-years
      → NHƯNG: daily practice compounds (small shifts → gradual recompile)

  VIRTUOUS SPIRAL:
    Calibrate well → better outcome (entity thrives + bond strong)
    → Confirms approach → curiosity about more nuances
    → Calibrate better → even better outcomes → ...
    → = Entity-access calibration becomes MASTERY domain
    → = Generative gap: "mỗi ngày hiểu thêm chút" → novelty reward
    → = Self-reinforcing loop (Lopes, Salovey & Straus 2003)

  VICIOUS SPIRAL:
    Calibrate poorly → bad outcome (entity suffers or drifts)
    → Self-blame (threat mode) → worse calibration
    → OR denial (blind mode) → no adjustment → ...
    → Break point: external intervention (therapy, trusted feedback, crisis)

  SOCIAL BASELINE EFFECT (Coan & Sbarra 2015):
    Brain OUTSOURCE emotion regulation to trusted others
    → Partner hand-holding → LESS threat neural activity
    → More trusted contacts → MORE PFC budget available → better calibration
    → = Social support ↑ → Trục 4 ↑ → calibration capacity ↑
    → Isolation → Trục 4 depleted → calibration capacity ↓

  🟢 Interoception training: Fukushima 2011 (R14), Gendlin 1978 (R15)
  🟢 Mentalization training: Fonagy 2002 (R5), Bateman & Fonagy 2006 (R6)
  🟢 Reflection practice: Trapnell & Campbell 1999 (R7)
  🟢 Emotion regulation ↔ social: Lopes, Salovey & Straus 2003 (R11)
  🟢 Social Baseline Theory: Coan & Sbarra 2015 (R9)
```

---

## §12 — CALIBRATION × ENTITY-ACCESS GRADIENT

```
⭐⭐⭐ CALIBRATION DIFFICULTY SCALES WITH ENTITY-ACCESS MỨC LEVEL (★ KEY):

  CORE INSIGHT:
    Calibration mechanism KHÁC per Mức level on Entity-Access Gradient
    Higher Mức = MORE entity-access depth = HARDER to calibrate
    Lower Mức = LESS depth = self-correcting OR irrelevant

  ┌──────────┬──────────────┬──────────────┬──────────────────────────────┐
  │ Mức      │ Calibration  │ Primary      │ Why                          │
  │          │ difficulty   │ mechanism    │                              │
  ├──────────┼──────────────┼──────────────┼──────────────────────────────┤
  │ 0a-0b    │ N/A          │ N/A          │ No entity-access → nothing   │
  │ (service)│              │              │ to calibrate                 │
  ├──────────┼──────────────┼──────────────┼──────────────────────────────┤
  │ 0c       │ TRIVIAL      │ Context      │ Tool-mode toward individual, │
  │ (tool)   │              │              │ no state modeling → no C     │
  ├──────────┼──────────────┼──────────────┼──────────────────────────────┤
  │ Mức 1-2  │ LOW          │ NATURAL      │ Shallow compile → easy to    │
  │ (unlabel)│              │ DRIFT        │ let go. No hardware bias. Entity-Compiled weak. │
  │          │              │              │ "Barista đổi quán" = natural │
  ├──────────┼──────────────┼──────────────┼──────────────────────────────┤
  │ Mức 3    │ LOW-MOD      │ EXTERNAL     │ Exit easy → friend's "no" =  │
  │ (bạn)    │              │ (exit cost)  │ strong signal → self-correct │
  │          │              │              │ Hardware=0 → no bias → C visible  │
  ├──────────┼──────────────┼──────────────┼──────────────────────────────┤
  │ Mức 4    │ HIGH         │ INTERNAL     │ Exit cost ↑ + hardware-subsidy →   │
  │ (Entity- │              │ (self-aware  │ C MASKED. PFC = "phần đời   │
  │ Owned)   │              │ + Trục 2)    │ tôi" → rationalize. Need    │
  │          │              │              │ 3-Layer actively.            │
  ├──────────┼──────────────┼──────────────┼──────────────────────────────┤
  │ Mức 5    │ MAXIMUM      │ EXTERNAL     │ By definition: calibration   │
  │ (Excess) │              │ INTERVENTION │ FAILING → that's WHY Mức 5.  │
  │          │              │ (therapy,    │ Internal mechanisms exhausted │
  │          │              │ crisis)      │ or overridden by compiled.   │
  └──────────┴──────────────┴──────────────┴──────────────────────────────┘

  ⭐ KEY OBSERVATIONS:

    Mức 1-3: SELF-CORRECTING
      → Exit cost low → environment provides calibration signals
      → Hardware-subsidy = zero or low → C/D visible → easy to detect
      → 3-Layer Architecture = useful but not CRITICAL
      → "Barista quá thân → đổi quán" = natural calibration at Mức 1
      → "Bạn kiểm soát nhau → bạn exit" = natural calibration at Mức 3

    Mức 4: CRITICAL ZONE
      → Exit cost rising → entity's "no" = weakening signal
      → Hardware-subsidy present → C masked as A → hard to detect
      → 3-Layer Architecture = ESSENTIAL
      → Self-Awareness (Trục 2) = DIFFERENCE MAKER
      → This is WHERE calibration matters most and is hardest
      → = WHY this file focuses on Mức 4 dynamics (parenting, romantic)

    Mức 5: CALIBRATION ALREADY FAILED
      → Person AT Mức 5 = calibration mechanisms have been overwhelmed
      → Internal observation insufficient → need EXTERNAL input
      → Therapy, crisis event, trusted friend's honest feedback
      → = Entity-Access-Excess.md §10: fix spectrum

  ⭐ PARENTING LIFECYCLE × CALIBRATION:
    Con 0-6 (Mức 4-5 entity-access, Mức 0 entity-access reversed):
      → Child = highest entity-access depth → hardest to calibrate
      → Child's own calibration = N/A (doesn't understand mechanism)
      → Parent ALONE must calibrate → Internal ONLY → Trục 2 critical

    Con 12-18 (Mức 4 ↓, child begins own calibration):
      → Teen rebellion = child's FIRST calibration attempts
      → "Ghét mẹ" = child testing: "can I say no?" = exit signal FORMING
      → Parent who RECEIVES this signal → recalibrate → healthy
      → Parent who OVERRIDES → signal weight stays low → excess persists

    Con 18+ (Mức 3-4, external calibration RETURNS):
      → Adult child CAN exit → signal weight ↑
      → "Con busy" = effective calibration signal
      → Parent→adult child: dynamics SHIFT toward friendship (Mức 3)
      → = Compilable-dominant destination (Entity-Access.md §3.5): C→B trajectory

  🟡 Calibration × Mức gradient = framework synthesis
  🟡 Mức 4 = critical calibration zone = framework synthesis
  🟡 Teen rebellion as calibration signal = framework synthesis
```

---

## §13 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 RESEARCH-GROUNDED (established):
═══════════════════════════════════════

  Baumrind parenting styles (1966, 1991) — ~60 years research
  Self-Determination Theory (Deci & Ryan 2000) — ~45 years
  Gottman bids for connection (2001) — ~25 years longitudinal
  Demand-withdraw pattern (Christensen & Heavey 1990) — replicated
  Reflection vs rumination (Trapnell & Campbell 1999) — established
  Mentalization (Fonagy 2002) — clinical evidence base
  Social Baseline Theory (Coan & Sbarra 2015) — neural evidence
  Parental burnout (Mikolajczak 2019) — replicated cross-culturally
  Interoception → empathy (Fukushima 2011) — established
  Parental investment theory (Trivers 1972) — foundational

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (novel combinations):
═══════════════════════════════════════

  3-Layer Calibration Architecture (maps to Simulation-Engine, novel application)
  Exit Cost = Signal Weight (novel framing of established dynamics)
  Hardware-Subsidy = Calibration Bias (novel angle on known hormone effects)
  Cannot prescribe applied to entity-access (parallel from Reward-Calibration)
  Calibration as Generative reward source (novel extension)
  5 failure modes taxonomy (novel organization of known phenomena)
  Calibration × Entity-Access Gradient per-Mức analysis
  Mức 4 = critical calibration zone
  Teen rebellion as calibration signal

═══════════════════════════════════════
🔴 HYPOTHESIS (testable but unverified):
═══════════════════════════════════════

  Exact mapping of 3 calibration layers to Simulation-Engine components
    (conceptually clean but neural correspondence not directly demonstrated)
  "Calibration as Generative reward" — mechanism plausible but no direct study
  "Parenting advice as threat trigger" — anecdotally common, no formal study
  Calibration difficulty × Mức level quantification (no empirical measure yet)

CÁI FRAMEWORK THÊM vs CÁI ĐÃ CÓ:
  Research đã biết: authoritative parenting best, mentalization trainable,
  burnout hurts parenting, bids maintain bonds.
  Framework THÊM: unifying MODEL explaining WHY (3-layer + exit cost + hardware bias
  + per-Mức analysis), connecting to broader architecture.
  = Organizing principle, not new discovery.
```

---

## §14 — CROSS-REFERENCES

| File | Sections | Relationship |
|------|----------|-------------|
| Entity-Access.md v1.1 | §1-§3, §5, §8-§9 | PREREQUISITE: entity-access definition + 3-Factor + gradient |
| Entity-Access-Excess.md v1.0 | §1-§10 | COMPANION: excess (Mức 5) — this file covers calibration |
| Entity-Compiled.md v1.0 | §1-§8 | FOUNDATION: brain compile agent vào body-base |
| Compiled-Fresh.md v2.0 | §6, §9, §10 | FOUNDATION: compiled quality + PFC budget + reversal |
| Simulation-Engine.md v1.0 | §1, §9, §11 | FOUNDATION: 3 components + reflection/rumination + training |
| PFC-Operations.md v1.0 | §1-§7 | FOUNDATION: Hold/Suppress, Compiled/Fresh, PFC universal |
| Self-Pattern-Modeling.md v3.1 | §0-§3 | FOUNDATION: Compiled/Fresh, Self-Pattern-Modeling as Simulation-Engine application |
| Reward-Calibration.md v1.1 | §1, §5 | PARALLEL: general reward calibration principle |
| Logic-Feeling-Balance.md v1.0 | §6-§7 | PARALLEL: cannot prescribe + infinite regress |
| Connection.md v4.0 | §9 | COMPANION: 2-body calibration dynamic equilibrium |
| Social-Calibration.md v1.1 | §2.5 | COMPANION: social system calibration (CHECK function) |
| Empathy.md v2.2 | §5 | DOWNSTREAM: burnout as calibration failure |
| Autonomy-Hardware.md v1.1 | §2 | FOUNDATION: vmPFC + DRN → autonomy violation detection |
| Self-Created-Threat.md v1.0 | §3 | DOWNSTREAM: threat-mode calibration failure |
| AI-Self-Model.md v2.0 | §4, §5 | DOWNSTREAM: Dual Check as calibration mechanism |
| Ask-AI.md v3.1 | §6 | DOWNSTREAM: body as quality controller = Layer 1 calibration |
| Education-Mechanism.md v1.0 | §3 | DOWNSTREAM: bridge reward calibration |
| Gap-Distribution-Profile.md v1.0 | §8 | COMPANION: portfolio risk, diversification |

---

## §15 — RESEARCH CITATIONS

| # | Citation | Used in | Evidence |
|---|----------|---------|----------|
| R1 | Baumrind 1966, 1991 — Parenting styles: Authoritative/Authoritarian/Permissive/Neglectful. Authoritative = best outcomes. | §7 | 🟢 |
| R2 | Deci & Ryan 2000 — Self-Determination Theory. Autonomy support + structure = optimal. | §3, §7 | 🟢 |
| R3 | Gottman & DeClaire 2001 — Bids for connection. Turning toward vs turning away. Bid-response ratio predicts outcomes. | §7, §8 | 🟢 |
| R4 | Christensen & Heavey 1990 — Demand-Withdraw interaction pattern. Escalation cycle. | §8 | 🟢 |
| R5 | Fonagy 2002 — Mentalization: capacity to understand behavior in terms of mental states. Trainable. | §6, §8, §11 | 🟢 |
| R6 | Bateman & Fonagy 2006 — Mentalization-Based Therapy (MBT). Clinical evidence for training. | §5, §11 | 🟢 |
| R7 | Trapnell & Campbell 1999 — Self-Reflection vs Self-Rumination. 2 dispositions, opposite correlates. | §6, §11 | 🟢 |
| R8 | Joireman, Parrott & Hammersla 2002 — Self-reflection → positive empathy correlation. | §6, §11 | 🟢 |
| R9 | Coan & Sbarra 2015 — Social Baseline Theory. Brain outsources emotion regulation. Neural evidence. | §11 | 🟢 |
| R10 | Mikolajczak et al. 2019 — Parental burnout: depleted → overcontrol OR emotional distance. Cross-cultural. | §5, §9 | 🟢 |
| R11 | Lopes, Salovey & Straus 2003 — Emotion regulation ↔ social interactions. Bidirectional. | §11 | 🟢 |
| R12 | Koudenburg et al. 2024 — Social interaction → self-concept clarity. "Sense of me" through "sense of we." | §11 | 🟢 |
| R13 | McNulty et al. 2013 — Implicit vs explicit partner attitudes. PFC rationalization. Science. | §1 | 🟢 |
| R14 | Fukushima et al. 2011 — Interoceptive accuracy → empathic accuracy correlation. Trainable. | §2, §9, §11 | 🟢 |
| R15 | Gendlin 1978 — Focusing. Body-felt sense awareness technique. | §9, §11 | 🟢 |
| R16 | Trivers 1972 — Parental investment theory. Highest investment → highest bias. | §4 | 🟢 |
| R17 | Feldman 2012 — Bio-behavioral synchrony. Oxytocin × parent-child. | §4 | 🟢 |
| R18 | Strathearn et al. 2009 — Maternal brain reward: own infant face. | §4 | 🟢 |
| R19 | Fraley & Shaver 1998 — Avoidant suppress but physiology elevated. Attachment change possible but slow. | §5 | 🟢 |
| R20 | Zeki & Romaya 2008 — Hate vs Love circuits. Shared: putamen+insula. Hate retains judgment. | §8 | 🟢 |
| R21 | Maccoby 1992 — Power asymmetry in parent-child relationships. | §3 | 🟢 |
| R22 | Hall 2018 — Friendship formation: 40-60h casual → 200+h close. | §8 | 🟢 |
| R23 | Segrin et al. 2013 — Parental anxiety → overparenting, not child need. | §9 | 🟢 |
| R24 | Soenens et al. 2015 — Self-worth contingency → psychological control. | §9 | 🟢 |
| R25 | Mitchell 2006 — Diverse interaction → sharper mental models. | §11 | 🟢 |
