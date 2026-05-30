---
title: Liking-Wanting — Bridge File Từ Berridge Đến Framework
version: 2.0
created: 2026-04-18
updated: 2026-05-24 (v2.0 — Reward-Signal-Architecture Evaluative/Direct-State integration, Simulation-Engine refs, cross-refs fixed)
previous: v1.1 (2026-05-23 Concept Cascade: +Bond-Architecture × wanting, +Satiation × liking, +Hardware-Subsidy × wanting)
status: v2.0 — BRIDGE FILE (mainstream reader entry point)
scope: |
  Map thuật ngữ wanting/liking (Berridge-Robinson 1998) sang kiến trúc framework.
  KHÔNG phải framework tool — là BRIDGE cho reader quen mainstream neuroscience.
  Giúp reader chuyển TỪ binary wanting/liking SANG kiến trúc multi-mechanism.
  v2.0 KEY: +Evaluative/Direct-State Reward distinction (Reward-Signal-Architecture v2.0) vào liking analysis.
  Berridge "liking" ≈ Evaluative Reward only. Direct-State Reward = loại Berridge chưa address.
purpose: |
  Reader biết Berridge sẽ hỏi: "Wanting/liking CỦA framework là gì?"
  File này trả lời câu hỏi đó, rồi CHỈ RÕ tại sao framework đi xa hơn binary.
  Entry point → reader sẽ được dẫn sang các file chi tiết.
dependencies:
  - Dopamine-Is-Not-Reward.md v1.0 — 7 bằng chứng + 7-step + framework endorse Berridge
  - 03-Reward.md (Body-Feedback/) — 5 Body-Feedback-Preconditions, 7-step mechanism chi tiết
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles
  - Imagine-Final.md v3.0 — constructive future simulation, 3-Layer, lifecycle
  - Simulation-Engine.md v1.0 — 1 engine, 3 components, 3 axes
  - Anchor-Schema.md v1.0 — Trust binding, 4 nguồn fill, cost
  - Valence-Propagation.md v3.0 — per-entity + chain propagation + PFC blindness
  - Drive.md v1.2 — integration hub, vô thức ENGINE + PFC NAVIGATOR
  - Novelty.md v1.2 — VTA seismograph + habituation detection
  - Feeling.md v3.0 — PFC observation of body, 7-layer fidelity
  - Entity-Compiled.md v1.0 — HOW entities compile into body-base
  - Bond-Architecture.md v2.0 — 4 bond types, gap clone impossible
  - Gap-Body-Need.md v1.0 — 3 Satiation Types, 5-Parameter
parent: Drive.md v1.2 (integration hub)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Liking-Wanting — Bridge File Từ Berridge Đến Framework

> **Bạn biết "wanting" và "liking" — hai khái niệm của Berridge-Robinson.**
> **Framework ĐỒNG Ý với Berridge: dopamine ≠ reward, wanting ≠ liking.**
> **Nhưng framework nhìn thấy CƠ CHẾ SÂU HƠN phía sau cả hai.**
>
> "Wanting" = NHIỀU mechanisms khác nhau, không chỉ 1 signal.
> "Liking" = reward CÓ ĐIỀU KIỆN, không phải tự động.
>
> File này: BRIDGE — từ Berridge → framework.
> Nếu bạn đang nghĩ theo wanting/liking, đây là cách framework
> nhìn CÁI TƯƠNG TỰ — nhưng chi tiết hơn, falsifiable hơn.
>
> **⚠️ FILE NÀY KHÔNG PHẢI FRAMEWORK TOOL.**
> Framework dùng: Imagine-Final + Body-Base + VTA 7-step + Body-Feedback-Precondition + Valence chain.
> File này dùng: cho READER muốn 1 GÓC NHÌN BẮT ĐẦU.

---

## Mục lục

- §0 — VỊ TRÍ + MỤC ĐÍCH
- §1 — BERRIDGE WANTING/LIKING RECAP
- §2 — WANTING → FRAMEWORK: KHÔNG CHỈ "MUỐN"
- §3 — LIKING → FRAMEWORK: KHÔNG CHỈ "THÍCH"
  - §3.1-§3.4 — 4 Layers: Opioid, Body-Feedback-Precondition, Chain, 3 Signals
  - §3.5 — Layer 5: Evaluative vs Direct-State (Reward-Signal-Architecture v2.0)
  - §3.6 — Tổng hợp: 5 Layers
- §4 — 5 CASES QUA CẢ HAI LENS
- §5 — TẠI SAO FRAMEWORK KHÔNG DÙNG WANTING/LIKING
- §6 — HONEST ASSESSMENT
- §7 — CROSS-REFERENCES + READING GUIDE

---

## §0 — VỊ TRÍ + MỤC ĐÍCH

```
FILE NÀY TRONG FRAMEWORK:

  ┌─────────────────────────────────────────────────────────────┐
  │ Dopamine-Is-Not-Reward.md                                 │
  │   = "TẠI SAO dopamine ≠ reward?"                            │
  │   = Bác bỏ misconception, 7 bằng chứng, 7-step mechanism   │
  │   = Hướng: Classical "dopamine = pleasure" → Framework      │
  └──────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ FILE NÀY — Liking-Wanting.md                                 │
  │   = "Wanting/liking MAP vào framework THẾ NÀO?"             │
  │   = Bridge từ Berridge terminology → framework architecture │
  │   = Hướng: Reader biết Berridge → muốn hiểu framework      │
  └──────────────────────────┬──────────────────────────────────┘
                             │
                             ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ Framework files chi tiết                                     │
  │   Imagine-Final.md v3.0 / 03-Reward.md / Valence-Prop. v3.0│
  │   Reward-Signal-Architecture.md v2.0 (Evaluative/Direct-St.)│
  │   Anchor-Schema.md / Drive.md / Novelty.md / Feeling.md v3.0│
  │   = Cơ chế đầy đủ — reader đi sâu sau khi có bridge        │
  └─────────────────────────────────────────────────────────────┘


⭐ MỤC ĐÍCH BRIDGE FILE:

  CÂU HỎI CỦA READER:
    "Framework nói dopamine ≠ reward. Tôi hiểu rồi.
     Vậy wanting là gì? Liking là gì? Map vào đâu?"

  CÂU TRẢ LỜI CỦA FILE NÀY:
    1. Wanting ≈ Imagine-Final preview + nhiều mechanism khác
    2. Liking ≈ Body-Base opioid + Body-Feedback-Preconditions
    3. Nhưng binary wanting/liking = quá đơn giản
    4. Framework có tham số CHI TIẾT hơn → cover nhiều case hơn
    5. Đây là BRIDGE — không phải destination

  READER NÀO CẦN FILE NÀY:
    → Biết Berridge wanting/liking → muốn framework equivalent
    → Đọc xong → chuyển sang file chi tiết phù hợp
    → KHÔNG NÊN dùng wanting/liking như framework terminology
```

---

## §1 — BERRIDGE WANTING/LIKING RECAP

