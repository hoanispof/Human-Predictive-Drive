---
title: AI-Schema-Detection — AI Hỗ Trợ Nhận Diện Schema + Valence Chain
version: 1.0
created: 2026-04-18
status: v1.0 — APPLICATION FILE (ứng dụng Valence-Propagation + Schema understanding)
scope: |
  HOW AI có thể hỗ trợ nhận diện schema patterns + valence chains.
  3-layer model: AI detect → Chuyên gia feel-check → Client self-verify.
  Fundamental limits: approximate, KHÔNG chính xác tuyệt đối.
  Upgraded từ Schema-Diagnostic.md (backup) + session N+16 analysis.
purpose: |
  Cầu nối framework lý thuyết → thực hành hỗ trợ.
  Ứng dụng trực tiếp từ Valence-Propagation.md §8 ("Mở cửa cho AI-Schema-Detection").
  Không phải tool AI cụ thể — mà là KIẾN TRÚC cho AI-assisted schema navigation.
sources: |
  Valence-Propagation.md v1.0 §8 — fundamental limits + 3 nguyên tắc + mở cửa ứng dụng
  Schema.md v1.1 §1.2 — "KHÔNG THỂ phân tích chính xác" (86 tỷ neurons, ~1/6 verbal)
  Schema/backup/Schema-Diagnostic.md — quy trình 5 bước map schema (upgraded)
  Somatic-Articulation-Loop.md — body-knowledge → explicit (Focusing, AI catalyst §5)
  Feeling.md v2.0 §2 (7-layer), §10 (Feeling Literacy 5-stage + AI era)
  Agent.md §0 — Self-Pattern-Match (chuyên gia simulate client)
  Chunk.md v2.0 §4 — activation dynamics, trigger surface, competitive re-linking
  Drive.md v1.1 §2 — 6 PFC Modes (spinning vs resolve = chunk availability)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# AI-Schema-Detection — AI Hỗ Trợ Nhận Diện Schema + Valence Chain

> **Bạn nói: "Tôi thích từ thiện."**
> **AI nghe 100 giờ nói chuyện của bạn.**
> **AI thấy: mỗi khi nói "giúp đỡ", bạn cũng nói "mẹ", "tuổi thơ", "bị bỏ rơi".**
> **AI gợi ý: "giúp đỡ" có thể link với "chứng minh tôi cần thiết".**
>
> **Chuyên gia tâm lý nghe AI.**
> **Chuyên gia simulate trong body MÌNH: "nếu tôi sợ bị bỏ rơi, tôi SẼ..."**
> **Body chuyên gia: "đúng, feel hợp lý."**
> **Chuyên gia hỏi bạn: "Khi nghĩ về giúp đỡ, body bạn cảm gì?"**
>
> **Bạn dừng lại. Lắng nghe body.**
> **"Ngực hơi nặng. Như sợ mất gì đó."**
> **→ Body vote: hypothesis CONFIRMED.**
>
> **AI detect. Chuyên gia feel-check. Bạn self-verify.**
> **3 tầng. Không ai đủ một mình. Cùng nhau: ENOUGH.**
>
> **"Công cụ NAVIGATE, không phải GPS chính xác."**

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — GIỚI HẠN NỀN TẢNG
- §2 — 3-LAYER MODEL (Kiến trúc tổng thể)
- §3 — AI LAYER: Pattern Detection + Chunk Depth Inference
- §4 — CHUYÊN GIA LAYER: Self-Pattern-Match + Body Vote
- §5 — CLIENT LAYER: Focusing + Self-Verify
- §6 — QUY TRÌNH THỰC HÀNH (Upgraded)
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES + STATUS

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 AI-SCHEMA-DETECTION TRONG KIẾN TRÚC:

  Framework đã xác lập (Valence-Propagation.md §8):
    → Schema vô tận, chain không thể map chính xác
    → NHƯNG: KHÔNG CẦN chính xác tuyệt đối
    → CÓ THỂ: nhận diện PATTERN, ước lượng NHÓM, suggest HƯỚNG
    → = "Công cụ NAVIGATE, không phải GPS chính xác"

  File NÀY = ỨNG DỤNG nguyên tắc đó:
    → HOW nhận diện patterns trong thực tế?
    → AI role + Chuyên gia role + Client role = gì?
    → Quy trình THỰC HÀNH upgraded từ Schema-Diagnostic.md

  Flow:
    Valence-Propagation.md §8 (lý thuyết: giới hạn + mở cửa)
         │
         ▼
    ┌─────────────────────────────────────────────────────────┐
    │ AI-SCHEMA-DETECTION.MD (FILE NÀY)                       │
    │                                                          │
    │   §1: Giới hạn (đặt kỳ vọng ĐÚNG)                      │
    │   §2: 3-Layer Model (kiến trúc tổng thể)               │
    │   §3-§5: Chi tiết mỗi layer                            │
    │   §6: Quy trình thực hành                              │
    └─────────────────────────────────────────────────────────┘
         │
         ▼
    Ứng dụng cụ thể:
      → Therapy (chuyên gia tâm lý + AI)
      → Self-development (tự calibrate + AI)
      → Education (giáo viên + AI detect learning patterns)
      → Workplace (coaching + AI behavioral analysis)
