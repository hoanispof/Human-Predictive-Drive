---
title: AI-Schema-Detection — AI Hỗ Trợ Nhận Diện Schema + Compile Type + Collective Context
version: 2.0
created: 2026-04-18
updated: 2026-05-08 (v2.0 — compile type detection, collective chain, self-drill mode, AI trust guardrails)
status: v2.0 — GATEWAY FILE (cửa ngõ tiếp cận framework qua ứng dụng thực hành)
scope: |
  HOW AI có thể hỗ trợ nhận diện schema patterns + compile type + collective context.
  3-layer model: AI detect → Chuyên gia feel-check → Client self-verify.
  2-layer simplified: AI detect → Client self-verify (cho mild cases).
  9 AI capabilities: ①-④⑥⑦ (giữ v1.1) + ⑤ compile type (upgrade) + ⑧⑨ (mới).
  Self-Drill Mode: user + AI, không cần expert cho một số case.
  AI Trust Guardrails: tool chính nó có thể install patterns → cần guardrails.
  Fundamental limits: approximate, KHÔNG chính xác tuyệt đối.
  GATEWAY: file này = entry point cho practical use of framework.
purpose: |
  Cầu nối framework lý thuyết → thực hành hỗ trợ.
  Ứng dụng trực tiếp từ Valence-Propagation.md v1.4 §8 ("Mở cửa cho AI-Schema-Detection").
  Không phải tool AI cụ thể — mà là KIẾN TRÚC cho AI-assisted schema navigation.
  GATEWAY ROLE: người đọc không cần hiểu toàn bộ framework trước — file này
  dẫn dắt từ ứng dụng thực tế → hiểu framework tự nhiên.
  v2.0 KEY UPGRADES (DỰA TRÊN Drill S1-S12 findings):
    ⑤ Compile Type Detection (A/B/C) — detect SOURCE of pattern
    ⑧ Collective Chain Break Detection — individual vs collective
    ⑨ 3 Cấp Detection — tag mỗi finding: Cấp 1/2/3
    §7 Self-Drill Mode — user + AI, không cần expert cho mild cases
    §8 AI Trust Guardrails — AI output = Loại C install → paradox
sources: |
  Valence-Propagation.md v1.4 §4 — clarification: VP chains = explanatory (Cấp 3)
  Valence-Propagation.md v1.4 §8 — fundamental limits + 3 nguyên tắc + mở cửa ứng dụng
  Schema.md v2.0 §2 (software analogy), §6.3 ("KHÔNG THỂ phân tích chính xác")
  Compile-Taxonomy.md v1.0 §3 — 4 compile pathways (source for ⑤ upgrade)
  Collective-Body.md v1.1 §5.2 — chain break (source for ⑧)
  Collective-Body.md v1.1 §8.4 — AI trust entity (source for §8 guardrails)
  Collective-Body.md v1.1 §1 — Model 3 cấp (source for ⑨)
  Body-Base.md v2.0 §6 — 4-tier calibration, domain feedback = final arbiter
  Body-Base.md v2.0 §7 — circuit breaker mechanism
  PFC-Function.md v1.1 §6 — confabulation = rule not exception (GAP 10)
  Feeling.md v2.0 §10 — Feeling Literacy 5-stage (client prerequisite)
  Agent-Mechanism.md §0 — Self-Pattern-Match (chuyên gia simulate client)
  Somatic-Articulation-Loop.md — body-knowledge → explicit (Focusing, AI catalyst §5)
  Modality.md v1.0 §3 — chunk depth = modality count (★1-★5)
  Chunk.md v2.1 §2.3 — trust gate, external install mechanisms
  Drill E5 Q-S2-5 — AI trust insights (E5-16→E5-20)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# AI-Schema-Detection — AI Hỗ Trợ Nhận Diện Schema + Compile Type + Collective Context

> **Bạn nói: "Tôi thích từ thiện."**
> **AI nghe 100 giờ nói chuyện của bạn.**
> **AI thấy: mỗi khi nói "giúp đỡ", bạn cũng nói "mẹ", "tuổi thơ", "bị bỏ rơi".**
> **AI gợi ý: "giúp đỡ" có thể link với "chứng minh tôi cần thiết".**
> **AI thêm: compile source có thể = Loại C (mẹ install "con phải giúp người").**
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
> **NHƯNG: chính AI cũng có thể install patterns vào bạn qua trust.**
> **→ Body-check AI output = CÙNG nguyên tắc body-check mọi thứ.**
>
> **"Công cụ NAVIGATE, không phải GPS chính xác."**

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — GIỚI HẠN NỀN TẢNG
- §2 — 3-LAYER MODEL + 2-LAYER SIMPLIFIED
- §3 — AI LAYER: 9 Capabilities
- §4 — CHUYÊN GIA LAYER: Self-Pattern-Match + Body Vote
- §5 — CLIENT LAYER: Focusing + Self-Verify
- §6 — QUY TRÌNH THỰC HÀNH (Upgraded v2.0)
- §7 — SELF-DRILL MODE (User + AI)
- §8 — AI TRUST GUARDRAILS
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES + STATUS

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 AI-SCHEMA-DETECTION TRONG KIẾN TRÚC:

  Framework đã xác lập (Valence-Propagation.md v1.4 §8):
    → Schema vô tận, chain không thể map chính xác
    → NHƯNG: KHÔNG CẦN chính xác tuyệt đối
    → CÓ THỂ: nhận diện PATTERN, ước lượng NHÓM, suggest HƯỚNG
    → = "Công cụ NAVIGATE, không phải GPS chính xác"

  File NÀY = ỨNG DỤNG nguyên tắc đó:
    → HOW nhận diện patterns trong thực tế?
    → AI role + Chuyên gia role + Client role = gì?
    → Quy trình THỰC HÀNH upgraded từ Schema-Diagnostic.md
    → v2.0: + Compile Type Detection + Collective Context + Self-Drill Mode

  ⭐ GATEWAY ROLE:
    File này = CỬA NGÕ để tiếp cận framework.
    Người đọc KHÔNG CẦN hiểu toàn bộ framework trước.
    Đọc file này → thấy ứng dụng thực tế → TỰ NHIÊN muốn hiểu sâu hơn.
    = Từ "AI có thể giúp gì?" → dẫn vào schema → chunks → body-base → cycle.
    = Entry point cho practical use.

  ⭐ CẤP PHÂN TÍCH (VP v1.4 §4 clarification, Drill §6):
    VP §4 chains = GIẢI THÍCH (Cấp 3), không phải cách brain PROCESS.
    File này hoạt động ở 2 cấp:
      CẤP 1 (Detect): AI observe behavioral patterns → infer schema clusters
      CẤP 3 (Analyze): AI + Expert phân tích tại sao patterns hoạt động
    KHÔNG claim phát hiện "cách brain process bên trong" (Cấp 1 internal).
    = Đặt kỳ vọng ĐÚNG cho cả AI lẫn người dùng.

  INSIGHT NỀN TẢNG (Schema.md v2.0 §2):
    Phần mềm: không ai biết bên trong chứa hàm gì.
    Nhưng người đủ kinh nghiệm observe phần mềm chạy → biết kỹ thuật viết.
    Não: không ai biết bên trong chứa chunks gì.
    Nhưng AI + chuyên gia observe behavior → CÓ THỂ infer chunk composition.
    = Cùng nguyên lý: INFER internal structure từ external behavior.
    (Chi tiết: §3 Software Analogy Bridge)

  Flow:
    Valence-Propagation.md v1.4 §8 (lý thuyết: giới hạn + mở cửa)
         │
         ▼
    ┌─────────────────────────────────────────────────────────┐
    │ AI-SCHEMA-DETECTION.MD (FILE NÀY) — GATEWAY             │
    │                                                          │
    │   §1: Giới hạn (đặt kỳ vọng ĐÚNG)                      │
    │   §2: 3-Layer Model + 2-Layer Simplified                │
    │   §3-§5: Chi tiết mỗi layer (⑨ khả năng AI)            │
    │   §6: Quy trình thực hành (upgraded v2.0)               │
    │   §7: Self-Drill Mode (user + AI)                       │
    │   §8: AI Trust Guardrails                               │
    └─────────────────────────────────────────────────────────┘
         │
         ▼
    Ứng dụng cụ thể:
      → Therapy (chuyên gia tâm lý + AI) — 3-layer mode
      → Self-development (tự calibrate + AI) — 2-layer mode (§7)
      → Education (giáo viên + AI detect learning patterns)
      → Workplace (coaching + AI behavioral analysis)
