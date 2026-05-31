---
title: Reading Roadmap — Tiến Trình Đọc Toàn Diện
version: 1.0
created: 2026-05-31
status: v1.0
scope: |
  Tiến trình đọc cho người muốn hiểu TOÀN DIỆN framework.
  Foundation → Individual Mechanisms → Entity System → Observable Patterns → Collective → Domain.
  Core path: 55 files, ~85,700 dòng.
  + Enrichment: 20 files, ~30,700 dòng.
  + Reference: 22 files, ~17,200 dòng.
purpose: |
  README.md + Ask-AI.md §0.1 cho SETUP TỐI THIỂU (8 files).
  File NÀY cho TIẾN TRÌNH ĐỌC nếu muốn đi sâu hơn.
  Mỗi Tier = 1 mức hiểu. Đọc tới đâu, hiểu tới đó.
  Không bắt buộc đọc hết — chọn Tier phù hợp mục tiêu.
position: |
  Root level — cùng vị trí với README.md, Ask-AI.md.
  README.md = getting started.
  Ask-AI.md = AI interaction protocol.
  Reading-Roadmap.md (FILE NÀY) = reading progression.
  Core-Deep-Dive/01-File-Index.md = flat file list (AI-readable lookup).
dependencies:
  - README.md — starter prompt references 8 must-read files
  - Ask-AI.md v3.2 — §0.1 Setup references 8 must-read files
  - Core-Deep-Dive/01-File-Index.md — flat file list
language: Tiếng Việt primary + English technical terms
---

# Reading Roadmap — Tiến Trình Đọc Toàn Diện

> **3 trụ cột:**
> 1. **Cá nhân** (Individual) — body-brain system hoạt động thế nào
> 2. **Tập thể** (Collective) — nhóm hình thành và vận hành thế nào
> 3. **Domain** (External Reality) — thực tế bên ngoài mà loài người vươn tới
>
> Mỗi Tier = 1 mức hiểu. Đọc tới đâu, hiểu tới đó.
> Không bắt buộc đọc hết — chọn Tier phù hợp mục tiêu.

---

## Tổng quan

| Tier | Theme | Files | Lines | Cộng dồn | Sau tier này, bạn hiểu... |
|------|-------|-------|-------|----------|--------------------------|
| 0 | Foundation | 8 | ~11,700 | ~11,700 | Core architecture — đủ để dùng AI |
| 1 | Mechanism | 14 | ~22,900 | ~34,600 | HOW từng component hoạt động |
| 2 | Entity | 8 | ~12,600 | ~47,200 | HOW não model entities và xây quan hệ |
| 3 | Observation | 13 | ~23,300 | ~70,500 | WHAT patterns hành vi quan sát được |
| 4 | Collective | 6 | ~7,800 | ~78,300 | HOW nhóm emerge và function |
| 5 | Domain | 6 | ~7,400 | ~85,700 | WHAT thực tế bên ngoài human |

```
PILLAR 1: CÁ NHÂN
  Tier 0 (Foundation) → Tier 1 (Mechanism)
                                 ↓
BRIDGE                       Tier 2 (Entity) → Tier 3 (Observation)
                                                      ↓
PILLAR 2: TẬP THỂ                                Tier 4 (Collective)

PILLAR 3: DOMAIN                                  Tier 5 (Domain)
```

> **Note:** Paths bắt đầu từ Core-Deep-Dive/ trừ khi ghi khác.
> Root-level files: Core-Software.md, Ask-AI.md.

---

## TIER 0 — FOUNDATION (8 files, ~11,700L)

*Minimum cho AI interaction. Chi tiết setup: Ask-AI.md §0.1.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| ① | Body-Base/Body-Base.md | 1,484 | Body-base FOUNDATION: 3 Hardware, Compiled/Fresh |
| ② | Core-Software.md *(root)* | 1,764 | Cycle ARCHITECTURE: chunk system, observation params |
| ③ | Body-Base/Chunk/Chunk.md | 1,664 | Chunk SUBSTRATE: activation, compile, NO SOURCE TAG |
| ④ | Body-Base/Body-Feedback/Body-Feedback.md | 1,164 | Body signal SYNTHESIS: Dual-Pull, Interface Loop |
| ⑤ | Body-Base/Feeling/Feeling.md | 2,184 | Body signal OBSERVATION: 7-layer fidelity gradient |
| ⑥ | PFC/PFC-Operations.md | 1,134 | PFC MECHANISM: Hold/Suppress, Budget, 3-Cost |
| ⑦ | PFC/Logic-Feeling.md | 1,526 | Observer LABELS: Logic vs Feeling = same mechanism |
| ⑧ | Ask-AI.md *(root)* | 805 | Protocol + Danger Zones + Navigation |

