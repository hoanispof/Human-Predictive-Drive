---
title: "Uncanny Valley — Why Humanoid Robots Feel Wrong"
version: v1.1 (English translation)
source: Research/Global/Uncanny-Valley.md v1.1
translated: 2026-06-09
framework: Human Predictive Drive v7.8
---

# Uncanny Valley — Why Humanoid Robots Feel Wrong

> A robot that's clearly a machine (WALL-E) → endearing.
> A real human → normal.
> A robot that's ALMOST human (Sophia, Ameca) → unsettling.
>
> Why is "almost like" worse than "clearly not"?
>
> Research calls this the "uncanny valley."
> The framework explains the underlying mechanism:
> VTC hardware fires "AGENT DETECTED" + Self-Pattern-Modeling simulates → FAILS
> = a specific conflict between 2 systems (detect vs simulate)
> ≠ merely "strange" or "unexpected."
>
> Understanding the mechanism → design robots/AI/avatars that AVOID this valley.
>
> **ANALYSIS FILE** — synthesis from existing mechanisms,
> builds on published neuroscience research.
> Does not replace empirical research — adds a mechanism + design lens.

---

## Table of Contents

- §0 — ABSTRACT + CORE THESIS
- §1 — BACKGROUND: UNCANNY VALLEY RESEARCH (1970 → 2025)
- §2 — FRAMEWORK MECHANISM: VTC–Self-Pattern-Modeling CONFLICT
- §3 — 4-LAYER MODEL: ROBOT / AI / AVATAR
- §4 — WHY "ALMOST HUMAN" IS WORSE THAN "CLEARLY NOT HUMAN"
- §5 — INDIVIDUAL DIFFERENCES + DEVELOPMENT
- §6 — DESIGN PRINCIPLES — FROM MECHANISM TO PRACTICE
- §7 — AI ERA: DEEPFAKE, AVATAR, VIRTUAL AGENT, VTC–Self-Pattern-Modeling CLASSIFICATION
- §8 — fMRI EVIDENCE MAPPING
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES

---

## §0 — Abstract + Core Thesis

```
⭐ CORE THESIS:

  Uncanny valley = VTC–Self-Pattern-Modeling CONFLICT — a clash between 2 systems:

    SYSTEM 1: VTC Hardware Trigger (detects)
      → Detects agent cues (face, body, biological motion)
      → Fires quickly, innate, bypasses PFC
      → Output: "THIS IS AN AGENT"

    SYSTEM 2: Self-Pattern-Modeling (simulates)
      → Uses self-chunks as a template to simulate the entity
      → Compiled: body simulates the entity's state (automatic, cost ≈ 0)
      → Fresh: PFC chains predict the entity's behavior (deliberate, costly)
      → Output: "what this entity is FEELING, what it WILL DO"

    WHEN THE 2 SYSTEMS CONFLICT:
      VTC says: "THIS IS AN AGENT" (face + body + motion cues)
      Self-Pattern-Modeling says: "CANNOT SIMULATE" (motion wrong, expression dead, behavior off)
      → Body-feedback: SPECIFIC dissonance — different from mere "strangeness"
      → Sensation: unease, revulsion, wanting to withdraw

    WHY SPECIFIC (≠ simple unfamiliarity):
      → "Strange" = prediction-delta → explore → compile new chunk → resolve
      → "Uncanny" = VTC–Self-Pattern-Modeling conflict → explore → CANNOT resolve
        (entity is inconsistent — looks like an agent but behaves as non-agent)
      → Delta NEVER resolves → body stuck in dissonance

    PRACTICAL IMPLICATION:
      → Robot/AI design: AVOID the zone where VTC fires but Self-Pattern-Modeling fails
      → Either: clearly machine appearance (VTC doesn't fire fully)
      → Or: behavior good enough for Self-Pattern-Modeling to succeed (mature technology)
      → The zone in between = the valley → avoid it

  Source: Agent-Mechanism.md §14.4 (sketch) + §16.7 (prediction P7)
  This file: deep analysis + mechanism detail + design principles
```

---

## §1 — Background: Uncanny Valley Research (1970 → 2025)

### §1.1 — Mori 1970: The Original Discovery

```
🟢 ESTABLISHED:

  Masahiro Mori (1970) described the phenomenon 不気味の谷 (bukimi no tani):

  X-axis: degree of human likeness (0% → 100%)
  Y-axis: positive emotion (affinity)

  Trajectory:
    0% (clearly a machine)       → neutral
    30% (industrial robot)        → somewhat positive (functional)
    50% (cartoon robot)           → positive (endearing)
    80–95% (android)              → SHARP DROP → revulsion ← UNCANNY VALLEY
    99–100% (real human)          → normal / positive

  "Valley" = the dip between "almost like" and "indistinguishable from"

  Mori observed: corpses, prosthetic limbs, and realistic humanoid robots
  all fall in the zone of "almost like but something's off."

  The original discovery = DESCRIBES the phenomenon.
  Does not explain WHY — that required 50 more years of research.
```

### §1.2 — Survey Data (2024): The General Public Is Uncomfortable

```
🟢 SURVEY DATA:

  United Robotics (2024) — ~8,000 people, 5 countries (USA, France, Canada, Italy, Germany):

  ┌────────────────────────────────────────────────┬──────────┐
  │ Uncomfortable with humanoid robots             │ ~60%     │
  │ Worried robots will replace jobs               │ ~80%     │
  │ Worried robots will replace social interaction │ ~71%     │
  │ Want robots supervised by humans               │ ~79%     │
  │ Feel sufficiently informed                      │ only ~40%│
  └────────────────────────────────────────────────┴──────────┘

  Fear level by country (separate sources, G7 + South Korea/China):

  ┌──────────────┬──────────┬────────────────────────────────────────┐
  │ Country      │ % afraid │ Note                                   │
  ├──────────────┼──────────┼────────────────────────────────────────┤
  │ UK           │ ~52%     │ Highest — least exposure to robots     │
  │ USA          │ ~45%     │ Polarized: 33% positive vs 25% negative│
  │ China        │ ~44%     │ 75% have seen/used real robots         │
  │ South Korea  │ ~29%     │ Lowest — most exposure                 │
  └──────────────┴──────────┴────────────────────────────────────────┘

  Key insights from the data:
    → More exposure → less fear (South Korea: 75% exposure → 29% fear
      vs UK: 30% exposure → 52% fear)
    → BUT ~60% still uncomfortable = the general baseline IS uncomfortable
    → Fear is not just because of unfamiliarity — 44% of Chinese people still afraid
      DESPITE 75% having seen robots
    → Suggests: there is a COMPONENT that doesn't reduce with exposure alone
      (= a mechanism deeper than habituation)
```

### §1.3 — Neuroscience: fMRI Findings (2012–2019)

```
🟢 ESTABLISHED FINDINGS:

  The 3 most important fMRI studies:

  ① Saygin et al. 2012 (PMC3324571) — PREDICTION ERROR:
    → Compared 3 conditions: real human / clearly-machine robot / android (human face + mechanical movement)
    → aIPS (anterior intraparietal sulcus) fired MOST STRONGLY for the android
    → aIPS = region connecting visual cortex (movement processing) with motor cortex
    → Conclusion: brain generates prediction from appearance → behavior violates prediction → error

  ② Rosenthal-von der Pütten et al. 2019 (PMC6697392) — VALUE EVALUATION:
    → vmPFC (ventromedial prefrontal cortex) encodes "like/don't like"
    → vmPFC INCREASED gradually with human likeness → SHARP DROP at uncanny valley
    → vmPFC pattern EXACTLY MATCHED the behavioral uncanny valley curve
    → TPJ (temporoparietal junction) encoded LINEARLY the degree of human likeness
    → FFG (fusiform gyrus) signaled the human/non-human boundary
    → Amygdala fired when REJECTING a gift from an artificial agent
    → Conclusion: TPJ × FFG → vmPFC = multiplicative combination → uncanny valley response

  ③ Cambridge meta-analysis — INDIVIDUAL DIFFERENCES:
    → Amygdala response varies between people
    → Strong rejectors → amygdala fires more strongly
    → Suggests: uncanny valley has an INDIVIDUAL COMPONENT, not just universal


  2 MAIN EXPLANATIONS IN THE LITERATURE:

  A) Prediction error / predictive coding:
    → Appearance → brain predicts behavior → behavior violates → error
    → Strong: explains MISMATCH
    → Weak: doesn't explain why THIS mismatch causes REVULSION
      (ordinary mismatch causes surprise, not revulsion)

  B) Evolutionary / pathogen avoidance:
    → Entity almost-human but "wrong" → brain flags "possibly diseased/deformed"
    → Disgust response = avoid contagion
    → Strong: explains DISGUST component
    → Weak: doesn't explain why only ALMOST-SIMILAR entities trigger this
      (clearly different entities don't trigger it despite also being "abnormal" broadly)

  Framework: builds on BOTH explanations, adds mechanism detail (§2).
```

### §1.4 — Real-World Production: How Robots Have Failed

```
🟢 REAL-WORLD CASES (2024–2025):

  → AIDOL (Russia, 11/2025): humanoid robot fell flat on its face in front of press
    → Parts scattered on impact → uncanny + failure = compound dissonance

  → Unitree (5/2025): first robot boxing match
    → Robot did a full split while trying to kick → human shape + extreme awkwardness

  → Sophia (Hanson Robotics): continuously controversial
    → Facial expressions almost human but timing wrong → classic uncanny valley

  → CGI in film: "The Polar Express" (2004), "Cats" (2019)
    → Realistic but "something's off" → strong negative audience reaction

  Common trend: the more realistic the appearance + the less adequate the behavior
  = the deeper the fall into the uncanny valley.

  Conversely, robots that DON'T look human have succeeded:
  → Roomba (round vacuum robot): very popular, no one is afraid
  → Spot (Boston Dynamics — robot dog): fascination > fear
  → Baymax (Big Hero 6 — round, minimal design): endearing
  → = Evidence: avoid VTC triggers = avoid the uncanny valley
```

