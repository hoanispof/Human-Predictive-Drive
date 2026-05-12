---
title: Autonomy-Hardware — Tại Sao Self-Action = Reward
version: 1.0
created: 2026-04-20
status: OBSERVATION PARAMETER v1.0 — HARDWARE MECHANISM
scope: |
  HARDWARE MECHANISM FILE: Giải thích TẠI SAO con người tự nhiên prefer
  self-action hơn external-control. Đây KHÔNG phải "thiết kế" hay "bản năng"
  — mà là EMERGENT PATTERN từ kiến trúc hardware: efference copy + VTA
  prediction-delta + opioid system → tự action = prediction accuracy CAO hơn
  = body reward CAO hơn. Universal — mọi người đều có, cross-species.
  Bổ sung: vmPFC + DRN controllability learning (Maier & Seligman 2016),
  cortisol direction tag (novelty vs threat), opioid vs relief pathways.
purpose: |
  File này giải thích CƠ CHẾ HARDWARE tạo ra autonomy preference.
  Autonomy.md (file đi kèm) giải thích SOFTWARE — chunk tích lũy,
  developmental arc, xu hướng cá nhân.
  Split vì: hardware mechanism = universal, nền tảng.
  Software development = individual, tùy experience.
  Các file khác (Cortisol-Baseline, BFM, Neural-Architecture) CẦN
  reference file này cho efference copy reward + vmPFC/DRN mechanism
  mà backup/Neurochemistry.md §6.3 từng chứa.
position: |
  Core-Deep-Dive/Observation/ — đi kèm Autonomy.md (software/development).
  Hardware mechanism NHƯNG nằm ở Observation/ vì: pattern này QUAN SÁT ĐƯỢC
  từ chính kiến trúc hardware, không phải hardware được thiết kế buộc phải
  như vậy. Giống VTA prediction-delta = emergent từ architecture.
dependencies:
  - Core-v7.8-Draft.md — §8 observation parameters, Autonomy definition
  - Cortisol-Baseline.md v2.0 — §7.2-§7.3 chunk direction tag
  - backup/Neurochemistry.md — §6.3 controllability, vmPFC + DRN
  - Neural-Architecture.md — vmPFC sub-region, amygdala pathway
  - Neural-Processing-Flow.md — §8.2 Feeling circuit (Insula + ACC + vmPFC)
  - Body-Feedback-Mechanism.md — Chunk-Shift/Miss/Gap, prediction-delta
  - Imagine-Final.md — §1 student bị ép vs thích (line 174-179)
  - Liking-Wanting.md — §4 Path A (opioid) vs Path B (relief)
  - Domain-Mapping-Drive.md — Student A vs B, threat vs novelty path
  - Reward-Economics.md — §9 controllability, Deci 1971 overjustification
companion_file: Autonomy.md (software/development — chunk accumulation, developmental arc)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Autonomy-Hardware — Tại Sao Self-Action = Reward

> Bạn tự đưa ly nước lên miệng. Tay feel nhiệt độ, weight, trajectory.
> Não predict: "nước ~25°C sẽ chạm môi ở angle X trong 0.3 giây."
> Miệng nhận → MATCH → body: "đúng rồi" → micro-opioid.
>
> Người khác đưa ly nước vào miệng bạn. Bạn KHÔNG cầm ly.
> Não KHÔNG có efference copy. Tay KHÔNG feel preview.
> Miệng nhận nước → "unpredicted timing, unpredicted temperature"
> → body: alerting signal, KHÔNG phải reward.
>
> CÙNG nước. CÙNG ly. CÙNG lượng. KHÁC prediction accuracy.
>
> Đây KHÔNG phải "preference." Đây là ARCHITECTURE.
> Efference copy + sensory preview + VTA prediction-delta = hardware.
> Self-action = better prediction = more reward.
> External-action = no efference copy = no preview = less reward.
>
> Không ai "thiết kế" body thích self-action.
> Kiến trúc tự PRODUCE pattern đó — emergent, giống VTA
> tự produce dopamine signal khi outcome > prediction.
>
> File này: TẠI SAO hardware produce pattern đó (mechanism),
> VÀ tại sao bị ép = damage ở hardware level (cortisol direction tag).
> Autonomy.md (file đi kèm): HOW pattern đó develop per person (chunks).

---

## Mục lục

- §0 — EMERGENT TỪ ARCHITECTURE, KHÔNG PHẢI THIẾT KẾ
- §1 — EFFERENCE COPY → SELF-PREDICTION ACCURACY
  - §1.1 — Mechanism: Motor Command → Sensory Prediction
  - §1.2 — Multi-Channel Preview: Tay → Não → Miệng
  - §1.3 — Compare Table: Self vs External
  - §1.4 — Prediction Accuracy = Measurable, NOT Abstract
- §2 — vmPFC + DRN: CONTROLLABILITY LEARNING
  - §2.1 — Maier & Seligman 2016: Bất Lực = MẶC ĐỊNH
  - §2.2 — vmPFC Learn "Kiểm Soát Được" → Suppress DRN
  - §2.3 — Cortisol Mãn Tính → vmPFC Teo → Helplessness
