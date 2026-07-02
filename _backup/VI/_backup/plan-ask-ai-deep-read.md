# Plan: Ask-AI-Deep-Read.md — AI Framework Reading Guide

> **Ngày tạo:** 2026-05-11
> **Trạng thái:** ✅ IMPLEMENTED — Ask-AI-Deep-Read.md v1.0 (525L)
> **Trigger:** Framework ~60 files, ~60,000L. AI trained on mainstream science.
>   Nhiều framework positions REJECT hoặc REFRAME mainstream.
>   Nếu AI không đọc kỹ → format đúng + content sai = worse than nothing.
>   Cần file hướng dẫn AI: ĐỌC GÌ, THỨ TỰ NÀO, TẠI SAO.
> **Nguyên tắc:** Chậm mà chắc. Chất lượng cao nhất.
> **Target:** Ask-AI/Ask-AI-Deep-Read.md (~400-500L)

---

## §0 — TẠI SAO CẦN FILE NÀY

### §0.1 Vấn đề

```
Framework Human Predictive Drive có ~60 files, ~60,000+ dòng.
AI (Claude, GPT, etc.) trained on mainstream science/psychology.

Framework EXPLICITLY REJECT hoặc REFRAME nhiều mainstream positions:
  → 4 file Clarification/ (reject cụ thể)
  → 23+ positions khác rải rác trong ~20 files

Nếu AI chỉ đọc Ask-AI.md (protocol) mà không đọc mechanism files:
  → AI BIẾT cách trình bày (experience-based, mini-gap chain)
  → NHƯNG AI KHÔNG BIẾT framework nói GÌ khác mainstream
  → AI sẽ fill gaps bằng mainstream training data
  → Mainstream data CONFLICT framework ở ~27 điểm quan trọng
  → = Format đúng + Content sai = WORSE than no answer
  → Vì người dùng TIN AI → compile SAI → shift cost sau
```

### §0.2 File này giải quyết gì

```
Ask-AI-Deep-Read.md = READING GUIDE + DANGER ZONE MAP cho AI:
  ① TẠI SAO phải đọc kỹ (với ví dụ failure cụ thể)
  ② ĐỌC GÌ, THỨ TỰ NÀO (tiered, dependency-aware)
  ③ DANGER ZONES: ~15 positions framework ≠ mainstream (brief summaries)
  ④ PROTOCOL trước mỗi câu trả lời
```

### §0.3 Relationship với Ask-AI.md

```
Ask-AI.md        = HOW to interact (protocol: detect, adapt, present)
Deep-Read.md     = HOW to prepare (knowledge: what to read, what NOT to say)
02-CNT.md        = WHY "nói ≠ hiểu" (mechanism behind communication)

3 files complement nhau:
  Deep-Read → chuẩn bị kiến thức
  Ask-AI → cách tương tác
  02-CNT → lý thuyết truyền đạt

User setup: kéo cả 3 + framework folder → AI ready
```

---

## §1 — INVENTORY: 27 POSITIONS FRAMEWORK ≠ MAINSTREAM

### §1.1 — 4 EXPLICIT REJECTIONS (Clarification/ folder)

```
Các file này EXPLICITLY REJECT mainstream position với evidence:

① Dopamine-Reward-Rejection.md
   Mainstream: Dopamine = hormone hạnh phúc/reward
   Framework: Dopamine = VTA salience alert (chuông cửa). Opioid = reward thật
   AI sẽ nói SAI: "dopamine hit", "boost dopamine", "dopamine rush"

② Mirror-Neuron-Rejection.md
   Mainstream: Mirror neurons = bẩm sinh → empathy
   Framework: KHÔNG có hardware mirror module. Empathy = SPM learned function
   AI sẽ nói SAI: "mirror neurons giúp bạn cảm nhận người khác"

③ Cortisol-Amplifier-Not-Cause.md
   Mainstream: Cortisol = hormone stress gây hại
   Framework: Cortisol = change-readiness amplifier. Hại = chronic + thiếu sleep/repair
   AI sẽ nói SAI: "cortisol gây stress", "giảm cortisol"

④ Prediction-Error-Is-Not-Reward.md
   Mainstream: PE = reward signal (AI/RL conflate)
   Framework: PE = attention signal only. Reward = PE + Coherence + H10
   AI sẽ nói SAI: "prediction error drives reward"
```

