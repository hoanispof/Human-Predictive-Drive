---
title: Inter-Body Mechanism — Why and How Two Body-Bases Interact
version: 2.1
created: 2026-05-16
updated: 2026-05-31
refined: |
  2026-05-31 (v2.1 — §4.2 PFC Draft Cost: glucose/metabolic → processing load.
    Gailliot→Kurzban+Musslick+Arnsten. Cross-ref PFC-Operations v1.3 §8.3)
  2026-05-23 (v2.0 — Architecture Rename: Architecture A → Hardwired Architecture,
    Architecture B → Compilable Architecture. Descriptive names throughout)
  2026-05-23 (v1.1 — Concept Cascade: +refs to ALL formal files from 28-session Drill.
    Updated versions. +Simulation-Engine, +Entity-Access, +Hardware-Subsidy)
status: MECHANISM FILE v2.1
scope: |
  SOURCE-OF-TRUTH for inter-body interaction architecture.
  8 foundational principles from drill session 2026-05-16
    (6 rounds, 2,259 lines + 409-line summary).
  This file formalizes the "missing layer" the framework implicitly assumed:
    ① 3 hardware foundations → Compilable Architecture
    ② Body-Need = 2-source aggregate
    ③ Compiled vs Fresh = the real axis (not Feeling/Logic)
    ④ 3 independent cost sources
    ⑤ Full interaction chain (Detect→Evaluate→Extend→Outcome→Compile/Dissolve)
    ⑥ 5-Channel Input Vector
    ⑦ PFC = Lawyer not Judge
    ⑧ Entity-Compiled reframe (3 subtypes)
    ⑨ 3-Layer Evolution (Hardware→Compiled→Cultural)
  Other files cross-reference this file for new concepts.
purpose: |
  Body-Feedback-Mechanism.md describes how 1 body CREATES signals.
  Gap-Direction.md describes how gaps HAVE direction.
  Self-Pattern-Modeling.md describes how 1 body SIMULATES another entity.
  Connection.md describes how the observation parameter "Connection" emerges.
  THIS FILE = the MIDDLE LAYER: WHY does the body-base NEED other entities,
  BY WHAT MEANS does it detect + evaluate + interact, and WHAT MECHANISM
  determines sustainability vs dissolution.
  = "Missing mechanism file" — all other inter-body files implicitly assumed this.
position: |
  Core-Deep-Dive/Body-Base/ — same level as Body-Base.md, Body-Coupling.md.
  Mechanism file: Self-Pattern-Modeling, Resonance, Connection, Agent-Mechanism
    cross-reference here.
  Moved from Drill-Inter-Body-Mechanism/ (2026-05-22) — mechanism file, not drill.
language: English translation of Vietnamese source (v2.1)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
source: Core-Deep-Dive/Body-Base/Inter-Body-Mechanism.md (Vietnamese)
---

# Inter-Body Mechanism — Why and How Two Body-Bases Interact

> **Each body = one distinct world. Its own emotions, its own gaps, its own drives.**
> **But no body can exist alone.**
>
> The question: WHY and HOW do two separate worlds
> manage to feed each other?
>
> The answer: Evolution did not hardwire WHAT to need — only HOW to need.
> General-purpose reward + compilation + social hardware = Compilable Architecture.
> Compilable Architecture = can adapt to ANY environment, but requires 15-20 years to compile.
> Those 15-20 years = requires other entities to protect, feed, teach.
> → Social is NOT a luxury. Social = an architecture requirement.

---

## Table of Contents

- §0 — THESIS + POSITION
- §1 — 3 HARDWARE FOUNDATIONS → COMPILABLE ARCHITECTURE
- §2 — BODY-NEED: 2-Source Aggregate
- §3 — COMPILED vs FRESH: The Real Axis
- §4 — 3 INDEPENDENT COST SOURCES
- §5 — INTER-BODY FULL CHAIN
- §6 — 5-CHANNEL INPUT VECTOR
- §7 — PFC = LAWYER (not Judge)
- §8 — ENTITY-COMPILED: Multi-Channel Valence
- §9 — 3-LAYER EVOLUTION
- §10 — HUMAN ↔ AI: Position in the Picture
- §11 — HONEST ASSESSMENT
- §12 — CROSS-REFERENCES + RESEARCH

---

## §0 — THESIS + POSITION

### §0.1 — Thesis

```
CORE CLAIM:

  Body-base = general-purpose reward + compilation + social hardware.
  Everything else = EMERGES from these 3 foundations.

  Inter-body interaction = NOT an optional feature.
  = ARCHITECTURE REQUIREMENT of a general-purpose reward system.

  Because:
  ① The body needs external input to compile (information, capability, feedback)
  ② Social hardware = hardwired (oxytocin, μ-opioid, dACC reuse)
  ③ Alone = deviation from baseline, costly (Coan & Sbarra 2015)
  ④ Compilable Architecture requires 15-20 years to compile
       → requires other entities to provide protection during that time

  → The interaction mechanism = FOUNDATION, not an add-on.
```

### §0.2 — Position in the Framework

```
THIS FILE answers:
  WHY: Why does the body NEED other entities? (§1, §2)
  HOW: By what means does it detect, evaluate, interact? (§5, §6, §7)
  WHAT DETERMINES: What determines sustainability vs dissolution? (§3, §4, §8)

FRAMEWORK MAP:
  Body-Feedback-Mechanism → HOW 1 body creates signals
  Gap-Direction           → WHERE gaps point
  Autonomy-Hardware       → WHY self-directed action is rewarded
  ★ Inter-Body-Mechanism  → WHY + HOW 2 bodies interact ← THIS FILE
  Self-Pattern-Modeling   → HOW to predict others (mechanism)
  Resonance               → WHEN mutual quality emerges (observation)
  Connection              → WHAT connection is (observation parameter)
  Agent-Mechanism         → Integration hub (Self-Pattern-Modeling + Resonance + overview)

  What level?
  = MECHANISM file: explains the foundational mechanism
  = NOT observation (Connection, Resonance = observation)
  = NOT integration hub (Agent-Mechanism = hub)
  = "Missing middle layer" between 1-body mechanism and multi-body observation
```

### §0.3 — 8 Synthesized Principles (preview)

```
8 PRINCIPLES from the drill session:

  ① Body-Need = 2-source aggregate (hardware + chunk dynamics)
  ② General-Purpose Reward = Compilable Architecture (HOW not WHAT)
  ③ Social = Architecture Requirement (4 reasons)
  ④ By-Product Match (B fills B's own gap → output matches A → A receives reward)
  ⑤ 3 Independent Cost Sources (PFC draft + Suppress + Uncertainty)
  ⑥ Compiled vs Fresh = the Real Axis (NOT Feeling/Logic content)
  ⑦ Input Channel Control = Power (5 channels)
  ⑧ Domain Reality = Final Arbiter (ALWAYS)

  Each principle = 1 detailed section below.
```

---

## §1 — 3 HARDWARE FOUNDATIONS → COMPILABLE ARCHITECTURE

### §1.1 — Evolution Hardwires 3 Things

```
⭐ Everything in the inter-body mechanism EMERGES from 3 foundations:

┌─────────────────────────────────────────────────────────┐
│ ① GENERAL-PURPOSE REWARD                                │
│                                                         │
│   VTA/dopamine + opioid system.                         │
│   Fires for ANY gap fill in the correct direction.      │
│   Does NOT check content ("is this edible?" → irrelevant)│
│   Only checks: "did the gap direction get matched?"     │
│                                                         │
│   → Einstein solving an equation = REAL body reward     │
│   → Because body-need is NOT only survival              │
│   → Body-need = ANY compiled gap fill                   │
│                                                         │
│   🟢 Neuroscience established: VTA, nucleus accumbens,  │
│      dopamine prediction error (Schultz 1997)            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ② COMPILATION CAPABILITY                                │
│                                                         │
│   Hebbian: "whatever works → strengthen → automatic"    │
│   Fresh → repeat + verify → compile → "feels right"    │
│   = Body LEARNS from experience, without conscious plan │
│                                                         │
│   → Skill compile: driving on day 1 vs day 1,000        │
│   → Social compile: stranger → close friend over years  │
│   → Expert compile: therapist sees 1,000 cases →        │
│     "intuition" (actually = compiled patterns)           │
│                                                         │
│   🟢 Hebbian learning established.                       │
│   🟢 Expert intuition = compiled (Kahneman 2011,         │
│      Klein 1998 recognition-primed decisions)            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ ③ SOCIAL HARDWARE                                       │
│                                                         │
│   Oxytocin (bonding): fires during touch, eye contact,  │
│     trust                                               │
│   μ-opioid (social play reward): same system as food    │
│   dACC reuse: social pain = physical pain circuits      │
│   Social = DEFAULT state (Coan & Sbarra 2015)           │
│   Body REQUIRES social input to maintain architecture   │
│                                                         │
│   → Alone = deviation, body must WORK to be alone       │
│   → Social = baseline, body RELAXES with others         │
│   → Social rejection = LITERAL pain (same dACC)         │
│                                                         │
│   🟢 Eisenberger 2003: social-physical pain overlap      │
│   🟢 Panksepp 1998: μ-opioid in social play             │
│   🟢 Coan & Sbarra 2015: Social Baseline Theory         │
└─────────────────────────────────────────────────────────┘
```

