---
title: Sound × Brain Drill — Overview + Reading Guide
version: 1.5
created: 2026-05-29
updated: 2026-05-29 (v1.5 — Verification Round 2: Selfhout citation fixed, I4 Alzheimer nuance, I24 updated, exposure numbers corrected.)
status: OVERVIEW v1.5
scope: |
  Entry point for the Drill-Sound-Brain folder.
  Reading guide, 44-insight index, folder structure, dependencies,
  testable predictions, open questions, cross-references.
  v1.1: +06 Architecture, +07 Entrainment, +02/03 refinements.
  v1.2: +08 Voice/Melody/Shape, +06 §3c Integer Ratio, +07 §7b Attention Paradox.
  v1.3: +09 Verification Research (10 insights verified, 18 corrections, 30+ new citations).
  v1.4: ALL 18 corrections APPLIED to 7 drill files. Insight tags updated. All files → v1.1.
  v1.5: Verification Round 2 — Selfhout citation fixed (J Adolescence), I4 Alzheimer mechanism
        nuanced (Jacobsen=anatomical sparing), exposure numbers corrected in 02,
        window sizes tagged as estimates in 03.
purpose: |
  Comprehensive drill on Sound × Brain × Framework.
  MAP neuroscience evidence (~150+ citations) onto framework mechanisms.
  VALIDATE existing mechanisms — does NOT add new mechanisms.
  IDENTIFY testable predictions + literature gaps.
  EXTEND framework into multi-modal compound territory.
  v1.1: +Music architecture WHY + Neural entrainment + Reward dynamics.
position: |
  Research/Drill-Sound-Brain/ — entry point.
  Read this file BEFORE all other files in this folder.
language: English
---

# Sound × Brain Drill — Overview + Reading Guide

> **Music = one of the richest human experiences.**
> **Auditory = the ONLY modality that compiles chunks BEFORE BIRTH.**
> **Music neuroscience = a mature field, 120+ curated citations.**
>
> **This drill:**
> **① COMPILES neuroscience evidence systematically**
> **② MAPS evidence onto EXISTING framework mechanisms**
> **③ VALIDATES: 5 landmark papers directly confirm framework predictions**
> **④ PREDICTS: 5 testable new predictions, 1 never yet tested**
> **⑤ EXTENDS: multi-modal compound territory (games, film, VR)**
>
> **Does NOT add new mechanisms.**
> **Confirms existing ones through the music domain.**

---

## §1 — Folder Structure

