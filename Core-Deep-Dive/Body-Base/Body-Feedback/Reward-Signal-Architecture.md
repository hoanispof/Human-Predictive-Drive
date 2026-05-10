---
title: Reward Signal Architecture — Type A/B + 5 Profiles + Interaction Model
version: 1.0
created: 2026-05-09
status: REFERENCE v1.0
scope: |
  WHAT KINDS of reward signals exist + HOW they interact.
  Type A (Evaluative, opioid) vs Type B (Direct State, non-opioid).
  A₀→A₃ Complexity Gradient. A Gates B mechanism.
  5 Reward Profiles (hương vị reward). Temporal Stack Model.
  Conditional Interaction Model (replaces simple additive).
  Development lifecycle + Individual differences overview.
  5 Forces Holding Model for sustained creative arcs.
purpose: |
  03-Reward.md answers: WHEN reward fires (H10 5 preconditions) + HOW mechanism works (7-step VTA).
  File này answers: WHAT KINDS of reward exist + HOW they interact.
  Complement, not replacement. Different questions → different files.
  Source: Distilled from Drill-Reward-Feeling-Main.md v1.2 (~6,700L, ALL 20 GAPs COMPLETE).
position: |
  Body-Feedback/ folder — ngang hàng với Body-Feedback-Mechanism.md + Gap-Direction.md.
  KHÔNG nằm trong chuỗi P1→P4 (01-Foundation → 02-Dissonance → 03-Reward → 04-Integration).
  Reading order: SAU 03-Reward.md (cần H10 foundation).
dependencies:
  - 03-Reward.md — H10 5 preconditions, 7-step VTA mechanism
  - Body-Feedback-Mechanism.md v1.1 — 2 sources, 3 chunk dynamics, compound
  - Feeling.md v2.0 — feeling = PFC observation of body-feedback
  - Feeling-Mechanism-Deep.md — §4 reward mechanism detail
  - Compile-Taxonomy.md v1.0 — 3 compile types, 4 pathways
  - PFC-Function.md v1.1 — 24 functions, PFC offline cases
  - PFC-Hardware.md v1.0 — COMT, DRD4, MAO-A, NE
  - Cortisol-Baseline.md v2.0 — amplifier, direction > level
  - Dopamine-Reward-Rejection.md v1.0 — dopamine ≠ reward
  - Liking-Wanting.md v1.0 — bridge Berridge, wanting mechanisms
  - Gap-Direction.md v1.0 — gap has direction, 2-layer model
  - Meaning.md v2.0 — life-level Anchor-Schema
  - Connection.md v3.1 — 3 Generative Primitives, L2 smoothing
drill_source: Drill-Reward-Feeling-Main.md v1.2 + Drill-Reward-Feeling-Cases.md v1.0
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Reward Signal Architecture — Type A/B + 5 Profiles + Interaction Model

> **03-Reward.md: KHI NÀO reward fire? (H10 preconditions, 7-step VTA)**
> **File này: reward fire CHẤT LƯỢNG THẾ NÀO? (Types, Profiles, Interaction)**
>
> Ăn ngon → "sướng." Hiểu bài toán → "sướng." Nghe nhạc hay → "sướng."
> Cùng 1 từ. Cùng 1 hệ opioid. Nhưng cảm giác KHÁC NHAU.
>
> Framework nói: Reward = body-base confirm signal (H10, 03-Reward.md).
> File này drill: **"Hương vị" reward đến từ đâu?**
> Và: tại sao cùng hệ thống mà 3 cái "sướng" trên KHÁC NHAU?
>
> **Source**: Distilled từ Drill-Reward-Feeling-Main.md v1.2
> (~6,700L, ALL 20 GAPs COMPLETE, 115+ research sources).

---

## §0 — POSITION + SCOPE + READING GUIDE

### §0.1 — Vị trí trong framework

```
03-Reward.md (P3):
  → WHEN reward fires: H10 5 preconditions (P1-P5)
  → HOW mechanism works: 7-step VTA → opioid pipeline
  → 7 reward cases (C1.1-C1.7)

Reward-Signal-Architecture.md (file này):
  → WHAT KINDS of reward: Type A vs Type B
  → HOW COMPLEX: A₀→A₃ gradient
  → HOW INTERACT: A Gates B, Conditional Interaction
  → WHAT "FLAVORS": 5 Reward Profiles
  → HOW CHANGE: Development lifecycle, Individual differences
  → WHAT SUSTAINS: 5 Forces Holding Model

→ 2 files = COMPLEMENT, không overlap.
→ Đọc 03-Reward TRƯỚC file này.
```

### §0.2 — Cấu trúc file

```
§1-§3:  ARCHITECTURE — Type A/B, A₀→A₃, A Gates B
§4:     PROFILES — 5 "hương vị" reward
§5-§6:  DYNAMICS — Temporal Stack, Conditional Interaction
§7:     STATE DEPENDENCE — 3 types (Cabanac refined)
§8:     DEVELOPMENT — Lifecycle + Individual differences
§9:     EVIDENCE — Key research data + naltrexone table
§10:    5 FORCES — Sustained creative arcs
§11:    HONEST ASSESSMENT — Confidence, limitations, predictions
§12:    CROSS-REFERENCES
```

---

## §1 — TYPE A/B: 2 LOẠI BODY-BASE CONFIRM SIGNAL

### §1.1 — Core distinction

```
🟡 REWARD SIGNAL CÓ 2 LOẠI — ORTHOGONAL DIMENSION:

  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  TYPE A — EVALUATIVE CONFIRM                                     │
  │                                                                  │
  │  Circuit: Hedonic hotspot (NAcc shell, VP, mOFC)                │
  │  Primary signal: μ-opioid                                       │
  │  Amplifier: Endocannabinoid (dependent on opioid — Stacey 2018) │
  │  H10: Full 5 preconditions required                             │
  │  Requires: Compiled chunks (P2) + body-need gap (P1)           │
  │  Learned: YES — quality depends on chunk library                │
  │  Modulated by: Alliesthesia (body state changes evaluation)     │
  │  Examples: Food, music, insight, visual beauty, social praise   │
  │  Mechanism: Input → EVALUATE vs body-need → confirm/reject      │
  │                                                                  │
  ├──────────────────────────────────────────────────────────────────┤
  │                                                                  │
  │  TYPE B — DIRECT STATE CONFIRM                                   │
  │                                                                  │
  │  Circuit: Interoceptive / body-state regulation (VARIES)        │
  │  Primary signal: VARIES by modality:                             │
  │    Touch: CT afferents → posterior insula (🟢 Löken 2009)       │
  │    Exercise: Endocannabinoid CB1 (🟢 Fuss 2015 PNAS)           │
  │    Temperature: thermoreceptor → hypothalamus                    │
  │  H10: Simplified (P1 basic, P2-P5 reduced/N/A)                 │
  │  Requires: Hardware pathways (minimal compiled chunks)          │
  │  Learned: MINIMAL — hardware from birth                         │
  │  Modulated by: Less — sensor-level adaptation only              │
  │  Examples: Touch comfort, runner's high, warmth, stretching     │
  │  Mechanism: Body activity → state DIRECTLY improves → signal    │
  │                                                                  │
  └──────────────────────────────────────────────────────────────────┘

  COMMON ELEMENT (framework level):
  "Reward = body-base confirm signal" — cả A VÀ B.
  Framework ĐÚNG ở abstraction level. A/B = mechanism detail bên dưới.

  Source: Drill §3.5, §3.7 (R1+R13).
  🟢 Berridge & Robinson 1998, 2003. 🟢 Loseth 2019. 🟢 Fuss 2015.
```

### §1.2 — Tại sao A/B ORTHOGONAL (không phải 6th profile)

```
🟡 3 KHẢ NĂNG ĐÃ CÂN NHẮC — CHỈ (b) ĐÚNG:

  (a) Thêm Profile ⑥ "Homeostatic" cho Type B → REJECTED
      Lý do: B CẮT NGANG tất cả profiles, không chỉ ①
  (b) A/B = meta-dimension ORTHOGONAL lên tất cả profiles → ✅ ACCEPTED
  (c) Split Profile ① thành ①a/①b → REJECTED
      Lý do: phải split ③, ④ nữa → redundant

  A/B cắt NGANG mọi profile:
    Profile ① Sensory:  food = A, touch = B
    Profile ③ Social:   praise = A, physical proximity = B
    Profile ④ Relief:   solved problem = A, pain stops = B

  → A/B = ORTHOGONAL DIMENSION × 5 Profiles
  → Mỗi profile có A/B RATIO riêng (xem §4)
  → A/B = spectrum, NOT binary
```

### §1.3 — H10 × Type A/B

```
🟡 H10 PRECONDITIONS — KHÁC NHAU CHO 2 LOẠI:

  ┌──────────────────┬─────────────────┬────────────────┐
  │ Precondition     │ Type A          │ Type B         │
  ├──────────────────┼─────────────────┼────────────────┤
  │ P1 Schema        │ REQUIRED —      │ SIMPLIFIED —   │
  │    pending       │ specific gap    │ body-need      │
  │                  │                 │ always present │
  ├──────────────────┼─────────────────┼────────────────┤
  │ P2 Chunks base   │ REQUIRED —      │ MINIMAL —      │
  │                  │ compiled for    │ hardware paths │
  │                  │ evaluation      │ from birth     │
  ├──────────────────┼─────────────────┼────────────────┤
  │ P3 VTA delta     │ REQUIRED —      │ UNCERTAIN —    │
  │                  │ novelty/change  │ may bypass VTA │
  │                  │                 │ (posterior     │
  │                  │                 │  insula path)  │
  ├──────────────────┼─────────────────┼────────────────┤
  │ P4 Goldilocks    │ REQUIRED —      │ HARDWARE —     │
  │                  │ ~40-70% match   │ CT ~1-10cm/s   │
  │                  │                 │ = fixed range  │
  ├──────────────────┼─────────────────┼────────────────┤
  │ P5 Chunk tag     │ REQUIRED —      │ N/A —          │
  │                  │ opioid/cortisol │ hardware, no   │
  │                  │ tag direction   │ tag needed     │
  └──────────────────┴─────────────────┴────────────────┘

  → Type B KHÔNG bị block bởi P2, P3, P5 failures
  → Type B = RELIABLE, ALWAYS-AVAILABLE baseline reward
  → Type A = RICH, VARIABLE, but CONDITIONAL on P1-P5
  → Loss of A (burnout, anhedonia) → B remains ("touch still good")
  → Loss of B (neuropathy) → A remains ("can still enjoy music")
  → Loss of BOTH → severe anhedonia (rare, devastating)

  Source: Drill §3.7.
```

### §1.4 — Type B = "Safe Baseline Reward" (Evolutionary Floor)

