# English Translation — Terminology Glossary

> **Status**: LIVING DOCUMENT — grows with each translation session
> **Created**: 2026-05-26
> **Sources**: Body-Feedback-Label.md v2.1, PFC-Label.md v1.0, Core-Software.md v2.2
> **Purpose**: Source of truth for English terminology across ALL translated files
> **Rule**: When translating, ALWAYS check this file first. Add new terms after each session.

---

## §0 — How to Use This Glossary

**When translating**: Look up every framework term before writing. Use EXACT phrasing.

**When a term is missing**: Add it here after deciding the English phrasing.

**Format per entry**:
- **Term** — the canonical English form (use this in all translations)
- Vietnamese context — how the term appears in Vietnamese text
- Definition — concise English definition
- Source — where the term is formally defined

**Already-English terms**: Most framework concepts already use English names.
These entries confirm the canonical form and provide definition context.

---

## §1 — Foundation Terms

> Source: Body-Feedback-Label.md §2

| Term | Vietnamese context | Definition | Source |
|---|---|---|---|
| **body-base** | "cơ thể-nền", "body-base system" | The entire system: hardware + compiled patterns + social hardware. Compilable Architecture. | Body-Base.md |
| **body-need** | "trạng thái CẦN" | Aggregate state of NEED at any moment. Sum of all gaps + hardware signals. Always exists (never = 0). Exists before PFC awareness. | BFL §2B |
| **hardware body-need** | "body-need từ hardware" | Source ①: Sensory-Driven. Homeostatic + nociceptive + hormonal. No compiled chunks needed. (hunger, thirst, pain, cold) | BFL §2B |
| **pattern body-need** | "body-need từ chunk dynamics" | Source ②: Chunk Dynamics/Pattern. Gap/Miss/Shift + Compound. Requires compiled chunks. (missing a friend, career gap, identity) | BFL §2B |
| **gap** | "gap", "lỗ hổng" | Specific chunk that SHOULD exist but is MISSING. Network predicts chunk C → C absent. Component of body-need. | BFL §2C |
| **gap direction** | "hướng gap", "gap direction" | Direction the gap points = f(surrounding chunks). Only fill matching this direction → reward. Per-person. "What you don't know creates no gap." | Gap-Direction.md |
| **drive** | "lực đẩy hành vi" | Behavioral push FROM body-need. Output: action to fill gap. | BFL §2D |
| **drive direction** | "hướng hành vi" | Gap direction expressed as behavior. Approach (toward) or avoidance (away from). | BFL §2D |
| **body-feedback** | "tín hiệu từ body" | ALL signals from body about current state. Umbrella term. Runs 24/7. 95% unconscious. Includes reward, dissonance, prediction-delta, baseline, valence tags. ≠ feeling. | BFL §2E |

**Key distinctions:**
- body-need = STATE (what body needs) vs body-feedback = SIGNAL (what body reports)
- gap = specific missing chunk vs body-need = aggregate of all gaps + hardware signals
- "What you don't know creates no gap" (no surrounding chunks → no gap direction → no gap)

---

## §2 — Reward Labels

> Source: Body-Feedback-Label.md §3

| Tier | Term | Vietnamese context | Definition |
|---|---|---|---|
| T1 | **positive body-feedback** | "body-feedback dương" | Most general. Body responds positively. |
| T2 | **body-base reward** | "body-base reward" | Body confirms: chunk matches body-need. Covers BOTH Evaluative + Direct-State. |
| T2 | **reward** | "reward" | Shorthand for body-base reward. Use when context is clear. |
| T2 | **Evaluative Reward** | "Evaluative Reward" | Opioid-based. Needs Body-Feedback-Precondition preconditions. Rich chunk library. |
| T2 | **Direct-State Reward** | "Direct-State Reward" | Non-opioid. Hardware-based. Less habituation. (touch, exercise, warmth) |
| T3 | **μ-opioid confirm** | "opioid confirm" | Evaluative. Hedonic hotspot pathway. NAcc/VP. |
| T3 | **CT afferent reward** | "CT afferent reward" | Direct-State. Touch comfort. ~1-10cm/s optimal. |
| T3 | **endocannabinoid reward** | "endocannabinoid reward" | Direct-State. Exercise/runner's high. CB1. |
| T3 | **E₀ / E₁ / E₂ / E₃** | "E₀→E₃" | Evaluative complexity gradient. E₀=hardware → E₃=expert evaluation. |
| T3 | **Profile ①-⑤** | "5 Profiles" | 5 "flavors" of reward: Sensory / Coherence / Social / Relief / Preview. |

