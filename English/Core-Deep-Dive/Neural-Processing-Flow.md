---
title: Neural-Processing-Flow — Complete Flow from Sensor → Cortex → PFC → Output
version: 2.0
created: 2026-04-17 (N+5 session)
updated: 2026-05-17 (v2.0 — +Compilable Architecture framing, +Compiled/Fresh at physical level, +PFC=Lawyer strengthen, +5-Channel mapping, +L3 operator fix, +Inter-Body cross-refs)
previous: v1.0 → backup/Neural-Processing-Flow-v1.0-backup.md
status: v2.0
scope: HARDWARE FLOW + PROCESSING FLOW + Compilable Architecture connection
purpose: |
  Physical foundation — the physical pathway signals travel through the brain.
  v2.0: WHY this hardware (Compilable Architecture trade-off), Compiled/Fresh at physical level,
  PFC=Lawyer as structural function, 5-Channel Input Vector connection.
dependencies:
  - Inter-Body-Mechanism.md v1.0 — Compilable Architecture, 5-Channel, PFC=Lawyer
  - Feeling.md v3.0 — 7-layer, Compiled/Fresh×Layer mapping
  - Logic-Feeling.md v2.0 — Compiled/Fresh axis
  - Body-Feedback-Mechanism.md v2.0 — 2-source, Body-Need
  - Body-Input-Enumeration.md — full body input catalog
source_version: Vietnamese v2.0 (2026-05-17)
english_created: 2026-06-05
english_updated:
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Neural-Processing-Flow — Complete Flow from Sensor → Cortex → PFC → Output

> **This file answers:** When eyes see, ears hear, skin touches, heart beats — what PATH do signals take through the brain?
>
> **Why it matters:** Every other mechanism (chunk, feeling, logic, imagination, plan) RUNS ON this physical pathway.

---

## §0 — Position in the Framework

```
  ┌─────────────────────────────────────────────────────┐
  │ HARDWARE LAYER (this file)                          │
  │ = PHYSICAL PATHWAY: Sensors → Thalamus → Cortex    │
  │   → Binding → Chunks → PFC → Output → Feedback     │
  ├─────────────────────────────────────────────────────┤
  │ CONTENT LAYER (Schema/Chunk.md + Modality)          │
  │ = PATTERNS compiled on hardware                     │
  ├─────────────────────────────────────────────────────┤
  │ PROCESSING LAYER (Logic-Feeling.md v2.0)            │
  │ = Compiled/Fresh spectrum (not "2 modes")           │
  ├─────────────────────────────────────────────────────┤
  │ BEHAVIOR LAYER (Imagine-Final + Logic-Planning)     │
  │ = PLAN + EXECUTE + FEEDBACK                         │
  └─────────────────────────────────────────────────────┘

  ⭐ COMPILABLE ARCHITECTURE CONNECTION (Inter-Body-Mechanism.md §1):

  WHY this hardware exists:
    Evolution selected Compilable Architecture for humans:
      ① General-Purpose Reward — fires for ANY gap fill in the correct direction
      ② Compilation — repeat + verify → automatic (Hebbian LTP)
      ③ Social Hardware — oxytocin, μ-opioid, dACC reuse

    Trade-off of Compilable Architecture:
      → Adapts to ANY environment (general-purpose)
      → BUT: requires 15-20 years to compile (slow development)
      → Hardware below = ENABLES Compilable Architecture:
        Thalamus gate = general-purpose filter (not hardwired per stimulus)
        6-layer cortex = uniform fabric (compiles ANY pattern)
        PFC = general-purpose orchestrator (not stimulus-specific)
        Binding = flexible (binds ANY combination)
      → Hardwired Architecture (insect): hardwired stimulus→response (no PFC needed)
      → Compilable Architecture (human): general input → general processing → COMPILE

    Implication for this file:
      → §1-§4: HOW signals travel = hardware infrastructure
      → §5: HOW compilation happens = Compilable Architecture's KEY mechanism
      → §6: WHY PFC = orchestrator not computer = general-purpose design
      → §7-§9: WHY simulation + feeling + externalization = CONSEQUENCES
        of general-purpose hardware (not hardwired outputs)

  🟡 Compilable Architecture framing = framework synthesis (Inter-Body drill 2026-05-16)
```

---

## §1 — Body Sensors: Input Sources

> **Full enumeration: Body-Input-Enumeration.md**

### §1.1 — Exteroceptive (sensing the external world)

```
VISION (eyes):
  Receptor: rods (~120M, light/dark) + cones (~6M, color) on retina
  → Retina pre-processes → optic nerve → thalamus (LGN) → V1
  Special pathways:
    Circadian: ipRGC → SCN hypothalamus (BYPASSES visual cortex — Berson 2002)
    Threat:    retina → LGN → amygdala (~12ms, BYPASSES V1 — LeDoux 1996)

AUDITION (ears):
  Receptor: hair cells (~16,000) in cochlea
  → Cochlear nerve → thalamus (MGN) → A1 (auditory cortex)
  Tonotopic mapping: frequency → position on cortex

OLFACTION (nose):
  Receptor: ~10M olfactory neurons, ~400 receptor types
  → Olfactory bulb → olfactory cortex → limbic
  ⭐ EXCEPTION: BYPASSES THALAMUS entirely (OLDEST sense, >500M years)
  → smell → STRONGEST + FASTEST emotional memory  🟢 Gottfried 2010

GUSTATION (tongue):
  Receptor: ~10,000 taste buds (sweet/salty/sour/bitter/umami)
  → Cranial nerves → thalamus (VPM) → gustatory cortex (insula)

TACTILE (skin):
  Receptor: Meissner (light touch), Pacinian (vibration), Merkel (pressure), Ruffini (stretch)
  + Thermoreceptors + Nociceptors (A-delta fast + C-fiber slow)
  + ⭐ C-tactile fibers (pleasant touch → insula DIRECTLY, separate pathway — Olausson 2002)
  → Spinal cord → thalamus (VPL) → somatosensory cortex (S1/S2)
```

### §1.2 — Proprioceptive (sensing body position)

```
PROPRIOCEPTION: muscle spindles + joint receptors + Golgi tendon → thalamus → S1 + cerebellum
VESTIBULAR: semicircular canals + otoliths → vestibular nuclei → cerebellum + cortex
KINESTHETIC: muscle activity + efference copy (motor → cerebellum)
```

### §1.3 — Interoceptive (sensing internal state)

```
Cardiovascular: baroreceptors → vagus → brainstem → insula
Respiratory: chemoreceptors (CO₂) + stretch receptors → brainstem
Visceral: enteric nervous system → vagus → insula
Metabolic: glucose/ghrelin/leptin → hypothalamus
Hormonal: cortisol/oxytocin/dopamine/serotonin → body STATE changes
Nociception internal: A-delta + C-fibers → ACC + insula
Thermal core: hypothalamic thermosensors

⭐ HUB: Most interoceptive signals → ANTERIOR INSULA
  Craig 2009: anterior insula = "seat of subjective awareness" 🟢

⭐ SELF-SIGNAL INTEROCEPTION (meta-capacity):
  = The capacity to read one's own internal state → Anterior insula + ACC + vmPFC
  = Predictive: brain PREDICTS body state, matches actual → prediction-delta
  🟢 Seth 2013, Barrett 2017
```

### §1.4 — Summary

```
~20+ sensor types, 3 categories:
  Exteroceptive:  5 types (eyes, ears, nose, tongue, skin)
  Proprioceptive: 3 types (position, balance, movement)
  Interoceptive:  7+ types (heart, lungs, gut, metabolism, hormones, pain, thermal)

All output = action potentials (electrical impulses). Differ in: frequency + pattern + pathway.
```

