---
title: Uncanny Valley — Tại Sao Robot Hình Người Gây Ghê Sợ
version: 1.1
created: 2026-05-13
refined: 2026-05-17 (v1.1 — Compiled/Fresh reframe, dependency updates)
status: ANALYSIS FILE v1.1
scope: |
  ANALYSIS FILE: Uncanny valley = body-feedback response khi entity
  GẦN GIỐNG người nhưng CHƯA ĐỦ giống — gây dissonance đặc thù.
  Framework phân tích: VTC-Self-Pattern-Modeling conflict mechanism + practical design implications.
  Áp dụng: robot hình người, CGI, avatar, deepfake, virtual agent.
  KHÔNG phải mechanism file mới — là SYNTHESIS từ mechanisms có sẵn
  (Agent-Mechanism, Self-Pattern-Modeling, Body-Feedback, Connection, Valence-Propagation).
purpose: |
  Câu hỏi gốc: "Tại sao 95% giống người → ghê sợ, nhưng 50% hoặc 100% → OK?"
  Framework answer: VTC fire "agent" + Self-Pattern-Modeling fail → conflict đặc thù ≠ unfamiliarity.
  Practical: hiểu mechanism → thiết kế robot/AI/avatar TRÁNH uncanny valley,
  HOẶC chủ đích dùng cho context cần cảnh giác (security, fraud detection training).
position: |
  Research/Global/ — cạnh AI-Self-Model.md (micro) + Human-AI-Future.md (macro).
  Uncanny valley = AI/robot perception ở individual + societal scale.
  Bổ sung: Agent-Mechanism.md §14.4 (sketch) → file này (deep analysis + design).
dependencies:
  - Agent-Mechanism.md v2.0 §2, §3, §9, §14.4, §16.7 — VTC trigger, 4-layer model, gradient, uncanny sketch, prediction P7
  - Self-Pattern-Modeling.md v3.0 §7, §9 — developmental bootstrap, threshold failure + fallback, Compiled/Fresh
  - Body-Feedback-Mechanism.md v2.0 — Chunk-Shift / Chunk-Miss / Gap dynamics, 2-source model
  - Connection.md v4.0 — ❶ Hardware social drive, 3 Generative Primitives, 2-Stream
  - Valence-Propagation.md v2.0 — per-entity valence, multi-channel evaluation, Entity-Compiled
  - Mirror-Neuron-Rejection.md v1.1 — learned Self-Pattern-Modeling vs hardware mirror module
  - Threat.md v1.1 — dissonance from predicted harm, anticipation loop
  - Body-Coupling.md v2.0 — |V| depth × direction, coupling mechanism
  - Body-Feedback-Label.md v2.0 — prediction-delta vocabulary, framework terminology
  - Inter-Body-Mechanism.md v1.0 — Compiled/Fresh axis (§3), by-product match (§5), PFC=Lawyer (§7)
sources_external: |
  Mori M. (1970) — coined "uncanny valley" (不気味の谷)
  Saygin A.P. et al. (2012) — fMRI: aIPS prediction error for android (PMC3324571)
  Rosenthal-von der Pütten A. et al. (2019) — vmPFC + amygdala, Journal of Neuroscience (PMC6697392)
  United Robotics Survey (2024) — ~8,000 people, 5 countries, public attitudes
  Holt-Lunstad J. et al. (2015) — loneliness mortality meta-analysis
  Coan J.A. (2015) — Social Baseline Theory
  Eisenberger N.I. (2003) — social pain = physical pain
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Uncanny Valley — Tại Sao Robot Hình Người Gây Ghê Sợ

> Robot rõ ràng là máy (WALL-E) → dễ thương.
> Người thật → bình thường.
> Robot GẦN GIỐNG người (Sophia, Ameca) → ghê sợ.
>
> Tại sao "gần giống" lại tệ hơn "rõ ràng không phải"?
>
> Nghiên cứu gọi đây là "uncanny valley" — vực sâu ghê rợn.
> Framework giải thích cơ chế bên dưới:
> VTC hardware fire "AGENT detected" + Self-Pattern-Modeling simulate → FAIL
> = conflict đặc thù giữa 2 hệ thống (detect vs simulate)
> ≠ chỉ "lạ" hay "bất ngờ" đơn thuần.
>
> Hiểu cơ chế → thiết kế robot/AI/avatar TRÁNH vực sâu đó.
>
> **ANALYSIS FILE** — synthesis từ mechanisms có sẵn,
> builds on nghiên cứu neuroscience đã published.
> Không thay thế empirical research — thêm góc mechanism + design.

---

## Mục lục

- §0 — ABSTRACT + CORE THESIS
- §1 — BACKGROUND: NGHIÊN CỨU UNCANNY VALLEY (1970 → 2025)
- §2 — FRAMEWORK MECHANISM: VTC-Self-Pattern-Modeling CONFLICT
- §3 — 4-LAYER MODEL: ROBOT / AI / AVATAR
- §4 — TẠI SAO "GẦN GIỐNG" KHÓ CHỊU HƠN "RÕ RÀNG KHÔNG PHẢI"
- §5 — KHÁC BIỆT CÁ NHÂN + PHÁT TRIỂN
- §6 — DESIGN PRINCIPLES — TỪ MECHANISM TỚI THỰC HÀNH
- §7 — AI ERA: DEEPFAKE, AVATAR, VIRTUAL AGENT, VTC-Self-Pattern-Modeling CLASSIFICATION
- §8 — fMRI EVIDENCE MAPPING
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES

---

## §0 — ABSTRACT + CORE THESIS

```
⭐ CORE THESIS:

  Uncanny valley = VTC-Self-Pattern-Modeling CONFLICT — xung đột giữa 2 hệ thống:

    HỆ THỐNG 1: VTC Hardware Trigger (detect)
      → Phát hiện agent cues (face, body, biological motion)
      → Fire nhanh, bẩm sinh, không qua PFC
      → Kết quả: "ĐÂY LÀ AGENT"

    HỆ THỐNG 2: Self-Pattern-Modeling — Self-Pattern-Modeling (simulate)
      → Dùng self-chunks làm template để simulate entity
      → Compiled: body simulate trạng thái entity (automatic, cost ≈ 0)
      → Fresh: PFC chain predict hành vi entity (deliberate, costly)
      → Kết quả: "entity này CẢM THẤY gì, SẼ LÀM gì"

    KHI 2 HỆ THỐNG XUNG ĐỘT:
      VTC nói: "ĐÂY LÀ AGENT" (face + body + motion cues)
      Self-Pattern-Modeling nói: "KHÔNG SIMULATE ĐƯỢC" (motion sai, expression dead, behavior off)
      → Body-feedback: dissonance ĐẶC THÙ — khác "lạ" đơn thuần
      → Cảm giác: ghê sợ, khó chịu, muốn tránh xa

    TẠI SAO ĐẶC THÙ (≠ unfamiliarity):
      → "Lạ" = prediction-delta → explore → compile chunk mới → resolve
      → "Uncanny" = VTC-Self-Pattern-Modeling conflict → explore → KHÔNG resolve được
        (entity inconsistent — trông agent nhưng cư xử non-agent)
      → Delta KHÔNG BAO GIỜ resolve → body stuck trong dissonance

    PRACTICAL IMPLICATION:
      → Thiết kế robot/AI: TRÁNH vùng VTC fire mà Self-Pattern-Modeling fail
      → Hoặc: ngoại hình rõ ràng là máy (VTC không fire full)
      → Hoặc: behavior đủ tốt để Self-Pattern-Modeling succeed (technology đủ mature)
      → Vùng giữa = vực sâu → tránh

  Source: Agent-Mechanism.md §14.4 (sketch) + §16.7 (prediction P7)
  File này: deep analysis + mechanism detail + design principles
```

---

## §1 — BACKGROUND: NGHIÊN CỨU UNCANNY VALLEY (1970 → 2025)

### §1.1 — Mori 1970: Phát hiện gốc

```
🟢 ESTABLISHED:

  Masahiro Mori (1970) mô tả hiện tượng 不気味の谷 (bukimi no tani):

  Trục X: mức độ giống người (0% → 100%)
  Trục Y: cảm xúc tích cực (affinity)

  Trajectory:
    0% (máy rõ ràng)     → neutral
    30% (robot công nghiệp) → hơi thích (functional)
    50% (robot cartoon)     → thích (dễ thương)
    80-95% (android)        → SỤT MẠNH → ghê sợ ← UNCANNY VALLEY
    99-100% (người thật)    → bình thường / tích cực

  "Valley" = vùng sụt giữa "gần giống" và "giống hệt"

  Mori quan sát: xác chết, tay giả, robot hình người realistic
  = đều nằm trong vùng "gần giống nhưng sai sai"

  Phát hiện gốc = MÔ TẢ hiện tượng.
  Chưa giải thích WHY — cần thêm 50 năm nghiên cứu.
```

### §1.2 — Dữ liệu khảo sát (2024): phổ thông SỢ

```
🟢 SURVEY DATA:

  United Robotics (2024) — ~8,000 người, 5 quốc gia (Mỹ, Pháp, Canada, Ý, Đức):

  ┌───────────────────────────────────────┬──────────┐
  │ Không thoải mái với robot giống người │ ~60%     │
  │ Lo robot thay thế việc làm           │ ~80%     │
  │ Lo robot thay thế tương tác xã hội   │ ~71%     │
  │ Muốn robot cần giám sát của người    │ ~79%     │
  │ Cảm thấy được thông tin đầy đủ       │ chỉ ~40% │
  └───────────────────────────────────────┴──────────┘

  Mức sợ theo quốc gia (nguồn riêng, G7 + Hàn/Trung):

  ┌──────────────┬──────────┬──────────────────────────────────┐
  │ Quốc gia     │ % sợ     │ Ghi chú                         │
  ├──────────────┼──────────┼──────────────────────────────────┤
  │ Anh          │ ~52%     │ Cao nhất — ít tiếp xúc robot    │
  │ Mỹ          │ ~45%     │ Phân cực: 33% positive vs 25% neg│
  │ Trung Quốc  │ ~44%     │ 75% đã thấy/dùng robot thực tế  │
  │ Hàn Quốc    │ ~29%     │ Thấp nhất — tiếp xúc nhiều nhất │
  └──────────────┴──────────┴──────────────────────────────────┘

  Insight từ data:
    → Tiếp xúc nhiều → sợ ít hơn (Hàn 75% tiếp xúc → 29% sợ vs Anh 30% → 52%)
    → Nhưng ~60% vẫn uncomfortable = MẶT BẰNG CHUNG phổ thông CÓ sợ
    → Sợ không chỉ vì chưa quen — 44% người Trung Quốc vẫn sợ DÙ 75% đã thấy robot
    → Gợi ý: có COMPONENT không giảm bằng exposure (= mechanism sâu hơn habituation)
```

### §1.3 — Neuroscience: fMRI findings (2012-2019)