**Key distinction**: prediction-delta ("doorbell") ≠ body-base reward ("gift behind the door")

---

## §3 — Dissonance Labels

> Source: Body-Feedback-Label.md §4

| Tier | Term | Vietnamese context | Definition |
|---|---|---|---|
| T1 | **negative body-feedback** | "body-feedback âm" | Most general. Body responds negatively. |
| T2 | **dissonance** | "dissonance", "không khớp" | Body detects mismatch (schema ≠ reality). Drives resolution. |
| T2 | **threat** | "threat", "đe dọa" | Body predicts harm (anticipated damage). Drives avoidance. |
| T2 | **recalibration dissonance** | "recalibration dissonance" | Neurons adjusting pattern. Transient. Self-resolves when adaptation completes. |
| T2 | **Evaluative Dissonance** | "Evaluative Dissonance" | Compiled, conditional. dACC + anterior insula. PFC can modulate. Develops with age. |
| T2 | **Direct-State Dissonance** | "Direct-State Dissonance" | Hardware, from birth. Nociceptors, thermoreceptors. PFC minimal. Numbness-proof. |
| T3 | **chunk-miss** | "chunk-miss" | Expected X, got <X. SNC mechanism. (Crespi 1942) |
| T3 | **chunk-shift** | "chunk-shift" | Same chunks, different valence. Context changed → re-evaluate. |
| T3 | **chunk-gap** | "chunk-gap" | Gap (§1) detected AS dissonance signal. Body fires signal because chunk missing. |
| T3 | **SNC** | "SNC" | Successive Negative Contrast. Downshift from high baseline → overreaction. |
| T3 | **nociception** | "nociception" | Tissue damage signal. Hardware. A-delta + C fibers. |
| T3 | **cortisol Role ①-⑤** | "5 cortisol Roles" | ① Compile Direction ② Holding ③ Threat-sustained ④ Inertia ⑤ Silent |

---

## §4 — Detection Layer

> Source: Body-Feedback-Label.md §5

| Term | Definition |
|---|---|
| **prediction-delta** | Brain detects deviation from current prediction. Dopamine alert. NOT yet good/bad — only "different from baseline." Step 2 in 7-step mechanism. |
| **DRD4 filter** | Receptor threshold for prediction-delta. 4R=sensitive (small delta detected). 7R=coarse (only large delta). Per-person. |
| **PFC spotlight** | Step 4: PFC boosts target region. NE + ACh amplification. |

---

## §5 — Baseline + Valence

> Source: Body-Feedback-Label.md §6-§7

| Term | Definition |
|---|---|
| **body-feedback baseline** | Pattern repeated → brain habituated → no prediction-delta → no alert. "New normal." |
| **habituated** | Same meaning, shorthand. Habituated ≠ value = 0. Losing habituated things → SNC → dissonance. |
| **approach tag** | Positive valence compiled onto chunk. "This domain → body-base reward." Drive TOWARD. |
| **avoidance tag** | Negative valence compiled onto chunk. "This domain → dissonance." Drive AWAY. |
| **Entity-Compiled** | Entity compiled into body-base at STRUCTURAL level. Entity's state = MY state. Per-channel valence profile. |
| **Entity-Compiled positive-dominant** | Majority channels positive. Presence = approach + reward. Loss = grief (body-base amputation). |
| **Entity-Compiled negative-dominant** | Majority channels negative. Presence = threat/dissonance. Loss = relief. |
| **Entity-Compiled mixed** | Significant BOTH positive AND negative channels simultaneously. MOST COMMON. Behavior oscillates. |

