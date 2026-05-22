---
title: Valence-Propagation — Hệ Thống Đánh Giá Của Body + Cơ Chế Truyền Qua Schema Network
version: 3.0
created: 2026-04-18
rewritten: 2026-05-22 (v3.0 — FULL REWRITE: Drill-Entity-Valence-Dynamics v2.0 integration + Phase A framework files)
previous_versions:
  - v2.0 → backup/Valence-Propagation-v2.0-backup.md
  - v1.4 → backup/Valence-Propagation-v1.4-backup.md
status: v3.0 — REFERENCE FILE (kiến trúc tổng thể Valence system)
scope: |
  WHAT valence IS + HOW valence WORKS per-entity + HOW valence BEHAVES over time +
  HOW valence PROPAGATES qua schema chain + WHY PFC không biết + GIỚI HẠN nền tảng.
  v3.0 KEY CHANGES (from Drill-Entity-Valence-Dynamics v2.0, 28 insights):
    ① Structural valence (inside EC, slow) vs Current valence (outside EC, fast)
    ② 3 Firing Modes: Maintenance / Chunk-Miss / Context-Trigger
    ③ Hardware Subsidy = ANTI-HABITUATION: modulate VTA habituation per entity
    ④ Satiation type × valence: Cyclic (oscillation) / Tonic (invisible) / Generative (renewable)
    ⑤ RSA A:B ratio × valence "feel": B=warm, A=exciting
    ⑥ Per-entity valence dynamics mapping table
    ⑦ "Xa mẹ mới biết thương" = 3 cơ chế cộng dồn
    ⑧ Mixed valence = PARALLEL per-channel, MOST COMMON
    ⑨ Phantom resonance 4-factor model
    ⑩ Technology × valence frontier + ENGINE/ROAD/VEHICLE
  + Phase A integration: Entity-Compiled v1.0, Entity-Access v1.0,
    PFC-Operations v1.0, Simulation-Engine v1.0
  + §3 Entity-Compiled SLIM DOWN (deep mechanism → pointer → EC v1.0)
purpose: |
  Central reference file cho toàn bộ Valence system trong framework.
  3 trụ cột: WHAT valence is + HOW valence behaves per-entity + HOW valence propagates.
  Vai trò tương đương Feeling.md v2.0 và Chunk.md v2.0 cho hệ thống tương ứng.
dependencies:
  - Body-Base.md v2.1 — L0-L1-L3 channels mà valence đánh giá
  - Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, 2 sources, 3 dynamics
  - Entity-Compiled.md v1.0 — deep mechanism (Hub-and-Spoke, Dunbar, grief, decay)
  - Entity-Access.md v1.0 — gradient Mức 0-5, 3-Factor Model, excess, calibration
  - PFC-Operations.md v1.0 — Hold/Suppress, Compiled/Fresh spectrum, PFC budget
  - Simulation-Engine.md v1.0 — 1 engine, 3 components, 3 axes
  - Inter-Body-Mechanism.md v1.0 — Entity-Compiled §8, 3-cost §4, By-Product Match §5
  - Body-Coupling.md v1.1 — coupling mechanism deep-dive (extends §4)
  - Connection.md v3.3 — 3 Generative Primitives, §3.3 2-luồng overview
  - Self-Pattern-Modeling.md v3.1 — F1/F2, Simulation Engine application 1
  - Agent-Mechanism.md v2.0 — integration hub, Architecture B
  - Collective-Body.md v1.2 — Model 3 cấp (Clarification reference)
  - Schema.md v2.0 — schema = chunks + links + purpose
  - Chunk.md v2.2 — chunk substrate, context-tag, 4 connection types
  - Anchor-Schema.md v1.2 — anchor amplify propagation, trust binding
  - Feeling.md v2.0 — PFC observation of body-feedback (khác tầng)
  - Reward-Signal-Architecture.md v1.0 — Type A/B × valence
  - Gap-Body-Need.md v2.0 — Cyclic/Tonic/Generative satiation types
  - Resonance-Entity.md v2.0 — hardware subsidy, RSA A:B per entity
  - Resonance-Sustainability.md v1.0 — 3 modalities, silence, maintenance decline
  - Obligation.md v1.0 — compiled prediction (independent of Entity-Compiled)
  - Protect.md v1.0 — f(replaceability × attachment depth)
  - Boredom.md v2.0 — dissonance + Imagine-Final mờ, source ⑥, M1-M4
  - Body-Feedback-Label.md v2.0 — vocabulary reference
sources:
  - Drill-Entity-Valence-Dynamics v2.0 (1,436L, 28 insights, 33 citations)
  - Valence-Propagation v2.0 (1,872L) — previous version content kept/refined
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Valence-Propagation — Hệ Thống Đánh Giá Của Body + Cơ Chế Truyền Qua Schema Network

> **Cái dao từng cắt tay bạn. Bạn SỢ nó.**
> **Cùng cái dao đó, bạn học cách dùng. Bạn THÍCH nó.**
> **Cùng cái dao đó, trong tay kẻ thù. Bạn SỢ nó LẠI.**
>
> Cùng 1 entity — valence THAY ĐỔI tùy experience và context.
> Đó là valence PER-ENTITY — cách body đánh giá 1 thứ cụ thể.
>
> Nhưng có thứ PHỨC TẠP hơn nhiều:
>
> **Ở với mẹ 20 năm. PFC bạn nói: "bình thường, không gì đặc biệt."**
> **L2 compiled: ôm, nấu ăn, dạy bài, hy sinh — 20 năm TÍCH LŨY.**
> **VTA habituated. Hardware subsidy counter. Tonic baseline INVISIBLE.**
> **PFC KHÔNG BIẾT baseline này tồn tại — cho đến khi MẤT.**
>
> **Xa mẹ. Đọc thơ. Bỗng KHÓC.**
> **3 cơ chế cộng dồn: decay asymmetry + contrast + articulation.**
> **20 năm body BIẾT. PFC mới observe LẦN ĐẦU.**
>
> File này: Valence LÀ GÌ, cấu trúc per-entity, Structural vs Current,
> cách valence BEHAVES over time (3 firing modes, hardware subsidy, satiation type),
> cách valence TRUYỀN qua schema chain,
> TẠI SAO PFC không biết, và GIỚI HẠN nền tảng.

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — VALENCE LÀ GÌ
- §2 — VALENCE PROFILE: Cấu Trúc Per-Entity
- §3 — STRUCTURAL VALENCE vs CURRENT VALENCE
- §4 — ENTITY-COMPILED: Body-Base Extension
- §5 — 2-LUỒNG + 2-TẦNG × VALENCE VISIBILITY
- §6 — 3 FIRING MODES
- §7 — VTA HABITUATION × HARDWARE SUBSIDY
- §8 — VALENCE × SATIATION TYPE
- §9 — MIXED VALENCE: PARALLEL PER-CHANNEL
- §10 — "XA MẸ MỚI BIẾT THƯƠNG" — 3 CƠ CHẾ CỘNG DỒN
- §11 — PER-ENTITY VALENCE DYNAMICS + RSA A:B
- §12 — PHANTOM RESONANCE × GRIEF
- §13 — TECHNOLOGY × VALENCE FRONTIER
- §14 — CÁCH VALENCE HÌNH THÀNH + UPDATE
- §15 — VALENCE PROPAGATION QUA SCHEMA CHAIN
- §16 — CHAIN PROPERTIES + WHY CHAIN DÀI TỒN TẠI
- §17 — CASES PHÂN TÍCH
- §18 — PFC BLINDNESS + 3 NGUYÊN TẮC
- §19 — HONEST ASSESSMENT
- §20 — CROSS-REFERENCES + CITATIONS

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 VALENCE TRONG KIẾN TRÚC FRAMEWORK:

  VALENCE = CÁCH BODY ĐÁNH GIÁ MỌI THỨ.

  Trước khi hành động, body phải ĐÁNH GIÁ:
    "Entity này ảnh hưởng body channels CỦA TÔI thế nào?"
    "Positive? Negative? Mixed? Qua channel nào?"
  Kết quả đánh giá = VALENCE.

  Valence THUỘC VỀ Body-Base vì:
    → Body là NƠI đánh giá xảy ra (amygdala, insula, body signals)
    → Body channels (L0-L1-L3) là THƯỚC ĐO đánh giá
    → Valence = body's ASSESSMENT, không phải PFC's judgment
    → PFC có thể OBSERVE valence (thành feeling), nhưng KHÔNG tạo ra nó
    → = Feeling.md v2.0: "Feeling = PFC observation of body"
    → = Valence = WHAT body computes. Feeling = WHAT PFC sees.

  VALENCE × BODY-NEED (BFM v2.0 §1):
    Body-Need = aggregate OUTPUT của chunk dynamics (BFM v2.0).
    Valence = body's ASSESSMENT per-entity → feeds INTO body-need.
    Entity có valence positive → body-need shift toward approach.
    Entity có valence negative → body-need shift toward avoid.
    Tổng hợp valences across entities + body state = body-need hiện tại.


  FILE NÀY TRONG FLOW:

    Body-Base.md (L0-L3 channels — NỀN TẢNG)
         │
         ▼
    Body-Feedback-Mechanism.md v2.0 (Body-Need aggregate, chunk dynamics)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ VALENCE-PROPAGATION.MD v3.0 (FILE NÀY)                     │
    │                                                              │
    │  TRỤ 1: VALENCE LÀ GÌ (§1-§4)                              │
    │    Per-entity valence → valence profile → Structural/Current │
    │    Entity-Compiled → body-base extension                     │
    │                                                              │
    │  TRỤ 2: VALENCE BEHAVES OVER TIME (§5-§13)          ← v3.0 │
    │    2-luồng/2-tầng → 3 Firing Modes → Hardware Subsidy       │
    │    Satiation type → Mixed valence → "Xa mẹ mới biết thương" │
    │    Per-entity dynamics → Phantom resonance → Technology      │
    │                                                              │
    │  TRỤ 3: VALENCE PROPAGATION (§14-§18)                       │
    │    4 cơ chế propagation → Chain properties → Cases           │
    │    PFC Blindness → 3 Nguyên tắc                              │
    └─────────────────────────────────────────────────────────────┘
         │
         ▼
    Drive.md (TỔNG HỢP valences → action)
    Feeling.md v2.0 (PFC OBSERVE valence → feeling)
    Emergent-Patterns.md (valence TÍCH LŨY → patterns emerge)
    Anchor-Schema.md (anchor AMPLIFY propagation)


  PHÂN BIỆT 4 CONCEPTS GẦN NHAU:

    VALENCE (file NÀY):
      "Entity X ảnh hưởng body channels CỦA TÔI thế nào?"
      = ĐÁNH GIÁ — cả per-entity lẫn qua schema chain
      Input: entity + body-base state + context + compiled schemas
      Output: valence profile + propagated valence qua network

    DRIVE (Drive.md):
      "NHIỀU drives đang active → não CHỌN hành động NÀO?"
      = TỔNG HỢP nhiều drives → action emerge
      Input: tất cả valences + body-needs + context
      Output: action cụ thể

    FEELING (Feeling.md v2.0):
      "PFC THẤY GÌ khi observe body-chunk interaction?"
      = PFC OBSERVATION — valence qua lens PFC
      Input: body signals + chunk activation
      Output: conscious experience (7 layers, 20-100% fidelity)

    BODY SIGNALS (Body-Dissonance.md):
      "Body PHẢN HỒI: đủ chưa? Hay chưa? Tiếp không?"
      = FEEDBACK sau action
      3 signals: Satisfaction, Reward, Dissonance

    Flow: Valence → Drive → Action → Body Signals → Update Valence → Loop


  v3.0 CHANGELOG:
    v2.0 → v3.0: +TRỤ 2 (§5-§13) từ Drill-Entity-Valence-Dynamics v2.0 (28 insights).
    §4 Entity-Compiled SLIM DOWN (deep mechanism → pointer → EC v1.0 + EA v1.0).
    §8+§9 v2.0 → §18 (merge PFC Blindness + 3 Nguyên tắc).
    + Phase A integration (PFC-Operations, Simulation-Engine, Entity-Compiled, Entity-Access).
    + Dependencies updated: SPM v3.1, Boredom v2.0, Gap-Body-Need v2.0, Resonance-Entity v2.0.
