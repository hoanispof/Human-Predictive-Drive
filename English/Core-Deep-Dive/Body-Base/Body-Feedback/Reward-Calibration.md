---
title: Reward Calibration — Observation File for Reward Amount × Gap Match
version: 1.1
created: 2026-05-10
refined: 2026-05-10 (v1.1 — §3.4 Premature Compilation, §5.4 Collective Calibration, §8.1③ Gap Shift + Schema Trust)
source_version: Vietnamese v1.1
english_created: 2026-06-06
status: OBSERVATION FILE v1.1
scope: |
  OBSERVATION FILE: HOW MUCH reward is ENOUGH for THIS gap,
  THIS person, THIS context? And what happens when there's too little / too much?
  Core thesis: Reward has a Goldilocks sweet spot per-gap, per-person, per-context.
  CANNOT prescribe — can only OBSERVE + ADJUST (dynamic equilibrium).
  3 Gap Types × Reward Match. Goldilocks Zone (Under/Match/Over).
  6 Over-Reward Mechanisms (threshold adaptation, overjustification, bridge dependency,
  baseline shift, competence-reward mismatch, Evaluative/Direct-State imbalance).
  Dynamic equilibrium parallel to Logic-Feeling-Balance.md.
  Observable indicators through communication + behavior (probabilistic, not diagnostic).
  Evaluative/Direct-State × Calibration. Reward-Economics insights through v7.8 lens.
purpose: |
  03-Reward.md answers: WHEN does reward fire? (5 Body-Feedback-Preconditions, 7-step VTA)
  Reward-Signal-Architecture answers: What QUALITY does reward fire with? (Evaluative/Direct-State, 5 Profiles, Evaluative Gates Direct-State)
  Gap-Direction.md answers: WHY is reward personal? (gap has direction)
  Gratitude.md §3-4: Anti-habituation + baseline shift
  Education-Mechanism.md §3: Bridge (external reward) in education
  This file answers: HOW MUCH reward is ENOUGH? And what happens when the amount is wrong?
  = CALIBRATION question — analogous to Cortisol-Baseline.md
  (cortisol = amplifier with Goldilocks; reward = signal with Goldilocks)
dependencies:
  - 03-Reward.md — 5 Body-Feedback-Preconditions, 7-step VTA, opioid vs dopamine, 7 cases
  - Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles, Evaluative Gates Direct-State
  - Body-Feedback-Mechanism.md v1.2 — 2 sources, 3 dynamics (Shift/Miss/Gap), compound
  - Gap-Direction.md v1.0 — gap has direction, "unknown = no gap", 2-layer
  - Gratitude.md v1.1 — §3 anti-habituation 3 mechanisms, §4 baseline shift
  - Education-Mechanism.md v1.0 — §3 bridge, 4 fill sources, overjustification
  - Cortisol-Baseline.md v2.0 — §7.7 5 Roles (② Holding, ④ Inertia relevant)
  - Status.md v2.0 — §1 Resource Access Map, competence-reward mismatch
  - Logic-Feeling-Balance.md v1.0 — §6-§7 infinite regress, cannot prescribe
  - PFC-Hardware.md v1.1 — §3.4 COMT × Reward Pattern, §3.5 Childhood trajectories
  - Background-Pattern.md v1.0 — invisible bias on gap direction landscape
  - Connection.md v3.1 — §9 calibration between 2 bodies, dynamic equilibrium
  - Reward-Economics.md v5.5 — 6 paths, money = proxy, habituation blindness (insights)
  - Meaning.md v2.0 — IDENTITY anchor, life-level Anchor-Schema
  - Obligation.md v1.0 — cortisol holding (Role ②), 5-factor formula
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Reward Calibration — Observation File for Reward Amount × Gap Match

> **Salary level A. Pleasant.**
> **Raise to 1.5A. More pleasant.**
> **Raise to 2A. Still pleasant — but less than before.**
> **Raise to 5A. Pleasant... then habituated.**
> **Raise to 10A. "How much does my colleague make?"**
>
> Same person. Same reward mechanism (Body-Feedback-Precondition, 03-Reward.md).
> But the AMOUNT of reward needed to produce satisfaction = CONTINUOUSLY SHIFTING.
>
> Sugar in food: too little = bland, just right = delicious, too much = sickening.
> Salary: too low = painful, right amount = fine, too high = creates DIFFERENT problems.
> Praise: too little = withering, just right = good, too much = "why the praise?"
>
> EVERY type of reward has a GOLDILOCKS — a sweet spot.
> AND the sweet spot is NOT FIXED: different per-person, per-gap, per-context, per-time.
>
> This file does NOT say "give this much reward."
> This file helps you SEE: which zone is reward currently in (under / match / over),
> AND what happens at each zone,
> AND why it is IMPOSSIBLE to prescribe "the right amount."

---

## Table of Contents

- §0 — POSITION IN FRAMEWORK
- §1 — CORE: REWARD HAS A GOLDILOCKS PER-GAP
- §2 — 3 GAP TYPES × REWARD MATCH
- §3 — GOLDILOCKS ZONE: 3 STATES
- §4 — OVER-REWARD: 6 HARMFUL MECHANISMS
- §5 — DYNAMIC EQUILIBRIUM: WHY PRESCRIBING IS IMPOSSIBLE
- §6 — OBSERVABLE INDICATORS
- §7 — EVALUATIVE/DIRECT-STATE × CALIBRATION
- §8 — REWARD-ECONOMICS INSIGHTS THROUGH V7.8 LENS
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES

---

## §0 — POSITION IN FRAMEWORK

### §0.1 — This file vs 5 related files

```
⭐ THIS FILE ANSWERS A NEW QUESTION:

  ┌───────────────────────────┬─────────────────────────────────────────┐
  │ File                      │ Question                                │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ 03-Reward.md              │ WHEN does reward fire?                  │
  │                           │ (5 Body-Feedback-Preconditions, 7-step VTA)      │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Reward-Signal-            │ What QUALITY does reward fire with?     │
  │ Architecture.md           │ (Evaluative/Direct-State, 5 Profiles, Evaluative Gates Direct-State)  │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Gap-Direction.md          │ WHY is reward personal?                 │
  │                           │ (gap has direction, f(surrounding chunks)) │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Gratitude.md §3-4         │ WHY do gifts habituate?                 │
  │                           │ (anti-habituation, baseline shift)      │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Education-Mechanism.md §3 │ Bridge reward in education?             │
  │                           │ (source ④, overjustification)           │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Reward-Calibration.md     │ HOW MUCH reward is ENOUGH?              │
  │ (THIS FILE)               │ What happens when the amount is wrong?  │
  │                           │ Why is prescribing impossible?          │
  └───────────────────────────┴─────────────────────────────────────────┘

  This file = OBSERVATION SYNTHESIS:
  → Synthesizes insights from ~15 files into 1 CALIBRATION lens
  → Does NOT create new mechanisms — reorganizes through "enough for this gap"
  → Reading flow: read AFTER 03-Reward + Reward-Signal-Architecture + Body-Feedback-Mechanism + Gap-Direction
```

### §0.2 — What this file IS

```
  ✓ Observation file — helps you SEE reward state
  ✓ Helps identify: under / match / over
  ✓ Explains 6 over-reward mechanisms (synthesized + new)
  ✓ Parallel to Cortisol-Baseline.md: cortisol has Goldilocks ↔ reward has Goldilocks
```

### §0.3 — What this file is NOT

```
  ✗ NOT a "how to design rewards" file (NOT prescriptive)
  ✗ NOT an economics file (Reward-Economics.md = Applications layer)
  ✗ NOT a repeat of Body-Feedback-Precondition or Reward-Signal-Architecture (reference only)
  ✗ NOT an education file (Education-Mechanism.md §3 already covers bridge)
  ✗ NOT an HR file
  ✗ Does NOT say "what to do" — only says "where things are" and "why it's hard"
```

---

## §1 — CORE: REWARD HAS A GOLDILOCKS PER-GAP

### §1.1 — Thesis