**Key distinction**: approach/avoidance tags = COMPILED (accumulated) vs reward/dissonance = MOMENTARY (happening now)

---

## §6 — Processing Spectrum

> Source: Body-Feedback-Label.md §8, PFC-Label.md §3

| Term | Vietnamese context | Definition |
|---|---|---|
| **Compiled processing** | "xử lý đã compile" | Automatic. Body-direct. Cost ≈ 0. Hebbian reinforced. "Feels like knowing." |
| **Fresh processing** | "xử lý Fresh" | PFC-mediated. Deliberate. Cost > 0. Each time = new effort. "Have to think it through." |
| **Semi-compiled** | "semi-compiled" | Mixed: partly compiled, partly fresh. |
| **Fresh → Compiled (learning)** | "học → compile" | Repetition + verification → Hebbian strengthen → automatic. = "Logic → feeling" (for that person). |
| **Compiled → Fresh (disruption)** | "bị phá → phải suy nghĩ lại" | New context, error detected → must re-evaluate deliberately. = "Feeling → logic." |

**Critical rule**: "Compiled/Fresh" = MECHANISM labels (use in analysis). "Logic/Feeling" = OBSERVER labels (use for general audience).

---

## §7 — PFC System

> Source: PFC-Label.md §2-§9

### PFC Roles

| Term | Definition |
|---|---|
| **PFC = Observer** | PFC observes body-feedback output. Reactive, NOT generative. ~5% of decisions. |
| **PFC = Lawyer** | PFC creates narrative FOR body-base. Post-hoc justification. Confabulation. NOT neutral judge. |
| **PFC = Director** (Orchestrator) | PFC biases spreading activation. Directs, does NOT compute directly. |
| **PFC = Universal Resource** | PFC budget = FINITE, SHARED for everything: learning, Self-Pattern-Modeling, decisions, suppress. |
| **PFC = Quality Controller** | Dual Check: body = quality controller, domain = final arbiter. PFC verifies body output against domain reality. |

### PFC Operations

| Term | Definition |
|---|---|
| **HOLD** (= PFC Amplify) | Amplify new/weak pattern. CAN compile → sustainable. Cost: ① PFC draft. Region: dlPFC, FEF. |
| **SUPPRESS** (= PFC Inhibit) | Block already-compiled pattern. CANNOT compile "not" → unsustainable. Cost: ② Suppress. Region: rIFG, vlPFC. |

### PFC Costs

| Term | Definition |
|---|---|
| **① PFC draft cost** | Metabolic cost from HOLD. f(chain_length × novelty). DECREASES as it compiles → ≈ 0. |
| **② Suppress cost** | Efference mismatch from SUPPRESS. f(intensity × duration). DOES NOT decrease (pattern still fires). = "Not being me." |
| **③ Uncertainty cost** | Multiple options, none compiled → hold open → cortisol. f(options × time × stakes). Decreases when committing. |
| **PFC budget** | Total PFC resource. FINITE. SHARED for all activities. Depleted by fatigue, stress, sleep deprivation, chronic suppress. |

### Compiled Quality

| Term | Definition |
|---|---|
| **Genuine-compiled** | Body reward confirmed → compiled. Approach tag. Self-Pattern-Modeling EXPANSIVE (rich body data). |
| **Schema-compiled** | PFC / obligation / social compliance → compiled. Neutral tag. Self-Pattern-Modeling LIMITED (narrow, rule-based). |
| **Threat-compiled** | Forced / threat → compiled. Avoidance tag. Self-Pattern-Modeling BIASED (fear-based). |

### PFC Regions

