---
title: PFC-Hardware — Individual Hardware Parameters
version: 1.1
created: 2026-04-19
updated: 2026-05-10 (v1.1 — §3.4-§3.5 COMT×Reward, §4.7-§4.8 DRD4×Reward+COMT×DRD4, §8b-§8c Receptor×Profiles+Shorthand)
status: REFERENCE v1.1
scope: |
  Hardware parameters that differentiate PFC performance between individuals.
  Focus: COMT, DRD4, NE receptors, Capacity/Quality.
  Same 24 functions (PFC-Function.md) but DIFFERENT hardware → DIFFERENT output.
supersedes: |
  PFC/Imagination/backup/PFC-Analysis-v1.1.md §8 (2026-03-15, ~985L)
  Insights integrated, framing updated to v7.8 cycle-based.
related: |
  PFC-Function.md — 24 functions PFC performs
  PFC-Development.md — PFC across life stages + training
  PFC-Hold-Dimensions.md — Why ~4±1 dimensions
  Neural-Architecture.md §2 — Physical PFC sub-regions
  Cortisol-Baseline.md v2.0 — Cortisol affects PFC function
  Core-Software.md §6 — PFC in overall cycle architecture
language: English primary + technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# PFC Hardware — Why Same 24 Functions Produce Different Output

> **Same 24 functions (PFC-Function.md), same ~4±1 slots (Hold).**
> **Different HARDWARE → different OUTPUT.**
>
> Hardware = WHAT DOESN'T CHANGE (or changes extremely slowly).
> Training = WHAT CAN CHANGE (PFC-Development.md).
>
> This file answers: why do 2 people with the same experience, the same chunks,
> one "gets bored fast" while the other "goes deeper"?
> Different hardware — not different "willpower."

---

## TABLE OF CONTENTS

- §1 — 2 Main Hardware Properties
- §2 — Observed Capacity ≠ Hardware Ceiling
- §3 — COMT: Clear Speed (Improviser vs Specialist)
- §4 — DRD4: Chunk Threshold (Data, Logical Gaps, Hypothesis D)
- §5 — MAO-A: Mood Stability (Whole Brain)
- §6 — NE α2/α1: PFC Circuit Breaker
- §7 — VTA Detection Loop (7 Steps)
- §8 — 4 Receptor Systems Summary
- §9 — Honest Assessment
- §10 — Cross-References

---

## §1 — 2 Main Hardware Properties

```
⚠️ NOTE: Capacity and Clear Speed are MEASURABLE PHENOMENA
   (clearly observable across individuals, measurable).
   Research (COMT, DRD4,...) = best current candidates
   to explain the mechanism — likely maps correctly,
   not yet definitively confirmed. Framework uses these
   at this confidence level.

  ┌─────────────┬──────────────────────────────┬──────────────────┐
  │             │ ① PFC-QUALITY                │ ② CLEAR SPEED    │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ What it is  │ WORKSPACE QUALITY:           │ Speed of         │
  │             │ Everyone holds ~4±1 slots.   │ clearing old     │
  │             │ (Interference limit = physics,│ drafts to make  │
  │             │ NOT a shortage of neurons.)  │ room for new     │
  │             │ Quality does NOT affect the  │ ones.            │
  │             │ NUMBER of slots — it affects │                  │
  │             │ PROCESSING QUALITY PER-SLOT: │                  │
  │             │ ① Resolution: sharp or blurry│                  │
  │             │ ② Noise filter: maintains    │                  │
  │             │    clarity under noise vs.   │                  │
  │             │    easily disrupted          │                  │
  │             │ ③ Retrieval: pulls chunks    │                  │
  │             │    from B fast/accurately    │                  │
  │             │    or slow/incorrectly       │                  │
  │             │ ④ Compression: compiles      │                  │
  │             │    chunks densely → each     │                  │
  │             │    slot holds MORE           │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ Hardware    │ PFC connection density +     │ COMT variant     │
  │             │ wiring quality (NOT number   │ (PFC-specific    │
  │             │ of neurons — 10B vs 12B      │ enzyme)          │
  │             │ still ~4±1 slots, but        │                  │
  │             │ per-slot quality DIFFERS)    │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ HIGH =      │ 4±1 slots × high resolution  │ Clears fast      │
  │             │ × clean × fast retrieve      │ → workspace      │
  │             │ × deep compression           │ FREED quickly    │
  │             │ = "Looking at 4 things and   │ → fresh rebuild  │
  │             │ SEEING the whole universe"   │                  │
  │             │ (expert)                     │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ LOW =       │ 4±1 slots × low resolution   │ Clears slow      │
  │             │ × noisy × slow retrieve      │ → draft HOLDS    │
  │             │ × shallow compression        │ LONG →           │
  │             │ = "Looking at 4 things and   │ incremental      │
  │             │ only SEEING 4 things"        │ modify           │
  │             │ (novice)                     │                  │
  ├─────────────┼──────────────────────────────┼──────────────────┤
  │ Affects     │ BOTH improviser AND          │ PRIMARY driver   │
  │             │ specialist benefit from      │ of Improviser    │
  │             │ high quality                 │ vs Specialist    │
  │             │                              │ tendency         │
  └─────────────┴──────────────────────────────┴──────────────────┘

  ⚠️ IMPORTANT: "4±1 slots" = FIXED by physics (interference limit)
     10B vs 20B PFC neurons → STILL ~4±1 slots
     → Evolution solved this with: compile → stack → pyramidal
     → NOT a bigger PFC → better quality compilation
     → Detail: PFC-Hold-Dimensions.md

  2 INDEPENDENT properties → create MANY profiles:
    High quality + Fast clear = "improviser with depth"
    High quality + Slow clear = "specialist with breadth"
    Low quality + Fast clear  = "jumps around, stays shallow"
    Low quality + Slow clear  = "slow and narrow"
```

🟢 Evidence: Cowan 2001 (~4±1), Bays & Husain 2008 (interference = precision drop),
Kane & Engle 2002 (WM capacity = noise filter), Chase & Simon 1973 (expert = compression quality)

---

## §2 — Observed Capacity ≠ Hardware Ceiling

