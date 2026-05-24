---
title: Body-Feedback Mechanism — Chunk Dynamics Classification
version: 2.0
created: 2026-04-20
updated: 2026-05-16 (v2.0 — FULL REWRITE: Body-Need aggregate, Complexity Spectrum, Cross-cutting clarification, Inter-Body drill integration)
previous: v1.3 → backup/Body-Feedback-Mechanism-v1.3-backup.md
status: REFERENCE v2.0
scope: |
  CORE MECHANISM FILE: HOW body-feedback arises from chunk dynamics.
  NEW v2.0: Body-Need aggregate framing + Complexity Spectrum.
  2 input sources (Sensory-Driven / Pattern-Driven).
  3 chunk dynamics (Chunk-Shift / Chunk-Miss / Chunk-Gap).
  Compound mechanism. Quality Baseline Shift.
  Research anchors: Crespi 1942, Schultz 1997, Berridge 2003, Amsel, Flaherty 1996.
purpose: |
  Existing files classify body-feedback by INTENSITY (02-Dissonance.md, 14 levels),
  SOURCE (02-Dissonance.md §3, 3 Genuine Discomfort Sources), and PRECONDITION (H10 5 preconditions).
  File này thêm trục thứ 4: CHUNK MECHANISM — HOW chunks fire tạo ra signal.
  Trục này match v7.8 "chunk-centric" principle: everything runs on chunks,
  classification phải chunk-based.
  v2.0 NEW: Body-Need aggregate concept — chunk dynamics = mechanism,
  body-need = aggregate OUTPUT. Complexity Spectrum (Simple→Social→Meta)
  shows CÙNG mechanism, KHÁC substrate level.
position: |
  Body-Feedback/ folder — ngang hàng với Body-Feedback.md (synthesis entry point).
  File này = MECHANISM reference (HOW body-feedback arises).
  Body-Feedback.md = ARCHITECTURE reference (WHAT body-feedback does + H10).
  01-04 files = CASE ANALYSES (apply mechanism to specific scenarios).
dependencies:
  - Chunk.md v2.2 — chunk substrate, context-tag model
  - Chunk-Activation-Dynamics.md — probability, re-linking, trigger surface
  - Valence-Propagation.md v1.4 — valence per-entity + chain propagation
  - Body-Feedback.md v1.1 — H10, dual-pull, interface loop
  - Body-Feedback-Label.md v2.0 — vocabulary reference (3-tier labels)
  - 02-Dissonance.md — intensity levels, source taxonomy, case analyses
  - Core-v7.8-Draft.md — cycle architecture, A/B/C/D zones
  - Cortisol-Baseline.md v2.0 — amplifier, holding signal
  - Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State, E₀→E₃, 5 Profiles
  - Inter-Body-Mechanism.md v1.0 — Body-Need aggregate, 3-cost, 5-channel
  - Gap-Direction.md v1.1 — gap has direction = f(surrounding chunks)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Mechanism — Chunk Dynamics Classification

> **Cùng 1 sự kiện "mất 100k".**
> Rơi mất → tiếc. Bị lừa → tiếc + tức. Bị bạn thân lừa → tiếc + tức + cay đắng.
>
> Cùng monetary loss. Nhưng chunk patterns fire KHÁC NHAU.
> Mỗi layer chunk thêm vào = thêm 1 "hương vị" dissonance.
>
> Body-feedback không chỉ có direction (reward/dissonance) và magnitude (nhẹ→cực).
> Body-feedback còn có **chunk dynamics** — CÁCH chunks fire tạo ra signal.
>
> Những signals này TỔNG HỢP thành **body-need** — trạng thái CẦN hiện tại
> mà body đòi đáp ứng. Body-need = aggregate output của chunk dynamics.
>
> File này formalize trục phân loại đó + body-need aggregate framing.

---

## Mục lục

- §0 — THESIS + VỊ TRÍ TRONG FRAMEWORK
- §1 — BODY-NEED: AGGREGATE OUTPUT
- §2 — 2 NGUỒN ĐẦU VÀO (Sensory-Driven / Pattern-Driven)
- §3 — 3 CHUNK DYNAMICS (Chunk-Shift / Chunk-Miss / Chunk-Gap)
- §4 — COMPOUND MECHANISM
- §5 — QUALITY BASELINE SHIFT
- §6 — MAP VÀO FRAMEWORK (v7.8 Cycle + H10)
- §7 — RESEARCH ANCHORS
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES

---

## §0 — THESIS + VỊ TRÍ TRONG FRAMEWORK

```
⭐ 4 TRỤC PHÂN LOẠI BODY-FEEDBACK:

  Body-feedback signal có 4 trục phân loại ORTHOGONAL (vuông góc):

  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  TRỤC 1 — DIRECTION (hướng):                                    │
  │    Reward (opioid) / Dissonance (mismatch) / Neutral            │
  │    → Body-Feedback.md §2 dual-pull                              │
  │                                                                 │
  │  TRỤC 2 — MAGNITUDE (cường độ):                                 │
  │    14 levels: nagging unease → emergency → shutdown              │
  │    → 02-Dissonance.md (case-based intensity spectrum)           │
  │                                                                 │
  │  TRỤC 3 — SOURCE (nguồn gốc bên ngoài):                        │
  │    3 Genuine Discomfort Sources: nociception, mismatch, recalibration │
  │    → 02-Dissonance.md §3 + Body-Feedback.md §5                  │
  │                                                                 │
  │  TRỤC 4 — CHUNK DYNAMICS (cơ chế chunk) ← FILE NÀY             │
  │    HOW chunks fire tạo ra signal                                │
  │    2 input sources × 3 dynamics × compound                      │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  4 trục ORTHOGONAL = mỗi trục MÔ TẢ KHÍA CẠNH KHÁC NHAU:
    → Cùng 1 signal có thể là: reward (trục 1) + nhẹ (trục 2)
      + social (trục 3) + Chunk-Shift (trục 4)
    → 4 trục KHÔNG thay thế nhau — BỔ SUNG nhau


⭐ v2.0 THÊM: BODY-NEED AGGREGATE FRAMING

  File này KHÔNG CHỈ phân loại signals (trục 4).
  File này CÒN cho thấy: signals TỔNG HỢP thành BODY-NEED.

  Body-Need = aggregate output = tổng hợp TẤT CẢ signals đang đòi đáp ứng.
  §1 define body-need. §2-§5 giải thích HOW body-need arises.
  = Missing link: "chunks fire" → "body cần gì" → "hành vi"


  FILE NÀY TRONG FLOW:

    Chunk.md v2.2 (sole substrate)
         │
         ▼
    Chunk-Activation-Dynamics (HOW chunks fire: probability, re-linking)
         │
         ▼
    ┌─────────────────────────────────────────────────────────────┐
    │ BODY-FEEDBACK-MECHANISM.MD v2.0 (FILE NÀY)                  │
    │                                                              │
    │  §1:  BODY-NEED = aggregate output                          │
    │  §2:  Input: 2 sources (Sensory-Driven / Pattern-Driven)   │
    │  §3:  Dynamics: 3 types (Chunk-Shift / Chunk-Miss / Gap)   │
    │  §4:  Compound: multiple dynamics simultaneous              │
    │  §5:  Baseline Shift: quality re-habituate                  │
    │                                                              │
    │  Output: body-feedback signal (direction + magnitude)        │
    │  = HOW chunk dynamics PRODUCE body-feedback → body-need      │
    │  = Missing layer giữa "chunks fire" và "body cần gì"        │
    └─────────────────────────────────────────────────────────────┘
         │
         ▼
    Body-Feedback.md (H10, dual-pull, interface loop)
    Feeling.md v2.0 (PFC observation of body-feedback)
    02-Dissonance.md (intensity spectrum + source taxonomy + case analyses)
    Inter-Body-Mechanism.md v1.0 (5-channel, 3-cost, entity interaction)
```

---

## §1 — BODY-NEED: AGGREGATE OUTPUT

### §1.1 — Definition

```
⭐ BODY-NEED = TỔNG HỢP TRẠNG THÁI CẦN HIỆN TẠI:

  Body-Need = aggregate của TẤT CẢ signals đang đòi body đáp ứng.

  KHÔNG phải 1 signal đơn → là TỔNG HỢP nhiều signals parallel.
  KHÔNG phải PFC tạo → body-need exist TRƯỚC PFC awareness.
  KHÔNG phải chỉ survival → BẤT KỲ compiled gap fill (Compilable Architecture).

  Body-Need = OUTPUT CỦA CƠ CHẾ file này mô tả:
    2 input sources (§2) → 3 chunk dynamics (§3) → compound (§4)
    → quality baseline shift (§5) → body-need aggregate

  (Inter-Body-Mechanism.md §2: Body-Need full definition + inter-body context)
```

### §1.2 — 2 genuine sources

```
⭐ BODY-NEED CHỈ ĐẾN TỪ 2 NGUỒN THẬT:

  ┌─────────────────────────────────────────────────────────────┐
  │ ① HARDWARE / SENSORY-DRIVEN (pre-chunk possible):           │
  │                                                             │
  │   Homeostatic: đói, khát, nhiệt, oxy, ngủ                  │
  │   Nociceptive: đau, injury, reflex                          │
  │   Hormonal: social isolation hardware, sexual drive          │
  │                                                             │
  │   → Domain stimulus → receptors → body signal               │
  │   → KHÔNG cần compiled chunks (animals đầy đủ)              │
  │   → D+C zones primary                                       │
  └─────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────┐
  │ ② CHUNK DYNAMICS / PATTERN-DRIVEN:                          │
  │                                                             │
  │   3 dynamics: Gap / Miss / Shift (+ Compound)               │
  │   → Internal chunk fire → body respond                      │
  │   → REQUIRES compiled chunks as prerequisite                │
  │   → Human-dominant (rich chunk network)                     │
  └─────────────────────────────────────────────────────────────┘

  ⭐ 2 nguồn KHÔNG loại trừ — 1 event kích hoạt CẢ ①+②:
    VD: ăn đồ ăn (① sensory) + nhớ lần trước ngon hơn (② Miss)
    VD: social isolation (① hardware oxytocin deficit + ② compiled friend Miss)

  Chi tiết mỗi nguồn: §2 file này.
```

