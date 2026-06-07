---
title: "Feeling — The Unified Feedback System of Body-Base"
version: 3.0
language: English
source_version: "Vietnamese v3.0"
english_created: 2026-06-06
source_path: "Core-Deep-Dive/Body-Base/Feeling/Feeling.md"
tags: [feeling, body-base, feedback-system, chunk-system, PFC, dopamine, reward, literacy]
---

# Feeling — The Unified Feedback System of Body-Base

> v3.0 — PFC=Lawyer integrated (rewritten 2026-05-17)
> Central reference file for the Feeling system.
> Seven companion files provide deeper coverage of specific subsections.

---

## §0 — POSITION IN FRAMEWORK

### 0.1 What This File Is

Feeling is not a separate system. It is the **observable output** of body-chunk interaction — the signal body-base sends to PFC, made noticeable.

Every other system in the framework uses feeling, whether explicitly or implicitly:
- **Chunk system** produces feelings as output of pattern-matching
- **Drive system** uses feeling as input to motivation direction
- **Imagine-Final** generates preview feelings before action
- **Schema system** fires compiled feelings from past experiences
- **Self-Observation** is feeling directed inward toward the self

Feeling is the **unified feedback system** through which body-base communicates with PFC.

### 0.2 Compilable Architecture Connection

The framework's Compilable Architecture explains **why** the feeling system is general-purpose rather than domain-specific.

```
COMPILABLE ARCHITECTURE → FEELING SYSTEM:

  Biological evolution → GENERAL-PURPOSE reward system
  (not hardcoded domain-specific rewards)
  ↓
  = General-purpose reward → GENERAL-PURPOSE FEEDBACK
  ↓
  = Feeling system: reports on ANY body-chunk interaction
  (physical, emotional, social, cognitive, aesthetic...)
  ↓
  = WHY feeling is not limited to "basic emotions"
  = WHY the same mechanism handles hunger, grief, insight, beauty

  → Detail: Inter-Body-Mechanism.md §1, Reward-Signal-Architecture.md §0.3
```

### 0.3 File Map

```
§0:  Position (why feeling is central)
§1:  Definition (what feeling is — formal)
§2:  7-Layer Fidelity Gradient (how much PFC can trust each layer)
§3:  Core Claim (body-first + PFC=Lawyer)
§4:  Signal Integration (3 hubs + 5-step mechanism)
§5:  8-Step Operational Flow (complete step-by-step)
§6:  Reward — Dopamine ≠ Reward
§7:  Feeling Gradient: Clear ↔ Vague
§8:  Feeling Quality = f(Chunk Library × Compile Context)
§9:  Feeling Loop + Chunk-Feeling Bridge
§10: Feeling Literacy + Training (5-Stage Framework)
§11: Evolutionary Framing (2M years + 5 mismatches)
§12: Honest Assessment (🟢/🟡/🔴 + predictions)
§13: Cross-References
§14: Status
```

---

## §1 — DEFINITION + 7 TYPES + 3 CRITICAL PROPERTIES

### 1.1 Formal Definition

```
⭐ FEELING = WHAT PFC SEES
  when it observes body-chunk interaction.

  NOT:
    ✗ "chemical reaction in the brain"
    ✗ "emotion as separate system"
    ✗ "subjective experience unrelated to body"
    ✗ "output of logic-planning"

  IS:
    ✓ Body-chunk interaction → integrated signal
    ✓ Signal crosses PFC observation threshold
    ✓ PFC observes → what PFC sees = feeling
    ✓ PFC can locate, label, and explain (with varying accuracy)
    ✓ The same mechanism operates across all feeling types
```

### 1.2 Seven Types of Feeling

All seven types operate through the same mechanism. The difference is which body signals are involved.

```
TYPE 1 — BODY-PHYSICAL:
  Source: physical body state (pain, temperature, hunger, fatigue)
  Example: "My back hurts." "I'm cold." "Starving right now."
  Layer: Feel-RawSignals → Feel-Consciousification (clear, sourced from hardware)

TYPE 2 — EMOTIONAL (narrow):
  Source: named emotional states (sadness, joy, anger, fear, disgust)
  Example: "I feel sad." "I'm excited."
  Layer: Feel-Observation → Feel-Labeling (PFC can label)

TYPE 3 — SOCIAL READING:
  Source: mirror system firing on social signals
  Example: "Something's off with them." "The room feels tense."
  Layer: Feel-Observation (often vague if unlabeled)

TYPE 4 — COGNITIVE / PREDICTION:
  Source: chunk mismatch, prediction error, logic tension
  Example: "This doesn't add up." "Something's wrong here."
  Layer: Feel-Observation → Feel-Labeling

TYPE 5 — PREDICTIVE / INTUITION:
  Source: many weak chunks converging without clear label
  Example: "I have a hunch." "Gut feeling about this."
  Layer: Feel-Consciousification → Feel-Observation (vague)

TYPE 6 — VALENCE:
  Source: compiled approach/avoid tags firing
  Example: "This feels right." "I don't like this."
  Layer: Feel-Observation (fast, compiled)

TYPE 7 — SCHEMA-TRIGGERED:
  Source: schema activates → compiled feeling fires
  Example: "I always feel anxious in meetings." (schema activated)
  Layer: Feel-Observation (strong, compiled, often automatic)
```

### 1.3 Three Critical Properties

```
⭐ PROPERTY 1 — MULTI-SOURCE:
  Feeling = aggregate of MULTIPLE body channels simultaneously.
  Not single-source.
  → Insula integrates: physical + emotional + social + cognitive signals
  → = WHY feelings are "complex" and difficult to reduce to one cause

⭐ PROPERTY 2 — INTEGRATED:
  Signals merge before PFC observes them.
  PFC does NOT observe raw individual signals.
  PFC observes the INTEGRATED result.
  → Integration happens below PFC (insula + ACC + VMPFC)

⭐ PROPERTY 3 — OBSERVABLE (2 dimensions):
  DIMENSION A — MAGNITUDE: How strong is the signal?
    → Strong → easier to cross PFC threshold → clearer feeling
    → Weak → may not cross threshold → unnoticed

  DIMENSION B — CLARITY: How distinguishable is the signal?
    → High clarity → easy to locate and label
    → Low clarity → vague, hard to name (→ §7 Gradient)

  → Both dimensions are trainable (→ §10 Feeling Literacy)
```

---

## §2 — 7-LAYER FIDELITY GRADIENT

> Framework contribution — useful functional taxonomy, not a validated anatomical taxonomy.

### 2.1 The Seven Layers

The 7-Layer Fidelity Gradient describes how much PFC can trust the signal at each stage of processing. Fidelity decreases as PFC involvement increases — because PFC interprets, and interpretation introduces error.

```
⭐ 7-LAYER FIDELITY GRADIENT:

  LAYER              | NAME                    | FIDELITY | DESCRIPTION
  ───────────────────┼─────────────────────────┼──────────┼──────────────────────────────
  Feel-RawSignals    | Raw body signals        | ~100%    | Directly from body hardware
  Feel-Integration   | Integrated signal       | ~90%     | Multi-source merged at insula
  Feel-Consciousif.  | Crosses threshold       | ~80%     | PFC becomes aware "something"
  Feel-Observation   | Recognized pattern      | ~70%     | PFC matches to known patterns
  Feel-Location      | Located in body/domain  | ~60%     | "In my chest" / "About work"
  Feel-Labeling      | Named                   | ~50%     | Verbal handle attached
  Feel-Explanation   | Explained / narrated    | ~20-70%  | PFC constructs story (varies)
  ───────────────────┴─────────────────────────┴──────────┴──────────────────────────────

  ⭐ FIDELITY DECREASES as PFC involvement increases.
  ⭐ Feel-Explanation is the LEAST reliable layer (PFC=Lawyer effect).
  ⭐ Feel-RawSignals → Feel-Consciousification = body truth.
  ⭐ Feel-Labeling → Feel-Explanation = PFC construction (often accurate, sometimes not).
```

### 2.2 Why Feel-Explanation Is Least Reliable

Feel-Explanation is where PFC constructs a narrative to explain the feeling. This is not neutral reporting — it is post-hoc rationalization.

```
PFC = LAWYER, NOT JUDGE (see §3.4 for full section):

  At Feel-Explanation layer:
  → PFC has a candidate label (from Feel-Labeling)
  → PFC builds a narrative: "I feel X BECAUSE Y"
  → This narrative can be WRONG while feeling CONVINCING
  → PFC argues for its preferred interpretation
  → Body signals get selected, filtered, reframed to fit

  EXAMPLES:
    "I'm nervous about the meeting" ← may actually be hunger + mild dread
    "I love my work" ← may actually be cortisol from deadline (wanting without liking)
    "I'm angry at them" ← may actually be shame projected outward

  → Trust Feel-Consciousification → Feel-Observation more than Feel-Explanation.
  → Ask body, not narrative.
```

### 2.3 Compiled/Fresh × 7-Layer Mapping

The Compiled/Fresh axis (from Compilable Architecture) interacts with the 7-Layer gradient in predictable ways.

```
🟡 COMPILED/FRESH × 7-LAYER MAPPING:

  COMPILED FEELING (chunk compiled, pathway fast):
    → Fires at Feel-Observation immediately (bypasses slow integration)
    → STRONG, FAST, AUTOMATIC
    → Feel-Explanation: "Of course I feel this way about X"
    → Risk: outdated compile context still fires (§8.4 trauma distortion)

  FRESH FEELING (new input, no matching compiled chunk):
    → Must go through Feel-RawSignals → Feel-Integration → Feel-Consciousification
    → SLOWER, WEAKER, HARDER TO LABEL
    → Feel-Explanation: often confabulated (no existing narrative template)
    → Benefit: domain-reality-checked (not pre-compiled)

  GRADIENT ACROSS AXES:
    Compiled × Labeled   = Feel-Observation–Feel-Labeling (clear, fast)
    Compiled × Unlabeled = Feel-Observation (recognized but nameless)
    Fresh × Strong       = Feel-Consciousification (noticeable, no label)
    Fresh × Weak         = Feel-Integration (vague, barely there)

  → Detail: Compiled/Fresh axis → Inter-Body-Mechanism.md §3
```

---

## §3 — CORE CLAIM + BODY-FIRST INVARIANT + PFC=LAWYER

### 3.1 Core Claim: Feeling Is Not a Separate System

