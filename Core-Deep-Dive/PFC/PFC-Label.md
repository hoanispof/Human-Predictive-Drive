---
title: PFC-Label Convention — Vocabulary Reference
version: 1.1
created: 2026-05-22
updated: 2026-05-25 (v1.1 — §4 +PFC Operations × dissonance type table, Dissonance-Signal-Architecture v1.0 integration)
status: REFERENCE v1.1
scope: |
  VOCABULARY REFERENCE: Label conventions for all PFC-related concepts.
  Formalizes the 3-tier label system: General → Direction → Specific.
  13 domains: Roles, Processing, Operations, Cost, Quality, Regions, Hardware,
  Simulation-Engine, Cognitive Ops, Failure Modes, Observer/Mechanism, Deprecated.
  Does NOT explain mechanisms (source files do that).
  ONLY formalizes: WHICH LABEL, WHAT IT MEANS, WHEN TO USE IT.
purpose: |
  PFC vocabulary appears in 78+ files but was NEVER formalized.
  Same concept → 3-5 different names → confusion.
  This file: VOCABULARY REFERENCE for all PFC-related labels.
  Companion to Body-Feedback-Label v2.0 (body-feedback vocabulary).
  Body-Feedback-Label = body SIGNAL vocabulary. This file = PFC OPERATION vocabulary.
  Overlap at Body-Feedback-Label §8/§9C = bridge zone (cross-ref, no duplication).
position: |
  Core-Deep-Dive/PFC/ — peer to PFC-Operations.md, Simulation-Engine.md.
  READ IMMEDIATELY AFTER PFC-Function.md (entry point) and PFC-Operations.md (mechanism).
dependencies:
  - PFC-Operations.md v1.0 — §2-§4 Hold/Suppress, §5 Quality, §9 Budget, §10 3-Cost
  - Simulation-Engine.md v1.0 — §1-§3 Engine/Components/Axes, §6 mPFC gradient
  - Logic-Feeling.md v2.1 — Compiled/Fresh spectrum, observer labels (companion)
  - PFC-Function.md v1.2 — 24 functions, 5 categories (companion)
  - PFC-Hardware.md v1.1 — COMT, DRD4, NE, capacity/quality
  - PFC-Hold-Dimensions.md — ~4±1 slots, interference limit
  - Body-Feedback-Label.md v2.1 — §8 Compiled/Fresh, §9C 3-cost (companion)
  - Dissonance-Signal-Architecture.md v1.0 — §7.2 PFC Operations × dissonance type
  - Ask-AI.md v3.1 — Dual Check: body=quality controller, domain=final arbiter
  - Autonomy-Hardware.md v1.1 — vmPFC/DRN, controllability
  - Cortisol-Baseline.md v2.1 — cortisol × PFC damage, NE α1
sources:
  - Drill-PFC-Label v1.0 (1,153L, 16 sections, 24 citations)
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# PFC-Label Convention — Vocabulary Reference

> **PFC-related vocabulary appears in 78+ files.**
> **Yet the same concept → 3-5 different names → confusion.**
>
> **"Fresh" / "PFC-Fresh" / "draft" / "operation" = same conceptual zone, DIFFERENT levels.**
> **"PFC" = Observer? Lawyer? Director? Universal Resource? = depends on context.**
>
> **This file: VOCABULARY REFERENCE for all PFC-related labels.**
> **Does NOT explain mechanisms (source files do that).**
> **ONLY formalizes: WHICH LABEL, WHAT IT MEANS, WHEN TO USE IT.**
>
> **Companion: Body-Feedback-Label v2.0 (body SIGNAL vocabulary).**
> **This file = PFC OPERATION vocabulary. Overlap at Body-Feedback-Label §8/§9C = bridge zone.**

---

## Table of Contents

- §0 — WHY THIS FILE EXISTS
- §1 — 3-TIER LABEL SYSTEM + 4 VOCABULARY LEVELS
- §2 — PFC ROLE LABELS (5 roles depending on context)
- §3 — PROCESSING SPECTRUM: COMPILED ←→ FRESH (brief)
- §4 — PFC OPERATIONS: HOLD + SUPPRESS (labels)
- §5 — PFC COST LABELS (3-cost + budget)
- §6 — COMPILED QUALITY LABELS (genuine / schema / threat)
- §7 — PFC REGION LABELS (anatomy mapping)
- §8 — PFC HARDWARE LABELS (individual differences)
- §9 — SIMULATION-ENGINE LABELS (1 engine, 3 components)
- §10 — PFC COGNITIVE LABELS (spotlight, narrative, labeling, check)
- §11 — PFC FAILURE MODES (5 patterns)
- §12 — OBSERVER vs MECHANISM (Logic/Feeling vs Compiled/Fresh)
- §13 — DEPRECATED TERMS + STANDARDIZATION
- §14 — USAGE RULES
- §15 — HONEST ASSESSMENT
- §16 — CROSS-REFERENCES
- §17 — RESEARCH CITATIONS

---

## §0 — WHY THIS FILE EXISTS

```
⭐ PFC VOCABULARY = SCATTERED + INCONSISTENT:

  PROBLEM 1 — SAME CONCEPT, MULTIPLE NAMES:
    "Fresh" / "PFC-Fresh" / "draft" / "Fresh processing" = 4 labels
    for the SAME concept: PROCESSING THAT IS NOT YET COMPILED.
    → Which file uses which name? Nobody knows.

  PROBLEM 2 — SAME WORD, DIFFERENT LEVELS:
    "Fresh" = STATE on the spectrum (position)
    "PFC operations" = ACTION (HOLD + SUPPRESS)
    "draft" = a SPECIFIC action (1 type of HOLD)
    → 3 different levels mixed up → confusing.

  PROBLEM 3 — PFC HAS MULTIPLE ROLES:
    Observer (Feeling.md), Lawyer (PFC-Operations.md §10),
    Director (Neural-Processing-Flow),
    Universal Resource (PFC-Operations.md §9),
    Quality Controller (Ask-AI v3.1 §6.1)
    → Which role applies when?

  PROBLEM 4 — PFC FILES ARE SCATTERED:
    PFC-Function.md, PFC-Hardware.md, PFC-Development.md,
    PFC-Hold-Dimensions.md, PFC-Configuration.md,
    PFC-Operations.md, Simulation-Engine.md,
    Logic-Feeling.md, Logic-Feeling-Balance.md
    → 9+ separate files about PFC → which vocabulary lives where?

  PROBLEM 5 — OVERLAP WITH BODY-FEEDBACK-LABEL:
    Body-Feedback-Label §8 already covers Compiled/Fresh processing labels.
    Body-Feedback-Label §9C already covers 3-cost sources.
    → This file SUPPLEMENTS (PFC operations, roles, regions, hardware),
    does NOT duplicate.


  ⭐ THIS FILE RESOLVES:
    → Formalizes vocabulary for ALL PFC-related concepts
    → Standardizes: 1 label only for 1 concept
    → Deprecates: "draft" standalone, "PFC-Fresh" redundant (§13)
    → 3-tier system: consistent with Body-Feedback-Label
    → Clearly distinguishes LEVELS: state / action / sub-action / role
```

---

## §1 — 3-TIER LABEL SYSTEM + 4 VOCABULARY LEVELS

