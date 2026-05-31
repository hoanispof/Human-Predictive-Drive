---
title: Body-Feedback Precondition — 5 Preconditions for Signal Fire
version: 1.0
created: 2026-05-30
status: REFERENCE v1.0
scope: |
  PRECONDITION REFERENCE: KHI NÀO body-feedback signal (reward/dissonance) fires?
  5 Preconditions model — formalize từ 03-Reward.md §3 (drill origin).
  Mỗi precondition: definition, mechanism, failure mode, refinement insights.
  Scope qualifier: ALL 5 required cho Evaluative. Direct-State = simplified subset.
  v1.0: Refine từ drill H10 — thêm direction component, genesis/decode split,
  boredom disambiguation, dynamic zone, 4-pathway quality ceiling.
purpose: |
  Existing files phân loại body-feedback theo:
    WHAT KINDS:  Reward-Signal-Architecture.md (reward types)
                 Dissonance-Signal-Architecture.md (dissonance types)
    HOW:         Body-Feedback-Mechanism.md (chunk dynamics)
    VOCAB:       Body-Feedback-Label.md (terminology)
  File này thêm trục: WHEN — 5 preconditions quyết định signal CÓ fire hay KHÔNG.
  Hoàn thành bộ 4 siblings: Mechanism → Label → Precondition → Signal Architecture.
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — ngang hàng Body-Feedback-Mechanism.md.
  Sibling relationship:
    Body-Feedback.md          = SYNTHESIS entry point (overview)
    Body-Feedback-Mechanism.md = HOW signal arises (chunk dynamics)
    Body-Feedback-Label.md     = VOCAB reference (terminology)
    Body-Feedback-Precondition.md = ⭐ WHEN signal fires (this file)
    Reward-Signal-Architecture.md = WHAT KINDS reward
    Dissonance-Signal-Architecture.md = WHAT KINDS dissonance
dependencies:
  - Body-Feedback.md v2.0 — §5.2 H10 summary table (pointer to this file)
  - Body-Feedback-Mechanism.md v2.1 — §6.2 chunk dynamics × preconditions mapping
  - Body-Feedback-Label.md v2.1 — vocabulary reference
  - Reward-Signal-Architecture.md v2.1 — §1.3 Evaluative/Direct-State × Precondition-1–Precondition-5
  - Dissonance-Signal-Architecture.md v1.0 — dissonance application (§9 cross-ref)
  - 03-Reward.md v1.1 — §3 H10 drill origin, §2 7-step VTA
  - 04-Integration.md — §9 H10 refined
  - Gap-Direction.md v2.0 — §3 "chưa biết = không gap", §6.3 hierarchy
  - Chunk.md v2.2 — chunk substrate, context-tag model
  - Compile-Taxonomy.md v2.0 — §3 4-pathway model (Precondition-5)
  - Cortisol-Baseline.md v2.2 — §3.3 Direction-At-Compile, §7 source > level
  - Reward-Calibration.md v1.1 — §1.2 Goldilocks per-gap dynamic
  - Boredom.md v2.1 — §1 + §7 boredom ≠ Precondition-3 failure
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Precondition — 5 Preconditions for Signal Fire

> **Cùng 1 bản nhạc hay.**
> Người chưa nghe bao giờ → "lạ quá" (không đủ chunks decode).
> Người nghe lần đầu → "hay!" (mới + vừa đủ match).
> Người nghe lần thứ 1000 → "chán" (không còn delta).
> Người bị ép nghe khi nhỏ → "ghét dù biết hay" (tag avoidance).
> Người đang no nê âm nhạc → "không cảm gì" (không có gap).
>
> Cùng stimulus. 5 người. 5 phản ứng KHÁC NHAU.
> Mỗi phản ứng = 1 precondition KHÁC bị fail.
>
> Body-feedback signal KHÔNG fire tự động khi có stimulus.
> Signal fires KHI VÀ CHỈ KHI 5 preconditions ĐỀU thỏa mãn.
>
> File này formalize 5 preconditions đó.

---

## §0 — Position + Scope

### §0.1 — 4 câu hỏi, 4 files

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Body-Feedback System                             │
│                                                                     │
│  WHAT KINDS?  → Reward-Signal-Architecture.md                      │
│                 Dissonance-Signal-Architecture.md                   │
│                                                                     │
│  HOW?         → Body-Feedback-Mechanism.md (chunk dynamics)        │
│                                                                     │
│  WHEN?        → ⭐ Body-Feedback-Precondition.md (THIS FILE)       │
│                 5 preconditions: Precondition-1–Precondition-5      │
│                 Signal fires if and only if all 5 Preconditions met            │
│                                                                     │
│  VOCAB?       → Body-Feedback-Label.md (terminology)               │
│                                                                     │
│  OVERVIEW?    → Body-Feedback.md (synthesis entry point)            │
└─────────────────────────────────────────────────────────────────────┘
```

### §0.2 — Scope + boundary rules

**File này DEFINE**:
- 5 preconditions cho body-feedback signal fire (Precondition-1–Precondition-5)
- Mỗi precondition: mechanism, met/failed states, refinement insights
- Conjunction logic (AND-gate structure)
- Developmental arc (infant → adult → aging)
- Dissonance application (not just reward)

**File này KHÔNG duplicate** (chỉ cross-ref):

| Nội dung | Thuộc file | Cross-ref |
|---|---|---|
| Evaluative/Direct-State × Precondition-1–Precondition-5 table | Reward-Signal-Architecture §1.3 | §1.2, §2-§6 per-Precondition notes |
| Chunk dynamics × preconditions mapping | Body-Feedback-Mechanism §6.2 | §7 conjunction logic |
| H10 48-line summary table | Body-Feedback §5.2 | §0.1 pointer |
| Timing asymmetry (dissonance → reward) | Dissonance-Signal-Architecture | §9 cross-ref |
| 7-step VTA mechanism | 03-Reward.md §2 | §4.2 cross-ref |

### §0.3 — Reading prerequisites

```
PHẢI đọc TRƯỚC:
  Body-Feedback.md         — dual-pull, interface loop, body-base
  03-Reward.md §2-§3       — 7-step VTA, H10 drill origin
  Chunk.md v2.2+           — chunk substrate, context-tag
  Compile-Taxonomy.md      — 4-pathway model (for §6 Precondition-5)

ĐỌC SONG SONG:
  Reward-Signal-Architecture — WHAT KINDS reward (→ type-split per precondition)
  Dissonance-Signal-Architecture — WHAT KINDS dissonance (→ §9 dissonance application)
  Body-Feedback-Mechanism — HOW chunks fire (→ dynamics × preconditions)
  Gap-Direction.md — gap has direction (→ §2 Precondition-1, §5 Precondition-4)
```

### §0.4 — Origin + evolution

🟡 File này formalize "H10" — hypothesis number từ drill 03-Reward.md §3.

```
DRILL ORIGIN (2026):
  03-Reward.md §3: "H10 — Body Signal Precondition Hypothesis v2"
  → 5 preconditions: Schema pending, Chunks base, prediction-delta,
    Goldilocks zone, Chunk tag

FRAMEWORK EVOLUTION:
  ① Drill → 92+ files dùng "H10" như concept name
  ② Gap-Direction.md → Precondition-1 thiếu direction, Precondition-2 thiếu genesis/decode split
  ③ Boredom.md → boredom ≠ Precondition-3 failure (disambiguation needed)
  ④ Reward-Calibration.md → Goldilocks zone dynamic (not fixed 40-70%)
  ⑤ Compile-Taxonomy.md → Precondition-5 binary → 4-pathway quality ceiling
  ⑥ Cortisol-Baseline.md → Precondition-5 opioid/cortisol → Direction-At-Compile gate

THIS FILE: Refine + formalize tất cả insights trên thành official reference.
```

---

## §1 — Formal Statement

### §1.1 — The conjunction claim

🟡 **Body-Feedback Precondition Statement v1.0**:

> Body-feedback signal (reward OR dissonance) fires to full magnitude
> WHEN AND ONLY WHEN **all 5 preconditions** are simultaneously met:
>
> | # | Precondition | Câu hỏi nó trả lời |
> |---|---|---|
> | Precondition-1 | **Directed-Gap** | Có gap đang active không? Gap hướng về đâu? |
> | Precondition-2 | **Chunk-Substrate** | Có đủ chunks để decode stimulus không? |
> | Precondition-3 | **Delta-Gate** | Có đủ biến động để VTA detect không? |
> | Precondition-4 | **Match-Range** | Match có nằm trong vùng phù hợp không? |
> | Precondition-5 | **Compile-Gate** | Chunks tag cho phép signal fire đúng hướng không? |
>
> **Logical form**: Signal_full = Precondition-1 ∧ Precondition-2 ∧ Precondition-3 ∧ Precondition-4 ∧ Precondition-5

**Claim strength**: 🟡 Framework synthesis — mỗi precondition riêng có research support 🟢,
nhưng conjunction "ALL 5 required" là framework-level claim chưa có direct empirical test.

### §1.2 — Scope qualifier: Evaluative vs Direct-State

```
⭐ "ALL 5 required" chỉ áp dụng cho EVALUATIVE reward/dissonance.