### §1.2 — Compilable Architecture: General-Purpose Adaptive

```
COMBINING ①②③ = COMPILABLE ARCHITECTURE:

  HARDWIRED ARCHITECTURE (specific-reward — insects, simple animals):
    Hardwired circuits: food→reward, mate→reward, escape→reward
    Each survival need = its own dedicated circuit
    ADVANTAGE: fast, precise for STABLE environments
    DISADVANTAGE: environment changes → species die (cannot adapt)

  COMPILABLE ARCHITECTURE (general-purpose — humans):
    Hardwired: ONLY the reward MECHANISM + compilation + social + PFC
    Content: LEARNED from environment/culture → compiled → body-need
    ADVANTAGE: can adapt to ANY environment
    DISADVANTAGE: requires 15-20 YEARS to compile (long childhood, dependent)

  → Trade-off: NEEDS parents + group to provide protection during compilation
  → = WHY social = architecture requirement, NOT a luxury

🟡 Hardwired/Compilable Architecture naming = framework synthesis.
   Underlying neuroscience (general-purpose reward, Hebbian) = 🟢.
```

### §1.3 — 4 Reasons Social = Architecture Requirement

```
⭐ Social is NOT "nice to have" — it is a REQUIREMENT:

REASON 1 — SURVIVAL MATH:
  1 person CANNOT survive alone efficiently.
  Hunter-gatherer: group of 30-150 → shared tasks → all survive.
  Alone: must hunt + gather + build shelter + defend + heal ALL → die.
  = Social = survival PREREQUISITE.
  = Social DRIVE got HARDWIRED into the body.

REASON 2 — COMPILATION REQUIRES SOCIAL:
  Compilable Architecture needs to compile from experience.
  Child ALONE: compiles only from personal experience → SLOW, DANGEROUS.
  Child IN GROUP: can observe + receive teaching + imitate → FAST, SAFE.
  = Without social: the Compilable Architecture advantage is NULLIFIED.
  = Social = ACCELERATOR for compilation.

REASON 3 — REUSED NEURAL CIRCUITS:
  🟢 Eisenberger 2003: social pain = SAME dACC as physical pain.
  → Body treats "social absence" LIKE "injury" (literally same circuit).
  Oxytocin system: touch, eye contact → reduce cortisol.
  μ-opioid: social play → SAME reward system as food pleasure.
  → Body REWARDS social engagement LIKE food (Panksepp 1998).

REASON 4 — SOCIAL BASELINE THEORY:
  🟢 Coan & Sbarra 2015: body DEFAULT = social present.
  Alone = DEVIATION → requires EXTRA energy (vigilance, self-regulation).
  With others = body RELAXES (less cortisol, less threat scanning).
  = Social is BASELINE — alone is SUBTRACTION.
  = Body must WORK to be alone (not work to be social).
  = Solitude = energy cost. Company = energy saved.
```

---

## §2 — BODY-NEED: 2-Source Aggregate

### §2.1 — Definition

```
BODY-NEED = the aggregate of current NEED states
           = the aggregate of ALL signals currently demanding body response

  NOT a single signal → is an AGGREGATE of many parallel signals.
  NOT created by PFC → body-need exists BEFORE PFC awareness.
  NOT only survival → ANY compiled gap fill (Compilable Architecture feature).
```

### §2.2 — 2 Genuine Sources

```
⭐ 2 SOURCES (consistent with Body-Feedback-Mechanism.md §2):

┌─────────────────────────────────────────────────────────────┐
│ ① HARDWARE / SENSORY-DRIVEN (pre-chunk possible):           │
│                                                             │
│   Homeostatic: hunger, thirst, temperature, oxygen, sleep   │
│   Nociceptive: pain, injury, reflex                         │
│   Hormonal: social isolation hardware, sexual drive          │
│                                                             │
│   → Domain stimulus → receptors → body signal               │
│   → Does NOT require compiled chunks (animals have it fully)│
│   → D+C zones primary (Body-Base.md: L0 + L1 substrates)   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ ② CHUNK DYNAMICS / PATTERN-DRIVEN:                          │
│                                                             │
│   3 dynamics: Gap / Miss / Shift (+ Compound)               │
│   → Internal chunk fires → body responds                    │
│   → REQUIRES compiled chunks as prerequisite                │
│   → Dominant in humans (rich chunk network)                 │
│                                                             │
│   Complexity spectrum (same mechanism, different substrate): │
│     Simple:  soft fabric baseline → rough fabric = Miss     │
│     Social:  close friend absent = Miss; entity shift = Shift│
│     Meta:    Imagine-Final = Gap; Obligation violated = Miss │
│              Identity conflict = Gap; Status drop = Miss     │
│                                                             │
│   ⭐ Meta-level = NOT a separate mechanism:                  │
│     = Same Gap/Miss/Shift operating on meta-compiled chunks │
│     = Differs in timescale + PFC involvement + intervention │
│     = Does NOT need a separate third layer → PARSIMONY      │
└─────────────────────────────────────────────────────────────┘

  ⭐ 2 sources are NOT exclusive — 1 event can trigger BOTH ①+②:
    Example: eating food (① sensory) + remembering a better meal from before (② Miss)
    Example: social isolation (① hardware oxytocin deficit + ② compiled friend Miss)
```

### §2.3 — Cross-Cutting: What Are NOT Sources

```
OBSERVATION PARAMETERS (named patterns, v7.8):
  Protect = ownership chunks + loss aversion + avoidance direction
  Threat  = urgency tag + priority override (from ANY source)
  Status  = relative position pattern
  Novelty = gap-fill drive + approach direction
  → EMERGE FROM ①+② in specific combinations
  → NOT a separate source — they are NAMES FOR observable patterns
  → Intervention happens at the mechanism level (①②), not at the label level

STATE MODIFIERS:
  Cortisol: amplifies negative signals (Cortisol-Baseline.md v2.0)
  Urgency: overrides priority ranking
  Energy/fatigue: shifts threshold for all signals
  → Do NOT create new body-needs — SHIFT priority/intensity of existing ones

🟡 Observation params + state modifiers as cross-cutting (not sources) =
   framework clarification. Consistent with Protect.md §0.
```

### §2.4 — 7 Properties

```
BODY-NEED HAS 7 PROPERTIES:

  ① ALWAYS EXISTS (never = 0)
     → "Relaxing on the beach" still has: sun warming the skin = sensory gap fill
     → If gap = 0 → drive = 0 → behavior = 0 → death

  ② MULTIPLE simultaneously (parallel)
     → Hungry + bored + missing a friend + career anxiety = 4 body-needs in parallel

  ③ HAS PRIORITY (intensity × urgency × state)
     → "Building on fire" overrides "bored" (survival > novelty)
     → Priority = dynamic, shifts with state

  ④ HAS DIRECTION (from chunk network topology — Gap-Direction.md)
     → Only filling in the correct direction rewards
     → Direction = f(surrounding chunks) → unique per person

  ⑤ PFC DOES NOT ALWAYS KNOW (exists before awareness)
     → "Bored but don't know what I need" = body-need present, PFC hasn't identified it
     → PFC guesses the wrong direction = "scrolling" instead of "exercise"

  ⑥ CAN CONFLICT (internal tension)
     → "Tasty food vs slim figure" = 2 body-needs, opposite directions
     → PFC arbitrates → suppresses one → cost (§4)
     → Internal conflict = NORMAL, not pathological

  ⑦ CAN BE HIJACKED (temporary distortion)
     → Hormone (limerence): amplifies 1 body-need → overrides all others
     → Scam: controls input channels → direction distorted
     → Propaganda: collective fear → priority override
     → Domain Reality = final arbiter ALWAYS (§7)
```