- §3 — CORTISOL DIRECTION TAG: CÙNG LEVEL, KHÁC TAG
  - §3.1 — Novelty Direction vs Threat Direction
  - §3.2 — Compile-Time Lock: Tag KHÔNG Đổi Sau Compile
  - §3.3 — "Giỏi Nhưng Ghét" = Threat-Compiled Chunks
- §4 — OPIOID vs RELIEF: 2 PATHWAYS, 2 KẾT QUẢ
  - §4.1 — Path A (Self-Chosen): Opioid → Sustainable
  - §4.2 — Path B (Bị Ép): Relief → Dependent
  - §4.3 — Deci 1971: External Override Internal
- §5 — BỊ ÉP = PREDICTION OVERRIDE → 2-LAYER DISSONANCE
- §6 — HONEST ASSESSMENT
  - §6.1 — Tier 1: Research-Backed (🟢)
  - §6.2 — Tier 2: Framework Synthesis (🟡)
  - §6.3 — Tier 3: Hypothesis (🔴)
  - §6.4 — Open Questions
- §7 — CROSS-REFERENCES

---

## §0 — EMERGENT TỪ ARCHITECTURE, KHÔNG PHẢI THIẾT KẾ

```
⭐ HARDWARE MECHANISM — UNIVERSAL:

  TẠI SAO CON NGƯỜI THÍCH TỰ LÀM:

    Không ai "dạy" bé thích tự xúc ăn.
    Không ai "thiết kế" body cho reward khi self-action.
    Pattern này EMERGENT từ 3 components hardware ĐÃ CÓ SẴN:

    ① EFFERENCE COPY (🟢 von Holst & Mittelstaedt 1950):
      → Motor cortex gửi command → ĐỒNG THỜI gửi COPY tới sensory cortex
      → Sensory cortex dùng copy để PREDICT sensory input sắp tới
      → = Chỉ khi TỰ ACTION mới có efference copy
      → = Khi NGƯỜI KHÁC action → KHÔNG có copy → KHÔNG có prediction

    ② VTA PREDICTION DELTA (🟢 Schultz 1997):
      → Outcome MATCH prediction → neutral-to-positive signal
      → Outcome MISS prediction → negative signal
      → = Self-action có efference copy → prediction tốt hơn → match nhiều hơn
      → = External-action không có copy → prediction kém → miss nhiều hơn

    ③ OPIOID SYSTEM (🟢 Berridge 2003):
      → Prediction match → micro-opioid release
      → = "Đúng rồi" signal → hedonic micro-reward
      → = Tích lũy qua hàng trăm lần → body PREFER self-action

    → 3 components ĐỘC LẬP — không ai thiết kế chúng "cho autonomy"
    → Efference copy evolved cho MOTOR CONTROL (tránh tự cù, etc.)
    → VTA evolved cho LEARNING (reward prediction)
    → Opioid evolved cho HEDONIC VALUATION
    → NHƯNG khi hoạt động CÙNG LÚC → emergent pattern:
      "self-action = better prediction = more reward"
    → = AUTONOMY PREFERENCE = BYPRODUCT of architecture
    → = Giống: nobody designed VTA "cho novelty" — VTA fires on prediction
      delta, novelty HAPPENS to produce large delta → novelty preference emerges

  SO SÁNH VỚI CÁC EMERGENT PATTERNS KHÁC:

    ┌──────────────────────┬──────────────────────────────────────┐
    │ EMERGENT PATTERN     │ HARDWARE COMPONENTS                  │
    ├──────────────────────┼──────────────────────────────────────┤
    │ Novelty preference   │ VTA prediction-delta + dopamine      │
    │                      │ = Large delta → large signal → seek  │
    ├──────────────────────┼──────────────────────────────────────┤
    │ Loss aversion        │ VTA asymmetry (loss > gain signal)   │
    │ (Protect)            │ = Negative delta > positive delta    │
    ├──────────────────────┼──────────────────────────────────────┤
    │ ⭐ AUTONOMY PREF.    │ Efference copy + VTA + opioid        │
    │                      │ = Self-action → copy → better        │
    │                      │   prediction → more match → reward   │
    ├──────────────────────┼──────────────────────────────────────┤
    │ Boredom              │ VTA habituate (delta → 0 over time)  │
    │                      │ + gap detection → dissonance signal  │
    └──────────────────────┴──────────────────────────────────────┘

    → Tất cả = EMERGENT, không phải "designed for"
    → Tất cả = observable FROM architecture, UNIVERSAL
    → Tất cả = có giá trị khoa học vì TESTABLE + FALSIFIABLE

  ⚠️ DISTINCTION QUAN TRỌNG:

    HARDWARE (file này): "TẠI SAO self-action = reward"
      → Universal — mọi người, mọi culture, cross-species
      → Không cần "học" — architecture tự produce
      → Efference copy có từ birth (dù motor chưa precise)

    SOFTWARE (Autonomy.md): "AI sẽ có XU HƯỚNG autonomy CAO/THẤP"
      → Individual — khác mỗi người tùy experience
      → CẦN "build" — motor chunks, controllability chunks, meta-chunk
      → Tùy môi trường (bố mẹ, school, culture)

    → Hardware cho sẵn REWARD cho self-action
    → Software quyết định AI DÙNG ĐƯỢC cái reward đó không
    → Bé bị ép mãn tính: hardware VẪN cho reward cho self-action
      NHƯNG software đã compile "tự làm = bị phạt" → SUPPRESS reward path
    → = Hardware đúng, software override → "biết nên tự làm nhưng không dám"
```

