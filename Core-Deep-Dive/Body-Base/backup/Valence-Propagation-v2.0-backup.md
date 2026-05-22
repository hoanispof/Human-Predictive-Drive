---
title: Valence-Propagation — Hệ Thống Đánh Giá Của Body + Cơ Chế Truyền Qua Schema Network
version: 2.0
created: 2026-04-18
updated: 2026-05-16 (v2.0 — FULL REWRITE: Entity-Compiled 3 subtypes, mixed valence, developmental trajectory, §5+§5b merge, Inter-Body drill integration)
previous: v1.4 → backup/Valence-Propagation-v1.4-backup.md
status: v2.0 — REFERENCE FILE (kiến trúc tổng thể Valence system)
scope: |
  WHAT valence IS + HOW valence WORKS per-entity + HOW valence PROPAGATES qua schema chain
  + WHY PFC không biết + GIỚI HẠN nền tảng.
  v2.0 KEY CHANGES:
    ① Entity-Owned → Entity-Compiled REFRAME: 3 subtypes (positive/negative/mixed)
    ② Mixed valence = PHỔ BIẾN NHẤT (drill §11.10) — not pathological
    ③ Entity-Compiled vs Obligation = INDEPENDENT mechanisms
    ④ Developmental trajectory: 0-5 positive → mixed emerge → adult possible shift
    ⑤ §5+§5b MERGE thành §6 Chain Properties mạch lạc
    ⑥ Body-Need aggregate reference (BFM v2.0 §1)
    ⑦ Inter-Body-Mechanism.md cross-refs throughout
  Tích hợp: Domain/backup/Valence.md (per-entity, DRAFT v0.5) + phân tích MỚI session N+16
  (propagation, chain properties, PFC blindness, fundamental limits)
  + drill Inter-Body Mechanism insights (Entity-Compiled, 3-cost, mixed valence).
purpose: |
  Central reference file cho toàn bộ Valence system trong framework.
  Thay thế Domain/Valence.md DRAFT (2026-04-12, ~579L → Domain/backup/Valence.md).
  Vai trò tương đương Feeling.md v2.0 và Chunk.md v2.0 cho hệ thống tương ứng.
dependencies:
  - Body-Base.md v2.1 — L0-L1-L3 channels mà valence đánh giá
  - Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, 2 sources, 3 dynamics
  - Inter-Body-Mechanism.md v1.0 — Entity-Compiled §8, 3-cost §4, By-Product Match §5
  - Body-Coupling.md v1.1 — coupling mechanism deep-dive (extends §3)
  - Connection.md v3.3 — 3 Generative Primitives, §3.3 2-luồng overview
  - Agent-Mechanism.md v1.0 — §12 body-need feeder, §12.2b L1/L2 transition
  - Self-Pattern-Match.md v2.4 — F1/F2, §10 reversed mapping
  - Collective-Body.md v1.2 — Model 3 cấp (§5 Clarification reference)
  - Schema.md v2.0 — schema = chunks + links + purpose
  - Chunk.md v2.2 — chunk substrate, context-tag, 4 connection types
  - Anchor-Schema.md v1.2 — anchor amplify propagation, trust binding
  - Feeling.md v2.0 — PFC observation of body-feedback (khác tầng)
  - Reward-Signal-Architecture.md v1.0 — Type A/B × valence
  - Obligation.md v1.0 — compiled prediction (independent of Entity-Compiled)
  - Protect.md v1.0 — f(replaceability × attachment depth)
  - Framework-Label.md v3.0 — vocabulary reference
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
> **Bạn giúp đỡ người lạ. PFC bạn nói: "vô tư thôi."**
> **Compiled patterns fire: empathy, identity, status, connection.**
> **Nhiều chuỗi SONG SONG → net reward >> cost.**
> **PFC KHÔNG BIẾT những chuỗi này tồn tại.**
>
> **Bạn "đam mê" vật lý. PFC nói: "vì nó hay."**
> **Body: hardware fit + chunk match + Goldilocks + prediction-delta.**
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
- §3 — ENTITY-COMPILED: Body-Base Extension
- §4 — CÁCH VALENCE HÌNH THÀNH + UPDATE
- §5 — VALENCE PROPAGATION QUA SCHEMA CHAIN
- §6 — CHAIN PROPERTIES + WHY CHAIN DÀI TỒN TẠI
- §7 — CASES PHÂN TÍCH
- §8 — PFC BLINDNESS + CONFABULATION
- §9 — GIỚI HẠN NỀN TẢNG + 3 NGUYÊN TẮC
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES + STATUS

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
    ┌─────────────────────────────────────────────────────────┐
    │ VALENCE-PROPAGATION.MD (FILE NÀY)                       │
    │                                                          │
    │  TẦNG 1: Per-Entity Valence (§1-§2)                     │
    │    Entity → body channels → valence profile              │
    │    "Cái dao NÀY ảnh hưởng body TÔI thế nào?"           │
    │                                                          │
    │  TẦNG 1b: Entity-Compiled (§3)                   ← MỚI │
    │    Agent compile SÂU → body-base extension               │
    │    3 subtypes: positive / negative / mixed                │
    │    2-luồng reward (L1 SPM-owned / L2 Entity-Compiled)   │
    │                                                          │
    │  TẦNG 2: Valence Propagation (§5-§6)                    │
    │    Valence TRUYỀN qua links trong schema network         │
    │    "Toán có valence positive VÌ link tới tương lai"     │
    │    Chain properties + WHY chain dài tồn tại             │
    │                                                          │
    │  TẦNG 3: PFC Blindness + Limits (§8-§9)                │
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

  "Body channels" = hệ thống L0-L1-L3 (Body-Base.md):
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

    ⚠️ NO SOURCE TAG (Drill §10 — GAP 8):
    → Valence stored KHÔNG kèm field "nguồn gốc" (internal hay external?)
    → Wire = wire. Body treat BÌNH ĐẲNG bất kể compiled từ đâu.
    → PFC CŨNG không phân biệt (§8 confabulation)
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
    BODY-BASE EXTENSION → §3 Entity-Compiled.


  ABSTRACT ENTITY VALENCE:

    Ngoài Object và Agent, còn có abstract entities:
      Toán, vật lý, từ thiện, Thiên Đàng, "tương lai tốt đẹp"...
    
    Abstract entity valence ĐẶC BIỆT vì:
      → Không có physical form → KHÔNG có L0 direct
      → Valence HOÀN TOÀN qua schema link (§5 Propagation)
      → Có thể UNFALSIFIABLE (Thiên Đàng, "ý nghĩa cuộc đời")
      → → Không bao giờ nhận negative feedback → valence KHÔNG BAO GIỜ bị revise
      → → = "Thiết kế" valence ổn định nhất có thể
      → = Agent-Mechanism.md §10: Mode 2 schema override cho abstract agents

    🟡 Abstract entity valence = framework concept
    🟢 Unfalsifiable belief resilience = Popper + Festinger 1957 (cognitive dissonance)
