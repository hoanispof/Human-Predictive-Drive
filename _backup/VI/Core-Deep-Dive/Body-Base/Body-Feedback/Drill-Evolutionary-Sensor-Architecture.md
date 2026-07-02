---
title: Drill — Evolutionary Sensor Architecture — Tại sao Body-Feedback PHẢI Như Vậy
version: 1.0
created: 2026-05-25
status: DRILL v1.0
scope: |
  FIRST-PRINCIPLES analysis: TẠI SAO evolution thiết kế body-feedback architecture như vậy.
  Không từ neuroscience observation (bottom-up) — từ evolutionary CONSTRAINT (top-down).
  8 insights: (1) can't make bidirectional sensor, (2) multiple one-way strategy,
  (3) brain integration levels, (4) baseline emergent, (5) WHY Evaluative MUST exist,
  (6) universal approach/avoid, (7) symmetry = functional requirement,
  (8) asymmetric speed in Evaluative layer.
purpose: |
  Dissonance-Signal-Architecture v1.0 answers: WHAT KINDS of dissonance exist (Evaluative/Direct-State).
  Reward-Signal-Architecture v2.0 answers: WHAT KINDS of reward exist (Evaluative/Direct-State).
  Inter-Body-Mechanism.md §9 answers: HOW evolution creates 3-layer stack.
  File này answers: TẠI SAO architecture PHẢI như vậy — từ evolutionary design constraints.
  = "If you were DESIGNING a body, what would you NEED?" → deduce architecture.
position: |
  Body-Feedback/ folder — ngang hàng Reward-Signal-Architecture + Dissonance-Signal-Architecture.
  Drill file — phân tích lưu trữ, complement Reward-Signal-Architecture/Dissonance-Signal-Architecture.
  KHÔNG trùng Inter-Body §9 (3-Layer macro) — file này về sensor-level micro constraints.
dependencies:
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃
  - Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State cho dissonance
  - Body-Feedback-Mechanism.md v2.0 — 2 sources, 3 dynamics
  - Inter-Body-Mechanism.md v2.0 — Compilable Architecture, 3-Layer Evolution
  - Body-Base.md v3.2 — L0, L1, 3 genuine sources, adaptive baseline
  - Cortisol-Baseline.md v2.1 — amplifier, direction > level
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Drill — Evolutionary Sensor Architecture: Tại sao Body-Feedback PHẢI Như Vậy

> **Approach thông thường (bottom-up):** Observe brain → describe architecture → note patterns.
> **Approach file này (top-down):** Nếu thiết kế body, CẦN GÌ? → deduce architecture → check against data.
>
> 3 câu hỏi gốc:
> ① Tại sao evolution KHÔNG tạo sensor bidirectional có trục 0 cố định?
> ② Tại sao Evaluative layer PHẢI tồn tại?
> ③ Tại sao reward và dissonance PHẢI có cùng architecture?
>
> Trả lời: Tất cả follow từ CONSTRAINTS của evolution — random mutation + selection.
> Evolution không có engineer, không có specification, không có fixed zero-point.
> → Mọi thứ về body-feedback architecture = CONSEQUENCE của constraints này.

---

## §0 — SCOPE + READING GUIDE

```
File này DRILL 8 insights từ first-principles reasoning:

  §1: Evolution's Design Constraint — can't make bidirectional sensor
  §2: Multiple One-Way Strategy — TRP channels, CT, nociceptors
  §3: Brain Integration Levels — receptor → spinal → insula
  §4: Baseline is Emergent — adaptive zero, not designed zero
  §5: WHY Evaluative MUST Exist — evolutionary constraint → compilation
  §6: Universal Approach/Avoid — bacteria → humans
  §7: Symmetry = Functional Requirement — information theory
  §8: Asymmetric Speed — survival-first in Evaluative layer
  §9: Connection to Framework Concepts
  §10: Honest Assessment
  §11: Cross-references
```

---

## §1 — EVOLUTION'S DESIGN CONSTRAINT

### §1.1 — Tại sao evolution KHÔNG THỂ tạo bidirectional sensor

