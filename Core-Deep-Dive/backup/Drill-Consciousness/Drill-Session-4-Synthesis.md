---
title: "Synthesis: Phase A + Phase B + Phase C → v1.5 Execution Plan"
version: v2.0
date: 2026-07-01
type: SYNTHESIS (Phase A+B original, Phase C update)
status: v2.0 — Phase C findings integrated
scope: |
  v1.0: Merged Phase A (6 sessions) + Phase B (3 sessions) → v1.5 plan.
  v2.0: Integrated Phase C (2 sessions) → updated v1.5 plan.
  Convergence map expanded (8 → 11 themes), 1 new SHOULD item (S10),
  1 SHOULD item modified (S7 broadened).
input_sessions:
  phase_a:
    - "Session 1: Hydranencephaly → Level 0, subcortical consciousness"
    - "Session 2: Dreaming → PFC = enabler not source, sustain hierarchy"
    - "Session 3: Split-Brain → state vs content broadcast, subcortical unity"
    - "Session 4: Blindsight → recurrence necessary, RPT integration"
    - "Session 5: Thalamic Gating → 3-role thalamus, 5-checkpoint"
    - "Session 6: Mechanism v2.0 synthesis → all integrated"
  phase_b:
    - "Session 1: Consciousness Quality Model → temporal dynamics, chunk density"
    - "Session 2: Body State × Consciousness → bidirectional modulation, paradox"
    - "Session 3: ADHD × Consciousness → sustain hierarchy dissociation"
  phase_c:
    - "Session 1: Hallucination × Consciousness Architecture → source attribution, 5-CP confirmed"
    - "Session 2: Intrusive/Persistent Patterns × Control → 3 failure modes, ironic process, PTSD"
input_files:
  - "Drill-Thalamo-Cortical-Mechanism.md v2.0 (Phase A synthesis)"
  - "Drill-Consciousness-Counterexamples.md v2.0 (Phase A counterexamples)"
  - "Drill-Thalamic-Gating.md v1.0 (Phase A Session 5)"
  - "Drill-Consciousness-Quality-Model.md v1.0 (Phase B Session 1)"
  - "Drill-Body-State-Consciousness.md v1.0 (Phase B Session 2)"
  - "Drill-ADHD-Consciousness.md v1.0 (Phase B Session 3)"
  - "Drill-Hallucination-Consciousness.md v1.0 (Phase C Session 1)"
  - "Drill-Intrusive-Consciousness.md v1.0 (Phase C Session 2)"
  - "Consciousness.md v1.4 (current target file)"
  - "Core-Software.md v3.4 (secondary target file)"
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Synthesis: Phase A + Phase B + Phase C → v1.5 Execution Plan

> **11 drill sessions. 6 counterexamples. 3 dynamics stress-tests. 2 control drills.**
> **One finding repeats across all of them:**
>
> **The 3-parameter model is ROBUST. No new parameters needed.**
> **But: temporal dynamics, sustain hierarchy, thalamic architecture,**
> **and source attribution need to be made EXPLICIT in the framework.**
>
> **v1.5 = make the implicit explicit.**

---

## Table of Contents