```
⭐ REWARD AMOUNT HAS A SWEET SPOT PER-GAP:

  Gap (Body-Feedback-Mechanism §3: Chunk-Shift / Chunk-Miss / Chunk-Gap)
  = a hole in the chunk network that needs filling.

  Too little reward for the gap → gap not filled → dissonance PERSISTS
  Just enough reward for the gap → gap fills + approach tag + chunk compiles
  Too much reward for the gap → SURPLUS → multiple harmful mechanisms (§4)

  = Like sugar in food:
    Too little sugar → bland → body "insufficient caloric signal"
    Just right sugar → delicious → E₀ hardware opioid confirms (Reward-Signal-Architecture §2.1)
    Too much sugar → sickening → body REJECTS (saturation threshold)
    = E₀ = hardware Goldilocks in its SIMPLEST FORM
    = SAME PATTERN at every level of reward, just INCREASINGLY COMPLEX

  🟢 Hedonic adaptation: Brickman & Campbell 1971
  🟢 Inverted-U: Yerkes-Dodson 1908 (performance ↔ arousal)
  🟡 Reward Goldilocks per-gap = framework synthesis
```

### §1.2 — Goldilocks is NOT FIXED

```
⭐ SWEET SPOT SHIFTS CONTINUOUSLY:

  → Different PER-PERSON (hardware):
    COMT Val/Val: many shallow rewards = MATCH hardware
    COMT Met/Met: fewer deeper rewards = MATCH hardware
    (PFC-Hardware.md §3.4)
    DRD4 variant: chunk threshold differs → goldilocks differs
    (PFC-Hardware.md §4.3)

  → Different PER-GAP-TYPE:
    Chunk-Shift: needs re-anchoring → different reward (§2)
    Chunk-Miss: needs compensating OR adjusting → different reward (§2)
    Chunk-Gap: needs exploration → different reward (§2)

  → Different PER-CONTEXT:
    Cortisol state: Role ② Holding → different reward needed (Cortisol §7.7)
    Existing chunks: expert vs novice → same input, different reward
    Relationship: given by close friend vs stranger → different valence
    Background-Pattern: invisible bias → gap landscape skewed
    (Background-Pattern.md §6)

  → Different PER-TIME:
    Baseline shift: continuous reward → baseline RISES → need MORE to match
    (Gratitude.md §4)
    Development stage: child vs adult → different thresholds
    Habituation: first time vs hundredth time → completely different prediction-delta

  → NO formula "give X reward for gap Y"
  → Only: OBSERVE + ADJUST continuously (§5)

  🟡 Per-person × per-gap × per-context × per-time = framework synthesis
```

### §1.3 — "Unknown = no gap" → Reward for a nonexistent gap = WASTED

```
⭐ FOUNDATIONAL PRINCIPLE (Gap-Direction.md §3):

  Gap = a hole in the chunk network = REQUIRES surrounding chunks to form edges.
  No surrounding chunks = no edges = NO HOLE.

  "Unknown = no gap":
    → Someone who doesn't know chess → has no gap about chess
    → Chess-related reward = MATCHES no gap → WASTED
    → Body receives stimulus → VTA checks → NO matching gap → no opioid confirm
    → = Reward "falls into empty space"

  EXAMPLES:
    A 5-year-old given a luxury supercar (no gap about cars yet)
      → Body: "a big thing" → no gap match → no reward
      → Parents: "why isn't the child excited?" → because the child has NO GAP for it

    Gifting E=mc² to a 3rd-grade student
      → No physics chunks compiled yet → no gap → no reward
      → Gifting it to Einstein → GAP IS PROFOUND → reward IS POWERFUL

  CALIBRATION IMPLICATION:
    Step 0 BEFORE calibrating reward: confirm that the RECIPIENT HAS A GAP.
    No gap → all reward = wasted or harmful (§4⑤ mismatch).

  🟡 "Reward for no-gap = wasted" = Gap-Direction.md core principle applied
```

---

## §2 — 3 GAP TYPES × REWARD MATCH

```
⭐ 3 CHUNK DYNAMICS (Body-Feedback-Mechanism.md §3) × APPROPRIATE REWARD:

  Each gap type has a DIFFERENT nature → DIFFERENT reward match:

  ┌──────────────┬──────────────────────────────┬──────────────────────────────┐
  │ Gap Type     │ Nature                       │ Reward Match                 │
  ├──────────────┼──────────────────────────────┼──────────────────────────────┤
  │ CHUNK-SHIFT  │ Context has changed →        │ RE-ANCHOR reward:            │
  │ (Body-Feedback-Mechanism §3.1)│ old baseline no longer fits. │ help build a NEW baseline    │
  │              │ "Moving cities, changing     │ in the NEW context.          │
  │              │ jobs, losing someone."       │                              │
  │              │                              │ = Direct-State effective     │
  │              │ Body is RE-CALIBRATING       │ (body-state: touch, exercise,│
  │              │ entire baseline → unstable   │ grounding, sleep, routine)   │
  │              │                              │                              │
  │              │                              │ ⚠️ Evaluative layer          │
  │              │                              │ MAY NOT WORK YET:            │
  │              │                              │ old chunks no longer         │
  │              │                              │ relevant → evaluation wrong  │
  ├──────────────┼──────────────────────────────┼──────────────────────────────┤
  │ CHUNK-MISS   │ Expected X, received less.   │ COMPENSATE reward:           │
  │ (Body-Feedback-Mechanism §3.2)│ "Expected higher salary,  │ fill the delta OR adjust     │
  │              │ received less." "Expected    │ the expectation.             │
  │              │ praise, received criticism." │                              │
  │              │                              │ = Evaluative layer:          │
  │              │ Body detects: actual <       │ PFC compares + evaluates →   │
  │              │ compiled expectation         │ opioid when delta fills      │
  │              │ → SNC (Crespi 1942)          │                              │
  │              │                              │ ⚠️ 2 PATHS (important):      │
  │              │                              │ Path A: fill delta (raise    │
  │              │                              │ actual → match expectation)  │
  │              │                              │ Path B: adjust expectation   │
  │              │                              │ (lower compiled → match      │
  │              │                              │ actual). BOTH can be healthy │
  ├──────────────┼──────────────────────────────┼──────────────────────────────┤
  │ CHUNK-GAP    │ Structure predicts C         │ EXPLORATION reward:          │
  │ (Body-Feedback-Mechanism §3.3)│ should exist → C not yet   │ bridge through exploration   │
  │              │ compiled → HOLE.             │ → chunk fills → opioid.      │
  │              │ "Don't know yet, want to     │                              │
  │              │ know." "Unsolved problem."   │ = prediction-delta (novelty) │
  │              │                              │ when new chunk matches gap → │
  │              │ Body detects: surrounding    │ + opioid when filled         │
  │              │ chunks predict C but C       │ = Profile ② Coherence        │
  │              │ is missing                   │ (Reward-Signal-Architecture §4) │
  └──────────────┴──────────────────────────────┴──────────────────────────────┘

  🟢 SNC: Crespi 1942, Flaherty 1996
  🟢 Dopamine prediction-delta: Schultz 1997
  🟡 Gap type × Reward match mapping = framework synthesis
```

### §2.1 — Wrong reward type for wrong gap = WASTED or HARMFUL

```
⭐ REWARD CALIBRATION IS NOT ONLY ABOUT AMOUNT — ALSO ABOUT TYPE:

  Example 1: Chunk-Miss (salary expectation gap) → given Direct-State (massage, spa)
    → Body is "expected X, received less" → needs evaluative resolution
    → Massage = body-state improvement → CORRECT Direct-State, BUT:
    → ROOT GAP (salary < expectation) REMAINS → dissonance REMAINS
    → = Right type of reward but for the wrong gap → only temporary

  Example 2: Chunk-Gap (wants to understand a problem) → given money
    → Body is "C should exist but missing" → needs exploration fill
    → Money = proxy token → DOES NOT match coherence gap
    → Gap (not understanding the problem) REMAINS → reward = empty
    → ⚠️ CAN BE HARMFUL: if money is STRONGER than exploration drive
      → overjustification (§4②): only solves the problem for money → stop when money stops

  Example 3: Chunk-Shift (losing someone important) → given logical advice
    → Body is RE-CALIBRATING entire baseline → unstable
    → Logic = Evaluative layer → old chunks invalidating → evaluation WRONG
    → Body NEEDS: Direct-State grounding (physical presence, touch, routine)
    → Advice = RIGHT type but WRONG timing
    → = "Person is drowning and you're lecturing them"

  PRINCIPLE:
    → Match gap TYPE first, then calibrate AMOUNT
    → Wrong type → no amount will fix it
    → Analogous to Gap-Direction.md: reward must match the SPECIFIC DIRECTION

  🟡 "Wrong type = wasted" = logical consequence of Gap-Direction principle
```

