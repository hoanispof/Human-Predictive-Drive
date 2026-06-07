---
title: Gap Direction — Body-Feedback Requires Directional Match
version: 2.0
created: 2026-04-27
rewritten: 2026-05-17 (v2.0 — FULL REWRITE: +By-product match connection, +2-Stream, +Compilable Architecture, +Compiled/Fresh note, +Inter-Body cross-refs, +Label v2.0 vocabulary)
status: v2.0 COMPLETE
scope: |
  CORE MECHANISM FILE: Gaps in the chunk network have SPECIFIC DIRECTION.
  Gap direction = f(surrounding chunk network structure).
  Reward/dissonance does NOT depend only on prediction error (Schultz 1997)
  — it also requires DIRECTION MATCH: stimulus must match the gap's specific direction.
  "Not knowing = no gap" = foundational principle.
  Unified model: Tier 1-4 chunks share the same substrate, differ in depth/origin.
  2-layer model: signal mechanism (Layer 1) × direction content (Layer 2).
  v2.0: Gap direction = WHY by-product match works (Inter-Body connection).
  v2.0: 2-Stream × gap direction. Compilable Architecture × gap direction.
  v2.0: Compiled/Fresh evaluation processing.
purpose: |
  Body-Feedback-Mechanism.md §3.3 defines Chunk-Gap:
    "Structure predicts C should exist → C not yet compiled → HOLE"
  But §3.3 does NOT yet formalize: C has a SPECIFIC SHAPE.
  This file formalizes:
  ① Gap direction = necessary consequence of "gap = hole in chunk network"
  ② "Not knowing = no gap" = genesis principle (distinct from Precondition-2 Chunk-Substrate diagnosis)
  ③ Reward = direction match quality (not merely "fill gap or not")
  ④ 2-layer model clarifies why Schultz 1997 is "correct but insufficient"
  ⑤ Gap direction install, Background-Pattern constraint, implications
  ⑥ v2.0: Gap direction = THE MECHANISM underneath by-product match
     (Inter-Body-Mechanism.md §5.4 — B's output matches A's gap DIRECTION)
dependencies:
  - Body-Feedback-Mechanism.md v2.0 — §3.3 Chunk-Gap definition, Shift/Miss/Gap, §1 Body-Need aggregate
  - Body-Feedback.md v2.0 — 5 Body-Feedback-Preconditions, dual-pull
  - Body-Feedback-Label.md v2.0 — vocabulary consistency, §2 Foundation terms
  - Inter-Body-Mechanism.md v1.0 — §2 Body-Need direction, §5 by-product match, §5.3 Full Chain
  - By-Product-Gap-Resonance.md v1.0 — §2 2-Stream Architecture, §1.5 by-product match
  - 03-Reward.md — Car Paradox C2.1-C2.5, Van Gogh gradient, Body-Feedback-Precondition cases
  - Chunk.md v2.0 — chunk substrate, compile, activation dynamics
  - Background-Pattern.md v1.0 — Background-Pattern bias gap direction landscape
  - Novelty.md v1.0 — Chunk-Gap = novelty foundation
  - Schema.md v2.0 — observation parameter, §4 depth, §8 body baseline
  - Cortisol-Baseline.md v2.0 — amplifier, direction tag, novelty vs threat
  - Imagine-Final.md — preview mechanism, Gap→Miss transition
  - Connection.md v3.3 — giving reward, Self-Pattern-Modeling-mediated, altruism
  - Gratitude.md v1.0 — Body-Feedback-Precondition applied to gifts, gap pre-requisite
  - Self-Pattern-Modeling v3.0 — Compiled/Fresh processing (Modeling-Stream mechanism)
  - Body-Base.md v3.1 — Compilable Architecture (3 foundations)
source_version: Vietnamese v2.0 (COMPLETE)
english_created: 2026-06-05
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Gap Direction — Body-Feedback Requires Directional Match

> **Father buys the most fashionable car popular with young people → intensely pleasant.**
> **Father buys a rocket (a thousand times more expensive) → confused.**
> **Father buys a vintage car (more expensive, father prefers it) → dislike.**
>
> **Same "father bought it." Same "expensive." Same "vehicle."**
> **But reward ONLY fires when stimulus MATCHES a SPECIFIC DIRECTION.**
>
> **E=mc² presented to Einstein → intensely pleasant.**
> **E=mc² presented to a student → "oh, interesting" but no body-level response.**
> **Same information. Same "objective value." Completely DIFFERENT reward.**
>
> **Why?**
>
> **Because gaps in the chunk network have DIRECTION.**
> **Direction = f(surrounding chunk network structure).**
> **No surrounding chunks = no walls = no hole = NO GAP.**
> **"Not knowing = no gap" = you CANNOT be missing something you don't know exists.**
>
> **Prediction error (Schultz 1997) = the DETECTION mechanism (something is different).**
> **Gap direction = the CONTENT of what is predicted (WHAT specifically is different).**
> **BOTH are needed to explain why reward is PERSONAL.**
>
> **v2.0: Gap direction = WHY by-product match works.**
> **B fills B's gap → output → matches A's gap DIRECTION → A rewards.**
> **Direction mismatch = output useless DESPITE being "good" by objective measure.**
>
> **This file: WHAT gap direction IS, WHY it is inevitable,**
> **HOW "not knowing = no gap" works,**
> **WHY this is the key to understanding the reward mechanism,**
> **and v2.0: WHY this is the foundation for inter-body by-product match.**

---

## Table of Contents

- §0 — WHY FORMALIZING GAP DIRECTION IS NEEDED
- §1 — DEFINITION
- §2 — PROOF: WHY GAPS MUST HAVE DIRECTION
- §3 — "NOT KNOWING = NO GAP" (Foundational Principle)
- §4 — 4 PROPERTIES OF GAP DIRECTION
- §5 — UNIFIED DIRECTION MODEL (Tier 1-4)
- §6 — 2-LAYER MODEL: SIGNAL MECHANISM vs DIRECTION CONTENT
- §7 — GAP DIRECTION FORMATION
- §8 — GAP DIRECTION × EXTERNAL INSTALL
- §9 — GAP DIRECTION × BACKGROUND PATTERN
- §10 — ABSTRACT ACTIVITY × BODY-BASE
- §11 — EXAMPLES
- §12 — GAP DIRECTION × INTER-BODY: BY-PRODUCT MATCH + 2-STREAM (★ NEW v2.0)
- §13 — IMPLICATIONS
- §14 — OPEN QUESTIONS
- §15 — HONEST ASSESSMENT
- §16 — CROSS-REFERENCES

---

## §0 — WHY FORMALIZING GAP DIRECTION IS NEEDED

### §0.1 — What the framework already has

```
BODY-FEEDBACK-MECHANISM.MD §3.3 (Chunk-Gap):

  "Structure predicts: if A and B are correct then C must exist"
  "C not yet compiled → HOLE in the network"
  "ACC detects inconsistency → body signal of restless unease"

  → Definition is CORRECT. Gap = hole where network predicts something.
  → §3.3 says "C should exist" — but DOES NOT ask: what does C look like?
  → NOT yet formalized: C has a SPECIFIC SHAPE determined by A, B, and the network


5 BODY-FEEDBACK-PRECONDITIONS (Body-Feedback.md §6):

  Precondition-1 Directed-Gap (body-need gap open)
  Precondition-2 Chunk-Substrate (sufficient substrate to decode)
  Precondition-3 Delta-Gate (delta large enough)
  Precondition-4 Match-Range (Goldilocks zone — dynamic)
  Precondition-5 Compile-Gate (opioid vs cortisol)

  → Precondition-2 says "chunks base inadequate → confused" — FAILURE MODE when receiving stimulus
  → Does NOT say: no chunks = gap CANNOT FORM = desire does not yet exist
  → Precondition-4 says "Goldilocks zone" — BUT match WITH WHAT?
    With gap direction! (implicit, not yet explicit)


03-REWARD.MD §5.9 (Car Paradox):

  "Reward = personalized function F(object, person's chunks, pending, history)"
  "Reward is NOT intrinsic to object"

  → Conclusion CORRECT — but MECHANISM not yet explained:
    Why personalized? BECAUSE each person has a DIFFERENT gap direction.
```

### §0.2 — What is MISSING

```
⭐ CURRENT FRAMEWORK = CORRECT BUT MISSING 1 DIMENSION:

  ALREADY PRESENT (implicit):
    ✅ Gap = hole in network
    ✅ "Structure predicts C" → C must fit A, B
    ✅ Reward = personalized
    ✅ Goldilocks zone (match range)

  MISSING (not yet explicit):
    ❌ Gap has SPECIFIC SHAPE = f(surrounding chunk network)
    ❌ "Not knowing = no gap" = GENESIS principle (prior to Precondition-1)
    ❌ Reward = DIRECTION MATCH quality (not just "fill or not fill")
    ❌ Prediction error = signal, direction = content (2 layers, distinct)
    ❌ All direction = chunk pattern direction (unified Tier 1-4)
    ❌ Gap direction can be INSTALLED from outside (F3 for gaps)
    ❌ Background-Pattern CONSTRAINS the gap direction landscape

  v2.0 — ONE MORE MISSING LAYER (not in v1.0):
    ❌ Gap direction = WHY by-product match works (Inter-Body §5.4)
    ❌ B's output matches A's gap DIRECTION → A rewards
    ❌ Direction mismatch = ANTI-MATCH (not just no-match)
    ❌ 2-Stream connection: Hardware-Stream = hardware gap direction matched,
       Modeling-Stream = Self-Pattern-Modeling-mediated gap direction matched
    ❌ Compilable Architecture × gap direction: general-purpose reward =
       gap direction NOT hardwired per-content → emerges from chunk network

  CONSEQUENCE OF MISSING:
    → When saying "gap fill → reward" — no explanation for
      why SAME gap with DIFFERENT fill → DIFFERENT reward
    → When saying "reward = personalized" — no MECHANISM underneath
    → When saying "Precondition-4 Match-Range" — no specification of match WITH WHAT
    → When saying "by-product match" — no explanation of WHY match/mismatch
    → = Framework describes CORRECTLY but does not EXPLAIN the deepest layer
```

### §0.3 — What this file adds

```
THIS FILE:
  → Does NOT modify existing definitions — they are CORRECT
  → ADDS a new dimension: direction (content specificity)
  → FORMALIZES necessary consequences from "gap = hole in network"
  → BRIDGES: gap mechanism (§3.3) ↔ reward evaluation (Body-Feedback-Precondition) ↔
    personalized reward (03-Reward §5.9)
  → v2.0: BRIDGES: gap direction ↔ by-product match ↔ 2-Stream
    (WHY inter-body reward works = output matches gap DIRECTION)
  → = Missing explanatory layer between "chunks fire" and "reward fires"
```

---

## §1 — DEFINITION

### §1.1 — What is Gap Direction

```
⭐ GAP DIRECTION = THE SPECIFIC SHAPE OF A HOLE IN THE CHUNK NETWORK:

  Body-Feedback-Mechanism.md §3.3 defines:
    Gap = hole in chunk network where structure predicts something missing

  Gap Direction = WHAT SPECIFICALLY is predicted missing:
    → Shape of the hole = constraints on what counts as valid fill
    → Determined by: surrounding chunks' content + links + density
    → Formal: Gap_Direction = f(surrounding_chunk_network_structure)

  Example:
    Network: [peers have stylish cars] + [going out feels good] + [looking cool]
    → Predicts: "if I also had a stylish trendy car → cool like that"
    → Gap direction = "stylish trendy car popular with peers"
    → NOT "a car" generically
    → NOT "a mode of transport"
    → NOT "an expensive thing"
    → = SPECIFIC direction, dependent on SPECIFIC surrounding compiled chunks
```

### §1.2 — Distinguishing: Gap vs Gap Direction

```
⭐ GAP ≠ GAP DIRECTION:

  GAP (§3.3):
    → Binary question: is there a hole or not?
    → Answer: yes/no
    → Trigger: ACC detects inconsistency → body signal
    → = DETECTION mechanism

  GAP DIRECTION:
    → Shape question: where does the hole point, which fills does it accept?
    → Answer: specific set of constraints
    → Determines: which fills count as VALID → whether reward fires
    → = EVALUATION mechanism

  SAME gap, DIFFERENT direction analysis:

    Einstein: Gap "unified physics" (binary: yes)
    Direction: must reconcile Newton + Maxwell + be mathematically elegant
    → E=mc² MATCHES direction → massive reward
    → Random formula MISSES direction → no reward

    Child wants a car: Gap "wants a car" (binary: yes)
    Direction: stylish + trendy + peers impressed + can drive out
    → The right car MATCHES → intensely pleasant
    → Vintage car MISSES direction (not trendy, peers not impressed)
    → Rocket OUTSIDE direction entirely (no chunks match at all)

  → Gap = "IS something missing?" (yes/no)
  → Gap Direction = "WHAT SPECIFICALLY is missing?" (shape + constraints)
  → Body-feedback needs BOTH: detect gap (§3.3) + evaluate direction match
```

### §1.3 — Relationship to §3.3

```
🟡 GAP DIRECTION DOES NOT REPLACE §3.3 — IT SUPPLEMENTS:

  §3.3 (Chunk-Gap mechanism):
    → HOW gap arises (network topology, ACC detection)
    → HOW gap transitions (Gap→Miss via Imagine-Final)
    → HOW gap drives behavior (novelty loop)
    → = MECHANISM layer

  Gap Direction (this file):
    → WHY gap has specific shape (surrounding chunk network)
    → WHY same gap accepts some fills but not others (direction match)
    → WHY reward magnitude varies (match quality)
    → = EVALUATION layer

  ANALOGY:
    §3.3 = "How the fire alarm WORKS" (mechanism)
    Gap Direction = "WHERE the fire is and WHAT KIND of response is needed" (content)
    → Need BOTH: detect + specify
```

### §1.4 — Gap Direction × By-Product Match (★ v2.0)

