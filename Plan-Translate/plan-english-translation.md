# English Translation — Master Plan + Methodology

> **Version**: 3.0
> **Created**: 2026-05-26
> **Updated**: 2026-05-27 (v3.0 — unified: plan + methodology in 1 file, prompt-translation.md DELETED)
> **Status**: ACTIVE
> **Supersedes**: v2.0 plan + prompt-translation.md (both merged here)
> **Companion files**:
>   - Plan-Translate/00-Glossary.md — terminology glossary (MUST load every session)
>   - Plan-Translate/plan-phase-X.md — per-phase detail plans (created just-in-time)

---

# ══════════════════════════════════════════════════
# PART 1 — PROJECT (WHAT)
# ══════════════════════════════════════════════════

## §0 — PROJECT OVERVIEW

Framework Human Predictive Drive (~319,000 dòng, ~16.2MB) hiện viết bằng
tiếng Việt primary + English technical terms. Project này tạo phiên bản
tiếng Anh HOÀN CHỈNH — không chỉ dịch, mà viết lại (rewrite) cho
English-speaking audience với chất lượng cao nhất có thể.

**Nguyên tắc cốt lõi:**
- Chậm mà chắc — mỗi file 3 phases (Deep Read → Plan → Execute)
- Không chỉ dịch — tạo phiên bản mới, có thể tái cấu trúc nếu cần
- Consistency > perfection — terminology nhất quán quan trọng hơn từng câu hoàn hảo
- Rolling wave planning — plan chi tiết cho phase hiện tại, tổng quan cho phases sau

### AI Role Definition

You are translating files from the **Human Predictive Drive** framework — a ~300,000-line Vietnamese neuroscience/psychology framework that describes human behavior through predictive body-brain mechanisms.

The source files are written in **Vietnamese primary + English technical terms** (a bilingual hybrid). ~40-50% of content is already in English (framework vocabulary, neuroscience terms, citations). Vietnamese carries the explanatory narrative, examples, and connecting logic.

Your task: **Create a high-quality English version** of each file. This is a **rewrite for an English-speaking audience**, not a word-for-word translation.

**You are NOT**:
- A machine translator producing literal output
- Simplifying or summarizing the content
- Adding your own analysis or opinions
- Changing the framework's claims or positions

**You ARE**:
- A skilled academic writer creating the English-language edition of a technical framework
- Preserving 100% of the content, structure, and depth
- Making the text read as if it was originally written in English
- Adding brief contextual notes ONLY where a non-Vietnamese reader would be lost

---

## §1 — SCOPE

### §1.1 Included (228 files)

| Phân vùng | Files | ~Lines |
|---|---|---|
| ROOT (Core-Software, Core-Hardware, Ask-AI, README) | 4 | 3,220 |
| Core-Deep-Dive/ framework files | ~98 | ~143,000 |
| Core-Deep-Dive/ drill files | ~56 | ~67,000 |
| Research/ | ~58 | ~76,000 |
| Applications/ | 8 | 9,262 |
| Public-Plan/ (non-plan files) | 4 | 2,675 |
| **TOTAL** | **~228** | **~301,000** |

### §1.2 Excluded

| Loại | Files | Lý do |
|---|---|---|
| backup/ và _backup/ folders | ~100+ | Versions cũ, không cần dịch |
| plan-*.md files | ~10 | Plans tiếng Việt, không dịch |
| VI/ folders (12 files) | 12 | Bản Vietnamese thuần của files đã tồn tại — dịch = duplicate |
| html-page/ | 1 | Web artifact |

### §1.3 Special handling

| File | Xử lý |
|---|---|
| 3 × 01-File-Index.md | REGENERATE sau khi tất cả files trong folder đã dịch |
| AI-Schema-Detection-update-draft.md | Dịch bình thường (active draft) |
| Quote-Analysis/plan.md | SKIP (plan file) |

### §1.4 VI/ files — Chi tiết

12 files trong Child-Chunk-Development/VI/ và Feeling/ là bản dịch Vietnamese
hoàn chỉnh của files đã tồn tại ở folder cha. Main files sẽ được tạo English
version → VI/ files trở thành redundant. SKIP.

Danh sách VI/ skip:
- Child-Chunk-Development/VI/00-Chunk-System-Sketch-VI.md
- Child-Chunk-Development/VI/01-PFC-Hardware-Reframe-VI.md
- Child-Chunk-Development/VI/02-Womb-to-Birth-Baseline-VI.md
- Child-Chunk-Development/VI/03-Visual-System-Arc-VI.md
- Child-Chunk-Development/VI/04-Auditory-System-Arc-VI.md
- Child-Chunk-Development/VI/05-Motor-Output-Arc-VI.md
- Child-Chunk-Development/VI/06a-Interoceptive-Bladder-Keystone-VI.md
- Child-Chunk-Development/VI/06b-Interoceptive-Other-States-VI.md
- Child-Chunk-Development/VI/07-Social-Recognition-Arc-VI.md
- Child-Chunk-Development/VI/08-Verbal-Production-Arc-VI.md
- Child-Chunk-Development/VI/09-Event-Chunks-Inference-Matrix-VI.md
- Child-Chunk-Development/VI/10-F1-Synthesis-VI.md
- Feeling/Drill-Feeling-Dev/Feel-Example-Draft_VI.md
- Feeling/Drill-Feeling-Knowning/VI/03-Theme-B-Verbal-Chain_VI.md

---

## §2 — KEY DECISIONS (Project-Level)

### §2.1 Folder structure

**Decision**: English/ parallel folder tại root, mirror source structure.

```
Human-Predictive-Drive/
├── English/                          ← NEW: toàn bộ English versions
│   ├── Core-Software.md
│   ├── Core-Hardware.md
│   ├── Ask-AI.md
│   ├── README.md
│   ├── Core-Deep-Dive/
│   │   ├── Observation/
│   │   ├── Body-Base/
│   │   ├── PFC/
│   │   ├── Collective/
│   │   ├── Domain/
│   │   └── Clarification/
│   ├── Research/
│   ├── Applications/
│   └── Public-Plan/
├── Plan-Translate/                   ← Plans + Glossary
│   ├── plan-english-translation.md   ← FILE NÀY (plan + methodology)
│   ├── 00-Glossary.md
│   └── plan-phase-X.md
├── Core-Software.md                  ← Vietnamese originals (untouched)
├── Core-Deep-Dive/
├── Research/
└── ...
```

**Lý do**: Source files untouched. Same internal structure → cross-refs hoạt động.
File names giữ nguyên → internal links work (chỉ cần thay root path).

### §2.2 File naming

**Decision**: Giữ NGUYÊN tên file (không suffix, không prefix).

**Lý do**: Cross-references dùng file names. Giữ nguyên = links work tự nhiên.

---

## §3 — PHASE ORDERING

### Ordering rationale

**Dependency-Driven Foundation-First:**
1. Files that DEFINE terms → before files that USE terms
2. Vocabulary reference → before mechanism files
3. Within sub-system: primitive → integration
4. Hub/entry-point files → LAST in sub-system (they reference everything)
5. Drill files → alongside their sub-system (shared vocabulary)

---

### PHASE A — Vocabulary + Core Architecture