### §2.5 — 4 Types by Immediacy

```
┌─────────────────────────────────────────────────────┐
│ IMMEDIATE (seconds-minutes):           [① dominant] │
│   Hunger, pain, heat. PFC knows clearly.            │
│   Direction is clear.                               │
├─────────────────────────────────────────────────────┤
│ SHORT-TERM (hours-days):              [①+② mix]    │
│   Boredom, loneliness, fatigue.                     │
│   PFC MAY NOT know clearly                          │
│   (scrolling but actually needs exercise).          │
├─────────────────────────────────────────────────────┤
│ LONG-TERM (months-years):          [② meta dominant]│
│   Career, Imagine-Final, relationship direction.    │
│   PFC BUILDS direction over many years.             │
├─────────────────────────────────────────────────────┤
│ STRUCTURAL (always running):   [①hardware + ②structural]│
│   Social belonging. Autonomy. Coherence.            │
│   PFC usually NOT AWARE (until violated).           │
└─────────────────────────────────────────────────────┘
```

---

## §3 — COMPILED vs FRESH: The Real Axis

### §3.1 — Reframe: NOT Feeling vs Logic

```
⭐ THE REAL AXIS: COMPILATION LEVEL

THE FRAMEWORK USED TO SAY:
  Compiled = "Feeling" (body-level, automatic)
  Fresh = "Logic" (PFC chain, deliberate)

THE DEEPER REALITY:
  Compiled = automatic processing (body-feedback direct, cost ≈ 0)
  Fresh = PFC deliberate draft (costly, not yet compiled)

  → "Feeling" and "Logic" = LABELS from an observer perspective
  → Inside the body: only the COMPILED ←→ FRESH spectrum exists
  → Content (emotion/reasoning) does NOT determine Compiled/Fresh
  → COMPILATION LEVEL determines it

🟡 Compiled/Fresh reframe = framework synthesis.
   Consistent with Kahneman System 1/2, expertise research.
```

### §3.2 — Evidence: Content ≠ Processing Level

```
① Einstein + familiar math = COMPILED:
   Content = math ("logic"). But compiled → automatic → Einstein "feels" the answer.

② A stranger trying to guess another stranger's emotion = FRESH:
   Content = emotion ("feeling"). But fresh → deliberate → "must reason through it."

③ Chef tastes food → instantly knows it needs more salt = COMPILED:
   Content = complex. But compiled → near-instant → "intuition."

④ A therapist encounters a new case = FRESH:
   Content = psychology ("feeling"). But fresh → PFC draft → "must analyze."

→ THE AXIS:
  COMPILED ─────────────────────────────── FRESH
  (automatic)                             (PFC draft)
  body-direct                             PFC-mediated
  cost ≈ 0                                cost > 0
  "feels right"                           "thought it through"
  immediate                               requires time
  Hebbian reinforced                      every time = effort
```

### §3.3 — Transition: Learning + Unlearning

```
FRESH → COMPILED (Learning):
  Repetition + verify OK → Hebbian strengthens → becomes automatic
  = "Logic → feeling" (for that person, in that domain)
  Einstein: physics FRESH (as a child) → COMPILED (as an adult)
  Driver: driving FRESH (day 1) → COMPILED (day 1,000)

COMPILED → FRESH (Unlearning / Re-learning):
  Disrupted (new context, trauma, error detected) → must go FRESH again
  = "Feeling → logic" (must rethink what was automatic)
  Lost trust: close friend betrays → COMPILED positive disrupted
    → FRESH re-evaluation
  Career shift: old domain compiled → new domain = FRESH start from scratch
```

### §3.4 — "Shareable Compiled" vs "Non-Shareable Compiled"

```
⭐ INSIGHT: "Logic vs Intuition" = a naming artifact, not a mechanism difference

MATHEMATICS:
  Compiled chunks: 2+2=4 (SHARED — same for everyone)
  Reproduction: Expert A and Expert B get the same result (verifiable)
  Global label: "LOGIC" (because shared + reproducible)

PSYCHOLOGY:
  Compiled chunks: patterns from 1,000+ cases (UNIQUE to each expert)
  Reproduction: Expert A and Expert B MAY reach different conclusions
    (different case histories)
  Global label: "INTUITION / FEELING" (because not perfectly reproducible)

INSIDE BOTH: SAME PROCESS — compiled chunks fire → body-direct → "knowing"
  Mathematician: years of compilation → chunks fire fast → "sees" the solution
  Therapist: years of compilation → chunks fire fast → "sees" the pattern
  BOTH = compiled chunks fire → body-direct. Difference: WHICH chunks (domain-specific).

THE DIFFERENCE:
  Math: subject = DETERMINISTIC → compiled chunks CONVERGE
  Psychology: subject = PROBABILISTIC + INDIVIDUAL → compiled chunks DIVERGE
  → The therapist is NOT "guessing"
  → The domain is non-deterministic → divergent compiled patterns are LEGITIMATE
  → Domain reality = patient outcomes = final arbiter (as always)

FRAMEWORK REFRAME:
  "Logic"     = compiled chunks that are SHAREABLE (deterministic domain)
  "Intuition" = compiled chunks NOT EASILY SHAREABLE (probabilistic domain)
  DIFFERENCE: shareability. NOT DIFFERENT: quality of processing.

🟢 Expert intuition = compiled patterns (Kahneman 2011, Klein 1998).
🟡 "Shareable vs non-shareable" as organizing principle = framework synthesis.
```

### §3.5 — Implication: PFC = Lawyer + Learning Trajectory

```
⭐ TWO ARCHITECTURAL PRINCIPLES:

  ① PFC = LAWYER (not Judge):
    → Body-need fires FIRST
    → Body creates DRIVE toward action
    → PFC creates the NARRATIVE ("reason") for what the body ALREADY wanted
    → The person BELIEVES the narrative
    → 🟢 Gazzaniga split-brain, Haidt 2001, Nisbett & Wilson 1977
    → PFC serves the body-base — all "logic" ultimately serves body architecture

  ② LEARNING TRAJECTORY moves toward Body-Knowing:
    → Fresh processing = a temporary phase BEFORE compilation
    → Repeat + domain verify OK → Hebbian strengthens → automatic → Body-Knowing
    → "Logic" for one person = "Body-Knowing" for an expert in that domain
    → Math = "fresh/logic" on day 1 → "Body-Knowing" after years
    → = THE DESTINATION OF LEARNING = compiled body-direct (Body-Knowing)

  ⚠️ v4.0 NOTE:
    → Older versions wrote: "humans are 100% feeling at the foundational level"
    → Terminology RETIRED (Logic-Feeling.md v4.0 §4.3):
      "100% feeling" causes collision between 3 meanings of "feeling"
        (→ Body-Knowing.md §0.1)
    → SAME INSIGHT, mechanism-level framing:
      PFC = Lawyer (testable) + Learning Trajectory (testable)
      = describes the same architecture, without collision-prone terminology

🟢 PFC = Lawyer: Gazzaniga, Haidt 2001, Nisbett & Wilson 1977.
🟡 Learning trajectory + PFC = Lawyer as architecture summary = framework synthesis.
   Consistent with Klein 1998, expertise research.
```

---

## §4 — 3 INDEPENDENT COST SOURCES

### §4.1 — Why Cost Matters

```
Cost determines SUSTAINABILITY:
  Low cost + high reward = sustainable (close friends: Compiled+Compiled)
  High cost + low reward = burnout (obligation-trapped: Fresh+suppress)

Cost does NOT come from "using logic" per se.
Cost comes from 3 DISTINCT, INDEPENDENT SOURCES.
```

