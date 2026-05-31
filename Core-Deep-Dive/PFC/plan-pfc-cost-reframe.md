# Plan: PFC Cost Reframe — "Glucose/Metabolic" → "Processing Load"

> **Vấn đề**: Framework cite Gailliot & Baumeister 2007 (glucose depletion → self-control fails)
> nhưng Hagger et al. 2016 (23 labs, d=0.04) đã falsify claim này.
> Framework hedge tốt ở PFC-Operations §8.3 nhưng §2.1, §4.3, §9.1 lại dùng
> "glucose consumption" như fact — internal contradiction.
>
> **Giải pháp**: Reframe "metabolic — glucose consumption" → "processing load"
> (serial bottleneck + catecholamine demand + allocation competition).
> Framework LOGIC không đổi. Chỉ mechanism label + citations thay đổi.

---

## I. RESEARCH FOUNDATION

### I.1 — Tại sao Gailliot 2007 bị falsify

```
Gailliot & Baumeister 2007 claim: self-control → blood glucose GIẢM → drink glucose → restore.

FALSIFIED BY:
  ① Hagger et al. 2016 (Registered Replication Report):
    23 independent labs, N=2,141, pre-registered.
    Effect size d = 0.04. Essentially ZERO.
    🟢 Highest quality replication in ego depletion literature.

  ② Physiological implausibility:
    Brain = ~5.6mg glucose/minute consumption.
    Total blood glucose = ~5g. Body homeostatically maintains it.
    10-minute cognitive task CANNOT meaningfully deplete blood glucose.
    Homeostasis: liver releases glucose to maintain blood levels.
    → Mechanism physiologically IMPOSSIBLE at the scale claimed.

  ③ Carter et al. 2015 (meta-analysis with bias correction):
    After correcting publication bias → ego depletion effect DISAPPEARS.

  ④ Dang et al. 2021 (second large replication):
    N=3,531 → near-zero effect. Confirms Hagger 2016.

  ⑤ Even Baumeister's group shifted:
    Later work moved from "glucose" to "motivational" explanations.
    The originator abandoned the glucose mechanism.
```

### I.2 — 3 cơ chế thay thế (all 🟢 established)

```
CƠ CHẾ A: SERIAL BOTTLENECK (Architectural)
  Musslick & Cohen 2021 (Trends in Cognitive Sciences)
  Petri, Musslick et al. 2021 (Nature Physics)

  PFC dùng shared representations (overlapping neural populations).
  → Shared representations = CANNOT parallel process.
  → 2 tasks sharing ANY representation → interference if simultaneous.
  → PFC PHẢI process SERIAL — hardware constraint, PERMANENT.
  → = WHY "multitasking" = rapid switching, not true parallel.

  Consequence cho framework:
    Compiled paths → basal ganglia, cerebellum → CAN parallel.
    Fresh paths → PFC → MUST serial → bottleneck.
    → Compiled cost ≈ 0 (bypasses PFC), Fresh cost > 0 (through PFC).
    → EXACTLY maps to framework's Compiled/Fresh distinction.

CƠ CHẾ B: CATECHOLAMINE MAINTENANCE (Neuromodulatory)
  Arnsten 2009 (Nature Reviews Neuroscience)
  Westbrook & Braver 2015 (Cognitive, Affective, & Behavioral Neuroscience)
  Westbrook & Braver 2016 (Neuron) — "Dopamine Does Double Duty"

  PFC sustained firing REQUIRES:
    → Dopamine at D1 receptors: narrow spatial tuning → reduce noise
    → Norepinephrine at α2A receptors: strengthen network connections
    → Both follow INVERTED-U: too little = impaired, too much = impaired
    → Prolonged use → catecholamine levels DECLINE → PFC performance DEGRADES
    → Sleep RESTORES catecholamine levels → "budget recharges"

  Consequence cho framework:
    "Mệt cuối ngày" = catecholamine levels genuinely LOWER
    "Budget recharges via sleep" = catecholamine restoration
    → This IS a real "depletion" — but of neurotransmitters, NOT glucose
    → Inverted-U explains stress interaction: cortisol → excess NE → PFC offline

CƠ CHẾ C: ALLOCATION COMPETITION (Computational)
  Kurzban, Duckworth & Kable 2013 (Behavioral and Brain Sciences)
  Inzlicht, Schmeichel & Macrae 2014 (Trends in Cognitive Sciences)
  Shenhav, Botvinick & Cohen 2017 (Annual Review of Neuroscience) — EVC model

  PFC = shared processing hardware for ALL cognitive control tasks.
  → Using PFC for task A = UNAVAILABLE for task B.
  → Subjective "effort" = brain's signal: "current allocation may not be optimal."
  → "Depletion" = motivational priority SHIFT (not energy exhaustion).
  → Sufficient incentive CAN restore "depleted" performance → not true exhaustion.

  Expected Value of Control (EVC):
    dACC computes: EVC = (payoff × probability) − cost
    → Determines whether, where, how much control to allocate.

  Consequence cho framework:
    "PFC budget shared" = allocation competition (all tasks compete for same PFC)
    "Parent mệt → Self-Pattern-Modeling yếu" = PFC allocated to work → less for child
    → Explains WHY motivation matters (incentive → reallocate)
    → Explains WHY beliefs about willpower affect performance
```

