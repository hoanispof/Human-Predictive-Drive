---
title: Body-Feedback Label Convention — Vocabulary Reference
version: 2.1
source_version: Vietnamese v2.1 (2026-05-25)
english_created: 2026-06-05
english_updated:
rewritten: 2026-05-17 (v2.0 — FULL REWRITE: +Foundation terms, +Compiled/Fresh processing, +Entity-Compiled 3 subtypes, +Inter-Body interaction labels, +5-Channel, +3-cost, +2-Stream)
updated: 2026-05-25 (v2.1 — §4 +Evaluative/Direct-State Dissonance labels at Tier 2+3, parallel §3 Reward structure, Dissonance-Signal-Architecture v1.0 integration)
previous: v1.1 → backup/Body-Feedback-Label-v1.1-backup.md
status: REFERENCE v2.1
scope: |
  VOCABULARY REFERENCE: Label conventions for the entire body-feedback system.
  Formalizes the 3-tier label system: General → Direction → Specific.
  This file = MUST-READ immediately after Body-Feedback.md.
  All framework files should use vocabulary according to these conventions.
  100% FRAMEWORK VOCABULARY — no terminology outside the framework.
  v2.0 EXPANSION: 7 concept families (from Inter-Body drill):
    ① Foundation terms (body-need, gap, gap direction, drive)
    ② Entity-Compiled 3 subtypes (positive/negative/mixed)
    ③ Compiled/Fresh processing labels (the true axis)
    ④ By-product match / Anti-match
    ⑤ 2-Stream Architecture (Hardware-Stream / Modeling-Stream)
    ⑥ 3 Independent Cost Sources
    ⑦ 5-Channel Input Vector
purpose: |
  The framework analyzes body-feedback through 4 orthogonal axes, a 7-step mechanism,
  Evaluative/Direct-State distinction, E₀→E₃ complexity gradient, 5 Profiles,
  3 chunk dynamics, and 5 cortisol Roles.
  v2.0: ADDS Foundation terms, Compiled/Fresh processing, Inter-Body interaction,
  Entity-Compiled multi-channel, 5-Channel Input, 3-cost.
  This file formalizes a unified vocabulary for the ENTIRE framework —
  covering both intra-body AND inter-body labels.
  Resolves:
    → "opioid confirm" only covers Evaluative, misses Direct-State
    → "pleasant/discomfort" confuses body-feedback (mechanism) with feeling (observation)
    → "Logic/Feeling" confuses observer labels with mechanism labels
    → Missing vocabulary for inter-body interaction
    → Foundation terms (body-need, gap) used everywhere but never defined
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
language: English (source: Vietnamese + English technical terms)
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Label Convention — Vocabulary Reference

> **The framework analyzes body-feedback through 4 orthogonal axes, a 7-step mechanism,**
> **Evaluative/Direct-State, E₀→E₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles...**
>
> **PLUS: Foundation terms, Compiled/Fresh processing, Entity-Compiled 3 subtypes,**
> **By-product match, 2-Stream, 3-cost, 5-Channel Input Vector.**
>
> **But when WRITING or SPEAKING, labels were NEVER formalized.**
>
> **This file: LABEL CONVENTIONS for the entire framework.**
> **100% framework vocabulary. Read immediately after Body-Feedback.md.**

---

## Table of Contents

- §0 — WHY THIS FILE IS NEEDED
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

## §0 — WHY THIS FILE IS NEEDED

```
⭐ THE FRAMEWORK HAS PRECISE MECHANISMS — BUT LACKED LABEL CONVENTIONS:

  The body-feedback system has:
    → 4 orthogonal classification axes (Body-Feedback-Mechanism.md §0)
    → 7-step mechanism from detection → reward (03-Reward.md §2)
    → Evaluative/Direct-State Reward distinction (Reward-Signal-Architecture.md §1)
    → E₀→E₃ complexity gradient + 5 Profiles
    → 3 chunk dynamics (Chunk-Shift/Miss/Gap)
    → 5 cortisol Roles (Cortisol-Baseline.md §7.7)

  v2.0 ADDS (from Inter-Body drill):
    → Foundation terms: body-need, gap, gap direction, drive (Inter-Body §2)
    → Compiled/Fresh = the true processing axis (Inter-Body §3)
    → Entity-Compiled 3 subtypes (Inter-Body §8, Valence-Propagation v2.0 §3)
    → By-product match + Anti-match (Inter-Body §5.4)
    → 2-Stream Architecture (By-Product-Gap-Resonance v1.0 §2)
    → 3 Independent Cost Sources (Inter-Body §4)
    → 5-Channel Input Vector (Inter-Body §6)

  BUT: no convention existed for WHICH LABEL to use when writing or speaking.
  → Same phenomenon → 5 different labels used → ambiguity


  4 SPECIFIC PROBLEMS:

  ① "OPIOID CONFIRM" ONLY COVERS EVALUATIVE REWARD:
    Evaluative Reward: μ-opioid → hedonic hotspot → CORRECTLY "opioid confirm"
    Direct-State Reward: CT afferents / endocannabinoid / thermoreceptor → NOT opioid
    → Correct general label = "body-base reward" (covers BOTH Evaluative AND Direct-State)
    (Reward-Signal-Architecture.md §1.1)

  ② CONFUSING BODY-FEEDBACK WITH FEELING:
    Body-feedback = MECHANISM (signal from body, runs 24/7, 95% unconscious)
    Feeling = OBSERVATION (PFC observes body-feedback → 7-layer gradient)
    "Pleasant" = feeling label (PFC has already observed + labeled) — NOT a body-feedback label
    → §10 of this file draws the distinction clearly
    (Feeling.md v2.2)

  ③ "LOGIC / FEELING" CONFUSES OBSERVER LABELS WITH MECHANISM LABELS (v2.0 NEW):
    THE TRUE AXIS internally = Compiled ←→ Fresh (compilation level)
    "Logic/Feeling" = observer perspective labels, NOT mechanism labels
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

  → When the chain is TRACEABLE → use Tier 3
    "chunk-miss → SNC → cortisol Role ② Holding"

  → When DIRECTION + CHARACTER is known but chain is complex → use Tier 2
    "body-base reward" / "dissonance" / "threat"

  → When you ONLY KNOW body responds +/- without more specificity → use Tier 1
    "positive body-feedback" / "negative body-feedback"


  AUDIENCE-APPROPRIATE:

    Expert / deep analysis:
      → Tier 3 primary. Chain trace clear.

    Researchers / those seeking understanding:
      → Tier 2 primary: "body-base reward", "dissonance", "chunk-miss"
      → Precise enough, sufficient understanding of basic mechanism

    General / overview:
      → Tier 1 when needed: "positive/negative body-feedback"
      → Can drill deeper if reader requests


  APPLIES TO ALL CATEGORIES (§2-§9):
    Each category has corresponding Tier 1/2/3 labels.
    3-Tier logic = UNIVERSAL, applies to foundation, signal,
    processing, and inter-body labels alike.
```

