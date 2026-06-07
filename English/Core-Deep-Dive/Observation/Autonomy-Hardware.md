---
title: Autonomy-Hardware — Why Self-Action = Reward
version: 1.2
created: 2026-04-20
updated: 2026-05-17
refined: 2026-05-23 (v1.2 — Concept Cascade: +Entity-Access calibration, +Hardware-Subsidy.
    Updated versions + cross-refs)
status: OBSERVATION PARAMETER v1.2 — HARDWARE MECHANISM
scope: |
  HARDWARE MECHANISM FILE: Explains WHY humans naturally prefer self-action over
  external control. This is NOT a "design" or "instinct" — it is an EMERGENT PATTERN
  from hardware architecture: efference copy + VTA prediction-delta + opioid system →
  self-action = higher prediction accuracy = higher body reward. Universal — everyone
  has it, cross-species.
  Supplements: vmPFC + DRN controllability learning (Maier & Seligman 2016),
  cortisol direction tag (novelty vs threat), opioid vs relief pathways.
  v1.1 KEY CHANGES:
    ⑪ +Compilable Architecture alignment: these emergent patterns = Compilable
       Architecture specific
    ⑫ +Cross-refs: Inter-Body-Mechanism v1.0, Body-Feedback-Label v2.0, dependency
       versions updated
purpose: |
  This file explains the HARDWARE MECHANISM that produces autonomy preference.
  Autonomy.md (companion file) explains SOFTWARE — chunk accumulation,
  developmental arc, individual tendency.
  Split because: hardware mechanism = universal, foundational.
  Software development = individual, experience-dependent.
  Other files (Cortisol-Baseline, Body-Feedback-Mechanism, Neural-Architecture) NEED
  to reference this file for efference copy reward + vmPFC/DRN mechanism
  that backup/Neurochemistry.md §6.3 previously contained.
position: |
  Core-Deep-Dive/Observation/ — companion to Autonomy.md (software/development).
  Hardware mechanism BUT located in Observation/ because: this pattern is OBSERVABLE
  FROM the hardware architecture itself, the hardware was not designed to be this way.
  Like VTA prediction-delta = emergent from architecture.
dependencies:
  - Core-v7.8-Draft.md — §8 observation parameters, Autonomy definition
  - Cortisol-Baseline.md v2.0 — §7.2-§7.3 chunk direction tag
  - Inter-Body-Mechanism.md v1.0 — §1.2 Compilable Architecture (general-purpose system)
  - Body-Feedback-Mechanism.md v2.0 — Chunk-Shift/Miss/Gap, prediction-delta
  - Body-Feedback-Label.md v2.0 — vocabulary consistency
  - backup/Neurochemistry.md — §6.3 controllability, vmPFC + DRN
  - Neural-Architecture.md — vmPFC sub-region, amygdala pathway
  - Neural-Processing-Flow.md — §8.2 Feeling circuit (Insula + ACC + vmPFC)
  - Imagine-Final.md — §1 student forced vs interested (line 174-179)
  - Liking-Wanting.md — §4 Path A (opioid) vs Path B (relief)
  - Domain-Mapping-Drive.md — Student A vs B, threat vs novelty path
  - Reward-Economics.md — §9 controllability, Deci 1971 overjustification
companion_file: Autonomy.md (software/development — chunk accumulation, developmental arc)
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Autonomy-Hardware — Why Self-Action = Reward

> You raise the glass of water to your mouth yourself. Your hand feels the
> temperature, weight, and trajectory.
> Brain predicts: "water ~25°C will touch lips at angle X in 0.3 seconds."
> Mouth receives → MATCH → body: "correct" → micro-opioid.
>
> Someone else brings the glass of water to your mouth. You are NOT holding the glass.
> Brain has NO efference copy. Hand feels NO sensory preview.
> Mouth receives water → "unpredicted timing, unpredicted temperature"
> → body: alerting signal, NOT reward.
>
> SAME water. SAME glass. SAME amount. DIFFERENT prediction accuracy.
>
> This is NOT "preference." This is ARCHITECTURE.
> Efference copy + sensory preview + VTA prediction-delta = hardware.
> Self-action = better prediction = more reward.
> External-action = no efference copy = no preview = less reward.
>
> Nobody "designed" the body to prefer self-action.
> Architecture PRODUCES that pattern on its own — emergent, just as VTA
> produces a dopamine signal on its own when outcome > prediction.
>
> This file: WHY hardware produces that pattern (mechanism),
> AND why being forced causes damage at the hardware level (cortisol direction tag).
> Autonomy.md (companion file): HOW that pattern develops per person (chunks).

---

## Table of Contents

- §0 — EMERGENT FROM ARCHITECTURE, NOT BY DESIGN
- §1 — EFFERENCE COPY → SELF-PREDICTION ACCURACY
  - §1.1 — Mechanism: Motor Command → Sensory Prediction
  - §1.2 — Multi-Channel Preview: Hand → Brain → Mouth
  - §1.3 — Compare Table: Self vs External
  - §1.4 — Prediction Accuracy = Measurable, NOT Abstract
- §2 — vmPFC + DRN: CONTROLLABILITY LEARNING
  - §2.1 — Maier & Seligman 2016: Helplessness = THE DEFAULT
  - §2.2 — vmPFC Learns "Controllable" → Suppresses DRN
  - §2.3 — Chronic Cortisol → vmPFC Atrophies → Helplessness