EVALUATIVE (compiled patterns, learning-dependent):
  → Precondition-1–Precondition-5 ALL required
  → Ví dụ: nghe nhạc hay, giải bài toán, thưởng thức Van Gogh

DIRECT-STATE (hardware signals, body-need-driven):
  → Precondition-1 simplified: body-need LUÔN present (hunger, thirst, pain, touch)
  → Precondition-2 minimal: hardware paths from birth (không cần compiled chunks)
  → Precondition-3 uncertain: may bypass VTA entirely (posterior insula pathway)
  → Precondition-4 hardware: CT afferent ~1-10cm/s = fixed range (không learned)
  → Precondition-5 N/A: hardware signals, no opioid/cortisol tag needed

  → Chi tiết type-split per precondition: Reward-Signal-Architecture §1.3

CLINICAL IMPLICATION:
  Evaluative bị block bởi Precondition-2/Precondition-3/Precondition-5 failures → anhedonia, burnout
  Direct-State KHÔNG bị block → "touch still works" = reliable baseline
  Mất CẢ HAI = rare + devastating (advanced depression, severe trauma)
```

### §1.3 — Falsifiability

🟡 Mỗi precondition tạo **testable prediction** khi bị violate:

| Violate | Prediction | Observable |
|---|---|---|
| Precondition-1 | Full person offered food → no reward | Alliesthesia research (Cabanac 1971) 🟢 |
| Precondition-2 | Van Gogh to untrained → confusion not reward | Art appreciation studies 🟢 |
| Precondition-3 | Routine event → no alert despite value | Hedonic adaptation literature 🟢 |
| Precondition-4 | Extreme novelty OR familiarity → no reward | Berlyne 1960 inverted-U 🟢 |
| Precondition-5 | Math-avoidant adult given "interesting" math → aversion | Clinical observation 🟢 |

**Framework prediction**: Cases "should reward but doesn't" = ít nhất 1 precondition bị fail.
Cases "shouldn't reward but does" = ALL 5 met nhưng observer chưa nhận ra.

### §1.4 — Precondition hierarchy

🟡 Từ Gap-Direction.md v2.0 §6.3 — preconditions có thứ bậc, không phải flat AND-gate:

```
"Chưa biết" → Precondition-2 → Precondition-1 → Precondition-3 → Precondition-4 → Precondition-5 → signal fire

Layer 0 (GENESIS):   "Chưa biết = không gap" — prerequisite cho Precondition-2
Layer 1 (SUBSTRATE):  Precondition-2 Chunk-Substrate — CÓ chunks để form gap?
Layer 2 (GAP):        Precondition-1 Directed-Gap — gap active + có direction?
Layer 3 (DETECTION):  Precondition-3 Delta-Gate — VTA detect delta?
Layer 4 (MATCH):      Precondition-4 Match-Range — match trong vùng phù hợp?
Layer 5 (DIRECTION):  Precondition-5 Compile-Gate — tag cho phép signal đúng hướng?

⭐ Hierarchy KHÔNG thay đổi "ALL 5 required" claim.
  → Nhưng CHO BIẾT failure mode nào xảy ra TRƯỚC.
  → Precondition-2 fail = Precondition-1 KHÔNG THỂ form (cho schema-level gaps).
  → Precondition-3 fail = Precondition-4 KHÔNG ĐƯỢC evaluate (sequential dependency).
```

---

## §2 — Precondition-1: Directed-Gap

### §2.1 — Definition

🟡 **Precondition-1 — Directed-Gap**:

> Body must have an **active gap** — an unresolved body-need OR schema seeking
> upgrade — AND that gap must have **direction** (toward what kind of fill).
>
> Gap = opening trong schema landscape where new information can fit.
> Direction = constraints on valid fill, determined by surrounding chunks.

**Tên cũ**: "Schema Pending Status" (drill 03-Reward.md §3.2)
**Đổi vì**: Tên cũ bỏ sót (a) hardware-driven gaps và (b) direction component.

### §2.2 — Precondition-1a: Hardware-driven gaps

🟢 Hardware-driven gaps = body-needs từ Body-Base:
- Hunger, thirst, pain avoidance, temperature, social contact, sleep
- LUÔN TỒN TẠI ở mức nào đó (homeostatic regulation)
- Infant từ sinh đã có — không cần learning
- Direction inherent: hunger → food direction, thirst → water direction

```
Đặc điểm Precondition-1a:
  ① Always available (homeostatic cycle)
  ② Direction = hardware-defined (specific body-need category)
  ③ Không cần Precondition-2 (chunks) — hardware path from birth
  ④ Intensity varies (satiated ↔ deprived)
  ⑤ → Chủ yếu cho DIRECT-STATE reward/dissonance
```

### §2.3 — Precondition-1b: Pattern-driven gaps

🟡 Pattern-driven gaps = schema-level needs:
- Coherence gap: incomplete knowledge, unresolved problem
- Curiosity gap: detected pattern hinting at more
- Skill gap: biết có thể làm tốt hơn nhưng chưa được
- Social gap: disconnection from expected social state

```
Đặc điểm Precondition-1b:
  ① Requires Precondition-2 first (phải có chunks mới có gap — §2.5)
  ② Direction = f(surrounding chunk network) (Gap-Direction.md §1.1)
  ③ Learned, not innate — develops through experience
  ④ Can be installed (education, marketing, social exposure)
  ⑤ → Chủ yếu cho EVALUATIVE reward/dissonance
```

**Ví dụ gap direction**:
- Nhạc sĩ nghe 1 đoạn → gap "giai điệu tiếp theo nên đi đâu?" = direction rõ
- Lập trình viên gặp bug → gap "nguyên nhân bug?" = direction hẹp
- Trẻ em chưa biết guitar tồn tại → gap KHÔNG THỂ TỒN TẠI (→ §2.5)

### §2.4 — Direction implicit

🟡 Từ Gap-Direction.md v2.0 §1.1:

> **Gap_Direction = f(surrounding_chunk_network_structure)**
>
> Shape of hole = constraints on valid fill.
> Chunks xung quanh gap QUY ĐỊNH direction.

**Tại sao direction quan trọng cho Precondition-1**:
- Gap KHÔNG direction = not really a gap (vague unease, not actionable)
- Direction cho biết LOẠI stimulus nào sẽ fill gap
- Direction quyết định Precondition-4 (Match-Range) evaluate match VỚI CÁI GÌ
- Thiếu direction → Precondition-4 không có reference point → signal không fire

```
Gap-Direction 4 properties (Gap-Direction.md §4):
  ① Direction — toward WHAT kind of fill
  ② Specificity — narrow (expert) vs broad (beginner)
  ③ Depth — signal strength (how much body "wants" fill)
  ④ Range — Goldilocks zone WITHIN that direction
```

### §2.5 — Precondition-2 → Precondition-1 dependency (schema-level)

🟡 Critical insight từ Gap-Direction.md §3:

> **"Chưa biết = không có gap"**
> Chunks_related_to_X = ∅ → Gap_about_X = IMPOSSIBLE
>
> Bạn KHÔNG THỂ thiếu thứ bạn không biết tồn tại.

**Implications**:
- Precondition-2 (Chunk-Substrate) là **prerequisite** cho Precondition-1b (Pattern-driven gap)
- Nếu Precondition-2 fail ở level genesis → Precondition-1b KHÔNG THỂ form
- Hardware Precondition-1a KHÔNG cần Precondition-2 (body-needs exist from birth)
- Đây là "Tầng 0" — trước cả precondition model

```
Precondition-2 → Precondition-1 dependency chain:
  ① Chưa có chunks về X → gap về X KHÔNG TỒN TẠI → Precondition-1 fail
  ② Có vài chunks về X → gap MƠ HỒ → Precondition-1 partial (direction broad)
  ③ Có nhiều chunks về X → gap RÕ RÀNG → Precondition-1 full (direction specific)