```
Research/Drill-Sound-Brain/
│
├── 00-Overview.md                  ← THIS FILE (entry point)
├── plan-Drill-Sound-Brain.md       ← Implementation plan
│
├── EVIDENCE:
│   └── 01-Sound-Brain-Neuroscience.md  (~730L)
│         10 research axes, 120+ citations, confidence-tagged
│
├── MECHANISM:
│   ├── 02-Sound-Background-Pattern.md  (~480L)
│   │     HOW music → Background-Pattern (8 insights)
│   │     v1.1: +§7b Gap-Direction × music ("no knowledge = no gap")
│   └── 03-Sound-Reward-Pipeline.md     (~410L)
│         7-step validation + musical anhedonia (4 insights)
│         v1.1: +§7b Reward-Calibration × music (3 zones + window)
│
├── ANALYSIS:
│   ├── 04-Sound-Social-Resonance.md    (~560L)
│   │     Music taste × resonance × convergence (14 insights)
│   │     5-step mechanism chain. 5 testable predictions.
│   └── 05-Multi-Modal-Compound.md      (~470L)
│         Audio+Visual+Action hierarchy (6 insights)
│
├── FOUNDATION + DYNAMICS (v1.1-1.2):
│   ├── 06-Music-Architecture-Prediction.md  (~630L)
│   │     WHY music is structured the way it is. Hard numbers.
│   │     Tonic, BPM, 4/4, verse-chorus, repetition, cross-cultural.
│   │     Each feature = prediction architecture constraint.
│   │     v1.2: +§3c Integer Ratio Principle (1 principle, 3 domains)
│   └── 07-Music-Entrainment-Reward-Dynamics.md  (~770L)
│         Neural sync (distributed oscillators + hub).
│         Continuous micro-rewards vs discrete macro-rewards.
│         Gap-Direction trajectory (inverted-U).
│         Music × Compiled vs Fresh tasks. Transfer effects.
│         v1.2: +§7b Attention Paradox (analysis can interfere with pleasure)
│
├── ELEMENTS + INTERFACE (v1.2):
│   └── 08-Musical-Elements-Brain-Interface.md  (~430L)
│         Voice 3-Channel (Semantic/Prosody/Voice-as-instrument).
│         Melody = multi-system activator (~5-6 systems from 1 line).
│         Shape vs Content: music = prediction template, brain = content fill.
│         Activation efficiency as unifying metric.
│
└── VERIFICATION (v1.3):
│   └── 09-Verification-Research.md  (~970L)
│         3 rounds verification. 30 corrections, 35+ new citations.
│         R1: 10 insights, 18 corrections. R2: 3 insights, 9 corrections.
│         R3: ~10 landmarks spot-checked, 3 corrections.
│         Key: "analysis kills pleasure" OVERSTATED. Selfhout citation FIXED.
│
└── SYNTHESIS (v1.5):
    └── 10-Synthesis.md  (~640L)
          Complete synthesis. 6 validations, 10 extensions, evidence quality map.
          49% confirmed, 43% synthesis, 7% untested, 0% wrong.
          Methodological lessons. Impact assessment. Limitations.

Total: 12 files, ~6,600L
```

---

## §2 — Reading Flow

```
RECOMMENDED:

  01 → 06 → 02 → 03 → 07 → 08 → 04 → 05 → 09

  01 Evidence base         — READ FIRST (foundation for everything)
  06 Architecture          — WHY music is structured the way it is (hard numbers)
  02 Background-Pattern    — HOW music → chunks → Background-Pattern
  03 Reward Pipeline       — HOW the brain rewards music (7-step validation)
  07 Entrainment+Dynamics  — Neural sync + reward flow + gap trajectory
  08 Elements+Interface    — Voice 3-channel, melody efficiency, shape vs content
  04 Social Resonance      — ★ LARGEST + MOST NOVEL (taste × resonance)
  05 Multi-Modal           — Audio+Visual+Action compound
  09 Verification          — Quality control: 10 insights checked, corrections listed

QUICK REFERENCE:
  "Music × Brain fundamentals?"                              → 01
  "Why is music structured the way it is?"                  → 06
  "What are the lasting effects of music?"                  → 02
  "Why does music feel pleasurable?"                        → 03
  "BPM, neural sync, flow?"                                → 07
  "Why does music only get better with repeated listening?" → 07 §5 + 02 §7b
  "Music while working?"                                    → 07 §7
  "Does analyzing music kill the pleasure?"                 → 07 §7b
  "Why does foreign-language music still move you?"         → 08 §1
  "What makes melody special?"                             → 08 §2
  "Does shared taste make connection easier?"               → 04
  "Music in games/films?"                                  → 05
  "Full synthesis of the drill?"                           → 10
  "What does the framework validate?"                      → 10 §2
  "How reliable is the drill?"                             → 10 §4-§5
```

---

## §3 — 44 Insights Index