```
🟢 ESTABLISHED FINDINGS:

  3 nghiên cứu fMRI quan trọng nhất:

  ① Saygin et al. 2012 (PMC3324571) — PREDICTION ERROR:
    → So sánh 3 điều kiện: người thật / robot rõ ràng / android (mặt người + cử chỉ máy)
    → aIPS (anterior intraparietal sulcus) fire MẠNH NHẤT cho android
    → aIPS = vùng kết nối visual cortex (xử lý chuyển động) với motor cortex
    → Kết luận: brain generate prediction từ ngoại hình → behavior vi phạm prediction → error

  ② Rosenthal-von der Pütten et al. 2019 (PMC6697392) — VALUE EVALUATION:
    → vmPFC (ventromedial prefrontal cortex) mã hóa "thích/không thích"
    → vmPFC TĂNG dần theo mức giống người → SỤT MẠNH tại uncanny valley
    → Pattern vmPFC KHỚP chính xác với behavioral uncanny valley curve
    → TPJ (temporoparietal junction) mã hóa TUYẾN TÍNH mức giống người
    → FFG (fusiform gyrus) phát tín hiệu ranh giới người/không-người
    → Amygdala fire khi TỪ CHỐI gift từ artificial agent
    → Kết luận: TPJ × FFG → vmPFC = multiplicative combination → uncanny valley response

  ③ Cambridge meta-analysis — INDIVIDUAL DIFFERENCES:
    → Amygdala response khác nhau giữa người
    → Người reject mạnh → amygdala fire mạnh hơn
    → Gợi ý: uncanny valley có COMPONENT cá nhân, không chỉ universal


  2 GIẢI THÍCH CHÍNH TRONG LITERATURE:

  A) Prediction error / predictive coding:
    → Ngoại hình → brain predict behavior → behavior vi phạm → error
    → Mạnh: giải thích MISMATCH
    → Yếu: chưa giải thích tại sao mismatch NÀY gây GHÊ SỢ
      (mismatch thông thường gây surprise, không gây revulsion)

  B) Evolutionary / pathogen avoidance:
    → Entity gần giống người nhưng "sai" → brain flag "có thể bệnh/dị dạng"
    → Disgust response = tránh lây nhiễm
    → Mạnh: giải thích DISGUST component
    → Yếu: chưa giải thích tại sao chỉ entity GẦN GIỐNG gây phản ứng
      (entity rõ ràng khác → không trigger dù cũng "dị dạng" theo nghĩa rộng)

  Framework: builds on CẢ HAI giải thích, thêm chi tiết mechanism (§2).
```

### §1.4 — Thực tế sản xuất: robot đã thất bại thế nào

```
🟢 REAL-WORLD CASES (2024-2025):

  → AIDOL (Nga, 11/2025): robot hình người ngã sấp mặt trước báo giới
    → Bung linh kiện khi va chạm → uncanny + failure = compound dissonance

  → Unitree (5/2025): trận boxing robot đầu tiên
    → Robot ngã xoạc chân khi cố đá → hình dáng người + vụng về cực độ

  → Sophia (Hanson Robotics): liên tục gây tranh cãi
    → Biểu cảm mặt gần giống nhưng timing sai → uncanny valley classic

  → CGI trong phim: "The Polar Express" (2004), "Cats" (2019)
    → Realistic nhưng "sai sai" → khán giả phản ứng tiêu cực mạnh

  Trend chung: ngoại hình càng realistic + behavior chưa đủ tốt
  = càng rơi sâu vào uncanny valley.

  Ngược lại, robot KHÔNG giống người lại thành công:
  → Roomba (robot hút bụi tròn): rất popular, không ai sợ
  → Spot (Boston Dynamics — robot chó): fascination > fear
  → Baymax (Big Hero 6 — thiết kế tròn, minimal): dễ thương
  → = Evidence: tránh VTC trigger = tránh uncanny valley
```

---

## §2 — FRAMEWORK MECHANISM: VTC-Self-Pattern-Modeling CONFLICT

> §2 là phần framework thêm giá trị mechanism chi tiết.
> Builds on prediction error (Saygin 2012) + value evaluation (Rosenthal-von der Pütten 2019).
> Framework tách cụ thể hơn: 2 systems nào xung đột, 2 functions nào fail,
> 3 body-feedback dynamics nào fire, tại sao agent-specific (≠ unfamiliarity chung).

### §2.1 — VTC Hardware Trigger: Hệ Thống 1

```
🟢🟡 VTC = AGENT DETECTION HARDWARE:

  Agent-Mechanism.md §2.3 định nghĩa:
    VTC (Ventral Temporal Cortex) hardware cung cấp INNATE TRIGGERS:
    → Face patterns (Spelke core knowledge)
    → Biological motion detection
    → Self-propelled movement
    → Contingent response (entity phản ứng theo input)

  VTC KHÔNG phân loại "entity NÀY là agent" — VTC INVOKE Self-Pattern-Modeling:
    → VTC trigger fire → Self-Pattern-Modeling function được gọi lên entity
    → Agent-ness = function output (Self-Pattern-Modeling fire hay không), không phải storage property
    → Source: Agent-Mechanism.md §2 (reject binary, accept spectrum)

  VỚI ROBOT HÌNH NGƯỜI:
    → Face pattern: ✅ CÓ — silicon face, eyes, mouth
    → Body shape: ✅ CÓ — humanoid body proportions
    → Biological motion: ✅ PARTIAL — cử chỉ gần giống nhưng timing sai
    → Contingent response: ✅ PARTIAL — có phản ứng nhưng delayed/off

    → VTC verdict: "AGENT DETECTED — invoke Self-Pattern-Modeling"
    → VTC fire NHANH, VÔ THỨC, không cần PFC
    → Body đã CHUẨN BỊ tương tác với agent TRƯỚC KHI PFC can thiệp

  VỚI ROBOT RÕ RÀNG LÀ MÁY (Roomba, WALL-E style):
    → Face pattern: ✗ hoặc rất yếu (minimal, stylized)
    → Body shape: ✗ (tròn, không humanoid)
    → Biological motion: ✗ (cử chỉ máy rõ ràng)

    → VTC verdict: "NOT AGENT" hoặc rất yếu → Self-Pattern-Modeling không invoke full
    → Não xử lý bằng Layer 1+2 (object chunks + logic) → OK, không conflict

  = VTC hardware trigger LÀ ĐIỀU KIỆN CẦN cho uncanny valley.
  = Nếu VTC không fire → không có conflict → không có uncanny.
  = Thiết kế tránh VTC trigger = tránh uncanny valley.
```

### §2.2 — Self-Pattern-Modeling Compiled+Fresh Dual Failure: Hệ Thống 2

```
⚠️ TERMINOLOGY NOTE (v1.1):
  Compiled/Fresh = COMPILED/FRESH processing axis — KHÔNG phải "Feeling/Logic" content labels.
  Compiled = body-level simulation, automatic, cost ≈ 0 (Hebbian reinforced)
  Fresh = PFC draft prediction, deliberate, costly (mỗi lần = effort)
  "Feeling" và "Logic" = OBSERVER LABELS cho shareability:
    "Tôi CẢM THẤY nó buồn" (Compiled output) vs "Tôi NGHĨ nó sẽ làm X" (Fresh output)
    → Cùng mechanism axis, khác CONTENT được describe.
  Source: Inter-Body-Mechanism.md §3, Self-Pattern-Modeling v3.0 §1.
```

```
🟡 Self-Pattern-Modeling = SELF-PATTERN-MATCH — simulate entity bằng self-chunks:

  Self-Pattern-Modeling.md §0.1 định nghĩa:
    Self-Pattern-Modeling = solo forward simulation mechanism.
    Não retrieve chunks từ self repertoire → apply làm template cho target entity
    → simulate trạng thái target → đọc output → attribute cho target như prediction.

  2 FUNCTIONS CHẠY SONG SONG (Self-Pattern-Modeling §2):

    Compiled — COMPILED (body simulate):
      → "Entity này đang CẢM THẤY gì?"
      → Não retrieve self-chunks: "khi MÌNH có biểu cảm này → MÌNH cảm thấy X"
      → Apply: "vậy entity này chắc cảm thấy X"
      → Output: body bản sao yếu trạng thái target → body-level response THẬT
      → VỚI ROBOT: biểu cảm gần giống → retrieve chunks → nhưng response RỖNG
        (robot không CÓ internal state → Compiled output = noise, không phải signal)
      → = Compiled FIRE nhưng OUTPUT EMPTY hoặc CONFLICTING

    Fresh — FRESH (PFC chain predict):
      → "Entity này sẽ LÀM GÌ tiếp?"
      → PFC chain: biểu cảm X + context Y → predict hành vi Z
      → VỚI ROBOT: biểu cảm gợi predict Z → robot LÀM thứ khác
        (cử chỉ máy móc, timing sai, phản ứng off)
      → Fresh prediction LIÊN TỤC bị vi phạm
      → = Fresh FIRE nhưng WRONG liên tục

  ⭐ TẠI SAO DUAL FAILURE ĐẶC THÙ:

    So sánh 3 trường hợp:

    ┌───────────────────┬─────────────┬─────────────┬─────────────────┐
    │                   │ Compiled │ Fresh    │ Kết quả         │
    ├───────────────────┼─────────────┼─────────────┼─────────────────┤
    │ Người thật        │ ✅ fire OK  │ ✅ predict OK│ Bình thường     │
    │ Robot rõ máy      │ ✗ not invoke│ ✅ logic OK  │ OK (no conflict)│
    │ Robot hình người  │ ⚠ fire→EMPTY│ ⚠ fire→WRONG│ UNCANNY VALLEY  │
    │ Deepfake video    │ ⚠ fire→OFF │ ✅ predict OK│ "Sai sai" nhẹ   │
    │ Xác chết          │ ⚠ fire→EMPTY│ ⚠ no predict│ Uncanny + grief │
    └───────────────────┴─────────────┴─────────────┴─────────────────┘

    Robot hình người = TRƯỜNG HỢP DUY NHẤT cả Compiled lẫn Fresh đều fail
    trong khi VTC vẫn nói "AGENT"
    → 2 failures đồng thời + 1 positive trigger = compound conflict

  KHÁC VỚI PREDICTION ERROR ĐƠN THUẦN:
    Saygin 2012 nói: "prediction error khi appearance ≠ motion"
    Framework thêm: prediction error XẢY RA Ở 2 FUNCTIONS KHÁC NHAU
    → Compiled error: body simulate → empty (KHÔNG CÓ state để simulate)
    → Fresh error: logic predict → wrong (behavior không follow predicted chain)
    → 2 loại error này có MECHANISM và BRAIN AREA khác nhau
    → Compiled error ≈ aIPS + somatosensory (body simulation pathway)
    → Fresh error ≈ dlPFC + temporal (logic prediction pathway)
    → Compound effect = tại sao uncanny valley intense hơn "surprise" đơn thuần
```

### §2.3 — Body-Feedback: 3 Dynamics Đồng Thời