### §1.3 — Cross-cutting: KHÔNG phải sources

```
🟡 OBSERVATION PARAMETERS VÀ STATE MODIFIERS = CROSS-CUTTING, KHÔNG PHẢI SOURCES:

  OBSERVATION PARAMETERS (named patterns, v7.8 — Protect.md §0):
    Protect = ownership chunks + loss aversion + avoidance direction
    Threat  = urgency tag + priority override (from ANY source)
    Status  = relative position pattern
    Novelty = gap-fill drive + approach direction
    → Emerge TỪ ①+② trong combinations cụ thể
    → KHÔNG phải source riêng — là TÊN GỌI cho patterns observable
    → Can thiệp ở level mechanism (①②), không ở level label

  STATE MODIFIERS:
    Cortisol: amplify negative signals (Cortisol-Baseline.md v2.0)
    Urgency: override priority ranking
    Energy/fatigue: shift threshold cho all signals
    → KHÔNG tạo body-need mới — SHIFT priority/intensity của existing

  TẠI SAO PHÂN BIỆT QUAN TRỌNG:
    "Protect" KHÔNG phải source thứ 3 → "Protect" = Chunk-Miss (mất cái đã compile)
                                         + Chunk-Shift (threat to owned) + avoidance tag
    "Status drop" KHÔNG phải source thứ 3 → = Chunk-Miss (compiled position lost)
    Can thiệp ĐÚng = can thiệp ở ①② mechanism
    Can thiệp SAI = treat label as independent cause → miss root mechanism

  (Inter-Body-Mechanism.md §2.3: cross-cutting clarification)
```

### §1.4 — 7 properties of Body-Need

```
BODY-NEED CÓ 7 PROPERTIES:

  ① LUÔN TỒN TẠI (không bao giờ = 0)
     → "Nằm thư giãn bãi biển" vẫn có: nắng chiếu = sensory fill gap
     → Nếu 0 gap → 0 drive → 0 hành vi → chết

  ② MULTIPLE cùng lúc (parallel)
     → Đói + chán + nhớ bạn + career anxiety = 4 body-needs song song

  ③ CÓ PRIORITY (intensity × urgency × state)
     → "Cháy nhà" override "chán" (survival > novelty)
     → Priority = dynamic, shift theo state

  ④ CÓ DIRECTION (từ chunk network topology — Gap-Direction.md)
     → Chỉ fill đúng hướng mới reward
     → Hướng = f(surrounding chunks) → mỗi người RIÊNG

  ⑤ PFC KHÔNG LUÔN BIẾT (exist trước awareness)
     → "Chán nhưng không biết cần gì" = body-need có, PFC chưa identify
     → PFC guess sai direction = "tiktok" thay vì "vận động"

  ⑥ CÓ THỂ CONFLICT (internal tension)
     → "Ăn ngon vs dáng đẹp" = 2 body-needs, opposite direction
     → PFC arbitrate → suppress 1 → cost (Inter-Body §4)
     → Mâu thuẫn nội tâm = BÌNH THƯỜNG, không bất thường

  ⑦ CÓ THỂ BỊ HIJACK (temporary distortion)
     → Hormone (limerence): amplify 1 body-need → override all others
     → Scam: control input channels → direction distort
     → Propaganda: collective fear → priority override
     → Domain Reality = final arbiter ALWAYS

  (Inter-Body-Mechanism.md §2.4: 7 properties full context)
```

### §1.5 — 4 loại theo immediacy

```
┌─────────────────────────────────────────────────────┐
│ IMMEDIATE (seconds-minutes):           [① dominant] │
│   Đói, đau, nóng. PFC biết rõ.                     │
│   Direction rõ ràng.                                │
├─────────────────────────────────────────────────────┤
│ SHORT-TERM (hours-days):              [①+② mix]    │
│   Chán, cô đơn, mệt.                               │
│   PFC CÓ THỂ KHÔNG biết rõ                         │
│   (lướt tiktok nhưng thật ra cần vận động).         │
├─────────────────────────────────────────────────────┤
│ LONG-TERM (months-years):          [② meta dominant]│
│   Career, Imagine-Final, relationship direction.    │
│   PFC BUILD direction qua nhiều năm.                │
├─────────────────────────────────────────────────────┤
│ STRUCTURAL (always running):   [①hardware + ②structural] │
│   Social belonging. Autonomy. Coherence.             │
│   PFC thường KHÔNG aware (until violated).          │
└─────────────────────────────────────────────────────┘

  (Inter-Body-Mechanism.md §2.5: 4 immediacy types full context)
```

---

## §2 — 2 NGUỒN ĐẦU VÀO

### §2.1 — Tại sao phân biệt 2 nguồn

```
🟡 BODY-FEEDBACK CÓ THỂ SINH RA TỪ 2 NGUỒN KHÁC NHAU:

  ① Domain thay đổi → body-input thay đổi → chunks fire THEO
  ② Chunks fire NỘI BỘ (replay, preview, so sánh) → body respond THEO

  Cùng output (body-feedback signal).
  Nhưng KHÁC input pathway → khác timing, khác zones, khác species capability.

  Phân biệt quan trọng vì:
  → Xác định CAN THIỆP ở đâu (fix environment vs fix internal patterns)
  → Hiểu TẠI SAO animals cũng có body-feedback (sensory-driven)
  → Hiểu TẠI SAO humans phong phú hơn (pattern-driven mạnh hơn)
```

### §2.2 — Sensory-Driven (từ body-input)

```
⭐ SENSORY-DRIVEN — DOMAIN ĐI TRƯỚC, CHUNKS FIRE THEO:

  FLOW:
    Domain stimulus → receptors (17 categories) → neural signal
    → compiled chunks MATCH/MISMATCH → body-feedback fires

  ĐẶC ĐIỂM:
    ① Body-input ĐI TRƯỚC — chunks fire REACTIVE (phản ứng)
    ② D+C zones primary (peripheral + subcortical)
    ③ Animals ĐẦY ĐỦ — không cần PFC
    ④ Timing: 50ms (nociception reflex) → seconds (sensory processing)
    ⑤ CẢ reward VÀ dissonance

  VÍ DỤ DISSONANCE:
    → Kim đâm vào da → nociceptors fire → đau (D zone reflex)
    → Trời nóng → thermoreceptors → khó chịu
    → Con gián → visual pattern match "ghê" → ghê tởm (C zone compiled)
    → Quần áo cứng cọ da → somatosensory mismatch → khó chịu
    → Bãi rác → olfactory → ghê tởm

  VÍ DỤ REWARD:
    → Đồ ăn ngon → taste receptors → opioid (body-need met)
    → Nhạc hay → auditory pattern → opioid (Goldilocks match)
    → Mùi hương thơm → olfactory → pleasant
    → Áo mềm mặc vào → somatosensory match → comfortable
    → Tranh đẹp → visual Goldilocks → aesthetic reward

  ĐẶC TÍNH QUAN TRỌNG:
    → Không cần PFC, không cần Imagine-Final
    → Chó ăn đồ ngon hơn vẫn thấy thích — same mechanism
    → Body-input TRỰC TIẾP drive chunk matching
    → Signal strength tùy delta giữa input và compiled baseline

  EVALUATIVE/DIRECT-STATE DIMENSION (Reward-Signal-Architecture.md §1):
    → Sensory-Driven ≈ DIRECT-STATE territory (direct state signals):
      Touch (CT afferents), temperature, pain, basic taste = hardware-level
      Non-opioid pathways, below PFC, minimal cortical involvement
    → Sensory-Driven CÓ THỂ CÓ Evaluative component khi cortical evaluation:
      Nhạc hay = auditory + cortical pattern match → Evaluative Reward
      Ăn ngon = taste + hedonic evaluation → Evaluative + Direct-State compound
    → "Pure sensory" = mostly Direct-State. "Sensory + evaluation" = Evaluative + Direct-State.

  🟢 RESEARCH:
    → Sensory processing pathways: established neuroscience
    → Hedonic responses in animals: Berridge facial coding (tongue protrusion)
    → Taste preference without cognition: Berridge 2003 (dopamine-depleted rats
      still show liking reactions to sucrose placed in mouth)
```

### §2.3 — Pattern-Driven (từ chunk network nội bộ)