```

---

## §1 — GIỚI HẠN NỀN TẢNG

```
🟡 NHẮC LẠI — TẠI SAO KHÔNG THỂ CHÍNH XÁC:

  Schema.md §1.2 đã xác lập:
    ① 86 tỷ neurons × ~100 nghìn tỷ connections = quá lớn để đọc
    ② Schema = multi-modal (verbal chỉ ~1/6 schema thật)
    ③ Schema SÂU = body adaptation (cortisol, muscle tension, gut state)
       → Chính người đó CŨNG không biết
    ④ Schema thay đổi liên tục
    ⑤ Khoa học chưa đủ công cụ

  Valence-Propagation.md §8 thêm:
    ⑥ Valence chain = schema × schema × links = vô tận × vô tận
    ⑦ PFC accuracy giảm theo chain length (confabulation)
    ⑧ Body check OUTPUT, không check TRUTH

  → TỔNG: schema network KHÔNG THỂ map chính xác từ bên ngoài.


  NHƯNG — ĐẶT KỲ VỌNG ĐÚNG:

  KHÔNG CẦN chính xác tuyệt đối. Con người chỉ cần:
    ① Biết PATTERN nào đang drive mình (nhận diện)
    ② Biết pattern đó SERVE body-base hay KHÔNG (check output)
    ③ Biết khi nào cần THAY ĐỔI (detect dissonance)

  METAPHOR:
    → Bác sĩ KHÔNG cần biết chính xác TỪNG tế bào
    → Bác sĩ cần: triệu chứng → cluster → diagnosis → treatment → verify
    → = Approximate + verify + adjust = ĐỦ để chữa bệnh
    → = AI-Schema-Detection CÙNG NGUYÊN LÝ


  3 CÁI CÓ THỂ:

    ① NHẬN DIỆN PATTERN (hành vi lặp lại = schema biểu hiện)
      → "Bạn luôn tránh conflict" = pattern observable
      → Pattern ≠ schema (pattern = OUTPUT, schema = MECHANISM)
      → NHƯNG: pattern → INFER schema cluster (ước lượng)

    ② ƯỚC LƯỢNG NHÓM (schema thuộc cluster nào)
      → "Tránh conflict" + "hay chiều người khác" + "sợ bị bỏ"
      → Cluster: có thể liên quan "abandonment fear" schema
      → = Cluster ≠ chẩn đoán. Cluster = hypothesis để verify.

    ③ SUGGEST HƯỚNG (chain NÀY có vẻ link tới body-base CHANNEL kia)
      → "Abandonment fear" → có thể link tới L1 connection deficit
      → Suggest: strengthen connection TRƯỚC, conflict skill SAU
      → = Hướng ≠ đáp án. Cần verify qua body-check.

  🟡 3-capability model = derived from Schema.md + Valence-Propagation.md
  🟢 "Navigate, not GPS" = consistent with bounded rationality (Simon 1955)
```

---

## §2 — 3-LAYER MODEL (Kiến trúc tổng thể)

```
🔴 HYPOTHESIS — application architecture, logic consistent, chưa test systematic

  ⭐ KHÔNG AI LAYER NÀO ĐỦ MỘT MÌNH:

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  LAYER 1: AI PATTERN DETECTOR                               │
  │    Input: verbal data, behavioral patterns, (optional) bio   │
  │    Process: NLP, clustering, contradiction detection         │
  │    Output: schema map SƠ LƯỢC + hypotheses                  │
  │    Strength: NHANH, RỘNG, không bỏ sót pattern              │
  │    Weakness: KHÔNG CÓ BODY → KHÔNG feel-check               │
  │    Confidence: LOW-MEDIUM (pattern ≠ causation)              │
  │                                                              │
  │         │ hypotheses + patterns                              │
  │         ▼                                                    │
  │                                                              │
  │  LAYER 2: CHUYÊN GIA FEEL-CHECKER                           │
  │    Input: AI suggestions + clinical experience               │
  │    Process: Self-Pattern-Match (simulate client in own body) │
  │    Output: verified / rejected hypotheses                    │
  │    Strength: CÓ BODY → feel-check → SÂU                     │
  │    Weakness: biased by own schemas, limited by own chunks    │
  │    Confidence: MEDIUM-HIGH (body-checked)                    │
  │                                                              │
  │         │ verified hypotheses + questions                    │
  │         ▼                                                    │
  │                                                              │
  │  LAYER 3: CLIENT SELF-VERIFIER                               │
  │    Input: verified hypotheses from expert                    │
  │    Process: Focusing (body listen) + PFC articulate          │
  │    Output: confirmed / denied + self-knowledge increase      │
  │    Strength: AUTHENTIC nhất — body CỦA HỌ là ultimate judge │
  │    Weakness: có thể suppress, deny, chưa đủ Feeling Literacy │
  │    Confidence: HIGHEST khi client có body-awareness skill    │
  │                                                              │
  │  KẾT QUẢ:                                                    │
  │    AI detect (NHANH, RỘNG) + Expert verify (SÂU, CẢM NHẬN)  │
  │    + Client confirm (AUTHENTIC) = 3 TẦNG verification        │
  │    → Confidence TĂNG DẦN qua mỗi layer                      │
  │    → Approximate + verified + confirmed = ENOUGH             │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘


  TẠI SAO 3 LAYERS, KHÔNG PHẢI 1 HAY 2:

    CHỈ AI (Layer 1):
      → Detect pattern nhưng KHÔNG feel-check
      → Có thể HOÀN TOÀN SAI về causation
      → VD: AI thấy "luôn nói về mẹ khi stress" → infer "mẹ = source"
        → NHƯNG: có thể mẹ = SAFE PLACE, không phải source
      → = Pattern ≠ Mechanism. AI thấy correlation, không thấy causation.

    CHỈ CHUYÊN GIA (Layer 2):
      → Feel-check TỐT nhưng BỎ SÓT patterns dài hạn
      → Chuyên gia nghe 1 giờ/tuần → miss patterns across 100 giờ
      → Chuyên gia cũng có OWN schemas → bias simulation
      → = Sâu nhưng hẹp. Cần AI mở rộng scope.

    CHỈ CLIENT (Layer 3):
      → Body BIẾT nhưng KHÔNG biết cách LẮNG NGHE
      → PFC confabulate (Valence-Propagation.md §7)
      → Suppress + deny = common defense
      → = Authentic nhưng cần GUIDE. Cần AI + Expert mở đường.

    3 LAYERS BỔ SUNG:
      → AI mở RỘNG (scope) → Expert đào SÂU (verify) → Client xác THẬT (confirm)
      → Mỗi layer bù weakness của layer khác
      → = Không ai ĐỦ → nhưng cùng nhau = ENOUGH

  🟢 Multi-method assessment improves validity (Campbell & Fiske 1959)
  🟢 Therapeutic alliance + client self-report = best outcomes (Lambert 2013)
  🟡 3-layer architecture = framework application model