---

## §2 — FOUNDATION: BODY-NEED + GAP + DRIVE (★ NEW v2.0)

```
⭐ FOUNDATION TERMS — ALL SUBSEQUENT SECTIONS REFERENCE THESE:

  ┌─────────────────────────────────────────────────────────────────┐
  │ CONCEPTUAL FLOW:                                                 │
  │                                                                  │
  │   body-base (system)                                             │
  │       ↓ generates                                                │
  │   body-need (aggregate state of NEED)                            │
  │       ↓ comprises                                                │
  │   gap + gap direction (specific chunks missing + direction)      │
  │       ↓ gives rise to                                            │
  │   drive (behavioral push to fill gap)                            │
  │       ↓ monitored by                                             │
  │   body-feedback (signal from body about current state — THIS FILE)│
  │                                                                  │
  └─────────────────────────────────────────────────────────────────┘


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A) BODY-BASE (the system):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ body-base               │ THE ENTIRE system: hardware + compiled   │
  │                         │ + social. = The "foundational body"      │
  │                         │ encompassing everything the body has     │
  │                         │ accumulated + currently operates.        │
  │                         │ Compilable Architecture: general-purpose reward + │
  │                         │ compilation + social hardware.           │
  │                         │ Use: when referring to THE SYSTEM        │
  │                         │ as a whole.                              │
  │                         │ (Body-Base.md v3.1, Inter-Body §1)      │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  B) BODY-NEED (aggregate state of NEED):

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Definition + when to use             │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-need           │ AGGREGATE current state of NEED.     │
  │ (general)│                    │ Aggregates ALL signals currently      │
  │         │                     │ demanding body response.             │
  │         │                     │ NOT a single signal → it is the SUM. │
  │         │                     │ Exists BEFORE PFC awareness.         │
  │         │                     │ Use: when speaking generally about   │
  │         │                     │ "what the body needs."               │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ hardware body-need  │ Source ①: Sensory-Driven.            │
  │ (source)│                     │ Homeostatic + nociceptive + hormonal.│
  │         │                     │ Requires NO compiled chunks.         │
  │         │                     │ e.g., hunger, thirst, pain, cold.   │
  │         │                     │ Use: when body-need originates       │
  │         │                     │ from hardware.                       │
  │         │                     │                                      │
  │         │ pattern body-need   │ Source ②: Chunk Dynamics/Pattern.    │
  │         │                     │ Gap / Miss / Shift (+ Compound).     │
  │         │                     │ REQUIRES compiled chunks.            │
  │         │                     │ e.g., missing a friend, career gap,  │
  │         │                     │ identity crisis.                     │
  │         │                     │ Use: when body-need originates       │
  │         │                     │ from chunk firing.                   │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ (specific gaps)     │ Specific gap + direction.            │
  │(specific)│                    │ e.g., "gap survival [direction: food]"│
  │         │                     │ e.g., "gap mastery [direction: math]"│
  │         │                     │ e.g., "gap connection               │
  │         │                     │       [direction: close friend A]"   │
  │         │                     │ Use: when a SPECIFIC gap             │
  │         │                     │ can be traced.                       │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Body-need ALWAYS EXISTS (never = 0)
  ⚠️ Body-need = MULTIPLE in parallel (simultaneous)
  ⚠️ Body-need HAS PRIORITY (intensity × urgency × state)
  ⚠️ PFC DOES NOT ALWAYS KNOW body-need (exists before awareness)
  ⚠️ 2 sources NOT mutually exclusive — 1 event can trigger BOTH ①+②
  (Inter-Body §2, Body-Feedback-Mechanism v2.0 §1)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  C) GAP + GAP DIRECTION (specific missing + direction):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ gap                     │ Chunk SHOULD exist but is MISSING.       │
  │                         │ Network predicts chunk C → C absent.     │
  │                         │ = A SPECIFIC component of body-need.     │
  │                         │ Use: when referring to "something        │
  │                         │ specific that is missing."               │
  │                         │                                          │
  │ gap direction           │ DIRECTION gap points = f(surrounding     │
  │                         │ chunks). Only filling in the RIGHT       │
  │                         │ DIRECTION → reward.                      │
  │                         │ Each person has their OWN direction.     │
  │                         │ "What you don't know creates no gap"     │
  │                         │ (no surrounding chunks → no direction    │
  │                         │ yet).                                    │
  │                         │ Use: when describing HOW a gap needs     │
  │                         │ to be filled.                            │
  │                         │ (Gap-Direction.md v2.0)                  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ gap ≠ body-need:
     Gap = 1 specific chunk missing (component)
     Body-need = AGGREGATE of all gaps + hardware signals (the sum)
     1 body-need can contain MANY parallel gaps
  ⚠️ "What you don't know creates no gap" — a gap ONLY exists when
     surrounding chunks have ALREADY compiled. A child has no gap
     around "quantum physics" because the substrate doesn't yet exist.
  ⚠️ Gap direction = WHY by-product match works:
     B's output matches A's gap DIRECTION → A receives reward.
     Direction mismatch → no reward EVEN IF output exists.


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  D) DRIVE (behavioral push):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ drive                   │ The behavioral PUSH from body-need.      │
  │                         │ = Behavioral output from body-need →     │
  │                         │ action to fill gap.                      │
  │                         │ Use: when describing "what DRIVES        │
  │                         │ behavior."                               │
  │                         │                                          │
  │ drive direction         │ = gap direction expressed as behavior.   │
  │                         │ Drive points TOWARD (approach) or        │
  │                         │ AWAY (avoidance).                        │
  │                         │ Use: when describing the DIRECTION       │
  │                         │ of behavior.                             │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ drive ≠ body-need:
     Body-need = STATE (state of NEED — internal)
     Drive = OUTPUT (behavioral push — toward action)
     Body-need → drive (but PFC can suppress drive → cost ②)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  E) BODY-FEEDBACK (signal domain — umbrella term of THIS FILE):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ body-feedback           │ ALL signals from body about current      │
  │                         │ state. UMBRELLA TERM for everything this │
  │                         │ file describes. Runs 24/7. 95%          │
  │                         │ unconscious.                             │
  │                         │ Includes: reward, dissonance, prediction-│
  │                         │ delta, baseline, valence tags...         │
  │                         │ ≠ Feeling (feeling = PFC OBSERVING       │
  │                         │ body-feedback — different layer, §10).  │
  │                         │ Use: when speaking generally about       │
  │                         │ "the body sending a signal."             │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ body-feedback MONITORS body-need:
     Body-need = WHAT is needed. Body-feedback = WHAT the body reports.
     Reward = "gap is being filled" (positive feedback)
     Dissonance = "gap NOT yet filled / blocked" (negative feedback)
     → Body-feedback = COMMUNICATION CHANNEL, body-need = CONTENT
```