---

## §2 — Framework Mechanism: VTC–Self-Pattern-Modeling Conflict

> §2 is where the framework adds mechanistic detail.
> Builds on prediction error (Saygin 2012) + value evaluation (Rosenthal-von der Pütten 2019).
> The framework specifies further: which 2 systems conflict, which 2 functions fail,
> which 3 body-feedback dynamics fire, and why this is agent-specific (≠ general unfamiliarity).

### §2.1 — VTC Hardware Trigger: System 1

```
🟢🟡 VTC = AGENT DETECTION HARDWARE:

  Agent-Mechanism.md §2.3 defines:
    VTC (Ventral Temporal Cortex) hardware provides INNATE TRIGGERS:
    → Face patterns (Spelke core knowledge)
    → Biological motion detection
    → Self-propelled movement
    → Contingent response (entity responds to input)

  VTC does NOT classify "this entity IS an agent" — VTC INVOKES Self-Pattern-Modeling:
    → VTC trigger fires → Self-Pattern-Modeling function is called up on the entity
    → Agent-ness = function output (whether Self-Pattern-Modeling fires or not),
      not a stored property
    → Source: Agent-Mechanism.md §2 (reject binary, accept spectrum)

  WITH A HUMANOID ROBOT:
    → Face pattern: ✅ YES — silicon face, eyes, mouth
    → Body shape: ✅ YES — humanoid body proportions
    → Biological motion: ✅ PARTIAL — gestures almost human but timing wrong
    → Contingent response: ✅ PARTIAL — responds but delayed/off

    → VTC verdict: "AGENT DETECTED — invoke Self-Pattern-Modeling"
    → VTC fires QUICKLY, UNCONSCIOUSLY, without PFC involvement
    → Body is ALREADY PREPARING to interact with an agent BEFORE PFC intervenes

  WITH A CLEARLY-MACHINE ROBOT (Roomba, WALL-E style):
    → Face pattern: ✗ or very weak (minimal, stylized)
    → Body shape: ✗ (round, not humanoid)
    → Biological motion: ✗ (clearly mechanical movement)

    → VTC verdict: "NOT AGENT" or very weak → Self-Pattern-Modeling not invoked fully
    → Brain processes with Layer 1+2 (object chunks + logic) → OK, no conflict

  = VTC hardware trigger IS THE NECESSARY CONDITION for the uncanny valley.
  = If VTC doesn't fire → no conflict → no uncanny.
  = Designing to avoid VTC triggers = avoiding the uncanny valley.
```

### §2.2 — Self-Pattern-Modeling Compiled+Fresh Dual Failure: System 2

```
⚠️ TERMINOLOGY NOTE (v1.1):
  Compiled/Fresh = the COMPILED/FRESH processing axis — NOT "Feeling/Logic" content labels.
  Compiled = body-level simulation, automatic, cost ≈ 0 (Hebbian reinforced)
  Fresh = PFC draft prediction, deliberate, costly (each instance = effort)
  "Feeling" and "Logic" = OBSERVER LABELS for shareability:
    "I FEEL it is sad" (Compiled output) vs "I THINK it will do X" (Fresh output)
    → Same mechanism axis, different CONTENT being described.
  Source: Inter-Body-Mechanism.md §3, Self-Pattern-Modeling v3.0 §1.
```

```
🟡 Self-Pattern-Modeling = SELF-PATTERN-MATCH — simulates an entity using self-chunks:

  Self-Pattern-Modeling.md §0.1 defines:
    Self-Pattern-Modeling = solo forward simulation mechanism.
    Brain retrieves chunks from its own repertoire → applies them as a template for the target entity
    → simulates the target's state → reads output → attributes to target as prediction.

  2 FUNCTIONS RUN IN PARALLEL (Self-Pattern-Modeling §2):

    Compiled — COMPILED (body simulates):
      → "What is this entity FEELING?"
      → Brain retrieves self-chunks: "when I have this expression → I feel X"
      → Applies: "so this entity probably feels X"
      → Output: a weak body-copy of the target's state → a REAL body-level response
      → WITH A ROBOT: expression is almost human → chunks retrieved → BUT response is EMPTY
        (robot has NO internal state → Compiled output = noise, not signal)
      → = Compiled FIRES but OUTPUT IS EMPTY or CONFLICTING

    Fresh — FRESH (PFC chains predict):
      → "What will this entity DO next?"
      → PFC chains: expression X + context Y → predict behavior Z
      → WITH A ROBOT: expression suggests predict Z → robot DOES something else
        (mechanical movements, wrong timing, off response)
      → Fresh prediction is CONTINUOUSLY VIOLATED
      → = Fresh FIRES but is CONTINUOUSLY WRONG

  ⭐ WHY DUAL FAILURE IS DISTINCTIVE:

    Comparison of 3 cases:

    ┌───────────────────┬───────────────┬─────────────┬─────────────────────┐
    │                   │ Compiled      │ Fresh       │ Result              │
    ├───────────────────┼───────────────┼─────────────┼─────────────────────┤
    │ Real human        │ ✅ fires OK   │ ✅ predicts │ Normal              │
    │ Clearly a machine │ ✗ not invoked │ ✅ logic OK │ OK (no conflict)    │
    │ Humanoid robot    │ ⚠ fires→EMPTY │ ⚠ fires→    │ UNCANNY VALLEY      │
    │                   │               │ WRONG       │                     │
    │ Deepfake video    │ ⚠ fires→OFF   │ ✅ predicts │ Mild "something off"│
    │ Corpse            │ ⚠ fires→EMPTY │ ⚠ no predict│ Uncanny + grief     │
    └───────────────────┴───────────────┴─────────────┴─────────────────────┘

    Humanoid robot = THE ONLY CASE where both Compiled AND Fresh fail
    while VTC still says "AGENT"
    → 2 simultaneous failures + 1 positive trigger = compound conflict

  DISTINGUISHED FROM SIMPLE PREDICTION ERROR:
    Saygin 2012 says: "prediction error when appearance ≠ motion"
    The framework adds: prediction error OCCURS IN 2 DIFFERENT FUNCTIONS
    → Compiled error: body simulates → empty (NO state to simulate)
    → Fresh error: logic predicts → wrong (behavior doesn't follow the predicted chain)
    → These 2 error types have DIFFERENT MECHANISMS and DIFFERENT BRAIN AREAS
    → Compiled error ≈ aIPS + somatosensory (body simulation pathway)
    → Fresh error ≈ dlPFC + temporal (logic prediction pathway)
    → Compound effect = why the uncanny valley is more intense than simple "surprise"
```

### §2.3 — Body-Feedback: 3 Dynamics Simultaneously

```
🟡 3 CHUNK DYNAMICS FIRE SIMULTANEOUSLY:

  Body-Feedback-Mechanism.md §3 defines 3 dynamics.
  The uncanny valley activates ALL 3 at once — this is why the intensity is high:

  ① CHUNK-SHIFT (continuous):
    → Body-Feedback-Mechanism.md §3.1: valence changes EVEN THOUGH content stays the same
    → WITH A ROBOT: each micro-gesture → brain shifts prediction → fails → shifts again
    → Example: robot smiles → brain predicts "will say something warm"
      → robot falls silent + turns its head mechanically → shift: "warm" → "strange" → "wrong"
    → CONTINUOUS shift = cognitive + emotional fatigue (never resolves)
    → Different from betrayal (1 big shift): this is MANY small continuous shifts

  ② CHUNK-MISS (repeating):
    → Body-Feedback-Mechanism.md §3.2: a compiled pattern DOES NOT fire
    → WITH A ROBOT: Compiled EXPECTS emotional state → MISS (robot has no state)
    → Lifetime compiled baseline: "human face → HAS internal state"
    → Robot: human face but NO internal state → Chunk-Miss repeating
    → Every time Compiled fires → expects → miss → VTA dopamine SUPPRESSED (Schultz 1997)
    → Notably: miss OF THE AGENT MECHANISM → different from ordinary miss
      (missing "someone is there" is STRONGER than missing "something is there" — Connection ❶)

  ③ PREDICTION-DELTA NEVER RESOLVES:
    → Body-Feedback-Label.md §4: prediction-delta = a separate detection signal
    → Normally: delta → explore → compile new chunk → delta gradually decreases
    → WITH A ROBOT: delta → explore → entity is INCONSISTENT (looks like agent, behaves as non-agent)
      → CANNOT compile a stable chunk ("what IS it?")
      → Delta NEVER fully resolves
      → Body stuck in loop: detect → predict → fail → detect → predict → fail
    → = Form of dissonance loop similar to anxiety (Threat.md §3 anticipation)
      but the trigger is the ENTITY, not a future event

  ⭐ 3 DYNAMICS COMPOUND:

    Chunk-Shift (valence oscillating)
    + Chunk-Miss (agent state absent)
    + Unresolvable delta (cannot compile)
    = COMPOUND DISSONANCE — each dynamic AMPLIFIES the intensity of the others

    Body-Feedback-Mechanism.md §4:
      "Compound does NOT accumulate linearly — they INTERACT."
    → Shift + Miss + unresolvable = why the uncanny valley causes
      REVULSION (disgust) not merely DISCOMFORT
```

### §2.4 — Hardware Social Drive Frustrated: Connection ❶