```
⭐ GAP DIRECTION = WHY BY-PRODUCT MATCH WORKS:

  Inter-Body-Mechanism.md §5.4 principle:
    Entity B fills B's gap → output = by-product
    When by-product matches A's gap direction → A receives reward

  GAP DIRECTION IS THE MECHANISM UNDERNEATH:
    → "Match" = B's output FITS THE SPECIFIC SHAPE of A's gap direction
    → "Mismatch" = B's output MISSES A's gap direction (no reward)
    → "Anti-match" = B's output CONFLICTS with A's gap direction (friction)

  EXAMPLES THROUGH THE GAP DIRECTION LENS:

    Striker → Defender:
      Defender A: gap "want team to win" → direction = "goals + defensive hold"
      Striker B: fills B's gap "want to score" → output = goal scored
      B's output = goal → matches A's direction "team wins"
      → A rewards. B neither knows nor needs to know A's gap direction.
      = By-product match BECAUSE directions happened to ALIGN.

    Father buys vintage car for child:
      Child A: gap direction = "stylish trendy car popular with peers"
      Father B: fills B's gap "want child to be happy" → output = vintage car (father's aesthetic)
      B's output = vintage car → MISSES A's direction (wrong aesthetic)
      → A does NOT reward. Father had good intentions but output MISSES DIRECTION.
      = By-product MISMATCH because father's gap direction ≠ child's gap direction.

    Innovation-focused CEO ↔ stability-preferring employee:
      Employee A: gap direction = "stability, routine, predictable"
      CEO B: fills B's gap "want growth" → output = change, disruption
      B's output = change → CONFLICTS A's direction (opposite to stability)
      → A is NEGATIVE (active friction, not just no-match).
      = ANTI-MATCH: by-product actively conflicts gap direction.

  ⭐ WHY BY-PRODUCT MATCH HAPPENS FREQUENTLY ENOUGH:
    → Species-level hardware overlap → gap directions PARTIALLY overlap
    → Same species → same basic needs → basic gap directions SIMILAR
    → Culture/language = shared chunk install → shared gap directions
    → Self-selection: gravitate toward high match-rate partners
    → = Foundation for Resonance (By-Product-Gap-Resonance v1.0 §1.5)

🟡 Gap direction as by-product match mechanism = framework synthesis.
   By-product match principle (Inter-Body §5.4) = 🟡 established logic.
   Species hardware overlap = 🟢 evolutionary biology.
```

---

## §2 — PROOF: WHY GAPS MUST HAVE DIRECTION

### §2.1 — Logical necessity

```
⭐ GAP DIRECTION = NECESSARY CONSEQUENCE, NOT ASSUMPTION:

  From §3.3: Gap = HOLE in chunk network

  STEP 1 — A hole exists BECAUSE there are walls:
    → Hole in a wall: exists because there is WALL AROUND it
    → Remove the wall → no hole remains → only empty space
    → Hole in chunk network: exists because there are SURROUNDING CHUNKS
    → Remove surrounding chunks → no hole → only "not knowing"
    → = HOLE AND WALLS CANNOT BE SEPARATED

  STEP 2 — Walls have shape → hole has shape:
    → Walls = surrounding chunks with SPECIFIC CONTENT
    → Chunk content: [A], [B], [A→B links], [A→? predictions]
    → Hole must be COMPATIBLE with the walls → hole has SHAPE = f(walls)
    → = Gap direction = shape of hole determined by surrounding chunks

  STEP 3 — "Structure predicts C" → C has constraints:
    → A and B are SPECIFIC chunks (Newton mechanics, Maxwell electromagnetism)
    → "If A and B → C" means C must be COMPATIBLE with both A and B
    → C is NOT "anything" — C must:
      ⓐ Resolve the inconsistency between A and B
      ⓑ Not break existing connections
      ⓒ Fit the existing network topology
    → = C has CONSTRAINTS = gap has DIRECTION

  CONCLUSION:
    Gap direction = LOGICAL NECESSITY from "gap = hole in chunk network"
    No new mechanism needed
    No new assumption needed
    Only FORMALIZE the consequence already implicit in §3.3
```

### §2.2 — Puzzle analogy

```
🟡 THE MISSING PUZZLE PIECE:

  A 1,000-piece puzzle with 1 piece missing:
    → Missing piece has SHAPE = f(shape of surrounding pieces)
    → Missing piece has COLOR = f(color of surrounding pieces)
    → Missing piece has POSITION = determined by puzzle topology
    → = ANY random piece won't fit — only the RIGHT piece fills the gap

  Chunk network is IDENTICAL:
    → Gap has "shape" = constraints from surrounding chunks
    → Gap has "content direction" = what the missing pattern should look like
    → Gap has "position" = where in network topology
    → = ANY random chunk won't fill it — only the CORRECTLY DIRECTED chunk

  BUT differs from puzzles in 2 important ways:

    ① Chunk gap: direction has RANGE (Goldilocks zone)
       → Many fills CAN match at varying levels
       → Partial fill → partial reward (mini-arc)
       → = Gap direction = shape + range, not a single exact answer

    ② Chunk gap: fill CHANGES THE WALLS → changes THE NEXT GAP
       → Puzzle: fill 1 piece → picture is clearer but other pieces DON'T change
       → Chunk gap: fill 1 gap → NEW chunks compile → network GROWS
         → detect NEW inconsistencies → NEW gaps emerge
       → = Each fill CAN create additional new gaps (§7.5 oscillation dynamics)
       → Example: Einstein fills special relativity → new chunks
         → detects "gravity doesn't fit" → NEW gap "general relativity"
       → = Gap landscape DYNAMIC, not a static puzzle
```

### §2.3 — Counter-test: can a gap have NO direction?

```
🟡 TEST: FIND AN EXAMPLE OF A GAP WITHOUT DIRECTION:

  TRY: "I feel like something is missing but I don't know what"
    → Felt sense (Gendlin 1978): body detects before PFC articulates
    → BUT: body STILL has direction — only PFC hasn't articulated it yet
    → Proof: when the right thing is found → body RECOGNIZES it ("this is it!")
    → If the gap truly had no direction → body could not "recognize" a fill
    → = Gap direction EXISTS at the body level; PFC may not yet KNOW it

  TRY: "I'm bored but I don't know what I want"
    → Boredom = Chunk-Miss (Body-Feedback-Mechanism.md §3.2 variant ⓑ)
    → NOT Chunk-Gap — this is missing ACTIVITY patterns
    → Try different things → when the right one is found → body rewards → "this!"
    → = Direction exists (compiled baseline patterns) but PFC hasn't labeled it

  TRY: "I'm curious about everything" (general curiosity)
    → Novelty.md §5 (DRD4 breadth): high breadth =
      many SMALL gaps across domains
    → Each small gap STILL HAS its own direction
    → "Curious about everything" = MANY directed gaps, not 1 undirected gap
    → = Aggregate of many directed gaps ≠ one directionless gap

  CONCLUSION: No example of a gap WITHOUT direction was found.
  → Gaps always have direction — PFC may not yet know the direction (implicit)
  → = Direction is an INEVITABLE property, not optional
```

---

## §3 — "NOT KNOWING = NO GAP" (Foundational Principle)

### §3.1 — Principle statement

```
⭐⭐ FOUNDATIONAL PRINCIPLE:

  "NOT KNOWING = NO GAP"

  Formal:
    Chunks_related_to_X = ∅ → Gap_about_X = IMPOSSIBLE

  In words:
    You CANNOT miss something you don't know exists.
    A gap NEEDS surrounding chunks to EXIST.
    No surrounding chunks = no walls = no hole = no gap.
    = Desire does NOT arise naturally — desire = f(chunks accumulated)

  Quick examples:
    → A person who doesn't know iPhones exist: doesn't want an iPhone
    → A person who doesn't know chess: doesn't want a beautiful chess set
    → A student who hasn't studied deep physics: has no gap about unified physics
    → An indigenous person who doesn't know laptops: concept doesn't exist = impossible gap
```

### §3.2 — How this differs from Precondition-2 Chunk-Substrate

```
⭐ "NOT KNOWING = NO GAP" ≠ Precondition-2 Chunk-Substrate:

  Precondition-2 Chunk-Substrate:
    → WHEN: Stimulus arrives → insufficient chunks → confused → no reward
    → QUESTION: "Why no reward WHEN RECEIVING?"
    → = DIAGNOSIS — explains failure mode when stimulus HAS ARRIVED
    → Example: Child receives a Van Gogh painting → "don't get it" → Precondition-2 fail

  "Not knowing = no gap":
    → BEFORE: Before any stimulus arrives
    → QUESTION: "Why no DESIRE at all?"
    → = GENESIS — explains why desire DOES NOT YET EXIST
    → Example: Child has NEVER wanted a Van Gogh painting (gap doesn't exist)

  TWO DIFFERENT QUESTIONS, TWO DIFFERENT LAYERS:

    ┌────────────────────────────────────────────────────────────────┐
    │                                                                │
    │  LAYER 1 — GENESIS ("Not knowing = no gap"):                  │
    │    Chunks about X = ∅ → Gap about X = impossible              │
    │    → Desire DOES NOT EXIST                                    │
    │    → PRIOR EVEN TO Precondition-1 (schema pending)            │
    │    → Answers: WHY no desire                                   │
    │                                                                │
    │  LAYER 2 — DETECTION (5 Body-Feedback-Preconditions):         │
    │    Gap EXISTS → stimulus arrives → Precondition check         │
    │    → Precondition-1: gap open? Precondition-2: decode?        │
    │    → Precondition-3: delta enough? Precondition-4: in range?  │
    │    → Precondition-5: tag appropriate?                         │
    │    → Answers: WHY reward fires or doesn't fire                │
    │                                                                │
    │  = LAYER 1 determines WHETHER a gap FORMS                     │
    │  = LAYER 2 determines WHETHER reward FIRES (once gap exists)  │
    │  = "Not knowing = no gap" is PREREQUISITE for the entire      │
    │    Body-Feedback-Precondition model                            │
    │                                                                │
    └────────────────────────────────────────────────────────────────┘
```

### §3.3 — Detailed examples

```
🟡 EXAMPLE: iPHONE FOR A 3-YEAR-OLD

  3-year-old:
    Chunks about smartphone: ≈ 0
    Chunks about apps, social media, camera: ≈ 0
    → No walls → no hole → no gap
    → "Want an iPhone" = IMPOSSIBLE desire
    → Receives iPhone → curiosity (press → light comes on = sensory novelty)
    → BUT: no "pleasant because I have an iPhone" — that gap DOES NOT EXIST

  16-year-old teenager:
    Chunks: [peers have iPhones] + [great camera] + [social media] + [status]
    → Rich walls → CLEAR hole: "I don't have an iPhone"
    → Gap direction: "new iPhone, beautiful model, works for social media + camera"
    → Receives the right iPhone → gap fills → pleasant
    → Receives an old basic phone → same "phone" but MISSES direction → not pleasant

  → SAME object (iPhone). DIFFERENT gap structure → COMPLETELY DIFFERENT reward.


🟡 EXAMPLE: E=MC² FOR DIFFERENT LEVELS OF EXPERTISE

  High school student:
    Physics chunks: F=ma, a few basic formulas
    Chunks about "unified framework": ≈ 0
    → No gap about unified physics — the concept DOES NOT EXIST
    → Hears E=mc² → "oh, interesting" → label-level recognition (mild novelty)
    → NO body-level reward because NO GAP to fill

  Undergraduate (knows labels, not yet deep):
    Chunks: labels [quantum], [relativity], [wave-particle]
    → Chunks SHALLOW — labels without depth
    → Gap EXISTS but SHALLOW (sparse network → weak prediction)
    → Hears explanation of E=mc² → "so that's how it works" → mild satisfaction
    → NOT "intensely pleasant" because gap is shallow + direction is vague

  Einstein (for comparison):
    Chunks: YEARS of deep physics (Newton + Maxwell + thought experiments)
    → Gap MASSIVE: "unified framework MUST exist" → direction EXTREMELY CLEAR
    → Direction: must reconcile Newton AND Maxwell AND be elegant
    → Gap open YEARS → Gap→Miss transition → compound signal
    → Derives E=mc² → matches direction PERFECTLY → compound 3 dynamics:
      Chunk-Gap fill + Chunk-Miss reverse + Chunk-Shift self-schema
    → = "Intensely pleasant"

  ┌─────────────────────┬─────────────┬─────────────┬────────────────────┐
  │                     │ High school │ Undergrad   │ Einstein           │
  ├─────────────────────┼─────────────┼─────────────┼────────────────────┤
  │ Physics chunks      │ Minimal     │ Labels only │ Years deep         │
  │ Gap exists?         │ ❌ No       │ ✅ Shallow  │ ✅ Massive         │
  │ Gap direction       │ N/A         │ Vague, sparse│ Extremely clear   │
  │ E=mc² match?        │ N/A         │ Partial     │ Perfect            │
  │ Reward              │ Mild novelty│ Mild satisf.│ Intensely pleasant │
  └─────────────────────┴─────────────┴─────────────┴────────────────────┘

  → SAME information (E=mc²) → COMPLETELY DIFFERENT reward
  → Reward = f(gap direction match), NOT f(information value)


🟡 EXAMPLE: MUSIC LISTENING TRAJECTORY (textbook case)

  "Not knowing = no gap" applied across 4 phases of listening:

  Phase 0 — Never heard jazz:
    Jazz chunks: ≈ 0 → no walls → NO GAP → NO desire
    → First time hearing jazz: confused OR neutral → skip

  Phase 2 — Goldilocks zone (after a few listening sessions):
    Chunks: enough (genre gist compiled, swing rhythm, blue notes learned)
    → Gap FORMED + direction clear: "want to hear more of this"
    → prediction-delta in sweet spot → peak enjoyment

  Phase 4 — Saturation:
    Chunks: complete for familiar pieces → prediction-delta → 0
    → Gap CLOSES → desire FADES for familiar tracks → "bored, find something new"

  = Inverted-U trajectory: 🟢 87.7% of 57 studies confirm (Chmiel & Schubert 2017).
  = Music = pure test case because inverted-U is quantifiable + timeline compact (days-months).
  → Drill-Sound-Brain/07-Music-Entrainment-Reward-Dynamics v1.2 §5.
```

### §3.4 — Consequences of the principle

```
⭐ 5 KEY CONSEQUENCES:

  ① DESIRE IS NOT NATURAL — DESIRE IS CONSTRUCTED:
     → Newborns: only Tier 1 gaps (hunger, warmth, contact)
     → All other desires = chunks accumulate → gap forms
     → "I want X" = "chunks about X have compiled sufficiently to create a gap"
     → = Desire is CONSTRUCTED, not innate (except Tier 1)

  ② EDUCATION MUST BUILD CHUNKS FIRST:
     → Presenting answers BEFORE students have a gap = no reward
     → Must build chunks FIRST → gap forms naturally → THEN present the answer
     → = "You cannot give an answer before the question exists"
     → = Explains why learning by doing > lecture

  ③ MARKETING = GAP INSTALLATION:
     → Ads build chunks: "beautiful people use product X" + "cool lifestyle"
     → Chunks compile → gap forms: "if I also had X..."
     → Product fills gap → reward → purchase
     → = Understanding marketing through the gap direction mechanism

  ④ THERAPY MUST MAP THE GAP LANDSCAPE:
     → Client "wants happiness but doesn't know what specifically"
     → = Fuzzy gap direction (sparse or conflicted network)
     → Therapy: help build chunks → gap direction SHARPENS → action becomes possible
     → Or: identify Background-Pattern constraining the gap landscape

  ⑤ CROSS-CULTURAL DIFFERENCES = DIFFERENT GAP LANDSCAPES:
     → Culture A: rich chunks about X → active gaps about X
     → Culture B: chunks about X = ∅ → no gaps about X
     → = "Cultural values" = shared gap landscape
     → = Why "happiness" DIFFERS across cultures
```

