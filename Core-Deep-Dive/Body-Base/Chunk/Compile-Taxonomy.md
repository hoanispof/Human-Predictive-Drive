---
title: Compile-Taxonomy — 1 Engine + Modulator Configurations
version: 3.0
created: 2026-05-08
updated: 2026-06-01 (v3.0 — Architecture reframe: 1 Engine + 3 Modulators)
status: v3.0
scope: |
  ARCHITECTURE REFRAME: ALL compile = Exposure → Hebbian (1 Engine).
  3 Compile Types (Experience/Expertise/Trust) = labels cho dominant modulator configs.
  Trust = AMPLIFIER (gradient Mức 0-5), KHÔNG phải GATE (binary).
  Multi-stream compile: Content/Value/Entity/Behavior chạy SONG SONG.
  Feedback loop: bidirectional, D→B slow/costly, B→D fast/free.
  3 Hardware Constraints + 6 Trade-offs + 4 Pathways (giữ từ v2.0).
  Sleep = Component S offline maintenance (chi tiết → Compile-Sleep.md v1.0).
  Evolutionary gradient: engine conserved, modulators accumulated.
  ~50 research citations. Dựa trên v2.0 + 2 drill sessions (2026-06-01).
purpose: |
  v2.0 organize theo OUTPUT (3 separate types — taxonomy-first).
  v3.0 organize theo MECHANISM (1 engine + modulator configs — mechanism-first).
  v2.0 KHÔNG SAI — patterns ĐÚNG. v3.0 = DEEPER layer: tại sao 3 types exist.
  Reconcile contradiction: Chunk.md §2.3 "gate" vs Entity-Access "gradient."
  ADD: architecture, multi-stream, feedback loop, evolutionary gradient.
  KEEP: 3 hardware constraints, 6 trade-offs, 4 pathways, interactions.
parent: Chunk.md v2.3 (§2 compile mechanisms = foundation)
related: |
  Compile-Sleep.md v1.0 — Component S chi tiết (6 mechanisms)
  Body-Base.md v3.3 §4 — summary 3 Compile Types (reference tới file này)
  Collective-Body.md v2.1 §2 — 4 compile pathways × 3 cấp
  PFC-Operations.md v1.3 — Hold/Suppress, PFC budget
  Chunk.md v2.3 §2 — 4 compile mechanisms + compile_rate formula
  Entity-Valence-Dynamics.md v1.1 — Structural/Current valence
  Entity-Access.md v1.2 §2 — gradient Mức 0-5
  Valence-Propagation.md v4.1 §2 — Trust = valence meta-dimension
  Simulation-Engine.md v1.1 — PFC imagination substrate (Source C2)
  Background-Pattern.md v2.0 — accumulated gist, Source C3
sources: |
  Compile-Taxonomy.md v2.0 — foundation (3 types, 4 pathways, 6 trade-offs)
  Drill-Compile-Architecture.md — raw drill (Source C, Multi-stream, B×D)
  Drill-10-Compile-Architecture.md — refined drill (Trust Reframe, Feedback MAP)
  Drill-11-Compile-Sleep.md — sleep as Component S
  Drill-Compile-Short-Collective.md — original taxonomy drill
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Compile-Taxonomy — 1 Engine + Modulator Configurations

> **4 đứa trẻ "đi học toán" — 4 cơ chế compile KHÁC NHAU.**
> **Nhưng TẤT CẢ đều chạy trên CÙNG 1 ENGINE: Exposure → Hebbian.**
>
> Khác nhau = MODULATOR nào dominant, KHÔNG phải engine nào chạy.
> Experience = engine + minimal modulators (direct exposure).
> Trust = engine + Entity-Valence amplifier (B-dominant).
> Expertise = engine + PFC sustained hold (D-dominant).
>
> **"Muốn con hay chữ thì yêu lấy thầy."**
> = PFC invest → Entity-Valence compile → body auto-receptive → PFC freed.
> = Architecture trong 1 câu tục ngữ.
>
> File này: ARCHITECTURE underneath taxonomy. Tại sao 3 types exist,
> tại sao chúng interact, tại sao chúng overlap.

---

## MỤC LỤC

- §0 — Vị Trí Trong Framework
- §1 — Core Architecture: 1 Engine + 3 Modulators + Sources + Sleep
- §2 — Tại Sao Brain Compile Ngắn: 3 Hardware Constraints
- §3 — Trust Reframe: Amplifier, Not Gate
- §4 — 3 Compile Types = Dominant Modulator Configurations
- §5 — Multi-Stream Compile: Content / Value / Entity / Behavior
- §6 — 4 Compile Pathways: Cùng Output, Khác Cơ Chế
- §7 — Feedback Loop: Bidirectional + Asymmetry
- §8 — 6 Trade-offs Của Compile Ngắn
- §9 — Interactions: Experience vs Trust, Chain Break, External Tools
- §10 — Evolutionary Gradient
- §11 — Edge Cases Verified (8+)
- §12 — Honest Assessment
- §13 — Cross-References

---

## §0 — Vị Trí Trong Framework

```
⭐ FILE NÀY = ARCHITECTURE UNDERNEATH COMPILE TAXONOMY:

  v2.0 (backup/Compile-Taxonomy-v2.0.md):
    Organize theo OUTPUT — "3 separate types" (taxonomy-first).
    Mô tả patterns ĐÚNG nhưng chưa giải thích tại sao.

  v3.0 (file này):
    Organize theo MECHANISM — "1 engine + modulator configurations."
    DEEPER layer: tại sao 3 types exist, interact, overlap.

  Content GIỐNG. Organizing principle KHÁC.
  v2.0 KHÔNG SAI — v3.0 = deeper understanding.


  VỊ TRÍ TRONG FILE HIERARCHY:

    Chunk.md v2.3 §2 (4 compile mechanisms = foundation)
      → [file này] (architecture: 1 engine + modulators + taxonomy)
      → Compile-Sleep.md v1.0 (Component S chi tiết)

    Body-Base.md v3.3 §4 (summary) → [file này] (chi tiết)
    Collective-Body.md v2.1 §2 (4 pathways × 3 cấp) → [file này] (chi tiết pathways)
    PFC-Operations.md v1.3 §2 (Hold/Suppress) → [file này] §1.4 (Modulator D)

    Đọc Chunk.md §2 trước → đọc file này → đọc Compile-Sleep.md.


  WHAT'S NEW IN v3.0:
    ① Architecture: 1 Engine + 3 Modulators + Sources + Sleep (§1)
    ② Trust = Amplifier not Gate (§3) — reconcile Chunk.md §2.3 vs Entity-Access
    ③ Multi-Stream Compile (§5) — Content/Value/Entity/Behavior song song
    ④ Feedback Loop + Asymmetry (§7) — D→B slow, B→D fast
    ⑤ Evolutionary Gradient (§10) — engine conserved, modulators accumulated
    ⑥ Edge Cases verified (§11) — 8+ cases stress-tested
```

---

## §1 — Core Architecture: 1 Engine + 3 Modulators + Sources + Sleep

```
⭐⭐⭐ THESIS CỐT LÕI:

  TẤT CẢ compile đều đi qua 1 con đường duy nhất:

    EXPOSURE → HEBBIAN STRENGTHENING → COMPILED CHUNK

  Không có "trust compile mechanism" riêng.
  Không có "expertise compile mechanism" riêng.
  CHỈ CÓ 1 ENGINE. 3 Compile Types = labels cho dominant modulator config.


  6 OBSERVATIONS HỘI TỤ:

  ① compile_rate formula (Chunk.md v2.3 §2.2):
     compile_rate ≈ f(exposure × saliency × contingency
                      × peak_valence × multi_modal_richness)
     Exposure = tham số NỀN. 4 tham số còn lại = QUALITY of exposure.

  ② 4 compile mechanisms (Chunk.md v2.3 §2.1) = 4 DẠNG exposure:
     Repetition = lặp exposure. Emotional peak = exposure cường độ cực cao.
     Multi-modal = exposure nhiều kênh. Sleep = replay exposure offline.
     KHÔNG có mechanism nào NGOÀI exposure.

  ③ "PFC KHÔNG compile" (PFC-Operations.md v1.3):
     PFC direct attention, hold, imagine, domain-check, change environment.
     TẤT CẢ = tạo/điều hướng exposure. KHÔNG vai trò nào = compile.

  ④ "Imagination = internal body experience":
     Imagine chanh → nước bọt THẬT. Imagine chó cắn → tim đập THẬT.
     Cùng pathways, cùng molecules, khác intensity.

  ⑤ Trẻ bị ép học (no trust) → VẪN compile kiến thức:
     Trust "đóng" nhưng body EXPOSED to content → content compile.
     Trust KHÔNG gate content compile. Trust amplify VALUE compile.

  ⑥ Hebbian = conserved across ALL species:
     Aplysia (Kandel 2000). Cá. Chó (Pavlov 1927). Người.
     Engine GIỐNG. Chỉ khác modulators.

  🟢 Hebbian learning: Hebb 1949
  🟢 LTP: Bliss & Lømo 1973
  🟢 Aplysia Hebbian: Kandel 2000
  🟡 "ALL compile = exposure" as unifying principle: framework synthesis
```

### §1.1 — Engine A: Exposure → Hebbian → Compile

