---
title: Prediction Error — Foundational Insight, Insufficient for Humans
version: v2.1
source: Core-Deep-Dive/Clarification/Prediction-Error-Is-Not-Reward.md v2.1
translated: 2026-06-09
status: COMPLETE
scope: |
  Prediction Error (PE) = foundational discovery in neuroscience.
  PE research on animals (monkeys, rats) = CORRECT, VALUABLE.
  Framework ACKNOWLEDGES the contribution + EXTENDS for humans:
  PE = attention/salience signal (VTA dopamine). Necessary, but not sufficient.
  Human reward = PE + COHERENCE + Body-Feedback Preconditions (body-base evaluation).
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Prediction Error — Foundational Insight, Insufficient for Humans

> **Schultz 1997 discovered that monkey brain neurons encode "different from prediction."**
> **This is one of the most important discoveries in modern neuroscience.**
>
> The insight that "the brain PREDICTS + COMPARES" opened a new view: humans and animals
> operate on a predictive principle — analyzable and understandable.
> This framework directly inherits that insight.
>
> **But:** The original research was on monkeys drinking juice — a simple context.
> Human reward is far more complex: multi-dimensional, body-evaluated.
> **PE = attention signal (Step 1). Human reward = a multi-step process, requiring 6 more steps.**
>
> This file acknowledges PE research's contribution, extends the mechanism for humans,
> and explains why the popular interpretation "PE = reward" is insufficient.

> **📋 VOCABULARY NOTE**: This file uses "PE" / "prediction error" because it is a
> Clarification file — its purpose is to compare the framework with mainstream neuroscience.
> In all OTHER framework files, the term **"prediction-delta"** replaces PE / VTA delta.
> See: [Body-Feedback-Label.md](../Body-Base/Body-Feedback/Body-Feedback-Label.md) v1.1.

---

## Table of Contents

- §0 — THE CONTRIBUTION OF PE RESEARCH
- §1 — FROM ORIGINAL DISCOVERY TO POPULAR INTERPRETATION
- §2 — PE IN AI vs HUMANS
- §3 — THE SPOTIFY TEST: WHY PE IS INSUFFICIENT
- §3b — NEUROSCIENCE VALIDATION: PE ≠ REWARD AT THE NEURAL SUBSTRATE LEVEL
- §4 — FRAMEWORK EXTENSION: PE + COHERENCE + BODY-FEEDBACK PRECONDITIONS
- §5 — 6 DISTINGUISHING CASES
- §6 — WHY THE SIMPLE INTERPRETATION HAPPENED
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §0 — THE CONTRIBUTION OF PE RESEARCH

```
⭐ PREDICTION ERROR RESEARCH = FOUNDATIONAL:

  Schultz 1997 discovery on macaque monkeys:
    → Dopamine neurons fire when reward > expected (positive PE)
    → Dopamine suppressed when reward < expected (negative PE)
    → Dopamine neutral when reward = expected (zero PE)
    → = VTA encodes PREDICTION ERROR 🟢

  WHY THIS IS AN IMPORTANT DISCOVERY:

    ① Opens a paradigm: the brain is NOT passively receiving input —
       the brain PREDICTS then COMPARES prediction with reality.
       "The predictive brain."
    ② Directly stimulated a research direction: humans and animals
       can be analyzed as systems — but more sophisticated than machines.
    ③ Foundation for Reinforcement Learning (AI/ML) —
       TD learning uses PE = reward signal, works excellently.
    ④ Human Predictive Drive Framework DIRECTLY INHERITS FROM THIS:
       "Predictive" in the framework's name = from this insight.
       VTA prediction error = Step 1 in the 7-step mechanism.

  FRAMEWORK ACKNOWLEDGES:
    PE research = correct, valuable, foundational.
    Framework BUILDS ON PE — adds layers for humans.
    Does NOT reject the original research.
```

---

## §1 — FROM ORIGINAL DISCOVERY TO POPULAR INTERPRETATION