```
⭐ CORE CLAIM:
  Feeling ≠ separate "emotion system" running in parallel.
  Feeling = observable output of body-chunk interaction.

  4 CONSEQUENCES:

  ① "Thinking vs Feeling" is a false dichotomy.
     → Both use the same system — difference is ATTENTION DIRECTION.
     → "Thinking": PFC attends to chunk patterns, logic.
     → "Feeling": PFC attends to body signals, valence, integrated state.

  ② You cannot turn feelings off — only redirect attention from them.
     → Suppression = PFC not attending to body signals.
     → Signals still fire. Integration still happens. Just below observation.

  ③ "No feeling" is impossible — the loop runs 24/7.
     → "I don't feel anything" = threshold too high, OR signals too weak.
     → NOT absence of feeling. Absence of DETECTION.

  ④ Training feeling = training PFC observation of body-chunk interaction.
     → Lowering threshold. Expanding label vocabulary. Building pattern library.
     → NOT "awakening" a dormant capacity — refining an existing mechanism.
```

### 3.2 Body-First Invariant

```
⭐ BODY-FIRST INVARIANT:
  Body signals fire BEFORE PFC consciously observes.
  This is not a theory — it is a timeline fact.

  TIMELINE:
    T = 0 ms      Body systems fire (muscle tension, heart rate, gut activity...)
    T = 100-200   Signal integration begins (insula, ACC, VMPFC)
    T = 200-300   Signal crosses PFC threshold → "something is happening"
    T = 300-500   PFC pattern-matches → Feel-Observation
    T = 500+      PFC labels, locates, explains → Feel-Labeling, Feel-Explanation

  → PFC does NOT generate feeling. PFC OBSERVES feeling already generated.
  → 🟢 Libet 1983: readiness potential precedes conscious will by ~350ms
  → 🟢 Bechara 1997: galvanic skin response precedes card selection insight by ~10 trials
  → IMPLICATION: When you think you "decided to feel" something —
    you are explaining what body already did.
```

### 3.3 Alexithymia Validates the Definition

```
🟡 ALEXITHYMIA AS VALIDATION:

  Alexithymia = difficulty identifying and describing feelings.
  Spectrum condition, ~10% of population (🟢 Taylor 2000, TAS-20).

  IN THE FRAMEWORK:
  → Alexithymia = PFC observation threshold too high OR label library too sparse.
  → Body signals fire normally. Integration happens normally.
  → PFC simply does NOT observe them (threshold too high) or cannot label (no vocabulary).

  PREDICTION:
  → Alexithymia patients should show NORMAL body responses (GSR, heart rate)
    but IMPAIRED verbal report of feeling states.
  → 🟢 Bird & Cook 2013: alexithymia in autism = interoceptive prediction deficit
  → 🟢 Shah et al. 2016: heart rate interoception impaired in alexithymia

  → VALIDATES: Feeling = PFC observation function. When observation is impaired,
    feeling (as consciously reported) is impaired — even though body signals are present.
```

### 3.4 PFC = Lawyer (Structural Bias)

> v3.0 — integrated from PFC=Lawyer principle. This is a structural property, not an occasional error.

```
⭐ PFC = LAWYER, NOT JUDGE:

  A JUDGE evaluates evidence neutrally → reaches conclusion.
  A LAWYER starts with a conclusion → selects evidence to support it.

  PFC operates more like a lawyer:
  → PFC already has a preferred interpretation (from compiled chunks, social expectations,
    prior narratives, current emotional state).
  → PFC then searches for body signals that SUPPORT this interpretation.
  → PFC de-emphasizes body signals that CONTRADICT it.
  → The resulting Feel-Explanation feels completely true — from inside.

  STRUCTURAL EVIDENCE:
  → 🟢 Gazzaniga (split-brain): Left hemisphere confabulates explanations for
    right-hemisphere-generated actions — with complete confidence.
  → 🟢 Haidt 2001: moral intuitions fire first; "moral reasoning" = post-hoc justification.
  → 🟢 Nisbett & Wilson 1977: people confidently report causes of their behavior
    that experimental evidence shows to be wrong.

  IMPLICATIONS FOR USING THIS FRAMEWORK:
  → Feel-Explanation = starting point, not conclusion.
  → Verify by descending: Feel-Explanation → Feel-Labeling → Feel-Observation → body.
  → Ask body (body vote): does the explanation produce smooth/resist/empty response?
  → Domain reality = final arbiter (§8.3).
```

### 3.5 Feeling Directed at Self = Self-Observation

```
🟡 SAME MECHANISM, DIFFERENT ATTENTION DIRECTION:

  Feeling observing DOMAIN (external):
  → "Something is wrong with this plan."
  → PFC attends to body signals ABOUT external object/situation.
  → Standard feeling operation.

  Feeling observing SELF (internal):
  → "I notice I'm anxious right now."
  → PFC attends to body signals ABOUT own body/state/pattern.
  → = SELF-OBSERVATION (same 7-layer mechanism, attention direction = inward).

  → Self-Observation.md v1.0 = full treatment.
  → Key: Self-Observation is not a different faculty — it is feeling with attention directed inward.
  → §4 Gradient Mức 0-6 in Self-Observation maps onto Feeling's 7-Layer.
```

---

## §4 — SIGNAL INTEGRATION: 3 HUBS + 5-STEP MECHANISM

### 4.1 Three Integration Hubs

```
⭐ 3 INTEGRATION HUBS:

  HUB 1 — ANTERIOR INSULA ("interoceptive cortex"):
  → Receives raw body signals from all channels
  → Integrates multi-source input
  → Primary role: "What is the body state right now?"
  → 🟢 Craig 2002, 2009: "interoceptive cortex" — how the body feels
  → Key property: insula PREDICTS body state (predictive processing)
    → Feeling = prediction error when prediction ≠ reality
    → 🟢 Seth 2013: interoceptive inference model

  HUB 2 — ANTERIOR CINGULATE CORTEX (ACC) ("conflict + salience monitor"):
  → Detects mismatch: prediction vs actual body state
  → Detects conflict: multiple competing chunks
  → Generates "something is off" signal even when specific cause is unclear
  → Role in rightness/wrongness feeling (§7.5)
  → 🟢 Botvinick 2004, Shackman 2011

  HUB 3 — VENTROMEDIAL PREFRONTAL CORTEX (VMPFC) ("value integrator"):
  → Tags body states with value (approach / avoid)
  → Somatic marker function (Damasio)
  → Links chunk to body state for future retrieval
  → 🟢 Bechara 1994, 1997 (Iowa Gambling Task)
```

### 4.2 Five-Step Integration Mechanism

```
🟡 5-STEP INTEGRATION:

  Step 1 — PARALLEL FIRING:
  Multiple body channels fire simultaneously.
  (physical signals + emotional signals + social signals + chunk activations)

  Step 2 — TEMPORAL BINDING:
  Signals occurring within ~100ms window are bound together as "one event."
  → 🟢 Engel 2001: gamma oscillation (~40Hz) as binding mechanism.

  Step 3 — PREDICTIVE MATCHING:
  Insula compares current signals against predicted body state.
  Prediction error = integrated feeling signal (larger error = stronger feeling).

  Step 4 — CONFLICT DETECTION:
  ACC monitors: are there competing patterns? multiple possible interpretations?
  "Something's off" signal generated even before specific conflict identified.

  Step 5 — VALUE TAGGING:
  VMPFC adds approach/avoid tag based on compiled history.
  → Positive match → approach tag → positive valence feeling.
  → Negative/threat match → avoid tag → negative valence feeling.
  → Neutral/unfamiliar → no strong tag → weak or empty valence.

  → Output of 5-step integration = the INTEGRATED SIGNAL that PFC observes.
  → This is what becomes feeling at Feel-Consciousification.
```

---

## §5 — 8-STEP OPERATIONAL FLOW

> Complete step-by-step mechanism. Each step grounded in research; integration = framework synthesis. 🟡

```
⭐ 8-STEP OPERATIONAL FLOW:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ① — BODY SIGNALS FIRE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Body-Need = aggregate of 2 sources:

  SOURCE A — Hardware/sensory-driven:
  → Physical body state signals (hunger, fatigue, pain, temperature, tension)
  → Mirror system (body resonance with others)
  → Hormonal state (cortisol, dopamine, oxytocin levels)

  SOURCE B — Chunk-dynamics-driven:
  → Chunks activating → create "gap" (pattern expects completion)
  → Schema firing → compiled body state
  → Prediction: expected body state not matching actual

  Body-Need = the aggregate gap between current state and expected/needed state.
  → Not a single signal. The integrated pull across all active gaps.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ② — VTA DETECTS DELTA ("something changed")
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ventral Tegmental Area detects CHANGE in body state (delta).
→ Releases dopamine: salience signal, NOT reward signal.
→ Dopamine = "Pay attention — something shifted."
→ NOT: "This is pleasurable." NOT: "Reward received."
→ 🟢 Berridge & Robinson 1998: dopamine = WANTING system, not LIKING system.
→ Purpose: direct attention toward the changed signal.

(Reward happens at step ⑤-⑥, not step ②. See §6.)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ③ — SIGNAL INTEGRATION (3-hub mechanism)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Signals from step ① converge at Anterior Insula + ACC + VMPFC.
5-step integration mechanism runs (§4.2).
Output: single integrated signal with magnitude + valence + conflict-detection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ④ — PFC OBSERVATION THRESHOLD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Integrated signal must cross PFC observation threshold to become a conscious feeling.

  THRESHOLD = VARIABLE (not fixed):
  → Fatigue → threshold RISES (harder to notice signals)
  → Stress → threshold SHIFTS (biased toward threat detection)
  → Mindfulness practice → threshold LOWERS (more signals noticed)
  → Alexithymia → threshold structurally HIGH (chronic underdetection)
  → Trauma flooding → threshold structurally LOW (chronic overdetection)

  IF crosses threshold → Feel-Consciousification: "something is happening"
  IF below threshold → signal undetected. Body still fires. Loop runs below awareness.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ⑤ — CHUNK PATTERN-MATCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PFC matches integrated signal against chunk library.

  STRONG MATCH (compiled chunk, high probability):
  → Immediate Feel-Observation: "I recognize this."
  → Schema fires. Compiled feeling activates. Fast, automatic.

  MODERATE MATCH (partial, familiar pattern):
  → Feel-Observation: "This feels like... X, maybe."
  → PFC holds candidate interpretation. Sends to body for verification.

  WEAK MATCH (multiple low-probability hits):
  → Convergence Zone: "Something... vague direction."
  → Multi-Weak-Signal-Convergence (§7.3).

  NO MATCH (novel input):
  → Feel-Consciousification remains: "Something, but what?"
  → PFC cannot proceed to Feel-Observation without matching chunk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ⑥ — LABEL SEARCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PFC searches for a verbal label — a word or phrase — for the feeling.

  Label found → Feel-Labeling activates → verbal handle available.
  → Label-As-Handle: verbal label opens logic-planning access to the feeling.
  → Logic-planning system can now work WITH this feeling (name it, plan around it).

  Label NOT found → feeling remains at Feel-Observation level.
  → "I feel something but can't say what."
  → Dwelling begins — continued attention without resolution.

  ⚠️ Label ≠ feeling itself.
  → Teaching someone the word "sad" does not create sadness.
  → Having no word for a feeling does not eliminate the feeling.
  → Label = ACCESS HANDLE, not the thing itself.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ⑦ — BODY VOTE ON INTERPRETATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PFC sends candidate interpretation DOWN to body for verification.
Body responds:

  SMOOTH ✅: "Yes — this interpretation fits."
  → Muscles relax slightly. Breathing settles. Sense of coherence.
  → PFC interpretation confirmed. Loop continues to step ⑧.

  RESIST ❌: "No — this interpretation misses something."
  → Body tightens. Sense of "not quite right."
  → PFC discards candidate. Returns to step ⑤ or ⑥ to try again.

  EMPTY ⬜: "Weak signal. Cannot verify."
  → No clear body response to interpretation.
  → May indicate: novel feeling, very subtle signal, or disconnection.

  → Body Vote = quality control mechanism. Not infallible (§8.3), but primary check.
  → 🟢 Gendlin: "resonating" — try label → body votes → smooth = correct.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP ⑧ — ACTION OR CONTINUED PROCESSING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Four possible paths:

  PATH A — Labeled + Smooth:
  → Feeling identified. Body confirmed. Label available.
  → Logic-planning can engage. Action can proceed.
  → "I know I'm anxious about the presentation. Let me prepare."

  PATH B — Labeled + Resist:
  → PFC has a label but body votes "wrong."
  → Return to step ⑤: search for better interpretation.
  → "I said 'angry' but that's not quite it. More like... hurt?"

  PATH C — Unlabeled + Dwell:
  → No label available. Body signals ongoing.
  → Continued attention. Waiting for convergence.
  → "I don't know what this feeling is yet. I'll sit with it."
  → Somatic-Articulation-Loop (Somatic-Articulation-Loop.md) operates here.

  PATH D — Unlabeled + Dismiss:
  → No label. Attention redirects away from signal.
  → Signal continues below PFC observation.
  → Risk: dismissed feelings accumulate → drive behavior without awareness.
```

