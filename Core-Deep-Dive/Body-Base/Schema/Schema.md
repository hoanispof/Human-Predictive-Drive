---
title: Schema.md v2.0 — Schema as Observation Parameter
created: 2026-03-25 (v1.0 DRAFT)
updated: 2026-04-20 (v2.0 REWRITE — observation parameter reframe per v7.8)
translated: 2026-06-09
status: v2.0 COMPLETE
scope: |
  Schema = observation parameter, NOT architectural component.
  Schema = named chunk-network pattern = a WAY OF OBSERVING, not how the brain operates.
  This file defines: what schema is, why it's useful, observable properties,
  interactions with body-feedback / PFC / domain, and limitations.
previous_version: Schema/backup/ (v1.1 content redistributed)
supersedes: |
  Schema-Operations.md (DRAFT 2026-03-26) → backup (content absorbed into Chunk.md v2.0, Feeling.md v2.0)
  Schema-Example.md (DRAFT 2026-03-24) → backup (data valid, framing outdated)
parent: Core-Software.md §9 (observation parameters table)
dependencies:
  - Core-Software.md — cycle architecture, observation parameters
  - Chunk.md v2.0 — chunk substrate (sole substrate)
  - Body-Feedback.md v1.1 — dual-pull, Body-Feedback-Precondition, interface loop
  - Body-Feedback-Mechanism.md v1.0 — chunk dynamics (Shift/Miss/Gap)
  - Feeling.md v2.0 — PFC reception interface
  - Cortisol-Baseline.md v2.0 — amplifier, direction gate
  - Valence-Propagation.md v1.1 — valence per-entity + chain
  - Anchor-Schema.md v1.2 — sync point, trust binding
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Schema — Observation Parameter

> **In software: a "function" is the actual unit of computation. A "feature" is how you describe the software from the outside.**
> **In the brain: chunks are the actual units of computation. Schema is how you describe chunk networks from the outside.**
>
> Schema is NOT an architectural component.
> Schema = named chunk-network pattern — an observation label.
> Useful for description, prediction, and communication.
> But the body-base does NOT "run schemas" — it runs CHUNKS.
>
> This file defines schema within the v7.8 cycle-based architecture.

---

## Table of Contents

- §0 — WHY THE REFRAME
- §1 — WHAT IS SCHEMA IN THE V7.8 FRAMEWORK
- §2 — THE SOFTWARE ANALOGY
- §3 — THE VALUE OF SCHEMA AS OBSERVATION PARAMETER
- §4 — OBSERVABLE PROPERTIES
- §5 — SCHEMA × BODY-FEEDBACK
- §6 — SCHEMA × PFC
- §7 — SCHEMA × DOMAIN
- §8 — BODY BASELINE STATE
- §9 — OPEN QUESTIONS
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

---

## §0 — WHY THE REFRAME

### §0.1 Schema in v1.1

```
V1.1 (2026-03-25 → 2026-04-18):
  → Schema = "a compiled, stable neural oscillation pattern"
  → Schema = SOFTWARE running on HARDWARE (neurons)
  → Schema System = architectural component (same level as Drive, Layer)
  → Chunks = "bricks", Schema = "the building"

  Problems:
  ① Schema LOOKS like a separate component → but is actually = chunks + links
  ② "Compiled schema" → implies schema IS something → actually chunks are compiled
  ③ 3 states (compiled/active/monitor) → actually chunk activation states
  ④ Schema-schema interaction → actually chunk spreading activation
  → = EVERYTHING a schema "does" = what chunks do. Schema is just a NAME.
```

### §0.2 What deep drilling revealed

```
63,000+ lines of drilling (44+ files, 2026-03 → 2026-04) yielded consistent results:

  Chunk.md v2.0: "Brain = database + 2 operators" → chunks = sole substrate
  Body-Feedback.md: "6-step interface loop" → cycles, not components
  Agent.md: "Agent = function on chunk substrate" → no separate category
  Feeling.md v2.0: "PFC reception of body-chunk interaction" → interface
  Drive.md v1.1: "Schema = DETECTOR, drive = emergent" → observation label
  Core-Software.md §0.2: 9/9 files compatible with the reframe

  → Schema = observation label for chunk network patterns
  → Like "feature" in software: describes from the outside, not the internal structure
```

### §0.3 What v2.0 is

