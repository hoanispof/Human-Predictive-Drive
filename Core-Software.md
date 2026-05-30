# Core-Software — Cycle-Based Architecture (Software Map)

> **Trạng thái:** v2.2 — 1 trong 2 bản đồ Core v7.8
> **Ngày:** 2026-05-25 (v2.2 — Core-Interface.md → backup, 3→2 bản đồ, Ask-AI.md = dynamic interface)
> **v2.1:** 2026-05-25 (§4.2 +Evaluative/Direct-State Dissonance parallel, §11 +Reframe #21, Dissonance-Signal-Architecture v1.0)
> **v2.0:** 2026-05-24 (FULL REWRITE — tích hợp 14 concept mới từ 28-session drill)
> **v1.0:** backup/Core-Software-v1.0-backup.md (2026-05-10)
> **Bản đồ này:** SOFTWARE MAP — CHẠY THẾ NÀO (mechanism chi tiết nhất)
> **Bản đồ khác:** Core-Hardware.md (CÁI GÌ ở ĐÂU)
> **Tương tác:** Ask-AI.md (AI generate dynamic interface per user)
> **Nguyên tắc:**
> - Cycle-based: Domain → Body-Input → Unconscious → Feeling → PFC → Body-Output → Domain
> - Chunk-System = sole substrate (mọi thứ chạy trên chunks)
> - Body-Feedback: Reward (Evaluative + Direct-State) hoặc Dissonance
> - PFC = observer + indirect orchestrator (Simulation-Engine + Hold/Suppress)
> - Schema, Drives, Valence = observation parameters, không phải components
> - Development = chunk density tăng dần (cùng architecture, khác chunks)
> **Tiền đề đọc:**
> - Chunk.md v2.3 — chunk substrate, trust gate, pattern hierarchy, Entity-Compiled ref
> - Body-Feedback.md — dual-pull, Body-Feedback-Precondition, 3 nguồn, interface loop
> - Body-Feedback-Mechanism.md v2.0 — 4th axis: chunk dynamics, Body-Need 2-source
> - Gap-Body-Need.md v1.0 — 3 Satiation Types, ENGINE/ROAD/VEHICLE, entity-gap matching
> - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles
> - Feeling.md v3.0 — PFC observation interface, 7-layer, PFC=Lawyer integrated
> - Agent-Mechanism.md v2.1 — agent = function on chunks, 11 sub-files, Compilable Architecture
> - Self-Pattern-Modeling.md v3.1 — 1 mechanism × 3 dimensions, Compiled/Fresh
> - Entity-Compiled.md v1.0 — hub-and-spoke, formation 40→200h, Dunbar, grief
> - Entity-Access.md v1.2 — gradient model Mức 0-5, 3-Factor, per-entity dynamics
> - Bond-Architecture.md v2.0 — 1 mechanism × 4 bond types, gap clone impossible, Resonance Decline
> - Simulation-Engine.md v1.0 — 1 engine, 3 components, 3 axes, N applications
> - PFC-Operations.md v1.0 — Hold/Suppress, Budget, Compiled Quality
> - Empathy.md v4.0 — Self-Pattern-Modeling applied, PFC budget, per-entity, 4-Layer
> - Valence-Propagation.md v3.0 — structural/current, 3 Firing Modes, Hardware-Subsidy
> - Cortisol-Baseline.md v2.1 — amplifier, direction gate, 7 modes, HPA paradox
> - Body-Base.md v3.2 — entry point, Model 3+1, Compilable Architecture
> - Compile-Taxonomy.md v2.0 — 3 Compile Types, 4 pathways, 6 trade-offs
> - Collective-Body.md v2.1 — Model 3 cấp, trust = only bridge, By-product L3
> - Connection.md v5.0 — 3 Generative Primitives, Entity-Access, Hardware-Subsidy, 4-Layer
> - Domain.md v2.0 — 3 Domain Types, Dual Check, 3 Nguồn Constraint
> - PFC-Configuration.md v1.1 — 6 dynamic modes, survival matrix
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Numbers (🟡):** `~X%` = calibration anchor — hướng + cỡ, KHÔNG phải đo lường.
>   `X-Y%` = range minh họa (biến thiên lớn). Insight nằm ở HƯỚNG + TƯƠNG QUAN,
>   không ở con số cụ thể. Mỗi người, mỗi context → số thực tế khác.
>   🟢 numbers (có citation) = research-backed. Chi tiết: §12.4.
> **Language:** Tiếng Việt primary + English technical terms

---

## Mục lục

- §0 — BA BẢN ĐỒ + TẠI SAO CYCLE-BASED
- §1 — KIẾN TRÚC CYCLE: SOFTWARE MAP
- §2 — DOMAIN
- §3 — BODY-INPUT (L0 + L1)
- §4 — UNCONSCIOUS PROCESSING
- §5 — FEELING (Bridge)
- §6 — PFC (Observer + Orchestrator)
- §7 — BODY-OUTPUT
- §8 — OBSERVATION PARAMETERS
- §9 — DEVELOPMENT TRAJECTORY
- §10 — MULTIPLE TIMESCALES
- §11 — KEY REFRAMES
- §12 — HONEST ASSESSMENT
- §13 — CROSS-REFERENCES

---

## §0 — BA BẢN ĐỒ + TẠI SAO CYCLE-BASED

### §0.1 Ba bản đồ Core v7.8

Framework mô tả body-brain system từ 2 góc nhìn, mỗi góc = 1 bản đồ:

| # | Bản đồ | Góc nhìn | Đối tượng | File |
|---|---|---|---|---|
| 1 | Hardware Map | CÁI GÌ ở ĐÂU | Neuroscience researcher | Core-Hardware.md |
| 2 | **Software Map** | **CHẠY THẾ NÀO** | **Framework researcher** | **File này** |

2 bản đồ mô tả CÙNG hệ thống. Khác góc nhìn. Đọc độc lập được.
Giống máy tính: sơ đồ mạch (Hardware) / code architecture (Software).
Tương tác với framework: Ask-AI.md — AI đọc framework, adapt theo mức hiểu của từng người.

### §0.2 Tại sao v7.8 cycle-based

Core-v7.5-Draft.md (2026-03) tổ chức: 4 layers + 3 drives + Schema System.
Scaffolding đó cho phép drill 35,000+ dòng phân tích (130+ files, 500+ citations).

Sau khi drill: tất cả mechanism files compatible — layers/drives/schemas = observation labels,
không phải architecture. Cycle-based match cách body-brain thực sự hoạt động.

| V7.5 | V7.8 | Lý do |
|---|---|---|
| 4 layers (L0-L3) | L0 circuit breaker + L1 inputs | L2 removed, L3 collapsed |
| 3 drives | Observation parameters | Drives = emergent, không phải operators |
| Schema System | Chunk-System (sole substrate) | Schema = observation label |
| Layer priority | Signal strength | Loudest wins, not highest layer |
| Cross-cutting | Properties of cycle | Cortisol = amplifier, Empathy = function |
| Feeling (implicit) | Explicit bridge | PFC observation interface |
| N modules riêng | 1 Simulation-Engine | Shared substrate cho Self-Pattern-Modeling, Imagine-Final, ... |
| Type A/Type B | Compiled/Fresh | Processing spectrum thật, không phải content types |

### §0.3 Nguyên tắc thiết kế

1. **Follow mechanism, not organization**: kiến trúc match cách body-brain thực sự hoạt động
2. **Chunk-centric**: chunks = sole substrate, mọi thứ khác = function hoặc property
3. **Cycle, not layers**: perception-action loop liên tục
4. **Observation parameters, not components**: Schema, Drives, Valence = cách quan sát
5. **Development = chunk density**: cùng architecture, khác chunks tích lũy
6. **1 Engine, N Applications**: Self-Pattern-Modeling, Imagine-Final, Self-Observation = applications trên cùng Simulation-Engine
7. **Honest about limits**: descriptive architecture + hypothesis generator, không phải clinical protocol

---

## §1 — KIẾN TRÚC CYCLE: SOFTWARE MAP

### §1.1 Ba góc nhìn — cùng hệ thống

```
🟡 CÙNG HỆ THỐNG — BA GÓC NHÌN:

  Giống quan sát một con robot:

  HARDWARE MAP (Core-Hardware.md):
    → Mở robot ra → thấy CPU, sensors, motors, dây dẫn, pin
    → "CÁI GÌ ở ĐÂU, nối với gì, specs cá nhân"
    → Cho chuyên gia thần kinh, muốn verify từng vùng não

  SOFTWARE MAP (file này):
    → Nhìn robot hoạt động → input → process → decide → act → feedback
    → "CÁI GÌ CHẠY thế nào, flow ra sao, mechanism chi tiết"
    → Cho researcher muốn hiểu WHY hệ thống hoạt động

  TƯƠNG TÁC (Ask-AI.md):
    → Hỏi AI → AI đọc framework → adapt theo mức hiểu → trả lời phù hợp
    → Dynamic interface — không cần đọc trực tiếp mechanism files
    → Cho mọi người, AI làm cầu nối giữa framework và người hỏi

  Cả hai bản đồ mô tả CÙNG body-brain system.
  Hardware: 4 zones A/B/C/D. Software: 7-step cycle ①→⑦.
  Mapping Hardware ↔ Software → §1.3.
```

### §1.2 Software Map — Functional Cycle

```
🟡 BẢN ĐỒ CHỨC NĂNG — "CÁI GÌ CHẠY THẾ NÀO, FLOW RA SAO":

  PFC ở trên cùng — điểm quan sát của mỗi người.
  Domain ở dưới cùng — nguồn stimuli.
  Perception ↑ đi lên. Action ↓ đi xuống.

  ┌────────────────────────────────────────────────────────────────────┐
  │                PFC (observer + orchestrator)                        │
  │                                                                    │
  │  OBSERVE: feeling + body vote + chunk activations                  │
  │  HOLD: ~4±1 WM slots (beginner: small, expert: meta-chunks)       │
  │  SUPPRESS: block unwanted pattern (costly, unsustainable)          │
  │  BUDGET: finite shared resource (mệt ở work → kém ở nhà)          │
  │  IMAGINE: Simulation-Engine-APPLICATION-2 (future simulation)       │
  │  DOMAIN-CHECK: "smooth" hay "sai so với reality"?                  │
  │                                                                    │
  │  SIMULATION-ENGINE (1 engine, N applications):                     │
  │    DMN + mPFC + insula + hippocampus = shared substrate            │
  │    Self-Pattern-Modeling = APPLICATION-1 (Other, Present, Simulate) │
  │    Imagine-Final = APPLICATION-2 (Self, Future, Simulate+Construct) │
  │    Self-Observation = APPLICATION-3 (Self, Present, Observe)        │
  │    Hỏng 1 component → ALL apps degrade (alexithymia proof)        │
  │                                                                    │
  │  ⚠️ KHÔNG THỂ: feel trực tiếp | compile | override signal mạnh   │
  │  PFC effectiveness = f(chunks đã compiled cho tình huống đó)       │
  │                                                                    │
  └──────┬──────────────────────────────────────┬──────────────────────┘
    ④↑ feeling                             ⑤↓ orchestrate
    arrives                                (hold chunks →
                                            bias direction)
  ┌──────┴──────────────────────────────────────┴──────────────────────┐
  │                        FEELING (bridge)                             │
  │                                                                     │
  │  Body signals integrate → trở thành PFC-observable                  │
  │  7-layer fidelity: raw 100% → ... → explanation 20-70%             │
  │  Compiled feeling (body biết) vs Fresh feeling (PFC mới thấy)       │
  │  Wise: trust Feel-Consciousification-Feel-Observation (pre-label) | Naive: trust Feel-Labeling-Feel-Explanation (lossy nhất)    │
  │                                                                     │
  └──────┬──────────────────────────────────────────────────────────────┘
    ③↑ magnitude × clarity → PFC-observable
  ┌──────┴──────────────────────────────────────────────────────────────┐
  │                   UNCONSCIOUS PROCESSING                             │
  │                                                                      │
  │  CHUNK-SYSTEM (sole substrate):                                      │
  │    Compile: repetition + emotional peak + multi-modal + sleep        │
  │    Compiled Quality: genuine / schema / threat (compile-time lock)   │
  │    Entity-Compiled: agent compile vào body-base (40→200h)            │
  │    Activate: probability-weighted spreading activation               │
  │    Link: Type 1-3 auto + Type 4 PFC deliberate                      │
  │    Never delete — only probability shift                             │
  │    Proto-chunk → Compiled → Meta-chunk (gradient)                    │
  │                                                                      │
  │  BODY-FEEDBACK (continuous evaluation):                              │
  │    REWARD: Evaluative (opioid, Body-Feedback-Precondition) + Direct-State (non-opioid) │
  │    DISSONANCE: input < baseline, mismatch, recalibration             │
  │    Dual-Pull: hardware pull (smooth) × domain pull (adapt)          │
  │    3 Satiation Types: Cyclic / Tonic / Generative                   │
  │    Hardware-Subsidy: body subsidize entity processing per Mức        │
  │                                                                      │
  │  CORTISOL (amplifier xuyên suốt):                                   │
  │    Modulates: sensitivity + energy + direction                       │
  │    Direction gate: novelty cortisol → approach | threat → avoidance │
  │    7 modes: IDLE → LAZY → ACTIVE → FOCUSED → PUSH → FREEZE → CRASH │
  │                                                                      │
  │  AGENT-MECHANISM (functions trên chunks):                            │
  │    Self-Pattern-Modeling v3.1: self → template → hiểu người khác    │
  │    Entity-Access Mức 0-5: Tool → Utility → Anchor → Deep → Excess  │
  │    Entity-Compiled: agent compile vào body structural level          │
  │    Bond-Architecture: 1 mechanism × 4 bond types                     │
  │    Valence: body assessment per entity, structural + current         │
  │    Resonance Decline: Compiled-Suppress → Reward-Habituated → ...   │
  │                                                                      │
  └──────┬──────────────────────────────────────────┬────────────────────┘
    ②↑ raw signals                              ⑥↓ compiled → execute
  ┌──────┴──────────────────────┐  ┌────────────────┴────────────────┐
  │         BODY-INPUT           │  │        BODY-OUTPUT              │
  │                              │  │                                 │
  │  L0: Alive threshold         │  │  Motor: compiled chunks         │
  │    (circuit breaker, binary) │  │    → movement                   │
  │  L1: 17 categories           │  │  Speech: language chunks        │
  │    (receptors → raw signals) │  │    → verbal output              │
  │    Mỗi input: evolved BL     │  │  Expression: facial, postural, │
  │    + individual baseline     │  │    vocal (often unconscious)    │
  │    + delta rule evaluation   │  │  PFC hold intention →           │
  │                              │  │  vô thức execute details        │
  └──────┬───────────────────────┘  └────────────────┬───────────────┘
    ①↑ stimuli                                      ⑦↓ effects
  ┌──────┴───────────────────────────────────────────────┴───────────────┐
  │                            DOMAIN                                     │
  │  3 TYPES: Reality (vật lý) | Abstract (toán) | Abstract-Dynamic (xã hội) │
  │  Tồn tại khách quan — domain KHÔNG nói dối                           │
  │  Dual Check: body = quality controller, domain = final arbiter       │
  │  Cục bộ thay đổi khi: tương tác + di chuyển + đổi góc nhìn          │
  └──────────────────────────────────────────────────────────────────────┘

  🔄 LOOP: ①→②→③→④ (perception ↑) + ⑤→⑥→⑦ (action ↓) → ① LIÊN TỤC
  Kể cả khi ngủ (REM processing, consolidation)
  Multiple timescales chạy ĐỒNG THỜI: ms → seconds → days → decades
  Development = cùng architecture, chunk density TĂNG DẦN
```

### §1.3 Mapping giữa Hardware và Software

```
🟡 MAPPING GIỮA HARDWARE VÀ SOFTWARE:

  ┌──────────────────────┬──────────────────────────────────────────────┐
  │ Software (chạy gì)    │ Hardware (ở đâu)                              │
  ├──────────────────────┼──────────────────────────────────────────────┤
  │ Body-Input (L0+L1)   │ Receptors → D (reflex) + C (thalamus) + B    │
  │ Chunk compile        │ B (PFC trainable) + C (indirect) + D (≈0)    │
  │ Body-Feedback fire   │ C (amygdala, VTA, brainstem) + B (insula)    │
  │ Feeling integrate    │ B (anterior insula → ACC → vmPFC)            │
  │ PFC observe + hold   │ A (dlPFC working memory)                     │
  │ PFC orchestrate      │ A → B (top-down) + A → C (vmPFC-amygdala)   │
  │ Simulation-Engine    │ A (mPFC) + B (DMN, insula) + C (hippocampus)│
  │ Entity-Compiled      │ A (ATL hub) + B (multi-modal spokes) + C     │
  │ Cortisol amplifier   │ C (HPA axis) → effects xuyên A+B+C+D        │
  │ Motor execute        │ A hold → B (motor cortex) → D (spinal)      │
  │ Delta rule (VTA)     │ C (VTA fire) → signal tới B + A              │
  │ Self-signal interoc. │ B (anterior insula) đọc D qua C (vagus)     │
  └──────────────────────┴──────────────────────────────────────────────┘

  ⭐ KEY INSIGHT:
    Hardware map = 4 vùng CỤ THỂ (A/B/C/D) — verify được bằng fMRI, lesion
    Software map = 7 bước CHỨC NĂNG (①→⑦) — describe cách system HOẠT ĐỘNG
    Interface map = observable patterns — mô tả cái OBSERVER THẤY
    Cùng hệ thống. Ba góc nhìn. Chi tiết Hardware → Core-Hardware.md.
```

### §1.4 Tại sao cycle, không layers

```
V7.5 LAYERS — vấn đề gì:

  L0 > L1 > L2 > L3 implies:
  ① Fixed priority ordering (L0 luôn thắng L1)
  ② Drives = separate operators đứng trên substrate
  ③ Connection, meaning = phải "nhét vào" layer nào đó
  ④ Development = unclear (layer nào develop trước?)

  Nhưng:
  ① Priority = signal strength, không phải layer rank
     → Đau mạnh thắng đói nhẹ, nhưng đói cực nặng thắng đau nhẹ
     → = Signal strength decides, not layer position
  ② Drives = emergent patterns trong cycle, không phải operators
  ③ Connection = L1 multi-input aggregate + Entity-Compiled → solved
  ④ Development = chunk density → clear

V7.8 CYCLE — giải quyết:

  ① No fixed priority — signal strength decides (loudest wins)
  ② No separate operators — drives = observation labels
  ③ No placement problem — everything = function or property of cycle
  ④ Development = same cycle, more chunks → naturally explained

SO SÁNH VỚI 6-STEP LOOP (Body-Feedback.md §3):

  Body-Feedback.md §3 mô tả: Domain → Body sensory → Feedback → Schema Update → Action → Domain
  V7.8 REFINES: adds Feeling bridge + PFC observation + Orchestrate detail.
  = V7.8 = 6-step + explicit Feeling + PFC + Orchestrate.
  COMPLEMENTARY, not competing.
```

---

## §2 — DOMAIN

```
🟢 DOMAIN = MÔI TRƯỜNG THỰC MÀ CON NGƯỜI TỒN TẠI:

  3 DOMAIN TYPES (Domain.md v2.0 §2):

    ┌─────────────────────┬────────────────────────┬──────────────────────┐
    │ Type                │ Ví dụ                   │ Constraint           │
    ├─────────────────────┼────────────────────────┼──────────────────────┤
    │ REALITY             │ Vật lý, sinh học,       │ Laws cố định.        │
    │ (vật lý)            │ hóa học, địa lý         │ Gravity = gravity.   │
    ├─────────────────────┼────────────────────────┼──────────────────────┤
    │ ABSTRACT             │ Toán, logic hình thức  │ Axiom-derived.       │
    │ (khái niệm tĩnh)   │                         │ 2+2 = 4 vĩnh viễn.  │
    ├─────────────────────┼────────────────────────┼──────────────────────┤
    │ ABSTRACT-DYNAMIC     │ Xã hội, kinh tế,      │ Collective maintain. │
    │ (khái niệm động)    │ luật, văn hóa, tiền   │ Tiền = domain chỉ   │
    │                     │                         │ khi collective tin.  │
    └─────────────────────┴────────────────────────┴──────────────────────┘

    → Reality: "laws" cố định, human chỉ MAP, không thay đổi được
    → Abstract: axiom-derived, consistent mãi mãi
    → Abstract-Dynamic: HUMAN TẠO + MAINTAIN → CÓ shelf-life
      → Tiền mất giá trị khi collective ngừng tin
      → Luật thay đổi khi collective thay đổi
      → "Bảo kê" mất khi hệ thống mất

  8 ĐẶC ĐIỂM CHẮC CHẮN (Domain.md v2.0 §3):
    ① Tồn tại KHÁCH QUAN — không phụ thuộc body observation
    ② Lớn hơn MỌI mô tả — mọi map = lossy summary
    ③ Feedback THẬT — domain KHÔNG nói dối (sai nằm ở interface)
    ④ Cục bộ thay đổi qua: tương tác + di chuyển + đổi góc nhìn
    ⑤ Chuyên gia vs người thường thấy KHÁC nhau ở cùng domain
    ⑥ Body tiếp xúc qua FRAGMENTS (receptors sample, không toàn bộ)
    ⑦ 3 types → 3 verification methods khác nhau
    ⑧ Domain TRƯỚC + SAU con người (Reality, Abstract vĩnh viễn)

  3 NGUỒN CONSTRAINT × SHELF-LIFE (Domain.md v2.0 §4):

    ┌─────────────────┬─────────────────────────┬──────────────────────┐
    │ Constraint       │ Hoạt động thế nào        │ Shelf-life           │
    ├─────────────────┼─────────────────────────┼──────────────────────┤
    │ PHYSICS          │ Laws vật lý, hóa, sinh  │ Vĩnh viễn            │
    │ HARDWARE         │ Evolved body specs      │ ~100K years          │
    │ COLLECTIVE       │ Institutions, norms     │ Decades-centuries    │
    └─────────────────┴─────────────────────────┴──────────────────────┘
    → Dependency ratio = f(3 nguồn) → predict stability + shift speed

  ⭐ DUAL CHECK (Domain.md v2.0 §5, Ask-AI.md v3.1):

    Body = QUALITY CONTROLLER: "có gì đó sai" / "smooth"
    Domain = FINAL ARBITER: Reality trả lời đúng/sai bất kể body nghĩ gì

    4 trường hợp (domain LUÔN ĐÚNG — "sai" = schema/body LỆCH domain):
    ① Body smooth + Domain confirms   → TỐT (schema khớp reality)
    ② Body flags  + Domain confirms   → BODY BIASED (false alarm, trauma, anxiety)
    ③ Body smooth + Domain contradicts → NGUY HIỂM NHẤT (schema sai mà body miss)
    ④ Body flags  + Domain contradicts → RÕ RÀNG (cả body + domain đều nói "sai")

    → Case ③ nguy hiểm nhất: body comfortable → KHÔNG có warning signal
      VD: pyramid scheme (tiền vào đều → body OK, reality = không bền)
    → "Domain contradicts" xảy ra khi:
      a) Schema person LỖI THỜI — domain Reality/Abstract không đổi, nhưng model sai
      b) Abstract-Dynamic domain THAY ĐỔI — collective shift, model cũ outdated
      c) Hardware error — receptor/processing hỏng → body nhận SAI từ domain
      → Cả 3 trường hợp: domain VẪN ĐÚNG. Lỗi ở schema hoặc interface.

  ANCESTRAL vs MODERN vs AI ERA:
    → Ancestral (2M+ years): natural fractals, tribal 30-150, daily walking,
      whole foods, natural light → body baselines CALIBRATED cho domain này
    → Modern: screens, processed food, sedentary → mismatch → "silent deficiencies"
    → AI era: unlimited information, AI assistance → new mismatch patterns emerging
    → Body-input deprivation accelerating across eras

  Reference: Domain.md v2.0 (full 712L, 3 Types, 8 đặc điểm, Dual Check)
```

---

## §3 — BODY-INPUT (L0 + L1)

### §3.1 L0 — Alive Threshold (Circuit Breaker)

```
🟢 L0 = BINARY CEASE-FUNCTION THREATS:

  Oxygen deprivation (minutes), extreme temperature (hours),
  critical dehydration (days), starvation (weeks),
  critical injury / blood loss (immediate),
  suffocation, drowning, electrocution (seconds)

  ĐẶC TÍNH:
    → BINARY: crossed = death, not crossed = function maintained
    → FIRES BEFORE unconscious processing (reflex, 50ms)
    → SUPPRESSES all other processing khi active
    → UNIVERSAL: mọi người, mọi văn hóa, mọi thời đại
    → Signal: LOUD, non-suppressible, non-habituable
    → Negativity bias + loss aversion AMPLIFIED ở L0

  KHÁC L1:
    → L1 deviations = uncomfortable but FUNCTIONAL
    → L0 crossed = function CEASES
    → L0 = circuit breaker TRƯỚC cycle
    → L1 = input cho cycle processing

  Reference: Body-Input-Enumeration.md §1.2.1
```

### §3.2 L1 — 17 Body-Input Categories

```
🟢🟡 L1 = BODY-INPUTS VỚI ADAPTIVE BASELINE:

  17 sub-categories trong 3 taxonomy chuẩn neuroscience:

  EXTEROCEPTION — sensing external world (5):
    ① Vision: fractal D ≈ 1.3-1.5 (Taylor 2006), bio motion, faces
    ② Audition: pink noise 1/f (Voss & Clarke 1975), voices
    ③ Olfaction: ~400 receptor types (Buck & Axel 1991), direct limbic
    ④ Gustation: 5+1 basic tastes, distinct from flavor
    ⑤ Tactile skin: mechanoreception + CT affective touch (Löken 2009)

  PROPRIOCEPTION — sensing body position (3):
    ⑥ Proprioception: muscle spindles + joint receptors (Sherrington 1906)
    ⑦ Vestibular: inner ear → head orientation, gravity
    ⑧ Kinesthetic: muscle dynamics, exertion, fatigue

  INTEROCEPTION — sensing internal state (9):
    ⑨ Thermoreception core: hypothalamic, ~37°C set point
    ⑩ Nociception: A-delta fast + C-fiber slow pain
    ⑪ Respiratory: breath rate, CO2 chemoreception, vagus
    ⑫ Cardiovascular: HR, HRV, blood pressure, vagal tone
    ⑬ Visceral: enteric NS (~100-500M neurons), gut-brain axis
    ⑭ Metabolic: blood glucose, hydration, ghrelin/leptin
    ⑮ Hormonal-sensed: cortisol, testosterone, oxytocin (downstream)
    ⑯ Sleep/Circadian: REM/NREM, SCN master clock, melatonin
    ⑰ Self-signal interoception META (KEYSTONE) ⭐

  ⭐ §3.2.1 Self-signal interoception = ARCHITECTURAL KEYSTONE:
    → Body's capacity to READ own internal state
    → Insula (Craig 2002, 2009) + ACC + predictive interoception (Seth 2013)
    → WITHOUT §3.2.1 functional: other inputs fire but body "cannot hear"
    → → Silent deficits accumulate without PFC awareness
    → Explains alexithymia (~10% population, Bird & Cook 2013)
    → Developmental: caregiver mirroring → child learns self-reading
    → Therapeutic targets: mindfulness, Gendlin focusing, somatic therapy
    → Reference: Body-Input-Enumeration.md §4.9

  MỖI INPUT CÓ:
    → Receptor system + neural pathway (hardware)
    → Evolved baseline range (ancestral calibration — Tier 1)
    → Individual baseline within evolved range (development — Tier 2)
    → Delta rule: deviation → reward (above) or dissonance (below)
    → Adaptation dynamics (§3.3 below)
    → Individual variation patterns

  Reference: Body-Input-Enumeration.md §2-§4 cho 8-field schema mỗi input
```

### §3.3 Baseline Adaptation Mechanism

```
🟡🟢 DELTA RULE — CORE MECHANISM (Helson 1964):

  BL(t+1) = BL(t) + α × (input_quality(t) - BL(t))

  → input > baseline → positive prediction-delta → REWARD → seek repeat
  → Repeated exposure → baseline shifts UP → same input = no reward
  → Seeking escalation → HEDONIC TREADMILL established

  EMPIRICAL VALIDATION: Hall 2019 NIH Cell Metabolism
    → Same participants, same calories offered
    → Ultra-processed diet → +500 kcal/day overconsumption
    → = Direct experimental measurement của baseline distortion

  ASYMMETRIC DECAY:
    → Baseline shifts UP fast (exploit new opportunities)
    → Baseline shifts DOWN slow (slow relinquishment)
    → Evolutionary logic: quick exploit + slow release = survival optimal
    → Modern consequence: engineered supernormal stimuli hijack "up" rapidly,
      recovery to ancestral baseline takes much longer

  UNIVERSAL ACROSS ALL 17 BODY-INPUT CATEGORIES:
    → Food (Hall 2019), sex, visual (screen), auditory (music),
      social validation, substances, mastery
    → One mechanism explains all — direction matters, not mechanism

  Reference: Body-Input-Enumeration.md §5
```

---

## §4 — UNCONSCIOUS PROCESSING

### §4.1 Chunk-System — Sole Substrate

```
🟡🟢 CHUNK = STRENGTH-WEIGHTED ASSOCIATIVE NETWORK COMPILED THROUGH EXPERIENCE:

  Não KHÔNG tính toán — não TÌM KIẾM trong database.
  Database = chunks. Operators = vô thức (~95%) + PFC (~5%).

  🟢 Hebb (1949): "Neurons that fire together, wire together"


  CHUNK = ATOM:
    → Nhóm neurons đã wire together → fire thành 1 ĐƠN VỊ
    → GRADIENT (yếu → mạnh), không binary (có/không)
    → Proto-chunk → Compiled → Meta-chunk
    → Multi-modal từ gốc: chunk "mẹ" = mặt + giọng + ôm + ấm

  4 COMPILE MECHANISMS:
    ① Repetition — LTP strengthening (🟢 Bliss & Lømo 1973)
    ② Emotional peak — amygdala + NE, 1 lần đủ (🟢 Brown & Kulik 1977)
    ③ Multi-modal — nhiều kênh cùng lúc → wire across cortex
    ④ Sleep consolidation — hippocampus replay (🟢 Walker 2017)

  5 EXTERNAL INSTALL MECHANISMS (Chunk.md §2.3):
    ① Co-attention ② Imitation ③ Social referencing
    ④ Label installation ⑤ Cultural transmission
    → TẤT CẢ 5 yêu cầu TRUST GATE ở mức nào đó
    → Trust = ONLY BRIDGE giữa external → internal compile
    → (Collective-Body.md v2.1 §5: trust = cơ chế DUY NHẤT nối cấp 1 và cấp 2)

  3 COMPILE TYPES (Compile-Taxonomy.md v2.0):

    Experience Compile — Direct Short (~90%): body trải nghiệm trực tiếp → compile
      [toán → brain fire → reward] hoặc [không học → mắng → sợ]
      = Hardware fit (approach) hoặc Threat (avoidance). 1-2 nodes.

    Expertise Compile (~5%): repetition + PFC-directed + domain verify
      [bán hàng → feedback → adjust → compile] lặp 1000+ lần
      = Deliberate practice. Meta-chunks. "Chuyên gia = library rất sâu."

    Trust Compile — Installed + Collective (~5%): external source → trust gate → compile
      [mẹ nói học tốt → trust → compile "học=tốt"] = 1-2 nodes
      = Trust install. Social default. Chain dài SỐNG ở collective (Cấp 2).

    → Cùng 4 compile mechanisms, KHÁC LOẠI sử dụng.
    → ~90%/~5% = calibration anchor (§12.4).

  COMPILED QUALITY DIMENSION (PFC-Operations.md v1.0 §5):
    → Chunks compile xong → có QUALITY TAG vĩnh viễn (compile-time lock):

    ┌──────────────────┬────────────────────────────────────────────────┐
    │ Quality          │ Meaning                                         │
    ├──────────────────┼────────────────────────────────────────────────┤
    │ GENUINE-compiled │ Body confirmed qua domain feedback thật.        │
    │                  │ Approach-tagged. Self-Pattern-Modeling accurate. │
    │                  │ = Experience Compile + Expertise Compile.        │
    ├──────────────────┼────────────────────────────────────────────────┤
    │ SCHEMA-compiled  │ PFC-driven, chưa body-confirm đầy đủ.          │
    │                  │ Trust Compile dominant. Confabulation phổ biến. │
    │                  │ Self-Pattern-Modeling may be inaccurate.         │
    ├──────────────────┼────────────────────────────────────────────────┤
    │ THREAT-compiled  │ Compiled dưới stress/ép buộc.                   │
    │                  │ Avoidance-tagged. Trigger defensive Self-Pattern-Modeling.   │
    │                  │ = "Biết" nhưng body phản ứng tiêu cực.          │
    └──────────────────┴────────────────────────────────────────────────┘
    → Cùng "compiled" nhưng KHÁC tag → KHÁC Self-Pattern-Modeling capacity, KHÁC suốt đời

  ENTITY-COMPILED (Entity-Compiled.md v1.0):
    → Brain compile AGENT vào body-base ở STRUCTURAL level
    → Agent's state = MY state. Agent's loss = body-base amputation.
    → Hub-and-Spoke neural architecture (ATL hub + multi-modal spokes)
    → Formation: 40→80→200h exposure (schema acceleration, Tse 2007)
    → Dunbar capacity ceiling: chunks finite + maintenance + interference
    → Grief = opioid withdrawal khi Entity-Compiled bị cắt
    → Reference: Entity-Compiled.md v1.0 (1,231L, 67 citations)

  4 CONNECTION TYPES (Chunk.md §3):
    Type 1: Shared contamination (automatic, spreading activation)
    Type 2: Aha moment (DMN incubation → sudden burst)
    Type 3: Meta-chunk compile (repeated co-firing → merge)
    Type 4: Static logical linking (PFC deliberate — = "thinking")

  ACTIVATION DYNAMICS (Chunk.md §4):
    → Probability-weighted spreading activation (🟢 Collins & Loftus 1975)
    → 7-factor link strength: repetition, recency, emotional weight,
      multi-modal, context match, emotional state match, anchor strength
    → Competitive re-linking: new links compete with old (🟢 Nader 2000)
    → NEVER delete — only probability shift
    → Compiled chunks KHÔNG bao giờ bị xóa — chỉ probability shift

  "SCHEMA" TRONG V7.8 = OBSERVATION LABEL:
    → Schema = named chunk-network pattern (chunks + links + purpose)
    → Giống "feature" trong software: tên gọi cho composition of functions
    → Schema KHÔNG phải component riêng biệt — là CÁCH QUAN SÁT chunk networks
    → Vẫn hữu ích như shorthand. Không phải đặc tính kỹ thuật của brain architecture

  MODEL 3+1 (Body-Base.md v3.2 §3):

    3 COMPONENTS CHẠY ĐỒNG THỜI trên chunk substrate:
      ① VÔ THỨC (~95%): compile + fire + evaluate
      ② PFC (~5%): direct + sequence + observe
      ③ TRUST: gate + modulate + connect (individual ↔ external)
    + 1 BRIDGE:
      ④ EXTERNAL TOOLS (×∞): giấy, máy tính, AI → mở rộng PFC capacity

    → Trust = Component 3, KHÔNG phải property — vì trust GATE tất cả external install

  MODEL 3 CẤP (Collective-Body.md v2.1 §1):

    Cấp 1: Individual — compile SHORT ở body (1-2 nodes). File NÀY mô tả.
    Cấp 2: Collective — institutions/culture HOLD chain dài (distributed).
    Cấp 3: Framework — explanatory decomposition (chain analysis).

    → Individual cycle (file này) = Cấp 1
    → Trust = ONLY BRIDGE giữa Cấp 1 và Cấp 2

  Reference: Chunk.md v2.3 (full detail)
```

### §4.2 Body-Feedback — Continuous Evaluation

```
🟡🟢 BODY-FEEDBACK = CÁCH BODY ĐÁNH GIÁ MỌI THỨ LIÊN TỤC:

  REWARD + DISSONANCE — EVALUATIVE/DIRECT-STATE DIMENSION (CẢ 2 DIRECTIONS):

    EVALUATIVE REWARD (opioid — Reward-Signal-Architecture.md v2.0 §1):
      → Body-Feedback-Precondition pass → VTA → opioid hedonic hotspot (NAcc shell, VP, mOFC)
      → CÓ ĐIỀU KIỆN: cần 5 preconditions đồng thời
      → Learned/compiled: E₀ hardware-install → E₁ basic → E₂ complex → E₃ deep
      → Naltrexone blocks hoàn toàn (🟢 Blass & Ciaramitaro 1994)
      → Berridge "liking" = chỉ loại này

    DIRECT-STATE REWARD (non-opioid — Reward-Signal-Architecture.md v2.0 §2):
      → Body-state change itself IS reward (không cần Body-Feedback-Precondition)
      → Hardware from birth: CT afferents (touch), eCB CB1 (exercise),
        thermoreceptors (warmth), vestibular (rocking)
      → Naltrexone KHÔNG block (pathway khác)
      → BURNOUT-PROOF: khi Evaluative rewards exhausted, Direct-State vẫn accessible
      → Van der Kolk 2014: body-oriented therapy = activate Direct-State pathways

    EVALUATIVE DISSONANCE (compiled — Dissonance-Signal-Architecture.md v1.0 §1):
      → dACC + anterior insula (social pain: Eisenberger 2003)
      → CRH → amygdala (anxiety/threat: HPA axis)
      → CÓ ĐIỀU KIỆN: cần compiled chunks, PFC can modulate
      → Develops with age: E₀ bitter aversion → E₃ moral injury
      → MOST adult suffering = Evaluative Dissonance
      → Chunk-Shift = Evaluative-only proof (context thay đổi → re-evaluate)

    DIRECT-STATE DISSONANCE (hardware — Dissonance-Signal-Architecture.md v1.0 §1):
      → Nociception: A-delta + C fibers → substance P + glutamate + CGRP
      → Thermoreceptors, visceral signals, ghrelin (hunger), histamine (itch)
      → Hardware from birth: PFC minimal
      → NUMBNESS-PROOF: khi Evaluative processing tê liệt, Direct-State vẫn fire
      → Parallel burnout-proof (Direct-State Reward) = 2 sàn tiến hóa

    DISSONANCE SOURCES:
      → 3 genuine sources: nociception / mismatch / recalibration
      → "Mismatch" splits: hardware mismatch → Direct-State, compiled mismatch → Evaluative
      → Evaluative/Direct-State ORTHOGONAL to source classification

  DUAL-PULL ARCHITECTURE (Body-Feedback.md §2):

    ① HARDWARE PULL (bảo thủ, muốn smooth):
       → Hebbian LTP: patterns quen càng mạnh
       → Metabolic efficiency: compiled = low cost
       → Feature: comfort zone, routine, contentment
       → Dark side: stagnation, evolution lag

    ② DOMAIN PULL (đòi adapt, map reality):
       → Prediction-delta: pattern mới → dopamine → attention
       → Evolutionary: không map reality → không sống sót
       → Feature: learning, growth, curiosity
       → Dark side: burnout, neural wear

    ⭐ TENSION = EVOLUTIONARY FEATURE, NOT BUG:
       → Reward fires khi 2 lực ALIGN ("passion" = body thích + domain cần)
       → Dissonance fires khi 2 lực CONFLICT

  Body-Feedback-Precondition — 5 PRECONDITIONS FOR EVALUATIVE SIGNAL FIRE (Body-Feedback-Precondition.md):

    ┌───┬──────────────────────────┬────────────────────────────┐
    │ # │ Precondition             │ Failure → subjective        │
    ├───┼──────────────────────────┼────────────────────────────┤
    │ 1 │ Directed-Gap             │ "Không cần" / polite no     │
    │ 2 │ Chunk-Substrate          │ "Chả hiểu" / confusion      │
    │ 3 │ Delta-Gate               │ "Bình thường" / "quen rồi" │
    │ 4 │ Match-Range              │ Too alien or too familiar   │
    │ 5 │ Compile-Gate             │ "Ghét dù hiểu" / avoidance  │
    └───┴──────────────────────────┴────────────────────────────┘
    ALL 5 REQUIRED for full Evaluative signal. Direct-State KHÔNG cần Body-Feedback-Precondition.

  3 SATIATION TYPES (Gap-Body-Need.md v1.0 §2):

    ┌──────────────┬─────────────────────────┬────────────────────────┐
    │ Type         │ Mechanism                │ Ví dụ                   │
    ├──────────────┼─────────────────────────┼────────────────────────┤
    │ CYCLIC       │ Fill → deplete → refill │ Ăn, ngủ, social touch  │
    │ TONIC        │ Maintain continuous      │ Connection, autonomy   │
    │ GENERATIVE   │ Fill → expand → new gap │ Mastery, creativity    │
    └──────────────┴─────────────────────────┴────────────────────────┘
    → "Chán nhau" = Cyclic gap filled + no Generative gap remaining
    → Technology fills ROUTINE gaps → frontier shifts to GENUINE gaps

  HARDWARE-SUBSIDY (Valence-Propagation.md v3.0):
    → Body subsidize entity processing per Entity-Access Mức:
      Mẹ→con (MAX oxytocin) → romantic (limerence TEMP) → bạn (NONE)
    → VTA habituation SLOWER for subsidized entities
    → = TẠI SAO mẹ không "chán" con dù chăm mỗi ngày

  CHUNK DYNAMICS — TRỤC THỨ 4 (Body-Feedback-Mechanism.md v2.0):
    Body-feedback có 4 trục phân loại ORTHOGONAL:
      Trục 1 — Direction: reward/dissonance (dual-pull ở trên)
      Trục 2 — Magnitude: 14 levels (02-Dissonance.md)
      Trục 3 — Source: nociception/mismatch/recalibration
      Trục 4 — Chunk Dynamics: HOW chunks fire tạo signal
        → 2 input sources: Sensory-Driven / Pattern-Driven
        → 3 dynamics: Chunk-Shift / Chunk-Miss / Chunk-Gap
        → Compound: multi-layer chunk firing = multi-flavor signal

  Reference: Body-Feedback.md + Body-Feedback-Mechanism.md v2.1
    + Reward-Signal-Architecture.md v2.1 + Dissonance-Signal-Architecture.md v1.0
```

### §4.3 Cortisol — Amplifier

```
🟡🟢 CORTISOL = CHANGE-READINESS AMPLIFIER, KHÔNG PHẢI STRESS HORMONE:

  Cortisol KHÔNG phải component riêng biệt.
  Cortisol = PHYSICAL MECHANISM (hormone thật) chạy XUYÊN QUA toàn bộ cycle.

  MODULATES 3 THINGS:
    → SENSITIVITY: how strong body-input signals register
    → ENERGY: how sustained action can be
    → DIRECTION: approach (novelty) vs avoid (threat) — at compile time

  DIRECTION GATE (Chunk.md §2.4):
    → Cortisol tại compile time = determines chunk association tag
    → Novelty-direction cortisol → chunks tag APPROACH
    → Threat-direction cortisol → chunks tag AVOIDANCE
    → CÙNG cortisol level → KHÁC direction → KHÁC outcome hoàn toàn

  7 MODES (inverted-U):
    IDLE (quá thấp) → LAZY → ACTIVE → FOCUSED (optimal) → PUSH → FREEZE → CRASH (quá cao)

  ⚠️ PHÂN BIỆT QUAN TRỌNG — 2 cơ chế KHÁC NHAU:

    NE (Norepinephrine) → FREEZE TỨC THỜI (Cortisol-Baseline.md v2.1 §9.1):
      → Threat detect → amygdala → NE flood → α1 receptors → PFC OFFLINE
      → Timeline: milliseconds. KHÔNG phải damage — là DESIGN FEATURE
      → Recovery: seconds sau khi threat qua → PFC bật lại hoàn toàn
      → 🟢 Arnsten 2009, 2015 — α1/α2 mechanism

    CORTISOL → NEURAL WEAR MÃN TÍNH (Cortisol-Baseline.md v2.1 §9.2-§9.4):
      → Cortisol baseline CAO MÃN TÍNH (weeks-months-years)
      → → Glutamate cao liên tục → PFC dendrite retraction
      → → Worse pattern recognition → worse solving → more cortisol → loop
      → HPA paradox: acute trauma → HIGH cortisol, chronic PTSD → LOW cortisol
        (Yehuda: HPA axis recalibrate, KHÔNG phải "hết stress")
      → 🟢 Arnsten 2009, McEwen 2007

  Reference: Cortisol-Baseline.md v2.1 (full 3,059L)
```

### §4.4 Agent-Mechanism — Functions on Chunk Substrate

```
🟡 MỌI "MODULE" CŨ = FUNCTION CHẠY TRÊN CÙNG CHUNK SUBSTRATE:

  ⭐ KEY INSIGHT V2.0: Brain có 1 SIMULATION-ENGINE, KHÔNG PHẢI N modules riêng.
  TẤT CẢ functions dưới đây = APPLICATIONS chạy trên ENGINE này.
  (Simulation-Engine chi tiết → §6.5)

  SELF-PATTERN-MODELING (Self-Pattern-Modeling.md v3.1):
    → Dùng cảm nhận bản thân để MODELING người khác
      — dựa trên dự đoán họ cũng giống mình một phần
    → = Simulation-Engine-APPLICATION-1 (Other, Present, Simulate)
    → 1 mechanism × 3 dimensions:
      Processing Level (Compiled vs Fresh)
      Valence (positive → empathy | negative → strategic | extreme → dehumanize)
      Output Intensity (automatic background → deliberate)
    → Quality = f(chunk library depth × overlap × feedback)
    → Gap-clone impossible: 5-step proof (Bond-Architecture.md v2.0 §3)
    → Over-clone = observation label cho 3 cơ chế thật:
      redirect + compiled suppress + converge

  ENTITY-ACCESS GRADIENT (Entity-Access.md v1.2):
    → Brain builds PREDICTIVE ACCESS-RELATIONSHIP with entity for gap-filling
    → 3-Factor Model: Engine Mode × Gap-Need Profile × Access Confidence
    → Gradient Mức 0-5:

    ┌───────┬──────────────────┬────────────────────────────────────────┐
    │ Mức   │ Label            │ Meaning                                 │
    ├───────┼──────────────────┼────────────────────────────────────────┤
    │ 0     │ Tool/Service     │ Gap fill = transactional only           │
    │ 1     │ Utility          │ Repeated access, some prediction        │
    │ 2     │ Anchor           │ Stable gap source, body tracks          │
    │ 3     │ Deep             │ Entity-Compiled significant             │
    │ 4     │ Core             │ Entity = body-base structural           │
    │ 5     │ Excess           │ GẦN NHƯ DUY NHẤT gap source (clinical) │
    └───────┴──────────────────┴────────────────────────────────────────┘
    → Entity-Owned = PFC LABEL cho Mức 4-5 (observation, NOT mechanism)
    → Reference: Entity-Access.md v1.2 (73 citations)

  BOND-ARCHITECTURE (Bond-Architecture.md v2.0):
    → Entity-Compiled = 1 mechanism DUY NHẤT × 4 bond type configurations:

    ┌────────────────┬───────────────────────┬──────────────────────────┐
    │ Bond type      │ Hardware-Subsidy       │ Design                    │
    ├────────────────┼───────────────────────┼──────────────────────────┤
    │ Parent→Child   │ MAX (oxytocin flood)  │ Asymmetric, unconditional │
    │ Child→Parent   │ HIGH (attachment)     │ Dependency → autonomy     │
    │ Romantic       │ TEMP (limerence 6-18m)│ Bilateral, reproductive   │
    │ Friendship     │ NONE (zero subsidy)   │ Mutual, voluntary, FAST   │
    └────────────────┴───────────────────────┴──────────────────────────┘
    → Gap clone = STRUCTURALLY IMPOSSIBLE (architecture proof: 1 gap ≠ 2 entities)
    → Cùng mechanism, khác configuration → khác dynamics hoàn toàn

  RESONANCE DECLINE (Bond-Architecture.md v2.0 §4):
    → 2 Forces + 1 Fuel giải thích TẠI SAO resonance giảm theo thời gian:
      Force: Compiled-Suppress (STRONGEST — suppress drive riêng → source dies) ★ LEVERAGE
      Force: Reward-Habituated (VTA quen → prediction-delta giảm, Weber-Fechner)
      Fuel: Novelty threshold (prediction complete + Entity-Compiled saturated = 2 lenses)
    → True understanding = anti-compiled-suppress (meta-principle ALL bonds)

  BY-PRODUCT-SCALE (By-Product-Scale.md v1.0):
    → CÙNG by-product match mechanism × 3 scales khác nhau:
      Pair (L1): oxytocin, direct, fast, personal
      Hub (L2): serotonin, reputation, medium, group
      Institutional (L3): trust infrastructure, slow, system
    → Prestige = genuine resonance (opioid reward)
    → Dominance = forced resonance (relief, not reward)

  RESONANCE-SUSTAINABILITY (Resonance-Sustainability.md v1.0):
    → WHAT CONDITIONS predict sustained vs decaying resonance:
      3 Primitive Conditions: Proximity × Duration × Agent-mode
      3 Modalities INDEPENDENT: Verbal / Non-verbal / Body-level
      4 Silence types: chỉ Intrinsic bền vững
      4-Layer synthesis: conditions × gap flexibility × modalities × amplification

  PHANTOM 4-FACTOR (Entity-Valence-Dynamics.md v2.0):
    → Khi entity MẤT (chết, chia tay, xa cách):
      ① Entity-Compiled depth (how deep in body-base)
      ② Gap redirect difficulty (specialized gaps = harder)
      ③ Hardware-Subsidy withdrawal (oxytocin/vasopressin drop)
      ④ Compiled pattern persistence (body still fires for absent entity)
    → Grief intensity = f(4 factors) — explains why some losses devastating, others mild

  EMPATHY (Empathy.md v4.0):
    → = Self-Pattern-Modeling applied to other agent's states
    → Connection ⊃ Empathy (mechanism ⊃ observation)
    → PFC budget × empathy: Fresh Self-Pattern-Modeling costs PFC → competes với ALL other tasks
    → Burnout = Compiled-Suppress + PFC depletion (NOT "too much empathy")

  VALENCE (Valence-Propagation.md v3.0):
    → Body's assessment of how entity affects body-inputs
    → Structural valence (compiled, stable) vs Current valence (momentary, fluctuating)
    → 3 Firing Modes: Tonic (background hum) / Phasic (acute spike) / Compound (mixed)
    → Per-entity dynamics: mỗi entity → unique valence profile
    → Hardware-Subsidy × VTA habituation: subsidized entities = slower habituation

  IMAGINATION (Imagine-Final.md v3.0):
    → = Simulation-Engine-APPLICATION-2 (Self, Future, Simulate+Construct)
    → KEY REFRAME v3.0: Imagine-Final ≠ mọi body prediction
      → Hardware prediction (subcortical: khát→uống) ≠ Imagine-Final
      → Imagine-Final = CONSTRUCTIVE simulation only (chunk-based, PFC-accessible)
    → Body-feedback evaluates imagined scenarios (body reacts to imagination)
    → Imagined chunks CAN trigger real body-base responses

  NONE of these need separate module. ALL run on Simulation-Engine substrate.
  Agent-Mechanism.md v2.1 = integration hub (11 sub-files, ~15,000L).
```

---

## §5 — FEELING (Bridge Unconscious → PFC)

```
🟡🟢 FEELING = WHAT PFC SEES KHI OBSERVE BODY-CHUNK INTERACTION:

  KHÔNG PHẢI hệ thống riêng biệt. KHÔNG có "feeling module."
  Feeling = INTERFACE giữa body computation và PFC awareness.
  Body = xử lý (compiled patterns fire). Feeling = kết quả hiện lên. PFC = observe.

  PFC = LAWYER (Feeling.md v3.0):
    → PFC KHÔNG phải judge (không tạo verdict mới)
    → PFC = lawyer (tìm argument cho verdict body ĐÃ đưa ra)
    → Body compute FIRST → Feeling emerge → PFC argue/justify LAST
    → "Rationalizing" = PFC làm lawyer cho body's verdict

  3 ĐẶC TÍNH DEFINING:
    ① MULTI-SOURCE: convergence từ nhiều body systems đồng thời
    ② INTEGRATED: unified sense, không phải list of signals
    ③ OBSERVABLE: threshold phụ thuộc magnitude × clarity (2 chiều)

  7-LAYER FIDELITY GRADIENT (Feeling.md v3.0 §2):

    Feel-RawSignals: Raw body signals              100% fidelity
    Feel-Integration: Integration (insula+ACC+VMPFC)  ~95%
    Feel-Consciousification: Consciousification              ~90%
    ════════ PFC THRESHOLD ════════════════════════
    Feel-Observation: Observation                     ~85%
    Feel-Location: Location                        70-90%
    Feel-Labeling: Labeling                        40-80%  ← CRITICAL LOSS
    Feel-Explanation: Explanation                     20-70%  ← MOST RISKY

    → Wise: trust Feel-Consciousification-Feel-Observation (body noticeable, pre-label)
    → Naive: trust Feel-Labeling-Feel-Explanation (label + explanation = lossy nhất)
    → Training = đưa attention ngược về Feel-Consciousification-Feel-Observation

    🟡 % = calibration anchor, KHÔNG phải đo lường (§12.4).

  ⭐ PFC OBSERVATION THRESHOLD — 2 CHIỀU (magnitude × clarity):

    MAGNITUDE = cường độ body signal (body-feedback generate):
      → Cao: đau, sợ, phấn khích → signal loud → PFC khó bỏ qua
      → Thấp: nagging unease nhẹ → signal quiet → dễ lọt

    CLARITY = chunk density cho phép PFC PHÂN BIỆT signal nói gì:
      → Cao: expert biết chính xác "đây là gì" → detect dù magnitude nhẹ
      → Thấp: novice thấy "có gì đó" nhưng không biết gì

    ┌────────────┬──────────────────────┬──────────────────────────┐
    │            │ MỜ (ít chunks)        │ RÕ (nhiều chunks)         │
    ├────────────┼──────────────────────┼──────────────────────────┤
    │ MẠNH       │ PFC thấy nhưng mờ    │ PFC thấy rõ ràng         │
    │            │ "có gì đó sai"       │ "cái này sai ở ĐÂY"     │
    ├────────────┼──────────────────────┼──────────────────────────┤
    │ NHẸ        │ PFC không notice     │ PFC tinh tế phát hiện    │
    │            │ Signal quá yếu +    │ Expert subtle detection   │
    │            │ quá mờ → bỏ qua    │ sommelier, chuyên gia     │
    └────────────┴──────────────────────┴──────────────────────────┘

    → Clarity CAO = HẠ magnitude threshold → expert "thấy nhiều hơn"
    → Self-signal interoception (§3.2.1) = clarity cho TOÀN BỘ feeling
    → Alexithymia = clarity thấp → PFC "deaf" to own body (🟢 Bird & Cook 2013)

  COMPILED vs FRESH FEELING:
    → Compiled feeling: body đã biết (chuyên gia → "cái này sai" tức thì)
    → Fresh feeling: PFC mới observe lần đầu (novice → "có gì đó...")
    → Compiled = faster, cheaper, more accurate (in familiar domains)
    → Fresh = slower, expensive, but necessary for new domains
    → Cùng mechanism, khác processing position trên Compiled/Fresh spectrum

  7 LOẠI FEELING (cùng mechanism):
    ① Body-physical: "đói", "mệt", "đau"
    ② Emotional: "vui", "buồn", "giận", "sợ"
    ③ Social reading: "người kia không tin"
    ④ Cognitive/prediction: "bài này đúng"
    ⑤ Predictive/intuition: "có gì đó không ổn"
    ⑥ Valence: "thích cái này", "ghét cái tên"
    ⑦ Schema-triggered: "bình yên khi về nhà"
    → TẤT CẢ = cùng mechanism: integrated body signal → PFC observe

  TEMPORAL ORDER (invariant):
    Body compute FIRST → Feeling emerge → PFC observe LAST
    → 🟢 Damasio 1994, 1999: somatic markers PRECEDE conscious decision
    → Feeling KHÔNG tạo ra thông tin mới — feeling REPORT body state

  Reference: Feeling.md v3.0 (full, PFC=Lawyer integrated)
```

---

## §6 — PFC (Observer + Orchestrator)

### §6.1 PFC = Observer, KHÔNG phải Controller

```
🟡🟢 PFC CÓ THỂ:
  → OBSERVE: đọc feeling, detect chunk activations
  → HOLD: ~4±1 WM slots (🟢 Cowan 2001) — amplify target pattern
  → SUPPRESS: block unwanted pattern (costly, unsustainable)
  → SEARCH: hold chunks → bias spreading activation direction
  → TYPE 4 LINKING: deliberate "thinking" (PFC hold A + B → check overlap → body vote)
  → SIMULATION-ENGINE: run applications (Self-Pattern-Modeling, Imagine-Final, Self-Observation)
  → DOMAIN-CHECK: verify "smooth" vs reality (Dual Check — §2)
  → ORCHESTRATE: hold goals → bias unconscious processing direction

🟡🟢 PFC KHÔNG THỂ:
  → FEEL directly (phải NHẬN từ body qua feeling bridge)
  → COMPILE tự động (vô thức compile, PFC chỉ observe kết quả)
  → RUN 95% background processing
  → OVERRIDE body-base khi signal quá mạnh (đói cực → ăn ngấu, crush → ấp úng)
  → CONTROL motor trực tiếp (PFC hold "viết con chó" → vô thức execute gõ phím)

  ⭐ PFC HARDWARE SPECS (COMT, DRD4, WM capacity, modality balance,
  connectivity limits) → Core-Hardware.md §5.
  File này chỉ mô tả PFC FUNCTION — CÓ THỂ và KHÔNG THỂ làm gì.
```

### §6.2 PFC Orchestrate — Indirect Control

```
🟡 PFC KHÔNG ĐIỀU KHIỂN TRỰC TIẾP BODY-BASE:

  PFC hold chunks → BIAS spreading activation trong vô thức
  → Vô thức tự phản ứng dây chuyền theo bias
  → Body-output tự execute theo compiled chunks

  VÍ DỤ CƠ CHẾ:

    PFC hold "viết con chó":
      → Vô thức đã compile [gõ c-o-n space c-h-ó]
      → Ngón tay tự gõ → PFC nhìn lại: đúng ✓

    Chuyên gia xem tranh ở chợ đồ cũ:
      → Lướt qua → vô thức match weak pattern "nét vẽ kỳ lạ"
      → PFC notice → cầm lên, xem kỹ hơn
      → PFC CHỦ ĐỘNG amplify input cho vô thức (xem kỹ hơn)
      → Vô thức match SÂU hơn → "bức tranh đặc biệt thật"
      → PFC không "thấy" tranh đẹp — PFC hold attention → vô thức match → body reward

  KHI PFC BẤT LỰC:
    Đói cực nặng → body-base signal quá mạnh → PFC hold "ăn lịch sự" nhưng overwhelm
    Gặp crush → body fire quá mạnh → PFC hold "bình tĩnh" nhưng chunks chưa compiled

  → PFC effectiveness = f(chunks đã compiled cho tình huống đó)
  → Nhiều chunks → PFC chỉ hold direction, vô thức run
  → Ít chunks → PFC bất lực dù hold mạnh cỡ nào
```

### §6.3 PFC Activation ≈ f(dissonance)

```
🟡 95/5 = OBSERVATION PARAMETER, KHÔNG PHẢI RATIO CỐ ĐỊNH:

  PFC hoạt động 100% NĂNG LỰC của nó — nhưng PHẠM VI kiểm soát giới hạn.
  PFC activation level TƯƠNG ỨNG với dissonance level:

    Vô thức ổn, môi trường ổn → PFC ~ 0% (không cần)
    Mild novelty → PFC ~ 5-15% (observe, light hold)
    Active problem → PFC ~ 20-40% (Type 4 linking, search)
    High stakes → PFC ~ 40-70% (strategic hold, domain-check)
    Crisis → PFC ~ 70-95% (full engagement, override attempts)
    Acute threat → NE α1 FREEZE — PFC offline tạm (ms, design feature)
    Chronic overload → Cortisol neural wear — PFC dendrite retraction (DAMAGE)

  → "95% vô thức" = observation that MOST processing doesn't need PFC
  → PFC có thể tham gia bất cứ lúc nào nếu dissonance sufficient
```

### §6.4 PFC Dynamic Configurations

```
🟡 PFC KHÔNG PHẢI ON/OFF — CÓ 6 CONFIGURATION MODES (PFC-Configuration.md v1.1):

  ① Normal: full function suite available
  ② Reallocation (Flow): task-serving ON, self-monitoring OFF — effortless
  ③ Reconfigured: stress shifts function balance
  ④ Disconnected (Threat): NE α1 → ALL PFC functions OFF — subcortical takeover
  ⑤ Hyperactivated (Dissociation): 4 functions WEAPONIZED — emotional numbness
  ⑥ Disintegrated (Psychedelic): nearly ALL OFF, Modify ENHANCED — structural change

  Configuration ≠ Participation (Drive.md §2). Orthogonal:
  "PFC bận CỠ NÀO" (participation) ≠ "PFC wired THẾ NÀO" (configuration).

  v1.1: +PTSD ④↔⑤ oscillation, +ADHD DMN interference (Config ① unstable)
  Reference: PFC-Configuration.md v1.1
```

### §6.5 Simulation-Engine — 1 Engine, N Applications

```
🟡🟢 BRAIN CÓ 1 GENERAL-PURPOSE SIMULATION-ENGINE (Simulation-Engine.md v1.0):

  KHÔNG PHẢI N modules riêng (empathy module, imagination module, self-reflection module).
  TẤT CẢ = APPLICATIONS chạy trên CÙNG 1 ENGINE.

  ENGINE = Constructive Simulation Substrate:
    DMN + vMPFC + anterior insula + hippocampus

  3 COMPONENTS:
    ① Interoception (anterior insula): ĐỌC body signals
    ② Constructive Simulation (DMN + hippocampus): RECOMBINE chunks vào scenarios
    ③ Self/Other Model (mPFC gradient): VENTRAL = self+close, DORSAL = distant

  3 AXES XÁC ĐỊNH APPLICATION:
    Target (Self ↔ Other) × Time (Past ↔ Future) × Operation (Observe ↔ Construct)

  APPLICATION = TỌA ĐỘ trong không gian 3 trục:

    ┌─────────────────────────┬───────────┬────────┬──────────────────┐
    │ Application             │ Target    │ Time   │ Operation        │
    ├─────────────────────────┼───────────┼────────┼──────────────────┤
    │ Self-Pattern-Modeling   │ Other     │ Present│ Simulate         │
    │ Self-Observation        │ Self      │ Present│ Observe          │
    │ Imagine-Final           │ Self      │ Future │ Simulate+Constr. │
    │ Episodic Memory         │ Self      │ Past   │ Reconstruct      │
    │ Counterfactual          │ Self      │ Past   │ Construct        │
    │ Moral Judgment          │ Other     │ Future │ Simulate         │
    │ Creativity              │ Abstract  │ Future │ Construct        │
    └─────────────────────────┴───────────┴────────┴──────────────────┘

  ⭐ DECISIVE PROOF — ALEXITHYMIA:
    → Component ① (interoception) DAMAGED → ALL applications degrade
    → Self-Pattern-Modeling kém, Imagine-Final mờ, Self-Observation yếu
    → = CÙNG engine → 1 component hỏng → ALL apps affected (🟢 Bird & Cook 2013)

  TRAINING IMPLICATION:
    → Luyện 1 application → improve TOÀN BỘ (shared engine substrate)
    → Mindfulness → tốt hơn ở Self-Pattern-Modeling VÀ Imagine-Final

  mPFC GRADIENT = ENTITY-ACCESS NEURAL MIGRATION:
    → Ventral mPFC = self + close entities (Entity-Access Mức 3-4)
    → Dorsal mPFC = distant entities (Entity-Access Mức 0-1)
    → Khi entity compile sâu → migrate từ dorsal → ventral
    → = Entity-Access gradient CÓ neural correlate thật

  Reference: Simulation-Engine.md v1.0 (900L, 27 citations)
```

### §6.6 PFC-Operations — Hold + Suppress + Budget

```
🟡 PFC CÓ 2 OPERATIONS CƠ BẢN (PFC-Operations.md v1.0):

  ┌──────────────┬──────────────────────────────────────────────────────┐
  │ Operation    │ Mechanism                                             │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ HOLD         │ Amplify target pattern (tăng activation)              │
  │              │ CAN compile → sustainable (body learns over time)     │
  │              │ Cost: moderate, giảm dần khi compile                  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ SUPPRESS     │ Block unwanted pattern (giảm activation)              │
  │              │ CANNOT compile "not" → unsustainable                  │
  │              │ Cost: HIGH, KHÔNG giảm (phải hold liên tục)           │
  │              │ = Tại sao "đừng nghĩ về con gấu trắng" thất bại     │
  └──────────────┴──────────────────────────────────────────────────────┘

  4 TỔ HỢP:
    Hold old + Hold new → Genuine shift (ideal)
    Hold new + Suppress old → Compiled suppress (common but fragile)
    Hold old only → Stagnation (comfort zone)
    Suppress old only → Depletion (futile)

  3 OUTCOMES:
    Genuine Shift: old pattern weakens naturally, new strengthens → permanent
    Compiled Suppress: old stays, new blocks → fragile, relapse risk
    Failure: PFC runs out of budget → old fires again

  ⭐ PFC BUDGET = FINITE SHARED RESOURCE:
    → PFC = universal resource: work, parenting, relationships, self-regulation
    → Mệt ở work → Self-Pattern-Modeling cho con YẾU → KHÔNG phải "không yêu con"
    → Parent-child = highest PFC cost (asymmetric: parent always monitors child)
    → Budget recharges: sleep, rest, routine (compiled chunks = cheaper)

  COMPILED QUALITY × PFC OPERATIONS:
    → Genuine-compiled chunks: PFC can use efficiently (low cost)
    → Schema-compiled chunks: PFC uses but with confabulation risk
    → Threat-compiled chunks: PFC must suppress → HIGH cost, unstable

  Reference: PFC-Operations.md v1.0 (30 citations)
```

---

## §7 — BODY-OUTPUT

```
🟡 BODY-OUTPUT = HÀNH VI ẢNH HƯỞNG DOMAIN:

  MOTOR: compiled chunks → movement
    → Walking, reaching, typing, cooking,...
    → PFC hold intention → vô thức execute motor details
    → Expert: meta-chunks → smooth auto execution
    → Beginner: PFC micromanage → clumsy

  SPEECH: compiled language chunks → verbal output
    → PFC hold "what to say" → vô thức: phonology + prosody + grammar
    → 3-tier anchor system: individual → group → global (lossy)

  EXPRESSION: facial, postural, vocal (often unconscious)
    → Micro-expressions: vô thức fire BEFORE PFC can suppress
    → Body language: compiled postural schemas
    → Vocal tone: autonomic modulation (Porges polyvagal)

  → BODY-OUTPUT thay đổi DOMAIN CỤC BỘ → new stimuli → loop continues
  → Domain bản chất không đổi — cá nhân tương tác + di chuyển + đổi góc nhìn
  → Feedback: reality responds (domain feedback thật) → body evaluate → adjust
```

---

## §8 — OBSERVATION PARAMETERS

```
🟡 "DRIVES" VÀ "SCHEMAS" CŨ = THAM SỐ PHỤC VỤ QUAN SÁT:

  Không phải components kiến trúc. Là named patterns quan sát từ cycle.
  Giá trị: giúp mô tả, predict, communicate. Không phải mechanism.

  ┌──────────────┬──────────────────────────────────────────────────────┐
  │ Parameter    │ Quan sát cái gì                                       │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Schema       │ Named chunk-network pattern (software "feature")      │
  │              │ Chunks + links + purpose = observation, not component  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Novelty      │ Positive prediction-delta pattern (Drive.md v1.2)     │
  │              │ DRD4: depth vs breadth tradeoff                       │
  │              │ 2 dạng: Sensory-Driven / Imagination-Driven           │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Threat       │ Dissonance from predicted harm (Threat.md v1.2)       │
  │              │ 5 mức × 3 trục. Modern = anticipation-dominant        │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Boredom      │ Unified formula: Dissonance + Imagine-Final mờ        │
  │              │ (Boredom.md v2.0) 6 nguồn dissonance, Resonance Decline │
  │              │ ⑥ By-product match dừng → resonance decay felt        │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Status       │ Resource Access Map (Status.md v2.0)                  │
  │              │ Evolutionary: resource access = body-base reward THẬT │
  │              │ Spectrum: hổ(1D) → khỉ(hierarchy) → người(multi-dim) │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Protect      │ Loss aversion + ownership chunk patterns              │
  │              │ (Protect.md v1.0) f(replaceability × attachment)      │
  │              │ Vasopressin + cortisol threat-pull. Giving đối trọng  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Connection   │ 3 Generative Primitives (Connection.md v5.0)          │
  │              │ ❶ Hardware × ❷ Self-Pattern-Modeling Compiled/Fresh    │
  │              │ × ❸ Per-Agent Valence                                 │
  │              │ Entity-Access gradient × connection spectrum           │
  │              │ Hardware-Subsidy (MAX → NONE per entity type)          │
  │              │ 4-Layer Sustainability model                          │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Meaning      │ Life-level Anchor-Schema ổn định (Meaning.md v2.0)    │
  │              │ 5 types: GOAL/STATE/IDENTITY/FAITH/ROLE               │
  │              │ Mỗi người meaning KHÁC vì optimal anchor KHÁC        │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Mastery      │ Domain chunk accumulation + sustained delta rule      │
  │              │ Generative gap: fill → expand → new gap                │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Autonomy     │ Prediction accuracy pattern (Autonomy.md + Hardware)   │
  │              │ "Tôi quyết định → kết quả tôi muốn" = high accuracy  │
  │              │ vmPFC + DRN controllability learning                   │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Disgust      │ Gustatory/olfactory rejection threshold               │
  │              │ Hardware: rejection threshold innate                   │
  │              │ What triggers: heavily learned (cultural)              │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Gratitude    │ Tầng 5 observation (Gratitude.md v1.1)                │
  │              │ 9 prerequisites đồng thời, agent-entity only          │
  │              │ 3 anti-habituation mechanisms. "Cảm ơn" = body tool  │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Obligation   │ Compiled prediction về cost maintain access           │
  │              │ (Obligation.md v1.0) 5-factor + StatusGap. 6 types   │
  │              │ Tiền = obligation technology. Access cost = mode shift│
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Melody       │ Emergent state of all systems running simultaneously │
  │              │ Good Melody 4 criteria: hardware smooth + map accurate │
  │              │ + map wide + sustainable long-term                     │
  ├──────────────┼──────────────────────────────────────────────────────┤
  │ Passion      │ When hardware pull + domain pull ALIGN (rare, quý)   │
  │              │ Gap-Distribution-Profile alignment indicator           │
  └──────────────┴──────────────────────────────────────────────────────┘

  CROSS-SPECIES PATTERN:
    Ở động vật: hardware (hormone) → behavior trực tiếp
    Ở con người: hardware → chunk processing → behavior
    = Cùng hormones, nhưng chunk system phức tạp → override đáng kể

  GIÁ TRỊ CỦA OBSERVATION PARAMETERS:
    → Predict patterns: người thích novelty X → xu hướng tiếp tục
    → Communicate: "anh ấy rất protect" dễ hiểu hơn "ownership chunks + loss aversion"
    → Diagnose: status thấp + connection thiếu + meaning absent = depression risk
    → NHƯNG: không phải mechanism — không dùng để thiết kế can thiệp
    → Can thiệp phải ở level mechanism: thay đổi body-input, compile chunks mới
```

---

## §9 — DEVELOPMENT TRAJECTORY

```
🟡 DEVELOPMENT = CHUNK DENSITY TĂNG DẦN:

  Cùng architecture từ sơ sinh tới chuyên gia.
  Khác: lượng chunks tích lũy + compiled depth.

  ┌────────────┬────────────────────────────────────────────────────────┐
  │ Stage      │ Chunk state → Behavior                                 │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Newborn    │ Near-zero chunks (some prenatal compiled: auditory)    │
  │            │ → Gross reward/dissonance → cry/smile                  │
  │            │ → PFC hardware ONLINE BUT chunks missing               │
  │            │ → Pattern matching limbic (arousal contagion, NOT mirror)│
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Infant     │ Proto-chunks building rapidly                          │
  │ (0-12mo)   │ → Visual arc, auditory arc, motor arc compiling       │
  │            │ → Social referencing start (6-9mo)                     │
  │            │ → Entity-Compiled begins: mẹ = first entity compiled  │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Toddler    │ Compiled chunks + self-other distinction              │
  │ (1-3yr)    │ → Rouge test (18-24mo, Amsterdam 1972)                │
  │            │ → TRUE Self-Pattern-Modeling starts (14-24mo, Warneken)│
  │            │ → Verbal labels → feeling detection improves           │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Child      │ Language chunks + label system                        │
  │ (3-10yr)   │ → Logic-planning enabled via verbal anchors            │
  │            │ → Complex emotions: ấm ức, ghen tị, tự hào            │
  │            │ → Cultural chunk installation accelerating             │
  │            │ → Entity-Access developing: Mức 0-1 → Mức 2-3         │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Teen       │ Abstract chunks + identity schemas                    │
  │ (10-18yr)  │ → "Tôi là ai", "ý nghĩa cuộc đời"                   │
  │            │ → Imagine-Final increasingly sophisticated             │
  │            │ → Domain specialization starting                       │
  │            │ → Bond types diversifying (friendship, romantic emerge) │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Adult      │ Deep domain chunks + nuanced feeling                  │
  │            │ → Expert intuition in practiced domains               │
  │            │ → Entity-Compiled deep relationships (Mức 3-4)        │
  │            │ → Compiled/Fresh ratio shifts toward Compiled          │
  │            │ → PFC budget management = key adult skill              │
  ├────────────┼────────────────────────────────────────────────────────┤
  │ Expert     │ Deep + cross-domain → creative, accurate intuition    │
  │            │ → 50,000+ patterns (Chase & Simon 1973 chess)          │
  │            │ → Meta-chunks → PFC freed → fluid performance         │
  │            │ → Expertise = large trigger surface + novelty direction│
  └────────────┴────────────────────────────────────────────────────────┘

  COMPILABLE ARCHITECTURE (Body-Base.md v3.2 §2, Inter-Body-Mechanism.md v1.1):
    → Body hardware DESIGNED to compile (Compilable-dominant destination)
    → Receptors → neurons → synaptic plasticity → Hebbian → compile
    → 3-Layer Evolution: Hardware → Compiled → Cultural
      Hardware: evolved specs (receptor sensitivity, hormone ratios)
      Compiled: individual accumulated chunks (experience + expertise + trust)
      Cultural: collective-maintained patterns (language, norms, institutions)
    → = TẠI SAO body works this way: evolution selected for compilable architecture

  CRITICAL PERIODS:
    → Some baselines lock during sensitive periods
    → Native phoneme by 7-10 (Kuhl 1992)
    → Attachment style by 1-3
    → Self-signal interoception developmental foundation (early caregiving)
    → CHUNKS compiled during critical periods = especially durable + influential

  RECEPTIVE-PRODUCTIVE ASYMMETRY (Chunk.md §11.3):
    → Receptive chunk formation PRECEDES productive by ~6-12 months
    → "Hiểu" trước "làm được" = receptive compiled, productive chưa
    → Applies to ANY skill, not just language
```

---

## §10 — MULTIPLE TIMESCALES

```
🟡 CYCLE CHẠY Ở NHIỀU TIMESCALES ĐỒNG THỜI:

  ms:       L0 reflex (circuit breaker, trước unconscious)
  100ms:    Chunk activation, spreading activation, body-feedback
  seconds:  Perception-action micro-cycle, feeling emerge
  minutes:  Mood shift, state change, deliberate thinking
  hours:    Problem solving, schema update, reconsolidation window
  days:     Baseline adaptation (delta rule), habit strengthening
  weeks:    Chunk network restructuring, new skill compile
  months:   Schema restructuring, identity shift, therapy effects
  years:    Development trajectory, expertise build
  decades:  Permanent baseline calibration, critical period effects

  TẤT CẢ CHẠY ĐỒNG THỜI — không tuần tự.
  Framework phải handle tất cả timescales, không chỉ acute.
```

---

## §11 — KEY REFRAMES

```
📌 REFRAMES LỚN — TỪ V7.5 QUA 28-SESSION DRILL:

  V7.5 → V7.8 (10 reframes gốc):

  1. L2 Quality layer REMOVED
     → "Quality channels" = L1 inputs với baseline shifted by delta rule

  2. L3 Drives COLLAPSED → observation parameters
     → Novelty, Status, Protect = emergent patterns, not separate operators

  3. Schema System → Chunk-System (sole substrate)
     → Schema = observation label cho chunk network patterns

  4. Layer priority → Signal strength
     → Loudest signal wins, regardless of "layer"

  5. Cross-cutting → Properties of cycle
     → Cortisol = physical mechanism, Empathy = function on chunk substrate

  6. Imagine (PFC layer) → PFC (component in cycle)
     → Imagination = one PFC function among several

  7. Connection (unclear position) → Solved
     → L1 multi-input aggregate + Entity-Compiled + attachment chunks

  8. Feeling (implicit) → Explicit bridge
     → 7-layer fidelity gradient, critical position in cycle

  9. Development (unclear) → Chunk density trajectory
     → Same architecture, different chunk density

  10. Architecture metaphor: Layers → Cycle
      → From stack to loop. Better matches actual mechanism.

  POST-DRILL REFRAMES (10 reframes mới từ 28-session drill):

  11. Entity-Compiled = structural body-base integration
      → Agent compile vào body ở STRUCTURAL level. Loss = amputation.
      → KHÔNG chỉ "mối quan hệ" — là neural architecture thật.

  12. Simulation-Engine = 1 engine, N applications
      → Self-Pattern-Modeling, Imagine-Final, Self-Observation = CÙNG engine.
      → Alexithymia = decisive proof. Luyện 1 → improve ALL.

  13. PFC Budget = shared finite resource
      → Mệt work → kém parenting. KHÔNG phải "không yêu" — là hết budget.
      → Hold vs Suppress: Hold CAN compile, Suppress CANNOT.

  14. Compiled Quality = compile-time lock
      → Genuine vs Schema vs Threat. Cùng "compiled" nhưng KHÁC tag suốt đời.
      → Explains: tại sao trust compile dễ confabulate, threat compile dễ trigger.

  15. Hardware-Subsidy = body subsidize entity processing
      → Mẹ→con MAX, romantic TEMP, bạn NONE.
      → = TẠI SAO mẹ không "chán" con. Friendship decay FAST vì zero subsidy.

  16. 3 Satiation Types = Cyclic / Tonic / Generative
      → KHÔNG phải tất cả gaps giống nhau. "Chán nhau" = Cyclic gap filled.
      → Technology fills Cyclic/Tonic → frontier = Generative.

  17. Entity-Access gradient = Mức 0-5
      → KHÔNG binary "yêu/không yêu" — là GRADIENT liên tục.
      → Entity-Owned = PFC LABEL cho Mức 4-5 (observation, NOT mechanism).

  18. Evaluative vs Direct-State Reward
      → 2 hệ reward KHÁC NHAU. Berridge chỉ study Evaluative (opioid).
      → Direct-State = burnout-proof, hardware, always available.

  19. Resonance Decline = 2 Forces + 1 Fuel
      → Resonance GIẢM theo thời gian = NORMAL (Compiled-Suppress + Reward-Habituated + novelty threshold).
      → Gap clone IMPOSSIBLE. True understanding = anti-compiled-suppress.

  20. Self-Pattern-Match → Self-Pattern-Modeling
      → Rename: "Match" implies passive. "Modeling" = active constructive process.
      → = Simulation-Engine-APPLICATION-1, KHÔNG phải standalone module.

  21. Evaluative/Direct-State = GENERAL body-feedback dimension (cả reward VÀ dissonance)
      → Reward-Signal-Architecture v2.0 chỉ defined cho reward. Dissonance-Signal-Architecture v1.0 extends cho dissonance.
      → Cùng architecture (Evaluative/Direct-State, insula gradient, E₀→E₃).
      → Khác neurochemistry: reward = opioid/CT/eCB, dissonance = substance P/dACC/CRH.
      → Evaluative Gates Direct-State = GENERAL mechanism (Placebo/Nocebo = proof).
      → Numbness-proof (dissonance) parallel burnout-proof (reward) = 2 sàn tiến hóa.
```

---

## §12 — HONEST ASSESSMENT

### §12.1 Cái framework này provides

```
🟡 THEORETICAL CONTRIBUTIONS:

  → Cycle-based architecture matching actual mechanism
  → Chunk-System as sole substrate (simplification + accuracy)
  → Observation parameters replacing component taxonomy
  → PFC as observer + indirect orchestrator
  → Simulation-Engine: 1 engine, N applications (unified substrate)
  → Entity-Compiled: structural body-base integration
  → Entity-Access gradient Mức 0-5 (continuous, not binary)
  → Hardware-Subsidy spectrum per entity type
  → 3 Satiation Types (Cyclic/Tonic/Generative)
  → Compiled Quality dimension (genuine/schema/threat)
  → PFC Budget as shared finite resource
  → Evaluative vs Direct-State Reward (2 independent systems)
  → Bond-Architecture: 1 mechanism × 4 configurations
  → Resonance Decline 2 Forces + 1 Fuel (gap clone impossible)
  → Body-Feedback 2-signal model + 4 axes classification
  → Body-Feedback-Precondition 5-precondition hypothesis
  → Dual-Pull architecture
  → Signal strength replacing layer priority
  → Dual Check: body = quality controller, domain = arbiter
  → 3 Domain Types (Reality/Abstract/Abstract-Dynamic)
  → Development as chunk density trajectory

🟢 EMPIRICAL GROUNDING:

  → 130+ files, 35,000+ dòng phân tích chuyên sâu
  → 500+ research citations across 30+ topic areas
  → 28-session drill + 6-session foundation rewrite
  → 15/15 case tests PASS (Phase R)
  → 50 extreme cases analyzed (Body-Base-Example.md)
  → Hall 2019 NIH = direct empirical validation (delta rule)
  → Alexithymia = decisive proof (Simulation-Engine shared substrate)
  → Cross-species patterns validated (Berridge, Panksepp, Schultz)
```

### §12.2 Cái framework này KHÔNG provides

```
⚠️ SCOPE LIMITS:

  → Quantitative individual baselines (descriptive only)
  → Precise adaptation rates (qualitative)
  → Clinical protocols (hypothesis generator, not treatment)
  → Biomarker specifications (architecture, not measurement)
  → Dose-response cho interventions (future + empirical work)
  → Consciousness/qualia explanation (out of scope)
  → Precise boundary L0↔L1 transition mechanism (neuroscience open question)
  → Quantitative: khi nào PFC override thành công vs thất bại
```

### §12.3 Open questions

```
✅ RESOLVED từ v1.0 (qua 28-session drill):

  3. Collective architectures scope → ✅ Collective-Body.md v2.1 (Model 3 cấp)
  4. Schema-body coupling → ✅ Body-Coupling.md v3.0 (full mechanism)
  7. How PFC "hold" biases spreading activation → ✅ PFC-Operations.md v1.0

🟡 PARTIALLY RESOLVED:

  1. Meaning cases not directly tested (B21-B23)
     → Meaning.md v2.0 (5 types, anchor-schema). Original test protocol chưa replicate.
  2. Mastery compound under-specified
     → Autonomy.md §4.7 + Gap-Body-Need v1.0 (Generative gap). Quantitative thresholds missing.
  9. Whether observation parameters list is complete
     → 15 params (§8). No formal closure — list may expand.

🔴 STILL OPEN:

  5. Cultural specificity beyond amplification
     WHERE culture acts identified — cross-cultural data lacking
  6. Precise boundary L0 reflex vs L1 processing
     Timescale known (ms vs 100ms) — transition mechanism = open
  8. Protect parameter: hormone vs chunk contribution ratio
     Position: vasopressin SET bias, chunks DETERMINE expression — exact ratio unknown

🟡 NEW QUESTIONS (post-drill):

  11. Entity-Compiled capacity: can chunk capacity expand with training?
      Dunbar ceiling (3 mechanisms) suggests NO — but training can increase EFFICIENCY
  12. Hardware-Subsidy: precise oxytocin→VTA habituation mechanism?
      Position described, molecular pathway detail = open
  13. Compiled Quality: can threat-compiled be re-tagged?
      PFC-Operations suggests 6-step reversal pathway — empirical validation needed
```

### §12.4 Number Convention

```
🟡 SỐ LIỆU TRONG FRAMEWORK = CALIBRATION ANCHOR:

  Framework dùng con số để giúp ước lượng HƯỚNG + CỠ.
  KHÔNG phải đo lường chính xác. KHÔNG phải ratio cố định.

  QUY ƯỚC:
    ~X%     = order of magnitude ("roughly this scale")
    X-Y%    = range minh họa ("biến thiên lớn, nằm trong khoảng này")
    🟢 + %  = research-backed (có citation, empirical basis)
    🟡 + %  = framework estimate (calibration anchor, không có measurement basis)

  VÍ DỤ:
    "~95% vô thức / ~5% PFC"
      → INSIGHT: phần lớn processing KHÔNG cần PFC.
      → KHÔNG PHẢI: PFC chính xác chạy 5.0% thời gian.

    "7-layer fidelity: 100% → ... → 20-70%"
      → INSIGHT: fidelity GIẢM DẦN. Drop critical ở labeling + explanation.
      → KHÔNG PHẢI: Feel-Observation luôn chính xác 85% cho tất cả mọi người.

    "~90% Experience Compile / ~5% Expertise Compile"
      → INSIGHT: PHẦN LỚN behavior = direct compiled. Expertise = phần nhỏ.
      → KHÔNG PHẢI: chính xác 90.0% behavior là Experience Compile.

  → Đọc số trong framework = đọc HƯỚNG + CỠ, không đọc measurement.
```

---

## §13 — CROSS-REFERENCES

### §13.1 Bản đồ khác + Tương tác

```
  Core-Hardware.md              — CÁI GÌ ở ĐÂU: 4 zones A/B/C/D, PFC hardware specs, receptors
  Ask-AI.md v3.1                — TƯƠNG TÁC: AI generate dynamic interface per user (protocol + navigation)
```

### §13.2 Body-Base (foundation)

```
  Body-Base/Body-Base.md v3.2              — Entry point, Model 3+1, Compilable Architecture
  Body-Base/Why-Body-Knows.md v1.2         — TẠI SAO body check đáng tin
  Body-Base/Cortisol-Baseline.md v2.1      — Amplifier, direction gate, 7 modes, HPA paradox
  Body-Base/Valence-Propagation.md v3.0    — Structural/Current, 3 Firing Modes, Hardware-Subsidy
  Body-Base/Body-Coupling.md v3.0          — HOW body couples with entity, 4 bond types
  Body-Base/Inter-Body-Mechanism.md v1.1   — Source-of-truth: 8 inter-body principles
```

### §13.3 Chunk system

```
  Chunk/Chunk.md v2.3                      — Chunk substrate, trust gate, pattern hierarchy
  Chunk/Compile-Taxonomy.md v2.0           — 3 Compile Types, 4 pathways, 6 trade-offs
  Chunk/Background-Pattern.md v2.0         — Accumulated chunk bias invisible to PFC
```

### §13.4 Agent-Mechanism (11 files)

```
  Agent-Mechanism/Agent-Mechanism.md v2.1      — Integration hub, Compilable Architecture
  Agent-Mechanism/Self-Pattern-Modeling.md v3.1 — 1 mech × 3 dims, Compiled/Fresh, Simulation-Engine-APPLICATION-1
  Agent-Mechanism/By-Product-Gap-Resonance.md v1.4 — Mutual match, 4 conditions, Resonance Decline
  Agent-Mechanism/Entity-Compiled.md v1.0       — Hub-and-spoke, 40→200h, Dunbar, grief
  Agent-Mechanism/Entity-Access.md v1.2         — Gradient Mức 0-5, 3-Factor Model
  Agent-Mechanism/Entity-Access-Excess.md v1.0  — Excess territory, addiction spectrum
  Agent-Mechanism/Entity-Access-Calibration.md v1.0 — 3-Layer self-regulation
  Agent-Mechanism/Bond-Architecture.md v2.0     — 1 mech × 4 bonds, gap clone impossible
  Agent-Mechanism/Resonance-Sustainability.md v1.0 — 4-Layer, 3 conditions, 3 modalities
  Agent-Mechanism/By-Product-Scale.md v1.0      — 1 mech × 3 scales (Pair/Hub/Institutional)
  Agent-Mechanism/Resonance-Per-Entity.md v1.0  — Per-relationship dynamics, Hardware-Subsidy spectrum
```

### §13.5 Body-Feedback (10+ files)

```
  Body-Feedback/Body-Feedback.md               — Dual-Pull, Body-Feedback-Precondition, Interface Loop
  Body-Feedback/Body-Feedback-Precondition.md v1.0 — 5 preconditions for signal fire
  Body-Feedback/Body-Feedback-Mechanism.md v2.0 — 4th axis, chunk dynamics, Body-Need
  Body-Feedback/Body-Feedback-Label.md v2.0     — Vocabulary reference, 3-tier labels
  Body-Feedback/Gap-Direction.md v2.0           — Gap = f(surrounding chunks)
  Body-Feedback/Gap-Distribution-Profile.md v1.1— Per-person gap landscape
  Body-Feedback/Gap-Body-Need.md v1.0           — 3 Satiation Types, ENGINE/ROAD/VEHICLE
  Body-Feedback/Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State, E₀→E₃
  Body-Feedback/Reward-Calibration.md v1.1      — Goldilocks per-gap, over-reward
  Body-Feedback/Hidden-Quality-Perception.md v1.0 — "Mặt lưng cái tủ"
  Body-Feedback/Action-Space.md v1.0            — Supply-side capability landscape
```

### §13.6 Feeling

```
  Feeling/Feeling.md v3.0                  — PFC observation interface, 7-layer, PFC=Lawyer
  Feeling/Feeling-Research.md              — 7+ research stream foundation
  Feeling/Feeling-Mechanism-Deep-Draft.md  — HOW body signals → felt experience end-to-end
```

### §13.7 PFC

```
  PFC/PFC-Function.md v1.2                — 24 functions × 5 categories
  PFC/PFC-Hardware.md v1.1                — 4 receptor systems, COMT/DRD4
  PFC/PFC-Configuration.md v1.1           — 6 dynamic modes, PTSD, ADHD
  PFC/PFC-Operations.md v1.0              — Hold/Suppress, Budget, Compiled Quality
  PFC/PFC-Label.md v1.0                   — Vocabulary reference, 13 domains
  PFC/Simulation-Engine.md v1.0           — 1 engine, 3 components, 3 axes, N apps
  PFC/Logic-Feeling.md v4.0               — Body-Knowing + Compiled/Fresh spectrum, observer labels
  PFC/Logic-Feeling-Balance.md v1.0       — Meta-principle: domain feedback = only arbiter
  PFC/Imagination/Imagine-Final.md v3.0   — Constructive simulation, boundary reframe
  PFC/Imagination/Imagination.md v2.0     — Process file, 5 modalities, cortisol×modes
```

### §13.8 Observation files

```
  Observation/Novelty.md v1.2              — Positive prediction-delta, DRD4
  Observation/Threat.md v1.2               — Dissonance from predicted harm
  Observation/Boredom.md v2.0              — Unified formula, 6 sources, Resonance Decline
  Observation/Drive.md v1.2                — Integration: HOW drives combine
  Observation/Empathy.md v4.0              — Self-Pattern-Modeling applied, PFC budget, 4-Layer
  Observation/Connection.md v5.0           — 3 Generative Primitives, Entity-Access, Hardware-Subsidy
  Observation/Status.md v2.0               — Resource Access Map, multi-dimensional
  Observation/Protect.md v1.0              — Loss aversion + ownership
  Observation/Meaning.md v2.0              — Life-level Anchor-Schema, 5 types
  Observation/Gratitude.md v1.1            — Tầng 5, 9 prerequisites
  Observation/Obligation.md v1.0           — Access cost, 6 types, tiền = technology
  Observation/Liking-Wanting.md v2.0       — Bridge Berridge→framework
  Observation/AI-Schema-Detection.md v2.0  — Gateway: 9 AI capabilities, self-drill
```

### §13.9 Domain

```
  Domain/Domain.md v2.0                    — 3 Types, Dual Check, 3 Nguồn Constraint
  Domain/Conflict-Dynamics.md v2.0         — OVERLAP × SCARCITY × COMMITMENT
  Domain/Drill-Emergent-Pattern.md v2.0    — Enemy, Nurturing, Violation
  Domain/Domain-Mapping-Drive.md v2.0      — WHY humans drive to map domain
```

### §13.10 Collective

```
  Collective/Collective.md v1.0            — Integration hub, 5 con đường
  Collective/Collective-Body.md v2.1       — Model 3 cấp, trust = only bridge
  Collective/Coordination-Node.md v1.2     — Prestige vs Dominance, Mẹ = first node
  Collective/Collective-Arc-Dynamics.md v1.2 — Shelf-life × constraint source
  Collective/Collective-Purpose.md v1.2    — Cosmic loop, humanity maps domain
  Collective/Compliance-Floor.md v2.1      — Luật tối thiểu
```

### §13.11 Schema + Melody + Evidence

```
  Schema/Schema.md v2.0                    — Observation parameter reframe
  Schema/Anchor-Schema.md                  — Sync point, 4 nguồn fill
  Melody Lens/Personal-Melody.md v2.0      — Metaphor: mỗi người = 1 bài nhạc
  Body-Base-Example.md                     — 50 extreme cases
  Body-Input-Enumeration.md               — 17 body-inputs, delta rule, 15/15 tests
```

### §13.12 Application files

```
  AI-Schema-Detection.md v2.0              — Gateway: self-drill, AI guardrails
  AI-Self-Model.md v2.0                    — Dual Check, stale calibration
  Ask-AI.md v3.1                           — Dual Check protocol (body + domain)
  Research/Education/                      — 5 education files
  Research/Child-Development/              — 4 child development files
```

### §13.13 Superseded files

```
  Core-v7.8-Draft.md v0.2                  → backup (_backup/Core-v7.8-Draft-pre-3maps.md)
  Core-v7.5-Draft.md                       → backup (layer-based architecture)
  Core-Software.md v1.0                    → backup/Core-Software-v1.0-backup.md
```

---

## Closing note

**Core-Software v2.2** — 1 trong 2 bản đồ Core v7.8.

Bản đồ phần mềm mô tả CHI TIẾT NHẤT cách body-brain system HOẠT ĐỘNG.
Cycle-based architecture emerge từ 35,000+ dòng phân tích chuyên sâu (130+ files, 500+ citations).
v2.0 tích hợp 14 concept mới từ 28-session drill + 6-session foundation rewrite:
Simulation-Engine, Entity-Compiled, Entity-Access, Bond-Architecture, Hardware-Subsidy,
3 Satiation Types, PFC-Operations, Compiled Quality, Resonance Decline, By-Product-Scale,
Resonance-Sustainability, Phantom 4-factor, Domain Types, Evaluative/Direct-State.

Muốn biết CÁI GÌ ở ĐÂU → Core-Hardware.md.
Muốn TƯƠNG TÁC với framework → Ask-AI.md (AI generate dynamic interface per user).

> *Core-Software v2.0 — "Perception-Action Cycle: Domain → Body-Input → Unconscious(Chunks) →
> Feeling → PFC → Body-Output → Domain. Chunks = sole substrate. Simulation-Engine = 1 engine,
> N applications (Self-Pattern-Modeling, Imagine-Final, Self-Observation). Body-Feedback = Evaluative
> reward (opioid, Body-Feedback-Precondition) + Direct-State reward (non-opioid, burnout-proof) + Dissonance.
> PFC = observer + orchestrator (Hold/Suppress, Budget, Compiled Quality).
> Entity-Compiled = structural body-base integration. Entity-Access Mức 0-5.
> Bond-Architecture = 1 mechanism × 4 bonds. Hardware-Subsidy per entity.
> 3 Satiation Types. Resonance Decline. Schema, Drives = observation parameters.
> Development = chunk density. 3 Domain Types + Dual Check.
> Model 3+1. Cấp 1 Individual, Cấp 2 Collective. Trust = only bridge.
> 20 key reframes. Framework iterates."*