```
🟡 B = EVOLUTIONARY FLOOR:

  Type B KHÔNG bị ảnh hưởng bởi:
  → P2 failure (chưa compile) — infant CAN experience
  → P5 cortisol tag — KHÔNG associated với threat
  → VTA habituation — B bypass VTA (🔴 prediction, §5)

  → B = reward CỔ HƠN Type A:
    Touch comfort: mọi sinh vật có da → benefit từ contact
    Exercise: body movement → homeostatic regulation
    → KHÔNG CẦN circuit đánh giá phức tạp
    → Type A evolved SAU, CHO đánh giá phức tạp hơn
    → "Cái này ăn được không? Dinh dưỡng? Độc?"

  → Trẻ sơ sinh: Type B đã có NGAY (touch, warmth)
  → Type A: develops with chunk compilation

  Therapeutic implication:
  → Burnout/anhedonia: Type A rewards exhausted
  → Type B VẪN accessible vì hardware-based
  → Body-oriented therapy = deliberately activate B pathways
  → B = "backdoor" qua stuck A gate (dissociation)
  → 🟢 Van der Kolk 2014: body-oriented approaches for trauma

  Source: Drill §3.5, §3.7, §3.11.
```

### §1.5 — Neurochemical Multi-Role Principle

```
🟡 FUNCTION = f(CIRCUIT × CONTEXT) — NOT f(MOLECULE ALONE):

  Cùng molecule, KHÁC circuit, KHÁC function:

  ┌─────────────────┬──────────────────────────────────────────────┐
  │ Neurochemical   │ Multiple Roles                                │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ Dopamine        │ Salience (VTA) / Motor (striatum) /          │
  │                 │ Working Memory (PFC)                          │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ Opioid          │ Pain modulation (original) /                  │
  │                 │ Hedonic evaluation (recruited) /              │
  │                 │ Social bonding (extended)                     │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ Endocannabinoid │ Body-state regulation (original, Type B) /   │
  │                 │ Hedonic amplifier (recruited into Type A) /   │
  │                 │ Stress modulation (amygdala CB1)              │
  └─────────────────┴──────────────────────────────────────────────┘

  🟢 Anderson 2010: Neural Reuse — old systems get RECRUITED into new circuits.
  🟢 Stacey 2018: eCB in NAcc hotspot DEPENDS on opioid (Type A amplifier).
  🟢 Fuss 2015: eCB in exercise INDEPENDENT of opioid (Type B primary).

  Framework ĐÚNG khi abstract trên hormone level.
  "Reward = body-base confirm signal" — hormone = implementation detail.

  Source: Drill §3.6.
```

### §1.6 — A/B × BFM 2-Source Mapping

```
🟡 TYPE A/B × SENSORY-DRIVEN / PATTERN-DRIVEN:

  ┌──────────────────┬──────────────────┬──────────────────┐
  │ BFM Source       │ Type A possible? │ Type B possible? │
  ├──────────────────┼──────────────────┼──────────────────┤
  │ Sensory-Driven   │ ✅ YES           │ ✅ YES           │
  │ (domain → body)  │ Food, music,     │ Touch, warmth,   │
  │                  │ visual beauty    │ exercise         │
  ├──────────────────┼──────────────────┼──────────────────┤
  │ Pattern-Driven   │ ✅ YES           │ ⚠️ VERY LIMITED  │
  │ (chunks → body)  │ Insight, preview,│ Preview of B     │
  │                  │ comparison       │ = LOW fidelity   │
  └──────────────────┴──────────────────┴──────────────────┘

  → Type B ≈ ALWAYS Sensory-Driven (requires actual hardware activation)
  → Type A = Sensory-Driven OR Pattern-Driven (evaluation either way)
  → Type B = "hardware-bound reward" (needs actual body-state change)
  → Type A = "evaluation-bound reward" (any input source)

  Source: Drill §3.7. Cross-ref: Body-Feedback-Mechanism.md §2.
```

---

## §2 — TYPE A COMPLEXITY GRADIENT: A₀→A₃

### §2.1 — Core finding: A is NOT monolithic

```
⭐ TYPE A CÓ SPECTRUM OF EVALUATION COMPLEXITY:

  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │  A₀ — HARDWARE-INSTALLED EVALUATION (simplest):                 │
  │    Mechanism: Taste receptor → brainstem → opioid                │
  │    Chunks needed: NONE — evolution PRE-COMPILED                  │
  │    Evaluation: BINARY (sweet → "caloric" → opioid)              │
  │    From birth: YES                                               │
  │    Examples: Sweet taste, bitter aversion, (possibly umami 🔴)   │
  │    Naltrexone: BLOCKS ✅                                         │
  │    = "Evolution đã compile sẵn evaluation đơn giản nhất"         │
  │                                                                  │
  │  A₁ — BASIC COMPILED EVALUATION:                                │
  │    Mechanism: Sensory → compiled chunks → hedonic hotspot        │
  │    Chunks needed: SOME (learned food preferences, 2-6 yrs)       │
  │    Evaluation: MULTI-FACTOR (taste + texture + memory + social)   │
  │    From birth: NO — develops with chunk compilation               │
  │    Examples: Learned food preferences, familiar music             │
  │    = "Food pickiness ở trẻ 3 tuổi"                               │
  │                                                                  │
  │  A₂ — COMPLEX COMPILED EVALUATION:                              │
  │    Mechanism: Rich pattern matching → multi-chunk → opioid       │
  │    Chunks needed: RICH library (years of exposure)               │
  │    Evaluation: RICH (pattern matching + emotional history)        │
  │    Examples: Music appreciation, aesthetic judgment, wine tasting │
  │    = "Phân biệt Beethoven hay hơn background music"              │
  │                                                                  │
  │  A₃ — DEEP COMPILED EVALUATION:                                 │
  │    Mechanism: Abstract schema fit → coherence → opioid           │
  │    Chunks needed: EXPERT-LEVEL (years/decades)                   │
  │    Evaluation: ABSTRACT (schema fit + coherence + elegance)      │
  │    Examples: Mathematical beauty, expert insight, scientific fit  │
  │    = "Einstein thấy equations fit → heart palpitations"           │
  │                                                                  │
  └──────────────────────────────────────────────────────────────────┘

  🟢 Steiner 1973, 1979: Gustofacial reflexes — neonates distinct responses.
  🟢 Blass & Hoffmeyer 1991: Sucrose calming neonates.
  🟢 Blass & Ciaramitaro 1994: Naltrexone REDUCES sucrose calming → opioid.
  🟢 Berridge 2003: Decorticated rats STILL show hedonic reactions → subcortical.
  🟢 Anencephalic infants STILL show gustofacial responses → definitively subcortical.

  Source: Drill §3.10 (R19).
```

### §2.2 — Tại sao A₀ VẪN là Type A (không phải Type B)

```
🟡 A₀ CROSS-CUTS A/B BINARY — nhưng VẪN LÀ TYPE A:

  ┌──────────────────┬──────────────┬──────────────┬──────────────────┐
  │ Đặc tính         │ Type A       │ Type B       │ Neonate Sweet    │
  ├──────────────────┼──────────────┼──────────────┼──────────────────┤
  │ Neurochemical    │ Opioid       │ Non-opioid   │ OPIOID ✅A       │
  │ Learning req.    │ Compiled     │ Hardware     │ HARDWARE ✅B      │
  │ PFC needed?      │ Yes          │ No           │ NO ✅B            │
  │ Naltrexone       │ Blocks       │ No effect    │ BLOCKS ✅A        │
  │ From birth?      │ No           │ Yes          │ YES ✅B           │
  │ Evaluation?      │ Yes (complex)│ None         │ YES (binary) ✅A  │
  └──────────────────┴──────────────┴──────────────┴──────────────────┘

  Resolution: A₀ VẪN Type A vì:
  ① Opioid pathway: CÙNG pathway với adult food/music reward.
  ② Evaluation EXISTS — dù binary. Type B = NO evaluation at all.
  ③ Contrast: Touch (B) = CT → state change, no matching.
     Sweet (A₀) = taste receptor → template match → opioid.
     → Qualitatively DIFFERENT pathways.

  A₀ = EVOLUTIONARY SHORTCUT:
  → Infant CŨNG needs to EVALUATE food — LIFE OR DEATH
  → CANNOT wait for compiled chunks — infant starves/poisons
  → Solution: PRE-INSTALL binary evaluation for taste
  → Sweet → opioid → approach → survive
  → Bitter → aversion → reject → survive

  Source: Drill §3.10 (R19).
```

### §2.3 — Development: layers BUILD on A₀ foundation

```
🟡 A₀→A₃ = LAYERS — STACKING, NOT REPLACING:

  ┌──────────────────────────────────────────────────────────────┐
  │  Birth:   A₀ only (sweet/bitter binary)                      │
  │     ↓                                                        │
  │  1-2yr:   A₀ + A₁ emerging (food preferences compile)       │
  │     ↓                                                        │
  │  5-10yr:  A₀ + A₁ + A₂ emerging (music, aesthetics)         │
  │     ↓                                                        │
  │  Expert:  A₀ + A₁ + A₂ + A₃ (abstract beauty, coherence)    │
  │                                                              │
  │  B = parallel track, independent, ALWAYS present             │
  │  A₀ = foundation, NEVER lost, layers BUILD on top            │
  └──────────────────────────────────────────────────────────────┘

  → Adult still likes sweet = A₀ + compiled layers on top
  → Expert wine tasting = A₀ + A₁ + A₂ (STACKING)
  → A₀ = FOUNDATION. A₁-A₃ = LAYERS built on foundation.
  → Each layer ADDS evaluation complexity, opioid pathway shared.
  → B = SEPARATE system. Non-opioid. No evaluation at all.

  Source: Drill §3.10 (R19).
```

---

## §3 — A GATES B: EVALUATION MODULATES HARDWARE SIGNAL

### §3.1 — NOT single locus — INSULA GRADIENT PROCESS

```
⭐ A GATES B = POSTERIOR-TO-ANTERIOR INSULA GRADIENT:

  🟢 Craig 2002, 2013: posterior insula → mid-insula → anterior insula
  = progressively context-enriched interoceptive representation.
  Framework's A Gates B = EXACTLY this gradient.


  5-STEP NEURAL PROCESS:

  STEP 1 — POSTERIOR INSULA: B arrives (~0-50ms)
    → CT afferents → lamina I → posterior insula
    → RAW, UNMODULATED first-order representation
    → SAME signal regardless of WHO touches
    → 🟢 Craig 2002: posterior insula = primary interoceptive cortex

  STEP 2 — A EVALUATION fires in parallel (~50-200ms)
    → Context chunks activate: WHO/WHAT/WHERE
    → Social schemas: friend? stranger? threat?
    → Amygdala: rapid threat assessment (LeDoux fast path)

  STEP 3 — ANTERIOR INSULA: B + A INTEGRATE (~100-300ms)
    → B signal PROPAGATES anteriorly
    → A context signal arrives TOP-DOWN
    → Anterior insula: INTEGRATES both = EXPERIENCED SIGNAL
    → 🟢 Craig 2009: anterior insula = "seat of subjective awareness"

  STEP 4 — ACC: CONFLICT CHECK (~200-400ms)
    → ACC monitors: B and A AGREE or CONFLICT?
    → B positive + A positive → silent (smooth)
    → B positive + A negative → FIRES (flags attention)
    → 🟢 Botvinick et al. 2004: ACC conflict monitoring

  STEP 5 — OFC/vmPFC: VALUE ASSIGNMENT (~300-500ms)
    → Final value computation
    → Integrates: insula output + ACC flag + PFC evaluation
    → 🟢 Damasio 1994: vmPFC somatic marker


  FLOW:

  B signal → posterior insula (raw)
              → mid-insula (context begins)
                 → anterior insula (B + A = EXPERIENCE)
                    → ACC (conflict?) + OFC/vmPFC (value)

  Source: Drill §3.13 (R18).
```