---

## §6 — REWARD: DOPAMINE ≠ REWARD

> Integrated from Feeling-Mechanism-Deep §4 — definitive statement.

### 6.1 Fundamental Distinction: Wanting ≠ Liking

```
⭐ REWARD = 2-LEVEL MECHANISM:

  LEVEL 1 — DOPAMINE ALERT (VTA):
  → "Something changed — pay attention!" (doorbell)
  → Signal: SALIENCE, not value
  → Motivates SEARCH / WANTING
  → 🟢 Berridge & Robinson 1998: dopamine = WANTING system

  LEVEL 2 — OPIOID REWARD (body-base):
  → "Chunk MATCHES body-need → genuine value confirmed" (the gift behind the door)
  → Signal: actual reward, pleasure, satisfaction
  → Tags chunk as "valuable" → reinforced in future
  → 🟢 Berridge 2003, Fields 2007: LIKING system

  CORTISOL DROP = RELIEF (consequence, not cause):
  → IF threat was pending → resolved → cortisol withdraws → relief bonus
  → IF no threat was pending → opioid only, no relief bonus

  🟢 BERRIDGE EVIDENCE:
  Rats with dopamine blocked → still LIKED sugar, did NOT SEEK sugar.
  Rats with dopamine stimulated → SOUGHT MORE, were NOT MORE PLEASED.
  → Dopamine (wanting) ≠ Opioid (liking). Confirmed.

  MODERN PATHOLOGY EXAMPLE:
  Social media scroll:
  → Dopamine fires (novelty delta = "something changed")
  → NO opioid (no body-need match)
  → = "Wanting without liking" (🟢 Berridge) = seeking behavior without satisfaction
  → = Why you can scroll for hours and feel empty.
```

### 6.2 Reward in the 8-Step Flow

```
🟡 REWARD HAPPENS BETWEEN STEP ⑤ AND ⑥:

  Steps ①-④: signals fire → integrate → cross threshold
  Step ⑤: chunk pattern-match → PFC holds candidate
  ──→ PFC sends chunk DOWN to body-base: "simulate → what does body feel?"
  ──→ Chunk MATCHES body-need → OPIOID release → GENUINE REWARD
  ──→ Chunk DOES NOT MATCH → body "meh" → PFC discards
  Step ⑥: IF reward → "eureka!" / "that's it!" / "yes!"
  Step ⑦: body vote SMOOTH → reinforce
  Step ⑧: chunk tagged "valuable" → strengthened for future

  → REWARD = at body-base checkpoint (between ⑤ and ⑥)
  → NOT at step ② (dopamine ≠ reward)
  → NOT at step ⑥ (label comes AFTER reward, not before)
```

### 6.3 Five Preconditions for Full Reward (Body-Feedback-Precondition)

```
🟡 BODY-FEEDBACK-PRECONDITION — ALL 5 REQUIRED:

  ┌───┬──────────────────────┬──────────────────────────┬──────────────────────────┐
  │ # │ Precondition         │ If Missing               │ Example                  │
  ├───┼──────────────────────┼──────────────────────────┼──────────────────────────┤
  │ 1 │ Directed-Gap         │ No open need → no reward │ Already full → food      │
  │   │ (body-need gap open) │                          │ offered → "not hungry"   │
  ├───┼──────────────────────┼──────────────────────────┼──────────────────────────┤
  │ 2 │ Chunk-Substrate      │ Cannot decode → confusion│ Van Gogh to a non-artist │
  │   │ (sufficient library) │                          │ → "I don't get it"       │
  ├───┼──────────────────────┼──────────────────────────┼──────────────────────────┤
  │ 3 │ Delta-Gate           │ No alert → no attention  │ Routine task → boredom   │
  │   │ (sufficient delta)   │ → no reward              │                          │
  ├───┼──────────────────────┼──────────────────────────┼──────────────────────────┤
  │ 4 │ Match-Range          │ Too alien OR too familiar│ Atonal music = alien     │
  │   │ (Goldilocks — dynamic│                          │ Same song 1000× = boring │
  ├───┼──────────────────────┼──────────────────────────┼──────────────────────────┤
  │ 5 │ Compile-Gate         │ Content OK but cortisol  │ Math learned under fear  │
  │   │ (opioid vs cortisol) │ → avoidance              │ → adult "hates math"     │
  └───┴──────────────────────┴──────────────────────────┴──────────────────────────┘

  "SHOULD reward but DOESN'T" = one precondition missed.
  → Diagnostic tool: identify WHICH precondition failed → targeted intervention.

  PRECONDITION-5 NOTE:
  If chunks were compiled under threat/coercion (cortisol-tagged),
  future activation fires cortisol instead of opioid.
  → Child who learned math under parental pressure:
    math chunks → cortisol (avoidance) rather than opioid (engagement).
  → This can persist into adulthood without intervention.
```

### 6.4 Eureka Model (4 Cases)

```
⭐ EUREKA INTENSITY = f(schemas_resolved × depth × threat_relief):

  ① ARCHIMEDES (threat-present + curiosity):
     → Strong opioid + cortisol DROP = DOUBLE reward
     → "Running out of the bath" level intensity

  ② EINSTEIN (pure cognitive dissonance, no threat):
     → Strong opioid + NO cortisol drop = deep satisfaction, less explosive
     → "I've been thinking about this for years" resolution

  ③ POSITIVE STUDENT (short arc, safe environment):
     → Moderate opioid + minimal threat = "Oh, I get it!" = healthy learning cycle

  ④ NEGATIVE STUDENT (coerced learning, no safe endpoint):
     → Weak/absent opioid + cortisol PERSISTS = NO reward → "I hate this subject"
     → Precondition-5 violated: cortisol-tagged → aversion compiled into chunks

  MICRO-REWARD IN DAILY LIFE:
  → Every small body-need match → micro-opioid → micro-feeling
  → "Finding the right word" → smooth → micro-reward
  → = Continuous micro-rewards = what makes an ordinary day feel meaningful
  → = Why flow states feel rewarding (continuous matches, sustained opioid)

  ⚠️ DOPAMINE-ONLY = EMPTY:
  Social media, clickbait, novelty loops:
  → Dopamine (delta signal) without opioid (no body-need match)
  → = Wanting without liking (🟢 Berridge)
  → = Modern psychological trap: high drive, low satisfaction
```

### 6.5 Evaluative vs Direct-State Reward + 5 Profiles

```
🟡 FEELING SYSTEM OBSERVES BOTH REWARD TYPES:

  The fundamental distinction (§6.1) covers dopamine (wanting) vs opioid (liking).
  A further distinction exists within opioid reward itself:

  EVALUATIVE REWARD (opioid-dependent):
  → Cortical processing → OFC/vmPFC evaluate → opioid release (if match)
  → Covers: insight, beauty, coherence, social approval
  → PFC observes CLEARLY (PFC is in the pathway)
  → VARIES across individuals (hardware, childhood compile context, exposure history)
  → Observed at: Feel-Observation → Feel-Labeling layer

  DIRECT-STATE REWARD (non-opioid pathways):
  → Hardware-level: CT afferents (gentle touch), endocannabinoid (exercise),
    oxytocin (social proximity), serotonin (satiety)
  → Below PFC pathway → PFC observes DIFFERENTLY (body-state shift, not "pleasant")
  → Feels: "comfortable" more than "pleasant" — less dramatic, more foundational
  → LESS variable across individuals = "democratic reward"
  → Observed at: Feel-Integration → Feel-Consciousification layer
  → = WHY exercise "feels good" in a diffuse way vs insight "feels good" in a crisp way


  5 REWARD PROFILES ("flavors" of reward):

  ① SENSORY — body-input matches compiled baseline
     → Good food, beautiful music, pleasant scent
     → Primarily Direct-State reward, simple-to-moderate complexity

  ② COHERENCE — chunk pattern resolves gap/mismatch
     → Insight, "aha", mathematical beauty, theory clicking into place
     → Complex to abstract, Evaluative Reward primary
     → 🟢 Zeki 2014: mathematical beauty activates same mOFC as visual beauty

  ③ SOCIAL — inter-entity chunk interaction
     → Approval, recognition, belonging, feeling seen
     → Both Evaluative (evaluation of social signal) + Direct-State (oxytocin, touch)

  ④ RELIEF — threat resolution, cortisol drop
     → "It's done. Finally." "Safe."
     → NOT opioid primary → cortisol DROP = relief sensation
     → Feeling: "lighter" more than "pleasant"

  ⑤ PREVIEW — anticipated future chunk match
     → "We're going on vacation next week!"
     → Cortical simulation of future state → partial opioid response
     → Fidelity varies by chunk library depth


  REWARD QUALITY = f(4 variables):
  ① Chunk library depth (Precondition-2: enough substrate to decode)
  ② Compile context (Precondition-5: opioid-tagged vs cortisol-tagged chunks)
  ③ Current body state (fatigue, cortisol load, sleep quality)
  ④ Evaluative/Direct-State ratio (individual hardware + developmental history)

  → Full detail: Reward-Signal-Architecture.md v2.1
```