```
🟢 BERRIDGE-ROBINSON (1998, 2003, 2016) — ESTABLISHED RESEARCH:

  CORE FINDING (3 decades rat experiments + human neuroimaging):

    WANTING = INCENTIVE SALIENCE:
      → Dopamine-driven motivation to SEEK
      → "Tôi MUỐN cái đó — đi tìm!"
      → Mesolimbic dopamine pathway (VTA → NAcc)
      → Có thể "wanting" MÀ KHÔNG "liking" (addiction: crave nhưng không enjoy)

    LIKING = HEDONIC RESPONSE:
      → Opioid-mediated pleasure when RECEIVED
      → "Tôi THÍCH cái đó — pleasant!"
      → Opioid system (endorphin, enkephalin)
      → Có thể "liking" MÀ KHÔNG "wanting" (Parkinson's: enjoy nhưng không seek)

  BẰNG CHỨNG QUYẾT ĐỊNH:

    Rat block dopamine → VẪN like sugar (ăn khi được cho, facial pleasure)
                       → KHÔNG seek sugar (không bấm lever, không đi tìm)

    Rat stimulate dopamine → seek MORE (seeking tăng dramatic)
                           → enjoy SAME (facial pleasure KHÔNG tăng)

    → Dopamine = SEEKING system (wanting)
    → Opioid = PLEASURE system (liking)
    → 2 hệ TÁCH BIỆT — có thể dissociate


⭐ FRAMEWORK ĐỒNG Ý HOÀN TOÀN VỚI BERRIDGE:

    ✅ Dopamine ≠ pleasure
    ✅ Dopamine = motivation / salience signal
    ✅ Opioid = actual pleasure / reward
    ✅ Wanting và liking có thể dissociate
    ✅ Addiction = wanting pathological, liking giảm

    → Framework KHÔNG bác bỏ Berridge
    → Framework EXTENDS Berridge (thêm mechanism, thêm chi tiết)
    (Chi tiết: Dopamine-Is-Not-Reward.md §5)


⚠️ LIMITATION CỦA BERRIDGE MÀ FRAMEWORK ADDRESS:

    ① "Liking fires KHI NÀO?" → Berridge: opioid system (black box)
       → Framework: 5 Body-Feedback-Preconditions (testable, falsifiable)

    ② "Wanting chỉ 1 loại?" → Berridge: incentive salience (singular concept)
       → Framework: NHIỀU mechanisms tạo ra "wanting" behavior

    ③ "Chain-mediated?" → Berridge: direct stimulus → response
       → Framework: reward qua schema chain DÀI (Einstein, altruism)

    ④ "Compile context?" → Berridge: không address
       → Framework: chunk tag direction (opioid vs threat) tùy compile context
```

---

## §2 — WANTING → FRAMEWORK: KHÔNG CHỈ "MUỐN"

```
🟡 BERRIDGE "WANTING" = 1 THUẬT NGỮ CHO NHIỀU CƠ CHẾ KHÁC NHAU:

  Berridge gọi TẤT CẢ motivation-to-seek = "wanting".
  Framework nhìn thấy ÍT NHẤT 6 mechanisms khác nhau
  mà Berridge gom chung thành 1 từ.

  Mỗi mechanism có cơ chế KHÁC NHAU, can thiệp KHÁC NHAU,
  biểu hiện KHÁC NHAU — nhưng output quan sát GIỐNG NHAU:
  "Người đó đang MUỐN cái gì đó."
```

### §2.1 — Mechanism 1: Imagine-Final Preview (PFC simulate → body pre-feel)

```
🟡 CƠ CHẾ:

  PFC simulate trạng thái TƯƠNG LAI:
    → "Nếu tôi ăn món đó → body sẽ no + ngon"
    → "Nếu tôi gặp bạn đó → body sẽ vui"
    → "Nếu NVIDIA thành công → body sẽ significance + mastery"

  Simulation-Engine chạy preview (Simulation-Engine.md v1.0):
    → 1 engine, 3 components: Interoception × Constructive Simulation × Self/Other Model
    → Imagine-Final = APPLICATION (Self, Future, Simulate+Construct) trên engine
    → Body RESPONSE simulation ở ~20-60% fidelity (Imagination.md v2.0 §2)
    → Opioid PREVIEW nhẹ nếu simulation "mượt hơn hiện tại"
    → = "MUỐN tới đó" = wanting

  3-LAYER (Imagine-Final.md v3.0 §3):
    ① Body-Need (TẠI SAO): đói, cô đơn, muốn chứng minh giá trị...
    ② Imagine-Final (VỀ ĐÂU): "no + ngon", "vui", "NVIDIA thành reference"
    ③ Plan + Parameters (BẰNG CÁCH NÀO): recipe, gọi điện, chiến lược GPU

    ⚠️ "GPU sẽ có giá trị" = tầng ③ (PARAMETER hỗ trợ plan)
       KHÔNG PHẢI tầng ② (Imagine-Final)
       Jensen's Imagine-Final = "NVIDIA thành reference / chứng minh vision đúng"
       = Cái body ông ấy PRE-FEEL, không phải nhận định logic về thị trường

  → Berridge "wanting" gần nhất với mechanism NÀY
  → NHƯNG: Imagine-Final preview chỉ là 1 PHẦN của "wanting"
  → Cross-ref: Simulation-Engine.md v1.0 §5 (engine architecture)
```

### §2.2 — Mechanism 2: VTA Dopamine Alert (salience signal)

```
🟡 CƠ CHẾ:

  VTA detect DELTA (habituation-based — Novelty.md v1.2):
    → Pattern cũ ổn định → VTA habituate → im
    → Pattern MỚI xuất hiện → VTA: "BIẾN ĐỘNG!" → dopamine fire
    → DRD4 receptor filter: 4R sensitive / 7R coarse

  Dopamine → PFC: "CÓ GÌ ĐÓ ĐÁNG CHÚ Ý — xem thử!"
    → KHÔNG nói "cái đó TỐT" hay "cái đó THƯỞNG"
    → Chỉ nói "CÓ THAY ĐỔI" → PFC attend

  = Berridge "incentive salience" ≈ mechanism NÀY
  = NHƯNG: framework specify WHEN VTA fires (habituation delta)
    và Berridge chỉ nói "salience" (descriptive)

  = Step 2 trong 7-step mechanism (Dopamine-Is-Not-Reward.md §4.2)
  = CẦN THIẾT cho wanting, nhưng KHÔNG ĐỦ = wanting
```

### §2.3 — Mechanism 3: Compiled Schema Momentum (vô thức auto-drive)

```
🟡 CƠ CHẾ:

  Schema compiled 30 năm → chạy AUTO không cần PFC:
    → Jensen Huang: compiled schema "build computing future"
      → Body tự drive HƯỚNG ĐÓ mà PFC không cần nhắc
    → Musician: compiled schema "chơi nhạc" → ngồi vào đàn = auto
    → Mẹ: compiled schema "chăm con" → nghe con khóc = body react NGAY

  = "Tiếng gọi", "passion", "calling", "gut feeling"
  = Imagine-Final.md v3.0 §3 Tầng 1 VÔ THỨC:
    → Body ĐÃ CÓ long-Imagine-Final từ lâu
    → PFC thậm chí KHÔNG NAME được → nhưng body DRIVE rõ ràng

  Entity-Compiled (Entity-Compiled.md v1.0):
    → Khi entity compile vào body-base (formation 40→200h exposure)
    → Entity-level momentum: compiled entity → body auto-drive TOWARD entity
    → VD: mẹ = entity compiled sâu nhất → momentum KHÔNG CẦN PFC
    → = Mechanism 3 ở ENTITY level, không chỉ schema level

  KHÁC Mechanism 1 (Imagine-Final preview):
    → Mechanism 1 = PFC actively simulate → body respond
    → Mechanism 3 = schema ĐÃ compiled → body auto-drive KHÔNG CẦN PFC
    → = Wanting VÔ THỨC — Berridge gọi chung = "wanting"

  ⚠️ BERRIDGE KHÔNG PHÂN BIỆT:
    → Wanting ý thức (PFC simulate → preview) vs
    → Wanting vô thức (compiled schema → auto-drive)
    → Framework PHÂN BIỆT vì can thiệp KHÁC:
      - Ý thức: PFC evaluate → có thể override
      - Vô thức: compiled quá sâu → override cực khó → cần decompile
```

### §2.4 — Mechanism 4: Anchor-Schema Binding (Trust commit)

```
🟡 CƠ CHẾ:

  Anchor-Schema (Anchor-Schema.md §0-§2):
    → Vô thức CẦN sync point → chấp nhận 1 schema làm anchor
    → Trust binding = hệ thống COMMIT vào hướng đó
    → Trust CAO → drive MẠNH + resist change + cost cao khi từ bỏ

  "Wanting" = có thể là Trust binding:
    → "Tôi muốn làm bác sĩ" = Anchor-Schema compiled từ bố mẹ inject
    → PFC không BIẾT tại sao muốn → body drive vì Trust binding CAO
    → Berridge: "wanting". Framework: Anchor-Schema + Trust.

  4 nguồn fill anchor (Anchor-Schema.md §3):
    ① PFC Imagine-Final (PFC build + body accept)
    ② Hippocampus simulation (động vật KHÔNG CÓ PFC vẫn drive)
    ③ Compiled schemas (tự thành anchor khi đủ mạnh)
    ④ External inject (tôn giáo, xã hội, bố mẹ install trực tiếp)

  → Wanting từ nguồn ④ = KHÔNG do cá nhân chọn
  → Berridge "wanting" không address NGUỒN GỐC → gom tất cả = "wanting"
```