- §3 — CORTISOL DIRECTION TAG: SAME LEVEL, DIFFERENT TAG
  - §3.1 — Novelty Direction vs Threat Direction
  - §3.2 — Compile-Time Lock: Tag Does Not Change After Compile
  - §3.3 — "Skilled But Hates It" = Threat-Compiled Chunks
- §4 — OPIOID vs RELIEF: 2 PATHWAYS, 2 OUTCOMES
  - §4.1 — Path A (Self-Chosen): Opioid → Sustainable
  - §4.2 — Path B (Forced): Relief → Dependent
  - §4.3 — Deci 1971: External Overrides Internal
- §5 — BEING FORCED = PREDICTION OVERRIDE → 2-LAYER DISSONANCE
- §6 — HONEST ASSESSMENT
  - §6.1 — Tier 1: Research-Backed (🟢)
  - §6.2 — Tier 2: Framework Synthesis (🟡)
  - §6.3 — Tier 3: Hypothesis (🔴)
  - §6.4 — Open Questions
- §7 — CROSS-REFERENCES

---

## §0 — EMERGENT FROM ARCHITECTURE, NOT BY DESIGN

```
⭐ HARDWARE MECHANISM — UNIVERSAL:

  WHY HUMANS PREFER TO DO THINGS THEMSELVES:

    Nobody "taught" a baby to prefer self-feeding.
    Nobody "designed" the body to reward self-action.
    This pattern is EMERGENT from 3 hardware components that ALREADY EXIST:

    ① EFFERENCE COPY (🟢 von Holst & Mittelstaedt 1950):
      → Motor cortex sends command → SIMULTANEOUSLY sends a COPY to sensory cortex
      → Sensory cortex uses the copy to PREDICT upcoming sensory input
      → = ONLY when SELF-ACTING is there an efference copy
      → = When SOMEONE ELSE acts → NO copy → NO prediction

    ② VTA PREDICTION DELTA (🟢 Schultz 1997):
      → Outcome MATCHES prediction → neutral-to-positive signal
      → Outcome MISSES prediction → negative signal
      → = Self-action has efference copy → better prediction → more matches
      → = External-action has no copy → poorer prediction → more misses

    ③ OPIOID SYSTEM (🟢 Berridge 2003):
      → Prediction match → micro-opioid release
      → = "Correct" signal → hedonic micro-reward
      → = Accumulated through hundreds of instances → body PREFERS self-action

    → 3 INDEPENDENT components — nobody designed them "for autonomy"
    → Efference copy evolved for MOTOR CONTROL (avoid self-tickle, etc.)
    → VTA evolved for LEARNING (reward prediction)
    → Opioid evolved for HEDONIC VALUATION
    → BUT when they operate SIMULTANEOUSLY → emergent pattern:
      "self-action = better prediction = more reward"
    → = AUTONOMY PREFERENCE = BYPRODUCT of architecture
    → = Like: nobody designed VTA "for novelty" — VTA fires on prediction
      delta, novelty HAPPENS to produce large delta → novelty preference emerges

  COMPARISON WITH OTHER EMERGENT PATTERNS:

    ┌──────────────────────┬──────────────────────────────────────┐
    │ EMERGENT PATTERN     │ HARDWARE COMPONENTS                  │
    ├──────────────────────┼──────────────────────────────────────┤
    │ Novelty preference   │ VTA prediction-delta + dopamine      │
    │                      │ = Large delta → large signal → seek  │
    ├──────────────────────┼──────────────────────────────────────┤
    │ Loss aversion        │ VTA asymmetry (loss > gain signal)   │
    │ (Protect)            │ = Negative delta > positive delta    │
    ├──────────────────────┼──────────────────────────────────────┤
    │ ⭐ AUTONOMY PREFER.  │ Efference copy + VTA + opioid        │
    │                      │ = Self-action → copy → better        │
    │                      │   prediction → more match → reward   │
    ├──────────────────────┼──────────────────────────────────────┤
    │ Boredom              │ VTA habituates (delta → 0 over time) │
    │                      │ + gap detection → dissonance signal  │
    └──────────────────────┴──────────────────────────────────────┘

    → All = EMERGENT, not "designed for"
    → All = observable FROM architecture, UNIVERSAL
    → All = scientifically valuable because TESTABLE + FALSIFIABLE

  ⭐ COMPILABLE ARCHITECTURE (Inter-Body-Mechanism.md §1.2):

    All patterns in the table above = COMPILABLE ARCHITECTURE emergent.
    Hardwired Architecture (insects): hardwired stimulus→response.
      → No efference copy → sensory prediction comparison path.
      → No vmPFC → no controllability learning.
      → No need for "autonomy preference" — all actions pre-wired.
    Compilable Architecture (mammals):
      → General-purpose reward + compilation + PFC.
      → Efference copy + VTA + opioid = autonomy preference = BY-PRODUCT.
      → vmPFC + DRN = controllability LEARNABLE (Maier & Seligman 2016).
    This file: documents the HARDWARE MECHANISM that produces autonomy preference
    in Compilable Architecture.

  ⚠️ IMPORTANT DISTINCTION:

    HARDWARE (this file): "WHY self-action = reward"
      → Universal — everyone, every culture, cross-species
      → Doesn't need to be "learned" — architecture produces it automatically
      → Efference copy present from birth (even before motor precision)

    SOFTWARE (Autonomy.md): "WHO will have HIGH or LOW autonomy tendency"
      → Individual — differs per person based on experience
      → NEEDS to be "built" — motor chunks, controllability chunks, meta-chunk
      → Depends on environment (parents, school, culture)

    → Hardware provides REWARD for self-action by default
    → Software determines WHETHER someone can ACCESS that reward
    → Child who is chronically forced: hardware STILL rewards self-action
      BUT software has compiled "self-action = punishment" → SUPPRESSES reward path
    → = Hardware correct, software overrides → "knows they should act
        independently but doesn't dare"
```

