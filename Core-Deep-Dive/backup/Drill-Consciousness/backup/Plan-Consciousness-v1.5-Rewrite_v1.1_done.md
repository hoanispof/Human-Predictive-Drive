---
title: "Plan — Consciousness v1.5 Rewrite"
version: 1.1
created: 2026-07-02
updated: 2026-07-02 (v1.1 — added E6: PFC-*.md full review session after rewrite)
status: ACTIVE — ready for execution
purpose: |
  Full REWRITE of Consciousness.md (v1.4.1 → v1.5) and
  Consciousness-Accessibility.md (v1.0 → v2.0).
  Careful REFINE of Core-Software.md (v3.4.1 → v3.5).
  Minor updates to PFC-Function.md and index files.
  
  Approach: Rewrite = write from scratch, integrating ALL drill findings naturally.
  File cũ → backup. File mới = definitive version.
  
  Sources:
    ① 12 drill files (Phase A: 7, Phase B: 3, Phase C: 2)
    ② Drill-Session-4-Synthesis.md v2.0 — 22 items (M1-M4, S1-S10, C1-C8)
    ③ Drill-Consciousness-Terminology-Analysis.md v2.1 — terminology constraints
    ④ Drill-Observation-Parameters-Ontology.md v1.0 — ontological reframe
    ⑤ Observer Fix v1.2 — 885 edits already applied (terminology clean)
    ⑥ Grand-Synthesis-Execution-Plan.md v1.0 — detailed change specification
  
  Supersedes:
    → Grand-Synthesis-Execution-Plan.md v1.0 (execution sections)
    → Plan-Foundation-Clarification.md (execution sections)
    → wise-crafting-wirth.md (DONE — Plan v1.4+v3.4)
    → Plan-Observer-Fix.md v1.2 (DONE)
dependencies:
  - "Observer Fix DONE (885 edits, terminology clean)"
  - "All 12 drill sessions DONE"
  - "Terminology Analysis DONE"
  - "Ontology Drill DONE"
  - "Grand Synthesis DONE (analysis valid, execution superseded by this plan)"
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Plan — Consciousness v1.5 Rewrite

> **12 drill sessions. 22 content items. 885 terminology fixes.**
> **All analysis DONE. All terminology CLEAN.**
>
> **Now: REWRITE for quality.**
> **Consciousness.md + Accessibility.md = from scratch.**
> **Core-Software.md = careful refine.**
>
> **Principle: "Chậm mà chắc. Quan trọng nhất là chất lượng nội dung."**

---

## Table of Contents