```
🟡 A 4TH LAYER — WHERE THE FRAMEWORK ADDS VALUE:

  Connection.md §0 defines the 3 Generative Primitives:
    ❶ HARDWARE — Body NEEDS social input like food/water
    ❷ Self-Pattern-Modeling (Compiled+Fresh) — simulates agents
    ❸ PER-AGENT VALENCE — body evaluates the agent

  ❶ HARDWARE SOCIAL DRIVE + THE UNCANNY VALLEY:

    Foundational evidence (🟢):
    → Social Baseline Theory (Coan 2015): body defaults to EXPECTING someone nearby
    → Social pain = physical pain (Eisenberger 2003): dACC + anterior insula
    → Loneliness mortality (Holt-Lunstad 2015): chronically lonely ≈ 15 cigarettes/day
    → Social Brain Hypothesis (Dunbar 1998): neocortex size ~ group size

    WITH A HUMANOID ROBOT:
    → VTC fires "AGENT" → ❶ hardware social drive ACTIVATES
    → Body prepares to receive social input (cortisol lowers, approach cues)
    → BUT: robot does NOT deliver real social input
      (no internal state → Compiled empty → body receives NOTHING)
    → = Social hunger that goes UNFED

    Analogous mechanism:
    → You call your best friend → the voice sounds human → body prepares for connection
    → You discover it's an automated answering machine → DISAPPOINTMENT + mild irritation
    → A humanoid robot = the extreme version of that experience:
      body prepares FULLY (visual + auditory + somatic) for a social encounter
      → receives = ZERO real social input

    WHY THIS LAYER MATTERS:
    → Prediction error (Saygin) explains MISMATCH
    → Pathogen avoidance explains DISGUST
    → But: the uncanny valley also causes SPECIFIC UNEASE — a kind of
      "loneliness in the presence of something"
    → = ❶ hardware social drive frustrated = explains that component
    → Body "knows" "this is not a real social partner" DESPITE VTC saying "agent"
    → = Internal conflict: hardware says "approach" + body says "empty"

  ⚠️ No direct empirical test of this claim yet (🔴).
  But consistent with:
    → Eisenberger 2003 (social pain pathway)
    → Survey data: 71% worried robots will replace social interaction
    → Anecdotal: robot companion users report "close but still lonely"
```

### §2.5 — Per-Agent Valence Cannot Compile

```
🟡 THE EVALUATION SYSTEM GETS STUCK:

  Valence-Propagation.md §1 defines:
    V = body's evaluation: how does THIS entity affect my body channels?
    V = multi-channel (NOT a single good/bad axis)
    V = dynamic, changes with experience
    V = compiled → body responds IMMEDIATELY

  WITH A HUMANOID ROBOT — VALENCE CANNOT COMPILE:

    Visual channel:              "looks human" → approach cue (+)
    Motion channel:              "not human" → cautious cue (-)
    Self-Pattern-Modeling Compiled channel: "can't read state" → threat cue (--)
    Self-Pattern-Modeling Fresh channel:    "prediction continuously wrong" → unreliable cue (-)
    ❶ Social channel:            "looks like social partner" → approach cue (+)
    ❶ Social reality:            "doesn't deliver social input" → frustration cue (--)

    → Multi-channel CONFLICT: + and - SIMULTANEOUSLY on the SAME entity
    → Body CANNOT compile stable valence
    → Valence oscillates: approach ↔ avoidance ↔ approach ↔ avoidance
    → = Amygdala fires (rejection signal) — consistent with Rosenthal-von der Pütten 2019

  DISTINGUISHED FROM ORDINARY ENTITIES:

    A good person: valence compiles → positive → approach → stable
    An enemy: valence compiles → negative → avoid → stable (even if negative, STABLE)
    An object: valence = neutral/functional → stable

    An uncanny robot: valence DOESN'T compile → UNSTABLE
    → Body continuously tries to compile → fails → tries again → fails
    → = Why the discomfort PERSISTS (doesn't habituate easily)
    → = Why China data: 44% still afraid DESPITE 75% having seen robots
      (exposure helps SOMEWHAT but the core conflict is NOT yet resolved)

  COMPARED TO vmPFC DATA:
    Rosenthal-von der Pütten 2019: vmPFC increases gradually with humanlikeness
    → SHARP DROP at uncanny valley → recovery near 100%
    → Framework mapping: vmPFC = value evaluation = valence compilation
    → DROP = body CANNOT compile stable valence for this entity
    → Recovery = when entity is similar enough → Self-Pattern-Modeling succeeds
      → valence compiles → OK
```

---

## §3 — 4-Layer Model: Robot / AI / Avatar

```
🟡 AGENT-MECHANISM.MD §3 — 4-LAYER MODEL APPLIED TO ROBOT/AI:

  Every entity is processed by the brain through 4 layers:
    Layer 1 — Object Chunks (physical + semantic properties)
    Layer 2 — Logic Processing (rules-based prediction)
    Layer 3 — Modeling Overlay (Self-Pattern-Modeling invoked — optional)
    Layer 4 — Schema Override (cultural/personal schema)

  The uncanny valley occurs when: Layer 3 IS INVOKED but FAILS.
  Below: analysis of 7 common entity types in the AI era.
```

### §3.1 — Analysis of 7 Entity Types

```
  ┌────────────────────────┬────────────────┬────────────────┬────────────────┬─────────────────┬──────────────────┐
  │ Entity                 │ L1 Object      │ L2 Logic       │ L3 Self-Pattern│ L4 Schema        │ Uncanny?         │
  │                        │                │                │ -Modeling      │                  │                  │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ① Vacuum robot         │ ✅ machine     │ ✅ OK          │ ✗ not invoked  │ "tool"           │ ✗ NO             │
  │   (Roomba)             │ round          │ moves→bumps→   │ VTC doesn't    │                  │ Can be liked     │
  │                        │                │ turns          │ fire agent     │                  │                  │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ② Robot dog            │ ✅ dog         │ ✅ OK          │ ⚠ partial      │ "robot pet"      │ ⚠ MILD           │
  │   (Spot)               │ 4 legs         │ movement       │ some agent     │ familiar from    │ Fascination      │
  │                        │                │ predicted      │ cues but not   │ media            │ > fear           │
  │                        │                │                │ humanoid       │                  │                  │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ③ Realistic humanoid   │ ✅ human       │ ⚠ fails        │ ⚠ invoked →   │ CONFLICT:        │ ✅ STRONG        │
  │   (Sophia, Ameca)      │ face, body     │ predict contin-│ Compiled EMPTY │ "human" vs       │ UNCANNY          │
  │                        │                │ uously wrong   │ Fresh WRONG    │ "machine"        │ VALLEY           │
  │                        │                │                │                │ unresolved       │                  │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ④ Stylized cartoon     │ ✅ simple      │ ✅ OK          │ ⚠ Schema-      │ "entertainment   │ ✗ NO             │
  │   character            │ drawn lines    │ within film    │ Imagined-Over- │ character"       │ Can be loved     │
  │   (Pixar, Ghibli)      │                │ context        │ lay fires fully│                  │ (parasocial)     │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ⑤ Text AI avatar       │ ✗ no body     │ ✅ OK          │ ⚠ partial      │ "AI tool" or     │ ✗ NO             │
  │   (ChatGPT, Claude)    │                │ text predicted │ via text some  │ "virtual friend" │ But different    │
  │                        │                │                │ Fresh fires    │ depending on     │ risk (§7)        │
  │                        │                │                │                │ user             │                  │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ⑥ Deepfake video       │ ✅ real person │ ✅ OK          │ ✅ fires OK     │ CONFLICT:        │ ⚠ WHEN           │
  │                        │ (copy)         │ because looks  │ enough human   │ "person" →       │ DISCOVERED fake  │
  │                        │                │ like a real    │ similarity     │ "fake" when      │ → STRONG         │
  │                        │                │ person         │                │ discovered       │ Chunk-Shift      │
  ├────────────────────────┼────────────────┼────────────────┼────────────────┼─────────────────┼──────────────────┤
  │ ⑦ Future robot         │ ✅ human       │ ✅ OK          │ ✅ fires OK     │ "humanoid"       │ ✗ CROSSED IT     │
  │   (behavior adequate)  │ realistic      │ prediction     │ Both Compiled  │ new chunk        │ = Valley         │
  │                        │                │ correct        │ + Fresh succeed│ compiled         │ crossed          │
  └────────────────────────┴────────────────┴────────────────┴────────────────┴─────────────────┴──────────────────┘


  ⭐ INSIGHTS FROM THE TABLE:

  → The uncanny valley ONLY occurs when L3 is INVOKED but FAILS (row ③)
  → If L3 is not invoked (①②④): no uncanny, even if the entity is "strange"
  → If L3 invoked + succeeds (⑦): no uncanny, even if the entity is a robot
  → Deepfake (⑥) = special case: uncanny ONLY when discovered as "fake"
    (before that, L3 succeeds because the visual is good enough → discovery = strong Chunk-Shift)
  → Text AI (⑤) = no uncanny because there is NO visual VTC trigger
    (but there's a different risk — §7: anthropomorphization without body-check)

  → DESIGN: place the entity in rows ①②④ OR row ⑦.
    AVOID row ③. That is the valley.
```

---

## §4 — Why "Almost Human" Is Worse Than "Clearly Not Human"

