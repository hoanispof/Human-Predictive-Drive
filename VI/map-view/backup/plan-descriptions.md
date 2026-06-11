# Plan: Descriptions Rewrite — global-index.json

> **Goal:** Fill shortDescription + fullDescription for all 234 files in global-index.json.
> Also verify domains / area / contentType per file.
> Language: 100% English. Chậm mà chắc — read each file before writing.
>
> **Created:** 2026-05-31
> **Status:** ✅✅ COMPLETE — All Batches A through L done. 233/234 files indexed (Body-Listening-Journey.md not present in global-index.json — skipped 🚫).

---

## §1 — Style Guide

### shortDescription (1 sentence, English, target <150 chars)

**Pattern:** `[Core concept] — [key content in plain language]`

**Rules:**
- Describe WHAT'S INSIDE the file, not "why/how" teaser
- No framework jargon without plain-language explanation
- If file has a clear thesis → state it directly
- If file is an overview/collection → list main elements briefly
- Laypeople (no framework knowledge) should understand after reading

**Examples — Good vs Bad:**

| File | ✗ Bad | ✓ Good |
|------|--------|--------|
| Chunk.md | "The foundational storage unit of the framework" | "Mental units (chunks) store all knowledge, habits, and patterns — how the brain accumulates and connects everything" |
| Dopamine-Is-Not-Reward | "Why dopamine is misunderstood" | "Dopamine signals 'pay attention,' not 'this feels good' — the most common pop-neuroscience mistake explained" |
| Body-Feedback.md | "Unified model body signal = function of 5 preconditions" | "The body generates signals through 5 simultaneous conditions — entry point for the 17-file body signal folder" |
| Hidden-Quality-Perception | "Compilation depth determines quality visibility" | "People literally cannot perceive quality in areas they lack experience — covers why experts see what beginners cannot" |
| Connection.md | "3 Generative Primitives, 8 pathways" | "Human connection has 3 generative sources and 8 pathways — how bonds form, what sustains them, and why they decay" |

---

### fullDescription (2–20 lines, English, use `\n` between paragraphs)

**Structure:**
```
Paragraph 1: Main concept — what is this file about, in plain language.
\n
Paragraph 2: Key mechanisms, models, or findings covered.
\n
Paragraph 3 (if needed): Notable sections, specific analyses, or edge cases.
\n
Last (optional): Practical implications or AI-era relevance.
```

**Rules:**
- `\n` = paragraph separator (rendered as `<br>` in HTML tooltip)
- Write in paragraphs, not bullet points
- Core mechanism files: longer (6–15 lines)
- Drill files: shorter (3–6 lines) — they're deep-dive support material
- Overview/reference: medium (4–8 lines)
- Enough to understand the scope without reading the file

**Example — Hidden-Quality-Perception.md:**
```
The brain can only detect a 'gap' (something missing) in areas where it already has built-up knowledge. This means people cannot perceive quality they've never encountered — not a failure of effort, but an architectural constraint of how memory works.
\n
Covers two types of hidden quality: technical depth (what domain experts see that novices cannot) and organizational quality (what coordinators see that others miss). Includes a meta-analysis reframe of Dunning-Kruger that differs from the popular version.
\n
AI-era note: AI can detect pattern-level quality but cannot detect body-level quality signals — the same architectural limitation applies. 24+ citations, ~1,738 lines.
```

**Example — 01-Foundation.md (drill file):**
```
A drill (deep-dive Q&A) exploring the foundation of body signal architecture: why the body pulls schemas in two opposing directions simultaneously (Hardware pull vs Domain pull), and how this creates the 6-step interface loop.
\n
Covers: Dual-Pull architecture, Interface Loop 6-step model, 2-layer calibration (why body signals are trustworthy), and the distinction between body-feedback and feeling.
```

---

### domains / area / contentType Verification

**domains** (multi-tag per file — check all that apply):
- `core` = any reader should encounter this file (foundation files)
- `neuroscience` = covers brain mechanisms, neurotransmitters, neural circuits
- `psychology` = covers behavior, cognition, mental processes
- `behavioral` = covers decision-making, behavioral economics, habits
- `development` = covers child development, lifespan, learning trajectories
- `education` = covers teaching, learning environments, curriculum
- `clinical` = covers mental health conditions, therapy, clinical applications
- `social-collective` = covers group dynamics, society, coordination
- `ai-tech` = relevant to AI systems, technology design, human-AI interaction
- `philosophy` = covers epistemology, ethics, meta questions