5 consequences (Gap-Direction.md §3.4):
  → Desire is CONSTRUCTED (not innate except hardware Tier 1)
  → Education phải BUILD chunks trước khi present answers
  → Marketing = gap installation (create chunks → create gap → sell fill)
  → Therapy phải MAP gap landscape (what gaps exist?)
  → Cross-cultural = different gap landscapes (different chunk bases)
```

### §2.6 — Precondition-1 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Satiated | Body-need filled → gap closed | "Không thèm" (no desire) |
| No active goal | Schema landscape stable | "Không cần gì" (contentment) |
| Empty scroll | Stimuli arrive, no gap matches | "Lướt mà không dừng" |
| Direction lost | Gap exists but surrounding chunks insufficient | "Muốn gì đó nhưng không biết gì" |

🟢 Research: Cabanac 1971 alliesthesia — same stimulus (sugar) shifts from
pleasant to unpleasant as body-need (hunger) gets filled. Precondition-1 failure = signal stops.

---

## §3 — Precondition-2: Chunk-Substrate

### §3.1 — Definition

🟡 **Precondition-2 — Chunk-Substrate**:

> Body must have **sufficient chunks** to (a) form gap about domain (genesis)
> AND (b) decode incoming stimulus for evaluation (decode).
>
> Chunks = compiled patterns from past experience (Chunk.md §2).
> Without chunks, body cannot even RECOGNIZE stimulus as relevant.

**Tên cũ**: "Chunks Base Adequacy" (drill 03-Reward.md §3.3)
**Đổi vì**: "Adequacy" mơ hồ. "Substrate" = nền tảng cần thiết, rõ nghĩa hơn.

### §3.2 — Precondition-2a: Genesis failure ("chưa biết = không gap")

🟡 Từ Gap-Direction.md §3 — TẦNG 0, trước cả precondition model:

> **Precondition-2a Genesis**: Chunks_related_to_X = ∅ → Gap KHÔNG THỂ TỒN TẠI
>
> Đây KHÔNG phải "stimulus đến mà không decode được" (= Precondition-2b).
> Đây là "gap về X CHƯA BAO GIỜ HÌNH THÀNH" — trước cả Precondition-1.

**Ví dụ Precondition-2a**:
- Trẻ 3 tuổi chưa biết guitar tồn tại → KHÔNG THỂ có gap "muốn chơi guitar"
- Người chưa bao giờ nghe jazz → KHÔNG THỂ có gap "muốn nghe jazz"
- Dân tộc chưa có khái niệm "thi cử" → KHÔNG THỂ có gap "muốn đỗ đạt"

```
Precondition-2a vs Precondition-2b — key distinction:
  Precondition-2a = TRƯỚC stimulus (gap không thể form → desire không tồn tại)
  Precondition-2b = SAU stimulus (stimulus đến nhưng không đủ chunks decode)
  Precondition-2a fail → Precondition-1 fail (no gap possible)
  Precondition-2b fail → confusion/strangeness (stimulus present but undecodable)
```

### §3.3 — Precondition-2b: Decode failure

🟡 Precondition-2b: Stimulus arrives but body **cannot decode** it:

> New input → unconscious searches for matching chunks → NO match found
> → "Cannot decode" → uncertainty → mild cortisol → NOT reward

**Ví dụ Precondition-2b**:
- Van Gogh shown to untrained viewer → chunks insufficient for art evaluation
  → "Không hiểu" (confusion, not reward) — even though painting objectively valuable
- Atonal music to pop listener → chunks insufficient for harmonic evaluation
  → "Lộn xộn" (confusion) — same music = masterpiece to trained listener
- Advanced mathematics to beginner → chunks insufficient for pattern recognition
  → "Không hiểu gì" — same proof = "beautiful" to mathematician

🟢 Research: Art appreciation studies confirm training → appreciation (Leder et al. 2004).
Mere exposure without understanding ≠ appreciation — chunk compilation required.

### §3.4 — Evaluative vs Direct-State

```
EVALUATIVE:
  Precondition-2 = REQUIRED — compiled chunks để evaluate pattern
  → Thiếu chunks = confusion → no reward
  → Van Gogh case = Precondition-2 failure (NOT Precondition-4)

DIRECT-STATE:
  Precondition-2 = MINIMAL — hardware paths from birth
  → CT afferents (touch), taste buds (sweet/bitter), nociceptors (pain)
  → Không cần compiled chunks — hardware decode đủ
  → Infant ngay từ sinh đã reward từ touch, sweetness
```

### §3.5 — Precondition-2 ≠ Precondition-5 distinction

```
⚠️ Precondition-2 và Precondition-5 KHÁC NHAU — cả hai liên quan chunks nhưng ở KHÁC layer:

  Precondition-2 Chunk-Substrate:
    Câu hỏi: CÓ ĐỦ chunks để DECODE stimulus không?
    Layer: SUBSTRATE — nền tảng
    Failure: confusion ("không hiểu")
    → Chunks EXIST or NOT

  Precondition-5 Compile-Gate:
    Câu hỏi: Chunks đã decode → tag CHO PHÉP signal đúng hướng không?
    Layer: DIRECTION — hướng signal
    Failure: signal wrong direction ("hiểu nhưng ghét")
    → Chunks exist BUT tagged approach/avoidance

  Ví dụ: Toán
    Precondition-2 fail: "Không hiểu toán" (insufficient chunks to decode)
    Precondition-5 fail: "Hiểu toán nhưng ghét toán" (chunks exist, tagged avoidance)
```

### §3.6 — Precondition-2 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Genesis (Precondition-2a) | No chunks about domain → gap impossible | "Không biết thứ đó tồn tại" |
| Decode (Precondition-2b) | Stimulus arrives, insufficient chunks to parse | "Không hiểu" / confusion |
| Partial decode | Some chunks match, insufficient for evaluation | "Lờ mờ hiểu nhưng chưa đủ" |
| Cross-domain gap | Chunks exist in domain A, not B — transfer fails | "Giỏi nhạc nhưng mù thơ" |

**Developmental trajectory** 🟡:
- Infant: minimal chunks → most stimuli = Precondition-2b fail → exploration critical
- Child: chunks accumulating → Precondition-2b failures narrow → domains opening
- Adult: rich chunk base → Precondition-2b rare in familiar domains → but still possible in NEW domains
- Expert: deep chunks in specialty → Precondition-2 = non-issue there → BUT may Precondition-2-fail in unfamiliar fields

🟢 Research: Expertise studies (Chi et al. 1981) — experts chunk patterns that novices cannot see.
Same chess board: grandmaster sees structure, novice sees random pieces = Precondition-2 difference.

---

## §4 — Precondition-3: Delta-Gate

### §4.1 — Definition

🟡 **Precondition-3 — Delta-Gate**:

> The change (delta) between current state and prediction must be **large enough**
> to exceed VTA habituation threshold, triggering dopamine alert.
>
> Precondition-3 answers: "Có gì MỚI không?" — detection mechanism, not value judgment.
> VTA dopamine = chuông cửa (doorbell). Precondition-3 = chuông CÓ KÊU không.

**Tên cũ**: "Prediction-Delta Threshold" (drill 03-Reward.md §3.4)
**Đổi vì**: "Delta-Gate" ngắn gọn hơn, nhấn mạnh tính gate (open/close).

### §4.2 — VTA habituation mechanism

🟡 Mechanism (03-Reward.md §2.2-§2.4, Step 2-3):

```
① VTA habituated to stable patterns → ignores familiar
② New input arrives → compare with prediction
③ Delta = |actual - predicted|
④ Delta > threshold → VTA fires dopamine → PFC attention triggered
⑤ Delta < threshold → VTA silent → no downstream processing

Threshold affected by:
  → Baseline arousal (cortisol level modulates sensitivity)
  → Recent history (nhiều delta liên tiếp → threshold tăng)
  → DRD4 variant (§4.5)
  → Domain expertise (expert detects finer deltas)
```

🟢 Research: Schultz 1997 — VTA dopamine neurons fire to unexpected rewards,
NOT to expected rewards. Response transfers to prediction cue after learning.
Prediction error signal = Precondition-3 mechanism.

### §4.3 — Scope: Evaluative ONLY

```
⭐ Precondition-3 chỉ áp dụng đầy đủ cho EVALUATIVE reward/dissonance.

EVALUATIVE:
  → Precondition-3 REQUIRED — VTA must detect delta
  → No delta → no alert → no downstream reward
  → Hedonic adaptation = Precondition-3 erosion over time

DIRECT-STATE:
  → Precondition-3 UNCERTAIN — may bypass VTA entirely
  → Posterior insula pathway: body-need → direct signal (no delta check)
  → Ví dụ: hungry person eats → reward fires WITHOUT needing "surprise"
  → Touch (CT afferents) → opioid release WITHOUT prediction error
  → Chi tiết: Reward-Signal-Architecture §1.3
