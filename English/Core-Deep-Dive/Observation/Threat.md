---
title: Threat — Observation Parameter
version: 1.3
created: 2026-04-20
updated: 2026-05-25 (v1.3 — §3 +Evaluative/Direct-State × 3 mechanism sources mapping, Dissonance-Signal-Architecture v1.0 integration)
refined: 2026-05-23 (v1.2 — Concept Cascade: +Simulation-Engine, +Entity-Access, +Bond-Architecture. Updated versions + cross-refs)
status: OBSERVATION PARAMETER v1.3
scope: |
  OBSERVATION FILE: Threat = named pattern when observing body-feedback
  (dissonance direction) + prediction of harm. NOT a component.
  This file describes: mechanism, spectrum, 3 mechanism sources, 3 origin sources,
  Threat × Imagine-Final, anticipation loop, when adaptive vs harmful.
  v1.1 KEY CHANGES:
    ⑪ +Compilable Architecture: threat = general-purpose system detecting GAP TOWARD LOSS
    ⑫ +Compiled/Fresh: compiled threat (phobia, auto) vs fresh (novel danger, costly)
    ⑬ +PFC=Lawyer in threat: suppress / amplify / fabricate threat
    ⑭ Version refs synced (Valence-Propagation v2.0, Body-Feedback-Mechanism v2.0)
    ⑮ +Cross-refs: Inter-Body-Mechanism.md v1.0, Body-Feedback-Label.md v2.0
purpose: |
  Core v7.8 §8 defines Threat briefly ("Dissonance from predicted harm").
  This file is the DEEP-DIVE: neuroscience, practical patterns, education implications.
  Key feature: 3 origin sources (Domain/Peer/Imposed) = cornerstone for education.
position: |
  Core-Deep-Dive/Observation/ — sibling to Novelty.md, Schema.md, Empathy.md.
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, §8 observation parameters
  - Body-Feedback-Mechanism.md v2.0 — Chunk-Shift/Miss/Gap, 2 input sources
  - Cortisol-Baseline.md v2.0 — amplifier, chronic vs acute
  - Chunk.md v2.0 — chunk substrate, compilation under emotional peak
  - Valence-Propagation.md v2.0 — body evaluation, chain propagation
  - Observation/Novelty.md v1.0 — parallel structure (PULL vs PUSH)
  - Imagine-Final-Evaluation.md — 2 axes × 4 angles, Domain Fit × Hardware Fit
  - Anchor-Schema.md — Trust binding, sync point
  - Inter-Body-Mechanism.md v1.0 — Compilable Architecture, Compiled/Fresh, PFC=Lawyer
  - Body-Feedback-Label.md v2.0 — vocabulary reference
  - PFC/Simulation-Engine.md v1.0 — simulated threat (Imagine-Final v3.0 boundary)
  - Chunk/Agent-Mechanism/Entity-Access.md v1.2 — threat FROM entities (access-based)
  - Chunk/Agent-Mechanism/Bond-Architecture.md v2.0 — threat to bond → protect response
sources_backup: |
  Merged + rewritten from: Threat.md v1.1 (1,936L) + Threat-Drive-Analysis.md (700L)
  Backup: _backup/Drive-v75-era/
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Threat — Observation Parameter

> Chased by a tiger → run. Fear of losing the job → sleepless nights.
> Worried the child will fail the exam → yell at the child.
> All of these are called "Threat" — but the mechanisms are COMPLETELY DIFFERENT.
>
> Tiger: physical, bounded, has an endorphin buffer, over in minutes.
> Job loss: anticipation, unbounded, no buffer, lasts months.
> Parenting anxiety: imposed, transmitted across generations, compiles the
> schema "authority = dangerous."
>
> Understanding that difference = understanding most modern anxiety.
>
> This file analyzes: what Threat looks like, the mechanisms underneath,
> the spectrum from micro to emergency, 2 taxonomies (mechanism + origin),
> why modern life is threat-dominant, and when threat is genuinely adaptive.

---

## Table of Contents

- §0 — THREAT AS OBSERVATION PARAMETER
- §1 — MECHANISM: BODY-FEEDBACK + PREDICTION OF HARM
- §2 — SPECTRUM: 5 LEVELS × 3 AXES
- §3 — 3 MECHANISM SOURCES: Physical / Social / Anticipation
- §4 — 3 ORIGIN SOURCES: Domain / Peer / Imposed
- §5 — THREAT × IMAGINE-FINAL: 3 CASES
- §6 — WHEN ADAPTIVE vs WHEN HARMFUL
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §0 — THREAT AS OBSERVATION PARAMETER

```
⭐ REFRAME v7.8:

  Core v7.5 (old): Threat emerges at each layer (L0→L4), Protect = L3 drive
  Core v7.8 (new): Threat = observation parameter — a label for a pattern

  Threat IS NOT:
    ✗ A separate channel (no "threat channel" in the brain)
    ✗ Layer-specific (not fixed to 1 location)
    ✗ Only in "L3 Protect" (that pattern was retired — observation parameter replaces it)
    ✗ Always bad (mechanism is NEUTRAL)

  Threat IS:
    ○ A label for the pattern: body-feedback (dissonance) + prediction of harm
    ○ Emergent from chunk dynamics — especially Chunk-Shift + Chunk-Miss
    ○ Appears ANYWHERE in the cycle when the body detects risk
    ○ Its value: to predict, communicate, and diagnose — NOT a mechanism itself

  COMPARISON WITH NOVELTY (parallel structure):

    ┌──────────────────┬──────────────────────────┬──────────────────────────┐
    │                  │ NOVELTY                  │ THREAT                   │
    ├──────────────────┼──────────────────────────┼──────────────────────────┤
    │ Base signal      │ Positive prediction delta│ Body-feedback dissonance │
    │ Interpretation   │ Opportunity              │ Harm                     │
    │ Direction        │ PULL (toward)            │ PUSH (away)              │
    │ Neurochemistry   │ Dopamine                 │ NE → Cortisol            │
    │ Natural brake    │ Habituation              │ Resolution of threat     │
    │ When it loops    │ Novelty Loop             │ Anxiety Loop             │
    │ Deep dive        │ Novelty.md               │ This file                │
    └──────────────────┴──────────────────────────┴──────────────────────────┘

  ⚠️ Novelty and Threat CAN run SIMULTANEOUSLY:
    → "Want to explore" (Novelty) + "Fear of failure" (Threat) = at the same time
    → The ratio determines the experience (Novelty.md §4.3: mixed loop)
    → See Observation/Drive.md for integration


⭐ COMPILABLE ARCHITECTURE → THREAT EXPANDS (Inter-Body-Mechanism.md §1.2):

  HARDWIRED ARCHITECTURE (insects, simple animals):
    Threat = HARDWIRED escape circuits: predator→flee, pain→withdraw.
    Detects ONLY threats ALREADY KNOWN (evolutionarily coded).
    A NEW threat that evolution hasn't coded → NOT detected → fatal.

  COMPILABLE ARCHITECTURE (humans):
    General-purpose system: LEARNS threats from experience + culture.
    → Detects NEW threats (social rejection, job loss, anticipation)
      that evolution CANNOT hardwire (because context changes constantly).
    → PFC simulates the future → predicts threats BEFORE THEY HAPPEN.
    → Culture transmits threats through language (no direct experience needed).

  → Compilable Architecture = why humans have a RICHER range of threat types:
    Physical (hardwired) + Social (learned) + Anticipation (PFC simulated).
  → Hardwired Architecture ONLY HAS Physical (hardwired escape).
  → = The POWER of Compilable Architecture AND the curse: detects MORE threats
    → more anxiety → but BETTER adaptation.

  🟡 Compilable Architecture threat expansion = framework synthesis.


THREAT IN THE CYCLE (Core v7.8 §1):

  Domain → Body-Input → Unconscious(Chunks) → Feeling → PFC → Body-Output → Domain
                              ↑
                    Body-feedback fires dissonance
                    + chunks predict harm
                    = "Threat" is observed

  Threat appears when:
  → Body-feedback fires in the dissonance direction (Chunk-Shift, Chunk-Miss)
  → AND: chunks predict "if nothing changes → bad consequences"
  → = Both components SIMULTANEOUSLY → Threat pattern emerges
  → Missing 1 component:
    → Dissonance WITHOUT prediction = just "discomfort" (boredom territory)
    → Prediction WITHOUT dissonance = just "knowing" (neutral knowledge)
```