Đọc: ① → ② → ③ → ④ → ⑤ → ⑥ → ⑦ → ⑧
(foundation → architecture → substrate → signals → observation → PFC → labels → protocol)

---

## TIER 1 — MECHANISM DEEP-DIVE (14 files, ~22,900L)

*HOW từng component hoạt động. 5 nhóm, đọc theo thứ tự nhóm.*

### 1A — Vocabulary + Reframe

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 1 | Body-Base/Schema/Schema.md | 832 | Schema = observation label, KHÔNG phải component |
| 2 | Body-Base/Body-Feedback/Body-Feedback-Label.md | 1,163 | Vocabulary standard: 3-tier label system |

### 1B — Chunk Deep-Dive

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 3 | Body-Base/Chunk/Compile-Taxonomy.md | 1,173 | 3 Compile Types (Experience/Expertise/Trust), 4 Pathways |
| 4 | Body-Base/Chunk/Background-Pattern.md | 2,521 | Invisible bias: 2D model (Depth × Density), Triple Bias |

### 1C — Body-Feedback Deep-Dive

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 5 | Body-Base/Body-Feedback/Body-Feedback-Mechanism.md | 1,534 | 2-source Body-Need + 4th axis phân loại |
| 6 | Body-Base/Body-Feedback/Gap-Direction.md | 2,715 | Gap = f(surrounding chunks), "chưa biết = không có gap" |
| 7 | Body-Base/Body-Feedback/Reward-Signal-Architecture.md | 2,016 | Evaluative vs Direct-State, E₀→E₃, 5 profiles |
| 8 | Body-Base/Body-Feedback/Dissonance-Signal-Architecture.md | 1,572 | Dissonance types, Evaluative gates Direct-State |

### 1D — PFC & Simulation

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 9 | PFC/PFC-Function.md | 568 | WHAT PFC does: 24 functions × 5 categories |
| 10 | PFC/Simulation-Engine.md | 977 | 1 engine, 3 components, 3 axes → 11+ applications |
| 11 | PFC/Imagination/Imagine-Final.md | 1,518 | Constructive simulation (≠ hardware prediction) |

### 1E — Feeling & Base Extensions

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 12 | Body-Base/Feeling/Body-Knowing.md | 2,042 | Compiled knowing: 3 directions = same mechanism |
| 13 | Body-Base/Valence-Propagation.md | 942 | 4 nguồn valence, 4 cơ chế propagation |
| 14 | Body-Base/Cortisol-Baseline.md | 3,340 | Cortisol = change-readiness amplifier (full mechanism) |

### Enrichment 1

*Đọc thêm nếu muốn sâu hơn — không bắt buộc cho Tier 2.*

| Path | Lines | Vai trò |
|------|-------|---------|
| Body-Feedback/Body-Feedback-Precondition.md | 1,422 | WHEN signal fires: 5 Preconditions |
| Body-Feedback/Gap-Body-Need.md | 1,403 | Per-gap dynamics, 3 Satiation Profiles |
| Body-Feedback/Gap-Distribution-Profile.md | 2,372 | Per-person gap landscape, ENGINE/ROAD/VEHICLE |
| Body-Feedback/Reward-Calibration.md | 1,356 | Goldilocks per-gap, 6 cơ chế over-reward |
| Body-Feedback/Action-Space.md | 1,729 | Supply-side capability, Behavior = f(GDP × AS) |
| Body-Feedback/Hidden-Quality-Perception.md | 1,738 | "Mặt lưng cái tủ" — quality invisible |
| Body-Base/Why-Body-Knows.md | 1,305 | Meta: tại sao body-check đáng tin? |
| Body-Base/Schema/Anchor-Schema.md | 1,880 | Sync point, 4 nguồn fill anchor |
| PFC/PFC-Hardware.md | 1,004 | 4 receptor systems (COMT/DRD4) |
| PFC/PFC-Configuration.md | 1,327 | 6 Configuration Modes |
| PFC/PFC-Development.md | 702 | Trajectory Worker → Director → Monitor → Compiled |
| PFC/Logic-Feeling-Balance.md | 1,631 | META-PRINCIPLE: neither logic nor feeling 100% accurate |
| PFC/Imagination/Somatic-Articulation-Loop.md | 2,844 | Body-knowledge → explicit-knowledge loop |
| PFC/Imagination/Imagination.md | 793 | Overview: 5 modalities × COMT/DRD4 |

