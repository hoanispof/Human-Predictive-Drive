---
title: Drive — Observation Parameter (Integration)
version: 1.2
created: 2026-04-20
updated: 2026-05-17
refined: 2026-05-23 (v1.2 — Concept Cascade: +Simulation-Engine, +Entity-Access, +Satiation types. Updated versions + cross-refs)
status: OBSERVATION PARAMETER v1.2
scope: |
  INTEGRATION FILE: Drive = label for energy + direction emergent from
  chunk dynamics + body-feedback. This file DOES NOT add new mechanisms —
  it INTEGRATES all observation parameters (Novelty, Threat, Status,...) to
  explain: "Why THIS action at THIS moment?"
  PFC participation spectrum, drive conflict, signal strength model.
  v1.1 KEY CHANGES:
    ⑪ +Compilable Architecture: drive = emergent from general-purpose reward system
    ⑫ +Compiled/Fresh: compiled drive (Drive-PFC-Absent/Monitor) vs fresh drive
        (Drive-PFC-Spinning through Override)
    ⑬ +Domain=Arbiter: drive direction CAN BE WRONG
    ⑭ Version refs synced (Valence-Propagation v2.0, Body-Feedback-Mechanism v2.0,
        Feeling v3.0)
    ⑮ +Cross-refs: Inter-Body-Mechanism.md v1.0, Body-Feedback-Label.md v2.0
purpose: |
  Novelty.md + Threat.md = individual mechanisms.
  This file = HOW they COMBINE → action at each moment.
  Core v7.8 §8 lists observation parameters. This file explains the interaction.
position: |
  Core-Deep-Dive/Observation/ — INTEGRATION file, read AFTER Novelty + Threat.
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, §8 observation parameters
  - Observation/Novelty.md v1.0 — PULL toward opportunity
  - Observation/Threat.md v1.0 — PUSH away from harm
  - Body-Feedback-Mechanism.md v2.0 — Shift/Miss/Gap, dual-pull
  - Chunk.md v2.0 — chunk substrate, compilation
  - Cortisol-Baseline.md v2.0 — amplifier dynamics
  - Feeling.md v3.0 — PFC observation interface
  - Imagine-Final-Evaluation.md — 2 axes × 4 angles
  - Anchor-Schema.md — Trust binding, sync point
  - Inter-Body-Mechanism.md v1.0 — Compilable Architecture, Compiled/Fresh, Domain=Arbiter
  - Body-Feedback-Label.md v2.0 — vocabulary reference
  - PFC/Simulation-Engine.md v1.0 — drive prediction uses Simulation-Engine
  - Chunk/Agent-Mechanism/Entity-Access.md v1.2 — drive directed at entities along gradient
  - Body-Feedback/Gap-Body-Need.md v1.0 — different drives have different satiation profiles
sources_backup: |
  Rewritten from: Drive.md v1.1 (2,733L)
  Backup: _backup/Drive-v75-era/
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Drive — Observation Parameter (Integration)

> A CEO decides to lay off 200 people (PFC ~85%, high cortisol, moral dissonance).
> Two hours later, back home playing with their child (PFC ~5%, automatic, happy).
>
> Same person. Same brain. DIFFERENT drives → COMPLETELY DIFFERENT mode.
>
> "Drive" is not a single module you switch on or off — it is a LABEL for the
> energy + direction CURRENTLY EMERGENT at the moment of observation.
>
> This file explains: why the same person behaves differently,
> HOW the PFC participates, and what happens when drives conflict.

---

## Table of Contents

- §0 — DRIVE AS OBSERVATION PARAMETER
- §1 — THE UNCONSCIOUS AS ENGINE, PFC AS OBSERVER-ORCHESTRATOR
- §2 — PFC PARTICIPATION SPECTRUM: 6 MODES
- §3 — DRIVE CONFLICT: 4 TYPES + RESOLUTION
- §4 — PULL vs PUSH: WHY IT MATTERS
- §5 — HONEST ASSESSMENT
- §6 — CROSS-REFERENCES

---

## §0 — DRIVE AS OBSERVATION PARAMETER