```
⭐ ENGINEER vs EVOLUTION — FUNDAMENTALLY KHÁC:

  ENGINEER (thiết kế máy):
    → Có specification: "nhiệt kế đo -40°C → +100°C"
    → Có reference standard: nước đông = 0°C
    → Có material control: chọn thủy ngân, thiết kế thang chia
    → Kết quả: 1 sensor, bidirectional, fixed zero-point

  EVOLUTION (random mutation + selection):
    → KHÔNG có specification — chỉ có "sống hoặc chết"
    → KHÔNG có reference standard — không ai define "0°C"
    → KHÔNG có material control — chỉ có random protein mutation
    → Protein receptor: fire hoặc không fire (threshold-based)
    → KHÔNG THỂ "thiết kế" 1 receptor có trục âm→0→dương

  → Evolution CHỈ có thể tạo: threshold sensors
    → Receptor protein: inactive khi stimulus < threshold
    → Active khi stimulus > threshold
    → = ONE-WAY signal — báo "vượt ngưỡng", KHÔNG báo "bao nhiêu dưới ngưỡng"
```

### §1.2 — Sensor bidirectional cần GÌ mà evolution không có

```
🟡 ĐỂ TẠO 1 SENSOR BIDIRECTIONAL CẦN:

  ① FIXED ZERO-POINT — reference standard cố định
    → Machine: 0°C = nước đông (defined BY ENGINEER)
    → Biology: KHÔNG ai define "baseline" — baseline EMERGE từ system state

  ② LINEAR RESPONSE — output proportional to deviation from zero
    → Machine: thermometer rises/falls linearly
    → Biology: receptor proteins fire ALL-OR-NONE or sigmoid
      → Không có "negative firing rate" (neuron không fire "ít hơn 0")

  ③ NEGATIVE ENCODING — cách báo "dưới baseline"
    → Machine: thermometer drops → column shrinks
    → Biology: neuron KHÔNG THỂ fire negative — chỉ fire hoặc silent
      → Silent KHÔNG phải "negative signal" — silent = "no signal"
      → → Cần SENSOR RIÊNG để báo "dưới baseline"

  → Kết luận: evolution BUỘC dùng multiple one-way sensors
  → KHÔNG PHẢI design choice — là CONSTRAINT của mechanism
```

---

## §2 — MULTIPLE ONE-WAY SENSOR STRATEGY

### §2.1 — Temperature: 3+ receptor types riêng biệt

```
🟢 TEMPERATURE SENSING — CASE ĐƯỢC NGHIÊN CỨU RÕ NHẤT:

  ┌────────────────┬──────────────┬───────────────────────────┐
  │ Receptor       │ Range        │ Báo gì                    │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPM8          │ <26°C        │ "LẠNH" — one-way          │
  │ 🟢 McKemy 2002 │              │ (menthol receptor)        │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPV3, TRPV4   │ 33-39°C     │ "ẤM" — one-way            │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPV1          │ >43°C        │ "NÓNG/ĐAU" — one-way     │
  │ 🟢 Caterina 97 │              │ (capsaicin receptor)      │
  ├────────────────┼──────────────┼───────────────────────────┤
  │ TRPA1          │ <17°C        │ "RẤT LẠNH/ĐAU" — one-way │
  └────────────────┴──────────────┴───────────────────────────┘

  → 4+ loại receptor RIÊNG BIỆT — khác protein, khác gene
  → Mỗi cái = threshold sensor (fire khi stimulus trong range)
  → KHÔNG phải 1 thermometer — là 4 "nút báo" cho 4 vùng khác nhau
  → Brain tích hợp 4 signals → tạo ra "cảm giác nhiệt độ" unified
```

### §2.2 — Touch: 3 hệ riêng biệt

```
🟢 TOUCH SENSING — 3 HỆ ĐỘC LẬP:

  CT afferents: CHỈ fire cho slow gentle touch (1-10 cm/s)
    → "Pleasant touch" sensor — ONE-WAY (chỉ báo "tốt")
    → 🟢 Löken et al. 2009: optimal velocity curve
    → 🟢 Olausson et al. 2002: unmyelinated C fibers

  Nociceptors (A-delta, C fibers): CHỈ fire khi tissue damage/intense pressure
    → "Pain" sensor — ONE-WAY (chỉ báo "xấu")
    → Threshold-based: dưới ngưỡng = silent

  Aβ mechanoreceptors: fire cho ALL touch (discriminative)
    → "Information" sensor — neutral (không tốt/xấu)
    → Meissner, Pacinian, Merkel, Ruffini — 4 subtypes

  → 3 hệ RIÊNG BIỆT cho CÙNG 1 modality
  → Evolution tạo ra: 1 sensor "tốt" + 1 sensor "xấu" + 1 sensor "thông tin"
  → Brain tích hợp 3 hệ → unified touch experience
```