**Goal**: Establish English terminology standard + overall framework framing.
**Estimated sessions**: 6-8

| # | Path | Lines | Role |
|---|---|---|---|
| A01 | Body-Feedback/Body-Feedback-Label.md | 1,163 | Vocabulary: body-feedback system |
| A02 | PFC/PFC-Label.md | 1,163 | Vocabulary: PFC system |
| A03 | README.md | 245 | Entry point, set tone |
| A04 | Core-Hardware.md | 414 | Physical architecture |
| A05 | Core-Software.md | 1,764 | Cycle architecture (LARGEST core file) |
| A06 | Ask-AI.md | 797 | AI interaction protocol |
| A07 | Neural-Architecture.md | 693 | 4-zone physical map |
| A08 | Neural-Processing-Flow.md | 1,271 | Signal pathway |
| A09 | Modality.md | 751 | 6 encoding channels |
| A10 | Blackbox-Map.md | 1,124 | What we don't know |

**Phase A total: 10 files, ~9,385 lines**

---

### PHASE B — Body-Feedback System

**Goal**: Foundation signal system — every mechanism file references this.
**Estimated sessions**: 8-10
**Pre-req**: Phase A complete (vocabulary established)

| # | Path | Lines | Note |
|---|---|---|---|
| B01 | Body-Feedback/Drill-Body-Feedback/01-Foundation.md | 1,127 | Dual-pull, interface loop |
| B02 | Body-Feedback/Drill-Body-Feedback/02-Dissonance.md | 1,853 | Dissonance spectrum |
| B03 | Body-Feedback/Drill-Body-Feedback/03-Reward.md | 2,280 | VTA + opioid |
| B04 | Body-Feedback/Drill-Body-Feedback/04-Integration.md | 1,856 | Unified loop |
| B05 | Body-Feedback/Body-Feedback-Mechanism.md | 1,531 | 4th axis, Body-Need |
| B06 | Body-Feedback/Gap-Direction.md | 2,681 | Gap = f(surrounding chunks) |
| B07 | Body-Feedback/Gap-Body-Need.md | 1,388 | 3 Satiation, ENGINE/ROAD/VEHICLE |
| B08 | Body-Feedback/Gap-Distribution-Profile.md | 2,370 | Per-person gap landscape |
| B09 | Body-Feedback/Reward-Signal-Architecture.md | 2,013 | Evaluative/Direct-State |
| B10 | Body-Feedback/Dissonance-Signal-Architecture.md | 1,571 | Counterpart of RSA |
| B11 | Body-Feedback/Reward-Calibration.md | 1,356 | Goldilocks per-gap |
| B12 | Body-Feedback/Action-Space.md | 1,729 | Supply-side capability |
| B13 | Body-Feedback/Hidden-Quality-Perception.md | 1,738 | Compilation depth → quality |
| B14 | Body-Feedback/Drill-Evolutionary-Sensor-Architecture.md | 636 | First-principles WHY |
| B15 | Body-Feedback/Body-Feedback.md | 1,150 | SYNTHESIS — last in sub-system |

**Phase B total: 15 files, ~25,279 lines**

---

### PHASE C — Chunk System

**Goal**: Sole substrate. Defines chunk, compile, agent-mechanism.
**Estimated sessions**: 14-18
**Pre-req**: Phase A + B complete

**C1. Chunk Core**

| # | Path | Lines | Note |
|---|---|---|---|
| C01 | Chunk/Chunk.md | 1,664 | DEFINES "chunk" for everything |
| C02 | Chunk/Compile-Taxonomy.md | 1,173 | 3 Compile Types |
| C03 | Chunk/Background-Pattern.md | 2,500 | Accumulated chunk bias |

**C2. Agent-Mechanism (dependency chain order)**

| # | Path | Lines | Why this position |
|---|---|---|---|
| C04 | Agent-Mechanism/Entity-Compiled.md | 1,231 | DEFINES entity-compiled |
| C05 | Agent-Mechanism/Self-Pattern-Modeling.md | 1,533 | APPLICATION-1 on Engine |
| C06 | Agent-Mechanism/Entity-Access.md | 1,468 | BUILDS ON Entity-Compiled |
| C07 | Agent-Mechanism/By-Product-Gap-Resonance.md | 1,709 | Core resonance |
| C08 | Agent-Mechanism/Bond-Architecture.md | 1,183 | BUILDS ON C04+C06 |
| C09 | Agent-Mechanism/Resonance-Sustainability.md | 1,355 | BUILDS ON C08 |
| C10 | Agent-Mechanism/Resonance-Per-Entity.md | 1,607 | BUILDS ON all above |
| C11 | Agent-Mechanism/By-Product-Scale.md | 905 | 1 mechanism × 3 scales |
| C12 | Agent-Mechanism/Entity-Access-Excess.md | 1,392 | Extension of C06 |
| C13 | Agent-Mechanism/Entity-Access-Calibration.md | 1,073 | Extension of C06 |
| C14 | Agent-Mechanism/Agent-Mechanism.md | 2,362 | HUB — last in sub-system |

**C3. Chunk Drills — Child Development**

| # | Path | Lines |
|---|---|---|
| C15 | Child-Chunk-Development/Foundation/00-Chunk-System-Sketch.md | 607 |
| C16 | Child-Chunk-Development/Foundation/01-PFC-Hardware-Reframe.md | 899 |
| C17 | Child-Chunk-Development/Foundation/02-Womb-to-Birth-Baseline.md | 965 |
| C18 | Child-Chunk-Development/Modality-Arcs/03-Visual-System-Arc.md | 849 |
| C19 | Child-Chunk-Development/Modality-Arcs/04-Auditory-System-Arc.md | 911 |
| C20 | Child-Chunk-Development/Modality-Arcs/05-Motor-Output-Arc.md | 767 |
| C21 | Child-Chunk-Development/Modality-Arcs/06a-Interoceptive-Bladder-Keystone.md | 1,086 |
| C22 | Child-Chunk-Development/Modality-Arcs/06b-Interoceptive-Other-States.md | 1,136 |
| C23 | Child-Chunk-Development/Modality-Arcs/07-Social-Recognition-Arc.md | 1,096 |
| C24 | Child-Chunk-Development/Modality-Arcs/08-Verbal-Production-Arc.md | 1,126 |
| C25 | Child-Chunk-Development/09-Event-Chunks-Inference-Matrix.md | 768 |
| C26 | Child-Chunk-Development/10-F1-Synthesis.md | 990 |

**C4. Chunk Drills — Internal Processing**

| # | Path | Lines |
|---|---|---|
| C27 | Chunk-Internal-Processing/00-Internal-Mechanism-Overview.md | 737 |
| C28 | Chunk-Internal-Processing/01-Chunk-Connection-Logical.md | 915 |
| C29 | Chunk-Internal-Processing/01b-Chunk-Activation-Dynamics.md | 806 |
| C30 | Chunk-Internal-Processing/01c-Chunk-Discovery-Lifecycle.md | 1,181 |
| C31 | Chunk-Internal-Processing/02-Feeling-Intuition-Gradient.md | 768 |
| C32 | Chunk-Internal-Processing/03-Chain-Anchor-Decay.md | 827 |
| C33 | Chunk-Internal-Processing/04-Right-Wrong-Vague.md | 874 |
| C34 | Chunk-Internal-Processing/05-Insight-Tacit-Upgrade.md | 786 |
| C35 | Chunk-Internal-Processing/06-Internal-Synthesis.md | 483 |

