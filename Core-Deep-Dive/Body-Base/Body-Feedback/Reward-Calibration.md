---
title: Reward Calibration — Observation File for Reward Amount × Gap Match
version: 1.1
created: 2026-05-10
refined: 2026-05-10 (v1.1 — §3.4 Premature Compilation, §5.4 Collective Calibration, §8.1③ Gap Shift + Schema Trust)
status: OBSERVATION FILE v1.1
scope: |
  OBSERVATION FILE: HOW MUCH reward is ENOUGH for THIS gap,
  THIS person, THIS context? And what happens when too little / too much?
  Core thesis: Reward has a Goldilocks zone per-gap, per-person, per-context.
  CANNOT be prescribed — can only OBSERVE + ADJUST (dynamic equilibrium).
  3 Gap Types × Reward Match. Goldilocks Zone (Under/Match/Over).
  6 Over-Reward Mechanisms (threshold adaptation, overjustification, bridge dependency,
  baseline shift, competence-reward mismatch, Evaluative/Direct-State imbalance).
  Dynamic equilibrium parallel to Logic-Feeling-Balance.md.
  Observable indicators through communication + behavior (probabilistic, not diagnostic).
  Evaluative/Direct-State × Calibration. Reward-Economics insights through the framework lens.
purpose: |
  03-Reward.md answers: WHEN reward fires (5 Body-Feedback-Preconditions, 7-step VTA)
  Reward-Signal-Architecture answers: WHAT QUALITY of reward fires (Evaluative/Direct-State, 5 Profiles, Evaluative Gates Direct-State)
  Gap-Direction.md answers: WHY reward is personal (gap has direction)
  Gratitude.md §3–4: Anti-habituation + baseline shift
  Education-Mechanism.md §3: Bridge (external reward) in education
  This file answers: HOW MUCH reward is ENOUGH? And what goes wrong when the amount is off?
  = CALIBRATION question — parallel to Cortisol-Baseline.md
  (cortisol = amplifier with Goldilocks; reward = signal with Goldilocks)
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — parallel to Reward-Signal-Architecture,
  Gap-Direction, Body-Feedback-Mechanism.
  MECHANISM observation file. Calibration is a property OF the Evaluative reward system,
  not an external application.
dependencies:
  - 03-Reward.md — 5 Body-Feedback-Preconditions, 7-step VTA, opioid vs dopamine, 7 cases
  - Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles, Evaluative Gates Direct-State
  - Body-Feedback-Mechanism.md v1.2 — 2 sources, 3 dynamics (Shift/Miss/Gap), compound
  - Gap-Direction.md v1.0 — gap has direction, "unknown = no gap," 2-layer
  - Gratitude.md v1.1 — §3 anti-habituation 3 mechanisms, §4 baseline shift
  - Education-Mechanism.md v1.0 — §3 bridge, 4 fill sources, overjustification
  - Cortisol-Baseline.md v2.0 — §7.7 5 Roles (② Holding, ④ Inertia relevant)
  - Status.md v2.0 — §1 Resource Access Map, competence-reward mismatch
  - Logic-Feeling-Balance.md v1.0 — §6–§7 infinite regress, cannot prescribe
  - PFC-Hardware.md v1.1 — §3.4 COMT × Reward Pattern, §3.5 Childhood trajectories
  - Background-Pattern.md v1.0 — invisible bias on gap direction landscape
  - Connection.md v3.1 — §9 calibration between 2 bodies, dynamic equilibrium
  - Reward-Economics.md v5.5 — 6 paths, money = proxy, habituation blindness (insights)
  - Meaning.md v2.0 — IDENTITY anchor, life-level Anchor-Schema
  - Obligation.md v1.0 — cortisol holding (Role ②), 5-factor formula
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Reward Calibration — Observation File for Reward Amount × Gap Match

> **Salary of $50K. Pleasant.**
> **Raised to $75K. More pleasant.**
> **Raised to $100K. Still pleasant, but less so than last time.**
> **Raised to $250K. Pleasant... then you get used to it.**
> **Raised to $500K. "How much does my colleague make?"**
>
> Same person. Same reward mechanism (Body-Feedback-Precondition, 03-Reward.md).
> But the AMOUNT of reward needed to create satisfaction = KEEPS CHANGING.
>
> Sugar in food: too little = bland, just right = delicious, too much = sickening.
> Salary: too low = painful, just right = fine, too high = different problems.
> Praise: not enough = wilting, just right = good, too much = "what's the praise for?"
>
> EVERY type of reward has a GOLDILOCKS zone — a sweet spot.
> AND the sweet spot is NOT FIXED: it varies per-person, per-gap, per-context, per-time.
>
> This file does NOT say "how much reward to give."
> This file helps you SEE: which zone the reward is in (under / match / over),
> WHAT happens in each zone,
> AND why it's IMPOSSIBLE to prescribe "how much reward."

---

## Table of Contents

- §0 — POSITION IN THE FRAMEWORK
- §1 — CORE: REWARD HAS A GOLDILOCKS ZONE PER-GAP
- §2 — 3 GAP TYPES × REWARD MATCH
- §3 — GOLDILOCKS ZONE: 3 STATES
- §4 — OVER-REWARD: 6 HARMFUL MECHANISMS
- §5 — DYNAMIC EQUILIBRIUM: WHY YOU CANNOT PRESCRIBE
- §6 — OBSERVABLE INDICATORS
- §7 — EVALUATIVE/DIRECT-STATE × CALIBRATION
- §8 — REWARD-ECONOMICS INSIGHTS THROUGH THE FRAMEWORK LENS
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES

---

## §0 — POSITION IN THE FRAMEWORK

### §0.1 — This file vs 5 related files

```
⭐ THIS FILE ANSWERS A NEW QUESTION:

  ┌───────────────────────────┬─────────────────────────────────────────┐
  │ File                      │ Question                                │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ 03-Reward.md              │ WHEN does reward fire?                  │
  │                           │ (5 Body-Feedback-Preconditions, 7-step  │
  │                           │  VTA)                                   │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Reward-Signal-            │ WHAT QUALITY of reward fires?           │
  │ Architecture.md           │ (Evaluative/Direct-State, 5 Profiles,   │
  │                           │  Evaluative Gates Direct-State)         │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Gap-Direction.md          │ WHY is reward personal?                 │
  │                           │ (gap has direction, f(surrounding       │
  │                           │  chunks))                               │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Gratitude.md §3–4         │ WHY does a gift habituate?              │
  │                           │ (anti-habituation, baseline shift)      │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Education-Mechanism.md §3 │ Bridge reward in education?             │
  │                           │ (Source ④, overjustification)          │
  ├───────────────────────────┼─────────────────────────────────────────┤
  │ Reward-Calibration.md     │ HOW MUCH reward is ENOUGH?              │
  │ (THIS FILE)               │ What goes wrong when the amount is off? │
  │                           │ Why can't we prescribe?                 │
  └───────────────────────────┴─────────────────────────────────────────┘

  This file = OBSERVATION SYNTHESIS:
  → Synthesizes insights from ~15 files into 1 CALIBRATION lens
  → Does NOT create new mechanisms — reorganizes through
    the "enough for this gap" lens
  → Reader flow: read AFTER 03-Reward + Reward-Signal-Architecture +
    Body-Feedback-Mechanism + Gap-Direction
```

### §0.2 — What this file IS

```
  ✓ Observation file — helps you SEE reward state
  ✓ Helps identify: under / match / over
  ✓ Explains 6 over-reward mechanisms (synthesized + NEW)
  ✓ Parallel to Cortisol-Baseline.md:
    cortisol has Goldilocks ↔ reward has Goldilocks
```

### §0.3 — What this file IS NOT

```
  ✗ NOT "how to design reward systems" (prescriptive)
  ✗ NOT an economics file (Reward-Economics.md = Applications layer)
  ✗ Does NOT repeat Body-Feedback-Precondition or
    Reward-Signal-Architecture (reference only)
  ✗ NOT an education file (Education-Mechanism.md §3 covers bridge)
  ✗ NOT an HR file
  ✗ Does NOT say "what to do" — only "where things stand" and "why it's hard"
```