---

## §1 — EFFERENCE COPY → SELF-PREDICTION ACCURACY

### §1.1 — Mechanism: Motor Command → Sensory Prediction

```
🟢 RESEARCH (von Holst & Mittelstaedt 1950, established neuroscience):

  EFFERENCE COPY — CƠ CHẾ CƠ BẢN:

    Khi BẠN thực hiện action:
      ① Motor cortex generate COMMAND → gửi tới muscles
      ② ĐỒNG THỜI: motor cortex gửi COPY (efference copy)
         → tới sensory cortex
      ③ Sensory cortex dùng copy → PREDICT sensory input sắp tới
         → "expect cảm giác X ở thời điểm Y với cường độ Z"
      ④ Sensory input arrives → COMPARE với prediction
      ⑤ Match → neutral-to-positive signal
         Mismatch → alerting/error signal

    Khi NGƯỜI KHÁC thực hiện action lên bạn:
      ① KHÔNG có motor command từ bạn
      ② KHÔNG có efference copy
      ③ Sensory cortex KHÔNG có prediction template
      ④ Sensory input arrives → "UNPREDICTED"
      ⑤ Alerting signal (dù input positive)

  🟢 CLASSIC EVIDENCE:

    TỰ CÙ (🟢 Blakemore et al. 1998):
      → Bạn tự cù → efference copy PREDICT cảm giác
      → Prediction MATCH → signal CANCELLED → không buồn cười
      → Người khác cù → NO efference copy → UNPREDICTED → buồn cười
      → = Efference copy CANCELS self-generated sensory input
      → = CÙNG input, KHÁC prediction → KHÁC body response

    VÍ DỤ MỞ RỘNG:
      → Tự gãi đầu: efference copy predict → match → neutral
      → Người khác gãi đầu: no copy → unpredicted → startle/alerting
      → = Hardware PHÂN BIỆT self-action vs external-action
        ở SENSORY LEVEL, TRƯỚC conscious processing

  ⭐ FRAMEWORK APPLICATION:

    Efference copy = lý do PHYSICAL tại sao self-action
    cho prediction accuracy CAO hơn external-action.

    KHÔNG phải "psychology" hay "preference" — là NEUROSCIENCE ARCHITECTURE.
    Body PHÂN BIỆT self vs external ở millisecond level.
    Và prediction match = opioid micro-reward (§0 ③).
    → = Self-action INHERENTLY more rewarding ở hardware level.
```

### §1.2 — Multi-Channel Preview: Tay → Não → Miệng

```
🟡 FRAMEWORK SYNTHESIS (🟢 efference copy + 🟢 multi-sensory integration):

  TỰ XÚC ĂN — MULTI-CHANNEL PREDICTION CASCADE:

    1. Motor cortex: "đưa muỗng lên miệng" (command)
    2. Efference copy → somatosensory cortex:
       "expect muỗng chạm môi ở angle X, pressure Y, timing Z"
    3. Tay cầm muỗng → touch receptors FIRE:
       → Thermal: "food ~35°C" (preview cho miệng)
       → Texture: "mềm, trơn" (preview cho lưỡi)
       → Weight: "~5ml" (preview cho lượng)
    4. Brain UPDATE prediction cho mouth:
       "food ~35°C, mềm, lượng ~5ml, sắp tới trong 0.5 giây"
    5. Miệng nhận → compare với ENRICHED prediction → MATCH
    6. VTA: match → neutral-positive delta
    7. Opioid: match → micro-reward

  MẸ XÚC — PREDICTION POOR:

    1. KHÔNG có motor command từ bé → KHÔNG có efference copy
    2. Sensory cortex KHÔNG có prediction template
    3. Bé's hand KHÔNG cầm muỗng:
       → KHÔNG có thermal preview
       → KHÔNG có texture preview
       → KHÔNG có weight preview
    4. Brain: NO enriched prediction available
    5. Miệng nhận input → "unpredicted timing, temperature, quantity"
    6. VTA: unpredicted (dù positive) → alerting signal, NOT reward
    7. = Mild dissonance, not catastrophic but CONSISTENT

  TỰ MẶC ÁO — CÙNG MECHANISM:

    Bé tự mặc:
      → Efference copy predict mọi contact point
      → Tay feel vải → preview cho body surface
      → Bé adjust speed, pressure theo body signal real-time
      → = PREDICTION MATCH ở hầu hết contact points

    Mẹ mặc cho:
      → Vải cọ xát theo trajectory CỦA MẸ → bé KHÔNG predict
      → Pressure points ở chỗ mẹ tay đặt → KHÔNG match bé's comfort
      → Speed: mẹ mặc nhanh → bé body chưa kịp adapt
      → = PREDICTION MISS ở nhiều contact points

    → CHẬM nhưng THOẢI MÁI (tự mặc) > nhanh nhưng PREDICTION MISS (mẹ mặc)
    → = Cost (chậm) < benefit (prediction match) khi motor chunks ĐỦ
```