---

## §3 — GOLDILOCKS ZONE: 3 STATES

### §3.1 — Under-reward (too little for the gap)

```
⭐ UNDER-REWARD = GAP NOT FILLED → DISSONANCE PERSISTS:

  MECHANISM:
    Gap exists → body detects → cortisol fires (amplifier)
    Reward arrives but NOT ENOUGH to fill gap → gap REMAINS
    → Cortisol Role ② Holding: "not done yet" → PFC tracking pending
    (Cortisol-Baseline.md §7.7)
    → Prolonged → CAN shift to Role ③ Threat-sustained
    (if gap relates to survival or social standing)

  DIRECTION SHIFT:
    Prolonged under-reward → approach tag CAN flip to avoidance:
    → "I try → insufficient reward → try more → still insufficient"
    → Chunk compiles with avoidance tag: "this domain = effort > reward"
    → = Learned helplessness pattern
    (Cortisol-Baseline.md §7.7 Role ① Compile Direction)

  EXAMPLES:
    Salary far below competence level:
      → Gap: competence >> reward → continuous Chunk-Miss
      → Cortisol sustained → departure or burnout
      → Status.md §1: Resource Access Map skewed → "I access less than I deserve"

    Child never praised despite effort:
      → Gap: effort → no recognition → Chunk-Miss
      → Prolonged → avoidance compiled: "trying = useless"
      → = Foundation for Background-Pattern.md [effort → insufficient return]

    Relationship lacking connection:
      → Gap: hardware social drive fires → insufficient response
      → Connection.md §9: one-sided calibration → dissonance
      → Body feels "lonely" despite having people nearby

  🟢 Learned helplessness: Seligman 1967
  🟢 Cortisol sustained: McEwen 1998 (allostatic load)
  🟡 Under-reward → direction shift = framework synthesis
```

### §3.2 — Match (just enough for the gap)

```
⭐ MATCH = SWEET SPOT → SUSTAINABLE:

  MECHANISM:
    Reward matches gap → prediction-delta → body-base reward → gap fills
    → Chunk compiles with approach tag
    → Body state: brief positive → resets → ready for next gap
    → = Healthy perception-action cycle

  RECOGNITION MARKERS:
    → Drive SELF-SUSTAINING: no continuous external push needed
    → Approach tags accumulate: "this domain = effort → reward"
    → Cortisol healthy: spike → resolves → returns to baseline
    → Baseline STABLE (doesn't shift up too fast)

  BUT — MATCH IS NOT FIXED:
    → Today's match CAN = tomorrow's under-reward
    (baseline shift: Gratitude.md §4 — reward habituates)
    → Match for this person ≠ match for that person
    (hardware: PFC-Hardware.md §3.4 — COMT × Reward Pattern)
    → Match in this context ≠ match in that context
    (cortisol state, relationship, Background-Pattern)

  EXAMPLES:
    Salary matching competence + recognition at right moments:
      → Chunk-Miss minimized → drive stable
      → Approach tags accumulate → loyalty emerges
      → = "Not rich but enjoy going to work"

    Child learning piano: chunks compile → opioid → "this sounds good!":
      → Gap fills → exploration continues → curiosity emerges
      → Bridge (source ④) gradually withdraws → sources ①②③ take over
      (Education-Mechanism.md §3.4)

  🟡 Match = sustainable = framework synthesis
```

### §3.3 — Over-reward (too much for the gap → §4)

```
⭐ OVER-REWARD = SURPLUS REWARD WITH NO MATCHING GAP:

  MECHANISM:
    Gap fills → reward KEEPS ARRIVING → surplus
    Surplus reward = NO gap to match → where does it go?

    3 DIRECTIONS SURPLUS REWARD GOES:
    ① Threshold adaptation → need MORE next time (§4①)
    ② Creates dependency → losing reward hurts even though it was originally a bonus (§4③④)
    ③ Imbalance → system skews → problems elsewhere (§4⑤⑥)

  WHY OVER-REWARD IS MORE DANGEROUS THAN UNDER-REWARD:
    → Under-reward: body knows "insufficient" → clear signal → CAN adjust
    → Over-reward: body is "pleasant" → DOES NOT signal "too much" → blind
    → = Over-reward is invisible → hard to recognize → hard to fix
    → Like Cortisol-Baseline.md Role ⑤ Silent:
      cortisol HIGH but NOT FELT → damage accumulates
    → Over-reward = "silent surplus" → damage accumulates

  → Details on 6 mechanisms: §4

  🟡 Over-reward harder to detect = framework inference
```

### §3.4 — Over-reward at CHUNK LEVEL: premature compilation

```
⭐ META-PRINCIPLE: OVER-REWARD FORCES CHUNK COMPILATION BEFORE SUFFICIENT FOUNDATION:

  Body-base = the side that ACTS + gathers information + engages with real domains.
  Body-base accumulates chunks → forms chunk-gaps → drive fills gaps
  = NATURAL PROCESS.

  Over-reward = reward EXCEEDING current chunk-gap:
    → Body receives surplus → doesn't yet have ENOUGH foundational chunks to evaluate/use it
    → But body MUST compile new chunks to PROCESS the surplus
    → Compiles IN CONTEXT of insufficient foundation → chunks SKEWED from the start
    → Skewed chunks → BECOME FOUNDATION for subsequent chunks → cascade
    → = Background-Pattern.md: skewed patterns accumulate → pervasive bias

  3 CASES — NOT ALL OVER-REWARD IS HARMFUL:

  CASE 1 — E₀ HARDWARE REJECT (HARMLESS):
    Too much sugar → sickening → body rejects IMMEDIATELY → DOESN'T compile wrong chunks
    → E₀ = hardware Goldilocks (Reward-Signal-Architecture §2.1) → immediate feedback
    → Body knows "too much" at hardware level → stops → harmless

  CASE 2 — NO GAP (HARMLESS):
    A 3rd-grade child given a luxury car → no car-related gap yet → no gap match
    → Body: "a big thing" → doesn't compile anything deep → harmless
    → = Gap-Direction.md §3: "unknown = no gap"
    → Reward falls into empty space → creates no damage

  CASE 3 — GAP EXISTS BUT DEPTH INSUFFICIENT (DANGEROUS ⚠️):
    Schema drive EXISTS (money = proxy, infinite gap) + gap EXISTS (want more)
    BUT foundational chunks INSUFFICIENT to evaluate + use reward properly.

    Lottery winner:
      → Gap [need money] EXISTS → reward matches gap type
      → BUT: chunks for "managing large wealth" DON'T EXIST
      → Body MUST compile "wealth management" chunks from scratch
      → Compiles IN CONTEXT of insufficient foundation → chunks often WRONG:
        [money is easy to come by] [can buy anything] [no need to be careful]
      → Wrong chunks → wrong decisions → lose money → intense SNC
      → 🟢 ~70% lottery winners = worse off within years

    Salary exceeding competence (§4⑤ details):
      → Gap [need money] EXISTS → reward matches gap type
      → BUT: chunks for "competence at this level" INSUFFICIENT
      → Body compiles: [high access] but LACKING [I deserve this access]
      → = Imposter syndrome + surrounding people recalibrate → double pressure
      → Chunks compile IN DISSONANCE → approach/avoidance MIXED

    Large inheritance:
      → Transfer WITHOUT effort → wealth chunks compile
        WITHOUT accompanying effort chunks
      → = "Having money but not knowing why you have it"
      → Background-Pattern forms: [money = comes freely]
      → Biases all subsequent financial decisions

  WHY CASE 3 IS MORE DANGEROUS THAN CASE 1+2:
    → Case 1: hardware feedback IMMEDIATE → stops → no wrong compilation
    → Case 2: no gap → compiles nothing → no damage
    → Case 3: gap EXISTS + drive EXISTS + foundation INSUFFICIENT → MUST compile
      → Compilation occurs DESPITE NOT BEING READY
      → Wrong chunks → BECOME foundation → cascade
      → = "Double-edged sword" — reward CAN genuinely improve body-base
        (actually wealthier), but SIMULTANEOUSLY creates skewed chunks

  🟢 Lottery winner outcomes: Brickman 1978, Hankins et al. 2011
  🟡 Premature compilation under over-reward = framework synthesis
  🟡 3-case distinction = framework analysis
```