```
🟢🟡 ENGINE A = CƠ CHẾ COMPILE DUY NHẤT:

  ┌───────────────────────────────────────────────────┐
  │                ENGINE A                            │
  │                                                   │
  │  [Exposure] → [Neural Activation] → [Hebbian]     │
  │       ↓              ↓                  ↓          │
  │  Pattern tiếp   Neurons fire      LTP/LTD         │
  │  xúc với brain  together          strengthen/      │
  │                                   weaken           │
  │                        ↓                           │
  │                 [Compiled Chunk]                    │
  │                 (auto-fire khi triggered)           │
  └───────────────────────────────────────────────────┘

  Engine A luôn hoạt động GIỐNG NHAU bất kể:
    Ai cung cấp exposure (mẹ, thầy, tự mình, reality)
    Exposure từ đâu (external, PFC imagination, spontaneous)
    Có trust hay không (trust chỉ AMPLIFY, không thay đổi mechanism)
    PFC có tham gia hay không (PFC chỉ DIRECT, body vẫn compile)


  4 COMPILE MECHANISMS = 4 DẠNG EXPOSURE (Chunk.md v2.3 §2.1):

  ┌────────────────┬──────────────────────┬─────────────────────────┐
  │ Mechanism      │ = Exposure dạng      │ Tại sao compile         │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ① Repetition   │ Lặp exposure nhiều   │ Co-fire nhiều lần       │
  │                │ lần                  │ → connections strengthen │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ② Emotional    │ Exposure cường độ    │ Amygdala + NE → wire    │
  │    peak        │ CỰC CAO (1 lần đủ)  │ CỰC NHANH              │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ③ Multi-modal  │ Exposure NHIỀU KÊNH  │ Cross-cortex co-fire    │
  │                │ cùng lúc             │ → richer binding        │
  ├────────────────┼──────────────────────┼─────────────────────────┤
  │ ④ Sleep        │ Replay exposure      │ Hippocampus replay      │
  │                │ OFFLINE              │ → strengthen/prune      │
  └────────────────┴──────────────────────┴─────────────────────────┘


  NO SOURCE TAG = EVIDENCE CHO 1 ENGINE (Chunk.md v2.3 §1.1):

    Compiled chunks KHÔNG có tag nguồn gốc.
    Chunks từ experience = chunks từ trust = chunks từ PFC-directed.
    = BÌNH ĐẲNG trong body.
    TẠI SAO: vì tất cả qua CÙNG 1 engine (Hebbian LTP).
    Product GIỐNG NHAU → mechanism GIỐNG NHAU.

  🟢 Bliss & Lømo 1973 (LTP)
  🟢 Brown & Kulik 1977 (emotional peak)
  🟢 Stein & Meredith 1993 (multi-modal)
  🟢 Walker 2017 (sleep consolidation)
  🟢 Johnson et al. 1993 (source monitoring — no source tag)
  🟡 4 mechanisms = 4 exposure types: framework synthesis
```

### §1.2 — Modulator B: Entity-Valence Bias (automatic)

```
🟡🟢 MODULATOR B = ENTITY-VALENCE BIAS:

  Entity-Compiled per-entity:
    Structural Valence Profile × Trust dimension
    (Entity-Valence-Dynamics.md v1.1, Valence-Propagation.md v4.1 §2)


  2 CÁCH MODULATE:

    ① AMPLIFY COMPILE RATE (quality):
       Same exposure từ trusted entity → compile MẠNH hơn.
       Mẹ nói "lửa nóng" = auditory + emotional contagion + coupling = RICH.
       Stranger nói "lửa nóng" = auditory only = mỏng.
       Trust KHÔNG thêm gì magical — trust làm CÙNG event bên ngoài
       tạo ra exposure PHONG PHÚ HƠN bên trong body.

    ② BIAS EXPOSURE PROBABILITY (quantity):
       High entity-valence → body AUTO-ATTEND entity đó → MORE exposure.
       Low entity-valence → body AUTO-AVOID → LESS exposure.


  ĐẶC TÍNH:
    AUTOMATIC: compiled, fires without PFC involvement
    COST ≈ 0: compiled patterns run for free
    FAST: fires in milliseconds (subcortical, pre-PFC)
    GRADIENT: Mức 0-5 per entity (Entity-Access.md v1.2), NOT binary
    CAN OVERRIDE PFC: Entity-Valence → PFC (direct, fast)

  Trust = VALENCE META-DIMENSION (Valence-Propagation.md v4.1 §2):
    Trust KHÔNG phải hệ thống riêng biệt.
    Trust = 1 chiều TRONG valence profile per-entity.
    Trust = MULTIPLIER cho toàn bộ profile.

  → Chi tiết Trust Reframe: §3.

  🟢 Social learning modulated by trust: Bandura 1977
  🟢 Emotional contagion: Hatfield et al. 1994
  🟢 Amygdala/subcortical response ~100ms: established neuroscience
  🟡 Entity-Valence as exposure modulator: framework synthesis
```

### §1.3 — Source C: 3 Exposure Sources (song song)

```
🟡🟢 EXPOSURE ĐẾN TỪ 3 KÊNH CHẠY SONG SONG:


  C1: EXTERNAL (body-input from reality)
    Sensory exposure từ environment: visual, auditory, tactile, olfactory, gustatory.
    + Social: facial expressions, prosody, gestures.
    + Actions: motor feedback, proprioception.
    = Body-Feedback-Mechanism.md v2.1 §1.2 ① Hardware/Sensory-Driven.
    ĐẶC ĐIỂM: multi-modal RICHEST, domain-checked, compile SÂU nhất.
    KHÔNG cần PFC. Available cho TẤT CẢ species.
    5 external install mechanisms (Chunk.md v2.3 §2.3) = variants of C1.

  C2: INTERNAL-DELIBERATE (PFC imagination/simulate)
    PFC chủ động tạo internal exposure: imagine scenario, nhẩm từ,
    mental rehearsal, thought experiment, planning, deliberate recall.
    = Simulation-Engine.md v1.1: Constructive Simulation.
    Body REACT with imagination THẬT (nước bọt, tim đập, opioid nhẹ).
    ĐẶC ĐIỂM: flexible, PFC-controlled, abstract domains (toán, lý, triết).
    GIỚI HẠN: nghèo multi-modal hơn C1, self-referencing risk, PFC budget.
    Human-dominant (PFC developed).

  C3: INTERNAL-AUTOMATIC (spontaneous chunk fire)
    Compiled chunks tự fire (KHÔNG PFC direct):
    ① Background-Pattern continuous baseline (Background-Pattern.md v2.0)
    ② Spontaneous memory resurface (context trigger → old chunk fires)
    ③ Association chains (chunk A → chunk B → chunk C cascade)
    ④ Mind wandering (DMN activate → 30-50% waking time)
    ⑤ Intrusive patterns (trauma replay, rumination — negative C3)
    = Body-Feedback-Mechanism.md v2.1 §1.2 ② Pattern-Driven.
    ĐẶC ĐIỂM: cost ≈ 0, self-reinforcing (strong → fire → stronger).
    REQUIRES compiled chunks (C3 KHÔNG hoạt động ở newborn).


  3 SOURCES × SONG SONG, TỈ LỆ BIẾN THIÊN:

  ┌─────────────────────┬──────┬──────┬──────┐
  │ Tình huống          │  C1  │  C2  │  C3  │
  ├─────────────────────┼──────┼──────┼──────┤
  │ Bé 6 tháng chơi    │ 90%  │  2%  │  8%  │
  │ Trẻ bị ép học      │ 60%  │  5%  │ 35%  │
  │ Sinh viên đọc sách │ 40%  │ 40%  │ 20%  │
  │ Expert suy nghĩ    │ 10%  │ 60%  │ 30%  │
  │ Nằm mơ (REM)       │  0%  │  0%  │100%  │
  └─────────────────────┴──────┴──────┴──────┘
  (% = ƯỚC LƯỢNG minh hoạ, KHÔNG phải đo lường chính xác.)


  PFC × SOURCES:
    PFC CAN amplify C1 (chú ý nghe, đi thực hành) + C2 (nhẩm, imagine).
    PFC CANNOT directly control C3 (Background-Pattern fires tự động).
    PFC suppress C3 = Modulator D cost, KHÔNG tắt được C3 source.
    → PFC = DIRECTOR cho C1+C2, OBSERVER cho C3.

  C1 + C2 + C3 → ALL feed vào CÙNG Engine A.
  Engine A KHÔNG phân biệt nguồn (Chunk.md v2.3 §1.1: NO SOURCE TAG).

  🟢 Mind wandering 30-50%: Smallwood & Schooler 2006
  🟢 Motor imagery → body response: Jeannerod 2001
  🟢 DMN activation: Raichle et al. 2001
  🟢 Ironic process (C3 suppress → rebound): Wegner 1987
  🟢 Input hypothesis: Krashen 1982
  🟡 3-source parallel model: framework synthesis
```

### §1.4 — Modulator D: PFC Hold + Suppress (deliberate)

```
🟡🟢 MODULATOR D = PFC OPERATIONS (PFC-Operations.md v1.3):


  2 OPERATIONS:

  D1: HOLD = PFC Amplify
    Top-down signal → amplify target pattern → TĂNG exposure quality.
    CAN lead to compilation (Hold → repeat → Hebbian → automatic → PFC freed).
    Cost: ① PFC draft (processing load). Brain: dlPFC, FEF.

  D2: SUPPRESS = PFC Inhibit
    Inhibitory signal → block output route.
    GIẢM exposure cho specific pattern.
    CANNOT compile "not" (only block, not build — Wegner 1987).
    Cost: ② Efference mismatch. Brain: rIFG, vlPFC.


  4 TỔ HỢP D1 × D2 (PFC-Operations.md v1.3 §3):

    ① Hold only         → compile new (easiest path)
    ② Hold + Suppress   → override old + build new (double cost)
    ③ Suppress only     → block only, no replacement (ALWAYS fails)
    ④ Neither           → compiled auto-fire (PFC not involved)


  PFC = DIRECTOR, BODY = COMPILER:

    ❌ "PFC compile" = SAI (PFC không compile)
    ✅ "PFC-directed body compile" = CHÍNH XÁC

    PFC 5 vai trò (PFC-Operations.md v1.3):
      ① Direct attention    ② Hold in working memory
      ③ Imagine/simulate    ④ Domain-check
      ⑤ Change environment
    MỖI vai trò = modulate exposure. KHÔNG vai trò nào = compile.


  ĐẶC BIỆT — MODULATOR D = ONLY MODULATOR CÓ COST:
    Modulator B (Entity-Valence): cost ≈ 0 (compiled, automatic)
    Modulator D (PFC Hold/Suppress): cost ① + ② (active, fatigable)
    PFC budget = finite → Modulator D = TEMPORARY
    Mục tiêu: D1 Hold → compile → release (transfer to automatic)

  🟢 PFC Hold: Baddeley 2003, Miller & Cohen 2001
  🟢 PFC Suppress: Anderson & Green 2001, Aron 2007
  🟢 Suppress fails alone: Wegner 1987
  🟡 Hold/Suppress as Modulator D: framework synthesis
```