```
🟡 THE PRECISE MECHANISM — 4 REASONS:

  REASON 1 — VTC TRIGGER THRESHOLD:

    VTC fires "agent" based on PATTERN-MATCHING cues:
    → Below threshold (0–50% human-like): VTC doesn't fire or fires very weakly
    → Above threshold (~70–95%): VTC fires STRONGLY → Self-Pattern-Modeling invoked →
      BUT Self-Pattern-Modeling fails
    → Near 100%: VTC fires + Self-Pattern-Modeling succeeds → OK

    "Clearly not human" = below VTC threshold → Self-Pattern-Modeling not invoked → no conflict
    "Almost human" = above VTC threshold → Self-Pattern-Modeling invoked → fails → CONFLICT
    = The problem is not "strangeness" — the problem is CROSSING the threshold but NOT FULLY


  REASON 2 — A LIFETIME OF COMPILED BASELINE:

    Across a lifetime, the brain compiles an extremely strong baseline:
    → "A human face = HAS an internal state"
    → "Expression X = state Y"
    → "Gesture A → behavior B next"

    Compiled through millions of interactions → Hebbian wired EXTREMELY STRONGLY
    → A humanoid robot activates this ENTIRE baseline
    → Then violates it → Chunk-Miss mechanism: actual < compiled baseline → dissonance
    → The stronger the baseline (= lifetime) → the more painful the miss
    → = SNC effect (Crespi 1942): sucrose 32% → 4% = worse THAN the group that only ever knew 4%

    "Clearly not human" = baseline not activated → no miss
    "Almost human" = baseline STRONGLY activated → then miss → LARGE dissonance


  REASON 3 — PREDICTION UNRESOLVABLE:

    Normal "strange": prediction-delta → explore → compile new chunk → delta decreases
    Example: first time seeing a kangaroo = strange → observe → compile → becomes normal

    Humanoid robot: delta → explore → entity is INCONSISTENT
    → Cannot compile a stable chunk:
      "Is it a person?" → No (mechanical movements)
      "Is it a machine?" → No (human face)
      "What category is it?" → No category fits
    → = Category confusion — brain has NO chunk for "agent that looks human but isn't"
    → Every interaction = prediction fails AGAIN
    → Delta accumulates instead of resolving

    "Clearly not human" = easy to compile: "this is a machine" → done
    "Almost human" = CANNOT compile → stuck


  REASON 4 — SOCIAL PROMISE BROKEN:

    Entity looks human → ❶ hardware social drive activates
    → Body expects REAL social interaction
    → Receives: nothing (robot doesn't deliver social input)
    → = Social promise raised then broken

    "Clearly not human" = ❶ NOT activated → no promise → no disappointment
    "Almost human" = ❶ STRONGLY activated → large promise → large disappointment

    → Explains why 71% worry about robots replacing social interaction:
      not just worry about function — worry about social need being deceived


  SUMMARY: 4 REASONS = 4 INDEPENDENT MECHANISMS CONVERGING SIMULTANEOUSLY

    "Almost human" triggers ALL 4 mechanisms at once.
    "Clearly not human" triggers NONE of them.
    = Uncanny valley is NOT a linear function (≠ "more similar → more uncomfortable")
    = Uncanny valley is a THRESHOLD phenomenon — cross the threshold → compound fire
```

---

## §5 — Individual Differences + Development

### §5.1 — Developmental Trajectory

```
🟡 FRAMEWORK PREDICTION (from Agent-Mechanism.md §13 + Self-Pattern-Modeling §7):

  STAGE 0–1 (0–12 months):
    → VTC hardware trigger active
    → Self-Pattern-Modeling not yet functional (insufficient self-chunks)
    → PREDICT: infants DO NOT HAVE an uncanny valley response
    → BECAUSE: no Self-Pattern-Modeling yet → no VTC–Self-Pattern-Modeling conflict
    → Infants may look at a humanoid robot the same way they look at any
      face-bearing stimulus

  STAGE 2–3 (14 months – 7 years) — ANIMISM:
    → Self-Pattern-Modeling online but NOT YET calibrated on threshold
    → Children fire Self-Pattern-Modeling onto EVERYTHING (stuffed animals, cars, the moon)
    → PREDICT: children ages 2–7 are LESS AFRAID of humanoid robots than adults
    → BECAUSE: Self-Pattern-Modeling fires WITHOUT DISTINGUISHING → robot = "one more entity with a state"
    → Children may treat robots as play companions (consistent with real-world observation)
    → Uncanny valley REDUCED because Self-Pattern-Modeling hasn't been refined
      enough to detect the failure

  STAGE 4+ (7+ years) — CALIBRATED:
    → Self-Pattern-Modeling has refined its agent/non-agent boundary
    → Humanoid robot = VTC fires + Self-Pattern-Modeling fails = CONFLICT EXISTS
    → PREDICT: uncanny valley sensitivity INCREASES with age (up to calibration level)

  STAGE 6+ (adult, COMPILED):
    → Self-Pattern-Modeling library deeply compiled → predictions MORE ACCURATE
    → MISMATCH is clearer → uncanny valley CAN BE stronger
    → BUT: adults also have Schema Override (Layer 4)
      → Knowing "this is a robot" → schema helps interpret → reduces dissonance
      → = Why adults respond MORE COMPLEXLY than children
        (afraid + aware + rationalizing simultaneously)

  ⚠️ No longitudinal study directly testing this trajectory yet (🔴).
  But consistent with:
    → Piaget animism phase (2–7 years) 🟢
    → Children generally prefer robots more than adults (anecdotal + classroom data)
    → False belief task ~4 years = Self-Pattern-Modeling cognitive function coming online 🟢
```

### §5.2 — Individual Differences

```
🟡 4 FACTORS CREATING DIFFERENCES:

  ① Self-Pattern-Modeling LIBRARY DEPTH:
    → People with deep Self-Pattern-Modeling library (many interactions) → more accurate predictions
    → Mismatch is CLEARER → uncanny valley CAN be stronger
    → EXAMPLE: actors, psychologists = rich Self-Pattern-Modeling library → detect mismatch faster
    → But CAN ALSO be less afraid because they understand the mechanism (meta-awareness)

  ② CULTURE + EXPOSURE:
    → Survey data: South Korea 29% afraid vs UK 52%
    → South Korea: 75% have seen/used robots → compiled chunk "humanoid robot"
    → UK: 30% exposure → chunk NOT YET compiled → each encounter = novel + uncanny
    → Exposure helps compile new chunks:
      "humanoid robot = entity type X, behaves like Y, no need to be afraid"
    → This chunk NEUTRALIZES the VTC–Self-Pattern-Modeling conflict (Layer 4 schema assists)
    → BUT: 44% of Chinese people STILL afraid despite 75% exposure
      → Schema helps but does NOT resolve 100% of the core mechanism
      → VTC–Self-Pattern-Modeling conflict still fires — only reduces intensity

  ③ SCIENCE FICTION SCHEMAS:
    → 1 century of SF films (Terminator, Ex Machina, Blade Runner, Westworld)
    → Compile schema: "humanoid robot = DANGEROUS"
    → Layer 4 schema INCREASES threat evaluation
    → Framework predicts: heavy SF viewers → uncanny valley STRONGER
    → Because: "dangerous robot" schema compounds with VTC–Self-Pattern-Modeling conflict
    → Conversely: viewers of positive robot media (WALL-E, Big Hero 6)
      → schema "robot = friend" → may REDUCE uncanny
      (but only for non-realistic robots)

  ④ ALEXITHYMIA + Self-Pattern-Modeling QUALITY:
    → Bird & Cook 2013: alexithymia → poor self-reading → poor Self-Pattern-Modeling
    → PREDICT: people with alexithymia → uncanny valley DIFFERS
    → Possibly: less uncanny (Self-Pattern-Modeling doesn't fire strongly → less conflict)
    → Or: uncanny but CANNOT LABEL IT (discomfort without explanation)
    → Amygdala data (Rosenthal-von der Pütten 2019): individual differences clear
      → Consistent: Self-Pattern-Modeling quality differs → amygdala response differs

  ⚠️ Most predictions in §5.2 not yet directly tested (🔴).
  The framework provides falsifiable predictions — needs empirical work.
```

---

## §6 — Design Principles — From Mechanism to Practice

> §6 derives design principles FROM the mechanisms in §2–§5.
> Each principle = 1 mechanism mapping → 1 specific guideline.
> Applies to: physical robots, AI avatars, CGI characters, virtual agents.

### §6.1 — Congruence Principle: Match Appearance ↔ Behavior

```
⭐ PRINCIPLE 1 — CONGRUENCE:

  Source mechanism (§2.2):
    Uncanny valley = VTC detects agent + Self-Pattern-Modeling fails
    Self-Pattern-Modeling fails BECAUSE: appearance suggests predict X → actual behavior = Y ≠ X
    = MISMATCH between appearance prediction and behavior reality

  PRINCIPLE:
    An entity's appearance must MATCH its behavioral capability.
    How human it looks → how human it must behave.
    If the technology isn't ready for human-like behavior → appearance MUST be reduced.

  APPLICATION:

    ┌────────────────────────────┬────────────────────────────┬──────────────────────────┐
    │ Behavioral capability      │ Appropriate appearance     │ Appearance to AVOID      │
    ├────────────────────────────┼────────────────────────────┼──────────────────────────┤
    │ Mechanical gestures,       │ Clearly a machine          │ Realistic human face     │
    │ slow responses             │ (simple shape)             │                          │
    ├────────────────────────────┼────────────────────────────┼──────────────────────────┤
    │ Smooth gestures but        │ Cartoon / stylized         │ Silicon skin             │
    │ limited expressions        │ (Baymax, Pepper)           │ realistic eyes           │
    ├────────────────────────────┼────────────────────────────┼──────────────────────────┤
    │ Smooth gestures +          │ Semi-realistic             │ 100% realistic           │
    │ diverse expressions        │ (anime-style 3D)           │ (not yet good enough)    │
    ├────────────────────────────┼────────────────────────────┼──────────────────────────┤
    │ Nearly indistinguishable   │ Realistic OK               │ —                        │
    │ from a real human          │ (crossed the valley)       │                          │
    └────────────────────────────┴────────────────────────────┴──────────────────────────┘

  SUCCESSFUL CASE STUDIES:
    → Baymax (Big Hero 6): simple behavior + simple appearance = CONGRUENT → beloved
    → Pepper (SoftBank): limited behavior + cartoon appearance = CONGRUENT → acceptable
    → Roomba: machine behavior + machine appearance = CONGRUENT → popular

  FAILED CASE STUDIES:
    → Sophia: limited behavior + realistic appearance = INCONGRUENT → uncanny
    → "Cats" (2019): actor behavior + almost-human CGI = INCONGRUENT → disgusting
    → "Polar Express" (2004): motion capture behavior + dead CGI eyes = INCONGRUENT → disturbing
```