```
🟡 "PFC strong/weak" = VAGUE. Observed Capacity is EMERGENT from 4 factors:

  OBSERVED CAPACITY = Hardware Ceiling × Chunks Quality × Cortisol State × Context Fit

  ① Hardware Ceiling (genetics — changes EXTREMELY SLOWLY):
     → Connection density, wiring quality → sets RANGE
     → HARDEST to measure + LEAST amenable to intervention
     → 🟢 Neural efficiency: skilled individuals fire LESS, NOT more
        (Haier 1992, Neubauer & Fink 2009) → efficiency > capacity
     → 🟢 Brain size vs IQ: very weak correlation (~0.24, ~6% variance)
        (Pietschnig 2015, meta-analysis of 148 studies)

  ② Chunks Quality (education + experience — changes over YEARS):
     → Chunks compiled DEEPLY + ORGANIZED WELL → fast, accurate retrieval
     → Rich chunks → PFC has RAW MATERIAL → rich output
     → Sparse chunks → PFC drafts in a vacuum → poor output even with strong PFC
     → Pyramidal compression (4×4×4) ONLY works when chunks ALREADY COMPILED
     → = "Strong PFC + empty B areas = a good workshop with no raw material"
     → ACTIONABLE: education + experience + compile time (sufficient sleep)

  ③ Cortisol State (mode — changes over HOURS):
     → Low cortisol → PFC clean, good filter, accurate retrieval
     → High cortisol → PFC noisy, weak filter, slow/inaccurate retrieval
     → SAME hardware + SAME chunks + DIFFERENT cortisol = DIFFERENT output
     → = "Think clearly in the morning, draw a blank in the evening" = same PFC
     → ACTIONABLE: sleep, reduce stress, body care

  ④ Context Fit (domain match — changes when ENVIRONMENT changes):
     → Chunks MATCH current domain → PFC retrieves INSTANTLY → "fast"
     → Chunks DON'T match → PFC must build fresh → "slow" even with strong PFC
     → = Expert changing fields → "slow" even though IQ unchanged
     → ≈ NOT directly actionable — only accumulate new experience

  → IQ tests measure TOTAL ①②③④ TOGETHER → cannot isolate ① alone
  → "Don't need a better PFC — need to USE the current PFC BETTER"
     via: rich chunks (②) + low cortisol (③) + context match (④)

  Intervention focus: ②③ (education + cortisol management)
  since ① doesn't change + ④ is hard to intervene directly
```

---

## §3 — COMT: Clear Speed (Improviser vs Specialist)

```
① COMT (Catechol-O-Methyltransferase)
   🟢 PRIMARY — well-replicated

   COMT = enzyme that breaks down dopamine IN PFC (PFC-specific, not whole-brain)

   Val/Val: enzyme FAST → dopamine clears FAST → PFC flexible, unstable
   Met/Met: enzyme SLOW → dopamine PERSISTS LONGER → PFC stable, less flexible

   🟢 Egan et al. 2001:
     fMRI during WM tasks (Wisconsin Card Sort, N-back)
     Val/Val: PFC more efficient when SWITCHING tasks
     Met/Met: PFC more efficient when MAINTAINING focus
     = 2 strategies, NOT one better than the other. Well-replicated.


SPECIALIST DRAFT MODE — COMT Met/Met (clears SLOW):
  ┌──────────────────────────────────────────────────────┐
  │ Dopamine STAYS LONG in PFC                           │
  │ → Draft is NOT cleared quickly                       │
  │ → WM HOLDS draft → edits ON TOP of old draft        │
  │                                                      │
  │ Process:                                             │
  │   Draft v1: [A]-[B]-[C]-[D]                         │
  │   Edit: remove [C] → write [C'] (connected to A,B,D)│
  │   Draft v2: [A]-[B]-[C']-[D]                        │
  │   → INCREMENTAL modification                        │
  │   → Each new part MUST connect to the remainder     │
  │   → = DIG DEEP in one direction                     │
  │   Strength: precise, consistent, deep               │
  │   Weakness: hard to break from chosen direction     │
  └──────────────────────────────────────────────────────┘

IMPROVISER DRAFT MODE — COMT Val/Val (clears FAST):
  ┌──────────────────────────────────────────────────────┐
  │ Dopamine is CLEARED FAST from PFC                    │
  │ → Draft is "erased" before editing is complete      │
  │ → Workspace EMPTY → ready for a COMPLETELY NEW draft│
  │                                                      │
  │ Process:                                             │
  │   Draft v1: [A]-[B]-[C]-[D]                         │
  │   Clear: [ ]-[ ]-[ ]-[ ] (workspace empty)          │
  │   New input from B+C → new context                  │
  │   Draft v2: [X]-[Y]-[Z]-[W] (COMPLETELY DIFFERENT)  │
  │   → FRESH rebuild from new input                    │
  │   → NOT constrained by old draft                    │
  │   → = JUMP to a completely different direction      │
  │   Strength: cross-domain, creative, unexpected      │
  │   Weakness: lacks depth, inconsistent               │
  └──────────────────────────────────────────────────────┘

  ⭐ KEY INSIGHT:
    Val/Val switches often NOT because they "want" to switch
    → but because the OLD DRAFT IS GONE → FORCED to build fresh
    Met/Met stays NOT because they "don't want" to switch
    → but because OLD DRAFT REMAINS → no room for a new draft
    → = HARDWARE manages the DRAFT, not "willpower" managing behavior

  "Gets bored fast" = DRAFT CLEARS FAST, not a "flaw" or "low reward"
    → ~15-20% of the population has Val/Val hardware → designed for exploration
    → ~60-70% has Met/Met hardware → designed for maintenance
    → BOTH are necessary for society
```


### §3.4 — COMT × Reward Pattern (v1.1 new — Drill R8)

