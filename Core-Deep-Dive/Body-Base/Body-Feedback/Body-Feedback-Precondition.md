---
title: Body-Feedback Precondition — 5 Preconditions for Signal Fire
version: 1.1
created: 2026-05-30
refined: 2026-06-14 (v1.1 — §6 Precondition-5: "tag" → "NET link pattern" throughout. Observation parameter model aligned with Drill v4.0 §4. Version refs updated.)
status: REFERENCE v1.1
scope: |
  PRECONDITION REFERENCE: WHEN does body-feedback signal (reward/dissonance) fire?
  5 Preconditions model — formalized from 03-Reward.md §3 (drill origin).
  Each precondition: definition, mechanism, failure mode, refinement insights.
  Scope qualifier: ALL 5 required for Evaluative. Direct-State = simplified subset.
  v1.0: Refined from drill H10 — added direction component, genesis/decode split,
  boredom disambiguation, dynamic zone, 4-pathway quality ceiling.
purpose: |
  Existing files classify body-feedback by:
    WHAT KINDS:  Reward-Signal-Architecture.md (reward types)
                 Dissonance-Signal-Architecture.md (dissonance types)
    HOW:         Body-Feedback-Mechanism.md (chunk dynamics)
    VOCAB:       Body-Feedback-Label.md (terminology)
  This file adds axis: WHEN — 5 preconditions determine whether signal fires or not.
  Completes the set of 4 siblings: Mechanism → Label → Precondition → Signal Architecture.
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — peer with Body-Feedback-Mechanism.md.
  Sibling relationship:
    Body-Feedback.md          = SYNTHESIS entry point (overview)
    Body-Feedback-Mechanism.md = HOW signal arises (chunk dynamics)
    Body-Feedback-Label.md     = VOCAB reference (terminology)
    Body-Feedback-Precondition.md = ⭐ WHEN signal fires (this file)
    Reward-Signal-Architecture.md = WHAT KINDS reward
    Dissonance-Signal-Architecture.md = WHAT KINDS dissonance
dependencies:
  - Body-Feedback.md v2.0 — §5.2 H10 summary table (pointer to this file)
  - Body-Feedback-Mechanism.md v2.1 — §6.2 chunk dynamics × preconditions mapping
  - Body-Feedback-Label.md v2.1 — vocabulary reference
  - Reward-Signal-Architecture.md v2.1 — §1.3 Evaluative/Direct-State × Precondition-1–Precondition-5
  - Dissonance-Signal-Architecture.md v1.0 — dissonance application (§9 cross-ref)
  - 03-Reward.md v1.1 — §3 H10 drill origin, §2 7-step VTA
  - 04-Integration.md — §9 H10 refined
  - Gap-Direction.md v2.0 — §3 "don't know it exists = no gap", §6.3 hierarchy
  - Chunk.md v3.1 — chunk substrate, context-tag model, Direction-At-Compile
  - Compile-Taxonomy.md v3.0 — §6 4-pathway model (Precondition-5)
  - Cortisol-Baseline.md v2.4 — §3.3 Direction-At-Compile, §7 source > level, §7.7 5 roles taxonomy
  - Reward-Calibration.md v1.1 — §1.2 Goldilocks per-gap dynamic
  - Boredom.md v2.1 — §1 + §7 boredom ≠ Precondition-3 failure
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Precondition — 5 Preconditions for Signal Fire

> **Same piece of captivating music.**
> Someone who's never heard it → "too strange" (insufficient chunks to decode).
> Someone hearing it for the first time → "captivating!" (novel + just enough match).
> Someone who's heard it 1,000 times → "boring" (no delta left).
> Someone forced to listen as a child → "dislike even though I know it's good" (negative-dominant NET).
> Someone saturated with music → "feel nothing" (no gap active).
>
> Same stimulus. 5 people. 5 DIFFERENT responses.
> Each response = a DIFFERENT precondition failing.
>
> Body-feedback signal does NOT fire automatically when a stimulus arrives.
> Signal fires WHEN AND ONLY WHEN all 5 preconditions are simultaneously met.
>
> This file formalizes those 5 preconditions.

---

## §0 — Position + Scope

### §0.1 — 4 questions, 4 files

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Body-Feedback System                             │
│                                                                     │
│  WHAT KINDS?  → Reward-Signal-Architecture.md                      │
│                 Dissonance-Signal-Architecture.md                   │
│                                                                     │
│  HOW?         → Body-Feedback-Mechanism.md (chunk dynamics)        │
│                                                                     │
│  WHEN?        → ⭐ Body-Feedback-Precondition.md (THIS FILE)       │
│                 5 preconditions: Precondition-1–Precondition-5      │
│                 Signal fires if and only if all 5 Preconditions met │
│                                                                     │
│  VOCAB?       → Body-Feedback-Label.md (terminology)               │
│                                                                     │
│  OVERVIEW?    → Body-Feedback.md (synthesis entry point)           │
└─────────────────────────────────────────────────────────────────────┘
```

### §0.2 — Scope + boundary rules

**This file DEFINES**:
- 5 preconditions for body-feedback signal fire (Precondition-1–Precondition-5)
- Each precondition: mechanism, met/failed states, refinement insights
- Conjunction logic (AND-gate structure)
- Developmental arc (infant → adult → aging)
- Dissonance application (not just reward)

**This file does NOT duplicate** (cross-references only):

| Content | Belongs in | Cross-ref |
|---|---|---|
| Evaluative/Direct-State × Precondition-1–Precondition-5 table | Reward-Signal-Architecture §1.3 | §1.2, §2-§6 per-precondition notes |
| Chunk dynamics × preconditions mapping | Body-Feedback-Mechanism §6.2 | §7 conjunction logic |
| H10 48-line summary table | Body-Feedback §5.2 | §0.1 pointer |
| Timing asymmetry (dissonance → reward) | Dissonance-Signal-Architecture | §9 cross-ref |
| 7-step VTA mechanism | 03-Reward.md §2 | §4.2 cross-ref |

### §0.3 — Reading prerequisites

```
MUST READ FIRST:
  Body-Feedback.md         — dual-pull, interface loop, body-base
  03-Reward.md §2-§3       — 7-step VTA, H10 drill origin
  Chunk.md v3.1             — chunk substrate, context-tag, Direction-At-Compile
  Compile-Taxonomy.md      — 4-pathway model (for §6 Precondition-5)

READ IN PARALLEL:
  Reward-Signal-Architecture — WHAT KINDS reward (→ type-split per precondition)
  Dissonance-Signal-Architecture — WHAT KINDS dissonance (→ §9 dissonance application)
  Body-Feedback-Mechanism — HOW chunks fire (→ dynamics × preconditions)
  Gap-Direction.md — gap has direction (→ §2 Precondition-1, §5 Precondition-4)
```

### §0.4 — Origin + evolution

🟡 This file formalizes "H10" — hypothesis label from drill 03-Reward.md §3.

```
DRILL ORIGIN (2026):
  03-Reward.md §3: "H10 — Body Signal Precondition Hypothesis v2"
  → 5 preconditions: Schema pending, Chunks base, prediction-delta,
    Goldilocks zone, Chunk tag

FRAMEWORK EVOLUTION:
  ① Drill → 92+ files use "H10" as concept name
  ② Gap-Direction.md → Precondition-1 missing direction, Precondition-2 missing genesis/decode split
  ③ Boredom.md → boredom ≠ Precondition-3 failure (disambiguation needed)
  ④ Reward-Calibration.md → Goldilocks zone dynamic (not fixed 40-70%)
  ⑤ Compile-Taxonomy.md → Precondition-5 binary → 4-pathway quality ceiling
  ⑥ Cortisol-Baseline.md → Precondition-5 opioid/cortisol → Direction-At-Compile gate

