---
title: "Schema.md v2.0 — Schema as Observation Parameter"
source: Schema/Schema.md
created: 2026-03-25 (v1.0 DRAFT)
updated: 2026-04-20 (v2.0 REWRITE — observation parameter reframe per v7.8)
status: v2.0 COMPLETE
scope: |
  Schema = observation parameter, NOT architectural component.
  Schema = named chunk-network pattern = a way of OBSERVING, not a way the BRAIN
  OPERATES.
  This file defines: what schema is, why it is useful, observable properties,
  interaction with body-feedback/PFC/domain, and limits.
previous_version: Schema/backup/ (v1.1 content redistributed)
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, observation parameters
  - Chunk.md v2.0 — chunk substrate (sole substrate)
  - Body-Feedback.md v1.1 — dual-pull, Body-Feedback-Precondition, interface loop
  - Body-Feedback-Mechanism.md v1.0 — chunk dynamics (Shift/Miss/Gap)
  - Feeling.md v2.0 — PFC observation interface
  - Cortisol-Baseline.md v2.0 — amplifier, direction gate
  - Valence-Propagation.md v1.1 — valence per-entity + chain
  - Anchor-Schema.md v1.2 — sync point, trust binding
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
english_created: 2026-06-07
---

# Schema — Observation Parameter

> **In software: "function" = actual computational unit. "Feature" = a description
> of software from the outside.**
> **In the brain: chunks = actual computational units. Schema = a description of
> chunk networks from the outside.**
>
> Schema is NOT an architectural component.
> Schema = named chunk-network pattern — an observation label.
> Useful for description, prediction, communication.
> But body-base does NOT "run schemas" — body-base runs CHUNKS.
>
> This file defines schema within the v7.8 cycle-based architecture.

---

## Table of Contents

- §0 — WHY REFRAME
- §1 — WHAT IS SCHEMA IN V7.8
- §2 — SOFTWARE ANALOGY
- §3 — VALUE OF SCHEMA AS OBSERVATION PARAMETER
- §4 — OBSERVABLE PROPERTIES
- §5 — SCHEMA × BODY-FEEDBACK
- §6 — SCHEMA × PFC
- §7 — SCHEMA × DOMAIN
- §8 — BODY BASELINE STATE
- §9 — OPEN QUESTIONS
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

---

## §0 — WHY REFRAME

### §0.1 Schema in v1.1

```
V1.1 (2026-03-25 → 2026-04-18):
  → Schema = "stabilized neural oscillation pattern (compiled)"
  → Schema = SOFTWARE running on HARDWARE (neurons)
  → Schema System = architectural component (same tier as Drive, Layer)
  → Chunks = "bricks", Schema = "the building"

  Problems:
  ① Schema LOOKS like a separate component → but is actually = chunks + links
  ② "Compiled schema" → implies schema IS something → actually chunks compiled
  ③ 3 states (compiled/active/monitor) → actually = chunk activation states
  ④ Schema-schema interaction → actually = chunk spreading activation
  → = EVERYTHING schema "does" = chunks do it. Schema is just a NAME.
```

### §0.2 Deep drill revealed

```
63,000+ lines of drill (44+ files, 2026-03 → 2026-04) yielded consistent results:

  Chunk.md v2.0: "Brain = database + 2 operators" → chunks = sole substrate
  Body-Feedback.md: "6-step interface loop" → cycle, not components
  Agent.md: "Agent = function on chunk substrate" → not a separate category
  Feeling.md v2.0: "PFC observation of body-chunk interaction" → interface
  Drive.md v1.1: "Schema = DETECTOR, drive = emergent" → observation label
  Core-v7.8-Draft.md §0.2: 9/9 files compatible with reframe

  → Schema = observation label for chunk network patterns
  → Like "feature" in software: describes from the outside, not internal structure
```

### §0.3 What v2.0 is

```
V2.0 REFRAME:
  → Schema = OBSERVATION PARAMETER (same group as: Novelty, Status, Protect, ...)
  → Body-base runs ENTIRELY on chunks
  → Schema = the way HUMANS OBSERVE chunk network patterns
  → Still USEFUL — but must know this is a lens, not reality

  UNCHANGED:
  → Observable properties (depth, activation, decay, override) remain VALID
  → Examples remain valid (love lifecycle, burnout, trauma cross-contamination)
  → Only STATUS changes: from "component" → "observation parameter"
```

---

## §1 — WHAT IS SCHEMA IN V7.8

### §1.1 Definition

