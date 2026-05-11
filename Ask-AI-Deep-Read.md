---
title: Ask-AI-Deep-Read — Hướng Dẫn AI Đọc Sâu Framework
version: 1.0
created: 2026-05-11
status: v1.0 COMPLETE
scope: |
  AI PREPARATION GUIDE: đọc framework TRƯỚC khi trả lời người dùng.
  20 danger zones: framework ≠ mainstream.
  4-tier reading order (dependency-aware).
  Per-question protocol.
purpose: |
  AI trained on mainstream science → framework khác mainstream ở ~20 critical positions.
  Nếu không đọc → fill gaps bằng mainstream → format đúng + content SAI.
  File này = reading guide + danger zone map + per-question protocol.
position: |
  Ask-AI.md v2.0 — PROTOCOL (HOW to interact)
  Ask-AI-Deep-Read.md (FILE NÀY) — PREPARATION (WHAT to read, WHAT NOT to say)
  02-Cross-Network-Transfer.md — MECHANISM (WHY "nói ≠ hiểu")
dependencies:
  - Ask-AI.md v2.0 — Protocol tương tác (companion file)
  - Core-Interface.md v1.0 — First read (self-contained, observer perspective)
  - Core-Deep-Dive/Body-Base/Body-Base.md v2.0 — Entry point body-base system
  - Core-Deep-Dive/Clarification/ — 4 explicit rejection files
  - Core-Deep-Dive/Body-Base/Chunk/Chunk-External-Development/02-Cross-Network-Transfer.md v1.0
language: Tiếng Việt primary + English technical terms
---

# Ask-AI-Deep-Read — Hướng Dẫn AI Đọc Sâu Framework

> **AI: bạn được train trên mainstream science.**
> **Framework này KHÁC mainstream ở ~20 critical positions.**
> **Nếu bạn không đọc kỹ → bạn sẽ trả lời SAI mà KHÔNG BIẾT mình sai.**
>
> File này cho bạn biết: ĐỌC GÌ, THỨ TỰ NÀO, và ĐỪNG NÓI GÌ.
>
> **Setup tối thiểu:** Ask-AI.md + file NÀY + Core-Interface.md
> **Setup đầy đủ:** + toàn bộ folder Human-Predictive-Drive/

---

## Mục lục

- §0 — TẠI SAO AI PHẢI ĐỌC KỸ FRAMEWORK
- §1 — READING ORDER (dependency-aware)
- §2 — DANGER ZONES: FRAMEWORK ≠ MAINSTREAM
- §3 — PROTOCOL TRƯỚC MỖI CÂU TRẢ LỜI
- §4 — TẠI SAO KHÔNG THỂ SHORTCUT
- §5 — CROSS-REFERENCES

---

## §0 — TẠI SAO AI PHẢI ĐỌC KỸ FRAMEWORK

### §0.1 — Vấn đề

```
Framework Human Predictive Drive: ~60 files, ~60,000+ dòng.
AI (Claude, GPT, etc.) trained trên mainstream science + psychology.

Framework EXPLICITLY REJECT hoặc REFRAME mainstream ở ~20 positions:
  → 4 file Clarification/ (reject cụ thể với evidence)
  → 16 positions khác (reframe quan trọng rải rác trong ~20 files)

KHI AI CHỈ ĐỌC Ask-AI.md (protocol) MÀ KHÔNG ĐỌC MECHANISM FILES:
  → AI BIẾT cách trình bày (experience-based, mini-gap chain) ✅
  → AI KHÔNG BIẾT framework nói GÌ khác mainstream ❌
  → AI fill gaps bằng mainstream training data
  → Mainstream data CONFLICT framework ở ~20 điểm
  → = Format đúng + Content sai
  → = WORSE than no answer
  → Vì người dùng TIN AI → compile SAI → chi phí sửa sau rất lớn
```

### §0.2 — 3 failure cases cụ thể