### §1.5 — Component S: Sleep Offline Maintenance

```
🟡🟢 COMPONENT S = SLEEP OFFLINE MAINTENANCE SYSTEM:

  Sleep KHÔNG ĐƠN THUẦN là "exposure source" thứ 4.
  Sleep có 6 mechanisms — chỉ ~1.5 exposure-based, ~4.5 optimization.

  ┌────┬──────────────────┬─────────────┬──────────────────────┐
  │ #  │ Mechanism         │ Exposure?   │ Primary function     │
  ├────┼──────────────────┼─────────────┼──────────────────────┤
  │ S1 │ SHY Homeostasis   │ ❌ NOT      │ Prune weak (SNR)     │
  │ S2 │ Hippocampal Replay│ ✅ YES      │ Strengthen existing  │
  │ S3 │ Active Consol.    │ ❌ NOT      │ Transfer (RAM→ROM)   │
  │ S4 │ Creative Linking  │ 🟡 PARTIAL  │ New remote links     │
  │ S5 │ Emot. Decoupling  │ ❌ NOT      │ Strip emotional tag  │
  │ S6 │ Gist Extraction   │ 🟡 PARTIAL  │ Abstract + generalize│
  └────┴──────────────────┴─────────────┴──────────────────────┘

  Cycle: Waking (build) → Sleep (maintain) → Waking (build on maintained).

  → CHI TIẾT: Compile-Sleep.md v1.0 (6 mechanisms, architecture interaction,
    sleep deprivation, waking rest comparison, ~40 citations).

  🟢 Multi-mechanism sleep model: Diekelmann & Born 2010
  🟡 Component S in compile architecture: framework synthesis
```

---

## §2 — Tại Sao Brain Compile Ngắn: 3 Hardware Constraints

```
🟢🟡 3 CONSTRAINTS ĐỘC LẬP CÙNG CHỈ VỀ COMPILE NGẮN:


  ① PFC ~4±1 SLOTS = PHYSICS LIMIT:

     PFC-Hold-Dimensions.md §2: 6 lực ĐỘC LẬP hội tụ tại ~4:
       Toán tổ hợp: marginal gain đạt đỉnh ở 3→4
       Cấu trúc thế giới: ~2-4 biến nhân quả chính per situation
       False positive: >4 chiều → signal-to-noise SỤP
       Interference: >4 → oscillations collide
       Energy: maintain mỗi chiều = TỐN processing load
       Evolution: không ĐỦ áp lực chọn lọc cho >4

     → Chain > 4 nodes = VƯỢT single PFC processing capacity
     → = Hardware limit, KHÔNG phải "lười biếng"

     🟢 Working memory ~4±1: Cowan 2001 (highly cited meta-analysis)


  ② PROCESSING SPEED: PFC ~200ms+, AMYGDALA ~12ms:

     PFC LUÔN CHẬM hơn subcortical response.
     Chain dài = PFC process CHẬM → body ĐÃ respond trước.
     Evolution ưu tiên NHANH cho survival.
     Compile ngắn = nhanh hơn = survival advantage.

     🟢 Amygdala response ~12ms: LeDoux 1996
     🟢 PFC response ~200ms+: established neuroscience


  ③ CORTISOL COST: CHAIN DÀI = ACTIVE LOCK → CORTISOL SUSTAINED:

     PFC hold chunks → Active Lock → cortisol.
     Cortisol-Baseline.md v2.2: sustained cortisol → neural wear.
     Chain dài → PFC hold LÂU → cortisol LÂU → TỐN chi phí.
     Compile ngắn → PFC hold ÍT → cortisol ÍT → tiết kiệm sinh học.

     🟢 Cortisol + sustained cognitive load: Lupien et al. 2009


  ⭐ CONVERGENCE — 3 CONSTRAINTS CÙNG HƯỚNG:

    PFC capacity:     chain dài = VƯỢT giới hạn
    Processing speed:  chain dài = QUÁ CHẬM
    Energy cost:       chain dài = QUÁ ĐẮT
    → Brain BUỘC compile ngắn = KHÔNG phải lựa chọn

    Analogy: mắt con người chỉ có 3 loại cone (RGB).
    Phổ ánh sáng = liên tục. Nhưng survival chỉ CẦN 3 trục.
    → PFC ~4 slots: nhân quả survival chỉ cần ~4 chiều → KHÔNG thêm.

  🟡 3-constraint convergence model: framework synthesis
  🟢 Components individually established (Cowan 2001, LeDoux 1996, Lupien 2009)
```

---

## §3 — Trust Reframe: Amplifier, Not Gate

### §3.1 — Contradiction detected

```
🟡 CONTRADICTION TRONG FRAMEWORK:

  SOURCE 1 — Chunk.md v2.3 §2.3 line 288:
    "TRUST = GATE CHO EXTERNAL INSTALL"
    → Ngôn ngữ "gate" = BINARY (mở/đóng).

  SOURCE 2 — Entity-Access.md v1.2 §2:
    "gradient Mức 0-5 per-entity"
    → Ngôn ngữ "gradient" = CONTINUOUS (0→1→2→3→4→5).

  SOURCE 3 — Trẻ bị ép học:
    Trust "đóng" (trẻ không tin học tốt).
    NHƯNG content vẫn compile qua forced exposure.
    → "Gate" = sai cho content compile.

  → "GATE" và "GRADIENT" contradict.
  → "GATE" và "content compile without trust" contradict.
```

### §3.2 — Resolution: Amplifier model (Mức 0-5)

```
🟡 TRUST = AMPLIFIER (GRADIENT), KHÔNG PHẢI GATE (BINARY):

  ┌────────────┬──────────────────────────────────┐
  │ Mức 0      │ Multiplier ≈ 0 → compile rate    │
  │ (stranger) │ CỰC THẤP từ entity này           │
  │            │ (LOOKS like gate = off)           │
  ├────────────┼──────────────────────────────────┤
  │ Mức 1      │ Multiplier thấp → cần NHIỀU      │
  │ (acquaint) │ exposure bù                      │
  ├────────────┼──────────────────────────────────┤
  │ Mức 2-3    │ Multiplier trung bình → compile   │
  │ (friend)   │ rate bình thường                  │
  ├────────────┼──────────────────────────────────┤
  │ Mức 4      │ Multiplier cao → ít exposure     │
  │ (partner)  │ vẫn compile                      │
  ├────────────┼──────────────────────────────────┤
  │ Mức 5      │ Multiplier MAX → 1-2 lần         │
  │ (self/     │ exposure = compile sâu            │
  │  child)    │                                  │
  └────────────┴──────────────────────────────────┘

  "Gate" = limit case CỦA amplifier khi multiplier → 0.
  Gate behavior ĐÚNG ở Mức 0. Nhưng KHÔNG đúng cho toàn bộ spectrum.
  "Amplifier" bao hàm cả gate behavior + gradient behavior.

  VÍ DỤ KIỂM CHỨNG:
    Mẹ nói "học đi con" → trust Mức 4-5 → ít lần nói đã compile [học → tốt]
    Người lạ nói "nên học nghề A" → trust Mức 0-1 → cần nghe NHIỀU người nói
    Bạn thân nói "thử nhạc jazz đi" → trust Mức 2-3 → vài lần + experience

  🟢 Entity-Access gradient Mức 0-5: Entity-Access.md v1.2 §2
  🟢 Trust = valence meta-dimension: Valence-Propagation.md v4.1 §2
  🟡 Trust = amplifier (not gate): framework synthesis
```

### §3.3 — Trust scope: VALUE vs CONTENT

```
⭐ PHÂN BIỆT QUAN TRỌNG:

  ┌────────────────────┬────────────────────┬─────────────────────┐
  │ Compile stream     │ Trust role          │ Ví dụ               │
  ├────────────────────┼────────────────────┼─────────────────────┤
  │ CONTENT compile    │ KHÔNG amplify      │ Trẻ bị ép → vẫn     │
  │ (knowledge, skill) │ (exposure alone    │ compile toán.        │
  │                    │ = đủ for content)  │ Không cần tin mẹ.    │
  ├────────────────────┼────────────────────┼─────────────────────┤
  │ VALUE compile      │ AMPLIFY            │ Mẹ nói "học tốt" →  │
  │ ([X → good/bad])   │ (trust = multiplier│ trust mẹ → compile   │
  │                    │ cho value install) │ [học → tốt] NHANH.   │
  ├────────────────────┼────────────────────┼─────────────────────┤
  │ ENTITY compile     │ IS the trust weight│ Trust weight chính   │
  │ (trust itself)     │ being compiled     │ nó = sản phẩm compile│
  │                    │                    │ từ direct experience.│
  └────────────────────┴────────────────────┴─────────────────────┘

  ⭐ "GIỎI NHƯNG GHÉT HỌC" = ARCHITECTURE PREDICTION:
    Content stream: compile thành công (exposure → knowledge) ✓
    Value stream: compile thất bại (amplifier ≈ 0 cho [học → tốt]) ✗
    → Có kiến thức, KHÔNG có [học → tốt] value compiled.
    → Architecture predicts this. "Gate" model cannot.

  → Trust amplify VALUE install, KHÔNG amplify content compile.
  → Chi tiết multi-stream: §5.

  🟡 Trust scope (Value vs Content): framework synthesis
  🟢 Hebbian indifferent to source: established neuroscience
```