```
🟢 ORIGINAL DISCOVERY = RESEARCH ON ANIMALS:

  Schultz 1997: monkey + juice reward
    → Context: 1 type of reward (juice), defined amount
    → PE > 0 = more juice than expected → monkey "happier"
    → IN THIS CONTEXT: PE ≈ reward signal = reasonable
    → Because: more juice = better, PE directly reflects value

  Berridge & Robinson 1998: rat + dopamine manipulation
    → Rats lost dopamine: STILL liked sugar (ate when offered)
       but DID NOT seek it anymore (seeking impaired)
    → = Dopamine = wanting (seeking), NOT liking (pleasure)
    → = PE (dopamine) related to seeking, NOT directly to reward

  BOTH STUDIES:
    → Correct, rigorous, foundational 🟢
    → Both on ANIMALS, SIMPLE context (1 type of reward)
    → Have not yet fully described the mechanism in HUMANS
    → (Human studies: fMRI, not single-neuron — lower resolution)


🟡 POPULAR INTERPRETATION = LOSS OF NUANCE:

  From animal findings → mainstream popularization:
    → "Positive PE → dopamine → reward → learning"
    → "PE = signal indicating: better or worse than expected"
    → Pop science: "prediction error drives your happiness"
    → AI/ML: PE = reward signal (correct for AI, but carried over to humans)

  Nuance lost:
    → Original research = animal, simple context, 1 reward type
    → Humans = multi-dimensional reward, body-evaluated
    → VTA fires for ANYTHING unexpected (good, bad, noise — all fire)
    → Body EVALUATES AFTER VTA — this is the step the original research hadn't covered

  = Original discovery CORRECT. Popular interpretation TOO SIMPLE for humans.
  = Framework adds the missing layers.
```

---

## §2 — PE IN AI vs HUMANS

```
🟡 WHY AI CAN USE PE SIMPLY (AND SHOULD):

  AI (Reinforcement Learning):
    → Reward function = PROGRAMMED, DEFINED by the designer
    → PE = actual reward - expected reward
    → Reward is a SPECIFIC NUMBER (score, win/lose, distance to goal)
    → PE directly tells: "better or worse than expected"
    → NO body evaluation needed → PE = reward signal = reasonable
    → AlphaGo, robotics, game AI — PE works excellently

  HUMANS — MORE COMPLEX:
    → DO NOT have a pre-programmed reward function
    → Body must SELF-GENERATE reward based on multi-dimensional evaluation
    → PE (VTA dopamine) only says: "something is DIFFERENT" (attention)
    → Body then EVALUATES: "is that difference good or bad?" (opioid/cortisol)
    → Evaluation depends on: coherence, chunk density, association tags,
      body-need state, Goldilocks zone — NOT just "different or not different"


  COMPARISON:

  ┌──────────────────────┬──────────────────────┬──────────────────────┐
  │                      │ AI (RL)              │ HUMAN                │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Reward function      │ Programmed (defined) │ Body-generated       │
  │ PE signal            │ = reward signal ✅   │ = attention signal   │
  │ Evaluation           │ Not needed (already) │ Body evaluates AFTER │
  │ Coherence            │ Not needed           │ REQUIRED for reward  │
  │ Body                 │ Does not exist       │ Body processes first │
  │ Random noise         │ PE high → low score  │ PE high → unpleasant │
  │ Preconditions        │ Not needed           │ Body-Feedback Precon.│
  └──────────────────────┴──────────────────────┴──────────────────────┘

  → AI uses PE = reward because reward IS DEFINED — reasonable for AI
  → Humans need additional evaluation because reward is NOT defined —
    body evaluates on its own
  → Same term "prediction error" but DIFFERENT function in the two systems
```

---

## §3 — THE SPOTIFY TEST: WHY PE IS INSUFFICIENT