```

---

## §3 — ENTITY-COMPILED: Body-Base Extension

> **v2.0 REFRAME**: "Entity-Owned" → "Entity-Compiled".
> "Owned" gợi ý CHỈ positive. NHƯNG negative structural CŨNG TỒN TẠI.
> VÀ mixed valence = PHỔ BIẾN NHẤT.
> → Inter-Body-Mechanism.md §8 define reframe này.

```
⭐ KHI PER-AGENT VALENCE COMPILE ĐỦ SÂU → BƯỚC NHẢY CHẤT:

  AGENT VALENCE CÓ DIMENSION MÀ OBJECT KHÔNG BAO GIỜ CÓ:

    Khi per-agent valence STRONG + compiled SÂU qua nhiều interaction:
      → Body KHÔNG CHỈ đánh giá "agent X ảnh hưởng tôi thế nào?"
      → Body chuyển sang: "agent X's state = MY state"
      → = Agent TRỞ THÀNH phần mở rộng body-base CỦA TÔI
      → = STRUCTURAL, SUSTAINED — không phụ thuộc từng episode tương tác

    BƯỚC NHẢY CHẤT — TẠI SAO KHÔNG PHẢI CHỈ "VALENCE MẠNH":

      Object strong positive (dao tốt, xe quen):
        → Valence ++, nhưng dao KHÔNG BAO GIỜ = "phần của tôi"
        → Mất dao = tiếc (resource loss), KHÔNG = đau (body-base loss)

      Agent strong compile (con, mẹ, bạn thân 20 năm):
        → Valence strong, VÀ agent = body-base extension
        → Agent's channels ĐƯỢC body treat AS own channels
        → Con đói = TÔI đói (structural, không chỉ empathy momentary)
        → Mất agent = PHẦN CỦA TÔI BỊ CẮT
        → = Tại sao grief ≠ "tiếc" — grief = body-base amputation

    TẠI SAO CHỈ AGENT, KHÔNG BAO GIỜ OBJECT:
      Object KHÔNG fire SPM → không có L1 episodes tích lũy
      Object KHÔNG bidirectional → không có mutual reinforcement
      Object DỄ thay thế → trust/dependency không compile sâu đủ
      → Body-base extension = EMERGENT property CHỈ CÓ ở agent valence
      → Object có thể valence CỰC POSITIVE (nhà, xe, sách yêu thích)
        nhưng KHÔNG BAO GIỜ = "phần mở rộng body-base"
      → Mất nhà = stress tài chính. Mất con = body-base amputation.
        2 loại loss KHÁC CĂN BẢN.

    🟢 Grief as body-level pain: Eisenberger 2003 (social pain = physical pain pathways)
    🟢 Attachment bond = body-level: Bowlby 1969
    🟢 Protect.md: loss aversion = f(replaceability × attachment depth)
    🟡 "Body-base extension" as explicit concept = framework synthesis
```

### §3.1 — Reframe: Entity-Owned → Entity-Compiled

```
⭐ REFRAME TERMINOLOGY (Inter-Body-Mechanism.md §8.1):

  CŨ: "Entity-Owned" (Luồng 2 — VP v1.4 §2)
  MỚI: "Entity-Compiled"

  TẠI SAO ĐỔI:
  → "Owned" gợi ý CHỈ positive (entity thuộc về tôi, tôi care)
  → NHƯNG: negative structural CŨNG TỒN TẠI (enemy wired into body-base)
  → VÀ: MIXED valence PHỔ BIẾN NHẤT (vừa thương vừa giận)

  Entity-Compiled = entity đã compile vào body-base ở STRUCTURAL level
  = Per-channel valence profile (KHÔNG phải 1 số positive/negative)
  = Bidirectional: entity's state AFFECTS my body-base (dù + hay -)

  🟡 "Entity-Compiled" reframe = framework synthesis.
     Consistent với Valence-Propagation multi-channel model.
```

### §3.2 — 3 Subtypes (spectrum)

```
⭐ 3 SUBTYPES — SPECTRUM, KHÔNG BINARY (Inter-Body-Mechanism.md §8.2):

  ① POSITIVE-DOMINANT (≈ old "Entity-Owned"):
     Majority channels positive. Presence = approach + reward. Loss = grief.
     Example: bạn thân lâu năm, con cái, mẹ healthy relationship.
     Mechanism: repeated feed → L2 threshold cross → structural compile.

  ② NEGATIVE-DOMINANT:
     Majority channels negative. Presence = threat/dissonance. Loss = relief.
     NHƯNG sub-case "obsession": loss = emptiness (mất mục tiêu).
     Example: bully, abuser, đối thủ obsessive.
     Mechanism: repeated harm → negative compile structural.

  ③ MIXED (AMBIVALENT) — PHỔ BIẾN NHẤT:
     Significant BOTH positive AND negative channels CÙNG LÚC.
     Behavior oscillates by STATE/TRIGGER/CONTEXT.
     Loss = COMPLEX grief (relief + pain simultaneously).
     Example: bố mẹ strict, vợ chồng conflict, frenemy.

     ┌──────────────────────────────────────────────┐
     │ VALENCE PROFILE "Mẹ" (multi-channel):       │
     │                                              │
     │   Nutrition:  ++ (nuôi nấng)                │
     │   Comfort:    ++ (an ủi, ôm ấp)            │
     │   Autonomy:   -- (ép học, cấm đoán)         │
     │   Mastery:    + (dạy kỹ năng)              │
     │   Status:     +/- (khen/chê trước mặt khách)│
     │                                              │
     │   KHÔNG AVERAGE: cả ++ và -- song song      │
     │   "Vừa thương vừa giận" = CẢ HAI fire       │
     │   STATE quyết định channel nào dominant      │
     └──────────────────────────────────────────────┘

  TẠI SAO ③ PHỔ BIẾN NHẤT?
    → Relationship dài → nhiều interaction types → nhiều channels compile
    → CÀNG GẦN nhau LÂU → càng nhiều channels (cả + và -)
    → "Thuần positive" = rare luxury of LIMITED interactions
    → Paradox: GẦN NHAU LÂU = deeper bond + deeper conflict potential
    → = Same person: STRONGEST positive channel + STRONGEST negative channel

  🟡 3 subtypes = framework synthesis (Drill §11.10).
  🟢 Ambivalence = well-documented (Cacioppo & Berntson 1994).