---

## §7 — FEELING GRADIENT: CLEAR ↔ VAGUE

> One of the most important insights: clear feeling and vague intuition are TWO ENDS of the SAME gradient, through the SAME mechanism.

### 7.1 The Gradient (6 Points)

```
⭐ FEELING-INTUITION GRADIENT:

  CLEAR ◄──────────────────────────────────────────► VAGUE

    ①          ②           ③           ④          ⑤          ⑥
  Body        Emotion      Gut         Intuition   Hunch      Pre-
  Signal      (named)      Feeling                 (vague)    monition

  "Pain"      "Sad"        "Stomach    "Something  "I don't   "Something
  "Hot"       "Happy"      says no"    feels off"  know why   feels..."
  "Hungry"    "Scared"                             but..."

  SOURCE:   1 strong    few           many weak   very weak   pre-verbal
  LABEL:    Easy        Medium        Hard        Very Hard   Impossible
  SPEED:    <100ms      100-500ms     500ms-3s    3-30s       hours
  TRUST:    Very high   High          Medium      Variable    Context-dep.

  ⭐ NOT 6 discrete types — CONTINUOUS GRADIENT.
  ⭐ SAME MECHANISM throughout — difference is SIGNAL PROFILE.
```

### 7.2 Three Variables Determine Position on Gradient

```
🟡 3 VARIABLES DETERMINE GRADIENT POSITION:

  ① SIGNAL COUNT:
     Few (1-2) → CLEAR. Many (5-20+) → VAGUE.
     = One voice in a quiet room vs twenty voices at a party.

  ② SIGNAL STRENGTH:
     Strong → CLEAR. Weak → VAGUE.
     BUT: many weak signals CAN CONVERGE → exceed threshold
     = Multi-Weak-Signal-Convergence (§7.3 core concept)

  ③ LABEL AVAILABILITY:
     Label present → CLEARER (verbal handle opens retrieval path)
     Label absent → VAGUER (stuck at Feel-Observation without name)
     Label does NOT change the signal — it changes ACCESS to the signal.

  INTERACTION:
  CLEAR = FEW signals × STRONG × LABELED ("my foot hurts")
  VAGUE = MANY signals × WEAK × UNLABELED
          ("something feels off" = 12+ weak signals × no label)
```

### 7.3 "Vague" = Multi-Weak-Signal-Convergence

```
⭐ MULTI-WEAK-SIGNAL-CONVERGENCE — CENTRAL HYPOTHESIS:

  CLAIM:
  "Vague" feeling = many weak signals converging simultaneously.
  Each chunk fires too weakly for PFC to detect individually.
  BUT collectively → body signal becomes coherent.
  → PFC detects "something" → VAGUE but DIRECTIONALLY CORRECT.

  NOT a malfunction. CORRECT response to complex multi-dimensional input.

  EVIDENCE:
  → 🟢 Tip-of-tongue phenomenon: awareness of convergence WITHOUT label
    (Brown & McNeill 1966) — you know you know it, can't retrieve it
  → 🟢 Incubation effect: unconscious convergence → sudden insight
    (Wallas 1926, Wagner 2004)
  → 🟢 Expert intuition: 10,000+ hours → many weak signals fire coherently
    (Klein 1998) — expert "gut" = multi-weak convergence resolving fast
  → 🟢 Gendlin felt sense: pre-verbal bodily knowing (Gendlin 1978)
    = phenomenological description of Multi-Weak-Signal-Convergence

  IN THE 8-STEP FLOW:
  Step ①: many weak signals fire (many partial chunk activations)
  Step ③: many weak signals CONVERGE at insula + ACC → aggregate crosses threshold
  Step ④: PFC detects "something" but CANNOT isolate specific source
  Step ⑤: SCATTERED match (many partial, no clear winner)
  Step ⑥: label search FAILS
  Step ⑧: → Path C (dwell) or Path D (dismiss)

  "Trust your vague feeling" (in expert domain):
  body detecting REAL pattern that chunk system hasn't formalized yet.
```

### 7.4 Convergence Zone

```
⭐ CONVERGENCE ZONE:

  = Region in semantic space where activation from MANY chunks OVERLAPS
  = NOT a single compiled chunk
  = Intersection of many activation paths — "a crossroads without a street name"

  PROPERTIES:
  ① No label → PFC cannot "grasp" it
  ② No single source → cannot point to specific chunk
  ③ Has a "location" in semantic space (intersection of activation paths)
  ④ Has DIRECTION — approximate sense of "that way"
  ⑤ DYNAMIC — becomes clearer as more chunks fire coherently

  RESOLUTION (how convergence zone becomes explicit knowledge):
  → Attend to it (Gendlin Focusing step 2-3)
  → New chunk COMPILED from convergence zone pattern
  → Feeling was FIRST → chunk comes AFTER
  → = Feeling = PREVIEW of a chunk that doesn't exist yet
  → = "Trust your vague feeling" in your expert domain:
    body detecting a real pattern that vocabulary hasn't caught up to

  RELATIONSHIP TO OTHER CONCEPTS:
  → Gendlin "felt sense" = PHENOMENOLOGICAL description
  → Multi-Weak-Signal-Convergence = MECHANISM producing it
  → ACC "vague detection" = DETECTOR of convergence zone signal
  → Convergence Zone = STRUCTURAL concept tying them together
  → Body-Knowing.md §5: pre-Body-Knowing formalized (3 sub-types)
```

### 7.5 Movement on the Gradient

```
🟡 GRADIENT DYNAMICS — POSITION IS CHANGEABLE:

  MOVEMENT LEFT (vaguer → clearer):
  → More domain experience → more chunks → stronger matches
  → Label learning → verbal handles become available
  → Attention training → lower PFC threshold
  → = WHY expert "intuition" is MORE RELIABLE:
    massive library → resolve fast → what was "vague" becomes "obvious"

  MOVEMENT RIGHT (clearer → vaguer):
  → Novel domain → few chunks → weak matches
  → Fatigue/stress → PFC threshold rises → signals harder to detect
  → Trauma overlay → distorted signals → unreliable reads

  RIGHTNESS/WRONGNESS GRADIENT (same mechanism, different application):
  Certain Wrong → Confident → Mild Unease → Hunch → ??
  "1+1=3"        "code has bug"  "something's off"  "???"
  → ACC detection spectrum applied to right/wrong evaluation
  → Same 6-point gradient operating in the cognitive domain

  → Training = systematically moving left on gradient (see §10)
```

---

## §8 — FEELING QUALITY = f(CHUNK LIBRARY × COMPILE CONTEXT)

> Feeling quality is NOT fixed. It is a function of chunk history — developmental, not innate.

### 8.1 Quality Model

```
⭐ FEELING QUALITY MODEL:

  Quality = f(chunk_library_size × compile_context × current_state)

  ① CHUNK LIBRARY SIZE (in relevant domain):
     Large → many reference points → accurate matches → reliable feeling
     Small → few references → unreliable or absent feeling response
     = Expert vs beginner gut feeling reliability gap

  ② COMPILE CONTEXT — Direction-At-Compile:
     Under curiosity/safety → opioid-tagged chunks → healthy, approach-oriented feeling
     Under threat/coercion → cortisol-tagged chunks → distorted, avoidance-oriented feeling

     5-dimension compile context:
     a) Emotional state at compile (calm / stressed / terrified)
     b) Body state (rested / exhausted / ill)
     c) Social context (supported / isolated / threatened)
     d) Repetition pattern (deliberate practice / forced repetition)
     e) Reward received (opioid / cortisol / mixed)

  ③ CURRENT STATE (modulators):
     Fatigue → threshold rises → quality drops
     Stress → cortisol → bias toward threat detection
     Mood → mood-congruent memory → bias in chunk activation
     (🟢 Bower 1981: sad mood → sad memories more accessible)

  = Feeling quality is NOT innate → DEVELOPMENTAL PRODUCT → CHANGEABLE.
```

### 8.2 Expert vs Beginner

```
🟡 SAME MECHANISM, DIFFERENT LIBRARY:

  EXPERT (10,000+ hours in domain):
  → Massive chunk library → strong probability links → fast convergence
  → "Gut feeling" = FAST chunk match → RELIABLE intuition
  → Firefighter example: "Something's off" → EVACUATE
    (body detected flashover pattern via multi-weak convergence)
  → 🟢 Klein 1998, Chase & Simon 1973 (50,000+ chess patterns)

  BEGINNER (few hours in domain):
  → Small chunk library → weak links → slow/unreliable convergence
  → Convergence zones persist (not enough references to resolve)
  → "Gut feeling" = mostly noise, not signal
  → Student: "Something's off" → cannot identify what → freeze

  WHEN TO TRUST GUT:
  → In your expert domain (large library) → HIGH trust
  → In unfamiliar domain → LOW trust (noise dominates)
  → In domain learned under trauma → DISTORTED (cortisol bias)
  → Under strong emotion → BIASED (mood-congruent activation)

  "Trust your gut" = GOOD advice for domain experts.
  "Trust your gut" = DANGEROUS advice for beginners or in unfamiliar domains.
```

### 8.3 Domain-Checked vs Self-Referencing

```
⭐ SELECTION PRESSURE ON FEELING QUALITY:

  DOMAIN-CHECKED:
  → Chunks compiled from REAL domain experience
  → Domain reality provides FEEDBACK → incorrect chunks corrected over time
  → "Genuine smooth": feeling accurately reflects domain truth
  → Expert scientist: feeling trained by real data → reliable signal

  SELF-REFERENCING:
  → Chunks compiled from INTERNAL loops only (no domain reality check)
  → Incorrect chunks PERSIST (no external feedback to correct them)
  → "False smooth": feeling is smooth but WRONG
  → Conspiracy theorist: feeling trained by internal loops → unreliable
  → Cult member: feeling trained by in-group loops → coherent but disconnected from reality

  HOW TO DISTINGUISH:
  → Domain-Checked: withstands domain testing → still smooth after challenge
  → Self-Referencing: breaks under rigorous testing → resists when challenged by evidence
  → Body vote ALONE is insufficient → body can vote smooth on Self-Referencing feeling
  → Requires: domain reality check alongside body vote

  ⭐ DOMAIN REALITY = FINAL ARBITER:
  → PFC = Lawyer → narrative can be WRONG (§3.4)
  → Body vote = quality controller → BUT can be distorted (§8.4)
  → Domain outcome = FINAL CHECK → no one overrides it
  → Timeline varies: scam (seconds) → childhood schema (10-30 years)
    → But reality ALWAYS arrives

  DUAL CHECK (from Ask-AI.md v3.1 §6.1):
  Step 1: Body feedback = quality controller ("does this feel wrong? → pause")
  Step 2: Domain reality = final arbiter (outcome confirms or rejects)

  → Training MUST include domain feedback, not just "learn to trust your body."
  → "I feel right about this" without domain testing = Self-Referencing trap.
```