```

---

## §1 — VALENCE LÀ GÌ

```
🟡 ĐỊNH NGHĨA:

  Valence = ĐÁNH GIÁ CỦA BODY về cách 1 entity ảnh hưởng body channels.

  "Entity" = bất kỳ thứ gì body gặp trong domain:
    → Object: dao, ghế, xe, sách, bom, gai, bật lửa...
    → Agent: mẹ, bạn, sếp, chó, Thiên Chúa, Jensen Huang...
    → Abstract: toán, vật lý, từ thiện, tương lai, Thiên Đàng...
    → Action: giúp đỡ, kiện tụng, học bài, giết người...
    → State: giàu, nghèo, cô đơn, nổi tiếng...

  "Body channels" = hệ thống L0-L1-L3 (Body-Base.md):
    → L0 Alive: safe ←→ dangerous
    → L1 Body-inputs: useful ←→ harmful (nutrition, sleep, sex...)
    → L3 Pattern: novelty, mastery, status, protect


  ⭐ 4 ĐẶC TÍNH CỐT LÕI:

  ① MULTI-CHANNEL — KHÔNG PHẢI 1 TRỤC TỐT/XẤU:

    SAI: "Mẹ = tốt" hoặc "Mẹ = xấu" (1 trục)
    ĐÚNG: Mẹ = {
      L1 nutrition: ++ (cho ăn)
      L1 comfort: ++ (ôm, vỗ về)
      L1 autonomy: -- (ép học, cấm chơi)
      L3 mastery: + (dạy bài)
      L3 novelty: - (bắt lặp lại bài khó)
    }
    = Valence KHÁC NHAU trên TỪNG CHANNEL
    = YÊU VÀ GHÉT CÙNG LÚC — không mâu thuẫn

    🟢 Mixed feelings (ambivalence): well-documented phenomenon
    🟢 Multi-dimensional emotion: không ai tranh cãi cảm xúc phức tạp

  ② DYNAMIC — THAY ĐỔI THEO THỜI GIAN:

    Dao lần đầu: { L0 safety: -- }
    Dao sau khi học: { L1 utility: ++, L0 safety: neutral }
    = CÙNG entity, KHÁC valence — vì experience thay đổi

  ③ CONTEXT-DEPENDENT:

    Quả bom trong tay tôi: { L0: ++, L1: ++ } (vũ khí, bảo vệ)
    Quả bom trong tay kẻ thù: { L0: --, L1: -- } (threat)
    = CÙNG entity, CÙNG thời điểm, KHÁC CONTEXT → khác valence

  ④ STORED IN SCHEMA:

    Valence profile được compiled vào schema qua experience
    → Gặp lại entity → schema load valence → body respond NGAY
    → Không cần re-evaluate từ đầu mỗi lần
    → = Tại sao thấy con chó từng cắn → SỢ NGAY (compiled valence)
    → = Schema.md §1: "Schema = PATTERN dao động neuron đã ổn định"
    → Valence = 1 DIMENSION của schema (cùng với motor, visual, somatic...)

    ⚠️ NO SOURCE TAG (Drill §10 — GAP 8):
    → Valence stored KHÔNG kèm field "nguồn gốc" (internal hay external?)
    → Wire = wire. Body treat BÌNH ĐẲNG bất kể compiled từ đâu.
    → PFC CŨNG không phân biệt (§18 confabulation)
    → "Tôi thật sự muốn X hay xã hội nạp?" = câu hỏi VÔ NGHĨA ở body level
    → "Tôi" = TỔNG HỢP internal + external compiled patterns
    → 🟢 Nisbett & Wilson 1977: PFC cannot access actual processing

    🟢 Fear conditioning: rapid, one-trial learning (LeDoux 1996)
    🟢 Evaluative conditioning: valence transfer qua association (De Houwer 2007)
```

---

## §2 — VALENCE PROFILE: Cấu Trúc Per-Entity

```
🟡 MỖI ENTITY TRONG DOMAIN CÓ 1 VALENCE PROFILE LƯU TRONG SCHEMA:

  ┌─────────────────────────────────────────────────────────────┐
  │ VALENCE PROFILE: Entity X                                    │
  │                                                              │
  │ BODY-BASE CHANNELS:                                          │
  │   L0 Alive:     safe ←───────→ dangerous                    │
  │   L1 Body-inputs:                                            │
  │     Nutrition:   useful ←─────→ harmful                      │
  │     Comfort:     pleasant ←───→ unpleasant                   │
  │     Sleep:       promoting ←──→ disrupting                   │
  │     Autonomy:    enabling ←───→ constraining                 │
  │   L3 Pattern:                                                │
  │     Novelty:     interesting ←→ boring                       │
  │     Mastery:     enabling ←───→ blocking                     │
  │     Status:      elevating ←──→ diminishing                  │
  │     Protect:     safe ←───────→ threatening (my resources)   │
  │                                                              │
  │ META-DIMENSIONS:                                             │
  │   Trust:           high ←─────→ low                          │
  │   Predictability:  high ←─────→ low                          │
  │   Replaceability:  easy ←─────→ hard                         │
  │   Dependency:      none ←─────→ critical                     │
  │                                                              │
  │ NET: tổng hợp across channels → approach / avoid / mixed     │
  └─────────────────────────────────────────────────────────────┘


  ĐẶC ĐIỂM PROFILE:

    ① Mỗi channel có valence RIÊNG — không average
      Mẹ: L1++ nhưng autonomy-- = KHÔNG phải "hơi positive"
      = Positive ở channels này, Negative ở channels kia, CÙNG LÚC

    ② Không phải mọi channel đều có valence cho mọi entity
      Dao: L0, L1 rõ ràng. L3 status? Gần zero. Novelty? Chỉ lần đầu.
      = Valence profile SPARSE cho objects, DENSE cho agents

    ③ Intensity KHÁC NHAU
      Dao cắt tay: L0 safety -2 (nhẹ)
      Hổ đuổi: L0 safety -10 (cực mạnh)
      = Cùng channel, cùng hướng, khác CƯỜNG ĐỘ

    ④ Meta-dimensions MODULATE body-base channels
      Trust cao → valence AMPLIFIED (tin người bạn thân → valence mạnh hơn)
      Trust thấp → valence DAMPENED (không tin người lạ → valence yếu)
      Replaceability dễ → mất entity ÍT impact
      Replaceability khó → mất entity IMPACT LỚN (grief)


  OBJECT VALENCE vs AGENT VALENCE:

  ┌─────────────────────┬──────────────────────────────────────────┐
  │ OBJECT VALENCE      │ AGENT VALENCE                             │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ Ít channels active   │ NHIỀU channels active                    │
  │ Dao: L0, L1          │ Mẹ: L0, L1, L3, trust, dependency      │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ Tương đối ỔN ĐỊNH   │ DYNAMIC — thay đổi liên tục              │
  │ Dao vẫn là dao       │ Mẹ vui sáng, cáu chiều                  │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ONE-WAY              │ BIDIRECTIONAL                             │
  │ Tôi đánh giá dao     │ Tôi đánh giá mẹ VÀ mẹ đánh giá tôi    │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ DỄ thay thế          │ KHÓ thay thế                             │
  │ Dao khác cũng cắt    │ Mẹ khác KHÔNG phải mẹ mình              │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ PREDICTABLE          │ UNPREDICTABLE                             │
  │ Valence ít bất ngờ   │ Valence có thể FLIP bất ngờ              │
  └─────────────────────┴──────────────────────────────────────────┘

  → Agent valence PHỨC TẠP hơn object vì 5 đặc điểm trên.
  → Agent valence CÓ dimension mà object KHÔNG BAO GIỜ có:
    BODY-BASE EXTENSION → §4 Entity-Compiled.


  ABSTRACT ENTITY VALENCE:

    Ngoài Object và Agent, còn có abstract entities:
      Toán, vật lý, từ thiện, Thiên Đàng, "tương lai tốt đẹp"...
    
    Abstract entity valence ĐẶC BIỆT vì:
      → Không có physical form → KHÔNG có L0 direct
      → Valence HOÀN TOÀN qua schema link (§15 Propagation)
      → Có thể UNFALSIFIABLE (Thiên Đàng, "ý nghĩa cuộc đời")
      → → Không bao giờ nhận negative feedback → valence KHÔNG BAO GIỜ bị revise
      → → = "Thiết kế" valence ổn định nhất có thể
      → = Agent-Mechanism.md §10: Mode 2 schema override cho abstract agents

    🟡 Abstract entity valence = framework concept
    🟢 Unfalsifiable belief resilience = Popper + Festinger 1957 (cognitive dissonance)
```

---

## §3 — STRUCTURAL VALENCE vs CURRENT VALENCE

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §1.

```
⭐⭐ 2 LOẠI VALENCE — KHÁC VỊ TRÍ, KHÁC TỐC ĐỘ, KHÁC SATIATION TYPE:

  STRUCTURAL VALENCE (INSIDE Entity-Compiled):
    = Aggregate of per-channel valence tags CỦA tất cả compiled chunks
    = Mỗi chunk có tag: approach / avoidance / neutral (compile-time lock)
    = Structural valence = SUM of all tags = valence PROFILE
    = CHẬM thay đổi (cần compile/decompile chunks = months/years)
    = 3 subtypes (§4.1): positive-dominant / negative-dominant / MIXED
    
    STRUCTURAL VALENCE CÓ SATIATION PROFILE (v3.0):
      Mỗi channel CÓ satiation type riêng (Gap-Body-Need v2.0 §2):
      → Cyclic channels: approach/avoidance tags OSCILLATE (hunger → fill → off → return)
      → Tonic channels: approach tags STABLE baseline (comfort, safety → slow build, slow fade)
      → Generative channels: approach tags RENEWABLE (curiosity → fill → new gap → repeat)
      → Structural valence = aggregate across ALL satiation types
      → Most deep entities = Tonic + Generative compound (§8)
    
    VD — Mẹ (structural valence profile):
      Channel [nấu ăn]: approach (+) — Cyclic (fill → return → fill)
      Channel [ôm]: approach (++) — Tonic (ongoing baseline)
      Channel [la mắng]: avoidance (--) — Cyclic (episode → fade)
      Channel [hy sinh]: complex (+/schema) — Tonic (persistent)
      Channel [dạy kỹ năng]: approach (+) — Generative (each lesson → new gap)
      = Structural valence = POSITIVE-DOMINANT, Tonic-base + Generative-bursts
      
  CURRENT VALENCE (OUTSIDE Entity-Compiled, per-moment):
    = L1 (SPM momentary) + activated L2 channels AT THIS MOMENT
    = Thay đổi PER SECOND (context-dependent)
    = What PFC observes → what person VERBALIZES
    
    CURRENT VALENCE "FEEL" = f(RSA A:B ratio) (RSA v2.0 §1):
      Type B dominant → "ấm áp, dễ chịu" (opioid, CT afferents)
      Type A dominant → "hào hứng, thú vị" (evaluative, dopamine-adjacent)
      → Mẹ ôm con: current = Type B dominant → "ấm"
      → Bạn kể chuyện hay: current = Type A dominant → "thú vị"
      → CÙNG positive valence, KHÁC "feel" vì KHÁC A:B ratio
    
    VD — Mẹ đang la:
      L1 = NEGATIVE (SPM simulate mẹ angry → body distress)
      L2 [la mắng] channel = ACTIVE (avoidance, Cyclic)
      L2 [ôm, nấu ăn] channels = DORMANT (not triggered)
      Current valence = NEGATIVE
      PFC label: "ghét mẹ" (lúc này)
      
    VD — Đọc thơ về mẹ (xa mẹ):
      L1 = POSITIVE (poem → SPM fire → body warm)
      L2 [hy sinh, ôm, nấu ăn] channels = ACTIVE (triggered by poem)
      L2 [la mắng] channels = DORMANT (not in poem context)
      Current valence = INTENSE POSITIVE (Type B dominant → "thương")
      
  ⭐ STRUCTURAL ≠ CURRENT:
    Structural = what's STORED (slow, aggregate across satiation types)
    Current = what's ACTIVATED (fast, context-dependent, RSA A:B ratio determines "feel")
    Cùng entity, cùng structural valence → KHÁC current valence tùy moment
    → "Ghét mẹ" (lúc bị la) vs "Thương mẹ" (lúc đọc thơ)
    → CÙNG structural (mixed) → KHÁC current (context activates different channels)
    
  🟡 Structural vs Current distinction + satiation type dimension = framework synthesis (v3.0)
  🟢 Per-channel valence: §2 (explicit "KHÔNG average")
  🟢 RSA A:B: Reward-Signal-Architecture v2.0 §1
