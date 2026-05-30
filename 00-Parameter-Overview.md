# Framework Parameter Overview — Kiến Trúc Tham Số Tổng Thể

> **Trạng thái:** v1.0 — 2026-05-27
> **Mục đích:** Bản đồ tham số quan sát + mechanism tổng thể. Lướt nhanh → nắm toàn cảnh hệ thống.
> **Nguyên tắc:** Tên tham số + file .md + giải thích 1 dòng. KHÔNG giải thích mechanism chi tiết.
> **Bản đồ khác:** Core-Hardware.md (vật lý) | Core-Software.md (cycle) | Ask-AI.md (tương tác)

---

## CYCLE CỐT LÕI

```
Domain → Body-Input → Unconscious Processing → Feeling → PFC → Body-Output → Domain
                              (lặp liên tục, ms → decades đồng thời)
```

---

## I. BODY-BASE — Nền Tảng (mọi thứ chạy trên đây)

Entry: Body-Base.md

### 1. Chunk System — Substrate duy nhất

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Chunk | Chunk/Chunk.md | Đơn vị nền tảng duy nhất. Mọi thứ — schema, feeling, drive — đều chạy trên chunks |
| Compile-Taxonomy | Chunk/Compile-Taxonomy.md | 3 loại compile: Experience (trải nghiệm trực tiếp) / Expertise (luyện tập) / Trust (tin và nhận) |
| Background-Pattern | Chunk/Background-Pattern.md | Tổng compiled bias tích lũy — vô hình với PFC nhưng chi phối hành vi |

### 2. Body-Feedback System — Cách body phát tín hiệu

Entry: Body-Feedback/Body-Feedback.md

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Body-Feedback | Body-Feedback/Body-Feedback.md | Hệ thống tín hiệu body → PFC. Dual-Pull + Body-Feedback-Precondition 5 preconditions + Interface Loop 6-step |
| Body-Feedback-Mechanism | Body-Feedback/Body-Feedback-Mechanism.md | 4th axis phân loại: chunk dynamics. Body-Need = 2 nguồn (hardware + chunk dynamics) |
| Body-Feedback-Label | Body-Feedback/Body-Feedback-Label.md | VOCABULARY 100% framework. 3-tier label (General→Direction→Specific). MUST-READ |
| Reward-Signal-Architecture | Body-Feedback/Reward-Signal-Architecture.md | 2 loại reward: Evaluative (opioid, có điều kiện) vs Direct-State (non-opioid, hardware trực tiếp) |
| Dissonance-Signal-Architecture | Body-Feedback/Dissonance-Signal-Architecture.md | Counterpart: 2 loại dissonance. Evaluative (PFC modulate được) vs Direct-State (numbness-proof) |
| Reward-Calibration | Body-Feedback/Reward-Calibration.md | BAO NHIÊU reward là ENOUGH? Goldilocks per-gap. Over-reward → 6 cơ chế hại |

### 3. Gap System — Hệ thống khoảng trống

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Gap-Direction | Body-Feedback/Gap-Direction.md | Gap = f(surrounding chunks). "Chưa biết = không có gap" — không có chunks xung quanh thì không có gap |
| Gap-Distribution-Profile | Body-Feedback/Gap-Distribution-Profile.md | Bản đồ gap của MỖI NGƯỜI (demand side). 4 trục: Center × Origin × Depth × Stability |
| Gap-Body-Need | Body-Feedback/Gap-Body-Need.md | Per-gap dynamics: 3 Satiation (Cyclic/Tonic/Generative). ENGINE/ROAD/VEHICLE architecture |
| Action-Space | Body-Feedback/Action-Space.md | Bản đồ khả năng của mỗi người (supply side). Behavior = Gap-Distribution-Profile × Action-Space |
| Hidden-Quality-Perception | Body-Feedback/Hidden-Quality-Perception.md | "Mặt lưng cái tủ." Chưa compile chunks về quality X → không có gap về X → body im lặng |

### 4. Valence — Hệ thống giá trị cảm xúc

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Valence-Propagation | Body-Base/Valence-Propagation.md | Valence definition + 4 nguồn + 4 cơ chế propagation + PFC Blindness. Companion: Entity-Valence-Dynamics.md |
| Entity-Valence-Dynamics | Body-Base/Entity-Valence-Dynamics.md | Structural vs Current. 3 Firing Modes. Hardware-Subsidy. Per-entity dynamics. Phantom resonance |