### §2.3 — Taste: sweet vs bitter = riêng hoàn toàn

```
🟢 TASTE — SEPARATE RECEPTOR FAMILIES:

  T1R2/T1R3 heterodimer: SWEET receptor
    → "Caloric, approach" — ONE-WAY
    → 🟢 Nelson et al. 2001

  T2R family (~25 variants): BITTER receptors
    → "Poison, reject" — ONE-WAY
    → Nhiều variants vì: nhiều loại độc → cần nhiều detectors

  → RIÊNG BIỆT hoàn toàn — khác protein, khác gene, khác pathway
  → Evolution KHÔNG tạo 1 "taste-o-meter" có trục ngon→0→dở
  → Tạo 2 hệ riêng: 1 detect "caloric" + 1 detect "poison"
```

### §2.4 — Pattern tổng quát

```
🟡 EVOLUTION'S UNIVERSAL STRATEGY:

  ① Multiple SIMPLE sensors (cheap to evolve: 1 protein = 1 gene)
  ② Each sensor = ONE-WAY, threshold-based (fire hoặc silent)
  ③ Brain INTEGRATES multiple signals → unified representation
  ④ Brain LEARNS baseline from integrated signals (= compilation)

  = "Nhiều sensor đơn giản + 1 brain tích hợp"
  > "1 super-sensor phức tạp"

  TẠI SAO strategy này WIN:
    → 1 gene mutation → 1 new receptor → detect 1 new thing
    → Simple, incremental, each mutation small
    → Brain integration = GENERAL-PURPOSE (Compilable Architecture)
    → → Không cần evolve new integration cho mỗi sensor mới
    → → Thêm sensor → brain automatically integrates

  TẠI SAO super-sensor LOSE:
    → Need multiple coordinated mutations simultaneously
    → Need internal reference standard (no way to evolve)
    → Need linear encoding (proteins don't work this way)
    → → Evolutionary dead end
```

---

## §3 — BRAIN INTEGRATION LEVELS

```
⭐ MANY ONE-WAY INPUTS → ONE BIDIRECTIONAL REPRESENTATION:

  ┌──────────────────┬────────────────────────┬──────────────────┐
  │ Level            │ Processing             │ Representation   │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ RECEPTOR         │ Threshold detection    │ Multiple         │
  │ (da, lưỡi)      │ Each: "above MY range" │ one-way signals  │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ SPINAL CORD      │ Gate control           │ Begin merging    │
  │                  │ (Aβ inhibit C fiber)   │ good/bad signals │
  │                  │ 🟢 Melzack & Wall 1965 │                  │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ BRAINSTEM        │ Converging pathways    │ Multi-modal      │
  │ + THALAMUS       │ Homeostatic regulation │ integration      │
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ POSTERIOR INSULA  │ First-order body map   │ Raw interoceptive│
  │                  │ 🟢 Craig 2002          │ (still Direct-St)│
  ├──────────────────┼────────────────────────┼──────────────────┤
  │ ANTERIOR INSULA  │ + context + evaluation │ Unified          │
  │                  │ 🟢 Craig 2009          │ BIDIRECTIONAL    │
  │                  │                        │ (Eval + Direct-St│
  │                  │                        │  integrated)     │
  └──────────────────┴────────────────────────┴──────────────────┘

  → Bidirectional experience = CREATED by brain, NOT by receptor
  → Receptor: "TRPM8 đang fire" (fact). Brain: "LẠNH hơn baseline" (evaluation)
  → "Prediction-delta" = brain-level concept (không tồn tại ở receptor level)
  → Framework mô tả cái xảy ra từ brainstem trở lên — đúng level
```

---

## §4 — BASELINE IS EMERGENT, NOT DESIGNED

### §4.1 — Machine zero vs Body zero

```
⭐ 2 LOẠI "ZERO" KHÁC NHAU FUNDAMENTALLY:

  MACHINE ZERO (designed):
    → 0°C = nước đông (defined by Celsius, universal)
    → 0V = no potential difference (defined by physics)
    → Fixed, universal, không thay đổi
    → Created BY engineer WITH specification

  BODY ZERO (emergent):
    → 37°C = where warm-sensitive + cold-sensitive neurons fire BALANCED
    → KHÔNG ai "define" 37°C — nó tình cờ là nơi hệ thống cân bằng
    → Adaptive, per-person, shifts over time
    → EMERGES from system dynamics, NOT designed
```