| Term | Framework mapping |
|---|---|
| **dlPFC** (dorsolateral) | Working memory, planning, HOLD operation hub. ~4±1 dimensions. |
| **vlPFC** (ventrolateral) | Response inhibition, SUPPRESS operation hub. |
| **vmPFC** (ventromedial) | Emotion regulation, somatic bridge, controllability (suppress DRN). |
| **OFC** (orbitofrontal) | Value computation, Evaluative Reward gateway, punishment learning. |
| **ACC** (anterior cingulate) | Conflict detection, ③ uncertainty cost, error monitoring. |
| **mPFC** (medial) | Self-referential, Self-Pattern-Modeling hub, Entity-Access gradient migration. |
| **FEF** (frontal eye fields) | Attention direction, part of HOLD network. |
| **rIFG** (right inferior frontal gyrus) | Motor inhibition, SUPPRESS hub. |

### PFC Hardware

| Term | Definition |
|---|---|
| **COMT** | Enzyme clearing prefrontal dopamine. Val/Val = fast clear → improviser. Met/Met = slow clear → specialist. |
| **DRD4** | Dopamine receptor sensitivity. 4R = sensitive. 7R = thrill-seeker. Filters prediction-delta threshold. |

### Simulation-Engine

| Term | Definition |
|---|---|
| **Simulation-Engine** | 1 general-purpose engine (DMN + mPFC + insula + hippocampus). NOT N separate modules. |
| **3 Components** | Interoception (body readout) × Constructive Simulation (CPU) × Self/Other Model (target). |
| **3 Axes** | Target (self/other) × Time (past/present/future) × Operation (read/simulate/evaluate). |

---

## §8 — Inter-Body Interaction

> Source: Body-Feedback-Label.md §9

| Term | Definition |
|---|---|
| **by-product match** | B fills B's own gap → output = by-product → matches A's gap direction → A receives reward. Foundation of inter-body feeding. |
| **anti-match** | By-product CONFLICTS gap direction. Worse than no-match = active friction. |
| **mutual match** (= Resonance) | Both receive reward from interaction. A matches B AND B matches A. |
| **one-way match** | Only one side receives reward. (parasocial, asymmetric service) |
| **Hardware-Stream** | Hardware/unidirectional by-product match. Reward from EXISTENCE/attribute. No engagement needed. HABITUATES. |
| **Modeling-Stream** | Self-Pattern-Modeling compiled mutual (bidirectional). Both engage Self-Pattern-Modeling → feedback loop. ANTI-HABITUATION. |
| **Proto-Modeling-Stream** | Primitive Modeling-Stream without full Self-Pattern-Modeling. (mother-infant contingent response, human-pet) |

---

## §9 — Observation Parameters

> These are NAMES for observable patterns, NOT components or modules.
> Analogy: "temperature" names molecular vibration — no particle called "temperature."

| Term | Vietnamese | Definition |
|---|---|---|
| **Novelty** | "Tò mò", "Novelty" | Pattern: VTA detects positive prediction-delta + chunk-gap dynamics. |
| **Threat** | "Đe dọa", "Threat" | Pattern: dissonance from predicted harm. 5 levels × 3 axes × 3 origins. |
| **Boredom** | "Chán" | Pattern: unified formula (Dissonance + dim Imagine-Final). 6 sources. |
| **Drive** | "Lực đẩy" | Pattern: energy + direction emergent from chunk dynamics. |
| **Empathy** | "Đồng cảm" | Pattern: Self-Pattern-Modeling Compiled + positive observation output. |
| **Connection** | "Kết nối" | Pattern: 3 Generative Primitives, 8 pathways. |
| **Status** | "Vị thế" | Pattern: Resource Access Map. Evolutionary grounded. |
| **Protect** | "Bảo vệ" | Pattern: loss aversion + ownership chunk dynamics. f(replaceability × attachment). |
| **Meaning** | "Ý nghĩa" | Pattern: stable life-level Anchor-Schema. 5 types (GOAL/STATE/IDENTITY/FAITH/ROLE). |
| **Autonomy** | "Tự chủ" | Pattern: f(motor chunks × controllability × meta-chunk "I do = better"). |
| **Gratitude** | "Biết ơn" | Pattern: Tier 5 (highest). 9 simultaneous prerequisites. Agent-entity only. |
| **Obligation** | "Nghĩa vụ" | Pattern: compiled prediction of cost to MAINTAIN access to agent-as-tool. |