```

### §4.4 — Boredom disambiguation

🟡 **Boredom ≠ Precondition-3 failure.** Từ Boredom.md v2.1 §1 + §7:

> Boredom = 2-dimensional state requiring 3 co-conditions:
> ① Gap exists (something wanted but absent)
> ② Gap unfilled (no available fill)
> ③ Signal below PFC threshold (too diffuse for action)
>
> Missing ANY single condition = NOT boredom.
> Missing ① = contentment. Missing ② = drive. Missing ③ = active emotion.

```
WHY boredom ≠ simple Precondition-3 failure:

  Precondition-3 failure alone = "no delta detected" → neutral, not bored
  → Routine events slip by unnoticed — NO dissonance, NO boredom

  Boredom requires Precondition-1 (gap EXISTS) + Precondition-4 (no suitable match available)
  → Body WANTS something (Precondition-1 met) but NOTHING matches (Precondition-4 fail)
  → Plus: signal too diffuse for PFC to commit action

  → Boredom = Precondition-1 met + Precondition-4 fail + PFC unclear = compound state
  → NOT = Precondition-3 fail (Precondition-3 fail = simply nothing detected)
```

### §4.5 — DRD4 modulation

🟡 DRD4 receptor variant (03-Reward.md §2.5, Step 3) modulates Precondition-3 DOWNSTREAM:

```
DRD4 = Step 3 FILTER, not Precondition-3 itself:
  → Precondition-3 = VTA fires dopamine (Step 2)
  → DRD4 = how dopamine is RECEIVED by target neurons (Step 3)

DRD4-7R ("novelty-seeking" variant):
  → Lower sensitivity → needs MORE delta for same response
  → Thresholds higher → routine feels MORE boring
  → BUT big delta → BIGGER response (amplified)

DRD4-4R (common variant):
  → Normal sensitivity → standard delta-response curve
  → Moderate novelty sufficient for reward

⚠️ DRD4 DOES NOT change Precondition-3 gate itself.
  → Precondition-3 = VTA detection. DRD4 = post-detection filtering.
  → Person with DRD4-7R: Precondition-3 fires normally, but downstream IMPACT differs.
```

🟢 Research: Ebstein et al. 1996 — DRD4-7R associated with novelty seeking.
Benjamin et al. 1996 — replicated. Meta-analyses: small but consistent effect.

### §4.6 — Precondition-3 → Precondition-4 sequential dependency

🟡 Precondition-3 must fire BEFORE Precondition-4 is evaluated:

```
Sequence:
  Precondition-3 fires (delta detected) → dopamine alert → PFC attention
  → THEN Precondition-4 evaluated (match quality assessed)

Precondition-3 fail → Precondition-4 NEVER CHECKED:
  → No delta → no alert → PFC doesn't attend → match quality irrelevant
  → Stimulus may be PERFECT match (Precondition-4 would pass) but Precondition-3 blocks detection

Precondition-3 pass → Precondition-4 CHECK:
  → Delta detected → attention → NOW evaluate: match trong vùng nào?
  → Precondition-4 pass → continue to Precondition-5
  → Precondition-4 fail → signal attenuated or wrong direction
```

### §4.7 — Precondition-3 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Habituation | Same pattern repeated → VTA adapts | "Chán" (hedonic treadmill) |
| Routine | Life predictable → few deltas | "Nhàm" (monotony) |
| Overstimulation | Too many deltas → threshold rises | "Tê liệt" (sensory overload) |
| Anhedonia (clinical) | VTA function impaired | "Không cảm gì" (depression symptom) |

**Hedonic adaptation cycle** 🟢:
```
Trial 1:   huge delta → reward intense
Trial 10:  moderate delta → reward moderate
Trial 100: small delta → reward mild
Trial 1000: near-zero delta → reward absent
→ SAME stimulus, DIFFERENT delta = DIFFERENT Precondition-3 outcome
→ This is prediction-delta erosion, NOT value change
```

🟢 Research: Frederick & Loewenstein 1999 — hedonic adaptation comprehensive review.
Brickman & Campbell 1971 — hedonic treadmill concept.

---

## §5 — Precondition-4: Match-Range

### §5.1 — Definition

🟡 **Precondition-4 — Match-Range**:

> Match between incoming pattern and gap direction must fall within
> a **suitable range** — not too alien, not too familiar.
>
> Precondition-4 answers: "Match có VỪA không?" — quality of fit, not just detection.
> Precondition-3 detects THAT something changed. Precondition-4 evaluates HOW WELL it fits.

**Tên cũ**: "Goldilocks Zone Position" (drill 03-Reward.md §3.5)
**Đổi vì**: (a) "Zone" bỏ sót direction-match component. (b) "40-70%" không cố định → "Range" = dynamic.
**Informal shorthand**: "Goldilocks zone" — used across framework as intuitive label for this precondition.

### §5.2 — Direction-match (not just magnitude)

🟡 Từ Gap-Direction.md v2.0 §6.3:

> Match VỚI CÁI GÌ? → Match với **gap direction**.
>
> Gap có direction = f(surrounding chunks).
> Precondition-4 evaluate: stimulus match DIRECTION + MAGNITUDE của gap.

```
Direction-match matters:

  ① Đúng direction + đúng range → reward (full match)
  ② Đúng direction + ngoài range → attenuated (too close or too far)
  ③ Sai direction + bất kỳ range → no reward (direction mismatch)

Ví dụ:
  Nhạc sĩ đang tìm giai điệu buồn (gap direction = melancholy)
  → Nhận được giai điệu buồn vừa đủ mới → reward ✅ (direction + range match)
  → Nhận được giai điệu vui → no reward ❌ (direction mismatch)
  → Nhận được giai điệu buồn nhưng quá phức tạp → confusion ❌ (range miss)
```

### §5.3 — Goldilocks zone (dynamic, not a fixed number)

🟡 Từ Reward-Calibration.md v1.1 §1.2:

> **Goldilocks zone**: novel enough to trigger + right direction to match gap.
> Dynamic per person / context / gap-type / time.
> The often-cited "40-70% match ratio" is a **rough approximation**, not a fixed threshold.
> Zone thay đổi theo 4 trục:

```
① PER-PERSON:
  COMT Val/Val → needs nhiều shallow rewards → zone rộng
  COMT Met/Met → needs ít deep rewards → zone hẹp
  DRD4-7R → higher threshold → zone shifted toward MORE novel
  (PFC-Hardware §3.4)

② PER-GAP-TYPE:
  Chunk-Shift → delta nhỏ đủ → zone rộng
  Chunk-Miss → delta trung bình → zone moderate
  Chunk-Gap → delta lớn cần thiết → zone hẹp
  (Body-Feedback-Mechanism.md §3)

③ PER-CONTEXT:
  Cortisol state: cao → zone thu hẹp (threat mode)
  Existing chunks: nhiều → zone narrow (expert) vs ít → zone wide (novice)
  Relationship: trusted source → zone wider (trust compile)
  Background pattern: stable → zone sensitive to small changes

④ PER-TIME:
  Baseline shift from repeated reward → zone dịch chuyển
  Developmental stage: child = wide zone, adult = narrower
  Habituation: trial 1 vs trial 100 = completely different zone
```

**Kết luận** (Reward-Calibration.md):
> "KHÔNG CÓ formula 'cho X reward cho gap Y' — Chỉ có OBSERVE + ADJUST liên tục."

### §5.4 — Expertise shift (E₀ → E₃)

🟡 Zone thay đổi theo expertise level:

```
E₀ (Zero exposure):
  → No chunks → Precondition-2 fail before Precondition-4 reached
  → Zone question irrelevant

E₁ (Beginner):
  → Few chunks → zone WIDE (nhiều thứ "mới + vừa đủ match")
  → Dễ reward, nhưng quality thấp
  → Ví dụ: mới học guitar, bấm được 1 hợp âm → reward!

E₂ (Intermediate):
  → Many chunks → zone NARROWS (phải tinh tế hơn mới "đủ mới")
  → Reward harder to trigger, nhưng quality cao hơn
  → Ví dụ: chơi guitar 5 năm, cần kỹ thuật mới mới "interesting"

E₃ (Expert):
  → Deep rich chunks → zone VERY NARROW + SHIFTED
  → Only subtle, refined differences trigger reward
  → BUT when triggered → very deep reward (rich chunk network activated)
  → Ví dụ: nghệ sĩ 30 năm, chỉ nuance tinh tế mới "wow"