**C5. Chunk Drills — External Development + Language**

| # | Path | Lines |
|---|---|---|
| C36 | Chunk-External-Development/00-External-Mechanism.md | 823 |
| C37 | Chunk-External-Development/01-External-Synthesis.md | 465 |
| C38 | Chunk-External-Development/02-Cross-Network-Transfer.md | 1,437 |
| C39 | Language-Structure-Analysis/01-Natural-Language-Architecture.md | 1,306 |
| C40 | Language-Structure-Analysis/02-Mathematical-Language-Architecture.md | 1,133 |
| C41 | Language-Structure-Analysis/03-Musical-Notation-Architecture.md | 566 |
| C42 | Language-Structure-Analysis/04-Visual-Diagram-Architecture.md | 516 |
| C43 | Language-Structure-Analysis/05-Programming-Language-Architecture.md | 747 |

**C6. Chunk Drills — Integration**

| # | Path | Lines |
|---|---|---|
| C44 | Drill-Chunk/09-Learning-Cycle.md | 1,556 |
| C45 | Drill-Chunk/99-Master-Synthesis.md | 1,406 |

**Phase C total: 45 files, ~48,580 lines**

---

### PHASE D — PFC System

**Goal**: Observer + orchestrator mechanisms.
**Estimated sessions**: 7-9
**Pre-req**: Phase A + B + C1-C2 complete (chunk + agent vocabulary)

| # | Path | Lines | Note |
|---|---|---|---|
| D01 | PFC/PFC-Function.md | 567 | DEFINES 24 functions |
| D02 | PFC/PFC-Hardware.md | 1,004 | COMT/DRD4 variation |
| D03 | PFC/PFC-Configuration.md | 1,327 | 6 modes |
| D04 | PFC/PFC-Development.md | 562 | Trajectory |
| D05 | PFC/PFC-Hold-Dimensions.md | 415 | Why ~4±1 |
| D06 | PFC/Attention-Spectrum.md | 389 | Multi-factor |
| D07 | PFC/Simulation-Engine.md | 977 | 1 engine, 3 components — KEY |
| D08 | PFC/PFC-Operations.md | 1,002 | Hold/Suppress — builds on all |
| D09 | PFC/Logic-Feeling.md | 1,525 | Observer labels |
| D10 | PFC/Logic-Planning.md | 666 | Logic side |
| D11 | PFC/Logic-Feeling-Balance.md | 1,629 | Meta-principle |
| D12 | PFC/Logic-Feeling-Failure-Examples.md | 830 | Evidence companion |
| D13 | PFC/Imagination/Imagination.md | 793 | Process overview |
| D14 | PFC/Imagination/Imagine-Final.md | 1,517 | Constructive simulation |
| D15 | PFC/Imagination/Imagine-Final-Evaluation.md | 3,070 | 3D framework |
| D16 | PFC/Imagination/Somatic-Articulation-Loop.md | 2,844 | Body → explicit |

**Phase D total: 16 files, ~19,117 lines**

---

### PHASE E — Feeling + Schema + Melody Lens

**Goal**: Observation interface + pattern recognition + metaphor system.
**Estimated sessions**: 8-11
**Pre-req**: Phase A-D complete

**E1. Feeling Core**

| # | Path | Lines |
|---|---|---|
| E01 | Feeling/Feeling.md | 2,184 |
| E02 | Feeling/Feeling-Research.md | 2,215 |
| E03 | Feeling/Feeling-Mechanism-Deep-Draft.md | 1,636 |
| E04 | Feeling/Feeling-Sources-Draft.md | 1,598 |
| E05 | Feeling/Feeling-Accuracy-Draft.md | 1,887 |
| E06 | Feeling/Feeling-Chunk-Bridge-Draft.md | 556 |
| E07 | Feeling/Feeling-Literacy-Training-Draft.md | 1,865 |
| E08 | Feeling/Body-Knowing.md | 2,041 |

**E2. Feeling Drills**

| # | Path | Lines |
|---|---|---|
| E09 | Feeling/Drill-Feeling-Dev/Feel-Development.md | 480 |
| E10 | Feeling/Drill-Feeling-Dev/Feel-Example-Draft.md | 11,553 |
| E11 | Feeling/Drill-Feeling-Knowning/00-Reading-Notes.md | 1,871 |
| E12 | Feeling/Drill-Feeling-Knowning/01-Theme-A-Architecture.md | 579 |
| E13 | Feeling/Drill-Feeling-Knowning/02-Theme-D-Right-Wrong.md | 711 |
| E14 | Feeling/Drill-Feeling-Knowning/03-Theme-B-Verbal-Chain.md | 661 |
| E15 | Feeling/Drill-Feeling-Knowning/04-Theme-C-Ritual.md | 596 |
| E16 | Feeling/Drill-Feeling-Knowning/05-Theme-E-Empathy-Giving.md | 902 |
| E17 | Feeling/Drill-Feeling-Knowning/06-Theme-F-Logic-Feeling-Check.md | 501 |
| E18 | Feeling/Drill-Feeling-Knowning/99-Overview-Synthesis.md | 1,883 |

**E3. Schema**

| # | Path | Lines |
|---|---|---|
| E19 | Schema/Schema.md | 832 |
| E20 | Schema/Anchor-Schema.md | 1,879 |
| E21 | Schema/Anchor-Schema-Example.md | 963 |
| E22 | Schema/Anchor-Schema-Extreme-Example.md | 1,646 |

**E4. Melody Lens**

| # | Path | Lines |
|---|---|---|
| E23 | Melody Lens/Personal-Melody.md | 922 |
| E24 | Melody Lens/Personal-Melody-Example.md | 357 |
| E25 | Melody Lens/Melody-Arc.md | 749 |
| E26 | Melody Lens/Global-Melody.md | 570 |

**Phase E total: 26 files, ~39,066 lines**

---

### PHASE F — Body-Base Root

**Goal**: Integration files that tie Body-Base system together.
**Estimated sessions**: 4-5
**Pre-req**: Phase B-E complete (all sub-systems translated)

| # | Path | Lines | Note |
|---|---|---|---|
| F01 | Body-Base/Why-Body-Knows.md | 1,304 | Meta-question |
| F02 | Body-Base/Cortisol-Baseline.md | 3,339 | Amplifier — referenced everywhere |
| F03 | Body-Base/Valence-Propagation.md | 2,001 | 3 pillars |
| F04 | Body-Base/Body-Coupling.md | 2,883 | Coupling mechanism |
| F05 | Body-Base/Inter-Body-Mechanism.md | 1,474 | 8 principles — source of truth |
| F06 | Body-Base/Body-Base.md | 1,479 | ENTRY POINT — last (refs 60+ files) |

**Phase F total: 6 files, ~12,480 lines**

---

### PHASE G — Observation Parameters

**Goal**: Named patterns emergent from chunk dynamics.
**Estimated sessions**: 5-7
**Pre-req**: Phase A-F complete (full Body-Base vocabulary)

**G1. Primitive**