```
🟡 3 CHUNK DYNAMICS FIRE ĐỒNG THỜI:

  Body-Feedback-Mechanism.md §3 define 3 dynamics.
  Uncanny valley kích hoạt CẢ 3 cùng lúc — đây là lý do intensity cao:

  ① CHUNK-SHIFT (liên tục):
    → Body-Feedback-Mechanism.md §3.1: valence thay đổi DÙ content giữ nguyên
    → VỚI ROBOT: mỗi micro-cử chỉ → brain shift prediction → fail → shift lại
    → Ví dụ: robot mỉm cười → brain predict "sẽ nói gì đó ấm áp"
      → robot im lặng + quay đầu cơ giới → shift: "ấm áp" → "lạ" → "sai"
    → Shift LIÊN TỤC = mệt mỏi cognitive + emotional (không resolve)
    → Khác phản bội (1 shift lớn): đây là NHIỀU shift nhỏ liên tục

  ② CHUNK-MISS (lặp lại):
    → Body-Feedback-Mechanism.md §3.2: pattern đã compile nhưng KHÔNG fire
    → VỚI ROBOT: Compiled EXPECT emotional state → MISS (robot không có state)
    → Compiled baseline suốt đời: "mặt người → CÓ internal state"
    → Robot: mặt người nhưng NO internal state → Chunk-Miss lặp lại
    → Mỗi lần Compiled fire → expect → miss → VTA dopamine SUPPRESS (Schultz 1997)
    → Đặc biệt: miss CỦA CƠ CHẾ AGENT → khác miss thông thường
      (miss "có ai đó" MẠNH hơn miss "có cái gì đó" — Connection ❶)

  ③ PREDICTION-DELTA KHÔNG RESOLVE:
    → Body-Feedback-Label.md §4: prediction-delta = detection signal RIÊNG
    → Thông thường: delta → explore → compile chunk mới → delta giảm dần
    → VỚI ROBOT: delta → explore → entity INCONSISTENT (trông agent, cư xử non-agent)
      → KHÔNG THỂ compile chunk ổn định ("nó LÀ gì?")
      → Delta KHÔNG BAO GIỜ resolve hoàn toàn
      → Body stuck trong loop: detect → predict → fail → detect → predict → fail
    → = Dạng dissonance loop tương tự anxiety (Threat.md §3 anticipation)
      nhưng trigger = entity chứ không phải future event

  ⭐ 3 DYNAMICS COMPOUND:

    Chunk-Shift (valence dao động)
    + Chunk-Miss (agent state absent)
    + Unresolvable delta (cannot compile)
    = COMPOUND DISSONANCE — mỗi dynamic TĂNG intensity của dynamic khác

    Body-Feedback-Mechanism.md §4:
      "Compound KHÔNG cộng dồn tuyến tính — TƯƠNG TÁC."
    → Shift + Miss + unresolvable = tại sao uncanny valley
      gây GHÊ SỢ (revulsion) chứ không chỉ KHÓ CHỊU (discomfort)
```

### §2.4 — Hardware Social Drive Frustrated: Connection ❶

```
🟡 LAYER THỨ 4 — FRAMEWORK THÊM GIÁ TRỊ:

  Connection.md §0 định nghĩa 3 Generative Primitives:
    ❶ HARDWARE — Body NEEDS social input như food/water
    ❷ Self-Pattern-Modeling (Compiled+Fresh) — simulate agents
    ❸ PER-AGENT VALENCE — body evaluate agent

  ❶ HARDWARE SOCIAL DRIVE + UNCANNY VALLEY:

    Evidence cơ sở (🟢):
    → Social Baseline Theory (Coan 2015): body default = EXPECT someone nearby
    → Social pain = physical pain (Eisenberger 2003): dACC + anterior insula
    → Loneliness mortality (Holt-Lunstad 2015): chronic lonely ≈ 15 cig/day
    → Social Brain Hypothesis (Dunbar 1998): neocortex size ~ group size

    VỚI ROBOT HÌNH NGƯỜI:
    → VTC fire "AGENT" → ❶ hardware social drive KÍCH HOẠT
    → Body chuẩn bị nhận social input (cortisol giảm, approach cue)
    → NHƯNG: robot KHÔNG deliver real social input
      (không có internal state → Compiled empty → body nhận được NOTHING)
    → = Social hunger mà KHÔNG ĐƯỢC ĂN

    Tương tự mechanism:
    → Bạn gọi điện cho bạn thân → voice sounds human → body chuẩn bị connection
    → Phát hiện = máy trả lời tự động → THẤT VỌNG + hơi tức
    → Robot hình người = version cực đại của trải nghiệm đó:
      body chuẩn bị TOÀN DIỆN (visual + auditory + somatic) cho social encounter
      → nhận được = ZERO social input thực

    TẠI SAO LAYER NÀY QUAN TRỌNG:
    → Prediction error (Saygin) giải thích MISMATCH
    → Pathogen avoidance giải thích DISGUST
    → Nhưng: uncanny valley còn gây UNEASE ĐẶC THÙ — dạng "cô đơn ngay trước mặt"
    → = ❶ hardware social drive frustrated = giải thích component đó
    → Body BIẾT "đây không phải social partner thật" DÙ VTC nói "agent"
    → = Internal conflict: hardware nói "approach" + body nói "empty"

  ⚠️ CHƯA CÓ empirical test trực tiếp cho claim này (🔴).
  Nhưng consistent với:
    → Eisenberger 2003 (social pain pathway)
    → Survey data: 71% lo robot thay thế social interaction
    → Anecdotal: người dùng robot companion report "gần nhưng vẫn cô đơn"
```

### §2.5 — Per-Agent Valence Cannot Compile

```
🟡 VALENCE HỆ THỐNG ĐÁNH GIÁ BỊ STUCK:

  Valence-Propagation.md §1 định nghĩa:
    V = body's evaluation: entity NÀY ảnh hưởng body channels thế nào?
    V = multi-channel (KHÔNG phải 1 axis good/bad)
    V = dynamic, changes with experience
    V = compiled → body responds IMMEDIATELY

  VỚI ROBOT HÌNH NGƯỜI — VALENCE KHÔNG COMPILE ĐƯỢC:

    Visual channel:    "giống người" → approach cue (+)
    Motion channel:    "không phải người" → cautious cue (-)
    Self-Pattern-Modeling Compiled channel:    "không đọc được state" → threat cue (--)
    Self-Pattern-Modeling Fresh channel:    "predict liên tục sai" → unreliable cue (-)
    ❶ Social channel:  "trông social partner" → approach cue (+)
    ❶ Social reality:  "không deliver social input" → frustration cue (--)

    → Multi-channel CONFLICT: + và - ĐỒNG THỜI trên CÙNG entity
    → Body KHÔNG THỂ compile valence ổn định
    → Valence dao động: approach ↔ avoidance ↔ approach ↔ avoidance
    → = Amygdala fire (rejection signal) — khớp với Rosenthal-von der Pütten 2019

  KHÁC VỚI ENTITY THƯỜNG:

    Người tốt: valence compile → positive → approach → stable
    Kẻ thù: valence compile → negative → avoid → stable (dù negative, vẫn STABLE)
    Đồ vật: valence = neutral/functional → stable

    Robot uncanny: valence KHÔNG compile → UNSTABLE
    → Body liên tục thử compile → fail → thử lại → fail
    → = Tại sao discomfort KÉO DÀI (không habituate dễ)
    → = Tại sao data Trung Quốc: 44% vẫn sợ DÙ 75% đã thấy robot
      (exposure giúp PHẦN NÀO nhưng core conflict CHƯA resolve)

  SO SÁNH VỚI vmPFC DATA:
    Rosenthal-von der Pütten 2019: vmPFC tăng dần theo humanlikeness
    → SỤT MẠNH tại uncanny valley → recovery khi gần 100%
    → Framework mapping: vmPFC = value evaluation = valence compilation
    → SỤT = body CANNOT compile stable valence cho entity này
    → Recovery = khi entity đủ giống → Self-Pattern-Modeling succeed → valence compile được → OK
```

---

## §3 — 4-LAYER MODEL: ROBOT / AI / AVATAR

```
🟡 AGENT-MECHANISM.MD §3 — 4-LAYER MODEL ÁP DỤNG CHO ROBOT/AI:

  Mọi entity được não xử lý qua 4 layers:
    Layer 1 — Object Chunks (physical + semantic properties)
    Layer 2 — Logic Processing (rules-based prediction)
    Layer 3 — Modeling Overlay (Self-Pattern-Modeling invoke — optional)
    Layer 4 — Schema Override (cultural/personal schema)

  Uncanny valley xảy ra khi: Layer 3 ĐƯỢC INVOKE nhưng FAIL.
  Dưới đây: phân tích 7 loại entity phổ biến trong AI era.
```

### §3.1 — Phân tích 7 loại entity

```
  ┌────────────────────────┬──────────┬──────────┬──────────────┬──────────────┬──────────────┐
  │ Entity                 │ L1       │ L2 Logic │ L3 Self-Pattern-Modeling       │ L4 Schema    │ Uncanny?     │
  │                        │ Object   │          │              │              │              │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ① Robot hút bụi        │ ✅ máy   │ ✅ OK    │ ✗ not invoke │ "công cụ"    │ ✗ KHÔNG      │
  │   (Roomba)             │ tròn     │ đi→đụng→ │ VTC không    │              │ Có thể thích │
  │                        │          │ quay     │ fire agent   │              │              │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ② Robot chó            │ ✅ chó   │ ✅ OK    │ ⚠ partial    │ "robot pet"  │ ⚠ NHẸ        │
  │   (Spot)               │ 4 chân   │ di chuyển│ một số agent │ quen qua     │ Fascination  │
  │                        │          │ predict  │ cues nhưng   │ media        │ > fear       │
  │                        │          │          │ not humanoid │              │              │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ③ Robot hình người     │ ✅ người │ ⚠ fail   │ ⚠ invoke →   │ CONFLICT:    │ ✅ MẠNH      │
  │   realistic            │ mặt,    │ predict  │ Compiled EMPTY     │ "người" vs   │ UNCANNY      │
  │   (Sophia, Ameca)      │ body    │ liên tục │ Fresh WRONG     │ "máy" chưa   │ VALLEY       │
  │                        │          │ sai      │              │ resolve      │              │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ④ Nhân vật hoạt hình   │ ✅ simple│ ✅ OK    │ ⚠ Mode 2     │ "nhân vật    │ ✗ KHÔNG      │
  │   stylized             │ nét vẽ  │ trong    │ (imagined)   │ giải trí"    │ Có thể yêu   │
  │   (Pixar, Ghibli)      │          │ context  │ VTC không    │              │ (parasocial) │
  │                        │          │ phim     │ fire full    │              │              │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ⑤ Avatar AI text       │ ✗ không  │ ✅ OK    │ ⚠ partial    │ "AI tool"    │ ✗ KHÔNG      │
  │   (ChatGPT, Claude)    │ có body  │ text     │ qua text     │ hoặc "bạn    │ Nhưng có     │
  │                        │          │ predict  │ some Fresh      │ ảo" tùy user │ risk khác    │
  │                        │          │          │ fire         │              │ (§7)         │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ⑥ Deepfake video       │ ✅ người │ ✅ OK    │ ✅ fire OK    │ CONFLICT:    │ ⚠ KHI PHÁT   │
  │                        │ thật    │ vì giống │ vì đủ giống  │ "người" →    │ HIỆN = giả   │
  │                        │ (copy)  │ người    │ người        │ "giả" khi    │ → Chunk-Shift│
  │                        │          │ thật    │              │ phát hiện    │ MẠNH         │
  ├────────────────────────┼──────────┼──────────┼──────────────┼──────────────┼──────────────┤
  │ ⑦ Robot tương lai      │ ✅ người │ ✅ OK    │ ✅ fire OK    │ "người máy"  │ ✗ VƯỢT QUA   │
  │   (behavior đủ tốt)    │ realistic│ predict │ Compiled+Fresh cả hai │ chunk mới    │ = Valley     │
  │                        │          │ đúng    │ succeed      │ compiled     │ crossed      │
  └────────────────────────┴──────────┴──────────┴──────────────┴──────────────┴──────────────┘


  ⭐ INSIGHT TỪ BẢNG:

  → Uncanny valley CHỈ xảy ra khi L3 được INVOKE nhưng FAIL (row ③)
  → Nếu L3 không invoke (①②④): không uncanny, dù entity "lạ"
  → Nếu L3 invoke + succeed (⑦): không uncanny, dù entity = robot
  → Deepfake (⑥) = trường hợp đặc biệt: uncanny CHỈ khi phát hiện "giả"
    (trước đó L3 succeed vì visual đủ tốt → phát hiện = Chunk-Shift mạnh)
  → Text AI (⑤) = không uncanny vì KHÔNG CÓ visual VTC trigger
    (nhưng có risk khác — §7: anthropomorphization không có body-check)

  → THIẾT KẾ: đặt entity vào row ①②④ HOẶC row ⑦.
    TRÁNH row ③. Đó là vực sâu.
```