```
⭐ REFRAME v7.8:

  Core v7.5 (old): 3 drives (Novelty/Status/Protect) = L3 operators
  Core v7.8 (new): Drive = observation parameter — label for energy+direction
                   emergent from chunk dynamics + body-feedback

  Drive IS NOT:
    ✗ "Decision → action" (wrong order)
      → Reality: body-need → drive → action → THEN "know" a decision was made
    ✗ "Conscious mind controls behavior" (dualism)
      → Reality: unconscious = primary engine (~95% of decisions)
    ✗ "Need motivation before acting" (simple motivation theory)
      → Reality: drives run CONTINUOUSLY, "lacking motivation" = drives CONFLICTING
    ✗ "1 drive at 1 moment" (single-channel model)
      → Reality: MANY drives SIMULTANEOUSLY → action = emergent output

  Drive IS:
    ○ Continuous — NEVER turns off (even during sleep: REM processing)
    ○ Multi-channel — many patterns running IN PARALLEL
    ○ Predictive — anticipates + acts ahead (not reactive)
    ○ Body-grounded — ALL drives START from body-feedback
    ○ Emergent — action = OUTPUT, not INPUT


⭐ COMPILABLE ARCHITECTURE → DRIVE EMERGENT (Inter-Body-Mechanism.md §1.2):

  HARDWIRED ARCHITECTURE (insects, simple animals):
    Hardwired circuits: food→eat, predator→flee, mate→approach.
    No need for "drive" — stimulus→response is FIXED.
    No PFC → no deliberation → no conflict.

  COMPILABLE ARCHITECTURE (humans):
    Hardwired: ONLY the reward MECHANISM + compilation + social + PFC.
    Content: LEARNED from environment → compiles → body-need.
    → NO "drive module" hardwired for specific behaviors.
    → Drive = EMERGENT OUTPUT from the general-purpose system:
      body-need aggregate + chunk dynamics + prediction + PFC orchestration
      → energy + direction appear → = "drive"

  → Drive is a LABEL for energy+direction emergent from Compilable Architecture.
  → Hardwired Architecture DOES NOT NEED the concept "drive" (stimulus→response
      is sufficient).
  → Compilable Architecture NEEDS the concept "drive" because output is NOT
      predetermined.

  🟡 Hardwired/Compilable Architecture = framework synthesis
      (Inter-Body-Mechanism.md §1.2). Underlying neuroscience
      (general-purpose reward, Hebbian) = 🟢.


DRIVE IN THE CYCLE (Core v7.8 §1):

  Domain → Body-Input → Unconscious(Chunks) → Feeling → PFC → Body-Output → Domain

  "Drive" = observation point for the ENTIRE cycle:
  → Body-Input generates body-feedback signals
  → Chunks process: match patterns, detect gaps, predict outcomes
  → Multiple body-feedback signals fire SIMULTANEOUSLY
  → Integrate → energy + direction EMERGE → action
  → = "Drive" = label for that energy + direction

  Observation value:
    → Predict: "this person is novelty-driven" → behavioral tendency
    → Communicate: "he is threat-driven" → describes state
    → Diagnose: "lacking drive" → boredom territory
    → BUT: intervene at the mechanism level, NOT the observation level

  ⚠️ DOMAIN = ARBITER — drive direction CAN BE WRONG:
    → Strong drive ≠ CORRECT drive.
    → Body-need fires → PFC creates direction → BUT PFC = Lawyer
      (Inter-Body-Mechanism.md §7): narrative serves body-need,
      does NOT necessarily fit domain reality.
    → Example: novelty drive pulling toward conspiracy theories = strong but WRONG direction.
    → Example: threat drive pulling away from a good opportunity = strong but WRONG direction.
    → Domain feedback = THE ONLY ARBITER that checks drive direction.
    → "Feels right" ≠ "Is right" — domain verification is needed.
    🟡 Domain=Arbiter = framework principle (Inter-Body-Mechanism.md §9)


POSITION OF THIS FILE:

  ┌─────────────────────────────────────────────────────────┐
  │ OBSERVATION PARAMETERS (individual):                    │
  │   Novelty.md  — PULL toward opportunity                 │
  │   Threat.md   — PUSH away from harm                     │
  │   (Status, Connection, Meaning,... — Core v7.8 §8)     │
  └────────────────────────┬────────────────────────────────┘
                           │
                           ▼
  ┌─────────────────────────────────────────────────────────┐
  │ INTEGRATION (THIS file):                                │
  │   HOW parameters combine → action at each moment       │
  │   PFC participation spectrum                            │
  │   Drive conflict + resolution                           │
  └─────────────────────────────────────────────────────────┘
```

---

## §1 — THE UNCONSCIOUS AS ENGINE, PFC AS OBSERVER-ORCHESTRATOR