```
V2.0 REFRAME:
  → Schema = OBSERVATION PARAMETER (same group as: Novelty, Status, Protect, ...)
  → Body-base runs ENTIRELY on chunks
  → Schema = how HUMANS OBSERVE chunk network patterns
  → Still USEFUL — but you must know this is a lens, not reality

  UNCHANGED:
  → Observable properties (depth, activation, decay, override) remain VALID
  → Examples remain correct (love lifecycle, burnout, trauma cross-contamination)
  → Only the STATUS changes: from "component" → "observation parameter"
```

---

## §1 — WHAT IS SCHEMA IN THE V7.8 FRAMEWORK

### §1.1 Definition

```
⭐ SCHEMA = NAMED CHUNK-NETWORK PATTERN:

  Schema = a set of linked chunks + shared purpose + A NAME

  Chunks [brake] + [check mirror] + [steer] + [observe surroundings] + ...
    + the links between them
    + purpose: "move safely"
    = the schema we CALL "driving a car"

  Schema does NOT EXIST as a separate entity in the brain.
  Schema = the NAME that PFC (or an outside observer) ASSIGNS TO
  an observable chunk network pattern.

  CHUNK = atom (actual unit of computation, fires in the brain)
  SCHEMA = molecule (name for a group of linked atoms)
  ATOMS EXIST PHYSICALLY → molecule = how we DESCRIBE the combination of atoms

  🟡 Reframe key:
  → "Schema fires" = chunks in that network fire
  → "Schema compiled" = chunks in that network have been strengthened
  → "Schema conflict" = 2 groups of chunks firing in opposing directions
  → "Schema update" = chunk links in that network re-weight
  → EVERY "schema operation" = chunk operation + observation label
```

### §1.2 Schema vs Chunk — clear distinction

```
┌───────────────┬──────────────────────────────────────┐
│               │ Chunk                                 │
├───────────────┼──────────────────────────────────────┤
│ Ontology      │ PHYSICALLY EXISTS (neurons wired)    │
│ Level         │ Atom — smallest unit                  │
│ Firing        │ Actually FIRES in the brain (measur.)│
│ Mechanism     │ LTP, spreading activation, compile    │
│ Classification│ CANNOT be fully classified (infinite) │
│ Examples      │ [red], [hot], [mother-face], [brake]  │
└───────────────┴──────────────────────────────────────┘

┌───────────────┬──────────────────────────────────────┐
│               │ Schema                                │
├───────────────┼──────────────────────────────────────┤
│ Ontology      │ OBSERVATION LABEL (name for pattern) │
│ Level         │ Molecule — name for a group of atoms  │
│ Firing        │ "Fires" = chunks in the network fire  │
│ Mechanism     │ Has NO mechanism of its own           │
│ Classification│ CAN be named (but name ≠ reality)    │
│ Examples      │ "driving", "fear of dogs", "love"     │
└───────────────┴──────────────────────────────────────┘

⭐ TEST:
  "Remove the concept of schema — what do you lose?"
  → Lose: a convenient shorthand, a fast way to communicate
  → Do NOT lose: mechanism (chunks still fire, link, compile identically)
  → = Schema = convenience, NOT necessity
```

---

## §2 — THE SOFTWARE ANALOGY

```
⭐ "FEATURE" IN SOFTWARE = SCHEMA IN THE BRAIN:

  SOFTWARE:
    → "Function" = actual unit of computation
    → Each function has real code, runs on a real CPU
    → Can be called, linked, reused
    → INFINITE functions can exist (depending on need)
    → CANNOT fully classify all functions

    → "Feature" = how you DESCRIBE software from the outside
    → "The game has a shop feature" → shop = MANY functions combined
    → "The game has a leaderboard feature" → leaderboard = MANY functions combined
    → Shop and leaderboard may SHARE 1 underlying function
    → Add/remove/modify a feature = change how you call things, NOT the functions

    → Feature = OBSERVATION PARAMETER:
      ✅ Useful: users know what the software "CAN DO"
      ✅ Communicative: product manager says "shop feature" → team understands
      ❌ Not technical: devs don't code "features" → devs code "functions"
      ❌ Feature does NOT exist separately → it's a name for a combination of functions

  BRAIN:
    → "Chunk" = actual unit of computation
    → Each chunk = neurons firing synchronously, real synapses
    → INFINITE chunks (depending on experience)
    → CANNOT fully classify all chunks

    → "Schema" = how you DESCRIBE chunk networks from the outside
    → "Fear of dogs" = MANY chunks combined ([dog]+[danger]+[retreat]+[heart racing])
    → "Driving a car" = MANY chunks combined ([brake]+[steer]+[mirror]+[speed])
    → "Fear of dogs" and "fear of snakes" SHARE the chunk [danger]
    → Add/remove/modify a schema = change the name, chunks STILL fire

    → Schema = OBSERVATION PARAMETER:
      ✅ Useful: "he has a complex love schema" → quick to understand
      ✅ Communicative: therapist says "old schema firing" → client understands
      ❌ Not a mechanism: the brain does NOT "run schemas" → brain fires chunks
      ❌ Schema does NOT exist separately → it's a name for a chunk network

  EXTENDED:
    → FlappyBird and CandyCrush: vastly DIFFERENT functions, minor engine overlap
    → Math professor and grocery clerk: math chunks OVERLAP, other chunks DIFFER
    → Excel source code CANNOT write FlappyBird: one-domain chunks ≠ another's
    → Dev learning web after game dev IS EASIER than a newcomer: engine chunks overlap → partial transfer
    → = Like chunks: overlap PARTIAL, transfer PARTIAL, never 100%
```