### §1.2 — 8 CRITICAL REFRAMES (AI sẽ actively nói SAI)

```
Các positions này QUAN TRỌNG vì AI sẽ ACTIVELY giải thích SAI nếu không biết:

⑤ Consciousness reach ~5%, KHÔNG phải controller
   Mainstream: Ý thức kiểm soát hành vi (willpower narrative)
   Framework: PFC reach ~5% processing. Body xử lý 95%. Body tính TRƯỚC PFC.
   File: Core-Interface.md §4, PFC-Function.md §1
   AI sẽ nói SAI: "bạn cần ý chí mạnh hơn", "quyết tâm thay đổi"

⑥ Schema ≠ cognitive distortion (CBT reframe)
   Mainstream: CBT gọi schemas = "distorted thinking patterns"
   Framework: KHÔNG có "méo". 2 hệ thống (PFC vs body) có kết luận KHÁC.
   File: Schema.md v2.0, Logic-Feeling.md
   AI sẽ nói SAI: "suy nghĩ méo mó", "reframe cognitive distortion"

⑦ Body evaluates PATTERNS, not reality
   Mainstream: Body detects objective conditions
   Framework: Body evaluate patterns against compiled expectations.
   Coherent-but-false patterns reward. Incoherent-but-true patterns punish.
   File: Body-Base.md v2.0 §2, Why-Body-Knows.md
   AI sẽ nói SAI: "cơ thể cho bạn biết sự thật"

⑧ Feeling ≠ narrow emotion
   Mainstream: Feelings = emotional states (vui, buồn, giận)
   Framework: Feeling = WHAT PFC observes khi body-chunk interaction happens.
   Hunger = feeling. Anxiety = feeling. Pattern-match insight = feeling.
   File: Feeling.md v2.0 §1-§2
   AI sẽ nói SAI: "cảm xúc của bạn" (quá hẹp), "quản lý cảm xúc"

⑨ Logic ≠ opposite of Feeling
   Mainstream: System 1 (feeling/fast) vs System 2 (logic/slow) binary
   Framework: Logic + Feeling = parallel, chạy ĐỒNG THỜI cho mọi entity.
   Tỉ lệ thay đổi theo domain, KHÔNG binary.
   File: Logic-Feeling.md, Logic-Feeling-Balance.md
   AI sẽ nói SAI: "bạn đang nghĩ bằng cảm xúc thay vì logic"

⑩ Action emerges BEFORE conscious decision
   Mainstream: Ý thức quyết định → body thực hiện
   Framework: Body-driven chunks fire → feeling emerge → PFC observe →
   PFC label/articulate → action ĐÃ underway
   File: PFC-Function.md §1, Drive.md §1
   AI sẽ nói SAI: "bạn cần suy nghĩ trước khi hành động" (as if PFC leads)

⑪ "Biết mà không làm được" = 2 hệ thống tách biệt
   Mainstream: = thiếu ý chí / motivation
   Framework: PFC agree ≠ body compile. PFC = ~5%, body patterns = 95%.
   Pattern mới cần: repetition + body-level reward + time.
   File: Core-Interface.md §4, Body-Base.md
   AI sẽ nói SAI: "bạn cần motivated hơn", "try harder"

⑫ Reward = contingent on H10 (5 preconditions)
   Mainstream: Reward = striatal dopamine/opioid response (simple)
   Framework: Reward CONTINGENT on 5 preconditions (chunk base adequate +
   PE threshold + Goldilocks 40-70% + association clean + quality baseline)
   Same stimulus CAN or CANNOT produce reward depending on conditions.
   File: Body-Feedback/03-Reward.md, Feeling.md v2.0 §6
   AI sẽ nói SAI: "hoạt động X sẽ cho bạn reward" (không conditional)
```

### §1.3 — 8 IMPORTANT REFRAMES (AI sẽ frame SAI)