```

---

## §4 — ENTITY-COMPILED: Body-Base Extension

> **v3.0 SLIM DOWN**: Entity-Compiled.md v1.0 + Entity-Access.md v1.0 đã tồn tại.
> §4 giữ CORE CONCEPTS + POINTER → 2 files cho deep mechanism + gradient.

```
⭐ KHI PER-AGENT VALENCE COMPILE ĐỦ SÂU → BƯỚC NHẢY CHẤT:

  AGENT VALENCE CÓ DIMENSION MÀ OBJECT KHÔNG BAO GIỜ CÓ:

    Khi per-agent valence STRONG + compiled SÂU qua nhiều interaction:
      → Body KHÔNG CHỈ đánh giá "agent X ảnh hưởng tôi thế nào?"
      → Body chuyển sang: "agent X's state = MY state"
      → = Agent TRỞ THÀNH phần mở rộng body-base CỦA TÔI
      → = STRUCTURAL, SUSTAINED — không phụ thuộc từng episode tương tác

    TẠI SAO CHỈ AGENT, KHÔNG BAO GIỜ OBJECT:
      Object KHÔNG fire SPM → không có L1 episodes tích lũy
      Object KHÔNG bidirectional → không có mutual reinforcement
      Object DỄ thay thế → trust/dependency không compile sâu đủ
      → Body-base extension = EMERGENT property CHỈ CÓ ở agent valence
      → Mất nhà = stress tài chính. Mất con = body-base amputation.
        2 loại loss KHÁC CĂN BẢN.

    🟢 Grief as body-level pain: Eisenberger 2003 (social pain = physical pain pathways)
    🟢 Attachment bond = body-level: Bowlby 1969
```

### §4.1 — 3 Subtypes (spectrum)

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

### §4.2 — Entity-Compiled vs Obligation = INDEPENDENT

```
⭐ 2 CƠ CHẾ KHÁC NHAU (Inter-Body-Mechanism.md §8.3):

  Entity-Compiled: "entity's state = MY state" (structural, automatic)
  Obligation:      "predict cost to MAINTAIN access" (prediction, PFC-mediated)

  CÓ THỂ ĐỘC LẬP:
    L2 HIGH + Obligation LOW:  bạn thân → vui tự động, không "nợ" gì
    L2 LOW + Obligation HIGH:  ân nhân xa lạ → không thân nhưng "phải trả"
    L2 HIGH + Obligation HIGH: bố mẹ → yêu thương + cảm thấy phải chăm sóc
    L2 LOW + Obligation LOW:   stranger → no drive either way

  Cross-ref: Obligation.md v1.0 §2-§4 chi tiết.
  🟡 L2 vs Obligation independence = framework synthesis.
```

### §4.3 — Deep Mechanism + Gradient → POINTER

```
⭐ FILE NÀY CHỈ ĐỊNH NGHĨA + KEY CONCEPTS.
  DEEP MECHANISM VÀ GRADIENT → 2 FILES RIÊNG:

  Entity-Compiled.md v1.0 (Agent-Mechanism/):
    = DEEP MECHANISM: neural reality, formation, capacity, dynamics, loss, decay
    → §1: 8 research streams hội tụ → Entity-Compiled = neural reality
    → §2: Hub-and-Spoke architecture + body simulation
    → §3: Formation timeline (40→200h) + acceleration + sleep
    → §4: Dunbar capacity ceiling + 3 resource limits
    → §5: "Hợp tính" (Pattern-Resonance Baseline) + meta-match
    → §7: Grief intensity model (A+B+C types)
    → §8: Love↔Hate shift (|valence| depth, direction switch)
    → §9: Decay 3-layer model (episodes fastest, schema slowest)

  Entity-Access.md v1.0 (Agent-Mechanism/):
    = GRADIENT MODEL: how access level changes, quality, excess, calibration
    → §1: 3-Factor Model (Engine Mode × Gap-Need × Access Confidence)
    → §2: Entity-Access Gradient Mức 0-5 (Tool → Excess)
    → §3: 4 Starting Modes × B-dominant destination
    → §6: Excess spectrum (Mức 5) — limerence, obsession
    → §8: Calibration architecture

  ⭐ ENTITY-OWNED = PFC LABEL (Entity-Access.md §2):
    Entity-Owned = PFC OBSERVATION at Mức 4-5, NOT mechanism.
    Mechanism = entity-access compilation (3-factor → baseline).
    Most entity-access = UNLABELED by PFC (fuzzy middle of gradient).
    = Binary "owned/not-owned" → REPLACED by gradient Mức 0-5.

  Framework readers: §4 NÀY (definition) → Entity-Compiled.md (mechanism)
                     → Entity-Access.md (gradient + dynamics).
```

---

## §5 — 2-LUỒNG + 2-TẦNG × VALENCE VISIBILITY

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §2.

```
⭐ TỪ VP v2.0 §3.4 + CONNECTION §3.3 + EMPATHY §8 + RESONANCE-ENTITY v2.0 §3:

  L1 — SPM-OWNED (momentary):
    Source: MỖI LẦN SPM F1 fire on entity
    Duration: per-episode, TRANSIENT
    Valence: + or - tùy current interaction
    Cost: SPM metabolic cost
    VD: "Mẹ cười → vui lây" (L1+), "mẹ la → khó chịu" (L1-)
    
  L2 — ENTITY-COMPILED (structural):
    Source: compiled valence depth (entity = body-base extension)
    Duration: SUSTAINED, persistent
    Valence: per-CHANNEL (can be + and - simultaneously)
    Cost: ≈ 0 (compiled = automatic)
    VD: "Con = part of me" (L2+), "Kẻ thù = threat to me" (L2-)

  2-TẦNG × VALENCE VISIBILITY (Connection v4.0 §3.2b):
  
    TẦNG A — HARDWARE-DRIVEN valence:
      Source: hormone, CT afferents, attachment circuits
      PFC visibility: LOW (automatic, below threshold khi stable)
      VD: oxytocin khi ôm con → warm → PFC "bình thường" (habituated)
      → Tầng A valence = INVISIBLE most of the time (hardware = default)
      → Becomes VISIBLE only through disruption (loss, absence)
      
    TẦNG B — SPM-DRIVEN valence:
      Source: SPM F1/F2 fire → prediction-delta → body-feedback
      PFC visibility: HIGH (PFC computes → PFC observes)
      VD: bạn kể insight mới → SPM evaluate → "thú vị!" (PFC label)
      → Tầng B valence = VISIBLE per episode (PFC is the source)
      → Habituates IF prediction complete (same insight = no delta)

  PER-ENTITY L1:L2 × TẦNG A:B PROPORTION (Resonance-Entity v2.0 §3-§8):

    ┌────────────────┬──────────────┬──────────────┬──────────────────────┐
    │ Entity         │ 2-luồng      │ 2-tầng       │ Valence visibility   │
    │                │ (L1:L2)      │ (A:B)        │ implication          │
    ├────────────────┼──────────────┼──────────────┼──────────────────────┤
    │ Mẹ→Con        │ L2 dominant  │ Tầng A dom.  │ INVISIBLE most time  │
    │                │ (structural) │ (hardware)   │ → visible on loss    │
    ├────────────────┼──────────────┼──────────────┼──────────────────────┤
    │ Con→Mẹ (child)│ L1→L2 shift  │ A+B balanced │ MIXED visibility     │
    │                │ (forming)    │              │ → shifts with age    │
    ├────────────────┼──────────────┼──────────────┼──────────────────────┤
    │ Bạn thân       │ L1 dominant  │ Tầng B dom.  │ VISIBLE per episode  │
    │                │ (momentary)  │ (SPM only)   │ → fades between      │
    ├────────────────┼──────────────┼──────────────┼──────────────────────┤
    │ Romantic post-L│ L1→L2        │ A→B shift    │ Limerence=visible    │
    │                │ (if compiled)│              │ → post-L=invisible   │
    ├────────────────┼──────────────┼──────────────┼──────────────────────┤
    │ Colleague      │ L1 only      │ Tầng B       │ VISIBLE only in      │
    │                │ (unless close)│ (SPM only)  │ Agent-mode moments   │
    └────────────────┴──────────────┴──────────────┴──────────────────────┘

  ⭐ KEY INSIGHT v3.0:
    L2 dominant + Tầng A dominant = MOST INVISIBLE valence (mẹ→con)
    L1 dominant + Tầng B dominant = MOST VISIBLE valence (bạn thân)
    → PARADOX: DEEPEST bond = LEAST VISIBLE valence
    → "Sống với mẹ 20 năm, không thấy gì" = L2+A → both invisible
    → "Gặp bạn mới, vui ghê" = L1+B → both visible
    → Explains "có mới nới cũ" illusion at mechanism level

  2 STREAMS CÓ THỂ CONFLICT (Connection §3.3):
  
    ┌──────────────────┬──────────┬──────────┬──────────────────────────┐
    │ Case             │ L1       │ L2       │ Result                   │
    ├──────────────────┼──────────┼──────────┼──────────────────────────┤
    │ Mẹ chăm con ốm  │ - (pain) │ + (ext.) │ L2 > L1 → VẪN CHĂM      │
    │ Bạn kể chuyện   │ + (joy)  │ + (ext.) │ COMPOUND reward          │
    │ Bác sĩ chăm lạ  │ - (pain) │ ≈ 0      │ L1 tích lũy → BURNOUT   │
    │ Con giận mẹ la   │ - (anger)│ mixed    │ "vừa giận vừa thương"   │
    │ Kẻ thù thua     │ + (rev.) │ + (safe) │ COMPOUND (Schadenfreude) │
    └──────────────────┴──────────┴──────────┴──────────────────────────┘
    
  BURNOUT FORMULA (Empathy §8):
    Burnout = f(L1 cost tích lũy / L2 compensation)
    L2 CAO + L1 vừa → KHÔNG burnout (mẹ chăm con)
    L2 ≈ 0 + L1 bất kỳ → BURNOUT (bác sĩ chăm stranger)
    L2 CAO + L1 CỰC CAO kéo dài → VẪN burnout (cha mẹ trẻ khuyết tật)
    
  🟢 L1/L2: VP v2.0 §3.4, Connection §3.3, Body-Coupling §1.3
  🟢 Burnout formula: Empathy §8, Figley 2002
  🟢 2-tầng: Connection v4.0 §3.2b
  🟡 L2+A = invisible, L1+B = visible paradox = framework synthesis (v3.0)
```

---

## §6 — 3 FIRING MODES

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §3.

```
⭐⭐ ENTITY-COMPILED VALENCE FIRE THEO 3 MODES:

  MODE 1 — MAINTENANCE (entity present, hàng ngày):
    Entity PRESENT → routine fire → L2 channels active → opioid LOW-LEVEL
    VTA HABITUATED → reward = BASELINE → PFC sees NOTHING special
    = "Background warmth" — có nhưng INVISIBLE
    = "Ở với mẹ 20 năm, không thấy gì đặc biệt"
    
    Hardware subsidy MODULATES Mode 1 (§7):
      HIGH subsidy (mẹ→con): opioid trickle MAINTAINED → baseline RICHER
        → Even habituated, body STILL gets anti-habituation signals
        → "Mẹ chán con" = pathological (hw subsidy SHOULD prevent)
      NONE subsidy (bạn): opioid trickle WITHOUT protection
        → VTA habituates FASTER → Mode 1 reward WEAKER
        → "Gặp bạn hàng ngày → bình thường" = no subsidy → fast habituation
      TEMPORARY subsidy (romantic limerence): SIMULATES rich Mode 1
        → Fades after 18-36m → Mode 1 reward DROPS → "hết lửa"
    
    Satiation type × Mode 1:
      Cyclic channels: Mode 1 = oscillating (on/off/on)
      Tonic channels: Mode 1 = continuous baseline (invisible)
      Generative channels: Mode 1 = only if novelty continues (else → habituate)
      
  MODE 2 — CHUNK-MISS (entity absent, cấp tính):
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
      → EC depth (deeper → more routines disrupted → slower calibration)
      → Hardware subsidy (HIGH → hw KEEPS firing → slower calibration)
      → Alternative gap-fill (other entities available → faster)
      → Hardware reactivity (HSP → more intense → slower)
      → Attachment style (anxious → slower, avoidant → suppress → "faster")
      → Satiation type (Tonic channels → slowest fade, Cyclic → fastest)
      
  MODE 3 — CONTEXT-TRIGGER (entity absent, tình cờ):
    External cue → match EC spoke → hub activate → L2 fire → body-feedback
    = UNPREDICTABLE (context-dependent)
    
    Triggers ranked by intensity:
      SENSORY DIRECT: thấy bà cụ giống mẹ → visual spoke → fire
      NARRATIVE: đọc bài Facebook về bố vất vả → linguistic match → fire
      ARTICULATION: đọc thơ về công ơn cha mẹ → FULL articulation → fire MẠNH
        → = §10 "New appreciation" mechanism
      OLFACTORY: smell mùi quen → olfactory direct to amygdala → fire NHANH
        → 🟢 Herz 2004: odor-evoked memory MORE emotional than visual
      CIRCUMSTANTIAL: buồn/lonely → brain RETRIEVE EC positive chunks → fire
        → = Nostalgia as self-regulation (§10.2)
      SOCIAL MEDIA: "On this day" photos, friend posts, viral content
        → Technology creates SYSTEMATIC Context-Triggers (§13)
    
    Intensity = f(cue specificity × EC depth × current gap state × hw reactivity × subsidy)
    
  🟢 VTA habituation: Schultz 1997
  🟢 Chunk-Miss + basal ganglia: O'Connor 2023
  🟢 Bowlby 3 phases: Bowlby 1969 (established)
  🟢 Olfactory-amygdala direct path: Herz 2004
  🟡 3 firing modes + hw subsidy modulation + satiation interaction = framework synthesis (v3.0)