---

## §2 — Thalamus: Gateway + Gatekeeper

### §2.1 — What the Thalamus Is

```
⭐ THALAMUS = CENTRAL RELAY STATION

  Location: central brain. Size: ~2 walnuts.
  
  RELAY:  forwards signals from sensors → cortex
  FILTER: filters signals (not all input reaches cortex)
  GATE:   opens/closes channels by attention (PFC-directed)
  
  🟢 Sherman & Guillery 2006 — thalamus as active relay
```

### §2.2 — Each Sense Has Its Own Nucleus

```
  Input          → Thalamic Nucleus     → Cortical Destination
  ─────────────────────────────────────────────────────────────
  Vision         → LGN                  → V1 (Visual cortex)
  Audition       → MGN                  → A1 (Auditory cortex)
  Touch/Pain     → VPL                  → S1 (Somatosensory)
  Taste          → VPM                  → Gustatory (insula)
  Proprioception → VPL                  → S1 + Cerebellum
  Interoception  → VMb + VMpo           → Anterior Insula

  ⭐ EXCEPTIONS (BYPASS thalamus):
  ① Olfaction → olfactory cortex → limbic DIRECTLY
  ② Amygdala subcortical: retina → LGN → amygdala (~12ms, before V1)
  ③ Circadian: ipRGC → SCN hypothalamus (no visual image)
```

### §2.3 — Thalamo-cortical Loop: 2 Directions

```
  BOTTOM-UP: Thalamus → Layer 4 cortex (raw data in)
  TOP-DOWN:  Cortex Layer 6 → thalamus (feedback: filter/amplify/suppress)
  PFC CONTROL: PFC → TRN (Thalamic Reticular Nucleus) → gates entire thalamus
  
  ⭐ METAPHOR: Thalamus = switchboard, TRN = operator, PFC = director directing the operator
  
  🟢 McAlonan et al. 2008 — TRN attentional gating
  🟢 Crick 1984 — searchlight hypothesis
```

---

## §3 — Cortical Areas: 6-Layer Architecture

### §3.1 — Cortical Column: Same Basic Architecture

```
⭐ MOUNTCASTLE 1957: The entire neocortex = SAME 6-LAYER STRUCTURE:

  Layer 1  MOLECULAR:          lateral connection highway between columns
  Layer 2/3 EXTERNAL PYRAMIDAL: receives/sends from OTHER CORTEX (cross-modal passes through here)
  Layer 4  INTERNAL GRANULAR:   receives input from THALAMUS (raw data port)
  Layer 5  INTERNAL PYRAMIDAL:  sends output OUTSIDE cortex (motor, subcortical)
  Layer 6  MULTIFORM:           sends feedback BACK TO THALAMUS (loop control)

  = "Neocortex is a uniform computational fabric" (Mountcastle)
  = Differ in WIRING + THICKNESS + RECEPTOR RATIO, not basic architecture
  
  🟢 Mountcastle 1957, 1978
  🟢 Douglas & Martin 2004 — canonical microcircuit
```

### §3.2 — Specialization: Same Architecture, Different Configuration

```
  ① LAYER THICKNESS:
     V1:  Layer 4 VERY THICK (heavy raw visual input)
     M1:  Layer 4 THIN, Layer 5 THICK (little input, much output)
     PFC: Layer 2/3 THICK (many cortex↔cortex connections)

  ② RECEPTOR DENSITY:
     PFC: many dopamine D1/D2 → sensitive to VTA signals
     V1:  few dopamine, many glutamate → high throughput

  ③ INHIBITORY RATIO:
     PFC: ~30% inhibitory → STRONG gate/brake
     Sensory: ~20% inhibitory → more throughput

  ④ CONNECTIVITY:
     V1: → V2, V4, MT (visual hierarchy)
     A1: → Wernicke (speech)
     PFC: → EVERYWHERE (broadest connectivity)
```

### §3.3 — Many-to-many Mapping

```
⭐ NOT 1:1. Mapping is MANY-TO-MANY:

  1 SENSOR → MANY cortical areas:
  ┌───────┐    ┌─ V1 Visual cortex (conscious image)
  │ EYES  ├────├─ Amygdala (~12ms, threat, BEFORE V1!)
  │       │    ├─ SCN hypothalamus (circadian, no image)
  └───────┘    └─ Superior Colliculus (eye orienting)

  ┌───────┐    ┌─ A1 Auditory cortex
  │ EARS  ├────├─ Amygdala (emotional sounds)
  │       │    ├─ Wernicke (speech sounds)
  └───────┘    └─ Motor cortex (rhythm→movement)

  ┌───────┐    ┌─ S1/S2 Somatosensory (where, what)
  │ SKIN  ├────├─ Insula (C-tactile: pleasant/unpleasant)
  │       │    ├─ ACC (pain: suffering dimension)
  └───────┘    └─ Motor (reflexive withdrawal)

  1 CORTICAL AREA ← MANY sensors:
  AMYGDALA ← eyes + ears + skin + nose + gut + hormones + mirror

  ⭐ IMPLICATION: "Modality" = PROCESSING AREA, not "input source"
  → Visual modality = Visual cortex PROCESSING (receives primarily from eyes
    + top-down from PFC + cross-modal from auditory)
```

### §3.4 — Visual Hierarchy: 1 Pathway in Detail

```
  Retina → LGN → V1 → V2 → V4 → IT
                          ↓
                          MT → MST

  V1: edges, orientations     → "straight line 45°"
  V2: contours, borders       → "circle outline"
  V4: shapes, colors          → "circular, red"
  IT: objects, faces          → "apple" / "mother's face" (CHUNKS!)
  MT: motion                  → "object moving left"

  ⭐ PFC reads IT (compiled patterns), DOES NOT read V1 (raw pixels)
  = PFC observes COMPILED RESULT, not raw data
  
  🟢 Felleman & Van Essen 1991
  🟢 Kanwisher 1997 — FFA (fusiform face area)
```

---

## §4 — Binding: How the Brain Syncs Multi-modal Input

> **F1 verdict: 07 §6 Emergent-Binding — 4 concurrent mechanisms**

### §4.1 — Gamma Oscillation ~40Hz — Temporal Synchrony

```
🟢 SINGER & GRAY 1995:

  Neurons in DIFFERENT cortical areas fire IN THE SAME PHASE within gamma band (~30-80Hz):
  → "fire same phase = belong to same object"

  Apple: V1(red) + V4(round) + MT(still) fire ~40Hz phase A = SAME object
  Glass: V1(blue) + V4(cylindrical) fire ~40Hz phase B = DIFFERENT object

  Cross-modal: Visual(apple) + Olfactory(apple scent) + Somatic(firm, cool) same phase A
  → Bound into 1 multi-modal chunk

  🟢 Singer 1999, Engel & Singer 2001, Fries 2005
  🟡 Debate: primary mechanism or correlate? (strong evidence, 25+ years)
```

### §4.2 — Multisensory Neurons — Hardware-level Binding

```
🟢 STEIN & MEREDITH 1993:

  Neurons RECEIVING INPUT FROM MULTIPLE MODALITIES:
  → 1 neuron fires when BOTH seeing AND hearing same object
  → Located in: Superior Colliculus, STS, Intraparietal Sulcus

  SUPERADDITIVITY: Visual(10) + Auditory(8) → simultaneously = 30 spikes (≠ 18!)
  TEMPORAL WINDOW: ~100-200ms for binding to occur
  DEVELOPMENTAL: present FROM BIRTH (hardware)
  
  🟢 Ghazanfar & Schroeder 2006
```