---

## §3 — POSITIVE: BODY-BASE REWARD LABELS

```
⭐ REWARD = BODY-BASE CONFIRM SIGNAL (body confirms: chunk MATCHES body-need)

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Definition + when to use             │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ positive            │ Most general. Body responds          │
  │ (general)│ body-feedback      │ positively. Does not specify         │
  │         │                     │ mechanism.                           │
  │         │                     │ Use: when only body response + is    │
  │         │                     │ known.                               │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ body-base reward    │ Body confirms chunk matches body-need │
  │ (type)  │                     │ (§2). Covers both Evaluative +       │
  │         │                     │ Direct-State.                        │
  │         │                     │ Use: when body confirmation is       │
  │         │                     │ clearly identified.                  │
  │         │                     │                                      │
  │         │ reward              │ Shorthand for body-base reward.      │
  │         │                     │ Use: when context is CLEARLY         │
  │         │                     │ body-feedback (no risk of confusion).│
  │         │                     │                                      │
  │         │ Evaluative Reward   │ Evaluative confirm. Opioid-based.    │
  │         │                     │ Requires full Body-Feedback-         │
  │         │                     │ Precondition. Rich chunk library.    │
  │         │                     │ Use: when clearly evaluative.        │
  │         │                     │                                      │
  │         │ Direct-State Reward │ Direct state confirm. Non-opioid.    │
  │         │                     │ Hardware-based. Less habituated.     │
  │         │                     │ Use: when clearly a body-state       │
  │         │                     │ response.                            │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ μ-opioid confirm    │ Evaluative. Hedonic hotspot pathway. │
  │(specific)│                    │ Use: when chain is traced to         │
  │         │                     │ NAcc/VP.                             │
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
  │         │ Profile ①-⑤         │ 5 reward "flavors."                  │
  │         │                     │ Sensory/Coherence/Social/Relief/     │
  │         │                     │ Preview.                             │
  │         │                     │ (Reward-Signal-Architecture §4)      │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ "opioid confirm" → ONLY use when speaking SPECIFICALLY about the Evaluative pathway
  ⚠️ "reward" in general → ALWAYS covers BOTH Evaluative AND Direct-State
  ⚠️ Remember: reward = body confirms "gap is filling in the right direction" (§2C)
     ≠ prediction-delta (detection signal — §5)
```

---

## §4 — NEGATIVE: DISSONANCE LABELS