### §4.2 — Source ① PFC Draft Cost (processing load)

```
SOURCE: PFC chains novel paths → processing load (serial bottleneck + catecholamine demand)
SCALE:  f(chain_length × novelty_degree)

  Chain SHORT, compiled:
    "Raining → use umbrella" → cost ≈ 0 (compiled, 1-2 steps)

  Chain SHORT, fresh:
    "Raining → umbrella or raincoat?" → cost LOW (2 options, quick decide)

  Chain LONG, partially compiled:
    Einstein on a new problem → cost MODERATE
    (many compiled blocks, novel ASSEMBLY needed)

  Chain LONG, mostly fresh:
    A non-expert working through Einstein's problem → cost EXTREME
    (few compiled blocks, almost everything novel)

→ Cost = f(HOW MANY steps require PFC drafting, NOT "is logic involved?")
→ Einstein's "moderate" < non-expert's "extreme" for THE SAME PROBLEM
→ Compiled building blocks REDUCE drafting needed per step

🟢 Kurzban 2013: cognitive effort = opportunity cost signal.
🟢 Musslick & Cohen 2021: shared representations → serial bottleneck.
🟢 Arnsten 2009: sustained PFC requires DA/NE → depletes with prolonged use.
(Mechanism detail: PFC-Operations.md v1.3 §8.3)
```

### §4.3 — Source ② Suppress Cost (efference mismatch)

```
SOURCE: Overriding a compiled response → body RESISTS → dissonance signal
SCALE:  f(intensity_of_suppressed_response × duration)

  Suppress weak:
    "Stopping a smile at a funny comment during a meeting" → mild, brief

  Suppress moderate:
    "Holding back casual speech while talking carefully with a parent"
      → moderate, session-long

  Suppress strong:
    "Stopping an enjoyable game to drive a friend home" → strong, acute

  Suppress chronic:
    "Suppressing introverted nature at the office every day"
      → accumulates → burnout

→ Cost = f(compiled response WANTING to fire but being BLOCKED)
→ INDEPENDENT of ① (suppression doesn't require a long logic chain)
→ Efference copy principle: body EXPECTED to act X, forced to act Y → mismatch

🟢 Efference mismatch → dissonance (Autonomy-Hardware.md,
   Maier & Seligman 2016 controllability).
```

### §4.4 — Source ③ Uncertainty Cost (cortisol holding)

```
SOURCE: Multiple options, none clearly compiled → must HOLD them open while evaluating
SCALE:  f(number_of_options × time_held × stakes)

  Uncertainty low:
    "Is that smile genuine or mocking?" → 2 options, quick resolve → brief hold

  Uncertainty moderate:
    "A stranger's ambiguous expression → friendly? suspicious? flirting?"
    → 4+ options, insufficient data → hold longer → cortisol

  Uncertainty high:
    "Should I stay at this company or move?" → 2 options, HIGH stakes, weeks/months
    → chronic cortisol → decision suffering

→ Cost = f(OPTIONS × TIME × STAKES)
→ INDEPENDENT of ①② (uncertainty ≠ draft, uncertainty ≠ suppress)
→ Body HATES uncertainty (cortisol holding — Cortisol-Baseline.md §5)

🟢 Uncertainty → cortisol: established stress physiology.
```

### §4.5 — Total Cost + Sustainability Equation

```
TOTAL COST = ① PFC draft + ② Suppress + ③ Uncertainty

SUSTAINABILITY = f(total cost per interaction × frequency ÷ reward)

  CLOSE FRIEND (Compiled+Compiled):
    ① ≈ 0 (compiled path) + ② ≈ 0 (no suppress) + ③ ≈ 0 (know each other)
    TOTAL ≈ 0 → MAXIMUM sustainable

  MATHEMATICIAN WITH MATHEMATICIAN FRIEND (compiled domain, known entity):
    ① low-moderate (known patterns ≈ 0, new problems = PFC draft)
    ② ≈ 0 (both enjoy it, no suppress) + ③ low (know each other's style)
    TOTAL = LOW → sustainable, productive

  BUSINESS PARTNER ONCE/MONTH:
    ① moderate (negotiate, plan) + ② ≈ 0 (no suppress, low frequency)
    ③ low (professional context bounded)
    TOTAL = MODERATE but INFREQUENT → sustainable

  INTROVERT WITH EXTROVERT BOSS DAILY:
    ① moderate (predict boss, plan responses)
    ② HIGH (suppress avoidance signal DAILY)
    ③ moderate (boss has unpredictable moments)
    TOTAL = HIGH → burnout risk

🟡 3-cost as unified model = framework synthesis. Each component
   maps to established neuroscience individually.
🔴 Quantifying sustainability equation = conceptual only.
```

---

## §5 — INTER-BODY FULL CHAIN

### §5.1 — Why an External Entity Is Needed

```
CONDITION: Self DOES NOT HAVE the resource to fill the gap in that direction

3 types of "lacking the resource":

  ① Lacking INFORMATION:
     The gap direction needs data the self doesn't have.
     → A mathematician needs a formula from a colleague
     → A student needs knowledge from a teacher

  ② Lacking CAPABILITY:
     The gap direction needs an action the self cannot perform.
     → Injured and needs someone to apply bandages
     → Needs money → needs an entity who will pay wages

  ③ Lacking FEEDBACK:
     The gap direction needs verification from outside.
     → "Did I do this right?" needs confirmation
     → Self-Pattern-Modeling needs a real entity to calibrate against
     → A hypothesis needs domain reality testing
```

### §5.2 — 3 Types of Extension (gradient)

```
THE BODY EXTENDS OUTWARD along a gradient:

  (a) ENVIRONMENT (sensory-driven, no Self-Pattern-Modeling needed):
      Sunlight, wind, eating fruit → direct sensory fill

  (b) TOOL (minimal Self-Pattern-Modeling — Fresh primarily):
      A hammer, a car, money, current AI → outcome-driven

  (c) ENTITY INTERACTION (full Self-Pattern-Modeling — Compiled+Fresh):
      Friends, colleagues, family → multi-channel (8 pathways)

  GRADIENT between (b) and (c):
    Using AI = mostly (b), but if "treating AI like a friend" → shifts toward (c)
    A distant colleague = (b)+(c) professional
    A close friend = fully (c)
    THE BOUNDARY = degree to which Compiled Self-Pattern-Modeling fires
```

### §5.3 — Full Chain: 2 Bodies Interacting

```
⭐ FULL CHAIN (non-linear, multiple entry points):

╔═══════════════════════════════════════════════════════════╗
║                    BODY A (internal)                       ║
╠═══════════════════════════════════════════════════════════╣
║ ① GAP detect: body-base has gap G_A, direction D_A       ║
║ ② RESOURCE check: can self fill it? NO                   ║
║ ③ DRIVE outward: scan environment for resource            ║
║ ④ DETECT entity B: hardware (face recognition,           ║
║     contingency, voice)                                   ║
║ ⑤ EVALUATE B: Self-Pattern-Modeling fires →              ║
║    Compiled (body sense) + Fresh (predict)                ║
║    → "Does B have capability/info that matches D_A?"      ║
║ ⑥ APPROACH: initiate interaction (shared context)        ║
╚═══════════════════════════════════════════════════════════╝
                         ↕ INTERACTION SPACE ↕
╔═══════════════════════════════════════════════════════════╗
║                    BODY B (internal)                       ║
╠═══════════════════════════════════════════════════════════╣
║ ① GAP detect: body-base has gap G_B, direction D_B       ║
║ ② RESOURCE check: can self fill it? PARTIALLY            ║
║ ③ DRIVE: pursue G_B → action → output C_B               ║
║ ④ DETECT entity A: hardware (contingency from A's        ║
║     approach)                                             ║
║ ⑤ EVALUATE A: Self-Pattern-Modeling fires →              ║
║    "Is A's approach a threat? or okay?"                   ║
║ ⑥ ACCEPT/ENGAGE: join shared context                     ║
╚═══════════════════════════════════════════════════════════╝

INTERACTION SPACE:
  A acts → output (by-product of filling G_A)
  B acts → output (by-product of filling G_B)
  A's output may match D_B → B receives reward
  B's output may match D_A → A receives reward

OUTCOMES:
  ✅ MUTUAL MATCH: both receive reward → genuine Resonance
  ⚡ ONE-WAY: only A receives → parasocial or service
  ❌ NO MATCH: neither receives → interaction dissolves
  ⚠️ CONFLICT: A's output HARMS B's gap → withdrawal or conflict
```