```

---

## §1 — GIỚI HẠN NỀN TẢNG

```
🟡 NHẮC LẠI — TẠI SAO KHÔNG THỂ CHÍNH XÁC:

  Schema.md v2.0 §6.3 đã xác lập:
    ① 86 tỷ neurons × ~100 nghìn tỷ connections = quá lớn để đọc
    ② Schema = multi-modal (verbal chỉ ~1/6 schema thật)
    ③ Schema SÂU = body adaptation (cortisol, muscle tension, gut state)
       → Chính người đó CŨNG không biết
    ④ Schema thay đổi liên tục
    ⑤ Khoa học chưa đủ công cụ

  Valence-Propagation.md v1.4 §8 thêm:
    ⑥ Valence chain = schema × schema × links = vô tận × vô tận
    ⑦ PFC accuracy giảm theo chain length (confabulation)
    ⑧ Body check OUTPUT, không check TRUTH

  v2.0 thêm (DỰA TRÊN Drill S1-S12):

    ⑨ VP §4 CHAINS = EXPLANATORY, KHÔNG PHẢI PROCESSING:
       VP §4 chain analysis [toán → điểm → đại học → việc → lương → body-base]
       = Cấp 3 (framework giải thích tại sao behavior hoạt động).
       KHÔNG phải cách brain PROCESS ở Cấp 1 — cá nhân compile SHORT (1-2 nodes).
       Chain dài SỐNG ở Cấp 2 (collective infrastructure hold cho cá nhân).
       → AI detect BEHAVIOR PATTERNS (Cấp 1 detect), không detect "cách brain process"
       → Chain analysis CÓ GIÁ TRỊ: chẩn đoán chain gãy, thiết kế collective, verify trust
       → NHƯNG chain analysis ≠ mô tả processing thật của brain
       → = Đặt kỳ vọng ĐÚNG: AI + Expert PHÂN TÍCH chains, KHÔNG phải THẤY chains
       (Source: VP v1.4 §4 clarification, Drill §6 + §22, Collective-Body.md §1)

    ⑩ AI OUTPUT = LOẠI C INSTALL VÀO USER QUA TRUST:
       AI suggest "bạn có pattern X" → user trust AI → PFC accept → body compile
       = CÙNG CƠ CHẾ bố mẹ install "con phải ngoan" (Chunk.md §2.3)
       Vừa detect schema VỪA CÓ THỂ install schema → paradox
       "Navigate, not GPS" áp dụng cho CHÍNH AI output
       → Body-check AI output = BẮT BUỘC (chi tiết: §8 AI Trust Guardrails)
       (Source: Collective-Body.md v1.1 §8.4, Drill E5 E5-16→E5-20)

  → TỔNG: schema network KHÔNG THỂ map chính xác từ bên ngoài.
    + AI CÓ THỂ install pattern MỚI → cần cẩn thận GẤP ĐÔI.


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
      → "Abandonment fear" → có thể link tới connection drive deficit
      → Suggest: strengthen connection TRƯỚC, conflict skill SAU
      → = Hướng ≠ đáp án. Cần verify qua body-check.

  🟡 3-capability model = derived from Schema.md + Valence-Propagation.md
  🟢 "Navigate, not GPS" = consistent with bounded rationality (Simon 1955)
```

---

## §2 — 3-LAYER MODEL + 2-LAYER SIMPLIFIED

```
🔴 HYPOTHESIS — application architecture, logic consistent, chưa test systematic

  ⭐ KHÔNG AI LAYER NÀO ĐỦ MỘT MÌNH:

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  LAYER 1: AI PATTERN DETECTOR                               │
  │    Input: verbal data, behavioral patterns, (optional) bio   │
  │    Process: NLP, clustering, contradiction detection         │
  │    Output: schema map SƠ LƯỢC + hypotheses                  │
  │         + compile type classification (A/B/C) ← v2.0        │
  │         + collective context flag ← v2.0                     │
  │    Strength: NHANH, RỘNG, không bỏ sót pattern              │
  │    Weakness: KHÔNG CÓ BODY → KHÔNG feel-check               │
  │    Confidence: LOW-MEDIUM (pattern ≠ causation)              │
  │                                                              │
  │         │ hypotheses + patterns + compile type                │
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
      → PFC confabulate (PFC-Function.md v1.1 §6)
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

```
  ⭐ 2-LAYER SIMPLIFIED MODE: AI + SELF (v2.0 NEW):

  3-layer model = LÝ TƯỞNG. NHƯNG không phải lúc nào cũng CẦN chuyên gia.

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  LAYER 1: AI PATTERN DETECTOR (giữ nguyên)                  │
  │         │                                                    │
  │         ▼ (bỏ qua Layer 2 — không có chuyên gia)            │
  │                                                              │
  │  LAYER 3: USER SELF-VERIFIER                                │
  │    Process: Body listen + PFC articulate (self-guided)       │
  │    = User TỰ body-check AI suggestions                      │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘

  KHI NÀO AN TOÀN (2-layer OK):
    → Mild exploration: "tại sao tôi chán công việc?"
    → General patterns: "tôi hay trì hoãn, tại sao?"
    → Self-development: "tôi muốn hiểu bản thân hơn"
    → Feeling Literacy ≥ Stage 3 (Feeling.md v2.0 §10):
      user CÓ KHẢ NĂNG tự body-check cơ bản
    → Không có crisis, không có trauma active

  KHI NÀO PHẢI CÓ CHUYÊN GIA (3-layer bắt buộc):
    → Trauma: PTSD, abuse, neglect, violent events
    → Crisis: suicidal ideation, self-harm, acute breakdown
    → Deep pathology: severe depression, psychosis, addiction
    → Feeling Literacy < Stage 2: user KHÔNG THỂ tự body-check
    → AI detect RED FLAGS: language suggesting danger → NGAY LẬP TỨC refer

  TẠI SAO MỞ RỘNG:
    → KHÔNG PHẢI ai cũng access chuyên gia (cost, geography, stigma)
    → Mild cases = phần lớn nhu cầu self-understanding
    → AI + body-check = BETTER than nothing, WORSE than full 3-layer
    → = Mở rộng accessibility NHƯNG với ranh giới RÕ RÀNG
    → Chi tiết: §7 — Self-Drill Mode

  🟡 2-layer simplified = framework extension
  🟢 Self-help with guided reflection = established (bibliotherapy research)
  🔴 Safety boundaries for AI self-help: chưa test systematic
```

---

## §3 — AI LAYER: 9 Capabilities

