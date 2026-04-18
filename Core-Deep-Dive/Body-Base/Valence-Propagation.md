---
title: Valence-Propagation — Hệ Thống Đánh Giá Của Body + Cơ Chế Truyền Qua Schema Network
version: 1.1
created: 2026-04-18
updated: 2026-04-18 (v1.1 — thêm §5b WHY chain dài tồn tại)
status: v1.1 — REFERENCE FILE (kiến trúc tổng thể Valence system)
scope: |
  WHAT valence IS + HOW valence WORKS per-entity + HOW valence PROPAGATES qua schema chain
  + WHY PFC không biết + GIỚI HẠN nền tảng.
  Tích hợp: Domain/backup/Valence.md (per-entity, DRAFT v0.5) + phân tích MỚI session N+16
  (propagation, chain properties, PFC blindness, fundamental limits).
purpose: |
  Central reference file cho toàn bộ Valence system trong framework.
  Thay thế Domain/Valence.md DRAFT (2026-04-12, ~579L → Domain/backup/Valence.md).
  Vai trò tương đương Feeling.md v2.0 và Chunk.md v2.0 cho hệ thống tương ứng.
sources: |
  Domain/backup/Valence.md (~579L) — per-entity valence, profile, object vs agent, cases
  Schema.md §1-§1.2 — schema = chunks + links + purpose, KHÔNG THỂ phân tích chính xác
  Drive.md §0 — schema = DETECTOR, vô thức = ENGINE, PFC = navigator
  Anchor-Schema.md §1-§2 — trust binding, cost, anchor strength
  Feeling.md v2.0 §2-§6 — 7-layer fidelity gradient, reward, 8-step flow
  Chunk.md v2.0 — chunk substrate, multi-modal binding
  Emergent-Patterns.md §5 — "Cho đi" pattern, 4 nguồn reward
  Empathy.md §6 — empathy reward override spectrum (lành mạnh → compulsive)
  Session N+16 analysis — 12+ cases, schema-chain valence propagation concept
  Session N+19 analysis — WHY chain dài tồn tại, 4 tầng cơ chế, PFC-Capacity refine
  PFC-Analysis.md — pyramidal compression, 4±1 dimensions, Observed Capacity formula
  Empathy.md §7 — evolutionary function, group selection logic
  Chunk.md v2.0 §3 — 4 connection types (substrate for chain formation)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
backup: Domain/backup/Valence.md
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
> **Bạn giúp đỡ người lạ. PFC bạn nói: "vô tư thôi."**
> **Body bạn ĐANG TÍNH: empathy reward + status + identity + connection.**
> **4 chuỗi schema fire SONG SONG → net reward >> cost.**
> **PFC KHÔNG BIẾT những chuỗi này tồn tại.**
>
> **Bạn "đam mê" vật lý. PFC nói: "vì nó hay."**
> **Body: hardware fit + chunk match + Goldilocks + VTA delta.**
> **Chain INVISIBLE — PFC chỉ thấy output, không thấy mechanism.**
>
> Valence KHÔNG CHỈ tồn tại per-entity.
> Valence CÒN TRUYỀN qua links trong schema network.
> Và những chuỗi truyền đó — PFC thường KHÔNG biết.
>
> File này: Valence LÀ GÌ, cấu trúc per-entity, cách hình thành,
> cách UPDATE, cách TRUYỀN qua schema chain,
> TẠI SAO PFC không biết, và GIỚI HẠN nền tảng.

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — VALENCE LÀ GÌ
- §2 — VALENCE PROFILE: Cấu Trúc Per-Entity
- §3 — CÁCH VALENCE HÌNH THÀNH + UPDATE
- §4 — VALENCE PROPAGATION QUA SCHEMA CHAIN
- §5 — 5 ĐẶC TÍNH CỦA CHAIN
- §5b — TẠI SAO CHAIN DÀI TỒN TẠI: 4 Tầng Cơ Chế ← MỚI v1.1
- §6 — CASES PHÂN TÍCH
- §7 — PFC BLINDNESS + CONFABULATION
- §8 — GIỚI HẠN NỀN TẢNG + 3 NGUYÊN TẮC
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES + STATUS

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
    → Body channels (L0-L3) là THƯỚC ĐO đánh giá
    → Valence = body's ASSESSMENT, không phải PFC's judgment
    → PFC có thể OBSERVE valence (thành feeling), nhưng KHÔNG tạo ra nó
    → = Tương tự Feeling.md v2.0: "Feeling = PFC observation of body"
    → = Valence = WHAT body computes. Feeling = WHAT PFC sees.


  FILE NÀY TRONG FLOW:

    Body-Base.md (L0-L3 channels — NỀN TẢNG)
         │
         ▼
    ┌─────────────────────────────────────────────────────────┐
    │ VALENCE-PROPAGATION.MD (FILE NÀY)                       │
    │                                                          │
    │  TẦNG 1: Per-Entity Valence (§1-§3)                     │
    │    Entity → body channels → valence profile              │
    │    "Cái dao NÀY ảnh hưởng body TÔI thế nào?"           │
    │                                                          │
    │  TẦNG 2: Valence Propagation (§4-§5-§5b) ← MỚI          │
    │    Valence TRUYỀN qua links trong schema network         │
    │    "Toán có valence positive VÌ link tới tương lai"     │
    │    §5b: WHY chain dài tồn tại (4 tầng cơ chế)          │
    │                                                          │
    │  TẦNG 3: PFC Blindness + Limits (§7-§8) ← MỚI         │
    │    PFC KHÔNG biết phần lớn valence chain                │
    │    "Cho đi vô tư" = PFC label cho invisible chain       │
    └─────────────────────────────────────────────────────────┘
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

  "Body channels" = hệ thống L0-L3 (Body-Base.md):
    → L0 Alive: safe ←→ dangerous
    → L1 Body-inputs: useful ←→ harmful (nutrition, sleep, sex...)
    → L3 Pattern: novelty, mastery, status, protect
    → (L2 removed — Body-Input-Enumeration.md reframe)


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

  THÊM: ABSTRACT ENTITY VALENCE:

    Ngoài Object và Agent, còn có abstract entities:
      Toán, vật lý, từ thiện, Thiên Đàng, "tương lai tốt đẹp"...
    
    Abstract entity valence ĐẶC BIỆT vì:
      → Không có physical form → KHÔNG có L0 direct
      → Valence HOÀN TOÀN qua schema link (§4 Propagation)
      → Có thể UNFALSIFIABLE (Thiên Đàng, "ý nghĩa cuộc đời")
      → → Không bao giờ nhận negative feedback → valence KHÔNG BAO GIỜ bị revise
      → → = "Thiết kế" valence ổn định nhất có thể
      → = Agent.md §10: Mode 2 schema override cho abstract agents

    🟡 Abstract entity valence = framework concept
    🟢 Unfalsifiable belief resilience = Popper + Festinger 1957 (cognitive dissonance)
```

---

## §3 — CÁCH VALENCE HÌNH THÀNH + UPDATE

```
🟡 VALENCE ĐƯỢC BUILD TỪ 4 NGUỒN:

  ① DIRECT EXPERIENCE — trải nghiệm trực tiếp:

    → Cầm dao → cắt tay → ĐAU → valence: { L0 safety: -- }
    → Mẹ cho ăn → HẾT ĐÓI → valence: { L1 nutrition: ++ }
    → Dẫm gai → ốm nhiều ngày → valence: { L0: ---, gai = threat }
    → Bật lửa nổ → đau + shock → valence: { L0: ---, bật lửa = threat }
    → = Nguồn CHÍNH XÁC NHẤT — body verify trực tiếp
    → = NHƯNG chậm (phải trải nghiệm mới biết)
    → 🟢 Classical conditioning: direct experience → valence formation (Pavlov, LeDoux)

  ② OBSERVED EXPERIENCE — quan sát người khác:

    → Thấy bạn bị chó cắn → valence chó: { L0 safety: - }
    → Thấy mẹ nấu ăn ngon → valence bếp: { L1: + }
    → = Self-Pattern-Match (Agent.md) đọc state người khác → infer valence
    → = NHANH hơn direct experience (không cần bị cắn để biết chó nguy hiểm)
    → = NHƯNG kém chính xác (SPM ≈ 10-30% intensity, có thể bias)
    → 🟢 Observational learning: Bandura 1977 (modeling)
    → 🟢 Social referencing: infants look to caregiver for valence cues (Sorce 1985)

  ③ SCHEMA INHERITANCE — thừa kế từ cộng đồng:

    → Mẹ nói "dao nguy hiểm" → valence: { L0 safety: - } (chưa cần bị cắt)
    → Cộng đồng nói "firefighters are heroes" → valence lính cứu hỏa: { trust: +, L0 safety: + }
    → Tôn giáo: "Thiên Chúa yêu thương" → valence God: { ALL: ++ }
    → Bố mẹ: "không học thì sau này vất vả" → valence "không học": { threat }
    → = NHANH NHẤT (không cần trải nghiệm hay quan sát)
    → = NHƯNG có thể SAI (schema inherit ≠ reality verify)
    → = TẠI SAO tuyên truyền WORK: install valence TRƯỚC khi verify
    → = TẠI SAO positive childhood → default valence positive cho "người"
    → 🟢 Cultural transmission of fear: Rachman 1977 (3 pathways)
    → 🟢 Evaluative conditioning via verbal instruction (De Houwer 2007)

  ④ CONTEXT INFERENCE — suy luận từ context:

    → Quả bom trong tay đồng đội: { positive }
    → Quả bom trong tay kẻ thù: { extreme negative }
    → Bụi cây trong công viên: { neutral }
    → Bụi cây trong chiến trường: { threat }
    → = Cùng entity, khác context → khác valence
    → = Logic/Modeling mode tính toán: "trong context NÀY, entity NÀY có ý nghĩa gì?"
    → 🟡 Context-dependent valence = framework framing of established phenomenon


  ĐỘ TIN CẬY vs TỐC ĐỘ — TRADE-OFF:

    ┌──────────────────────────┬────────────────┬──────────────┐
    │ Nguồn                     │ Tốc độ          │ Độ chính xác  │
    ├──────────────────────────┼────────────────┼──────────────┤
    │ ① Direct experience       │ Chậm nhất      │ Cao nhất      │
    │ ② Observed experience     │ Trung bình     │ Trung bình    │
    │ ③ Schema inheritance      │ Nhanh nhất     │ Thấp nhất     │
    │ ④ Context inference       │ Tùy context    │ Tùy chunks    │
    └──────────────────────────┴────────────────┴──────────────┘

    → Evolutionary logic: "rắn nguy hiểm" inherit NHANH > tự bị cắn rồi biết
    → Trade-off: nhanh → có thể sai. Chậm → chính xác hơn nhưng cost cao.
    → 🟢 Prepared learning: biologically prepared associations (Seligman 1971)