```
⭐ WHY IS THE UNCONSCIOUS THE PRIMARY ENGINE?

  4 reasons the unconscious BEATS PFC in EVERY race:

  ① CAPACITY: ~95% of brain bandwidth
    → Unconscious: MILLIONS of signals/second
    → PFC: ~4±1 items simultaneously (Cowan 2001)
    → = PFC is a SMALL spotlight on an ENORMOUS stage

  ② SPEED: milliseconds vs seconds
    → Compiled chunks fire in ms
    → PFC: 200ms+ deliberation
    → = Unconscious HAS ALREADY ACTED before PFC can "think"

  ③ EFFICIENCY: low energy cost
    → Compiled schemas = automatic = low energy
    → PFC deliberation = processing-intensive (~2% mass, ~20% energy)
    → = The brain CONSERVES by using the unconscious TO THE MAXIMUM

  ④ EVOLUTION: 500 million years vs ~2 million years
    → Unconscious: present in ALL animals (500M years of fine-tuning)
    → PFC: fully developed only in humans (~2M years)
    → = PFC BUILDS ON TOP OF the unconscious, does NOT REPLACE it

  → CONCLUSION:
    → Unconscious = DEFAULT mode → runs AT ALL TIMES
    → PFC = EXCEPTION mode → runs WHEN NEEDED
    → MOST of life = unconscious handles it → PFC at rest
    → PFC engages when: new dissonance, large novelty, new threat,
      drives conflict, Imagine-Final threatened


⭐ SIGNAL STRENGTH MODEL (replaces Layer Priority):

  v7.5 (old): L0 > L1 > L2 > L3 (fixed priority)
  v7.8 (new): STRONGEST signal wins (no fixed hierarchy)

  → L0 signals HAPPEN TO BE loudest (evolutionary design for survival)
  → BUT: NOT always. Context determines:
    → Normally: hunger (strong) overrides curiosity (weak) → find food
    → But: Einstein skipped meals to imagine (PFC overrides body-input)
    → But: people held in hiding accepted extreme threats for many reward chains
    → = Valence chain CAN override signal strength
      (Valence-Propagation.md §5③)

  → PFC CAN override (Drive-PFC-Override, §2) — but ALWAYS AT A COST
  → Sustained override → repair debt → body eventually wins

  ⭐ COMPILED/FRESH = THE REAL AXIS (Inter-Body-Mechanism.md §3):

    Unconscious vs PFC IS ACTUALLY the Compiled vs Fresh spectrum:

    COMPILED DRIVE (Compiled — automatic, cost ≈ 0):
      → Chunks already compiled → body-feedback direct → action EMERGES
      → Unconscious auto → Drive-PFC-Absent/Monitor (§2)
      → Example: driving a familiar route (compiled route chunks fire → auto)
      → Example: chef sees ingredients → "instantly knows" what to make
      → = Most of everyday life (~70-80%) = compiled drive

    FRESH DRIVE (Fresh — PFC drafts, cost > 0):
      → NEW situation / conflict → chunks don't match → PFC must draft
      → PFC deliberates → Drive-PFC-Spinning through Override (§2)
      → Example: first day at work → everything new → PFC constantly drafting
      → Example: conflict between novelty vs threat → PFC arbitrates
      → = New + difficult situations = fresh drive territory

    TRANSITION Fresh→Compiled (Learning):
      → Fresh drive repeats + resolves → chunks compile → compiled drive
      → = "First day at work" (fresh) → "month 6" (compiled)
      → Kahneman System 1 (compiled) / System 2 (fresh) equivalent
      → Details: Inter-Body-Mechanism.md §3.3

    → INSIGHT: Drive-PFC-Spinning vs Drive-PFC-Resolve = SAME fresh territory
      → Differ in chunk availability, NOT activation level

  🟢 Unconscious processing dominance = neuroscience consensus
  🟢 PFC capacity limits = Cowan 2001 (4±1)
  🟢 PFC energy cost = Raichle 2006
  🟢 Evolutionary timeline = comparative neuroscience
  🟡 Compiled/Fresh drive distinction = framework synthesis (consistent with Kahneman)


⭐ AT EVERY MOMENT, MANY SIGNALS ARE RUNNING SIMULTANEOUSLY:

  ┌────────────────────────────────────────────────────────┐
  │  Body-input signals:  which channels are starved?      │
  │  Chunk patterns:      what matches? gaps? conflicts?   │
  │  Body-feedback:       reward or dissonance? how much?  │
  │  Imagine-Final:       which action serves long-term?   │
  │                                                        │
  │  → Integrate → STRONGEST SIGNAL WINS                  │
  │  → = energy + direction EMERGE → action               │
  └────────────────────────────────────────────────────────┘

  Most of the time: signals ALIGN → action SMOOTH:
    → Body OK + compiled chunks match context + no dissonance
    → = PFC NOT NEEDED → Drive-PFC-Absent/Monitor (§2)
    → = "Ordinary everyday life"

  When signals CONFLICT or are STARVED:
    → Body urgent + chunks don't match + high dissonance
    → = PFC is called → Drive-PFC-Spinning through Override (§2)
    → = "Difficult situations" — PFC participation needed
```