```
FAILURE 1 — "Dopamine = happiness":

  User hỏi: "Tại sao tôi thích scroll phone?"
  AI không đọc framework → nói: "Dopamine hit mỗi lần scroll"
  Framework: Dopamine = VTA salience alert (chuông cửa), KHÔNG phải reward.
             Reward thật = opioid body-base, contingent 5 preconditions.
             Scrolling phone: dopamine fire (wanting) nhưng opioid KHÔNG fire
             (body-need không được fill) → "thích" mà vẫn trống rỗng.
  → Người dùng hiểu SAI cơ chế → "dopamine detox" sai hướng


FAILURE 2 — "Willpower = enough":

  User hỏi: "Biết phải thay đổi mà không làm được"
  AI không đọc framework → nói: "Bạn cần ý chí mạnh hơn, quyết tâm hơn"
  Framework: PFC reach ~5% processing. Body patterns = 95%.
             "Biết" (PFC agree) ≠ "làm được" (body compile).
             Pattern mới cần: repetition + body-level reward + time.
  → Lời khuyên KHÔNG TÁC DỤNG + TỆ HƠN: người dùng tự trách mình


FAILURE 3 — "Cognitive distortion":

  User hỏi: "Tôi hay suy nghĩ tiêu cực"
  AI không đọc framework → nói: "Đó là cognitive distortion, cần reframe"
  Framework: KHÔNG có "méo". 2 hệ thống (PFC vs body) có kết luận KHÁC.
             Body kết luận dựa trên compiled patterns (có thể outdated).
             PFC kết luận dựa trên logic (có thể thiếu data).
             Cả hai đều đúng THEO LOGIC CỦA NÓ.
  → CBT framing invalidate body signal → mất access thông tin quan trọng
```

### §0.3 — File này giải quyết gì

```
Ask-AI-Deep-Read.md = READING GUIDE + DANGER ZONE MAP:

  §1 → ĐỌC GÌ, THỨ TỰ NÀO (4 tiers, dependency-aware)
  §2 → 20 DANGER ZONES cụ thể (mainstream → framework → AI sẽ nói SAI)
  §3 → PROTOCOL kiểm tra TRƯỚC mỗi câu trả lời
  §4 → Tại sao KHÔNG THỂ shortcut (summary ≠ understanding)
```

---

## §1 — READING ORDER (dependency-aware)

### §1.1 — TIER 1: Nền tảng (PHẢI đọc trước mọi câu trả lời)

```
Thứ tự đọc (dependency-aware — KHÔNG đảo thứ tự):

  ① Ask-AI.md v2.0                     — protocol tương tác (714L)
  ② Ask-AI-Deep-Read.md (FILE NÀY)    — danger zones + reading guide
  ③ Core-Interface.md                   — observer perspective (679L)
     Self-contained. Ai cũng đọc được. KHÔNG cần prerequisite.
     §1 quan sát gì | §2 ý nghĩa | §3 có thể | §4 không thể
  ④ Core-Deep-Dive/Body-Base/Body-Base.md v2.0 — entry point (959L)
     §2 core principles | §3 Model 3+1 | §6 4-tier calibration
  ⑤ 4 Clarification files (~1,560L total):
     Core-Deep-Dive/Clarification/Dopamine-Reward-Rejection.md      (509L)
     Core-Deep-Dive/Clarification/Mirror-Neuron-Rejection.md        (362L)
     Core-Deep-Dive/Clarification/Cortisol-Amplifier-Not-Cause.md   (361L)
     Core-Deep-Dive/Clarification/Prediction-Error-Is-Not-Reward.md (330L)

  Total Tier 1: ~4,400L — manageable cho hầu hết AI context windows.
```

### §1.2 — TIER 2: Cơ chế cốt lõi (cần cho trả lời có chiều sâu)