```
⭐ SCHEMA = NAMED CHUNK-NETWORK PATTERN:

  Schema = a collection of linked chunks + shared purpose + NAME

  Chunks [press brake] + [check mirror] + [steer] + [observe traffic] + ...
    + links between them
    + purpose: "move safely"
    = the pattern we CALL "driving"

  Schema does NOT EXIST as a separate entity in the brain.
  Schema = the NAME that PFC (or an external observer) GIVES
  to an observable chunk network pattern.

  CHUNK = atom (actual computational unit, fires in the brain)
  SCHEMA = molecule (name for a group of linked atoms)
  ATOMS EXIST PHYSICALLY → molecule = how we DESCRIBE the combination of atoms

  🟡 Key reframe:
  → "Schema fires" = chunks in that network fire
  → "Schema compiled" = chunks in that network have been strengthened
  → "Schema conflict" = 2 chunk groups fire in opposite directions
  → "Schema update" = chunk links in the network re-weight
  → EVERY "schema operation" = chunk operation + observation label
```

### §1.2 Schema vs. Chunk — clear distinction

```
┌─────────────────┬────────────────────────────────────────────┐
│                 │ Chunk                                       │
├─────────────────┼────────────────────────────────────────────┤
│ Ontology        │ PHYSICALLY EXISTS (neurons wired)          │
│ Level           │ Atom — smallest unit                        │
│ Fires           │ ACTUALLY fires in brain (measurable)        │
│ Mechanism       │ LTP, spreading activation, compile          │
│ Classification  │ CANNOT classify all (infinite)              │
│ Examples        │ [red], [hot], [mother-face], [foot-brake]   │
└─────────────────┴────────────────────────────────────────────┘

┌─────────────────┬────────────────────────────────────────────┐
│                 │ Schema                                      │
├─────────────────┼────────────────────────────────────────────┤
│ Ontology        │ OBSERVATION LABEL (name for pattern)       │
│ Level           │ Molecule — name for a combination of atoms  │
│ Fires           │ "Fires" = chunks in the network fire        │
│ Mechanism       │ NO mechanism of its own                     │
│ Classification  │ CAN be named (but name ≠ reality)           │
│ Examples        │ "driving", "fear of dogs", "romantic love"  │
└─────────────────┴────────────────────────────────────────────┘

⭐ TEST:
  "Remove the concept of schema → what do we lose?"
  → Lose: convenient shorthand, quick communication
  → DO NOT lose: mechanism (chunks still fire, link, compile exactly the same)
  → = Schema = convenience, NOT necessity
```

---

## §2 — SOFTWARE ANALOGY

```
⭐ "FEATURE" IN SOFTWARE = SCHEMA IN THE BRAIN:

  SOFTWARE:
    → "Function" = actual computational unit
    → Each function has real code, runs on real CPU
    → Can be called, linked, reused
    → INFINITE functions can exist (as needed)
    → CANNOT classify all functions

    → "Feature" = how you DESCRIBE software from the outside
    → "The game has a shop feature" → shop = MANY functions combined
    → "The game has a ranking feature" → ranking = MANY functions combined
    → Shop and ranking may SHARE 1 core function
    → Adding/removing/modifying a feature = changing how functions are called,
      NOT changing the functions themselves

    → Feature = OBSERVATION PARAMETER:
      ✅ Useful: user knows what the software "CAN DO"
      ✅ Communication: product manager says "shop feature" → team understands
      ❌ Not technical: devs don't code "features" → devs code "functions"
      ❌ Feature does NOT exist independently → is a name for a combination of
         functions

  BRAIN:
    → "Chunk" = actual computational unit
    → Each chunk = neurons firing synchronously, real synapses
    → INFINITE chunks (depending on experience)
    → CANNOT classify all chunks

    → "Schema" = how you DESCRIBE chunk networks from the outside
    → "Fear of dogs" = MANY chunks combined ([dog]+[danger]+[retreat]+[heart-
       racing])
    → "Driving" = MANY chunks combined ([brake]+[steer]+[mirror]+[speed])
    → "Fear of dogs" and "fear of snakes" SHARE the chunk [danger]
    → Adding/removing/modifying a schema = changing the name, chunks STILL fire

    → Schema = OBSERVATION PARAMETER:
      ✅ Useful: "he has a complex love schema" → quickly understood
      ✅ Communication: therapist says "old schema firing" → client understands
      ❌ Not mechanism: brain does NOT "run schemas" → brain fires chunks
      ❌ Schema does NOT exist independently → is a name for a chunk network

  EXTENDED ANALOGY:
    → FlappyBird and CandyCrush: VERY DIFFERENT functions, slight engine overlap
    → Math professor and grocery clerk: math chunks OVERLAP, other chunks DIFFER
    → Excel source code CANNOT write FlappyBird: chunks from ONE domain ≠ chunks
       from ANOTHER domain
    → Game dev learning web dev easier than a newbie: engine chunk overlap →
       partial transfer
    → = Like chunks: PARTIAL overlap, PARTIAL transfer, not 100%
```