---

## §4 — OVER-REWARD: 6 HARMFUL MECHANISMS

```
⭐ 6 MECHANISMS — each is a different pathway through which surplus reward causes harm:

  Not all 6 occur simultaneously.
  Also not necessarily just 1 mechanism per case.
  = Combination varies by case, person, context.
```

### §4.1 — ① THRESHOLD ADAPTATION (hedonic treadmill)

```
⭐ CONTINUOUS REWARD → BASELINE RISES → SAME REWARD = LOWER PREDICTION-DELTA:

  MECHANISM (Gratitude.md §3.1 + §4):
    Gift first time → VTA fires delta → opioid → reward → "pleasant"
    Gift times 2-10 → VTA gradually habituates → reward DECREASES
    Gift times 50-100+ → VTA fully habituated → gift = INVISIBLE
    → Need NEWER, LARGER reward to generate positive prediction-delta
    → = Hedonic treadmill: running constantly, position DOES NOT ADVANCE

  EXAMPLES:
    Salary: $100K → adapt → $500K → adapt → $1M → "still not enough"
    Sugar: medium sweet → adapt → need SWEETER → adapt → need SWEETER STILL
    Praise: "good" → adapt → "excellent" → adapt → "genius" → adapt
    → Every level becomes "the new normal"

  WHY SOMEONE "COMFORTABLE" STILL FEELS "LACKING":
    → Body GENUINELY lacks — because baseline HAS SHIFTED
    → Not "greediness" — it's biological threshold that has calibrated upward
    → Stopping at current level → actual < shifted baseline → negative prediction-delta → "lacking"
    → = Not greed, but threshold adaptation

  🟢 Hedonic treadmill: Brickman & Campbell 1971, Frederick & Loewenstein 1999
  🟢 VTA habituation: Schultz 1997 (predicted reward → no dopamine signal)
  🟢 Hedonic adaptation: Brickman 1978 (lottery winners return to baseline)
```

### §4.2 — ② OVERJUSTIFICATION (external kills internal)

```
⭐ EXTERNAL REWARD STRONGER THAN INTERNAL PREDICTION-DELTA → BRAIN ONLY TRACKS EXTERNAL:

  MECHANISM (Education-Mechanism.md §3.1):
    Before: behavior had intrinsic prediction-delta (internal drive) → did it because ENJOYED it
    Add strong external reward → brain switches tracking to external
    (external > internal → VTA tracks STRONGER source)
    Remove external → prediction-delta = 0 (internal already suppressed) → STOPS behavior

  EXAMPLES:
    Pay a child to draw → draws for money → money stops → stops drawing
    (EVEN THOUGH previously drew because enjoyed it)

    Reward candy for studying → studies for candy → candy stops → stops studying
    (EVEN THOUGH previously was curious to know)

    Bonus for creativity → creates for bonus → bonus cut → creativity stops
    (EVEN THOUGH previously had internal creative drive)

  BRIDGE PARALLEL (Education-Mechanism.md §3.1):
    → Bridge = external injection (source ④) KEEPING student engaged
    → CORRECT bridge = smallest possible → wait for sources ①②③ to emerge → phase out
    → OVERDOSED bridge = overjustification → source ④ dominates → ①②③ suppressed
    → = "Medication overdose → poisoning" (Education-Mechanism.md §3.1)

  🟢 Overjustification effect: Deci 1971, Lepper et al. 1973
  🟢 Self-Determination Theory: Deci & Ryan 1985, 2000
```

### §4.3 — ③ BRIDGE DEPENDENCY (removing bridge = anchor crash)

```
⭐ SOURCE ④ DOMINATES TOO LONG → SOURCES ①②③ NEVER EMERGE:

  MECHANISM (Education-Mechanism.md §3.4):
    4 anchor fill sources: ① PFC Imagine-Final, ② Hippocampus experience,
    ③ Compiled schemas, ④ External injection (bridges).
    Correct bridge: ④ holds → ①②③ grow → ④ gradually withdraws → HEALTHY transition
    Bridge dependency: ④ dominates 100% → ①②③ DO NOT develop
    → Remove ④ = anchor crash (Anchor-Schema.md: sync point lost)
    → "Nobody tells me what to do anymore → I don't know what I want"

  DIFFERS FROM OVERJUSTIFICATION:
    ② Overjustification: external KILLS internal that already existed
    ③ Bridge dependency: external PREVENTS internal from FORMING
    → ② = destroys existing. ③ = prevents emergence.
    → ③ more serious: ② can still restore (recover suppressed internal),
      ③ requires BUILDING FROM SCRATCH (internal never existed)

  EXAMPLES:
    Child only studies with candy → no candy = no studying
    → Candy for 12 years → source ① (knowing what they want) NEVER DEVELOPED
    → Enters adult life → "quarter-life crisis" → ~50-60% motivation disappears
    (Education-Mechanism.md §3.4 → mass schooling pattern)

    Employee only works for bonus → no bonus = no effort
    → Bonus for 10 years → internal drive NEVER FORMED for the domain
    → Cut bonus = collapse → "I only work for money"

  🟢 Extrinsic motivation crowding: Frey & Jegen 2001
  🟡 Bridge dependency vs overjustification distinction = framework synthesis
```

### §4.4 — ④ BASELINE SHIFT (gift habituates → loss hurts)

```
⭐ CONTINUOUS GIFT → BASELINE SHIFTS → SAME GIFT = PREDICTION-DELTA ≈ 0:

  MECHANISM (Gratitude.md §4):
    Baseline compilation formula:
      compile_rate ≈ f(repetition × saliency × peak_valence × multi_modal × contingency)
    High repetition → strong baseline shift → gift = baseline = INVISIBLE
    Losing gift → actual < compiled baseline → SNC → "anger"
    (even though the gift was originally a BONUS, not an entitlement)

  DIFFERS FROM THRESHOLD ADAPTATION:
    ① Threshold adapt: need MORE to get reward at the SAME LEVEL
    ④ Baseline shift: same reward = prediction-delta ≈ 0 (invisible), LOSS HURTS
    → ① = reward GRADUALLY DECREASES. ④ = reward DISAPPEARS + losing it = NEGATIVE.
    → ④ more dangerous: not just "need more" but "losing it = crisis"

  EXAMPLES:
    Company car → used 5 years → habituated → "normal"
    → Lose car = negative prediction-delta even though car was originally a bonus
    → Like SNC (Crespi 1942): downshift from high baseline → anger, not sadness

    Home-cooked meals 10,000 times → habituated → invisible
    → Move away for 5 years → VTA habituation DECAYS → return and eat = "intensely pleasant"
    → = Variation (Gratitude.md §3.2) resets baseline

    Continuous social media likes → baseline = "must have likes"
    → One post with no likes → SNC → "is something wrong?"

  🟢 SNC: Crespi 1942, Flaherty 1996
  🟢 Hedonic adaptation: Brickman 1978
  🟡 Baseline shift → loss = negative = framework synthesis from Gratitude.md §4
```

### §4.5 — ⑤ COMPETENCE-REWARD MISMATCH (2 directions)