VALENCE UPDATE — 3 LOẠI:

  ① REINFORCEMENT — valence MẠNH thêm:
    → Mẹ cho ăn 1000 lần → valence { L1: ++ } compiled CỰC SÂU
    → Bạn thân giúp đỡ nhiều năm → valence { trust: ++++ }
    → = Lặp lại consistent → valence COMPILE thành schema sâu
    → = Khó thay đổi vì đã anchored

  ② REVISION — valence THAY ĐỔI DẦN:
    → Dao: lần đầu cắt tay { L0: -- } → học cách dùng { L1: ++ dần override L0: -- }
    → = Domain feedback KHÁC valence hiện tại → body adjust DẦN
    → Tốc độ revision tùy: intensity × frequency × recency

  ③ VIOLENT FLIP — valence BỊ ĐẢO NGƯỢC:
    → Bạn thân phản bội: trust++++ → trust---- (FLIP)
    → Phát hiện sư thầy tham nhũng: valence chùa flip
    → = CỰC HIẾM nhưng CỰC MẠNH — vì phá compiled schema
    → = Anchor-Schema.md §2: flip phá anchor → cascade collapse
    → 🟢 Betrayal trauma: Freyd 1996


  TỐC ĐỘ UPDATE — 3 yếu tố:

    INTENSITY: feedback mạnh → update nhanh
      Bị chó cắn (đau mạnh) → valence update NGAY 1 lần
      Bạn hơi chậm trả lời tin nhắn → update RẤT CHẬM

    FREQUENCY: feedback lặp lại → update tích lũy
      Mẹ cho ăn MỖI NGÀY → valence compile RẤT SÂU
      Gặp người lạ 1 LẦN → valence RẤT NÔNG

    RECENCY: feedback GẦN ĐÂY ảnh hưởng nhiều hơn
      Bạn giúp hôm qua → valence tươi
      Bạn giúp 5 năm trước → valence MỜ DẦN (trừ khi đã compile sâu)


  ⚠️ BIAS TRONG UPDATE:

    → Negativity bias: negative feedback → update NHANH hơn positive
      (evolutionary: bỏ qua threat = chết > bỏ qua reward = mất cơ hội)
    → Confirmation bias: valence hiện tại → filter feedback cho match
      (ghét ai → chú ý hành vi xấu → ghét thêm → loop)

    🟢 Negativity bias: robust finding (Baumeister et al. 2001)
    🟢 Confirmation bias: established (Nickerson 1998)
```

---

## §4 — VALENCE PROPAGATION QUA SCHEMA CHAIN

> **Đây là concept MỚI quan trọng nhất của file này.**
> Valence.md cũ mô tả valence PER-ENTITY.
> Section NÀY mô tả valence TRUYỀN QUA NETWORK giữa các schemas.

```
🔴 HYPOTHESIS — concept mới, logic consistent với established research,
    chưa formalize trong literature dưới tên "valence propagation"

⭐ CORE INSIGHT:

  Framework đã có (Schema.md §1):
    Schema = CHUNKS + LINKS + PURPOSE
    Chunks = atoms. Links = connections GIỮA atoms. Purpose = function.

  Valence.md cũ mô tả:
    Mỗi entity có 1 valence profile → per-entity assessment

  NHƯNG: entities KHÔNG tồn tại cô lập.
    Entities LINK VỚI NHAU qua schema network.
    Và valence TRUYỀN qua những links đó.


  VÍ DỤ ĐƠN GIẢN:

    Entity "toán" — có feed body-base trực tiếp không?
    → KHÔNG. Ngồi làm toán: mệt (L1-), chán có thể (L3-).
    → Vậy valence lẽ ra NEGATIVE.
    → NHƯNG nhiều học sinh vẫn làm toán. Tại sao?

    Vì "toán" LINK tới chain:
      toán → điểm tốt → đại học → việc tốt → lương → body-base L1 feed
    
    Valence positive từ CUỐI chain (body-base feed)
    TRUYỀN NGƯỢC qua từng node:
      lương (+++) → việc tốt (++) → đại học (+) → điểm tốt (+) → toán (+)
    
    = Toán có valence positive KHÔNG VÌ toán trực tiếp feed body
    = MÀ VÌ toán LINK tới chain kết thúc ở body-base feed
    = Valence propagation qua schema chain.


  VÍ DỤ PHỨC TẠP:

    Entity "giấu người Do Thái" (gia đình Hà Lan trong WWII, 🟢 documented):
    → Miep Gies và gia đình giấu Anne Frank + 7 người trong 2 năm
    → L0 cost TRỰC TIẾP: bị phát hiện = TỬ HÌNH. L1 cost: bớt thức ăn, chỗ ở
    → Vậy per-entity valence: CỰC NEGATIVE (threat L0)
    → NHƯNG họ vẫn giấu. Tại sao?

    Vì "giấu người Do Thái" LINK tới NHIỀU chains SONG SONG:

      Chain 1 (empathy): họ sợ hãi, đói → giấu → họ an toàn → empathy reward
      Chain 2 (identity): "tôi là người đứng đắn" → identity confirm → reward
      Chain 3 (anchor): moral schema "bảo vệ người vô tội" → serve Anchor-Schema
      Chain 4 (status): nhóm kháng chiến biết → solidarity → connection reward

    4 chains positive > L0/L1 cost (dù cost = tử hình!)
    → Net valence: vẫn POSITIVE ở body level → drive "giấu"
    → Body chấp nhận RISK L0 vì TỔNG reward từ 4 chains + anchor CỰC MẠNH

    PFC biết: "vì đó là điều đúng đắn" (it was the right thing to do)
    PFC KHÔNG biết: body đang tính 4 reward chains
    = Valence propagation INVISIBLE cho PFC
    🟢 Miep Gies khi được hỏi luôn nói: "I did what anyone would have done"
       = Classic PFC confabulation — body computed 4 chains, PFC reports 1 simple reason


⭐ 4 CƠ CHẾ PROPAGATION:

  ① FORWARD PROPAGATION (learning path):

    Body-base need → tìm path → action → reward → path COMPILE
    
    Ví dụ:
      Đói → tìm quán → ăn → hết đói → "quán này tốt" (compile)
      Mệt → nằm → ngủ → tỉnh → "giường = recovery" (compile)
    
    = Đây là CƠ CHẾ CƠ BẢN NHẤT — body TỰ TÌM path tới reward
    = Mỗi path thành công → COMPILE → lần sau TỰ ĐỘNG fire
    = 🟢 Operant conditioning: Thorndike's Law of Effect (1898)
    = 🟢 Reinforcement learning: Sutton & Barto 1998

  ② BACKWARD PROPAGATION (reward spread):

    Reward ở cuối chain → valence positive TRUYỀN NGƯỢC qua từng node

    Ví dụ:
      Lương (reward) → job (positive) → đại học (positive) → toán (positive)
      = Toán có valence positive VÌ nó nằm trên đường tới reward

    Cơ chế:
      → Body experience: toán → ... → reward. Toán = PREDICTOR of reward.
      → Qua lặp lại (hoặc schema install): toán ĐÃ associate với reward chain
      → = Toán TỰ NÓ trigger 1 phần reward anticipation (dopamine)
      → = Feeling.md v2.0 §6: dopamine = wanting/salience, không phải reward itself

    🟢 Conditioned reinforcement: neutral stimulus → associated with reinforcer
       → acquires reinforcing value (Skinner, token economy)
    🟢 Temporal difference learning: reward prediction propagates backward
       (Schultz 1997, dopamine neurons)
    🟡 "Valence propagation" as explicit model = framework formalization

  ③ LATERAL PROPAGATION (generalization):

    Entity tương tự CŨNG nhận valence — dù chưa trải nghiệm trực tiếp

    Ví dụ NEGATIVE:
      1 con chó cắn → SỢ con chó đó → sợ TẤT CẢ chó (category)
      → sợ NGƯỜI NUÔI chó (associated entity) → ghét KHU VỰC có chó
      = Valence LAN NGANG qua similarity + association

    Ví dụ POSITIVE:
      Tuổi thơ: mẹ tốt + bố tốt + hàng xóm tốt + thầy cô tốt
      → Valence positive cho "người" (category)
      → Gặp người lạ → default valence positive → approach → sẵn sàng giúp
      = POSITIVE overgeneralization — CÙNG CƠ CHẾ với negative

    ⚠️ ASYMMETRY:
      Negative lateral: NHANH + RỘNG (1 con chó cắn → sợ mọi chó)
      Positive lateral: CHẬM + HẸP (cần NHIỀU experience positive mới generalize)
      → Evolutionary logic: false positive threat > false negative threat
      → = Negativity bias trong propagation (consistent với §3 update bias)

    🟢 Stimulus generalization: Pavlov, Watson (Little Albert 1920)
    🟢 Overgeneralization in anxiety: Dunsmoor & Murphy 2015
    🟡 Positive overgeneralization = same mechanism: logical inference

  ④ INSTALL PROPAGATION (schema inheritance chain):

    Cộng đồng install TOÀN BỘ CHAIN sẵn, KHÔNG cần trải nghiệm

    Ví dụ:
      Bố mẹ install: "không học → vất vả → đau khổ"
      = Chain: không học → vất vả → body-base threat
      = Đứa trẻ CHƯA trải nghiệm "vất vả" nhưng chain ĐÃ có
      = Valence "không học" = negative (propagated từ installed chain)

      Tôn giáo install: "sống đạo đức → Thiên Đàng → hạnh phúc vĩnh cửu"
      = Chain: đạo đức → Thiên Đàng → reward vĩnh cửu
      = TOÀN BỘ chain installed qua ritual + community reinforce
      = Không cần verify → unfalsifiable → chain KHÔNG BAO GIỜ bị phá

      Patriotic install (MỌI quốc gia đều có):
        "Nation → Flag → Military → Freedom → Safety"
        = Chain: Nation (+++) → Flag (++) → Soldiers (+) → tất cả linked positive
        = Install qua education + media + national holidays + ritual
        VD: WWII Mỹ — "Uncle Sam Wants YOU" poster → install chain: enlist → serve nation → freedom
        VD: WWII Anh — "Keep Calm and Carry On" → install chain: endure → nation survives → safety
        VD: Bất kỳ quốc gia nào: quốc ca + chào cờ mỗi sáng → patriotic chain compile SÂU

    Đặc điểm install propagation:
      → NHANH NHẤT: không cần direct experience
      → CÓ THỂ install chain DÀI (5+ nodes) trong thời gian ngắn
      → CÓ THỂ SAI: chain content chưa verify
      → NHƯNG: evolutionary effective (inherit "rắn nguy hiểm" > tự bị cắn)
      → NGUY HIỂM khi bị weaponize: tuyên truyền, cult, extremism

    🟢 Cultural transmission: Boyd & Richerson 1985
    🟢 Indoctrination effects: established in social psychology
    🟡 "Install propagation" as explicit model = framework term