---

## §2 — PFC PARTICIPATION SPECTRUM: 6 MODES

```
⭐ PFC = CONTINUOUS SPECTRUM, NOT ON/OFF

  PFC participation = spectrum from 0% → 95%
  Framework discretizes into 6 MODES for communication.

  2 AXES:
    Axis 1: PFC ACTIVATION — "How BUSY is PFC?"
    Axis 2: PFC EFFECTIVENESS — "Is PFC being USEFUL while busy?"

  ⚠️ IMPORTANT INSIGHT:
    HIGH activation ≠ HIGH effectiveness
    Drive-PFC-Spinning: PFC 30-50% but NOT effective (insufficient chunks)
    Drive-PFC-Resolve: PFC 20-40% but VERY effective (sufficient chunks)
    → "Busier" ≠ "better" — CHUNKS determine PFC quality


2-AXIS DIAGRAM:

  PFC EFFECTIVENESS ▲
  (chunks quality)   │
                     │
    HIGH ────────────┤── [DRIVE-PFC-RESOLVE] ──── [DRIVE-PFC-STRATEGIC] ──
    (chunks           │    PFC 20-40%                PFC 60-80%
     sufficient,      │    scan → match → act        hold → optimize
     relevant)        │                                       │
                      │                              [DRIVE-PFC-OVERRIDE]
                      │                                PFC 80-95%
                      │                                against body-base
                      │                                ⚠️ EXTREMELY costly
                      │
    LOW ─────────────┤── [DRIVE-PFC-SPINNING]
    (chunks           │    PFC 30-50%
     insufficient,    │    try → fail → try → fail
     wrong level)     │
                      │
    N/A ─────────────┤── [DRIVE-PFC-ABSENT] ─── [DRIVE-PFC-MONITOR]
    (PFC not needed)  │    PFC 0-5%                PFC 5-15%
                      │    fully automatic          background scan
                      │
                      └──────────────────────────────────────────►
                          0%     20%     40%     60%     80%    95%
                                    PFC ACTIVATION (% bandwidth)

  ⚠️ 6 modes = labeled ZONES on a continuous spectrum, not 6 fixed boxes.


═══════════════════════════════════════════════════════
DRIVE-PFC-ABSENT (PFC ~0-5%)
═══════════════════════════════════════════════════════

  Fully automatic unconscious. PFC "lights off."
  Conditions: safe context + compiled chunks + no dissonance

  Examples: playing with children, walking a familiar route, driving reflexes
  = ~60-70% of waking time. "Normal," "natural."

  🟢 Automatic behavior dominance = neuroscience consensus


═══════════════════════════════════════════════════════
DRIVE-PFC-MONITOR (PFC ~5-15%)
═══════════════════════════════════════════════════════

  PFC observing, NOT intervening. "Security camera."
  Unconscious still running ~90%. PFC scans: "anything unusual?"
  If dissonance detected → escalates to Drive-PFC-Spinning+.

  Example: driving a familiar route, friend asks to hang out
      (PFC: "am I free? → yes, OK")

  🟢 Background monitoring = attention research (Posner 1980)


═══════════════════════════════════════════════════════
DRIVE-PFC-SPINNING (PFC ~30-50%, INSUFFICIENT chunks)
═══════════════════════════════════════════════════════

  ⭐ MOST UNCOMFORTABLE MODE — PFC active but NOT effective.
  "Knows there's a problem, doesn't know how to fix it."

  Mechanism:
    → PFC scans chunks → finds ONLY solutions at the SAME LEVEL
    → Tries A → fails → A' → fails → A'' → fails
    → The CORRECT solution = DIFFERENT LEVEL — but chunks for that level DON'T EXIST

  Example: bored watching TV
    → PFC: change channel? scroll social media? snack? → ALL 3 = same level (passive)
    → Correct solution: go outside, move, meet a friend (DIFFERENT LEVEL: active)
    → But the chunk "go for a walk" may: not exist / be weak / be suppressed

  Why most uncomfortable:
    → PFC active = HIGH processing load (serial bottleneck + catecholamine)
    → But: no resolution = reward 0
    → = HIGH cost + NO reward → WORST experience

  ⚠️ PFC% higher than Drive-PFC-Resolve — because of FORCED searching, not because
      it's more capable.

  🟡 Spinning mechanism = framework analysis
  🟢 PFC energy cost without reward = frustration research


═══════════════════════════════════════════════════════
DRIVE-PFC-RESOLVE (PFC ~20-40%, SUFFICIENT chunks)
═══════════════════════════════════════════════════════

  PFC active AND effective. "Knows the problem AND knows how to fix it."
  Scan → match → act → resolve → PFC decreases.

  Example: doctor encounters familiar symptom → chunks match → diagnoses → done
  = "Expertise" = Drive-PFC-Resolve in a specific domain

  ⚠️ PFC% LOWER than Drive-PFC-Spinning because chunks are sufficient → scan fast → done.
  → = Chunks determine spinning vs resolve, NOT "effort"

  🟢 Expertise = pattern recognition (Chase & Simon 1973)


═══════════════════════════════════════════════════════
DRIVE-PFC-STRATEGIC (PFC ~60-80%, MANY + META chunks)
═══════════════════════════════════════════════════════

  PFC HAS a solution → but HOLDS.
  Meta-observes: "is the immediate solution OPTIMAL long-term?"

  = Drive-PFC-Resolve + META-COGNITIVE layer:
    → PFC evaluates PFC: "am I thinking about this correctly?"
    → Metacognition (Flavell 1979)

  6 ways to gather more data while holding:
    → Read/research, ask experienced people, sleep (REM consolidation),
      release → DMN (walk, shower → unconscious processes),
      observe more, imagine and simulate scenarios

  Example: CEO holds before an investment decision → "need more data"

  🟢 Metacognition = Flavell 1979
  🟡 Drive-PFC-Strategic as distinct from Drive-PFC-Resolve = framework distinction


═══════════════════════════════════════════════════════
DRIVE-PFC-OVERRIDE (PFC ~80-95%)
═══════════════════════════════════════════════════════

  PFC WORKS AGAINST body-feedback signal. Most costly, most rare.

  → Skipping meals to finish a deadline
  → Tough love (overriding empathy for long-term benefit)
  → Staying in a dangerous situation out of duty

  ⚠️ ALWAYS AT A COST (body protests):
    → Cost ∝ intensity of body drive × duration of override
    → Mild, short override → small cost, fast recovery
    → Strong, prolonged override → burnout, trauma
    → = "Daily override" = path to burnout

  🟢 Executive function override = Miller & Cohen 2001


SUMMARY:

  ┌─────────────────────┬──────────┬──────────────┬──────────────────────────┐
  │ Drive Mode          │ PFC %    │ Effectiveness│ When                     │
  ├─────────────────────┼──────────┼──────────────┼──────────────────────────┤
  │ Drive-PFC-Absent    │  0-5%    │ N/A          │ Auto, safe, compiled     │
  │ Drive-PFC-Monitor   │  5-15%   │ N/A          │ Scan, ready to activate  │
  │ Drive-PFC-Spinning  │ 30-50%   │ LOW          │ Dissonance + no chunks   │
  │ Drive-PFC-Resolve   │ 20-40%   │ HIGH         │ Dissonance + chunks OK   │
  │ Drive-PFC-Strategic │ 60-80%   │ HIGH + META  │ Complex, needs optimizing│
  │ Drive-PFC-Override  │ 80-95%   │ HIGH but COST│ Against body, last resort│
  └─────────────────────┴──────────┴──────────────┴──────────────────────────┘

  → MOST of life: Drive-PFC-Absent/Monitor (~70-80% of waking time)
  → Drive-PFC-Spinning vs Resolve = SAME situation, DIFFERENT chunks →
      DIFFERENT mode → DIFFERENT output
  → = Chunks = THE DETERMINING VARIABLE
```