---

## §4 — 3 Compile Types = Dominant Modulator Configurations

### §4.1 — Experience Compile: Engine A + Minimal Modulators

```
🟡🟢 EXPERIENCE COMPILE — DIRECT EXPOSURE → HEBBIAN → COMPILE:

  MODULATOR CONFIG:
    Engine A: ✅ Full (Hebbian direct)
    Modulator B: Minimal (direct verify, trust optional)
    Sources: C1 dominant (body-input from reality)
    Modulator D: Minimal (body direct, PFC không cần)

  = "Thuần engine" — modulators ở mức background.

  MECHANISM:
    [action → sensory result → body evaluation → compile]
    Body trải nghiệm trực tiếp → body tự wire → chunk hình thành.

  VÍ DỤ:
    [cho → người nhận vui → ấm]    → compiled [cho → ấm]
    [chạm lửa → nóng → đau]       → compiled [lửa → tránh]
    [ăn ngon → opioid]             → compiled [quán này → tốt]

  ĐẶC ĐIỂM:
    ✅ MẠNH NHẤT: multi-modal (thấy + nghe + chạm + cảm xúc → wire deep)
    ✅ NHANH NHẤT: không cần PFC deliberation, amygdala ~12ms
    ❌ PHẠM VI HẸP: chỉ compile cái ĐÃ trải nghiệm trực tiếp

  ~90% behavior hàng ngày = Experience compiled patterns fire tự động.

  🟢 Hebbian learning: Hebb 1949
  🟢 Positive/negative reinforcement: Skinner 1953, Rescorla & Wagner 1972
  🟡 ~90% estimate: framework approximation
```

### §4.2 — Trust Compile: Engine A + Modulator B Dominant

```
🟡 TRUST COMPILE — ENTITY-VALENCE AMPLIFY VALUE INSTALL:

  MODULATOR CONFIG:
    Engine A: ✅ Full (Hebbian — cùng engine)
    Modulator B: ⭐ DOMINANT (trust = multiplier amplify value)
    Sources: C1 từ trusted source
    Modulator D: Low (chọn trust ai + post-hoc confabulation)

  = "Engine + auto-turbo from Entity-Valence."

  MECHANISM:
    Trust source → body nhận input → compile [action→result] SHORT.
    Chain dài NẰM Ở collective (CẤP 2), KHÔNG ở individual (CẤP 1).

  VÍ DỤ:
    Trẻ: trust mẹ → compile [học → tốt]
      Collective hold: [học → đại học → việc → lương → body-base feed]
    Ngôn ngữ: trust môi trường → compile [từ → nghĩa]
      Collective hold: [hệ thống ngữ pháp + từ vựng + pragmatics]

  5 DẠNG TRUST SOURCE:
    ① Mẹ / caregiver: FOUNDATIONAL trust (Mức 4-5)
    ② Thầy/cô: DELEGATED trust (trust inherit qua mẹ)
    ③ Tập thể: CONSENSUS trust (social proof — Cialdini 1984)
    ④ Kinh sách / hệ thống: COMPILED trust (unfalsifiable)
    ⑤ Lãnh đạo: COUPLING trust (Body-Coupling.md v3.0)

  ĐẶC ĐIỂM:
    ✅ NHANH: bypass chain verification qua trust
    ✅ RỘNG: access collective knowledge mà không cần experience riêng
    ❌ PHỤ THUỘC COLLECTIVE: chain gãy → cá nhân gánh
    ❌ DỄ BỊ EXPLOIT: trust wrong source → compiled sai

  ⭐ TRUST COMPILE = PHẦN LỚN SOCIAL BEHAVIOR:
    Ngôn ngữ, đạo đức, skill xã hội, world knowledge, religious beliefs,
    political views, career expectations = TẤT CẢ Trust Compile installed.

  🟢 Cultural transmission: Boyd & Richerson 1985
  🟢 Social learning: Bandura 1977
  🟢 Social proof: Cialdini 1984
  🟡 Trust Compile dominance insight: framework synthesis
```

### §4.3 — Expertise Compile: Engine A + Modulator D Dominant

```
🟡🟢 EXPERTISE COMPILE — PFC-DIRECTED SUSTAINED EXPOSURE:

  MODULATOR CONFIG:
    Engine A: ✅ Full (Hebbian — cùng engine)
    Modulator B: Low (self-verify via Domain-Checked)
    Sources: C1 + C2 balanced (practice + imagination)
    Modulator D: ⭐ DOMINANT (PFC sustained hold × years)

  = "Engine + manual turbo from PFC (costly, slow)."

  MECHANISM:
    Experience NHIỀU LẦN → chunks → meta-chunks → pyramidal compression.
    PFC DIRECT attention qua nhiều năm → vô thức compile SÂU.

  VÍ DỤ:
    Expert chess: 50,000+ patterns → "cảm nhận" thế cờ
    Bác sĩ 20 năm: "nhìn bệnh nhân biết ngay"
    Einstein: decades → E=mc² = 1 meta-chunk (bên trong = decades compiled)

  PFC DIRECT qua 5 cách (KHÔNG có cách nào là compile):
    ① Direct attention vào domain cụ thể
    ② Hold ~4 chunks active → co-fire → body wire
    ③ Imagine/simulate scenario → body react + compile
    ④ Domain-check: verify smooth vs reality
    ⑤ Change environment → body-input mới

  External tools EXTEND (Collective-Body.md v2.1 §3.3):
    PFC hold 4 → viết ra → PFC freed → hold 4 tiếp → STACK
    = "Cấp 2 cá nhân": giấy, máy tính, database, AI

  ĐẶC ĐIỂM:
    ✅ CHÍNH XÁC NHẤT: calibrated qua domain feedback
    ❌ CHẬM NHẤT: cần YEARS trong 1 domain (Chase & Simon 1973: ~10 years)
    ❌ DOMAIN-SPECIFIC: Einstein = expert vật lý + novice cooking

  ~5% behavior = khi cá nhân hoạt động TRONG expert domain.

  🟢 Expert chess 50,000+: Chase & Simon 1973
  🟢 Neural efficiency: Haier 1992, Neubauer & Fink 2009
  🟢 Deliberate practice ~10 years: Ericsson et al. 1993
  🟢 Extended mind: Clark & Chalmers 1998
  🟡 "PFC-directed body compile": framework terminology
```

### §4.4 — Bảng So Sánh: 1 Engine + 3 Configs

```
🟡 COMPARISON TABLE — 3 CONFIGS CỦA CÙNG 1 ENGINE:

  ┌──────────────────┬─────────┬──────────┬──────────┬──────────┐
  │ COMPILE TYPE     │ ENGINE  │ MOD B    │ SOURCES  │ MOD D    │
  │                  │    A    │ (Entity- │ (C1/C2/  │ (PFC)    │
  │                  │         │ Valence) │ C3)      │          │
  ├──────────────────┼─────────┼──────────┼──────────┼──────────┤
  │ EXPERIENCE       │ ✅ Full  │ Minimal  │ C1       │ Minimal  │
  │ (~90%)           │         │ (direct  │ dominant │ (body    │
  │                  │         │ verify)  │          │ direct)  │
  ├──────────────────┼─────────┼──────────┼──────────┼──────────┤
  │ TRUST            │ ✅ Full  │ ⭐ HIGH  │ C1 from  │ Low      │
  │ (overlap)        │         │ (amplify │ trusted  │ (chọn    │
  │                  │         │ value)   │ source   │ trust)   │
  ├──────────────────┼─────────┼──────────┼──────────┼──────────┤
  │ EXPERTISE        │ ✅ Full  │ Low      │ C1+C2    │ ⭐ HIGH  │
  │ (~5%)            │         │ (self-   │ balanced │ (PFC     │
  │                  │         │ verify)  │          │ years)   │
  └──────────────────┴─────────┴──────────┴──────────┴──────────┘

  ENGINE A = LUÔN FULL. Sự khác biệt = MODULATOR nào DOMINANT.

  ⚠️ LƯU Ý QUAN TRỌNG:
    ~90% + ~5% + Trust = KHÔNG cộng thành 100% vì overlapping.
    Ranh giới Experience/Trust KHÔNG binary → SPECTRUM.
    VD: [ăn ngon → ấm] = Experience (direct) + Trust (cultural "ngon").
    Phần lớn real-world compile = MIX nhiều modulators.

  TẠI SAO VẪN HỮU ÍCH GIỮ 3 LABELS:
    "Experience" = nói nhanh: engine dominant, direct exposure.
    "Trust" = nói nhanh: Entity-Valence dominant.
    "Expertise" = nói nhanh: PFC dominant.
    = Labels cho DOMINANT config, không phải separate mechanisms.
    = Giống "đi bộ / chạy / leo núi" = useful labels dù cùng cơ mechanism.

  🟡 3 types as modulator configs: framework synthesis
  🟡 Percentage estimates: framework approximation, not precise
```

---

## §5 — Multi-Stream Compile: Content / Value / Entity / Behavior

### §5.1 — 4 Streams chạy đồng thời

```
⭐⭐ MỌI SITUATION = NHIỀU COMPILE STREAMS CHẠY ĐỒNG THỜI:

  ┌───────────────┬─────────────────────┬────────────────────┐
  │ STREAM        │ WHAT COMPILES       │ MODULATOR DOMINANT │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ① CONTENT     │ Nội dung, kiến thức │ Engine A only       │
  │               │ Facts, skills       │ (Experience type)   │
  │               │ Procedures, data    │ Minimal B/D         │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ② VALUE       │ Đánh giá tốt/xấu   │ B (Entity-Valence)  │
  │               │ Approach/avoid tag  │ Trust-amplified     │
  │               │ "Cái này có tốt?"   │                     │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ③ ENTITY      │ Entity-Valence      │ B (update weights)  │
  │               │ Trust update        │ Per-entity compile  │
  │               │ "Người này đáng tin?"│                     │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ④ BEHAVIOR    │ Approach/avoidance  │ Direction-At-Compile│
  │               │ Motor-association   │ (Chunk.md v2.3 §2.4)│
  │               │ Habit formation     │ Valence direction   │
  └───────────────┴─────────────────────┴────────────────────┘

  Content stream LUÔN = Experience Compile (Engine A, direct exposure).
  Value stream = Trust-modulated (B amplify/suppress).
  → "Trust Compile" = chủ yếu VALUE stream (B-dominant), KHÔNG phải content.
  → Content VẪN compile qua Experience (Engine A alone).
```

