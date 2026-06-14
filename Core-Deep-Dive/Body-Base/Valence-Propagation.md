---
title: Valence-Propagation — The Body's Evaluation System + Propagation Mechanism Through Schema Network
version: 1.0 (English)
source_version: 4.1 (Vietnamese, 2026-05-29)
translated: 2026-06-11
status: v1.0 — REFERENCE FILE (valence definition + propagation mechanism)
scope: |
  WHAT valence IS (definition, 4 properties, valence profile per-entity) +
  HOW valence FORMS (4 sources, 3 update types, bias) +
  HOW valence PROPAGATES through schema chain (4 mechanisms, 5 chain properties, 4-layer long chain) +
  CASES analysis (6 groups) + PFC BLINDNESS + 3 PRINCIPLES + LIMITS.
  v4.0 SPLIT: Per-entity valence dynamics → Entity-Valence-Dynamics.md v1.0.
  Companion: Entity-Valence-Dynamics.md v1.0 = HOW valence BEHAVES per-entity over time.
  This file = WHAT valence IS + HOW it FORMS + HOW it PROPAGATES.
purpose: |
  Central reference for valence definition + formation + propagation mechanism.
  2 pillars: WHAT valence IS (§1-§2) + HOW valence FORMS AND PROPAGATES (§3-§7).
  Per-entity dynamics → Entity-Valence-Dynamics.md v1.0 (companion file).
dependencies:
  - Entity-Valence-Dynamics.md v1.0 — companion: HOW valence behaves per-entity over time
  - Body-Base.md v3.3 — L0+L1 substrate + observation parameters that valence evaluates
  - Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, 2 sources, 3 dynamics
  - Schema.md v2.0 — schema = chunks + links + purpose
  - Chunk.md v2.2 — chunk substrate, context-tag, 4 connection types
  - Anchor-Schema.md v1.2 — anchor amplifies propagation, trust binding
  - Collective-Body.md v1.2 — 3-Level Model (Clarification reference)
  - Self-Pattern-Modeling.md v3.1 — observed experience (§3 source ②)
  - Agent-Mechanism.md v2.1 — Schema-Imagined-Overlay (§2 abstract entities)
  - Feeling.md v3.0 — PFC observation of body-feedback (different layer)
  - Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State × valence
  - Drive.md — synthesizes valences → action
language: English translation (Vietnamese primary + English technical terms in source)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Valence-Propagation — The Body's Evaluation System + Propagation Mechanism Through Schema Network

> **The knife that once cut your hand. You FEAR it.**
> **The same knife, once you learn to use it. You LIKE it.**
> **The same knife, in an enemy's hand. You FEAR it AGAIN.**
>
> Same entity — valence CHANGES depending on experience and context.
> That is per-entity valence — how the body evaluates one specific thing.
>
> But there is something FAR MORE COMPLEX:
>
> **Does math directly feed body-base? NO.**
> **But math LINKS to a chain: math → grades → university → job → salary → body feeds.**
> **Positive valence at the END of the chain PROPAGATES BACKWARD → math (+).**
> **= Valence PROPAGATION through schema network.**
>
> This file: WHAT valence IS, per-entity structure,
> how valence FORMS from 4 sources,
> how valence PROPAGATES through schema chains,
> WHY PFC doesn't know, and the FUNDAMENTAL LIMITS.
>
> **Per-entity valence dynamics** (Structural vs Current, Hardware-Subsidy,
> 3 Firing Modes, Satiation Type, Phantom resonance...)
> **→ Entity-Valence-Dynamics.md v1.0** (companion file).

---

## Table of Contents

