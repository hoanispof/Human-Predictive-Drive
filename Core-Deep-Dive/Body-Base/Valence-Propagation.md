---
title: Valence-Propagation — Hệ Thống Đánh Giá Của Body + Cơ Chế Truyền Qua Schema Network
version: 4.1
created: 2026-04-18
rewritten: 2026-05-29 (v4.0 — SPLIT: entity-valence dynamics → Entity-Valence-Dynamics.md v1.0)
refined: 2026-05-29 (v4.1 — L3 RETIRE: "L0-L1-L3 channels" → L0+L1 substrate + observation parameters. 2-dimension model aligned with Body-Base v3.3)
previous_versions:
  - v3.0 → backup/Valence-Propagation-v3.0-backup.md
  - v2.0 → backup/Valence-Propagation-v2.0-backup.md
  - v1.4 → backup/Valence-Propagation-v1.4-backup.md
status: v4.1 — REFERENCE FILE (valence definition + propagation mechanism)
scope: |
  WHAT valence IS (definition, 4 đặc tính, valence profile per-entity) +
  HOW valence FORMS (4 nguồn, 3 update types, bias) +
  HOW valence PROPAGATES qua schema chain (4 cơ chế, 5 chain properties, 4-tầng chain dài) +
  CASES phân tích (6 nhóm) + PFC BLINDNESS + 3 NGUYÊN TẮC + GIỚI HẠN.
  v4.0 SPLIT: Per-entity valence dynamics (v3.0 §3-§13) → Entity-Valence-Dynamics.md v1.0.
  Companion: Entity-Valence-Dynamics.md v1.0 = HOW valence BEHAVES per-entity over time.
  File này = WHAT valence IS + HOW it FORMS + HOW it PROPAGATES.
purpose: |
  Central reference cho valence definition + formation + propagation mechanism.
  2 trụ: WHAT valence IS (§1-§2) + HOW valence FORMS AND PROPAGATES (§3-§7).
  Per-entity dynamics → Entity-Valence-Dynamics.md v1.0 (companion file).
dependencies:
  - Entity-Valence-Dynamics.md v1.0 — companion: HOW valence behaves per-entity over time
  - Body-Base.md v3.3 — L0+L1 substrate + observation parameters mà valence đánh giá
  - Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, 2 sources, 3 dynamics
  - Schema.md v2.0 — schema = chunks + links + purpose
  - Chunk.md v2.2 — chunk substrate, context-tag, 4 connection types
  - Anchor-Schema.md v1.2 — anchor amplify propagation, trust binding
  - Collective-Body.md v1.2 — Model 3 cấp (Clarification reference)
  - Self-Pattern-Modeling.md v3.1 — observed experience (§3 nguồn ②)
  - Agent-Mechanism.md v2.0 — Mode 2 schema override (§2 abstract entities)
  - Feeling.md v2.0 — PFC observation of body-feedback (khác tầng)
  - Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State × valence
  - Drive.md — tổng hợp valences → action