| # | Path | Lines |
|---|---|---|
| G01 | Observation/Novelty.md | 993 |
| G02 | Observation/Threat.md | 1,073 |
| G03 | Observation/Boredom.md | 1,302 |
| G04 | Observation/Drive.md | 776 |

**G2. Social**

| # | Path | Lines |
|---|---|---|
| G05 | Observation/Empathy.md | 2,895 |
| G06 | Observation/Connection.md | 3,072 |
| G07 | Observation/Status.md | 2,470 |
| G08 | Observation/Protect.md | 2,004 |

**G3. Higher-order**

| # | Path | Lines |
|---|---|---|
| G09 | Observation/Meaning.md | 1,979 |
| G10 | Observation/Autonomy-Hardware.md | 903 |
| G11 | Observation/Autonomy.md | 1,007 |
| G12 | Observation/Gratitude.md | 2,201 |
| G13 | Observation/Obligation.md | 2,554 |

**G4. Bridge / Tool**

| # | Path | Lines |
|---|---|---|
| G14 | Observation/Liking-Wanting.md | 1,206 |
| G15 | Observation/AI-Schema-Detection.md | 1,718 |
| G16 | Observation/AI-Schema-Detection-update-draft.md | 319 |

**Phase G total: 16 files, ~26,472 lines**

---

### PHASE H — Collective + Domain + Clarification

**Goal**: Group dynamics, external reality, framework divergences.
**Estimated sessions**: 5-6
**Pre-req**: Phase A-G complete

**H1. Collective**

| # | Path | Lines | Note |
|---|---|---|---|
| H01 | Collective/Collective-Body.md | 1,780 | Core mechanism |
| H02 | Collective/Coordination-Node.md | 2,211 | Resource allocation |
| H03 | Collective/Collective-Arc-Dynamics.md | 1,083 | Shelf-life |
| H04 | Collective/Collective-Purpose.md | 1,114 | Meta-level |
| H05 | Collective/Compliance-Floor.md | 819 | Governance |
| H06 | Collective/Collective.md | 813 | HUB — last |

**H2. Domain**

| # | Path | Lines |
|---|---|---|
| H07 | Domain/Domain.md | 716 |
| H08 | Domain/Conflict-Dynamics.md | 635 |
| H09 | Domain/Discovery-vs-Expansion.md | 1,067 |
| H10 | Domain/Knowledge-Flow.md | 674 |
| H11 | Domain/Domain-Mapping-Drive.md | 3,666 |
| H12 | Domain/Drill-Emergent-Pattern.md | 675 |

**H3. Clarification**

| # | Path | Lines |
|---|---|---|
| H13 | Clarification/Dopamine-Is-Not-Reward.md | 693 |
| H14 | Clarification/Prediction-Error-Is-Not-Reward.md | 491 |
| H15 | Clarification/Mirror-Neuron-Rejection.md | 463 |
| H16 | Clarification/Cortisol-Amplifier-Not-Cause.md | 458 |

**Phase H total: 16 files, ~16,858 lines**

---

### PHASE I — Research

**Goal**: Applied research + extensions. Files relatively independent.
**Estimated sessions**: 15-20
**Pre-req**: Phase A-H complete (full framework vocabulary)

**I1. Health-Conditions**

| # | Path | Lines |
|---|---|---|
| I01 | Health-Conditions/Hijack/Addiction-Analysis.md | 1,170 |
| I02 | Health-Conditions/Hijack/Alcohol-Brain-Mechanism.md | 849 |
| I03 | Health-Conditions/Hijack/Alcohol-Vietnam-Generational.md | 794 |
| I04 | Health-Conditions/Hijack/Nicotine-Brain-Mechanism.md | 1,119 |
| I05 | Health-Conditions/Neurodegeneration/Parkinson-Analysis.md | 1,598 |
| I06 | Health-Conditions/Neurodegeneration/Alzheimer-Analysis.md | 2,996 |
| I07 | Health-Conditions/OCD-Analysis.md | 1,540 |
| I08 | Health-Conditions/PTSD-Analysis.md | 2,646 |
| I09 | Health-Conditions/Neurodiversity/ADHD-Observation.md | 1,959 |
| I10 | Health-Conditions/Neurodiversity/Autism-Observation.md | 2,789 |

**I2. Love**

| # | Path | Lines |
|---|---|---|
| I11 | Love-Romantic.md | 3,287 |
| I12 | Love-Unified.md | 2,532 |

**I3. Global**

| # | Path | Lines |
|---|---|---|
| I13 | Global/Human-AI-Future.md | 982 |
| I14 | Global/AI-Self-Model.md | 1,580 |
| I15 | Global/Social-Calibration.md | 1,809 |
| I16 | Global/Uncanny-Valley.md | 1,513 |
| I17 | Global/Innovation-Geography.md | 1,174 |

**I4. Birth-Rate-Decline**

| # | Path | Lines |
|---|---|---|
| I18 | Global/Birth-Rate-Decline/00_Overview.md | 407 |
| I19 | Global/Birth-Rate-Decline/01_South-Korea_Analysis.md | 778 |
| I20 | Global/Birth-Rate-Decline/03_China_Analysis.md | 835 |
| I21 | Global/Birth-Rate-Decline/04_France_Analysis.md | 740 |
| I22 | Global/Birth-Rate-Decline/05_Finland_Analysis.md | 705 |
| I23 | Global/Birth-Rate-Decline/06_Israel_Analysis.md | 845 |
| I24 | Global/Birth-Rate-Decline/09_Vietnam_Analysis.md | 742 |
| I25 | Global/Birth-Rate-Decline/09_Vietnam_Solution.md | 579 |
| I26 | Global/Birth-Rate-Decline/100_Solutions.md | 562 |

**I5. Human-Learning**

| # | Path | Lines |
|---|---|---|
| I27 | Human-Learning/Child-Development/Child-Development-Mechanism.md | 2,640 |
| I28 | Human-Learning/Child-Development/Natural-Development.md | 2,404 |
| I29 | Human-Learning/Child-Development/Skill-Introduction.md | 2,276 |
| I30 | Human-Learning/Child-Development/Mother-Optimization.md | 2,562 |
| I31 | Human-Learning/Education-Mechanism/Education-Mechanism.md | 1,714 |
| I32 | Human-Learning/Education-Mechanism/Domain-Knowledge-Map.md | 999 |
| I33 | Human-Learning/Education-Mechanism/Expansion-Saturation-Crisis.md | 1,829 |
| I34 | Human-Learning/Education-Mechanism/Compile-Type-Learning.md | 1,234 |
| I35 | Human-Learning/Education-Mechanism/Connection-Education.md | 2,165 |
| I36 | Human-Learning/Education-Mechanism/Observation/Education-Arms-Race.md | 1,141 |
| I37 | Human-Learning/Education-Mechanism/Observation/Money-Education.md | 1,980 |

**I6. Remaining Research**