```
⭐ PATTERN-DRIVEN — CHUNKS FIRE TRƯỚC, BODY RESPOND THEO:

  FLOW:
    Internal chunk activity (replay, preview, comparison, gap detect)
    → body-base simulate/respond → body-feedback fires

  ĐẶC ĐIỂM:
    ① Chunks fire NỘI BỘ — KHÔNG cần domain stimulus mới
    ② B+C zones primary (cortical + subcortical), A(PFC) optional
    ③ Animals có (hippocampal replay), humans RICH hơn nhiều
    ④ Timing: seconds → years
    ⑤ CẢ reward VÀ dissonance
    ⑥ CẦN compiled chunks làm prerequisite

  6 CƠ CHẾ TRIGGER (chunks fire nội bộ):

    ⓐ REPLAY — hippocampus phát lại experience cũ
       → Sleep replay (🟢 Walker 2017)
       → Awake replay (spontaneous recall)
       → "Nhớ lại bị chó cắn" → body respond sợ

    ��� PREVIEW — PFC hoặc hippocampus simulate future
       → Imagine-Final preview: "nếu mua xe thì sẽ thế nào"
       → Body pre-feel: ~20-60% fidelity (Imagination.md §2)
       → Chuột cũng có: hippocampal preplay trước navigation
         (🟢 Pfeiffer & Foster 2013)

    ⓒ COMPARISON — 2+ chunk patterns so sánh nội bộ
       → Social comparison: "bạn C giỏi hơn mình"
       → Quality comparison: "hôm qua ăn ngon hơn hôm nay"
       → PFC hoặc unconscious cũng so sánh được

    ⓓ GAP DETECT — ACC/insula detect inconsistency trong network
       → "Vật lý Newton có mâu thuẫn" (Einstein)
       → "Framework này còn thiếu gì đó" (felt sense)
       → KHÔNG CẦN PFC — ACC tự detect

    ⓔ SPREADING ACTIVATION — 1 chunk fire → cascade qua network
       → Chị-B khoe con → chunks về CON MÌNH fire theo
       → Collins & Loftus 1975 🟢
       → Cascade có thể activate patterns tạo dissonance mới

    ⓕ CONTEXT-FREE CHUNK FIRE — trauma chunk fires without context:
       → Chunk.md §2.6: context-free chunks = ④ state only, THIẾU ①②③
       → Sensory cue → amygdala low road match (~12ms) → chunk fires NỘI BỘ
       → Body responds AS IF in original trauma (full state metadata fires)
       → = Pattern-Driven vì chunk fires NỘI BỘ, không phải external threat
       → NHƯNG chunk THIẾU temporal/spatial context → body KHÔNG BIẾT là quá khứ
       → PFC arrives ~200ms SAU → corrective signal LATE + may be OFFLINE
       → = Flashback mechanism (PTSD-Analysis.md §4)
       → = ⓐ Replay KHÁC: replay = hippocampal, CÓ context → "nhớ lại"
         ⓕ Context-free = amygdala, KHÔNG context → "sống lại"
       → 🟢 LeDoux 1996: low road ~12ms, 🟢 Brewin 2010: S-rep

  VÍ DỤ DISSONANCE:
    → Chị-A nghe chị-B khoe con → so sánh → chạnh lòng (comparison)
    → Einstein thấy vật lý mâu thuẫn → bứt rứt (gap detect)
    → Nhớ lại bị phản bội → đau (replay)
    → Imagine-Final xe đẹp mà chưa có → thiếu (preview)

  VÍ DỤ REWARD:
    → Imagine-Final "sẽ giải được bài toán" → mini opioid (preview)
    → Nhớ lại kỷ niệm đẹp → ấm áp (replay)
    → So sánh "mình giỏi hơn trước" → tự tin (comparison)
    → Gap fill: "À, hiểu rồi!" → opioid burst (gap filled)

  EVALUATIVE/DIRECT-STATE DIMENSION (Reward-Signal-Architecture.md §1):
    → Pattern-Driven = primarily EVALUATIVE territory (evaluative):
      Cortical pattern match → OFC/vmPFC evaluation → opioid (if match)
      Insight, coherence, preview = all require cortical processing
    → Pattern-Driven CÓ THỂ kích hoạt Direct-State:
      Replay of touch memory → body re-simulate → B partial activation
      Preview of exercise → motor cortex pre-activate → B trace
    → Evaluative Gates Direct-State (Reward-Signal-Architecture.md §3):
      A evaluation MODULATES B body-state response
      = WHY "nghĩ về ôm" ≠ "ôm thật" (preview fidelity < 100%)

  🟢 RESEARCH:
    → Hippocampal replay/preplay: Pfeiffer & Foster 2013, Wilson & McNaughton 1994
    → Spreading activation: Collins & Loftus 1975
    → Social comparison: Festinger 1954
    → ACC error detection: Bush et al. 2000
```

### §2.4 — So sánh 2 nguồn

```
┌──────────────────────┬──────────────────────┬──────────────────────┐
│                      │ SENSORY-DRIVEN       │ PATTERN-DRIVEN       │
├──────────────────────┼──────────────────────┼──────────────────────┤
│ Trigger              │ Domain stimulus      │ Internal chunk fire  │
│ Direction            │ Outside → In         │ Inside → Body        │
│ Primary zones        │ D + C                │ B + C (A optional)   │
│ Reward type          │ Mostly Direct-State  │ Mostly Evaluative    │
│ Animals              │ ĐẦY ĐỦ              │ CÓ nhưng limited     │
│ PFC cần?             │ KHÔNG                │ Optional             │
│ Timing               │ ms → seconds         │ seconds → years      │
│ Prerequisite         │ Receptors active      │ Compiled chunks      │
│ Ví dụ dissonance     │ Kim đâm, nóng, gián  │ So sánh, nhớ lại    │
│ Ví dụ reward         │ Đồ ngon, nhạc hay    │ Insight, preview     │
│ Can thiệp            │ Fix environment      │ Fix internal pattern │
└──────────────────────┴──────────────────────┴──────────────────────┘

⭐ CẢ 2 NGUỒN → CÙNG OUTPUT: body-feedback signal (direction + magnitude)
⭐ CẢ 2 NGUỒN → có thể trigger BẤT KỲ chunk dynamics nào (§3)
⭐ KHÔNG LOẠI TRỪ: 1 event có thể kích hoạt CẢ 2 nguồn cùng lúc
   VD: ăn đồ ăn (sensory) + nhớ lại lần ăn trước ngon hơn (pattern)
```

### §2.5 — Complexity Spectrum (cùng mechanism, khác substrate)

```
🟡 3 DYNAMICS (§3) HOẠT ĐỘNG Ở MỌI SUBSTRATE LEVEL:

  ┌─────────────────────────────────────────────────────────────────┐
  │ SIMPLE (physical objects, sensory patterns):                     │
  │   Chunk-Miss: áo mềm baseline → áo cứng = "tệ hơn quen"      │
  │   Chunk-Shift: thức ăn quen → phát hiện hết hạn = valence flip │
  │   Chunk-Gap: công thức thiếu 1 gia vị → "thấy thiếu gì đó"    │
  ├─────────────────────────────────────────────────────────────────┤
  │ SOCIAL (entities, relationships):                                │
  │   Chunk-Miss: bạn thân absent = "nhớ"                           │
  │   Chunk-Shift: bạn thân phản bội = valence flip entity chunks  │
  │   Chunk-Gap: "có vẻ nó buồn gì đó" = detect gap in Self-Pattern-Modeling model  │
  ├─────────────────────────────────────────────────────────────────┤
  │ META (abstract compiled structures):                             │
  │   Chunk-Miss: Imagine-Final không đạt = compiled preview missed │
  │               Status drop = compiled position lost               │
  │               Obligation violated = compiled prediction broken   │
  │   Chunk-Shift: Identity challenge = self-schema valence shift   │
  │   Chunk-Gap: "Cuộc sống thiếu meaning" = meta-gap in coherence │
  └─────────────────────────────────────────────────────────────────┘

  ⭐ KEY INSIGHT — TẦNG ③ COLLAPSE:

    Imagine-Final, Obligation, Identity, Status:
    = CÙNG chunk dynamics (Gap/Miss/Shift)
    = Chỉ khác SUBSTRATE LEVEL (meta-compiled structures)
    = Khác timescale + PFC involvement + intervention approach
    = KHÔNG phải mechanism riêng — KHÔNG CẦN tầng phân loại mới

    Tại sao meta FEELS khác:
    → Network size lớn hơn (identity = hundreds of chunks)
    → Timescale dài hơn (career gap = years)
    → PFC involvement nhiều hơn (abstract requires cortical)
    → Nhưng BODY-FEEDBACK MECHANISM = SAME: Gap/Miss/Shift

    → Parsimony: 3 dynamics explain ALL levels
    → Can thiệp: identify WHICH dynamic + WHICH substrate
    → "Mất ý nghĩa cuộc sống" = Meta Chunk-Gap = ACC detect
      inconsistency in coherence network → body signal "bứt rứt"
      → same mechanism as "vật lý mâu thuẫn" nhưng khác substrate

  (Inter-Body-Mechanism.md §2.2: complexity spectrum defined)
```

---

## §3 — 3 CHUNK DYNAMICS

### §3.0 — Tổng quan

```
🟡 KHI BODY-FEEDBACK FIRE, CHUNK NETWORK CÓ 3 LOẠI THAY ĐỔI:

  Chunk dynamics MÔ TẢ: cái gì xảy ra TRONG chunk network khi signal sinh ra.

  ① CHUNK-SHIFT — valence CỦA chunks thay đổi (content giữ nguyên)
  ② CHUNK-MISS — pattern đã compiled KHÔNG ĐƯỢC FIRE (absent)
  ③ CHUNK-GAP  — pattern CHƯA TỪNG CÓ nhưng network detect thiếu

  3 dynamics:
  → KHÔNG loại trừ — 1 event có thể trigger 2-3 dynamics cùng lúc (§4)
  → Áp dụng cho CẢ reward VÀ dissonance (khác direction, cùng mechanism)
  → Có thể trigger bởi CẢ sensory-driven VÀ pattern-driven (§2)
  → Hoạt động ở MỌI substrate level: Simple / Social / Meta (§2.5)
```

### §3.1 — Chunk-Shift (valence thay đổi)