### §1.3 — Compare Table: Self vs External

```
⭐ SUMMARY TABLE:

  ┌─────────────────┬──────────────────────┬──────────────────────┐
  │ PARAMETER        │ SELF-ACTION          │ EXTERNAL-ACTION      │
  ├─────────────────┼──────────────────────┼──────────────────────┤
  │ Efference copy  │ ✅ CÓ               │ ❌ KHÔNG             │
  │ Timing predict  │ HIGH (tự quyết)      │ LOW (người khác)     │
  │ Spatial predict │ HIGH (motor command) │ LOW (unpredicted)    │
  │ Thermal preview │ YES (hand feel)      │ NO (no hand contact) │
  │ Texture preview │ YES                  │ NO                   │
  │ Olfactory prev. │ CLOSER (self-pace)   │ PARTIAL              │
  │ Overall pred.   │ HIGH                 │ LOW                  │
  │ VTA signal      │ Match → positive     │ Miss → alerting      │
  │ Opioid          │ Micro-reward         │ Absent               │
  │ Body feedback   │ REWARD               │ MILD DISSONANCE      │
  └─────────────────┴──────────────────────┴──────────────────────┘

  → CÙNG action. CÙNG object. CÙNG outcome.
  → KHÁC: ai control → KHÁC prediction accuracy → KHÁC body feedback.
  → = HARDWARE ARCHITECTURE tự produce distinction này.
  → = Mọi người đều có. Mọi tuổi. Cross-species.
```

### §1.4 — Prediction Accuracy = Measurable, NOT Abstract

```
⭐ FALSIFIABILITY:

  "AGENCY FEELING" (mainstream):
    → "Cảm giác tôi có quyền quyết định"
    → ĐO BẰNG GÌ? → self-report questionnaire
    → BÁC BỎ THẾ NÀO? → unfalsifiable
    → = PFC LABEL cho body state — hữu ích cho giao tiếp, KHÔNG giải thích cơ chế

  "SELF-PREDICTION ACCURACY" (framework):
    → Self-action → sensory outcome MATCH/MISMATCH prediction
    → ĐO BẰNG GÌ:
      ① Efference copy match ratio (neural imaging, 🟢 technology exists)
      ② Sensory prediction-delta (VTA dopamine, 🟢 Schultz 1997)
      ③ Opioid release on match (🟢 PET scan measurable)
      ④ Behavioral proxy: preference test (choose self vs external)
    → BÁC BỎ THẾ NÀO:
      → Nếu self-action KHÔNG produce higher prediction accuracy
        → efference copy mechanism bị bác bỏ (unlikely — well-established)
      → Nếu higher prediction accuracy KHÔNG produce more reward
        → VTA/opioid link bị bác bỏ (unlikely — Schultz + Berridge)
    → = CLEAR testable chain → giá trị khoa học CAO

  FRAMEWORK POSITION:
    → "Agency feeling" = PFC label cho body state
    → Body state = prediction accuracy pattern (measurable)
    → Giống: "đau" = PFC label cho nociceptor signal
    → "Đau" hữu ích giao tiếp. "Nociceptor signal" giải thích cơ chế.
    → "Agency feeling" hữu ích giao tiếp. "Prediction accuracy" giải thích cơ chế.
```

---

## §2 — vmPFC + DRN: CONTROLLABILITY LEARNING

### §2.1 — Maier & Seligman 2016: Bất Lực = MẶC ĐỊNH

```
🟢 RESEARCH — REVERSED ORIGINAL THEORY:

  ORIGINAL (Seligman 1967):
    → Trạng thái bình thường = ACTIVE
    → Uncontrollable events → LEARN helplessness
    → = "Learned helplessness" = brain LEARNS to be passive

  REVERSED (Maier & Seligman 2016):
    → Trạng thái bình thường = PASSIVE (bất lực)
    → Brain phải HỌC rằng tình huống controllable
    → = "Learned controllability" mới là cái phải học
    → = Passive response = DEFAULT (brainstem DRN)
    → = Active response = LEARNED (vmPFC inhibit DRN)

  🟢 CƠ CHẾ NEURAL (Maier & Seligman 2016; Maier & Watkins 2010):

    DRN (Dorsal Raphe Nucleus — thân não):
      → Fire khi aversive event → passive response DEFAULT
      → = Serotonin release → passive coping (freeze, give up)
      → = KHÔNG phải "depression serotonin" — là passive default

    vmPFC (ventromedial Prefrontal Cortex):
      → CÓ THỂ learn "tình huống này controllable"
      → Controllable DETECTED → vmPFC INHIBIT DRN
      → DRN suppressed → passive response BLOCKED → active coping possible
      → = vmPFC = GATE cho active behavior

    EVIDENCE:
      → vmPFC lesion → animals CANNOT learn controllability
        → Behave helpless EVEN when situation IS controllable
      → vmPFC intact + repeated controllable experience → robust controllability

  ⭐ FRAMEWORK TRANSLATION:

    DRN default = body assumes "actions don't matter"
    vmPFC learn = body learns "my actions → outcomes"
    vmPFC training = ACCUMULATED EXPERIENCE of controllable situations

    → = Hardware CHO PHÉP learn controllability
    → = Nhưng PHẢI ĐƯỢC TRAIN qua experience
    → = Nếu không train (helicopter parenting) → DRN default GIỮ NGUYÊN
    → = Nếu train nhiều (cho tự thử) → vmPFC robust → active coping

  ⚠️ CONTENT NÀY TRƯỚC ĐÂY Ở backup/Neurochemistry.md §6.3:
    → "Controllability = biến quan trọng nhất"
    → "Action Clarity ≈ controllability + available action path"
    → Các file thay thế (Neural-Architecture, Neural-Processing-Flow)
      KHÔNG cover vmPFC/DRN controllability detail
    → File này = primary reference cho mechanism này
```