### 8.4 Trauma and Distortion

```
🟡 HOW TRAUMA DISTORTS FEELING:

  MECHANISM:
  → Traumatic event → chunks compile under EXTREME physiological state
  → 1 trauma event ≈ 100 neutral repetitions in emotional weight
  → Cortisol-tagged (Precondition-5 violated) + expanded trigger surface

  4 DISTORTION PATTERNS:

  ① FALSE POSITIVE:
     Body signals "DANGER" when safe (core PTSD pattern).
     Old threat-context chunks fire on partial cues.

  ② NUMBING:
     Body dampens signals → threshold rises → miss important signals.
     "I don't feel much" → body protecting from overwhelm.

  ③ MISLABELING:
     Trauma chunk HIJACKS label → wrong interpretation confidently held.
     E.g.: shame labeled as anger (more tolerable label substituted).

  ④ BODY-STATE LOCKED (Direction-At-Compile):
     Old compile direction fires regardless of current context.
     Meeting rooms trigger school anxiety. Conflict triggers childhood fear response.

  RECOVERY (competitive re-linking, Chunk.md §4):
  → NEW experiences → NEW chunks → COMPETE with trauma chunks
  → Over time: new links GROW → old links become RELATIVELY weaker
  → BUT: old links are NEVER deleted → stress can reactivate them
  → 3 update pathways:
    a) Re-association (new context + old trigger)
    b) Novelty hijack (strong new experience)
    c) Therapy reconsolidation (🟢 Nader 2000: reconsolidation window)

  → Feeling quality CAN improve after trauma — requires active intervention.
```

---

## §9 — FEELING LOOP + CHUNK-FEELING BRIDGE

> Chunk system and feeling system = 1 unified system seen from 2 observation angles.

### 9.1 Feeling Loop (Core Framework Loop)

```
⭐ FEELING LOOP:

  ┌────────────────────────────────────────────────────────────┐
  │  BODY SYSTEMS FIRE (body-base + mirror + schema + ...)     │
  │     ↓                                                      │
  │  CHUNK SYSTEM ACTIVATES (probability distribution)         │
  │     ↓                                                      │
  │  INTEGRATION (anterior insula + ACC + VMPFC)               │
  │     ↓                                                      │
  │  FEELING (Feel-Consciousification: becomes noticeable)     │
  │     ↓                                                      │
  │  PFC OBSERVES (Feel-Observation → Feel-Explanation:        │
  │                locate, label, explain)                     │
  │     ↓                                                      │
  │  DRIVE (feeling → motivation direction)                    │
  │     ↓                                                      │
  │  ACTION (execute, or inhibit)                              │
  │     ↓                                                      │
  │  NEW BODY STATE → back to top (loop continues)             │
  └────────────────────────────────────────────────────────────┘

  KEY PROPERTIES:
  ① CONTINUOUS 24/7 (even during sleep, loop runs at reduced level)
  ② MULTI-TIMESCALE: milliseconds (reflex) → seconds → hours → years (trait)
  ③ PARALLEL: multiple loops running simultaneously, interdependent
  ④ SELF-REINFORCING or SELF-CORRECTING:
     Positive → approach action → good outcome → reinforced
     Negative → reactive action → bad outcome → amplified
     Negative → reflective action → correction → loop broken
  ⑤ MULTIPLE ENTRY POINTS: can be interrupted at ANY stage:
     Body (exercise) / Integration (meditation) / Observation (mindfulness)
     / Label (reframing) / Action (behavioral activation) / Environment

  NESTED LOOPS:
  → Imagine-Final Loop (preview feelings before action)
  → Schema Loop (compiled feelings fire from past contexts)
  → Mirror Loop (feeling others → own body)
  → Valence Loop (compiled approach/avoid assessments)
  → Drive Loop (feeling → action direction)
  → Learning Loop (outcome → update → better future feeling)
```

### 9.2 Chunk → Feeling Production Mapping

```
⭐ CHUNK OPERATIONS PRODUCE FEELING LAYERS:

  ┌──────────────────────────┬──────────────────────────────┬──────────────────────┐
  │ Chunk operation          │ Feeling layer produced        │ Mechanism            │
  ├──────────────────────────┼──────────────────────────────┼──────────────────────┤
  │ Body-input signals fire  │ Feel-RawSignals               │ body-base + mirror   │
  │ Signal integration       │ Feel-Integration              │ Insula + ACC + VMPFC │
  │ Crosses PFC threshold    │ Feel-Consciousification       │ Strong enough → PFC  │
  │ Chunk pattern-match      │ Feel-Observation              │ Chunks → context     │
  │ Label search (Label-As-  │ Feel-Location + Feel-Labeling │ Verbal-as-handle     │
  │   Handle)                │                               │                      │
  │ Body vote + PFC explains │ Feel-Explanation              │ PFC narrative (Lawyer│
  └──────────────────────────┴──────────────────────────────┴──────────────────────┘

  ACTIVATION DYNAMICS → FEELING PROPERTIES:
  → Probability distribution → feeling CLARITY
    (strong winner = clear; scattered = vague)
  → Activation SPEED → feeling TIMING
    (fast = instant; slow = delayed recognition)
  → Activation COMPETITION → feeling AMBIVALENCE
    ("happy and sad at the same time" = competing chunks)
  → Trigger surface SIZE → feeling SENSITIVITY
    (large surface = hyper-sensitive; small = low sensitivity)

  COMPILE CONTEXT → FEELING QUALITY:
  → Compiled under safety → accurate, nuanced, approach-oriented
  → Compiled under threat → biased toward threat, avoidance-oriented
  → Rich vocabulary → easy to identify and communicate
  → Poor vocabulary → present but cannot be named
```

### 9.3 Feeling → Chunk Feedback (5 Mechanisms)

```
⭐ FEELING FEEDS BACK INTO CHUNK SYSTEM:

  ① BODY VOTE → LINK STRENGTHENING/WEAKENING:
     Smooth → link probability INCREASES (Hebbian principle)
     Resist → link DECREASES → alternative chunks searched
     = EVERY feeling episode = training data for chunk system

  ② EMOTIONAL STATE → PROBABILITY BIAS:
     Feeling "sad" → sad-compiled chunks BOOSTED → more sad feelings
     = Circular: feeling → chunk bias → same feeling → more bias
     = Explains mood persistence.
     Breaking: external input (strong event) or PFC deliberate intervention.

  ③ VAGUE FEELING DETECTION → CURIOSITY DRIVE:
     Vague feeling → convergence zone → VTA fires → curiosity
     = Feeling DRIVES chunk discovery (Chunk Discovery Lifecycle)

  ④ REWARD FEELING → CHUNK TAGGING:
     Opioid reward → chunk tagged "valuable" → priority in future activation
     Without reward → chunk may decay or become inert

  ⑤ TRAUMA FEELING → CHUNK DISTORTION:
     Extreme negative → cortisol-tagged → avoidance feeling propagates
     Breaking: competitive re-linking via new positive experiences in same domain
```

### 9.4 Body Vote = Meeting Point of Chunk and Feeling Systems

```
⭐ BODY VOTE = WHERE CHUNK AND FEELING SYSTEMS MEET:

  FROM CHUNK SYSTEM PERSPECTIVE:
  → PFC holds candidate interpretation → sends DOWN to body
  → Body simulates: does this chunk match body-need?
  → Body responds: smooth / resist / empty

  FROM FEELING SYSTEM PERSPECTIVE:
  → Body generates integrated feeling → PFC labels it → sends DOWN for verification
  → Body responds: smooth (correct label) / resist (wrong label) / empty (uncertain)

  → SAME MECHANISM, 2 observation angles.
  → 🟢 Gendlin "resonating": try a label → body votes → smooth = both systems agree

  CONVERGENCE ZONE = THE TRANSITION POINT:
  → WHERE feeling system DETECTS what chunk system hasn't COMPILED yet
  → "Vague" = body knows, chunk system doesn't have the name yet
  → Resolution: new chunk compiled → feeling CLARIFIES
  → = Feeling = PREVIEW of a chunk that doesn't exist yet
  → = Dynamic boundary between feeling-knows and chunk-has-named
```

### 9.5 One Unified System

```
⭐ WITH THE BRIDGE — ONE SYSTEM:

  ① FRAMEWORK COHERENCE:
     Any chunk question has a feeling answer.
     Any feeling question has a chunk answer.
     They are the same phenomenon from different vantage points.

  ② PRACTICAL APPLICATIONS:
     Education: "Student doesn't feel motivated."
     → Chunk reading: Precondition-1 not met (no open need)
       OR Precondition-5 violated (cortisol-tagged from prior coercion)
     → Feeling reading: threshold too high at step ④
       OR body resists at step ⑦
     → Same problem, different vocabulary. Same solution.

     Daily life: "I feel off but don't know why."
     → Chunk reading: convergence zone forming
     → Feeling reading: Multi-Weak-Signal-Convergence, gradient points ④-⑥
     → Action: attend convergence zone (Focusing practice) → resolve

  ③ AI COLLABORATION:
     Human: feeling (body vote, convergence zone detection, reward calibration)
     AI: logic (search, analysis, planning, synthesis)
     → Feeling = irreplaceable human input to human-AI collaboration.
     → AI can process logic. AI cannot feel.
```

---

## §10 — FEELING LITERACY + TRAINING (5-STAGE FRAMEWORK)

> Feeling literacy = the most important skill in the AI era.

### 10.1 Literacy Redefined via Chunk Mechanism