### §3.2 — 4 Modulation Outcomes

```
🟡 A EVALUATION → 4 POSSIBLE EFFECTS ON B SIGNAL:

  ┌──────────────────────┬──────────────────────────────────┐
  │ A Evaluation Result  │ Effect on B Signal               │
  ├──────────────────────┼──────────────────────────────────┤
  │ A positive           │ AMPLIFY B → compound pleasant    │
  │ (trusted person)     │ B + A = more than either alone   │
  ├──────────────────────┼──────────────────────────────────┤
  │ A negative           │ SUPPRESS/OVERRIDE B              │
  │ (stranger, threat)   │ Net unpleasant despite B positive│
  ├──────────────────────┼──────────────────────────────────┤
  │ A absent             │ B RAW (unmodulated)              │
  │ (infant, dissociation│ Basic pleasant from hardware     │
  │  PFC offline)        │ = "pure Type B experience"       │
  ├──────────────────────┼──────────────────────────────────┤
  │ A conflicted         │ AMBIGUOUS signal                 │
  │ (attracted stranger) │ Arousal + caution = mixed        │
  │                      │ ACC fires strongly (conflict)    │
  └──────────────────────┴──────────────────────────────────┘

  Evolutionary logic:
  → Pure B = dangerous (snake touch = CT pleasant but DANGER)
  → A GATE evolved to provide CONTEXT for B signals
  → = Safety filter ON TOP OF hardware pleasure

  Infant design:
  → A gate NOT YET FORMED → B dominant → all touch accepted
  → = "Trust the world first, learn to evaluate later"
  → A gate develops GRADUALLY with chunk compilation

  Source: Drill §3.7, §3.13 (R18).
```

### §3.3 — Insula Gradient × Development

```
🟡 INSULA MATURATION = A GATE FORMATION:

  Neonate: posterior functional, anterior IMMATURE
    → B propagates unmodulated → all touch accepted
    → A gate NOT YET FORMED

  ~8 months: anterior DEVELOPING → stranger anxiety emerges
    → A gate FORMING → stranger touch → suppress begins
    → ≈ Anterior insula maturation marker

  Adult: anterior fully FUNCTIONAL → full A Gates B
    → Touch experience highly context-dependent

  Elderly (cognitive decline): anterior may SIMPLIFY
    → A gate LOOSENS → touch more valued in simpler way
    → = "Bà chỉ cần nắm tay" = B re-emerging

  → Insula maturation curve MIRRORS A/B development gradient (§8.1)
  → NOT coincidence — insula gradient IS the A gate mechanism

  ⚠️ FRAMEWORK SCOPE BOUNDARY:
  Mechanism at CONCEPT level: "A evaluation modulates B hardware signal."
  Neural mapping: "via posterior-to-anterior insula gradient."
  Framework NOTES mapping for verification anchors.
  Framework does NOT commit to sub-region claims as FRAMEWORK claims.

  Source: Drill §3.13 (R18).
```

### §3.4 — 6 Edge Cases: A/B Boundary

```
🟡 6 EDGE CASES — TYPE A/B THỰC TẾ LÀ SPECTRUM:

  ① SPICY FOOD: B INPUT (pain) → A REWARD (compensatory endorphin)
     → Input pathway ≠ Reward pathway
     → "Acquired taste" = compile transforms B input → A reward

  ② SOCIAL TOUCH: B component (CT afferents) + A component (social eval)
     → Friend: A amplifies B → compound pleasant
     → Stranger: A overrides B → unpleasant despite CT
     → Infant: A minimal → B raw → basic comfort (design feature)
     → Dissociation: A suppressed → B may get through → "backdoor"

  ③ MUSIC + MOVEMENT: A (music evaluation) + B (body rhythm) + ③ Social
     → Dancing = A + B + Social = compound across 3+ channels
     → Cultural universality: mọi nền văn hóa có dance

  ④ MASSAGE: B (CT) + A (technique evaluation) + ④ Relief
     → Bad massage: A negative → override B → unpleasant

  ⑤ SEXUAL PLEASURE: B (physical) + A (attractiveness eval)
     + ③ Social (bonding) + ④ Relief (tension release)
     → Có thể là reward COMPOUND NHẤT trong repertoire

  ⑥ ASMR: A GATE decides WHETHER B-like response fires
     → NOT everyone experiences → genetic variation

  5 INSIGHTS:
  1. A/B = orthogonal DIMENSIONS, not binary (most rewards = compound)
  2. Input pathway ≠ Reward pathway (spicy: B input → A reward)
  3. A GATES B — evaluation CAN amplify OR suppress hardware
  4. A/B ratio SHIFTS across development (§8.1)
  5. "Modulation gradient" — B not modulated, A fully modulated, mixed varies

  Source: Drill §3.7 (R13 edge cases).
```

---

## §4 — 5 REWARD PROFILES: "HƯƠNG VỊ" REWARD

### §4.1 — Neuroscience foundation

```
🟢 CÙNG HỆ THỐNG, KHÁC "HƯƠNG VỊ":

  Tik, Soreq, Kounios et al. 2020 (NeuroImage):
    → Insight activates CÙNG NAcc/VTA/dopaminergic circuitry
      như food, sex, drugs
    → = CÙNG reward hardware

  Kounios & Beeman 2009:
    → Aha moment: gamma burst ở right aSTG (unique cho insight)
    → ~100ms sau: reward signal ở orbitofrontal cortex
    → NHƯNG chỉ ở participants with HIGH reward sensitivity

  Ultra-high-field fMRI 2018:
    → "Aha!" = qualitatively DISTINCT from pride/satisfaction

  → CONVERGENCE:
    Cùng NAcc/VTA (hardware) + khác activation pattern (context)
    = Cùng opioid + khác concurrent body signals
    = Cùng "ngọt" + khác "hương vị"

  Source: Drill §2.1.
```

### §4.2 — 5 Reward Profiles

```
🟡 5 PROFILES = Opioid (common) + Context Signals (source-specific):

  ┌────────────────────────┬──────────────────────────────────────────────┐
  │ Profile                │ Components                                   │
  ├────────────────────────┼──────────────────────────────────────────────┤
  │                        │                                              │
  │ ① SENSORY REWARD       │ Opioid + specific receptor pathway           │
  │   (ăn ngon, mùi hương, │ Body LOCATION rõ (miệng, mũi, da, tai)     │
  │    nhạc hay, tranh đẹp)│ Duration: WHILE experiencing                │
  │                        │ Replay fidelity: ~20-60% (§5.3)            │
  │                        │ Input: Sensory-Driven (BFM §2.2)           │
  │                        │ Motor: SAVORING — slow, enjoy, linger       │
  │                        │                                              │
  ├────────────────────────┼──────────────────────────────────────────────┤
  │                        │                                              │
  │ ② COHERENCE REWARD     │ Opioid + ACC coherence resolve              │
  │   (insight, eureka,    │   + right aSTG (unique, 🟢 Kounios 2009)   │
  │    "hiểu rồi!", beauty)│ Body LOCATION mơ hồ ("ngực", "đầu")        │
  │                        │ Duration: BURST then GLOW (§5.4)           │
  │                        │ Unique behavior: compulsive recheck         │
  │                        │ Poincaré Equivalence: math=art=music beauty │
  │                        │   (🟢 Zeki 2014: mOFC convergence)          │
  │                        │ Motor urgency = 3-component compound:       │
  │                        │   fragility + arousal + verification (§4.4) │
  │                        │ Input: Pattern-Driven (BFM §2.3 ⓓ gap fill)│
  │                        │                                              │
  ├────────────────────────┼──────────────────────────────────────────────┤
  │                        │                                              │
  │ ③ SOCIAL REWARD        │ Opioid + mirror signals + status update      │
  │   (khen, connection,   │ Body: chest warmth, oxytocin contribution   │
  │    approval, belonging)│ Duration: DURING + AFTERGLOW                │
  │                        │ Input: Sensory-Driven (agent input)         │
  │                        │   + Pattern-Driven (schema match)           │
  │                        │ Connection.md: L1 SPM-owned momentary       │
  │                        │                                              │
  ├────────────────────────┼──────────────────────────────────────────────┤
  │                        │                                              │
  │ ④ RELIEF REWARD        │ Cortisol DROP dominant (NOT opioid-led)      │
  │   (threat resolved,    │ Body: muscle relax, breathing ease,         │
  │    "xong rồi",        │   shoulder drop                              │
  │    "thoát rồi")       │ Duration: IMMEDIATE then FADE               │
  │                        │ ≠ pleasure — = ABSENCE of pain/threat       │
  │                        │ Eureka compounds: ② + ④ = double reward     │
  │                        │ Cross-ref: Cortisol-Baseline.md             │
  │                        │                                              │
  ├────────────────────────┼──────────────────────────────────────────────┤
  │                        │                                              │
  │ ⑤ PREVIEW REWARD       │ Opioid REDUCED (fidelity follows A₀→A₃)     │
  │   (tưởng tượng, nhớ   │ = Replay/preview of ①②③④                    │
  │    lại, anticipation)  │ Same quality, lower intensity                │
  │                        │ BFM §2.3: ⓐ REPLAY + ⓑ PREVIEW             │
  │                        │ Cần compiled chunks (prerequisite)           │
  │                        │                                              │
  └────────────────────────┴──────────────────────────────────────────────┘

  ⚠️ PROFILES KHÔNG LOẠI TRỪ — có thể COMPOUND:
    Eureka sau struggle: ② coherence + ④ relief = DOUBLE
    Ăn cùng bạn bè: ① sensory + ③ social = COMPOUND
    Được khen vì giải bài: ② coherence + ③ social = COMPOUND
    Tưởng tượng ăn ngon: ⑤ preview OF ① sensory
    → Compound = NORM, not exception (chi tiết §6)

  Source: Drill §2.2, §7.3 (R4).
```

### §4.3 — Profiles × A/B Ratio

