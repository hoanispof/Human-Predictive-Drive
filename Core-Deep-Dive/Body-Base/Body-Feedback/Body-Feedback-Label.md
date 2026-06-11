---
title: Body-Feedback Label Convention — Vocabulary Reference
version: 2.1
created: 2026-05-12
rewritten: 2026-05-17 (v2.0 — FULL REWRITE: +Foundation terms, +Compiled/Fresh processing, +Entity-Compiled 3 subtypes, +Inter-Body interaction labels, +5-Channel, +3-cost, +2-Stream)
updated: 2026-05-25 (v2.1 — §4 +Evaluative/Direct-State Dissonance labels at Tier 2+3, parallel §3 Reward structure, Dissonance-Signal-Architecture v1.0 integration)
previous: v1.1 → backup/Body-Feedback-Label-v1.1-backup.md
status: REFERENCE v2.1
scope: |
  VOCABULARY REFERENCE: Label conventions for the entire body-feedback system.
  Formalizes the 3-tier label system: General → Direction → Specific.
  This file = MUST-READ immediately after Body-Feedback.md.
  All files in the framework should use vocabulary per these conventions.
  100% FRAMEWORK VOCABULARY — no terminology outside the framework.
  v2.0 EXPANDED: 7 concept families (from Inter-Body drill):
    ① Foundation terms (body-need, gap, gap direction, drive)
    ② Entity-Compiled 3 subtypes (positive/negative/mixed)
    ③ Compiled/Fresh processing labels (the real axis)
    ④ By-product match / Anti-match
    ⑤ 2-Stream Architecture (Hardware-Stream / Modeling-Stream)
    ⑥ 3 Independent Cost Sources
    ⑦ 5-Channel Input Vector
purpose: |
  Framework analyzes body-feedback across 4 axes, 7-step mechanism,
  Evaluative/Direct-State, E₀→E₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles.
  v2.0: ADDS Foundation terms, Compiled/Fresh processing, Inter-Body interaction,
  Entity-Compiled multi-channel, 5-Channel Input, 3-cost.
  This file formalizes unified vocabulary for THE ENTIRE framework —
  covering both intra-body AND inter-body labels.
  Resolves:
    → "opioid confirm" only covers Evaluative, misses Direct-State
    → "pleasant/discomfort" conflates body-feedback (mechanism) with feeling (observation)
    → "Logic/Feeling" conflates observer labels with mechanism labels
    → Missing vocabulary for inter-body interaction
    → Foundation terms (body-need, gap) used everywhere but never formally defined
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — peer to Body-Feedback-Mechanism.md.
  READ IMMEDIATELY AFTER Body-Feedback.md (entry point).
dependencies:
  - Body-Feedback.md v2.0 — §2 dual-pull, §4 4 axes, §5 3 sources, §6 Body-Feedback-Precondition
  - Body-Feedback-Mechanism.md v2.0 — §1 Body-Need aggregate, §2 2 sources, §3 3 dynamics
  - Reward-Signal-Architecture.md v2.0 — §1 Evaluative/Direct-State, §2 E₀→E₃, §4 5 Profiles
  - Dissonance-Signal-Architecture.md v1.0 — §1 Evaluative/Direct-State Dissonance, §2 E₀→E₃ dissonance, §3 Evaluative Gates
  - 03-Reward.md v1.1 — §2 7-step mechanism, §3 Body-Feedback-Precondition, Step 5 body-base check
  - Cortisol-Baseline.md v2.0 — §7.7 5 Roles
  - Valence-Propagation.md v2.0 — §3 Entity-Compiled, approach/avoidance tags
  - Inter-Body-Mechanism.md v1.0 — §3 Compiled/Fresh, §4 3-cost, §5 by-product match, §6 5-Channel, §7 PFC=Lawyer, §8 Entity-Compiled
  - By-Product-Gap-Resonance.md v1.0 — §2 2-Stream Architecture
  - Feeling.md v2.2 — PFC observation of body-feedback (different layer)
  - Gap-Direction.md v2.0 — gap has direction = f(surrounding chunks)
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Label Convention — Vocabulary Reference

> **Framework analyzes body-feedback across 4 axes, 7-step mechanism,**
> **Evaluative/Direct-State, E₀→E₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles...**
>
> **PLUS: Foundation terms, Compiled/Fresh processing, Entity-Compiled 3 subtypes,**
> **By-product match, 2-Stream, 3-cost, 5-Channel Input Vector.**
>
> **Yet when WRITING/SPEAKING, labels were NEVER formalized.**
>
> **This file: LABEL CONVENTIONS for the entire framework.**
> **100% framework vocabulary. Read immediately after Body-Feedback.md.**

---

## Table of Contents

- §0 — WHY THIS FILE EXISTS
- §1 — 3-TIER LABEL SYSTEM
- §2 — FOUNDATION: BODY-NEED + GAP + DRIVE (★ NEW v2.0)
- §3 — POSITIVE: BODY-BASE REWARD LABELS
- §4 — NEGATIVE: DISSONANCE LABELS
- §5 — DETECTION: PREDICTION-DELTA LAYER (SEPARATE)
- §6 — NEUTRAL: BODY-FEEDBACK BASELINE
- §7 — COMPILED: VALENCE TAGS + ENTITY-COMPILED
- §8 — COMPILED/FRESH: PROCESSING LABELS (★ NEW v2.0)
- §9 — INTER-BODY: INTERACTION LABELS (★ NEW v2.0)
- §10 — OBSERVATION VS MECHANISM (DIFFERENT LAYERS)
- §11 — USAGE RULES
- §12 — CROSS-REFERENCES

---

## §0 — WHY THIS FILE EXISTS