### §2.5 — Mechanism 5: Valence Chain Propagation (indirect wanting)

```
🟡 CƠ CHẾ:

  Valence-Propagation.md v3.0:
    → Valence TRUYỀN qua links trong schema network
    → PFC KHÔNG BIẾT chuỗi truyền này tồn tại

  "Muốn học toán" — Berridge: wanting.
  Framework nhìn thấy CHAIN:
    Toán → giỏi → mẹ khen → connection need → body reward
    = "Wanting toán" thực ra là wanting CONNECTION qua chain

  "Đam mê vật lý" — Berridge: wanting.
  Framework:
    Vật lý → hardware fit + chunk match + Goldilocks + prediction-delta
    = NHIỀU chains fire SONG SONG → net valence >> threshold → drive
    = PFC nói "đam mê". Body: nhiều compiled chains invisible

  → Wanting KHÔNG NẰM Ở TARGET — nằm ở BODY-NEED qua chain
  → Berridge "wanting for X" → Framework "body-need Y propagated via chain to X"
  → Can thiệp khác: block X ≠ fix Y (chuyển trường ≠ fix connection need)
```

### §2.6 — Mechanism 6: Self-Generated Threat (wanting = tránh mất)

```
🟡 CƠ CHẾ:

  Threat.md v1.2 — 3 loại threat-driven behavior:
    → PFC tự generate threat: "nếu tôi DỪNG → mất tất cả"
    → Body: cortisol → push AWAY from stopping → push TOWARD continuing
    → Output quan sát = "muốn tiếp tục" = Berridge "wanting"

  Jensen Huang example:
    → 30 năm build NVIDIA → compiled schema + anchor + trust
    → Self-generated threat: "dừng = phản bội vision + mất legacy"
    → Drive tiếp = TRÁNH MẤT, không phải thuần "muốn thêm"
    → Berridge: "wanting". Framework: THREAT avoidance.

  Gambling "muốn gỡ":
    → Thua → PFC generate threat: "nếu dừng = mất vĩnh viễn"
    → Body: cortisol push → tiếp tục chơi → output = "wanting to play"
    → Berridge: "wanting". Framework: threat-driven, NOT pure wanting.

  → CRITICAL: cùng output behavior, KHÁC hoàn toàn mechanism
  → Can thiệp khác: reduce threat ≠ reduce wanting signal
  → = Tại sao therapy for gambling ≠ "bớt muốn chơi"
    mà = "nhận ra threat tự generate + decompile"
```

### §2.7 — Tổng hợp: "Wanting" = 6 mechanisms gom chung

```
🟡 BẢNG TỔNG HỢP:

┌───┬──────────────────────────┬──────────────────────┬─────────────────────┐
│ # │ Mechanism                │ Drive từ đâu?        │ PFC biết không?     │
├───┼──────────────────────────┼──────────────────────┼─────────────────────┤
│ 1 │ Imagine-Final Preview    │ PFC simulate → body  │ ✅ Biết rõ          │
│   │                          │ pre-feel             │                     │
├───┼──────────────────────────┼──────────────────────┼─────────────────────┤
│ 2 │ VTA Dopamine Alert       │ VTA detect delta →   │ 🟡 Chỉ thấy "chú ý"│
│   │                          │ dopamine → PFC attend│                     │
├───┼──────────────────────────┼──────────────────────┼─────────────────────┤
│ 3 │ Compiled Schema Momentum │ Compiled schema auto │ ❌ PFC không biết   │
│   │                          │ fire → body drive    │ tại sao             │
├───┼──────────────────────────┼──────────────────────┼─────────────────────┤
│ 4 │ Anchor-Schema Binding    │ Trust commit →       │ ❌ Thường không biết│
│   │                          │ resist change        │ (confabulate lý do) │
├───┼──────────────────────────┼──────────────────────┼─────────────────────┤
│ 5 │ Valence Chain            │ Body-need qua chain  │ ❌ PFC chỉ thấy    │
│   │ Propagation              │ → surface target     │ target, không chain │
├───┼──────────────────────────┼──────────────────────┼─────────────────────┤
│ 6 │ Self-Generated Threat    │ PFC tự generate      │ 🟡 PFC nghĩ        │
│   │                          │ threat → cortisol    │ "muốn", body = sợ  │
└───┴──────────────────────────┴──────────────────────┴─────────────────────┘

  → Berridge GOM TẤT CẢ = "wanting" (incentive salience)
  → Framework PHÂN BIỆT 6 mechanisms
  → Cùng output behavior ("đang tìm kiếm cái gì đó")
  → KHÁC hoàn toàn cơ chế bên trong
  → KHÁC hoàn toàn cách can thiệp

  ⚠️ KHÔNG có nghĩa Berridge SAI:
    → Berridge ĐÚNG rằng wanting ≠ liking (tách 2 hệ)
    → Framework NÓI THÊM: wanting = ÍT NHẤT 6 mechanisms
    → = Phóng to microscope, không phải đổi microscope
```

---

## §3 — LIKING → FRAMEWORK: KHÔNG CHỈ "THÍCH"

```
🟡 BERRIDGE "LIKING" = OPIOID HEDONIC RESPONSE.
   FRAMEWORK ĐỒNG Ý — NHƯNG THÊM: KHI NÀO, QUA CHAIN NÀO, VÀ TAG GÌ.

  Berridge nói: "Liking = opioid system fires → pleasure."
  Framework hỏi tiếp: "Opioid fires KHI NÀO? Điều kiện gì?
    Qua đường nào? Và tại sao cùng stimulus mà khác người khác liking?"

  Framework trả lời = 5 layers mà Berridge chưa specify.
```

### §3.1 — Layer 1: Body-Base Opioid (Step 5 — core of liking)

```
🟡 CƠ CHẾ:

  7-step mechanism Step 5 (Dopamine-Is-Not-Reward.md §4.2):
    → PFC send chunk → body-base simulate
    → Body có active needs (đói, social, exploration, safety...)
    → Chunk fits need? → YES → OPIOID RELEASE = REWARD THẬT
    →                   → NO  → body "meh" → PFC discard

  = LÕI CỦA LIKING:
    → Subjective experience "pleasant", "satisfied", "eureka"
    → = Endogenous opioids (endorphin, enkephalin, dynorphin)
    → = Berridge ĐÚNG: liking = opioid

  NHƯNG: framework specify Step 5 NẰM SAU steps 1-4:
    1. Unconscious fire (24/7)
    2. VTA detect delta (dopamine alert)
    3. DRD4 filter (threshold)
    4. PFC spotlight (top-down boost)
    → 5. BODY-BASE CHECK ⭐

  → Liking KHÔNG XẢY RA một mình — liking xảy ra SAU quá trình
  → Berridge treat liking như isolated event. Framework: liking = Step 5 TRONG loop.
```

### §3.2 — Layer 2: 5 Body-Feedback-Preconditions (KHI NÀO opioid fires)

```
🟡 CƠ CHẾ:

  Body-Feedback-Precondition (03-Reward.md §3):

    Opioid fires WHEN ALL 5 preconditions met:

    ① Precondition-1 Directed-Gap
       → Body phải có need đang chờ fill / schema chờ resolve
       → No: ăn khi ĐÃ NO → sugar vào → body "meh" → no liking
       → Yes: ăn khi ĐANG ĐÓI → sugar vào → body "fill need!" → opioid
       → 🟢 Alliesthesia (Cabanac 1971): same food less pleasant when full

    ② Precondition-2 Chunk-Substrate
       → Đủ chunks substrate để decode + recognize incoming pattern
       → No: nghe nhạc jazz phức tạp lần đầu → "không hiểu" → no liking
       → Yes: nghe sau 10 lần → chunks build → recognize → "hay!" → opioid
       → = Van Gogh paradox: appreciation REQUIRES chunks (03-Reward.md §6)

    ③ Precondition-3 Delta-Gate
       → Biến động đủ lớn để VTA detect
       → No: bài hát nghe 100 lần → VTA habituate → "chán" (no delta)
       → Yes: bài hát nghe lần 5 → vẫn fresh đủ → VTA fire → attend → liking
       → = Hedonic treadmill at neural level (Brickman 1978 🟢)

    ④ Precondition-4 Match-Range
       → Match ratio không quá cao (boring) cũng không quá thấp (confusion)
       → No: match quá cao = "biết rồi" = no delta → no liking
       → No: match quá thấp = "không hiểu gì" = confusion → cortisol → no liking
       → Yes: match vừa phải = "quen nhưng mới!" = sweet spot → opioid
       → 🟢 Berlyne optimal arousal, inverted-U curve

    ⑤ Precondition-5 Compile-Gate
       → Chunk tag opioid-associated (not threat-tagged)
       → No: chunk compiled lúc cortisol cao → threat-tagged → retrieval = discomfort
       → Yes: chunk compiled lúc cortisol thấp → opioid-tagged → retrieval = comfort
       → = CÙNG CONTENT, KHÁC TAG → khác liking
       → (Cortisol-Baseline.md v2.1: compile direction gate)

  BERRIDGE'S OPEN QUESTION (2016):
    "What determines when liking fires?"
    → Framework answer: 5 Body-Feedback-Preconditions.
    → Each precondition testable + falsifiable independently.
```