```
⭐ DISSONANCE = BODY SIGNAL OF "MISMATCH" (mismatch / predicted harm / recalibration)

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Definition + when to use             │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ negative            │ Most general. Body responds          │
  │ (general)│ body-feedback      │ negatively.                          │
  │         │                     │ Use: when only body response — is    │
  │         │                     │ known.                               │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ dissonance          │ Body detects mismatch (schema ≠      │
  │ (type)  │                     │ reality). Drives resolution.         │
  │         │                     │ Use: when mismatch is clearly        │
  │         │                     │ identified.                          │
  │         │                     │                                      │
  │         │ threat              │ Body predicts harm (anticipated      │
  │         │                     │ damage). Drives avoidance.           │
  │         │                     │ Use: when anticipatory harm is       │
  │         │                     │ clearly identified.                  │
  │         │                     │ (Threat.md: 5 levels × 3 axes       │
  │         │                     │  × 3 sources)                        │
  │         │                     │                                      │
  │         │ recalibration       │ Neurons adjusting pattern.           │
  │         │ dissonance          │ Transient, self-resolving when       │
  │         │                     │ adaptation completes.                │
  │         │                     │ Use: when discomfort comes from      │
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
  │         │                     │ PFC minimal. Numbness-proof.         │
  │         │                     │ Use: when clearly a body-state       │
  │         │                     │ response (pain, hunger, temp, itch). │
  │         │                     │ (Dissonance-Signal-Architecture §1)  │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ chunk-miss          │ Expected X, got <X. SNC mechanism.   │
  │(specific)│                    │ (Crespi 1942, Flaherty 1996)         │
  │         │                     │                                      │
  │         │ chunk-shift         │ Same chunks, DIFFERENT valence.      │
  │         │                     │ Context changed → re-evaluate.       │
  │         │                     │                                      │
  │         │ chunk-gap           │ = gap (§2C) being DETECTED as        │
  │         │                     │ dissonance signal. C should exist    │
  │         │                     │ but missing → body fires signal.     │
  │         │                     │ (Gap-Direction.md: gap has direction) │
  │         │                     │                                      │
  │         │ SNC                 │ Successive Negative Contrast.        │
  │         │                     │ Specific chunk-miss: downshift       │
  │         │                     │ from high baseline → overreact.      │
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
  │         │                     │ ④ Inertia (addicted to productivity) │
  │         │                     │ ⑤ Silent (elevated but unfelt)       │
  │         │                     │ (Cortisol-Baseline.md §7.7)          │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Evaluative/Direct-State = ORTHOGONAL to source (dissonance/threat/recalibration)
     1 event can be BOTH "mismatch" (source) AND "Evaluative" (type)
     e.g., betrayal = mismatch (source) + Evaluative Dissonance (type)
     e.g., needle prick = nociception (source) + Direct-State Dissonance (type)
     (Dissonance-Signal-Architecture.md §1 — parallel Reward-Signal-Architecture §1)
  ⚠️ Cortisol = AMPLIFIER, not the SOURCE of dissonance
     (Body-Feedback.md §5: cortisol injection → no pain)
  ⚠️ "Discomfort" = feeling label (PFC observes) ≠ dissonance (mechanism)
  ⚠️ chunk-gap (signal) vs gap (state):
     Gap (§2C) = STATE: chunk missing (PFC may not know)
     Chunk-gap (§4 here) = SIGNAL: body FIRES dissonance upon detecting a gap
     = Gap exists → body detects → fires chunk-gap signal
```

---

## §5 — DETECTION: PREDICTION-DELTA LAYER (SEPARATE)

```
⭐ PREDICTION-DELTA = DETECTION LAYER — SEPARATE FROM REWARD/DISSONANCE:

  Brain detects "a DEVIATION from prediction" → does NOT yet know if good or bad.
  Reward/dissonance = the NEXT step (Step 5: body-base check).
  2 DISTINCT layers, CANNOT be merged.

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Definition + when to use             │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ prediction-delta    │ Brain detects deviation from current │
  │         │                     │ prediction. Dopamine alert.           │
  │         │                     │ Does NOT yet know good/bad — only    │
  │         │                     │ "different from baseline."           │
  │         │                     │ = Step 2 in the 7-step mechanism.    │
  │         │                     │ Use: when referring to a detection   │
  │         │                     │ signal.                              │
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

    Prediction-delta = the "doorbell" (DEVIATION DETECTED — attention!)
    Body-base reward = the "gift behind the door" (chunk MATCHES body-need)

    Doorbell → NOT the gift. Gift → doesn't ALWAYS need a doorbell.
    (Direct-State Reward can bypass prediction-delta — Reward-Signal-Architecture §1.3 Precondition-3)

    → DO NOT merge prediction-delta with body-base reward
    → DO NOT call prediction-delta a "reward signal"
    → Detection (Step 2) ≠ Evaluation (Step 5)
```

---

## §6 — NEUTRAL: BODY-FEEDBACK BASELINE

```
⭐ BODY-FEEDBACK BASELINE = THE "ACCUSTOMED" STATE:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition                               │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ body-feedback baseline  │ Repeated pattern → brain habituated →    │
  │                         │ no prediction-delta → no alert.          │
  │                         │ = "The new normal."                      │
  │                         │                                          │
  │ habituated              │ Synonym, shorthand. Use when context     │
  │                         │ is clearly body-feedback.                │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⭐ HABITUATED ≠ VALUE = 0:

    Oxygen: habituated (breathed daily) → VALUE = life/death
    Monthly salary: habituated (received every month) → VALUE = survival
    Loyal employee: habituated (always present) → VALUE = team foundation

    → Habituated = no prediction-delta = brain NOT alert
    → DOES NOT MEAN "not important"
    → ONLY MEANS "brain doesn't fire a detection signal because it has adapted"
    → LOSING something habituated → negative prediction-delta (SNC) → dissonance
    → "Turns out it mattered!" = habituated value turned INVISIBLE

    (Reward-Calibration.md §8.3)

  ⚠️ Connection to §2: body-need CAN be habituated:
     Gap "survival" filled daily (salary) → habituated → brain ignores it
     BUT the gap STILL EXISTS (lose salary → SNC → "turns out it mattered!")
     = Body-need exists ≠ body-feedback fires
```

---

## §7 — COMPILED: VALENCE TAGS + ENTITY-COMPILED