sources:
  - Valence-Propagation v3.0 (2,001L) — content preserved (§1-§2 + §14-§18 → §3-§7)
  - Entity-valence dynamics (v3.0 §3-§13) → Entity-Valence-Dynamics.md v1.0
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
> **Toán có feed body-base trực tiếp không? KHÔNG.**
> **Nhưng toán LINK tới chain: toán → điểm → đại học → job → lương → body feed.**
> **Valence positive ở CUỐI chain TRUYỀN NGƯỢC → toán (+).**
> **= Valence PROPAGATION qua schema network.**
>
> File này: Valence LÀ GÌ, cấu trúc per-entity,
> cách valence HÌNH THÀNH từ 4 nguồn,
> cách valence TRUYỀN qua schema chain,
> TẠI SAO PFC không biết, và GIỚI HẠN nền tảng.
>
> **Per-entity valence dynamics** (Structural vs Current, Hardware-Subsidy,
> 3 Firing Modes, Satiation Type, Phantom resonance...)
> **→ Entity-Valence-Dynamics.md v1.0** (companion file).

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — VALENCE LÀ GÌ
- §2 — VALENCE PROFILE: Cấu Trúc Per-Entity
- §3 — CÁCH VALENCE HÌNH THÀNH + UPDATE
- §4 — VALENCE PROPAGATION QUA SCHEMA CHAIN
- §5 — CHAIN PROPERTIES + WHY CHAIN DÀI TỒN TẠI
- §6 — CASES PHÂN TÍCH
- §7 — PFC BLINDNESS + 3 NGUYÊN TẮC
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES + CITATIONS

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 VALENCE TRONG KIẾN TRÚC FRAMEWORK:

  VALENCE = CÁCH BODY ĐÁNH GIÁ MỌI THỨ.

  Trước khi hành động, body phải ĐÁNH GIÁ:
    "Entity này ảnh hưởng body-base CỦA TÔI thế nào?"
    "Positive? Negative? Mixed? Qua channel nào?"
  Kết quả đánh giá = VALENCE.

  Valence THUỘC VỀ Body-Base vì:
    → Body là NƠI đánh giá xảy ra (amygdala, insula, body signals)
    → Body-base substrate (L0+L1) là THƯỚC ĐO đánh giá
    → Valence = body's ASSESSMENT, không phải PFC's judgment
    → PFC có thể OBSERVE valence (thành feeling), nhưng KHÔNG tạo ra nó
    → = Feeling.md v2.0: "Feeling = PFC observation of body"
    → = Valence = WHAT body computes. Feeling = WHAT PFC sees.

  VALENCE × BODY-NEED (Body-Feedback-Mechanism v2.0 §1):
    Body-Need = aggregate OUTPUT của chunk dynamics (Body-Feedback-Mechanism v2.0).
    Valence = body's ASSESSMENT per-entity → feeds INTO body-need.
    Entity có valence positive → body-need shift toward approach.
    Entity có valence negative → body-need shift toward avoid.
    Tổng hợp valences across entities + body state = body-need hiện tại.


  FILE NÀY TRONG FLOW:

    Body-Base.md (L0+L1 substrate — NỀN TẢNG)
         │
         ▼
    Body-Feedback-Mechanism.md v2.0 (Body-Need aggregate, chunk dynamics)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ VALENCE-PROPAGATION.MD v4.1 (FILE NÀY)                     │
    │                                                              │
    │  TRỤ 1: VALENCE LÀ GÌ (§1-§2)                              │
    │    Valence definition → valence profile per-entity           │
    │                                                              │
    │  → Entity-Valence-Dynamics.md v1.0 (COMPANION FILE)         │
    │    HOW valence behaves per-entity over time:                 │
    │    Structural/Current, 3 Firing Modes, Hardware-Subsidy,     │
    │    Satiation Type, Mixed valence, Phantom resonance,         │
    │    Technology frontier                                       │
    │                                                              │
    │  TRỤ 2: VALENCE FORMATION + PROPAGATION (§3-§7)             │
    │    4 nguồn hình thành → 4 cơ chế propagation → Chain        │
    │    properties → Cases phân tích → PFC Blindness              │
    └─────────────────────────────────────────────────────────────┘
         │
         ▼
    Drive.md (TỔNG HỢP valences → action)
    Feeling.md v2.0 (PFC OBSERVE valence → feeling)
    Drill-Emergent-Pattern.md (valence TÍCH LŨY → patterns emerge)
    Anchor-Schema.md (anchor AMPLIFY propagation)


  PHÂN BIỆT 4 CONCEPTS GẦN NHAU:

    VALENCE (file NÀY):
      "Entity X ảnh hưởng body-base CỦA TÔI thế nào?"
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


  v4.1 CHANGELOG:
    v4.0 → v4.1: L3 RETIRE — "L0-L1-L3 channels" → L0+L1 substrate + observation parameters.
    §1 def: 2-dimension model (Substrate L0+L1 × Processing Direct-State/Evaluative).
    §2 table: "BODY-BASE CHANNELS" → "SUBSTRATE ASSESSMENT" + "EVALUATIVE ASSESSMENT".
    +Social under L1 (hardware social need, Coan 2015).
    Observation parameters (Novelty, Status, Protect, Mastery) = evaluative OUTPUT, not channels.
    Aligned with Body-Base.md v3.3 §5.3 (L3 retired in v3.0).

  v4.0 CHANGELOG:
    v3.0 → v4.0: SPLIT — entity-valence dynamics (v3.0 §3-§13) → Entity-Valence-Dynamics.md v1.0.
    File này giữ: TRỤ 1 (§1-§2 definition) + TRỤ 2 (§3-§7 formation + propagation).
    Renumber: v3.0 §14→§3, §15→§4, §16→§5, §17→§6, §18→§7.
    v3.0 → backup/Valence-Propagation-v3.0-backup.md.

  v2.0 → v3.0: +TRỤ 2 (§5-§13) từ Drill-Entity-Valence-Dynamics v2.0 (28 insights).
    §4 Entity-Compiled SLIM DOWN. §8+§9 v2.0 → §18 (merge PFC Blindness + 3 Nguyên tắc).