```
⭐ TIER SELECTION RULES (same as Body-Feedback-Label §1):

  Tier 3 (MOST SPECIFIC) > Tier 2 (DIRECTION) > Tier 1 (MOST GENERAL)

  → When knowing SPECIFICALLY what PFC is doing → use Tier 3:
    "dlPFC HOLD new pattern → ① PFC draft cost"

  → When knowing DIRECTION but not specific → use Tier 2:
    "Fresh processing" / "HOLD" / "SUPPRESS"

  → When ONLY knowing PFC is involved → use Tier 1:
    "PFC processing" / "PFC cost"


  AUDIENCE-APPROPRIATE:

    Expert / deep analysis:
      → Tier 3 primary. Region + operation + cost traced.

    Learning / Research files:
      → Tier 2 primary: "Fresh processing", "HOLD", "suppress cost"
      → Precise enough, sufficient for understanding basic mechanism.

    General / overview:
      → Tier 1 when needed: "PFC is processing" / "PFC cost"
      → Can drill deeper if needed.


  4 LEVELS OF PFC VOCABULARY:

    ┌────────────────────────────────────────────────────┐
    │ LEVEL 1 — ROLES (what PFC "is" in that context):   │
    │   Observer, Lawyer, Director, Universal Resource,   │
    │   Quality Controller                                │
    │                                                    │
    │ LEVEL 2 — STATES (position on the spectrum):        │
    │   Compiled ←→ Fresh                                 │
    │                                                    │
    │ LEVEL 3 — OPERATIONS (what PFC does):               │
    │   HOLD = amplify new                                │
    │   SUPPRESS = block existing                         │
    │                                                    │
    │ LEVEL 4 — SUB-OPERATIONS (specific):                │
    │   "draft novel path" = specific HOLD action          │
    │   "inhibit compiled response" = specific SUPPRESS    │
    └────────────────────────────────────────────────────┘

  ⚠️ Do NOT mix levels:
    ✗ "PFC-Fresh operation" (mixes state with operation)
    ✓ "Fresh processing requires HOLD operation" (distinguished)
    ✗ "draft" standalone (ambiguous — state? action? output?)
    ✓ "PFC HOLD draft novel path" (operation + sub-action clearly stated)
```

---

## §2 — PFC ROLE LABELS

```
⭐ PFC HAS 5 ROLES DEPENDING ON CONTEXT — USE THE RIGHT ROLE:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Role Label              │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ ① PFC = Observer        │ PFC OBSERVES body-feedback output.       │
  │                         │ Reactive, NOT generative.                │
  │                         │ ~5% decisions, 95% body self-processes.  │
  │                         │ ⚠️ % = calibration anchor.               │
  │                         │ "Reads output, does not create output."  │
  │                         │ Use: when emphasizing PFC does NOT        │
  │                         │ control but only observes.               │
  │                         │ (Feeling.md, PFC-Function.md §1)         │
  │                         │                                          │
  │ ② PFC = Lawyer          │ PFC constructs narrative FOR body-base.  │
  │                         │ Post-hoc justification. Confabulation.   │
  │                         │ NOT neutral judge — advocates for body.  │
  │                         │ Body-need fires FIRST → PFC justifies    │
  │                         │ AFTER.                                   │
  │                         │ Use: when analyzing PFC narrative ≠      │
  │                         │ actual body-need.                        │
  │                         │ (PFC-Operations.md §10, Gazzaniga)       │
  │                         │                                          │
  │ ③ PFC = Director        │ PFC steers, does NOT compute directly.   │
  │   (Orchestrator)        │ Biases spreading activation. Chooses     │
  │                         │ direction.                               │
  │                         │ "Director sets direction, actors perform."│
  │                         │ Use: when emphasizing PFC only BIASES,   │
  │                         │ does not carry out computation.          │
  │                         │ (Neural-Processing-Flow)                 │
  │                         │                                          │
  │ ④ PFC = Universal       │ PFC budget = FINITE, SHARED for ALL.     │
  │   Resource              │ Learning, Self-Pattern-Modeling,         │
  │                         │ decisions, suppress, social, self-       │
  │                         │ monitor, Imagine-Final.                  │
  │                         │ Fatigue from work → weaker Self-Pattern- │
  │                         │ Modeling with one's child.               │
  │                         │ Use: when analyzing PFC budget trade-off │
  │                         │ across activities.                       │
  │                         │ (PFC-Operations.md §9)                   │
  │                         │                                          │
  │ ⑤ PFC = Quality         │ Dual Check: body = quality controller,   │
  │   Controller            │ domain = final arbiter.                  │
  │                         │ PFC checks body output AGAINST domain    │
  │                         │ reality. THE ONLY system that can check  │
  │                         │ against domain.                          │
  │                         │ Use: when emphasizing PFC verify         │
  │                         │ function.                                │
  │                         │ (Ask-AI v3.1 §6.1)                      │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ 5 roles do NOT CONFLICT — same PFC, DIFFERENT PERSPECTIVES:
     Observer = perspective (what PFC reads)
     Lawyer = output quality (whom PFC justifies for)
     Director = mechanism (how PFC influences)
     Universal Resource = resource constraint (how PFC is limited)
     Quality Controller = verification function (what PFC checks)

  ⚠️ Do NOT use "PFC = controller" or "PFC = boss":
     PFC does NOT control the body. Body processes 95% automatically.
     PFC only BIASES direction + OBSERVES output.
```

---

## §3 — PROCESSING SPECTRUM: COMPILED ←→ FRESH

> PFC-Operations.md v1.0 §1 = full treatment.
> Body-Feedback-Label v2.0 §8 = same labels from the body side.
> This section = BRIEF label reference.

```
⭐ THE REAL PROCESSING AXIS = COMPILATION LEVEL:

  COMPILED ─────────────────────────────────────── FRESH
  (automatic)                                    (PFC-mediated)
  body-direct                                    deliberate
  cost ≈ 0                                      cost > 0
  "feels known"                                 "have to think"
  Hebbian reinforced                            each instance = new effort


  ┌─────────┬─────────────────────────┬──────────────────────────────────┐
  │ Tier    │ Label                   │ Meaning                         │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ processing              │ Most general. PFC involved.      │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ Compiled processing     │ Automatic. Body-direct. Cost ≈ 0.│
  │         │ Fresh processing        │ PFC-mediated. Deliberate.        │
  │         │ Semi-compiled           │ Mixed: part compiled, part fresh.│
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ Fresh → Compiled        │ LEARNING: repeat + verify OK.   │
  │ (trans.)│ (learning)              │ = "Logic → feeling" (observer).  │
  │         │ Compiled → Fresh        │ DISRUPTION: new context, error.  │
  │         │ (disruption)            │ = "Feeling → logic" (observer).  │
  └─────────┴─────────────────────────┴──────────────────────────────────┘

  ⚠️ "Compiled/Fresh" = MECHANISM AXIS. "Logic/Feeling" = OBSERVER LABELS.
     When analyzing mechanism: MUST use Compiled/Fresh.
     When describing to general audience: "Logic/Feeling" is OK
     (but recognize it is approximate).

  ⚠️ Spectrum, NOT binary:
     Each chunk sits SOMEWHERE on the spectrum.
     "Expert partially stuck" = compiled on the familiar part, fresh on the new part.

  (Body-Feedback-Label §8 = SAME labels. PFC-Operations.md §1 = SOURCE.)
```

---

## §4 — PFC OPERATIONS: HOLD + SUPPRESS

> PFC-Operations.md v1.0 §2-§4 = full mechanism.
> This section = LABEL reference only.