```
⭐ 2 LAYERS OF COMPILED VALENCE:

  LAYER 1 — APPROACH / AVOIDANCE TAGS (accumulated onto chunks):

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ Label               │ Definition                                   │
  ├─────────────────────┼──────────────────────────────────────────────┤
  │ approach tag        │ POSITIVE valence compiled onto a chunk.      │
  │                     │ "This domain → body-base reward" (verified). │
  │                     │ Drive points TOWARD domain/agent.            │
  │                     │                                              │
  │ avoidance tag       │ NEGATIVE valence compiled onto a chunk.      │
  │                     │ "This domain → dissonance" (verified).       │
  │                     │ Drive points AWAY FROM domain/agent.         │
  └─────────────────────┴──────────────────────────────────────────────┘

  COMPILED vs MOMENTARY DISTINCTION:

    Reward / dissonance = MOMENTARY (occurring now — §3/§4)
    Approach / avoidance = COMPILED (accumulated across many experiences)

    → "I enjoy math" = approach tag (compiled through many reward instances)
    → "I'm elated because I solved the problem" = body-base reward (momentary)
    → 2 DISTINCT things, though related

    → Approach tags = INPUT for drive direction (§2D)
    → Reward/dissonance = INPUT for compiling approach/avoidance tags

  (Valence-Propagation.md v2.0: per-entity valence + chain propagation)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  LAYER 2 — ENTITY-COMPILED (body-base extension):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Entity-Compiled         │ Entity has compiled into body-base at    │
  │ (general)               │ STRUCTURAL level. Entity's state =       │
  │                         │ MY state. Per-channel valence profile.   │
  │                         │ Use: general term for structural bond.   │
  │                         │ (Inter-Body §8, Valence-Propagation      │
  │                         │  v2.0 §3)                                │
  │                         │                                          │
  │ Entity-Compiled         │ Majority channels positive.              │
  │ positive-dominant       │ Presence = approach + reward.            │
  │                         │ Loss = grief (body-base amputation).     │
  │                         │ ≈ old "Entity-Owned" concept.            │
  │                         │ e.g., close friend, child, healthy       │
  │                         │ parent.                                  │
  │                         │                                          │
  │ Entity-Compiled         │ Majority channels negative.              │
  │ negative-dominant       │ Presence = threat/dissonance.            │
  │                         │ Loss = relief (or emptiness if obsess).  │
  │                         │ e.g., bully, abuser, obsessive rival.   │
  │                         │                                          │
  │ Entity-Compiled         │ Significant BOTH positive AND negative   │
  │ mixed                   │ channels SIMULTANEOUSLY. ★ MOST COMMON. │
  │                         │ Behavior oscillates by state/context.    │
  │                         │ Loss = complex grief (relief + pain).    │
  │                         │ e.g., strict parents, conflicted couple. │
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
     The closer and longer the relationship → the more channels compile (both + and -)
     "Purely positive" = rare luxury of limited interactions
     "Love and resentment together" = NORMAL multi-channel compilation, not pathological
```

---

## §8 — COMPILED/FRESH: PROCESSING LABELS (★ NEW v2.0)

```
⭐ THE TRUE AXIS OF PROCESSING: COMPILATION LEVEL — NOT CONTENT

  "Logic" and "Feeling" = OBSERVER LABELS (descriptions for outside observers)
  INSIDE THE BODY: only the COMPILED ←→ FRESH spectrum exists
  Content (emotion/reasoning) does NOT determine processing level
  COMPILATION LEVEL determines it

  (Inter-Body-Mechanism.md §3)

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Compiled processing     │ Automatic. Body-direct. Cost ≈ 0.       │
  │                         │ Hebbian reinforced through repeated      │
  │                         │ exposure.                                │
  │                         │ "Feels right" / "intuitive" / immediate. │
  │                         │ Use: when processing requires NO PFC    │
  │                         │ draft (already compiled).                │
  │                         │                                          │
  │                         │ e.g., Einstein "seeing" the mathematical │
  │                         │       solution                           │
  │                         │ e.g., A chef instantly knowing the dish  │
  │                         │       needs salt                         │
  │                         │ e.g., Close friends instantly reading    │
  │                         │       each other's mood                  │
  │                         │                                          │
  │ Fresh processing        │ PFC draft. Deliberate. Cost > 0.         │
  │ (= Fresh PFC draft)     │ Each instance = effort (not yet          │
  │                         │ compiled).                               │
  │                         │ "Must think" / "must analyze."           │
  │                         │ Use: when PFC is chaining novel paths.   │
  │                         │                                          │
  │                         │ e.g., A math novice who must reason      │
  │                         │       through each step                  │
  │                         │ e.g., A therapist encountering an        │
  │                         │       unfamiliar case who must analyze   │
  │                         │ e.g., Strangers who must guess each      │
  │                         │       other's emotions                   │
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
  │                         │ = "Feeling → logic" (must think it       │
  │                         │ through again).                          │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘


  ⭐ "LOGIC" vs "FEELING" = OBSERVER LABELS — WHEN TO USE EACH?

  ┌────────────────────────────┬───────────────────────────────────────┐
  │ Context                    │ Appropriate label                     │
  ├────────────────────────────┼───────────────────────────────────────┤
  │ Mechanism analysis:        │ Compiled / Fresh (CORRECT)            │
  │ Describing to general      │ Logic / Feeling (OK, but knowing      │
  │ audience:                  │ these are observer labels, not        │
  │                            │ mechanism)                            │
  │ Research / deep analysis:  │ Compiled / Fresh (REQUIRED)           │
  │ Observation parameter:     │ Logic-Feeling (file name, observation)│
  └────────────────────────────┴───────────────────────────────────────┘

  ⚠️ "Logic" = compiled chunks SHAREABLE (deterministic domain: math, physics)
  ⚠️ "Intuition" = compiled chunks NOT EASILY SHAREABLE (probabilistic domain: psychology)
  ⚠️ INTERNALLY: the mechanism is IDENTICAL. The difference: SHAREABILITY, not quality.
  ⚠️ RETIRED: "Humans are 100% feeling at the base layer" — terminology collision.
     v4.0 framing: PFC = Lawyer + Learning Trajectory (Logic-Feeling.md v4.0 §4.3).
     = PFC serves body-base (Lawyer). Fresh → compile → Body-Knowing (Learning Trajectory).
     = Same insight, at mechanism level, avoiding the collision-prone term "feeling."
```