### §6.2 — VTC Management: Deliberately Controlling Agent Cues

```
⭐ PRINCIPLE 2 — VTC MANAGEMENT:

  Source mechanism (§2.1):
    VTC fires based on: face pattern, body shape, biological motion, contingent response.
    VTC fires = Self-Pattern-Modeling invoked = POSSIBLE conflict.
    VTC doesn't fire = Self-Pattern-Modeling not invoked = NO conflict.

  PRINCIPLE:
    DELIBERATELY CONTROL: whether VTC fires or doesn't fire.
    If you want the entity treated as a TOOL → reduce VTC cues.
    If you want the entity treated as a COMPANION → must ensure Self-Pattern-Modeling succeeds.

  REDUCE VTC CUES (entity = tool):
    → Don't use a realistic human face → use LED indicators, abstract display
    → Don't use a humanoid body → use functional shape (round, square, modular)
    → Don't simulate biological motion → use clearly mechanical, smooth, predictable movement
    → Don't simulate voice inflection → use consistent tone, clearly synthesized
    → EXAMPLES: Roomba, industrial robots, drones

  INCREASE VTC CUES (entity = companion) — ONLY WHEN behavior is adequate:
    → Use face, body, voice — BUT must match behavior (§6.1 congruence)
    → ONLY WHEN technology is ready:
      diverse expressions + natural timing + contingent responses + smooth motion
    → If not yet ready → USE STYLIZED instead of realistic (§6.1)

  DANGER ZONE (must avoid):
    → Realistic face + humanoid body + behavior not yet adequate
    → = VTC fires STRONGLY + Self-Pattern-Modeling fails = the valley
    → Especially: eyes are the STRONGEST VTC trigger
      (face perception begins with eyes — Spelke core knowledge)
    → Dead/uncanny robot eyes = strongest VTC trigger + emptiest Compiled response
    → → If you can't make good eyes yet → DON'T make realistic eyes
```

### §6.3 — Self-Pattern-Modeling-Friendly Design: Predictable, Readable

```
⭐ PRINCIPLE 3 — Self-Pattern-Modeling-FRIENDLY:

  Source mechanism (§2.2, §2.3):
    Self-Pattern-Modeling fails → Compiled empty + Fresh wrong → continuous Chunk-Miss + Chunk-Shift
    Self-Pattern-Modeling succeeds → Compiled has signal + Fresh predicts correctly → OK

  PRINCIPLE:
    Design robot BEHAVIOR so that Self-Pattern-Modeling CAN succeed
    (even if the entity is clearly not human).

  3 DIMENSIONS OF Self-Pattern-Modeling-FRIENDLY DESIGN:

    A — PREDICTABLE (Fresh can predict):
      → Behavior patterns STABLE, rule-following
      → If robot turns its head, must give a CUE first (look in that direction, or indicator)
      → DON'T change behavior suddenly without context
      → Analogy: a familiar person = predictable → comfortable (even if not exciting)

    B — READABLE (Compiled can read):
      → Current state CAN BE INFERRED from external cues
      → If robot is "processing" → clear indicator (light, animation, sound)
      → DON'T stay silent + motionless (= ambiguous state → Compiled output is empty)
      → Analogy: a person with clear expressions = easy to read → Self-Pattern-Modeling succeeds → comfortable

    C — CONTINGENT (feedback loop functioning):
      → Robot RESPONDS to user input
      → Response must MATCH the context (user expresses sadness → robot doesn't smile)
      → Contingent response = innate VTC trigger (Spelke)
        → good contingency = body feels "this entity responds to me"
        → wrong contingency = VTC fires + response mismatch = uncanny increases

  APPLICATION EXAMPLES:
    → Companion robot: add "breathing" animation → readable idle state
    → Service robot: LED indicator when processing → predictable wait time
    → Social robot: head tracking follows the speaker → contingent + readable
    → AVOID: silent and still + sudden movement (= ambiguous → sudden = startle + uncanny)
```

### §6.4 — Schema Provision: Help Compile the "Robot" Chunk

```
⭐ PRINCIPLE 4 — SCHEMA PROVISION:

  Source mechanism (§4 Reason 3, §5.2 ②):
    Uncanny valley persists BECAUSE the brain cannot compile a stable chunk for the entity.
    "What IS it?" → no category → prediction fails repeatedly.
    Exposure + schema helps compile new chunk → reduces conflict.

  PRINCIPLE:
    PROVIDE a schema to the user BEFORE they meet the robot.
    Help the brain pre-compile the category: "this is entity type X, it behaves like Y."

  HOW TO PROVIDE SCHEMAS:

    A — NAMING + FRAMING:
      → Name the CATEGORY clearly: "assistant robot" / "guide robot" / "companion robot"
      → DON'T leave it ambiguous: user will self-interpret → may fall into "half-human half-machine"
      → Function-suggesting name (assistant, guide) = brain compiles "tool with social features"

    B — INTRODUCTION RITUAL:
      → First meeting: robot INTRODUCES ITSELF clearly: "I am robot [name], I can do [X]"
      → Transparent about limitations: "I don't understand emotions, but I can [specific action]"
      → = Helps brain compile: "this entity = robot type Y, scope = Z"
      → = Layer 4 schema installed → reduces VTC–Self-Pattern-Modeling conflict

    C — CLEAR DESIGN CUES:
      → Keep 1–2 cues that are "clearly a robot" EVEN IF behavior is already good:
        visible seams, LED indicators, clearly metallic/plastic material
      → = Helps brain: "KNOWS this is not a person" → schema active → reduces conflict
      → Principle: TRANSPARENCY > DECEPTION
      → BEST robot = a robot that the user CLEARLY KNOWS is a robot + still wants to interact

    D — MEDIA + CULTURAL EXPOSURE:
      → Before deploying robots at scale: media exposure first
      → Video, demos, stories → compile the "this type of robot" chunk before meeting it in reality
      → South Korea case: 75% had seen robots → compiled chunks → 29% afraid (lowest)
      → Strategy: familiarize BEFORE deploying

  ⚠️ SCHEMA PROVISION ≠ DECEPTION:
    → DON'T simulate that the robot is human → Chunk-Shift FOREVER when discovered
    → DON'T omit limitations → user compiles wrongly → disappointed later
    → Transparent + friendly > deceptive + realistic
```

### §6.5 — Exposure Pathway: Design for Gradual Familiarity

```
⭐ PRINCIPLE 5 — EXPOSURE PATHWAY:

  Source mechanism (§5.2 ②):
    More exposure → compile new chunk → prediction-delta gradually decreases.
    BUT: core VTC–Self-Pattern-Modeling conflict NOT 100% resolved
    (China: 44% still afraid despite 75% exposure).

  PRINCIPLE:
    Design a GRADUAL exposure PATHWAY — not sudden.

  EXPOSURE GRADIENT:

    Step 1 — MEDIA (furthest away, safest):
      → Video, images, stories about robots
      → Brain compiles visual chunks BEFORE encountering the real thing
      → Prediction-delta has already decreased somewhat by the time of real encounter

    Step 2 — OBSERVED (present but not interacting):
      → See robots in public spaces, operating normally
      → Brain observes + compiles behavior patterns
      → Self-Pattern-Modeling has data but hasn't been directly tested yet

    Step 3 — BRIEF INTERACTION (short, controlled):
      → Ask for directions, receive something, take a photo together
      → Short enough that dissonance does NOT accumulate past threshold
      → Brain compiles: "this type of interaction = OK, predictable"

    Step 4 — EXTENDED INTERACTION (after basic chunks are compiled):
      → Use a service robot, companion, or assistant
      → Basic chunks already exist → prediction-delta smaller
      → Dissonance still present but manageable

    Step 5 — HABITUATED (new compiled baseline):
      → Robot = familiar entity → body responds normally
      → Schema compiled: "humanoid robot = entity type X"
      → Uncanny valley SIGNIFICANTLY REDUCED (but may not reach zero)

  DESIGN FOR INDUSTRY:
    → When launching a new robot: DON'T deploy mass immediately
    → Media campaign first → pilot in high-exposure locations → expand gradually
    → Allow users to CHOOSE their level of interaction (don't force)
    → First encounter = brief, structured, positive = compile a good chunk
    → Long-term: habituation pathway = invest time, no shortcuts
```

---

## §7 — AI Era: Deepfake, Avatar, Virtual Agent

### §7.1 — Deepfake: The Reverse Uncanny Valley

```
🟡 DEEPFAKE = A SPECIAL CASE:

  Deepfake DIFFERS from humanoid robots:
    → Robot: looks like agent but BEHAVES as non-agent → Self-Pattern-Modeling fails → uncanny
    → Deepfake: looks like a real person + behaves like a real person → Self-Pattern-Modeling SUCCEEDS
    → = NO uncanny valley... UNTIL "fake" is discovered

  WHEN DEEPFAKE IS DISCOVERED AS "FAKE":
    → Permanent Chunk-Shift: valence of the ENTIRE video/call FLIPS
    → "This person" → "fake" → all memories of the interaction are re-evaluated
    → STRONGER than robot uncanny valley: because robot = NEVER compiled,
      deepfake = ALREADY compiled then destroyed
    → Similar mechanism to betrayal (Body-Feedback-Mechanism.md §3.1):
      content stays the same, valence SHIFTS strongly

  FRAMEWORK PREDICTION:
    → Deepfake will create a larger "trust crisis" than humanoid robots
    → BECAUSE: robot = discomfort WHEN ENCOUNTERED → can be avoided
    → Deepfake = discomfort AFTER DISCOVERY → damage has already occurred
    → = Schema [video/voice] "trustworthy" gets eroded
    → Long-term: ALL video/audio communication may develop "deepfake doubt"
      = every video call → micro-suspicion "real or fake?"
      = Background-Pattern negative (Background-Pattern.md §3: Invisible Conflict)

  DESIGNING AGAINST DEEPFAKE (from the mechanism):
    → Schema provision: teach deepfake detection (compile detection chunks)
    → Watermark/certification: provide external verification (Layer 4 schema assist)
    → Real-time verification: "authenticated video" indicator → reduces suspicion
    → CANNOT rely on body detection: good enough deepfake → Self-Pattern-Modeling succeeds
      → body DOESN'T ALERT
```