```
═══ 02-Sound-Background-Pattern (Insights 1-8) ═══

  1. Music chunks = inherently multi-modal (auditory+motor+emotional minimum)
     → chunk depth naturally DEEPER than verbal-only                        🟡

  2. Genre = sustained context consistency → ideal for link density growth
     → each genre = years × daily × consistent acoustic context             🟡

  3. Gist extraction → abstract aesthetic pattern = taste signature = PFC label
     → taste signature = PFC label for music Background-Pattern             🟡

  4. Music Background-Pattern = Low compile-Depth + HIGH Density
     → Alzheimer: Jacobsen 2015 = anatomical sparing (regions less affected)
     → Framework "distributed → resistant" = plausible addition, not Jacobsen's finding 🟢/🟡

  5. 3 satiation types apply: Cyclic (single track) / Tonic (background) / Generative (exploration)
     → per-listener profile depends on individual ratio of the 3 types      🟡

  6. Tonic listeners (always have background music) = STRONGEST Background-Pattern
     → continuous firing → PFC-invisible → link density extremely high      🟡

  7. Structural valence per-person per-genre → influences body baseline
     → same genre, different person = different valence tag                  🟡

  8. Music Background-Pattern = frequency-driven, no DEDICATED neurochemical subsidy
     → frequency × duration compensate. Borrowed social neurochemistry (oxytocin inconsistent) 🟡


═══ 03-Sound-Reward-Pipeline (Insights 9-12) ═══

  9. Salimpoor 2011 caudate/NAcc = DIRECT validation of 7-step mechanism
     → 2 brain regions, 2 time points = PE ≠ reward                        🟢

  10. Musical anhedonia = Body-Feedback-Precondition Precondition-2 Chunk-Substrate
      fail at hardware level (broken pathway)
      → pipeline REQUIRES intact pathway. PE ok + pathway broken → no reward 🟢

  11. Cheung 2019: pleasure MAX when uncertainty HIGH + outcome POSITIVE
      → PE + coherence = reward model validated with 80k chords              🟢

  12. Music boredom = VTA habituation + prediction completion
      → Boredom formula applied: prediction-delta = 0                       🟡


═══ 04-Sound-Social-Resonance (Insights 13-28) ═══

  13. Shared taste increases resonance probability via gap overlap + chunk overlap
      → = Enhancer, NOT resonance core                                      🟡

  14. Music taste match = Enhancer. Making music together = CAN BE resonance core
      → active = by-product match at OUTPUT. Passive = shared INPUT only    🟡

  15. Music = signal for gap overlap → Self-Pattern-Modeling fires → approach
      → body detects similarity → approach BEFORE PFC becomes conscious     🟡

  19. Music taste = proxy signal for Background-Pattern similarity
      → Boer 2011: values (not personality) mediate                         🟢

  20. Music REINFORCES Background-Pattern via Triple Bias
      → processing style converges via shared gist compilation              🟡

  21. 2 fans meet without knowing each other's taste → STILL increased resonance (process level)
      → gap overlap at processing style level, not just content             🟡

  22. Causation = bidirectional, selection dominant, reinforcement secondary
      → Direction confirmed (Selfhout 2009, Ter Bogt 2017). Exact ratio varies. 🟡

  23. Each genre biases Background-Pattern DIFFERENTLY → different type of resonance
      → jazz: nuanced. Metal: intense. Pop: social fluency.                🟡

  24. Non-mainstream genre = STRONGER resonance predictor (narrower filter)
      → Selfhout 2009 (J Adolescence): non-mainstream > mainstream for formation
      → Ter Bogt 2017: only highbrow consistently predicts friendship selection 🟢

  25. Blind compatibility (Q2) = TESTABLE PREDICTION not yet tested
      → framework predicts d=0.2-0.4. Literature gap confirmed.            🔴

  26. Full 5-step mechanism chain formalized
      → selection → reinforcement → meeting → discovery → snowball         🟡

  27. Discover shared taste = ACCELERATION in Entity-Compiled formation
      → VTA fires (unexpected similarity) + Self-Pattern-Modeling validation 🟡

  28. Genre specificity × signal: inverted-U discovery, monotonic accuracy
      → too niche = hard to find. Moderate niche = optimal signal.         🟡


═══ 05-Multi-Modal-Compound (Insights 29-32) ═══

  29. More modalities × COHERENT = compound reward (potentially super-additive)
      × INCOHERENT = compound dissonance. Effect size varies by conditions. 🟡

  30. Rhythm games = 5-modality sync = peak compound reward territory
      → designed optimal: audio+visual+motor+haptic+score                   🟡

  31. Film reward = different TYPE from game (not "less")
      → Film: deep Evaluative + Simulation-Engine. Game: broad compound.   🟡

  32. Sound oscillates Tonic ↔ Cyclic — dual function
      → background substrate (Tonic) + foreground anchor (Cyclic peaks)    🟡


═══ 06-Music-Architecture-Prediction (Insights 33-35c) ═══

  33. Music architecture = prediction + social bonding co-optimization
      → Each feature = solution to a brain prediction constraint.
      → Tonic=anchor, BPM=sync, verse-chorus=oscillation, repetition=training
      → ⚠️ Social bonding = co-equal driver (Savage 2021), not prediction alone 🟡

  34. ~94% pop = 4/4 + BPM ~120 + I-IV-V = top 3 chords
      → 4/4 = lowest complexity → widest Goldilocks accessibility
      → ⚠️ I-IV-V 62% = derived from 100-song corpus, not standalone stat  🟢

  35. Cross-cultural: universals = prediction constraints, learned = solutions
      → Tonic center, regular pulse, discrete pitch = universal             🟢
      → Specific scales, meters, forms = culturally specific                🟢

  35b. Tension-resolution = FRACTAL — same pattern at EVERY timescale
       → Beat (500ms) → phrase (8s) → section (30s) → song (3-4 min)      🟢
       → 1/f noise (Voss & Clarke 1975): mathematical proof of self-similarity
       → Melodic arch dominant in 6,251 melodies (Huron 1996)              🟢
       → Multi-scale prediction matching = compound reward across hierarchy 🟡

  35c. ⭐ Integer Ratio Principle = 1 principle operating across levels (v1.2)
       → Consonance (pitch), groove (rhythm), neural entrainment = SAME underlying rule:
         phase-locking easier when ratio = simple integers (1:2, 2:3)      🟢
       → Steve Reich "Piano Phase": designed violation → designed tension   🟢
       → Large & Palmer 2002 (Cognitive Science): neural resonance at integer-ratio 🟢
       → Bowling & Purves 2015: harmonicity basis — DEBATED (McDermott 2016) 🟢/⚠️


═══ 07-Music-Entrainment-Reward-Dynamics (Insights 36-39) ═══

  36. Neural entrainment = distributed oscillator WITH hub (putamen+SMA)
      → BPM regular → phase-lock → cross-region coherence → compound       🟢

  37. Music = continuous prediction stream with phasic reward peaks
      → SAME 7-step, DIFFERENT temporal pattern from math (discrete) or reading 🟡

  38. Gap formation trajectory = inverted-U across exposure
      → "No knowledge = no gap" → forming → Goldilocks → saturation        🟡
      → Window size ∝ complexity (simple narrow, jazz wide) — estimates    🟡

  38b. ⭐ Attention × Music: Effort vs Knowledge (REFINED v1.1)
       → Real-time analytical EFFORT CAN interfere with flow immersion      🟡
       → BUT accumulated analytical KNOWLEDGE INCREASES liking (Hou 2024)   🟢
       → 2 modes: Flow/immersion (PFC relaxed) + Expert appreciation (PFC+) 🟡
       → Depth layers: UNCONSCIOUS — lose depth → reduced enjoyment even without
         awareness of what's missing                                        🟢
       → Koelsch 2004: implicit harmony processing (ERAN response)         🟢
       → ⚠️ Original "analysis → kills pleasure" OVERSTATED (Hou 2024 contradicts)

  39. ⭐ Unified hierarchy: nested gap-fill = brain's GENERAL architecture
      → Music × math × language = shared IFG/BA44 mechanisms (Nakai 2026)  🟢/🟡
      → Startup parallel = analogical, NOT empirically tested               🟡
      → PFC budget → FORCED decompose → hierarchical nested levels
      → Music = PURE FORM (designed, fractal, passive, dense reward)
      → Quality prediction: decomposition × level alignment × Goldilocks    🟡
      → Mini-arc decomposition: Gap-Body-Need §5 (established)              🟢
      → Progress Principle: Amabile & Kramer 2011 (small wins = key)       🟢


═══ 08-Musical-Elements-Brain-Interface (Insights 40-44) ═══

  40. ⭐ Voice 3-Channel: vocal processing through 3 PARTIALLY SEPARABLE channels
      → Semantic (requires language) + Prosody (language-independent) + Voice-as-instrument
                                                                            🟢/🟡
      → ⭐ Norman-Haignere 2022: song-selective neurons STRENGTHENS model
      → Cross-talk exists (Gordon & Schon 2010) → "partially separable"

  41. ⭐ Why foreign-language music still moves you even without understanding the lyrics
      → 2 of 3 channels DO NOT require language comprehension → still active 🟡
      → Semantic OFF → PFC freed → possibly less interfered (not directly tested)
      → Poor lyrics when understood → Semantic DISRUPTS (negative prediction-delta)

  42. ⭐ Melody = multi-system activator (~5-6 systems from 1 line)
      → ~5-6 systems (auditory+motor+prediction+emotion+memory)             🟡
      → "Activation efficiency" = 🟡 FRAMEWORK CONCEPT, not published metric
      → 🔴 "First-lock mechanism" = NO evidence (Racette & Peretz 2007 suggests otherwise)
      → Earworm = plausible multi-system mechanism, NOT proven causal        🟡

  43. 6 structural attributes of effective melodic writing (research-supported)
      → Arch contour, small steps + sparse leaps, variation-based repetition,
        clear rhythmic profile, singable range, moderate statistical typicality 🟢
      → = Prediction architecture optimization at ELEMENT level

  44. Shape vs Content: music provides the SHAPE, the brain fills in the CONTENT
      → ⭐ Langer 1953 (Feeling and Form) — NOT novel framework claim
      → 3 mechanisms compress the BRECVEMA-8 (Juslin 2013): direct, learned, isomorphism
        (missing: Aesthetic Judgment = meta-level)                          🟡
      → Forced imagery: depends on congruence (complement OK, impose weaker) 🟡
      → "Ineffability" = body-feedback first, PFC label second (not mysterious)
```