```
🟡 MỖI PROFILE CÓ A/B RATIO RIÊNG:

  ┌────────────────┬───────────────┬──────────────┬────────────────────┐
  │ Profile        │ Type A        │ Type B       │ Typical Ratio      │
  │                │ (evaluative)  │ (direct)     │                    │
  ├────────────────┼───────────────┼──────────────┼────────────────────┤
  │ ① SENSORY      │ Food, music,  │ Touch, warmth│ VARIES by modality │
  │                │ visual beauty │ stretching   │ Food: ~80A/20B     │
  │                │               │              │ Touch: ~20A/80B    │
  │                │               │              │ Music: ~90A/10B    │
  ├────────────────┼───────────────┼──────────────┼────────────────────┤
  │ ② COHERENCE    │ Insight,      │ (minimal)    │ ~95A/5B            │
  │                │ eureka, math  │ body relief  │                    │
  │                │ beauty        │ component    │                    │
  ├────────────────┼───────────────┼──────────────┼────────────────────┤
  │ ③ SOCIAL       │ Praise eval,  │ Physical     │ Online praise:     │
  │                │ status, belong│ proximity,   │   ~90A/10B         │
  │                │               │ co-regulation│ Mother hug:        │
  │                │               │              │   ~40A/60B         │
  ├────────────────┼───────────────┼──────────────┼────────────────────┤
  │ ④ RELIEF       │ Evaluated     │ Physical     │ Problem solved:    │
  │                │ relief (solved│ relief       │   ~70A/30B         │
  │                │ problem)      │ (pain stops) │ Pain stops:        │
  │                │               │              │   ~20A/80B         │
  ├────────────────┼───────────────┼──────────────┼────────────────────┤
  │ ⑤ PREVIEW      │ Preview of A  │ Preview of B │ Inherits source    │
  │                │ (high fidelity│ (LOW fidelity│ B preview fidelity │
  │                │  ~40-60%)     │  ~10-30% 🔴) │ DROPS sharply      │
  └────────────────┴───────────────┴──────────────┴────────────────────┘

  ⚠️ Ratios = approximate illustration, NOT precise measurement.
  Real brain = continuous spectrum, not discrete percentages.

  Source: Drill §3.7 (R1+R13).
```

### §4.4 — Motor Urgency: Profile ② Specific Marker

```
🟡 MOTOR URGENCY = COMPOUND 3 COMPONENTS (exclusively Profile ②):

  ❶ FRAGILITY URGENCY: insight = new pattern, chưa compiled
     → Working memory ~4 items (🟢 Cowan 2001) → interruption = LOST
     → Motor response: EXTERNALIZE content (Hamilton carved on bridge)

  ❷ AROUSAL OVERFLOW: extreme dopamine + opioid + relief
     → Body CAN'T be still (Heisenberg climbed rock at dawn)
     → Content-general (jumping, pacing)

  ❸ VERIFICATION URGENCY: "is the pattern ACTUALLY coherent?"
     → Coherence CAN be wrong (false insight exists)
     → Wiles: "kept coming back to desk to see if it was still there"

  3 components fire SIMULTANEOUSLY → PFC observes as 1 "urgency" feeling.

  SAVORING vs URGENCY:
  → Type B rewards: NO motor urgency (touch → relax, melt into it)
  → Type A sensory (①): LOW urgency (stimulus external + persistent)
  → Type A coherence (②): HIGH urgency (internal + transient + CAN be wrong)
  → = Motor urgency = EXCLUSIVELY Type A + Pattern-Driven + Coherence
  → = Profile ② SPECIFIC behavioral marker

  FLOW vs EUREKA:
  → Eureka: 1 massive insight → HIGH urgency (Hamilton, Archimedes)
  → Flow: many small insights → SUSTAINED mild engagement (not urgency)
  → = 2 modes of SAME ② reward, different temporal profile

  Source: Drill §7.3 (R4).
```

### §4.5 — Poincaré Equivalence: Beauty = H10 P4

```
🟢🟡 BEAUTY = THE FEELING OF GOLDILOCKS-LEVEL PATTERN COHERENCE:

  🟢 Zeki, Romaya, Benincasa & Atiyah 2014:
    → Beautiful math equations → medial OFC area A1 ACTIVATED
    → SAME mOFC region also activates for:
      Visual beauty (🟢 Ishizu & Zeki 2011)
      Musical beauty (🟢 Blood & Zatorre 2001)
      Facial beauty (🟢 O'Doherty et al. 2003)

  Framework: beauty = H10 P4 operating on ANY domain's chunks.
  NOT a separate aesthetic faculty.

  3 simultaneous conditions:
    ① Sufficient COMPLEXITY (P4 floor): 1+1=2 → no beauty (trivial)
    ② Sufficient SURPRISE (P3 delta): known proof 100th time → no beauty
    ③ Sufficient COHERENCE (P4 ceiling): random → no beauty

  Beauty = OPTIMAL coherence-to-complexity ratio = Goldilocks for patterns.

  P2 = BEAUTY GATE:
    No chunks in domain → P4 CANNOT fire → no beauty experience.
    → Visual beauty: MOST ACCESSIBLE (hardware-aided P2)
    → Math beauty: LEAST ACCESSIBLE (expert A₃ chunks required)
    → = "Tại sao không phải ai cũng thấy toán đẹp"
      = P2 gate highest for math, not lack of aesthetic sense

  ② cross-domain priming (Einstein's music mechanism):
    → Music ② active → ACC coherence detection WARM
    → Physics chunks also activate (background P1)
    → Already-warm ACC detects coherence MORE EASILY
    → = "Music is the driving force behind intuition" — ② pathway warmed

  Source: Drill §3.19 (R3). Cross-ref: PFC-Hardware.md (COMT/DRD4 for ②).
```

### §4.6 — Temporal Profile mỗi Profile khác nhau

```
🟡 TEMPORAL PROFILE = THÊM 1 CHIỀU PHÂN BIỆT:

  ① SENSORY:   ─────████████─────  (during stimulus)
  ② COHERENCE: ─────██▓▓▒▒░░────  (burst → glow → fade)
  ③ SOCIAL:    ─────████▓▓▒▒░░──  (during + afterglow)
  ④ RELIEF:    ─────████▒░───────  (immediate → fast fade)
  ⑤ PREVIEW:   ─────▓▓▒▒░░──────  (reduced version of source)

  ████ = peak intensity
  ▓▓   = strong afterglow
  ▒▒   = moderate fade
  ░░   = trace
  ──   = baseline

  → Chi tiết temporal dynamics: §5

  Source: Drill §2.3.
```

---

## §5 — TEMPORAL STACK MODEL

### §5.1 — Onset latency follows A₀→A₃ gradient

```
🟡 ONSET = f(EVALUATION COMPLEXITY):

  ┌──────────────────┬─────────────┬──────────────────────────────────┐
  │ Type             │ Onset       │ WHY                              │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ B (hardware)     │ ~20-100ms   │ Peripheral → posterior insula.   │
  │                  │             │ NO evaluation. Shortest path.    │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₀ (hw-installed)│ ~100-300ms  │ Taste receptor → brainstem →     │
  │                  │             │ opioid. Pre-compiled binary eval.│
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₁ (basic comp.) │ ~200ms-1s   │ Sensory → compiled chunks →     │
  │                  │             │ simple matching → opioid.        │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₂ (complex comp)│ ~500ms-2s   │ Multi-chunk evaluation.         │
  │                  │             │ Context-dependent matching.       │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₃ (deep comp.)  │ ~1-5s       │ Abstract schema fit. ACC         │
  │                  │             │ coherence → opioid pipeline.     │
  └──────────────────┴─────────────┴──────────────────────────────────┘

  ⚠️ Timing ranges = ESTIMATES from processing depth, not measured.
  GRADIENT direction = strong framework prediction.

  KEY: "First feel" of any experience = B or A₀.
  A₁-A₃ layers arrive LATER → experience BUILDS over time.
  → Ăn chocolate: vị ngọt (A₀ ~100ms) → "ngon" (A₁ ~500ms)
    → "ngon như lần ở Paris" (A₃ compare, ~2-5s)
  → Each layer ADDS to subjective richness.

  Source: Drill §3.14 (R5).
```

### §5.2 — Decay: 2 fundamentally different mechanisms

```
🟡 A HABITUATES VIA VTA (central). B VIA RECEPTOR (peripheral):

  TYPE A = VTA HABITUATION:
    → VTA detects prediction delta → habituates → delta → 0
    → 🟢 Schultz 1997: reward prediction error disappears when expected
    → ALL Type A rewards habituate this way — universal mechanism
    → "Boring but still tastes good" = VTA habituated, receptor intact

  TYPE B = RECEPTOR ADAPTATION (modality-specific):
    → B likely bypasses VTA → NOT "baseline-adjusted"
    → Each modality has ITS OWN adaptation curve:

    ┌──────────────────┬─────────────┬──────────────────────────────────┐
    │ B Modality       │ Adaptation  │ WHY                              │
    ├──────────────────┼─────────────┼──────────────────────────────────┤
    │ CT touch         │ SLOW        │ CT DESIGNED for sustained contact│
    │ (dynamic stroke) │ (dynamic)   │ (~1-10 cm/s) 🟢 Löken 2009     │
    ├──────────────────┼─────────────┼──────────────────────────────────┤
    │ CT touch         │ FAST        │ CT responds to MOVEMENT, not     │
    │ (static pressure)│ (static)    │ sustained position               │
    ├──────────────────┼─────────────┼──────────────────────────────────┤
    │ Temperature      │ FAST        │ Thermoreceptor adaptation =      │
    │                  │ (~5-10 min) │ physics (🟢 well-established)    │
    ├──────────────────┼─────────────┼──────────────────────────────────┤
    │ Exercise eCB     │ SLOW        │ Metabolic process, CB1 receptor  │
    │                  │ (weeks/mos) │ desensitization possible but slow│
    └──────────────────┴─────────────┴──────────────────────────────────┘

  → KHÔNG CÓ "B habituation rate" chung
  → "Which B modalities habituate at what rate?" = right question

  HEDONIC TREADMILL (🟢 Brickman & Campbell 1971):
    → = PRIMARILY Type A phenomenon (VTA habituation)
    → Type B = RESISTANT — B = "hedonic FLOOR"
    → "Rich or poor, a hug still feels the same" — B is democratic

  COMFORT OBJECTS:
    B components (PERSIST): CT afferents fire during handling
    A components (habituated but gate intact): "safe" schema → amplifies B
    → "Boring but comforting" = VTA: "nothing new", body: "still good"
    → Spousal touch 20 years: ZERO novelty, STILL comforting

  Source: Drill §3.11 (R20).
```

### §5.3 — Preview fidelity = f(cortical proportion)