```

### §3.3 — Điều kiện hình thành + Gradient

```
🟡 ĐIỀU KIỆN HÌNH THÀNH ENTITY-COMPILED:

  ① Nhiều interaction tích lũy → valence compile SÂU
  ② Trust CAO + Replaceability THẤP + Dependency có
  ③ SPM fire THÀNH CÔNG nhiều lần → valence reinforce
  → Body DẦN DẦN treat agent channels AS own channels
  → = Quá trình COMPILE, không phải quyết định ý thức
  → = GRADIENT: từ "quen biết" → "thân" → "thân thiết" → "body-base extension"

  Compile intensity = f(|peak_valence| × interaction_frequency)
  → Peak valence quyết định — repetition = multiplier, not driver
  → 🟢 Emotional intensity predicts memory strength (McGaugh 2004)

  ⭐ MECHANISM DEEP-DIVE → Body-Coupling.md v1.1:
    §3 ở trên mô tả CONCEPT: agent compile sâu → body-base extension.
    Body-Coupling.md drill MECHANISM chi tiết + MỞ RỘNG:
      → 2D Model: |❸| Depth × ❸ Direction → 3 outcomes
      → Extension (positive) + Entanglement (NEGATIVE) + Neutral
      → 3 Phase: ❸ initiates → threshold → coupling sustains independent of L1
      → Negative coupling: 4 accelerators, 4-tầng loss dissolution
      → System compilation: per-context (company, nation) KHÁC per-agent coupling
      → Smoothing + Anti-smoothing = emergent property of |coupling depth|
    §3 NÀY giữ vai trò: PER-ENTITY valence overview + 3 subtypes + 2-luồng concept.
    Body-Coupling.md = WHERE TO GO cho full mechanism analysis.
```

### §3.4 — 2 Luồng Reward (L1 / L2)

```
⭐ 2 LUỒNG REWARD — TẠI SAO MẸ CHĂM CON DÙ KHÓ CHỊU:

  Khi interact với agent, body nhận 2 LUỒNG reward/feedback ĐỒNG THỜI:

  Luồng 1 (SPM-owned, momentary):
    = Body-feedback từ MỖI LẦN SPM F1 fire trên target
    = Có thể + (bạn vui → vui lây) hoặc - (con ốm → khó chịu)
    = Thuộc về SPM mechanism (Self-Pattern-Match.md §2.1)

  Luồng 2 (Entity-Compiled, structural):
    = COMPILED valence → agent = body-base extension
    = SUSTAINED — fire BẤT KỂ Luồng 1 positive hay negative
    = Agent's wellbeing = MY wellbeing (structural, không chỉ momentary)
    = Thuộc về per-agent valence compiled (section NÀY)

  2 luồng INDEPENDENT, có thể CONFLICT:

    Mẹ chăm con ốm:
      L1: negative (simulate con suffering → body khó chịu)
      L2: positive (con = body-base extension → chăm con = feed body-base MÌNH)
      → L2 > L1 → VẪN CHĂM dù L1 negative

    Bác sĩ chăm bệnh nhân lạ:
      L1: negative (simulate suffering → cost THẬT)
      L2: ≈ 0 (bệnh nhân lạ → chưa compiled thành body-base extension)
      → L1 cost TÍCH LŨY không bù → burnout
      → = Moral injury (SPM v2.4 §10) = F1 cost tích lũy KHI L2 không đủ bù

    Bạn thân kể chuyện vui:
      L1: positive (vui lây)
      L2: positive (bạn = body-base extension)
      → COMPOUND reward → gặp bạn thân = cực tốt

  ⭐ COST IMPLICATIONS (Inter-Body-Mechanism.md §4):
    Interaction cost = 3 NGUỒN INDEPENDENT:
      ① PFC Draft Cost (metabolic — chain length × novelty)
      ② Suppress Cost (override compiled response → dissonance)
      ③ Uncertainty Cost (options × time × stakes → cortisol)
    Sustainability = f(total cost per interaction × frequency ÷ reward)
    L2 STRONG → bù cost tốt → bền vững
    L2 ≈ 0 → cost tích lũy → burnout risk

  🟡 2-luồng separation = framework synthesis (Connection.md §3.3)
  🟢 Empathy fatigue ở professionals: Figley 2002 (compassion fatigue)
```

### §3.5 — Entity-Compiled vs Obligation = INDEPENDENT

```
⭐ 2 CƠ CHẾ KHÁC NHAU (Inter-Body-Mechanism.md §8.3):

  Entity-Compiled: "entity's state = MY state" (structural, automatic)
  Obligation:      "predict cost to MAINTAIN access" (prediction, PFC-mediated)

  CÓ THỂ ĐỘC LẬP:
    L2 HIGH + Obligation LOW:  bạn thân → vui tự động, không "nợ" gì
    L2 LOW + Obligation HIGH:  ân nhân xa lạ → không thân nhưng "phải trả"
    L2 HIGH + Obligation HIGH: bố mẹ → yêu thương + cảm thấy phải chăm sóc
    L2 LOW + Obligation LOW:   stranger → no drive either way

  SUSTAINABILITY:
    L2 HIGH + Obligation vô tư (type A) = MOST SUSTAINABLE
      Giúp nhau = vui (L2) + maintain (obligation satisfied). Self-reinforcing.
    L2 LOW + Obligation bắt buộc (type C) = UNSUSTAINABLE
      No reward + chronic cost = obligation-trapped (Resonance §9).

  Cross-ref: Obligation.md v1.0 §2-§4 chi tiết.

  🟡 L2 vs Obligation independence = framework synthesis.
     Consistent với observable cases (bạn thân ≠ ân nhân ≠ stranger).