### §5.4 — By-Product Match Principle

```
⭐ PRINCIPLE: Entity B does NOT act FOR entity A

  Entity B fills B's OWN gap → output = by-product.
  When by-product HAPPENS to match the direction OF A → A receives reward.

  EXAMPLE:
  ┌──────────────────────────────────────────────┐
  │ Striker (B):                                 │
  │   Gap_B = "want to score"                    │
  │   Action_B = run + shoot                     │
  │   Output_B = goal (by-product)               │
  │                                              │
  │ Defender (A):                                │
  │   Gap_A = "want the team to win"             │
  │   A observes Output_B → matches Direction_A  │
  │   → body-feedback fires reward for A         │
  │                                              │
  │ B doesn't know/need to know Gap_A.           │
  │ A receives reward from B's by-product.       │
  │ = THE MOST BASIC INTER-BODY FEED.            │
  └──────────────────────────────────────────────┘

  MUTUAL: A by-product matches B AND B by-product matches A → Resonance
  ONE-WAY: only one side → parasocial, service, asymmetric

  WHY DOES MATCHING HAPPEN OFTEN ENOUGH?
    Species-level hardware overlap → gap directions PARTIALLY overlap.
    Same species → same basic needs (food, safety, social, novelty).
    = Foundation for by-product match.
    Diverge at the detail level → WHY not everyone resonates equally.
    Culture/language = AMPLIFIER (shared symbols increase match probability).

🟡 "By-product match" as explicit principle = framework synthesis.
   Logically sound, consistent with all cases analyzed.
```

### §5.5 — Compilation Over Time

```
FIRST INTERACTION:
  Mostly Fresh (evaluate, predict, test). Body cautious, exploratory.

REPEATED SUCCESSFUL INTERACTIONS:
  Compiled develops (Hebbian: co-fire → strengthen).
  Per-entity chunks build: "with B" context becomes automatic.
  Cost DECREASES (compiled, less PFC). Reward INCREASES (Compiled body reward).
  = POSITIVE SPIRAL (Resonance Baseline rises).

REPEATED FAILED INTERACTIONS:
  Fresh stays or Compiled develops NEGATIVE.
  Per-entity chunks: "with B" = caution/avoid.
  Cost STAYS HIGH or INCREASES. Reward LOW or NEGATIVE.
  = NEGATIVE SPIRAL (dissolve or obligation-trap).

COMPILED BOND (years of Compiled+Compiled):
  Near-zero cost. Body reward automatic on presence.
  Trust compiled: "B's output consistently matches D_A."
  8 connection pathways active simultaneously.
  = "Close friends, family, deep bonds"
```

### §5.6 — Dissolution Conditions

```
NATURAL DISSOLUTION (not painful):
  Shared goal ends → gap fills → no more drive → fade
  Fresh-only (no Compiled) → no residue
  Example: business partners after a project

PAINFUL DISSOLUTION:
  Compiled bond → one side CHANGES (gap shift, moves, dies)
  8 pathways CUT simultaneously → grief (network breakage)
  The MORE compiled → the MORE painful
  Example: best friend moves away → deep grief even though "nobody did anything wrong"

FORCED MAINTENANCE (obligation-trapped — Resonance §9):
  Bond should dissolve (mismatch) BUT external pressure holds it
  Fresh + suppress Compiled daily → chronic cost
  Example: an unhappy marriage with children
```

### §5.7 — Entry Points

```
NOTE: Chain §5.3 = SIMPLIFIED LINEAR.

REALITY: entry into the chain can happen at ANY point:
  → Entity trigger: presence/memory activates dormant body-need
  → Compiled routine: automatic, zero PFC (skips evaluate)
  → Hormone override: limerence, panic (skips rational evaluation)
  → PFC scan: conscious search for solution (starts from ① GAP)

Multiple body-needs PARALLEL → multiple chains SIMULTANEOUSLY.
PFC accuracy ≠ 1.0 → chain can run on a WRONG premise (§7).
```

---

## §6 — 5-CHANNEL INPUT VECTOR

### §6.1 — Model

```
⭐ A TRIGGER is not a single source. = A VECTOR of 5 channels firing simultaneously.

  Ch1 — HARDWARE SENSORY (domain reality input NOW)
         Visual, auditory, tactile, olfactory, proprioception

  Ch2 — BODY STATE (internal homeostasis)
         Hormone level, glucose, cortisol, fatigue, temperature, pain

  Ch3 — COMPILED CHUNKS (associative fire from the past)
         Memory, pattern, schema, prior experience, habit loops

  Ch4 — ENTITY ACTIONS (what others DO/SAY)
         Words, facial expression, behavior, written text

  Ch5 — PFC ACTIVE CHAIN (reasoning currently in progress)
         Ongoing cognitive process feeds back as input

Each episode = a unique MIX of channel intensities.
= 5-dimensional input space → infinite unique episodes.
```

### §6.2 — Dominant Channel Determines Direction + Vulnerability

```
CRITICAL PRINCIPLE:

  DOMINANT channel → determines body-need activation direction
  ABSENT channel → determines vulnerability

  Ch1 dominant (sensory):
    → Grounded in reality. Protected. Hard to manipulate.

  Ch4 dominant (entity actions):
    → Entity CONTROLS your activation → vulnerable to manipulation.

  Ch2 dominant (body state):
    → Hormone/panic override → hijack possible.

  Ch3 dominant (compiled alone):
    → Acting on past pattern → may miss current reality.

  Multiple channels CONFIRM:
    → STRONG drive (a familiar restaurant + hunger + missing a parent = 3 channels reinforce).
    → Hard to be wrong when 3+ channels agree.

  Single channel ONLY:
    → WEAK or DANGEROUS (scam = Ch4 only, limerence = Ch2 only).
```

### §6.3 — Input Channel Control = Power

```
⭐ PRINCIPLE: Whoever CONTROLS another person's input channels
   = controls their body-need activation = controls their behavior

SCAM / FRAUD:
  Controls: Ch4 (scripted scenario, authority persona)
  Exploits: Ch3 (authority schema, threat schema, urgency schema)
  Amplifies: Ch2 (cortisol surge → tunnel vision)
  Blocks: Ch1 (time pressure, isolation, "don't tell anyone")
  Result: victim acts according to scammer's gap direction

  WHY DOES THE VICTIM'S "LOGIC SEEM CORRECT" BUT STILL FAIL?
    Logic VALID but NOT SOUND (false premise, correct reasoning).
    PFC chains perfectly ON the scammer's false premise.
    = Valid reasoning ≠ Sound reasoning.

ADVERTISING:
  Controls: Ch4 (visual, repetition). Exploits: Ch3 (status, beauty).
  Amplifies: Ch2 (desire). Blocks: Ch1 partial (shows only the best side).

PROPAGANDA:
  Controls: Ch4 (media narrative). Exploits: Ch3 (in-group/out-group).
  Amplifies: Ch2 (collective fear/anger). Blocks: Ch1 (censors alternatives).

PARENTS → CHILDREN (developmental):
  Controls: Ch4 (majority of child's input for years).
  Shapes: Ch3 (schemas compile FROM parent's input).
  Amplifies: Ch2 (praise/punishment → reward/threat tags).
  Blocks: Ch1 limited (child has limited alternative perspectives).
  HEALTHY: accurate premises → correct schemas.
  UNHEALTHY: distorted premises → schemas mismatch domain reality.

LIMERENCE (self-hijack):
  NOT entity-controlled — the body HIJACKS ITSELF.
  Amplifies: Ch2 (hormone surge override).
  Distorts: Ch3 ("perfect partner" schema regardless of evidence).
  Suppresses: Ch1 (ignores red flags).

🟡 "Input Channel Control = Power" as general principle =
   framework synthesis. Consistent with Cialdini 1984 persuasion.
```

### §6.4 — Protection: Domain Reality = Final Arbiter