```
⭐ REWARD AND COMPETENCE MISALIGNED → DISSONANCE:

  MECHANISM:

  DIRECTION A — Reward > Competence (Imposter):
    → Receives reward MUCH higher than actual competence → body detects mismatch
    → Status.md §1: Resource Access Map = I ACCESS more than I deserve
    → Body: "this access is unsustainable" → cortisol rises (uncertainty)
    → Surrounding people: detect mismatch → social recalibration
    → "If one side won't adjust, the other side must"
      = Collective adjustment to rebalance access map
    → Example: promoted too quickly → imposter feelings + team friction

  DIRECTION B — Competence > Reward (Undervalued):
    → Actual competence GENUINELY exceeds received reward → continuous Chunk-Miss
    → Body: "I GIVE more than I RECEIVE" → resentment accumulates
    → Prolonged → departure or quiet quitting
    → Example: senior engineer paid same as junior → "not valued properly"

  BOTH DIRECTIONS ARE DYNAMIC:
    → Direction A: surroundings adjust back (lower expectations, increase scrutiny)
    → Direction B: person adjusts (find elsewhere, reduce effort)
    → = Dynamic equilibrium: both sides continuously adjust
    → Connection.md §9: calibration = 2 bodies tuning each other

  🟡 Competence-reward mismatch = Status.md Resource Access Map × Chunk-Miss
  🟡 Dynamic equilibrium = framework synthesis
```

### §4.6 — ⑥ EVALUATIVE/DIRECT-STATE IMBALANCE (one type too dominant)

```
⭐ TOO MUCH EVALUATIVE OR TOO MUCH DIRECT-STATE → IMBALANCE:

  MECHANISM (Reward-Signal-Architecture §1-§3):

  TOO MUCH EVALUATIVE:
    → E₃ threshold HIGH (Reward-Signal-Architecture §2.1: E₀→E₃ gradient)
    → Simple pleasures NOT ENOUGH prediction-delta to clear threshold
    → Direct-State Reward STILL WORKS (hardware) but PFC "dismisses" it (accustomed to E₃)
    → = "Accomplished but cannot feel joy"
    → E₃ evaluative = complex, conditional, EASILY habituated
    → Direct-State = hardware, simple, RELIABLE but NEGLECTED

  TOO MUCH DIRECT-STATE:
    → Body-state comfort HIGH but evaluative depth LOW
    → No chunk compilation for E₂-E₃ → no coherence reward
    → = "Enjoyable but feels empty" (fun without depth)
    → Meaning.md: no GOAL/STATE/IDENTITY anchor → no meaning

  EVALUATIVE/DIRECT-STATE RATIO NEEDS BALANCE:
    → Maximize Evaluative alone → lose Direct-State → lose safe baseline
    → Maximize Direct-State alone → lose Evaluative → lose depth + meaning
    → = Evaluative/Direct-State ratio = a calibration parameter in its own right

  EVALUATIVE GATES DIRECT-STATE IMPLICATION (Reward-Signal-Architecture §3):
    → Strong Evaluative calibration → Direct-State experience AMPLIFIED (E₃ anchor amplifies)
    → Weak Evaluative calibration → Direct-State experience "flat" (no gate to amplify through)
    → Over-calibrate Evaluative → BLOCKS Direct-State gate → "understand everything but can't feel it"
    → = "Expert wine taster no longer enjoys casual wine"

  🟡 Evaluative/Direct-State imbalance = Reward-Signal-Architecture Evaluative/Direct-State + Meaning.md synthesis
  🟡 Evaluative Gates Direct-State implication for calibration = framework inference
```

---

## §5 — DYNAMIC EQUILIBRIUM: WHY PRESCRIBING IS IMPOSSIBLE

### §5.1 — Parallel with Logic-Feeling-Balance.md

```
⭐ REWARD CALIBRATION = CANNOT PRESCRIBE — SAME REASON:

  Logic-Feeling-Balance.md §6-§7:
    → Try to create a rule → every rule has a blind spot
    → Try a meta-rule → the meta-rule also has a blind spot
    → = Infinite regress → NO stopping point
    → = Gödel-like incompleteness at the cognitive level

  Reward Calibration SAME PATTERN:
    → Try to prescribe "give X reward for gap Y" → fails because:

    ① Different person → DIFFERENT sweet spot
       (hardware: COMT, DRD4, receptor sensitivity — PFC-Hardware.md §3.4)
    ② Different context → DIFFERENT sweet spot
       (cortisol state, relationship, Background-Pattern — dynamic)
    ③ Different time → DIFFERENT sweet spot
       (baseline shift, development stage, habituation — Gratitude.md §4)
    ④ Different gap → DIFFERENT sweet spot
       (Shift/Miss/Gap, direction, depth — Gap-Direction.md)

    → = 4 dimensions ALL dynamic → fixed formula CANNOT cover
    → Try meta-formula "adjust per person per context per time per gap"
    → Meta-formula = itself a fixed formula → SAME problem
    → = Infinite regress

  🟡 Reward calibration ≡ Logic-Feeling balance = framework parallel
  🟡 Infinite regress = Gödel-like incompleteness applied to reward
```

### §5.2 — Perception-action cycle: domain feedback is the only arbiter

```
⭐ REWARD CALIBRATION = PERCEPTION-ACTION CYCLE:

  Manager ↔ employee:
    → Manager gives reward → employee responds → manager observes → adjusts
    → Employee gives effort → manager responds → employee observes → adjusts
    → 2 BODIES tuning each other continuously (Connection.md §9)
    → NO fixed point — only TEMPORARY equilibrium

  Parent ↔ child:
    → Bridge (source ④) → child responds → observe → adjust bridge
    → Child develops ①②③ → bridge gradually withdraws → observe → adjust further
    → = CONTINUOUS calibration, not "withdraw all bridge on day X"

  Society ↔ individual:
    → Obligation (society expects) ↔ Autonomy (individual wants)
    → 2 forces adjust continuously → equilibrium shifts with context
    → Obligation.md: 5-factor formula = observation, not prescription

  DOMAIN FEEDBACK = THE ONLY ARBITER:
    → No one OUTSIDE can know the sweet spot of someone INSIDE
    → Only: observe response → adjust → observe → adjust
    → = Dynamic equilibrium, NOT a fixed formula
    → Each person SELF-CALIBRATES (Logic-Feeling-Balance.md §10)

  WHY THIS FILE HELPS (even without prescribing):
    → Helps RECOGNIZE: "which zone is reward currently in" (under / match / over)
    → Helps UNDERSTAND: "which mechanism is running" (6 mechanisms §4)
    → Helps AVOID: common traps (wrong type, wrong amount, wrong timing)
    → = Describes, does NOT prescribe (Logic-Feeling-Balance.md §8.1)

  🟡 Perception-action cycle for reward = dynamic equilibrium
  🟡 Domain feedback = only arbiter = Logic-Feeling-Balance.md core
```

### §5.3 — Why this is NORMAL

```
  IF reward calibration COULD be perfectly prescribed:
    → There would be no need to observe responses
    → There would be no need to adjust
    → There would be no need for relationship
    → There would be no need to LIVE through experience

  = Perfect prescription = omniscience
  = Humans ≠ omniscient (Logic-Feeling-Balance.md §7.4)
  = Therefore: cannot prescribe = CORRECT, NORMAL, EXPECTED

  Dynamic equilibrium between giver and receiver is NOT a problem.
  It IS the mechanism:
    → Giver observes → adjusts → receiver responds → giver observes → ...
    → INFINITE LOOP = relationship, management, parenting, teaching
    → Every attempt to shortcut the loop = fails (prescribing = shortcut)

  🟡 Cannot prescribe = expected = framework epistemological position
```

### §5.4 — Collective Calibration: markets as natural anti-over-reward