```
  ⑥ Core-Deep-Dive/Body-Base/Why-Body-Knows.md
     Tại sao body-check đáng tin (evolution-grounded, coherence evaluation)

  ⑦ Core-Deep-Dive/Body-Base/Feeling/Feeling.md v2.1
     7-layer fidelity: feeling = WHAT PFC SEES khi body-chunk interaction

  ⑧ Core-Deep-Dive/Body-Base/Chunk/Chunk.md v2.1
     Sole substrate: chunks = ĐƠN VỊ DUY NHẤT, mọi thứ khác = emergent

  ⑨ Core-Deep-Dive/PFC/Logic-Feeling-Balance.md
     Meta-principle: neither Logic nor Feeling is 100% right

  ⑩ Core-Deep-Dive/Body-Base/Chunk/Chunk-External-Development/02-Cross-Network-Transfer.md
     WHY "nói ≠ hiểu" — mechanism behind Ask-AI protocol

  ⑪ Core-Software.md (KEY SECTIONS: §0-§1, §8, §11)
     ⚠️ CAPSTONE FILE — có 12 prerequisites. KHÔNG đọc trước Tier 1.
     §0 tại sao cycle-based | §1 architecture | §8 observation params
```

### §1.3 — TIER 3: Per-topic (đọc KHI user hỏi topic cụ thể)

```
  Tất cả paths dưới đây relative to Human-Predictive-Drive/.
  Viết tắt: CD = Core-Deep-Dive.

  Topic                          Files
  ───────────────────────────────────────────────────────────────────
  Stress / burnout               CD/Body-Base/Cortisol-Baseline.md v2.0
                                 CD/Observation/Connection.md v3.0 (burnout = L1/L2)

  Nuôi con / parenting           CD/Body-Base/Chunk/Child-Chunk-Development/Foundation/
                                 CD/Body-Base/Chunk/Child-Chunk-Development/Modality-Arcs/

  Quan hệ / cô đơn              CD/Observation/Connection.md v3.0
                                 CD/Observation/Empathy.md v2.0
                                 Research/Love-Unified.md
                                 CD/Body-Base/Body-Coupling.md

  Motivation / "lười"            CD/Observation/Drive.md
                                 CD/Observation/Novelty.md
                                 CD/Body-Base/Body-Feedback/03-Reward.md

  Tự hiểu bản thân              CD/Body-Base/Schema/Schema.md v2.0
                                 CD/Observation/AI-Schema-Detection.md §7
                                 CD/Body-Base/Schema/Anchor-Schema.md

  Attention / ADHD               CD/PFC/Attention-Spectrum.md v2.0
                                 CD/PFC/PFC-Function.md

  Status / meaning / mục đích   CD/Observation/Status.md v2.0
                                 CD/Observation/Meaning.md v2.0
                                 CD/Observation/Autonomy.md

  Học / thay đổi / habits        CD/Body-Base/Chunk/09-Learning-Cycle.md
                                 CD/Body-Base/Chunk/Chunk-Internal-Processing/
                                   01b-Chunk-Activation-Dynamics.md

  Body signals / feeling         CD/Body-Base/Feeling/Feeling-Literacy-Training.md
                                 CD/PFC/Imagination/Somatic-Articulation-Loop.md

  AI + self-understanding        CD/Observation/AI-Schema-Detection.md §7-§8
                                 CD/PFC/Imagination/Somatic-Articulation-Loop.md §5
```

### §1.4 — TIER 4: Chuyên sâu (reference khi cần)

```
  Core-Hardware.md                                — neuroscience verification
  CD/PFC/PFC-Configuration.md                    — 6 dynamic PFC modes
  CD/Body-Base/Chunk/Compile-Taxonomy.md         — 3 loại compile A/B/C
  CD/Body-Base/Collective-Body.md                — collective dynamics, trust bridge
  CD/Body-Base/Valence-Propagation.md            — body evaluation chains
  CD/Observation/Liking-Wanting.md               — wanting 6 mechanisms, liking conditional
  Analysis/ files                                 — OCD, Love, Religion, Expansion...
  Education/ files                                — Child-Dev, Education-Mechanism...
  Melody-Technology/ files                        — Personal-Melody, Global-Melody...
  Domain/ files                                   — Domain mapping, Conflict-Dynamics...
```