---

## §4 — Framework Validation Points

```
5 LANDMARK PAPERS DIRECTLY VALIDATE FRAMEWORK:

  ★ Salimpoor 2011 (Nature Neuroscience)
    → 7-step mechanism: caudate ≠ NAcc = PE ≠ reward
    → Validates: Dopamine-Is-Not-Reward.md

  ★ Martínez-Molina 2016 (PNAS)
    → Musical anhedonia = domain-specific disconnect
    → Validates: Body-Feedback-Precondition Precondition-2 Chunk-Substrate
      (chunks base adequate) + pipeline integrity

  ★ Cheung 2019 (Current Biology)
    → 80k chords: uncertainty × positive = max pleasure
    → Validates: Prediction-Error-Is-Not-Reward.md (PE + coherence + Goldilocks)

  ★ Boer 2011 (PSPB)
    → Values (not personality) mediate music → attraction
    → Validates: Background-Pattern → values territory (deeper than surface)

  ★ Selfhout 2009 (Journal of Adolescence 32:95-107)
    → Non-mainstream music predicts friendship formation STRONGER
    → Ter Bogt 2017: only highbrow consistently predicts friendship selection
    → Validates: filter specificity model (narrower = stronger signal)
```

---

## §5 — Testable Predictions

```
5 FRAMEWORK-NOVEL PREDICTIONS:

  TP1 — Blind compatibility (04 §8):
    2 strangers matched by taste vs random → blind interaction → rapport ↑?
    UNTESTED. Framework predicts d=0.2-0.4. Closest: Byrne 1971 chain.

  TP2 — Niche > mainstream controlled (04 §5):
    Niche-matched pairs vs mainstream-matched → niche = STRONGER compatibility?
    PARTIALLY supported (Selfhout 2009). Need stranger-meeting design.

  TP3 — Active music → Entity-Compiled FASTER (04 §2):
    Singing/playing together → entity depth over time > other activities?
    PARTIALLY supported (Weinstein 2016). Need longitudinal measurement.

  TP4 — Music Background-Pattern → non-music processing (04 §3 Step ②):
    Same genre 5+ years → similar decision-making / ambiguity tolerance?
    UNTESTED. Need controlled processing style measurement.

  TP5 — Compound > sum in multi-modal (05 §2):
    Coherent audio+visual+action → reward > sum of individual modalities?
    PARTIAL (game engagement data). Need: fMRI comparing tiers.
```