---

## §3 — VALUE OF SCHEMA AS OBSERVATION PARAMETER

```
🟡 SCHEMA IS STILL USEFUL — knowing its limits clearly:

  ① DESCRIPTIVE:
     → "Love schema contaminated by trauma" = shorthand for:
       "connection chunks + trust chunks + trauma chunks share
       shared chunk [excitement] → trauma fires when connection fires"
     → Schema = SHORT LANGUAGE for COMPLEX chunk pattern
     → No need to name 50 chunks → name 1 schema

  ② PREDICTIVE:
     → "Person with abandonment fear schema → predict jealousy when partner
        is busy"
     → = Person has strongly compiled chunk network [abandonment + worry +
        control]
       → predict chunks fire when partner is absent → jealousy
     → Schema allows FASTER behavior prediction than listing chunks

  ③ COMMUNICATIVE:
     → Therapist: "old schema firing" → client understands immediately
     → If said: "chunk network [childhood abandonment + cortisol association
       + amygdala pattern] is spreading activation" → NOBODY understands
     → Schema = language for NON-EXPERTS

  ④ NAVIGATION AID:
     → "Fix the love schema" = practical instruction:
       recognize pattern → body-listen → differentiate chunks
     → NO NEED to know exact chunks → knowing PATTERN = enough to navigate
     → Schema = compass, NOT GPS

  ⚠️ LIMITS:
     → Schema is NOT mechanism → do NOT use to DESIGN interventions
     → Interventions must work at chunk level:
       change body-input, compile new chunks, re-associate existing chunks
     → "Fix the schema" = actually "re-wire chunk links" + "compile new chunks"
     → Saying "fix the schema" = convenient → but must KNOW underneath = chunk
        work
```

---

## §4 — OBSERVABLE PROPERTIES

### §4.1 Gradient Depth (chunk compile depth)

```
🟡 Observable schemas have DEPTH GRADIENT:

  Underlying reality: chunks compiled at different depths.
  Observation label: "deep schema" or "shallow schema."

  SHALLOW (domain-specific, few repetitions, few modalities):
    → "Take an umbrella when it rains" — few chunks, weak links
    → Changes: WITHIN A DAY (change context = changes immediately)
    → Impact: NARROW (1 context)

  MIDDLE (cross-context, many repetitions):
    → "Must always be productive" — many chunks, reinforced over years
    → Changes: WEEKS → MONTHS (needs repeated new experience)
    → Impact: MODERATE (many contexts)

  DEEP (body-embedded, high emotional weight):
    → "I am worthless" — chunks embedded in cortisol baseline, muscle tension
    → Changes: MONTHS → YEARS (must change BODY, not just "think differently")
    → Impact: BROAD (affects every context)

  DEPTH = f(number of repetitions × number of modalities × emotional weight)
  → HIGH Depth = STRONG synapses = dense chunk links = hard to re-wire
  → LOW Depth = WEAK synapses = thin chunk links = easy to re-wire

  ⚠️ DEPTH IS ONLY 1 DIMENSION — 2D MODEL:
  → Dimension 2 = LINK DENSITY (how many other chunks has this pattern linked
    with over time)
  → High Depth + Low Density (bitten by a dog once): PFC can see it, therapy
    weeks
  → Low Depth + High Density (cultural pattern): PFC CANNOT see it, therapy
    YEARS
  → Details: Chunk/Background-Pattern.md (2D model: Compile Depth × Link Density)

  🟢 Validated by "lottery winner" study (Brickman et al. 1978):
    Surface: "no work tomorrow" → CHANGES IMMEDIATELY ✅
    Mid: "I am wealthy" → takes months to "believe" ⚠️
    Deep: "I am worthless" → PERSISTS even after winning ❌
    Body: cortisol baseline STILL HIGH ❌
    → ~70% of lottery winners return to happiness baseline within 1-2 years
    → Because: deep chunk networks DO NOT change from surface-level change
```

### §4.2 Activation States (chunk activation observation)