```
⭐ PFC HAS 2 OPERATIONS ON THE SPECTRUM:

  ┌─────────┬─────────────────────────┬──────────────────────────────────┐
  │ Tier    │ Label                   │ Meaning                         │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ PFC operation           │ Most general. PFC is acting.     │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ HOLD (= PFC Amplify)    │ Amplify new/weak pattern.        │
  │         │                         │ CAN compile → sustainable.       │
  │         │                         │ Cost: ① PFC draft.               │
  │         │                         │ Region: dlPFC, FEF.              │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ SUPPRESS (= PFC Inhibit)│ Block already-compiled pattern.  │
  │         │                         │ CANNOT compile "not" → unsust.   │
  │         │                         │ Cost: ② Suppress (efference).    │
  │         │                         │ Region: rIFG, vlPFC.             │
  └─────────┴─────────────────────────┴──────────────────────────────────┘

  ⚠️ HOLD ≠ SUPPRESS — FUNDAMENTALLY DIFFERENT:

    ┌──────────────┬────────────────────┬────────────────────┐
    │              │ HOLD               │ SUPPRESS            │
    ├──────────────┼────────────────────┼────────────────────┤
    │ Direction    │ BOOST new          │ BLOCK existing      │
    │ Body feels   │ "Effort" (neutral) │ "Not being me"      │
    │ Compile?     │ CAN compile new    │ Cannot compile "not"│
    │ Sustainable  │ Yes (→compile→free)│ No (cost persists)  │
    │ Cost source  │ ① PFC draft       │ ② Efference mismatch│
    └──────────────┴────────────────────┴────────────────────┘


  4 COMBINATIONS:

    ① Hold only       — Learn new, no conflict. Cost: ①. EASIEST.
    ② Hold + Suppress — Learn new WHILE blocking old. Cost: ① + ②. DOUBLE.
                         3 outcomes: A (genuine shift), B (compiled suppress),
                         C (failure/burst). (PFC-Operations.md §4)
    ③ Suppress only   — Block without replacing. Cost: ②. WORST.
                         Wegner ironic process: rebound.
    ④ Neither         — Compiled runs automatically. Cost: ≈ 0. No PFC.

  PFC OPERATIONS × DISSONANCE TYPE (Dissonance-Signal-Architecture.md v1.0 §7.2):

    ┌──────────────────┬──────────────────────┬─────────────────────────┐
    │                  │ Evaluative Dissonance│ Direct-State Dissonance │
    ├──────────────────┼──────────────────────┼─────────────────────────┤
    │ HOLD (reframe)   │ CAN compile new     │ MINIMAL effect          │
    │                  │ → resolve source      │ (pain stays pain)       │
    │ SUPPRESS (block) │ Partial, temporary   │ NEAR ZERO               │
    │                  │ → rebound risk        │ (hardware overrides)    │
    │ Placebo effect   │ N/A                  │ Evaluative modulates    │
    │                  │                      │ Direct-State (proof)    │
    └──────────────────┴──────────────────────┴─────────────────────────┘
    → PFC STRONGER with Evaluative Dissonance, WEAKER with Direct-State.
    → Parallel: PFC Hold/Suppress × Reward (Dissonance-Signal-Architecture §7.2 = full table).

  (PFC-Operations.md §2-§4 = SOURCE mechanism detail.)
```

---

## §5 — PFC COST LABELS

> PFC-Operations.md v1.0 §9-§10 = full mechanism.
> Body-Feedback-Label v2.0 §9C = same labels from the body side.
> This section = LABEL reference only.

```
⭐ 3 INDEPENDENT COST SOURCES + BUDGET:

  ┌─────────┬─────────────────────────┬──────────────────────────────────┐
  │ Tier    │ Label                   │ Meaning                         │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ PFC cost                │ Most general. PFC is spending.   │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ ① PFC draft cost        │ Processing load from HOLD.        │
  │         │                         │ f(chain_length × novelty).        │
  │         │                         │ DECREASES as chunk compiles       │
  │         │                         │ (→ ≈ 0 when compiled).           │
  │         │                         │ Region: dlPFC, FEF.              │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ ② Suppress cost         │ Efference mismatch from SUPPRESS. │
  │         │                         │ f(intensity × duration).          │
  │         │                         │ DOES NOT DECREASE (pattern still  │
  │         │                         │ fires). = "Not being me" feeling. │
  │         │                         │ Region: rIFG, vlPFC.             │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ ③ Uncertainty cost      │ Multiple options, none compiled.  │
  │         │                         │ Holds open → cortisol.            │
  │         │                         │ f(options × time × stakes).       │
  │         │                         │ DECREASES when committed           │
  │         │                         │ (choose 1 → hold).               │
  │         │                         │ Region: ACC (conflict).           │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ PFC budget              │ TOTAL resource PFC can use.      │
  │ (system)│ (= Universal Resource)  │ FINITE. SHARED for ALL activities:│
  │         │                         │ learning, Self-Pattern-Modeling,  │
  │         │                         │ decisions, suppress, social,      │
  │         │                         │ self-monitor, Imagine-Final.      │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ Total cost              │ = ① + ② + ③ combined.            │
  └─────────┴─────────────────────────┴──────────────────────────────────┘

  ⚠️ 3 cost sources INDEPENDENT (can appear separately or simultaneously):
     Only ① = learning something new (effort but manageable)
     Only ② = suppressing something old (draining and unsustainable)
     ① + ② = changing a habit (double cost — WHY change is hard)
     ① + ② + ③ = changing careers without knowing where to go (TRIPLE — max load)

  ⚠️ PFC budget REDUCED by:
     Fatigue (end of day), Cortisol (stress), Sleep deprivation,
     Illness, Chronic suppress (accumulated ② cost)
     → "Fatigue from work → weaker Self-Pattern-Modeling with one's child"
     = budget DEPLETED, not laziness.

  ⚠️ ① CAN DECREASE (compile → automatic). ② CANNOT DECREASE (pattern stays).
     → Long-term: HOLD-heavy strategies >> SUPPRESS-heavy strategies.

  (PFC-Operations.md §9-§10 = SOURCE. Body-Feedback-Label §9C = SAME labels.)
```

---

## §6 — COMPILED QUALITY LABELS

> PFC-Operations.md v1.0 §5 = full mechanism.
> This section = LABEL reference only.

```
⭐ COMPILED CHUNKS HAVE A QUALITY DIMENSION — DISTINGUISH 3 TYPES:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Genuine-compiled        │ REAL body reward confirmed → compile.    │
  │                         │ → approach tag.                          │
  │                         │ → Self-Pattern-Modeling EXPANSIVE        │
  │                         │   (rich body data).                      │
  │                         │ Example: A parent who genuinely enjoys   │
  │                         │ cooking → genuine-compiled understanding  │
  │                         │ of "what tastes good" → creative         │
  │                         │ Self-Pattern-Modeling with their child.  │
  │                         │ Use: when compiled through real          │
  │                         │ experience + body confirmation.          │
  │                         │                                          │
  │ Schema-compiled         │ PFC / obligation / social compliance.    │
  │                         │ → neutral tag.                           │
  │                         │ → Self-Pattern-Modeling LIMITED          │
  │                         │   (narrow, rule-based).                  │
  │                         │ Example: "Everyone studies" → compiles   │
  │                         │ HOW TO do it but does NOT compile WHY    │
  │                         │ body likes it.                           │
  │                         │ Use: when compiled through rule/schema,  │
  │                         │ not through body engagement.             │
  │                         │                                          │
  │ Threat-compiled         │ Forced / threatened / coerced → compile. │
  │                         │ → avoidance tag.                         │
  │                         │ → Self-Pattern-Modeling BIASED           │
  │                         │   (fear-based patterns).                 │
  │                         │ Example: Being punished → compiles       │
  │                         │ "don't speak up" → Self-Pattern-Modeling:│
  │                         │ predicts others will punish.             │
  │                         │ Use: when compiled under pressure/threat.│
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⭐ QUALITY = COMPILE-TIME LOCK:
    Tag (approach/neutral/avoidance) is assigned AT COMPILE TIME.
    After compiling → tag DOES NOT CHANGE.
    Same knowledge, same compile level — DIFFERENT quality → DIFFERENT for life.

  ⚠️ SAME OUTPUT, DIFFERENT QUALITY:
    Genuine-compiled "knows how to cook" ≠ Schema-compiled "knows how to cook"
    Genuine: rich body data → CAN generalize → creative
    Schema: rule data only → CANNOT generalize → repeats the same patterns

  ⚠️ 3 quality types are NOT changeable → must BUILD NEW (genuine) alongside.
    "Fixing" threat-compiled ≠ erasing → compile ADDITIONAL genuine patterns.

  (PFC-Operations.md §5 = SOURCE detail.)
```