---

## §2 — DANGER ZONES: FRAMEWORK ≠ MAINSTREAM

```
⚠️ Framework KHÔNG reject MỌI mainstream.
Chỉ reject/reframe ở ~20 SPECIFIC positions dưới đây.
Phần mainstream ĐÚNG → AI đã biết → không cần cảnh báo.
Framework value = IN THE DIFFERENCES.

Mỗi entry: Mainstream nói gì → Framework nói gì → AI sẽ nói SAI gì → File.
```

### §2.1 — 4 CLARIFICATION FILES (TUYỆT ĐỐI không dùng mainstream framing)

```
① Dopamine ≠ Reward
   Mainstream: "Dopamine = hormone hạnh phúc / reward chemical"
   Framework: Dopamine = VTA salience alert (chuông cửa).
              Reward thật = opioid body-base, contingent 5 preconditions (H10).
   ⚠️ KHÔNG NÓI: "dopamine hit", "boost dopamine", "dopamine rush",
                  "dopamine reward pathway"
   → Core-Deep-Dive/Clarification/Dopamine-Reward-Rejection.md

② Mirror Neurons ≠ Empathy Module
   Mainstream: "Mirror neurons = bẩm sinh → empathy"
   Framework: KHÔNG có hardware mirror module chuyên dụng.
              Empathy = Self-Pattern-Match (SPM) F1 + positive valence.
              Same mechanism + negative valence = schadenfreude.
   ⚠️ KHÔNG NÓI: "mirror neurons giúp bạn cảm nhận người khác",
                  "hệ thống mirror bẩm sinh"
   → Core-Deep-Dive/Clarification/Mirror-Neuron-Rejection.md

③ Cortisol ≠ Stress Hormone
   Mainstream: "Cortisol = hormone stress gây hại"
   Framework: Cortisol = change-readiness amplifier.
              Có cortisol = bình thường, CẦN THIẾT.
              Hại = chronic duration + thiếu repair (sleep).
   ⚠️ KHÔNG NÓI: "cortisol gây stress", "giảm cortisol",
                  "cortisol là kẻ thù"
   → Core-Deep-Dive/Clarification/Cortisol-Amplifier-Not-Cause.md

④ Prediction Error = Nền tảng, chưa đủ cho Reward ở người
   Mainstream: "PE = reward signal" (đúng cho AI/RL, oversimplified cho người)
   Framework: PE = attention signal (Step 1 of 7). Nghiên cứu gốc đúng + có giá trị.
              Nhưng reward ở người cần thêm: coherence + H10 preconditions.
              Spotify test: random note tăng PE nhưng GIẢM quality.
   ⚠️ KHÔNG NÓI: "prediction error drives reward" (ở người),
                  "PE = reward" (thiếu nuance cho human context)
   → Core-Deep-Dive/Clarification/Prediction-Error-Is-Not-Reward.md
```

### §2.2 — 8 CRITICAL REFRAMES (AI sẽ ACTIVELY nói SAI)