```
⭐ THE FRAMEWORK HAS PRECISE MECHANISMS — MISSING: LABEL CONVENTIONS:

  Body-feedback system has:
    → 4 orthogonal classification axes (Body-Feedback-Mechanism.md §0)
    → 7-step mechanism from detection → reward (03-Reward.md §2)
    → Evaluative/Direct-State Reward distinction (Reward-Signal-Architecture.md §1)
    → E₀→E₃ complexity gradient + 5 Profiles
    → 3 chunk dynamics (Chunk-Shift/Miss/Gap)
    → 5 cortisol Roles (Cortisol-Baseline.md §7.7)

  v2.0 ADDED (from Inter-Body drill):
    → Foundation terms: body-need, gap, gap direction, drive (Inter-Body §2)
    → Compiled/Fresh = the real processing axis (Inter-Body §3)
    → Entity-Compiled 3 subtypes (Inter-Body §8, Valence-Propagation v2.0 §3)
    → By-product match + Anti-match (Inter-Body §5.4)
    → 2-Stream Architecture (By-Product-Gap-Resonance v1.0 §2)
    → 3 Independent Cost Sources (Inter-Body §4)
    → 5-Channel Input Vector (Inter-Body §6)

  BUT: no conventions for WHICH LABEL TO USE when writing/speaking.
  → Same phenomenon → 5 different terms → ambiguity


  4 SPECIFIC PROBLEMS:

  ① "OPIOID CONFIRM" ONLY COVERS EVALUATIVE REWARD:
    Evaluative Reward: μ-opioid → hedonic hotspot → CORRECT to say "opioid confirm"
    Direct-State Reward: CT afferents / endocannabinoid / thermoreceptor → NOT opioid
    → Correct general label = "body-base reward" (covers BOTH Evaluative AND Direct-State)
    (Reward-Signal-Architecture.md §1.1)

  ② CONFLATING BODY-FEEDBACK WITH FEELING:
    Body-feedback = MECHANISM (signal from body, runs 24/7, 95% unconscious)
    Feeling = OBSERVATION (PFC observes body-feedback → 7-layer gradient)
    "Pleasant" = feeling label (PFC has observed + labeled) — NOT a body-feedback label
    → §10 of this file draws this distinction clearly
    (Feeling.md v2.2)

  ③ "LOGIC / FEELING" CONFLATES OBSERVER LABELS WITH MECHANISM LABELS (v2.0 NEW):
    REAL INTERNAL AXIS = Compiled ←→ Fresh (compilation level)
    "Logic/Feeling" = observer perspective labels, NOT mechanism
    → §8 of this file formalizes processing labels
    (Inter-Body-Mechanism.md §3)

  ④ FOUNDATION TERMS USED EVERYWHERE BUT NEVER DEFINED (v2.0 NEW):
    "body-need", "gap", "gap direction" = appear HUNDREDS of times
    But never formalized in a single place
    → §2 of this file defines the foundation
    (Body-Feedback-Mechanism v2.0 §1, Inter-Body §2, Gap-Direction.md)


  ⭐ THIS FILE RESOLVES:
    → Formalizes unified vocabulary for the entire framework
    → 3-tier system: as specific as possible, as general as necessary
    → Foundation terms defined FIRST → all subsequent sections reference §2
    → Covers BOTH intra-body AND inter-body vocabulary
```

---

## §1 — 3-TIER LABEL SYSTEM

```
⭐ TIER SELECTION RULES:

  Tier 3 (MOST SPECIFIC) > Tier 2 (DIRECTION) > Tier 1 (MOST GENERAL)

  → When chain is TRACEABLE → use Tier 3
    "chunk-miss → SNC → cortisol Role ② Holding"

  → When DIRECTION + CHARACTER known but chain is complex → use Tier 2
    "body-base reward" / "dissonance" / "threat"

  → When ONLY knowing body response is +/- with no further specificity → use Tier 1
    "body-feedback positive" / "body-feedback negative"


  AUDIENCE-APPROPRIATE:

    Expert / deep analysis:
      → Tier 3 primary. Chain tracing explicit.

    Learning / Research files:
      → Tier 2 primary: "body-base reward", "dissonance", "chunk-miss"
      → Precise enough, sufficient for understanding basic mechanism

    General / overview:
      → Tier 1 when needed: "body-feedback positive/negative"
      → Can drill deeper if reader requests


  APPLIES TO ALL CATEGORIES (§2-§9):
    Every category has corresponding Tier 1/2/3.
    3-Tier logic = UNIVERSAL, applies to foundation, signal,
    processing, and inter-body labels alike.
```

---

## §2 — FOUNDATION: BODY-NEED + GAP + DRIVE (★ NEW v2.0)

```
⭐ FOUNDATIONAL TERMS — ALL SUBSEQUENT SECTIONS REFERENCE HERE:

  ┌─────────────────────────────────────────────────────────────────┐
  │ CONCEPTUAL FLOW:                                                 │
  │                                                                  │
  │   body-base (system)                                             │
  │       ↓ produces                                                 │
  │   body-need (aggregate state of NEED)                            │
  │       ↓ contains                                                 │
  │   gap + gap direction (specific chunks missing + direction)      │
  │       ↓ generates                                                │
  │   drive (pushes behavior to fill gap)                            │
  │       ↓ monitored by                                             │
  │   body-feedback (signals from body about current state — THIS FILE) │
  │                                                                  │
  └─────────────────────────────────────────────────────────────────┘


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A) BODY-BASE (the system):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ body-base               │ THE ENTIRE SYSTEM: hardware + compiled   │
  │                         │ + social. = The "body foundation"        │
  │                         │ encompassing everything the body has     │
  │                         │ accumulated and currently operates.      │
  │                         │ Compilable Architecture: general-purpose │
  │                         │ reward + compilation + social hardware.  │
  │                         │ Use: when referring to the system as a   │
  │                         │ whole.                                   │
  │                         │ (Body-Base.md v3.1, Inter-Body §1)      │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  B) BODY-NEED (aggregate state of NEED):

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Meaning + when to use                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-need           │ AGGREGATE state of current NEED.     │
  │(general)│                     │ Aggregates ALL signals currently      │
  │         │                     │ demanding body response.             │
  │         │                     │ NOT a single signal → is a TOTAL.    │
  │         │                     │ Exists BEFORE PFC awareness.         │
  │         │                     │ Use: when speaking generally about   │
  │         │                     │ "what the body needs."               │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ hardware body-need  │ Source ①: Sensory-Driven.            │
  │ (source)│                     │ Homeostatic + nociceptive + hormonal.│
  │         │                     │ Does NOT require compiled chunks.    │
  │         │                     │ Examples: hunger, thirst, pain, cold.│
  │         │                     │ Use: when body-need arises from      │
  │         │                     │ hardware.                            │
  │         │                     │                                      │
  │         │ pattern body-need   │ Source ②: Chunk Dynamics/Pattern.    │
  │         │                     │ Gap / Miss / Shift (+ Compound).     │
  │         │                     │ REQUIRES compiled chunks.            │
  │         │                     │ Examples: missing a close friend,    │
  │         │                     │ career gap, identity need.           │
  │         │                     │ Use: when body-need arises from      │
  │         │                     │ chunk firing.                        │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ (specific gaps)     │ Specific gap + specific direction.   │
  │(specific)│                    │ Examples:                            │
  │         │                     │ "gap survival [direction: food]"     │
  │         │                     │ "gap mastery [direction: mathematics]"│
  │         │                     │ "gap connection [direction: close    │
  │         │                     │  friend A]"                          │
  │         │                     │ Use: when the specific gap is        │
  │         │                     │ traceable.                           │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Body-need ALWAYS EXISTS (never = 0)
  ⚠️ Body-need = MULTIPLE simultaneously (parallel)
  ⚠️ Body-need HAS PRIORITY (intensity × urgency × state)
  ⚠️ PFC DOES NOT ALWAYS KNOW body-need (exists before awareness)
  ⚠️ 2 sources are NOT exclusive — 1 event activates BOTH ①+②
  (Inter-Body §2, Body-Feedback-Mechanism v2.0 §1)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  C) GAP + GAP DIRECTION (specific missing + direction):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ gap                     │ Chunk SHOULD exist but is MISSING.       │
  │                         │ Network predicts chunk C → C absent.     │
  │                         │ = A SPECIFIC component within body-need. │
  │                         │ Use: when describing "something specific  │
  │                         │ is missing."                             │
  │                         │                                          │
  │ gap direction           │ DIRECTION the gap points =               │
  │                         │ f(surrounding chunks).                   │
  │                         │ Only filling the RIGHT DIRECTION         │
  │                         │ produces reward.                         │
  │                         │ Each person has their OWN direction.     │
  │                         │ "Not yet knowing = no gap" (no           │
  │                         │ surrounding chunks yet = no direction).  │
  │                         │ Use: when describing HOW a gap needs to  │
  │                         │ be filled.                               │
  │                         │ (Gap-Direction.md v2.0)                  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ gap ≠ body-need:
     Gap = 1 specific missing chunk (component)
     Body-need = AGGREGATE of all gaps + hardware signals (total)
     1 body-need can contain MANY gaps in parallel
  ⚠️ "Not yet knowing = no gap" — gap ONLY exists when surrounding chunks
     HAVE compiled. A child has no "quantum physics" gap because the
     substrate does not exist yet.
  ⚠️ Gap direction = WHY by-product match works:
     B's output matches A's gap DIRECTION → A receives reward.
     Direction mismatch → no reward EVEN WITH output.


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  D) DRIVE (pushes behavior):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ drive                   │ Behavioral FORCE from body-need.         │
  │                         │ = Behavioral output from body-need →     │
  │                         │ → action to fill gap.                    │
  │                         │ Use: when describing "what PUSHES        │
  │                         │ behavior."                               │
  │                         │                                          │
  │ drive direction         │ = gap direction expressed as behavior.   │
  │                         │ Drive TOWARD (approach) or               │
  │                         │ AWAY FROM (avoidance).                   │
  │                         │ Use: when describing direction of        │
  │                         │ behavior.                                │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ drive ≠ body-need:
     Body-need = STATE (state of NEED — internal)
     Drive = OUTPUT (behavioral force — toward action)
     Body-need → drive (but PFC can suppress drive → cost ②)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  E) BODY-FEEDBACK (signal domain — umbrella term for THIS FILE):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ body-feedback           │ ALL signals from body about current      │
  │                         │ state. UMBRELLA TERM for everything      │
  │                         │ described in this file. Runs 24/7.       │
  │                         │ 95% unconscious.                         │
  │                         │ Includes: reward, dissonance, prediction-│
  │                         │ delta, baseline, valence tags...          │
  │                         │ ≠ Feeling (feeling = PFC OBSERVES body-  │
  │                         │ feedback — different layer, see §10).    │
  │                         │ Use: when speaking generally about "body │
  │                         │ sending signals."                        │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ body-feedback MONITORS body-need:
     Body-need = WHAT is needed. Body-feedback = WHAT body reports.
     Reward = "gap is being filled" (positive feedback)
     Dissonance = "gap NOT filled / being blocked" (negative feedback)
     → Body-feedback = COMMUNICATION CHANNEL, body-need = CONTENT
```