---

## §1 — MECHANISM: BODY-FEEDBACK + PREDICTION OF HARM

```
⭐ THREAT = 2 COMPONENTS SIMULTANEOUSLY:

  ① BODY-FEEDBACK (dissonance direction) — SIGNAL:
    → "Something is wrong" — body detects mismatch
    → Spectrum: nagging unease → restless → worried → scared → panic → shutdown
    → = PURE SIGNAL (doesn't yet know WHY, only knows "something's off")
    → Underlying chunk dynamics:
      → Chunk-Shift: valence chunks change → dissonance
      → Chunk-Miss: familiar pattern absent → dissonance
      → Body-Feedback-Mechanism.md §3.1, §3.2

  ② PREDICTION OF HARM — INTERPRETATION:
    → Unconscious OR PFC predicts: "if nothing changes → BAD CONSEQUENCES"
    → Unconscious: reflex-level (tiger → run, NO PFC needed)
    → PFC: simulates the future (deadline → "if I'm late → I'll get fired")
    → = INTERPRETING the signal → determines the response

  → Same body-feedback signal → DIFFERENT interpretation → DIFFERENT output:
    → Dissonance + predict harm = THREAT
    → Dissonance + detect opportunity = NOVELTY
    → Dissonance + predict nothing = "discomfort" (boredom)


§1.1 — SCHEMA = TRIGGER, HORMONE = SUSTAIN

  ⚠️ IMPORTANT REFINEMENT — exact sequence:

  OLD (implied): hormone INITIATES threat
  NEW (correct): schema fires → hormone arrives AFTER

  Timeline:
    Schema fires       → NE spike        → Adrenaline     → Cortisol peak
    0ms                  500ms              1-2s              5-20 minutes
    ("Danger!")          (instant energy)   (fight/flight)    (sustain alert)

  Example:
    → Playing happily → suddenly remember "THE EXAM IS TODAY!"
    → Schema fires IMMEDIATELY: "exam = important + late = consequences"
    → At this moment cortisol IS STILL LOW (hasn't risen yet)
    → BUT body ALREADY KNOWS to get moving → SCHEMA knows, not cortisol
    → NE spike (0.5-2s): instant energy → start moving
    → Cortisol peak (5-20 min): SUSTAINS alert → still racing heart at school

  → Schema = TRIGGER (always fires first)
  → NE + Adrenaline = instant energy
  → Cortisol = SUSTAINER (maintains, does not initiate)

§1.2 — PFC = LAWYER IN THREAT (Inter-Body-Mechanism.md §7)

  ⭐ PFC is NOT a neutral judge — it is a LAWYER for the body-base.
  In the threat domain, PFC "argues the case" in 3 directions:

  ① SUPPRESS (denies threat when body IS signaling it):
    → Body: cortisol, restless, "something is wrong."
    → PFC: "It's fine." / "I'm overthinking." / "This is normal."
    → = PFC suppresses body signal → NO action → threat ACCUMULATES.
    → Example: physical symptoms → PFC: "probably nothing" → delays seeing a doctor.
    → Example: toxic relationship → PFC: "everyone's like this" → stays.

  ② AMPLIFY (exaggerates threat beyond reality):
    → Body: micro-dissonance (mild, context-appropriate).
    → PFC: "THIS IS DEFINITELY GOING TO GO TERRIBLY WRONG!" — catastrophizes
        beyond the real signal.
    → = PFC amplifies → cortisol RISES → anticipation loop (§3③) → anxiety.
    → Example: boss says "need to meet" (micro) → PFC: "I'm probably being fired" (strong).
    → Example: child has 38° fever → parent's PFC: "something serious!" (limited
        medical knowledge = fewer chunks).

  ③ FABRICATE (creates threat that doesn't exist):
    → Body: neutral or calm.
    → PFC: "But WHAT IF... ?" — generates threat FROM NOTHING.
    → = PFC generates threat → body responds (cortisol) → PFC: "See, I was right!"
    → = Self-fulfilling: PFC creates threat → body confirms → PFC believes more.
    → Example: 3am, everything is fine → PFC: "what if the company goes bankrupt?"

  ⚠️ DOMAIN = ARBITER — checks the PFC narrative:
    → PFC suppresses → domain feedback shows the threat IS real.
    → PFC amplifies → domain feedback shows the threat is SMALLER than imagined.
    → PFC fabricates → domain feedback shows there IS NO threat.
    → "Feeling unsafe" ≠ "Actually unsafe" — domain verification is needed.

  🟢 Gazzaniga split-brain: PFC confabulates reasons (literal lawyer).
  🟢 Haidt 2001: moral judgment = intuition → reasoning = post-hoc.
  🟡 3 distortion modes in threat = framework classification.


  EXCEPTION:
    Chronic hormone baseline DRIFT → hormone CAN drive directly:
    → High cortisol baseline → generalized anxiety (worry without clear cause)
    → = Abnormal, not the standard process
    → Cortisol-Baseline.md v2.0: details

  ⭐ COMPILED vs FRESH THREAT (Inter-Body-Mechanism.md §3):

    Compiled/Fresh = the real axis — applied to threat:

    COMPILED THREAT (Compiled — automatic, cost ≈ 0):
      → Schema ALREADY compiled: pattern → body-feedback IMMEDIATELY → auto response.
      → Example: phobia (spider → fear → run, NO PFC evaluation needed).
      → Example: someone already compiled as "dangerous" → body tenses IMMEDIATELY
          on sight.
      → Example: shouting SIMILAR to a parent's → compiled schema fires → scared
          even with a stranger.
      → = Trauma responses = COMPILED threat (extreme compilation under emotional peak).
      → FAST, low cost, BUT can be WRONG (overgeneralize).

    FRESH THREAT (Fresh — PFC drafts, cost > 0):
      → NEW situation with no existing schema → PFC must evaluate:
        "Is this dangerous? How much? What action?"
      → Example: strange email from new boss → PFC drafts: "praise or warning?"
      → Example: unfamiliar body symptom → PFC drafts: "illness or normal?"
      → SLOW, high cost, BUT more accurate (evaluates context).

    TRANSITION Fresh→Compiled:
      → Fresh threat repeated + confirmed → compiles → compiled threat.
      → = "First time scared: had to think" → "Tenth time: automatic."
      → Can be UNLEARNED (exposure therapy = forcing Compiled to re-evaluate
          → Fresh → recompile).
      → Kahneman: compiled threat ≈ System 1 fear, fresh threat ≈ System 2
          risk assessment.

  🟢 NE → adrenaline → cortisol cascade = neuroscience verified
  🟡 Schema = trigger, hormone = sustain = framework emphasis (consistent with timeline)
  🟡 Compiled/Fresh threat = framework synthesis (consistent with dual-process theory)
```