THIS FILE: Refines + formalizes all insights above into official reference.
```

---

## §1 — Formal Statement

### §1.1 — The conjunction claim

🟡 **Body-Feedback Precondition Statement v1.0**:

> Body-feedback signal (reward OR dissonance) fires to full magnitude
> WHEN AND ONLY WHEN **all 5 preconditions** are simultaneously met:
>
> | # | Precondition | Question it answers |
> |---|---|---|
> | Precondition-1 | **Directed-Gap** | Is there an active gap? Where is the gap directed? |
> | Precondition-2 | **Chunk-Substrate** | Are there sufficient chunks to decode the stimulus? |
> | Precondition-3 | **Delta-Gate** | Is there enough change for VTA to detect? |
> | Precondition-4 | **Match-Range** | Does the match fall within a suitable range? |
> | Precondition-5 | **Compile-Gate** | Does the chunk NET link pattern permit the signal in the correct direction? |
>
> **Logical form**: Signal_full = Precondition-1 ∧ Precondition-2 ∧ Precondition-3 ∧ Precondition-4 ∧ Precondition-5

**Claim strength**: 🟡 Framework synthesis — each individual precondition has research support 🟢,
but the conjunction "ALL 5 required" is a framework-level claim without direct empirical test yet.

### §1.2 — Scope qualifier: Evaluative vs Direct-State

```
⭐ "ALL 5 required" applies ONLY to EVALUATIVE reward/dissonance.

EVALUATIVE (compiled patterns, learning-dependent):
  → Precondition-1–Precondition-5 ALL required
  → Examples: appreciating captivating music, solving a problem, enjoying Van Gogh

DIRECT-STATE (hardware signals, body-need-driven):
  → Precondition-1 simplified: body-need ALWAYS present (hunger, thirst, pain, touch)
  → Precondition-2 minimal: hardware paths from birth (compiled chunks not required)
  → Precondition-3 uncertain: may bypass VTA entirely (posterior insula pathway)
  → Precondition-4 hardware: CT afferent ~1-10cm/s = fixed range (not learned)
  → Precondition-5 N/A: hardware signals, no compiled link pattern needed

  → Type-split details per precondition: Reward-Signal-Architecture §1.3

CLINICAL IMPLICATION:
  Evaluative blocked by Precondition-2/Precondition-3/Precondition-5 failures → anhedonia, burnout
  Direct-State NOT blocked → "touch still works" = reliable baseline
  Loss of BOTH = rare + devastating (advanced depression, severe trauma)
```

### §1.3 — Falsifiability

🟡 Each precondition creates a **testable prediction** when violated:

| Violate | Prediction | Observable |
|---|---|---|
| Precondition-1 | Full person offered food → no reward | Alliesthesia research (Cabanac 1971) 🟢 |
| Precondition-2 | Van Gogh to untrained → confusion not reward | Art appreciation studies 🟢 |
| Precondition-3 | Routine event → no alert despite objective value | Hedonic adaptation literature 🟢 |
| Precondition-4 | Extreme novelty OR familiarity → no reward | Berlyne 1960 inverted-U 🟢 |
| Precondition-5 | Math-avoidant adult given "interesting" math → aversion | Clinical observation 🟢 |

**Framework prediction**: Cases of "should reward but doesn't" = at least 1 precondition failing.
Cases of "shouldn't reward but does" = ALL 5 are met but the observer hasn't recognized it.

### §1.4 — Precondition hierarchy

🟡 From Gap-Direction.md v2.0 §6.3 — preconditions have a hierarchy, not a flat AND-gate:

```
"Don't know it exists" → Precondition-2 → Precondition-1 → Precondition-3 → Precondition-4 → Precondition-5 → signal fires

Layer 0 (GENESIS):   "Don't know it exists = no gap" — prerequisite for Precondition-2
Layer 1 (SUBSTRATE):  Precondition-2 Chunk-Substrate — ARE there chunks to form a gap?
Layer 2 (GAP):        Precondition-1 Directed-Gap — gap active + has direction?
Layer 3 (DETECTION):  Precondition-3 Delta-Gate — VTA detects delta?
Layer 4 (MATCH):      Precondition-4 Match-Range — match in suitable range?
Layer 5 (DIRECTION):  Precondition-5 Compile-Gate — NET link pattern permits signal in correct direction?

⭐ Hierarchy does NOT change "ALL 5 required" claim.
  → But TELLS US which failure mode occurs FIRST.
  → Precondition-2 fail = Precondition-1 CANNOT form (for schema-level gaps).
  → Precondition-3 fail = Precondition-4 NOT evaluated (sequential dependency).
```

---

## §2 — Precondition-1: Directed-Gap

### §2.1 — Definition

🟡 **Precondition-1 — Directed-Gap**:

> Body must have an **active gap** — an unresolved body-need OR schema seeking
> upgrade — AND that gap must have **direction** (toward what kind of fill).
>
> Gap = opening in the schema landscape where new information can fit.
> Direction = constraints on valid fill, determined by surrounding chunks.

**Old name**: "Schema Pending Status" (drill 03-Reward.md §3.2)
**Changed because**: The old name missed (a) hardware-driven gaps and (b) the direction component.

### §2.2 — Precondition-1a: Hardware-driven gaps

🟢 Hardware-driven gaps = body-needs from Body-Base:
- Hunger, thirst, pain avoidance, temperature, social contact, sleep
- ALWAYS present at some level (homeostatic regulation)
- Infants have from birth — no learning required
- Direction inherent: hunger → food direction, thirst → water direction

```
Precondition-1a characteristics:
  ① Always available (homeostatic cycle)
  ② Direction = hardware-defined (specific body-need category)
  ③ Does not require Precondition-2 (chunks) — hardware path from birth
  ④ Intensity varies (satiated ↔ deprived)
  ⑤ → Primary source for DIRECT-STATE reward/dissonance
```

### §2.3 — Precondition-1b: Pattern-driven gaps

🟡 Pattern-driven gaps = schema-level needs:
- Coherence gap: incomplete knowledge, unresolved problem
- Curiosity gap: detected pattern hinting at more
- Skill gap: knowing you could do better but haven't yet
- Social gap: disconnection from expected social state

```
Precondition-1b characteristics:
  ① Requires Precondition-2 first (must have chunks before a gap can exist — §2.5)
  ② Direction = f(surrounding chunk network) (Gap-Direction.md §1.1)
  ③ Learned, not innate — develops through experience
  ④ Can be installed (education, marketing, social exposure)
  ⑤ → Primary source for EVALUATIVE reward/dissonance
```

**Gap direction examples**:
- A musician hears a phrase → gap "where should the melody go next?" = clear direction
- A programmer encounters a bug → gap "what's causing this bug?" = narrow direction
- A child who doesn't know guitar exists → gap CANNOT EXIST (→ §2.5)

### §2.4 — Direction implicit

🟡 From Gap-Direction.md v2.0 §1.1:

> **Gap_Direction = f(surrounding_chunk_network_structure)**
>
> Shape of hole = constraints on valid fill.
> Surrounding chunks DEFINE the direction.

**Why direction matters for Precondition-1**:
- Gap WITHOUT direction = not really a gap (vague unease, not actionable)
- Direction specifies WHAT KIND of stimulus will fill the gap
- Direction determines what Precondition-4 (Match-Range) evaluates the match AGAINST
- Without direction → Precondition-4 has no reference point → signal cannot fire

```
Gap-Direction 4 properties (Gap-Direction.md §4):
  ① Direction — toward WHAT kind of fill
  ② Specificity — narrow (expert) vs broad (beginner)
  ③ Depth — signal strength (how much body "wants" fill)
  ④ Range — Goldilocks zone WITHIN that direction
```

### §2.5 — Precondition-2 → Precondition-1 dependency (schema-level)

🟡 Critical insight from Gap-Direction.md §3:

> **"Don't know it exists = no gap"**
> Chunks_related_to_X = ∅ → Gap_about_X = IMPOSSIBLE
>
> You CANNOT miss something you don't know exists.

**Implications**:
- Precondition-2 (Chunk-Substrate) is a **prerequisite** for Precondition-1b (Pattern-driven gap)
- If Precondition-2 fails at genesis level → Precondition-1b CANNOT form
- Hardware Precondition-1a does NOT need Precondition-2 (body-needs exist from birth)
- This is "Layer 0" — prior to the precondition model itself

```
Precondition-2 → Precondition-1 dependency chain:
  ① No chunks about X → gap about X DOES NOT EXIST → Precondition-1 fails
  ② A few chunks about X → gap is VAGUE → Precondition-1 partial (direction broad)
  ③ Many chunks about X → gap is CLEAR → Precondition-1 full (direction specific)

5 consequences (Gap-Direction.md §3.4):
  → Desire is CONSTRUCTED (not innate except hardware Tier 1)
  → Education must BUILD chunks before presenting answers
  → Marketing = gap installation (create chunks → create gap → sell fill)
  → Therapy must MAP the gap landscape (what gaps exist?)
  → Cross-cultural = different gap landscapes (different chunk bases)