```
⭐ CHUNK-SHIFT — CÙNG CHUNKS, KHÁC ĐÁNH GIÁ:

  ĐỊNH NGHĨA:
    Valence (đánh giá) của chunk network BỊ THAY ĐỔI.
    Chunks content vẫn y nguyên — đánh giá THAY ĐỔI.
    Có thể đột ngột (1 event) hoặc dần dần (many events).

  CƠ CHẾ:
    Thông tin mới (1 chunk mới hoặc 1 experience mới)
    → Re-evaluate valence của chunks liên quan
    → Valence propagate qua network (Valence-Propagation.md §4)
    → Body-feedback fire theo valence MỚI

  DIRECTION:
    Shift NEGATIVE (dissonance):
      → Phản bội: chunks về người yêu VẪN ĐÓ, valence FLIP negative
      → Phát hiện đồ giả: chunks về sản phẩm vẫn đó, valence drop
      → Nhận tin xấu về ai đó: chunks vẫn đó, valence shift

    Shift POSITIVE (reward):
      → Exposure therapy thành công: fear chunks → safety association grows
      → Học dùng dao: fear valence → utility valence
      → Được giải thích hiểu lầm: negative valence → positive restore

  TẠI SAO "SHIFT", KHÔNG PHẢI "FLIP":
    → "Flip" gợi ý binary (+ → -), nhưng thực tế là GRADIENT
    → Có thể shift nhẹ (hơi thất vọng) hoặc shift mạnh (phản bội)
    → Shift có thể ở NHIỀU channels khác mức (Valence-Propagation §2)
    → "Shift" capture cả partial change

  ĐẶC ĐIỂM:
    ① Chunks CONTENT không thay đổi — memories vẫn y nguyên
    ② Chỉ VALENCE (đánh giá) thay đổi
    ③ Propagation qua network: 1 chunk shift → kéo theo nhiều chunks
    ④ Intensity tùy: network size × shift magnitude × surprise level
    ⑤ Cơ chế nền: competitive re-linking (Chunk-Activation-Dynamics §3)

  VÍ DỤ PHÂN TÍCH — PHẢN BỘI:

    Trước phát hiện:
      Chunks [người yêu] = {
        Visual: mặt, dáng, nụ cười — content
        Auditory: giọng nói — content
        Somatic: ôm, hôn — content
        Emotional: yêu, tin tưởng, an toàn — VALENCE (positive)
      }

    Sau phát hiện "phản bội":
      1 chunk MỚI compile: [phản bội] (emotional peak, 1 lần đủ)
      → Valence propagation: [phản bội] → re-evaluate ALL connected chunks
      → Chunks [người yêu] = {
        Visual: CÙNG mặt, dáng, nụ cười — content UNCHANGED
        Auditory: CÙNG giọng — content UNCHANGED
        Somatic: CÙNG cảm giác — content UNCHANGED
        Emotional: đau, tức, mất mát, bị phản bội — VALENCE SHIFTED
      }

    → Cùng memories. Cùng content. KHÁC evaluation.
    → "Nhìn ảnh cũ mà đau" = content trigger → new valence fires → dissonance

  🟢 RESEARCH:
    → Evaluative conditioning: valence transfer qua association (De Houwer 2007)
    → Fear conditioning: rapid valence assignment (LeDoux 1996)
    → Extinction ≠ erasure: old valence suppressed, not deleted (Bouton 2004)
    → Reconsolidation: valence CAN be modified during window (Nader 2000)
```

### §3.2 — Chunk-Miss (pattern absent)

```
⭐ CHUNK-MISS — PATTERN ĐÃ COMPILED NHƯNG KHÔNG ĐƯỢC FIRE:

  ĐỊNH NGHĨA:
    Body-base đã compile pattern X thành baseline.
    Pattern X không fire (absent, degraded, hoặc chất lượng giảm).
    VTA detect: actual < compiled baseline → negative prediction-delta.
    Body signal: "worse than expected."

  CƠ CHẾ:
    ① Body compile chunks ở quality X (qua repetition, experience)
    ② VTA habituate tới pattern X → X = baseline mới
    ③ Pattern X bị absent hoặc quality giảm
    ④ VTA fires NEGATIVE prediction-delta (dopamine SUPPRESS)
       → 🟢 Schultz 1997: reward < predicted → dopamine dip below baseline
    ⑤ Body signal: dissonance ("worse than expected")

  ⭐ BODY-BASE KHÔNG "NHỚ" THEO KIỂU PFC RECALL:
    → Compiled baseline = Hebbian LTP đã wire pattern
    → Pattern tồn tại ở BODY LEVEL (C+D zones)
    → KHÔNG CẦN PFC nhớ lại — compiled pattern TỰ FIRE khi mismatch
    → Tương tự: mặc áo mềm quen rồi, mặc áo cứng → body signal NGAY
      TRƯỚC KHI PFC kịp "nhớ" áo mềm

  4 VARIANTS:

    ⓐ MISS RÕ — PFC biết thiếu gì:
       → TikTok quen → máy hỏng → "muốn xem TikTok mà không được"
       → Áo mềm → áo cứng → "áo này cứng quá"
       → Gạo ngon → gạo rẻ → "cơm hôm nay không ngon"
       → PFC CÓ label: biết source, biết muốn gì

    ⓑ MISS MỜ — delta tích tụ, PFC không detect:
       → Ngồi nhà xem phim nhiều ngày → uể oải → "chán mà không biết vì sao"
       → Thiếu vận động dần dần → body cồn cào → PFC confused
       → Delta mỗi ngày quá nhỏ → không vượt threshold PFC attention
       → Connection: Boredom-Analysis.md core mechanism
       → ĐẶC BIỆT NGUY HIỂM: tích tụ silent → bùng khi quá ngưỡng

    ⓒ MISS VÔ THỨC — body biết, PFC không biết:
       → Từ quê lên thành phố làm việc lâu → về quê bỗng sảng khoái
       → "Không biết vì sao thích leo núi, vào rừng thấy thoải mái"
       → Body đã compile patterns (không khí, cây xanh, vận động)
         ở C+D level → PFC KHÔNG có verbal label
       → Khi pattern fire lại → opioid → "thoải mái mà không biết vì sao"
       → Sở thích tùy người = compiled patterns tùy experience cá nhân

    ⓓ MISS IRRESOLVABLE — hardware prevents resolution:
       → Normal miss (ⓐⓑⓒ): miss → adjust → resolve (seconds-days)
       → Irresolvable miss: hardware NGĂN CẢN resolution
       → Parkinson-Analysis.md §5.2: PFC predict "bước đi"
         → gate LOCKED → body KHÔNG bước → MISMATCH
         → Adjust → try harder → STILL fail → CANNOT resolve
       → = Chronic prediction-delta mà MỌI attempt đều tạo miss MỚI
       → Accumulation: frustration + helplessness + cortisol chronic↑
       → UNIQUE: chưa condition nào tạo irresolvable miss RÕ bằng Parkinson
         (Addiction: execution OK. Depression: IF ép → CÓ THỂ. Parkinson: CAN'T.)
       → 🟡 Framework: irresolvable miss = new Chunk-Miss variant (from drill)

  MISS REWARD (hướng ngược):
    → Reuniting: gặp lại bạn cũ → pattern fire lại → opioid
    → Về quê: compiled nature patterns fire → reward
    → Recovery after illness: body patterns restore → relief + reward

  🟢 RESEARCH — SUCCESSIVE NEGATIVE CONTRAST (SNC):

    Crespi 1942, Flaherty 1996:
    → Setup: Nhóm A ăn sucrose 32% (ngon) nhiều bữa → switch sang 4% (thường)
    → Control: Nhóm B ăn sucrose 4% từ đầu
    → Kết quả: Nhóm A sau switch → ăn ÍT HƠN CẢ nhóm B
    → = Body không chỉ "hơi thất vọng" — phản ứng MẠNH HƠN mức neutral
    → = Compiled baseline bị violated → NEGATIVE signal chủ động

    → Amsel frustration theory: SNC = PRIMARY FRUSTRATION
      = cảm xúc aversive trigger khi expected-actual discrepancy
    → = Chunk-Miss mechanism ở ANIMAL level — KHÔNG cần PFC

    Schultz 1997 — neural mechanism:
    → Expected reward = X (compiled baseline)
    → Actual reward = Y
    → Y > X → dopamine TĂNG ("hay hơn expected")
    → Y = X → dopamine BÌNH THƯỜNG ("đúng expected")
    → Y < X → dopamine BỊ SUPPRESS ("tệ hơn expected") ⭐
    → Dopamine suppress = SIGNAL CHỦ ĐỘNG: "worse than expected"

  BASELINE SHIFT DYNAMICS (chi tiết §5):
    → 1 lần experience chưa đủ shift baseline mạnh
    → Nhiều lần → Hebbian wire cứng → baseline shift rõ
    → Miss sau 1 lần = nhẹ. Miss sau 100 lần = mạnh.
    → Recovery possible: nếu quality thấp sustained đủ lâu → re-habituate
```

### §3.3 — Chunk-Gap (pattern chưa tồn tại)

#### §3.3a — Core: Definition + Mechanism

