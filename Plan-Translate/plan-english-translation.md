# English Translation — Master Plan + Methodology

> **Version**: 4.0
> **Created**: 2026-05-26
> **Updated**: 2026-06-05 (v4.0 — full audit against global-index.json: +24 new files, -10 removed, line counts verified)
> **Status**: ACTIVE
> **Supersedes**: v3.0 (2026-05-27)
> **Source of truth**: map-view/global-index.json (240 files, 2026-06-02) + README.md
> **Companion files**:
>   - Plan-Translate/00-Glossary.md — terminology glossary (MUST load every session)
>   - Plan-Translate/plan-phase-X.md — per-phase detail plans (created just-in-time)

---

# ══════════════════════════════════════════════════
# PART 1 — PROJECT (WHAT)
# ══════════════════════════════════════════════════

## §0 — PROJECT OVERVIEW

Framework Human Predictive Drive (~250,000 dòng, 242 files) hiện viết bằng
tiếng Việt primary + English technical terms. Project này tạo phiên bản
tiếng Anh HOÀN CHỈNH — không chỉ dịch, mà viết lại (rewrite) cho
English-speaking audience với chất lượng cao nhất có thể.

**Nguyên tắc cốt lõi:**
- Chậm mà chắc — mỗi file 3 phases (Deep Read → Plan → Execute)
- Không chỉ dịch — tạo phiên bản mới, có thể tái cấu trúc nếu cần
- Consistency > perfection — terminology nhất quán quan trọng hơn từng câu hoàn hảo
- Rolling wave planning — plan chi tiết cho phase hiện tại, tổng quan cho phases sau

### AI Role Definition

You are translating files from the **Human Predictive Drive** framework — a ~250,000-line Vietnamese neuroscience/psychology framework that describes human behavior through predictive body-brain mechanisms.

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

### §1.1 Source of truth

**map-view/global-index.json** (generated 2026-06-02, 241 files) + README.md = **242 files**.
Phase K thêm 3 × File-Index regeneration = **245 entries tổng cộng**.

### §1.2 Included (242 files)

| Phân vùng | Files | Lines |
|---|---|---|
| ROOT (Core-Software, Core-Hardware, Ask-AI, README, Reading-Roadmap) | 5 | 2,947 |
| Core-Deep-Dive/ | 161 | 165,735 |
| Research/ | 68 | 73,612 |
| Applications/ | 8 | 8,298 |
| **TOTAL** | **242** | **~250,592** |

### §1.3 Excluded

| Loại | Lý do |
|---|---|
| backup/ và _backup/ folders | Versions cũ |
| plan-*.md files | Plans tiếng Việt |
| VI/ folders (14 files) | Bản Vietnamese thuần — dịch = duplicate |
| Public-Plan/ | Skip theo quyết định v4.0 |
| docs/ | Web build artifacts |
| map-view/ | Visualization artifacts |
| Plan-Translate/ | Plan files, không dịch |

### §1.4 Special handling

| File | Xử lý |
|---|---|
| 3 × 01-File-Index.md | REGENERATE sau khi tất cả files trong folder đã dịch (Phase K) |
| README.md | Đã phần lớn English — tạo bản English tương ứng Vietnamese |
| Quote-Analysis/plan.md | SKIP (plan file, không có trong global-index) |
| Quote-Analysis/pending-quotes.md | SKIP (tracking file, không có trong global-index) |

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
│   └── Applications/
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

### Translation order ≠ Reading order (by design)

Reading-Roadmap.md defines a TOP-DOWN reading order (overview → detail).
Translation plan uses BOTTOM-UP order (detail → synthesis). Đây là đúng vì:

- **Bottom-up**: establish precise vocabulary at detail level FIRST
- **Hub files last**: Body-Base.md, Body-Feedback.md, Agent-Mechanism.md dịch CUỐI
  sub-system vì chúng DÙNG tất cả vocabulary từ child files
- **Glossary = bridge**: 00-Glossary.md đảm bảo consistency regardless of order
- **No 2-pass needed**: nếu dịch đúng thứ tự, mỗi file chỉ cần viết 1 lần

### Quality gates between phases

| After Phase | Review |
|---|---|
| A (Vocabulary) | ⭐ Glossary frozen check: all A01-A02 terms finalized. A05 Core-Software phrasing baseline. |
| B (Body-Feedback) | Check A05 Core-Software references to Body-Feedback still consistent. Minor touch-up if needed. |
| C (Chunk) | Check A05 references to Chunk + Agent-Mechanism still consistent. |
| E (Feeling) | Cross-check Feeling ↔ Body-Feedback terminology alignment. |
| F (Body-Base Root) | ⭐ Body-Base.md = ENTRY POINT cho readers. Review all cross-refs to translated files. |
| H (Collective+Domain) | All Core-Deep-Dive done. Full consistency sweep before Research. |
| I (Research) | Research files relatively independent. Spot-check glossary compliance. |

---

### PHASE A — Vocabulary + Core Architecture

**Goal**: Establish English terminology standard + overall framework framing.
**Estimated sessions**: 5-7

| # | Path | Lines | Role |
|---|---|---|---|
| A01 | Body-Feedback/Body-Feedback-Label.md | 1,004 | Vocabulary: body-feedback system |
| A02 | PFC/PFC-Label.md | 1,014 | Vocabulary: PFC system |
| A03 | README.md | 196 | Entry point (already mostly English) |
| A04 | Core-Hardware.md | 330 | Physical architecture |
| A05 | Core-Software.md | 1,600 | Cycle architecture (LARGEST core file) |
| A06 | Ask-AI.md | 621 | AI interaction protocol |
| A07 | Neural-Architecture.md | 802 | 4-zone physical map + bilateral architecture |
| A08 | Neural-Processing-Flow.md | 1,025 | Signal pathway |
| A09 | Modality.md | 589 | 6 encoding channels |
| A10 | Blackbox-Map.md | 886 | What we don't know |
| A11 | Reading-Roadmap.md | 283 | ⭐ NEW: 6-tier reading guide |
| A12 | Auditory-Hardware.md | 559 | ⭐ NEW: WHY auditory = unique channel |