```
🟡 PREVIEW FIDELITY FOLLOWS A₀→A₃ GRADIENT:

  Core principle: Preview = cortical SIMULATION.
  Cannot activate PERIPHERAL hardware (receptors, afferents).
  → More cortical pathway = higher preview fidelity.

  ┌──────────────────┬─────────────┬──────────────────────────────────┐
  │ Type             │ Est. Fidelity│ WHY                             │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ B (pure hardware)│ ~5-15%      │ Peripheral only. CT, eCB,       │
  │ Touch, exercise  │             │ thermoreceptors unreachable.     │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₀ (hw-installed)│ ~15-25%     │ Brainstem opioid partially      │
  │ Sweet taste      │             │ simulable via gustatory cortex.  │
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₁ (basic comp.) │ ~25-40%     │ Compiled food/music chunks fire.│
  │ Food preferences │             │ Actual sensory component missing.│
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₂ (complex comp)│ ~40-60%     │ Rich compiled chunks fire.      │
  │ Music, aesthetics│             │ Pattern matching mostly cortical.│
  ├──────────────────┼─────────────┼──────────────────────────────────┤
  │ A₃ (deep comp.)  │ ~60-80%     │ PURELY cortical. Abstract schema│
  │ Math beauty,     │             │ = fully simulable internally.    │
  │ expert coherence │             │ No peripheral component needed.  │
  └──────────────────┴─────────────┴──────────────────────────────────┘

  ⚠️ Percentages = ILLUSTRATIVE, not measured.

  🟢 Kosslyn 1994: visual imagery uses visual cortex (~30% overlap).
  🟢 Jeannerod 1995: motor imagery uses motor cortex.
  🟢 Damasio 1994: somatic marker = body responds to simulation "as if" real.

  "Nhớ vị chocolate RÕ HƠN nhớ cảm giác massage":
  → Chocolate (A₁, ~30-40%) → compiled taste chunks fire
  → Massage (mostly B, ~10-15%) → CT sensation COMPLETELY ABSENT
  → "Nhớ rõ hơn" = higher cortical proportion = more simulable

  WANTING × PREVIEW — CRAVING VULNERABILITY:
  → High preview fidelity → strong wanting → drive to seek (Type A)
  → Low preview fidelity → weak wanting (Type B)
  → Type B resistant to craving (needs actual experience)

  ⚠️ "APPARENT B PREVIEW" CAVEAT:
  → "Remember massage → body relaxes" = NOT B preview
  → = Preview of B CONTEXT through A pathway (schema activation)

  Source: Drill §3.12 (R17).
```

### §5.4 — A₃ Afterglow: 4 overlapping curves

```
🟡 A₃ AFTERGLOW = 4 MECHANISMS WITH DIFFERENT TIMESCALES:

  NOT 1 signal "lasting days" — 4 signals taking turns sustaining:

  CURVE 1 — OPIOID CONSOLIDATION GLOW:
    Gap fill → opioid. Chunks STILL consolidating.
    Each micro-consolidation = mini-opioid pulse.
    Duration: hours → days. 🟢 McGaugh 2000.

  CURVE 2 — RELIEF COMPOUND (cortisol drop gradient):
    Years of pending → cortisol elevated.
    Gap fill → cortisol DROP. But cortisol has INERTIA.
    Duration: days → weeks (proportional to pending duration).

  CURVE 3 — BACKGROUND PROCESSING CASCADE:
    New chunks → network reorganizes → RELATED micro-insights.
    "À, nó CŨNG có nghĩa..." = secondary discoveries.
    Duration: hours → days. 🟢 Collins & Loftus 1975.

  CURVE 4 — VERIFICATION LOOP (R4):
    Each recheck → "vẫn đúng" → ANOTHER opioid pulse.
    Duration: minutes → hours (until compiled as "confirmed").

  ┌──────────────────────────────────────────────────────────────┐
  │  t=0:      ████ opioid burst (curve 1)                       │
  │  t=1min:   ████▓▓▓ + relief (curve 2) + recheck (curve 4)  │
  │  t=1h:     ▓▓▓▓▓▓ consolidation + relief + background      │
  │  t=next day: ▓▓▓ relief + "new implications!" (curves 2+3) │
  │  t=2-3 days: ░░░ relief fading + occasional insight         │
  └──────────────────────────────────────────────────────────────┘

  → A₃ afterglow LONG: ALL 4 mechanisms active.
  → A₀ afterglow SHORT: minimal consolidation, no relief cascade.

  Source: Drill §3.14 (R5).
```

### §5.5 — Temporal Stack: richness = active layers × overlap

```
🟡 TEMPORAL STACK MODEL:

  Any experience = SUM of overlapping temporal profiles.
  "Richness" = number of active layers + overlap quality.

  VÍ DỤ: Ăn cùng bạn bè:

    Time→   0ms    200ms   500ms   1s     5s    30s   5min   1h
            ├──────┼───────┼──────┼──────┼─────┼─────┼──────┤
    B(touch): ░░░░░  (background, very slow decay)
    A₀(taste):      ████████████████████████░░░░
    A₁(food):                ████████████████████████░░░░░░░
    A₂(eval):                        ███████████████████░░░░░░
    ③Social:                                ████████████████████████████
    ④Relief:                                     ████████████████████████
    ⑤Preview:                                                    ▓▓▓▓▓▓▓▓

    Total:   ░      ██      ████    █████ █████ █████  ███   ▓▓
             barely sweet   compound peak  rich  fading glow  memory

  → Compound experiences BUILD: layers arrive at different times
  → Rush (drugs, gambling) = "shallow": 1-2 layers, fast decay
  → Deep compound = "rich": nhiều layers, build dần, decay chậm

  Duration = f(source_type × A/B_type × compound_layers × pending)

  Source: Drill §3.14 (R5).
```

---

## §6 — CONDITIONAL INTERACTION MODEL

### §6.1 — NOT additive — replaces BFM §4 simple model

```
⭐ COMPOUND = NORM, NOT EXCEPTION.
  BFM §4: Signal_total = Σ (dynamics × intensity × network_size).
  REFINED: Interaction type DEPENDS ON 4 variables.
  → CONDITIONAL INTERACTION MODEL.

  Source: Drill §3.15 (R7).
```

### §6.2 — Within-type interaction (same substrate)

```
🟡 A + A (same opioid pathway):
    → Hotspot finite capacity (~1mm³)
      🟢 Peciña & Berridge 2005: hotspot SMALL, specific
    → 2 A signals converge → same receptors → CEILING
    → = SUBADDITIVE — diminishing returns

    Within A level matters:
      A₁ + A₁ (food + music): MOST subadditive (both sensory opioid)
      A₁ + A₃ (food + insight): LESS subadditive (different pathways)

  B + B (different receptors):
    → Touch (CT) + Warmth (thermoreceptors)
    → DIFFERENT peripheral pathways → little competition
    → = NEAR-ADDITIVE

  Source: Drill §3.15 (R7).
```

### §6.3 — Cross-type interaction (A + B) = modulation

```
🟡 A + B = MODULATION, NOT ARITHMETIC:

  This is A GATE MODULATION (§3):
  B signal fires → A evaluation fires → anterior insula integrates.

  ┌──────────────────┬──────────────────────────────────────────┐
  │ A Gate Setting    │ Compound Result                          │
  ├──────────────────┼──────────────────────────────────────────┤
  │ A positive       │ SUPERADDITIVE: A amplifies B             │
  │ (trusted person) │ Compound > A_alone + B_alone             │
  ├──────────────────┼──────────────────────────────────────────┤
  │ A negative       │ SUBTRACTIVE: A suppresses/overrides B    │
  │ (stranger)       │ NEGATIVE despite B positive              │
  ├──────────────────┼──────────────────────────────────────────┤
  │ A absent         │ RAW B: no modulation                     │
  │ (infant, PFC off)│ = "Pure Type B experience"               │
  ├──────────────────┼──────────────────────────────────────────┤
  │ A conflicted     │ NON-LINEAR: qualitatively NEW            │
  │ (attracted       │ Arousal + caution = ambiguous             │
  │  stranger)       │ 🟢 Botvinick 2004: ACC conflict          │
  └──────────────────┴──────────────────────────────────────────┘

  → A controls the GAIN of B, does not add to B.

  Source: Drill §3.15 (R7), §3.7 (R13).
```

### §6.4 — Relief (④) = system-state MULTIPLIER

```
🟡 RELIEF ≠ ADDITIVE SIGNAL — RELIEF = GLOBAL STATE CHANGE:

  Cortisol DROP → 3 simultaneous effects:
    ① Body muscles relax → sensory signals CLEARER
    ② PFC load decreases → perception RICHER
    ③ Opioid system disinhibited → opioid response STRONGER

  Compound_with_relief = base_compound × (1 + relief_factor)

  Relief factor = f(prior_pending_duration × cortisol_drop):
    Short pending (minutes): ~1.2-1.5x
    Medium pending (days): ~1.5-3x
    Long pending (years): ~3-10x

  → Einstein years → "DAYS ecstasy" (large multiplier)
  → Student 5 min → "oh, cool" (small multiplier)
  → Same coherence type (A₃). VASTLY different magnitude.

  "Comfort food" = food whose reward MULTIPLIED by relief.
  🟢 Brickman & Campbell 1971: contrast effect — framework:
  cortisol relief = MECHANISM behind contrast.

  Source: Drill §3.15 (R7).
```

### §6.5 — Temporal overlap determines compound quality

```
🟡 3 TEMPORAL PATTERNS:

  SIMULTANEOUS PEAK (rare, maximum density):
    All channels peak ~ same time → MAXIMUM compound.
    Example: orgasm = physical B + evaluation A + social + relief.

  SEQUENTIAL PEAK (common, building):
    Channels peak one after another → experience "builds."
    Example: dinner with friends → richer over time.

  ASYNCHRONOUS (common, phased):
    Distinct phases with different character.
    Example: concert → visual → music → crowd → encore → afterglow.

  Source: Drill §3.15 (R7).
```

### §6.6 — Unified Conditional Model

```
🟡 4 VARIABLES DETERMINE INTERACTION TYPE:

  ┌─────────────────────┬──────────────────────────────────────────┐
  │ Variable            │ Effect on Interaction                     │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ① Substrate overlap │ Same substrate (A+A): SUBADDITIVE        │
  │                     │ Different substrate (A+B, B+B): ADDITIVE │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ② A gate direction  │ Positive: SUPERADDITIVE. Negative:       │
  │                     │ SUBTRACTIVE. Absent: RAW. Conflicted:    │
  │                     │ NON-LINEAR.                              │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ③ Relief presence   │ With relief: MULTIPLICATIVE              │
  │                     │ Without: base interaction only            │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ④ Temporal overlap  │ Simultaneous: MAXIMUM compound           │
  │                     │ Sequential: BUILDING. Async: PHASED.     │
  └─────────────────────┴──────────────────────────────────────────┘

  QUALITATIVE FORMULA:

    Compound = [Σ(same-substrate, subadditive)]
             + [A_gate × B_signals (modulation)]
             × [1 + relief_factor (multiplier)]
             × [temporal_overlap_coefficient]

  ⚠️ QUALITATIVE model — captures TYPES and DIRECTIONS, not magnitudes.

  Cross-ref: BFM §4 additive model → REFINED here to conditional.

  Source: Drill §3.15 (R7).
```

---

## §7 — 3 TYPES STATE DEPENDENCE (Cabanac Refined)

### §7.1 — Cabanac conflated 3 mechanisms