### §2.2 — vmPFC Learn "Kiểm Soát Được" → Suppress DRN

```
🟡 FRAMEWORK SYNTHESIS (🟢 mechanism, 🟡 chunk framing):

  vmPFC LEARNING PROCESS:

    Step 1: Aversive event → DRN fires (DEFAULT passive)
    Step 2: Subject takes action + outcome CHANGES
      → vmPFC detect: "action → outcome changed" = controllability signal
    Step 3: Repeated controllable experiences
      → vmPFC strengthen: "tình huống LOẠI NÀY = controllable"
    Step 4: Next similar event
      → DRN fires (DEFAULT) → vmPFC: "controllable!" → INHIBIT DRN
      → Passive response BLOCKED → active coping ENABLED

  ⭐ DOMAIN-SPECIFIC (framework addition):

    vmPFC KHÔNG learn "mọi thứ controllable" — learn PER DOMAIN:
      → Tự xúc ăn thành công × 50 → "ăn = controllable"
      → Tự mặc áo thành công × 30 → "mặc = controllable"
      → Chưa resolve conflict → "conflict = ?"
      → = DOMAIN-SPECIFIC controllability

    → CEO confident (business: thousands of experiences)
      nhưng helpless trong relationship (never trained)
    → Student giỏi toán (novelty path) nhưng social anxiety (no training)
    → = Autonomy ≠ global trait — collection of domain-specific states
    → = KHÔNG phải "personality" — là chunk gap
```

### §2.3 — Cortisol Mãn Tính → vmPFC Teo → Helplessness

```
🟢 RESEARCH (McEwen 2007, Maier & Seligman 2016):

  CHRONIC CORTISOL → vmPFC STRUCTURAL DAMAGE:

    → Chronic cortisol → dendritic retraction in vmPFC
      (🟢 McEwen 2007: glucocorticoid-mediated dendritic remodeling)
    → vmPFC neurons SHRINK → fewer connections → WEAKER DRN inhibition
    → = vmPFC TEO VẬT LÝ → lost controllability learning
    → = DRN REGAIN DOMINANCE → passive default RETURNS

    Consequence:
      → Person who HAD controllability → LOSES it after chronic stress
      → "Bất lực TỔNG QUÁT HÓA sang cả tình huống kiểm soát được"
      → = Biological basis for "không thể bắt đầu dù biết nên làm"
      → = KHÔNG phải "lười" — vmPFC cấu trúc đã damaged

  2 PATHWAYS TỚI HELPLESSNESS:

    Pathway 1 — OVER-CONTROL (no training):
      → Parent làm MỌI THỨ cho trẻ → no controllable experience
      → vmPFC KHÔNG được train → DRN default stays
      → 🟢 LeMoyne & Buchanan 2011: helicopter → helplessness

    Pathway 2 — CHRONIC THREAT (damage):
      → Parent imposed threats → chronic cortisol
      → vmPFC developing UNDER cortisol → structural damage
      → Controllability chunks KHÔNG compile (or weak)
      → = ≠ "thiếu ý chí" — vmPFC developmental deficit

    CẢ 2 → cùng kết quả: helplessness
    = Body-Base-Example.md: "parent's over-feeding of caring channel
      = child's starving of autonomy channel"

  RECOVERY:
    → vmPFC CÓ THỂ recover (🟢 neuroplasticity)
    → NHƯNG slower than damage
    → Requires: CONTROLLED exposure to controllable situations
    → = CBT graded exposure = REBUILD vmPFC controllability
    → = Therapy ≠ "talk about feelings" — là RE-TRAIN vmPFC
    → Timeline: tháng-năm
```

---

## §3 — CORTISOL DIRECTION TAG: CÙNG LEVEL, KHÁC TAG

### §3.1 — Novelty Direction vs Threat Direction