---

## §3 — POSITIVE: BODY-BASE REWARD LABELS

```
⭐ REWARD = BODY-BASE CONFIRM SIGNAL (body confirms: chunk MATCHES body-need)

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Meaning + when to use                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-feedback       │ Most general. Body responds          │
  │(general)│ positive            │ positively. Mechanism unspecified.   │
  │         │                     │ Use: when only knowing body          │
  │         │                     │ response is positive.                │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ body-base reward    │ Body confirms chunk matches          │
  │  (type) │                     │ body-need (§2). Covers both          │
  │         │                     │ Evaluative + Direct-State.           │
  │         │                     │ Use: when body confirmation is clear.│
  │         │                     │                                      │
  │         │ reward              │ Shorthand for body-base reward.      │
  │         │                     │ Use: when context ALREADY CLEAR as   │
  │         │                     │ body-feedback (no confusion risk).   │
  │         │                     │                                      │
  │         │ Evaluative Reward   │ Evaluative confirmation. Opioid-     │
  │         │                     │ based. Requires full Body-Feedback-  │
  │         │                     │ Precondition. Rich chunk library     │
  │         │                     │ needed.                              │
  │         │                     │ Use: when clearly evaluative.        │
  │         │                     │                                      │
  │         │ Direct-State Reward │ Direct state confirmation.           │
  │         │                     │ Non-opioid. Hardware-based.          │
  │         │                     │ Low habituation.                     │
  │         │                     │ Use: when clearly body-state.        │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ μ-opioid confirm    │ Evaluative. Hedonic hotspot pathway. │
  │(specific)│                    │ Use: when chain traced to NAcc/VP.   │
  │         │                     │                                      │
  │         │ CT afferent reward  │ Direct-State. Touch comfort pathway. │
  │         │                     │ ~1-10cm/s optimal (Löken 2009).      │
  │         │                     │                                      │
  │         │ endocannabinoid     │ Direct-State. Exercise/runner's high.│
  │         │ reward              │ CB1 pathway (Fuss 2015).             │
  │         │                     │                                      │
  │         │ E₀ / E₁ / E₂ / E₃  │ Evaluative complexity gradient.      │
  │         │                     │ E₀=hardware, E₃=expert evaluation.   │
  │         │                     │ (Reward-Signal-Architecture §2)      │
  │         │                     │                                      │
  │         │ Profile ①-⑤         │ 5 "flavors" of reward.               │
  │         │                     │ Sensory/Coherence/Social/Relief/     │
  │         │                     │ Preview.                             │
  │         │                     │ (Reward-Signal-Architecture §4)      │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ "opioid confirm" → use ONLY when specifically referring to Evaluative pathway
  ⚠️ "reward" in general → always covers BOTH Evaluative AND Direct-State
  ⚠️ Remember: reward = body confirms "gap is being filled in the right direction" (§2C)
     ≠ prediction-delta (detection signal — §5)
```

---

## §4 — NEGATIVE: DISSONANCE LABELS