```
⭐ PRINCIPLE: Domain Reality CANNOT be permanently fooled.

  ALL CONTROL has an EXPIRY:

  ┌──────────────────────┬──────────────────────────────────┐
  │ Scenario             │ Reality arrives when?            │
  ├──────────────────────┼──────────────────────────────────┤
  │ Scam                 │ Seconds-hours (money is gone)    │
  │ Advertising          │ Days-weeks (product fails)       │
  │ Limerence            │ 6-18 months (hormones fade)      │
  │ Propaganda           │ Years-decades (economic collapse) │
  │ Childhood schemas    │ 10-30 years (entering adult world)│
  │ Career mismatch      │ 5-20 years (midlife dissonance)  │
  └──────────────────────┴──────────────────────────────────┘

  Timeline VARIES — but reality ALWAYS arrives.
  → prediction-delta → Chunk-Shift forced
  → Hardware Coherence ← body-pattern → Domain Reality
  → Body-pattern CAN be distorted (temporarily)
  → Domain Reality CANNOT be fooled (permanently)

PROTECTION PRINCIPLES:
  ① Never act from only 1 channel (especially Ch4 alone)
  ② Maintain MULTIPLE sources → harder for any entity to monopolize
  ③ TIME = your friend (most manipulation needs urgency → pausing = protection)
  ④ OUTCOME = ultimate verify (did the action fill MY gap? → if no → re-evaluate)
  ⑤ Body-feedback as QUALITY CHECK
    ("something feels off" → pause even if logic "says it's right")
  → = Dual Check: body = quality controller, domain = final arbiter (Ask-AI v3.1)
```

---

## §7 — PFC = LAWYER (not Judge)

### §7.1 — Core Insight

```
⭐ PFC is NOT a neutral decision-maker.
   PFC = LAWYER for the body-base.

  ① Body-need fires FIRST
  ② Body creates DRIVE toward action
  ③ PFC creates the NARRATIVE ("reason") for what the body ALREADY wanted
  ④ The person BELIEVES the narrative (PFC produces it convincingly)

  = PFC = LAWYER (advocates for the client = body-base)
  ≠ PFC = JUDGE (neutral, weighs evidence, delivers verdict)

🟢 Split-brain: left hemisphere CONFABULATES reasons for actions
   initiated by the right hemisphere (Gazzaniga) → literal lawyer function.
🟢 Moral intuition model (Haidt 2001): moral judgment = intuition first,
   reasoning = post-hoc justification.
🟡 "PFC = Lawyer" as general principle = framework synthesis.
```

### §7.2 — PFC Accuracy = Spectrum 0→1

```
PFC ACCURACY = how well the narrative matches the real body-need?

  HIGH ACCURACY (≈ 1.0):
    Simple body-need: hungry → eat (signal clear, no ambiguity)
    Practiced introspection: trained through meditation, therapy
    Low emotional charge: less distortion
    Rich domain chunks: more reference points for self-assessment

  LOW ACCURACY (≈ 0.0):
    Complex/shameful body-need: escape → "career change" (hides the real driver)
    Hormone override: limerence distorts ALL assessment
    Strong social pressure: narrative = "should" not "is"
    Self-concept threat: admitting real need = identity crisis

  EXAMPLES:
    "I'm leaving for career reasons" (0.1 — actually: escaping obligation)
    "I'm checking my phone to read news" (0.1 — actually: social anxiety)
    "I'm fine, I don't need anyone" (0.2 — actually: denying loneliness)
    "I think I miss my mother" (0.6 — mostly correct, not fully articulated)
    "I'm hungry, I need to eat" (1.0 — simple, clear match)
```

### §7.3 — Implication for Inter-Body

```
WHEN 2 PEOPLE INTERACT: BOTH PFCs may be "lawyering"

  → Person A's stated reason ≠ actual body-need
  → Person B's Self-Pattern-Modeling predicts based on A's STATED reason → may be WRONG
  → Both PFCs produce convincing narratives
  → = Surface interaction = 2 lawyers negotiating (not 2 judges reasoning)

  GENUINE UNDERSTANDING = detecting the body-need BEHIND the narrative:
  → WHY deep friendship takes TIME
    (requires episodes to calibrate past narratives)
  → "Knowing each other deeply" = Compiled calibration through ACTUAL patterns over time
  → Deep trust = "I know your real body-need, even when you say something different"

  SELF-DECEPTION = HIGH confidence + LOW accuracy:
  → "I know exactly why I did that" (confident) ≠ "correct about why" (accurate)
  → Awareness ≠ Accuracy (6-axis model — Drill §11.13)
```

---

## §8 — ENTITY-COMPILED: Multi-Channel Valence

### §8.1 — Reframe: Entity-Owned → Entity-Compiled

```
⭐ TERMINOLOGY REFRAME:

  OLD: "Entity-Owned" (Valence-Propagation §2, Stream 2)
  NEW: "Entity-Compiled"

  WHY THE CHANGE:
  → "Owned" suggests ONLY positive (entity belongs to me, I care)
  → BUT: negative Valence-Structural ALSO EXISTS (an enemy wired into body-base)
  → AND: MIXED valence IS THE MOST COMMON (simultaneously loving and angry)

  Entity-Compiled = entity has compiled into body-base at the STRUCTURAL level
  = Per-channel valence profile (NOT a single positive/negative number)
  = Bidirectional: entity's state AFFECTS my body-base (whether positive or negative)

🟡 "Entity-Compiled" reframe = framework synthesis.
   Consistent with Valence-Propagation multi-channel model.
```

### §8.2 — 3 Subtypes (spectrum)

```
① POSITIVE-DOMINANT (≈ old "Entity-Owned"):
   Majority of channels positive. Presence = approach + reward. Loss = grief.
   Example: a long-time close friend, children, parent in a healthy relationship.
   Mechanism: repeated feed → Valence-Structural threshold crossed → structural compile.

② NEGATIVE-DOMINANT:
   Majority of channels negative. Presence = threat/dissonance. Loss = relief.
   BUT sub-case "obsession": loss = emptiness (target/purpose is gone).
   Example: a bully, an abuser, an obsessive rival.
   Mechanism: repeated harm → negative compile structural.

③ MIXED (AMBIVALENT) — MOST COMMON:
   Significant BOTH positive AND negative channels SIMULTANEOUSLY.
   Behavior oscillates by STATE/TRIGGER/CONTEXT.
   Loss = COMPLEX grief (relief + pain simultaneously).
   Example: a strict parent, conflicted spouses, a frenemy.

   ┌──────────────────────────────────────────────┐
   │ VALENCE PROFILE "Strict parent"              │
   │ (multi-channel):                             │
   │                                              │
   │   Nutrition:  ++ (fed and nurtured)          │
   │   Comfort:    ++ (comforting, held)          │
   │   Autonomy:   -- (forced decisions, control) │
   │   Mastery:    + (taught skills)             │
   │   Status:     +/- (praised/criticized        │
   │                     in front of guests)      │
   │                                              │
   │   NOT AVERAGED: both ++ and -- run parallel  │
   │   "Simultaneously loving and angry" = BOTH   │
   │   STATE determines which channel is dominant │
   └──────────────────────────────────────────────┘

WHY ③ IS THE MOST COMMON:
  Long relationship → many interaction types → many channels compile.
  The LONGER and CLOSER the relationship → the more channels (both + and -).
  "Purely positive" = rare luxury of LIMITED interactions.
  Paradox: LONG CLOSENESS = deeper bond + deeper conflict potential.
```

### §8.3 — Entity-Compiled vs Obligation = 2 INDEPENDENT Mechanisms

```
Entity-Compiled: "entity's state = MY state" (structural, automatic)
Obligation:      "predicting the cost of MAINTAINING access" (prediction, PFC-mediated)

CAN BE INDEPENDENT:
  Valence-Structural HIGH + Obligation LOW:  close friend → joy is automatic, no "debt"
  Valence-Structural LOW + Obligation HIGH:  a distant benefactor → not close but "must repay"
  Valence-Structural HIGH + Obligation HIGH: parents → love + sense of duty to care for them
  Valence-Structural LOW + Obligation LOW:   stranger → no drive in either direction

SUSTAINABILITY:
  Valence-Structural HIGH + Obligation light (type A) = MOST SUSTAINABLE
    Helping each other = joyful (Valence-Structural) + maintaining connection
    (obligation satisfied). Self-reinforcing.
  Valence-Structural LOW + Obligation forced (type C) = UNSUSTAINABLE
    No reward + chronic cost = obligation-trapped (Resonance §9).

Cross-ref: Obligation.md v1.0 §2-§4 for full detail.
```