---

## TIER 2 — ENTITY SYSTEM (8 files, ~12,600L)

*Bridge cá nhân → tập thể. Não model entities và xây quan hệ thế nào.*

### 2A — Foundation

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 1 | Body-Base/Inter-Body-Mechanism.md | 1,474 | 8 nguyên tắc SOURCE-OF-TRUTH inter-body |
| 2 | Body-Base/Chunk/Agent-Mechanism/Agent-Mechanism.md | 2,362 | Integration hub: entity mechanism overview |

### 2B — Core Models

*Đọc theo thứ tự — mỗi file builds on file trước.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 3 | Agent-Mechanism/Self-Pattern-Modeling.md | 1,532 | APPLICATION-1 on Simulation-Engine, 3 dimensions |
| 4 | Agent-Mechanism/Entity-Access.md | 1,468 | Gradient Mức 0-5, 3-Factor Model |
| 5 | Agent-Mechanism/Entity-Compiled.md | 1,231 | 40→200h, Dunbar, Hub-and-Spoke, Grief A+B+C |
| 6 | Agent-Mechanism/Bond-Architecture.md | 1,234 | Gap clone impossible, 1 mechanism × 4 bonds |
| 7 | Agent-Mechanism/By-Product-Gap-Resonance.md | 1,711 | Resonance core: 4 conditions đồng thời |
| 8 | Body-Base/Entity-Valence-Dynamics.md | 1,547 | Per-entity valence, 3 Firing Modes, Phantom |

### Enrichment 2

| Path | Lines | Vai trò |
|------|-------|---------|
| Body-Base/Body-Coupling.md | 2,895 | HOW body couples with entity, 2D model |
| Agent-Mechanism/Resonance-Sustainability.md | 1,355 | 4-Layer sustainability, 3 conditions |
| Agent-Mechanism/By-Product-Scale.md | 903 | 1 mechanism × 3 scales (Pair/Hub/Institutional) |
| Agent-Mechanism/Resonance-Per-Entity.md | 1,629 | 5+ entity profiles, lifecycle shift |
| Agent-Mechanism/Entity-Access-Excess.md | 1,392 | Mức 5, cùng circuits với drug addiction |
| Agent-Mechanism/Entity-Access-Calibration.md | 1,073 | 3-Layer calibration, Exit Cost |

---

## TIER 3 — OBSERVABLE PATTERNS (13 files, ~23,300L)

*Observation parameters = TÊN GỌI cho patterns emerged từ nhiều hệ thống
tương tác — KHÔNG phải tính năng cố định của hardware.*
*Mỗi parameter overlap với nhiều parameter khác — ranh giới là mờ theo
thiết kế. Thứ tự đọc tối ưu hoá dependency, không phải phân loại.*

### 3A (5 files, ~5,100L)
*Đọc ngay sau Tier 0-2. Không cần observation parameters khác.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 1 | Observation/Novelty.md | 993 | VTA prediction-delta, DRD4 Depth vs Breadth |
| 2 | Observation/Threat.md | 1,073 | 5 mức × 3 trục, modern = anticipation-dominant |
| 3 | Observation/Autonomy-Hardware.md | 903 | Efference copy, vmPFC+DRN controllability |
| 4 | Observation/Drive.md | 776 | Integration: N+T → action, 6 PFC modes |
| 5 | Observation/Boredom.md | 1,324 | Unified formula, 6 nguồn dissonance |