---

## §1 — CORE: REWARD HAS A GOLDILOCKS ZONE PER-GAP

### §1.1 — Thesis

```
⭐ REWARD AMOUNT HAS A SWEET SPOT PER-GAP:

  Gap (Body-Feedback-Mechanism §3: Chunk-Shift / Chunk-Miss / Chunk-Gap)
  = hole in the chunk network that needs filling.

  Too little reward for the gap → gap unfilled → dissonance PERSISTS
  Just enough reward for the gap → gap fills + approach tag + chunk compiles
  Too much reward for the gap → SURPLUS → multiple harmful mechanisms (§4)

  = Like sugar in food:
    Too little sugar → bland → body "insufficient caloric signal"
    Just right sugar → delicious → E₀ hardware opioid confirm
      (Reward-Signal-Architecture §2.1)
    Too much sugar → sickening → body REJECTS (saturation threshold)
    = E₀ = simplest hardware Goldilocks
    = SAME PATTERN across ALL types of reward, just more COMPLEX

  🟢 Hedonic adaptation: Brickman & Campbell 1971
  🟢 Inverted-U: Yerkes-Dodson 1908 (performance ↔ arousal)
  🟡 Reward Goldilocks per-gap = framework synthesis
```

### §1.2 — Goldilocks is NOT FIXED

```
⭐ SWEET SPOT KEEPS CHANGING:

  → Varies PER-PERSON (hardware):
    COMT Val/Val: many shallow rewards = MATCH for this hardware
    COMT Met/Met: fewer deeper rewards = MATCH for this hardware
    (PFC-Hardware.md §3.4)
    DRD4 variant: different chunk threshold → different Goldilocks
    (PFC-Hardware.md §4.3)

  → Varies PER-GAP-TYPE:
    Chunk-Shift: needs re-anchoring → different reward (§2)
    Chunk-Miss: needs compensating OR adjusting → different reward (§2)
    Chunk-Gap: needs exploration → different reward (§2)

  → Varies PER-CONTEXT:
    Cortisol state: Role ② Holding → different reward needed
      (Cortisol §7.7)
    Existing chunks: expert vs novice → same input, different reward
    Relationship: close friend giving vs stranger giving → different valence
    Background-Pattern: invisible bias → gap landscape skewed
      (Background-Pattern.md §6)

  → Varies PER-TIME:
    Baseline shift: continuous reward → baseline RISES → MORE is needed
      (Gratitude.md §4)
    Development stage: child vs adult → different thresholds
    Habituation: first vs hundredth time → completely different prediction-delta

  → NO formula "give X reward for gap Y"
  → Only OBSERVE + ADJUST continuously (§5)

  🟡 Per-person × per-gap × per-context × per-time = framework synthesis
```

### §1.3 — "Unknown = no gap" → Reward for something with no gap = WASTED

```
⭐ FOUNDATIONAL PRINCIPLE (Gap-Direction.md §3):

  Gap = hole in the chunk network = MUST have surrounding chunks to form its edges.
  No surrounding chunks = no edges = NO HOLE.

  "Unknown = no gap":
    → You don't know chess → no gap about chess
    → Chess-related reward = DOESN'T MATCH any gap → WASTED
    → Body receives stimulus → VTA checks → NO matching gap → no opioid confirm
    → = Reward "falling into empty space"

  EXAMPLES:
    A 5-year-old receiving a supercar (no gap about cars yet)
      → Body: "big thing" → no gap match → no reward
      → Parents: "why isn't the child thrilled?" → because the child HAS NO GAP yet

    Giving E=mc² to a third-grader
      → No physics chunks → no gap → no reward
      → Giving it to Einstein → EXTREMELY DEEP gap → EXTREMELY STRONG reward

  IMPLICATION FOR CALIBRATION:
    Step 0 BEFORE calibrating reward: confirm the RECIPIENT HAS A GAP.
    No gap → all reward = wasted or harmful (§4⑤ mismatch).

  🟡 "Reward for no-gap = wasted" = Gap-Direction.md core principle applied
```

---

## §2 — 3 GAP TYPES × REWARD MATCH

```
⭐ 3 CHUNK DYNAMICS (Body-Feedback-Mechanism.md §3) × APPROPRIATE REWARD:

  Each gap type has a DIFFERENT nature → DIFFERENT reward match:

  ┌──────────────┬──────────────────────────────┬────────────────────────────────┐
  │ Gap Type     │ Nature                       │ Reward Match                   │
  ├──────────────┼──────────────────────────────┼────────────────────────────────┤
  │ CHUNK-SHIFT  │ Context changed →            │ RE-ANCHOR reward:              │
  │              │ old baseline no longer fits. │ help build a NEW baseline      │
  │              │ "Moving cities, changing     │ in the NEW context.            │
  │              │ jobs, losing someone."       │                                │
  │              │                              │ = Direct-State Reward          │
  │              │ Body is RE-CALIBRATING       │ effective (body-state: touch,  │
  │              │ the entire baseline →        │ exercise, warmth, grounding,   │
  │              │ unstable                     │ sleep, routine)                │
  │              │                              │                                │
  │              │                              │ ⚠️ Evaluative Reward           │
  │              │                              │ MAY NOT WORK YET:              │
  │              │                              │ old chunks invalidating →      │
  │              │                              │ evaluation misfires            │
  ├──────────────┼──────────────────────────────┼────────────────────────────────┤
  │ CHUNK-MISS   │ Expected X, got <X.          │ COMPENSATE reward:             │
  │              │ "Expected a higher salary,   │ fill the delta OR adjust       │
  │              │ got less." "Expected praise, │ the expectation.               │
  │              │ got criticism."              │                                │
  │              │                              │ = Evaluative Reward:           │
  │              │ Body detects: actual <       │ PFC compares + evaluates →     │
  │              │ compiled expectation         │ opioid when delta is filled    │
  │              │ → SNC (Crespi 1942)          │                                │
  │              │                              │ ⚠️ 2 PATHS (important):       │
  │              │                              │ Path A: fill the delta         │
  │              │                              │   (raise actual → match        │
  │              │                              │   expectation)                 │
  │              │                              │ Path B: adjust expectation     │
  │              │                              │   (lower compiled →            │
  │              │                              │   match actual)                │
  │              │                              │ Both paths can be healthy      │
  ├──────────────┼──────────────────────────────┼────────────────────────────────┤
  │ CHUNK-GAP    │ Structure predicts C         │ EXPLORATION reward:            │
  │              │ should exist → C not yet     │ bridge through exploration     │
  │              │ compiled → HOLE.             │ → chunk fills → opioid.        │
  │              │ "Don't know yet, want to     │                                │
  │              │ know." "Problem unsolved."   │ = prediction-delta (novelty)   │
  │              │                              │ when new chunk matches gap     │
  │              │ Body detects: surrounding    │ + opioid when filled           │
  │              │ chunks predict C but C       │ = Profile ② Coherence          │
  │              │ is missing                   │ (Reward-Signal-Architecture §4)│
  └──────────────┴──────────────────────────────┴────────────────────────────────┘

  🟢 SNC (Successive Negative Contrast): Crespi 1942, Flaherty 1996
  🟢 Dopamine prediction-delta: Schultz 1997
  🟡 Gap type × Reward match mapping = framework synthesis
```

### §2.1 — Wrong reward type for wrong gap = WASTED or HARMFUL