```
🟢🟡 ALLIESTHESIA (Cabanac 1971) = ACTUALLY 3 LEVELS:

  Cabanac 🟢: cùng stimulus, khác hedonic value tùy body state.
  Framework REFINES: Cabanac GỘP ít nhất 3 mechanisms khác nhau.


  ❶ SENSOR-LEVEL STATE DEPENDENCE (hardware / physics):

    Definition: Physical state changes SENSOR OUTPUT itself.
    → Temperature: thermoreceptor delta from homeostatic setpoint
    → CT afferents: optimal ~1-10 cm/s = HARDWARE property (🟢 Löken 2009)
    → Exercise eCB: release = f(duration, intensity) = metabolic

    Characteristics:
    → CANNOT override by PFC (physics, not opinion)
    → Present from BIRTH (hardware)
    → Type B territory primarily
    → DETERMINISTIC: same physical input = same output


  ❷ EVALUATION-LEVEL STATE DEPENDENCE (classical alliesthesia):

    Definition: Body-need state changes EVALUATION OUTCOME.
    → Đói → chocolate = "fit body-need" → opioid → pleasant
    → No → chocolate = "no body-need" → no opioid → neutral
    → Mechanism: P1 (schema pending) modulates evaluation result
    → 🟢 Cabanac 1971: gustatory alliesthesia

    Characteristics:
    → CAN partially override by PFC (force-eat when full = possible)
    → Develops with CHUNK COMPILATION (needs chunks)
    → Type A territory primarily
    → = H10 P1 mechanism


  ❸ GATE-LEVEL STATE DEPENDENCE (A modulates B experience):

    Definition: Social/emotional context modulates EXPERIENCE of
    hardware signal — B signal constant, A gate varies.
    → Lonely → A gate AMPLIFIES B → touch more valued
    → Touch-saturated → A gate NEUTRAL → touch baseline
    → Stranger → A gate SUPPRESSES B → touch uncomfortable
    → Dissociation → A gate BLOCKS → touch may not register

    Characteristics:
    → B signal NOT changing — A modulation changing
    → Develops with A gate formation (§3.3)
    → Interaction territory (A × B)


  COMPARISON TABLE:

  ┌──────────────────┬──────────────────┬──────────────┬─────────────────┐
  │ Dimension        │ ❶ Sensor-level   │ ❷ Evaluation │ ❸ Gate-level    │
  ├──────────────────┼──────────────────┼──────────────┼─────────────────┤
  │ What changes     │ Sensor output    │ Eval result  │ A modulation    │
  │                  │ itself           │              │ of B signal     │
  ├──────────────────┼──────────────────┼──────────────┼─────────────────┤
  │ PFC override?    │ NO (physics)     │ PARTIAL      │ PARTIAL         │
  │                  │                  │ (can force)  │ (therapy)       │
  ├──────────────────┼──────────────────┼──────────────┼─────────────────┤
  │ From birth?      │ YES              │ NO (needs    │ NO (needs       │
  │                  │ (hardware)       │ chunks)      │ A gate)         │
  ├──────────────────┼──────────────────┼──────────────┼─────────────────┤
  │ Type territory   │ Type B           │ Type A       │ A × B           │
  ├──────────────────┼──────────────────┼──────────────┼─────────────────┤
  │ Examples         │ Temp setpoint,   │ Food hunger, │ Touch lonely    │
  │                  │ CT speed range,  │ music mood,  │ vs stranger,    │
  │                  │ exercise fatigue │ insight gap  │ dissociation    │
  ├──────────────────┼──────────────────┼──────────────┼─────────────────┤
  │ Intervention     │ Change PHYSICAL  │ Change BODY- │ Change SOCIAL/  │
  │                  │ state            │ NEED state   │ EMOTIONAL       │
  │                  │                  │              │ context         │
  └──────────────────┴──────────────────┴──────────────┴─────────────────┘

  Source: Drill §3.9 (R14).
```

### §7.2 — Temperature Paradox: Cabanac refined

```
🟡 TEMPERATURE = SENSOR-LEVEL, NOT EVALUATION-LEVEL:

  Cabanac INCLUDED temperature in alliesthesia (1971).
  Framework REFINES: temperature = sensor-level mechanism
  MASQUERADING as evaluation-level.

  Observable: Cold person → warm water = pleasant
              Warm person → warm water = unpleasant
  Looks like: evaluation-level (same as food)
  Actually is: sensor-level (thermoreceptor delta from setpoint)

  Proof:
  → PFC CANNOT override: "WANT to enjoy hot bath" when overheated = FAILS
  → Evaluation-level CAN be partially overridden: force-eat when full = POSSIBLE
  → Temperature = ABSOLUTE, non-negotiable
  → Food = PARTIAL, overridable

  → Same OBSERVATION (changed hedonic value)
  → Different MECHANISM (sensor physics vs evaluation circuit)
  → Framework contribution: distinguishes mechanism levels
     that Cabanac's concept conflated

  Source: Drill §3.9 (R14).
```

---

## §8 — DEVELOPMENT + INDIVIDUAL DIFFERENCES

### §8.1 — A/B Development Gradient Lifecycle

```
🟡 A/B RATIO SHIFTS ACROSS DEVELOPMENT:

  STAGE 1 — Neonate (0-3 months): A/B ≈ 5/95
    Type B dominant: touch, warmth, sucking, vestibular
    Type A₀ only: sweet preference (~5%)
    → Body = nearly pure hardware-driven reward
    → Neonatal care = primarily physical contact

  STAGE 2 — Infant (3-18 months): A/B ≈ 20/80
    Type B still dominant. A growing (food preferences, familiar faces)
    → Stranger anxiety (~8 months) = A gate starts evaluating

  STAGE 3 — Child (2-7 years): A/B ≈ 40/60
    A expanding: music preference, food pickiness, coherence (puzzles)
    B maintained: still NEEDS touch, warmth, physical comfort
    → A can now OVERRIDE B: "don't touch me!" (stranger eval)

  STAGE 4 — Adolescent (12-18): A/B ≈ 60/40
    A dominant: social evaluation INTENSE, aesthetic developing
    B maintained but SOCIALLY CONSTRAINED:
    → "Embarrassed by parent hug" = social A gate VERY strong

  STAGE 5 — Adult (25+): A/B ≈ 70/30 (varies enormously)
    Type A: full range (mastery, aesthetic, social, coherence)
    Type B: persists but often NEGLECTED:
    → "Quá bận để tập" (exercise B neglected)
    → "Không ai ôm" (touch B neglected)
    → Body-Base deficit ACCUMULATES silently
    → Expert in domain: A SO compiled → feels automatic like B

  STAGE 6 — Elderly: A/B potentially shifts BACK toward B
    → Cognitive decline reduces A capacity
    → Physical touch becomes MORE valuable again
    → = Evolutionary CIRCLE: hardware first and last

  LIFECYCLE ARC:
    B dominant → A builds → A peaks → A may decline → B persists
    B NEVER reaches zero — hardware PERSISTS

  Source: Drill §3.8, §3.10 (R19).
```

### §8.2 — 4 Sensitive Periods (NOT critical)

```
🟡 WINDOWS WHERE P5 TAGS COMPILE MORE READILY:

  WINDOW 1 — Foundation (0-3 tuổi):
    A/B ≈ 5-20% / 95-80%. P5 tags from BODY experience.
    → Attachment quality = P5 FOUNDATION tag (🟢 Sroufe 2005).
    → [người → safe] vs [người → unsafe] — PERSISTS deepest.

  WINDOW 2 — Exploration (3-7 tuổi):
    A/B ≈ 40/60. P5 tags from PLAY + exploration.
    THE WINDOW where approach/avoidance tags for DOMAINS compile.
    → 1 STRONG avoidance tag can override many mild approach tags.

  WINDOW 3 — Deepening (7-12 tuổi):
    A/B ≈ 50/50. School begins → threat vs novelty DIVERGES.
    → "Ghét toán" or "thích toán" compiled here → persists decades.
    → Education system = MASS P5 TAG INSTALLATION mechanism.

  WINDOW 4 — Identity (12-18 tuổi):
    A/B ≈ 60/40. P5 tags COMPOUND with social (③) tags.
    → "Tôi là người thích X" = accumulated approach → identity chunk.
    → Reconsolidation still possible but HARDER.

  🟡 NOT "critical period" (Lorenz binary):
    Sensitive = compile EASIER, tag ATTACHES STRONGER.
    Later reconsolidation possible (but requires destabilization).

  Source: Drill §3.21 (R6). 🟢 Sroufe 2005, Bowlby 1969, Ainsworth 1978.
```

### §8.3 — 4-Pathway × P5 Tag Model

```
🟡 COMPILE PATHWAY → DIFFERENT P5 TAGS → DIFFERENT ADULT REWARD:

  ┌────────────────────────┬──────────────────────┬──────────────────────┐
  │ Pathway                │ Body State at Compile│ Adult Reward Profile  │
  ├────────────────────────┼──────────────────────┼──────────────────────┤
  │ ① Hardware Fit         │ Dopamine/opioid      │ ② coherence natural  │
  │   (body tự reward)     │ (APPROACH tag)       │ flow ACCESSIBLE      │
  │                        │                      │ sustainable decades  │
  ├────────────────────────┼──────────────────────┼──────────────────────┤
  │ ② Trust Install        │ Trust-warmth         │ Depends on collective│
  │   (nghe mẹ → compile)  │ (moderate APPROACH)  │ chain holding        │
  ├────────────────────────┼──────────────────────┼──────────────────────┤
  │ ③ Social Default       │ Neutral-conformity   │ ④ relief dominant    │
  │   (mọi người đều đi)   │ (weak/NEUTRAL tag)   │ "xong rồi" > "hay"  │
  ├────────────────────────┼──────────────────────┼──────────────────────┤
  │ ④ Threat Avoidance     │ Cortisol-NE          │ ④ relief ONLY        │
  │   (sợ bị mắng)         │ (AVOIDANCE tag)      │ burnout trajectory   │
  │                        │                      │ "giỏi MÀ không thích"│
  └────────────────────────┴──────────────────────┴──────────────────────┘

  KEY: Adult reward capacity = NOT random trait.
  = Accumulated P5 tags through childhood × pathway used.
  = "Talent" = early opioid-tagged exposure + hardware fit + years

  COMPOUND TAG ACCUMULATION:
  → Each domain accumulates tags over years
  → Peak negative > peak positive per event (evolutionary asymmetry)
  → "1 lần bị mắng khi giải toán sai > 20 lần giải toán êm ả"
  → Approach snowball: approach → seek → compile → more approach
  → Avoidance snowball: avoid → no compile → tag stays → avoid more
  → BOTH self-reinforcing. Breaking avoidance = EXTERNAL intervention needed.

  OVERJUSTIFICATION = P5 TAG OVERWRITE:
  → 🟢 Lepper, Greene & Nisbitt 1973:
    Free drawing → expected reward → drawing DROPS
  → Framework: extrinsic reward OVERWRITES P5 from approach to instrumental
  → Pathway ① → ④ shift = DESTRUCTIVE (intrinsic → extrinsic)

  Source: Drill §3.21 (R6). Cross-ref: Compile-Taxonomy.md §3.
  🟢 Ryan & Deci SDT. 🟢 Harter 1981, 1992. 🟢 Mueller & Dweck 1998.
```