```

---

## §3 — AI LAYER: Pattern Detection + Chunk Depth Inference

```
🟡 AI CÓ THỂ LÀM GÌ — 6 KHẢ NĂNG CỤ THỂ:


  ① VERBAL PATTERN TRACKING (across sessions):

    → Client nói 100 giờ → AI track TOÀN BỘ verbal patterns
    → Phát hiện: "mỗi khi nói về công việc, client dùng 'phải', 'nên', 'sợ'"
    → Phát hiện: "mỗi khi nói về bạn bè, client dùng 'vui', 'thoải mái'"
    → → Gợi ý: valence "công việc" = negative (threat-based language)
    → → Gợi ý: valence "bạn bè" = positive

    Chuyên gia nghe 1 giờ/tuần → CÓ THỂ BỎ SÓT pattern lặp qua nhiều tháng
    AI KHÔNG bỏ sót (memory + pattern match trên full corpus)

    🟢 NLP sentiment analysis = existing technology
    🟢 Topic modeling = established (LDA, BERT embeddings)


  ② SCHEMA CLUSTER SUGGESTION:

    → AI thấy: khi nói "công việc" → language tense
    → AI thấy: khi nói "sếp" → CŨNG tense, CÙNG từ ngữ
    → AI thấy: khi nói "bố" → CŨNG CÙNG pattern
    → → Gợi ý: "công việc", "sếp", "bố" có thể thuộc CÙNG schema cluster
    → → Possible chain: bố (authority) → sếp (authority) → công việc (authority context)
    → = AI detect LATERAL links mà chuyên gia chưa thấy

    VD mạnh hơn:
    → Client: "Tôi thích giúp đỡ mọi người" (positive, session 5)
    → Client: "Hồi nhỏ tôi hay bị bỏ một mình" (neutral tone, session 12)
    → Client: "Tôi rất khó chịu khi người ta từ chối giúp đỡ của tôi" (session 23)
    → AI cluster: "giúp đỡ" + "bị bỏ" + "từ chối" = possible chain:
      "giúp đỡ" = chứng minh "tôi cần thiết" = resolve "bị bỏ rơi" fear
    → Chuyên gia CHƯA THẤY vì 3 data points cách nhau 18 sessions

    🟡 Schema clustering from verbal data = framework application of NLP


  ③ CONTRADICTION DETECTION (verbal vs behavioral):

    → Client nói: "Tôi không care về tiền" (verbal)
    → NHƯNG AI track: 70% quyết định client kể = optimize tiền
    → → Flag: possible disconnect giữa verbal schema và behavioral schema
    → = "PFC nói một đằng, body làm một nẻo" — AI detect MISMATCH

    → Client nói: "Tôi đã tha thứ cho bố" (verbal)
    → NHƯNG: mỗi lần nhắc "bố" → ngôn ngữ shift sang defensive
    → → Flag: verbal forgiveness vs body-level resentment still active

    → = Feeling.md v2.0 §2: Layer 7 (Explanation) = 20-70% accuracy
    → = AI detect khi Layer 7 CONFLICT với Layer 1-5 behavioral output

    🟢 Discrepancy detection = computational linguistics capability


  ④ SCHEMA CHAIN HYPOTHESIS GENERATION:

    → AI thấy pattern: client giúp đỡ compulsively
    → AI thấy pattern: client kể tuổi thơ bị bỏ rơi
    → AI thấy pattern: client rất negative khi "bị từ chối giúp"
    → → Hypothesis: "giúp đỡ" chain =
      help others → they need me → I am valuable → resolve "bị bỏ rơi"
    → → = Valence chain: help → identity ("needed") → abandonment schema resolve
    → = AI generate HYPOTHESIS cho chuyên gia VERIFY
    → = AI KHÔNG chẩn đoán — AI GỢI Ý

    ⚠️ Hypothesis CÓ THỂ SAI:
    → "Giúp đỡ" có thể KHÔNG link tới "bị bỏ rơi"
    → Có thể: đơn giản là mirror reward + positive childhood
    → = AI generate MULTIPLE hypotheses → chuyên gia chọn cái nào feel-check đúng

    🟡 Chain hypothesis from behavioral patterns = framework application


  ⑤ VALENCE PROPAGATION PATTERN DETECTION:

    → AI track: client positive về "toán" + positive về "tương lai"
    → AI track: client negative về "toán" NHƯNG positive về "tương lai"
      KHI nói "bố mẹ nói phải học"
    → → Detect: valence "toán" có thể = INSTALLED (qua chain) chứ không phải INTRINSIC
    → → Distinguish: "thích toán vì body reward" vs "học toán vì sợ bố mẹ"

    → = Valence-Propagation.md §4: AI detect WHICH propagation mechanism:
      Forward (intrinsic)? Install (inherited)? Threat (forced)?

    🟡 Valence propagation detection = novel framework application


  ⑥ ⭐ CHUNK DEPTH INFERENCE (insight từ session N+16):

    NGUYÊN LÝ:
      Schema verbalize được → IMPLY chunks đã tích lũy bên dưới.
      Chunks build TUẦN TỰ — KHÔNG skip tầng.
      → Biết OUTPUT (verbal complexity) → INFER INPUT (chunk depth)

    CÁCH LÀM:
      a) Verbal complexity → chunk depth estimation:
        → Client nói CHI TIẾT về domain X
          ("bức tranh đẹp ở composition, tone lạnh, nét cọ mạnh ở góc này")
          → Chunks hội họa = SÂU (color theory + technique + composition)
        → Client nói MƠ HỒ về domain Y
          ("bức tranh đẹp, tôi thích")
          → Chunks hội họa = NÔNG (body feel nhưng PFC chưa label)
        → = AI estimate chunk depth PER DOMAIN từ verbal complexity

      b) Prerequisite inference:
        → Client biết "lượng tử" → CHẮC CHẮN đã qua: đếm → số thực → số ảo → ...
        → = AI infer CHUNK TREE mà không cần hỏi từng cái
        → = Tiết kiệm thời gian, focus vào GAPS

      c) Gap detection:
        → Client biết X (complex) nhưng KHÔNG biết B (prerequisite OF X)
        → RED FLAG: schema có thể INSTALLED (verbal only) chứ không phải BUILT
        → VD: "Tôi biết phải tha thứ" (verbal) nhưng body VẪN giận
          → = Verbal schema WITHOUT chunk depth = shallow, dễ collapse
        → = Detect "biết bằng đầu" vs "biết bằng body"

      d) Body-verbal mismatch:
        → Client nói CHI TIẾT (verbal depth cao)
        → NHƯNG body language tense / defensive / flat
        → = Verbal chunks ĐỦ nhưng body schema CONFLICT
        → Flag cho chuyên gia: "check body response khi nói về X"

    🟡 Chunk depth inference = novel framework application
    🟢 Prerequisite knowledge structures = educational psychology (Ausubel 1968)
    🟢 Verbal fluency as expertise indicator = established


  AI LAYER — GIỚI HẠN:

    ✗ AI KHÔNG có body → KHÔNG feel-check
    ✗ AI KHÔNG biết body-base state → chỉ infer từ verbal/behavioral
    ✗ AI detect CORRELATION, không detect CAUSATION
    ✗ AI hypothesis CÓ THỂ HOÀN TOÀN SAI
    → = Output = APPROXIMATE MAP + HYPOTHESES
    → = CẦN Layer 2 (chuyên gia) để verify
    → = AI = CÔNG CỤ cho chuyên gia, KHÔNG THAY THẾ chuyên gia