---

## §2 — SPECTRUM: 5 LEVELS × 3 AXES

```
⭐ THREAT IS NOT ON/OFF — IT IS A CONTINUOUS SPECTRUM

  Pop psychology: "stress" = 1 state (present or absent)
  Framework: Threat = SPECTRUM from micro-dissonance to shutdown

  3 SIMULTANEOUS AXES (3-dimensional space):
    ① INTENSITY: mild → extreme (neurochemical escalation)
    ② SOURCE: external-input → internal-predict → mixed
    ③ DURATION: acute (seconds) → chronic (years)


═══════════════════════════════════════════════════════
AXIS 1: INTENSITY — Neurochemical Escalation
═══════════════════════════════════════════════════════

  LEVEL 1 — MICRO (5-15% body resource):
    NE trace. Nagging unease, slight restlessness.
    PFC still normal. Response: scan, check.
    → Boss's email "need to meet" → micro-threat. Duration: seconds → minutes.
    → Cost: NEAR ZERO. Adaptive, beneficial.

  LEVEL 2 — MILD (15-30% body resource):
    NE clear + mild adrenaline. Mild worry.
    PFC functioning OPTIMALLY — sweet spot for problem-solving.
    → Deadline in 3 days, haven't started → mild worry → start working.
    → Cost: LOW. Yerkes-Dodson optimal.

  LEVEL 3 — MODERATE (30-60% body resource):
    High NE + adrenaline + cortisol BEGINS.
    PFC still functioning but tunnel vision (narrow focus, reduced creativity).
    → Deadline TOMORROW → cortisol → working through the night.
    → Cost: MODERATE. Productive short-term, harmful if prolonged.

  LEVEL 4 — STRONG (60-90% body resource):
    High NE + STRONG adrenaline + HIGH cortisol.
    PFC HEAVILY REDUCED — amygdala begins to override.
    → Threatened → fight or flight. Simple decisions, no nuance.
    → Cost: HIGH. Life-saving (acute) or harmful (chronic).

  LEVEL 5 — EMERGENCY (90-100% body resource):
    FULL mobilization. PFC NEARLY OFFLINE — amygdala in control.
    → 3 modes: Fight / Flight / Freeze
    → Shutdown (overload): vagal syncope — circuit breaker, not a signal
    → Cost: EXTREMELY HIGH. PTSD risk if prolonged.

  SUMMARY:
    ┌───────────┬──────────┬────────────────┬─────────────┬──────────────┐
    │ Level     │ Resource │ Neurochemistry │ PFC status  │ Response     │
    ├───────────┼──────────┼────────────────┼─────────────┼──────────────┤
    │ Micro     │  5-15%   │ NE trace       │ Normal      │ Scan, check  │
    │ Mild      │ 15-30%   │ NE + adrenaline│ OPTIMAL     │ Plan, prepare│
    │ Moderate  │ 30-60%   │ + cortisol     │ Tunnel      │ Act, focus   │
    │ Strong    │ 60-90%   │ + amygdala     │ HEAVILY ↓   │ Fight/flight │
    │ Emergency │ 90-100%  │ FULL mobilize  │ NEAR OFF    │ F/F/F/Shut   │
    └───────────┴──────────┴────────────────┴─────────────┴──────────────┘

  → MILD (15-30%) = SWEET SPOT for productivity
  → = Yerkes-Dodson law: performance optimal at MODERATE arousal

  🟢 NE → adrenaline → cortisol cascade = verified
  🟢 Amygdala overrides PFC (Arnsten 2009, LeDoux)
  🟢 Yerkes-Dodson law (1908, replicated)
  🟡 % body resource per level = framework approximation


═══════════════════════════════════════════════════════
AXIS 2: SOURCE — External vs Internal vs Mixed
═══════════════════════════════════════════════════════

  EXTERNAL-INPUT:
    → Signal from the SENSES — happening OUTSIDE right now
    → Speed: ms (reflex) → seconds. Unconscious reacts BEFORE PFC.
    → Endorphin buffer PRESENT (physical threat) → fast recovery
    → STOPS when external threat DISAPPEARS
    → Examples: tiger, someone jumping out, physical pain

  INTERNAL-PREDICT:
    → Threat GENERATED BY THE BRAIN — PFC or unconscious imagines harm
    → Body DOES NOT DISTINGUISH imagined vs real (~20-60% fidelity)
    → NO endorphin buffer (no physical pain)
    → NO clear endpoint ("when does the imagining stop?")
    → = PRIMARY SOURCE of modern anxiety
    → Examples: 3am worry about job loss, student dreading exam failure

  MIXED (External feeds Internal):
    → External event (real) → triggers schema → PFC imagines WORST CASE
    → = Small event + large imagination = threat EXCEEDS reality
    → Example: boss says "need to meet" (micro) → PFC: "I'm probably being fired" (strong)
    → Example: typical parenting anxiety: child has 38° fever → PFC: "something serious?"
    → Threat level = f(external input × internal imagination × accumulated chunks)

  ⭐ WHY KNOWLEDGE REDUCES THREAT:
    → Doctor sees child with 38° fever: "normal" → MICRO threat (sufficient medical chunks)
    → First-time parent sees child with 38° fever: "this is terrible!" → STRONG threat
        (fewer medical chunks)
    → = Same external input → DIFFERENT chunks → DIFFERENT threat level
    → = Education REDUCES threat (more chunks → more accurate prediction)

  SUMMARY:
    ┌──────────────┬────────────────┬────────────────┬────────────────┐
    │              │ External       │ Internal       │ Mixed          │
    ├──────────────┼────────────────┼────────────────┼────────────────┤
    │ Speed        │ ms (reflex)    │ Slow (imagined)│ Fast trigger   │
    │ Duration     │ Short (ends    │ LONG (no clear │ LONG (amplify) │
    │              │ when gone)     │ endpoint)      │                │
    │ Endorphin    │ PRESENT        │ ABSENT         │ Depends on mix │
    │ PFC role     │ Assess AFTER   │ GENERATE threat│ AMPLIFY threat │
    │ Modern risk  │ LOW (few tigers│ HIGH (anxiety) │ HIGH (news)    │
    └──────────────┴────────────────┴────────────────┴────────────────┘

  → Modern life: external threats DOWN (physically safest in history)
  → BUT: internal + mixed UP (social media, news, comparison, anticipation)
  → = PARADOX: physically safest ever — highest-ever anxiety

  🟢 Nocebo effect, stress response to imagined threat = verified
  🟢 Anticipatory anxiety → cortisol (Gaab et al. 2005)
  🟢 Catastrophizing = CBT research, knowledge reduces anxiety = verified


═══════════════════════════════════════════════════════
AXIS 3: DURATION — Acute vs Chronic
═══════════════════════════════════════════════════════

  ACUTE (seconds → hours):
    → Clear event → response → event ends → cortisol drops → repair
    → Body DESIGNED for acute. LOW cost if recovery is complete.

  CHRONIC (days → months → years):
    → NO clear event end → cortisol DOES NOT DROP
    → Body NOT DESIGNED for chronic → systems running on emergency continuously
    → Cortisol baseline rises → new normal = stressed
    → Repair IS CUT (body prioritizes threat response)
    → Neural wear: PFC dendrite retraction, hippocampus damage,
      immune suppression, reduced sleep quality (Cortisol-Baseline.md v2.0)

  ⭐ DURATION MATTERS MORE THAN INTENSITY:
    → Level 3 (moderate) + acute (1 night) = OK, body can repair
    → Level 3 (moderate) + chronic (6 months) = BURNOUT
    → Level 2 (mild) + chronic = WORSE than Level 4 (strong) + acute
    → = "Living with mild daily worry EVERY DAY" > "One terrifying event, then it's done"

  🟢 Chronic cortisol → neural damage (McEwen 1998, 2007)
  🟢 Cortisol → hippocampus neurotoxicity (Sapolsky)
  🟢 Cortisol → PFC dendrite retraction (Arnsten 2009)
  🟡 "Duration > intensity" = framework emphasis, supported by research
```