```
⭐ IF PE = REWARD WERE SUFFICIENT, THEN:

  Test 1 — Random notes:
    A familiar piece of music + 1 random note added anywhere
    → PE is high (unexpected note)
    → If PE = reward → "better than the original"?
    → REALITY: worse, unpleasant, breaks the music
    → = PE high but reward = 0, dissonance = high
    → ⇒ PE is not sufficient for reward ✓

  Test 2 — Noise = best music:
    Random noise = MAXIMUM PE (nothing can be predicted)
    → If PE = reward → noise = the best music in the world?
    → REALITY: noise is the most unpleasant
    → ⇒ PE is not sufficient for reward ✓

  Test 3 — Spotify adds a small unexpected note:
    A familiar piece → Spotify automatically adds 1 unexpected note
    → PE increases (unexpected)
    → If PE = reward → listener finds it more enjoyable?
    → REALITY: listener finds it "wrong," "buggy," "unpleasant"
    → ⇒ PE is not sufficient for reward ✓


  SO WHAT MAKES A NEW PIECE OF MUSIC "GOOD"?

  A new piece of music is GOOD when:
    ① PE fires (VTA): "oh, something NEW" → ATTENTION ← PE plays its role
    ② The new element is COHERENT with the musical structure → body evaluates → "FIT!"
    ③ Goldilocks zone: familiar enough (safe) + novel enough (interesting)
    ④ Adequate chunk base: listener has enough chunks to EVALUATE
    ⑤ No negative association tag

  → "GOOD" = PE + Coherence + Goldilocks + Adequate chunks + No negative tag
  → = Body-Feedback Preconditions: ALL 5 must be met
  → = PE is STEP 1 — necessary. But 4 more factors are needed.

  WHERE DOES THE RANDOM NOTE FAIL?
    ✅ Precondition-3 Delta-Gate: YES (new note = unexpected) — PE passes
    ❌ Precondition-4 Match-Range: NO (random note breaks structure → too alien)
    ❌ Coherence: NO (note does not fit the structure)
    → PE passes but coherence + Goldilocks fail → dissonance

  WHERE DOES A GOOD NEW PIECE PASS?
    ✅ Precondition-3 Delta-Gate: YES (new piece = unexpected elements)
    ✅ Precondition-4 Match-Range: YES (familiar enough yet fresh enough)
    ✅ Coherence: YES (new elements FIT the structure)
    ✅ Precondition-2 Chunk-Substrate: YES (listener has sufficient musical experience)
    → ALL pass → body-base reward signal fires → REWARD → "good music!"
```

---

## §3b — NEUROSCIENCE VALIDATION: PE ≠ REWARD AT THE NEURAL SUBSTRATE LEVEL

```
⭐⭐ §3 SPOTIFY TEST = FRAMEWORK PREDICTS.
    §3b = NEUROSCIENCE CONFIRMS.

  §3 argues by LOGIC: random note = high PE but unpleasant → PE insufficient.
  §3b supplements with NEUROSCIENCE DATA: 3 landmark papers confirm
  PE and reward are 2 DIFFERENT things at the brain level.


  ═══ VALIDATION 1: Salimpoor 2011 — 2 brain regions, 2 time points ═══

  🟢 Salimpoor et al. 2011 (Nature Neuroscience 14:257-262)
      ~1,600+ citations. PET [¹¹C]raclopride.

  Finding:
    CAUDATE active during ANTICIPATION of musical peak
    → = Steps 1-3: VTA detects delta → dopamine cascade → "something is coming!"

    NUCLEUS ACCUMBENS active during EXPERIENCE of the peak
    → = Steps 5-6: body evaluates → opioid releases → "it's GOOD!"

  Why this is validation:
    ① 2 DIFFERENT brain regions → prediction ≠ experience (different substrates)
    ② 2 DIFFERENT time points → anticipation ≠ pleasure (different phases)
    ③ = PE (Steps 1-3) and Reward (Steps 5-6) are separable at the NEURAL level
    ④ = "Spotify Test" (§3) construct → Salimpoor = EMPIRICAL confirmation

  Supporting:
    🟢 Ferreri et al. 2019 (PNAS): levodopa increases + risperidone decreases
    musical pleasure BIDIRECTIONALLY → dopamine = causal, not just correlated


  ═══ VALIDATION 2: Cheung 2019 — Goldilocks across 80,000 chords ═══

  🟢 Cheung et al. 2019 (Current Biology 29:4084-4092)
      80,000 chords from Billboard Hot 100 (1958-1991).
      Information-theoretic measures: entropy (uncertainty) + surprise.

  Finding:
    Pleasure MAXIMIZED when:
      UNCERTAINTY HIGH (many possible next chords) + OUTCOME POSITIVE (chord FITS context)
    → = Surprising BUT coherent = peak pleasure

  Why this is validation:
    §3 Spotify Test predicts:
      Random note = high PE but NO coherence → unpleasant
      Perfect prediction = zero PE → bland
      Sweet spot = PE + coherence → enjoyable
    Cheung 2019 QUANTIFIES this EXACT relationship with 80,000 data points.
    → = "Spotify Test" (§3) = validated by empirical data

  Supporting:
    🟢 Gold et al. 2019 (PNAS): pleasure = interaction of acoustic × schematic.
    Acoustic features (sensory) or schematic expectations (cognitive) ALONE
    are insufficient — INTERACTION is required = BOTH PE AND coherence are needed.
    = Body-Feedback Preconditions: ALL preconditions needed simultaneously.


  ═══ SYNTHESIS ═══

  §3 (Spotify Test)  = Framework PREDICTS: random PE ≠ reward
  §3b Salimpoor 2011 = Neuroscience CONFIRMS: 2 regions, 2 times = 2 steps
  §3b Cheung 2019    = Neuroscience CONFIRMS: Goldilocks = 80k data points

  = §3 prediction → §3b validation → STRENGTHENS the entire file.
  = PE ≠ Reward is not only a logical argument — there is NEURAL SUBSTRATE evidence.

  ⚠️ CAVEAT:
    Opioid role in music pleasure: body-level confirmed (Mallik 2017,
    naltrexone reduces physiological response). Subjective pleasure unclear
    (Mas-Herrero 2023). Does NOT undermine the multi-step model — only refines
    Step 6 (body-level) vs Step 7 (conscious experience).
```