**area** (single tag — which framework section):
`core-foundation` | `observation-params` | `body-feedback` | `chunk-system` | `agent-mechanism` | `pfc-system` | `feeling-system` | `schema-anchor` | `collective` | `domain-theory` | `health-conditions` | `child-development` | `education-app` | `global-analysis` | `meta-epistemology` | `reference-tools` | `melody-lens` | `clarification`

**contentType** (single tag):
- `mechanism` = explains HOW something works (core mechanism file)
- `analysis` = deep analysis of one topic (research or applied)
- `observation` = observation parameter file (what to observe in the world)
- `drill` = drill/Q&A deep exploration (supporting material)
- `overview` = synthesis, entry point, index
- `practical` = guide for application or practice
- `reference` = vocabulary, labels, tools, index

---

## §2 — Progress Tracker

Legend: `⬜` pending | `🔄` in progress | `✅` done

---

### BATCH A — Core Foundation + Observation Parameters (~32 files)
*Priority: HIGHEST — entry points for all readers*

**Core Foundation (16 files)**
- ✅ `00-Parameter-Overview.md` — `00-Parameter-Overview.md`
- ✅ `Ask-AI.md` — `Ask-AI.md`
- ✅ `Core-Hardware.md` — `Core-Hardware.md`
- ✅ `Core-Software.md` — `Core-Software.md`
- ✅ `Auditory-Hardware.md` — `Core-Deep-Dive/Auditory-Hardware.md`
- ✅ `Blackbox-Map.md` — `Core-Deep-Dive/Blackbox-Map.md`
- ✅ `Body-Base.md` — `Core-Deep-Dive/Body-Base/Body-Base.md`
- ✅ `Body-Coupling.md` — `Core-Deep-Dive/Body-Base/Body-Coupling.md`
- ✅ `Cortisol-Baseline.md` — `Core-Deep-Dive/Body-Base/Cortisol-Baseline.md`
- ✅ `Entity-Valence-Dynamics.md` — `Core-Deep-Dive/Body-Base/Entity-Valence-Dynamics.md`
- ✅ `Inter-Body-Mechanism.md` — `Core-Deep-Dive/Body-Base/Inter-Body-Mechanism.md`
- ✅ `Valence-Propagation.md` — `Core-Deep-Dive/Body-Base/Valence-Propagation.md`
- ✅ `Why-Body-Knows.md` — `Core-Deep-Dive/Body-Base/Why-Body-Knows.md`
- ✅ `Modality.md` — `Core-Deep-Dive/Modality.md`
- ✅ `Neural-Architecture.md` — `Core-Deep-Dive/Neural-Architecture.md`
- ✅ `Neural-Processing-Flow.md` — `Core-Deep-Dive/Neural-Processing-Flow.md`

**Observation Parameters (16 files)**
- ✅ `Novelty.md` — `Core-Deep-Dive/Observation/Novelty.md`
- ✅ `Threat.md` — `Core-Deep-Dive/Observation/Threat.md`
- ✅ `Boredom.md` — `Core-Deep-Dive/Observation/Boredom.md`
- ✅ `Drive.md` — `Core-Deep-Dive/Observation/Drive.md`
- ✅ `Empathy.md` — `Core-Deep-Dive/Observation/Empathy.md`
- ✅ `Connection.md` — `Core-Deep-Dive/Observation/Connection.md`
- ✅ `Status.md` — `Core-Deep-Dive/Observation/Status.md`
- ✅ `Protect.md` — `Core-Deep-Dive/Observation/Protect.md`
- ✅ `Meaning.md` — `Core-Deep-Dive/Observation/Meaning.md`
- ✅ `Autonomy-Hardware.md` — `Core-Deep-Dive/Observation/Autonomy-Hardware.md`
- ✅ `Autonomy.md` — `Core-Deep-Dive/Observation/Autonomy.md`
- ✅ `Liking-Wanting.md` — `Core-Deep-Dive/Observation/Liking-Wanting.md`
- ✅ `Gratitude.md` — `Core-Deep-Dive/Observation/Gratitude.md`
- ✅ `Obligation.md` — `Core-Deep-Dive/Observation/Obligation.md`
- ✅ `AI-Schema-Detection.md` — `Core-Deep-Dive/Observation/AI-Schema-Detection.md`
- ✅ `AI-Collective-Detection.md` — `Core-Deep-Dive/Observation/AI-Collective-Detection.md`

---

### BATCH B — Body-Feedback System (~17 files)