---

## §9 — INTER-BODY: INTERACTION LABELS (★ NEW v2.0)

```
⭐ VOCABULARY FOR INTER-BODY INTERACTION (Inter-Body-Mechanism.md):

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A) BY-PRODUCT MATCH / ANTI-MATCH (Inter-Body §5.4, By-Product-Gap-Resonance v1.0):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ by-product match        │ B fills gap OF B (§2C) → output =        │
  │                         │ by-product → matches A's gap direction   │
  │                         │ → A receives reward.                     │
  │                         │ = FOUNDATIONAL mechanism of inter-body   │
  │                         │ feeding.                                 │
  │                         │ Use: when describing HOW 2 entities      │
  │                         │ feed each other.                         │
  │                         │                                          │
  │ anti-match              │ By-product CONFLICTS gap direction (§2C).│
  │                         │ Worse than no-match = ACTIVE friction.   │
  │                         │ e.g., innovation-driven CEO ↔            │
  │                         │ change-averse employee.                  │
  │                         │ Use: when by-product causes dissonance.  │
  │                         │                                          │
  │ mutual match            │ BOTH parties receive reward from         │
  │ (= Resonance)           │ interaction. A matches B AND B matches A.│
  │                         │ Use: when both parties have by-product   │
  │                         │ match.                                   │
  │                         │                                          │
  │ one-way match           │ Only 1 party receives reward.            │
  │                         │ e.g., parasocial relationships,          │
  │                         │ asymmetric service.                      │
  │                         │ Use: when match is not mutual.           │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  B) 2-STREAM ARCHITECTURE (By-Product-Gap-Resonance v1.0 §2):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Hardware-Stream         │ Hardware/Unidirectional by-product match.│
  │ (hardware/unidirect.)   │ Reward from the OTHER's EXISTENCE/       │
  │                         │ attributes. Does not require reciprocal  │
  │                         │ engagement. HABITUATES (Weber-Fechner).  │
  │                         │ Experienced SEPARATELY (each side        │
  │                         │ unaware of the other's experience).      │
  │                         │ Use: when reward comes from presence/    │
  │                         │ attribute.                               │
  │                         │                                          │
  │ Modeling-Stream         │ Self-Pattern-Modeling compiled mutual    │
  │ (Self-Pattern-Modeling  │ (bidirectional). REQUIRES both parties   │
  │  mutual)                │ to engage Self-Pattern-Modeling →        │
  │                         │ feedback loop. 2 brains SYNCHRONIZED.    │
  │                         │ Can CHANGE other's state.                │
  │                         │ ANTI-HABITUATION (Hebbian → stronger).   │
  │                         │ Unsustainable if 1-sided.                │
  │                         │ Use: when describing deep mutual         │
  │                         │ connection.                              │
  │                         │                                          │
  │ Proto-Modeling-Stream   │ Modeling-Stream primitive (without full  │
  │                         │ Self-Pattern-Modeling).                  │
  │                         │ Mother-infant: contingent response.      │
  │                         │ Human-dog: associative matching.         │
  │                         │ Use: when there is mutual exchange but   │
  │                         │ without full bilateral                   │
  │                         │ Self-Pattern-Modeling.                   │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  C) 3 INDEPENDENT COST SOURCES (Inter-Body §4):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ cost (general)          │ TOTAL COST = ① + ② + ③.                 │
  │                         │ Use: when speaking generally about       │
  │                         │ "costly interaction."                    │
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
  │                         │ Use: when describing suppression of      │
  │                         │ an impulse.                              │
  │                         │                                          │
  │ ③ uncertainty cost      │ Multiple options, none compiled → hold   │
  │                         │ open → cortisol. f(options×time×stakes). │
  │                         │ = No known answer → must wait → stress.  │
  │                         │ Use: when describing uncertainty/        │
  │                         │ not knowing.                             │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ 3 cost sources INDEPENDENT (can appear separately or simultaneously)
  ⚠️ SUSTAINABILITY = f(total cost × frequency ÷ reward)
  ⚠️ Cost does NOT come from "using logic" per se — it comes from these 3 specific sources
  ⚠️ Connection to §2: high cost + body-need not filled = unsustainable

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  D) 5-CHANNEL INPUT VECTOR (Inter-Body §6):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Ch1 — Hardware Sensory  │ Domain reality input NOW.                │
  │                         │ Visual, auditory, tactile, olfactory.    │
  │                         │                                          │
  │ Ch2 — Body State        │ Internal homeostasis.                    │
  │                         │ Hormone, glucose, cortisol, fatigue.     │
  │                         │                                          │
  │ Ch3 — Compiled Chunks   │ Associative fire from past.              │
  │                         │ Memory, pattern, schema, habit loops.    │
  │                         │                                          │
  │ Ch4 — Entity Actions    │ What others DO/SAY.                      │
  │                         │ Words, facial expression, behavior.      │
  │                         │                                          │
  │ Ch5 — PFC Active Chain  │ Reasoning in progress.                   │
  │                         │ Ongoing cognitive process → feedback.    │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Channel DOMINANT → determines vulnerability:
     Ch1 dominant = grounded in reality (protected)
     Ch4 dominant = entity controls activation (vulnerable)
     Multiple channels CONFIRM = strong drive (hard to manipulate)
     Single channel ONLY = dangerous (scam, limerence)

  ⚠️ "Input Channel Control = Power":
     Whoever controls another's input channels = controls their behavior
     (Scam: control Ch4 + amplify Ch2 + block Ch1 = victim follows)
  ⚠️ Connection to §2: 5 channels = 5 ways to ACTIVATE body-need

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  E) SUPPLEMENTARY LABELS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Definition + when to use                 │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Compilable Architecture │ Human system: general-purpose reward +   │
  │                         │ compilation + social hardware.           │
  │                         │ Trade-off: flexible but 15-20yr compile. │
  │                         │ (vs Hardwired Architecture:              │
  │                         │  specific-reward)                        │
  │                         │ Use: when explaining WHY the human       │
  │                         │ system works this way.                   │
  │                         │ (Inter-Body §1.2)                        │
  │                         │                                          │
  │ PFC = Lawyer            │ PFC creates a narrative FOR the          │
  │                         │ body-base. NOT a neutral judge —         │
  │                         │ advocates for the client.                │
  │                         │ Body-need (§2) fires FIRST → PFC         │
  │                         │ justifies.                               │
  │                         │ Use: when analyzing PFC narrative ≠      │
  │                         │ actual body-need.                        │
  │                         │ (Inter-Body §7, Gazzaniga split-brain)   │
  │                         │                                          │
  │ Domain Reality          │ Final arbiter. CANNOT be permanently     │
  │ = Final Arbiter         │ fooled. Timeline varies (seconds→years). │
  │                         │ Dual Check: body=quality controller,     │
  │                         │ domain=final arbiter.                    │
  │                         │ Use: when noting that "reality will      │
  │                         │ verify."                                 │
  │                         │ (Inter-Body §6.4, Ask-AI v3.1)          │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘
```