### I.3 — Tổng hợp: Processing Load = A + B + C

```
PROCESSING LOAD = 3 cơ chế ĐỒNG THỜI:

  ┌───────────────────────────┬──────────────────────────────────────┐
  │ Serial Bottleneck (A)     │ PFC cannot parallel → must queue     │
  │                           │ PERMANENT hardware constraint        │
  │                           │ Musslick & Cohen 2021               │
  ├───────────────────────────┼──────────────────────────────────────┤
  │ Catecholamine Demand (B)  │ DA/NE sustain working memory        │
  │                           │ DEGRADE with prolonged use           │
  │                           │ RESTORE via sleep                    │
  │                           │ Arnsten 2009, Westbrook 2016        │
  ├───────────────────────────┼──────────────────────────────────────┤
  │ Allocation Competition (C)│ All tasks share same PFC hardware   │
  │                           │ REAL-TIME opportunity cost signal    │
  │                           │ Kurzban 2013, Shenhav 2017          │
  └───────────────────────────┴──────────────────────────────────────┘

  → "Processing load" = label bao trùm cả 3.
  → Không commit vào 1 model → future-proof.
  → Framework logic KHÔNG THAY ĐỔI — chỉ mechanism label chính xác hơn.
```

---

## II. DEFINITION CHANGES

### II.1 — ① PFC Draft Cost

```
OLD:
  "① PFC draft cost (metabolic — glucose consumption)"
  "f(chain_length × novelty)"
  Citation: Gailliot & Baumeister 2007

NEW:
  "① PFC draft cost (processing load)"
  "f(chain_length × novelty)"
  Citations: Musslick & Cohen 2021, Arnsten 2009, Kurzban 2013
  
  = Cost of constructing novel processing paths through PFC's serial bottleneck.
  Serial bottleneck (shared representations cannot parallel process)
  + catecholamine demand (dopamine/NE required for working memory maintenance)
  + allocation competition (PFC serving current task = unavailable for others).
  DECREASES with compilation: compiled paths → basal ganglia → bypass PFC → cost ≈ 0.
```

### II.2 — PFC Budget

```
OLD:
  "PFC budget = total PFC resource. FINITE. SHARED.
   Depleted by fatigue, stress, sleep deprivation."

NEW:
  "PFC budget = total PFC processing capacity at any moment. FINITE. SHARED.
   Determined by:
     (a) Architectural ceiling — serial bottleneck, permanent hardware constraint
     (b) Catecholamine state — DA/NE levels, depletes with sustained use, restores via sleep
     (c) Allocation competition — current tasks occupy pipeline, real-time opportunity cost
     (d) Cortisol interference — stress → amygdala competes → effective budget shrinks"

  Note: (d) = already in framework (McEwen 2007, Arnsten 2009). Just made explicit.
```

### II.3 — Terms to REMOVE