### §4.3 — Convergence Zones — Hub Areas for Integration

```
🟢 DAMASIO 1989:

  PARIETAL:        ← visual + auditory + somatosensory + proprioceptive
                   → SPATIAL MAP: "what is where"  🟢 Andersen 1997

  STS:             ← face + voice + body language
                   → PERSON PERCEPTION: "who is doing what"  🟢 Hein & Knight 2008

  ANTERIOR INSULA: ← interoception + nociception + affective touch + emotional
                   → BODY STATE: "what the body is doing"
                   → Where FEELING EMERGES (§8)  🟢 Craig 2009

  vmPFC:           ← insula (body state) + amygdala (valence) + memory
                   → VALUE BRIDGE: somatic marker → conscious evaluation
                   → vmPFC weak = Phineas Gage  🟢 Damasio 1994
```

### §4.4 — Amygdala Affective Tagging

```
🟢 AMYGDALA = "EMOTIONAL HIGHLIGHTER":

  Emotional event → amygdala fires → NE release broad
  → ALL neurons firing at the same moment → synapses STRENGTHEN (Hebbian LTP enhanced)
  → = "Emotional event → STRONG binding + FAST compilation"

  = Flashbulb memory mechanism (Brown & Kulik 1977)
  = Direction-At-Compile: same mechanism, different direction (novelty vs threat)
  
  🟢 McGaugh 2004, LeDoux 1996
```

### §4.5 — DMN Scaffolding

```
🟢 DMN = network active when NOT doing a task:
  mPFC + PCC + Angular gyrus + Hippocampus + Lateral temporal

  DMN provides LONG-RANGE CONNECTIVITY:
  → Without DMN → binding is LOCAL only
  → With DMN → binding is DISTANT (visual + insula + amygdala sync)
  → DMN present in adult-like form from birth (Doria et al. 2010)
```

### §4.6 — Binding Summary

```
  ┌───────────────────────────────────────────────────────┐
  │ #  │ Mechanism            │ Level      │ Speed       │
  ├───────────────────────────────────────────────────────┤
  │ 1  │ Gamma sync ~40Hz     │ Oscillation│ ~25ms       │
  │ 2  │ Multisensory neurons │ Hardware   │ Instant     │
  │ 3  │ Convergence zones    │ Hub areas  │ ~50-100ms   │
  │ 4  │ Amygdala tagging     │ Emotional  │ ~12-50ms    │
  │ 5  │ DMN scaffolding      │ Network    │ Continuous  │
  └───────────────────────────────────────────────────────┘
  → NO single binder. 5 mechanisms run SIMULTANEOUSLY.
  → Binding = EMERGENT PROPERTY.
```

---

## §5 — Chunk Compilation

> **Full analysis: Schema/Chunk.md**

### §5.1 — Chunk = Compiled Pattern

```
  BEFORE compilation: neurons fire INDEPENDENTLY → PFC holds 5 slots
  AFTER compilation:  neurons fire AS ONE → PFC holds 1 slot → COMPRESSION

  Chunk = physical change: synapses strengthen (LTP) + myelin thickens
```

### §5.2 — 4 Compilation Mechanisms

```
  ① REPETITION:          repeat many times → slow, durable
  ② EMOTIONAL PEAK:      amygdala + NE → 1 occurrence, strong (flashbulb)
  ③ MULTI-MODAL:         many modalities simultaneously → deep
  ④ SLEEP CONSOLIDATION: hippocampus replay → cortex transfer
  🟢 Diekelmann & Born 2010
```

### §5.3 — Multi-modal Chunks Span Many Areas

```
  1 modality  = surface ("water boils at 100°C" verbal only — easily forgotten)
  2 modalities = medium ("red light = stop" — verbal + visual)
  4 modalities = deep ("fear of dogs" — visual + auditory + somatic + emotional)
  5+ modalities = near-permanent ("I am worthless" — all modalities — years of therapy)
  → Chunk depth = modality count (Modality-Analysis §4)
```

### §5.4 — Expert = Meta-chunks

```
  Beginner: chunk A, B, C → PFC chains 3 steps (3 WM slots)
  Expert: meta-chunk [ABC] → PFC holds 1 slot → freed 2 slots for more
  → Expertise = compile chains → meta-chunks → PFC operates at higher level
  → "Experts are not smarter — experts have more compiled chunks"
  🟢 Chase & Simon 1973
```

### §5.5 — Compiled/Fresh at Physical Level (v2.0)

```
⭐ WHY COMPILED = FAST, FRESH = SLOW — at HARDWARE level:

  COMPILED PATH (Hebbian-strengthened):
    → Synapses: LTP-strengthened (🟢 Hebb 1949, Bliss & Lømo 1973)
    → Axons: MYELINATED (saltatory conduction: 100m/s vs 1m/s unmyelinated)
    → Pathway: DIRECT cortex→subcortex (bypass PFC bottleneck)
    → Neurotransmitter: vesicles PRE-DOCKED (faster release)
    → = Signal travels ESTABLISHED superhighway: fast, reliable, low energy

  FRESH PATH (novel, not yet compiled):
    → Synapses: weak, untested connections
    → Axons: unmyelinated or partially myelinated (SLOW conduction)
    → Pathway: must route THROUGH PFC (bottleneck: ~3-5 WM slots)
    → Neurotransmitter: needs dopamine BOOST for novel path activation
    → = Signal travels unmapped terrain: slow, unreliable, HIGH energy

  PHYSICAL CONSEQUENCES:
    Compiled: ~50-100ms response (subcortical direct)
    Fresh: ~300-500ms+ response (PFC chain required)
    = WHY expert "feels" the answer (compiled → body-direct → fast)
    = WHY beginner "thinks" the answer (fresh → PFC route → slow)
    = SAME CONTENT, different physical path quality

  COMPILATION PHYSICALLY CHANGES THE BRAIN:
    ① Synapse strength: LTP → larger post-synaptic density
    ② Myelin: oligodendrocytes wrap axon → speed increase 50-100x
    ③ Dendritic spine growth: more connection points per neuron
    ④ Pruning: competing weak paths WEAKENED (competitive)
    → = Compilation = PHYSICAL INFRASTRUCTURE built over time
    → = Compiled (Body-Knowing) = signal on SUPERHIGHWAY
    → = Fresh (PFC draft) = signal on DIRT ROAD being built

  CONNECTION WITH THE FRAMEWORK:
    → Logic-Feeling.md v2.0 §1: Compiled/Fresh = the real axis
    → Feeling.md v3.0 §2.5: 7-layer × Compiled/Fresh
    → Inter-Body §3: content ≠ processing level (Einstein math = compiled = fast)
    → 3-cost model: fresh = processing-intensive because novel path construction

🟢 Hebb 1949 (Hebbian learning principle)
🟢 Bliss & Lømo 1973 (LTP discovery)
🟢 Fields 2008 (activity-dependent myelination)
🟡 "Compiled = superhighway, Fresh = dirt road" metaphor = framework synthesis
```

---

## §6 — PFC: Observer + Director + Simulator

> **Full analysis: PFC-Analysis.md**

### §6.1 — PFC 5 Functions