```

### §3.6 — Developmental trajectory

```
🟡 ENTITY-COMPILED TRAJECTORY (con → bố mẹ):
   (Drill §11.11, Inter-Body-Mechanism.md §8.4)

  Con 0-5:   ① positive chủ yếu (parent = source of ALL feed)
  Con 5-12:  ③ mixed emerge (autonomy ↑, conflict ↑, positive vẫn strong)
  Con 12-18: ③ INTENSIFY (puberty → autonomy surge → peak ambivalence)
  Adult:     Possible shift ① (distance → negative fade → positive reassert)
             HOẶC stuck ③ or shift ② (nếu childhood damage severe)

  = Developmental complexity gradient: simple → maximum mixed → possible simplify
  = Recovery possible nhưng depends on interaction quality post-independence

  GENERAL PRINCIPLE:
    Trẻ nhỏ: entity valence SIMPLER (fewer channels, less mixed)
    Trẻ lớn: begin mixed (more channels compile)
    Người lớn: MAXIMUM mixed (most relationships = ③ varying degrees)
    = Complexity IS NORMAL, not pathological
    = "Thuần positive" = rare luxury of limited/chosen interactions

  🟡 Developmental trajectory = framework synthesis.
  🟢 Adolescent ambivalence toward parents: established developmental psychology.
```

---

## §4 — CÁCH VALENCE HÌNH THÀNH + UPDATE

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
    → = Self-Pattern-Match đọc state người khác → infer valence
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

## §5 — VALENCE PROPAGATION QUA SCHEMA CHAIN

> **Đây là concept MỚI quan trọng nhất của file này.**
> Valence.md cũ mô tả valence PER-ENTITY.
> Section NÀY mô tả valence TRUYỀN QUA NETWORK giữa các schemas.

> ⚠️ **CLARIFICATION — Chain Analysis = EXPLANATORY, Không Phải Processing**
> *(Drill §6, §22 — GAP 13 RESOLVED)*
>
> Chain analysis dưới đây = **Cấp 3** (framework giải thích tại sao behavior hoạt động).
> **KHÔNG phải** cách brain PROCESS ở **Cấp 1** — cá nhân compile SHORT (1-2 nodes).
> Chain dài **SỐNG ở Cấp 2** (collective infrastructure hold cho cá nhân).
> Vẫn CÓ GIÁ TRỊ: chẩn đoán chain gãy, thiết kế collective, phát hiện trust sai.
>
> Chi tiết Model 3 cấp + 4 compile pathways: Collective-Body.md v1.2 §1-§2.

```
🟡 CLARIFICATION — 3 CẤP PHÂN TÍCH (Drill §6, §22):

  VP §5 chain analysis ở dưới mô tả:
    [toán → điểm → đại học → việc → lương → body-base]
  = Cấp 3 analysis. ĐÚNG logic. NHƯNG não KHÔNG process thế.

  Cấp 1 (Individual brain):
    Compile SHORT. Cùng hành vi "đi học toán", 4 pathways khác nhau:
      Hardware fit:    [toán → brain fire → opioid]           — 1 node
      Trust + fit:     [mẹ nói → trust → học → khen → ấm]   — 2 nodes
      Social default:  [mọi người đều học → bình thường]      — 1 node
      Threat avoid:    [không học → mắng → sợ → học]          — 1-2 nodes
    → TẤT CẢ short. Chain DÀI không nằm trong đầu cá nhân.

  Cấp 2 (Collective):
    Giáo dục + thị trường + kinh tế = infrastructure HOLD chain dài.
    Cá nhân chỉ cần trust + compile short → collective deliver kết quả.

  Cấp 3 (Framework — VP §5 analysis):
    GIẢI THÍCH tại sao behavior hoạt động (evolutionary + structural reason).
    MÔ TẢ collective infrastructure. PHÁT HIỆN chain break.

  GIÁ TRỊ THỰC TẾ (chain analysis KHÔNG VÔ NGHĨA):
    ① Chẩn đoán: "Học nhưng thất nghiệp" = biết node NÀO gãy → fix cụ thể
    ② Thiết kế: giáo dục/tôn giáo/policy = thiết kế chain ở Cấp 2
    ③ Verify: collective schema CÓ THỂ sai → chain analysis kiểm tra

  → Chi tiết: Collective-Body.md v1.2 §1 (Model 3 cấp) + §2 (4 pathways)
```

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
    PFC KHÔNG biết: compiled patterns fire nhiều chains song song
    = Valence propagation INVISIBLE cho PFC
    🟢 Miep Gies khi được hỏi luôn nói: "I did what anyone would have done"
       = Classic PFC confabulation — compiled patterns fired nhiều chains, PFC reports 1 simple reason


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
      → = Negativity bias trong propagation (consistent với §4 update bias)

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

## §6 — CHAIN PROPERTIES + WHY CHAIN DÀI TỒN TẠI

> v2.0: MERGE từ v1.4 §5 (5 đặc tính) + §5b (4 tầng cơ chế) thành 1 section mạch lạc.

### §6.1 — 5 Đặc tính của Chain

```
🔴 HYPOTHESIS — framework formalization, logic consistent

  Valence chain (§5) có 5 đặc tính quyết định behavior:


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
      Hardware fit + chunk match → Goldilocks → prediction-delta → opioid
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

    ⭐ QUAN TRỌNG:
      Single chain YẾU → drive YẾU → dễ bỏ
      Multiple parallel chains → drive MẠNH → khó bỏ
      = Tại sao "đam mê" = nhiều chains converge vào 1 activity
      = Tại sao "nghiện" = chains lock → khó thoát
      = Tại sao "cho đi" CÓ nhiều nguồn reward (Emergent-Patterns §5)


  ④ CONFLICTING CHAINS → MIXED VALENCE:

    2+ chains NGƯỢC HƯỚNG cho cùng 1 entity.

    Ví dụ — "Mẹ":
      Chain positive: cho ăn → comfort → protection → L1++ L0++
      Chain negative: ép học → mất tự do → autonomy-- L3-
      → CÙNG entity "mẹ", 2 chains ngược → YÊU + GHÉT cùng lúc
      → = Mixed valence (§2) VÌ conflicting chains
      → = §3.2 ③ Mixed = PHỔ BIẾN NHẤT — cùng mechanism

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
       → Chain thật: empathy + identity + status + connection (nhiều chains invisible)
       → PFC: "Vô tư thôi" — vì không thấy chains phía sau

    d) Chain MULTI-BRANCH (quá phức tạp để PFC track):
       → Gia đình giấu Anne Frank: 4 chains × multiple links each
       → PFC chỉ track 1-2 chains đơn giản nhất
       → PFC: "Vì đó là điều đúng" — đúng 1 chain, bỏ sót 3

    → Chi tiết: §8 PFC Blindness

    🟢 Confabulation: Nisbett & Wilson 1977
    🟡 5 đặc tính chain = framework formalization