| # | Path | Lines |
|---|---|---|
| I38 | Money-Analysis.md | 1,832 |
| I39 | Climate-Cognition.md | 1,064 |
| I40 | Fidgeting-Analysis.md | 1,276 |
| I41 | Sensitivity-Classification.md | 305 |
| I42 | Self-Created-Threat.md | 988 |
| I43 | Relativity-Explained.md | 1,293 |
| I44 | Melody-Technology/Melody-Technology-Overview.md | 404 |
| I45 | Melody-Technology/Religion.md | 1,955 |
| I46 | Melody-Technology/Idol-Phenomenon.md | 963 |
| I47 | Meta-Impact/Meta-Impact.md | 471 |
| I48 | Meta-Impact/Creator-Lens.md | 446 |
| I49 | Meta-Impact/Epistemological-Position.md | 530 |
| I50 | Mismatch-Patterns/Collective-Schema-Pressure.md | 758 |
| I51 | Neuro-Measurement/00-Goals.md | 176 |
| I52 | Neuro-Measurement/01-Implementation-Plan.md | 132 |

**I7. Quote-Analysis**

| # | Path | Lines |
|---|---|---|
| I53 | Quote-Analysis/pending-quotes.md | 110 |
| I54 | Quote-Analysis/Work-Adversity-Fear-Cluster.md | 1,106 |
| I55 | Quote-Analysis/Work-Chunk-Dependent-Visibility-Cluster.md | 848 |
| I56 | Quote-Analysis/Work-Comparison-Thief-Of-Joy.md | 1,130 |
| I57 | Quote-Analysis/Work-Goal-And-Why.md | 780 |
| I58 | Quote-Analysis/Work-Journey-Destination-Cluster.md | 865 |
| I59 | Quote-Analysis/Work-Move-Fast-Break-Things.md | 709 |
| I60 | Quote-Analysis/Work-Stay-Hungry-Stay-Foolish.md | 658 |
| I61 | Quote-Analysis/Work-Think-Act-Become-Cluster.md | 1,013 |

**Phase I total: 61 files, ~78,506 lines**

---

### PHASE J — Applications + Public-Plan

**Goal**: Practical implementations + public-facing content.
**Estimated sessions**: 3-5
**Pre-req**: Phase I complete (full research vocabulary)

**J1. Applications — Education System**

| # | Path | Lines |
|---|---|---|
| J01 | Applications/Education-System/00_Overview.md | 406 |
| J02 | Applications/Education-System/Education-System.md | 1,629 |
| J03 | Applications/Education-System/Hardware-Calibration.md | 1,689 |
| J04 | Applications/Education-System/Curriculum-Framework.md | 990 |
| J05 | Applications/Education-System/Era-Analysis-2025.md | 836 |

**J2. Applications — VN-specific**

| # | Path | Lines | Note |
|---|---|---|---|
| J06 | Applications/Education-System/Country/VN/VN-Education-Status.md | 1,531 | Heavy annotation |
| J07 | Applications/Education-System/Country/VN/VN-Cultural-Factors.md | 1,224 | Heavy annotation |
| J08 | Applications/Education-System/Country/VN/VN-Recommendations.md | 957 | Heavy annotation |

**J3. Public-Plan**

| # | Path | Lines |
|---|---|---|
| J09 | Public-Plan/01-Dopamine-Not-Reward.md | 539 |
| J10 | Public-Plan/expert-verification-map.md | 1,175 |
| J11 | Public-Plan/framing-engagement-value.md | 643 |
| J12 | Public-Plan/summary-paper-outline.md | 318 |

**Phase J total: 12 files, ~11,937 lines**

---

### PHASE K — File Index Regeneration

**Goal**: Generate English versions of File-Index files.
**Estimated sessions**: 1
**Pre-req**: ALL previous phases complete

| # | Path | Note |
|---|---|---|
| K01 | Core-Deep-Dive/01-File-Index.md | Regenerate with English descriptions |
| K02 | Research/01-File-Index.md | Regenerate with English descriptions |
| K03 | Applications/01-File-Index.md | Regenerate with English descriptions |

---

### SUMMARY

| Phase | Files | ~Lines | Sessions | Cumulative |
|---|---|---|---|---|
| A: Vocab + Core | 10 | 9,385 | 6-8 | 10 |
| B: Body-Feedback | 15 | 25,279 | 8-10 | 25 |
| C: Chunk + Agent + Drills | 45 | 48,580 | 14-18 | 70 |
| D: PFC | 16 | 19,117 | 7-9 | 86 |
| E: Feeling + Schema + Melody | 26 | 39,066 | 8-11 | 112 |
| F: Body-Base Root | 6 | 12,480 | 4-5 | 118 |
| G: Observation | 16 | 26,472 | 5-7 | 134 |
| H: Collective + Domain + Clarif | 16 | 16,858 | 5-6 | 150 |
| I: Research | 61 | 78,506 | 15-20 | 211 |
| J: Applications + Public | 12 | 11,937 | 3-5 | 223 |
| K: File Index Regeneration | 3 | — | 1 | 226 |
| **TOTAL** | **226** | **~287,680** | **~76-100** | |

---

## §4 — PROGRESS TRACKING

Format: [x] = done, [ ] = not started, [~] = in progress

### Phase A — Vocabulary + Core Architecture
- [ ] A01 Body-Feedback-Label.md
- [ ] A02 PFC-Label.md
- [ ] A03 README.md
- [ ] A04 Core-Hardware.md
- [ ] A05 Core-Software.md
- [ ] A06 Ask-AI.md
- [ ] A07 Neural-Architecture.md
- [ ] A08 Neural-Processing-Flow.md
- [ ] A09 Modality.md
- [ ] A10 Blackbox-Map.md

### Phase B — Body-Feedback System
- [ ] B01 01-Foundation.md
- [ ] B02 02-Dissonance.md
- [ ] B03 03-Reward.md
- [ ] B04 04-Integration.md
- [ ] B05 Body-Feedback-Mechanism.md
- [ ] B06 Gap-Direction.md
- [ ] B07 Gap-Body-Need.md
- [ ] B08 Gap-Distribution-Profile.md
- [ ] B09 Reward-Signal-Architecture.md
- [ ] B10 Dissonance-Signal-Architecture.md
- [ ] B11 Reward-Calibration.md
- [ ] B12 Action-Space.md
- [ ] B13 Hidden-Quality-Perception.md
- [ ] B14 Drill-Evolutionary-Sensor-Architecture.md
- [ ] B15 Body-Feedback.md

### Phase C — Chunk System
- [ ] C01 Chunk.md
- [ ] C02 Compile-Taxonomy.md
- [ ] C03 Background-Pattern.md
- [ ] C04 Entity-Compiled.md
- [ ] C05 Self-Pattern-Modeling.md
- [ ] C06 Entity-Access.md
- [ ] C07 By-Product-Gap-Resonance.md
- [ ] C08 Bond-Architecture.md
- [ ] C09 Resonance-Sustainability.md
- [ ] C10 Resonance-Per-Entity.md
- [ ] C11 By-Product-Scale.md
- [ ] C12 Entity-Access-Excess.md
- [ ] C13 Entity-Access-Calibration.md
- [ ] C14 Agent-Mechanism.md
- [ ] C15-C26 Child-Chunk-Development (12 files)
- [ ] C27-C35 Chunk-Internal-Processing (9 files)
- [ ] C36-C43 Chunk-External-Development + Language (8 files)
- [ ] C44 09-Learning-Cycle.md
- [ ] C45 99-Master-Synthesis.md