```
🟡 COMT EXTENDED: COGNITION → REWARD

  §3 analyzes COMT for COGNITION (draft management).
  Drill R8 extends: COMT also affects REWARD patterns.

  PFC draft management → reward timing + depth:

  ┌──────────────────────┬──────────────────────────────────────────┐
  │ Val/Val (Improviser) │ Met/Met (Specialist)                      │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ ② MANY shallow       │ ② FEWER but DEEPER insights              │
  │ insights → MANY      │ → FEWER but STRONGER rewards             │
  │ micro-rewards        │                                          │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Afterglow: SHORT     │ Afterglow: LONG                          │
  │ (draft clears →      │ (draft persists → re-derive →            │
  │  next topic)         │  additional opioid pulses)               │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Cross-domain ②:      │ Cross-domain ②: HARDER                   │
  │ NATURAL (workspace   │ (workspace occupied → new domain         │
  │  clears → new domain)│  blocked by existing draft)              │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Flow: HARDER to      │ Flow: EASIER to sustain                  │
  │ sustain (draft clears│ (draft persists → continuous             │
  │ during flow →        │  coherence stream)                       │
  │ interruption)        │                                          │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Compound: MORE VARIED│ Compound: LESS varied but DEEPER         │
  │ (many domains)       │ (same domain = deep stack)               │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ Risk: "dopamine      │ Risk: "stuck in rut"                     │
  │ chasing" — jump to   │ (can't escape domain even when           │
  │ next novelty before  │  diminishing returns)                    │
  │ depth compiles       │                                          │
  └──────────────────────┴──────────────────────────────────────────┘

  Val/Met Heterozygous (~50% population):
    → Context-dependent switching → FLEXIBLE reward pattern.
    → Can flow AND explore depending on state.

  ⭐ KEY INSIGHT:
    "Improviser gets BORED not because reward is LOW — because DRAFT CLEARS
    before depth compiles. Specialist gets STUCK not because curiosity is
    LOW — because draft WON'T CLEAR for new domain."
    → ≠ personality trait → = HARDWARE managing DRAFTS differently

  → Detail: Reward-Signal-Architecture.md §4 (5 Profiles)
  🟡 COMT × Reward extension = inferred from COMT × Cognition, not directly tested.
  Source: Drill §3.22 ❸ (R8).
```


### §3.5 — COMT × Childhood Compilation (v1.1 new — Drill R8)

```
🟡 HARDWARE × CHILDHOOD = 4 REWARD TRAJECTORIES:

  COMT sets RANGE (how fast drafts clear).
  Childhood Precondition-5 tags set DIRECTION (approach vs avoidance).
  Combination → 4 distinct reward life trajectories:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ Combination        │ Reward Life          │ Implication          │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + approach │ DEEP FLOW expert     │ Best case for ②      │
  │ childhood          │ (draft stays +       │ Sustainable decades  │
  │                    │ approach-tagged)      │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + avoidance│ RIGID ANXIETY        │ Draft stuck +        │
  │ childhood          │ (cannot escape +     │ threat-tagged =      │
  │                    │ threat-tagged domain)│ WORST combination    │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + approach │ CREATIVE EXPLORER    │ Breadth + approach   │
  │ childhood          │ (jumps freely +      │ = versatile joy      │
  │                    │ approach-tagged)      │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + avoidance│ SCATTERED ANXIETY    │ Jump + avoid = chaos │
  │ childhood          │ (drafts clear +      │ Nothing feels safe   │
  │                    │ threat-tagged)        │ or deep enough       │
  └────────────────────┴──────────────────────┴──────────────────────┘

  ⭐ SAME hardware, DIFFERENT childhood = COMPLETELY DIFFERENT reward life.
  → Hardware sets RANGE. Childhood sets DIRECTION within range.
  → = "Nature sets the instrument. Nurture plays the tune."

  Implications:
    → Met/Met + avoidance = most urgently needs intervention
      (draft stuck ON threat-tagged chunks → cannot escape anxiety loop)
    → Val/Val + avoidance = chaotic but LESS stuck
      (drafts clear → can encounter new approach-tagged experiences)
    → Approach childhood = protective for BOTH COMT variants
    → Avoidance childhood = damaging for BOTH, worse for Met/Met

  → Detail: Compile-Taxonomy.md §3, Reward-Signal-Architecture.md §8.4
  🟡 COMT × Childhood = framework synthesis, observational consistency.
  Source: Drill §3.22 ❺ (R8).
```

---

## §4 — DRD4: Chunk Threshold