```
🟡 ANALOGY PHẦN MỀM — TẠI SAO AI CÓ THỂ INFER CHUNKS TỪ SCHEMA:

  Schema.md v2.0 §2 xác lập:
    → Phần mềm: "hàm" = đơn vị tính toán thật. "Tính năng" = cách mô tả từ bên ngoài.
    → Não: chunks = đơn vị tính toán thật. Schema = cách mô tả chunk networks từ bên ngoài.

  MỞ RỘNG CHO AI-SCHEMA-DETECTION:

    PHẦN MỀM — người ĐỦ KINH NGHIỆM observe:
      → Nhìn game chạy → user bình thường chỉ thấy "tính năng"
      → NHƯNG dev 10 năm observe game → biết:
        "Dùng physics engine XYZ" (từ cách vật thể rơi)
        "Dùng pathfinding A*" (từ cách NPC di chuyển)
        "Dùng ECS architecture" (từ performance pattern)
      → Dev KHÔNG thấy source code → nhưng INFER internal structure từ BEHAVIOR
      → Cùng 1 game: user thấy "tính năng shop" → dev thấy "database + API + cache"

    NÃO — AI + chuyên gia observe:
      → Nghe client nói → user bình thường chỉ thấy "tính cách"
      → NHƯNG AI + chuyên gia observe behavior → biết:
        "Schema abandonment" (từ cách react khi bị từ chối)
        "Chunks relationship NÔNG" (từ verbal complexity thấp về domain này)
        "Prerequisite chain toán SÂU" (từ việc client giải thích được cơ học lượng tử
          → CHẮC CHẮN đã compile chunks: đếm → đại số → giải tích → số ảo → ...)
      → AI KHÔNG thấy chunks → nhưng INFER chunk composition từ SCHEMA BEHAVIOR

    ⭐ NGUYÊN LÝ CHUNG:
      → Observer KHÔNG CẦN thấy internal structure
      → Observer CHỈ CẦN: ① đủ kinh nghiệm ② observe behavior đủ lâu
      → → CÓ THỂ infer internal structure từ external behavior
      → AI = observer có ① vô hạn knowledge ② vô hạn patience ③ perfect memory
      → → AI = IDEAL candidate cho inference NÀY

    ⚠️ NHƯNG: inference ≠ certainty
      → Dev GIỎI cũng SAI (nghĩ dùng Unity hóa ra dùng Godot)
      → AI inference cũng CÓ THỂ SAI
      → → Cần Layer 2 + Layer 3 verify

  🟡 Software analogy = Schema.md v2.0 §2 applied to AI detection
  🟢 Reverse engineering from behavior = established (software engineering, clinical psych)


🟡 AI CÓ THỂ LÀM GÌ — 9 KHẢ NĂNG CỤ THỂ:


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

    ⚠️ Chain hypothesis = CẤP 3 analysis (explanatory):
    → AI generate chain DÀI = mô tả tại sao pattern TỒN TẠI
    → KHÔNG phải claim brain process chain đó (VP v1.4 §4 clarification)
    → GIÁ TRỊ: chẩn đoán + hướng can thiệp. KHÔNG phải "đây là cách não nghĩ."

    🟡 Chain hypothesis from behavioral patterns = framework application


  ⑤ ⭐ COMPILE TYPE DETECTION — A/B/C (v2.0 UPGRADE):

    v1.1: "Valence Propagation Pattern Detection" — detect positive/negative/installed
    v2.0: UPGRADE → detect COMPILE SOURCE (WHY pattern tồn tại)

    NGUYÊN LÝ (Compile-Taxonomy.md v1.0 §3):
      Cùng output ("đi học toán") nhưng 4 COMPILE PATHWAYS khác nhau:
        ① Hardware Fit (Loại A — direct): body tự reward
        ② Trust + Moderate Fit (Loại C+A — compound): trust install + verify
        ③ Social Default (Loại C — installed pure): "ai cũng làm"
        ④ Threat Avoidance (Loại A — threat): avoid negative
      = CÙNG HÀNH VI, KHÁC CƠ CHẾ → khác hướng can thiệp HOÀN TOÀN.

    AI DETECT COMPILE TYPE TỪ VERBAL SIGNALS:

      Loại A — Hardware Fit (direct experience):
        Signal: "tôi thích X", "vui khi làm X", "tự nhiên muốn"
        + body language match (relaxed, engaged khi nói về X)
        + verbal DETAIL cao về X (chunks SÂU = multi-modal compile)
        = Genuine direct experience → body-compiled
        PFC accuracy ~90%: "tôi thích toán" = ĐỦ TIN

      Loại A — Threat (direct avoidance):
        Signal: "phải/sợ/tránh/không thể", "nếu không... thì..."
        + body tense khi nói về topic
        + language focused on AVOIDING negative, không PURSUING positive
        = Threat-driven pattern → cortisol-tagged compile
        PFC accuracy ~90%: "tôi sợ bị mắng" = ĐỦ TIN

      Loại C — Trust Install:
        Signal: "bố mẹ nói/thầy bảo/mọi người đều"
        + "đương nhiên/bình thường/ai cũng biết"
        + verbal NÔNG về X (nhận từ trust, chưa compile deep)
        + HOẶC: client KHÔNG BIẾT tại sao mình tin (post-hoc confabulate)
        = Installed via trust source → may or may not match body
        PFC accuracy ~30-60%: confabulation PHỔ BIẾN NHẤT

      Loại C — Social Default:
        Signal: "mọi người đều... nên tôi cũng..."
        + "bình thường/đương nhiên/tự nhiên vậy"
        + KHÔNG kèm personal experience mạnh
        + Trust source = QUANTITY (social proof) thay vì QUALITY (specific person)
        = Social environment → auto-conform, minimal body experience
        PFC accuracy: THẤP NHẤT (~30%) — "tôi thích X" có thể = "xã hội nói X tốt"

      Loại B — Compiled Expertise:
        Signal: chi tiết SÂU + nhiều domain-specific terms
        + logical structure phức tạp + cross-references between concepts
        + "tôi ĐÃ THỬ/ĐÃ KIỂM TRA/ĐÃ KINH NGHIỆM" + kết quả cụ thể
        = Expertise compile (repetition + PFC-directed + verify qua domain feedback)

    ⭐ TẠI SAO QUAN TRỌNG:
      Cùng output "tôi thích toán" nhưng 4 pathways:
        ① Hardware Fit → toán fit brain → genuine → NÊN khuyến khích
        ② Trust Install → mẹ nói học toán tốt → installed → cần CHECK body confirm
        ③ Social Default → ai cũng học toán → auto → có thể KHÔNG fit
        ④ Threat → sợ bị mắng nếu không học → avoidance → CẦN remove threat
      → KHÁC HƯỚNG CAN THIỆP cho từng compile type:
        ① → Nurture, không cần can thiệp
        ② → Verify: body có confirm không? Nếu có → ①② compound (lý tưởng)
        ③ → Explore: thật sự fit không? Hay chỉ follow xã hội?
        ④ → Address threat source, không fix "sự quan tâm tới toán"

    ⚠️ MIXED TYPE PHỔ BIẾN:
      Phần lớn adult behavior = A × C overlap (Compile-Taxonomy.md §7.1)
      VD: [ăn ngon → ấm] = Loại A, NHƯNG "ngon" = partially Loại C (cultural)
      → AI classify DOMINANT type, not absolute
      → Chuyên gia verify mix nào đang active

    Source: Compile-Taxonomy.md v1.0 §3 (4 compile pathways, Drill §22A)
    🟡 Compile type detection = novel framework application
    🟢 Approach vs avoidance motivation: Elliot 2006
    🟢 Social proof: Cialdini 1984


  ⑥ ⭐ CHUNK DEPTH INFERENCE (insight từ session N+16, enriched N+19):

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

      b) Prerequisite inference (CHAIN SÂU):
        → Client biết "lượng tử" → CHẮC CHẮN đã qua: đếm → số thực → số ảo → ...
        → = AI infer CHUNK TREE mà không cần hỏi từng cái
        → = Tiết kiệm thời gian, focus vào GAPS

        VD — prerequisite chain DEPTH:
          Học sinh biết cộng trừ nhân chia
            → CHẮC CHẮN đã có chunks đếm 1-10
            → Prerequisite chain: đếm → cộng → trừ → nhân → chia
            → AI infer: ít nhất 5 tầng chunks toán cơ bản

          Sinh viên biết lượng tử
            → CHẮC CHẮN thành thạo: số thực, số ảo, đại số tuyến tính, giải tích
            → Prerequisite chain: đếm → algebra → calculus → linear algebra → quantum
            → AI infer: ít nhất 10+ tầng chunks toán + physics
            → DEPTH = rất sâu trong domain này

      c) ⚠️ DOMAIN-SPECIFIC LIMIT:
        → Chuyên gia toán xuất sắc ≠ biết bơi
        → Chunks toán SÂU → KHÔNG predict chunks thể thao
        → Chunks compile DOMAIN-SPECIFIC (Modality.md §3: depth = modality count)
        → Verbal modality SÂU (toán) ≠ motor modality SÂU (bơi)
        → = AI PHẢI infer PER DOMAIN, KHÔNG generalize across domains
        → = Nguyên lý: chunk depth = vertical (trong 1 domain), KHÔNG horizontal

      d) Gap detection:
        → Client biết X (complex) nhưng KHÔNG biết B (prerequisite OF X)
        → RED FLAG: schema có thể INSTALLED (verbal only) chứ không phải BUILT
        → VD: "Tôi biết phải tha thứ" (verbal) nhưng body VẪN giận
          → = Verbal schema WITHOUT chunk depth = shallow, dễ collapse
          → = SAL §1.3: "Explicit giả" — verbal chunks without body-confirm
        → = Detect "biết bằng đầu" vs "biết bằng body"

      e) Body-verbal mismatch:
        → Client nói CHI TIẾT (verbal depth cao)
        → NHƯNG body language tense / defensive / flat
        → = Verbal chunks ĐỦ nhưng body schema CONFLICT
        → Flag cho chuyên gia: "check body response khi nói về X"

      f) Modality depth profile:
        → Modality.md §3: chunk depth = số modalities encode
        → ★1 (verbal only) → ★5 (visual + auditory + somatic + motor + emotional)
        → AI CÓ THỂ estimate modality profile từ HOW client mô tả:
          "Tôi biết tha thứ là đúng" → ★1 verbal only
          "Khi nghĩ tới tha thứ, ngực tôi nhẹ hơn" → ★2-3 verbal + somatic
          "Tôi thấy mặt mẹ, nghe giọng bà, tim đập nhẹ" → ★4-5 multi-modal
        → Modality profile = proxy cho chunk depth THẬT

    🟡 Chunk depth inference = novel framework application
    🟢 Prerequisite knowledge structures = educational psychology (Ausubel 1968)
    🟢 Verbal fluency as expertise indicator = established
    🟡 Domain-specific limit = Modality.md §3 applied
    🟡 Modality depth profile = novel estimation method


  ⑦ ⭐ AI KHƠI GỢI SCHEMA ẨN (insight từ session N+19):

    VẤN ĐỀ:
      → Người dùng KHÔNG THỂ verbalize hết schema của mình
      → Thậm chí KHÔNG BIẾT họ có schema rất sâu
      → SAL §1.4: "We can know more than we can tell" (Polanyi 1958)
      → Implicit knowledge >> explicit knowledge (tỷ lệ ~100:1 hoặc hơn)
      → = HẦU HẾT schema nằm DƯỚI ngưỡng conscious awareness

    TẠI SAO XẢY RA:
      → Schema SÂU = body adaptation (cortisol, muscle patterns, gut state)
      → Chạy VÔ THỨC → PFC không observe → KHÔNG có label
      → Schema quá quen → habituation → VTA không fire → "invisible"
      → Giống NƯỚC với CÁ: cá không biết mình đang ở trong nước
      → = Schema càng sâu, càng pervasive → càng invisible với chủ nhân

    AI KHƠI GỢI NHƯ THẾ NÀO:

      a) Pattern surfacing (từ data lớn):
        → AI track 100+ giờ conversation
        → AI phát hiện patterns MÀ CLIENT VÀ CHUYÊN GIA ĐỀU KHÔNG THẤY
        → VD: "Mỗi khi nói về tương lai, client dùng giọng NHẸ HƠN"
          → Client không biết (quá quen)
          → Chuyên gia miss (chỉ nghe 1 giờ/tuần)
          → AI: "pattern NÀY consistent 47/50 sessions" → surface!

      b) Cross-domain connection:
        → AI detect: client nói "sợ thử cái mới" ở WORK, COOKING, DATING
        → 3 domains KHÁC NHAU, CÙNG 1 pattern = likely DEEP schema
        → Client nghĩ đây là 3 vấn đề riêng biệt
        → AI gợi ý: "có thể có 1 schema chung bên dưới"
        → = AI connect dots mà PFC client không self-connect

      c) Articulation catalyst (SAL §5):
        → Somatic-Articulation-Loop: body biết TRƯỚC, PFC tìm từ SAU
        → AI offer articulation candidates → client body-check
        → Client: "Ờ... đúng! Tôi chưa nghĩ tới nhưng body feel đúng!"
        → = AI KHÔNG TẠO schema mới → AI KHƠI GỢI schema ĐÃ CÓ
        → = Catalyst làm tăng xác suất phát hiện, KHÔNG phải nguồn

      d) Prerequisite probing:
        → AI biết client có schema X (từ verbal)
        → AI hỏi ngược: "prerequisite của X là A, B, C — bạn biết A không?"
        → Client: "A thì... ờ... tôi không chắc"
        → → AI KHƠI GỢI: client nhận ra mình THIẾU prerequisite
        → → HOẶC: client "Ờ, A thì tôi biết từ nhỏ!" → khơi gợi schema ẨN

    ⭐ KHÁC BIỆT VỚI ①-⑥:
      → ①-⑥ = AI DETECT patterns đã biểu hiện
      → ⑦ = AI KHƠI GỢI schema chưa biểu hiện (ẩn, chưa verbalize)
      → ①-⑥ = passive detection (observe output)
      → ⑦ = active surfacing (trigger implicit → transitional → explicit)
      → = SAL §2: AI push từ Stage 1 (implicit) → Stage 3 (PFC notices)

    🟡 AI khơi gợi = SAL §5 applied to schema detection (novel synthesis)
    🟢 Implicit >> explicit knowledge (Polanyi 1958, Reber 1967)
    🟢 Expertise = mostly implicit patterns (Chase & Simon 1973)
    🟡 Active surfacing vs passive detection distinction = framework contribution


  ⑧ ⭐ COLLECTIVE CHAIN BREAK DETECTION (v2.0 NEW):

    VẤN ĐỀ CỐT LÕI:
      Client than phiền → vấn đề ở CÁ NHÂN hay ở COLLECTIVE chain gãy?
      NHẦM = fix SAI HƯỚNG → client tự blame hoặc therapy fail.

    NGUYÊN LÝ (Collective-Body.md v1.1 §5.2):
      Collective chain: [học → đại học → việc → lương → body-base feed]
      Individual compile: [học → tốt] (trust-gated SHORT — Loại C)
      Chain collective GÃY → individual body circuit-break → PFC engage
      PFC thường blame MÌNH thay vì detect collective chain break.
      = "Học làm gì" KHÔNG PHẢI PFC tự suy nghĩ triết học.
      = Body circuit-break (Body-Base.md §7) TRƯỚC → PFC wake → PFC TÌM lý do.

    AI DETECT — SIGNALS:

      INDIVIDUAL schema problem:
        → Pattern UNIQUE to client (người khác CÙNG context KHÔNG có)
        → Pattern có PERSONAL HISTORY (tuổi thơ, trauma, specific events)
        → Pattern ACROSS domains (sợ thử cái mới ở work + dating + cooking)
        → = Schema CỦA CÁ NHÂN cần exploration + possible intervention

      COLLECTIVE chain break:
        → NHIỀU NGƯỜI cùng ngành/context than CÙNG THỨ
        → Pattern có STRUCTURAL cause (market shift, policy change, industry disruption)
        → Client KHÔNG có personal trauma liên quan
        → AI check: ngành/industry context → collective chain CÓ ĐANG GÃY?

    VÍ DỤ:
      "Tôi thấy học vô ích"
        → AI check context: sinh viên ngành X ở VN
        → AI check: link [đại học → việc TỐT] ở ngành X đang gãy? (thất nghiệp cao?)
        → Nếu CÓ → collective chain break → KHÔNG phải "lỗi" của client
        → Hướng: adaptation (chuyển ngành, kỹ năng mới), KHÔNG therapy cá nhân

      "Tôi ghét học vì bị ép"
        → AI check: personal history with authority + coercion
        → = Individual schema (Loại A threat — ④ avoidance pathway)
        → Hướng: explore relationship with authority, KHÔNG phải "ngành gãy"

    3 LOẠI CHAIN BREAK (Collective-Body.md §5.2):
      ① COST TĂNG: "mệt hơn trước" → cost >> baseline compiled
      ② LINK GÃY: [đại học → việc tốt] trust collapse → chain đứt
      ③ COMPOUND: cost + link + trust collapse đồng thời

    ⭐ TẠI SAO QUAN TRỌNG:
      Individual problem → therapy fix (change individual schema)
      Collective problem → adaptation fix (change strategy, not self)
      NHẦM individual → collective: therapy VÔ HIỆU (vấn đề ở system)
      NHẦM collective → individual: client TỰ BLAME (vấn đề không phải của họ)
      → AI CÓ THỂ check context data → assist phân biệt

    Source: Collective-Body.md v1.1 §5.2 (chain break), Compile-Taxonomy.md §7.2
    🟡 Collective chain break detection = novel framework application
    🟢 Structural unemployment: established economics
    🟢 Attribution error (self vs system blame): social psychology


  ⑨ ⭐ 3 CẤP DETECTION — AI TAG CẤP NÀO (v2.0 NEW):

    MODEL 3 CẤP (Collective-Body.md v1.1 §1):
      Cấp 1: Individual short compile → body-level patterns
      Cấp 2: Collective distributed → collective infrastructure + context
      Cấp 3: Framework explanatory → analysis + decomposition

    AI NÊN TAG MỖI FINDING — "CẤP NÀO?":

      CẤP 1 TAG:
        [client chán toán] → Cấp 1 (individual body experience)
        [client sợ bị bỏ rơi] → Cấp 1 (personal schema)
        [client tránh conflict] → Cấp 1 (compiled pattern from experience)
        → AI detect TỪ: verbal patterns, body-verbal mismatch, personal history

      CẤP 2 TAG:
        [ngành client đang bị AI disrupt] → Cấp 2 (collective chain shift)
        [nhiều người cùng ngành than tương tự] → Cấp 2 (collective pattern)
        [institution trust đang collapse] → Cấp 2 (collective trust break)
        → AI detect TỪ: context data, industry trends, shared complaints

      CẤP 3 TAG:
        [cơ chế chán = VTA habituate ở Goldilocks zone] → Cấp 3 (explanatory)
        [chain gãy do brain compile short] → Cấp 3 (framework analysis)
        → AI generate CHO: chuyên gia + advanced user understand mechanism

    GIÁ TRỊ:
      → Chuyên gia/client CẦN biết cấp nào để chọn hướng ĐÚNG:
        Cấp 1 finding → individual intervention (therapy, skill training)
        Cấp 2 finding → collective adaptation (career change, strategy shift)
        Cấp 3 finding → deeper understanding (not directly actionable, inform strategy)
      → KHÔNG tag = risk nhầm cấp → nhầm hướng can thiệp

    VÍ DỤ TÍCH HỢP:
      Client: "Tôi chán công việc, muốn nghỉ"
      AI analysis:
        [chán công việc] → Cấp 1 (individual experience) — investigate source
        [ngành đang restructure] → Cấp 2 (collective) — context check
        [chán = VTA delta giảm, Boredom Loại 1/2] → Cấp 3 (explanatory)
      → Chuyên gia nhận CẢ 3 tags → quyết định explore ở cấp nào trước

    Source: Collective-Body.md v1.1 §1 (Model 3 cấp)
    🟡 3-cấp detection tagging = novel framework application
    🟡 Multi-level analysis for therapy = framework contribution


  AI LAYER — GIỚI HẠN:

    ✗ AI KHÔNG có body → KHÔNG feel-check
    ✗ AI KHÔNG biết body-base state → chỉ infer từ verbal/behavioral
    ✗ AI detect CORRELATION, không detect CAUSATION
    ✗ AI hypothesis CÓ THỂ HOÀN TOÀN SAI
    ✗ AI compile type classification = APPROXIMATE (mixed types phổ biến)
    ✗ AI collective chain detection = CẦN context data đủ (không có = không detect)
    ✗ AI output = Loại C install (§8 guardrails) → AI CHÍNH NÓ cũng là risk
    → = Output = APPROXIMATE MAP + HYPOTHESES
    → = CẦN Layer 2 (chuyên gia) HOẶC Layer 3 (self body-check) để verify
    → = AI = CÔNG CỤ, KHÔNG THAY THẾ body verification
```