---

## §6 — Open Questions

```
OQ1: Opioid vs dopamine in music pleasure — debate active
     Mas-Herrero 2023 challenges opioid role in SUBJECTIVE pleasure

OQ2: Consonance preference = innate or learned?
     McDermott 2016: likely learned. Some researchers argue partial innate.

OQ3: Music evolutionary function — social bonding vs other hypotheses
     Savage 2021: social bonding = leading. NOT settled.

OQ4: Music Background-Pattern → non-music domain transfer
     Framework predicts YES. Only indirect evidence.

OQ5: VR/full-immersion music neuroscience — almost no data yet

OQ6: Streaming era × music Background-Pattern formation
     Algorithm-driven exposure vs self-selection → different formation?

OQ7: Cross-cultural validation of 5-step chain
     Most research = WEIRD samples. Need non-Western replication.
```

---

## §7 — Dependencies (Framework Files Referenced)

```
CORE (all drill files):
  Chunk.md v2.3, Modality.md v1.0, Body-Feedback.md v3.1,
  Body-Feedback-Label.md v2.1

BY FILE:
  02: Background-Pattern.md v2.0, Valence-Propagation.md v3.0,
      Gap-Body-Need.md v1.0, Cortisol-Baseline.md v2.1
  03: Dopamine-Is-Not-Reward.md v1.2, Prediction-Error-Is-Not-Reward.md v2.0,
      Reward-Signal-Architecture.md v2.1, Boredom.md v2.0
  04: By-Product-Gap-Resonance.md v1.4, Self-Pattern-Modeling.md v3.1,
      Connection.md v5.0, Entity-Compiled.md v1.0, Anchor-Schema.md v1.2
  05: Autonomy-Hardware.md v1.1, Personal-Melody.md v2.0,
      Simulation-Engine.md v1.1, Melody-Arc.md v2.0
  08: Body-Feedback-Mechanism.md v2.1, By-Product-Gap-Resonance.md v1.4,
      Modality.md v1.0, PFC-Operations.md v1.0, Personal-Melody.md v2.0
```

---

## §8 — Position in Framework

```
  The framework already contains music-related files:
    Personal-Melody.md v2.0 — metaphor communication tool (Melody-Lens)
    Musical-Notation-Architecture.md — music = communication format (Language-Structure)
    Auditory-System-Arc.md — prenatal compile (Child-Chunk-Development)
    Prediction-Error-Is-Not-Reward.md §3 — Spotify test (Clarification)

  This drill COMPLEMENTS, does NOT replace:
    → Personal-Melody = metaphor. Drill = mechanism + evidence.
    → Musical-Notation = notation structure. Drill = neural processing + social.
    → Auditory-Arc = development. Drill = adult ongoing effects.
    → PE-clarification = 1 example. Drill = comprehensive mapping.

  Does NOT change framework mechanisms.
  VALIDATES + EXTENDS existing mechanisms through the music domain.
```

---

> *00-Overview v1.5 — Entry point for the Drill-Sound-Brain folder.
> 11 files (10 drill + 1 overview), ~6,600L. 44 insights. 5 validation points. 5 testable predictions.
> 7 open questions. Reading flow: 01→06→02→03→07→08→04→05→09.
> Core value: MAP neuroscience evidence onto framework mechanisms, VALIDATE, PREDICT, EXTEND.*