---

## §3 — THE VALUE OF SCHEMA AS OBSERVATION PARAMETER

```
🟡 SCHEMA IS STILL USEFUL — when you know its limits:

  ① DESCRIPTIVE:
     → "Love schema contaminated by trauma" = shorthand for:
       "chunks [connection] + chunks [trust] + chunks [trauma] sharing
       shared chunk [excitement] → trauma fires when connection fires"
     → Schema = SHORT LANGUAGE for COMPLEX chunk patterns
     → No need to name 50 chunks → name 1 schema

  ② PREDICTIVE:
     → "Person with an abandonment schema → predict jealousy when partner is busy"
     → = Person has chunk network [abandoned + anxious + controlling] compiled strongly
       → predict chunks fire when partner is absent → jealousy
     → Schema helps PREDICT behavior faster than listing all chunks

  ③ COMMUNICATIVE:
     → Therapist: "old schema firing" → client understands immediately
     → If instead: "chunk network [childhood abandonment + cortisol association
       + amygdala pattern] is spreading activation" → NOBODY understands
     → Schema = language for NON-EXPERTS

  ④ NAVIGATIONAL:
     → "Fix the love schema" = practical instruction:
       recognize the pattern → listen to the body → distinguish chunks
     → No need to know which exact chunks → knowing the PATTERN = enough to navigate
     → Schema = a compass, NOT a GPS

  ⚠️ LIMITATIONS:
     → Schema is NOT a mechanism → do NOT use it to DESIGN interventions
     → Interventions must work at the chunk level:
       change body input, compile new chunks, re-associate existing chunks
     → "Fix the schema" = actually "re-wire chunk links" + "compile new chunks"
     → Saying "fix the schema" = convenient → but you must KNOW underneath = chunk work
```

---

## §4 — OBSERVABLE PROPERTIES

### §4.1 Gradient Depth (chunk compile depth)

```
🟡 Observable schemas have a DEPTH GRADIENT:

  Underlying reality: chunks compiled at different depths.
  Observation label: "deep schema" or "shallow schema."

  SHALLOW (domain-specific, little repetition, few modalities):
    → "Carry an umbrella when it rains" — few chunks, weak links
    → Changeable: in DAYS (change context = change immediately)
    → Impact: NARROW (1 context)

  INTERMEDIATE (cross-context, more repetition):
    → "I must always be productive" — many chunks, reinforced over years
    → Changeable: WEEKS → MONTHS (requires repeated new experience)
    → Impact: MODERATE (many contexts)

  DEEP (body-embedded, high emotional weight):
    → "I am worthless" — chunks embedded in cortisol baseline, muscle tension
    → Changeable: MONTHS → YEARS (must change the BODY, not just "think differently")
    → Impact: BROAD (affects every context)

  DEPTH = f(number of repetitions × number of modalities × emotional weight)
  → High depth = STRONG synapses = dense chunk links = hard to re-wire
  → Low depth = WEAK synapses = thin chunk links = easy to re-wire

  ⚠️ DEPTH IS ONLY 1 DIMENSION — 2D MODEL:
  → Dimension 2 = LINK DENSITY (how many other chunks the pattern has linked with over time)
  → High Depth + Low Density (bitten by a dog once): PFC notices, weeks of therapy
  → Low Depth + High Density (cultural pattern): PFC does NOT notice, YEARS of therapy
  → Details: Chunk/Background-Pattern.md (2D model: Compile Depth × Link Density)

  🟢 "Lottery winner" verification (Brickman et al. 1978):
    Surface: "tomorrow I won't go to work" → CHANGES IMMEDIATELY ✅
    Mid: "I am a wealthy person" → months before they truly "believe" it ⚠️
    Deep: "I am worthless" → STILL PRESENT even after becoming wealthy ❌
    Body: cortisol baseline STILL HIGH ❌
    → ~70% of lottery winners return to their happiness baseline within 1–2 years
    → Because: deep chunk networks do NOT change due to surface-level change
```