```
  ① DRAFT:     creates temporary pattern (mixed-selectivity neurons, Rigotti 2013)
  ② TEST:      sends down to specialist regions to evaluate (amygdala/insula/temporal/BG)
  ③ ROUTE:     pass or discard based on feedback
  ④ BRAKE:     veto behavioral output (~200-500ms, after subcortical ~50ms)
  ⑤ TRANSLATE: verbalize post-hoc (rationalization — Gazzaniga)

  ⭐ PFC = LAWYER, not Judge (Inter-Body §7, v2.0 ELEVATED):
    Function ⑤ = NOT neutral reporting. = LAWYERING for body-base.
    → Body-need fires FIRST → drive forms → PFC creates NARRATIVE "the reason"
    → Person BELIEVES narrative = "rational decision"
    → 🟢 Gazzaniga split-brain: left hemisphere CONFABULATES post-hoc
    → 🟢 Haidt 2001: moral intuition first, reasoning = justification
    → 🟢 Nisbett & Wilson 1977: cannot report actual causes
    → IMPLICATION: PFC output (function ⑤) = STRUCTURAL bias
      Not occasional error — DESIGNED to serve body-base
    → Domain Reality = only check on PFC narrative (Inter-Body §6.4)
```

### §6.2 — KB4 Dual Role

```
  COMPILED schemas: PFC = GATE (veto/allow, minimal effort, PFC quiet)
  NEW schemas:      PFC = WORKSPACE MANAGER (hold space, effortful, PFC active)
  LEARNING = migration: Workspace → Gate (PFC freed for next thing)
```

### §6.3 — Sub-regions

```
  dlPFC: holds multiple schemas → compare A vs B
  vmPFC: BRIDGE body↔conscious → somatic marker (Damasio). Weak = poor decisions.
  OFC:   predicts reward per action → flexible update. Hyperactive = OCD.
  ACC:   detects schema CONFLICT → alerts "something feels off". Hypo = abulia. Hyper = anxiety.
  mPFC:  simulates other minds (Theory of Mind) → DMN hub → empathy ceiling = chunk overlap
```

### §6.4 — Top-down Spotlight

```
  PFC → VTA (dopamine) + LC (NE) + BF (acetylcholine) → target cortical area
  → Neurons fire MORE STRONGLY (gain increase) = "spotlight"
  → PFC doesn't turn cortex on/off — PFC BRIGHTENS/DIMS cortex
  
  = Bidirectional: bottom-up saliency + top-down spotlight = attention loop
  🟢 Desimone & Duncan 1995, Miller & Cohen 2001
```

### §6.5 — PFC Does NOT Compute — PFC Orchestrates

```
  PFC = CONDUCTOR, not a player
  → A conductor does not play music — a conductor COORDINATES
  → PFC drafts + tests + routes + brakes + translates + spotlights + gates
  → PFC does NOT: compute, generate content, evaluate, or make the final decision
```

---

## §7 — Simulation: Top-down Re-activation

> **Full analysis: [Imagination-Analysis-v2.md](Imagination/Imagination-Analysis-v2.md)**

### §7.1 — PFC Re-activates Cortical Patterns

```
⭐ IMAGINATION = PFC re-activates THE SAME cortical areas used for real perception

  REAL PERCEPTION (bottom-up):
    Eyes see a horse → retina → LGN → V1 → V2 → V4 → IT
    → IT fires "horse" pattern → PFC observes → KNOWS "horse"
    → Activation: STRONG (100% — real photon input)

  IMAGINATION (top-down):
    PFC "thinks about the horse" → spotlight signal FEEDS BACK to visual cortex
    → IT fires "horse" pattern (SAME neurons, SAME area)
    → Activation: WEAKER (~30-50% compared to real input)
    → = "Seeing" the horse in the mind — DIMMER than reality

  ⭐ SAME CORTICAL AREA, DIFFERENT DIRECTION + INTENSITY:
    Bottom-up (real):    sensor → thalamus → cortex → PFC    [STRONG, CLEAR]
    Top-down (imagine):  PFC → cortex (re-activate pattern)   [WEAK, DIM]

  🟢 Kosslyn 1994, 2005: fMRI confirmed — imagining uses SAME V1/V2 as real seeing
  🟢 Pearson 2019: individual differences (aphantasia → hyperphantasia spectrum)
```

### §7.2 — Multi-modal Simulation

```
PFC does NOT only re-activate visual — re-activates EVERY modality:

  VISUAL IMAGINE:    PFC → visual cortex    → "see" in the mind
  AUDITORY IMAGINE:  PFC → auditory cortex  → "hear" in the mind (inner voice, music)
  MOTOR IMAGINE:     PFC → motor cortex     → "feel" movement (measurable via EMG!)
  SOMATIC IMAGINE:   PFC → insula + S1      → "feel" body state
  EMOTIONAL IMAGINE: PFC → amygdala + insula → "feel" fear/joy/sadness

  ⭐ BODY TRULY RESPONDS TO IMAGINATION:

  Fidelity by modality (% vs real experience — calibration anchor, not precisely measured):
    Cortisol/stress response:  40-70%  (highest — imagine threat → cortisol REALLY rises!)
    Opioid/pleasure:           20-40%
    Motor activation:          10-30%  (measured via EMG — muscles contract slightly during imagination)
    Oxytocin:                  10-20%

  → Insight: cortisol response STRONGEST, oxytocin WEAKEST (direction clear, numbers approximate)
  → Imagine being scolded by your boss → cortisol REALLY rises significantly!
  → Imagine hugging someone you love → oxytocin REALLY rises slightly
  → Body does NOT clearly distinguish real vs imagined (only differs in intensity)
  → = Reason: worrying about the future causes REAL harm (real cortisol)
  → = Reason: mental rehearsal IMPROVES real performance (motor pre-build)
```

### §7.3 — Dual Output: Test + Pre-build

```
WHEN PFC IMAGINES, 2 things happen SIMULTANEOUSLY:

  ① TEST: "Is this idea feasible?"
     → PFC simulates → body responds → feel "ok" or "something's off"
     → = Body evaluates BEFORE logic verifies
     → = Imagine-Final.md: "draft → body test → pass/fail"

  ② PRE-BUILD: Schema partially compiled
     → Neurons fire pattern → synapses strengthen slightly
     → = Schema HAS ALREADY BEGUN compiling BEFORE actually doing it
     → = Mental rehearsal is effective because: rehearse = pre-compile
     → 🟢 Pascual-Leone 1995: mental piano practice → motor cortex REALLY changes
        (5 days of imagining piano play = cortical map expands, without TOUCHING the piano!)

  ⭐ IMPLICATION:
  → Imagine = NOT "just thinking" — imagine = ACTUALLY changes the brain (slightly)
  → Each imagination = 1 micro-compile event
  → Imagine many times = repetition compile (mechanism ① from §5.2)
  → = Imagination IS a chunk compilation mechanism (supplements the 4 mechanisms)
```

### §7.4 — Film/VR = "Hacking" Real Input into Cortical Areas

```
⭐ WHY WE FEAR A HORROR FILM EVEN KNOWING IT'S FAKE:

  FILM provides REAL input for 2/5 modalities:
    Visual: eyes see actual zombie on screen → V1 fires STRONGLY (100% activation)
    Auditory: ears hear real zombie sound from speakers → A1 fires STRONGLY (100%)
    → 2 modalities receive REAL input → pattern match → amygdala fires
    → Amygdala DOES NOT CHECK "real or fake" — amygdala fires if pattern matches
    → = GENUINELY SCARED even knowing it's fake (cortisol rises, heart rate rises)

  ABSENT:
    Touch: no contact with zombie → somatosensory quiet
    Smell: no zombie smell → olfactory quiet
    Proprioception: sitting on sofa → vestibular knows "safe"
    → 3/5 modalities say "safe" → conflict → "scared but knows it's fake"

  VR = STRONGER HACK:
    Visual: headset wraps 360° → V1 fires STRONGLY
    Auditory: spatial audio → A1 fires STRONGLY
    Vestibular: head tracking → vestibular MATCHES visual
    Proprioceptive: hand controllers → some proprioceptive match
    → 4/5 modalities → NEARLY REAL
    → VR sickness = vestibular-visual MISMATCH (lag, frame drop)
    → = Body detects: "visual says turning, vestibular says stationary" → nausea

  ⭐ GENERALIZED PRINCIPLE:
    → Many modalities receiving consistent input → brain treats as REAL
    → Fewer modalities or conflict → brain detects "fake" but partial response still fires
    → = Chunk depth (§5.3): more modalities = stronger = "more real"
```