⭐ PROPAGATION DYNAMICS:

  4 cơ chế KHÔNG hoạt động riêng lẻ — chúng TƯƠNG TÁC:

    Forward tìm path → Backward reinforce path → Lateral expand scope
    Install provide starting chains → Forward/Backward VERIFY hoặc REJECT

    Ví dụ tích hợp (học sinh làm toán):
      Install: bố mẹ nói "học = tương lai" (④ install chain)
      Forward: làm bài → được điểm → nhẹ nhõm (① forward find reward)
      Backward: điểm tốt → valence toán tăng (② backward propagate)
      Lateral: toán tốt → "lý cũng tốt" (③ lateral to similar subject)
      
      HOẶC Forward FAIL: làm toán → sai → bị mắng → dissonance
      → Chain INSTALLED ("học = tương lai") CONFLICT với chain EXPERIENCED ("toán = đau")
      → Body phải resolve: chain nào MẠNH hơn?
      → Nếu install chain trust > experience pain → tiếp tục
      → Nếu experience pain > install trust → bỏ cuộc, ghét toán

  🟢 Spreading activation: Collins & Loftus 1975
     (Concepts in memory activate related concepts — established)
  🟢 Associative network models: Anderson 1983
  🟡 4-mechanism model = framework categorization
```

---

## §5 — 5 ĐẶC TÍNH CỦA CHAIN

```
🔴 HYPOTHESIS — framework formalization, logic consistent

  Valence chain (§4) có 5 đặc tính quyết định behavior:


  ① CHAIN LENGTH → VALENCE DECAY + PFC ACCURACY DECREASE:

    Chain NGẮN:
      Gai → đau chân → body-base L0
      Length = 1. Valence MẠNH. PFC trace 100%.
      "Tôi sợ vì bị đau" — PFC biết CHÍNH XÁC.

    Chain TRUNG BÌNH:
      Toán → điểm → đại học → việc tốt → lương → body-base
      Length = 4. Valence YẾU hơn ở đầu chain (toán).
      PFC trace ~70%. "Tôi học vì tương lai" — đúng nhưng THIẾU detail.

    Chain DÀI:
      Moral schema → "bảo vệ người vô tội" → giấu Anne Frank → empathy + identity + anchor
      Length = 4+, multi-branch. Valence PHỨC TẠP.
      PFC trace ~30%. "Vì đó là điều đúng" — đúng surface, THIẾU mechanism.

    Chain INVISIBLE:
      Hardware fit + chunk match → Goldilocks → VTA delta → opioid
      PFC KHÔNG THẤY chain (hardware-level).
      PFC trace ~10%. "Tôi thích toán" — label, KHÔNG phải explanation.

    NGUYÊN TẮC:
      → Chain LENGTH tăng → valence tại đầu chain GIẢM (decay)
      → Chain LENGTH tăng → PFC accuracy GIẢM (more confabulation)
      → Chain LENGTH tăng → DỄ BỊ ĐỨT (nhiều links = nhiều điểm fail)

    🟢 Goal gradient effect: Hull 1932, stronger near goal
    🟢 Temporal discounting: delay → value decrease (Ainslie 1975)
    🟡 PFC accuracy ≈ f(1/chain_length): framework inference


  ② CHAIN TRUST → PROPAGATION STRENGTH:

    Mỗi link trong chain có TRUST level riêng.
    Propagation strength ≈ PRODUCT of trust at each link.

    Ví dụ HIGH trust chain:
      Bố mẹ nói "học = tương lai" (trust bố mẹ: 90%)
      Thầy cô confirm "đúng" (trust thầy: 80%)
      Bạn bè cũng học (social proof: 70%)
      → Chain trust ≈ high → valence "học" propagate MẠNH

    Ví dụ LOW trust chain:
      Người lạ nói "invest bitcoin = giàu" (trust: 20%)
      → Chain trust LOW → valence "invest" propagate YẾU
      → NHƯNG nếu 100 người nói (social amplify) → trust TĂNG
      → = Tại sao scam + hype WORK: quantity override quality of trust

    ĐẶC BIỆT — Trust = 0 tại 1 link → CHAIN ĐỨT:
      Install chain: "học = tương lai tốt"
      Experience: 4 năm đại học → thất nghiệp
      → Trust "đại học → việc tốt" link = COLLAPSE
      → Toàn bộ chain phía trước link đó BỊ ẢNH HƯỞNG
      → "Học vô ích" = chain đứt → valence "học" flip negative

    → Anchor-Schema.md §2: Trust ≥ Cost → hold; Trust < Cost → collapse
    → 🟡 Chain trust = product of link trusts: framework model


  ③ PARALLEL CHAINS → ADDITIVE:

    NHIỀU chains CÓ THỂ connect entity → body-base CÙNG LÚC.
    Valence = TỔNG từ tất cả chains.

    Ví dụ — Gia đình Hà Lan giấu người Do Thái (WWII):
      Chain 1: empathy reward (họ an toàn) → opioid
      Chain 2: identity confirm ("tôi = người đứng đắn") → reward
      Chain 3: moral anchor-schema service → reward
      Chain 4: resistance network solidarity → connection reward
      → 4 chains ADDITIVE → valence CỰC MẠNH → override L0 threat (tử hình)

    Ví dụ — "Học sinh làm toán":
      Chain a: "tương lai tốt" (install) → positive
      Chain b: "sợ bị mắng" (threat) → avoid negative
      Chain c: hardware fit + mastery → intrinsic reward
      Chain d: "toán thú vị" (self-label) → reinforce
      → 4 chains PARALLEL → drive MẠNH → làm bài

    ⭐ QUAN TRỌNG:
      Single chain YẾU → drive YẾU → dễ bỏ
      Multiple parallel chains → drive MẠNH → khó bỏ
      = Tại sao "đam mê" = nhiều chains converge vào 1 activity
      = Tại sao "nghiện" = chains lock → khó thoát
      = Tại sao "cho đi" CÓ 4 nguồn reward (Emergent-Patterns §5)


  ④ CONFLICTING CHAINS → MIXED VALENCE:

    2+ chains NGƯỢC HƯỚNG cho cùng 1 entity.

    Ví dụ — "Mẹ":
      Chain positive: cho ăn → comfort → protection → L1++ L0++
      Chain negative: ép học → mất tự do → autonomy-- L3-
      → CÙNG entity "mẹ", 2 chains ngược → YÊU + GHÉT cùng lúc
      → = Mixed valence (§2) VÌ conflicting chains

    Ví dụ — "Công việc":
      Chain positive: lương → security → L1++
      Chain negative: stress → mệt → health- → L0- L1-
      → "Cần việc nhưng ghét đi làm" = 2 chains conflict

    Ví dụ — "Biết nên học nhưng không muốn":
      Chain A: toán → tương lai → body-base (install, positive)
      Chain B: toán → mệt → body discomfort (direct, negative)
      → PFC biết chain A (verbalize được: "nên học")
      → Body FEEL chain B (mệt, chán — direct experience)
      → Conflict: PFC nói "nên" vs body nói "không muốn"

    RESOLUTION:
      → Chain nào MẠNH hơn → drive theo hướng đó
      → Mạnh = trust × length_decay × intensity × number_of_parallel_chains
      → = Drive.md: action = EMERGENT OUTPUT từ tổng hợp tất cả


  ⑤ INVISIBLE CHAINS → PFC CONFABULATION:

    Chain INVISIBLE cho PFC khi:

    a) Chain COMPILED SÂU (auto fire, không qua PFC):
       → "Thấy chó → SỢ" = compiled chain, body fire trước PFC biết
       → PFC: "Tôi sợ chó" — biết OUTPUT nhưng chain ĐÃ fire xong

    b) Chain HARDWARE-LEVEL (hormone, empathy, VTA — PFC không access):
       → "Tôi yêu em" — hormone + body chemistry + schema
       → PFC KHÔNG access hormone computation
       → PFC: "Vì em đẹp, em thông minh" — confabulation

    c) Chain QUÁ DÀI (PFC chỉ thấy node gần nhất):
       → "Tôi thích từ thiện" — PFC thấy "thích" (node gần nhất)
       → Chain thật: empathy + identity + status + connection (4 chains invisible)
       → PFC: "Vô tư thôi" — vì không thấy chains phía sau

    d) Chain MULTI-BRANCH (quá phức tạp để PFC track):
       → Gia đình giấu Anne Frank: 4 chains × multiple links each
       → PFC chỉ track 1-2 chains đơn giản nhất
       → PFC: "Vì đó là điều đúng" — đúng 1 chain, bỏ sót 3

    → Chi tiết: §7 PFC Blindness

    🟢 Confabulation: Nisbett & Wilson 1977
    🟡 5 đặc tính chain = framework formalization
```

---

## §5b — TẠI SAO CHAIN DÀI TỒN TẠI: 4 Tầng Cơ Chế

> **Câu hỏi**: Vì sao cá nhân VÔ THỨC hình thành valence chain xa vời kỳ quái?
> Toán → điểm → đại học → việc → lương → body-base (4 links).
> Moral schema → bảo vệ người vô tội → giấu Anne Frank → 4 chains reward (4+ links).
> Einstein → vật lý → mystery → decades chunks → body fire (compiled depth).
>
> Chain dài KHÔNG phải feature được "thiết kế".
> Chain dài = EMERGENT từ 4 tầng cơ chế chồng lên nhau.

```
🟡 FRAMEWORK SYNTHESIS — logic consistent, dựa trên established mechanisms