---

## §1 — EFFERENCE COPY → SELF-PREDICTION ACCURACY

### §1.1 — Mechanism: Motor Command → Sensory Prediction

```
🟢 RESEARCH (von Holst & Mittelstaedt 1950, established neuroscience):

  EFFERENCE COPY — BASIC MECHANISM:

    When YOU perform an action:
      ① Motor cortex generates COMMAND → sends to muscles
      ② SIMULTANEOUSLY: motor cortex sends a COPY (efference copy)
         → to sensory cortex
      ③ Sensory cortex uses the copy → PREDICTS upcoming sensory input
         → "expect sensation X at time Y with intensity Z"
      ④ Sensory input arrives → COMPARE with prediction
      ⑤ Match → neutral-to-positive signal
         Mismatch → alerting/error signal

    When SOMEONE ELSE performs an action on you:
      ① NO motor command from you
      ② NO efference copy
      ③ Sensory cortex has NO prediction template
      ④ Sensory input arrives → "UNPREDICTED"
      ⑤ Alerting signal (even if the input is positive)

  🟢 CLASSIC EVIDENCE:

    SELF-TICKLE (🟢 Blakemore et al. 1998):
      → Tickle yourself → efference copy PREDICTS the sensation
      → Prediction MATCHES → signal CANCELLED → not ticklish
      → Someone else tickles → NO efference copy → UNPREDICTED → ticklish
      → = Efference copy CANCELS self-generated sensory input
      → = SAME input, DIFFERENT prediction → DIFFERENT body response

    EXTENDED EXAMPLES:
      → Scratching your own head: efference copy predicts → match → neutral
      → Someone else scratches your head: no copy → unpredicted → startle/alerting
      → = Hardware DISTINGUISHES self-action vs external-action
        at the SENSORY LEVEL, BEFORE conscious processing

  ⭐ FRAMEWORK APPLICATION:

    Efference copy = the PHYSICAL REASON why self-action
    provides higher prediction accuracy than external-action.

    NOT "psychology" or "preference" — it is NEUROSCIENCE ARCHITECTURE.
    Body DISTINGUISHES self vs external at the millisecond level.
    And prediction match = micro-opioid reward (§0 ③).
    → = Self-action INHERENTLY more rewarding at the hardware level.
```

### §1.2 — Multi-Channel Preview: Hand → Brain → Mouth

```
🟡 FRAMEWORK SYNTHESIS (🟢 efference copy + 🟢 multi-sensory integration):

  SELF-FEEDING — MULTI-CHANNEL PREDICTION CASCADE:

    1. Motor cortex: "bring spoon to mouth" (command)
    2. Efference copy → somatosensory cortex:
       "expect spoon to touch lips at angle X, pressure Y, timing Z"
    3. Hand holds spoon → touch receptors FIRE:
       → Thermal: "food ~35°C" (preview for mouth)
       → Texture: "soft, smooth" (preview for tongue)
       → Weight: "~5ml" (preview for quantity)
    4. Brain UPDATES prediction for mouth:
       "food ~35°C, soft, quantity ~5ml, arriving in 0.5 seconds"
    5. Mouth receives → compares with ENRICHED prediction → MATCH
    6. VTA: match → neutral-positive delta
    7. Opioid: match → micro-reward

  PARENT FEEDING — PREDICTION POOR:

    1. NO motor command from child → NO efference copy
    2. Sensory cortex has NO prediction template
    3. Child's hand NOT holding the spoon:
       → NO thermal preview
       → NO texture preview
       → NO weight preview
    4. Brain: NO enriched prediction available
    5. Mouth receives input → "unpredicted timing, temperature, quantity"
    6. VTA: unpredicted (even if positive) → alerting signal, NOT reward
    7. = Mild dissonance, not catastrophic but CONSISTENT

  SELF-DRESSING — SAME MECHANISM:

    Child dresses themselves:
      → Efference copy predicts every contact point
      → Hand feels fabric → preview for body surface
      → Child adjusts speed, pressure in real-time based on body signal
      → = PREDICTION MATCH at most contact points

    Parent dresses child:
      → Fabric rubs along PARENT'S trajectory → child CANNOT predict
      → Pressure points where parent places hands → do NOT match child's comfort
      → Speed: parent dresses quickly → child's body cannot adapt in time
      → = PREDICTION MISS at many contact points

    → SLOW but COMFORTABLE (self-dressing) > fast but PREDICTION MISS
        (parent dressing)
    → = Cost (slow) < benefit (prediction match) when motor chunks SUFFICIENT
```

### §1.3 — Compare Table: Self vs External