```
③ DRD4 (Dopamine Receptor D4)
   ⚠️ THE FRAMEWORK DOES NOT USE DRD4 AS ITS PRIMARY MECHANISM.
   Documented here for reference and to explain WHY it is not used.


§4.1 DATA (measurable — cannot be disputed) 🟢:

  → DRD4-7R receptor binds dopamine WEAKER than 4R at the molecular level
    (Van Tol et al. 1992 — in vitro, measured) = FACT
  → Individuals carrying DRD4-7R TEND to score higher on Novelty Seeking
    (Ebstein 1996 + several subsequent studies) = OBSERVATION
    (though effect size is small ~10% and replication is not fully consistent)


§4.2 OLD INTERPRETATION (has logical gaps — framework does NOT use) ❌:

  Common narrative:
    "7R less sensitive → less pleasant → must seek more novelty to compensate"

  LOGICAL GAPS:
    If 7R receptor is less dopamine-sensitive:
      → Novelty ALSO gives LESS reward (novelty uses the same dopamine system)
      → Encountering difficulty in a new domain → LESS reward → should give up SOONER?
      → Switching domains requires BUILDING a foundation → LARGE effort, SMALL reward
        → why endure it?
    If 4R receptor is more sensitive:
      → Novelty gives MORE reward → why NOT switch constantly?
      → Scrolling social media = more pleasant → should be MORE addicted?
    → Logic "less sensitive → seek MORE" is internally contradictory
    → COMT explains the same behavior WITHOUT contradiction (§3)


§4.3 HYPOTHESIS D — Chunk Threshold (framework proposal) 🔴⭐:

  BASIS:
    Berridge (1998, 2003): dopamine ≠ reward, dopamine = signal
    → Dopamine does NOT cause pleasure → only SIGNALS "new chunk has value"
    → Actual pleasure = opioid = body-base response when chunk value is confirmed

  MODEL:
    ① B+C neurons fire continuously → attempt synchrony → patterns form
    ② VTA detects UNUSUALLY STRONG SYNCHRONY (above baseline)
    ③ VTA fires → dopamine → binds DRD4 receptor ON PFC neuron
    ④ DRD4-7R less sensitive → HIGH DISTURBANCE THRESHOLD:
       Small fluctuations = PFC TRULY DOESN'T KNOW (receptor doesn't open)
       Only LARGE fluctuations cross threshold → PFC receives FEW signals,
       each signal = LARGE
    ⑤ DRD4-4R sensitive → LOW THRESHOLD:
       Even small fluctuations cross → PFC receives MANY signals
    ⑥ PFC spotlight directs to region with signal → body-base check
    ⑦ Result:
       7R: FEW detections → each = LARGE chunk → body reward HIGH → DRAWN to novelty
       4R: MANY detections → each = SMALL chunk → body reward SMALL → SATISFIED
           with routine
       7R: "......... AHA!" (wait long, 1 big insight)
       4R: "ah... ah... ah..." (many, small, continuous)


§4.4 VALIDATING Hypothesis D — testing against cases:

  Social media scrolling:
    7R: small chunks continuously → DO NOT cross threshold → "boring, not interesting"
        → STOP early
    4R: small chunks CROSS threshold → each post = mild reward → continue
    → ✅ 7R scrolls LESS, 4R scrolls MORE (opposite of old interpretation)

  Gambling:
    7R: near-miss = large chunk → body thinks "ALMOST WON" → STRONG hook
    4R: near-miss = small chunk → body says "hmm" but NOT strongly
    → ✅ 7R more easily hooked by near-miss (consistent with gambling observations)

  Encountering a hard problem:
    7R: waits for LARGE chunk → IF foundation chunks SUFFICIENT → "AHA!" →
        reward EXTREMELY HIGH
        → IF foundation chunks INSUFFICIENT → wait forever → frustrate → give up
    4R: small chunks continuously → each step = reward → steady progress
    → ✅ 7R = breakthrough OR frustrate. 4R = incremental steady.

  → ALL CASES consistent ✅. No contradiction in any scenario.


§4.5 4 Hypotheses compared:

  Hypothesis A (PFC draft retention):
    ✅ Explains SWITCH behavior
    ❌ Does NOT explain why 7R is DRAWN to novelty (motivation)

  Hypothesis B (tonic vs phasic):
    ✅ Explains "staying still = uncomfortable"
    ❌ Does NOT explain gambling near-miss hook

  Hypothesis C (gene linkage):
    ✅ Explains data inconsistency (GWAS doesn't find DRD4 significant)
    ❌ Explains NO mechanism at all

  Hypothesis D (chunk threshold) ⭐:
    ✅ SWITCH (7R bypasses small chunks → seeks large ones)
    ✅ MOTIVATION (large chunk → large reward)
    ✅ GAMBLING (near-miss = large chunk → body takes it as real)
    ✅ SCROLL (small chunks < threshold → bores quickly)
    ✅ DEEP WORK (needs foundation chunks + time → AHA or frustrate)
    ✅ Grounded in: Berridge (dopamine ≠ reward) = established
    ✅ Consistent with ALL measured data (Van Tol + Ebstein)

  → Framework prefers Hypothesis D
  → A may SUPPLEMENT D (2 effects overlap)


§4.6 Testable Predictions:

  Predict 1: 7R responds MORE STRONGLY than 4R to a LARGE chunk
             7R responds MORE WEAKLY than 4R to a SMALL chunk
             4R responds UNIFORMLY to all chunk sizes

  Predict 2: Stimulants — 7R individuals require HIGHER doses than 4R
             (higher threshold → needs STRONGER dopamine signal)
             🟢 Some support: ADHD medication — 7R carriers
                often require HIGHER stimulant doses

  → If predictions hold = confirms hypothesis
  → If predictions fail = needs revision
```


### §4.7 — DRD4 × Reward Profile (v1.1 new — Drill R8)

```
🔴 DRD4 HYPOTHESIS D × REWARD (extending §4.3):

  DRD4-7R = HIGH chunk threshold (detects LARGE chunks only).
  DRD4-4R = LOW chunk threshold (detects small chunks).

  Extension to REWARD patterns (IF Hypothesis D correct):

    7R: ② rewards RARE but INTENSE ("AHA!" type)
        Sensory: need STRONGER stimulus for same pleasure
        Flow: once IN flow MORE intense, getting INTO flow HARDER
        Domain: NEEDS deep chunk library → shallow domain = frustrate
        Risk: "can't find anything interesting" if domain wrong

    4R: ② rewards FREQUENT but MILD ("ah..." — steady accumulation)
        Sensory: mild stimulus sufficient
        Flow: easier entry, less intense peak
        Domain: satisfies across breadth → less domain-dependent
        Risk: "content with surface" → may not develop depth

  ⚠️ DRD4 = Hypothesis D (framework 🔴), NOT established.
  BUT consistent with observed individual differences in reward intensity.
  AND: Direct-State reward = hardware-level → NOT affected by DRD4
    (Direct-State below VTA threshold system → "democratic reward").

  → Detail: Reward-Signal-Architecture.md §1
  Source: Drill §3.22 ❹ (R8).
```


### §4.8 — COMT × DRD4 Interaction (v1.1 new — Drill R8)