---

## §4 — 4 PROPERTIES OF GAP DIRECTION

### §4.0 — Overview

```
⭐ GAP DIRECTION HAS 4 OBSERVABLE PROPERTIES:

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  ① DIRECTION: toward WHAT specific fill                        │
  │  ② SPECIFICITY: constraints narrow or broad                    │
  │  ③ DEPTH: surrounding network → signal strength               │
  │  ④ RANGE: Goldilocks zone within direction                     │
  │                                                                │
  │  4 properties INDEPENDENT — combine to determine:              │
  │  → WHICH fills the gap accepts                                 │
  │  → HOW STRONG the gap signal fires                             │
  │  → HOW MUCH reward when filled                                 │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘
```

### §4.1 — Direction (toward what)

```
⭐ DIRECTION = WHAT SPECIFICALLY the network predicts is missing:

  Direction answers: "Missing WHAT?"
  = Predicted content = what the gap POINTS TOWARD

  Car example:
    Network: [peers have stylish cars] + [looking cool] + [going out] + [modern aesthetic]
    → Direction: "stylish trendy car popular with peers"
    → NOT "a car" (too broad)
    → NOT "a vehicle" (too abstract)
    → NOT "an expensive vintage car" (wrong aesthetic direction)
    → = SPECIFIC direction, dependent on SPECIFIC compiled surrounding chunks

  Einstein example:
    Network: [Newton mechanics] + [Maxwell electromagnetism] + [conflict]
    → Direction: "unified framework reconciling BOTH + elegant"
    → NOT "a random formula" (misses direction)
    → NOT "pick one and discard the other" (violates network structure)
    → = Direction = WHAT specifically resolves the inconsistency

  Thirst example:
    Body-state: dehydration sensors fire → [thirst] chunks activate
    → Direction: "water" (Tier 1 evolutionarily specific)
    → NOT "food" (different body-need direction)
    → Tier 1 direction: extremely specific, universal, genetically determined

  ⭐ DIRECTION CAN CHANGE:
    → Direction CAN change as chunk network grows:
      Initially: "want a car" (broad) → learn more about models → "want model X" (narrow)
    → Direction CAN split:
      "Want a car" → learn more → "want a sports car" + "want a practical car"
    → = Direction = DYNAMIC, evolves with chunk network
```

### §4.2 — Specificity (narrow vs broad)

```
⭐ SPECIFICITY = HOW TIGHT OR LOOSE the constraints are:

  Specificity answers: "How many fills are ACCEPTED?"
  = Resolution of gap direction

  NARROW SPECIFICITY (tight constraints):
    → Collector: "a specific stamp, specific year, specific country"
    → Only 1 fill is RIGHT → match/mismatch is clear
    → Reward: VERY HIGH when matched (rare fill found)
    → Risk: VERY LOW chance of fill → frustration

  BROAD SPECIFICITY (loose constraints):
    → "Want to travel somewhere" → many destinations match
    → Many fills acceptable → easier to match
    → Reward: MODERATE per fill (less specific = less gap closure)
    → Benefit: flexible, adaptable

  SPECIFICITY = f(chunk network resolution):
    → FEW chunks about topic → direction BROAD (vague, few constraints)
    → MANY chunks about topic → direction NARROW (clear, many constraints)
    → Example: new to chess → "want a beautiful chess set" (broad)
    → Example: 10-year player → "want an ebony board, weighted pieces,
      Staunton pattern, 3.75-inch king" (narrow)

  SPECIFICITY × REWARD:
    → Narrow match → HIGH reward (rare + precise gap fill)
    → Broad match → MODERATE reward per fill
    → Narrow mismatch → HIGH dissonance (close but wrong)
    → Broad mismatch → MODERATE dissonance
    → Example: Want red car, get same model in blue (narrow miss: 90% match →
      reward IS there but with a "but..." feeling)
```

### §4.3 — Depth (signal strength)

```
⭐ DEPTH = SURROUNDING NETWORK → SIGNAL STRENGTH:

  Depth answers: "How STRONG is the gap signal?"
  = f(surrounding network size × density × time pending)

  SHALLOW (sparse network):
    → Few related chunks → thin walls → small hole
    → Body signal: mild, easy to ignore
    → Example: newly learned about a topic → mild curiosity
    → Example: student hears label "quantum" → shallow interest

  DEEP (dense network):
    → Many related chunks → thick walls → large + clear hole
    → Body signal: STRONG, persistent, hard to ignore
    → Example: Einstein's years of physics → massive gap signal → CANNOT ignore
    → Example: a 20-year collector missing 1 item → obsessive drive

  DEPTH × TIME PENDING:
    → Gap newly opened → signal moderate → CAN fade if not reinforced
    → Gap open for YEARS → Gap→Miss transition (§3.3 ①)
      → Signal COMPOUND: gap + miss + cortisol holding
    → = Depth × Time = COMPOUND signal strength

  DEPTH × REWARD MAGNITUDE:
    → Shallow gap fill → mild reward → "oh, interesting"
    → Deep gap fill → massive reward → "eureka!" "intensely pleasant!"
    → 🟡 Reward ∝ Gap_depth × Fill_match_quality
    → = Explains why Einstein's E=mc² >> student's "oh interesting"
    → = SAME information, DIFFERENT depth → DIFFERENT reward magnitude

  🟢 REFERENCE:
    → Gap decomposition mini-arc (§3.3): deeper gap = more mini-arcs needed
    → Effort-proportional reward (03-Reward.md §4.7)
    → Progress principle (Amabile & Kramer 2011): deeper gap =
      more powerful "small wins"
```

### §4.4 — Range (Goldilocks zone within direction)

```
⭐ RANGE = NOT "MORE = BETTER" — BELL CURVE WITHIN DIRECTION:

  Range answers: "How much fill is OPTIMAL?"
  = Goldilocks zone WITHIN gap direction (connects to Precondition-4 Match-Range)

  CURRENT FRAMEWORK (Precondition-4 Match-Range):
    → Goldilocks zone (dynamic — novel enough + right direction)
    → Too alien (<20%): "too strange" → confusion
    → Too familiar (>90%): "already know this" → habituation

  GAP DIRECTION EXTENDS THIS:
    → Match RIGHT DIRECTION but WRONG MAGNITUDE → ALSO misses
    → "More" within correct direction ≠ "better"

  Massage example:
    Direction: relaxation (Tier 1 body-need)
    Range: light → pleasant → slightly painful → PAIN
    = Bell curve: optimal pressure zone; beyond it = nociception
    = Correct direction, MAGNITUDE exceeds range → negative

  Praise example:
    Direction: recognition of effort (self-schema relevant)
    Range: "Good job" ✅ → "Very talented" ✅✅ →
           "Genius" ⚠️ → "The next Einstein" ❌
    = Beyond range: Precondition-4 violated (mismatch with self-schema)
    = Still "right direction" but MAGNITUDE too large → body rejects

  Monetary reward example:
    Direction: resource reward (body-need met)
    Range: $100 ✅ → $1,000 ✅✅ → $100,000 ⚠️ → $100 billion ❌
    = $100 billion: right direction (money) but EXCEEDS range
    = Body: "I don't believe it" → Precondition-4 violated (too alien for self-schema)

  Food seasoning example:
    Direction: taste reward (Tier 1)
    Range: bland → balanced → delicious → too salty/spicy → PAIN
    = Tier 1 range: evolutionarily calibrated optimal zone
    = 10× spice: correct direction (taste) but EXCEEDS range → nociception

  ⭐ RANGE = MULTI-DIMENSIONAL:
    → Body evaluates MULTIPLE dimensions SIMULTANEOUSLY
    → Example: silk fabric:
      Texture: soft ✅ + Temperature: cool ✅ + Breathability: airy ✅
      = Matches many dimensions → reward
    → Example: plastic bag:
      Texture: soft ✅ + Temperature: hot ❌ + Breathability: blocked ❌
      = Matches 1 dimension, violates many → net negative
    → = Range is PER-DIMENSION; body computes NET across all dimensions

  RANGE × SPECIFICITY:
    → Narrow specificity + narrow range = VERY hard to satisfy
      (collector wants a specific item in perfect condition)
    → Broad specificity + broad range = EASY to satisfy
      (want to go somewhere, weather reasonably nice)
    → = Specificity × Range = the "hard to please" spectrum
```

### §4.5 — 4 Properties combined

```
🟡 COMBINED TABLE:

  ┌──────────────┬──────────────────┬──────────────────┬─────────────────────┐
  │ Property     │ Question         │ Determines       │ Example             │
  ├──────────────┼──────────────────┼──────────────────┼─────────────────────┤
  │ Direction    │ Missing WHAT     │ Which fills are  │ "Stylish trendy     │
  │              │ specifically?    │ valid            │ car"                │
  ├──────────────┼──────────────────┼──────────────────┼─────────────────────┤
  │ Specificity  │ Constraints      │ How many fills   │ Broad: "a car"      │
  │              │ tight or loose?  │ match            │ Narrow: "model X    │
  │              │                  │                  │ in red"             │
  ├──────────────┼──────────────────┼──────────────────┼─────────────────────┤
  │ Depth        │ How strong is    │ Reward           │ Shallow: mild       │
  │              │ the signal?      │ magnitude        │ Deep: massive       │
  ├──────────────┼──────────────────┼──────────────────┼─────────────────────┤
  │ Range        │ How much is      │ Optimal zone     │ Massage:            │
  │              │ optimal?         │ for fill         │ light→pain curve    │
  └──────────────┴──────────────────┴──────────────────┴─────────────────────┘

  Reward = f(Direction_match × Specificity_fit × Depth × Range_within)

  → Direction wrong → no reward (vintage car for teenager)
  → Direction right + Specificity miss → partial reward (blue instead of red car)
  → Direction right + Depth shallow → mild reward (student hears E=mc²)
  → Direction right + Range exceeded → diminished/negative (over-the-top praise)
  → ALL match → maximum reward (right car for teenager, E=mc² for Einstein)
```

---

## §5 — UNIFIED DIRECTION MODEL (Tier 1-4)

### §5.1 — All direction = chunk pattern direction

```
⭐⭐ KEY INSIGHT: NOT 2 TYPES OF DIRECTION — ALL ARE PATTERNS

  Sensory input enters the brain:
    Skin touches silk → mechanoreceptors fire → neural signal
    → Somatosensory cortex → PATTERN
    → Pattern matches compiled patterns → body-feedback

  Compiled patterns FROM EVOLUTION = CHUNKS:
    → Genes wire connections in advance (Tier 1)
    → Millions of years: [smooth+breathable+cool] wired EXTREMELY DEEP
    → Universal across humans (shared evolutionary history)
    → BUT STILL CHUNKS — same substrate, same rules

  Compiled patterns FROM EXPERIENCE = CHUNKS:
    → Personal experience wires connections (Tier 2-4)
    → Years-decades: [stylish car+cool+peers approve] compiled
    → Personal/cultural (differs per person)
    → ALSO CHUNKS — same substrate, same rules

  → ONLY 1 TYPE OF DIRECTION: chunk pattern direction
  → Difference: ORIGIN + DEPTH + UNIVERSALITY
  → NOT "hardware" vs "software" — all are chunks
  → Consistent with "chunks = sole substrate" (Chunk.md v2.0 §1)

  v2.0 CONNECTION — COMPILABLE ARCHITECTURE:
    → Compilable Architecture (Body-Base.md v3.1, Inter-Body §1):
      general-purpose reward + compilation + social hardware
    → Gap directions NOT hardwired per-content (unlike Hardwired Architecture species)
    → Gap directions EMERGE from accumulated chunk network
    → = WHY gap direction is PERSONAL (not species-fixed)
    → = WHY gap direction CHANGES (chunks accumulate → direction evolves)
    → Hardwired Architecture (insects): gap directions = FIXED (genes specify)
      → Bee: "find flower with wavelength X" = hardwired direction
    → Compilable Architecture (humans): gap directions = COMPILED
      → Human: "find car that matches MY aesthetic" = compiled direction
    → = Compilable Architecture × gap direction = foundation for DIVERSITY of desires
```

### §5.2 — 4 Tiers of direction origin

```
🟡 DIRECTION ORIGIN = 4 TIERS (Chunk.md §2 calibration hierarchy):

  TIER 1 — EVOLUTIONARY (genes compile):
    → Origin: millions of years of natural selection
    → Depth: EXTREMELY DEEP (hardwired, universal)
    → Examples: hunger, thirst, pain, temperature, touch comfort
    → "Not knowing = no gap": DOES NOT APPLY in the usual sense
      → Genes have already "known" → newborns STILL have gaps (hunger)
      → = Species already "experienced" millions of years → genes carry knowledge
    → Modifiable: EXTREMELY DIFFICULT (requires evolutionary timescale)
    → Example: silk → skin feels directly → reward
      even without prior exposure (Tier 1 chunks already know "smooth = good")

  TIER 2 — DEVELOPMENTAL (childhood compile):
    → Origin: childhood experience (0-18)
    → Depth: DEEP (compiled during critical periods)
    → Examples: attachment style, cultural norms, language
    → "Not knowing = no gap": FULLY APPLIES
    → Modifiable: DIFFICULT (Background-Pattern territory)
    → Example: child grows up seeing peers with cars → gap forms

  TIER 3 — CULTURAL (shared compile):
    → Origin: cultural exposure, education, social learning
    → Depth: MODERATE (compiled through repeated cultural input)
    → Examples: "vintage car = valuable" (collector culture), jazz appreciation
    → "Not knowing = no gap": FULLY APPLIES
    → Modifiable: MODERATE (exposure + time)
    → Example: Father loves vintage cars (Tier 3 collector culture) →
      different gap direction than child (Tier 2-3 youth culture)

  TIER 4 — LEARNED (individual compile):
    → Origin: deliberate learning, expertise
    → Depth: VARIABLE (depends on effort × time × emotional weight)
    → Examples: physics expertise, programming skill, art training
    → "Not knowing = no gap": FULLY APPLIES
    → Modifiable: EASIEST (build chunks → gap direction shifts)
    → Example: Einstein's physics chunks (Tier 4) → gap direction "unified physics"
```

### §5.3 — Tier 1 special: genes = pre-installed chunks