```
⭐ REWARD CALIBRATION IS NOT JUST ABOUT AMOUNT — IT'S ALSO ABOUT TYPE:

  Example 1: Chunk-Miss (salary expectation gap) but given Direct-State Reward
             (massage, spa)
    → Body is "expected X, got <X" → needs evaluative resolution
    → Massage = body-state improvement → correct Direct-State, BUT:
    → The ROOT gap (salary < expectation) REMAINS → dissonance REMAINS
    → = Correct type but WRONG gap → only temporary

  Example 2: Chunk-Gap (wanting to understand a problem) but given money
    → Body is "C should exist but missing" → needs exploration fill
    → Money = proxy token → DOESN'T MATCH the coherence gap
    → Gap (not understanding the problem) REMAINS → reward = empty
    → ⚠️ CAN BE HARMFUL: if money is STRONGER than the exploration drive
      → overjustification (§4②): now only solves problems for money →
        no money → stops

  Example 3: Chunk-Shift (losing someone dear) but given logical advice
    → Body is RE-CALIBRATING its entire baseline → unstable
    → Logic = Evaluative Reward → old chunks invalidating → evaluation misfires
    → Body NEEDS: Direct-State grounding (being held, presence, routine)
    → Advice = correct type but WRONG timing
    → = "Someone is drowning and you're lecturing them"

  PRINCIPLE:
    → Match gap TYPE first, then calibrate AMOUNT
    → Wrong type → no amount is enough → always wasted
    → Equivalent to Gap-Direction.md: reward must match the SPECIFIC DIRECTION

  🟡 "Wrong type = wasted" = logical consequence of Gap-Direction principle
```

---

## §3 — GOLDILOCKS ZONE: 3 STATES

### §3.1 — Under-reward (too little for the gap)

```
⭐ UNDER-REWARD = GAP UNFILLED → DISSONANCE PERSISTS:

  MECHANISM:
    Gap exists → body detects → cortisol fires (amplifier)
    Reward arrives but INSUFFICIENT to fill gap → gap REMAINS
    → Cortisol Role ② Holding: "not done yet" → PFC tracking pending
      (Cortisol-Baseline.md §7.7)
    → Extended duration → CAN shift to Role ③ Threat-sustained
      (if gap is survival- or socially-relevant)

  DIRECTION SHIFT:
    Prolonged under-reward → approach tag CAN flip to avoidance:
    → "I try → insufficient reward → try more → still insufficient"
    → Chunk compiles with avoidance tag:
      "this domain = effort > reward"
    → = Learned helplessness pattern
      (Cortisol-Baseline.md §7.7 Role ① Compile Direction)

  EXAMPLES:
    Salary far below competence level:
      → Gap: competence >> reward → continuous Chunk-Miss
      → Sustained cortisol → leave or burnout
      → Status.md §1: Resource Access Map skewed →
        "I am ACCESS-ing less than I deserve"

    Child not acknowledged despite effort:
      → Gap: effort → no recognition → Chunk-Miss
      → Extended → avoidance compiles: "trying is pointless"
      → = Foundation for Background-Pattern.md [effort → not enough]

    Relationship lacking connection:
      → Gap: ❶ hardware social drive fires → insufficient response
      → Connection.md §9: one-way calibration → dissonance
      → Body feels "lonely" even with people nearby

  🟢 Learned helplessness: Seligman 1967
  🟢 Cortisol sustained: McEwen 1998 (allostatic load)
  🟡 Under-reward → direction shift = framework synthesis
```

### §3.2 — Match (just right for the gap)

```
⭐ MATCH = SWEET SPOT → SUSTAINABLE:

  MECHANISM:
    Reward matches gap → prediction-delta → body-base reward → gap fills
    → Chunk compiles with approach tag
    → Body state: brief positive → resets → ready for next gap
    → = Healthy perception-action cycle

  IDENTIFYING FEATURES:
    → Drive SELF-SUSTAINING: no constant external push needed
    → Approach tags accumulating: "this domain = effort → reward"
    → Cortisol healthy: spike → resolve → return to baseline
    → Baseline STABLE (not shifting up too quickly)

  BUT — MATCH IS NOT FIXED:
    → Today's match CAN become tomorrow's under-reward
      (baseline shift: Gratitude.md §4 — reward habituates)
    → Match for this person ≠ match for another person
      (hardware: PFC-Hardware.md §3.4 — COMT × Reward Pattern)
    → Match in this context ≠ match in another context
      (cortisol state, relationship, Background-Pattern)

  EXAMPLES:
    Salary matching competence + timely recognition:
      → Chunk-Miss minimized → drive stable
      → Approach tags accumulate → loyalty emerges
      → = "Not wealthy but happy to go to work"

    Child learning piano: chunks compile → opioid → "beautiful!":
      → Gap fills → exploration continues → curiosity emerges
      → Bridge (Source ④) gradually withdrawn → Sources ①②③ take over
        (Education-Mechanism.md §3.4)

  🟡 Match = sustainable = framework synthesis
```

### §3.3 — Over-reward (too much for the gap → §4)

```
⭐ OVER-REWARD = SURPLUS REWARD WITH NO MATCHING GAP:

  MECHANISM:
    Gap fills → reward KEEPS ARRIVING → surplus
    Surplus reward = NO matching gap → where does it go?

    3 DIRECTIONS SURPLUS REWARD FLOWS:
    ① Threshold adaptation → needs MORE next time (§4①)
    ② Creates dependency → losing the reward becomes painful
      even though it was previously a bonus (§4③④)
    ③ Imbalance → system tilts → problems emerge elsewhere (§4⑤⑥)

  WHY OVER-REWARD IS MORE DANGEROUS THAN UNDER-REWARD:
    → Under-reward: body KNOWS "insufficient" → clear signal →
      CAN adjust
    → Over-reward: body feels "pleasant" → NO signal of "too much" → blind
    → = Over-reward is invisible → hard to detect → hard to fix
    → Like Cortisol-Baseline.md Role ⑤ Silent:
      cortisol HIGH but NOT PERCEIVED → damage accumulates
    → Over-reward = "silent surplus" → damage accumulates

  → Details of 6 mechanisms: §4

  🟡 Over-reward harder to detect = framework inference
```

### §3.4 — Over-reward at CHUNK LEVEL: premature compilation

```
⭐ META-PRINCIPLE: OVER-REWARD FORCES CHUNK COMPILATION BEFORE THE
  FOUNDATION IS READY:

  Body-base is on the ACTION side — collecting information + interacting
  with real domains. Body-base accumulates chunks → chunk-gap forms →
  drive to fill the gap = NATURAL PROCESS.

  Over-reward = reward EXCEEDS CURRENT chunk-gap:
    → Body receives surplus → INSUFFICIENT foundation chunks to evaluate/use
      the reward properly
    → But body IS FORCED to compile new chunks to PROCESS the surplus
    → Compiling IN CONTEXT of insufficient foundation → chunks SKEWED
      from the start
    → Skewed chunks → BECOME FOUNDATION for subsequent chunks → cascade
    → = Background-Pattern.md: skewed patterns accumulate → pervasive bias

  3 CASES — NOT ALL OVER-REWARD IS HARMFUL:

  CASE 1 — E₀ HARDWARE REJECT (HARMLESS):
    Too much sugar → sickening → body rejects IMMEDIATELY →
      DOESN'T compile wrong chunks
    → E₀ = hardware Goldilocks (Reward-Signal-Architecture §2.1) →
      IMMEDIATE feedback
    → Body knows "too much" at the hardware level → stops → harmless

  CASE 2 — NO GAP (HARMLESS):
    Third-grader receiving a car → no gap about cars → no gap match
    → Body: "big thing" → doesn't compile anything deep → harmless
    → = Gap-Direction.md §3: "unknown = no gap"
    → Reward falls into empty space → creates no damage

  CASE 3 — GAP EXISTS BUT DEPTH INSUFFICIENT (DANGEROUS ⚠️):
    Schema drive EXISTS (money = proxy, infinite gap) + gap EXISTS
    (wants more) BUT foundation chunks INSUFFICIENT to properly
    evaluate + use the reward.

    Lottery winner:
      → Gap [needs money] EXISTS → reward matches gap type
      → BUT: chunks for "managing large wealth" NOT YET PRESENT
      → Body FORCED to compile "wealth management" chunks from scratch
      → Compiling IN CONTEXT of insufficient foundation → chunks often WRONG:
        [money is easy to get] [can buy anything] [no need for caution]
      → Wrong chunks → wrong decisions → lose money →
        Successive Negative Contrast (SNC) extreme
      → 🟢 ~70% of lottery winners are worse off within years

    Salary exceeding competence (§4⑤ detail):
      → Gap [needs money] EXISTS → reward matches gap type
      → BUT: chunks for "competence at this level" INSUFFICIENT
      → Body compiles: [high access] but MISSING [I deserve this access]
      → = Imposter syndrome + peers recalibrate → double pressure
      → Chunks compile IN DISSONANCE → approach/avoidance MIXED

    Large inheritance:
      → Transfer WITHOUT effort → "wealth" chunks compile WITHOUT
        accompanying effort chunks
      → = "Wealthy but don't know why"
      → Background-Pattern forms: [money = free]
      → Biases every financial decision going forward

  WHY CASE 3 IS MORE DANGEROUS THAN CASES 1+2:
    → Case 1: hardware feedback IMMEDIATE → stops → no wrong compilation
    → Case 2: no gap → nothing to compile → no damage
    → Case 3: gap EXISTS + drive EXISTS + foundation INSUFFICIENT →
      FORCED to compile
      → Compilation happens WHETHER OR NOT ready
      → Skewed chunks → BECOME FOUNDATION → cascade
      → = "A double-edged sword" — reward CAN GENUINELY IMPROVE body-base
        (actually wealthier), but SIMULTANEOUSLY creates skewed chunks

  🟢 Lottery winner outcomes: Brickman 1978, Hankins et al. 2011
  🟡 Premature compilation under over-reward = framework synthesis
  🟡 3-case distinction = framework analysis
```