### §4.2 — Adaptive baseline

```
🟡 BODY BASELINE = ADAPTIVE ZERO — SHIFT THEO THỜI GIAN:

  ① HABITUATION: lặp lại → baseline shift UP
    → Café mỗi ngày → body compile "có café" = baseline mới
    → Ngày không có café → deviation FROM NEW baseline → dissonance

  ② SNC (Successive Negative Contrast):
    → Baseline "đã có cái tốt" → downshift → overreact
    → 🟢 Crespi 1942, Flaherty 1996

  ③ COMPILATION depth:
    → Expert baseline KHÁC novice baseline (compiled patterns khác nhau)
    → Musician hears dissonance that non-musician misses

  ④ PER-PERSON variation:
    → COMT genotype → dopamine clearance speed → sensitivity baseline khác
    → DRD4 genotype → novelty threshold khác
    → → "Zero" IS DIFFERENT per person

  → Machine: 1 thermometer = 1 zero, universal
  → Body: mỗi channel × mỗi người × mỗi thời điểm = DIFFERENT zero
  → → Brain MUST continuously RECALIBRATE zero
  → → Recalibration = compilation (learning new baseline)
```

---

## §5 — WHY EVALUATIVE LAYER MUST EXIST

```
⭐ EVALUATIVE LAYER = CONSEQUENCE OF EVOLUTIONARY CONSTRAINT:

  PROBLEM:
    Evolution CANNOT hardcode zero-point (§1)
    → Sensors chỉ báo "vượt ngưỡng" — KHÔNG báo "deviation from baseline"
    → Baseline = emergent (§4) — khác per person, shifts over time
    → → SOMEONE must figure out "baseline CỦA TÔI là gì"
    → → SOMEONE must evaluate "deviation bao nhiêu, hướng nào"

  SOLUTION:
    BRAIN learns baseline through COMPILATION:
    → Experience → body-feedback → Hebbian → compiled pattern = learned baseline
    → New input → compare vs compiled baseline → evaluate deviation
    → = EVALUATIVE PROCESSING

  THEREFORE:
    → Evaluative layer PHẢI tồn tại
    → KHÔNG PHẢI optional feature — là NECESSARY solution cho "no hardcoded zero"
    → Compilable Architecture = brain's answer to evolution's limitation

  DIRECT-STATE = what evolution CAN hardcode:
    → Nociception: tissue damage IS bad (no baseline needed — damage = always bad)
    → CT afferents: gentle touch IS pleasant (no baseline needed — CT pathway = always)
    → Hardware from birth — KHÔNG cần learn baseline
    → = THESE are what evolution can do WITHOUT compilation

  EVALUATIVE = what evolution CANNOT hardcode → brain must learn:
    → "Café buổi sáng có tốt không?" → depends on MY compiled baseline
    → "Bị mẹ mắng có đau không?" → depends on MY Entity-Compiled depth
    → "Công ty phá sản có sợ không?" → depends on MY career compilation
    → = THESE require LEARNED baseline → require Evaluative processing

  → Direct-State = evolution's DIRECT solution (hardcode what's universal)
  → Evaluative = evolution's INDIRECT solution (compile what's individual)
  → 2 types = NECESSARY, not accidental
```

---

## §6 — UNIVERSAL APPROACH/AVOID

### §6.1 — Bacteria → humans: cùng principle