```
⭐ TIER 1 HAS ONE IMPORTANT DIFFERENCE:

  "Not knowing = no gap" principle says:
    No chunks → no walls → no hole → no gap

  BUT Tier 1: genes PRE-INSTALL chunks:
    → Newborns have NOT experienced mother's milk → BUT STILL have a gap (hunger)
    → Have not experienced warmth → BUT STILL have a gap (cold discomfort)
    → = "Individual doesn't yet know" but "species already knows"
    → Genes carry evolutionary knowledge as PRE-COMPILED chunks

  REFINED PRINCIPLE for Tier 1:
    Original: "Not knowing = no gap"
    Refined: "Not knowing AND genes haven't wired it = no gap"
    → Tier 1: genes wire → gap exists without personal experience
    → Tier 2-4: genes DON'T wire → gap REQUIRES personal/cultural experience
    → = 2 sources of "knowing": evolutionary (genes) + experiential (chunks)

  WHY THIS REFINEMENT MATTERS:
    → Explains the silk example: first time wearing it IS pleasant
      (Tier 1 chunks "already know" smooth = good)
    → Explains food: first time eating something delicious DOES taste good
      (Tier 1 taste receptors calibrated)
    → Explains why Tier 1 gaps are UNIVERSAL but
      Tier 2-4 gaps are PERSONAL
    → = Tier 1 = shared species knowledge.
      Tier 2-4 = individual accumulated knowledge.
```

### §5.4 — Unified comparison table

```
🟡 COMPARISON ACROSS 3 CASES VIA UNIFIED MODEL:

  ┌──────────────────┬───────────────┬───────────────┬───────────────┐
  │                  │ Silk (Tier 1) │ Car (Tier 2-3)│ E=mc²(Tier 4)│
  ├──────────────────┼───────────────┼───────────────┼───────────────┤
  │ Chunk origin     │ Evolution     │ Experience +  │ Years of      │
  │                  │ (genes wire)  │ social context│ study         │
  │ Depth            │ Extremely deep│ Moderate      │ Deep (expert) │
  │ Universality     │ ~Universal    │ Cultural/     │ Individual    │
  │                  │               │ generational  │               │
  │ Gap direction    │ Multi-dim     │ Specific      │ Specific      │
  │                  │ optimal space │ social object │ knowledge gap │
  │ "Not knowing =   │ N/A (genes    │ ✅ Fully      │ ✅ Fully      │
  │   no gap"        │ pre-install)  │ applies       │ applies       │
  │ Modifiable?      │ Extremely hard│ Moderate      │ Yes (learn)   │
  │ Direction source │ Genes         │ Chunks + Bgnd │ Chunks        │
  │ Match mechanism  │ Sensory match │ Pattern match │ Pattern match │
  │ Range type       │ Evolutionary  │ Social/       │ Intellectual  │
  │                  │ optimal zone  │ personal zone │ coherence     │
  └──────────────────┴───────────────┴───────────────┴───────────────┘

  ⭐ SAME MECHANISM: chunks → gap direction → match → reward
  ⭐ DIFFERENT: origin, depth, universality, modifiability
  ⭐ = 1 UNIFIED MODEL for ALL reward/dissonance evaluation
```

### §5.5 — Compiled/Fresh processing × gap direction (★ v2.0)

```
⭐ GAP DIRECTION EVALUATION = COMPILED OR FRESH:

  (Inter-Body-Mechanism.md §3, Body-Feedback-Label.md v2.0 §8)

  COMPILED EVALUATION (body-direct, cost ≈ 0):
    → Expert in domain: compiled chunks match CHECK → automatic
    → Hears E=mc² → body KNOWS whether it matches (Einstein case)
    → Sees a car → body KNOWS "right direction" or not (teenager case)
    → Speed: milliseconds. Accuracy: HIGH (if chunks are rich)
    → = Gap direction match evaluated BEFORE PFC is aware

  FRESH EVALUATION (PFC deliberate, costly):
    → New domain: PFC must BUILD the match/mismatch assessment
    → Read car reviews → PFC processes specs → "does this match my gap?"
    → Speed: slow (seconds-minutes). Accuracy: VARIABLE.
    → = PFC TRIES to evaluate — but CAN BE WRONG (PFC=Lawyer §7)

  SPECTRUM (not binary):
    → Full compiled: body knows instantly (expert + domain match)
    → Mostly compiled + some fresh: body guides + PFC fine-tunes
    → Mostly fresh: PFC leads + body gives vague signal
    → Full fresh: no compiled chunks → "don't know what I want"

  ⭐ WHY THIS MATTERS:
    → Expert's "feeling" about a match = COMPILED evaluation (accurate, fast)
    → Beginner's "analysis" of a match = FRESH evaluation (slow, uncertain)
    → "Trust your gut" = trust compiled evaluation (IF chunks are rich)
    → "Think carefully" = use fresh evaluation (IF compiled is insufficient)
    → = Dual Check (Ask-AI v3.1): body = quality controller, domain = arbiter

🟡 Compiled/Fresh evaluation spectrum = framework synthesis.
   Compiled processing = automatic = 🟢 (dual-process theory, Kahneman 2011).
   Fresh PFC processing = deliberate = 🟢 (working memory literature).
```

---

## §6 — 2-LAYER MODEL: SIGNAL MECHANISM vs DIRECTION CONTENT

### §6.1 — Why 2 layers are needed

```
⭐ PREDICTION ERROR (SCHULTZ 1997) IS CORRECT BUT INSUFFICIENT:

  Schultz 1997:
    → VTA fires dopamine when: actual > predicted
    → VTA suppresses when: actual < predicted
    → = Signal mechanism: body DETECTS "something is different from expected"
    → = GENERIC: "better/worse than expected" — but
      does NOT carry information about "different IN WHAT WAY specifically"

  INSUFFICIENT because:
    → Same "actual > predicted" (positive prediction error)
    → But: trendy car = pleasant, vintage car = not liked
    → Both are "better than expected" (father bought a car unexpectedly)
    → Why DIFFERENT reward? Because the DIRECTION is DIFFERENT.

  NEED LAYER 2:
    → Layer 1 tells us: "there is mismatch/match" (signal fires)
    → Layer 2 tells us: "match WITH WHAT specifically" (direction content)
    → Need BOTH to explain reward as actually experienced
```

### §6.2 — 2 Layers defined

```
⭐⭐ 2-LAYER MODEL:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  LAYER 1 — SIGNAL MECHANISM (HOW body detects):            │
  │                                                             │
  │    VTA: detects prediction-delta (Schultz 1997)             │
  │    ACC: detects inconsistency (Bush et al. 2000)            │
  │    = GENERIC mechanism: "something is different/missing/    │
  │      inconsistent"                                          │
  │    = Does NOT carry information "different IN WHAT WAY"     │
  │    = Fire alarm: only signals "there IS a fire"            │
  │                                                             │
  │  LAYER 2 — DIRECTION CONTENT (WHAT body expects):          │
  │                                                             │
  │    Chunk network structure: surrounding chunks define gap   │
  │    Gap direction: WHAT specifically is predicted missing    │
  │    Match quality: HOW well stimulus fits gap shape          │
  │    = PERSONAL: each person has a DIFFERENT direction        │
  │    = Building map: shows "WHERE the fire is, which way"    │
  │                                                             │
  │  TOGETHER = COMPLETE EVALUATION:                            │
  │    Layer 1: "there IS a fire" (signal fires)               │
  │    Layer 2: "fire in the kitchen, need water" (direction)  │
  │    = Body detects + knows direction = reward or dissonance  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  v2.0 NOTE — BY-PRODUCT MATCH × 2-LAYER MODEL:
    → Inter-body interaction:
      Layer 1: "B did something" (prediction-delta from B's action)
      Layer 2: "Does B's output match MY gap direction?" (direction evaluation)
    → By-product match = Layer 2 match positive
    → Anti-match = Layer 2 match NEGATIVE (conflicts direction)
    → No-match = Layer 1 fires but Layer 2 = neutral (irrelevant)
    → = 2-layer model explains why same action by B →
      A1 rewards, A2 no-match, A3 anti-match (different gap directions)
```

### §6.3 — Body-Feedback-Preconditions reinterpreted through 2 layers

```
⭐ 5 BODY-FEEDBACK-PRECONDITIONS = ALREADY DESCRIBE 2 LAYERS (not yet stated explicitly):

  ┌─────────────────────────────────┬──────────┬──────────────────────────────┐
  │ Body-Feedback-Precondition      │ Layer    │ Function in 2-layer model    │
  ├─────────────────────────────────┼──────────┼──────────────────────────────┤
  │ Precondition-1 Directed-Gap     │ Layer 2  │ DIRECTION EXISTS             │
  │ (body-need gap)                 │          │ Gap formed, has direction    │
  │                                 │          │ = Prerequisite for evaluation│
  ├─────────────────────────────────┼──────────┼──────────────────────────────┤
  │ Precondition-2 Chunk-Substrate  │ Layer 2  │ DIRECTION CAN FORM           │
  │ (sufficient substrate)          │          │ Enough chunks = walls = hole │
  │                                 │          │ = Prerequisite for P1        │
  ├─────────────────────────────────┼──────────┼──────────────────────────────┤
  │ Precondition-3 Delta-Gate       │ Layer 1  │ SIGNAL FIRES                 │
  │ (delta large enough)            │          │ Prediction-delta detected    │
  │                                 │          │ = Detection mechanism active │
  ├─────────────────────────────────┼──────────┼──────────────────────────────┤
  │ Precondition-4 Match-Range      │ Layer 2  │ DIRECTION MATCH QUALITY      │
  │ (Goldilocks zone — dynamic)     │          │ Match WITH gap direction     │
  │                                 │          │ = Range property check       │
  ├─────────────────────────────────┼──────────┼──────────────────────────────┤
  │ Precondition-5 Compile-Gate     │ Layer 2  │ DIRECTION VALENCE            │
  │ (opioid/cortisol)               │          │ Compiled association tag     │
  │                                 │          │ = Reward or threat direction?│
  └─────────────────────────────────┴──────────┴──────────────────────────────┘

  HIERARCHY NOW CLEARER:

    "Not knowing = no gap"
        ↓ (prerequisite)
    Precondition-2: enough chunks → direction CAN form
        ↓ (prerequisite)
    Precondition-1: gap direction EXISTS (pending active)
        ↓ (gap exists, now evaluate stimulus)
    Precondition-3: signal fires (Layer 1 — detection)
        ↓ (something detected)
    Precondition-4: direction match quality (Layer 2 — within range?)
        ↓ (match quality assessed)
    Precondition-5: valence tag check (Layer 2 — reward or threat?)
        ↓
    REWARD or DISSONANCE fires

  → "Not knowing = no gap" = LAYER 0 — prior to the entire Precondition model
  → Precondition-2 → Precondition-1 = Layer 2 prerequisites (gap must exist)
  → Precondition-3 = Layer 1 (signal must fire)
  → Precondition-4 → Precondition-5 = Layer 2 quality check
  → = Preconditions ALREADY described 2 layers — just hadn't DISTINGUISHED them
```

### §6.4 — Why the 2-layer model is useful

```
🟡 EXPLAINS PHENOMENA THAT THE 1-LAYER MODEL CANNOT:

  ① "Same prediction error, different reward":
    → Trendy car and vintage car: BOTH are surprises (positive prediction error)
    → 1-layer: both should reward → WRONG
    → 2-layer: Layer 1 fires for BOTH, but Layer 2 only matches for
      the trendy car → CORRECT

  ② "Reward is personal":
    → 1-layer: prediction error = generic → should be universal → WRONG
    → 2-layer: Layer 2 = chunk network = PERSONAL → reward is personal → CORRECT

  ③ "More ≠ better":
    → 1-layer: larger prediction error = more reward → WRONG
    → 2-layer: Layer 1 = larger delta, but Layer 2 = out of range
      → diminished/negative → CORRECT

  ④ "Know but don't feel":
    → PFC updated (Layer 1 acknowledged) but
      chunk network unchanged (Layer 2 direction same)
    → 1-layer: know = feel → WRONG
    → 2-layer: Layer 1 (know) ≠ Layer 2 (feel direction) →
      can diverge → CORRECT

  ⑤ "By-product match is selective" (v2.0):
    → 1-layer: B did something unexpected → all observers reward → WRONG
    → 2-layer: Layer 1 fires for all observers, but Layer 2 (direction match)
      = DIFFERENT per observer → only matching observers reward → CORRECT
    → = Explains why same action → some people like it, others don't

  → 2-layer model does NOT REPLACE prediction error —
    ADDS a layer underneath explaining CONTENT
```

---

## §7 — GAP DIRECTION FORMATION

### §7.1 — Natural formation: chunks compile → gaps emerge

```
⭐ GAP DIRECTION FORMS NATURALLY AS CHUNKS ACCUMULATE:

  FLOW:
    Experience → chunks compile → network grows → internal structure forms
    → Structure predicts "C should exist" → C not yet present → GAP with DIRECTION

  Example — child sees peers' cars:
    ① Sees peer with a stylish car → chunks compile: [peer-has-car] + [looks-cool]
    ② Hears peer talk about drives → more chunks: [going-out-freely] + [independence]
    ③ Sees girl impressed by peer's car → chunks: [car → impressed]
    ④ Network predicts: "if I also had one → cool + free + impressed"
    ⑤ Prediction not yet reality → GAP forms
    ⑥ Gap direction = f(all compiled chunks):
       "stylish trendy car popular with peers"
    → NOT A SINGLE STEP REQUIRED PFC TO ACTIVELY DO THIS
    → Unconscious compiles automatically → gap emerges naturally

  Example — student gradually learning physics:
    ① Studies Newton → chunks compile: [F=ma] + [gravity]
    ② Studies Maxwell → more chunks: [electromagnetic waves] + [light]
    ③ If teacher is GOOD → introduces conflict: "Newton and Maxwell
       contradict each other about the speed of light"
    ④ Conflict chunks: [Newton ≠ Maxwell at X]
    ⑤ Network predicts: "there must be a framework that resolves this"
    ⑥ Gap forms: direction = "resolve Newton-Maxwell contradiction"
    → Gap ONLY forms AFTER sufficient chunks compile
    → A POOR teacher skips the conflict → student has NO gap → lecture is boring

  FORMATION SPEED:
    → Emotional peak experience: 1 event CAN be sufficient
      (Example: seeing peer drive a cool car → emotional → gap forms fast)
    → Neutral repeated experience: needs many repetitions
      (Example: studying physics gradually → gap forms slowly)
    → = Chunk.md §2.2: compile rate = f(repetition × saliency ×
      peak_valence × multi_modal × contingency)
```

### §7.2 — Gap→Miss transition: direction SHARPENS