```
⭐ FEELING LITERACY — DEFINITION:

  = The ability of PFC to observe body-chunk interaction with HIGH FIDELITY.

  5 FACTORS (each = a chunk system property → each TRAINABLE):

  A) LOW THRESHOLD — detect more signals
     Mechanism: interoceptive prediction training → threshold decreases
     = More signals noticed, more of the feeling gradient accessible

  B) HIGH DISCRIMINATION — distinguish pain/fatigue/sadness
     (rather than lumping everything into "something's wrong")
     Mechanism: chunk library large enough → convergence zones resolve faster

  C) RICH LABEL VOCABULARY — many verbal handles
     Mechanism: Label-As-Handle → more retrieval paths to logic-planning
     = More feelings can be "used" in planning and communication

  D) ACCURATE ATTRIBUTION — correctly mapping signal to source
     Mechanism: sufficient cross-domain chunks → PFC generates better hypotheses
     → body vote narrows to correct one faster

  E) CALIBRATION — knowing which layer to trust in which context
     Mechanism: meta-chunks (chunks ABOUT the feeling process)
     = "I know Feel-Explanation is often wrong when I'm under stress"

  FORMULA:
  Literacy = f(threshold × library_size × label_count × attribution × meta)

  WHAT LITERACY IS NOT:
  ✗ "Listen to your body more" (vague)
  ✗ "Control your emotions" (opposite: literacy = READING, not suppression)
  ✗ "Trust everything your body says" (dangerous: Feel-Labeling and Feel-Explanation often wrong)
  ✗ "Talk more about your feelings" (output ≠ internal accuracy)
  ✗ "An innate trait you either have or don't" (WRONG: trainable via chunk mechanism)
```

### 10.2 AI Era: Feeling = Critical Human Skill

```
⭐ "HUMANS NEED TO FEEL ACCURATELY → AI WILL HELP PLAN ACCURATELY."

  AI = LOGIC AMPLIFIER:
  → AI processes logic better than humans
  → AI has no body → no feeling
  → AI can mimic emotional language → it does NOT have body computation
  → AI can generate plausible-sounding answers → cannot body-vote them

  SPECIFIC SHIFTS IN AI ERA:

  ① DECISION: AI thinks → Human feels → Decide together
     (AI generates options, human body-votes quality)

  ② EVALUATION: Body vote = PRIMARY quality check on AI output
     (AI cannot check its own output against body reality)

  ③ CREATIVITY: Human feels "does this work?" → AI crafts and refines
     (Aesthetic judgment is body-based, not rule-based)

  ④ MEANING: Body-generated, cannot be outsourced
     (What matters to you = your body's answer, not AI's recommendation)

  ⑤ RELATIONSHIP: Human-only territory
     (Mirror system, embodied resonance, genuine presence)

  THE PARADOX:
  → AI makes logic EASIER to access (democratizes cognitive processing)
  → AI makes feeling MORE IMPORTANT (feeling is now the differentiator)
  → AI era also makes feeling HARDER to develop naturally
    (more screen time, less physical engagement, dopamine-without-opioid loops)
  → DELIBERATE literacy training = necessary, not optional.
```

### 10.3 Five-Stage Training Framework

```
⭐ 5-STAGE TRAINING (grounded in chunk mechanism):

  STAGE 1: BODY AWARENESS
  → Goal: lower PFC observation threshold → detect MORE signals
  → Mechanism: interoceptive prediction refinement (Seth 2013),
    attention pathway strengthening, habituation reduction
  → Methods: body scan (MBSR protocol), interoceptive check-in,
    breath awareness practices
  → 🟢 Farb 2013, Lazar 2005 (insula cortical thickening with practice)
  → ⚠️ ALONE insufficient → without Stage 2, can produce overwhelm
    (sensing more but lacking discrimination vocabulary)

  STAGE 2: SIGNAL DISCRIMINATION
  → Goal: distinguish DIFFERENT signals (not just "something's there")
  → Mechanism: feeling chunk library expansion, cross-channel comparison
  → Build: "Is this hunger or anxiety?" "Is this fatigue or sadness?"
  → 🟢 Barrett 2017: emotional granularity → better health outcomes

  STAGE 3: PATTERN RECOGNITION
  → Goal: build body-situation links ("this feeling = this type of situation")
  → Mechanism: pattern chunks compiled via repetition + deliberate attention
  → Example: firefighter's "something's off" = body recognizing flashover pattern
  → = Expert intuition as cultivated skill

  STAGE 4: LABEL ATTACHMENT
  → Goal: verbal handle available → logic-planning access opened
  → Mechanism: Label-As-Handle + Label 3-tier vocabulary development
  → Label opens the door between feeling system and logic-planning system

  STAGE 5: META-FEELING
  → Goal: feelings ABOUT feelings → recursive awareness + calibration
  → "I know I'm angry AND I know Feel-Explanation is often confabulating
    when I'm in this state."
  → = Wisdom: knowing which layer to trust in which context
  → = The difference between emotional reaction and emotional intelligence

  EACH STAGE = CHUNK COMPILE PROCESS. Cannot skip stages permanently.
  CAN train all 5 simultaneously (Gendlin Focusing covers all 5, §10.4).
  Domain-specific: feeling-literate about cooking ≠ feeling-literate about physics.
```

### 10.4 Gendlin Focusing as Integrated Training

```
🟡 FOCUSING = INTEGRATED TRAINING (all 5 stages simultaneously):

  Gendlin Focusing 6 Steps × Chunk Mechanism:

  Step 1 — Clearing a Space:
  → PFC resets, sets aside known concerns → lower threshold (Stage 1)

  Step 2 — Felt Sense:
  → Attend to the whole body sense of an issue → convergence zone (Stage 1+2)
  → The felt sense = Multi-Weak-Signal-Convergence becoming noticeable

  Step 3 — Getting a Handle:
  → Find a word, phrase, image, gesture that fits the felt sense → label search (Stage 4)
  → Label-As-Handle: verbal handle for the felt sense

  Step 4 — Resonating:
  → Take handle back to felt sense → body vote verification (Stage 2+3)
  → Smooth = right. Resist = not quite. Try again.

  Step 5 — Asking:
  → Ask body what it needs, what's central → deeper chunk activation (Stage 3)
  → Body consults further, not PFC theorizing

  Step 6 — Receiving:
  → Accept what body offers → meta-awareness of body truth (Stage 5)
  → Not evaluating what arrived — receiving it

  BODY SHIFT = CONVERGENCE ZONE RESOLVING:
  Before Focusing: vague feeling, many weak signals, no label
  During Focusing: attend → resonate → handle found
  After Shift: body relaxes, feeling CLARIFIES, gradient moves left
  = Convergence zone → newly compiled chunk pattern
  → 🟢 50+ years of clinical validation

  WHY FOCUSING WORKS AT CHUNK LEVEL:
  → Lowers threshold (Stage 1: attention + clearing)
  → Expands library (Stage 2: discrimination in real-time)
  → Builds patterns (Stage 3: body-situation links)
  → Attaches labels (Stage 4: handle step)
  → Develops meta-awareness (Stage 5: receiving step, not evaluating)
  → = Most efficient single practice because it covers ALL 5 stages.
```

### 10.5 Five Failure Modes

```
🟡 5 FAILURE MODES (why feeling training fails — chunk-level explanation):

  ① COGNITIVE OVERRIDE:
     PFC jumps directly to Feel-Explanation → skips body → "I'm fine."
     = Steps ④-⑤ bypassed; steps ⑥-⑧ run without body input.
     Body signals still fire. Just not consulted.

  ② ALEXITHYMIA:
     Threshold permanently raised → miss signals.
     🟢 ~10% of population on spectrum (Taylor 2000, TAS-20)
     Congenital OR acquired (chronic invalidation in development).

  ③ TRAUMA FLOOD:
     Threshold TOO LOW → overwhelm.
     Standard meditation CAN be harmful for trauma survivors.
     Need titrated approach: 🟢 Levine 2010 (Somatic Experiencing).

  ④ CULTURAL SUPPRESSION:
     "Real men don't cry." "Good girls don't get angry."
     Signals detected by body → culturally installed chunk filter → suppressed before report.
     Chunk-level: cultural filter chunks installed → block at Feel-Location/Feel-Labeling.

  ⑤ SELF-REFERENCING TRAP (most dangerous):
     Feeling training WITHOUT domain feedback.
     Process: Train body awareness → learn to "trust the body" →
     body gives smooth vote on Self-Referencing (untested) belief.
     = "I feel right about this" about a conspiracy theory.
     Prevention: ALWAYS include domain feedback alongside feeling training.
     Domain-Checked/Self-Referencing distinction (§8.3) is non-negotiable.
```

---

## §11 — EVOLUTIONARY FRAMING (2M YEARS + 5 MISMATCHES)

### 11.1 Binary Feeling Was Sufficient for 2 Million Years

```
⭐ ANCESTRAL ENVIRONMENT:

  VOCABULARY NEEDED: ~20-50 feeling states sufficient for survival.
  → Binary: POSITIVE (approach) vs NEGATIVE (avoid)
  → + Specific: hunger, thirst, fear, pain, fatigue, temperature extremes
  → + Social: belonging, rejection, love, grief

  WHY IT WORKED:
  → Simple environment. Body-environment ALIGNED.
  → Feeling signals RELIABLE (perceived threat = actual threat, mostly).
  → PFC role MINIMAL: act on feeling → usually correct.
  → = 2 million years: "binary + basic specific feeling = sufficient" ✓
```

### 11.2 Five Modern Mismatches

```
⭐ 5 MISMATCHES REQUIRING UPGRADED LITERACY:

  MISMATCH 1 — ENVIRONMENT:
  Ancient "stress" signal (predator) → now triggered by 8+ modern causes:
  deadline, bills, email, social media, traffic, news, social comparison...
  Body cannot distinguish. Same physiological stress response, radically different causes.
  → Stress signal = vague direction ("something bad") not specific source.

  MISMATCH 2 — DECISION TIMESCALE:
  Ancestral: seconds to hours (flee now? eat this?).
  Modern: months to decades (career? marriage? city to live in?).
  Feeling was not designed for long-horizon decisions.
  → Body vote on 20-year career plan = unreliable indicator of 20-year outcome.

  MISMATCH 3 — CHRONIC vs ACUTE:
  Ancestral: escape predator → rest → cortisol clears.
  Modern: years of deadlines → cortisol without resolution.
  → Cortisol designed for acute use → chronic = physiological damage.
  → Chronic stress pathology = ancestral system running without off-switch.

  MISMATCH 4 — SOCIAL COMPLEXITY:
  Ancestral: 50-150 close relationships (Dunbar's number).
  Modern: thousands of weak ties + social media pseudoconnections.
  Mirror system evolved for face-to-face presence → now fires for avatars.
  → "Lonely in a crowd" = genuine phenomenon, not weakness.

  MISMATCH 5 — INFORMATION OVERLOAD:
  Ancestral: threats were local, actionable.
  Modern: news of distant threats arrives in real time.
  Body treats "earthquake on another continent" like immediate threat.
  → Cortisol mobilization for things you cannot act on → learned helplessness.

  EVOLUTIONARY MISMATCH CONDITIONS (largely products of these 5):
  → Obesity, anxiety disorders, depression, ADHD, chronic pain
  → ALL = body signals that were CORRECT for ancestral environment,
    INAPPROPRIATE for modern conditions

  FRAMEWORK POSITIONING — INTERPRETER BRIDGE:
  → Body still writes messages in ancestral language.
  → This framework = dictionary + translator between ancestral body and modern environment.
  → Body is still correct — modern humans just need to learn to read what it's saying.

  AI ERA:
  → AI outsources cognition (language, logic, pattern search).
  → Human body-based feeling = evolutionary heritage AI cannot replicate.
  → Feeling literacy = irreplaceable human skill in the AI era.
```