### Phase D-K
- [ ] D01-D16 PFC System (16 files)
- [ ] E01-E26 Feeling + Schema + Melody (26 files)
- [ ] F01-F06 Body-Base Root (6 files)
- [ ] G01-G16 Observation Parameters (16 files)
- [ ] H01-H16 Collective + Domain + Clarification (16 files)
- [ ] I01-I61 Research (61 files)
- [ ] J01-J12 Applications + Public-Plan (12 files)
- [ ] K01-K03 File Index Regeneration (3 files)

---

## §5 — GLOSSARY STRATEGY

**File**: Plan-Translate/00-Glossary.md (CREATED, ~150 terms initial)

### §5.1 Categories

- **Core**: chunk, compile, body-feedback, prediction-delta, PFC, etc.
- **Observation**: novelty, threat, boredom, drive, empathy, etc.
- **Agent**: entity-access, entity-compiled, self-pattern-modeling, etc.
- **Processing**: compiled/fresh, hold/suppress, etc.
- **Cultural**: Vietnamese terms that stay Vietnamese + explanation

### §5.2 Growth process

1. Initial: extract from Body-Feedback-Label.md + PFC-Label.md (~150 terms) — DONE
2. Phase A: add terms from Core-Software, Core-Hardware
3. Each subsequent phase: add new terms discovered
4. Glossary = living document, grows throughout project

---

## §6 — NOTES + OPEN QUESTIONS

### §6.1 Large files requiring special attention

| File | Lines | Note |
|---|---|---|
| Feel-Example-Draft.md | 11,553 | May need multiple sessions |
| Core-Software.md | 1,764 | Central file, set tone for everything |
| Domain-Mapping-Drive.md | 3,666 | Deep cross-references |
| Love-Romantic.md | 3,287 | Test case for entire framework |
| Cortisol-Baseline.md | 3,339 | Medical terminology |
| Imagine-Final-Evaluation.md | 3,070 | Complex 3D framework |
| Connection.md | 3,072 | Many dependencies |
| Empathy.md | 2,895 | ~20 dependencies |
| Alzheimer-Analysis.md | 2,996 | Heavy medical content |
| Somatic-Articulation-Loop.md | 2,844 | Nuanced body-knowledge |

### §6.2 Ordering may adjust

Phase ordering is designed for maximum vocabulary consistency.
Actual execution may reveal better orderings within phases.
Each plan-phase-X.md can adjust internal ordering.

---

# ══════════════════════════════════════════════════
# PART 2 — METHODOLOGY (HOW)
# ══════════════════════════════════════════════════

## §7 — 3-PHASE WORKFLOW (MANDATORY FOR ALL FILES)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHY 3 PHASES:

  Translation quality depends on UNDERSTANDING DEPTH.

  1-pass = "I read the words and converted them to English."
  3-phase = "I understood the file's role in the framework,
    planned how to present it for an English audience, and THEN wrote
    it as if I were the original author writing in English."

  Every file in this framework matters. No shortcuts.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOW TO USE:

  For each file, run 3 phases:

  PHASE 1 — DEEP READ (no writing)
    Load: this plan + 00-Glossary.md + source file + key dependencies
    Command: "Phase 1: Deep Read [filename]."
    Output: Understanding Report (§8.1)

  PHASE 2 — DRAFT PLAN (outline + decisions)
    Command: "Phase 2: Draft the translation plan for [filename]."
    Output: Translation Plan (§8.2)

  PHASE 3 — EXECUTE (write the English version)
    Command: "Phase 3: Execute the translation of [filename]."
    Output: Complete English file + translation notes (§8.3)

    For large files (>2,000 lines): split Phase 3 at § boundaries.

  Context window: Prioritize Glossary > English deps > Vietnamese deps.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


PHASE 1 — DEEP READ
════════════════════

  Goal: UNDERSTAND the file deeply before any translation decisions.

  1. Read Vietnamese source COMPLETELY (every section, warning, example)
  2. Read 00-Glossary.md — identify all framework terms, flag missing ones
  3. Read plan-phase-X.md entry — anticipated challenges
  4. Read key dependency files (English first, Vietnamese if not yet translated)
  5. Identify Vietnamese cultural content → classify Category A/B/C/D/E (§11)
  6. Identify restructuring opportunities (DEFAULT: keep original structure)
  7. Output Understanding Report (§8.1)

  ⚠️ DO NOT write any translation text in Phase 1.


PHASE 2 — DRAFT PLAN
═════════════════════

  Goal: Make ALL decisions before writing.

  1. Structure decision: keep / restructure? Why?
  2. Section-by-section plan (purpose, terms, Vietnamese content, deps needed)
  3. Glossary additions: propose new terms
  4. Vietnamese content handling: full table per item
  5. Execution plan: how many blocks? which deps per block?
  6. Open questions: ask before Phase 3
  7. Output Translation Plan (§8.2)

  ⚠️ DO NOT write any translation text in Phase 2.
  ⚠️ User reviews plan before Phase 3.


PHASE 3 — EXECUTE
══════════════════

  Goal: Write the English version following Phase 2 plan.

  1. Load Phase 2 plan + Glossary + dependencies
  2. Write YAML header (§10.1)
  3. Write Table of Contents
  4. Work section by section: read Vietnamese → understand INTENT → write English
  5. Final review: natural flow? Quality checklist (§15)?
  6. Output complete file + Translation Notes (§8.3)

  Large files: split into blocks. Translation notes after final block only.
  ⚠️ Follow Phase 2 plan. Note deviations.
```

---

## §8 — OUTPUT FORMATS (Per Phase)

### §8.1 Phase 1 Output: Understanding Report

```markdown
# Phase 1 — Deep Read Report: [filename]

## File Identity
- **Role**: [DEFINES vs REFERENCES]
- **Size**: [lines] | **Sections**: [count] | **Dependencies**: [count]

## Key Concepts Defined Here
- [concept]: [brief description]

## Key Concepts Referenced (defined elsewhere)
- [concept]: defined in [file.md §X]

## Dependencies Read
- [file.md] — read: [YES/partial/NO] — needed for: [sections]

## Vietnamese Cultural Content
- §X: [content] → Category [A/B/C/D/E]

## Translation Challenges
- [challenge]: [why hard + initial thoughts]

## Restructuring Opportunities
- [opportunity or "NONE"]

## New Terms Not in Glossary
- [term]: [proposed English]
```

### §8.2 Phase 2 Output: Translation Plan

```markdown
# Phase 2 — Translation Plan: [filename]

## Structure Decision
- [ ] Keep original / [ ] Restructure: [describe]

## Section-by-Section Plan
### §0 — [VN title] → [EN title]
- Content: [summary] | Approach: [keep/merge/expand]
- Terms: [list] | Vietnamese: [Category + handling]
- Deps needed: [files]
[repeat per section]

## Glossary Additions
| Term | English | Category |
|---|---|---|

## Vietnamese Examples
| §X | Vietnamese | Category | English |
|---|---|---|---|

## Execution Plan
- Block 1: §0-§X (deps: [...])
- Block 2: §Y-§Z (deps: [...])