**Mechanism + Reference (12 files)**
- ✅ `Body-Feedback.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback.md`
- ✅ `Body-Feedback-Precondition.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Precondition.md`
- ✅ `Body-Feedback-Label.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Label.md`
- ✅ `Body-Feedback-Mechanism.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Body-Feedback-Mechanism.md`
- ✅ `Gap-Direction.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Gap-Direction.md`
- ✅ `Gap-Distribution-Profile.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Gap-Distribution-Profile.md`
- ✅ `Gap-Body-Need.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Gap-Body-Need.md`
- ✅ `Hidden-Quality-Perception.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Hidden-Quality-Perception.md`
- ✅ `Action-Space.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Action-Space.md`
- ✅ `Reward-Signal-Architecture.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Reward-Signal-Architecture.md`
- ✅ `Dissonance-Signal-Architecture.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Dissonance-Signal-Architecture.md`
- ✅ `Reward-Calibration.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Reward-Calibration.md`

**Drill files (5 files)**
- ✅ `01-Foundation.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/01-Foundation.md`
- ✅ `02-Dissonance.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/02-Dissonance.md`
- ✅ `03-Reward.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/03-Reward.md`
- ✅ `04-Integration.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Body-Feedback/04-Integration.md`
- ✅ `Drill-Evolutionary-Sensor-Architecture.md` — `Core-Deep-Dive/Body-Base/Body-Feedback/Drill-Evolutionary-Sensor-Architecture.md`

---

### BATCH C — Feeling System + Clarification (~22 files)

**Feeling Mechanism (8 files)**
- ✅ `Feeling.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling.md`
- ✅ `Feeling-Research.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling-Research.md`
- ✅ `Feeling-Mechanism-Deep-Draft.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling-Mechanism-Deep-Draft.md`
- ✅ `Feeling-Sources-Draft.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling-Sources-Draft.md`
- ✅ `Feeling-Accuracy-Draft.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling-Accuracy-Draft.md`
- ✅ `Feeling-Chunk-Bridge-Draft.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling-Chunk-Bridge-Draft.md`
- ✅ `Feeling-Literacy-Training-Draft.md` — `Core-Deep-Dive/Body-Base/Feeling/Feeling-Literacy-Training-Draft.md`
- ✅ `Body-Knowing.md` — `Core-Deep-Dive/Body-Base/Feeling/Body-Knowing.md`

**Feeling Overview + Drill (10 files)**
- ✅ `00-Reading-Notes.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/00-Reading-Notes.md`
- ✅ `99-Overview-Synthesis.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/99-Overview-Synthesis.md`
- ✅ `01-Theme-A-Architecture.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/01-Theme-A-Architecture.md`
- ✅ `02-Theme-D-Right-Wrong.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/02-Theme-D-Right-Wrong.md`
- ✅ `03-Theme-B-Verbal-Chain.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/03-Theme-B-Verbal-Chain.md`
- ✅ `04-Theme-C-Ritual.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/04-Theme-C-Ritual.md`
- ✅ `05-Theme-E-Empathy-Giving.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/05-Theme-E-Empathy-Giving.md`
- ✅ `06-Theme-F-Logic-Feeling-Check.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Knowning/06-Theme-F-Logic-Feeling-Check.md`
- ✅ `Feel-Development.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Dev/Feel-Development.md`
- ✅ `Feel-Example-Draft.md` — `Core-Deep-Dive/Body-Base/Feeling/Drill-Feeling-Dev/Feel-Example-Draft.md`

**Clarification (4 files)**
- ✅ `Dopamine-Is-Not-Reward.md` — `Core-Deep-Dive/Clarification/Dopamine-Is-Not-Reward.md`
- ✅ `Cortisol-Amplifier-Not-Cause.md` — `Core-Deep-Dive/Clarification/Cortisol-Amplifier-Not-Cause.md`
- ✅ `Mirror-Neuron-Rejection.md` — `Core-Deep-Dive/Clarification/Mirror-Neuron-Rejection.md`
- ✅ `Prediction-Error-Is-Not-Reward.md` — `Core-Deep-Dive/Clarification/Prediction-Error-Is-Not-Reward.md`

---

### BATCH D — Chunk System Core + Schema-Anchor (~15 files)