```
REMOVE from framework vocabulary:
  "glucose consumption" — as mechanism for PFC cost (specific claim falsified)
  "glucose depletes" — as explanation for PFC failure
  "metabolic" — as shorthand for PFC draft cost (ambiguous, conflates Claim A and B)

KEEP (different claims, VALID):
  "metabolic" in evolutionary context (Herculano-Houzel 2012 — brain energy cost) → PFC-Development
  "metabolic" in Social Baseline Theory (Coan 2015 — proximity reduces cost) → Connection, Status
  "metabolic" in interoception (glucose/ghrelin/leptin sensing) → Neural-Processing-Flow, Core-Hardware
  "glucose" in nutrition context (PFC-Development §4: stable glucose = stable PFC) → VALID different claim
```

### II.4 — Citation Updates

```
REMOVE:
  Gailliot & Baumeister 2007 — as 🟢 for PFC cost mechanism
  (May keep as historical reference in §8.3 ego depletion discussion with ❌ or 🔴 tag)

ADD:
  Kurzban, Duckworth & Kable 2013 — opportunity cost model of subjective effort
  Musslick & Cohen 2021 — shared representations → parallel processing limits
  Arnsten 2009 — catecholamine modulation of PFC (already in file as R13, repurpose)
  Westbrook & Braver 2016 — dopamine double duty in cognitive effort
  Shenhav, Botvinick & Cohen 2017 — Expected Value of Control (EVC)
  Inzlicht, Schmeichel & Macrae 2014 — motivational shift account

KEEP (already in framework):
  Arnsten 2009 (R13) — already cited for PFC NE α1 disconnect. Expand role.
  Inzlicht & Schmeichel 2012 — already cited in §8.3. Expand role.
```

---

## III. AFFECTED FILES + CHANGE MAP

### Phase 1: Central File (PFC-Operations.md)

```
FILE: PFC-Operations.md v1.2 → v1.3

CHANGES:
  §2.1 (line 136):
    OLD: "COST: ① PFC draft (metabolic — glucose consumption)."
    NEW: "COST: ① PFC draft (processing load — serial bottleneck + catecholamine demand)."

  §4.3 (lines 362-371):
    OLD: "③ PFC metabolic budget = FINITE → glucose depletes."
         "🟢 Gailliot & Baumeister 2007: glucose depletion → self-control fails."
    NEW: "③ PFC processing capacity = FINITE → load exceeds capacity."
         "🟢 Kurzban 2013: opportunity cost → PFC reallocates away from current task."
         "🟢 Arnsten 2009: catecholamine decline → PFC sustained firing degrades."

  §8.3 (lines 682-706): KEEP + ENHANCE
    Already hedges well. Add:
    → Explicit note: Gailliot 2007 glucose mechanism FALSIFIED (Hagger 2016).
    → Framework's position STRENGTHENED by replacement models.
    → Add Kurzban 2013, Westbrook 2016 citations.
    → Move Gailliot from 🟢 to ❌ (falsified specific glucose mechanism)

  §9.1 (line 764):
    OLD: "🟢 Gailliot & Baumeister 2007: glucose consumption during PFC tasks."
    NEW: "🟢 Kurzban 2013: PFC = shared hardware → allocation competition."
         "🟢 Musslick & Cohen 2021: shared representations → serial bottleneck."

  §12 Honest Assessment (line 1004):
    REMOVE: "Self-control metabolic cost: Gailliot & Baumeister 2007"
    ADD: "PFC processing constraints: Musslick & Cohen 2021, Kurzban 2013"
         "Catecholamine modulation: Arnsten 2009, Westbrook & Braver 2016"

  §14 Citation Table:
    R8: Gailliot → CHANGE tag to ❌ or REMOVE from 🟢 list
    ADD: R-new citations (Kurzban, Musslick, Westbrook, Shenhav)
    R13 Arnsten 2009: expand "Used in" column to include §2, §4, §9

  YAML header: version 1.2 → 1.3, update note
```

### Phase 2: Source-of-Truth File (Inter-Body-Mechanism.md)