### §8.4 — 5-Axis Individual Differences Model

```
🟡 INDIVIDUAL REWARD PROFILE = 5-AXIS EMERGENT:

  ┌──────────────────────┬──────────────────────┬─────────────────────┐
  │ Axis                 │ What It Determines   │ Changeable?          │
  ├──────────────────────┼──────────────────────┼─────────────────────┤
  │ ① Hardware           │ Reward CEILING +     │ NO (genetic)         │
  │   Architecture       │ BIAS toward profiles │ COMT, DRD4, MAO-A,  │
  │                      │                      │ NE, opioid density   │
  ├──────────────────────┼──────────────────────┼─────────────────────┤
  │ ② Childhood          │ Reward DIRECTION +   │ VERY HARD (deepest   │
  │   Compilation        │ P5 tags (§8.3)       │ chunks, reconsolid.  │
  │                      │                      │ possible but costly) │
  ├──────────────────────┼──────────────────────┼─────────────────────┤
  │ ③ Domain Exposure    │ WHERE reward         │ YES (education +     │
  │                      │ expresses (P2 met)   │ experience)          │
  ├──────────────────────┼──────────────────────┼─────────────────────┤
  │ ④ Channel Balance    │ HOW DOMINANT one     │ PARTIALLY (lifestyle │
  │                      │ profile becomes      │ choices, culture)    │
  ├──────────────────────┼──────────────────────┼─────────────────────┤
  │ ⑤ Current State      │ Reward ACCESSIBILITY │ YES (most malleable) │
  │                      │ right now            │ Cortisol, sleep,     │
  │                      │                      │ social context       │
  └──────────────────────┴──────────────────────┴─────────────────────┘

  KEY: "Reward sensitivity" is NOT a single trait.
  = 5-axis EMERGENT property. 2 people "equally sensitive"
  but in COMPLETELY DIFFERENT profiles.

  TYPE B = "DEMOCRATIC REWARD":
  → B = non-opioid, non-PFC, hardware pathways
  → Hardware individual differences = primarily TYPE A variation
  → B reward MORE EGALITARIAN across individuals
  → B = evolution's EQUALIZER

  Source: Drill §3.22 (R8).
  Cross-ref: PFC-Hardware.md (Axis ① details: COMT × DRD4 × Reward).
```

### §8.5 — COMT × DRD4 Interaction Patterns

```
🟡 COMT × DRD4 = 4 COMPOUND REWARD TYPES:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ Combination        │ Reward Pattern       │ Popular Label        │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + 7R       │ Clear fast + high    │ "Thrill seeker"      │
  │                    │ threshold → NEED     │ Big novel experiences │
  │                    │ novel BIG experiences│                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + 4R       │ Clear slow + low     │ "Obsessive expert"   │
  │                    │ threshold → SATISFY  │ Deep single domain   │
  │                    │ within single domain │                      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + 4R       │ Clear fast + low     │ "Social butterfly"   │
  │                    │ threshold → many     │ Many small rewards   │
  │                    │ small rewards        │ from many domains    │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + 7R       │ Clear slow + high    │ "Frustrated genius   │
  │                    │ threshold → draft    │  or true genius"     │
  │                    │ stuck + needs BIG    │ BIMODAL outcome      │
  │                    │ chunks              │                      │
  └────────────────────┴──────────────────────┴──────────────────────┘

  COMT × CHILDHOOD COMPILATION:

  ┌────────────────────┬──────────────────────┬──────────────────────┐
  │ Combination        │ Reward Life          │ Key Insight          │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + approach │ DEEP FLOW expert     │ Best case for ②      │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Met/Met + avoidance│ RIGID ANXIETY        │ Worst combination    │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + approach │ CREATIVE EXPLORER    │ Versatile joy        │
  ├────────────────────┼──────────────────────┼──────────────────────┤
  │ Val/Val + avoidance│ SCATTERED ANXIETY    │ Nothing deep enough  │
  └────────────────────┴──────────────────────┴──────────────────────┘

  SAME hardware, DIFFERENT childhood = COMPLETELY DIFFERENT reward life.
  → Hardware sets RANGE. Childhood sets DIRECTION within range.
  → = "Nature sets the instrument. Nurture plays the tune."

  ⚠️ COMT × Reward = extension from cognition (PFC-Hardware.md).
  Reward-specific COMT data limited. COMT × DRD4 = framework synthesis.
  🟢 Egan et al. 2001: COMT Val/Met fMRI well-replicated.
  🔴 DRD4 Hypothesis D = framework hypothesis, not established.

  Source: Drill §3.22 (R8). Cross-ref: PFC-Hardware.md §3-§4.
```

### §8.6 — 4 Departure Patterns + 3-Variable Shorthand

```
🟡 INDIVIDUAL DEPARTURES FROM AVERAGE GRADIENT:

  ┌──────────────────┬──────────────────────┬──────────────────────────┐
  │ Pattern          │ Description          │ Mechanism                │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ ① Precocious A   │ A develops EARLY     │ High PFC + Hardware Fit  │
  │                  │ (child prodigy)      │ + early approach tags    │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ ② Extended B     │ B stays dominant     │ Touch-rich culture       │
  │                  │ longer than average  │ (athletes, craftsmen)    │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ ③ Arrested A     │ A STOPS developing   │ Threat-path education →  │
  │                  │ at Stage 3-4         │ avoidance tags BLOCK     │
  ├──────────────────┼──────────────────────┼──────────────────────────┤
  │ ④ Reversed A/B   │ A declines           │ Chronic stress →         │
  │                  │ prematurely          │ cortisol → A eroded      │
  └──────────────────┴──────────────────────┴──────────────────────────┘

  Pattern ③ = MOST COMMON education failure:
  → "I can't do math" = NOT hardware limitation
  → = Accumulated avoidance tags (R6 mechanism)
  → Intervention: reconsolidation window + safe re-exposure

  Pattern ④ = burnout mechanism:
  → Chronic stress → sustained cortisol → dlPFC dendrite retraction
  → A capacity physically REDUCED (not just blocked)
  → Recovery: cortisol reduction + time + B floor restoration


  3-VARIABLE SHORTHAND (practical compression):

    ① A/B Ratio: where on spectrum (pure A → balanced → pure B)
    ② Dominant Profile: which of 5 is STRONGEST (①②③④⑤)
    ③ Breadth: how many profiles ACTIVE (narrow → broad)

  → "Personality" re: reward = this 3-variable profile
  → "Compatibility" in relationships = OVERLAP (not identity)
  → Simple "extrovert/introvert" fails to predict reward behavior

  ⚠️ 3-Variable Shorthand = practical compression, loses interaction detail.
  Cannot MEASURE precisely yet — organizing framework.

  Source: Drill §3.22 (R8).
```

---

## §9 — KEY EVIDENCE TABLE

### §9.1 — Naltrexone: A vs B Discriminator

```
🟢🟡 NALTREXONE (OPIOID BLOCKER) = KEY DISCRIMINATOR:

  ┌──────────────┬─────────────┬──────────────┬──────────────────────────┐
  │ Modality     │ Naltrexone  │ Type         │ Source                    │
  ├──────────────┼─────────────┼──────────────┼──────────────────────────┤
  │ Food/sweet   │ BLOCKS ✅    │ Type A       │ 🟢 Smith & Berridge 2007 │
  │ Music        │ BLOCKS ✅    │ Type A       │ 🟢 Mallik 2017           │
  │ Sex          │ BLOCKS ✅    │ Type A       │ 🟢 Sex Med Rev 2025      │
  │ Insight      │ (untested)  │ Type A (pred)│ 🔴 Framework prediction  │
  │ Touch        │ NO EFFECT ⚠️│ Type B       │ 🟢 Loseth 2019           │
  │ Exercise     │ NO EFFECT ⚠️│ Type B       │ 🟢 Fuss 2015, Siebers 21│
  │ Temperature  │ (untested)  │ Type B (pred)│ 🔴 Framework prediction  │
  │ Spicy food   │ BLOCKS      │ A (compensat)│ 🟡 Via pain → endorphin  │
  └──────────────┴─────────────┴──────────────┴──────────────────────────┘

  → Naltrexone = "litmus test" for Type A vs B
  → NOT yet tested: insight, temperature (framework predictions)

  Source: Drill-Reward-Feeling-Cases.md §9.1.
```

### §9.2 — Endocannabinoid Multi-Role

```
🟢 eCB = CONTEXT-DEPENDENT FUNCTION:

  IN NAcc hotspot (🟢 Mahler 2007):
    → Anandamide at hotspot DOUBLES liking reactions
    → BUT: opioid-DEPENDENT (🟢 Stacey 2018)
    → = Type A territory (AMPLIFIER, not primary)

  IN exercise (🟢 Fuss 2015 PNAS):
    → Runner's high = endocannabinoid PRIMARY
    → Naltrexone DOES NOT reduce exercise euphoria
    → = Type B territory (PRIMARY, not amplifier)

  → SAME molecule, DIFFERENT circuit, DIFFERENT function
  → = Neurochemical Multi-Role Principle (§1.5)

  Source: Drill-Reward-Feeling-Cases.md §9.2.
```

---

## §10 — 5 FORCES HOLDING MODEL

### §10.1 — Why geniuses persist when cost > reward

```
🟡 5 FORCES COMPOUND HOLDING — for sustained creative arcs:

  ┌─────────────────────┬────────────────────────────────────────────┐
  │ Force               │ Mechanism                                   │
  ├─────────────────────┼────────────────────────────────────────────┤
  │ F1: MEANING         │ Life-level Anchor-Schema (Meaning.md §1)   │
  │ (Life Anchor)       │ = "Tôi LÀ physicist" compiled deep         │
  │                     │ → CONTINUOUS background identity-coherence  │
  │                     │ → Absent: "để làm gì?" → break dễ          │
  ├─────────────────────┼────────────────────────────────────────────┤
  │ F2: GAP-DIRECTION   │ Persistent P1 at life scale                │
  │ (Zeigarnik life)    │ = Specific research question / project     │
  │                     │ → PFC ⑧ Active Lock — CANNOT release       │
  │                     │ → Absent: có meaning nhưng không biết hướng │
  ├─────────────────────┼────────────────────────────────────────────┤
  │ F3: ② MICRO-REWARDS │ Intermittent reinforcement                 │
  │ (Intermittent ②)    │ = Mỗi sub-insight → opioid → "đúng hướng" │
  │                     │ → Intermittent = STRONGEST schedule         │
  │                     │   (🟢 Skinner variable ratio)               │
  │                     │ → ALONE insufficient for years-long arcs    │
  ├─────────────────────┼────────────────────────────────────────────┤
  │ F4: TRUST THÁI ĐỘ   │ Body-base smooth with collective           │
  │ (Collective trust)  │ = DEFAULT valence toward humanity = APPROACH│
  │                     │ → GATE deciding WHO benefits from ②         │
  │                     │ → Absent: solve for self only               │
  │                     │ → Inverted: use intelligence AGAINST        │
  ├─────────────────────┼────────────────────────────────────────────┤
  │ F5: RECOGNITION     │ Status/peer acknowledgment                  │
  │ (Social ③)          │ = "Được công nhận" = resource access map    │
  │                     │ → CAN override material deficit             │
  │                     │ → Paradox: pre-fame = most creative         │
  └─────────────────────┴────────────────────────────────────────────┘

  5 FORCES = COMPOUND — mỗi force hold 1 tầng:
    F1 = WHY. F2 = WHERE. F3 = CONFIRMATION.
    F4 = FOR WHOM. F5 = VALIDATION.

  INSUFFICIENT forces → characteristic failures:
    Missing F1: "talented but directionless"
    Missing F2: "meaningful life but stuck"
    Missing F3: "persistent but unrewarded" (burnout risk)
    Missing F4: "brilliant but selfish"
    Missing F5: "contributing but unacknowledged"

  Source: Drill §3.20 (R3 extended).
```