---

## §12 — HONEST ASSESSMENT

### 12.1 Confidence Breakdown

```
🟢 HIGH CONFIDENCE — research-established:

  ✓ Body-feeling pipeline exists (Damasio 1994, 1999; Craig 2002, 2009)
  ✓ Anterior insula as interoceptive integration hub (Craig 2002, 2009)
  ✓ ACC as conflict/salience monitor (Botvinick 2004, Shackman 2011)
  ✓ VMPFC role in somatic markers (Bechara 1994, 1997)
  ✓ Body-first temporal order (Libet 1983, Bechara 1997)
  ✓ Dopamine ≠ reward: wanting vs liking (Berridge & Robinson 1998, 2003)
  ✓ Opioid = actual reward/liking (Berridge 2003, Fields 2007)
  ✓ Spreading activation probability-weighted (Collins & Loftus 1975)
  ✓ Mood-congruent memory (Bower 1981)
  ✓ Expert pattern recognition as compressed chunk library (Klein 1998, Chase & Simon 1973)
  ✓ Gendlin felt sense + body shift (Gendlin 1978, 50+ years clinical validation)
  ✓ Interoceptive prediction model (Seth 2013)
  ✓ Meditation → interoceptive accuracy improvement (Farb 2013, Lazar 2005)
  ✓ Emotional granularity → health outcomes (Barrett 2017)
  ✓ Social pain activates physical pain circuits (Eisenberger 2003)
  ✓ Memory reconsolidation window (Nader 2000)
  ✓ Temporal binding via gamma oscillation (Engel 2001)
  ✓ Tip-of-tongue = convergence without label (Brown & McNeill 1966)
  ✓ Trauma disrupts body awareness (van der Kolk 2014, Levine 2010)
  ✓ Alexithymia spectrum (Taylor 2000, TAS-20)
  ✓ Dual process (Kahneman 2011) — framework refines:
    Logic vs Feeling distinction by SOURCE (rule-based vs body-based),
    not by speed alone
  ✓ Split-brain confabulation (Gazzaniga) — PFC constructs post-hoc narratives
  ✓ Moral intuition fires first, reasoning post-hoc (Haidt 2001) [v3.0]
  ✓ People cannot accurately report causes of behavior (Nisbett & Wilson 1977) [v3.0]


🟡 MEDIUM CONFIDENCE — framework synthesis:

  ⚠ 7-layer structure (framework contribution, useful heuristic, not validated taxonomy)
  ⚠ 8-step operational flow (each step grounded independently, integration = framework)
  ⚠ Feeling = PFC observation of body-chunk interaction (consistent reframe, not direct test)
  ⚠ Multi-Weak-Signal-Convergence (consistent with priming research, not directly tested)
  ⚠ Convergence Zone as structural concept (phenomenology via Gendlin, mechanism plausible)
  ⚠ 5 Preconditions (Body-Feedback-Precondition) (each individually grounded, matrix = framework)
  ⚠ Eureka intensity model 4 cases (consistent with stress-reward literature, not directly measured)
  ⚠ Domain-Checked vs Self-Referencing selection pressure (logically follows, not empirically tested)
  ⚠ Quality model f(library × context × state) (factors established, interaction = framework)
  ⚠ Body vote mechanism (consistent with Gendlin, precise mechanism = framework)
  ⚠ 5-stage training framework (each stage grounded, integrated model = framework)
  ⚠ Chunk-feeling bridge as unified system (coherent, formal claim = framework)
  ⚠ 5-mismatch evolutionary framing (plausible evolutionary psychology, not rigorously tested)
  ⚠ Feeling loop as "core framework loop" (framework claim)
  ⚠ AI era → feeling literacy critical (logical argument, empirical prediction about future)
  ⚠ Alexithymia validates "feeling = PFC observation" (Bird & Cook 2013, Shah et al. 2016)
  ⚠ PFC = Lawyer as structural principle for Feel-Explanation
    (consistent with Gazzaniga, Haidt, Nisbett & Wilson; formal principle = framework synthesis)
  ⚠ Compiled/Fresh × 7-Layer mapping (each component grounded independently,
    cross-mapping as unified axis = framework synthesis)
  ⚠ Compilable Architecture → feeling system as consequence (evolution argument, logically sound)
  ⚠ Body-Need 2-source as input to feeling Step ① (consistent with Body-Feedback-Mechanism v2.0)
  ⚠ Domain Reality = Final Arbiter for feeling accuracy (logical principle,
    consistent with Domain-Checked/Self-Referencing; timeline evidence strong but variable)


🔴 LOW CONFIDENCE — hypotheses:

  ⚠ Fidelity percentages per layer (illustrative, not measured)
  ⚠ Exact timing of 8-step flow (approximate, individual variation large)
  ⚠ Precise neural map of convergence zone
  ⚠ Goldilocks zone boundaries for Match-Range (inverted-U established, dynamic per person/context)
  ⚠ DRD4 4R/7R as primary determinant of reward sensitivity
  ⚠ "Micro-reward" continuous opioid concept (plausible, frontier measurement)
  ⚠ Meta-chunk recursive structure (conceptually sound, implementation frontier)
  ⚠ "AI cannot have genuine feeling" (philosophical claim, hard problem of consciousness)
```

### 12.2 Key Falsifiable Predictions

```
⭐ REPRESENTATIVE PREDICTIONS:

  P-F1: Body-first temporal order (broad)
  → Galvanic skin response changes BEFORE verbal report across all domains
  → 🟢 Partially confirmed (Bechara), broader formal test pending

  P-F2: Integration hub damage → feeling impairment
  → Insula damage → reduced interoceptive accuracy → impaired signal detection
  → 🟢 Consistent with lesion literature

  P-F3: Expert library → earlier vague detection
  → Larger domain chunk library → detect vague signals EARLIER + MORE ACCURATELY
  → 🟢 Klein 1998 consistent; formal test framework-specific

  P-F4: Meditation → threshold reduction
  → 8-week mindfulness training → measurable interoceptive improvement
  → 🟢 Farb 2013 supports

  P-F5: Label availability → clarity (NOT content)
  → Teaching feeling vocabulary → clearer reports WITHOUT changing body state
  → 🟡 Barrett 2017 supports indirectly

  P-F6: Trauma compile → Precondition-5 violation pattern
  → Domain learned under threat → adult retrieval fires cortisol + avoidance response
  → 🟢 Math anxiety research supports (Ashcraft 2002)

  P-F7: Dopamine-only → empty feeling
  → Social media scroll → "wanting without liking" = high drive, low satisfaction
  → 🟡 Consistent with Berridge framework

  P-F8: Body vote accuracy (body shift)
  → Correct PFC label → measurable body relaxation
  → 🟢 Gendlin clinical supports; formal measurement = frontier

  P-F9: Domain-Checked vs Self-Referencing divergence
  → Domain-feedback training → more accurate feeling than self-referencing only
  → 🔴 Framework-specific, not yet tested

  P-F10: Eureka intensity = f(schemas × depth × threat relief)
  → Problem solved under threat > problem solved without threat in intensity
  → 🟡 Consistent with stress-reward literature

  (Full prediction inventories: Feeling-Mechanism-Deep.md §7.2,
   Feeling-Literacy-Training.md §7.2, Feeling-Chunk-Bridge.md §5.1)
```

### 12.3 Honest Limits

```
⚠️ WHAT THIS FILE DOES NOT CLAIM:

  ✗ "All feelings are 100% accurate."
  → Feel-RawSignals → Feel-Consciousification = body truth.
  → Feel-Labeling → Feel-Explanation = often wrong (PFC=Lawyer).

  ✗ "PFC is bad and should be suppressed."
  → Modern complexity requires expanded PFC role.
  → The feeling loop NEEDS PFC at Feel-Observation through Feel-Explanation.

  ✗ "Always trust your gut."
  → Domain-Checked → trustworthy. Self-Referencing → misleading.
  → Expert domain → trust. Unfamiliar domain → verify.

  ✗ "Ancestral feelings are always right for modern life."
  → Five mismatches are real. Requires interpretation, not direct acting-on.

  ✗ "Feeling replaces logic in decisions."
  → Logic + Feeling parallel, both required (Logic-Feeling.md).
  → Feeling is quality check; logic is structure.

  ✗ "This framework is complete."
  → 7 companion files add detail. Research is ongoing.

  ✗ "AI can never have genuine feeling."
  → Philosophical claim, hard problem. Framework position based on current
    understanding of embodiment. Open to revision.

  ✗ "This replaces clinical assessment or therapy."
  → Framework is theoretical. Does not replace clinical evaluation or treatment.


  WHAT THIS FILE DOES CLAIM:
  ✓ Feeling is body's way of becoming noticeable to PFC.
  ✓ Feeling is multi-source, integrated body state.
  ✓ PFC accuracy varies — Feel-Consciousification → Feel-Observation more reliable
    than Feel-Labeling → Feel-Explanation.
  ✓ Feeling quality = f(chunk history) — trainable, not innate.
  ✓ Feeling literacy is trainable and valuable.
  ✓ AI era makes feeling literacy more critical, not less.
  ✓ Chunk system and feeling system = one unified system, 2 observation angles.
  ✓ Framework provides useful models: 7-layer, 8-step, gradient, quality.
```

---

## §13 — CROSS-REFERENCES

### 13.1 Within the Feeling/ Folder (7 Companion Files)

```
📚 COMPANION FILES — detail beyond this reference:

  Body-Knowing.md             — WHEN PFC "knows": compiled recognition function,
                                3 directions, formation 5-stage, pre-Body-Knowing
                                3 sub-types, quality 6 dimensions

  Feeling-Sources.md          — WHERE: 10+ source channels, 50+ examples,
                                case study "I love them" decomposed

  Feeling-Accuracy.md         — HOW PFC READS: accuracy spectrum, error modes,
                                pain as special case, literacy development stages

  Feeling-Research.md         — RESEARCH: Damasio, Gendlin, Craig, Panksepp,
                                Barrett + decision-making, expertise, creativity,
                                mental health, AI literature

  Feeling-Mechanism-Deep.md   — HOW (deep): 8-step flow detail, integration
                                mechanism, reward 5-precondition, gradient,
                                Multi-Weak-Signal-Convergence, quality model, 10 predictions

  Feeling-Literacy-Training.md — TRAINING (deep): 5-stage detail, Focusing
                                6-step × mechanism, failure modes, developmental
                                trajectory, AI era, 6 predictions

  Feeling-Chunk-Bridge.md     — BRIDGE (deep): chunk→feeling production mapping,
                                feeling→chunk feedback, integration points,
                                convergence zone as transition, practical applications
```