```
⭐ MỌI SINH VẬT SỐNG ĐỀU CẦN APPROACH/AVOID:

  ┌──────────────┬────────────┬──────────────────────────────────┐
  │ Organism     │ Neurons    │ Mechanism                        │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ E. coli      │ 0          │ Chemoreceptors trên membrane     │
  │ (vi khuẩn)   │            │ → swim toward glucose (approach) │
  │              │            │ → tumble away from acid (avoid)  │
  │              │            │ = Direct chemical response       │
  │              │            │ 🟢 Berg & Brown 1972              │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ C. elegans   │ 302        │ Simple circuits                  │
  │ (giun)       │            │ → learned avoidance              │
  │              │            │ → habituation (proto-compile!)   │
  │              │            │ 🟢 Rankin et al. 1990             │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Drosophila   │ ~100K      │ Mushroom body (learning center)  │
  │ (ruồi)      │            │ → conditioned preference/aversion│
  │              │            │ → dopamine reward pathways       │
  │              │            │ 🟢 Waddell 2013                   │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Fish         │ ~10M       │ Pallium (proto-cortex)           │
  │              │            │ → learned fear, social hierarchy │
  │              │            │ → opioid reward system           │
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Dog/Cat      │ ~500M-2B   │ Cortex + limbic                  │
  │              │            │ → Social bonding, learned fear   │
  │              │            │ → E₀-E₂ (food pref, social eval)│
  │              │            │ → Compilation: present but limited│
  ├──────────────┼────────────┼──────────────────────────────────┤
  │ Human        │ ~86B       │ Massive cortex + PFC             │
  │              │            │ → E₀-E₃ (abstract, existential) │
  │              │            │ → Compilation: DEEP (decades)    │
  │              │            │ → "Cuộc đời vô nghĩa" = E₃ only │
  └──────────────┴────────────┴──────────────────────────────────┘

  → Approach/avoid = UNIVERSAL across ALL life
  → KHÔNG phải feature của neuron — là feature của SỐNG
  → Vi khuẩn: chemical gradient. Giun: 302-neuron circuit.
  → Human: 86 billion neurons. SAME PRINCIPLE.
```

### §6.2 — Evaluative/Direct-State qua evolution spectrum

```
🟡 DIRECT-STATE = UNIVERSAL. EVALUATIVE = SCALES WITH COMPILATION:

  Vi khuẩn: Direct-State only (chemical sensor → immediate response)
  Giun (302n): Direct-State + proto-Evaluative (habituation = basic baseline learn)
  Côn trùng: Direct-State + E₀ (hardwired evaluation, mushroom body)
  Cá: Direct-State + E₀-E₁ (opioid pathway, learned preferences)
  Chó/mèo: Direct-State + E₀-E₂ (social evaluation, entity recognition)
  Humans: Direct-State + E₀-E₃ (abstract, existential, decades compilation)

  → Direct-State = evolutionary FLOOR — mọi sinh vật có nervous system
  → Evaluative = scales with COMPILATION CAPACITY
  → More neurons → more compilation → deeper Evaluative → more "types" of suffering AND reward
  → = Trade-off: Compilable Architecture = more adaptation BUT more vulnerability
  → = WHY humans "suffer from thoughts alone" (E₃ Evaluative Dissonance)
    và côn trùng không (chỉ Direct-State)
```

---

## §7 — SYMMETRY = FUNCTIONAL REQUIREMENT

### §7.1 — Information theory argument

```
⭐ ONE-WAY SENSOR = ZERO USEFUL INFORMATION (Shannon 1948):

  Sensor CHỈ báo "mát = sướng" nhưng KHÔNG báo "nóng = vấn đề":
    → Ra trời nắng gắt: KHÔNG signal
    → Vào nhà mát: signal "sướng"
    → NHƯNG: nếu không có signal "nóng" → không biết mát KHÁC GÌ nóng
    → → "Mát = sướng" chỉ có nghĩa NẾU có "nóng = khó chịu" làm reference

  Information = requires CONTRAST:
    → Shannon: signal không bao giờ thay đổi = zero information
    → Signal chỉ đi 1 hướng = half information
    → Signal đi cả 2 hướng = full information
    → → Body NEEDS bidirectional feedback cho mỗi channel

  → KHÔNG THỂ có reward channel mà KHÔNG có dissonance channel tương ứng
  → KHÔNG THỂ có dissonance channel mà KHÔNG có reward channel tương ứng
  → → 2 hướng = functional REQUIREMENT, không phải coincidence
```

### §7.2 — Body cần smooth up/maintain/down axis