Pattern: expertise NARROWS zone + SHIFTS toward subtlety
  → CÙNG stimulus: beginner rewards, expert bored (or vice versa)
  → Van Gogh: beginner = Precondition-2 fail, art student = Precondition-4 zone match, expert = Precondition-4 too familiar
```

🟢 Research: Training gradient in music appreciation (North & Hargreaves 1995).
Zajonc 1968 mere exposure — preference peaks then declines with overexposure.
Berlyne 1960 — inverted-U arousal × complexity.

### §5.5 — Failure asymmetry: reward vs dissonance

🟡 Precondition-4 failure khác nhau cho reward và dissonance:

```
REWARD Precondition-4 failure:
  Too alien → confusion (Precondition-2 boundary)
  Too familiar → boredom (habituation)
  Direction mismatch → indifference

DISSONANCE Precondition-4 "failure" (i.e., dissonance does NOT fire):
  Too alien → actually MAY still fire dissonance (threat response)
  Too familiar → dissonance attenuated (habituated mismatch accepted)
  → Asymmetry: alien stimuli → reward BLOCKED but dissonance ENHANCED

⚠️ Dissonance has LOWER threshold than reward:
  → Threat detection favors false positives (evolutionary advantage)
  → → Precondition-4 zone for dissonance is WIDER than for reward
  → → Easier to trigger dissonance than reward from same mismatch
  → Chi tiết: Dissonance-Signal-Architecture.md, §9 this file
```

### §5.6 — Precondition-4 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Too alien | Match < lower bound → cannot evaluate | "Quá lạ, không hiểu" |
| Too familiar | Match > upper bound → habituated | "Quá quen, không còn gì mới" |
| Direction mismatch | Stimulus matches wrong gap direction | "Không phải cái tôi tìm" |
| Zone shifted | Expertise/context changed zone → stimulus no longer fits | "Hồi trước hay, giờ chán" |

---

## §6 — Precondition-5: Compile-Gate

### §6.1 — Definition

🟡 **Precondition-5 — Compile-Gate**:

> Chunks being activated must have **appropriate association tag** that permits
> signal to fire in the expected direction. Tag compiled at formation time
> persists through retrieval and determines signal DIRECTION + QUALITY.
>
> Precondition-5 answers: "Tag CHO PHÉP không?" — direction gate, not substrate check.

**Tên cũ**: "Chunk Association Tag" (drill 03-Reward.md §3.6)
**Đổi vì**: (a) "Association Tag" mô tả mechanism, không mô tả function.
(b) "Compile-Gate" nhấn mạnh: tag được compile vào chunk → gate quyết định direction.

### §6.2 — Scope: Evaluative ONLY

```
⭐ Precondition-5 CHỈ áp dụng cho EVALUATIVE reward/dissonance.

EVALUATIVE:
  → Precondition-5 REQUIRED — chunks' tag determines signal direction
  → Approach-tagged → opioid pathway → genuine reward
  → Avoidance-tagged → cortisol pathway → discomfort despite understanding
  → Quality ceiling depends on tag (§6.4)

DIRECT-STATE:
  → Precondition-5 = N/A — hardware signals, no tag needed
  → CT afferents fire opioid directly (no compiled tag)
  → Taste buds signal directly (sweet → approach, bitter → avoid)
  → Hardware "tag" = hardwired, not compiled
  → Chi tiết: Reward-Signal-Architecture §1.3

⚠️ Precondition-5 = N/A là ONLY precondition completely absent in Direct-State.
  (Precondition-3 is "uncertain", others are "simplified" — Precondition-5 is clean N/A.)
```

### §6.3 — Direction-At-Compile gate model

🟡 Từ Cortisol-Baseline.md v2.2 §3.3 — tag không binary (opioid/cortisol) mà là **gradient**:

> Tại compile time: cortisol level + body-state direction
> → determines tag on resulting chunk.
> Key insight: "cortisol assigned DIRECTION — direction matters more than level."

```
4-Threshold Gradient (Cortisol-Baseline.md §3.3):

  ┌───────────┬──────────────────┬───────────────────────────────────┐
  │ Threshold │ threat:novelty   │ Tag outcome                       │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Light     │ ~60:40           │ Mild cortisol + opioid anticipation│
  │           │                  │ Tag: "ok, tolerable"               │
  │           │                  │ Easy to update later               │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Moderate  │ ~80:20           │ Moderate cortisol, little opioid   │
  │           │                  │ Tag: "unpleasant"                  │
  │           │                  │ Update needs time                  │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Heavy     │ ~95:5            │ Strong cortisol, deep fear compiled│
  │           │                  │ Tag: extremely hard to update      │
  ├───────────┼──────────────────┼───────────────────────────────────┤
  │ Extreme   │ Trauma           │ Body refuses to use chunk          │
  │           │                  │ Net negative value                 │
  │           │                  │ Avoidance = only possible response │
  └───────────┴──────────────────┴───────────────────────────────────┘

⭐ CÙNG cortisol level, KHÁC source:
  Novelty cortisol (curious but tense) → chunk tagged APPROACH
  Threat cortisol (afraid) → chunk tagged AVOIDANCE
  → SOURCE > LEVEL (Cortisol-Baseline.md §7)