---

## §4 — OVER-REWARD: 6 HARMFUL MECHANISMS

```
⭐ 6 MECHANISMS — each is a DIFFERENT route through which surplus reward causes harm:

  Not all 6 mechanisms occur simultaneously.
  Nor is there only 1 mechanism per case.
  = Combination varies by case, by person, by context.
```

### §4.1 — ① THRESHOLD ADAPTATION (hedonic treadmill)

```
⭐ CONTINUOUS REWARD → BASELINE RISES → SAME REWARD = PREDICTION-DELTA DECREASES:

  MECHANISM (Gratitude.md §3.1 + §4):
    Gift the first time → VTA fires delta → opioid → reward → "pleasant"
    Gift times 2–10 → VTA gradually habituates → reward DECREASES
    Gift times 50–100+ → VTA fully habituated → gift = INVISIBLE
    → Needs NEWER, BIGGER reward to create a positive prediction-delta
    → = Hedonic treadmill: running constantly, position NEVER ADVANCES

  EXAMPLES:
    Salary: $100K → adapt → $1M → adapt → $10M → "still not enough"
    Sugar: just sweet → adapt → needs SWEETER → adapt → needs EVEN SWEETER
    Praise: "great" → adapt → "excellent" → adapt → "genius" → adapt
    → Each level becomes "the new normal"

  WHY YOU'RE "COMFORTABLE" YET STILL "LACKING":
    → Body is GENUINELY lacking — because the baseline HAS SHIFTED
    → Not "greed" — it's the BIOLOGICAL threshold that recalibrated upward
    → Staying at the current level → actual < shifted baseline →
      prediction-delta negative → "lacking"
    → = Not greed, but threshold adaptation

  🟢 Hedonic treadmill: Brickman & Campbell 1971, Frederick & Loewenstein 1999
  🟢 VTA habituation: Schultz 1997 (predicted reward → no dopamine signal)
  🟢 Hedonic adaptation: Brickman 1978 (lottery winners return to baseline)
```

### §4.2 — ② OVERJUSTIFICATION (external kills internal)

```
⭐ EXTERNAL REWARD STRONGER THAN INTERNAL PREDICTION-DELTA → BRAIN TRACKS ONLY EXTERNAL:

  MECHANISM (Education-Mechanism.md §3.1):
    Before: behavior has intrinsic prediction-delta (internal drive) →
      DOES IT BECAUSE THEY ENJOY IT
    Add STRONG external reward → brain switches to tracking EXTERNAL
      (external > internal → VTA tracks the STRONGER source)
    Remove external → prediction-delta = 0 (internal was suppressed) →
      BEHAVIOR STOPS

  EXAMPLES:
    Pay to draw → draws for money → no money → stops drawing
      (even though they used to draw because they LIKED it)

    Give candy to study → studies for candy → no candy → stops studying
      (even though they were CURIOUS to know)

    Bonus for creativity → creates for bonus → cut bonus → creativity gone
      (even though there was an internal creative drive before)

  BRIDGE PARALLEL (Education-Mechanism.md §3.1):
    → Bridge = external injection (Source ④) that KEEPS students engaged
    → Correct bridge = smallest possible → wait for Sources ①②③ to emerge
      → phase out
    → Bridge TOO STRONG = overjustification → Source ④ dominates →
      ①②③ suppressed
    → = "Medicine overdosed → poisoning"
      (Education-Mechanism.md §3.1)

  🟢 Overjustification effect: Deci 1971, Lepper et al. 1973
  🟢 Self-Determination Theory: Deci & Ryan 1985, 2000
```

### §4.3 — ③ BRIDGE DEPENDENCY (withdraw the bridge = anchor crash)

```
⭐ SOURCE ④ DOMINATES TOO LONG → SOURCES ①②③ NEVER EMERGE:

  MECHANISM (Education-Mechanism.md §3.4):
    4 fill sources for anchor: ① PFC Imagine-Final, ② Hippocampus experience,
    ③ Compiled schemas, ④ External injection (bridges).
    Correct bridge: ④ holds → ①②③ grow → ④ withdraws gradually →
      HEALTHY transition
    Bridge dependency: ④ dominates 100% → ①②③ NEVER DEVELOP
    → Remove ④ = anchor crash (Anchor-Schema.md: sync point lost)
    → "No one tells me what to do → I don't know what I want"

  DIFFERS FROM OVERJUSTIFICATION:
    ② Overjustification: external KILLS internal that already existed
    ③ Bridge dependency: external PREVENTS internal from FORMING
    → ② = destroys existing. ③ = prevents emergence.
    → ③ is more serious: ② can still restore (recover the suppressed internal),
      ③ must BUILD FROM SCRATCH (internal never existed)

  EXAMPLES:
    Child who only studies with candy → no candy = no studying
    → Candy for 12 years → Source ① (knowing what they want) NEVER DEVELOPS
    → Enters adult life → "quarter-life crisis" →
      ~50–60% of motivation disappears
      (Education-Mechanism.md §3.4 → mass schooling pattern)

    Employee who only works for bonus → no bonus = no effort
    → Bonus for 10 years → internal drive NEVER FORMED for this domain
    → Cut bonus = collapse → "I only work for money"

  🟢 Extrinsic motivation crowding: Frey & Jegen 2001
  🟡 Bridge dependency vs overjustification distinction = framework synthesis
```

### §4.4 — ④ BASELINE SHIFT (gift habituates → losing it = pain)

```
⭐ CONTINUOUS GIFT → BASELINE SHIFT → SAME GIFT = prediction-delta ≈ 0:

  MECHANISM (Gratitude.md §4):
    Baseline compilation formula:
      compile_rate ≈ f(repetition × saliency × peak_valence × multi_modal ×
        contingency)
    HIGH repetition → STRONG baseline shift → gift = baseline = INVISIBLE
    Losing the gift → actual < compiled baseline → SNC → "anger"
    (even though the gift was previously a BONUS, not an entitlement)

  DIFFERS FROM THRESHOLD ADAPTATION:
    ① Threshold adaptation: needs MORE to get the SAME LEVEL of reward
    ④ Baseline shift: same reward = prediction-delta ≈ 0 (invisible),
      LOSING IT = PAIN
    → ① = reward DECREASES gradually. ④ = reward DISAPPEARS + loss = NEGATIVE.
    → ④ is more dangerous: not just "need more" but "losing it = crisis"

  EXAMPLES:
    Company car → used for 5 years → habituated → "normal"
    → Losing the car = negative prediction-delta even though the car was
      originally a bonus
    → Like SNC (Crespi 1942): downshift from high baseline → anger, not sadness

    Mother's cooking 10,000 times → habituated → invisible
    → Away from home for 5 years → VTA habituation decays →
      coming back to eat = "intensely pleasant"
    → = Variation (Gratitude.md §3.2) resets the baseline

    Social media likes continuously → baseline = "must have likes"
    → One post with no likes → SNC → "something wrong with me?"

  🟢 SNC: Crespi 1942, Flaherty 1996
  🟢 Hedonic adaptation: Brickman 1978
  🟡 Baseline shift → loss = negative = framework synthesis from Gratitude.md §4
```