```
⭐ CHUNK-GAP — PATTERN CHƯA CÓ NHƯNG NETWORK DETECT THIẾU:

  ĐỊNH NGHĨA:
    Chunk network topology có HOLES (lỗ hổng) hoặc CONFLICTS (mâu thuẫn).
    Pattern SHOULD exist (based on network structure) nhưng DOESN'T.
    ACC/insula detect inconsistency → body signal "có gì đó thiếu/mâu thuẫn."
    KHÁC Chunk-Miss: Miss = ĐÃ CÓ rồi mất. Gap = CHƯA BAO GIỜ CÓ.

  CƠ CHẾ:
    ① Chunk network compile qua experience → network topology hình thành
    ② Network có internal structure (connections, patterns, expectations)
    ③ Structure predict: "nếu A và B đúng thì C phải tồn tại"
    ④ Nhưng C CHƯA compile → HOLE trong network
    ⑤ ACC detect inconsistency → body signal "bứt rứt, chưa ổn"
    ⑥ Signal drive behavior: tìm, khám phá, giải quyết → fill gap

  ĐẶC ĐIỂM:
    ① PFC có thể hoặc KHÔNG THỂ articulate cụ thể thiếu gì
    ② Felt sense = body detecting gap trước PFC verbal label
       (Somatic-Articulation-Loop.md: implicit → transitional → explicit)
    ③ Signal persistent — không tự resolve (phải fill gap)
    ④ Fill gap → opioid reward (effort-proportional: 03-Reward.md §4.7)
    ⑤ ⭐ FOUNDATION CHO NOVELTY DRIVE
       Gap detect → bứt rứt → drive to explore/fill → discovery → opioid
    ⑥ ⭐ GAP CÓ HƯỚNG CỤ THỂ (Gap Direction):
       "Structure predict C" → C có HÌNH DẠNG = f(surrounding chunks)
       → Gap direction = what SPECIFICALLY is predicted missing
       → Reward fires CHỈ khi fill MATCH direction, không chỉ "fill gap"
       → "Chưa biết = không có gap" (no chunks → no bờ → no hole)
       → Chi tiết: Gap-Direction.md (4 properties, 2-layer model, unified Tier 1-4)

  GAP vs MISS:

    ┌───────────────────────────┬──────────────────────┐
    │ CHUNK-MISS                │ CHUNK-GAP            │
    ├───────────────────────────┼──────────────────────┤
    │ ĐÃ CÓ → mất              │ CHƯA BAO GIỜ CÓ     │
    │ Body "nhớ" baseline       │ Network "predict"    │
    │ Negative prediction error │ Inconsistency detect │
    │ VTA mechanism             │ ACC mechanism        │
    │ "Muốn lại cái cũ"        │ "Muốn cái chưa có"  │
    │ Recovery = restore        │ Resolution = create  │
    │ VD: TikTok mất            │ VD: Einstein E=mc²   │
    └───────────────────────────┴──────────────────────┘

  VÍ DỤ:

    Einstein:
      → Chunk network về vật lý: Newton + Maxwell + thought experiments
      → Network internal structure: "nếu cả 2 đúng thì phải có unified framework"
      → Unified framework CHƯA TỒN TẠI → GAP
      → Body signal: "bứt rứt, vật lý chưa coherent" → drive nghiên cứu
      → Fill gap (E=mc²) → opioid burst cực mạnh (years of pending)

    Framework này:
      → Chunk network về cognitive science đang build
      → "Vague thấy thiếu gì đó" → GAP (body detect trước PFC articulate)
      → Drive drill → fill gap → "à, chunk dynamics classification!"
      → Insight = gap filled → opioid

    Chunk-Gap + CONFLICT (sub-type):
      → 2 patterns fire CONTRADICTORY → không thể cả 2 đúng
      → GAP = thiếu RESOLUTION giữa 2 patterns
      → VD: cognitive dissonance (Festinger 1957)
      → VD: "nên ở hay đi?" — 2 Imagine-Finals compete, gap = no resolution

  🟢 RESEARCH:
    → ACC error/conflict detection: Bush, Luu, Posner 2000
    → Cognitive dissonance: Festinger 1957
    → Curiosity as information gap: Loewenstein 1994 (information gap theory)
    → Aha moments and ACC: Kounios & Beeman 2009
    → Felt sense: Gendlin 1978 (body detects before verbal)
```

#### §3.3b — Gap → Novelty Drive Loop

```
⭐ GAP → NOVELTY DRIVE = PERPETUAL GAP-FILL CYCLE:

  ┌─────────────────────────────────────────┐
  │                                         │
  │  Gap detected (ACC/insula)              │
  │       ↓                                 │
  │  Body signal: "bứt rứt, thiếu gì đó"   │
  │       ↓                                 │
  │  Drive: explore, research, try          │
  │       ↓                                 │
  │  Fill gap (new chunks compile)          │
  │       ↓                                 │
  │  Opioid reward (effort-proportional)    │
  │       ↓                                 │
  │  VTA habituate → new baseline           │
  │       ↓                                 │
  │  Network detect NEW gap                 │
  │       ↓                                 │
  │  [LOOP continues]                       │
  │                                         │
  │  = Novelty drive = perpetual gap-fill   │
  │  = "Tò mò" = body detecting gaps        │
  │  = Science = systematic gap-filling      │
  │  = Art = aesthetic gap-filling           │
  └─────────────────────────────────────────┘
```

#### §3.3c — Gap → Miss Transition

```
⭐ GAP CÓ THỂ CHUYỂN THÀNH CHUNK-MISS:

  Chunk-Gap thuần: ACC detect "thiếu" → body bứt rứt → drive tìm.
  NHƯNG Gap có thể CHUYỂN thành Chunk-Miss qua cơ chế sau:


  ① CƠ CHẾ CỐT LÕI — Imagine-Final preview compile thành baseline:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  Gap detected (ACC) → PFC build Imagine-Final preview       │
  │    ↓                                                        │
  │  Imagine-Final ổn định + lặp nhiều lần                      │
  │    ↓                                                        │
  │  Body compile preview thành expectation baseline             │
  │  (§5 Quality Baseline Shift: repeated preview = new normal) │
  │    ↓                                                        │
  │  Body now EXPECTS cái chưa-từng-có                          │
  │    ↓                                                        │
  │  Reality vẫn KHÔNG có → VTA: actual < baseline              │
  │    ↓                                                        │
  │  = Chunk-Gap (ACC, mơ hồ) → Chunk-Miss (VTA, cụ thể)      │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

    Điều kiện: Imagine-Final phải ỔN ĐỊNH (không đổi) + LẶP đủ nhiều.
    Nếu Imagine-Final ĐỔI → gap cũng đổi → body fire pattern MỚI → path KHÁC.


  ② TẠI SAO PREVIEW LẶP — Cortisol holding signal:

    Gap kéo dài + unresolved → cortisol fires "still need change"
    (Cortisol-Baseline.md §3.8: holding signal giữ imagination loop active)
    → PFC bị BUỘC quay lại Imagine-Final → preview lặp CƯỠNG BỨC
    → Compile baseline NHANH hơn so với preview tự nguyện
    → = "Không ngừng nghĩ về nó" = cortisol holding loop
    → = Cortisol = ACCELERATOR cho Gap→Miss transition


  ③ DIRECTION TAG — Cùng transition, KHÁC outcome:

    Cortisol direction (Cortisol-Baseline.md §3.5) quyết định CHẤT LƯỢNG:

    Gap + Novelty cortisol (curiosity body state):
      → Baseline compile với opioid tag
      → Miss = "muốn + chưa có" → DRIVE seek → productive
      → = "Kỳ vọng hào hứng"

    Gap + Threat cortisol (anxiety body state):
      → Baseline compile với cortisol tag
      → Miss = "sợ + chưa có" → ANXIETY loop → destructive
      → = "Kỳ vọng lo sợ"

    → Cùng Gap→Miss mechanism, KHÁC direction → KHÁC outcome hoàn toàn


  ④ ỨNG DỤNG — "Kỳ vọng càng cao, thất vọng càng lớn":

    Folk wisdom này = Gap→Miss transition:

      Preview VIVID + lặp NHIỀU + Imagine-Final ỔN ĐỊNH
        → Body compile baseline CAO
          → Reality < baseline → Chunk-Miss delta LỚN → "thất vọng lớn"

      Preview THẤP hoặc KHÔNG preview
        → Baseline thấp → Reality ≥ baseline → "bất ngờ comfortable"

    VÍ DỤ:
      → Trẻ thấy bạn được mẹ ôm → PFC preview "nếu mình được ôm"
        → Preview lặp → baseline shift → thiếu = Chunk-Miss cụ thể
        → Ban đầu Gap (mơ hồ) → sau thành Miss (rõ ràng, đau)

      → Xe showroom: preview "có xe" lặp nhiều tháng
        → Body compile thành expectation → chưa có = Miss
        → Khác với "chưa biết xe tồn tại" (pure Gap)


  ⑤ KHI NÀO TRANSITION KHÔNG XẢY RA:

    Nếu Imagine-Final UPDATE SÁT REALITY → baseline track reality
    → Delta nhỏ → KHÔNG thành Miss mạnh.

    Imagine-Final update khi:
      → Domain feedback loop: HÀNH ĐỘNG → nhận feedback → update
      → Background processing: sleep đủ + cortisol không quá cao
      → Chunks liên quan đủ lớn: raw material cho background processing

    Hầu hết người: chunks ổn định → Imagine-Final ổn định → preview lặp
    → transition gần như chắc chắn khi gap kéo dài.
```

#### §3.3d — Gap Decomposition (Mini-Arc Dynamics)

```
⭐ GAP DECOMPOSITION — MINI-ARC DYNAMICS:

  Big Gap tồn tại YEARS (e.g., Einstein unified physics).
  Body KHÔNG THỂ chịu Gap signal liên tục mà không reward.
  → NẾU gap không decompose → burnout / bỏ cuộc hoặc Gap→Miss transition.

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  BIG GAP: "unified physics framework"                       │
  │    ↓                                                        │
  │  Decompose thành MINI GAPS (tự nhiên hoặc PFC chủ động):   │
  │    → Mini gap 1: photoelectric effect → FILL → mini opioid  │
  │    → Mini gap 2: Brownian motion → FILL → mini opioid       │
  │    → Mini gap 3: special relativity → FILL → bigger opioid  │
  │    → BIG GAP FILL: E=mc² → compound opioid burst           │
  │                                                             │
  │  Mỗi mini fill:                                             │
  │    → Opioid reward (effort-proportional: 03-Reward.md §4.7) │
  │    → VTA reset → detect NEXT mini gap → sustain drive       │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  Ứng dụng:
    → PhD: big gap "thesis" → mini gaps (chapters, experiments)
    → Game design: "win game" → mini gaps (levels, quests)
    → Education: "hiểu vật lý" → mini gaps (bài tập, lab)
    → Startup: "build product" → mini gaps (sprints, milestones)

  Gap KHÔNG decompose → kéo dài → CÓ THỂ transition sang Miss (§3.3c).
  Gap decompose tốt → sustained drive + regular reward.
  = PFC Mode 5 Strategic (Drive.md §2): plan decomposition.

  🟢 RESEARCH:
    → Goal gradient effect: Hull 1932 (effort increases near goal = mini-arc)
    → Progress principle: Amabile & Kramer 2011
      (small wins = most powerful motivator in creative work)
```