⭐ 4 TẦNG CƠ CHẾ TẠO + GIỮ CHAIN DÀI:

  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG  │ VAI TRÒ      │ CƠ CHẾ                    │ CONFIDENCE │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  1    │ EXIST        │ Chunk substrate tự nhiên  │ 🟢         │
  │       │ Chain tồn tại│ tạo chain qua connections │            │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  2    │ EXTEND       │ 4 cơ chế valence          │ 🟢🟡      │
  │       │ Chain kéo dài│ propagation (§4)           │            │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  3    │ FIT          │ Pyramidal compression cho │ 🟢🟡      │
  │       │ Chain fit PFC│ chain dài vào 4±1 chiều   │            │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  4    │ FILTER       │ Group selection giữ lại   │ 🟡🔴      │
  │       │ Chain survive│ cá nhân có chain dài      │            │
  └───────┴──────────────┴───────────────────────────┴────────────┘


  TẦNG 1 — CHUNK SUBSTRATE TỰ NHIÊN TẠO CHAIN (EXIST):

    Chunk.md v2.0 §3: 4 loại connection GIỮA chunks:
      Type 1: Shared Contamination — neurons chung fire lẫn nhau (VÔ THỨC, automatic)
      Type 2: Aha Moment — DMN incubation → sudden burst link
      Type 3: Meta-chunk Compile — fire cùng nhau nhiều lần → merge thành 1 unit
      Type 4: Static Logical Linking — PFC chủ đích hold + check

    Chain dài KHÔNG ĐƯỢC "thiết kế". Nó EMERGE từ:
      → Type 1: spreading activation tự lan theo TẤT CẢ links (Collins & Loftus 1975)
      → Type 3: chunks → meta-chunks → schemas → hierarchy (Hebb 1949)
      → 4 types = ECOSYSTEM (§3.3): mỗi type feed type khác

    QUAN TRỌNG:
      → Chunk system KHÔNG CÓ giới hạn "chỉ link gần"
      → Mọi thứ co-fire → CÓ THỂ link → chain POTENTIAL = vô hạn
      → Chain dài = side effect TẤT YẾU của cách chunk compile
      → KHÔNG CẦN cơ chế riêng cho "tạo chain dài"

    🟢 Spreading activation: Collins & Loftus 1975
    🟢 Hebbian learning: Hebb 1949
    🟢 Associative network models: Anderson 1983


  TẦNG 2 — VALENCE PROPAGATION KÉO DÀI CHAIN (EXTEND):

    §4 đã mô tả 4 cơ chế propagation. Vai trò cho chain DÀI:

      ① Forward: body TỰ TÌM path tới reward → path càng xa = chain càng dài
      ② Backward: reward ở cuối → valence spread NGƯỢC → "kéo dài" chain về phía gốc
         → 🟢 Temporal difference learning (Schultz 1997)
      ③ Lateral: mở RỘNG chain sang entities tương tự (category generalize)
      ④ Install: cộng đồng install chain DÀI (5+ nodes) NGAY LẬP TỨC
         → KHÔNG cần trải nghiệm → chain dài form trong 1 câu nói

    ĐẶC BIỆT — Install Propagation (④) giải thích chain dài ở TRẺ EM:
      → Trẻ chưa có đủ direct experience để build chain dài
      → NHƯNG bố mẹ install: "học → tương lai → sung sướng" = chain 3+ links
      → Cộng đồng install: "sống tốt → Thiên Đàng" = chain unfalsifiable
      → = Chain dài CÓ THỂ xuất hiện TRƯỚC khi vô thức kịp compile

    DYNAMICS:
      → Forward/Backward VERIFY chain installed
      → Chain installed mà forward CONFIRM → compiled SÂU → dài + bền
      → Chain installed mà forward FAIL → đứt → valence flip
      → = §4 Propagation Dynamics đã mô tả interaction này


  TẦNG 3 — PYRAMIDAL COMPRESSION CHO CHAIN DÀI FIT VÀO PFC (FIT):

    ⚠️ QUAN TRỌNG — ĐÍNH CHÍNH:
      → "PFC lớn hơn → chain dài hơn" = SAI
      → 🟢 Brain size vs IQ: tương quan RẤT YẾU (~0.24, ~6% variance)
         (Pietschnig 2015, meta-analysis 148 studies)
      → PFC luôn chỉ hold 4±1 dimensions (physics limit — interference)
         (🟢 Cowan 2001)

    VẬY chain dài FIT vào PFC BẰNG CÁCH NÀO?

      → Pyramidal compression (PFC-Analysis.md):
        4 chunks → compile → 1 meta-chunk
        4 meta-chunks → compile → 1 super-meta
        → 4×4×4 = 64 thông tin gốc compressed vào 1 slot PFC

      → "Nhìn 4 thứ nhưng THẤY cả vũ trụ" (expert) — PFC-Analysis.md
      → "Nhìn 4 thứ chỉ THẤY 4 thứ" (novice)
      → CÙNG 4±1 dimensions, KHÁC compression quality

    INSIGHT — Chain dài là sản phẩm của VÔ THỨC, không phải PFC:
      → Vô thức compile chunks → stack → pyramidal → compressed
      → Mỗi "link" mà PFC thấy = thực ra meta-chunk chứa hàng chục links
      → PFC thấy chain "ngắn" (3-4 items) → thực ra = chain compiled SÂU
      → Einstein "thấy" E=mc² = 1 meta-chunk. Bên trong = decades compiled.

    HỆ QUẢ:
      → Chain dài KHÔNG cần "PFC lớn hơn" hay "PFC capacity cao hơn"
      → Chain dài cần VÔ THỨC COMPILE ĐỦ SÂU
      → = Observed Capacity (PFC-Analysis.md):
        OBSERVED = Hardware Ceiling × Vô Thức Quality × Cortisol State × Context Fit
      → Yếu tố ② Vô Thức Quality = QUYẾT ĐỊNH cho chain dài
      → CAN THIỆP ĐƯỢC: giáo dục + experience + compile time (ngủ đủ)

    TẠI SAO chain dài KHÁC NHAU giữa các cá nhân:
      → Trẻ em: chunks chưa đủ compiled → chain ngắn → valence trực tiếp
      → Expert: chunks compiled sâu + pyramidal → chain dài trong domain
      → Đổi domain: chunks mới chưa compile → chain ngắn lại
      → = Chain dài = f(vô thức quality), KHÔNG PHẢI f(PFC size)

    🟢 Chase & Simon 1973: expert chess 50,000+ chunk patterns
    🟢 Neural efficiency: người giỏi fire ÍT hơn (Haier 1992, Neubauer & Fink 2009)
    🟡 Pyramidal compression model: framework synthesis từ Cowan + Chase & Simon
    🟡 Chain length = f(compile depth): framework inference


  TẦNG 4 — GROUP SELECTION FILTER (FILTER):

    Giả thiết: chọn lọc tự nhiên ở cấp TẬP THỂ giữ lại gene cho chain dài.

    CƠ CHẾ (Empathy.md §7):
      Nhóm CÓ chain dài:
        → Empathy: SPM detect người khác thiếu → share → nhóm khỏe
        → Đầu tư dài hạn: install chain "học = tương lai" → next gen giỏi hơn
        → Hợp tác: chain "giúp đồng minh → an toàn cùng" → nhóm mạnh
        → Truyền kiến thức: install propagation → build collective knowledge

      Nhóm KHÔNG CÓ chain dài (chỉ valence trực tiếp):
        → Chỉ react theo per-entity immediate valence
        → Ít empathy (SPM yếu → không share khi thừa)
        → Ít đầu tư dài hạn (chain ngắn → chỉ thấy cost trước mắt)
        → Ít hợp tác (không thấy chain "giúp → được giúp lại")
        → → Nhóm YẾU HƠN → bị loại bởi chiến tranh, thiên nhiên, cạnh tranh

    🟢 Kin selection: Hamilton 1964
    🟢 Reciprocal altruism: Trivers 1971
    🟡 Group selection: Wilson 2007 (debated nhưng logic consistent)
    🔴 "Group selection cho chain dài" = framework hypothesis, chưa test

    ⚠️ PHÂN BIỆT CAUSE vs FILTER:
      → Tầng 1-3 = CAUSE (tạo ra chain dài ở cấp cá nhân)
      → Tầng 4 = FILTER (giữ lại chain dài ở cấp tập thể)
      → Chain dài EMERGE từ chunk architecture (Tầng 1)
      → Evolution KHÔNG "cố tình tạo" chain dài
      → Evolution CHỈ "giữ lại" cá nhân/nhóm CÓ chain dài
      → = Cause ≠ Filter — distinction quan trọng

    ⚠️ KHÔNG CẦN group selection để giải thích chain dài:
      → Tầng 1-3 ĐÃ ĐỦ giải thích WHY chain dài tồn tại ở cấp cá nhân
      → Tầng 4 giải thích thêm WHY chain dài PHÁT TRIỂN MẠNH qua evolution
      → = Tầng 4 BỔSUNG, không phải THAY THẾ Tầng 1-3


  ⭐ TRADE-OFF NỀN TẢNG — CHAIN DÀI = FEATURE, KHÔNG PHẢI BUG:

    Chain dài CÓ HẠN CHẾ RÕ RÀNG cho cá nhân:

    ① PFC BLIND → confabulate:
      → Share "vô tư" → PFC KHÔNG BIẾT tại sao → không thể self-correct
      → "Tôi thích từ thiện" = PFC label cho 4 invisible chains (§7)
      → Hại: không biết mechanism → dễ bị exploit (manipulation, guilt-trip)

    ② TRAUMA chain compiled sâu → PFC đoán sai gốc:
      → Khó chịu nền (cortisol drift) → PFC thấy "khó chịu" nhưng KHÔNG trace được chain
      → PFC đoán: "chắc do công việc" / "do thời tiết" / "do người yêu"
      → Đoán SAI → fix SAI → chain vẫn còn → loop khó chịu kéo dài
      → = §5 ⑤c: chain quá dài → PFC chỉ thấy node gần nhất

    ③ UNFALSIFIABLE chains → sacrifice phi lý:
      → Tin thần linh (not real) + chain "tử vì đạo → Thiên Đàng → reward vĩnh cửu"
      → Chain KHÔNG BAO GIỜ bị phá (no verification possible)
      → Cá nhân sacrifice L0 (chết) cho chain content KHÔNG CÓ THẬT
      → = §6 D2 + §8 Nguyên tắc 1: effectiveness ≠ truthfulness

    NHƯNG — xét XÁC SUẤT TỔNG THỂ, chain dài = NET POSITIVE:

    ┌──────────────────────┬────────────────────────────────────────┐
    │ Hại (cá nhân, ít)    │ Lợi (tập thể, nhiều)                  │
    ├──────────────────────┼────────────────────────────────────────┤
    │ PFC blind → bị       │ Empathy → share khi thừa → nhóm khỏe │
    │ exploit đôi khi      │ (Empathy.md §7)                       │
    ├──────────────────────┼────────────────────────────────────────┤
    │ Trauma chain →       │ Deferred investment → đầu tư dài hạn  │
    │ khó chịu kéo dài    │ → next gen giỏi hơn                   │
    ├──────────────────────┼────────────────────────────────────────┤
    │ Unfalsifiable belief │ Cooperation → chain "giúp → được giúp" │
    │ → sacrifice cá nhân │ → nhóm mạnh hơn                       │
    ├──────────────────────┼────────────────────────────────────────┤
    │ Confabulate lý do    │ Knowledge transfer → install chain    │
    │ → self-correct chậm │ → collective learning nhanh            │
    └──────────────────────┴────────────────────────────────────────┘

    → P(benefit cho nhóm) >> P(harm cho cá nhân cụ thể)
    → Evolution giữ lại vì NET POSITIVE ở cấp population

    TƯƠNG TỰ — immune system analogy:
      → Immune system đôi khi tấn công nhầm cơ thể (autoimmune)
      → Nhưng P(chống infection thành công) >> P(autoimmune)
      → → Evolution giữ immune system dù có side effect
      → Chain dài CÙNG LOGIC: đôi khi PFC blind gây hại cá nhân
      → Nhưng P(empathy + cooperation + deferred investment) >> P(harm)
      → → Evolution giữ chain dài dù có trade-off

    🟢 Immune system trade-off: established evolutionary biology
    🟡 Chain dài as analogous trade-off: framework reasoning, logic consistent


  TÓM TẮT:

    Chain dài = EMERGENT, không phải DESIGNED:

      TẦNG 1: Chunk Substrate    → Chain EXIST (side effect tất yếu)
      TẦNG 2: Valence Propagation → Chain EXTEND (4 cơ chế + install)
      TẦNG 3: Pyramidal Compress  → Chain FIT vào PFC (quality, không size)
      TẦNG 4: Group Selection     → Chain SURVIVE qua evolution (filter)

    → = "Vì sao tôi vô thức có chain dài?"
      Vì chunk system CỦA BẠN tự nhiên tạo links (1),
      valence propagation kéo dài chúng (2),
      vô thức compile compress cho fit PFC (3),
      và evolution đã giữ lại gene này vì nhóm có chain dài mạnh hơn (4).