---

## §4 — FRAMEWORK EXTENSION: PE + COHERENCE + BODY-FEEDBACK PRECONDITIONS

```
⭐ FULL MECHANISM — PE IS STEP 1 OF 7:

  STEP 1 — VTA DETECT (Prediction Error):
    → New input → VTA compares with expected baseline
    → Actual ≠ expected → VTA fires dopamine
    → = ATTENTION signal: "something is DIFFERENT"
    → = This is what Schultz 1997 discovered — CORRECT
    → PE completes its role here: signals "something new"

  STEP 2 — BODY EVALUATE (Coherence Check):
    → Chunks matching: does the new pattern FIT into the existing chunk network?
    → Coherence = does the new thing MESH with what's already compiled?
    → FIT (coherent) → preparation for reward
    → NOT FIT (incoherent) → preparation for dissonance
    → = This step was NOT in the original PE research
      (animal context too simple to require it)

  STEP 3 — BODY-FEEDBACK PRECONDITION CHECK:
    → Precondition-1 Directed-Gap: Is the body-need gap open? (is it needed?)
    → Precondition-2 Chunk-Substrate: Is the chunk base adequate? (enough to evaluate?)
    → Precondition-3 Delta-Gate: Is the prediction-delta threshold met? ← PE lives here
    → Precondition-4 Match-Range: Goldilocks zone? (familiar enough, novel enough?)
    → Precondition-5 Compile-Gate: What is the chunk's association tag? (not avoidance-tagged?)
    → ALL 5 required. Missing ANY → reward does not fire.

  STEP 4 — SIGNAL FIRES:
    → ALL pass + coherent → body-base reward signal fires → REWARD
    → ANY fail OR incoherent → cortisol → DISSONANCE
    → = "Gift or snake" depends on the ENTIRE evaluation, not just PE

  → PE = STEP 1 (attention). FOUNDATIONAL, NECESSARY.
  → REWARD = STEP 4 (body-base evaluation → signal fires). After passing STEPS 2 + 3.
  → Framework adds Steps 2-3 in between — this is the part the original research
    hadn't yet covered.
  → = "Doorbell rings (PE) → check who's there (coherence + preconditions)
       → then we know: gift (reward) or snake (dissonance)"

  ⚠️ IMPORTANT NOTE — REWARD ≠ A SINGLE CHEMICAL:
    Reward = MULTI-STEP PROCESS, NOT a single substance.
    → Evaluative: opioid = primary chemical. Requires Body-Feedback Preconditions.
      Complex. Examples: enjoying music, solving a puzzle, insight, deep connection.
    → Direct-State: NON-opioid (CT afferents, endocannabinoid).
      Examples: touch, hugging, exercise, warmth. Present from birth.
    → Do NOT replace "dopamine = reward" with "opioid = reward"
      — both are oversimplifications.
    → Reward = the entire evaluation process, not any single chemical.
    → Detail: Reward-Signal-Architecture.md §1-§3


  ⭐ 2-LAYER MODEL (Gap-Direction.md §6):
    This file distinguishes PE vs Reward via 4 STEPS (process).
    Gap-Direction.md formalizes further: 2 LAYERS:
      Layer 1 = SIGNAL MECHANISM: VTA/ACC detects "something is different" (= PE)
      Layer 2 = DIRECTION CONTENT: chunk network determines "different HOW"
    "Coherence" (step 2) = does the stimulus match the GAP DIRECTION?
    Coherence DIFFERS across people because gap direction DIFFERS (chunk networks DIFFER).
    = Why the SAME PE makes a trendy car = reward, an antique car = not for another:
      PE (Layer 1) fires for BOTH, but Layer 2 only matches for the trendy car.


  CROSS-REFERENCE WITH DOPAMINE-IS-NOT-REWARD §4 (7-STEP):

    Step 1: VTA detects delta (PE) — ATTENTION ← Schultz 1997
    Step 2: Dopamine cascade (salience) — ALERTING
    Step 3: Spreading activation (chunks fire)
    Step 4: Body-base evaluation (coherence + Body-Feedback Preconditions) ← Framework adds
    Step 5: Body-base VOTE (reward/dissonance) — EVALUATION
    Step 6: Opioid release (if reward) — ACTUAL REWARD
    Step 7: PFC observes (feeling) — CONSCIOUS EXPERIENCE

    → PE = Steps 1-2 (Schultz discovered — correct, kept as-is)
    → REWARD = Steps 5-6 (framework adds — the part where humans are more complex)
    → Steps 3-4 = the "middle" part that animal research didn't need
      because its context was simple
```