---

## §7 — PFC REGION LABELS

```
⭐ PFC REGIONS AND THEIR FRAMEWORK MAPPING:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Region Label            │ Framework mapping + when to use          │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ dlPFC                   │ Working memory. Planning. Cognitive      │
  │ (dorsolateral PFC)      │ control. ~4±1 dimensions.                │
  │                         │ = HOLD operation hub.                    │
  │                         │ Use: when tracing HOLD to specific       │
  │                         │ region.                                  │
  │                         │                                          │
  │ vlPFC                   │ Response inhibition. Rule maintenance.   │
  │ (ventrolateral PFC)     │ = SUPPRESS operation hub.                │
  │                         │ Use: when tracing SUPPRESS to region.    │
  │                         │                                          │
  │ vmPFC                   │ Emotion regulation. Somatic bridge.      │
  │ (ventromedial PFC)      │ Amygdala connection (uncinate fasciculus)│
  │                         │ Controllability: vmPFC suppresses DRN.   │
  │                         │ Cortisol damage → vmPFC weakens →        │
  │                         │ DRN regains → learned helplessness.      │
  │                         │ Use: when tracing emotion regulation,    │
  │                         │ autonomy, controllability.               │
  │                         │ (Autonomy-Hardware.md v1.1)              │
  │                         │                                          │
  │ mPFC                    │ Self-model. Social cognition. DMN hub.   │
  │ (medial PFC)            │ Simulation-Engine Component 3:           │
  │                         │   Ventral = self + close others          │
  │                         │   Dorsal = dissimilar others             │
  │                         │ = GRADIENT (not binary).                 │
  │                         │ Entity-Compiled = migration from         │
  │                         │ dorsal → ventral.                        │
  │                         │ Use: when tracing Self-Pattern-Modeling, │
  │                         │ self-model, social prediction.           │
  │                         │ (Simulation-Engine.md v1.0 §6)           │
  │                         │                                          │
  │ rIFG                    │ Inhibitory control hub.                  │
  │ (right inferior         │ Specific region WITHIN vlPFC area.       │
  │  frontal gyrus)         │ = SUPPRESS execution point.              │
  │                         │ Use: when precise anatomical label is    │
  │                         │ needed.                                  │
  │                         │ (Aron 2007)                              │
  │                         │                                          │
  │ ACC                     │ Conflict monitoring. Error detection.    │
  │ (anterior cingulate     │ PFC/limbic OVERLAP (not pure PFC).       │
  │  cortex)                │ = ③ Uncertainty cost detector.           │
  │                         │ Fires when multiple options conflict.    │
  │                         │ Use: when tracing conflict/uncertainty.  │
  │                         │                                          │
  │ OFC                     │ Value computation. Reward expectation.   │
  │ (orbitofrontal cortex)  │ Integrates reward history.               │
  │                         │ Use: when tracing value judgment.        │
  │                         │                                          │
  │ FEF                     │ Attention direction. Eye movement.       │
  │ (frontal eye fields)    │ = HOLD attention component.              │
  │                         │ Use: when tracing attention allocation.  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ GAP FROM REGION → FRAMEWORK CONCEPT:
    Region = physical structure. Framework concept = functional label.
    MAPPING may NOT be 1:1 (1 region → many functions, 1 function → many regions).
    Use region labels when PRECISION is needed. Framework labels when ANALYZING.

  ⚠️ Use TIER 2 (HOLD/SUPPRESS) instead of Tier 3 (dlPFC/rIFG) in MOST cases.
    Region labels needed only when:
    → Research citation (anatomy specification required)
    → Neural damage analysis (lesion → which function lost)
    → Cross-referencing neuroscience literature
```

---

## §8 — PFC HARDWARE LABELS

```
⭐ INDIVIDUAL DIFFERENCES — WHY SAME 24 FUNCTIONS PRODUCE DIFFERENT OUTPUTS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ PFC hardware            │ Innate specs: wiring, receptors,         │
  │                         │ connection density. = WHAT DOES NOT      │
  │                         │ CHANGE (or changes extremely slowly).    │
  │                         │ Use: general term for individual         │
  │                         │ differences.                             │
  │                         │ (PFC-Hardware.md v1.1)                   │
  │                         │                                          │
  │ PFC quality             │ Workspace quality PER-SLOT:              │
  │ (= PFC-Quality)         │ ① Resolution (sharp or blurred)         │
  │                         │ ② Noise filter (stays clean despite      │
  │                         │   interference)                          │
  │                         │ ③ Retrieval (fast/accurate chunk access) │
  │                         │ ④ Compression (compiles more tightly)   │
  │                         │ Use: when analyzing processing quality.  │
  │                         │                                          │
  │ PFC clear speed         │ COMT-dependent. Speed of clearing old    │
  │ (= COMT clear)          │ drafts.                                  │
  │                         │ Val/Val: FAST = "Improviser"             │
  │                         │   (flexible, fast switching, unstable).  │
  │                         │ Met/Met: SLOW = "Specialist"             │
  │                         │   (focused, deep, incremental).          │
  │                         │ Val/Met: intermediate.                   │
  │                         │ Use: when analyzing processing speed.    │
  │                         │ (PFC-Hardware.md §3)                     │
  │                         │                                          │
  │ PFC slots               │ ~4±1 dimensions (NOT separate boxes).    │
  │ (= working memory       │ Interference limit (physics constraint). │
  │  dimensions)            │ NUMBER of slots SAME for EVERYONE        │
  │                         │ (hardware). QUALITY per-slot differs     │
  │                         │ (PFC quality). Compiled chunks: pyramidal│
  │                         │ stacking → experts fit MORE in same      │
  │                         │ slots.                                   │
  │                         │ Use: when analyzing working memory.      │
  │                         │ (PFC-Hold-Dimensions.md)                 │
  │                         │                                          │
  │ DRD4 filter             │ Receptor threshold for prediction-delta. │
  │ (= chunk threshold)     │ 4R: sensitive (small delta detected).    │
  │                         │ 7R: coarse (only large delta).           │
  │                         │ Use: when analyzing sensitivity.         │
  │                         │ (PFC-Hardware.md §4)                     │
  │                         │                                          │
  │ NE α2/α1                │ PFC circuit breaker under stress.        │
  │ (= stress threshold)    │ Normal: α2 (low NE) → PFC functions.    │
  │                         │ Stress: α1 (high NE) → PFC DISCONNECT.  │
  │                         │ Individual threshold varies.             │
  │                         │ Use: when analyzing PFC under stress.    │
  │                         │ (PFC-Hardware.md §6, Arnsten 2009)       │
  │                         │                                          │
  │ MAO-A                   │ Mood stability (WHOLE BRAIN, not         │
  │ (= mood stability)      │ PFC-only). Serotonin + dopamine + NE     │
  │                         │ metabolism.                              │
  │                         │ Use: when analyzing emotional stability. │
  │                         │ (PFC-Hardware.md §5)                     │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ "Improviser" vs "Specialist" = NOT BETTER/WORSE — just DIFFERENT profiles.
  ⚠️ PFC capacity DECREASES with: age, cortisol, fatigue, sleep deprivation.
     Observed capacity = hardware ceiling × current state.
  ⚠️ "IQ" NOT USED in framework — too crude.
     Use: PFC quality + clear speed + DRD4 + compiled chunks = richer model.
```