**Phase A total: 12 files, ~8,909 lines**

---

### PHASE B — Body-Feedback System

**Goal**: Foundation signal system — every mechanism file references this.
**Estimated sessions**: 7-9
**Pre-req**: Phase A complete (vocabulary established)

| # | Path | Lines | Note |
|---|---|---|---|
| B01 | Body-Feedback/Drill-Body-Feedback/01-Foundation.md | 791 | Dual-pull, interface loop |
| B02 | Body-Feedback/Drill-Body-Feedback/02-Dissonance.md | 1,321 | Dissonance spectrum |
| B03 | Body-Feedback/Drill-Body-Feedback/03-Reward.md | 1,601 | VTA + opioid + 5 Preconditions |
| B04 | Body-Feedback/Drill-Body-Feedback/04-Integration.md | 1,406 | Unified loop |
| B05 | Body-Feedback/Body-Feedback-Mechanism.md | 1,255 | 4th axis, Body-Need |
| B06 | Body-Feedback/Body-Feedback-Precondition.md | 1,097 | ⭐ NEW: 5 Preconditions for signal firing |
| B07 | Body-Feedback/Gap-Direction.md | 2,222 | Gap = f(surrounding chunks) |
| B08 | Body-Feedback/Gap-Body-Need.md | 1,273 | 3 Satiation, ENGINE/ROAD/VEHICLE |
| B09 | Body-Feedback/Gap-Distribution-Profile.md | 1,921 | Per-person gap landscape |
| B10 | Body-Feedback/Reward-Signal-Architecture.md | 1,611 | Evaluative/Direct-State |
| B11 | Body-Feedback/Dissonance-Signal-Architecture.md | 1,223 | Counterpart of RSA |
| B12 | Body-Feedback/Reward-Calibration.md | 1,087 | Goldilocks per-gap |
| B13 | Body-Feedback/Action-Space.md | 1,408 | Supply-side capability |
| B14 | Body-Feedback/Hidden-Quality-Perception.md | 1,376 | Compilation depth → quality |
| B15 | Body-Feedback/Drill-Evolutionary-Sensor-Architecture.md | 507 | First-principles WHY |
| B16 | Body-Feedback/Body-Feedback.md | 963 | SYNTHESIS — last in sub-system |

**Phase B total: 16 files, ~21,062 lines**

---

### PHASE C — Chunk System

**Goal**: Sole substrate. Defines chunk, compile, agent-mechanism.
**Estimated sessions**: 13-17
**Pre-req**: Phase A + B complete

**C1. Chunk Core**

| # | Path | Lines | Note |
|---|---|---|---|
| C01 | Chunk/Chunk.md | 1,333 | v3.0 RESTRUCTURE — DEFINES "chunk" |
| C02 | Chunk/Compile-Taxonomy.md | 1,236 | v3.0 REFRAME — 1 Engine, 3 Types |
| C03 | Chunk/Compile-Sleep.md | 992 | ⭐ NEW: offline maintenance system |
| C04 | Chunk/Background-Pattern.md | 2,034 | v2.0 REWRITE — accumulated chunk bias |

**C2. Agent-Mechanism (dependency chain order)**

| # | Path | Lines | Why this position |
|---|---|---|---|
| C05 | Agent-Mechanism/Entity-Compiled.md | 1,015 | DEFINES entity-compiled |
| C06 | Agent-Mechanism/Self-Pattern-Modeling.md | 1,238 | v3.1 — APPLICATION-1 on Engine |
| C07 | Agent-Mechanism/Entity-Access.md | 1,196 | BUILDS ON Entity-Compiled |
| C08 | Agent-Mechanism/By-Product-Gap-Resonance.md | 1,364 | v1.4 — Core resonance |
| C09 | Agent-Mechanism/Bond-Architecture.md | 1,010 | v2.0 — BUILDS ON C05+C07 |
| C10 | Agent-Mechanism/Resonance-Sustainability.md | 1,044 | BUILDS ON C09 |
| C11 | Agent-Mechanism/Resonance-Per-Entity.md | 1,416 | BUILDS ON all above |
| C12 | Agent-Mechanism/By-Product-Scale.md | 813 | 1 mechanism × 3 scales |
| C13 | Agent-Mechanism/Entity-Access-Excess.md | 1,121 | Extension of C07 |
| C14 | Agent-Mechanism/Entity-Access-Calibration.md | 901 | Extension of C07 |
| C15 | Agent-Mechanism/Agent-Mechanism.md | 1,817 | v2.1 — HUB, last in sub-system |

**C3. Chunk Drills — Child Development**

| # | Path | Lines |
|---|---|---|
| C16 | Child-Chunk-Development/Foundation/00-Chunk-System-Sketch.md | 455 |
| C17 | Child-Chunk-Development/Foundation/01-PFC-Hardware-Reframe.md | 624 |
| C18 | Child-Chunk-Development/Foundation/02-Womb-to-Birth-Baseline.md | 693 |
| C19 | Child-Chunk-Development/Modality-Arcs/03-Visual-System-Arc.md | 568 |
| C20 | Child-Chunk-Development/Modality-Arcs/04-Auditory-System-Arc.md | 608 |
| C21 | Child-Chunk-Development/Modality-Arcs/05-Motor-Output-Arc.md | 506 |
| C22 | Child-Chunk-Development/Modality-Arcs/06a-Interoceptive-Bladder-Keystone.md | 708 |
| C23 | Child-Chunk-Development/Modality-Arcs/06b-Interoceptive-Other-States.md | 723 |
| C24 | Child-Chunk-Development/Modality-Arcs/07-Social-Recognition-Arc.md | 724 |
| C25 | Child-Chunk-Development/Modality-Arcs/08-Verbal-Production-Arc.md | 729 |
| C26 | Child-Chunk-Development/09-Event-Chunks-Inference-Matrix.md | 558 |
| C27 | Child-Chunk-Development/10-F1-Synthesis.md | 701 |