```
🔴 INTERACTION EFFECTS — WHY "TYPE" DESCRIPTIONS FAIL:

  Simple trait psychology: "extrovert = high reward sensitivity."
  Framework: reward sensitivity = 5-axis emergent →
  trait descriptions = LOSSY COMPRESSION.

  COMT × DRD4 → 4 COMPOUND REWARD PATTERNS:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ Combination        │ Reward Pattern       │ Popular Label        │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + 7R       │ Clear fast + high    │ "Thrill seeker"      │
  │                    │ threshold = NEED     │ Jumps to big novel   │
  │                    │ novel BIG experiences│ experiences           │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + 4R       │ Clear slow + low     │ "Obsessive expert"   │
  │                    │ threshold = SATISFY  │ Deep within single   │
  │                    │ within single domain │ domain               │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + 4R       │ Clear fast + low     │ "Social butterfly"   │
  │                    │ threshold = many     │ Many small rewards   │
  │                    │ small rewards, none  │ from many domains    │
  │                    │ deep                 │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + 7R       │ Clear slow + high    │ "Frustrated genius   │
  │                    │ threshold = draft    │  or true genius"     │
  │                    │ stuck + needs BIG    │ BIMODAL: highest     │
  │                    │ chunks               │ genius OR highest    │
  │                    │                      │ frustration          │
  └────────────────────┴──────────────────────┴──────────────────────┘

  ⭐ Met/Met + 7R = MOST EXTREME BIMODAL:
    → IF domain right + deep chunks: draft persists + big threshold met
      = DEEPEST flow, most intense ②, most productive
    → IF domain wrong + shallow: draft stuck + threshold never met
      = HIGHEST frustration, most miserable

  → = Same hardware, different DOMAIN FIT → "genius" or "miserable"
  → = Counseling implication: Met/Met + 7R NEEDS right domain most urgently

  ⚠️ COMT × DRD4 interaction = framework reasoning, NOT tested.
  ⚠️ DRD4 = Hypothesis D (🔴). COMT × DRD4 = 🔴 × 🔴 = highly speculative.
  ⚠️ "Popular labels" = ILLUSTRATIVE, not clinical categories.
  Source: Drill §3.22 ❺ (R8).
```

---

## §5 — MAO-A: Mood Stability (Whole Brain)

```
② MAO-A (Monoamine Oxidase A)
   🟢 SUPPLEMENTARY — replicated

   MAO-A = enzyme that breaks down dopamine + serotonin WHOLE BRAIN
   (unlike COMT which is PFC-specific only)

   LOW activity: dopamine + serotonin PERSIST LONGER → mood STABLE
   HIGH activity: dopamine + serotonin CLEAR FAST → mood SHIFTS

   🟢 Research: Shih et al. 1999

   DIFFERS FROM COMT IN SCOPE:
     COMT = clears dopamine in PFC (local, PFC-specific)
     MAO-A = clears dopamine + serotonin WHOLE BRAIN (global)
     → 2 DIFFERENT "tuning knobs":
       COMT = PFC draft management (improviser/specialist)
       MAO-A = mood + energy overall (stable/volatile)

   Combinations:
     COMT fast + MAO-A slow = improviser PFC + stable mood
     COMT slow + MAO-A fast = specialist PFC + shifting mood

   THE CORE MECHANISM:
     IMPROVISER vs SPECIALIST = primarily driven by COMT (PFC clear speed):
     → Same dopamine release → DIFFERENT enzyme → DIFFERENT draft duration
       → DIFFERENT behavior
     → = Hardware manages the DRAFT, not hardware managing REWARD

     NOT:
       ❌ "Hormones fluctuate FASTER" (fluctuation speed ≈ similar)
       ❌ "Less pleasant" (liking/opioid may be the same)
       ❌ "Needs more dopamine" (DRD4 narrative has logical gaps)

     BUT:
       ✅ Draft is CLEARED fast or HELD long in PFC workspace
       ✅ = A problem of DRAFT MANAGEMENT, not REWARD SENSITIVITY

   ESTIMATED DISTRIBUTION (simplified, without DRD4):
     COMT Val/Val + MAO-A high: ~15-20% (improviser, switches fast)
     COMT Met/Met + MAO-A low:  ~60-70% (specialist, deep focus)
     Mixed:                     ~15-20% (T-shaped, context-dependent)
```

---

## §6 — NE α2/α1: PFC Circuit Breaker

```
NOREPINEPHRINE (NE) — FROM LOCUS COERULEUS (LC):

  LC = small cluster of neurons in the BRAINSTEM (C zone)
  → Operates UNCONSCIOUSLY — PFC does NOT control LC
  → LC receives input from: amygdala (threat), hypothalamus (arousal), body state
  → LC releases NE → broadcasts WHOLE BRAIN (but PFC is particularly sensitive)


NE has 2 TYPES of receptors ON PFC:

  ┌──────────────┬──────────────────────────┬──────────────────────────┐
  │              │ α2 RECEPTORS             │ α1 RECEPTORS             │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Affinity     │ HIGH (activates at       │ LOW (activates only at   │
  │              │ low-moderate NE)         │ high NE)                 │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ When active  │ ENHANCES PFC networks    │ DISCONNECTS PFC networks │
  │              │ → WM sharp, attention    │ → WM LOST, PFC OFFLINE   │
  │              │   focused                │                          │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ When         │ Normal, focused          │ Acute stress, emergency  │
  ├──────────────┼──────────────────────────┼──────────────────────────┤
  │ Felt as      │ "Focused, clear-headed"  │ "Panicked, disoriented,  │
  │              │                          │  can't think"            │
  └──────────────┴──────────────────────────┴──────────────────────────┘

  = SAME 1 chemical (NE), DIFFERENT receptor (α2 vs α1), OPPOSITE effect
  = Yerkes-Dodson at the RECEPTOR LEVEL


ACUTE THREAT SEQUENCE (milliseconds):

  1. Amygdala detects threat (via "low road" — LeDoux 1996)
     → Sensory thalamus → Amygdala DIRECTLY (bypasses cortex)
     → ~12ms — BEFORE PFC knows what happened

  2. Amygdala → signals LC → NE FLOOD

  3. High NE → α1 receptors on PFC ACTIVATE
     → PFC network connections DISCONNECT
     → PFC OFFLINE (NOT "busy" — SEVERED CONNECTION)

  4. SIMULTANEOUSLY high NE ENHANCES:
     → Amygdala (C zone — threat response amplified)
     → Basal ganglia (C zone — compiled responses ready)
     → = Brain TRANSFERS CONTROL: A(PFC) → C(subcortical)

  5. Body responds: fight / flight / freeze (compiled, UNCONSCIOUS)
     → BYPASSES PFC — because PFC is offline

  6. Threat passes → NE DECREASES gradually
     → α1 deactivates → PFC reconnects → back online
     → PFC evaluates AFTER: "what just happened?"

  The ENTIRE sequence 1-5 = DESIGN FEATURE, not a bug.
  → Recovery: seconds → PFC back online.
  → ≠ cortisol damage (weeks-months, REAL DAMAGE).
  → Detail: Core-Software.md §4.3


CORE INSIGHT:
  → PFC has α1 receptors = "circuit breaker" BUILT INTO itself
  → Body (via LC) can SHUT DOWN PFC at any moment
  → PFC CANNOT prevent this shutdown (α1 = hardware level)
  → = PFC is NOT the "boss" — it is a TOOL the body can TURN OFF

  Evolution logic:
    Emergency does NOT need deliberation (PFC slow, ~200ms+)
    Emergency NEEDS compiled response (C subcortical fast, ~12ms)
    → α1 = evolutionary "circuit breaker" — 500 million years of optimization


🟢 THREAT GRADIENT (Mobbs et al. 2007):
  fMRI: virtual predator chasing subjects:
    Threat FAR: vmPFC ACTIVE (planning, strategy)
    Threat CLOSE: vmPFC DEACTIVATED → PAG activated (panic, reflex)
    = GRADIENT, not an ON/OFF switch
    = Closer to danger → more PFC suppressed → subcortical stronger


PTSD IMPLICATION:
  → Chronically HIGH NE baseline (PTSD characteristic)
  → α1 active CHRONICALLY → PFC impaired CONTINUOUSLY
  → "Can't think clearly" = PFC PERSISTENTLY disconnected
  → Not "weakness" — HARDWARE is compromised
  → Treatment: reduce NE baseline → α1 deactivates → PFC reconnects
  → 🟢 PTSD + NE dysregulation = established (Southwick 1999)
```