```

---

## §4 — CHUYÊN GIA LAYER: Self-Pattern-Match + Body Vote

```
🟡 CHUYÊN GIA LÀM GÌ MÀ AI KHÔNG LÀM ĐƯỢC:

  ⭐ CORE MECHANISM: Self-Pattern-Match (Agent.md §0)

    Chuyên gia nhận hypothesis từ AI:
      "Client có thể có abandonment schema linking giúp đỡ → identity"

    Chuyên gia Self-Pattern-Match:
      → PFC retrieve SELF chunks matching client's described situation
      → Apply làm template: "nếu TÔI có abandonment fear, TÔI sẽ..."
      → Body CỦA CHUYÊN GIA simulate: feeling gì? drive gì? tránh gì?
      → Body vote: "hypothesis NÀY feel ĐÚNG không?"

    Output:
      → Body feel coherent → "có vẻ đúng, explore thêm"
      → Body feel incongruent → "không đúng, AI hypothesis sai"
      → Body feel ambiguous → "chưa rõ, cần thêm data từ client"


  TẠI SAO CHUYÊN GIA CÓ THỂ LÀM:

    ① CHUNKS TỪ NHIỀU CLIENTS:
      → Chuyên gia 10 năm → hàng nghìn cases → chunk library RẤT SÂU
      → Pattern recognition: "client NÀY giống client kia ở điểm..."
      → = Expertise = large trigger surface + many cross-links (Chunk.md v2.0 §4.4)
      → 🟢 Clinical expertise: pattern recognition across cases (Klein 1998)

    ② BODY CÓ THỂ SIMULATE:
      → Chuyên gia CÓ body → CÓ THỂ feel-check
      → AI KHÔNG CÓ body → KHÔNG thể feel
      → = Sự khác biệt CỐT LÕI giữa AI và chuyên gia
      → = Chuyên gia = body-checker, AI = pattern-detector

    ③ TRAINING QUAN SÁT:
      → Chuyên gia train: đọc body language, micro-expression, voice tone
      → = Thêm data NGOÀI verbal mà AI text-only KHÔNG CÓ
      → = Nếu AI có video/audio → CÓ THỂ supplement (tương lai)


  CHUYÊN GIA LÀM GÌ VỚI AI HYPOTHESIS:

    BƯỚC 1: Nhận AI patterns + hypotheses
    BƯỚC 2: Self-Pattern-Match từng hypothesis
    BƯỚC 3: CHỌN hypothesis feel most coherent
    BƯỚC 4: Design câu hỏi cho client để VERIFY:
      → "Khi nghĩ về [topic], bạn cảm thấy gì trong cơ thể?"
      → "Nếu [scenario], bạn TƯỞNG TƯỢNG mình sẽ..."
      → = Câu hỏi trigger body response CỦA CLIENT
      → = KHÔNG hỏi "tại sao" (PFC confabulate) → hỏi "cảm gì" (body report)
    BƯỚC 5: Observe client body response → confirm/deny


  CHUYÊN GIA — GIỚI HẠN:

    ✗ Chuyên gia CŨNG có schemas CỦA MÌNH → BIAS simulation
      → VD: chuyên gia có abandonment fear → OVER-detect abandonment ở client
    ✗ Chuyên gia chunk library CÓ HẠN → miss unusual patterns
      → Client từ culture KHÁC → chunks không match → simulation kém
    ✗ Chuyên gia chỉ nghe 1 giờ/tuần → miss long-term patterns
      → = AI BỔ SUNG ở đây (track patterns across sessions)
    ✗ Chuyên gia fatigue → quality GIẢM cuối ngày
      → AI KHÔNG fatigue → consistent

    → = Chuyên gia GIỎI nhưng KHÔNG hoàn hảo
    → = AI BỔ SUNG weakness của chuyên gia
    → = Chuyên gia BỔ SUNG weakness của AI
    → = 2 layers CẦN nhau

  🟢 Therapist empathy = Self-Pattern-Match (Goldman simulation theory)
  🟢 Therapist bias = established concern in clinical psychology
  🟢 Clinical pattern recognition = expertise research (Klein 1998)
  🟡 AI + Therapist complementary model = framework application
