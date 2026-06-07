---
title: Entity-Valence-Dynamics — Cách Valence Behaves Per-Entity Over Time
version: 1.3
created: 2026-05-29
refined: |
  2026-05-29 (v1.1 — L3 RETIRE: dep Body-Base v2.1→v3.3, L0-L1-L3→L0+L1 substrate)
  2026-06-04 (v1.2 — §2.4 MECHANISM NOTE: "state = my state" = description,
    gap-fillability = mechanism. Level 1/2 distinction. Cross-ref Drill-Body-Base-Boundary-Spectrum v1.2)
  2026-06-05 (v1.3 — §2.4 ENRICH: Embodied-Mirror→Gap-Predict 2-step meta-process, 3 firing patterns,
    3 pain types, Novelty vs Gap-Fillability distinction. Source: Drill-Agent-Feed-Channel v2.2)
status: v1.3 — REFERENCE FILE (entity-valence dynamics)
scope: |
  HOW valence BEHAVES per-entity over time:
  Structural vs Current valence, Entity-Compiled extension,
  2-luồng/2-tầng × visibility, 3 Firing Modes, Hardware-Subsidy × VTA habituation,
  Satiation type × valence dynamics, Mixed valence, "Xa mẹ mới biết thương",
  Nostalgia, Per-entity trajectory + Reward-Signal-Architecture, Extreme valence (Love/Hate),
  Phantom resonance, Technology × valence frontier.
  v1.0 EXTRACTED from Valence-Propagation.md v3.0 §3-§13 + 3 Drill GAPs absorbed.
  Companion file: Valence-Propagation.md v4.1 = WHAT valence IS + HOW it PROPAGATES.
  This file = HOW valence BEHAVES per-entity.
purpose: |
  Central reference for per-entity valence dynamics within the framework.
  Builds on Valence-Propagation.md v4.1 §1-§2 (valence definition + profile).
  Per-entity dynamics: structural/current distinction, visibility mechanism,
  firing modes, habituation, satiation interaction, mixed valence,
  "new appreciation," nostalgia, per-entity mapping, extreme valence,
  phantom resonance, technology era impact.
dependencies:
  - Valence-Propagation.md v4.1 — companion file: WHAT valence is (§1-§2) + HOW propagates (§3-§7)
  - Body-Base.md v4.0 — L0+L1 substrate + observation parameters mà valence đánh giá
  - Body-Feedback-Mechanism.md v2.1 — Body-Need aggregate, chunk dynamics
  - Entity-Compiled.md v1.2 — deep mechanism (Hub-and-Spoke, Dunbar, grief, decay)
  - Entity-Access.md v1.3 — gradient Mức 0-5, 3-Factor Model
  - PFC-Operations.md v1.2 — Hold/Suppress, Compiled/Fresh spectrum, PFC budget
  - Simulation-Engine.md v1.2 — 1 engine, 3 components, 3 axes
  - Inter-Body-Mechanism.md v1.0 — Entity-Compiled §8, 3-cost §4, By-Product Match §5
  - Body-Coupling.md v3.1 — coupling mechanism deep-dive
  - Connection.md v5.0 — 3 Generative Primitives, §3.3 2-luồng overview
  - Self-Pattern-Modeling.md v3.2 — Compiled/Fresh, Simulation-Engine application 1
  - Agent-Mechanism.md v2.0 — integration hub, Compilable Architecture
  - Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State × valence
  - Dissonance-Signal-Architecture.md v1.0 — Hardware-Subsidy bidirectional (§6.2)
  - Gap-Body-Need.md v2.0 — Cyclic/Tonic/Generative satiation types
  - Resonance-Per-Entity.md v1.1 — hardware-subsidy per entity, Reward-Signal-Architecture Evaluative:Direct-State
  - Resonance-Sustainability.md v1.0 — 3 modalities, silence, maintenance decline
  - Boredom.md v2.0 — dissonance + Imagine-Final mờ, source ⑥, Resonance Decline
  - Body-Feedback-Label.md v2.0 — vocabulary reference
sources:
  - Drill-Entity-Valence-Dynamics v2.0 (1,436L, 28 insights, 33 citations) — PRIMARY
  - Valence-Propagation.md v3.0 §3-§13 — extracted content
  - 3 Drill GAPs absorbed: §6 (8-channel visibility), §12 (verbalization × Reward-Signal-Architecture), §14 ("chán" decomposition)
  - Drill-Agent-Feed-Channel v2.2 — §5 Embodied-Mirror→Gap-Predict 2-step meta-process, 3 firing patterns, 3 pain types
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Entity-Valence-Dynamics — Cách Valence Behaves Per-Entity Over Time

> **Ở với mẹ 20 năm. PFC bạn nói: "bình thường, không gì đặc biệt."**
> **Valence-Structural compiled: ôm, nấu ăn, dạy bài, hy sinh — 20 năm TÍCH LŨY.**
> **VTA habituated. Hardware-subsidy counter. Tonic baseline INVISIBLE.**
> **PFC KHÔNG BIẾT baseline này tồn tại — cho đến khi MẤT.**
>
> **Xa mẹ. Đọc thơ. Bỗng KHÓC.**
> **3 cơ chế cộng dồn: decay asymmetry + contrast + articulation.**
> **20 năm body BIẾT. PFC mới observe LẦN ĐẦU.**
>
> File này: HOW valence BEHAVES per-entity over time.
> Structural vs Current, 2-luồng/2-tầng visibility, 3 Firing Modes,
> Hardware-Subsidy × habituation, Satiation Type × dynamics,
> Mixed valence, "xa mẹ mới biết thương," nostalgia,
> per-entity trajectory, extreme valence, phantom resonance,
> technology × valence frontier.
>
> **Companion:** Valence-Propagation.md v4.1 = WHAT valence IS + HOW it PROPAGATES.
> **File này** = HOW valence BEHAVES per-entity.
> **Đọc trước:** Valence-Propagation.md v4.1 §1-§2 (valence definition + profile).

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — STRUCTURAL VALENCE vs CURRENT VALENCE
- §2 — ENTITY-COMPILED: Body-Base Extension
- §3 — 2-LUỒNG + 2-TẦNG × VALENCE VISIBILITY
- §4 — 3 FIRING MODES
- §5 — VTA HABITUATION × HARDWARE-SUBSIDY
- §6 — VALENCE × SATIATION TYPE
- §7 — MIXED VALENCE: PARALLEL PER-CHANNEL
- §8 — "XA MẸ MỚI BIẾT THƯƠNG" — 3 CƠ CHẾ CỘNG DỒN
- §9 — NOSTALGIA = Valence-Structural ACTIVE SELF-REGULATION
- §10 — PER-ENTITY VALENCE DYNAMICS + Reward-Signal-Architecture Evaluative:Direct-State
- §11 — EXTREME VALENCE: LOVE/HATE + DISORGANIZED
- §12 — PHANTOM RESONANCE × GRIEF
- §13 — TECHNOLOGY × VALENCE FRONTIER
- §14 — HONEST ASSESSMENT
- §15 — CROSS-REFERENCES + CITATIONS

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
⭐⭐ ENTITY-VALENCE-DYNAMICS v1.0 — CORE THESIS:

  ① Entity-Compiled = storage. Valence = emergent from stored tags.
  ② 2 loại valence: Structural (inside Entity-Compiled, slow) vs Current (outside, fast)
  ③ Valence-Momentary (Self-Pattern-Modeling-owned) vs Valence-Structural (Entity-Compiled) = 2 streams ĐỘC LẬP
  ④ 2-tầng: Hardware-driven (A) vs Self-Pattern-Modeling-driven (B) → KHÁC visibility
  ⑤ 2-luồng: Valence-Momentary vs Valence-Structural → per-entity proportion determines trajectory
  ⑥ Valence-Structural INVISIBLE khi stable (VTA habituation → baseline → PFC sees nothing)
  ⑦ Hardware-Subsidy = ANTI-HABITUATION: modulate VTA habituation RATE per entity
  ⑧ Valence dynamics KHÁC per satiation type (Cyclic/Tonic/Generative)
  ⑨ 3 Firing Modes: Maintenance / Chunk-Miss / Context-Trigger
  ⑩ Reward-Signal-Architecture Evaluative:Direct-State ratio determines valence "feel"
  ⑪ Mixed valence = parallel per-channel (Cacioppo Evaluative Space Model 1994)
  ⑫ "Xa mẹ mới biết thương" = decay asymmetry + contrast + articulation
  ⑬ Nostalgia = Valence-Structural as ACTIVE self-regulation tool (Sedikides 2018)
  ⑭ Phantom resonance = f(compilation depth × hardware-subsidy × Valence-Structural × duration)
  ⑮ Per-entity valence trajectory = f(satiation × subsidy × 2-tầng × 2-luồng)

  v1.0 GAPs absorbed from Drill-Entity-Valence-Dynamics v2.0:
    + §4.1: 8-channel Valence-Structural visibility taxonomy (A-H)
    + §6.1: "Chán" × satiation type decomposition
    + §10.2: Verbalization = PFC observation × Reward-Signal-Architecture mapping


  FILE NÀY TRONG FLOW:

    Valence-Propagation.md v4.1 §1-§2 (WHAT valence IS: definition + profile)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ ENTITY-VALENCE-DYNAMICS.MD v1.0 (FILE NÀY)                  │
    │                                                              │
    │  HOW valence BEHAVES per-entity over time:                   │
    │    §1-§2: Structural/Current + Entity-Compiled extension     │
    │    §3-§5: Visibility + Firing Modes + Hardware-Subsidy       │
    │    §6-§7: Satiation type + Mixed valence                     │
    │    §8-§9: "Xa mẹ mới biết thương" + Nostalgia               │
    │    §10: Per-entity trajectory + Reward-Signal-Architecture    │
    │    §11-§12: Extreme valence + Phantom resonance              │
    │    §13: Technology frontier                                  │
    └─────────────────────────────────────────────────────────────┘
         │
         ▼
    Valence-Propagation.md v4.1 §3-§7 (HOW valence PROPAGATES: chain + cases)
    Drive.md (TỔNG HỢP valences → action)
    Feeling.md v2.0 (PFC OBSERVE valence → feeling)


  ĐỌC FILE NÀY SAU: Valence-Propagation.md v4.1 §1-§2.
  File này BUILDS ON definition + profile foundation từ Valence-Propagation.
```

---

## §1 — STRUCTURAL VALENCE vs CURRENT VALENCE

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §1.

```
⭐⭐ 2 LOẠI VALENCE — KHÁC VỊ TRÍ, KHÁC TỐC ĐỘ, KHÁC SATIATION TYPE:

  STRUCTURAL VALENCE (INSIDE Entity-Compiled):
    = Aggregate of per-channel valence tags CỦA tất cả compiled chunks
    = Mỗi chunk có tag: approach / avoidance / neutral (compile-time lock)
    = Structural valence = SUM of all tags = valence PROFILE
    = CHẬM thay đổi (cần compile/decompile chunks = months/years)
    = 3 subtypes (§2.1): positive-dominant / negative-dominant / MIXED
    
    STRUCTURAL VALENCE CÓ SATIATION PROFILE:
      Mỗi channel CÓ satiation type riêng (Gap-Body-Need v2.0 §2):
      → Cyclic channels: approach/avoidance tags OSCILLATE (hunger → fill → off → return)
      → Tonic channels: approach tags STABLE baseline (comfort, safety → slow build, slow fade)
      → Generative channels: approach tags RENEWABLE (curiosity → fill → new gap → repeat)
      → Structural valence = aggregate across ALL satiation types
      → Most deep entities = Tonic + Generative compound (§6)
    
    VD — Mẹ (structural valence profile):
      Channel [nấu ăn]: approach (+) — Cyclic (fill → return → fill)
      Channel [ôm]: approach (++) — Tonic (ongoing baseline)
      Channel [la mắng]: avoidance (--) — Cyclic (episode → fade)
      Channel [hy sinh]: complex (+/schema) — Tonic (persistent)
      Channel [dạy kỹ năng]: approach (+) — Generative (each lesson → new gap)
      = Structural valence = POSITIVE-DOMINANT, Tonic-base + Generative-bursts
      
  CURRENT VALENCE (OUTSIDE Entity-Compiled, per-moment):
    = Valence-Momentary (Self-Pattern-Modeling) + activated Valence-Structural channels AT THIS MOMENT
    = Thay đổi PER SECOND (context-dependent)
    = What PFC observes → what person VERBALIZES
    
    CURRENT VALENCE "FEEL" = f(Reward-Signal-Architecture Evaluative:Direct-State ratio) (Reward-Signal-Architecture v2.1 §1):
      Direct-State dominant → "ấm áp, comfortable" (opioid, CT afferents)
      Evaluative dominant → "hào hứng, thú vị" (evaluative, dopamine-adjacent)
      → Mẹ ôm con: current = Direct-State dominant → "ấm"
      → Bạn kể chuyện hay: current = Evaluative dominant → "thú vị"
      → CÙNG positive valence, KHÁC "feel" vì KHÁC Evaluative:Direct-State ratio
    
    VD — Mẹ đang la:
      Valence-Momentary = NEGATIVE (Self-Pattern-Modeling simulate mẹ angry → body distress)
      Valence-Structural [la mắng] channel = ACTIVE (avoidance, Cyclic)
      Valence-Structural [ôm, nấu ăn] channels = DORMANT (not triggered)
      Current valence = NEGATIVE
      PFC label: "ghét mẹ" (lúc này)
      
    VD — Đọc thơ về mẹ (xa mẹ):
      Valence-Momentary = POSITIVE (poem → Self-Pattern-Modeling fire → body warm)
      Valence-Structural [hy sinh, ôm, nấu ăn] channels = ACTIVE (triggered by poem)
      Valence-Structural [la mắng] channels = DORMANT (not in poem context)
      Current valence = INTENSE POSITIVE (Direct-State dominant → "thương")
      
  ⭐ STRUCTURAL ≠ CURRENT:
    Structural = what's STORED (slow, aggregate across satiation types)
    Current = what's ACTIVATED (fast, context-dependent, Reward-Signal-Architecture Evaluative:Direct-State ratio determines "feel")
    Cùng entity, cùng structural valence → KHÁC current valence tùy moment
    → "Ghét mẹ" (lúc bị la) vs "Thương mẹ" (lúc đọc thơ)
    → CÙNG structural (mixed) → KHÁC current (context activates different channels)
    
  🟡 Structural vs Current distinction + satiation type dimension = framework synthesis
  🟢 Per-channel valence: Valence-Propagation.md v4.1 §2 (explicit "KHÔNG average")
  🟢 Reward-Signal-Architecture Evaluative:Direct-State: Reward-Signal-Architecture v2.1 §1