---

## §10 — OBSERVATION VS MECHANISM (DIFFERENT LAYERS)

```
⭐ BODY-FEEDBACK ≠ FEELING — 2 DIFFERENT LAYERS:

  ┌──────────────────┬───────────────────────────────────────────────┐
  │ Layer            │ Description                                   │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ BODY-FEEDBACK    │ MECHANISM: signal from body → runs 24/7       │
  │ (mechanism)      │ 95% UNCONSCIOUS (PFC cannot observe)          │
  │                  │ Labels: body-need, gap, reward, dissonance,   │
  │                  │ prediction-delta, chunk-miss/shift/gap,       │
  │                  │ Compiled/Fresh, 3-cost, 5-Channel (§2-§9)    │
  │                  │ = THIS FILE describes the vocabulary of       │
  │                  │ this layer                                    │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ FEELING          │ OBSERVATION: PFC observes body-feedback       │
  │ (observation)    │ 7-layer gradient (implicit → explicit)        │
  │                  │ Labels: "pleasant" / "comfortable" /          │
  │                  │ "satisfied" / "vague" / "nagging unease" /    │
  │                  │ "discomfort" / "stuck" / "emptiness" /        │
  │                  │ "apathetic"                                   │
  │                  │ = Feeling.md v2.2 describes the vocabulary    │
  │                  │ of this layer                                 │
  └──────────────────┴───────────────────────────────────────────────┘

  ⚠️ COMMON CONFUSIONS:

    "Pleasant" ≠ reward:
      → "Pleasant" = PFC observation of body-base reward
        (Feel-Location/Feel-Labeling: already observed + labeled)
      → Reward can RUN while PFC does not observe
        (Feel-RawSignals/Feel-Integration: body signal but PFC hasn't detected it yet)
      → = Body-base reward OCCURS without "feeling pleasant" (this is possible)

    "Discomfort" ≠ dissonance:
      → "Discomfort" = PFC observation OF dissonance signal
      → Dissonance runs 24/7, PFC only observes a small fraction
      → = "Background-Pattern" dissonance = invisible (Background-Pattern.md)

    "Intuition" ≠ only feeling:
      → "Intuition" = compiled processing (§8: applies to ALL domains: math, emotion alike)
      → A chef "knowing" the dish needs salt = intuition = COMPILED (not "feeling only")
      → True axis: Compiled/Fresh — not Logic/Feeling content

  (Feeling.md v2.2: feeling = PFC observation of body-feedback)
  (01-Foundation.md §5: 7-layer clarity gradient)
```

---

## §11 — USAGE RULES

### §11.1 — Core Principles