### §4.2 Activation States (chunk activation observation)

```
🟡 Observable schema states — actually = chunk activation levels:

  "COMPILED" (unconscious, auto-run):
    → Chunks fire AUTOMATICALLY when a trigger matches
    → PFC does NOT participate
    → Observation: "automatic behavior," "knowing without needing to think"
    → Mechanism: chunk spreading activation, probability-weighted
    → Example: see a dog → chunks [dog-threat] fire → step back. No "thinking" needed.
    → = THE MAJORITY of daily behavior

  "ACTIVE" (PFC currently holding):
    → PFC holds anchor chunks → BIASES spreading activation toward a specific direction
    → Observation: "thinking about," "currently focused on"
    → Mechanism: PFC working memory hold + chunk bias (Chunk.md §8)
    → Example: PFC holds [game design] → activation spreads through game-related chunks

  "MONITOR" (background, always running lightly):
    → Chunks run in the BACKGROUND → alert PFC when they detect mismatch
    → Observation: "always noticing," "keeping watch"
    → Mechanism: low-level chunk activation + prediction-delta detection
    → Example: chunks [is my child safe?] run in background → child cries → VTA alerts PFC
    → 🟢 Cocktail party effect (Cherry 1953): your own name = always-on monitor

  → These 3 states ARE observation labels for CHUNK ACTIVATION LEVELS
  → Chunks do NOT "know" which schema they belong to → they only fire according to link strength
```

### §4.3 Decay + Reactivation (chunk decay observation)

```
🟡 Schema "fading" = chunks decaying along a gradient:

  Chunks weaken when not reinforced:
    → Synapses weaken → fire LESS → pattern FADES
    → SHALLOW (few repetitions, few modalities): fades QUICKLY (months)
    → DEEP (many repetitions, many modalities, emotional): fades EXTREMELY SLOWLY

  🟢 Alzheimer's: newest chunks lost FIRST, OLDEST lost LAST
  → = Depth = durability

  Interference — new chunks compete with old:
    → Proactive: old chunks BLOCK new chunks ("used to a stick shift → hard to learn automatic")
    → Retroactive: new chunks compete with links of old chunks
    → 🟢 Competitive re-linking (Nader 2000): chunk links are NEVER fully deleted,
      only probability shifts. Stress can reactivate old links.
    → = "10 years sober and still can relapse" — old links STILL EXIST

  Reactivation:
    → Chunk links are weak but STILL THERE → reactivation is EASIER than learning fresh
    → 🟢 Savings effect (Ebbinghaus): "re-learning" is faster than "learning the first time"
    → = Schema "faded" = chunk links weakened, NOT gone
```

### §4.4 Cross-Contamination (shared chunk activation)

```
🟡 Schemas "affecting each other" = chunks SHARING:

  Chunk [excitement] belongs to MANY networks:
    → Network "love": [crush] → [excitement] → [closeness] → ...
    → Network "fear of abandonment": [alone] → [excitement] → [anxiety] → ...
    → Shared chunk [excitement] = BRIDGE

  When the "love" network fires:
    → [crush] fires → [excitement] fires → spreading activation
    → [excitement] ALSO activates the "fear of abandonment" network (via shared link)
    → = "Feeling happy and in love → suddenly INEXPLICABLY ANXIOUS"
    → = NOT inexplicable: shared chunk bridge

  Why TRAUMA networks contaminate most easily:
    ① Compiled DEEP (emotional peak → strong synapses)
    ② Chunks BROAD (fear, excitement, insecurity = COMMON chunks → shared widely)
    ③ Amygdala reinforcement (chronic cortisol → amygdala sensitive → fires easily)
    → = Trauma = the EASIEST "contaminant" for other chunk networks

  🟢 Retrieval-induced forgetting (Anderson 1994)
  🟢 Stress relapse mechanism (Sinha 2001)

  "Choosing the wrong person" example:
    → Chunks [love = excitement + insecurity + fear of loss] compiled from childhood trauma
    → Meets someone new → unconscious match: person triggers EXCITEMENT + INSECURITY
    → Body sensation RESEMBLES "love" (similar dopamine + NE)
    → Unconscious does NOT distinguish → trauma chunks assembled into new "love"
    → = "Always falling for the wrong person" = trauma chunk matching, NOT "bad luck"
```

---

## §5 — SCHEMA × BODY-FEEDBACK