### §3.3 — Layer 3: Chain-Mediated Liking (indirect reward)

```
🟡 CƠ CHẾ:

  Berridge experiments = DIRECT stimulus → response:
    → Sugar vào miệng → opioid → liking ✅
    → = Simple, observable, replicable

  NHƯNG: nhiều liking trong đời thực = QUA SCHEMA CHAIN:

    Einstein Eureka:
      Schema dissonance (gap lớn trong vật lý) + chunk MỚI fits gap
      → Chain: chunk → schema match → dissonance resolved → opioid BURST
      → = Liking qua chain "knowledge gap → fill"
      → = KHÔNG có sugar, KHÔNG có direct stimulus
      → = Opioid fires qua ABSTRACT chain

    Altruism (Valence-Propagation.md v3.0):
      Giúp người lạ → PFC: "vô tư thôi"
      Body: mirror reward + status chain + identity chain + connection need
      → Nhiều compiled chains fire SONG SONG → net opioid >> cost → "feel good"
      → PFC KHÔNG BIẾT chains → confabulate "vì tử tế"
      → = Liking qua INVISIBLE MULTI-CHAIN

    Studying children (Imagine-Final.md v3.0 §3):
      Trẻ THÍCH học: curiosity compiled → mastery need → giải bài = opioid
      → Chain: bài toán → giải được → mastery → body reward
      Trẻ BỊ ÉP học: safety need (tránh phạt) → hoàn thành = relief, NOT opioid
      → Chain: bài toán → xong → không bị mắng → cortisol DROP (relief)
      → = CÙNG behavior, KHÁC chain, KHÁC loại "liking"

  → Berridge "liking" = chủ yếu direct (sugar, food, sex)
  → Framework: liking = CŨNG qua chain dài, invisible, multi-layered
```

### §3.4 — Layer 4: 3 Body Signals (không chỉ 1 loại "liking")

```
🟡 CƠ CHẾ:

  Body-Feedback-Mechanism.md v2.0 — 3 body signals, KHÔNG CHỈ 1:

    ① Body-Satisfaction ("đủ rồi"):
       → Homeostasis need MET → body signal "stop seeking"
       → VD: ăn no → "đủ rồi, dừng ăn"
       → = Liking? Sort of — nhưng drive = DỪNG, không phải "tiếp"

    ② Body-Reward ("hay, tiếp!"):
       → Chunk fit body-need beyond maintenance → opioid → "MORE"
       → VD: Eureka, flow state, social bonding, mastery breakthrough
       → = Berridge "liking" ≈ signal NÀY

    ③ Body-Dissonance ("chưa ổn"):
       → Current state ≠ expected → "SOMETHING WRONG"
       → VD: đang vui → bạn nói lạnh nhạt → dissonance
       → = KHÔNG phải liking — nhưng body feedback cùng hệ

  → Berridge "liking" = chủ yếu signal ② (Body-Reward)
  → Framework phân biệt ① ② ③ vì can thiệp KHÁC:
    - "Đủ rồi" cần STOP → nếu không stop = overdo
    - "Hay, tiếp" cần TIẾP → nếu stop = miss opportunity
    - "Chưa ổn" cần ADJUST → nếu ignore = accumulate dissonance
```

### §3.5 — Layer 5: Evaluative vs Direct-State Reward (2 LOẠI reward khác nhau)

```
🟡 CƠ CHẾ (Reward-Signal-Architecture.md v2.0 §1):

  BERRIDGE "LIKING" = CHỈ EVALUATIVE REWARD:

    EVALUATIVE REWARD:
      → Circuit: Hedonic hotspot (NAcc shell, VP, mOFC)
      → Signal: μ-opioid
      → Body-Feedback-Precondition: Full 5 preconditions REQUIRED
      → Cần: Compiled chunks (Precondition-2 Chunk-Substrate) + body-need gap (Precondition-1 Directed-Gap)
      → LEARNED — quality depends on chunk library
      → VD: food, music, insight, visual beauty, social praise
      → = Berridge "liking" ≈ TOÀN BỘ nằm ở đây

    DIRECT-STATE REWARD:
      → Circuit: Interoceptive / body-state regulation (VARIES by modality)
      → Signal: KHÔNG PHẢI opioid chính:
        Touch: CT afferents → posterior insula (🟢 Löken 2009)
        Exercise: Endocannabinoid CB1 (🟢 Fuss 2015 PNAS)
        Temperature: thermoreceptor → hypothalamus
      → Body-Feedback-Precondition: SIMPLIFIED (Precondition-1 basic, Precondition-2–Precondition-5 reduced/N/A)
      → Hardware từ sinh — MINIMAL compiled chunks needed
      → VD: touch comfort, runner's high, warmth, stretching
      → = Berridge KHÔNG STUDY loại này


  TẠI SAO QUAN TRỌNG CHO LIKING ANALYSIS:

    ① Berridge chỉ đo Evaluative (opioid-mediated hedonic hotspot):
       → Naltrexone blocks Evaluative → "liking blocked"
       → NHƯNG: touch comfort (Direct-State) NOT blocked by naltrexone
       → = CÓ liking experiences mà Berridge framework KHÔNG CAPTURE

    ② "Thích" trong đời thực = BLEND Evaluative + Direct-State:
       Social touch: Direct-State (CT afferents) + Evaluative (ai chạm?)
       → Bạn thân chạm: Evaluative AMPLIFY Direct-State → compound pleasant
       → Người lạ chạm: Evaluative SUPPRESS Direct-State → unpleasant dù CT vẫn fire
       → Infant: Evaluative chưa compile → Direct-State raw → mọi touch accepted
       → = Evaluative Gates Direct-State (Reward-Signal-Architecture v2.0 §3)

    ③ Direct-State = BURNOUT-PROOF:
       → Evaluative exhausted (anhedonia) → Direct-State VẪN hoạt động
       → "Touch still good" khi "nothing feels rewarding anymore"
       → = Therapeutic backdoor qua stuck Evaluative gate
       → 🟢 Van der Kolk 2014: body-oriented approaches for trauma

    ④ E₀→E₃ gradient = Evaluative KHÔNG monolithic:
       → E₀ (hardware-install): sweet taste (from birth, evolution pre-compiled)
       → E₁ (basic compiled): food preferences (~2-6 years)
       → E₂ (complex compiled): music appreciation, wine tasting (years)
       → E₃ (deep compiled): mathematical beauty, expert insight (decades)
       → = Evaluative Reward GROWS with compilation depth
       → = WHY "reward capacity" DEVELOPS, not fixed at birth

    ⑤ Body-Feedback-Precondition × 2 loại — layers 1-4 chủ yếu mô tả EVALUATIVE pathway:
       → 5 Body-Feedback-Preconditions (§3.2) apply MAINLY to Evaluative Reward
       → Direct-State: Precondition-1 basic (body-need always present), Precondition-2–Precondition-5 reduced/N/A
       → = Direct-State RELIABLE, Evaluative CONDITIONAL
       → = Tại sao layers 1-4 (opioid, Body-Feedback-Precondition, chain, signals) chủ yếu map EVALUATIVE

  → Berridge: "liking = opioid" → Framework: "EVALUATIVE liking = opioid"
  → Framework thêm: Direct-State liking = non-opioid, hardware, always available
  → = THÊM 1 DIMENSION mà wanting/liking binary KHÔNG CÓ
  → Cross-ref: Reward-Signal-Architecture.md v2.0 §1-§3 (full architecture)
```