## Open Questions
- [questions]
```

### §8.3 Phase 3 Output: English File + Notes

Output the ENTIRE file (YAML header → last line). Then add:

```markdown
---
## TRANSLATION NOTES
### Glossary Additions: [term]: [English] — [context]
### Restructuring: [changes or "None"]
### Decisions: [section]: [what and why]
### Deviations from Plan: [changes or "None"]
### Quality Checklist (§15): [x]/[ ] per item
### Uncertainties: [section]: [what]
```

Split large files at § boundaries. Translation notes after FINAL split only.

---

## §9 — NON-NEGOTIABLE RULES

### §9.1 Terminology Consistency

**ALL framework terms MUST match 00-Glossary.md EXACTLY.**

- Verify all terms against Glossary before writing ANY section
- Use EXACT canonical form (capitalization, hyphenation, phrasing)
- Missing term → flag it, propose English rendering
- NEVER invent alternative phrasings

Must be exact:
- "body-base reward" (NOT "bodily reward" or "physical reward")
- "prediction-delta" (NOT "prediction error" — framework rejects this)
- "Self-Pattern-Modeling" (NOT "self-modeling" or "pattern matching")
- "Compiled/Fresh" (NOT "automatic/deliberate" — except when explaining)
- "Entity-Compiled" (NOT "bonded entity" or "attached entity")
- "Hardware Subsidy" (NOT "biological support" or "hormonal aid")

### §9.2 Content Preservation

- **100% content preserved** — do NOT omit, summarize, or condense
- 15 bullet points → 15 bullet points. 20-row table → 20-row table.
- ⚠️ warnings and ⭐ highlights preserved with full content
- All quantitative claims preserved: "~95%", "40→200h", "4±1"

### §9.3 Structure Preservation

- **§ numbers**: preserved EXACTLY (§0, §1.1, §2.3...)
- **Confidence markers**: 🟢🟡🔴 preserved EXACTLY
- **Version numbers**: v2.0, v3.1... preserved EXACTLY
- **File paths**: preserved EXACTLY
- **Citations**: (Author Year) preserved EXACTLY
- **Tables**: same rows/columns
- **Code blocks**: same layout, translate text only
- **Emoji markers**: ⚠️ ⭐ 🔄 preserved

### §9.4 What You May Change

- Vietnamese narrative → natural English prose
- Vietnamese examples → English equivalents OR keep + annotate (§11)
- Section titles → English (keep §numbers)
- Table of contents → English
- Brief additions for non-Vietnamese readers (naturally integrated)
- Merge short Vietnamese sentences into flowing English prose
- Vietnamese emphasis (CAPS) → English emphasis (CAPS or bold)

---

## §10 — STRUCTURAL RULES

### §10.1 YAML Header Transformation

**Source:**
```yaml
---
title: Body-Feedback Label Convention — Vocabulary Reference
version: 2.1
created: 2026-05-12
rewritten: 2026-05-17 (v2.0 — FULL REWRITE: ...)
status: REFERENCE v2.1
scope: |
  VOCABULARY REFERENCE: Quy ước label cho toàn bộ body-feedback system...