---

## §3 — DRIVE CONFLICT: 4 TYPES + RESOLUTION

```
⭐ WHY CONFLICT MATTERS:

  Humans are "complex" because drives FREQUENTLY CONFLICT.
  Many signals SIMULTANEOUSLY + in different directions = conflict →
      "mysterious" behavior
  Understanding conflict types → explains MOST "irrational" behavior


═══════════════════════════════════════════════════════
TYPE 1: SIGNAL STRENGTH (survival override)
═══════════════════════════════════════════════════════

  When body-input signal is EXTREMELY STRONG → overrides EVERYTHING else.
  → Unconscious AUTO, PFC does not participate.

  Specific mechanism: NE flood → α1 receptors → PFC DISCONNECTS
    → PFC is literally cut off → CANNOT negotiate
    → Not "PFC chooses to yield" — body SHUTS DOWN PFC (Arnsten 2009)

  Examples:
    → Oxygen deprived → breathe, regardless of what is happening
    → Very hungry → stop everything → find food
    → Tiger → forget status → RUN

  🟢 α1 receptor → PFC offline = Arnsten 2009, LeDoux 1996


═══════════════════════════════════════════════════════
TYPE 2: NOVELTY vs THREAT (pull vs push)
═══════════════════════════════════════════════════════

  When Novelty (PULL) vs Threat (PUSH) toward the SAME target.

  → Novelty > Threat → EXPLORE (approach wins)
  → Threat > Novelty → STAY BACK (avoid wins)
  → Equal → FROZEN → PFC must arbitrate

  Example: want to change careers
    → Novelty: "new field, exciting, growth"
    → Threat: "loss of income, family disapproves, risk of failure"
    → Resolution depends on chunks:
      → HAS chunks (network, savings, skills): Drive-PFC-Resolve → change
      → LACKS chunks: Drive-PFC-Spinning → "wants to but is afraid"
      → META chunks: Drive-PFC-Strategic → "prepare 6 months first"

  🟢 Approach-avoidance conflict = Lewin 1935, Miller 1944


═══════════════════════════════════════════════════════
TYPE 3: BODY-FEEDBACK vs PFC (override territory)
═══════════════════════════════════════════════════════

  Body wants X NOW, PFC says NO.
  = PFC uses a DISTANT Imagine-Final to override a NEAR body-feedback.
  = Drive-PFC-Override — always at a cost.

  Examples:
    → Sleep (body) vs Deadline (PFC) → stay awake → cost: repair debt
    → Empathy (body) vs Strategy (PFC) → don't help → cost: guilt
    → Fear (body) vs Duty (PFC) → stay → cost: trauma risk

  → Cost ∝ intensity × duration. Prolonged = burnout.

  🟢 PFC override = executive function (Miller & Cohen 2001)


═══════════════════════════════════════════════════════
TYPE 4: INTRA-OBSERVATION (same level, different directions)
═══════════════════════════════════════════════════════

  When 2 observation patterns have equal signal strength, DIFFERENT directions.
  → MOST COMPLEX — no auto priority → PFC uses Imagine-Final as tiebreaker.

  Example: speak candidly vs maintain harmony
    → Integrity: "should speak candidly"
    → Status: "speaking candidly → offend someone"
    → PFC arbitrates: Imagine-Final "respected leader" → choose candor
    → OR: Imagine-Final "harmonious relationship" → choose harmony

  Example: parents vs career
    → Empathy schema: "care for parents, want to please them"
    → Growth schema: "want to develop, seek challenges"
    → EQUAL strength, BOTH feel "right" → PFC arbitrates based on Imagine-Final
    → There is NO single correct answer — framework EXPLAINS, does not prescribe

  🟡 Intra-observation conflict = framework classification
  🟢 Multiple social motives = Fiske 2004


═══════════════════════════════════════════════════════
RESOLUTION RULES — 5 rules in order
═══════════════════════════════════════════════════════

  1. EMERGENCY → strongest signal AUTO WINS (PFC not involved)

  2. NON-EMERGENCY → PFC arbitrates based on IMAGINE-FINAL
     → Imagine-Final clear → fast resolution (Drive-PFC-Resolve)
     → Imagine-Final unclear → spinning (Drive-PFC-Spinning) or
         deliberation (Drive-PFC-Strategic)

  3. EQUAL STRENGTH → intensity + Imagine-Final relevance decide
     → Truly equal → FROZEN → need more information/time

  4. PFC OVERRIDE → possible but COSTLY
     → Use sparingly — "daily override" = burnout path

  5. NO IMMEDIATE RESOLUTION → 3 options:
     a) FROZEN → need more chunks, data, time
     b) STRATEGIC ACCEPT → accept temporary dissonance (conserve PFC)
     c) RELEASE → DMN → let unconscious process → possible eureka

  ⚠️ CONFLICT CAN BE GOOD:
    → Conflict FORCES PFC to participate → evaluate → grow
    → Resolve → NEW chunks compile → mode upgrade
    → = "Difficulty" = opportunity (if resolved)
    → = "Difficulty" = damage (if NOT resolved + prolonged)
```