**Chunk Mechanism + Overview (11 files)**
- ✅ `Chunk.md` — `Core-Deep-Dive/Body-Base/Chunk/Chunk.md`
- ✅ `Compile-Taxonomy.md` — `Core-Deep-Dive/Body-Base/Chunk/Compile-Taxonomy.md`
- ✅ `Background-Pattern.md` — `Core-Deep-Dive/Body-Base/Chunk/Background-Pattern.md`
- ✅ `99-Master-Synthesis.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/99-Master-Synthesis.md`
- ✅ `09-Event-Chunks-Inference-Matrix.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/09-Event-Chunks-Inference-Matrix.md`
- ✅ `10-F1-Synthesis.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/10-F1-Synthesis.md`
- ✅ `00-Chunk-System-Sketch.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Foundation/00-Chunk-System-Sketch.md`
- ✅ `01-External-Synthesis.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/01-External-Synthesis.md`
- ✅ `00-Internal-Mechanism-Overview.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/00-Internal-Mechanism-Overview.md`
- ✅ `05-Insight-Tacit-Upgrade.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/05-Insight-Tacit-Upgrade.md`
- ✅ `06-Internal-Synthesis.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/06-Internal-Synthesis.md`

**Schema-Anchor (4 files)**
- ✅ `Schema.md` — `Core-Deep-Dive/Body-Base/Schema/Schema.md`
- ✅ `Anchor-Schema.md` — `Core-Deep-Dive/Body-Base/Schema/Anchor-Schema.md`
- ✅ `Anchor-Schema-Example.md` — `Core-Deep-Dive/Body-Base/Schema/Anchor-Schema-Example.md`
- ✅ `Anchor-Schema-Extreme-Example.md` — `Core-Deep-Dive/Body-Base/Schema/Anchor-Schema-Extreme-Example.md`

---

### BATCH E — Agent-Mechanism + PFC System (~28 files)

**Agent-Mechanism (11 files)**
- ✅ `Agent-Mechanism.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Agent-Mechanism.md`
- ✅ `Self-Pattern-Modeling.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Self-Pattern-Modeling.md`
- ✅ `By-Product-Gap-Resonance.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/By-Product-Gap-Resonance.md`
- ✅ `Entity-Access.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Entity-Access.md`
- ✅ `Entity-Access-Excess.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Entity-Access-Excess.md`
- ✅ `Entity-Access-Calibration.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Entity-Access-Calibration.md`
- ✅ `Bond-Architecture.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Bond-Architecture.md`
- ✅ `Resonance-Sustainability.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Resonance-Sustainability.md`
- ✅ `By-Product-Scale.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/By-Product-Scale.md`
- ✅ `Resonance-Per-Entity.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Resonance-Per-Entity.md`
- ✅ `Entity-Compiled.md` — `Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/Entity-Compiled.md`

**PFC System (17 files)**
- ✅ `PFC-Function.md` — `Core-Deep-Dive/PFC/PFC-Function.md`
- ✅ `PFC-Hardware.md` — `Core-Deep-Dive/PFC/PFC-Hardware.md`
- ✅ `PFC-Operations.md` — `Core-Deep-Dive/PFC/PFC-Operations.md`
- ✅ `PFC-Configuration.md` — `Core-Deep-Dive/PFC/PFC-Configuration.md`
- ✅ `PFC-Development.md` — `Core-Deep-Dive/PFC/PFC-Development.md`
- ✅ `PFC-Hold-Dimensions.md` — `Core-Deep-Dive/PFC/PFC-Hold-Dimensions.md`
- ✅ `PFC-Label.md` — `Core-Deep-Dive/PFC/PFC-Label.md`
- ✅ `Simulation-Engine.md` — `Core-Deep-Dive/PFC/Simulation-Engine.md`
- ✅ `Attention-Spectrum.md` — `Core-Deep-Dive/PFC/Attention-Spectrum.md`
- ✅ `Logic-Feeling.md` — `Core-Deep-Dive/PFC/Logic-Feeling.md`
- ✅ `Logic-Feeling-Balance.md` — `Core-Deep-Dive/PFC/Logic-Feeling-Balance.md`
- ✅ `Logic-Feeling-Failure-Examples.md` — `Core-Deep-Dive/PFC/Logic-Feeling-Failure-Examples.md`
- ✅ `Logic-Planning.md` — `Core-Deep-Dive/PFC/Logic-Planning.md`
- ✅ `Imagination.md` — `Core-Deep-Dive/PFC/Imagination/Imagination.md`
- ✅ `Imagine-Final.md` — `Core-Deep-Dive/PFC/Imagination/Imagine-Final.md`
- ✅ `Imagine-Final-Evaluation.md` — `Core-Deep-Dive/PFC/Imagination/Imagine-Final-Evaluation.md`
- ✅ `Somatic-Articulation-Loop.md` — `Core-Deep-Dive/PFC/Imagination/Somatic-Articulation-Loop.md`