### §3.6 — Tổng hợp: "Liking" = reward CÓ ĐIỀU KIỆN + CÓ LOẠI

```
🟡 BẢNG TỔNG HỢP:

┌───┬───────────────────────────────────┬──────────────────────────┬─────────────────┐
│ # │ Layer                             │ Framework specify        │ Berridge address│
├───┼───────────────────────────────────┼──────────────────────────┼─────────────────┤
│ 1 │ Body-Base Opioid                  │ Step 5 trong 7-step loop │ ✅ Core concept │
├───┼───────────────────────────────────┼──────────────────────────┼─────────────────┤
│ 2 │ 5 Body-Feedback-Preconditions     │ KHI NÀO opioid fires    │ ❌ "Black box"  │
├───┼───────────────────────────────────┼──────────────────────────┼─────────────────┤
│ 3 │ Chain-Mediated                    │ Reward qua schema chain  │ ❌ Chỉ direct   │
│   │                                   │ (dài, invisible, multi)  │ stimulus        │
├───┼───────────────────────────────────┼──────────────────────────┼─────────────────┤
│ 4 │ 3 Body Signals                    │ Satisfaction / Reward /  │ 🟡 Chỉ focus    │
│   │                                   │ Dissonance              │ "liking" = 1    │
├───┼───────────────────────────────────┼──────────────────────────┼─────────────────┤
│ 5 │ Evaluative vs Direct-State        │ 2 LOẠI reward: opioid   │ ❌ Chỉ study    │
│   │                                   │ (Evaluative) + non-opioid│ Evaluative      │
│   │                                   │ (Direct-State) + E₀→E₃  │ (opioid side)   │
└───┴───────────────────────────────────┴──────────────────────────┴─────────────────┘

  → Berridge: liking = opioid hedonic response (correct but incomplete)
  → Framework: liking = Evaluative (opioid, conditional, compiled)
                       + Direct-State (non-opioid, hardware, always available)
  → = Liking không chỉ có ĐIỀU KIỆN — còn có LOẠI khác nhau

  → Tại sao framework đi xa hơn:
    - Berridge giải thích "liking xảy ra" (descriptive, Evaluative only)
    - Framework giải thích "liking xảy ra KHI NÀO + TẠI SAO + QUA ĐÂU + LOẠI NÀO"
      (mechanism + architecture)
```

---

## §4 — 5 CASES QUA CẢ HAI LENS

### §4.1 — Case 1: Rat Experiment (Berridge Classic)

```
SETUP:
  Chuột bị block dopamine → cho sugar

BERRIDGE LENS:
  → Wanting blocked (no dopamine = no seeking)
  → Liking preserved (opioid intact = still enjoy sugar khi given)
  → = Evidence tách wanting/liking ✅

FRAMEWORK LENS:
  → Step 2 VTA blocked → no dopamine → no PFC alert (steps 2-4 fail)
  → Step 5 body-base opioid INTACT
  → Sugar vào miệng BYPASS attention gate (direct sensory → body)
  → Body-need (hunger) still pending → sugar fits → opioid fires
  → = SAME explanation, nhưng framework SPECIFY MECHANISM:
    - VTA block = steps 2-4 fail (no seeking pathway)
    - Opioid intact = step 5 still works IF stimulus arrives
    - "Liking preserved" = Body-Feedback-Preconditions still met
      (schema pending ✅, chunks adequate ✅, stimulus direct ✅)

FRAMEWORK THÊM GÌ:
  → Predict: nếu chuột CŨNG block opioid → liking CŨNG mất
  → Predict: nếu chuột NO hunger (schema pending fail) → liking giảm
  → 🟢 Cả hai predictions confirmed (Peciña & Berridge 2005, Cabanac alliesthesia)

  Reward-Signal-Architecture LENS (§3.5):
  → Sugar liking = EVALUATIVE Reward (E₀ hardware-install evaluation)
  → Naltrexone block = blocks Evaluative pathway → liking MẤT
  → NHƯNG: nếu chuột được TOUCH comfort → Direct-State Reward VẪN có
  → = Naltrexone experiment chỉ test EVALUATIVE side
```

### §4.2 — Case 2: Gambling / Slot Machine

```
SETUP:
  Người chơi slot machine → thắng ít, thua nhiều → vẫn tiếp

BERRIDGE LENS:
  → Wanting HIGH (dopamine sensitized to gambling cues — lights, sounds, near-misses)
  → Liking LOW (rare actual win → infrequent opioid)
  → = Wanting-heavy, liking-poor → compulsive loop

FRAMEWORK LENS:
  → VTA fires on random reward schedule (micro-delta mỗi spin):
    - Near-miss = LARGE delta → VTA fire strong → dopamine surge
    - Win = delta → VTA fire → dopamine → PFC attend
    - Routine loss = habituate → VTA mildly fire
  → Step 5 body-base check:
    - Win: body-need "exchange value" temporarily met → OPIOID (rare)
    - Loss: body-need NOT met → no opioid → but next spin = new delta
  → Self-Generated Threat (§2.6 Mechanism 6):
    - "Nếu dừng = mất hết / không gỡ được" → cortisol → PUSH to continue
    - PFC nhìn = "wanting to win". Body = threat avoidance.
  → Anchor-Schema potential:
    - "Sẽ gỡ lại" thành anchor → Trust binding → resist stop

FRAMEWORK THÊM GÌ:
  → Gambling "wanting" = ÍT NHẤT 3 mechanisms khác nhau:
    ② VTA dopamine alert (random schedule sensitization)
    ⑥ Self-generated threat ("thua rồi phải gỡ")
    ④ Anchor-schema binding (nếu compiled)
  → Can thiệp: chỉ block dopamine (CBT "bớt muốn") = THIẾU
  → Cần: address threat (⑥) + decompile anchor (④)
  → = Tại sao gambling therapy phức tạp hơn "bảo người ta bớt muốn"
```

### §4.3 — Case 3: TikTok / Social Media Scroll

```
SETUP:
  Scroll TikTok 2 tiếng → "chán, mệt, trống" → nhưng không dừng được

BERRIDGE LENS:
  → Wanting continuous (dopamine micro-doses per video)
  → Liking absent (no real pleasure — "empty")
  → = Pure wanting without liking → "dopamine trap"

FRAMEWORK LENS:
  → VTA fires on EVERY video (micro-delta — content mới mỗi swipe):
    - Novelty.md v1.2: mỗi post = micro-delta → VTA fire nhẹ
    - DRD4 threshold MET vì content ĐỔI liên tục
  → Step 5 body-base check FAIL LIÊN TỤC:
    - Body-need thật (connection? rest? meaning?) → KHÔNG match với video content
    - Precondition-1 Directed-Gap (schema pending): body MUỐN connection → videos ≠ connection
    - No opioid → no reward thật → "empty feel"
  → Imagine-Final.md v3.0 (sai target — PFC channel wrong body-need):
    - Body signal "thiếu gì đó" → PFC thử scroll → tạm bớt → chán lại
    - PFC fix SAI channel — body cần connection, PFC cho novelty
  → NHƯNG VẪN TIẾP vì:
    - VTA vẫn fire (step 2) → dopamine = "có thể video TIẾP sẽ khác"
    - PFC weakened (mệt) → executive override yếu → cannot stop

FRAMEWORK THÊM GÌ:
  → "Empty scrolling" = VTA active + body-need UNMET + PFC sai target
  → Berridge đúng (wanting without liking) nhưng không explain WHY empty
  → Framework: Precondition-1 Directed-Gap FAIL (wrong schema pending addressed)
  → Giải pháp: không phải "block dopamine" (pop "dopamine detox")
    mà = identify body-need thật (connection? rest?) + provide đúng channel

  Reward-Signal-Architecture LENS (§3.5):
  → TikTok reward (nếu có) = 100% Evaluative, 0% Direct-State
  → Không có touch, không có body movement, không có physical warmth
  → Direct-State pathways HOÀN TOÀN im lặng trong lúc scroll
  → = "Empty" VÌ thiếu Direct-State baseline reward
  → Giải pháp Reward-Signal-Architecture: dừng scroll → đi bộ (Direct-State exercise)
    hoặc ôm người thân (Direct-State touch + Evaluative social)
```