### 3B (3 files, ~7,600L)
*Cần Tier 2 entity system. Đọc sau 3A.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 6 | Observation/Status.md | 2,470 | Resource Access Map, evolutionary grounded |
| 7 | Observation/Protect.md | 2,004 | f(replaceability × attachment), Vasopressin |
| 8 | Observation/Connection.md | 3,080 | 3 Generative Primitives, 8 pathways, 4-Layer |

### 3C (5 files, ~10,600L)
*Cần 3A + 3B. Build trên observation parameters trước.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 9 | Observation/Empathy.md | 2,903 | Self-Pattern-Modeling Compiled + ❸ positive |
| 10 | Observation/Meaning.md | 1,979 | Life-level Anchor-Schema, 5 types |
| 11 | Observation/Autonomy.md | 1,007 | Software: f(motor × controllability × meta-chunk) |
| 12 | Observation/Obligation.md | 2,554 | 6 types, tiền = obligation technology |
| 13 | Observation/Gratitude.md | 2,201 | Tầng 5, 9 prerequisites đồng thời |

*Note: Autonomy-Hardware (3A #3) và Autonomy (3C #11) là companion files.*

*3 observation parameters chưa có file riêng (chỉ mô tả trong Core-Software.md §8):
Disgust (rejection threshold), Mastery (sustained domain accumulation), Passion (hardware + domain pull align).*

### Enrichment 3

| Path | Lines | Vai trò |
|------|-------|---------|
| Observation/Liking-Wanting.md | 1,205 | Bridge: Berridge → framework (Wanting ≠ Liking) |
| Observation/AI-Schema-Detection.md | 1,749 | AI detection: 9 capabilities + Self-Drill |
| Observation/AI-Collective-Detection.md | 732 | Collective-level detection ⑩-⑭ |

---

## TIER 4 — COLLECTIVE (6 files, ~7,800L)

*Collective = emergent infrastructure, KHÔNG phải entity riêng.*
*Cần Tier 0-2 làm nền.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 1 | Collective/Collective.md | 813 | Hub: 5 con đường collective ảnh hưởng cá nhân |
| 2 | Collective/Collective-Body.md | 1,780 | Model 3 cấp, trust bridge, system compilation |
| 3 | Collective/Coordination-Node.md | 2,211 | Dominance vs Prestige, Mẹ = first node |
| 4 | Collective/Collective-Arc-Dynamics.md | 1,083 | 3 nguồn constraint, dependency ratio, shelf-life |
| 5 | Collective/Collective-Purpose.md | 1,114 | Cosmic loop, 3 forces, biological ceiling |
| 6 | Collective/Compliance-Floor.md | 819 | Tự do = default, 4 tầng nền |

---

## TIER 5 — DOMAIN (6 files, ~7,400L)

*Domain = thực tế bên ngoài, inferred through human interaction.*
*Cần Tier 0-2 làm nền.*

| # | Path | Lines | Vai trò |
|---|------|-------|---------|
| 1 | Domain/Domain.md | 716 | 3 Domain Types, Dual Check, 8 đặc điểm |
| 2 | Domain/Conflict-Dynamics.md | 635 | OVERLAP × SCARCITY × COMMITMENT |
| 3 | Domain/Discovery-vs-Expansion.md | 1,067 | Sense → Verify → Scale pipeline |
| 4 | Domain/Knowledge-Flow.md | 674 | Dòng chảy xuyên thế hệ |
| 5 | Domain/Domain-Mapping-Drive.md | 3,665 | WHY humans drive to map domain |
| 6 | Domain/Drill-Emergent-Pattern.md | 675 | Enemy, Nurturing, Giving, Violation patterns |

---

## BRIDGES — Liên Kết Giữa Các Hệ Thống

*5 cầu nối chính. Thứ tự theo tier mà reader gặp lần đầu.*

| Bridge | Mechanism | Key concept |
|--------|-----------|-------------|
| Body↔PFC | Feeling = PFC observation interface | Body-Knowing + Somatic-Articulation-Loop |
| PFC↔Domain | Imagine-Final + Logic-Planning | Dual Check: body = quality controller, domain = final arbiter |
| PFC↔Entity | Simulation-Engine → Self-Pattern-Modeling | 1 engine → N applications (self/other/future) |
| Body↔Entity | Body-Coupling + Entity-Compiled | Hardware-Subsidy per bond type |
| Body↔Collective | By-Product-Gap-Resonance + By-Product-Scale | ENGINE/ROAD/VEHICLE |

---

## REFERENCE — Đọc Bất Kỳ Lúc Nào

*Không thuộc tiến trình chính. Đọc khi cần hoặc khi tò mò.*

### Clarification — Framework ≠ Mainstream

| Path | Lines | Vai trò |
|------|-------|---------|
| Clarification/Dopamine-Is-Not-Reward.md | 864 | 7 bằng chứng + 7-step mechanism |
| Clarification/Cortisol-Amplifier-Not-Cause.md | 458 | Cortisol ≠ "stress hormone" (tóm tắt) |
| Clarification/Mirror-Neuron-Rejection.md | 463 | Không có mirror module bẩm sinh |
| Clarification/Prediction-Error-Is-Not-Reward.md | 596 | PE ≠ reward — insufficient cho humans |

### Hardware Reference

| Path | Lines | Vai trò |
|------|-------|---------|
| Core-Hardware.md *(root)* | 414 | Physical brain architecture overview |
| Neural-Architecture.md | 693 | 4 phân vùng neural |
| Neural-Processing-Flow.md | 1,270 | Full signal pathway: Sensor → Output |
| Modality.md | 752 | 6 kênh encoding (Visual/Auditory/Somatic/...) |
| Auditory-Hardware.md | 735 | DUY NHẤT arc compile trước sinh |

### Melody Lens — Metaphor Communication

| Path | Lines | Vai trò |
|------|-------|---------|
| Body-Base/Melody Lens/Personal-Melody.md | 922 | Mỗi người = 1 bài nhạc |
| Body-Base/Melody Lens/Personal-Melody-Example.md | 357 | 3 profiles trajectory phổ biến |
| Body-Base/Melody Lens/Melody-Arc.md | 749 | Dissonance → compile → melody upgrade |
| Body-Base/Melody Lens/Global-Melody.md | 570 | Group → culture → global interactions |

### PFC Detail

| Path | Lines | Vai trò |
|------|-------|---------|
| PFC/PFC-Label.md | 1,164 | Vocabulary reference: 13 domain labels |
| PFC/PFC-Hold-Dimensions.md | 415 | WHY ~4±1 (6 lực hội tụ) |
| PFC/Attention-Spectrum.md | 389 | Multi-factor attention spectrum |
| PFC/Logic-Planning.md | 666 | Chain labeled chunks → plan |
| PFC/Logic-Feeling-Failure-Examples.md | 831 | 18 ví dụ verified (logic sai + feeling sai) |
| PFC/Imagination/Imagine-Final-Evaluation.md | 3,071 | 2-trục + 3D framework (Clarity × Quality × Trust) |

### Schema Detail

| Path | Lines | Vai trò |
|------|-------|---------|
| Body-Base/Schema/Anchor-Schema-Example.md | 963 | 24 ví dụ annotated (Micro → eXtreme) |
| Body-Base/Schema/Anchor-Schema-Extreme-Example.md | 1,646 | Failure mode: anchor quá mạnh + skip domain check |

### Other

| Path | Lines | Vai trò |
|------|-------|---------|
| Blackbox-Map.md | 1,124 | 5 GAPs chưa biết + 20 research directions |

---

## Tổng kết

| | Files | Lines |
|---|---|---|
| **Core path** (Tier 0-5) | 55 | ~85,700 |
| + Enrichment (1-3) | +20 | +30,700 |
| + Reference | +22 | +17,200 |
| **Toàn bộ** | ~97 | ~133,600 |

> **Không cần đọc 97 files.** Tier 0 (8 files) đã đủ cho hầu hết câu hỏi.
> Mỗi Tier thêm = 1 mức hiểu sâu hơn. Chọn điểm dừng phù hợp.
>
> **Ngoài Core-Deep-Dive:** Framework còn có Research/ (~30+ files) và Applications/ (~10+ files)
> cho các ứng dụng cụ thể: Education, Health Conditions, Love, Money, Religion, AI-Self-Model...
> Xem Research/01-File-Index.md và Applications/01-File-Index.md.