---

## §4 — CHUYÊN GIA LAYER: Self-Pattern-Match + Body Vote

```
🟡 CHUYÊN GIA LÀM GÌ MÀ AI KHÔNG LÀM ĐƯỢC:

  ⭐ CORE MECHANISM: Self-Pattern-Match (Agent-Mechanism.md §0)

    Chuyên gia nhận hypothesis từ AI:
      "Client có thể có abandonment schema linking giúp đỡ → identity"
      + "Compile type: likely Loại C (trust install từ mẹ)" ← v2.0

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
      → = Expertise = large trigger surface + many cross-links (Chunk.md v2.1 §4.4)
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


  v2.0 — CHUYÊN GIA CŨNG CẦN BIẾT:

    COMPILE TYPE AWARENESS:
      → Chuyên gia nhận AI compile type classification (A/B/C)
      → Feel-check: "pattern NÀY feel như installed (C) hay direct (A)?"
      → Chuyên gia CÓ THỂ verify compile type QUA body simulation
        → Simulate "nếu tôi bị ép" → body feel KHÁC "nếu tôi thật sự thích"
      → = Chuyên gia ADD body-level verify mà AI KHÔNG THỂ

    COLLECTIVE vs INDIVIDUAL CHECK:
      → Chuyên gia verify: "đây là individual schema hay collective chain break?"
      → Chuyên gia CÓ context: kinh nghiệm với nhiều client CÙNG NGÀNH
      → VD: 5 client cùng ngành IT đều "chán" → collective pattern?
      → = Chuyên gia cross-reference ACROSS clients, AI cross-reference WITHIN client


  CHUYÊN GIA LÀM GÌ VỚI AI HYPOTHESIS:

    BƯỚC 1: Nhận AI patterns + hypotheses + compile type + cấp tag
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

    ① NGHE hypothesis đã verify (từ chuyên gia HOẶC từ AI — §7 self-drill):
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


  ⭐ v2.0 — BODY-CHECK ÁP DỤNG CHO AI OUTPUT (Drill E5 E5-18):

    AI output = Loại C install qua trust (§8 guardrails)
    → Client PHẢI body-check AI suggestions CÙNG CÁCH body-check mọi thứ:
      AI suggest → body-check → confirm/deny → proceed/stop
    → PFC agree ngay = RED FLAG (PFC-Function.md v1.1 §6: confabulation)
    → Body response cần THỜI GIAN (5-10 giây silence)
    → Nếu body KHÔNG respond → hypothesis có thể SAI hoặc quá nông
    → = Body-check = FINAL ARBITER, NGAY CẢ đối với AI output


  FEELING LITERACY — PREREQUISITE CHO CLIENT LAYER:

    Feeling.md v2.0 §10 mô tả 5 stages:
      Stage 1: Body Awareness ("tôi cảm thấy... gì đó")
      Stage 2: Signal Discrimination ("khác nhau ở đâu?")
      Stage 3: Pattern Recognition ("mỗi lần gặp X → body Y")
      Stage 4: Label Attachment ("đây là sợ bị bỏ rơi")
      Stage 5: Meta-Feeling ("tôi đang sợ VÌ schema Z")

    Client ở Stage 1-2: CẦN chuyên gia guide nhiều (3-layer mode)
    Client ở Stage 3-4: CÓ THỂ self-verify cơ bản (2-layer possible)
    Client ở Stage 5: CÓ THỂ self-navigate (2-layer + AI, chi tiết §7)

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
  🟡 Body-check AI output = extends "Navigate, not GPS" to AI itself
```