### §10.2 — Trust Thái Độ vs Trust Nội Dung

```
🟡 2 LOẠI TRUST — INDEPENDENT, DIFFERENT SOURCE:

  ┌──────────────────────┬──────────────────────────────────────────┐
  │ TRUST NỘI DUNG       │ TRUST THÁI ĐỘ                            │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ "Chain dài collective │ "Con người NÓI CHUNG là tích cực"        │
  │  hold HOẠT ĐỘNG"     │ = Body-base DEFAULT = APPROACH            │
  │ = COGNITIVE trust    │ = BODY-BASE trust                         │
  │ = Tin hệ thống      │ = CẢM THẤY smooth với mọi người          │
  │ Source: evidence,    │ Source: CHILDHOOD COMPILATION              │
  │ institution track    │ = Attachment pattern (🟢 Bowlby/Ainsworth) │
  └──────────────────────┴──────────────────────────────────────────┘

  → CÓ THỂ có 1 mà không có 2:
    Trust nội dung without thái độ: "biết hệ thống ok, ghét mọi người"
    Trust thái độ without nội dung: "yêu mọi người, không tin hệ thống"

  → F4 = GATE deciding WHERE intelligence POINTS
  → Reward mechanism = AMORAL — H10 fires for coherence bất kể moral
  → P5 tag determines direction: childhood compilation decides

  Source: Drill §3.20 (R3 extended).
  🟢 Bowlby 1969, Ainsworth 1978: attachment styles.
```

### §10.3 — Recognition can exceed material comfort

```
🟡 RECOGNITION > MATERIAL: RATIONAL AT BODY-BASE:

  ① Status.md: recognition = RESOURCE ACCESS MAP node
     → "Được công nhận" = predict FUTURE resource access
     → Body: [recognized → future safe → approach]
  ② Collective-Body.md: chain dài sống ở collective
     → "Ăn ngon" = short chain (immediate)
     → "Được công nhận" = long chain (aggregate HIGHER expected value)
  ③ Meaning.md: Life-level anchor > daily anchor
     → Life-level OVERRIDE daily-level discomfort

  PFC KHÔNG CẦN check — body-base ALREADY evaluated.
  = RATIONAL at body-base, not "hijack" or "delusion."

  GIỚI HẠN: L0 survival FLOOR (Body-Base.md)
  → Malnutrition → L0 signal OVERRIDE status reward

  RECOGNITION PARADOX:
  → Pre-fame: F1+F2+F3 = pure ② → maximum creativity
  → Post-fame: F5 adds → sustaining BUT constraining
  → Expectation pressure → cortisol → ② pathway disrupted
  → = WHY "sophomore slump" exists across creative domains

  Source: Drill §3.20 (R3 extended).
```

---

## §11 — HONEST ASSESSMENT

### §11.1 — Research-backed (🟢)

```
🟢 STRONG EVIDENCE (50+ sources):

  Type A/B:
  → Opioid = primary Type A (Berridge, Mallik 2017, Tik 2020)
  → Touch = Type B, naltrexone no effect (Loseth 2019)
  → CT afferents → posterior insula (Löken 2009)
  → Exercise euphoria = eCB not opioid (Fuss 2015, Siebers 2021)
  → eCB in NAcc dependent on opioid (Stacey 2018)
  → Neonate sweet → opioid calming (Blass 1991, 1994)
  → Gustofacial reflexes subcortical (Steiner 1973, anencephalic)
  → Decorticated rats still show sweet hedonic (Berridge 2003)

  Neural mechanisms:
  → Posterior-to-anterior insula gradient (Craig 2002, 2013)
  → ACC conflict monitoring (Botvinick 2004)
  → vmPFC somatic marker (Damasio 1994)
  → mOFC convergence for beauty (Zeki 2014, Ishizu 2011, Blood 2001)
  → DLPFC deactivates during flow (Limb & Braun 2008)
  → Dissociation = PFC hyperactivation (Lanius 2010)
  → Reconsolidation (Nader 2000), REBUS (Carhart-Harris 2019)

  Development + Individual:
  → Attachment → competence (Sroufe 2005, 30 years)
  → Intrinsic motivation orientation (Harter 1981, 1992)
  → Overjustification effect (Lepper 1973)
  → Praise type → motivation (Mueller & Dweck 1998)
  → COMT Val/Met cognition (Egan 2001)
  → Hedonic adaptation (Brickman & Campbell 1971)

  Other:
  → VTA reward prediction error (Schultz 1997)
  → Hotspot ~1mm³ finite (Peciña & Berridge 2005)
  → Visual/motor imagery uses cortex (Kosslyn 1994, Jeannerod 1995)
  → Neural reuse (Anderson 2010)
  → Van der Kolk 2014: body-oriented therapy
```

### §11.2 — Framework synthesis (🟡)

```
🟡 CONSISTENT BUT FRAMEWORK-SPECIFIC (60+ items):

  Core architecture:
  → Type A/B distinction (evaluative vs direct state)
  → A/B = ORTHOGONAL dimension (not 6th profile)
  → A₀→A₃ complexity gradient
  → A Gates B mechanism (3 bước → 5-step insula process)
  → B = "safe baseline reward" (evolutionary floor)
  → 5 Reward Profiles (framework organizing)

  Dynamics:
  → Temporal Stack Model (onset follows A₀→A₃)
  → Conditional Interaction Model (4 variables)
  → Relief = system-state multiplier
  → 3 types state dependence (refining Cabanac)
  → Motor urgency = 3-component compound

  Development:
  → A/B development gradient lifecycle
  → 4-Pathway × P5 Tag Model
  → Compound Tag Accumulation (bidirectional snowball)
  → 5-Axis Individual Differences Model
  → 4 Departure Patterns
  → Poincaré Equivalence = H10 P4 on any domain

  Sustained arcs:
  → 5 Forces Holding Model
  → Trust thái độ vs nội dung distinction
  → Recognition paradox (pre-fame = most creative)

  All items = consistent with 🟢 research but not directly tested
  as framework claims. Framework ADDS organizing structure.
```

### §11.3 — Hypotheses and predictions (🔴)

```
🔴 TESTABLE PREDICTIONS (40+ numbered):

  Core architecture:
  → Preview fidelity A > B (P-R17a through P-R17d)
  → B habituation rates modality-specific (P-R20a through P-R20d)
  → A Gates B = insula gradient (P-R18a through P-R18d)
  → A₀ complexity gradient (P-R19a through P-R19d)
  → 3-type state dependence (P-R14a through P-R14d)
  → Motor urgency 3-component (P-R4a through P-R4d)

  Dynamics:
  → Onset latency gradient B→A₃ (P-R5a through P-R5d)
  → A₃ afterglow = 4 curves (P-R5 mechanism)
  → Conditional Interaction Model (P-R7a through P-R7d)

  Development:
  → P5 → adult capacity (P-R6a through P-R6d)
  → 5-Axis model (P-R8a through P-R8d)
  → Beauty = H10 P4 (P-R3a through P-R3e)

  Sustained arcs:
  → 5 Forces predictions (P-R3f through P-R3h)

  Full prediction list: Drill-Reward-Feeling-Main.md §11.
```

### §11.4 — Key limitations

```
⚠️ LIMITATIONS:

  → "5 profiles" = framework organizing, brain may not have 5 discrete types
  → Type A/B = framework organizing tool, NOT brain architecture
  → A/B ratios (80/20 etc.) = ILLUSTRATIVE, not measured
  → A₀→A₃ gradient = organizing, brain may not have discrete levels
  → Onset latency values = ESTIMATES from processing depth, not measured
  → Conditional Interaction Model = qualitative, not mathematical
  → Relief multiplier magnitudes = ILLUSTRATIVE ranges
  → 5 Forces weights/interactions unknown
  → COMT × Reward = extension from cognition, reward-specific data limited
  → COMT × DRD4 interaction = framework synthesis, not tested
  → 4 Departure Patterns = framework organizing from clinical observation
  → 3-Variable Shorthand = cannot measure precisely yet
  → Biographical data (8 figures) = retrospective, selection bias
  → Compound Tag Accumulation = qualitative, weights not measured
```

---

## §12 — CROSS-REFERENCES

```
FRAMEWORK FILES LIÊN QUAN:

  COMPLEMENT FILE:
  → 03-Reward.md — HOW reward fires (H10 preconditions) → file này WHAT KINDS

  MECHANISM:
  → Body-Feedback-Mechanism.md v1.1 — chunk dynamics + A/B × source mapping
  → Feeling.md v2.0 — feeling = PFC observation of reward signal
  → Feeling-Mechanism-Deep.md — §4 reward mechanism detail

  PFC:
  → PFC-Configuration.md — 6 modes × reward interaction
  → PFC-Function.md v1.1 — 24 functions
  → PFC-Hardware.md — COMT/DRD4 × reward patterns (Axis ①)

  RELATED SYSTEMS:
  → Compile-Taxonomy.md v1.0 — 4 pathways × P5 tag
  → Dopamine-Reward-Rejection.md v1.0 — dopamine = alert, Type A opioid = reward
  → Liking-Wanting.md v1.0 — bridge Berridge, wanting mechanisms
  → Cortisol-Baseline.md v2.0 — relief profile ④
  → Gap-Direction.md v1.0 — gap direction = F2 in 5 Forces
  → Meaning.md v2.0 — life-level Anchor-Schema = F1
  → Status.md v2.0 — Resource Access Map = F5
  → Connection.md v3.1 — L1 SPM-owned, 3 Generative Primitives

  DRILL SOURCE:
  → Drill-Reward-Feeling-Main.md v1.2 — full drill source (~6,700L)
  → Drill-Reward-Feeling-Cases.md v1.0 — data + cases (~2,015L)
```