```

---

## §7 — VTA HABITUATION × HARDWARE SUBSIDY

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §4.

```
⭐⭐ UNIFIED MODEL v3.0: TẠI SAO VALENCE "INVISIBLE" Ở DIFFERENT RATES:

  CƠ CHẾ GỐC (Body-Coupling §1.4 + BFM §3.2):
    Entity present REPEATEDLY → VTA encode as BASELINE
    VTA only fire reward khi: ACTUAL > BASELINE (positive prediction-delta)
    Entity present = EXPECTED = baseline met → delta = 0 → VTA silent
    → PFC: "bình thường, không có gì"
    → Body: L2 channels VẪN fire → opioid trickle → but below PFC threshold
    
  HARDWARE SUBSIDY = WHY DIFFERENT ENTITIES HABITUATE AT DIFFERENT RATES:
  
    VTA habituation = UNIVERSAL law (Schultz 1997)
    NHƯNG: hardware subsidy COUNTER habituation ở DIFFERENT LEVELS
    (from Resonance-Entity v2.0 §2)
    
    ┌────────────────────┬──────────────────────┬───────────────────────────┐
    │ Subsidy Level      │ Entity               │ Valence Habituation Rate  │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ MAXIMUM            │ Mẹ→Con               │ VERY SLOW                 │
    │ (oxytocin +        │                      │ Multiple hw systems COUNTER│
    │ baby schema +      │                      │ VTA habituation actively  │
    │ synchrony +        │                      │ → valence invisible but   │
    │ prolactin)         │                      │ RICHER baseline than others│
    │                    │                      │ → loss = DEVASTATING delta │
    │                    │                      │ 🟢 Feldman 2012           │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ MODERATE           │ Con→Mẹ, Kin          │ SLOW                      │
    │ (attachment hw,    │                      │ Attachment scaffold slows  │
    │ oxytocin scaffold) │                      │ habituation somewhat      │
    │                    │                      │ 🟢 Roberts & Dunbar 2011: │
    │                    │                      │ kin resilient without     │
    │                    │                      │ active maintenance        │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ TEMPORARY          │ Romantic (limerence)  │ ARTIFICIALLY SLOW → FAST  │
    │ (dopamine + NE     │                      │ 18-36m: SIMULATES slow    │
    │ surge, 18-36m)     │                      │ Post-limerence: subsidy   │
    │                    │                      │ EXPIRES → standard rate   │
    │                    │                      │ → "hết lửa" = subsidy end │
    │                    │                      │ 🟢 Fisher 2004            │
    ├────────────────────┼──────────────────────┼───────────────────────────┤
    │ NONE               │ Bạn thân, Colleague  │ STANDARD (fastest)        │
    │ (general μ-opioid  │                      │ No dedicated counter-hw   │
    │ only)              │                      │ → VTA habituates at       │
    │                    │                      │ default rate              │
    │                    │                      │ → MUST maintain via novelty│
    │                    │                      │ 🟢 Panksepp 1998          │
    └────────────────────┴──────────────────────┴───────────────────────────┘

  PARADOX ENRICHED:
    EC DEEPER + HIGH SUBSIDY → VTA habituated SLOWER → reward STILL somewhat visible
    EC DEEPER + NO SUBSIDY → VTA habituated FASTEST → reward MOST invisible
    
    → Mẹ→con: DEEP EC + MAX subsidy = habituated but RICH baseline
    → Bạn thân: DEEP EC + NO subsidy = habituated and LEAN baseline
    → = TẠI SAO "mất mẹ" = devastating nhưng "mất bạn" = recoverable
    → = KHÔNG chỉ depth → cả subsidy determines loss severity
    
    → Limerence DEEP + TEMP subsidy = INTENSE visible (reward FEELS strong)
    → Post-limerence: SAME depth nhưng subsidy GONE → reward ↓↓
    → = "Yêu lúc đầu mãnh liệt" → "Giờ bình thường" = subsidy expired, NOT love gone
    
  ONLY VISIBLE THROUGH:
    → ABSENCE (Mode 2): entity removed → baseline violated → pain
    → TRIGGER (Mode 3): context cue → L2 fire above threshold → feel
    → COMPARISON: new entity (no habituation) vs old (habituated) → old "feels less"
    → = "Có mới nới cũ" = VTA comparison, NOT bond quality comparison
    
  🟢 VTA habituation: Schultz 1997 (dopamine prediction error)
  🟢 Hedonic adaptation: Bao & Lyubomirsky 2013
  🟢 Hardware subsidy mechanisms: Feldman 2012, Fisher 2004, Panksepp 1998
  🟡 Subsidy × habituation rate = unified per-entity model = framework synthesis (v3.0)
```

---

## §8 — VALENCE × SATIATION TYPE

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §5.

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
      → DIRECTLY connects to VTA habituation (§7)

  GENERATIVE VALENCE — RENEWABLE EXCITING:
    Gap fill → new gap CREATE → new fill → new gap → perpetual
    = Valence renews with each novelty cycle
    
    Characteristics:
      → SELF-RENEWING: fill creates new gap → new delta → new reward
      → NOVELTY-DEPENDENT: same content → habituate → need NEW
      → EXCITING "feel": Type A dominant (evaluation, insight, discovery)
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
    
    Romantic post-L: Tonic + Generative (if genuine match)
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
    → Boredom.md v2.0 §3: source ⑥ by-product match dừng, M1-M4

  🟡 Satiation type × valence dynamics = framework synthesis (v3.0)
  🟢 3 satiation profiles: Gap-Body-Need v2.0 §2 (established independently)
  🟢 VTA habituation per reward type: Schultz 1997
```

---

## §9 — MIXED VALENCE: PARALLEL PER-CHANNEL

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §7.

```
⭐⭐ POSITIVE + NEGATIVE = 2 HỆ THỐNG THẦN KINH ĐỘC LẬP:

  🟢 Cacioppo & Berntson 1994 (Psychological Bulletin):
     EVALUATIVE SPACE MODEL (ESM):
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

  FRAMEWORK MAPPING (§2, §4.1):
    Per-channel valence = multi-dimensional (not bipolar axis)
    CẢ positive AND negative channels CÓ THỂ fire cùng lúc
    = Framework MORE GRANULAR than ESM (per-CHANNEL not just 2 dimensions)
    
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
      → If Type B dominant: "thương" = warm, gentle → mẹ direction
      → If Type A dominant: "thích" = exciting → bạn direction
      → SAME positive valence, DIFFERENT WORD → reflects RSA A:B ratio
      
    "CHÁN" = Generative dead + Tonic habituated
      → NO visible positive signal → PFC: "chán"
      → KHÁC "ghét": chán = ABSENCE of reward, ghét = PRESENCE of threat
      → "Chán" NGUY HIỂM HƠN (silent), "ghét" NHÌN THẤY (có thể address)
      
    "KHÔNG CẢM THẤY GÌ" = L2 habituated → below PFC threshold
      → L2 VẪN CÓ nhưng VTA habituated → invisible
      → ≠ "hết thương" → = "PFC không observe"
    
  🟡 Satiation type × mixed valence + verbalization = framework synthesis (v3.0)
  🟢 ESM: Cacioppo & Berntson 1994
  🟢 Parent-child ambivalence 50%: Lüscher & Pillemer 1998
  🟢 Vietnamese mixed emotions: Fang et al. 2025, Miyamoto et al. 2010
```

---

## §10 — "XA MẸ MỚI BIẾT THƯƠNG" — 3 CƠ CHẾ CỘNG DỒN

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §8.

```
⭐⭐⭐ PARADOX: sống cùng 20 năm = đôi khi ghét. Xa mẹ = bỗng thương.

  CƠ CHẾ ① — DECAY ASYMMETRY (Entity-Compiled.md v1.0 §9):
  
    3-layer decay model:
      ③ Negative EPISODES (cãi nhau, bị la): FADE NHANH NHẤT (months)
        → Hippocampus-dependent → most vulnerable to decay
        → CYCLIC avoidance channels → episode-bound → decay FAST (§8)
      ② Positive AFFECT (warmth, safety, love): FADE CHẬM HƠN
        → Reward circuits → more resistant
        → TONIC approach channels → baseline → decay SLOW (§8)
      ① Positive SCHEMA (mẹ = ai, hình ảnh): PERSIST DECADES
        → Neocortical → very resistant
    
    → Over time: Cyclic negative EPISODES fade → Tonic positive PERSIST
    → Net valence SHIFT POSITIVE
    → "Quên hết chuyện giận, chỉ nhớ cái tốt" = decay asymmetry × satiation type

  CƠ CHẾ ② — CONTRAST EFFECT (L2 absence → visible):
  
    Enriched with hardware subsidy (§7):
    Với mẹ: L2 = Tonic baseline → VTA habituated → INVISIBLE
    NHƯNG: hardware subsidy (MODERATE — con→mẹ direction) → baseline RICHER than bạn
    Xa mẹ: environment mới KHÔNG CÓ L2 warmth
    → L2 absence = VISIBLE lần đầu
    → "Hóa ra ấm lắm" = contrast with new environment
    → ⭐ Subsidy explains WHY contrast STRONGER for mẹ than for bạn:
      Mẹ: richer baseline (subsidized) → larger delta on absence
      Bạn: leaner baseline (no subsidy) → smaller delta on absence
      → "Xa mẹ nhớ MẠNH hơn xa bạn" = subsidy difference, not just depth
    
  CƠ CHẾ ③ — FIRST-TIME ARTICULATION:
  
    Với mẹ: PFC bận observe NEGATIVE (conflict = salient = above threshold)
    → Positive L2 = Tonic = habituated → PFC không allocate attention
    → 20 năm body BIẾT "thương mẹ" → PFC chưa bao giờ ARTICULATE
    
    Xa mẹ + đọc thơ:
    → Thơ = linguistic chunks MÔ TẢ compiled experience
    → PFC MATCH words ↔ compiled L2 → CONFIRM → "ồ, hóa ra tôi thương mẹ lắm"
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
    ② Subsidized baseline revealed → contrast STRONG (hardware subsidy)
    ③ Articulation + de-habituation → PFC observe + amplify
    = "Xa mẹ mới biết thương" = NOT paradox. = 3 mechanisms STACK.
    
  "CẢM XÚC CHƯA TỪNG THỂ HIỆN BAO GIỜ TRƯỚC KIA":
    = KHÔNG PHẢI "cảm xúc mới"
    = PFC LẦN ĐẦU OBSERVE Tonic positive mà LUÔN Ở ĐÓ
    = Body biết 20 năm. PFC mới observe lần đầu khi có lens (thơ).
    
  🟢 Decay 3-layer: Entity-Compiled.md v1.0 §9
  🟢 Whiteman et al. 2011: 10-year longitudinal — conflict ↓, intimacy ↑
  🟢 Arnett 2004: leaving home → more satisfying parent relationship
  🟡 3-mechanism model + satiation type decay + subsidy contrast = framework synthesis (v3.0)
```