**C4. Chunk Drills — Internal Processing**

| # | Path | Lines |
|---|---|---|
| C28 | Chunk-Internal-Processing/00-Internal-Mechanism-Overview.md | 608 |
| C29 | Chunk-Internal-Processing/01-Chunk-Connection-Logical.md | 751 |
| C30 | Chunk-Internal-Processing/01b-Chunk-Activation-Dynamics.md | 650 |
| C31 | Chunk-Internal-Processing/01c-Chunk-Discovery-Lifecycle.md | 957 |
| C32 | Chunk-Internal-Processing/02-Feeling-Intuition-Gradient.md | 616 |
| C33 | Chunk-Internal-Processing/03-Chain-Anchor-Decay.md | 663 |
| C34 | Chunk-Internal-Processing/04-Right-Wrong-Vague.md | 720 |
| C35 | Chunk-Internal-Processing/05-Insight-Tacit-Upgrade.md | 643 |
| C36 | Chunk-Internal-Processing/06-Internal-Synthesis.md | 407 |

**C5. Chunk Drills — External Development + Language**

| # | Path | Lines |
|---|---|---|
| C37 | Chunk-External-Development/00-External-Mechanism.md | 677 |
| C38 | Chunk-External-Development/01-External-Synthesis.md | 382 |
| C39 | Chunk-External-Development/02-Cross-Network-Transfer.md | 1,153 |
| C40 | Language-Structure-Analysis/01-Natural-Language-Architecture.md | 1,040 |
| C41 | Language-Structure-Analysis/02-Mathematical-Language-Architecture.md | 885 |
| C42 | Language-Structure-Analysis/03-Musical-Notation-Architecture.md | 441 |
| C43 | Language-Structure-Analysis/04-Visual-Diagram-Architecture.md | 409 |
| C44 | Language-Structure-Analysis/05-Programming-Language-Architecture.md | 591 |

**C6. Chunk Drills — Integration**

| # | Path | Lines |
|---|---|---|
| C45 | Drill-Chunk/09-Learning-Cycle.md | 1,062 |
| C46 | Drill-Chunk/99-Master-Synthesis.md | 1,205 |
| C47 | Drill-Chunk/Drill-Body-Base-Boundary-Spectrum.md | 1,173 | ⭐ NEW |
| C48 | Drill-Chunk/Drill-Neural-Bilateral-Architecture.md | 264 | ⭐ NEW |
| C49 | Drill-Chunk/Drill-Agent-Feed-Channel.md | 901 | ⭐ NEW |

**Phase C total: 49 files, ~42,325 lines**

---

### PHASE D — PFC System

**Goal**: Observer + orchestrator mechanisms.
**Estimated sessions**: 6-9
**Pre-req**: Phase A + B + C1-C2 complete (chunk + agent vocabulary)

| # | Path | Lines | Note |
|---|---|---|---|
| D01 | PFC/PFC-Function.md | 469 | v1.2 — DEFINES 24 functions |
| D02 | PFC/PFC-Hardware.md | 799 | COMT/DRD4 variation |
| D03 | PFC/PFC-Configuration.md | 1,048 | v1.1 — 6 modes + PTSD/ADHD/Parkinson |
| D04 | PFC/PFC-Development.md | 566 | Trajectory |
| D05 | PFC/PFC-Hold-Dimensions.md | 321 | Why ~4±1 |
| D06 | PFC/Attention-Spectrum.md | 318 | v2.1 — Multi-factor + ADHD inverted-U |
| D07 | PFC/Simulation-Engine.md | 856 | 1 engine, 3 components — KEY |
| D08 | PFC/PFC-Operations.md | 967 | Hold/Suppress — builds on all |
| D09 | PFC/Logic-Feeling.md | 1,244 | v4.0 — Observer labels + Body-Knowing |
| D10 | PFC/Logic-Planning.md | 527 | Logic side |
| D11 | PFC/Logic-Feeling-Balance.md | 1,387 | Meta-principle |
| D12 | PFC/Logic-Feeling-Failure-Examples.md | 685 | Evidence companion |
| D13 | PFC/Self-Observation.md | 1,251 | ⭐ NEW: APPLICATION-3 Simulation-Engine |
| D14 | PFC/Imagination/Imagination.md | 642 | v2.0 — Process overview |
| D15 | PFC/Imagination/Imagine-Final.md | 1,239 | v3.0 — Constructive simulation |
| D16 | PFC/Imagination/Imagine-Final-Evaluation.md | 2,501 | 3D framework |
| D17 | PFC/Imagination/Somatic-Articulation-Loop.md | 2,256 | Body → explicit |

**Phase D total: 17 files, ~17,076 lines**

---

### PHASE E — Feeling + Schema + Melody Lens

**Goal**: Observation interface + pattern recognition + metaphor system.
**Estimated sessions**: 8-11
**Pre-req**: Phase A-D complete

**E1. Feeling Core**