### §4.5 — ⑤ COMPETENCE-REWARD MISMATCH (2 directions)

```
⭐ REWARD AND COMPETENCE MISALIGNED → DISSONANCE:

  MECHANISM:

  DIRECTION A — Reward > Competence (Imposter):
    → Receives reward HIGHER than actual competence → body detects mismatch
    → Status.md §1: Resource Access Map = accessing MORE than deserved
    → Body: "this access is not sustainable" → cortisol rises (uncertainty)
    → Those around you: detect mismatch → social recalibration
    → "If the sky won't yield to the earth, the earth must yield to the sky"
      = Collective adjustment to rebalance the access map
    → Example: promoted too quickly → imposter feeling + team friction

  DIRECTION B — Competence > Reward (Undervalued):
    → Actual competence HIGHER than reward received → continuous Chunk-Miss
    → Body: "I am GIVING more than I am RECEIVING" → resentment accumulates
    → Extended → leave or quiet quitting
    → Example: senior engineer earning a junior salary → "not deserved"

  BOTH DIRECTIONS ARE DYNAMIC:
    → Direction A: others adjust back (lower expectations, increase scrutiny)
    → Direction B: the person adjusts (find somewhere else, reduce effort)
    → = Dynamic equilibrium: both sides continuously adjust
    → Connection.md §9: calibration = 2 bodies tuning to each other

  🟡 Competence-reward mismatch = Status.md Resource Access Map × Chunk-Miss
  🟡 Dynamic equilibrium = framework synthesis
```

### §4.6 — ⑥ EVALUATIVE/DIRECT-STATE IMBALANCE (one type too dominant)

```
⭐ TOO MUCH EVALUATIVE OR TOO MUCH DIRECT-STATE → LOSS OF BALANCE:

  MECHANISM (Reward-Signal-Architecture §1–§3):

  TOO MUCH EVALUATIVE REWARD:
    → E₃ threshold HIGH (Reward-Signal-Architecture §2.1: E₀→E₃ gradient)
    → Simple pleasures INSUFFICIENT prediction-delta to clear threshold
    → Direct-State Reward STILL works (hardware) but PFC "dismisses" it
      (already calibrated to E₃)
    → = "Wealthy but unable to feel joy"
    → E₃ evaluative = complex, conditional, EASY TO habituate
    → Direct-State = hardware, simple, RELIABLE but NEGLECTED

  TOO MUCH DIRECT-STATE REWARD:
    → Body-state comfort HIGH but evaluative depth LOW
    → No chunk compilation for E₂–E₃ → no coherence reward
    → = "Fun but empty"
    → Meaning.md: no GOAL/STATE/IDENTITY anchor → no meaning

  EVALUATIVE/DIRECT-STATE RATIO NEEDS BALANCE:
    → Maximize Evaluative alone → lose Direct-State → lose safe baseline
    → Maximize Direct-State alone → lose Evaluative → lose depth + meaning
    → = Evaluative/Direct-State ratio = calibration parameter IN ITSELF

  EVALUATIVE GATES DIRECT-STATE IMPLICATION
  (Reward-Signal-Architecture §3):
    → Strong Evaluative calibration → Direct-State experience AMPLIFIED
      (E₃ anchor amplifies)
    → Weak Evaluative calibration → Direct-State "flat" (no gate to amplify
      through)
    → Over-calibrate Evaluative → BLOCKS Direct-State → "understand everything
      but can't feel it"
    → = "Expert wine taster no longer enjoys casual wine"

  🟡 Evaluative/Direct-State imbalance = Reward-Signal-Architecture
    Evaluative/Direct-State + Meaning.md synthesis
  🟡 Evaluative Gates Direct-State implication for calibration =
    framework inference
```

---

## §5 — DYNAMIC EQUILIBRIUM: WHY YOU CANNOT PRESCRIBE

### §5.1 — Parallel with Logic-Feeling-Balance.md

```
⭐ REWARD CALIBRATION = CANNOT BE PRESCRIBED — SAME REASON:

  Logic-Feeling-Balance.md §6–§7:
    → Try to create a rule → every rule has blind spots
    → Try a meta-rule → the meta-rule also has blind spots
    → = Infinite regress → NO stopping point
    → = Gödel-like incompleteness at the cognitive level

  Reward Calibration FOLLOWS THE SAME PATTERN:
    → Try to prescribe "give X reward for gap Y" → fails because:

    ① Different person → different sweet spot
       (hardware: COMT, DRD4, receptor sensitivity —
        PFC-Hardware.md §3.4)
    ② Different context → different sweet spot
       (cortisol state, relationship, Background-Pattern — all dynamic)
    ③ Different time → different sweet spot
       (baseline shift, development stage, habituation — Gratitude.md §4)
    ④ Different gap → different sweet spot
       (Shift/Miss/Gap, direction, depth — Gap-Direction.md)

    → = 4 dimensions ALL dynamic → fixed formula CANNOT cover them
    → Try meta-formula "adjust per person per context per time per gap"
    → Meta-formula = itself a fixed formula → SAME problem
    → = Infinite regress

  🟡 Reward calibration ≡ Logic-Feeling balance = framework parallel
  🟡 Infinite regress = Gödel-like incompleteness applied to reward
```

### §5.2 — Perception-action cycle: domain feedback = the only arbiter

```
⭐ REWARD CALIBRATION = PERCEPTION-ACTION CYCLE:

  Manager ↔ employee:
    → Manager gives reward → employee responds → manager observes → adjusts
    → Employee gives effort → manager responds → employee observes → adjusts
    → 2 BODIES continuously tune to each other (Connection.md §9)
    → NO fixed point — only TEMPORARY equilibrium

  Parent ↔ child:
    → Bridge (Source ④) → child responds → observe → adjust bridge
    → Child develops ①②③ → bridge gradually withdrawn → observe →
      withdraw more
    → = CONTINUOUS calibration, not "remove all bridge on day X"

  Society ↔ individual:
    → Obligation (society expects) ↔ Autonomy (individual wants)
    → 2 forces continuously adjust → equilibrium shifts with context
    → Obligation.md: 5-factor formula = observation, not prescription

  DOMAIN FEEDBACK = THE ONLY ARBITER:
    → No one OUTSIDE can know the sweet spot of the person INSIDE
    → Only: observe response → adjust → observe → adjust
    → = Dynamic equilibrium, NOT fixed formula
    → Each person SELF-CALIBRATES (Logic-Feeling-Balance.md §10)

  WHY THIS FILE HELPS (even though it doesn't prescribe):
    → Helps IDENTIFY: "which zone is the reward in?" (under / match / over)
    → Helps UNDERSTAND: "which mechanism is running?" (6 mechanisms §4)
    → Helps AVOID: common traps (wrong type, wrong amount, wrong timing)
    → = Describe, NOT prescribe (Logic-Feeling-Balance.md §8.1)

  🟡 Perception-action cycle for reward = dynamic equilibrium
  🟡 Domain feedback = only arbiter = Logic-Feeling-Balance.md core
```

### §5.3 — Why this is completely NORMAL

```
  IF reward calibration COULD be perfectly prescribed:
    → No need to observe responses
    → No need to adjust
    → No need for relationship
    → No need to LIVE through experience

  = Perfect prescription = omniscience
  = Humans ≠ omniscient (Logic-Feeling-Balance.md §7.4)
  = Therefore: cannot prescribe = CORRECT, NORMAL, EXPECTED

  Dynamic equilibrium between giver and receiver is NOT a problem.
  It IS the mechanism:
    → Giver observes → adjusts → receiver responds → giver observes → ...
    → INFINITE LOOP = relationship, management, parenting, teaching
    → Every attempt to shortcut the loop = fails (prescription = a shortcut)

  🟡 Cannot prescribe = expected = framework epistemological position
```

### §5.4 — Collective Calibration: the market = natural anti-over-reward