🟢 Research: Arnsten 2009, 2015; LeDoux 1996; Mobbs 2007; Ramos & Arnsten 2007; Southwick 1999

---

## §7 — VTA Detection Loop (7 Steps)

```
🟡 HYPOTHESIS — logic consistent with research, no one has validated the
   full chain. Each step = established independently.
   ASSEMBLED into flow = framework contribution.


STEP 1 — B+C NEURONS FIRE CONTINUOUSLY (24/7, including during sleep):
  86 billion neurons fire → signal spreads through ~7000 neighbors per neuron
  → Neurons ATTEMPT synchrony → most FAIL → dissipate
  → Some SUCCEED → pattern forms = chunk
  → NO ONE controls this — self-organizing

  ⭐ CORTISOL = CALIBRATION ENERGY:
  → Cortisol rises → neurons fire MORE STRONGLY (arousal)
  → Chunks being compiled get SHAKEN UP → TRY NEW patterns
  → = Cortisol serves B+C calibration; PFC is the SECONDARY party
    that gets notified


STEP 2 — VTA DETECTS CHANGE (delta, not absolute):
  VTA (~400,000 neurons, midbrain — C zone):
  → Region X fires stably → VTA HABITUATES → ignores
  → Region X suddenly fires DIFFERENTLY → VTA detects: "CHANGE!" → fires
  → = VTA detects DELTA (change), not ABSOLUTE
  → Old compiled schema fires STRONGLY but STEADILY → VTA habituates → silent
  → New pattern fires WEAKLY but DIFFERENTLY → VTA detects → fires

  ⭐ Does NOT need complex "predict → compare → error" (Schultz 1997)
  → ONLY NEEDS: "habituate → different from habit → fire" (habituation + delta)
  → = Simpler mechanism, SAME observable result

  VTA fires → dopamine → broadcasts: PFC, Nucleus Accumbens, Hippocampus


STEP 3 — RECEPTOR FILTER (DRD4):
  Dopamine in the synaptic cleft → binds DRD4 receptor on PFC neuron
  → 7R (less sensitive): needs MORE dopamine → only detects LARGE changes
  → 4R (sensitive): less dopamine sufficient → detects even SMALL changes
  → PFC does NOT "choose to ignore" — 7R TRULY DOESN'T KNOW small chunks exist
  → = HARDWARE filter, not SOFTWARE choice


STEP 4 — PFC SPOTLIGHT (top-down):
  PFC neuron fires → sends DOWN to B cortical areas:
  → Boosts NE + Acetylcholine at the target region
  → Neurons in the target region fire MORE STRONGLY = "spotlight"
  → PFC does NOT "tell" B what to compute — only RAISES THE VOLUME
  → Spreading activation: boost region A → neighbors fire → RELATED chunks

  Asymmetry:
    Up:   B+C → VTA (intermediary) → dopamine → PFC (indirect)
    Down: PFC → DIRECTLY → B target (no middleman)

  🟢 Desimone & Duncan 1995, Miller & Cohen 2001


STEP 5 — BODY-BASE CHECK:
  PFC receives chunk → integrates into workspace
  → Sends down to body-base: "simulate → what does the body feel?"
  → Chunk MATCHES body-need → opioid release → REAL reward
  → Chunk DOESN'T match → body "meh" → discard
  → Dopamine = signal "there's a change" (doorbell)
  → Opioid = reward "actually valuable" (gift behind the door)


STEP 6 — REINFORCE + LOOP:
  Body reward (opioid) → that region REINFORCES:
  → Neurons fire STRONGLY + connections TIGHTEN → NEW pattern STABILIZES
  → VTA habituates → PFC reduces attention
  → ON TOP OF new stable pattern → B+C TRIES FURTHER
  → NEW change → VTA detects → dopamine → PFC → body check → loop

  AFTER MANY ROUNDS:
  → Rough pattern → many body-check rounds → refined
  → = High-quality schema = many body-check rounds
  → = "Same instrument, same energy → the melody is now different"


STEP 7 — CLEAN UP (COMT clear):
  Dopamine in the synaptic cleft doesn't stay permanently:
    COMT enzyme (PFC-specific): Val/Val clears FAST, Met/Met clears SLOW
    DAT transporter (striatum-specific): PFC has LITTLE DAT → COMT is primary
  → After cleanup: synaptic cleft CLEAN → ready for NEW signal


THE LOOP SUMMARIZED:
  ① B+C: neurons self-fire + self-synchronize → patterns form
  ② VTA: detects CHANGE (habituation) → fires → dopamine → PFC
  ③ Receptor: 4R receives small changes / 7R only large ones (HARDWARE filter)
  ④ PFC: spotlight DOWN to B target → boost → B responds CLEARLY
  ⑤ Body-base: check chunk → reward (opioid) if matches body-need
  ⑥ Reinforce: reward → pattern strengthens → stabilizes → B+C tries further → LOOP
  ⑦ COMT: clears dopamine → clear speed → affects draft duration

  = Bottom-up (dopamine signal) ↔ Top-down (PFC spotlight)
  = NO ONE controls the whole thing = self-organizing network
```