---

## §5 — 6 DISTINGUISHING CASES

```
🟡 6 CASES SHOWING PE AND REWARD DO NOT ALWAYS GO TOGETHER:

  CASE 1 — PE high + REWARD high:
    New good music = unexpected + coherent + Goldilocks
    → PE fires (it's new!) + body evaluates (it fits!) → body-base reward → "good!"
    → = PE + coherence = reward ✓
    → = Context similar to Schultz: simple, PE ≈ reward — research CORRECT here

  CASE 2 — PE high + DISSONANCE:
    Spotify random note = unexpected + incoherent
    → PE fires (it's new!) + body evaluates (it breaks the structure!) → cortisol → "bad"
    → = PE high but coherence fails → dissonance
    → = Context DIFFERENT from Schultz: more complex, PE ≠ reward

  CASE 3 — PE low + REWARD:
    A beloved piece of music heard for the 100th time
    → PE near zero (already known) + coherence high + body-need met
    → Mild opioid → "comfortable, familiar"
    → = Low PE but still has reward (comfort zone, hardware pull)

  CASE 4 — PE low + NEUTRAL:
    An ordinary piece of music heard many times
    → PE zero + medium coherence + body-need somewhat met
    → No reward, no dissonance
    → = "Background music, nothing particularly felt"

  CASE 5 — PE high + CONFUSED:
    Free jazz heard for the first time (by someone unfamiliar with it)
    → PE extremely high + chunk base NOT adequate (Precondition-2 fails)
    → Body CANNOT evaluate → confused → "I don't get it"
    → = PE high but Precondition-2 fails → no reward, no clear dissonance
    → BUT: someone WITH jazz chunks → Precondition-2 passes → CAN have reward
    → = Reward PER-PERSON (depends on chunk library), not universal

  CASE 6 — PE high + BLOCKED:
    A new good piece of music BUT performed by someone the listener dislikes
    → PE fires + coherence OK + Goldilocks OK
    → BUT Precondition-5 Compile-Gate = AVOIDANCE (dislikes the performer)
    → Body blocks reward → "good song but can't stand listening to it"
    → = PE + coherence pass, but Precondition-5 fails → reward blocked

  → 6 cases show: PE and REWARD are 2 INDEPENDENT variables in humans
  → Case 1 (simple) ≈ animal research context — PE ≈ reward, research correct
  → Cases 2-6 (complex) = what humans typically encounter — PE insufficient,
    additional layers needed
```

---

## §6 — WHY THE SIMPLE INTERPRETATION HAPPENED