---

## §4 — COMPOUND MECHANISM

```
⭐ COMPOUND — NHIỀU DYNAMICS FIRE ĐỒNG THỜI:

  NGUYÊN TẮC:
    3 chunk dynamics KHÔNG LOẠI TRỪ.
    1 event có thể trigger 2-3 dynamics cùng lúc.
    Mỗi dynamic thêm = thêm 1 "hương vị" body-feedback.
    = Tại sao dissonance/reward CÓ NHIỀU SẮC THÁI.


  VÍ DỤ PHÂN TÍCH — MẤT 100K:

  ┌──────────────────────┬──────────────┬──────────────┬──────────────┐
  │ Event                │ Chunk-Shift  │ Chunk-Miss   │ Chunk-Gap    │
  ├──────────────────────┼──────────────┼──────────────┼──────────────┤
  │ Rơi mất 100k         │              │ ✅ resource   │              │
  │                      │              │ giảm         │              │
  │ Subjective:          │              │ "tiếc"       │              │
  ├──────────────────────┼──────────────┼──────────────┼──────────────┤
  │ Bị lừa 100k          │ ✅ trust      │ ✅ resource   │              │
  │                      │ shift        │ giảm         │              │
  │ Subjective:          │ "tức"        │ "tiếc"       │              │
  ├──────────────────────┼──────────────┼──────────────┼──────────────┤
  │ Bị bạn thân lừa 100k │ ✅ trust      │ ✅ resource   │ ✅ identity  │
  │                      │ FLIP strong  │ giảm         │ "tôi là ai   │
  │                      │ + connection │              │ mà bạn thân  │
  │                      │ damage       │              │ lại lừa?"    │
  │ Subjective:          │ "tức + đau"  │ "tiếc"       │ "cay đắng"  │
  └──────────────────────┴──────────────┴──────────────┴──────────────┘

  → Cùng 100k loss. 1 dynamic → 2 → 3 = phức tạp hơn, đau hơn, lâu resolve hơn.


  VÍ DỤ PHÂN TÍCH — CHỊ-A/CHỊ-B:

    Chị-A body smooth, chơi thoải mái
    → Chị-B khoe con đạt thành tích giỏi (sensory input: auditory)
    → Spreading activation: chunks về CON MÌNH fire
    → Chunk dynamics:
      Chunk-Gap: con mình vs con chị-B → gap "con mình chưa đạt"
      Chunk-Shift (nhẹ): valence của buổi gặp shift từ vui → chạnh lòng
    → Compound: Gap + Shift → "chạnh lòng, không nói nhiều nữa"
    → LƯU Ý: body-input KHÔNG thay đổi — chỉ chunk fire NỘI BỘ thay đổi


  VÍ DỤ COMPOUND REWARD — EINSTEIN BREAKTHROUGH:

    Fill Chunk-Gap: E=mc² giải mâu thuẫn vật lý → gap filled → opioid MẠNH
    Chunk-Shift: self-schema shift ("tôi = người giải được") → positive
    Chunk-Miss (reverse): years of "thiếu giải pháp" → NÓ ĐÂY → relief + reward
    → Compound 3 dynamics → euphoria cực kỳ


  ⭐ COMPOUND PRINCIPLE:

    Signal_total = Σ (dynamics_i × intensity_i × network_size_i)

    → Nhiều dynamics = tổng signal MẠNH HƠN
    → Network_size lớn = propagation xa = affect nhiều chunks = MẠNH HƠN
    → Intensity mỗi dynamic tùy delta magnitude
    → = Tại sao "bạn thân phản bội" > "người lạ lừa" > "tự rơi"
      (cùng loss, khác compound level)


  🟡 CONDITIONAL INTERACTION MODEL (Reward-Signal-Architecture.md §6):

    ⚠️ COMPOUND ≠ ADDITIVE.
    Công thức Σ ở trên = APPROXIMATION. Thực tế: CONDITIONAL.

    Reward compound NOT simply A + B. 4 VARIABLES determine interaction:

    ① Substrate Overlap:
       → Cùng receptor system (opioid + opioid) → SUPERADDITIVE
       → Khác system (opioid + endocannabinoid) → ADDITIVE
       → Cạnh tranh (opioid + cortisol) → SUBTRACTIVE

    ② A Gate Direction (Reward-Signal-Architecture.md §3):
       → A evaluates → AMPLIFY B → superadditive
       → A evaluates → SUPPRESS B → subtractive
       → A absent → B RAW (no evaluation)

    ③ Relief Presence:
       → Nếu threat pending resolved → cortisol DROP = MULTIPLIER
       → Nếu no threat → opioid only, no relief bonus
       → Relief + reward = STRONGEST compound (Archimedes "Eureka!")

    ④ Temporal Overlap:
       → Simultaneous → compound (most powerful)
       → Sequential (seconds) → cascade (moderate)
       → Sequential (hours+) → independent (no compound)

    → Diagnostic: compound cảm xúc UNEXPECTED = check 4 variables
    → Chi tiết: Reward-Signal-Architecture.md §6 (Conditional Interaction Model)
```

---

## §5 — QUALITY BASELINE SHIFT

```
⭐ QUALITY BASELINE SHIFT — CƠ CHẾ KẾT NỐI SENSORY-DRIVEN VỚI CHUNK-MISS:

  ĐỊNH NGHĨA:
    Body compile chunks ở quality X qua repeated experience.
    VTA habituate → X = baseline mới.
    Quality tăng lên Z > X → positive prediction-delta → reward.
    Quality giảm xuống Y < X → negative prediction-delta → dissonance (Chunk-Miss).
    = Baseline "trượt" theo experience.


  CƠ CHẾ 4 BƯỚC:

    ① COMPILE:
       Repeated experience ở quality X → Hebbian LTP → neurons wire pattern
       → Pattern compiled vào C+D zones (subcortical + peripheral)
       → KHÔNG CẦN PFC để maintain (body-level compile)

    ② HABITUATE:
       VTA habituate tới pattern X → X = "bình thường" → không fire
       → Giống thermostat set ở 25°C: không signal khi đúng 25°C

    ③ DETECT DELTA:
       Actual quality thay đổi:
       → Actual > baseline → positive prediction-delta → reward
       → Actual < baseline → negative prediction-delta → Chunk-Miss
       → Actual = baseline → no signal → neutral

    ④ RE-HABITUATE:
       Nếu quality MỚI sustained đủ lâu → baseline SHIFT lại:
       → Quality mới THẤP hơn sustained → body re-habituate → baseline hạ
       → Quality mới CAO hơn sustained → body re-habituate → baseline nâng
       → = Hedonic adaptation (🟢 Brickman 1978)


  TIMELINE + COMPILE STRENGTH:

    ┌──────────────────────────────────────────────────────────────┐
    │                                                              │
    │  1 lần experience (quality cao):                             │
    │    → Proto-chunk weak → baseline shift NHẸ                   │
    │    → PFC có Imagine-Final preview                            │
    │    → Body-base CHƯA shift rõ                                 │
    │    → Nếu quality giảm → PFC "hụt hẫng" > body-base dissonance │
    │                                                              │
    │  Vài lần (3-10):                                             │
    │    → Chunk strengthening → baseline bắt đầu shift            │
    │    → SNC effect xuất hiện (Crespi: rats downshift)           │
    │    → Body-base dissonance RÕ khi quality giảm                │
    │                                                              │
    │  Nhiều lần (50-100+):                                        │
    │    → Chunk fully compiled → baseline SHIFT CỨNG              │
    │    → Quality giảm = dissonance MẠNH (SNC effect maximum)     │
    │    → Re-habituate xuống chậm (strong compile = slow decay)   │
    │                                                              │
    │  → compile_rate ≈ f(repetition × saliency × peak_valence    │
    │                     × multi_modal × contingency)             │
    │  → Chunk.md v2.2 §2.2: same 5-parameter formula             │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘


  ANIMALS CÓ BASELINE SHIFT:

    🟢 Crespi 1942 / Flaherty 1996 (SNC in rats):
    → Rats trained on high reward → downshift → WORSE than control
    → = Compiled baseline + negative prediction-delta
    → = Chunk-Miss mechanism at animal level
    → KHÔNG cần PFC — mechanism ở body-base level

    Chó ăn đồ ngon quen → chê đồ rẻ:
    → Baseline shift: quality cao = new normal
    → Đồ rẻ = Chunk-Miss → body signal refuse
    → Training lại: sustained quality thấp → re-habituate → accept
    → = Same mechanism as rat SNC


  ĐẶC TÍNH QUAN TRỌNG:

    ① BIDIRECTIONAL: baseline shift LÊN và XUỐNG đều được
    ② ASYMMETRIC: shift LÊN dễ hơn shift XUỐNG
       → 🟢 Loss aversion (Kahneman & Tversky 1979): losing hurts ~2x gaining
       → Body resist quality decrease MẠNH hơn accept quality increase
    ③ DOMAIN-SPECIFIC: baseline shift ĐỘC LẬP per domain
       → Đồ ăn baseline và quần áo baseline shift RIÊNG
       → Có thể quen đồ ăn ngon nhưng chưa quen quần áo đẹp
    ④ INDIVIDUAL: mỗi người baseline KHÁC vì experience KHÁC
       → Cùng 1 chất lượng → người A thấy "bình thường", người B "ngon"
       → = Per-person reward (03-Reward.md §5.9)
```