```

---

## §1 — VALENCE LÀ GÌ

```
🟡 ĐỊNH NGHĨA:

  Valence = ĐÁNH GIÁ CỦA BODY về cách 1 entity ảnh hưởng body-base.

  "Entity" = bất kỳ thứ gì body gặp trong domain:
    → Object: dao, ghế, xe, sách, bom, gai, bật lửa...
    → Agent: mẹ, bạn, sếp, chó, Thiên Chúa, Jensen Huang...
    → Abstract: toán, vật lý, từ thiện, tương lai, Thiên Đàng...
    → Action: giúp đỡ, kiện tụng, học bài, giết người...
    → State: giàu, nghèo, cô đơn, nổi tiếng...

  Body-base có 2 CHIỀU ĐÁNH GIÁ (Body-Base.md v3.3):

    CHIỀU 1 — SUBSTRATE (body monitors CÁI GÌ?):
      → L0 Alive: safe ←→ dangerous (binary threshold)
      → L1 Body-inputs: useful ←→ harmful (nutrition, sleep, comfort, autonomy, social...)

    CHIỀU 2 — SIGNAL PROCESSING (body tạo signal KIỂU GÌ?):
      → Direct-State: hardware pathways, from birth (Reward-Signal-Architecture.md)
      → Evaluative: compiled patterns, develops with age (E₀→E₃)

    OBSERVATION PARAMETERS (named patterns at evaluative output):
      → Novelty, Status, Protect, Mastery = TÊN GỌI cho patterns PFC observe
      → KHÔNG phải channels hay layers — là OUTPUT của evaluative processing trên L0+L1


  ⭐ 4 ĐẶC TÍNH CỐT LÕI:

  ① MULTI-CHANNEL — KHÔNG PHẢI 1 TRỤC TỐT/XẤU:

    SAI: "Mẹ = tốt" hoặc "Mẹ = xấu" (1 trục)
    ĐÚNG: Mẹ = {
      L1 nutrition: ++ (cho ăn)
      L1 comfort: ++ (ôm, vỗ về)
      L1 autonomy: -- (ép học, cấm chơi)
      Mastery: + (dạy bài)
      Novelty: - (bắt lặp lại bài khó)
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
    → PFC CŨNG không phân biệt (§7 confabulation)
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
  │ SUBSTRATE ASSESSMENT (L0 + L1):                               │
  │   L0 Alive:     safe ←───────→ dangerous                    │
  │   L1 Body-inputs:                                            │
  │     Nutrition:   useful ←─────→ harmful                      │
  │     Comfort:     pleasant ←───→ unpleasant                   │
  │     Sleep:       promoting ←──→ disrupting                   │
  │     Autonomy:    enabling ←───→ constraining                 │
  │     Social:      connecting ←─→ isolating                    │
  │                                                              │
  │ EVALUATIVE ASSESSMENT (compiled pattern evaluation):         │
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

    ① Mỗi dimension có valence RIÊNG — không average
      Mẹ: L1++ nhưng autonomy-- = KHÔNG phải "hơi positive"
      = Positive ở dimensions này, Negative ở dimensions kia, CÙNG LÚC

    ② Không phải mọi dimension đều có valence cho mọi entity
      Dao: L0, L1 rõ ràng. Status? Gần zero. Novelty? Chỉ lần đầu.
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
  │ Dao: L0, L1          │ Mẹ: L0, L1, evaluative, trust, dependency │
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
    BODY-BASE EXTENSION → Entity-Valence-Dynamics.md §2.


  ABSTRACT ENTITY VALENCE:

    Ngoài Object và Agent, còn có abstract entities:
      Toán, vật lý, từ thiện, Thiên Đàng, "tương lai tốt đẹp"...
    
    Abstract entity valence ĐẶC BIỆT vì:
      → Không có physical form → KHÔNG có L0 direct
      → Valence HOÀN TOÀN qua schema link (§4 Propagation)
      → Có thể UNFALSIFIABLE (Thiên Đàng, "ý nghĩa cuộc đời")
      → → Không bao giờ nhận negative feedback → valence KHÔNG BAO GIỜ bị revise
      → → = "Thiết kế" valence ổn định nhất có thể
      → = Agent-Mechanism.md §10: Mode 2 schema override cho abstract agents

    🟡 Abstract entity valence = framework concept
    🟢 Unfalsifiable belief resilience = Popper + Festinger 1957 (cognitive dissonance)
```

---

> **⭐ COMPANION FILE — Per-Entity Valence Dynamics:**
>
> Entity-Valence-Dynamics.md v1.0 chi tiết cách valence THAY ĐỔI per-entity over time:
> Structural vs Current valence, 2-luồng/2-tầng × visibility,
> 3 Firing Modes, Hardware-Subsidy × VTA habituation,
> Satiation Type × dynamics, Mixed valence, "Xa mẹ mới biết thương,"
> per-entity trajectory, extreme valence, phantom resonance, technology frontier.
>
> **Đọc:** §1-§2 trên (valence definition) → Entity-Valence-Dynamics.md → §3-§7 dưới (formation + propagation).

---

## §3 — CÁCH VALENCE HÌNH THÀNH + UPDATE

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

## §4 — VALENCE PROPAGATION QUA SCHEMA CHAIN

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

## §5 — CHAIN PROPERTIES + WHY CHAIN DÀI TỒN TẠI

### §5.1 — 5 Đặc tính

```
🔴 HYPOTHESIS — framework formalization, logic consistent
  ⚠️ % below = calibration anchor illustrating gradient, KHÔNG phải đo lường chính xác.

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
    → CÙNG entity, 2 chains ngược → YÊU + GHÉT cùng lúc (Entity-Valence-Dynamics.md §7)
    
  ⑤ INVISIBLE CHAINS → PFC CONFABULATION:
    Chain compiled SÂU / hardware-level / quá dài / multi-branch
    → PFC KHÔNG access → phải explain → CONFABULATE
    → Chi tiết: §7

  🟡 5 chain properties = framework formalization
```

### §5.2 — 4 Tầng Cơ Chế Tạo + Giữ Chain Dài

```
🟡 CHAIN DÀI = EMERGENT, KHÔNG DESIGNED:

  TẦNG 1 — EXIST: Chunk substrate tự nhiên tạo chain qua connections
    → Spreading activation tự lan (Collins & Loftus 1975)
    → Chunks → meta-chunks → schemas → hierarchy (Hebb 1949)
    🟢 Established mechanisms

  TẦNG 2 — EXTEND: 4 cơ chế valence propagation kéo dài chain (§4)
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

## §6 — CASES PHÂN TÍCH

```
🟡 CASES PHÂN LOẠI THEO 6 NHÓM — verify valence system:


  ═══════════════════════════════════════
  NHÓM A — DIRECT CHAIN (ngắn, PFC trace được):
  ═══════════════════════════════════════

  A1) Dẫm gai → luôn đi dép:
    Chain: gai → đau → L0 threat. Length 1. Direct. 1 lần ĐỦ.
    PFC accuracy: ~100%. = Per-entity valence, không cần propagation.

  A2) Bật lửa nổ → sợ bật lửa:
    Chain: bật lửa → nổ → đau + shock → L0. Length 1. Direct.


  ═══════════════════════════════════════
  NHÓM B — DEFERRED INVESTMENT (chain dài, trust):
  ═══════════════════════════════════════

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


  ═══════════════════════════════════════
  NHÓM C — MIRROR CHAIN ("cho đi", invisible):
  ═══════════════════════════════════════

  C1) Trẻ con giúp mẹ:
    Chain 1: compiled deep valence mẹ: {++}
    Chain 2: Self-Pattern-Modeling → empathy dissonance. Chain 3: giúp → mẹ vui → opioid.
    Chain 4: reciprocity schema → identity.
    PFC: "Vì mẹ hay giúp tôi" — biết chain 4, KHÔNG biết chain 2+3.

  C2) "Vô tư" giúp người lạ:
    Chain 1-5: lateral overgeneralize + empathy + status + identity + connection
    PFC: "Vô tư thôi" — KHÔNG biết 5 chains. Feel-Explanation label.


  ═══════════════════════════════════════
  NHÓM D — SCHEMA INHERITANCE (installed, unfalsifiable):
  ═══════════════════════════════════════

  D1) Gia đình Hà Lan giấu người Do Thái WWII (🟢 documented):
    Schema inheritance + empathy + identity + anchor + connection = 5 chains
    → 5 chains > L0 cost (tử hình!) → body drive "giấu"
    🟢 Yad Vashem: ~28,000 "Righteous Among Nations"

  D2) Tin Thiên Đàng → vượt khó:
    Unfalsifiable chain. Body VẪN feed dù content chưa verify:
    "Sống đạo đức" → community accept → connection feed.
    = Schema effectiveness ≠ Schema truthfulness (§7)

  D3) "Giàu mới hạnh phúc" → đạt rồi emptiness:
    Installed chain promise ALL channels. Reality: L1 feed ONLY.
    Đường đi sacrifice connection + health → đạt giàu → MISMATCH.
    NHƯNG: giàu MÀ giữ relationship + health → KHÔNG emptiness.


  ═══════════════════════════════════════
  NHÓM E — MISLINK (cơ chế đúng, content sai):
  ═══════════════════════════════════════

  E1) Sát nhân máu lạnh:
    Schema MISLINK: gây hại → CONTROL → mastery → reward.
    Hardware typically NOT broken: IQ average+. Chunks OK. Chain sai.
    🟢 Hickey 2013: serial killers report "power" and "control"

  E2) Revenge phi lý (bỏ 200M kiện cho 100M):
    L1 cost: -200M. NHƯNG chain 1-3: dissonance resolve + identity + Schadenfreude >> cost.
    🟢 Costly punishment: Fehr & Gächter 2002
    🟢 Schadenfreude: Takahashi et al. 2009


  ═══════════════════════════════════════
  NHÓM F — OVERGENERALIZE (lateral propagation):
  ═══════════════════════════════════════

  F1) Bị chó cắn → sợ mọi chó → ghét người nuôi chó:
    Direct → category → associated entity. Negative: NHANH + RỘNG.

  F2) Positive childhood → default trust người lạ:
    CÙNG CƠ CHẾ, khác hướng. NHƯNG cần NHIỀU experience hơn (negativity bias).
```

---

## §7 — PFC BLINDNESS + 3 NGUYÊN TẮC

### §7.1 — PFC Blindness

```
🟡 TẠI SAO PFC THƯỜNG KHÔNG BIẾT VALENCE CHAIN:

  Feeling.md v2.0 §2: 7 LAYERS — fidelity GIẢM DẦN:
    Feel-RawSignals → Feel-Location: body → integration → chunk match (valence chain hoạt động ở đây)
    Feel-Labeling (40-80%). Feel-Explanation (20-70%)
    PFC OBSERVE từ Feel-Labeling trở đi → thấy OUTPUT, KHÔNG thấy MECHANISM.

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

### §7.2 — 3 Nguyên Tắc

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

### §7.3 — Giới Hạn Nền Tảng

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

## §8 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (~20 claims)
═══════════════════════════════════════

  Valence definition (§1-§2):
    Multi-channel emotional processing: established
    Mixed feelings (ambivalence): Cacioppo & Berntson 1994
    Fear conditioning + evaluative conditioning: LeDoux 1996, De Houwer 2007
    Nisbett & Wilson 1977: PFC cannot access actual processing
    Unfalsifiable belief resilience: Popper + Festinger 1957

  Valence hình thành + propagation evidence (§3-§5):
    4 nguồn: classical conditioning, observational (Bandura), cultural (Rachman), context
    Spreading activation: Collins & Loftus 1975
    Temporal difference learning: Schultz 1997
    Goal gradient: Hull 1932. Temporal discounting: Ainslie 1975
    Stimulus generalization: Pavlov, Watson. Overgeneralization: Dunsmoor & Murphy 2015
    Prepared learning: Seligman 1971
    Betrayal trauma: Freyd 1996
    Negativity bias: Baumeister et al. 2001. Confirmation bias: Nickerson 1998

  PFC blindness (§7):
    Confabulation: Nisbett & Wilson 1977
    Readiness potential: Libet 1983
    Split-brain: Gazzaniga

  Per-entity valence dynamics → Entity-Valence-Dynamics.md v1.0 §14.


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (~8 claims)
═══════════════════════════════════════

  §1-§2: Valence as multi-channel PROFILE, Object vs Agent vs Abstract
  §3: 4 nguồn as explicit model + 3 update types
  §4: 4 propagation mechanisms as explicit model
  §5: 5 chain properties + 4-tầng chain dài
  §7: 3 nguyên tắc (effectiveness≠truthfulness, output check, vô tư 2 levels)

  Per-entity dynamics synthesis → Entity-Valence-Dynamics.md v1.0 §14.


═══════════════════════════════════════
🔴 HYPOTHESIS (~4 claims)
═══════════════════════════════════════

  Valence propagation as EXPLICIT NAMED MODEL
  Backward propagation (abstract chain)
  Chain trust = product of link trusts (oversimplified)
  Group selection cho chain dài (optional, Tầng 4)


CÂU HỎI MỞ:
  → Cơ chế neural CỤ THỂ cho valence propagation? Brain regions?
  → Chain decay function: linear? exponential? step?
  → Maximum chain length mà body vẫn trust?
  → Positive overgeneralize: same mechanism nhưng KHÁC TỐC ĐỘ bao nhiêu?
```

---

## §9 — CROSS-REFERENCES + CITATIONS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Body-Base.md v3.3 — L0+L1 substrate + observation parameters
    → Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, chunk dynamics
    → Schema.md v2.0 — schema = chunks + links + purpose
    → Chunk.md v2.2 — chunk substrate, context-tag, 4 connections
    → Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State × valence
    → Body-Feedback-Label.md v2.0 — vocabulary reference

  COMPANION FILE (per-entity valence dynamics):
    → Entity-Valence-Dynamics.md v1.0 — Structural/Current, 3 Firing Modes,
      Hardware-Subsidy, Satiation Type, Mixed valence, Phantom resonance,
      Technology frontier. ĐỌC SAU §1-§2, TRƯỚC §3-§7.

  PFC + OBSERVATION:
    → Feeling.md v2.0 — PFC observation of body (7 layers)
    → Drive.md — tổng hợp valences → action
    → Self-Pattern-Modeling.md v3.1 — observed experience (§3 nguồn ②)
    → Agent-Mechanism.md v2.0 — Mode 2 schema override (§2 abstract entities)

  PROPAGATION CONTEXT:
    → Collective-Body.md v1.2 — Model 3 cấp + trust bridge (§4)
    → Anchor-Schema.md v1.2 — anchor amplify chain, trust ≥ cost (§3, §5)
    → Drill-Emergent-Pattern.md §5 — "Cho đi" pattern (§6 cases)
    → Empathy.md v2.2 §6-§8 — empathy reward, burnout formula (§6 cases)
    → Somatic-Articulation-Loop.md — body → explicit knowledge

  APPLICATION:
    → AI-Schema-Detection.md v2.0 — pattern detection
    → Imagine-Final-Evaluation.md — Mismatch quadrant
    → Blackbox-Map.md §4+§7 — BLACKBOX 2 chain complexity


RESEARCH CITATIONS:

  | # | Citation | Used in |
  |---|----------|---------|
  | R1 | LeDoux 1996 — Fear conditioning | §1 |
  | R2 | De Houwer 2007 — Evaluative conditioning | §1, §3 |
  | R3 | Nisbett & Wilson 1977 — PFC confabulation | §1, §7 |
  | R4 | Festinger 1957 — Cognitive dissonance | §2 |
  | R5 | Bandura 1977 — Observational learning | §3 |
  | R6 | Rachman 1977 — Cultural fear transmission | §3 |
  | R7 | Seligman 1971 — Prepared learning | §3 |
  | R8 | Freyd 1996 — Betrayal trauma | §3 |
  | R9 | Baumeister et al. 2001 — Negativity bias | §3 |
  | R10 | Nickerson 1998 — Confirmation bias | §3 |
  | R11 | Schultz 1997 — Dopamine prediction error / VTA | §4 |
  | R12 | Dunsmoor & Murphy 2015 — Overgeneralization in anxiety | §4 |
  | R13 | Boyd & Richerson 1985 — Cultural transmission | §4 |
  | R14 | Collins & Loftus 1975 — Spreading activation | §4, §5 |
  | R15 | Hull 1932 — Goal gradient | §5 |
  | R16 | Ainslie 1975 — Temporal discounting | §5 |
  | R17 | Pietschnig 2015 — Brain size vs IQ | §5 |
  | R18 | Cowan 2001 — PFC 4±1 | §5 |
  | R19 | Hebb 1949 — Hebbian learning | §5 |
  | R20 | Fehr & Gächter 2002 — Costly punishment | §6 |
  | R21 | Takahashi et al. 2009 — Schadenfreude | §6 |
  | R22 | Hickey 2013 — Serial killers | §6 |
  | R23 | Libet 1983 — Readiness potential | §7 |


STATUS:

  v1.0 — 2026-04-18 — Initial version: per-entity + propagation + chain + cases
  v1.1 — 2026-04-18 — +§5b chain dài. ĐÍNH CHÍNH PFC size.
  v1.3 — 2026-04-28 — +Body-Coupling reference.
  v1.4 — 2026-05-08 — +Clarification Explanatory vs Processing. GAP 13+8 RESOLVED.
  v2.0 — 2026-05-16 — FULL REWRITE: Entity-Compiled reframe, 3 subtypes, merge §5+§5b.
  v3.0 — 2026-05-22 — FULL REWRITE: +Drill-Entity-Valence-Dynamics v2.0 (28 insights).
    +TRỤ 2 entity-valence dynamics. Phase A integration.
    v2.0 → backup/Valence-Propagation-v2.0-backup.md.
  v4.0 — 2026-05-29 — SPLIT: entity-valence dynamics (v3.0 §3-§13) → Entity-Valence-Dynamics.md v1.0.
    File này giữ: definition (§1-§2) + formation/propagation (§3-§7).
    Renumber: v3.0 §14→§3, §15→§4, §16→§5, §17→§6, §18→§7.
    v3.0 → backup/Valence-Propagation-v3.0-backup.md.
  v4.1 — 2026-05-29 — L3 RETIRE: "L0-L1-L3 channels" → L0+L1 substrate + observation parameters.
    §1: 2-dimension model (Substrate × Processing). §2: table restructure SUBSTRATE + EVALUATIVE.
    Aligned with Body-Base v3.3 §5.3.
```