```
⭐ SUMMARY TABLE:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ PARAMETER          │ SELF-ACTION          │ EXTERNAL-ACTION      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Efference copy     │ ✅ PRESENT           │ ❌ ABSENT            │
  │ Timing prediction  │ HIGH (self-determined)│ LOW (someone else)  │
  │ Spatial prediction │ HIGH (motor command) │ LOW (unpredicted)    │
  │ Thermal preview    │ YES (hand feel)      │ NO (no hand contact) │
  │ Texture preview    │ YES                  │ NO                   │
  │ Olfactory preview  │ CLOSER (self-paced)  │ PARTIAL              │
  │ Overall prediction │ HIGH                 │ LOW                  │
  │ VTA signal         │ Match → positive     │ Miss → alerting      │
  │ Opioid             │ Micro-reward         │ Absent               │
  │ Body feedback      │ REWARD               │ MILD DISSONANCE      │
  └────────────────────┴──────────────────────┴──────────────────────┘

  → SAME action. SAME object. SAME outcome.
  → DIFFERENT: who controls → DIFFERENT prediction accuracy → DIFFERENT
      body feedback.
  → = HARDWARE ARCHITECTURE produces this distinction automatically.
  → = Everyone has it. All ages. Cross-species.
```

### §1.4 — Prediction Accuracy = Measurable, NOT Abstract

```
⭐ FALSIFIABILITY:

  "AGENCY FEELING" (mainstream):
    → "The feeling that I have the right to decide"
    → MEASURED HOW? → self-report questionnaire
    → HOW TO FALSIFY? → unfalsifiable
    → = PFC LABEL for body state — useful for communication, does NOT
        explain mechanism

  "SELF-PREDICTION ACCURACY" (framework):
    → Self-action → sensory outcome MATCH/MISMATCH with prediction
    → MEASURED BY:
      ① Efference copy match ratio (neural imaging, 🟢 technology exists)
      ② Sensory prediction-delta (VTA dopamine, 🟢 Schultz 1997)
      ③ Opioid release on match (🟢 PET scan measurable)
      ④ Behavioral proxy: preference test (choose self vs external)
    → HOW TO FALSIFY:
      → If self-action does NOT produce higher prediction accuracy
        → efference copy mechanism falsified (unlikely — well-established)
      → If higher prediction accuracy does NOT produce more reward
        → VTA/opioid link falsified (unlikely — Schultz + Berridge)
    → = CLEAR testable chain → HIGH scientific value

  FRAMEWORK POSITION:
    → "Agency feeling" = PFC label for body state
    → Body state = prediction accuracy pattern (measurable)
    → Like: "pain" = PFC label for nociceptor signal
    → "Pain" useful for communication. "Nociceptor signal" explains mechanism.
    → "Agency feeling" useful for communication. "Prediction accuracy" explains
        mechanism.
```

---

## §2 — vmPFC + DRN: CONTROLLABILITY LEARNING

### §2.1 — Maier & Seligman 2016: Helplessness = THE DEFAULT

```
🟢 RESEARCH — REVERSED ORIGINAL THEORY:

  ORIGINAL (Seligman 1967):
    → Normal state = ACTIVE
    → Uncontrollable events → LEARN helplessness
    → = "Learned helplessness" = brain LEARNS to be passive

  REVERSED (Maier & Seligman 2016):
    → Normal state = PASSIVE (helplessness)
    → Brain must LEARN that the situation is controllable
    → = "Learned controllability" is the thing that must be learned
    → = Passive response = DEFAULT (brainstem DRN)
    → = Active response = LEARNED (vmPFC inhibits DRN)

  🟢 NEURAL MECHANISM (Maier & Seligman 2016; Maier & Watkins 2010):

    DRN (Dorsal Raphe Nucleus — brainstem):
      → Fires during aversive event → passive response DEFAULT
      → = Serotonin release → passive coping (freeze, give up)
      → = NOT "depression serotonin" — it is the passive default

    vmPFC (ventromedial Prefrontal Cortex):
      → CAN learn "this situation is controllable"
      → Controllable DETECTED → vmPFC INHIBITS DRN
      → DRN suppressed → passive response BLOCKED → active coping possible
      → = vmPFC = GATE for active behavior

    EVIDENCE:
      → vmPFC lesion → animals CANNOT learn controllability
        → Behave helpless EVEN when situation IS controllable
      → vmPFC intact + repeated controllable experience → robust controllability

  ⭐ FRAMEWORK TRANSLATION:

    DRN default = body assumes "my actions don't matter"
    vmPFC learns = body learns "my actions → outcomes"
    vmPFC training = ACCUMULATED EXPERIENCE of controllable situations

    → = Hardware ALLOWS learning controllability
    → = But MUST BE TRAINED through experience
    → = Without training (helicopter parenting) → DRN default REMAINS
    → = With training (allowed to try) → vmPFC robust → active coping

  ⚠️ THIS CONTENT WAS PREVIOUSLY IN backup/Neurochemistry.md §6.3:
    → "Controllability = the most important variable"
    → "Action Clarity ≈ controllability + available action path"
    → Replacement files (Neural-Architecture, Neural-Processing-Flow)
      DO NOT cover vmPFC/DRN controllability in detail
    → This file = PRIMARY REFERENCE for this mechanism
```

### §2.2 — vmPFC Learns "Controllable" → Suppresses DRN

