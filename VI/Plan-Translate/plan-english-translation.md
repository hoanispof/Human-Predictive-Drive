# English Translation — Master Plan + Methodology

> **Version**: 5.0
> **Created**: 2026-05-26
> **Updated**: 2026-06-08 (v5.0 — FRESH START: retranslate from scratch for max quality)
> **Status**: ACTIVE — FRESH START
> **Supersedes**: v4.0 (2026-06-05)
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

**Decision**: Giữ NGUYÊN tên file — EXACT match với source, bao gồm `-Draft` suffix và `drill-*` prefix.

**Lý do**: Cross-references dùng file names. Giữ nguyên = links work tự nhiên. Không rename, không drop suffix.

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
| C47 | Drill-Chunk/Drill-Neural-Bilateral-Architecture.md | 264 | ⭐ NEW |
| C48 | Drill-Chunk/Drill-Agent-Feed-Channel.md | 901 | ⭐ NEW |

> ⚠️ **Drill-Body-Base-Boundary-Spectrum.md** — moved to Phase G (G00).
> Reason: conceptually depends on Body-Base.md §2 (F08), Entity-Valence-Dynamics (F04),
> Body-Coupling (F05) as foundational premises — all Phase F files.
> Must translate AFTER Phase F complete for terminology consistency.

**Phase C total: 48 files, ~41,152 lines**

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
**Estimated sessions**: 6-8
**Pre-req**: Phase A-F complete (full Body-Base vocabulary)

**G0. Body-Base × Chunk Boundary Drill** *(moved from Phase C — requires Phase F vocabulary)*

| # | Path | Lines |
|---|---|---|
| G00 | Drill-Chunk/Drill-Body-Base-Boundary-Spectrum.md | 1,173 | ⭐ Moved from C — needs F04/F05/F08 |

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

**Phase G total: 17 files, ~22,559 lines**

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
| C: Chunk + Agent + Drills | 48 | 41,152 | 13-16 | 76 |
| D: PFC | 17 | 17,076 | 6-9 | 93 |
| E: Feeling + Schema + Melody | 26 | 32,568 | 9-12 | 119 |
| F: Body-Base Root | 8 | 11,753 | 4-5 | 127 |
| G: Observation | 17 | 22,559 | 6-8 | 144 |
| H: Collective + Domain + Clarif | 16 | 13,903 | 4-6 | 160 |
| I: Research | 74 | 73,612 | 18-24 | 234 |
| J: Applications | 8 | 8,298 | 3-4 | 242 |
| K: File Index Regeneration | 3 | — | 1 | 245 |
| **TOTAL** | **245** | **~250,892** | **~76-102** | |

> **v4.0 note**: Line counts verified 2026-06-05 against actual files.
> Framework tinh gọn ~13% so với v3.0 (nhiều files rewrite/split) dù thêm 24 files mới.

---

## §4 — PROGRESS TRACKING

> ⚠️ **v5.0 FRESH START — 2026-06-08**
> Starting from zero. Every [x] below = translated in THIS fresh run.

Format: [x] = done, [ ] = not started, [~] = in progress