| # | Path | Lines |
|---|---|---|
| E01 | Feeling/Feeling.md | 1,788 | v3.0 — PFC=Lawyer integrated |
| E02 | Feeling/Feeling-Research.md | 1,705 |
| E03 | Feeling/Feeling-Mechanism-Deep-Draft.md | 1,325 |
| E04 | Feeling/Feeling-Sources-Draft.md | 1,244 |
| E05 | Feeling/Feeling-Accuracy-Draft.md | 1,485 |
| E06 | Feeling/Feeling-Chunk-Bridge-Draft.md | 446 |
| E07 | Feeling/Feeling-Literacy-Training-Draft.md | 1,500 |
| E08 | Feeling/Body-Knowing.md | 1,670 |

**E2. Feeling Drills**

| # | Path | Lines |
|---|---|---|
| E09 | Feeling/Drill-Feeling-Dev/Feel-Development.md | 358 |
| E10 | Feeling/Drill-Feeling-Dev/Feel-Example-Draft.md | 9,121 |
| E11 | Feeling/Drill-Feeling-Knowning/00-Reading-Notes.md | 1,337 |
| E12 | Feeling/Drill-Feeling-Knowning/01-Theme-A-Architecture.md | 412 |
| E13 | Feeling/Drill-Feeling-Knowning/02-Theme-D-Right-Wrong.md | 528 |
| E14 | Feeling/Drill-Feeling-Knowning/03-Theme-B-Verbal-Chain.md | 496 |
| E15 | Feeling/Drill-Feeling-Knowning/04-Theme-C-Ritual.md | 430 |
| E16 | Feeling/Drill-Feeling-Knowning/05-Theme-E-Empathy-Giving.md | 669 |
| E17 | Feeling/Drill-Feeling-Knowning/06-Theme-F-Logic-Feeling-Check.md | 336 |
| E18 | Feeling/Drill-Feeling-Knowning/99-Overview-Synthesis.md | 1,401 |

**E3. Schema**

| # | Path | Lines |
|---|---|---|
| E19 | Schema/Schema.md | 653 |
| E20 | Schema/Anchor-Schema.md | 1,522 |
| E21 | Schema/Anchor-Schema-Example.md | 767 |
| E22 | Schema/Anchor-Schema-Extreme-Example.md | 1,328 |

**E4. Melody Lens**

| # | Path | Lines |
|---|---|---|
| E23 | Melody Lens/Personal-Melody.md | 725 |
| E24 | Melody Lens/Personal-Melody-Example.md | 302 |
| E25 | Melody Lens/Melody-Arc.md | 584 |
| E26 | Melody Lens/Global-Melody.md | 436 |

**Phase E total: 26 files, ~32,568 lines**

---

### PHASE F — Body-Base Root

**Goal**: Integration files that tie Body-Base system together.
**Estimated sessions**: 4-5
**Pre-req**: Phase B-E complete (all sub-systems translated)

| # | Path | Lines | Note |
|---|---|---|---|
| F01 | Body-Base/Why-Body-Knows.md | 1,018 | v1.2 — Meta-question |
| F02 | Body-Base/Cortisol-Baseline.md | 2,716 | v2.1 — Amplifier + Yehuda HPA paradox |
| F03 | Body-Base/Valence-Propagation.md | 749 | v4.0 SPLIT — WHAT + HOW valence |
| F04 | Body-Base/Entity-Valence-Dynamics.md | 1,416 | ⭐ NEW: split from Valence v4.0 — per-entity |
| F05 | Body-Base/Body-Coupling.md | 2,270 | v3.0 REWRITE — 2D coupling model |
| F06 | Body-Base/Inter-Body-Mechanism.md | 1,196 | v2.0 — 8 principles, source of truth |
| F07 | Body-Base/Trust.md | 1,134 | ⭐ NEW: compiled prediction reliability |
| F08 | Body-Base/Body-Base.md | 1,254 | v3.4 — ENTRY POINT, last (refs 60+ files) |

**Phase F total: 8 files, ~11,753 lines**

---

### PHASE G — Observation Parameters

**Goal**: Named patterns emergent from chunk dynamics.
**Estimated sessions**: 5-7
**Pre-req**: Phase A-F complete (full Body-Base vocabulary)

**G1. Primitive**

| # | Path | Lines |
|---|---|---|
| G01 | Observation/Novelty.md | 776 |
| G02 | Observation/Threat.md | 842 |
| G03 | Observation/Boredom.md | 1,025 | v2.0 REWRITE |
| G04 | Observation/Drive.md | 600 |

**G2. Social**

| # | Path | Lines |
|---|---|---|
| G05 | Observation/Empathy.md | 2,309 | v4.0 REWRITE |
| G06 | Observation/Connection.md | 2,407 | v5.0 REWRITE |
| G07 | Observation/Status.md | 1,967 | v2.0 |
| G08 | Observation/Protect.md | 1,647 |

**G3. Higher-order**

| # | Path | Lines |
|---|---|---|
| G09 | Observation/Meaning.md | 1,612 | v2.0 |
| G10 | Observation/Autonomy-Hardware.md | 722 |
| G11 | Observation/Autonomy.md | 788 |
| G12 | Observation/Gratitude.md | 1,744 | v1.1 |
| G13 | Observation/Obligation.md | 2,038 |

**G4. Bridge / Tool**

| # | Path | Lines |
|---|---|---|
| G14 | Observation/Liking-Wanting.md | 947 | v2.0 |
| G15 | Observation/AI-Schema-Detection.md | 1,394 | v2.1 (absorbed update-draft) |
| G16 | Observation/AI-Collective-Detection.md | 568 | ⭐ NEW: collective-level ⑩-⑭ |

**Phase G total: 16 files, ~21,386 lines**

---

### PHASE H — Collective + Domain + Clarification

**Goal**: Group dynamics, external reality, framework divergences.
**Estimated sessions**: 5-6
**Pre-req**: Phase A-G complete

**H1. Collective**