### 5. Cortisol — Amplifier

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Cortisol-Baseline | Body-Base/Cortisol-Baseline.md | Cortisol = amplifier thay đổi, KHÔNG phải nguyên nhân đau. Direction > Level. 7 modes |

### 6. Body-Coupling — Body↔Entity

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Body-Coupling | Body-Base/Body-Coupling.md | HOW body gắn kết sâu với entity khác. 2D: Depth × Direction. 4 bond types × Hardware-Subsidy |

### 7. Agent-Mechanism — Hệ thống mô hình hóa agent

Entry: Chunk/Agent-Mechanism/Agent-Mechanism.md
Phân biệt: Agent = ENTITY (đối tượng), Agent-Mechanism = FUNCTION (cơ chế)

#### 7a. Core Modeling — Cách não xây mô hình về agent

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Self-Pattern-Modeling | Agent-Mechanism/Self-Pattern-Modeling.md | 1 cơ chế × 3 chiều (Processing × Valence × Output). Não dùng chunks của MÌNH để mô phỏng NGƯỜI KHÁC |
| Entity-Compiled | Agent-Mechanism/Entity-Compiled.md | Não compile agent vào body-base ở structural level. Hub-and-spoke. Formation 40→200h. Dunbar ceiling |
| Entity-Access | Agent-Mechanism/Entity-Access.md | Gradient Mức 0-5: não xây predictive access-relationship với entity để fill gaps |
| Entity-Access-Excess | Agent-Mechanism/Entity-Access-Excess.md | Mức 5 = entity gần như DUY NHẤT gap source. Cùng circuits với drug addiction |
| Entity-Access-Calibration | Agent-Mechanism/Entity-Access-Calibration.md | HOW entity-access tự điều chỉnh. 3-Layer. Exit Cost = Signal Weight |

#### 7b. Resonance System — Cơ chế tương tác giữa các body

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| By-Product-Gap-Resonance | Agent-Mechanism/By-Product-Gap-Resonance.md | Core: resonance = by-product match ở OUTPUT. 4 conditions đồng thời. Gap clone IMPOSSIBLE |
| Bond-Architecture | Agent-Mechanism/Bond-Architecture.md | 1 cơ chế × 4 bond types (parent/friend/romantic/professional). Resonance Decline decline mechanisms |
| Resonance-Sustainability | Agent-Mechanism/Resonance-Sustainability.md | 4-Layer sustainability. 3 conditions + 3 modalities + amplification + trajectory |
| Resonance-Per-Entity | Agent-Mechanism/Resonance-Per-Entity.md | Cùng cơ chế, KHÁC dynamics per relationship. Hardware-Subsidy: MAX→NONE. Lifecycle 6 phases |
| By-Product-Scale | Agent-Mechanism/By-Product-Scale.md | 1 cơ chế × 3 scales: Pair / Hub / Institutional. Prestige = genuine resonance |

### 8. Schema — Observation label

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Schema | Schema/Schema.md | Named chunk-network pattern = cách mô tả từ BÊN NGOÀI. Body chạy chunks, KHÔNG chạy schemas |
| Anchor-Schema | Schema/Anchor-Schema.md | Sync point cho toàn hệ thống. 4 nguồn fill. Thiếu anchor → "chán / lost" |

### 9. Melody Lens — Hệ thống metaphor

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Personal-Melody | Melody Lens/Personal-Melody.md | Mỗi người = 1 bài nhạc = emergent state toàn bộ chunks đang chạy đồng thời |
| Melody-Arc | Melody Lens/Melody-Arc.md | Chu kỳ build: dissonance → compile → melody upgrade |
| Global-Melody | Melody Lens/Global-Melody.md | Melodies tương tác ở collective scale: gia đình → văn hóa → toàn cầu |

### 10. Supporting

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Why-Body-Knows | Body-Base/Why-Body-Knows.md | Meta-question: TẠI SAO body đáng tin? 2-tier calibration |
| Inter-Body-Mechanism | Body-Base/Inter-Body-Mechanism.md | 8 nguyên tắc kiến trúc inter-body. Source-of-truth |
| Neural-Architecture | Core-Deep-Dive/Neural-Architecture.md | 4 zones A/B/C/D. Bản đồ sinh lý chi tiết |
| Neural-Processing-Flow | Core-Deep-Dive/Neural-Processing-Flow.md | Con đường vật lý tín hiệu: Sensor → Thalamus → Cortex → PFC → Output → Feedback |
| Modality | Core-Deep-Dive/Modality.md | 6 kênh encoding (Visual/Auditory/Somatic/Motor/Emotional/Communication) |

---