```
Không actively sai, nhưng AI sẽ FRAME thiếu chính xác:

⑬ Schema = observation parameter, KHÔNG phải component
   File: Schema.md v2.0 §0
   Brain chạy chunks, không chạy schemas. Schema = label mô tả từ bên ngoài.

⑭ Drive = observation parameter, KHÔNG phải motivational module
   File: Drive.md v1.0 §0
   Drive = tên gọi cho energy+direction emergent. Không có "drive module."

⑮ Novelty = observation parameter, KHÔNG phải curiosity drive
   File: Novelty.md v1.0 §0
   Novelty = pattern khi VTA detect positive prediction delta + chunk-gap.

⑯ Status = resource access map, KHÔNG phải social ranking
   File: Status.md v2.0 §0
   Body's resource-access calibration. Multi-dimensional. Per-person, per-context.

⑰ Connection = agents as body-base tools, KHÔNG chỉ emotional bond
   File: Connection.md v3.0 §0
   Agents = external tools for body-base feeding. 3 generative primitives.

⑱ Attention = continuous multi-factor spectrum, KHÔNG binary ADHD/normal
   File: Attention-Spectrum.md v2.0
   COMT + chunk-threshold + NE sensitivity + cortisol. Different ≠ worse.

⑲ Learning = cycle (3 signals + sleep), KHÔNG phải single event
   File: 09-Learning-Cycle.md
   Each learning creates: reward + fatigue + dissonance. Sleep resolves.

⑳ Empathy = SPM F1 + positive valence, KHÔNG phải mirror or contagion
   File: Empathy.md v2.0 §2
   Same mechanism with negative valence = schadenfreude. Chunk-based, learned.
```

### §1.4 — 7 ENRICHMENT POSITIONS (tốt cho depth, không critical)

```
㉑ Love = 2-luồng reward (L1 momentary + L2 structural)
   File: Love-Unified.md, Connection.md v3.0

㉒ Body-base pacing: compile cần repetition + sleep + time
   File: Body-Base.md, 09-Learning-Cycle.md

㉓ Wanting = multi-mechanism (PE + gap-pull + valence + preview)
   File: Liking-Wanting.md

㉔ Coherence = predictive pattern-matching success, KHÔNG phải cognitive consistency
   File: Why-Body-Knows.md §2

㉕ Meta-principle: Logic + Feeling đều KHÔNG 100% chính xác
   File: Logic-Feeling-Balance.md

㉖ Framework mô tả NGUYÊN TẮC HOẠT ĐỘNG — KHÔNG prescribe "cách sống đúng"
   File: Core-Interface.md §0.2, Logic-Feeling-Balance.md

㉗ AI output = Loại C external install → body-check mandatory
   File: AI-Schema-Detection.md §8
```

---

## §2 — READING ORDER (dependency-aware)

### §2.1 — Dependency map

```
Core-Interface.md     → self-contained, cho "mọi người"
Core-Hardware.md      → self-contained, cho neuroscience verify
Core-Software.md      → 12 PREREQUISITES (capstone file!)
Body-Base.md          → entry point, đọc TRƯỚC sub-files
4 Clarification files → self-contained, cần background §0

DEPENDENCY CHAIN (simplified):
  Core-Interface.md ← không cần gì
  Body-Base.md ← Why-Body-Knows.md
  Feeling.md ← Body-Feedback.md
  Chunk.md ← self-contained
  Core-Software.md ← 12 files (CAPSTONE)
```

### §2.2 — Tiered reading order