---

## §8 — Feeling Emergence: Body Signal → Conscious Awareness

> **Full analysis: [Feeling.md](Body-Base/Feeling/Feeling.md) + [Feeling-Sources.md](Body-Base/Feeling/Feeling-Sources.md)**

### §8.1 — 7-layer Model: Raw → Conscious → Label → Explain

```
FEELING = the journey of SIGNAL from body UP to consciousness:

  ┌───────────────────────────────────────────────────────────────────────────┐
  │ Layer                   │ Name          │ Content                │Fidelity│
  ├───────────────────────────────────────────────────────────────────────────┤
  │ Feel-RawSignals         │ Raw signals   │ Heart rate, gut, pain  │  100%  │
  │ Feel-Integration        │ Integration   │ Multi-source combine   │  ~95%  │
  │ Feel-Consciousification │ Felt sense    │ "Something's off"      │  ~90%  │
  │ Feel-Observation        │ Observation   │ "In chest / in gut"    │  ~85%  │
  │ Feel-Location           │ Location      │ "Like last time"       │  ~80%  │
  │ Feel-Labeling           │ LABELING      │ "I'm anxious"          │ 40-80% │
  │ Feel-Explanation        │ EXPLANATION   │ "Because of deadline"  │ 20-70% │
  └───────────────────────────────────────────────────────────────────────────┘

  ⭐ FIDELITY DECREASES UPWARD (% = calibration anchor, not precisely measured — Core-Software.md §12.4):
    Feel-RawSignals = body truth (100% — body does not lie)
    Feel-Labeling = compressed label (40-80% — 1 word compresses 80%+ of information)
    Feel-Explanation = PFC confabulation (20-70% — PFC FABRICATES reasons post-hoc)

  → Most people "access" feeling at Feel-Labeling—Feel-Explanation (label + explain)
  → But Feel-Labeling—Feel-Explanation = MOST LOSSY
  → Wise practitioners dwell at Feel-Consciousification—Feel-Observation (felt sense — pre-verbal, high fidelity)
  → = Gendlin Focusing: train to stay at Feel-Consciousification, not rush up to Feel-Labeling—Feel-Explanation
```

### §8.2 — Feeling Observation Circuit: Insula + ACC + vmPFC

```
⭐ 3 BRAIN AREAS = "FEELING CIRCUIT":

  ANTERIOR INSULA:
    ← Receives: interoceptive signals (heart, lungs, gut, hormones, pain, thermal)
    → Generates: integrated BODY STATE representation
    → = "Dashboard" showing what the body is doing
    → Craig 2009: "seat of subjective awareness" 🟢

  ACC (Anterior Cingulate Cortex):
    ← Receives: conflict signals (schema A vs schema B mismatch)
    → Generates: "something's off" alert → sends to PFC
    → = "Alarm" when there is conflict
    → ⭐ ACC = physical mechanism for the "something feels off" sense

  vmPFC (Ventromedial PFC):
    ← Receives: insula body state + amygdala valence + memory associations
    → Generates: BRIDGE between body signal and conscious evaluation
    → = "Translator" body → conscious
    → vmPFC strong = feels clearly → good decisions (Damasio somatic marker)
    → vmPFC weak = feels dimly → poor decisions (Phineas Gage)

  FLOW:
    Body signals → Insula (integrate) → ACC (check conflict) → vmPFC (bridge to conscious)
    → PFC observe → Feel-Consciousification felt sense → (optional) Feel-Labeling label → (optional) Feel-Explanation explain

  ⭐ FEELING is NOT "in PFC" — feeling is in INSULA + ACC:
    PFC only OBSERVES feeling (via vmPFC bridge)
    Feeling EXISTS at body level (Feel-RawSignals) → insula integrates (Feel-Integration) → felt sense emerges (Feel-Consciousification)
    PFC may NOT observe (if vmPFC is weak, or attention is elsewhere)
    → = Feeling exists EVEN WHEN PFC does not register it (alexithymia)
    → = "Body knows what the mind doesn't" = insula has signal, PFC doesn't read it
```

### §8.3 — 10 Feeling Sources: Multi-channel Integration

```
FEELING = NOT only 1 INPUT — but ~10 channels integrated:

  ① L0 Threat signal       (amygdala: danger?)
  ② L1 Interoceptive       (insula: body state — heart, lungs, gut)
  ③ Novelty signal          (VTA dopamine: novel? interesting?)
  ④ Meaning/Schema          (temporal: matches what is already known?)
  ⑤ Agent mirror input     (mPFC: what is the other person feeling?)
  ⑥ Mirror-resonance       (body auto-fires in response to another person)
  ⑦ Schema expectation     (matches prediction or violates it?)
  ⑧ Imagine-Final preview  (how will the future feel?)
  ⑨ Valence compiled       (learned: this is good/bad from experience)
  ⑩ Cognitive evaluation   (PFC: what does logic say?)

  → INSULA integrates ~10 channels → 1 unified body state
  → PFC observes 1 unified state (DOES NOT observe 10 channels separately)
  → = Reason: feeling is COMPLEX + HARD to label
    (1 word "anxiety" compresses 10 channels into 1 label — loses 80%+ info)

  Full detail: Feeling-Sources.md


  ⭐ 5-CHANNEL INPUT VECTOR (Inter-Body §6, v2.0 connection):

  10 feeling sources MAP onto 5-Channel model:
    Ch1 HARDWARE SENSORY (①②③ above: threat, interoceptive, novelty)
    Ch2 BODY STATE (hormone level, fatigue, cortisol — baseline)
    Ch3 COMPILED CHUNKS (④⑦⑨: meaning, schema expectation, valence)
    Ch4 ENTITY ACTIONS (⑤⑥: agent mirror, mirror-resonance)
    Ch5 PFC ACTIVE CHAIN (⑧⑩: imagine-final preview, cognitive evaluation)

  Each episode = unique MIX of 5 channel intensities
  = 5-dimensional input space → infinite unique episodes
  Channel DOMINANT → determines body-need activation direction
  Channel ABSENT → determines vulnerability to manipulation

  Protection principle: never act from 1 channel alone
  (Inter-Body §6.4: Domain Reality = Final Arbiter)
```

### §8.4 — 2-Direction Flow (recap from Logic-Planning §7.4)

```
⭐ FEELING → LABEL: 2 directions to the same destination

  DIRECTION A — FEEL-FIRST (bottom-up):
    Body pattern fires → feel vague (Feel-Consciousification) → PFC attends → chunk becomes clearer
    → finds label (Feel-Labeling) → used in logic plan
    = Newborn, adult novel insight, Einstein

  DIRECTION B — LABEL-FIRST (top-down):
    Receives label (education) → practices → body compiles chunk → feeling matches label
    = Student, doctor, reading book: "ah, THAT is anxiety"

  Same destination: chunk with label → usable in plan
  Different starting point: body-first vs language-first
```