### §5.1 There are no "negative schemas" — only conflicts

```
🟡 EVERY chunk network forms TO SERVE the body → always "positive" at first:

  "Suppressing your voice":
    = POSITIVE when growing up with strict parents (PROTECTS body from punishment)
    = "NEGATIVE" when at a company that needs communication (BLOCKS body from connecting)
    → SAME chunk network → DIFFERENT context → from "positive" TO "negative"
    → = Chunk networks do NOT have a fixed valence → CONTEXT determines it

  3 types of conflict:

    Type 1 — 2 networks, SAME context, OPPOSING directions:
      "Want to eat" + "want to lose weight" → both positive separately → conflict SIMULTANEOUSLY

    Type 2 — Network CORRECT in OLD context, WRONG in NEW context (OUTDATED):
      "Save every penny" → CORRECT when poor → OUTDATED when salary is stable

    Type 3 — MULTIPLE networks individually CORRECT, COLLECTIVELY conflicting:
      "Career" + "family" + "self-care" = ALL positive → 24 hours is NOT enough

  Mechanism:
    → Network A pushes body LEFT, network B pushes body RIGHT
    → Body can only go one direction → PFC must choose
    → Blocked network STILL fires → costs energy → dissonance
    → 🟡 PAIN ∝ |force_A − force_B| when they OPPOSE
    → MAXIMUM PAIN when the 2 forces are NEARLY EQUAL (paralysis)
    → "Even a wrong decision, once made, feels lighter than NO decision"
```

### §5.2 Override spectrum

```
🟡 Chunk networks CAN override body-base signals:

  MECHANISM — double suppress:
    ① Chunk network redirects attention (PFC ignores body signal)
    ② Cortisol from chunk network suppresses body sensation (biochemistry)
    → Body is NEARLY silenced → chunk network runs freely

  SPECTRUM from mild to extreme:

    Mild (daily):
      → Reading an engaging book → forget to eat: novelty chunks override hunger signal
      → Scrolling social media until 2am: novelty chunks override sleep signal

    Moderate:
      → Workaholic forgetting to sleep: threat-status chunks override L1 sleep
      → Extreme dieting: status chunks override L1 nutrition

    Severe:
      → Gaming to the point of death: novelty chunk loop overrides survival signals
      → Anorexia: status chunks override L0 nutrition

    Extreme:
      → Martyrdom: belief chunk network overrides L0 Alive
      → Mother jumping into fire to save her child: protect chunks override L0 Alive (own body)

  → V7.8: signal strength decides, NOT layer priority
  → Chunk network compiled STRONGLY + sustained cortisol = CAN override ANY signal
  → "Bug" for the individual (forgetting to eat → harms body)
  → "Feature" for the gene/collective (self-sacrifice → gene survives)
```

### §5.3 Chunk association — Novelty vs Threat

```
🟡 Same chunk, different association → different FOR LIFE:

  NOVELTY-DIRECTION compile (curiosity, delight):
    → Chunk associated with: curiosity + relief + opioid
    → Body-base: "this chunk gives me PLEASURE" → willing to use it again
    → Example: Newton reading physics out of curiosity → chunk tagged with opioid → LOVES it

  THREAT-DIRECTION compile (fear, coercion):
    → Chunk associated with: fear + cortisol + "have to"
    → Body-base: "this chunk is tagged UNCOMFORTABLE" → does not want to use it again
    → Example: student forced to study math → chunk tagged with cortisol → HATES it

  → SAME knowledge → DIFFERENT association → DIFFERENT ability to use it
  → Cortisol at compile time = determines chunk association tag (Chunk.md §2.4 Direction-At-Compile)
  → EVERY BEHAVIOR = MIX of threat + novelty (in DIFFERENT ratios)

  Threshold:
    Mild threat (60:40): easier to update later → chunk association CAN shift
    Heavy threat (95:5): cortisol deeply embedded → body RESISTS using it → EXTREMELY hard to update

  → Details: Cortisol-Baseline.md v2.0 §3.5
```

### §5.4 The Overflow Point

```
🟡 Chunk swap within a heavily active network:

  Network actively running STRONGLY (compiled for months, cortisol sustained):
    → Chunk [I can push through] holds network in "enduring" mode
    → Body: uncomfortable but NOT yet at the threshold for PAIN

  1 SMALL event (boss gives a mild reminder):
    → Chunk swaps: [I can push through] → [I might get fired]
    → SAME network SAME intensity → but now in "THREAT" mode
    → All energy → runs on threat → body-feedback EXTREMELY LARGE

  Spectrum of reactions to THE SAME event:
    Person who is healthy (cup empty): "ok, I'll fix it" → easy
    Person tired for 3 months (cup half full): uncomfortable for an hour → then ok
    Person burned out (cup overflowing): CRIES right there on the spot
    → SAME drop → DIFFERENT outcome → because accumulated dissonance is DIFFERENT

  → Body-Feedback-Mechanism.md: compound dynamics = Miss + Shift + Gap
  → 02-Dissonance.md: 14 intensity levels
```