```

### §6.2 — 4 Tầng Cơ Chế Tạo + Giữ Chain Dài

```
🟡 TẠI SAO CHAIN DÀI TỒN TẠI?

  Chain dài KHÔNG phải feature được "thiết kế".
  Chain dài = EMERGENT từ 4 tầng cơ chế chồng lên nhau.

  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG  │ VAI TRÒ      │ CƠ CHẾ                    │ CONFIDENCE │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  1    │ EXIST        │ Chunk substrate tự nhiên  │ 🟢         │
  │       │ Chain tồn tại│ tạo chain qua connections │            │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  2    │ EXTEND       │ 4 cơ chế valence          │ 🟢🟡      │
  │       │ Chain kéo dài│ propagation (§5)           │            │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  3    │ FIT          │ Pyramidal compression cho │ 🟢🟡      │
  │       │ Chain fit PFC│ chain dài vào 4±1 chiều   │            │
  ├───────┼──────────────┼───────────────────────────┼────────────┤
  │  4    │ FILTER       │ Group selection giữ lại   │ 🟡🔴      │
  │       │ Chain survive│ cá nhân có chain dài      │            │
  └───────┴──────────────┴───────────────────────────┴────────────┘


  TẦNG 1 — CHUNK SUBSTRATE TỰ NHIÊN TẠO CHAIN (EXIST):

    Chunk.md v2.2 §3: 4 loại connection GIỮA chunks:
      Type 1: Shared Contamination — neurons chung fire lẫn nhau (VÔ THỨC, automatic)
      Type 2: Aha Moment — DMN incubation → sudden burst link
      Type 3: Meta-chunk Compile — fire cùng nhau nhiều lần → merge thành 1 unit
      Type 4: Static Logical Linking — PFC chủ đích hold + check

    Chain dài KHÔNG ĐƯỢC "thiết kế". Nó EMERGE từ:
      → Type 1: spreading activation tự lan theo TẤT CẢ links (Collins & Loftus 1975)
      → Type 3: chunks → meta-chunks → schemas → hierarchy (Hebb 1949)
    → Chunk system KHÔNG CÓ giới hạn "chỉ link gần"
    → Chain dài = side effect TẤT YẾU của cách chunk compile

    🟢 Spreading activation: Collins & Loftus 1975
    🟢 Hebbian learning: Hebb 1949
    🟢 Associative network models: Anderson 1983


  TẦNG 2 — VALENCE PROPAGATION KÉO DÀI CHAIN (EXTEND):

    §5 đã mô tả 4 cơ chế propagation. Vai trò cho chain DÀI:
      ① Forward: body TỰ TÌM path tới reward → path càng xa = chain càng dài
      ② Backward: reward ở cuối → valence spread NGƯỢC → "kéo dài" chain về phía gốc
      ③ Lateral: mở RỘNG chain sang entities tương tự (category generalize)
      ④ Install: cộng đồng install chain DÀI (5+ nodes) NGAY LẬP TỨC

    Install Propagation (④) giải thích chain dài ở TRẺ EM:
      → Trẻ chưa có đủ direct experience để build chain dài
      → NHƯNG bố mẹ install: "học → tương lai → sung sướng" = chain 3+ links
      → = Chain dài CÓ THỂ xuất hiện TRƯỚC khi vô thức kịp compile

    🟢 Temporal difference learning (Schultz 1997) supports backward propagation.


  TẦNG 3 — PYRAMIDAL COMPRESSION CHO CHAIN DÀI FIT VÀO PFC (FIT):

    ⚠️ ĐÍNH CHÍNH: "PFC lớn hơn → chain dài hơn" = SAI
      → 🟢 Brain size vs IQ: tương quan RẤT YẾU (~0.24, ~6% variance)
         (Pietschnig 2015, meta-analysis 148 studies)
      → PFC luôn chỉ hold 4±1 dimensions (physics limit — interference)
         (🟢 Cowan 2001)

    Chain dài FIT vào PFC bằng PYRAMIDAL COMPRESSION:
      → 4 chunks → compile → 1 meta-chunk
      → 4 meta-chunks → compile → 1 super-meta
      → 4×4×4 = 64 thông tin gốc compressed vào 1 slot PFC
      → "Nhìn 4 thứ nhưng THẤY cả vũ trụ" (expert) — PFC-Analysis.md

    Chain dài = sản phẩm của VÔ THỨC, không phải PFC:
      → Vô thức compile chunks → stack → pyramidal → compressed
      → PFC thấy chain "ngắn" (3-4 items) → thực ra = chain compiled SÂU
      → Chain dài KHÔNG cần "PFC lớn hơn" hay "PFC capacity cao hơn"
      → Chain dài cần VÔ THỨC COMPILE ĐỦ SÂU

    🟢 Chase & Simon 1973: expert chess 50,000+ chunk patterns
    🟢 Neural efficiency: Haier 1992, Neubauer & Fink 2009
    🟡 Chain length = f(compile depth): framework inference


  TẦNG 4 — GROUP SELECTION FILTER (FILTER):

    Giả thiết: chọn lọc tự nhiên ở cấp TẬP THỂ giữ lại gene cho chain dài.

    Nhóm CÓ chain dài:
      → Empathy, đầu tư dài hạn, hợp tác, truyền kiến thức
    Nhóm KHÔNG CÓ (chỉ valence trực tiếp):
      → Ít empathy, ít hợp tác, ít đầu tư → YẾU HƠN

    ⚠️ PHÂN BIỆT CAUSE vs FILTER:
      → Tầng 1-3 = CAUSE (tạo ra chain dài ở cấp cá nhân)
      → Tầng 4 = FILTER (giữ lại chain dài ở cấp tập thể)
      → Tầng 1-3 ĐÃ ĐỦ giải thích chain dài → Tầng 4 = optional

    🟢 Kin selection: Hamilton 1964. Reciprocal altruism: Trivers 1971.
    🟡 Group selection: Wilson 2007 (debated nhưng logic consistent)
    🔴 "Group selection cho chain dài" specifically = framework hypothesis