---

## §6 — MAP VÀO FRAMEWORK

### §6.1 — v7.8 Cycle Architecture

```
🟡 CHUNK DYNAMICS TRONG V7.8 PERCEPTION-ACTION CYCLE:

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  ① DOMAIN → BODY-INPUT (L0 + L1 receptors)                    │
  │     → SENSORY-DRIVEN input enters here                        │
  │                                                                │
  │  ② BODY-INPUT → UNCONSCIOUS (B + C + D zones)                 │
  │     → Chunks match against input                               │
  │     → PATTERN-DRIVEN input originates here (replay, preview)   │
  │                                                                │
  │     ⭐ CHUNK DYNAMICS FIRE HERE:                                │
  │     → Chunk-Shift: valence re-evaluated based on new info      │
  │     → Chunk-Miss: compiled baseline vs actual → delta          │
  │     → Chunk-Gap: network topology → inconsistency detected     │
  │     → Compound: multiple dynamics simultaneous                 │
  │                                                                │
  │  ③ UNCONSCIOUS → FEELING (integrated signal emerges)           │
  │     → Body-feedback signal (direction + magnitude)             │
  │     → Chunk dynamics determine QUALITY of signal               │
  │                                                                │
  │  ④ FEELING → PFC (observe, label, choose)                      │
  │     → PFC observes signal but may NOT know which dynamic       │
  │     → "Chạnh lòng" = PFC label for Chunk-Gap + Chunk-Shift     │
  │                                                                │
  │  ⑤ PFC → BODY-OUTPUT → DOMAIN → LOOP                          │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘


  ZONE MAP:

    D (Peripheral, PFC near-zero reach):
      → Sensory-driven input primary pathway
      → Chunk-Miss: gut baseline shift, cardiac patterns
      → Baseline shift compiled HERE → body signal WITHOUT PFC

    C (Subcortical, PFC limited reach):
      → Amygdala: Chunk-Shift (fear conditioning, valence flip)
      → VTA: Chunk-Miss detection (prediction-delta)
      → ACC: Chunk-Gap detection (inconsistency)
      → Hippocampus: Pattern-driven input (replay, preplay)

    B (Cortical, PFC trainable):
      → Complex chunk networks → all 3 dynamics
      → Chunk-Gap rich here (knowledge gaps, skill gaps)
      → Cortical modality areas hold compiled baselines

    A (PFC):
      → OBSERVE chunk dynamics output (feeling layer)
      → CAN bias: hold chunks → influence which dynamics fire
      → CANNOT directly cause dynamics (dynamics emerge from B+C+D)
      → PFC role: observe, label, choose response, orchestrate
```

### §6.2 — H10 Preconditions

```
🟡 CHUNK DYNAMICS × H10 5 PRECONDITIONS:

  H10: Signal fires khi ALL 5 preconditions met.
  Chunk dynamics MÔ TẢ HOW signal arises — H10 mô tả WHEN.

  ┌────────────────────┬─────────────┬─────────────┬─────────────┐
  │ H10 Precondition   │ Chunk-Shift │ Chunk-Miss  │ Chunk-Gap   │
  ├────────────────────┼─────────────┼─────────────┼─────────────┤
  │ P1 Schema pending  │ Shift tạo   │ Miss = body │ Gap = body  │
  │ (body-need gap)    │ NEW pending │ -need mất   │ -need thiếu │
  │                    │ (phản bội → │ quality     │ pattern     │
  │                    │ need fix)   │             │             │
  ├────────────────────┼─────────────┼─────────────┼─────────────┤
  │ P2 Chunks base     │ Cần chunks  │ Cần compiled│ Cần enough  │
  │ (đủ substrate)     │ để evaluate │ baseline    │ network to  │
  │                    │ new info    │ (no compile │ DETECT gap  │
  │                    │             │ = no miss)  │             │
  ├────────────────────┼─────────────┼─────────────┼─────────────┤
  │ P3 prediction-     │ Shift =     │ Miss = neg. │ Gap detect  │
  │ delta              │ valence     │ prediction  │ = ACC       │
  │ (biến động đủ)     │ delta       │ error       │ signal      │
  ├────────────────────┼─────────────┼─────────────┼─────────────┤
  │ P4 Goldilocks      │ Shift xảy   │ N/A (body   │ Gap phải    │
  │ (40-70% match)     │ ra ở BẤT KỲ │ already     │ detectable  │
  │                    │ match level │ knows)      │ (not too    │
  │                    │             │             │ alien)      │
  ├────────────────────┼─────────────┼─────────────┼─────────────┤
  │ P5 Chunk tag       │ NEW valence │ Compiled    │ Compiled    │
  │ (opioid/cortisol)  │ tag from    │ baseline    │ surrounding │
  │                    │ shift event │ carries tag │ chunks tag  │
  └────────────────────┴─────────────┴─────────────┴─────────────┘

  INSIGHTS:
  → Chunk-Miss KHÔNG CẦN P4 (Goldilocks) — body already has baseline
  → Chunk-Gap CẦN P2 (enough network to detect gap)
  → Chunk-Shift CẦN P3 (delta đủ lớn để register)
  → Compound = P1-P5 checked MULTIPLE TIMES per dynamic
```

---

## §7 — RESEARCH ANCHORS

```
🟢 HIGH CONFIDENCE (each component well-established):

  CHUNK-MISS MECHANISM:
    🟢 Successive Negative Contrast: Crespi 1942, Flaherty 1996
    🟢 Reward prediction error: Schultz, Dayan, Montague 1997
    🟢 Frustration theory: Amsel 1958, 1992
    🟢 Wanting vs liking: Berridge & Robinson 1998, 2003
    🟢 Loss aversion ~2x: Kahneman & Tversky 1979
    🟢 Hedonic adaptation: Brickman, Coates, Janoff-Bulman 1978

  CHUNK-SHIFT MECHANISM:
    🟢 Fear conditioning: LeDoux 1996
    🟢 Evaluative conditioning: De Houwer 2007
    🟢 Extinction ≠ erasure: Bouton 2004
    🟢 Memory reconsolidation: Nader, Schafe, LeDoux 2000
    🟢 Spreading activation: Collins & Loftus 1975

  CHUNK-GAP MECHANISM:
    🟢 ACC error/conflict detection: Bush, Luu, Posner 2000
    🟢 Cognitive dissonance: Festinger 1957
    🟢 Information gap theory (curiosity): Loewenstein 1994
    🟢 Aha moment + ACC: Kounios & Beeman 2009
    🟢 Felt sense: Gendlin 1978

  INPUT SOURCES:
    🟢 Sensory processing: established neuroscience
    🟢 Hippocampal replay: Wilson & McNaughton 1994
    🟢 Hippocampal preplay: Pfeiffer & Foster 2013
    🟢 Social comparison: Festinger 1954

  GAP DYNAMICS:
    🟢 Goal gradient effect: Hull 1932
    🟢 Progress principle: Amabile & Kramer 2011


🟡 FRAMEWORK SYNTHESIS (novel integration):

  🟡 2-source classification (Sensory-Driven / Pattern-Driven):
     Components established. Classification = framework contribution.

  🟡 3-dynamic classification (Shift / Miss / Gap):
     Each mechanism established individually.
     Unified taxonomy as ORTHOGONAL chunk dynamics = framework contribution.

  🟡 Compound mechanism:
     Multi-signal co-occurrence recognized in affect research.
     Formalization via chunk dynamics = framework contribution.

  🟡 Quality Baseline Shift as bridge (Sensory → Miss):
     SNC + hedonic adaptation established.
     Framing as chunk compile mechanism = framework contribution.

  🟡 Gap → Novelty drive foundation:
     Curiosity research established (Loewenstein).
     Formalization via chunk network topology = framework contribution.

  🟡 Gap → Miss transition via Imagine-Final preview:
     Hedonic adaptation + preview compile established individually.
     Transition mechanism = framework contribution.

  🟡 Gap decomposition / mini-arc dynamics:
     Goal gradient (Hull 1932) + progress principle (Amabile 2011) established.
     Formalization as gap decomposition = framework contribution.

  🟡 3+1 Chunk-Miss variants (rõ / mờ / vô thức / irresolvable):
     Each observable. Taxonomy = framework contribution.
     v1.3→v2.0: ⓓ irresolvable = hardware prevents resolution (Parkinson drill).

  🟡 Context-free chunk as Pattern-Driven variant:
     PTSD drill: flashback = ⓕ context-free chunk fires internally.
     Consistent Brewin 2010 DRT + Chunk.md §2.6 context-tag model.

  🟡 v2.0 NEW — Body-Need as aggregate output:
     Body-need concept established in motivation research.
     Framing as aggregate of 2-source × 3-dynamics = framework contribution.

  🟡 v2.0 NEW — Complexity Spectrum (Simple → Social → Meta):
     Each substrate level observable. Unified taxonomy = framework contribution.
     Tầng ③ collapse: meta-level = same dynamics, different substrate.

  🟡 v2.0 NEW — Cross-cutting clarification:
     Observation parameters + state modifiers ≠ sources.
     Conceptual clarification = framework contribution.


🔴 SPECULATIVE:

  🔴 Exact compound signal summation formula
  🔴 Precise timeline for baseline shift (1 vs 10 vs 100 exposures)
  🔴 ACC as primary Gap detector (vs other conflict detection circuits)
  🔴 Chunk-Miss variant boundaries (clear threshold between rõ/mờ/vô thức)
  🔴 Gap → Miss transition: exact preview repetition count for baseline shift
  🔴 Gap decomposition: optimal mini-gap size for sustained drive
```

---