```
🟡 Observable schema in 3 states — actually = chunk activation:

  "COMPILED" (unconscious, auto-run):
    → Chunks fire AUTOMATICALLY when trigger matches
    → PFC does NOT participate
    → Observation: "automatic behavior", "knowing without thinking"
    → Mechanism: chunk spreading activation probability-weighted
    → Example: see dog → chunks [threat-dog] fire → retreat. No need to "think."
    → = MOST daily behavior

  "ACTIVE" (PFC currently holding):
    → PFC holds anchor chunks → BIASES spreading activation toward specific
       direction
    → Observation: "currently thinking about", "currently focused on"
    → Mechanism: PFC working memory hold + chunk bias (Chunk.md §8)
    → Example: PFC holds [game design] → activation spreads within game-related
       chunks

  "MONITOR" (background, always running lightly):
    → Chunks run in BACKGROUND → alert PFC when mismatch detected
    → Observation: "always paying attention to", "keeping watch"
    → Mechanism: low-level chunk activation + prediction-delta detection
    → Example: chunks [is my child safe?] run background → child cries → VTA
       alerts PFC
    → 🟢 Cocktail party effect (Cherry 1953): own name = always-on monitor

  → These 3 states = observation labels for CHUNK ACTIVATION LEVELS
  → Chunks do NOT "know" which schema they belong to → only fire per link
     strength
```

### §4.3 Decay + Reactivation (chunk decay observation)

```
🟡 Schema "fading" = chunks decaying in gradient:

  Chunk weakens gradually when not reinforced:
    → Synapse weakens → fires LESS → pattern FADES
    → SHALLOW (few repetitions, few modalities): fades FAST (months)
    → DEEP (many repetitions, many modalities, emotional): fades EXTREMELY SLOWLY

  🟢 Alzheimer's: loses NEWEST chunks first, OLDEST chunks lost LAST
  → = Depth = durability

  Interference — new chunks compete with old chunks:
    → Proactive: old chunks BLOCK new chunks ("used to manual → hard to learn
       automatic")
    → Retroactive: new chunks compete with links of old chunks
    → 🟢 Competitive re-linking (Nader 2000): chunk links NEVER fully deleted,
      only probability shift. Stress can reactivate old links.
    → = "10 years sober, still possible to relapse" — old links STILL EXIST

  Reactivation:
    → Chunk links weak but STILL PRESENT → reactivate EASIER than learn new
    → 🟢 Savings effect (Ebbinghaus): "re-learning" faster than "learning for
       the first time"
    → = Schema "fading" = chunk links weak, NOT lost
```

### §4.4 Cross-Contamination (shared chunk activation)

```
🟡 Schemas "influence each other" = chunks SHARED:

  Chunk [excitement] belongs to MANY networks:
    → Network "romantic love": [crush] → [excitement] → [closeness] → ...
    → Network "fear of abandonment": [alone] → [excitement] → [anxiety] → ...
    → Shared chunk [excitement] = BRIDGE

  When "romantic love" network fires:
    → [crush] fires → [excitement] fires → spreading activation
    → [excitement] ALSO activates "fear of abandonment" network (via shared link)
    → = "Feeling happy in love → suddenly ANXIOUS for no reason"
    → = NOT for no reason: shared chunk bridge

  Why TRAUMA networks cross-contaminate easily:
    ① Compiled DEEP (emotional peak → strong synapses)
    ② Chunks BROAD (fear, excitement, insecurity = COMMON chunks → widely shared)
    ③ Amygdala reinforced (chronic cortisol → amygdala sensitive → fires easily)
    → = Trauma = EASIEST "contaminant" for other chunk networks

  🟢 Retrieval-induced forgetting (Anderson 1994)
  🟢 Stress relapse mechanism (Sinha 2001)

  Example — "always choosing the wrong person":
    → Chunks [love = excitement + insecurity + fear of loss] compiled from
       childhood trauma
    → Meet someone new → unconscious matches: person gives feeling of EXCITEMENT
       + INSECURITY
    → Body sensation SIMILAR to "love" (dopamine + NE similar)
    → Unconscious does NOT distinguish → assembles trauma chunks into "new love"
    → = "Always falling for the wrong person" = trauma chunk matching, NOT
       "bad luck"
```

---

## §5 — SCHEMA × BODY-FEEDBACK

### §5.1 No "negative" schemas — only conflict