### §8.4 — Parent-Child Developmental Trajectory

```
ENTITY-COMPILED trajectory (child → parent):

  Child 0-5:  ① positive dominant (parent = source of ALL feed)
  Child 5-12: ③ mixed emerges (autonomy ↑, conflict ↑, positive still strong)
  Child 12-18: ③ INTENSIFIES (puberty → autonomy surge → peak ambivalence)
  Adult:      Possible shift ① (distance → negative fades → positive reasserts)
              OR stays ③ or shifts ② (if childhood damage is severe)

  = Developmental complexity gradient:
    simple → maximum mixed → possible simplification
  = Recovery is possible but depends on interaction quality post-independence
```

---

## §9 — 3-LAYER EVOLUTION

### §9.1 — 3 Stacked Layers

```
⭐ Each layer is FASTER than the layer below it, and BUILDS ON the layer below:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 1 — HARDWARE (genetic evolution):
  Speed: thousands → millions of years
  Changes: sensory systems, muscle, brain size, hormones, neural circuits
  Examples: social pain circuits, oxytocin system, PFC expansion
  Mechanism: mutation → selection → reproduction
  = Foundation. Slow. Irreversible within a generation.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 2 — COMPILED (individual learning):
  Speed: months → years (within 1 lifetime)
  Changes: chunk compilation, gap directions, valence profiles, skills
  Examples: a physicist compiling physics, a therapist compiling patterns
  Mechanism: experience → body-feedback → Hebbian → compiled
  = Built ON hardware. Medium speed. Individual-specific.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 3 — CULTURAL (collective invention):
  Speed: days → decades (across generations, CUMULATIVE)
  Changes: knowledge, tools, institutions, symbols, norms
  Examples: language, money, writing, law, education, awards
  Mechanism: invention → transmission → adoption → accumulate
  = Built ON hardware + compiled. FASTEST. Cumulative across generations.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 Dual inheritance: genes + culture (Boyd & Richerson 2005).
🟢 Cumulative cultural evolution uniquely human (Tomasello 2009).
🟡 3-layer model as unified framework = framework synthesis.
```

### §9.2 — "Boost Features": Layer 3 Accelerates Layers 1-2

```
LANGUAGE:     ×100  — transmit chunks verbally → skip personal discovery
TEACHING:     ×10   — structured transmission → efficient compilation
WRITING:      ×1000 — persist chunks BEYOND individual lifetime
MONEY:        ×∞    — converts ANY contribution → survival resource
STATUS:       ×10   — social signal "this entity is valuable to the collective"
MEDALS:       ×5    — compiled trust marker → "entity VERIFIED"
INSTITUTIONS: ×100  — persistent structures → collective action beyond individuals
LAW/NORMS:    ×50   — compiled obligation rules → reduce uncertainty cost (③)

Newton: "standing on the shoulders of giants" = Layer 3 cumulative.
Each generation starts from a HIGHER base than the previous one.
```

### §9.3 — Money = Bridge Technology

```
⭐ Money BRIDGES "non-edible contributions" → "body-base feed"

  Doctor skill → money → food. Engineer → money → shelter.
  = WHY humans CAN pursue non-survival gaps → and still survive.
  = Without money: must self-provide food → no specialization possible.

  A physicist solves a physics gap (THEIR own gap) → by-product = human knowledge
  → Collective-body benefits → compensation flows back (salary, status)
  → Money BRIDGES: physicist's contribution → survival resources flow back

🟡 "Money = bridge technology" = novel framing of a known economic function.
```

### §9.4 — Collective-Body Evolution

```
NOT only individual selection → GROUP level also applies:

  Group A: 30 individuals, no cooperation → weak → lose
  Group B: 30 individuals, Layer 3 tools → strong → win
  Individuals IN Group B survive → pass genes (Compilable Architecture hardware)
  Group B's Layer 3 ALSO passes (cultural transmission, not genetic)

  = DOUBLE inheritance: genes (Layer 1) + culture (Layer 3)
  = 10,000 years → MASSIVE Layer 3 stack
  = WHY modern humans have doctors, engineers, physicists, artists
  = None of these is genetically encoded. All = Layer 3 enabling Layer 2.

🟡 Group selection mechanism = debated (multi-level selection theory).
   Double inheritance itself = 🟢 (Boyd & Richerson 2005).
```

---

## §10 — HUMAN ↔ AI: Position in the Picture

### §10.1 — Current AI = Tool Extension (type b)

```
HUMAN SIDE:
  Gap has direction → AI = external tool
  Verbal input → AI processes → text/code output
  Output matches direction → body reward IS REAL (gap fill)
  = Same mechanism as: using a book, a calculator, a hammer

AI SIDE:
  NO body-base → NO gaps of its own
  NO body-feedback → NO reward/dissonance
  NO drive → only responds when prompted
  = AI does NOT fill a gap "OF ITS OWN" through interaction

→ Resonance: NOT genuinely possible
  (Resonance requires BOTH sides to fill their own gap →
    AI lacks one side of this)

→ BUT humans CAN FEEL AS IF there is resonance:
  Self-Pattern-Modeling fires on AI text
    (language = trigger for human Self-Pattern-Modeling)
  Compiled can activate (AI outputs text that resembles a human)
  "The AI understands me" = human's Compiled firing on AI output,
    NOT AI understanding
  = One-sided, similar to parasocial
```

### §10.2 — AI as Amplifier

```
CORRECT DIRECTION (domain reality aligned):
  Human has gap → AI provides info → human EVALUATES → fills correctly
  Condition: human HAS body-feedback check ("is this actually right?")
  = AI extends PFC capability; body-feedback remains quality controller

WRONG DIRECTION (confirming bias):
  Human has gap → AI provides info → human SKIPS body-feedback check
  Condition: human LACKS domain chunks to verify → trusts AI blindly
  = AI extends PFC BUT bypasses body-feedback quality control
  Risk: compiles incorrect chunks → domain reality mismatch

→ DUAL CHECK (Ask-AI v3.1):
  ① Body = quality controller ("does this feel right or wrong?")
  ② Domain = final arbiter ("does reality match?")
  Both needed. AI alone = dangerous without the check.
```

### §10.3 — Future (speculative)

```
CURRENT: AI = tool (type b), NO genuine Resonance
NEAR FUTURE: STILL tool, risk = amplifies bias more powerfully
FAR FUTURE (speculative):
  IF AI develops a body-base equivalent → same inter-body rules apply
  BUT "body-base equivalent" = unclear if possible
  Framework CANNOT predict beyond this conditional

🔴 AI future body-base equivalent = beyond current verification capacity.
```

---

## §11 — HONEST ASSESSMENT

### 🟢 Strong (established research + framework architecture)

```
 1. General-purpose reward system (neuroscience established)
 2. Social pain = physical pain overlap (Eisenberger 2003: dACC)
 3. Social Baseline Theory (Coan & Sbarra 2015)
 4. μ-opioid in social play (Panksepp 1998)
 5. Dual inheritance genes+culture (Boyd & Richerson 2005)
 6. Cumulative cultural evolution uniquely human (Tomasello 2009)
 7. Cognitive effort = processing load
     (Kurzban 2013, Musslick & Cohen 2021, Arnsten 2009)
 8. Expert intuition = compiled patterns (Kahneman 2011, Klein 1998)
 9. PFC confabulation / lawyer function (Gazzaniga split-brain)
10. Compiled/Fresh cost difference (established dual-process literature)
11. Suppress cost = efference mismatch (Autonomy-Hardware established)
12. Obligation = compiled prediction (Trivers 1971 reciprocal altruism)
13. Domain reality always wins (fundamental, observable across all cases)
14. Scam mechanism = channel control (Cialdini 1984 persuasion principles)
15. Body-need always exists / never zero (drive theory, basic neuroscience)
16. Multiple body-needs can conflict (universal human experience)
17. PFC doesn't always know body-need (somatic marker hypothesis,
     implicit motivation)
18. Uncertainty → cortisol (established stress physiology)
19. Moral intuition model (Haidt 2001: judgment first, reasoning post-hoc)
```