```
🟡 ORGANISM CẦN 3 TRẠNG THÁI CHO MỖI PARAMETER:

  ┌──────────────┬──────────────────────────────────────┐
  │ State        │ Organism's need                      │
  ├──────────────┼──────────────────────────────────────┤
  │ IMPROVING    │ "Đang tốt lên" → tiếp tục hành vi   │
  │ (approach)   │ = reward signal                      │
  ├──────────────┼──────────────────────────────────────┤
  │ MAINTAINING  │ "Ổn" → giữ nguyên                    │
  │ (baseline)   │ = no signal / low signal             │
  ├──────────────┼──────────────────────────────────────┤
  │ DEGRADING    │ "Đang tệ đi" → thay đổi hành vi    │
  │ (avoid)      │ = dissonance signal                  │
  └──────────────┴──────────────────────────────────────┘

  Thiếu BẤT KỲ state nào → hệ thống HƯ:
    Chỉ approach (reward only): không biết khi nào degrading → chết vì ignore threats
    Chỉ avoid (dissonance only): không biết khi nào improving → cannot learn what works
    Chỉ maintain (no feedback): zombie → no adaptation possible

  → CẢ 3 states PHẢI có cho MỌI parameter
  → → Reward + dissonance PHẢI cùng tồn tại cho MỌI channel
  → → Architecture cho reward PHẢI symmetric với dissonance
    (vì cùng channel, cùng sensors, cùng integration machinery)
```

### §7.3 — Tại sao CÙNG architecture

```
🟡 REWARD VÀ DISSONANCE DÙNG CÙNG INFRASTRUCTURE:

  Cùng insula gradient: posterior → anterior (🟢 Craig 2002)
  Cùng ACC conflict monitoring (🟢 Botvinick 2004)
  Cùng evaluation machinery (anterior insula + OFC/vmPFC)

  TẠI SAO evolution KHÔNG tạo 2 hệ thống riêng biệt:
    → 2 hệ riêng = 2× cost (double the neural machinery)
    → 2 hệ riêng = synchronization problem (cần coordinate 2 systems)
    → 2 hệ riêng = evolution must evolve BOTH in parallel

  1 hệ bidirectional = cheaper, simpler, auto-synchronized:
    → Same sensors → different direction → different output
    → Same evaluation machinery → applied to both directions
    → Evolution only needs to evolve 1 integration system
    → → Natural selection STRONGLY favors 1 symmetric system over 2 separate
```

---

## §8 — ASYMMETRIC SPEED IN EVALUATIVE LAYER

```
⭐ ARCHITECTURE SYMMETRIC — NHƯNG SPEED ASYMMETRIC — TẠI SAO?

  DIRECT-STATE: tương đối SYMMETRIC speed
    Pain onset ≈ touch onset (cùng hardware speed)
    Pain offset ≈ touch offset (khi stimulus removed)
    → Hardware: symmetric — vì cùng mechanism, cùng receptor dynamics

  EVALUATIVE: STRONGLY ASYMMETRIC speed
    Threat detection: FAST (amygdala ~12ms, bypass PFC)
    Reward evaluation: SLOW (5 Body-Feedback-Preconditions, PFC verify)
    Threat clearance: SLOW (cortisol half-life 60-90 min)
    Reward deactivation: FAST (opioid off in seconds)

  TẠI SAO ASYMMETRIC NẾU CÙNG ARCHITECTURE:
    → Architecture = symmetric (cùng hardware, cùng integration)
    → TIMING = asymmetric (DIFFERENT evolutionary pressure)
    → Evolution TUNE speed independently cho mỗi direction:

    Miss threat (false negative) → CHẾT → gene eliminated
    False alarm threat (false positive) → tốn energy → survive
    → → Threat detection: OPTIMIZE cho SPEED (thà nhầm còn hơn chậm)

    Miss reward (false negative) → bỏ lỡ → survive, find later
    False alarm reward (false positive) → approach danger → CHẾT
    → → Reward evaluation: OPTIMIZE cho ACCURACY (verify trước khi approach)

  → Architecture: symmetric (cùng sensors, cùng brain integration)
  → Speed: asymmetric (different survival cost → different optimization)
  → = Evolution CAN tune speed WITHOUT changing architecture
    (like same car, different gear ratios)

  🟢 Baumeister et al. 2001: "Bad is stronger than good"
  🟢 Kahneman & Tversky 1979: Loss aversion ~2×
  🟢 Rozin & Royzman 2001: Negativity dominance
```

---

## §9 — CONNECTION TO FRAMEWORK CONCEPTS