```
🟢/🟡 (research: cortisol mechanisms 🟢, direction framing 🟡):

  CÙNG CORTISOL LEVEL, KHÁC DIRECTION (Cortisol-Baseline §7.2-§7.3):

    ┌─────────────────┬──────────────────────┬──────────────────────┐
    │                 │ NOVELTY DIRECTION    │ THREAT DIRECTION     │
    │                 │ (tự chọn, tò mò)    │ (bị ép, sợ)         │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Cortisol level  │ Moderate             │ Moderate-Cao         │
    │ Kèm theo        │ + Dopamine (seeking) │ + NE (alert)         │
    │                 │ + Opioid nhẹ (prev.) │ + Adrenaline         │
    │ Body state      │ HƯNG PHẤN            │ CĂNG                 │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Chunk tag       │ APPROACH (opioid)    │ AVOIDANCE (threat)   │
    │                 │ "hiểu = sướng"       │ "học = khó chịu"     │
    │ Long-term       │ Body THÍCH dùng lại  │ Body TRÁNH dùng      │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Sleep quality   │ TỐT                  │ CÓ THỂ KÉM          │
    │ Repair quality  │ CAO                  │ THẤP                 │
    │ Net health      │ Repair ≥ Damage      │ Repair < Damage      │
    ├─────────────────┼──────────────────────┼──────────────────────┤
    │ Chunk quality   │ CÓ + DÙNG ĐƯỢC      │ CÓ + KHÓ DÙNG       │
    │                 │ + THÍCH              │ + GẮN SỢ             │
    └─────────────────┴──────────────────────┴──────────────────────┘

  AUTONOMY CONNECTION:
    → Self-chosen action = typically NOVELTY direction
    → Forced action = typically THREAT direction
    → = Autonomy (self) vs Ép (external) → KHÁC cortisol direction
    → = KHÁC chunk tag → KHÁC cả đời

    (Table duplicated from Cortisol-Baseline §7.2 cho self-contained reference)
```

### §3.2 — Compile-Time Lock: Tag KHÔNG Đổi Sau Compile

```
🟡 FRAMEWORK:

  CHUNKS COMPILE AT MOMENT cortisol fires (Cortisol-Baseline §7.3):
    → Body state direction tại moment đó = LOCK IN vào chunk
    → = COMPILE-TIME variable

  Student A (tự chọn, interest):
    → Cortisol moderate + dopamine + opioid preview
    → Body state = NOVELTY direction
    → Math chunks compile với APPROACH TAG (opioid present at compile)
    → Adult: "tôi yêu toán, dùng thoải mái"

  Student B (bị ép, threat):
    → Cortisol moderate (SAME LEVEL) + NE + adrenaline
    → Body state = THREAT direction
    → Math chunks compile với AVOIDANCE TAG (threat direction at compile time)
    → Adult: "tôi giỏi toán nhưng GHÉT mở sách toán"

  → CÙNG content learned. CÙNG cortisol level.
  → KHÁC direction → KHÁC tag → KHÁC 20 năm sau.
```

### §3.3 — "Giỏi Nhưng Ghét" = Threat-Compiled Chunks

```
🟡 FRAMEWORK (Domain-Mapping-Drive.md §7.1):

  ┌────────────────────┬──────────────────┬──────────────────┐
  │                    │ STUDENT A (self) │ STUDENT B (ép)   │
  ├────────────────────┼──────────────────┼──────────────────┤
  │ Short term (6 mo)  │ Slower start     │ Faster (forced)  │
  │ Chunk quantity     │ Fewer initially  │ More initially   │
  │ Chunk quality      │ Approach-tagged   │ Avoidance-tagged │
  │ Long term (10 yr)  │ Continue growing │ Decay + avoidance│
  │ Net result         │ DEEP + ENJOYED   │ BROAD but AVOIDED│
  └────────────────────┴──────────────────┴──────────────────┘

  Decision-makers (bố mẹ, school) thấy 6-month results:
    → Student B = "tốt hơn" → push system toward threat path
  Decision-makers KHÔNG thấy 10-year results:
    → Student A = MUCH better
  → = Short-term visible bias (Domain-Mapping-Drive.md line 2991-2993)

  "Giỏi nhưng ghét" = VERY COMMON phenomenon:
    → Chunks CÓ (giỏi) nhưng avoidance-tagged (ghét)
    → Body TRÁNH dùng → career trong lĩnh vực đó = BURNOUT risk
    → = Threat-compiled mastery = fragile achievement
```

---

## §4 — OPIOID vs RELIEF: 2 PATHWAYS, 2 KẾT QUẢ

### §4.1 — Path A (Self-Chosen): Opioid → Sustainable

```
🟡 FRAMEWORK (🟢 Berridge opioid/dopamine):

  PATH A — TỰ CHỌN:

    ① Body-need active (curiosity, interest)
    ② PFC: Imagine-Final = "tôi muốn HIỂU / LÀM / GIẢI"
    ③ Self-initiated action → efference copy → prediction
    ④ Outcome MATCH → VTA: positive prediction-delta
    ⑤ Opioid: match → "đúng rồi" → hedonic reward
    ⑥ Chunk compile với APPROACH TAG → "hiểu = sướng"
    ⑦ Next encounter: body THÍCH dùng chunk → approach → repeat

    = Self-reinforcing, self-sustaining, compound, resilient
```

### §4.2 — Path B (Bị Ép): Relief → Dependent