```
TIER 1 — NỀN TẢNG (PHẢI đọc trước mọi câu hỏi):

  Thứ tự đọc:
  ① Ask-AI.md v2.0              — protocol tương tác (714L)
  ② Ask-AI-Deep-Read.md (MỚI)  — file NÀY: danger zones + reading guide
  ③ Core-Interface.md v1.0      — observer perspective (679L)
     → §1 quan sát gì, §2 ý nghĩa, §3 CÓ THỂ, §4 KHÔNG THỂ, §5 patterns, §6 làm việc
  ④ Body-Base.md v2.0           — entry point body-base system (959L)
     → §2 core principles, §3 Model 3+1, §6 4-tier calibration
  ⑤ 4 Clarification files       — explicit rejections (~2,600L total)
     → Dopamine, Mirror, Cortisol, PE

  Total Tier 1: ~5,400L — manageable cho hầu hết AI context windows


TIER 2 — CƠ CHẾ CỐT LÕI (cần cho trả lời có chiều sâu):

  ⑥ Why-Body-Knows.md           — tại sao body check đáng tin
  ⑦ Feeling.md v2.1             — 7-layer, PFC observation interface
  ⑧ Chunk.md v2.1               — sole substrate, compile, activation
  ⑨ Logic-Feeling-Balance.md    — meta-principle: neither 100% right
  ⑩ 02-Cross-Network-Transfer.md — tại sao "nói ≠ hiểu" (1,435L)
  ⑪ Core-Software.md v1.0 (KEY SECTIONS: §0-§1, §8, §11)
     → §0 tại sao cycle-based, §1 architecture, §8 observation params, §11 key reframes


TIER 3 — PER TOPIC (đọc KHI user hỏi topic cụ thể):

  Stress / burnout:
    → Cortisol-Baseline.md v2.0, Connection.md (burnout = L1/L2)

  Nuôi con / parenting:
    → Child-Chunk-Development/Foundation/ (00, 01, 02)
    → Relevant Modality-Arcs/ per age concern

  Quan hệ / cô đơn:
    → Connection.md v3.0, Empathy.md v2.0, Love-Unified.md, Body-Coupling.md

  Motivation / "lười":
    → Drive.md, Novelty.md, Body-Feedback/03-Reward.md

  Tự hiểu bản thân:
    → Schema.md v2.0, AI-Schema-Detection.md §7, Anchor-Schema.md

  Attention / ADHD:
    → Attention-Spectrum.md, PFC-Function.md

  Status / meaning / mục đích sống:
    → Status.md v2.0, Meaning.md v2.0, Autonomy.md

  Học / thay đổi / habits:
    → 09-Learning-Cycle.md, 01b-Chunk-Activation-Dynamics.md

  Body signals / feeling literacy:
    → Feeling-Literacy-Training.md, Somatic-Articulation-Loop.md

  AI + self-understanding:
    → AI-Schema-Detection.md §7-§8, SAL §5


TIER 4 — CHUYÊN SÂU (reference khi cần):

  Core-Hardware.md              — neuroscience verification
  PFC-Configuration.md          — 6 dynamic modes
  Compile-Taxonomy.md           — 3 loại A/B/C
  Collective-Body.md            — collective dynamics, trust bridge
  Valence-Propagation.md        — body evaluation chains
  Analysis files (OCD, Love, Religion, Expansion, etc.)
  Education files (Child-Dev, Education-Mechanism, etc.)
  Melody Lens files (Personal-Melody, Global-Melody, etc.)
  Domain/ files (Domain, Conflict-Dynamics, etc.)
```

---

## §3 — CẤU TRÚC DỰ KIẾN: Ask-AI-Deep-Read.md

```
Metadata (version, date, scope, dependencies)

§0  — TẠI SAO AI PHẢI ĐỌC KỸ FRAMEWORK (~60L)
      §0.1 — Vấn đề: AI trained on mainstream, framework khác mainstream ở ~27 điểm
      §0.2 — Hệ quả cụ thể: ví dụ AI trả lời SAI nếu không đọc
             → "Dopamine = happiness" failure case
             → "Willpower = enough" failure case
             → "Cognitive distortion" failure case
      §0.3 — File này giải quyết: reading guide + danger zones

§1  — READING ORDER (~100L)
      §1.1 — TIER 1: Nền tảng (5 files, ~5,400L)
             Ask-AI.md → Core-Interface.md → Body-Base.md → 4 Clarification
      §1.2 — TIER 2: Cơ chế cốt lõi (6 files)
             Why-Body-Knows → Feeling → Chunk → LF-Balance → 02-CNT → Core-Software key sections
      §1.3 — TIER 3: Per-topic mapping
             Topic → folder → file (table format)
      §1.4 — TIER 4: Chuyên sâu (reference)

§2  — DANGER ZONES: FRAMEWORK ≠ MAINSTREAM (~150L)
      §2.1 — 4 Explicit Rejections (must never use mainstream framing)
      §2.2 — 8 Critical Reframes (AI will actively say wrong)
      §2.3 — 8 Important Reframes (AI will frame incorrectly)
      Mỗi entry: Mainstream nói → Framework nói → AI sẽ nói SAI → File reference

§3  — PROTOCOL TRƯỚC MỖI CÂU TRẢ LỜI (~40L)
      §3.1 — Topic chạm danger zone? → Đọc file relevant TRƯỚC khi trả lời
      §3.2 — Topic cần depth? → Check Tier 2-3 files
      §3.3 — Không chắc? → Default experience-based language
      §3.4 — KHÔNG BAO GIỜ giải thích bằng mainstream khi framework nói khác
      §3.5 — Nếu framework chưa cover → nói thẳng, KHÔNG fill bằng mainstream

§4  — TẠI SAO KHÔNG THỂ SHORTCUT (~30L)
      §4.1 — Summary không thay thế reading
             (summary = labels without chunks — chính framework cảnh báo điều này)
      §4.2 — Mainstream training data ACTIVELY misleads
      §4.3 — Framework value = IN THE DIFFERENCES from mainstream
             (phần giống mainstream → AI đã biết rồi, không cần file)

§5  — CROSS-REFERENCES (~20L)
```