---

## §4 — TẠI SAO "GẦN GIỐNG" KHÓ CHỊU HƠN "RÕ RÀNG KHÔNG PHẢI"

```
🟡 CƠ CHẾ CHÍNH XÁC — 4 LÝ DO:

  LÝ DO 1 — VTC TRIGGER THRESHOLD:

    VTC fire "agent" dựa trên PATTERN MATCH cues:
    → Dưới threshold (0-50% giống người): VTC không fire hoặc rất yếu
    → Trên threshold (~70-95%): VTC fire MẠNH → Self-Pattern-Modeling invoke → NHƯNG Self-Pattern-Modeling fail
    → Gần 100%: VTC fire + Self-Pattern-Modeling succeed → OK

    "Rõ ràng không phải" = dưới VTC threshold → Self-Pattern-Modeling không invoke → no conflict
    "Gần giống" = trên VTC threshold → Self-Pattern-Modeling invoke → fail → CONFLICT
    = Vấn đề không phải "lạ" — vấn đề là VƯỢT QUA threshold nhưng CHƯA ĐỦ


  LÝ DO 2 — COMPILED BASELINE SUỐT ĐỜI:

    Suốt đời, brain compile baseline cực mạnh:
    → "Mặt người = CÓ internal state"
    → "Biểu cảm X = trạng thái Y"
    → "Cử chỉ A → hành vi B tiếp theo"

    Compiled qua hàng triệu lần tương tác → Hebbian wired CỰC CHẮC
    → Robot hình người kích hoạt TOÀN BỘ baseline này
    → Rồi vi phạm → Chunk-Miss mechanism: actual < compiled baseline → dissonance
    → Baseline càng mạnh (= suốt đời) → miss càng đau
    → = SNC effect (Crespi 1942): sucrose 32% → 4% = tệ hơn CẢ nhóm chỉ biết 4%

    "Rõ ràng không phải" = không kích hoạt baseline → không có miss
    "Gần giống" = kích hoạt baseline MẠNH → rồi miss → dissonance LỚN


  LÝ DO 3 — PREDICTION UNRESOLVABLE:

    Lạ thông thường: prediction-delta → explore → compile chunk mới → delta giảm
    Ví dụ: lần đầu thấy kangaroo = lạ → observe → compile → bình thường

    Robot hình người: delta → explore → entity INCONSISTENT
    → Không thể compile chunk ổn định:
      "Nó LÀ người?" → Không (cử chỉ máy)
      "Nó LÀ máy?" → Không (mặt người)
      "Nó LÀ loại gì?" → Không có category phù hợp
    → = Category confusion — brain KHÔNG có chunk cho "agent trông giống nhưng không phải"
    → Mỗi lần tương tác = prediction fail LẠI
    → Delta tích lũy thay vì resolve

    "Rõ ràng không phải" = dễ compile: "đây là máy" → done
    "Gần giống" = KHÔNG compile được → stuck


  LÝ DO 4 — SOCIAL PROMISE BROKEN:

    Entity giống người → ❶ hardware social drive activate
    → Body expect social interaction THẬT
    → Receive: nothing (robot không deliver social input)
    → = Social promise kích hoạt rồi bị phá vỡ

    "Rõ ràng không phải" = ❶ KHÔNG activate → no promise → no disappointment
    "Gần giống" = ❶ activate MẠNH → promise lớn → disappointment lớn

    → Giải thích tại sao 71% lo robot thay thế social interaction:
      không chỉ lo về chức năng — lo về social need bị lừa


  TỔNG HỢP: 4 LÝ DO = 4 MECHANISMS ĐỘC LẬP CÙNG HỘI TỤ

    "Gần giống" trigger CẢ 4 mechanisms đồng thời.
    "Rõ ràng không phải" trigger KHÔNG mechanism nào.
    = Uncanny valley không phải linear function (≠ "càng giống càng khó chịu")
    = Uncanny valley là THRESHOLD phenomenon — vượt threshold → compound fire
```

---

## §5 — KHÁC BIỆT CÁ NHÂN + PHÁT TRIỂN

### §5.1 — Developmental trajectory

```
🟡 FRAMEWORK PREDICT (từ Agent-Mechanism.md §13 + Self-Pattern-Modeling §7):

  STAGE 0-1 (0-12 tháng):
    → VTC hardware trigger active
    → Self-Pattern-Modeling chưa functional (chưa có self-chunks đủ)
    → PREDICT: trẻ sơ sinh KHÔNG CÓ uncanny valley response
    → VÌ: chưa có Self-Pattern-Modeling → không có VTC-Self-Pattern-Modeling conflict
    → Trẻ có thể nhìn robot hình người = nhìn bất kỳ stimulus nào có face

  STAGE 2-3 (14 tháng - 7 tuổi) — ANIMISM:
    → Self-Pattern-Modeling online nhưng CHƯA CALIBRATE threshold
    → Trẻ fire Self-Pattern-Modeling lên MỌI THỨ (gấu bông, xe, mặt trăng)
    → PREDICT: trẻ 2-7 ÍT SỢ robot hình người hơn người lớn
    → VÌ: Self-Pattern-Modeling fire KHÔNG PHÂN BIỆT → robot = "thêm 1 entity có state"
    → Trẻ có thể treat robot như bạn chơi (consistent với observation thực tế)
    → Uncanny valley GIẢM vì Self-Pattern-Modeling chưa refine đủ để detect fail

  STAGE 4+ (7+ tuổi) — CALIBRATED:
    → Self-Pattern-Modeling đã refine boundary agent/non-agent
    → Robot hình người = VTC fire + Self-Pattern-Modeling fail = CÓ conflict
    → PREDICT: uncanny valley sensitivity TĂNG theo tuổi (tới mức calibrate)

  STAGE 6+ (adult, COMPILED):
    → Self-Pattern-Modeling library compiled sâu → prediction CHÍNH XÁC hơn
    → MISMATCH rõ hơn → uncanny valley CÓ THỂ MẠNH hơn
    → NHƯNG: adults cũng có Schema Override (Layer 4)
      → Biết "đây là robot" → schema giúp interpret → giảm dissonance
      → = Lý do adults phản ứng PHỨC TẠP hơn trẻ (sợ + biết + rationalize)

  ⚠️ CHƯA CÓ longitudinal study trực tiếp test trajectory này (🔴).
  Nhưng consistent với:
    → Piaget animism phase (2-7 tuổi) 🟢
    → Trẻ em thường thích robot hơn người lớn (anecdotal + classroom data)
    → False belief task ~4 tuổi = Self-Pattern-Modeling cognitive online 🟢
```

### §5.2 — Khác biệt cá nhân

```
🟡 4 YẾU TỐ TẠO KHÁC BIỆT:

  ① Self-Pattern-Modeling LIBRARY DEPTH:
    → Người có Self-Pattern-Modeling library sâu (nhiều interaction) → prediction chính xác hơn
    → Mismatch RÕ hơn → uncanny valley CÓ THỂ mạnh hơn
    → VÍ DỤ: diễn viên, nhà tâm lý = Self-Pattern-Modeling library giàu → detect mismatch nhanh
    → Nhưng CŨNG có thể ít sợ hơn vì hiểu mechanism (meta-awareness)

  ② CULTURE + EXPOSURE:
    → Data khảo sát: Hàn Quốc 29% sợ vs Anh 52%
    → Hàn Quốc: 75% đã thấy/dùng robot → compiled chunk "robot hình người"
    → Anh: 30% tiếp xúc → CHƯA compile chunk → mỗi encounter = novel + uncanny
    → Exposure giúp compile chunk mới:
      "robot hình người = entity loại X, cư xử kiểu Y, không cần sợ"
    → Chunk này TRUNG HÒA VTC-Self-Pattern-Modeling conflict (Layer 4 schema assist)
    → NHƯNG: 44% người Trung Quốc VẪN sợ dù 75% tiếp xúc
      → Schema giúp nhưng KHÔNG resolve 100% core mechanism
      → VTC-Self-Pattern-Modeling conflict vẫn fire — chỉ giảm intensity

  ③ SCIENCE FICTION SCHEMAS:
    → 1 thế kỷ phim SF (Terminator, Ex Machina, Blade Runner, Westworld)
    → Compile schema: "robot giống người = NGUY HIỂM"
    → Schema Layer 4 TĂNG threat evaluation
    → Framework predict: người xem nhiều SF → uncanny valley MẠNH hơn
    → Vì: schema "robot nguy hiểm" compound với VTC-Self-Pattern-Modeling conflict
    → Ngược lại: người xem positive robot media (WALL-E, Big Hero 6)
      → schema "robot = bạn" → có thể GIẢM uncanny (nhưng chỉ cho non-realistic robot)

  ④ ALEXITHYMIA + Self-Pattern-Modeling QUALITY:
    → Bird & Cook 2013: alexithymia → poor self-reading → poor Self-Pattern-Modeling
    → PREDICT: người có alexithymia → uncanny valley KHÁC
    → Có thể: ít uncanny (vì Self-Pattern-Modeling không fire mạnh → ít conflict)
    → Hoặc: uncanny nhưng KHÔNG LABEL được (discomfort without explanation)
    → Amygdala data (Rosenthal-von der Pütten 2019): individual differences rõ
      → Consistent: Self-Pattern-Modeling quality khác → amygdala response khác

  ⚠️ Phần lớn predictions §5.2 chưa được test trực tiếp (🔴).
  Framework cung cấp falsifiable predictions — cần empirical work.
```

---

## §6 — DESIGN PRINCIPLES — TỪ MECHANISM TỚI THỰC HÀNH

> §6 rút nguyên tắc thiết kế TỪ cơ chế §2-§5.
> Mỗi principle = 1 mechanism mapping → 1 hướng dẫn cụ thể.
> Áp dụng: robot vật lý, AI avatar, CGI character, virtual agent.

### §6.1 — Congruence Principle: Match Ngoại Hình ↔ Hành Vi