```

### §6.3 — Trade-off nền tảng: Chain dài = Feature, không Bug

```
🟡 CHAIN DÀI CÓ HẠN CHẾ CHO CÁ NHÂN:

  ① PFC BLIND → confabulate → dễ bị exploit
  ② TRAUMA chain compiled sâu → PFC đoán sai gốc → fix sai
  ③ UNFALSIFIABLE chains → sacrifice phi lý (tử vì đạo → Thiên Đàng)

  NHƯNG — xét XÁC SUẤT TỔNG THỂ, chain dài = NET POSITIVE:

  ┌──────────────────────┬────────────────────────────────────────┐
  │ Hại (cá nhân, ít)    │ Lợi (tập thể, nhiều)                  │
  ├──────────────────────┼────────────────────────────────────────┤
  │ PFC blind → bị       │ Empathy → share khi thừa → nhóm khỏe │
  │ exploit đôi khi      │                                        │
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
    → Chain dài CÙNG LOGIC: đôi khi PFC blind gây hại cá nhân
    → Nhưng P(empathy + cooperation + deferred investment) >> P(harm)

  🟢 Immune system trade-off: established evolutionary biology
  🟡 Chain dài as analogous trade-off: framework reasoning, logic consistent


  TÓM TẮT — CHAIN DÀI = EMERGENT, KHÔNG DESIGNED:

    TẦNG 1: Chunk Substrate    → Chain EXIST (side effect tất yếu)
    TẦNG 2: Valence Propagation → Chain EXTEND (4 cơ chế + install)
    TẦNG 3: Pyramidal Compress  → Chain FIT vào PFC (quality, không size)
    TẦNG 4: Group Selection     → Chain SURVIVE qua evolution (filter)
```

---

## §7 — CASES PHÂN TÍCH

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

    ⚠️ CỤ THỂ internal schemas NÀO drive Jensen Huang = CHỈ ÔNG ẤY BIẾT.
    Framework chỉ có thể INFER từ observable behavior, KHÔNG phải đọc vị chính xác.


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
    Reward khi giết: mastery (control) + identity confirm + threat resolution
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
    Compiled patterns fire ĐÚNG theo valence system → PFC thấy "phi lý" vì PFC chỉ thấy L1
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

  F3) Positive childhood → default trust người lạ:
    = POSITIVE overgeneralize (ngược với F1):
    Nhiều agents positive → category "người" = positive (lateral)
    → Gặp người lạ → default approach → sẵn sàng giúp
    = CÙNG CƠ CHẾ, khác hướng (positive vs negative)
    = NHƯNG: cần NHIỀU experience hơn (negativity bias asymmetry)
```

---

## §8 — PFC BLINDNESS + CONFABULATION

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

  ③ PFC KHÔNG BIẾT (chain invisible, hardware, compiled):
    "Tôi thích từ thiện" — PFC: "vô tư." Body: nhiều compiled chains fire.
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
        → Mỗi bí ẩn vật lý = prediction-delta → VTA fire → dopamine + opioid
        → = Body fire reward CỰC MẠNH khi gặp mystery → PFC label: "beautiful"

      NHƯNG — body-base fire CÙNG CƠ CHẾ cho MỌI NGƯỜI, chỉ khác INPUT:
        → Einstein: sướng vì gặp mystery vật lý (chunk physics + hardware fit)
        → Đầu bếp: sướng vì nấu món vừa ý (chunk cooking + hardware fit)
        → Nhạc sĩ: sướng vì sáng tác giai điệu hay (chunk music + hardware fit)
        → = CÙNG opioid pathway, CÙNG prediction-delta, CÙNG Goldilocks reward
        → = Khác CHUNKS + khác HARDWARE → khác INPUT trigger → CÙNG body-base fire

      Einstein nghĩ "mystery" là đặc biệt vì PFC của ÔNG ẤY chỉ thấy chain CỦA ÔNG.
      Ông không thấy: đầu bếp CŨNG "rapt in awe" khi nấu món hoàn hảo.
      = PFC confabulation + identity schema ("physicist = cách sống đúng")
      = Mỗi người TƯỞNG domain CỦA MÌNH là đặc biệt → vì body CỦA HỌ fire mạnh nhất ở đó


  "VÔ TƯ" VÀ "ĐAM MÊ" — 2 CONFABULATION PHỔ BIẾN NHẤT:

  ⭐ "CHO ĐI VÔ TƯ":
    PFC: "Tôi giúp người khác. Vô tư. Không mong đợi gì."
    Compiled patterns fire (ví dụ — không cố định, per person):
      → Giúp → họ improve → empathy → opioid (+)
      → Giúp → "tôi = người tốt" → identity (+)
      → Giúp → community see → status (+)
      → Giúp → bond → future reciprocal access (+)
    Net: nhiều chains reward >> cost → body drive "giúp"
    
    "Vô tư" = ĐÚNG từ góc nhìn PFC (PFC thật sự không thấy chain)
    "Vô tư" = SAI từ góc nhìn body (compiled patterns LUÔN fire, luôn có reward)
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
    Compiled patterns fire:
      Hardware fit: processing style match physics thinking
      Chunk accumulation: years of practice → Goldilocks zone
      prediction-delta: mỗi insight → prediction-delta → dopamine
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

## §9 — GIỚI HẠN NỀN TẢNG + 3 NGUYÊN TẮC

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
      Chuyên gia tâm lý giỏ Self-Pattern-Match (feel-check)
      Client giỏi body-verify (Focusing, Somatic-Articulation-Loop)
      = 3 tầng: AI detect → Chuyên gia feel-check → Client self-verify
      = Không cần chính xác tuyệt đối. Approximate + verify = ĐỦ.
      → (Chi tiết: AI-Schema-Detection.md v2.0)