## II. PFC — Observer + Orchestrator

### 1. PFC Core

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| PFC-Function | PFC/PFC-Function.md | 24 functions × 5 categories. ~95% compiled, ~5% active PFC |
| PFC-Hardware | PFC/PFC-Hardware.md | 4 receptor systems (COMT/DRD4/serotonin/GABA). Giải thích TẠI SAO cùng 24 functions mà output khác |
| PFC-Configuration | PFC/PFC-Configuration.md | 6 dynamic modes. PFC switch giữa các modes tùy context |
| PFC-Operations | PFC/PFC-Operations.md | 2 operations (Hold + Suppress). PFC Budget = shared resource. Compiled Quality (genuine/schema/threat) |
| PFC-Development | PFC/PFC-Development.md | Trajectory: Worker→Director→Monitor→Compiled. "Trẻ chưa có PFC" = SAI — đúng là chưa có chunks |
| PFC-Hold-Dimensions | PFC/PFC-Hold-Dimensions.md | WHY ~4±1: 6 lực độc lập hội tụ cùng trỏ về ~4 dimensions đồng thời |
| PFC-Label | PFC/PFC-Label.md | VOCABULARY REFERENCE. 13 domain. Companion với Body-Feedback-Label.md |
| Attention-Spectrum | PFC/Attention-Spectrum.md | Phổ chú ý multi-factor. Inverted-U model |

### 2. Simulation-Engine — Engine tổng quát của PFC

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Simulation-Engine | PFC/Simulation-Engine.md | 1 engine (DMN+mPFC+insula+hippocampus), 3 components, 3 axes → N applications. Luyện 1 → improve tất cả |

### 3. Feeling — Bridge Body↔PFC

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Feeling | Feeling/Feeling.md | PFC observation of body-chunk interaction. HỆ THỐNG phản hồi unified, KHÔNG chỉ "emotion" |
| Body-Knowing | Feeling/Body-Knowing.md | Compiled chunks + body signal → "biết mà không cần giải thích." Function CỦA Feeling system |

### 4. Logic-Feeling — Observer Labels

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Logic-Feeling | PFC/Logic-Feeling.md | "Logic" vs "Feeling" = CÙNG mechanism, khác SHAREABILITY (chia sẻ được = "logic") |
| Logic-Feeling-Balance | PFC/Logic-Feeling-Balance.md | META: Cả Logic lẫn Feeling đều KHÔNG 100% chính xác. Domain feedback = trọng tài duy nhất |
| Logic-Planning | PFC/Logic-Planning.md | Chain labeled chunks → plan → action. AI mạnh ở đây → framework focus Feeling side |

### 5. Imagination — Future Simulation

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Imagination | Imagination/Imagination.md | Process + overview. 5 modalities. Cortisol fidelity (40-70%) > opioid (20-40%) → worry dễ hơn visualization |
| Imagine-Final | Imagination/Imagine-Final.md | Constructive future simulation. KHÔNG phải mọi body prediction — CHỈ constructive (chunk-based). 5 levels |
| Imagine-Final-Evaluation | Imagination/Imagine-Final-Evaluation.md | Đánh giá Imagine-Final: 2 trục (Domain Fit × Hardware Fit) + Trust = 3D framework |
| Somatic-Articulation-Loop | Imagination/Somatic-Articulation-Loop.md | Body-knowledge → explicit-knowledge: loop recursive. AI = catalyst giúp PFC tìm từ nhanh hơn |

---

## III. OBSERVATION PARAMETERS — Tham Số Quan Sát

Nguồn chính thức: Core-Software.md §8 (15 params)
Observation parameters = named patterns, KHÔNG phải mechanism. Hữu ích để mô tả, predict, communicate.
Tất cả files tại: Core-Deep-Dive/Observation/

### A. Cross-species — Bản năng (động vật cũng có ở dạng đơn giản hơn)