```
🟡 THE NATURAL PATH OF SCIENCE — NOT A MISTAKE:

  ① ANIMAL STUDIES = SIMPLE CONTEXT (reasonable as a starting point):
    → Schultz 1997: monkey + juice — 1 reward type, defined
    → In the juice context: PE > 0 ≈ reward = REASONABLE
    → Generalizing from animal → human = the natural step in science
    → But human context is more complex: multi-dimensional, per-person
    → = Extension needed, not a refutation of the original finding

  ② AI/RL SUCCESS = POSITIVE REINFORCEMENT for the simple interpretation:
    → TD learning uses PE = reward signal → AI works well
    → = "PE = reward works" — true, for AI
    → AI success created momentum to preserve the simple interpretation
    → But AI has a DEFINED reward function; humans do not
    → = AI success proves PE works for AI; has not proven it is sufficient for humans

  ③ BROAD TERMINOLOGY:
    → "Prediction error" groups many mechanisms: VTA delta (attention),
       body evaluation (reward), learning update
    → Same term for many different steps = natural in the early stage
    → As understanding deepens → need to distinguish each step clearly
    → Framework distinguishes: PE (Step 1) vs evaluation (Step 4) vs reward (Step 6)

  IN SUMMARY:
    The simple interpretation arose because:
    → Original discovery correct + simple animal context + AI success
    → = Natural momentum for the "PE = reward" narrative
    → Framework: PE = Step 1 (correct). But human reward needs Steps 2-6 in addition.
    → = EXTENDING the interpretation, not denying the discovery.
```

---

## §7 — HONEST ASSESSMENT

```
⭐ CONTRIBUTION OF PE RESEARCH TO THE FRAMEWORK:
  → "Predictive brain" paradigm → framework name: Human PREDICTIVE Drive
  → VTA prediction error = Step 1 in the 7-step mechanism
  → Dopamine as salience signal → framework inherits + clarifies
  → Animal vs human comparison → helps identify WHAT needs to be added for humans
  → AI/RL TD learning → useful analogy to contrast AI vs human reward

🟢 ESTABLISHED (research correct, framework preserves):
  → VTA dopamine = prediction error signal (Schultz 1997) ✅
  → Dopamine ≠ reward/pleasure (Berridge & Robinson 1998-2016) ✅
  → Opioid system involvement in hedonic response (Fields 2007) ✅
  → Random noise ≠ rewarding (common sense + acoustic research) ✅
  → Goldilocks zone / optimal novelty (Berlyne 1960) ✅
  → AI/RL uses PE as reward signal successfully (TD learning) ✅

🟢 v2.1 UPGRADED (music neuroscience validation — §3b):
  → PE = attention signal, NOT sufficient for human reward
    (v2.0: 🟡 consistent with Berridge. v2.1: 🟢 Salimpoor 2011 confirms
    caudate (anticipation) ≠ NAcc (experience) = 2 neural substrates, 2 phases.
    PE = Steps 1-3, Reward = Steps 5-6 — temporal + spatial dissociation.)
  → PE + coherence = reward formula (Goldilocks applied to PE)
    (v2.0: 🟡 "Spotify Test" = logical construct. v2.1: 🟢 Cheung 2019
    QUANTIFIES with 80,000 chords — pleasure MAX when uncertainty (PE) HIGH
    + outcome POSITIVE (coherence). §3 construct → §3b validation.
    Note: Goldilocks CONCEPT = 🟢 established (Berlyne 1960, in §7 ESTABLISHED).
    The upgrade here = how the framework APPLIES Goldilocks to PE vs reward.)

🟡 FRAMEWORK SYNTHESIS (extending from research):
  → Coherence evaluation as a separate step
    (framework organizing, consistent with neuroscience, not yet formalized elsewhere)
  → Body-Feedback Preconditions — 5 conditions (framework hypothesis, empirically testable)
  → 4-step mechanism (VTA → coherence → Preconditions → body-base signal) — framework integration
  → Evaluative/Direct-State reward distinction (opioid vs non-opioid pathways)
  → AI/human distinction re: PE (logical argument, testable)

🔴 HYPOTHESIS (framework estimate, not yet measured):
  → Exact timeline VTA → coherence → opioid (framework estimate)
  → Whether coherence evaluation = single step or distributed process
  → Quantitative threshold for coherence (how much "fit" = sufficient?)

⚠️ SUMMARY:
  → PE research = FOUNDATIONAL. Correct. Valuable. Framework builds on it.
  → Framework does NOT reject Schultz 1997 or Berridge.
  → Framework EXTENDS: adds coherence + Body-Feedback Preconditions +
    Evaluative/Direct-State distinction for humans.
  → Reward = PROCESS, not a chemical (neither opioid nor dopamine alone).
  → = PE put in its correct position (Step 1 of 7), not abandoned.
  → = CLARIFICATION + EXTENSION, not rejection.
```