### §4.4 — Case 4: Jensen Huang (30 năm build NVIDIA)

```
SETUP:
  Jensen Huang drive liên tục 30 năm → build NVIDIA thành computing reference

BERRIDGE LENS:
  → Intense wanting (motivation to build, never stop)
  → Liking present but infrequent (major milestones = pleasure)
  → = Strong wanting sustains through low-liking periods

FRAMEWORK LENS:
  → MULTI-MECHANISM BLEND (không chỉ 1 "wanting"):

    ① Imagine-Final Preview (§2.1):
       → Body-need: significance + mastery + legacy (tầng ①)
       → Imagine-Final: "NVIDIA thành reference" (tầng ②)
       → Plan: GPU strategy, partnerships, timing (tầng ③)
       → ⚠️ "GPU sẽ có giá trị" = PARAMETER tầng ③, KHÔNG PHẢI tầng ②
       → Body PRE-FEEL "đạt được vision" → opioid preview → drive

    ③ Compiled Schema Momentum (§2.3):
       → 30 năm compiled → body tự drive AUTO
       → Không cần PFC nhắc → compiled schema chạy "build NVIDIA" mỗi sáng
       → = Deepest, most persistent source of Jensen's drive

    ④ Anchor-Schema Binding (§2.4):
       → "NVIDIA vision" = Anchor-Schema Trust CỰC CAO
       → Cost of stopping = enormous (identity, legacy, commitment)
       → = Wanting TỰ DUY TRÌ qua Trust binding

    ⑥ Self-Generated Threat (§2.6):
       → "Nếu tôi dừng → mất tất cả / phản bội vision"
       → Cortisol push → tiếp tục → output = "driven"

  → LIKING qua chain (§3.3):
    - Major milestone → schema chain complete → opioid
    - VD: GPU revolution thành hiện thực → body-need (significance) MET → opioid STRONG
    - Nhưng: VTA habituate milestone → NEXT milestone cần lớn hơn (treadmill)
    - Daily work: Goldilocks match (enough challenge + enough competence) → micro-opioid

FRAMEWORK THÊM GÌ:
  → Berridge: "Jensen wants intensely." (1 sentence)
  → Framework: Jensen's drive = BLEND 4 mechanisms + liking qua milestone chain
  → Giải thích TẠI SAO 30 năm không dừng: compiled momentum (③) + anchor binding (④) + threat avoidance (⑥)
  → Giải thích TẠI SAO vẫn enjoy: milestone opioid + daily Goldilocks micro-reward
  → = CANNOT reduce to "wanting" — phải phân biệt mechanisms
```

### §4.5 — Case 5: Einstein Eureka + Altruism + Studying Children

```
⭐ 3 SUB-CASES — đều chain-mediated, đều invisible cho PFC:


CASE 5a — EINSTEIN EUREKA:

  BERRIDGE: wanting = motivation to solve physics. Liking = eureka pleasure.

  FRAMEWORK:
    → Wanting = schema dissonance (vật lý có gap CHƯA giải) →
      body-need mastery + curiosity → Imagine-Final "hiểu" → drive
    → Liking = eureka moment:
      - Schema dissonance lớn (Precondition-1 Directed-Gap met ✅)
      - Chunks base adequate — Einstein ĐÃ build 10+ năm (Precondition-2 Chunk-Substrate ✅)
      - Chunk mới fits gap = LARGE delta (Precondition-3 Delta-Gate ✅)
      - Goldilocks: phần lớn framework đã có, chunk mới = key piece (Precondition-4 Match-Range ✅)
      - Chunks opioid-tagged — deep curiosity context (Precondition-5 Compile-Gate ✅)
      → ALL 5 met → OPIOID BURST = Eureka
      → Nếu có threat context (Einstein under stress): cortisol DROP bonus → EXPLOSIVE
      → Nếu no threat (pure curiosity): opioid alone → deep satisfaction

    → ⚠️ Eureka reward = OPIOID, không phải "dopamine spike"
      (Dopamine-Is-Not-Reward.md §3.7 — N+10 correction)


CASE 5b — ALTRUISM ("từ thiện vô tư"):

  BERRIDGE: wanting = motivation to help. Liking = pleasure of helping.

  FRAMEWORK:
    → PFC nói: "giúp người vì tử tế" (confabulation)
    → Compiled patterns fire nhiều chains SONG SONG (Valence-Propagation.md v3.0):
      → mirror Self-Pattern-Modeling → see relief → body mirror → micro-opioid
      → status → "người tốt" identity confirm → status need met → opioid
      → identity → action match tự nhận → coherence → opioid
      → connection → bond with recipient → connection need met → opioid
    → Net: nhiều chains × micro-opioid > cost of helping → body = "feel good"
    → PFC KHÔNG BIẾT chains → label = "vô tư", "vì tình người"
    → = LIKING is REAL (opioid fires) nhưng MECHANISM invisible

    → Berridge: "helping = liking" (accurate but surface)
    → Framework: "helping = multi-chain-mediated opioid bursts" (mechanism visible)


CASE 5c — STUDYING CHILDREN (cùng hành vi, khác liking):

  BERRIDGE: wanting = motivation to study. Liking = pleasure of learning.

  FRAMEWORK — 2 PATHS:

    Path A — Trẻ THÍCH HỌC (curiosity compiled):
      → Body-need: mastery + curiosity (hardware fit)
      → Imagine-Final: "tôi giải được cái khó" → body pre-feel satisfied
      → Giải bài xong → schema match → Goldilocks → opioid
      → = GENUINE liking — all Body-Feedback-Preconditions met

    Path B — Trẻ BỊ ÉP HỌC (safety-driven):
      → Body-need: safety (tránh phạt) + connection (mẹ khen)
      → Imagine-Final: "không bị mắng / được khen"
      → Hoàn thành bài → threat REMOVED → cortisol DROP = RELIEF
      → = KHÔNG phải opioid-liking — là RELIEF (cortisol drop)
      → PFC nhìn = "hoàn thành → feel better" = looks like "liking"
      → Body: KHÁC HOÀN TOÀN — relief ≠ reward

    ⚠️ CÙNG HÀNH VI ("ngồi làm bài") + KHÁC CƠ CHẾ:
      Path A: opioid-driven → sustainable, self-reinforcing
      Path B: relief-driven → dependent on threat → stops when threat removed
      Berridge: cả hai = "liking learning"
      Framework: KHÁC — opioid vs cortisol drop

    Reward-Signal-Architecture LENS (§3.5):
      Path A = EVALUATIVE Reward (E₂ coherence: pattern match → opioid)
      Path B = KHÔNG CÓ reward — chỉ có relief (cortisol drop ≠ opioid)
      Path C (thường bị BỎ QUA): môi trường học thân thiện
        → Cô giáo ấm áp + bạn bè → DIRECT-STATE touch/proximity reward
        → Direct-State component CÓ THỂ support learning environment
        → = Tại sao "cảm giác an toàn trong lớp" quan trọng dù KHÔNG trực tiếp liên quan đến bài
        → = Direct-State reward NÂNG baseline, giúp Evaluative dễ fire hơn
```

---

## §5 — TẠI SAO FRAMEWORK KHÔNG DÙNG WANTING/LIKING

