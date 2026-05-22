---
title: Protect — Observation Parameter
version: 1.1
created: 2026-04-20
updated: 2026-05-17
status: OBSERVATION PARAMETER v1.1
scope: |
  OBSERVATION FILE: Protect = named pattern khi quan sát loss aversion
  + ownership chunk dynamics. Protect không phải component hay operator —
  là TÊN GỌI cho patterns emergent từ compiled ownership chunks
  + asymmetric prediction-delta khi mất.
  File này mô tả: mechanism (ownership chunks + loss aversion),
  formula (replaceability × attachment), spectrum (vật → người → ý tưởng → identity),
  hardware (vasopressin + cortisol threat-pull), chunk dynamics (incl. Gap→Miss),
  endowment effect, protect × giving balance, cross-parameter interactions,
  healthy vs toxic protect, cultural schemas.
purpose: |
  Core v7.8 §8 define Protect ngắn gọn ("Loss aversion + ownership chunk patterns,
  f(perceived replaceability × attachment chunks)").
  File này DEEP-DIVE: tại sao "của tôi" tồn tại ở body-level (compiled chunks),
  tại sao mất đau hơn được (asymmetric delta), hormone nào participate,
  khi nào protect adaptive vs pathological, và tại sao protect có ĐỐI TRỌNG
  tự nhiên (giving dynamic — Agent-Mechanism.md §12.3).
  Dùng cho người cần hiểu chi tiết.
position: |
  Core-Deep-Dive/Observation/ — ngang hàng Novelty.md, Threat.md, Status.md,
  Connection.md, Drive.md, Boredom.md, Empathy.md, Schema.md, Liking-Wanting.md.
  Tất cả = observation parameter deep-dives, KHÔNG phải mechanism files.
sources_backup: |
  Không có file cũ riêng cho Protect — nội dung phân tán trong
  Core drafts + Neurochemistry.md + scattered analysis.
  File mới viết hoàn toàn cho v7.8 observation parameter framework.
  v1.1 KEY CHANGES (2026-05-17):
    ⑪ +Architecture B alignment: protect = emergent observation trong
       general-purpose system, KHÔNG phải hardwired "bản năng bảo vệ" riêng
    ⑫ +Compiled/Fresh: compiled protect (auto, cost ≈ 0) vs fresh protect
       (novel threat → PFC evaluate, costly)
    ⑬ Agent-Mechanism.md → Agent-Mechanism.md (renamed 2026-04-24)
    ⑭ Version refs updated (VP v2.0, Empathy v3.0, Connection v4.0)
    ⑮ +IBM v1.0, +BFL v2.0 cross-refs
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, §8 observation parameters
  - Body-Feedback-Mechanism.md v2.0 — Chunk-Miss/Gap/Shift, §4 Compound, §5 Baseline Shift
  - Chunk.md v2.0 — chunk substrate, compilation, hierarchy
  - Agent-Mechanism.md v2.0 — SPM mechanism, §12 body-need feeder, §12.3 mirror reward override
  - Cortisol-Baseline.md v2.0 — amplifier (NOT cause), inertia, direction gate
  - Clarification/Cortisol-Amplifier-Not-Cause.md — cortisol ≠ stress
  - Clarification/Prediction-Error-Is-Not-Reward.md — PE ≠ reward
  - Threat.md v1.1 — 3 origin sources, loss as threat
  - Connection.md v4.0 — attachment chunks, overlap territory
  - Status.md v2.1 — territorial maps, Schema Access Map
  - Empathy.md v3.0 — SPM function, §7 sharing dynamics, compassion fatigue
  - Inter-Body-Mechanism.md v1.0 — Architecture B §1.2, Compiled/Fresh §3
  - Body-Feedback-Label.md v2.0 — vocabulary consistency
  - backup/Neurochemistry.md — §8 Vasopressin detail
---

# Protect — Observation Parameter

> Laptop tôi hỏng + đủ tiền mua mới → "thôi kệ."
> Laptop tôi hỏng + không đủ tiền → ghét bạn làm hỏng.
>
> Cùng một cái laptop. Cùng một người bạn. Cùng một sự kiện "hỏng."
> Khác: TÔI CÓ THỂ THAY THẾ ĐƯỢC KHÔNG?
>
> "Protect" không phải bản năng bảo vệ nguyên thủy.
> Là patterns emergent khi body detect: "thứ đã compiled vào baseline
> có nguy cơ bị absent — và tôi không chắc thay thế được."
>
> Từ "giữ đồ" → "giữ con" → "giữ ý tưởng" → "giữ identity" —
> cùng mechanism, khác object, khác intensity.
>
> NHƯNG protect KHÔNG phải lực duy nhất.
> Body cũng có giving dynamic — khi direct reward ≈ 0 (đã đủ),
> mirror reward (chia sẻ) > keep reward (giữ) → body TỰ drive cho đi.
> Gene "share khi thừa" THẮNG gene "giữ hết cho mình."
>
> File này: protect LÀ GÌ (ownership chunks + loss aversion),
> TẠI SAO mất đau hơn được (asymmetric prediction-delta),
> FORMULA tính intensity, hardware nào participate,
> ĐỐI TRỌNG TỰ NHIÊN (giving dynamic),
> và KHI NÀO protect là lành mạnh vs khi nào thành toxic.

---

## Mục lục

- §0 — PROTECT LÀ OBSERVATION PARAMETER
- §1 — CORE MECHANISM: OWNERSHIP CHUNKS + LOSS AVERSION
  - §1.1 — Ownership Chunks = Compiled Baseline
  - §1.2 — Loss Aversion = Asymmetric Prediction Delta
  - §1.3 — Tại Sao "Của Tôi" Tồn Tại Ở Body-Level
  - §1.4 — Cortisol: Amplifier, NOT Cause
- §2 — FORMULA: f(PERCEIVED REPLACEABILITY × ATTACHMENT CHUNKS)
  - §2.1 — Perceived Replaceability (PFC assessment, thường SAI)
  - §2.2 — Attachment Chunks (compile depth)
  - §2.3 — Interaction Matrix + Cases
- §3 — SPECTRUM: VẬT → NGƯỜI → Ý TƯỞNG → IDENTITY
  - §3.1 — Physical Objects (simplest)
  - §3.2 — People (complex, connection overlap, grief = open-loop protect)
  - §3.3 — Ideas + Beliefs (schema territory, confirmation bias)
  - §3.4 — Identity (most abstract, existential crisis = compound failure)
- §4 — BODY-LEVEL HARDWARE
  - §4.1 — Vasopressin: Defense Side of Bonding
  - §4.2 — Cortisol Direction Gate: Protect = Threat-Pull
  - §4.3 — Cross-Species Pattern
- §5 — CHUNK DYNAMICS × PROTECT
  - §5.1 — Chunk-Shift (revalue ownership)
  - §5.2 — Chunk-Miss (loss = absent baseline)
  - §5.3 — Chunk-Gap → Miss Transition (aspiration → ownership TRƯỚC possession)
  - §5.4 — Compound (devastating loss)
- §6 — ENDOWMENT EFFECT: BASELINE SHIFT → OWNERSHIP INFLATION
  - §6.1 — Mechanism (time × interaction)
  - §6.2 — Sunk Cost as Protect Pattern
  - §6.3 — Digital Ownership (modern variation)
- §7 — PROTECT × GIVING: ĐỐI TRỌNG TỰ NHIÊN
  - §7.1 — Mirror Reward Override (Agent-Mechanism.md §12.3)
  - §7.2 — Evolutionary Balance: Share vs Keep
  - §7.3 — Compassion Fatigue = Body Self-Protect
- §8 — PROTECT × OTHER PARAMETERS
  - §8.1 — × Threat (loss = threat trigger, 3 origin sources)
  - §8.2 — × Connection (attachment → ownership, grief = open-loop)
  - §8.3 — × Status (territorial maps)
  - §8.4 — × Autonomy (control dimension)
- §9 — HEALTHY vs TOXIC PROTECT
  - §9.1 — When Adaptive (5 dấu hiệu)
  - §9.2 — When Pathological (5 patterns)
  - §9.3 — Cultural Protect Schemas
- §10 — HONEST ASSESSMENT
  - §10.1 — Open Questions
- §11 — CROSS-REFERENCES

---

## §0 — PROTECT LÀ OBSERVATION PARAMETER

```
⭐ REFRAME V7.8:

  Core v7.5 (cũ): Protect = L3 operator (1 trong 3 drives: Novelty/Status/Protect)
                   → drive riêng, mechanism riêng, xếp ngang Novelty/Status

  Core v7.8 (mới): Protect = OBSERVATION PARAMETER
                    = Named pattern khi quan sát loss aversion + ownership chunks
                    = Emergent từ body-level chunk compilation + prediction-delta
                    = KHÔNG PHẢI component hay operator — là TÊN GỌI

  VỊ TRÍ TRONG CYCLE:

    ┌─────────────────────────────────────────────────────────┐
    │  BODY INPUTS (hardware)                                 │
    │    ↓                                                    │
    │  CHUNK PROCESSING (compile, predict, compare)           │
    │    ↓                                                    │
    │  PREDICTION DELTA (actual vs compiled baseline)         │
    │    ↓                                                    │
    │  ★ PROTECT = pattern observable TẠI ĐÂY ★              │
    │    = khi delta NEGATIVE + object đã compiled + low      │
    │      replaceability → body fires "giữ lại, đừng mất"   │
    │    ↓                                                    │
    │  BEHAVIOR: giữ, canh, ghen, kiểm soát, hoặc buông     │
    └─────────────────────────────────────────────────────────┘

  PROTECT KHÔNG PHẢI "BẢN NĂNG BẢO VỆ":
    → Framework v7.8 KHÔNG endorse khái niệm "bản năng" riêng
    → Protect = emergent pattern từ:
      ① Ownership chunks (compiled baseline: "thứ này = của tôi")
      ② Loss aversion (asymmetric delta: mất đau ~2× được)
      ③ Replaceability assessment (PFC evaluate: thay thế được không?)
    → 3 thành phần này đều có mechanism riêng đã document
    → "Protect" = tên gọi TIỆN khi observe patterns kết hợp

  ⭐ ARCHITECTURE B — TẠI SAO "PROTECT" TỒN TẠI (IBM §1.2):

    Architecture A (côn trùng): escape circuit hardwired → stimulus→flee.
    KHÔNG CÓ "protect" — vì không compile ownership, không có baseline
    → mất tổ = build tổ mới (KHÔNG đau, vì không có compiled baseline)

    Architecture B (mammals, humans):
    General-purpose system COMPILE experience → form baseline →
    mọi thứ đã compiled = PHẦN CỦA body-state →
    mất = baseline violated = pain signal THẬT.

    → "Protect" = ARCHITECTURE CONSEQUENCE:
      Hệ thống general-purpose COMPILE mọi thứ →
      mọi thứ đã compiled = có thể MẤT →
      cần mechanism phát hiện + respond to loss →
      = Protect EMERGE từ architecture, KHÔNG cần "bản năng bảo vệ" riêng

    → Architecture B organisms protect MORE thứ hơn A:
      A: chỉ protect body (hardwired)
      B: protect body + compiled objects + people + ideas + identity
      → SPECTRUM (§3) = consequence of general-purpose compilation depth

    🟡 Architecture A/B framing = framework synthesis (IBM §1.2).

  GIÁ TRỊ CỦA TÊN GỌI:
    → Predict: người protect cao X → dễ predict hành vi quanh X
    → Communicate: "anh ấy rất protect" dễ hiểu hơn mechanism
    → Diagnose: protect quá mạnh + threat cao = anxiety, kiểm soát
    → NHƯNG: can thiệp phải ở level mechanism, không ở level label
      (can thiệp = thay đổi body-input, re-compile chunks,
       adjust replaceability assessment — Core v7.8 §8)

  CORTISOL POSITIONING (Cortisol-Baseline.md §0.1 line 116):
    → Protect drive = cortisol MODERATE-HIGH, threat-pull
    → KHÁC novelty drive = cortisol LOW-MODERATE, domain-pull
    → = Protect gắn với AVOIDANCE direction, novelty gắn với APPROACH
    → = Chunks compiled under protect = tagged AVOIDANCE
      (Chunk.md v2.0 §2.4 NT7: cortisol direction gate at compile)
```

---

## §1 — CORE MECHANISM: OWNERSHIP CHUNKS + LOSS AVERSION

```
⭐ PROTECT = 2 THÀNH PHẦN CỐT LÕI:

  ┌──────────────────────────────────────────────────────────────┐
  │  OWNERSHIP CHUNKS              LOSS AVERSION                 │
  │  (compiled baseline:           (asymmetric prediction-delta: │
  │   "thứ này = của tôi")          mất đau ~2× được)           │
  │         │                              │                     │
  │         └──────────┬───────────────────┘                     │
  │                    ↓                                         │
  │           PROTECT PATTERN                                    │
  │      = body fires "giữ lại"                                  │
  │      = intensity tùy replaceability                          │
  └──────────────────────────────────────────────────────────────┘

  Ownership chunks KHÔNG CÓ → loss aversion KHÔNG FIRE.
  → Laptop người lạ hỏng → bạn không care.
  → Laptop bạn vừa mua hôm qua cũng hỏng → care NGAY.
  → Cùng laptop. Khác: ai đã compile "của tôi."

  Loss aversion KHÔNG CÓ → ownership chunks chỉ là data.
  → Biết laptop là "của mình" nhưng body không react khi hỏng?
  → Hiếm. Vì loss aversion là body-level mechanism (VTA, subcortical).
  → Chỉ xảy ra khi ownership chunks CHƯA compile deep
    (mua hôm nay, hỏng hôm nay → "thôi kệ, chưa quen").
```

### §1.1 — Ownership Chunks = Compiled Baseline

```
🟡 OWNERSHIP CHUNKS — BODY-LEVEL "CỦA TÔI":

  ĐỊNH NGHĨA:
    Khi body interact repeatedly với object/person/idea →
    experience compile thành chunks ở body-level (C+D zones).
    Pattern "X + tôi interact" → Hebbian LTP → wire cứng.
    Kết quả: body có BASELINE bao gồm X.
    → X là "của tôi" = X LÀ PHẦN CỦA COMPILED BASELINE.

  KHÔNG CẦN PFC DECLARE "CỦA TÔI":
    → Trẻ 2 tuổi giữ đồ chơi không cho bạn chơi.
    → Chưa có concept "sở hữu" ở PFC level.
    → Body ĐÃ compile: "đồ chơi này + tay tôi = baseline."
    → Ai lấy đi = Chunk-Miss = dissonance = khóc.
    → = Ownership chunk formation TRƯỚC khi có ngôn ngữ.

  COMPILE PATHWAY (BFM §5 Quality Baseline Shift):

    ① Interact lần 1: proto-chunk weak
       → PFC aware "cái này mới" nhưng body chưa shift baseline
       → Mất: PFC "hơi tiếc" > body dissonance (nhẹ)

    ② Interact lần 3-10: chunk strengthening
       → Body baseline bắt đầu include X
       → Mất: body dissonance RÕ (Chunk-Miss xuất hiện)
       → BFM §5: SNC effect bắt đầu (Crespi rats downshift)

    ③ Interact lần 50-100+: fully compiled
       → X = phần CỨNG của baseline
       → Mất: body dissonance MẠNH (SNC effect maximum)
       → Re-habituate (buông) = chậm, khó, đau
       → BFM §5 ④: re-habituate chậm vì strong compile = slow decay

    (BFM §5: compile_rate ≈ f(repetition × saliency × peak_valence
                               × multi_modal × contingency))

  VÍ DỤ:
    → Xe mới mua 1 ngày: scratch → "tức nhưng ok"
    → Xe đã lái 3 năm: scratch → "ai làm vậy?!" (compiled deep)
    → Nhà ở 20 năm: phải dọn → grief thực sự (body-level loss)

  ⭐ "CỦA TÔI" = GRADIENT, KHÔNG PHẢI BINARY:
    → Mới mua = ownership chunk weak
    → Dùng lâu = ownership chunk strong
    → Dùng lâu + emotional experience = ownership chunk VERY STRONG
    → Cùng vật, khác compile history → khác protect intensity
    → Giải thích: 2 người cùng mất laptop nhưng react KHÁC
      (người A: 1 tháng, dùng ít. Người B: 3 năm, memories trong đó.)
```

### §1.2 — Loss Aversion = Asymmetric Prediction Delta

```
🟢 LOSS AVERSION — MẤT ĐAU ~2× ĐƯỢC:

  🟢 Kahneman & Tversky 1979 (Prospect Theory):
    → Gaining $100: positive utility = X
    → Losing $100: negative utility ≈ 2X
    → = Body phản ứng với LOSS mạnh hơn GAIN cùng magnitude
    → = ASYMMETRIC prediction-delta

  CƠ CHẾ TRONG FRAMEWORK:

    ① Compiled baseline = X (VTA habituated)
    ② Actual quality TĂNG lên X+Δ:
       → VTA fires POSITIVE prediction-delta
       → Body signal: "tốt hơn expected" → reward
    ③ Actual quality GIẢM xuống X-Δ:
       → VTA fires NEGATIVE prediction-delta
       → Body signal: "tệ hơn expected" → dissonance
    ④ ⭐ ASYMMETRY: magnitude ③ > magnitude ② cho cùng Δ
       → = Loss aversion ở body-level

    (BFM §5 ĐẶC TÍNH ③: ASYMMETRIC — shift LÊN dễ hơn shift XUỐNG)
    (= Body resist quality decrease MẠNH hơn accept quality increase)

  TẠI SAO ASYMMETRIC? (evolutionary logic)
    → 🟡 Gaining something = nice but not survival-critical
    → Losing something already compiled = survival risk
    → Body đã invest resources compile pattern → mất = waste
    → Body bias TOWARD KEEPING > TOWARD GAINING = conservative strategy
    → Conservative strategy survives BETTER in uncertain environments

  🟢 SNC EVIDENCE (Crespi 1942, Flaherty 1996):
    → Rats: high reward → switch to low → ăn ÍT HƠN CẢ control group
    → = Không chỉ "hơi thất vọng" — phản ứng MẠNH HƠN neutral
    → = Body-level mechanism, KHÔNG CẦN PFC
    → = Loss aversion TỒN TẠI ở động vật = hardware-level
    → (BFM §3.2: SNC = Chunk-Miss mechanism at animal level)

  🟢 Schultz 1997 (dopamine neurons):
    → Expected = X, Actual < X → dopamine SUPPRESS below baseline
    → = Neural mechanism cụ thể cho negative prediction-delta
    → Dopamine suppress = CHỦ ĐỘNG signal "worse than expected"
    → Không phải "thiếu reward" — là ACTIVE negative signal

  ⚠️ NHƯNG: PREDICTION DELTA ≠ REWARD/PAIN
    (Clarification/Prediction-Error-Is-Not-Reward.md):
    → Prediction delta = VTA salience alert (chuông cửa: "có thay đổi!")
    → PAIN thật đến từ 3 nguồn khác: nociception / mismatch / recalibration
      (Body-Feedback.md: 3 nguồn khó chịu thật)
    → Cortisol = sustainer/amplifier, KHÔNG phải cause
      (Clarification/Cortisol-Amplifier-Not-Cause.md)
    → = Protect pain = BODY-BASE pain, not just "dopamine drop"
```

### §1.3 — Tại Sao "Của Tôi" Tồn Tại Ở Body-Level

```
🟡 "CỦA TÔI" KHÔNG PHẢI KHÁI NIỆM PFC — LÀ BODY STATE:

  BẰNG CHỨNG:

  ① Trẻ pre-verbal (12-18 tháng) ĐÃ protect đồ chơi:
     → Chưa có ngôn ngữ, chưa có concept "sở hữu"
     → Body đã compile: "tay tôi + đồ chơi này = baseline"
     → Ai lấy = baseline violated = dissonance = khóc/giữ chặt
     → = Ownership chunks compile TRƯỚC ngôn ngữ

  ② Động vật protect territory:
     → Chó: giữ xương, growl khi ai tới gần
     → Chim: giữ tổ, attack kẻ xâm nhập
     → KHÔNG có PFC phức tạp → = body-level mechanism
     → 🟢 Prairie vole: vasopressin → territorial defense (Young & Wang 2004)

  ③ Phantom limb (🟢):
     → Mất tay → body VẪN fire pattern "tay tôi ở đây"
     → = Compiled ownership chunks TỒN TẠI sau khi object mất
     → = Body KHÔNG "biết" tay đã mất → Chunk-Miss liên tục
     → Extreme case: body-level ownership của chính body parts

  ④ Endowment effect (🟢 Thaler 1980):
     → Người được cho cốc → định giá cao hơn người chưa có
     → CHỈ CẦN CẦM 30 GIÂY → ownership chunk bắt đầu form
     → = Body compile fast khi physical contact (multi-modal input)
     → = "Của tôi" bắt đầu ở body TRƯỚC KHI PFC quyết định giữ/bán

  IMPLICATION:
    → "Buông bỏ" bằng PFC rational decision = TẠM THỜI
    → Body-level ownership chunks VẪN fire (compiled, not erasable)
    → Buông thực sự = re-habituate (BFM §5 ④: sustained absence →
      baseline shift XUỐNG) — chậm, đau, nhưng possible
    → = Giải thích tại sao "biết nên buông" mà body vẫn giữ
    → PFC override possible nhưng COSTLY (fight body signal liên tục)
    → Duration of override = limited (PFC executive function = depletable)
```

### §1.3b — Compiled vs Fresh Protect (IBM §3)

```
⭐ PROTECT CÓ 2 CHẾ ĐỘ XỬ LÝ — TƯƠNG ỨNG COMPILED/FRESH AXIS:

  F1 COMPILED PROTECT (automatic, cost ≈ 0):
    → Ownership chunks ĐÃ compiled deep → loss signal fires TỰ ĐỘNG
    → Body react TRƯỚC KHI PFC kịp evaluate
    → Ví dụ: ai chạm vào con → mẹ phản ứng NGAY (compiled protection)
    → Ví dụ: nghe tin sếp restructure team → bụng thắt NGAY (compiled job ownership)
    → = Phản ứng bảo vệ tức thời, KHÔNG CẦN suy nghĩ
    → CÓ THỂ overgeneralize: protect quá mạnh cho thứ KHÔNG thực sự threatened

  F2 FRESH PROTECT (PFC evaluate, cost > 0):
    → Novel threat to valued entity → body alert NHƯNG PFC cần evaluate
    → "Đây có thực sự threatened không? Mất thì sao? Thay thế được không?"
    → Ví dụ: nghe tin công ty có thể bị mua lại → PFC đánh giá impact
    → Ví dụ: bạn nói "tôi muốn nói chuyện" → PFC evaluate: threat hay không?
    → Cost: PFC executive function + uncertainty + possible suppress body signal
    → = Chậm hơn nhưng CHÍNH XÁC hơn compiled protect

  F2 → F1 TRANSITION (compilation path):
    → Repeated loss of same type → pattern compile → next time = automatic
    → Người bị phản bội 3 lần → "dấu hiệu" compile → lần 4 body react NGAY
    → = Protect schemas LEARN + COMPILE over time
    → ⚠️ Trauma = forced compilation: 1 event CỰC MẠNH → compile ngay
       → post-trauma protect = overgeneralized compiled response

  🟡 Compiled/Fresh protect = framework synthesis (IBM §3, Kahneman S1/S2 consistent).
```

### §1.4 — Cortisol: Amplifier, NOT Cause

```
⭐ CORTISOL TRONG PROTECT — FRAMEWORK CLARIFICATION:

  ⚠️ Mainstream + pop science: "mất → cortisol → đau → protect"
  ⚠️ Framework: "mất → 3 nguồn đau THẬT → cortisol AMPLIFY + SUSTAIN"

  (Cortisol-Amplifier-Not-Cause.md — clarification chi tiết)

  CORTISOL TRONG PROTECT CYCLE:

    ① LOSS DETECTED → body-base pain fires (3 nguồn)
    ② Cortisol fires 20-30 phút SAU NE+Adrenaline spike
       → = SUSTAINER, không phải initiator
    ③ Cortisol AMPLIFY body sensitivity
       → ownership chunks fire MẠNH HƠN
       → loss signal PERSIST lâu hơn
    ④ Cortisol INERTIA (Cortisol-Baseline.md §2.3):
       → Object recovered → cortisol KHÔNG hạ ngay
       → Cortisol baseline takes weeks/months to re-calibrate
       → = Protect ANXIETY PERSISTS sau khi threat resolved
       → Ví dụ: tìm được ví bị mất → vẫn kiểm ví liên tục 1 tuần sau

  DIRECTION GATE (Cortisol-Baseline.md §3, Chunk.md §2.4 NT7):
    → Cùng cortisol level, KHÁC direction:
    → Protect cortisol = threat-pull → chunks tag AVOIDANCE
    → Novelty cortisol = domain-pull → chunks tag APPROACH
    → → Protect-related chunks compile VỚI avoidance tag
    → → Khi re-activate, body default AVOID (không approach)
    → → = Giải thích: sau mất mát, body TRÁNH situation tương tự
         (avoidance learning = protect-compiled chunks firing)

  GYM ANALOGY (Cortisol-Baseline.md intro):
    → Cortisol = GYM cho neurons
    → Không tập = thoái hóa (cortisol zero = Addison's)
    → Tập vừa + nghỉ đủ = mạnh hơn (acute stress + recovery = resilient)
    → Tập quá + không nghỉ = chấn thương (chronic cortisol + no repair = PFC damage)
    → = Protect acute (mất → recover → adapt) = HEALTHY
    → = Protect chronic (mất → not recover → cortisol sustain) = PATHOLOGICAL
    → Key variable = REPAIR capability (sleep), KHÔNG phải cortisol level
```

---

## §2 — FORMULA: f(PERCEIVED REPLACEABILITY × ATTACHMENT CHUNKS)

```
⭐ PROTECT INTENSITY FORMULA (Core v7.8 §8):

  Protect intensity = f(perceived replaceability × attachment chunks)

  ┌───────────────────────────────────────────────────────────────┐
  │                                                               │
  │  Replaceability THẤP + Attachment CAO = PROTECT CỰC MẠNH     │
  │  Replaceability CAO  + Attachment THẤP = PROTECT NHẸ          │
  │  Replaceability THẤP + Attachment THẤP = PROTECT VỪA          │
  │  Replaceability CAO  + Attachment CAO = PROTECT VỪA-CAO       │
  │                                                               │
  │  → 2 tham số NHÂN nhau, không CỘNG                            │
  │  → Replaceability thấp ALONE chưa đủ (nếu chưa attach)       │
  │  → Attachment cao ALONE → protect vẫn có nhưng giảm           │
  │    (vì "mất thì mua cái khác" = buffer)                      │
  │                                                               │
  └───────────────────────────────────────────────────────────────┘

  CORE INSIGHT TỪ V7.8 §8:
    → Laptop hỏng + đủ tiền mua mới (replaceability CAO) → ok
    → Laptop hỏng + không đủ tiền (replaceability THẤP) → ghét bạn
    → CÙNG attachment chunks (cùng laptop, cùng thời gian dùng)
    → KHÁC replaceability → KHÁC protect intensity
    → = Replaceability là GATE cho protect expression
```

### §2.1 — Perceived Replaceability (PFC assessment, thường SAI)

```
🟡 PERCEIVED REPLACEABILITY — PFC ASSESSMENT, KHÔNG PHẢI THỰC TẾ:

  QUAN TRỌNG: "perceived" — KHÔNG PHẢI replaceability THỰC TẾ.

  PFC assess: "nếu mất X, tôi có thể có lại X (hoặc tương đương) không?"
  → Assessment này có thể SAI — và THƯỜNG SAI:

  ① ĐÁNH GIÁ QUÁ THẤP (under-estimate replaceability):
     → "Không ai hiểu tôi như người này" (thực tế: nhiều người có thể)
     → "Job này là duy nhất" (thực tế: nhiều job tương đương)
     → = Compiled chunks + narrow experience → PFC thiếu data
     → → Protect OVER-FIRE → kiểm soát, anxiety, ghen tuông

  ② ĐÁNH GIÁ QUÁ CAO (over-estimate replaceability):
     → "Bạn bè thì thiếu gì" (thực tế: deep connection hiếm)
     → "Tiền thì kiếm lại được" (thực tế: opportunity cost real)
     → = Nhiều surface experience → PFC overgeneralize
     → → Protect UNDER-FIRE → buông quá dễ → regret later

  REPLACEABILITY FACTORS:
    → Resources (tiền, thời gian, năng lượng để thay thế)
    → Availability (thứ thay thế CÓ SẴN không?)
    → Uniqueness (thứ này có unique properties không?)
    → Compilation cost (phải compile lại bao lâu?)
    → Emotional investment (Imagine-Final gắn với object này?)

  ⭐ COMPILATION COST = HIDDEN FACTOR:
    → Mất laptop: mua mới = tiền. NHƯNG: setup lại, data, thói quen?
    → Mất relationship: gặp người khác possible. NHƯNG: compile lại
      attachment chunks từ đầu? 3-5 năm? More?
    → Compilation cost THƯỜNG bị ignore ở PFC level
    → Body BIẾT (vì body đã compile → biết "compile tốn bao nhiêu")
    → → PFC nói "thay được" nhưng body nói "đau" = dissonance
    → = "Biết là thay được nhưng không muốn" = body correct, PFC wrong
      (body account for compilation cost, PFC doesn't)
```

### §2.2 — Attachment Chunks (compile depth)

```
🟡 ATTACHMENT CHUNKS — COMPILE DEPTH QUYẾT ĐỊNH INTENSITY:

  Attachment chunks = ownership chunks đã compile TỚI MỨC NÀO.

  FACTORS ẢNH HƯỞNG COMPILE DEPTH
  (= BFM §5 compile_rate 5-parameter formula):

    ① Repetition: dùng/interact bao nhiêu lần?
       → 1 lần = proto-chunk → protect nhẹ
       → 100 lần = fully compiled → protect mạnh

    ② Saliency: experience có nổi bật không?
       → Laptop dùng bình thường = moderate saliency
       → Laptop dùng viết thesis, deadline, stress = HIGH saliency
       → = Emotional peak → faster, deeper compile

    ③ Multi-modal: bao nhiêu kênh input?
       → Chỉ nhìn (thấy trên kệ) = 1 kênh → weak
       → Cầm + dùng + nghe + smell = multi-modal → strong
       → = Physical contact ACCELERATE ownership chunk formation
       → (Thaler endowment: cầm 30 giây đủ shift)

    ④ Peak valence: emotional peaks gắn với object?
       → Nhẫn cưới = vật + emotional peak + shared experience
       → Laptop = vật + utility (moderate emotional)
       → → Nhẫn cưới protect >> laptop protect (cùng giá tiền)
       → (Valence-Propagation.md: valence TAG determines chunk weight)

    ⑤ Contingency: object CÓ GẮN VỚI REWARD TRỰC TIẾP?
       → Tool giúp kiếm tiền = contingent (reward linked)
       → Đồ trang trí = non-contingent (no direct reward link)
       → → Contingent objects compile FASTER (reinforcement)

  GRADIENT:
    Proto-chunk (weak) ────────────────── Fully compiled (strong)
    "biết là của mình"                    "PHẦN CỦA MÌNH"
    PFC-level only                        Body-level embedded
    Mất → "tiếc"                          Mất → grief thực sự
```

### §2.3 — Interaction Matrix + Cases

```
🟡 PROTECT INTENSITY MATRIX:

  ┌─────────────────────┬──────────────────────┬──────────────────────┐
  │                     │ Attachment THẤP      │ Attachment CAO       │
  │                     │ (weak compile)       │ (deep compile)       │
  ├─────────────────────┼──────────────────────┼──────────────────────┤
  │ Replaceability CAO  │ ① PROTECT NHẸ        │ ③ PROTECT VỪA-CAO   │
  │ (dễ thay thế)       │ Mất → "thôi kệ"     │ Mất → "tiếc nhưng   │
  │                     │ Ví dụ: bút bi mới   │  tìm cái khác"      │
  │                     │ mua                  │ Ví dụ: áo yêu thích │
  │                     │                      │  nhưng biết mua lại  │
  ├─────────────────────┼──────────────────────┼──────────────────────┤
  │ Replaceability THẤP │ ② PROTECT VỪA        │ ④ PROTECT CỰC MẠNH  │
  │ (khó thay thế)      │ Mất → "hmm, phiền"  │ Mất → grief / rage   │
  │                     │ Ví dụ: giấy tờ      │ Ví dụ: nhẫn cưới,   │
  │                     │ hiếm (chưa kịp gắn  │  con, relationship   │
  │                     │ bó nhưng khó thay)   │  20 năm              │
  └─────────────────────┴──────────────────────┴──────────────────────┘

  CASE STUDIES:

  Case ①: Bút bi mới mua
    → Compile: proto-chunk (vài giờ)
    → Replaceability: rất cao (vài ngàn đồng)
    → Mất → body signal minimal → PFC: "mua cái khác"
    → Protect intensity: ~0

  Case ②: Passport / giấy tờ quan trọng
    → Compile: weak (ít interact, để trong tủ)
    → Replaceability: thấp (thời gian + bureaucracy)
    → Mất → PFC stress > body dissonance
    → Protect intensity: moderate, mainly PFC-driven (not body-compiled)

  Case ③: Laptop dùng 3 năm + đủ tiền mua mới
    → Compile: deep (daily use, multi-modal, data, habits)
    → Replaceability: cao (tiền đủ, data backed up)
    → Mất → body dissonance real (compiled baseline absent)
         → NHƯNG PFC buffer: "mua được cái mới"
         → Body mourns BUT PFC provides path → manageable
    → Protect intensity: moderate-high

  Case ④: Con / partner / relationship sâu
    → Compile: extremely deep (years, multi-modal, emotional peaks)
    → Replaceability: extremely low (unique person, unique history)
    → Mất → body GRIEF (compiled patterns fire continuously,
              Chunk-Miss massive, no resolution possible)
    → Protect intensity: MAXIMUM
    → = Cha mẹ protect con = strongest protect humans have
      (maximum compile depth × minimum replaceability)
    → (Agent-Mechanism.md §12.6: "Grief = loss of real agent source
       + active SPM firing on memory → painful open-loop")
```

---

## §3 — SPECTRUM: VẬT → NGƯỜI → Ý TƯỞNG → IDENTITY

```
⭐ PROTECT KHÔNG CHỈ "GIỮ ĐỒ" — LÀ SPECTRUM TỪ CỤ THỂ TỚI TRỪU TƯỢNG:

  ┌────────────────────────────────────────────────────────────────────┐
  │  CỤ THỂ                                              TRỪU TƯỢNG │
  │  ←──────────────────────────────────────────────────────────────→ │
  │                                                                    │
  │  VẬT         NGƯỜI        Ý TƯỞNG        IDENTITY                │
  │  (đồ chơi,   (con, bạn,   (quan điểm,    (tôi là ai,            │
  │   xe, nhà)    partner)     niềm tin,      giá trị,               │
  │                            framework)      "kiểu người")          │
  │                                                                    │
  │  Hardware     Hardware     Mostly          Entirely                │
  │  + compiled   + compiled   compiled        compiled                │
  │               + connection                                         │
  │               + SPM (Agent)                                        │
  │                                                                    │
  │  Mất → có     Mất → có    Mất → không     Mất → identity          │
  │  thể thay     thể không   thể chứng      crisis                   │
  │  thế          bao giờ     minh "mất"                               │
  └────────────────────────────────────────────────────────────────────┘

  CÙNG MECHANISM — KHÁC OBJECT:
    → Ownership chunks compile cho TẤT CẢ types
    → Loss aversion apply cho TẤT CẢ types
    → Replaceability assessment apply cho TẤT CẢ types
    → KHÁC: complexity, duration, intensity, resolution path
```

### §3.1 — Physical Objects (simplest)

```
VẬT = PROTECT ĐƠN GIẢN NHẤT:

  Mechanism clear:
    → Body interact vật → compile ownership chunks
    → Physical contact = multi-modal → compile nhanh
    → Mất vật = Chunk-Miss rõ (BFM §3.2 ⓐ: biết thiếu gì)
    → Thay thế = mua/tìm cái mới → baseline re-habituate

  ĐẶC ĐIỂM:
    → Thường replaceability ĐÁNH GIÁ ĐƯỢC (tiền, available)
    → Compile depth tùy thời gian + emotional association
    → Duration: protect giảm nhanh khi có replacement
    → Exception: vật có emotional value (quà từ người đã mất,
      ảnh gia đình, nhật ký) → compile depth CỰC CAO
      → replaceability = 0 → protect = quasi-permanent

  VÍ DỤ GRADIENT:
    Bút bi → cốc yêu thích → laptop → xe → nhà →
    nhẫn cưới → ảnh gia đình duy nhất
    (protect tăng dần: replaceability GIẢM + attachment TĂNG)
```

### §3.2 — People (complex, connection overlap, grief = open-loop protect)

```
NGƯỜI = PROTECT PHỨC TẠP NHẤT:

  ⭐ PROTECT NGƯỜI ≠ CONNECTION NGƯỜI:
    → Connection = body reward khi CÙNG nhau (multi-input aggregate)
      (Connection.md §1: "thứ GIỮA 2 agents, không nằm TRONG")
    → Protect = body resistance khi có NGUY CƠ MẤT
    → Có thể: connection thấp NHƯNG protect cao
      (cha mẹ xa con: không vui khi ở cùng, nhưng rất protect)
    → Có thể: connection cao NHƯNG protect thấp
      (bạn bè vui vẻ nhưng "nếu mất thì thôi" — low compile depth)

  PROTECT NGƯỜI = PROTECT VẬT NHƯNG:
    ① Compile depth thường CAO HƠN nhiều (years of interaction)
    ② Multi-modal RICH (face, voice, touch, smell, shared memory)
    ③ Replaceability thường THẤP (unique person, unique history)
    ④ SPM ACTIVE: Self-Pattern-Match fire on person → enrich ownership
       (Agent-Mechanism.md §12: every successful SPM = partial agent input)
    ⑤ Dynamic: người thay đổi → ownership chunks phải UPDATE
       (vật static, người dynamic → protect phức tạp hơn)

  CHA MẸ → CON = PEAK PROTECT:
    → Compile depth: từ pregnancy/birth, 24/7, years
    → Multi-modal: mọi kênh input đều fire
    → Replaceability: = 0 (unique individual, không thay thế)
    → Hardware: vasopressin + oxytocin + cortisol response to child distress
    → SPM: parent constantly model child's state → deep ownership integration
    → = STRONGEST protect pattern humans produce
    → 🟡 Evolutionary logic: offspring = gene propagation,
      protect offspring = maximize reproductive success
    → (Empathy.md §6.3 line 1105: "L0 Protect Gene > L1 Nutrition")

  ⭐ GRIEF = PROTECT FIRING MÀ KHÔNG THỂ RESOLVE:
    → Người mất → compiled ownership chunks VẪN fire
    → Body expect patterns (voice, face, presence) → absent = Chunk-Miss
    → SPM VẪN fire on memory → body signals "social presence"
      NHƯNG feedback = 0 → painful open-loop
    → (Agent-Mechanism.md §12.6: "Grief = loss of real agent source
       + active SPM firing on memory → painful open-loop")
    → Chunk-Miss LIÊN TỤC, KHÔNG resolve (person KHÔNG return)
    → = Grief duration ≈ re-habituate time for deep compiled chunks
    → Sâu → lâu. Shallow → nhanh. (BFM §5: compile strength → decay time)
    → ĐẶC BIỆT: SPM memory fire → body senses "presence" →
      "they're still here somehow" = body literally sensing compiled patterns
```

### §3.3 — Ideas + Beliefs (schema territory, confirmation bias)

```
🟡 Ý TƯỞNG = "TERRITORY" TRỪU TƯỢNG:

  OWNERSHIP CHUNKS CHO Ý TƯỞNG:
    → "Quan điểm của tôi" = PFC-level compiled schemas
    → Compile qua: suy nghĩ, tranh luận, defend, teach, apply
    → Mỗi lần defend/apply = strengthen ownership chunk
    → → Ý tưởng trở thành "CỦA TÔI" giống vật trở thành "CỦA TÔI"

  MECHANISM GIỐNG HỆT:
    → Ai challenge ý tưởng = threat to ownership chunks
    → Body react: defensive, irritated, dig in
    → = CÙNG mechanism với ai lấy đồ chơi của trẻ 2 tuổi
    → PFC rationalize: "tôi bảo vệ CHÂN LÝ"
    → Body thực tế: "tôi bảo vệ OWNERSHIP CHUNKS"

  REPLACEABILITY CỦA Ý TƯỞNG:
    → Thấp khi: ý tưởng = identity core ("tôi TIN vào X")
    → Cao khi: ý tưởng = peripheral ("X có vẻ đúng, nhưng ok nếu sai")
    → → Protect intensity phụ thuộc vào GẦN IDENTITY bao nhiêu

  VÍ DỤ:
    → Nhà khoa học defend theory 20 năm:
      compile depth CỰC CAO (career, reputation, identity)
      + replaceability CỰC THẤP (thay theory = thay identity)
      = Protect CỰC MẠNH → resist evidence ngược
      = 🟢 Confirmation bias = PROTECT PATTERN cho ý tưởng

    → Framework này (!) = compiled chunks cho người viết:
      challenge framework = Chunk-Miss threat
      NHƯNG: nếu framework designed to UPDATE (v7.5→v7.8)
      → ownership chunks INCLUDE "updating = ok"
      → = Protect THẤP hơn cho specific version,
          Protect CAO cho underlying approach

  ⭐ BACKFIRE EFFECT (🟢 Nyhan & Reifler 2010):
    → Cho người evidence NGƯỢC quan điểm → hold STRONGER
    → = Protect firing: threat to ownership chunks → double down
    → = Cùng mechanism với trẻ giữ chặt đồ chơi hơn khi bị giật
    → Implication: muốn thay đổi ý tưởng ≠ attack
      → phải reduce perceived replaceability threat
      → cho alternative TRƯỚC khi challenge current (give replacement
        before taking away → reduce Chunk-Miss anticipation)
```

### §3.4 — Identity (most abstract, existential crisis = compound failure)

```
🟡 IDENTITY = PROTECT LEVEL CAO NHẤT:

  IDENTITY CHUNKS:
    → "Tôi là người như thế nào" = compiled self-schema
    → Bao gồm: values, capabilities, roles, relationships, beliefs
    → = TỔNG HỢP của tất cả ownership chunks ở các level khác

  TẠI SAO PROTECT IDENTITY = MẠNH NHẤT:
    → Compile depth: TOÀN BỘ CUỘC ĐỜI (mọi experience compile into self)
    → Multi-modal: mọi kênh input đều contribute
    → Replaceability: = 0 (bạn KHÔNG THỂ "thay thế" identity)
    → = Maximum depth × minimum replaceability = maximum protect

  IDENTITY THREAT CASES:

    ① "Tôi là người giỏi" → fail liên tục → identity chunk threatened
       → Protect fire: deny failure, blame external, avoid challenge
       → = Defensive mechanisms = PROTECT PATTERNS cho identity

    ② "Tôi là người tốt" → bị chỉ ra hành vi xấu → identity threat
       → Protect fire: rationalize, minimize, counter-attack
       → = Cognitive dissonance (🟢 Festinger 1957) = identity protect

    ③ "Tôi là đàn ông mạnh mẽ" → bị thấy khóc → identity threat
       → Protect fire: suppress emotion, deny vulnerability
       → = Toxic masculinity = CULTURAL identity protect schema

    ④ "Tôi là người sáng tạo" → stuck in routine → identity gap
       → Protect fire: anxiety, restless, seek novelty desperately
       → = Identity Gap = Chunk-Gap for self-schema

  ⭐ EXISTENTIAL CRISIS = MASSIVE IDENTITY PROTECT FAILURE:
    → Nhiều identity chunks bị challenge ĐỒNG THỜI
    → Ví dụ: mất job (role) + mất partner (relationship) + health scare
    → = Compound: Shift + Miss + Gap cho identity (BFM §4)
    → Body: massive cortisol, no resolution, no clear path
    → = "Tôi là ai?" = identity ownership chunks dissolving
    → Duration: prolonged vì identity = deepest compiled chunks
      → re-habituate = essentially rebuild self-schema
      → = Therapy duration for identity crisis = months-years
```

---

## §4 — BODY-LEVEL HARDWARE

```
⭐ PROTECT CÓ HARDWARE COMPONENTS — KHÔNG CHỈ COMPILED CHUNKS:

  Framework v7.8: observation parameter = emergent từ hardware + chunks.
  Protect đặc biệt rõ hardware contribution:
    → Vasopressin: defense side of bonding system
    → Cortisol: amplifier + direction gate (threat-pull)
    → Cross-species: hardware giống, chunk processing khác

  ⚠️ LƯU Ý: ở con người, hardware → chunk processing → behavior.
  Hardware KHÔNG trực tiếp drive behavior (khác động vật).
  = Core v7.8 §8: "cùng hormones, nhưng chunk system phức tạp → override."
```

### §4.1 — Vasopressin: Defense Side of Bonding

```
🟢 VASOPRESSIN = DEFENSE OF BONDED ATTACHMENT:

  🟢 Young & Wang (2004):
    → Oxytocin: "yêu" → gắn bó, tin tưởng
    → Vasopressin: "bảo vệ cái mình yêu" → canh giữ, territorial
    → = 2 MẶT của cùng bonding system
    → (Neurochemistry.md §8: "vasopressin = MẶT PHÒNG THỦ của oxytocin")

  🟢 PRAIRIE VOLE EVIDENCE (direct, animal):
    → Block vasopressin → VẪN gắn bó nhưng KHÔNG bảo vệ bạn đời
    → = Vasopressin MỘT MÌNH không tạo gắn bó
    → = Vasopressin BẢO VỆ gắn bó ĐÃ CÓ
    → = Defense mechanism cho compiled attachment chunks
    → = Protect ≠ create bond. Protect = DEFEND existing bond.

  BIẾN THIÊN (Neurochemistry.md §8):
    → Vasopressin CAO: bảo vệ mạnh, ghen tuông, kiểm soát
    → Vasopressin THẤP: gắn bó nhưng ít bảo vệ, dễ buông
    → Oxytocin cao + Vasopressin cao = "yêu nhiều, giữ chặt"
    → = KHÔNG mâu thuẫn — 2 hệ bổ sung cùng mạnh
    → Giải thích: "yêu thương + kiểm soát" = oxytocin + vasopressin cùng cao

  🟡 Ở CON NGƯỜI — INDIRECT EVIDENCE:
    → 🟢 Vasopressin receptor gene (AVPR1A) variation →
      correlate với partner bonding patterns (Walum et al. 2008)
    → NHƯNG: ở người, vasopressin → chunk processing → behavior
    → KHÔNG trực tiếp "vasopressin → protect" như ở vole
    → = Hardware bias (vasopressin) + compiled chunks = actual behavior
    → = Vasopressin SET TENDENCY, chunks DETERMINE expression

  FRAMEWORK POSITION:
    → Vasopressin = body-level BIAS TOWARD defending bonded objects
    → Không phải "protect hormone" — là defense-side of bonding system
    → Tương tự serotonin cho status: serotonin = certainty bias nền,
      KHÔNG PHẢI status decision maker (Status.md §7)
    → Vasopressin = defense bias nền, KHÔNG PHẢI protect decision maker
    → Chunks (compiled experience) = actual protect pattern
    → = Core v7.8 §8: "Protect parameter: hormone contribution
         vs chunk contribution ratio" (open research question)
```

### §4.2 — Cortisol Direction Gate: Protect = Threat-Pull

```
🟡 CORTISOL DIRECTION — TẠI SAO PROTECT = AVOIDANCE-TAGGED:

  (Cortisol-Baseline.md §7, Chunk.md v2.0 §2.4 NT7)

  DIRECTION PRINCIPLE (Source > Level):
    → CÙNG cortisol level, KHÁC direction → KHÁC chunk tag:
    → Novelty cortisol: curiosity body state → chunks tag APPROACH
    → Threat/loss cortisol: anxiety body state → chunks tag AVOIDANCE
    → Protect = almost always THREAT direction (loss = threat)

  IMPLICATION FOR PROTECT:

    ① Chunks compiled during protect = AVOIDANCE-tagged:
       → Body default: TRÁNH situation giống → future behavior avoid
       → Ví dụ: bị lừa tiền → chunks compile "lừa" với avoidance
       → → Tự động TRÁNH situations giống (dù rational analysis = safe)
       → = Protect-compiled chunks CREATE avoidance patterns

    ② Protect cortisol = MODERATE-HIGH (Cortisol-Baseline §0.1):
       → Higher than novelty (LOW-MODERATE) → body MORE mobilized
       → = Protect reactions = STRONGER, FASTER than novelty reactions
       → = Giải thích: body protect > body explore (survival priority)

    ③ Cortisol inertia applies (Cortisol-Baseline §2.3):
       → Loss → cortisol spike → sustain → INERTIA
       → Object recovered → cortisol KHÔNG hạ ngay
       → = Protect patterns PERSIST beyond actual threat
       → = Hyper-vigilance period sau loss/near-loss

  PROTECT × CORTISOL COUPLING (Cortisol-Baseline §10.6):
    → Same loss, KHÁC cortisol baseline → KHÁC experienced intensity
    → Người A (high baseline): mất ví = "hoảng loạn"
    → Người B (low baseline): mất ví = "phiền nhưng ok"
    → → Protect intensity = objective loss × personal cortisol baseline
    → → Anxious people (high cortisol) protect MẠNH HƠN cho cùng object
    → → Không phải "họ quá nhạy cảm" — là cortisol baseline difference
```

### §4.3 — Cross-Species Pattern

```
🟢 CROSS-SPECIES: CÙNG HARDWARE, KHÁC CHUNK PROCESSING:

  ĐỘNG VẬT:
    → Hardware (vasopressin, cortisol) → behavior GẦN TRỰC TIẾP
    → Chó: growl at food threat → immediate, predictable
    → Chim: attack nest intruder → immediate, predictable
    → Prairie vole: vasopressin → mate-guarding → immediate, predictable
    → = Hardware-driven protect, ít chunk modulation

  CON NGƯỜI:
    → Hardware (same hormones) → chunk processing → behavior
    → Chunk system: override, modulate, redirect, amplify, suppress
    → = CÙNG vasopressin firing nhưng KHÁC behavior output

  VÍ DỤ:
    → Vasopressin cao + compiled "ghen = bình thường" → ghen công khai
    → Vasopressin cao + compiled "ghen = xấu" → suppress → anxiety ngầm
    → Vasopressin cao + compiled "trust partner" → mild vigilance only
    → = CÙNG hardware, 3 behavior patterns KHÁC NHAU
    → = Chunks (compiled experience) DETERMINE expression

  → = Core v7.8 §8 cross-species pattern:
    "Ở động vật: hardware (hormone) → behavior trực tiếp
     Ở con người: hardware → chunk processing → behavior
     = Cùng hormones, nhưng chunk system phức tạp → override đáng kể
     = Giải thích tại sao human protect behavior khó đoán hơn nhiều"
```

---

## §5 — CHUNK DYNAMICS × PROTECT

```
⭐ BFM CHUNK DYNAMICS ÁP DỤNG CHO PROTECT:

  Body-Feedback-Mechanism.md define 3 chunk dynamics + compound.
  Mỗi dynamic có biểu hiện ĐẶC TRƯNG trong protect context.

  ┌──────────────────────────────────────────────────────────────┐
  │  Dynamic     │ Trong Protect context                        │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Chunk-Shift  │ Ownership chunks REVALUE (cùng object,      │
  │              │ khác perceived value/threat)                  │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Chunk-Miss   │ Owned object/person ABSENT                   │
  │              │ = compiled baseline → gone = LOSS             │
  │              │ = CORE mechanism underlying all protect loss  │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Chunk-Gap    │ Aspiration for ownership → NEED              │
  │              │ (chưa có nhưng network detect "nên có")      │
  │              │ ⭐ CÓ THỂ transition thành Miss (BFM §3.3)   │
  ├──────────────┼──────────────────────────────────────────────┤
  │ Compound     │ 2-3 dynamics ĐỒNG THỜI                      │
  │              │ (devastating loss = compound protect fire)    │
  └──────────────┴──────────────────────────────────────────────┘
```

### §5.1 — Chunk-Shift (revalue ownership)

```
CHUNK-SHIFT TRONG PROTECT:

  ĐỊNH NGHĨA (BFM §3.1): cùng chunks, VALENCE thay đổi.
  Object VẪN "của tôi" nhưng value/threat PERCEPTION shift.

  CASES:

  ① SHIFT LÊN (tăng protect):
     → Ai khen vật của bạn → bỗng "quý hơn" → protect tăng
     → Được biết vật hiếm → revalue → protect tăng
     → Threat gần (ai muốn mượn) → salience tăng → protect tăng
     → = Cùng compiled chunks, environmental cue shift valence

  ② SHIFT XUỐNG (giảm protect):
     → Biết vật rẻ hơn tưởng → "thôi kệ" → protect giảm
     → Có vật tốt hơn → cái cũ devalue → protect giảm
     → Relationship reveal: người mình protect BETRAY → revalue
       (protect → anger/disgust → protect collapse)
     → = BFM §4 "bạn thân lừa 100k": trust FLIP strong = Shift

  ③ SHIFT PHỨC TẠP (ambivalent):
     → Relationship tension: vẫn yêu nhưng hurt → protect + conflict
     → Object có history phức tạp: quà từ ex → protect + pain
     → = 2 valence directions CÙNG LÚC → body confused
     → = Chunk-Shift không luôn clean — có thể messy
```

### §5.2 — Chunk-Miss (loss = absent baseline)

```
CHUNK-MISS TRONG PROTECT = CORE LOSS MECHANISM:

  ĐỊNH NGHĨA (BFM §3.2): owned object/person ABSENT →
  compiled baseline violated. VTA detect: actual < baseline →
  negative prediction-delta → body signal "worse than expected."

  3 VARIANTS (BFM §3.2 ⓐⓑⓒ):

  ⓐ MISS RÕ — biết mất gì:
     → Laptop bị cướp → "laptop tôi mất" → PFC có label
     → Partner chia tay → biết rõ ai absent
     → Protect fire: tìm lại, đòi lại, hoặc grieve explicitly
     → = Resolution path rõ (nếu có)

  ⓑ MISS MỜ — delta tích tụ, không rõ source:
     → Dọn nhà mới → "có gì đó không ổn" (chưa biết thiếu gì)
     → = Compiled environmental patterns absent nhưng PFC không label
     → Protect fire: anxiety mờ, uneasy, không biết cần protect gì
     → ĐẶC BIỆT NGUY HIỂM: không target → không resolve
     → (BFM §3.2 ⓑ: "đặc biệt nguy hiểm: tích tụ silent → bùng khi quá ngưỡng")

  ⓒ MISS VÔ THỨC — body biết, PFC không:
     → Về quê sau lâu → "sao ở đây thoải mái" = MISS REWARD
       (compiled patterns fire lại → opioid → "thoải mái mà không biết vì sao")
     → Xa người thân lâu → "bình thường thôi" nhưng body cortisol cao
     → = Body compiled patterns absent → signal persistent nhưng silent
     → = Protect cần target mà PFC không see

  PROTECT × MISS DYNAMICS:
    → Compile depth CAO → Miss MẠNH → Protect MẠNH → duration LÂU
    → Compile depth THẤP → Miss NHẸ → Protect NHẸ → duration NGẮN
    → Re-habituate (BFM §5 ④): sustained absence → baseline shift xuống
    → NHƯNG: deep compile = slow re-habituate
    → → Mất partner 10 năm = YEARS of Chunk-Miss
    → → Mất laptop 1 tháng = WEEKS of Chunk-Miss
```

### §5.3 — Chunk-Gap → Miss Transition (aspiration → ownership TRƯỚC possession)

```
⭐ GAP→MISS TRANSITION — RẤT RELEVANT CHO PROTECT:

  (BFM §3.3 — 7 sub-mechanisms chi tiết)

  CƠ CHẾ CỐT LÕI:
    → Chunk-Gap: chưa SỞ HỮU nhưng network detect "nên có"
    → Imagine-Final preview lặp nhiều lần ("imagine having X")
    → Preview compile thành EXPECTATION BASELINE (BFM §5)
    → Body now EXPECTS cái chưa-từng-có
    → Reality vẫn KHÔNG có → VTA: actual < baseline
    → = Gap (ACC, mơ hồ) → Miss (VTA, cụ thể)
    → = PROTECT FIRE CHO THỨ CHƯA SỞ HỮU

  TẠI SAO RELEVANT CHO PROTECT:

    ① Pre-ownership protect:
       → Muốn nhà: xem nhiều → Imagine-Final compile "nhà tôi"
       → Mua được: "cuối cùng cũng có" (miss-reward feeling)
       → Deal fail: "MẤT nhà" (dù chưa bao giờ có)
       → = Gap→Miss: body treats aspiration AS IF already owned
       → = Protect fire cho thứ CHƯA LÀ "CỦA TÔI" trên giấy tờ

    ② Cortisol accelerator (BFM §3.3 ②):
       → Gap kéo dài + unresolved → cortisol holding signal
       → Cortisol forces PFC quay lại Imagine-Final → preview lặp CƯỠNG BỨC
       → Compile baseline NHANH hơn preview tự nguyện
       → = "Không ngừng nghĩ về nó" = cortisol accelerate Gap→Miss
       → = Protect-like anxiety TRƯỚC KHI thực sự own anything

    ③ Direction tag matters (BFM §3.3 ③):
       → Gap + novelty cortisol: "kỳ vọng hào hứng" → productive drive
       → Gap + threat cortisol: "kỳ vọng lo sợ" → protect anxiety
       → = Cùng Gap→Miss mechanism, KHÁC direction → KHÁC outcome
       → Protect direction = threat-tagged → anxiety loop

    ④ "Kỳ vọng càng cao, thất vọng càng lớn" (BFM §3.3 ⑦):
       → Preview VIVID + lặp NHIỀU → compile baseline CAO
       → Reality < baseline → Chunk-Miss delta LỚN → "thất vọng lớn"
       → = Protect cho expectations = real phenomenon, not irrational

  PROTECT BEHAVIOR TỪ GAP:
    → Eager to acquire, anxious about missing out (FOMO)
    → Defensive about "upcoming" possession (chưa có mà đã giữ)
    → Jealous of others who HAVE what you GAP
```

### §5.4 — Compound (devastating loss)

```
⭐ COMPOUND = TẠI SAO CERTAIN LOSSES DEVASTATING:

  (BFM §4: Compound Mechanism — chi tiết)

  Single dynamic = manageable.
  Compound = 2-3 dynamics ĐỒNG THỜI = overwhelming.

  ┌─────────────────────────────────────────────────────────────────┐
  │  Event                 │ Dynamics              │ Intensity      │
  ├────────────────────────┼───────────────────────┼────────────────┤
  │ Laptop hỏng            │ Miss alone            │ Moderate       │
  │ (thay thế được)        │                       │                │
  ├────────────────────────┼───────────────────────┼────────────────┤
  │ Bị lừa tiền bởi       │ Miss (tiền)           │ HIGH           │
  │ người quen             │ + Shift (trust flip)  │                │
  ├────────────────────────┼───────────────────────┼────────────────┤
  │ Bạn thân lừa 100k     │ Miss (tiền)           │ VERY HIGH      │
  │ (BFM §4 case)         │ + Shift (trust FLIP   │ (3 dynamics)   │
  │                        │   strong + connection │                │
  │                        │   damage)             │                │
  │                        │ + Gap ("tôi là ai mà  │                │
  │                        │   bạn thân lại lừa?") │                │
  ├────────────────────────┼───────────────────────┼────────────────┤
  │ Chia tay sau 10 năm    │ Miss (person absent)  │ VERY HIGH      │
  │                        │ + Shift (partner → ex) │                │
  │                        │ + Gap (future plans ≠) │                │
  ├────────────────────────┼───────────────────────┼────────────────┤
  │ Mất con               │ Miss (extreme compile) │ MAXIMUM        │
  │                        │ + Gap (future gone)    │ (irreversible) │
  │                        │ + Shift (self = parent │                │
  │                        │   → self = ?)          │                │
  │                        │ + SPM open-loop        │                │
  │                        │   (Agent-Mechanism.md §12.6)     │                │
  └────────────────────────┴───────────────────────┴────────────────┘

  TẠI SAO COMPOUND = DEVASTATING:
    → Mỗi dynamic = 1 cortisol source
    → Compound = MULTIPLE cortisol sources ĐỒNG THỜI
    → Body capacity to process = LIMITED
    → 3 dynamics > body capacity → OVERWHELM → shutdown hoặc spiral
    → = Mất người thân ≠ "buồn" — là system overload

  ⭐ COMPOUND PRINCIPLE (BFM §4):
    Signal_total = Σ (dynamics_i × intensity_i × network_size_i)
    → Nhiều dynamics = tổng signal MẠNH HƠN
    → Network_size lớn = propagation xa = affect nhiều chunks = MẠNH HƠN
    → = Tại sao "bạn thân phản bội" > "người lạ lừa" > "tự rơi"
      (cùng loss, khác compound level)
```

---

## §6 — ENDOWMENT EFFECT: BASELINE SHIFT → OWNERSHIP INFLATION

```
⭐ ENDOWMENT EFFECT = PROTECT MECHANISM TRONG ECONOMICS:

  🟢 Thaler 1980 / Kahneman, Knetsch & Thaler 1990:
    → Cho người cốc → hỏi "bán bao nhiêu?" → trung bình $7
    → Hỏi người khác "mua bao nhiêu?" → trung bình $3
    → CÙNG CỐC. Khác: ai ĐÃ CẦM.
    → = Ownership chunks form NHANH → inflate value → protect fire

  = PROTECT MECHANISM giải thích endowment effect:
    → Cầm cốc → body compile (physical contact, multi-modal)
    → Baseline shift: "cốc này = của tôi" (BFM §5 ①②)
    → Bán = mất = Chunk-Miss potential
    → Loss aversion: mất đau ~2× được → inflate selling price
    → = Endowment effect = protect pattern observable in economics
```

### §6.1 — Mechanism (time × interaction)

```
🟡 OWNERSHIP INFLATION = f(TIME × INTERACTION):

  ┌──────────────────────────────────────────────────────────────┐
  │  TIME OWNING        │  INFLATION EFFECT                      │
  ├──────────────────────┼───────────────────────────────────────┤
  │  30 giây (Thaler)   │  Nhẹ nhưng MEASURABLE (endowment)    │
  │  1 ngày             │  Proto-chunks → moderate inflation     │
  │  1 tuần             │  Chunks strengthening → noticeable     │
  │  1 tháng            │  Compiled → "thấy quen" → strong      │
  │  1 năm              │  Deep compile → "phần cuộc sống"       │
  │  10 năm+            │  Identity-level → "phần của TÔI"       │
  └──────────────────────┴───────────────────────────────────────┘

  INFLATION ≠ VALUE TĂNG:
    → Object không TỐT hơn theo thời gian (vật thì thậm chí hao mòn)
    → Body BASELINE INCLUDE object → mất = pain
    → Pain avoidance → inflate "giá bán" (require compensation > actual value)
    → = Protect mechanism CREATE illusion of higher value

  INTERACTION ACCELERATOR:
    → Chỉ SỞ HỮU (đồ trong tủ) = slow compile
    → SỞ HỮU + daily USE = fast compile
    → SỞ HỮU + emotional events = VERY fast compile
    → → Cùng 1 năm: đồ dùng hàng ngày > đồ cất trong tủ (protect intensity)
    → (BFM §5: compile_rate ≈ f(repetition × saliency × peak_valence
                                 × multi_modal × contingency))
```

### §6.2 — Sunk Cost as Protect Pattern

```
🟡 SUNK COST FALLACY = PROTECT PATTERN CHO INVESTMENT:

  🟢 Arkes & Blumer 1985:
    → Đã đầu tư → tiếp tục dù không rational → "đã lỡ rồi"
    → Economics: sunk cost = irrelevant cho future decision
    → Body: sunk cost = COMPILED OWNERSHIP CHUNKS cho investment

  PROTECT MECHANISM:
    → Invest time/money/effort vào X → compile ownership chunks cho X
    → Stop X = MẤT investment = Chunk-Miss
    → Loss aversion: mất investment đau ~2× potential gain từ stop
    → → Continue X dù X fails = PROTECT compiled investment chunks

  VÍ DỤ:
    → Xem phim dở 1 giờ → "đã xem 1 tiếng rồi, xem nốt"
      = Protect 1 giờ investment (dù 1 giờ tiếp sẽ CŨNG dở)
    → Relationship unhappy 5 năm → "đã 5 năm rồi, bỏ uổng"
      = Protect 5 năm compiled chunks (dù tiếp tục = thêm pain)
    → Business failing → "đã đổ 500 triệu, phải tiếp"
      = Protect financial + emotional investment chunks

  ⭐ SUNK COST STRENGTH ∝ COMPILE DEPTH:
    → Nhiều tiền + nhiều thời gian + emotional events = deep compile
    → → "Đã đổ" CÀNG nhiều → CÀNG khó bỏ
    → Không phải "irrationality" — là BODY-LEVEL protect pattern
      cho deep compiled chunks
    → Rational override (PFC) possible nhưng COSTLY (fight body signal)
    → = "Đau khi bỏ" = body signal THẬT, không phải "sai lầm nhận thức"
      (dù quyết định bỏ CÓ THỂ đúng — body signal vẫn real)
```

### §6.3 — Digital Ownership (modern variation)

```
🟡 DIGITAL OWNERSHIP = NEW PROTECT TERRITORY:

  HIỆN TƯỢNG:
    → Social media accounts, followers, posts, photos
    → Digital files, game items, virtual property
    → Online identity, reputation, reviews
    → Subscriptions, playlists, bookmarks, saved content

  PROTECT MECHANISM GIỐNG:
    → Compile ownership chunks qua repeated interaction
    → Time + emotional events = deep compile
    → Mất account = Chunk-Miss (compiled patterns absent)
    → Replaceability assessment (rebuild followers? recover photos?)

  ĐẶC BIỆT DIGITAL:

    ① FRAGILE: platform có thể delete bất cứ lúc nào
       → Ownership chunks COMPILED nhưng control = LOW
       → = Mismatch: body feels "của tôi" nhưng platform says "no"
       → = Protect fire nhưng NO ACTION available → anxiety

    ② ACCUMULATIVE: digital không degrade → compile LIÊN TỤC
       → 10 năm photos → massive ownership chunk library
       → Mất = massive Chunk-Miss (không thể recreate)
       → Duration of grief ∝ library size

    ③ SOCIAL IDENTITY: followers, reputation = STATUS ownership
       → Mất followers = Chunk-Miss + Status threat compound
       → (Status.md §9: Chunk Dynamics mapping)

    ④ SUNK COST EXTREME: 8 năm game progress, delete account?
       → = Protect CỰC MẠNH dù "chỉ là game"
       → Body doesn't distinguish "virtual" vs "physical" at chunk level

  IMPLICATION:
    → Digital protect = REAL protect (body doesn't distinguish substrate)
    → "Chỉ là mạng" → KHÔNG ĐÚNG ở body-level
    → Compiled chunks cho digital objects = same mechanism as physical
    → Mất digital = real grief (proportional to compile depth)
    → (Agent-Mechanism.md §12: body-response mechanism doesn't distinguish
       "real" from "schema-driven" at cortisol/oxytocin level)
```

---

## §7 — PROTECT × GIVING: ĐỐI TRỌNG TỰ NHIÊN

```
⭐ PROTECT KHÔNG PHẢI LỰC DUY NHẤT — CÓ ĐỐI TRỌNG:

  Nếu protect LÀ "giữ lại" → giving LÀ "cho đi."
  Cả hai = body-level mechanisms, KHÔNG phải PFC moral decision.
  Body TỰ TÍNH: "keep vs share" ở subcortical level.
  = Protect có COUNTERWEIGHT tự nhiên — evolution built BOTH.
```

### §7.1 — Mirror Reward Override (Agent-Mechanism.md §12.3)

```
🟡 MIRROR REWARD OVERRIDE — KHI "CHO" > "GIỮ":

  (Agent-Mechanism.md §12.3 — Cây xoài scenario)

  CƠ CHẾ:
    → Body-base satiated (xoài đã đủ ăn)
    → See neighbor who might enjoy xoài
    → Self-Pattern-Match fires: "neighbor ăn xoài → vui"
    → Body pre-experiences weak mirror reward từ simulated neighbor pleasure
    → Calculation:
      Keep xoài: reward ≈ 0 (already satiated → Chunk-Miss cho xoài = 0)
      Give xoài: mirror reward > 0 (SPM simulate neighbor pleasure)
    → ⭐ Mirror reward > keep reward → body drives giving action

  KEY INSIGHT:
    → Đây KHÔNG PHẢI "đạo đức" hay "ý thức tốt"
    → Là BODY-LEVEL CALCULATION: keep reward vs share reward
    → Khi direct reward LOW (đã đủ) → mirror reward WIN → cho đi
    → Khi direct reward HIGH (đang thiếu) → keep reward WIN → giữ lại
    → = Protect vs Giving = DYNAMIC BALANCE, not fixed ratio

  CONDITION FOR GIVING TO WIN:
    ① Direct need satiated (body đã đủ)
    ② SPM quality sufficient (can simulate other's pleasure)
    ③ Compilation cost of sharing LOW (giving ≠ losing much)
    ④ Mirror reward detectable (empathy chunks compiled)
    → NẾU thiếu bất kỳ condition → protect WIN → keep

  IMPLICATION:
    → "Hào phóng" ≠ personality trait → = satiation + SPM quality
    → "Keo kiệt" ≠ personality trait → = unsatiated + poor SPM
    → → Can thiệp: satisfy basic needs → SPM naturally drives sharing
    → → Force sharing khi unsatiated = PFC override (depletable, fragile)
```

### §7.2 — Evolutionary Balance: Share vs Keep

```
🟡 EVOLUTIONARY: TẠI SAO EVOLUTION GIỮ CẢ PROTECT VÀ GIVING:

  (Empathy.md §7 — evolutionary function + positive-sum logic)

  GENE "GIỮ HẾT CHO MÌNH":
    → Short-term advantage: resources secured
    → Long-term risk: group cooperation GIẢM
    → = Isolate → no backup → die alone when crisis hits

  GENE "SHARE KHI THỪA":
    → Short-term cost: resources shared
    → Long-term advantage: group cooperation TĂNG
    → = Embedded in group → mutual aid → survive crisis
    → (Empathy.md: "Gene 'share khi thừa' THẮNG gene 'giữ hết cho mình'")

  EVOLUTIONARY SOLUTION = BOTH:
    → Keep gene: protect CÁI ĐÃ CÓ (survival baseline)
    → Share gene: give PHẦN THỪA (group cooperation bonus)
    → = Body TÍCH HỢP cả hai: protect when scarce, share when abundant
    → = Dynamic balance, NOT one or the other

  FRAMEWORK REFRAME:
    → Protect = ADAPTIVE khi scarce (giữ = survive)
    → Protect = MALADAPTIVE khi abundant (giữ hết = isolate)
    → Giving = ADAPTIVE khi satiated (chia = cooperate)
    → Giving = MALADAPTIVE khi scarce (cho hết = die)
    → = Context quyết định: CÁI NÀO dominant = tùy satiation level
    → = Không có "tốt" hay "xấu" tuyệt đối

  ⭐ MODERN MISMATCH:
    → Scarcity environment (historically): protect = ĐÚNG đa số trường hợp
    → Abundance environment (modern): protect STILL fires ở body-level
    → = Body compiled từ history, chưa re-habituate abundance
    → = "Thừa mà vẫn giữ" = protect pattern from scarcity era
      firing in abundance context
    → (Mismatch pattern: hardware/compiled reactions ≠ current environment)
```

### §7.3 — Compassion Fatigue = Body Self-Protect

```
🟡 COMPASSION FATIGUE = PROTECT ÁP DỤNG CHO CHÍNH MÌNH:

  (Empathy.md §8 line 1322: "Compassion fatigue = body self-protect")

  CƠ CHẾ:
    → SPM fire liên tục cho người khác → body absorb stress signals
    → Cortisol tích tụ → body-base depleted
    → Body detect: "tôi đang mất resources" = self-Chunk-Miss
    → Protect fire CHO CHÍNH MÌNH → suppress empathy → withdraw
    → = Body SELF-PROTECT khi empathy overload

  3 DEFENSE MECHANISMS (Empathy.md §8):
    → ① Blunting: giảm SPM sensitivity → "không cảm nữa"
    → ② Avoidance: tránh exposure → "không muốn nghe thêm"
    → ③ Dissociation: disconnect body signal → "bình thường thôi"
    → = TẤT CẢ = protect patterns applied to SELF resources

  PROTECT HIERARCHY IMPLIED:
    → Protect SELF > protect OTHERS (evolutionary priority)
    → Compiled pattern: "nếu tôi suy yếu, không thể protect ai khác"
    → → Self-protect TRƯỚC → recover → empathy restore
    → = Oxygen mask principle: put your own first
    → = Không phải "ích kỷ" — là body-level resource management

  IMPLICATION:
    → Healthcare workers, caregivers, therapists = high compassion fatigue risk
    → KHÔNG PHẢI "empathy quá cao" → là "protect-self mechanism firing"
    → Treatment: restore body resources (sleep, rest, own needs met)
      → body-base recover → protect-self reduces → empathy capacity returns
    → Force empathy khi depleted = PFC override (fragile, counterproductive)
```

---

## §8 — PROTECT × OTHER PARAMETERS

```
⭐ PROTECT KHÔNG ĐỘC LẬP — INTERACT VỚI MỌI OBSERVATION PARAMETER:

  Protect = emergent pattern → overlap và interact với tất cả.
  4 interactions quan trọng nhất:
```

### §8.1 — × Threat (loss = threat trigger, 3 origin sources)

```
PROTECT × THREAT = CLOSELY LINKED:

  ⭐ PROTECT VÀ THREAT OVERLAP NHƯNG KHÁC:
    → Threat = dissonance from PREDICTED HARM (broad — Threat.md §1)
    → Protect = resistance to LOSING OWNED THINGS (specific)
    → Protect ⊂ Threat in many cases (loss of owned = a type of threat)
    → NHƯNG: Threat > Protect (threat từ harm CHƯA liên quan ownership)
    → Ví dụ: threat từ tiếng ồn lớn = threat, không phải protect
             threat từ "sắp mất laptop" = protect-triggered threat

  3 ORIGIN SOURCES (Threat.md §4) APPLIED TO PROTECT:

    ① DOMAIN origin: natural loss risk → healthy protect response
       → Đồ dễ vỡ → cẩn thận → proportional protect
       → Kinh tế bất ổn → tiết kiệm → proportional protect
       → = ADAPTIVE: risk real, protect proportional

    ② PEER origin: competition → protect territory → manageable
       → Bạn bè cạnh tranh → protect position → normal
       → Thị trường cạnh tranh → protect market share → normal
       → = Protect fires within peer dynamics, bounded by context

    ③ IMPOSED origin: authority teach "MẤT = CHẾT" → OVER-FIRE
       → Cha mẹ: "CẨN THẬN! MẤT LÀ KHÔNG ĐƯỢC!"
       → → Compile "mất = catastrophe" schema
       → → Protect OVER-FIRE cho MỌI object (disproportional)
       → = Most toxic protect patterns = IMPOSED origin
       → = Child compiles threat schema WITHOUT direct experience
       → = Protection anxiety in adults = often IMPOSED childhood origin

  VICIOUS CYCLE (tương tự Status.md §10):
    → High protect → see more loss threats → cortisol → higher protect
    → → "Người lo sợ mất" → hyper-vigilant → see threat everywhere
    → → Cortisol inertia → SUSTAIN anxiety beyond actual threat
    → Break: reduce perceived threat → cortisol down → protect normalizes
```

### §8.2 — × Connection (attachment → ownership, grief = open-loop)

```
PROTECT × CONNECTION = COMPLEX OVERLAP:

  CONNECTION BUILD PROTECT:
    → Connection compile attachment chunks (Connection.md §1-§2)
    → Attachment chunks = ownership chunks cho người
    → → Connection TĂNG → Protect cho người đó TĂNG
    → → "Càng thân → càng sợ mất" = connection building protect

  NHƯNG KHÁC NHAU:
    → Connection = reward KHI CÙNG nhau (present-focused)
    → Protect = resistance KHI NGUY CƠ MẤT (threat-focused)
    → Có thể: high connection + low protect (enjoy now, ok if ends)
    → Có thể: low connection + high protect (don't enjoy but can't leave)

  ⭐ "LOW CONNECTION + HIGH PROTECT" = TOXIC PATTERN:
    → Relationship không happy NHƯNG can't leave
    → = Connection reward LOW (not enjoying together)
    → = Protect HIGH (compiled chunks + low replaceability)
    → = Sunk cost + loss aversion > connection reward
    → = Body "giữ" vì SỢ MẤT, không phải vì MUỐN CÙNG
    → Common in: long unhappy relationships, codependency

  GRIEF = PROTECT × CONNECTION COMPOUND (Agent-Mechanism.md §12.6):
    → Connection source GONE → SPM still fires on memory
    → Body senses "presence" (compiled patterns) nhưng feedback = 0
    → = Painful open-loop: protect fires, no resolution, no target
    → = Most intense khi connection + protect BOTH extremely high
    → Duration ∝ compile depth of BOTH connection + ownership chunks

  SECURE ATTACHMENT = BALANCED:
    → High connection (enjoy together) + moderate protect (care but not anxious)
    → = Protect fires khi THỰC SỰ threatened, not chronic
    → = Vasopressin + oxytocin balanced

  ANXIOUS ATTACHMENT = PROTECT DOMINANT:
    → Moderate connection + HIGH protect (always worried about losing)
    → = Cortisol baseline elevated → protect chronic
    → = Compiled "loss = catastrophe" từ early experience (imposed origin)
    → = Protect override enjoyment → relationship = anxiety management
```

### §8.3 — × Status (territorial maps)

```
PROTECT × STATUS = TERRITORIAL OVERLAP:

  STATUS MAP = PROTECT TERRITORY:
    → Status = schema access patterns (Status.md §1: Schema Access Map)
    → Status maps compiled → "vị trí của tôi trong nhóm"
    → Maps = OWNED patterns → protect applies
    → Mất status maps = Chunk-Miss → protect fire

  HIERARCHY AS PROTECT STRUCTURE:
    → Hierarchy = simplest status map (1 dimension)
    → Position trong hierarchy = OWNED territory
    → Ai challenge position = threat to owned territory
    → → Protect fire: defend position, attack challenger
    → = "Bảo vệ vị trí" = protect pattern cho status maps

  STATUS PROTECT CASES:
    → CEO protect title: position compiled deep → high protect
    → Expert protect reputation: domain mastery → ownership chunks
    → Parent protect "good parent" image: identity + status compound
    → → Tất cả = protect patterns cho compiled status maps

  SEROTONIN × VASOPRESSIN:
    → 🟡 Serotonin = certainty bias cho status position (Status.md §7)
    → 🟡 Vasopressin = defense bias cho bonded territory (§4.1)
    → High cả 2: confident + defensive = "vị trí vững + giữ chặt"
    → Low serotonin + high vasopressin: insecure + defensive = anxious protect
    → → Combination matters, không single hormone
```

### §8.4 — × Autonomy (control dimension)

```
🟡 PROTECT × AUTONOMY = CONTROL DIMENSION:

  AUTONOMY = "tôi quyết → kết quả tôi muốn" (Core v7.8 §8)
  PROTECT = "giữ cái tôi có"

  OVERLAP:
    → Owned things mà tôi CONTROL = protect + autonomy satisfied
    → Owned things mà NGƯỜI KHÁC control = protect fire MẠNH
    → = Protect TĂNG khi autonomy bị threatened

  VÍ DỤ:
    → Nhà tôi, tôi trang trí tùy ý = low protect (autonomy HIGH)
    → Nhà thuê, chủ nhà cấm sửa = high protect (autonomy LOW over owned space)
    → = CÙNG ownership chunks nhưng KHÁC autonomy → KHÁC protect
    → Laptop tôi, tôi toàn quyền = moderate protect
    → Laptop tôi, company giám sát = protect + autonomy COMPOUND threat

  IMPLICATION:
    → Reduce control over owned things = AMPLIFY protect
    → → Regulation, restrictions on property → protect + autonomy compound
    → → Helicopter parenting: control child's owned territory → child protect fire
    → → Micromanagement: control employee's domain → protect + status compound
    → = Autonomy loss = protect AMPLIFIER (each reinforces the other)
```

---

## §9 — HEALTHY vs TOXIC PROTECT

```
⭐ PROTECT LÀ SPECTRUM — KHÔNG TỐT KHÔNG XẤU TỰ NÓ:

  Protect = observation parameter. Mechanism hoạt động.
  KHI NÀO adaptive, khi nào pathological = TÙY CONTEXT.
  (= Cùng principle với Threat.md §6: threat có lợi và có hại)
```

### §9.1 — When Adaptive (5 dấu hiệu)

```
HEALTHY PROTECT = BOUNDED + PROPORTIONAL + RESOLVING:

  5 DẤU HIỆU PROTECT LÀNH MẠNH:

  ① BOUNDED: protect fire khi THỰC SỰ threatened, stop khi safe
     → Khóa cửa khi đi = protect bounded → adaptive
     → Kiểm khóa 10 lần = protect UNBOUNDED → pathological

  ② PROPORTIONAL: intensity phù hợp với actual risk
     → Lo mất ví khi đi chợ đông = proportional
     → Lo mất ví khi ở nhà = disproportional
     → = §2 formula: accurate replaceability + accurate attachment assessment

  ③ RESOLVING: protect có ACTION và action WORKS
     → Backup data → protect resolve → cortisol down
     → Lo mất data + KHÔNG backup = protect unresolved → chronic
     → = Protect + action → resolution → cortisol normalize

  ④ FLEXIBLE: có thể BUÔNG khi replaceability changes
     → Xe cũ → xe mới → buông xe cũ ok = flexible
     → Xe cũ → xe mới → VẪN giữ xe cũ "nhỡ đâu" = inflexible
     → = Re-habituate hoạt động bình thường (BFM §5 ④)

  ⑤ BALANCED WITH GIVING: protect ≠ override sharing
     → Protect cái cần + share cái thừa = balanced (§7)
     → Protect MỌI THỨ + share KHÔNG GÌ = protect dominant → isolation
     → = §7.2: context quyết định: scarce → protect, abundant → share

  EVOLUTIONARY VALUE:
    → Protect owned resources = survival advantage
    → Protect offspring = gene propagation
    → Protect territory = resource security
    → = ADAPTIVE when bounded, proportional, aligned with survival
    → = Body mechanism DESIGNED to be adaptive — pathology = distortion
```

### §9.2 — When Pathological (5 patterns)

```
TOXIC PROTECT = CHRONIC + DISPROPORTIONAL + UNRESOLVABLE:

  ① HOARDING (🟢 DSM-5 Hoarding Disorder):
     → Protect fire cho MỌI owned object
     → Replaceability assessment BROKEN: "mọi thứ đều irreplaceable"
     → = Ownership chunks compile nhưng KHÔNG decay (BFM §5 ④ blocked)
     → = Miss ⓑ (mờ): body signal "thiếu" khi vứt BẤT CỨ GÌ
     → Treatment: không phải "vứt đi" → phải re-calibrate
       replaceability assessment + allow re-habituate

  ② JEALOUS CONTROL:
     → Protect partner QUÁ mức → kiểm soát, theo dõi, isolate
     → = Vasopressin HIGH + compiled "mất = catastrophe" schema
     → = Protect override connection → relationship = prison
     → = Often IMPOSED origin: "nếu không giữ chặt, mất" (§8.1 ③)
     → = Connection.md overlap: protect destroy the connection it tries to keep

  ③ TERRITORIAL AGGRESSION:
     → Protect territory → attack bất kỳ ai "xâm phạm"
     → Online: "đây là topic CỦA TÔI, đừng có ý kiến"
     → Workplace: "đây là project CỦA TÔI, đừng có tham gia"
     → = Protect × status compound → aggressive defense
     → = Ideas as territory (§3.3) → aggression when challenged

  ④ IDENTITY RIGIDITY:
     → Protect identity chunks → REFUSE all change/growth
     → "Tôi luôn như vậy" = protect identity baseline
     → Mọi feedback = threat → defensive → stagnate
     → = Protect identity SO STRONG → override learning
     → = §3.4: identity protect at maximum → growth impossible

  ⑤ SUNK COST TRAP:
     → Protect investment → continue failing endeavors
     → Years in wrong career, unhappy relationship, bad investment
     → = §6.2: compiled chunks too deep → protect override rational PFC
     → = Not "stupidity" — body signal genuinely says "đau khi bỏ"

  COMMON THREAD:
    → All pathological protect = protect OVERRIDE other signals
    → Body says "giữ" → PFC agrees (or can't override)
    → Other needs SACRIFICED: connection, autonomy, growth, health
    → = Protect becomes DOMINANT parameter → suppress everything else
    → = §7: giving dynamic SUPPRESSED → isolation → more protect → spiral
```

### §9.3 — Cultural Protect Schemas

```
🟡 CULTURAL SCHEMAS SHAPE PROTECT PATTERNS:

  PROTECT SCHEMAS = COMPILED FROM ENVIRONMENT:
    → Culture teach: "X = cần protect, Y = ok mất"
    → Family teach: protect intensity for specific objects
    → Experience teach: what loss ACTUALLY feels like
    → = Schemas KHÔNG innate — compiled qua experience + imposed teaching

  EXAMPLES:

  ① COLLECTIVIST CULTURES (🟡):
     → Family = CORE ownership → protect family EXTREME
     → Individual property = secondary → protect objects MODERATE
     → "Mất mặt gia đình" = compound: protect × status × connection
     → = Cultural schema: family honor = most protected territory

  ② INDIVIDUALIST CULTURES (🟡):
     → Personal property = high protect
     → Personal freedom = high protect (autonomy × protect)
     → Family = important but not override-level
     → = Cultural schema: "my stuff, my choice, my life"

  ③ SCARCITY ENVIRONMENTS:
     → Everything scarce → replaceability LOW for everything
     → → Protect fire MẠNH cho mọi thứ (survival-proportional)
     → → Hoard when possible = ADAPTIVE in scarcity (not pathological)
     → → Transition to abundance: protect patterns PERSIST
       (cortisol inertia + compiled schemas don't auto-update)
     → = Post-war generation: protect food, objects, money = compiled scarcity
     → = §7.2: "thừa mà vẫn giữ" = scarcity-compiled protect in abundance

  ④ IMPOSED PROTECT SCHEMAS (most relevant):
     → "Cẩn thận! Mất là chết!" = parent compile threat schema
     → "Đàn ông phải protect gia đình" = gender role compile
     → "Tiền để dành, đừng tiêu" = financial protect schema
     → → Tất cả = IMPOSED (Threat.md §4 ③) → compile WITHOUT experience
     → → Có thể OVER-FIRE: protect pattern disproportional to actual risk
     → → Most common source of toxic protect in modern environments
```

---

## §10 — HONEST ASSESSMENT

```
⭐ ĐÁNH GIÁ TRUNG THỰC — FRAMEWORK PROTECT ANALYSIS:

  ┌──────────────────────────────────────────────────────────────────┐
  │  CLAIM                              │ CONFIDENCE │ STATUS       │
  ├─────────────────────────────────────┼────────────┼──────────────┤
  │ Loss aversion ~2× (Kahneman 1979)  │ 🟢         │ Robust       │
  │ SNC in animals (Crespi 1942)       │ 🟢         │ Replicated   │
  │ Dopamine suppress = loss signal    │ 🟢         │ Schultz 1997 │
  │ Endowment effect (Thaler 1980)     │ 🟢         │ Robust       │
  │ Vasopressin → defend bond (vole)   │ 🟢         │ Young 2004   │
  │ AVPR1A gene × bonding (human)      │ 🟢         │ Walum 2008   │
  │ Cognitive dissonance (Festinger)    │ 🟢         │ Established  │
  │ Backfire effect (Nyhan & Reifler)   │ 🟢         │ Replicated   │
  │ Sunk cost fallacy (Arkes 1985)     │ 🟢         │ Established  │
  │ Cortisol = amplifier not cause     │ 🟢         │ Clarified    │
  │ SPM → grief open-loop (Agent §12)  │ 🟡         │ Synthesis    │
  │ Chunk-Miss = core loss mechanism   │ 🟡         │ Synthesis    │
  │ Ownership chunks = body-level      │ 🟡         │ Synthesis    │
  │ f(replaceability × attachment)     │ 🟡         │ Framework    │
  │ Vasopressin = defense bias (human) │ 🟡         │ Indirect     │
  │ Protect × Giving balance           │ 🟡         │ Synthesis    │
  │ Mirror reward override mechanism   │ 🟡         │ Framework    │
  │ Gap→Miss transition for protect    │ 🟡         │ Extension    │
  │ Compound dynamics = multiplicative │ 🟡         │ Logical      │
  │ Digital ownership = same mechanism │ 🟡         │ Extrapolation│
  │ Sunk cost = protect pattern        │ 🟡         │ Reframe      │
  │ Identity protect = highest level   │ 🟡         │ Framework    │
  │ Compassion fatigue = self-protect  │ 🟡         │ Reframe      │
  │ Cultural schemas shape protect     │ 🟡         │ Observation  │
  │ Cortisol direction gate for protect│ 🟡         │ Synthesis    │
  │ Architecture B → protect emergent │ 🟡         │ Synthesis    │
  │ Compiled/Fresh protect 2 modes    │ 🟡         │ Synthesis    │
  └─────────────────────────────────────┴────────────┴──────────────┘

  WHAT'S STRONG:
    → Loss aversion, endowment effect, SNC = very well-established
    → Vasopressin role in animal bonding defense = well-established
    → Dopamine prediction-delta mechanism = well-established
    → Cognitive dissonance, sunk cost = well-established
    → Cortisol = amplifier (not cause) = well-clarified in framework
    → = Foundation research ROBUST — framework builds ON established science

  WHAT'S FRAMEWORK SYNTHESIS:
    → Mapping Chunk-Miss/Shift/Gap/Compound onto protect = novel reframe
    → f(replaceability × attachment) = framework formula, not tested empirically
    → Spectrum vật→người→ý tưởng→identity = logical extension, not proven
    → Protect × Giving balance via mirror reward = synthesis from Agent-Mechanism.md + Empathy.md
    → Gap→Miss transition for protect = extension of BFM mechanism
    → SPM grief open-loop = synthesis from Agent-Mechanism.md §12
    → = Novel framework contributions, internally consistent, not yet validated

  WHAT'S HONESTLY UNCERTAIN:
    → Vasopressin role in HUMAN protect behavior = indirect evidence only
    → Exact hormone/chunk contribution ratio = unknown (Core v7.8 open Q)
    → Whether compound dynamics are truly multiplicative vs additive = unknown
    → Digital ownership compile rate vs physical = no comparative data
    → Cultural schema transmission mechanism for protect = under-researched
    → Compassion fatigue as "self-protect" = plausible reframe, not proven
```

### §10.1 — Open Questions

```
6 CÂU HỎI MỞ:

  Q1: Hormone contribution vs chunk contribution ratio?
      → Core v7.8 §8 open question
      → Vasopressin SET bias nhưng chunks DETERMINE expression
      → Ratio? Context-dependent? Domain-dependent?
      → Cần: pharmacological studies + behavioral correlation

  Q2: Protect decay rate for different object types?
      → Physical objects: fast re-habituate (weeks-months?)
      → People: slow (months-years?)
      → Ideas: unknown (decades?)
      → Identity: possibly never full re-habituate?
      → Cần: longitudinal studies on attachment decay

  Q3: Digital ownership compile rate vs physical?
      → Physical: multi-modal (touch, weight, temperature)
      → Digital: visual + interaction nhưng less sensory
      → Is compile rate SLOWER? Or compensated by interaction frequency?
      → 8 giờ/ngày digital interaction vs 1 giờ/ngày physical?
      → Cần: comparative endowment studies physical vs digital

  Q4: Protect × Imagine-Final interaction?
      → Protect fire MẠNH hơn khi Imagine-Final INCLUDES owned object?
      → "Tương lai tôi CÓ X" → mất X = Imagine-Final violated?
      → = Protect + meaning compound?
      → Cần: study protect intensity × future planning specificity

  Q5: Mirror reward override threshold?
      → At what satiation level does giving > keeping?
      → Is threshold individual (personality/experience) or universal?
      → Can threshold be trained (meditation, practice)?
      → Cần: behavioral economics studies with satiation manipulation

  Q6: Imposed protect schema — can it be fully un-compiled?
      → "Mất = catastrophe" schema compiled in childhood
      → Therapy can build override schemas (PFC level)
      → Can BODY-LEVEL compiled schema actually decompile?
      → Or only override/suppress (PFC, depletable)?
      → Cần: longitudinal therapy outcome studies
      → = Related to §1.3: "biết nên buông" mà body vẫn giữ
```

---

## §11 — CROSS-REFERENCES

```
CORE FILES:
  → Core-v7.8-Draft.md §8 — Protect definition, observation parameter framework
  → Core-v7.8-Draft.md §8 open Q — Hormone vs chunk contribution ratio

DRILL SOURCE:
  → Inter-Body-Mechanism.md v1.0 §1.2 — Architecture B (protect = emergent from general-purpose)
  → Inter-Body-Mechanism.md v1.0 §3 — Compiled/Fresh axis (compiled vs fresh protect)

MECHANISM FILES:
  → Body-Feedback-Mechanism.md v2.0 §3.1 — Chunk-Shift (revalue)
  → Body-Feedback-Mechanism.md §3.2 — Chunk-Miss (core loss mechanism, 3 variants)
  → Body-Feedback-Mechanism.md §3.3 — Chunk-Gap (→ Gap→Miss transition, 7 sub-mechanisms)
  → Body-Feedback-Mechanism.md §4 — Compound dynamics (100k case, principle formula)
  → Body-Feedback-Mechanism.md §5 — Quality Baseline Shift (endowment foundation, asymmetry)
  → Cortisol-Baseline.md v2.0 §0.1 — Protect = cortisol MODERATE-HIGH, threat-pull
  → Cortisol-Baseline.md v2.0 §2.3 — Cortisol inertia
  → Cortisol-Baseline.md v2.0 §3 — Direction gate (novelty vs threat cortisol)
  → Cortisol-Baseline.md v2.0 §7 — Source > Level principle
  → Cortisol-Baseline.md v2.0 §10.6 — Cortisol × baseline coupling
  → Chunk.md v2.0 §2.4 NT7 — Cortisol direction gate at compile
  → Agent-Mechanism.md §12 — Body-need feeder (social presence as need)
  → Agent-Mechanism.md §12.3 — Mirror reward override (giving mechanism)
  → Agent-Mechanism.md §12.6 — Grief = loss of agent source + SPM open-loop

CLARIFICATION FILES:
  → Clarification/Cortisol-Amplifier-Not-Cause.md — Cortisol ≠ stress, ≠ pain cause
  → Clarification/Prediction-Error-Is-Not-Reward.md — PE ≠ reward, 3 pain sources

VOCABULARY:
  → Body-Feedback-Label.md v2.0 — prediction-delta, Compiled/Fresh, terminology consistency

OBSERVATION PARAMETER FILES:
  → Threat.md v1.1 — 3 origin sources (Domain/Peer/Imposed), loss as threat
  → Connection.md v4.0 — Attachment chunks, hardware vs compiled, grief overlap
  → Status.md v2.1 — Schema Access Map, §9 Chunk Dynamics, territorial maps
  → Empathy.md v3.0 — SPM function, §7 sharing dynamics, §8 compassion fatigue
  → Novelty.md — Parallel: novelty = PULL toward new, protect = RESIST losing old
  → Boredom.md — Chunk-Miss ⓑ (mờ) mechanism cross-reference
  → Liking-Wanting.md — Wanting mechanisms overlap with protect motivation

REFERENCE FILES:
  → backup/Neurochemistry.md §8 — Vasopressin detail (Young & Wang 2004)
  → Imagine-Final-Evaluation.md — Evaluation framework (protect × Imagine-Final)
  → Valence-Propagation.md v2.0 — Body evaluation, chain propagation

KEY RESEARCH CITATIONS:
  → 🟢 Kahneman & Tversky 1979 — Prospect Theory, loss aversion ~2×
  → 🟢 Thaler 1980 — Endowment effect
  → 🟢 Kahneman, Knetsch & Thaler 1990 — Endowment experiment
  → 🟢 Crespi 1942 / Flaherty 1996 — SNC (animal loss response)
  → 🟢 Schultz 1997 — Dopamine prediction-delta neurons
  → 🟢 Young & Wang 2004 — Vasopressin and bonding defense
  → 🟢 Walum et al. 2008 — AVPR1A gene and human pair bonding
  → 🟢 Arkes & Blumer 1985 — Sunk cost fallacy
  → 🟢 Nyhan & Reifler 2010 — Backfire effect
  → 🟢 Festinger 1957 — Cognitive dissonance
  → 🟢 Brickman 1978 — Hedonic adaptation
  → 🟢 DSM-5 — Hoarding Disorder criteria
  → 🟢 Coan 2015 — Social Baseline Theory
  → 🟢 Eisenberger 2003 — Social pain = physical pain regions
```

---

## SUMMARY

```
PROTECT = OBSERVATION PARAMETER (v7.8)
= Loss aversion + ownership chunk patterns
= f(perceived replaceability × attachment chunks)

CORE (§1):
  → Ownership chunks = compiled baseline ("của tôi" ở body-level)
  → Loss aversion = asymmetric prediction-delta (mất đau ~2× được)
  → Body-level (pre-verbal, cross-species), NOT PFC concept
  → Cortisol = amplifier NOT cause (Clarification file)

FORMULA (§2):
  → Replaceability × Attachment → 2×2 matrix + 4 cases
  → Perceived replaceability (PFC, thường SAI)
  → Compilation cost = hidden factor body knows, PFC doesn't

SPECTRUM (§3): vật → người → ý tưởng → identity
  (cùng mechanism, khác object, khác intensity)
  → Grief = open-loop protect (SPM fires, no feedback)
  → Confirmation bias = protect cho ý tưởng
  → Existential crisis = compound identity protect failure

HARDWARE (§4): vasopressin (defense bias 🟢 vole, 🟡 human)
  + cortisol direction gate (protect = threat-pull, avoidance-tagged)
  → Cross-species: same hardware, different chunk processing

CHUNK DYNAMICS (§5): Shift / Miss / Gap→Miss / Compound
  → Miss = core loss. Gap→Miss = pre-ownership protect.
  → Compound = devastating (multiplicative, not additive).

ENDOWMENT (§6): baseline shift → ownership inflation → sunk cost
  + digital ownership (body doesn't distinguish substrate)

PROTECT × GIVING (§7): ĐỐI TRỌNG TỰ NHIÊN
  → Mirror reward override: keep ≈ 0 → share > keep → body gives
  → Evolution built BOTH: protect when scarce, share when abundant
  → Compassion fatigue = body self-protect (protect SELF > protect OTHERS)

CROSS-PARAMETER (§8): ×Threat (3 origins, imposed=most toxic),
  ×Connection (grief=compound), ×Status (territorial), ×Autonomy (control)

HEALTHY vs TOXIC (§9): bounded/proportional/resolving + balanced giving
  vs chronic/disproportional + 5 pathological patterns
  → Cultural schemas SHAPE protect (imposed origin = most toxic source)

FILE: ~1,950 lines | 11 sections + summary
VERSION: v1.1 | 2026-05-17 (refine từ v1.0)

v1.1 CHANGES (2026-05-17):
  ⑪ +Architecture B: protect = emergent observation trong general-purpose system
     (Architecture A: không compile ownership → không có "protect")
  ⑫ +Compiled/Fresh protect: F1 compiled (auto, cost ≈ 0) vs F2 fresh (PFC evaluate)
     + trauma = forced compilation, overgeneralization risk
  ⑬ Agent.md → Agent-Mechanism.md throughout (renamed 2026-04-24)
  ⑭ Version refs updated (VP v2.0, Empathy v3.0, Connection v4.0, BFM v2.0)
  ⑮ +IBM v1.0, +BFL v2.0 cross-refs
  ⑯ Honest Assessment: +2 🟡 (Architecture B, Compiled/Fresh)
```