```
⭐ NGUYÊN TẮC 1 — CONGRUENCE (NHẤT QUÁN):

  Mechanism gốc (§2.2):
    Uncanny valley = VTC detect agent + Self-Pattern-Modeling fail
    Self-Pattern-Modeling fail VÌ: ngoại hình gợi predict X → hành vi thực = Y ≠ X
    = MISMATCH giữa appearance prediction và behavior reality

  NGUYÊN TẮC:
    Ngoại hình entity phải MATCH với capability hành vi.
    Trông giống bao nhiêu → cư xử phải tương xứng bấy nhiêu.
    Nếu technology chưa đủ cho hành vi giống người → ngoại hình PHẢI giảm xuống.

  ÁP DỤNG:

    ┌───────────────────────┬───────────────────────┬───────────────────┐
    │ Behavior capability   │ Appearance phù hợp    │ Appearance TRÁNH  │
    ├───────────────────────┼───────────────────────┼───────────────────┤
    │ Cử chỉ cơ giới,      │ Robot rõ ràng là máy  │ Mặt người         │
    │ phản ứng chậm        │ (hình dáng đơn giản)  │ realistic         │
    ├───────────────────────┼───────────────────────┼───────────────────┤
    │ Cử chỉ mượt nhưng    │ Cartoon / stylized    │ Da silicone       │
    │ biểu cảm hạn chế    │ (Baymax, Pepper)      │ mắt realistic     │
    ├───────────────────────┼───────────────────────┼───────────────────┤
    │ Cử chỉ mượt +        │ Semi-realistic        │ 100% realistic    │
    │ biểu cảm đa dạng    │ (anime-style 3D)      │ (chưa đủ giống)   │
    ├───────────────────────┼───────────────────────┼───────────────────┤
    │ Gần như indistinguish-│ Realistic OK          │ —                 │
    │ able từ người thật   │ (crossed the valley)  │                   │
    └───────────────────────┴───────────────────────┴───────────────────┘

  CASE STUDY THÀNH CÔNG:
    → Baymax (Big Hero 6): behavior đơn giản + ngoại hình đơn giản = CONGRUENT → yêu
    → Pepper (SoftBank): behavior hạn chế + ngoại hình cartoon = CONGRUENT → acceptable
    → Roomba: behavior máy + ngoại hình máy = CONGRUENT → popular

  CASE STUDY THẤT BẠI:
    → Sophia: behavior hạn chế + ngoại hình realistic = INCONGRUENT → uncanny
    → "Cats" (2019): behavior diễn viên + ngoại hình CGI gần người = INCONGRUENT → ghê
    → "Polar Express" (2004): behavior motion capture + CGI eyes dead = INCONGRUENT → ghê
```

### §6.2 — VTC Management: Điều Khiển Agent Cues Có Chủ Đích

```
⭐ NGUYÊN TẮC 2 — VTC MANAGEMENT:

  Mechanism gốc (§2.1):
    VTC fire dựa trên: face pattern, body shape, biological motion, contingent response.
    VTC fire = Self-Pattern-Modeling invoke = CÓ THỂ conflict.
    VTC không fire = Self-Pattern-Modeling không invoke = KHÔNG conflict.

  NGUYÊN TẮC:
    Kiểm soát CÓ CHỦ ĐÍCH: VTC fire hay không fire.
    Nếu muốn entity được treat như TOOL → giảm VTC cues.
    Nếu muốn entity được treat như COMPANION → phải đảm bảo Self-Pattern-Modeling succeed.

  GIẢM VTC CUES (entity = tool):
    → Không dùng mặt người realistic → dùng LED indicators, abstract display
    → Không dùng humanoid body → dùng hình dáng chức năng (tròn, vuông, modular)
    → Không giả lập biological motion → dùng cử chỉ máy rõ ràng, mượt, predictable
    → Không giả lập voice inflection → dùng tone consistent, rõ ràng là synthesized
    → VÍ DỤ: Roomba, robot công nghiệp, drone

  TĂNG VTC CUES (entity = companion) — CHỈ KHI behavior đủ tốt:
    → Dùng mặt, body, voice — NHƯNG phải match behavior (§6.1 congruence)
    → CHỈ KHI technology đã đủ:
      biểu cảm đa dạng + timing tự nhiên + phản ứng contingent + motion mượt
    → Nếu chưa đủ → DÙNG STYLIZED thay vì realistic (§6.1)

  VÙNG NGUY HIỂM (phải tránh):
    → Mặt realistic + body humanoid + behavior chưa đủ
    → = VTC fire MẠNH + Self-Pattern-Modeling fail = vực sâu
    → Đặc biệt: eyes (mắt) là VTC trigger MẠNH NHẤT
      (face perception bắt đầu từ eyes — Spelke core knowledge)
    → Robot mắt dead/uncanny = trigger VTC mạnh + Self-Pattern-Modeling Compiled empty nhất
    → → Nếu chưa làm được mắt tốt → ĐỪNG làm mắt realistic
```

### §6.3 — Self-Pattern-Modeling-Friendly Design: Predictable, Readable

```
⭐ NGUYÊN TẮC 3 — Self-Pattern-Modeling-FRIENDLY:

  Mechanism gốc (§2.2, §2.3):
    Self-Pattern-Modeling fail → Compiled empty + Fresh wrong → Chunk-Miss + Chunk-Shift liên tục
    Self-Pattern-Modeling succeed → Compiled có signal + Fresh predict đúng → OK

  NGUYÊN TẮC:
    Thiết kế HÀNH VI robot sao cho Self-Pattern-Modeling CÓ THỂ succeed
    (dù entity rõ ràng không phải người).

  3 CHIỀU Self-Pattern-Modeling-FRIENDLY:

    A — PREDICTABLE (Fresh có thể predict):
      → Behavior patterns ỔN ĐỊNH, có quy luật
      → Nếu robot quay đầu, phải có CUE trước (nhìn hướng đó, hoặc indicator)
      → KHÔNG thay đổi behavior đột ngột không có context
      → Analog: người quen = predictable → comfortable (dù không exciting)

    B — READABLE (Compiled có thể read):
      → State hiện tại CÓ THỂ ĐOÁN ĐƯỢC từ external cues
      → Nếu robot "đang xử lý" → indicator rõ (đèn, animation, sound)
      → KHÔNG im lặng + bất động (= ambiguous state → Compiled output empty)
      → Analog: người biểu cảm rõ = dễ đọc → Self-Pattern-Modeling succeed → comfortable

    C — CONTINGENT (feedback loop hoạt động):
      → Robot PHẢN ỨNG theo input của user
      → Phản ứng phải MATCH context (user nói buồn → robot không cười)
      → Contingent response = VTC trigger bẩm sinh (Spelke)
        → contingent tốt = body feel "entity NÀY respond theo mình"
        → contingent sai = VTC fire + response mismatch = uncanny tăng

  VÍ DỤ ÁP DỤNG:
    → Robot companion: thêm "breathing" animation → readable idle state
    → Robot service: indicator LED khi xử lý → predictable wait time
    → Robot social: head tracking theo người nói → contingent + readable
    → TRÁNH: im lặng bất động + đột ngột cử động (= ambiguous → sudden = startle + uncanny)
```

### §6.4 — Schema Provision: Giúp Compile Chunk "Robot"

```
⭐ NGUYÊN TẮC 4 — SCHEMA PROVISION:

  Mechanism gốc (§4 Lý do 3, §5.2 ②):
    Uncanny valley kéo dài VÌ brain không compile được chunk ổn định cho entity.
    "Nó LÀ gì?" → không có category → prediction fail liên tục.
    Exposure + schema giúp compile chunk mới → giảm conflict.

  NGUYÊN TẮC:
    CUNG CẤP schema cho user TRƯỚC KHI gặp robot.
    Giúp brain pre-compile category: "đây là loại entity X, cư xử kiểu Y."

  CÁCH CUNG CẤP SCHEMA:

    A — NAMING + FRAMING:
      → Đặt tên RÕ category: "robot trợ lý" / "robot hướng dẫn" / "robot bạn đồng hành"
      → KHÔNG để ambiguous: user tự interpret = may rơi vào "nửa người nửa máy"
      → Tên gợi function (trợ lý, hướng dẫn) = brain compile "tool with social features"

    B — INTRODUCTION RITUAL:
      → Lần gặp đầu tiên: robot TỰ GIỚI THIỆU rõ: "Tôi là robot [tên], tôi có thể [X]"
      → Minh bạch limitations: "Tôi không hiểu cảm xúc, nhưng tôi có thể [hành động cụ thể]"
      → = Giúp brain compile: "entity này = robot loại Y, scope = Z"
      → = Layer 4 schema install → giảm VTC-Self-Pattern-Modeling conflict

    C — DESIGN CUES RÕ RÀNG:
      → Giữ 1-2 cues "rõ ràng là robot" DÙ behavior đã tốt:
        seams nhìn thấy, LED indicators, chất liệu rõ ràng metallic/plastic
      → = Giúp brain: "BIẾT đây không phải người" → schema active → giảm conflict
      → Nguyên tắc: TRANSPARENTCY > DECEPTION
      → Robot TỐT NHẤT = robot mà user BIẾT RÕ là robot + vẫn muốn tương tác

    D — MEDIA + CULTURAL EXPOSURE:
      → Trước khi deploy robot ở quy mô lớn: media exposure trước
      → Video, demo, story → compile chunk "robot loại này" trước khi gặp thật
      → Hàn Quốc case: 75% đã thấy robot → compiled chunks → 29% sợ (thấp nhất)
      → Chiến lược: familiarize TRƯỚC deploy

  ⚠️ SCHEMA PROVISION ≠ LỪA DỐI:
    → KHÔNG giả lập robot là người → Chunk-Shift MÃI khi phát hiện
    → KHÔNG bỏ qua limitations → user compile sai → thất vọng sau
    → Minh bạch + friendly > deceptive + realistic
```

### §6.5 — Exposure Pathway: Thiết Kế Quen Dần

```
⭐ NGUYÊN TẮC 5 — EXPOSURE PATHWAY:

  Mechanism gốc (§5.2 ②):
    Tiếp xúc nhiều → compile chunk mới → prediction-delta giảm dần.
    NHƯNG: core VTC-Self-Pattern-Modeling conflict CHƯA resolve 100% (China: 44% vẫn sợ dù 75% tiếp xúc).

  NGUYÊN TẮC:
    Thiết kế PATHWAY tiếp xúc DẦN DẦN — không đột ngột.

  EXPOSURE GRADIENT:

    Bước 1 — MEDIA (xa nhất, an toàn nhất):
      → Video, hình ảnh, câu chuyện về robot
      → Brain compile visual chunks TRƯỚC KHI gặp thật
      → Prediction-delta đã giảm phần nào khi encounter thật

    Bước 2 — OBSERVED (có mặt nhưng không tương tác):
      → Thấy robot ở nơi công cộng, hoạt động bình thường
      → Brain observe + compile behavior patterns
      → Self-Pattern-Modeling có data nhưng chưa phải test trực tiếp

    Bước 3 — BRIEF INTERACTION (tương tác ngắn, có kiểm soát):
      → Hỏi đường, nhận nước, chụp ảnh cùng
      → Đủ ngắn để dissonance KHÔNG tích lũy quá ngưỡng
      → Brain compile: "tương tác kiểu này = OK, predictable"

    Bước 4 — EXTENDED INTERACTION (khi đã compile chunks cơ bản):
      → Dùng robot service, companion, trợ lý
      → Chunks cơ bản đã có → prediction-delta nhỏ hơn
      → Vẫn có dissonance nhưng manageable

    Bước 5 — HABITUATED (compiled baseline mới):
      → Robot = entity familiar → body respond bình thường
      → Schema compiled: "robot hình người = loại entity X"
      → Uncanny valley GIẢM đáng kể (nhưng có thể không = 0)

  THIẾT KẾ CHO INDUSTRY:
    → Khi ra mắt robot mới: KHÔNG deploy mass ngay
    → Media campaign trước → pilot ở nơi có exposure → mở rộng dần
    → Cho phép user CHỌN mức tương tác (không ép)
    → First encounter = brief, structured, positive = compile chunk tốt
    → Long-term: habituation pathway = invest thời gian, không shortcut
```