### 13.2 Framework Dependencies

```
📚 REWARD ARCHITECTURE:

  Reward-Signal-Architecture.md v2.1
  → Evaluative/Direct-State full treatment
  → E₀→E₃ compilation depth
  → 5 Profiles (Sensory/Coherence/Social/Relief/Preview)
  → Compilable Architecture connection (WHY reward system is general-purpose)

  Dissonance-Signal-Architecture.md v1.0
  → Evaluative/Direct-State Dissonance
  → Mismatch Splitting
  → Clinical applications

📚 CHUNK SYSTEM:

  Chunk.md v2.0               — Chunk system central reference (14 sections)
  01b-Chunk-Activation-Dynamics — Probability, re-linking, trigger surface
  01c-Chunk-Discovery-Lifecycle — 7-step discovery cycle, convergence zone,
                                  Domain-Checked vs Self-Referencing
  01-Chunk-Connection-Logical  — 4-type connection taxonomy, body vote mechanism
  02-Feeling-Intuition-Gradient — Multi-Weak-Signal-Convergence, 6-point gradient
  04-Right-Wrong-Vague         — ACC detection, rightness/wrongness spectrum
  05-Insight-Tacit-Upgrade     — Insight mechanism, tacit knowledge surfacing
  03-Reward (Body-Feedback)    — Body-Feedback-Precondition 5 preconditions
  99-Master-Synthesis          — Unified architecture, all hypotheses

📚 INTER-BODY DRILL (v3.0 integrations):

  Inter-Body-Mechanism.md v1.0 — Source-of-truth for drill principles
  → §1: Compilable Architecture → §0 framing (WHY feeling = general-purpose)
  → §2: Body-Need 2-source aggregate → §5 Step ① connection
  → §3: Compiled/Fresh = real axis → §2.5 mapping
  → §7: PFC = Lawyer → §2.3 Feel-Explanation + §3.4 formal section
  → §6.4: Domain Reality = Final Arbiter → §8.3

📚 BODY-FEEDBACK FOLDER:

  Body-Feedback-Mechanism.md v2.0 — Chunk dynamics, 2-source, Body-Need 7 properties
  Body-Feedback-Label.md v2.0     — Vocabulary reference (3-tier labels)
  Gap-Direction.md v2.0           — Gap has direction = f(surrounding chunks)
  Body-Feedback.md v2.0           — Entry point synthesis (10 files, ~16,500 lines)

📚 BODY + CORE:

  Core-v7.5-Draft.md §2           — Body-Base L0+L1 substrate
  Body-Input-Enumeration.md       — Full body input catalog, self-signal keystone
  Neural-Processing-Flow.md       — Hardware pathway: sensor → cortex → binding → PFC
  Body-Dissonance.md              — 14+ specific dissonance signals

📚 PROCESSING + PLANNING:

  Logic-Feeling.md                — Body-Knowing + observer labels (why "Logic"/"Feeling" emerge)
  Logic-Planning.md               — Label 3-tier, AI-assisted planning
  Somatic-Articulation-Loop.md    — Body-knowledge → verbal-knowledge (7-stage loop)
  Imagine-Final.md                — Preview mechanism (preview feelings source)
  PFC-Analysis.md                 — PFC role observing feelings
  Ask-AI.md v3.1                  — Dual Check: body = quality controller, domain = arbiter
  Self-Observation.md v1.0        — Feeling directed INWARD toward self
```

### 13.3 Key Research References

```
📚 CORE REFERENCES (alphabetical):

  Barrett L.F. (2017)              — Emotional granularity, constructed emotion
  Bechara A. (1994, 1997)          — Iowa Gambling Task, somatic markers
  Berridge K. & Robinson T. (1998, 2003) — Wanting ≠ liking, dopamine ≠ reward
  Botvinick M. (2004)              — ACC conflict monitoring
  Bower G. (1981)                  — Mood-congruent memory
  Brown R. & McNeill D. (1966)     — Tip-of-tongue phenomenon
  Chase H. & Simon H. (1973)       — Chess expertise, 50,000+ patterns
  Collins A. & Loftus E. (1975)    — Spreading activation in semantic networks
  Craig A.D. (2002, 2009, 2013)    — Interoception, anterior insula integration
  Damasio A. (1994, 1999, 2010)    — Somatic markers, feeling of self
  Eisenberger N. (2003)            — Social pain activates physical pain circuits
  Engel A. (2001)                  — Temporal binding, gamma oscillation
  Farb N. (2013)                   — Meditation → interoceptive accuracy
  Fields H. (2007)                 — Opioid reward system
  Gazzaniga M.                     — Left hemisphere confabulation (PFC=Lawyer evidence)
  Gendlin E. (1978)                — Focusing, felt sense, body shift
  Haidt J. (2001)                  — Moral intuition first, reasoning post-hoc
  Klein G. (1998)                  — Expert intuition, recognition-primed decision
  Lazar S. (2005)                  — Meditation → insula cortical thickening
  LeDoux J. (1996)                 — Amygdala fast pathway, fear conditioning
  Levine P. (2010)                 — Somatic Experiencing, trauma recovery
  Libet B. (1983)                  — Readiness potential precedes conscious will
  Nader K. (2000)                  — Memory reconsolidation window
  Nisbett R. & Wilson T. (1977)    — Humans cannot accurately report causes of behavior
  Panksepp J. (1998)               — Affective neuroscience, 7 primary systems
  Seth A. (2013)                   — Interoceptive inference, predictive processing
  Taylor G. (2000)                 — TAS-20 alexithymia measurement
  van der Kolk B. (2014)           — The Body Keeps the Score

  (Full citations + extended references: Feeling-Research.md)
```

---

## §14 — STATUS

```
FEELING.MD v3.0 — STATUS:

  English Translation: v1.0, 2026-06-06
  Source Version: Vietnamese v3.0 (updated 2026-05-17)
  Source Lines: ~2,245
  Sections: 15 (§0-§14)

  SOURCE INCORPORATES:
  → Feeling.md v1 — 7-layer structure, feeling loop, body-base, evolutionary framing
  → Feeling-Mechanism-Deep (~1,592 lines) — 8-step flow, reward, gradient, quality
  → Feeling-Literacy-Training (~1,658 lines) — 5-stage, Focusing, AI era
  → Feeling-Chunk-Bridge (~551 lines) — bidirectional mapping, body vote
  → Chunk-Analysis substrate (44+ files, ~48,600 lines)

  CONFIDENCE COUNTS: 23 🟢 + 21 🟡 + 8 🔴
  PREDICTIONS: 10 representative (full inventories in 3 deep files)

  COMPANION FILES (detail beyond this reference):
  → Feeling-Sources.md (WHERE)
  → Feeling-Accuracy.md (HOW PFC READS)
  → Feeling-Research.md (RESEARCH)
  → Feeling-Mechanism-Deep.md (HOW detail)
  → Feeling-Literacy-Training.md (TRAINING detail)
  → Feeling-Chunk-Bridge.md (BRIDGE detail)
  → Body-Knowing.md (WHEN PFC "knows")

  RELATIONSHIP TO CHUNK.MD v2.0:
  → Chunk.md v2.0 = chunk system reference
  → Feeling.md v3.0 = feeling system reference
  → BOTH describe ONE unified system from 2 different observation angles
  → Bridge explicit in §9

  v3.0 CHANGES (source updated 2026-05-17 — Inter-Body Drill Integration):
  → §0: Added Compilable Architecture connection
  → §2.3 Feel-Explanation: PFC=Lawyer as structural integration
  → §2.5 NEW: Compiled/Fresh × 7-Layer mapping
  → §3.4 NEW: PFC = Lawyer formal section
  → §5 Step ①: Body-Need 2-source aggregate framing added
  → §6.5: Reward-Signal-Architecture v2.0 cross-ref, Evaluative/Direct-State added
  → §8.3: Domain Reality = Final Arbiter formal principle + Dual Check
  → §12: 3 new 🟢 + 5 new 🟡
  → §13: Inter-Body section + Body-Feedback section added
```

---

> **END OF Feeling.md v3.0 (English)**
>
> **Summary:**
> §0: Position (unified feedback system + Compilable Architecture origin)
> §1: Definition (FEELING = what PFC sees when observing body-chunk interaction; 7 types; 3 properties)
> §2: 7-Layer Fidelity Gradient (Feel-RawSignals → Feel-Explanation; PFC=Lawyer at top; Compiled/Fresh mapping)
> §3: Core Claim (feeling ≠ separate system; Body-First Invariant; PFC=Lawyer structural bias; Self-Observation connection)
> §4: Signal Integration (anterior insula + ACC + VMPFC; 5-step integration mechanism)
> §5: 8-Step Operational Flow (Body Signals Fire → VTA Delta → Integration → Threshold → Chunk Match → Label Search → Body Vote → Action)
> §6: Reward (dopamine = wanting NOT liking; opioid = liking; 5 preconditions; 4 eureka cases; Evaluative/Direct-State; 5 profiles)
> §7: Feeling Gradient Clear↔Vague (6-point gradient; 3 variables; Multi-Weak-Signal-Convergence; Convergence Zone)
> §8: Feeling Quality (library × compile context × current state; expert vs beginner; Domain-Checked/Self-Referencing; trauma distortion)
> §9: Feeling Loop + Chunk-Feeling Bridge (bidirectional; body vote as meeting point; one unified system)
> §10: Feeling Literacy + Training (5-factor literacy; AI era imperative; 5-stage framework; Gendlin Focusing; 5 failure modes)
> §11: Evolutionary Framing (binary feeling = sufficient for 2M years; 5 modern mismatches)
> §12: Honest Assessment (23🟢 + 21🟡 + 8🔴; 10 predictions; explicit limits)
> §13: Cross-References (7 companion files; framework dependencies; research references)
> §14: Status
>
> **Core insight:** "Humans need to FEEL accurately → AI will help PLAN accurately."
> Chunk system and feeling system = ONE system, 2 observation angles.
> PFC = Lawyer (not Judge) → trust body at Feel-Consciousification → Feel-Observation over Feel-Explanation narrative.
> Domain Reality = Final Arbiter. Body vote = quality controller. PFC narrative = starting point, not conclusion.