---

## §8 — 4 Receptor Systems Summary

```
  ┌──────────┬──────────────────┬──────────────────┬──────────────┐
  │ Receptor │ Chemical         │ PFC Effect       │ Timeframe    │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ DRD4     │ Dopamine (VTA)   │ Chunk THRESHOLD  │ Per-event    │
  │          │                  │ "which           │ (ms)         │
  │          │                  │ fluctuations     │              │
  │          │                  │ are large enough │              │
  │          │                  │ to report?"      │              │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ COMT     │ Dopamine (PFC)   │ CLEAR SPEED      │ Per-draft    │
  │          │                  │ "how long does   │ (seconds)    │
  │          │                  │ a draft stay     │              │
  │          │                  │ before clearing?"│              │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ α2       │ NE (LC)          │ ENHANCE PFC      │ Continuous   │
  │          │                  │ "sharp, focused" │ (at moderate │
  │          │                  │                  │ NE)          │
  ├──────────┼──────────────────┼──────────────────┼──────────────┤
  │ α1       │ NE (LC)          │ DISCONNECT PFC   │ Emergency    │
  │          │                  │ "offline, reflex"│ (ms, acute)  │
  └──────────┴──────────────────┴──────────────────┴──────────────┘

  = 4 receptor systems → 4 ways hardware affects PFC
  = EACH person has a DIFFERENT VARIANT at each receptor
  = "PFC profile" = combination of DRD4 × COMT × α2/α1 sensitivity × PFC-Quality
```


### §8b — 4 Receptor Systems × 5 Reward Profiles (v1.1 new — Drill R8)

```
🟡 HARDWARE AFFECTS REWARD PROFILES DIFFERENTLY:

  §8 shows 4 receptor systems × PFC function (cognition).
  §8b extends: 4 systems + μ-opioid × 5 REWARD profiles:

  ┌──────────────┬──────────────┬──────────────┬──────────────┬─────────────┐
  │ Receptor     │ ① Sensory    │ ② Coherence  │ ③ Social     │ ④ Relief    │
  │ System       │   Reward     │   Reward     │   Reward     │   Reward    │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ COMT         │ Low impact   │ HIGH: clear  │ Moderate     │ Low impact  │
  │ (PFC clear   │ (sensory =   │ speed → ②    │ (social eval │ (cortisol   │
  │  speed)      │ below PFC)   │ develop speed│ = PFC-partly)│ system)     │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ DRD4         │ Low impact   │ HIGH: chunk  │ Moderate     │ Low impact  │
  │ (Hypothesis  │ (sensory not │ threshold →  │ (social cues │ (not VTA-   │
  │  D threshold)│ VTA-gated)   │ "AHA" vs "ah"│ = prediction │ gated)      │
  │              │              │              │ delta)       │             │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ MAO-A        │ Moderate     │ Moderate     │ HIGH: mood   │ HIGH: base  │
  │ (mood global │ (sensory     │ (sustained   │ stability →  │ cortisol ↔  │
  │  stability)  │ valence)     │ affect mood) │ social resil.│ relief mag. │
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ NE α2/α1     │ Low impact   │ HIGH: PFC    │ HIGH: threat │ HIGH: NE ↔  │
  │ (circuit     │              │ stability →  │ assessment → │ cortisol →  │
  │  breaker)    │              │ flow access  │ social threat│ relief sens.│
  ├──────────────┼──────────────┼──────────────┼──────────────┼─────────────┤
  │ μ-Opioid     │ HIGHEST      │ HIGH         │ HIGH         │ Moderate    │
  │ receptor     │ (E₀-E₃ all   │ (coherence   │ (social bond │ (relief =   │
  │ density      │ opioid)      │ → opioid)    │ opioid-aided)│ cortisol    │
  │              │              │              │              │ primarily)  │
  └──────────────┴──────────────┴──────────────┴──────────────┴─────────────┘

  ⭐ DIRECT-STATE (touch, warmth, exercise) = LESS affected by ALL receptor systems:
    → Direct-State = non-opioid, non-PFC, hardware-level pathways
    → Direct-State reward = MORE EGALITARIAN across individuals
    → Hardware individual differences = primarily EVALUATIVE variation
    → Direct-State = evolution's EQUALIZER ("democratic reward")

  → Evaluative: μ-opioid density + COMT + DRD4 → HIGHLY variable
  → Direct-State: CT afferent density varies LESS across individuals
  → = WHY body-based reward (touch, exercise) is "democratic"

  ⚠️ μ-opioid receptor density = 🟡 consistent with pharmacological
  literature but individual variation poorly mapped.
  ⚠️ Table = framework synthesis, NOT established receptor-by-profile mapping.
  Source: Drill §3.22 ❷ (R8).
```


### §8c — 3-Variable Shorthand (v1.1 new — Drill R8)

```
🟡 PRACTICAL DESCRIPTION — 3-Variable Profile:

  Full model (5 profiles × 5 axes = 25 cells) = too complex for daily use.
  COMPRESSED DESCRIPTION uses 3 variables:

  ┌──────────────────────────────────────────────────────────┐
  │ ① Evaluative/Direct-State Ratio: position on the         │
  │                                  Evaluative ↔ Direct-State│
  │                                  spectrum                 │
  │ ② Dom. Profile: which of the 5 profiles (①②③④⑤) STRONGEST│
  │ ③ Breadth:      how many profiles ACTIVE (narrow ↔ broad) │
  └──────────────────────────────────────────────────────────┘

  EXAMPLES (illustrative, NOT measured):

    Physicist: High Evaluative (90/10), Dominant ②, Moderate breadth (②+③+④)
      → Intense coherence seeker, some social/relief, very little Direct-State

    Chef: Balanced Evaluative/Direct-State (60/40), Dominant ①, Narrow (①+④)
      → Sensory-driven, relief from completion, significant body reward

    Therapist: Moderate Evaluative (55/45), Dominant ③, Broad (①②③④⑤)
      → Social reward primary, accesses ALL profiles

    Athlete: Low Evaluative (30/70), Dominant Direct-State+④, Narrow
      → Body-driven, relief from exertion, minimal coherence/social

  → "Personality" re: reward = this 3-variable profile
  → Simple "extrovert/introvert" = LOSSY COMPRESSION of 3 variables
  → = Framework alternative to trait psychology for reward description

  ⚠️ Cannot MEASURE precisely yet — organizing framework.
  ⚠️ Illustrative examples = framework reasoning, not clinical data.
  → Detail: Reward-Signal-Architecture.md §4
  → Detail: Reward-Signal-Architecture.md §8.5 (5-axis model)
  Source: Drill §3.22 ❽ (R8).
```