## §8 — HONEST ASSESSMENT

```
STRENGTHS:
  ✅ Match v7.8 chunk-centric principle
  ✅ Each dynamic grounded in established research
  ✅ Explains phenomena current framework describes but doesn't MECHANIZE:
     → Compound dissonance (100k example)
     → Social dissonance without body-input change (chị-A/chị-B)
     → Animal body-feedback (SNC without PFC)
     → Felt sense gap detection (Gendlin, before PFC verbal)
  ✅ Provides foundation for Novelty drive (Chunk-Gap loop)
  ✅ Orthogonal to existing 3 trục — BỔ SUNG, không THAY THẾ
  ✅ v2.0: Body-Need aggregate framing connects dynamics → behavior
  ✅ v2.0: Complexity Spectrum shows parsimony (3 dynamics → all levels)

LIMITATIONS:
  ⚠ 3 dynamics boundary: some cases COULD be classified differently
     → Betrayal: is it Shift (valence change) or Gap (trust resolution gap)?
     → Answer: COMPOUND — cả 2 fire. Boundary is soft.
  ⚠ Exact neural pathways for each dynamic not fully mapped
  ⚠ Compound summation is conceptual, not quantified
  ⚠ Baseline shift timeline lacks precise dose-response data
  ⚠ Body-Need aggregate concept = framework synthesis, not independently tested
  ⚠ Complexity Spectrum levels (Simple/Social/Meta) = useful heuristic,
     not sharp categories — actual substrate is continuous

WHAT THIS FILE DOES NOT DO:
  ✗ Replace intensity classification (02-Dissonance.md)
  ✗ Replace source classification (02-Dissonance.md §3)
  ✗ Replace H10 preconditions (Body-Feedback.md §5)
  ✗ Replace case analyses (01-04 files)
  ✗ Replace inter-body mechanism (Inter-Body-Mechanism.md)
  → File này THÊM trục phân loại + aggregate framing, không xóa trục nào
```

---

## §9 — CROSS-REFERENCES

```
📚 INTER-BODY MECHANISM (v2.0 NEW):
  → Inter-Body-Mechanism.md v1.0 — Body-Need §2, 3-cost §4, 5-channel §6
    → §2 Body-Need aggregate: full 7 properties + 4 immediacy types
    → §2.3 Cross-cutting: obs params + state modifiers ≠ sources
    → §2.2 Complexity spectrum: Simple→Social→Meta
    → §4 3-cost model: PFC draft + suppress + uncertainty
    → §6 5-channel input vector: trigger = vector, not single source

📚 REWARD ARCHITECTURE:
  → Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State dimension, 5 Profiles, Interaction Model
    → §2 Evaluative/Direct-State maps to: Sensory-Driven ≈ Direct-State, Pattern-Driven ≈ Evaluative
    → §3 Evaluative Gates Direct-State = evaluation modulates body-state
    → §6 Conditional Interaction Model = replaces simple additive compound

📚 WITHIN BODY-FEEDBACK FOLDER:
  → Body-Feedback.md v1.1 — §2 dual-pull, §5 H10 5 preconditions
  → Body-Feedback-Label.md v2.0 — 3-tier vocabulary reference
  → 01-Foundation.md §3 — 6-step interface loop
  → 01-Foundation.md §5 — body-feedback vs feeling 7-layer
  → 02-Dissonance.md §2 — 5 mini dissonance cases (per dynamics relabel)
  → 02-Dissonance.md §3 — 3 Genuine Discomfort Sources
  → 02-Dissonance.md §8 — trauma loop (compound Shift + Miss + Gap)
  → 02-Dissonance.md §9 — hedonic trap (Chunk-Miss from schema decay)
  → 03-Reward.md §2 — VTA 7-step loop
  → 03-Reward.md §4 — 7 reward cases (per dynamics relabel)
  → 03-Reward.md §5 — ô tô paradox (per-person Chunk-Miss/Gap)
  → 04-Integration.md §6-8 — Einstein/hedonic/trauma walkthroughs

📚 HEALTH CONDITIONS (v1.3 preserved):
  → PTSD-Analysis.md v1.0 §4 — flashback = context-free chunk fire (→ §2.3 ⓕ)
  → Parkinson-Analysis.md v1.1 §5.2 — chronic irresolvable prediction-delta (→ §3.2 ⓓ)
  → Chunk.md v2.2 §2.6 — context-tag model (4 metadata types, 2 chunk types)

📚 CHUNK SYSTEM:
  → Chunk.md v2.2 §1-§4 — substrate, compile, connections, activation
  → Chunk-Activation-Dynamics.md §2 — probability distribution
  → Chunk-Activation-Dynamics.md §3 — competitive re-linking (Shift mechanism)
  → Chunk-Activation-Dynamics.md §4 — trigger surface

📚 VALENCE + FEELING:
  → Valence-Propagation.md v1.4 — valence per-entity + chain propagation
  → Feeling.md v2.0 — PFC observation of body-feedback (output of dynamics)
  → Somatic-Articulation-Loop.md — felt sense = Gap detection pre-verbal

📚 GAP + DIRECTION:
  → Gap-Direction.md v1.1 — gap has direction = f(surrounding chunks)
    → 4 properties, 2-layer model, unified Tier 1-4
    → "Chưa biết = không có gap" principle
  → Cortisol-Baseline.md v2.0 §3.5 — chunk association tag (Shift mechanism)
  → Cortisol-Baseline.md v2.0 §3.8 — holding signal (Gap→Miss accelerator)

📚 OTHER FRAMEWORK:
  → Core-v7.8-Draft.md §1 — perception-action cycle
  → Core-v7.8-Draft.md §4 — unconscious processing (where dynamics fire)
  → Observation/Boredom.md — Chunk-Miss variant ⓑ (miss mờ) + 2-chiều formula
  → Observation/Novelty.md — Chunk-Gap = foundation mechanism
  → Observation/Connection.md §1.3 — 4 Cases mapped to chunk dynamics
     (Đủ=Chunk-Miss, Mất=Chunk-Miss++, Thiếu=Chunk-Gap, Toxic=Chunk-Shift)
  → PFC/Imagination/Imagination.md — preview = Pattern-Driven source

📚 KEY RESEARCH (30+ citations):
  🟢 Amabile & Kramer 2011 — progress principle
  🟢 Amsel 1958, 1992 — frustration theory
  🟢 Berridge & Robinson 1998, 2003 — wanting vs liking
  🟢 Bouton 2004 — extinction ≠ erasure
  🟢 Brewin 2010 — Dual Representation Theory (S-rep/C-rep)
  🟢 Brickman et al. 1978 — hedonic adaptation
  🟢 Bush, Luu, Posner 2000 — ACC conflict detection
  🟢 Collins & Loftus 1975 — spreading activation
  🟢 Crespi 1942, 1944 — successive contrast
  🟢 De Houwer 2007 — evaluative conditioning
  🟢 Festinger 1954 — social comparison
  🟢 Festinger 1957 — cognitive dissonance
  🟢 Flaherty 1996 — consummatory successive contrast
  🟢 Gendlin 1978 — focusing, felt sense
  🟢 Hull 1932 — goal gradient effect
  🟢 Kahneman & Tversky 1979 — loss aversion
  🟢 Kounios & Beeman 2009 — aha moments, ACC
  🟢 LeDoux 1996 — fear conditioning, low road
  🟢 Loewenstein 1994 — information gap theory of curiosity
  🟢 Nader, Schafe, LeDoux 2000 — reconsolidation
  🟢 Pfeiffer & Foster 2013 — hippocampal preplay
  🟢 Schultz, Dayan, Montague 1997 — reward prediction error
  🟢 Walker 2017 — sleep consolidation
  🟢 Wilson & McNaughton 1994 — hippocampal replay
```

---

> **END OF Body-Feedback-Mechanism.md v2.0**
>
> **CHANGELOG v1.3 → v2.0:**
>   ✅ NEW §1: Body-Need aggregate output (definition, 2 sources, cross-cutting,
>      7 properties, 4 immediacy). Bridges "dynamics fire" → "body cần gì."
>   ✅ NEW §2.5: Complexity Spectrum (Simple→Social→Meta) + Tầng ③ collapse.
>      3 dynamics explain ALL substrate levels → parsimony.
>   ✅ §1.3: Cross-cutting clarification (obs params + state modifiers ≠ sources).
>   ✅ §3.3 restructured: sub-sections (core/novelty/transition/decomposition).
>   ✅ §6: Merged v7.8 map + H10 map into single section.
>   ✅ §8-§9: Updated assessment + cross-refs for new content + Inter-Body ref.
>   ✅ All v1.3 content preserved: 2-source, 3 dynamics, compound, baseline shift,
>      context-free chunk ⓕ, irresolvable miss ⓓ, ALL 30+ research citations.
>
> **Summary:** Core mechanism reference for body-feedback chunk dynamics:
>   §1: Body-Need = aggregate output (NEW v2.0)
>   §2: 2 input sources + Complexity Spectrum (NEW v2.0)
>   §3: 3 chunk dynamics (restructured Gap sub-sections)
>   §4: Compound mechanism (Conditional Interaction Model)
>   §5: Quality Baseline Shift (SNC bridge)
>   §6: Framework maps (v7.8 + H10)
>   §7-§9: Research + Assessment + Cross-refs
>
> **Trục thứ 4**: orthogonal to existing 3 trục (direction, magnitude, source).
> **Foundation**: Chunk-Gap = Novelty drive mechanism.
> **Key research**: SNC (Crespi 1942) proves Chunk-Miss at animal level.
> **v2.0 core additions**: Body-Need aggregate + Complexity Spectrum +
>   Cross-cutting clarification. All 3 derive from Inter-Body drill insights.
>
> **Phiên bản:** v2.0, 2026-05-16.