```
🟡 FRAMEWORK (Liking-Wanting.md §4):

  PATH B — BỊ ÉP:

    ① External threat (punishment, shame)
    ② Body-need: SAFETY (tránh phạt), NOT curiosity
    ③ Imagine-Final: "không bị mắng" (Imagine-Final.md line 178)
    ④ Action = compliance (external-directed)
    ⑤ Threat REMOVED → cortisol DROP → RELIEF
    ⑥ Chunk compile với AVOIDANCE TAG → "học = khó chịu, xong = nhẹ nhõm"
    ⑦ Next encounter: body TRÁNH → cần external threat

    = Dependent, decay without threat, shallow, fragile

  ⚠️ CÙNG HÀNH VI, KHÁC CƠ CHẾ:
    Path A student: ngồi làm bài → opioid → sustainable
    Path B student: ngồi làm bài → relief → stops without threat
    Observer: "cả hai chăm chỉ" → KHÔNG PHÂN BIỆT từ hành vi
    Body: HOÀN TOÀN KHÁC

    → = Tại sao 2 students cùng điểm NHƯNG:
      A ra đời → tiếp tục grow
      B ra đời → DỪNG → "ghét lĩnh vực đã giỏi"
```

### §4.3 — Deci 1971: External Override Internal

```
🟢 RESEARCH (Deci 1971, Reward-Economics.md §9):

  OVERJUSTIFICATION EFFECT:

    🟢 Deci (1971):
      → Group A: play puzzle (intrinsic)
      → Group B: play puzzle + paid
      → Phase 2: no payment → Group B STOPPED. Group A continued.
      → = External reward REPLACED internal reward

  FRAMEWORK TRANSLATION:

    Group A: Imagine-Final = "understand" → self-prediction → opioid → sustainable
    Group B: Imagine-Final SHIFTS to "get paid" → external prediction
      → Remove payment → prediction MISS → WORSE than never paid
      → Old Imagine-Final ("understand") DELINKED → VERY HARD to recover

  IMPLICATION:
    External rewards (kẹo, tiền, khen) CÓ THỂ DAMAGE autonomy:
      → "Thưởng QUÁ MẠNH/LÂU = override internal prediction"
      → Reward-Economics.md §9: external reward = scaffolding → THÁO khi xong
      → Giữ quá lâu → autonomy LOST
```

---

## §5 — BỊ ÉP = PREDICTION OVERRIDE → 2-LAYER DISSONANCE

```
🟡 FRAMEWORK:

  "BỊ ÉP" = PREDICTION OVERRIDE CÓ 2 LAYERS:

  Layer 1 — Prediction override (immediate, BFM §3.2):
    → Current prediction stream bị interrupt
    → Bé đang chơi đồ chơi → mẹ đút food → INTERRUPT
    → Body: "prediction cho đồ chơi → đột nhiên food = OVERRIDE"
    → = Giống bất kỳ prediction miss nào

  Layer 2 — Controllability dissonance (meta, vmPFC):
    → "Prediction CỦA TÔI = irrelevant vì NGƯỜI KHÁC quyết"
    → vmPFC: "tình huống này KHÔNG controllable"
    → DRN: passive coping response
    → = META-LEARNING: "prediction của tôi không matter ở đây"
    → 🟢 Maier & Seligman 2016: uncontrollable → DRN default → passive

  ⚠️ "BỊ ÉP + KẾT QUẢ TỐT" VẪN = DISSONANCE:

    Mẹ ép học toán → bé giỏi toán → kết quả TỐT
    NHƯNG:
      → Prediction CỦA BÉ bị override → chunks compile AVOIDANCE TAG
      → = "Giỏi toán nhưng GHÉT toán"
      → = Outcome quality ≠ autonomy satisfaction

    Sếp ép cách mới → kết quả tốt hơn
    NHƯNG:
      → Nhân viên's prediction bị override → VẪN dissonance
      → = "Đúng nhưng tôi KHÔNG quyết" = low autonomy DÙ outcome good
```

---

## §6 — HONEST ASSESSMENT

### §6.1 — Tier 1: Research-Backed (🟢)

```
🟢 STRONG SUPPORT:

  ① Efference copy mechanism
    → von Holst & Mittelstaedt (1950): motor copy → sensory prediction
    → Blakemore et al. (1998): self-tickle cancellation
    → Well-established, foundation of motor neuroscience

  ② VTA prediction-delta
    → Schultz (1997): outcome vs prediction → dopamine signal
    → Foundation of reinforcement learning neuroscience

  ③ vmPFC + DRN controllability
    → Maier & Seligman (2016): reversed theory, well-replicated
    → Maier & Watkins (2010): vmPFC inhibit DRN mechanism
    → McEwen (2007): chronic cortisol → vmPFC dendritic retraction

  ④ Overjustification
    → Deci (1971): well-replicated across decades
    → SDT (Deci & Ryan 1985, 2000): autonomy + competence + relatedness

  ⑤ Opioid system
    → Berridge (2003): opioid vs dopamine hedonic distinction
```

### §6.2 — Tier 2: Framework Synthesis (🟡)

```
🟡 PLAUSIBLE — combine established, chưa direct test:

  ① "Self-action = higher prediction accuracy than external-action"
    → Logical from efference copy + multi-channel preview
    → Chưa direct experiment comparing prediction-delta self vs other-fed
    → TESTABLE: compare sensory prediction-delta

  ② Cortisol direction tag = COMPILE-TIME lock
    → Consistent with cortisol + opioid literature
    → "Tag as permanent" chưa rõ = permanent or gradual?
    → Therapy suggests retag possible but hard

  ③ Emergent pattern framing
    → "Autonomy preference = byproduct of architecture"
    → Logically sound — but "emergent" is a claim about WHY, hard to test
    → Alternative: could be directly selected (evolution for autonomy)
```