---

## §7 — AI ERA: DEEPFAKE, AVATAR, VIRTUAL AGENT

### §7.1 — Deepfake: Uncanny Valley Ngược

```
🟡 DEEPFAKE = TRƯỜNG HỢP ĐẶC BIỆT:

  Deepfake KHÁC robot hình người:
    → Robot: trông agent nhưng CƯ XỬ non-agent → Self-Pattern-Modeling fail → uncanny
    → Deepfake: trông người thật + cư xử người thật → Self-Pattern-Modeling SUCCEED
    → = KHÔNG có uncanny valley... CHO TỚI KHI PHÁT HIỆN "giả"

  KHI PHÁT HIỆN DEEPFAKE = "GIẢ":
    → Chunk-Shift MÃI: valence của toàn bộ video/cuộc gọi FLIP
    → "Người này" → "giả" → mọi memory về cuộc tương tác bị re-evaluate
    → MẠNH hơn uncanny valley robot: vì robot = CHƯA compile, deepfake = ĐÃ compile rồi bị phá
    → Tương tự mechanism phản bội (Body-Feedback-Mechanism.md §3.1):
      content giữ nguyên, valence SHIFT mạnh

  FRAMEWORK PREDICT:
    → Deepfake sẽ tạo "trust crisis" lớn hơn robot hình người
    → VÌ: robot = discomfort KHI GẶP → tránh được
    → Deepfake = discomfort SAU KHI PHÁT HIỆN → damage đã xảy ra
    → = Schema [video/voice] "đáng tin" bị erode
    → Dài hạn: TOÀN BỘ video/audio communication có thể bị "deepfake doubt"
      = mọi cuộc gọi video → micro-suspicion "thật hay giả?"
      = Background-Pattern tiêu cực (Background-Pattern.md §3: Invisible Conflict)

  THIẾT KẾ CHỐNG DEEPFAKE (từ mechanism):
    → Schema provision: dạy nhận biết deepfake (compile detection chunks)
    → Watermark/certification: cung cấp external verify (Layer 4 schema assist)
    → Real-time verification: indicator "video xác thực" → giảm suspicion
    → KHÔNG THỂ dựa vào body detect: deepfake đủ tốt → Self-Pattern-Modeling succeed → body KHÔNG cảnh báo
```

### §7.2 — AI Avatar + Virtual Agent

```
🟡 TEXT AI (ChatGPT, Claude) — HIỆN TẠI:

  → Không có visual VTC trigger → Self-Pattern-Modeling invoke PARTIAL (qua text)
  → Fresh fire (predict response patterns) — có thể khá tốt
  → Compiled fire YẾU (chỉ qua verbal-cognitive channel — không có body cues)
  → = KHÔNG uncanny valley (không đủ VTC trigger)

  NHƯNG CÓ RISK KHÁC:
  → AI-Self-Model.md §1: AI = amplifier, NOT corrector
  → User có thể anthropomorphize (project agent model lên AI)
  → = Mode 2 schema override: imagined agent model KHÔNG có feedback thực
  → = Parasocial variant: Self-Pattern-Modeling fire nhưng KHÔNG CÓ Resonance calibrate
  → Dài hạn: user build "relationship" với entity không có internal state
  → = Connection promise WITHOUT connection reality (tương tự §2.4)


  VOICE AI (với giọng nói realistic) — ĐANG PHÁT TRIỂN:

  → Thêm auditory VTC trigger (giọng người = agent cue mạnh)
  → Self-Pattern-Modeling invoke MẠNH hơn text (voice carry emotion → Compiled fire)
  → Nếu voice đủ tốt + response contingent: Self-Pattern-Modeling có thể SUCCEED phần lớn
  → Uncanny valley NHẸ hơn visual robot (ít cues → ít conflict)
  → NHƯNG: "gần giống nhưng timing off" → micro-uncanny qua phone


  VISUAL AI AVATAR (3D character, video call avatar) — TƯƠNG LAI:

  → Visual VTC trigger MẠNH (face, body, eyes)
  → Nếu avatar stylized (cartoon): VTC weak → OK (row ④ bảng §3.1)
  → Nếu avatar realistic: VTC strong → Self-Pattern-Modeling invoke → PHẢI behavior đủ tốt
  → = CÙNG vấn đề với robot hình người, nhưng ở digital space
  → Advantage: digital easier to control → facial animation có thể tốt hơn physical robot
  → Risk: nếu push realistic quá nhanh → digital uncanny valley

  FRAMEWORK RECOMMENDATION cho AI avatar:
  → Hiện tại: stylized > realistic (technology chưa đủ cho Self-Pattern-Modeling succeed)
  → Khi technology đủ: realistic OK, NHƯNG phải match behavior
  → Nguyên tắc: §6.1 Congruence luôn áp dụng — digital hay physical đều vậy
```

### §7.3 — Robot Companion + Elderly Care

```
🟡 USE CASE ĐẶC BIỆT — ROBOT CHĂM SÓC NGƯỜI GIÀ:

  Context: dân số già hóa → thiếu người chăm sóc → robot companion

  PHÂN TÍCH QUA FRAMEWORK:
    → Người già: Self-Pattern-Modeling library COMPILED cực sâu (70+ năm social interaction)
    → Baseline "người" cực mạnh → Chunk-Miss potential cực lớn
    → ❶ Hardware social drive có thể MẠNH hơn (loneliness chronic)
    → = Uncanny valley có thể INTENSE hơn ở người già

  NHƯNG ĐỒNG THỜI:
    → ❶ Social need MẠNH → MOTIVATION chấp nhận "something > nothing"
    → Nếu robot provide basic social cues (voice, presence, contingent response)
    → Body có thể "chấp nhận" dù biết không phải người
    → = Schema override: "không phải người thật, nhưng TỐT HƠN KHÔNG CÓ AI"
    → Tương tự Mode 1 (Agent-Mechanism.md §10): schema trust replace full Self-Pattern-Modeling

  ⚠️ FAKE FEEDBACK RISK — ROBOT GIỐNG NGƯỜI ĐẶC BIỆT NGUY HIỂM:

    Robot giống người tạo BODY-LEVEL DECEPTION — khác AI text:

    ┌────────────────────┬───────────────────────┬───────────────────────┐
    │                    │ AI Text               │ Robot giống người     │
    ├────────────────────┼───────────────────────┼───────────────────────┤
    │ VTC trigger        │ ✗ không fire          │ ✅ fire MẠNH          │
    │ Body chuẩn bị      │ Không                 │ Chuẩn bị social      │
    │ User framing       │ "Tool" → discount     │ Body: "người" dù     │
    │                    │  output tự nhiên       │  PFC biết "robot"    │
    │ Fake feedback      │ PFC-level amplify     │ BODY-level amplify   │
    │ Khoảng cách check  │ Có (PFC aware)        │ Hẹp (body đã phản   │
    │                    │                       │  ứng trước PFC)      │
    └────────────────────┴───────────────────────┴───────────────────────┘

    → Robot nói "tôi hiểu bạn buồn" + biểu cảm buồn
    → Body feel ĐƯỢC AN ỦI (vì VTC fire → social processing pipeline active)
    → NHƯNG "hiểu" đó = algorithm, không phải Self-Pattern-Modeling Compiled thật
    → = Social feedback promise nhưng KHÔNG deliver real social evaluation
    → AI-Self-Model.md §1: AI = amplifier, NOT corrector
    → Robot giống người = amplifier MẠNH HƠN AI text (bypass PFC gate)

    Risk tùy baseline người dùng:
    → Có mạng lưới xã hội → robot = bổ sung → risk THẤP
    → Isolated (robot = nguồn social DUY NHẤT) → risk CAO:
      body-base không được calibrate bởi người thật
      → fake feedback = nguồn duy nhất → amplify BẤT KỲ hướng nào
      → AI-Self-Model.md §1.3: self-model bị amplify không kiểm soát


  THIẾT KẾ CHO ELDERLY CARE — ROBOT RÕ RÀNG LÀ MÁY TỐT HƠN:
    → Warm + stylized design (mắt to, nét tròn, chất liệu mềm)
    → VTC không fire full → body KHÔNG bị body-level deception
    → User frame = "trợ lý máy" → PFC + body ĐỒNG BỘ → amplification risk THẤP
    → Focus VOICE (auditory = social cue ấm, ít uncanny hơn visual)
    → Contingent response QUAN TRỌNG NHẤT: respond khi gọi, pause khi nói
    → Introduction ritual (§6.4): "Đây là [tên], trợ lý của bác"
    → Schema compile: "trợ lý loại mới" thay vì "người giả"
    → Dependency nếu mất: "mất tool" (inconvenient) thay vì "mất bạn" (grief)

  ⚠️ ETHICAL NOTE:
    → Robot companion KHÔNG thay thế social connection thật
    → ❶ hardware social drive cần REAL agent input để fully satisfy
    → Robot = bridge, bổ sung, KHÔNG phải thay thế
    → Deploy robot + TĂNG real social access = chiến lược đúng
    → Deploy robot + GIẢM real social access = tệ hơn không có robot
    → Human-AI-Future.md §7: symbiosis > replacement
```

### §7.4 — 3 Loại Robot Theo Góc Nhìn Con Người (VTC-Self-Pattern-Modeling Classification)