---

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
- [x] C47 Drill-Neural-Bilateral-Architecture.md ⭐
- [x] C48 Drill-Agent-Feed-Channel.md ⭐

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
- [x] E03 Feeling-Mechanism-Deep-Draft.md
- [x] E04 Feeling-Sources-Draft.md
- [x] E05 Feeling-Accuracy-Draft.md
- [x] E06 Feeling-Chunk-Bridge-Draft.md
- [x] E07 Feeling-Literacy-Training-Draft.md
- [x] E08 Body-Knowing.md
- [x] E09 Feel-Development.md
- [x] E10 Feel-Example-Draft.md ✅ full rewrite (124 examples E1–E116 + E117–E124 §9b drive chunks; all 9 required fields consistent; §0–§15 complete; 2026-06-09)
- [x] E11 00-Reading-Notes.md ✅ (Drill-Feeling-Knowning/; §1 notes from 13 source files; §2 cross-theme mapping 6 themes; §3 RQ1–RQ21; §4 status; 2026-06-09)
- [x] E12 01-Theme-A-Architecture.md ✅ (Drill-Feeling-Knowning/; §0–§6; 5 sub-questions answered; expanded Tier 2 architecture; Body-First Invariant + bidirectional flow; 7-Q open questions table; 2026-06-09)
- [x] E13 02-Theme-D-Right-Wrong.md ✅ (Drill-Feeling-Knowning/; §0–§6; 8 sub-questions answered; 4 cases: infant VoE/Einstein/scientist/partner; gradient 4 dimensions; compiled not random; 2026-06-09)
- [x] E14 03-Theme-B-Verbal-Chain.md ✅ (Drill-Feeling-Knowning/; §0–§6; 6 sub-questions; anchor hypothesis CORRECT; plan before verbal ~2Myr; verbal one enabler among several; 2026-06-09)
- [x] E15 04-Theme-C-Ritual.md ✅ (Drill-Feeling-Knowning/; §0–§6; ritual=multi-layered compile mechanism; 5 layers behavioral+contextual+emotional+social+symbolic; all 3 candidates partial; compile combo EXTREMELY POWERFUL; Göbekli Tepe ~11,600 BP; schema classification flip agent↔object; modern ritual decline=anchor crisis; 6 open questions C-Q1–C-Q6; 2026-06-09)
- [x] E16 05-Theme-E-Empathy-Giving.md ✅ (Drill-Feeling-Knowning/; §0–§6; empathy=Resonance output; thiện cảm=affinity compound positive valence; joy/discomfort 4 sub-cases; mango vs banana case different mechanisms; giving freely=broader schema trust; 7 open questions E-Q1–E-Q7; 2026-06-09)
- [x] E17 06-Theme-F-Logic-Feeling-Check.md ✅ (Drill-Feeling-Knowning/; §0–§6; integration check PASSED; Logic-Feeling consistent with all A-E themes; RQ19 resolved=2 tracks 1 observer; 5 minor updates suggested; all 6 themes complete; 2026-06-09)
- [x] E18 99-Overview-Synthesis.md ✅ (Drill-Feeling-Knowning/; §0–§10 + statistics; 1,884-line source; 10 meta-insights (body-first invariant/~95/5 split/unified pattern-match/multi-channel convergence/bidirectional architecture/positive-negative trust/compiled dominance/3 tiers across species/user intuitions 92% accurate/framework evolution); 34+ questions consolidated; 23 open question groups U1–U23; 5 minor updates + 3 architectural decisions; 6 practical application sections; Drill-Feeling-Knowning set COMPLETE (6 themes + overview); 2026-06-09)
- [x] E19 Schema.md ✅ (Schema/; §0–§11; v2.0 reframe: schema=observation parameter NOT component; chunk=atom/schema=molecule analogy; software feature analogy; 4 values (descriptive/predictive/communicative/navigational); 4 observable properties (depth gradient/activation states/decay+reactivation/cross-contamination); schema×body-feedback (no negative schemas/override spectrum/novelty-vs-threat/overflow point); schema×PFC (best guess/orchestration/cannot analyze precisely); schema×domain (Base→Shift→Check universal); body baseline state mechanism; 4 open questions; "a compass not a GPS"; 2026-06-09)
- [x] E20 Anchor-Schema.md ✅ (Schema/; §0–§7 + closing quote; 1,881-line source; Anchor-Schema=unconscious REQUIREMENT for sync point (bottom-up) vs Imagine-Final=PFC product (top-down); 6-step flow ①dissonance→②compiled scan→③PFC imagine→④body evaluate→⑤anchor amplify→⑥domain feedback; STEP ② MOST IMPORTANT ~80% compiled; multi-scale anchors micro→life; Trust=binding force; Anchor Strength 3 levels; Trust≥Cost→holds; 3 independent dimensions Clarity×Quality×Trust; positive trust (opioid "hard but worth it") vs negative trust (cortisol relief "phew escaped it"); 4 sources fill: ①PFC Imagine-Final/②Hippocampus/③Compiled ~80%/④External Inject; External inject 4 mechanisms: repetition/ritual/emotional peak/social; Religion=FULL COMBO inject; 3 tiers across species Tier 0 Reactive/Tier 1 Simulated/Tier 2 Directed; "Fish do NOT have midlife crises — the price of PFC"; historical trajectory prehistoric→agricultural→modern maximum complexity; social media=anti-anchor machine; 3 levels missing anchor: Level 1 Weak/Level 2 Missing/Level 3 Conflict (WORST); Level 3 most common in modern society; self-knowledge=most important skill; 2026-06-09)
- [x] E21 Anchor-Schema-Example.md ✅ (Schema/; COMPLETE healthy spectrum 20 examples; M1-M5 micro/S1-S5 short/D1-D5 medium/L1-L5 long/X1-X5 special; annotation key: anchor/trust/strength/cost/domain/source/outcome; 7 cross-spectrum patterns: Trust≥Cost→holds / Faint→Build→Compiled trajectory / trust invisible until broken / domain verifiability→stability / empathy-driven anchor sub-type / Trust Gap most dangerous period / Hardware-First Harm (see extreme file); "unfalsifiable trust = HIGH as arithmetic but opposite reason"; "semi-real = weakest trust"; refers to Anchor-Schema-Extreme-Example.md for over-zone; 2026-06-09)
- [x] E22 Anchor-Schema-Extreme-Example.md ✅ (Schema/; 1,647-line source; Hardware-First Harm=anchor PRIORITIZES hardware smoothness OVER domain reality; Yerkes-Dodson analog for anchor strength (too little=cacophony, too much+domain skipped=harm); COMPLETE INVERSE of Mismatch (body✓/warning✗/exit hard vs body✗/warning✓/exit possible); 5 domain check fail mechanisms: ①Reframe/②Dismiss/③Isolate/④Postpone/⑤Counter-Evidence Bias (all 5 appear simultaneously = "layered defense"); 5 conditions for formation: ①Multi-channel reward/②Compiled deep/③Domain unfalsifiable or semi-real/④Exit cost extreme/⑤External reinforcement; Y1 Cult: 5/5 conditions ALL STRONG + 6 reward channels + Source④ full combo = ENGINEERED Hardware-First; Y2 Threat loop mother-child: HYBRID Hardware-First(mother)+Mismatch(child); empathy-driven anchor MISDIRECTED; VN/Asia context; Y3 Gaming: 4 body-base channels (novelty/mastery/connection/status) simultaneously; engineered by game design; WHO ICD-11 2018; Y4 Limerence: EGO-DYSTONIC; OCD-like serotonin shift (Marazziti 1999 ↓40%); trauma bonding; intermittent reinforcement; 7+ exit attempts average; Hardware-First+ego-dystonic HYBRID; Y5 Workaholism: ZERO stigma/ZERO warnings (society PRAISES); karoshi/burnout/CVD citations; "I'm fine feeling=body smooth from anchor"; BEST-DISGUISED harm; Y6 Substance: CHEMICAL PATHWAY different from Y1-Y5 (schema-mediated vs direct receptor activation); supraphysiological dopamine; receptor downregulation; physical dependency layer; 4-layer exit: Detox+MAT+CBT+Social; "cold turkey willpower USUALLY FAILS"; addiction=medical condition not moral failing; §3 Dose-dependent: 4 zones Healthy/Borderline/Dependent/Extreme; 5 mechanisms dose curve; 4 threshold signals (Replacement/Body Override/Social Concern/Reflection Ability); "frog in boiling water" pattern; §4 cross-pattern: stigma vs warning table (Y5 ZERO warning key); ego-syntonic vs dystonic (Y4+Y6 hybrid=opening for help); schema-level vs chemical-level; §5 disclaimers: framework provides AN ANGLE OF VIEW not clinical diagnosis; 2026-06-09)
- [x] E23 Personal-Melody.md ✅ (Melody Lens/; 923-line source; Melody=METAPHOR for emergent chunk-network state (observation parameter, not architecture component); metaphor→mechanism mapping table (notes/instruments/harmony/dissonance/tempo/key/earworm/conductor); §1 Start Melody hardware profile: DRD4×COMT×Capacity×Modality×Body-base×Efference precision; §2 Multi-modal sync = "beautiful/feels amazing" = opioid; gamma synchronization (Buzsáki 2006); §3 "Taste" = personal chunk pattern match; guilty pleasure = 2 obs parameters conflict simultaneously; §4 Two-axis tension: Body-base pull (smooth) vs Domain pull (adapt) = LIFELONG; approach/avoidance tag at compile time; cortisol=amplifier NOT tag source; §5 "Good melody" 4 criteria: smooth on OWN hardware + maps domain accurately + broadly + sustainably; passion = both forces aligned; motivation bridge 5 types → remove bridge when intrinsic ready → overjustification risk; §6 Imagine-Final = compass; unconscious 95% / PFC 5%; without compass=drifts; wrong compass=builds wrong; §7 Arc dynamics: wave pattern peak/trough; each trough higher than last; paradox smooth+sees more dissonance; lifetime trajectory U-curve; §8 5 equilibrium profiles: ①Never enough/②Enough+Stop/③Enough+Keep Going/④Enough+Share/⑤Infinite Horizon; §9 Predicting others via Self-Pattern-Modeling: 3 overlap layers species/culture/personal; "crooked ruler" blind spot; judgmental=lazy template building; §10 Difficulty vs Mismatch: opioid pathway (build) vs relief pathway (consume); ~60-70% some mismatch; 2026-06-09)
- [x] E24 Personal-Melody-Example.md ✅ (Melody Lens/; 358-line source; 3 profiles = 3 PHASES not 3 types of people; notation ♩♫♯! preserved; §1 Stable Center: smooth/approach-dominant; Boredom risk at midlife; §2 Center+Sprint Arc: self-chosen arc→approach tag; arc compile=PERMANENT asset; chunks from failed arc NOT LOST transfer to next; body-base maintenance critical; §3 Disruption Imposed: divorce/economic downturn/illness examples; imposed→no efference copy→avoidance tag risk; recovery path = connection (social buffer) + time; post-traumatic growth possible; §4 comparison table 3 profiles + universal lessons + phase-specific: connection first in disruption; KEY INSIGHT: §2 vs §3 same dissonance DIFFERENT tag because AUTONOMY decides; 2026-06-09)
- [x] E25 Melody-Arc.md ✅ (Melody Lens/; 750-line source; Arc=build cycle smooth→dissonance→smooth (key change metaphor F#/Bb→G major); WHY arcs have dissonance: PFC smooth job/body conservative/domain demands adapt/compile threshold/cortisol amplifier; §2 Chunk dynamics in arc: Gap(start)→Miss(Valley)→Shift(resolve); approach arc vs avoidance arc = HOW you teach determines TAG; §3 9 design principles: Imagine-Final prereq/chunk order/compile threshold/bridge trust/real-check GPS/delusion trap/survivorship bias/hardware variation; §4 Arc shapes: single/long; THE VALLEY = most dangerous point; §5 6 optimization techniques: ①Anchor First/②Mini-Arc(3-7 chunks)/③Real-Check Intervals(after mini-compile NOT at peak)/④Social Mirror(show process not just result)/⑤Progress Markers/⑥Body-Base Maintenance(paradox more effort=worse result); §6 7-step observer protocol; §7 7 failure modes including avoidance tag failure; §8 3 examples child/dev/CEO; 2026-06-09)
- [x] E26 Global-Melody.md

### Phase F — Body-Base Root (8 files)
- [x] F01 Why-Body-Knows.md
- [x] F02 Cortisol-Baseline.md
- [x] F03 Valence-Propagation.md
- [x] F04 Entity-Valence-Dynamics.md ⭐
- [x] F05 Body-Coupling.md
- [x] F06 Inter-Body-Mechanism.md
- [x] F07 Trust.md ⭐
- [x] F08 Body-Base.md (ENTRY POINT — last in sub-system)

### Phase G — Observation Parameters (17 files)
- [x] G00 Drill-Body-Base-Boundary-Spectrum.md ⭐ (moved from Phase C — needs F04/F05/F08)
- [x] G01 Novelty.md
- [x] G02 Threat.md
- [x] G03 Boredom.md
- [x] G04 Drive.md
- [x] G05 Empathy.md ✅ (Observation/; §0–§11 + closing metaphor; empathy=observable output Self-Pattern-Modeling Compiled+❸ positive; Connection⊃Empathy; 2-stream Valence-Momentary+Valence-Structural; burnout reframe Compiled-Suppress+PFC depletion; VS strong+Compiled weak parent case; 3-layer calibration; AI lacks body→no real empathy; 2026-06-09)
- [x] G06 Connection.md ✅ (Observation/; §0–§18; Connection=❶Hardware×❷Self-PM×❸Valence; 3 Generative Primitives; 8 valence chain pathways; 2-Stream Architecture Hardware+Modeling; Resonance Decline 2 Forces+1 Fuel; 4-Layer Sustainability; Phantom 4-factor; Gap Clone Impossible; 4 loneliness types; Entity-Access gradient; "absence makes the heart grow fonder" 3-mechanism; Compilable Architecture Social=Requirement; 2026-06-09)
- [x] G07 Status.md ✅ (Observation/; §0–§17; Status=Resource Access Map (not hierarchy); 3 Interaction Modes Take/Exchange/Comply; Compilable Architecture status=emergent; Compiled/Fresh scan; Disruption Cycle 3 scenarios A/B/C; Position vs Aspiration; Serotonin=Certainty Bias candidate; Serotonin Ratchet easy-up/hard-down; PFC=Lawyer 3 distortion modes; Chunk-Shift/Miss/Gap mapping; Status=meta-parameter; Military case study; "Successful but empty" multi-causal 5 causes; Being Seen + Belonging; Conflict at scale OVERLAP×SCARCITY×COMMITMENT; 2026-06-09)
- [x] G08 Protect.md ✅ (Observation/; §0–§11; Protect=emergent observation parameter (not instinct); Ownership Chunks=compiled baseline; Loss Aversion asymmetric ~2×; f(replaceability×attachment) formula; Spectrum object→person→idea→identity; Compiled/Fresh Protect; Vasopressin defense-side; Endowment Effect; Sunk Cost=protect pattern; Gap→Miss Transition for protect; Compound devastating loss table; Giving=natural counterweight via Mirror Reward Override; Compassion Fatigue=self-protect; Backfire Effect=idea protect; Healthy vs Toxic 5 patterns each; Cultural schemas; 2026-06-09)
- [x] G09 Meaning.md ✅ (Observation/; §0–§11; Meaning=life-level Anchor-Schema body-accepted; 5 anchor types GOAL/STATE/IDENTITY/FAITH/ROLE; 3 failure modes Absent/Exhausted/Disrupted; 4 anchor sources PFC-Imagine-Final/Compiled-Experience/External-Inject/Hippocampus; Frankl Logotherapy 3 routes; Age gradient teens→retirement; Self-help critique 4 problems; Meaning≠Boredom≠Burnout≠Depression differential; Domain=Arbiter meaning-can-be-wrong; Compilable Architecture → meaning emergent; 10 cases verified; Gratitude×Meaning 🔴 open; AI era Q6; 2026-06-09)
- [x] G10 Autonomy-Hardware.md ✅ (Observation/; §0–§7; Autonomy-Hardware=emergent-from-architecture; Efference-copy+VTA-prediction-delta+Opioid → self-action=reward; vmPFC+DRN controllability-learning Maier-Seligman-2016 reversed; Cortisol-direction-tag compile-time-lock Novelty-vs-Threat; Path-A-opioid vs Path-B-relief; 2-layer-dissonance prediction-override+controllability-loss; Entity-Access×vmPFC; Hardware-Subsidy×autonomy compound; 2026-06-09)
- [x] G11 Autonomy.md ✅ (Observation/; §0–§7; Autonomy-Software=chunk-accumulation; Motor-Chunks→Self-as-Agent-Meta-Chunk→"NO!"-generalization; 5-phase developmental arc 0-18m+adult; vmPFC domain-specific controllability; 3 counterweights chunks/choice-overload/structure; ×Protect×Threat×Status×Connection×Novelty×Meaning×Mastery; 5 healthy/5 pathological; Entity-Access×Simulation-Engine; cultural collectivism/individualism; AI-era Q4; 2026-06-09)
- [x] G12 Gratitude.md ✅ (Observation/; §0–§11; Gratitude=Tier-5-most-integrative-9-components; Body-Feedback-Precondition+PFC-Comparison+Source-Attribution+Self-Pattern-Modeling+Entity-Compiled+Obligation+Autonomy+❸-update; 3-anti-habituation: Variation+Comparison+Ritual; Baseline-Shift+SNC; Gift-Obligation spectrum; 5-chains-for-speaker; Type-A/B/C gratitude; Gratitude-O(1); Cross-channel-exploitation; 4-chunk-types; 2-tier-calibration; 2026-06-09)
- [x] G13 Obligation.md ✅ (Observation/; §0–§13; Obligation=compiled-prediction-ongoing-cost-maintain-agent-access; 5-factor-formula: Agent_value×Repl⁻¹×Cost_clarity⁻¹×Autonomy⁻¹×Endpoint⁻¹; Status-Gap-Multiplier; 6-type-spectrum: Financial/Exchange/Social-debt/Role/Identity/Compound; 3-independent-mechanisms: Obligation+Valence-Structural-buffer+Self-Pattern-Modeling; Access-Cost; O(1)-community-scaling; 3-cost-model; 2026-06-09)
- [x] G14 Liking-Wanting.md ✅ (Observation\; §0–§7; BRIDGE-FILE-not-framework-tool; wanting=6-mechanisms: Imagine-Final-Preview+VTA-Dopamine-Alert+Compiled-Schema-Momentum+Anchor-Schema-Binding+Valence-Chain-Propagation+Self-Generated-Threat; liking=5-layers: Body-Base-Opioid+5-Body-Feedback-Preconditions+Chain-Mediated+3-Body-Signals+Evaluative-vs-Direct-State-Reward; E0-E3-gradient; 5-cases: rat+gambling+TikTok+Jensen-Huang+Einstein-altruism-studying; 5-reasons-framework-no-use-wanting-liking; 2026-06-09)
- [x] G15 AI-Schema-Detection.md ✅ (Observation\; §0–§10; GATEWAY-FILE-practical-entry-point; 3-layer-model: AI-detect+Expert-feel-check+Client-self-verify; 2-layer-simplified: AI+Self-mild-cases; 9-AI-capabilities: ①verbal-tracking+②schema-cluster+③contradiction-detect+④chain-hypothesis+⑤compile-type-Experience/Expertise/Trust+⑥chunk-depth-inference+⑦elicit-hidden-schemas+⑧collective-chain-break+⑨3-level-tagging; Self-Drill-Mode; AI-Trust-Guardrails: cross-domain+speed-gap+systemic-bias; 5-step-process; 2026-06-09)
- [x] G16 AI-Collective-Detection.md ⭐ ✅ (Observation\; §0–§9; COMPANION-to-AI-Schema-Detection; collective-capabilities-⑩-⑭: ⑩Arc-Shift+Scale-Diagnosis-3-expired-sources+4-level-scale; ⑪Coordination-Node-Assessment: fail/authority-schema/mismatch; ⑫Collective-Schema-Pressure: compound-multiplicative+culture-aware; ⑬Gap-Distribution×Collective-Matching: 4-axes; ⑭Collective-Level-Verification: match-method-to-scale; Step-0-collective-check-before-individual; 4-collective-guardrails; 2026-06-09)

### Phase H — Collective + Domain + Clarification (16 files)
- [x] H01 Collective-Body.md ✅ (Collective\; §0–§10; 3-Level-Model-Individual→Collective→Framework; Compilable-Architecture-requirement-4-reasons; 4-compile-pathways-same-output; §2.5-Individual-Detect-Collective-Gap-5-step+4-cases+Rush-lifecycle; By-Product-Match-3-scales: Scale-Pair/Scale-Hub/Scale-Institutional; Dual-Pull-Propagation-human-designed-systems: software+law+medicine+org; Global-Body-analogy-70%-30%; Trust=only-bridge+5-external-install+PFC=Lawyer-collective; Chain-break-3-types; Trust-Hijack: brand+cross-domain+public-callout; Compilation-Source-Match-3-layer-guilt; System-Compilation-6-mechanisms; Valence-Structural-vs-System-Compilation-comparison; 3-proxy-types: Leader/Symbol/Virtual-Agent; AI-7th-trust-entity: cross-domain-default+install-compile-gap+systemic-bias; Technology×Scale-Interaction-frontier-shift; 2026-06-09)
- [x] H02 Coordination-Node.md ✅ (Collective\; §0–§11; STATUS≠TALENT≠CONTRIBUTION-3-independent-dimensions; Node=Partial-PFC-for-collective; 2-Routes: Dominance-forced-resonance-relief-tag vs Prestige-genuine-resonance-opioid; Prestige=human-specific-via-Compilable-Architecture; 5-Capabilities: Self-Pattern-Modeling-across-domains+Gap-Detection+PFC-Bandwidth+Uncertainty-Tolerance+Trust-Cascade-Building; 2-Chunk-Types: Meta-People-core+Scaffold-Domain-threshold; Mother=first-coordination-node-maps-all-5-capabilities; Node-dual-nature-VEHICLE+ROAD; 5-Phases-emergence: Detect→First-Followers→Trust-Cascade→Scale-Transition→Lock/Recalibrate; 3-Scale-Maps: Personal/Role/Symbolic; Owner-vs-Leader-3-configurations; Emergence≠Effectiveness-4-cases; Peter-Principle-empirical-Benson-2019-N38843; Hereditary-penalty-Pérez-González-Bennedsen; Institutional-checks-compensate-Ottinger-2025; 3-tier-compile-model: Scaffold→Experience→Expertise; Gabarro-1987-24-36-months; Satisficing-Simon-1956; 3-failure-modes; Evolution-5-stages; Hardware-Subsidy-Per-Scale: oxytocin→serotonin→trust-infrastructure; 2026-06-09)
- [x] H03 Collective-Arc-Dynamics.md ✅ (Collective\; §0–§9+NewConcepts; 3-Constraint-Sources: Physics/Body/Collective; Dependency-Ratio→Shelf-Life; Inverted-Hierarchy-experience-vs-ontology; Eisenberger-2003; 4-factors-arc-stability: Grounding+Mass+FeedbackSpeed+Disruption; Snapshot-of-arc; 4.3-lifecycle-5-phases; 4.4-acceleration; §4.5-Scale-dependent-4-levels: Shift/Disruption/NodeDeath/ArcExtinction; WWII-acceleration; True-but-Unnecessary-distinct-from-Expired/Wrong/OptimizationOverride; Value=skill-minus-baseline; §6-implications: LayeredStrategy+DualCheck-scales-with-dependency; Bond-Architecture×Arc+Resonance-Sustainability×Arc+By-Product-Scale×Arc; 2026-06-09)
- [x] H04 Collective-Purpose.md ✅ (Collective\; §0–§6+NewConcepts; META-level; Cosmic-Loop-5-steps; Vertical-vs-Horizontal-loop; Domain-fixed-knowledge-changes; Discovery≠Creation; 3-Forces-drive-participation: Resonance+StatusLock+SurvivalSchema; Biological-Ceiling-guarantees-dispersal; Knowledge-non-rivalrous; 5-example-contribution-roles; Weak-vs-Strong-claim; Teilhard/Vervaeke/Kuhn/Dawkins-precedents; 3-level-implications: Individual/Framework/Society; Suppression-breaks-loop-functional-argument; Diversity=parallel-exploration; Bond-Architecture×Collective+Resonance-Sustainability×Collective+By-Product-Scale×Collective; 2026-06-09)
- [x] H05 Compliance-Floor.md ✅ (Collective\; §0–§12+NewConcepts; Freedom=Default-Rules=Exception; Harm-Principle-Mill-1859; 4-tier-floor: Body-Base/Chunks/Melody-Space/Information-Integrity; Universal-7-rules; 5-inherent-limits: Discrete-vs-Continuous+Context-faster+Hardware-diverse+Legislator-bias+Zero-sum-boundary; 4-floor-rising-forces: Power-uniformity+Cascade-fear+Cultural-inertia+Precautionary-bias; 3-step-cascade-check; 3-natural-groups; Group②=social-health-indicator; Empathy=Self-Pattern-Modeling-Compiled+Valence-Structural-positive; Self-Pattern-Modeling-alone-not-enough-sociopath; Valence-Structural-alone-not-enough-love-without-understanding; 2-stream: Valence-Momentary-fast+Valence-Structural-baseline; General-Valence-Structural-for-humanity-3-sources; Sociopath-analysis; Rules=Bridge-Empathy=RootSolution; Floor=f(population-empathy); 5-principles-optimal-floor; Real-examples: hair-dyeing/religion/drunk-driving/gun-control; Hart-1961-open-texture; OECD-regulatory-accumulation; Hare-1993-psychopathy; Batson-1991; Entity-Access×Compliance+Hardware-Subsidy×Compliance; 2026-06-09)
- [x] H06 Collective.md ✅ (Collective\; §0–§8; Hub-file-5-sub-files; Collective=EmergentInfrastructure-NOT-entity; 3-properties: RealConstraints+Distributed+EmergentPatterns; Compilable-Architecture-requirement; 3-Level-Model-preview; 5-Pathways: ①TrustCompile+②BehavesLikeDomain+③SchemaInheritance+④StatusAccessMap+⑤SystemCompilation; 5-pathways-run-simultaneously; 3-forces+5-pathways=EmergentCompliance; Folder-architecture-3-reading-paths; 7-cross-cutting-themes: Tech×Scale+ByProductMatch+HardwareSubsidy+GlobalBodyAnalogy+AIEra+3Forces+BiologicalCeiling; Individual-vs-Collective-boundary; Trust=ONLY-bridge; Individual-detects-collective-gap; 2026-06-09)
- [x] H07 Domain.md ✅ (Domain\; §0–§9; Domain=ExternalReality; Lean-epistemological-reflection-not-direct; 3-domain-types: Reality/Abstract/Abstract-Dynamic; 3-methods-knowing: Feedback+Convergence+Combination; 8-certain-characteristics: Exists-independent+Infinite+Finite-at-point+Knowledge-convergence+Permits-combination+Real-feedback+Incremental-only+Expansion-accelerates; 3-constraint-sources×shelf-life: Physics∞/Hardware∞/CollectiveLimited; Individual-no-source-sensor; Dual-Check: Body=QualityController-Domain=FinalArbiter; 4-cases-table; AI-amplifies-risk; Domain-types×DualCheck; 5-framework-intersections: Gap-system+Compiled-Fresh+Satiation+Simulation-Engine+Entity-Access; Arthur-2009+Kurzweil-2005+Conway-Morris-2003+Kahneman-2011; Kant-phenomena-not-noumena; Platonism-debate-DM6; 2026-06-09)
- [x] H08 Conflict-Dynamics.md ✅ (Domain\; §1–§10; Conflict=Overlap×Scarcity×Commitment; 3-conditions-necessary-and-sufficient; EntityAccess-overlap-paradox; Difference≠Conflict; DifferentGapDistribution+SameImagineFinal=Strongest; Similarity→Conflict; InnerConflict=SameMechanism; Perceived-vs-Actual-scarcity-table; SimulationEngine-amplifies-perceived; Domain-Types×conflict: Reality-resolves-fast/Abstract-Dynamic-persists/Abstract-rarely-true; Multi-scale-5-levels; SecurityDilemma-2-SimulationEngines; Historical-comparison-table-4-periods; Resolution-3-strategies: BreakOverlap+BreakScarcity+BreakCommitment; ImagineFinal-awareness-meta-strategy; Satiation×resolution-3-types; Scarcity=Engine; Evolution-5-examples; Diversity-from-scarcity; SelfPatternModeling-distributes-surplus; Scarcity=trap-when-no-expansion-capacity; Fisher-Ury-1981+Sherif-1966+Allport-1954; 2026-06-09)
- [x] H09 Discovery-vs-Expansion.md ✅ (Domain\; §1–§9; 2-modes: Discovery=build-Imagine-Final-from-zero/Expansion=execute-from-existing; 3-point-spectrum: Sense(Phase1-2-no-verify)→Verify(Phase3-5-domain-confirm)→Scale(expansion); Discovery-5-phase-spiral: Scatter/Trial-and-error/Initial-convergence/Optimize/Deep-convergence; 3-reasons-cannot-skip: reference-need+attractor-only-visible-when-mapped+domain-incremental; Dissonance-mandatory; Real-check=only-compass; §2.5-Sense-Without-Verify=Philosophy: Democritus/Dalton+Aristotle/Galileo+Hippocrates+Freud+Mencius+AdamSmith+Pythagoras; NaturalPhilosophy→Physics-naming-transition; Wundt-1879-psychology-separates; Remaining-philosophy=no-verify-tools-yet; Philosophy-value=scatter-phase-for-humanity; Expansion-4-steps; 4-reasons-faster: Foundation+Tools+Guide+Community; Diminishing-returns→discovery-at-edge; Education=Expansion-mode; Both-modes-always-parallel; Einstein-needed-expansion+student-has-micro-discovery; Oscillation-mechanism; Ratio-5-factors: Hardware+Expertise+Task+Environment+LifeStage; Pipeline=engine-of-civilization-4-reasons; Imagine-Final-Bootstrap=discovery-process; Implications-Education/Team/AI-era/Personal; March-1991+Kuhn-1962+Arthur-2009+Newton-giants; 9-open-questions-DE-1-through-DE-9; DE-9-fractal-same-mechanism-all-scales: Imagine-Final+Discovery+Knowledge-Flow+Global-Melody; 2026-06-09)
- [x] H10 Knowledge-Flow.md ✅ (Domain\; §1–§11; Flow-Internal→Output→External-Chunk; Workshop→Blueprint→Factory-metaphor; Why-A-shares: empathy-mirror-biochemistry; Compression: E=mc²-example+spectrum-table-walking→ride-hailing; Domain-invariant-Schema-variable; Optimization-pressure: MinCost×MaxCoverage; Override-not-discard: legacy-obsoleted; 2-mechanisms: individual-decay+global-override; Override-chain-heat-domain; Dissonance→Output→Smooth-3-phases; Arc-Wave: 3-clustering-reasons+peak-trough+trough-rises; Paradox: smoother-but-sees-more-dissonance; Background-arcs; Fractal-4-scales: skill/career/lifetime/global; 4-shared-constraints; Arc-distance-from-base; Baseline-Shift: generations-table+flow-as-measure-of-progress; Acceleration-positive-feedback-loop; Body-bandwidth-limit; 100yr-prediction: override-schemas+permanent-schemas; Simulation-Engine×Knowledge-Flow; PFC-Budget×Arc-Wave; Hardware-Subsidy×Compression; Ebbinghaus+cumulative-culture; 2026-06-09)
- [x] H11 Domain-Mapping-Drive.md ✅ (Domain\; §0–§10; Central-question="why-given-doesnt-satisfy"; Scope=DESCRIPTIVE-not-prescriptive; 5-main-arguments: hardware-feature+process-reward+chunk-threshold+3-threat-types+7-education-principles; §1-Evolutionary: SelectionPressure-individual-A-satisfied-dies/B-explorer-survives; Cross-species: Rats-Kavanau1967/Rhesus-Butler1953/Crows/Octopus/DomesticDogs; Children-universal-6mo-object-permanence→2yo-why-phase→4-7yo-creativity-peak; GildedCage-evidence: Brickman1978-lottery+retirement-blues+historical-royalty+gap-year; Restless=feature-not-bug; Imagine-Final-collapse=emptiness; Curiosity-distribution-5/25/50/15/5%; Hardware-Subsidy+Simulation-Engine+Entity-Access-v2.0; §2-Mechanism: VTA=delta-detector-not-absolute+Schultz1997+HedonicTreadmill-Brickman1978+3-Satiation-types-v2.0; Opioid-fires-PER-STEP-BUILD-phase: pho-cooking-9-fire-events-vs-restaurant-1; Bug-fixing; Bicycle-learning; PFC-Budget+4-Firing-Modes-v2.0; Chunk-threshold-self-sustaining: Forest-example+Einstein-Isaacson2007-threshold-15-17yo+Darwin-20yr-cant-stop-1839-sketched-1859-published; Below-threshold=boredom-not-mismatch; Entity-Compiled-v2.0; Imagine-Final-Lifecycle-5-phases+3-outcomes: BUILD→SAVE→BACKGROUND→RELOAD→REFINE; Monday-math-problem-example; Sleep-consolidation-Wagner2004; Einstein-1905-breakthrough; §3-3WayBalance: Dissonance-Zone1-bored/Zone2-sweet-Csikszentmihalyi1990/Zone3-overwhelm; Vygotsky-ZPD-1978; Imagine-Final-4-quadrant: SweetSpot/Mismatch/Delusion/Fantasy; Parent-inject-examples; Mini-reward-sustainable: passionate-coder-vs-money-coder; Resonance-Sustainability-4-layer-v2.0; Entity-Access×Zone2-v2.0; §4-ModernParadox: Lighter-problem-10-examples; CapacityRefund: Einstein-right-vs-CoachPotato-wrong; Environment-designed-for-shallow; Satiation×Abundance-v2.0; §5-5Patterns: Einstein-verbal-logical-4-key-observations; Chef-JacquesPepin-somatic-9-fire-events; Craftsman-Japanese-80yo-carpenter-apprenticeship; CrossDomain-Synthesist-Darwin/Simon/Hofstadter/McGilchrist+AI-lowers-hardware-bar; Polymath-Leonardo/Franklin; §6-CosmicLoop: Domain→Body→Schema→Knowledge→Domain; Fire-chunks-200000yr-example; Knowledge-convergence-weak-claim; Individual-contribution-3-scales: invisible/small-public/large-public; Non-linear-ahead-behind; §7-7-Education-principles: Novelty-path>threat-path+compound-interest-chunk-associations; 3-threat-types: Domain-KEEP+Peer-KEEP-monitor+Imposed-REDUCE; Rich-reality-2-environment-comparison; Wait-for-threshold-reading-example; Hardware-calibration-3-children; Respect-lifecycle-Schedule-A-14h-BUILD-vs-Schedule-B-6h-BUILD-16h-rest; Transition-2025-2070+; §8-6-Barriers: short-term-bias+cultural-anchor+measurement-systems+rich-env-cost+hardware-calibration-difficulty+economic-political; §9-HonestAssessment-🟢🟡🔴+6-caveats+5-missing; §10-Connections; 2026-06-09)
- [x] H12 Drill-Emergent-Pattern.md ✅ (Domain\; §0–§9; Emergent-Pattern=compiled-valence-relationship-from-repeated-interaction; NOT-pre-designed-NOT-conscious-decision; 3-why-emergent: nobody-designed+emerges-from-interaction+cannot-predict; Pattern-structure: Trigger+Mechanism+CompiledState+Influence+BreakCondition; §2-Connection-MOVED→Connection.md-v5.0; §3-Enemy: sustained-negative-valence; Asymmetry-forms-faster-than-connection; Negativity-bias-Baumeister2001; 3-forms: AgentEnemy/ObjectEnemy/ObjectAsProxy; Dehumanization=agent→object-reclassify→SelfPatternModeling-OFF; Surgeon-temporary-functional-vs-war-permanent-dangerous; Schema-inheritance→enemy→prejudice=overgeneralize; §4-Nurturing: 4-factors-MULTIPLY: Living×Vulnerability×Expressiveness×Similarity; BabySchema-Lorenz1943-Glocker2009; FacialEMG-Dimberg2000; Xu2009-ingroup-empathy-bias; Unique-reward=other-person-state-improves; Own-baby-4-factors-MAX-vs-fish-near-zero; §5-Giving: body-sufficient+detect-other-lacking+share-reward>keep; Same-mango-more-total-reward-distributed; NOT-selfless-4-reward-sources: SelfPatternModeling+Status+Connection+Schema; 3-violation-tests: own-body-base-insufficient/core-schema-violated/reciprocity=0; Spectrum-Healthy→Override-A-justified→Override-B-schema-hijack-no-ceiling; §6-Superseded: Dependency→Entity-Access+Excess; MixedValence→Valence-Propagation; GroupDynamics→Collective-folder; §7-Violation: Impact=Investment×Severity; 2×2-table; 3-responses: Recalibrate-healthy-hard/Overgeneralize-evolutionary-safe/Collapse-high-schema-rare; Schema-level-4-rows: SpecificAgent/Category/OrgDomain/Worldview; Domain-types×recovery-difficulty; Cases: romantic-betrayal+monk-vow+double-violation; Recovery-3-paths: same-entity-scarred/new-entity-blocked-by-overgeneralize/new-anchor-for-collapse; §8-🟢🟡🔴; 2026-06-09)
- [x] H13 Dopamine-Is-Not-Reward.md ✅ (Clarification\; §1–§7; VocabNote=prediction-error-only-when-discussing-mainstream-Schultz-framework-uses-prediction-delta; §1-Research-state: settled=VTA-mesolimbic+wanting≠liking+Schultz-PE+opioid-hedonic+Parkinson-incomplete+addiction-multi-system+naltrexone-reduces-euphoria; debated=mechanism-of-liking+PE-vs-salience+dopamine-role+opioid-role-permissive-vs-active; gap=20-30yr-pop-science-lag; §2-3-positions: Classical-Olds1954-Wise1980s-dopamine=pleasure; Berridge-Robinson-1998-wanting≠liking-separated-black-box; Framework=VTA-salience-alert-DOORBELL+body-base-opioid-GIFT+7-step; §2.1-8-criterion-table; §3-9-evidence: #1-Berridge-rat-lesion-decisive; #2-Schultz-PE=salience-not-pleasure-habituation-alternative; #3-Parkinson-anhedonia-incomplete-wanting-down-liking-preserved; #3b-MusicalAnhedonia-strongest-pipeline-test-Martinez-Molina2016-PNAS-domain-specific-disconnect-auditory↔NAcc; #4-opioid=direct-pleasure-morphine-Peciña2005; #5-addiction-wanting≠liking; #6-scroll-empty-VTA+no-opioid; #7-Eureka=opioid-not-dopamine-4-intensity-contexts; #8-Naltrexone-blocks-euphoria-not-dopamine-Jayaram-Lindström2017-PET-5+-studies; summary-table-9x; §4-7-step: Step1-unconscious-fire; Step2-VTA-delta-habituation-NOT-PE; Step3-DRD4-filter; Step4-PFC-spotlight; Step5-BODY-BASE-CHECK-critical; Step6-reinforce; Step7-COMT-clear; 5-preconditions-for-opioid: DirectedGap+ChunkSubstrate+DeltaGate+MatchRange+CompileGate; §4.4-addiction-3-types: TypeA-opioid-bypass-step5/TypeB-stimulant-complex-naltrexone-evidence/TypeC-behavioral-empty-chase; §4.5-chunk-compile-cortisol-direction-gate; §4.6-Imagine-Final-integration; §5-vs-Berridge: 5-extensions: VTA-mechanism+5-preconditions+body-base-grounding+cortisol-direction+step5-bypass; §5.3-answers-Berridge-2016-open-question; §5.4-Schultz-alternative-not-refutation; §5.5-3way-table: Nicotine-hijack-step5/Parkinson-loss-steps2-4/ADHD-tuning-step3; NIC-PD-2024-NEJM-nicotine-not-neuroprotective; §6-honest: 5-open-questions+health-conditions-validation+musical-anhedonia-QED; §7-cross-refs; 2026-06-09)
- [x] H14 Prediction-Error-Is-Not-Reward.md ✅ (Clarification\; §0–§8; CLARIFICATION+EXTENSION-not-rejection; VocabNote=PE-in-this-file-prediction-delta-in-all-others; §0-PE-contribution: Schultz1997-foundational-predictive-brain-paradigm-Step1-of-7; §1-original→popular: animal-simple-context-both-correct+nuance-lost; §2-AI-vs-human: AI-has-defined-reward-function/human-body-generates; comparison-table; §3-Spotify-test: 3-tests-random-note+noise=best-music+unexpected-note-all-fail-PE-alone; good-music=PE+Coherence+Goldilocks+AdequateChunks+NoNegativeTag; Precondition3-passes-but-Match-Range-coherence-fail=dissonance; §3b-Neuroscience-validation: Salimpoor2011-NatureNeuro-caudate(anticipation)≠NAcc(experience)=2substrates-2phases; Cheung2019-CurrentBiology-80k-chords-pleasure-MAX=uncertainty-HIGH+outcome-POSITIVE; Ferreri2019-PNAS-bidirectional; Gold2019-PNAS-acoustic×schematic-interaction; §3-predicts-§3b-confirms; §4-Extension: Step1-VTA(PE)+Step2-CoherenceCheck+Step3-5Preconditions+Step4-signal; PE=Step1-necessary; Reward=Step4-after-2+3; Reward≠single-chemical: Evaluative(opioid)+Direct-State(non-opioid); 2-layer-model-GapDirection; §5-6-cases: PE-high+reward(Case1)/PE-high+dissonance(Case2)/PE-low+reward(Case3)/PE-low+neutral(Case4)/PE-high+confused-Precondition2-fail(Case5)/PE-high+blocked-Precondition5-fail(Case6); §6-why-simple-interpretation: animal-simple-context+AI-success+broad-terminology; §7-🟢🟡🔴+Salimpoor+Cheung-upgraded; §8-cross-refs; 2026-06-09)
- [x] H15 Mirror-Neuron-Rejection.md ✅ (Clarification\; §1–§7; Rejects-hardware-mirror-module-NOT-PE-research; §1-Research-state: settled=mirror-neurons-monkeys+shared-fMRI-humans+broken-mirror-autism-DEAD-Bird&Cook2013+empathy-learnable; debated=innate-vs-learned+automatic-vs-motivated; not-unified=Self-Pattern-Modeling-proposed; §2-3-positions-table: Rizzolatti-innate-module/Heyes-ASL-learned/Framework-prediction-model-7-rows; Framework=closest-to-Heyes+adds-WHY; §3-7-evidence: #1-newborns-no-real-mirror-arousal-contagion-only-Dondi1999+Oostenbroek2016-failed-replicate; #2-mirror-develops-GRADUALLY-0-6mo-pattern→6-9mo-social-ref→9-12mo-instrumental→14-18mo-complex→18-24mo-true-empathy→2-7yo-animism→7plus; #3-cross-species-gradient: mother-strongest/stranger-medium/dog-weaker/cat-less/fish-near-zero/insects-zero; #4-DECISIVE-Bird&Cook2013-alexithymia-NOT-autism-drives-empathy-deficit; autistic-WITHOUT-alexithymia=empathy-intact; #5-statues-sacred-stones-placebos: compiled-schema-fires-no-agent-input; #6-mirror-CAN-be-suppressed: dehumanization+negative-schema+PTSD-retroactive-flood; #7-rouge-test-infant-0-5mo-treats-reflection-as-Other→18-24mo-learns-self-distinction; §4-Framework-alternative: 4-steps-objects-deterministic/agent-non-deterministic-must-build-model/own-state-as-template/compile+generalize; 3-mechanisms-mainstream-conflates: PatternMatching-limbic-near-innate/AgentModeling=Self-Pattern-Modeling-learned-14-24m/SchemaSimulation-compiled-mature-no-input; §5-vs-Heyes: 5-extensions: WHY-learn=agent-non-deterministic+self-awareness-architectural-prerequisite+3-mechanism-taxonomy+schema-override-pathway+chunk-substrate-integration; §6-🟢🟡🔴: hardware-mirror-rejected=🟡/Bird&Cook=🟢/3-mechanisms=🟡/byproduct-framing=🔴; §7-cross-refs; 2026-06-09)
- [x] H16 Cortisol-Amplifier-Not-Cause.md ✅ (Clarification\; §1–§8; Cortisol=change-readiness-amplifier-NOT-stress-hormone; Firefighter-analogy: cortisol-present-when-pain-but-not-cause; §1-Misconception: Selye1936-origin+correlation≠causation+AI-bias-reinforcement-loop; §2-3-evidence: #1-cortisol-injection-healthy-person-no-distress; #2-Addison-zero-cortisol=dangerous-not-comfortable; #3-cortisol-high-during-exercise/sex/problem-solving=positive; §3-Definition: change-readiness-amplifier; 3-modulations: Sensitivity+Energy+Direction; Electricity-analogy; Gym-analogy; Inverted-U-7-modes-IDLE→LAZY→ACTIVE→FOCUSED→PUSH→FREEZE→CRASH; CORTISOL=SUSTAINER-NOT-TRIGGER: timeline-0ms-schema→500ms-NE→1-2s-adrenaline→2-5s-behavior→5-20min-cortisol-peaks; §4-3-real-sources: Nociception+Mismatch+Recalibration; §5-Direction>Level: novelty-vs-threat-table; Direction-Gate-Chunk-§2.4-compile-time; §5b-Repair×Damage: gym-analogy; Net-health=Repair-Damage; 5-row-table; PFC-dendrite-retraction-McEwen2007; Amygdala-hypertrophy-Vyas2002; Vicious-cycle-diagram; Trauma-loop-4-stages; §6-4-fix-strategies: FixSource+FixDirection+FixDuration+FixBaseline; cortisol-detox=marketing; §7-🟢🟡🔴+complete-picture-IMPORTANT: acute-OK/chronic+sleep-OK/chronic+no-sleep=damage; §8-cross-refs; 2026-06-09)

### Phase I — Research (74 files)

**I1. Health-Conditions (12 files)**
- [x] I01 Addiction-Analysis.md ✅ (Health-Conditions\Hijack\; §0–§10; OVERVIEW-for-Chemical-Hijack-folder; Dopamine≠reward-doorbell/opioid=gift-behind-door; 3-positions: Classical-dopamine-pleasure/Berridge-wanting≠liking/Framework-7-step; §1.2-wrong-mechanism→wrong-solution; §2-Chunk-Reward-Loop-Hijack: 3-hijack-points: BFP-bypass+cycle-never-stops+shortcut-compile; §2.2-4-phase: Pull/Tolerance/Push(negative-reinf)/Dependency; §2.3-false-positive=bypass-not-deceive; §3-Evaluative/Direct-State-attack: Evaluative-hijack=back-door+Direct-State-hijack=real-but-not-lasting+both-simultaneously=strongest; §3.2-Evaluative-Gates-Direct-State-bypass; §4-3-groups: Chemical(bypass-depth×speed×specificity)/Behavioral(exploit-not-bypass-variable-ratio)/Schema-based(not-enough-chunk-competes-hardest-recovery); §5-Withdrawal=body-base-baseline-disrupted+cortisol-amplification; §5.1-substance-coupling-hypothesis-🔴partial; §5.2-4-mechanisms+gradient; §6-PFC-Config×stages: Normal/Reallocation/approaching-④/④-Disconnected/oscillation=torment/①-rebuild; key-insight="not-lack-of-willpower=PFC-offline"; §7-Recovery=re-compilation: chunks-never-delete-only-probability-shift; Direct-State=evolutionary-floor-backdoor-for-anhedonia; Social-coupling=alternative-reward; 4-compile-pathways×recovery; §8-Self-medication: dissonance+substance=relief-not-fix+loop; PFC-Config-mechanism; §9-confidence-table+6-open-questions; §10-cross-refs; 2026-06-09)
- [x] I02 Alcohol-Brain-Mechanism.md ✅ (Health-Conditions\Hijack\; §0–§9; Ethanol=carpet-bombing-5-systems: GABA(dominant)+NMDA(double-down)+Opioid(real-reward-Mitchell2012)+Dopamine(indirect-salience)+Serotonin(mood-short-term); §1.3-2-directions-suppress+reward=self-reinforcing; §2-BAC-gradient: 0.02-0.03=barely-tipsy/0.04-0.06=tipsy/0.08-0.10=drunk/0.15+=heavily/0.25+=fatal; Order=PFC→Cortex→Hippocampus→Cerebellum→Brainstem; §3-PFC-vulnerability: NMDA-density-highest+recurrent-circuits-most-complex; Arnsten2009+Goldman-Rakic1995; §4-6-factors: ALDH2/ADH1B-east-asian-specifics(ADH1B*2=~70-85%VN+ALDH2*2=~25-30%VN); Asian-flush=body-protecting; Brooks2009-esophageal-cancer-6-10x; COMT/DRD4(framework-inference); Cortisol-baseline(novelty-cortisol+alcohol=release/threat-cortisol+alcohol=worse); Tolerance(GABA-down+NMDA-up≠less-damage); Body-composition; §5-"In-vino-veritas": compiled-chunks-dominate-when-PFC-off; 5-drunk-types: happy/aggressive/sad/talkative/reckless=dominant-chunks; §6-4-conditions: Bounded-stress+PFC-not-overloaded+Imagine-Final-clear+Few-alternatives; 4/4=functional-release/0-1/4=counter-productive; §7-4-phase+withdrawal-FATAL: GABA-down+NMDA-up-rebound→seizure→death; ONLY-2-substances-fatal-withdrawal=alcohol+benzodiazepines; §8-🟢🟡🔴; §9-cross-refs; 2026-06-09)
- [x] I03 Alcohol-Vietnam-Generational.md ✅ (Health-Conditions\Hijack\; §0–§11; Vietnam-case-study-applying-4-conditions; §1-GDP-$100→$4700-timeline+internet-penetration; §2-Đổi-Mới-generation(1960-80)-4/4-conditions-met=GOLDEN-AGE-communal-drinking; §2.3-genetic-paradox: 5-schema-signals-vs-1-body-signal=schema-wins(ALDH2*2-25-30%-VN); §3-Millennials(1980-97)-2-3/4; §4-Gen-Z(1997-2012)-0/4=natural-rejection; NielsenIQ2025-45%-limit; Inside.beer2023-12%-decline; Berenberg2018-global-GenZ-20%-less; §4.4-"not-weaker=DIFFERENT-stress-structure"-bounded-vs-unbounded-analogy; §5-cultural-mechanism-5-channels: Obligation(compiled-prediction)+Status-threat(Resource-Access-Map)+Connection(real-opioid-shared-state)+Schema-Identity(childhood-install)+Business-survival(L1-threat); §6-4x4-table-core-analysis; §7-Decree-100=Compliance-Floor-CATALYST-not-cause; 3-groups: self-motivated+social-followers+need-enforcement; §8-predictions-10-20yr: alcohol→niche-choice; "refusing-alcohol=maturity"-schema-compiling; VN-per-capita→5-6L; §9-body-needs-don't-disappear→digital-replacement: 5-needs-table; damage-comparison-table: alcohol-CAN-BE-FATAL-vs-digital=lighter; "exchanging-alcohol-for-phone=possibly-better-not-necessarily-healthy"; §10-🟢🟡🔴; §11-cross-refs; 2026-06-09)
- [x] I04 Nicotine-Brain-Mechanism.md ✅ (Health-Conditions\Hijack\; §0–§12; Dopamine-Cluster-File-1: SOURCE-forced-fire; §1-nAChR-2-subtypes: α4β2(high-affinity→VTA→dopamine)+α7(opioid-Pathway2); §1.2-2-mechanisms: direct-stimulation+GABA-disinhibition; §1.4-3-systems-simultaneously: dopamine+serotonin(raphe-nAChR+MAO-A)+NE(LC-nAChR+HPA); §1.5-comparison-table: scroll-phone→nicotine→alcohol→cocaine→heroin; §2-cigarette≠nicotine: MAO-I(Fowler1996-40%-MAO-B-reduction)+acetaldehyde(Belluzzi2005)+CO(cycle-reinforcer); Guillem2005-"dramatically-increases-motivation"; MAO-I-from-smoke-not-nicotine; §3-7-products: pH-determines-absorption-site; cigarette(acid-pH5.5-lungs-10-19s-FASTEST)+thuốc-lào(N.rustica-3-9×-nicotine-massive-bolus)+hookah(CO-8×-cigarette-AHA)+cigar(alkaline-pH8.5-mouth)+pipe+snus+snuff; §3.7-3-factors: speed×amplifiers×session-pattern; §4-dose-gradient: Level1-2-3-4; §5-3-misconceptions-SAME-PATTERN: dopamine(focus)+serotonin(confidence)+NE(alertness)=restoration-not-enhancement; Heishman2010-d=0.16-0.44; Taylor2014-quit→mental-health-IMPROVE; Moylan2012-smokers>anxiety-depression; §5.5-self-reinforcing-belief-loop; §6-5-individual-factors: CYP2A6(most-important)+CHRNA5-rs16969968(aversion-ceiling)+COMT(framework-inference)+cortisol-baseline+age-first-exposure; §7-chunk-dynamics: trigger-landscape-6-contexts+Body-Coupling-7-modalities+"don't-know-what-to-do-with-hands"+identity-chunk-West&Brown2013; §8-withdrawal=upregulation-rebound: UNIQUE-opposite-other-drugs; Fenster1999-causal-link-9.7≈9.9nM; receptor-count-200-300%+; timeline-5-stages: 4-24h/48-72h-PEAK/1-4wk/1-12mo-context-cravings/1yr+; chunk-cravings-persist-after-chemical-resolves; §9-PFC-long-term: CO-hypoxia+vasoconstriction; body-feedback-distorted-filter; §10-bridges: Parkinson-RR=0.59-Hernán2002+α7-nAChR-PI3K-Akt-neuroprotection+MAO-B(same-as-selegiline); Alzheimer-cholinergic-hypothesis; Dopamine-Cluster-preview-3-way-table; §11-🟢🟡🔴; §12-cross-refs; 2026-06-09)
- [x] I05 Parkinson-Analysis.md ✅ (Health-Conditions\Neurodegeneration\; §0–§15; Dopamine-Cluster-File-2: SOURCE-dying; §0-3-category-table: Hijack/Degradation/Configuration; §1-overview+4-motor-symptoms+non-motor-paradigm-shift; §2-2-neuron-types: Modulatory(secondary-DYING)+Processing(primary-initially-intact); §2.2-Basal-ganglia=GATE-default-CLOSED+dopamine=KEY+GATE-LOCKED-diagram; §2.4-not-energy-depletion-but-gate-blocked; §3-α-synuclein: normal-protein→misfold-process→5-toxic-mechanisms; §3.3-WHY-SNc-first-4-reasons: dopamine-metabolism-oxidative-stress+iron-neuromelanin+Ca-pacemaking-24/7+75000-axon-arbor; §3.4-threshold-decades-accumulation; §3.5-template-seeding-physical-contact; §3.6-5-transfer-routes: exosomes+nanotubes+trans-synaptic+secretion+lysis; §3.7-remaining-neurons-overwork-accelerating-death; §3.8-protective-factors: exercise-BDNF(OR=0.67)+3-risk-factors+physical-labor-paradox; §4-Braak-6-stages+framework-mapping: L0→L1→modulatory→PFC-bottom-up+gut-brain-dual-hit; §5-prediction-intact+execution-fails: unique-case-vs-addiction/Alzheimer/ADHD/depression; §5.2-chronic-irresolvable-prediction-delta; §5.3-FOG=gate-overload-multiple-demands; §5.4-masked-face-social-gate; §6-3-dopamine-pathways: Nigrostriatal(FIRST-motor)+Mesolimbic(wanting-impaired-liking-preserved-Sienkiewicz-Jarosz2005+Loas2012)+Mesocortical(PFC-fuel-latest); §7-non-motor: depression=HARDWARE-3-systems+apathy≠depression-separate-circuits+RBD=gate-leaking-sleep+pain+autonomic+compound-cascade; §8-levodopa-paradox: gate-key-from-outside+overdose-hypothesis(Gotham1988)+ICDs-13.6%(Weintraub2010)+efficacy-decline+ON/OFF; §9-DBS: beta-oscillation-jam+electrical-override+tradeoff-side-effects; §10-body-feedback: multiple-concurrent-irresolvable-deltas+3-management-principles(delta-reduction+BDNF+cortisol); §11-nicotine-bridge: RR=0.59+NIC-PD-2024-FAILED+3-candidates(MAO-B+CO+CYP450)+reverse-causation-debate; §12-pandemic: doubled-2015+3-drivers(aging-89%+smoking-decline-10%+pesticides)+dual-role-table; §13-hijack-vs-degradation: 9-row-table+SOFTWARE-vs-HARDWARE; §14-🟢🟡🔴; §15-cross-refs; 2026-06-09)
- [x] I06 Alzheimer-Analysis.md ✅ (Health-Conditions\Neurodegeneration\; §0–§19; Neurodegeneration-Cluster-File-2: SYNAPSE-LOSS-primary; §0-framework-position: unique-case-chunks-dissolve-vs-Parkinson-gate-locked; Forgetting(retrieval-fail)vs-Loss(substrate-damage); §1-overview-57M+5-stages+APOE-ε4+14-modifiable-factors(Livingston2020/2024~45%)+4-Phase-model(Silent→Accumulation→Cascade→Symptoms)+heterogeneity-5-6-clinical-subtypes("umbrella-like-cancer"); §2-tau-biology: MAPT-gene-6-isoforms; normal-2-3-mol-phosphate→Alzheimer-3-4×; pretangle-from-childhood(Braak&Del-Tredici-2011-90%-ages-4-29); GSK-3β+CDK5-kinases+PP2A-phosphatase(71%); 5-stage-progression: pretangle→oligomers(MOST-TOXIC)→fibrils→tangles→ghost-tangles; tau-phosphorylation×synaptic-plasticity=same-machinery-quantitative-shift; §3-amyloid×tau: APP-BACE1-Aβ40/42; amyloid-cascade-99.6%-failure(Cummings2014); "amyloid-facilitated-tauopathy"-model; 6+-root-cause-hypotheses; Bhatt2019-positive-feedback-loops; §4-Braak-staging-Alzheimer: 6-stages-entorhinal→hippocampus→neocortex-INSIDE-OUT; vs-Parkinson-bottom-up; retrogenesis(Reisberg2002); myelin-model(Bartzokis2004/2011+Depp2023-upstream-amyloid); §5-synapse-loss-PRIMARY: Terry1991-r=0.96+Selkoe2002+DeKosky1990+Scheff2006-55%-fewer; tau→synapse-3-mechanisms+activity-dependent; Phase-Transition: activity-protective→destructive; chunk-degradation-3-levels(weakening→fragmentation→loss)+2-stages(anterograde-then-retrograde); §6-5-mechanisms-"last-in-first-out"-OVERDETERMINED: memory-consolidation+compile-depth×distribution+activity-dependent-spread+Multiple-Trace-Theory(Nadel&Moscovitch1997)+myelination-order; Background-Pattern-exposed-through-erosion; §7-Self-Pattern-Modeling-dissolution: 4-stage-identity-timeline(recent→role→relationship→core)+Compiled-vs-Fresh-uneven-loss+reminiscence-bump; §8-body-feedback: Body-Base-still-alive-software-collapsing; BPSD-4-types(agitation+wandering+sundowning+paranoia); pain-undertreatment-49%-have-pain-20-40%-receive-analgesics; §9-connection-ambiguous-loss: Boss1999-5-8yr-frozen-grief+caregiver-Body-Coupling-one-sided+Schulz&Beach1999-63%-higher-mortality+Brodaty2009-34%-depression; §10-acetylcholine: Bartus1982+NbM+ACh-enables-chunk-compilation; nicotine-bridge-same-receptor-opposite-direction; ChEI-compensate-not-fix; §11-sleep×glymphatic: Xie2013+Hauglund2025-NE-oscillations-pump-CSF; 1-night=measurable-damage; Sabia2021+Benedict2015+Jorgensen2020; 5-axis-attack; vicious-cycle; zolpidem-warning; §12-5-protective-layers: Perez-Nievas2013-4-phenotypic-differences; centenarians-spread-without-accumulation(preprint); resistance-vs-resilience(Arenaza-Urquijo2018); Sister-Mary+SuperAgers; §13-music+religion+procedural: hierarchy-7-levels; 3-factor-model(depth×distribution×emotional); religion-6-memory-systems; degradation-order-validates-compilation-model; §14-cognitive-activity+stress: Wilson2007/2021+retirement+Wallensten2023-OR4.00+Lupien1998-hippocampus-14%+FINGER-trial+ikigai; §15-Parkinson-vs-Alzheimer-9-row-comparison-table+5-common-grounds; §16-treatment: 4-categories+NIA-AA-2024-revised+AMARANTH2025+cure-requires-3-things-③-impossible; §17-reverse-engineering-lens: living-archaeology+5-layer-hierarchy+architecture-determines-pattern-not-cause+Background-Pattern-exposed+parallel-with-autism; §18-🟢🟡🔴-~75-citations+13-open-questions; §19-cross-refs; 2026-06-09)
- [x] I07 OCD-Analysis.md ✅ (Health-Conditions\; §1–§13; "done"-pipeline-3-line-model; Line1=OFC-caudate-done-detector; Line2=serotonin-threshold; Line3=PFC-override; PANDAS/PANS=causal-proof-Line1(Swedo1998-strep→caudate-attack→OCD-immediately→repair→stops); §4.1-Chunk-Miss-never-resolves+spreading-activation-uninhibited; §4.3-5-Cortisol-Roles-in-OCD: Role②→③→⑤-escalation-path-vicious-cycle; §4.4-PFC-5%-operator-override-failure; §4.5-serotonin=AMPLIFIER-NOT-ROOT-CAUSE: 4-evidence-points(PANDAS-fix-root-stops+relapse-SSRI-80%-vs-CBT-20-30%+love-self-resolves-bond-compiles+cross-species-gradient); §4.5b-Self-Pattern-Modeling-childhood-bias×OCD-like-in-love: anxious-attachment=threat-biased-library+compound-uncertainty(Self-Pattern-Modeling+obligation); §4.6-cross-species-OCD: deer-mice(Korff2008)+SAPAP3-mice(Welch2007-Nature)+Hoxb8-mice(Greer&Capecchi2002+Chen2010-bone-marrow)+dogs-CCD(Dodman2010+Irimajiri2009-RCT)+captive-primates(Mason&Latham2004+Novak2006); Lines1+2=cross-species-ancient-circuit; Line3=human-ONLY; §4.7-Basal-ganglia×Parkinson-bridge: Parkinson=gate-LOCKED; OCD=gate-signal-NOISY; same-architectural-principle-different-failure-DBS-different-targets; §5-Love↔OCD: same-circuit(Marazziti1999-serotonin-↓40%); love-has-exit(bond-compiles→done); OCD-no-exit; ego-syntonic-vs-dystonic; §5.4-extended-limerence=OCD-like; §6-serotonin=certainty-bias(Status.md-v2.1-§9.2); OCD-requires-3-4×SSRI-dose-vs-depression; noradrenergic-NOT-effective; §7.1-PTSD-intrusion-vs-OCD-obsession: context-FREE(amygdala-encoded-missing-3/4-metadata-body-before-PFC-200ms) vs context-INTACT(done-signal-noisy-PFC-knows-body-doesnt-trust); §7.2-Autism×OCD-cascade-not-comorbidity(17.4%-van-Steensel2011-meta): 3-pathways(sensory-gain+masking-cortisol+predictive-coding-threshold); RRBs-vs-compulsions=ego-syntonic-vs-dystonic; §8-treatment-map: SSRIs=Line2; CBT/ERP=Line3; combo=gold-standard; SSRI-alone-~80%-relapse; combo-~30-50%; CBT-alone-~20-30%-relapse; DBS=Line1-last-resort; §9-Tesla-trajectory: functional→OCD-like-via-3-line-degradation(aging+chronic-cortisol+isolation); §10-hardware-environment-ratios: Line1-~80%-hardware; Line2-~50/50; Line3-~30%-hardware-70%-environment; waxing-waning(Skoog&Skoog1999); ~25-30%-full-remission; §11-🟢🟡🔴; §12-OCD-Q1–Q11-open-questions; §13-cross-refs; 2026-06-09)
- [x] I08 PTSD-Analysis.md ✅ (Health-Conditions\; §0–§16; Chunk-Context-Tag-Failure-PTSD=6th-Health-Condition; §0-framework-position: encoding-failure-category-NEW(hardware+chunks-intact-context-metadata-lost); §1-DSM-5-4-clusters+prevalence(Kessler2005-6.8%-US+Koenen2017-3.9%-global)+only-~20-30%-trauma-exposed→PTSD+Gilbertson2002-landmark-twin-hippocampal-volume-PRE-EXISTING-vulnerability; §2-context-tag-formalization: 4-metadata-types(temporal+spatial+causal+state); normal=4/4→"remembering"; trauma=state-only→"re-living"; Brewin-DRT-C-rep/S-rep-mapping; treatment=add-context-not-erase; §3-2-encoding-pathways: hippocampal(contextual)-vs-amygdala(context-free); Kim&Diamond2002-temporal-dynamics-DOUBLE-HIT(cortisol-suppresses+amygdala-disrupts-hippocampus); hippocampal-volume-pre-existing+acquired; §4-flashback-mechanism: sensory-trigger→context-free-chunk-fires→body-first-temporal-sequence(amygdala-12ms→body-50ms→PFC-200ms+); Rauch1996-PET-speechless-terror(Broca's-deactivated+mPFC-reduced); PFC-Config-④↔⑤-oscillation(Lanius2010-13-30%); §5-Yehuda-paradox: PTSD=LOW-cortisol-baseline(OPPOSITE-chronic-stress)+GR-UPREGULATED+enhanced-feedback; 2-phase-reconciliation(acute-HIGH→chronic-LOW); §6-hyperarousal: prediction-model-recalibrated-to-threat; PFC↓×Amygdala↑-vicious-cycle(Shin2006+Arnsten2009+Vyas2002); §7-avoidance=logical-body-response-to-pain(Eisenberger2003-Science)+Config-⑤-emotional-numbing+progressive-narrowing-cascade; §8-REM=overnight-therapy(Walker2009)+PTSD-elevated-NE→REM-mechanism-FAILS+nightmare=failed-processing-repeating+prazosin-mechanism; §9-extinction≠erasure(Bouton2004-4-return-phenomena)+Milad2009-PTSD=impaired-extinction-RECALL-not-acquisition+reconsolidation-window(Nader2000+Schiller2010); §10-treatment-unification: ALL=add-context-metadata; PE+EMDR(van-den-Hout2012-working-memory-taxation)+CPT+SSRIs+somatic; "two-thirds-problem"(Steenkamp2015-JAMA-~2/3-veterans-retain-diagnosis); novel: MDMA-Phase3(Mitchell2021/2023-Nature-Med-FDA-declined-2024)+Propranolol-reconsolidation(Brunet2018-ES=2.74)+SGB-RCT(Rae-Olmsted2020-JAMA-Psych-peripheral-storage-strongest-evidence)+Yoga-RCT(van-der-Kolk2014-52%-treatment-resistant-remission); §11-C-PTSD: Herman1992+ICD-11-6B41; Self-Pattern-Modeling-compiled-under-threat; Background-Pattern-3D-model(depth×density×context-quality); phase-based-evidence-MIXED(Dutch-RCT-2021-challenge); §12-comorbidities: PTSD×Depression(avoidance→reward-unused→anhedonia)+PTSD×Addiction(Khantzian-self-medication-30-50%)+PTSD×ADHD-mimicry(hyperarousal-mimics-stimulants-may-worsen)+PTSD×Alzheimer(Yaffe2010-~2×-dementia-risk); §13-intergenerational: Yehuda2016-FKBP5-methylation(🔴-small-samples)+prenatal-pathway-strongest-human-evidence(maternal-PTSD→11β-HSD2-reduced→fetal-HPA-recalibration); §14-3-framework-contributions-PTSD-forced; full-context-tag-model-formalization; 5-testable-predictions(P1-P5); §15-honest-assessment-🟢🟡🔴+Q1-Q7; §16-cross-refs; 2026-06-09)
- [x] I09 ADHD-Observation.md ✅ (Health-Conditions\Neurodiversity\; §0–§16+References; Dopamine-Cluster-3/3+Neurodiversity-Cluster-1/2; §0-framework-position: 3-cluster-comparison(Nicotine-SOURCE-FORCED/Parkinson-SOURCE-DYING/ADHD-CLEARANCE-fast+RECEPTOR-under-sensitive); OBSERVATION-not-Analysis(Neurodiversity-folder-not-disease); builds-on-Attention-Spectrum.md-v2.1; §1-ADHD-reframe: "Attention-Deficit"=misnomer; 3-presentations(Inattentive+Hyperactive-Impulsive+Combined); prevalence-5-7%-children(Polanczyk2007)+2.5-4%-adults(Faraone2006)+~50%-persistence; 3-layer-age-model(Layer1=chemical-hardware-0%-change/Layer2=structural-hardware-~25-30%-myelination/Layer3=software-~40-50%-compensation); §2-Double-Hit-DAT+DRD4: DAT-clears-fast(Spencer2007-PET)+DRD4-7R-under-sensitive(Frontiers2024-review); compound-both-ends(sending+receiving); Triple-Hit-PFC(DAT+COMT+DRD4); NE-parallel(Arnsten2009-alpha-2A/alpha-1); §3-3-way-comparison-table: Nicotine(Hijack-SOFTWARE)+Parkinson(Loss-HARDWARE)+ADHD(Tuning-CALIBRATED-DIFFERENTLY); 3-dopamine-perspectives(Hijack-teaches/Loss-teaches/Tuning-teaches); §4-EF-Barkley1997: behavioral-inhibition-primary→4-EF-downstream; working-memory=HOLD-DURATION-NOT-capacity(Martinussen2005-26-studies); inhibition(vlPFC-stop-signal-50-100ms-slow-Stop-Signal-Task); planning+sequencing(Mode1-unstable); task-switching-HYPER-vs-HYPO(PMC7515948-inattention=goal-neglect+switch-costs); Motivation≠Activation-v1.3(mesolimbic-wanting-intact+mesocortical-PFC-execute-under-fueled); §5-emotional-dysregulation: Shaw2014-25-45%-youth+30-70%-adults; RSD=social-prediction-delta×amygdala×PFC-under-fueled; cortisol-CORRECTED-v1.3(hypo-tonic-lower-baseline+hyper-phasic-higher-reactivity); 6-step-Threshold→Anxiety-chain(micro-cues-filtered→accumulate→explosion-surprise→cascade→schema-compile-"threats-unpredictable"→anxiety-as-hypervigilance-compensation); 3-environment-scenarios(good-Self-Pattern-Modeling/critical/overprotective); gaze-cueing-SELECTIVE(eyes-fail-arrows-intact-Psychiatry-Research-2016); alpha-modulation-INVERSE(PMC6969336-EEG-2019-n=45); §6-time-perception: temporal-myopia(Barkley1997)+3-timing-mechanisms-affected(Frontiers-Human-Neuro-2017); prediction-temporal-resolution-hypothesis(🔴); hyperfocus×time-collapse; §7-hyperfocus×gap-direction: 4-conditions(gap-massive+preconditions+immediate-reward+low-distraction); anticipation-vs-consummation-split(Plichta2014-VS-hyporesponsive-d=0.48-0.58+PLOS-ONE-2014-anticipation↓-delivery-normal/↑); paradox-resolved("can't-focus"+"hyperfocus-6-hours"=SAME-threshold-mechanism); §8-DMN-interference: Sonuga-Barke&Castellanos2007+Castellanos2008-anticorrelation-reduced; Mode1-unstable-PFC-drifts-toward-DMN; §9-Inverted-U: Frontiers-Psych-2022+ScienceDirect-2026-quadratic-fit+Tran2026-17000+-entrepreneurship; peak-ascending(threshold-rises+EF-sufficient)+peak(sweet-spot)+right-descending(3-reasons: EF-below-minimum+comorbidity-consumption+arc-failure-accumulation); Big-arc-anxiety-chain; environment-shifts-peak(🟡); ADHD+neurotypical-pairing; §10-lifespan: childhood-hyperactivity-visible+classroom-mismatch; adolescence-internalization+label-damage+PIB(protective→crash-Betancourt2024-ES-0.46-0.67); adulthood-PFC-depletion-cost-v1.3-CORRECTED(burnout=PFC-effort-depletion-NOT-chronic-cortisol); after-25-3-layers×age+neuroplasticity-slower; late-diagnosis-identity-re-compilation(French&Cassidy2026+PMC2022-5-themes); §11-medication: compensate-NOT-fix(DAT/DRD4/COMT=genes=unchanged); methylphenidate-DAT-block(Volkow2001/2012-signal-amplification-NOT-adding-dopamine); amphetamine-DAT-block+VMAT2-reverse; atomoxetine-NET-inhibitor-PFC-selective(Bymaster2002-NE+300%+dopamine-PFC); guanfacine-alpha-2A-agonist; §12-ADHD×Autism: Rommelse2010-20-50%-ADHD→ASD+50-72%-shared-genetics; 2D-model(Config×Tuning)+4-quadrant-table; overlap-vs-distinction-table(sensory-seeks-vs-manages+normal-vs-reduced-habituation); PTSD-mimicry(hyperarousal-mimics-ADHD+stimulants-may-WORSEN-PTSD); §13-calibration: per-position(subclinical/mild/moderate/severe); 3+1-conditions(safe-environment+arc-decomposition+fit+exercise); exercise-best-evidenced-non-pharma(SMD-0.611-overall+aerobic-2025-g=0.761-inhibition); parent/educator-implications; §14-P1–P8-testable-predictions; §15-🟢🟡🔴-honest-assessment+limitations; §16-cross-refs(full-cluster-table+companion-files); 2026-06-09)
- [x] I10 Autism-Observation.md ✅ (Health-Conditions\Neurodiversity\; §0–§16+References; Neurodiversity-Cluster-2/2+Health-Conditions-Drill-5/6; OBSERVATION-framing; "Configuration-DIFFERENT-not-broken"; builds-on-4-prior-files; §0-framework-position: 6-file-comparison(Nicotine-HIJACK/Parkinson-LOSS/ADHD-TUNING/Alzheimer-LOSS/Autism-CONFIGURATION-DIFFERENT/PTSD-CONTEXT-TAG-LOST); OBSERVATION-not-Analysis-reason; scope-CAN-CANNOT; §1-spectrum-not-binary: DSM-5-2-domains+3-levels(A:social-communication+B:RRB-4-criteria); 3-levels=support-needs-not-severity; prevalence-1-in-31(Shaw2025-CDC-MMWR-74-SS-2-2022-data)+3.4:1-sex-ratio(Loomes2017-meta); heritability-64-91%(Tick2016-meta)+102-risk-genes(Satterstrom2020-Cell)+polygenic-common-variation-primary(Gaugler2014-52.4%); idiosyncratic-connectivity(Hahamy2015-NatNeurosci-inter-individual-variability-core); serotonin-hyperserotonemia->25%(Schain1961)+GABA-reduced-sensorimotor(Puts2017)+E/I(Rubenstein2003); RRB-2-factor(Bishop2013-N=1825: RSM=sensorimotor-IQ-correlated+IS=insistence-sameness-IQ-independent); "many-things-under-one-name"-parallel-Alzheimer-labeling-cascade-⑥→⑦; 3-pathways-→-"social-difficulty"(①Configuration+②Tuning-severe-ADHD+③Deprivation); quasi-autism(Rutter1999-ERA-6%-adoptees+recovery<6months+Rutter2007-followup); §2-sensory-processing: prevalence-95%(Tomchek2007)+mixed-per-modality(Tavassoli2014)+reduced-habituation(Green2015-JAMA-Psychiatry-72-8)+amygdala-hyperactivation(Green2013-JAACAP)+cascade-model-5-steps; seeking-vs-avoidance; 7+-independent-channels-continuous-spectrum; §3-multisensory-integration: TBW-~600ms-vs-~300ms(Foss-Feig2010)+speech-specific-enlargement(Stevenson2014-J-Neurosci)+social=inherently-multi-modal-cascade-4-steps; §4-predictive-coding-3-theories: Hypo-priors(Pellicano2012-TiCS)+HIPPEA(Van-de-Cruys2014-Psych-Review)+Aberrant-Precision(Lawson2014-Front-Hum-Neurosci); all-3→prediction-delta-LARGER; IS=prediction-delta-REDUCTION-strategy; §5-Self-Pattern-Modeling: Compiled/Fresh-2-functions; "empathy-deficit"=BUSTED(Bird&Cook2013-alexithymia-sole-predictor-controlling); Double-Empathy(Milton2012+Crompton2020/2025-NatHumBehav-registered-replication); thin-slice-bias(Sasson2017-disappears-text-only); eye-avoidance=active-self-protection(Hadjikhani2017); ToM-critique(Gernsbacher&Yergeau2019); §6-masking: Hull2017-3-stage-model; Lai2017-d=0.98-gender-difference; mental-health-cost(Cook2021-systematic-review+Cage2019); chronic-mismatch→cortisol→burnout; late-diagnosis; §7-alexithymia: ~50%-autism-vs-~5%-general(Kinnaird2019-meta); alexithymia-NOT-autism-predicts(Bird&Cook2013+Shah2016); self-to-other-model(Bird&Viding2014); §8-special-interests: gap-direction-CONCENTRATED; monotropism(Murray2005+Dwyer2024-empirical); OCD-vs-Special-Interests-table; 92%-calming(Patten-Koenig2017); §9-EPF: Mottron2006-8-principles+Raven's-+30-percentile(Dawson2007)+detail-focused=STYLE(Happé&Frith2006); strengths-FROM-configuration; §10-meltdown/shutdown: OVERFLOW-not-tantrum; reduced-habituation+amplified-prediction-delta=TRIPLE-load; stimming=regulation(Kapp2019-4-functions); recovery-protocol; §11-developmental-trajectory: early-signs-12-18months; language-range; adolescence-risk-convergence; adult-outcomes(Howlin2004)+aging-gap(Happé2012); late-diagnosis-re-compilation; Optimal-Outcome(Fein2013-4-13%); Temple-Grandin-case; labeling-paradox; §12-ADHD×Autism-2D-model(Config×Tuning-table)+overlap-vs-distinction-table; §13-co-occurring-as-cascade: anxiety-39.6%(van-Steensel2011)+depression-23%/37%(Hollocks2019)+epilepsy-20-30%+GI-OR=4.42(McElhanon2014); §14-P1-P8-testable-predictions; §15-🟢🟡🔴+Q1-Q9; §16-cross-refs; 2026-06-09)
- [x] I11 ADHD-Trade-Off.md ✅ (Health-Conditions\Neurodiversity\; §0–§12+References; Neurodiversity-WHY-file; builds-on-ADHD-Observation.md; §0-cluster-position(3-files: WHAT/WHY/HOW); §1-evolutionary: polygenic-500+-loci-SNP-heritability-22%; DRD4-7R=ONE-piece-not-"the-gene"(Naka2011-NO-positive-selection); 3-hypotheses-all-🔴(balancing-selection/hunter-gatherer/neutral-drift); era-shift-table-4-eras(Hunter-gatherer→Agricultural→Industrial-PEAK-MISMATCH→Digital); spectrum-not-binary; §2-social-compilation-asymmetry: passive(neurotypical-micro-cues-auto)vs-active(ADHD-3-pathways: big-events+explicit+repeated-consequences); gaze-cueing-SELECTIVE(Psychiatry-Research-2016: eyes-fail-arrows-intact)+alpha-modulation-INVERSE(EEG-2019-n=45)+longitudinal-age-4-predicts-ADHD-6-7(PMC12087504-2025); social-cognition-improves-WITH-AGE(meta-49-studies-n=2449: large-children-NS-adults)+Sells2023(21-studies); 3-Compiled-Quality(genuine/schema/threat)+SST-small-effect(SMD-0.32-0.39+Bussanich2025-ES=0.09-negligible); 2-phase-passive→active-avoidance; 5-detection-signals(timing+micro-reciprocity+topic-flow+emotional-binary+observer-modeling-failure); PIB(Betancourt2024-ES-0.46-0.67+PIB-protective→crash); §3-masking-cost: passing-tax-PFC-budget-split(no-percentages-not-measured); ADHD-masks-LESS-than-autism(PMC11528950-2024-hierarchy); compiled-suppress-trajectory(framework-prediction-no-longitudinal-data); §4-Background-Pattern: 3-common-patterns(effort-not-enough+social-threat+cant-finish)+triple-bias; cortisol-CORRECTED(basal-LOWER-NatureTranPsych2021+reactivity-HIGHER-PMC5837926=hypo-tonic+hyper-phasic); spike-crash-cascade(vs-old-double-deficit); §5-satiation-profile: generative-dominant-bias+anticipation-vs-consummation(Plichta2014-d=0.48-0.58+PLOS-ONE-2014)+novelty-SHARED-vulnerability-not-distinct(PMC4097844); §6-3D-model(severity×fit×support)+subclinical-sweet-spot: creativity-g=0.36-clinical-no-benefit(Tran2026)+start-vs-sustain; §7-Self-Created-Threat: narrow-window+90:10-pull-push-ratio(framework-derived); §8-burnout-trajectory(5-phases)+late-diagnosis: women-5yr-later(EurekAlert2024-28.96vs24.13)+gender-ratio-3:1→1:1(PMC10173330)+4-step-post-diagnosis-process; §9-collective-role: complementarity(🔴-conceptual)+double-empathy-extension(🔴-ADHD-specific-no-data); §10-central-thesis: f(Hardware×Environment×Compilation); §11-🟢🟡🔴+CAN/CANNOT; §12-cross-refs; 2026-06-09)
- [x] I12 ADHD-Attention-Optimization.md ✅ (Health-Conditions\Neurodiversity\; §0–§12+References; Neurodiversity-HOW-file-3/3; builds-on-ADHD-Observation+ADHD-Trade-Off; §0-cluster-position; §1-foundation: threshold=hardware=unchangeable+domain-selection=HIGHEST-LEVERAGE(Hotte-Meunier2024+Tran2026)+A→B→C-internal-novelty-model(🔴); §2-environment-design-3+1: Condition1=safety-explicit-communication(parental-warmth-59-studies+written>facial-feedback)+Condition2=arc-decomposition-mini-arcs(4-principles: size+tangibility+transitions+variety)+Condition3=novelty+autonomy+immediate-feedback+Condition+1=AI-compensator(🟡-very-early); §3-reward-engineering: anticipation-deficit(Plichta2014)+Motivation≠Activation+feast-to-famine-4-steps+evaluative+direct-state-pairing+overjustification-trap; §4-external-PFC-scaffolding: 5-functions(working-memory+inhibition+time-perception+planning+emotional-regulation); AI-as-PFC-partner-5-applications(🟡); "outperform-neurotypical-with-scaffolding"=🔴-no-evidence; §5-repair-cycle: exercise-TOP-TIER(aerobic-2025-inhibition-g=0.761+flexibility-g=0.780+PMC10434964-SMD=0.611+chronic>acute)+sleep-73-80%-circadian-alterations(Frontiers2025)+5-component-repair-cycle(exercise+sleep+play+connection+re-fire); §6-social-compilation-acceleration: 5-strategies(safe-practice+mechanism>rules+video-review+explicit-feedback+pattern-extraction)+3-ADHD-social-advantages(directness+intensity+cross-domain); §7-big-arc-drive: valley-5-preparation-strategies(predict+pre-position+refresh+planned-switching+graveyard-prevention)+90:10-applied+inattention>hyperactivity-project-abandonment(PMC7515948-goal-neglect); §8-Background-Pattern-management: 4-detection-options(therapist/coach+partner+journaling+AI)+late-diagnosis-4-step-process(information→grief→recompile→optimization); §9-per-position-table: subclinical/mild/moderate/severe×strategy×medication+exercise-applies-ALL-positions; §10-hierarchy-9-levels+applicability-beyond-clinical; §11-🟢🟡🔴+CAN/CANNOT; §12-cross-refs; 2026-06-09)

**I2. Love (2 files)**
- [x] I13 Love-Romantic.md ✅ (Research\; §0–§14+References; Love=DRIVE-not-emotion; 3-stages(Lust+Limerence+Attachment); Hardware-Subsidy-TEMPORARY-18-36m; 3-Generative-Primitives×Love(❶Hardware-FLOOD+❷Self-Pattern-Modeling-Composite-MAX+❸Valence→Body-Base-Extension); 2-Stream-Model(Hardware-Stream-habituates+Modeling-Stream-anti-habituates); 2-Stream-Reward(Valence-Momentary+Valence-Structural); PFC-TRIPLE-blindness(self-reduces+PFC=Lawyer+Motivated-Inaccuracy); Serotonin↓=AMPLIFIER-not-cause(parallel-cortisol; root=genuine-uncertainty; SSRIs-relapse-80%); §6-Romeo-Juliet-4-amplifiers(Protect+Cortisol-Role③+Us-vs-Them+Reactance; Intensity≠Quality); §7-Trauma-Chunks×Partner-Selection(§7.2-trauma+§7.3-Self-Pattern-Modeling-childhood-bias+Fork-Mechanism-vmPFC-DRN-Controllability-Maier&Seligman-2016+7-variables+Resonance-Baseline-⑦+Functional-Avoidant+Attachment-labels=outcomes-mechanism-under-labels+§7.4-collective-schemas); §8-Compiled-red-green-flags; §9-Limerence=Gift+Window+Fuel(3-Satiation-Types: Cyclic+Tonic+Generative; Limerence=Generative-dominant; Boredom=Generative-dead+Tonic-invisible); §10-Transition-4-Directions(A-Actually-good+B-Mismatch+C-Habituated-stagnant+D-Drop)+Compiled-Fresh-Reveal; §11-Long-term(11-subsections: Compiled-Suppress=highest-leverage; Resonance-Decline-2-forces+1-fuel; Anti-compiled-suppress=differentiation-reframe; 4-Layer-Sustainability(Foundation+Modality+Amplification-PPR+Secure-Base+Trajectory); Entity-Access-Excess-bilateral-trap+unilateral-suffocation+3-origins); §12-Break-up-compound-grief(8-pathways+3-layers: Withdrawal+Amputation+Compound; Grief-A+B+C; Phantom-4-factor; Love↔Hate-shared-circuits; Decay-3-Layer; No-contact=natural-decay); §13-Honest-assessment(~35-🟢+~25-🟡+~12-🔴); 2026-06-09)
- [x] I14 Love-Unified.md ✅ (Research\; §0–§14+CrossRefs; "Love"=Entity-Compiled-Body-Base-Extension(ALL-types-same-root-mechanism); Valence-Structural-Smoothing=GENERAL-mechanism(not-romantic-specific; smoothing_capacity≈|Valence-Structural|−max(Schema_A,competing); 3-functions: Filter+Amplifier+Propagation); 2-Axis-Model(Depth×Channels; Foundational-vs-Additive; 4-Modifiers); Hardware-Subsidy-4-level×6-types(MAX-parent→child+MOD-child→parent+TEMP-romantic+NONE-friendship/mentor/pet); Satiation-3-types×6-love-types("Boredom"=Generative-dead+Tonic-invisible≠stopped-loving); Bond-Architecture-4-types×6-love-types(Attachment+Caretaking+Sexual+Affiliative; Resonance-Decline-2-forces+1-fuel; Anti-compiled-suppress; Domain-Coverage-5×4-matrix); §7-6-types-unified(Romantic+Parent→Child(§7.2a-Hardware-Seed+§7.2b-Valence-Structural×Compiled-Matrix-Smoothing-vs-Fixing+§7.2c-Self-Pattern-Modeling-3-Modes)+Child→Parent-3-stages+Friendship+Mentor+Pet/Parasocial; Calibration-hierarchy; 17-dimension-comparison-table); §8-Entity-Access-gradient×6-types(healthy-Level4; Excess-Level5; Calibration-dynamics; Paradox-strongest-bond=hardest-to-calibrate); §9-4-Layer-Sustainability+3-Firing-Modes+4-silence-types; §10-Phantom-4-factor+Grief-A+B+C+Love↔Hate-shared-circuits+Decay-3-Layer; §11-Edge-cases(Stockholm+Combat-bond+Phantom+Anti-smoothing-scale+By-Product-Scale); §13-🟢/🟡/🔴+9-open-Q+10-testable-P; 2026-06-09)

**I3. Global (5 files)**
- [x] I15 Human-AI-Future.md ✅ (Research\Global\; §0–§12+CrossRefs; AI-has-NO-agency(no-body-needs→no-drive→no-self-direction; all-AI-risk=human-decisions-through-tool); §0-Architectural-diff-table(Substrate+Body-feedback+Efference-copy+Self-Pattern-Modeling+Valence+Co-regulation+Agency); §1-5-reasons-body-feedback-irreplaceable; §2-3-Layer-complement(AI-detect+Human-feel-check+Self-verify)+Bottleneck-shift; §3-3-risk-types-table(Individual-amplifier+Social-arms-race+Species-robot-far-off); §4-Amplifier-5-failure-domains+manageable; §5-Social-main(§5.1-Prisoner's-Dilemma+Status+Approach-tag-loop+§5.2-Salami-Slicing+Tag-persistence+§5.3-5-difficulty-factors+§5.4-Chain-break-push-back-possible); §6-Species-risk-note+logical-dead-end; §7-Symbiosis(Efference-copy-4-levels+5-modes-different-tags+Melody-Accelerator+Drive-PFC-Resolve-shift+4-conditions); §8-5-human-upgrades+hardware-upgrade-timeline; §9-Collective-orientation=decisive-factor(ratio-care-collective/care-self); §10-2-axis×3-levels-2D-space(Level1-Screen+Level2-Robot-VTC+Level3-BCI-outside-scope); §11-🟢/🟡/🔴+7-open-Q; 2026-06-09)
- [x] I16 AI-Self-Model.md ✅ (Research\Global\; §0–§11+CrossRefs; AI=AMPLIFIER-of-whatever-self-model-you-provide(wrong-model×AI=amplified-wrong; right-model×AI=amplified-growth); §0-Thesis+3-companion-file-trilogy(Social-Calibration+AI-Self-Model+Human-AI-Future)+MACRO-depends-on-MICRO; §1-5-subsections(§1.1-amplifies-any-model-incl-wrong+§1.2-AI-sycophancy-Sharma-2024-ICLR+Wei-2023+Not-One-Thing-2025+§1.3-self-model=Trust-Injected-filter-stakes-higher-post-AI+§1.4-Automation-bias-Parasuraman-1997-Goddard-2012-Buçinca-2021-Bansak&Hainmueller-2024-Schemmer-2024+Dunning-Kruger×AI-Fernandes-2025-Bastani-2024+§1.5-Honest-AI-STILL-amplifies-body-checks-COHERENCE-not-TRUTH-formula=f(output-coherence×existing-chunks)); §2-AI-delays-correction-cycle(§2.1-normal-cycle+§2.2-AI-breaks-cycle-diagram(without/misuse/correct)+§2.3-Dismissability-Asymmetry-Peer=body-to-body(hard-dismiss)-AI=text-to-PFC(easy-dismiss)+§2.4-Positive-body-feedback+wrong-model=also-dangerous); §3-DUAL-CHECK-v2.0(§3.1-Body=quality-controller(~90%)+3-failure-modes(Evolution-Lag/Wrong-Chunk/Schema-Override)+AI-amplifies-②specifically+§3.2-4-case-matrix(Body-YES+Domain-NO=MOST-DANGEROUS-in-AI-era)+§3.3-2-step-Protocol+per-domain-domain-check-table); §4-STALE-CALIBRATION-v2.0(§4.1-calibration-has-expiry+§4.2-5-stages(Trained→Transition→Solo+AI→Stale→Crash)+§4.3-AI-masks-staleness(AI-past-data+expert-past-chunks=double-confirmation-of-past)+§4.4-peer-review-catches-what-AI-misses+§4.5-5-trends-increasing-risk); §5-5-failure-domains+pattern-summary-table+3-tier-verification(AI→body-check→domain-verify); §6-Right-model×AI=amplified-growth(symbiosis-principles+per-domain-correct-use+compound-evidence-Banerjee-2024-Henry-2024-Fogliato-2022); §7-Self-Check-Diagnostic-6-questions(§7.1-Approach/Avoidance+§7.2-Body-feedback+§7.3-Skill-test+§7.4-Feedback-loop+staleness+§7.5-Confirm/Challenge+§7.6-Stale-calibration-v2.0); §8-Body-listening=AI-era-skill(§8.1-paradox-AI-stronger→body-listening-MORE-important+§8.2-training-methods+§8.3-3-step-iterative-loop+§8.4-knowing-doing-gap-amplified); §9-Future-tech-3-levels(external/wearable/BCI)+understand-before-augmenting; §10-🟢/🟡/🔴+10-open-Q; 2026-06-09)
- [x] I17 Social-Calibration.md ✅ (Research\Global\; §0–§8+CrossRefs; Society=AUTO-CALIBRATION-SYSTEM(7-functions-run-automatically-individual-doesn't-need-to-understand-mechanism); §0-Position+3-companion-files(Social-Calibration=WHERE-WE-CAME-FROM+Human-AI-Future=MACRO+AI-Self-Model=MICRO); §1-Thesis(thermostat-metaphor+7-function-table+Compilable-Architecture→collective=requirement); §2-7-functions(§2.1-Direction-Imagine-Final-pre-installed+§2.2-Push-external-threat→cortisol+§2.3-Pull-social-reward-Body-Feedback-Precondition+§2.4-Repair-cortisol-reset-circadian+§2.5-Check-domain-feedback-gossip+§2.6-Identity-NEW-rites-of-passage-Van-Gennep-1909-Turner-1967+§2.7-Connection-NEW-Dunbar~150-Holt-Lunstad-2010); §3-4-stage-historical(§3.1-Hunter-Gatherer-all-7-built-in+§3.2-Agricultural-religion-covers-7/7-guilds-formalize+§3.3-Industrial-strained-but-holding+§3.4-InfoAI-era-ALL-CARRIERS+FUNCTIONS-failing-simultaneously+Disruption-Cycle-still-applies); §4-Mechanism-mapping-table+§4.1-Temporal(Direction/Push/Pull/Check/Repair)-vs-Background(Identity/Connection); §5-3-wave-compound-breakdown(Modernity+Information+AI)+per-function-detailed+evidence-summary(Putnam-2000+Holt-Lunstad+Twenge-2019+Pew-2022+Cho-2018+Walker-2023)+cross-reference-framework-evidence; §6-What-remains(body-feedback+family-core+domain-feedback+rituals+community)+§6.2-Transition-gap-diagram(old-declining+new-not-mature)+§6.3-3-directions(Self-calibration-2-LEVELS(Level1-basic-awareness-collective-teaches+Level2-deep-creator-diverger)+AI-as-tool(can-replace-Direction/Check-partial-CANNOT-replace-Connection/Identity/Repair/Push)+New-collective-structures-🔴-emerging)+§6.4-Framework-for-2-groups(transition-gap-navigators+creators-divergers); §7-🟢/🟡/🔴+7-open-Q; 2026-06-09)
- [x] I18 Uncanny-Valley.md ✅ (Research\Global\; §0–§10+CrossRefs; Uncanny-valley=VTC–Self-Pattern-Modeling-CONFLICT(System1-VTC-Hardware-fires-AGENT-DETECTED+System2-Self-Pattern-Modeling-CANNOT-SIMULATE); §0-Core-thesis+practical-implication; §1-Background(Mori-1970+United-Robotics-Survey-2024-~8000-people-~60%-uncomfortable+fMRI-Saygin-2012-aIPS+Rosenthal-von-der-Pütten-2019-vmPFC-dip+real-world-failures-Sophia-AIDOL-Polar-Express-Cats); §2-Framework-mechanism(§2.1-VTC-Hardware-Trigger+§2.2-Compiled-EMPTY+Fresh-WRONG-dual-failure+§2.3-3-body-feedback-dynamics-compound(Chunk-Shift+Chunk-Miss+Prediction-Delta-NEVER-resolves)+§2.4-Hardware-Social-Drive-frustrated-❶-Connection+§2.5-Per-Agent-Valence-CANNOT-compile-vmPFC-dip-explained); §3-4-layer-model+7-entity-type-table(Roomba/Spot/Humanoid-robot/Cartoon/Text-AI/Deepfake/Future-robot); §4-4-reasons-why-almost-human-WORSE(VTC-threshold+lifetime-compiled-baseline-SNC-effect-Crespi-1942+prediction-unresolvable-category-confusion+social-promise-broken); §5-Individual-differences(§5.1-Developmental-trajectory-4-stages-0mo→adult+§5.2-4-factors-Self-Pattern-Modeling-library+Culture+SF-schema+Alexithymia); §6-5-design-principles(§6.1-Congruence-appearance-matches-behavior+§6.2-VTC-Management-control-agent-cues+§6.3-Self-Pattern-Modeling-Friendly-Predictable+Readable+Contingent+§6.4-Schema-Provision-4-methods+§6.5-Exposure-Pathway-5-steps); §7-AI-era(§7.1-Deepfake=reverse-uncanny-Self-Pattern-Modeling-succeeds-until-discovered-Chunk-Shift+§7.2-Text/Voice/Visual-AI-avatar+§7.3-Robot-Companion-Elderly-Care-BODY-LEVEL-DECEPTION-risk-clearly-machine-better+§7.4-VTC–Self-Pattern-Modeling-Classification-3-types-Type1-Robot-Tool+Type2-Human-Like-Robot-Tool+Type3-Robot-New-Species+logical-dead-end); §8-fMRI-mapping-6-regions(aIPS+vmPFC+TPJ+FFG+Amygdala+dACC)+computational-model-multiplicative; §9-🟢/🟡/🔴+Falsifiable-P7-prediction(strange+consistent=NO-uncanny-vs-humanoid+inconsistent=UNCANNY); §10-CrossRefs; 2026-06-09)
- [x] I19 Innovation-Geography.md ✅ (Research\Global\; §1–§14; Innovation=f(Chunk-Density×Processing-Capacity×Resources×Time)+Climate=modifier-only; §1-Core-hypothesis+formula; §2-Mechanism(§2.1-PFC-needs-chunks+§2.2-Trade-hub=highest-chunk-density+§2.3-Competition-multiplier+§2.4-Competition-Driven-Domain-Expansion-speciation-analogy+cascading+AI-era-dev-example); §3-Timeline(§3.1-Ancient-7-clusters-Sumer/Egypt/Indus/Greece/Rome/China/India+§3.2-Medieval-3-clusters-Islamic-Golden-Age/Song/Timbuktu+§3.3-Early-Modern-4-clusters-Italy/Dutch/British/Austro-Hungarian); §4-Modern-era-USA/China/India/Singapore+Internet; §5-Post-1400-Europe-convergence(§5.1-Chunks×Resources×Competition×Climate-multiplicative+§5.2-Decisive-moment-chunk-injection-timeline); §6-Innovation-speed-exponential(chunks²+distribution-speed+AI-discontinuous-jump); §7-Counter-examples(Venice/China/North-Korea/Mongolia/Iceland-all-confirm-chunks>climate); §8-Climate-real-role(macro-5-10%+individual-25-35%-2-scales-2-weights); §9-3-eras(§9.1-Trade-Hub-Era-geography-60-70%+§9.2-Internet-Era-4-barriers-language/jargon/volume/synthesis-geography-30-40%+§9.3-AI-Era-5-barriers-eliminated-what-remains-human-geography-5-10%+§9.4-summary-table-bottleneck-shifts-external→internal); §10-AI-era-case-study(§10.1-AI-removes-barriers+§10.2-Intuitive-thinker+AI=perfect-complement+§10.3-4-groups-liberated-AI-equalizer+§10.4-body-remains-final-bottleneck); §11-Testable-predictions+applications(personal/team/city/nation); §12-Existing-research(Jacobs/Diamond/Ridley/Romer/Mokyr/Bernstein+4-new-contributions); §13-6-open-questions; §14-Connections+honest-assessment; 2026-06-09)

**I4. Birth-Rate-Decline (9 files)**
- [x] I20 00_Overview.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§8; Birth-rate-decline=DOMAIN-FEEDBACK-body-says-conditions-not-sufficient-for-next-generation; §1-Asset→Cost-shift-history(survival/economic/connection/status-BEFORE-vs-AFTER); §2-5-axes(①Children-asset→cost+②Competing-Imagine-Finals+③Repair-cycle-broken-NOT-cortisol-too-high+④Compiled-schemas-childhood-Collective-Body-Trust-Compile+⑤Connection-declining-nuclear-family); §3-Universal-pattern-table(Poor-High/Developing-Declining/Developed-Low/Highly-Developed-Very-Low)+Demographic-Transition-Theory-Thompson-1929; §4-6-case-studies+3-Layer-model(Layer1-Infrastructure-policy-CAN-fix+Layer2-Desire-culture-NOT-policy+Layer3-Meaning-deepest-policy-CANNOT-touch)+summary-table-all-6+4-trap-types(Cost/Schema/Ceiling/Sufficiency); §5-Solution=create-conditions-NOT-incentivize(when-body-WANTS+5-axes-fix+4-ineffective-solutions-cash/propaganda/coercion); §6-Folder-structure; §7-🟢/🟡/🔴(Meaning=ultimate-determinant-Israel-2.9-vs-Finland-1.25=same-GDP-welfare-different-meaning-TFR-2.3x); §8-Open-questions-BR3-BR12; 2026-06-09)
- [x] I21 01_South-Korea_Analysis.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§11; Korea=ALL-5-axes-broken-simultaneously+NO-compensating-factor=0.72-world-lowest; §1-Timeline-6.16→0.72-in-63-years+Key-stats(cost-$272K-#1-world+Seoul-TFR-0.581+$270B-spent-still-fell); §2-5-axes(①Children-cost-hagwon-78%-kids+suneung-1-exam-decides-life+②Competing-Imagine-Finals-career-freedom-travel+③Repair-broken-1872hrs-#5-OECD-gender-gap-29%+④Compiled-schemas-3-sources-A-bored-parents-B-own-childhood-C-peers-D-34yr-anti-natalist-legacy+⑤Connection-nuclear-family-Seoul-50%-pop); §3-Self-reinforcing-downward-spiral(3-feedback-loops+WHY-Korea-went-past-Japan-1.3); §4-Hell-Joseon=Domain-Feedback+Sampo→Opo→Chilpo→N-po=Imagine-Final-Collapse; §5-Gender-conflict(Conflict=Overlap×Scarcity×Commitment+4B=body-detects-THREAT-across-L0-L1-L2+anti-feminism=STATUS-THREAT+MUTUAL-WITHDRAWAL=birth-collapse+digital-sex-crimes-compound); §6-3-generations(Rebuild-TFR-6.16→2.82+Miracle-2.82→1.47+Hell-Joseon-1.47→0.72+schemas-compound-like-compound-interest); §7-Policy-failure(5-reasons-carrot-bridge-inflation/schemas/repair/connection/gender-conflict+SMALL-effect-paternity-leave+working-hours+researchers-quote); §8-Comparison-Korea-Japan-China-worst-of-all-worlds-no-compensating-factor; §9-🟢/🟡/🔴; §10-9-open-questions; §11-Connections; 2026-06-09)
- [x] I22 03_China_Analysis.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§13; China=LARGEST-FORCED-SCHEMA-COMPILATION-in-history-35yr-1.4B-people; §1-Scale(324M-IUD+108M-sterilization+TFR-7.51→0.93+2025-7.92M-births-lowest-since-1949+−3.39M-pop+marriage-−53%+cost-#2-world+Shanghai-center-TFR<0.5+attitudes-56.79%→79.78%-in-3yrs); §2-One-child=3-phase-forced-schema-compilation(Phase1-behavioral-coercion-1980-1995-desire-unchanged+Phase2-internalization-1995-2015-behavior-becomes-genuine-preference+Phase3-schema-lock-in-2015-now-persists-after-policy-removed)=KEY-INSIGHT-"Policy-CAN-compile-schemas-removing-policy-CANNOT-undo-schemas"; §3-5-axes(①cost-#2-world-6.3x-GDP+②Competing-Imagine-Finals-TangPing-BaiLan+③repair-broken-996-culture+④compiled-schemas-STRONGEST-of-all-cases+⑤connection-4-2-1-burden); §4-Compounding=multiplicative-NOT-additive(×education+×housing+×996+×gender-imbalance+×psychology-Cameron-2013-Science+×4-2-1-burden-spiral); §5-Reversal-failures(2013-10%-registered+2016-bump-then-collapse+2021-mocked+2025-lowest-ever-despite-no-limit="removing-dam-from-dried-up-river"); §6-TangPing/BaiLan=Imagine-Final-Collapse(TangPing≈Sampo+BaiLan≈N-po+censorship-suppresses-language-NOT-schemas); §7-Gender-imbalance(peak-sex-ratio-121.18-2004+30M-bare-branches+bride-price-380K-RMB-Jiangxi+urban-women-choosing-independence+self-perpetuating-40yr); §8-Government-response(wrong-channel: $500yr-vs-$75-95K+censorship-vs-schema+declarative-promotion-vs-experience+Double-Reduction-tutoring-underground+Xi-childbirth-culture=rhetorical); §9-Population-forecast(2100~633M-−780M-from-peak+labor-crisis+aging-crisis+pension-dry-2035+GDP-declining); §10-3-country-comparison(Korea-0.75-vs-China-0.93-WHY+Japan-1.2-WHY+Confucian-vulnerability-pattern+Vietnam=mid-trajectory); §11-🟢/🟡/🔴; §12-10-open-questions-CN1-CN10; §13-Connections; 2026-06-09)
- [x] I23 04_France_Analysis.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§11; France=POLICY-CEILING-best-EU-but-not-enough; §1-Timeline(TFR-2.02→1.56+2025-lowest-since-WWI+births-833K→645K+key-stats-crèche-59%-ĐH-€178+comparison-France-Korea-Israel); §2-5-axes(France-fixes-2.5/5:①cost-strong+②competing-Imagine-Finals-cannot-fix+③repair-partial-35h-vs-Shabbat+④schemas-partial-shifting+⑤connection-partial); §3-Policy-arsenal(childcare+education+leave+financial+work-life+3.5%-GDP); §4-Why-higher-EU(vs-Germany-Rabenmutter-schema+vs-Italy-Spain-familialist-welfare-collapsed+vs-Nordic-workism-hypothesis); §5-Why-declining(①policy-retrenchment-2015+②desired-size-2.5→1.9-schemas-shifting+③eco-anxiety-new-Imagine-Final+④gender-double-burden+⑤postponement+⑥housing+Macron-demographic-rearmament-failed); §6-France-vs-Israel(policy-comparable-France-more-BUT-TFR-half-gap=shared-Imagine-Final+available-repair-vs-enforced-Shabbat+150yr-institutional-vs-3000yr-experiential+formula-desire>infrastructure); §7-Immigration(only-+0.1-TFR+second-gen-convergence-1-generation=schemas=environmental); §8-Lesson(Policy-CAN:cost+repair+gate+floor; Policy-CANNOT:desire+eco-anxiety+double-burden+shared-Imagine-Final+enforce-rhythm; FLOOR=f(policy)-LEVEL=f(desire)+TFR≈min(desire,infrastructure)); §9-🟢/🟡/🔴; §10-FR1-FR10-open-questions; §11-Connections; 2026-06-09)
- [x] I24 05_Finland_Analysis.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§12; Finland=PERFECT-WELFARE+TFR-COLLAPSE=DEFINITIVE-PROOF; §1-Timeline(TFR-1.87→1.25-lowest-since-1776+−33%-14yrs+Nordic-comparison-Finland-worst); §2-Paradox(has-everything:leave+childcare+free-edu+#1-happy+#2-gender-equality→still-1.25=policy-necessary-NOT-sufficient+axes-①③-fixed-②④⑤-NOT); §3-5-axes(①cost-FULLY-FIXED+②workism-competing-Imagine-Finals+③repair-partial-no-Shabbat-rhythm+④schemas-secularization-shift+⑤connection-44%-solo-declining); §4-Happiness-paradox(individual-contentment≠family-desire+3-different-reasons-Korea-cannot-vs-Vietnam-difficult-vs-Finland-dont-need-to=PURE-desire-bottleneck); §5-Workism(career-replacing-family-as-meaning+net-workism-tracks-TFR+Denmark-decreased-work-importance=highest-Nordic+beyond-equality); §6-Secularization(90%→69%-church+gap-members-0.5-more-children+Schubert-Oxford+Luoto-3.64-vs-urban-1.05=same-welfare-religion=only-variable); §7-Sufficiency-trap(welfare-enables-solo-comfortable+steps-1-5+body-needs-met=children=optional+comparing-traps-Korea-Cost-China-Schema-France-Ceiling-Finland-Sufficiency-Israel-None); §8-Nordic-comparison(workism+Nokia-scarring+secularization-pace+isolation-culture+childlessness-level+CULTURE>POLICY); §9-Final-lesson(3-layers-infra/desire/meaning+6-case-synthesis-table+Layer-3=ULTIMATE-DETERMINANT+when-Layer3-present-overrides-cost); §10-🟢/🟡/🔴; §11-FI1-FI10-open-questions; §12-Connections; 2026-06-09)
- [x] I25 06_Israel_Analysis.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§13; Israel=ANOMALY-developed-economy+high-TFR-2.9; §1-Timeline-stable-~3.0-for-45yrs+breakdown-Secular-2.0/TraditionalNonRel-2.2-2.5/TraditionalRel-2.8-3.0/ModOrthodox-3.77/Haredi-6.5+NonHaredi-Jewish-2.45-highest-OECD+Israel-vs-Korea-same-GDP-same-female-employment-TFR-4x-different=economics-cannot-explain; §2-5-axes-REVERSED(①cost-exists-but-OVERRIDDEN-by-evaluative-value+②Imagine-Finals-career+family-COEXIST-not-either-or+③repair-STRUCTURED-Shabbat+④schemas-children=good-millennia+⑤connection-STRONG-extended-family-Shabbat+summary-table-Korea-vs-Israel-every-axis-opposite); §3-Shared-Imagine-Final-4-layers-stacked(Layer1-Religion-be-fruitful=first-mitzvah+Layer2-Survival-replace-6M-77%-Iranian-threat+Layer3-National-each-child=future-soldier-mandatory-military-both-genders+Layer4-Social-family=default-childlessness=pitiful+4-layers-override-economic-cost+fertility-DECOUPLED-from-economics-because-Layer1-unconscious>PFC-cost-calculation); §4-Connection(Shabbat-70%+-weekly-even-secular+extended-family-nearby-470km-country+grandparents-active-childcare+kibbutz-legacy-society-has-shared-responsibility+military-both-genders=shared-experience=gender-solidarity-not-conflict); §5-Schemas(table-Korea-vs-Israel-each-schema-type+3000yr-time-depth+transmission-EXPERIENCE-not-policy+consistency-all-sources-religion+family+society+nation-all-say-birth=good+Soviet-immigrants-teens→2-3-children-adults→1-child=compilation-timing-determines-behavior); §6-Repair-cycle(Shabbat-6:1-rhythm-6days-drive+1day-repair+HIGH-stress-but-STRUCTURED-repair=Net-Health>0+contrast-Korea-no-cultural-enforcement+extended-holidays-Pesach-Sukkot-Hanukkah); §7-Secular-surprise(secular≠secular-West+93-97%-Seder+70%+-Shabbat-dinner+Layer1-still-active-at-unconscious-level+IVF-most-generous-world-free-unlimited-cycles-to-2-live-births-4.7%-births-IVF=ENABLE-desire-not-CREATE+IVF-bridge-for-people-who-ALREADY-want); §8-Post-crisis-fertility(1967-1973-Oct7-war→TFR-RISES+Oct7-detail-initial-drop-then-Jan-2024-3.10-Aug-2024-3.19-+10%-births-2024+mechanism-L0-threat-ACTIVATES-shared-Imagine-Final-vs-normal-countries-suppresses+3-conditions-required); §9-Warning-signs(secular→1.7-2030s+Muslim-3.29→2.71-sharp-decline+Christian-Druze-already-below-replacement+Haredi-7.5→6.5+Taub-Center-2025-demographic-crossroads+westernization-Layer1-weakening); §10-Lessons(CAN:shared-Imagine-Final>money+structured-connection+schemas-from-experience+IVF=enable-not-create+repair-cultural-structure; CANNOT:3000yr-DNA+existential-threat+small-geography+military-both-genders+fix≥3/5-axes-needed-Israel-fixes-4/5-cost-high-but-overridden); §11-🟢/🟡/🔴; §12-IL1-IL10-open-questions; §13-Connections; 2026-06-09)
- [x] I26 09_Vietnam_Analysis.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§11; Vietnam=THE-CROSSROADS-stabilize-or-follow-Korea-China; §1-Timeline-6.27→1.91-in-64yrs+16yr-plateau-2000-2016-was-PLATEAU-not-FLOOR+decline-2.11→1.91-in-3yrs-FASTER-than-China+regional-breakdown-HCMC-1.32/HaGiang-2.69/32-provinces-below-replacement+key-stats(housing-HCMC-34yr-income-5th-world+marriage-age-30.4-HCMC=Shanghai+61%-children-not-required+SRB-111.4+GDP-$5026+old-before-rich); §2-5-axes(①cost-★★★-rising-HCMC-40yr-PIR+②competing-Imagine-Finals-★★★-rising-FourNos-evidence+③repair-★★★-rising-48h+OT-no-Shabbat-no-RTT+④schemas-★★★-rising-transition-rural-old-vs-urban-new+62yr-2child-policy-compile+⑤connection-★★-rising-extended-family-eroding+summary-table-all-5-cases); §3-HCMC-canary(TFR-1.32-below-replacement-20yr+age-30.4=Shanghai+preview-vs-outlier-argument+Scenario-C-bifurcation-1.5-1.6-national); §4-Policy-VN-vs-China(comparison-table-duration-62yr-vs-36yr-enforcement-lighter-reversal-2025-vs-2016+VN-advantages:shallower-schemas+acted-earlier+less-gender-imbalance; VN-weaknesses:longer-policy+incentives-$118-vs-$180K; PopLaw-12-2025-removes-limits+7mo-maternity+social-housing); §5-FourNos(=Sampo+TangPing-Vietnamese-version+comparison-table-stage-drop-sequence+NOT-yet-Npo/BaiLan+UNFPA-desire-still-exists-stuck-by-barriers≠Korea-China-dont-want+window-closing); §6-Buffers(1-maternity-6-7mo+2-extended-family+3-Tet-1-2yr+4-regional-diversity+5-urbanization-38%+6-act-early+7-education-not-yet-extreme; ALL-ERODING+window-10-15-years-before-2035-2040-exhausted); §7-Confucian-zone(7/7-countries-ALL-ultra-low+VN=last-standing+4-mechanisms:education-status+filial-piety-quality-over-quantity+rapid-urbanization-breaks-family+hierarchical-overwork); §8-3-scenarios(A-stabilize-1.7-1.8-20-25%-needs-France-level-investment+B-Korea-China-1.0-1.3-25-30%-default-trajectory+C-bifurcation-1.5-1.6-45-50%-most-likely+timeline-2026-2030-decisive-window); §9-🟢/🟡/🔴; §10-VN1-VN10-open-questions; §11-Connections; 2026-06-09)
- [x] I27 09_Vietnam_Solution.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§10; Vietnam-Solution=applying-framework-to-specific-VN-case; §1-Diagnosis(COST-TRAP-primary+UNFPA-want-but-stuck+73%-delay-marriage-finances+62yr-policy=mild-schema-trap+housing-HCMC-34yr=extreme+Layer1=primary-bottleneck); §2-Regional-strategy(HCMC-1.3-extreme-cost-trap→housing+childcare+connection/Hanoi-1.6-2.1→housing+edu+gender/Mekong-1.62→economic+connection/NorthCentral-above-maintain/Highlands-above-raise-quality-not-pressure; PopLaw-2025-delegates-to-provinces=right-direction); §3-Layer1(#1-housing:995K-social-housing-Singapore-HDB-rent-to-own-speculate-tax+#2-childcare-0-3:nurseries-sliding-fee-Samsung-FDI-negotiate-WomensUnion+#3-education-prevention:Circular29-enforce-NO-suneung-diverse-pathways-free-preschool+#4-leave+work:maternity-6-7mo+paternity-10days+enforce-48h→40h+anti-discrimination+#5-financial:lump-sum→monthly-allowance-$20-40-per-child-means-tested+IVF-subsidy); §4-Layer2(①visible-happy-families-document-not-propaganda+②decompile-2child-62yr-schema-needs-time+removal+visibility+③first-birth-crisis-finance=fix-L1+genuine-community-activities-WomensUnion+④son-preference-reduce-via-visible-female-success); §5-Layer3(①Tet+homecoming-increase-12-15x-yr-monthly-FamilyDay+②community-bonds-modernize:multi-gen-housing-community-childcare-centers-NRD-phase3+③WomensUnion+YouthUnion-network-leverage:community-childcare-groups-parent-support-couple-forming-genuine+④family-heritage-preserve-NOT-create-new:Layer1-fix→family-less-suffering→heritage-self-sustains); §6-Budget(11.4%-GDP-vs-France-45%+$3.37B-allocated-2026-2030+HCMC-$4.2M-per-birth-incentive+target-0.5-1.0%-GDP-$2.5-5B+strategy-do-more-with-less:WomensUnion-free-infra+extended-family-free-childcare+digital-economy-revenue-growing+FDI-Samsung-leverage+social-housing=investment-not-spending); §7-Timeline(Phase1-2026-2030:TFR≥1.85+Phase2-2030-2036:TFR≥1.7+Phase3-2036+:TFR≥1.6-1.7); §8-What-NOT-to-do(lump-sum+propaganda+welfare-only+restrict-divorce+edu-arms-race-free+wait-and-hope+pressure-highlands); §9-Measurement(leading:marriage+attitudes+PIR+childcare-coverage/concurrent:births+first-birth-age/lagging:TFR+cohort+next-gen-attitudes+red-flags); §10-🟡/🔴; 2026-06-09)
- [x] I28 100_Solutions.md ✅ (Research\Global\Birth-Rate-Decline\; §1–§10; Solutions=Imagine-Final-for-global-melody=destination-not-road-map; §1-Imagine-Final(society-where-body-NATURALLY-wants-children-not-due-to-coercion-or-money-but-conditions-sufficient+3-layers:L1-not-much-more-expensive+L2-positive-default+L3-has-meaning+when-all-3-no-encouragement-needed+each-country-own-path); §2-Priority(L1-FIRST→L2→L3+CANNOT-fix-L2-while-L1-broken+CANNOT-fix-L3-while-L1+L2-not-in-place+BUT-L3-takes-longest-so-start-parallel+priority-matrix:COST-TRAP→L1-urgent+SCHEMA-TRAP→L1+L2+CEILING-TRAP→L2+3+SUFFICIENCY-TRAP→L3+2); §3-Diagnostic(4-questions:want-but-cannot→cost-trap/dont-care→desire-problem/past-suppression-policy→schema-trap/no-shared-meaning→sufficiency-trap); §4-Layer1-Infrastructure-checklist(childcare-0-3-MOST-IMPORTANT-France-59%+education-no-arms-race+housing-PIR≤10yr+leave-both-genders-maternity+paternity-81%-uptake+monthly-financial-not-lump-sum+IVF-enable-not-create+expected-effect-cost-trap-TFR+0.2-0.5-vs-sufficiency-trap-TFR+0); §5-Layer2-Desire(compile-via-experience-not-declaration+propaganda-fails:Macron+Xi+Korea+①visibility-happy-families+②integrate-competing-Imagine-Finals-career+children=BOTH-necessary-not-sufficient+③schema-trap-decompile-via-experiential-override-15-20yr+④first-birth-crisis-Finland-75%-decline+partner-finding=barrier+community-spaces+⑤immigration-convergence=schemas=environmental); §6-Layer3-Meaning(=Imagine-Final-family-active-at-L1-not-L2+3-scales:individual>community>national+individual=closest-strongest-1-happy-friend>1000-posters+community=Luoto-3.64-vs-Tampere-1.06=same-country-same-welfare+national=too-far-only-existential-threat+hierarchy-bottom-up-not-top-down+approaches:fix-L1+L2→L3-emerges+structured-connection-rhythm+each-place-finds-own-meaning+limits:no-proof-of-concept-at-national-scale+biggest-open-question); §7-7-principles(diagnose-before-treat+remove-barriers>incentivize+experience>declaration+ongoing>lump-sum+both-genders+act-early+floor+ceiling-simultaneously); §8-Ineffective(lump-sum-strongest-evidence-across-all-cases+propaganda+removing-limits-alone+banning-abortion+welfare-alone+restricting-divorce+government-matchmaking); §9-How-to-use(5-steps:position→layer→actions→avoid-§8→implement-measure-adjust+AI-prompt-template); §10-🟢/🟡/🔴; 2026-06-09)

**I5. Human-Learning (11 files)**
- [x] I29 Child-Development-Mechanism.md ✅ (Research\Human-Learning\Child-Development\; §0–§11; PFC-Reframe(hardware-online-chunks-missing-Hodel2018-5-pillars:synaptogenesis+fNIRS+resting-state-networks+myelination+consciousness-signature)+PFC-Inference-Ladder-L0-L4+Receptive-Productive-Asymmetry+PFC-Budget; §2-Compile-Architecture(1Engine-Hebbian-LTP+3Modulators:Entity-Valence-Bias/PFC-Modulation/Sleep-Maintenance+3-Exposure-Channels+3-Compile-Types:Genuine/Schema/Threat+External-Install-Trust-Gated+5-Parameter-Formula+Compiled/Fresh-ratio+Multi-Stream-Compile-4-streams-simultaneous); §3-Approach/Avoidance-Tags(Body-State-at-Compile+4-Threshold-gradient+Structural-vs-Current-Valence+Salami-Slicing+Valence-Propagation+Mixed-Valence-Cacioppo1994+Triple-Bias+Reconsolidation-Window-4-6hr-Nader2000+Extinction≠Erasure+Neural-Wear-PFC-dendrites-retract-amygdala-grow-Arnsten2009+ACE-Felitti1998+Recovery-Asymmetry); §4-Chunk-Dynamics(Gap/Miss/Shift)+Dual-Pull-Architecture+Attachment-Prerequisite(Hardware-Drive-Eisenberger2003+Hardware-Subsidy-oxytocin+Entity-Compiled-Hub-and-Spoke-Patterson2007+2-Asymmetric-Bonds+Co-Regulation→Self-Regulation+Virtual-Chunks+Phantom-4-Factor+Trust≠Valence+3-Trust-Sub-Dimensions:Authority/Competence/Intention+4-Formation-Sources+Build-Slow-Collapse-Fast+Mother=First-Coordination-Node); §5-Feeling-Development(7-Layer-Fidelity-Gradient-RawSignals→Integration→Consciousification→Observation→Location→Labeling→Explanation+per-age-development+Caregiving-Label-Mechanism-3-outcomes+Feeling-Fidelity→Self-Pattern-Modeling-prerequisite-Bird&Cook2013+Self-Observation-§5.4-APPLICATION-3-2-Axis-Model-Gradient-Level-0-6-Caregiver-ON/OFF-Compiled-Quality-table-Keystone-cascade+External-Scaffold-per-level); §6-Self-Pattern-Modeling-Bootstrap(3-mechanisms:Arousal-Contagion/Self-Pattern-Modeling/Resonance+Timeline:0-6m→6-9m→14-18m→18-24m→2-4y→4-7y+Animism=healthy+Prerequisite-Chain+6-Consequences); §7-Autonomy(Efference-Copy-von-Holst1950+vmPFC+DRN-Maier2016+Hardware-Subsidy-for-self-action+PFC-Budget×Autonomy+Compiled/Fresh×Autonomy+5-Phase-Arc+Child-A-vs-B); §8-Cortisol(Amplifier-Not-Cause-3-evidence+3-pain-sources+3-states+Sleep=Repair+2-tier-calibration+Recovery-Asymmetry+Direction>Level+Dissonance-Signal-Architecture+PFC-Budget×Cortisol); §9-Observation-Parameters-emergence-timeline+Imagine-Final-v3.0-development-trajectory(hardware-prediction≠Imagine-Final+0-6m+6-18m+18m-3y+3-6y)+7-Consequences; §10-🟢12/🟡13/🔴7; 2026-06-10)
- [x] I30 Natural-Development.md ✅ (Research\Human-Learning\Child-Development\; §0–§10; LAYER-2-in-5-tier-architecture=PHENOMENA-file-not-Mechanism; §0-Paradox(society-invests-6-18y-foundation-forms-0-6y-mostly-natural+4-file-map+reader-guide); §1-Hardware-at-start(PFC-online-from-prenatal-Hodel2018+synaptogenesis-overproduction-then-pruning-use-it-or-lose-it-Huttenlocher1979+myelination-order:brainstem→sensory→motor→language→PFC-intracortical-Yakovlev1967+body-base-0-100%-pure); §2-Natural-behaviors(Oral-Exploration:mouth=highest-receptor-density-4-purposes-vagus-self-soothe-immune+Crawling:5-purposes-cross-lateral-vestibular-depth-perception-hand-strength-autonomy-AAP-against-baby-walkers+Standing-Falling:17-falls-hour-Adolph-3-purposes-parent-reaction-compiles-INTO-schema+Touch-Grab-Throw:4-purposes-cause-effect-agency+Crying:4-purposes-NOT-manipulation-body-signal-training-co-regulation-Trust×Self-Observation-DUAL-TRAINING-Trust≠Valence+Babbling:4-purposes-statistical-learning-parentese-OK+Imitation:3-purposes-Self-Pattern-Modeling-bootstrap-Mirror-Neuron-Rejection+Free-Play:5-purposes-Simulation-Engine-first-run-pretend-play=FIRST-Imagine-Final-possible); §3-Sleep(Offline-Maintenance-6-mechanisms:SHY-Homeostasis-Tononi&Cirelli+Hippocampal-Replay-Wilson&McNaughton-only-exposure+Active-Consolidation-Born&Wilhelm-RAM→ROM+Creative-Linking-REM-Cai2009+Emotional-Decoupling-REM-Walker2017+Gist-Extraction-Payne2009+Growth-hormone+~1.5-exposure-~4.5-optimization+REM-newborns-50%-vs-adults-20-25%-endogenous-stimulation-self-testing+Night-waking=normal=safety-check+Nap=maintenance-window); §4-Timeline(0-3m:sensory-world-social-smile-6-8wk+3-6m:voluntary-reaching=first-agency+6-12m:crawling-pointing=joint-attention-stranger-anxiety=progress-separation-anxiety=attachment-working+12-24m:walking-NO!=celebrate-autonomy-tantrum=emotion-strong+PFC-zero-PFC-Budget-depleted+2-4y:WHY=gap-direction-clear+pretend-play=SE-running+imaginary-friend=Self-Pattern-Modeling-calibrating+early-lying=Theory-of-Mind+4-6y:complex-play-meaningful-friendship-4-Layer-Sustainability+natural-readiness-pre-academic+fairness-sensitivity+Personal-Melody-beginning+Trust+Self-Observation milestones-table); §5-Support-principles(Safe-not-sterile+Follow-child-not-lead+Respond-not-react-social-referencing+Diverse-environment-open-toys>closed+Presence>intervention+Model-don't-preach-Self-Pattern-Modeling-24/7); §6-Mistakes(Blocking-natural-behaviors+Overprotection+Early-academic-pressure-Finland-7y-catches-up-or-surpasses-at-10-11y+Screens-VTA-habituation-3-satiation-types-3-firing-modes+Suppressing-emotions-Trust-collapse-when-lying+Over-scheduling-PFC-Budget-depleted+Comparing-Structural-Valence-damage); §7-Framework-lens(Approach/Avoidance-Tags×parenting-4-threshold-reconsolidation-Hardware-Subsidy-Mixed-Valence-Multi-Stream-knows-but-doesn't-do+Chunk-dynamics-Gap/Miss/Shift-Gap-Direction+Connection-Entity-Compiled-2-asymmetric-bonds-Coordination-Node-Trust-sub-dimensions-Secure→Explore→Learn+Cortisol-amplifier-not-cause-Direction>Level+Observation-parameters-emerge-chunks-sufficient+Imagine-Final-v3.0-4-stages+Feeling-7-Layer-Self-Pattern-Modeling-bootstrap-Self-Observation-Level0→2-Compiled-Quality-table-Keystone-Cascade); §8-Honest-assessment(🟢12-areas+🟡7+🔴7+3-risks:anxiety+cultural-bias+burnout+Good-enough-parenting-Winnicott); §9-10-open-questions; §10-full-cross-refs; 2026-06-10)
- [x] I31 Skill-Introduction.md ✅ (Research\Human-Learning\Child-Development\; §0–§11; LAYER-2-in-5-tier-architecture=APPLICATIONS-file(distinct-from-PHENOMENA=Natural-Dev+MECHANISMS=Mechanism); §0-Position(4-file-set+how-to-read+v7.8-concepts:chunks-compile+approach/avoidance-tag+body-signal=prediction-delta+readiness=prerequisite-chunks+schema); §1-Principles(Readiness>Age:3-conditions-biological+interest-signal+no-resistance-signal+Gap-Direction-lens+WHY-readiness>age-approach-vs-avoidance+Body-Signal-Decides:3-tier-body-feedback-Tier1-2-only-NOT-yet-Tier3+Compiled-state-vs-Fresh-state+Dissonance-Signal-Architecture+Self-Observation-Level×Readiness:Level1/2/3+Caregiver-ON/OFF-switch-for-body-listening+Skill-Serves-Imagine-Final:NOT-parent-Imagine-Final+Simulation-Engine-limitation-0-6y+durable-interest-4-6y+Quality>Quantity:deep-compile-Generative-vs-Reactive-Firing-Modes+mastery-confidence-spillover+MAX-2-3-per-week-with-guideline-table+Process>Result:threat-path-vs-novelty-path+Hardware-Subsidy-for-process+4-steps×Compile-Type:Experience-leads-Trust-follows-3-Compile-Types(Experience/Trust/Expertise)+Multi-Stream-4-streams-VALUE-first-CONTENT-second+"can-play-but-hates-it"=Content✓-Value✗+Trust×Instructor=VALUE-amplifier:3-sub-dimensions+first-weeks-build-trust+love-the-teacher→learn-the-lesson+choose-teacher-child-LIKES>most-qualified); §2-4-Steps(Exposure+Interest+Guided-Play+Structured+approach/avoidance-tag-per-step+Valence-dynamics-Current→Structural+Multi-Stream×4-steps+Withdrawal:3-withdrawal-types-distinguished-by-Multi-Stream-Value-avoidance-vs-Content-satiation-vs-Habituation+Sensitive-Periods-table:phoneme/pitch/gross-motor/fine-motor/syntax/reading+Sensitive≠Critical+Triple-Bias-first-experience-sets-3-biases+Critical-Asymmetry:PFC-path-SLOW+Entity-Valence-path-FAST+Modeling-mechanistic-basis+Hardware-Subsidy+Entity-Valence=compound-effect); §3-Motor(Swimming:water-trust-prerequisite+4-steps+Cycling:balance-bike>training-wheels-mechanistic-reason+Sport:diversity-first-specialization-later-Côté-Lloyd-per-sport-readiness-table+Dance:natural-rhythm-response+ballet-warning-pre-ballet≠real-ballet+pointe-not-before-11-12); §4-Music(Foundation-Triangle:Listening+Singing+Rhythm+all-3-prerequisite-for-instruments+parent-singing>recorded-music+absolute-pitch-window+Piano:Suzuki-vs-Traditional+practice-principles-5min/day+Violin:fractional-sizes-Suzuki-parent-must-attend-every-lesson+Guitar/Ukulele:ukulele-as-gateway+Drums:most-natural-instrument-lowest-entry-barrier+Wind:latest-start-age-8-10); §5-Cognitive(Reading:oral-language+phonological-awareness+print-awareness+letter-knowledge+4-steps+child-reads-books-15min-day×5y=450hr-exposure>flashcard-drills+Writing:motor-prerequisites-5-stages-scribbling→letters+pincer-grip-foundation+reading-before-writing-NORMAL+Math:subitizing-innate+concrete-before-abstract+3-counting-steps:rote→one-to-one→cardinality+L2:OPOL+immersion>instruction+class=1hr-week=vitamin-not-main-meal+50hr/yr-vs-immersion-2000hr-40×-difference+Logic:puzzles-by-age+construction-progression+board-games+unplugged-coding-conditionals-loops-through-games); §6-Creative(Drawing:4-stages-scribbling→pre-schematic→schematic+process-art+coloring-books-creativity=0+phrases-that-kill-creativity+Construction:age-progression-knob-puzzle→duplo→kapla→technic+free-build>instruction-sets+Storytelling:developmental-arc-2-3y-sequence→3-4y-central-event→4-5y-problem-resolution→5-6y-complex+5-support-steps+1-sentence-every-evening); §7-Hardware-Calibration(DRD4-4R:instruction-following-OK-vs-7R/ADHD:hyperfocus-short-bursts-novelty-within-practice+Modality:somatic-demo>explain-vs-verbal-add-motor+Sensitivity:HSC-PFC-Budget-depletes-faster-dissonance-amplification-stronger-small-group-first+Low-Sensitivity-needs-more-stimulation+Temperament:cautious-warm-up-needed-vs-bold-encourage-depth+Trust-per-entity:trust-DEFAULT-first-weeks-build-trust); §8-Mistakes(7-common:jump-to-step4+parent-Imagine-Final+too-many-skills+comparing+result-not-process+not-accepting-withdrawal+blaming-child-not-approach)+Warning-Signs:physical+behavioral+emotional+relational+Resonance-Decline:Compiled-Suppress+Reward-Habituated+4-Layer-Sustainability×skill-practice; §9-🟢8/🟡6/🔴5+4-risks; §10-7-open-questions; §11-full-cross-refs; 2026-06-10)
- [x] I32 Mother-Optimization.md ✅ (Research\Human-Learning\Child-Development\; §0–§12; LAYER-2-in-5-tier-architecture=MEDICAL-HEAVY-file-framework-lens-LIGHT(distinct-from-other-3-Child-Dev-files); §0-Position(4-file-map+how-this-file-differs:medicine=central-framework=lens-only+Guilt-Prevention-§0.3:5-points-prenatal≠destiny-brain-plastic+v7.8-terminology:cortisol=amplifier+direction>level+baseline-calibration+PFC-hardware-online-prenatal); §1-Fetal-brain-timeline(T1:weeks3-4-neural-tube+neural-tube-defects+folic-acid-CRITICAL-TIMING-before-knowing+weeks5-8-regionalization+week7-neurogenesis-250k-neurons-per-minute+T2:migration+axon-growth+synaptogenesis-begins+hearing-~week20+fetal-kicks=self-testing+compiling-motor-chunks+T3:myelination+fastest-brain-growth+cortex-folding-gyrification+fetal-REM=offline-compile+final-assembly-line:breathing+swallowing+sucking+visual-timeline); §2-4-Hardware-factors(Genetics:blueprint-not-destiny-DRD4+COMT+5-HTTLPR-genes=range-not-fixed-point+Fetal-Activity:self-testing+compiling-5-behaviors+Mother-CAN-indirectly-influence+Maternal-State:the-main-focus-§3-§7+Hardware-Subsidy-for-mother-v2.1+Mother=first-Coordination-Node-v2.1+Oxytocin=Trust-Hardware-v2.3:receptor-ready-prenatal-trust-needs-post-birth-data+Interoception=Self-Observation-Hardware-v2.3:insula-T2-T3-hardware-yes-application-not-yet+Stochastic:random-variation=accept+control-map-visual); §3-Cortisol-mechanism(11β-HSD2-enzyme=placental-filter-80%-converts-to-cortisone+filter-weakens-T3+chronic-stress+First-Body-Feedback-Pipeline-v2.1+11β-HSD2=Hardware-Subsidy-biochemical-v2.1+4-fetal-effects:HPA-calibration-most-important+hippocampus+amygdala+PFC-synapses-all-🟡+Structural-Valence-from-prenatal-cortisol-v2.1+Direction>Level:novelty≠threat+cortisol-NECESSARY-for-fetal-development+Practical:reduce-chronic+increase-recovery+shift-threat→novelty); §4-Nutrition(key-nutrients-table:folic-acid/iron/DHA/iodine/choline/protein/VitD/zinc+timing+function+confidence+traditional-practices-filtering:keep-fish-veg-eggs-seafood+taboos-without-basis+morning-sickness:fetus-small+reserves+T1+eat-what-you-can); §5-Substances(Alcohol=FASD-no-safe-amount-🟢+Tobacco=CO-cuts-O2+nicotine-receptor-dev+secondhand-smoke+Toxins:lead-mercury-strongest-evidence+small-fish-OK-large-AVOID+pesticides+BPA-moderate+Medications=doctor-territory-don't-stop-on-own+Caffeine<200mg-likely-OK); §6-Physical+Mental(Sleep=repair-mechanism-PRIORITY#1-T3-filter-weakest+per-trimester-tips+Exercise:ACOG-150min-week-moderate+what-to-avoid+Weight-gain+Infections:rubella-toxoplasmosis-CMV+Dental-health+Stress-management-tools-ranked-PFC-cost:breathing<nature<music<social<meditation+PFC-Budget-concept-v2.1+social-support=Hardware-Subsidy-for-mother-oxytocin-v2.1+Partner=secondary-Coordination-Node-v2.1+Prenatal-depression=medical-treatment-CBT-or-SSRI-per-doctor); §7-Epigenetics(mechanism:DNA-methylation+histone-modification+prenatal-effects:folic-acid+Dutch-Hunger-Winter-extreme-famine-IGF2+stress→NR3C1-🟡+Cross-generational:Överkalix-study-🔴+Pre-conception-paternal-🔴+father-health-matters-too); §8-Control-table(Mother-controls:nutrition+avoid-substances+medical-care+sleep+exercise+seek-help+Partially-controls:stress-level+environment+social-support+economic+Cannot-control:genetics+random+some-complications+previous-generation+circumstances+Frame:"Optimize-what-you-CAN-accept-what-you-CANNOT"+Good-enough-mother-Winnicott=applies-from-pregnancy); §9-Per-trimester-guide(Pre-conception+T1:folic-acid-HIGHEST-VALUE+avoid-alcohol-tobacco+first-visit+T2:nutrition-build-up+exercise-best-window+stress-management-important+bond-talk-sing-w20+T3:sleep-PRIORITY#1+maintain-nutrition+cortisol-management-MOST-IMPORTANT+HPA-calibrating+Quick-summary-table); §10-Honest-assessment(what-file-CAN-do:framework+V7.8-lens+distinguish-🟢🟡🔴+what-CANNOT:replace-doctor+no-individual-protocol+cannot-prove-causation+confidence-per-section:folic-acid-🟢+cortisol-effects-🟡+cross-generational-🔴+6-risks:guilt+overinterpretation+replacing-doctor+cultural-bias+reverse-perfectionism+over-interpreting-V7.8); §11-12-open-questions(epigenetic-reversibility+paternal-contribution+microbiome+talking-singing+preterm+C-section+twins+pollution+baseline-calibration-precision+Hardware-Subsidy-variation+first-entity-representation-timing+first-coordination-node-quality); §12-full-cross-refs; 2026-06-10)
- [x] I33 Education-Mechanism.md ✅ (Research\Human-Learning\Education-Mechanism\; §0–§6+Changelog; LAYER-3-in-5-tier-architecture=INVARIANT-PRINCIPLES-of-education(distinct-from-LAYER-2-Child-Dev+LAYER-4-per-era-applications); §0-Position(triple-set:Education-Mechanism-HOW+Domain-Knowledge-Map-WHAT+Connection-Education-WHO+engine-model:Framework=ENGINE+AI=RUNTIME+Teacher=CALIBRATOR+Student=VERIFIER+scope:infinite-methods-brain-based-principles+NOT-prescribe); §1-Context-Shift(same-Compile-Architecture-1E+3M+same-perception-action-cycle+3-changes:Scale-1-family→1-teacher-30students+Structure-curiosity-driven→curriculum-guided+Purpose-survival→individual+society+humanity+Structural-Tension-individual-wants-hardware-fit↔society-needs-era-fit-CANNOT-resolve-only-BALANCE+Education=Hardware-Subsidy-system:family-individual-subsidy+school-societal-subsidy+Education=Guided-Chunk-Config-Optimization+Education=Gap-Landscape-Shaping+Education≠School-format-vs-process); §2-10-Arc-Design-Principles(P1-Direction>Level:structural-valence-tags+Multi-Stream-4-streams-Content/Value/Entity/Behavior+skilled-but-hates-it=Content✓-Value✗+target-BOTH-streams+P2-Cost-Formula:5-factors-chunk-gap×hardware-mismatch×direction×subsidy-inverse×PFC-budget-inverse+Hardware-Subsidy-hidden-dimension+AI-tutor=NO-subsidy+PFC-budget-finite-shared+P3-Prerequisite-Check:missing-prerequisite=NOT-dumb+Precondition-2+3-different-causes-of-hates-math+P4-Mini-Arcs+Valley:opioid-micro-reward+PFC-budget×timing+Valley=Evaluative-Dissonance-workable-vs-Direct-State-not-workable+Resonance-Decline:Compiled-Suppress+Reward-Habituated+normalize-dissonance-meta-skill+P5-Imagine-Final-Before-Content:v3.0-constructive-simulation+3-Layer-hierarchy-Body-Need→IF→Plan+Lifecycle-5-phases+Quality-4-angles+Critical-Asymmetry:PFC-path-SLOW+Entity-Valence-path-FAST+show-dont-tell-mechanism-basis+P6-Feedback-Loop:distinguish-dissonance-type+iterative-calibration-doctor-analogy+P7-Sleep-Maintenance:6-mechanisms-~1.5-exposure-~4.5-optimization+SWS+REM+PFC-degrades-FIRST+waking-rest-≈30%-DMN+spacing-leverages-sleep-mechanisms+P8-Assess-Depth:4-stages-Recognize→Explain→Apply→Create/Transfer+Bloom-connection+P9-Trust-Before-Content-v2.2:Trust=compiled-prediction-RELIABILITY+3-sub-dimensions-Authority/Competence/Intention+Trust≠Valence-like≠trust+Trust=Amplifier-for-VALUE-stream+Default→Calibrated×education-stages-table+Virtuous/Vicious-loop+trust-builds-slow-collapses-fast-1-betrayal+repair-months+P10-Self-Observation-Metacognitive-Foundation-v2.2:Level×strategy-table+Teacher-as-External-Scaffold-per-Level+PFC-budget-competition+Keystone-cascade-5+-systems+Teen-Paradox-CAN-observe-CAN'T-regulate+SYNTHESIS-3-Compile-Types×Arc-phases:Trust-bootstrap→Experience-depth→Expertise-mastery+current-education=Phase1-only-structural-gap); §3-Bridge+Motivation(Bridge=External-Inject-source④+4-types:carrot+identity-inject+social-expectation+threat+Hardware-Subsidy≠Bridge+AI-tutor=NO-subsidy+smallest-possible-bridge+Critical-Asymmetry×Bridge:Entity-Valence-path>>PFC-path+"love-teacher→learn-lesson"+Curiosity=TARGET-not-bridge+3-ORIGIN-taxonomy:Type1-Domain-KEEP+Type2-Peer-KEEP+monitor+Type3-Imposed-REDUCE+same-cortisol-different-origin=different-outcome+4-fill-sources-transition-trajectory:0-6-②④→6-12-②③④→12-18-①②③→18+-①②③+quarter-life-crisis=source④-withdrawn-abruptly+Entity-Access-gradient:AI-Level0+new-teacher-Level0c-1+good-teacher-Level2-3+parent-Level4++Coordination-Node:Prestige-approach-vs-Dominance-avoidance+Anchor=Legacy:forget-knowledge-remember-feeling+education-installs-anchor-not-just-chunks); §4-AI-Model-🔴(3-layer:AI-Arc-Generator+Teacher/Parent-Calibrator+Student-Verifier+Entity-Access-per-layer+Simulation-Engine-lens+framework=OS-for-AI-tutor); §5-Honest-Assessment(🟢🟡🔴-per-section+6-risks); §6-Full-cross-refs; 2026-06-10)
- [x] I34 Domain-Knowledge-Map.md ✅ (Research\Human-Learning\Education-Mechanism\; §0–§6+Changelog; LAYER-3-in-5-tier=WHAT-knowledge-groups(triple-set-FILE-2); §0-Position(triple-set-HOW+WHAT+WHO+3-tier-taxonomy:Foundation/Era-specific/Per-hardware+scope:domain-MAP-not-curriculum); §1-6-Foundation-Domains(all-cross-era-durable:①Literacy-prerequisite-for-all-other-domains+sensitive-period-0-6+②Numeracy-logical-thinking-substrate+concrete-before-abstract+③Somatic-body=processing-channel+interoception-chain:somatic→interoception→Self-Observation→Self-Pattern-Modeling-foundation+④Social/Emotional-survival-all-eras+Entity-Compiled-formation+4-Layer-Sustainability+⑤Creative/Expressive-novel-combinations-human-differentiator+Imagine-Final-emerge-channel+⑥Meta-learning=learning-how-to-learn+training-shared-Simulation-Engine+Trust-Calibration-as-meta-skill:Default→Calibrated-4-phases+Self-Observation-formal-mechanism:Level2-3-self-awareness+domain-feedback=only-differentiator+meta-learning-emerges-in-parallel-not-taught-separately); §2-6-Era-Specific-Domains(all-2025+-time-bound:①AI-Literacy-teach-principles-not-tools+②Info-Curation-trust-calibration-formal-backing-source-evaluation=trust-calibration-per-domain+③Systems-Thinking-feedback-loops+④Basic-Science-Literacy-arguable-placement-boundary-fuzzy+⑤Cross-cultural-scale+frequency+⑥Digital-Wellbeing-new-domain-info-overload+Evaluative-dissonance+boredom-loop); §3-Per-Hardware(observe-not-plan+hardware-tendencies-surface-via-6-Foundation+Gap-Distribution-Profile-4-axes+Hardware-Subsidy:parent-MAX-teacher-MODERATE-AI-NONE+Imagine-Final-connection+NORMAL-for-late-bloomer+NORMAL-for-multi-domain); §4-Timing+Prerequisite(Tier1-first→Tier2-after-foundation-basic→Tier3-after-tendencies-surface+PFC-budget-constraint:high-PFC-domains-ages-12++Balance-trajectory-table:6-12-Foundation-dominant+12-18-transition+18+-specialization+AI-check-per-chunk-status-NOT-age); §5-Honest-Assessment(🟢🟡🔴-per-section+4-risks:false-completeness+era-bias+western-bias+placement-debates); §6-Full-cross-refs; 2026-06-10)
- [x] I35 Expansion-Saturation-Crisis.md ✅ (Research\Human-Learning\Education-Mechanism\; §0–§11; OBSERVATION-LEVEL=APPLIES-mechanisms-to-explain-global-phenomenon(NOT-new-mechanism); §0-Position(intersection-3-streams:Domain-Mapping+Education+Generational-Shift+scope-in/out+reader-flow+Collective-chain-break:education=Trust-Compile-install+"why-study?"=Types②③+Compile-Taxonomy:education=primarily-Trust-Compile-without-Experience-Compile=boring); §1-Data-Global(thesis:structural-shift-NOT-any-country-fault+country-comparison-table:US/China/India/Korea/Spain/Indonesia+over-supply-white-collar-shortage-skilled-workers+timeline-1970s-2025+Conflict-Dynamics:OVERLAP×SCARCITY×COMMITMENT); §2-Framework-Core-3-eras(Era1-1800s-1970s:expansion-golden-age-wide-territory-Imagine-Final-CLEAR+Era2-1970s-2000s:early-signal-saturation-IT-bought-time+Era3-2000s-now:saturated-AI-replacing+core-mismatch=producing-Expanders-economy-needs-Discoverers+compression-paradox:better-compression→higher-baseline→harder-to-differentiate+Trust-signal-degradation:credential-inflation=trust-signal-loss-installed-trust-persists-Trust-Depth+Gap-Distribution-Profile:millions-same-gap-profile=OVERLAP); §3-Given-Paradox(Domain-Mapping-Drive-§4:Given-bypasses-process=no-reward+3-paradoxes:Modern/Education/Career-SAME-mechanism+learning-is-boring=CORRECT-per-hardware+Hardware-Subsidy-pointing-wrong-direction+Boredom×Meaning×Cortisol+Dissonance-Signal-Architecture:quarter-life-crisis=Evaluative+Direct-State-compound); §4-Career-Guidance(old=destination-fit-worked-Era1-2+new=process-fit-Discovery-era+Sense→Verify→Scale-spectrum+Process-fit-replaces-Destination-fit:Career-Construction-Theory-Savickas+YouScience-aptitude+Germany-Ausbildung-dual-system-6.5%-vs-EU-14.6%=process+domain-feedback>process-alone+Finland-16.1%=process-only-missing-domain-feedback); §5-AI-Disruption(replaces-expansion-work:data-entry/basic-coding/translation/content-writing-60-70%-McKinsey-2024+enables-discovery:cross-domain-connection+somatic-articulation+rapid-prototype+expansion-obsolete-discovery-premium); §6-Conflict-Dynamics(OVERLAP×SCARCITY×COMMITMENT×intensifying+Entity-Access:Era3-need-Level3-4+Cortisol-bounded-vs-unbounded-competition+Coordination-Node:university-disconnected-from-discovery-economy+Collective-chain-break-formal:3-types-cost/link/compound); §7-4-Conditions-Model(4-conditions:bounded-stress+PFC-undemanding+clear-Imagine-Final+low-competition+previous-gen-4/4-met→loop-CLOSES→settled+current-gen-0-1/4-met→loop-OPEN→adrift+cant-handle-hardship=wrong-frame:bounded≠unbounded-DIFFERENT-structure-not-level); §8-Value-of-Understanding(Value1-reduce-self-blame-dissonance:structural-attribution→cortisol-novelty-direction+Trust-lag-explains-self-blame-persistence+Value2-new-Imagine-Final:process-vs-destination+Value3-right-questions:which-process-fits-body); §9-5-Predictions+window-before-crisis(expansion-education-loses-value+AI-accelerates-entry-level-displacement+discovery-premium+career-guidance-reframe+apprenticeship-renaissance+5-year-2025-2030+10-year-2030-2035-forecasts); §10-🟢-data-established/🟡-framework-synthesis/🔴-hypothesis+4-risks:structural-determinism+confirmation-bias+retrospective+prescription-hidden-in-description); §11-full-cross-refs; 2026-06-10)
- [x] I36 Compile-Type-Learning.md ✅ (Research\Human-Learning\Education-Mechanism\; §0–§8+Changelog; OBSERVATION-LEVEL-deep-dive-into-1-mechanism=compile-type-influence-on-chunk-quality; §0-Core-Problem(Transfer-Failure:Experience-Compile-chunks-link-domain-Trust-Compile-chunks-link-context+NOT-saying-Trust-bad=most-powerful-collective-knowledge-mechanism+problem=Trust-Compile-ALONE); §0.1-Evolutionary-context(2M-yrs-100%-Experience→100K-language→5K-writing→500-print→200-school-dominant→50-TV→15-smartphone→5-TikTok:mismatch-increasing-exponential+NOT-"old-days-better"=Experience-Compile-eliminated-too-fast); §1-3-Compile-Types-in-learning(§1.1-Experience=Engine-pure-multi-modal-deep-transfer-good-slow-narrow+§1.2-Expertise=PFC-dominant-years-meta-chunks+Self-Observation-Mức3+-prerequisite-for-body-feedback-calibration-domain-feedback=referee-SO=ability-to-read+§1.3-Trust=Entity-Valence-dominant-AMPLIFIER-NOT-Gate-amplifies-VALUE-not-CONTENT+Trust.md-formal-backing:Trust=compiled-prediction-reliability≠Valence+3-sub-dimensions×learning:Authority-structural/Competence-calibratable/Intention-CRITICAL-VALUE-stream+4-formation-sources:③④-fast-low-accuracy+Compiled-Quality:Genuine/Schema/Threat-lock+pi-example:Archimedes-all-4-streams-✓/Rote-Content-only/Curious-all-✓-via-transition); §2-Research-2-extremes(transfer-failure:Whitehead-1929-inert-knowledge+Barnett&Ceci-2002+Marton&Säljo-1976-surface/deep+play-deprivation:Gray-2011-play-decline→anxiety/depression+Brown-2009+Finland-balanced-vs-East-Asia-dominant-Trust=SAME-PISA-DIFFERENT-wellbeing+Montessori:Lillard-2006-2012-hands-on>lecture+Chinese-Learner-Paradox:Watkins&Biggs-1996=verified-repetition-not-mechanical); §3-Trust→Experience-Transition(Trust-THEN-Verify:3-steps-install→domain-encounter→chunk-upgrade+when-Trust-sufficient:abstract-domain/low-risk/foundation-tool+when-NOT:physical-skill/uncertainty/creative/personal-values+LOCKED=dangerous:12-years-school-only→graduate-know-without-do); §4-Per-domain(§4.1-Math:self-verifying-internal-consistency-Trust-can-transition-via-repetition-BUT-algebraic≠geometric-understanding-Value-stream-CAN'T+§4.2-Language:L1=Experience/L2-school=Trust→immersion=Experience+§4.3-Programming:immediate-domain-feedback-natural-Trust→Experience-transition+§4.4-Sports=Experience-mandatory-Trust-only-guide+§4.5-Social=Experience-dominant-~70%+Entity-Compiled-40-200h+§4.6-Screen=weakest:passive-no-trust-amplifier-no-contingency-3/4-streams-near-zero+young-children-vs-adults-TikTok:suspended-chunks-vs-existing-chunk-activation+DOUBLE-DAMAGE:compile-no-anchor+hijack-VTA+VTA-habituation:screen-pace→real-domain-boring+learning-letters:person>screen-3-parameters-contingency/multi-modal/saliency); §5-Mechanical-vs-Body-Check-Repetition(KEY-INSIGHT:Mechanical=Trust-strengthen-same-type+Body-check=Trust→Experience-transition-chunk-upgrade+Dissonance-Signal-Architecture:Evaluative-workable/Direct-State-not+Body-Feedback-Label-3-tier+Body-check=Self-Observation-Level-3+-application:Level-0-2-mechanical-default/Level-3+-verified+PFC-Budget-competition-body-check-consumer-→short-sessions+4-stream-update-vs-2-stream-strengthen+Chinese-Learner=verified-repetition+self-diagnostic:1-question-Feynman-technique=body-check-via-teaching); §6-Education-Design(8-principles:①Trust=bootstrap/②per-domain-mix/③play=infrastructure/④repetition≠repetition/⑤body-feedback-beyond-grades/⑥Hardware-Subsidy=transition-subsidy-Teacher-MODERATE-AI-NONE/⑦PFC-Budget-constraint/⑧Sleep×Compile-Type:Experience→Replay+Gist/Trust→Consolidation/Expertise→Creative-Linking+optimal-4-phase-flow:Trust-install→Experience-verify→Verified-Repetition→Expertise); §7-🟢10-established/🟡16-synthesis/🔴4-hypothesis+4-risks; §8-full-cross-refs; 2026-06-10)
- [x] I37 Connection-Education.md ✅ (Research\Human-Learning\Education-Mechanism\; §0–§11; MAIN-FILE="WHO"=education-triple-set(HOW+WHAT+WHO)+absorbs-Empathy-Education-v2.0+expands-5-pillars; §0-Position(triple-set+layer-1-2-3-architecture+compared-to-Empathy-Education-v2.0:adds-bond-formation+4-bond-types+entity-access+4-layer-sustainability+coordination-node+phantom); §1-Why-Important(pragmatic>moral:positive-sum-logic+Compilable-Architecture=social=REQUIREMENT:4-reasons-survival/compilation/reused-circuits/social-baseline+auto-calibration-breaking:3-waves-stacking+moral-vs-pragmatic-determines-HOW-we-teach); §2-Mechanism-Summary(3-Generative-Primitives:❶Hardware-innate-3-condition-MET>UNMET>VIOLATED+❷Self-Pattern-Modeling=skill-NOT-hardware-module+❸Per-Agent-Valence-positive→empathy-negative→schadenfreude+Hardware-Subsidy-spectrum:MAX-mother/MODERATE-kin/TEMPORARY-romantic-18-36mo/NONE-friends+Bond-formation-40→200h-Hall-2018+non-linear-~40-60h-schema-forms+resonance-4-conditions-simultaneously+§2.5-Self-Observation=KEYSTONE-ALL-5-pillars:cascade-fail-table+Level×social-skill-ceiling-table+External-Scaffold+Compiled-Quality-warning); §3-Empathy-Education(Self-Pattern-Modeling=function-NOT-mirror-module→TEACHABLE+self-awareness=upstream-prerequisite-Bird&Cook-2013+connection-drive-INNATE→don't-damage-it+4-damage-patterns:abandonment/violence/emotion-rejection/shame+Trust-damage-compounds+1-anchor-person=enough-Werner-1989+4-fill-sources-applied); §4-Building-Connection(Entity-Compiled:active>passive≈zero-text+sleep=compiler+non-linear-curve+diversity-expands-range+4-bond-types:parent→child-gap-direction=parent/child→parent-opioid-age-invariant/romantic-limerence-mask/friendship-purest-test+8-pathways-as-education-targets+gap-clone-impossible+anti-compiled-suppress=meta-principle); §5-Choosing-Calibrating(Entity-Access-gradient×age-0-3-Level0/3-6-Level0-1/6-12-Level1-2/12-18-Level2-3/adult-0-5+Tool-vs-Agent-mode-dynamic-PFC-resource+gap-source-A:B-healthy-C:D-excess+PFC-budget+Dunbar=boundary-is-architecture-~5-intimate-~15-sympathy-~50-acquaintance-~150-ceiling+wrong-choice=compiled-suppress-cost+exit-skill+§5.6-Trust-Calibration:Trust=compiled-prediction-reliability≠Valence+3-sub-dimensions:Authority/Competence/Intention+Default→Calibrated-4-phases×age+Trust-generalization-WARNING:cross-domain-spill+Position-trust-vs-Person-trust); §6-Sustaining(4-Layer:Foundation-3-conditions/Modality-3-channels+4-types-silence/Amplification-ACR+PPR+Secure-Base/Trajectory-decline-normal+Resonance-Decline:Compiled-Suppress★LEVERAGE+Reward-Habituated+Novelty-fuel+Hardware-Subsidy×maintenance-effort+Repair:rupture+repair>no-rupture+ACR+PPR+Trust-repair≠connection-repair-MONTHS); §7-Groups(Status≠Talent≠Contribution-3-independent+Prestige-genuine-resonance-opioid-vs-Dominance-forced-relief-tag+parent=first-coordination-node+Dunbar-layers+inclusion/exclusion-8-pathways-reverse); §8-Per-age(0-3-foundation-connection=safe+3-6-recognition-others-feel+6-12-building-cooperation=good-for-me+12-18-meta+calibrate+Teen-Paradox-dlPFC-mature-vmPFC-incomplete+adult-still-buildable); §9-AI-Era(AI-no-body→real-connection-absent+connection=irreplaceable-human-advantage+Phantom:imaginary-friends-normal-parasocial-mixed-AI-companion-highest-risk); §10-🟢-established/🟡-synthesis/🔴-hypothesis+confidence-per-section; §11-full-cross-refs+8-open-questions-CE-1-to-CE-8; 2026-06-10)
- [x] I38 Education-Arms-Race.md ✅ (Research\Human-Learning\Education-Mechanism\Observation\; §1–§10; OBSERVATION=game-theory+data+framework-lens-on-education-arms-race; §1-Mechanism(positional-good-Hirsch-1976+prisoner-dilemma-Nash-equilibrium+credential-inflation-Red-Queen+Gap-Distribution-Profile-homogenization+signaling-theory-Spence-1973+spending-diminishing-returns); §2-Spectrum-table-9-countries(Finland-★-minimal/Germany/France/USA/growing-case/Japan/Singapore/China/India/Korea-★★★★★-extreme+3-case-details:Finland-structural-prevention-never-started+Korea-Nash-locked-suneung+China-ban-failed-2021-underground); §3-Consequences(birth-rate:-28%-fertility-AER-2024+mental-health:Korea-4148-Japan-529-India-13000-suicides+sleep-deprivation-4.9-5.5h+Dissonance-Signal-Arch:Evaluative+Direct-State-compound+inequality:7×-gap-USA+creativity-diminishing-returns); §4-Why-Hard-to-Stop(all-bans-failed-table+5-reasons:unilateral-disarmament-suicide+supply-ban≠demand-fix+race-adapts+prevention>>cure+Trust-Lock-in:installed-trust-depth-multi-source-cannot-calibrate-Phase-2-stuck-domain-changed); §5-Framework-Lens(zero-sum-Imagine-Final+body-cannot-stop-substrate-Evaluative+schema-self-reinforce+cost-multiplier+§5.4-2-nested-levels:society→parents→children-Type3-Imposed-Hardware-Subsidy-INVERTED+§5.5-Hardware-First-Harm-societal-scale:strong-anchor+body-smooth-GDP+skip-body-check-TFR-signals-rationalized+invisible-chronic-damage+Y5-workaholism-parallel+§5.6-societal-anchor-④-dominated-80-90%+§5.7-Imagine-Final-4-corners:domain-partial+hardware-LOW+Mismatch-dominant+§5.8-Resonance-Decline-credential-decay+4-Layer-unsustainability); §6-Structural-Solutions(5-solutions:①eliminate-single-exam②vocational-track-with-real-value③affordable-diverse-uni④school-remediation⑤wage-compression+§6.6-6-barriers:short-term-bias/cultural-anchor-rigidity/measurement-systems/rich-environment-cost/hardware-calibration/economic-political-incentives+§6.7-3-ORIGIN-applied:KEEP-Type1+2/REDUCE-Type3-rankings-shame-reform+§6.8-shift-source④:media-diversification+cultural-celebration+alternatives-in-school); §7-Prevention-Window-Case(★★★↑-accelerating-not-yet-extreme+structural-recommendations:no-single-exam+vocational+public-uni-affordable); §8-🟢-established/🟡-synthesis/🔴-hypothesis; §9-7-open-questions-EA-1-to-EA-7; §10-full-cross-refs+trust-integration-v1.4; 2026-06-10)
- [x] I39 Money-Education.md ✅ (Research\Human-Learning\Education-Mechanism\Observation\; §0–§11; OBSERVATION=money-education-through-framework-lens-WHY-matters-WHY-fails-HOW-to-compile-correctly; §0-Position(Observation-file-applies-Money-Analysis-to-education-context+per-age-guide-NOT-new-mechanism+answers-Money-Analysis-Q8:critical-period-for-money-schema-compile); §1-Why-Important(Whitebread-2013-habits-set-age-7+Background-Pattern-2D-model-LOW-depth-HIGH-density=invisible-pervasive+4-exposure-modes-compiling-continuously-without-intention+parents-already-teaching-even-without-intending+approach/avoidance-tags-determine-lifelong-outcomes+Compiled-Quality-Dimension:Genuine/Schema/Threat-compiled); §2-Why-Current-Approaches-Fail(4-failure-modes:①knowledge-behavior-gap-PFC≠body-Mandell-2008+Trust-mechanism-installed-persists-never-verified+②overjustification-Deci-1971-external-kills-internal+③threat-path-Type3-Imposed=avoidance-tag-for-life+3-ORIGIN-applied:Domain-healthy/Peer-complex/Imposed-harmful+Dissonance-Signal-Architecture-Evaluative-vs-Direct-State+④premature-compilation-too-much-too-soon-threshold-shift); §3-Framework-Principles(6:①Experience>Lecture+Self-Observation-spending-body-signal-Level3+②Approach-direction-ALWAYS-reframe-table+③Goldilocks-per-age+④Natural>Imposed-consequences+⑤Don't-monetize-internal-drive-overjustification-allowance-distinction+⑥Teach-proxy-nature-tool≠goal-PFC-Budget-constraint); §4-Per-age(0-3-Observation-parents-copying+3-6-First-Experience-mini-transactions+6-12-Management-allowance-budget+12-18-Real-World-earning-complexity-Self-Observation-Level4+prerequisite-chain-Goldilocks-per-age); §5-5-healthy-schemas(①money=tool②limited→I-choose③effort→reward=normal④money-can't-buy-everything⑤giving=approach-not-loss)+5-toxic-schemas(①solution-to-everything+Trust-Generalization-KOL-exploit-per-entity≠per-domain+②dangerous/scary③free④human-worth⑤giving=losing)+Trust-Calibration=THE-financial-meta-skill); §6-Common-Mistakes(①guilt-trip-parents-worked-hard=Type5-Identity-Obligation+Hardware-Subsidy-inversion+②scarcity-messaging-shame+③monetizing-grades=overjustification+threat-compound+④social-comparison-money=human-worth-compile); §7-Valence-Structural-Bonds(Valence-Structural-Depth×money=INVERSE-relationship+table+exchange-vs-Valence-Structural-distinction+Entity-Access-modulator:money-opens-doors-relationship-quality=inside+wealthy-family-specific-risk:money-replacing-presence); §8-Cultural(East-Asian-Background-Pattern:money=family-tool-Takahashi-2016+lucky-money-approach-vs-avoidance+Western:money=independence+OECD-PISA-2022+direction-principle=universal-regardless-of-culture); §9-AI-Era(cortisol-path-absorbed+6-principles-still-valid+Trust-Generalization-AI-new-risk:smooth-content-installed-trust-persists+Trust-Calibration=core-skill-AI-era); §10-🟢-established/🟡-synthesis/🔴-hypothesis+7-open-questions; §11-full-cross-refs+Trust+Self-Observation-integrations-v1.2; 2026-06-10)

**I6. Remaining Research (16 files)**
- [x] I40 Money-Analysis.md ✅ (Research\; §0–§11; RESEARCH-SYNTHESIS=money-through-framework-v7.8-lens-~15-files-unified; §0-Position(this-file-vs-~15-files-scattered+ADDS:cross-parameter+individual↔collective↔AI+gap-shift-insight); §1-3-Layer-Definition(①Proxy-Token:money-itself=zero-body-base-value+prediction="$100→food→opioid"+Knutson-2001-anticipation-not-possession+Kahneman-Deaton-2010+②Obligation-Technology:4-functions=standardize-cross-domain+convert-implicit→explicit+scale-O(n²)→O(1)+optimize-PFC-prediction+③Shared-Chunk-Prediction:trust-token-collective-holds+collapse=hyperinflation+bank-run-Diamond-Dybvig-1983+meta-insight:money≈language-both=proxy-extending-not-replacing); §2-Evolutionary-Foundation(chain:fight→status→exchange→obligation-tracking→money→AI?+each-step=reduce-cooperation-cost+body-rewards-prediction-not-paper+Schultz-1997-VTA); §3-5-Functions(①fill-survival-gap:strongest-most-direct+②reduce-prediction-cost:O(n²)→O(1)+PFC-freed+③expand-Resource-Access-Map:diminishing-returns-$0→$30K→$100K→$1M++④bootstrap-exploration:catalyst-cortisol-floor→PFC-open→dare-try→internal-drive-forms+fuse-metaphor+⑤scale-cooperation:O(1)-per-transaction-billions); §4-Why-Everyone-Chases(4.1-"have-to"=biological-imperative-not-social+Herzberg-hygiene+4.2-"want-to"-6-paths:①schema-not-updated=Background-Pattern-unsynced/②threshold-adaptation-hedonic-treadmill/③money=proxy-for-tier2-3/④low-prolactin-cant-brake/⑤identity-lock=dừng=meaning-crisis/⑥cortisol-treadmill-chasing-state-not-money+4.3-schema[money=best]=HIGH-trust:source②+④-simultaneously+but-INCOMPLETE-functional-incomplete+4.4-Gap-Shift-core-insight:survival-gap-fills→habituated→gap-shifts-tier2-3-BUT-label-stays=billionaire-money=scorecard-not-endpoint+schema-too-strong-to-self-update+4.5-society-organizes-around-money-for-cooperation-advantage); §5-When-Harmful-6-Mechanisms(①threshold-adaptation-hedonic-treadmill+②overjustification-kills-internal-drive+③bridge-dependency-prevents-internal-forming+④premature-compilation-lottery/inheritance/salary-exceeds-competence+⑤Valence-Structural-bond-destruction=implicit-bond-exists-where-money-forbidden+⑥habituation-blindness-essential-undervalued+6-mechanisms-can-overlap); §6-When-Useless-7-Cases(Gap-mismatch:wrong-type→wasted+7-cases:①loss-loved-one②wealthy-empty-meaning-gap③imposter④want-to-understand-coherence⑤lonely-Valence-Structural⑥health-damage⑦lacking-autonomy-no-efference-copy+pattern:richer→gap-shifts-higher→money-matches-less+Valence-Structural-depth×money=INVERSE-scale+deepest-relationships=where-money-forbidden); §7-Cross-Parameters(§7.1-Status:money=1-dimension-not-whole+§7.2-Obligation:6-types-TYPE1-2-effective-TYPE3-5-useless+§7.3-Meaning:2-independent-tiers+§7.4-Connection:money-buys-Valence-Momentary-not-Valence-Structural+wealthy-lonely+§7.5-Autonomy:2-directional-money-can-increase-OR-decrease+§7.6-Protect:loss-aversion-asymmetry+§7.7-Gratitude:counter-habituation-3-mechanisms+§7.8-Drive/Boredom:fuel-not-compass+§7.9-Threat/Cortisol:5-roles); §8-Collective-Scale(3-Tier-Model:individual-compiles-SHORT-collective-holds-LONG+trust=bridge+market=collective-calibration=anti-over-reward-natural+2-path-economy:cortisol-stability+dopamine-innovation+knowledge-flow-lubricant-intergenerational+conflict:2-directional); §9-AI-Era(AI=new-intermediary-reduces-prediction-cost+convergence=new-premium+speculation:post-money-economy-via-AI-matching); §10-🟢/🟡/🔴-confidence+5-testable-predictions+8-open-questions-MA-1-to-MA-8; §11-full-cross-refs+Money-Education.md-companion; 2026-06-10)
- [x] I41 Climate-Cognition.md ✅ (Research\; §1–§12; HYPOTHESIS+RESEARCH-SUPPORT=temperature-modulates-PFC-via-body-state-pathway; §1-Observation(500yr-pattern-cold=more-innovation+recency-bias-exposed:Egypt/Mesopotamia/India/Islamic-Golden-Age-all-HOT+scale:MACRO~5-10%/MICRO~25-35%); §2-Research-Data(inverted-U-curve-Seppänen-2006-peak~22°C+heat:PFC-connectivity-DOWN+limbic-UP-Sundaram-2013-fMRI+Park-2020-10M-students:+1°F→1%-annual-learning-loss+asymmetry:heat-impairs-ATTENTION/MATH/PERCEPTION-cold-impairs-REASONING/LEARNING/MEMORY+brief-cold-paradox:NE+530%-dopamine+250%-Sramek-2000+Gaoua-2012-KEY:thermal-displeasure-ITSELF=cognitive-load); §3-3-Mechanisms-overview(PRESSURE+BODY-STATE+REWARD-BALANCE+cumulative); §4-Pressure(4-seasons=forced-Plan→Execute→Test→Adjust-cycle+winter=forced-PFC-training); §5-Body-State(PFC-generates-heat→hot-body-resists+stability>absolute-value:thermal-oscillation-10-15°C-indoor/outdoor+CO₂-Satish-2012+Double-Calibration-Problem-CONFIRMED-Gaoua-2012+AC-execute-OK/imagine-NOT-sufficient+3-hardware-groups); §6-Reward-Balance(cold=Evaluative-PRIMARY-reward+hot=Direct-State-abundant+measurement-bias:only-Evaluative-counted-patents/papers); §7-Confounds(colonialism-BIGGEST+Jared-Diamond-E-W-vs-N-S+writing-systems); §8-Counter-examples(extreme-cold≠creative+Islamic-Golden-Age:architecture-micro-climate+institutions+trade+India:meditation=indoor-state+Singapore:AC+institutions+Vikings-vs-modern-Scandinavia→institutions>climate); §9-Applications(AC-game-changer-not-complete+workspace-20-22°C-CO₂<1000ppm+individual-optimization+climate-change+AI-era); §10-6-open-questions; §11-honest-assessment-section-by-section+overall-UPGRADE:hypothesis→hypothesis-with-substantial-research-support+5.4-Double-Calibration-🔴→🟢; §12-connections+12-research-citations; 2026-06-10)
- [x] I42 Fidgeting-Analysis.md ✅ (Research\; §1–§15; ANALYSIS=fidgeting-as-change-readiness-output-when-blocked; §1-Definition(NEAT-300-800kcal-Levine-2005+§1.1-ROOT=change-readiness-bypass:proprioceptive-feedback-deceives-brainstem+NOT-bad-habit); §2-3-Layers(brainstem-proprioceptive-calming/motor-cortex-VTA-arousal-management/micro-novelty-reward-hybrid+Evaluative-vs-Direct-State-mapping); §3-VTA-Discriminator(leg-bounce=VTA-ignore-no-dopamine/doodle=prediction-delta-loop-continuous-micro-reward+pen-click-escalation=unconscious-novelty-seeking); §4-Spectrum(pure-fidget→micro-novelty→full-novelty+drift-rightward+stops-when:arousal-OK/real-task/full-novelty); §5-vs-OCD(complete-comparison-table+3-circuit-model-sync:all-3-normal-vs-OCD-1+2-broken); §6-Beach-Test(heuristic:stops-when-relaxed=arousal-regulation/still-occurs=other); §7-Modality-Specific(somatic→physical/verbal→mental-loop+rumination-risk/visual→doodle+🔴prediction); §8-Exercise(scheduled-motor-discharge+exercise-need-by-modality+programmer-example); §9-Sitting-Still-Not-Free(active-suppress=PFC-cost+Hartanto/Andrade/Farley-support); §10-Broad-Spectrum-Table(fidgeting/doodling/stimming/habit/tic/OCD/stereotypy/BFRB+3-question-quick-distinction); §11-Trajectory(⭐6-steps:0-target→1-tension→2-fidget→3-micro-novelty→4-habit→5-BFRB→6-OCD+conditions-per-step+population-%+decision-tree+4-BFRB-predictions); §12-Evidence-Hub(🟢/🟡/🔴); §13-Honest-Assessment; §14-10-open-questions-FDG-1-to-FDG-10; §15-connections; 2026-06-10)
- [x] I43 Sensitivity-Classification.md ✅ (Research\; §1–§8; DRAFT=sensitivity-decomposed-into-2-independent-layers; §1-Problem("sensitive"=1-word-7-different-things:emotional/auditory/pattern/skin/social/olfactory/nerve+HSP-Aron-1996-bundles-mechanisms); §2-2-Layer-Framework(Sensor×Processing+BOTH-possible+must-identify-WHICH-layer); §3-Layer1-Sensor(6-channels:eyes/ears/skin/nose/tongue/viscera+3-quality-levels:GOOD/AVERAGE/POOR+KEY:sensitive-because-GOOD≠sensitive-because-BROKEN-look-same-from-outside); §4-Layer2-Processing(7-brain-regions:visual/auditory/somatosensory/limbic+insula/Self-Pattern-Modeling/VTA+PFC/mPFC+amygdala+INDEPENDENT-per-channel); §5-Why-Separate(3-examples:noise-sensitivity-3-people-3-causes-3-fixes+emotional-sensitivity+without-separation=wrong-advice); §6-v7.8-Lens(Layer1=Sensory-Driven-Direct-State+Layer2=Core-Hardware-Zone-B/C+compound:GOOD×DOMINANT=high-signal+POOR×DOMINANT=distorted-deeply+cortisol-AMPLIFIER-interaction); §7-Honest-Assessment(🟢-HSP-Aron/interoception-heartbeat/DRD4+🟡-2-layers-not-formally-tested+🔴-completeness-unknown); §8-Connections(Climate-Cognition-§5.6-application); 2026-06-10)
- [x] I44 Self-Created-Threat.md ✅ (Research\; §0–§8; SYNTHESIS+APPLICATION=self-created-threat-as-learnable-skill; §0-Position(foundation-Q:why-drive-strong-post-success+body-cant-distinguish-imagine-vs-real+framework=APPLY-not-new-mechanism); §1-Core-Mechanism(§1.1-neuroscience:same-pathway-Kosslyn-2001-Ganis-2004-fidelity-20-60%+§1.2-Trust-Compile-from-PFC:chain-must-reach-body-base-or-body-ignores+Imagine-Final-connection:push=simulate-losing-IF+Protect-loss-aversion-2x+6-CEO-cases-all-chain-to-specific-IF-not-generic+§1.3-"try-harder"-floating-Trust-Compile-vs-anchored-chain); §2-4-Types(①Competition:Status+Protect-Jensen-"30-days-bankruptcy"+Andy-Grove-paranoid/②Time-Waste:L0+Novelty-Steve-Jobs-mortality-tool-Elon-Musk-species/③Responsibility:Connection+Status-atlas-syndrome/④Legacy:Status+Novelty-Bezos-regret-min+table-anchor×duration×risk); §3-3-Stages(①Experience-real-threat:body-compile-threat=energy+CEO-childhoods+BUT-too-strong+weak-PFC=TRAUMA/②Observe-pattern:Yerkes-Dodson+NOT-yet-verbal/③Self-create-consciously:simulate-cues-body-responds+mandatory-sequence-can't-skip+4-conditions-ALL-needed); §4-ON-OFF(LAYER-creates=LAYER-can-dismiss+PFC-level:baat-tat-switch-REPAIR-happens/body-compiled:cant-reach-chronic-cortisol/⚠️-PFC-level-CAN-compile-into-body-level-if-no-repair-cycle=workaholic-burnout); §5-AI-Era(5-old-sources-decreasing+drive-void+quiet-quitting-NEET-symptoms+3-skills:body-listening/self-created-drive/collective-awareness+novelty-pull=other-path+transition-skill-education-fixes); §5.5-Full-Cycle(Social-Calibration-source-data+old-society=auto-calibrated+future=self-calibrate:6-components-Direction/Sustain/Push-Valley/Real-Check/Repair/Re-Fire+temporal-interplay:start-PULL/valley-PUSH+PULL/end-PULL/after-REPAIR); §6-Calibration(§6.1-inverted-U:drift/flow/burnout/crash+§6.2-peak-shifts-per-person-6-params+§6.3-cycle:ON→action→OFF→repair→evaluate+2-mistakes:never-off/never-back-on); §7-Honest-Assessment(🟢-Kosslyn/Yerkes-Dodson/Sapolsky+🟡-synthesis+🔴-AI-era-void/sequence+survivorship-bias-warning); §8-Cross-refs; 2026-06-10)
- [x] I45 Relativity-Explained.md ✅ (Research\; §0–§20; STANDALONE-REFERENCE=shortest-compile-pathway-for-relativity; §0-Purpose(GPS-real-world-use+reverse-teaching:Pythagoras-first-not-tensors+4-section-format:Intuition/Real-Math/Verification/What-This-Means); §1-Timeline(~500BC-Pythagoras→2022-EHT-Sgr-A*+Knowledge-Flow-pattern:decades→hours); §2-Level0-Foundation(3D-space+time+speed=all-prereqs); §3-Level1-Pythagoras(c²=a²+b²+3D-extension+invariance-key-insight); §4-Level2-c-constant(Michelson-Morley-1887-zero-result+c=299792458m/s+2-postulates); §5-Level3-Spacetime-Interval(Minkowski-s²=-(ct)²+x²+y²+z²+car-analogy:space-time-compete+invariance); §6-Level4-Lorentz-γ(light-clock-derivation-via-Pythagoras+γ=1/√(1-v²/c²)+table-from-walking-speed-to-100%c); §7-Level5-Time-Dilation(t'=γt₀+GPS:38μs/day+muon-γ=15.8-at-0.998c+Hafele-Keating-1971+twin-paradox-explained); §8-Level6-Length-Contraction(L'=L₀/γ+rod-example+muon-from-muon-frame-950m); §9-Level7-E=mc²(E=γmc²+c²=9×10¹⁶+Hiroshima-0.7g+PET-scan+extended:E²=(pc)²+(mc²)²+photon-E=pc); §10-Level8-Equivalence-Principle(elevator-thought-experiment+light-bends-Eddington-1919+gravitational-time-dilation-Pound-Rebka-1959); §11-Level9-Curved-Spacetime(no-attractive-force:mass-curves-spacetime+geodesic-great-circle-analogy+rubber-sheet-limits+Mercury-43-arcsec-Einstein-"heart-raced"); §12-Level10-Einstein-Field-Equations(Gμν+Λgμν=(8πG/c⁴)Tμν+cosmological-constant-history+Wheeler-quote+tensor-explained-scalar/vector/tensor+non-linear-feedback-loop); §13-Level11-Black-Holes(Schwarzschild-1916-WWI+rs=2GM/c²-table-6-objects+event-horizon-space-time-swap+time-dilation-formula+EHT-2019-M87*-2022-Sgr-A*); §14-Level12-Gravitational-Waves(LIGO-4km-tubes+h=ΔL/L≈10⁻²¹+1/1000-proton+GW150914:3M☉→3.6×10⁴⁹W-chirp-Nobel-2017); §15-Level13-Cosmology(Hubble-1929-v=H₀d+expansion-not-flying+Big-Bang-not-explosion+CMB-Penzias-Wilson-1965+Friedmann-equation-3-scenarios+dark-energy-Λ>0-1998-Nobel-2011+observable-universe-46.5Bly); §16-Level14-Physics-Breaks(singularity=math-breaks/Planck-scale-ℓP=10⁻³⁵m/GR+QM-incompatible+String-Theory+Loop-Quantum-Gravity+FRONTIER); §17-14/14-predictions-verified-table; §18-Framework-Connection(🟡:Knowledge-Flow-compile-pathway-shortens/body-base-anchor-shift:Pattern-Driven→Sensory-Driven/Domain-Mapping-Drive-survival-knowledge); §19-Honest-Assessment(✅Special+General-100%/🟡dark-energy-dark-matter-inflation/🔴quantum-gravity-singularity-Λ-problem); §20-5-primary-sources+5-experimental+5-framework-cross-refs; 2026-06-10)
- [x] I46 Melody-Technology-Overview.md ✅ (Research\Melody-Technology\; §0–§6; INDEX/ROADMAP=Melody-Technology-concept+7-function-framework+spectrum; §0-Concept("Melody-Technology"=any-system-serving-body-base+community-architecture+no-judgment-on-best/analyzes-MECHANISM+MTF=observation-clusters-not-modules+MIXED-body-base+PFC-technology:compound-Chain0+Chain2-3+chain-profile-per-implementation); §1-7-Functions-MTF-v2.0(MTF1-life-level-anchor/MTF2-structured-connection/MTF3-compiled-compliance/MTF4-dissonance-resolution/MTF5-contemplative-practice/MTF6-schema-template/MTF7-reward-schedule+v2.0-changes:merge-MTF1+MTF7-old+promote-MTF4b→MTF5); §2-Analyzed(Religion-7/7+compound/Idol-1-4/7/Education-3-4/7/Law-MTF3-only); §3-Spectrum(casual-fan→committed→hardcore→devotion→folk-belief→religion+SAME-3-Generative-Primitives-different-depth+anchor-type+scope); §4-Not-Analyzed-Predictions(Ideology~5-6/7/Self-help~2-3/7/Sports~3-4/7/Games~3-4/7/Social-movements~4-5/7/Family~4-5/7/Military~5-6/7/AI-meaning~2-3/7+all-🔴HYPOTHESIS); §5-Why-Analyze-All(①trade-offs-per-impl/②optimal=per-person-mix/③not-enough-data-yet/④ultimate-goal=guide+3-tier-priority); §6-cross-refs+25-dependency-files; 2026-06-10)
- [x] I47 Religion.md ✅ (Research\Melody-Technology\; §0–§15; RESEARCH-FILE-v3.1=religion-as-community-architecture-serving-body-base; §0-Position(RESEARCH-not-Core-Deep-Dive+Model-3-Level:collective-holds-7-functions/individual-compiles-short+Trust=only-bridge+6-principles:①no-truth-claim/②community-architecture/③per-person/④neutral-evidence/⑤MTF=observation-clusters/⑥body-base-vs-PFC-mixed:Chain0+Chain2-3-COMPOUND); §1-7-MTF-Functions(table:MTF1-life-anchor/MTF2-connection/MTF3-compliance/MTF4-dissonance/MTF5-contemplative/MTF6-schema/MTF7-reward+FAITH-type-anchor-most-durable+compound-per-function); §2.1-MTF1(FAITH-type-anchor+death-management=killer-feature+unfalsifiable=NEVER-voids+scope-gradient:GOAL→FAITH+coherence-effect+serotonin-stability-🔴+Li-2016-33%-mortality); §2.2-MTF2(3-Primitives-engaged+hardware-subsidy-MODERATE+Bond-Architecture-3/4-types+Entity-Compiled-thousands-hours+4-Layer-Sustainability+fixes-both-loneliness-types); §2.3-MTF3(Type5-Identity-Obligation+Compliance-Floor+vmPFC-controllability+action-path); §2.4-MTF4(Chunk-Gap-resolved+confession=Chunk-Shift-near-immediate+cycle-dependency+Compilation-Source-Match-layer②); §2.5-MTF5(Simulation-Engine-1E-3C+prayer=Self-Pattern-Modeling-on-virtual-agent+God=Entity-Access-VENTRAL-if-deep+🔴God-as-virtual-Entity-Compiled); §2.6-MTF6(pre-compiled-chunk-network-template+multi-source-social-proof+hardware-fit-trade-off); §2.7-MTF7(5-preconditions+3-anti-habituation:variation/comparison/ritual+5-reward-profiles-ALL-covered+only-tech-covering-all-5); §3-Compound-Dynamics(SUPERADDITIVE+MTF1×MTF3/MTF2×MTF7/MTF4×MTF5+strongest:death-management=MTF1×MTF4×MTF5+community-sustainability=MTF2×MTF3×MTF6×MTF7); §4-Compile-Mechanisms(5-mechanisms:childhood/repetition/emotional-peak/socialization/multi-channel+childhood=deepest-why-logic-fails+4-compile-pathways:hardware-fit/trust+experience/social-default/threat-avoidance); §5-Faith=Choosing-Stability(James-1896/Tillich-1957/Plantinga-2000+unfalsifiable=stability-choice+Imagine-Final-3D+faith≠dogma-nuance); §6-Per-Hardware(DRD4/COMT/cortisol-baseline-table+Big-Five×religiosity-Saroglou-2002+per-hardware-per-context); §7-Religion×Idol(same-3-Primitives-different-depth+table:media/parasocial-vs-community/real+MTF1-coverage=key-difference); §8-Domain-Speciation(hardware-diversity→interpretation-diverge+split-trade-off+Coordination-Node:Prestige→Dominance-risk+3-scale-hardware-subsidy); §9-Value+Limitations(Li-2016-33%/Hummer-1999+7yr/suicide-69-75%/Putnam-capital/Ano-coping-r.33/Koenig-80%-positive+4-limitations:hardware-mismatch/leader-dominance/faith→dogma/dependency+~70/30-ratio); §10-Loss-of-Faith(7-functions-collapse-simultaneously+Entity-Compiled-grief-A+B+C+opioid-withdrawal+4-amplifiers+4-stages:Doubt/Crisis/Collapse/Rebuild+devastation=indirect-evidence-of-real-value); §11-Secularization(5-reasons-declining+Meaning-Crisis-per-MTF+Marx-2/7-only+Berger-self-refutation+replacement-per-function-table+package-irreplaceable); §12-Future-AI(AI-CAN:MTF1/3/4/6+AI-CANNOT:MTF2/5/7/Entity-Compiled+menu-options-future+AI=gateway-not-replacement); §13-🟢×19/🟡×15/🔴×5; §14-7-open-questions; §15-cross-refs-30+-files; 2026-06-10)
- [x] I48 Idol-Phenomenon.md ✅ (Research\Melody-Technology\; §0–§12; RESEARCH-FILE-v2.6=idol-phenomenon-as-body-base-drives-compiling-chunks-about-idol; §0-Position(LEANS-Chain0-sensory-dominant-vs-religion-LEANS-Chain2-3-coherence-dominant+both-compound-different-ratio+explains:idol=fast-shallow/religion=slow-deep); §1-5-Drives(①Body-Reward:5-preconditions-music-reward-VTA-opioid+DIRECT-STATE+Evaluative-Gates-amplifies-fan-depth-gradient/②Connection:3-Primitives-❶hardware-❷Self-Pattern-Modeling-❸valence-parasocial/③Imagine-Final:GOAL-IDENTITY-anchor-vs-religion-FAITH-type/④Schema:chunk-network-pattern-melody-template-teen-fitting/⑤Belonging:fan-community-3-Primitives-GENUINE-connection-idol=bridge); §2-Formula(modality×frequency×reward×hardware×social×valence+table-6-idol-types-channels+scientist-fewer-fans=fewer-channels-not-lesser-value); §3-Parasocial(Self-Pattern-Modeling-Compiled-fires-REAL-biochemistry+BUT-1-way-no-calibration+drift=shock-when-reality-differs+❸-valence-dense-1-way+Hardware-Subsidy=NONE-habituates-fast+Entity-Compiled-SHALLOW-3-4/6-spokes+Entity-Access-Level-2-vs-0+"idol-knows-everything-idol-doesn't-know-who-you-are"+2-stream-Valence-Momentary+Structural+🔴Body-Base-Extension-rare+v2.6-Trust-1-way:schema-inheritance-Phase2-persist-cross-domain); §4-Benefits(①accessible-body-reward/②anchor-for-those-without/③connection-for-lonely:parasocial-buffer+fan-community-REAL/④low-cost-schema-testing/⑤emotional-regulation); §5-Harms(①parasocial-replaces-real:drift/Compiled-Suppress/fails-4-Layer/②anchor-replaced-must-be-like-idol:hardware-mismatch-chronic-chunk-miss/③dependency-grief-f(replaceability×attachment)-1-way-grief-no-closure/④trust-cross-domain-exploit:Trust-Phase2-persists-PFC-filter-OFF/⑤obligation-toxicity:Type2-Exchange+Type4-Role); §6-Industry-Exploit(Factor①repetition/③emotional-peaks/④multi-modal/⑤context+specific:behind-scenes/30s-fan-meeting/limited-merch=wanting-not-liking/fan-wars-tribal); §7-Self-Upgrade(channels/frequency+variation/reward-quality-genuine/hardware-match); §8-Scale(individual/cultural-idol/historical-idol+spectrum-table:casual→committed→hardcore→devotion→folk→religion+v2.6-trust-depth=driver-spectrum-position); §9-AI-Idol(all-formula-factors-maximized+Self-Pattern-Modeling-on-virtual=parallel-religion-§2.5+pseudo-bidirectional-artificial-calibration+Entity-Compiled-accelerated+4-dangers:stronger/replaces-real/dependency-no-breakpoint/addiction-by-design); §10-🟢×9/🟡×10/🔴×5; §11-6-open-questions; §12-cross-refs; 2026-06-10)
- [x] I49 drill-religion-evidence.md ✅ (Research\Melody-Technology\; EVIDENCE-DRILL=evidence-foundation-for-Religion.md-v3.0-rewrite; 3-Axes+Summary; Axis1-Q1.1-Q1.7=value-of-religion:Q1.1-Wellbeing/Health/Longevity(Li-2016-JAMA-N=74534-HR=0.67-33%-mortality/Hummer-1999-+7yr/McCullough-2000-OR=1.29/Chen-VanderWeele-2020-68%-deaths-of-despair/Yaden-2022-N=666K-r=.18)+Q1.2-Resilience(Ano-Vasconcelles-2005-49studies-positive-r=.33-negative-r=.22/suicide-meta-2022-N=8M-OR=0.25-0.31/grief+Frankl-meaning)+Q1.3-Community(Putnam-2000-single-most-important-repository/Lim-Putnam-2010-church-friends-super-charged/Brooks-2006-350%-giving+Q1.4-Meaning(Steger-Frazier-2005-meaning-mediates/VanderWeele-2017-all-6-flourishing-domains/TMT-Burke-2010-r=.35)+Q1.5-Anti-Habituation(Ramadan-review-2024:72.7%-depression/85.7%-stress/Baha'i-2022-3mo-lasting/PNAS-2025-gratitude-g=0.19/Rounding-2012-61%-vs-34.4%-delayed-gratification)+Q1.6-Contemplative(Goyal-2014-JAMA-anxiety-ES=0.38/Holzel-2011-8wk-gray-matter/Schjoedt-2009-prayer=mentalizing-networks-brain-treats-God-as-social-partner)+Q1.7-Prosocial(Kelly-Shariff-2024-N=811K-r=.13-behavioral-r=.06/ingroup-bias-Saroglou/self-report-inflate); Axis2-Q2.1-Q2.5=validating-sensitive-claims:Q2.1-community-pressure(VERDICT:biased→replace-with-socialization-environment/Voas-Crockett-2005-50%-transmission/Pew-2025-retention-table-45%-100%/Iannaccone-1994-3-factor-model:hardware-fit×community-architecture×exit-cost-multiplicative)+Q2.2-faith(VERDICT:deliberately-not-real-checking=reductive-caricature/James-1896-Will-to-Believe/Tillich/Kierkegaard/Plantinga-2000-properly-basic/commitment-under-underdetermined-evidence)+Q2.3-childhood-install(VERDICT:runs-counter-to-science/Barrett-2012-born-believers/Kelemen-2004-promiscuous-teleology/McCauley-2011-maturationally-natural→replace-install-with-cognitive-preparedness)+Q2.4-harmful-vs-beneficial(VERDICT:majority-positive/Koenig-2012-80%positive-6%harmful/Pew-2025-77%-helps-society/~70/30-ratio-for-rewrite)+Q2.5-Marx(VERDICT:superseded/Berger-1999-self-refuted/Stark-Finke-2000-rational-choice/condense-to-1-note); Axis3-Q3.1-Q3.4=community-architecture:Q3.1-per-person(Saroglou-2002-2010-Agreeableness-r=.20-Conscientiousness-r=.17-consistent-19-countries/fit-concept-per-personality-type)+Q3.2-functional-equivalence(Boyer-2001/Atran-2002/Norenzayan-2013-Big-Gods/5-core-functions-universal)+Q3.3-non-truth-dependent(VanderWeele-benefits-via-attendance-not-doctrine/Lim-Putnam-community-drives-satisfaction/Kaptchuk-2010-OLP-parallel/Japanese-religion/James-pragmatism/SBNR-community-component-critical)+Q3.4-secularization-nuance(Berger-1999-self-refuted/Habermas-post-secular/Taylor/Vervaeke-2019-meaning-crisis/Putnam-social-capital-decline/SBNR-worse-than-religious/Scandinavia-exception-needs-massive-infrastructure); Summary=Top-10-evidence/5-key-reframes/6-nuances/citation-map-table-30+-entries; 2026-06-10)
- [x] I50 Meta-Impact.md ✅ (Research\Meta-Impact\; §1–§6+Cross-refs; META-ANALYSIS=framework-predicting-its-own-impact; §1-Risks(§1.1-labeling-people:MBTI-analogy-label=light-chunk-mechanism=heavy/§1.2-self-misdiagnosis-ego-schema:chunk-serves-ego-not-domain-feedback/§1.3-weaponization-marginal-gain:attack-low-already-has-tools/defense-high-currently-zero-tools+net=democratize-defense>attack+AI-trust-entity-NEW-risk:cross-domain-default+install-compile-speed-gap+systemic-hijack); §2-Value(§2.1-understand-self:per-observation-parameters+chunk-gap+body-feedback/§2.2-understand-others:Compiled+Fresh+per-agent-valence+BUT-blackbox+54%-deception-detection+context-dependent=predict-PATTERN-not-INSTANCE/§2.3-education:4-files-principles-not-applications-yet/§2.4-mental-health:mechanism-not-label-BUT-not-treatment-conventional-essential/§2.5-current-state:rough-compass-not-GPS); §3-Dynamics(§3.1-scarcity-branches:low-scarcity→win-win/high-scarcity→exploit/§3.2-4-natural-brakes:burnout/understanding-paradox/gradual-adoption/equilibrium/§3.3-Self-Pattern-Modeling-complexity:valence-blackbox+54%-deception+context-dependent=no-master-key); §4-Meta(§4.1-self-consistent:hardware-invariant-knowing-≠-changing+chunks-change-exactly-as-mechanism-describes/§4.2-convergent-discovery:Friston+Barrett+CLARION-different-lenses+AI-expands-funnel/§4.3-adoption-bottom-up:organic-spread+differential-per-chunk-depth); §5-Failure-Modes(§5.1-wrong-node:Schultz-1997-example-prob=LOW/§5.2-wrong-connections:BIGGEST-risk-prob=MEDIUM-HIGH-new-contribution-unvalidated/§5.3-too-coarse:prob=HIGH-near-certain+3-examples/§5.4-summary-table:3-types×probability×consequence×fix); §6-🟢-meta-consistency+defense>attack/🟡-adoption-dynamics/🔴-circular-argument+optimism-bias+coarse-may-understate; 2026-06-10)
- [x] I51 Creator-Lens.md ✅ (Research\Meta-Impact\; §1–§6+Cross-refs; META-ANALYSIS=framework-shaped-by-creators-lens; §1-Profile(game-dev+somatic-processor+personal-crisis+AI-synthesis+1-person-consequences:higher-bias/higher-depth/deeper-blind-spots); §2-Game→Framework(mapping-table:stats→observation-params/state-machine→chunk-lifecycle/NPC-AI→Self-Pattern-Modeling/etc+§2.1-specific-mapping-12-concepts+§2.2-observation-first-methodology:theory-first-vs-observation-first+case-study-monkey-OCD→serotonin=amplifier-not-cause→explains-SSRI-80%-relapse+why-question-hard-within-silo+general-pattern+framework-relies-on-academic-as-foundation-loop+caveat:apophenia+confirmation+Dunning-Kruger); §3-Blind-Spots(game-arch-vs-actual-brain:discrete-vs-gradient/deterministic-vs-stochastic/clean-vs-messy/fixed-vs-shifting+§3.1-warning-signs+3-self-corrections-v6→v7.8:schema/channels/navigate-level); §4-Lens-Comparison(academic/philosopher/clinician/game-dev:each-tradeoff); §5-Creation-Process(§5.1-3-phases:accumulation-2yr/trigger-new-AI-model/sprint-1-week+role-division:I=questions+body-check/AI=domain-depth+structure+§5.2-quality-control:self-consistent≠correct+need-external-verify+§5.3-why-AI-alone-cannot:no-somatic-direction+human-alone-no-depth+echo-chamber-risk); §6-🟢-self-aware-bias+convergent-design/🟡-peer-challenge-absent+echo-chamber/🔴-no-academic-background+circular-argument; 2026-06-10)
- [x] I52 Epistemological-Position.md ✅ (Research\Meta-Impact\; §1–§7+Cross-refs; META-ANALYSIS=where-framework-stands-in-scientific-landscape; §1-Structural-Problem(conventional=middle-range-theories-not-connected+4-structural-reasons:incentive/RCT-isolates-interactions/specialization-silo/paradigm-lock+framework=attempt-to-draw-graph+precision-vs-integration-tradeoff+§1.1-why-convergence-not-happened:depth-necessary-first+Berridge/Panksepp/Damasio/Friston-each-built-1-part+outsider-different-angle-but-risk+self-referential-caveat); §2-Observation-Parameters(=latent-variables/temperature+inflation+cognitive-load-examples+Novelty=cluster-of-VTA-DRD4-chunk-gap-etc+right-question:does-it-predict+§2.2-current-status:predicts✅-generalizes⚠️-measures❌+v6→v7.8-more-honest-epistemological); §3-Complementary-Position(§3.1-framework-better-for:mechanistic-specificity-4-social-anxiety-cases/cross-domain-novel-prediction/individual-specificity+§3.2-conventional-essential:RCT-hundreds-vs-n=1/clinical-safety/foundation-layer-Schultz+Berridge+Friston-all-nodes+§3.3-validation-path:framework-validated-BY-conventional); §4-Culture-as-Parameter(natural-experiment:suppression→sublimation+underground+obsession+spectrum-persists/3-contexts-same-pattern/culture-changes-proportion-not-existence=hardware-signature/falsification-logic+genuine-predictive-power); §5-Research-Frontier(precision-psychiatry/computational-psychiatry-Friston/Borsboom-2017-network-theory/RDoC-convergent-discovery+bottom-up-vs-top-down+falsifiable-prediction:converge-7-15yr); §6-Human×AI(human=navigator-somatic/AI=domain-expert×1000+loop-process+why-AI-alone-can't+4-confidence-levels:currently-Level1); §7-🟢-clear-position+hardware-evidence+parallel-frontier/🟡-no-instrument-GAP+§1.1-circular/🔴-Level1-echo-chamber+conventional-may-converge-without-this; 2026-06-10)
- [x] I53 Collective-Schema-Pressure.md ✅ (Research\Mismatch-Patterns\; §0–§10; OBSERVATION-FILE=compound-pressure-from-multiple-collective-schemas-stacking; §0-Position(observation-not-new-mechanism+synthesis-of-Trust-Compile+Obligation+Status+Cortisol+7-mechanism-files); §1-Collective-Schema(=chunk-network-compiled-Level2-installed-Level1-via-Trust-Amplifier+example-6-obligations+schemas-NOT-bad-foundational-mechanism+4-conditions-for-pressure:too-many/rigid/hardware-mismatch/obsolete); §2-Compound-Effect(§2.1-1-schema-manageable+5-schemas-compound=MULTIPLICATIVE-not-additive+self-amplifying-spiral+§2.2-Schema-Stack-6-layers:Education/Career/Asset/Marriage/Filial/Meaning+each-manageable+6-at-once=PFC-overload+cortisol-never-drops); §3-Trade-off(§3.1-same-schema-2-outcomes:hardware-match=growth/mismatch=trauma+VTA-delta-no-body-confirm+Pathway4-threat-avoidance+§3.2-structural-not-moral+~70%-match-~15%-each-tail+mismatch-rate>0-always); §4-Asian-Confucian(§4.1-descriptive-not-prescriptive+§4.2-Density×Rigidity-2D:Nordic-low/East-Asian-high+compound=f(Density×Rigidity)+🟢Hofstede+🟡synthesis+§4.3-6-schemas:Education/Career/Asset/Marriage/Filial/Face+each-functional-in-original-context-mismatch-when-context-changed); §5-Body-Level(6-body-effects:①cortisol-sustained-5-holdings-never-drop/②PFC-overload->4-slots/③autonomy-dissonance-imposed-no-efference-copy/④meaning-disrupted-5-competing-anchors/⑤connection-hollowed-constrained-Self-Pattern-Modeling/⑥birth-rate:Korea-0.72-Japan-1.20-China-1.09); §6-Productivity-Paradox(Korea-200x-60yr/Japan/China/Vietnam+3-reasons-effective:Pathway4-Expansion/Social-Default-cheap-coordination/Trust-Compile-fast-transmission+EXPANSION≠DISCOVERY:Pathway4-poor-for-Discovery+formula:MAXIMIZE-Expansion/MINIMIZE-Discovery+HIGH-individual-cost+Expansion-Saturation-Crisis-mismatch); §7-Modern-Clash(5-schema-clashes:credential-inflation/stable-job-illusion/house-30-impossible/filial-nuclear-family/AI-era-breaks-chain+structural-lag:schemas-compile-slow-domains-change-fast); §8-Recognize-Pattern(§8.1-cannot-prescribe-Logic-Feeling-Balance/§8.2-4-step-detection:list/classify/observe-compound/domain-feedback+awareness≠rejection); §9-🟢-6-claims/🟡-6-claims/🔴-3-hypotheses+what-added:mechanism/type/body/individual-variation/trade-off+5-open-questions; §10-cross-refs; 2026-06-10)
- [x] I54 00-Goals.md ✅ (Research\Neuro-Measurement\; §1–§6; OUTLINE=measuring-brain-states-in-real-work-environments; §1-Context(4-activation-modes:tight-stable/wide-stable/wide-jumping/overload+problem:nobody-knows-current-mode+core-question:real-time-cheap-reliable-enough-to-act); §2-Goals(§2.1-6-states-to-detect:focused/creative-flow/eustress/distress/fatigue/neural-wear+§2.2-feedback-loop-analytics+§2.3-team-tool-support-not-surveillance); §3-Methods(§3.1-EEG:5-states-it-measures-well+3-states-it-measures-poorly/§3.2-HRV-wearable:4-states+Apple-Watch-Oura-Whoop-Garmin/§3.3-conversation:qualitative-high-bandwidth/§3.4-behavioral-metrics:keystroke+mouse+commits+breaks); §4-Comparison-table(4-methods×6-dimensions+optimal-combo:EEG+HRV+conversation+behavioral); §5-Framework-links(neural-efficiency+4-modes+frontal-asymmetry+evaluative-reward+body-base+PFC-Config+COMT); §6-6-open-questions; 2026-06-10)
- [x] I55 01-Implementation-Plan.md ✅ (Research\Neuro-Measurement\; §1–§7; OUTLINE=practical-implementation-roadmap; §1-5-principles(self-first/cheap-first/support-not-surveillance/correlation-first/body-base-primary); §2-Devices(§2.1-EEG-table:Muse2-$250/MuseS/Emotiv-Insight-$500/Emotiv-Epoc-X/OpenBCI+recommendation-Muse2+§2.2-HRV-table:Oura-Ring/Apple-Watch/Whoop/Garmin); §3-4-Phases(Phase0-preparation-1wk/Phase1-self-measurement-2-4wk/Phase2-pattern-analysis-1-2wk/Phase3-pilot-2-3people/Phase4-team-workflow+each-has-output-statement); §4-Risk-table(5-risks:noise/surveillance/novelty/overthinking/discomfort+mitigation); §5-Success-metrics(Phase1-2:3-states-70%-accuracy+r>0.3+body-check+Phase3-4:50%-continue+1-undetected-wear-case+measurable-workflow-improvement); §6-6-drill-questions; §7-cross-refs; 2026-06-10)

**I7. Quote-Analysis (8 files)**
- [x] I56 Work-Adversity-Fear-Cluster.md ✅ (Research\Quote-Analysis\; §0–§14; CLUSTER=5-quotes-5-cultures-5-centuries-1-mechanism; §0-verification-table(3/5-misattributed:Jung-concept-NOT-Jung/Frankl-space-NOT-Frankl-actually-Rollo-May-via-Covey/Marcus-paraphrase-by-Holiday)+full-quote-comparison-mainstream-vs-original-vs-what-was-cut; §1-logical-chain(FDR=WHAT/Jung=WHY/Frankl=WHERE/Nietzsche=WHEN/Marcus=HOW); §2-FDR-fear-loop=meta-threat(cortisol-vicious-cycle-Vyas2002/bank-run-collective-self-fulfilling-prophecy/FDR-response-as-collective-PFC); §3-Jung-suppress≠delete(5-layers:cannot-compile-not+Wegner-ironic-process+PFC-budget-depletion+compiled-suppress=buried+self-reinforcing-loop+6-step-reversal); §4-Frankl-space=PFC-window(space-wide-vs-nonexistent-5-conditions-each+space-negative-for-PTSD+Frankl-attitude-not-response); §5-Nietzsche-hormesis-vs-damage(4-outcomes-table:stronger/same/weaker/broken+7-variables+hormesis-zone=Antifragile); §6-Marcus-obstacle=prediction-delta(obstacle-expands-gap-landscape+Einstein-example); §7-convergent-concept-Adversity-Direction(approach-tag=growth/avoidance-tag=damage+5-facets-1-crystal); §8-space-as-pivot(PFC-online-vs-offline-dual-box-diagram+7-variables); §9-failure-modes(5-single-quote-dangers+5-cluster-level:F1-ignore-conditions/F2-observation-vs-prescription/F3-attitude-vs-action/F4-survivor-bias/F5-collective-ignored); §10-AI-era-inverted-problem(drive-vacuum+Marcus-inverted); §11-5-calibration-principles; §12-meta-observations(misattribution-as-Triple-Bias-phenomenon+400yr-recurrence+compression=Chunk-Miss); §13-honest-assessment(🟢🟡🔴+limitations); §14-cross-refs+citations(Vyas/Shin/Wegner/Maier&Seligman/Felitti/Gross/Taleb+full-quote-sources); 2026-06-10)
- [x] I57 Work-Chunk-Dependent-Visibility-Cluster.md ✅ (Research\Quote-Analysis\; §0–§12; CLUSTER=3-quotes-3-dimensions-1-principle; §0-verification(1-verified-Jobs-Stanford-2005/1-semi-verified-Paul-Jobs-via-biography/1-floating-Socrates-paraphrase)+oversimplification-table; §1-logical-relationship-3D-model(spatial/temporal/depth)+Dunning-Kruger-meta+tree-diagram+series-convergence-table-3-clusters; §2-Socrates-gap-landscape-expansion(oscillation-dynamics+fill→new-chunks→new-gaps+Dunning-Kruger-table-chunk-level-vs-self-assessment+specificity+depth+double-ignorance); §3-Jobs-temporal-asymmetry(Phase3-background-processing=connecting-dots+calligraphy→Mac-typography-example+constructive-simulation-constraint+probabilistic-channels-via-Background-Pattern+reflection-vs-rumination); §4-Paul-Jobs-quality-visibility(chunks-absent→body-silent-mechanism+carpenter-15yr-vs-copier-6mo+Gibson-differentiation+Compiled-Fresh-Double-Blindness+You'll-know=Background-Pattern-level+quality-compounding-leading-vs-lagging-indicator); §5-convergent-concept-Chunk-Dependent-Visibility(temporal-visibility-gradient+series-convergence-3-clusters); §6-missing-middle(body-role+domain-feedback+direction-tag-table:humility/curiosity/craftsmanship-vs-helplessness/passivity/perfectionism); §7-failure-modes(F1.1-7-Socrates/F2.1-6-Jobs/F3.1-5-Paul-Jobs); §8-AI-era(3-quotes×AI:can/cannot-each+convergent-AI-insight); §9-6-calibration-principles; §10-4-meta-observations(load-bearing-principle/attribution-pattern/2-Jobs-quotes/direction-tag-recurring); §11-honest-assessment(🟢🟡🔴); §12-cross-refs+citations-19; 2026-06-10)
- [x] I58 Work-Comparison-Thief-Of-Joy.md ✅ (Research\Quote-Analysis\; §0–§13; SINGLE-QUOTE=floating-attribution-Roosevelt-unverified; §0-verification+oversimplification; §1-upward=thief(aspiration-inflation-mechanism+social-media-amplifier+escalating-baseline×serotonin-ratchet); §2-downward=restorer(PFC-bypasses-VTA-habituation+religion-as-empirical-anti-treadmill-engineering+chunks-needed-for-downward); §3-lateral=calibrator(CHECK-function-100kyr+modern-breakdown-echo-chambers); §4-biased=amplifier(Triple-Bias-3-mechanisms+self-fulfilling-prophecy-loop); §5-status-gate=meta-mechanism(maps-wide-vs-narrow+PFC=Lawyer-3-distortion-modes); §6-convergent-concept-Comparison-Direction-Asymmetry(5×5-table-UP/DOWN/LATERAL/BIASED/GATE+series-convergence-C1-C5-table); §7-missing-middle-7-elements(frequency/subject/reference-group=compiled/timing/baseline/trainable/Background-Pattern); §8-12-failure-modes(FM-C1-4=never-compare/FM-C5-7=always-compare/FM-C8-12=direction-specific); §9-AI-era-5-dimensions(upward-amplified/downward-possible-friend/lateral-outsourced/human-vs-AI-new-axis/personalized-dual-use); §10-6-calibration-principles; §11-4-meta-observations(correct-observation-wrong-scope/1-word-5-mechanisms/floating-attribution/direction=series-variable); §12-honest-assessment(🟢🟡🔴); §13-cross-refs+23-citations; 2026-06-10)
- [x] I59 Work-Goal-And-Why.md ✅ (Research\Quote-Analysis\; §0–§8; SINGLE-QUOTE=floating-attribution-Musk-unverified; §0-why-analyze(mechanism-vs-observation+hidden-step-reveal); §1-know-goal(Imagine-Final-content+Gradient-5-levels-Level3+-needed+Gap-Direction-sharp→reward-fires-accurately+Boredom-mechanism-no-goal=Drive-PFC-Spinning); §2-know-why(material-for-Anchor-Schema-NOT-anchor-itself+Source④-External-Inject+Valence-Propagation-schema-chain+No-knowledge=no-gap-applied-to-purpose+Body-acceptance=hidden-step+4-rejection-cases:value-conflict/chain-too-abstract/trust-insufficient/negative-trust); §3-look-forward+enjoy(opioid-preview-via-Imagine-Final+Compiled-Quality-Genuine+By-Product-Match-During-Work+Positive-Trust-vs-Negative-Trust-6-row-table); §4-unified-diagram(Goal→Gap-direction→Why+body-acceptance→Look-Forward→Enjoy→Work-Better); §5-5-failure-modes(value-conflict/why-too-abstract/leader-not-trusted/negative-trust/anchor-type-mismatch); §6-6-calibration-principles(vivid-not-just-clear/genuine-not-just-logical/match-anchor-type/positive-trust/repeat-to-compile/allow-body-acceptance-time); §7-honest-assessment(🟢🟡🔴); §8-cross-refs+citations(Locke&Latham/Deci&Ryan/Damasio/Schultz/Csikszentmihalyi/Berridge/Schacter/Hackman&Oldham); 2026-06-10)
- [x] I60 Work-Journey-Destination-Cluster.md ✅ (Research\Quote-Analysis\; §0–§13; CLUSTER=6-quotes-5-traditions-1-paradox; §0-verification(1/6-verified-LeGuin-1969/1-uncertain-ThichNhatHanh-likely-Muste/4-floating)+oversimplification-3-ways; §1-progression(Binary→Positive-Definition→Cultural→Identity→Paradox→Synthesis); §2-basic-Q1+Q2+Q4(Satiation-Profile-Mismatch:Cyclic-vs-Generative+Hedonic-Treadmill+Q2=STATE-type-anchor+Q4=cultural-schema-installed-destination); §3-identity-Q5(Pathway1-pure-identity+Imagine-Final-lifecycle=the-journey-literally+reward-fires-Phase1+Phase3+Phase4); §4-paradox-Q3(meta-trap-destruction:using-journey-as-tool=still-destination+Muste-ancestry+failure-mode=toxic-positivity); §5-synthesis-Q6-LeGuin(Anchor-Paradox:destination=essential-as-navigation-tool+achieving=Anchor-Exhausted+destination=compass-not-reward); §6-convergent-concept-Imagine-Final-Navigation-Paradox(3-structural-components:Satiation-Mismatch+Pathway1vs2+Anchor-Paradox+series-convergence-C1-C4-table+direction-tag-recurs); §7-missing-middle-6-elements(body-role/satiation-profile/direction-essential/domain-feedback/cortisol-direction-tag/per-person-variation); §8-12-failure-modes(5-destination:FM-D1-Anchor-Exhaustion/FM-D2-Treadmill/FM-D3-Schema-Install/FM-D4-Pathway2-Dependency/FM-D5-Meaning≠Happiness+7-journey:FM-J1-no-direction/FM-J2-Tonic-habituation/FM-J3-meta-destination-trap/FM-J4-toxic-positivity/FM-J5-anti-destination-overcorrection/FM-J6-schema-journey/FM-J7-avoidance-journey); §9-AI-era-5-dimensions(destination-accelerator/fills-Pathway2-not-1/given-answer=journey-bypass/amplifies-journey-need/optimize-happiness-anti-pattern); §10-6-calibration-principles; §11-4-meta-observations; §12-honest-assessment(🟢🟡🔴); §13-cross-refs+19-citations; 2026-06-10)
- [x] I61 Work-Move-Fast-Break-Things.md ✅ (Research\Quote-Analysis\; §0–§8; SINGLE-QUOTE=verified-Zuckerberg-IPO-2012+changed-F8-2014; §0-comparison-table(Goal+Why/Hungry+Foolish/Fast+Break:levels/direction/source/unique)+lifecycle(2006-born/2012-thrived/2014-self-changed/2017-criticism); §1-decode-move-fast(Context-A-early=natural-state-cost≈0/Context-B-mature=suppress-genuine=cost②+speed=prediction-delta-per-time=faster-learning+fast-with-direction-≠-fast-without:Drive-PFC-Resolve-vs-Spinning); §2-decode-break-things(break=negative-prediction-delta=forced-chunk-update+delta=0=no-update+same-break-different-direction-tag→different-for-life:Founder-approach-vs-Employee-threat+compiled-base-cost=f(depth×density):cheap-early/expensive-late); §3-combined-early-stage-5-conditions(low-compiled-base/cheap-errors/no-Background-Pattern/PFC-budget-full/novelty-drive-satisfied+ENGINE-ROAD-VEHICLE); §4-lifecycle(compiled-base-grows→cost-grows+compiled-caution=genuine-signal:genuine-vs-schema-suppress-table+entity-access-disruption:users-Level3-4-trust-violation+stable-infrastructure=framework-aligned:Hold-only=optimal); §5-5-failure-modes(speed-as-identity/break-others/fast-without-direction/skip-domain-feedback/chronic-crisis-PFC-damage); §6-6-calibration-principles(domain-maturity/break-your-own/feedback-loop/genuine-caution-respect/oscillate-sprint-consolidate/per-person-DRD4); §7-honest-assessment(🟢🟡🔴); §8-cross-refs+13-citations; 2026-06-10)
- [x] I62 Work-Stay-Hungry-Stay-Foolish.md ✅ (Research\Quote-Analysis\; §0–§8; SINGLE-QUOTE=verified-StewartBrand-Jobs-Stanford-2005; §0-comparison-table(Goal+Why-vs-Hungry+Foolish:external-vs-internal/prescriptive-vs-philosophical/floating-vs-verified/management-vs-death); §1-hungry(Generative-satiation-profile:fill→new-gaps→perpetual+VTA-still-fires=capacity-for-surprise+expert-has-MORE-novelty-counter-intuitive:combinatorial-space-grows+not-hungry=Type3-boredom=Drive-PFC-Spinning); §2-foolish(Resist-Background-Pattern-Triple-Bias:Retrieval/Template/Interpretation+gaps-open=prevent-premature-closure+PFC-double-cost①+②+only-sustainable-in-generative-environment); §3-synergy(hungry-alone=tunnel-vision/foolish-alone=never-masters+both=ENGINE-running+ROAD-open+Jobs-evidence); §4-death-context(ultimate-Anchor-Schema-disruption+cortisol-direction-tag-clarifies+weak-anchors-collapse/strong-remain+Type3-boredom-forced+death-strips-Background-Pattern-bias); §5-6-failure-modes(3-hungry:novelty-loop/status-escalation/workaholic+3-foolish:actually-incompetent/ignore-domain-feedback/Dunning-Kruger+combination-fail:no-arbiter=delusion/depleted-PFC=burnout); §6-6-calibration-principles(generative-test/expertise-prerequisite/explore-not-execute/domain-arbiter/PFC-oscillate/per-person-DRD4); §7-honest-assessment(🟢🟡🔴); §8-cross-refs+12-citations; 2026-06-10)
- [x] I63 Work-Think-Act-Become-Cluster.md ✅ (Research\Quote-Analysis\; §0–§11; CLUSTER=2-quotes-2-halves-1-pipeline("Fake it till you make it"=OUTER-HALF/action+attribution-floating-Amy-Cuddy-2012+"The mind is everything"=INNER-HALF/thought+attribution-UNVERIFIED-not-Pali-Canon); §0-verification-table(0/2-confirmed)+mainstream-vs-original(Aristotle-practice-in-community/Dhammapada-mind-LEADS-not-IS)+what's-missing; §1-logical-relationship(Think→Act→DomainFB→BodyConfirm→Compile→Become:Quote2-covers-THINK/Quote1-covers-ACT/BOTH-miss-middle-2-steps); §2-fake-it-decoded(3-types:Hold-Only/Hold+Suppress/Permanent-Performance+3-outcomes:Genuine-Shift/Compiled-Suppress/PFC-Failure+direction-tag:curiosity→approach/obligation→flat/fear→avoidance+bootstrap-mechanism=framework-version+efference-copy=body-always-knows); §3-mind-everything-decoded(PFC=5%-extension-not-source/Triple-Bias:Retrieval+Template+Interpretation/think-alone-insufficient-4-reasons:Oettingen-effect+no-body-chunks+PFC-seed≠PFC-create+fix-body-first/reflection-vs-rumination:curiosity-direction-vs-threat-direction); §4-Compile-Quality-Gate(5-variables:Direction-tag+Body-confirm+Domain-feedback+Internal-vs-External-drive+Existing-pattern-depth+3-outcomes:Genuine/Schema/Threat-compiled); §5-missing-middle(domain-feedback+body-confirmation=2-steps-both-quotes-skip); §6-8-failure-modes(compiled-suppress-masquerades/imposter-syndrome-loop/Oettingen-effect/rumination-as-thinking/wrong-direction/toxic-positivity/Background-Pattern-resistance/PFC-budget-exhaustion); §7-AI-era(AI-amplifies-both→Quality-Gate-more-important/risk=industrial-scale-hollow-success/opportunity=AI-as-domain-check-tool); §8-6-calibration-principles; §9-4-meta-observations(popularity∝1/nuance/PFC-illusion/compression-3-step→1-step/series-convergence); §10-honest-assessment(🟢🟡🔴); §11-cross-refs+19-citations; 2026-06-10)

**I8. Drill-Sound-Brain (11 files)** ⭐
- [x] I64 00-Overview.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/00-Overview.md | Entry point + reading guide: 44-insight index, 5 validation points, 5 testable predictions, 7 open questions, folder structure, dependencies, framework position | v1.5
- [x] I65 01-Sound-Brain-Neuroscience.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/01-Sound-Brain-Neuroscience.md | Evidence base: 10 research axes, 120+ citations (Salimpoor/Martínez-Molina/Cheung/Boer/Selfhout landmarks), 10 synthesis blocks, honest assessment table | v1.1
- [x] I66 02-Sound-Background-Pattern.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/02-Sound-Background-Pattern.md | 8 insights: multi-modal chunks, genre context, taste signature=PFC label, Alzheimer 2D model, 3 satiation types, structural valence, frequency-driven, snowball+locked taste | v1.2
- [x] I67 03-Sound-Reward-Pipeline.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/03-Sound-Reward-Pipeline.md | 7-step validation: Salimpoor 2011 caudate/NAcc direct validation, musical anhedonia pipeline proof, Cheung 2019 Goldilocks, PCM precision weighting, music boredom formula | v1.1
- [x] I68 04-Sound-Social-Resonance.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/04-Sound-Social-Resonance.md | 14 insights, 5-step mechanism chain (★ framework contribution), values not personality (Boer 2011), niche>mainstream (Selfhout 2009), influence>selection (Ter Bogt 2017), TP1 blind compatibility (untested, framework-novel) | v1.2
- [x] I69 05-Multi-Modal-Compound.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/05-Multi-Modal-Compound.md | 3-tier hierarchy (Sound→+Visual→+Action), coherence=gate for super-additive reward, efference copy Tier 3 exclusive, film vs game different profiles, user hypothesis refined | v1.2
- [x] I70 06-Music-Architecture-Prediction.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/06-Music-Architecture-Prediction.md | Foundational reference: ~94% pop=4/4, BPM=120=locomotion, verse-chorus 80-90%+, tonic=prediction anchor, tension-resolution=gap-fill cycle, fractal 5-level nesting, integer ratio principle unifying pitch+rhythm | v1.2
- [x] I71 07-Music-Entrainment-Reward-Dynamics.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/07-Music-Entrainment-Reward-Dynamics.md | Distributed entrainment (putamen/SMA hub NOT clock), continuous prediction stream with phasic peaks, gap-formation inverted-U (5 phases P0→P4), 2-mode enjoyment (flow vs expert appreciation), PFC budget matrix (compiled+familiar=optimal, fresh+unfamiliar=worst), unified hierarchy music=math=startup, Hou 2024 corrects "analysis kills pleasure" | v1.2
- [x] I72 08-Musical-Elements-Brain-Interface.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/08-Musical-Elements-Brain-Interface.md | Voice 3-channel (Semantic/Prosody/Voice-as-instrument), melody = highest activation efficiency (~5-6 systems/1 line), earworm mechanism, shape vs content (Langer 1953), 3 mechanisms (Direct/Learned/Isomorphic), BRECVEMA compression | v1.1
- [x] I73 09-Verification-Research.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/09-Verification-Research.md | Quality control: 3 rounds, 30 corrections, 35+ citations; key findings: "analysis kills pleasure" wrong (Hou 2024), "melody = first locked" unsubstantiated, I-IV-V 62% no source, peak at 2-8 exposures (Schellenberg 2008) | v2.0
- [x] I74 10-Synthesis.md — DONE 2026-06-10 | English/Research/Drill-Sound-Brain/10-Synthesis.md | Complete synthesis: 6 validations (Salimpoor/Martínez-Molina/Cheung/Boer/Selfhout/Chmiel), 10 extensions, 49% confirmed/43% synthesis/7% untested/0% wrong, 5 testable predictions, 7 open questions, 4 correction patterns | v1.0

### Phase J — Applications (8 files)
- [x] J01 00_Overview.md — DONE 2026-06-10 | English/Applications/Education-System/00_Overview.md | Folder map v2.3: 5-tier architecture, file flow diagram, reading order per audience, Tier 1-3 connections, durability guide + statistics | v2.3
- [x] J02 Education-System.md — DONE 2026-06-10 | English/Applications/Education-System/Education-System.md | Main framework v3.2: 4 stages (6-12/12-18/18-25+), 5 roles, ENGINE/ROAD/VEHICLE throughout, Compile Architecture (Trust→Experience→Expertise), Trust×Self-Observation×Stages matrix, teacher 8 lenses, parent Trust dynamics, 4-channel integration, constraints+reality, honest assessment | v3.2
- [x] J03 Hardware-Calibration.md — DONE 2026-06-10 | English/Applications/Education-System/Hardware-Calibration.md | 6 hardware dimensions (DIM 1-6: modality/VTA/cortisol/PFC-pace/social/body-base), per-age observable indicators, calibration strategies per DIM, Trust×Calibration Quality (trust-intention upstream), Self-Observation×Calibration Depth (teacher Level 4-5), Trust×Self-Observation coupled matrix (4 states), neurodiversity reframe (ADHD/ASD/Gifted/LD), miscalibration labels (lazy/slow/hyperactive/unmotivated) + Dissonance-Signal-Architecture + trust+self-observation root causes, 5-step calibration cycle, Entity-Access+Entity-Compiled lenses | v1.2
- [x] J04 Curriculum-Framework.md — DONE 2026-06-10 | English/Applications/Education-System/Curriculum-Framework.md | Delivery matrix v2.3: 7 curriculum principles (Foundation First/Mechanism-Based/Adaptability/Developmental Timeline/Gap Landscape/Societal Subsidy/PFC Budget), 3-tier taxonomy (Foundation/Era-specific/Per-hardware), Foundation Matrix L1-L4 × 6 domains × 4 stages, Compiled Quality cross-cut, PFC Budget constraint, v2.2 Compile Type per-domain, v2.3 Self-Observation cross-cutting infrastructure (Level targets per stage), Era-specific delivery (AI/InfoCuration/SystemsThinking/SciLit/CrossCultural/DigWellbeing), Sequencing balance table, v2.2 Multi-Stream sequencing, v2.3 Trust-aware sequencing (trust-first/trust-intensive/trust-calibration), Reduce/Don't-Remove guidance | v2.3
- [x] J05 Era-Analysis-2025.md — DONE 2026-06-10 | English/Applications/Education-System/Era-Analysis-2025.md | Era context layer v2.2: §0 purpose+disclaimer (expiry date, prediction limits, tech-centric bias), §1 technology landscape (LLM/AI Agents/Generative AI/Education AI, rate-of-change pattern, Simulation-Engine lens), §2 changing skills (knowledge access shift, chunk threshold, job market, learning changes, info overload), §3 constants anchor (brain mechanism/development timeline/social needs/foundation skills), §4 six major uncertainties (AGI trajectory, job market, attention+brain, AI tutor, geopolitics, inequality, AI relationships+phantom type+Trust lens), §5 six era themes + Gap Landscape + Hardware-Subsidy era impact, §6 honest assessment | v2.2
- [x] J06 VN-Education-Status.md — DONE 2026-06-10 | English/Applications/Education-System/Country/VN/VN-Education-Status.md | VN education snapshot v2.2: §0 system overview (5-level structure, 2024-2025 scale, budget decline 5.7%→2.89% GDP, GDPT 2018 reform, TALIS 2024 teacher data, PISA trend), §1 Education-Mechanism lens (6/8 arc design principles ✗, bridge ④-dominant, 3 ORIGIN Imposed-dominant, system-level foundation lopsided), §2 five strengths (literacy/teacher platform/GDPT 2018/family involvement/efficiency), §3 six weaknesses (CRITICAL: threat-dominant+direction wrong+Dissonance+Trust damage+Self-Observation unlabeled deficit; HIGH: one-size+hardware; Imagine-Final narrow+external; MEDIUM: bridge escalating+surface assessment; STRUCTURAL: rural-urban-ethnic gap), §4 six data tables (mental health/teachers/private tutoring/PISA/disparities/university+employment), §5 gap analysis table (14 dimensions with %-bars, new concept gaps, GAP≠BLAME), §6 honest assessment (6 limitations, confidence table, reading recommendation), Connections (5 tiers) | v2.2
- [x] J07 VN-Cultural-Factors.md — DONE 2026-06-10 | English/Applications/Education-System/Country/VN/VN-Cultural-Factors.md | VN cultural factors v2.2: §0 Hofstede dimensions (Power Distance 70/Individualism 30/restrained), culture=context framing; §1 eight factors (①Teacher Reverence: Trust Social Norm Install, platform+passive risk; ②Transform Life: strong but narrow+external Imagine-Final, 60% wrong field; ③Collectivism: face-saving suppresses Self-Observation vocabulary; ④Extended Family: trust depth 5/5 sources, guilt=corrupted subsidy; ⑤Endurance: delays gratification skill+suppresses body-state observation; ⑥Credential: Trust Generalization chain 844 years; ⑦Hierarchy: suppresses Phase 3 calibration; ⑧Regional: compound ethnic minority barriers); §2 Culture×Mechanism 8×8 matrix (Culture=PROTECTS Foundation+HINDERS Depth+Per-individual; 5/8 factors permit chronic Imposed; 4/8 factors normalize threat-path); §3 five leverage points (Teacher Trust→Calibrator ★★★★★; Family Redirect ★★★★★; Expand Imagine-Final ★★★★☆; Delayed Gratification Redirect ★★★☆☆; Collectivism→Peer Learning ★★★☆☆); §4 four risk points (CRITICAL: chronic Imposed 5/8 factors; HIGH: passive learning 4/8; HIGH: Forced-Fit scale 4/8; STRUCTURAL: widening gap); §5 honest assessment (6 limitations, confidence table, PISA Paradox="knows but hates it" at scale, "Keep DRIVE change DIRECTION") | v2.2
- [x] J08 VN-Recommendations.md — DONE 2026-06-10 | English/Applications/Education-System/Country/VN/VN-Recommendations.md | VN final recommendations v2.2: §0 Imagine-Final derived (Global×VN strengths×Era×New concepts) — five targets (Students/Teachers/Families/Society/Ethnic minorities); §1 priority actions Tier1 QW-1 Direct-State Recovery+Direction (Self-Observation Level 2 prerequisite→⓪detect before rest), QW-2 per-hardware+Entity-Access seed (Trust-intention signal), QW-3 Imagine-Final micro+Connection seed ($0 immediate); Tier2 MT-1 Teacher Trio Calibrator (5 modules: HOW/WHAT/WHO/Bridge/Trust+Self-Observation, CONVERT structural→relational trust), MT-2 Assessment reform (Compiled Quality+gap diversification+separate graduation/university exams), MT-3 Imagine-Final program+Entity-Access (hardware discovery gr7-9, simulation workshop gr10-11), MT-4 Hardware-Subsidy optimization; Tier3 LT-1 class size reduction, LT-2 Trio curriculum, LT-3 per-individual tracking, LT-4 ethnic minority foundation, LT-5 cultural narrative shift (15-30yr); §2 transition path "fixing airplane mid-flight" (Direct-State first, 4-phase roadmap, GDPT 2018 synergy, realistic constraints); §3 per-stakeholder MOET/schools/teachers/parents/students; §4 five VN contributions to global Imagine-Final (Subsidy Platform Model, PISA Paradox, Dissonance-Signal-Architecture first-mover, Trio curriculum, Keep Drive Change Direction); §5 honest assessment (armchair risk, complexity risk, cannot guarantee, phantom risk) | v2.2

### Phase K — File Index Regeneration (3 files)
- [x] K01 Core-Deep-Dive/01-File-Index.md — DONE 2026-06-10 | English/Core-Deep-Dive/01-File-Index.md | Full 185-entry index regenerated in English: all Body-Base (Chunk/Feeling/Schema/Melody/Body-Feedback subfolders + drills), Observation (Novelty/Threat/Boredom/Drive/Empathy/Connection/Status/Protect/Meaning/Autonomy/Liking-Wanting/Gratitude/Obligation/AI-Detection), PFC (Function/Hardware/Configuration/Development/Operations/Simulation-Engine/Label/Logic-Feeling/Imagine-Final/Self-Observation), Collective, Domain, Clarification folders; descriptions translated to English with framework vocabulary preserved (Self-Pattern-Modeling, Hardware-Subsidy, Entity-Access Level 0-5, Compiled Quality, ENGINE/ROAD/VEHICLE, Simulation-Engine, Gap-Distribution-Profile, Bond-Architecture, Resonance-Sustainability, Reward-Signal-Architecture/Dissonance-Signal-Architecture, Compile-Taxonomy, Compile-Sleep, Background-Pattern, Coordination-Node, By-Product-Scale, Phantom 4-factor, etc.)
- [x] K02 Research/01-File-Index.md — DONE 2026-06-10 | English/Research/01-File-Index.md | Full 99-entry Research index regenerated in English: Human-Learning (Child-Development 4 files, Education-Mechanism 7 files), Global (Human-AI-Future/Social-Calibration/AI-Self-Model/Uncanny-Valley/Innovation-Geography + Birth-Rate-Decline 8 files), Health-Conditions (Hijack 4 files, Neurodiversity 4 files, Neurodegeneration 2 files, OCD/PTSD), Melody-Technology (Religion/Idol/Drill + Overview), Meta-Impact (3 files), Mismatch-Patterns, Neuro-Measurement (2 files), standalone Research files (Money-Analysis/Climate-Cognition/Fidgeting/Love-Romantic/Love-Unified/Relativity/Self-Created-Threat/Sensitivity), Quote-Analysis (12 files), Drill-Sound-Brain (11 files); all descriptions translated to English with framework vocabulary preserved
- [x] K03 Applications/01-File-Index.md — DONE 2026-06-10 | English/Applications/01-File-Index.md | 8-entry Applications/Education-System index regenerated in English (see K03 annotation above)

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