---

## §3 — 3 MECHANISM SOURCES: Physical / Social / Anticipation

```
⭐ SAME OUTPUT CORTISOL — DIFFERENT ACTIVATION MECHANISMS, DIFFERENT RECOVERY

  §3 = MECHANISM taxonomy: "HOW does the body respond?"
  §4 = ORIGIN taxonomy: "WHERE does the threat come from?"
  2 taxonomies are ORTHOGONAL — they complement each other, do not overlap.
  A single threat event can map onto BOTH axes:
    → Parent shouts "if you don't study you'll get punished" (Imposed origin)
      → triggers Social mechanism (shouting) + Anticipation mechanism
          (imagining the punishment)


═══════════════════════════════════════════════════════
① PHYSICAL — Pain / Physical Danger
═══════════════════════════════════════════════════════

  Trigger: Nociceptors (pain) or sensory detection of danger
  Timeline: 50ms reflex (spinal cord) → 200ms brain → 500ms NE → 5-20min cortisol

  CHARACTERISTICS:
    → HAS REFLEX (spinal cord → hand withdraws BEFORE brain knows)
    → HAS ENDORPHIN buffer (natural pain relief after a few minutes)
    → Duration SHORT (threat passes → cortisol drops quickly)
    → Recovery FAST
    → Present in all species ✅

  → Body DESIGNED for this type. Low cost if acute.
  → Modern life: RARE (few tigers, less direct warfare)

  🟢 Nociception, reflex arc, endorphin system = neuroscience verified


═══════════════════════════════════════════════════════
② SOCIAL — Being Yelled At / Rejected / Losing Status
═══════════════════════════════════════════════════════

  Trigger: Auditory/visual input → schema decodes "social danger"
  Timeline: 200ms decode → 500ms amygdala + schema → 1-2s NE → 5-20min cortisol

  CHARACTERISTICS:
    → NO reflex buffer (must be processed by the brain)
    → NO endorphin buffer (no physical pain trigger)
    → Oxytocin DECREASES (connection threatened)
    → Serotonin MAY DECREASE (status threatened)
    → Duration LONGER than physical
    → Recovery SLOWER (no natural painkiller for social pain)
    → Only social species have this (primates, humans) ✅

  ⭐ PHYSICAL PAIN vs EMOTIONAL PAIN:

    PHYSICAL PAIN:
      Reflex ✅ + Endorphin ✅ + Usually SHORT ✅
      → Fast recovery

    EMOTIONAL PAIN (social):
      Reflex ❌ + Endorphin ❌ + Can be PROLONGED ❌
      → SLOW recovery

    → IRONY: hitting (physical) has endorphin buffer → faster recovery
    → Chronic yelling and scolding (social) has no buffer → DEEPER damage
    → ⚠️ NOT suggesting hitting is acceptable — rather: "chronic emotional
        scolding IS ALSO violence"

  🟢 Eisenberger et al. 2003: social rejection activates the SAME brain regions
     as physical pain (dACC + Insula) — social pain = REAL PAIN
  🟢 Social pain lacks opioid buffering → longer recovery


═══════════════════════════════════════════════════════
③ ANTICIPATION — Imagining Future Consequences
═══════════════════════════════════════════════════════

  Trigger: PFC or schema predicts "if I don't do X → Y will happen (bad)"
  Timeline: schema fires 0ms → PFC drafts 500ms → body simulates → mild cortisol

  CHARACTERISTICS:
    → Threat HAS NOT HAPPENED (only IMAGINED)
    → Mild cortisol each time — but REPEATING → accumulates
    → PFC can LOOP indefinitely (imagine → stress → imagine again)
    → = PRIMARY SOURCE OF MODERN ANXIETY
    → Only species with strong PFC (primarily humans) ✅

  ⭐ ANTICIPATION LOOP (anxiety mechanism):

    ┌──────────────────────────────────────┐
    │ PFC imagines: "if this isn't done?" │
    │           ↓                          │
    │ Body: mild cortisol → "worried"      │
    │           ↓                          │
    │ PFC detects "worried": "yes, danger!"│
    │           ↓                          │
    │ PFC imagines more: "if I fail..."   │
    │           ↓                          │
    │ Body: more cortisol → "more worried" │
    │           ↓                          │
    │ PFC: "AND IT COULD GET EVEN WORSE…"  │
    │           ↓                          │
    │         LOOP ↻                       │
    └──────────────────────────────────────┘

    → SELF-AMPLIFYING: worried → imagine threat → more worried → more imagination
    → DOES NOT STOP ON ITS OWN (no body satisfaction to fire)
    → Stops only when: PFC depleted / external interrupt /
      threat resolved / new schema overrides

    → Anxiety = Anticipation loop that is NOT BROKEN
    → Depression = loop + body EXHAUSTED (cortisol exhaustion)

  ⭐ WHY ANTICIPATION DOMINATES IN MODERN LIFE:

    ① Infinite anticipation chains:
      "Don't study hard → won't get into a good university → won't get a good job
       → won't have money → won't have a home → children will suffer → ..."
      → Chain HAS NO END. PFC imagines threat INFINITELY.

    ② Social media = social threat 24/7:
      → Before: compared to 50 people in the village
      → Now: compared to 1 BILLION people on the internet
      → Status aspiration gap = ALWAYS HIGH

    ③ Always-on culture:
      → 50 notifications/day = 50 micro-threat spikes
      → No single spike BIG ENOUGH to notice — but they ACCUMULATE

    ④ Threat-drive across generations:
      → Parents worry → pressure children → children worry → pressure grandchildren → ...
      → Schema transmitted, not genes

  → RESULT: most modern people are driven by Threat MOST OF THE TIME
  → NOT a personal weakness — the ENVIRONMENT continuously generates threat

  🟡 Body does not distinguish imagined vs real = framework claim
  🟢 Nocebo effect + stress to imagined threat = verified
  🟢 Anticipatory anxiety → cortisol = Gaab et al. 2005
  🟢 CBT targets anticipation loop = established effectiveness


SUMMARY OF 3 SOURCES:

  ┌──────────────────┬──────────────┬──────────────┬──────────────────┐
  │                  │ PHYSICAL     │ SOCIAL       │ ANTICIPATION     │
  ├──────────────────┼──────────────┼──────────────┼──────────────────┤
  │ Speed            │ 50ms reflex  │ 200ms decode │ 500ms+ imagined  │
  │ Endorphin buffer │ PRESENT      │ ABSENT       │ ABSENT           │
  │ Natural duration │ Short        │ Moderate     │ CAN BE INFINITE  │
  │ Recovery         │ Fast         │ Slow         │ Needs loop-break │
  │ Modern frequency │ Low          │ High         │ VERY HIGH        │
  │ Species          │ All species  │ Social species│ Primarily humans │
  └──────────────────┴──────────────┴──────────────┴──────────────────┘


EVALUATIVE/DIRECT-STATE × THREAT (Dissonance-Signal-Architecture.md v1.0 §1):

  3 MECHANISM SOURCES MAP ONTO 2 TYPES OF DISSONANCE:

    ① Physical threat ≈ DIRECT-STATE DISSONANCE territory:
      → Nociception, hardware pathways, endorphin buffer
      → Body can handle from birth, minimal PFC
      → Numbness-proof: Direct-State still fires even when Evaluative is numb

    ② Social threat ≈ EVALUATIVE DISSONANCE territory:
      → dACC + anterior insula (Eisenberger 2003), NO endorphin
      → Compiled chunks required (social schema ≠ reality)
      → PFC can modulate (reframe → decreases, nocebo → increases)

    ③ Anticipation threat ≈ EVALUATIVE DISSONANCE territory:
      → Simulation-Engine generates dissonance WITHOUT external input
      → CRH → amygdala, PFC loop, cortisol accumulates
      → Direct-State CANNOT create anticipation (hardware = NOW only)

  → Physical: SHORT + has buffer. Social/Anticipation: LONG + no buffer.
  → Dissonance-Signal-Architecture explains: Direct-State has endorphin;
      Evaluative does NOT.


THREAT × NEW CONCEPTS (28-session Drill Propagation):

  SIMULATION-ENGINE × THREAT (Simulation-Engine.md v1.0):
    → Anticipation (③ above) = Simulation-Engine drafts outcome → body evaluates
        as THREAT
    → Imagine-Final v3.0 KEY BOUNDARY: hardware prediction (automatic) ≠ Imagine-Final
    → Simulated threat = Simulation-Engine running a threat scenario
    → PFC budget: prolonged simulation COSTS processing capacity
    → = Anticipation loop = Simulation-Engine STUCK on a threat scenario

  ENTITY-ACCESS × THREAT (Entity-Access.md v1.2):
    → Threat FROM entities = function of Entity-Access gradient:
      Level 5 (child/self) threat = EXTREMELY STRONG (hardware-subsidy amplifies)
      Level 3 (close friend) threat = STRONG
      Level 1 (acquaintance) threat = MUCH MILDER
    → LOSING access = threat direction (Entity-Access-Excess.md v1.0)
    → Threat of access DROP = common anticipation source

  BOND-ARCHITECTURE × THREAT (Bond-Architecture.md v2.0):
    → Threat TO bond = protect response (Protect.md)
    → 4 bond types → 4 threat profiles:
      Proximity bond threat: physical separation (LOSING safe territory)
      Shared-Experience threat: divergent paths (GROWING APART)
      Reciprocal threat: imbalance (GIVING more than RECEIVING)
      Identity threat: values clash (BEING CHANGED against your nature)
    → Bond type determines WHAT COUNTS as threat — same event, different bond,
        different threat

  🟡 Simulation-Engine × threat = framework formalization
  🟡 Entity-Access × threat = framework application (consistent with attachment theory)
  🟡 Bond-Architecture × threat = framework taxonomy (novel)
```