```
🟡 8 INSIGHTS MAP LÊN FRAMEWORK:

  §1 (can't make bidirectional) →
    Framework's "prediction-delta" = BRAIN-LEVEL concept
    (không phải receptor-level — receptors don't compute delta)

  §2 (multiple one-way) →
    Body-Base.md L1 "17 categories" = multiple one-way sensor channels
    Brain integrates → "body-feedback" = INTEGRATED signal

  §3 (brain integration) →
    Craig's insula gradient = FROM one-way TO bidirectional
    Posterior insula = still one-way (Direct-State)
    Anterior insula = bidirectional (Evaluative + Direct-State integrated)

  §4 (baseline emergent) →
    Body-Base.md: "adaptive baseline" = LEARNED, per-person, shifts
    NOT hardcoded — COMPILED through experience
    = WHY SNC works: baseline CAN shift UP → downshift = overreact

  §5 (WHY Evaluative MUST exist) →
    Evaluative = brain's answer to "no hardcoded zero"
    Evaluative = compilation applied to baseline learning + deviation evaluation
    Compilable Architecture = ENABLES Evaluative layer
    = WHY côn trùng (Hardwired Architecture) = Direct-State only

  §6 (universal approach/avoid) →
    Framework's body-feedback system = HUMAN VERSION of universal principle
    Same principle as bacteria chemotaxis — DIFFERENT depth
    E₀→E₃ = compilation depth gradient

  §7 (symmetry required) →
    Reward-Signal-Architecture + Dissonance-Signal-Architecture = 2 counterpart files = CORRECT
    Reward Evaluative/Direct-State ↔ Dissonance Evaluative/Direct-State
    = SAME architecture, different direction
    = Functional requirement, not coincidence

  §8 (asymmetric speed) →
    Asymmetry in EVALUATIVE (compiled = tunable), not Direct-State (hardware = fixed)
    = WHY "calming down" takes time (Evaluative clearance slow)
    = WHY 1 negative ruins positive experience (Evaluative threat: fast-on, slow-off)
```

---

## §10 — HONEST ASSESSMENT

```
🟢 ESTABLISHED:
  → TRP channels as separate receptor types — 🟢 Caterina 1997, McKemy 2002
  → CT afferents separate from nociceptors — 🟢 Löken 2009
  → Sweet/bitter separate receptors — 🟢 Nelson 2001
  → Insula gradient — 🟢 Craig 2002, 2009
  → Gate control theory — 🟢 Melzack & Wall 1965
  → "Bad is stronger than good" — 🟢 Baumeister 2001
  → Bacteria chemotaxis — 🟢 Berg & Brown 1972
  → C. elegans habituation — 🟢 Rankin 1990

🟡 FRAMEWORK SYNTHESIS:
  → "Evolution can't make bidirectional sensor" = synthesis from known constraints
  → "Evaluative MUST exist because no hardcoded zero" = novel derivation
  → "Symmetry = functional requirement" from information theory = novel
  → "Asymmetry in Evaluative, not Direct-State" = framework insight
  → Spectrum bacteria→humans with E₀→E₃ mapping = framework

🔴 HYPOTHESIS:
  → Exact E₀→E₃ boundaries across species
  → Whether C. elegans habituation truly = proto-Evaluative
  → Precise evolutionary selection mechanism for speed asymmetry tuning
```

---

## §11 — CROSS-REFERENCES

```
PRIMARY:
  → Reward-Signal-Architecture.md v2.0 — reward Evaluative/Direct-State
  → Dissonance-Signal-Architecture.md v1.0 — dissonance Evaluative/Direct-State
  → Body-Feedback-Mechanism.md v2.0 — 2 sources, 3 dynamics
  → Inter-Body-Mechanism.md v2.0 — Compilable Architecture (§1), 3-Layer Evolution (§9)

BODY-BASE:
  → Body-Base.md v3.2 — L0, L1 (17 categories = multiple one-way sensors), adaptive baseline
  → Cortisol-Baseline.md v2.1 — amplifier, direction > level, sustainer
  → Body-Feedback-Label.md v2.0 — vocabulary standard

EVIDENCE:
  → Threat.md — 3 sources, amygdala fast path
  → 02-Dissonance.md — 3 genuine sources (nociception ≈ Direct-State)
  → 03-Reward.md — Body-Feedback-Preconditions, 7-step VTA
```

---

> *"Evolution không có engineer. Không có specification. Không có fixed zero-point.
> → Buộc dùng multiple one-way sensors + brain tích hợp.
> → Brain phải LEARN baseline = compilation = Evaluative layer.
> → Evaluative layer PHẢI bidirectional (reward + dissonance) vì information theory.
> → Architecture symmetric vì cùng infrastructure, speed asymmetric vì khác survival cost.
> → Từ vi khuẩn tới con người: cùng principle, khác depth.
> → Framework không 'thiết kế' architecture — DERIVE nó từ evolutionary constraints."*