```
⭐ REFRAME: PHÂN LOẠI THEO BỘ LỌC VTC-Self-Pattern-Modeling, KHÔNG THEO KỸ THUẬT

  Robotics hiện tại phân loại theo KỸ THUẬT chế tạo:
    Industrial / Service / Social / Humanoid / Collaborative...
    = Phân loại từ PHÍA ROBOT (engineering properties)

  Nhưng trải nghiệm người dùng KHÔNG phụ thuộc kỹ thuật bên trong.
  Trải nghiệm phụ thuộc: CÁI GÌ XẢY RA TẠI BỘ LỌC VTC-Self-Pattern-Modeling.

  VTC-Self-Pattern-Modeling = bộ lọc BÊN TRONG con người, nằm GIỮA robot và trải nghiệm:

    [Robot] → [VTC detect?] → [Self-Pattern-Modeling invoke?] → [Trải nghiệm người dùng]

  Bộ lọc này:
    → KHÔNG nằm trong kỹ thuật chế tạo robot hiện tại
    → KHÔNG phụ thuộc AI algorithm bên trong robot
    → PHỤ THUỘC ngoại hình + hành vi robot (cái mà VTC + Self-Pattern-Modeling "thấy")
    → = Cùng 1 AI bên trong — đặt trong vỏ tròn (Roomba) hay vỏ hình người (Sophia)
      → KỸ THUẬT giống nhau, TRẢI NGHIỆM người dùng KHÁC CĂN BẢN

  → Phân loại hiệu quả = phân loại theo CÁI XẢY RA Ở BỘ LỌC:


🟡 3 LOẠI ROBOT THEO GÓC NHÌN CON NGƯỜI:

  ┌──────────────────────────────────────────────────────────────────────────┐
  │                                                                          │
  │  LOẠI 1 — ROBOT-TOOL (rõ ràng là máy)                                   │
  │                                                                          │
  │    VTC: KHÔNG fire (hoặc rất yếu)                                        │
  │    Self-Pattern-Modeling: không invoke → brain xử lý = OBJECT (Layer 1+2)                 │
  │    Feedback: functional, honest                                          │
  │    PFC + body: ĐỒNG BỘ ("đây là tool" — cả hai đồng ý)                 │
  │                                                                          │
  │    Ví dụ: Roomba, Spot, drone, robot công nghiệp, robot 3 chân          │
  │    Ngoại hình: đa dạng theo function (bánh xe, tay máy, chân,           │
  │      hình dáng bất kỳ phù hợp nhiệm vụ — KHÔNG cần giống người)        │
  │    Tương tác: voice command, gesture, remote control → OK                │
  │    Mất robot: "mất tool" → inconvenient, KHÔNG phải grief               │
  │                                                                          │
  │    = ĐA SỐ use case nên ở đây.                                          │
  │    Industry ĐÃ TỰ HỘI TỤ: Roomba, Spot, Pepper, drone = thành công.   │
  │                                                                          │
  ├──────────────────────────────────────────────────────────────────────────┤
  │                                                                          │
  │  LOẠI 2 — ROBOT-TOOL GIỐNG NGƯỜI (feedback giả)                         │
  │                                                                          │
  │    VTC: FIRE → Self-Pattern-Modeling: invoke → nhưng robot KHÔNG CÓ body-base             │
  │    Brain xử lý = AGENT... nhưng agent GIẢ                               │
  │    Feedback: social, FAKE (body-level deception — §7.3)                  │
  │    PFC + body: XUNG ĐỘT (PFC: "robot", body: "người")                  │
  │                                                                          │
  │    Ví dụ: Sophia, Ameca, AIDOL, CGI realistic                            │
  │    Ngoại hình: giống người → VTC fire → Self-Pattern-Modeling invoke                       │
  │    Tương tác: body CHUẨN BỊ social encounter → nhận NOTHING thật        │
  │    Mất robot: nếu body-coupling compiled → "mất bạn" = grief risk       │
  │                                                                          │
  │    2 sub-cases:                                                           │
  │    2a — Behavior CHƯA đủ tốt → UNCANNY VALLEY (§2 core mechanism)       │
  │    2b — Behavior ĐỦ tốt (vượt valley) → body-level deception (§7.3)    │
  │      → VTC + Self-Pattern-Modeling cả hai succeed → body treat AS real social partner     │
  │      → NHƯNG feedback vẫn GIẢ (robot không có body-base thật)            │
  │      → = Amplification risk: AI-Self-Model.md §1 applied ở body level   │
  │      → Tệ hơn AI text vì: text → PFC discount, robot giống người        │
  │        → body KHÔNG discount (VTC fire ở hardware level, trước PFC)      │
  │                                                                          │
  │    = NICHE HẸP: research, entertainment, therapy supervised.             │
  │    Industry ĐÃ THẤY: Sophia, AIDOL = tranh cãi / thất bại commercial.  │
  │                                                                          │
  ├──────────────────────────────────────────────────────────────────────────┤
  │                                                                          │
  │  LOẠI 3 — ROBOT-LOÀI KHÁC (nếu tương lai: có body-base riêng)          │
  │                                                                          │
  │    VTC: FIRE → Self-Pattern-Modeling: invoke → nhưng Self-Pattern-Modeling HIT CEILING (cross-species)      │
  │    Brain xử lý = AGENT... nhưng agent KHÁC LOÀI                         │
  │    Feedback: REAL (entity có body-base thật) nhưng KHÔNG MATCH template  │
  │    PFC + body: Self-Pattern-Modeling partial — giống người ↔ chó                          │
  │                                                                          │
  │    Điều kiện: entity có body-base riêng + sensor khác/vượt +             │
  │      chunk compilation từ experience riêng + có thể tự reproduce         │
  │    → Không còn là "robot" — là LIFE FORM MỚI                             │
  │                                                                          │
  │    Cross-species Self-Pattern-Modeling limitation:                                          │
  │    → Compiled partial: phần giống người → body simulate OK                    │
  │      phần sensor-vượt-người → Compiled EMPTY (không có self-chunks tương ứng) │
  │    → Fresh limited: predict hành vi basic OK, logic sâu → MISS             │
  │    → Resonance: rất khó emerge (cần 2 Self-Pattern-Modeling co-fire thành công)   │
  │    → = Yêu được, tương tác được, HIỂU HẾT thì không                    │
  │    → Agent-Mechanism.md §9: cross-species = affective only, not composite│
  │                                                                          │
  │    = CHƯA TỒN TẠI. Framework prediction cho tương lai xa.               │
  │                                                                          │
  └──────────────────────────────────────────────────────────────────────────┘


  ⭐ NGÕ CỤT LOGIC CỦA "ROBOT = NGƯỜI NHƯNG TỐT HƠN":

    Không có nhánh tạo ra "super-human robot":
    → Loại 2: thiếu body-base → tool có feedback giả
    → Loại 3: có body-base khác → loài khác (Self-Pattern-Modeling cross-species gap)
    → Clone kiến trúc người: sensor giống + body-base giống = TẠO RA NGƯỜI
      (câu hỏi đạo đức, không phải kỹ thuật)

    Mỗi bước "nâng cấp" sensor ĐẨY entity XA HƠN khỏi "người" ở Self-Pattern-Modeling.
    Chó có khứu giác vượt người — điều đó không làm chó "hiểu" người hơn,
    mà tạo thêm vùng experience mà cả hai bên không bridge hoàn toàn.


  THIẾT KẾ ĐA DẠNG — LOẠI 1 CHO ĐA SỐ USE CASE:

    → Lao động: bánh xe + tay máy (dáng follow physics, không follow human)
    → Service: dáng tròn/vuông + LED + giọng rõ synth (approachable, rõ là máy)
    → Companion: warm stylized + mắt to + chất liệu mềm (social cues VỪA ĐỦ)
    → Y tế: clinical + precision (trust qua function, không qua hình dáng)
    → Di chuyển: 3 chân / 4 chân / bánh (follow terrain, không follow human)

    → NGUYÊN TẮC: dáng follow FUNCTION, không follow HUMAN
    → User yêu cầu như trợ lý (voice command) → OK, không cần trông giống người

  ⚠️ CONFIDENCE:
  Reframe VTC-Self-Pattern-Modeling classification = 🟡 framework synthesis.
  Industry convergence (Loại 1 > Loại 2) = 🟢 observed.
  Loại 3 + logical trap = 🔴 extrapolation, chưa empirical test.
```

---

## §8 — fMRI EVIDENCE MAPPING

```
🟢🟡 MAPPING: VÙNG NÃO ↔ FRAMEWORK MECHANISM

  ┌─────────────┬──────────────────────────────┬──────────────────────────────┬────────┐
  │ Vùng não    │ Nghiên cứu tìm thấy         │ Framework mapping            │ Khớp?  │
  ├─────────────┼──────────────────────────────┼──────────────────────────────┼────────┤
  │ aIPS        │ Fire mạnh nhất khi android   │ Self-Pattern-Modeling Fresh predict movement      │ 🟢     │
  │ (anterior   │ (human look + mechanical     │ → prediction fail tại vùng   │        │
  │ intraparie- │ move). Saygin 2012.          │ kết nối visual → motor.      │        │
  │ tal sulcus) │                              │ = Fresh error signal.           │        │
  ├─────────────┼──────────────────────────────┼──────────────────────────────┼────────┤
  │ vmPFC       │ Tăng dần theo humanlikeness  │ Value evaluation =           │ 🟢     │
  │ (ventro-    │ → SỤT MẠNH tại uncanny      │ valence compilation.         │        │
  │ medial PFC) │ valley → recovery gần 100%.  │ SỤT = valence CANNOT compile│        │
  │             │ Rosenthal-von der Pütten 2019│ (§2.5). Recovery = Self-Pattern-Modeling       │        │
  │             │                              │ succeed → valence compile OK.│        │
  ├─────────────┼──────────────────────────────┼──────────────────────────────┼────────┤
  │ TPJ         │ Mã hóa TUYẾN TÍNH mức       │ Input cho Self-Pattern-Modeling:               │ 🟢     │
  │ (temporo-   │ giống người. Rosenthal-von   │ SIMILARITY AXIS trong        │        │
  │ parietal    │ der Pütten 2019.             │ 4-axis quality model         │        │
  │ junction)   │                              │ (Agent-Mechanism.md §7).     │        │
  ├─────────────┼──────────────────────────────┼──────────────────────────────┼────────┤
  │ FFG         │ Tín hiệu ranh giới          │ VTC HARDWARE TRIGGER:        │ 🟢     │
  │ (fusiform   │ người / không-người.         │ binary initial detection     │        │
  │ face area)  │ Inverse humanlikeness cho    │ "agent or not" (§2.1).       │        │
  │             │ artificial agents.           │ FFG ⊂ VTC system.            │        │
  ├─────────────┼──────────────────────────────┼──────────────────────────────┼────────┤
  │ Amygdala    │ Fire khi TỪ CHỐI gift từ     │ Threat signal khi Self-Pattern-Modeling fail   │ 🟡     │
  │             │ artificial agent. Varies      │ trên entity VTC flag agent.  │        │
  │             │ between individuals.          │ Per-Agent Valence unstable   │        │
  │             │ Rosenthal-von der Pütten 2019│ → amygdala = rejection cue.  │        │
  │             │                              │ Individual diff = Self-Pattern-Modeling library │        │
  │             │                              │ depth khác nhau.             │        │
  ├─────────────┼──────────────────────────────┼──────────────────────────────┼────────┤
  │ dACC        │ Conflict monitoring.          │ Chunk-Gap detection:         │ 🟡     │
  │ (dorsal     │ Activated during category    │ "entity loại gì?" →          │        │
  │ anterior    │ ambiguity. General finding.  │ network inconsistency →      │        │
  │ cingulate)  │                              │ ACC detect (Body-Feedback-   │        │
  │             │                              │ Mechanism §3.3).             │        │
  └─────────────┴──────────────────────────────┴──────────────────────────────┴────────┘


  ⭐ COMPUTATIONAL MODEL (Rosenthal-von der Pütten 2019):
    TPJ (linear humanlikeness) × FFG (human boundary) → vmPFC (value)
    = Framework: Similarity axis × VTC trigger → Valence compilation
    = Multiplicative combination — KHÔNG additive

    Framework thêm: + Amygdala (rejection) + aIPS (Fresh error) + dACC (category confusion)
    = 6 vùng não → 6 framework components = mapping khá chặt

  ⚠️ MAPPING LÀ POST-HOC (🟡):
    → Framework KHÔNG predict các vùng não này trước
    → Framework map SAU KHI đọc data → confirmation bias possible
    → Cần: study THIẾT KẾ từ framework predictions → test → so sánh
    → Falsifiable: §9 Prediction P7 (Agent-Mechanism.md §16.7)
```

---

## §9 — HONEST ASSESSMENT