---

## §4 — 3 ORIGIN SOURCES: Domain / Peer / Imposed

```
⭐ §4 = ORIGIN taxonomy: "WHERE does the threat come from in the environment?"
  Helps understand INTERVENTION + PREVENTION
  (different from §3, which helps understand BIOLOGY + RECOVERY)

  Both taxonomies need to be used TOGETHER:
    → Understanding mechanism (§3) → know how to recover
    → Understanding origin (§4) → know whether to let the threat fire or prevent it


═══════════════════════════════════════════════════════
① DOMAIN THREATS (from physical reality)
═══════════════════════════════════════════════════════

  DEFINITION: Threats from physical reality itself — no one created them.

  Examples:
    → Bicycle chain breaks → needs fixing
    → Unexpected rain → find shelter
    → Light goes out while reading → fix the light
    → Shoe breaks → repair or replace

  CHARACTERISTICS:
    → Real, body-confirmable
    → Scale usually small — everyday mini-dissonance
    → Temporary — solvable, then it ends
    → Agency-supporting — most are solvable by the person themselves

  VALUE:
    → Each solve = mini-opioid + new chunk
    → Builds competence chunks ("I CAN fix problems")
    → Calibrates realistic expectations about uncertainty

  Example — Child encounters domain threat:
    Reaction A (oversheltering): parents immediately fix it
    → Child doesn't face dissonance → no new chunks → lacks resilience

    Reaction B (trusting the child): "Your pen ran out — what do you think you can do?"
    → BUILD phase → solve → opioid → "I encounter a problem → I can solve it"

  → ACTION: KEEP — do not eliminate. Preserve age-appropriate exposure.


═══════════════════════════════════════════════════════
② PEER SOCIAL THREATS (from the horizontal social system)
═══════════════════════════════════════════════════════

  DEFINITION: Threats from social dynamics among peers (friends, colleagues).

  Examples:
    → Being lightly teased by friends
    → Competing over toys
    → Argument with a close friend
    → Negative feedback from a colleague

  CHARACTERISTICS:
    → Symmetric power — neither side has absolute authority
    → Complex — many factors, no single correct answer
    → Negotiable — outcomes shaped by participant skill

  VALUE:
    → Core training for social navigation
    → Teaches empathy, conflict resolution, social reading
    → Builds chunks about human behavior from direct experience

  LIMITS:
    → Mild-to-moderate peer threats = KEEP (training opportunity)
    → BULLYING (chronic + severe + asymmetric power) = INTERVENE
    → Distinction: "conflict resolvable with skill" vs "victim has no power"

  → ACTION: KEEP + MONITOR. Intervene when there is chronic asymmetric harm.


═══════════════════════════════════════════════════════
③ IMPOSED ADULT THREATS (from authority above)
═══════════════════════════════════════════════════════

  DEFINITION: Threats actively CREATED by authority figures (parents, teachers,
  bosses) to control behavior. Artificial pressure from a position of power.

  Examples:
    → "If you don't study I'll punish you"
    → "Look at how well your friend is doing" (comparison-shame)
    → "If you don't get into a good university, your life is ruined"
    → Boss: "If you don't work overtime → no promotion"

  CHARACTERISTICS:
    → Artificial — created by authority
    → Asymmetric power — the person being threatened has no real choice
    → Often chronic — authority repeats indefinitely
    → Often internalized — compiles into schema → fires on its own
        when authority is absent
    → MOST DAMAGING when authority = the connection source (parents)
      → Connection source = threat source → DEEP CONFLICT
      → = Insecure attachment mechanism

  ⭐ IMPOSED SPECTRUM — FROM TOXIC TO REASONABLE:

    ❌❌ TOXIC: "You're so stupid! Look at your friend!" / hitting / shaming
      → Physical + Social + Anticipation mechanisms fire ALL 3
      → Schema compiles: "studying = pain", "authority = dangerous"
      → Long-term: trauma, background anxiety, hating learning for life

    ❌ SHAME-BASED: "Others will laugh at you if you don't study"
      → Social mechanism. Schema: "studying = avoiding shame"
      → Dependent on external validation

    ⚠️ REASONABLE (an acceptable bridge): "Finish the homework before playing games"
      → Mild anticipation. Schema: "effort → reward"
      → Technically imposed but mild + explained + fair

    ✅ NOVELTY PATH (ideal): "This is really interesting, want to try it?"
      → NOT a threat — this is Novelty pull
      → Schema: "knowledge = a TOOL that expands your world"
      → Intrinsic motivation

    SPECTRUM:
    BAD ←──────────────────────────────────────────────────→ GOOD
    Toxic    Shame    Reasonable    Reward-based    Novelty path
    PUSH ←─────────────────────────────────────────────────→ PULL

  → ACTION: REDUCE gradually. Replace with reasonable → novelty path.


⭐ MATRIX: ORIGIN × MECHANISM (both taxonomies combined)

  ┌────────────────┬──────────────┬──────────────┬──────────────────┐
  │                │ PHYSICAL     │ SOCIAL       │ ANTICIPATION     │
  ├────────────────┼──────────────┼──────────────┼──────────────────┤
  │ DOMAIN         │ Fall from    │ (rare)       │ "Code crash →    │
  │ (reality)      │ bike, burn,  │              │ boss will be     │
  │                │ cut          │              │ angry"           │
  ├────────────────┼──────────────┼──────────────┼──────────────────┤
  │ PEER SOCIAL    │ (uncommon)   │ Friend teases,│ "Friend won't   │
  │ (equal power)  │              │ argument     │ play with me"    │
  ├────────────────┼──────────────┼──────────────┼──────────────────┤
  │ IMPOSED ADULT  │ Physical     │ Yelling,     │ "Don't study →  │
  │ (authority)    │ punishment   │ shame,       │ future collapses"│
  │                │              │ comparison   │                  │
  └────────────────┴──────────────┴──────────────┴──────────────────┘

  → Imposed threats can fire ALL 3 mechanisms → highest destructive power

  KEY GUIDANCE: KEEP / KEEP / REDUCE
    ┌────────────────┬──────────┬────────────┬──────────────────┐
    │                │ DOMAIN   │ PEER SOCIAL│ IMPOSED ADULT    │
    ├────────────────┼──────────┼────────────┼──────────────────┤
    │ Body-confirmed │ Yes      │ Yes, messy │ No (artificial)  │
    │ Agency         │ High     │ Medium     │ Low              │
    │ Long-term value│ High     │ High       │ Low (chronic)    │
    │ Action         │ KEEP     │ KEEP +     │ REDUCE gradually │
    │                │ + enable │ monitor    │ (transition)     │
    └────────────────┴──────────┴────────────┴──────────────────┘

  → "Eliminate all threat" = wrong target
  → "Right type at right dose" = correct target

  🟡 Origin taxonomy = framework formulation
  🟢 Social rejection damage (Eisenberger 2003)
  🟢 Authority-based shame most damaging (Slavich 2010)
  🟢 Authoritative parenting research (Baumrind 1967)
```