---

## §4 — PULL vs PUSH: WHY IT MATTERS

```
⭐ CORE: SAME BEHAVIOR → DIFFERENT DRIVE → DIFFERENT SUSTAINABILITY

  PULL drives (novelty, connection, experience):
    → "Want to do it" → enjoy the process → sustainable
    → Body-feedback: reward per step → positive chunks compile
    → Satisfaction: CAN fire → natural endpoint

  PUSH drive (threat):
    → "Have to do it" → endure the process → costs cortisol → not sustainable
    → Body-feedback: relief when threat temporarily gone (≠ reward)
    → Satisfaction: HARD to fire → no natural endpoint
    → = "Avoiding threat ≠ body-need fulfilled"

  COMPARISON:

    ┌────────────────┬────────────────┬────────────────┐
    │                │ PULL drives    │ PUSH drive     │
    ├────────────────┼────────────────┼────────────────┤
    │ Direction      │ TOWARD reward  │ AWAY FROM harm │
    │ Felt as        │ "Want to"      │ "Have to"      │
    │ Process feel   │ Enjoy          │ Stress         │
    │ Endpoint       │ Clear (when    │ UNCLEAR        │
    │                │ satisfied)     │                │
    │ Satisfaction   │ Fires ✅       │ Hard to fire ❌│
    │ Sustainability │ High           │ LOW            │
    │ Schema compile │ Positive       │ Negative       │
    │ Body cost      │ Low            │ HIGH           │
    │ When healthy   │ Default mode   │ Emergency      │
    │ When dominant  │ Flow territory │ BURNOUT        │
    └────────────────┴────────────────┴────────────────┘


DRIVE × NEW CONCEPTS (28-session Drill Propagation):

  SIMULATION-ENGINE (Simulation-Engine.md v1.0):
    → Drive PREDICTION uses Simulation-Engine: PFC simulates outcome → body evaluates
    → "Want to do it" = Simulation-Engine drafts → body REWARD → approach
    → "Have to do it" = Simulation-Engine drafts → body THREAT → avoid or endure

  ENTITY-ACCESS GRADIENT (Entity-Access.md v1.2):
    → Drives DIRECTED AT entities along Level 0-5 gradient
    → Drive toward Level 5 entity (child, self) = STRONGER than Level 1 (acquaintance)
    → Hardware-Subsidy: body provides baseline drive "for free" per entity level
    → = WHY drive to protect a child > drive to protect a colleague

  SATIATION TYPES (Gap-Body-Need.md v1.0):
    → Different drives have DIFFERENT satiation profiles:
      ENGINE satiation: mechanism generating the drive gets tired
          (dopamine downregulation)
      ROAD satiation: familiar path fills → new path needed
      VEHICLE satiation: specific entity saturates
    → PULL drives: usually ROAD/VEHICLE satiation (novelty → bored with path,
        not the engine)
    → PUSH drives: ENGINE satiation rarely occurs (threat = survival → body
        DOES NOT ALLOW tiredness)
    → = Explains why threat-drive is HARD TO STOP ON ITS OWN (§4 below)


⭐ THREAT-DRIVE DOMINANCE IN MODERN LIFE:

  Most modern activities are HIJACKED by threat-drive:

    GOING TO WORK:
      Ideal: novelty + connection drive → enjoy
      Reality: "lose job → lose money → suffer" → threat → endure

    STUDYING:
      Ideal: novelty drive → curiosity → learn because it's interesting
      Reality: "fail exam → parents scold → future collapses" → threat →
          study just to pass

    RELATIONSHIPS:
      Ideal: connection drive → close because it's warm
      Reality: "break up → be alone" → threat → stay because scared

  → Pattern: same behavior → different drive → different output + sustainability
  → NOT the behavior that's wrong → the DRIVE is wrong
  → Threat-Drive is DESIGNED for emergencies (short-term)
  → Society has turned it into the DEFAULT (long-term) = BURNOUT


⭐ SHIFTING FROM PUSH → PULL:

  OPEN QUESTION (Threat-Drive-Analysis.md §14):
    → Can Threat CONVERT to pull?
    → "Have to study" → gradually → "want to study"?
    → POSSIBLE: if in the process of "having to" → accidentally ENJOYS →
        new schema
    → BUT: cortisol TOO HIGH → PFC offline → CANNOT discover enjoyment
    → = PARADOX: threat-drive PREVENTS the very shift toward pull-drive
    → = Why: reduce threat FIRST, then build the novelty path

  🟡 Pull vs push sustainability = framework analysis
  🟢 Threat designed for emergency (stress physiology)
  🟡 Modern threat-drive dominance = derived, consistent with epidemiology
```