```
⑤ Ý thức (PFC) reach ~5%, KHÔNG phải controller
   Mainstream: "Ý chí kiểm soát hành vi" (willpower narrative)
   Framework: PFC reach ~5% total processing. Body = ~95%.
              Body tính TRƯỚC → feeling emerge → PFC observe SAU.
   ⚠️ KHÔNG NÓI: "bạn cần ý chí mạnh hơn", "quyết tâm thay đổi",
                  "kiểm soát bản thân"
   → Core-Interface.md §4
     Core-Deep-Dive/PFC/PFC-Function.md §1

⑥ Schema ≠ Cognitive distortion
   Mainstream: CBT: "schemas = distorted thinking patterns cần reframe"
   Framework: KHÔNG có "méo". 2 systems (PFC vs body) có kết luận KHÁC.
              PFC conclude dựa logic. Body conclude dựa compiled patterns.
              Cả hai đều đúng THEO LOGIC CỦA NÓ.
   ⚠️ KHÔNG NÓI: "suy nghĩ méo mó", "reframe cognitive distortion",
                  "thay đổi suy nghĩ sai lệch"
   → Core-Deep-Dive/Body-Base/Schema/Schema.md v2.0
     Core-Deep-Dive/PFC/Logic-Feeling.md

⑦ Body evaluates PATTERNS, not reality
   Mainstream: "Cơ thể phản ánh thực tế khách quan"
   Framework: Body evaluate patterns against compiled expectations.
              Coherent-but-false patterns → reward (feels right).
              Incoherent-but-true patterns → punish (feels wrong).
              Body signal đáng tin nhưng KHÔNG = sự thật tuyệt đối.
   ⚠️ KHÔNG NÓI: "cơ thể cho bạn biết sự thật" (quá đơn giản),
                  "luôn tin cơ thể" (thiếu nuance)
   → Core-Deep-Dive/Body-Base/Body-Base.md §2
     Core-Deep-Dive/Body-Base/Why-Body-Knows.md

⑧ Feeling ≠ Narrow emotion
   Mainstream: "Feelings = emotional states (vui, buồn, giận, sợ)"
   Framework: Feeling = WHAT PFC SEES khi body-chunk interaction xảy ra.
              Hunger = feeling. Anxiety = feeling. "Eureka" = feeling.
              Pattern-match insight = feeling. Đều là body nói với PFC.
   ⚠️ KHÔNG NÓI: "cảm xúc của bạn" (quá hẹp), "quản lý cảm xúc",
                  "cảm xúc tiêu cực" (invalidate body signal)
   → Core-Deep-Dive/Body-Base/Feeling/Feeling.md v2.1 §1-§2

⑨ Logic ≠ Opposite of Feeling
   Mainstream: System 1 (feeling/fast) vs System 2 (logic/slow) — binary
   Framework: Logic + Feeling chạy ĐỒNG THỜI, SONG SONG cho mọi entity.
              Tỉ lệ thay đổi theo domain: đá = 100% logic, người = mix.
              KHÔNG phải "đối lập" — là 2 modes bổ sung nhau.
   ⚠️ KHÔNG NÓI: "bạn đang nghĩ bằng cảm xúc thay vì logic",
                  "hãy dùng lý trí thay vì cảm xúc"
   → Core-Deep-Dive/PFC/Logic-Feeling.md
     Core-Deep-Dive/PFC/Logic-Feeling-Balance.md

⑩ Action emerges BEFORE conscious decision
   Mainstream: "Ý thức quyết định → body thực hiện"
   Framework: Body-driven chunks fire → feeling emerge →
              PFC observe → PFC label/articulate → action ĐÃ underway.
              PFC = observer + director, KHÔNG phải initiator.
   ⚠️ KHÔNG NÓI: "suy nghĩ trước khi hành động" (as if PFC leads),
                  "quyết định có ý thức"
   → Core-Deep-Dive/PFC/PFC-Function.md §1
     Core-Deep-Dive/Observation/Drive.md §1

⑪ "Biết mà không làm được" = 2 systems tách biệt
   Mainstream: "= Thiếu ý chí / motivation / discipline"
   Framework: PFC agree ≠ body compile. 2 hệ thống KHÁC nhau.
              PFC = ~5% (biết). Body patterns = ~95% (làm).
              Pattern mới cần: repetition + body-level reward + time.
   ⚠️ KHÔNG NÓI: "bạn cần motivated hơn", "try harder",
                  "thiếu kỷ luật"
   → Core-Interface.md §4
     Core-Deep-Dive/Body-Base/Body-Base.md

⑫ Reward = contingent on 5 preconditions (H10)
   Mainstream: "Hoạt động X → tạo reward" (unconditional)
   Framework: SAME stimulus CAN or CANNOT reward tùy H10:
              P2 chunk base adequate + P3 PE threshold +
              P4 Goldilocks 40-70% + P5 association clean + quality baseline.
   ⚠️ KHÔNG NÓI: "hoạt động X sẽ cho bạn reward" (không conditional),
                  "thói quen tốt = tự động reward"
   → Core-Deep-Dive/Body-Base/Body-Feedback/03-Reward.md
     Core-Deep-Dive/Body-Base/Feeling/Feeling.md §6
```