---

## §5 — THREAT × IMAGINE-FINAL: 3 CASES

```
⭐ THREAT + IMAGINE-FINAL INTERACT → THE MOST COMPLEX PATTERNS

  Cross-ref: Imagine-Final-Evaluation.md (2 axes × 4 angles)
  Cross-ref: Anchor-Schema.md (Trust binding)

  STRUCTURE:
    → Imagine-Final ALIGNED + Threat = PRODUCTIVE
    → Imagine-Final MISALIGNED + Threat = DESTRUCTIVE
    → NO Imagine-Final + Threat = LOST


═══════════════════════════════════════════════════════
CASE 1: Imagine-Final ALIGNED + Threat = PRODUCTIVE
═══════════════════════════════════════════════════════

  = "Know what I want + know the risk of not doing it"
  = Threat PUSH + Imagine-Final PULL = 2 forces in THE SAME DIRECTION

  → Each step forward → closer to Imagine-Final → body-feedback reward
  → Threat DECREASES GRADUALLY with progress
  → = Self-resolving: progress → reward + threat decreases → sustainable

  Example: young doctor, Imagine-Final "save lives" (matches hardware)
    + Threat "if I don't study → patients suffer consequences"
    → Drive: study intensely → each successful case → reward + threat decreases


═══════════════════════════════════════════════════════
CASE 2: Imagine-Final MISALIGNED + Threat = DESTRUCTIVE SPIRAL
═══════════════════════════════════════════════════════

  = "Think I want X — but hardware/domain ≠ X"
  ⚠️ THE MOST DANGEROUS PATTERN — very common, very hard to recognize

  4 PHASES:

    PHASE 1 — STRONG DRIVE (months 1-6):
      → Misalignment not yet known → threat + novelty both pulling → "enthusiasm"
      → LOOKS LIKE Case 1 — hard to distinguish

    PHASE 2 — DISSONANCE ACCUMULATES (months 6-18):
      → Body-feedback reward LESS than expected (wrong direction)
      → Dissonance rises + reward falls = gap WIDENING

    PHASE 3 — TIPPING POINT (month 18+):
      → Accumulated dissonance > Imagine-Final pull
      → Body: "should stop" — BUT threat still pushing: "if I stop → failure"
      → = STUCK: wants to stop + afraid to stop → classic burnout precursor

    PHASE 4 — COLLAPSE OR CHRONIC:
      → Path A (fortunate): collapse → pain → recognizes misalignment → rebuilds
      → Path B (unfortunate): threat overrides → continues → chronic → health issues

  ⭐ TIPPING POINT — concept to formalize:

    Imagine-Final pull ────────────
                        ╲
                         ╲  ← positive drive (continue)
                          ╲
    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╳─ ─ ─ ─ TIPPING POINT
                          ╱
                         ╱  ← negative drive (should stop)
                        ╱
    Accumulated dissonance ────────────
                                        → time

    Before tipping: continue. After tipping: SHOULD STOP.
    If threat overrides → chronic → burnout path.


═══════════════════════════════════════════════════════
CASE 3: NO Imagine-Final + Threat = LOST
═══════════════════════════════════════════════════════

  = "Don't know what I want, but know I MUST DO SOMETHING"
  = Threat PUSHING but NO direction

  → High anxiety + low direction = FREEZE or SCATTER
  → Example: graduating student "must choose a career" + "don't know what I like"
  → Example: job loss + "don't know what I want to do"

  Why this is common:
    → Education system forces choice EARLY (not enough chunks yet)
    → Threat-based parenting: "must be like this" but no guidance on "what do you want?"
    → = Person KNOWS HOW TO FEAR but DOES NOT KNOW HOW TO WANT

  🟡 3 Cases = framework analysis
  🟢 Burnout phases (Maslach)
  🟢 Cognitive dissonance → physiological response = established
```