---

## §9 — Honest Assessment

```
🟢 ESTABLISHED:
  WM ~4±1 items (Cowan 2001)
  COMT Val/Met effects on PFC (Egan 2001, well-replicated)
  DRD4-7R binding affinity lower than 4R (Van Tol 1992)
  NE α2/α1 dual effect on PFC (Arnsten 2009, 2015)
  Amygdala low road ~12ms (LeDoux 1996)
  Threat gradient PFC→PAG (Mobbs 2007)
  Dopamine ≠ reward (Berridge 1998, 2003)
  VTA detects novelty/surprise (Schultz 1997)
  Top-down attention PFC→cortex (Desimone & Duncan 1995)
  Neural efficiency: skilled individuals fire LESS (Haier 1992, Neubauer & Fink 2009)
  Brain size vs IQ: ~6% variance (Pietschnig 2015)
  PTSD + NE dysregulation (Southwick 1999)

🟡 FRAMEWORK SYNTHESIS:
  2-parameter model (Quality + Clear Speed) — novel organization
  Observed Capacity = 4-factor formula — novel, components established
  "Improviser/Specialist = COMT draft management" — novel framing
  VTA = delta detector (habituation) — prediction-delta, NOT a
    "prediction error" calculator
  PFC spotlight = raises volume, does not command computation
  7-step VTA detection loop — novel integration
  COMT × Reward pattern (§3.4) — extension from cognition to reward domain (v1.1)
  COMT × Childhood trajectories (§3.5) — 4 combos, framework synthesis (v1.1)
  4 Receptor Systems × 5 Profiles (§8b) — cross-mapping, not established (v1.1)
  3-Variable Shorthand (§8c) — practical but lossy compression (v1.1)
  Direct-State "democratic reward" — less hardware-variable (v1.1)

🔴 NEEDS MORE RESEARCH:
  DRD4 Hypothesis D (chunk threshold) — testable, never tested
  DRD4 Hypothesis A vs B vs C vs D — not yet settled
  MAO-A × COMT interaction — limited data
  Individual α2/α1 sensitivity variance — not well characterized
  Quantitative: how large a chunk size crosses the 7R threshold?
  COMT × DRD4 interaction patterns (§4.8) — framework 🔴×🔴, highly speculative (v1.1)
  DRD4 × Reward profiles (§4.7) — depends on Hypothesis D validity (v1.1)
  μ-opioid individual density variation — poorly mapped (v1.1)

🔴 TESTABLE PREDICTIONS (v1.1):
  P-R8a: COMT Val/Val → shorter flow, more domain-switches
    → Met/Met → longer flow, fewer domain switches
  P-R8b: Direct-State reward sensitivity has LOWER individual variance than Evaluative
    → B SD < A SD (B = hardware, A = compilation-dependent)
  P-R8d: Met/Met + 7R = HIGHEST variance in life satisfaction
    → BIMODAL: very high (right domain) OR very low (wrong domain)
```

---

## §10 — Cross-References

```
PFC FOLDER:
  PFC-Function.md v1.2 — 24 observable functions
  PFC-Configuration.md v1.0 — 6 dynamic modes, survival matrix (v1.1 NEW)
  PFC-Development.md — life stages + training
  PFC-Hold-Dimensions.md — why ~4±1

PHYSICAL MAP:
  Neural-Architecture.md §2 — sub-regions, connectivity

REWARD (v1.1 NEW):
  Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State, 5 Profiles, E₀→E₃
    → §3.4 COMT×Reward maps to Reward-Signal-Architecture §4 (profiles)
    → §8b Receptor×Profiles maps to Reward-Signal-Architecture §8.5
      (individual differences)
  03-Reward.md — Body-Feedback-Precondition preconditions, 7-step VTA
  Dopamine-Is-Not-Reward.md — Berridge, wanting ≠ liking
  Liking-Wanting.md — wanting × liking mechanisms

COMPILATION (v1.1 NEW):
  Compile-Taxonomy.md v3.0 §6 — 4 pathways → 4 Precondition-5 tag types
    → §3.5 COMT×Childhood maps to 4-Pathway × Precondition-5 Tag Model

BODY SYSTEMS:
  Cortisol-Baseline.md v2.0 — cortisol affects PFC function
  Body-Feedback.md — body signals + Body-Feedback-Precondition

CORE:
  Core-Software.md §6 — PFC in cycle architecture
  Chunk.md v2.0 — chunks PFC operates on

DRILL SOURCE (v1.1):
  Drill-Reward-Feeling-Main.md v1.2 §3.22 (R8) — Individual Differences

OLD FILE (backup):
  PFC/Imagination/backup/PFC-Analysis-v1.1.md §8 — source content
```

---

> **PFC-Hardware.md v1.1**
>
> 4 receptor systems: DRD4 (threshold), COMT (clear speed), α2 (enhance), α1 (disconnect).
> PFC-Quality = resolution × filter × retrieval × compression (per-slot).
> Observed Capacity = Hardware × Chunks × Cortisol × Context.
> Improviser vs Specialist = COMT draft management, not reward sensitivity.
> v1.1: COMT×Reward, COMT×Childhood, DRD4×Reward, COMT×DRD4 interaction,
>   4 Receptors × 5 Profiles, 3-Variable Shorthand, Direct-State "democratic reward."
>
> Version: v1.1, 2026-05-10.