```
⭐ DYNAMIC EQUILIBRIUM IS NOT ONLY 2-BODY — ALSO AT SOCIAL SCALE:

  §5.2 describes 2-body calibration (manager↔employee, parent↔child).
  But at larger scale: MARKETS = collective calibration
  of MILLIONS of deals simultaneously.

  MECHANISM:
    Each deal = 2+ parties, each party has their OWN gap:
      Manager: gap "need someone to do the work" → willing to pay
      Employee: gap "need money + meaning" → willing to work
      → Negotiation = 2 gaps INTERSECTING → equilibrium point

    "Everyone wants maximum" = each party pushes max per deal
    "Everyone receives a certain amount" = equilibrium after negotiation
    = Status.md §5: exchange = MOST COMMON mode in modern humans

    Market = collective equilibrium:
      → Wage = "compromise point" that IS CURRENTLY WORKING
      → Nobody prescribes → emerges from millions of negotiations
      → = Dynamic equilibrium at SOCIAL SCALE

  COLLECTIVE CALIBRATION = NATURAL ANTI-OVER-REWARD MECHANISM:

    In a normal market:
      → Side A wants to pay LEAST → side B wants to receive MOST
      → 2 forces PULLING OPPOSITE → equilibrium in MATCH ZONE
      → = Over-reward BLOCKED by the other side of the deal
      → = "If one side won't yield, the other side must"

    Why it works:
      → Each side has CONSTRAINTS (budget, alternative options, market rate)
      → Constraints → cap reward at reasonable zone
      → = Collective → equilibrium → match zone → sustainable

  OVER-REWARD OCCURS WHEN COLLECTIVE CALIBRATION IS BROKEN:

    ① Lottery:
       → Reward is RANDOM → doesn't go through negotiation → no calibration
       → Surplus without anchor → premature compilation (§3.4 Case 3)

    ② Power imbalance:
       → One side has UNUSUAL leverage → pushes reward too far one direction
       → Example: monopoly, corruption, nepotism
       → Receiver over-rewarded → §4⑤ competence-reward mismatch
       → BUT: surroundings will RECALIBRATE
         (Status.md §6: disruption → recalibrate → new stability)

    ③ Inheritance / transfer without deal:
       → Wealth transfer WITHOUT effort → no calibration
       → Wealth chunks compile WITHOUT deal experience
       → = §3.4 Case 3: gap exists + drive exists, depth insufficient

    ④ Schema [money = the best] + normal salary:
       → Collective calibration WORKS → reward at equilibrium
       → Schema drive STILL WORKS → because reward MATCHES real gap
       → = NOT over-reward → NO problem
       → = Most people, most of the time → STABLE

  = Collective calibration like IMMUNE SYSTEM for over-reward:
    → Normal: prevents surplus naturally (deal = equilibrium)
    → When broken: over-reward enters → damage (§4)
    → Cross-ref: Status.md §5 (exchange as positive-sum),
      Obligation.md §5.2 (money as obligation technology)

  🟡 Collective calibration as anti-over-reward = framework synthesis
  🟢 Market equilibrium: Adam Smith 1776, supply/demand
  🟢 Lottery winner outcomes: Brickman 1978
```

---

## §6 — OBSERVABLE INDICATORS

### §6.1 — Observing through communication + behavior

```
⭐ REWARD STATE CAN BE OBSERVED — PROBABILISTIC, NOT CERTAIN:

  ⚠️ IMPORTANT:
    → Observable = probabilistic, NOT diagnostic
    → Same behavior CAN = many different root causes
    → AI-Schema-Detection.md: 3-layer model applies
      Layer 1: observe patterns
      Layer 2: expert verifies mechanism
      Layer 3: self confirms (body knows best)
    → This file = Layer 1 (observe) → REQUIRES Layer 2+3 to confirm
```

### §6.2 — Under-reward signals

```
  VERBAL (through communication):
    → "Not valued" / "nobody appreciates what I do"
    → "Bored" (but in a "nothing is coming back" way, different from Boredom)
    → "Not enough" / "need more" (genuine, not threshold adaptation)
    → "I try and nobody notices"
    → Implicit: talks LITTLE about the domain, low energy when discussing

  BEHAVIORAL (through behavior):
    → Effort gradually decreasing (diminishing input → diminishing reward expectation)
    → Seeking alternative sources (side job, new relationship, alternative domain)
    → Avoidance accumulating ("lazy" = may be compiled avoidance)
    → Withdrawal (retreating from related social contexts)

  BODY (through observation):
    → Sustained cortisol visible: fatigue, poor sleep, irritability
    → Chronically low energy (different from boredom: boredom = high arousal)
    → Drive collapse signs (Cortisol-Baseline.md Role ② → ③)

  ⚠️ "Bored" CAN = Boredom.md (high arousal + unclear Imagine-Final)
     OR = under-reward (low reward → avoidance). Distinguish by context.
```

### §6.3 — Match signals

```
  VERBAL (through communication):
    → TALKS LITTLE ABOUT REWARD (habituated = invisible — Gratitude.md §4!)
    → Talks more about the DOMAIN than about the reward
    → "I enjoy this" (approach-directed, not reward-directed)
    → No complaints, but also no enthusiastic praise

  BEHAVIORAL (through behavior):
    → Stable: drive self-sustaining, doesn't need constant external push
    → Approach tags visible: returns to domain on their own
    → Growth: chunks accumulate → skill increases → natural progression
    → Low maintenance: minimal external intervention needed

  BODY (through observation):
    → Baseline stable (cortisol healthy cycle: spike → resolves → resets)
    → Adequate energy level
    → Normal sleep pattern

  ⚠️ MATCH LOOKS "NORMAL" — EASY TO OVERLOOK:
    → Gratitude.md §3.1: gift habituates → invisible → "normal"
    → Match = BEST STATE but INVISIBLE because prediction-delta ≈ 0
    → Only SEEN through comparison: "before (under) vs now (match)"
    → = Paradox: best state = least visible
```

### §6.4 — Over-reward signals (per mechanism §4)

```
  ① THRESHOLD ADAPTATION:
    → "Not enough" DESPITE objectively high levels + peer comparison
    → "Why does someone else have it but not me yet?" — social comparison dominant
    → Speed of "getting bored" INCREASES: new reward → excited → adapted → "next" FASTER
    → = "Running without arriving" (treadmill behavior)

  ② OVERJUSTIFICATION:
    → "Won't do it if nobody pays" for something PREVIOUSLY ENJOYED
    → Only discusses reward (money, bonus) rather than domain (skill, impact)
    → Remove external reward → immediate behavioral collapse
    → = "Music stops when money stops" (even though originally played for enjoyment)

  ③ BRIDGE DEPENDENCY:
    → Panic when bridge is reduced: "what if there's no X?"
    → NO visible internal drive: "what do I want? I don't know"
    → Quarter-life crisis pattern (Education-Mechanism.md §3.4)
    → = "Only knows how to follow instructions, doesn't know what they want"

  ④ BASELINE SHIFT:
    → "Used to it" — discusses reward as entitlement
    → LOSING reward → DISPROPORTIONATELY STRONG reaction (anger, not sadness)
    → "Why is this being taken away?" — even though reward was a bonus, not a contract
    → = SNC pattern (Crespi 1942)

  ⑤ COMPETENCE-REWARD MISMATCH:
    → Direction A (imposter): "I don't deserve this" + friction with peers
    → Direction B (undervalued): "nobody values me correctly" + resentment
    → Team dynamics shift: envy, scrutiny, passive resistance
    → = Status.md Resource Access Map skewed visible through social behavior

  ⑥ EVALUATIVE/DIRECT-STATE IMBALANCE:
    → "Accomplished but unhappy" (Evaluative excess, Direct-State neglect)
    → "Enjoyable but feels empty" (Direct-State excess, Evaluative absent)
    → Simple pleasures feel "flat" (Evaluative threshold too high)
    → Meaning void despite material comfort (Meaning.md anchor absent)
```

---

## §7 — EVALUATIVE/DIRECT-STATE × CALIBRATION

### §7.1 — Evaluative calibration = complex