---

## §9 — SIMULATION-ENGINE LABELS

> Simulation-Engine.md v1.0 = full architecture.
> This section = LABEL reference only.

```
⭐ 1 ENGINE, 3 COMPONENTS, N APPLICATIONS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Simulation-Engine       │ General-purpose brain substrate.         │
  │                         │ DMN + mPFC + anterior insula +           │
  │                         │ hippocampus. Retrieve → recombine →      │
  │                         │ simulate → readout.                      │
  │                         │ Use: when referring to the shared        │
  │                         │ substrate for Self-Pattern-Modeling,     │
  │                         │ Self-Observation, Imagine-Final, etc.    │
  │                         │                                          │
  │ Component 1:            │ Anterior insula. Reads body signals.     │
  │ Interoception           │ "THE SCREEN" — readout device.           │
  │                         │ Unique to self-target.                   │
  │                         │ Use: when tracing body-signal readout.   │
  │                         │                                          │
  │ Component 2:            │ DMN + hippocampus. Recombines chunks.    │
  │ Constructive Simulation │ "CPU + RAM" — processing engine.         │
  │                         │ Use: when tracing simulation generation. │
  │                         │                                          │
  │ Component 3:            │ mPFC gradient. Ventral=self+close,       │
  │ Self/Other Model        │ Dorsal=distant. "CONTROL PANEL" —        │
  │                         │ selects simulation target.               │
  │                         │ Use: when tracing target selection.      │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  3 AXES (coordinates):

    Axis A — Target:    Self ←→ Close Other ←→ Far Other.
                         Gradient ventral → dorsal mPFC.

    Axis B — Time:      Past ← Present → Future (+ Counterfactual)

    Axis C — Operation: Observe ← Simulate → Evaluate/Construct.


  NAMED APPLICATIONS = SPECIFIC COORDINATES in 3D space:

    Self-Pattern-Modeling  = (Other, Present, Simulate).
    Self-Observation       = (Self, Present, Observe).
    Imagine-Final          = (Self, Future, Simulate).
    Memory recall          = (Self, Past, Observe).
    Counterfactual         = (Self, Alt-Past, Simulate).
    Empathy simulation     = (Other, Present, Observe+Simulate).

  ⚠️ Training 1 component = improves ALL applications (shared substrate).
  ⚠️ Damaging 1 component = degrades ALL applications (alexithymia = proof).
  ⚠️ Named applications = POINTS — unnamed apps are equally real.

  (Simulation-Engine.md v1.0 = SOURCE detail.)


  SELF-OBSERVATION GRADIENT (Self-Observation.md v1.0 §4):

    Level 0: Body-React           [NO PFC]          Hardware reflex
    Level 1: Body-Detect          [MINIMAL PFC]     "Something is there"
    ─── BOUNDARY: GAP between signal and response ───
    Level 2: Body-Recognize       [LOW-MID PFC]     "I know I am X"
    Level 3: Body-Predict         [MIDDLE PFC]      "Soon I will Y"
    Level 4: Pattern-Observe      [MID-HIGH PFC]    "I often X when Y"
    Level 5: Meta-Observe         [HIGH PFC]        "I am observing my observation"
    Level 6: Calibrated-Observe   [HIGH+COMPILED]   "Can I trust this observation?"

    Boundary Level 1→2 = Self-Observation begins when there is a GAP
    between signal and response (PFC encodes state SEPARATELY from response).
    Level 2 = most basic true Self-Observation = Body-Knowing Inward.
```

---

## §10 — PFC COGNITIVE LABELS

```
⭐ VOCABULARY FOR SPECIFIC PFC COGNITIVE OPERATIONS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ PFC spotlight           │ Attention allocation. = VOLUME INCREASE  │
  │ (= attention allocation)│ in target region, NOT a command.         │
  │                         │ Bottom-up (dopamine) or top-down (PFC).  │
  │                         │ "Increases volume, does not command      │
  │                         │  computation."                           │
  │                         │ Use: when describing PFC selecting what  │
  │                         │ to attend to.                            │
  │                         │ (PFC-Hardware.md, Neural-Processing-Flow)│
  │                         │                                          │
  │ PFC narrative           │ Post-hoc verbal explanation.             │
  │                         │ MAY confabulate (PFC = Lawyer).          │
  │                         │ Body-need fires FIRST → PFC justifies    │
  │                         │ AFTER. = Feel-Explanation (Explained —   │
  │                         │ lossy).                                  │
  │                         │ Use: when analyzing explanation ≠ cause. │
  │                         │ (Logic-Feeling-Balance.md)               │
  │                         │                                          │
  │ Labeling                │ PFC assigns verbal chunk (word) to body  │
  │ (= verbal coding)       │ pattern. Fidelity DECREASES 40-80%.      │
  │                         │ "Pleasant" = label FOR body-base reward  │
  │                         │ — lossy representation.                  │
  │                         │ Use: when analyzing PFC label ≠ body     │
  │                         │ experience.                              │
  │                         │ (Feeling.md, Blackbox-Map.md)            │
  │                         │                                          │
  │ PFC check               │ PFC verifies output with domain reality. │
  │ (= domain verification) │ = Quality Controller function (§2 ⑤).   │
  │                         │ THE ONLY system that checks against      │
  │                         │ domain.                                  │
  │                         │ Dual Check: body + domain = 2 layers.    │
  │                         │ Use: when describing verification        │
  │                         │ process.                                 │
  │                         │ (Ask-AI v3.1)                            │
  │                         │                                          │
  │ Working memory          │ PFC maintains chunks active.             │
  │ compression             │ BEFORE compile: 5 separate slots needed. │
  │                         │ AFTER compile: 1 meta-chunk slot.        │
  │                         │ Expert: pyramidal stacking → more chunks │
  │                         │ in same ~4±1 slots.                      │
  │                         │ Use: when analyzing expertise ≠ IQ.      │
  │                         │ (Neural-Processing-Flow.md)              │
  │                         │                                          │
  │ Somatic-Articulation    │ Recursive loop: body pattern → external  │
  │ Loop                    │ articulation → body verify → refine.     │
  │                         │ PFC seeks words to match body-known.     │
  │                         │ AI catalyst CAN accelerate the loop.     │
  │                         │ Use: when describing "knows but cannot   │
  │                         │ yet express" → articulation process.     │
  │                         │ (Somatic-Articulation-Loop.md)           │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ PFC spotlight ≠ attention (general):
     PFC spotlight = PFC's specific mechanism of amplification.
     Attention (general) = umbrella term covering both bottom-up + top-down.

  ⚠️ PFC narrative ≠ PFC check:
     Narrative = EXPLAIN (may confabulate — Lawyer function).
     Check = VERIFY (against domain — Quality Controller function).
     Explaining ≠ Checking. "Why?" ≠ "Is it correct?"
```