### §6.3 — Tier 3: Hypothesis (🔴)

```
🔴 SPECULATIVE:

  ① Multi-channel preview specifics (hand → temperature → mouth prediction)
    → Nobody measured whether hand temperature preview ACTUALLY
      improves infant mouth prediction accuracy
    → TESTABLE IN PRINCIPLE but not yet tested

  ② "Emergent not designed" claim
    → Framework ASSERTS autonomy preference = byproduct
    → Could be wrong: maybe direct selection pressure FOR autonomy
    → Distinction matters for theory, less for practical application
```

### §6.4 — Open Questions

```
⚠️ 3 OPEN QUESTIONS (hardware-specific):

  Q1: Efference copy DEVELOPMENT — when functional?
    → Present from birth? Or develops with motor cortex?
    → If present from birth → hardware reward for self-action from DAY 1
    → If develops → there's a "before efference copy" period
    → 🟢 Research suggests: basic form present early, refines with development

  Q2: vmPFC critical period?
    → Is there a window for controllability learning?
    → Or lifelong plasticity?
    → 🟢 Neuroplasticity research: lifelong but SLOWER with age
    → Practical: early training = easier, but adult recovery = possible

  Q3: Can approach tag → avoidance tag (and reverse)?
    → Trauma: can approach-tagged chunk be RE-tagged to avoidance?
    → Therapy: can avoidance-tagged be RE-tagged to approach?
    → Partially answered: therapy works slowly → retag possible but hard
    → = Important for intervention design
```

---

## §7 — CROSS-REFERENCES

```
HARDWARE/MECHANISM FILES:
  → Cortisol-Baseline.md §7.2-§7.3 — direction tag, novelty vs threat
  → backup/Neurochemistry.md §6.3 — controllability, vmPFC + DRN (original source)
  → Neural-Architecture.md — vmPFC sub-region, amygdala pathway
  → Neural-Processing-Flow.md §8.2 — Feeling circuit (Insula + ACC + vmPFC)
  → Body-Feedback-Mechanism.md §3 — Chunk-Shift/Miss/Gap, prediction-delta

COMPANION FILE:
  → Autonomy.md — SOFTWARE/DEVELOPMENT: chunk accumulation, developmental arc,
    cross-parameter interactions, healthy vs toxic, counterweights

OBSERVATION FILES (cross-parameter):
  → Liking-Wanting.md §4 — Path A (opioid) vs Path B (relief)
  → Imagine-Final.md §1 — student bị ép vs thích (line 174-179)
  → Domain-Mapping-Drive.md §7.1 — Student A vs B, 10-year divergence
  → Reward-Economics.md §9 — controllability, Deci 1971

RESEARCH CITATIONS:
  🟢 von Holst & Mittelstaedt (1950) — efference copy
  🟢 Blakemore et al. (1998) — self-tickle cancellation
  🟢 Schultz (1997) — VTA prediction-delta
  🟢 Berridge (2003) — opioid vs dopamine
  🟢 Maier & Seligman (2016) — controllability = learned, helplessness = default
  🟢 Maier & Watkins (2010) — vmPFC + DRN mechanism
  🟢 McEwen (2007) — chronic cortisol → dendritic retraction
  🟢 Deci (1971) — overjustification effect
  🟢 Deci & Ryan (1985, 2000) — Self-Determination Theory
  🟢 LeMoyne & Buchanan (2011) — helicopter parenting → helplessness
```

---

## SUMMARY

```
AUTONOMY-HARDWARE = Tại sao self-action = reward (emergent from architecture)

EFFERENCE COPY (§1): Self-action → motor cortex gửi COPY → sensory cortex
  PREDICT input sắp tới → match → micro-opioid. External-action → no copy →
  no prediction → mild dissonance. = Physical mechanism, universal, measurable.

vmPFC + DRN (§2): Bất lực = MẶC ĐỊNH (Maier & Seligman 2016 reversed).
  vmPFC LEARN controllability → inhibit DRN. Chronic cortisol → vmPFC teo →
  helplessness returns. Domain-specific: controllable ở A ≠ controllable ở B.

CORTISOL DIRECTION (§3): Cùng level, KHÁC direction → KHÁC tag.
  Self-chosen = novelty direction = approach tag = body thích dùng.
  Forced = threat direction = avoidance tag = body tránh. Compile-time lock.

2 PATHWAYS (§4): Path A (self) → opioid → sustainable.
  Path B (ép) → relief → dependent on threat. Cùng hành vi, KHÁC cơ chế.
  Overjustification (Deci 1971): external override internal = damage.

BỊ ÉP (§5): 2-layer dissonance — immediate prediction override +
  meta controllability loss. Kết quả tốt VẪN dissonance nếu bị ép.

= Hardware PRODUCE autonomy preference — emergent, not designed.
= Companion file Autonomy.md covers SOFTWARE: how this develops per person.
```