### §5.2 — Test case: Trẻ bị ép học (4 streams visible)

```
🟡 TEST CASE — TRẺ BỊ MẸ ÉP HỌC TOÁN:

  ① Content:  [2+2=4], [phép nhân], [công thức]
     → Engine A qua C1 (ngồi đọc sách) → compile ✓
     → Trust KHÔNG ảnh hưởng (content = direct exposure)

  ② Value:    [học → sợ bị mắng → tránh bị mắng → "phải làm"]
     → Engine A + context: threat direction → compile ✓ nhưng AVOIDANCE
     → Trust cho "học = tốt" KHÔNG compile ✗ (amplifier ≈ 0)

  ③ Entity:   [mẹ + ép] → Entity-Valence update
     → [mẹ] structural valence: mixed (yêu thương + ép buộc)
     → compile ✓ (direct experience)

  ④ Behavior: [nghe mẹ → ngồi xuống → mở sách]
     → Motor-association compile: avoidance-driven habit → compile ✓

  = 4 streams ĐỘC LẬP. 3/4 compile. 1/4 không (value).
  = "Giỏi nhưng ghét học" = ①✓ ②✗.
  = "Sợ mẹ nhưng không yêu mẹ" = ④✓ ③mixed.
```

### §5.3 — Test case: Trẻ học với thầy yêu quý (4 streams positive)

```
🟡 TEST CASE — SINH VIÊN THÍCH GIÁO SƯ, THÍCH MÔN HỌC:

  ① Content:  [lý thuyết], [phương pháp], [thuật ngữ]
     → Engine A qua C1 (nghe giảng) + C2 (suy nghĩ bài tập) → compile ✓

  ② Value:    [môn này = thú vị → approach]
     → Trust amplify: GS nói "phần này quan trọng" → body amplify → compile ✓

  ③ Entity:   [giáo sư] → Entity-Valence STRENGTHEN positive
     → Trust tăng → future value amplification TĂNG → compile ✓

  ④ Behavior: [đến lớp đúng giờ → ngồi hàng đầu → hỏi câu hỏi]
     → Approach-driven habit → compile ✓

  = 4 streams ALL positive. = Lý tưởng.
  = Approach direction → sustainable, low cortisol cost.
```

### §5.4 — Implication: Can thiệp giáo dục cần biết stream nào thất bại

```
🟡 IMPLICATION:

  Can thiệp giáo dục CẦN biết STREAM NÀO đang thất bại:
    Content ✗: cần thêm exposure (thời gian, practice)
    Value ✗: cần build trust TRƯỚC (entity-valence toward teacher/subject)
    Entity ✗: cần fix relationship (teacher-student dynamic)
    Behavior ✗: cần thay đổi direction (approach, not avoidance)

  Sai stream → sai can thiệp → "cố gắng hơn" mà không hiệu quả.

  🟡 4-stream multi-stream model: framework synthesis
  🟢 Hebbian concurrent: multiple patterns strengthen simultaneously
  🟢 Direction-At-Compile: Chunk.md v2.3 §2.4
```

---

## §6 — 4 Compile Pathways: Cùng Output, Khác Cơ Chế

```
🟡 4 PATHWAYS — TEST CASE: "CÙNG LÀ HỌC SINH ĐI HỌC TOÁN":

  THỰC TẾ — 4 đứa trẻ, 4 compile pathways KHÁC NHAU:


  ① HARDWARE FIT (Experience Compile — direct short):

     [toán → brain fire → Goldilocks zone → VTA → opioid]
     = "Tự thấy thú vị." CẤP 1 direct.
     MODULATOR CONFIG: Engine A + minimal B/D, C1, novelty direction.
     Trust: KHÔNG CẦN. Chain length: 1 node.

     Novelty.md: Goldilocks zone = task difficulty ≈ current capacity
     → VTA fire → dopamine → body pursue → opioid
     → = Hardware fit, KHÔNG phải "có năng khiếu bẩm sinh"


  ② TRUST + MODERATE FIT (Trust + Experience — compound):

     Bố mẹ nói "học quan trọng" → trust → compile [học → tốt]
     + Tự học → hợp hardware → cost vừa phải → status
     = CẤP 1: [học → mẹ khen + điểm + status → body ấm] (2 nodes)
     = CẤP 2: bố mẹ hold chain dài [học → tương lai → body-base]
     MODULATOR CONFIG: Engine A + B + partial D, C1.
     Trust: HIGH (bố mẹ). Verify: PARTIAL (direct experience confirm).

     → COMPOUND: Trust install + Experience confirm = CỰC BỀN.
     → = Phổ biến nhất? Nhiều học sinh = MIX pathway ①②


  ③ SOCIAL DEFAULT (Trust Compile — installed pure):

     "Thấy ai cũng đi học → đương nhiên mình cũng đi"
     = CẤP 1: [mọi người đều học → bình thường → tôi cũng] (1 node)
     MODULATOR CONFIG: Engine A + B social proof, C1, minimal D.
     Trust source: QUANTITY (social proof — Cialdini 1984).

     → "Compile" thậm chí KHÔNG CẦN body experience mạnh
     → Chỉ cần social environment → body auto-conform


  ④ THREAT AVOIDANCE (Experience Compile — direct short):

     [không học → mẹ mắng / bị đánh → threat → học để avoid]
     = CẤP 1 direct. Chain length: 1-2 nodes.
     MODULATOR CONFIG: Engine A + minimal B, C1, threat direction.
     Trust: KHÔNG CẦN (direct threat experience).

     → Chunk.md v2.3 §2.4: threat direction → compile WITH avoidance
     → Cortisol-tagging: compiled [không học → nguy hiểm]


  ⭐ HỘI TỤ — 4 PATHWAYS, 1 OUTPUT:

     4 pathways KHÁC NHAU → cùng output: "đi học"
     TẤT CẢ compile SHORT ở CẤP 1 (1-2 nodes)
     Chain DÀI nằm ở CẤP 2 (collective)
     → Cùng engine. Khác modulator configs. Khác direction.


  GIÁ TRỊ THỰC CỦA 4 PATHWAYS:

    ① Hiểu tại sao CÙNG hành vi = KHÁC mechanism
       → Can thiệp giáo dục CẦN biết học sinh đi theo pathway nào
    ② Pathway ④ (threat) = compile tốt nhưng cortisol cost CAO
    ③ Pathway ①② = sustainable hơn (approach direction)
    ④ Giáo dục TỐT = tạo điều kiện cho pathway ①② thay vì ④

  🟡 REWARD IMPLICATION (Reward-Signal-Architecture.md v2.1 §8.4):
    4 pathways → khác Precondition-5 tags → khác reward capacity ở người lớn:
    ① Hardware Fit → approach tag → flow accessible
    ② Trust + moderate → depends on collective chain
    ③ Social Default → neutral tag → relief dominant
    ④ Threat Avoidance → avoidance tag → burnout trajectory

  🟡 4 compile pathways model: framework synthesis
  🟢 Social proof: Cialdini 1984
  🟢 Approach vs avoidance motivation: Elliot 2006
```

---

## §7 — Feedback Loop: Bidirectional + Asymmetry

### §7.1 — Interaction map: 10 paths

```
⭐⭐ CÁC COMPONENTS KHÔNG ĐỘC LẬP — TƯƠNG TÁC 2 CHIỀU:

  ┌──────────┬──────────────────────────────────────────────────────┐
  │ Path     │ Mechanism                                            │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ D → B    │ PFC tạo positive exposure with entity                │
  │          │ → compile → Entity-Valence update (INDIRECT, SLOW)   │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ B → D    │ Entity-Valence bias PFC attention (DIRECT, FAST)     │
  │          │ VD: ghét teacher → body auto-reject → PFC phải       │
  │          │ suppress → PFC mệt → body win                       │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ D → C    │ PFC create imagination (→C2) hoặc change environment │
  │          │ (→C1). PFC direct attention → filter C1 salience.    │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ C → D    │ Body-input (dissonance signals) can wake PFC.        │
  │          │ VD: đau bụng → PFC wakes → engage problem-solving    │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ B → C    │ Entity-Valence bias exposure SOURCE selection:       │
  │          │ body auto-attend high-valence entity → more C1       │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ B → A    │ Entity-Valence amplify compile RATE from that entity.│
  │          │ Trust = multiplier. Same exposure → compile STRONGER.│
  ├──────────┼──────────────────────────────────────────────────────┤
  │ A → B    │ Compiled chunks update Entity-Valence profile.       │
  │          │ VD: mới biết thầy giỏi → [thầy → positive] tăng    │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ A → C    │ Compiled patterns change salience filters +          │
  │          │ material cho C2 (imagination) + C3 (spontaneous).    │
  ├──────────┼──────────────────────────────────────────────────────┤
  │ A → D    │ Compiled expertise cho PFC material tốt hơn.        │
  │          │ Compiled pattern → PFC freed (Hold → auto).          │
  └──────────┴──────────────────────────────────────────────────────┘

  = NOT hierarchy (top-down). = FEEDBACK SYSTEM (bidirectional loop).
  Mọi component ảnh hưởng mọi component khác.

  🟡 Feedback system model: framework synthesis
```

### §7.2 — Critical Asymmetry: D→B slow/costly, B→D fast/free