### §10.1 — Nostalgia = L2 Active Self-Regulation

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
    → Brain RETRIEVE EC positive chunks (L2 channel F: PFC recall)
    → L2 fire → opioid release → body STABILIZE
    → = Body DÙNG compiled Tonic warmth từ past entities làm THUỐC AN THẦN
    
    Nostalgia DÙNG TONIC channels (not Cyclic or Generative):
      → Body recalls BASELINE warmth (Tonic) not episodes (Cyclic)
      → "Nhớ cảm giác ấm áp" not "nhớ lần nấu ăn cụ thể"
      → Entities with DEEP Tonic + HIGH subsidy = strongest nostalgia source (mẹ)

  VIDEO-CALL PARADOX:
    🟢 Van Tilburg et al. 2019: students feel MOST homesick during video-chat
    FRAMEWORK: Video = PARTIAL EC firing → L2 fire → NHƯNG touch/smell MISSING
    → Chunk-Miss ở MISSING spokes AMPLIFIED by partial activation
    → "Gọi mẹ xong nhớ hơn" = ĐÚNG, architecturally explainable

  🟢 Nostalgia self-regulation: Sedikides 2018
  🟢 Video-call homesickness: van Tilburg 2019
  🟡 Nostalgia as L2 Tonic self-regulation = framework synthesis (v3.0)
```

---

## §11 — PER-ENTITY VALENCE DYNAMICS + RSA A:B

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §10+§11.

```
⭐⭐ VALENCE DYNAMICS MAPPED PER ENTITY TYPE:

  MẸ→CON VALENCE:
    Dominant satiation: Tonic (existence-based) + Generative bursts (child changes)
    Hardware subsidy: MAXIMUM → habituation SLOW → Mode 1 = RICH baseline
    RSA A:B: ~40A/60B → valence "feel" = ẤM ÁP (B dominant)
    2-tầng: Tầng A dominant → valence INVISIBLE (hardware-driven)
    2-luồng: L2 dominant → valence STRUCTURAL (body-base extension)
    Mixed valence: LOW (hardware bias approach → avoidance rare)
    "Chán" risk: LOW (auto-novelty + max subsidy)
    Phantom on loss: DEVASTATING (all 4 factors MAX — §12)
    Technology substitute: CANNOT (CT afferents offline)
    → Trajectory: STABLE INVISIBLE baseline → visible ONLY on loss/trigger
    → = "Không thấy gì đặc biệt" → mất → DEVASTATING = signature pattern
    
  CON→MẸ VALENCE (child/teen):
    Dominant satiation: Cyclic + Tonic MIX (episodic needs + baseline safety)
    Hardware subsidy: MODERATE → habituation SLOW-MEDIUM
    RSA A:B: ~50A/50B → valence "feel" = BALANCED (ấm + đánh giá)
    2-tầng: A+B balanced → valence MIXED visibility
    2-luồng: L1→L2 shifting → valence FORMS over years
    Mixed valence: HIGH (normative 50% — Lüscher 1998)
    "Chán" risk: MODERATE (teen lifecycle shift, not true "chán")
    Phantom on loss: MAJOR (deep compilation + attachment hardware)
    Technology substitute: PARTIAL (video call maintain SOME)
    → Trajectory: FORMING → MIXED (teen) → POSITIVE SHIFT (xa mẹ = §10)
    → = "Vừa giận vừa thương" → xa mẹ → "thương mẹ mãnh liệt" = signature
    
  BẠN THÂN VALENCE:
    Dominant satiation: Generative dominant + Tonic component
    Hardware subsidy: NONE → habituation STANDARD (fastest)
    RSA A:B: ~70A/30B → valence "feel" = THÚ VỊ, HỨNG KHỞI (A dominant)
    2-tầng: Tầng B dominant → valence VISIBLE per episode
    2-luồng: L1 dominant → valence MOMENTARY (per-interaction reward)
    Mixed valence: LOW (genuine → positive-dominant)
    "Chán" risk: HIGH if no novelty (Generative habituates fast)
    Phantom on loss: MINOR-MODERATE (replaceable, no hardware lock-in)
    Technology substitute: PARTIAL (online maintain Generative, not touch)
    → Trajectory: EXCITING → HABITUATE without novelty → FADE without contact
    → = "Gặp nhau vui ghê" → "Lâu không gặp, quên" = signature pattern

  ROMANTIC VALENCE (post-limerence):
    Dominant satiation: Tonic + Generative (if genuine match)
    Hardware subsidy: TEMPORARY → vasopressin/oxytocin (if attachment forms)
    RSA A:B: ~60A/40B → valence "feel" = HỨNG KHỞI + ẤM (mixed A+B)
    2-tầng: A→B shift (limerence Tầng A simulated → post-L Tầng B)
    2-luồng: L1→L2 (if Entity-Compiled forms)
    Mixed valence: MODERATE → HIGH (living together → more conflict channels)
    "Chán" risk: HIGHEST (inflated baseline + no permanent subsidy + max exposure)
    Phantom on loss: COMPLEX (L2 structural + possible hormone echo)
    Technology substitute: PARTIAL (communication, not physical intimacy)
    → Trajectory: INTENSE (limerence) → 3 paths: genuine/flat/dissolution
    → = "Yêu cuồng nhiệt" → "Vẫn yêu" OR "Hết lửa" OR "Chia tay"

  COLLEAGUE VALENCE (Agent-mode moments):
    Dominant satiation: Generative (domain-specific)
    Hardware subsidy: NONE
    RSA A:B: ~85A/15B → valence "feel" = ĐÁNH GIÁ, KÍCH THÍCH TRÍ TUỆ
    2-tầng: Tầng B only → valence VISIBLE in Agent-mode only
    2-luồng: L1 only (unless transition to friend)
    Mixed valence: LOW (professional → thin)
    "Chán" risk: MODERATE (domain routine → habituate)
    Phantom on loss: MINOR (functional, replaceable)
    Technology substitute: HIGH (remote work maintains domain Generative)
    → Trajectory: CONTEXT-DEPENDENT → only in Agent-mode → fade on job change
    → = "Nghỉ việc → quên tuột" = signature pattern
```

### §11.1 — RSA A:B × Valence "Feel" + Hardware Reactivity

```
⭐ HARDWARE QUYẾT ĐỊNH CƯỜNG ĐỘ + RSA QUYẾT ĐỊNH "FEEL":

  HARDWARE REACTIVITY:
    🟢 Hariri et al. 2002: 5-HTTLPR short allele → GREATER amygdala response
    🟢 Aron & Aron 1997: HSP (15-20%) → deeper processing, more empathy
    🟢 Belsky & Pluess 2009: S-allele = PLASTICITY (not just vulnerability)
       More hurt under negative → BUT more appreciation under positive

  RSA A:B × VALENCE "FEEL" (Reward-Signal-Architecture v2.0 §1):
    Type B dominant (opioid, CT afferents) → "ấm áp, dễ chịu, an toàn"
    Type A dominant (evaluative, dopamine-adjacent) → "thú vị, exciting"
    
  ⭐ REACTIVITY × RSA A:B = 2 INDEPENDENT AXES:
    High reactivity + B dominant = INTENSE WARMTH (sensitive+warm)
    High reactivity + A dominant = INTENSE EXCITEMENT (sensitive+curious)
    Low reactivity + B dominant = GENTLE WARMTH
    Low reactivity + A dominant = CALM INTEREST
    → 4 combinations → 4 different valence "profiles"

  SPM vs REACTIVITY vs RSA (phân biệt rõ):
    SPM = prediction ACCURACY (how well predict entity)
    Reactivity = response INTENSITY (how strongly body responds)
    RSA A:B = response QUALITY (warm vs exciting)
    → 3 trục INDEPENDENT
    
  🟢 5-HTTLPR: Hariri 2002. HSP: Aron & Aron 1997. Plasticity: Belsky 2009.
  🟡 Reactivity × RSA A:B as 2 independent axes = framework synthesis (v3.0)
```

---

## §12 — PHANTOM RESONANCE × GRIEF

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §15.

```
⭐⭐ PHANTOM RESONANCE 4-FACTOR MODEL (Resonance-Entity v2.0 §15):

  MECHANISM:
    Entity compiled across channels → presence = BASELINE
    Entity lost → compiled patterns FIRE on triggers → predicted response = X
    → Actual response = NOTHING → prediction-delta NEGATIVE → body-feedback = pain
    → = "Phantom limb" of relationship (Ratcliffe 2018)
    → Patterns KEEP FIRING until Hebbian weaken → SLOW without deliberate uncompile

  PHANTOM DEPTH = f(4 factors):
    ① Compilation depth: more channels compiled → more phantom firing points
    ② Hardware subsidy: hw-supported bond → hw KEEPS firing after loss
    ③ L2 structural: entity = body-base extension → loss = body-base AMPUTATION
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

  ┌────────────────────┬──────────┬──────────┬──────────┬──────────┬───────────┐
  │ Factor             │ Mẹ mất   │ Con mất  │ Bạn mất  │ Partner  │ Colleague │
  │                    │ (con→mẹ) │ (mẹ→con) │ thân mất │ mất      │ mất       │
  ├────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ① Compilation      │ DEEP     │ VERY DEEP│ MODERATE │ DEEP     │ SHALLOW   │
  ├────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ② Hardware subsidy │ MODERATE │ MAXIMUM  │ NONE     │ SOME     │ NONE      │
  ├────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ③ L2 structural    │ STRONG   │ VERY     │ MODERATE │ STRONG   │ WEAK      │
  │                    │          │ STRONG   │ to WEAK  │ to VERY  │           │
  ├────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ ④ Duration         │ DECADES  │ YEARS→   │ YEARS    │ YEARS→   │ MONTHS→   │
  │                    │          │ DECADES  │          │ DECADES  │ YEARS     │
  ├────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ Dominant phantom   │ TONIC    │ TONIC+   │GENERATIVE│ MIXED    │ GENERATIVE│
  │ satiation type     │          │ CYCLIC   │          │ (all 3)  │           │
  ├────────────────────┼──────────┼──────────┼──────────┼──────────┼───────────┤
  │ PHANTOM INTENSITY  │ MAJOR    │DEVASTATING│ MINOR-  │ COMPLEX  │ MINOR     │
  │                    │          │          │ MODERATE │          │           │
  └────────────────────┴──────────┴──────────┴──────────┴──────────┴───────────┘

  ⭐ MẸ MẤT CON = MOST DEVASTATING:
    ALL 4 factors MAX → TONIC + CYCLIC phantom compound
    → Sanders 1980: parental grief = most severe category
    → Some parents: phantom NEVER fully resolves → "chronic grief"

  EXTREME VALENCE — LOVE/HATE SHARED CIRCUITS:
    🟢 Zeki & Romaya 2008 (PLoS ONE):
      SHARED: putamen + insula (cả love VÀ hate)
      LOVE: large parts judgment cortex DEACTIVATE → "mù quáng vì yêu"
      HATE: small zone deactivate → RETAINS judgment → "tính toán trả thù"
    → |Valence| CAO → body engage DEEP
    → Love → Hate: EASY (flip direction, keep depth) → betrayal
    → Hate → Love: HARD (negativity bias + need sustained positive)
    → Indifference → either: HARDER (need to BUILD depth first)
    → = Hate CLOSER to love than indifference is

  DISORGANIZED ATTACHMENT (Main & Hesse 1990):
    🟢 "FRIGHT WITHOUT SOLUTION": attachment figure = COMFORT AND FEAR source
    → 2-TẦNG CONFLICT: Tầng A (hardware) → approach VS Tầng B (SPM) → avoid
    → Cross-tầng → PFC arbitration INSUFFICIENT
    → Normal mixed: same tầng → PFC can arbitrate
    → QUALITATIVELY different from normal mixed

  🟢 Grief = phantom limb: Ratcliffe 2018. Parental grief: Sanders 1980.
  🟢 Love/hate circuits: Zeki & Romaya 2008. Disorganized: Main & Hesse 1990.
  🟡 Phantom × satiation type + 4-factor model = framework synthesis (v3.0)