---

## §10 — Agent-Mechanism System

| Term | Definition |
|---|---|
| **Agent-Mechanism** | FUNCTION on chunks (NOT entity). Integration hub for inter-body mechanisms. |
| **Self-Pattern-Modeling** | APPLICATION-1 on Simulation-Engine. 1 mechanism × 3 dimensions (Processing Level × Valence × Output Intensity). |
| **Entity-Access** | Gradient model: brain builds predictive access-relationship. Mức 0 (Tool) → Mức 5 (Excess). |
| **Entity-Compiled** | Brain compiles agent into body-base at STRUCTURAL level. Hub-and-spoke neural architecture. Formation: 40→200h. Dunbar ~150. |
| **By-Product-Gap-Resonance** | Core = by-product match at OUTPUT. 4 simultaneous conditions. Gap clone IMPOSSIBLE. |
| **Bond-Architecture** | Entity-Compiled = 1 mechanism × 4 bond configurations (parent/friend/romantic/professional). |
| **Resonance-Sustainability** | 4-Layer model. 3 conditions × 3 modalities. What predicts sustained vs decaying resonance. |
| **Resonance-Per-Entity** | Per-entity dynamics. Same mechanism, different dynamics per relationship type. |
| **By-Product-Scale** | 1 mechanism × 3 scales: Pair / Hub / Institutional. |
| **Hardware-Subsidy** | Hormone-based anti-habituation. Oxytocin (L1) → Serotonin (L2) → Trust infrastructure (L3). Spectrum: MAX → NONE. |
| **Resonance Decline** | 2 Forces + 1 Fuel: Compiled-Suppress (strongest, leverage point) + Reward-Habituated (Weber-Fechner) + Novelty threshold (prediction complete + Entity-Compiled saturated = 2 lenses). |
| **Entity-Access-Excess** | Excess territory on gradient (Mức 5). Entity = near-only gap source. Same circuits as drug addiction. |
| **Entity-Access-Calibration** | How entity-access self-regulates. 3-Layer Architecture. Exit Cost = Signal Weight. |

---

## §11 — Chunk System

| Term | Vietnamese context | Definition |
|---|---|---|
| **chunk** | "chunk" | Strength-weighted associative network compiled through experience. Brain searches, doesn't compute. |
| **proto-chunk** | "proto-chunk" | Weak chunk. Fires sometimes, partial pattern-match. |
| **compiled chunk** | "chunk đã compile" | Medium-strong. Fires reliably. Holdable in working memory. |
| **meta-chunk** | "meta-chunk" | Strong. Many sub-chunks merged → fire as 1 unit. Expert: [driving] = 1 meta-chunk. |
| **compile** | "compile" | Process of strengthening chunks through repetition, emotional peak, multi-modal input, sleep. |
| **3 Compile Types** | "3 loại Compile" | Experience (direct) / Expertise (domain repetition) / Trust (installed by others). |
| **Background-Pattern** | "Background-Pattern" | Accumulated chunk bias invisible to PFC. 2D: Depth × Density. |
| **Schema** | "Schema" | Observation label for named chunk-network pattern. NOT architecture component. |
| **Anchor-Schema** | "Anchor-Schema" | Sync point unconscious needs for system-wide synchronization. 4 sources fill. |

---

## §12 — Core Architecture