| # | Path | Lines | Note |
|---|---|---|---|
| H01 | Collective/Collective-Body.md | 1,488 | v2.1 — Core mechanism |
| H02 | Collective/Coordination-Node.md | 1,782 | v1.2 — Resource allocation |
| H03 | Collective/Collective-Arc-Dynamics.md | 861 | v1.2 — Shelf-life |
| H04 | Collective/Collective-Purpose.md | 840 | v1.2 — Meta-level |
| H05 | Collective/Compliance-Floor.md | 643 | v2.1 — Governance |
| H06 | Collective/Collective.md | 625 | HUB — last |

**H2. Domain**

| # | Path | Lines |
|---|---|---|
| H07 | Domain/Domain.md | 554 | v2.0 FULL REWRITE |
| H08 | Domain/Conflict-Dynamics.md | 487 | v2.0 |
| H09 | Domain/Discovery-vs-Expansion.md | 825 |
| H10 | Domain/Knowledge-Flow.md | 540 |
| H11 | Domain/Domain-Mapping-Drive.md | 2,849 | v2.0 |
| H12 | Domain/Drill-Emergent-Pattern.md | 513 | v2.0 (shrunk ~50%) |

**H3. Clarification**

| # | Path | Lines |
|---|---|---|
| H13 | Clarification/Dopamine-Is-Not-Reward.md | 690 | v1.2 |
| H14 | Clarification/Prediction-Error-Is-Not-Reward.md | 481 |
| H15 | Clarification/Mirror-Neuron-Rejection.md | 362 |
| H16 | Clarification/Cortisol-Amplifier-Not-Cause.md | 363 |

**Phase H total: 16 files, ~13,903 lines**

---

### PHASE I — Research

**Goal**: Applied research + extensions. Files relatively independent.
**Estimated sessions**: 18-24
**Pre-req**: Phase A-H complete (full framework vocabulary)

**I1. Health-Conditions**

| # | Path | Lines |
|---|---|---|
| I01 | Health-Conditions/Hijack/Addiction-Analysis.md | 959 | v3.1 |
| I02 | Health-Conditions/Hijack/Alcohol-Brain-Mechanism.md | 754 |
| I03 | Health-Conditions/Hijack/Alcohol-Vietnam-Generational.md | 705 |
| I04 | Health-Conditions/Hijack/Nicotine-Brain-Mechanism.md | 887 | v1.1 |
| I05 | Health-Conditions/Neurodegeneration/Parkinson-Analysis.md | 1,258 | v1.1 |
| I06 | Health-Conditions/Neurodegeneration/Alzheimer-Analysis.md | 2,409 | v1.1 FULL REWRITE |
| I07 | Health-Conditions/OCD-Analysis.md | 1,269 | v2.2 |
| I08 | Health-Conditions/PTSD-Analysis.md | 2,160 |
| I09 | Health-Conditions/Neurodiversity/ADHD-Observation.md | 1,740 | v1.2 |
| I10 | Health-Conditions/Neurodiversity/Autism-Observation.md | 2,226 |
| I11 | Health-Conditions/Neurodiversity/ADHD-Trade-Off.md | 1,085 | ⭐ NEW |
| I12 | Health-Conditions/Neurodiversity/ADHD-Attention-Optimization.md | 995 | ⭐ NEW |

**I2. Love**

| # | Path | Lines |
|---|---|---|
| I13 | Love-Romantic.md | 2,607 | v3.0 REWRITE |
| I14 | Love-Unified.md | 2,071 | v2.0 REWRITE |

**I3. Global**

| # | Path | Lines |
|---|---|---|
| I15 | Global/Human-AI-Future.md | 775 | v3.0 FULL REWRITE |
| I16 | Global/AI-Self-Model.md | 1,233 | v2.0 |
| I17 | Global/Social-Calibration.md | 1,561 |
| I18 | Global/Uncanny-Valley.md | 1,210 |
| I19 | Global/Innovation-Geography.md | 947 |

**I4. Birth-Rate-Decline**

| # | Path | Lines |
|---|---|---|
| I20 | Global/Birth-Rate-Decline/00_Overview.md | 331 | v2.1 |
| I21 | Global/Birth-Rate-Decline/01_South-Korea_Analysis.md | 619 |
| I22 | Global/Birth-Rate-Decline/03_China_Analysis.md | 661 |
| I23 | Global/Birth-Rate-Decline/04_France_Analysis.md | 580 |
| I24 | Global/Birth-Rate-Decline/05_Finland_Analysis.md | 554 |
| I25 | Global/Birth-Rate-Decline/06_Israel_Analysis.md | 666 |
| I26 | Global/Birth-Rate-Decline/09_Vietnam_Analysis.md | 587 |
| I27 | Global/Birth-Rate-Decline/09_Vietnam_Solution.md | 443 |
| I28 | Global/Birth-Rate-Decline/100_Solutions.md | 437 | v1.1 |

**I5. Human-Learning**

| # | Path | Lines |
|---|---|---|
| I29 | Human-Learning/Child-Development/Child-Development-Mechanism.md | 2,500 |
| I30 | Human-Learning/Child-Development/Natural-Development.md | 2,253 | v2.0 |
| I31 | Human-Learning/Child-Development/Skill-Introduction.md | 2,044 | v2.0 |
| I32 | Human-Learning/Child-Development/Mother-Optimization.md | 2,213 | v2.0 |
| I33 | Human-Learning/Education-Mechanism/Education-Mechanism.md | 1,838 |
| I34 | Human-Learning/Education-Mechanism/Domain-Knowledge-Map.md | 831 |
| I35 | Human-Learning/Education-Mechanism/Expansion-Saturation-Crisis.md | 1,500 | v1.1 |
| I36 | Human-Learning/Education-Mechanism/Compile-Type-Learning.md | 1,264 |
| I37 | Human-Learning/Education-Mechanism/Connection-Education.md | 1,889 |
| I38 | Human-Learning/Education-Mechanism/Observation/Education-Arms-Race.md | 949 | v1.2 |
| I39 | Human-Learning/Education-Mechanism/Observation/Money-Education.md | 1,624 |