| # | Parameter | File | Ý nghĩa |
|---|-----------|------|---------|
| 1 | **Novelty** | Novelty.md | Positive prediction-delta: "CÁI MỚI → VTA fire." 2 dạng: Sensory-Driven / Imagination-Driven. DRD4 depth vs breadth |
| 2 | **Threat** | Threat.md | Dissonance from predicted harm. 5 mức × 3 trục. Modern = anticipation-dominant (không có endorphin buffer) |
| 3 | **Boredom** | Boredom.md | "Chán" = Dissonance + Imagine-Final mờ. 6 nguồn. "Chán nhau" = by-product match dừng (source ⑥) |
| 4 | **Drive** | Drive.md | INTEGRATION: Novelty + Threat + Boredom combine → energy + direction → action tại mỗi thời điểm |
| 5 | **Status** | Status.md | Resource Access Map. Evolutionary: resource access = body-base reward THẬT. Spectrum: hổ→khỉ→người |
| 6 | **Protect** | Protect.md | Loss aversion + ownership. f(replaceability × attachment). Spectrum: vật → người → ý tưởng → identity |
| 7 | **Connection** | Connection.md | 3 Generative Primitives (❶Hardware × ❷Self-Pattern-Modeling × ❸Valence). 8 pathways. "Cô đơn" = dissonance |
| 8 | **Autonomy** | Autonomy.md + Autonomy-Hardware.md | "Tôi quyết định → kết quả tôi muốn." Hardware: efference copy (universal). Software: meta-chunk compile (per-person) |
| 9 | **Disgust** | *(Core-Software.md §8)* | Rejection threshold. Hardware: innate. WHAT triggers: heavily learned (cultural). Chưa có file riêng |

### B. Human-specific — Luyện tập (cần chunk compilation depth)

| # | Parameter | File | Ý nghĩa |
|---|-----------|------|---------|
| 10 | **Empathy** | Empathy.md | Self-Pattern-Modeling applied → quan sát "hiểu người khác." PFC budget, per-entity, burnout = compiled suppress |
| 11 | **Obligation** | Obligation.md | Compiled prediction về cost liên tục để MAINTAIN access. 6 types. Tiền = obligation technology |
| 12 | **Gratitude** | Gratitude.md | Tầng 5 (cao nhất). 9 prerequisites đồng thời. Agent-entity only. 3 anti-habituation. Hiếm vì khó |
| 13 | **Meaning** | Meaning.md | Có/thiếu life-level Anchor-Schema ổn định. 5 types (GOAL/STATE/IDENTITY/FAITH/ROLE). Mỗi người KHÁC |
| 14 | **Mastery** | *(Core-Software.md §8)* | Domain chunk accumulation + sustained delta. Generative gap: fill → expand → new gap. Chưa có file riêng |

### C. Emergent — Meta-level

| # | Parameter | File | Ý nghĩa |
|---|-----------|------|---------|
| 15 | **Melody** | Melody Lens/ folder | Emergent state tổng hợp toàn bộ systems đang chạy đồng thời |
| 16 | **Passion** | *(Core-Software.md §8)* | Khi hardware pull + domain pull ALIGN (rare, quý). Gap-Distribution-Profile alignment indicator |
| 17 | **Schema** | Schema/Schema.md | Named chunk-network pattern — observation label, KHÔNG phải component |

### Bridge/Tool — Nằm trong Observation/ nhưng không phải observation parameter

| File | Ý nghĩa |
|------|---------|
| Liking-Wanting.md | Bridge Berridge→framework. "Wanting" = 6 mechanisms. "Liking" = reward CÓ ĐIỀU KIỆN |
| AI-Schema-Detection.md | Gateway thực hành: 3-tầng model (AI detect → Chuyên gia feel-check → Client self-verify) |

---

## IV. DOMAIN — Thực Tại Bên Ngoài

Entry: Domain/Domain.md

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Domain | Domain/Domain.md | 3 types: Reality / Abstract / Abstract-Dynamic. Dual Check: body = quality controller, domain = final arbiter |
| Conflict-Dynamics | Domain/Conflict-Dynamics.md | Conflict = Overlap × Scarcity × Commitment |
| Discovery-vs-Expansion | Domain/Discovery-vs-Expansion.md | 3 điểm trên phổ progress: Sense → Verify → Scale |
| Knowledge-Flow | Domain/Knowledge-Flow.md | Dòng chảy xuyên thế hệ: internal → output → external chunk |
| Domain-Mapping-Drive | Domain/Domain-Mapping-Drive.md | WHY con người drive map domain dù "có sẵn": prediction-delta + opioid per step |

---

## V. COLLECTIVE — Hệ Thống Tập Thể

Entry: Collective/Collective.md