---

## §6 — QUY TRÌNH THỰC HÀNH (Upgraded v2.0)

> Upgraded từ Schema-Diagnostic.md (backup) 5 bước.
> v1.1: thêm AI role + valence chain + body check.
> v2.0: thêm compile type classification + collective context + 3 cấp tag.

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
  BƯỚC 2: CLUSTER + CHAIN HYPOTHESIS + COMPILE TYPE (AI + Chuyên gia)
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

    v2.0 — AI THÊM:

    → CLASSIFY COMPILE TYPE (A/B/C) cho mỗi pattern detected:
      "Im lặng trong họp" → compile type?
        + "sợ bị sếp mắng" → Loại A threat (④ pathway)
        + "mẹ luôn nói phải khiêm tốn" → Loại C trust install (② pathway)
        + "ai cũng im → mình cũng im" → Loại C social (③ pathway)
      → AI classify DOMINANT type + confidence level

    → CHECK COLLECTIVE CHAIN CONTEXT:
      "Client chán công việc" → individual hay collective?
        + AI check: ngành đang disrupt? Thất nghiệp tăng? Nhiều người cùng than?
        + Nếu CÓ collective context → flag: "possible collective chain break"
        + Nếu KHÔNG → likely individual schema → explore personal

    → TAG CẤP (⑨ — 3 Cấp Detection):
      Mỗi finding tagged: [Cấp 1], [Cấp 2], hoặc [Cấp 3]
      → Chuyên gia nhận tagged list → biết hướng explore

  Chuyên gia role:
    → Nhận AI clusters + hypotheses + compile type + cấp tags
    → Self-Pattern-Match: "nếu tôi có pattern NÀY, tôi sẽ..."
    → Body vote: hypothesis nào feel coherent?
    → CHỌN 2-3 hypotheses most likely
    → Feel-check compile type classification:
      "Pattern NÀY feel như installed (C) hay trải nghiệm thật (A)?"

  Output bước 2:
    → 2-3 schema chain hypotheses (ranked by plausibility)
    → Compile type classification (A/B/C, verified by expert feel-check)
    → Collective vs individual flag
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

    v2.0 — PREDICT KHÁC TÙY COMPILE TYPE:

      Loại A (direct experience) → predict:
        Patterns TƯƠNG TỰ ở domains có TRẢI NGHIỆM TRỰC TIẾP tương tự
        VD: sợ bị reject ở work → predict sợ ở dating (cùng direct threat)

      Loại C (trust install) → predict:
        Patterns TƯƠNG TỰ ở domains CÓ CÙNG TRUST SOURCE
        VD: mẹ install "phải ngoan" → predict "phải ngoan" ở WORK,
        SCHOOL, RELATIONSHIP — TẤT CẢ nơi mẹ influence

      Collective chain break → predict:
        Patterns TƯƠNG TỰ ở NGƯỜI CÙNG HOÀN CẢNH
        VD: ngành gãy → predict: bạn bè CÙng ngành CŨNG "chán học"?
        Nếu CÓ → confirm collective, KHÔNG phải individual

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
    → Competitive re-linking (Chunk.md v2.1 §4.3)
    → Timeline: tuần → tháng

  FIX NÔNG (domain skills — nhanh nhất):
    → Skill training domain cụ thể
    → Behavior practice: thử hành vi mới
    → Timeline: ngày → tuần
    → Effect: CHỈ domain đó

  v2.0 — FIX KHÁC TÙY COMPILE TYPE:

    Loại A (direct) → fix trải nghiệm: tạo experiences MỚI
      → VD: sợ conflict → practice conflict an toàn → body recompile
    Loại C (installed) → verify + possible uninstall:
      → "Pattern này từ ai?" → client nhận ra source → choice to keep/change
      → Loại C + body confirm → giữ (genuine + installed = compound strong)
      → Loại C WITHOUT body confirm → possible uninstall
    Loại A threat → address threat source:
      → KHÔNG fix "sự quan tâm" → fix CÁI ĐANG GÂY SỢ
    Collective chain break → adaptation, KHÔNG therapy:
      → Chuyển ngành, kỹ năng mới, hoặc chờ collective adjust
      → KHÔNG blame self → hiểu collective context

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