```

---

## §6 — CASES PHÂN TÍCH

```
🟡 CASES PHÂN LOẠI THEO 6 NHÓM — verify valence propagation model:


  ═══════════════════════════════════════════════════════════════
  NHÓM A — DIRECT CHAIN (ngắn, PFC trace được):
  ═══════════════════════════════════════════════════════════════

  A1) Dẫm gai → luôn đi dép:
    Chain: gai → đau chân → ốm nhiều ngày → body-base L0 threat
    Length: 1. Direct experience. 1 lần ĐỦ (intensity cực cao).
    Schema compile: "đất trống + chân trần = threat" → behavior: đi dép
    PFC accuracy: ~100%. "Vì bị ốm lần đó."
    = Per-entity valence, KHÔNG cần propagation model

  A2) Bật lửa nổ → sợ bật lửa:
    Chain: bật lửa → nổ → đau + shock → L0 threat
    Length: 1. Giống A1.
    = Object valence đơn giản, direct experience.


  ═══════════════════════════════════════════════════════════════
  NHÓM B — DEFERRED INVESTMENT (chain dài, trust-dependent):
  ═══════════════════════════════════════════════════════════════

  B1) Học sinh làm toán (4 khả năng song song):
    Chain a: toán → điểm → đại học → job → lương → L1 (install, length 4)
    Chain b: không học → bị mắng → L0 threat (install, length 1-2)
    Chain c: hardware fit → Goldilocks → VTA → reward (invisible, intrinsic)
    Chain d: "toán thú vị" = PFC label SAU → reinforce chain c
    → 4 chains PARALLEL, mỗi cái different mechanism
    → PFC biết: chain a ("vì tương lai") + chain b ("sợ bị mắng")
    → PFC KHÔNG biết: chain c (hardware fit) + chain d (label ≠ cause)

  B2) Jensen Huang — 30 năm Imagine-Final:

    🟢 FACTS (public record):
      - Sinh Đài Loan, 9 tuổi sang Mỹ, vào reform school (không phải boarding school)
      - Co-founded NVIDIA 1993, gần phá sản nhiều lần (NV1 chip fail)
      - Nói: "If I knew how hard it was, I wouldn't have started NVIDIA"
      - ~30 năm từ startup → tỷ phú → AI revolution leader
      - Vẫn drive mạnh ở tuổi 60+, vẫn CEO, vẫn hands-on

    🟡 FRAMEWORK INFERENCE (dựa trên facts, nhưng internal state = chỉ ông ấy biết):
    
    Giai đoạn 1 (khởi đầu):
      Chain: Anchor-Schema nào đó (có thể identity-driven, có thể mastery-driven)
      Length: LONG + DEFERRED. Trust: HIGH (chunks kỹ thuật tích lũy + co-founders align)
      Body-base feed: CHƯA CÓ trực tiếp. Body chấp nhận vì Anchor trust > cost.
    Giai đoạn 2 (GPU Game thành công):
      Chain VERIFY: thành công → tiền → L1 feed → trust TĂNG
      Backward propagation: reward → NVIDIA positive → Anchor CONFIRM
    Giai đoạn 3 (tỷ phú, 60+ tuổi):
      Body-base ĐÃ đủ. Drive vẫn mạnh. Tại sao?
      → Khả năng: Anchor-Schema EVOLVE content ("legacy"? "AI revolution"?)
      → + Intrinsic reward: mastery + novelty vẫn fire (hardware fit + chunk depth)
      → = Anchor-Schema có thể EVOLVE content mà GIỮ function

    ⚠️ CỤ THỂ internal schemas NÀO drive Jensen Huang = CHỈ ÔNG ẤY BIẾT.
    Framework chỉ có thể INFER từ observable behavior, KHÔNG phải đọc vị chính xác.
    = Minh họa cho §8 Nguyên tắc: schema network KHÔNG THỂ map chính xác từ bên ngoài.


  ═══════════════════════════════════════════════════════════════
  NHÓM C — MIRROR CHAIN ("cho đi", invisible multi-source):
  ═══════════════════════════════════════════════════════════════

  C1) Trẻ con giúp mẹ:
    Chain 1: Mẹ chăm → compiled deep valence mẹ: {++}
    Chain 2: Thấy mẹ mệt → Self-Pattern-Match → empathy dissonance
    Chain 3: Giúp mẹ → mẹ vui → empathy reward (opioid)
    Chain 4: "Mẹ hay làm thế" → reciprocity schema → identity
    PFC: "Vì mẹ hay giúp tôi" — biết chain 4, KHÔNG biết chain 2+3

  C2) Positive childhood → giúp đỡ người lạ "vô tư":
    Chain 1: Tuổi thơ positive → positive overgeneralize → "người = tốt" (lateral)
    Chain 2: Gặp người lạ → schema "tốt" fire → no threat → approach
    Chain 3: Giúp → họ improve → empathy reward
    Chain 4: Giúp → community see → status +
    Chain 5: Giúp → "tôi là người tốt" → identity confirm
    PFC: "Vô tư thôi" — KHÔNG biết 5 chains. Layer 7 label.

  C3) "Tôi thích từ thiện" (PFC không biết tại sao):
    = Case C2 nhưng schema ĐÃ compiled SÂU
    PFC chỉ thấy output "thích", không access mechanism
    Feeling.md v2.0 §2: Layer 6 (label) → Layer 7 (explanation 20-70%)
    "Thích" = label. "Vô tư" = explanation. CẢ HAI không phải mechanism.


  ═══════════════════════════════════════════════════════════════
  NHÓM D — SCHEMA INHERITANCE (installed chain, có thể unfalsifiable):
  ═══════════════════════════════════════════════════════════════

  D1) Gia đình Hà Lan giấu người Do Thái trong WWII (🟢 documented):
    Installed chains: Church/moral education → "bảo vệ người vô tội" → "đó là bổn phận"
    + Mirror chain: người Do Thái sợ hãi → giấu → họ an toàn → empathy reward
    + Identity: "tôi là người đứng đắn" (Miep Gies: "anyone would have done it")
    + Anchor-Schema: moral schema "không đứng nhìn kẻ ác giết người vô tội"
    + Connection: Dutch Resistance network → solidarity → belonging
    = Schema inheritance + empathy + identity + anchor + connection = 5 chains converge
    🟢 Yad Vashem ghi nhận ~28,000 "Righteous Among Nations" — ordinary people, same pattern

  D2) Tin Thiên Đàng → vượt khó → body-base VẪN feed:
    Installed chain: đạo đức → Thiên Đàng → reward vĩnh cửu
    UNFALSIFIABLE: không ai verify Thiên Đàng → chain KHÔNG BAO GIỜ bị phá
    ⭐ KEY INSIGHT: body-base VẪN feed dù chain content chưa verify:
      "Chịu khó làm việc" → kiếm sống → L1 feed
      "Sống đạo đức" → community accept → connection feed
      "Vượt khó" → mastery → L3 feed
    = Schema effectiveness ≠ Schema truthfulness
    = Body check OUTPUT (hành vi có feed không), KHÔNG check TRUTH (chain đúng không)
    PFC không cần question: vì body-base smooth → no dissonance → no trigger

  D3) "Giàu mới hạnh phúc" → đạt được → trống rỗng:
    Installed chain: giàu → "hạnh phúc" (promise ALL channels)
    Reality: giàu → L1 feed. NHƯNG đường đi sacrifice L1 comfort + connection
    → Đạt giàu → body CHECK: melody smooth? → NO (channels khác DEFICIT)
    → "Sao giàu rồi vẫn không hạnh phúc?" = PFC phát hiện MISMATCH
    = Imagine-Final-Evaluation.md: Mismatch quadrant
    ⭐ NHƯNG: người giàu MÀ giữ được relationship + health → KHÔNG trống rỗng
    = Cùng Imagine-Final, khác ĐƯỜNG ĐI → khác output body-base


  ═══════════════════════════════════════════════════════════════
  NHÓM E — MISLINK (cơ chế đúng, content sai):
  ═══════════════════════════════════════════════════════════════

  E1) Sát nhân máu lạnh:
    Hardware: OK (thủ đoạn phức tạp = chunks tốt + PFC hoạt động)
    Schema MISLINK: gây hại → CONTROL → mastery channel → reward
    Khả năng chain:
      Tuổi thơ bị abuse → "người = threat" → "bạo lực = cách resolve threat"
      Hoặc: identity "tôi = predator" compiled → Anchor-Schema → all behavior sync
      Hoặc: empathy ĐẢO NGƯỢC → thấy người khác đau → body reward (không phải dissonance)
    Reward khi giết: mastery (control) + identity confirm + threat resolution
    Reward khi đứng trước tòa: attention (status) + combat (mastery) + identity
    🟢 Serial killers: many report "power" and "control" feelings
    🟢 Hardware typically NOT broken: IQ average or above (Hickey 2013)
    🟡 Schema mislink as explanation = framework framing

  E2) Revenge phi lý (bỏ 200 triệu kiện cho 100 triệu):
    Chain analysis:
      L1 cost: -200M (financial loss)
      Chain 1: dissonance "công bằng" → resolve → RELIEF (+++)
      Chain 2: "kẻ xấu bị trừng phạt" → identity confirm → reward
      Chain 3: thấy kẻ lừa bị tù → Schadenfreude → ventral striatum → reward
    Net: chain 1+2+3 > L1 cost
    Body tính ĐÚNG theo valence system → PFC thấy "phi lý" vì PFC chỉ tính L1
    🟢 Schadenfreude: Takahashi et al. 2009 (ventral striatum activation)
    🟢 Costly punishment: Fehr & Gächter 2002 (humans punish at personal cost)


  ═══════════════════════════════════════════════════════════════
  NHÓM F — OVERGENERALIZE (lateral propagation):
  ═══════════════════════════════════════════════════════════════

  F1) Bị chó cắn → sợ mọi chó → ghét người nuôi chó:
    Step 1: 1 con chó → L0 threat (direct, 1 trial)
    Step 2: 1 con chó → TẤT CẢ chó (lateral, category generalize)
    Step 3: chó → NGƯỜI NUÔI chó (lateral, associated entity)
    = Valence propagation: direct → category → associated
    = Negative overgeneralize: NHANH, RỘNG (evolutionary safe)
    🟢 Phobia generalization: established pattern

  F2) Quân Nhật tấn công 1 người thân → thù toàn bộ quân đội:
    = F1 nhưng ở agent level + amplified bởi community schema inheritance
    1 lính Nhật → TẤT CẢ lính Nhật → quân đội Nhật → "kẻ thù"
    + Schema inheritance: cả cộng đồng reinforce → propagation CỰC MẠNH
    + Anchor-Schema "đuổi giặc" emerge → sync toàn bộ

  F3) Positive childhood → default trust người lạ:
    = POSITIVE overgeneralize (ngược với F1):
    Nhiều agents positive → category "người" = positive (lateral)
    → Gặp người lạ → default approach → sẵn sàng giúp
    = CÙNG CƠ CHẾ, khác hướng (positive vs negative)
    = NHƯNG: cần NHIỀU experience hơn (negativity bias asymmetry)