```

---

## §2 — ENTITY-COMPILED: Body-Base Extension

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 + Entity-Compiled.md v1.2.
> **Slim down**: Entity-Compiled.md v1.2 + Entity-Access.md v1.3 đã tồn tại.
> §2 giữ CORE CONCEPTS + POINTER → 2 files cho deep mechanism + gradient.

```
⭐ KHI PER-AGENT VALENCE COMPILE ĐỦ SÂU → BƯỚC NHẢY CHẤT:

  AGENT VALENCE CÓ DIMENSION MÀ OBJECT KHÔNG BAO GIỜ CÓ:

    Khi per-agent valence STRONG + compiled SÂU qua nhiều interaction:
      → Body KHÔNG CHỈ đánh giá "agent X ảnh hưởng tôi thế nào?"
      → Body chuyển sang: "agent X's state = MY state"
      → = Agent TRỞ THÀNH phần mở rộng body-base CỦA TÔI
      → = STRUCTURAL, SUSTAINED — không phụ thuộc từng episode tương tác

    TẠI SAO CHỈ AGENT, KHÔNG BAO GIỜ OBJECT:
      Object KHÔNG fire Self-Pattern-Modeling → không có Valence-Momentary episodes tích lũy
      Object KHÔNG bidirectional → không có mutual reinforcement
      Object DỄ thay thế → trust/dependency không compile sâu đủ
      → Body-base extension = EMERGENT property CHỈ CÓ ở agent valence
      → Mất nhà = stress tài chính. Mất con = body-base amputation.
        2 loại loss KHÁC CĂN BẢN.

    🟢 Grief as body-level pain: Eisenberger 2003 (social pain = physical pain pathways)
    🟢 Attachment bond = body-level: Bowlby 1969
```

### §2.1 — 3 Subtypes (spectrum)

```
⭐ 3 SUBTYPES — SPECTRUM, KHÔNG BINARY (Inter-Body-Mechanism.md §8.2):

  ① POSITIVE-DOMINANT (≈ old "Entity-Owned"):
     Majority channels positive. Presence = approach + reward. Loss = grief.
     Example: bạn thân lâu năm, con cái, mẹ healthy relationship.

  ② NEGATIVE-DOMINANT:
     Majority channels negative. Presence = threat/dissonance. Loss = relief.
     NHƯNG sub-case "obsession": loss = emptiness (mất mục tiêu).
     Example: bully, abuser, đối thủ obsessive.

  ③ MIXED (AMBIVALENT) — PHỔ BIẾN NHẤT:
     Significant BOTH positive AND negative channels CÙNG LÚC.
     Behavior oscillates by STATE/TRIGGER/CONTEXT.
     Loss = COMPLEX grief (relief + pain simultaneously).
     Example: bố mẹ strict, vợ chồng conflict, frenemy.

  TẠI SAO ③ PHỔ BIẾN NHẤT?
    → Relationship dài → nhiều interaction types → nhiều channels compile
    → CÀNG GẦN nhau LÂU → càng nhiều channels (cả + và -)
    → "Thuần positive" = rare luxury of LIMITED interactions
    → Paradox: GẦN NHAU LÂU = deeper bond + deeper conflict potential

  🟡 3 subtypes = framework synthesis.
  🟢 Ambivalence = well-documented (Cacioppo & Berntson 1994).
```

### §2.2 — Entity-Compiled vs Obligation = INDEPENDENT

```
⭐ 2 CƠ CHẾ KHÁC NHAU (Inter-Body-Mechanism.md §8.3):

  Entity-Compiled: "entity's state = MY state" (structural, automatic)
  Obligation:      "predict cost to MAINTAIN access" (prediction, PFC-mediated)

  CÓ THỂ ĐỘC LẬP:
    Valence-Structural HIGH + Obligation LOW:  bạn thân → vui tự động, không "nợ" gì
    Valence-Structural LOW + Obligation HIGH:  ân nhân xa lạ → không thân nhưng "phải trả"
    Valence-Structural HIGH + Obligation HIGH: bố mẹ → yêu thương + cảm thấy phải chăm sóc
    Valence-Structural LOW + Obligation LOW:   stranger → no drive either way

  Cross-ref: Obligation.md v1.0 §2-§4 chi tiết.
  🟡 Valence-Structural vs Obligation independence = framework synthesis.
```

### §2.3 — Deep Mechanism + Gradient → POINTER

```
⭐ FILE NÀY CHỈ ĐỊNH NGHĨA + KEY CONCEPTS.
  DEEP MECHANISM VÀ GRADIENT → 2 FILES RIÊNG:

  Entity-Compiled.md v1.2 (Agent-Mechanism/):
    = DEEP MECHANISM: neural reality, formation, capacity, dynamics, loss, decay
    → §1: 8 research streams hội tụ → Entity-Compiled = neural reality
    → §2: Hub-and-Spoke architecture + body simulation
    → §3: Formation timeline (40→200h) + acceleration + sleep
    → §4: Dunbar capacity ceiling + 3 resource limits
    → §5: "Hợp tính" (By-Product-Gap-Resonance Baseline) + meta-match
    → §7: Grief intensity model (A+B+C types)
    → §8: Love↔Hate shift (|valence| depth, direction switch)
    → §9: Decay 3-layer model (episodes fastest, schema slowest)

  Entity-Access.md v1.3 (Agent-Mechanism/):
    = GRADIENT MODEL: how access level changes, quality, excess, calibration
    → §1: 3-Factor Model (Engine Mode × Gap-Need × Access Confidence)
    → §2: Entity-Access Gradient Mức 0-5 (Tool → Excess)
    → §3: 4 Starting Modes × Compilable-dominant destination
    → §6: Excess spectrum (Mức 5) — limerence, obsession
    → §8: Calibration architecture

  ⭐ ENTITY-OWNED = PFC LABEL (Entity-Access.md §2):
    Entity-Owned = PFC OBSERVATION at Mức 4-5, NOT mechanism.
    Mechanism = entity-access compilation (3-factor → baseline).
    Most entity-access = UNLABELED by PFC (fuzzy middle of gradient).
    = Binary "owned/not-owned" → REPLACED by gradient Mức 0-5.

  Framework readers: §2 NÀY (definition) → Entity-Compiled.md (mechanism)
                     → Entity-Access.md (gradient + dynamics).
```

### §2.4 — MECHANISM NOTE: Description vs Mechanism (from Drill-Body-Base-Boundary-Spectrum v1.2)

```
⭐⭐ "AGENT'S STATE = MY STATE" = DESCRIPTION, KHÔNG PHẢI MECHANISM:

  §2 nói: "Body chuyển sang: agent X's state = MY state"
  → ĐÚNG như DESCRIPTION (what it looks like from PFC observation).
  → NHƯNG: mechanism gốc hơn nằm ở GAP-FILLABILITY.

  MECHANISM (Entity-Compiled §7 + Gap-Body-Need §11-12):
    ① Entity compiled deep → fills NHIỀU gaps uniquely → part of BASELINE
    ② Entity's state change → Self-Pattern-Modeling predict gap-fillability change → body respond
       (mẹ buồn → mẹ fill gaps kém → gap-fillability GIẢM → body respond)
    ③ Entity mất → baseline VIOLATED → Chunk-Miss ACROSS compiled channels → pain
    ④ Entity-Compiled §7: Grief = A(gap-feed loss) + B(rebuild cost) + C(phantom firing)
       → Component A = gap-fillability. Component C = baseline Chunk-Miss.

  "ENTITY'S STATE = MY STATE" = COMPRESSED PREDICTION:
    → Entity fills nhiều gaps uniquely qua nhiều năm
    → Brain compile SHORTCUT: "entity state ≈ proxy cho gap-fillability CỦA TÔI"
    → Entity OK → gaps fillable → I'm OK
    → Entity NOT OK → gaps threatened → I'm NOT OK
    → = Compressed prediction, EMERGES từ compilation depth + gap dependency

  PROOF — "XA MẸ MỚI BIẾT THƯƠNG" (§8):
    → Mẹ's state KHÔNG ĐỔI (mẹ vẫn ổn ở nhà)
    → NHƯNG MÌNH ĐAU (nhớ mẹ, trống, thiếu)
    → Nếu mechanism = "state sharing": mẹ ổn → mình nên ổn → SAI
    → Nếu mechanism = baseline violated: gaps unfilled → pain → ĐÚNG ✓
    → = §8 "xa mẹ" CHÍNH LÀ proof cho gap-fillability mechanism

  NOTE VỀ "CHỈ AGENT, KHÔNG BAO GIỜ OBJECT":
    → ĐÚNG cho LEVEL 2 (entity body-base extension: "agent's state = my state")
    → NHƯNG: Object CAN extend LEVEL 1 (body-schema extension)
      → Tool: Iriki 1996 — bimodal neurons extend receptive field
      → Prosthetic: Murray 2004 — body-schema integration qua years of use
      → Rubber hand: Botvinick 1998 — body-schema update trong 120s
    → LOSS MECHANISM CÙNG cho cả 2 levels:
      Level 1 loss: body-schema baseline violated × unfillability
      Level 2 loss: body-base baseline violated × unfillability (deeper, wider, permanent)
      = CÙNG formula, KHÁC parameters (depth, breadth, duration, replaceability)

  NOTE VỀ "OBJECT DỄ THAY THẾ":
    → TENDENCY đúng (đũa, bàn ghế = dễ thay thế → pain ≈ 0)
    → NHƯNG: context-dependent:
      PC mất (có tiền) = dễ thay thế → annoyance
      PC mất (không tiền + data duy nhất) = KHÔNG thay thế → real distress
      Tay giả dùng 20 năm mất = KHÔNG dễ thay thế → body-schema violation
    → Replaceability = VARIABLE, không phải property CỐ ĐỊNH của "object" vs "agent"
    → Agent THƯỜNG harder to replace (unique Self-Pattern-Modeling data, unique personality)
    → Nhưng mechanism = CÙNG: Δ(predicted gap-fillability)

  Cross-ref: Drill-Body-Base-Boundary-Spectrum v1.2 §12 (Loss Mechanism),
             §14 (Gap Analysis), Gap-Body-Need §11-12, Entity-Compiled §7.

  🟡 Mechanism reframe (description vs mechanism) = drill synthesis
  🟡 Level 1 vs Level 2 distinction = drill synthesis
  🟢 "Xa mẹ" as proof: Entity-Valence-Dynamics §8 (3 cơ chế cộng dồn)
  🟢 Object body-schema extension: Iriki 1996, Botvinick 1998, Murray 2004