---

### BATCH F — Chunk Drills (~23 files)
*Lower priority — supporting material for deep readers*

**Child-Chunk-Development Foundation (2 files)**
- ✅ `01-PFC-Hardware-Reframe.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Foundation/01-PFC-Hardware-Reframe.md`
- ✅ `02-Womb-to-Birth-Baseline.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Foundation/02-Womb-to-Birth-Baseline.md`

**Child-Chunk-Development Modality Arcs (7 files)**
- ✅ `03-Visual-System-Arc.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/03-Visual-System-Arc.md`
- ✅ `04-Auditory-System-Arc.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/04-Auditory-System-Arc.md`
- ✅ `05-Motor-Output-Arc.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/05-Motor-Output-Arc.md`
- ✅ `06a-Interoceptive-Bladder-Keystone.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/06a-Interoceptive-Bladder-Keystone.md`
- ✅ `06b-Interoceptive-Other-States.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/06b-Interoceptive-Other-States.md`
- ✅ `07-Social-Recognition-Arc.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/07-Social-Recognition-Arc.md`
- ✅ `08-Verbal-Production-Arc.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Child-Chunk-Development/Modality-Arcs/08-Verbal-Production-Arc.md`

**Chunk-External-Development (2 files)**
- ✅ `00-External-Mechanism.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/00-External-Mechanism.md`
- ✅ `02-Cross-Network-Transfer.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/02-Cross-Network-Transfer.md`

**Language-Structure-Analysis (5 files)**
- ✅ `01-Natural-Language-Architecture.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/Language-Structure-Analysis/01-Natural-Language-Architecture.md`
- ✅ `02-Mathematical-Language-Architecture.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/Language-Structure-Analysis/02-Mathematical-Language-Architecture.md`
- ✅ `03-Musical-Notation-Architecture.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/Language-Structure-Analysis/03-Musical-Notation-Architecture.md`
- ✅ `04-Visual-Diagram-Architecture.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/Language-Structure-Analysis/04-Visual-Diagram-Architecture.md`
- ✅ `05-Programming-Language-Architecture.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-External-Development/Language-Structure-Analysis/05-Programming-Language-Architecture.md`

**Chunk-Internal-Processing (6 files)**
- ✅ `01b-Chunk-Activation-Dynamics.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/01b-Chunk-Activation-Dynamics.md`
- ✅ `01c-Chunk-Discovery-Lifecycle.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/01c-Chunk-Discovery-Lifecycle.md`
- ✅ `01-Chunk-Connection-Logical.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/01-Chunk-Connection-Logical.md`
- ✅ `02-Feeling-Intuition-Gradient.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/02-Feeling-Intuition-Gradient.md`
- ✅ `03-Chain-Anchor-Decay.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/03-Chain-Anchor-Decay.md`
- ✅ `04-Right-Wrong-Vague.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/Chunk-Internal-Processing/04-Right-Wrong-Vague.md`

**Other Chunk Drill**
- ✅ `09-Learning-Cycle.md` — `Core-Deep-Dive/Body-Base/Chunk/Drill-Chunk/09-Learning-Cycle.md`

---

### BATCH G — Collective + Domain Theory (~12 files)

**Collective (6 files)**
- ✅ `Collective.md` — `Core-Deep-Dive/Collective/Collective.md`
- ✅ `Collective-Body.md` — `Core-Deep-Dive/Collective/Collective-Body.md`
- ✅ `Collective-Arc-Dynamics.md` — `Core-Deep-Dive/Collective/Collective-Arc-Dynamics.md`
- ✅ `Collective-Purpose.md` — `Core-Deep-Dive/Collective/Collective-Purpose.md`
- ✅ `Compliance-Floor.md` — `Core-Deep-Dive/Collective/Compliance-Floor.md`
- ✅ `Coordination-Node.md` — `Core-Deep-Dive/Collective/Coordination-Node.md`

**Domain Theory (6 files)**
- ✅ `Domain.md` — `Core-Deep-Dive/Domain/Domain.md`
- ✅ `Domain-Mapping-Drive.md` — `Core-Deep-Dive/Domain/Domain-Mapping-Drive.md`
- ✅ `Knowledge-Flow.md` — `Core-Deep-Dive/Domain/Knowledge-Flow.md`
- ✅ `Discovery-vs-Expansion.md` — `Core-Deep-Dive/Domain/Discovery-vs-Expansion.md`
- ✅ `Conflict-Dynamics.md` — `Core-Deep-Dive/Domain/Conflict-Dynamics.md`
- ✅ `Drill-Emergent-Pattern.md` — `Core-Deep-Dive/Domain/Drill-Emergent-Pattern.md`