```
⭐ EVALUATIVE — COMPLEX GOLDILOCKS:

  Evaluative = conditional, all 5 Body-Feedback-Preconditions required (Reward-Signal-Architecture §1.3)
  → Threshold ADAPTS: E₀→E₃ gradient → threshold rises with experience
  → Habituation: VTA habituates → same stimulus = lower prediction-delta → needs NOVELTY
  → Context-dependent: body state, relationship, cortisol → ALL affect it
  → Per-person: COMT × Childhood = 4 trajectories (PFC-Hardware.md §3.5)

  EVALUATIVE CALIBRATION NEEDS ANTI-HABITUATION:
    → Gratitude.md §3: 3 mechanisms (Variation, Comparison, Ritual)
    → Without anti-habituation → Evaluative reward decays → anhedonia
    → = "Everything is fine but can't feel anything" = Evaluative threshold HIGH + no delta

  E₃ = PEAK COMPLEXITY (Reward-Signal-Architecture §2.1):
    → Multi-domain coherence + compound insight + meta-evaluation
    → Threshold VERY HIGH → E₃ reward = RARE
    → When present: POWERFUL (opioid + dopamine + cortisol drop compound)
    → When absent: "chronic anhedonia" (baseline E₃ → everything below = "meh")
    → = Expert/professional hazard: E₃ calibrated → simple pleasures no longer sufficient

  🟡 Evaluative calibration complexity = Reward-Signal-Architecture + Gratitude synthesis
```

### §7.2 — Direct-State calibration = simpler but important

```
⭐ DIRECT-STATE — SIMPLER GOLDILOCKS:

  Direct-State = hardware-based, simplified Body-Feedback-Preconditions (Reward-Signal-Architecture §1.3)
  → Threshold BARELY ADAPTS: body-state sensors = stable
  → Habituation: MINIMAL (body-level adaptation only, not VTA)
  → = RELIABLE baseline reward (Reward-Signal-Architecture §1.4: "evolutionary floor")

  DIRECT-STATE = SAFE BASELINE WHEN EVALUATIVE IS EXHAUSTED:
    → Burnout/anhedonia: Evaluative exhausted → Evaluative reward OFF
    → Direct-State STILL accessible: touch, exercise, warmth, stretching
    → = "Backdoor" past exhausted Evaluative gate
    → 🟢 Van der Kolk 2014: body-oriented therapy for trauma

  DIRECT-STATE CALIBRATION:
    → Goldilocks: body-state range (CT afferents ~1-10cm/s — Reward-Signal-Architecture §1.1)
    → Under Direct-State: body neglected (no touch, no movement) → baseline LOW
    → Match Direct-State: regular body-state engagement → stable baseline
    → Over Direct-State: rare but possible (exercise addiction, sensory overload)
    → = Direct-State calibration = KEEPING hardware channels active

  🟡 Direct-State = reliable + simple calibration = Reward-Signal-Architecture §1.4 synthesis
```

### §7.3 — Evaluative Gates Direct-State: calibration interaction

```
⭐ EVALUATIVE CALIBRATION AFFECTS DIRECT-STATE EXPERIENCE (Reward-Signal-Architecture §3):

  Evaluative Gates Direct-State mechanism (Reward-Signal-Architecture §3):
    → Strong E₃ anchor → sensory experience EVEN MORE POWERFUL
    → Weak E₃ anchor → sensory experience "flat"
    → = Evaluative calibration INDIRECTLY affects Direct-State quality

  CALIBRATION IMPLICATIONS:
    → Over-calibrate Evaluative → threshold HIGH → blocks Direct-State gate
    → = "Understand everything but can't feel it"
    → = Expert wine taster can't enjoy casual wine
    → = Musician can't enjoy pop music

    → Under-calibrate Evaluative → Evaluative threshold LOW → gate ineffective
    → = "Can feel but can't go deep"
    → = Enjoy but shallow

    → BALANCE Evaluative + Direct-State = both feed each other:
    → Evaluative depth → Direct-State amplifies → Direct-State experience → new Evaluative insight → ...
    → = Virtuous cycle when balanced

  🟡 Evaluative Gates Direct-State × Calibration = Reward-Signal-Architecture §3 inference
```

---

## §8 — REWARD-ECONOMICS INSIGHTS THROUGH V7.8 LENS

### §8.1 — 6 paths to "wealthy yet still chasing money" (from Reward-Economics.md)

```
⭐ 6 PATHS → MAPPED TO V7.8 MECHANISMS:

  Same behavior ("wealthy yet still chasing money"), 6 DIFFERENT MECHANISMS:

  ① Schema not yet updated = Background-Pattern.md:
    → Grew up in scarcity → Background-Pattern [money = safety] compiled deep + high density
    → Now wealthy but Background-Pattern NOT UPDATED → cortisol baseline still high
    → = PFC knows "wealthy" but body STILL feels "lacking"
    → Pattern type: Low Depth + High Density (Background-Pattern §2.2 → INVISIBLE but PERVASIVE)

  ② Threshold adaptation = §4①:
    → $100K → adapt → $500K → adapt → $1M → treadmill
    → Hedonic treadmill (Brickman 1971)

  ③ Money = proxy for layers 2-3 = Reward-Signal-Architecture 5 Profiles + GAP SHIFT:
    → Money ≠ the goal → money = proxy for:
      Status (Profile ③ Social: serotonin ranking)
      Impact (Profile ② Coherence: "I was right, I changed the world")
      Score (Profile ④ Relief: "won the game")
    → Chasing Profiles ②③④ through MONEY PROXY, not chasing Profile ①

    GAP SHIFT — LABEL STAYS, MECHANISM CHANGES:
      Early stage: schema [money = the best] → fills REAL survival gap
      Survival filled: gap SHIFTS to coherence/status/relief
      BUT: LABEL still = "make money" (PFC hasn't updated the label)
      → Billionaire STILL "makes money" but real reward comes from:
        creativity (②), influence (③), winning deals (④), legacy (⑤)
      → They're often NOT suffering — because body IS BEING FED
        through OTHER channels, money = the scoreboard

    WHY SCHEMA [MONEY = BEST] HAS HIGH TRUST:
      → Source ④ External Injection: continuous collective validation
        ("everyone needs money" → confirmed daily)
      → Source ② Experience: lacking money → having money → problems solved
        (paying tuition, buying a home, treating illness → REAL)
      → 2 STRONG trust sources + CONTINUOUS repetition → HIGH trust
      → Schema = FUNCTIONAL (works well at survival+social layers)
      → BUT INCOMPLETE: missing layer "money = proxy, body-base = endpoint"
      → = Anchor-Schema.md: HIGH Trust ≠ HIGH Quality
        (Trust = "I believe it", Quality = "comprehensively correct")
      → Functional-incomplete schema = COMMON, not a defect
      → Only becomes a problem when gap has shifted BUT schema hasn't updated

  ④ Low satiation signal = PFC-Hardware.md receptor system:
    → "Enough, stop" signal WEAK → CANNOT BRAKE
    → Not "wanting more" → it's WEAK BRAKING MECHANISM

  ⑤ Identity lock = Meaning.md §3.3 IDENTITY type anchor:
    → "I = the person who makes money" = IDENTITY anchor compiled rigid
    → Stop making money = identity crash = Meaning crisis
    → "Retired and became depressed" = anchor collapse

  ⑥ Cortisol treadmill = Cortisol-Baseline.md §7.7 Role ④ Inertia:
    → Moderate cortisol continuously → dopamine rises → "productive"
    → Stop = cortisol DROPS → body feels uncomfortable
    → Chasing the CORTISOL STATE, not chasing money

  RECOGNITION (important because intervention DIFFERS):
    ① Schema not updated    → anxious despite wealth, hoarding, defensive
    ② Threshold adapt       → "bored" if not increasing, peer comparison
    ③ Proxy for layers 2-3  → talks about impact/vision, money is a tool
    ④ Low satiation signal  → cannot stop ANYTHING, not just money
    ⑤ Identity lock         → fears retirement, "don't know who I am if I stop working"
    ⑥ Cortisol treadmill    → "rest = restless", needs to be busy to feel calm

  → Same behavior, 6 DIFFERENT interventions.
  → Wrong path → intervention = INEFFECTIVE.
  → = Observation more important than prescription.

  🟢 Brickman 1978 (lottery), Kahneman & Deaton 2010 (income + well-being)
  🟡 6-path mapping to v7.8 = framework synthesis
```