```
🟡 EVERY chunk network forms TO SERVE body → always "positive" initially:

  "Holding back words":
    = POSITIVE when at home with strict parents (PROTECTS body from punishment)
    = "NEGATIVE" when at work requiring communication (BLOCKS body from connecting)
    → SAME chunk network → DIFFERENT context → from "positive" BECOMES "negative"
    → = Chunk network has NO fixed valence → CONTEXT determines it

  3 types of conflict:

    Type 1 — 2 networks in SAME context, DIFFERENT direction:
      "Want to eat" + "want to lose weight" → both positive separately →
      conflict SIMULTANEOUSLY

    Type 2 — Network CORRECT in OLD context, WRONG in NEW context (OUTDATED):
      "Save every penny" → CORRECT when poor → OUTDATED when salary is stable

    Type 3 — MULTIPLE networks each CORRECT individually, CONFLICT in total:
      "Career" + "family" + "self-care" = ALL positive → 24 hours NOT enough

  Mechanism:
    → Network A pushes body LEFT, network B pushes RIGHT
    → Body can only go 1 direction → PFC must choose
    → Blocked network STILL fires → consumes energy → dissonance
    → 🟡 PAIN ∝ |force_A − force_B| when OPPOSING directions
    → MAXIMUM PAIN when 2 forces NEARLY EQUAL (paralysis)
    → "Making a decision, even the wrong one, feels better than NOT deciding"
```

### §5.2 Override spectrum

```
🟡 Chunk networks CAN override body-base signals:

  MECHANISM — double suppress:
    ① Chunk network redirects attention (PFC ignores body signal)
    ② Cortisol from chunk network suppresses body sensation (biochemistry)
    → Body nearly SILENCED → chunk network runs freely

  SPECTRUM from mild to extreme:

    Mild (daily):
      → Reading engrossing book, forget to eat: novelty chunks override hunger
      → Scrolling social media until 2am: novelty chunks override sleep signal

    Moderate:
      → Workaholic forgetting sleep: threat-status chunks override L1 sleep
      → Extreme diet: status chunks override L1 nutrition

    Severe:
      → Gaming until death: novelty chunk loop overrides survival signals
      → Anorexia: status chunks override L0 nutrition

    Extreme:
      → Dying for a cause: belief chunk network overrides L0 Alive
      → Mother jumping into fire to save child: protect chunks override
         L0 Alive (self)

  → V7.8: signal strength decides, NOT layer priority
  → Chunk network compiled STRONGLY + sustained cortisol = CAN override ANY signal
  → "Bug" for individual (forgetting to eat → harms body)
  → "Feature" for genes/collective (self-sacrifice → gene survival)
```

### §5.3 Chunk association — Novelty vs. Threat

```
🟡 Same chunk, different association → different for LIFE:

  NOVELTY-DIRECTION compile (curiosity, enthusiasm):
    → Chunk linked with: curiosity + relief + opioid
    → Body-base: "this chunk gives me PLEASURE" → willing to use again
    → Example: Newton reads physics out of curiosity → chunk linked to opioid
       → LOVES it

  THREAT-DIRECTION compile (fear, coercion):
    → Chunk linked with: fear + cortisol + "must do"
    → Body-base: "this chunk is linked to DISCOMFORT" → doesn't want to use
    → Example: student forced to study math → chunk linked to cortisol →
       HATES it

  → SAME knowledge → DIFFERENT association → DIFFERENT usability
  → Cortisol at compile time = determines chunk association tag
    (Chunk.md §2.4 Direction-At-Compile)
  → EVERY BEHAVIOR = MIX of threat + novelty (DIFFERENT ratios)

  Thresholds:
    Mild threat (60:40): can update later → chunk association CAN shift
    Heavy threat (95:5): extreme cortisol depth → body RESISTS when used →
      EXTREMELY HARD to update

  → Details: Cortisol-Baseline.md v2.0 §3.5
```

### §5.4 "The Last Drop" (chunk swap in active network)

```
🟡 Chunk swap in a strongly active network:

  Network strongly active (compiled months, cortisol sustained):
    → Chunk [I can endure] holds network in "bearing it" mode
    → Body: uncomfortable but NOT yet at PAIN threshold

  1 SMALL event (boss gives mild criticism):
    → Chunk swap: [I can endure] → [I might get fired]
    → SAME network SAME intensity → but now in "THREAT" mode
    → All energy → runs threat → body-feedback EXTREME

  Spectrum of reactions to the SAME event:
    Healthy person (empty glass): "ok, fix it" → calm
    Person tired 3 months (half-full glass): uncomfortable for 1 hour → ok
    Burned-out person (full glass): CRIES on the spot
    → SAME drop → DIFFERENT result → because accumulated dissonance DIFFERS

  → Body-Feedback-Mechanism.md: compound dynamics = Miss + Shift + Gap
  → 02-Dissonance.md: 14 intensity levels
```