```

---

## §5 — CLIENT LAYER: Focusing + Self-Verify

```
🟡 CLIENT LÀ ULTIMATE VERIFIER:

  ⭐ CORE: Body CỦA CLIENT là thước đo CUỐI CÙNG.

  AI detect patterns → chuyên gia feel-check → NHƯNG:
    → AI KHÔNG phải client → có thể sai
    → Chuyên gia KHÔNG phải client → simulation approximate
    → CHỈ client CÓ body CỦA MÌNH → CHỈ client verify AUTHENTIC

  = Somatic-Articulation-Loop.md core insight:
    "Body biết trước khi PFC có từ.
     Articulation là PROCESS, không phải retrieval."


  CLIENT LÀM GÌ:

    ① NGHE hypothesis đã verify (từ chuyên gia):
      → "Có thể bạn giúp đỡ người khác liên quan tới sợ bị bỏ rơi"
      → Client NGHE → body PHẢN ỨNG NGAY (trước PFC process)

    ② BODY LISTEN (Focusing — Gendlin 1981):
      → Dừng lại. Lắng nghe body.
      → "Khi nghe câu đó, body tôi cảm gì?"
      → "Ngực nặng" → somatic response = schema SÂU confirmed ✅
      → "Vai gồng" → somatic response = schema SÂU confirmed ✅
      → "Không feel gì" → có thể suppressed (sâu) hoặc hypothesis sai

    ③ PFC ARTICULATE (Somatic-Articulation-Loop):
      → Body response → PFC TỪ TỪ tìm từ
      → "Nặng ở ngực... như sợ mất gì đó... à, sợ không ai cần mình"
      → = Body → felt sense → handle → articulate → INSIGHT
      → 🟢 Gendlin Focusing: 50+ years research tradition

    ④ CONFIRM/DENY/ADJUST:
      → Body confirm + PFC articulate match → hypothesis CONFIRMED
      → Body deny (no response / opposite response) → hypothesis REJECTED
      → Body partial (some match, some not) → hypothesis NEEDS ADJUSTMENT
      → = Client = FINAL JUDGE, nhưng cần GUIDE (AI + chuyên gia mở đường)


  FEELING LITERACY — PREREQUISITE CHO CLIENT LAYER:

    Feeling.md v2.0 §10 mô tả 5 stages:
      Stage 1: Body Awareness ("tôi cảm thấy... gì đó")
      Stage 2: Signal Discrimination ("khác nhau ở đâu?")
      Stage 3: Pattern Recognition ("mỗi lần gặp X → body Y")
      Stage 4: Label Attachment ("đây là sợ bị bỏ rơi")
      Stage 5: Meta-Feeling ("tôi đang sợ VÌ schema Z")

    Client ở Stage 1-2: CẦN chuyên gia guide nhiều
    Client ở Stage 3-4: CÓ THỂ self-verify cơ bản
    Client ở Stage 5: CÓ THỂ self-navigate (AI + occasional check)

    → = Feeling Literacy QUYẾT ĐỊNH client layer effective cỡ nào
    → = Training Feeling Literacy = TĂNG client self-verification capacity


  CLIENT — GIỚI HẠN:

    ✗ Client CÓ THỂ SUPPRESS (defense mechanism):
      → Schema quá đau → body TẮT response → "không feel gì"
      → = KHÔNG phải hypothesis sai → mà body CHẶN
      → = Chuyên gia cần RECOGNIZE suppression vs genuine no-match

    ✗ Client CÓ THỂ CONFABULATE (PFC bịa):
      → "Ừ đúng rồi, vì hồi nhỏ bố bỏ đi" → có thể POST-HOC rationalization
      → = PFC agree TOO FAST có thể = confabulation
      → = Body response CHẬM hơn PFC → real confirmation thường CẦN thời gian

    ✗ Client Feeling Literacy THẤP → verify KÉM:
      → "Tôi không biết body tôi cảm gì" → Layer 3 gần vô hiệu
      → = Cần TRAIN body awareness TRƯỚC khi verify sâu

    ✗ Client có thể MUỐN hypothesis đúng (confirmation bias):
      → "Tôi muốn có lý do rõ ràng" → accept hypothesis DÙ body không confirm
      → = Chuyên gia cần WATCH for too-easy acceptance

  🟢 Focusing = Gendlin 1981 (50+ years, multiple meta-analyses)
  🟢 Client self-report validity with body-awareness training = established
  🟡 5-stage Feeling Literacy as prerequisite = framework model
  🟡 Client as ultimate verifier = framework principle