```

---

## §13 — TECHNOLOGY × VALENCE FRONTIER

> **v3.0 NEW** — từ Drill-Entity-Valence-Dynamics v2.0 §16+§17.

```
⭐⭐ TECHNOLOGY THAY ĐỔI VALENCE DYNAMICS THẾ NÀO:

  SENSORY VALENCE TRIGGERS = LESS RELEVANT (technology filled):
    → Hunger: delivery apps → fill without entity → sensory Cyclic valence ↓
    → Temperature: AC, heating → self-fill → comfort Cyclic valence ↓
    → Entertainment: Netflix, games → fill novelty → Generative partially filled
    → = Sensory valence no longer REQUIRES entities (technology substitute)
    
  MODERN VALENCE FRONTIER = SOCIAL + ABSTRACT:
    Technology CHƯA fill:
      → Touch/comfort: CT afferents require PHYSICAL presence → Tonic Type B unfilled
      → Emotional regulation: L2 structural requires compiled entity → no substitute
      → Generative mutual: shared discovery requires 2 genuine drives → no one-way fill
      → Social validation: requires REAL social comparison → no synthetic
      → Meaning-in-relationship: entity-specific, cannot be mass-produced
    → "Có tiền mua mọi thứ nhưng vẫn cô đơn" = sensory filled, social unfilled

  SOCIAL MEDIA × VALENCE DYNAMICS:
    Context-Trigger AMPLIFICATION:
      → More triggers per day (algorithmic, curated)
      → "On this day" = ALGORITHMIC nostalgia scheduling
      → Friend posts = SYSTEMATIC narrative triggers
      → = Mode 3 firing FREQUENCY increased dramatically
    Parasocial valence:
      → Compiled positive BUT no L2 structural → shallow
      → Time on parasocial → LESS time for genuine → valence DECLINE
    
  AI × VALENCE:
    AI can: trigger EXISTING L2 (write about mẹ → EC fire → feel)
    AI can: fill Generative gaps (insight, analysis, conversation)
    AI cannot: create L2 (no mutual, no body, no by-product from AI gap)
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
    
  🟡 Technology × valence frontier + specialization portfolio = framework synthesis (v3.0)
  🟢 Kahneman & Deaton 2010: $75K plateau (sensory saturation evidence)
  🟢 Durkheim 1893: organic solidarity — specialized units NEED each other
```

---

## §14 — CÁCH VALENCE HÌNH THÀNH + UPDATE

```
🟡 VALENCE ĐƯỢC BUILD TỪ 4 NGUỒN:

  ① DIRECT EXPERIENCE — trải nghiệm trực tiếp:
    → Cầm dao → cắt tay → ĐAU → valence: { L0 safety: -- }
    → Mẹ cho ăn → HẾT ĐÓI → valence: { L1 nutrition: ++ }
    → = Nguồn CHÍNH XÁC NHẤT — body verify trực tiếp
    → = NHƯNG chậm (phải trải nghiệm mới biết)
    → 🟢 Classical conditioning: Pavlov, LeDoux 1996

  ② OBSERVED EXPERIENCE — quan sát người khác:
    → Thấy bạn bị chó cắn → valence chó: { L0 safety: - }
    → = Self-Pattern-Modeling đọc state người khác → infer valence
    → = NHANH hơn direct experience, kém chính xác hơn
    → 🟢 Observational learning: Bandura 1977
    → 🟢 Social referencing: Sorce 1985

  ③ SCHEMA INHERITANCE — thừa kế từ cộng đồng:
    → Mẹ nói "dao nguy hiểm" → valence: { L0 safety: - } (chưa cần bị cắt)
    → Tôn giáo: "Thiên Chúa yêu thương" → valence God: { ALL: ++ }
    → = NHANH NHẤT (không cần trải nghiệm hay quan sát)
    → = NHƯNG có thể SAI (schema inherit ≠ reality verify)
    → = TẠI SAO tuyên truyền WORK: install valence TRƯỚC khi verify
    → 🟢 Cultural transmission of fear: Rachman 1977
    → 🟢 Evaluative conditioning via verbal instruction: De Houwer 2007

  ④ CONTEXT INFERENCE — suy luận từ context:
    → Quả bom trong tay đồng đội: { positive }
    → Quả bom trong tay kẻ thù: { extreme negative }
    → = Cùng entity, khác context → khác valence

  ĐỘ TIN CẬY vs TỐC ĐỘ — TRADE-OFF:
    ┌──────────────────────────┬────────────────┬──────────────┐
    │ Nguồn                     │ Tốc độ          │ Độ chính xác  │
    ├──────────────────────────┼────────────────┼──────────────┤
    │ ① Direct experience       │ Chậm nhất      │ Cao nhất      │
    │ ② Observed experience     │ Trung bình     │ Trung bình    │
    │ ③ Schema inheritance      │ Nhanh nhất     │ Thấp nhất     │
    │ ④ Context inference       │ Tùy context    │ Tùy chunks    │
    └──────────────────────────┴────────────────┴──────────────┘
    → Evolutionary: "rắn nguy hiểm" inherit NHANH > tự bị cắn rồi biết
    → 🟢 Prepared learning: Seligman 1971


VALENCE UPDATE — 3 LOẠI:

  ① REINFORCEMENT — valence MẠNH thêm:
    → Mẹ cho ăn 1000 lần → valence { L1: ++ } compiled CỰC SÂU
    → = Lặp lại consistent → valence COMPILE thành schema sâu

  ② REVISION — valence THAY ĐỔI DẦN:
    → Dao: lần đầu cắt tay { L0: -- } → học cách dùng { L1: ++ dần override L0: -- }
    → Tốc độ revision tùy: intensity × frequency × recency

  ③ VIOLENT FLIP — valence BỊ ĐẢO NGƯỢC:
    → Bạn thân phản bội: trust++++ → trust---- (FLIP)
    → = CỰC HIẾM nhưng CỰC MẠNH — vì phá compiled schema
    → = Anchor-Schema.md §2: flip phá anchor → cascade collapse
    → 🟢 Betrayal trauma: Freyd 1996

  ⚠️ BIAS TRONG UPDATE:
    → Negativity bias: negative feedback → update NHANH hơn positive
    → Confirmation bias: valence hiện tại → filter feedback cho match
    → 🟢 Negativity bias: Baumeister et al. 2001
    → 🟢 Confirmation bias: Nickerson 1998
```

---

## §15 — VALENCE PROPAGATION QUA SCHEMA CHAIN

> ⚠️ **CLARIFICATION — Chain Analysis = EXPLANATORY, Không Phải Processing**
> *(Drill §6, §22 — GAP 13 RESOLVED)*
>
> Chain analysis = **Cấp 3** (framework giải thích tại sao behavior hoạt động).
> **KHÔNG phải** cách brain PROCESS ở **Cấp 1** — cá nhân compile SHORT (1-2 nodes).
> Chain dài **SỐNG ở Cấp 2** (collective infrastructure hold cho cá nhân).
> Vẫn CÓ GIÁ TRỊ: chẩn đoán chain gãy, thiết kế collective, phát hiện trust sai.
> Chi tiết Model 3 cấp + 4 compile pathways: Collective-Body.md v1.2 §1-§2.

```
🔴 HYPOTHESIS — concept mới, logic consistent với established research,
    chưa formalize trong literature dưới tên "valence propagation"

⭐ CORE INSIGHT:

  Framework đã có (Schema.md §1):
    Schema = CHUNKS + LINKS + PURPOSE

  Entities KHÔNG tồn tại cô lập.
    Entities LINK VỚI NHAU qua schema network.
    Và valence TRUYỀN qua những links đó.

  VÍ DỤ:
    Entity "toán" — có feed body-base trực tiếp không? → KHÔNG.
    NHƯNG "toán" LINK tới chain:
      toán → điểm tốt → đại học → việc tốt → lương → body-base L1 feed
    Valence positive từ CUỐI chain TRUYỀN NGƯỢC:
      lương (+++) → việc tốt (++) → đại học (+) → điểm tốt (+) → toán (+)
    = Toán có valence positive VÌ link tới chain kết thúc ở body-base feed


⭐ 4 CƠ CHẾ PROPAGATION:

  ① FORWARD PROPAGATION (learning path):
    Body-base need → tìm path → action → reward → path COMPILE
    VD: Đói → tìm quán → ăn → hết đói → "quán này tốt" (compile)
    🟢 Operant conditioning: Thorndike's Law of Effect 1898
    🟢 Reinforcement learning: Sutton & Barto 1998

  ② BACKWARD PROPAGATION (reward spread):
    Reward ở cuối chain → valence positive TRUYỀN NGƯỢC qua từng node
    VD: Lương (reward) → job → đại học → toán (positive vì trên đường tới reward)
    🟢 Temporal difference learning: Schultz 1997 (dopamine prediction error)
    🟡 Explicit "valence backward propagation" = framework formalization

  ③ LATERAL PROPAGATION (generalization):
    Entity tương tự CŨNG nhận valence — dù chưa trải nghiệm trực tiếp
    VD: 1 con chó cắn → sợ TẤT CẢ chó → sợ NGƯỜI NUÔI chó
    ⚠️ ASYMMETRY: Negative lateral NHANH + RỘNG. Positive lateral CHẬM + HẸP.
    🟢 Stimulus generalization: Pavlov, Watson (Little Albert 1920)
    🟢 Overgeneralization in anxiety: Dunsmoor & Murphy 2015

  ④ INSTALL PROPAGATION (schema inheritance chain):
    Cộng đồng install TOÀN BỘ CHAIN sẵn, KHÔNG cần trải nghiệm
    VD: Bố mẹ install: "không học → vất vả → đau khổ"
    VD: Tôn giáo: "sống đạo đức → Thiên Đàng → hạnh phúc vĩnh cửu"
      = TOÀN BỘ chain installed, unfalsifiable → KHÔNG BAO GIỜ bị phá
    🟢 Cultural transmission: Boyd & Richerson 1985
    🟡 "Install propagation" = framework term

  4 cơ chế TƯƠNG TÁC:
    Forward tìm path → Backward reinforce → Lateral expand → Install provide starting chains
    Install chain CÓ THỂ bị Forward VERIFY hoặc REJECT

  🟢 Spreading activation: Collins & Loftus 1975
  🟢 Associative network models: Anderson 1983
  🟡 4-mechanism model = framework categorization
```

---

## §16 — CHAIN PROPERTIES + WHY CHAIN DÀI TỒN TẠI

### §16.1 — 5 Đặc tính

```
🔴 HYPOTHESIS — framework formalization, logic consistent

  ① CHAIN LENGTH → VALENCE DECAY + PFC ACCURACY DECREASE:
    Chain NGẮN (gai → đau): Valence MẠNH. PFC trace 100%.
    Chain TRUNG BÌNH (toán → ... → lương): Valence YẾU hơn. PFC ~70%.
    Chain DÀI (multi-branch): Valence PHỨC TẠP. PFC ~30%.
    Chain INVISIBLE (hardware): PFC ~10%. "Tôi thích toán" = label, not explanation.
    🟢 Goal gradient: Hull 1932. Temporal discounting: Ainslie 1975.

  ② CHAIN TRUST → PROPAGATION STRENGTH:
    Mỗi link có trust level riêng. Propagation ≈ PRODUCT of trusts.
    Trust = 0 tại 1 link → CHAIN ĐỨT:
      "4 năm đại học → thất nghiệp" → link collapse → "Học vô ích"
    → Anchor-Schema.md §2: Trust ≥ Cost → hold; Trust < Cost → collapse.

  ③ PARALLEL CHAINS → ADDITIVE:
    NHIỀU chains connect entity → body-base CÙNG LÚC → valence = TỔNG
    Single chain YẾU → dễ bỏ. Multiple parallel → MẠNH → khó bỏ.
    = Tại sao "đam mê" = nhiều chains converge vào 1 activity

  ④ CONFLICTING CHAINS → MIXED VALENCE:
    Chain positive (mẹ cho ăn → L1++) + Chain negative (mẹ ép học → autonomy--)
    → CÙNG entity, 2 chains ngược → YÊU + GHÉT cùng lúc (§9)
    
  ⑤ INVISIBLE CHAINS → PFC CONFABULATION:
    Chain compiled SÂU / hardware-level / quá dài / multi-branch
    → PFC KHÔNG access → phải explain → CONFABULATE
    → Chi tiết: §18

  🟡 5 chain properties = framework formalization