```
FILE: Inter-Body-Mechanism.md v2.0 → v2.1

CHANGES:
  §4.2 (lines 559-583):
    OLD: "SOURCE: PFC chain novel paths → glucose + neurotransmitters consumed"
         "🟢 Cognitive effort = metabolic cost (Gailliot & Baumeister 2007)."
    NEW: "SOURCE: PFC chain novel paths → processing load (serial bottleneck + catecholamine demand)"
         "🟢 Kurzban 2013: opportunity cost model of cognitive effort."
         "🟢 Arnsten 2009: sustained PFC firing requires DA/NE → depletable."
         "🟢 Musslick & Cohen 2021: shared representations → serial processing constraint."
```

### Phase 3: PFC Folder Files

```
3A. Logic-Feeling.md v2.1 → v2.2
  §3.4 (line 614): "glucose, neurotransmitters" → "processing load"
  Lines 632, 720: Gailliot citation → Kurzban/Arnsten citations
  ~4 edits

3B. Logic-Feeling-Balance.md v3.0 → v3.1
  Line 238: "metabolic (glucose, neurotransmitters)" → "processing load"
  Line 1397: Gailliot → Kurzban/Arnsten
  ~2 edits

3C. PFC-Label.md → minor update
  §5 (line 378): "Metabolic cost từ HOLD" → "Processing load từ HOLD"
  §10 (lines 1024-1026): UPDATE hedge (strengthen — glucose model NOW explicitly falsified)
  Citation table: Gailliot tag update
  ~3 edits

3D. PFC-Development.md → CAREFUL
  §3b METABOLIC CEILING (lines 328-342): KEEP — different claim (evolutionary, Herculano-Houzel)
  Line 338: "highest glucose consumption per neuron" → ADD clarifying note:
    "(evolutionary constraint — distinct from acute ego depletion, which is falsified)"
  Line 577: "Glucose STABLE → PFC stable" → KEEP (nutrition, not ego depletion)
  ~1 edit (clarifying note only)

3E. Imagine-Final.md v3.0 → v3.1
  Line 714: "metabolic — glucose consumption" → "processing load"
  ~1 edit

3F. Simulation-Engine.md — check if needs update
  (likely just cross-ref, minimal)
```

### Phase 4: Observation Folder Files

```
4A. Connection.md v5.0 → v5.1
  Line 1495: "PFC Draft Cost (metabolic)" → "PFC Draft Cost (processing load)"
  Line 2260: "PFC glucose depletion" → "PFC processing load accumulated"
  ~2 edits

4B. Obligation.md
  Lines 520-521: "PFC DRAFT COST (metabolic)" + "glucose consumed"
    → "PFC DRAFT COST (processing load)" + "serial bottleneck occupied"
  ~1 edit

4C. Empathy.md
  Line 1106: "cost > 0 (glucose + neurotransmitter)" → "cost > 0 (processing load)"
  ~1 edit

4D. Threat.md
  Line 615: "COSTS metabolic resources" → "COSTS processing capacity"
  ~1 edit

4E. Status.md
  Lines 160, 1456: "metabolic cost" in Social Baseline context → KEEP (Coan 2015, valid usage)
  ~0 edits

4F. Novelty.md
  Line 356: "metabolic, cortisol, sleep" → "processing load, cortisol, sleep"
  Line 558: hormone/leptin context → KEEP (interoception, not PFC cost)
  ~1 edit

4G. Boredom.md — check if affected
```

### Phase 5: Other Folders