```
🟡 FRAMEWORK SYNTHESIS (🟢 mechanism, 🟡 chunk framing):

  vmPFC LEARNING PROCESS:

    Step 1: Aversive event → DRN fires (DEFAULT passive)
    Step 2: Subject takes action + outcome CHANGES
      → vmPFC detects: "action → outcome changed" = controllability signal
    Step 3: Repeated controllable experiences
      → vmPFC strengthens: "situations OF THIS TYPE = controllable"
    Step 4: Next similar event
      → DRN fires (DEFAULT) → vmPFC: "controllable!" → INHIBITS DRN
      → Passive response BLOCKED → active coping ENABLED

  ⭐ DOMAIN-SPECIFIC (framework addition):

    vmPFC does NOT learn "everything is controllable" — learns PER DOMAIN:
      → Self-feed successfully × 50 → "eating = controllable"
      → Self-dress successfully × 30 → "dressing = controllable"
      → Never resolved conflict → "conflict = ?"
      → = DOMAIN-SPECIFIC controllability

    → CEO confident (business: thousands of experiences)
      but helpless in relationships (never trained)
    → Student good at math (novelty path) but social anxiety (no training)
    → = Autonomy ≠ global trait — collection of domain-specific states
    → = NOT "personality" — it is a chunk gap
```

### §2.3 — Chronic Cortisol → vmPFC Atrophies → Helplessness

```
🟢 RESEARCH (McEwen 2007, Maier & Seligman 2016):

  CHRONIC CORTISOL → vmPFC STRUCTURAL DAMAGE:

    → Chronic cortisol → dendritic retraction in vmPFC
      (🟢 McEwen 2007: glucocorticoid-mediated dendritic remodeling)
    → vmPFC neurons SHRINK → fewer connections → WEAKER DRN inhibition
    → = vmPFC PHYSICALLY ATROPHIES → loses controllability learning
    → = DRN REGAINS DOMINANCE → passive default RETURNS

    Consequence:
      → Person who HAD controllability → LOSES it after chronic stress
      → "Helplessness generalizes to even controllable situations"
      → = Biological basis for "cannot start even when knowing they should"
      → = NOT laziness — vmPFC structure has been damaged

  2 PATHWAYS TO HELPLESSNESS:

    Pathway 1 — OVER-CONTROL (no training):
      → Parent does EVERYTHING for child → no controllable experience
      → vmPFC NOT trained → DRN default stays
      → 🟢 LeMoyne & Buchanan 2011: helicopter → helplessness

    Pathway 2 — CHRONIC THREAT (damage):
      → Parent imposes threats → chronic cortisol
      → vmPFC developing UNDER cortisol → structural damage
      → Controllability chunks DO NOT compile (or are weak)
      → = ≠ "lack of willpower" — vmPFC developmental deficit

    BOTH → same outcome: helplessness
    = Body-Base-Example.md: "parent's over-feeding of caring channel
      = child's starving of autonomy channel"

  RECOVERY:
    → vmPFC CAN recover (🟢 neuroplasticity)
    → BUT slower than the damage
    → Requires: CONTROLLED exposure to controllable situations
    → = CBT graded exposure = REBUILD vmPFC controllability
    → = Therapy ≠ "talk about feelings" — it is RE-TRAINING the vmPFC
    → Timeline: months to years
```

---

## §3 — CORTISOL DIRECTION TAG: SAME LEVEL, DIFFERENT TAG

### §3.1 — Novelty Direction vs Threat Direction

```
🟢/🟡 (research: cortisol mechanisms 🟢, direction framing 🟡):

  SAME CORTISOL LEVEL, DIFFERENT DIRECTION (Cortisol-Baseline §7.2-§7.3):

    ┌─────────────────┬────────────────────────┬──────────────────────┐
    │                 │ NOVELTY DIRECTION      │ THREAT DIRECTION     │
    │                 │ (self-chosen,curious)  │ (forced, scared)     │
    ├─────────────────┼────────────────────────┼──────────────────────┤
    │ Cortisol level  │ Moderate               │ Moderate-High        │
    │ Accompanied by  │ + Dopamine (seeking)   │ + NE (alert)         │
    │                 │ + Mild opioid (preview)│ + Adrenaline         │
    │ Body state      │ ENERGIZED              │ TENSE                │
    ├─────────────────┼────────────────────────┼──────────────────────┤
    │ Chunk tag       │ APPROACH (opioid)      │ AVOIDANCE (threat)   │
    │                 │ "understanding =       │ "studying = painful" │
    │                 │  pleasant"             │                      │
    │ Long-term       │ Body LIKES using it    │ Body AVOIDS using it │
    ├─────────────────┼────────────────────────┼──────────────────────┤
    │ Sleep quality   │ GOOD                   │ CAN BE POOR          │
    │ Repair quality  │ HIGH                   │ LOW                  │
    │ Net health      │ Repair ≥ Damage        │ Repair < Damage      │
    ├─────────────────┼────────────────────────┼──────────────────────┤
    │ Chunk quality   │ PRESENT + USABLE       │ PRESENT + HARD TO USE│
    │                 │ + ENJOYED              │ + FEAR-ATTACHED      │
    └─────────────────┴────────────────────────┴──────────────────────┘

  AUTONOMY CONNECTION:
    → Self-chosen action = typically NOVELTY direction
    → Forced action = typically THREAT direction
    → = Autonomy (self) vs Forced (external) → DIFFERENT cortisol direction
    → = DIFFERENT chunk tag → DIFFERENT life trajectory

    (Table duplicated from Cortisol-Baseline §7.2 for self-contained reference)
```