⭐ 3 NGUYÊN TẮC QUAN TRỌNG:

  NGUYÊN TẮC 1 — Schema Effectiveness ≠ Schema Truthfulness:

    Schema CÓ THỂ sai hoàn toàn về content MÀ VẪN effective:
      → Tin Thiên Đàng: unfalsifiable, chưa verify → NHƯNG behavioral output
        (chăm chỉ + đạo đức) → body-base feed → EFFECTIVE
      → Patriotic schema: install chain qua education + media + ritual
        → drive bảo vệ cộng đồng → body-base feed → EFFECTIVE
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
      → = PFC chỉ question khi CÓ VẤN ĐỀ, không question khi MỌI THỨ ỔN

  NGUYÊN TẮC 3 — "Vô Tư" Đúng Ở Tầng PFC, Sai Ở Tầng Body:

    2 TẦNG OBSERVATION khác nhau cho CÙNG 1 hành vi:

    TẦNG PFC (conscious experience):
      → PFC thấy: "Tôi muốn giúp. Không mong gì."
      → PFC THẬT SỰ không thấy reward chains
      → → Từ góc nhìn PFC: "vô tư" = MÔ TẢ ĐÚNG conscious experience

    TẦNG BODY (compiled patterns fire):
      → Compiled patterns fire: nhiều chains reward → net positive → drive "giúp"
      → Compiled patterns LUÔN fire, LUÔN có reward
      → → Từ góc nhìn body: "vô tư" = SAI — always reward-driven

    CẢ HAI ĐÚNG — ở tầng riêng:
      → Không nên nói "cho đi vô tư là giả" (PFC experience THẬT)
      → Không nên nói "cho đi thật sự vô tư" (body computation CÓ reward)
      → = 2 tầng observation KHÁC NHAU cho cùng 1 phenomenon
      → = Feeling.md v2.0 core claim: "Feeling = PFC observation of body"

    IMPLICATION:
      → "Cho đi" CÓ GIÁ TRỊ: cả người cho lẫn người nhận đều benefit
      → Biết mechanism KHÔNG LÀM GIẢM giá trị
      → Biết mechanism CÓ THỂ GIÚP: hiểu khi nào sẽ dừng (3 violation tests)
      → = Framework mục đích: HIỂU, không phải PHÁN XÉT
```

---

## §10 — HONEST ASSESSMENT

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

  Entity-Compiled evidence:
    → Grief as body-level pain: Eisenberger 2003
    → Attachment bond: Bowlby 1969
    → Empathy fatigue: Figley 2002
    → Adolescent ambivalence toward parents: established developmental psychology
    → Emotional intensity → memory strength: McGaugh 2004


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

  §3 Entity-Compiled (v2.0 NEW/REWRITE):
  → "Entity-Compiled" reframe terminology: 🟡 framework synthesis
  → 3 subtypes (positive/negative/mixed): 🟡 framework categorization
     (each subtype maps to established phenomena — ambivalence, attachment, obsession)
  → Mixed = most common: 🟡 logical inference from multi-channel model
     (more channels compile = more mixed; long relationships = more channels)
  → Entity-Compiled vs Obligation = independent: 🟡 framework synthesis
     (observable: bạn thân ≠ ân nhân; consistent with 2-mechanism model)
  → Developmental trajectory (0-5 → ③ emerge → adult): 🟡 framework synthesis
     (consistent with 🟢 developmental psych — adolescent ambivalence)
  → 2-luồng separation (L1 SPM-owned / L2 Entity-Compiled): 🟡 framework synthesis
     (consistent with 🟢 compassion fatigue research — Figley 2002)
  → 3-cost annotation (PFC draft + suppress + uncertainty): 🟡 framework synthesis
     (each component 🟢 individually; unified model 🟡)

  §6 Chain dài (merged from v1.4 §5+§5b):
  → Tầng 1 EXIST (chunk substrate tạo chain): 🟢 established mechanisms
  → Tầng 2 EXTEND (valence propagation kéo dài): 🟢🟡 mixed
  → Tầng 3 FIT (pyramidal compression): 🟢🟡
  → Chain dài = f(vô thức quality, KHÔNG PHẢI PFC size): 🟡
  → Tầng 4 FILTER (group selection cho chain dài): 🟡🔴
  → Trade-off (chain dài = feature, not bug): 🟡


HYPOTHESIS (🔴):

  → Valence propagation as EXPLICIT NAMED MODEL:
    Concept IMPLICIT trong spreading activation + conditioned reinforcement,
    nhưng explicit formalization "valence propagation qua schema chain" = MỚI.

  → Backward propagation (reward → valence spread ngược):
    🟢 Temporal difference learning (Schultz) supports.
    🔴 NHƯNG: cơ chế CỤ THỂ cho "valence spread backward through abstract chain"
    chưa formalize trong neuroscience.

  → Chain trust = product of link trusts:
    Mathematical model. Likely OVERSIMPLIFIED.

  → Group selection cho chain dài (§6.2 Tầng 4):
    🔴 Specific hypothesis. Logic consistent, chưa direct evidence.
    Tầng 1-3 ĐÃ ĐỦ → Tầng 4 = optional.


⚠️ BLACKBOX 2: Valence complexity — chuỗi valence dài (trauma compiled mờ
  + hormone shift + hardware variants + multi-layer interaction) gần như
  incomputable. Framework predict PATTERN, không predict INSTANCE cụ thể.
  Chi tiết: Blackbox-Map.md §4 + §7.
  UPDATE: BB2 = BB1 + collective scale + hardware variance (Collective-Body.md §1).

  §5 Clarification (v1.4→v2.0): Chain analysis = Cấp 3 EXPLANATORY, không phải
  Cấp 1 processing. 3 cấp phân tích formalized.
  🟡 Framework synthesis dựa trên drill findings — logic consistent.


CÂU HỎI MỞ:

  → Cơ chế neural CỤ THỂ cho valence propagation? Brain regions? Circuits?
  → Chain decay function: linear? exponential? step? Context-dependent?
  → Maximum chain length mà body vẫn "trust"?
    ⤷ §6.2 Tầng 3: chain length bị giới hạn bởi pyramidal compression quality,
      KHÔNG phải absolute limit. Maximum = f(compression quality × link trust).
  → Khi nào chain BỊ ĐỨT vs khi nào body REPAIR?
  → Filter mechanism: body có filter nào cho "chain NÀY đáng trust"?
  → Positive overgeneralize: same mechanism nhưng KHÁC TỐC ĐỘ bao nhiêu?
  → AI-assisted schema detection: CAN HAPPEN? HOW? (→ AI-Schema-Detection.md)
  → Entity-Compiled subtypes: precise boundary giữa ①②③? Có gradient hay threshold?
  → Mixed coupling grief: HOW LONG does complex grief (relief+pain) take to resolve?
```