```

---

## §7 — PFC BLINDNESS + CONFABULATION

```
🟡 TẠI SAO PFC THƯỜNG KHÔNG BIẾT VALENCE CHAIN:

  Feeling.md v2.0 §2 mô tả 7 LAYERS — fidelity GIẢM DẦN:
    Layer 1: Raw body signal → 100% fidelity
    Layer 2: Integration → ~95%
    ...
    Layer 6: Labeling → 40-80%
    Layer 7: Explanation → 20-70% accuracy

  Valence chain hoạt động ở Layer 1-5 (body → integration → chunk match).
  PFC OBSERVE từ Layer 6 trở đi (label + explain).
  = PFC thấy OUTPUT (feeling), KHÔNG thấy MECHANISM (chain).
  = PFC phải EXPLAIN → bắt buộc tìm lý do → nếu chain invisible → CONFABULATE.


  3 CẤP ĐỘ PFC AWARENESS:

  ① PFC BIẾT (chain ngắn + direct + recent):
    "Tôi sợ gai vì bị ốm lần đó" — chain length 1, direct experience
    "Tôi thích quán này vì đồ ăn ngon" — length 1, direct
    Accuracy: ~80-100%
    = Hầu hết per-entity direct valence → PFC trace được

  ② PFC BIẾT MỘT PHẦN (chain trung bình + installed):
    "Tôi học vì tương lai" — chain length 4, installed
    → Đúng SURFACE, THIẾU detail (WHICH channels? Intrinsic reward nào?)
    "Tôi giúp mẹ vì mẹ hay giúp tôi" — chain 2-3, reciprocity
    → Đúng 1 chain, BỎ SÓT empathy + identity chains
    Accuracy: ~40-70%
    = PFC biết chain DỄ NHẤT, bỏ sót chains invisible

  ③ PFC KHÔNG BIẾT (chain invisible, hardware, compiled):
    "Tôi thích từ thiện" — PFC: "vô tư." Body: 4 chains reward.
    "Tôi đam mê vật lý" — PFC: "vì nó hay." Body: hardware + Goldilocks.
    "Tôi yêu em" — PFC: "vì em đẹp." Body: hormone + schema + empathy.
    Accuracy: ~10-30%
    = PFC CONFABULATE: tìm lý do PHÙ HỢP nhưng KHÔNG PHẢI mechanism

    ⭐ VÍ DỤ TIÊU BIỂU — Einstein (🟢 quote có thật):
      "The most beautiful experience we can have is the mysterious."
      "He who can no longer pause to wonder and stand rapt in awe,
       is as good as dead; his eyes are closed."

      Einstein NÓI NHƯ THỂ ai không trải nghiệm sự bí ẩn thì chưa sống đúng.
      PFC của Einstein: "the mysterious is the most beautiful experience"
      Body của Einstein: hardware fit + decades of chunk accumulation + Goldilocks zone
        → Mỗi bí ẩn vật lý = prediction error → VTA delta → dopamine + opioid
        → = Body fire reward CỰC MẠNH khi gặp mystery → PFC label: "beautiful"

      NHƯNG — body-base fire CÙNG CƠ CHẾ cho MỌI NGƯỜI, chỉ khác INPUT:
        → Einstein: sướng vì gặp mystery vật lý (chunk physics + hardware fit)
        → Đầu bếp: sướng vì nấu món vừa ý (chunk cooking + hardware fit)
        → Nhạc sĩ: sướng vì sáng tác giai điệu hay (chunk music + hardware fit)
        → Họa sĩ: sướng vì vẽ được hình thù mong muốn (chunk art + hardware fit)
        → Ai đó: sướng vì ăn ngon, thấy cảnh đẹp, gặp người yêu...
        → = CÙNG opioid pathway, CÙNG VTA delta, CÙNG Goldilocks reward
        → = Khác CHUNKS + khác HARDWARE → khác INPUT trigger → CÙNG body-base fire

      Einstein nghĩ "mystery" là đặc biệt vì PFC của ÔNG ẤY chỉ thấy chain CỦA ÔNG.
      Ông không thấy: đầu bếp CŨNG "rapt in awe" khi nấu món hoàn hảo.
      = PFC confabulation + identity schema ("physicist = cách sống đúng")
      = Mỗi người TƯỞNG domain CỦA MÌNH là đặc biệt → vì body CỦA HỌ fire mạnh nhất ở đó


  "VÔ TƯ" VÀ "ĐAM MÊ" — 2 CONFABULATION PHỔ BIẾN NHẤT:

  ⭐ "CHO ĐI VÔ TƯ":
    PFC: "Tôi giúp người khác. Vô tư. Không mong đợi gì."
    Body tính:
      Chain 1: Giúp → họ improve → empathy → opioid (+)
      Chain 2: Giúp → "tôi = người tốt" → identity (+)
      Chain 3: Giúp → community see → status (+)
      Chain 4: Giúp → bond → future reciprocal access (+)
    Net: 4 chains reward >> cost → body CHỌN "giúp"
    
    "Vô tư" = ĐÚNG từ góc nhìn PFC (PFC thật sự không thấy chain)
    "Vô tư" = SAI từ góc nhìn body (body LUÔN tính, luôn có reward)
    CẢ HAI đều đúng — ở TẦNG KHÁC NHAU.

    BẰNG CHỨNG "KHÔNG VÔ TƯ" — 3 violation tests:
    (Emergent-Patterns.md §5, Empathy.md §6)
      Test 1: "Cho đi" DỪNG khi body-base thiếu
        → Người đói khát không còn cho cơm nữa → L1 self > empathy reward
      Test 2: "Cho đi" DỪNG khi schema bị phản bội
        → Phát hiện tổ chức từ thiện gian lận → identity chain COLLAPSE → dừng cho
      Test 3: "Cho đi" DỪNG khi reciprocity = 0 kéo dài
        → Giúp mãi mà không ai quan tâm → connection chain FAIL → dần dừng
    → Nếu thật sự "vô tư" → sẽ KHÔNG DỪNG. Nhưng nó DỪNG → có điều kiện.

  ⭐ "ĐAM MÊ":
    PFC: "Tôi đam mê vật lý. Đây là con đường của tôi."
    Body tính:
      Hardware fit: processing style match physics thinking
      Chunk accumulation: years of practice → Goldilocks zone
      VTA delta: mỗi insight → prediction error → dopamine
      Mastery reward: solve problem → opioid
      Identity: "physicist" = Anchor-Schema compiled
    
    "Đam mê" = PFC LABEL cho state "nhiều chains converge → strong sustained drive"
    "Đam mê" KHÔNG PHẢI nguyên nhân hành vi — mà là MÔ TẢ kết quả
    = Drive.md §0: "'Đam mê' = MÔ TẢ drive mạnh + sustained, KHÔNG PHẢI nguyên nhân"

    🟢 Nisbett & Wilson 1977: "Telling more than we can know"
      → Subjects confabulate reasons cho decisions đã xảy ra
    🟢 Libet 1983: readiness potential TRƯỚC conscious decision
      → Body decide trước, PFC biết sau
    🟢 Gazzaniga split-brain: left hemisphere confabulates explanations
      → PFC PHẢI explain → bịa nếu không biết