---

## §11 — PFC FAILURE MODES

```
⭐ 5 FAILURE PATTERNS — LABELS FOR RECOGNITION:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Failure Label           │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ ① Lawyer failure        │ PFC narrative ≠ body truth.              │
  │   (confabulation)       │ PFC justifies body-need with WRONG logic.│
  │                         │ "I'm sad because of XYZ" → actually body │
  │                         │ is tired + hungry + stressed → any        │
  │                         │ trigger → PFC mislabels.                 │
  │                         │ Use: when explanation ≠ actual cause.    │
  │                         │                                          │
  │ ② Philosopher trap      │ PFC imagines extensively but NEVER       │
  │                         │ checks domain → confident but WRONG.     │
  │                         │ "Overthinking" without verifying.        │
  │                         │ Use: when analyzing excessive reasoning  │
  │                         │ without domain feedback.                 │
  │                         │ (Discovery-vs-Expansion.md)              │
  │                         │                                          │
  │ ③ Budget overload       │ PFC budget exceeded → quality DROPS      │
  │   (depletion)           │ ACROSS ALL activities.                   │
  │                         │ "Fatigue from work → weaker Self-Pattern-│
  │                         │ Modeling with one's child."              │
  │                         │ NOT "laziness" — PFC budget = finite.    │
  │                         │ Use: when analyzing performance drop     │
  │                         │ after sustained PFC use.                 │
  │                         │                                          │
  │ ④ Suppress escalation   │ Too many domains suppressed → reward     │
  │   (→ learned            │ pathways NARROW → cortisol ↑ →          │
  │    helplessness)        │ vmPFC structural damage → DRN regains →  │
  │                         │ passive for EVERYTHING.                  │
  │                         │ Compiled suppress = DOOR closed.         │
  │                         │ Enough doors closed → room goes DARK.   │
  │                         │ Use: when tracing from local suppress →  │
  │                         │ global helplessness.                     │
  │                         │ (PFC-Operations.md §8)                   │
  │                         │                                          │
  │ ⑤ Cortisol disconnect   │ Chronic cortisol → NE α1 activates →    │
  │   (PFC offline)         │ PFC DISCONNECTS from body signals.       │
  │                         │ "Rage mode" / "freeze" / "numb."         │
  │                         │ PFC literally OFFLINE — not "weak will." │
  │                         │ Use: when PFC IS NOT FUNCTIONING         │
  │                         │ (stress/trauma response).                │
  │                         │ (PFC-Hardware.md §6, Arnsten 2009)       │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Failure modes = FOR RECOGNITION, not BLAME:
     "PFC failed" = structural/resource explanation, NOT moral judgment.
     Understanding the failure mode → target intervention correctly.
```

---

## §12 — OBSERVER vs MECHANISM LABELS

> Logic-Feeling.md v2.1 = full treatment.
> Body-Feedback-Label v2.0 §10 = same distinction from the body side.
> This section = BRIEF reference.

```
⭐ "LOGIC/FEELING" vs "COMPILED/FRESH" — 2 DISTINCT LAYERS:

  ┌──────────────────┬───────────────────────────────────────────────┐
  │ Layer            │ Labels + when to use                          │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ MECHANISM        │ Compiled / Fresh.                              │
  │ (the real axis)  │ = Processing level INSIDE the body.           │
  │                  │ Content (emotion/reasoning) does NOT           │
  │                  │ determine it. COMPILATION LEVEL determines it. │
  │                  │ Use: ALL deep analysis, research, mechanism   │
  │                  │ files. REQUIRED.                               │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ OBSERVATION      │ Logic / Feeling.                               │
  │ (observer labels)│ = OBSERVER perspective — looking from outside.│
  │                  │ "Logic" = compiled chunks that are SHAREABLE  │
  │                  │   (deterministic: math, physics).              │
  │                  │ "Intuition"/"Feeling" = compiled chunks        │
  │                  │   NOT EASILY SHAREABLE                         │
  │                  │   (probabilistic: psychology, interpersonal).  │
  │                  │ INTERNALLY: mechanism is IDENTICAL. Difference:│
  │                  │ SHAREABILITY, not quality.                     │
  │                  │ Use: describing to general audience.           │
  │                  │ Overview files.                                │
  └──────────────────┴───────────────────────────────────────────────┘


  USAGE RULES:

  ┌────────────────────────────┬───────────────────────────────────────┐
  │ Context                    │ Appropriate label                     │
  ├────────────────────────────┼───────────────────────────────────────┤
  │ Mechanism analysis:        │ Compiled / Fresh (CORRECT)            │
  │ Research / deep analysis:  │ Compiled / Fresh (REQUIRED)           │
  │ Describing to general      │ Logic / Feeling (OK, approximate)     │
  │ audience:                  │                                       │
  │ Observation parameter file:│ Logic-Feeling (filename, convention)  │
  │ Talking about humans in    │ PFC = Lawyer + Learning Trajectory    │
  │ general:                   │ = PFC serves body-base, learning →    │
  │                            │   Body-Knowing (compiled body-direct) │
  └────────────────────────────┴───────────────────────────────────────┘

  ⚠️ Do NOT say "feeling opposes logic":
    → Say "compiled pattern conflicts with fresh processing"
    → Because INTERNALLY there is no "feeling" vs "logic" — only compilation levels.

  ⚠️ "Intuition" = compiled processing (BOTH math AND emotion):
    A chef knowing salt is missing = intuition = COMPILED (not "feeling only")
    An expert mathematician "seeing" the solution = intuition = COMPILED (not "logic only")

  ⚠️ RETIRED: "Humans are 100% feeling at the foundational layer" — terminology collision
    (Logic-Feeling.md v4.0 §4.3: RETIRED. PFC = Lawyer + Learning Trajectory = same insight,
     mechanism-level, without the collision-prone word "feeling")

  (Logic-Feeling.md v4.0 = SOURCE. Body-Feedback-Label §10 = SAME distinction.)
```

---

## §13 — DEPRECATED TERMS + STANDARDIZATION