```

### §2.6 — Precondition-1 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Satiated | Body-need filled → gap closed | "No desire" |
| No active goal | Schema landscape stable | "Don't need anything" |
| Empty scroll | Stimuli arrive, no gap matches | "Scrolling without stopping" |
| Direction lost | Gap exists but surrounding chunks insufficient | "Want something but don't know what" |

🟢 Research: Cabanac 1971 alliesthesia — same stimulus (sugar) shifts from
pleasant to unpleasant as body-need (hunger) gets filled. Precondition-1 failure = signal stops.

---

## §3 — Precondition-2: Chunk-Substrate

### §3.1 — Definition

🟡 **Precondition-2 — Chunk-Substrate**:

> Body must have **sufficient chunks** to (a) form a gap about a domain (genesis)
> AND (b) decode incoming stimulus for evaluation (decode).
>
> Chunks = compiled patterns from past experience (Chunk.md §2).
> Without chunks, body cannot even RECOGNIZE stimulus as relevant.

**Old name**: "Chunks Base Adequacy" (drill 03-Reward.md §3.3)
**Changed because**: "Adequacy" is vague. "Substrate" = necessary foundation, clearer.

### §3.2 — Precondition-2a: Genesis failure ("don't know it exists = no gap")

🟡 From Gap-Direction.md §3 — LAYER 0, prior to the precondition model:

> **Precondition-2a Genesis**: Chunks_related_to_X = ∅ → Gap CANNOT EXIST
>
> This is NOT "stimulus arrives and can't be decoded" (= Precondition-2b).
> This is "gap about X has NEVER FORMED" — prior to Precondition-1.

**Precondition-2a examples**:
- A 3-year-old who doesn't know guitar exists → CANNOT have a gap "want to play guitar"
- Someone who's never heard jazz → CANNOT have a gap "want to hear jazz"
- A culture without the concept of "exams" → CANNOT have a gap "want to pass exams"

```
Precondition-2a vs Precondition-2b — key distinction:
  Precondition-2a = BEFORE stimulus (gap cannot form → desire doesn't exist)
  Precondition-2b = AFTER stimulus (stimulus arrives but insufficient chunks to decode)
  Precondition-2a fail → Precondition-1 fail (no gap possible)
  Precondition-2b fail → confusion/strangeness (stimulus present but undecodable)
```

### §3.3 — Precondition-2b: Decode failure

🟡 Precondition-2b: Stimulus arrives but body **cannot decode** it:

> New input → unconscious searches for matching chunks → NO match found
> → "Cannot decode" → uncertainty → mild cortisol → NOT reward

**Precondition-2b examples**:
- Van Gogh shown to untrained viewer → chunks insufficient for art evaluation
  → "Can't understand" (confusion, not reward) — even though painting is objectively valuable
- Atonal music to pop listener → chunks insufficient for harmonic evaluation
  → "Sounds chaotic" — same music = masterpiece to trained listener
- Advanced mathematics to beginner → chunks insufficient for pattern recognition
  → "I don't understand any of this" — same proof = "beautiful" to mathematician

🟢 Research: Art appreciation studies confirm training → appreciation (Leder et al. 2004).
Mere exposure without understanding ≠ appreciation — chunk compilation required.

### §3.4 — Evaluative vs Direct-State

```
EVALUATIVE:
  Precondition-2 = REQUIRED — compiled chunks needed to evaluate pattern
  → Insufficient chunks = confusion → no reward
  → Van Gogh case = Precondition-2 failure (NOT Precondition-4)

DIRECT-STATE:
  Precondition-2 = MINIMAL — hardware paths from birth
  → CT afferents (touch), taste buds (sweet/bitter), nociceptors (pain)
  → Compiled chunks not required — hardware decode sufficient
  → Infant from birth already rewards from touch, sweetness
```

### §3.5 — Precondition-2 ≠ Precondition-5 distinction

```
⚠️ Precondition-2 and Precondition-5 DIFFER — both involve chunks but at DIFFERENT layers:

  Precondition-2 Chunk-Substrate:
    Question: Are there ENOUGH chunks to DECODE the stimulus?
    Layer: SUBSTRATE — the foundation
    Failure: confusion ("can't understand")
    → Chunks EXIST or NOT

  Precondition-5 Compile-Gate:
    Question: Once chunks decode → does the NET link pattern PERMIT the signal in the correct direction?
    Layer: DIRECTION — signal direction
    Failure: signal fires in wrong direction ("understand but dislike")
    → Chunks exist BUT NET link pattern determines direction (positive or negative dominant)

  Example: Math
    Precondition-2 fail: "I don't understand math" (insufficient chunks to decode)
    Precondition-5 fail: "I understand math but hate math" (chunks exist, negative-dominant NET)
```

### §3.6 — Precondition-2 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Genesis (Precondition-2a) | No chunks about domain → gap impossible | "Don't know it exists" |
| Decode (Precondition-2b) | Stimulus arrives, insufficient chunks to parse | "Can't understand" / confusion |
| Partial decode | Some chunks match, insufficient for evaluation | "Vaguely understand but not enough" |
| Cross-domain gap | Chunks exist in domain A, not B — transfer fails | "Good at music but blind to poetry" |

**Developmental trajectory** 🟡:
- Infant: minimal chunks → most stimuli = Precondition-2b fail → exploration critical
- Child: chunks accumulating → Precondition-2b failures narrow → domains opening
- Adult: rich chunk base → Precondition-2b rare in familiar domains → but still possible in NEW domains
- Expert: deep chunks in specialty → Precondition-2 = non-issue there → BUT may Precondition-2-fail in unfamiliar fields

🟢 Research: Expertise studies (Chi et al. 1981) — experts chunk patterns that novices cannot see.
Same chess board: grandmaster sees structure, novice sees random pieces = Precondition-2 difference.

---

## §4 — Precondition-3: Delta-Gate

### §4.1 — Definition

🟡 **Precondition-3 — Delta-Gate**:

> The change (delta) between current state and prediction must be **large enough**
> to exceed VTA habituation threshold, triggering dopamine alert.
>
> Precondition-3 answers: "Is there anything NEW?" — detection mechanism, not value judgment.
> VTA dopamine = doorbell. Precondition-3 = whether the doorbell RINGS.

**Old name**: "Prediction-Delta Threshold" (drill 03-Reward.md §3.4)
**Changed because**: "Delta-Gate" is more concise, emphasizes the gate nature (open/close).

### §4.2 — VTA habituation mechanism

🟡 Mechanism (03-Reward.md §2.2-§2.4, Step 2-3):

```
① VTA habituated to stable patterns → ignores familiar
② New input arrives → compare with prediction
③ Delta = |actual - predicted|
④ Delta > threshold → VTA fires dopamine → PFC attention triggered
⑤ Delta < threshold → VTA silent → no downstream processing

Threshold affected by:
  → Baseline arousal (cortisol level modulates sensitivity)
  → Recent history (many consecutive deltas → threshold rises)
  → DRD4 variant (§4.5)
  → Domain expertise (expert detects finer deltas)
```

🟢 Research: Schultz 1997 — VTA dopamine neurons fire to unexpected rewards,
NOT to expected rewards. Response transfers to prediction cue after learning.
Prediction error signal = Precondition-3 mechanism.

### §4.3 — Scope: Evaluative ONLY

```
⭐ Precondition-3 applies fully ONLY to EVALUATIVE reward/dissonance.

EVALUATIVE:
  → Precondition-3 REQUIRED — VTA must detect delta
  → No delta → no alert → no downstream reward
  → Hedonic adaptation = Precondition-3 erosion over time

DIRECT-STATE:
  → Precondition-3 UNCERTAIN — may bypass VTA entirely
  → Posterior insula pathway: body-need → direct signal (no delta check)
  → Example: hungry person eats → reward fires WITHOUT needing "surprise"
  → Touch (CT afferents) → opioid release WITHOUT prediction error
  → Details: Reward-Signal-Architecture §1.3
```

### §4.4 — Boredom disambiguation

🟡 **Boredom ≠ Precondition-3 failure.** From Boredom.md v2.1 §1 + §7:

> Boredom = 2-dimensional state requiring 3 co-conditions:
> ① Gap exists (something wanted but absent)
> ② Gap unfilled (no available fill)
> ③ Signal below PFC threshold (too diffuse for action)
>
> Missing ANY single condition = NOT boredom.
> Missing ① = contentment. Missing ② = drive. Missing ③ = active emotion.

```
WHY boredom ≠ simple Precondition-3 failure:

  Precondition-3 failure alone = "no delta detected" → neutral, not bored
  → Routine events slip by unnoticed — NO dissonance, NO boredom

  Boredom requires Precondition-1 (gap EXISTS) + Precondition-4 (no suitable match available)
  → Body WANTS something (Precondition-1 met) but NOTHING matches (Precondition-4 fail)
  → Plus: signal too diffuse for PFC to commit to action

  → Boredom = Precondition-1 met + Precondition-4 fail + PFC unclear = compound state
  → NOT = Precondition-3 fail (Precondition-3 fail = simply nothing detected)
```

### §4.5 — DRD4 modulation

🟡 DRD4 receptor variant (03-Reward.md §2.5, Step 3) modulates Precondition-3 DOWNSTREAM:

```
DRD4 = Step 3 FILTER, not Precondition-3 itself:
  → Precondition-3 = VTA fires dopamine (Step 2)
  → DRD4 = how dopamine is RECEIVED by target neurons (Step 3)

DRD4-7R ("novelty-seeking" variant):
  → Lower sensitivity → needs MORE delta for same response
  → Thresholds higher → routine feels MORE boring
  → BUT big delta → BIGGER response (amplified)

DRD4-4R (common variant):
  → Normal sensitivity → standard delta-response curve
  → Moderate novelty sufficient for reward

⚠️ DRD4 DOES NOT change Precondition-3 gate itself.
  → Precondition-3 = VTA detection. DRD4 = post-detection filtering.
  → Person with DRD4-7R: Precondition-3 fires normally, but downstream IMPACT differs.
```

🟢 Research: Ebstein et al. 1996 — DRD4-7R associated with novelty seeking.
Benjamin et al. 1996 — replicated. Meta-analyses: small but consistent effect.

### §4.6 — Precondition-3 → Precondition-4 sequential dependency

🟡 Precondition-3 must fire BEFORE Precondition-4 is evaluated:

```
Sequence:
  Precondition-3 fires (delta detected) → dopamine alert → PFC attention
  → THEN Precondition-4 evaluated (match quality assessed)

Precondition-3 fail → Precondition-4 NEVER CHECKED:
  → No delta → no alert → PFC doesn't attend → match quality irrelevant
  → Stimulus may be PERFECT match (Precondition-4 would pass) but Precondition-3 blocks detection

Precondition-3 pass → Precondition-4 CHECKED:
  → Delta detected → attention → NOW evaluate: match falls in what range?
  → Precondition-4 pass → continue to Precondition-5
  → Precondition-4 fail → signal attenuated or wrong direction
```

### §4.7 — Precondition-3 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Habituation | Same pattern repeated → VTA adapts | "Boring" (hedonic treadmill) |
| Routine | Life predictable → few deltas | "Monotonous" |
| Overstimulation | Too many deltas → threshold rises | "Numb" (sensory overload) |
| Anhedonia (clinical) | VTA function impaired | "Feel nothing" (depression symptom) |

**Hedonic adaptation cycle** 🟢:
```
Trial 1:   huge delta → reward intense
Trial 10:  moderate delta → reward moderate
Trial 100: small delta → reward mild
Trial 1000: near-zero delta → reward absent
→ SAME stimulus, DIFFERENT delta = DIFFERENT Precondition-3 outcome
→ This is prediction-delta erosion, NOT value change
```

🟢 Research: Frederick & Loewenstein 1999 — hedonic adaptation comprehensive review.
Brickman & Campbell 1971 — hedonic treadmill concept.

---

## §5 — Precondition-4: Match-Range

### §5.1 — Definition

🟡 **Precondition-4 — Match-Range**:

> Match between incoming pattern and gap direction must fall within
> a **suitable range** — not too alien, not too familiar.
>
> Precondition-4 answers: "Does the match FIT?" — quality of fit, not just detection.
> Precondition-3 detects THAT something changed. Precondition-4 evaluates HOW WELL it fits.

**Old name**: "Goldilocks Zone Position" (drill 03-Reward.md §3.5)
**Changed because**: (a) "Zone" missed the direction-match component. (b) "40-70%" is not fixed → "Range" = dynamic.
**Informal shorthand**: "Goldilocks zone" — used across framework as intuitive label for this precondition.

### §5.2 — Direction-match (not just magnitude)

🟡 From Gap-Direction.md v2.0 §6.3:

> Match AGAINST WHAT? → Match against **gap direction**.
>
> Gap has direction = f(surrounding chunks).
> Precondition-4 evaluates: stimulus match DIRECTION + MAGNITUDE of gap.

```
Direction-match matters:

  ① Correct direction + correct range → reward (full match)
  ② Correct direction + outside range → attenuated (too close or too far)
  ③ Wrong direction + any range → no reward (direction mismatch)

Example:
  Musician searching for a sad melody (gap direction = melancholy)
  → Receives a sufficiently novel sad melody → reward ✅ (direction + range match)
  → Receives a cheerful melody → no reward ❌ (direction mismatch)
  → Receives a sad melody that's too complex → confusion ❌ (range miss)
```

### §5.3 — Goldilocks zone (dynamic, not a fixed number)

🟡 From Reward-Calibration.md v1.1 §1.2:

> **Goldilocks zone**: novel enough to trigger + right direction to match gap.
> Dynamic per person / context / gap-type / time.
> The often-cited "40-70% match ratio" is a **rough approximation**, not a fixed threshold.
> Zone changes along 4 axes:

```
① PER-PERSON:
  COMT Val/Val → needs more shallow rewards → zone wide
  COMT Met/Met → needs fewer deep rewards → zone narrow
  DRD4-7R → higher threshold → zone shifted toward MORE novel
  (PFC-Hardware §3.4)

② PER-GAP-TYPE:
  Chunk-Shift → small delta sufficient → zone wide
  Chunk-Miss → moderate delta → zone moderate
  Chunk-Gap → larger delta needed → zone narrow
  (Body-Feedback-Mechanism.md §3)

③ PER-CONTEXT:
  Cortisol state: high → zone narrows (threat mode)
  Existing chunks: many → zone narrow (expert) vs few → zone wide (novice)
  Relationship: trusted source → zone wider (trust compile)
  Background pattern: stable → zone sensitive to small changes

④ PER-TIME:
  Baseline shift from repeated reward → zone shifts
  Developmental stage: child = wide zone, adult = narrower
  Habituation: trial 1 vs trial 100 = completely different zone
```

**Conclusion** (Reward-Calibration.md):
> "There is NO formula 'give X reward for gap Y' — only OBSERVE + ADJUST continuously."

### §5.4 — Expertise shift (E₀ → E₃)

🟡 Zone changes with expertise level:

```
E₀ (Zero exposure):
  → No chunks → Precondition-2 fails before Precondition-4 is reached
  → Zone question irrelevant

E₁ (Beginner):
  → Few chunks → zone WIDE (many things are "new + just enough to match")
  → Easy to reward, but quality is low
  → Example: just learning guitar, can play 1 chord → reward!

E₂ (Intermediate):
  → Many chunks → zone NARROWS (needs more sophistication to be "novel enough")
  → Reward harder to trigger, but quality is higher
  → Example: 5 years playing guitar, needs new technique to find it "interesting"

E₃ (Expert):
  → Deep rich chunks → zone VERY NARROW + SHIFTED
  → Only subtle, refined differences trigger reward
  → BUT when triggered → very deep reward (rich chunk network activated)
  → Example: 30-year artist, only delicate nuance produces "wow"

Pattern: expertise NARROWS zone + SHIFTS toward subtlety
  → SAME stimulus: beginner rewards, expert bored (or vice versa)
  → Van Gogh: beginner = Precondition-2 fail, art student = Precondition-4 zone match, expert = Precondition-4 too familiar
```

🟢 Research: Training gradient in music appreciation (North & Hargreaves 1995).
Zajonc 1968 mere exposure — preference peaks then declines with overexposure.
Berlyne 1960 — inverted-U arousal × complexity.

### §5.5 — Failure asymmetry: reward vs dissonance

🟡 Precondition-4 failure differs for reward and dissonance:

```
REWARD Precondition-4 failure:
  Too alien → confusion (Precondition-2 boundary)
  Too familiar → boredom (habituation)
  Direction mismatch → indifference

DISSONANCE Precondition-4 "failure" (i.e., dissonance does NOT fire):
  Too alien → actually MAY still fire dissonance (threat response)
  Too familiar → dissonance attenuated (habituated mismatch accepted)
  → Asymmetry: alien stimuli → reward BLOCKED but dissonance ENHANCED

⚠️ Dissonance has LOWER threshold than reward:
  → Threat detection favors false positives (evolutionary advantage)
  → → Precondition-4 zone for dissonance is WIDER than for reward
  → → Easier to trigger dissonance than reward from same mismatch
  → Details: Dissonance-Signal-Architecture.md, §9 this file
```

### §5.6 — Precondition-4 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Too alien | Match < lower bound → cannot evaluate | "Too strange, can't understand" |
| Too familiar | Match > upper bound → habituated | "Too familiar, nothing new" |
| Direction mismatch | Stimulus matches wrong gap direction | "Not what I'm looking for" |
| Zone shifted | Expertise/context changed zone → stimulus no longer fits | "Used to be captivating, now boring" |

---

## §6 — Precondition-5: Compile-Gate

### §6.1 — Definition

🟡 **Precondition-5 — Compile-Gate**:

> Chunks being activated must have **NET link pattern** (sum of Type 1 emotional
> links, 7-factor strength) that permits signal to fire in the expected direction.
> Link pattern compiled at formation time persists through retrieval and
> determines signal DIRECTION + QUALITY.
>
> Precondition-5 answers: "Does the NET link pattern PERMIT it?" — direction gate, not substrate check.

**Old name**: "Chunk Association Tag" (drill 03-Reward.md §3.6)
**Changed because**: (a) "Association Tag" implies binary — actual mechanism = NET of Type 1 links.
(b) "Compile-Gate" emphasizes: link pattern compiled at formation → gate determines direction.
(c) v1.1: "tag" → "NET link pattern" aligned with Drill v4.0 §4 (observation parameter model).

### §6.2 — Scope: Evaluative ONLY

```
⭐ Precondition-5 applies ONLY to EVALUATIVE reward/dissonance.

EVALUATIVE:
  → Precondition-5 REQUIRED — chunks' NET link pattern determines signal direction
  → Positive-dominant NET → opioid pathway → genuine reward
  → Negative-dominant NET → cortisol pathway → discomfort despite understanding
  → Quality ceiling depends on NET link pattern (§6.4)

DIRECT-STATE:
  → Precondition-5 = N/A — hardware signals, no compiled link pattern needed
  → CT afferents fire opioid directly (no compiled links)
  → Taste buds signal directly (sweet → approach, bitter → avoid)
  → Hardware pathways = hardwired, not compiled
  → Details: Reward-Signal-Architecture §1.3

⚠️ Precondition-5 = N/A is the ONLY precondition completely absent in Direct-State.
  (Precondition-3 is "uncertain", others are "simplified" — Precondition-5 is clean N/A.)
```

### §6.3 — Direction-At-Compile gate model

🟡 From Cortisol-Baseline.md v2.4 §3.3 — NET link pattern is NOT binary but a **gradient**:

> At compile time: cortisol AMPLIFIES link formation in the direction
> determined by body state. No binary tag at neural level.
> Key insight: "cortisol amplifies DIRECTION — direction matters more than level."

```
⭐ 'Direction-At-Compile' = OBSERVATION PARAMETER (Drill v4.0 §4):
  No binary tag at neural level. Direction = NET of all Type 1 links
  (7-factor strength) at compile. "Approach" = positive links dominate NET.
  "Avoidance" = negative links dominate NET. Link pattern CAN shift
  via competitive re-linking (Chunk.md v3.1 §4.3).

4-Threshold Gradient (Cortisol-Baseline.md v2.4 §3.3):

  ┌───────────┬──────────────────┬───────────────────────────────────┐
  │ Threshold │ threat:novelty   │ NET link outcome                  │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Light     │ ~60:40           │ Mild cortisol + opioid anticipation│
  │           │                  │ NET: mildly positive               │
  │           │                  │ Easy to shift later                │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Moderate  │ ~80:20           │ Moderate cortisol, little opioid   │
  │           │                  │ NET: moderately negative           │
  │           │                  │ Shift needs time                   │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Heavy     │ ~95:5            │ Strong cortisol, deep fear compiled│
  │           │                  │ NET: strongly negative             │
  │           │                  │ Extremely hard to shift            │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Extreme   │ Trauma           │ Body refuses to use chunk          │
  │           │                  │ NET: overwhelmingly negative       │
  │           │                  │ Avoidance = only possible response │
  └───────────┴──────────────────┴───────────────────────────────────┘

⭐ SAME cortisol level, DIFFERENT source:
  Novelty cortisol (curious but tense) → positive links dominate → approach OBSERVED
  Threat cortisol (afraid) → negative links dominate → avoidance OBSERVED
  → SOURCE > LEVEL (Cortisol-Baseline.md v2.4 §7)
```

### §6.4 — 4-Pathway × quality ceiling

🟡 From Compile-Taxonomy.md v3.0 §6:

> Each compile pathway creates a DIFFERENT Precondition-5 NET pattern → determines reward capacity:

```
┌──────────────────────┬───────────────────────┬────────────────────────────┐
│ Pathway              │ Precondition-5 NET    │ Reward ceiling             │
│                      │ Pattern               │                            │
├──────────────────────┼───────────────────────┼────────────────────────────┤
│ ① Hardware Fit       │ Positive-dominant     │ HIGHEST — natural coherence│
│   (direct experience │                       │ Flow accessible            │
│    in Goldilocks)    │                       │ Sustainable engagement     │
├──────────────────────┼───────────────────────┼────────────────────────────┤
│ ② Trust + Moderate   │ Moderate positive     │ MODERATE — depends on      │
│   (trusted source +  │                       │ collective chain quality   │
│    partial verify)   │                       │ Can upgrade with experience│
├──────────────────────┼───────────────────────┼────────────────────────────┤
│ ③ Social Default     │ Mixed/neutral         │ LOW — relief dominant      │
│   (consensus,        │                       │ "Done" > "Interesting"     │
│    "everyone does it")│                      │ PFC confabulation ~30%     │
├──────────────────────┼───────────────────────┼────────────────────────────┤
│ ④ Threat Avoidance   │ Negative-dominant     │ LOWEST — relief ONLY       │
│   (fear-driven       │                       │ Never genuine engagement   │
│    compliance)       │                       │ Burnout trajectory         │
└──────────────────────┴───────────────────────┴────────────────────────────┘

⭐ Precondition-5 NET pattern at childhood compile → PERSISTS → constrains ADULT reward profile.
  "Skilled but resentful" = Precondition-5 fail (understand but negative-dominant NET).
  Pathway ④ = why many people "succeed but aren't happy."
```

### §6.5 — Re-association 3 paths

🟡 Precondition-5 NET pattern CAN shift, but requires resources (Cortisol-Baseline.md v2.4 §7.6):

```
3 Re-association Paths (= add competing links → shift NET):

  Path 1: NEW POSITIVE CONTEXT (months → years)
    → Same domain, new positive experiences
    → Add competing positive links → gradually shift NET toward approach
    → Slowest but most robust
    → Example: math-phobic adult finds a good teacher → years → "math is ok"

  Path 2: NOVELTY HIJACK (weeks → months)
    → Completely new angle/context for same domain
    → Bypass old chunks → build new positive-linked chunks
    → Old negative-linked chunks still exist BUT new chunks dominate
    → Example: learn math through music → new chunks, new positive links

  Path 3: AI SUPPORT (weeks — 🔴 hypothesis level)
    → AI provides perfectly calibrated Goldilocks stimuli
    → Consistent positive experiences accumulate faster
    → NET shift accelerated by controlled exposure
    → ⚠️ Hypothesis level — not yet validated

⭐ Key: re-association = ADD COMPETING LINKS, not deletion.
  Old negative-linked chunks still exist (no deletion mechanism).
  New positive-linked chunks added.
  Which set DOMINATES NET = f(recency, frequency, context).
```

### §6.6 — Precondition-5 ≠ Precondition-2 distinction (restated)

```
Summary distinction:

  Precondition-2 Chunk-Substrate:  CAN you decode? (existence of chunks)
  Precondition-5 Compile-Gate:     WHAT DIRECTION does decoded signal go? (NET link pattern on chunks)

  Precondition-2 fail: "I don't understand this problem" (no chunks to decode)
  Precondition-5 fail: "I understand this problem but hate math" (chunks exist, negative-dominant NET)

  Precondition-2 fix: LEARN (accumulate chunks) — education problem
  Precondition-5 fix: RE-LINK (add competing positive links → shift NET) — much harder, emotional rewiring

  Precondition-2 is about SUBSTRATE (does the foundation exist?)
  Precondition-5 is about DIRECTION (which way does the NET link pattern flow?)
```

### §6.7 — Precondition-5 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Threat-linked | Chunks compiled under fear → negative-dominant NET | "Dislike even though I know it's good" |
| Social-default | Chunks compiled via consensus → mixed/neutral NET | "Relieved when done, not engaged" |
| Mixed-NET | Some links positive + some negative → ambivalent NET | "Both attracted and afraid" |
| Trauma-linked | Extreme compile → overwhelmingly negative NET | "Can't even think about it" (avoidance) |

**Genius paradox** (03-Reward.md §3.6):
```
Newton/Tesla/Einstein: high baseline cortisol
  → BUT: learning-domain chunks compiled in CURIOSITY state
  → Threat source ≠ learning domain → Precondition-5 NET = positive-dominant in learning
  → Reward accessible in learning domain DESPITE high overall cortisol

Key: threat SOURCE matters, not threat LEVEL.
  → Person stressed about money can still enjoy music (different domain)
  → Person stressed about music cannot enjoy music (same domain)
  → Precondition-5 NET pattern is DOMAIN-SPECIFIC, not global
```

🟢 Research: Cortisol effects on learning are direction-dependent (Lupien et al. 2007).
Same cortisol level → enhanced OR impaired memory depending on context and timing.

---

## §7 — Conjunction Logic + Failure Mode Table

### §7.1 — AND-gate structure

🟡 **Core logic**: Signal fires if and only if Precondition-1 ∧ Precondition-2 ∧ Precondition-3 ∧ Precondition-4 ∧ Precondition-5.

> Preconditions operate as an AND-gate — missing ANY 1 → signal does not fire at full magnitude.
> NO precondition can compensate for another.
> Precondition-2 (chunks) does NOT offset Precondition-5 (NET pattern). Precondition-3 (delta) does NOT offset Precondition-1 (gap).

```
Full signal (reward or dissonance):
  Precondition-1 ✅ + Precondition-2 ✅ + Precondition-3 ✅ + Precondition-4 ✅ + Precondition-5 ✅ → FULL SIGNAL

Partial cases:
  4/5 met → signal ATTENUATED (reduced, not zero)
  3/5 met → signal WEAK (barely perceptible)
  2/5 met → signal ABSENT (no subjective experience)
  1/5 met → NOTHING

⚠️ "Attenuated" ≠ "absent":
  → Near-miss cases produce MILD signal ("almost captivating," "vaguely interesting")
  → Framework prediction: mild reward = 1 precondition BARELY failing
  → Clinical: chronic mild anhedonia = 1 precondition chronically weak
```

### §7.2 — Dependencies between preconditions

🟡 Preconditions are NOT flat — they have a dependency hierarchy (§1.4):

```
DEPENDENCY 1: Precondition-2 → Precondition-1 (schema-level)
  Precondition-2 (chunks) must exist BEFORE Precondition-1b (schema gap) can form.
  "Don't know it exists = no gap" → Precondition-2a fail = Precondition-1b impossible.
  ⚠️ Precondition-1a (hardware) does NOT need Precondition-2 → body-needs exist from birth.

DEPENDENCY 2: Precondition-3 → Precondition-4 (sequential)
  Precondition-3 (delta detected) must fire BEFORE Precondition-4 (match quality) is evaluated.
  Precondition-3 fail → PFC doesn't attend → Precondition-4 not checked → Precondition-4 irrelevant.
  ⚠️ Stimulus may be a PERFECT match (Precondition-4 would pass) but Precondition-3 blocks detection.

NO OTHER DEPENDENCIES:
  Precondition-5 independent of Precondition-3/Precondition-4 (link pattern compiled at formation, not at evaluation)
  Precondition-1 independent of Precondition-3 (gap exists before delta detection)
  Precondition-4 independent of Precondition-5 (match quality separate from NET link direction)
```

### §7.3 — Per-precondition failure → specific outcome

🟡 Each precondition failure produces a **distinct** subjective experience:

| Precondition-fail | Others met | Outcome | Typical phrase |
|---|---|---|---|
| Precondition-1 | Precondition-2–Precondition-5 ✅ | No desire → signal irrelevant | "No desire," "Have enough already" |
| Precondition-2 | Precondition-1, Precondition-3–Precondition-5 ✅ | Confusion → cannot evaluate | "Can't understand," "Too strange" |
| Precondition-3 | Precondition-1, Precondition-2, Precondition-4, Precondition-5 ✅ | Unnoticed → attention not triggered | "Normal," "Already used to it" |
| Precondition-4 | Precondition-1–Precondition-3, Precondition-5 ✅ | Wrong range → too alien or too familiar | "Too hard" / "Too easy" |
| Precondition-5 | Precondition-1–Precondition-4 ✅ | Wrong direction → aversion despite understanding | "Understand but dislike" |

**Diagnostic power**: Knowing WHICH precondition failed → knowing EXACTLY how to fix it.
- Precondition-1 fail → create/activate gap (education, exposure, need induction)
- Precondition-2 fail → build chunks (training, scaffolding, prerequisite learning)
- Precondition-3 fail → introduce variation (change context, angle, presentation)
- Precondition-4 fail → calibrate difficulty (simpler for too-alien, harder for too-familiar)
- Precondition-5 fail → add competing links → shift NET (new context, positive re-linking — §6.5)

### §7.4 — Chunk dynamics × preconditions

🟡 Body-Feedback-Mechanism.md §6.2 maps chunk dynamics (Shift/Miss/Gap) × Precondition-1–Precondition-5:

```
⭐ KEY INSIGHT: Chunk dynamics ≠ preconditions, but they INTERACT.

  Chunk-Shift:
    Precondition-1 = shift CREATES new pending (e.g. betrayal creates need to fix)
    Precondition-2 = needs chunks to evaluate new info
    Precondition-3 = shift = valence delta (inherent)
    Precondition-4 = shift occurs at ANY match level
    Precondition-5 = NEW link pattern from shift event

  Chunk-Miss:
    Precondition-1 = miss = body-need loses quality
    Precondition-2 = needs compiled baseline (no compile = no miss)
    Precondition-3 = miss = negative prediction error
    Precondition-4 = N/A (body already KNOWS — no Goldilocks needed)
    Precondition-5 = compiled baseline carries link pattern

  Chunk-Gap:
    Precondition-1 = gap = body-need lacks pattern
    Precondition-2 = needs enough chunk network to DETECT gap
    Precondition-3 = gap detect = ACC signal
    Precondition-4 = gap must be detectable (not too alien)
    Precondition-5 = surrounding compiled chunks carry link pattern

  → Details: Body-Feedback-Mechanism.md §6.2

⚠️ Compound dynamics = Precondition-1–Precondition-5 checked MULTIPLE TIMES per event.
  Example: scammed by a close friend → Shift (betrayal) + Miss (trust lost) + Gap (how to fix?)
  → Each dynamic triggers its own Precondition-1–Precondition-5 check → compound signal
```

### §7.5 — Multi-precondition failure combinations

🟡 When MULTIPLE preconditions fail simultaneously:

```
Precondition-1 + Precondition-3 co-fail:
  No gap + no delta → COMPLETE INDIFFERENCE
  → Example: scrolling social media while satiated — nothing registers

Precondition-1 + Precondition-4 co-fail:
  Gap exists but nothing matches → BOREDOM (Boredom.md §7)
  → Body WANTS (Precondition-1) but nothing FITS (Precondition-4) + signal too diffuse
  → ⚠️ Boredom = Precondition-1 met + Precondition-4 fail, NOT simple Precondition-3 fail

Precondition-2 + Precondition-4 co-fail:
  Insufficient chunks + wrong range → OVERWHELM
  → Example: advanced lecture to a complete beginner

Precondition-3 + Precondition-5 co-fail:
  No delta + negative NET → STAGNANT AVERSION
  → Example: math-phobic person forced to do math daily
  → Habituated (Precondition-3 fail) + avoidance-tagged (Precondition-5 fail) → chronic low-grade suffering

Precondition-1 + Precondition-2 + Precondition-3 co-fail:
  No gap + no chunks + no delta → EMPTINESS
  → Nothing wanted, nothing understood, nothing new → existential boredom
  → "Don't want, don't enjoy, don't know what's wanted"
```

---

## §8 — Developmental Arc

### §8.1 — Infant (0-2 years)

🟡 Infant precondition profile:

```
Precondition-1: ✅ Precondition-1a AVAILABLE from birth (body-needs: hunger, warmth, social contact)
    ❌ Precondition-1b NOT YET (schema gaps require chunks that don't exist yet)
    → Infant reward = almost entirely Direct-State

Precondition-2: ⚠️ THE BOTTLENECK — near-zero chunks at birth
    → Most stimuli = Precondition-2b fail → "everything is strange"
    → Chunks compile rapidly via 4+1 channels:
      Direct experience, emotional peak, multi-modal, sleep consolidation,
      external installation (caregiver)
    → Precondition-2 is PRIMARY developmental axis in infancy

Precondition-3: ✅ PRESENT but unfocused
    → Everything is novel → delta continuously high
    → BUT: so many deltas → threshold competition → attention scattered
    → Orienting response (Sokolov 1963) = Precondition-3 in its most basic form 🟢

Precondition-4: ⚠️ NARROW — few existing chunks = most inputs outside match range
    → Wide zone in theory, but few chunks to match WITH
    → Simple stimuli (faces, voices, rhythms) fit → reward accessible
    → Complex stimuli → Precondition-2 fail before Precondition-4 reached

Precondition-5: ⚠️ ENTIRELY DEPENDENT ON CAREGIVING
    → Link patterns form via social referencing + caregiver emotional state
    → Caregiver curious while exposing → positive links dominate
    → Caregiver anxious while exposing → negative links dominate
    → ⭐ Precondition-5 in infancy = CAREGIVER responsibility, not child's
```

🟢 Research: Social referencing (Sorce et al. 1985) — infants use caregiver
facial expressions to associate novel stimuli with approach/avoidance links.

### §8.2 — Child (2-12 years)

🟡 Chunk accumulation + link pattern compilation phase:

```
Precondition-1: Precondition-1b DEVELOPING — schema gaps form as chunk network grows
    → "Wanting to know why" (curiosity gaps) emerge ~age 3-4
    → Social gaps (acceptance, status) emerge ~age 5-7
    → Direction becomes more specific with experience

Precondition-2: RAPID EXPANSION
    → Chunks compile via experience + education + social learning
    → Domain-specific: rich chunks in play/social, fewer in academic (initially)
    → Precondition-2 bottleneck loosens → more stimuli decodable → more rewards accessible

Precondition-3: FUNCTIONAL — novelty detection well-established
    → BUT: attention systems still developing (PFC immature)
    → High DRD4 expression in childhood → lower threshold → MORE novelty-seeking
    → → Children NEED more stimulation (not "hyperactive" — developmentally normal)

Precondition-4: WIDE ZONE — relatively few chunks → large range of stimuli feel "new enough"
    → Easy to reward → exploration phase
    → Zone gradually narrows with expertise accumulation

Precondition-5: ⭐ CRITICAL PERIOD — link patterns compiling from emotional context
    → Same content taught under curiosity vs fear → OPPOSITE lifelong trajectories
    → Compile-Taxonomy.md: 4 pathways (HwFit/Trust/Social/Threat)
    → Childhood Precondition-5 link patterns PERSIST into adulthood and constrain adult reward
    → ⚠️ "Education is Precondition-5 programming" — emotional context matters as much as content
```

### §8.3 — Adult (12+ years)

🟡 Full operational profile:

```
Precondition-1: FULL RANGE — both Precondition-1a (hardware) and Precondition-1b (schema) operational
    → Complex gap landscapes: career, relationship, identity, meaning
    → Direction highly specific in expert domains

Precondition-2: DOMAIN-DIFFERENTIATED
    → Rich chunks in familiar domains → Precondition-2 non-issue
    → Sparse chunks in unfamiliar domains → Precondition-2 fail still possible
    → Expert vs novice = SAME stimulus, DIFFERENT Precondition-2 outcome

Precondition-3: HABITUATION becomes primary challenge
    → Daily routine → delta erosion → reward fades despite objective quality
    → Hedonic adaptation: same job, same relationship → Precondition-3 erodes
    → Counter: deliberate variation, new challenges, travel

Precondition-4: NARROWED + SHIFTED by expertise
    → Expert zone narrow → only subtle refinements trigger reward
    → Beginner zone in new domains → wide → easy rewards
    → Cross-domain exploration = Precondition-4 reset strategy

Precondition-5: ACCUMULATED BIOGRAPHICAL LINK PATTERNS
    → Childhood compilations persist: "skilled but resentful" patterns established
    → NET shift possible but costly (months-years, §6.5)
    → Professional competence ≠ enjoyment (Precondition-5 fail common in adults)
    → "Burnout" often = Precondition-3 (no delta) + Precondition-5 (negative link accumulation)
```

### §8.4 — Aging + burnout

🟡 Erosion patterns:

```
Precondition-1: WEAKENS — body-needs reduce (lower drive baseline)
    → Curiosity gaps may narrow (fewer active schemas)
    → Social gaps may intensify OR diminish (isolation vs acceptance)

Precondition-2: DOMAIN DECAY — chunks in neglected areas atrophy
    → "Schema portfolio neglect" (04-Integration.md §5.5)
    → Work chunks hypertrophy, hobby/relationship chunks decay
    → Rebuilding decayed chunks takes months-to-years

Precondition-3: ERODES — long-term habituation + reduced VTA sensitivity
    → Same environment for decades → deep habituation
    → Neurobiological: VTA dopamine function declines with age 🟢
    → Counter: novel experiences, learning new skills, travel

Precondition-4: CAN RE-WIDEN — if person enters new domain
    → Retirement + new hobby → beginner zone → Precondition-4 wide → rewards accessible again
    → "Second wind" phenomenon = Precondition-4 reset in new domain

Precondition-5: CORTISOL ACCUMULATION — life stress compounds negative links
    → Chronic work stress → work chunks accumulate negative-dominant NET
    → "Competent but aversive" = burnout hallmark
    → Late-life NET shift harder but possible (Path 1 slow positive re-linking)

BURNOUT FORMULA (compound):
  Precondition-3 erosion (habituated) + Precondition-5 avoidance (stress-tagged) + Precondition-1 weak (gap unclear)
  → "Don't want, don't enjoy, don't know what's wanted" = triple precondition failure
```

🟢 Research: Dopamine system aging (Bäckman et al. 2006).
Burnout and reward system (Sokka et al. 2017 — reduced reward anticipation in burnout).

---

## §9 — Dissonance Application

### §9.1 — Precondition-1–Precondition-5 apply to dissonance, not just reward

🟡 The precondition model is a **body-feedback** model, not just a reward model:

> Body-feedback signal = reward OR dissonance.
> Precondition-1–Precondition-5 determine whether the signal fires — for BOTH directions.
> But preconditions operate DIFFERENTLY for dissonance vs reward.

```
REWARD firing: Precondition-1–Precondition-5 all met → opioid pathway → approach signal
DISSONANCE firing: Precondition-1–Precondition-5 met but in NEGATIVE direction → cortisol pathway → avoidance signal

Key difference: DIRECTION of match, not presence of preconditions.
  Precondition-1: gap exists (same for both — need drives signal)
  Precondition-2: chunks exist to decode (same — substrate required)
  Precondition-3: delta detected (same — change needed)
  Precondition-4: match is NEGATIVE direction → dissonance fires
  Precondition-5: NET link pattern determines signal QUALITY (not just direction)
```

### §9.2 — Precondition-5 inverted: negative-NET × dissonance

🟡 Precondition-5 works INVERSELY for dissonance compared to reward:

```
REWARD:
  Positive-dominant NET → opioid → full reward (ceiling HIGH)
  Negative-dominant NET → blocked → reward limited (ceiling LOW)

DISSONANCE:
  Negative-dominant NET → cortisol AMPLIFIED → dissonance threshold LOWER
  Positive-dominant NET → cortisol DAMPENED → dissonance threshold HIGHER

→ Negative-linked chunks make dissonance EASIER to fire, not harder.
→ Same mismatch: positive-dominant domain → mild dissonance
                  negative-dominant domain → intense dissonance

Example:
  Musician (positive-dominant NET) makes mistake → mild dissonance, quickly resolved
  Math-phobic adult (negative-dominant NET) makes math error → intense dissonance, slow to resolve
  → SAME type of error, DIFFERENT Precondition-5 NET pattern → DIFFERENT dissonance intensity
```

### §9.3 — Asymmetric transition speed

🟡 From Dissonance-Signal-Architecture §7.5 — reward → dissonance vs dissonance → reward:

```
REWARD → DISSONANCE: FAST
  → Amygdala ~12ms bypasses PFC
  → Opioid off in seconds
  → Threat detection = survival priority
  → Example: enjoying music → sudden loud noise → instant dissonance

DISSONANCE → REWARD: SLOW
  → Cortisol half-life ~60-90 minutes
  → Opioid RE-activation requires FULL H10 re-check (all 5 preconditions)
  → PFC must re-assess safety before releasing opioid gate
  → Example: stressful exam → relief → takes minutes-hours, not seconds

⭐ Asymmetry resides in EVALUATIVE layer specifically.
  Direct-State is relatively symmetric (pain stops → relief fast).
  Evaluative adds "precondition re-verification" delay.
```

🟢 Research: Negativity bias (Baumeister et al. 2001, Rozin & Royzman 2001).
Loss aversion (Kahneman & Tversky 1979) — losses loom ~2× larger than gains.
Evolutionary logic: missing threat = death (max cost), false alarm = low cost.

### §9.4 — Evaluative gates

🟡 From Dissonance-Signal-Architecture §3 — evaluative layer GATES direct-state dissonance:

```
Evaluative gates can:
  ① AMPLIFY — nocebo effect (expecting pain → more pain)
  ② SUPPRESS — placebo effect (expecting relief → less pain)
  ③ ABSENT — infant/dissociation (no evaluative layer active)
  ④ CONFLICT — "pain from a loved one" (mismatch between signal directions)

→ Precondition-1–Precondition-5 for dissonance: evaluative gates modulate INTENSITY, not just presence.
→ Same physical stimulus: different evaluative context → different dissonance level.
→ Mechanism details: Dissonance-Signal-Architecture.md §3
```

🟢 Research: Placebo analgesia (Wager et al. 2004). Nocebo hyperalgesia (Zubieta et al. 2005).
Craig 2002/2009 — insula gradient model for interoception.

---

## §10 — Honest Assessment

### §10.1 — Confidence per precondition

| # | Precondition | Confidence | Basis |
|---|---|---|---|
| Precondition-1 | Directed-Gap | 🟢 HIGH | Satiety/motivation research extensive. Alliesthesia. |
| Precondition-2 | Chunk-Substrate | 🟢 HIGH | Expertise/training studies. Chi et al. 1981. Art appreciation. |
| Precondition-3 | Delta-Gate | 🟢 HIGH | VTA prediction error well-established. Schultz 1997. |
| Precondition-4 | Match-Range | 🟡 MODERATE | Inverted-U supported (Berlyne 1960). Dynamic zone = framework claim. |
| Precondition-5 | Compile-Gate | 🟡 MODERATE | Cortisol × learning direction-dependent 🟢. 4-pathway model = framework. |
| ALL | Conjunction | 🟡 MODERATE | Each Precondition individual 🟢, but "ALL 5 required" = framework-level claim. |

### §10.2 — Open questions

```
Q1: Precondition-3 × Precondition-4 interaction boundary
  When Precondition-3 (delta) is very large, can Precondition-4 (match) be bypassed?
  Example: extreme surprise → reward regardless of match quality?
  → Current: framework says NO (Precondition-4 still required)
  → But: extreme delta cases not yet studied rigorously

Q2: Precondition-5 re-association speed
  Path 3 (AI support) accelerates re-association — to what degree?
  → Hypothesis level (🔴). No empirical validation yet.
  → If AI CAN accelerate → massive educational implications

Q3: Direct-State Precondition-3 mechanism
  Does Direct-State bypass VTA entirely or use different threshold?
  → Reward-Signal-Architecture §1.3 marks Precondition-3 as "UNCERTAIN" for Direct-State
  → Posterior insula pathway hypothesized but not fully mapped

Q4: Dissonance precondition thresholds
  Are dissonance Precondition-1–Precondition-5 thresholds LOWER than reward Precondition-1–Precondition-5?
  → Evolutionarily predicted (negativity bias)
  → But: quantitative threshold comparison not available

Q5: Compound dynamics × precondition cycling
  When compound event triggers Shift + Miss + Gap simultaneously,
  do preconditions get checked 3× independently? Or integrated?
  → Body-Feedback-Mechanism §6.2 suggests independent, but mechanism unclear
```

### §10.3 — Falsifiable predictions

🟡 If Body-Feedback Precondition model is correct:

```
PREDICTION 1: "Should reward but doesn't" cases
  → ALWAYS traceable to specific Precondition-failure
  → If ANY case found where ALL 5 met but NO reward → model falsified

PREDICTION 2: Precondition-5 re-association observable
  → Person with avoidance-tagged domain + positive re-exposure
  → Should show gradual NET shift → measurable via fMRI/EEG

PREDICTION 3: Precondition-2a genesis testable
  → Expose subject to completely novel domain → measure desire BEFORE vs AFTER
  → Before chunks: no desire. After chunks: desire possible.
  → Gap formation should correlate with chunk accumulation

PREDICTION 4: Precondition-3 → Precondition-4 sequential
  → Subliminal stimulus (below Precondition-3 threshold) that would match Precondition-4
  → Should produce NO reward (Precondition-3 blocks before Precondition-4 evaluated)
  → Testable with masked priming paradigms

PREDICTION 5: Developmental Precondition-5 testable
  → Same content taught under curiosity vs fear conditions
  → Approach/avoidance tags should persist → measurable years later
  → Partially supported by education research 🟢
```

---

## §11 — Cross-References

### §11.1 — Primary sources (drill origin)

| File | Relevant section | Relationship |
|---|---|---|
| 03-Reward.md v1.1 | §3 H10 Core | DRILL ORIGIN — this file formalizes §3 |
| 04-Integration.md | §9 H10 refined | DRILL INTEGRATION — cross-validated cases |

### §11.2 — Sibling files (Body-Feedback system)

| File | Relevant section | What it covers (this file cross-refs) |
|---|---|---|
| Body-Feedback.md v2.0 | §5.2 | H10 summary table (48 lines, pointer to this file) |
| Body-Feedback-Mechanism.md v2.1 | §6.2 | Chunk dynamics × Precondition-1–Precondition-5 mapping (§7.4) |
| Body-Feedback-Label.md v2.1 | — | Vocabulary reference (terminology) |
| Reward-Signal-Architecture.md v2.1 | §1.3 | Evaluative/Direct-State × Precondition-1–Precondition-5 table (§1.2) |
| Dissonance-Signal-Architecture.md v1.0 | §3, §7.5 | Evaluative gates + asymmetric transition (§9) |

### §11.3 — Refinement sources

| File | Relevant section | What refined |
|---|---|---|
| Gap-Direction.md v2.0 | §3, §6.3 | Precondition-1 direction + "don't know it exists = no gap" + hierarchy |
| Cortisol-Baseline.md v2.4 | §3.3, §7, §7.7 | Precondition-5 Direction-At-Compile gradient + source > level + 5 roles |
| Compile-Taxonomy.md v3.0 | §6 | Precondition-5 4-pathway × quality ceiling |
| Reward-Calibration.md v1.1 | §1.2 | Precondition-4 Goldilocks zone (dynamic, not fixed number) |
| Boredom.md v2.1 | §1, §7 | Precondition-3 boredom disambiguation |
| Chunk.md v3.1 | §2.4, §2.6, §4.2 | Precondition-2 substrate + context-tag + Direction-At-Compile + 7-factor links |

### §11.4 — Developmental sources

| File | Relevant section | What informed |
|---|---|---|
| Child-Development-Mechanism.md | §2.3 | Infant precondition profile (§8.1) |
| 04-Integration.md | §5.5, §5.6, §7 | Aging + burnout erosion (§8.4) |

### §11.5 — Precondition name mapping (from drill)

```
┌──────────────────────────────┬──────────────────────────────────┐
│ Drill name (H10)             │ Formal name (this file)          │
├──────────────────────────────┼──────────────────────────────────┤
│ Schema Pending Status        │ Precondition-1 Directed-Gap      │
│ Chunks Base Adequacy         │ Precondition-2 Chunk-Substrate   │
│ Prediction-Delta Threshold   │ Precondition-3 Delta-Gate        │
│ Goldilocks Zone Position     │ Precondition-4 Match-Range       │
│ Chunk Association Tag        │ Precondition-5 Compile-Gate      │
└──────────────────────────────┴──────────────────────────────────┘
```