```
⭐ DYNAMIC EQUILIBRIUM NOT JUST 2-BODY — ALSO AT SOCIAL SCALE:

  §5.2 describes 2-body calibration (manager↔employee, parent↔child).
  But at larger scale: THE MARKET = collective calibration of
  MILLIONS of deals simultaneously.

  MECHANISM:
    Each deal = 2+ parties, each party HAS THEIR OWN gap:
      Manager: gap "needs someone to do the work" → willing to pay
      Employee: gap "needs money + meaning" → willing to work
      → Negotiation = 2 gaps INTERSECTING → equilibrium point

    "Everyone wants maximum" = each party pushes max per deal
    "Everyone accepts some amount" = equilibrium after negotiation
    = Status.md §5: exchange = the MOST COMMON mode in modern humans

    Market = collective equilibrium:
      → Salary level = "the compromise point that currently works"
      → No one prescribes → emerges from millions of negotiations
      → = Dynamic equilibrium AT SOCIAL SCALE

  COLLECTIVE CALIBRATION = NATURAL ANTI-OVER-REWARD MECHANISM:

    In a normal market:
      → Side A wants to pay LEAST → Side B wants to receive MOST
      → 2 forces PULLING IN OPPOSITE DIRECTIONS → equilibrium in MATCH zone
      → = Over-reward PREVENTED by the other side of the deal
      → = "If the sky won't yield to the earth, the earth must yield to the sky"

    Why it works:
      → Each side has CONSTRAINTS (budget, alternatives, market rate)
      → Constraints → cap reward at a reasonable level
      → = Collective → equilibrium → match zone → sustainable

  OVER-REWARD OCCURS WHEN COLLECTIVE CALIBRATION BREAKS DOWN:

    ① Lottery / random windfall:
       → Reward RANDOM → no negotiation → no calibration
       → Surplus without anchor → premature compilation (§3.4 Case 3)

    ② Power imbalance:
       → One side has EXTRAORDINARY leverage → pushes reward too far to one side
       → Examples: monopoly, corruption, nepotism
       → Over-rewarded side → §4⑤ competence-reward mismatch
       → BUT: those around will RECALIBRATE
         (Status.md §6: disruption → recalibrate → new equilibrium)

    ③ Inheritance / non-deal transfer:
       → Wealth transferred WITHOUT effort → no calibration
       → "Wealth" chunks compile WITHOUT accompanying deal experience
       → = §3.4 Case 3: gap exists + drive exists, depth insufficient

    ④ Schema [money = best] + normal salary:
       → Collective calibration WORKS → reward at equilibrium
       → Schema drive STILL WORKS → because reward MATCHES real gap
       → = NOT over-reward → NO problem
       → = Most people, most of the time → STABLE

  = Collective calibration is like an IMMUNE SYSTEM for over-reward:
    → Normal: prevents surplus naturally (deal = equilibrium)
    → When broken: over-reward penetrates → damage (§4)
    → Cross-ref: Status.md §5 (exchange positive-sum),
      Obligation.md §5.2 (money = obligation technology)

  🟡 Collective calibration as anti-over-reward = framework synthesis
  🟢 Market equilibrium: Adam Smith 1776, supply/demand
  🟢 Lottery winner outcomes: Brickman 1978
```

---

## §6 — OBSERVABLE INDICATORS

### §6.1 — Observing through communication + behavior

```
⭐ CAN OBSERVE REWARD STATE — PROBABILISTIC, NOT CERTAIN:

  ⚠️ IMPORTANT:
    → Observable = probability, NOT diagnosis
    → Same behavior CAN = many different underlying causes
    → AI-Schema-Detection.md: 3-tier model applies
      Tier 1: Observe patterns
      Tier 2: Expert verifies mechanism
      Tier 3: Self confirms (body knows best)
    → This file = Tier 1 (observe) → Tiers 2+3 NEEDED to confirm
```

### §6.2 — Under-reward signals

```
  VERBAL (through communication):
    → "Not appreciated" / "no one values me properly"
    → "Bored" (the kind that means "nothing coming back," different
      from boredom/Boredom.md)
    → "Not enough" / "need more" (genuine, not threshold adaptation)
    → "I try but no one sees it"
    → Implicit: talks LESS about the domain, low energy when discussing it

  BEHAVIORAL (through behavior):
    → Effort gradually decreasing (diminishing input → diminishing reward
      expectation)
    → Seeking alternatives (side job, new relationship, different domain)
    → Avoidance accumulating ("lazy" = can be compiled avoidance)
    → Withdrawal (retreating from relevant social context)

  BODY (through observation):
    → Visible sustained cortisol: fatigue, poor sleep, irritable
    → Chronically low energy (differs from boredom: boredom = high arousal)
    → Drive collapse signs (Cortisol-Baseline.md Role ② → ③)

  ⚠️ "Bored" CAN = Boredom.md (high arousal + unclear Imagine-Final)
     OR = under-reward (low reward → avoidance). Distinguish by context.
```

### §6.3 — Match signals

```
  VERBAL (through communication):
    → TALKS LITTLE ABOUT REWARD (habituated = invisible — Gratitude.md §4!)
    → Talks about the DOMAIN more than the reward
    → "I enjoy this" (approach-directed, not reward-directed)
    → No complaints, but also no enthusiastic praise

  BEHAVIORAL (through behavior):
    → Stable: drive self-sustaining, no constant external push needed
    → Approach tags visible: returns to domain on their own
    → Growth: chunks accumulate → skill increases → natural progression
    → Low maintenance: minimal external intervention needed

  BODY (through observation):
    → Stable baseline (cortisol healthy cycle: spike → resolve → reset)
    → Adequate energy level
    → Normal sleep pattern

  ⚠️ MATCH LOOKS "NORMAL" — EASY TO OVERLOOK:
    → Gratitude.md §3.1: gift habituates → invisible → "just normal"
    → Match = BEST STATE but INVISIBLE because prediction-delta ≈ 0
    → Only visible by COMPARISON: "before (under) vs now (match)"
    → = Paradox: best state = least visible
```

### §6.4 — Over-reward signals (per mechanism §4)

```
  ① THRESHOLD ADAPTATION:
    → "Not enough" DESPITE objectively high level + peer comparison
    → "Why does he/she have that but I don't?" — social comparison dominant
    → Speed of "getting bored" INCREASES: new reward → excited → adapt →
      "next" FASTER
    → = "Running but never arriving" (treadmill behavior)

  ② OVERJUSTIFICATION:
    → "Won't do it if no one pays" for something they USED TO ENJOY
    → Only discusses reward (money, bonus) instead of domain (skill, impact)
    → Remove external reward → immediate behavior collapse
    → = "No payment, no performance" (even though they used to do it
      because they loved it)

  ③ BRIDGE DEPENDENCY:
    → Panic when bridge reduces: "what if I don't have X?"
    → NO visible internal drive: "what do I want? I don't know"
    → Quarter-life crisis pattern (Education-Mechanism.md §3.4)
    → = "Only knew how to follow instructions, never learned what they want"

  ④ BASELINE SHIFT:
    → "Used to it" — talks about reward like an entitlement
    → LOSING reward → reaction DISPROPORTIONATELY STRONG (anger, not sadness)
    → "Why is this being taken away?" — even though reward was a bonus,
      not a contract
    → = SNC pattern (Crespi 1942)

  ⑤ COMPETENCE-REWARD MISMATCH:
    → Direction A (imposter): "I don't deserve this" + surrounding friction
    → Direction B (undervalued): "no one values me properly" + resentment
    → Team dynamics shift: envy, scrutiny, passive resistance
    → = Status.md Resource Access Map skewed visible through social behavior

  ⑥ EVALUATIVE/DIRECT-STATE IMBALANCE:
    → "Wealthy but sad" (Evaluative excess, Direct-State neglect)
    → "Fun but empty" (Direct-State excess, Evaluative absent)
    → Simple pleasures feel "flat" (Evaluative threshold too high)
    → Meaning void despite material comfort (Meaning.md anchor absent)
```

---

## §7 — EVALUATIVE/DIRECT-STATE × CALIBRATION

### §7.1 — Evaluative calibration = complex