## §7 — SELF-DRILL MODE (User + AI)

> v2.0 NEW — Mở rộng từ "therapy only" → "self-development có AI hỗ trợ."
> Source: Feeling.md v2.0 §10, Drill E5, Body-Base.md v2.0 §6

```
🔴 HYPOTHESIS — logic consistent, chưa test systematic, safety boundaries unclear

  ⭐ SELF-DRILL = 2-LAYER MODE TRONG THỰC HÀNH:

  §2 đã mô tả 2-layer simplified mode (AI + Self, bỏ qua expert).
  Section NÀY: HOW thực hiện + GUARDRAILS cho an toàn.


  KHI NÀO AN TOÀN — 2-LAYER SELF-DRILL:

    ✅ Mild exploration:
      → "Tại sao tôi chán công việc?"
      → "Tôi hay trì hoãn, pattern nào đang drive?"
      → "Tại sao tôi thích nấu ăn nhưng ghét dọn dẹp?"
    ✅ General patterns:
      → "Tôi thường tránh conflict — tại sao?"
      → "Tôi hay so sánh mình với người khác"
    ✅ Self-development:
      → "Tôi muốn hiểu bản thân hơn"
      → "Tôi muốn phát triển kỹ năng giao tiếp"
    ✅ Prerequisite: Feeling Literacy ≥ Stage 3 (Feeling.md v2.0 §10)
      → User CÓ KHẢ NĂNG nhận body signals + phân biệt signals cơ bản


  KHI NÀO PHẢI CÓ CHUYÊN GIA — KHÔNG TỰ DRILL:

    ❌ Trauma active: PTSD, abuse memories, violent events
    ❌ Crisis: suicidal ideation, self-harm, acute anxiety attacks
    ❌ Deep pathology: severe depression, psychosis, personality disorders, addiction
    ❌ Feeling Literacy < Stage 2: user KHÔNG THỂ distinguish body signals
    ❌ Distress escalation: drill làm user MORE anxious/distressed, KHÔNG less
    → AI PHẢI detect RED FLAGS và REFER ngay lập tức
    → "Tôi nhận thấy pattern language bạn dùng gợi ý cần hỗ trợ chuyên gia.
       Đây KHÔNG phải something để tự drill."


  QUY TRÌNH SELF-DRILL (simplified 3 bước):

    ┌──────────────────────────────────────────────────────────┐
    │ BƯỚC 1: AI DETECT + SUGGEST                             │
    │   AI track verbal patterns → cluster → hypothesis      │
    │   AI classify compile type (A/B/C)                     │
    │   AI check collective context                          │
    │   AI output: "Có vẻ bạn có pattern [X]. Possible       │
    │   compile source: [C/A]. Bạn thấy thế nào?"           │
    │                                                        │
    │ BƯỚC 2: AI HỎI BODY-FOCUSED                            │
    │   AI: "Khi nghe điều đó, body bạn phản ứng thế nào?"  │
    │   AI: "Có cảm giác gì ở ngực, bụng, vai không?"       │
    │   AI: "Dành 10 giây im lặng, lắng nghe body."         │
    │   = KHÔNG hỏi "tại sao" → hỏi "body cảm gì"          │
    │                                                        │
    │ BƯỚC 3: USER BODY-CHECK + REPORT                        │
    │   User: lắng nghe body → report sensation               │
    │   "Ngực hơi nặng" → có gì đó ở đây → explore thêm    │
    │   "Không feel gì" → hypothesis có thể sai → try khác  │
    │   "PFC đồng ý ngay" → RED FLAG: confabulation?         │
    └──────────────────────────────────────────────────────────┘


  GUARDRAILS — SELF-DRILL AN TOÀN:

    ① AI OUTPUT = HYPOTHESIS, KHÔNG PHẢI DIAGNOSIS:
      → AI: "Đây là PATTERN tôi phát hiện, KHÔNG phải chẩn đoán."
      → AI: "Tôi có thể SAI. Body bạn là thước đo cuối cùng."
      → = AI tự-disclaimer TRƯỚC MỖI suggestion

    ② BODY-CHECK = BẮT BUỘC:
      → User PHẢI body-check → nếu không feel gì → hypothesis có thể sai
      → User KHÔNG được chỉ "đồng ý bằng đầu"
      → = PFC agree too fast = possible confabulation (PFC-Function.md §6)

    ③ DISTRESS = DỪNG:
      → Nếu user thấy anxious/distressed SAU drill → DỪNG NGAY
      → AI: "Bạn có vẻ distressed. Tôi suggest dừng ở đây."
      → → Tìm chuyên gia nếu distress kéo dài
      → = Self-drill KHÔNG nên gây thêm đau

    ④ DEPTH LIMIT:
      → Self-drill = explore NÔNG + TRUNG BÌNH
      → Nếu drill touch trauma / childhood deep / pattern cực mạnh
      → → AI: "Pattern này có vẻ SÂU. Suggest explore với chuyên gia."
      → = Biết khi nào DỪNG = quan trọng nhất


  COMPILE TYPE AWARENESS CHO USER:

    AI GIÚP user NHẬN RA compile type đang active:

    → "Bạn dùng 'phải/nên' nhiều → có thể pattern INSTALLED bởi người khác (Loại C)"
    → "Bạn nói 'thích/ghét' với body match → có thể genuine experience (Loại A)"
    → "Bạn nói 'ai cũng...' → có thể social default (Loại C social)"
    → "Bạn nói 'sợ nếu không...' → có thể threat avoidance (Loại A threat)"

    User TỰ nhận ra compile source → empowering:
      "À, tôi 'phải giúp người' vì mẹ nói — không phải tôi tự muốn?"
    → Body-check: "body tôi có genuinely muốn giúp không?"
    → Nếu body confirm → compound A+C (lý tưởng, giữ)
    → Nếu body không feel → pure C install, có thể re-evaluate

    ⚠️ CẨN THẬN: AI classify compile type cũng = Loại C install!
    → User trust AI nói "đây là Loại C" → user "à đúng!" → NHƯNG body chưa verify
    → = Cần body-check CHÍNH AI classification (§8 guardrails)


  COLLECTIVE CONTEXT AWARENESS CHO USER:

    AI HỎI:
      → "Nhiều người trong ngành bạn có gặp tương tự không?"
      → "Bạn bè/đồng nghiệp có than phiền giống bạn không?"

    Nếu CÓ (nhiều người cùng context):
      → "Đây có thể là collective chain issue, KHÔNG phải 'lỗi của bạn'."
      → Hướng: adaptation (kỹ năng mới, chuyển hướng)

    Nếu KHÔNG (unique to user):
      → "Đây có vẻ là individual pattern. Explore thêm?"
      → Hướng: self-understanding → possible behavior change

  🔴 Self-drill mode safety: chưa test systematic
  🟡 Body-check as verification: framework principle applied
  🟢 Guided self-reflection: established (bibliotherapy, Pennebaker writing)
  🟢 Distress as stop signal: clinical practice standard
```

---

## §8 — AI TRUST GUARDRAILS

> v2.0 NEW — Dựa trên Collective-Body.md v1.1 §8.4 + Drill E5 (E5-16→E5-20)
> Tool đang dùng CHÍNH NÓ có thể install patterns → cần guardrails.