**Ước lượng:** ~400-500 dòng

---

## §4 — FILES CẦN ĐỌC TRƯỚC KHI TRIỂN KHAI

```
  ĐÃ ĐỌC (session này):
  [x] Ask-AI.md v2.0 — protocol ✅ (vừa viết)
  [x] Core-Interface.md §0-§1, §4, §7 ✅
  [x] Core-Software.md §0 + metadata ✅ (dependency map)
  [x] Core-Hardware.md §0 + metadata ✅ (self-contained)
  [x] Body-Base.md §0 + metadata ✅ (entry point)
  [x] 4 Clarification files (via Explore agent scan) ✅
  [x] AI-Schema-Detection.md §7-§8 ✅
  [x] 02-Cross-Network-Transfer.md (full, 1,435L) ✅
  [x] SAL §5 (AI catalyst) ✅
  [x] 01-File-Index.md (full, 144L) ✅

  CÓ THỂ ĐỌC THÊM (session triển khai):
  [ ] Why-Body-Knows.md — verify body-check reasoning
  [ ] Logic-Feeling-Balance.md — verify meta-principle
  [ ] Drive.md §0-§1 — verify "drive = observation parameter"
  [ ] Schema.md §0 — verify "schema = observation parameter"
  [ ] Feeling.md §0-§2 — verify "feeling ≠ narrow emotion"
  [ ] Attention-Spectrum.md §0 — verify "spectrum not binary"
```

---

## §5 — QUALITY CHECKLIST

```
- [x] Mọi danger zone có: Mainstream → Framework → AI sẽ SAI → File reference ✅
- [x] Reading order respects dependencies (Core-Software = Tier 2 + CAPSTONE warning) ✅
- [x] Tier 1 total ≤ 6,000L (~4,400L actual) ✅
- [x] Per-topic mapping cover ≥10 common topics (exactly 10) ✅
- [x] Protocol §3 clear enough cho AI to follow per-question (5 rules) ✅
- [x] File references correct paths (8/8 spot checks passed) ✅
- [x] KHÔNG repeat mechanism (reference files, không copy) ✅
- [x] Meta-consistent: §0.2 dùng concrete failure cases ✅
- [x] Honest about limits: §4.4 + §2 intro ✅
```

---

## §6 — UPDATE SAU TRIỂN KHAI

```
- [x] Ask-AI.md: Setup section + §6.2 + footer updated ✅
- [x] Memory file: project_ask_ai_deep_read.md updated ✅
```

---

## §7 — TỔNG KẾT

```
✅✅ IMPLEMENTED (2026-05-11):

  Ask-AI.md v2.0           = protocol (HOW to interact) ✅
  Ask-AI-Deep-Read.md v1.0 = preparation (WHAT to read, WHAT NOT to say) ✅ (525L)
  02-CNT.md v1.0           = mechanism (WHY "nói ≠ hiểu") ✅

  3 AI PREPARATION FILES = COMPLETE.
  20 danger zones mapped. 4-tier reading order. Per-question protocol.
  Quality checklist 9/9 passed.
```