- [§0 — Scope & Approach](#0--scope--approach)
- [§1 — File Scope](#1--file-scope)
- [§2 — Consciousness.md v1.5 — Structure](#2--consciousnessmd-v15--structure)
- [§3 — Consciousness-Accessibility.md v2.0 — Structure](#3--consciousness-accessibilitymd-v20--structure)
- [§4 — Core-Software.md v3.5 — Refine Spec](#4--core-softwaremd-v35--refine-spec)
- [§5 — Other Files](#5--other-files)
- [§6 — Execution Sessions](#6--execution-sessions)
- [§7 — Quality Protocol](#7--quality-protocol)
- [§8 — Bias Checklist](#8--bias-checklist)
- [§9 — Source References](#9--source-references)

---

## §0 — Scope & Approach

```
⭐ APPROACH — 2 TYPES OF WORK:

  REWRITE (write from scratch):
    → Consciousness.md v1.4.1 → v1.5
    → Consciousness-Accessibility.md v1.0 → v2.0
    → File cũ move vào backup/
    → Write entirely new file, integrating ALL findings naturally
    → NOT patching 22 items into existing file
    → Advantage: coherent flow, no legacy artifacts

  REFINE (careful in-place edit):
    → Core-Software.md v3.4.1 → v3.5
    → PFC-Function.md v1.2 → v1.3
    → In-place changes, preserve working content
    → Only touch sections that need updating


⭐ WHAT HAS ALREADY BEEN DONE (do NOT redo):

  Observer Fix (885 edits, 148 files):
    → "observer" entity language → state language ✅
    → Obs params disambiguation blocks removed ✅
    → PFC "Observer" → "Orchestrator" (role name) ✅
    → PFC-Function.md §1 "OBSERVE" → "RECEIVE" ✅
    → Consciousness.md §1.5 thu gọn ✅

  These items from Grand-Synthesis-Execution-Plan.md are DONE:
    T1, T3, T4, T-CS1, T-CS2, PFC-Fn §1 rename


⭐ WHAT REMAINS (26 items):

  Content (22 items — the CORE of v1.5):
    4 MUST: M1 (scope), M2 (recurrence), M3+ (PFC Biased Hub), M4 (3-role thalamus)
    10 SHOULD: S1-S10
    8 COULD: C1-C8

  Terminology (4 items):
    T2 (definition hierarchy), T5 (header — optional), T6 (stage metaphor), O-CS1 (§9 meta)

  File-specific:
    PFC-note (consciousness-enabled note in PFC-Function.md)
    PFC label: "Biased Hub" in Core-Software.md §6 (CHỐT)


⭐ KEY DECISIONS (already made):

  ① PFC label = "Biased Hub" (chốt 2026-07-02)
  ② Consciousness.md = full rewrite
  ③ Consciousness-Accessibility.md = full rewrite
  ④ Core-Software.md = careful refine (NOT rewrite)
  ⑤ PFC-Label.md = NO changes needed (already correct)
  ⑥ 11 observation parameter files = NO changes needed
```

---

## §1 — File Scope

```
⭐ FILES TO CHANGE:

  ┌───────────────────────────────────┬──────────┬───────────────────┐
  │ File                              │ Approach │ Estimated Size    │
  ├───────────────────────────────────┼──────────┼───────────────────┤
  │ Consciousness.md v1.4.1 → v1.5   │ REWRITE  │ ~2200 lines       │
  │ Consciousness-Accessibility v2.0 │ REWRITE  │ ~700 lines        │
  │ Core-Software.md v3.4.1 → v3.5   │ REFINE   │ ~60 lines changed │
  │ PFC-Function.md v1.2 → v1.3      │ MINOR    │ ~15 lines added   │
  │ 01-File-Index.md                  │ UPDATE   │ ~5 lines          │
  │ global-index.json                 │ UPDATE   │ ~5 lines          │
  └───────────────────────────────────┴──────────┴───────────────────┘


⭐ BACKUP PLAN:

  Before rewrite:
    Consciousness.md v1.4.1 → backup/Consciousness_v1.4.1_backup.md
    Consciousness-Accessibility.md v1.0 → backup/Consciousness-Accessibility_v1.0_backup.md

  Old plans (already completed their purpose):
    wise-crafting-wirth.md → backup/ (Plan v1.4+v3.4, DONE)
    Plan-Observer-Fix.md → backup/ (v1.2, DONE)
    Grand-Synthesis-Execution-Plan.md → KEEP as reference (analysis §0-§2 still valid)
    Plan-Foundation-Clarification.md → KEEP as reference (tracking record)


⭐ FILES CONFIRMED NO CHANGES:

  PFC-Label.md v1.1 — 5 roles correct, no "Observer" ✅
  11 observation parameter files §0 — already correct per Ontology Drill ✅
  PFC-Operations.md — no changes in this scope ✅
  Other PFC files — no changes ✅
  ~50+ files with "PFC = observer" — gradual fix, NOT in scope ✅
```

---

## §2 — Consciousness.md v1.5 — Structure

```
⭐ REWRITE APPROACH:

  Read ALL sources → Write from scratch → Integrate naturally.
  
  Current v1.4.1 = good foundation but has:
    → Items patched incrementally across v1.0-v1.4.1
    → 22 content items NOT yet integrated
    → Some sections could flow better with fresh writing

  v1.5 = opportunity to write as ONE COHERENT DOCUMENT
  with ALL findings baked in from the start.


⭐ TARGET STRUCTURE — v1.5:

  HEADER + QUOTE
    → Version: 1.5
    → Clean quote: consciousness = knowing + GWT + stage metaphor (T6)
    → ~12 lines (T5)

  §0 — POSITION IN FRAMEWORK
    → M1: Scope = Level 2 access consciousness
      Acknowledge L0 (affective), L1 (phenomenal), L3 (meta)
      Framework correctly addresses L2 — scope choice, not limitation
    → Position: enabling state of chunk network
    → Companion files list
    → ~30 lines

  §1 — DEFINITION: CONSCIOUSNESS = "KNOWING"
    §1.1 Functional Definition
      → T2: "Knowing" = PRIMARY definition
      → "Enabling state" = architectural descriptor (secondary)
      → T6: Canonical stage metaphor (1 instance)
      → State language throughout (no "observer")
    §1.2 "Knowing" = f(signal × anchor × attention)
      → 3-parameter model introduction
    §1.3 "Knowing" vs "Broadcast"
      → Compatible, different level (WHAT vs HOW)
    §1.4 Consciousness ≠ Brain Region
      → Network state, not location
    §1.5 Meta-Level: Enabling State
      → 3 properties (already clean from Observer Fix)
      → S4: Internal vs external knowing dimension
        Dreaming: internal present, external absent
        Lucid dreaming: both present
      → Brief cross-ref to Core-Software.md §8

  §2 — SPECTRUM OF "KNOWING"
    §2.1 3-Parameter Model
      → Existing content (strong, preserve)
      → S5: Temporal dynamics explicit
        f(signal(t) × anchor(t) × attention(t))
        Parameters adequate at t₀ may decay by t₁ (ADHD)
        + Structural pattern: every candidate "4th parameter" 
        maps to existing parameters (modulator/envelope/domain)
      → S6: Post-threshold resolution
        Clarity → richer content (resolution), not just entry
        Expert vs novice: same input, different chunk activation
      → C2: Prediction-delta as multi-parameter modulator
      → C4: Attention parameter richness (ADHD bimodal)
    §2.2 Derived Landmarks (4 Levels)
    §2.3 Map → Feeling 7-Layer
      → S8: State vs Cause consciousness split
        STATE = Feel-Observation (high fidelity, ~85%)
        CAUSE = Feel-Explanation (low fidelity, 20-70%)
    §2.4 Map → Chunk Anchor Hierarchy
    §2.5 Map → Discovery Lifecycle

  §3 — 4 TYPES OF "NOT KNOWING"
    → Largely preserved (strong content, no items target here)

  §4 — ANCHOR = CONSCIOUSNESS ENABLEMENT
    → Largely preserved (strong content)

  §5 — MECHANISMS: HOW "KNOWING" WORKS ⚠️ LARGEST CHANGE AREA
    §5.1 Mechanism Overview (MAJOR modification)
      → M2: Recurrence before broadcast
        signal → recurrence (RPT, CP4) → IF sufficient →
        broadcast (GWT, CP5) → knowing
        RPT + GWT = COMPLEMENTARY, not competing
        Evidence: blindsight, TMS timing, COGITATE 2025
      → M4: 3-role thalamus (replace generic "backbone")
        Role 1 — STATE CONTROL: tonic/burst, CM-Pf
        Role 2 — CONTENT GATE: TRN, high-order nuclei
        Role 3 — ROUTING HUB: pulvinar, transthalamic
        Consciousness = when ALL 3 roles CONVERGE
        + C6: Core/matrix debate note (3-5 lines)
      → Existing thalamo-cortical loop + binocular rivalry (preserve)
    §5.2 Biased Competition (preserve)
    §5.3 2 Pathways: Push + Pull (preserve)
    §5.4 Arousal vs Content (extend)
      → S3: Tonic vs burst as consciousness prerequisite
        Tonic = compatible, burst (NREM) = incompatible
        = CP2 in 5-checkpoint model
    §5.5 Impaired Consciousness (extend)
      → S7: Self-referential paradox (DOMAIN-GENERAL)
        Domain 1 — Body: cortisol → PFC↓ → can't detect
        Domain 2 — Thought: negative thought → cortisol → PFC↓
        General: any signal triggering cortisol can impair PFC
      → C3: Bidirectional loop note
    §5.6 NEW — 5-CHECKPOINT PATHWAY
      → S1: CP1 TRN gate → CP2 tonic mode → CP3 high-order nuclei →
        CP4 cortical recurrence → CP5 global broadcast
      → Every consciousness failure maps to checkpoint failure
      → Cross-ref: Drill-Thalamo-Cortical-Mechanism.md v2.0
    §5.7 NEW — SUSTAIN HIERARCHY
      → S2: Primary vs additional sustain
        PRIMARY: ① thalamo-cortical resonance ② CM-Pf gate
        ADDITIONAL: ③ PFC WM hold ④ limbic/amygdala drive
      → ADHD/dreaming convergence evidence
      → C5: Limbic drive as functional substitute
    §5.8 NEW — SOURCE ATTRIBUTION
      → S10: Source monitoring as independent dimension on 5-CP
        All CPs pass + source intact = normal
        All CPs pass + source fails = hallucination
        All CPs pass + source intact but false = Charles Bonnet
        Different failure mechanisms: mPFC vs hippocampal
      → "Different Doors, Same Theater"
    §5.9 OPTIONAL — PATTERN LIFECYCLE
      → C1: Entry → Hold → Compete → Exit → (Encode or Forget)

  §6 — PFC = BIASED HUB ← label chốt
    §6.1 PFC Role: Biased Hub — Enabler, NOT Source
      → M3+: PFC = Biased Hub, receives + gates + biases + orchestrates
      → dlPFC (executive, OFF during dreaming) ≠ vmPFC (emotion, ON)
      → PFC UPGRADES consciousness (L1→L2→L3), does not GENERATE
      → Content generated in posterior cortex (Koch 2016)
      → Evidence: disable PFC → consciousness persists
    §6.2 Biased Hub Model (preserve core, update terminology)
    §6.3 Evidence Summary (preserve)

  §7 — COMPILED/FRESH × KNOWING/NOT-KNOWING
    → Largely preserved (strong content)

  §8 — BOUNDARY DYNAMICS
    §8.1 Threshold Dynamics (preserve)
    §8.2 Compilation Trajectory (preserve)
    §8.3 Meta-Chunks (preserve)
    §8.4 NEW — 3 Types of Forgetting
      → S9: ① "Know you forgot" = meta-chunk persists, content decayed
            ② "Don't know you forgot" = no trace (default)
            ③ "Triggered recall" = dormant meta-chunk, cue activates

  §9 — HONEST ASSESSMENT
    → Update for v1.5 additions
    → Note expanded mechanism detail (3-role, 5-CP, sustain)
    → Note terminology corrections (PFC Biased Hub)
    → Note Level 2 scope explicitly

  §10 — CROSS-REFERENCES
    → Update versions, add drill file refs
    → C7: Affective blindsight (SC→pulvinar→amygdala)
    → C8: Body-state developmental trajectory → Feeling.md
    → Obs params: brief note "See Core-Software.md §8 + §9"

  §11 — RESEARCH CITATIONS
    → All existing + new from drills:
      COGITATE 2025, Fang 2025, Wang 2025, Voss 2014,
      Lamme 2003, Wegner 1987/1994, Brewin et al. 2010,
      Johnson et al. 1993

  SECTION RENUMBERING: NONE
    → All changes within existing sections or NEW subsections (§5.6-§5.9, §8.4)
    → §0-§11 top-level numbering unchanged
    → Cross-reference impact: MINIMAL
```

---

## §3 — Consciousness-Accessibility.md v2.0 — Structure

```
⭐ REWRITE APPROACH:

  v1.0 has solid foundation (3-state model, 2×3 matrix, 2 transition modes).
  v2.0 = rewrite with SAME core model + NEW connections to v1.5 concepts.
  
  DEPENDS ON: Consciousness.md v1.5 complete (need final section numbers)


⭐ TARGET STRUCTURE — v2.0:

  §0 — POSITION IN FRAMEWORK
    → Updated to reference Consciousness.md v1.5
    → Clarify companion relationship

  §1 — 3 STATES OF AWARENESS
    §1.1 Definitions: Knowing, Accessible, Not-Accessible
    §1.2 Why "Not-Knowing" Needs Subdivision
    §1.3 Theoretical Support (Block, Karmiloff-Smith)

  §2 — MAPPING TO 4-TYPE TAXONOMY
    → Same core mapping
    → Updated cross-refs to v1.5

  §3 — EXTENDED MATRIX: 2×3 VIEW
    §3.1 The 2×3 Matrix
    §3.2 Analysis: What Each Cell Reveals

  §4 — TRANSITION MODES
    §4.1 Accessible → Knowing: VTA-Dependent (Top-Down Pull)
    §4.2 Accessible → Knowing: VTA-Independent (Bottom-Up/Cue)
    §4.3 Not-Accessible → Accessible: Creating Accessibility
    §4.4 Evidence: Depletion Confirms 2 Modes

  §5 — CONNECTIONS TO FRAMEWORK (EXPANDED in v2.0)
    §5.1 × Compilation Pathways (preserve)
    §5.2 × Meta-Chunks (preserve)
    §5.3 × Self-Observation Training (preserve)
    §5.4 NEW × 5-Checkpoint Pathway
      → How does each CP relate to accessibility?
      → CP failure at different stages → different accessibility outcomes
    §5.5 NEW × Sustain Hierarchy
      → Primary sustain intact, additional impaired (ADHD)
        → Accessibility EXISTS but transition speed/quality reduced
      → Primary sustain lost (anesthesia)
        → ALL accessibility suspended
    §5.6 NEW × Forgetting Types
      → S9's 3 types map to accessibility states:
        "Know you forgot" = Accessible (meta-chunk = retrieval path exists)
        "Don't know you forgot" = Not-Accessible (no trace)
        "Triggered recall" = conditionally Accessible (dormant path, cue activates)
      → = Forgetting taxonomy IS accessibility taxonomy (same structure)
    §5.7 NEW × Source Attribution
      → Hallucination: signal is Accessible + Knowing, but source is WRONG
      → = Accessibility model needs "source accuracy" alongside "can it reach stage"

  §6 — HONEST ASSESSMENT
    → Updated for v2.0 additions
    → Note new connections as 🟡 framework synthesis

  §7 — CROSS-REFERENCES
    → Updated versions

  §8 — RESEARCH CITATIONS
    → Existing + any new relevant
```

---

## §4 — Core-Software.md v3.5 — Refine Spec

```
⭐ REFINE APPROACH — 4 sections, careful in-place edits:

  DEPENDS ON: Consciousness.md v1.5 complete (§8 references v1.5 content)


  ┌─────────────────────────────────────────────────────────────┐
  │ §0.3 — DESIGN PRINCIPLES                                    │
  ├─────────────────────────────────────────────────────────────┤
  │ Check: principle #8 "Consciousness = enabling state"         │
  │ already exists? If yes → verify wording matches v1.5.       │
  │ If no → add.                                                │
  │ Size: ~2-3 lines                                            │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │ §6 — PFC (Biased Hub) ← LABEL CHANGE                       │
  ├─────────────────────────────────────────────────────────────┤
  │ Current: "PFC (Orchestrator)"                                │
  │ Change to: "PFC (Biased Hub)"                                │
  │ Keep "Orchestrator" as role description WITHIN section       │
  │ Fix §6.1 label if needed                                    │
  │ Verify consistency with Consciousness.md v1.5 §6             │
  │ Size: ~10-15 lines modified                                 │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │ §8 — CONSCIOUSNESS (ENABLING STATE)                          │
  ├─────────────────────────────────────────────────────────────┤
  │ §8.0: Update to match v1.5 definition hierarchy             │
  │   → "Knowing" = primary, "enabling state" = architectural   │
  │   → Add M1 scope reference (Level 2 = "knowing")           │
  │ §8.1: Update content to reflect v1.5 enrichments            │
  │   → Brief refs to 3-role thalamus, sustain hierarchy        │
  │   → PFC = Biased Hub (enabler) note                         │
  │ ⚠️ §8.2 was REMOVED by Observer Fix — do NOT recreate      │
  │ Size: ~20-25 lines modified                                 │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │ §9 — OBSERVATION PARAMETERS (meta-description)               │
  ├─────────────────────────────────────────────────────────────┤
  │ O-CS1: Replace meta-description                              │
  │                                                              │
  │ CURRENT:                                                     │
  │   "Not architectural components. They are named patterns     │
  │    observed from the cycle. Value: helps describe, predict,  │
  │    communicate. Not mechanism."                              │
  │                                                              │
  │ NEW (from Ontology Drill):                                   │
  │   "Observation parameter = a recurring pattern identified    │
  │    through observation methodology.                          │
  │                                                              │
  │    This framework's observation parameters are the specific  │
  │    patterns emerging from human Compilable Architecture      │
  │    chunk dynamics.                                           │
  │                                                              │
  │    Each maps to identifiable neural substrates               │
  │    (VTA, amygdala, serotonin...) but is NOT a separate       │
  │    module — the mapping is many:many.                        │
  │                                                              │
  │    Like 'temperature' in physics: no neuron IS 'novelty,'   │
  │    but the pattern is real, measurable, and causal.          │
  │                                                              │
  │    The name is convention; the pattern is real.              │
  │    Intervention: target the MECHANISMS that produce the      │
  │    pattern, not the pattern itself."                         │
  │                                                              │
  │ Size: ~14 lines replaced                                     │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │ VERSION + INDEX                                              │
  ├─────────────────────────────────────────────────────────────┤
  │ Version: v3.4.1 → v3.5                                     │
  │ Changelog: add v3.5 entry                                   │
  │ Size: ~5 lines                                              │
  └─────────────────────────────────────────────────────────────┘
```

---

## §5 — Other Files

```
⭐ PFC-FUNCTION.MD v1.2 → v1.3:

  §1 "OBSERVE" → "RECEIVE": ALREADY DONE ✅
  
  ADD consciousness-enabled note (~10 lines, near §0 or §6):
    "These 24 functions require consciousness as enabling state.
     PFC provides the hardware substrate; consciousness provides
     the state that makes processing self-accessible.
     Functions emerge from the combination, not PFC alone.
     Without consciousness (anesthesia): PFC intact, 0/24 available.
     Without PFC (damage): consciousness exists, but loses
     gating + strategic capacity.
     Cross-ref: Consciousness.md v1.5 §6."
  
  Version bump: v1.2 → v1.3


⭐ INDEX FILES:

  01-File-Index.md:
    → Consciousness.md: v1.4.1 → v1.5
    → Consciousness-Accessibility.md: v1.0 → v2.0
    → Core-Software.md: v3.4.1 → v3.5
    → PFC-Function.md: v1.2 → v1.3

  global-index.json:
    → Same version updates


⭐ CONFIRMED NO CHANGES:

  PFC-Label.md v1.1 — 5 roles correct ✅
  PFC-Operations.md — no scope ✅
  11 observation parameter files — already correct ✅
```

---

## §6 — Execution Sessions

```
⭐ SESSION PLAN — 5 PHASES:


═══════════════════════════════════════════════════════════════
E1: CONSCIOUSNESS.MD v1.5 — REWRITE
═══════════════════════════════════════════════════════════════

  ⚠️ LARGEST PHASE. Split into sub-sessions for quality.

  E1-PREP: Backup + Structure Planning
    → Backup v1.4.1 → backup/
    → Read key drill sources (Synthesis v2.0, Thalamo-Cortical v2.0,
      Terminology v2.1) for content details
    → Finalize exact section outline
    → ~30 min

  E1a: Write §0-§2 (Definition + Spectrum)
    Items: M1, S4, S5, S6, S8, C2, C4, T2, T6
    → §0: Position + scope statement (M1)
    → §1: Definition + enabling state + internal/external knowing (S4)
    → §2: Spectrum + temporal (S5) + resolution (S6) + state/cause (S8)
    → Estimated: ~600-700 lines
    → 1 focused session

  E1b: Write §3-§5 (Taxonomy + Anchor + Mechanisms)
    Items: M2, M4, S1, S2, S3, S7, S10, C1, C3, C5, C6
    → §3-§4: Largely preserve content (strong, no major items)
    → §5: MAJOR rewrite — recurrence (M2), 3-role thalamus (M4),
      5-CP (S1), sustain (S2), tonic/burst (S3), paradox (S7),
      source attribution (S10), lifecycle (C1)
    → Estimated: ~700-900 lines
    → ⚠️ 1-2 focused sessions (§5 alone is ~400-500 lines)

  E1c: Write §6-§11 (PFC + Matrix + Boundary + Assessment)
    Items: M3+, S9, C7, C8, citations
    → §6: PFC Biased Hub (M3+) — enabler, dlPFC/vmPFC
    → §7: Matrix (preserve)
    → §8: Boundary + forgetting (S9)
    → §9-§11: Assessment, cross-refs, citations
    → Estimated: ~600-700 lines
    → 1 focused session

  TOTAL E1: ~2100-2300 lines, 3-4 focused sessions


═══════════════════════════════════════════════════════════════
E2: CONSCIOUSNESS-ACCESSIBILITY.MD v2.0 — REWRITE
═══════════════════════════════════════════════════════════════

  DEPENDS ON: E1 complete (need v1.5 section numbers)

  → Backup v1.0 → backup/
  → Rewrite with same 3-state model + new v1.5 connections
  → New §5.4-§5.7 (5-CP, sustain, forgetting, source attribution)
  → Estimated: ~700-800 lines
  → 1 focused session


═══════════════════════════════════════════════════════════════
E3: CORE-SOFTWARE.MD v3.5 — REFINE
═══════════════════════════════════════════════════════════════

  DEPENDS ON: E1 complete (need v1.5 content to reference)

  → §0.3: Design principle check/add
  → §6: PFC label "Orchestrator" → "Biased Hub"
  → §8: Update to match v1.5
  → §9: Replace meta-description (ontology)
  → Version bump
  → Estimated: ~60 lines changed
  → Within 1 session (can combine with E2 or E4)


═══════════════════════════════════════════════════════════════
E4: PFC-FUNCTION.MD + INDEX FILES — MINOR
═══════════════════════════════════════════════════════════════

  → PFC-Function.md: consciousness-enabled note + version bump
  → 01-File-Index.md: version updates
  → global-index.json: version updates
  → Estimated: ~25 lines total
  → Within E3 session


═══════════════════════════════════════════════════════════════
E5: CROSS-REFS + VERIFY
═══════════════════════════════════════════════════════════════

  → Grep verification (see §7)
  → Coherence read (key sections)
  → Cross-ref consistency check
  → Estimated: 30-60 min within final session


═══════════════════════════════════════════════════════════════
E6: PFC-*.MD REVIEW (added 2026-07-02)
═══════════════════════════════════════════════════════════════

  DEPENDS ON: E1-E5 complete (Consciousness rewrite finalized)

  PURPOSE: Rà soát toàn bộ PFC-*.md sau khi Consciousness v1.5
  hoàn thành, đảm bảo thông tin chính xác và nhất quán.

  SCOPE:
    → PFC-Function.md: verify 24 functions consistent with v1.5
      (PFC = Biased Hub framing, enabling state relationship)
    → PFC-Operations.md: verify Hold/Suppress/Budget consistent
    → PFC-Label.md: verify 5 roles still accurate post-v1.5
    → PFC-Configuration.md: verify 6 modes consistent
    → PFC-Hardware.md, PFC-Development.md, PFC-Hold-Dimensions.md:
      spot-check for stale refs or outdated framing

  KEY POINTS TO VERIFY (from session discussion 2026-07-02):
    ① PFC = Biased Hub (not just Orchestrator) — Orchestrator = 1/5
      categories, not PFC's defining characteristic
    ② PFC functions ≠ Consciousness functions — 2 different meta-levels
      (PFC = brain region with actions, Consciousness = enabling state)
    ③ PFC functions require consciousness as enabling state BUT also
      operate on unconscious content (~95%)
    ④ PFC is primary contributor to these functions, not sole owner
      (sub-regions involve ACC, TRN, thalamus, etc.)
    ⑤ File naming "PFC-*" is correct — functions mapped to PFC
      sub-regions via lesion/fMRI evidence

  APPROACH: Read each file → check consistency with Consciousness.md
  v1.5 and Core-Software.md v3.5 → fix if needed → version bump

  Estimated: 1 focused session
  Principle: "Chậm mà chắc" — verify AFTER rewrite, not during

  STATUS: ✅ DONE (2026-07-02)
    5 verification points: ALL PASS
    ① Biased Hub: PFC-Function.md ✅, PFC-Label.md ✅ (added Biased Hub note)
    ② 2 meta-levels: ✅ all files consistent
    ③ Enabling state: ✅ all files consistent
    ④ Primary not sole: ✅ many-to-many mapping correct
    ⑤ File naming: ✅ correct
    Stale refs fixed: PFC-Function v1.2→v1.3 (4 files),
      Consciousness v1.0→v1.5 (2 files), PFC-Configuration v1.0→v1.1 (1 file),
      PFC-Function footer v1.2→v1.3
    PFC-Label.md: added "Biased Hub" primary label note in §2
    Files outside 7 PFC core (Logic-Feeling, Imagination, Self-Observation):
      NOT in scope — will update when those files version bump


═══════════════════════════════════════════════════════════════
DEPENDENCY MAP:
═══════════════════════════════════════════════════════════════

    E1a → E1b → E1c → E2 ─→ E5 → E6
    (§0-§2)  (§3-§5)  (§6-§11)  (Accessibility)  (verify)  (PFC review)
                                    ↓
                              E3 → E4
                            (Core-SW) (PFC+index)

    E1 phải hoàn thành trước E2, E3 (source of truth)
    E2 và E3 có thể song song (independent files)
    E4 sau E3 (PFC refs Core-Software.md)
    E5 sau E1-E4 (verify all)
    E6 sau E5 (PFC review — last, after everything settled)


═══════════════════════════════════════════════════════════════
SESSION BOUNDARIES (natural pause points):
═══════════════════════════════════════════════════════════════

    SESSION A: E1-PREP + E1a (backup + §0-§2)
    SESSION B: E1b (§3-§5 — may need 2 sessions for §5)
    SESSION C: E1c (§6-§11)
    SESSION D: E2 + E3 + E4 (Accessibility + Core-SW + PFC + index)
    SESSION E: E5 (verify)
    SESSION F: E6 (PFC-*.md full review)

    MINIMUM: 5 sessions (A + B + C + D/E combined + F)
    RECOMMENDED: 6 sessions (§5 gets its own session)
    MAXIMUM: 7 sessions (E2 and E3 separate)
```

---

## §7 — Quality Protocol

```
⭐ DURING EACH REWRITE SESSION:

  BEFORE writing:
    □ Re-read relevant source items (M/S/C items for that section)
    □ Check current v1.4.1 content for what to PRESERVE vs REWRITE
    □ Note confidence level for each claim (🟢/🟡/🔴)

  DURING writing:
    □ State language (no "observer" entity) — already clean from Observer Fix
    □ 3-tier confidence on ALL claims
    □ Full concept names (no abbreviation)
    □ Cross-refs use specific section numbers
    □ Each section: WHAT → WHY → HOW → EVIDENCE → LIMITATION

  AFTER each section:
    □ Read back for flow and coherence
    □ Check: all claimed evidence has citation
    □ Check: no scope creep (only items in plan)


⭐ GREP VERIFICATION (E5):

  1. "observer" in Consciousness.md v1.5
     → Expected: 0 non-phenomenal uses
  2. "observer" in Core-Software.md §6 + §8
     → Expected: 0 (only §6.7 Self-Observation = KEEP)
  3. "backbone" in Consciousness.md §5
     → Expected: 0 (replaced by 3-role thalamus)
  4. "just names" OR "just labels" in Core-Software.md §9
     → Expected: 0 (replaced by ontology meta)
  5. Section number consistency
     → §5.6, §5.7, §5.8 exist only in new content
  6. Cross-ref versions match actual versions


⭐ COHERENCE READ (E5):

  □ §0 → §1.1 → §1.5: scope clear? definition hierarchy clear?
  □ §5.1 → §5.6 → §5.7 → §5.8: mechanisms flow naturally?
  □ §6: PFC description matches Core-Software.md §6?
  □ Consciousness-Accessibility.md: references match v1.5 sections?
  □ Core-Software.md §8: consistent with Consciousness.md v1.5?
```

---

## §8 — Bias Checklist

```
⚠️ BIASES TO MONITOR (inherited from Synthesis v2.0 + Terminology v2.1):

  CONTENT BIASES:
    □ Thalamus-centrism: 5 sessions of focus → risk overweighting
      Mitigation: cortex = GENERATOR, thalamus = INFRASTRUCTURE
    □ Post-hoc 5-checkpoint: formulated after evidence
      Mitigation: each CP has independent prior evidence + falsifiable
    □ Confirmation bias: "framework handles everything"
      Mitigation: check if "already covered" = wishful thinking
    □ Source Attribution overextension: elevating drill finding to framework
      Mitigation: S10 = SHOULD not MUST — enrichment, not correction
    □ Convergence confirmation: treating convergence as proof
      Mitigation: convergence = consistent, not proven

  REWRITE BIASES:
    □ Over-engineering: rewrite tempts adding more than planned
      Mitigation: ONLY items in this plan. COULD items = add if natural,
      skip if forced
    □ Loss aversion: keeping v1.4.1 text verbatim "because it was there"
      Mitigation: preserve CONTENT, not exact wording. Rewrite means rewrite.
    □ Scope creep: "already rewriting, might as well add X"
      Mitigation: 22 items is already comprehensive. Quality > quantity.
    □ PFC label cascade: fixing "Biased Hub" → wanting to fix 50+ files
      Mitigation: Core-Software.md §6 + Consciousness.md §6 ONLY

  TERMINOLOGY BIASES:
    □ Over-correction: removing "observer" too aggressively
      Mitigation: phenomenal usage OK. Only remove from definitions/mechanism.
    □ Overselling "emergent": philosophically loaded
      Mitigation: descriptive use only (arises from interaction, not reducible)
```

---

## §9 — Source References

```
⭐ DRILL FILES (evidence base — READ during rewrite):

  Phase A (Counterexample):
    → Drill-CE-Hydranencephaly.md — L0, subcortical consciousness
    → Drill-CE-Dreaming.md — PFC = enabler not source
    → Drill-CE-Split-Brain.md — state vs content broadcast
    → Drill-CE-Blindsight.md — recurrence necessary (M2)
    → Drill-Thalamic-Gating.md — 3-role thalamus, 5-CP (M4, S1)
    → Drill-Thalamo-Cortical-Mechanism.md v2.0 — synthesis
    → Drill-Consciousness-Counterexamples.md v2.0 — evidence index

  Phase B (Dynamics):
    → Drill-Consciousness-Quality-Model.md — temporal (S5), resolution (S6)
    → Drill-Body-State-Consciousness.md — paradox (S7), state/cause (S8)
    → Drill-ADHD-Consciousness.md — sustain (S2), temporal (S5)

  Phase C (Control):
    → Drill-Hallucination-Consciousness.md — source attribution (S10)
    → Drill-Intrusive-Consciousness.md — paradox broadened (S7), PTSD

  Analysis:
    → Drill-Session-4-Synthesis.md v2.0 — 22 items, 11 convergence themes
    → Drill-Consciousness-Terminology-Analysis.md v2.1 — 4 findings
    → Drill-Observation-Parameters-Ontology.md v1.0 — ontological model

  Plans (reference, superseded for execution):
    → Grand-Synthesis-Execution-Plan.md v1.0 — change specification detail
    → Plan-Foundation-Clarification.md v1.0 — tracking record
```

---

## TRACKING

```
E1-PREP: Backup + structure planning          DONE (2026-07-02)
E1a: Consciousness.md §0-§2                   DONE (2026-07-02, 665 lines)
E1b: Consciousness.md §3-§5                   DONE (2026-07-02, 1671 lines total, 11 items integrated)
E1c: Consciousness.md §6-§11                  DONE (2026-07-02, 2681 lines total, items: M3+, S9, C7, C8)
E2: Consciousness-Accessibility.md v2.0       DONE (2026-07-02, 954 lines, 85 confidence tags, 4 NEW §5.4-§5.7)
E3: Core-Software.md v3.5                     DONE (2026-07-02, PFC→Biased Hub, §8 v1.5, §9 ontology)
E4: PFC-Function.md + index files             DONE (2026-07-02, v1.3 consciousness note + 01-File-Index + global-index)
E5: Cross-refs + verify                       DONE (2026-07-02, grep clean, stale refs fixed, coherence 4/4 PASS, Plan-Observer-Fix→backup)
E6: PFC-*.md full review                      TODO (added 2026-07-02)
```

---

> **Plan-Consciousness-v1.5-Rewrite.md v1.1**
> **Rewrite Consciousness.md + Accessibility from scratch.**
> **Refine Core-Software.md carefully.**
> **Then: full PFC-*.md review for consistency.**
> **5-7 sessions. "Chậm mà chắc."**