```
⭐ AS SPECIFIC AS POSSIBLE. AS GENERAL AS NECESSARY.

  ① Tier 3 > Tier 2 > Tier 1:
     If chain is traceable → Tier 3 ("chunk-miss → SNC → cortisol Role ②")
     If direction is known → Tier 2 ("body-base reward" / "dissonance")
     If only +/- is known → Tier 1 ("positive/negative body-feedback")

  ② DO NOT merge prediction-delta with body-base reward:
     "prediction-delta" = detection (Step 2)
     "body-base reward" = evaluation (Step 5)
     = 2 DIFFERENT events, CAN occur INDEPENDENTLY

  ③ "reward" = body-base reward (BOTH Evaluative AND Direct-State):
     NOT limited to opioid / Evaluative
     Direct-State (touch, exercise, warmth) = genuine reward, CORRECT label

  ④ DISTINGUISH compiled (tags) vs momentary (signals):
     Approach/avoidance = accumulated onto chunks (§7)
     Reward/dissonance = occurring right now (§3/§4)

  ⑤ DISTINGUISH mechanism (body-feedback) vs observation (feeling):
     Body-feedback labels: reward, dissonance, prediction-delta,...
     Feeling labels: "pleasant", "comfortable", "satisfied",
       "vague", "nagging unease", "discomfort",
       "stuck", "emptiness", "apathetic"
     Do NOT use feeling labels in place of body-feedback labels (§10)

  ⑥ USE "Compiled/Fresh" when analyzing mechanism:
     "Logic/Feeling" = ok for describing from the outside (observer perspective)
     "Compiled/Fresh" = REQUIRED for deep analysis (mechanism level)
     Do NOT say "feeling conflicts with logic" → say "compiled conflicts with fresh" (§8)

  ⑦ 3-COST = 3 separate sources, DO NOT merge:
     "Fatigue" can = ① PFC draft, ② suppress, ③ uncertainty, or COMBO
     Label the SPECIFIC cost source → understand mechanism → know how to reduce it (§9C)

  ⑧ ENTITY-COMPILED ≠ APPROACH TAG:
     Approach tag = per-chunk, simple (+/-) (§7 Layer 1)
     Entity-Compiled = per-entity, multi-channel, structural (§7 Layer 2)
     Do NOT say "approach tag toward mother"
     → say "Entity-Compiled mixed (mother)"

  ⑨ BODY-NEED = the foundation, NOT a signal:
     Body-need (§2) = STATE (state of NEED — ALWAYS exists)
     Body-feedback = SIGNAL (body REPORTS about state)
     Do NOT say "body-need fires" → say "body-feedback fires because of body-need X"
     Body-need = CONTEXT, body-feedback = COMMUNICATION
```

### §11.2 — Application Examples

```
  EXAMPLE 1: Salary increase from 10M → 15M VND

  TIER 2 (sufficient for Research files):
    "Body-need [survival] has gap [income].
     10M → body-base reward (gap fills in the right direction) → habituated.
     15M → smaller prediction-delta → diminished reward (gap has shrunk)."

  TIER 3 (for deep analysis):
    "Body-need [survival] has gap [income direction: ≥10M VND/month].
     10M (first time):
       prediction-delta (novel) → DRD4 pass → PFC spotlight
       → body-base check: chunk [10M salary] matches gap direction
       → Evaluative Reward
       → chunk compile: [10M salary = approach tag]
     10M (month 12):
       habituated: same pattern → no prediction-delta → no alert
       → gap IS filled → body-feedback baseline
     15M:
       prediction-delta (differs from 10M baseline) → body-base check
       → gap shrink (mostly filled) → diminished reward
       → = Diminishing returns = gap shrink over time"


  EXAMPLE 2: Mother-child conflict (inter-body):

  TIER 2:
    "Child: Entity-Compiled mixed (mother). Hardware-Stream habituated.
     Modeling-Stream exists but with conflicting direction.
     Cost: ② suppress high (impulse suppression) + ③ uncertainty (mother unpredictable).
     By-product: mother fills gap OF THE MOTHER (teaching) → output anti-matches
     child's gap direction (autonomy)."

  TIER 3:
    "Child: Entity-Compiled mixed [nutrition++, comfort++, autonomy--, status+/-]
     Body-need [autonomy] has gap [direction: self-determination].
     Mother says 'you must study': Ch4 dominant → compiled chunks Ch3 fire
     [prohibition schema] → body-state Ch2 cortisol ↑
     → suppress cost ② (compiled response wants to push back but suppressed)
     → uncertainty cost ③ (will mother punish or relent?)
     → dissonance: chunk-gap [autonomy direction blocked]
     By-product mechanism: Mother fills gap 'raising well' (HER OWN gap)
     → output = forcing study → anti-matches child's gap direction [freedom to explore]
     PFC = Lawyer: child's narrative 'mother doesn't understand me' (may be 0.3 accuracy)"
```

---

## §12 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback.md v1.1            │ ENTRY POINT. §4 4 axes.              │
  │                                  │ §6 Body-Feedback-Precondition.       │
  │                                  │ Read BEFORE this file.              │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Mechanism.md v2.0  │ §1 Body-Need aggregate. §2 2 sources.│
  │                                  │ §3 3 dynamics. Tier 3 labels.        │
  │                                  │ SOURCE for §2 Foundation.            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Inter-Body-Mechanism.md v1.0     │ §2 Body-Need. §3 Compiled/Fresh.    │
  │                                  │ §4 3-cost. §5 By-product match.     │
  │                                  │ §6 5-Channel. §7 PFC=Lawyer.        │
  │                                  │ §8 Entity-Compiled.                  │
  │                                  │ SOURCE for §8+§9 of this file.      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gap-Direction.md v2.0            │ §1 Definition: gap = f(surrounding   │
  │                                  │ chunks). "What you don't know        │
  │                                  │ creates no gap."                     │
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
  │                                  │ Compiled vs momentary distinction.   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ By-Product-Gap-Resonance.md v1.0 │ §2 2-Stream Architecture.            │
  │                                  │ Hardware-Stream/Modeling-Stream/     │
  │                                  │ Proto labels defined.                │
  │                                  │ By-product match + anti-match.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Feeling.md v2.2                  │ PFC observation of body-feedback.    │
  │                                  │ 7-layer gradient. DIFFERENT LAYER    │
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
  │                                  │ THE ONLY PLACE to discuss            │
  │                                  │ terminology outside the framework +  │
  │                                  │ why the framework uses different      │
  │                                  │ labels.                              │
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
> *§8 Processing: Compiled/Fresh = the true axis (Logic/Feeling = observer labels).*
> *§9 Inter-Body: by-product match, 2-Stream, 3-cost, 5-Channel.*
> *§10 Distinction: body-feedback (mechanism) ≠ feeling (observation).*
>
> *Body-need = STATE. Body-feedback = SIGNAL. Gap direction = WHY match works.*
> *"Doorbell" ≠ "gift behind the door."*