**I6. Remaining Research**

| # | Path | Lines |
|---|---|---|
| I40 | Money-Analysis.md | 1,476 |
| I41 | Climate-Cognition.md | 835 |
| I42 | Fidgeting-Analysis.md | 1,058 |
| I43 | Sensitivity-Classification.md | 253 |
| I44 | Self-Created-Threat.md | 743 |
| I45 | Relativity-Explained.md | 945 |
| I46 | Melody-Technology/Melody-Technology-Overview.md | 410 | v2.0 |
| I47 | Melody-Technology/Religion.md | 1,307 | v2.3 |
| I48 | Melody-Technology/Idol-Phenomenon.md | 798 | v2.1 |
| I49 | Melody-Technology/drill-religion-evidence.md | 869 | ⭐ NEW |
| I50 | Meta-Impact/Meta-Impact.md | 350 | v2.1 |
| I51 | Meta-Impact/Creator-Lens.md | 346 | v2.0 |
| I52 | Meta-Impact/Epistemological-Position.md | 420 | v2.0 |
| I53 | Mismatch-Patterns/Collective-Schema-Pressure.md | 615 |
| I54 | Neuro-Measurement/00-Goals.md | 128 |
| I55 | Neuro-Measurement/01-Implementation-Plan.md | 97 |

**I7. Quote-Analysis**

| # | Path | Lines |
|---|---|---|
| I56 | Quote-Analysis/Work-Adversity-Fear-Cluster.md | 878 |
| I57 | Quote-Analysis/Work-Chunk-Dependent-Visibility-Cluster.md | 673 |
| I58 | Quote-Analysis/Work-Comparison-Thief-Of-Joy.md | 917 |
| I59 | Quote-Analysis/Work-Goal-And-Why.md | 618 |
| I60 | Quote-Analysis/Work-Journey-Destination-Cluster.md | 714 |
| I61 | Quote-Analysis/Work-Move-Fast-Break-Things.md | 556 |
| I62 | Quote-Analysis/Work-Stay-Hungry-Stay-Foolish.md | 529 |
| I63 | Quote-Analysis/Work-Think-Act-Become-Cluster.md | 813 |

**I8. Drill-Sound-Brain** ⭐ NEW FOLDER

| # | Path | Lines |
|---|---|---|
| I64 | Drill-Sound-Brain/00-Overview.md | 367 |
| I65 | Drill-Sound-Brain/01-Sound-Brain-Neuroscience.md | 586 |
| I66 | Drill-Sound-Brain/02-Sound-Background-Pattern.md | 513 |
| I67 | Drill-Sound-Brain/03-Sound-Reward-Pipeline.md | 418 |
| I68 | Drill-Sound-Brain/04-Sound-Social-Resonance.md | 556 |
| I69 | Drill-Sound-Brain/05-Multi-Modal-Compound.md | 461 |
| I70 | Drill-Sound-Brain/06-Music-Architecture-Prediction.md | 908 |
| I71 | Drill-Sound-Brain/07-Music-Entrainment-Reward-Dynamics.md | 906 |
| I72 | Drill-Sound-Brain/08-Musical-Elements-Brain-Interface.md | 609 |
| I73 | Drill-Sound-Brain/09-Verification-Research.md | 777 |
| I74 | Drill-Sound-Brain/10-Synthesis.md | 529 |

**Phase I total: 74 files, ~73,612 lines**

---

### PHASE J — Applications

**Goal**: Practical implementations.
**Estimated sessions**: 3-4
**Pre-req**: Phase I complete (full research vocabulary)

**J1. Applications — Education System**

| # | Path | Lines |
|---|---|---|
| J01 | Applications/Education-System/00_Overview.md | 372 | v2.0 |
| J02 | Applications/Education-System/Education-System.md | 1,524 | v2.0 |
| J03 | Applications/Education-System/Hardware-Calibration.md | 1,618 |
| J04 | Applications/Education-System/Curriculum-Framework.md | 943 | v2.0 |
| J05 | Applications/Education-System/Era-Analysis-2025.md | 707 | v2.0 |

**J2. Applications — VN-specific**

| # | Path | Lines | Note |
|---|---|---|---|
| J06 | Applications/Education-System/Country/VN/VN-Education-Status.md | 1,306 | v2.0, heavy annotation |
| J07 | Applications/Education-System/Country/VN/VN-Cultural-Factors.md | 991 | v2.0, heavy annotation |
| J08 | Applications/Education-System/Country/VN/VN-Recommendations.md | 837 | v2.0, heavy annotation |

**Phase J total: 8 files, ~8,298 lines**

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

| Phase | Files | Lines | Sessions | Cumulative |
|---|---|---|---|---|
| A: Vocab + Core | 12 | 8,909 | 5-7 | 12 |
| B: Body-Feedback | 16 | 21,062 | 7-9 | 28 |
| C: Chunk + Agent + Drills | 49 | 42,325 | 13-17 | 77 |
| D: PFC | 17 | 17,076 | 6-9 | 94 |
| E: Feeling + Schema + Melody | 26 | 32,568 | 9-12 | 120 |
| F: Body-Base Root | 8 | 11,753 | 4-5 | 128 |
| G: Observation | 16 | 21,386 | 6-8 | 144 |
| H: Collective + Domain + Clarif | 16 | 13,903 | 4-6 | 160 |
| I: Research | 74 | 73,612 | 18-24 | 234 |
| J: Applications | 8 | 8,298 | 3-4 | 242 |
| K: File Index Regeneration | 3 | — | 1 | 245 |
| **TOTAL** | **245** | **~250,892** | **~76-102** | |