```
⭐⭐ TERMS TO DEPRECATE + REPLACEMENTS:

  ┌─────────────────────┬─────────────────────┬──────────────────────────┐
  │ DEPRECATED          │ REPLACEMENT         │ REASON                   │
  ├─────────────────────┼─────────────────────┼──────────────────────────┤
  │                     │                     │                          │
  │ "PFC-Fresh"         │ "Fresh processing"  │ Redundant. Fresh ALREADY │
  │                     │ or "Fresh"          │ implies PFC involvement. │
  │                     │                     │ "PFC-Fresh" = saying it  │
  │                     │                     │ twice.                   │
  │                     │                     │                          │
  │ "draft" (standalone │ STATE: "Fresh       │ "draft" is ambiguous —  │
  │  noun)              │  processing"        │ state? action? output?   │
  │                     │ ACTION: "HOLD" or   │ Mixes 3 levels.          │
  │                     │  "PFC HOLD"         │ Use "draft" ONLY when    │
  │                     │ SPECIFIC: "PFC draft│ it is a VERB + object:   │
  │                     │  novel path"        │ "PFC draft novel path."  │
  │                     │                     │                          │
  │ "thinking" (as      │ "Fresh processing"  │ "Thinking" is ambiguous  │
  │  mechanism label)   │                     │ — compiled intuition is  │
  │                     │                     │ also "thinking" in the   │
  │                     │                     │ broad sense.             │
  │                     │                     │                          │
  │ "willpower"         │ "PFC budget" or     │ "Willpower" implies      │
  │                     │ "SUPPRESS capacity" │ moral quality.           │
  │                     │                     │ PFC budget = structural  │
  │                     │                     │ resource, not virtue.    │
  │                     │                     │                          │
  │ "self-control"      │ "Active SUPPRESS"   │ Specify: active versus   │
  │ (without specifying │ or "Compiled        │ compiled suppress.       │
  │  which type)        │  SUPPRESS"          │ Different mechanism,     │
  │                     │                     │ different cost, different│
  │                     │                     │ sustainability.          │
  │                     │                     │                          │
  │ "PFC controls       │ "PFC biases/directs"│ PFC does NOT control     │
  │  body"              │                     │ the body. PFC biases     │
  │                     │                     │ direction.               │
  │                     │                     │ ~95% is automatic.       │
  │                     │                     │                          │
  │ "conscious          │ "Deliberate" or     │ "Conscious" is           │
  │  processing"        │ "Fresh processing"  │ misleading — compiled    │
  │                     │                     │ CAN also be "conscious"  │
  │                     │                     │ (aware of compiled       │
  │                     │                     │ output).                 │
  │                     │                     │                          │
  └─────────────────────┴─────────────────────┴──────────────────────────┘


  ⭐ STANDARDIZED TERMS (USE CONSISTENTLY):

  ┌────────────────────────────┬─────────────────────────────────────────┐
  │ Concept                    │ STANDARD LABEL                          │
  ├────────────────────────────┼─────────────────────────────────────────┤
  │ Spectrum position:         │ "Compiled" / "Fresh" / "Semi-compiled"  │
  │ PFC actions on spectrum:   │ "HOLD" / "SUPPRESS" / "PFC operations"  │
  │ What PFC does during HOLD: │ "PFC draft novel path" (verb + object)  │
  │ Cost from HOLD:            │ "① PFC draft cost"                      │
  │ Cost from SUPPRESS:        │ "② Suppress cost"                       │
  │ Cost from indecision:      │ "③ Uncertainty cost"                     │
  │ Total resource:            │ "PFC budget"                             │
  │ Individual differences:    │ "PFC hardware" (general)                │
  │ Processing speed:          │ "PFC clear speed" / "COMT"              │
  │ Sensitivity:               │ "DRD4 filter"                            │
  │ Attention mechanism:       │ "PFC spotlight"                          │
  │ Post-hoc explanation:      │ "PFC narrative"                          │
  │ Verbal coding:             │ "Labeling" (with fidelity loss noted)    │
  │ Domain verification:       │ "PFC check" / "Dual Check"              │
  │ Shared substrate:          │ "Simulation-Engine"                      │
  │ Compile quality:           │ "Genuine/Schema/Threat-compiled"         │
  │ Observer-level labels:     │ "Logic/Feeling" (with disclaimer)        │
  │ Mechanism-level labels:    │ "Compiled/Fresh" (REQUIRED for analysis) │
  └────────────────────────────┴─────────────────────────────────────────┘
```

---

## §14 — USAGE RULES

```
⭐ SUMMARY RULES:

  ① USE THE CORRECT LEVEL:
     State → "Fresh" / "Compiled" (position on spectrum)
     Operation → "HOLD" / "SUPPRESS" (action PFC performs)
     Sub-operation → "PFC draft novel path" (specific verb + object)
     Role → "Observer" / "Lawyer" / "Director" / etc. (depending on context)
     ✗ Do NOT mix: "PFC-Fresh operation" (mixes state + operation)

  ② COMPILED/FRESH FOR MECHANISM, LOGIC/FEELING FOR OBSERVATION:
     Deep analysis: "compiled conflicts with fresh" (CORRECT)
     ✗ "feeling opposes logic" (WRONG at mechanism level)
     Overview/description: "Logic vs Feeling" (OK, approximate)

  ③ SPECIFIC COST SOURCE:
     ✗ "PFC is drained" (too general — drained from what?)
     ✓ "① PFC draft cost is high due to novel learning"
     ✓ "② Suppress cost because suppressing a response"
     ✓ "① + ② double cost because changing a habit"

  ④ SPECIFY SUPPRESS TYPE:
     ✗ "suppressing" (active or compiled?)
     ✓ "Active suppress — PFC is actively blocking"
     ✓ "Compiled suppress — compiled into meta-pattern"

  ⑤ PFC BUDGET TRADE-OFF:
     When analyzing "why did performance drop":
     → Check: what was PFC budget already spent on before?
     → "Fatigue from work → weaker Self-Pattern-Modeling with child"
     = ④ Universal Resource

  ⑥ DO NOT BLAME — EXPLAIN THE MECHANISM:
     ✗ "No willpower" (moral judgment)
     ✓ "PFC budget depleted" or "② suppress cost unsustainable"
     ✗ "Lazy"
     ✓ "Compiled suppress → reward pathways narrowed → flat affect"

  ⑦ REGION LABELS ONLY WHEN NEEDED:
     Most cases → use Tier 2 (HOLD/SUPPRESS/PFC budget)
     Region (dlPFC/rIFG) → only for citation/anatomy/damage analysis

  ⑧ ROLE LABEL BY CONTEXT:
     Describing observation → PFC = Observer
     Analyzing narrative bias → PFC = Lawyer
     Explaining mechanism → PFC = Director
     Budget trade-off → PFC = Universal Resource
     Verification → PFC = Quality Controller
     Do NOT use multiple roles simultaneously (confusing) — choose the best fit.

  ⑨ RELATIONSHIP WITH BODY-FEEDBACK-LABEL:
     Body-Feedback-Label §8 already covers Compiled/Fresh processing labels.
     Body-Feedback-Label §9C already covers 3-cost labels.
     → This file SUPPLEMENTS: operations, roles, regions, hardware, failure modes.
     → Do NOT duplicate content — cross-reference.
     → Both files together → consistent vocabulary.
```

---

## §15 — HONEST ASSESSMENT

```
WHAT THIS FILE DOES WELL:

  ✓ Formalizes PFC vocabulary from 78+ files into 1 reference
  ✓ 3-tier system consistent with Body-Feedback-Label v2.0
  ✓ 4 vocabulary levels (Role/State/Operation/Sub-operation) clearly distinguished
  ✓ 5 PFC roles with context rules
  ✓ Deprecated terms with specific replacements
  ✓ Cross-ref strategy: SUPPLEMENTS, does not duplicate PFC-Operations /
    Simulation-Engine / Body-Feedback-Label


WHAT REMAINS UNCERTAIN:

  ? Region-to-function mapping may NOT be 1:1 — framework simplifies.
    Neuroscience continues refining these mappings.

  ? "~4±1 slots" — exact number still debated.
    Framework uses as approximate guide, not absolute.

  ❌ Ego depletion glucose model — FALSIFIED (Hagger 2016: d=0.04, Dang 2021).
    Framework uses "processing load" (serial bottleneck + catecholamine + allocation).
    Details: PFC-Operations.md v1.3 §8.3.

  ? PFC narrative confabulation — extent varies by individual.
    Framework uses "PFC = Lawyer" as a tendency, not 100% confabulation.


WHAT THIS FILE DOES NOT COVER:

  ✗ Mechanism detail (→ PFC-Operations.md v1.0)
  ✗ Simulation-Engine architecture (→ Simulation-Engine.md v1.0)
  ✗ Compiled/Fresh full spectrum (→ Logic-Feeling.md v2.1)
  ✗ Body-feedback vocabulary (→ Body-Feedback-Label v2.0)
  ✗ PFC 24 functions catalog (→ PFC-Function.md v1.2)
  ✗ PFC development trajectory (→ PFC-Development.md)
  ✗ PFC hardware individual differences mechanism (→ PFC-Hardware.md v1.1)
```