---

## §5 — HONEST ASSESSMENT

```
  FULL FILE — HONEST EVALUATION:

  🟢 VERIFIED (neuroscience / established research):
    ┌────────────────────────────────────────────────────────────┐
    │ Unconscious processing dominance (Dijksterhuis, Bargh)     │
    │ PFC capacity limits — 4±1 (Cowan 2001)                     │
    │ PFC energy cost (Raichle 2006)                              │
    │ Evolutionary timeline PFC vs subcortical                    │
    │ NE → α1 → PFC disconnect (Arnsten 2009)                    │
    │ Pattern recognition = expertise (Chase & Simon 1973)        │
    │ Approach-avoidance conflict (Lewin 1935, Miller 1944)       │
    │ Executive function override (Miller & Cohen 2001)           │
    │ Metacognition (Flavell 1979)                                │
    │ Predictive processing (Clark 2013, Friston)                 │
    │ Parallel processing (multiple circuits simultaneously)      │
    │ Automatic behavior = established                            │
    │ Background monitoring (Posner 1980)                         │
    └────────────────────────────────────────────────────────────┘

  🟡 FRAMEWORK SYNTHESIS (consistent logic, derived from 🟢):
    ┌────────────────────────────────────────────────────────────┐
    │ Drive = observation parameter (not an operator)             │
    │ Signal strength model (vs fixed layer priority)             │
    │ 6 PFC modes on 2-axis spectrum                              │
    │ Drive-PFC-Spinning vs Resolve differentiated by chunks      │
    │ 4 conflict types classification                             │
    │ 5 resolution rules                                          │
    │ Pull vs Push sustainability difference                      │
    │ Modern threat-drive dominance                               │
    │ Conflict as growth opportunity                               │
    │ Push→Pull transition paradox                                │
    │ Compilable Architecture → drive emergent (v1.1)             │
    │ Compiled/Fresh drive distinction (v1.1)                     │
    │ Domain=Arbiter — drive direction can be wrong (v1.1)        │
    └────────────────────────────────────────────────────────────┘

  🔴 HYPOTHESIS (logical but unverified):
    ┌────────────────────────────────────────────────────────────┐
    │ Exact PFC% per mode — approximation                         │
    │ Drive-PFC-Absent/Monitor = 70-80% of waking time — est.    │
    │ Optimal pull:push ratio — unknown                           │
    │ Push→Pull transition conditions — unclear                   │
    │ Signal strength vs valence chain priority — case-dependent  │
    └────────────────────────────────────────────────────────────┘
```