```

---

## §6 — QUY TRÌNH THỰC HÀNH (Upgraded)

> Upgraded từ Schema-Diagnostic.md (backup) 5 bước.
> Thêm: AI role ở mỗi bước + valence chain detection + body check.

```
🟡 QUY TRÌNH 5 BƯỚC — 3 LAYERS TÍCH HỢP:


  ═══════════════════════════════════════════════════════════════
  BƯỚC 1: THU THẬP PATTERN (AI + Client)
  ═══════════════════════════════════════════════════════════════

  AI role:
    → Track verbal data across sessions (tháng → năm)
    → Tag: từ ngữ lặp, topic frequency, emotional tone per topic
    → Output: "Client nói về [X] 47 lần, 80% negative tone"

  Client role:
    → Kể chuyện tự nhiên (không cần structure)
    → Hỏi gợi (chuyên gia hoặc AI):
      "Ở work bạn thường thế nào?"
      "Khi stress bạn thường làm gì?"
      "Điều gì khiến bạn khó chịu nhất?"

  Chuyên gia role:
    → Observe body language, tone, micro-expression
    → Note: "client nói X nhưng body tense"

  Output bước 1:
    → 10-20 behavioral patterns (hành vi lặp lại)
    → AI: tagged by domain, frequency, tone
    → Chuyên gia: noted body-verbal mismatches

  ⚠️ THU HÀNH VI, KHÔNG THU LÝ DO
    → "Im lặng trong họp" = hành vi ✅
    → "Vì sợ nói sai" = lý do → CHƯA thu (PFC confabulate)


  ═══════════════════════════════════════════════════════════════
  BƯỚC 2: CLUSTER + CHAIN HYPOTHESIS (AI + Chuyên gia)
  ═══════════════════════════════════════════════════════════════

  AI role:
    → Cluster co-occurring patterns:
      "im lặng" + "tránh party" + "chỉ đi nếu có bạn thân"
      → Cluster: "tránh bị đánh giá bởi người không quen"
    → Detect contradictions:
      Client nói "không care tiền" NHƯNG 70% decisions = optimize tiền
    → Generate chain hypotheses:
      "Tránh đánh giá" + "phải làm hài lòng" → possible chain:
      "sợ bị reject" → "phải chứng minh giá trị" → behavior patterns
    → Chunk depth inference:
      Client nói CHI TIẾT về cooking → chunks cooking SÂU
      Client nói MƠ HỒ về relationships → chunks relationship NÔNG
      → Gap: cooking expert nhưng relationship beginner

  Chuyên gia role:
    → Nhận AI clusters + hypotheses
    → Self-Pattern-Match: "nếu tôi có pattern NÀY, tôi sẽ..."
    → Body vote: hypothesis nào feel coherent?
    → CHỌN 2-3 hypotheses most likely

  Output bước 2:
    → 2-3 schema chain hypotheses (ranked by plausibility)
    → Chuyên gia đã feel-check (Layer 2 verified)


  ═══════════════════════════════════════════════════════════════
  BƯỚC 3: BODY-CHECK VỚI CLIENT (Chuyên gia + Client)
  ═══════════════════════════════════════════════════════════════

  Chuyên gia role:
    → Trình bày hypothesis NHẸ NHÀNG (không áp đặt):
      "Có vẻ như khi bạn giúp người khác, có gì đó liên quan tới..."
    → Hỏi body-focused (KHÔNG hỏi "tại sao"):
      "Khi nghe câu đó, body bạn cảm gì?"
      "Có gì thay đổi ở ngực, vai, bụng không?"
    → Observe client body response TRƯỚC KHI client trả lời verbal

  Client role (Focusing):
    → Dừng lại. Lắng nghe body.
    → Report body sensation: "ngực nặng", "vai gồng", "bụng co"
    → HOẶC: "không feel gì" → có thể suppress hoặc hypothesis sai

  AI role (nếu có bio-data):
    → Track: HR tăng? Skin conductance? Voice pitch change?
    → = Bio-feedback supplement cho body-check

  Output bước 3:
    → Body confirm: hypothesis likely ĐÚNG → proceed
    → Body deny: hypothesis likely SAI → quay bước 2, thử hypothesis khác
    → Body ambiguous: cần thêm data → proceed carefully

  ⚠️ BODY RESPONSE CHẬM HƠN PFC:
    → Client nói "đúng rồi" TOO FAST → có thể confabulation
    → Body response thật thường CẦN 5-10 giây silence
    → Chuyên gia: cho THỜI GIAN, đừng rush


  ═══════════════════════════════════════════════════════════════
  BƯỚC 4: PREDICT + VERIFY (AI + Chuyên gia + Client)
  ═══════════════════════════════════════════════════════════════

  Schema hypothesis CONFIRMED → dùng nó PREDICT hành vi ở domain KHÁC:

  AI role:
    → Generate predictions từ hypothesis:
      Nếu "sợ bị reject" → predict: "sợ thử cái mới", "discount lời khen"
    → Check: past data CÓ support predictions không?
      → "Client nói 'tôi sợ thử cái mới' ở session 8" → MATCH ✅

  Chuyên gia role:
    → Hỏi client về domains CHƯA discuss:
      "Khi thử cái mới, bạn thường thế nào?"
      "Khi được khen, bạn cảm thấy sao?"
    → Compare response vs prediction

  Client role:
    → Trả lời thật → body-check nếu cần

  Scoring:
    → 5 predictions → 4+ match → schema hypothesis LIKELY đúng ✅
    → 5 predictions → 2-3 match → PARTIALLY đúng → adjust
    → 5 predictions → 0-1 match → hypothesis SAI → quay bước 2

  ⚠️ KHÔNG BAO GIỜ "chắc chắn đúng" — chỉ "likely đúng"
    → Tiếp tục verify qua thời gian
    → Schema THAY ĐỔI → hypothesis cần update


  ═══════════════════════════════════════════════════════════════
  BƯỚC 5: HƯỚNG CAN THIỆP (Chuyên gia + Client)
  ═══════════════════════════════════════════════════════════════

  Schema hypothesis VERIFIED → fix Ở ĐÂU trong gradient:

  FIX SÂU (body baseline — hiệu quả nhất, chậm nhất):
    → Body-level: exercise, sleep, nutrition, safe environment
    → Somatic therapy: body-focused processing
    → Timeline: tháng → năm
    → Effect: MỌI gradient levels TỰ adjust

  FIX GIỮA (schema chain — hiệu quả vừa):
    → Identify chain links: A→B→C→body-base
    → STRENGTHEN hoặc WEAKEN specific links
    → Competitive re-linking (Chunk.md v2.0 §4.3)
    → Timeline: tuần → tháng

  FIX NÔNG (domain skills — nhanh nhất):
    → Skill training domain cụ thể
    → Behavior practice: thử hành vi mới
    → Timeline: ngày → tuần
    → Effect: CHỈ domain đó

  THỨ TỰ:
    → Crisis: fix nông TRƯỚC (cần kết quả NGAY)
    → Long-term: fix sâu TRƯỚC (bền vững)
    → Ideal: sâu + nông ĐỒNG THỜI

  AI role ở bước 5:
    → Track progress: "client dùng từ negative về X GIẢM 30% sau 3 tháng"
    → Alert: "pattern cũ RE-APPEAR" → có thể schema chưa resolve ở body level
    → = AI monitor DÒNG thời gian mà chuyên gia chỉ thấy ĐIỂM