---

## §16 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Label v2.1         │ COMPANION. §8 Compiled/Fresh labels. │
  │                                  │ §9C 3-cost labels. This file         │
  │                                  │ SUPPLEMENTS.                         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Dissonance-Signal-Arch. v1.0     │ §7.2 PFC Operations × 2 dissonance  │
  │                                  │ types. SOURCE for §4 new table.      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Operations.md v1.0           │ SOURCE: §2-§4 Hold/Suppress, §5     │
  │                                  │ Quality, §8 Compiled Suppress, §9   │
  │                                  │ Budget, §10 3-Cost. MECHANISM file. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Simulation-Engine.md v1.0        │ SOURCE: §1-§3 Engine/Components/    │
  │                                  │ Axes. §6 mPFC gradient. §7          │
  │                                  │ Alexithymia. ARCHITECTURE file.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Logic-Feeling.md v2.1            │ Compiled/Fresh spectrum full         │
  │                                  │ treatment. Observer labels. SOURCE.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Function.md v1.2             │ 24 functions, 5 categories.         │
  │                                  │ SOURCE for "WHAT PFC does."         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Hardware.md v1.1             │ COMT, DRD4, NE, capacity/quality.   │
  │                                  │ SOURCE for §8 hardware labels.      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Hold-Dimensions.md           │ ~4±1 slots. Interference limit.     │
  │                                  │ SOURCE for "PFC slots" label.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Development.md               │ PFC lifetime trajectory. Training.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Ask-AI.md v3.1                   │ Dual Check: body = quality           │
  │                                  │ controller, domain = final arbiter. │
  │                                  │ SOURCE for §2 ⑤.                   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Feeling.md v3.0                  │ PFC observation of body-feedback.   │
  │                                  │ 7-layer gradient.                   │
  │                                  │ Feel-Explanation = lossy.           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Neural-Processing-Flow.md        │ PFC = Director/Orchestrator.        │
  │                                  │ Working memory compression.         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Somatic-Articulation-Loop.md     │ Somatic-Articulation-Loop:          │
  │                                  │ body → articulate → verify.         │
  │                                  │ PFC seeks words for body-known.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Autonomy-Hardware.md v1.1        │ vmPFC / DRN. Controllability.       │
  │                                  │ Compiled suppress → helplessness.   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.1        │ Cortisol × PFC damage. NE α1.      │
  │                                  │ SOURCE for §11 failure ⑤.          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Logic-Feeling-Balance.md         │ PFC = Lawyer. Domain = final        │
  │                                  │ arbiter. Meta-principle: neither    │
  │                                  │ 100%.                               │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Discovery-vs-Expansion.md        │ Philosopher trap. PFC imagines      │
  │                                  │ without domain check.               │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Self-Pattern-Modeling.md v3.1    │ APPLICATION-1 on Simulation-Engine. │
  │                                  │ Self-Pattern-Modeling =             │
  │                                  │ (Other, Present, Simulate).         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Imagine-Final.md v3.0            │ APPLICATION-2 on Simulation-Engine. │
  │                                  │ Imagine-Final = (Self, Future,      │
  │                                  │ Construct).                         │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

## §17 — RESEARCH CITATIONS

```
  ┌────┬──────────────────────────────────────────────┬─────────┬──────────┐
  │ #  │ Citation                                      │ Used in │ Evidence │
  ├────┼──────────────────────────────────────────────┼─────────┼──────────┤
  │ R1 │ Miller & Cohen 2001 — Integrative Theory PFC │ §4      │ 🟢      │
  │ R2 │ Baddeley 2003 — Working Memory                │ §4, §10 │ 🟢      │
  │ R3 │ Aron 2007 — rIFG Inhibitory Control           │ §4, §7  │ 🟢      │
  │ R4 │ Wegner 1987 — Ironic Process Mental Control   │ §4      │ 🟢      │
  │ R5 │ Kahneman 2011 — System 1/2                    │ §3      │ 🟢      │
  │ R6 │ Evans & Stanovich 2013 — Dual Process Theory  │ §3      │ 🟢      │
  │ R7 │ Klein 1998 — Naturalistic Decision Making     │ §3      │ 🟢      │
  │ R8 │ Gailliot & Baumeister 2007 — Glucose Depletion│ §10 (hist.)│ ❌ FALSIFIED │
  │ R9 │ Hagger et al. 2016 — Ego Depletion FAILED    │ §10     │ 🟢      │
  │ R10│ Maier & Seligman 2016 — Controllability       │ §7, §11 │ 🟢      │
  │ R11│ McEwen 2007 — Cortisol vmPFC Damage           │ §7, §11 │ 🟢      │
  │ R12│ Arnsten 2009 — PFC NE α1 Disconnect           │ §8, §11 │ 🟢      │
  │ R13│ Gazzaniga — Split-Brain Confabulation          │ §2      │ 🟢      │
  │ R14│ Schacter & Addis 2007 — Constructive Simulation│ §9     │ 🟢      │
  │ R15│ Buckner & Carroll 2007 — Self-Projection       │ §9      │ 🟢      │
  │ R16│ Mitchell 2006 — mPFC Self/Other Gradient       │ §7, §9  │ 🟢      │
  │ R17│ Tamir & Mitchell 2010 — Ventral/Dorsal mPFC    │ §9      │ 🟢      │
  │ R18│ Bird & Cook 2013 — Alexithymia                 │ §9      │ 🟢      │
  │ R19│ Lombardo 2010 — Shared Circuits Self/Other     │ §9      │ 🟢      │
  │ R20│ Lally et al. 2010 — Habit Formation            │ §3      │ 🟢      │
  │ R21│ Chase & Simon 1973 — Expertise Chunking        │ §3, §10 │ 🟢      │
  │ R22│ Anderson & Green 2001 — Think/No-Think         │ §4      │ 🟢      │
  │ R23│ Curtis & D'Esposito 2003 — PFC Sustained Firing│ §4      │ 🟢      │
  │ R24│ Inzlicht & Schmeichel 2012 — Motivational Acct │ §5      │ 🟢      │
  └────┴──────────────────────────────────────────────┴─────────┴──────────┘
```

---

**END OF FILE — PFC-Label v1.0 (24 citations, 17 sections)**

> *PFC-Label Convention v1.0 — Vocabulary Reference.*
> *Companion to Body-Feedback-Label v2.0.*
>
> *§2 Roles: Observer / Lawyer / Director / Universal Resource / Quality Controller.*
> *§3 Spectrum: Compiled ←→ Fresh (the real axis, not Logic/Feeling).*
> *§4 Operations: HOLD (amplify) / SUPPRESS (block) — 4 combinations, 3 outcomes.*
> *§5 Cost: ① PFC draft + ② Suppress + ③ Uncertainty. Budget = finite, shared.*
> *§6 Quality: Genuine / Schema / Threat — compile-time lock.*
> *§7-§8 Regions + Hardware: dlPFC, vlPFC, vmPFC, mPFC, COMT, DRD4.*
> *§9 Simulation-Engine: 1 engine, 3 components, 3 axes.*
> *§10-§11 Cognitive ops + Failure modes.*
> *§12 Observer vs Mechanism: Logic/Feeling ≠ Compiled/Fresh.*
> *§13 Deprecated: "PFC-Fresh", "draft" standalone, "willpower", "self-control" unspecified.*
> *§14 Rules: correct level, correct context, don't blame — explain the mechanism.*