- [§0 — POSITION IN FRAMEWORK](#0)
- [§1 — WHAT VALENCE IS](#1)
- [§2 — VALENCE PROFILE: Per-Entity Structure](#2)
- [§3 — HOW VALENCE FORMS + UPDATES](#3)
- [§4 — VALENCE PROPAGATION THROUGH SCHEMA CHAIN](#4)
- [§5 — CHAIN PROPERTIES + WHY LONG CHAINS PERSIST](#5)
  - [§5.1 — 5 Properties](#51)
  - [§5.2 — 4-Layer Mechanism for Creating + Maintaining Long Chains](#52)
- [§6 — CASE ANALYSIS](#6)
- [§7 — PFC BLINDNESS + 3 PRINCIPLES](#7)
  - [§7.1 — PFC Blindness](#71)
  - [§7.2 — 3 Principles](#72)
  - [§7.3 — Fundamental Limits](#73)
- [§8 — HONEST ASSESSMENT](#8)
- [§9 — CROSS-REFERENCES + CITATIONS](#9)

---

## §0 — POSITION IN FRAMEWORK

```
🟡 VALENCE IN THE FRAMEWORK ARCHITECTURE:

  VALENCE = THE WAY THE BODY EVALUATES EVERYTHING.

  Before taking action, the body must EVALUATE:
    "How does this entity affect MY body-base?"
    "Positive? Negative? Mixed? Through which channel?"
  The result of this evaluation = VALENCE.

  Valence BELONGS TO Body-Base because:
    → Body is WHERE the evaluation happens (amygdala, insula, body signals)
    → Body-base substrate (L0+L1) is the MEASURING STANDARD of evaluation
    → Valence = body's ASSESSMENT, not PFC's judgment
    → PFC can OBSERVE valence (becoming feeling), but does NOT create it
    → = Feeling.md v3.0: "Feeling = PFC observation of body"
    → = Valence = WHAT body computes. Feeling = WHAT PFC sees.

  VALENCE × BODY-NEED (Body-Feedback-Mechanism v2.0 §1):
    Body-Need = aggregate OUTPUT of chunk dynamics.
    Valence = body's ASSESSMENT per-entity → feeds INTO body-need.
    Entity with positive valence → body-need shifts toward approach.
    Entity with negative valence → body-need shifts toward avoidance.
    Synthesis of valences across entities + body state = current body-need.


  THIS FILE IN THE FLOW:

    Body-Base.md (L0+L1 substrate — FOUNDATION)
         │
         ▼
    Body-Feedback-Mechanism.md v2.0 (Body-Need aggregate, chunk dynamics)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ VALENCE-PROPAGATION.MD v4.1 (THIS FILE)                     │
    │                                                              │
    │  PILLAR 1: WHAT VALENCE IS (§1-§2)                          │
    │    Valence definition → valence profile per-entity           │
    │                                                              │
    │  → Entity-Valence-Dynamics.md v1.0 (COMPANION FILE)         │
    │    HOW valence behaves per-entity over time:                 │
    │    Structural/Current, 3 Firing Modes, Hardware-Subsidy,     │
    │    Satiation Type, Mixed valence, Phantom resonance,         │
    │    Technology frontier                                       │
    │                                                              │
    │  PILLAR 2: VALENCE FORMATION + PROPAGATION (§3-§7)          │
    │    4 formation sources → 4 propagation mechanisms → Chain   │
    │    properties → Case analysis → PFC Blindness               │
    └─────────────────────────────────────────────────────────────┘
         │
         ▼
    Drive.md (SYNTHESIZES valences → action)
    Feeling.md v3.0 (PFC OBSERVES valence → feeling)
    Drill-Emergent-Pattern.md (valence ACCUMULATES → patterns emerge)
    Anchor-Schema.md (anchor AMPLIFIES propagation)


  DISTINGUISHING 4 CLOSELY RELATED CONCEPTS:

    VALENCE (this file):
      "How does entity X affect MY body-base?"
      = EVALUATION — both per-entity and through schema chain
      Input: entity + body-base state + context + compiled schemas
      Output: valence profile + propagated valence through network

    DRIVE (Drive.md):
      "MANY drives are active → which ACTION does the brain CHOOSE?"
      = SYNTHESIS of many drives → action emerges
      Input: all valences + body-needs + context
      Output: specific action

    FEELING (Feeling.md v3.0):
      "WHAT does PFC SEE when observing body-chunk interaction?"
      = PFC OBSERVATION — valence through the PFC lens
      Input: body signals + chunk activation
      Output: conscious experience (7 layers, 20-100% fidelity)

    BODY SIGNALS (Body-Dissonance.md):
      "Body RESPONDS: sufficient? Or not? Continue?"
      = FEEDBACK after action
      3 signals: Satisfaction, Reward, Dissonance

    Flow: Valence → Drive → Action → Body Signals → Update Valence → Loop
```

---

## §1 — WHAT VALENCE IS

```
🟡 DEFINITION:

  Valence = THE BODY'S EVALUATION of how an entity affects body-base.

  "Entity" = anything the body encounters in a domain:
    → Object: knife, chair, car, book, bomb, thorn, lighter...
    → Agent: mother, friend, boss, dog, God, Jensen Huang...
    → Abstract: math, physics, charity, the future, Heaven...
    → Action: helping, suing, studying, killing...
    → State: rich, poor, lonely, famous...

  Body-base has 2 EVALUATION DIMENSIONS (Body-Base.md v3.3):

    DIMENSION 1 — SUBSTRATE (what the body monitors):
      → L0 Alive: safe ←→ dangerous (binary threshold)
      → L1 Body-inputs: useful ←→ harmful (nutrition, sleep, comfort, autonomy, social...)

    DIMENSION 2 — SIGNAL PROCESSING (what type of signal the body creates):
      → Direct-State: hardware pathways, from birth (Reward-Signal-Architecture.md)
      → Evaluative: compiled patterns, develops with age (E₀→E₃)

    OBSERVATION PARAMETERS (named patterns at evaluative output):
      → Novelty, Status, Protect, Mastery = NAMES for patterns PFC observes
      → NOT channels or layers — they are OUTPUT of evaluative processing on L0+L1


  ⭐ 4 CORE PROPERTIES:

  ① MULTI-CHANNEL — NOT A SINGLE GOOD/BAD AXIS:

    WRONG: "Mother = good" or "Mother = bad" (1 axis)
    RIGHT: Mother = {
      L1 nutrition: ++ (feeds me)
      L1 comfort: ++ (hugs, soothes)
      L1 autonomy: -- (forces studying, forbids play)
      Mastery: + (teaches)
      Novelty: - (forces repetition of hard material)
    }
    = Valence DIFFERS on EACH CHANNEL
    = LOVE AND DISLIKE SIMULTANEOUSLY — not contradictory

    🟢 Mixed feelings (ambivalence): well-documented phenomenon
    🟢 Multi-dimensional emotion: no dispute that emotions are complex

  ② DYNAMIC — CHANGES OVER TIME:

    Knife the first time: { L0 safety: -- }
    Knife after learning to use: { L1 utility: ++, L0 safety: neutral }
    = SAME entity, DIFFERENT valence — because experience changed

  ③ CONTEXT-DEPENDENT:

    Bomb in my ally's hand: { L0: ++, L1: ++ } (weapon, protection)
    Bomb in an enemy's hand: { L0: --, L1: -- } (threat)
    = SAME entity, SAME moment, DIFFERENT CONTEXT → different valence

  ④ STORED IN SCHEMA:

    Valence profile compiled into schema through experience
    → Entity encountered again → schema loads valence → body responds IMMEDIATELY
    → No need to re-evaluate from scratch each time
    → = Why seeing a dog that once bit you → INSTANT FEAR (compiled valence)
    → = Schema.md §1: "Schema = stabilized pattern of neural oscillation"
    → Valence = 1 DIMENSION of schema (alongside motor, visual, somatic...)

    ⚠️ NO SOURCE TAG (Drill §10 — GAP 8):
    → Valence is stored WITHOUT a field for "source" (internal or external?)
    → Wire = wire. Body treats EQUALLY regardless of where compiled.
    → PFC ALSO cannot distinguish (§7 confabulation)
    → "Do I truly want X or was it socially installed?" = a MEANINGLESS question at body level
    → "I" = SYNTHESIS of internal + external compiled patterns
    → 🟢 Nisbett & Wilson 1977: PFC cannot access actual processing

    🟢 Fear conditioning: rapid, one-trial learning (LeDoux 1996)
    🟢 Evaluative conditioning: valence transfer through association (De Houwer 2007)
```

---

## §2 — VALENCE PROFILE: Per-Entity Structure

```
🟡 EACH ENTITY IN A DOMAIN HAS A VALENCE PROFILE STORED IN SCHEMA:

  ┌─────────────────────────────────────────────────────────────┐
  │ VALENCE PROFILE: Entity X                                    │
  │                                                              │
  │ SUBSTRATE ASSESSMENT (L0 + L1):                               │
  │   L0 Alive:      safe ←────────→ dangerous                  │
  │   L1 Body-inputs:                                            │
  │     Nutrition:    useful ←──────→ harmful                    │
  │     Comfort:      pleasant ←────→ unpleasant                 │
  │     Sleep:        promoting ←───→ disrupting                 │
  │     Autonomy:     enabling ←────→ constraining               │
  │     Social:       connecting ←──→ isolating                  │
  │                                                              │
  │ EVALUATIVE ASSESSMENT (compiled pattern evaluation):         │
  │     Novelty:      interesting ←→ boring                      │
  │     Mastery:      enabling ←────→ blocking                   │
  │     Status:       elevating ←───→ diminishing                │
  │     Protect:      safe ←─────────→ threatening (resources)   │
  │                                                              │
  │ META-DIMENSIONS:                                             │
  │   Trust:           high ←──────→ low                         │
  │   Predictability:  high ←──────→ low                         │
  │   Replaceability:  easy ←──────→ hard                        │
  │   Dependency:      none ←──────→ critical                    │
  │                                                              │
  │ NET: synthesis across channels → approach / avoid / mixed    │
  └─────────────────────────────────────────────────────────────┘


  PROFILE CHARACTERISTICS:

    ① Each dimension has its OWN valence — no averaging
      Mother: L1++ but autonomy-- = NOT "slightly positive"
      = Positive on some dimensions, Negative on others, SIMULTANEOUSLY

    ② Not every dimension has valence for every entity
      Knife: L0, L1 clear. Status? Near zero. Novelty? Only the first time.
      = Valence profile SPARSE for objects, DENSE for agents

    ③ Intensity VARIES
      Knife cuts hand: L0 safety -2 (mild)
      Tiger chasing: L0 safety -10 (extreme)
      = Same channel, same direction, different INTENSITY

    ④ Meta-dimensions MODULATE body-base channels
      High trust → valence AMPLIFIED (trust a close friend → valence stronger)
      Low trust → valence DAMPENED (distrust a stranger → valence weaker)
      Trust mechanism details: Trust.md v1.0
      Easy replaceability → losing entity has LITTLE impact
      Hard replaceability → losing entity has BIG IMPACT (grief)


  OBJECT VALENCE vs AGENT VALENCE:

  ┌─────────────────────┬──────────────────────────────────────────┐
  │ OBJECT VALENCE      │ AGENT VALENCE                             │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ Few channels active  │ MANY channels active                     │
  │ Knife: L0, L1        │ Mother: L0, L1, evaluative, trust,       │
  │                      │ dependency                               │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ Relatively STABLE   │ DYNAMIC — changes continuously           │
  │ Knife is still knife │ Mother happy in morning, irritable later │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ONE-WAY              │ BIDIRECTIONAL                             │
  │ I evaluate knife     │ I evaluate mother AND mother evaluates me │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ EASY to replace      │ HARD to replace                          │
  │ Another knife works  │ A different mother is NOT my mother      │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ PREDICTABLE          │ UNPREDICTABLE                             │
  │ Valence rarely       │ Valence can FLIP unexpectedly            │
  │ surprises            │                                           │
  └─────────────────────┴──────────────────────────────────────────┘

  → Agent valence MORE COMPLEX than object due to these 5 properties.
  → Agent valence HAS dimensions that object valence NEVER has:
    BODY-BASE EXTENSION → Entity-Valence-Dynamics.md §2.


  ABSTRACT ENTITY VALENCE:

    Beyond Object and Agent, there are abstract entities:
      Math, physics, charity, Heaven, "a bright future"...
    
    Abstract entity valence is SPECIAL because:
      → No physical form → NO direct L0
      → Valence ENTIRELY through schema links (§4 Propagation)
      → Can be UNFALSIFIABLE (Heaven, "the meaning of life")
      → → Never receives negative feedback → valence NEVER gets revised
      → → = Designed for maximum valence stability
      → = Agent-Mechanism.md §10: Schema-Imagined-Overlay for abstract agents

    🟡 Abstract entity valence = framework concept
    🟢 Unfalsifiable belief resilience = Popper + Festinger 1957 (cognitive dissonance)
```

---

> **⭐ COMPANION FILE — Per-Entity Valence Dynamics:**
>
> Entity-Valence-Dynamics.md v1.0 details how valence CHANGES per-entity over time:
> Structural vs Current valence, 2-stream/2-layer × visibility,
> 3 Firing Modes, Hardware-Subsidy × VTA habituation,
> Satiation Type × dynamics, Mixed valence, "absence makes the heart grow fonder,"
> per-entity trajectory, extreme valence, phantom resonance, technology frontier.
>
> **Reading order:** §1-§2 above (valence definition) → Entity-Valence-Dynamics.md → §3-§7 below (formation + propagation).

---

## §3 — HOW VALENCE FORMS + UPDATES

```
🟡 VALENCE IS BUILT FROM 4 SOURCES:

  ① DIRECT EXPERIENCE:
    → Hold knife → cut hand → PAIN → valence: { L0 safety: -- }
    → Mother feeds you → HUNGER GONE → valence: { L1 nutrition: ++ }
    → = MOST ACCURATE source — body verifies directly
    → = BUT slow (must experience first to learn)
    → 🟢 Classical conditioning: Pavlov, LeDoux 1996

  ② OBSERVED EXPERIENCE:
    → Watch a friend get bitten by a dog → dog valence: { L0 safety: - }
    → = Self-Pattern-Modeling reads another's state → infers valence
    → = FASTER than direct experience, less accurate
    → 🟢 Observational learning: Bandura 1977
    → 🟢 Social referencing: Sorce 1985

  ③ SCHEMA INHERITANCE:
    → Mother says "knives are dangerous" → valence: { L0 safety: - } (no cut needed)
    → Religion: "God is love" → valence God: { ALL: ++ }
    → = FASTEST (no experience or observation needed)
    → = BUT can be WRONG (inherited schema ≠ verified reality)
    → = WHY propaganda WORKS: installs valence BEFORE verification
    → 🟢 Cultural transmission of fear: Rachman 1977
    → 🟢 Evaluative conditioning via verbal instruction: De Houwer 2007

  ④ CONTEXT INFERENCE:
    → Bomb in an ally's hand: { positive }
    → Bomb in an enemy's hand: { extreme negative }
    → = Same entity, different context → different valence

  ACCURACY vs SPEED — TRADE-OFF:
    ┌──────────────────────────┬────────────────┬──────────────┐
    │ Source                    │ Speed          │ Accuracy      │
    ├──────────────────────────┼────────────────┼──────────────┤
    │ ① Direct experience       │ Slowest        │ Highest       │
    │ ② Observed experience     │ Medium         │ Medium        │
    │ ③ Schema inheritance      │ Fastest        │ Lowest        │
    │ ④ Context inference       │ Context-       │ Chunk-        │
    │                           │ dependent      │ dependent     │
    └──────────────────────────┴────────────────┴──────────────┘
    → Evolutionary: inheriting "snakes are dangerous" is FASTER than being bitten first
    → 🟢 Prepared learning: Seligman 1971


VALENCE UPDATE — 3 TYPES:

  ① REINFORCEMENT — valence grows STRONGER:
    → Mother feeds 1,000 times → valence { L1: ++ } compiled VERY DEEPLY
    → = Consistent repetition → valence COMPILES into deep schema

  ② REVISION — valence GRADUALLY CHANGES:
    → Knife: first cut { L0: -- } → learn to use { L1: ++ gradually overrides L0: -- }
    → Revision speed depends on: intensity × frequency × recency

  ③ VIOLENT FLIP — valence is REVERSED:
    → Close friend betrays: trust++++ → trust---- (FLIP)
    → = VERY RARE but VERY POWERFUL — destroys compiled schema
    → = Anchor-Schema.md §2: flip destroys anchor → cascade collapse
    → 🟢 Betrayal trauma: Freyd 1996

  ⚠️ BIASES IN UPDATE:
    → Negativity bias: negative feedback → updates FASTER than positive
    → Confirmation bias: current valence → filters feedback to match
    → 🟢 Negativity bias: Baumeister et al. 2001
    → 🟢 Confirmation bias: Nickerson 1998
```

---

## §4 — VALENCE PROPAGATION THROUGH SCHEMA CHAIN

> ⚠️ **CLARIFICATION — Chain Analysis = EXPLANATORY, Not Processing**
> *(Drill §6, §22 — GAP 13 RESOLVED)*
>
> Chain analysis = **Level 3** (framework explains why behavior works).
> **NOT** how the brain PROCESSES at **Level 1** — individuals compile SHORT (1-2 nodes).
> Long chains **LIVE at Level 2** (collective infrastructure holds them for individuals).
> Still VALUABLE: diagnose broken chains, design collectives, detect false trust.
> Details on 3-Level Model + 4 compile pathways: Collective-Body.md v1.2 §1-§2.

```
🔴 HYPOTHESIS — new concept, logic consistent with established research,
    not yet formalized in literature under the name "valence propagation"

⭐ CORE INSIGHT:

  Already established in the framework (Schema.md §1):
    Schema = CHUNKS + LINKS + PURPOSE

  Entities do NOT exist in isolation.
    Entities LINK TO EACH OTHER through schema network.
    And valence PROPAGATES through those links.

  EXAMPLE:
    Entity "math" — does it directly feed body-base? → NO.
    BUT "math" LINKS to a chain:
      math → good grades → university → good job → salary → body-base L1 feed
    Positive valence from the END of the chain PROPAGATES BACKWARD:
      salary (+++) → good job (++) → university (+) → good grades (+) → math (+)
    = Math has positive valence BECAUSE it links to a chain ending in body-base feed


⭐ 4 PROPAGATION MECHANISMS:

  ① FORWARD PROPAGATION (learning path):
    Body-base need → find path → action → reward → path COMPILES
    Example: Hungry → find restaurant → eat → no longer hungry → "this place is good" (compile)
    🟢 Operant conditioning: Thorndike's Law of Effect 1898
    🟢 Reinforcement learning: Sutton & Barto 1998

  ② BACKWARD PROPAGATION (reward spread):
    Reward at end of chain → positive valence PROPAGATES BACKWARD through each node
    Example: Salary (reward) → job → university → math (positive because on the path to reward)
    🟢 Temporal difference learning: Schultz 1997 (dopamine prediction error)
    🟡 Explicit "valence backward propagation" = framework formalization

  ③ LATERAL PROPAGATION (generalization):
    Similar entities ALSO receive valence — even without direct experience
    Example: 1 dog bites → fear ALL dogs → fear PEOPLE WHO OWN dogs
    ⚠️ ASYMMETRY: Negative lateral FASTER + WIDER. Positive lateral SLOWER + NARROWER.
    🟢 Stimulus generalization: Pavlov, Watson (Little Albert 1920)
    🟢 Overgeneralization in anxiety: Dunsmoor & Murphy 2015

  ④ INSTALL PROPAGATION (schema inheritance chain):
    Community installs an ENTIRE CHAIN upfront, without experience needed
    Example: Parents install: "don't study → hard life → suffering"
    Example: Religion: "live ethically → Heaven → eternal happiness"
      = ENTIRE chain installed, unfalsifiable → NEVER gets broken
    🟢 Cultural transmission: Boyd & Richerson 1985
    🟡 "Install propagation" = framework term

  4 mechanisms INTERACT:
    Forward finds path → Backward reinforces → Lateral expands → Install provides starting chains
    Installed chain CAN be Forward-VERIFIED or REJECTED

  🟢 Spreading activation: Collins & Loftus 1975
  🟢 Associative network models: Anderson 1983
  🟡 4-mechanism model = framework categorization
```

---

## §5 — CHAIN PROPERTIES + WHY LONG CHAINS PERSIST

### §5.1 — 5 Properties

```
🔴 HYPOTHESIS — framework formalization, logic consistent
  ⚠️ % below = calibration anchor illustrating gradient, NOT precise measurement.

  ① CHAIN LENGTH → VALENCE DECAY + PFC ACCURACY DECREASES:
    SHORT chain (thorn → pain): Valence STRONG. PFC traces 100%.
    MEDIUM chain (math → ... → salary): Valence WEAKER. PFC ~70%.
    LONG chain (multi-branch): Valence COMPLEX. PFC ~30%.
    INVISIBLE chain (hardware): PFC ~10%. "I like math" = a label, not an explanation.
    🟢 Goal gradient: Hull 1932. Temporal discounting: Ainslie 1975.

  ② CHAIN TRUST → PROPAGATION STRENGTH:
    Each link has its own trust level. Propagation ≈ PRODUCT of trusts.
    Trust = 0 at 1 link → CHAIN BREAKS:
      "4 years of university → unemployed" → link collapses → "Education is useless"
    → Anchor-Schema.md §2: Trust ≥ Cost → holds; Trust < Cost → collapse.

  ③ PARALLEL CHAINS → ADDITIVE:
    MANY chains connect entity → body-base SIMULTANEOUSLY → valence = TOTAL
    Single chain WEAK → easy to give up. Multiple parallel → STRONG → hard to give up.
    = Why "passion" = many chains converging on 1 activity

  ④ CONFLICTING CHAINS → MIXED VALENCE:
    Positive chain (mother feeds → L1++) + Negative chain (mother forces studying → autonomy--)
    → SAME entity, 2 opposing chains → LOVE + DISLIKE simultaneously (Entity-Valence-Dynamics.md §7)
    
  ⑤ INVISIBLE CHAINS → PFC CONFABULATION:
    Chain compiled DEEPLY / hardware-level / too long / multi-branch
    → PFC CANNOT access → must explain → CONFABULATES
    → Details: §7

  🟡 5 chain properties = framework formalization
```

### §5.2 — 4-Layer Mechanism for Creating + Maintaining Long Chains

```
🟡 LONG CHAINS = EMERGENT, NOT DESIGNED:

  LAYER 1 — EXIST: Chunk substrate naturally creates chains through connections
    → Spreading activation propagates naturally (Collins & Loftus 1975)
    → Chunks → meta-chunks → schemas → hierarchy (Hebb 1949)
    🟢 Established mechanisms

  LAYER 2 — EXTEND: 4 valence propagation mechanisms lengthen the chain (§4)
    → Forward finds path + Backward reinforces + Install by community
    🟢🟡 Mixed

  LAYER 3 — FIT: Pyramidal compression fits long chain into PFC 4±1
    → 4×4×4 = 64 original pieces of information compressed into 1 slot
    → Long chain = UNCONSCIOUS product, not PFC output
    ⚠️ CORRECTION: "Larger PFC → longer chain" = FALSE
    → 🟢 Brain size vs IQ: ~0.24 correlation (Pietschnig 2015)
    → 🟢 Cowan 2001: PFC holds 4±1 dimensions
    🟢🟡

  LAYER 4 — FILTER: Group selection retains individuals with long chains
    → Layers 1-3 ALREADY SUFFICIENT → Layer 4 = optional
    🟡🔴

  TRADE-OFF: Long chain = feature, NOT bug
    → Harm (individual): PFC blind, trauma chain, unfalsifiable sacrifice
    → Benefit (collective): empathy, deferred investment, cooperation, knowledge transfer
    → P(group benefit) >> P(individual harm) → evolution retains it
```

---

## §6 — CASE ANALYSIS

```
🟡 CASES GROUPED INTO 6 CATEGORIES — verifying the valence system:


  ═══════════════════════════════════════
  GROUP A — DIRECT CHAIN (short, PFC can trace):
  ═══════════════════════════════════════

  A1) Step on thorn → always wear shoes:
    Chain: thorn → pain → L0 threat. Length 1. Direct. 1 time SUFFICIENT.
    PFC accuracy: ~100%. = Per-entity valence, no propagation needed.

  A2) Lighter explodes → fear of lighters:
    Chain: lighter → explosion → pain + shock → L0. Length 1. Direct.


  ═══════════════════════════════════════
  GROUP B — DEFERRED INVESTMENT (long chain, trust):
  ═══════════════════════════════════════

  B1) Student doing math (4 parallel possibilities):
    Chain a: math → grades → university → job → salary → L1 (install, length 4)
    Chain b: don't study → get scolded → L0 threat (install, length 1-2)
    Chain c: hardware fit → Goldilocks → VTA → reward (invisible, intrinsic)
    Chain d: "math is interesting" = PFC label AFTER → reinforces chain c
    → 4 PARALLEL chains, PFC knows a+b, does NOT know c+d

  B2) Jensen Huang — 30 years of Imagine-Final (🟢 public record):
    Phase 1: Anchor-Schema → NVIDIA startup. LONG + DEFERRED chain.
    Phase 2: GPU success → chain VERIFIED → trust INCREASES.
    Phase 3: Billionaire, 60+. Body-base ALREADY sufficient. Drive still strong.
      → Anchor-Schema EVOLVES + intrinsic mastery + novelty still fires.
    ⚠️ Which internal schemas drive him = ONLY HE KNOWS. Framework only INFERS.


  ═══════════════════════════════════════
  GROUP C — MIRROR CHAIN ("giving," invisible):
  ═══════════════════════════════════════

  C1) Child helps mother:
    Chain 1: deep compiled valence for mother: {++}
    Chain 2: Self-Pattern-Modeling → empathy dissonance.
    Chain 3: helping → mother happy → opioid.
    Chain 4: reciprocity schema → identity.
    PFC: "Because mother always helps me" — knows chain 4, does NOT know chains 2+3.

  C2) "Selflessly" helping a stranger:
    Chains 1-5: lateral overgeneralization + empathy + status + identity + connection
    PFC: "Just doing it" — does NOT know the 5 chains. Feel-Explanation label.


  ═══════════════════════════════════════
  GROUP D — SCHEMA INHERITANCE (installed, unfalsifiable):
  ═══════════════════════════════════════

  D1) Dutch family hiding Jews in WWII (🟢 documented):
    Schema inheritance + empathy + identity + anchor + connection = 5 chains
    → 5 chains > L0 cost (death penalty!) → body drives "hide them"
    🟢 Yad Vashem: ~28,000 "Righteous Among Nations"

  D2) Believing in Heaven → overcoming hardship:
    Unfalsifiable chain. Body STILL feeds even though content is unverified:
    "Living ethically" → community acceptance → connection feed.
    = Schema effectiveness ≠ Schema truthfulness (§7)

  D3) "Rich = happy" → achieving it then emptiness:
    Installed chain promises ALL channels. Reality: L1 feed ONLY.
    Path sacrifices connection + health → achieve wealth → MISMATCH.
    BUT: wealth WHILE maintaining relationship + health → NO emptiness.


  ═══════════════════════════════════════
  GROUP E — MISLINK (mechanism correct, content wrong):
  ═══════════════════════════════════════

  E1) Cold-blooded murderer:
    Schema MISLINK: causing harm → CONTROL → mastery → reward.
    Hardware typically NOT broken: IQ average+. Chunks OK. Chain is wrong.
    🟢 Hickey 2013: serial killers report "power" and "control"

  E2) Irrational revenge (spend $200K to win a $100K case):
    L1 cost: -$200K. BUT chains 1-3: dissonance resolved + identity + Schadenfreude >> cost.
    🟢 Costly punishment: Fehr & Gächter 2002
    🟢 Schadenfreude: Takahashi et al. 2009


  ═══════════════════════════════════════
  GROUP F — OVERGENERALIZE (lateral propagation):
  ═══════════════════════════════════════

  F1) Bitten by dog → fear all dogs → dislike dog owners:
    Direct → category → associated entity. Negative: FASTER + WIDER.

  F2) Positive childhood → default trust of strangers:
    SAME MECHANISM, different direction. BUT requires MORE experience (negativity bias).
```

---

## §7 — PFC BLINDNESS + 3 PRINCIPLES

### §7.1 — PFC Blindness

```
🟡 WHY PFC USUALLY DOESN'T KNOW THE VALENCE CHAIN:

  Feeling.md v3.0 §2: 7 LAYERS — fidelity DECREASES upward:
    Feel-RawSignals → Feel-Location: body → integration → chunk match (valence chain operates here)
    Feel-Labeling (40-80%). Feel-Explanation (20-70%)
    PFC OBSERVES from Feel-Labeling upward → sees OUTPUT, NOT the MECHANISM.

  3 LEVELS OF PFC AWARENESS:

  ① PFC KNOWS (~80-100%): short + direct + recent chain
    "I'm afraid of thorns because I got hurt that one time" — chain length 1

  ② PFC KNOWS PARTIALLY (~40-70%): medium chain + installed
    "I study because of the future" — correct at SURFACE, MISSING detail

  ③ PFC DOES NOT KNOW (~10-30%): invisible, hardware, compiled chain
    "I like giving to charity" — PFC: "just doing it." Body: many compiled chains firing.
    "I'm passionate about physics" — PFC: "because it's interesting." Body: hardware + Goldilocks.
    → PFC CONFABULATES: finds reasons that FIT but are NOT the mechanism

  ⭐ "SELFLESS GIVING" AND "PASSION" — 2 MOST COMMON CONFABULATIONS:
  
    "GIVING SELFLESSLY": PFC doesn't see chains. Body: empathy + identity + status + reciprocal.
    EVIDENCE IT IS NOT "SELFLESS" — 3 violation tests:
      Test 1: STOPS when body-base is depleted (starving → won't give their own food)
      Test 2: STOPS when schema betrays (charity fraud discovered → stops donating)
      Test 3: STOPS when reciprocity = 0 sustained over time
    → If truly "selfless" → would NOT stop. But it stops → there are conditions.

    "PASSION": PFC label for "many chains converging → strong sustained drive"
    "Passion" is NOT the cause of behavior — it is a DESCRIPTION of the result
    = Drive.md §0: "'Passion' = DESCRIPTION of strong + sustained drive, NOT the cause"

  🟢 Confabulation: Nisbett & Wilson 1977
  🟢 Readiness potential: Libet 1983
  🟢 Split-brain confabulation: Gazzaniga
```

### §7.2 — 3 Principles

```
⭐ 3 IMPORTANT PRINCIPLES:

  PRINCIPLE 1 — Schema Effectiveness ≠ Schema Truthfulness:
    A schema can be completely wrong AND STILL be effective:
      Believing in Heaven → behavioral output (diligence + ethics) → body feeds → EFFECTIVE
    A schema can be true AND STILL fail:
      "Rich = happy" → path sacrifices connection → FAILS
    → 2 SEPARATE dimensions: true+effective, true+fails, false+effective, false+fails

  PRINCIPLE 2 — Body Checks OUTPUT, Not TRUTH:
    Body does NOT verify chain content. Body ONLY verifies chain output.
    → Body = PRAGMATIST, not SCIENTIST
    → Wrong schema PERSISTS LONG if output still feeds body-base
    → Right schema GETS REJECTED if output does NOT feed
    → PFC ONLY checks truth when TRIGGERED (dissonance, forced evaluation)

  PRINCIPLE 3 — "Selfless" Is Correct at PFC Level, Wrong at Body Level:
    PFC LEVEL: "I want nothing in return" = ACCURATE DESCRIPTION of conscious experience
    BODY LEVEL: Compiled patterns ALWAYS fire, ALWAYS have reward
    BOTH ARE CORRECT — at their respective levels.
    → Knowing the mechanism does NOT REDUCE the value of "giving"
    → Framework purpose: to UNDERSTAND, not to JUDGE
```

### §7.3 — Fundamental Limits

```
🟡 INFINITE SCHEMAS → CHAIN CANNOT BE MAPPED PRECISELY:

  86 billion neurons × ~100 trillion connections = system far too large
  Schema is MULTI-MODAL (body + motor + visual + somatic + emotional + verbal)
  → Chain A→B→C→...→body-base: we know it EXISTS, we cannot map it exactly

  Humans do NOT NEED precise mapping:
    ① Know WHICH PATTERN is driving (recognition, not precision needed)
    ② Know whether pattern SERVES body-base OR NOT (check output)
    ③ Know WHEN CHANGE IS NEEDED (detect dissonance)
  → Framework = "navigation tool, not a precise GPS"

  ⚠️ BLACKBOX 2: Valence complexity — long valence chains are nearly incomputable.
  Framework predicts PATTERNS, not INSTANCES. Details: Blackbox-Map.md §4+§7.
```

---

## §8 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (~20 claims)
═══════════════════════════════════════

  Valence definition (§1-§2):
    Multi-channel emotional processing: established
    Mixed feelings (ambivalence): Cacioppo & Berntson 1994
    Fear conditioning + evaluative conditioning: LeDoux 1996, De Houwer 2007
    Nisbett & Wilson 1977: PFC cannot access actual processing
    Unfalsifiable belief resilience: Popper + Festinger 1957

  Valence formation + propagation evidence (§3-§5):
    4 sources: classical conditioning, observational (Bandura), cultural (Rachman), context
    Spreading activation: Collins & Loftus 1975
    Temporal difference learning: Schultz 1997
    Goal gradient: Hull 1932. Temporal discounting: Ainslie 1975
    Stimulus generalization: Pavlov, Watson. Overgeneralization: Dunsmoor & Murphy 2015
    Prepared learning: Seligman 1971
    Betrayal trauma: Freyd 1996
    Negativity bias: Baumeister et al. 2001. Confirmation bias: Nickerson 1998

  PFC blindness (§7):
    Confabulation: Nisbett & Wilson 1977
    Readiness potential: Libet 1983
    Split-brain: Gazzaniga

  Per-entity valence dynamics → Entity-Valence-Dynamics.md v1.0 §14.


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (~8 claims)
═══════════════════════════════════════

  §1-§2: Valence as multi-channel PROFILE, Object vs Agent vs Abstract
  §3: 4 sources as explicit model + 3 update types
  §4: 4 propagation mechanisms as explicit model
  §5: 5 chain properties + 4-layer long chain
  §7: 3 principles (effectiveness≠truthfulness, output check, "selfless" at 2 levels)

  Per-entity dynamics synthesis → Entity-Valence-Dynamics.md v1.0 §14.


═══════════════════════════════════════
🔴 HYPOTHESIS (~4 claims)
═══════════════════════════════════════

  Valence propagation as EXPLICIT NAMED MODEL
  Backward propagation (abstract chain)
  Chain trust = product of link trusts (oversimplified)
  Group selection for long chains (optional, Layer 4)


OPEN QUESTIONS:
  → Specific neural mechanism for valence propagation? Brain regions?
  → Chain decay function: linear? exponential? step?
  → Maximum chain length that body still trusts?
  → Positive overgeneralization: same mechanism but HOW MUCH DIFFERENT speed?
```

---

## §9 — CROSS-REFERENCES + CITATIONS

```
CROSS-REFERENCES:

  FOUNDATIONS:
    → Body-Base.md v3.3 — L0+L1 substrate + observation parameters
    → Body-Feedback-Mechanism.md v2.0 — Body-Need aggregate, chunk dynamics
    → Schema.md v2.0 — schema = chunks + links + purpose
    → Chunk.md v2.2 — chunk substrate, context-tag, 4 connections
    → Reward-Signal-Architecture.md v2.1 — Evaluative/Direct-State × valence
    → Body-Feedback-Label.md v2.0 — vocabulary reference

  COMPANION FILE (per-entity valence dynamics):
    → Entity-Valence-Dynamics.md v1.0 — Structural/Current, 3 Firing Modes,
      Hardware-Subsidy, Satiation Type, Mixed valence, Phantom resonance,
      Technology frontier. READ AFTER §1-§2, BEFORE §3-§7.

  PFC + OBSERVATION:
    → Feeling.md v3.0 — PFC observation of body (7 layers)
    → Drive.md — synthesizes valences → action
    → Self-Pattern-Modeling.md v3.1 — observed experience (§3 source ②)
    → Agent-Mechanism.md v2.1 — Schema-Imagined-Overlay (§2 abstract entities)

  PROPAGATION CONTEXT:
    → Collective-Body.md v1.2 — 3-Level Model + trust bridge (§4)
    → Anchor-Schema.md v1.2 — anchor amplifies chain, trust ≥ cost (§3, §5)
    → Drill-Emergent-Pattern.md §5 — "Giving" pattern (§6 cases)
    → Empathy.md v2.2 §6-§8 — empathy reward, burnout formula (§6 cases)
    → Somatic-Articulation-Loop.md — body → explicit knowledge

  APPLICATION:
    → AI-Schema-Detection.md v2.0 — pattern detection
    → Imagine-Final-Evaluation.md — Mismatch quadrant
    → Blackbox-Map.md §4+§7 — BLACKBOX 2 chain complexity


RESEARCH CITATIONS:

  | # | Citation | Used in |
  |---|----------|---------|
  | R1 | LeDoux 1996 — Fear conditioning | §1 |
  | R2 | De Houwer 2007 — Evaluative conditioning | §1, §3 |
  | R3 | Nisbett & Wilson 1977 — PFC confabulation | §1, §7 |
  | R4 | Festinger 1957 — Cognitive dissonance | §2 |
  | R5 | Bandura 1977 — Observational learning | §3 |
  | R6 | Rachman 1977 — Cultural fear transmission | §3 |
  | R7 | Seligman 1971 — Prepared learning | §3 |
  | R8 | Freyd 1996 — Betrayal trauma | §3 |
  | R9 | Baumeister et al. 2001 — Negativity bias | §3 |
  | R10 | Nickerson 1998 — Confirmation bias | §3 |
  | R11 | Schultz 1997 — Dopamine prediction error / VTA | §4 |
  | R12 | Dunsmoor & Murphy 2015 — Overgeneralization in anxiety | §4 |
  | R13 | Boyd & Richerson 1985 — Cultural transmission | §4 |
  | R14 | Collins & Loftus 1975 — Spreading activation | §4, §5 |
  | R15 | Hull 1932 — Goal gradient | §5 |
  | R16 | Ainslie 1975 — Temporal discounting | §5 |
  | R17 | Pietschnig 2015 — Brain size vs IQ | §5 |
  | R18 | Cowan 2001 — PFC 4±1 | §5 |
  | R19 | Hebb 1949 — Hebbian learning | §5 |
  | R20 | Fehr & Gächter 2002 — Costly punishment | §6 |
  | R21 | Takahashi et al. 2009 — Schadenfreude | §6 |
  | R22 | Hickey 2013 — Serial killers | §6 |
  | R23 | Libet 1983 — Readiness potential | §7 |
```

---

## Changelog

```
v1.0 — 2026-06-11 — English translation from source v4.1 (2026-05-29)
  → Full translation of §0–§9
  → Complete TOC added
  → All 4 propagation mechanisms translated
  → PFC blindness + 3 principles + fundamental limits
  → All 23 research citations preserved
  → Companion file note (Entity-Valence-Dynamics.md v1.0) preserved
```

---

> **END OF Valence-Propagation.md v1.0 (English)**
> Source: Human-Predictive-Drive/Core-Deep-Dive/Body-Base/Valence-Propagation.md v4.1 (2026-05-29)
> Translated: v1.0 — 2026-06-11
> Sections: §0–§9 + TOC + Changelog
> Confidence: 🟢 ~20 citations / 🟡 ~8 framework synthesis claims / 🔴 ~4 hypotheses