```

---

## §7 — HONEST ASSESSMENT

```
VERIFIED (🟢):

  Foundation:
    → NLP sentiment analysis, topic modeling = existing technology
    → Verbal fluency as expertise indicator = established
    → Prerequisite knowledge structures: Ausubel 1968
    → Discrepancy detection in text = computational linguistics
    → Multi-method assessment: Campbell & Fiske 1959
    → Therapeutic alliance + client self-report: Lambert 2013
    → Focusing: Gendlin 1981 (50+ years)
    → Clinical pattern recognition: Klein 1998
    → Simulation theory of empathy: Goldman
    → Therapist bias: established concern
    → Body-awareness training improves self-report: established
    → Bounded rationality: Simon 1955, Kahneman 2011

FRAMEWORK REASONING (🟡):

  Architecture:
    → 3-layer model (AI + Expert + Client): framework application
    → 6 AI capabilities: framework application of existing NLP
    → Chunk depth inference from verbal output: novel, logical
    → Upgraded 5-step process: refined from Schema-Diagnostic.md
    → "Navigate, not GPS": framework principle
    → 3-capability model (pattern, cluster, suggest): derived

  Mechanism:
    → Self-Pattern-Match for therapy: Agent.md applied
    → Feeling Literacy as prerequisite: Feeling.md v2.0 applied
    → Valence chain detection: Valence-Propagation.md applied
    → Body-check integration: Somatic-Articulation-Loop.md applied