```
🟡 IMAGINE-FINAL PREVIEW MAKES DIRECTION CLEARER:

  Body-Feedback-Mechanism.md §3.3 ①:
    Gap detected → PFC builds Imagine-Final preview
    → Preview repeats → body compiles preview into baseline
    → Gap TRANSITIONS to Miss (body now EXPECTS what it doesn't have)

  GAP DIRECTION PERSPECTIVE:
    → Initially: gap direction VAGUE (sparse network → shape unclear)
    → Imagine-Final preview: ADDS DETAIL to direction
      "Have a car" → "model X" → "model X in red" → "drive to the beach"
    → Each preview cycle: direction SHARPENS (specificity increases)
    → = Imagine-Final = direction refinement mechanism

  Example: "Want a car" evolution:
    Week 1: "want a car for getting around" (broad direction)
    Week 4: "want a sports car, good-looking" (direction narrowing)
    Month 3: "want model X, red, black interior" (narrow direction)
    → Direction SHARPENS with each Imagine-Final preview iteration
    → Specificity increases → range narrows → harder to satisfy

  ⚠️ RISK: Over-specification
    → Too many preview loops → direction becomes EXTREMELY narrow
    → Reality rarely matches 100% → "achieved it but still feel something's missing"
    → = §3.3 ⑦: "The higher the expectation, the greater the disappointment"
    → = Direction over-specification = setup for disappointment
```

### §7.3 — Direction change: network grows → gap shape evolves

```
🟡 GAP DIRECTION IS NOT FIXED — EVOLVES WITH THE NETWORK:

  New chunks compile → surrounding network changes
  → Walls change → hole shape changes → direction evolves

  Example: "Want a car" → learn more → direction SHIFTS:
    Phase 1: "stylish trendy car" (youth aesthetic)
    Phase 2: learn about cars → discover vintage car value → new chunks compile
    Phase 3: gap direction SHIFTS: "classic vintage cars are beautiful too"
    → = Education/exposure → direction shift POSSIBLE

  Career gap direction evolution:
    Age 18: "want to be wealthy" (broad, status-driven)
    Age 25: "want a career with meaning" (direction shift via experience)
    Age 35: "want work-life balance" (direction shift via feedback)
    → Each phase: chunks compile → gap direction evolves

  BUT: Background-Pattern RESISTS direction change (§9):
    → Background-Pattern = deeply compiled pattern → biases gap landscape
    → Gap direction shift MUST overcome Background-Pattern inertia
    → = Why career change at 35 is HARDER than at 25
    → = Background-Pattern.md: resolution = years, not weeks
```

### §7.4 — Direction split: 1 gap → 2 sub-gaps

```
🟡 A GAP CAN SPLIT AS THE NETWORK REFINES:

  Network grows → detects: "this gap is actually 2 DIFFERENT gaps"
  → 1 parent gap → 2+ child gaps, each with its own direction

  Example: "Want a car" splits:
    → "Want a sports car (weekend drives)"
    → "Want a practical car (daily commute)"
    → = 2 functions, 2 contexts, 2 directions

  Einstein's "unified physics" splits:
    → "Special relativity" (uniform motion)
    → "General relativity" (gravity + acceleration)
    → Each sub-gap has its own direction, its own fill

  = Gap decomposition (§3.3 mini-arc) IS also direction split:
    Big gap → mini gaps = big direction → sub-directions
    Each sub-gap fill = mini reward
    All sub-gaps filled = compound reward
```

### §7.5 — Oscillation dynamics: fill creates BOTH reward AND new dissonance

```
⭐⭐ MINI-FILL DOESN'T JUST REDUCE THE GAP — IT ALSO CREATES NEW GAPS:

  SIMPLE (incorrect) view:
    Gap → fill → reward → smaller gap → fill → ... → gap = 0 → done
    = Linear decrease, eventually finished

  CORRECT view:
    Gap → fill → reward + NEW CHUNKS COMPILE
    → New chunks = new WALLS → detect NEW inconsistencies
    → = MORE dissonance (larger network → sees MORE)
    → Net: reward FROM fill + dissonance FROM new detections

  MECHANISM:

    ① FILL: mini gap closed → new chunks compile → opioid (reward) ✅
    ② GROW: new chunks = network expands → new walls appear
    ③ DETECT: bigger network → detect inconsistencies NOT SEEN before
    ④ NEW GAP: new inconsistency → new gap → new direction
    ⑤ OSCILLATION: reward (①) + dissonance (④) SIMULTANEOUSLY

  PATTERN:
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  fill₁ → reward₁ + chunks₁ → detect new gap₂       │
    │  fill₂ → reward₂ + chunks₂ → detect new gap₃       │
    │  fill₃ → reward₃ + chunks₃ → detect new gap₄       │
    │  ...                                                │
    │  fillₙ → BREAKTHROUGH: many chunks suddenly UNIFY  │
    │       → COMPOUND reward (all accumulated gaps close)│
    │       → BUT: bigger network → detect NEXT-LEVEL gap │
    │       → LOOP CONTINUES at higher level              │
    │                                                     │
    └─────────────────────────────────────────────────────┘

  TREND across the process:
    → Reward per fill: INCREASES (each fill more chunks = more opioid)
    → Dissonance per detection: ALSO INCREASES (larger network = bigger holes)
    → Total dissonance: ACCUMULATES (many unresolved mini-inconsistencies)
    → Until CRITICAL MASS: accumulated chunks suddenly cohere
    → = BREAKTHROUGH = compound resolution of ALL accumulated gaps

  Einstein example (detail in §10.4):
    Years 1-5: fill photoelectric → reward + new chunks
      → detect "wave-particle duality contradiction" → new dissonance
    Years 5-10: fill special relativity → reward + new chunks
      → detect "gravity doesn't fit" → more dissonance
    Years 10-15: accumulate tensor math + thought experiments
      → dissonance EXTREMELY HIGH (many valuable chunks not yet unified)
    November 1915: field equations → ALL accumulated chunks UNIFY
      → COMPOUND reward (years × massive network × all-at-once)

  ⭐ WHY BREAKTHROUGH REWARD IS SO INTENSE:
    → Reward is NOT just "fill 1 gap"
    → Reward = resolve ALL accumulated mini-inconsistencies SIMULTANEOUSLY
    → = Accumulated dissonance over YEARS → released IN ONE MOMENT
    → Compound: Gap fill + Miss reverse + Shift + Cortisol drop
    → = Why "eureka" moments feel TRANSCENDENT

  ⚠️ RISK: If breakthrough doesn't come:
    → Accumulated dissonance keeps growing → no compound resolution
    → Cortisol holding → persistent → burnout
    → = Why research CAN be destructive if gap is too deep
    → Example: Einstein spent 30 years on unified field theory → never resolved
    → = Perpetual gap at too deep a level → chronic dissonance

  🟢 REFERENCE:
    → Progress principle (Amabile & Kramer 2011): small wins sustain motivation
    → Gap decomposition (§3.3 mini-arc): each mini fill = reward
    → Combinatorial explosion (Novelty.md §5): network grows → more combinations
```

---

## §8 — GAP DIRECTION × EXTERNAL INSTALL

### §8.1 — F3 applied to gap CREATION

```
⭐ CHUNK EXTERNAL INSTALL (F3) → GAP INSTALL:

  Chunk.md §2 F3: External Install = chunks installed from outside
  (education, media, social influence, advertising)

  GAP DIRECTION PERSPECTIVE:
    → F3 installs chunks AROUND a potential gap → gap NATURALLY FORMS
    → External agent does NOT "install a gap directly"
    → External agent installs CHUNKS → chunks create WALLS → hole emerges
    → = "Directed gap installation" = build surrounding chunks
      so that a gap forms with the DESIRED DIRECTION

  MECHANISM:
    ① Install chunks A, B: [product X] + [users of X = cool]
    ② Chunks compile → network predicts: "if I also had X → cool"
    ③ Prediction not yet reality → gap forms: direction = "product X"
    ④ Product X available → fills gap → reward → purchase
    → = Advertiser engineers gap direction TOWARD their product

  v2.0 NOTE — 5-CHANNEL INPUT VECTOR (Inter-Body §6):
    → Gap install via WHICH CHANNEL?
    → Ch1 Hardware Sensory: product design triggers Tier 1 (beauty, texture)
    → Ch3 Compiled Chunks: brand awareness (repeated exposure → compiled)
    → Ch4 Entity Actions: influencer uses product → social proof
    → Ch5 PFC Active Chain: ad presents "logical argument" for need
    → = Marketing uses MULTIPLE channels simultaneously
    → = Most effective: Ch3+Ch4 (compiled + social) > Ch5 only (just logic)
```

### §8.2 — 4 forms of gap installation

```
🟡 4 FORMS OF GAP INSTALL:

  ① ADVERTISING (commercial):
     → Installs chunks: [product + lifestyle + social proof]
     → Gap direction: toward specific product
     → Fill: purchase product
     → Ethical? Depends on product quality vs gap promise
     → = Marketing 101: "create need" = install gap direction

  ② EDUCATION:
     → Installs chunks: [knowledge base + conflict + curiosity]
     → Gap direction: toward understanding/skill
     → Fill: learning, practice, discovery
     → = Good teacher: build chunks FIRST → present challenge SECOND
     → = Poor teacher: present answer without gap → no reward → boring

  ③ SOCIAL MEDIA:
     → Installs chunks: [others' lives + comparison + lifestyle]
     → Gap direction: toward "lifestyle I don't have yet"
     → Fill: consumption, travel, status display
     → ⚠️ Problematic: gap direction may be UNREALISTIC
       (filtered reality → impossible Imagine-Final)
     → = Novelty.md §3: social media hacks the natural brake

  ④ CULTURE / RELIGION:
     → Installs chunks: [shared values + rituals + meaning framework]
     → Gap direction: toward culturally-defined "good life"
     → Fill: following cultural path, rituals, community belonging
     → = Shared gap landscape = cultural identity
     → = Why cultural values feel "natural" =
       gaps installed early (Tier 2) → feel like Tier 1
```

### §8.3 — Ethical implications

```
🟡 GAP INSTALL ETHICS:

  GAP INSTALL ITSELF = NEUTRAL (tool, not inherently good or bad)

  ETHICAL when:
    → Fill GENUINELY serves body-base (education → skills → resources)
    → Direction is honest (product = what was advertised)
    → Gap depth is appropriate (not manufacturing desperation)

  PROBLEMATIC when:
    → Fill does NOT serve body-base (addictive product, empty status)
    → Direction is manipulated (filtered reality → impossible standard)
    → Gap depth is artificially deepened (FOMO, scarcity tactics)
    → Exploits Tier 1 gaps (sex sells = hijack sexual gap for product)

  FRAMEWORK VIEW:
    → Understanding the gap install mechanism → understanding WHY marketing works
    → Understanding direction → understanding WHY some products "feel right"
    → Understanding "not knowing = no gap" → understanding WHY exposure matters
    → = Knowledge empowers BOTH creators AND consumers
```

---

## §9 — GAP DIRECTION × BACKGROUND PATTERN

### §9.1 — Background-Pattern constrains the gap landscape

```
⭐ BACKGROUND PATTERN BIASES WHICH GAPS CAN FORM:

  Background-Pattern.md: Background-Pattern = accumulated chunk-network pattern
  → Forms over years → invisible to PFC → biases ALL processing

  Background-Pattern × GAP DIRECTION:
    → Background-Pattern = deeply compiled chunk network THROUGHOUT the brain
    → Background-Pattern's chunks ARE "surrounding chunks" for many potential gaps
    → = Background-Pattern constrains WHICH gaps can form and WHICH DIRECTIONS they point

  Example — Background-Pattern [effort → never enough]:
    → All achievement-related chunks contaminated by [not enough]
    → Gap direction bias: "need to achieve MORE" (never enough)
    → EVEN WHEN achieved → Background-Pattern creates NEW gap: "still not enough"
    → = Chronic dissatisfaction = Background-Pattern constraining the gap landscape
    → = "Running without arriving" = the destination keeps MOVING

  Example — Background-Pattern [connection → danger]:
    → Intimacy-related chunks contaminated by [danger]
    → Gap direction SUPPRESSED: gaps about deep connection DO NOT FORM
    → Or: gap forms but direction is DISTORTED
      ("want connection" + [danger] → direction = "safe connection = control")
    → = Avoidant attachment = Background-Pattern suppressing connection gap formation

  Example — Background-Pattern [expertise → identity]:
    → Expert's identity chunks linked to domain
    → Gap direction FOCUSED: gaps about domain = STRONG
    → Gaps about OTHER domains = WEAK (Background-Pattern doesn't support)
    → = "Expert who only knows their specialty" = Background-Pattern focusing gap landscape
```

### §9.2 — Background-Pattern × gap direction resolution

```
🟡 CHANGING THE GAP LANDSCAPE REQUIRES CHANGING BACKGROUND-PATTERN:

  WHY IT IS DIFFICULT:
    → Background-Pattern chunks = deeply compiled (years)
    → Background-Pattern chunks = old walls → constrain OLD gap directions
    → Install NEW chunks → but Background-Pattern chunks STILL REMAIN → conflict
    → = Gap direction shift is PULLED BACK by Background-Pattern

  RESOLUTION (from Background-Pattern.md §10):
    → CANNOT fix Background-Pattern directly (too distributed, PFC-invisible)
    → MUST build a competing Background-Pattern → new chunks → new walls → new gap directions
    → Takes YEARS (competing pattern must reach comparable density)
    → = Therapy = slowly build new chunk network →
      new gap landscape emerges ALONGSIDE the old one
    → Old Background-Pattern doesn't disappear — new Background-Pattern competes → probability shifts

  Example:
    → Client Background-Pattern [effort → never enough]
    → Therapy: compile new chunks [effort → okay, rest is okay, enough exists]
    → New chunks create new WALLS → new gaps become possible:
      "want to rest" (gap that DID NOT EXIST before — Background-Pattern suppressed it)
    → = Therapy = GAP LANDSCAPE EXPANSION via competing Background-Pattern
```

---

## §10 — ABSTRACT ACTIVITY × BODY-BASE

### §10.1 — The "hijack" question

```
⭐ "WHAT DOES E=MC² DO FOR BODY-BASE?" — DEEP ANALYSIS:

  PROPOSAL: Abstract work (physics, art, math) uses mechanisms
  evolved for survival → body reward fires despite NOT being directly survival-relevant

  BUT "HIJACK" IMPLIES: mechanism is being misused, output does NOT serve body-base
  → Analysis shows: this is NOT "misuse" — it is EXTENDED APPLICATION
```

### §10.2 — Evolution wired: inconsistency = danger