---

### BATCH H — Melody Lens (~18 files)

**Core Mechanism (4 files)**
- ✅ `Global-Melody.md` — `Core-Deep-Dive/Body-Base/Melody Lens/Global-Melody.md`
- ✅ `Melody-Arc.md` — `Core-Deep-Dive/Body-Base/Melody Lens/Melody-Arc.md`
- ✅ `Personal-Melody.md` — `Core-Deep-Dive/Body-Base/Melody Lens/Personal-Melody.md`
- ✅ `Personal-Melody-Example.md` — `Core-Deep-Dive/Body-Base/Melody Lens/Personal-Melody-Example.md`

**Melody-Technology Analysis (3 files)**
- ✅ `Idol-Phenomenon.md` — `Research/Melody-Technology/Idol-Phenomenon.md`
- ✅ `Religion.md` — `Research/Melody-Technology/Religion.md`
- ✅ `Melody-Technology-Overview.md` — `Research/Melody-Technology/Melody-Technology-Overview.md`

**Sound-Brain Drill Series (11 files)**
- ✅ `00-Overview.md` — `Research/Drill-Sound-Brain/00-Overview.md`
- ✅ `01-Sound-Brain-Neuroscience.md` — `Research/Drill-Sound-Brain/01-Sound-Brain-Neuroscience.md`
- ✅ `02-Sound-Background-Pattern.md` — `Research/Drill-Sound-Brain/02-Sound-Background-Pattern.md`
- ✅ `03-Sound-Reward-Pipeline.md` — `Research/Drill-Sound-Brain/03-Sound-Reward-Pipeline.md`
- ✅ `04-Sound-Social-Resonance.md` — `Research/Drill-Sound-Brain/04-Sound-Social-Resonance.md`
- ✅ `05-Multi-Modal-Compound.md` — `Research/Drill-Sound-Brain/05-Multi-Modal-Compound.md`
- ✅ `06-Music-Architecture-Prediction.md` — `Research/Drill-Sound-Brain/06-Music-Architecture-Prediction.md`
- ✅ `07-Music-Entrainment-Reward-Dynamics.md` — `Research/Drill-Sound-Brain/07-Music-Entrainment-Reward-Dynamics.md`
- ✅ `08-Musical-Elements-Brain-Interface.md` — `Research/Drill-Sound-Brain/08-Musical-Elements-Brain-Interface.md`
- ✅ `09-Verification-Research.md` — `Research/Drill-Sound-Brain/09-Verification-Research.md`
- ✅ `10-Synthesis.md` — `Research/Drill-Sound-Brain/10-Synthesis.md`

---

### BATCH I — Child Development + Education Applications (~19 files)

**Child Development (4 files)**
- ✅ `Child-Development-Mechanism.md` — `Research/Human-Learning/Child-Development/Child-Development-Mechanism.md`
- ✅ `Mother-Optimization.md` — `Research/Human-Learning/Child-Development/Mother-Optimization.md`
- ✅ `Natural-Development.md` — `Research/Human-Learning/Child-Development/Natural-Development.md`
- ✅ `Skill-Introduction.md` — `Research/Human-Learning/Child-Development/Skill-Introduction.md`

**Education Applications (15 files)**
- ✅ `00_Overview.md` — `Applications/Education-System/00_Overview.md`
- ✅ `Education-System.md` — `Applications/Education-System/Education-System.md`
- ✅ `Curriculum-Framework.md` — `Applications/Education-System/Curriculum-Framework.md`
- ✅ `Hardware-Calibration.md` — `Applications/Education-System/Hardware-Calibration.md`
- ✅ `Era-Analysis-2025.md` — `Applications/Education-System/Era-Analysis-2025.md`
- ✅ `VN-Cultural-Factors.md` — `Applications/Education-System/Country/VN/VN-Cultural-Factors.md`
- ✅ `VN-Education-Status.md` — `Applications/Education-System/Country/VN/VN-Education-Status.md`
- ✅ `VN-Recommendations.md` — `Applications/Education-System/Country/VN/VN-Recommendations.md`
- ✅ `Education-Mechanism.md` — `Research/Human-Learning/Education-Mechanism/Education-Mechanism.md`
- ✅ `Compile-Type-Learning.md` — `Research/Human-Learning/Education-Mechanism/Compile-Type-Learning.md`
- ✅ `Expansion-Saturation-Crisis.md` — `Research/Human-Learning/Education-Mechanism/Expansion-Saturation-Crisis.md`
- ✅ `Connection-Education.md` — `Research/Human-Learning/Education-Mechanism/Connection-Education.md`
- ✅ `Education-Arms-Race.md` — `Research/Human-Learning/Education-Mechanism/Observation/Education-Arms-Race.md`
- ✅ `Money-Education.md` — `Research/Human-Learning/Education-Mechanism/Observation/Money-Education.md`
- ✅ `Domain-Knowledge-Map.md` — `Research/Human-Learning/Education-Mechanism/Domain-Knowledge-Map.md`