```

### §16.2 — 4 Tầng Cơ Chế Tạo + Giữ Chain Dài

```
🟡 CHAIN DÀI = EMERGENT, KHÔNG DESIGNED:

  TẦNG 1 — EXIST: Chunk substrate tự nhiên tạo chain qua connections
    → Spreading activation tự lan (Collins & Loftus 1975)
    → Chunks → meta-chunks → schemas → hierarchy (Hebb 1949)
    🟢 Established mechanisms

  TẦNG 2 — EXTEND: 4 cơ chế valence propagation kéo dài chain (§15)
    → Forward tìm path + Backward reinforce + Install cộng đồng
    🟢🟡 Mixed

  TẦNG 3 — FIT: Pyramidal compression cho chain dài vào PFC 4±1
    → 4×4×4 = 64 thông tin gốc compressed vào 1 slot
    → Chain dài = sản phẩm VÔ THỨC, không phải PFC
    ⚠️ ĐÍNH CHÍNH: "PFC lớn hơn → chain dài hơn" = SAI
    → 🟢 Brain size vs IQ: ~0.24 correlation (Pietschnig 2015)
    → 🟢 Cowan 2001: PFC hold 4±1 dimensions
    🟢🟡

  TẦNG 4 — FILTER: Group selection giữ lại cá nhân có chain dài
    → Tầng 1-3 ĐÃ ĐỦ → Tầng 4 = optional
    🟡🔴

  TRADE-OFF: Chain dài = feature, NOT bug
    → Hại (cá nhân): PFC blind, trauma chain, unfalsifiable sacrifice
    → Lợi (tập thể): empathy, deferred investment, cooperation, knowledge transfer
    → P(benefit nhóm) >> P(harm cá nhân) → evolution giữ lại
```

---

## §17 — CASES PHÂN TÍCH

```
🟡 CASES PHÂN LOẠI THEO 6 NHÓM — verify valence system:


  ═══════════════════════════════════════════════════
  NHÓM A — DIRECT CHAIN (ngắn, PFC trace được):
  ═══════════════════════════════════════════════════

  A1) Dẫm gai → luôn đi dép:
    Chain: gai → đau → L0 threat. Length 1. Direct. 1 lần ĐỦ.
    PFC accuracy: ~100%. = Per-entity valence, không cần propagation.

  A2) Bật lửa nổ → sợ bật lửa:
    Chain: bật lửa → nổ → đau + shock → L0. Length 1. Direct.


  ═══════════════════════════════════════════════════
  NHÓM B — DEFERRED INVESTMENT (chain dài, trust):
  ═══════════════════════════════════════════════════

  B1) Học sinh làm toán (4 khả năng song song):
    Chain a: toán → điểm → đại học → job → lương → L1 (install, length 4)
    Chain b: không học → bị mắng → L0 threat (install, length 1-2)
    Chain c: hardware fit → Goldilocks → VTA → reward (invisible, intrinsic)
    Chain d: "toán thú vị" = PFC label SAU → reinforce chain c
    → 4 chains PARALLEL, PFC biết a+b, KHÔNG biết c+d

  B2) Jensen Huang — 30 năm Imagine-Final (🟢 public record):
    Giai đoạn 1: Anchor-Schema → NVIDIA startup. Chain LONG + DEFERRED.
    Giai đoạn 2: GPU thành công → chain VERIFY → trust TĂNG.
    Giai đoạn 3: Tỷ phú, 60+. Body-base ĐÃ đủ. Drive vẫn mạnh.
      → Anchor-Schema EVOLVE + intrinsic mastery + novelty vẫn fire.
    ⚠️ Internal schemas NÀO drive = CHỈ ÔNG ẤY BIẾT. Framework chỉ INFER.


  ═══════════════════════════════════════════════════
  NHÓM C — MIRROR CHAIN ("cho đi", invisible):
  ═══════════════════════════════════════════════════

  C1) Trẻ con giúp mẹ:
    Chain 1: compiled deep valence mẹ: {++}
    Chain 2: SPM → empathy dissonance. Chain 3: giúp → mẹ vui → opioid.
    Chain 4: reciprocity schema → identity.
    PFC: "Vì mẹ hay giúp tôi" — biết chain 4, KHÔNG biết chain 2+3.

  C2) "Vô tư" giúp người lạ:
    Chain 1-5: lateral overgeneralize + empathy + status + identity + connection
    PFC: "Vô tư thôi" — KHÔNG biết 5 chains. Layer 7 label.


  ═══════════════════════════════════════════════════
  NHÓM D — SCHEMA INHERITANCE (installed, unfalsifiable):
  ═══════════════════════════════════════════════════

  D1) Gia đình Hà Lan giấu người Do Thái WWII (🟢 documented):
    Schema inheritance + empathy + identity + anchor + connection = 5 chains
    → 5 chains > L0 cost (tử hình!) → body drive "giấu"
    🟢 Yad Vashem: ~28,000 "Righteous Among Nations"

  D2) Tin Thiên Đàng → vượt khó:
    Unfalsifiable chain. Body VẪN feed dù content chưa verify:
    "Sống đạo đức" → community accept → connection feed.
    = Schema effectiveness ≠ Schema truthfulness (§18)

  D3) "Giàu mới hạnh phúc" → đạt rồi trống rỗng:
    Installed chain promise ALL channels. Reality: L1 feed ONLY.
    Đường đi sacrifice connection + health → đạt giàu → MISMATCH.
    NHƯNG: giàu MÀ giữ relationship + health → KHÔNG trống rỗng.


  ═══════════════════════════════════════════════════
  NHÓM E — MISLINK (cơ chế đúng, content sai):
  ═══════════════════════════════════════════════════

  E1) Sát nhân máu lạnh:
    Schema MISLINK: gây hại → CONTROL → mastery → reward.
    Hardware typically NOT broken: IQ average+. Chunks OK. Chain sai.
    🟢 Hickey 2013: serial killers report "power" and "control"

  E2) Revenge phi lý (bỏ 200M kiện cho 100M):
    L1 cost: -200M. NHƯNG chain 1-3: dissonance resolve + identity + Schadenfreude >> cost.
    🟢 Costly punishment: Fehr & Gächter 2002
    🟢 Schadenfreude: Takahashi et al. 2009


  ═══════════════════════════════════════════════════
  NHÓM F — OVERGENERALIZE (lateral propagation):
  ═══════════════════════════════════════════════════

  F1) Bị chó cắn → sợ mọi chó → ghét người nuôi chó:
    Direct → category → associated entity. Negative: NHANH + RỘNG.

  F2) Positive childhood → default trust người lạ:
    CÙNG CƠ CHẾ, khác hướng. NHƯNG cần NHIỀU experience hơn (negativity bias).
```

---

## §18 — PFC BLINDNESS + 3 NGUYÊN TẮC

> v3.0: MERGE từ v2.0 §8 + §9.

### §18.1 — PFC Blindness

```
🟡 TẠI SAO PFC THƯỜNG KHÔNG BIẾT VALENCE CHAIN:

  Feeling.md v2.0 §2: 7 LAYERS — fidelity GIẢM DẦN:
    Layer 1-5: body → integration → chunk match (valence chain hoạt động ở đây)
    Layer 6: Labeling (40-80%). Layer 7: Explanation (20-70%)
    PFC OBSERVE từ Layer 6 trở đi → thấy OUTPUT, KHÔNG thấy MECHANISM.

  3 CẤP ĐỘ PFC AWARENESS:

  ① PFC BIẾT (~80-100%): chain ngắn + direct + recent
    "Tôi sợ gai vì bị ốm lần đó" — chain length 1

  ② PFC BIẾT MỘT PHẦN (~40-70%): chain trung bình + installed
    "Tôi học vì tương lai" — đúng SURFACE, THIẾU detail

  ③ PFC KHÔNG BIẾT (~10-30%): chain invisible, hardware, compiled
    "Tôi thích từ thiện" — PFC: "vô tư." Body: nhiều compiled chains fire.
    "Tôi đam mê vật lý" — PFC: "vì nó hay." Body: hardware + Goldilocks.
    → PFC CONFABULATE: tìm lý do PHÙ HỢP nhưng KHÔNG PHẢI mechanism

  ⭐ "VÔ TƯ" VÀ "ĐAM MÊ" — 2 CONFABULATION PHỔ BIẾN NHẤT:
  
    "CHO ĐI VÔ TƯ": PFC không thấy chains. Body: empathy + identity + status + reciprocal.
    BẰNG CHỨNG "KHÔNG VÔ TƯ" — 3 violation tests:
      Test 1: DỪNG khi body-base thiếu (đói → không cho cơm)
      Test 2: DỪNG khi schema phản bội (từ thiện gian lận → dừng)
      Test 3: DỪNG khi reciprocity = 0 kéo dài
    → Nếu thật sự "vô tư" → sẽ KHÔNG DỪNG. Nhưng nó DỪNG → có điều kiện.

    "ĐAM MÊ": PFC label cho "nhiều chains converge → strong sustained drive"
    "Đam mê" KHÔNG PHẢI nguyên nhân hành vi — mà là MÔ TẢ kết quả
    = Drive.md §0: "'Đam mê' = MÔ TẢ drive mạnh + sustained, KHÔNG PHẢI nguyên nhân"

  🟢 Confabulation: Nisbett & Wilson 1977
  🟢 Readiness potential: Libet 1983
  🟢 Split-brain confabulation: Gazzaniga
```

### §18.2 — 3 Nguyên Tắc

```
⭐ 3 NGUYÊN TẮC QUAN TRỌNG:

  NGUYÊN TẮC 1 — Schema Effectiveness ≠ Schema Truthfulness:
    Schema CÓ THỂ sai hoàn toàn MÀ VẪN effective:
      Tin Thiên Đàng → behavioral output (chăm chỉ + đạo đức) → body feed → EFFECTIVE
    Schema CÓ THỂ true MÀ VẪN fail:
      "Giàu = hạnh phúc" → đường đi sacrifice connection → FAIL
    → 2 chiều KHÁC NHAU: true+effective, true+fail, false+effective, false+fail

  NGUYÊN TẮC 2 — Body Check OUTPUT, Không Check TRUTH:
    Body KHÔNG verify chain content. Body CHỈ verify chain output.
    → Body = PRAGMATIST, không phải SCIENTIST
    → Schema sai TỒN TẠI LÂU nếu output vẫn feed body-base
    → Schema đúng BỊ REJECT nếu output KHÔNG feed
    → PFC CHỈ check truth khi TRIGGERED (dissonance, forced evaluation)

  NGUYÊN TẮC 3 — "Vô Tư" Đúng Ở Tầng PFC, Sai Ở Tầng Body:
    TẦNG PFC: "Không mong gì" = MÔ TẢ ĐÚNG conscious experience
    TẦNG BODY: Compiled patterns LUÔN fire, LUÔN có reward
    CẢ HAI ĐÚNG — ở tầng riêng.
    → Biết mechanism KHÔNG LÀM GIẢM giá trị "cho đi"
    → Framework mục đích: HIỂU, không phải PHÁN XÉT
```

### §18.3 — Giới Hạn Nền Tảng

```
🟡 SCHEMA VÔ TẬN → CHAIN KHÔNG THỂ MAP CHÍNH XÁC:

  86 tỷ neurons × ~100 nghìn tỷ connections = hệ thống quá lớn
  Schema MULTI-MODAL (body + motor + visual + somatic + emotional + verbal)
  → Chain A→B→C→...→body-base: biết nó TỒN TẠI, không thể vẽ bản đồ

  Con người KHÔNG CẦN map chính xác:
    ① Biết PATTERN nào đang drive (nhận diện, không cần chính xác)
    ② Biết pattern đó SERVE body-base hay KHÔNG (check output)
    ③ Biết khi nào cần THAY ĐỔI (detect dissonance)
  → Framework = "công cụ navigate, không phải GPS chính xác"

  ⚠️ BLACKBOX 2: Valence complexity — chuỗi valence dài gần như incomputable.
  Framework predict PATTERN, không predict INSTANCE. Chi tiết: Blackbox-Map.md §4+§7.