```
🟡 5 LÝ DO FRAMEWORK KHÔNG DÙNG WANTING/LIKING NHƯ THUẬT NGỮ:


LÝ DO 1 — BINARY COLLAPSE QUÁ NHIỀU INFORMATION:

  Wanting = 6 mechanisms gom chung (§2):
    → Imagine-Final preview (PFC simulate)
    → VTA dopamine alert (salience)
    → Compiled schema momentum (vô thức auto)
    → Anchor-schema binding (trust commit)
    → Valence chain propagation (indirect)
    → Self-generated threat (tránh mất)

  "Wanting" nén 6 mechanisms khác nhau thành 1 từ.
  = Mất thông tin VỀ NGUỒN GỐC drive
  = Mất thông tin VỀ CÁCH CAN THIỆP
  = Tương tự gọi "ốm" cho cả cảm lạnh lẫn ung thư — đúng nhưng VÔ ÍCH cho treatment


LÝ DO 2 — LIKING KHÔNG TỰ ĐỘNG — CÓ 5 PRECONDITIONS:

  Berridge: "liking fires khi opioid" (black box condition)
  Framework: "liking fires khi ALL 5 Body-Feedback-Preconditions met"

  Dùng "liking" gom chung = KHÔNG PHÂN BIỆT:
    → Direct liking (sugar) vs chain-mediated (eureka)
    → Opioid reward vs relief (cortisol drop)
    → Compiled-context liking (opioid-tagged) vs threat-compiled (threat-tagged)

  = "Liking" nói "pleasant" nhưng không nói "pleasant KIỂU GÌ + TẠI SAO"


LÝ DO 3 — PFC BLINDNESS KHÔNG THỂ HIỆN QUA WANTING/LIKING:

  Valence-Propagation.md v3.0 — PFC Blindness:
    → PFC chỉ thấy OUTPUT ("muốn cái đó" / "thích cái đó")
    → PFC KHÔNG thấy MECHANISM (chain nào? precondition nào?)
    → PFC CONFABULATE lý do ("vì tôi thích" / "vì tôi muốn")

  Dùng wanting/liking = THEO PFC PERSPECTIVE
  = Mô tả WHAT PFC SEES, không phải WHAT BODY DOES
  = Framework CẦN body-perspective → cần tham số chi tiết hơn


LÝ DO 4 — "LIKING" THIẾU EVALUATIVE/DIRECT-STATE DIMENSION:

  Berridge "liking" = opioid hedonic response (Evaluative Reward)
  NHƯNG: "thích" trong đời thực CÒN có Direct-State Reward:
    → Touch comfort, runner's high, warmth = KHÔNG qua opioid hedonic hotspot
    → Hardware-based, always available, burnout-proof

  Dùng "liking" gom chung = KHÔNG PHÂN BIỆT:
    → Evaluative "thích" (food, music, insight) vs Direct-State "thích" (touch, warmth)
    → Compound "thích" (social touch = Evaluative + Direct-State blend)
    → = Mất thông tin VỀ LOẠI reward + CƠ CHẾ can thiệp
  (Chi tiết: §3.5 + Reward-Signal-Architecture.md v2.0)


LÝ DO 5 — FRAMEWORK ĐÃ CÓ THAM SỐ ĐẦY ĐỦ:

  Thay vì wanting/liking, framework dùng:

  ┌─────────────────────────────────────────────────────────────┐
  │ THAY CHO "WANTING":                                         │
  │                                                              │
  │   → Imagine-Final (preview state + 3-layer + clarity level) │
  │   → prediction-delta detection (habituation-based)          │
  │   → Compiled schema state (auto-drive vs PFC-driven)        │
  │   → Anchor-Schema + Trust level (binding strength)          │
  │   → Valence chain (which chains fire, where they lead)      │
  │   → Threat state (self-generated? external? none?)          │
  │   → Entity-Compiled momentum (per-entity auto-drive)        │
  │                                                              │
  │   = MỖI THAM SỐ ĐỘC LẬP, ĐO ĐƯỢC, CAN THIỆP ĐƯỢC        │
  ├─────────────────────────────────────────────────────────────┤
  │ THAY CHO "LIKING":                                          │
  │                                                              │
  │   → 5 Body-Feedback-Preconditions (which met, which failed)           │
  │   → Body signals (Satisfaction / Reward / Dissonance)       │
  │   → Chain path (direct vs chain-mediated, length)           │
  │   → Chunk tag (opioid vs threat, compile context)           │
  │   → Opioid vs relief (reward vs cortisol drop)             │
  │   → Evaluative vs Direct-State (reward TYPE + pathway)      │
  │   → E₀→E₃ gradient (evaluation complexity depth)           │
  │                                                              │
  │   = MỖI LAYER FALSIFIABLE, PREDICT ĐƯỢC, KHÁC BIỆT ĐƯỢC   │
  └─────────────────────────────────────────────────────────────┘

  → Framework KHÔNG CẦN wanting/liking — đã có tham số chi tiết hơn
  → Dùng wanting/liking = đi lùi về resolution thấp hơn
  → = Nhìn ảnh 4K rồi quay lại 480p — thấy CÙNG THỨ nhưng mất detail


⭐ TỔNG KẾT:

  Wanting/liking = ĐÚNG ở level tách "seeking ≠ pleasure"
  Wanting/liking = THIẾU ở level phân tích mechanism + can thiệp + reward type
  Framework = KHÔNG BÁC BỎ — chỉ ZOOM IN sâu hơn
  File này = BRIDGE giúp reader zoom từ Berridge → framework
```

### §5.1 — × New Concepts (28-session Drill Propagation)

```
BOND-ARCHITECTURE × WANTING (Bond-Architecture.md v2.0):

  6 wanting mechanisms (§2) MAP vào 4 bond types:

  ┌────────────────────────┬────────────────────────────────────┐
  │ WANTING MECHANISM      │ BOND TYPE INTERACTION              │
  ├────────────────────────┼────────────────────────────────────┤
  │ ① Imagine-Final Preview│ All bonds — PFC simulate per-bond │
  │ ② VTA Dopamine Alert   │ All bonds — delta detection       │
  │ ③ Compiled Momentum    │ Proximity + Shared-Experience     │
  │                        │ (auto-drive from compiled routine) │
  │ ④ Anchor-Schema Binding│ Identity bond (strongest anchor)  │
  │ ⑤ Valence Chain        │ Reciprocal bond (chain exchange)  │
  │ ⑥ Self-Generated Threat│ Identity + Proximity (loss fear)  │
  └────────────────────────┴────────────────────────────────────┘

  → Bond type SHAPES which wanting mechanisms DOMINATE:
    Proximity bond → ③ compiled momentum + ⑥ loss fear → stable, conservative
    Reciprocal bond → ⑤ valence chain + ① imagine → active, exchange-driven
    Identity bond → ④ anchor + ⑥ threat → deepest, hardest to change

SATIATION TYPES × LIKING (Gap-Body-Need.md v1.0):

  Liking (§3) = opioid CÓ ĐIỀU KIỆN → satiation matters:
    ENGINE satiation: opioid system mệt → liking GIẢM dù stimulus SAME
      VD: ăn cùng món yêu thích → lần 1 ngon, lần 100 bình thường
    ROAD satiation: cùng path fill → bored → cần path MỚI
      VD: được khen cùng cách → habituate → cần khen KHÁC
    VEHICLE satiation: entity cụ thể bão hòa → cần entity KHÁC
      VD: nghe bài nhạc yêu thích × 50 → chuyển bài
  → Precondition-4 Match-Range (§3.2) = satiation boundary:
    Dưới satiation → liking fire. Trên satiation → "quen rồi" → no fire.

HARDWARE-SUBSIDY × WANTING (Entity-Valence-Dynamics.md v1.0 §5):

  → Hardware-subsidy AMPLIFY wanting SELECTIVELY:
    Mức 5 entity (con): wanting ③ compiled momentum + ⑥ loss fear = MAXIMUM
      → Body cung cấp oxytocin/opioid baseline → wanting "miễn phí"
    Mức 1 entity (stranger): wanting = chỉ ① imagine + ② VTA → must EARN
    → = TẠI SAO wanting toward family ≠ wanting toward stranger
      (CÙNG mechanism, KHÁC hardware-subsidy)

🟡 Bond-Architecture × wanting = framework application (6 mech × 4 bonds)
🟡 Satiation × liking = framework convergence (Precondition-4 Match-Range ↔ satiation)
🟡 Hardware-Subsidy × wanting = framework application (selective amplification)
```

---

## §6 — HONEST ASSESSMENT

### §6.1 — Điều chắc chắn 🟢