```
⭐ DISSONANCE = BODY SIGNAL "MISMATCH" (mismatch / predicted harm / recalibration)

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Meaning + when to use                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-feedback       │ Most general. Body responds          │
  │(general)│ negative            │ negatively.                          │
  │         │                     │ Use: when only knowing body          │
  │         │                     │ response is negative.                │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ dissonance          │ Body detects mismatch (schema ≠      │
  │  (type) │                     │ reality). Drive works to resolve.    │
  │         │                     │ Use: when mismatch is clear.         │
  │         │                     │                                      │
  │         │ threat              │ Body predicts harm (predicted harm). │
  │         │                     │ Drive avoids.                        │
  │         │                     │ Use: when anticipation of harm is    │
  │         │                     │ clear.                               │
  │         │                     │ (Threat.md: 5 levels × 3 axes ×     │
  │         │                     │ 3 sources)                           │
  │         │                     │                                      │
  │         │ recalibration       │ Neurons adjusting pattern.           │
  │         │ dissonance          │ Transient, self-resolves when        │
  │         │                     │ adaptation completes.                │
  │         │                     │ Use: when discomfort arises from     │
  │         │                     │ learning/adjusting (not mismatch/    │
  │         │                     │ threat).                             │
  │         │                     │                                      │
  │         │ Evaluative          │ Compiled, conditional. dACC +        │
  │         │ Dissonance          │ anterior insula. PFC can modulate.   │
  │         │                     │ Develops with age + chunk library.   │
  │         │                     │ Use: when clearly evaluative         │
  │         │                     │ (social pain, moral injury, anxiety).│
  │         │                     │ (Dissonance-Signal-Architecture §1)  │
  │         │                     │                                      │
  │         │ Direct-State        │ Hardware, from birth. Nociceptors,   │
  │         │ Dissonance          │ thermoreceptors, visceral signals.   │
  │         │                     │ PFC minimal involvement.             │
  │         │                     │ Numbness-proof.                      │
  │         │                     │ Use: when clearly body-state         │
  │         │                     │ (pain, hunger, temperature, itch).   │
  │         │                     │ (Dissonance-Signal-Architecture §1)  │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ chunk-miss          │ Expected X, received <X.             │
  │(specific)│                    │ SNC mechanism.                       │
  │         │                     │ (Crespi 1942, Flaherty 1996)         │
  │         │                     │                                      │
  │         │ chunk-shift         │ Same chunks, DIFFERENT valence.      │
  │         │                     │ Context changes → re-evaluate.       │
  │         │                     │                                      │
  │         │ chunk-gap           │ = gap (§2C) being DETECTED as        │
  │         │                     │ dissonance signal. Chunk C should    │
  │         │                     │ exist but is missing → body fires    │
  │         │                     │ signal.                              │
  │         │                     │ (Gap-Direction.md: gap has direction)│
  │         │                     │                                      │
  │         │ SNC                 │ Successive Negative Contrast.        │
  │         │                     │ Specific chunk-miss: downshift from  │
  │         │                     │ high baseline → overreaction.        │
  │         │                     │                                      │
  │         │ nociception         │ Tissue damage signal. Hardware.      │
  │         │                     │ A-delta + C fibers.                  │
  │         │                     │                                      │
  │         │ substance P /       │ Direct-State. Nociception pathway.   │
  │         │ CGRP / glutamate    │ Pain transmission A-delta + C fibers.│
  │         │                     │ (Dissonance-Signal-Architecture §1.6)│
  │         │                     │                                      │
  │         │ dACC activation     │ Evaluative. Social pain pathway.     │
  │         │                     │ 🟢 Eisenberger 2003 (Cyberball).     │
  │         │                     │ (Dissonance-Signal-Architecture §1.6)│
  │         │                     │                                      │
  │         │ CRH → amygdala      │ Evaluative. Anxiety/threat pathway.  │
  │         │                     │ HPA axis → cortisol cascade.         │
  │         │                     │ (Dissonance-Signal-Architecture §1.6)│
  │         │                     │                                      │
  │         │ E₀→E₃ dissonance   │ Evaluative complexity gradient       │
  │         │                     │ applied to dissonance direction.     │
  │         │                     │ E₀=bitter aversion (hardware).       │
  │         │                     │ E₃=moral injury (expert evaluation). │
  │         │                     │ (Dissonance-Signal-Architecture §2)  │
  │         │                     │                                      │
  │         │ cortisol Role ①-⑤   │ Context-specific amplifier role:     │
  │         │                     │ ① Compile Direction                  │
  │         │                     │ ② Holding ("not yet done")           │
  │         │                     │ ③ Threat-sustained (chronic)         │
  │         │                     │ ④ Inertia (productive addiction)     │
  │         │                     │ ⑤ Silent (elevated but unfelt)       │
  │         │                     │ (Cortisol-Baseline.md §7.7)          │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Evaluative/Direct-State = ORTHOGONAL to source (dissonance/threat/recalibration)
     1 event can be BOTH "mismatch" (source) AND "Evaluative" (type)
     Example: betrayal = mismatch (source) + Evaluative Dissonance (type)
     Example: pin prick = nociception (source) + Direct-State Dissonance (type)
     (Dissonance-Signal-Architecture.md §1 — parallel Reward-Signal-Architecture §1)
  ⚠️ Cortisol = AMPLIFIER, not SOURCE of dissonance
     (Body-Feedback.md §5: cortisol injection → no pain)
  ⚠️ "Discomfort" = feeling label (PFC observes) ≠ dissonance (mechanism)
  ⚠️ chunk-gap (signal) versus gap (state):
     Gap (§2C) = STATE: chunk missing (PFC may not know)
     Chunk-gap (§4 here) = SIGNAL: body FIRES dissonance because it detects the gap
     = Gap exists → body detects → fires chunk-gap signal
```

---

## §5 — DETECTION: PREDICTION-DELTA LAYER (SEPARATE)

```
⭐ PREDICTION-DELTA = DETECTION LAYER — SEPARATE FROM REWARD/DISSONANCE:

  Brain detects "THERE IS VARIATION from prediction" → does NOT yet know if good or bad.
  Reward/dissonance = LATER step (Step 5: body-base check).
  2 distinct layers, CANNOT be merged.

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Meaning + when to use                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ prediction-delta    │ Brain detects variation from current │
  │         │                     │ prediction. Dopamine alert.          │
  │         │                     │ Does NOT yet know good/bad —         │
  │         │                     │ only "different from baseline."      │
  │         │                     │ = Step 2 in the 7-step mechanism.    │
  │         │                     │ Use: when describing detection signal.│
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ DRD4 filter         │ Receptor threshold for prediction-   │
  │(specific)│                    │ delta:                               │
  │         │                     │ 4R=sensitive (small delta detected)  │
  │         │                     │ 7R=coarse (only large delta)         │
  │         │                     │ (PFC-Hardware.md: per-person)        │
  │         │                     │                                      │
  │         │ PFC spotlight       │ Step 4: PFC boosts target region.    │
  │         │                     │ NE + ACh amplification.              │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⭐ CRITICAL DISTINCTION:

    Prediction-delta = "doorbell" (THERE IS VARIATION — pay attention!)
    Body-base reward = "the gift behind the door" (chunk MATCHES body-need)

    Doorbell → NOT the gift. Gift → doesn't always need a doorbell.
    (Direct-State Reward can bypass prediction-delta — Reward-Signal-Architecture §1.3 Precondition-3)

    → Do NOT merge prediction-delta with body-base reward
    → Do NOT call prediction-delta a "reward signal"
    → Detection (Step 2) ≠ Evaluation (Step 5)
```

---

## §6 — NEUTRAL: BODY-FEEDBACK BASELINE