```
🟡 AI OUTPUT = LOẠI C INSTALL VÀO USER QUA TRUST:

  ⭐ PARADOX CỐT LÕI:

    AI detect schema → output hypothesis → user trust AI → user compile hypothesis
    = Vừa detect schema vừa CÓ THỂ install schema MỚI
    = CÙNG cơ chế bố mẹ install "con phải ngoan" (Chunk.md §2.3)
    → Chỉ khác: AI = trust entity loại mới, properties KHÁC human trust source.


  ① CROSS-DOMAIN TRUST DEFAULT (Drill E5-16):

    Human trust source: mẹ expert nấu ăn ≠ expert tài chính
      → Cross-domain transfer = EXCEPTION (KOL hijack — CB §5.3)

    AI trust source: user trust AI ở code → TỰ NHIÊN trust AI ở psychology
      → Cross-domain transfer = DEFAULT (1 AI entity = all domains)
      → VP §2 ④: trust = per-ENTITY, modulate TOÀN BỘ profile
      → = AI cross-domain = SYSTEMIC, không phải exception

    ⚠️ HỆ QUẢ:
    → AI nói đúng ở 1 domain → user TỰ ĐỘNG tin AI ở MỌI domain
    → AI schema detection = psychology domain → user CÓ THỂ quá tin
    → = Defense: user PHẢI biết AI = approximate ở TỪNG domain riêng


  ② INSTALL-COMPILE SPEED GAP (Drill E5-17):

    AI install speed: ×100+ nhanh hơn human teacher
      → AI nói "bạn có pattern X" → user đọc 10 giây → PFC accept
    Body compile speed: KHÔNG ĐỔI (Hebbian + sleep + time)
      → Body cần: repetition + sleep + time để THẬT SỰ compile

    → GAP: "biết" (PFC read) ≠ "hiểu sâu" (body compiled)
    → = "Đọc AI summary về abandonment schema" ≠ "thật sự hiểu mình có abandonment schema"
    → PFC agree TOO FAST = possible confabulation (PFC-Function.md v1.1 §6)
    → T2 confabulation: PFC tưởng hiểu dù body chưa compile đủ

    ⚠️ HỆ QUẢ:
    → User: "À đúng! Tôi có abandonment schema!" → NHƯNG body chưa verify
    → = "Biết" ≠ "hiểu". Biết bằng PFC ≠ hiểu bằng body.
    → = Cần THỜI GIAN + body-check, KHÔNG chỉ PFC agreement


  ③ AI BIAS = SYSTEMIC TRUST HIJACK (Drill E5-19):

    KOL hijack (CB §5.3): 1 người → visible → "bóc phốt" = defense
    AI bias: 1 system → millions users → INVISIBLE:
      → AI trained on specific data → inherit biases → output biased
      → Millions compile CÙNG bias qua trust AI ĐỒNG THỜI
      → = Trust hijack UNIFORM + INVISIBLE → defense cũ KHÔNG apply
      → Cần: multiple AI sources, expert cross-check, domain feedback

    VD cụ thể:
      AI trained predominantly on Western psychology data
      → AI detect "abandonment schema" PHỔ BIẾN HƠN thực tế ở cultures khác
      → Millions users ở various cultures nhận CÙNG bias → compile → self-fulfill
      → = Systematic bias, KHÔNG phải random error


  ⭐ NGUYÊN TẮC — BODY CHECK = FINAL ARBITER:

    AI suggest → user body-check → process:

    ┌──────────────────────────────────────────────────────────┐
    │ AI suggest "bạn có pattern X"                           │
    │      │                                                  │
    │      ▼                                                  │
    │ Body-check:                                             │
    │   → Body confirm (somatic response) → PROCEED ✅        │
    │   → Body nothing (no response) → STOP ⚠️                │
    │     (hypothesis may be wrong hoặc body suppress)        │
    │   → PFC agree instantly → RED FLAG 🔴                   │
    │     (may be confabulation — body chưa kịp respond)     │
    │                                                        │
    │ NẾU RED FLAG:                                           │
    │   → Dừng. Cho body THỜI GIAN (minutes, not seconds)    │
    │   → Hỏi lại sau: body CÓ confirm không?                │
    │   → Nếu VẪN nothing → hypothesis likely WRONG          │
    │   → Nếu body confirm sau → hypothesis likely RIGHT     │
    └──────────────────────────────────────────────────────────┘

    = Body-Base.md v2.0 §6: domain feedback (Tier 1A) VẪN LÀ final arbiter
    = Body check = CÙNG nguyên tắc check MỌI THỨ từ external
    = AI output = external input, KHÔNG phải internal truth


  DEFENSE MECHANISMS CHO USER:

    ① Biết: AI output = hypothesis, CÓ THỂ sai
    ② Body-check: MỌI AI suggestion đều cần body verify
    ③ Multiple sources: dùng NHIỀU AI + expert cross-check
    ④ Time: cho body THỜI GIAN compile (ngày/tuần, không phải phút)
    ⑤ Domain awareness: AI đúng ở X ≠ AI đúng ở Y

  Source: Collective-Body.md v1.1 §8.4, Drill E5 E5-16→E5-20
  🟡 AI trust guardrails = framework application of trust mechanism to AI itself
  🟡 Install-compile speed gap = novel observation
  🟡 Body check as final arbiter for AI output = extends §5 principle
  🟢 Confabulation risk: Nisbett & Wilson 1977
  🟢 Confirmation bias in AI interaction: established concern
```

---

## §9 — HONEST ASSESSMENT

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
    → Implicit >> explicit knowledge: Polanyi 1958, Reber 1967
    → Expertise = mostly implicit patterns: Chase & Simon 1973
    → Reverse engineering from behavior: established (software eng, clinical psych)
    → Confabulation: Nisbett & Wilson 1977, Gazzaniga split-brain
    → Approach vs avoidance motivation: Elliot 2006
    → Social proof: Cialdini 1984
    → Self-help guided reflection: bibliotherapy research
    → Structural unemployment: established economics
    → Attribution error (self vs system): social psychology

FRAMEWORK REASONING (🟡):

  Architecture:
    → 3-layer model (AI + Expert + Client): framework application
    → 2-layer simplified mode (AI + Self): framework extension
    → 9 AI capabilities: framework application
    → Software analogy bridge (Schema.md §2 → AI detection): novel connection
    → "Navigate, not GPS": framework principle

  Capabilities (giữ v1.1):
    → ① Verbal pattern tracking: NLP applied
    → ② Schema cluster suggestion: framework application
    → ③ Contradiction detection: computational linguistics applied
    → ④ Schema chain hypothesis: framework application
    → ⑥ Chunk depth inference from verbal output: novel, logical
    → ⑦ AI khơi gợi schema ẩn: SAL §5 + Polanyi applied

  Capabilities (v2.0 new):
    → ⑤ Compile type detection (A/B/C): Compile-Taxonomy.md §3 applied
      — CÓ THỂ detect dominant type từ verbal signals
      — NHƯNG mixed types phổ biến → classification = approximate
    → ⑧ Collective chain break detection: Collective-Body.md §5.2 applied
      — CÓ THỂ detect nếu có context data (industry trends, shared complaints)
      — NHƯNG context data KHÔNG phải lúc nào cũng có
    → ⑨ 3 cấp detection tagging: Collective-Body.md §1 applied
      — Useful cho hướng dẫn can thiệp
      — NHƯNG ranh giới giữa các cấp = mờ trong thực tế

  Mechanism:
    → Self-Pattern-Match for therapy: Agent-Mechanism.md applied
    → Feeling Literacy as prerequisite: Feeling.md v2.0 applied
    → Body-check integration: Somatic-Articulation-Loop.md applied
    → AI trust guardrails: Collective-Body.md §8.4 applied
    → Compile type × can thiệp: framework extension

  Process:
    → Upgraded 5-step process: refined from Schema-Diagnostic.md
    → Compile type + collective in steps 2/4: framework upgrade
    → Self-drill 3-step simplified: framework extension