---

## §9 — Externalization Loop: Weak Internal → Strong External

> **Full analysis: [Somatic-Articulation-Loop.md](Imagination/Somatic-Articulation-Loop.md)**

### §9.1 — Principle: Internal Weak → Externalize → Re-input Strong

```
⭐ EXTERNALIZATION = HACK converting weak top-down into strong bottom-up:

  TOP-DOWN (imagine):
    PFC re-activates cortical pattern → WEAK (~30-50%)
    → Dim, hard to hold, easily lost, WM limit ~3-5 items

  EXTERNALIZE (output to the world):
    Hand draws → image on paper
    Mouth speaks → sound in the air
    Hand writes → words on screen
    Hand plays instrument → sound from the instrument

  RE-INPUT (bottom-up):
    Eyes see the drawing → visual cortex fires STRONGLY (100% — real input!)
    Ears hear oneself speak → auditory cortex fires STRONGLY
    → Pattern is now CLEAR + STRONG + DURABLE compared to internal imagination

  COMPARE:
    PFC compares: external (clear) vs internal intent (dim)
    → "That's what I meant" → keep
    → "Not quite right, horns too big" → adjust → redraw → re-input → compare again
    → = FEEDBACK LOOP: imagine → externalize → perceive → compare → adjust
```

### §9.2 — Instances: Every Creative Process Uses This Mechanism

```
  Painter:    imagine (weak) → paint → look (strong) → adjust → repaint
  Musician:   hear in head (weak) → play instrument → listen (strong) → adjust
  Writer:     think idea (weak) → write → read back (strong) → revise
  Programmer: think logic (weak) → code → run → see result (strong) → debug
  Scientist:  hypothesis (weak) → experiment → observe (strong) → revise
  Architect:  imagine building (weak) → draw blueprint → look (strong) → refine

  → EVERY creative/intellectual process = SAME loop:
    Internal (weak top-down) → Externalize → Re-perceive (strong bottom-up) → Compare → Iterate
```

### §9.3 — Somatic-Articulation Loop: Feeling-specific Externalization

```
  Feeling version of the externalization loop:

  Feel vague (Feel-Consciousification, weak) → try saying / writing it → listen back / read back (strong)
  → Body check: "getting closer" / "not yet" / "YES, THAT'S IT!"
  → Adjust label → try again → body check → ...
  → Finally: feeling has an accurate label → usable in logic

  CATALYST needed:
    → A listener (therapist, friend, partner)
    → AI (available 24/7, patient, multi-format)
    → Writing (journaling, freewriting)
    → Drawing (art therapy)

  = NOT retrieval — but a CONSTRUCTION process (built gradually, not pre-existing)
```

### §9.4 — Clark Extended Mind

```
🟢 CLARK & CHALMERS 1998 — Extended Mind Thesis:

  "Mind is NOT only in the skull — mind INCLUDES external tools"

  Paper + pen = extends WM (drawing = adds visual "memory" outside the brain)
  Calculator = extends math processing
  Code editor = extends logic processing
  AI chatbot = extends articulation capacity

  → Externalization is NOT "dumping info outside"
  → Externalization = EXTENDS cognitive capacity beyond brain limits
  → = Brain (3-5 WM slots) + Paper (unlimited visual slots) = STRONGER system

  ⭐ AI ERA EXTENSION:
  → AI = EXTREMELY POWERFUL externalization partner
  → Feel vague → tell AI → AI suggests label → body check → iterate
  → AI helps plan → PFC freed → can feel more
  → = "Humans need to FEEL correctly → AI will help PLAN correctly" (Logic-Planning.md)
```

---

## §10 — Complete Flow Diagram

### §10.1 — Full Flow: Sensor → PFC → Output → Feedback

```
⭐ COMPLETE FLOW IN 1 DIAGRAM:

  ┌──────────────────────────────────────────────────────────────────┐
  │                    BODY SENSORS (~20+ types)                     │
  │  Exteroceptive: eyes, ears, nose, tongue, skin                   │
  │  Proprioceptive: position, balance, movement                     │
  │  Interoceptive: heart, lungs, gut, hormones, pain, thermal       │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ raw electrical signals (action potentials)
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │                    THALAMUS (Gateway)                            │
  │  • Each sense → own nucleus (LGN, MGN, VPL, VPM,...)            │
  │  • FILTER + GATE (TRN control, PFC directs)                     │
  │  • Exceptions: olfaction bypass, amygdala subcortical pathway    │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ filtered signals → Layer 4
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │               CORTICAL AREAS (6-layer columns)                   │
  │                                                                  │
  │  Visual    Auditory    Somatosensory    Motor    Emotional       │
  │  cortex    cortex      cortex (S1/S2)   cortex   (amygdala)     │
  │    │          │             │              │          │          │
  │    ├──sparse cross-modal connections (Layer 2/3)──────┤          │
  │    │          │             │              │          │          │
  │    └──────────┴─────────────┴──────────────┴──────────┘          │
  │                         │                                        │
  │              BINDING MECHANISMS:                                  │
  │              • Gamma sync ~40Hz                                  │
  │              • Multisensory neurons                              │
  │              • Convergence zones (Parietal/STS/Insula)           │
  │              • Amygdala affective tagging                        │
  │              • DMN scaffolding                                   │
  │                         │                                        │
  │              COMPILATION:                                        │
  │              • Repetition / Emotional peak /                     │
  │                Multi-modal / Sleep consolidation                 │
  │              • Pattern → Chunk → Meta-chunk                      │
  └────────────────────────┬─────────────────────────────────────────┘
                           │ compiled patterns (chunks)
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │           FEELING CIRCUIT (Insula + ACC + vmPFC)                 │
  │                                                                  │
  │  Anterior Insula: integrates body state (10 channels → 1 state) │
  │  ACC: detects conflict → "something feels off" signal            │
  │  vmPFC: bridges body → conscious (somatic marker)               │
  │                         │                                        │
  │  → Feel-RawSignals raw → Feel-Integration integrate              │
  │    → Feel-Consciousification felt sense → (optional Feel-Labeling)│
  └────────────────────────┬─────────────────────────────────────────┘
                           │ feeling signals + compiled chunks
                           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │                    PFC (Orchestrator)                            │
  │                                                                  │
  │  OBSERVE:   reads compiled patterns + feeling state              │
  │  DRAFT:     creates temporary patterns (mixed-selectivity neurons)│
  │  TEST:      sends to specialist regions (amygdala/insula/BG)    │
  │  ROUTE:     pass/discard based on body feedback                 │
  │  BRAKE:     veto behavioral output (~200-500ms)                 │
  │  TRANSLATE: verbalize post-hoc                                   │
  │  SPOTLIGHT: amplify target cortical areas (NE + Ach + DA)       │
  │  SIMULATE:  re-activate cortical patterns TOP-DOWN (§7)         │
  │                                                                  │
  │  dlPFC: compare   vmPFC: value   OFC: reward   ACC: conflict    │
  │  mPFC: social simulation (Theory of Mind, DMN hub)              │
  └──────────┬───────────────────────────────────┬───────────────────┘
             │ motor commands                     │ top-down re-activation
             ▼                                    ▼
  ┌────────────────────┐            ┌─────────────────────────────┐
  │  MOTOR OUTPUT      │            │  SIMULATION (top-down)      │
  │  • Speech (Broca)  │            │  • Re-activate visual/      │
  │  • Hand movement   │            │    auditory/motor/somatic   │
  │  • Facial expression│           │  • ~30-50% activation       │
  │  • Body posture    │            │  • Body RESPONDS (real      │
  │  • Writing/Drawing │            │    cortisol, real EMG)      │
  │  • Code typing     │            │  • Dual: test + pre-build   │
  └────────┬───────────┘            └──────────────────────────────┘
           │ externalized output
           ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │              EXTERNALIZATION LOOP                                │
  │                                                                  │
  │  Internal (weak, ~30-50%) → Externalize (hand/voice/write)      │
  │  → Re-perceive (strong, 100% — real visual/auditory input)      │
  │  → Compare (PFC: external vs internal intent)                   │
  │  → Adjust → Externalize again → ...                             │
  │                                                                  │
  │  = Creative process loop. Writing-as-thinking. Drawing-as-seeing │
  │  = Somatic-Articulation Loop (feeling → label construction)     │
  │  = AI catalyst: feel → tell AI → AI suggest → body check        │
  └──────────────────────────┬───────────────────────────────────────┘
                             │ feedback (re-enters as new input)
                             ▼
                    ← BACK TO BODY SENSORS (loop) ←
```