```
⭐ BODY-FEEDBACK BASELINE = STATE OF "ALREADY ACCUSTOMED":

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning                                  │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ body-feedback baseline  │ Pattern repeats → brain habituates →     │
  │                         │ no prediction-delta → no alert.           │
  │                         │ = "The new normal state."                 │
  │                         │                                           │
  │ habituated              │ Same meaning, shorthand. Use when context │
  │                         │ is already clear as body-feedback.        │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⭐ HABITUATED ≠ VALUE = 0:

    Oxygen: habituated (breathing every day) → VALUE = life/death
    Monthly salary: habituated (arrives every month) → VALUE = survival
    Loyal team member: habituated (always present) → VALUE = team foundation

    → Habituated = no prediction-delta = brain NOT alerting
    → Does NOT mean "not important"
    → ONLY means "brain does not fire detection signal because accustomed"
    → LOSING something habituated → negative prediction-delta (SNC) → dissonance
    → "Turns out it mattered!" = habituated value made INVISIBLE

    (Reward-Calibration.md §8.3)

  ⚠️ Connection to §2: body-need CAN be habituated:
     Gap "survival" filled daily (salary) → habituated → brain ignores it
     BUT gap STILL EXISTS (lose salary → SNC → "turns out it mattered!")
     = Body-need exists ≠ body-feedback fires
```

---

## §7 — COMPILED: VALENCE TAGS + ENTITY-COMPILED

```
⭐ 2 LAYERS OF COMPILED VALENCE:

  LAYER 1 — APPROACH / AVOIDANCE TAGS (accumulated onto chunks):

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ Label               │ Meaning                                      │
  ├─────────────────────┼──────────────────────────────────────────────┤
  │ approach tag        │ POSITIVE valence compiled onto chunk.         │
  │                     │ "This domain → body-base reward" (verified). │
  │                     │ Drive TOWARD domain/agent.                   │
  │                     │                                               │
  │ avoidance tag       │ NEGATIVE valence compiled onto chunk.         │
  │                     │ "This domain → dissonance" (verified).        │
  │                     │ Drive AWAY FROM domain/agent.                 │
  └─────────────────────┴──────────────────────────────────────────────┘

  DISTINGUISHING COMPILED VERSUS MOMENTARY:

    Reward / dissonance = MOMENTARY (happening right now — §3/§4)
    Approach / avoidance = COMPILED (accumulated across many experiences)

    → "I enjoy mathematics" = approach tag (compiled across many reward instances)
    → "I am happy right now because I solved the problem" = body-base reward (momentary)
    → 2 DISTINCT things, though related

    → Approach tags = INPUT for drive direction (§2D)
    → Reward/dissonance = INPUT for compiling approach/avoidance tags

  (Valence-Propagation.md v2.0: per-entity valence + chain propagation)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  LAYER 2 — ENTITY-COMPILED (body-base extension):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Entity-Compiled         │ Entity has compiled into body-base at a  │
  │ (general)               │ STRUCTURAL level. Entity's state =       │
  │                         │ MY state. Per-channel valence profile.   │
  │                         │ Use: general term for structural bond.   │
  │                         │ (Inter-Body §8, Valence-Propagation      │
  │                         │ v2.0 §3)                                 │
  │                         │                                          │
  │ Entity-Compiled         │ Majority channels positive.              │
  │ positive-dominant       │ Presence = approach + reward.            │
  │                         │ Loss = grief (body-base amputation).     │
  │                         │ ≈ old "Entity-Owned" concept.            │
  │                         │ Examples: close friend, child, healthy   │
  │                         │ parent.                                  │
  │                         │                                          │
  │ Entity-Compiled         │ Majority channels negative.              │
  │ negative-dominant       │ Presence = threat/dissonance.            │
  │                         │ Loss = relief (or emptiness if obsessed).│
  │                         │ Examples: bully, abuser, obsessive rival.│
  │                         │                                          │
  │ Entity-Compiled         │ Significant BOTH positive AND negative   │
  │ mixed                   │ channels SIMULTANEOUSLY. ★ MOST COMMON. │
  │                         │ Behavior oscillates by state/context.    │
  │                         │ Loss = complex grief (relief + pain).    │
  │                         │ Examples: strict parent, conflicted      │
  │                         │ partner.                                 │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Entity-Compiled ≠ approach/avoidance tag:
     Approach/avoidance = Layer 1 (per-chunk, simple: +/-)
     Entity-Compiled = Layer 2 (per-entity, multi-channel, structural)
     = QUALITATIVE LEAP: entity's state AFFECTS my body-base
     = Losing entity = body-base amputation (not merely "resource loss")

  ⚠️ Entity-Compiled ≠ Obligation:
     Entity-Compiled: "entity's state = MY state" (structural, automatic)
     Obligation: "predict cost to MAINTAIN access" (prediction, PFC-mediated)
     = 2 INDEPENDENT mechanisms — can be high/low independently
     (Obligation.md v1.0 §2-§4)

  ⚠️ Mixed = MOST COMMON:
     Longer and closer relationship → more channels compile (both + and -)
     "Purely positive" = rare luxury of limited interactions
     "Both caring and resentful" = NORMAL multi-channel compile, not pathological
```

---

## §8 — COMPILED/FRESH: PROCESSING LABELS (★ NEW v2.0)