| Term | Definition |
|---|---|
| **Compilable Architecture** | Human system: general-purpose reward + compilation + social hardware. Flexible but 15-20yr compile time. |
| **Hardwired Architecture** | Insect/simple animal: specific stimulus → specific response. No compilation needed. No novelty detection. |
| **Cycle** | Core architecture: Domain → Body-Input → Unconscious → Feeling → PFC → Body-Output → Domain. Continuous. |
| **Dual Check** | Body = quality controller (~90%), Domain reality = final arbiter. |
| **Domain Reality** | External reality. Final arbiter. Cannot be permanently fooled. Timeline: seconds → years. |
| **Imagine-Final** | Constructive future simulation on Simulation-Engine. ≠ all body prediction — ONLY constructive simulation (chunk-based). |
| **Personal-Melody** | Metaphor: each person = 1 song = emergent state of entire chunk network running simultaneously. |
| **Modality** | 6 encoding channels: Visual / Auditory / Somatic / Motor / Emotional / Communication. |

---

## §13 — Confidence + Formatting

| Term | Usage |
|---|---|
| **🟢** | Research support — peer-reviewed evidence exists |
| **🟡** | Framework synthesis — logically derived from 🟢 evidence |
| **🔴** | Hypothesis — speculative, needs testing |
| **~X%** | Calibration anchor — direction + magnitude, NOT measurement |
| **§X.Y** | Section reference — universal, language-independent |

---

## §14 — Vietnamese Terms (Keep + Annotate)

Some Vietnamese terms have no clean English equivalent. Keep the Vietnamese (italicized) + English explanation.

| Vietnamese | English rendering | Context |
|---|---|---|
| *ân tình* | reciprocal emotional debt | Obligation type unique to Vietnamese/East Asian cultures |
| *nhậu* | social drinking ritual | Vietnamese collective drinking culture |
| *thuốc lào* | Vietnamese water pipe tobacco (*Nicotiana rustica*) | 3-9× nicotine of regular tobacco |
| *bốn không* | "four noes" | VN youth rejecting marriage/children/house/car |
| *hợp tính* | Pattern-Resonance Baseline (compatibility) | "Compatible chemistry" between people |
| *mặt lưng cái tủ* | "the back of the wardrobe" | Hidden quality — invisible unless you look, but craftsmanship matters |
| *chưa biết = không có gap* | "What you don't know creates no gap" | Core principle: no surrounding chunks → no gap direction → no gap |
| *cùng kiến trúc, khác chunks* | "same architecture, different chunks" | Development = same system, different accumulated content |

---

## §15 — Deprecated / Do Not Use

| Do NOT use | Use instead | Why |
|---|---|---|
| "PFC-Fresh" | "Fresh processing" | Redundant — Fresh already implies PFC-mediated |
| "draft" (standalone) | "PFC HOLD draft novel path" | Ambiguous — state? action? output? |
| "Logic vs Feeling" (in mechanism analysis) | "Compiled vs Fresh" | Logic/Feeling are observer labels, not mechanism |
| "pleasant/comfortable" (for mechanism) | "body-base reward" | pleasant = feeling label (PFC observation), not body-feedback |
| "stress" (for cortisol) | "cortisol as amplifier" | Cortisol ≠ stress. Cortisol = amplifier, direction + duration matter. |
| "mirror neurons" | "Self-Pattern-Modeling learned prediction" | Framework rejects dedicated mirror module |
| "willpower" | "PFC budget + HOLD/SUPPRESS operations" | "Willpower" conflates mechanism with morality |
| "dopamine = reward" | "dopamine = prediction-delta signal" | Dopamine = detection/salience, NOT reward |
| "prediction error = reward" | "prediction-delta + body-base check = reward" | PE alone insufficient — needs Body-Feedback-Precondition preconditions |

---

## §16 — Growth Log

| Date | Session | Terms added | Notes |
|---|---|---|---|
| 2026-05-26 | Initial | ~150 terms | Foundation extracted from BFL v2.1 + PFC-Label v1.0 |
| | | | |

---

> *This glossary is the SINGLE SOURCE OF TRUTH for English terminology.*
> *Every translation session: CHECK before writing. UPDATE after writing.*
> *Consistency across 226 files depends on this document.*