| Tham số | File | Ý nghĩa |
|---------|------|---------|
| Collective | Collective/Collective.md | Emergent infrastructure. 5 con đường collective ảnh hưởng cá nhân |
| Collective-Body | Collective/Collective-Body.md | Model 3 cấp (Individual → Collective → Framework). Trust = bridge duy nhất |
| Coordination-Node | Collective/Coordination-Node.md | Resource allocation position. Dominance (relief) vs Prestige (genuine resonance) |
| Collective-Arc-Dynamics | Collective/Collective-Arc-Dynamics.md | TẠI SAO compiled patterns có shelf-life khác nhau. Dependency ratio → shift speed |
| Collective-Purpose | Collective/Collective-Purpose.md | Meta: humanity collective map domain reality. Cosmic loop |
| Compliance-Floor | Collective/Compliance-Floor.md | Luật tối thiểu để melodies không phá nhau. Tự do = default, luật = ngoại lệ |

---

## VI. BRIDGES — Liên Kết Giữa Các Hệ Thống

| Bridge | Mechanism | Key concept |
|--------|-----------|-------------|
| Body↔Collective | By-Product-Gap-Resonance + By-Product-Scale | ENGINE/ROAD/VEHICLE (Hardware / Collective / Compilation) |
| Body↔PFC | Feeling = PFC observation interface | Body-Knowing = compiled recognition. Somatic-Articulation-Loop = implicit → explicit |
| PFC↔Domain | Imagine-Final + Logic-Planning | Dual Check: body = quality controller, domain = final arbiter |
| PFC↔Entity | Simulation-Engine → Self-Pattern-Modeling | 1 engine → N applications (self/other/future) |
| Body↔Entity | Body-Coupling + Entity-Compiled | Hardware-Subsidy per bond type. Structural coupling ở body-base level |

---

## VII. CLARIFICATION — Sửa Hiểu Lầm Phổ Biến

Tại: Core-Deep-Dive/Clarification/

| File | Hiểu lầm → Sự thật |
|------|---------------------|
| Dopamine-Is-Not-Reward.md | Dopamine = salience signal ("chuông cửa"), KHÔNG phải reward ("quà") |
| Prediction-Error-Is-Not-Reward.md | Prediction-error cần + Coherence + Body-Feedback-Precondition preconditions mới = reward |
| Mirror-Neuron-Rejection.md | Không có hardware mirror module bẩm sinh. Empathy = Self-Pattern-Modeling learned function |
| Cortisol-Amplifier-Not-Cause.md | Cortisol ≠ "stress hormone." Key = REPAIR, không phải cortisol level |

---

## VIII. BLACKBOX — Vùng Chưa Biết

| File | Ý nghĩa |
|------|---------|
| Core-Deep-Dive/Blackbox-Map.md | 5-Layer Gap Analysis. GAP lớn nhất: Signal Transduction "Driver Layer" (molecular biology giữa receptor → chunk) |

---

## IX. RESEARCH & APPLICATIONS — Ứng Dụng Framework

Các file này DÙNG observation parameters để phân tích, KHÔNG thêm mechanism mới.

| Folder | Nội dung chính |
|--------|----------------|
| Research/Love-Romantic.md | Test case cho toàn bộ framework: romantic love |
| Research/Love-Unified.md | "Tình yêu" mọi dạng = Entity-Compiled compile đủ sâu |
| Research/Money-Analysis.md | Tiền = proxy token + obligation technology + shared chunk prediction |
| Research/Self-Created-Threat.md | Trust Compile PFC→body. 4 loại self-created threat |
| Research/Health-Conditions/ | Addiction, Nicotine, Alcohol, OCD, PTSD, ADHD, Autism, Parkinson, Alzheimer |
| Research/Global/ | Human-AI-Future, AI-Self-Model, Social-Calibration, Uncanny-Valley, Birth-Rate-Decline |
| Research/Melody-Technology/ | Religion (7/7 functions), Idol-Phenomenon |
| Research/Human-Learning/ | Child-Development (0-6), Education-Mechanism, Money-Education |
| Research/Meta-Impact/ | Framework predict tác động CỦA CHÍNH NÓ |
| Applications/Education-System/ | Ứng dụng vào hệ thống giáo dục |

---

## GHI CHÚ

- Tất cả paths tương đối từ Core-Deep-Dive/ (trừ khi ghi rõ)
- Observation parameters = named patterns, KHÔNG phải mechanism. Dùng để mô tả + predict. Can thiệp → phải ở level mechanism
- Framework v7.8: Chunk-System = sole substrate. Schema, Drive, Valence = observation parameters
- 3 file chưa có file riêng: Disgust, Mastery, Passion (chỉ có trong Core-Software.md §8)
- Empathy có file riêng trong Observation/ nhưng KHÔNG nằm trong danh sách §8 — có thể coi là application của Self-Pattern-Modeling
- Cross-species: ở động vật hormone → behavior trực tiếp. Ở người: hormone → chunk processing → behavior