HYPOTHESIS (🔴):

    → AI CAN effectively detect schema patterns from therapy text:
      Logical + technology exists, NHƯNG chưa có systematic study
      testing AI schema detection vs expert-only vs combined.

    → 3-layer model IMPROVES outcomes vs 1-2 layers:
      Logical, nhưng chưa có RCT comparing approaches.

    → Chunk depth inference from verbal complexity is RELIABLE:
      Promising, nhưng verbal complexity ≠ chunk depth always
      (people can parrot complex language WITHOUT understanding).

    → Gap detection (verbal without body-compile) is DETECTABLE by AI:
      Requires subtle linguistic cues that may be below AI detection threshold.

    → Bio-data supplement ADDS meaningful signal:
      HRV, skin conductance exist as measures, nhưng noise-to-signal ratio
      in real therapy context = CHƯA RÕ.


CÂU HỎI MỞ:

    → Privacy: therapy data + AI = sensitive. Security? Consent? Ownership?
    → Bias: AI trained on WHICH population? Western? Asian? Mixed?
    → Cultural: schema patterns KHÁC across cultures → AI cần calibrate?
    → Cost: AI infrastructure cho therapy = accessible? Affordable?
    → Regulation: AI-assisted therapy = legal framework nào?
    → Harm: AI wrong hypothesis → client trust AI quá → damage?
    → Training: chuyên gia cần TRAIN gì để work with AI effectively?
```

---

## §8 — CROSS-REFERENCES + STATUS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Valence-Propagation.md v1.0 §8 — "Navigate, not GPS" + mở cửa ứng dụng
    → Schema.md v1.1 §1.2 — "KHÔNG THỂ phân tích chính xác"
    → Feeling.md v2.0 §2 — 7-layer fidelity gradient (Layer 7 = 20-70%)
    → Feeling.md v2.0 §10 — Feeling Literacy 5-stage + AI era
    → Chunk.md v2.0 §4 — activation dynamics, trigger surface, competitive re-linking

  MECHANISM:
    → Agent.md §0 — Self-Pattern-Match (chuyên gia simulate)
    → Drive.md v1.1 §2 — 6 PFC Modes (spinning vs resolve = chunks)
    → Somatic-Articulation-Loop.md — body-knowledge → explicit (Focusing, AI catalyst)
    → Valence-Propagation.md §4-§5 — propagation 4 mechanisms + 5 chain properties

  TIỀN THÂN (backup):
    → Schema/backup/Schema-Diagnostic.md — quy trình 5 bước gốc (upgraded ở §6)

  LIÊN QUAN:
    → Body-Input-Enumeration.md — L0/L1/L3 channels (body-base targets)
    → Anchor-Schema.md — anchor sync point (schema detection includes anchor identification)
    → Emergent-Patterns.md §5 — "Cho đi" pattern (example of hidden valence chain)


STATUS:

  v1.0 — 2026-04-18 — Session N+16

  Sections:
    §0  Position trong framework
    §1  Giới hạn nền tảng (đặt kỳ vọng)
    §2  3-Layer Model (AI + Expert + Client)
    §3  AI Layer: 6 capabilities (pattern tracking, clustering, contradiction,
        chain hypothesis, valence propagation, ⭐chunk depth inference)
    §4  Chuyên gia Layer: Self-Pattern-Match + body vote
    §5  Client Layer: Focusing + self-verify + Feeling Literacy prerequisite
    §6  Quy trình 5 bước (upgraded: AI role + body-check + chain detection)
    §7  Honest assessment (🟢🟡🔴)
    §8  Cross-references + Status

  Confidence:
    🟢 Foundation technologies (NLP, Focusing, expertise research)
    🟡 3-layer architecture, 6 AI capabilities, upgraded process
    🔴 AI schema detection effectiveness, chunk depth inference reliability,
        3-layer outcome improvement vs alternatives

  Next:
    → Test: pilot AI-assisted therapy session (if opportunity)
    → Privacy/ethics framework for therapy AI
    → Cultural calibration: schema patterns across cultures
    → Training protocol: chuyên gia + AI collaboration
```