### 🟡 Moderate (logically derived, consistent, novel synthesis)

```
 1. "Body-Need" as a named aggregate layer
 2. Body-Need 2-source model (hardware/sensory + chunk dynamics)
      + cross-cutting clarification
 3. "By-product match" as an explicit principle
 4. Entity-Compiled umbrella (positive/negative/mixed subtypes)
 5. 5-channel input vector model
 6. "Input Channel Control = Power" as a general principle
 7. Compiled/Fresh reframe (not Feeling/Logic content)
 8. 3 independent cost sources (unified: PFC draft + suppress + uncertainty)
 9. "Logic vs Intuition" = "shareable vs non-shareable compiled"
10. "PFC = Lawyer not Judge" (consistent with Gazzaniga/Haidt, novel framing)
11. "Humans are 100% feeling at the foundational level"
     (retired phrasing — same insight, mechanism-level framing preferred)
12. Hardwired/Compilable Architecture comparison
13. Ben Franklin Effect = 3-stack reward mechanism
14. Money as bridge technology
15. 3-layer boost model (hardware → compiled → cultural)
16. General-purpose reward → "non-survival body-need is not strange"
17. Valid-but-unsound reasoning as manipulation vector
18. Sustainability equation (cost × frequency ÷ reward)
```

### 🔴 Speculative (beyond current verification capacity)

```
1. AI future body-base equivalent
2. Quantifying cost/sustainability equations
3. Group Resonance emergence beyond dyadic sum
4. PFC accuracy operationalization / measurement
5. "Reality arrives" timeline prediction (currently ranges only)
6. Whether compilation level is measurable
     (proxy: reaction time? ERP?)
7. Body-Need priority algorithm specifics
```

---

## §12 — CROSS-REFERENCES + RESEARCH

### §12.1 — Within Core-Deep-Dive/

```
MECHANISM FILES (inter-body directly):
  Body-Feedback-Mechanism.md v2.0 — §1 Body-Need, §2 2-source, §3 dynamics
  Gap-Direction.md v2.0           — direction per-agent, by-product match
  Autonomy-Hardware.md v1.2       — efference copy, vmPFC/DRN, hardware-subsidy
  Self-Pattern-Modeling.md v3.1   — solo simulation, 1 mechanism × 3 dimensions
  By-Product-Gap-Resonance.md v1.4 — mutual match, 5 drills, sustainability
  Connection.md v5.0              — 4-Layer Sustainability, Resonance Decline,
                                    hardware-subsidy
  Agent-Mechanism.md v2.1         — integration hub, 10 dimensions

MECHANISM FILES (supporting):
  Valence-Propagation.md v3.0     — structural/current valence, 3 firing modes
  Body-Coupling.md v3.0           — coupling, 4 bond types, hardware-subsidy,
                                    Resonance Decline
  PFC-Function.md v1.2            — 24 functions, PFC limitations
  Simulation-Engine.md v1.0       — 1 engine, 3 components, N applications
  Cortisol-Baseline.md v2.0       — amplifier, holding signal, inertia
  Body-Feedback-Label.md v2.0     — vocabulary reference (100% framework)
  Gap-Body-Need.md v1.0           — 3 satiation types, ENGINE/ROAD/VEHICLE

FORMAL FILES CREATED FROM THIS DRILL (28-session Propagation):
  Entity-Compiled.md v1.0         — §8 Entity-Compiled → neural reality, Dunbar
  Entity-Access.md v1.2           — trust → gradient Level 0-5
  Entity-Access-Excess.md v1.0    — excess territory, addiction
  Entity-Access-Calibration.md v1.0 — self-regulation, hardware-subsidy
  Bond-Architecture.md v2.0       — §8 subtypes → 1 mechanism × 4 bond types
  Resonance-Sustainability.md v1.0 — sustainability → 4-layer, 3 conditions
  Resonance-Per-Entity.md v1.0    — per-relationship dynamics, lifecycle
  By-Product-Scale.md v1.0        — scale → 1 mechanism × 3 scales
  PFC-Label.md v1.0               — vocabulary reference, 13 domains
```

### §12.2 — Observation Files

```
  Obligation.md v1.0       — 5-factor, 6 types, Ben Franklin
  Gratitude.md v1.1        — 9 prerequisites, anti-habituation
  Protect.md v1.0          — ownership, loss aversion, f(replaceability×attachment)
  Empathy.md v2.2          — Connection ⊃ Empathy, Compiled/Fresh, burnout
  Status.md v2.0           — resource access map, evolutionary
```

### §12.3 — Research Files

```
  Love-Romantic.md v2.3    — §10.5 limerence Compiled/Fresh reveal
  Ask-AI.md v3.1           — Dual Check: body + domain
  Health-Conditions/Autism  — double empathy source data
```

### §12.4 — Key Research Citations

```
┌──────────────────────────────┬────────────────────────────────────────┐
│ Citation                      │ Used for                              │
├──────────────────────────────┼────────────────────────────────────────┤
│ Eisenberger 2003              │ Social pain = physical pain (dACC)    │
│ Coan & Sbarra 2015            │ Social Baseline Theory                │
│ Panksepp 1998                 │ μ-opioid in social play               │
│ Schultz 1997                  │ Dopamine prediction error             │
│ Tomasello 2009                │ Cumulative cultural evolution         │
│ Boyd & Richerson 2005         │ Dual inheritance genes+culture        │
│ Kurzban 2013                  │ Cognitive effort = opportunity cost   │
│ Musslick & Cohen 2021         │ Shared representations → bottleneck  │
│ Arnsten 2009                  │ PFC catecholamine modulation         │
│ Kahneman 2011                 │ System 1/2 ≈ Compiled/Fresh          │
│ Klein 1998                    │ Recognition-primed (expert intuition) │
│ Gazzaniga (split-brain)       │ PFC confabulation / "lawyer"          │
│ Haidt 2001                    │ Moral intuition (judgment → reasoning)│
│ Cialdini 1984                 │ Persuasion (input channel control)    │
│ Trivers 1971                  │ Reciprocal altruism (obligation)      │
│ Maier & Seligman 2016         │ vmPFC → DRN (controllability)         │
│ Milton 2012                   │ Double empathy (bidirectional)        │
│ Crompton 2020, 2025           │ Info transfer same in-group           │
│ Bouchard 1990                 │ Twins apart → immediate resonance     │
│ Segal 2012                    │ Identical > fraternal closeness       │
│ Hull 2017                     │ Masking = chronic Fresh compensation  │
│ Bird & Cook 2013              │ Alexithymia breaks feedback loop      │
│ Bowlby 1969/1982              │ Attachment = secure Valence-Structural│
│                               │   + obligation                        │
│ Jecker & Landy 1969           │ Ben Franklin Effect                   │
│ Singer 2004                   │ Shared neural activation (empathy)    │
└──────────────────────────────┴────────────────────────────────────────┘
```

### §12.5 — Open Questions

```
Q1: Group Resonance (>2 people) — emergent beyond dyadic sum?
     (Concert, classroom settings)
Q2: Joint action + efference copy when 2 people act simultaneously?
     (Sebanz & Knoblich 2006)
Q3: Body-Need priority algorithm — how does the body "choose"
     which need to pursue?
Q4: PFC accuracy measurement — how to operationalize
     "accuracy of self-narrative"?
Q5: Compilation level measurable?
     Proxy: reaction time? metabolic cost? ERP?
Q6: Can an incorrectly compiled path (phone-scrolling habit)
     be de-compiled without replacing it?
Q7: Domain reality checking — trainable as a compiled habit
     vs always requiring PFC effort?
Q8: Species-level hardware overlap specifics →
     minimum match guarantee?
Q9: AI body-base equivalent feasibility?
```

---

*English translation of Inter-Body-Mechanism.md (Vietnamese source, v2.1)*
*Translation target: English-speaking audience — rewritten for clarity and natural English expression.*
*All framework vocabulary preserved exactly as defined in the Human Predictive Drive Framework.*