```

### §2.4.1 — Embodied-Mirror→Gap-Predict: 2-STEP META-PROCESS

> Nguồn: Drill-Agent-Feed-Channel v2.2 §5 + Entity-Compiled.md v1.2 §2.3.

```
⭐⭐ §2.4 MÔ TẢ MECHANISM: gap-fillability prediction (Gap-Predict).
  NHƯNG: Gap-Predict KHÔNG hoạt động đơn độc.
  Entity-Compiled §2.3 MÔ TẢ Embodied-Mirror: body simulation.
  CÁI MỚI: Embodied-Mirror → Gap-Predict = UNIFIED 2-STEP META-PROCESS.

  STEP 1 — Embodied-Mirror: EMBODIED SIMULATION (PRESENT mirroring):
    Entity-Compiled fire → body simulate entity's CURRENT state
    bằng OWN pain/joy circuits
    = Entity-Compiled §2.3: "body mình = simulator cho close person"
    = Singer 2004: ACC + anterior insula fire khi nhìn partner đau
    Scale: Entity-Compiled depth (self > close > stranger)

    Properties:
      PRESENT-oriented: mirror entity state AS IT IS NOW
      Automatic: fire khi Entity-Compiled activated (không cần PFC)
      Graded: intensity = f(Entity-Compiled depth)
      Uses OWN circuits: pain circuits CỦA TÔI simulate pain CỦA ENTITY

  STEP 2 — Gap-Predict: GAP-FILLABILITY PREDICTION (ANTICIPATORY signal):
    Entity state (từ Embodied-Mirror output HOẶC từ information trực tiếp) →
    Self-Pattern-Modeling predict: entity fill gaps tương lai THẾ NÀO? →
    Body generate signal:
      Entity ổn → gaps fillable → relief, yên tâm
      Entity threatened → gaps threatened → anxiety, lo
    = §2.4 trên: "entity's state = my state" = compressed prediction
    Scale: Entity-Compiled depth × gap dependency breadth

  ⭐ Embodied-Mirror VÀ Gap-Predict = 2 TẦNG KHÁC NHAU:
    Embodied-Mirror = MIRROR (body simulate entity state → feel entity's pain/joy)
    Gap-Predict = PREDICT (entity state → predict impact on MY gaps → feel MY concern)

    Embodied-Mirror fire → Gap-Predict CÓ THỂ nhận output:
      Embodied-Mirror simulate "entity đau" → Gap-Predict predict "entity less available" → MY anxiety
    NHƯNG: Gap-Predict CŨNG fire ĐỘC LẬP khi có information KHÔNG qua Embodied-Mirror

  KHÁC BIỆT VỚI LAYER 0 ENTRAINMENT (Gap-Body-Need v2.0 §11.3):
    Entrainment = PHYSICS-LEVEL oscillator sync (vô thức, bidirectional)
    Embodied-Mirror = COGNITIVE simulation (Entity-Compiled fire → body mirror)
    Embodied-Mirror CẦN Entity-Compiled. Entrainment KHÔNG cần.
    Embodied-Mirror MORE one-directional. Entrainment BIDIRECTIONAL.
    3 cơ chế ĐỘC LẬP: Entrainment (Layer 0) / Embodied-Mirror (simulation) / Gap-Predict (prediction)

  NOVELTY vs GAP-FILLABILITY: 2 MECHANISMS KHÁC CHIỀU THỜI GIAN:
    Novelty/Prediction-delta (Gap-Body-Need v2.0 §4.2) = TỨC THỜI:
      VTA fire khi actual ≠ predicted → reward/pain
      Time-reference: NOW (entity behavior AT THIS MOMENT vs prediction)
      VD: bạn nói điều bất ngờ → delta → dopamine → "interesting!"

    Gap-Fillability Prediction (Gap-Predict) = TƯƠNG LAI:
      Self-Pattern-Modeling predict entity's FUTURE impact on my gaps
      Time-reference: FUTURE (entity state → predict gap-fill trajectory)
      VD: bạn nói "sắp chuyển xa" → predict future loss → anxiety

    CẢ HAI = Processing MECHANISMS (Gap-Body-Need v2.0 §4.2):
      Chạy ACROSS tất cả hardware sources (unbounded, cross-source)
      KHÁC hardware SOURCES (bounded, fire cho 1 loại input)
    NHƯNG: KHÁC chiều thời gian (tức thời vs tương lai)

  🟢 Embodied-Mirror body simulation: Entity-Compiled §2.3. Singer 2004: ACC + insula.
  🟢 Gap-Predict gap-fillability: §2.4 trên. Eisenberger 2003: social pain.
  🟡 Embodied-Mirror → Gap-Predict = unified 2-step meta-process = drill synthesis (Drill-Agent-Feed-Channel v2.2 §5)
  🟡 Novelty tức thời vs Gap-Fillability tương lai = drill synthesis
```

### §2.4.2 — 3 FIRING PATTERNS

> Nguồn: Drill-Agent-Feed-Channel v2.2 §5.

```
⭐⭐ Embodied-Mirror VÀ Gap-Predict CÓ 3 FIRING PATTERNS (ĐỘC LẬP HOẶC NỐI TIẾP):

  ① Embodied-Mirror ALONE (simulation only, no gap-fillability concern):
    Entity-Compiled fire → body simulate entity state → feel entity's pain/joy
    NHƯNG: KHÔNG fire Gap-Predict (no gap prediction)

    KHI NÀO:
      → Entity = FICTIONAL (xem phim khóc khi nhân vật chết)
      → Entity = STRANGER observed (thấy stranger bị đau → wince)
      → Entity = CLOSE nhưng gap-fillability KHÔNG threatened
        (mẹ kể chuyện buồn CŨ → Embodied-Mirror → Gap-Predict = 0 vì mẹ đang ổn)

    Observable: "đau cùng" nhưng KHÔNG lo. Feel entity's pain WITHOUT anxiety about MY gaps.
    Seeking: muốn giúp entity (comfort-giving, NOT self-protective)

  ② Gap-Predict ALONE (prediction only, no simulation):
    Information → Self-Pattern-Modeling predict gap-fillability change → body signal
    KHÔNG qua Embodied-Mirror (entity state CHƯA được simulate)

    KHI NÀO:
      → Entity ĐANG ỔN nhưng information predict CHANGE:
        Bạn nói "tao sắp chuyển xa" → bạn ĐỦ khỏe → Embodied-Mirror = 0
        NHƯNG: predict bạn ABSENT tương lai → Gap-Predict fire → anxiety
      → Entity status CẬP NHẬT qua third-party info:
        Nghe tin mẹ bệnh (qua ai kể) → chưa thấy mẹ đau → Embodied-Mirror = 0
        NHƯNG: predict mẹ less available → Gap-Predict fire → lo

    Observable: "lo, bất an" nhưng CHƯA "đau cùng". Feel MY concern WITHOUT mirroring.
    Seeking: muốn CHECK, gọi điện, verify information (information-seeking, NOT comfort-giving)

  ③ Embodied-Mirror → Gap-Predict (nối tiếp — COMPOUND):
    Step 1: Entity-Compiled fire → Embodied-Mirror simulate entity state → feel entity's pain
    Step 2: Embodied-Mirror output → Gap-Predict predict gap-fillability impact → feel MY anxiety
    = COMPOUND: "đau cùng" + "lo cho mình" CÙNG LÚC

    KHI NÀO:
      → Entity PRESENT + entity IN PAIN + entity = gap-filler:
        Thấy chồng đau → Embodied-Mirror (xót, đau cùng) → Gap-Predict predict (chồng less available → lo)
        Thấy mẹ khóc → Embodied-Mirror (buồn cùng) → Gap-Predict predict (mẹ threatened → my safety threatened)

    Observable: "vừa xót vừa lo". Hai feelings compound.
    Seeking: COMPOUND — muốn giúp entity (Embodied-Mirror) + muốn secure gap (Gap-Predict)
    = "Vừa muốn an ủi mẹ VỪA lo không ai chăm mình" = ③ compound

  ⭐ 3 PATTERNS = OBSERVABLE KHÁC NHAU:
    ① = feel OTHER's pain only → comfort-giving
    ② = feel MY concern only → information-seeking
    ③ = feel BOTH → compound seeking behavior
    → PFC LABEL KHÁC: ① "thương" ② "lo" ③ "vừa thương vừa lo"
    → Seeking behavior KHÁC: ① giúp ② check ③ both

  🟡 3 firing patterns (independent / independent / sequential) = drill synthesis
  🟢 Embodied-Mirror alone: Singer 2004 (empathy for fictional character → ACC fire)
  🟢 Gap-Predict alone: consistent with "xa mẹ mới biết thương" (§8) — Gap-Predict without Embodied-Mirror
```

### §2.4.3 — 3 PAIN TYPES: OBSERVABLE DISTINCTION

> Nguồn: Drill-Agent-Feed-Channel v2.2 §5.

```
⭐⭐ 3 PAIN TYPES CẢM THẤY KHÁC NHAU, SEEK KHÁC NHAU:

  ┌─────────────────────────┬──────────────────────┬──────────────────────────────┐
  │ Pain type               │ Signal               │ Seeking behavior             │
  ├─────────────────────────┼──────────────────────┼──────────────────────────────┤
  │ Hardware gap pain       │ "trống, thiếu, lạnh" │ Muốn ôm, muốn gặp            │
  │ (gap unfilled NOW)      │ HIỆN TẠI             │ = direct gap FILL            │
  ├─────────────────────────┼──────────────────────┼──────────────────────────────┤
  │ Gap-Predict             │ "lo, bất an, worry"  │ Muốn check, gọi điện         │
  │ (FUTURE threatened)     │ TƯƠNG LAI            │ = VERIFY gap-fillability     │
  ├─────────────────────────┼──────────────────────┼──────────────────────────────┤
  │ Embodied-Mirror         │ "đau cùng, xót"      │ Muốn giúp entity hết đau     │
  │ (simulate entity)       │ PRESENT but OTHER's  │ = REDUCE entity's pain       │
  └─────────────────────────┴──────────────────────┴──────────────────────────────┘

  3 EXPERIENCES KHÁC NHAU. 3 SEEKING BEHAVIORS KHÁC NHAU:
    → CÙNG entity (mẹ) có thể fire cả 3:
      "Nhớ ôm mẹ" = hardware gap pain (Touch/Comfort unfilled NOW)
      "Lo mẹ già" = Gap-Predict anticipatory (predict mẹ's future state → my gaps threatened)
      "Thấy mẹ đau → xót" = Embodied-Mirror (simulate mẹ's pain on own circuits)
    → 3 experiences ĐỒNG THỜI hoặc ĐỘC LẬP tùy context

  TIME-REFERENCE DISTINCTION:
    Hardware gap = HIỆN TẠI (gap unfilled right now)
    Embodied-Mirror = HIỆN TẠI nhưng OTHER's state (entity pain right now, mapped onto me)
    Gap-Predict anticipatory = TƯƠNG LAI (predict gap-fillability trajectory)
    → 3 time-references: MY present / OTHER's present / MY future

  VERBALIZATION × 3 PAIN TYPES:
    "Nhớ mẹ quá" = Hardware gap (Touch, Safety unfilled) — Direct-State feel
    "Sao lo cho mẹ quá" = Gap-Predict (predict mẹ's state → my gaps) — Evaluative feel
    "Thấy mẹ đau mà xót" = Embodied-Mirror (mirror mẹ's pain) — Direct-State feel
    → Connects to §10.2: verbalization = f(which pain type × Reward-Signal-Architecture Evaluative:Direct-State)

  GRIEF DECOMPOSITION (Entity-Compiled §7):
    Grief = A(gap-feed loss) + B(rebuild cost) + C(phantom firing):
      A = Gap-Predict PERMANENT (gap-fillability = 0 vĩnh viễn → chronic anticipatory pain)
      B = PFC computation (rebuild cost, not body pain type)
      C = Hardware gap (compiled routines fire → no response → Chunk-Miss pain)
    → Embodied-Mirror DROPS to 0 khi entity absent (không còn entity state để simulate)
    → NHƯNG: Embodied-Mirror CÓ THỂ fire khi RECALL entity in pain (PFC retrieve → Embodied-Mirror simulate)
    → Grief = primarily Hardware gap pain (C) + Gap-Predict anticipatory (A). Embodied-Mirror = episodic only.

  🟡 3 pain types + observable distinction = drill synthesis
  🟢 Hardware gap pain: Gap-Body-Need v2.0 §2-§4. Eisenberger 2003.
  🟢 Embodied-Mirror: Singer 2004. Entity-Compiled §2.3.
  🟡 Gap-Predict anticipatory: §2.4 mechanism reframe
  🟡 Grief decomposition × 3 pain types = framework synthesis
```

---

## §3 — 2-LUỒNG + 2-TẦNG × VALENCE VISIBILITY

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §2 + Connection v5.0 §3.3 + Empathy v2.2 §8.

```
⭐ TỪ Connection §3.3 + Empathy §8 + Resonance-Per-Entity v1.1 §3:

  Valence-Momentary — Self-Pattern-Modeling-OWNED:
    Source: MỖI LẦN Self-Pattern-Modeling Compiled fire on entity
    Duration: per-episode, TRANSIENT
    Valence: + or - tùy current interaction
    Cost: Self-Pattern-Modeling processing cost
    VD: "Mẹ cười → vui lây" (Valence-Momentary+), "mẹ la → khó chịu" (Valence-Momentary-)
    
  Valence-Structural — ENTITY-COMPILED:
    Source: compiled valence depth (entity = body-base extension)
    Duration: SUSTAINED, persistent
    Valence: per-CHANNEL (can be + and - simultaneously)
    Cost: ≈ 0 (compiled = automatic)
    VD: "Con = part of me" (Valence-Structural+), "Kẻ thù = threat to me" (Valence-Structural-)

  2-TẦNG × VALENCE VISIBILITY (Connection v5.0 §3.2b):
  
    TẦNG A — HARDWARE-DRIVEN valence:
      Source: hormone, CT afferents, attachment circuits
      PFC visibility: LOW (automatic, below threshold khi stable)
      VD: oxytocin khi ôm con → warm → PFC "bình thường" (habituated)
      → Tầng Hardware valence = INVISIBLE most of the time (hardware = default)
      → Becomes VISIBLE only through disruption (loss, absence)
      
    TẦNG B — Self-Pattern-Modeling-DRIVEN valence:
      Source: Self-Pattern-Modeling Compiled/Fresh fire → prediction-delta → body-feedback
      PFC visibility: HIGH (PFC computes → PFC observes)
      VD: bạn kể insight mới → Self-Pattern-Modeling evaluate → "thú vị!" (PFC label)
      → Tầng PFC valence = VISIBLE per episode (PFC is the source)
      → Habituates IF prediction complete (same insight = no delta)

  PER-ENTITY Valence-Momentary:Valence-Structural × TẦNG A:B PROPORTION (Resonance-Per-Entity v1.1 §3-§8):

    ┌────────────────┬───────────────────────────────┬──────────────────────────────┬──────────────────────┐
    │ Entity         │ 2-luồng                       │ 2-tầng                       │ Valence visibility   │
    │                │ (Momentary:Structural)        │ (A:B)                        │ implication          │
    ├────────────────┼───────────────────────────────┼──────────────────────────────┼──────────────────────┤
    │ Mẹ→Con         │ Valence-Structural dominant   │ Tầng Hardware dominant       │ INVISIBLE most time  │
    │                │                               │ (hardware)                   │ → visible on loss    │
    ├────────────────┼───────────────────────────────┼──────────────────────────────┼──────────────────────┤
    │ Con→Mẹ (child) │ Momentary→Structural shift    │ A+B balanced                 │ MIXED visibility     │
    │                │ (forming)                     │                              │ → shifts with age    │
    ├────────────────┼───────────────────────────────┼──────────────────────────────┼──────────────────────┤
    │ Bạn thân       │ Valence-Momentary dominant    │ Tầng PFC dominant            │ VISIBLE per episode  │
    │                │                               │ (Self-Pattern-Modeling only) │ → fades between      │
    ├────────────────┼───────────────────────────────┼──────────────────────────────┼──────────────────────┤
    │ Romantic       │ Momentary→Structural          │ A→B shift                    │ Limerence=visible    │
    │ post-limerence │ (if compiled)                 │                              │ → post-limerence     │
    │                │                               │                              │   =invisible         │
    ├────────────────┼───────────────────────────────┼──────────────────────────────┼──────────────────────┤
    │ Colleague      │ Valence-Momentary only        │ Tầng PFC                     │ VISIBLE only in      │
    │                │ (unless close)                │ (Self-Pattern-Modeling only) │ Agent-mode moments   │
    └────────────────┴───────────────────────────────┴──────────────────────────────┴──────────────────────┘

  ⭐ KEY INSIGHT:
    Valence-Structural dominant + Tầng Hardware dominant = MOST INVISIBLE valence (mẹ→con)
    Valence-Momentary dominant + Tầng PFC dominant = MOST VISIBLE valence (bạn thân)
    → PARADOX: DEEPEST bond = LEAST VISIBLE valence
    → "Sống với mẹ 20 năm, không thấy gì" = Valence-Structural+A → both invisible
    → "Gặp bạn mới, vui ghê" = Valence-Momentary+B → both visible
    → Explains "có mới nới cũ" illusion at mechanism level

  2 STREAMS CÓ THỂ CONFLICT (Connection §3.3):
  
    ┌──────────────────┬───────────────────┬───────────────────┬─────────────────────────────────────────┐
    │ Case             │ Valence-Momentary │ Valence-Structural│ Result                                  │
    ├──────────────────┼───────────────────┼───────────────────┼─────────────────────────────────────────┤
    │ Mẹ chăm con ốm  │ - (pain)          │ + (ext.)          │ Structural > Momentary → VẪN CHĂM        │
    │ Bạn kể chuyện   │ + (joy)           │ + (ext.)          │ COMPOUND reward                          │
    │ Bác sĩ chăm lạ  │ - (pain)          │ ≈ 0               │ Momentary tích lũy → BURNOUT             │
    │ Con giận mẹ la   │ - (anger)         │ mixed             │ "vừa giận vừa thương"                   │
    │ Kẻ thù thua     │ + (rev.)          │ + (safe)          │ COMPOUND (Schadenfreude)                 │
    └──────────────────┴───────────────────┴───────────────────┴─────────────────────────────────────────┘
    
  BURNOUT FORMULA (Empathy §8):
    Burnout = f(Valence-Momentary cost tích lũy / Valence-Structural compensation)
    Valence-Structural CAO + Valence-Momentary vừa → KHÔNG burnout (mẹ chăm con)
    Valence-Structural ≈ 0 + Valence-Momentary bất kỳ → BURNOUT (bác sĩ chăm stranger)
    Valence-Structural CAO + Valence-Momentary CỰC CAO kéo dài → VẪN burnout (cha mẹ trẻ khuyết tật)
    
  🟢 Valence-Momentary/Valence-Structural: Connection §3.3, Body-Coupling §1.3
  🟢 Burnout formula: Empathy §8, Figley 2002
  🟢 2-tầng: Connection v5.0 §3.2b
  🟡 Valence-Structural+A = invisible, Valence-Momentary+B = visible paradox = framework synthesis
```

---

## §4 — 3 FIRING MODES

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §3.

```
⭐⭐ ENTITY-COMPILED VALENCE FIRE THEO 3 FIRING MODES:

  FIRING-MAINTENANCE (entity present, hàng ngày):
    Entity PRESENT → routine fire → Valence-Structural channels active → opioid LOW-LEVEL
    VTA HABITUATED → reward = BASELINE → PFC sees NOTHING special
    = "Background warmth" — có nhưng INVISIBLE
    = "Ở với mẹ 20 năm, không thấy gì đặc biệt"
    
    Hardware-subsidy MODULATES Firing-Maintenance (§5):
      HIGH subsidy (mẹ→con): opioid trickle MAINTAINED → baseline RICHER
        → Even habituated, body STILL gets anti-habituation signals
        → "Mẹ chán con" = pathological (hardware-subsidy SHOULD prevent)
      NONE subsidy (bạn): opioid trickle WITHOUT protection
        → VTA habituates FASTER → Firing-Maintenance reward WEAKER
        → "Gặp bạn hàng ngày → bình thường" = no subsidy → fast habituation
      TEMPORARY subsidy (romantic limerence): SIMULATES rich Firing-Maintenance
        → Fades after 18-36m → Firing-Maintenance reward DROPS → "hết lửa"
    
    Satiation type × Firing-Maintenance:
      Cyclic channels: Firing-Maintenance = oscillating (on/off/on)
      Tonic channels: Firing-Maintenance = continuous baseline (invisible)
      Generative channels: Firing-Maintenance = only if novelty continues (else → habituate)
      
  FIRING-CHUNK-MISS (entity absent, cấp tính):
    Entity ABSENT → compiled routine fire → no response → PAIN
    = O'Connor 2023: basal ganglia VẪN fire "entity sẽ ở đây"
      TRONG KHI medial temporal biết "đã mất/xa" → 2 systems CONFLICT
    = Bowlby 3 phases: Protest → Despair → Detachment
    
    Timeline:
      Hours-days: ACUTE (routine disrupted → Chunk-Miss liên tục)
      Weeks: CALIBRATING (brain redirect → pain ↓ dần)
      Months: ADAPTED (most routines redirected → occasional trigger only)
      = "Nhớ mẹ vài ngày đầu, rồi quen" = calibration trajectory
    
    Calibration speed depends on:
      → Entity-Compiled depth (deeper → more routines disrupted → slower calibration)
      → Hardware-subsidy (HIGH → hardware KEEPS firing → slower calibration)
      → Alternative gap-fill (other entities available → faster)
      → Hardware reactivity (Highly Sensitive Person → more intense → slower)
      → Attachment style (anxious → slower, avoidant → suppress → "faster")
      → Satiation type (Tonic channels → slowest fade, Cyclic → fastest)
      
  FIRING-CONTEXT-TRIGGER (entity absent, tình cờ):
    External cue → match Entity-Compiled spoke → hub activate → Valence-Structural fire → body-feedback
    = UNPREDICTABLE (context-dependent)
    
    Triggers ranked by intensity:
      SENSORY DIRECT: thấy bà cụ giống mẹ → visual spoke → fire
      NARRATIVE: đọc bài Facebook về bố vất vả → linguistic match → fire
      ARTICULATION: đọc thơ về công ơn cha mẹ → FULL articulation → fire MẠNH
        → = §8 "New appreciation" mechanism
      OLFACTORY: smell mùi quen → olfactory direct to amygdala → fire NHANH
        → 🟢 Herz 2004: odor-evoked memory MORE emotional than visual
      CIRCUMSTANTIAL: buồn/lonely → brain RETRIEVE Entity-Compiled positive chunks → fire
        → = §9 Nostalgia as self-regulation
      SOCIAL MEDIA: "On this day" photos, friend posts, viral content
        → Technology creates SYSTEMATIC Context-Triggers (§13)
    
    Intensity = f(cue specificity × Entity-Compiled depth × current gap state × hardware reactivity × subsidy)
    
  🟢 VTA habituation: Schultz 1997
  🟢 Chunk-Miss + basal ganglia: O'Connor 2023
  🟢 Bowlby 3 phases: Bowlby 1969 (established)
  🟢 Olfactory-amygdala direct path: Herz 2004
  🟡 3 firing modes + hardware-subsidy modulation + satiation interaction = framework synthesis
```

### §4.1 — 8 Kênh Valence-Structural Trở Nên Visible

> **v1.0 GAP absorbed** — từ Drill-Entity-Valence-Dynamics v2.0 §6.
> Formal taxonomy mở rộng Firing-Context-Trigger thành specific channels.

```
⭐ 8 KÊNH QUA ĐÓ Valence-Structural TRỞ NÊN VISIBLE CHO PFC:

  A — INVISIBLE KHI STABLE: VTA habituated = default. PFC sees nothing.
     = Firing-Maintenance. Valence-Structural CÓ ĐÓ nhưng baseline = invisible.
  
  B — EXTERNAL TRIGGER: sensory/narrative/context match Entity-Compiled spoke → Valence-Structural fire
    VD: "Thấy bà cụ nhặt rác giống mẹ" → visual spoke → fire
    VD: "Đọc bài Facebook bố vất vả" → linguistic match → fire
    VD: "Ngửi mùi nước hoa quen" → olfactory direct → fire NHANH
    
  C — Self-Pattern-Modeling OUTPUT: someone mention entity → Self-Pattern-Modeling fire → Valence-Structural activate
    VD: "Ai đó nhắc tới mẹ bạn" → Self-Pattern-Modeling fire → Valence-Structural tag lên → feel
    
  D — LOSS / CHUNK-MISS: entity absent → full depth REVEALED
    VD: "Lên đại học → nhớ mẹ" = Valence-Structural entire depth fire → pain
    = MẠNH NHẤT vì: toàn bộ Valence-Structural fire simultaneously
    = Firing-Chunk-Miss
    
  E — LOGIC-FEELING MISMATCH: PFC says X but body says Y → conflict visible
    VD: "Miệng nói ghét mẹ nhưng body thấy thương" → dissonance → PFC notice
    
  F — PFC RECALL (proxy trigger): chủ động nhớ → chunks fire → Valence-Structural auto
    VD: "Tối nằm nhớ mẹ" → recall → Entity-Compiled fire → Valence-Structural fire → body feel
    → CAN become nostalgia self-regulation tool (§9)

  TECHNOLOGY ERA — 2 KÊNH MỚI:
  
  G — SOCIAL MEDIA TRIGGER: platform-mediated Context-Trigger
    VD: "On this day" feature → past photos → SYSTEMATIC Valence-Structural activation
    VD: Friend post about parent → narrative match → B channel fire
    VD: Viral "letter to mom" video → articulation trigger → §8 mechanism
    
    ⭐ Social media = TECHNOLOGY creates SYSTEMATIC Context-Triggers
      Pre-technology: Firing-Context-Trigger = RANDOM (organic encounters)
      Post-technology: Firing-Context-Trigger = SYSTEMATIC (algorithmic, curated, daily)
      → More Valence-Structural visibility events PER DAY than pre-technology era
      → NHƯNG: may also habituate (daily exposure → VTA adapt to platform triggers)
    
  H — AI PARTIAL TRIGGER: AI output match Entity-Compiled patterns → PARTIAL Valence-Structural fire
    VD: AI write about mẹ → linguistic match → Valence-Structural fire
    → NHƯNG: AI = no entity → no mutual → no resonance
    → AI triggers EXISTING Valence-Structural, does NOT create Valence-Structural

  MAPPING → 3 FIRING MODES:
    Channel A = Firing-Maintenance
    Channel D = Firing-Chunk-Miss
    Channels B, C, E, F, G, H = Firing-Context-Trigger subtypes
    → 8-channel taxonomy = Firing-Context-Trigger DECOMPOSED into specific trigger types

  🟢 6 channels: Body-Coupling §1.4 (framework established)
  🟡 Social media + AI as new trigger channels = framework synthesis
```

---

## §5 — VTA HABITUATION × HARDWARE-SUBSIDY

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §4.

```
⭐⭐ UNIFIED MODEL: TẠI SAO VALENCE "INVISIBLE" Ở DIFFERENT RATES:

  CƠ CHẾ GỐC (Body-Coupling §1.4 + Body-Feedback-Mechanism §3.2):
    Entity present REPEATEDLY → VTA encode as BASELINE
    VTA only fire reward khi: ACTUAL > BASELINE (positive prediction-delta)
    Entity present = EXPECTED = baseline met → delta = 0 → VTA silent
    → PFC: "bình thường, không có gì"
    → Body: Valence-Structural channels VẪN fire → opioid trickle → but below PFC threshold
    
  HARDWARE-SUBSIDY = WHY DIFFERENT ENTITIES HABITUATE AT DIFFERENT RATES:
  
    VTA habituation = UNIVERSAL law (Schultz 1997)
    NHƯNG: hardware-subsidy COUNTER habituation ở DIFFERENT LEVELS
    (from Resonance-Per-Entity v1.1 §2)
    
    ┌────────────────────┬──────────────────────┬───────────────────────────┐
    │ Subsidy Level      │ Entity               │ Valence Habituation Rate  │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ MAXIMUM            │ Mẹ→Con               │ VERY SLOW                 │
    │ (oxytocin +        │                      │ Multiple hardware systems COUNTER│
    │ baby schema +      │                      │ VTA habituation actively  │
    │ synchrony +        │                      │ → valence invisible but   │
    │ prolactin)         │                      │ RICHER baseline than others│
    │                    │                      │ → loss = DEVASTATING delta │
    │                    │                      │ 🟢 Feldman 2012           │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ MODERATE           │ Con→Mẹ, Kin          │ SLOW                      │
    │ (attachment hardware,    │                      │ Attachment scaffold slows  │
    │ oxytocin scaffold) │                      │ habituation somewhat      │
    │                    │                      │ 🟢 Roberts & Dunbar 2011: │
    │                    │                      │ kin resilient without     │
    │                    │                      │ active maintenance        │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ TEMPORARY          │ Romantic (limerence)  │ ARTIFICIALLY SLOW → FAST  │
    │ (dopamine +        │                      │ 18-36m: SIMULATES slow    │
    │ norepinephrine     │                      │ Post-limerence: subsidy   │
    │ surge, 18-36m)     │                      │ EXPIRES → standard rate   │
    │                    │                      │ → "hết lửa" = subsidy end │
    │                    │                      │ 🟢 Fisher 2004            │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ NONE               │ Bạn thân, Colleague  │ STANDARD (fastest)        │
    │ (general μ-opioid  │                      │ No dedicated counter-hardware   │
    │ only)              │                      │ → VTA habituates at       │
    │                    │                      │ default rate              │
    │                    │                      │ → MUST maintain via novelty│
    │                    │                      │ 🟢 Panksepp 1998          │
    └────────────────────┴──────────────────────┴───────────────────────────┘

  PARADOX ENRICHED:
    Entity-Compiled DEEPER + HIGH SUBSIDY → VTA habituated SLOWER → reward STILL somewhat visible
    Entity-Compiled DEEPER + NO SUBSIDY → VTA habituated FASTEST → reward MOST invisible
    
    → Mẹ→con: DEEP Entity-Compiled + MAX subsidy = habituated but RICH baseline
    → Bạn thân: DEEP Entity-Compiled + NO subsidy = habituated and LEAN baseline
    → = TẠI SAO "mất mẹ" = devastating nhưng "mất bạn" = recoverable
    → = KHÔNG chỉ depth → cả subsidy determines loss severity
    
    → Limerence DEEP + TEMP subsidy = INTENSE visible (reward FEELS strong)
    → Post-limerence: SAME depth nhưng subsidy GONE → reward ↓↓
    → = "Yêu lúc đầu mãnh liệt" → "Giờ bình thường" = subsidy expired, NOT love gone
    
  ONLY VISIBLE THROUGH:
    → ABSENCE (Firing-Chunk-Miss): entity removed → baseline violated → pain
    → TRIGGER (Firing-Context-Trigger): context cue → Valence-Structural fire above threshold → feel
    → COMPARISON: new entity (no habituation) vs old (habituated) → old "feels less"
    → = "Có mới nới cũ" = VTA comparison, NOT bond quality comparison
    
  ⭐ HARDWARE-SUBSIDY = BIDIRECTIONAL AMPLIFIER (Dissonance-Signal-Architecture.md v1.0 §6.2):
    §5 trên = reward direction (subsidy slows VTA habituation → reward invisible).
    NHƯNG: Hardware-Subsidy CŨNG amplifies DISSONANCE from entity:
      Mẹ mắng: Entity-Compiled (Mức 4+) + Hardware-Subsidy MAX
        → Evaluative Dissonance AMPLIFIED → body response STRONGER
      Stranger mắng: NO Hardware-Subsidy
        → Evaluative Dissonance = base level → weaker body response
    → CÙNG mechanism: mẹ khen > stranger khen (reward) + mẹ mắng > stranger mắng (dissonance)
    → Hardware-Subsidy = KHÔNG CHỈ anti-habituation, mà là AMPLIFIER cả 2 chiều.

  🟢 VTA habituation: Schultz 1997 (dopamine prediction error)
  🟢 Hedonic adaptation: Bao & Lyubomirsky 2013
  🟢 Hardware-subsidy mechanisms: Feldman 2012, Fisher 2004, Panksepp 1998
  🟡 Subsidy × habituation rate = unified per-entity model = framework synthesis
  🟡 Subsidy bidirectional (reward + dissonance) = framework synthesis (Dissonance-Signal-Architecture v1.0)
```

---

## §6 — VALENCE × SATIATION TYPE

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §5.

```
⭐⭐ VALENCE DYNAMICS KHÁC CĂN BẢN PER SATIATION TYPE:

  (Gap-Body-Need v2.0 §2: Cyclic / Tonic / Generative)

  CYCLIC VALENCE — SHARP OSCILLATION:
    Gap fill → reward → gap OFF → no valence signal → gap RETURN → need again
    = Valence oscillates with fill/unfill cycle
    
    Characteristics:
      → SHARP onset: gap fires → valence IMMEDIATE
      → SHARP offset: gap filled → valence DROPS
      → Predictable rhythm: body knows cycle
      → VD: "đói" (negative) → "no" (positive) → "đói lại" (negative lại)
      → VD: mẹ la (avoidance) → mẹ thôi (relief) → episode-bound
    
    Valence implications:
      → Cyclic channels = MOST VISIBLE (high delta per cycle)
      → Cyclic channels = MOST FORGETTABLE (episode-bound → decay fast)
      → "Quên chuyện cãi nhau" (negative Cyclic) but "nhớ cảm giác ấm" (Tonic)

  TONIC VALENCE — SLOW INVISIBLE BASELINE:
    Gap fill ongoing → reward LOW-LEVEL → VTA habituate → INVISIBLE
    = Valence builds slowly, becomes background, invisible when present
    
    Characteristics:
      → SLOW onset: tonic builds over weeks/months
      → INVISIBLE when present (VTA habituated = baseline)
      → DEVASTATING when removed (baseline violation = large delta)
      → VD: comfort from mẹ = 20 năm background → "không thấy gì" → mẹ mất → PAIN
      → VD: safety at home = invisible → homeless → visible
    
    Valence implications:
      → Tonic channels = LEAST VISIBLE (below PFC threshold)
      → Tonic channels = SLOWEST DECAY (compiled deep, hardware-supported if subsidy)
      → Tonic valence = INVISIBLE while present, DEVASTATING when absent
      → = THE "không khí" of entity-valence dynamics
      → DIRECTLY connects to VTA habituation (§5)

  GENERATIVE VALENCE — RENEWABLE EXCITING:
    Gap fill → new gap CREATE → new fill → new gap → perpetual
    = Valence renews with each novelty cycle
    
    Characteristics:
      → SELF-RENEWING: fill creates new gap → new delta → new reward
      → NOVELTY-DEPENDENT: same content → habituate → need NEW
      → EXCITING "feel": Evaluative dominant (insight, discovery)
      → VD: bạn thân kể chuyện mới → insight → new question → new insight
      → VD: partner cùng khám phá → shared discovery → both rewarded
    
    Valence implications:
      → Generative channels = MOST VISIBLE (high novelty = high delta)
      → Generative channels = FASTEST HABITUATION without novelty input
      → Generative valence = "exciting" component of relationships
      → = TẠI SAO new relationships "feel more" — Generative channels ACTIVE
      → = TẠI SAO old relationships "feel less" — Generative HABITUATED

  COMPOUND DYNAMICS (most entities):
    Most deep entities = Tonic + Generative compound:
    
    Mẹ→con: Tonic dominant + Generative bursts (child changes daily)
    → Tonic = invisible safety. Generative = "con mỗi ngày 1 khác"
    → Valence trajectory: STABLE (auto-novelty + max subsidy)
    
    Bạn thân: Generative dominant + Tonic component
    → Generative = "nói chuyện hay." Tonic = "gặp thì thoải mái"
    → Valence trajectory: NOVELTY-DEPENDENT (no subsidy → must maintain)
    
    Romantic post-limerence: Tonic + Generative (if genuine match)
    → Tonic = "thoải mái bên nhau." Generative = "vẫn exciting"
    → Valence trajectory: ACTIVE EFFORT required (limerence subsidy expired)
    
    Colleague: Generative dominant (domain-specific)
    → Generative = "work together → learn." Tonic = minimal
    → Valence trajectory: CONTEXT-DEPENDENT (only in Agent-mode moments)

  ⭐ "CHÁN" = GENERATIVE DIES + TONIC SURVIVES (→ Boredom.md v2.0):
    Most relationships = Tonic + Generative compound
    "Chán" = Generative component habituated + Tonic invisible
    → "Vẫn thoải mái nhưng không exciting" = Tonic intact, Generative dead
    → PFC only sees: no Generative reward + Tonic invisible = "chán"
    → Body reality: Tonic STILL PROVIDES, PFC just can't see it
    → Boredom.md v2.0 §3: source ⑥ by-product match dừng, Resonance Decline
    → Chi tiết: §6.1

  🟡 Satiation type × valence dynamics = framework synthesis
  🟢 3 satiation profiles: Gap-Body-Need v2.0 §2 (established independently)
  🟢 VTA habituation per reward type: Schultz 1997
```

### §6.1 — "Chán" × Valence Decline

> **v1.0 GAP absorbed** — từ Drill-Entity-Valence-Dynamics v2.0 §14.
> Phân tích chi tiết "chán" qua Resonance Decline (2 Forces + 1 Fuel) + satiation type decomposition.

```
⭐⭐ "CHÁN" = VALENCE DECLINE QUA 2 FORCES + 1 FUEL + SATIATION TYPE DECOMPOSITION:

  2 FORCES + 1 FUEL (Bond-Architecture v2.0 §4):
  
    FORCE: COMPILED-SUPPRESS (nhân tạo, ★ LEVERAGE POINT):
      Gap riêng bị suppress → mất drive → mất by-product
      → By-product match STOPS → resonance declines → valence ↓
      → ATTACKS SOURCE of valence (kill the drive that produces by-product)
      → Accelerates Reward-Habituated + drains novelty fuel
      
    FORCE: REWARD-HABITUATED (tự nhiên, ĐỘC LẬP):
      Weber-Fechner → same stimulus → VTA giảm fire
      → MODULATED by hardware-subsidy (§5):
        HIGH subsidy → habituation SLOWED (mẹ→con: subsidy counters)
        NONE subsidy → habituation STANDARD rate (bạn thân: habituates naturally)
        
    FUEL: NOVELTY ≥ THRESHOLD? (tự nhiên, PROBABILISTIC):
      2 lenses cùng 1 phenomenon:
        Lens prediction: Self-Pattern-Modeling compiled SÂU → predict HOÀN HẢO → no prediction-delta → no reward
        Lens knowledge: All channels COMPILED → no new chunks to add → self-expansion rate = 0 (Aron & Aron 1996)

  SATIATION TYPE × "CHÁN" MECHANISM:
  
    CYCLIC channels: IMMUNE to "chán" (inherently oscillate → always return)
      → Hunger always returns → always need to eat → CANNOT habituate permanently
      → "Chán ăn" = temporary (Cyclic off-phase), NOT structural "chán"
      
    TONIC channels: MOST VULNERABLE to invisibility (habituate to baseline)
      → Comfort = baseline → VTA habituate → "bình thường"
      → Tonic "chán" = NOT really bored → just INVISIBLE
      → ≠ actual decline → = PFC threshold issue
      → FIX: absence reveals (Firing-Chunk-Miss), trigger reveals (Firing-Context-Trigger)
      
    GENERATIVE channels: MOST VULNERABLE to actual "chán"
      → Novelty dries up → no new gap → no new delta → no reward
      → "Biết hết rồi, không có gì mới" = Generative DEAD
      → TRUE structural decline (not just invisible — actually GONE)
      → FIX: new shared experiences → new Generative source

  ⭐ "CHÁN" = GENERATIVE DIES + TONIC SURVIVES:
    Most relationships = Tonic + Generative compound
    "Chán" = Generative component habituated + Tonic invisible
    → "Vẫn thoải mái nhưng không exciting" = Tonic intact, Generative dead
    → PFC only sees: no Generative reward + Tonic invisible = "chán"
    → Body reality: Tonic STILL PROVIDES, PFC just can't see it
    
    BOREDOM-MECHANISM CONNECTION:
      Boredom.md v2.0: boredom = dissonance + blurred Imagine-Final
      → Relationship "chán" = body detects gap (Generative died) nhưng PFC 
        KHÔNG CÓ direction (don't know HOW to fix → Imagine-Final blurred)
      → KHÁC "ghét" which HAS clear direction (avoid this specific thing)

  PER-ENTITY "CHÁN" PATTERNS:
  
    Mẹ→con: "CHÁN" EXTREMELY RARE
      → Tonic: PROTECTED by MAX subsidy → slow habituation
      → Generative: AUTO (child changes daily → built-in novelty source)
      → "Mẹ chán con" = pathological (hardware dysfunction)
      
    Bạn thân: "CHÁN" = Reward-Habituated + novelty dưới ngưỡng (natural, fixable)
      → Generative habituated (same routine) + NO subsidy to counter
      → FIX: new shared activities (Aron 2000)
      
    Romantic post-limerence: "CHÁN" = ALL MECHANISMS COMPOUND → HIGHEST RISK
      → Limerence inflated baseline → reality < baseline → disappoint
      → No permanent hardware-subsidy (limerence expired)
      → Max habituation exposure (live together daily)
      → Schema "phải yêu" → compiled suppress genuine complaints (Compiled-Suppress)
      → Gottman Type 2: emotional disengagement → divorce ~16.2 years

  🟢 4 mechanisms: Boredom.md v2.0 §3
  🟢 Gottman & Levenson 2000: Type 2 divorce ~16.2 years
  🟢 Aron & Aron 1996: self-expansion model
  🟡 Satiation type × "chán" + boredom-mechanism connection = framework synthesis
```

---

## §7 — MIXED VALENCE: PARALLEL PER-CHANNEL

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §7.

```
⭐⭐ POSITIVE + NEGATIVE = 2 HỆ THỐNG THẦN KINH ĐỘC LẬP:

  🟢 Cacioppo & Berntson 1994 (Psychological Bulletin):
     EVALUATIVE SPACE MODEL:
     Positive và negative affect = 2 SEPARATE, PARTIALLY INDEPENDENT substrates
     → CÓ THỂ co-activate → CẢ HAI HIGH cùng lúc = mixed
     
  🟢 Vaccaro, Kaplan & Damasio 2020 (Perspectives on Psych. Science):
     TWO-LEVEL ARCHITECTURE:
       Level 1 (brainstem): RAPID SWITCHING giữa positive/negative
       Level 2 (insular cortex): INTEGRATION thành unified "mixed" feeling
     → BOTH switching AND genuine co-activation
     
  🟢 Larsen, McGraw & Cacioppo 2001 (JPSP):
     Students moving out: CẢ happy VÀ sad đồng thời
     → Experimental confirmation of co-activation
     
  🟢 Schneider et al. 2021:
     Mouse-tracking: ambivalent ≠ neutral (BEHAVIORALLY distinct)
     → "Không cảm thấy gì" ≠ "vừa thương vừa giận"

  FRAMEWORK MAPPING (Valence-Propagation.md v4.1 §2, §2.1):
    Per-channel valence = multi-dimensional (not bipolar axis)
    CẢ positive AND negative channels CÓ THỂ fire cùng lúc
    = Framework MORE GRANULAR than Evaluative Space Model (per-CHANNEL not just 2 dimensions)
    
  MIXED VALENCE × SATIATION TYPE:
    
    Cyclic channels: approach + avoidance CÓ THỂ OSCILLATE independently
      → Mẹ nấu ăn (approach, Cyclic) + mẹ la (avoidance, Cyclic)
      → 2 Cyclic channels fire CÙNG LÚC = "vừa giận vừa thấy thương"
      
    Tonic channels: approach baseline STABLE + avoidance channel INTERMITTENT
      → Mẹ comfort (approach, Tonic = invisible) + mẹ la lúc này (avoidance, Cyclic)
      → Mixed = Tonic baseline (invisible) + Cyclic episode (visible)
      → PFC ONLY observes Cyclic → labels "ghét mẹ" → BUT Tonic STILL THERE
      
    Generative channels: almost always POSITIVE (curiosity = approach)
      → Generative avoidance RARE (unless domain anxiety = compiled fear of topic)

  PER-ENTITY MIXED PATTERNS:
  
    🟢 Lüscher & Pillemer 1998: ~50% parent-child = ambivalent = NORMATIVE
    
    Mẹ→con: LOW mixed (hardware bias → approach-dominant, avoidance rare)
    Con→mẹ: HIGH mixed (normative — approach + avoidance both active)
    Bạn thân: LOW mixed (genuine → positive-dominant, avoidance = drift apart)
    Romantic: MODERATE → HIGH (living together → more conflict channels)
    Colleague: LOW (professional → thin, not enough depth for mixed)
    
    → CLOSER + LONGER → MORE channels → MORE mixed potential (not pathological)
    
  VERBALIZATION × MIXED VALENCE:
    
    "GHÉT" = avoidance channels DOMINATE PFC observation
      → Tonic approach channels DORMANT (invisible) → PFC misses them
      → VD: "Ghét mẹ" lúc bị la = Cyclic avoidance VISIBLE + Tonic approach INVISIBLE
      
    "VỪA GIẬN VỪA THƯƠNG" = BOTH channels above PFC threshold
      → 🟢 Vietnamese: single phrase captures mixed → language facilitates
      → 🟢 Miyamoto et al. 2010: East Asian = higher ambivalence tolerance
      
    "THƯƠNG" = approach channels DOMINATE
      → If Direct-State dominant: "thương" = warm, gentle → mẹ direction
      → If Evaluative dominant: "thích" = exciting → bạn direction
      → SAME positive valence, DIFFERENT WORD → reflects Reward-Signal-Architecture Evaluative:Direct-State ratio
      
    "CHÁN" = Generative dead + Tonic habituated (§6.1 chi tiết)
      → NO visible positive signal → PFC: "chán"
      → KHÁC "ghét": chán = ABSENCE of reward, ghét = PRESENCE of threat
      → "Chán" NGUY HIỂM HƠN (silent), "ghét" NHÌN THẤY (có thể address)
      
    "KHÔNG CẢM THẤY GÌ" = Valence-Structural habituated → below PFC threshold
      → Valence-Structural VẪN CÓ nhưng VTA habituated → invisible
      → ≠ "hết thương" → = "PFC không observe"

    → Systematic verbalization × Reward-Signal-Architecture mapping: §10.2
    
  🟡 Satiation type × mixed valence + verbalization = framework synthesis
  🟢 Evaluative Space Model: Cacioppo & Berntson 1994
  🟢 Parent-child ambivalence 50%: Lüscher & Pillemer 1998
  🟢 Vietnamese mixed emotions: Fang et al. 2025, Miyamoto et al. 2010
```

---

## §8 — "XA MẸ MỚI BIẾT THƯƠNG" — 3 CƠ CHẾ CỘNG DỒN

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §8.

```
⭐⭐⭐ PARADOX: sống cùng 20 năm = đôi khi ghét. Xa mẹ = bỗng thương.

  CƠ CHẾ ① — DECAY ASYMMETRY (Entity-Compiled.md v1.2 §9):
  
    3-layer decay model:
      ③ Negative EPISODES (cãi nhau, bị la): FADE NHANH NHẤT (months)
        → Hippocampus-dependent → most vulnerable to decay
        → CYCLIC avoidance channels → episode-bound → decay FAST (§6)
      ② Positive AFFECT (warmth, safety, love): FADE CHẬM HƠN
        → Reward circuits → more resistant
        → TONIC approach channels → baseline → decay SLOW (§6)
      ① Positive SCHEMA (mẹ = ai, hình ảnh): PERSIST DECADES
        → Neocortical → very resistant
    
    → Over time: Cyclic negative EPISODES fade → Tonic positive PERSIST
    → Net valence SHIFT POSITIVE
    → "Quên hết chuyện giận, chỉ nhớ cái tốt" = decay asymmetry × satiation type

  CƠ CHẾ ② — CONTRAST EFFECT (Valence-Structural absence → visible):
  
    Enriched with hardware-subsidy (§5):
    Với mẹ: Valence-Structural = Tonic baseline → VTA habituated → INVISIBLE
    NHƯNG: hardware-subsidy (MODERATE — con→mẹ direction) → baseline RICHER than bạn
    Xa mẹ: environment mới KHÔNG CÓ Valence-Structural warmth
    → Valence-Structural absence = VISIBLE lần đầu
    → "Hóa ra ấm lắm" = contrast with new environment
    → ⭐ Subsidy explains WHY contrast STRONGER for mẹ than for bạn:
      Mẹ: richer baseline (subsidized) → larger delta on absence
      Bạn: leaner baseline (no subsidy) → smaller delta on absence
      → "Xa mẹ nhớ MẠNH hơn xa bạn" = subsidy difference, not just depth
    
  CƠ CHẾ ③ — FIRST-TIME ARTICULATION:
  
    Với mẹ: PFC bận observe NEGATIVE (conflict = salient = above threshold)
    → Positive Valence-Structural = Tonic = habituated → PFC không allocate attention
    → 20 năm body BIẾT "thương mẹ" → PFC chưa bao giờ ARTICULATE
    
    Xa mẹ + đọc thơ:
    → Thơ = linguistic chunks MÔ TẢ compiled experience
    → PFC MATCH words ↔ compiled Valence-Structural → CONFIRM → "ồ, hóa ra tôi thương mẹ lắm"
    → = Somatic-Articulation-Loop: body knows → thơ provide words → body confirm
    → FIRST-TIME observation → NO habituation → FULL emotional impact
    
    De-habituation effect:
    → Thơ present SAME content in NOVEL form
    → VTA: novel context → fire (prediction-delta > 0)
    → Cùng nội dung "mẹ hy sinh" nhưng cách trình bày MỚI → reward
    → + Negative ABSENT in poem (no daily friction)
    → = "Filtered" experience → net positive MAXIMUM
    
  3 CƠ CHẾ CỘNG DỒN:
    ① Cyclic negative faded → net positive (decay asymmetry)
    ② Subsidized baseline revealed → contrast STRONG (hardware-subsidy)
    ③ Articulation + de-habituation → PFC observe + amplify
    = "Xa mẹ mới biết thương" = NOT paradox. = 3 mechanisms STACK.
    
  "CẢM XÚC CHƯA TỪNG THỂ HIỆN BAO GIỜ TRƯỚC KIA":
    = KHÔNG PHẢI "cảm xúc mới"
    = PFC LẦN ĐẦU OBSERVE Tonic positive mà LUÔN Ở ĐÓ
    = Body biết 20 năm. PFC mới observe lần đầu khi có lens (thơ).
    
  🟢 Decay 3-layer: Entity-Compiled.md v1.2 §9
  🟢 Whiteman et al. 2011: 10-year longitudinal — conflict ↓, intimacy ↑
  🟢 Arnett 2004: leaving home → more satisfying parent relationship
  🟡 3-mechanism model + satiation type decay + subsidy contrast = framework synthesis
```

---

## §9 — NOSTALGIA = Valence-Structural ACTIVE SELF-REGULATION

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §9.

```
⭐ NOSTALGIA KHÔNG PHẢI RANDOM — LÀ BODY TỰ CHỮA:

  🟢 Sedikides & Wildschut 2018 (Review of General Psychology):
     Negative states (buồn, cô đơn, vô nghĩa) → TRIGGER nostalgia
     Nostalgia → positive affect + self-esteem + social connectedness
     = SELF-REGULATION mechanism (not just "nhớ quá khứ")
     
  🟢 Oba et al. 2016 (Social Cognitive and Affective Neuroscience):
     Memory + reward systems CO-PRODUCE nostalgic experiences
     Hippocampus (retrieve) + striatum/reward (valence) → CÙNG LÚC

  FRAMEWORK MAPPING:
    Negative state → gap unfilled → body cần stabilize
    → Brain RETRIEVE Entity-Compiled positive chunks (Valence-Structural channel F: PFC recall — §4.1)
    → Valence-Structural fire → opioid release → body STABILIZE
    → = Body DÙNG compiled Tonic warmth từ past entities làm THUỐC AN THẦN
    
    Nostalgia DÙNG TONIC channels (not Cyclic or Generative):
      → Body recalls BASELINE warmth (Tonic) not episodes (Cyclic)
      → "Nhớ cảm giác ấm áp" not "nhớ lần nấu ăn cụ thể"
      → Entities with DEEP Tonic + HIGH subsidy = strongest nostalgia source (mẹ)

  VIDEO-CALL PARADOX:
    🟢 Van Tilburg et al. 2019: students feel MOST homesick during video-chat
    FRAMEWORK: Video = PARTIAL Entity-Compiled firing → Valence-Structural fire → NHƯNG touch/smell MISSING
    → Chunk-Miss ở MISSING spokes AMPLIFIED by partial activation
    → "Gọi mẹ xong nhớ hơn" = ĐÚNG, architecturally explainable

  🟢 Nostalgia self-regulation: Sedikides 2018
  🟢 Video-call homesickness: van Tilburg 2019
  🟡 Nostalgia as Valence-Structural Tonic self-regulation = framework synthesis
```

---

## §10 — PER-ENTITY VALENCE DYNAMICS + Reward-Signal-Architecture Evaluative:Direct-State

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §10+§11.

```
⭐⭐ VALENCE DYNAMICS MAPPED PER ENTITY TYPE:

  MẸ→CON VALENCE:
    Dominant satiation: Tonic (existence-based) + Generative bursts (child changes)
    Hardware-subsidy: MAXIMUM → habituation SLOW → Firing-Maintenance = RICH baseline
    Reward-Signal-Architecture Evaluative:Direct-State: ~40Evaluative/60Direct-State → valence "feel" = ẤM ÁP (Direct-State dominant)
    2-tầng: Tầng Hardware dominant → valence INVISIBLE (hardware-driven)
    2-luồng: Valence-Structural dominant → valence STRUCTURAL (body-base extension)
    Mixed valence: LOW (hardware bias approach → avoidance rare)
    "Chán" risk: LOW (auto-novelty + max subsidy)
    Phantom on loss: DEVASTATING (all 4 factors MAX — §12)
    Technology substitute: CANNOT (CT afferents offline)
    → Trajectory: STABLE INVISIBLE baseline → visible ONLY on loss/trigger
    → = "Không thấy gì đặc biệt" → mất → DEVASTATING = signature pattern
    
  CON→MẸ VALENCE (child/teen):
    Dominant satiation: Cyclic + Tonic MIX (episodic needs + baseline safety)
    Hardware-subsidy: MODERATE → habituation SLOW-MEDIUM
    Reward-Signal-Architecture Evaluative:Direct-State: ~50Evaluative/50Direct-State → valence "feel" = BALANCED (ấm + đánh giá)
    2-tầng: A+B balanced → valence MIXED visibility
    2-luồng: Valence-Momentary→Valence-Structural shifting → valence FORMS over years
    Mixed valence: HIGH (normative 50% — Lüscher 1998)
    "Chán" risk: MODERATE (teen lifecycle shift, not true "chán")
    Phantom on loss: MAJOR (deep compilation + attachment hardware)
    Technology substitute: PARTIAL (video call maintain SOME)
    → Trajectory: FORMING → MIXED (teen) → POSITIVE SHIFT (xa mẹ = §8)
    → = "Vừa giận vừa thương" → xa mẹ → "thương mẹ mãnh liệt" = signature
    
  BẠN THÂN VALENCE:
    Dominant satiation: Generative dominant + Tonic component
    Hardware-subsidy: NONE → habituation STANDARD (fastest)
    Reward-Signal-Architecture Evaluative:Direct-State: ~70Evaluative/30Direct-State → valence "feel" = THÚ VỊ, HỨNG KHỞI (Evaluative dominant)
    2-tầng: Tầng PFC dominant → valence VISIBLE per episode
    2-luồng: Valence-Momentary dominant → valence MOMENTARY (per-interaction reward)
    Mixed valence: LOW (genuine → positive-dominant)
    "Chán" risk: HIGH if no novelty (Generative habituates fast)
    Phantom on loss: MINOR-MODERATE (replaceable, no hardware lock-in)
    Technology substitute: PARTIAL (online maintain Generative, not touch)
    → Trajectory: EXCITING → HABITUATE without novelty → FADE without contact
    → = "Gặp nhau vui ghê" → "Lâu không gặp, quên" = signature pattern

  ROMANTIC VALENCE (post-limerence):
    Dominant satiation: Tonic + Generative (if genuine match)
    Hardware-subsidy: TEMPORARY → vasopressin/oxytocin (if attachment forms)
    Reward-Signal-Architecture Evaluative:Direct-State: ~60Evaluative/40Direct-State → valence "feel" = HỨNG KHỞI + ẤM (mixed Evaluative+Direct-State)
    2-tầng: Hardware→PFC shift (limerence Tầng Hardware simulated → post-limerence Tầng PFC)
    2-luồng: Valence-Momentary→Valence-Structural (if Entity-Compiled forms)
    Mixed valence: MODERATE → HIGH (living together → more conflict channels)
    "Chán" risk: HIGHEST (inflated baseline + no permanent subsidy + max exposure)
    Phantom on loss: COMPLEX (Valence-Structural + possible hormone echo)
    Technology substitute: PARTIAL (communication, not physical intimacy)
    → Trajectory: INTENSE (limerence) → 3 paths: genuine/flat/dissolution
    → = "Yêu cuồng nhiệt" → "Vẫn yêu" OR "Hết lửa" OR "Chia tay"

  COLLEAGUE VALENCE (Agent-mode moments):
    Dominant satiation: Generative (domain-specific)
    Hardware-subsidy: NONE
    Reward-Signal-Architecture Evaluative:Direct-State: ~85Evaluative/15Direct-State → valence "feel" = ĐÁNH GIÁ, KÍCH THÍCH TRÍ TUỆ
    2-tầng: Tầng PFC only → valence VISIBLE in Agent-mode only
    2-luồng: Valence-Momentary only (unless transition to friend)
    Mixed valence: LOW (professional → thin)
    "Chán" risk: MODERATE (domain routine → habituate)
    Phantom on loss: MINOR (functional, replaceable)
    Technology substitute: HIGH (remote work maintains domain Generative)
    → Trajectory: CONTEXT-DEPENDENT → only in Agent-mode → fade on job change
    → = "Nghỉ việc → quên tuột" = signature pattern
```

### §10.1 — Reward-Signal-Architecture Evaluative:Direct-State × Valence "Feel" + Hardware Reactivity

```
⭐ HARDWARE QUYẾT ĐỊNH CƯỜNG ĐỘ + Reward-Signal-Architecture QUYẾT ĐỊNH "FEEL":

  HARDWARE REACTIVITY:
    🟢 Hariri et al. 2002: 5-HTTLPR short allele → GREATER amygdala response
    🟢 Aron & Aron 1997: Highly Sensitive Person (15-20%) → deeper processing, more empathy
    🟢 Belsky & Pluess 2009: S-allele = PLASTICITY (not just vulnerability)
       More hurt under negative → BUT more appreciation under positive

  Reward-Signal-Architecture Evaluative:Direct-State × VALENCE "FEEL" (Reward-Signal-Architecture v2.1 §1):
    Direct-State dominant (opioid, CT afferents) → "ấm áp, comfortable, an toàn"
    Evaluative dominant (dopamine-adjacent) → "thú vị, exciting"
    
  ⭐ REACTIVITY × Reward-Signal-Architecture Evaluative:Direct-State = 2 INDEPENDENT AXES:
    High reactivity + Direct-State dominant = INTENSE WARMTH (sensitive+warm)
    High reactivity + Evaluative dominant = INTENSE EXCITEMENT (sensitive+curious)
    Low reactivity + Direct-State dominant = GENTLE WARMTH
    Low reactivity + Evaluative dominant = CALM INTEREST
    → 4 combinations → 4 different valence "profiles"

  Self-Pattern-Modeling vs REACTIVITY vs Reward-Signal-Architecture (phân biệt rõ):
    Self-Pattern-Modeling = prediction ACCURACY (how well predict entity)
    Reactivity = response INTENSITY (how strongly body responds)
    Reward-Signal-Architecture Evaluative:Direct-State = response QUALITY (warm vs exciting)
    → 3 trục INDEPENDENT
    
  🟢 5-HTTLPR: Hariri 2002. Highly Sensitive Person: Aron & Aron 1997. Plasticity: Belsky 2009.
  🟡 Reactivity × Reward-Signal-Architecture Evaluative:Direct-State as 2 independent axes = framework synthesis
```

### §10.2 — Verbalization = PFC Observation × Reward-Signal-Architecture

> **v1.0 GAP absorbed** — từ Drill-Entity-Valence-Dynamics v2.0 §12.
> Systematic mapping: người ta NÓI GÌ = f(which channels fire × Reward-Signal-Architecture Evaluative:Direct-State ratio).
> §7 có verbalization × mixed valence. §10.2 = comprehensive per-entity reference.

```
⭐ VERBALIZATION = PFC OBSERVATION CỦA CHANNEL STATE × Reward-Signal-Architecture Evaluative:Direct-State RATIO:

  "GHÉT" = avoidance channels DOMINATE PFC observation
    → Approach channels: DORMANT hoặc below threshold (Tonic = invisible)
    → PFC label: "ghét" → NHƯNG body VẪN CÓ Tonic approach channels
    → VD: "Ghét mẹ" lúc bị bắt học = Cyclic avoidance VISIBLE + Tonic approach INVISIBLE
    → Body reality: mixed (Tonic STILL THERE, just habituated)
    
  "VỪA GIẬN VỪA THƯƠNG" = BOTH channels above PFC threshold
    → PFC observe avoidance (giận: Cyclic mẹ la) + approach (thương: Tonic mẹ = safe)
    → CẢ HAI fire cùng lúc → PFC CAN verbalize both
    → 🟢 Vietnamese: single phrase "vừa giận vừa thương"
    → 🟢 Miyamoto et al. 2010: East Asian = higher ambivalence tolerance
    → = Language REFLECTS AND FACILITATES mixed experience
    
  "THƯƠNG" = approach channels DOMINATE PFC observation
    → Avoidance channels: dormant, faded, or below threshold
    → If Direct-State dominant: "thương" = warm, gentle → mẹ direction
    → If Evaluative dominant: "thích" = exciting, stimulating → bạn direction
    → SAME positive valence, DIFFERENT WORD → reflects Reward-Signal-Architecture Evaluative:Direct-State ratio
    
  "NHỚ" = Chunk-Miss or Context-Trigger activated
    → If Tonic channel activated: "nhớ cảm giác ấm" = Direct-State dominant → "nhớ quá"
    → If Generative channel activated: "nhớ lúc nói chuyện hay" = Evaluative dominant → "tiếc quá"
    → Reward-Signal-Architecture ratio determines nhớ "ấm áp" (Direct-State) vs nhớ "hào hứng" (Evaluative)
    
  "TRỐNG / MẤT MÁT" = Entity-Compiled fire → no response → Chunk-Miss
    → Entity absent → routine fire into void → pain
    → PFC label: "trống" hoặc "nhớ"
    
  "KHÔNG CẢM THẤY GÌ" = Valence-Structural habituated → below PFC threshold
    → Valence-Structural VẪN CÓ nhưng VTA habituated → invisible
    → PFC: "bình thường" = ĐÚNG observation → SAI conclusion
    → ≠ "hết thương" → = "PFC không observe"
    → Tầng Hardware + Tonic = MOST likely to be "invisible"
    
  "CHÁN" = Generative dies + Tonic habituated (§6.1)
    → Generative channels: Valence-Momentary ≈ 0 (no new gap-fill)
    → Tonic channels: VTA habituated → invisible
    → PFC: "chán" = NO visible positive signal
    → KHÁC "ghét": chán = ABSENCE of reward, ghét = PRESENCE of threat
    → "Chán" NGUY HIỂM HƠN (silent — Tonic invisible, Generative dead)
    → "Ghét" NHÌN THẤY (có thể address trực tiếp)
    
  🟡 Verbalization × Reward-Signal-Architecture Evaluative:Direct-State ratio + satiation type visibility = framework synthesis
  🟢 Vietnamese mixed emotion: Fang et al. 2025, Miyamoto et al. 2010
```

---

## §11 — EXTREME VALENCE: LOVE/HATE + DISORGANIZED

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §13 + Valence-Propagation v3.0 §12.

```
⭐ LOVE/HATE SHARED CIRCUITS, DIFFERENT PFC:

  🟢 Zeki & Romaya 2008 (PLoS ONE):
    SHARED: putamen + insula (cả love VÀ hate)
    DIFFERENCE:
      LOVE: LARGE parts of judgment cortex DEACTIVATE
        → Lover = LESS CRITICAL → "mù quáng vì yêu"
      HATE: only SMALL zone deactivate
        → Hater RETAINS judgment → "tính toán trả thù"

  FRAMEWORK MAPPING:
    Entity-Compiled positive → PFC partially deactivate → less critical → accept
    Entity-Compiled negative → PFC ACTIVE → strategic Self-Pattern-Modeling → calculate
    Entity-Compiled mixed → PFC OSCILLATE → "vừa giận vừa thương"

    → |Valence| CAO (love OR hate) → body engage DEEP
    → |Valence| THẤP (indifference) → body DISENGAGE
    → Love → Hate: EASY (flip direction, keep Entity-Compiled depth) → betrayal
    → Hate → Love: HARD (negativity bias + need sustained positive)
    → Indifference → either: HARDER (need to BUILD depth first)
    → = Hate CLOSER to love than indifference is

  DISORGANIZED ATTACHMENT (Main & Hesse 1990):
    🟢 "FRIGHT WITHOUT SOLUTION":
       Attachment figure = source of COMFORT AND source of FEAR
       → Brain CANNOT resolve: approach (need comfort) vs avoid (fear)
       → = Behavioral strategy COLLAPSE
    🟢 30-year longitudinal: disorganized → LARGER amygdala in adulthood

    FRAMEWORK MAPPING:
      Normal mixed: approach DOMINANT, occasional avoidance → manageable
      Disorganized: approach ≈ avoidance → system STUCK
      → PFC OVERLOADED (must simultaneously approach AND avoid)
      → Connection §3.3: Mixed valence = Compiled conflict + Fresh multiple plans → Cost TĂNG
      → QUALITATIVELY different from normal mixed (not just degree)

      HARDWARE × Self-Pattern-Modeling CONFLICT:
        Tầng A (hardware): attachment DRIVE → approach (Bowlby — automatic)
        Tầng B (Self-Pattern-Modeling): threat-compiled → avoidance (learned)
        → 2-tầng CONFLICT = WORSE than single-tầng mixed
        → Hardware says "approach" + Self-Pattern-Modeling says "avoid" = body CANNOT resolve
        → Normal mixed: same tầng → PFC can arbitrate
        → Disorganized: cross-tầng → PFC arbitration INSUFFICIENT

  🟢 Love/hate circuits: Zeki & Romaya 2008
  🟢 Disorganized attachment: Main & Hesse 1990
  🟢 30-year longitudinal: disorganized → larger amygdala
  🟡 Disorganized as 2-tầng conflict (hardware vs Self-Pattern-Modeling) = framework synthesis
```

---

## §12 — PHANTOM RESONANCE × GRIEF

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §15 + Valence-Propagation v3.0 §12.

```
⭐⭐ PHANTOM RESONANCE 4-FACTOR MODEL (Resonance-Per-Entity v1.1 §15):

  MECHANISM:
    Entity compiled across channels → presence = BASELINE
    Entity lost → compiled patterns FIRE on triggers → predicted response = X
    → Actual response = NOTHING → prediction-delta NEGATIVE → body-feedback = pain
    → = "Phantom limb" of relationship (Ratcliffe 2018)
    → Patterns KEEP FIRING until Hebbian weaken → SLOW without deliberate uncompile

  PHANTOM DEPTH = f(4 factors):
    ① Compilation depth: more channels compiled → more phantom firing points
    ② Hardware-subsidy: hardware-supported bond → hardware KEEPS firing after loss
    ③ Valence-Structural: entity = body-base extension → loss = body-base AMPUTATION
    ④ Duration compiled: longer relationship → deeper Hebbian → slower fade

  PHANTOM × SATIATION TYPE:
    Tonic channels: MOST persistent phantom (compiled deep → fire continuously)
      → "Nhớ cảm giác ấm mà không ai cho" = Tonic phantom
      → Hardest to resolve: baseline violation ONGOING
    Cyclic channels: EPISODIC phantom (fire at cycle points only)
      → "Giờ ăn tối → nhớ mẹ nấu" = Cyclic phantom
      → Resolves FASTER: can redirect Cyclic to alternative source
    Generative channels: MINIMAL phantom (novelty-dependent → no entity = no fire)

  PER-ENTITY PHANTOM INTENSITY:

  ┌────────────────────────┬──────────┬──────────┬──────────┬──────────┬───────────┐
  │ Factor                 │ Mẹ mất   │ Con mất  │ Bạn mất  │ Partner  │ Colleague │
  │                        │ (con→mẹ) │ (mẹ→con) │ thân mất │ mất      │ mất       │
  ├────────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ① Compilation          │ DEEP     │ VERY DEEP│ MODERATE │ DEEP     │ SHALLOW   │
  ├────────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ② Hardware-subsidy     │ MODERATE │ MAXIMUM  │ NONE     │ SOME     │ NONE      │
  ├────────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ③ Valence-Structural   │ STRONG   │ VERY     │ MODERATE │ STRONG   │ WEAK      │
  │                        │          │ STRONG   │ to WEAK  │ to VERY  │           │
  ├────────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ④ Duration             │ DECADES  │ YEARS→   │ YEARS    │ YEARS→   │ MONTHS→   │
  │                        │          │ DECADES  │          │ DECADES  │ YEARS     │
  ├────────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ Dominant phantom       │ TONIC    │ TONIC+   │GENERATIVE│ MIXED    │ GENERATIVE│
  │ satiation type         │          │ CYCLIC   │          │ (all 3)  │           │
  ├────────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ PHANTOM INTENSITY      │ MAJOR    │DEVASTATING│ MINOR-  │ COMPLEX  │ MINOR     │
  │                        │          │          │ MODERATE │          │           │
  └────────────────────────┴──────────┴──────────┴──────────┴──────────┴───────────┘

  ⭐ MẸ MẤT CON = MOST DEVASTATING:
    ALL 4 factors MAX → TONIC + CYCLIC phantom compound
    → Sanders 1980: parental grief = most severe category
    → Some parents: phantom NEVER fully resolves → "chronic grief"

  🟢 Grief = phantom limb: Ratcliffe 2018. Parental grief: Sanders 1980.
  🟢 Rejected lovers cocaine circuits: Fisher 2010.
  🟡 Phantom × satiation type + 4-factor model = framework synthesis
```

---

## §13 — TECHNOLOGY × VALENCE FRONTIER

> Nguồn: Drill-Entity-Valence-Dynamics v2.0 §16+§17.

```
⭐⭐ TECHNOLOGY THAY ĐỔI VALENCE DYNAMICS THẾ NÀO:

  SENSORY VALENCE TRIGGERS = LESS RELEVANT (technology filled):
    → Hunger: delivery apps → fill without entity → sensory Cyclic valence ↓
    → Temperature: air conditioning, heating → self-fill → comfort Cyclic valence ↓
    → Entertainment: Netflix, games → fill novelty → Generative partially filled
    → = Sensory valence no longer REQUIRES entities (technology substitute)
    
  MODERN VALENCE FRONTIER = SOCIAL + ABSTRACT:
    Technology CHƯA fill:
      → Touch/comfort: CT afferents require PHYSICAL presence → Tonic Direct-State unfilled
      → Emotional regulation: Valence-Structural requires compiled entity → no substitute
      → Generative mutual: shared discovery requires 2 genuine drives → no one-way fill
      → Social validation: requires REAL social comparison → no synthetic
      → Meaning-in-relationship: entity-specific, cannot be mass-produced
    → "Có tiền mua mọi thứ nhưng vẫn cô đơn" = sensory filled, social unfilled

  SOCIAL MEDIA × VALENCE DYNAMICS:
    Context-Trigger AMPLIFICATION:
      → More triggers per day (algorithmic, curated)
      → "On this day" = ALGORITHMIC nostalgia scheduling
      → Friend posts = SYSTEMATIC narrative triggers
      → = Firing-Context-Trigger firing FREQUENCY increased dramatically
    Parasocial valence:
      → Compiled positive BUT no Valence-Structural → shallow
      → Time on parasocial → LESS time for genuine → valence DECLINE
    
  AI × VALENCE:
    AI can: trigger EXISTING Valence-Structural (write about mẹ → Entity-Compiled fire → feel)
    AI can: fill Generative gaps (insight, analysis, conversation)
    AI cannot: create Valence-Structural (no mutual, no body, no by-product from AI gap)
    AI cannot: fill Tonic (no physical presence, no CT afferents)
    → AI fills SOME valence triggers but creates NO new valence depth
    → Risk: AI sufficient for Generative → human Generative narrows

  ENGINE/ROAD/VEHICLE × VALENCE PORTFOLIO (Gap-Body-Need v2.0 §8):
    Pre-modern: less specialized → 1 entity fills MANY gap types → FEW entities, BROAD
    Modern: more specialized → entities SEGMENTED by function → MORE entities, THINNER
    
    ⭐ SPECIALIZATION TRADE-OFF:
      → More entities → portfolio DIVERSIFIED → MORE RESILIENT to loss
      → NHƯNG: if 1 entity carries DISPROPORTIONATE valence:
        "Vợ là tất cả" = ALL channels → 1 entity → FRAGILE
      → DIVERSIFIED portfolio = MORE RESILIENT
      → Mẹ (Tonic) + partner (Tonic+Generative) + friends (Generative) + colleagues (domain)
      → = Each entity fills DIFFERENT satiation type → loss of 1 ≠ loss of ALL
    
    ROAD × VALENCE ACCESS:
      → Urban: many potential entities → more portfolio options
      → Immigration: ROAD changes → most entities lost → massive valence disruption
      → Retirement: colleague entities lost → portfolio SHRINKS → gap opens
    
  🟡 Technology × valence frontier + specialization portfolio = framework synthesis
  🟢 Kahneman & Deaton 2010: $75K plateau (sensory saturation evidence)
  🟢 Durkheim 1893: organic solidarity — specialized units NEED each other
```

---

## §14 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (~25 claims)
═══════════════════════════════════════

  Entity-Compiled:
    Grief as body-level pain: Eisenberger 2003
    Attachment bond: Bowlby 1969
    Empathy fatigue: Figley 2002
    Adolescent ambivalence: established developmental psychology
    Parent-child ambivalence 50%: Lüscher & Pillemer 1998

  Valence dynamics:
    VTA habituation: Schultz 1997
    Chunk-Miss + basal ganglia: O'Connor 2023
    Bowlby 3 phases: Bowlby 1969
    Olfactory-amygdala: Herz 2004
    Evaluative Space Model: Cacioppo & Berntson 1994
    2-level bittersweet: Vaccaro, Kaplan & Damasio 2020
    Co-activation: Larsen, McGraw & Cacioppo 2001
    Ambivalent ≠ neutral: Schneider et al. 2021
    Nostalgia self-regulation: Sedikides & Wildschut 2018
    Video-call homesickness: van Tilburg et al. 2019
    Highly Sensitive Person: Aron & Aron 1997. Plasticity: Belsky & Pluess 2009
    Love/hate circuits: Zeki & Romaya 2008
    Disorganized attachment: Main & Hesse 1990
    Leaving home → better: Whiteman 2011, Arnett 2004
    Hardware-subsidy: Feldman 2012, Fisher 2004, Panksepp 1998
    Hedonic adaptation: Bao & Lyubomirsky 2013
    Parental grief: Sanders 1980. Phantom: Ratcliffe 2018.
    Income plateau: Kahneman & Deaton 2010

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (~23 claims)
═══════════════════════════════════════

  §1: Structural vs Current valence + satiation type dimension
  §2: Entity-Compiled 3 subtypes, Entity-Compiled vs Obligation
  §3: Valence-Structural+A = invisible, Valence-Momentary+B = visible paradox
  §4: 3 Firing Modes taxonomy + hardware-subsidy modulation
  §4.1: 8-channel Valence-Structural visibility taxonomy (from drill)
  §5: Hardware-subsidy × habituation rate = unified model
  §6: Cyclic/Tonic/Generative × valence dynamics
  §6.1: "Chán" × satiation type decomposition (from drill)
  §7: Satiation type × mixed valence + verbalization mapping
  §8: "New appreciation" 3-mechanism model
  §9: Nostalgia as Valence-Structural Tonic self-regulation
  §10: Per-entity valence dynamics trajectory + Reward-Signal-Architecture Evaluative:Direct-State × feel
  §10.2: Verbalization × Reward-Signal-Architecture mapping (from drill)
  §11: Disorganized as 2-tầng conflict (hardware vs Self-Pattern-Modeling)
  §12: Phantom 4-factor model × satiation type
  §13: Technology × valence frontier
  §2.4.1: Embodied-Mirror → Gap-Predict = unified 2-step meta-process (drill synthesis)
  §2.4.1: Novelty tức thời vs Gap-Fillability tương lai = 2 mechanisms khác chiều thời gian
  §2.4.2: 3 firing patterns (Embodied-Mirror alone / Gap-Predict alone / Embodied-Mirror→Gap-Predict sequential)
  §2.4.3: 3 pain types + observable distinction (hardware gap / Gap-Predict anticipatory / Embodied-Mirror)
  §2.4.3: Grief decomposition × 3 pain types + specialization portfolio

═══════════════════════════════════════
🔴 HYPOTHESIS (~3 claims)
═══════════════════════════════════════

  Social media habituation of nostalgia triggers
  Entity-Compiled subtypes: gradient hay threshold?
  Exact partial Entity-Compiled fire intensity formula


CÂU HỎI MỞ:
  → Social media → systematic Firing-Context-Trigger triggers: habituate or accumulate?
  → Disorganized: only attachment-specific or can generalize?
  → AI partial Valence-Structural trigger: long-term effect on genuine entity valence?
  → Cross-cultural variation in mixed valence tolerance → mechanism?
```

---

## §15 — CROSS-REFERENCES + CITATIONS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Valence-Propagation.md v4.1 — companion file (WHAT valence is + HOW propagates)
    → Body-Base.md v4.0 — L0+L1 substrate + observation parameters
    → Body-Feedback-Mechanism.md v2.1 — Body-Need aggregate, chunk dynamics
    → Schema.md v2.0 — schema = chunks + links + purpose
    → Chunk.md v2.2 — chunk substrate, context-tag, 4 connections
    → Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State × valence
    → Dissonance-Signal-Architecture.md v1.0 — Hardware-Subsidy bidirectional
    → Gap-Body-Need.md v2.0 — Cyclic/Tonic/Generative satiation types
    → Body-Feedback-Label.md v2.0 — vocabulary reference

  ENTITY-COMPILED + ACCESS + DYNAMICS:
    → Entity-Compiled.md v1.2 — deep mechanism (Hub-and-Spoke, Dunbar, grief, decay)
    → Entity-Access.md v1.3 — gradient Mức 0-5, 3-Factor Model, excess, calibration
    → Inter-Body-Mechanism.md v1.0 — §8 Entity-Compiled reframe, §4 3-cost, §5 By-Product Match
    → Body-Coupling.md v3.1 — coupling 2D model, 3 Phase, extension/entanglement
    → Connection.md v5.0 — 3 Generative Primitives, 2-luồng/2-tầng overview
    → Self-Pattern-Modeling.md v3.2 — Compiled/Fresh, Simulation-Engine application 1
    → Agent-Mechanism.md v2.0 — integration hub, Compilable Architecture
    → Resonance-Per-Entity.md v1.1 — hardware-subsidy per entity, Reward-Signal-Architecture Evaluative:Direct-State
    → Resonance-Sustainability.md v1.0 — 3 modalities, maintenance decline
    → Obligation.md v1.0 — compiled prediction (independent of Entity-Compiled)
    → Protect.md v1.0 — f(replaceability × attachment), loss aversion
    → Boredom.md v2.0 — dissonance + Imagine-Final mờ, source ⑥, Resonance Decline

  PFC + SIMULATION:
    → PFC-Operations.md v1.2 — Hold/Suppress, Compiled/Fresh, PFC budget
    → Simulation-Engine.md v1.2 — 1 engine, 3 components, 3 axes
    → Feeling.md v2.0 — PFC observation of body (7 layers)

  DRILL SOURCE:
    → backup/Drill-Inter-Body-Mechanism/Drill-Entity-Valence-Dynamics.md v2.0 — primary drill source
    → Drill-Agent-Feed-Channel v2.2 — §5 Embodied-Mirror→Gap-Predict 2-step meta-process (§2.4.1-§2.4.3)


RESEARCH CITATIONS:

  | # | Citation | Used in |
  |---|----------|---------|
  | R1 | Schultz 1997 — Dopamine prediction error / VTA | §1,§4,§5 |
  | R2 | Cacioppo & Berntson 1994 — Evaluative Space Model | §7 |
  | R3 | Vaccaro, Kaplan & Damasio 2020 — Bittersweet neuroscience | §7 |
  | R4 | Larsen, McGraw & Cacioppo 2001 — Can feel happy+sad | §7 |
  | R5 | Schneider et al. 2021 — Ambivalent ≠ neutral | §7 |
  | R6 | Lüscher & Pillemer 1998 — 50% parent-child ambivalence | §7,§10 |
  | R7 | Sedikides & Wildschut 2018 — Nostalgia self-regulation | §9 |
  | R8 | Oba et al. 2016 — Memory+reward coproduce nostalgia | §9 |
  | R9 | Van Tilburg et al. 2019 — Video-chat homesickness | §9 |
  | R10 | Hariri et al. 2002 — 5-HTTLPR amygdala reactivity | §10.1 |
  | R11 | Aron & Aron 1997 — Highly Sensitive Person 15-20% | §10.1 |
  | R12 | Belsky & Pluess 2009 — Plasticity model | §10.1 |
  | R13 | Zeki & Romaya 2008 — Love/hate shared circuits | §11 |
  | R14 | Main & Hesse 1990 — Disorganized attachment | §11 |
  | R15 | O'Connor 2023 — Basal ganglia grief firing | §4 |
  | R16 | Bowlby 1969 — Attachment 3 phases | §2,§4 |
  | R17 | Herz 2004 — Odor-evoked emotional memory | §4 |
  | R18 | Bao & Lyubomirsky 2013 — Hedonic adaptation | §5 |
  | R19 | Whiteman et al. 2011 — Parent-child over time | §8 |
  | R20 | Arnett 2004 — Emerging adulthood | §8 |
  | R21 | Fang et al. 2025 — Cross-cultural mixed emotions | §7,§10.2 |
  | R22 | Miyamoto et al. 2010 — Dialectical thinking ambivalence | §7,§10.2 |
  | R23 | Feldman 2012 — Biobehavioral synchrony | §5 |
  | R24 | Fisher 2004 — Limerence motivation drive | §5 |
  | R25 | Panksepp 1998 — μ-opioid social play | §5 |
  | R26 | Roberts & Dunbar 2011 — Kin resilient vs friends | §5 |
  | R27 | Sanders 1980 — Parental grief most severe | §12 |
  | R28 | Ratcliffe 2018 — Grief as phantom limb | §12 |
  | R29 | Fisher 2010 — Rejected lovers cocaine circuits | §12 |
  | R30 | Aron & Aron 1996 — Self-expansion model | §6.1 |
  | R31 | Gottman & Levenson 2000 — Type 2 divorce | §6.1 |
  | R32 | Kahneman & Deaton 2010 — Income-wellbeing plateau | §13 |
  | R33 | Durkheim 1893 — Organic solidarity | §13 |
  | R34 | Eisenberger 2003 — Social pain = physical pain | §2 |
  | R35 | Figley 2002 — Compassion fatigue | §3 |
  | R36 | Singer et al. 2004 — Empathy shared pain (ACC + anterior insula) | §2.4.1,§2.4.2,§2.4.3 |


STATUS:

  v1.0 — 2026-05-29 — Extracted from Valence-Propagation.md v3.0 §3-§13.
    + 3 Drill GAPs absorbed: §4.1 (8-channel), §6.1 ("chán" decomposition), §10.2 (verbalization).
    + Valence-Propagation §12 split: §11 (Love/Hate) + §12 (Phantom).
    Source: Drill-Entity-Valence-Dynamics v2.0 (28 insights, 33 citations).
  v1.1 — 2026-05-29 — L3 RETIRE: dep Body-Base v2.1→v3.3, L0-L1-L3→L0+L1 substrate.
    Companion Valence-Propagation v4.0→v4.1 updated.
  v1.2 — 2026-06-04 — §2.4 MECHANISM NOTE: "state = my state" = description,
    gap-fillability = mechanism. Level 1/2 distinction.
    Source: Drill-Body-Base-Boundary-Spectrum v1.2.
  v1.3 — 2026-06-05 — §2.4 ENRICH: Embodied-Mirror→Gap-Predict 2-step meta-process,
    3 firing patterns, 3 pain types, Novelty vs Gap-Fillability distinction.
    +§2.4.1 (2-step meta-process) +§2.4.2 (3 firing patterns) +§2.4.3 (3 pain types).
    +R36 Singer 2004. +5 🟡 framework syntheses.
    Source: Drill-Agent-Feed-Channel v2.2 §5.
```