```

---

## §8 — GIỚI HẠN NỀN TẢNG + 3 NGUYÊN TẮC

```
🟡 GIỚI HẠN NỀN TẢNG — SCHEMA VÔ TẬN → CHAIN KHÔNG THỂ MAP CHÍNH XÁC:

  Schema.md §1.2 đã xác lập:
    ① 86 tỷ neurons × ~100 nghìn tỷ connections = hệ thống quá lớn
    ② Schema = MULTI-MODAL (body + motor + visual + somatic + emotional + verbal)
       → Verbal chỉ capture ~1/6 schema thật
    ③ Schema SÂU = body adaptation (cortisol, muscle tension, gut state)
       → Chính người đó CŨNG không biết
    ④ Schema thay đổi liên tục → "chụp" lúc này → lúc sau đã khác
    ⑤ Khoa học hiện đại chưa đủ công cụ

  VALENCE CHAIN — GIỚI HẠN NHÂN LÊN:
    → Schema A đã không thể mô tả chính xác
    → Schema B cũng không
    → LINK giữa A và B cũng không (multi-modal, implicit, body-level)
    → CHAIN A→B→C→...→body-base: CÒN KHÓ HƠN
    → Network TOÀN BỘ: vô tận schemas × vô tận links = KHÔNG THỂ map

  VÀ THÊM — KHÔNG CÓ CẤU TRÚC CỐ ĐỊNH:
    → Schema network KHÔNG như database có bảng + cột + quan hệ rõ
    → Mỗi người = 1 network KHÁC (cùng event → khác schema → khác chain)
    → Cùng 1 người, network THAY ĐỔI liên tục
    → Có chain mà PFC KHÔNG BAO GIỜ biết (hardware-level)
    → Có chain KHÔNG THỂ verbalize (body-level, somatic)
    → = "Kiến trúc xâu chuỗi kỳ quái" — biết nó TỒN TẠI, không thể vẽ bản đồ

  VẬY "MÒ MÃI VÔ NGHĨA"?

    KHÔNG. Vì con người KHÔNG CẦN map chính xác để SỐNG TỐT.

    Con người chỉ cần:
      ① Biết PATTERN nào đang drive mình (nhận diện, không cần chính xác)
      ② Biết pattern đó SERVE body-base hay KHÔNG (check output, không check chain)
      ③ Biết khi nào cần THAY ĐỔI (detect dissonance, không cần biết full chain)

    Framework = "CÔNG CỤ NAVIGATE, không phải GPS chính xác"
              = "Công thức, không đáp án" — tool để TỰ KHÁM PHÁ

    3 cái CÓ THỂ:
      → Nhận diện PATTERN (hành vi lặp lại = schema biểu hiện)
      → Ước lượng NHÓM (schema chain thuộc cluster nào)
      → Suggest HƯỚNG (chain NÀY có vẻ link tới body-base CHANNEL kia)

    → MỞ CỬA CHO AI-SCHEMA-DETECTION:
      AI giỏi pattern detection trên large corpus
      Chuyên gia tâm lý giỏi Self-Pattern-Match (feel-check)
      Client giỏi body-verify (Focusing, Somatic-Articulation-Loop)
      = 3 tầng: AI detect → Chuyên gia feel-check → Client self-verify
      = Không cần chính xác tuyệt đối. Approximate + verify = ĐỦ.
      → (Chi tiết: AI-Schema-Detection.md — file tiếp theo)


⭐ 3 NGUYÊN TẮC QUAN TRỌNG:

  NGUYÊN TẮC 1 — Schema Effectiveness ≠ Schema Truthfulness:

    Schema CÓ THỂ sai hoàn toàn về content MÀ VẪN effective:
      → Tin Thiên Đàng: unfalsifiable, chưa verify → NHƯNG behavioral output
        (chăm chỉ + đạo đức) → body-base feed → EFFECTIVE
      → Patriotic schema ("nation is worth dying for"): install chain qua education
        + media + ritual → drive bảo vệ cộng đồng → body-base feed → EFFECTIVE
        🟢 Mọi quốc gia đều có, content KHÁC nhưng mechanism GIỐNG

    Schema CÓ THỂ partially true MÀ VẪN fail:
      → "Giàu = hạnh phúc": true rằng tiền → L1 feed. NHƯNG nếu đường đi
        sacrifice L1 comfort + connection → đạt giàu → TRỐNG RỖNG → FAIL

    → Effectiveness = behavioral output có feed body-base không?
    → Truthfulness = chain content có đúng reality không?
    → 2 chiều KHÁC NHAU. Có thể true+effective, true+fail, false+effective, false+fail.

  NGUYÊN TẮC 2 — Body Check OUTPUT, Không Check TRUTH:

    Body KHÔNG verify chain content (A→B→C có đúng không?)
    Body CHỈ verify chain output (hành vi cuối có feed body-base không?)

    Thiên Đàng: body KHÔNG check "Thiên Đàng có thật?" (impossible)
    Body CHECK: "sống đạo đức → community accept → body smooth" → YES → tiếp
    = Body = PRAGMATIST, không phải SCIENTIST

    TẠI SAO:
      → Body không CÓ CÁCH check abstract chain truth (no sensor for "truth")
      → Body CHỈ CÓ sensors cho body-base channels (pain, pleasure, dissonance...)
      → → Body tối ưu: "output feed tôi?" → YES/NO → đủ

    HỆ QUẢ:
      → Schema sai CÓ THỂ tồn tại RẤT LÂU nếu output vẫn feed body-base
      → Schema đúng CÓ THỂ bị reject nếu output KHÔNG feed body-base
      → = Tại sao misinformation KHÓ xóa: body đã compile → output "OK" → giữ
      → = Tại sao sự thật đau đớn BỊ REJECT: output = dissonance → body reject

    PFC CÓ THỂ CHECK TRUTH — nhưng:
      → PFC chỉ check khi TRIGGERED (dissonance, curiosity, forced evaluation)
      → Nếu body smooth → PFC KHÔNG CÓ TRIGGER để check
      → = Tại sao tin Thiên Đàng smooth: body OK → PFC idle → không question
      → = PFC chỉ question khi CÓ VẤN ĐỀ, không question khi MỌI THỨ ỔN

  NGUYÊN TẮC 3 — "Vô Tư" Đúng Ở Tầng PFC, Sai Ở Tầng Body:

    2 TẦNG OBSERVATION khác nhau cho CÙNG 1 hành vi:

    TẦNG PFC (conscious experience):
      → PFC thấy: "Tôi muốn giúp. Không mong gì."
      → PFC THẬT SỰ không thấy reward chains
      → → Từ góc nhìn PFC: "vô tư" = MÔ TẢ ĐÚNG conscious experience

    TẦNG BODY (unconscious computation):
      → Body tính: 4+ chains reward → net positive → drive "giúp"
      → Body LUÔN tính, LUÔN có reward calculation
      → → Từ góc nhìn body: "vô tư" = SAI — always reward-driven

    CẢ HAI ĐÚNG — ở tầng riêng:
      → Không nên nói "cho đi vô tư là giả" (PFC experience THẬT)
      → Không nên nói "cho đi thật sự vô tư" (body computation CÓ reward)
      → = 2 tầng observation KHÁC NHAU cho cùng 1 phenomenon
      → = Feeling.md v2.0 core claim: "Feeling = PFC observation of body"
      → = PFC observes WHAT body does, not HOW body computes

    IMPLICATION:
      → "Cho đi" CÓ GIÁ TRỊ: cả người cho lẫn người nhận đều benefit
      → Biết mechanism KHÔNG LÀM GIẢM giá trị
      → Biết mechanism CÓ THỂ GIÚP: hiểu khi nào sẽ dừng (3 violation tests)
      → = Framework mục đích: HIỂU, không phải PHÁN XÉT
```

---

## §9 — HONEST ASSESSMENT

```
VERIFIED (🟢):

  Per-entity valence:
    → Multi-channel emotional processing: established
    → Mixed feelings (ambivalence): well-documented (Cacioppo & Berntson 1994)
    → Negativity bias: robust (Baumeister et al. 2001)
    → Confirmation bias: established (Nickerson 1998)
    → Fear conditioning + evaluative conditioning: established

  Valence hình thành:
    → 4 nguồn: classical conditioning, observational learning (Bandura),
      cultural transmission (Rachman 1977), context inference
    → Update dynamics: consistent with learning theory
    → Betrayal trauma: Freyd 1996

  Propagation evidence:
    → Spreading activation: Collins & Loftus 1975 (established)
    → Conditioned reinforcement chains: Skinner, token economy (established)
    → Temporal difference learning: Schultz 1997 (dopamine prediction error)
    → Goal gradient effect: Hull 1932 (established)
    → Temporal discounting: Ainslie 1975 (established)
    → Stimulus generalization: Pavlov, Watson (established)
    → Overgeneralization in anxiety: Dunsmoor & Murphy 2015

  PFC blindness:
    → Confabulation: Nisbett & Wilson 1977 (established)
    → Readiness potential: Libet 1983 (established, debated interpretation)
    → Split-brain confabulation: Gazzaniga (established)

  Cases:
    → Schadenfreude: Takahashi et al. 2009
    → Costly punishment: Fehr & Gächter 2002
    → Prosocial behavior + mirror: de Waal 2008
    → Unfalsifiable belief resilience: Popper + Festinger 1957