---

### BATCH J — Health Conditions (~12 files)

- ✅ `OCD-Analysis.md` — `Research/Health-Conditions/OCD-Analysis.md`
- ✅ `PTSD-Analysis.md` — `Research/Health-Conditions/PTSD-Analysis.md`
- ✅ `Addiction-Analysis.md` — `Research/Health-Conditions/Hijack/Addiction-Analysis.md`
- ✅ `Alcohol-Vietnam-Generational.md` — `Research/Health-Conditions/Hijack/Alcohol-Vietnam-Generational.md`
- ✅ `Alcohol-Brain-Mechanism.md` — `Research/Health-Conditions/Hijack/Alcohol-Brain-Mechanism.md`
- ✅ `Nicotine-Brain-Mechanism.md` — `Research/Health-Conditions/Hijack/Nicotine-Brain-Mechanism.md`
- ✅ `Alzheimer-Analysis.md` — `Research/Health-Conditions/Neurodegeneration/Alzheimer-Analysis.md`
- ✅ `Parkinson-Analysis.md` — `Research/Health-Conditions/Neurodegeneration/Parkinson-Analysis.md`
- ✅ `ADHD-Attention-Optimization.md` — `Research/Health-Conditions/Neurodiversity/ADHD-Attention-Optimization.md`
- ✅ `ADHD-Trade-Off.md` — `Research/Health-Conditions/Neurodiversity/ADHD-Trade-Off.md`
- ✅ `ADHD-Observation.md` — `Research/Health-Conditions/Neurodiversity/ADHD-Observation.md`
- ✅ `Autism-Observation.md` — `Research/Health-Conditions/Neurodiversity/Autism-Observation.md`

---

### BATCH K — Global & Economic Analysis (~32 files)

**Love + Money (3 files)**
- ✅ `Love-Romantic.md` — `Research/Love-Romantic.md`
- ✅ `Love-Unified.md` — `Research/Love-Unified.md`
- ✅ `Money-Analysis.md` — `Research/Money-Analysis.md`

**Global Social Analysis (7 files)**
- ✅ `AI-Self-Model.md` — `Research/Global/AI-Self-Model.md`
- ✅ `Human-AI-Future.md` — `Research/Global/Human-AI-Future.md`
- ✅ `Innovation-Geography.md` — `Research/Global/Innovation-Geography.md`
- ✅ `Social-Calibration.md` — `Research/Global/Social-Calibration.md`
- ✅ `Uncanny-Valley.md` — `Research/Global/Uncanny-Valley.md`
- ✅ `Self-Created-Threat.md` — `Research/Self-Created-Threat.md`
- ✅ `Sensitivity-Classification.md` — `Research/Mismatch-Patterns/Sensitivity-Classification.md`

**Birth Rate Decline Series (9 files)**
- ✅ `00_Overview.md` — `Research/Global/Birth-Rate-Decline/00_Overview.md`
- ✅ `01_South-Korea_Analysis.md` — `Research/Global/Birth-Rate-Decline/01_South-Korea_Analysis.md`
- ✅ `03_China_Analysis.md` — `Research/Global/Birth-Rate-Decline/03_China_Analysis.md`
- ✅ `04_France_Analysis.md` — `Research/Global/Birth-Rate-Decline/04_France_Analysis.md`
- ✅ `05_Finland_Analysis.md` — `Research/Global/Birth-Rate-Decline/05_Finland_Analysis.md`
- ✅ `06_Israel_Analysis.md` — `Research/Global/Birth-Rate-Decline/06_Israel_Analysis.md`
- ✅ `09_Vietnam_Analysis.md` — `Research/Global/Birth-Rate-Decline/09_Vietnam_Analysis.md`
- ✅ `09_Vietnam_Solution.md` — `Research/Global/Birth-Rate-Decline/09_Vietnam_Solution.md`
- ✅ `100_Solutions.md` — `Research/Global/Birth-Rate-Decline/100_Solutions.md`