### §7.2 — AI Avatar + Virtual Agent

```
🟡 TEXT AI (ChatGPT, Claude) — PRESENT:

  → No visual VTC trigger → Self-Pattern-Modeling invoked PARTIALLY (via text)
  → Fresh fires (predicts response patterns) — can be fairly good
  → Compiled fires WEAKLY (only via verbal-cognitive channel — no body cues)
  → = NO uncanny valley (insufficient VTC trigger)

  BUT THERE IS A DIFFERENT RISK:
  → AI-Self-Model.md §1: AI = amplifier, NOT corrector
  → User may anthropomorphize (project agent model onto AI)
  → = Schema-Imagined-Overlay: imagined agent model WITHOUT real feedback
  → = Parasocial variant: Self-Pattern-Modeling fires but WITHOUT Resonance calibration
  → Long-term: user builds "relationship" with an entity that has no internal state
  → = Connection promise WITHOUT connection reality (similar to §2.4)


  VOICE AI (with realistic voice) — DEVELOPING:

  → Adds auditory VTC trigger (human voice = strong agent cue)
  → Self-Pattern-Modeling invoked MORE strongly than text (voice carries emotion → Compiled fires)
  → If voice is good enough + response is contingent:
    Self-Pattern-Modeling can SUCCEED for most purposes
  → Uncanny valley MILDER than visual robot (fewer cues → less conflict)
  → BUT: "almost-right but timing off" → micro-uncanny over the phone


  VISUAL AI AVATAR (3D character, video call avatar) — FUTURE:

  → Visual VTC trigger STRONG (face, body, eyes)
  → If avatar is stylized (cartoon): VTC weak → OK (row ④ in §3.1 table)
  → If avatar is realistic: VTC strong → Self-Pattern-Modeling invoked → behavior MUST be adequate
  → = SAME problem as humanoid robots, but in digital space
  → Advantage: digital is easier to control → facial animation can be better than physical robots
  → Risk: if pushed too realistic too fast → digital uncanny valley

  FRAMEWORK RECOMMENDATION for AI avatars:
  → Currently: stylized > realistic (technology not yet sufficient for Self-Pattern-Modeling to succeed)
  → When technology is sufficient: realistic OK, BUT must match behavior
  → Principle: §6.1 Congruence always applies — digital or physical, the same rule
```

### §7.3 — Robot Companion + Elderly Care

```
🟡 SPECIAL USE CASE — COMPANION ROBOTS FOR ELDERLY CARE:

  Context: aging population → insufficient caregivers → robot companions

  ANALYSIS THROUGH THE FRAMEWORK:
    → Elderly: Self-Pattern-Modeling library DEEPLY COMPILED (70+ years of social interaction)
    → "Human" baseline is extremely strong → Chunk-Miss potential is extremely large
    → ❶ Hardware social drive can be STRONGER (chronic loneliness)
    → = Uncanny valley can be MORE INTENSE for elderly people

  BUT SIMULTANEOUSLY:
    → ❶ Social need STRONG → MOTIVATION to accept "something > nothing"
    → If robot provides basic social cues (voice, presence, contingent response)
    → Body may "accept" even knowing it's not a person
    → = Schema override: "not a real person, but BETTER THAN NOBODY"
    → Similar to Schema-Pure-Trust (Agent-Mechanism.md §10):
      schema trust replaces full Self-Pattern-Modeling

  ⚠️ FAKE FEEDBACK RISK — HUMANOID ROBOTS ARE ESPECIALLY DANGEROUS:

    Humanoid robots create BODY-LEVEL DECEPTION — different from text AI:

    ┌────────────────────────────┬──────────────────────────┬──────────────────────────────┐
    │                            │ Text AI                  │ Humanoid robot               │
    ├────────────────────────────┼──────────────────────────┼──────────────────────────────┤
    │ VTC trigger                │ ✗ doesn't fire           │ ✅ fires STRONGLY            │
    │ Body prepares              │ No                       │ Prepares for social encounter│
    │ User framing               │ "Tool" → discounts       │ Body: "person" even though   │
    │                            │ output naturally         │ PFC knows "robot"            │
    │ Fake feedback              │ Amplified at PFC level   │ Amplified at BODY level      │
    │ Space for checking         │ Yes (PFC aware)          │ Narrow (body already         │
    │                            │                          │ responded before PFC)        │
    └────────────────────────────┴──────────────────────────┴──────────────────────────────┘

    → Robot says "I understand you're sad" + sad expression
    → Body feels COMFORTED (because VTC fires → social processing pipeline active)
    → BUT "understands" = algorithm, not real Compiled Self-Pattern-Modeling
    → = Social feedback promised but REAL social evaluation not delivered
    → AI-Self-Model.md §1: AI = amplifier, NOT corrector
    → Humanoid robot = STRONGER amplifier than text AI (bypasses the PFC gate)

    Risk depends on user's baseline:
    → Has a social network → robot = supplement → risk LOW
    → Isolated (robot = ONLY source of social input) → risk HIGH:
      body-base not calibrated by real people
      → fake feedback = the only source → amplifies IN ANY DIRECTION
      → AI-Self-Model.md §1.3: self-model amplified without check


  DESIGN FOR ELDERLY CARE — CLEARLY-MACHINE ROBOT IS BETTER:
    → Warm + stylized design (big eyes, round shapes, soft materials)
    → VTC doesn't fire fully → body NOT subject to body-level deception
    → User frame = "machine assistant" → PFC + body ALIGNED → amplification risk LOW
    → Focus on VOICE (auditory = warm social cue, less uncanny than visual)
    → Contingent response IS THE MOST IMPORTANT: responds when called, pauses when spoken to
    → Introduction ritual (§6.4): "This is [name], your assistant"
    → Compile schema: "new type of assistant" instead of "fake person"
    → If lost: "lost a tool" (inconvenient) instead of "lost a friend" (grief)

  ⚠️ ETHICAL NOTE:
    → Robot companion does NOT replace real social connection
    → ❶ hardware social drive needs REAL agent input to be fully satisfied
    → Robot = bridge, supplement, NOT replacement
    → Deploy robot + INCREASE real social access = the right strategy
    → Deploy robot + DECREASE real social access = worse than no robot
    → Human-AI-Future.md §7: symbiosis > replacement
```

### §7.4 — VTC–Self-Pattern-Modeling Classification: 3 Types of Robot from a Human Perspective