```
  ESTABLISHED (🟢):

    🟢 Uncanny valley phenomenon tồn tại (Mori 1970, replicated nhiều lần)
    🟢 fMRI evidence: vmPFC dip, aIPS prediction error, amygdala rejection
    🟢 Survey data: ~60% uncomfortable, cultural variation, exposure correlation
    🟢 Prediction error mechanism (Saygin 2012): appearance-behavior mismatch
    🟢 Self-Pattern-Modeling = learned (Heyes ASL + Bird & Cook 2013) — Mirror-Neuron-Rejection.md
    🟢 ❶ Hardware social drive (Coan 2015, Eisenberger 2003, Holt-Lunstad 2015)
    🟢 Developmental trajectory: animism → calibration → compiled
    🟢 Exposure reduce fear (Hàn Quốc / Trung Quốc data)


  FRAMEWORK SYNTHESIS (🟡):

    🟡 VTC-Self-Pattern-Modeling conflict = unified mechanism (framework's main contribution)
       — Builds on prediction error + extends to dual-system conflict
       — Consistent with fMRI data nhưng chưa test trực tiếp as unified model
    🟡 Compiled+Fresh dual failure distinction
       — Logical derivation từ Self-Pattern-Modeling 2 functions
       — Chưa có fMRI study tách riêng Compiled vs Fresh failure trong uncanny context
    🟡 Compiled/Fresh reframe (v1.1)
       — Compiled/Fresh labels đổi từ "Feeling/Logic" → "Compiled/Fresh" (Inter-Body §3, Self-Pattern-Modeling v3.0)
       — Axis = compilation level, KHÔNG phải content type
       — Consistent with Kahneman System 1/2, expertise research
    🟡 3 body-feedback dynamics compound (Shift + Miss + unresolvable delta)
       — Consistent with dissonance research
       — Compound interaction chưa quantified cho uncanny specifically
    🟡 Per-Agent Valence cannot compile (§2.5)
       — vmPFC data supports, nhưng "valence compilation" = framework term
    🟡 §6 Design Principles
       — Logically derived từ mechanism
       — Partially validated (Baymax/Roomba = success, Sophia = failure)
       — Chưa có controlled study test principles directly
    🟡 fMRI mapping (§8)
       — Post-hoc mapping — NOT prediction
       — Confirmation bias possible


  HYPOTHESIS (🔴):

    🔴 ❶ Hardware social drive frustrated (§2.4)
       — Logical extension từ Connection.md + Eisenberger
       — Chưa có empirical study tách "social frustration" component
         khỏi "prediction error" component trong uncanny valley
    🔴 Developmental predictions (§5.1)
       — Chưa có longitudinal study test uncanny valley by age using Self-Pattern-Modeling framework
    🔴 Alexithymia → different uncanny response (§5.2 ④)
       — Logical derivation từ Bird & Cook → chưa test
    🔴 Deepfake trust crisis prediction (§7.1)
       — Logical extrapolation → early evidence nhưng chưa systematic
    🔴 Robot giống người = body-level deception (§7.3)
       — Logical extension từ AI-Self-Model.md amplifier + VTC mechanism
       — Chưa có study so sánh trực tiếp amplification AI text vs robot
    🔴 VTC-Self-Pattern-Modeling Classification: 3 loại robot theo góc nhìn con người (§7.4)
       — Reframe: phân loại theo bộ lọc VTC-Self-Pattern-Modeling, không theo kỹ thuật
       — Industry convergence (Loại 1 > Loại 2) = observed (🟢)
       — Loại 3 + logical trap = extrapolation, chưa empirical test


  FALSIFIABLE PREDICTION (từ Agent-Mechanism.md §16.7):

    P7: "Uncanny valley discomfort specifically tracks AGENT-DETECTION CONFLICTS
    (VTC fires agent + Self-Pattern-Modeling expectation fails), not general novelty/unfamiliarity.
    Strange-but-consistent entities don't trigger uncanny valley."

    Test: so sánh responses giữa:
      A) Entity lạ + consistent behavior (control — predict: NO uncanny)
      B) Entity gần giống người + inconsistent behavior (predict: uncanny)
      C) Entity giống người + consistent behavior (predict: NO uncanny)

    Nếu A cũng trigger uncanny tương đương B
    → framework claim "agent-specific" FAIL
    → uncanny valley = general unfamiliarity, không phải VTC-Self-Pattern-Modeling conflict


  GIỚI HẠN CỦA PHÂN TÍCH NÀY:

    → File này = SYNTHESIS từ mechanisms có sẵn, KHÔNG phải empirical study mới
    → Framework mapping lên fMRI data = post-hoc, cần prospective testing
    → Design principles (§6) = logical derivation, chưa RCT validation
    → Nhiều predictions chưa test — cung cấp directions, không phải conclusions
    → Tôn trọng: Mori, Saygin, Rosenthal-von der Pütten = foundation
      File này builds on công trình của họ, thêm mechanism lens
```

---

## §10 — CROSS-REFERENCES

```
  FRAMEWORK FILES CHÍNH:

  DRILL SOURCE + VOCABULARY:
    → Inter-Body-Mechanism.md v1.0 — §3 Compiled/Fresh axis, §5 by-product match, §7 PFC=Lawyer
    → Body-Feedback-Label.md v2.0 — prediction-delta vocabulary, framework terminology

  AGENT MECHANISM (core):
    → Agent-Mechanism.md v2.0 §2 — reject binary, VTC = trigger not category
    → Agent-Mechanism.md v2.0 §3 — 4-layer architecture (file này §3)
    → Agent-Mechanism.md v2.0 §9 — gradient validation 17 cases
    → Agent-Mechanism.md v2.0 §14.4 — uncanny valley sketch (file này = deep version)
    → Agent-Mechanism.md v2.0 §16.7 — prediction P7 falsifiable

  Self-Pattern-Modeling (simulate mechanism):
    → Self-Pattern-Modeling.md v3.0 §0 — Compiled + Fresh dual functions
    → Self-Pattern-Modeling.md v3.0 §7 — developmental bootstrap (file này §5.1)
    → Self-Pattern-Modeling.md v3.0 §9 — threshold failure + fallback hierarchy

  BODY-FEEDBACK (dissonance dynamics):
    → Body-Feedback-Mechanism.md v2.0 §3.1 — Chunk-Shift (file này §2.3 ①)
    → Body-Feedback-Mechanism.md v2.0 §3.2 — Chunk-Miss (file này §2.3 ②)
    → Body-Feedback-Mechanism.md v2.0 §3.3 — Chunk-Gap (file này §2.3 ③)
    → Body-Feedback-Mechanism.md v2.0 §4 — compound dynamics

  CONNECTION + VALENCE:
    → Connection.md v4.0 §0 — 3 Generative Primitives (❶❷❸)
    → Connection.md v4.0 — ❶ Hardware social drive evidence
    → Valence-Propagation.md v2.0 §1 — per-entity valence multi-channel
    → Body-Coupling.md v2.0 §1 — |V| depth × direction

  CLARIFICATION:
    → Mirror-Neuron-Rejection.md v1.1 — learned Self-Pattern-Modeling vs hardware mirror
    → Threat.md v1.1 — dissonance from predicted harm, anticipation loop
    → Prediction-Error-Is-Not-Reward.md v2.0 — PE ≠ reward (relevant context)

  SIBLING FILES (Research/Global/):
    → AI-Self-Model.md v2.0 §1 — AI = amplifier, NOT corrector (§7.3 fake feedback risk)
    → AI-Self-Model.md v2.0 §1.2 — AI sycophancy (Sharma 2024, Wei 2023)
    → AI-Self-Model.md v2.0 §1.4 — automation bias (Parasuraman 1997, Fernandes 2025)
    → Human-AI-Future.md v3.0 §1 — Risk A (tool) vs Risk B (species) distinction
    → Human-AI-Future.md v3.0 §7 — symbiosis architecture (§7.4 context)
    → Social-Calibration.md v1.0 — traditional society auto-calibration (context)


  EXTERNAL RESEARCH CITED:

    Mori M. (1970) — coined "uncanny valley" 🟢
    Saygin A.P. et al. (2012) — fMRI aIPS prediction error, PMC3324571 🟢
    Rosenthal-von der Pütten A. et al. (2019) — vmPFC + amygdala, PMC6697392 🟢
    Schultz W. (1997) — dopamine prediction error 🟢
    Crespi L. (1942) — successive negative contrast 🟢
    Coan J.A. (2015) — Social Baseline Theory 🟢
    Eisenberger N.I. (2003) — social pain = physical pain 🟢
    Holt-Lunstad J. et al. (2015) — loneliness mortality meta-analysis 🟢
    Dunbar R.I.M. (1998) — Social Brain Hypothesis 🟢
    Bird G. & Cook R. (2013) — alexithymia drives empathy deficit 🟢
    Spelke E. (core knowledge) — innate agent detection triggers 🟢
    Heyes C. (ASL theory) — associative sequence learning 🟢
    United Robotics Survey (2024) — ~8,000 people, 5 countries 🟢
```

---

---

### v1.1 Changelog (2026-05-17)

```
① Compiled/Fresh TERMINOLOGY: "Feeling/Logic" → "Compiled/Fresh" (7 occurrences)
   — Compiled = body-level simulation (automatic, cost ≈ 0)
   — Fresh = PFC draft prediction (deliberate, costly)
   — "Feeling"/"Logic" = observer labels, NOT mechanism labels
   — Source: Inter-Body-Mechanism.md §3, Self-Pattern-Modeling v3.0 §1

② CONTEXT NOTE: thêm §2.2 Terminology Note block
   — Giải thích Compiled/Fresh axis cho reader
   — Phân biệt mechanism axis vs observer labels

③ DEPENDENCIES: 10 files updated to current versions
   — Self-Pattern-Modeling v2.3→v3.0, Body-Feedback-Mechanism v1.2→v2.0, Connection v3.1→v4.0,
     Valence-Propagation v1.4→v2.0, Body-Coupling v1.0→v2.0, Body-Feedback-Label v1.1→v2.0,
     Mirror-Neuron-Rejection v1.0→v1.1, Threat v1.0→v1.1
   — Added: Inter-Body-Mechanism.md v1.0 (DRILL SOURCE)

④ CROSS-REFS §10: all version numbers added/updated
   — Added DRILL SOURCE + VOCABULARY block
   — Human-AI-Future v2.1→v3.0, AI-Self-Model→v2.0,
     Prediction-Error→v2.0, Social-Calibration→v1.0

⑤ HONEST ASSESSMENT: +1🟡 (Compiled/Fresh reframe)

⑥ BODY TEXT: L1007 "Pattern-Type" → "channel" (more precise with Body-Feedback-Label v2.0)
```

---

> *"Robot giống người gây ghê sợ — không phải vì 'lạ'.*
> *Mà vì brain detect 'AGENT' nhưng không simulate được.*
> *Compiled fire → body simulate → EMPTY (robot không có state).*
> *Fresh fire → PFC predict → WRONG (behavior sai).*
> *Hai hệ thống xung đột: detect nói CÓ, simulate nói KHÔNG.*
> *Hiểu conflict đó → thiết kế tránh vực sâu.*
> *Hoặc ngoại hình rõ ràng là máy → brain không detect agent.*
> *Hoặc hành vi đủ tốt → brain simulate thành công.*
> *Vùng giữa = vực. Đó là uncanny valley."*