FRAMEWORK REASONING (🟡):

  → Valence as multi-channel PROFILE (formalization mới, concept đúng)
  → Object vs Agent vs Abstract valence complexity (framework categorization)
  → 4 nguồn hình thành as explicit model (established components, new grouping)
  → Meta-dimensions (trust, predictability, replaceability): framework addition
  → 4 propagation mechanisms as explicit model (established components, new framing)
  → 5 chain properties (length/trust/parallel/conflict/invisible): new formalization
  → PFC accuracy ≈ f(1/chain_length): logical inference, untested
  → 6 nhóm cases categorization: framework analysis
  → 3 nguyên tắc (effectiveness≠truthfulness, body checks output, vô tư at 2 levels):
    framework synthesis, logic consistent

  §5b WHY chain dài tồn tại (v1.1):
  → Tầng 1 EXIST (chunk substrate tạo chain): 🟢 established mechanisms
    (Hebb 1949, Collins & Loftus 1975, Anderson 1983)
  → Tầng 2 EXTEND (valence propagation kéo dài): 🟢🟡 mixed
    (TD learning 🟢, install propagation = framework term 🟡)
  → Tầng 3 FIT (pyramidal compression): 🟢🟡
    (Cowan 2001, Chase & Simon 1973 🟢; compression model = framework synthesis 🟡)
  → Chain dài = f(vô thức quality, KHÔNG PHẢI PFC size): 🟡
    (Pietschnig 2015 meta ~0.24 🟢 supports; causal claim = framework 🟡)
  → Tầng 4 FILTER (group selection cho chain dài): 🟡🔴
    (Hamilton/Trivers 🟢; group selection debated 🟡; specific claim = 🔴)
  → Cause vs Filter distinction: 🟡 framework framing
  → Trade-off nền tảng (chain dài = feature, not bug): 🟡
    (immune system analogy 🟢; application to chain dài = framework reasoning 🟡)


HYPOTHESIS (🔴):

  → Valence propagation as EXPLICIT NAMED MODEL:
    Concept IMPLICIT trong spreading activation + conditioned reinforcement,
    nhưng explicit formalization "valence propagation qua schema chain" = MỚI.
    Cần test: có phải NÀO CŨNG valence, hay có filter mechanism?

  → Backward propagation (reward → valence spread ngược):
    🟢 Temporal difference learning (Schultz) supports prediction error propagation.
    🔴 NHƯNG: cơ chế CỤ THỂ cho "valence spread backward through abstract chain"
    chưa formalize trong neuroscience. Logical inference from TD learning.

  → Chain trust = product of link trusts:
    Mathematical model. Likely OVERSIMPLIFIED. Actual mechanism probably
    non-linear, context-dependent, asymmetric.

  → Positive overgeneralization = same speed as negative:
    UNLIKELY — negativity bias suggests asymmetric. Framework acknowledged.

  → Serial killer schema mislink as full explanation:
    OVERSIMPLIFIED — psychopathy involves hardware variation (amygdala, ACC)
    not just schema content. Framework acknowledged "hardware OK" is approximate.

  → Group selection cho chain dài (§5b Tầng 4):
    🔴 Specific hypothesis: nhóm có chain dài → mạnh hơn → survive.
    Logic consistent với Hamilton/Trivers, nhưng CHƯA có direct evidence
    cho "chain length" specifically as selection pressure.
    Tầng 1-3 ĐÃ ĐỦ giải thích chain dài ở cá nhân → Tầng 4 = optional.


CÂU HỎI MỞ:

  → Cơ chế neural CỤ THỂ cho valence propagation? Brain regions? Circuits?
  → Chain decay function: linear? exponential? step? Context-dependent?
  → Maximum chain length mà body vẫn "trust"? Có giới hạn?
    ⤷ §5b Tầng 3 gợi ý: chain length THỰC TẾ bị giới hạn bởi
      pyramidal compression quality, KHÔNG phải absolute limit.
      Chain "dài" mà compressed tốt = body vẫn trust.
      Chain "ngắn" mà mỗi link low trust = body KHÔNG trust.
      → Maximum = f(compression quality × link trust), không phải f(link count)
  → Khi nào chain BỊ ĐỨT vs khi nào body REPAIR?
  → Filter mechanism: body có filter nào cho "chain NÀY đáng trust"?
  → Positive overgeneralize: same mechanism nhưng KHÁC TỐC ĐỘ bao nhiêu?
  → AI-assisted schema detection: CAN HAPPEN? HOW? (→ AI-Schema-Detection.md)
```

---

## §10 — CROSS-REFERENCES + STATUS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Body-Base.md — L0-L3 channels mà valence đánh giá
    → Body-Input-Enumeration.md — reframe L0-L3, body-inputs chi tiết
    → Schema.md §1-§1.2 — schema = chunks + links + purpose, KHÔNG THỂ phân tích
    → Chunk.md v2.0 — chunk substrate, multi-modal binding, compile dynamics
    → Chunk.md v2.0 §3 — 4 loại connections (§5b Tầng 1 EXIST) ← MỚI v1.1

  MECHANISM:
    → Drive.md §0 — schema = DETECTOR, vô thức = ENGINE, PFC = navigator
    → Drive.md §0 — "Đam mê" = MÔ TẢ drive, KHÔNG PHẢI nguyên nhân
    → Feeling.md v2.0 §2 — 7-layer fidelity gradient (Layer 7 = 20-70% accuracy)
    → Feeling.md v2.0 §3 — core claim: feeling = PFC observation of body
    → Feeling.md v2.0 §5 — 8-step operational flow
    → Feeling.md v2.0 §6 — dopamine ≠ reward, 5 preconditions
    → Agent.md §0 — Self-Pattern-Match (mirror mechanism for observed experience)
    → Agent.md §10 — Mode 2 schema override cho abstract agents
    → PFC-Analysis.md — pyramidal compression, 4±1 dimensions,
      Observed Capacity = Hardware × Vô Thức × Cortisol × Context (§5b Tầng 3 FIT) ← MỚI v1.1

  PROPAGATION CONTEXT:
    → Anchor-Schema.md §1-§2 — anchor amplify chain, trust ≥ cost → hold
    → Emergent-Patterns.md §5 — "Cho đi" pattern, 4 nguồn reward
    → Empathy.md §6 — empathy reward override spectrum (lành mạnh → compulsive)
    → Empathy.md §7 — evolutionary function, group selection logic (§5b Tầng 4 FILTER) ← MỚI v1.1
    → Somatic-Articulation-Loop.md — body knowledge → explicit knowledge

  CŨ (đã backup):
    → Domain/backup/Valence.md — per-entity valence DRAFT v0.5
      (content integrated vào §1-§3 file NÀY)
    → Domain/backup/Object-Agent.md — binary classification (superseded by Agent.md)

  TIẾP THEO:
    → AI-Schema-Detection.md (chưa viết) — AI-assisted schema pattern detection
      = Ứng dụng valence propagation model + schema network understanding


STATUS:

  v1.0 — 2026-04-18 — Session N+16
    → Initial version: §0-§10, per-entity + propagation + chain + cases + PFC blindness
  
  v1.1 — 2026-04-18 — Session N+19
    → THÊM §5b: "Tại Sao Chain Dài Tồn Tại: 4 Tầng Cơ Chế"
      Tầng 1 EXIST (chunk substrate), Tầng 2 EXTEND (valence propagation),
      Tầng 3 FIT (pyramidal compression, PFC quality ≠ PFC size),
      Tầng 4 FILTER (group selection — hypothesis)
    → UPDATE §9: thêm confidence cho §5b + thêm hypothesis group selection
    → UPDATE §9 Open Questions: partial answer cho "maximum chain length"
    → UPDATE §10: thêm cross-refs PFC-Analysis.md, Empathy.md §7, Chunk.md §3
    → ĐÍNH CHÍNH: "PFC lớn hơn → chain dài" = SAI. Chain dài = f(vô thức compile quality)
    → THÊM §5b Trade-off: chain dài = feature (net positive cho tập thể dù có hại cá nhân)
    → FIX terminology: "mirror reward/dissonance" → "empathy reward/dissonance" toàn file
    → FIX cross-refs: "Empathy-Mirror.md §8.5" → "Empathy.md §6" (file đã thay thế)
  
  Tổng hợp:
    → Domain/backup/Valence.md (~579L) — per-entity valence, profile, cases
    → Session N+16 analysis — 12+ cases, schema-chain propagation concept
    → Session N+19 analysis — WHY chain dài tồn tại, PFC-Capacity refine
    → Schema.md, Drive.md, Anchor-Schema.md, Feeling.md v2.0, Agent.md, Chunk.md v2.0
    → Emergent-Patterns.md §5, Empathy.md §6, PFC-Analysis.md, Empathy.md §7
  
  Sections:
    §0  Position trong framework
    §1  Valence là gì (4 đặc tính)
    §2  Valence profile per-entity (L0-L3 + meta + Object/Agent/Abstract)
    §3  Hình thành (4 nguồn) + Update (3 loại) + Bias
    §4  ⭐ Valence Propagation qua schema chain (4 cơ chế) — v1.0
    §5  ⭐ 5 đặc tính chain (length, trust, parallel, conflict, invisible) — v1.0
    §5b ⭐ Tại sao chain dài tồn tại: 4 tầng cơ chế — v1.1 MỚI
    §6  Cases phân tích (6 nhóm, 12+ cases)
    §7  ⭐ PFC Blindness + Confabulation ("vô tư", "đam mê") — v1.0
    §8  ⭐ Giới hạn nền tảng + 3 nguyên tắc — v1.0
    §9  Honest assessment (🟢🟡🔴) — updated v1.1
    §10 Cross-references + Status — updated v1.1

  Confidence distribution:
    🟢 Per-entity valence, formation, update, bias, cases
    🟢 Spreading activation, conditioned reinforcement, confabulation
    🟢 Chunk substrate tạo chain (Hebb, Collins & Loftus) — §5b Tầng 1
    🟡 Profile structure, 4-mechanism model, 5 chain properties
    🟡 3 nguyên tắc, 6 nhóm cases, PFC accuracy function
    🟡 Pyramidal compression cho chain fit (Cowan, Chase & Simon) — §5b Tầng 3
    🟡 Chain dài = f(vô thức quality) — §5b
    🔴 Valence propagation as named model, backward propagation mechanism
    🔴 Chain trust = product model, positive overgeneralize speed
    🔴 Group selection cho chain dài — §5b Tầng 4

  Next:
    → AI-Schema-Detection.md — ứng dụng valence propagation + schema navigation
    → Audit files liên quan: Drive.md, Emergent-Patterns.md có thể cần update cross-refs
    → Test cases thêm để verify chain model
```