---

## §6 — SCHEMA × PFC

### §6.1 PFC receives chunk network output → calls them "schemas"

```
🟡 PFC does NOT "see" schema — PFC sees CHUNK ACTIVATIONS → LABELS:

  Body computes FIRST → Feeling emerges → PFC receives LAST
  (🟢 Damasio 1994, 1999: somatic markers precede conscious decision)

  PFC receives:
    → Many chunks fire SIMULTANEOUSLY in a pattern → PFC receives the integrated output
    → PFC labels: "ah, this is 'fear of dogs'" (verbal label for chunk pattern)
    → Label = Feeling.md v2.0 Feel-Labeling (40–80% fidelity) — LOSSY

  PFC does NOT see:
    → Which SPECIFIC chunks are currently firing (too many, too fast)
    → Which SPECIFIC links are strong/weak
    → Which shared chunks are bridging to WHICH network
    → = PFC sees OUTPUT (feeling, behavior) → infers the PATTERN → calls it "schema"

  → = Schema = PFC's BEST GUESS about what chunk network is active
  → APPROXIMATE, not exact
  → Useful, not authoritative
```

### §6.2 PFC orchestrates chunk networks

```
🟡 PFC CAN bias chunk activation (indirect control):

  PFC holds chunks → BIASES spreading activation direction
  → Unconscious responds in a chain reaction following the bias
  → Chunks compiled for the situation → auto-execute

  Example: PFC holds "write 'dog'"
    → Unconscious has compiled [type d-o-g]
    → Fingers type automatically → PFC reviews: correct ✓
    → PFC does NOT think about motor details

  Example: Expert browsing paintings at a flea market
    → Glances past → unconscious weak match: "strange brushwork"
    → PFC notices → picks it up, uses a magnifying glass (amplifies input for unconscious)
    → Unconscious matches DEEPER → "this is a special painting"
    → = PFC does NOT "see" the beauty → PFC holds attention →
      unconscious matches → body reward → PFC receives the reward

  WHEN PFC IS POWERLESS:
    → Chunks for that situation NOT COMPILED → PFC holds but unconscious has nothing to run
    → Body-base signal too strong → PFC override fails
    → PFC effectiveness = f(chunks already compiled for that situation)
```

### §6.3 Schema CANNOT be precisely analyzed

```
🟡 WHY you cannot accurately "read" a schema:

  ① 86 billion neurons × ~100 trillion connections = too complex
  ② Chunk networks = MULTI-MODAL (verbal captures only ~1/6)
  ③ Deep chunks = BODY EMBEDDED (cortisol baseline, muscle tension)
     → even the person themselves does NOT know
  ④ Chunk links change CONTINUOUSLY → a "snapshot" now → already different moments later
  ⑤ Current tools NOT SUFFICIENT: fMRI shows brain regions, NOT chunk content

  SO WHAT CAN THE FRAMEWORK DO?
    → NOT analyze precisely (impossible)
    → CAN: recognize PATTERNS (repeated behaviors = chunk network manifestations)
    → CAN: estimate depth (deep vs surface chunks)
    → CAN: suggest directions (fix body first, chunk links self-adjust)
    → = A COMPASS, not a GPS
    → = "A formula, not an answer"

  ⭐ OTHERS SEE PATTERNS THE PERSON THEMSELVES CANNOT SEE:
    → Deep chunks = run unconsciously → PFC does NOT receive
    → OUTSIDE observer: sees REPEATED BEHAVIOR patterns → builds chunks ABOUT the pattern
    → = "You tend to self-sabotage right when you're close to success" (close friend sees it, you don't)
    → 🟢 Blind spot bias (Pronin 2002)
    → = Therapist / mentor / close friend: their PRIMARY value = being an external observer
    → Gives you chunks ABOUT YOURSELF that your own PFC cannot build
```

---

## §7 — SCHEMA × DOMAIN

### §7.1 Base → Shift → Check — Universal Pattern