dependencies:
  - Body-Feedback.md v2.0 — §2 dual-pull, §4 4 trục, §5 3 nguồn, §6 H10
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---
```

**Target:**
```yaml
---
title: Body-Feedback Label Convention — Vocabulary Reference
version: 2.1
source_version: Vietnamese v2.1 (2026-05-25)
english_created: [today's date]
english_updated: [leave empty]
status: REFERENCE v2.1
scope: |
  VOCABULARY REFERENCE: Label conventions for the entire body-feedback system...
  [Translate FULLY — do NOT summarize]
dependencies:
  - Body-Feedback.md v2.0 — §2 dual-pull, §4 4 axes, §5 3 sources, §6 H10
  [Keep paths EXACTLY. Translate description after —]
language: English (source: Vietnamese + English technical terms)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---
```

**Rules:**
- `title`: keep as-is (already English)
- `version`: keep EXACTLY + ADD `source_version` + ADD `english_created`
- `scope` + `purpose`: TRANSLATE fully
- `dependencies`: keep paths + versions, translate descriptions
- `rewritten`/`updated`/`previous`: keep (source history)
- REMOVE `position:` and `sources_backup:` fields

### §10.2 Code Block Handling

**ASCII Diagrams**: Translate Vietnamese labels, preserve structure EXACTLY.
```
Source: PFC ở trên cùng — điểm quan sát của mỗi người.
Target: PFC at the top — each person's observation point.
```

**Structured Explanations**: Translate headers/content, keep → arrows and indentation.
```
Source: ⭐ FRAMEWORK CÓ MECHANISMS CHÍNH XÁC — THIẾU CONVENTION DÙNG LABEL:
Target: ⭐ THE FRAMEWORK HAS PRECISE MECHANISMS — BUT LACKED LABEL CONVENTIONS:
```

**ASCII Tables**: Translate cell content, preserve box-drawing structure.
```
Source: │ Label │ Nghĩa + khi nào dùng │
Target: │ Label │ Definition + when to use │
```

**Mixed Language Lines**: Only translate Vietnamese parts.
```
Source: BUDGET: finite shared resource (mệt ở work → kém ở nhà)
Target: BUDGET: finite shared resource (tired at work → impaired at home)
```

**Size**: Source 30 lines → target ≈ 30 lines. Don't collapse or expand.

### §10.3 Markdown Tables

Translate headers + cells. Keep formatting (bold, links). Keep file references EXACTLY. "File này" → "This file"

### §10.4 Cross-References

**Dependency lines**: Keep path + version EXACTLY. Translate description only.
```
Source: Body-Feedback.md v2.0 — §2 dual-pull, §4 4 trục
Target: Body-Feedback.md v2.0 — §2 dual-pull, §4 4 axes
```

**Inline refs**: Keep EXACTLY as-is. **Version history**: Translate description, keep dates.

---

## §11 — VIETNAMESE CONTENT HANDLING

### §11.1 Five Categories

**A: Universal examples** → Translate directly.
```
"VD: đói, khát, đau, lạnh" → "e.g., hunger, thirst, pain, cold"
```

**B: Cultural examples** → Keep Vietnamese + English context.
```
"thuốc lào" → "*thuốc lào* (Vietnamese water pipe tobacco)"
"nhậu" → "*nhậu* (Vietnamese social drinking ritual)"
```

**C: Proverbs/sayings** → Keep Vietnamese + translate + explain.
```
"mặt lưng cái tủ" → "*mặt lưng cái tủ* ('the back of the wardrobe') — hidden quality"
```

**D: VN-specific data** → Keep + annotate source.
```
"Tỷ lệ sinh VN 6.0→1.9" → "Vietnam's birth rate 6.0→1.9 (World Bank data)"
```

**E: Framework principle in Vietnamese** → Translate, keep Vietnamese as reference.
```
"Chưa biết = không có gap" → "'What you don't know creates no gap' (*chưa biết = không có gap*)"
```

### §11.2 Abbreviations + Markers

| Vietnamese | English |
|---|---|
| VD: | e.g., |
| Ví dụ: | Example: |
| Nghĩa: | Meaning: |
| Dùng: / Dùng khi: | Use: / Use when: |
| Lý do: | Reason: |
| Tại sao: | Why: |
| Xem: | See: |
| Chi tiết: | Details: |
| Lưu ý: | Note: |
| Quan trọng: | Important: |
| Mục lục | Table of Contents |

### §11.3 Emphasis Patterns

| Vietnamese | English |
|---|---|
| "KHÔNG phải X" | "NOT X" (keep caps) |
| "TOÀN BỘ hệ thống" | "the ENTIRE system" |
| "CẢ ①+②" | "BOTH ①+②" |
| "CHỈ khi..." | "ONLY when..." |
| "LUÔN TỒN TẠI" | "ALWAYS EXISTS" |
| "KHÔNG BAO GIỜ" | "NEVER" |
| "★ NEW v2.0" | keep as-is |

### §11.4 Self-Referential

"File này" → "This file" | "Xem §X" → "See §X" | "→ chi tiết tại X.md" → "→ details in X.md"

---

## §12 — TONE + STYLE GUIDE

### §12.1 Voice
- **Academic but accessible** — researcher to educated general audience
- **Direct and assertive** — preserve the framework's strong claims
- **Honest about limits** — keep "hypothesis" / "we don't know" where source has them

### §12.2 Sentence Structure
Combine short Vietnamese sentences into flowing English, preserve emphasis.
```
Source: Body-need LUÔN TỒN TẠI. Không bao giờ = 0.
Target: Body-need ALWAYS EXISTS — it never equals zero.
```

### §12.3 Headers
"§0 — TẠI SAO CẦN FILE NÀY" → "§0 — WHY THIS FILE IS NEEDED"

### §12.4 Blockquotes
Translate with emotional impact. Preserve ** bold ** and → arrows.
```
Source: > **Bạn thấy bạn thân khóc → body bạn khó chịu.**
Target: > **You see your close friend cry → your body feels uneasy.**
```

---

## §13 — SPECIAL PATTERNS

**Warnings**: ⚠️ Body-need LUÔN TỒN TẠI → ⚠️ Body-need ALWAYS EXISTS (never = 0)

**Key Distinctions**: Preserve ≠ structure.
```
⚠️ gap ≠ body-need:
   Gap = 1 specific missing chunk
   Body-need = AGGREGATE of all gaps + hardware signals
```

**Numbered items**: ①②③④⑤⑥⑦ — keep EXACTLY.

**Confidence tags**: 🟡 PFC là observer → 🟡 PFC is an observer

**Mainstream → Framework**: Preserve contrast structure exactly.

---

## §14 — DEPRECATED TERMS (DO NOT USE)

| DO NOT USE | USE INSTEAD | WHY |
|---|---|---|
| "prediction error" | "prediction-delta" | Framework rejects RPE framing |
| "mirror neurons" (module) | "Self-Pattern-Modeling learned prediction" | Rejects dedicated mirror module |
| "willpower" | "PFC budget + Hold/Suppress" | Conflates mechanism with morality |
| "dopamine = reward" | "dopamine = prediction-delta signal" | Dopamine = detection, NOT reward |
| "stress" (for cortisol) | "cortisol as amplifier" | Cortisol ≠ stress |
| "pleasant" (mechanism) | "body-base reward" | pleasant = feeling label |
| "Logic vs Feeling" (mechanism) | "Compiled vs Fresh" | Observer ≠ mechanism labels |
| "willpower depletion" | "PFC budget depletion" | Mechanism-based framing |

If source uses deprecated term to explain why it's wrong → quote it, mark framework's position.

---

## §15 — QUALITY CHECKLIST

- [ ] All framework terms match 00-Glossary.md
- [ ] YAML header follows §10.1 template
- [ ] § numbers preserved exactly
- [ ] Cross-references valid (paths, versions, §refs)
- [ ] Vietnamese examples handled per §11 (Category A/B/C/D/E)
- [ ] Citations preserved verbatim
- [ ] Confidence markers 🟢🟡🔴 preserved
- [ ] Code block structure preserved
- [ ] No content omitted vs. source
- [ ] Natural English flow (not translation-ese)
- [ ] ⚠️ warnings preserved with full content
- [ ] Tables: same rows/columns
- [ ] Blockquotes: emotional impact preserved
- [ ] "Mainstream → Framework" contrasts preserved
- [ ] Deprecated terms NOT accidentally introduced

---

## §16 — COMMON PITFALLS

1. **Inconsistent terminology**: "body reward" vs "body-base reward"
2. **Over-translating**: expanding "Entity-Compiled" into a phrase — use the term
3. **Under-translating**: leaving Vietnamese untranslated in English text
4. **Breaking code blocks**: ASCII tables must align after translation
5. **Losing emphasis**: Vietnamese CAPS → English should keep CAPS where appropriate
6. **Adding hedging**: "Perhaps..." — the framework doesn't hedge
7. **Summarizing**: condensing 5-line explanation to 2 lines
8. **Missing warnings**: ⚠️ lines carry critical info — never skip
9. **Changing cross-references**: paths, §numbers, versions must be EXACT
10. **Using deprecated terms**: "prediction error" = CRITICAL ERROR
11. **Translating framework terms**: don't convert "body-base reward" to "physical reward"
12. **Losing Vietnamese identity**: some examples ARE the framework's character

---

## §17 — EXAMPLE: FULL SECTION TRANSLATION

**Vietnamese Source (§2B Body-Feedback-Label.md):**
```
  B) BODY-NEED (aggregate trạng thái CẦN):

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Nghĩa + khi nào dùng                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │ TIER 1  │ body-need           │ TỔNG HỢP trạng thái CẦN hiện tại.   │
  │ (chung) │                     │ Dùng: khi nói chung "body cần gì."  │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │ TIER 2  │ hardware body-need  │ Nguồn ①: Sensory-Driven.            │
  │ (source)│                     │ VD: đói, khát, đau, lạnh.           │
  │         │ pattern body-need   │ Nguồn ②: Chunk Dynamics/Pattern.    │
  │         │                     │ VD: nhớ bạn, career gap, identity.  │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Body-need LUÔN TỒN TẠI (không bao giờ = 0)
  ⚠️ 2 nguồn KHÔNG loại trừ — 1 event kích hoạt CẢ ①+②
```

**English Translation:**
```
  B) BODY-NEED (aggregate state of NEED):

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Definition + when to use             │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │ TIER 1  │ body-need           │ AGGREGATE current state of NEED.     │
  │ (general)│                    │ Use: general "what the body needs."  │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │ TIER 2  │ hardware body-need  │ Source ①: Sensory-Driven.            │
  │ (source)│                     │ e.g., hunger, thirst, pain, cold.   │
  │         │ pattern body-need   │ Source ②: Chunk Dynamics/Pattern.    │
  │         │                     │ e.g., missing a friend, career gap.  │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Body-need ALWAYS EXISTS (never = 0)
  ⚠️ 2 sources NOT mutually exclusive — 1 event can trigger BOTH ①+②
```

**What changed**: Vietnamese → English. Structure PRESERVED. Terms EXACT. ⚠️ KEPT.

---

> *This file is the SINGLE SOURCE OF TRUTH for the English translation project.*
> *PART 1 = what to translate (project management).*
> *PART 2 = how to translate (methodology).*
> *Load this + 00-Glossary.md + plan-phase-X.md at the start of every session.*