---

## §6 — SCHEMA × PFC

### §6.1 PFC observes chunk networks → calls it "schema"

```
🟡 PFC does NOT "see" the schema — PFC sees CHUNK ACTIVATIONS → LABELS them:

  Body computes FIRST → Feeling emerges → PFC observes LAST
  (🟢 Damasio 1994, 1999: somatic markers precede conscious decision)

  PFC observes:
    → Many chunks firing SIMULTANEOUSLY in pattern → PFC receives the synthesis
    → PFC labels: "ah, this is 'fear of dogs'" (verbal label for chunk pattern)
    → Label = Feeling.md v2.0 Feel-Labeling (40-80% fidelity) — LOSSY

  PFC does NOT see:
    → WHICH specific chunks are firing (too many, too fast)
    → WHICH specific links are strong/weak
    → Which shared chunks are bridging to WHICH network
    → = PFC sees OUTPUT (feeling, behavior) → infers backward → calls it "schema"

  → = Schema = PFC's BEST GUESS about what chunk network is active
  → APPROXIMATE, not exact
  → Useful, not authoritative
```

### §6.2 PFC orchestrates chunk networks

```
🟡 PFC CAN bias chunk activation (indirect control):

  PFC holds chunks → BIASES spreading activation direction
  → Unconscious reacts in chain according to bias
  → Chunks compiled for the situation → auto-execute

  Example: PFC holds "write the word dog"
    → Unconscious has compiled [type d-o-g]
    → Fingers type automatically → PFC checks: correct ✓
    → PFC does NOT think about motor details

  Example: Expert glancing at painting at a flea market
    → Glances past → unconscious weak match: "unusual brushwork"
    → PFC notices → picks it up, uses magnifying glass (amplifies input for
       unconscious)
    → Unconscious matches DEEPER → "remarkable painting"
    → = PFC does NOT "see" the beautiful painting → PFC holds attention →
      unconscious matches → body reward → PFC observes reward

  WHEN PFC IS POWERLESS:
    → Chunks for the situation NOT YET COMPILED → PFC holds but unconscious has
       nothing to run
    → Body-base signal too strong → PFC override fails
    → PFC effectiveness = f(chunks already compiled for that situation)
```

### §6.3 Schema cannot be analyzed precisely

```
🟡 WHY schemas cannot be "read" precisely:

  ① 86 billion neurons × ~100 trillion connections = too complex
  ② Chunk networks = MULTI-MODAL (verbal captures only ~1/6)
  ③ Deep chunks = BODY EMBEDDED (cortisol baseline, muscle tension)
     → even the OWNER does not know
  ④ Chunk links change CONTINUOUSLY → snapshot now → already different later
  ⑤ Current tools NOT SUFFICIENT: fMRI sees regions, NOT chunk content

  SO WHAT CAN THE FRAMEWORK DO?
    → NOT precise analysis (impossible)
    → CAN: recognize PATTERNS (repeating behavior = chunk network manifesting)
    → CAN: estimate depth (deep vs. surface chunks)
    → CAN: suggest direction (fix body first, chunk links adjust naturally)
    → = COMPASS, not GPS
    → = "Formula, not the answer"

  ⭐ OTHERS SEE PATTERNS THE OWNER CANNOT SEE:
    → Deep chunks = run unconsciously → PFC does NOT observe
    → OUTSIDE observer: sees REPEATING behavior pattern → builds chunks ABOUT
       the pattern
    → = "You tend to self-sabotage when close to success" (close friend sees
       it; you don't)
    → 🟢 Blind spot bias (Pronin 2002)
    → = Therapist/mentor/close friend: primary value = external observer
    → Provides chunks ABOUT YOURSELF that your PFC cannot build on its own
```

---

## §7 — SCHEMA × DOMAIN

### §7.1 Base → Shift → Check — Universal Pattern