> **v4.0 note**: Line counts verified 2026-06-05 against actual files.
> Framework tinh gọn ~13% so với v3.0 (nhiều files rewrite/split) dù thêm 24 files mới.

---

## §4 — PROGRESS TRACKING

Format: [x] = done, [ ] = not started, [~] = in progress

### Phase A — Vocabulary + Core Architecture (12 files)
- [x] A01 Body-Feedback-Label.md
- [x] A02 PFC-Label.md
- [x] A03 README.md
- [x] A04 Core-Hardware.md
- [x] A05 Core-Software.md
- [x] A06 Ask-AI.md
- [x] A07 Neural-Architecture.md
- [x] A08 Neural-Processing-Flow.md
- [x] A09 Modality.md
- [x] A10 Blackbox-Map.md
- [x] A11 Reading-Roadmap.md ⭐
- [x] A12 Auditory-Hardware.md ⭐

### Phase B — Body-Feedback System (16 files)
- [x] B01 01-Foundation.md
- [x] B02 02-Dissonance.md
- [x] B03 03-Reward.md
- [x] B04 04-Integration.md
- [x] B05 Body-Feedback-Mechanism.md
- [x] B06 Body-Feedback-Precondition.md ⭐
- [x] B07 Gap-Direction.md
- [x] B08 Gap-Body-Need.md
- [x] B09 Gap-Distribution-Profile.md
- [x] B10 Reward-Signal-Architecture.md
- [x] B11 Dissonance-Signal-Architecture.md
- [x] B12 Reward-Calibration.md
- [x] B13 Action-Space.md
- [x] B14 Hidden-Quality-Perception.md
- [x] B15 Drill-Evolutionary-Sensor-Architecture.md
- [x] B16 Body-Feedback.md

### Phase C — Chunk System (49 files)
- [x] C01 Chunk.md
- [x] C02 Compile-Taxonomy.md
- [x] C03 Compile-Sleep.md ⭐
- [x] C04 Background-Pattern.md
- [x] C05 Entity-Compiled.md
- [x] C06 Self-Pattern-Modeling.md
- [x] C07 Entity-Access.md
- [x] C08 By-Product-Gap-Resonance.md
- [x] C09 Bond-Architecture.md
- [x] C10 Resonance-Sustainability.md
- [x] C11 Resonance-Per-Entity.md
- [x] C12 By-Product-Scale.md
- [x] C13 Entity-Access-Excess.md
- [x] C14 Entity-Access-Calibration.md
- [x] C15 Agent-Mechanism.md
- [x] C16 00-Chunk-System-Sketch.md
- [x] C17 01-PFC-Hardware-Reframe.md
- [x] C18 02-Womb-to-Birth-Baseline.md
- [x] C19 03-Visual-System-Arc.md
- [x] C20 04-Auditory-System-Arc.md
- [x] C21 05-Motor-Output-Arc.md
- [x] C22 06a-Interoceptive-Bladder-Keystone.md
- [x] C23 06b-Interoceptive-Other-States.md
- [x] C24 07-Social-Recognition-Arc.md
- [x] C25 08-Verbal-Production-Arc.md
- [x] C26 09-Event-Chunks-Inference-Matrix.md
- [x] C27 10-F1-Synthesis.md
- [x] C28 00-Internal-Mechanism-Overview.md
- [x] C29 01-Chunk-Connection-Logical.md
- [x] C30 01b-Chunk-Activation-Dynamics.md
- [x] C31 01c-Chunk-Discovery-Lifecycle.md
- [x] C32 02-Feeling-Intuition-Gradient.md
- [x] C33 03-Chain-Anchor-Decay.md
- [x] C34 04-Right-Wrong-Vague.md
- [x] C35 05-Insight-Tacit-Upgrade.md
- [x] C36 06-Internal-Synthesis.md
- [x] C37 00-External-Mechanism.md
- [x] C38 01-External-Synthesis.md
- [x] C39 02-Cross-Network-Transfer.md
- [x] C40 01-Natural-Language-Architecture.md
- [x] C41 02-Mathematical-Language-Architecture.md
- [x] C42 03-Musical-Notation-Architecture.md
- [x] C43 04-Visual-Diagram-Architecture.md
- [x] C44 05-Programming-Language-Architecture.md
- [x] C45 09-Learning-Cycle.md
- [x] C46 99-Master-Synthesis.md
- [x] C47 Drill-Body-Base-Boundary-Spectrum.md ⭐
- [x] C48 Drill-Neural-Bilateral-Architecture.md ⭐
- [x] C49 Drill-Agent-Feed-Channel.md ⭐

### Phase D — PFC System (17 files)
- [x] D01 PFC-Function.md
- [x] D02 PFC-Hardware.md
- [x] D03 PFC-Configuration.md
- [x] D04 PFC-Development.md
- [x] D05 PFC-Hold-Dimensions.md
- [x] D06 Attention-Spectrum.md
- [x] D07 Simulation-Engine.md
- [x] D08 PFC-Operations.md
- [x] D09 Logic-Feeling.md
- [x] D10 Logic-Planning.md
- [x] D11 Logic-Feeling-Balance.md
- [x] D12 Logic-Feeling-Failure-Examples.md
- [x] D13 Self-Observation.md ⭐
- [x] D14 Imagination.md
- [x] D15 Imagine-Final.md ⭐
- [x] D16 Imagine-Final-Evaluation.md ⭐
- [x] D17 Somatic-Articulation-Loop.md ⭐