### §10.2 — Bottom-up vs Top-down: 2 Directions

```
BOTTOM-UP (reality → brain):
  Sensor → Thalamus → Cortex → Binding → Chunk → Feeling → PFC observes
  = "The world telling the brain"
  = STRONG, accurate, body-driven
  = Source of feeling (Feel-RawSignals—Feel-Consciousification)
  = Source of chunk compilation

TOP-DOWN (brain → cortex re-activation):
  PFC → Spotlight → Cortex re-activate → Body responds (partial)
  = "The brain telling itself"
  = WEAKER (~30-50%), can be wrong (confabulation)
  = Source of imagination, planning, simulation
  = Source of mental rehearsal, worry, creativity

⭐ HEALTHY COGNITION = BALANCE BETWEEN 2 DIRECTIONS:
  Too much bottom-up = reactive (only responds, does not plan)
  Too much top-down = detached (lives in the head, does not feel reality)
  Balance = feel reality (bottom-up) + plan ahead (top-down) + check (feedback)
```

### §10.3 — Observation Parameters Modulating Flow (v2.0 FIX)

```
⚠️ v2.0 FIX: v1.0 called these "L3 operators" — outdated.
   v7.8 reframe: L3 removed. These are OBSERVATION PARAMETERS
   (named patterns emerging from body-need interactions, not a separate layer).
   Inter-Body §2.3: "Observation params = NOT sources — are NAMES for observable patterns."

3 OBSERVATION PARAMETERS MODULATE flow (do not create separate flow):

  NOVELTY (observation parameter):
    → VTA detect above-baseline input quality → dopamine → PFC spotlight
    → Shifts baselines upward (hedonic treadmill)
    → Operates across ALL body-input categories
    → = NAMED PATTERN from gap-fill drive (Gap-Direction.md)

  STATUS (observation parameter):
    → PFC construct: social position → PROXY for body-input access
    → Status itself has NO body-base receiver
    → Status → body-input payoff (community → co-presence; reputation → resources)
    → Status without payoff = emptiness
    → = NAMED PATTERN from social hardware needs (Inter-Body §1)

  PROTECT (observation parameter):
    → Guard body-inputs from threats
    → Extends via Empathy-Mirror: mirrored body-state → protect-other behavior
    → = NAMED PATTERN from ownership + loss aversion (Protect.md)

  → 3 parameters MODULATE flow, do not create separate flow
  → Novelty: affects WHAT gets spotlighted
  → Status: affects WHAT PFC drafts as goal
  → Protect: affects WHAT gets priority (threat override)
  → Intervenes at mechanism level (body-need sources), not at label level
```

---

## §11 — Honest Assessment + References

### §11.1 — Confidence Levels

```
═══════════════════════════════════════
🟢 ESTABLISHED NEUROSCIENCE
═══════════════════════════════════════

  Thalamic relay + gating:           Sherman & Guillery 2006, Jones 2007
  6-layer cortical column:           Mountcastle 1957, Douglas & Martin 2004
  Visual hierarchy V1→IT:            Felleman & Van Essen 1991, Hubel & Wiesel 1962
  Olfaction bypass thalamus:         Gottfried 2010
  Amygdala subcortical pathway:      LeDoux 1996
  Multisensory neurons:              Stein & Meredith 1993, Ghazanfar 2006
  Amygdala emotional modulation:     McGaugh 2004
  DMN at birth:                      Doria et al. 2010
  Anterior insula interoception:     Craig 2002, 2009
  vmPFC somatic marker:              Damasio 1994, 1996
  Top-down re-activation (imagine):  Kosslyn 1994, 2005
  Mental rehearsal motor:            Pascual-Leone 1995
  ACC conflict detection:            Botvinick et al. 2004
  PFC attention control:             Desimone & Duncan 1995, Miller & Cohen 2001
  TRN attention gating:              McAlonan et al. 2008
  C-tactile affective touch:         Olausson 2002
  Predictive interoception:          Seth 2013, Barrett 2017
  Extended mind:                     Clark & Chalmers 1998
  Sleep consolidation:               Diekelmann & Born 2010
  Felt sense / Focusing:             Gendlin 1978
  PFC mixed selectivity:             Rigotti et al. 2013
  Expert chunking:                   Chase & Simon 1973
  Hebbian learning:                  Hebb 1949
  LTP discovery:                     Bliss & Lømo 1973
  Activity-dependent myelination:    Fields 2008
  Split-brain confabulation:         Gazzaniga (v2.0: PFC=Lawyer)
  Moral intuition first:             Haidt 2001 (v2.0: PFC=Lawyer)
  Cannot report causes:              Nisbett & Wilson 1977 (v2.0: PFC=Lawyer)


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS
═══════════════════════════════════════

  Gamma binding as PRIMARY mechanism:    Singer well-supported, debate ongoing
  5-mechanism binding model:             4 from Emergent-Binding + gamma = synthesis
  Many-to-many mapping as reframe:       Consistent with evidence, framework framing
  7-layer feeling fidelity gradient:     Framework contribution (Feeling.md)
  10-channel feeling integration:        Framework contribution (Feeling-Sources.md)
  Externalization as general principle:  Consistent, generalized from established instances
  PFC 5-function model:                  Framework synthesis (PFC-Analysis.md)
  KB4 dual role:                         Framework synthesis, consistent
  Chunk depth = modality count:          Framework contribution (Modality-Analysis.md)
  2-Direction flow (feel-first/label-first): Framework contribution (Logic-Planning.md)
  Compilable Architecture as WHY this hardware (v2.0): Consistent with evolutionary neuroscience
  Compiled/Fresh at physical level (v2.0):   LTP + myelin = established; framing = synthesis
  PFC = Lawyer as structural function (v2.0): Consistent with Gazzaniga/Haidt, elevated
  5-Channel Input Vector mapping (v2.0):     Framework synthesis (Inter-Body §6)
  Observation parameters (not L3 operators):  v7.8 reframe, consistent


═══════════════════════════════════════
🔴 HYPOTHESES
═══════════════════════════════════════

  Specific fidelity percentages (Feel-RawSignals 100%, Feel-Explanation 20-70%):  Illustrative, not measured
  Imagination fidelity % per modality:                  Approximate, varies individually
  "ACC = physical mechanism for the 'something feels off' sense":  Plausible, not directly tested
  AI as externalization catalyst effectiveness:          New, unstudied longitudinally
```

### §11.2 — What This File CLAIMS vs NOT CLAIMS