- [§0 — Executive Summary](#0--executive-summary)
- [§1 — Phase A Recap: Counterexample Drill (6 Sessions)](#1--phase-a-recap)
- [§2 — Phase B Recap: Dynamics Drill (3 Sessions)](#2--phase-b-recap)
- [§2.5 — Phase C Recap: Control Drill (2 Sessions)](#25--phase-c-recap)
- [§3 — Convergence Map (A + B + C)](#3--convergence-map)
- [§4 — Merged & Deduplicated Change List](#4--merged--deduplicated-change-list)
- [§5 — Prioritized v1.5 Changes (MUST / SHOULD / COULD)](#5--prioritized-v15-changes)
- [§6 — File-by-File Change Specification](#6--file-by-file-change-specification)
- [§7 — Execution Plan: Phases & Dependencies](#7--execution-plan)
- [§8 — Cross-Reference Impact Assessment](#8--cross-reference-impact)
- [§9 — Scope Estimation](#9--scope-estimation)
- [§10 — Bias Checklist for Execution](#10--bias-checklist)
- [§11 — Cross-References](#11--cross-references)

---

## §0 — Executive Summary

```
⭐ v2.0 = PHASE C INTEGRATED INTO v1.5 PLAN.
   v1.0 merged 9 sessions (Phase A + B). v2.0 adds Phase C (2 sessions).
   Total: 11 drill sessions → one comprehensive v1.5 execution plan.

   INPUT:
     Phase A (Counterexample Drill): 6 sessions, 8 framework change items
     Phase B (Dynamics Drill): 3 sessions, 14 enrichment recommendations
     Phase C (Control Drill): 2 sessions, 5 new concepts identified  ← NEW

   PHASE C VERDICT:
     → 1 NEW SHOULD item: S10 Source Attribution dimension
     → 1 MODIFIED SHOULD item: S7 broadened (body-state → domain-general)
     → 3 concepts → drill/PFC-Ops only (too detailed for Consciousness.md)
     → Framework CONFIRMED by 2 more independent stress-tests

   AFTER DEDUPLICATION:
     4 MUST changes (correct inaccuracies — UNCHANGED from v1.0)
     10 SHOULD changes (was 9 — added S10 Source Attribution)
     8 COULD changes (nice to have — UNCHANGED from v1.0)

   KEY FINDING — CONVERGENCE (updated):
     11 themes confirmed by MULTIPLE independent sessions (was 8):
       ① 3-parameter model ROBUST (B ×3, C ×2)
       ② Sustain hierarchy = 2-tier (A ×3, B ×1, C ×1)
       ③ PFC = enabler not source (A ×3, B ×1, C ×2)
       ④ Temporal dimension needs explicitness (B ×2)
       ⑤ Thalamus = 3 roles not monolithic (A ×5, C ×1)
       ⑥ Meta-consciousness = domain-general (B ×2)
       ⑦ Modulators affect all 3 params simultaneously (B ×4)
       ⑧ Recurrence + broadcast = complementary (A ×2, C ×1)
       ⑨ Source monitoring = independent dimension (C ×2)          ← NEW
       ⑩ Self-referential paradox = domain-general (B ×1, C ×1)   ← NEW
       ⑪ PFC suppress has structural limits (C ×2)                ← NEW

   CROSS-REFERENCE IMPACT: MINIMAL (unchanged)
     → All changes = subsection additions or modifications
     → NO top-level section renumbering in Consciousness.md
     → NO section renumbering in Core-Software.md
     → Estimated: <5 cross-reference fixes

   ESTIMATED EXECUTION:
     Phase 1 (MUST): ~60-80 lines, 1 session
     Phase 2 (SHOULD): ~115-170 lines, 1-2 sessions (was ~100-150)
     Phase 3 (COULD): ~80-100 lines, 1 session (optional)
     Phase 4 (Core-Software.md): ~30-50 lines, within Phase 1
     Phase 5 (Cross-refs + verify): ~30 min
```

---

## §1 — Phase A Recap: Counterexample Drill (6 Sessions)

```
⭐ PHASE A = ARCHITECTURAL STRESS-TEST:
  "Can the framework handle conditions where consciousness is unusual?"

  6 COUNTEREXAMPLES DRILLED:
    S1 Hydranencephaly: consciousness WITHOUT cortex?
    S2 Dreaming: consciousness WITHOUT PFC?
    S3 Split-Brain: consciousness WITHOUT corpus callosum?
    S4 Blindsight: processing WITHOUT consciousness?
    S5 Thalamic Gating: WHY is >95% processing unconscious?
    S6 Mechanism Synthesis: integrate all findings

  8 v1.5 ITEMS IDENTIFIED (from Drill-Thalamo-Cortical-Mechanism.md §cross-refs):

    ① SCOPE STATEMENT: framework = Level 2 (access consciousness)
       Acknowledge L0 (affective), L1 (phenomenal), L3 (meta) exist
       but are NOT modeled. Framework's "knowing" = L2 = VALID.
       Evidence: hydranencephaly (L0), dreaming (L1), lucid dreaming (L3)

    ② RECURRENCE before broadcast: RPT (CP4) + GWT (CP5) integration
       Currently: signal → ignition → broadcast → knowing
       Change to: signal → recurrence (Lamme) → broadcast (Dehaene) → knowing
       Evidence: blindsight (no V1 → no awareness), TMS timing, COGITATE 2025

    ③ PFC REFINEMENT: dlPFC ≠ vmPFC, enabler not source
       dlPFC: executive, WM, judgment — OFF during dreaming
       vmPFC: emotion, self-reference — ON during dreaming
       Content generated in posterior cortex (Koch hot zone, COGITATE 2025)
       Evidence: dreaming, frontal lobectomy, Voss 2014 (lucid → causal)

    ④ 3-ROLE THALAMUS: replace monolithic "backbone"
       Role 1 — STATE CONTROL: tonic/burst, TRN, CM-Pf ("Is stage lit?")
       Role 2 — CONTENT GATE: TRN gating, high-order nuclei ("Who enters?")
       Role 3 — ROUTING HUB: pulvinar, transthalamic relay ("Stage manager")
       Evidence: convergent across ALL 5 sessions

    ⑤ 5-CHECKPOINT PATHWAY:
       CP1 TRN gate → CP2 tonic mode → CP3 high-order nuclei →
       CP4 cortical recurrence → CP5 global broadcast
       Every consciousness failure maps to specific checkpoint(s)
       Evidence: independent prior evidence for each CP

    ⑥ SUSTAIN HIERARCHY: primary (thalamo-cortical + CM-Pf) vs
       additional (PFC WM hold + limbic drive)
       Evidence: dreaming (PFC off → consciousness exists),
       anesthesia (thalamus off → consciousness abolished)

    ⑦ TONIC vs BURST prerequisite: thalamic firing mode gates consciousness
       Tonic = consciousness-compatible; burst = consciousness-incompatible
       Evidence: NREM, anesthesia, Comm Bio 2026

    ⑧ "KNOWING" INTERNAL vs EXTERNAL dimension:
       Internal knowing = experiencing within the state (dreaming: present)
       External knowing = report, act, remember (dreaming: absent)
       Lucid dreaming = internal + external knowing
       Note: v1.4 PARTIALLY addressed via disambiguation (§1.5)
```

---

## §2 — Phase B Recap: Dynamics Drill (3 Sessions)

```
⭐ PHASE B = REAL-WORLD STRESS-TEST:
  "How does consciousness WORK in everyday extreme conditions?"

  3 SESSIONS DRILLED:

  ─────────────────────────────────────────────────────────────────
  SESSION 1 — CONSCIOUSNESS QUALITY MODEL:
  ─────────────────────────────────────────────────────────────────

    CORE FINDING: 3-parameter model is ALREADY dynamic.
    f(signal(t) × anchor(t) × attention(t)) — parameters change at each t.
    The "gap" = model doesn't make temporal dynamics EXPLICIT, not that
    it lacks them.

    ENRICHMENT RECOMMENDATIONS:
      SHOULD: ① Explicit temporal dynamics in §2.1
      SHOULD: ② Post-threshold resolution (chunk density → richer content)
      SHOULD: ③ 3 types of forgetting (know-you-forgot / don't-know / triggered)
      COULD:  ④ Prediction-delta as multi-parameter modulator
      COULD:  ⑤ Pattern lifecycle description (entry → hold → compete → exit)

    STATUS: 3-parameter model MORE COMPLETE than preliminary analysis suggested.


  ─────────────────────────────────────────────────────────────────
  SESSION 2 — BODY STATE × CONSCIOUSNESS:
  ─────────────────────────────────────────────────────────────────

    CORE FINDING: Body state = BIDIRECTIONAL MODULATOR.
    Direction 1: body → modulates all 3 consciousness parameters
    Direction 2: consciousness → observes body state (but PFC = Lawyer)
    Paradox: signal can impair its own detector (cortisol → PFC ↓)

    ENRICHMENT RECOMMENDATIONS:
      SHOULD: ① Self-referential paradox note (signal impairs detector)
      SHOULD: ② State vs Cause consciousness split (STATE easy, CAUSE hard)
      COULD:  ③ Bidirectional loop note
      COULD:  ④ Body-state developmental trajectory
      NOT NEEDED: Interoception as separate parameter (= domain clarity)

    STATUS: Framework has EXTENSIVE body-state coverage (6+ files).
    Gap = IMPLICIT connections, not missing content.


  ─────────────────────────────────────────────────────────────────
  SESSION 3 — ADHD × CONSCIOUSNESS ARCHITECTURE:
  ─────────────────────────────────────────────────────────────────

    CORE FINDING: ADHD = natural experiment DISSOCIATING sustain hierarchy.
    Primary sustain (thalamo-cortical) = INTACT → consciousness EXISTS.
    Additional sustain (PFC WM hold) = IMPAIRED → quality reduced.
    Limbic drive = ENHANCED → compensates.
    Hyperfocus = RESTORATION of additional sustain via reward dopamine.

    ENRICHMENT RECOMMENDATIONS:
      SHOULD: ① Temporal dimension in §2.1 (= Session 1 SHOULD ①, MERGE)
      SHOULD: ② ADHD as sustain hierarchy evidence (extends Phase A ⑥, MERGE)
      COULD:  ③ Attention parameter richness (distribution not just magnitude)
      COULD:  ④ Limbic drive as functional sustain substitute
      NOT NEEDED: ADHD as separate consciousness disorder

    STATUS: 3-parameter model captures ADHD as TEMPORAL PROFILE
    (adequate at t₀, decays fast) — NOT deficit profile.
```

---

## §2.5 — Phase C Recap: Control Drill (2 Sessions)

```
⭐ PHASE C = CONTROL STRESS-TEST:
  "What happens when patterns resist PFC control?"
  Added in v2.0 — runs BEFORE v1.5 execution to check for gaps.

  2 SESSIONS DRILLED:

  ─────────────────────────────────────────────────────────────────
  SESSION 1 — HALLUCINATION × CONSCIOUSNESS ARCHITECTURE:
  ─────────────────────────────────────────────────────────────────

    CORE FINDING: All 5 CPs pass, but with WRONG SOURCE.
    5-CP describes pathway, source monitoring describes attribution.
    These are INDEPENDENT dimensions.

    NEW CONCEPTS:
      ① Source Attribution dimension (strongest v1.5 candidate)
        → All CPs pass + source monitoring fails = hallucination
        → All CPs pass + source monitoring intact = Charles Bonnet
        → = New dimension ON 5-CP model, not a new parameter
      ② "Different Doors, Same Theater" principle
        → 6 types (schizophrenic, psychedelic, hypnagogic, CB,
          sensory deprivation, fever) → different entry, same loop
      ③ Predictive coding × precision weighting connection
      ④ Source monitoring continuum (imagination → hallucination)

    CONFIRMED: 3-param ROBUST, 5-CP ROBUST, sustain hierarchy,
      PFC = enabler, "knowing" can be wrong about reality

    v1.5 CANDIDATE: ① Source Attribution = NEW SHOULD item


  ─────────────────────────────────────────────────────────────────
  SESSION 2 — INTRUSIVE/PERSISTENT PATTERNS × CONTROL:
  ─────────────────────────────────────────────────────────────────

    CORE FINDING: PFC suppress has 3 STRUCTURALLY DIFFERENT failure modes:
      MISMATCH: signal in self-sustaining loop > PFC capacity
      PARADOX: suppress command CONTAINS the target
      DEPLETION: PFC budget exhausted → suppress = zero

    NEW CONCEPTS:
      ① 3 failure modes of PFC suppress (mismatch, paradox, depletion)
      ② Ironic process = Hold/Suppress structural property (Wegner 1987)
      ③ Rumination = self-referential paradox applied to THOUGHT
        → Extends Phase B Session 2 finding from body-state to domain-general
      ④ PTSD through 5-CP confirms Source Attribution (hippocampal context)
      ⑤ 6 exit mechanisms mapped across all intrusive types

    CONFIRMED: PFC Hold/Suppress, PFC budget finite, biased competition
      (+ boundary defined), self-referential paradox domain-general,
      cortisol vicious cycle in thought domain, Background-Pattern Triple Bias

    v1.5 CANDIDATES:
      → S7 broadened: paradox = domain-general, not body-specific
      → Source Attribution: STRENGTHENED by PTSD confirmation
      → 3 failure modes: better as PFC-Operations enrichment
      → Ironic process: better as PFC-Operations enrichment
      → Exit mechanisms: drill-only (too detailed)
```

---

## §3 — Convergence Map

```
⭐ 11 THEMES CONFIRMED BY MULTIPLE INDEPENDENT SESSIONS:
  (v2.0: updated with Phase C — themes 1-8 from v1.0, themes 9-11 NEW)

  ┌───┬──────────────────────────────┬──────────────────────────────┬────────────┐
  │ # │ Theme                        │ Sessions Confirming          │ Confidence │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 1 │ 3-parameter model ROBUST     │ B-S1, B-S2, B-S3,           │ 🟢→🟡     │
  │   │ (no new parameters needed)   │ C-S1, C-S2 (5 sessions)     │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 2 │ Sustain hierarchy = 2-tier   │ A-S2, A-S5, A-S6,           │ 🟢→🟡     │
  │   │ (primary vs additional)      │ B-S3, C-S1 (5 sessions)     │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 3 │ PFC = enabler, NOT source    │ A-S2, A-S4, A-S5,           │ 🟢→🟡     │
  │   │ (dlPFC ≠ vmPFC)             │ B-S3, C-S1, C-S2 (6 sess)   │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 4 │ Temporal dimension needed    │ B-S1, B-S3                   │ 🟡        │
  │   │ (parameters evolve over t)   │ (2 sessions)                 │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 5 │ Thalamus = 3 distinct roles  │ A-S1 through A-S5,           │ 🟢→🟡     │
  │   │ (state, gate, route)         │ C-S1 (6 sessions)            │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 6 │ Meta-consciousness =         │ B-S2, B-S3                   │ 🟡        │
  │   │ domain-general mechanism     │ (2 sessions)                 │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 7 │ Modulators affect all 3      │ B-S1 ×2, B-S2, B-S3         │ 🟡        │
  │   │ params simultaneously        │ (4 examples)                 │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 8 │ Recurrence + broadcast =     │ A-S4, A-S5,                  │ 🟢→🟡     │
  │   │ complementary (RPT + GWT)    │ C-S1 (3 sessions)            │            │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │ 9 │ Source monitoring =          │ C-S1, C-S2                   │ 🟡        │
  │   │ independent dimension on     │ (2 sessions: hallucination   │            │
  │   │ 5-CP model                   │ + PTSD, different causes)    │ NEW v2.0   │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │10 │ Self-referential paradox =   │ B-S2, C-S2                   │ 🟡        │
  │   │ domain-general (not body-    │ (2 sessions: body-state      │            │
  │   │ state specific)              │ + thought-content)           │ NEW v2.0   │
  ├───┼──────────────────────────────┼──────────────────────────────┼────────────┤
  │11 │ PFC suppress has structural  │ C-S1, C-S2                   │ 🟡        │
  │   │ limits, not just capacity    │ (2 sessions: mismatch +      │            │
  │   │ limits                       │ paradox + depletion)         │ NEW v2.0   │
  └───┴──────────────────────────────┴──────────────────────────────┴────────────┘


  ⭐ META-FINDING — PHASE B STRUCTURAL PATTERN:

    Every Phase B session tested a CANDIDATE new parameter:
      S1: chunk density → NOT parameter, = precondition
      S1: prediction-delta → NOT parameter, = modulator
      S2: interoception → NOT parameter, = domain clarity
      S3: ADHD temporal profile → NOT parameter, = temporal envelope

    STRUCTURAL PATTERN:
      f(signal × anchor × attention) = the 3 INDEPENDENT dimensions.
      Everything else either:
        a) Affects all 3 simultaneously → = MODULATOR / PRECONDITION
        b) Is a temporal property of existing parameters → = ENVELOPE
        c) Is a domain-specific application → = SAME model, different domain

    This pattern ITSELF is a finding worth noting in v1.5.


  ⭐ CONVERGENCE: ADHD + DREAMING → SUSTAIN HIERARCHY

    Two INDEPENDENT conditions reaching SAME conclusion from OPPOSITE directions:

    DREAMING approach:      REMOVE PFC completely (offline during sleep)
      → Consciousness EXISTS (vivid dreams, emotional content)
      → Primary sustain SUFFICIENT for consciousness existence

    ADHD approach:          REDUCE PFC function (under-fueled chronically)
      → Consciousness EXISTS but quality REDUCED
      → Additional sustain impaired, primary sustain intact

    → BOTH → PFC = ADDITIONAL sustain, NOT PRIMARY
    → = 2-tier sustain hierarchy CONFIRMED by 2 independent conditions
    → = Strongest convergent evidence across all 11 sessions


  ⭐ META-FINDING — PHASE C STRUCTURAL PATTERN (NEW v2.0):

    Phase C tested whether CONTROL FAILURES reveal architecture gaps:

    SESSION 1 (hallucination):
      → 5-CP pathway = ROBUST (all types map cleanly)
      → BUT: pathway describes WHETHER conscious, not whether VERIDICAL
      → = Source Attribution is an INDEPENDENT dimension on 5-CP
      → Johnson et al. 1993 (source monitoring) + Brewin 2010 (S-rep/C-rep)

    SESSION 2 (intrusive patterns):
      → PFC suppress fails for 3 STRUCTURALLY DIFFERENT reasons
      → NOT "PFC is weak" but "suppress has 3 distinct failure modes"
      → Self-referential paradox extends from body-state to thought-content
      → = The paradox is a GENERAL PROPERTY of cortisol × PFC interaction

    STRUCTURAL PATTERN:
      Control failures REVEAL architecture more precisely than normal
      operation does. Just as Phase B found that stress-tests confirm
      the 3-parameter model, Phase C found that control failures
      confirm the 5-CP and sustain hierarchy — AND reveal what those
      models DON'T yet capture (source attribution).


  ⭐ CONVERGENCE: HALLUCINATION + PTSD → SOURCE ATTRIBUTION (NEW v2.0)

    Two INDEPENDENT conditions reaching SAME conclusion from DIFFERENT causes:

    HALLUCINATION approach:  Internal signal → all 5 CPs pass
      → Source monitoring fails (mPFC/corollary discharge broken)
      → Patient BELIEVES content is real (schizophrenia)
      → OR: patient KNOWS it's not real (Charles Bonnet, mPFC intact)

    PTSD approach:          Trauma memory → all 5 CPs pass
      → Source monitoring fails (hippocampal CONTEXT absent)
      → S-rep fires without C-rep → feels PRESENT not PAST
      → = Brewin 2010: different mechanism, same result

    → BOTH → Source monitoring = INDEPENDENT of consciousness PATHWAY
    → "Different Doors, Same Theater" confirmed for 2nd time
    → = Source Attribution dimension justified by convergent evidence
```

---

## §4 — Merged & Deduplicated Change List

```
⭐ ALL RECOMMENDATIONS COMPILED, DUPLICATES MERGED:

  DEDUPLICATION LOG:

    MERGE 1: Phase B S1-① (temporal dynamics) + S3-① (temporal in §2.1)
      → Single item: "Temporal dynamics explicit in §2.1"
      → Reason: same recommendation from 2 independent sessions

    MERGE 2: Phase A ⑥ (sustain hierarchy) + Phase B S3-② (ADHD evidence)
      → Single item: "Sustain hierarchy + ADHD/dreaming convergence evidence"
      → Reason: S3 adds evidence to A's structural recommendation

    v2.0 ADDITIONS FROM PHASE C:

    NEW: Phase C S1-① (Source Attribution) → NEW SHOULD item S10
      → Source monitoring as independent dimension on 5-CP model
      → Confirmed by hallucination (mPFC) + PTSD (hippocampal)
      → No merge needed — concept did not exist in v1.0

    MODIFY: Phase C S2-③ (rumination paradox) → BROADENS existing S7
      → S7 was body-state specific: "signal impairs its own detector"
      → Now domain-general: body-state + thought-content
      → Rumination = thought → cortisol → PFC↓ → thought persists

    NOT ADDED (stays in drill files or PFC-Operations enrichment):
      → 3 failure modes of PFC suppress → PFC-Operations enrichment
      → Ironic process → PFC-Operations §2.3 extension
      → Exit mechanism taxonomy → drill-only
      → Predictive coding precision weighting → too detailed
      → Source monitoring continuum → too clinical


  AFTER DEDUPLICATION: 22 unique items (4 MUST + 10 SHOULD + 8 COULD)

    See §5 for full prioritized list.
```

---

## §5 — Prioritized v1.5 Changes (MUST / SHOULD / COULD)

```
════════════════════════════════════════════════════════════════════
MUST — INACCURATE WITHOUT (correct existing claims)
════════════════════════════════════════════════════════════════════

  M1. SCOPE STATEMENT: Framework = Level 2 (access consciousness)
      Source: Phase A (S1 hydranencephaly, S2 dreaming, S6 synthesis)
      Location: Consciousness.md §0
      Change: Add explicit scope = Level 2 "knowing."
              Acknowledge L0 (affective), L1 (phenomenal), L3 (meta) exist.
              Framework correctly addresses L2 — not a limitation but a choice.
      Why MUST: Without this, reader may assume framework claims to cover
                ALL consciousness, which it does not.
      Size: ~15-20 lines

  M2. RECURRENCE AS MECHANISM STEP BEFORE BROADCAST
      Source: Phase A (S4 blindsight, S5 gating)
      Location: Consciousness.md §5.1
      Change: Current = signal → ignition → broadcast → knowing.
              New = signal → recurrence through primary cortex (RPT, CP4) →
              IF sufficient → global broadcast (GWT, CP5) → knowing.
              RPT + GWT = COMPLEMENTARY, not competing.
      Why MUST: Without recurrence step, framework cannot explain blindsight
                (processing without awareness = recurrence failure).
      Size: ~15-20 lines modification to §5.1

  M3. PFC REFINEMENT: ENABLER, NOT SOURCE
      Source: Phase A (S2 dreaming, S4 blindsight, S5 gating), Phase B (S3 ADHD)
      Location: Consciousness.md §6
      Change: Distinguish dlPFC (executive, WM — OFF during dreaming) from
              vmPFC (emotion, self-reference — ON during dreaming).
              PFC = access/control ENABLER. Content = posterior cortex.
              PFC UPGRADES consciousness (L1→L2→L3), does not GENERATE it.
      Why MUST: Current §6 implies PFC = central to consciousness.
                Dreaming evidence shows consciousness exists without dlPFC.
      Size: ~15-20 lines modification + note in §6.1

  M4. 3-ROLE THALAMUS: REPLACE MONOLITHIC "BACKBONE"
      Source: Phase A (all 5 sessions convergent)
      Location: Consciousness.md §5.1 + §5.4
      Change: Replace generic "thalamus = backbone" with 3-role formulation:
              Role 1 — State Control (tonic/burst, CM-Pf) = "stage lit?"
              Role 2 — Content Gate (TRN, high-order nuclei) = "who enters?"
              Role 3 — Routing Hub (pulvinar, transthalamic) = "stage manager"
              Most processing unconscious because default = relay only (Role 3).
              Consciousness = when ALL 3 roles CONVERGE.
      Why MUST: "Backbone" is vague and misleading. 3-role formulation has
                converging evidence from 5 independent angles.
      Size: ~25-30 lines, may require subsection within §5


════════════════════════════════════════════════════════════════════
SHOULD — SIGNIFICANTLY BETTER WITH (additive enrichments, strong evidence)
════════════════════════════════════════════════════════════════════

  S1. 5-CHECKPOINT PATHWAY SUMMARY
      Source: Phase A (S5 gating, S6 mechanism)
      Location: Consciousness.md §5 (new subsection §5.6 or within §5.1)
      Change: Add concise summary of 5-checkpoint model:
              CP1 TRN gate → CP2 tonic mode → CP3 high-order nuclei →
              CP4 cortical recurrence → CP5 global broadcast.
              Every consciousness failure maps to checkpoint failure.
              Cross-ref: full model in Drill-Thalamo-Cortical-Mechanism.md
      Size: ~20-25 lines

  S2. SUSTAIN HIERARCHY + ADHD/DREAMING CONVERGENCE
      Source: Phase A ⑥ + Phase B S3-② (MERGED)
      Location: Consciousness.md §5 (new subsection after mechanisms)
      Change: Add sustain mechanism hierarchy:
              PRIMARY: ① thalamo-cortical resonance (works without PFC)
                       ② CM-Pf consciousness gate
              ADDITIONAL: ③ PFC WM hold (absent during dreaming)
                          ④ limbic/amygdala drive (enhanced during dreaming)
              + Convergence note: ADHD (PFC reduced → quality reduced) +
              dreaming (PFC absent → consciousness exists) = 2 independent
              conditions confirming 2-tier hierarchy from opposite directions.
      Size: ~25-30 lines

  S3. TONIC vs BURST AS CONSCIOUSNESS PREREQUISITE
      Source: Phase A ⑦
      Location: Consciousness.md §5.4 (extend Arousal vs Content)
      Change: Add explicit note that thalamic firing MODE determines
              whether consciousness is possible. Tonic = compatible,
              burst (NREM) = incompatible. Same anatomy, different mode.
              This is CP2 in the 5-checkpoint model.
      Size: ~10-15 lines

  S4. "KNOWING" INTERNAL vs EXTERNAL DIMENSION
      Source: Phase A ⑧
      Location: Consciousness.md §1.5 or §2 (extend existing)
      Change: Dreaming reveals "knowing" has 2 dimensions:
              Internal knowing = experiencing within the state
              External knowing = report, act, remember after
              v1.4 PARTIALLY addressed (disambiguation in §1.5).
              v1.5: add internal/external distinction explicitly.
      Size: ~10-15 lines

  S5. TEMPORAL DYNAMICS EXPLICIT IN §2.1
      Source: Phase B S1-① + S3-① (MERGED, convergent)
      Location: Consciousness.md §2.1 (extend 3-parameter description)
      Change: Add note that parameters have TEMPORAL PROFILES:
              f(signal(t) × anchor(t) × attention(t))
              Parameters adequate at t₀ may decay by t₁ (ADHD).
              Parameters modulated over hours (body state, cortisol).
              Entry → Resolution → Duration = temporal PHASES of same model.
              NOT a new parameter — temporal evolution of existing ones.
              Also note structural pattern: every candidate "4th parameter"
              tested (chunk density, prediction-delta, interoception, ADHD
              temporal profile) maps to existing parameters.
      Size: ~20-25 lines

  S6. POST-THRESHOLD RESOLUTION CONCEPT
      Source: Phase B S1-②
      Location: Consciousness.md §2.1 or near Feeling §2.2b cross-ref
      Change: Currently §2.2b says clarity → lower threshold (entry).
              Add: clarity → richer post-threshold content (resolution).
              Chunk density enriches what APPEARS on stage, not just WHETHER.
              Expert vs novice: same raw input, different chunk activation,
              different resolution. Not "better consciousness" — different
              content quality through same 3-parameter mechanism.
      Size: ~10-15 lines

  S7. SELF-REFERENTIAL PARADOX NOTE (BROADENED in v2.0)
      Source: Phase B S2-① + Phase C S2-③ (BROADENED)
      Location: Consciousness.md near §5.5 (impaired consciousness)
      Change: The self-referential paradox is DOMAIN-GENERAL, not body-specific:
              DOMAIN 1 — Body-state (Phase B S2):
                Cortisol → PFC ↓ → cannot receive cortisol accurately.
                The body signal impairs its own detector.
              DOMAIN 2 — Thought-content (Phase C S2):
                Negative thought → cortisol → PFC ↓ → cannot redirect thought.
                The thought impairs its own controller.
                Rumination = WORSE than body-state because thought IS on
                consciousness stage and is PORTABLE (cannot escape by
                changing environment).
              GENERAL PRINCIPLE: Any signal that triggers cortisol can
              impair the PFC mechanism that would normally control it.
              External stimuli do NOT have this property (stimulus removal
              = signal removal).
              Connects: Cortisol §9 + Consciousness §5.5② + Background §5⑦
              + Drill-Body-State §2.2 + Drill-Intrusive §4.
      Size: ~15-20 lines (was ~10-15)

  S8. STATE vs CAUSE CONSCIOUSNESS SPLIT
      Source: Phase B S2-②
      Location: Consciousness.md §2 (extend spectrum description)
      Change: "Knowing" has STATE level (what?) and CAUSE level (why?).
              STATE = Feel-Observation (high fidelity, ~85%).
              CAUSE = Feel-Explanation (low fidelity, 20-70%, PFC=Lawyer).
              "I know I'm angry" = STATE consciousness (relatively easy).
              "I know WHY I'm angry" = CAUSE consciousness (systematically hard).
              Connects to Feeling §2.3-§2.5 (7-layer fidelity gradient).
      Size: ~10-15 lines

  S9. 3 TYPES OF FORGETTING
      Source: Phase B S1-③
      Location: Consciousness.md §8 (new §8.4 or extend §8.3)
      Change: Forgetting is NOT one type — 3 distinct types:
              ① "Know you forgot" = meta-chunk persists, content decayed
              ② "Don't know you forgot" = no trace (default for most experience)
              ③ "Triggered recall" = dormant meta-chunk, cue activates
              Maps to existing framework: meta-chunks §8.3, anchor decay,
              cue-dependent recall (Tulving 1973).
      Size: ~15-20 lines

  S10. SOURCE ATTRIBUTION DIMENSION (NEW in v2.0)
      Source: Phase C S1-① (hallucination) + Phase C S2-④ (PTSD confirms)
      Location: Consciousness.md §5 (new subsection, after 5-checkpoint §5.6)
      Change: 5-CP model describes the PATHWAY to consciousness:
              signal passes all 5 checkpoints → content becomes conscious.
              Source monitoring describes WHETHER content is correctly
              ATTRIBUTED to its actual source (internal vs external).
              These are INDEPENDENT:
                All CPs pass + source monitoring INTACT = normal perception
                All CPs pass + source monitoring FAILS = hallucination
                All CPs pass + source monitoring INTACT but content FALSE =
                  Charles Bonnet (patient KNOWS it's not real)
              Source monitoring fails for DIFFERENT reasons:
                Hallucination: mPFC / corollary discharge failure
                PTSD: hippocampal context absent (S-rep without C-rep)
              = "Different Doors, Same Theater" — different mechanism,
              same result (incorrect source attribution on consciousness)
              Evidence: 🟢 Johnson, Hashtroudi & Lindsay 1993,
                        🟢 Brewin et al. 2010, 🟡 framework synthesis
      Why SHOULD not MUST: Framework is correct without it (5-CP works).
              Source attribution makes the model MORE COMPLETE for
              understanding clinical phenomena, but doesn't correct
              an existing inaccuracy. Adding it = enrichment, not correction.
      Size: ~15-20 lines


════════════════════════════════════════════════════════════════════
COULD — NICE TO HAVE (lower priority, smaller impact)
════════════════════════════════════════════════════════════════════

  C1. PATTERN LIFECYCLE DESCRIPTION
      Source: Phase B S1-⑤
      Location: Consciousness.md §5 or §8
      Change: Make implicit lifecycle explicit:
              Entry → Hold → Compete → Exit → (Encode or Forget).
              Individual mechanisms already covered; lifecycle framing is new.
      Size: ~10-15 lines

  C2. PREDICTION-DELTA AS MULTI-PARAMETER MODULATOR
      Source: Phase B S1-④
      Location: Consciousness.md §2.1 or §8.1
      Change: Explicit statement that prediction-delta modulates ALL 3
              parameters simultaneously (signal + attention + anchor).
              Already in §7.3, §8.2 but not framed as "multi-parameter."
      Size: ~5-10 lines

  C3. BIDIRECTIONAL LOOP NOTE
      Source: Phase B S2-③
      Location: Consciousness.md near §5.5 or §8
      Change: Body state modulates consciousness that observes body state.
              Creates virtuous/vicious cycles. Currently only in Cortisol §9.6.
      Size: ~5-10 lines

  C4. ATTENTION PARAMETER RICHNESS
      Source: Phase B S3-③
      Location: Consciousness.md §2.1 parameter ③
      Change: ADHD reveals attention has DISTRIBUTION (bimodal: 0% or ~100%)
              not just magnitude (0-100%). Threshold-gated, not linear.
      Size: ~5-10 lines

  C5. LIMBIC DRIVE AS FUNCTIONAL SUSTAIN SUBSTITUTE
      Source: Phase B S3-④
      Location: Within S2 (sustain hierarchy) if included
      Change: Limbic drive can COMPENSATE for PFC sustain deficit in ADHD.
              Not just "emotional coloring" — genuine alternative pathway.
      Size: ~5 lines within S2

  C6. CORE/MATRIX DEBATE NOTE
      Source: Phase A (Session 5)
      Location: Within thalamus description (M4)
      Change: Note Sherman & Usrey 2024 challenge to core/matrix classification.
              Use functional description (focal vs diffuse) not strict categories.
      Size: ~3-5 lines within M4

  C7. AFFECTIVE BLINDSIGHT CROSS-REFERENCE
      Source: Phase A (Session 4)
      Location: Cross-references §10
      Change: Note SC → pulvinar → amygdala pathway for unconscious emotion.
              Links to Level 0 (subcortical affective consciousness).
      Size: ~3-5 lines

  C8. BODY-STATE DEVELOPMENTAL TRAJECTORY
      Source: Phase B S2-④
      Location: Not in Consciousness.md — better as cross-ref to Feeling.md
      Change: Note that body-state consciousness develops through stages
              (Reflex → Proto → Labeled → Meta). Same 3-parameter model.
      Size: ~5 lines cross-reference
```

---

## §6 — File-by-File Change Specification

```
════════════════════════════════════════════════════════════════════
FILE 1: Consciousness.md v1.4 → v1.5
════════════════════════════════════════════════════════════════════

  SECTION-BY-SECTION CHANGES:

  §0 — POSITION IN FRAMEWORK:
    + M1: Scope statement (Level 2 explicit, L0/L1/L3 acknowledged)
    Modify existing §0 text. ~15-20 lines added.

  §1 — DEFINITION:
    §1.5:
      + S4: Internal vs external knowing dimension (extend existing)
      ~10-15 lines added to existing subsection.

  §2 — SPECTRUM:
    §2.1:
      + S5: Temporal dynamics note (parameters evolve over time)
      + S6: Post-threshold resolution concept (chunk density → richer content)
      + S5 also: structural pattern note (candidate parameters → modulators)
      ~30-40 lines added to existing subsection.
    §2.x (or within §2):
      + S8: State vs Cause consciousness split
      ~10-15 lines, brief note.

  §5 — MECHANISMS:
    §5.1:
      + M2: Recurrence before broadcast (RPT + GWT integration)
      + M4: 3-role thalamus (replace "backbone")
      ~40-50 lines modified/added (largest single change).
    §5.4:
      + S3: Tonic vs burst prerequisite (extend existing arousal content)
      ~10-15 lines added.
    §5.5 (near):
      + S7: Self-referential paradox note (BROADENED in v2.0:
        domain-general, not body-specific — includes thought-content)
      + C3: Bidirectional loop note (if included)
      ~15-25 lines added (was ~10-20, S7 expanded).
    §5.6 (NEW subsection):
      + S1: 5-checkpoint pathway summary
      ~20-25 lines, new subsection.
    §5.7 (NEW subsection):
      + S2: Sustain hierarchy (primary vs additional)
      + C5: Limbic drive as functional substitute (within S2)
      ~25-35 lines, new subsection.
    §5.8 (NEW subsection, added in v2.0):
      + S10: Source Attribution dimension
      Source monitoring = independent of consciousness pathway.
      All CPs pass + source monitoring fails = hallucination/PTSD.
      All CPs pass + source monitoring intact = normal/Charles Bonnet.
      Cross-ref: Drill-Hallucination §10.1①, Drill-Intrusive §10.1④
      ~15-20 lines, new subsection.

  §6 — PFC:
    §6.1:
      + M3: PFC refinement (dlPFC ≠ vmPFC, enabler not source)
      ~15-20 lines modified.

  §8 — BOUNDARY DYNAMICS:
    §8.4 (NEW subsection):
      + S9: 3 types of forgetting
      ~15-20 lines, new subsection.
    §8.x (if C1 included):
      + C1: Pattern lifecycle
      ~10-15 lines.

  §9 — HONEST ASSESSMENT:
    Update confidence/scope statements to reflect v1.5 additions.
    ~5-10 lines modified.

  §10 — CROSS-REFERENCES:
    + C7: Affective blindsight cross-ref
    + C8: Body-state developmental trajectory cross-ref
    + Update version references
    ~5-10 lines added.

  §11 — RESEARCH CITATIONS:
    Add new citations from drill sessions (COGITATE 2025, Fang 2025,
    Wang 2025, Voss 2014, Lamme 2003, etc.)
    ~15-20 lines added.

  HEADER:
    Version: 1.4 → 1.5
    Status: update description
    Dependencies: add drill file references
    ~10 lines modified.


  ⭐ SECTION NUMBER IMPACT:
    → §0-§8: NO renumbering. Changes are modifications or NEW subsections.
    → NEW subsections: §5.6, §5.7, §5.8 (v2.0), §8.4 — do NOT affect
      top-level numbering.
    → §9-§11: NO renumbering.
    → Cross-reference impact: MINIMAL (see §8 below).


════════════════════════════════════════════════════════════════════
FILE 2: Core-Software.md v3.4 → v3.5
════════════════════════════════════════════════════════════════════

  §8 — CONSCIOUSNESS (ENABLING STATE):
    Modify existing section to reflect:
    + M1: Scope = Level 2 reference
    + M4: 3-role thalamus summary
    + S2: Sustain hierarchy summary
    + M3: PFC = enabler note
    ~30-50 lines modified within existing §8.
    NO section renumbering — §8 stays §8.


════════════════════════════════════════════════════════════════════
FILE 3: Other Files (minimal impact)
════════════════════════════════════════════════════════════════════

  Feeling.md:
    No structural changes needed.
    S6 (post-threshold resolution) may add a note in §2.2b but could also
    be fully handled via cross-ref from Consciousness.md §2.1.

  01-File-Index.md:
    Update Consciousness.md version: v1.4 → v1.5
    Update Core-Software.md version: v3.4 → v3.5

  global-index.json:
    Update versions.
```

---

## §7 — Execution Plan: Phases & Dependencies

```
⭐ EXECUTION ORDER:

  ┌──────────────────────────────────────────────────────────────────┐
  │ PHASE 1: MUST changes to Consciousness.md                       │
  │   M1 (scope) → M2 (recurrence) → M4 (3-role thalamus)          │
  │   → M3 (PFC refinement)                                         │
  │   Order rationale: §0 first, then §5, then §6                   │
  │   Estimated: 1 focused session                                   │
  ├──────────────────────────────────────────────────────────────────┤
  │ PHASE 2A: SHOULD changes — Mechanisms cluster                    │
  │   S1 (5-checkpoint) → S2 (sustain hierarchy) → S3 (tonic/burst) │
  │   → S7 (self-referential, BROADENED) → S10 (source attribution) │
  │   All within §5. Top-down order within section.                  │
  │   v2.0: +S10 added, S7 expanded. ~15-20 lines more than v1.0.   │
  │   Estimated: 1 focused session                                   │
  ├──────────────────────────────────────────────────────────────────┤
  │ PHASE 2B: SHOULD changes — Model cluster                        │
  │   S5 (temporal dynamics) → S6 (resolution) → S8 (state/cause)  │
  │   → S4 (internal/external) → S9 (forgetting)                   │
  │   §2.1 first, then §1.5, then §8.                               │
  │   Estimated: 1 focused session                                   │
  ├──────────────────────────────────────────────────────────────────┤
  │ PHASE 3: Core-Software.md update                                 │
  │   DEPENDS ON: Phase 1 complete (needs final Consciousness.md     │
  │   section numbers and content to reference)                      │
  │   Can run DURING Phase 2 if Phase 1 is stable.                   │
  │   Estimated: within Phase 2 session                              │
  ├──────────────────────────────────────────────────────────────────┤
  │ PHASE 4: COULD changes (optional, if quality allows)             │
  │   C1-C8 in priority order. Can be deferred or omitted.           │
  │   Estimated: 1 session if included                               │
  ├──────────────────────────────────────────────────────────────────┤
  │ PHASE 5: Cross-references + verification                         │
  │   DEPENDS ON: ALL content changes complete.                      │
  │   Grep for stale references.                                     │
  │   Update index files.                                            │
  │   Read key sections to verify coherence.                         │
  │   Estimated: 30-60 min within final session                      │
  └──────────────────────────────────────────────────────────────────┘


  DEPENDENCIES:
    Phase 1 → Phase 2A, 2B (MUST before SHOULD)
    Phase 1 → Phase 3 (Consciousness.md before Core-Software.md)
    Phase 2A, 2B → Phase 5 (content before cross-refs)
    Phase 4 = independent (can be deferred)

  NATURAL SESSION BOUNDARIES:
    Session A: Phase 1 (MUST) + Phase 2A (mechanisms SHOULD)
    Session B: Phase 2B (model SHOULD) + Phase 3 (Core-Software)
    Session C: Phase 4 (COULD) + Phase 5 (verify)
    OR compressed:
    Session A: Phase 1 + 2A + 2B (all Consciousness.md)
    Session B: Phase 3 + 4 + 5 (Core-Software + COULD + verify)
```

---

## §8 — Cross-Reference Impact Assessment

```
⭐ CROSS-REFERENCE IMPACT = MINIMAL:

  WHY MINIMAL:
    → All changes = subsection additions or modifications
    → NO top-level section renumbering (§0-§11 unchanged)
    → NEW subsections (§5.6, §5.7, §5.8, §8.4) don't shift existing numbers
    → Existing subsection content modified in-place (§5.1, §5.4, §6.1)

  SPECIFIC CROSS-REF CHANGES NEEDED:

  ┌─────────────────────────┬──────────────────────┬─────────────────┐
  │ Change                  │ Old Reference         │ New Reference    │
  ├─────────────────────────┼──────────────────────┼─────────────────┤
  │ None identified         │ —                     │ —                │
  │ (all changes are within │                       │                  │
  │ existing sections or    │                       │                  │
  │ NEW subsections)        │                       │                  │
  └─────────────────────────┴──────────────────────┴─────────────────┘

  VERIFICATION GREP COMMANDS (run after all changes):
    1. "Consciousness.md §5.6" → should exist only in new content
    2. "Consciousness.md §5.7" → should exist only in new content
    3. "Consciousness.md §5.8" → should exist only in new content (v2.0)
    4. "Consciousness.md §8.4" → should exist only in new content
    5. "thalamus = backbone" → should be 0 matches after M4
    6. General: read §0, §5, §6 flow for coherence

  CONTRAST WITH v1.4:
    v1.4 renumbered §8.1→§1.5, §8.2-§8.4→§8.1-§8.3
    → Required ~4 cross-ref updates across 3 files
    v1.5 has NO renumbering → ZERO forced cross-ref changes

  Core-Software.md v3.4→v3.5:
    → §8 content modified in-place → NO section renumbering
    → Cross-refs to "Core-Software.md §8" remain valid
```

---

## §9 — Scope Estimation

```
⭐ ESTIMATED CHANGES (v2.0 updated):

  ┌────────────┬──────────────┬────────────────┬───────────────────┐
  │ Priority   │ Item Count   │ Lines Added    │ Sessions Needed   │
  ├────────────┼──────────────┼────────────────┼───────────────────┤
  │ MUST       │ 4            │ ~70-90         │ 1                 │
  │ SHOULD     │ 10 (was 9)   │ ~150-195       │ 1-2               │
  │ COULD      │ 8            │ ~50-80         │ 1 (optional)      │
  │ Core-SW    │ 1 file       │ ~30-50         │ within SHOULD     │
  │ Cross-refs │ ~0-5         │ ~5-10          │ within verify     │
  │ Verify     │ —            │ —              │ 30-60 min         │
  ├────────────┼──────────────┼────────────────┼───────────────────┤
  │ TOTAL      │ 22 items     │ ~305-425 lines │ 2-3 sessions      │
  └────────────┴──────────────┴────────────────┴───────────────────┘

  v2.0 CHANGES TO ESTIMATE:
    → S10 (Source Attribution): +15-20 lines
    → S7 (broadened): +5 lines over v1.0 estimate
    → Total SHOULD: was ~130-170, now ~150-195

  CONSCIOUSNESS.MD v1.5 SIZE:
    Current v1.4: ~1968 lines (verified)
    v1.5 additions: ~305-395 lines (net, after ~130 lines removed)
    v1.5 total: ~2143-2233 lines

  COMPARE:
    v1.3 → v1.4: restructuring (moved §8.1→§1.5, added disambiguation)
    v1.4 → v1.5: enrichment (adding substance, not restructuring)
    v1.5 = LARGER change in content, SMALLER change in structure
```

---

## §10 — Bias Checklist for Execution

```
⚠️ BIASES TO MONITOR DURING v1.5 EXECUTION:

  FROM PHASE A:
    □ Thalamus-centrism: 5 sessions of focus → risk overweighting
      Mitigation: cortex = GENERATOR, thalamus = INFRASTRUCTURE
    □ Post-hoc 5-checkpoint: formulated after evidence
      Mitigation: each CP has independent prior evidence + falsifiable
    □ "Levels" as evasion: counterexample → assign to "different level"
      Mitigation: levels make testable predictions (activity patterns)
    □ Key paper overreliance: Fang n=5, Pinto n=2, de Gelder n=1
      Mitigation: note limits, note convergent evidence

  FROM PHASE B:
    □ Confirmation bias: "framework handles everything" feels too good
      Mitigation: check if "already covered" = wishful thinking
    □ New-parameter avoidance: refusing new parameters to preserve model
      Mitigation: each candidate rigorously tested against criteria
    □ ADHD conflation: ADHD mechanism ≠ consciousness mechanism
      Mitigation: ADHD REVEALS architecture, doesn't DEFINE it
    □ Temporal model bias: forcing 4 stages when they overlap
      Mitigation: stages = description of dynamics, not rigid sequence

  FROM PHASE C (v2.0):
    □ Source Attribution overextension: elevating drill finding to framework
      Mitigation: S10 = SHOULD not MUST — enrichment, not correction
    □ Clinical claim creep: mapping OCD/PTSD → may imply clinical expertise
      Mitigation: drill = understanding mechanism, NOT treatment guide
    □ 3 failure modes as clean taxonomy: reality is continuous
      Mitigation: kept in drill/PFC-Ops only, NOT in Consciousness.md
    □ Self-referential paradox generalization: 2 domains ≠ universal
      Mitigation: S7 notes "any signal that triggers cortisol" — specific

  FROM CONVERGENCE:
    □ Convergence confirmation: treating convergence as proof
      Mitigation: convergence = consistent, not proven
    □ Selection bias: remembering convergent findings, forgetting divergent
      Mitigation: each drill file has honest assessment section
    □ Scope creep: adding too many enrichments → document overload
      Mitigation: MUST/SHOULD/COULD priority + size estimates
      v2.0 CHECK: only +1 SHOULD (S10) from entire Phase C =
      CONSERVATIVE, not scope creep
```

---

## §11 — Cross-References

```
SOURCE FILES (input to this synthesis):

  Phase A:
    → Drill-CE-Hydranencephaly.md v1.0
    → Drill-CE-Dreaming.md v1.0
    → Drill-CE-Split-Brain.md v1.0
    → Drill-CE-Blindsight.md v1.0
    → Drill-Thalamic-Gating.md v1.0
    → Drill-Thalamo-Cortical-Mechanism.md v2.0 (Phase A synthesis)
    → Drill-Consciousness-Counterexamples.md v2.0

  Phase B:
    → Drill-Consciousness-Quality-Model.md v1.0
    → Drill-Body-State-Consciousness.md v1.0
    → Drill-ADHD-Consciousness.md v1.0

  Phase C (v2.0):
    → Drill-Hallucination-Consciousness.md v1.0 (Phase C Session 1)
    → Drill-Intrusive-Consciousness.md v1.0 (Phase C Session 2)

  Current target files:
    → Consciousness.md v1.4
    → Core-Software.md v3.4

  Plans:
    → Plan-Counterexample-Deep-Drill.md (Phase A plan — ALL DONE)
    → Plan-Consciousness-Dynamics-Drill.md (Phase B plan — Sessions 1-4 DONE)
    → Plan-Consciousness-Control-Drill.md (Phase C plan — Sessions 1-3 DONE)

  NEXT:
    → Grand-Synthesis-Execution-Plan.md v1.0 SUPERSEDES this file's
      execution sections (§6-§7). It merges this file's 22 items with
      Terminology Analysis (4 findings) + Ontology Drill (1 finding)
      into 32 unified items with file-by-file execution plan.
    → Use Grand-Synthesis-Execution-Plan.md for execution.
    → This file's analysis sections (§0-§5, convergence map) remain
      valid as reference.
```