```
5A. Body-Base/Why-Body-Knows.md
  Line 804: "glucose, effort" → "processing load"
  ~1 edit

5B. Neural-Processing-Flow.md
  Line 131: "Metabolic: glucose/ghrelin/leptin" → KEEP (interoception sensing)
  Line 485: "METABOLICALLY expensive" → "processing-intensive" or KEEP (general statement)
  ~0-1 edits

5C. Core-Hardware.md
  Line 229: "⑭ Metabolic — glucose, hydration, ghrelin/leptin" → KEEP (body-base sensing)
  ~0 edits

5D. Core-Software.md
  Line 1148: "PFC runs out of budget" → OK (no glucose reference)
  Line 1150-1154: "PFC BUDGET = FINITE SHARED RESOURCE" → OK (no glucose reference)
  ~0 edits

5E. Domain/Domain-Mapping-Drive.md
  Line 938: "glucose, oxygen" → "processing load"
  ~1 edit

5F. Collective/Coordination-Node.md
  Line 930: "metabolic cost giảm" (Social Baseline) → KEEP (Coan 2015, valid)
  ~0 edits

5G. Plan-Translate/00-Glossary.md
  Lines 165, 168: update "① PFC draft cost" and "PFC budget" definitions
  Line 336: "willpower" mapping → update
  ~3 edits

5H. Quote Analysis files
  Work-Think-Act-Become-Cluster.md: Gailliot citations → update
  Work-Adversity-Fear-Cluster.md: Gailliot citation → update
  Work-Move-Fast-Break-Things.md: ego depletion reference → OK (already neutral)
  ~3-4 edits
```

### Phase 6: Backup Files — NO CHANGE

```
All files in backup/ folders → DO NOT TOUCH.
They represent historical versions.
```

---

## IV. EXECUTION ORDER

```
PHASE 1: PFC-Operations.md (central file — ~8 edits)
  → After Phase 1: VERIFY consistency within PFC-Operations.md
  → §2.1, §4.3, §8.3, §9.1, §12, §14 must ALL be internally consistent

PHASE 2: Inter-Body-Mechanism.md (source-of-truth — ~2 edits)
  → After Phase 2: VERIFY consistency PFC-Ops ↔ Inter-Body

PHASE 3: PFC folder (6 files — ~12 edits)
  → 3A Logic-Feeling → 3B LF-Balance → 3C PFC-Label
  → 3D PFC-Development → 3E Imagine-Final → 3F Simulation-Engine

PHASE 4: Observation folder (6-7 files — ~6 edits)
  → 4A Connection → 4B Obligation → 4C Empathy
  → 4D Threat → 4E Status → 4F Novelty → 4G Boredom

PHASE 5: Other folders (~8 edits)
  → 5A Why-Body-Knows → 5B Neural-Processing-Flow
  → 5D Core-Software → 5E Domain-Mapping-Drive
  → 5G Glossary → 5H Quote Analysis

PHASE 6: VERIFY
  → grep "glucose" — should only remain in:
     (a) PFC-Development (evolutionary constraint)
     (b) Neural-Processing-Flow (interoception)
     (c) Core-Hardware (body-base sensing)
     (d) PFC-Development §4 nutrition
     (e) backup/ files
  → grep "Gailliot" — should only remain in:
     (a) §8.3 ego depletion discussion (with ❌ tag)
     (b) backup/ files
  → grep "metabolic" — should only remain in:
     (a) Evolutionary context (Herculano-Houzel, Raichle)
     (b) Social Baseline (Coan 2015)
     (c) Interoception context
     (d) backup/ files
```

---

## V. WHAT DOES NOT CHANGE

```
FRAMEWORK LOGIC: All predictions unchanged.
  Fresh > Compiled cost: ✓ (processing load replaces glucose, same direction)
  Cost DECREASES with compilation: ✓ (compiled → bypass PFC serial bottleneck)
  Budget SHARED: ✓ (same PFC hardware for all tasks)
  Budget RECHARGES via sleep: ✓ (catecholamine restoration + consolidation)
  "Mệt → Self-Pattern-Modeling yếu": ✓ (allocation competition + catecholamine decline)
  Parent-child = highest cost: ✓ (most complex fresh demand on PFC)
  Cortisol → PFC damage: ✓ (unchanged, McEwen 2007)

② SUPPRESS COST: Unchanged (efference mismatch, not metabolic).
③ UNCERTAINTY COST: Unchanged (cortisol holding, not metabolic).

Only ① PFC draft cost MECHANISM changes.
```

---

## VI. ESTIMATED SCOPE

```
Total files affected: ~20 active files
Total edits: ~35-40
Total lines changed: ~100-150
Risk: LOW (label change, no logic change)
Sessions needed: 1-2
```