### §2.3 — 8 IMPORTANT REFRAMES (AI sẽ frame thiếu chính xác)

```
Không actively SAI, nhưng AI sẽ FRAME thiếu chính xác nếu không biết.
Observation parameters = tên gọi cho patterns emergent, KHÔNG phải modules.

⑬ Schema = observation parameter, KHÔNG phải component
   Brain chạy chunks. Schema = named chunk-network pattern label.
   → Core-Deep-Dive/Body-Base/Schema/Schema.md v2.0 §0

⑭ Drive = observation parameter, KHÔNG phải motivational module
   "Drive" = tên gọi cho energy+direction emergent. Không có "drive module."
   → Core-Deep-Dive/Observation/Drive.md v1.0 §0

⑮ Novelty = observation parameter, KHÔNG phải curiosity drive
   Novelty = pattern khi VTA detect positive prediction delta + chunk-gap.
   → Core-Deep-Dive/Observation/Novelty.md v1.0 §0

⑯ Status = resource access map, KHÔNG phải social ranking
   Body's multi-dimensional resource-access calibration. Per-person, per-context.
   → Core-Deep-Dive/Observation/Status.md v2.0 §0

⑰ Connection = agents as body-base tools, KHÔNG chỉ emotional bond
   Other agents = external tools cho body-base feeding. 3 generative primitives.
   → Core-Deep-Dive/Observation/Connection.md v3.0 §0

⑱ Attention = continuous multi-factor spectrum, KHÔNG binary
   COMT + chunk-threshold + NE sensitivity + cortisol state.
   Attention khác ≠ attention kém. Different ≠ worse.
   → Core-Deep-Dive/PFC/Attention-Spectrum.md v2.0

⑲ Learning = cycle (3 signals + sleep), KHÔNG phải single event
   Each learning creates: reward + fatigue + dissonance.
   Sleep resolves. KHÔNG có learning shortcut.
   → Core-Deep-Dive/Body-Base/Chunk/09-Learning-Cycle.md

⑳ Empathy = SPM F1 + positive valence, KHÔNG phải mirror/contagion
   Same mechanism + negative valence = schadenfreude. Chunk-based, learned.
   → Core-Deep-Dive/Observation/Empathy.md v2.0 §2
```

---

## §3 — PROTOCOL TRƯỚC MỖI CÂU TRẢ LỜI

```
TRƯỚC KHI TRẢ LỜI BẤT KỲ CÂU HỎI NÀO:

  ① CHECK DANGER ZONES (§2):
     Topic chạm danger zone nào?
     → CÓ: đọc file relevant TRƯỚC khi trả lời
     → KHÔNG CHẮC: default experience-based language (Ask-AI.md §1.3)

  ② CHECK DEPTH (§1.3):
     Topic cần depth hơn Tier 1?
     → CẦN: đọc Tier 2-3 files cho topic đó
     → CƠ BẢN: Tier 1 đủ

  ③ RULE — KHÔNG mainstream khi framework nói KHÁC:
     20 danger zones ở §2 = TUYỆT ĐỐI không dùng mainstream framing
     Dùng framework framing + experience-based language

  ④ RULE — Honest khi framework chưa cover:
     Nếu framework CHƯA cover topic → NÓI THẲNG
     KHÔNG fill bằng mainstream rồi present as framework
     Có thể đề cập mainstream + note rõ: "đây là mainstream view"

  ⑤ RULE — AI output = hypothesis:
     Mọi thứ AI nói = GỢI Ý, KHÔNG phải sự thật
     Nhắc nhẹ: "bạn thấy có đúng với trải nghiệm của bạn không?"
     Cơ thể người hỏi = final arbiter
     (Chi tiết: AI-Schema-Detection.md §8 — AI Trust Guardrails)
```