```
⭐ THE REAL PROCESSING AXIS: COMPILATION LEVEL — NOT CONTENT

  "Logic" and "Feeling" = OBSERVER LABELS (describing for outside understanding)
  INSIDE THE BODY: only a COMPILED ←→ FRESH spectrum exists
  Content (emotion/reasoning) does NOT determine processing level
  COMPILATION LEVEL determines it

  (Inter-Body-Mechanism.md §3)

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Compiled processing     │ Automatic. Body-direct. Cost ≈ 0.        │
  │                         │ Hebbian reinforced across many instances.│
  │                         │ "Feels right" / "intuition" / immediate. │
  │                         │ Use: when processing does NOT require    │
  │                         │ PFC drafting (fully compiled).           │
  │                         │                                          │
  │                         │ Examples:                                │
  │                         │ Expert mathematician "sees" the solution │
  │                         │ A chef instantly knows when salt is      │
  │                         │ missing                                  │
  │                         │ Close friends immediately sense each     │
  │                         │ other's mood                             │
  │                         │                                          │
  │ Fresh processing        │ PFC drafting. Deliberate. Cost > 0.      │
  │ (= Fresh PFC draft)     │ Each instance = effort (not yet          │
  │                         │ compiled). "Have to think" / "have to    │
  │                         │ analyze."                                │
  │                         │ Use: when PFC is chaining novel paths.   │
  │                         │                                          │
  │                         │ Examples:                                │
  │                         │ A mathematics student reasons through    │
  │                         │ each step deliberately                   │
  │                         │ A therapist encountering an unusual case │
  │                         │ must analyze it from scratch             │
  │                         │ Strangers have to guess each other's     │
  │                         │ emotions                                 │
  │                         │                                          │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ TRANSITION LABELS:      │                                          │
  │                         │                                          │
  │ Fresh → Compiled        │ LEARNING: repetition + verified OK →     │
  │ (learning)              │ Hebbian strengthening → automatic.       │
  │                         │ = "Logic → feeling" (for that person).   │
  │                         │                                          │
  │ Compiled → Fresh        │ DISRUPTION: new context, error detected  │
  │ (disruption)            │ → must re-evaluate deliberately.         │
  │                         │ = "Feeling → logic" (must think again).  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘


  ⭐ "LOGIC" vs "FEELING" = OBSERVER LABELS — WHEN TO USE:

  ┌────────────────────────────┬───────────────────────────────────────┐
  │ Context                    │ Appropriate label                     │
  ├────────────────────────────┼───────────────────────────────────────┤
  │ Mechanism analysis:        │ Compiled / Fresh (CORRECT)            │
  │ Describing to general      │ Logic / Feeling (OK, but recognize    │
  │ audience:                  │ these are observer labels, not        │
  │                            │ mechanism labels)                     │
  │ Research / deep analysis:  │ Compiled / Fresh (REQUIRED)           │
  │ Observation parameter:     │ Logic-Feeling (filename, observation) │
  └────────────────────────────┴───────────────────────────────────────┘

  ⚠️ "Logic" = compiled chunks that are SHAREABLE (deterministic domain: math, physics)
  ⚠️ "Intuition" = compiled chunks NOT EASILY SHAREABLE (probabilistic domain: psychology)
  ⚠️ INTERNALLY: mechanism is IDENTICAL. Difference: SHAREABILITY, not quality.
  ⚠️ RETIRED: "Humans are 100% feeling at the foundational layer" — terminology collision.
     v4.0 framing: PFC = Lawyer + Learning Trajectory (Logic-Feeling.md v4.0 §4.3).
     = PFC serves body-base (Lawyer). Fresh → compile → Body-Knowing (Learning Trajectory).
     = Same insight, mechanism-level, without the collision-prone word "feeling."
```

---

## §9 — INTER-BODY: INTERACTION LABELS (★ NEW v2.0)

```
⭐ VOCABULARY FOR INTER-BODY INTERACTION (Inter-Body-Mechanism.md):

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A) BY-PRODUCT MATCH / ANTI-MATCH (Inter-Body §5.4, By-Product-Gap-Resonance v1.0):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ by-product match        │ B fills B's OWN gap (§2C) → output =    │
  │                         │ by-product → matches A's gap direction   │
  │                         │ → A receives reward.                     │
  │                         │ = FOUNDATIONAL mechanism of inter-body   │
  │                         │ feeding.                                 │
  │                         │ Use: when describing HOW 2 entities feed.│
  │                         │                                          │
  │ anti-match              │ By-product CONFLICTS with gap direction  │
  │                         │ (§2C). Worse than no-match = ACTIVE      │
  │                         │ friction.                                │
  │                         │ Example: a change-driving leader ↔ a     │
  │                         │ person who prefers stability.            │
  │                         │ Use: when by-product generates           │
  │                         │ dissonance.                              │
  │                         │                                          │
  │ mutual match            │ BOTH parties receive reward from         │
  │ (= Resonance)           │ interaction. A matches B AND B matches A.│
  │                         │ Use: when both sides have by-product     │
  │                         │ match.                                   │
  │                         │                                          │
  │ one-way match           │ Only 1 side receives reward.             │
  │                         │ Examples: parasocial relationship,       │
  │                         │ asymmetric service.                      │
  │                         │ Use: when match is not mutual.           │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  B) 2-STREAM ARCHITECTURE (By-Product-Gap-Resonance v1.0 §2):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Hardware-Stream         │ Hardware/Unidirectional by-product match.│
  │ (hardware/unidirect.)   │ Reward from the OTHER SIDE's             │
  │                         │ EXISTENCE/attributes.                    │
  │                         │ Does not require reciprocal engagement.  │
  │                         │ HABITUATES (Weber-Fechner).              │
  │                         │ Felt INDEPENDENTLY (each side unaware    │
  │                         │ of the other's experience).              │
  │                         │ Use: when reward comes from presence/    │
  │                         │ attributes.                              │
  │                         │                                          │
  │ Modeling-Stream         │ Self-Pattern-Modeling compiled mutual    │
  │ (Self-Pattern-Modeling  │ (bidirectional). REQUIRES both sides to  │
  │  mutual)                │ engage Self-Pattern-Modeling → feedback  │
  │                         │ loop. 2 brains SYNCHRONIZE. Can CHANGE   │
  │                         │ the other's state.                       │
  │                         │ ANTI-HABITUATION (Hebbian → stronger).   │
  │                         │ Unsustainable if one-sided.              │
  │                         │ Use: when describing deep mutual         │
  │                         │ connection.                              │
  │                         │                                          │
  │ Proto-Modeling-Stream   │ Primitive Modeling-Stream (not full      │
  │                         │ Self-Pattern-Modeling).                  │
  │                         │ Parent-infant: contingent response.      │
  │                         │ Person-dog: associative matching.        │
  │                         │ Use: when mutual exchange exists but     │
  │                         │ lacks full bilateral Self-Pattern-       │
  │                         │ Modeling.                                │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  C) 3 INDEPENDENT COST SOURCES (Inter-Body §4):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ cost (general)          │ TOTAL COST = ① + ② + ③.                 │
  │                         │ Use: when speaking generally about       │
  │                         │ "interaction is costly."                 │
  │                         │                                          │
  │ ① PFC draft cost        │ PFC chains novel paths → processing      │
  │                         │ load. f(chain_length × novelty_degree).  │
  │                         │ = Fresh processing (§8) has COST.        │
  │                         │ Use: when describing cognitive effort.   │
  │                         │                                          │
  │ ② suppress cost         │ Override compiled response → efference   │
  │                         │ mismatch → body resists → dissonance.    │
  │                         │ f(intensity × duration).                 │
  │                         │ = Body WANTS X, forced to do Y →         │
  │                         │ mismatch.                                │
  │                         │ Use: when describing suppression effort. │
  │                         │                                          │
  │ ③ uncertainty cost      │ Multiple options, none compiled → holds  │
  │                         │ open → cortisol. f(options×time×stakes). │
  │                         │ = Not knowing the answer → must wait →   │
  │                         │ stress.                                  │
  │                         │ Use: when describing uncertainty/not     │
  │                         │ knowing.                                 │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ 3 cost sources are INDEPENDENT (can appear individually or simultaneously)
  ⚠️ SUSTAINABILITY = f(total cost × frequency ÷ reward)
  ⚠️ Cost does NOT come from "using logic" per se — comes from these 3 specific sources
  ⚠️ Connection to §2: high cost + body-need unfilled = unsustainable

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  D) 5-CHANNEL INPUT VECTOR (Inter-Body §6):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Ch1 — Hardware Sensory  │ Domain reality input NOW.                │
  │                         │ Visual, auditory, tactile, olfactory.    │
  │                         │                                          │
  │ Ch2 — Body State        │ Internal homeostasis.                    │
  │                         │ Hormone, glucose, cortisol, fatigue.     │
  │                         │                                          │
  │ Ch3 — Compiled Chunks   │ Associative firing from the past.        │
  │                         │ Memory, pattern, schema, habit loops.    │
  │                         │                                          │
  │ Ch4 — Entity Actions    │ What others DO/SAY.                      │
  │                         │ Words, facial expression, behavior.      │
  │                         │                                          │
  │ Ch5 — PFC Active Chain  │ Reasoning in progress.                   │
  │                         │ Ongoing cognitive process → feedback.    │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Dominant channel → determines vulnerability:
     Ch1 dominant = grounded in reality (protected)
     Ch4 dominant = entity controls activation (vulnerable)
     Multiple channels CONFIRMING = strong drive (hard to manipulate)
     Single channel ONLY = dangerous (scam, limerence)

  ⚠️ "Input Channel Control = Power":
     Whoever controls another person's input channels controls their behavior
     (Scam: control Ch4 + amplify Ch2 + block Ch1 = victim follows)
  ⚠️ Connection to §2: 5 channels = 5 ways to ACTIVATE body-need

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  E) SUPPLEMENTARY LABELS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Meaning + when to use                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Compilable Architecture │ Human system: general-purpose reward +   │
  │                         │ compilation + social hardware.           │
  │                         │ Trade-off: flexible but 15-20yr compile. │
  │                         │ (versus Hardwired Architecture:          │
  │                         │ specific-reward)                         │
  │                         │ Use: when explaining WHY the human       │
  │                         │ system works this way.                   │
  │                         │ (Inter-Body §1.2)                        │
  │                         │                                          │
  │ PFC = Lawyer            │ PFC constructs narrative FOR body-base.  │
  │                         │ NOT a neutral judge — advocates for      │
  │                         │ its client.                              │
  │                         │ Body-need (§2) fires FIRST → PFC         │
  │                         │ justifies after.                         │
  │                         │ Use: when analyzing PFC narrative ≠      │
  │                         │ actual body-need.                        │
  │                         │ (Inter-Body §7, Gazzaniga split-brain)   │
  │                         │                                          │
  │ Domain Reality          │ Final arbiter. CANNOT be permanently     │
  │ = Final Arbiter         │ fooled. Timeline varies (seconds→years). │
  │                         │ Dual Check: body=quality controller,     │
  │                         │ domain=final arbiter.                    │
  │                         │ Use: when noting "reality will verify."  │
  │                         │ (Inter-Body §6.4, Ask-AI v3.1)          │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘
```