```
⭐ EVALUATIVE REWARD — COMPLEX GOLDILOCKS:

  Evaluative = conditional, all 5 Body-Feedback-Preconditions required
  (Reward-Signal-Architecture §1.3)
  → Threshold ADAPTS: E₀→E₃ gradient → threshold rises with experience
  → Habituation: VTA habituates → same stimulus = lower prediction-delta →
    needs NOVELTY
  → Context-dependent: body state, relationship, cortisol → ALL affect it
  → Per-person: COMT × Childhood = 4 trajectories (PFC-Hardware.md §3.5)

  EVALUATIVE CALIBRATION NEEDS ANTI-HABITUATION:
    → Gratitude.md §3: 3 mechanisms (Variation, Comparison, Ritual)
    → Without anti-habituation → Evaluative reward decays → anhedonia
    → = "Everything is fine but I feel nothing" = Evaluative threshold
      HIGH + no delta

  E₃ = THE PEAK OF COMPLEXITY (Reward-Signal-Architecture §2.1):
    → Multi-domain coherence + compound insight + meta-evaluation
    → Threshold VERY HIGH → E₃ reward = RARE
    → When it arrives: POWERFUL (opioid + dopamine + cortisol drop
      compound)
    → When absent: "chronic boredom" (baseline at E₃ → everything below = "meh")
    → = Expert/professional hazard: E₃ calibrated → simple pleasures
      insufficient

  🟡 Evaluative calibration complexity = Reward-Signal-Architecture +
    Gratitude synthesis
```

### §7.2 — Direct-State calibration = simpler but crucial

```
⭐ DIRECT-STATE REWARD — SIMPLER GOLDILOCKS:

  Direct-State = hardware-based, simplified Body-Feedback-Precondition
  (Reward-Signal-Architecture §1.3)
  → Threshold ADAPTS LESS: body-state sensors = stable
  → Habituation: MINIMAL (body-level adaptation only, not VTA)
  → = RELIABLE baseline reward (Reward-Signal-Architecture §1.4:
    "evolutionary floor")

  DIRECT-STATE = SAFE BASELINE WHEN EVALUATIVE IS EXHAUSTED:
    → Burnout/anhedonia: Evaluative exhausted → Evaluative Reward OFF
    → Direct-State STILL accessible: touch, exercise, warmth, stretching
    → = "Backdoor" past the stuck Evaluative gate
    → 🟢 Van der Kolk 2014: body-oriented therapy for trauma

  DIRECT-STATE CALIBRATION:
    → Goldilocks: body-state range (CT afferents ~1–10 cm/s —
      Reward-Signal-Architecture §1.1)
    → Under Direct-State: body neglected (no touch, no movement) →
      baseline LOW
    → Match Direct-State: regular body-state engagement → stable baseline
    → Over Direct-State: rare but possible (exercise addiction,
      sensory overload)
    → = Direct-State calibration = KEEPING hardware channels active

  🟡 Direct-State = reliable + simple calibration =
    Reward-Signal-Architecture §1.4 synthesis
```

### §7.3 — Evaluative Gates Direct-State: calibration interaction

```
⭐ EVALUATIVE CALIBRATION AFFECTS DIRECT-STATE EXPERIENCE
   (Reward-Signal-Architecture §3):

  Evaluative Gates Direct-State mechanism (Reward-Signal-Architecture §3):
    → Strong E₃ anchor → sensory experience EVEN MORE POWERFUL
    → Weak E₃ anchor → sensory experience "flat"
    → = Evaluative calibration INDIRECTLY affects Direct-State quality

  CALIBRATION IMPLICATIONS:
    → Over-calibrate Evaluative → threshold HIGH → blocks Direct-State gate
    → = "Understand everything but can't feel it"
    → = Expert wine taster can't enjoy casual wine
    → = Musician can't enjoy pop music

    → Under-calibrate Evaluative → Evaluative threshold LOW →
      Direct-State gate ineffective
    → = "Can feel but can't go deep"
    → = Enjoyable but shallow

    → BALANCE Evaluative + Direct-State = both feed each other:
    → Evaluative depth → Direct-State amplified → Direct-State experience
      → Evaluative new insight → ...
    → = Virtuous cycle when balanced

  🟡 Evaluative Gates Direct-State × Calibration =
    Reward-Signal-Architecture §3 inference
```

---

## §8 — REWARD-ECONOMICS INSIGHTS THROUGH THE FRAMEWORK LENS

### §8.1 — 6 paths for "wealthy yet still chasing money"

```
⭐ 6 PATHS → MAPPED TO FRAMEWORK MECHANISMS:

  Same behavior ("wealthy yet still chasing money"),
  6 DIFFERENT UNDERLYING MECHANISMS:

  ① Background-Pattern not yet updated:
    → Grew up in scarcity → Background-Pattern [money = safety] compiled
      deep + high density
    → Now wealthy but Background-Pattern NOT YET UPDATED →
      cortisol baseline remains high
    → = PFC knows "wealthy" but body STILL feels "lacking"
    → Quadrant: Low Depth + High Density
      (Background-Pattern §2.2 → INVISIBLE but PERVASIVE)

  ② Threshold adaptation = §4①:
    → $100K → adapt → $1M → adapt → $10M → treadmill
    → Hedonic treadmill (Brickman 1971)

  ③ Money = proxy for Tier 2–3 = Reward-Signal-Architecture 5 Profiles
     + GAP SHIFT:
    → Money ≠ the goal → money = proxy for:
      Status (Profile ③ Social: serotonin ranking)
      Impact (Profile ② Coherence: "I was right, I changed the world")
      Score (Profile ④ Relief: "winning the game")
    → Chasing Profiles ②③④ via the PROXY of money,
      not actually chasing Profile ①

    GAP SHIFT — LABEL STAYS, MECHANISM CHANGES:
      Early stage: schema [money = best] → fills REAL survival gap
      Survival filled: gap SHIFTS to coherence/status/relief
      BUT: the LABEL stays as "making money" (PFC hasn't updated the label)
      → Billionaires STILL "make money" but real reward comes from:
        creativity (Profile ②), influence (Profile ③), winning deals
        (Profile ④), legacy (Profile ⑤)
      → They are typically NOT suffering — because body IS BEING FED
        through OTHER channels, money = just the scorecard

    WHY SCHEMA [MONEY = BEST] HAS HIGH TRUST:
      → Source ④ External Injection: continuous collective validation
        ("everyone needs money" → confirmed daily)
      → Source ② Experience: lack money → have money → problem solved
        (pay tuition, buy home, cover medical bills → REAL)
      → 2 trust sources STRONG + repeated CONSTANTLY → HIGH trust
      → Schema = FUNCTIONAL (works well at survival+social layers)
      → BUT INCOMPLETE: missing layer "money = proxy,
        body-base = endpoint"
      → = Anchor-Schema.md: HIGH Trust ≠ HIGH Quality
        (Trust = "I believe," Quality = "wholly correct")
      → Functionally incomplete schema = COMMON, not a flaw
      → Only becomes a problem when gap HAS SHIFTED but
        schema has NOT UPDATED

  ④ Weak prolactin = PFC-Hardware.md receptor system:
    → "Enough, stop" signal WEAK → CANNOT BRAKE
    → Not "wanting more" → it's a WEAK BRAKING MECHANISM

  ⑤ Identity lock = Meaning.md §3.3 IDENTITY type anchor:
    → "I = a money-maker" = IDENTITY anchor compiled rigid
    → Stop making money = identity crash = Meaning crisis
    → "Retired but depressed" = anchor collapse

  ⑥ Cortisol treadmill = Cortisol-Baseline.md §7.7 Role ④ Inertia:
    → Moderate cortisol continuously → dopamine increases → "productive"
    → Stop = cortisol DROPS → body "uncomfortable"
    → Chasing the CORTISOL STATE, not chasing money

  IDENTIFYING WHICH PATH (important because interventions differ):
    ① Background-Pattern not updated → anxious despite wealth,
      hoarding, defensive
    ② Threshold adaptation → "bored" if no increase, compares with peers
    ③ Money as proxy for tiers 2–3 → talks about impact/vision,
      money = tool
    ④ Weak prolactin → can't stop ANYTHING, not just money
    ⑤ Identity lock → afraid to retire, "don't know who I am
      if I stop working"
    ⑥ Cortisol treadmill → "rest = restless," needs busyness to feel calm

  → Same behavior, 6 DIFFERENT interventions.
  → Wrong path → intervention = INEFFECTIVE.
  → = Observation is more important than prescription.

  🟢 Brickman 1978 (lottery), Kahneman & Deaton 2010 (income + well-being)
  🟡 6-path mapping to framework = framework synthesis
```