```
🟡 ALL chunk networks interact with domain via the SAME pattern:

  ① STABLE BASE (compiled familiar chunks):
     → VTA: familiar → does NOT fire (habituation) → PFC doesn't pay attention

  ② SLIGHT SHIFT from base (trying something new, slightly different):
     → VTA: detects VARIATION → dopamine → PFC is informed

  ③ BODY CHECK (domain reality test):
     → Fits: opioid → ACCEPT → chunk links UPDATE
     → Doesn't fit: REJECT → return to old

  ④ NEW BASE → shift again → check again → ...

  This pattern runs ACROSS ALL domains:
    Food: familiar rice (base) + new side dish (shift) + tasty? (check)
    Music: familiar genre + new song + good?
    Code: existing architecture + new feature + works?
    People: known friend + new person + compatible?
    → SAME mechanism: prediction-delta + body evaluate + chunk update

  ⭐ DUAL-PULL TENSION (Body-Feedback.md §2):
    → Hardware pull: wants to stay smooth → CONSERVATIVE
    → Domain pull: demands adaptation → DEMANDING
    → = Chunk networks always PULLED between "stability" and "update"
    → = ATTRACTOR PATTERN: stable base + incremental shift + feedback check
```

### §7.2 Chunk network formation — 2 pathways

```
🟡 Chunk networks build via 2 sources:

  PATHWAY 1 — UNCONSCIOUS BUILDS ON ITS OWN (no PFC needed):
    → Association learning: stimulus → body responds → chunks wire THEMSELVES
    → FAST (1 experience CAN be enough, especially with emotional peak)
    → NO PFC cost
    → BUT: only from DIRECT EXPERIENCE
    → 🟢 Children 0-4 years: PFC nearly zero → STILL builds complex networks

  PATHWAY 2 — PFC DRAFTS + COMPILES (imagination):
    → PFC imagines scenario → body simulates → body checks → compiles if ok
    → SLOWER, COSTS PFC
    → BUT: from IMAGINATION — no need for direct experience
    → Can PREDICT FURTHER, SAFER, CROSS-DOMAIN possible
    → Example: Einstein thought experiment → draft → insight

  BOTH NEED TO BE STRONG:
    Strong unconscious + weak PFC: many basic chunks + LITTLE far prediction
    Strong PFC + weak unconscious: good draft but NO body-verification
    BOTH strong: wide foundation + high peak = expert

  ⚠️ UNCONSCIOUS ASSEMBLES USING AVAILABLE CHUNKS — DOES NOT DISCRIMINATE:
    → Unconscious finds CLOSEST-MATCHING chunks → ASSEMBLES
    → Does NOT filter "healthy" or "trauma"
    → Trauma chunks CAN be assembled into a new network WITHOUT KNOWING
    → = "Each person loves DIFFERENTLY even meeting the SAME person"
```

---

## §8 — BODY BASELINE STATE

```
🟡 ALL chunk networks build ON 1 foundation: body baseline state
  = Ground truth — PFC, verbal, logic ALL reference back to this

  Body Baseline State = OVERALL state of body at REST:
    Cortisol baseline:   background stress level
    Opioid tone:         background pleasure level
    Oxytocin level:      background connection level
    Muscle tension:      shoulders tight? relaxed?
    Gut state:           digestion normal?
    Sleep architecture:  deep sleep sufficient? REM sufficient?
    HRV:                 heart rate variability
    Immune baseline:     chronic inflammation?

  = "When nothing is happening, how does MY body feel?"

  ⭐ WHY BODY BASELINE IS WHAT IT IS — MECHANISM:
    → Body baseline = PHYSICAL REFLECTION of Background-Patterns
    → High cortisol baseline because Background-Pattern [threat] runs in
       background → sustained cortisol
    → Low opioid tone because Background-Pattern [not enough] suppresses reward
    → High muscle tension because Background-Pattern [alert] fires continuously
    → = Body baseline is NOT random — is the output of accumulated chunk patterns
    → Details on mechanism: Chunk/Background-Pattern.md (chunk-level underneath)

  Fix body baseline → chunk networks adjust on their own (ground truth changes)
  Fix chunks WITHOUT fixing body → relapse (body PULLS back to old state)
  Fix BOTH body + build competing Background-Pattern simultaneously → TRUE
    resolution

  → Correct order: Body → Chunks → Schema observation → CORRECT ORDER
  → = "Know it but don't change" = verbal chunks updated, Background-Pattern NOT YET

  3 ways to reverse-engineer body baseline:
    ① Observe behavior: "what do I usually DO when stressed?" → chunk network
       manifesting
    ② Observe body: "are my shoulders usually tight or relaxed?" → current body
       state
    ③ Self-identify conflicts: "what do I WANT but don't DO?" → chunk conflict
    → = No need to know EXACT chunks → knowing PATTERN = enough to navigate
```

---

## §9 — OPEN QUESTIONS