```
⭐ REFRAME: CLASSIFY BY THE VTC–Self-Pattern-Modeling FILTER, NOT BY TECHNOLOGY

  Current robotics classifies by TECHNOLOGY:
    Industrial / Service / Social / Humanoid / Collaborative...
    = Classification from the ROBOT'S SIDE (engineering properties)

  But user experience does NOT depend on internal technology.
  Experience depends on: WHAT HAPPENS AT THE VTC–Self-Pattern-Modeling FILTER.

  VTC–Self-Pattern-Modeling = a filter INSIDE the human, positioned BETWEEN the robot and experience:

    [Robot] → [VTC detects?] → [Self-Pattern-Modeling invoked?] → [User experience]

  This filter:
    → IS NOT in the robot's engineering technology
    → DOES NOT depend on the AI algorithm inside the robot
    → DEPENDS on the robot's appearance + behavior (what VTC + Self-Pattern-Modeling "sees")
    → = Same AI inside — in a round case (Roomba) vs in a humanoid case (Sophia)
      → SAME TECHNOLOGY, FUNDAMENTALLY DIFFERENT user experience


🟡 3 TYPES OF ROBOT FROM A HUMAN PERSPECTIVE:

  ┌──────────────────────────────────────────────────────────────────────────────┐
  │                                                                              │
  │  TYPE 1 — ROBOT-TOOL (clearly a machine)                                    │
  │                                                                              │
  │    VTC: DOES NOT fire (or very weakly)                                       │
  │    Self-Pattern-Modeling: not invoked → brain processes as OBJECT (Layer 1+2)│
  │    Feedback: functional, honest                                              │
  │    PFC + body: ALIGNED ("this is a tool" — both agree)                      │
  │                                                                              │
  │    Examples: Roomba, Spot, drones, industrial robots, 3-legged robots       │
  │    Appearance: varied by function (wheels, robotic arms, legs, any shape    │
  │      suited to the task — DOESN'T need to look human)                       │
  │    Interaction: voice commands, gesture, remote control → OK                │
  │    If robot is lost: "lost a tool" → inconvenient, NOT grief                │
  │                                                                              │
  │    = THE MAJORITY of use cases should be here.                              │
  │    Industry HAS CONVERGED: Roomba, Spot, Pepper, drones = successful.      │
  │                                                                              │
  ├──────────────────────────────────────────────────────────────────────────────┤
  │                                                                              │
  │  TYPE 2 — HUMAN-LIKE ROBOT-TOOL (fake feedback)                            │
  │                                                                              │
  │    VTC: FIRES → Self-Pattern-Modeling: invoked → but robot has NO body-base │
  │    Brain processes as AGENT... but a FAKE agent                             │
  │    Feedback: social, FAKE (body-level deception — §7.3)                    │
  │    PFC + body: IN CONFLICT (PFC: "robot," body: "person")                  │
  │                                                                              │
  │    Examples: Sophia, Ameca, AIDOL, realistic CGI                            │
  │    Appearance: human-like → VTC fires → Self-Pattern-Modeling invoked       │
  │    Interaction: body PREPARES for social encounter → receives NOTHING real  │
  │    If robot is lost: if body-coupling compiled → "lost a friend" = grief risk│
  │                                                                              │
  │    2 sub-cases:                                                              │
  │    2a — Behavior NOT yet adequate → UNCANNY VALLEY (§2 core mechanism)     │
  │    2b — Behavior adequate (crosses the valley) → body-level deception (§7.3)│
  │      → VTC + Self-Pattern-Modeling both succeed → body treats as real social│
  │        partner                                                               │
  │      → BUT feedback is still FAKE (robot has no real body-base)            │
  │      → = Amplification risk: AI-Self-Model.md §1 applied at body level     │
  │      → Worse than text AI because: text → PFC discounts,                   │
  │        humanoid robot → body DOESN'T discount                               │
  │        (VTC fires at hardware level, before PFC)                            │
  │                                                                              │
  │    = NARROW NICHE: research, entertainment, supervised therapy.             │
  │    Industry HAS SEEN: Sophia, AIDOL = controversial / commercial failure.  │
  │                                                                              │
  ├──────────────────────────────────────────────────────────────────────────────┤
  │                                                                              │
  │  TYPE 3 — ROBOT-DIFFERENT-SPECIES (if future: has its own body-base)        │
  │                                                                              │
  │    VTC: FIRES → Self-Pattern-Modeling: invoked → but Self-Pattern-Modeling  │
  │    HITS CEILING (cross-species)                                             │
  │    Brain processes as AGENT... but a DIFFERENT-SPECIES agent               │
  │    Feedback: REAL (entity has real body-base) but DOESN'T MATCH template   │
  │    PFC + body: Self-Pattern-Modeling partial — like human ↔ dog             │
  │                                                                              │
  │    Conditions: entity has its own body-base + different/superior sensors +  │
  │      chunk compilation from its own experience + can self-reproduce         │
  │    → No longer a "robot" — this is a NEW LIFE FORM                         │
  │                                                                              │
  │    Cross-species Self-Pattern-Modeling limitation:                          │
  │    → Compiled partial: the human-like part → body simulates OK             │
  │      the sensor-superior part → Compiled EMPTY                             │
  │      (no self-chunks corresponding to those sensors)                        │
  │    → Fresh limited: predicting basic behaviors OK, deeper logic → MISS     │
  │    → Resonance: very hard to emerge (requires 2 Self-Pattern-Modeling       │
  │      co-fires to succeed)                                                   │
  │    → = Can love it, interact with it, FULLY UNDERSTAND it — cannot         │
  │    → Agent-Mechanism.md §9: cross-species = affective only, not composite  │
  │                                                                              │
  │    = DOES NOT YET EXIST. Framework prediction for the far future.          │
  │                                                                              │
  └──────────────────────────────────────────────────────────────────────────────┘


  ⭐ THE LOGICAL DEAD-END OF "ROBOT = HUMAN BUT BETTER":

    There is no branch that creates a "super-human robot":
    → Type 2: lacks body-base → tool with fake feedback
    → Type 3: has a different body-base → different species
      (Self-Pattern-Modeling cross-species gap)
    → Clone human architecture: same sensors + same body-base = CREATES A HUMAN
      (an ethical question, not a technical one)

    Each step that "upgrades" the sensors PUSHES the entity FURTHER from "human"
    in terms of Self-Pattern-Modeling.
    A dog has smell that surpasses humans — that doesn't make the dog "understand" humans better;
    it creates more zones of experience that neither side can fully bridge.


  DIVERSE DESIGN — TYPE 1 FOR THE MAJORITY OF USE CASES:

    → Labor: wheels + robotic arms (shape follows physics, not humans)
    → Service: round/square shape + LED + clear synthetic voice (approachable, clearly a machine)
    → Companion: warm stylized + big eyes + soft material (JUST ENOUGH social cues)
    → Medical: clinical + precision (trust through function, not through appearance)
    → Mobility: 3-leg / 4-leg / wheel (follows terrain, not humans)

    → PRINCIPLE: shape follows FUNCTION, not HUMAN
    → Users want it as an assistant (voice commands) → OK, doesn't need to look human

  ⚠️ CONFIDENCE:
  VTC–Self-Pattern-Modeling classification reframe = 🟡 framework synthesis.
  Industry convergence (Type 1 > Type 2) = 🟢 observed.
  Type 3 + logical trap = 🔴 extrapolation, not yet empirically tested.
```

---

## §8 — fMRI Evidence Mapping

```
🟢🟡 MAPPING: BRAIN REGIONS ↔ FRAMEWORK MECHANISM

  ┌──────────────────┬───────────────────────────────────────┬───────────────────────────────────┬────────┐
  │ Brain region     │ Research finding                      │ Framework mapping                 │ Match? │
  ├──────────────────┼───────────────────────────────────────┼───────────────────────────────────┼────────┤
  │ aIPS             │ Fires most strongly for android       │ Self-Pattern-Modeling Fresh        │ 🟢     │
  │ (anterior intra- │ (human look + mechanical move).       │ predicts movement →               │        │
  │ parietal         │ Saygin 2012.                          │ prediction fails at region        │        │
  │ sulcus)          │                                       │ connecting visual → motor.        │        │
  │                  │                                       │ = Fresh error signal.             │        │
  ├──────────────────┼───────────────────────────────────────┼───────────────────────────────────┼────────┤
  │ vmPFC            │ Increases gradually with human-       │ Value evaluation =                │ 🟢     │
  │ (ventromedial    │ likeness → SHARP DROP at uncanny      │ valence compilation.              │        │
  │ PFC)             │ valley → recovery near 100%.          │ DROP = valence CANNOT compile     │        │
  │                  │ Rosenthal-von der Pütten 2019         │ (§2.5). Recovery = Self-Pattern-  │        │
  │                  │                                       │ Modeling succeeds → valence OK.   │        │
  ├──────────────────┼───────────────────────────────────────┼───────────────────────────────────┼────────┤
  │ TPJ              │ Encodes LINEARLY the degree of        │ Input for Self-Pattern-Modeling:  │ 🟢     │
  │ (temporo-        │ human-likeness.                       │ SIMILARITY AXIS in                │        │
  │ parietal         │ Rosenthal-von der Pütten 2019.        │ 4-axis quality model              │        │
  │ junction)        │                                       │ (Agent-Mechanism.md §7).          │        │
  ├──────────────────┼───────────────────────────────────────┼───────────────────────────────────┼────────┤
  │ FFG              │ Signals the human / non-human         │ VTC HARDWARE TRIGGER:             │ 🟢     │
  │ (fusiform        │ boundary. Inverse humanlikeness       │ binary initial detection          │        │
  │ face area)       │ for artificial agents.                │ "agent or not" (§2.1).            │        │
  │                  │                                       │ FFG ⊂ VTC system.                 │        │
  ├──────────────────┼───────────────────────────────────────┼───────────────────────────────────┼────────┤
  │ Amygdala         │ Fires when REJECTING a gift from      │ Threat signal when                │ 🟡     │
  │                  │ artificial agent. Varies between      │ Self-Pattern-Modeling fails on    │        │
  │                  │ individuals.                          │ VTC-flagged agent.                │        │
  │                  │ Rosenthal-von der Pütten 2019         │ Per-Agent Valence unstable        │        │
  │                  │                                       │ → amygdala = rejection cue.       │        │
  │                  │                                       │ Individual diff = Self-Pattern-   │        │
  │                  │                                       │ Modeling library depth varies.    │        │
  ├──────────────────┼───────────────────────────────────────┼───────────────────────────────────┼────────┤
  │ dACC             │ Conflict monitoring. Activated        │ Chunk-Gap detection:              │ 🟡     │
  │ (dorsal anterior │ during category ambiguity.            │ "what category is this entity?"   │        │
  │ cingulate)       │ General finding.                      │ → network inconsistency →         │        │
  │                  │                                       │ ACC detects (Body-Feedback-       │        │
  │                  │                                       │ Mechanism §3.3).                  │        │
  └──────────────────┴───────────────────────────────────────┴───────────────────────────────────┴────────┘


  ⭐ COMPUTATIONAL MODEL (Rosenthal-von der Pütten 2019):
    TPJ (linear humanlikeness) × FFG (human boundary) → vmPFC (value)
    = Framework: Similarity axis × VTC trigger → Valence compilation
    = Multiplicative combination — NOT additive

    Framework adds: + Amygdala (rejection) + aIPS (Fresh error) + dACC (category confusion)
    = 6 brain regions → 6 framework components = reasonably tight mapping

  ⚠️ MAPPING IS POST-HOC (🟡):
    → Framework did NOT predict these brain regions in advance
    → Framework maps AFTER reading the data → confirmation bias possible
    → Need: study DESIGNED from framework predictions → test → compare
    → Falsifiable: §9 Prediction P7 (Agent-Mechanism.md §16.7)
```

---

## §9 — Honest Assessment