---

## §11 — CROSS-REFERENCES + STATUS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Body-Base.md v2.1 — L0-L3 channels mà valence đánh giá
    → Body-Input-Enumeration.md — reframe L0-L3, body-inputs chi tiết
    → Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate (§1), 2 sources, 3 dynamics
    → Schema.md v2.0 §1-§1.2 — schema = chunks + links + purpose, KHÔNG THỂ phân tích
    → Chunk.md v2.2 — chunk substrate, context-tag, 4 connections (§6.2 Tầng 1)
    → Reward-Signal-Architecture.md v1.0 — Type A/B × valence: A = evaluative valence,
      B = direct state valence. Valence propagation = primarily Type A territory
    → Framework-Label.md v3.0 — vocabulary reference (3-tier labels)

  ENTITY-COMPILED + COUPLING:
    → Inter-Body-Mechanism.md v1.0 — §8 Entity-Compiled reframe (3 subtypes),
      §4 3-cost model, §5 By-Product Match, §7 PFC=Lawyer
    → Body-Coupling.md v1.1 — coupling mechanism deep-dive: 2D model (|❸| Depth × Direction),
      3 Phase, extension/entanglement/neutral, system compilation — extends §3
    → Connection.md v3.3 — 3 Generative Primitives, §3.3 2-luồng reward overview
    → Agent-Mechanism.md v1.0 — §12 body-need feeder, §12.2b L1/L2 transition
    → Self-Pattern-Match.md v2.4 — F1/F2, §10 reversed mapping (Schadenfreude, sadism)
    → Obligation.md v1.0 — compiled prediction (INDEPENDENT of Entity-Compiled, §3.5)
    → Protect.md v1.0 — f(replaceability × attachment), loss aversion

  PROPAGATION CONTEXT:
    → Collective-Body.md v1.2 §1-§2 — Model 3 cấp + trust bridge (§5 Clarification)
    → Anchor-Schema.md v1.2 §1-§2 — anchor amplify chain, trust ≥ cost → hold
    → Emergent-Patterns.md §5 — "Cho đi" pattern, 4 nguồn reward
    → Empathy.md v2.2 §6 — empathy reward override spectrum (lành mạnh → compulsive)
    → Somatic-Articulation-Loop.md — body knowledge → explicit knowledge

  PFC + FEELING:
    → Feeling.md v2.0 §2 — 7-layer fidelity gradient (Layer 7 = 20-70% accuracy)
    → Feeling.md v2.0 §3 — core claim: feeling = PFC observation of body
    → Drive.md §0 — schema = DETECTOR, vô thức = ENGINE, PFC = navigator
    → PFC-Analysis.md — pyramidal compression, 4±1 dimensions (§6.2 Tầng 3)

  APPLICATION:
    → AI-Schema-Detection.md v2.0 — AI-assisted schema pattern detection
    → Imagine-Final-Evaluation.md — Mismatch quadrant (§7 case D3)

  CŨ (đã backup):
    → Domain/backup/Valence.md — per-entity valence DRAFT v0.5
      (content integrated vào §1-§2 file NÀY)


STATUS:

  v1.0 — 2026-04-18 — Session N+16
    → Initial version: §0-§10, per-entity + propagation + chain + cases + PFC blindness
  
  v1.1 — 2026-04-18 — Session N+19
    → THÊM §5b: "Tại Sao Chain Dài Tồn Tại: 4 Tầng Cơ Chế"
    → UPDATE §9: thêm confidence cho §5b
    → ĐÍNH CHÍNH: "PFC lớn hơn → chain dài" = SAI
    → FIX terminology: "mirror reward" → "empathy reward"

  v1.3 — 2026-04-28
    → UPDATE §2: thêm Body-Coupling.md reference note
    → UPDATE §10: thêm cross-ref Body-Coupling.md v1.0

  v1.4 — 2026-05-08
    → THÊM §4 Clarification: Explanatory vs Processing (Drill §6, §22)
    → GAP 13 (CRITICAL) RESOLVED + GAP 8 RESOLVED
    → THÊM §1 ④ "No Source Tag"
    → Cross-ref: Collective-Body.md §1-§2

  v2.0 — 2026-05-16 — FULL REWRITE (Inter-Body Drill integration)
    → ⭐ §3 REWRITE: Entity-Owned → Entity-Compiled (3 subtypes)
      Mixed valence = most common. Developmental trajectory.
      Entity-Compiled vs Obligation = independent.
      3-cost model reference. Body-Coupling.md deep-dive pointer.
    → §2 RESTRUCTURE: tách Entity-Compiled thành §3 riêng (was lumpy)
    → §5+§5b MERGE → §6: Chain Properties + Why Chain Dài (mạch lạc hơn)
    → §0 UPDATE: +Body-Need aggregate reference (BFM v2.0 §1),
      +Inter-Body-Mechanism.md v1.0 refs, flow diagram updated
    → §10 UPDATE: +🟡 Entity-Compiled (3 subtypes, mixed, trajectory, L2 vs obligation)
      +🟡 3-cost annotation, +⚠ open questions Entity-Compiled boundaries
    → §11 UPDATE: +Inter-Body refs, +BFM v2.0 refs, all file versions updated
    → ALL research citations preserved (30+ from v1.4 + new: McGaugh 2004, Eisenberger 2003 expanded)
    → ALL signature examples preserved (Miep Gies, Jensen Huang, Einstein, 100k, Chị-A/B)
    → v1.4 → backup/Valence-Propagation-v1.4-backup.md
```