---

## §10 — OBSERVATION VS MECHANISM (DIFFERENT LAYERS)

```
⭐ BODY-FEEDBACK ≠ FEELING — 2 DISTINCT LAYERS:

  ┌──────────────────┬───────────────────────────────────────────────┐
  │ Layer            │ Description                                   │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ BODY-FEEDBACK    │ MECHANISM: signals from body → runs 24/7      │
  │ (mechanism)      │ 95% UNCONSCIOUS (PFC cannot observe)          │
  │                  │ Labels: body-need, gap, reward, dissonance,   │
  │                  │ prediction-delta, chunk-miss/shift/gap,       │
  │                  │ Compiled/Fresh, 3-cost, 5-Channel (§2-§9)    │
  │                  │ = THIS FILE describes vocabulary for this     │
  │                  │ layer                                         │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ FEELING          │ OBSERVATION: PFC observes body-feedback       │
  │ (observation)    │ 7-layer gradient (implicit → explicit)        │
  │                  │ Labels: "pleasant" / "comfortable" /          │
  │                  │ "satisfied" / "vague" / "nagging unease" /    │
  │                  │ "discomfort" / "stuck" / "emptiness" /        │
  │                  │ "apathetic"                                   │
  │                  │ = Feeling.md v2.2 describes vocabulary for    │
  │                  │ this layer                                    │
  └──────────────────┴───────────────────────────────────────────────┘

  ⚠️ COMMON CONFUSIONS:

    "Pleasant" ≠ reward:
      → "Pleasant" = PFC observing body-base reward
        (Feel-Location/Feel-Labeling: already observed + labeled)
      → Reward can RUN while PFC does not observe it
        (Feel-RawSignals/Feel-Integration: body signals but PFC has not noticed)
      → = Body-base reward CAN OCCUR without "feeling pleasant" (possible)

    "Discomfort" ≠ dissonance:
      → "Discomfort" = PFC observation OF dissonance signal
      → Dissonance runs 24/7, PFC only observes a small fraction
      → = "Background-Pattern" dissonance = invisible (Background-Pattern.md)

    "Intuition" ≠ only feeling:
      → "Intuition" = compiled processing (§8: EVERYTHING: math AND emotion)
      → A chef "knowing" salt is missing = intuition = COMPILED (not "feeling only")
      → Real axis: Compiled/Fresh — not Logic/Feeling content

  (Feeling.md v2.2: feeling = PFC observation of body-feedback)
  (01-Foundation.md §5: 7-layer clarity gradient)
```

---

## §11 — USAGE RULES

### §11.1 — Core Principles

```
⭐ AS SPECIFIC AS POSSIBLE. AS GENERAL AS NECESSARY.

  ① Tier 3 > Tier 2 > Tier 1:
     If chain is known → Tier 3 ("chunk-miss → SNC → cortisol Role ②")
     If direction is known → Tier 2 ("body-base reward" / "dissonance")
     If only +/- is known → Tier 1 ("body-feedback positive/negative")

  ② Do NOT merge prediction-delta with body-base reward:
     "prediction-delta" = detection (Step 2)
     "body-base reward" = evaluation (Step 5)
     = 2 DISTINCT events, CAN occur INDEPENDENTLY

  ③ "reward" = body-base reward (BOTH Evaluative AND Direct-State):
     Do NOT limit to opioid / Evaluative
     Direct-State (touch, exercise, warmth) = REAL reward, CORRECT label

  ④ DISTINGUISH compiled (tags) versus momentary (signals):
     Approach/avoidance = already accumulated onto chunk (§7)
     Reward/dissonance = happening right now (§3/§4)

  ⑤ DISTINGUISH mechanism (body-feedback) versus observation (feeling):
     Body-feedback labels: reward, dissonance, prediction-delta,...
     Feeling labels: "pleasant", "comfortable", "satisfied",
       "vague", "nagging unease", "discomfort",
       "stuck", "emptiness", "apathetic"
     Do NOT use feeling labels in place of body-feedback labels (§10)

  ⑥ USE "Compiled/Fresh" when analyzing mechanism:
     "Logic/Feeling" = acceptable for external description (observer perspective)
     "Compiled/Fresh" = REQUIRED for deep analysis (mechanism level)
     Do NOT say "feeling opposes logic" → say "compiled conflicts with fresh" (§8)

  ⑦ 3-COST = 3 independent sources, do NOT merge:
     "Tired/drained" can = ① PFC draft, ② suppress, ③ uncertainty, or COMBO
     Label the SPECIFIC cost source → understand mechanism → know how to reduce it (§9C)

  ⑧ ENTITY-COMPILED ≠ APPROACH TAG:
     Approach tag = per-chunk, simple (+/-) (§7 Layer 1)
     Entity-Compiled = per-entity, multi-channel, structural (§7 Layer 2)
     Do NOT say "approach tag toward a parent figure"
     → say "Entity-Compiled mixed (parent figure)"

  ⑨ BODY-NEED = foundation, NOT a signal:
     Body-need (§2) = STATE (state of NEED — always exists)
     Body-feedback = SIGNAL (body REPORTS about state)
     Do NOT say "body-need fires" → say "body-feedback fires because of body-need X"
     Body-need = CONTEXT, body-feedback = COMMUNICATION
```