```
🟡 ALL chunk networks interact with domain following THE SAME pattern:

  ① Have a stable BASE (compiled, familiar chunks):
     → VTA: familiar → does NOT fire (habituation) → PFC doesn't pay attention

  ② SLIGHT SHIFT from base (try something new, slightly different):
     → VTA: detects DEVIATION → dopamine → PFC is notified

  ③ BODY CHECK (domain reality test):
     → Matches: opioid → ACCEPT → chunk links UPDATE
     → Doesn't match: REJECT → return to old base

  ④ NEW BASE → shift again → check again → ...

  This PATTERN runs ACROSS ALL domains:
    Eating: familiar rice (base) + new side dish (shift) + tasty? (check)
    Music: familiar genre + new song + good?
    Code: existing architecture + new feature + does it work?
    People: existing friends + someone new + do we connect?
    → SAME mechanism: prediction-delta + body evaluates + chunk update

  ⭐ DUAL-PULL TENSION (Body-Feedback.md §2):
    → Hardware pull: wants to stay smooth → CONSERVATIVE
    → Domain pull: demands adaptation → DEMANDING
    → = Chunk networks are always PULLED between "stability" and "updating"
    → = ATTRACTOR PATTERN: stable base + incremental shift + feedback check
```

### §7.2 How chunk networks form — 2 pathways

```
🟡 Chunk networks build through 2 sources:

  PATHWAY 1 — UNCONSCIOUS SELF-BUILDS (no PFC required):
    → Association learning: stimulus → body responds → chunks WIRE THEMSELVES
    → FAST (1 experience CAN be enough, especially at emotional peaks)
    → COSTS NO PFC
    → BUT: only from DIRECT EXPERIENCE
    → 🟢 Children ages 0–4 with near-zero PFC → STILL build complex networks

  PATHWAY 2 — PFC DRAFTS + COMPILES (via imagination):
    → PFC imagines scenario → body simulates → body checks → compiles if ok
    → SLOWER, COSTS PFC
    → BUT: from IMAGINATION — no direct experience needed
    → Predicts FURTHER ahead, SAFER, CROSS-DOMAIN possible
    → Example: Einstein's thought experiments → draft → insight

  BOTH NEED TO BE STRONG:
    Strong unconscious + weak PFC: many basic chunks + LITTLE far prediction
    Strong PFC + weak unconscious: good at drafting but NO body verification
    BOTH STRONG: wide foundation + high ceiling = expert

  ⚠️ THE UNCONSCIOUS ASSEMBLES FROM AVAILABLE CHUNKS — WITHOUT DISTINGUISHING:
    → Unconscious finds the CLOSEST MATCHING chunks → assembles them
    → Does NOT filter "healthy" vs "trauma"
    → Trauma chunks CAN be assembled into new networks WITHOUT NOTICING
    → = "Each person loves differently even when they meet the same person"
```

---

## §8 — BODY BASELINE STATE

```
🟡 ALL chunk networks build ON 1 foundation: body baseline state
  = Ground truth — PFC, verbal, logic all REFERENCE BACK here

  Body Baseline State = the OVERALL state of the body at REST:
    Cortisol baseline:  background stress level
    Opioid tone:        background pleasure level
    Oxytocin level:     background connection level
    Muscle tension:     shoulders tense? relaxed?
    Gut state:          digestion normal?
    Sleep architecture: sufficient deep sleep? sufficient REM?
    HRV:                heart rate variability
    Immune baseline:    chronic inflammation?

  = "When nothing is happening, how does MY body feel?"

  ⭐ WHY THE BODY BASELINE IS THE WAY IT IS — MECHANISM:
    → Body baseline = PHYSICAL REFLECTION of Background-Patterns
    → HIGH cortisol baseline because Background-Pattern [threat] runs in background → cortisol sustained
    → LOW opioid tone because Background-Pattern [not enough] suppresses reward
    → HIGH muscle tension because Background-Pattern [alert] fires continuously
    → = Body baseline is NOT random — it is the output of accumulated chunk patterns
    → Details of mechanism: Chunk/Background-Pattern.md (chunk-level underneath)

  Fix body baseline → chunk networks self-adjust (ground truth changes)
  Fix chunks WITHOUT fixing body → relapse (body PULLS back to old state)
  Fix SIMULTANEOUSLY: body + build competing Background-Pattern → TRUE resolution

  → Order: Body → Chunks → Schema observation → THE CORRECT ORDER
  → = "Knowing but not changing" = verbal chunks updated, Background-Pattern NOT yet

  3 WAYS to reverse-engineer body baseline:
    ① Observe behavior: "what do I typically DO when stressed?" → chunk network manifesting
    ② Observe body: "are my shoulders USUALLY tense or relaxed?" → current body state
    ③ Self-identify conflicts: "what do I WANT but NOT DO?" → chunk conflict
    → = No need to know EXACTLY which chunks → knowing the PATTERN = enough to navigate
```