```
S1: Does a truly "negative" chunk network ACTUALLY exist?
    → Framework: only conflict → but "I am worthless" ALWAYS conflicts in
       EVERY context?
    → Possible: always-on network compiled EXTREMELY DEEP = pseudo-negative
    → Technically conflict → practically = negative everywhere
    → ⚠️ Not fully resolved yet

S2: Can chunk links decrease to ZERO completely?
    → Likely: NEVER true zero → only EXTREMELY LOW probability
    → "10 years sober, still possible to relapse" = old links STILL EXIST,
       just very weak
    → 🟢 Competitive re-linking (Nader 2000): new links COMPETE with old
    → 🟢 Stress relapse (Sinha 2001): stress reactivates old links

S3: Can AI detect chunk network patterns?
    → AI reads TEXT = detects verbal chunks (~1/6 of total)
    → NEEDS: body data (HRV, cortisol, muscle) to detect DEEP patterns
    → 3 tiers: AI detects → Expert verifies → Client body-checks
    → Details: AI-Schema-Detection.md

S4: Epigenetics × chunk networks?
    → Trauma → high cortisol → epigenetic changes → 1-2 generations?
    → 🟢 Dias & Ressler 2014: fear conditioning → offspring fear response
    → = Chunk ASSOCIATION may be "inherited" via epigenetics
```

---

## §10 — HONEST ASSESSMENT

```
ESTABLISHED (🟢):
  → Chunk = learned associative patterns (Hebb 1949, Bliss & Lømo 1973)
  → Spreading activation (Collins & Loftus 1975)
  → Competitive re-linking (Nader 2000)
  → Savings effect (Ebbinghaus)
  → Cocktail party effect (Cherry 1953)
  → Lottery winners returning to baseline (Brickman et al. 1978)
  → Blind spot bias (Pronin 2002)
  → Stress relapse (Sinha 2001)
  → Somatic markers precede decision (Damasio 1994)
  → Fear conditioning epigenetics (Dias & Ressler 2014)

FRAMEWORK SYNTHESIS (🟡):
  → Schema = observation parameter (consistent with 9/9 deep drill files)
  → "No negative schemas" = only context-dependent conflict
  → Override spectrum = same mechanism, different degree
  → Chunk association tag (novelty vs. threat direction)
  → PFC observes chunk activations → labels them = "schema"
  → Base → Shift → Check = universal pattern
  → Body baseline = ground truth → fix body first
  → Dual-pull tension = evolutionary feature

METAPHOR (⚠️):
  → "Schema = software feature" = helpful analogy, not 1-to-1 exact
  → Brain is NOT a computer → analogy aids understanding, is not a model
  → Depth gradient = observation, CANNOT measure precisely per-%
```

---

## §11 — CROSS-REFERENCES

### §11.1 Core mechanism files

```
  Core-v7.8-Draft.md              — cycle architecture, §8 observation parameters
  Chunk.md v2.0                   — chunk substrate (sole substrate, 14 sections)
  Body-Feedback.md v1.1           — dual-pull, Body-Feedback-Precondition, interface
                                    loop
  Body-Feedback-Mechanism.md v1.0 — chunk dynamics (Shift/Miss/Gap), compound
  Feeling.md v2.0                 — PFC observation interface, 7-layer fidelity
  Cortisol-Baseline.md v2.0       — amplifier, direction gate, 7 modes
  Valence-Propagation.md v1.1     — valence per-entity + chain + PFC blindness
```

### §11.2 Schema-specific files

```
  Anchor-Schema.md v1.2               — sync point, trust binding, 4 fill sources
  Anchor-Schema-Example.md            — anchor cases
  Anchor-Schema-Extreme-Example.md    — extreme anchor cases
  AI-Schema-Detection.md              — AI-assisted pattern detection
  Melody Lens/                        — Personal-Melody, Global-Melody, Melody-Arc
```

### §11.3 Related analysis

```
  Agent.md v1.0               — agent = function on chunks, 4-layer
  Empathy.md v1.0             — Self-Pattern-Modeling applied to others
  Drive.md v1.1               — drive = emergent, 6 PFC Modes
  Imagination-Analysis-v2.md  — imagine = PFC engine
```

### §11.4 Application files

```
  Body-Personal-Optimization.md   — personal tuning
  Body-Parenting-Optimization.md  — parenting application
  Research/Education/             — education applications
```

### §11.5 Superseded files (in backup/)

```
  Schema-Operations-v1.md  — content → Chunk.md v2.0, Feeling.md v2.0
  Schema-Example-v1.md     — data valid, framing outdated
  Schema-Diagnostic.md     — diagnostic tools (framing outdated)
```