---

## §6 — WHEN ADAPTIVE vs WHEN HARMFUL

```
⭐ THREAT = NEUTRAL — a mechanism, not a disease


WHEN ADAPTIVE:

  ① EMERGENCY RESPONSE — life-saving (acute, bounded)
  ② DEADLINE MOTIVATION — Yerkes-Dodson sweet spot (mild, has endpoint)
  ③ BOUNDARY DEFENSE — protecting values (assertive behavior)
  ④ GROWTH CATALYST — Threat + aligned Imagine-Final = productive drive (Case 1)
  ⑤ INVESTMENT BRIDGE — threat holds through the phase "not enough chunks yet"
    → When chunks SUFFICIENT → intrinsic reward takes over → LOWER the threat floor

  FAVORABLE CONDITIONS:
    ✅ Specific (not abstractly infinite)
    ✅ Has a clear endpoint
    ✅ Has an action that resolves it
    ✅ Short-term or can be switched off
    ✅ Cortisol just enough


WHEN HARMFUL:

  ① CHRONIC — prolonged without resolution → Neural Wear
  ② ABSTRACT — no specific target → energy mobilized but unused → damage
  ③ SELF-AMPLIFYING — anticipation loop (§3 ③)
  ④ OVERRIDES BODY WARNINGS — forces continuation when body says "stop"
      → burnout
  ⑤ EXPLOITATIVE — threat deliberately created to control behavior
    → Guilt-based parenting, FOMO, political fear

  ⭐ THREAT-DRIVE IN EVERYDAY LIFE:

    PULL drives (novelty, connection, experience):
      → "Want to" → enjoy the process → sustainable

    PUSH drive (threat):
      → "Have to" → endure the process → costs cortisol → not sustainable

    Same behavior (going to work, studying, exercising) → different drive →
    different sustainability:
      → Study because it's interesting (novelty pull) = schema "studying = engaging"
      → Study because scared (threat push) = schema "studying = stress"
      → = Same behavior → DIFFERENT drive → DIFFERENT schema compiled
          → DIFFERENT LIFE TRAJECTORY


SUMMARY:

  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │  THREAT + acute + bounded + resolvable = ADAPTIVE          │
  │  = Emergency, deadline, growth, boundary defense           │
  │                                                            │
  │  THREAT + chronic + unbounded + no resolution = HARMFUL    │
  │  = Neural Wear, anxiety, burnout, override, exploitation   │
  │                                                            │
  │  → KEY VARIABLE: DURATION + RESOLUTION                     │
  │  → "Can be stopped" = healthy | "Cannot be stopped" = toxic│
  │                                                            │
  └────────────────────────────────────────────────────────────┘

  🟡 Classification = framework analysis
  🟢 Chronic stress → harm = extensive research
  🟢 Yerkes-Dodson = established
  🟢 CBT targets anticipation = established effectiveness
```