### §3.2 — Compile-Time Lock: Tag Does Not Change After Compile

```
🟡 FRAMEWORK:

  CHUNKS COMPILE AT THE MOMENT cortisol fires (Cortisol-Baseline §7.3):
    → The body state direction at that moment = LOCKED IN to the chunk
    → = COMPILE-TIME variable

  Student A (self-chosen, interested):
    → Cortisol moderate + dopamine + opioid preview
    → Body state = NOVELTY direction
    → Math chunks compile with APPROACH TAG (opioid present at compile)
    → Adult: "I love math, use it comfortably"

  Student B (forced, threatened):
    → Cortisol moderate (SAME LEVEL) + NE + adrenaline
    → Body state = THREAT direction
    → Math chunks compile with AVOIDANCE TAG (threat direction at compile time)
    → Adult: "I'm good at math but HATE opening a math book"

  → SAME content learned. SAME cortisol level.
  → DIFFERENT direction → DIFFERENT tag → DIFFERENT outcome 20 years later.
```

### §3.3 — "Skilled But Hates It" = Threat-Compiled Chunks

```
🟡 FRAMEWORK (Domain-Mapping-Drive.md §7.1):

  ┌────────────────────┬──────────────────┬──────────────────┐
  │                    │ STUDENT A (self) │ STUDENT B (forced│
  ├────────────────────┼──────────────────┼──────────────────┤
  │ Short term (6 mo)  │ Slower start     │ Faster (forced)  │
  │ Chunk quantity     │ Fewer initially  │ More initially   │
  │ Chunk quality      │ Approach-tagged  │ Avoidance-tagged │
  │ Long term (10 yr)  │ Continues growing│ Decay + avoidance│
  │ Net result         │ DEEP + ENJOYED   │ BROAD but AVOIDED│
  └────────────────────┴──────────────────┴──────────────────┘

  Decision-makers (parents, school) see 6-month results:
    → Student B = "better" → push system toward threat path
  Decision-makers DO NOT see 10-year results:
    → Student A = MUCH better
  → = Short-term visible bias (Domain-Mapping-Drive.md line 2991-2993)

  "Skilled but hates it" = VERY COMMON phenomenon:
    → Chunks EXIST (skilled) but avoidance-tagged (hates it)
    → Body AVOIDS using them → career in that field = BURNOUT risk
    → = Threat-compiled mastery = fragile achievement
```

---

## §4 — OPIOID vs RELIEF: 2 PATHWAYS, 2 OUTCOMES

### §4.1 — Path A (Self-Chosen): Opioid → Sustainable

```
🟡 FRAMEWORK (🟢 Berridge opioid/dopamine):

  PATH A — SELF-CHOSEN:

    ① Body-need active (curiosity, interest)
    ② PFC: Imagine-Final = "I want to UNDERSTAND / DO / SOLVE"
    ③ Self-initiated action → efference copy → prediction
    ④ Outcome MATCHES → VTA: positive prediction-delta
    ⑤ Opioid: match → "correct" → hedonic reward
    ⑥ Chunk compiles with APPROACH TAG → "understanding = pleasant"
    ⑦ Next encounter: body LIKES using chunk → approach → repeat

    = Self-reinforcing, self-sustaining, compound, resilient
```

### §4.2 — Path B (Forced): Relief → Dependent

```
🟡 FRAMEWORK (Liking-Wanting.md §4):

  PATH B — FORCED:

    ① External threat (punishment, shame)
    ② Body-need: SAFETY (avoid punishment), NOT curiosity
    ③ Imagine-Final: "avoid being scolded" (Imagine-Final.md line 178)
    ④ Action = compliance (externally directed)
    ⑤ Threat REMOVED → cortisol DROPS → RELIEF
    ⑥ Chunk compiles with AVOIDANCE TAG → "studying = uncomfortable, done = relief"
    ⑦ Next encounter: body AVOIDS → requires external threat

    = Dependent, decays without threat, shallow, fragile

  ⚠️ SAME BEHAVIOR, DIFFERENT MECHANISM:
    Path A student: sits to do homework → opioid → sustainable
    Path B student: sits to do homework → relief → stops without threat
    Observer: "both are diligent" → CANNOT DISTINGUISH from behavior
    Body: COMPLETELY DIFFERENT

    → = Why 2 students with the same grades BUT:
      A enters adult life → continues growing
      B enters adult life → STOPS → "hates the field they were skilled at"
```

### §4.3 — Deci 1971: External Overrides Internal

```
🟢 RESEARCH (Deci 1971, Reward-Economics.md §9):

  OVERJUSTIFICATION EFFECT:

    🟢 Deci (1971):
      → Group A: plays puzzle (intrinsic)
      → Group B: plays puzzle + paid
      → Phase 2: no payment → Group B STOPPED. Group A continued.
      → = External reward REPLACED internal reward

  FRAMEWORK TRANSLATION:

    Group A: Imagine-Final = "understand" → self-prediction → opioid →
        sustainable
    Group B: Imagine-Final SHIFTS to "get paid" → external prediction
      → Remove payment → prediction MISS → WORSE than never paid
      → Old Imagine-Final ("understand") DELINKED → VERY HARD to recover

  IMPLICATION:
    External rewards (candy, money, praise) CAN DAMAGE autonomy:
      → "Reward TOO STRONG/PROLONGED = overrides internal prediction"
      → Reward-Economics.md §9: external reward = scaffolding →
          REMOVE when done
      → Keep too long → autonomy LOST
```