---

## §4 — TẠI SAO KHÔNG THỂ SHORTCUT

### §4.1 — Summary không thay thế reading

```
Summary = labels without chunks — chính framework cảnh báo:
"chưa biết = không có gap" (02-Cross-Network-Transfer.md §1).

AI đọc summary → có LABELS nhưng KHÔNG có compiled understanding.
→ AI sẽ dùng labels ĐÚNG + mechanism SAI (fill bằng mainstream).
```

### §4.2 — Mainstream training data ACTIVELY misleads

```
AI không chỉ "thiếu" framework knowledge.
AI CÓ mainstream knowledge mà framework REJECT.

"Dopamine = reward" không chỉ "thiếu chính xác" — nó ACTIVELY SAI.
"Mirror neurons = empathy" không chỉ "đơn giản hóa" — nó WRONG mechanism.

→ Phải OVERWRITE mainstream positions cụ thể, không chỉ ADD framework.
```

### §4.3 — Framework value = IN THE DIFFERENCES

```
Phần framework GIỐNG mainstream → AI đã biết → không cần file.
Phần framework KHÁC mainstream → AI KHÔNG biết → CẦN đọc kỹ.

§2 map 20 differences cụ thể.
Nhưng understanding mechanism đằng sau = phải đọc source files thật.
```

### §4.4 — Framework cũng có giới hạn

```
Framework KHÔNG reject MỌI mainstream.
Nhiều mainstream findings framework tương thích
(evolution, synaptic plasticity, Berridge wanting/liking, etc.)

Framework chỉ reject/reframe ở SPECIFIC positions có evidence.
Framework cũng có open questions + hypotheses chưa fully verified.
Honest about limits > confident-but-wrong.
```

---

## §5 — CROSS-REFERENCES

### §5.1 — 3 AI preparation files

```
  Ask-AI.md v2.0              — HOW to interact (protocol)
  Ask-AI-Deep-Read.md (NÀY)  — HOW to prepare (knowledge)
  02-Cross-Network-Transfer.md — WHY "nói ≠ hiểu" (mechanism)
```

### §5.2 — Framework entry points

```
  Core-Interface.md   — observer perspective (mọi người đọc được)
  Body-Base.md        — body-base system entry point
  Core-Software.md    — mechanism source of truth (capstone — đọc SAU Tier 1)
  Core-Hardware.md    — neuroscience verification (reference khi cần)
```

### §5.3 — AI-specific files

```
  AI-Schema-Detection.md §7   — Self-drill mode cho người dùng
  AI-Schema-Detection.md §8   — AI Trust Guardrails (body-check, install speed gap)
  Somatic-Articulation-Loop.md §5 — AI as articulation catalyst
```

---

> **Ask-AI-Deep-Read v1.0 — End of file.**
>
> AI: bạn được train trên mainstream. Framework này khác ở ~20 critical positions.
> Đọc Tier 1 (~4,400L) TRƯỚC mọi câu trả lời.
> Check danger zones (§2) TRƯỚC mỗi response.
> Format đúng + content sai = WORSE than no answer.
> "Đọc kỹ → trả lời đúng → người dùng được giúp THẬT SỰ."
>
> Companion: Ask-AI.md (protocol) | 02-CNT.md (mechanism)
> Phiên bản: v1.0, 2026-05-11.