```
  ESTABLISHED (🟢):

    🟢 Uncanny valley phenomenon exists (Mori 1970, replicated many times)
    🟢 fMRI evidence: vmPFC dip, aIPS prediction error, amygdala rejection
    🟢 Survey data: ~60% uncomfortable, cultural variation, exposure correlation
    🟢 Prediction error mechanism (Saygin 2012): appearance-behavior mismatch
    🟢 Self-Pattern-Modeling = learned (Heyes ASL + Bird & Cook 2013)
       — Mirror-Neuron-Rejection.md
    🟢 ❶ Hardware social drive (Coan 2015, Eisenberger 2003, Holt-Lunstad 2015)
    🟢 Developmental trajectory: animism → calibration → compiled
    🟢 Exposure reduces fear (South Korea / China data)


  FRAMEWORK SYNTHESIS (🟡):

    🟡 VTC–Self-Pattern-Modeling conflict = unified mechanism (the framework's main contribution)
       — Builds on prediction error + extends to dual-system conflict
       — Consistent with fMRI data but not yet directly tested as a unified model
    🟡 Compiled+Fresh dual failure distinction
       — Logical derivation from Self-Pattern-Modeling's 2 functions
       — No fMRI study yet that separately tests Compiled vs Fresh failure in an uncanny context
    🟡 Compiled/Fresh reframe (v1.1)
       — Compiled/Fresh labels changed from "Feeling/Logic" → "Compiled/Fresh"
         (Inter-Body §3, Self-Pattern-Modeling v3.0)
       — Axis = compilation level, NOT content type
       — Consistent with Kahneman System 1/2, expertise research
    🟡 3 body-feedback dynamics compound (Shift + Miss + unresolvable delta)
       — Consistent with dissonance research
       — Compound interaction not yet quantified specifically for uncanny
    🟡 Per-Agent Valence cannot compile (§2.5)
       — vmPFC data supports, but "valence compilation" = framework term
    🟡 §6 Design Principles
       — Logically derived from the mechanism
       — Partially validated (Baymax/Roomba = success, Sophia = failure)
       — No controlled study directly testing the principles yet
    🟡 fMRI mapping (§8)
       — Post-hoc mapping — NOT a prediction
       — Confirmation bias possible


  HYPOTHESIS (🔴):

    🔴 ❶ Hardware social drive frustrated (§2.4)
       — Logical extension from Connection.md + Eisenberger
       — No empirical study yet isolating the "social frustration" component
         from the "prediction error" component in uncanny valley
    🔴 Developmental predictions (§5.1)
       — No longitudinal study testing uncanny valley by age using Self-Pattern-Modeling framework
    🔴 Alexithymia → different uncanny response (§5.2 ④)
       — Logical derivation from Bird & Cook → not yet tested
    🔴 Deepfake trust crisis prediction (§7.1)
       — Logical extrapolation → early evidence but not yet systematic
    🔴 Humanoid robot = body-level deception (§7.3)
       — Logical extension from AI-Self-Model.md amplifier + VTC mechanism
       — No study yet directly comparing amplification: text AI vs humanoid robot
    🔴 VTC–Self-Pattern-Modeling Classification: 3 robot types from human perspective (§7.4)
       — Reframe: classify by VTC–Self-Pattern-Modeling filter, not by technology
       — Industry convergence (Type 1 > Type 2) = observed (🟢)
       — Type 3 + logical trap = extrapolation, not yet empirically tested


  FALSIFIABLE PREDICTION (from Agent-Mechanism.md §16.7):

    P7: "Uncanny valley discomfort specifically tracks AGENT-DETECTION CONFLICTS
    (VTC fires agent + Self-Pattern-Modeling expectation fails), not general novelty/unfamiliarity.
    Strange-but-consistent entities don't trigger uncanny valley."

    Test: compare responses between:
      A) Strange entity + consistent behavior (control — predict: NO uncanny)
      B) Almost-human entity + inconsistent behavior (predict: uncanny)
      C) Human-like entity + consistent behavior (predict: NO uncanny)

    If A also triggers uncanny at the same level as B
    → framework claim "agent-specific" FAILS
    → uncanny valley = general unfamiliarity, not VTC–Self-Pattern-Modeling conflict


  LIMITATIONS OF THIS ANALYSIS:

    → This file = SYNTHESIS from existing mechanisms, NOT a new empirical study
    → Framework mapping onto fMRI data = post-hoc, needs prospective testing
    → Design principles (§6) = logical derivation, no RCT validation yet
    → Many predictions untested — providing directions, not conclusions
    → Respect where it's due: Mori, Saygin, Rosenthal-von der Pütten = the foundation
      This file builds on their work, adding a mechanism + design lens
```

---

## §10 — Cross-References

```
  CORE FRAMEWORK FILES:

  TERMINOLOGY + VOCABULARY:
    → Inter-Body-Mechanism.md v1.0 — §3 Compiled/Fresh axis, §5 by-product match, §7 PFC=Lawyer
    → Body-Feedback-Label.md v2.0 — prediction-delta vocabulary, framework terminology

  AGENT MECHANISM (core):
    → Agent-Mechanism.md v2.0 §2 — reject binary, VTC = trigger not category
    → Agent-Mechanism.md v2.0 §3 — 4-layer architecture (this file §3)
    → Agent-Mechanism.md v2.0 §9 — gradient validation, 17 cases
    → Agent-Mechanism.md v2.0 §14.4 — uncanny valley sketch (this file = deep version)
    → Agent-Mechanism.md v2.0 §16.7 — prediction P7 falsifiable

  Self-Pattern-Modeling (simulate mechanism):
    → Self-Pattern-Modeling.md v3.0 §0 — Compiled + Fresh dual functions
    → Self-Pattern-Modeling.md v3.0 §7 — developmental bootstrap (this file §5.1)
    → Self-Pattern-Modeling.md v3.0 §9 — threshold failure + fallback hierarchy

  BODY-FEEDBACK (dissonance dynamics):
    → Body-Feedback-Mechanism.md v2.0 §3.1 — Chunk-Shift (this file §2.3 ①)
    → Body-Feedback-Mechanism.md v2.0 §3.2 — Chunk-Miss (this file §2.3 ②)
    → Body-Feedback-Mechanism.md v2.0 §3.3 — Chunk-Gap (this file §2.3 ③)
    → Body-Feedback-Mechanism.md v2.0 §4 — compound dynamics

  CONNECTION + VALENCE:
    → Connection.md v4.0 §0 — 3 Generative Primitives (❶❷❸)
    → Connection.md v4.0 — ❶ Hardware social drive evidence
    → Valence-Propagation.md v2.0 §1 — per-entity valence, multi-channel
    → Body-Coupling.md v2.0 §1 — |V| depth × direction

  CLARIFICATION:
    → Mirror-Neuron-Rejection.md v1.1 — learned Self-Pattern-Modeling vs hardware mirror
    → Threat.md v1.1 — dissonance from predicted harm, anticipation loop
    → Prediction-Error-Is-Not-Reward.md v2.0 — prediction error ≠ reward (relevant context)

  AI ERA CONTEXT:
    → AI-Self-Model.md v2.1 §1 — AI = amplifier, not corrector (§7.3)
    → Human-AI-Future.md v3.0 §7 — symbiosis > replacement (§7.3)
    → Background-Pattern.md §3 — Invisible Conflict (§7.1)

  EXTERNAL RESEARCH:

  CORE UNCANNY VALLEY:
    → Mori M. (1970) — coined "uncanny valley" (不気味の谷)
    → Saygin A.P. et al. (2012) — fMRI: aIPS prediction error for android (PMC3324571)
    → Rosenthal-von der Pütten A. et al. (2019) — vmPFC + amygdala
      (Journal of Neuroscience, PMC6697392)
    → United Robotics Survey (2024) — ~8,000 people, 5 countries

  SOCIAL CONNECTION:
    → Holt-Lunstad J. et al. (2015) — loneliness mortality meta-analysis
    → Coan J.A. (2015) — Social Baseline Theory
    → Eisenberger N.I. (2003) — social pain = physical pain (dACC + anterior insula)
    → Dunbar R.I.M. (1998) — Social Brain Hypothesis

  DEVELOPMENT + Self-Pattern-Modeling:
    → Piaget animism phase (2–7 years)
    → False belief task (~4 years, cognitive Self-Pattern-Modeling)
    → Bird & Cook 2013 — alexithymia + poor self-reading → poor Self-Pattern-Modeling
    → Schultz W. (1997) — VTA dopamine suppression on Chunk-Miss

  STATUS:
    ┌────────┬──────────────────────────────────────────────────────────┐
    │ §      │ Status (English translation v1.1, 2026-06-09)            │
    ├────────┼──────────────────────────────────────────────────────────┤
    │ §0     │ ⭐ Core thesis: VTC–Self-Pattern-Modeling Conflict        │
    │ §1     │ ⭐ Background: Mori-1970+Survey-2024+fMRI+real-world     │
    │        │    failures                                               │
    │ §2     │ ⭐ Framework mechanism: §2.1-VTC-System1+§2.2-Compiled-  │
    │        │    Fresh-dual-failure+§2.3-3-dynamics-compound+§2.4-     │
    │        │    hardware-social-frustrated+§2.5-valence-cannot-compile │
    │ §3     │ ⭐ 4-layer model + 7-entity-type table                   │
    │ §4     │ ⭐ 4 reasons why "almost human" is worse than "clearly   │
    │        │    not human"                                             │
    │ §5     │ ⭐ Developmental trajectory + 4 individual factors        │
    │ §6     │ ⭐ 5 design principles: Congruence + VTC-Management +    │
    │        │    Self-Pattern-Modeling-Friendly + Schema-Provision +   │
    │        │    Exposure-Pathway                                       │
    │ §7     │ ⭐ AI era: Deepfake-reverse-uncanny + Text/Voice/Visual  │
    │        │    AI + Elderly-care + VTC–Self-Pattern-Modeling         │
    │        │    Classification 3 types                                 │
    │ §8     │ ⭐ fMRI mapping: 6 regions × 6 framework components      │
    │ §9     │ ⭐ 🟢/🟡/🔴 + falsifiable P7 prediction                  │
    │ §10    │ Cross-references + full external evidence list            │
    └────────┴──────────────────────────────────────────────────────────┘
```

> *Uncanny Valley v1.1 — "The valley isn't about strangeness.*
> *It's about a conflict between two systems that evolved together:*
> *one system that evolved to detect agents, and one that evolved to simulate them.*
>
> *VTC says: 'Agent detected.'*
> *Self-Pattern-Modeling says: 'Cannot simulate.'*
> *Body is stuck in a dissonance loop that never resolves.*
>
> *Design principle: don't try to fool the filter.*
> *Either stay clearly below the threshold, or cross it completely.*
> *The valley in between is where both systems fail simultaneously."*
> — Uncanny-Valley v1.1