---

## §6 — CROSS-REFERENCES

```
  ← FOUNDATION (read first):
    Core-v7.8-Draft.md §1 — cycle architecture
    Core-v7.8-Draft.md §8 — ALL observation parameters
    Observation/Novelty.md v1.2 — PULL mechanism deep-dive
    Observation/Threat.md v1.2 — PUSH mechanism deep-dive
    Inter-Body-Mechanism.md v1.0 §1.2 — Compilable Architecture
        (general-purpose → drive emergent)
    Inter-Body-Mechanism.md v1.0 §3 — Compiled/Fresh processing axis
    Inter-Body-Mechanism.md v1.0 §7 — PFC=Lawyer (Domain=Arbiter correction)
    PFC-Configuration.md v1.0 — §2 participation modes ORTHOGONAL with config
        (2026-05-10)

  ← MECHANISM (read first or alongside):
    Body-Feedback-Mechanism.md v2.0 — chunk dynamics → body-feedback
    Chunk.md v2.3 — chunk substrate
    Valence-Propagation.md v3.0 — structural/current valence, 3 firing modes
    Feeling.md v3.0 — PFC observation interface
    Cortisol-Baseline.md v2.0 — amplifier dynamics
    Body-Feedback-Label.md v2.0 — vocabulary reference
    Simulation-Engine.md v1.0 — drive prediction uses simulation
    Entity-Access.md v1.2 — drive directed at entities along gradient
    Gap-Body-Need.md v1.0 — satiation types per drive

  ↔ PARALLEL (same Observation/ folder):
    Observation/Empathy.md v4.0 — Self-Pattern-Modeling → detect drives in others
    Observation/Boredom.md v2.0 — when drive LACKS target (by-product match stops)
    Observation/Liking-Wanting.md — wanting overlaps with drive mechanism
    Observation/AI-Schema-Detection.md — detect drive patterns
    Schema.md v2.0 — schema = observation parameter for chunk patterns

  → DOWNSTREAM:
    Imagine-Final-Evaluation.md — quality of Imagine-Final → conflict resolution
    Anchor-Schema.md — Trust as tiebreaker in drive conflict

  → APPLICATIONS:
    Domain-Mapping-Drive.md — drive in education context
    Boredom-Analysis.md — when drive LACKS target

  STATUS:
    v1.0 — 2026-04-20 — written fresh for v7.8 cycle-based architecture
    v1.1 — 2026-05-17 — +Compilable Architecture, +Compiled/Fresh,
        +Domain=Arbiter, version sync
    v1.2 — 2026-05-23 — Concept Cascade: +Simulation-Engine, +Entity-Access
        gradient, +Satiation types, version updates
    Rewritten from: Drive.md v1.1-old (backup: _backup/Drive-v75-era/)
    Aligned: Core v7.8, Inter-Body-Mechanism v1.0, signal strength model
```