---

## §7 — HONEST ASSESSMENT

```
  FULL FILE — HONEST EVALUATION:

  🟢 VERIFIED (neuroscience / established research):
    ┌────────────────────────────────────────────────────────────┐
    │ NE → adrenaline → cortisol cascade (stress physiology)    │
    │ Fight/flight/freeze responses (LeDoux, Cannon)             │
    │ Amygdala overrides PFC at high stress (Arnsten 2009)       │
    │ Yerkes-Dodson law (1908, replicated)                        │
    │ Chronic cortisol → neural damage (McEwen 1998, 2007)       │
    │ Cortisol → PFC dendrite retraction (Arnsten)               │
    │ Cortisol → hippocampus neurotoxicity (Sapolsky)            │
    │ Chronic stress → immune suppression                         │
    │ Social rejection = physical pain regions (Eisenberger 2003)│
    │ Social pain lacks opioid buffer                             │
    │ Authority shame most damaging (Slavich 2010)                │
    │ Anticipatory anxiety → cortisol (Gaab 2005)                │
    │ Vagal syncope mechanism (documented)                        │
    │ Burnout phases (Maslach)                                    │
    │ Authoritative parenting (Baumrind 1967)                     │
    │ CBT effectiveness for anxiety                               │
    │ Knowledge reduces anxiety (health literacy research)        │
    └────────────────────────────────────────────────────────────┘

  🟡 FRAMEWORK SYNTHESIS (consistent logic, derived from 🟢):
    ┌────────────────────────────────────────────────────────────┐
    │ Threat = observation parameter (not a component)           │
    │ 2 components (body-feedback + prediction of harm)          │
    │ Schema = trigger, hormone = sustain                        │
    │ 5-level intensity spectrum                                  │
    │ Duration > intensity for long-term damage                   │
    │ 3 mechanism sources (Physical/Social/Anticipation)         │
    │ 3 origin sources (Domain/Peer/Imposed)                     │
    │ Origin × Mechanism matrix                                   │
    │ KEEP/KEEP/REDUCE guidance                                   │
    │ Anticipation loop = anxiety mechanism                       │
    │ Modern anxiety paradox (safe but anxious)                  │
    │ Threat × Imagine-Final 3 Cases                              │
    │ Tipping point model                                         │
    │ Pull vs Push sustainability difference                      │
    │ Compilable Architecture → threat type expansion (v1.1)     │
    │ Compiled/Fresh threat (phobia vs novel danger) (v1.1)      │
    │ PFC=Lawyer: suppress/amplify/fabricate threat (v1.1)       │
    └────────────────────────────────────────────────────────────┘

  🔴 HYPOTHESIS (logical but unverified):
    ┌────────────────────────────────────────────────────────────┐
    │ % body resource per intensity level — approximation        │
    │ Exact tipping point measurement — undefined                │
    │ Optimal threat:novelty ratio — unknown                     │
    │ Imposed→internalized timeline per individual — variable    │
    │ Cross-generation threat transmission mechanics — unclear   │
    └────────────────────────────────────────────────────────────┘
```

---

## §8 — CROSS-REFERENCES

```
  ← FOUNDATION (read first or alongside):
    Core-v7.8-Draft.md §8 — Threat = observation parameter definition
    Body-Feedback-Mechanism.md v2.0 §3.1-§3.2 — Chunk-Shift/Miss = Threat substrate
    Cortisol-Baseline.md v2.0 — amplifier, chronic vs acute dynamics
    Chunk.md v2.0 — chunk compilation under emotional peak
    Inter-Body-Mechanism.md v1.0 §1.2 — Compilable Architecture (threat type expansion)
    Inter-Body-Mechanism.md v1.0 §3 — Compiled/Fresh (compiled threat vs fresh threat)
    Inter-Body-Mechanism.md v1.0 §7 — PFC=Lawyer (suppress/amplify/fabricate threat)
    PFC-Configuration.md v1.0 — Strategy A→config④, Strategy B→config⑤ (2026-05-10)

  ← NEW MECHANISM (28-session Drill):
    Simulation-Engine.md v1.0 — simulated threat = Simulation-Engine draft outcome
    Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State × 3 mechanism
        sources mapping
    Entity-Access.md v1.2 — threat FROM entities along gradient
    Bond-Architecture.md v2.0 — threat to bond → protect response (4 types)
    Imagine-Final.md v3.0 — hardware prediction ≠ Imagine-Final boundary

  ↔ PARALLEL (same Observation/ folder):
    Observation/Novelty.md v1.2 — PULL toward opportunity (parallel to Threat PUSH)
    Observation/Drive.md v1.2 — HOW Threat + Novelty + other patterns → action
    Observation/Empathy.md v4.0 — Self-Pattern-Modeling detects threat in others
    Observation/Liking-Wanting.md — Wanting under threat conditions

  → DOWNSTREAM:
    Imagine-Final-Evaluation.md — 2 axes × 4 angles (§5 3 Cases reference)
    Anchor-Schema.md — Trust binding, negative trust from threat
    Feeling.md v3.0 — PFC observation of threat signals (worried, scared, panic)
    Valence-Propagation.md v3.0 — threat valence propagation, 3 firing modes
    Body-Feedback-Label.md v2.0 — vocabulary reference

  → APPLICATIONS:
    Domain-Mapping-Drive.md — 3 threat types + transition reality
    AI-Schema-Detection.md — detect threat patterns in clients

  STATUS:
    v1.0 — 2026-04-20 — written fresh for v7.8 cycle-based architecture
    v1.1 — 2026-05-17 — +Compilable Architecture, +Compiled/Fresh, +PFC=Lawyer,
        version sync
    v1.2 — 2026-05-23 — Concept Cascade: +Simulation-Engine, +Entity-Access gradient,
        +Bond-Architecture 4 bond types, version updates
    v1.3 — 2026-05-25 — §3 +Evaluative/Direct-State × 3 mechanism sources mapping
        (Dissonance-Signal-Architecture v1.0)
    Merged from: Threat.md v1.1-old + Threat-Drive-Analysis.md
        (backup: _backup/Drive-v75-era/)
    Aligned: Core v7.8, Inter-Body-Mechanism v1.0, prediction-delta terminology
```