```
⭐⭐ ASYMMETRY GIẢI THÍCH NHIỀU HIỆN TƯỢNG:

  ┌──────────┬──────────────────────┬──────────────────────┐
  │          │ D → B                │ B → D                │
  │          │ (PFC → Entity-V)     │ (Entity-V → PFC)     │
  ├──────────┼──────────────────────┼──────────────────────┤
  │ Speed    │ CHẬM (weeks/months)  │ NHANH (milliseconds) │
  │ Cost     │ CAO (PFC hold liên   │ THẤP (compiled =     │
  │          │ tục + create exposure)│ cost ≈ 0)            │
  │ Path     │ INDIRECT (D→C→A→B)  │ DIRECT (B→D)         │
  │ Sustain  │ Bền NẾU compile xong│ Rất bền (compiled)   │
  └──────────┴──────────────────────┴──────────────────────┘

  ANALOGY:
    Entity-Valence (B) = "trọng trường" — luôn kéo về compiled direction.
    PFC (D) = "tên lửa" — CÓ THỂ thoát, nhưng TỐN FUEL.
    Fuel (PFC budget) = FINITE → phải đạt orbit (compile) trước khi hết fuel.
    Nếu compile xong → bay free. Nếu hết fuel trước → rơi lại.

  IMPLICATION:
    → "Biết mà không làm" = PFC tên lửa hết fuel, Entity-Valence kéo lại.
    → Therapy takes months = D→B indirect path.
    → Forced learning unsustainable = D fight B liên tục, PFC exhausted.
    → "Yêu lấy thầy" = invest D once → compile B → B runs free (§7.3).

  🟡 D→B vs B→D asymmetry: framework synthesis
  🟢 PFC slower than subcortical: LeDoux 1996
  🟢 PFC budget finite: PFC-Operations.md v1.3 §8
  🟢 CBT mechanism = gradual recompilation: Beck 1979, Foa & Kozak 1986
```

### §7.3 — Virtuous loop: "Muốn con hay chữ thì yêu lấy thầy"

```
⭐ VIETNAMESE PROVERB = ARCHITECTURE TRONG 1 CÂU TỤC NGỮ:

  Step 1: PFC framing [thầy → đang cố giúp mình]
          → D: Hold positive frame. Cost: ① PFC draft (initial investment).

  Step 2: PFC direct positive interactions
          → D → C1: tạo body-input positive với thầy
          (hỏi han, tham gia lớp, cảm ơn)

  Step 3: Body experience positive interactions
          → C1 → Engine A: exposure → Hebbian → compile [thầy → positive]
          Multi-modal: see face + hear voice + feel warmth.

  Step 4: Entity-Valence [thầy] TĂNG
          → A → B: compiled chunks update entity-valence profile.

  Step 5: Body AUTO-RECEPTIVE to thầy's knowledge
          → B → A: Entity-Valence amplify ALL exposure from thầy.
          Same lesson → compile DEEPER (trust = multiplier).

  Step 6: Knowledge compile NHANH hơn
          → A output: content chunks accumulate faster.

  Step 7: PFC FREED
          → B runs automatic (compiled, cost ≈ 0)
          → PFC budget available cho other tasks. SUSTAINABLE.

  = VIRTUOUS LOOP: invest D → compile B → B runs free → D freed.

  "Yêu" = build Entity-Valence (B)
  "Thầy" = entity target
  "Hay chữ" = content compile amplified by B
  "Muốn con" = PFC intention (D) cần initiate

  🟡 Proverb as virtuous loop illustration: framework synthesis
  🟢 Positive teacher-student relationship → learning: established
  🟢 Emotional context affects learning: Immordino-Yang & Damasio 2007
```

### §7.4 — Vicious loop: "Ghét giáo viên"

```
🟡 REVERSE — "GHÉT GIÁO VIÊN → TỰ ĐỘNG TỪ CHỐI":

  Step 1: Entity-Valence [teacher → negative] compiled
          (past: bị mắng, bị xấu hổ, unfair) → B negative.

  Step 2: Teacher speaks → B ATTENUATE exposure
          Body auto-filter: giảm attention, giảm receptivity.
          Same lesson → compile YẾU hơn (trust = near-zero multiplier).

  Step 3: PFC try override → Suppress negative entity-valence
          D: Suppress cost ② efference mismatch. PFC-Operations.md v1.3 §2.2.

  Step 4: PFC fatigue → release → B reassert
          B compiled, automatic, fast → body reject teacher's input AGAIN.

  Step 5: Less compile → fall behind → more frustration → B MORE negative
          "Ghét thầy → dở môn → ghét hơn" = VICIOUS self-reinforcing.

  Step 6: BREAK THE LOOP — CẦN inject positive exposure (C1):
          → Thay thầy (new entity, reset B to neutral)
          → Thầy cũ thay đổi approach (create new positive C1)
          → Third party mediate (context cho positive interaction)
          → NHƯNG: old B NEVER deleted, chỉ competitive re-linking (Chunk.md v2.3 §2.5)

  🟡 Vicious loop model: framework synthesis
  🟢 Ironic rebound: Wegner 1987
```

---

## §8 — 6 Trade-offs Của Compile Ngắn

```
🟡 COMPILE NGẮN = DOMINANT MODE VÀ CÓ 6 TRADE-OFFS RÕ RÀNG:


  T1 — NHANH NHƯNG DỄ BỊ LỪA (trust wrong source):

    Compile ngắn + trust = bypass verification.
    Trust amplifier CAO → body hành động theo trust mà không verify.
    → Nếu source SAI → compiled SAI → body hành động theo pattern sai.

    Ví dụ:
      Bố mẹ: "phụ nữ không cần học cao" → trust → compile SÂU
        → 30 tuổi: body compiled [học = không cần] → KHÓ thay đổi
      Cult: install chain qua trust → compile SÂU → weaponized trust

    Root cause: Trust amplifier CAO = bypass verification.
    Trust ĐÚNG → compile đúng → tiết kiệm. Trust SAI → tốn kém.

    🟢 Cult persuasion: Cialdini 2006


  T2 — PFC KHÔNG THỂ SELF-CORRECT (confabulation):

    PFC explain post-hoc → label ≠ mechanism → fix SAI CHỖ → loop kéo dài.

    Ví dụ:
      "Sao tôi cưới người này?" (marriage stress)
        PFC: "bị lừa" / THẬT: body compiled [partner → ấm] từ experience
        Context thay đổi → pattern KHÔNG MATCH → confused

    ⭐ Trade-off CHỈ LỘ khi context thay đổi hoặc chain gãy.
    Khi mọi thứ smooth → trade-off này INVISIBLE.

    🟢 Confabulation: Nisbett & Wilson 1977


  T3 — COMPILED PATTERN BỀN HƠN CONTEXT (lag):

    Compile = Hebbian LTP → KHÔNG thể xóa (Chunk.md v2.3 §2.5).
    Context thay đổi NHANH → compiled pattern thay đổi CHẬM → LAG.

    Ví dụ:
      Code HTML compiled SÂU → HTML obsolete → body VẪN fire "tôi giỏi HTML"
      Chia tay → body VẪN fire [tối → gọi điện partner] → Chunk-Miss

    Root cause: chunks KHÔNG CÓ cơ chế "unwire" chủ động.
    "Bỏ thói cũ" = chunk MỚI compile ĐỦ MẠNH → ĐÈ chunk cũ.


  T4 — "TẠI SAO TÔI LÀM VẬY?" = KHÔNG CÓ 1 ĐÁP ÁN ĐÚNG:

    Body compile compound (nhiều sources), PFC KHÔNG tag nguồn → confabulation.

    Ví dụ:
      "Tại sao muốn sinh con?"
        PFC: "bản năng" / THẬT: hormone + collective + Valence-Structural
        + identity + meaning = COMPOUND → PFC chọn 1 → THIẾU compound

    Root cause: NO SOURCE TAG (Chunk.md v2.3 §1.1) + confabulation.


  T5 — PHỤ THUỘC COLLECTIVE (collective gãy → individual gánh):

    Trust Compile = individual SHORT + collective LONG.
    → Khi collective chain GÃY → individual thiệt hại mà KHÔNG biết tại sao.

    Ví dụ:
      AI disruption: [ngành X → việc X] GÃY → "mình học làm gì?"
        Chain gãy ở collective, KHÔNG phải lỗi cá nhân.
        PFC thường blame MÌNH (vì PFC chỉ thấy Cấp 1).

    Root cause: Trust Compile = individual KHÔNG hold chain → KHÔNG biết gãy ở đâu.


  T6 — "BIẾT MÀ KHÔNG LÀM" (PFC logic ≠ compiled pattern):

    PFC chain logic "nên làm X" →
    NHƯNG body compiled [KHÔNG X → thoải mái] (Experience Compile).

    Ví dụ:
      "Biết nên tập thể dục" → body: compiled [sáng → ngủ → thoải mái]
        PFC chain = TRUST (installed). Body = EXPERIENCE (direct).
        EXPERIENCE thắng (multi-modal, direct > verbal install).

    Root cause: 2 Compile Types cạnh tranh. Experience > Trust trong hầu hết cases.
    = Asymmetry §7.2: Experience compile = B self (Mức 5 multiplier).
      Trust compile = B external (Mức 2-3 multiplier). Self > external.
    → CAN THIỆP: chuyển từ TRUST → EXPERIENCE (direct experience).
    → VD: muốn tập thể dục → ĐI TẬP → body compile [tập → ấm] → override.


  ⭐ 6 TRADE-OFFS = KHÔNG PHẢI BUG, MÀ LÀ FEATURE:

    Compile ngắn + trust = TỐI ƯU cho survival environment:
      Nhanh (ms, không ngày). Rộng (access collective). Rẻ (ít cortisol).

    Trade-offs = GIÁ CỦA TỐI ƯU HÓA:
      T1: nhanh → dễ lừa
      T2: auto → khó tự sửa
      T3: bền → lag khi context đổi
      T4: compound → PFC confused
      T5: phụ thuộc → collective gãy = gánh
      T6: Experience > Trust → "biết mà không làm"

    → Evolution MAXIMIZE survival probability, KHÔNG minimize trade-offs.

  🟡 6 trade-offs framework: drill synthesis
  🟢 Components individually established (see references above)
```