### Phase E — Feeling + Schema + Melody (26 files)
- [x] E01 Feeling.md ⭐
- [x] E02 Feeling-Research.md
- [x] E03 Feeling-Mechanism-Deep.md
- [x] E04 Feeling-Sources.md
- [x] E05 Feeling-Accuracy.md
- [x] E06 Feeling-Chunk-Bridge.md
- [x] E08 Body-Knowing.md (translated out of order — source was fully read previous session)
- [x] E07 Feeling-Literacy-Training.md
- [x] E09 Feel-Development.md
- [~] E10 Feel-Example-Draft.md (IN PROGRESS — §1 E1-E10 done; §2-§15 continue next session)
- [ ] E11-E18 Feeling Drills (8 files remaining)
- [ ] E19-E22 Schema (4 files)
- [ ] E23-E26 Melody Lens (4 files)

### Phase F — Body-Base Root (8 files)
- [ ] F01-F03 Why-Body-Knows + Cortisol + Valence
- [ ] F04 Entity-Valence-Dynamics.md ⭐
- [ ] F05-F06 Body-Coupling + Inter-Body
- [ ] F07 Trust.md ⭐
- [ ] F08 Body-Base.md (ENTRY POINT — last)

### Phase G — Observation Parameters (16 files)
- [ ] G01-G04 Primitive (4 files)
- [ ] G05-G08 Social (4 files)
- [ ] G09-G13 Higher-order (5 files)
- [ ] G14-G15 Bridge (2 files)
- [ ] G16 AI-Collective-Detection.md ⭐

### Phase H — Collective + Domain + Clarification (16 files)
- [ ] H01-H06 Collective (6 files)
- [ ] H07-H12 Domain (6 files)
- [ ] H13-H16 Clarification (4 files)

### Phase I — Research (74 files)
- [ ] I01-I12 Health-Conditions (12 files, +2 ADHD new ⭐)
- [ ] I13-I14 Love (2 files)
- [ ] I15-I19 Global (5 files)
- [ ] I20-I28 Birth-Rate-Decline (9 files)
- [ ] I29-I39 Human-Learning (11 files)
- [ ] I40-I55 Remaining Research (16 files, +1 drill-religion ⭐)
- [ ] I56-I63 Quote-Analysis (8 files)
- [ ] I64-I74 Drill-Sound-Brain (11 files) ⭐ NEW FOLDER

### Phase J — Applications (8 files)
- [ ] J01-J05 Education System (5 files)
- [ ] J06-J08 VN-specific (3 files)

### Phase K — File Index Regeneration (3 files)
- [ ] K01-K03 File-Index ×3

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
| Feel-Example-Draft.md | 9,121 | May need multiple sessions |
| Domain-Mapping-Drive.md | 2,849 | Deep cross-references |
| Cortisol-Baseline.md | 2,716 | Medical terminology |
| Love-Romantic.md | 2,607 | v3.0 — test case for entire framework |
| Imagine-Final-Evaluation.md | 2,501 | Complex 3D framework |
| Connection.md | 2,407 | v5.0 — many dependencies |
| Alzheimer-Analysis.md | 2,409 | v1.1 — heavy medical content |
| Empathy.md | 2,309 | v4.0 — ~20 dependencies |
| Body-Coupling.md | 2,270 | v3.0 REWRITE |
| Somatic-Articulation-Loop.md | 2,256 | Nuanced body-knowledge |
| PTSD-Analysis.md | 2,160 | Context-tag model |
| Autism-Observation.md | 2,226 | Heavy research content |

### §6.2 v4.0 Changes vs v3.0

- **Source of truth**: global-index.json (was manual count)
- **Public-Plan SKIP**: không dịch (user decision 2026-06-05)
- **+24 files mới**: framework đã mở rộng đáng kể (Trust, Self-Observation, Compile-Sleep, Drill-Sound-Brain, ADHD extensions, AI-Collective-Detection, etc.)
- **-10 files removed**: README → kept anyway, AI-Schema-Detection-update-draft → merged, pending-quotes → tracking file, Public-Plan ×4, File-Index ×3 → Phase K riêng
- **Framework tinh gọn ~13%**: nhiều files rewrite/split → lines giảm dù files tăng
- **Line counts VERIFIED**: all 240 files counted via PowerShell 2026-06-05

### §6.3 Ordering may adjust

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

### §9.1 Terminology — Use 00-Glossary.md as source of truth

- Verify all framework terms against Glossary before writing ANY section
- Use EXACT canonical form (capitalization, hyphenation, phrasing)
- Use full concept names — only abbreviations already in source are OK
- Missing term → flag it, propose English rendering, add to Glossary

### §9.2 Content — Preserve 100%

- Every bullet point, table row, warning, highlight → preserved
- Quantitative claims preserved exactly: "~95%", "40→200h", "4±1"

### §9.3 Structure — Preserve exactly

- § numbers, 🟢🟡🔴 confidence markers, version numbers, file paths, citations, tables, code blocks, emoji markers

### §9.4 What you may change

- Vietnamese narrative → natural English prose
- Vietnamese examples → English equivalents or keep + annotate (§11)
- Section titles → English (keep §numbers)
- Merge short Vietnamese sentences into flowing English
- Brief contextual additions for non-Vietnamese readers

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

## §15 — QUALITY CHECKLIST (per file)

Verify after completing each file:

1. All framework terms match 00-Glossary.md exactly
2. Full concept names used throughout
3. YAML header follows §10.1 template
4. Every bullet, table row, warning, ⚠️, blockquote from source → present
5. §numbers, 🟢🟡🔴, versions, file paths, citations → unchanged
6. Code block structure and ASCII alignment preserved
7. Vietnamese CAPS emphasis → English CAPS preserved
8. Framework's assertive tone preserved
9. Vietnamese cultural examples handled per §11 categories
10. "Mainstream → Framework" contrasts preserved
11. Natural English flow (reads as originally written in English)

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