```

---

## §19 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (~35 claims)
═══════════════════════════════════════

  Per-entity valence:
    Multi-channel emotional processing: established
    Mixed feelings (ambivalence): Cacioppo & Berntson 1994
    Negativity bias: Baumeister et al. 2001
    Fear conditioning + evaluative conditioning: LeDoux 1996, De Houwer 2007
    Confirmation bias: Nickerson 1998

  Valence hình thành + propagation evidence:
    4 nguồn: classical conditioning, observational (Bandura), cultural (Rachman), context
    Spreading activation: Collins & Loftus 1975
    Temporal difference learning: Schultz 1997
    Goal gradient: Hull 1932. Temporal discounting: Ainslie 1975
    Stimulus generalization: Pavlov, Watson. Overgeneralization: Dunsmoor & Murphy 2015

  PFC blindness:
    Confabulation: Nisbett & Wilson 1977
    Readiness potential: Libet 1983
    Split-brain: Gazzaniga
    Betrayal trauma: Freyd 1996

  Entity-Compiled:
    Grief as body-level pain: Eisenberger 2003
    Attachment bond: Bowlby 1969
    Empathy fatigue: Figley 2002
    Adolescent ambivalence: established developmental psychology
    Parent-child ambivalence 50%: Lüscher & Pillemer 1998

  Valence dynamics (v3.0 NEW):
    VTA habituation: Schultz 1997
    Chunk-Miss + basal ganglia: O'Connor 2023
    Bowlby 3 phases: Bowlby 1969
    Olfactory-amygdala: Herz 2004
    ESM: Cacioppo & Berntson 1994
    2-level bittersweet: Vaccaro, Kaplan & Damasio 2020
    Co-activation: Larsen, McGraw & Cacioppo 2001
    Ambivalent ≠ neutral: Schneider et al. 2021
    Nostalgia self-regulation: Sedikides & Wildschut 2018
    Video-call homesickness: van Tilburg et al. 2019
    HSP: Aron & Aron 1997. Plasticity: Belsky & Pluess 2009
    Love/hate circuits: Zeki & Romaya 2008
    Disorganized attachment: Main & Hesse 1990
    Leaving home → better: Whiteman 2011, Arnett 2004
    Hardware subsidy: Feldman 2012, Fisher 2004, Panksepp 1998
    Hedonic adaptation: Bao & Lyubomirsky 2013
    Parental grief: Sanders 1980. Phantom: Ratcliffe 2018.
    Income plateau: Kahneman & Deaton 2010

═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (~25 claims)
═══════════════════════════════════════

  §1-§2: Valence as multi-channel PROFILE, Object vs Agent vs Abstract
  §3: Structural vs Current valence + satiation type dimension
  §4: Entity-Compiled 3 subtypes, Entity-Compiled vs Obligation
  §5: L2+A = invisible, L1+B = visible paradox
  §6: 3 Firing Modes taxonomy + hw subsidy modulation
  §7: Hardware subsidy × habituation rate = unified model
  §8: Cyclic/Tonic/Generative × valence dynamics
  §9: Satiation type × mixed valence + verbalization mapping
  §10: "New appreciation" 3-mechanism model
  §11: Per-entity valence dynamics trajectory + RSA A:B × feel
  §12: Phantom 4-factor model × satiation type
  §13: Technology × valence frontier + specialization portfolio
  §14: 4 nguồn as explicit model
  §15: 4 propagation mechanisms as explicit model
  §16: 5 chain properties + 4-tầng chain dài
  §18: 3 nguyên tắc (effectiveness≠truthfulness, output check, vô tư 2 levels)

═══════════════════════════════════════
🔴 HYPOTHESIS (~6 claims)
═══════════════════════════════════════

  Valence propagation as EXPLICIT NAMED MODEL
  Backward propagation (abstract chain)
  Chain trust = product of link trusts (oversimplified)
  Group selection cho chain dài (optional, Tầng 4)
  Exact articulation amplification magnitude
  Partial EC fire intensity formula


CÂU HỎI MỞ:
  → Cơ chế neural CỤ THỂ cho valence propagation? Brain regions?
  → Chain decay function: linear? exponential? step?
  → Maximum chain length mà body vẫn trust?
  → Positive overgeneralize: same mechanism nhưng KHÁC TỐC ĐỘ bao nhiêu?
  → Social media habituation of nostalgia triggers?
  → Entity-Compiled subtypes: gradient hay threshold?
```

---

## §20 — CROSS-REFERENCES + CITATIONS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Body-Base.md v2.1 — L0-L3 channels mà valence đánh giá
    → Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, chunk dynamics
    → Schema.md v2.0 — schema = chunks + links + purpose
    → Chunk.md v2.2 — chunk substrate, context-tag, 4 connections
    → Reward-Signal-Architecture.md v1.0 — Type A/B × valence
    → Gap-Body-Need.md v2.0 — Cyclic/Tonic/Generative satiation types
    → Body-Feedback-Label.md v2.0 — vocabulary reference

  ENTITY-COMPILED + ACCESS + DYNAMICS:
    → Entity-Compiled.md v1.0 — deep mechanism (Hub-and-Spoke, Dunbar, grief, decay)
    → Entity-Access.md v1.0 — gradient Mức 0-5, 3-Factor Model, excess, calibration
    → Inter-Body-Mechanism.md v1.0 — §8 EC reframe, §4 3-cost, §5 By-Product Match
    → Body-Coupling.md v1.1 — coupling 2D model, 3 Phase, extension/entanglement
    → Connection.md v3.3 — 3 Generative Primitives, 2-luồng/2-tầng overview
    → Self-Pattern-Modeling.md v3.1 — F1/F2, Simulation Engine application 1
    → Agent-Mechanism.md v2.0 — integration hub, Architecture B
    → Resonance-Entity.md v2.0 — hardware subsidy per entity, RSA A:B
    → Resonance-Sustainability.md v1.0 — 3 modalities, maintenance decline
    → Obligation.md v1.0 — compiled prediction (independent of EC)
    → Protect.md v1.0 — f(replaceability × attachment), loss aversion
    → Boredom.md v2.0 — dissonance + Imagine-Final mờ, source ⑥, M1-M4

  PFC + SIMULATION:
    → PFC-Operations.md v1.0 — Hold/Suppress, Compiled/Fresh, PFC budget
    → Simulation-Engine.md v1.0 — 1 engine, 3 components, 3 axes
    → Feeling.md v2.0 — PFC observation of body (7 layers)
    → Drive.md — tổng hợp valences → action

  PROPAGATION CONTEXT:
    → Collective-Body.md v1.2 — Model 3 cấp + trust bridge
    → Anchor-Schema.md v1.2 — anchor amplify chain, trust ≥ cost
    → Emergent-Patterns.md §5 — "Cho đi" pattern
    → Empathy.md v2.2 §6-§8 — empathy reward, burnout formula
    → Somatic-Articulation-Loop.md — body → explicit knowledge

  APPLICATION:
    → AI-Schema-Detection.md v2.0 — pattern detection
    → Imagine-Final-Evaluation.md — Mismatch quadrant


RESEARCH CITATIONS:

  | # | Citation | Used in |
  |---|----------|---------|
  | R1 | Schultz 1997 — Dopamine prediction error / VTA | §3,§6,§7 |
  | R2 | Cacioppo & Berntson 1994 — Evaluative Space Model | §9 |
  | R3 | Vaccaro, Kaplan & Damasio 2020 — Bittersweet neuroscience | §9 |
  | R4 | Larsen, McGraw & Cacioppo 2001 — Can feel happy+sad | §9 |
  | R5 | Schneider et al. 2021 — Ambivalent ≠ neutral | §9 |
  | R6 | Lüscher & Pillemer 1998 — 50% parent-child ambivalence | §9,§11 |
  | R7 | Sedikides & Wildschut 2018 — Nostalgia self-regulation | §10.1 |
  | R8 | Oba et al. 2016 — Memory+reward coproduce nostalgia | §10.1 |
  | R9 | Van Tilburg et al. 2019 — Video-chat homesickness | §10.1 |
  | R10 | Hariri et al. 2002 — 5-HTTLPR amygdala reactivity | §11.1 |
  | R11 | Aron & Aron 1997 — HSP 15-20% | §11.1 |
  | R12 | Belsky & Pluess 2009 — Plasticity model | §11.1 |
  | R13 | Zeki & Romaya 2008 — Love/hate shared circuits | §12 |
  | R14 | Main & Hesse 1990 — Disorganized attachment | §12 |
  | R15 | O'Connor 2023 — Basal ganglia grief firing | §6 |
  | R16 | Bowlby 1969 — Attachment 3 phases | §4,§6 |
  | R17 | Herz 2004 — Odor-evoked emotional memory | §6 |
  | R18 | Bao & Lyubomirsky 2013 — Hedonic adaptation | §7 |
  | R19 | Whiteman et al. 2011 — Parent-child over time | §10 |
  | R20 | Arnett 2004 — Emerging adulthood | §10 |
  | R21 | Fang et al. 2025 — Cross-cultural mixed emotions | §9 |
  | R22 | Miyamoto et al. 2010 — Dialectical thinking ambivalence | §9 |
  | R23 | Feldman 2012 — Biobehavioral synchrony | §7 |
  | R24 | Fisher 2004 — Limerence motivation drive | §7 |
  | R25 | Panksepp 1998 — μ-opioid social play | §7 |
  | R26 | Roberts & Dunbar 2011 — Kin resilient vs friends | §7 |
  | R27 | Sanders 1980 — Parental grief most severe | §12 |
  | R28 | Ratcliffe 2018 — Grief as phantom limb | §12 |
  | R29 | Fisher 2010 — Rejected lovers cocaine circuits | §12 |
  | R30 | Aron & Aron 1996 — Self-expansion model | §8 |
  | R31 | Gottman & Levenson 2000 — Type 2 divorce | §8 |
  | R32 | Kahneman & Deaton 2010 — Income-wellbeing plateau | §13 |
  | R33 | Durkheim 1893 — Organic solidarity | §13 |
  | R34 | Eisenberger 2003 — Social pain = physical pain | §4 |
  | R35 | LeDoux 1996 — Fear conditioning | §1 |
  | R36 | De Houwer 2007 — Evaluative conditioning | §1,§14 |
  | R37 | Nisbett & Wilson 1977 — PFC confabulation | §1,§18 |
  | R38 | Bandura 1977 — Observational learning | §14 |
  | R39 | Rachman 1977 — Cultural fear transmission | §14 |
  | R40 | Seligman 1971 — Prepared learning | §14 |
  | R41 | Boyd & Richerson 1985 — Cultural transmission | §15 |
  | R42 | Collins & Loftus 1975 — Spreading activation | §15,§16 |
  | R43 | Ainslie 1975 — Temporal discounting | §16 |
  | R44 | Hull 1932 — Goal gradient | §16 |
  | R45 | Freyd 1996 — Betrayal trauma | §14 |
  | R46 | Baumeister et al. 2001 — Negativity bias | §14 |
  | R47 | Nickerson 1998 — Confirmation bias | §14 |
  | R48 | Libet 1983 — Readiness potential | §18 |
  | R49 | Festinger 1957 — Cognitive dissonance | §2 |
  | R50 | Fehr & Gächter 2002 — Costly punishment | §17 |
  | R51 | Takahashi et al. 2009 — Schadenfreude | §17 |
  | R52 | Pietschnig 2015 — Brain size vs IQ | §16 |
  | R53 | Cowan 2001 — PFC 4±1 | §16 |
  | R54 | Hebb 1949 — Hebbian learning | §16 |
  | R55 | Hickey 2013 — Serial killers | §17 |


STATUS:

  v1.0 — 2026-04-18 — Initial version: per-entity + propagation + chain + cases
  v1.1 — 2026-04-18 — +§5b chain dài. ĐÍNH CHÍNH PFC size.
  v1.3 — 2026-04-28 — +Body-Coupling reference.
  v1.4 — 2026-05-08 — +Clarification Explanatory vs Processing. GAP 13+8 RESOLVED.
  v2.0 — 2026-05-16 — FULL REWRITE: Entity-Compiled reframe, 3 subtypes, merge §5+§5b.
  v3.0 — 2026-05-22 — FULL REWRITE: Drill-Entity-Valence-Dynamics v2.0 (28 insights).
    +TRỤ 2 (§5-§13): 2-luồng/2-tầng, 3 Firing Modes, Hardware Subsidy,
    Satiation Type, Mixed Valence, "Xa mẹ", Per-entity dynamics, Phantom,
    Technology frontier. §4 slim down (→ pointer EC v1.0 + EA v1.0).
    §8+§9 v2.0 merge → §18. Phase A integration.
    v2.0 → backup/Valence-Propagation-v2.0-backup.md.
```