---

## §8 — CROSS-REFERENCES

```
WITHIN FRAMEWORK:
  Body-Feedback-Label.md v2.0 — ⭐ VOCABULARY REFERENCE.
    Framework uses "prediction-delta" instead of PE / VTA delta.
    3-tier label system. 100% framework vocabulary.
  Reward-Signal-Architecture.md — ⭐ Evaluative (opioid) vs Direct-State (non-opioid),
    5 profiles, reward = PROCESS not chemical
  Gap-Direction.md — ⭐ 2-layer model formalizes PE vs reward:
    Layer 1 = signal mechanism (PE), Layer 2 = direction content (gap direction)
  Dopamine-Is-Not-Reward.md — dopamine ≠ reward, 7-step mechanism
  Body-Feedback.md — Body-Feedback Preconditions (5 conditions), dual-pull architecture
  Body-Feedback-Mechanism.md — 3 chunk dynamics (Shift/Miss/Gap)
  03-Reward.md — car paradox, Van Gogh gradient, reward mechanism
  Chunk.md v2.0 — chunk substrate, activation dynamics
  Core-Software.md §4.2 — body-feedback in cycle architecture
  Feeling.md v2.1 §2.2b — PFC threshold in 2 dimensions (magnitude × clarity)
  Why-Body-Knows.md §2 — Goldilocks zone
  Novelty.md — VTA as seismograph, novelty ≠ reward

Drill-Sound-Brain (v2.1 — music neuroscience validation):
  Drill-Sound-Brain/03-Sound-Reward-Pipeline.md §2, §4
    → Salimpoor 2011 (caudate ≠ NAcc) + Cheung 2019 (80k chords)
    → Per-step validation of 7-step mechanism
  Drill-Sound-Brain/10-Synthesis.md §2 Validation 1, 3
    → PE ≠ Reward (Validation 1) + Goldilocks (Validation 3)

KEY RESEARCH (framework acknowledges + builds on):
  Schultz 1997 — VTA PE signal (foundational — framework builds on this)
  Berridge & Robinson 1998, 2003, 2016 — wanting ≠ liking (foundational)
  Berlyne 1960 — optimal novelty / inverted-U
  Zajonc 1968 — mere exposure effect
  Crespi 1942 / Flaherty 1996 — SNC (baseline violation)
  Fields 2007 — opioid hedonic system
  Sutton & Barto 1998 — TD learning (PE works for AI — correct for AI)

v2.1 RESEARCH (§3b validation):
  🟢 Salimpoor et al. 2011 (Nature Neuroscience 14:257-262) — caudate ≠ NAcc,
      anticipation ≠ experience, ~1,600+ citations, PET raclopride
  🟢 Cheung et al. 2019 (Current Biology 29:4084-4092) — 80k chords,
      pleasure MAX = high uncertainty + POSITIVE outcome
  🟢 Ferreri et al. 2019 (PNAS) — bidirectional dopamine modulation (causal)
  🟢 Gold et al. 2019 (PNAS) — acoustic × schematic interaction required
```

---

> *Prediction Error v2.1 — "PE (Schultz 1997) = foundational discovery, correct, valuable.
> Framework builds on it: PE = Step 1 (attention signal). Human reward
> = multi-step process, requires: coherence + Body-Feedback Preconditions + body-base evaluation.
> v2.1: §3b Neuroscience Validation — Salimpoor 2011 confirms caudate (anticipation)
> ≠ NAcc (experience) = PE ≠ Reward at the neural substrate level. Cheung 2019
> validates Goldilocks with 80,000 chords. §3 construct → §3b validation.
> PE = the doorbell — foundational. Gift or snake = body evaluates further."*