```
🟡 TIER 1 MECHANISM: INCONSISTENCY DETECTION

  Evolution selected:
    → Inconsistent environment = hard to predict = dangerous
    → Predator behaving unpredictably → hard to predict trajectory → more likely to be killed
    → Genes wire: detect inconsistency → body discomfort → FIX IT → safety
    → = ACC (Anterior Cingulate Cortex) = inconsistency detector
    → 🟢 Bush, Luu, Posner 2000: ACC fires on conflict/error

  Mechanism properties:
    → Does NOT distinguish domain: ACC detects ANY inconsistency
    → [prey moving in strange direction] = inconsistency → body alert
    → [Newton ≠ Maxwell] = inconsistency → body alert
    → SAME ACC, SAME signal type
    → Body does NOT "know" this is physics — body only knows "pattern doesn't match"

  → = Tier 1 mechanism applied BEYOND its original domain
  → Like: hand evolved for grasping → ALSO used for writing, playing piano
  → = Extended application, NOT malfunction

  v2.0 NOTE — COMPILABLE ARCHITECTURE CONNECTION:
    → Compilable Architecture = general-purpose reward (Inter-Body §1)
    → General-purpose = SAME mechanism fires for ANY domain
    → = WHY abstract activity CAN fire body reward
    → Hardwired Architecture (insects): mechanism SPECIFIC per domain
      → Bee cannot feel "eureka" about physics
    → Compilable Architecture (humans): mechanism GENERAL
      → Human CAN feel "eureka" about abstract patterns
    → = Abstract gap fill is a FEATURE of Compilable Architecture, not a bug
```

### §10.3 — 2 paths to serving body-base

```
⭐ ABSTRACT ACTIVITY SERVES BODY-BASE VIA 2 PATHS:

  PATH 1 — DIRECT (internal state improves):
    → Inconsistency in world model → body feels "unsafe" → cortisol
    → Resolve inconsistency → pattern coherent → body feels "safe" → opioid
    → = Body-base state GENUINELY improves:
      ✅ Cortisol decreases (inconsistency resolved)
      ✅ Opioid increases (coherence reward)
      ✅ Sleep improves (less pending → less cortisol holding)
    → = Body-base served DIRECTLY, INDEPENDENT of external outcome
    → = Einstein feels better THE MOMENT he derives E=mc², before anyone knows

  PATH 2 — INDIRECT (external outcome):
    → Abstract work → expertise → recognition → status → resources
    → Einstein: E=mc² → fame → academic position → resources → body-base
    → = But this is a CONSEQUENCE, not the REASON body reward fires
    → Body reward fires BECAUSE of Path 1 (gap fill)
    → Path 2 = bonus, often arrives LATER

  WHY EVOLUTION DIDN'T "CUT OFF" ABSTRACT APPLICATION:
    → Because: people who solve abstract problems = SURVIVAL ADVANTAGE
    → Tool invention, strategic planning, prediction = abstract gap fill
    → Selection pressure: keep mechanism GENERAL → apply broadly
    → Restrict to survival-only → lose abstract capability → disadvantage
    → = "Feature, not bug" — generalizing gap detection = competitive edge
```

### §10.4 — Einstein full lifecycle (Gap Direction deep analysis)

```
⭐⭐ EINSTEIN = PERFECT CASE TO TEST THE GAP DIRECTION MECHANISM:

  Why this case matters:
  → Process spans DECADES → direction EVOLVES are clearly visible
  → Multiple mini-arcs → oscillation dynamics visible
  → Breakthrough + post-breakthrough → perpetual loop visible
  → Verify cascade → reward in layers visible
  → = Tests the ENTIRE Gap Direction mechanism end-to-end


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 0 — INITIAL GAP DIRECTION: VAGUE                     │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Chunks: [Newton mechanics] + [Maxwell electromagnetism]    │
  │  Conflict: "speed of light inconsistent between frameworks" │
  │                                                             │
  │  Gap direction:                                             │
  │    = "SOMETHING resolves this contradiction"                │
  │    = Direction VAGUE: only knows "something is needed"      │
  │    = Does NOT know the specific shape (E=mc² doesn't exist  │
  │      yet as a concept)                                      │
  │    = §4.2 Specificity: BROAD (loose constraints)            │
  │                                                             │
  │  Analogy: knows "a puzzle piece is missing" but DOES NOT   │
  │  know the overall picture → only knows constraints from     │
  │  surrounding pieces (must be compatible with Newton AND     │
  │  Maxwell)                                                   │
  │                                                             │
  │  Body signal: mild dissonance — "something doesn't fit"     │
  │  Imagine-Final: fuzzy — "some unified framework"            │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASES 1-3 — OSCILLATION: reward + new dissonance (§7.5)  │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  MINI-ARC 1 — Photoelectric effect (1905):                  │
  │    Fill: photon model solves photoelectric → opioid ✅      │
  │    New chunks: [photon] + [wave-particle duality]           │
  │    New inconsistency: "photon model ≠ Maxwell continuous"   │
  │    Net: reward + MORE dissonance                            │
  │    Direction SHIFTS: "need something BROADER than just      │
  │    photoelectric"                                           │
  │                                                             │
  │  MINI-ARC 2 — Special relativity (1905):                    │
  │    Fill: time dilation, length contraction → opioid ✅✅    │
  │    New chunks: [spacetime] + [Lorentz] + [E=mc²]           │
  │    New inconsistency: "SR does NOT handle gravity"          │
  │    Net: bigger reward + BIGGER dissonance                   │
  │    Direction SHARPENS: "need a geometric theory of gravity" │
  │                                                             │
  │  MINI-ARC 3 — Grossman collaboration (1912-1914):           │
  │    Fill: tensor calculus tools → opioid ✅ ("this might fit")│
  │    New chunks: [tensor calculus] + [Riemannian geometry]    │
  │    New inconsistency: "equations close but NOT QUITE RIGHT" │
  │    Net: moderate reward + ACCUMULATED dissonance very high  │
  │                                                             │
  │  TREND across Phases 1-3:                                   │
  │    → Physics network: GROWS massively each year             │
  │    → Gap direction: SHARPENS (vague → "geometric gravity")  │
  │    → Total dissonance: ACCUMULATES (many valuable chunks    │
  │      not yet unified)                                       │
  │    → Body state: persistent mild-to-moderate dissonance     │
  │      + cortisol holding + forced Imagine-Final repetition   │
  │    → = Conditions for COMPOUND BREAKTHROUGH building        │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 4 — BREAKTHROUGH: November 1915                      │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Field equations complete:                                  │
  │    → 1 framework UNIFIES all accumulated chunks             │
  │    → NOT just filling 1 gap — resolves ALL accumulated      │
  │      mini-inconsistencies SIMULTANEOUSLY                    │
  │                                                             │
  │  Why reward is EXTREMELY INTENSE:                           │
  │    ① Chunk-Gap fill: unified framework found → opioid       │
  │    ② Chunk-Miss reverse: YEARS of "not found yet" → "HERE" │
  │    ③ Chunk-Shift: self-schema "I am the one who solved it"  │
  │    ④ Cortisol DROP: years of holding signal → RELEASED      │
  │    ⑤ Accumulated inconsistencies: ALL resolved at once      │
  │    = COMPOUND 5 dynamics → "intensely pleasant"             │
  │                                                             │
  │  ⭐ Reward ∝ accumulated_dissonance × time_pending           │
  │           × network_size × all-at-once_resolution           │
  │  = Years × massive network × compound                       │
  │  = COMPOUND EXPLOSION, not a single fill                    │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 4.5 — VERIFY CASCADE: reward IN LAYERS               │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  LAYER 1 — Self-verify (personal logic):                    │
  │    Einstein checks equations → "math is correct"            │
  │    Body: coherent internally → opioid ✅                    │
  │    BUT: still uncertain → residual anxiety                  │
  │                                                             │
  │  LAYER 2 — Friend-verify (Grossman, Besso, Hilbert):        │
  │    Share → they check → "makes sense"                       │
  │    Self-Pattern-Modeling: "people I respect ALSO see it     │
  │    as correct" → opioid ✅                                  │
  │    Trust dimension grows → residual anxiety decreases       │
  │                                                             │
  │  LAYER 3 — Community-verify (publish, peer review):         │
  │    Paper → physics community gradually confirms logic       │
  │    Each confirmation = one more layer of reward             │
  │    Trust dimension continues growing                        │
  │                                                             │
  │  LAYER 4 — Empirical-verify (1919 eclipse, Eddington):      │
  │    Light bends EXACTLY as predicted → reality itself confirms│
  │    Trust dimension MAXIMIZED: "no need to doubt anymore"    │
  │    = PEAK reward (Phase 5 > Phase 4 because Trust complete) │
  │    (04-Integration.md §6.6: Trust dimension analysis)       │
  │                                                             │
  │  Mechanism at each layer:                                   │
  │    ⓐ Residual uncertainty decreases → cortisol drops       │
  │    ⓑ Trust dimension grows (Anchor-Schema.md §2)            │
  │    ⓒ Self-schema reinforced: "I am TRULY correct"           │
  │    ⓓ Social reward: recognition, status (Path 2)            │
  │    = Reward is not a single moment — it is a CASCADE        │
  │      across many layers                                     │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 5 — "ADDICTION": PERPETUAL PURSUIT                   │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  After general relativity:                                  │
  │    Physics network: EXTREMELY LARGE (biggest ever for 1     │
  │    person at that time)                                     │
  │    → Large network → detect NEW inconsistency:              │
  │      "General relativity ≠ quantum mechanics"               │
  │    → NEW GAP: "unified field theory"                        │
  │    → = §7.5 oscillation: fill → new chunks → new gap       │
  │                                                             │
  │  WHY HE CANNOT STOP — 5 mechanisms lock:                    │
  │                                                             │
  │  ① NEW GAP INEVITABLE:                                      │
  │    Larger network → detect new inconsistency → new gap      │
  │    Questions NEVER END because each answer = more chunks    │
  │    = more detection capability (Novelty.md §5 combinatorial)│
  │                                                             │
  │  ② REWARD MEMORY (Background-Pattern):                      │
  │    Body compiled: [physics gap fill = MASSIVE opioid]       │
  │    Background-Pattern forms: [seeking in physics = who I am]│
  │    Body KNOWS: effort in domain → enormous reward possible  │
  │    = Extremely strong drive because reward history is deep  │
  │                                                             │
  │  ③ GAP→MISS TRANSITION:                                     │
  │    "Unified field theory" gap → Imagine-Final previews loop │
  │    Previews compile into baseline → body EXPECTS resolution │
  │    No resolution → Chunk-Miss CONTINUOUS → cortisol holding │
  │    = CANNOT STOP THINKING ABOUT IT                          │
  │                                                             │
  │  ④ IDENTITY LOCKED:                                         │
  │    Self-schema: "I am a physicist seeking unified theory"   │
  │    Stopping research = identity threat → massive dissonance │
  │    (Background-Pattern.md §10.4: Background-Pattern         │
  │    integrated into identity)                                │
  │                                                             │
  │  ⑤ DEPTH × SPECIFICITY TRAP:                               │
  │    Extremely deep network + extremely specific → very narrow │
  │    gap direction                                            │
  │    Very few possible fills → persistent → perpetual drive   │
  │    Einstein spent 30 YEARS (1925-1955) — never resolved     │
  │    = Gap too deep + too narrow → unresolvable within        │
  │      a lifetime → chronic pursuit                           │
  │                                                             │
  │  "ADDICTION" = SAME mechanism as addiction:                 │
  │    ① Reward history compiled deep → body expects reward     │
  │    ② Gap persistent → cortisol holding → can't stop         │
  │    ③ Identity locked → stopping = self-schema threat        │
  │    ④ Network grows → more gaps → more drive                 │
  │    DIFFERENCE from addiction: abstract gap fill SERVES      │
  │    body-base. Addiction: fill does NOT serve body-base.     │
  │    = Same mechanism, different outcome = Feature vs Bug     │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

### §10.5 — Other cases

```
🟡 OTHER CASES — ABSTRACT ACTIVITY × BODY-BASE:

  STUDENT WHO STUDIES INTENSELY:
    Gap: "better future" (Imagine-Final compiled)
    Direction: toward academic success → career → resources
    Path 1: each lesson = mini gap fill → micro opioid ✅
    Path 2: grades → opportunities → body-base future ✅
    ⚠️ IF studied under threat cortisol → Path 1 is poisoned
      (chunks compile with cortisol tag → "hate studying" despite still driving)

  CHARITABLE GIVING (giving only):
    Gap: Self-Pattern-Modeling fires → simulates recipient's need → body mirrors need ✅
    Direction: reduce another's suffering (gap via Compiled body simulation)
    Path 1: Self-Pattern-Modeling gap fill + oxytocin → body-state improves ✅
    Path 2: community standing → access → body-base ✅
    + Self-schema shift: "I am generous" → chunks compile → reward
    + Connection pathway ④ (Connection.md §8): giving = reward pathway
    = MULTIPLE reward channels override resource loss

  ARTIST CREATING:
    Gap: aesthetic vision not yet realized (creative gap)
    Direction: specific artistic expression
    Path 1: each creative step = mini gap fill → opioid ✅
    Path 2: art → recognition → resources (IF successful) ⚠️
    ⚠️ Path 2 uncertain → many artists persist
      BECAUSE Path 1 alone is strong enough
    = Explains "starving artist" = Path 1 reward > resource loss

  SOLVING A SUDOKU:
    Gap: each empty cell = mini gap (network predicts specific number)
    Direction: VERY specific (number X in cell Y)
    Fill each cell → micro opioid. Complete → compound reward.
    → For someone who doesn't know Sudoku → no chunks → no gap → no drive ✅
    = Almost purely Path 1 — demonstrates abstract gap fill
      serving body-base DIRECTLY without external outcome
```

---

## §11 — EXAMPLES (organized by property tested)

### §11.1 — Group A: "Not knowing = no gap"

```
🟡 TEST: No chunks → no gap → no desire → no reward

  A1. 3-YEAR-OLD RECEIVES THE LATEST iPHONE:
    Chunks about smartphone: ≈ 0
    Gap about iPhone: IMPOSSIBLE (no surrounding chunks)
    Receives it → curious (press → light comes on = sensory novelty)
    BUT: no "pleasant because I have an iPhone" → gap does not exist
    → Parent: rich chunks → gap → pleasant
    → SAME object, DIFFERENT gap existence → DIFFERENT reward ✅

  A2. PERSON WHO DOESN'T KNOW CHESS RECEIVES EXPENSIVE CHESS SET:
    Chunks about chess: ≈ 0 → no gap "want a beautiful chess set"
    Receives it → "oh, beautiful" (visual novelty) but no deep reward
    → 10-year player: gap "quality chess set" → pleasant ✅

  A3. AMAZON INDIGENOUS PERSON RECEIVES A LAPTOP:
    Digital technology chunks: ≈ 0 → concept doesn't exist
    Receives it → curiosity → might use it as a cutting board
    → Gap about "laptop": IMPOSSIBLE ✅

  A4. NEVER HEARD JAZZ, GIVEN JAZZ CONCERT TICKET:
    Jazz chunks: minimal (label only) → gap nearly non-existent
    → 20-year jazz lover: specific gap → intensely pleasant ✅

  CONCLUSION: All 4 cases confirm — no chunks = no gap = no reward