---

## §5 — BEING FORCED = PREDICTION OVERRIDE → 2-LAYER DISSONANCE

```
🟡 FRAMEWORK:

  "BEING FORCED" = PREDICTION OVERRIDE WITH 2 LAYERS:

  Layer 1 — Prediction override (immediate, Body-Feedback-Mechanism §3.2):
    → Current prediction stream is interrupted
    → Child is playing with a toy → parent spoon-feeds → INTERRUPT
    → Body: "prediction for toy → suddenly food = OVERRIDE"
    → = Like any prediction miss

  Layer 2 — Controllability dissonance (meta, vmPFC):
    → "MY prediction = irrelevant because SOMEONE ELSE decides"
    → vmPFC: "this situation is NOT controllable"
    → DRN: passive coping response
    → = META-LEARNING: "my prediction doesn't matter here"
    → 🟢 Maier & Seligman 2016: uncontrollable → DRN default → passive

  ⚠️ "FORCED + GOOD OUTCOME" STILL = DISSONANCE:

    Parent forces child to study math → child becomes good at math →
        outcome is GOOD
    BUT:
      → Child's prediction was overridden → chunks compile with AVOIDANCE TAG
      → = "Good at math but HATES math"
      → = Outcome quality ≠ autonomy satisfaction

    Boss forces new approach → result is better
    BUT:
      → Employee's prediction was overridden → STILL dissonance
      → = "Correct but I DID NOT DECIDE" = low autonomy DESPITE good outcome
```

### §5.1 — × New Concepts (28-session Drill Propagation)

```
ENTITY-ACCESS × AUTONOMY-HARDWARE (Entity-Access.md v1.2):
  → vmPFC controllability learning (§2) = Entity-Access CALIBRATION hardware:
    vmPFC learns "I can control ACCESS" → Entity-Access-Calibration.md v1.0
    vmPFC atrophies (chronic stress) → LOST calibration capacity
    → = Autonomy hardware = access calibration hardware
  → DRN inhibition pattern = per-entity access gating:
    Controllable entity → vmPFC inhibits DRN → approach
    Uncontrollable entity → DRN fires → helplessness per entity

HARDWARE-SUBSIDY × AUTONOMY (Entity-Valence-Dynamics.md v1.0 §5):
  → Hardware-subsidy INTERACTS with autonomy hardware:
    High subsidy entities (child, partner): efference copy BONUS
      → Body rewards self-action toward THESE entities even MORE
      → = WHY caring for one's child = highest autonomy feeling
          (hardware + subsidy compound)
    Low subsidy entities (stranger): efference copy ALONE
      → Body reward proportional to prediction accuracy only
  → Autonomy + hardware-subsidy = COMPOUND reward:
    Self-chosen action + toward subsidy entity = MAXIMUM opioid
    Forced action + toward non-subsidy entity = MINIMUM (double penalty)

🟡 Entity-Access × autonomy hardware = framework convergence (vmPFC = calibration)
🟡 Hardware-Subsidy × autonomy = framework application (compound reward)
```

---

## §6 — HONEST ASSESSMENT

### §6.1 — Tier 1: Research-Backed (🟢)

```
🟢 STRONG SUPPORT:

  ① Efference copy mechanism
    → von Holst & Mittelstaedt (1950): motor copy → sensory prediction
    → Blakemore et al. (1998): self-tickle cancellation
    → Well-established, foundation of motor neuroscience

  ② VTA prediction-delta
    → Schultz (1997): outcome vs prediction → dopamine signal
    → Foundation of reinforcement learning neuroscience

  ③ vmPFC + DRN controllability
    → Maier & Seligman (2016): reversed theory, well-replicated
    → Maier & Watkins (2010): vmPFC inhibits DRN mechanism
    → McEwen (2007): chronic cortisol → vmPFC dendritic retraction

  ④ Overjustification
    → Deci (1971): well-replicated across decades
    → SDT (Deci & Ryan 1985, 2000): autonomy + competence + relatedness

  ⑤ Opioid system
    → Berridge (2003): opioid vs dopamine hedonic distinction
```

### §6.2 — Tier 2: Framework Synthesis (🟡)

```
🟡 PLAUSIBLE — combines established research, not yet directly tested:

  ① "Self-action = higher prediction accuracy than external-action"
    → Logical from efference copy + multi-channel preview
    → No direct experiment yet comparing prediction-delta self vs other-fed
    → TESTABLE: compare sensory prediction-delta

  ② Cortisol direction tag = COMPILE-TIME lock
    → Consistent with cortisol + opioid literature
    → "Tag as permanent" unclear = permanent or gradual?
    → Therapy suggests retagging possible but difficult

  ③ Emergent pattern framing
    → "Autonomy preference = byproduct of architecture"
    → Logically sound — but "emergent" is a claim about WHY, hard to test
    → Alternative: could be directly selected (evolution for autonomy)

  ④ Compilable Architecture specificity (v1.1)
    → "These emergent patterns = Compilable Architecture only" = framework claim
    → Insects DO have simpler efference copies → but no vmPFC/controllability
    → Boundary between Hardwired and Compilable may be gradient, not sharp
```

### §6.3 — Tier 3: Hypothesis (🔴)