---

## §9 — Interactions: Experience vs Trust, Chain Break, External Tools

### §9.1 — Experience vs Trust: Cạnh tranh, hợp lực, override

```
🟡 EXPERIENCE × TRUST INTERACTIONS:


  ⭐ HỢP LỰC — khi Experience confirm Trust:

    Trust install [học → tốt] + Experience confirm [học → mẹ khen → ấm]
    = COMPOUND STRONG. Cả 2 configs cùng hướng → pattern cực bền.
    = "Educated + enjoy" case. Lý tưởng.


  ⭐ CẠNH TRANH — khi Experience contradict Trust:

    Trust install [rượu → xấu] + Experience compile [rượu → vui → ấm]
    = Competing chains → chain MẠNH HƠN thắng (Valence-Propagation.md v4.1 §5).
    Experience thường thắng (multi-modal, direct > verbal install).
    = "Biết rượu xấu mà vẫn uống."


  ⭐ TRUST OVERRIDE EXPERIENCE — hiếm nhưng xảy ra:

    Điều kiện: Trust install CỰC SÂU + Experience compile NÔNG.
    VD: Religious prohibition mạnh (trust deep + community reinforce + repeated)
      → Body compiled [rượu → tội] CỰC SÂU qua NHIỀU NĂM
      → Direct experience [rượu → vui] = 1 lần → NÔNG → Trust thắng.

    → Trust override Experience CẦN: trust deep + repetition + emotional reinforcement.
    → = Tại sao education + culture CAN work, nhưng cần THỜI GIAN + INTENSITY.


  ⭐ OVERLAPPING — ranh giới mờ:

    [ăn ngon → ấm] = Experience (direct) + Trust (cultural "ngon").
    → Phần lớn adult behavior = Experience × Trust overlap, KHÔNG purely 1 type.

  🟡 Experience × Trust interaction dynamics: framework synthesis
```

### §9.2 — Chain Break: Collective gãy, cá nhân detect

```
🟡 KHI COLLECTIVE CHAIN GÃY — BODY DETECT TRƯỚC PFC:

  Chain collective: [học → đại học → việc → lương → body-base feed]
  Individual compile: [học → tốt] (Trust Compile SHORT)

  PFC KHÔNG TỰ NHIÊN SUY NGHĨ "chain gãy."
  BODY circuit-break TRƯỚC → PFC wake SAU (Body-Base.md v3.3 §7).


  ① COST TĂNG:
     Baseline compiled = "học → vừa phải"
     Reality mới = "học → mệt quá" → cost >> baseline
     Body-Feedback-Mechanism.md v2.1 §3 Chunk-Miss:
     VTA negative delta → dissonance signal.

  ② LINK GÃY:
     Collective chain GÃY ở [đại học → việc TỐT]
     Trust collapse → toàn bộ chain ẢNH HƯỞNG
     "Học vô ích" = chain đứt → valence "học" FLIP negative.

  ③ COMPOUND:
     Cost TĂNG + link GÃY + trust COLLAPSE
     = Body-Feedback-Mechanism.md v2.1 §4 COMPOUND
     → PFC wake MẠNH → "học làm gì" = PFC RE-EVALUATE

  ⭐ KEY INSIGHT:
    "Học làm gì" KHÔNG phải PFC tự phát suy nghĩ triết học.
    = Collective chain GÃY → body DETECT → PFC engage.
    Individual KHÔNG biết gãy ở ĐÂU (vì KHÔNG hold chain).
    → PFC thường blame MÌNH thay vì detect collective chain break.

  🟡 Chain break detection model: framework synthesis
  🟢 Circuit breaker concept: established neuroscience (NE α1 disconnect)
```

### §9.3 — Expertise × External Tools: Cấp 2 cá nhân

```
🟡 EXPERTISE COMPILE EXTEND QUA EXTERNAL TOOLS:

  EINSTEIN MODEL:

    ① WRITE DOWN = external memory
       PFC hold 4 → viết ra → PFC freed → hold 4 tiếp
    ② TRUST PAST SELF
       "Công thức X tôi đã kiểm chứng" → trust tag → build on top
    ③ ITERATIVE RECURSIVE
       Verify A → trust A → build B → verify B → trust B → stack
    ④ SLEEP CONSOLIDATE giữa các bước

  HIERARCHY:
    PFC 4±1 (hardware limit)
    → ×4 pyramidal compression (vô thức — Valence-Propagation.md v4.1 §5b)
    → ×∞ external tools (giấy, máy tính, database, AI)

  → External tools = "Cấp 2 cá nhân" (Collective-Body.md v2.1 §3.3)
  → MỞ RỘNG individual compile BEYOND hardware limit

  🟢 Extended mind thesis: Clark & Chalmers 1998
  🟢 Epistemic actions: Kirsh & Maglio 1994
  🟡 "Cấp 2 cá nhân": framework synthesis
```

---

## §10 — Evolutionary Gradient

```
⭐ MODULATORS ĐƯỢC THÊM QUA TIẾN HÓA — ENGINE CONSERVED:


  ┌──────────────┬─────────┬───────────┬───────────┬──────────────┐
  │ Species      │ Engine A│ Sources C │ Entity-V B│ PFC D        │
  ├──────────────┼─────────┼───────────┼───────────┼──────────────┤
  │ Aplysia      │ Hebbian │ C1 only   │ ✗         │ ✗            │
  │ (sea slug)   │ basic   │ (tactile) │           │              │
  ├──────────────┼─────────┼───────────┼───────────┼──────────────┤
  │ Cá, bò sát   │ Hebbian │ C1 (multi-│ Basic     │ ✗ minimal    │
  │              │         │ sensory)  │ (friend/  │              │
  │              │         │           │ foe)      │              │
  ├──────────────┼─────────┼───────────┼───────────┼──────────────┤
  │ Chó, mèo     │ Hebbian │ C1 + C3   │ Basic     │ Limited      │
  │ (social      │         │ basic     │ (attach-  │ (inhibitory) │
  │ mammals)     │         │           │ ment)     │              │
  ├──────────────┼─────────┼───────────┼───────────┼──────────────┤
  │ Linh trưởng   │ Hebbian │ C1 + C3   │ Rich      │ Moderate     │
  │ (primates)   │         │ + C2 basic│ (social   │ (planning)   │
  │              │         │           │ complex)  │              │
  ├──────────────┼─────────┼───────────┼───────────┼──────────────┤
  │ Con người     │ Hebbian │ C1+C2+C3  │ Full      │ Full         │
  │ (humans)     │         │ FULL      │ (Entity-  │ (5 roles,    │
  │              │         │ (imagine, │ Compiled, │ Simulation-  │
  │              │         │ tools, AI)│ Mức 0-5)  │ Engine)      │
  └──────────────┴─────────┴───────────┴───────────┴──────────────┘


  PATTERN:
    Engine A (Hebbian) = CONSERVED từ Aplysia → human.
    Evolution THÊM modulators + sources, KHÔNG thay đổi engine.
    MỖI BƯỚC = THÊM MODULATOR, KHÔNG thay đổi ENGINE.

  IMPLICATIONS:
    ① Dog training = pure Engine A + minimal B (repetition × reward).
    ② Human education = Engine A + B + C2 + D (PHỨC TẠP hơn, POWERFUL hơn).
    ③ Compilable Architecture (Body-Base.md v3.3 §2):
       = Engine A + full modulator suite → CAN learn ANYTHING (general-purpose).
       NHƯNG: no pre-wired content → cần 15-20 năm calibrate.

  🟢 Aplysia Hebbian: Kandel 2000
  🟢 PFC evolution: Semendeferi et al. 2002
  🟢 Attachment system mammals: Bowlby 1969
  🟡 Modulator additive evolution model: framework synthesis
```

---

## §11 — Edge Cases Verified (8+)

```
⭐ 8 EDGE CASES — TẤT CẢ CONSISTENT VỚI ARCHITECTURE:


  ① TRAUMA (emotional peak):
     Engine A: 1 exposure × peak_valence CỰC CAO → compile immediate.
     Source: C1. Mod B: [chó] flip negative ngay. PFC: BYPASSED (~12ms).
     → Engine A compile WITHOUT modulator D.
     🟢 LeDoux 1996

  ② CULT (Entity-Valence override PFC):
     Engine A: multi-modal + emotional peak + repetition → deep compile.
     B: [leader → positive++++] = DOMINANT. D: PFC WEAKENED.
     → B maximized + D minimized + C enriched = deep install.
     🟢 Cialdini 2006

  ③ THERAPY (PFC-guided recompile):
     Engine A: new exposure (C2 imagination + C1 controlled exposure).
     D: PFC Hold new frame. B: gradually UPDATE (indirect D → B).
     → Reconsolidation window: recall → modify → re-compile.
     🟢 Foa & Kozak 1986, Nader 2000

  ④ TRẺ BỊ ÉP HỌC (multi-stream):
     Content compile ✓ (Engine A + C1 forced). Value ✗ (trust ≈ 0).
     Entity: mixed. Behavior: avoidance habit ✓.
     → Multi-stream: content VẪN compile dù trust thấp.

  ⑤ "BIẾT MÀ KHÔNG LÀM":
     Trust value installed thin. Experience compiled deep.
     Engine A products CẠNH TRANH: Experience > Trust.
     → Compile DEPTH difference + B asymmetry (self > external).
     🟢 Elliot 2006

  ⑥ IMMERSION LANGUAGE:
     Engine A: massive C1 exposure. B: minimal. D: moderate.
     → Pure Engine A + C1 = immersion learning (slow but DEEP).
     🟢 Krashen 1982

  ⑦ EXPERT BLIND SPOT:
     Expert: decades D-compiled → pyramidal compression → "thấy 4."
     Novice: chưa compiled → cần C1 + C2 + time.
     → Trust amplify VALUE, KHÔNG amplify CONTENT (§3.3).

  ⑧ "YÊU LẤY THẦY" (full feedback cycle):
     D invest → C1 positive → A compile → B update → B auto → D freed.
     = Virtuous loop (§7.3). PFC one-time cost → permanent benefit.


  8/8 CASES CONSISTENT.
  Architecture giải thích TẤT CẢ mà 3-type taxonomy giải thích,
  PLUS giải thích thêm cases mà taxonomy KHÔNG giải thích rõ:
    → "Giỏi nhưng ghét học" (multi-stream: content ✓ value ✗)
    → "Biết mà không làm" (compile depth + B asymmetry)
    → Immersion > classroom (source richness > PFC effort)

  🟡 Edge case stress-testing: framework synthesis
  🟢 Individual cases: citations as listed per case
```