```

### §11.2 — Group B: "Same object, wrong direction"

```
🟡 TEST: Direction mismatch → no reward despite category match

  B1. LOVES MATH, GIVEN AN EXPENSIVE LITERATURE BOOK:
    Gap direction: "a great math book" (rich math chunks)
    Literature book: category "book" ✅ but direction "math" ❌
    → Mild appreciation but no gap-fill reward ✅

  B2. THIRSTY, GIVEN DELICIOUS FOOD:
    Gap direction: "water" (Tier 1 dehydration → specific)
    Food: satisfies hunger but MISSES thirst direction
    → Body STILL signals "thirsty" even after eating ✅

  B3. WANTS A RED CAR, GIVEN SAME MODEL IN BLUE:
    Gap direction: model X + RED (narrow specificity)
    Blue car: 90% match but misses 10% (color dimension)
    → Reward IS there but with a "but..." feeling = partial direction match ✅

  B4. LOVES BEEF PHO, OFFERED CHICKEN PHO:
    Gap direction: "beef pho" (specific compiled preference)
    Chicken pho: "pho" ✅ but "beef" ❌
    → Partial reward + mild disappointment (missed direction) ✅

  CONCLUSION: Direction match required — category match NOT sufficient
```

### §11.3 — Group C: "More ≠ better" (range exceeded)

```
🟡 TEST: Correct direction but BEYOND range → diminished/negative

  C1. MASSAGE:
    Direction: relaxation (Tier 1)
    Range: light → pleasant → slightly painful → PAIN (bell curve)
    → Extreme pressure: correct direction but EXCEEDS range → nociception ✅

  C2. MUSIC VOLUME:
    Direction: auditory enjoyment (Tier 1)
    Range: quiet → ideal → exciting → EAR PAIN
    → Extreme volume: cochlear damage → nociception overrides ✅

  C3. MONETARY REWARD:
    Direction: resource reward
    Range: $100 → $1,000 → $100,000 → $100 billion ❌
    → $100 billion: "I don't believe it" → Precondition-4 violated
      (mismatch with self-schema) ✅

  C4. PRAISE:
    Direction: recognition (self-schema relevant)
    Range: "Good work" → "Very talented" → "Genius" → "The next Einstein" ❌
    → "The next Einstein": body rejects (self-schema mismatch too large) ✅

  C5. EATING CANDY:
    Direction: sweet taste (Tier 1)
    Range: 1 → 5 → 10 → 100 pieces ❌
    → 100 pieces: receptor saturation + nausea + blood sugar alarm ✅

  C6. FOOD SEASONING:
    Direction: taste enhancement (Tier 1)
    Range: bland → balanced → delicious → too salty/spicy → PAIN
    → 10× spice: nociception overrides taste reward ✅

  CONCLUSION: Bell curve per dimension — more ≠ better, even in correct direction
```

### §11.4 — Group D: "Abstract gap fill"

```
🟡 TEST: Abstract activity fills gap → body reward despite no direct survival value

  D1. SOLVING A SUDOKU:
    Gap: each empty cell = mini gap, network predicts specific number
    Direction: "number X in cell Y" (very specific, very narrow)
    Fill each cell → micro opioid. Complete → compound reward.
    → For someone who doesn't know Sudoku → no chunks → no gap → no drive ✅

  D2. READING A NOVEL:
    Gap: "what happens next?" (plot creates directed gap)
    Direction: character fate prediction (Self-Pattern-Modeling-based)
    Plot twist → prediction wrong → prediction-delta → new gap → fill → reward
    → Author = gap direction engineer (create→fill→create loop) ✅

  D3. COLLECTING STAMPS:
    Gap: "stamp X from year Y" (extremely narrow direction)
    Fill: find specific stamp → gap fill → opioid
    Complete set = all gaps closed = massive compound
    → Outsider: "just old stamps" → no chunks → no gap → no reward ✅

  D4. PLAYING AN RPG:
    Gap: quests, levels, items = engineered gap system
    Direction: game designers CREATE gap directions deliberately
    Level up → self-schema shift (avatar = proxy self) → reward
    → Game = artificial gap-direction factory ✅

  CONCLUSION: Abstract gaps use SAME mechanism — gap fill → opioid
  regardless of survival relevance
```

### §11.5 — Group E: "Paradoxical reward"

```
🟡 TEST: Reward where a naive model predicts NO reward

  E1. WATCHING A SAD FILM → CRYING → BUT "WONDERFUL":
    Compiled Self-Pattern-Modeling: body simulates character → genuine sadness
    Gap: about the human condition → film articulates → gap fills
    + Safety frame: "this is a film" → body processes risk-free
    = Sad (body simulation) + reward (gap fill) + safety → MIXED ✅

  E2. EATING CHILI PEPPERS (CAPSAICIN):
    Nociceptors fire → PAIN signal
    Body responds: endorphin release → opioid
    + Compiled chunks after exposure: [spicy = pleasant after pain]
    → First time: NOT pleasant (not yet compiled)
    → After exposure: direction SHIFTS: [spicy → endorphin → pleasant] ✅

  E3. GOING TO THE GYM WITH MUSCLE SORENESS:
    Exercise: nociception (muscle strain)
    After exercise: endorphin + sense of accomplishment
    Imagine-Final: fit body → gap "body now vs desired body"
    Each session = partial gap fill toward Imagine-Final ✅

  E4. GIVING MONEY TO A STRANGER (CHARITY):
    Body loses resources → naive model: should be NEGATIVE
    Compiled Self-Pattern-Modeling → simulates recipient happy → body mirrors → opioid
    + Connection pathway ④ (giving reward)
    + Self-schema: "I am generous" → positive shift
    + Community mechanism: giving → others value you → access
    = MULTIPLE reward channels > resource loss ✅

  CONCLUSION: Paradoxical rewards explained — multiple gaps/channels
  interact, not just "stimulus → single response"
```

### §11.6 — Summary matrix

```
  ┌─────────┬───────────────────────────────────┬─────────────┐
  │ Group   │ Test                              │ Confirmed?  │
  ├─────────┼───────────────────────────────────┼─────────────┤
  │ A (4)   │ No chunks → no gap → no reward   │ ✅ All 4    │
  │ B (4)   │ Wrong direction → no reward       │ ✅ All 4    │
  │ C (6)   │ Beyond range → diminished/neg.    │ ✅ All 6    │
  │ D (4)   │ Abstract gap fill → body reward   │ ✅ All 4    │
  │ E (4)   │ Paradoxical → multi-channel       │ ✅ All 4    │
  ├─────────┼───────────────────────────────────┼─────────────┤
  │ TOTAL   │ 22 examples tested                │ ✅ All 22   │
  └─────────┴───────────────────────────────────┴─────────────┘

  No counter-examples found.