### §8.2 — Money = shared chunk prediction token

```
🟡 WHAT MONEY IS THROUGH THE FRAMEWORK LENS:

  Money = PROXY TOKEN for prediction:
    → "$1,000" = shared chunk that society compiled: "can exchange for X"
    → Money itself HAS NO body-base value (paper, digits)
    → Value resides in prediction: "have money → body-base GETS FED"

  = Shared Chunk Prediction:
    → Everyone compiles THE SAME chunk: "$1,000 ≈ X food ≈ Y services"
    → THIS chunk = shared across society → TRUSTWORTHY
    → Inflation = chunk prediction invalidated → SNC → anger

  Money ≈ Status.md Resource Access Map extension:
    → Have money = resource access MAP EXPANDS
    → More money = more schemas "accessible"
    → Lose money = schemas "blocked" → status DROP → cortisol

  🟡 Money = proxy token = Reward-Economics.md insight + framework
    chunk reframe
```

### §8.3 — Habituation Blindness × Economics

```
🟡 prediction-delta = 0 ≠ VALUE = 0:

  Oxygen: prediction-delta = 0 (completely habituated), VALUE = life/death
  Daily meals: prediction-delta = 0 (baseline), VALUE = essential nutrition
  Monthly salary: prediction-delta = 0 (compiled baseline), VALUE = survival

  COMMON CONFUSION:
    → prediction-delta = 0 → "no value" → ignore it → lose it →
      SNC → "turns out it was important"
    → = Habituation Blindness: body SEES it but doesn't REWARD it →
      PFC thinks "not needed"
    → Gratitude.md §3: 3 anti-habituation mechanisms =
      AGAINST habituation blindness

  ECONOMICS IMPLICATION:
    → What matters MOST = what has prediction-delta ≈ 0 (habituated =
      invisible)
    → What generates STRONG positive prediction-delta = often new/rare
      but may NOT be important
    → = Novelty bias: brain tracks novelty > tracks importance
    → = Why a salary CUT "hurts" more than a salary RAISE "pleases"
      (loss aversion)
    → Protect.md: loss aversion = f(replaceability × attachment)

  🟢 Loss aversion: Kahneman & Tversky 1979 (prospect theory)
  🟢 Endowment effect: Thaler 1980
  🟡 prediction-delta = 0 ≠ Value = 0 = Gratitude.md +
    Reward-Economics insight
```

---

## §9 — HONEST ASSESSMENT

### §9.1 — Confidence per section

```
  ┌──────────────────────────────┬──────────┬──────────────────────────┐
  │ Section                      │ Level    │ Notes                    │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §1 Goldilocks per-gap        │ 🟢       │ Well-documented:         │
  │                              │          │ Yerkes-Dodson, Brickman, │
  │                              │          │ Schultz                  │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §2 Gap types × reward match  │ 🟡       │ Body-Feedback-Mechanism  │
  │                              │          │ 3 dynamics = 🟢          │
  │                              │          │ Mapping to reward type   │
  │                              │          │ = framework synthesis    │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §3 Goldilocks zones          │ 🟡       │ Under/over = well-known  │
  │                              │          │ Match description =      │
  │                              │          │ framework synthesis      │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §4 6 over-reward mechanisms  │ 🟢→🟡   │ ①②④: strong research.   │
  │                              │          │ ③⑤⑥: framework synth    │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §5 Dynamic equilibrium       │ 🟡       │ Parallel Logic-Feeling-  │
  │                              │          │ Balance = framework meta  │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §6 Observable indicators     │ 🟡       │ Probabilistic, not       │
  │                              │          │ diagnostic. Per-case     │
  │                              │          │ verification needed      │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §7 Evaluative/Direct-State   │ 🟡       │ Reward-Signal-           │
  │    calibration               │          │ Architecture synthesis   │
  │                              │          │ applied to calibration   │
  ├──────────────────────────────┼──────────┼──────────────────────────┤
  │ §8 Economics insights        │ 🟡       │ v5.5 insights remapped   │
  │                              │          │ to framework mechanisms  │
  └──────────────────────────────┴──────────┴──────────────────────────┘
```

### §9.2 — Value + Limitations

```
  VALUE OF THIS FILE:
    → Synthesizes insights from ~15 files into 1 CALIBRATION lens
    → 6 over-reward mechanisms = organized for the first time
      (scattered previously)
    → Dynamic equilibrium thesis = made explicit (implicit before)
    → Observable indicators = practical guide
    → Gap type × reward match = new mapping

  LIMITATIONS:
    → This file = OBSERVATION SYNTHESIS, creates no new mechanisms
    → Reality = continuous, high-dimensional → file simplifies
    → Observable indicators = probabilistic, REQUIRES case-by-case
      verification
    → 6 mechanisms can overlap in practice (not always separable)
    → Dynamic equilibrium = principled position but untestable
      in absolute terms
```

### §9.3 — Predictions (testable)

```
  P1: Over-reward group (high external reward, minimal gap) will show
      faster threshold adaptation than match group
      → Measure: hedonic adaptation speed via longitudinal survey

  P2: Direct-State reward when Evaluative is exhausted will restore
      partial function
      → Measure: body-oriented intervention for burnout patients

  P3: Wrong gap type × reward match will produce LOWER satisfaction
      than under-reward with CORRECT match
      → Measure: employee satisfaction per reward-fit survey

  P4: Variation (Gratitude §3.2) injection will slow threshold
      adaptation
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
  │ v1.0                             │ 5 Profiles, Evaluative Gates         │
  │                                  │ Direct-State — §7 calibration        │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Mechanism.md v1.2  │ 3 dynamics (Shift/Miss/Gap),        │
  │                                  │ compound — §2 gap types              │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gap-Direction.md v1.0            │ Gap has direction, "unknown =       │
  │                                  │ no gap" — §1.3 foundation           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gratitude.md v1.1                │ §3 anti-habituation, §4 baseline    │
  │                                  │ shift — §4①④ mechanisms             │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Education-Mechanism.md v1.0      │ §3 bridge, Source ④,                │
  │                                  │ overjustification — §4②③            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.0        │ §7.7 5 Roles (② Holding,           │
  │                                  │ ④ Inertia) — §3.1 under-reward      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Status.md v2.0                   │ §1 Resource Access Map — §4⑤       │
  │                                  │ competence-reward mismatch          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Logic-Feeling-Balance.md v1.0    │ §6–§7 infinite regress — §5         │
  │                                  │ dynamic equilibrium parallel        │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Hardware.md v1.1             │ §3.4 COMT × Reward, §3.5           │
  │                                  │ Childhood — §1.2 per-person         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Background-Pattern.md v1.0       │ Invisible bias on gap landscape     │
  │                                  │ — §1.2 per-context                  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Connection.md v3.1               │ §9 calibration between 2 bodies     │
  │                                  │ — §5.2 perception-action cycle      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Meaning.md v2.0                  │ IDENTITY anchor, life-level —       │
  │                                  │ §4⑥ Evaluative/Direct-State         │
  │                                  │ imbalance, §8.1⑤ identity lock      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Obligation.md v1.0               │ Cortisol holding (Role ②),         │
  │                                  │ 5-factor — §5.2 equilibrium         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ AI-Schema-Detection.md v2.0      │ 3-tier model — §6.1 observe        │
  │                                  │ ≠ diagnose                          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Reward-Economics.md v5.5         │ 6 paths, money = proxy — §8        │
  │ (Applications/)                  │ insights remapped to framework      │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

> *Reward Calibration v1.1 — Observation File.*
> *Reward has a Goldilocks zone per-gap: cannot be prescribed, can only be observed + adjusted.*
> *Dynamic equilibrium, not a fixed formula.*
> *Domain feedback = the only arbiter.*