```
🔴 SPECULATIVE:

  ① Multi-channel preview specifics (hand → temperature → mouth prediction)
    → Nobody has measured whether hand temperature preview ACTUALLY
      improves infant mouth prediction accuracy
    → TESTABLE IN PRINCIPLE but not yet tested

  ② "Emergent not designed" claim
    → Framework ASSERTS autonomy preference = byproduct
    → Could be wrong: maybe direct selection pressure FOR autonomy
    → Distinction matters for theory, less for practical application
```

### §6.4 — Open Questions

```
⚠️ 3 OPEN QUESTIONS (hardware-specific):

  Q1: Efference copy DEVELOPMENT — when does it become functional?
    → Present from birth? Or develops with motor cortex?
    → If present from birth → hardware reward for self-action from DAY 1
    → If develops → there is a "before efference copy" period
    → 🟢 Research suggests: basic form present early, refines with development

  Q2: vmPFC critical period?
    → Is there a window for controllability learning?
    → Or lifelong plasticity?
    → 🟢 Neuroplasticity research: lifelong but SLOWER with age
    → Practical: early training = easier, but adult recovery = possible

  Q3: Can approach tag → avoidance tag (and reverse)?
    → Trauma: can approach-tagged chunk be RE-tagged to avoidance?
    → Therapy: can avoidance-tagged be RE-tagged to approach?
    → Partially answered: therapy works slowly → retagging possible but difficult
    → = Important for intervention design
```

---

## §7 — CROSS-REFERENCES

```
DRILL SOURCE:
  → Inter-Body-Mechanism.md v1.0 §1.2 — Compilable Architecture (general-purpose,
    efference copy context)

VOCABULARY:
  → Body-Feedback-Label.md v2.0 — prediction-delta, approach/avoidance tag

HARDWARE/MECHANISM FILES:
  → Cortisol-Baseline.md v2.0 §7.2-§7.3 — direction tag, novelty vs threat
  → backup/Neurochemistry.md §6.3 — controllability, vmPFC + DRN (original source)
  → Neural-Architecture.md — vmPFC sub-region, amygdala pathway
  → Neural-Processing-Flow.md §8.2 — Feeling circuit (Insula + ACC + vmPFC)
  → Body-Feedback-Mechanism.md v2.0 §3 — Chunk-Shift/Miss/Gap, prediction-delta

COMPANION FILE:
  → Autonomy.md v1.1 — SOFTWARE/DEVELOPMENT: chunk accumulation, developmental arc,
    cross-parameter interactions, healthy vs toxic, counterweights

OBSERVATION FILES (cross-parameter):
  → Liking-Wanting.md §4 — Path A (opioid) vs Path B (relief)
  → Imagine-Final.md §1 — student forced vs interested (line 174-179)
  → Domain-Mapping-Drive.md §7.1 — Student A vs B, 10-year divergence
  → Reward-Economics.md §9 — controllability, Deci 1971

RESEARCH CITATIONS:
  🟢 von Holst & Mittelstaedt (1950) — efference copy
  🟢 Blakemore et al. (1998) — self-tickle cancellation
  🟢 Schultz (1997) — VTA prediction-delta
  🟢 Berridge (2003) — opioid vs dopamine
  🟢 Maier & Seligman (2016) — controllability = learned, helplessness = default
  🟢 Maier & Watkins (2010) — vmPFC + DRN mechanism
  🟢 McEwen (2007) — chronic cortisol → dendritic retraction
  🟢 Deci (1971) — overjustification effect
  🟢 Deci & Ryan (1985, 2000) — Self-Determination Theory
  🟢 LeMoyne & Buchanan (2011) — helicopter parenting → helplessness
```

---

## SUMMARY

```
AUTONOMY-HARDWARE = Why self-action = reward (emergent from architecture)

EFFERENCE COPY (§1): Self-action → motor cortex sends COPY → sensory cortex
  PREDICTS upcoming input → match → micro-opioid. External-action → no copy →
  no prediction → mild dissonance. = Physical mechanism, universal, measurable.

vmPFC + DRN (§2): Helplessness = THE DEFAULT (Maier & Seligman 2016 reversed).
  vmPFC LEARNS controllability → inhibits DRN. Chronic cortisol → vmPFC atrophies
  → helplessness returns. Domain-specific: controllable in A ≠ controllable in B.

CORTISOL DIRECTION (§3): Same level, DIFFERENT direction → DIFFERENT tag.
  Self-chosen = novelty direction = approach tag = body likes using it.
  Forced = threat direction = avoidance tag = body avoids. Compile-time lock.

2 PATHWAYS (§4): Path A (self) → opioid → sustainable.
  Path B (forced) → relief → dependent on threat. Same behavior, DIFFERENT mechanism.
  Overjustification (Deci 1971): external overrides internal = damage.

BEING FORCED (§5): 2-layer dissonance — immediate prediction override +
  meta controllability loss. Good outcome STILL = dissonance if forced.

= Hardware PRODUCES autonomy preference — emergent, not designed.
= Companion file Autonomy.md covers SOFTWARE: how this develops per person.

~904 lines | version 1.2 | 2026-05-23
v1.1 CHANGES: ⑪ +Compilable Architecture alignment (§0) ⑫ +Inter-Body-Mechanism/
  Body-Feedback-Label cross-refs ⑬ Dependency versions updated
v1.2 CHANGES: +Entity-Access calibration (§5.1), +Hardware-Subsidy (§5.1),
  version updates
```