```

### §6.4 — 4-Pathway × quality ceiling

🟡 Từ Compile-Taxonomy.md v2.0 §3:

> Mỗi compile pathway tạo KHÁC Precondition-5 tag → determines reward capacity:

```
┌──────────────────────┬───────────────────┬────────────────────────────┐
│ Pathway              │ Precondition-5 Tag            │ Reward ceiling              │
├──────────────────────┼───────────────────┼────────────────────────────┤
│ ① Hardware Fit       │ Approach          │ HIGHEST — natural coherence │
│   (direct experience │                   │ Flow accessible             │
│    in Goldilocks)    │                   │ Sustainable engagement      │
├──────────────────────┼───────────────────┼────────────────────────────┤
│ ② Trust + Moderate   │ Moderate approach │ MODERATE — depends on       │
│   (trusted source +  │                   │ collective chain quality    │
│    partial verify)   │                   │ Can upgrade with experience │
├──────────────────────┼───────────────────┼────────────────────────────┤
│ ③ Social Default     │ Neutral           │ LOW — relief dominant       │
│   (consensus, "mọi  │                   │ "Done" > "Interesting"      │
│    người đều làm")   │                   │ PFC confabulation ~30%     │
├──────────────────────┼───────────────────┼────────────────────────────┤
│ ④ Threat Avoidance   │ Avoidance         │ LOWEST — relief ONLY        │
│   (fear-driven       │                   │ Never genuine engagement    │
│    compliance)       │                   │ Burnout trajectory          │
└──────────────────────┴───────────────────┴────────────────────────────┘

⭐ Precondition-5 tag at childhood compile → PERSISTS → constrains ADULT reward profile.
  "Giỏi mà không thích" = Precondition-5 fail (understand but avoidance-tagged).
  Pathway ④ = giải thích tại sao nhiều người "thành công nhưng không hạnh phúc."
```

### §6.5 — Re-association 3 paths

🟡 Precondition-5 tag CAN change, nhưng tốn resources (Cortisol-Baseline.md §7.6):

```
3 Re-association Paths:

  Path 1: NEW POSITIVE CONTEXT (months → years)
    → Cùng domain, new positive experiences
    → Gradually overlay approach tag onto avoidance-tagged chunks
    → Slowest nhưng most robust
    → Ví dụ: math-phobic adult finds good teacher → years → "math ok"

  Path 2: NOVELTY HIJACK (weeks → months)
    → Completely new angle/context for same domain
    → Bypass old chunks → build new approach-tagged chunks
    → Old avoidance chunks still exist BUT new chunks dominate
    → Ví dụ: learn math through music → new chunks, new tag

  Path 3: AI SUPPORT (weeks — 🔴 hypothesis level)
    → AI provides perfectly calibrated Goldilocks stimuli
    → Consistent positive experiences accumulate faster
    → Tag shift accelerated by controlled exposure
    → ⚠️ Hypothesis level — not yet validated

⭐ Key: re-association = OVERLAY, not deletion.
  Old avoidance-tagged chunks still exist.
  New approach-tagged chunks added.
  Which set DOMINATES = f(recency, frequency, context).
```

### §6.6 — Precondition-5 ≠ Precondition-2 distinction (restated)

```
Summary distinction:

  Precondition-2 Chunk-Substrate:  CAN you decode? (existence of chunks)
  Precondition-5 Compile-Gate:     WHAT DIRECTION does decoded signal go? (tag on chunks)

  Precondition-2 fail: "Tôi không hiểu bài toán này" (no chunks to decode)
  Precondition-5 fail: "Tôi hiểu bài toán này nhưng ghét toán" (chunks exist, tagged avoid)

  Precondition-2 fix: LEARN (accumulate chunks) — education problem
  Precondition-5 fix: RE-ASSOCIATE (change tag) — much harder, emotional rewiring

  Precondition-2 is about SUBSTRATE (does the foundation exist?)
  Precondition-5 is about DIRECTION (which way does the signal flow?)
```

### §6.7 — Precondition-5 failure modes

| Failure type | Mechanism | Subjective experience |
|---|---|---|
| Threat-tagged | Chunks compiled under fear → avoidance direction | "Ghét dù biết hay" |
| Social-default | Chunks compiled via consensus → relief only | "Làm xong là mừng, không hào hứng" |
| Mixed-tag | Some chunks approach + some avoidance → ambivalent | "Vừa thích vừa sợ" |
| Trauma-tagged | Extreme compile → body refuses chunk activation | "Không thể nghĩ đến" (avoidance) |

**Thiên tài paradox** (03-Reward.md §3.6):
```
Newton/Tesla/Einstein: high baseline cortisol
  → BUT: learning-domain chunks compiled in CURIOSITY state
  → Threat source ≠ learning domain → Precondition-5 tag = approach in learning
  → Reward accessible in learning domain DESPITE high overall cortisol

Key: threat SOURCE matters, not threat LEVEL.
  → Person stressed about money can still enjoy music (different domain)
  → Person stressed about music cannot enjoy music (same domain)
  → Precondition-5 tag is DOMAIN-SPECIFIC, not global
```

🟢 Research: Cortisol effects on learning are direction-dependent (Lupien et al. 2007).
Same cortisol level → enhanced OR impaired memory depending on context and timing.

---

## §7 — Conjunction Logic + Failure Mode Table

### §7.1 — AND-gate structure

🟡 **Core logic**: Signal fires if and only if Precondition-1 ∧ Precondition-2 ∧ Precondition-3 ∧ Precondition-4 ∧ Precondition-5.

> Preconditions hoạt động như AND-gate — thiếu BẤT KỲ 1 → signal không fire đầy đủ.
> KHÔNG có precondition nào compensate cho precondition khác.
> Precondition-2 (chunks) KHÔNG bù cho Precondition-5 (tag). Precondition-3 (delta) KHÔNG bù cho Precondition-1 (gap).

```
Full signal (reward hoặc dissonance):
  Precondition-1 ✅ + Precondition-2 ✅ + Precondition-3 ✅ + Precondition-4 ✅ + Precondition-5 ✅ → FULL SIGNAL

Partial cases:
  4/5 met → signal ATTENUATED (reduced, not zero)
  3/5 met → signal WEAK (barely perceptible)
  2/5 met → signal ABSENT (no subjective experience)
  1/5 met → NOTHING

⚠️ "Attenuated" ≠ "absent":
  → Near-miss cases tạo ra MILD signal ("gần hay", "hơi thú vị")
  → Framework prediction: mild reward = 1 precondition BARELY failing
  → Clinical: chronic mild anhedonia = 1 precondition chronically weak
```

### §7.2 — Dependencies between preconditions

🟡 Preconditions KHÔNG flat — có thứ bậc dependency (§1.4):

```
DEPENDENCY 1: Precondition-2 → Precondition-1 (schema-level)
  Precondition-2 (chunks) phải tồn tại TRƯỚC khi Precondition-1b (schema gap) có thể form.
  "Chưa biết = không gap" → Precondition-2a fail = Precondition-1b impossible.
  ⚠️ Precondition-1a (hardware) KHÔNG cần Precondition-2 → body-needs exist from birth.

DEPENDENCY 2: Precondition-3 → Precondition-4 (sequential)
  Precondition-3 (delta detected) phải fire TRƯỚC khi Precondition-4 (match quality) được evaluate.
  Precondition-3 fail → PFC không attend → Precondition-4 không được check → Precondition-4 irrelevant.
  ⚠️ Stimulus có thể PERFECT match (Precondition-4 pass) nhưng Precondition-3 blocks detection.

NO OTHER DEPENDENCIES:
  Precondition-5 independent of Precondition-3/Precondition-4 (tag compiled at formation, not at evaluation)
  Precondition-1 independent of Precondition-3 (gap exists before delta detection)
  Precondition-4 independent of Precondition-5 (match quality separate from tag direction)
```

### §7.3 — Per-precondition failure → specific outcome

🟡 Mỗi precondition failure tạo ra **distinct** subjective experience:

| Precondition-fail | Others met | Outcome | Typical phrase |
|---|---|---|---|
| Precondition-1 | Precondition-2–Precondition-5 ✅ | No desire → signal irrelevant | "Không thèm", "Đủ rồi" |
| Precondition-2 | Precondition-1, Precondition-3–Precondition-5 ✅ | Confusion → cannot evaluate | "Không hiểu", "Lạ quá" |
| Precondition-3 | Precondition-1, Precondition-2, Precondition-4, Precondition-5 ✅ | Unnoticed → attention not triggered | "Bình thường", "Quen rồi" |
| Precondition-4 | Precondition-1–Precondition-3, Precondition-5 ✅ | Wrong range → too alien or too familiar | "Quá khó" / "Quá dễ" |
| Precondition-5 | Precondition-1–Precondition-4 ✅ | Wrong direction → aversion despite understanding | "Hiểu nhưng ghét" |

**Diagnostic power**: Knowing WHICH precondition failed → biết CHÍNH XÁC cách fix.
- Precondition-1 fail → create/activate gap (education, exposure, need induction)
- Precondition-2 fail → build chunks (training, scaffolding, prerequisite learning)
- Precondition-3 fail → introduce variation (change context, angle, presentation)
- Precondition-4 fail → calibrate difficulty (simpler for too-alien, harder for too-familiar)
- Precondition-5 fail → re-associate tags (new context, positive overlay — §6.5)

### §7.4 — Chunk dynamics × preconditions

🟡 Body-Feedback-Mechanism.md §6.2 maps chunk dynamics (Shift/Miss/Gap) × Precondition-1–Precondition-5:

```
⭐ KEY INSIGHT: Chunk dynamics ≠ preconditions, nhưng INTERACT.

  Chunk-Shift:
    Precondition-1 = shift CREATES new pending (e.g. betrayal creates need to fix)
    Precondition-2 = needs chunks to evaluate new info
    Precondition-3 = shift = valence delta (inherent)
    Precondition-4 = shift occurs at ANY match level
    Precondition-5 = NEW valence tag from shift event

  Chunk-Miss:
    Precondition-1 = miss = body-need loses quality
    Precondition-2 = needs compiled baseline (no compile = no miss)
    Precondition-3 = miss = negative prediction error
    Precondition-4 = N/A (body already KNOWS — no Goldilocks needed)
    Precondition-5 = compiled baseline carries tag

  Chunk-Gap:
    Precondition-1 = gap = body-need lacks pattern
    Precondition-2 = needs enough chunk network to DETECT gap
    Precondition-3 = gap detect = ACC signal
    Precondition-4 = gap must be detectable (not too alien)
    Precondition-5 = surrounding compiled chunks carry tag

  → Chi tiết: Body-Feedback-Mechanism.md §6.2

⚠️ Compound dynamics = Precondition-1–Precondition-5 checked MULTIPLE TIMES per event.
  Ví dụ: bị bạn thân lừa → Shift (betrayal) + Miss (trust lost) + Gap (how to fix?)
  → Mỗi dynamic triggers Precondition-1–Precondition-5 check riêng → compound signal
```

### §7.5 — Multi-precondition failure combinations

🟡 Khi NHIỀU preconditions fail đồng thời:

```
Precondition-1 + Precondition-3 co-fail:
  No gap + no delta → COMPLETE INDIFFERENCE
  → Ví dụ: scrolling social media while satiated — nothing registers

Precondition-1 + Precondition-4 co-fail:
  Gap exists but nothing matches → BOREDOM (Boredom.md §7)
  → Body WANTS (Precondition-1) but nothing FITS (Precondition-4) + signal too diffuse
  → ⚠️ Boredom = Precondition-1 met + Precondition-4 fail, NOT simple Precondition-3 fail

Precondition-2 + Precondition-4 co-fail:
  Insufficient chunks + wrong range → OVERWHELM
  → Ví dụ: advanced lecture to complete beginner

Precondition-3 + Precondition-5 co-fail:
  No delta + wrong tag → STAGNANT AVERSION
  → Ví dụ: forced daily math by math-phobic person
  → Habituated (Precondition-3 fail) + avoidance-tagged (Precondition-5 fail) → chronic low-grade suffering

Precondition-1 + Precondition-2 + Precondition-3 co-fail:
  No gap + no chunks + no delta → EMPTINESS
  → Nothing wanted, nothing understood, nothing new → existential boredom
```

---

## §8 — Developmental Arc

### §8.1 — Infant (0-2 years)

🟡 Infant precondition profile:

```
Precondition-1: ✅ Precondition-1a AVAILABLE from birth (body-needs: hunger, warmth, social contact)
    ❌ Precondition-1b NOT YET (schema gaps require chunks that don't exist yet)
    → Infant reward = almost entirely Direct-State

Precondition-2: ⚠️ THE BOTTLENECK — near-zero chunks at birth
    → Most stimuli = Precondition-2b fail → "everything is strange"
    → Chunks compile rapidly via 4+1 channels:
      Direct experience, emotional peak, multi-modal, sleep consolidation,
      external installation (caregiver)
    → Precondition-2 is PRIMARY developmental axis in infancy

Precondition-3: ✅ PRESENT but unfocused
    → Everything is novel → delta continuously high
    → BUT: so many deltas → threshold competition → attention scattered
    → Orienting response (Sokolov 1963) = Precondition-3 in its most basic form 🟢

Precondition-4: ⚠️ NARROW — few existing chunks = most inputs outside match range
    → Wide zone in theory, but few chunks to match WITH
    → Simple stimuli (faces, voices, rhythms) fit → reward accessible
    → Complex stimuli → Precondition-2 fail before Precondition-4 reached

Precondition-5: ⚠️ ENTIRELY DEPENDENT ON CAREGIVING
    → Tags installed via social referencing + caregiver emotional state
    → Caregiver curious while exposing → approach tag
    → Caregiver anxious while exposing → avoidance tag
    → ⭐ Precondition-5 in infancy = CAREGIVER responsibility, not child's
```

🟢 Research: Social referencing (Sorce et al. 1985) — infants use caregiver
facial expressions to tag novel stimuli as approach/avoid.

### §8.2 — Child (2-12 years)

🟡 Chunk accumulation + tag compilation phase:

```
Precondition-1: Precondition-1b DEVELOPING — schema gaps form as chunk network grows
    → "Muốn biết tại sao" (curiosity gaps) emerge ~age 3-4
    → Social gaps (acceptance, status) emerge ~age 5-7
    → Direction becomes more specific with experience

Precondition-2: RAPID EXPANSION
    → Chunks compile via experience + education + social learning
    → Domain-specific: rich chunks in play/social, fewer in academic (initially)
    → Precondition-2 bottleneck loosens → more stimuli decodable → more rewards accessible

Precondition-3: FUNCTIONAL — novelty detection well-established
    → BUT: attention systems still developing (PFC immature)
    → High DRD4 expression in childhood → lower threshold → MORE novelty-seeking
    → → Children NEED more stimulation (not "hyperactive" — developmentally normal)

Precondition-4: WIDE ZONE — relatively few chunks → large range of stimuli feel "new enough"
    → Easy to reward → exploration phase
    → Zone gradually narrows with expertise accumulation

Precondition-5: ⭐ CRITICAL PERIOD — tags compiling from emotional context
    → Same content taught under curiosity vs fear → OPPOSITE lifelong trajectories
    → Compile-Taxonomy.md: 4 pathways (HwFit/Trust/Social/Threat)
    → Childhood Precondition-5 tags PERSIST into adulthood and constrain adult reward
    → ⚠️ "Education is Precondition-5 programming" — emotional context matters as much as content
```

### §8.3 — Adult (12+ years)

🟡 Full operational profile:

```
Precondition-1: FULL RANGE — both Precondition-1a (hardware) and Precondition-1b (schema) operational
    → Complex gap landscapes: career, relationship, identity, meaning
    → Direction highly specific in expert domains

Precondition-2: DOMAIN-DIFFERENTIATED
    → Rich chunks in familiar domains → Precondition-2 non-issue
    → Sparse chunks in unfamiliar domains → Precondition-2 fail still possible
    → Expert vs novice = SAME stimulus, DIFFERENT Precondition-2 outcome

Precondition-3: HABITUATION becomes primary challenge
    → Daily routine → delta erosion → reward fades despite objective quality
    → Hedonic adaptation: same job, same relationship → Precondition-3 erodes
    → Counter: deliberate variation, new challenges, travel

Precondition-4: NARROWED + SHIFTED by expertise
    → Expert zone narrow → only subtle refinements trigger reward
    → Beginner zone in new domains → wide → easy rewards
    → Cross-domain exploration = Precondition-4 reset strategy

Precondition-5: ACCUMULATED BIOGRAPHICAL TAGS
    → Childhood compilations persist: "giỏi mà ghét" patterns established
    → Re-association possible but costly (months-years, §6.5)
    → Professional competence ≠ enjoyment (Precondition-5 fail common in adults)
    → "Burnout" often = Precondition-3 (no delta) + Precondition-5 (avoidance tag accumulation)
```

### §8.4 — Aging + burnout

🟡 Erosion patterns:

```
Precondition-1: WEAKENS — body-needs reduce (lower drive baseline)
    → Curiosity gaps may narrow (fewer active schemas)
    → Social gaps may intensify OR diminish (isolation vs acceptance)

Precondition-2: DOMAIN DECAY — chunks in neglected areas atrophy
    → "Schema portfolio neglect" (04-Integration.md §5.5)
    → Work chunks hypertrophy, hobby/relationship chunks decay
    → Rebuilding decayed chunks takes months-to-years

Precondition-3: ERODES — long-term habituation + reduced VTA sensitivity
    → Same environment for decades → deep habituation
    → Neurobiological: VTA dopamine function declines with age 🟢
    → Counter: novel experiences, learning new skills, travel

Precondition-4: CAN RE-WIDEN — if person enters new domain
    → Retirement + new hobby → beginner zone → Precondition-4 wide → rewards accessible again
    → "Second wind" phenomenon = Precondition-4 reset in new domain

Precondition-5: CORTISOL ACCUMULATION — life stress compounds avoidance tags
    → Chronic work stress → work chunks tagged avoidance
    → "Competent but aversive" = burnout hallmark
    → Late-life re-association harder but possible (Path 1 slow overlay)

BURNOUT FORMULA (compound):
  Precondition-3 erosion (habituated) + Precondition-5 avoidance (stress-tagged) + Precondition-1 weak (gap unclear)
  → "Không muốn, không thích, không biết muốn gì" = triple precondition failure
```

🟢 Research: Dopamine system aging (Bäckman et al. 2006).
Burnout and reward system (Sokka et al. 2017 — reduced reward anticipation in burnout).

---

## §9 — Dissonance Application

### §9.1 — Precondition-1–Precondition-5 apply to dissonance, not just reward

🟡 Precondition model là **body-feedback** model, không chỉ reward model:

> Body-feedback signal = reward OR dissonance.
> Precondition-1–Precondition-5 quyết định signal CÓ fire không — cho CẢ HAI hướng.
> Nhưng preconditions hoạt động KHÁC cho dissonance vs reward.

```
REWARD firing: Precondition-1–Precondition-5 all met → opioid pathway → approach signal
DISSONANCE firing: Precondition-1–Precondition-5 met but in NEGATIVE direction → cortisol pathway → avoidance signal

Key difference: DIRECTION of match, not presence of preconditions.
  Precondition-1: gap exists (same for both — need drives signal)
  Precondition-2: chunks exist to decode (same — substrate required)
  Precondition-3: delta detected (same — change needed)
  Precondition-4: match is NEGATIVE direction → dissonance fires
  Precondition-5: tag determines signal QUALITY (not just direction)
```

### §9.2 — Precondition-5 inverted: threat-tag × dissonance

🟡 Precondition-5 works INVERSELY for dissonance compared to reward:

```
REWARD:
  Approach-tagged chunks → opioid → full reward (ceiling HIGH)
  Avoidance-tagged chunks → blocked → reward limited (ceiling LOW)

DISSONANCE:
  Avoidance-tagged chunks → cortisol AMPLIFIED → dissonance threshold LOWER
  Approach-tagged chunks → cortisol DAMPENED → dissonance threshold HIGHER

→ Threat-tagged chunks make dissonance EASIER to fire, not harder.
→ Same mismatch: approach-tagged domain → mild dissonance
                  avoidance-tagged domain → intense dissonance

Ví dụ:
  Musician (approach-tagged) makes mistake → mild dissonance, quickly resolved
  Math-phobic adult (avoidance-tagged) makes math error → intense dissonance, slow to resolve
  → SAME type of error, DIFFERENT Precondition-5 tag → DIFFERENT dissonance intensity
```

### §9.3 — Asymmetric transition speed

🟡 Từ Dissonance-Signal-Architecture §7.5 — reward → dissonance vs dissonance → reward:

```
REWARD → DISSONANCE: FAST
  → Amygdala ~12ms bypasses PFC
  → Opioid off in seconds
  → Threat detection = survival priority
  → Ví dụ: enjoying music → sudden loud noise → instant dissonance

DISSONANCE → REWARD: SLOW
  → Cortisol half-life ~60-90 minutes
  → Opioid RE-activation requires FULL H10 re-check (all 5 preconditions)
  → PFC must re-assess safety before releasing opioid gate
  → Ví dụ: stressful exam → relief → takes minutes-hours, not seconds

⭐ Asymmetry resides in EVALUATIVE layer specifically.
  Direct-State is relatively symmetric (pain stops → relief fast).
  Evaluative adds "precondition re-verification" delay.
```

🟢 Research: Negativity bias (Baumeister et al. 2001, Rozin & Royzman 2001).
Loss aversion (Kahneman & Tversky 1979) — losses loom ~2× larger than gains.
Evolutionary logic: missing threat = death (max cost), false alarm = low cost.

### §9.4 — Evaluative gates

🟡 Từ Dissonance-Signal-Architecture §3 — evaluative layer GATES direct-state dissonance:

```
Evaluative gates can:
  ① AMPLIFY — nocebo effect (expecting pain → more pain)
  ② SUPPRESS — placebo effect (expecting relief → less pain)
  ③ ABSENT — infant/dissociation (no evaluative layer active)
  ④ CONFLICT — "pain from loved one" (mismatch between signal directions)

→ Precondition-1–Precondition-5 for dissonance: evaluative gates modulate INTENSITY, not just presence.
→ Same physical stimulus: different evaluative context → different dissonance level.
→ Chi tiết mechanism: Dissonance-Signal-Architecture.md §3
```

🟢 Research: Placebo analgesia (Wager et al. 2004). Nocebo hyperalgesia (Zubieta et al. 2005).
Craig 2002/2009 — insula gradient model for interoception.

---

## §10 — Honest Assessment

### §10.1 — Confidence per precondition

| # | Precondition | Confidence | Basis |
|---|---|---|---|
| Precondition-1 | Directed-Gap | 🟢 HIGH | Satiety/motivation research extensive. Alliesthesia. |
| Precondition-2 | Chunk-Substrate | 🟢 HIGH | Expertise/training studies. Chi et al. 1981. Art appreciation. |
| Precondition-3 | Delta-Gate | 🟢 HIGH | VTA prediction error well-established. Schultz 1997. |
| Precondition-4 | Match-Range | 🟡 MODERATE | Inverted-U supported (Berlyne 1960). Dynamic zone = framework claim. |
| Precondition-5 | Compile-Gate | 🟡 MODERATE | Cortisol × learning direction-dependent 🟢. 4-pathway model = framework. |
| ALL | Conjunction | 🟡 MODERATE | Each Precondition individual 🟢, but "ALL 5 required" = framework-level claim. |

### §10.2 — Open questions

```
Q1: Precondition-3 × Precondition-4 interaction boundary
  Khi Precondition-3 (delta) rất lớn, Precondition-4 (match) có bị bypass không?
  Ví dụ: extreme surprise → reward regardless of match quality?
  → Hiện tại: framework says NO (Precondition-4 still required)
  → Nhưng: extreme delta cases chưa studied rigorously

Q2: Precondition-5 re-association speed
  Path 3 (AI support) accelerates re-association — to what degree?
  → Hypothesis level (🔴). No empirical validation yet.
  → Nếu AI CAN accelerate → educational implications massive

Q3: Direct-State Precondition-3 mechanism
  Does Direct-State bypass VTA entirely or use different threshold?
  → Reward-Signal-Architecture §1.3 marks Precondition-3 as "UNCERTAIN" for Direct-State
  → Posterior insula pathway hypothesized but not fully mapped

Q4: Dissonance precondition thresholds
  Are dissonance Precondition-1–Precondition-5 thresholds LOWER than reward Precondition-1–Precondition-5?
  → Evolutionarily predicted (negativity bias)
  → But: quantitative threshold comparison not available

Q5: Compound dynamics × precondition cycling
  When compound event triggers Shift + Miss + Gap simultaneously,
  do preconditions get checked 3× independently? Or integrated?
  → Body-Feedback-Mechanism §6.2 suggests independent, but mechanism unclear
```

### §10.3 — Falsifiable predictions

🟡 If Body-Feedback Precondition model is correct:

```
PREDICTION 1: "Should reward but doesn't" cases
  → ALWAYS traceable to specific Precondition-failure
  → If ANY case found where ALL 5 met but NO reward → model falsified

PREDICTION 2: Precondition-5 re-association observable
  → Person with avoidance-tagged domain + positive re-exposure
  → Should show gradual tag shift → measurable via fMRI/EEG

PREDICTION 3: Precondition-2a genesis testable
  → Expose subject to completely novel domain → measure desire BEFORE vs AFTER
  → Before chunks: no desire. After chunks: desire possible.
  → Gap formation should correlate with chunk accumulation

PREDICTION 4: Precondition-3 → Precondition-4 sequential
  → Subliminal stimulus (below Precondition-3 threshold) that would match Precondition-4
  → Should produce NO reward (Precondition-3 blocks before Precondition-4 evaluated)
  → Testable with masked priming paradigms

PREDICTION 5: Developmental Precondition-5 testable
  → Same content taught under curiosity vs fear conditions
  → Approach/avoidance tags should persist → measurable years later
  → Partially supported by education research 🟢
```

---

## §11 — Cross-References

### §11.1 — Primary sources (drill origin)

| File | Relevant section | Relationship |
|---|---|---|
| 03-Reward.md v1.1 | §3 H10 Core | DRILL ORIGIN — this file formalizes §3 |
| 04-Integration.md | §9 H10 refined | DRILL INTEGRATION — cross-validated cases |

### §11.2 — Sibling files (Body-Feedback system)

| File | Relevant section | What it covers (this file cross-refs) |
|---|---|---|
| Body-Feedback.md v2.0 | §5.2 | H10 summary table (48 lines, pointer to this file) |
| Body-Feedback-Mechanism.md v2.1 | §6.2 | Chunk dynamics × Precondition-1–Precondition-5 mapping (§7.4) |
| Body-Feedback-Label.md v2.1 | — | Vocabulary reference (terminology) |
| Reward-Signal-Architecture.md v2.1 | §1.3 | Evaluative/Direct-State × Precondition-1–Precondition-5 table (§1.2) |
| Dissonance-Signal-Architecture.md v1.0 | §3, §7.5 | Evaluative gates + asymmetric transition (§9) |

### §11.3 — Refinement sources

| File | Relevant section | What refined |
|---|---|---|
| Gap-Direction.md v2.0 | §3, §6.3 | Precondition-1 direction + "chưa biết = không gap" + hierarchy |
| Cortisol-Baseline.md v2.2 | §3.3, §7 | Precondition-5 Direction-At-Compile gradient + source > level |
| Compile-Taxonomy.md v2.0 | §3 | Precondition-5 4-pathway × quality ceiling |
| Reward-Calibration.md v1.1 | §1.2 | Precondition-4 Goldilocks zone (dynamic, not fixed number) |
| Boredom.md v2.1 | §1, §7 | Precondition-3 boredom disambiguation |
| Chunk.md v2.2 | §2.6 | Precondition-2 substrate + context-tag |

### §11.4 — Developmental sources

| File | Relevant section | What informed |
|---|---|---|
| Child-Development-Mechanism.md | §2.3 | Infant precondition profile (§8.1) |
| 04-Integration.md | §5.5, §5.6, §7 | Aging + burnout erosion (§8.4) |

### §11.5 — Precondition name mapping (from drill)

```
┌──────────────────────────────┬──────────────────────────────────┐
│ Drill name (H10)             │ Formal name (this file)          │
├──────────────────────────────┼──────────────────────────────────┤
│ Schema Pending Status        │ Precondition-1 Directed-Gap      │
│ Chunks Base Adequacy         │ Precondition-2 Chunk-Substrate   │
│ Prediction-Delta Threshold   │ Precondition-3 Delta-Gate        │
│ Goldilocks Zone Position     │ Precondition-4 Match-Range       │
│ Chunk Association Tag        │ Precondition-5 Compile-Gate      │
└──────────────────────────────┴──────────────────────────────────┘
```