```

---

## §12 — GAP DIRECTION × INTER-BODY: BY-PRODUCT MATCH + 2-STREAM (★ NEW v2.0)

### §12.1 — Gap direction = foundation for by-product match

```
⭐⭐ BY-PRODUCT MATCH ONLY WORKS BECAUSE OF GAP DIRECTION:

  Inter-Body-Mechanism.md §5.4:
    "Entity B fills B's gap → output = by-product"
    "When by-product matches A's gap direction → A receives reward"

  ANALYSIS THROUGH GAP DIRECTION:
    → "Match" = B's output fits THE SPECIFIC SHAPE of A's gap
    → NOT "B did something nice" (vague)
    → = B's output matches A's gap DIRECTION + SPECIFICITY + RANGE
    → = Gap direction is THE EVALUATOR for by-product match

  WHY GAP DIRECTION IS NEEDED TO UNDERSTAND BY-PRODUCT MATCH:

    ① WITHOUT gap direction: "B output → A rewards" = magic
       → Why does SAME output from B → A1 rewards, A2 nothing, A3 annoyance?
       → = No explanatory mechanism

    ② WITH gap direction: "B output matches A's specific direction → A rewards"
       → A1 rewards: B's output matches A1's gap direction ✅
       → A2 nothing: B's output irrelevant to A2's gap directions
       → A3 annoyance: B's output CONFLICTS with A3's gap direction (anti-match)
       → = CLEAR mechanism. Testable. Per-person.

  TRIPLE-CASE EXAMPLE:
    B = a singer performing live
    B's gap: "want to perform, want audience to like it" → action = sing
    B's output = the performance (by-product of filling B's gap)

    A1 (10-year fan): gap direction = "hear song Y live from this singer"
      → Output matches direction EXACTLY → massive reward ✅
    A2 (came along with a friend, doesn't know the artist): gap direction ≠ music domain
      → Output = irrelevant → no gap-fill reward (maybe mild novelty)
    A3 (neighbor wanting a quiet evening): gap direction = "quiet evening"
      → Output = loud music → CONFLICTS direction → annoyance (anti-match) ❌

    = SAME output (the performance). 3 DIFFERENT gap directions. 3 DIFFERENT outcomes.
    = Gap direction = THE mechanism explaining selectivity of by-product match.


  ⭐ ANTI-MATCH = NOT JUST "NO MATCH" — ACTIVE DIRECTION CONFLICT:

    No-match: B's output irrelevant to A's gap (neutral — no reward, no harm)
      Example: singer performs → someone who doesn't care → nothing happens

    Anti-match: B's output ACTIVELY OPPOSES A's gap direction
      Example: innovation-focused CEO → employee gap "stability" → change = THREATENS stability
      Example: extrovert being loud → introvert gap "quiet" → noise = CONFLICTS direction

    Anti-match is WORSE than no-match:
      → No-match = 0 reward (neutral)
      → Anti-match = NEGATIVE (active dissonance, threat signal)
      → = Output pushes A FURTHER from gap fill
      → = Body-feedback: dissonance + possible cortisol (if persistent)

🟡 Gap direction as by-product match foundation = framework synthesis.
   Each component established separately — integration = contribution.
```

### §12.2 — 2-Stream Architecture × Gap Direction

```
⭐ HARDWARE-STREAM AND MODELING-STREAM = 2 TYPES OF GAP DIRECTION MATCH:

  (By-Product-Gap-Resonance.md v1.0 §2)

  HARDWARE-STREAM × GAP DIRECTION:
    = Hardware-level gap directions matched by EXISTENCE/ATTRIBUTES

    Mechanism:
      Entity B EXISTS / HAS ATTRIBUTE X
      → X matches A's gap direction (hardware or compiled)
      → A rewards
      B NEED NOT DO ANYTHING.

    Gap directions involved:
      → Tier 1 (hardware): baby schema, sexual attractiveness, voice timbre
      → Tier 2-3 (compiled): status patterns, aesthetic preferences
      → Direction evaluation: mostly COMPILED (automatic hardware check)

    Properties:
      → UNIDIRECTIONAL: A has gap, B's existence fills it. No loop.
      → HABITUATES: constant stimulus → Weber-Fechner → direction "fades"
        (body adjusts baseline → same stimulus = smaller delta)
      → MULTI-CHANNEL: beauty + voice + smell = multiple directions matched

    Examples:
      Husband gap "aesthetic pleasure" → wife is attractive = Hardware-Stream match
      Mother gap "caregiving fulfillment" → baby is cute (baby schema) = Hardware-Stream match
      Fan gap "novelty + beauty" → singer's performance = Hardware-Stream match


  MODELING-STREAM × GAP DIRECTION:
    = Self-Pattern-Modeling-mediated gap directions matched by ACTIONS (mutual)

    Mechanism:
      A's Self-Pattern-Modeling detects B's state → A responds appropriately
      → A's RESPONSE = by-product of A filling A's gap "understand B"
      → A's response matches B's gap direction "be understood"
      → B rewards → B responds → B's response matches A's gap "be understood in return"
      → = MUTUAL by-product match via Self-Pattern-Modeling-mediated actions

    Gap directions involved:
      → Tier 2-4 (compiled): understanding, emotional resonance, shared meaning
      → Direction evaluation: Compiled (experts in each other) or
        Fresh (still learning each other)

    Properties:
      → BIDIRECTIONAL: BOTH must match each other's gap directions
      → ANTI-HABITUATION: Hebbian → more practice → better match → MORE reward
        (direction matching IMPROVES → reward INCREASES over time)
      → Can CHANGE gap direction: deep Modeling-Stream → A can help B see new gaps
        ("a close friend says one sentence that shifts your whole perspective"
        = installs chunks → new direction)

    Examples:
      Close friend A: gap "be understood without having to explain everything"
        → B Compiled Self-Pattern-Modeling → responds EXACTLY matching → A massive reward
      Therapist: gap direction "help client see clearly"
        → Client Self-Pattern-Modeling reciprocates → therapist rewards (mutual Modeling-Stream)


  TEMPORAL DYNAMIC:
    Hardware-Stream: PEAKS EARLY → habituates (hedonic treadmill)
    Modeling-Stream: ZERO at start → grows → deepens → can become STRONGEST

    Total direction-match reward = Hardware-Stream + Modeling-Stream (independent, parallel)
    Sustainable relationships: Modeling-Stream growth > Hardware-Stream decline
    Failing relationships: Hardware-Stream habituated + Modeling-Stream never developed

🟡 2-Stream × gap direction = framework synthesis.
   Hedonic adaptation (Hardware-Stream) = 🟢.
   Interpersonal synchrony (Modeling-Stream) = 🟢 (Feldman 2007, Coan & Sbarra 2015).
```

### §12.3 — Compilable Architecture × Gap Direction: general-purpose evaluation

```
⭐ COMPILABLE ARCHITECTURE = WHY GAP DIRECTION IS NOT FIXED:

  (Inter-Body-Mechanism.md §1, Body-Base.md v3.1)

  Hardwired Architecture (insects):
    → Hardwired reward: flower wavelength X → approach
    → Gap direction = FIXED by genes per species
    → ALL members = SAME gap directions (bee 1 = bee 2)
    → = CANNOT explain personal reward differences

  Compilable Architecture (humans):
    → General-purpose reward: ANY compiled gap fill → reward
    → Gap direction = EMERGES from accumulated chunk network
    → Each person = UNIQUE gap directions (different chunks compiled)
    → = EXPLAINS personal reward differences PERFECTLY

  IMPLICATIONS FOR INTER-BODY:
    → Compilable Architecture = WHY by-product match is SELECTIVE
      (each person has different directions → different matches)
    → Compilable Architecture = WHY relationships are PERSONAL
      (my directions overlap SOME people, not others)
    → Compilable Architecture = WHY cultural bonding works
      (shared chunk install → shared directions → easier match)
    → Compilable Architecture = WHY diversity is valuable
      (different directions → different outputs → richer by-product landscape)

  INTER-BODY CONSEQUENCE:
    → A and B have gap directions determined by THEIR chunk networks
    → Match probability = f(overlap in gap direction landscape)
    → Species hardware = SOME overlap guaranteed (Tier 1 shared)
    → Culture = ADDITIONAL overlap (Tier 2-3 shared install)
    → Personal experience = DIVERGENCE (Tier 4 individual)
    → = Why "same group but DIFFERENT connection depth" = different Tier 4 overlap
```

### §12.4 — 3 Independent Cost Sources × Gap Direction

```
🟡 3-COST MODEL APPLIES TO GAP DIRECTION EVALUATION:

  (Inter-Body-Mechanism.md §4)

  WHEN EVALUATING BY-PRODUCT MATCH:

    ① PFC DRAFT COST — "Does B's output match my direction?"
       → If COMPILED: cost ≈ 0 (body knows instantly)
         Example: close friend speaks → body KNOWS match or not (milliseconds)
       → If FRESH: cost HIGH (PFC must build evaluation)
         Example: stranger's proposal → PFC analyzes fit (seconds-minutes)
       → = Expert in the relationship → lower evaluation cost

    ② SUPPRESS COST — "Output misses my direction → must suppress reaction"
       → Anti-match → body fires dissonance → urge to react (withdraw/fight)
       → Social context requires suppression → PFC override → processing load
       → Example: CEO change → employee suppresses frustration daily = costly
       → = Chronic direction-mismatch + suppress = burnout trajectory

    ③ UNCERTAINTY COST — "Will B's output match my direction?"
       → Unknown entity: can't predict → cortisol
       → Known entity: predict accurately → low uncertainty
       → = WHY familiar = comfortable (direction-match is predictable)
       → = WHY new = stressful even if ultimately beneficial

  SUSTAINABILITY:
    → All 3 costs low = sustainable interaction (close friend, compiled)
    → High ① = new territory (learning phase — acceptable if temporary)
    → High ② = chronic mismatch (→ burnout, need to exit)
    → High ③ = instability (→ anxiety until resolved)
    → = Gap direction match QUALITY determines interaction sustainability
```

### §12.5 — Input Channel Control × Gap Direction

```
🟡 5-CHANNEL INPUT VECTOR DETERMINES WHICH GAP DIRECTIONS ACTIVATE:

  (Inter-Body-Mechanism.md §6)

  5 CHANNELS:
    Ch1: Hardware Sensory (visual, auditory, touch, smell, taste)
    Ch2: Body State (hunger, fatigue, hormone level)
    Ch3: Compiled Chunks (activated patterns from memory)
    Ch4: Entity Actions (other entities' observable behaviors)
    Ch5: PFC Active Chain (deliberate thoughts, plans, predictions)

  × GAP DIRECTION:
    → Gap direction activation DEPENDS on which channels are active
    → Ch1 dominant (sensory-rich): Tier 1 gap directions activate
      Example: live concert → auditory → Tier 1 aesthetic gaps fire
    → Ch3 dominant (memory-triggered): Tier 2-4 gap directions activate
      Example: reunion → compiled friend-chunks fire → Modeling-Stream gaps activate
    → Ch4 dominant (entity-focused): by-product match evaluation active
      Example: observe B's actions → evaluate match/mismatch to my directions
    → Ch5 dominant (PFC-driven): abstract gap directions active
      Example: planning → Tier 4 career/knowledge gaps fire

  INTER-BODY APPLICATION:
    → Entity B primarily enters via Ch1 + Ch4 (perceive + observe actions)
    → WHICH gap directions B can match = limited by available channels
    → Text-only communication: Ch5 dominant, Ch1 minimal
      → Can only match abstract/intellectual gap directions
    → In-person: Ch1 + Ch3 + Ch4 full → match wider range of directions
      → Hardware-Stream (Ch1: beauty, voice) + Modeling-Stream (Ch4: responsive actions)
    → = WHY in-person > text for deep bonding (more channels = more matches)

  MANIPULATION = CONTROLLING CHANNELS TO DISTORT GAP DIRECTION:
    → Propaganda: Ch4 (social proof) + Ch5 (arguments) → install specific direction
    → Advertising: Ch1 (beauty) + Ch4 (influencer) → associate product with direction
    → Gaslighting: Ch4 (entity actions) + Ch5 (reframe) → distort existing directions
    → = Power = control over WHICH directions get activated
    → = Inter-Body-Mechanism.md §6: "Input Channel Control = Power"
```

---

## §13 — IMPLICATIONS

### §13.1 — Education

```
🟡 EDUCATION MUST BUILD CHUNKS FIRST, PRESENT ANSWERS SECOND:

  COMMON CURRENT APPROACH:
    → Teacher presents answer → students note it down → test
    → = "Giving the answer before there is a question" → no gap → no reward → boring

  GAP DIRECTION APPROACH:
    ① Build chunks: introduce concepts, examples, experiences
    ② Create conflict: show inconsistency, pose a problem
    ③ Gap emerges: student FEELS "something is missing" (direction forms)
    ④ Present tools: guide toward answer (not give the answer)
    ⑤ Student fills gap: discovery → opioid → intrinsic motivation
    → = Gap direction mechanism = natural curiosity driver
    → = "Build the question before giving the answer"
```

### §13.2 — Therapy

```
🟡 THERAPY = MAP AND EXPAND THE GAP LANDSCAPE:

  DIAGNOSIS: Map client's gap direction landscape
    → Which gaps are active? (what they want)
    → Which gaps are suppressed? (what Background-Pattern prevents)
    → Which gap directions are distorted? (Background-Pattern contamination)

  INTERVENTION:
    → Build new chunks → expand gap landscape possibilities
    → Identify Background-Pattern constraints → build competing patterns
    → Sharpen fuzzy directions → Imagine-Final refinement
    → = Therapy does NOT "fix" gaps — therapy ENABLES new gaps

  Example: Client "wants happiness but doesn't know what specifically":
    → = Fuzzy gap direction (sparse or conflicted network)
    → Therapy: explore → build chunks → direction sharpens
    → NOT: prescribe "happiness = X" (installing someone else's direction)
```

### §13.3 — Marketing (ethical vs exploitative)

```
🟡 UNDERSTANDING GAP INSTALL → UNDERSTANDING MARKETING:

  ETHICAL MARKETING:
    → Product GENUINELY fills a real gap → honest direction install
    → Example: "You have problem X → product solves X" → gap direction = X → fill = product

  EXPLOITATIVE MARKETING:
    → Creates ARTIFICIAL gap → fills with unnecessary product
    → Example: "You lack status" → install [status = product X] → purchase X
    → Gap was manufactured, not a genuine body-need

  CONSUMER DEFENSE:
    → Recognize: "Am I buying because the GAP is REAL or INSTALLED?"
    → "Not knowing = no gap": before the ad, I had NO desire → the ad INSTALLED the gap
    → = Awareness of the mechanism = partial immunity
```

### §13.4 — Parenting

```
🟡 PARENTING: UNDERSTANDING CHILD'S GAP DIRECTION ≠ PARENT'S:

  Car Paradox (03-Reward.md §5):
    → Father loves vintage cars (father's gap direction)
    → Child wants a trendy car (child's gap direction)
    → Father buys a vintage car = fills FATHER'S gap, MISSES child's gap

  PRINCIPLE:
    → Gift = by-product of parent filling PARENT'S gap
      ("want child to be happy" → buy what parent finds valuable)
    → Gap direction mismatch → gift MISSES → confusion, not ingratitude
    → = NOT "child is ungrateful" — parent's direction ≠ child's direction

  BETTER APPROACH:
    → Observe child's chunk network: what has compiled, what direction is pointing
    → Ask directly OR provide experiences → let child's direction reveal itself
    → = Gift that fills CHILD'S gap direction = genuine reward

  CAUTION:
    → Parent can INSTALL gap direction (via chunk install)
    → "You should want X" repeated → chunks compile → gap forms → child wants X
    → = Gap direction can be GIVEN, but what serves child's body-base?
    → = Ethical install: X genuinely serves child. Unethical: X serves parent.
```

### §13.5 — Self-knowledge

```
🟡 "WHAT DO I WANT?" = MAP MY OWN GAP LANDSCAPE:

  COMMON CONFUSION:
    → "I don't know what I want" = fuzzy gap directions (sparse network or PFC
      hasn't articulated body-level direction)
    → NOT = "no gaps" (gaps EXIST at body level; PFC just hasn't labeled them)

  HOW TO DISCOVER:
    ① Notice body reactions: what makes body "light up"?
      → = Compiled evaluation (fast, accurate if chunks are rich)
    ② Notice accumulation patterns: what topics do you spontaneously return to?
      → = Active gaps (persistent signal)
    ③ Notice dissonance: what bothers you repeatedly?
      → = Gaps being blocked or missed

  WHY "FOLLOW YOUR PASSION" PARTIALLY WORKS:
    → "Passion" = active gap with direction, accumulated over years
    → Following it = filling gap that body genuinely wants filled
    → Problem: "passion" can also be Background-Pattern-driven (avoidance-tagged pursuit)
    → = More precise: "Follow directions where body BOTH wants AND approach-tagged chunks"
```

---

## §14 — OPEN QUESTIONS

```
Q1: Gap direction threshold — when does direction become "clear enough" to evaluate?
  → Network sparse → direction too vague → body cannot meaningfully evaluate match
  → Threshold for "direction is formed enough" = unclear
  → Possible marker: when body can "recognize" a fill ("this is it!") = direction crossed threshold

Q2: Conflicting gap directions — when A and B directions pull opposite ways?
  → Example: "want status" + "want authenticity" → both active, conflicting
  → Body computes NET? Takes the stronger one? Oscillates?
  → Background-Pattern.md §10 suggests: both fire simultaneously → ambivalence
  → Mechanism not yet fully mapped

Q3: Gap direction across cultures — is there a cross-cultural "core"?
  → Tier 1 = universal (hardware). But Tier 2-3 = cultural.
  → Is there a Tier 1.5 — near-universal but compiled, not genetic?
  → Example: "shelter", "community", "meaning" — universal or cultural?

Q4: Gap direction install ethics — at what point does install cross into manipulation?
  → Education: generally ethical (fills genuine body-base needs via skills)
  → Advertising: often engineering desire that serves company, not body-base
  → Line = whether fill GENUINELY serves body-base
  → But "genuine" is contested — who determines?

Q5: Imagine-Final over-specification — can it be measured?
  → Gap direction narrows with Imagine-Final loops → harder to satisfy
  → Is there a measurable threshold of "over-specification"?
  → Treatment: deliberately broaden Imagine-Final → relax specificity?
```

---

## §15 — HONEST ASSESSMENT

### §15.1 — What is well-supported

```
🟢 HIGH CONFIDENCE:
  → Gap = hole in network (§3.3) = framework established
  → Surrounding chunks determine what counts as a valid fill = logical necessity
  → "Not knowing = no gap" principle = strongly supported (no counter-examples found)
  → Direction properties (direction/specificity/depth/range) = logically derived
  → Tier 1-4 origin hierarchy = consistent with chunk substrate model
  → Einstein case = consistent with all mechanism claims
  → 22 examples tested — all consistent, 0 counter-examples found

🟢 RESEARCH SUPPORT (underlying mechanisms):
  → VTA prediction error (Schultz 1997): Layer 1 signal mechanism
  → ACC inconsistency detection (Bush et al. 2000): gap detection
  → Compiled/Fresh dual process (Kahneman 2011): evaluation spectrum
  → Hedonic adaptation (Frederick & Loewenstein 1999): Hardware-Stream habituation
  → Expertise gradient (Chi et al. 1981): direction specificity with chunks
  → Music inverted-U (Chmiel & Schubert 2017): gap direction + range
  → Interpersonal synchrony (Feldman 2007): Modeling-Stream foundation
```

### §15.2 — What is framework synthesis

```
🟡 MODERATE CONFIDENCE (framework-level claims):
  → "Gap direction = necessary consequence of gap = hole in network" — logically derived,
    but direct empirical test of "gap direction" as a construct = not yet done
  → 2-layer model (signal mechanism vs direction content) = synthesized framework;
    each layer individually supported 🟢, but 2-layer separation as a formal model =
    framework synthesis
  → By-product match = gap direction evaluation — logically consistent, not yet empirically tested
  → Compilable Architecture × gap direction = framework integration across multiple files
  → Gap direction × Background-Pattern — logically consistent with both constructs,
    cross-construct integration = framework synthesis
```

### §15.3 — What is hypothesis-level

```
🔴 LOW CONFIDENCE (hypothesis):
  → Precise threshold for gap direction formation (Q1 above) = unknown
  → Conflicting gap directions computation mechanism (Q2) = not mapped
  → Cross-cultural "Tier 1.5" near-universal directions (Q3) = speculative
  → Measurable Imagine-Final over-specification threshold (Q5) = not yet formalized
```

---

## §16 — CROSS-REFERENCES

### §16.1 — Foundation files

| File | Relevant section | Relationship |
|---|---|---|
| Body-Feedback-Mechanism.md v2.0 | §3.3 Chunk-Gap | This file formalizes the SHAPE of the hole §3.3 defines |
| Body-Feedback.md v2.0 | §6 Preconditions | §6.3 reinterprets Preconditions through 2-layer model |
| 03-Reward.md | §5.9 Car Paradox | This file provides the mechanism underneath personalized reward |
| Chunk.md v2.0 | §2 compile dynamics | Foundation for all direction claims |

### §16.2 — Sibling files

| File | Relevant section | What it covers |
|---|---|---|
| Body-Feedback-Precondition.md v1.0 | §1 Formal Statement, §5-§6 | Precondition-1 Directed-Gap + Precondition-4 Match-Range + §6.3 hierarchy |
| Body-Feedback-Label.md v2.0 | §8 | Compiled/Fresh vocabulary |
| Reward-Signal-Architecture.md | §1 | Evaluative/Direct-State × direction matching |

### §16.3 — v2.0 new connections

| File | Relevant section | v2.0 addition |
|---|---|---|
| Inter-Body-Mechanism.md v1.0 | §5.4, §6 | By-product match foundation + 5-channel input |
| By-Product-Gap-Resonance.md v1.0 | §2 | 2-Stream Architecture × gap direction |
| Body-Base.md v3.1 | §3 Compilable Architecture | General-purpose reward × gap direction diversity |
| Self-Pattern-Modeling v3.0 | Compiled/Fresh | Modeling-Stream evaluation mechanism |

### §16.4 — Constraint files

| File | Relevant section | Relationship |
|---|---|---|
| Background-Pattern.md v1.0 | §10 resolution | Background-Pattern constrains which gaps can form (§9) |
| Imagine-Final.md | preview mechanism | Gap→Miss transition + direction sharpening (§7.2) |
| Cortisol-Baseline.md v2.0 | §3.3 direction tag | Cortisol source determines gap direction valence |
| Novelty.md v1.0 | §5 DRD4 breadth | Chunk-Gap = novelty foundation, breadth/depth trade-off |