---

## §9 — OPEN QUESTIONS

```
S1: Does a "negative" chunk network TRULY not exist?
    → Framework: there is only conflict → but "I am worthless" ALWAYS conflicts in EVERY context?
    → Possible: an always-on network compiled EXTREMELY DEEP = pseudo-negative
    → Technically conflict → practically = negative everywhere
    → ⚠️ Not fully resolved

S2: Can chunk links decrease to ABSOLUTE ZERO?
    → Likely: NEVER zero → only EXTREMELY LOW probability
    → "10 years sober and still can relapse" = old links REMAIN though extremely weak
    → 🟢 Competitive re-linking (Nader 2000): new links COMPETE with old
    → 🟢 Stress relapse (Sinha 2001): stress reactivates old links

S3: Can AI detect chunk network patterns?
    → AI reads TEXT = detects verbal chunks (~1/6 of total)
    → NEEDED: body data (HRV, cortisol, muscle tension) to detect DEEP patterns
    → 3 levels: AI detects → specialist verifies → client body-checks
    → Details: AI-Schema-Detection.md (planned)

S4: Epigenetics × chunk networks?
    → Trauma → high cortisol → epigenetic changes → 1–2 generations?
    → 🟢 Dias & Ressler 2014: fear conditioning → offspring show fear response
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
  → Lottery winners return to happiness baseline (Brickman et al. 1978)
  → Blind spot bias (Pronin 2002)
  → Stress relapse (Sinha 2001)
  → Somatic markers precede decision (Damasio 1994)
  → Fear conditioning epigenetics (Dias & Ressler 2014)

FRAMEWORK SYNTHESIS (🟡):
  → Schema = observation parameter (consistent with 9/9 deep drill files)
  → "No negative schemas" = only context-dependent conflict
  → Override spectrum = same mechanism, different degree
  → Chunk association tag (novelty vs threat direction)
  → PFC receives chunk activations → labels them = "schema"
  → Base → Shift → Check = universal pattern
  → Body baseline = ground truth → fix body first
  → Dual-pull tension = evolutionary feature

METAPHOR (⚠️):
  → "Schema = software feature" = an illustration, NOT 1-to-1 accurate
  → The brain is NOT a computer → analogy aids understanding, not a model
  → Depth gradient = an observation, NOT measurable per exact percentage
```

---

## §11 — CROSS-REFERENCES

### §11.1 Core mechanism files

```
  Core-Software.md                — cycle architecture, §9 observation parameters
  Chunk.md v2.0                  — chunk substrate (sole substrate, 14 sections)
  Body-Feedback.md v1.1          — dual-pull, Body-Feedback-Precondition, interface loop
  Body-Feedback-Mechanism.md v1.0— chunk dynamics (Shift/Miss/Gap), compound
  Feeling.md v2.0                — PFC reception interface, 7-layer fidelity
  Cortisol-Baseline.md v2.0      — amplifier, direction gate, 7 modes
  Valence-Propagation.md v1.1    — valence per-entity + chain + PFC blindness
```

### §11.2 Schema-specific files

```
  Anchor-Schema.md v1.2          — sync point, trust binding, 4 fill sources
  Anchor-Schema-Example.md       — anchor cases
  Anchor-Schema-Extreme-Example.md — extreme anchor cases
  AI-Schema-Detection.md         — AI-assisted pattern detection
  Melody Lens/                   — Personal-Melody, Global-Melody, Melody-Arc
```

### §11.3 Related analysis

```
  Agent.md v1.0                  — agent = function on chunks, 4-layer
  Empathy.md v1.0                — Self-Pattern-Modeling applied to others
  Drive.md v1.1                  — drive = emergent, 6 PFC Modes
  Imagination-Analysis-v2.md     — imagination = PFC engine
```

### §11.4 Application files

```
  Body-Personal-Optimization.md  — personal tuning
  Body-Parenting-Optimization.md — parenting application
  Research/Education/             — education applications
```

### §11.5 Superseded files (in backup/)

```
  Schema-Operations-v1.md        — content → Chunk.md v2.0, Feeling.md v2.0
  Schema-Example-v1.md           — data valid, framing outdated
  Schema-Diagnostic.md           — diagnostic tools (framing outdated)
```

---

> *Schema v2.0 — "Schema = observation parameter, NOT component.*
> *Chunks are what the brain actually runs. Schema is what we call it."*