```
  → Dopamine ≠ reward (Berridge 1998, decisive, 7 lines of evidence)
  → Wanting ≠ liking (Berridge-Robinson, 3 decades replicated)
  → Opioid system = hedonic response (morphine, Peciña 2005)
  → Addiction = wanting pathological + liking giảm (Robinson-Berridge 2003)
  → Habituation = established neuroscience mechanism
  → CT afferents = gentle touch pathway (🟢 Löken 2009)
  → Endocannabinoid = exercise reward pathway (🟢 Fuss 2015 PNAS)
  → Naltrexone blocks opioid hedonic response (🟢 Blass & Ciaramitaro 1994)
```

### §6.2 — Điều framework claim (testable nhưng chưa test đầy đủ) 🟡

```
  → 5 Body-Feedback-Preconditions: logic consistent, each testable, chưa test đồng thời
  → Habituation vs Prediction Error: cùng observables, chưa decisive test
  → 6 wanting mechanisms: phân biệt từ framework analysis, chưa isolated experimentally
  → Chain-mediated liking: Eureka + altruism = opioid qua chain → logic consistent,
    direct measurement chưa có cho abstract chains
  → Chunk tag direction (cortisol compile gate): framework-specific, evidence indirect
  → Goldilocks zone: inverted-U supported (Berlyne 🟢), no precise % range
  → Evaluative/Direct-State distinction: components individually well-supported (🟢),
    ORTHOGONAL framing + Evaluative Gates Direct-State mechanism = framework synthesis (🟡)
  → E₀→E₃ gradient: each level has evidence, gradient AS spectrum = framework model (🟡)
  → Entity-Compiled momentum as wanting source: framework-specific, indirect evidence
```

### §6.3 — Vị trí bridge file này

```
  FILE NÀY:
    → KHÔNG claim discovery mới
    → KHÔNG rebut Berridge (framework ĐỒNG Ý)
    → MAPPING existing framework concepts sang mainstream terminology
    → + CHỈ RA tại sao framework goes beyond
    → = Giá trị = BRIDGE, không phải contribution khoa học mới

  NẾU BERRIDGE ĐỌC FILE NÀY:
    → Likely agree: wanting/liking = simplified description
    → Likely interested: Body-Feedback-Preconditions = testable answer to his open question
    → Likely ask: "Where's the data for 5 preconditions ALL met → opioid?"
    → Framework answer: "Testable hypothesis. We haven't run the experiment."

  → Framework HONEST: extend Berridge, KHÔNG claim hơn Berridge
  → Framework value: MECHANISM testable, NOT just description
```

---

## §7 — CROSS-REFERENCES + READING GUIDE

### §7.1 — Reading Guide cho reader

```
NẾU BẠN MUỐN HIỂU:

  "Dopamine thực sự là gì?"
    → Dopamine-Is-Not-Reward.md v1.0 (7 bằng chứng + 7-step + framework position)

  "Reward hoạt động thế nào? 5 Body-Feedback-Preconditions?"
    → 03-Reward.md (Body-Feedback/) (7-step detailed + Body-Feedback-Precondition + 7 reward cases)

  "Reward có mấy LOẠI? Evaluative vs Direct-State?"
    → Reward-Signal-Architecture.md v2.0 (Body-Feedback/) (2 loại + E₀→E₃ + 5 Profiles)

  "Imagine-Final là gì? Hardware prediction vs constructive?"
    → Imagine-Final.md v3.0 (PFC/Imagination/) (constructive simulation + lifecycle + 3 chiều)

  "Brain simulate bằng gì? 1 engine cho tất cả?"
    → Simulation-Engine.md v1.0 (PFC/) (3 components + 3 axes + N applications)

  "Anchor-Schema? Trust binding?"
    → Anchor-Schema.md v1.0 (Schema/) (vô thức sync + 4 nguồn + cost)

  "Valence chain propagation? PFC blindness?"
    → Valence-Propagation.md v3.0 (Body-Base/) (per-entity + chain + 3 Firing Modes)

  "Drive tổng thể — nhiều drives → action?"
    → Drive.md v1.2 (Observation/) (integration hub, vô thức engine + PFC navigator)

  "VTA detection mechanism?"
    → Novelty.md v1.2 (Observation/) (VTA seismograph + habituation + DRD4)

  "Feeling — PFC thấy gì khi observe body?"
    → Feeling.md v3.0 (Body-Base/Feeling/) (7-layer fidelity + PFC observation interface)

  "Body feedback — 3 body signals?"
    → Body-Feedback/ folder (01-Foundation + 02-Dissonance + 03-Reward)

  "Entity compile vào body thế nào?"
    → Entity-Compiled.md v1.0 (Agent-Mechanism/) (Hub-and-Spoke + formation + grief)
```

### §7.2 — Cross-References

```
DEPENDENCY FILES (file NÀY phụ thuộc):

  Clarification/:
  [Dopamine-Is-Not-Reward.md v1.0](../Clarification/Dopamine-Is-Not-Reward.md) — 7-step + 7 evidence

  Body-Base/:
  [03-Reward.md](../Body-Base/Body-Feedback/03-Reward.md) — 5 Body-Feedback-Preconditions + reward cases
  [Reward-Signal-Architecture.md v2.0](../Body-Base/Body-Feedback/Reward-Signal-Architecture.md) — Evaluative/Direct-State + E₀→E₃ + 5 Profiles
  [Valence-Propagation.md v3.0](../Body-Base/Valence-Propagation.md) — chain propagation + 3 Firing Modes
  [Anchor-Schema.md v1.0](../Body-Base/Schema/Anchor-Schema.md) — Trust binding + 4 nguồn fill
  [Feeling.md v3.0](../Body-Base/Feeling/Feeling.md) — PFC observation + 7-layer fidelity

  PFC/:
  [Imagine-Final.md v3.0](../PFC/Imagination/Imagine-Final.md) — constructive simulation + 3-Layer + lifecycle
  [Simulation-Engine.md v1.0](../PFC/Simulation-Engine.md) — 1 engine, 3 components, N applications

  Observation/ (cùng folder):
  [Drive.md v1.2](Drive.md) — vô thức ENGINE + PFC NAVIGATOR + integration
  [Novelty.md v1.2](Novelty.md) — VTA seismograph + habituation
  [Threat.md v1.2](Threat.md) — 3 threat types + self-generated threat

  Agent-Mechanism/:
  [Entity-Compiled.md v1.0](../Body-Base/Chunk/Agent-Mechanism/Entity-Compiled.md) — entity compilation + momentum
  [Bond-Architecture.md v2.0](../Body-Base/Chunk/Agent-Mechanism/Bond-Architecture.md) — 4 bond types × wanting
  [Self-Pattern-Modeling.md v3.1](../Body-Base/Chunk/Agent-Mechanism/Self-Pattern-Modeling.md) — mirror + prediction

RESEARCH CITATIONS (primary):
  🟢 Berridge & Robinson 1998, 2003, 2016 — wanting ≠ liking (foundational)
  🟢 Peciña & Berridge 2005 — NAcc hedonic hotspot, opioid vs dopamine dissociation
  🟢 Schultz 1997 — dopamine prediction-delta signal (reinterpreted as salience/delta)
  🟢 Cabanac 1971 — alliesthesia (same food, different pleasure when full vs hungry)
  🟢 Brickman 1978 — hedonic treadmill
  🟢 Berlyne — optimal arousal, inverted-U curve
  🟢 Koob & Volkow 2010 — addiction as allostatic multi-system
  🟢 Löken et al. 2009 — CT afferents, gentle touch pathway
  🟢 Fuss et al. 2015 PNAS — endocannabinoid exercise reward
  🟢 Van der Kolk 2014 — body-oriented approaches for trauma
  🟢 Blass & Ciaramitaro 1994 — naltrexone reduces sucrose calming → opioid
```

---

**Kết luận**: Wanting/liking (Berridge-Robinson) = bước tiến QUAN TRỌNG so với "dopamine = reward". Framework ĐỒNG Ý và EXTENDS: wanting = ít nhất 6 mechanisms khác nhau, liking = Evaluative Reward (opioid, CÓ ĐIỀU KIỆN) + Direct-State Reward (non-opioid, hardware, always available). File này là BRIDGE — giúp reader chuyển từ binary wanting/liking sang kiến trúc framework chi tiết hơn. Framework KHÔNG dùng wanting/liking vì binary collapse quá nhiều information cần cho phân tích + can thiệp + reward type.