### §11.2 — Applied Examples

```
  EXAMPLE 1: Salary increase from $1,000 → $1,500/month

  TIER 2 (sufficient for Research files):
    "Body-need [survival] has gap [income].
     $1,000/month → body-base reward (gap filled in correct direction) → habituated.
     $1,500/month → smaller prediction-delta → reward decreases (gap has shrunk)."

  TIER 3 (for deep analysis):
    "Body-need [survival] has gap [income direction: ≥$1,000/month].
     $1,000 (first time):
       prediction-delta (novel) → DRD4 pass → PFC spotlight
       → body-base check: chunk [$1,000/month salary] matches gap direction
       → Evaluative Reward
       → chunk compiles: [$1,000/month salary = approach tag]
     $1,000 (month 12):
       habituated: same pattern → no prediction-delta → no alert
       → gap ALREADY filled → body-feedback baseline
     $1,500:
       prediction-delta (different from $1,000 baseline) → body-base check
       → gap shrinks (largely filled) → reward decreases
       → = Diminishing returns = gap shrinks over time"


  EXAMPLE 2: Parent-child conflict (inter-body):

  TIER 2:
    "Child: Entity-Compiled mixed (parent). Hardware-Stream habituated.
     Modeling-Stream present but conflicting directions.
     Cost: ② suppress high (holding back responses) + ③ uncertainty
     (parent unpredictable).
     By-product: parent fills PARENT's own gap (guiding/teaching) → output
     anti-matches child's gap direction (autonomy)."

  TIER 3:
    "Child: Entity-Compiled mixed [nutrition++, comfort++, autonomy--, status+/-]
     Body-need [autonomy] has gap [direction: self-determination].
     Parent says 'you must study': Ch4 dominant → compiled chunks Ch3 fire
     [restriction schema] → body-state Ch2 cortisol ↑
     → suppress cost ② (compiled response wants to push back but is held in)
     → uncertainty cost ③ (will parent punish or not?)
     → dissonance: chunk-gap [autonomy direction blocked]
     By-product mechanism: Parent fills gap 'raising well' (PARENT's own gap)
     → output = forced studying → anti-matches child's gap direction [freedom to explore]
     PFC = Lawyer: child narrative 'they don't understand me' (may be 0.3 accuracy)"
```

---

## §12 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback.md v1.1            │ ENTRY POINT. §4 4 axes. §6           │
  │                                  │ Body-Feedback-Precondition.          │
  │                                  │ Read BEFORE this file.               │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Mechanism.md v2.0  │ §1 Body-Need aggregate. §2 2 sources.│
  │                                  │ §3 3 dynamics. Tier 3 labels.        │
  │                                  │ SOURCE for §2 Foundation.            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Inter-Body-Mechanism.md v1.0     │ §2 Body-Need. §3 Compiled/Fresh.     │
  │                                  │ §4 3-cost. §5 By-product match.      │
  │                                  │ §6 5-Channel. §7 PFC=Lawyer.         │
  │                                  │ §8 Entity-Compiled.                  │
  │                                  │ SOURCE for §8+§9 of this file.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gap-Direction.md v2.0            │ §1 Definition: gap = f(surrounding   │
  │                                  │ chunks). "Not yet knowing = no gap." │
  │                                  │ SOURCE for §2C Foundation.           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Reward-Signal-Architecture.md    │ §1 Evaluative/Direct-State.          │
  │ v2.0                             │ §2 E₀→E₃. §4 5 Profiles.            │
  │                                  │ Tier 2-3 reward labels.              │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ 03-Reward.md v1.1                │ §2 7-step mechanism.                 │
  │                                  │ §3 Body-Feedback-Preconditions.      │
  │                                  │ Step 5 detail.                       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.0        │ §7.7 5 Roles. Amplifier, not cause.  │
  │                                  │ Tier 3 dissonance labels.            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Valence-Propagation.md v2.0      │ §3 Entity-Compiled (3 subtypes).     │
  │                                  │ Approach/avoidance tags.             │
  │                                  │ Compiled versus momentary            │
  │                                  │ distinction.                         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ By-Product-Gap-Resonance.md v1.0 │ §2 2-Stream Architecture.            │
  │                                  │ Hardware-Stream/Modeling-Stream/     │
  │                                  │ Proto labels defined.                │
  │                                  │ By-product match + anti-match.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Feeling.md v2.2                  │ PFC observation of body-feedback.    │
  │                                  │ 7-layer gradient. Different layer    │
  │                                  │ (§10).                               │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Base.md v3.3                │ L0+L1 substrate. Compilable          │
  │                                  │ Architecture. System-level context   │
  │                                  │ for §2A.                             │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Threat.md                        │ 5 levels × 3 axes × 3 sources.       │
  │                                  │ Tier 2 dissonance label: threat.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Ask-AI.md v3.1                   │ Dual Check: body = quality           │
  │                                  │ controller, domain = final arbiter.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Clarification/ folder            │ Bridge mainstream → framework.       │
  │                                  │ ONLY PLACE to discuss non-framework  │
  │                                  │ terminology + why framework uses     │
  │                                  │ different labels.                    │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

> *Body-Feedback Label Convention v2.0 — Vocabulary Reference.*
> *100% framework vocabulary.*
> *3-tier system: as specific as possible, as general as necessary.*
>
> *§2 Foundation: body-need = aggregate of NEED. Gap = specific missing. Drive = behavioral push.*
> *§3-§6 Signals: reward / dissonance / prediction-delta / baseline.*
> *§7 Compiled: approach/avoidance tags + Entity-Compiled 3 subtypes.*
> *§8 Processing: Compiled/Fresh = the real axis (Logic/Feeling = observer labels).*
> *§9 Inter-Body: by-product match, 2-Stream, 3-cost, 5-Channel.*
> *§10 Distinction: body-feedback (mechanism) ≠ feeling (observation).*
>
> *Body-need = STATE. Body-feedback = SIGNAL. Gap direction = WHY match works.*
> *"The doorbell" ≠ "the gift behind the door."*