```
CLAIMING:
  ✓ Body signals travel specific physical pathways to specific cortical areas
  ✓ Thalamus gates most (not all) sensory input
  ✓ Cortical architecture is uniform 6-layer (Mountcastle), specialized by wiring
  ✓ Sensor→cortex mapping is many-to-many (not 1:1)
  ✓ Binding uses multiple concurrent mechanisms (not single binder)
  ✓ PFC observes compiled patterns, does not compute raw data
  ✓ PFC can re-activate cortical patterns top-down (imagination)
  ✓ Body responds to imagination (partial, measurable)
  ✓ Feeling emerges in insula/ACC/vmPFC circuit, PFC observes
  ✓ Externalization converts weak top-down to strong bottom-up

NOT CLAIMING:
  ✗ This is a complete neuroscience textbook (simplified for framework use)
  ✗ Specific neuron counts or exact pathway details are comprehensive
  ✗ Fidelity percentages are measured (they are framework estimates)
  ✗ Binding problem is "solved" (active research area)
  ✗ Consciousness is explained (hard problem remains)
```

### §11.3 — Full Reference List

```
  Andersen 1997    — Multimodal spatial representations in parietal cortex
  Barrett 2017     — Predictive interoception / constructed emotion
  Berson 2002      — ipRGC circadian pathway
  Botvinick 2004   — ACC conflict monitoring
  Brown & Kulik 1977 — Flashbulb memory
  Chase & Simon 1973 — Expert chunking in chess
  Clark & Chalmers 1998 — Extended Mind thesis
  Craig 2002, 2009 — Interoception, anterior insula, awareness
  Crick 1984       — Searchlight hypothesis (thalamus + attention)
  Damasio 1989     — Convergence-divergence zones
  Damasio 1994     — Somatic marker hypothesis / Descartes' Error
  Desimone & Duncan 1995 — Biased competition attention model
  Diekelmann & Born 2010 — Sleep-dependent memory consolidation
  Doria et al. 2010 — Neonatal DMN functional connectivity
  Douglas & Martin 2004 — Canonical cortical microcircuit
  Engel & Singer 2001 — Temporal binding by gamma oscillation
  Felleman & Van Essen 1991 — Hierarchical visual processing
  Fries 2005       — Communication through coherence
  Gendlin 1978     — Focusing / felt sense
  Ghazanfar & Schroeder 2006 — Cross-modal cortical interactions
  Gottfried 2010   — Olfactory-limbic direct pathway
  Hein & Knight 2008 — STS multimodal person processing
  Hubel & Wiesel 1962 — Visual cortex feature detection
  Jones 2007       — Thalamic nuclei functional mapping
  Kanwisher 1997   — Fusiform face area (FFA)
  Kosslyn 1994, 2005 — Mental imagery uses visual cortex
  LeDoux 1996      — Amygdala fear conditioning / subcortical pathway
  McAlonan et al. 2008 — TRN attentional gating
  McGaugh 2004     — Emotional modulation of memory
  Miller & Cohen 2001 — PFC top-down control
  Mountcastle 1957 — Cortical column uniformity
  Olausson 2002    — C-tactile affective touch pathway
  Pascual-Leone 1995 — Mental rehearsal changes motor cortex
  Pearson 2019     — Mental imagery individual differences
  Rigotti et al. 2013 — PFC mixed selectivity neurons
  Seth 2013        — Predictive interoception
  Sherman & Guillery 2006 — Thalamus as active relay
  Singer & Gray 1995 — Gamma oscillation binding
  Stein & Meredith 1993 — Multisensory integration
  Hebb 1949            — Hebbian learning principle (v2.0)
  Bliss & Lømo 1973    — LTP discovery (v2.0)
  Fields 2008          — Activity-dependent myelination (v2.0)
  Gazzaniga            — Split-brain confabulation (v2.0: PFC=Lawyer)
  Haidt 2001           — Moral intuition first (v2.0: PFC=Lawyer)
  Nisbett & Wilson 1977 — Cannot report actual causes (v2.0: PFC=Lawyer)
```

---

## §12 — CROSS-REFERENCES (v2.0 NEW)

```
📚 INTER-BODY DRILL:
  → Inter-Body-Mechanism.md v1.0 §1: Compilable Architecture (WHY this hardware)
  → Inter-Body-Mechanism.md v1.0 §3: Compiled/Fresh = the real axis (→ §5.5)
  → Inter-Body-Mechanism.md v1.0 §6: 5-Channel Input Vector (→ §8.3)
  → Inter-Body-Mechanism.md v1.0 §7: PFC = Lawyer (→ §6.1)

📚 FEELING + BODY-FEEDBACK:
  → Feeling.md v3.0 §2.5: Compiled/Fresh × 7-Layer mapping
  → Feeling.md v3.0 §3.4: PFC = Lawyer formal
  → Body-Feedback-Mechanism.md v2.0: 2-source, Body-Need aggregate
  → Body-Input-Enumeration.md: full body input catalog (§1 source)

📚 PROCESSING:
  → Logic-Feeling.md v2.0 §1: Compiled/Fresh = the real axis
  → Logic-Feeling.md v4.0 §3: Flow (Body-Knowing Anchor ↔ Fresh Explore ↔ Domain Verify)
  → PFC-Analysis.md: PFC functions detail
  → Somatic-Articulation-Loop.md: externalization mechanism detail

📚 CHUNK + COMPILATION:
  → Chunk.md v2.0: chunk system reference
  → Modality-Analysis.md: modality depth

📚 OBSERVATION:
  → Gap-Direction.md v2.0: gap direction (novelty parameter)
  → Protect.md v1.0: protect parameter
  → Status.md v2.0: status parameter
```

---

## §13 — STATUS (v2.0)

```
File: Neural-Processing-Flow.md
Version: 2.0
Created: 2026-04-17
Updated: 2026-05-17
Previous: v1.0 → backup/Neural-Processing-Flow-v1.0-backup.md
Lines: ~1,230

v2.0 CHANGES (2026-05-17 — Inter-Body Drill Integration):
  → Header: v2.0, +dependencies, +confidence markers
  → §0: +Compilable Architecture connection (WHY this hardware = general-purpose)
  → §5.5 NEW: Compiled/Fresh at PHYSICAL level
    (WHY compiled=fast: LTP+myelin. WHY fresh=slow: novel unmyelinated paths)
  → §6.1: +PFC=Lawyer elevated (structural function, not occasional error)
  → §8.3: +5-Channel Input Vector connection (10 channels → 5-channel model)
  → §10.3 FIX: "L3 operators" → "Observation parameters" (v7.8 reframe)
  → §11: +6 🟢 citations (Hebb, Bliss&Lømo, Fields, Gazzaniga, Haidt, Nisbett&Wilson)
         +5 🟡 items (Compilable Architecture, Compiled/Fresh physical, PFC=Lawyer, 5-Channel, observation parameters)
  → §12 NEW: Cross-references section
  → ALL v1.0 hardware content PRESERVED (§1-§4, §7, §9)
  → ALL 35+ research citations preserved + 6 added = 41+ total
```

---

> **Neural-Processing-Flow.md v2.0 — End of file.**
>
> Physical foundation: complete flow from sensor → thalamus → cortex → binding → chunks → feeling → PFC → simulation → externalization → feedback loop.
>
> v2.0: +Compilable Architecture (WHY), +Compiled/Fresh physical (HOW compiled=fast),
> +PFC=Lawyer (structural), +5-Channel mapping, +L3→observation parameter fix.
>
> All other mechanisms in the framework RUN ON this flow.
>
> **Version:** v2.0, 2026-05-17.