### §8.2 — Money = shared chunk prediction token

```
🟡 WHAT MONEY IS THROUGH V7.8 LENS:

  Money = PROXY TOKEN for prediction:
    → "100 dollars" = a shared chunk that society has compiled: "exchanges for X"
    → Money itself has NO body-base value (paper, numbers)
    → Value lies in prediction: "having money → body-base GETS FED"

  = Shared Chunk Prediction:
    → Everyone compiles SAME chunk: "$100 ≈ X food ≈ Y services"
    → This chunk = shared across society → TRUSTWORTHY
    → Inflation = chunk prediction invalidated → SNC → anger

  Money ≈ Status.md Resource Access Map extension:
    → Having money = resource access MAP EXPANDS
    → More money = more schemas "accessible"
    → Losing money = schemas "blocked" → status DROPS → cortisol

  🟡 Money = proxy token = Reward-Economics.md insight + v7.8 chunk reframe
```

### §8.3 — Habituation Blindness × Economics

```
🟡 PREDICTION-DELTA = 0 ≠ VALUE = 0:

  Oxygen: prediction-delta = 0 (completely habituated), VALUE = life/death
  Daily meals: prediction-delta = 0 (baseline), VALUE = essential nutrition
  Monthly salary: prediction-delta = 0 (compiled baseline), VALUE = survival

  COMMON CONFUSION:
    → prediction-delta = 0 → "no value" → ignored → lost → SNC → "turns out it was crucial"
    → = Habituation Blindness: body RECEIVES but DOESN'T REWARD → PFC thinks "not needed"
    → Gratitude.md §3: 3 anti-habituation mechanisms = FIGHTING habituation blindness

  ECONOMICS IMPLICATION:
    → Most important things = things with prediction-delta ≈ 0 (habituated = invisible)
    → Things generating strong positive prediction-delta = often new/rare but may NOT be important
    → = Novelty bias: brain tracks novelty > tracks importance
    → = Why salary reduction "hurts" more than salary increase "pleases" (loss aversion)
    → Protect.md: loss aversion = f(replaceability × attachment)

  🟢 Loss aversion: Kahneman & Tversky 1979 (prospect theory)
  🟢 Endowment effect: Thaler 1980
  🟡 prediction-delta = 0 ≠ Value = 0 = Gratitude.md + Reward-Economics insight
```

---

## §9 — HONEST ASSESSMENT

### §9.1 — Confidence per section

```
  ┌──────────────────────────────┬──────────┬──────────────────────────┐
  │ Section                      │ Level    │ Notes                    │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §1 Goldilocks per-gap       │ 🟢       │ Well-documented:         │
  │                              │          │ Yerkes-Dodson, Brickman, │
  │                              │          │ Schultz                  │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §2 Gap types × reward match │ 🟡       │ Body-Feedback-Mechanism  │
  │                              │          │ 3 dynamics = 🟢          │
  │                              │          │ Mapping to reward type   │
  │                              │          │ = framework synthesis    │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §3 Goldilocks zones         │ 🟡       │ Under/over = well-known  │
  │                              │          │ Match description =      │
  │                              │          │ framework synthesis      │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §4 6 over-reward mechanisms │ 🟢→🟡   │ ①②④: strong research.   │
  │                              │          │ ③⑤⑥: framework synth    │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §5 Dynamic equilibrium      │ 🟡       │ Parallel Logic-Feeling-  │
  │                              │          │ Balance = framework meta │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §6 Observable indicators    │ 🟡       │ Probabilistic, not       │
  │                              │          │ diagnostic. Per-case     │
  │                              │          │ verification needed      │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §7 Evaluative/Direct-State  │ 🟡       │ Reward-Signal-Archit.    │
  │ calibration                  │          │ synthesis applied to     │
  │                              │          │ calibration context      │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §8 RE insights              │ 🟡       │ v5.5 insights remapped   │
  │                              │          │ to v7.8 mechanisms       │
  └──────────────────────────────┴──────────┴──────────────────────────┘
```

### §9.2 — Value + Limitations

```
  VALUE OF THIS FILE:
    → Synthesizes insights from ~15 files into 1 CALIBRATION lens
    → 6 over-reward mechanisms = organized for the first time (scattered before)
    → Dynamic equilibrium thesis = made explicit (previously implicit)
    → Observable indicators = practical guide
    → Gap type × reward match = new mapping

  LIMITATIONS:
    → This file = OBSERVATION SYNTHESIS, does not create new mechanisms
    → Reality = continuous, high-dimensional → file simplifies
    → Observable indicators = probabilistic, REQUIRE case-by-case verification
    → 6 mechanisms can overlap in practice (not always separable)
    → Dynamic equilibrium = principled position but untestable in absolute terms
```

### §9.3 — Predictions (testable)

```
  P1: Over-reward group (high external reward, minimal gap) will show
      threshold adaptation faster than match group
      → Measure: hedonic adaptation speed via longitudinal survey

  P2: Direct-State reward when Evaluative is exhausted will restore partial function
      → Measure: body-oriented intervention for burnout patients

  P3: Wrong gap type × reward match will produce LOWER satisfaction
      than under-reward with CORRECT match
      → Measure: employee satisfaction per reward-fit survey

  P4: Variation (Gratitude §3.2) injection will slow threshold adaptation
      → Measure: intermittent vs continuous reward schedule outcomes

  🟡 Predictions testable but not yet tested in this specific framework
```

---

## §10 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ 03-Reward.md                     │ Body-Feedback-Preconditions, 7-step  │
  │                                  │ VTA, 7 cases — §0 file position      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Reward-Signal-Architecture.md    │ Evaluative/Direct-State, E₀→E₃,     │
  │ v1.0                             │ 5 Profiles, Evaluative Gates —       │
  │                                  │ §7 calibration                       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Mechanism.md v1.2  │ 3 dynamics (Shift/Miss/Gap),        │
  │                                  │ compound — §2 gap types              │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gap-Direction.md v1.0            │ Gap has direction,                   │
  │                                  │ "unknown = no gap" — §1.3 foundation │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gratitude.md v1.1                │ §3 anti-habituation, §4 baseline     │
  │                                  │ shift — §4①④ mechanisms              │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Education-Mechanism.md v1.0      │ §3 bridge, source ④, overjust —     │
  │                                  │ §4②③ mechanisms                      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.0        │ §7.7 5 Roles (② Holding,            │
  │                                  │ ④ Inertia) — §3.1 under-reward      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Status.md v2.0                   │ §1 Resource Access Map — §4⑤        │
  │                                  │ competence-reward mismatch           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Logic-Feeling-Balance.md v1.0    │ §6-§7 infinite regress — §5         │
  │                                  │ dynamic equilibrium parallel         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Hardware.md v1.1             │ §3.4 COMT × Reward, §3.5            │
  │                                  │ Childhood — §1.2 per-person          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Background-Pattern.md v1.0       │ Invisible bias on gap landscape      │
  │                                  │ — §1.2 per-context                   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Connection.md v3.1               │ §9 calibration between 2 bodies —   │
  │                                  │ §5.2 perception-action cycle         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Meaning.md v2.0                  │ IDENTITY anchor, life-level —        │
  │                                  │ §4⑥ Evaluative/Direct-State         │
  │                                  │ imbalance, §8.1⑤ identity lock       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Obligation.md v1.0               │ Cortisol holding (Role ②),          │
  │                                  │ 5-factor — §5.2 equilibrium          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ AI-Schema-Detection.md v2.0      │ 3-layer model — §6.1 observe        │
  │                                  │ ≠ diagnose                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Reward-Economics.md v5.5         │ 6 paths, money = proxy — §8         │
  │ (Applications/)                  │ insights remapped to v7.8            │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

> *Reward Calibration v1.1 — Observation File.*
> *Reward has a Goldilocks per-gap: cannot prescribe, can only observe + adjust.*
> *Dynamic equilibrium, not a fixed formula.*
> *Domain feedback = the only arbiter.*