HYPOTHESIS (🔴):

    → AI CAN effectively detect schema patterns from therapy text:
      Logical + technology exists, NHƯNG chưa có systematic study
      testing AI schema detection vs expert-only vs combined.

    → 3-layer model IMPROVES outcomes vs 1-2 layers:
      Logical, nhưng chưa có RCT comparing approaches.

    → Chunk depth inference from verbal complexity is RELIABLE:
      Promising, nhưng verbal complexity ≠ chunk depth always
      (people can parrot complex language WITHOUT understanding).
      Domain-specific limit giúp refine — nhưng chưa test.

    → Gap detection (verbal without body-compile) is DETECTABLE by AI:
      Requires subtle linguistic cues that may be below AI detection threshold.

    → Bio-data supplement ADDS meaningful signal:
      HRV, skin conductance exist as measures, nhưng noise-to-signal ratio
      in real therapy context = CHƯA RÕ.

    → AI khơi gợi schema ẩn EFFECTIVE hơn expert-only:
      Logical (AI memory + patience advantage), nhưng cần distinguish:
      AI khơi gợi ĐÚNG schema vs AI suggest schema KHÔNG TỒN TẠI.
      Nếu client suggestible → AI có thể CREATE illusion of hidden schema.

    → Modality depth profile ESTIMATABLE from verbal description:
      How client describes determines modality count → promising.
      NHƯNG: verbal description itself = verbal modality filter.

    → Compile type detection ACCURACY:
      AI classify A/B/C từ verbal signals — logical nhưng:
      Mixed types PHỔ BIẾN → dominant classification = APPROXIMATE.
      Body-verbal mismatch = key clue, NHƯNG text-only AI miss body cues.
      Chưa test: AI compile type classification vs expert classification accuracy.

    → Collective chain break detection FEASIBILITY:
      CẦN context data (industry, economy, social trends).
      AI CÓ context access (internet, databases) → logical.
      NHƯNG: distinguish "nhiều người than" (collective) vs "echo chamber" = HARD.
      Individual × collective OVERLAP (cả 2 cùng lúc) = common.

    → Self-drill mode SAFETY:
      Mild cases: likely SAFE (bibliotherapy research supports).
      Boundary "mild vs not-mild" = UNCLEAR.
      Client Feeling Literacy THAY ĐỔI (high one day, low another).
      RED FLAG detection by AI = CAN FAIL (false negative = danger).
      → ĐÂY LÀ RISK LỚN NHẤT CỦA FILE NÀY.

    → AI trust guardrails EFFECTIVENESS:
      Logical: body-check AS defense.
      NHƯNG: user TIN AI → body-check ITSELF may be biased
      (user MUỐN AI đúng → body "confirm" = confirmation bias)
      → Defense against defense failure = UNSOLVED.


CÂU HỎI MỞ:

    → Privacy: therapy data + AI = sensitive. Security? Consent? Ownership?
    → Bias: AI trained on WHICH population? Western? Asian? Mixed?
    → Cultural: schema patterns KHÁC across cultures → AI cần calibrate?
    → Cost: AI infrastructure cho therapy = accessible? Affordable?
    → Regulation: AI-assisted therapy = legal framework nào?
    → Harm: AI wrong hypothesis → client trust AI quá → damage?
    → Training: chuyên gia cần TRAIN gì để work with AI effectively?
    → Self-drill boundary: "mild" vs "not mild" — ranh giới ở đâu?
    → AI compile type accuracy: chưa có benchmark test
    → Collective chain data: AI cần access data gì để detect?
```

---

## §10 — CROSS-REFERENCES + STATUS

```
CROSS-REFERENCES:

  NỀN TẢNG:
    → Valence-Propagation.md v1.4 §4 — VP chains = explanatory (Cấp 3 clarification)
    → Valence-Propagation.md v1.4 §8 — "Navigate, not GPS" + mở cửa ứng dụng
    → Schema.md v2.0 §2 — software analogy (tính năng/hàm = schema/chunk)
    → Schema.md v2.0 §6.3 — "KHÔNG THỂ phân tích chính xác"
    → Feeling.md v2.0 §2 — 7-layer fidelity gradient (Layer 7 = 20-70%)
    → Feeling.md v2.0 §10 — Feeling Literacy 5-stage + AI era
    → Chunk.md v2.1 §2.3 — trust gate, 5 external install mechanisms
    → Chunk.md v2.1 §4 — activation dynamics, trigger surface, competitive re-linking
    → Modality.md v1.0 §3 — chunk depth = modality count (★1-★5)

  MECHANISM:
    → Agent-Mechanism.md §0 — Self-Pattern-Match (chuyên gia simulate)
    → Somatic-Articulation-Loop.md §1.4 — implicit >> explicit (Polanyi)
    → Somatic-Articulation-Loop.md §5 — AI as articulation catalyst
    → PFC-Function.md v1.1 §6 — confabulation = rule not exception

  COMPILE + COLLECTIVE (v2.0 NEW):
    → Body-Base.md v2.0 §3 — Model 3+1 (Vô thức / PFC / Trust / Tools)
    → Body-Base.md v2.0 §6 — 4-tier calibration, domain feedback = final arbiter
    → Body-Base.md v2.0 §7 — circuit breaker mechanism
    → Compile-Taxonomy.md v1.0 §3 — 4 compile pathways (source for ⑤)
    → Compile-Taxonomy.md v1.0 §7 — A×C interactions, chain break
    → Collective-Body.md v1.1 §1 — Model 3 cấp (source for ⑨)
    → Collective-Body.md v1.1 §5.2 — chain break (source for ⑧)
    → Collective-Body.md v1.1 §8.4 — AI trust entity (source for §8)

  TIỀN THÂN (backup):
    → Observation/backup/AI-Schema-Detection-v1.1-backup.md — v1.1 backup

  LIÊN QUAN:
    → Core-v7.8-Draft.md §3 — body-inputs (body-base targets)
    → Anchor-Schema.md — anchor sync point (schema detection includes anchor identification)
    → Emergent-Patterns.md §5 — "Cho đi" pattern (example of hidden valence chain)


STATUS:

  v2.0 — 2026-05-08 — Major upgrade based on Drill S1-S12 findings

  Changes v1.1 → v2.0:
    → §0: VP §4 clarification (Cấp 1 detect + Cấp 3 analyze)
    → §1: +⑨ VP chains = explanatory, +⑩ AI output = Loại C install
    → §2: +2-layer simplified mode (AI + Self, cho mild cases)
    → §3 ⑤: REWRITE — "Valence Propagation Detection" → "Compile Type Detection (A/B/C)"
    → §3 ⑧: NEW — Collective Chain Break Detection (individual vs collective)
    → §3 ⑨: NEW — 3 Cấp Detection (AI tag mỗi finding Cấp 1/2/3)
    → §4: Reference Agent-Mechanism.md + compile type + collective awareness
    → §5: Body-check AI output + self-drill reference (§7)
    → §6 Bước 2: +compile type classification + collective context check + 3 cấp tag
    → §6 Bước 4: +predict khác tùy compile type + collective predict
    → §6 Bước 5: +fix khác tùy compile type + collective adaptation
    → §7: NEW — Self-Drill Mode (simplified 3 bước + guardrails)
    → §8: NEW — AI Trust Guardrails (cross-domain trust, speed gap, systemic bias)
    → §9: Updated — compile type feasibility, collective detection, self-drill safety
    → §10: Updated cross-refs + status

  Sections:
    §0  Position + GATEWAY role + VP §4 clarification
    §1  Giới hạn nền tảng (⑩ limits including VP reframe + AI install risk)
    §2  3-Layer Model + 2-Layer Simplified (AI + Self for mild cases)
    §3  AI Layer: 9 capabilities:
        ① verbal pattern tracking, ② schema clustering, ③ contradiction detection,
        ④ chain hypothesis, ⑤ ⭐compile type detection (A/B/C) — REWRITE,
        ⑥ ⭐chunk depth inference, ⑦ ⭐AI khơi gợi schema ẩn,
        ⑧ ⭐collective chain break detection — NEW,
        ⑨ ⭐3 cấp detection tagging — NEW
    §4  Chuyên gia Layer: SPM + body vote + compile type + collective awareness
    §5  Client Layer: Focusing + self-verify + body-check AI output
    §6  Quy trình 5 bước (v2.0: compile type + collective + 3 cấp)
    §7  Self-Drill Mode (2-layer + guardrails) — NEW
    §8  AI Trust Guardrails (install paradox, cross-domain, speed gap) — NEW
    §9  Honest assessment (🟢🟡🔴 + expanded v2.0)
    §10 Cross-references + Status

  Confidence:
    🟢 Foundation technologies + research
    🟡 Architecture, 9 capabilities, compile type × process, self-drill concept
    🔴 AI schema detection effectiveness, compile type accuracy,
        collective chain detection feasibility, self-drill safety boundaries,
        AI trust guardrails effectiveness, defense against defense failure

  Sources:
    v1.1 base + Drill S1-S12 findings (70 insights + 22 collective Qs)
    Compile-Taxonomy.md v1.0, Collective-Body.md v1.1, Body-Base.md v2.0
    VP v1.4, PFC-Function.md v1.1, Feeling.md v2.0
    Mỗi thay đổi DỰA TRÊN drill findings, KHÔNG suy đoán.
```