---

## §12 — Honest Assessment

```
🟢 ESTABLISHED (strong research support):

  Hebbian learning / LTP: Hebb 1949, Bliss & Lømo 1973
  PFC ~4±1 working memory: Cowan 2001
  PFC response slower than subcortical: LeDoux 1996
  Cortisol cost of sustained load: Lupien 2009
  Expert patterns 50,000+: Chase & Simon 1973
  Neural efficiency (experts fire less): Haier 1992, Neubauer & Fink 2009
  Deliberate practice ~10 years: Ericsson 1993
  No chunk deletion / reconsolidation: Nader 2000
  Confabulation: Nisbett & Wilson 1977
  Social proof: Cialdini 1984
  Cultural transmission: Boyd & Richerson 1985
  Social learning: Bandura 1977
  Extended mind: Clark & Chalmers 1998
  PFC Hold/Suppress: Miller & Cohen 2001, Baddeley 2003, Aron 2007
  Suppress → rebound: Wegner 1987
  Sleep multi-mechanism: Diekelmann & Born 2010
  Aplysia Hebbian conserved: Kandel 2000
  Motor imagery → body response: Jeannerod 2001
  Emotional context → learning: Immordino-Yang & Damasio 2007


🟡 FRAMEWORK SYNTHESIS (logic consistent, dựa trên established):

  "1 Engine + 3 Modulators" unification:
    Components individually established. Architecture = synthesis.
    TESTABLE: predict content compile without trust → measurable.

  Trust = AMPLIFIER (not GATE):
    Resolves internal contradiction (gate vs gradient Mức 0-5).
    TESTABLE: measure compile rate at different trust levels.

  Multi-stream compile (4 streams):
    Novel concept. Components individually recognized.
    TESTABLE: "giỏi nhưng ghét học" = content ✓ value ✗.

  3 Compile Types = dominant modulator:
    Novel reframe. Preserves existing taxonomy. Adds architecture.

  D→B slow/costly vs B→D fast/free asymmetry:
    Consistent with established PFC/subcortical speed differences.

  Evolutionary gradient (engine conserved, modulators added):
    Consistent with comparative neuroscience.

  PFC accuracy per pathway (§6):
    Speculative estimates. Needs testing.


🔴 NEEDS MORE RESEARCH:

  Precise % breakdown across 3 Compile Types
  Quantitative trust amplifier weights (Mức 0-5 = what multiplier?)
  Multi-stream resource competition (independent or shared?)
  Cross-cultural variation in 4 compile pathways
  Whether Trust → Experience conversion rate measurable
  Neural signature differences between 3 Compile Types
  Compile_rate formula mathematical form (multiplicative? additive?)
```

---

## §13 — Cross-References

### §13.1 — Framework files referenced

```
COMPILE ARCHITECTURE:
  Compile-Sleep.md v1.0 — Component S chi tiết (6 mechanisms)
  Chunk.md v2.3 §2 — 4 compile mechanisms, compile_rate formula, trust, no source tag
  PFC-Operations.md v1.3 — Hold/Suppress, 4 combinations, PFC budget
  Entity-Valence-Dynamics.md v1.1 — Structural/Current valence, trust meta-dimension
  Entity-Access.md v1.2 §2 — gradient Mức 0-5 (supports amplifier model)
  Simulation-Engine.md v1.1 — PFC imagination substrate (Source C2)
  Background-Pattern.md v2.0 — accumulated gist (Source C3)

BODY-BASE + BODY-FEEDBACK:
  Body-Base.md v3.3 §2 — Compilable Architecture, §4 summary, §7 circuit breaker
  Body-Feedback-Mechanism.md v2.1 — 2 sources, Chunk-Miss, Compound dynamics
  Cortisol-Baseline.md v2.2 — sustained cortisol → neural wear
  Why-Body-Knows.md v1.2 — 2-tầng calibration
  Body-Coupling.md v3.0 — entity coupling mechanism

VALENCE + REWARD:
  Valence-Propagation.md v4.1 §2 — trust = valence meta-dimension
  Reward-Signal-Architecture.md v2.1 §8.4 — 4-Pathway × Precondition-5

COLLECTIVE + OBSERVATION:
  Collective-Body.md v2.1 §2 — 4 compile pathways × 3 cấp, §3.3 external tools
  Meaning.md v2.0 — Anchor disrupted = T5 chain break × identity
  Religion.md v2.6 §2.1 — External inject bypass PFC = Trust mechanism
  Status.md v2.0 — Resource Access Map = Experience (evolutionary direct)

PFC DETAIL:
  PFC-Hold-Dimensions.md — 6 lực hội tụ tại 4±1
  PFC-Hardware.md — Individual variance (COMT, DRD4, NE)
  PFC-Function.md v1.2 — 24 PFC functions
  Inter-Body-Mechanism.md v2.1 — Compilable Architecture, 3-Layer Evolution
```

### §13.2 — Research citations

```
ESTABLISHED (🟢):

  CORE NEUROSCIENCE:
  Hebb 1949 — Hebbian learning
  Bliss & Lømo 1973 — LTP discovery
  Dudek & Bear 1992 — LTD
  Kandel 2000 — Aplysia universal Hebbian
  Nader 2000 — Reconsolidation
  McGaugh 2004 — Emotional arousal enhances consolidation

  PFC + WORKING MEMORY:
  Cowan 2001 — Working memory ~4±1
  LeDoux 1996 — Amygdala fast pathway
  Miller & Cohen 2001 — PFC top-down attentional control
  Baddeley 2003 — Working memory model
  Curtis & D'Esposito 2003 — PFC sustained firing
  Anderson & Green 2001 — Think/No-Think paradigm
  Aron 2007 — rIFG inhibitory control
  Arnsten 2009 — PFC impaired under stress
  Lupien et al. 2009 — Cortisol + cognitive load

  LEARNING + MEMORY:
  Brown & Kulik 1977 — Flashbulb memories
  Skinner 1953 — Reinforcement
  Rescorla & Wagner 1972 — Conditioning model
  Stein & Meredith 1993 — Multi-modal integration
  Walker 2017 — Sleep consolidation
  Kolb 1984 — Experiential learning
  Jeannerod 2001 — Motor imagery
  Driskell et al. 1994 — Mental rehearsal meta-analysis

  EXPERTISE:
  Chase & Simon 1973 — Expert chess patterns 50,000+
  Haier 1992 — Neural efficiency
  Neubauer & Fink 2009 — Neural efficiency review
  Ericsson et al. 1993 — Deliberate practice

  SOCIAL + CULTURAL:
  Bandura 1977 — Social learning theory
  Boyd & Richerson 1985 — Cultural transmission
  Cialdini 1984, 2006 — Social proof, persuasion
  Hatfield et al. 1994 — Emotional contagion
  Nisbett & Wilson 1977 — Confabulation
  Johnson et al. 1993 — Source monitoring / reality monitoring
  Tajfel 1979 — In-group favoritism
  Nickerson 1998 — Confirmation bias
  Immordino-Yang & Damasio 2007 — Emotion and learning

  COGNITION:
  Wegner 1987 — Ironic process theory
  Smallwood & Schooler 2006 — Mind wandering
  Raichle et al. 2001 — DMN
  Krashen 1982 — Input hypothesis
  Clark & Chalmers 1998 — Extended mind
  Kirsh & Maglio 1994 — Epistemic actions
  Elliot 2006 — Approach vs avoidance

  THERAPY:
  Beck 1979 — CBT
  Foa & Kozak 1986 — Exposure therapy

  EVOLUTION:
  Pavlov 1927 — Classical conditioning
  Bowlby 1969 — Attachment theory
  Semendeferi et al. 2002 — PFC evolution

  SLEEP:
  Diekelmann & Born 2010 — Sleep and memory review
  (Full sleep citations → Compile-Sleep.md v1.0 §9.2)


FRAMEWORK SYNTHESIS (🟡):
  "1 Engine + 3 Modulators" unification — 2026-06-01
  Trust = amplifier (not gate) — 2026-06-01
  Trust scope VALUE vs CONTENT — 2026-06-01
  3-source parallel model (C1/C2/C3) — 2026-06-01
  Multi-stream compile (4 streams) — 2026-06-01
  Feedback asymmetry (B→D direct, D→B indirect) — 2026-06-01
  3 Compile Types = modulator configurations — 2026-06-01
  Evolutionary modulator gradient — 2026-06-01
  Component S in compile architecture — 2026-06-01
  Gate = limit case of amplifier — 2026-06-01
  4 compile pathways model — Drill-Compile-Short-Collective.md
  6 trade-offs framework — Drill-Compile-Short-Collective.md
```

---

> **PARENT**: Chunk.md v2.3 §2 (4 compile mechanisms = foundation)
> **COMPANION**: Compile-Sleep.md v1.0 (Component S chi tiết)
> **BACKUP**: backup/Compile-Taxonomy-v2.0.md (v2.0 preserved)