**Quote Analysis (8 files)**
- ✅ `Work-Adversity-Fear-Cluster.md` — `Research/Quote-Analysis/Work-Adversity-Fear-Cluster.md`
- ✅ `Work-Chunk-Dependent-Visibility-Cluster.md` — `Research/Quote-Analysis/Work-Chunk-Dependent-Visibility-Cluster.md`
- ✅ `Work-Comparison-Thief-Of-Joy.md` — `Research/Quote-Analysis/Work-Comparison-Thief-Of-Joy.md`
- ✅ `Work-Goal-And-Why.md` — `Research/Quote-Analysis/Work-Goal-And-Why.md`
- ✅ `Work-Journey-Destination-Cluster.md` — `Research/Quote-Analysis/Work-Journey-Destination-Cluster.md`
- ✅ `Work-Move-Fast-Break-Things.md` — `Research/Quote-Analysis/Work-Move-Fast-Break-Things.md`
- ✅ `Work-Stay-Hungry-Stay-Foolish.md` — `Research/Quote-Analysis/Work-Stay-Hungry-Stay-Foolish.md`
- ✅ `Work-Think-Act-Become-Cluster.md` — `Research/Quote-Analysis/Work-Think-Act-Become-Cluster.md`

**Research Misc (5 files)**
- ✅ `Climate-Cognition.md` — `Research/Climate-Cognition.md`
- ✅ `Fidgeting-Analysis.md` — `Research/Fidgeting-Analysis.md`
- ✅ `Relativity-Explained.md` — `Research/Relativity-Explained.md`
- ✅ `Collective-Schema-Pressure.md` — `Research/Mismatch-Patterns/Collective-Schema-Pressure.md`
- 🚫 `Body-Listening-Journey.md` — `Research/Drill-Reward-Feeling/Body-Listening-Journey.md` *(not present in global-index.json — skipped)*

---

### BATCH L — Meta-Epistemology + Reference Tools (~5 files)

- ✅ `Meta-Impact.md` — `Research/Meta-Impact/Meta-Impact.md`
- ✅ `Creator-Lens.md` — `Research/Meta-Impact/Creator-Lens.md`
- ✅ `Epistemological-Position.md` — `Research/Meta-Impact/Epistemological-Position.md`
- ✅ `00-Goals.md` — `Research/Neuro-Measurement/00-Goals.md`
- ✅ `01-Implementation-Plan.md` — `Research/Neuro-Measurement/01-Implementation-Plan.md`

---

## §3 — Session Notes

### Edge Cases
- **Drill files:** shorter fullDescription (3-6 lines), focus on what the drill explores
- **Files ending in -Draft:** still full files, treat same as regular files
- **Language-Structure-Analysis series:** reference files, medium description
- **Quote-Analysis files:** each is an analysis of 1 famous quote through framework lens
- **Birth-Rate-Decline series:** country-by-country analysis applying framework to demographic data
- **Files in `Melody Lens/` folder:** note the space in folder name

### Session Log
| Date | Batch | Files done | Notes |
|------|-------|-----------|-------|
| 2026-05-31 | — | 0/234 | Plan created, HTML updated |
| 2026-05-31 | A | 32/234 | Core Foundation + Observation Parameters |
| 2026-05-31 | B | 49/234 | Body-Feedback System (12 mechanism + 5 drill) |
| 2026-05-31 | C | 71/234 | Feeling System + Clarification (22 files) |
| 2026-05-31 | D | 86/234 | Chunk System + Schema-Anchor (15 files) |
| 2026-05-31 | E | 114/234 | Agent-Mechanism + PFC System (28 files) |
| 2026-05-31 | F | 137/234 | Chunk Drills (23 files) |
| 2026-05-31 | G | 149/234 | Collective + Domain Theory (12 files) |
| 2026-05-31 | H | 167/234 | Melody Lens + Sound-Brain Drill (18 files) |
| 2026-05-31 | I | 186/234 | Child Development + Education Applications (19 files) |
| 2026-05-31 | J | 198/234 | Health Conditions (12 files) |
| 2026-05-31 | K | 233/234 | Global Analysis + Quote Analysis + Research Misc (31 files; 1 skipped) |
| 2026-05-31 | L | 233/234 | Meta-Epistemology + Neuro-Measurement (5 files) — COMPLETE |

---

## Cross-references
```
plan-descriptions.md (this file)
  ← plan.md (overall HTML viewer plan)
  ← global-index.json (target data file)
  → index.html (HTML viewer — reads global-index.json)
```
