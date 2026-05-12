# Plan: Refine Framework → Body-Feedback-Label Vocabulary

> **Mục tiêu**: Toàn bộ framework dùng 100% vocabulary theo Body-Feedback-Label.md v1.1.
> **Nguyên tắc**: CHỈ Clarification/ folder mới dùng từ "PE" / "prediction error".
> **Tạo**: 2026-05-12

---

## QUY TẮC THAY THẾ

```
┌───────────────────────────────┬──────────────────────────────────────────┐
│ CŨ (cần thay)                │ MỚI (framework vocabulary)               │
├───────────────────────────────┼──────────────────────────────────────────┤
│ PE (dùng chung / mơ hồ)      │ Tùy context:                             │
│                               │   → prediction-delta (nếu = detection)   │
│                               │   → body-base reward (nếu = reward)      │
│                               │   → dissonance (nếu = mismatch âm)      │
│                               │   → body-feedback (nếu = chung cả +/-)  │
│                               │                                          │
│ prediction error (noun)       │ prediction-delta                         │
│                               │ (= detection signal, Step 2, chưa +/-)  │
│                               │                                          │
│ VTA delta                     │ prediction-delta                         │
│                               │ (function-based, không anatomy-based)    │
│                               │                                          │
│ PE signal / PE response       │ prediction-delta / body-feedback         │
│                               │ (tùy context detection hay response)     │
│                               │                                          │
│ PE positive / PE dương        │ prediction-delta dương                   │
│                               │ (detection: vượt prediction)             │
│                               │                                          │
│ PE negative / PE âm           │ prediction-delta âm                      │
│                               │ (detection: dưới prediction → SNC)       │
│                               │                                          │
│ opioid confirm (dùng chung)   │ body-base reward                         │
│                               │ (cover CẢ Type A VÀ Type B)             │
│                               │                                          │
│ PE sensitivity                │ prediction-delta sensitivity             │
│                               │ (DRD4 filter threshold)                  │
│                               │                                          │
│ PE-driven                     │ prediction-delta-driven                  │
│                               │                                          │
│ PE = reward                   │ XÓA hoặc clarify:                        │
│                               │ prediction-delta ≠ body-base reward      │
│                               │ (Step 2 detection ≠ Step 5 evaluation)   │
└───────────────────────────────┴──────────────────────────────────────────┘

  ⚠️ NGOẠI LỆ — GIỮ NGUYÊN:
    → Clarification/ folder: PE discussion là MỤC ĐÍCH file
    → Research citations: "Schultz (1997) prediction error" = tên gốc paper
    → Khi quote mainstream neuroscience terminology (trong Clarification context)

  ⚠️ CLARIFICATION FILES — THÊM CROSS-REF:
    → Thêm reference tới Body-Feedback-Label.md
    → "Framework dùng 'prediction-delta' thay cho 'PE'" — note rõ
```

---

## TỔNG QUAN PHASES

```
  Phase │ Scope                        │ Files │ ~Refs │ Priority
  ──────┼──────────────────────────────┼───────┼───────┼──────────
    1   │ Body-Feedback Core           │   9   │  ~85  │ ⭐⭐⭐ HIGHEST
    2   │ Body-Base Core               │   5   │  ~35  │ ⭐⭐⭐
    3   │ Feeling                      │   4   │  ~10  │ ⭐⭐
    4   │ Chunk                        │   8   │  ~28  │ ⭐⭐
    5   │ Observation                  │   7   │  ~17  │ ⭐⭐
    6   │ PFC + Imagination            │   5   │   ~8  │ ⭐
    7   │ Domain + Melody              │   2   │  ~13  │ ⭐
    8   │ Core Top-level               │   4   │  ~10  │ ⭐
    9   │ Research                     │   9   │  ~40  │ ⭐
   10   │ Meta-Impact + Education      │   4   │   ~5  │ ⭐
   11   │ Entry Points (Ask-AI, Index) │   3   │  ~15  │ ⭐⭐
    C   │ Clarification (cross-ref)    │   3   │ KEEP  │ ⭐
  ──────┼──────────────────────────────┼───────┼───────┼──────────
  TOTAL │                              │  ~63  │ ~266+ │
  ──────┴──────────────────────────────┴───────┴───────┴──────────

  SKIP: backup/ files, draft/analysis files (lower priority, later)
```

---

## PHASE 1: BODY-FEEDBACK CORE (9 files)

> Foundation — Body-Feedback-Label.md chính là vocabulary reference,
> nên FOLDER CỦA NÓ phải clean nhất.

```
  # │ File                          │ PE │ pred-err │ VTA-δ │ Total
  ──┼───────────────────────────────┼────┼──────────┼───────┼──────
  1 │ 03-Reward.md                  │  — │     4    │  21   │  ~25  ← HEAVIEST
  2 │ Reward-Calibration.md         │ 22 │     —    │   2   │  ~24
  3 │ Gap-Direction.md              │  — │    14    │   2   │  ~16
  4 │ 01-Foundation.md              │  2 │     2    │   5   │   ~9
  5 │ 04-Integration.md             │  3 │     3    │   2   │   ~8
  6 │ Body-Feedback.md              │  1 │     2    │   3   │   ~6
  7 │ Reward-Signal-Architecture.md │  — │     2    │   1   │   ~3
  8 │ Body-Feedback-Mechanism.md    │  — │     2    │   1   │   ~3
  9 │ 02-Dissonance.md              │  — │     —    │   1   │   ~1
  ──┴───────────────────────────────┴────┴──────────┴───────┴──────
                                    SUBTOTAL:          ~95
```

---

## PHASE 2: BODY-BASE CORE (5 files)

```
  # │ File                    │ PE │ pred-err │ VTA-δ │ Total
  ──┼─────────────────────────┼────┼──────────┼───────┼──────
  1 │ Why-Body-Knows.md       │ 13 │     4    │   1   │  ~18
  2 │ Valence-Propagation.md  │  — │     2    │   4   │   ~6
  3 │ Body-Base.md            │  — │     3    │   3   │   ~6
  4 │ Cortisol-Baseline.md    │  — │     1    │   2   │   ~3
  5 │ Schema.md               │  — │     —    │   2   │   ~2
  ──┴─────────────────────────┴────┴──────────┴───────┴──────
                              SUBTOTAL:          ~35
```

---

## PHASE 3: FEELING (4 files)

```
  # │ File                      │ PE │ pred-err │ VTA-δ │ Total
  ──┼───────────────────────────┼────┼──────────┼───────┼──────
  1 │ Feeling-Sources.md        │  — │     3    │   —   │   ~3
  2 │ Feeling-Mechanism-Deep.md │  — │     —    │   3   │   ~3
  3 │ Feeling.md                │  — │     1    │   1   │   ~2
  4 │ Feeling-Literacy-Training │  — │     1    │   1   │   ~2
  ──┴───────────────────────────┴────┴──────────┴───────┴──────
                                SUBTOTAL:          ~10
```

---

## PHASE 4: CHUNK (8 files)

```
  # │ File                             │ PE │ pred-err │ VTA-δ │ Total
  ──┼──────────────────────────────────┼────┼──────────┼───────┼──────
  1 │ 09-Learning-Cycle.md             │  — │     7    │   —   │   ~7
  2 │ Social-Recognition-Arc.md        │  — │     7    │   —   │   ~7
  3 │ 04-Right-Wrong-Vague.md          │  — │     6    │   —   │   ~6
  4 │ Womb-to-Birth-Baseline.md        │  — │     3    │   —   │   ~3
  5 │ 02-Cross-Network-Transfer.md     │  — │     2    │   —   │   ~2
  6 │ 01c-Chunk-Discovery-Lifecycle.md │  — │     —    │   1   │   ~1
  7 │ Visual-System-Arc.md             │  — │     1    │   —   │   ~1
  8 │ 00-Chunk-System-Sketch.md        │  — │     —    │   1   │   ~1
  ──┴──────────────────────────────────┴────┴──────────┴───────┴──────
                                       SUBTOTAL:          ~28

  NOTE: Social-Recognition-Arc + Womb-to-Birth + Visual-System
        có bản VI/ tương ứng → refine song song.
```

---

## PHASE 5: OBSERVATION (7 files)

```
  # │ File                    │ PE │ pred-err │ VTA-δ │ Total
  ──┼─────────────────────────┼────┼──────────┼───────┼──────
  1 │ Protect.md              │  2 │     3    │   —   │   ~5
  2 │ Liking-Wanting.md       │  1 │     1    │   3   │   ~5
  3 │ Novelty.md              │  — │     2    │   3   │   ~5
  4 │ Gratitude.md            │  — │     —    │   3   │   ~3
  5 │ Connection.md           │  — │     1    │   —   │   ~1
  6 │ Obligation.md           │  — │     1    │   —   │   ~1
  7 │ AI-Schema-Detection.md  │  — │     —    │   1   │   ~1
  ──┴─────────────────────────┴────┴──────────┴───────┴──────
                              SUBTOTAL:          ~21
```

---

## PHASE 6: PFC + IMAGINATION (5 files)

```
  # │ File                        │ PE │ pred-err │ VTA-δ │ Total
  ──┼─────────────────────────────┼────┼──────────┼───────┼──────
  1 │ Somatic-Articulation-Loop   │  — │     —    │   3   │   ~3
  2 │ PFC-Hardware.md             │  — │     1    │   1   │   ~2
  3 │ PFC-Function.md             │  — │     —    │   1   │   ~1
  4 │ Logic-Feeling.md            │  — │     —    │   1   │   ~1
  5 │ Logic-Feeling-Balance.md    │  — │     1    │   —   │   ~1
  ──┴─────────────────────────────┴────┴──────────┴───────┴──────
                                  SUBTOTAL:           ~8
```

---

## PHASE 7: DOMAIN + MELODY (2 files)

```
  # │ File                    │ PE │ pred-err │ VTA-δ │ Total
  ──┼─────────────────────────┼────┼──────────┼───────┼──────
  1 │ Domain-Mapping-Drive.md │  — │     6    │   6   │  ~12
  2 │ Personal-Melody.md      │  — │     1    │   —   │   ~1
  ──┴─────────────────────────┴────┴──────────┴───────┴──────
                              SUBTOTAL:          ~13
```

---

## PHASE 8: CORE TOP-LEVEL (4 files)

```
  # │ File                      │ PE │ pred-err │ VTA-δ │ Total
  ──┼───────────────────────────┼────┼──────────┼───────┼──────
  1 │ Core-Software.md          │  — │     1    │   3   │   ~4
  2 │ Neural-Architecture.md    │  1 │     2    │   —   │   ~3
  3 │ Modality.md               │  1 │     1    │   —   │   ~2
  4 │ Neural-Processing-Flow.md │  — │     1    │   —   │   ~1
  ──┴───────────────────────────┴────┴──────────┴───────┴──────
                                SUBTOTAL:          ~10
```

---

## PHASE 9: RESEARCH (9 files)

```
  # │ File                          │ PE │ pred-err │ VTA-δ │ Total
  ──┼───────────────────────────────┼────┼──────────┼───────┼──────
  1 │ Fidgeting-Analysis.md         │  — │    17    │   —   │  ~17
  2 │ Child-Development-Mechanism   │  1 │     4    │   —   │   ~5
  3 │ Expansion-Saturation-Crisis   │  — │     1    │   4   │   ~5
  4 │ Idol-Phenomenon.md            │  — │     —    │   5   │   ~5
  5 │ Addiction-Analysis.md         │  — │     1    │   4   │   ~5
  6 │ OCD-Analysis.md               │  — │     3    │   —   │   ~3
  7 │ Religion.md                   │  — │     —    │   2   │   ~2
  8 │ Love-Romantic.md              │  — │     1    │   —   │   ~1
  9 │ Innovation-Geography.md       │  — │     1    │   —   │   ~1
  ──┴───────────────────────────────┴────┴──────────┴───────┴──────
                                    SUBTOTAL:          ~44
```

---

## PHASE 10: META-IMPACT + EDUCATION (4 files)

```
  # │ File                       │ PE │ pred-err │ VTA-δ │ Total
  ──┼────────────────────────────┼────┼──────────┼───────┼──────
  1 │ Curriculum-Framework.md    │  1 │     —    │   —   │   ~1
  2 │ Education-Arms-Race.md     │  — │     —    │   1   │   ~1
  3 │ Creator-Lens.md            │  — │     1    │   —   │   ~1
  4 │ Epistemological-Position   │  1 │     —    │   —   │   ~1
  ──┴────────────────────────────┴────┴──────────┴───────┴──────
                                 SUBTOTAL:           ~4
```

---

## PHASE 11: ENTRY POINTS (3 files)

> Đây là nơi AI + người đọc TIẾP CẬN ĐẦU TIÊN → phải clean.

```
  # │ File              │ PE │ pred-err │ VTA-δ │ Total
  ──┼───────────────────┼────┼──────────┼───────┼──────
  1 │ Ask-AI.md         │  3 │     5    │   1   │   ~9
  2 │ 01-File-Index.md  │  2 │     2    │   1   │   ~5
  3 │ README.md         │  — │     1    │   —   │   ~1
  ──┴───────────────────┴────┴──────────┴───────┴──────
                        SUBTOTAL:          ~15
```

---

## PHASE C: CLARIFICATION (3 files — SPECIAL)

> PE discussion THUỘC VỀ ĐÂY. GIỮ PE. CHỈ THÊM CROSS-REF.

```
  # │ File                              │ Action
  ──┼───────────────────────────────────┼──────────────────────────────────
  1 │ Prediction-Error-Is-Not-Reward.md │ THÊM note: framework dùng
    │ (PE:116, pred-err:14, VTA-δ:4)   │ "prediction-delta" → ref Label.md
  2 │ Dopamine-Reward-Rejection.md      │ THÊM note: framework vocabulary
    │ (PE:9, pred-err:7, VTA-δ:1)      │ → ref Body-Feedback-Label.md
  3 │ Cortisol-Amplifier-Not-Cause.md   │ Nhỏ. Thêm cross-ref nếu cần.
    │ (pred-err:2)                      │
  ──┴───────────────────────────────────┴──────────────────────────────────
```

---

## QUY TRÌNH REFINE MỖI FILE

```
  Bước 1: ĐỌC toàn bộ file → hiểu context từng vị trí PE/VTA delta
  Bước 2: XÁC ĐỊNH label thay thế theo Body-Feedback-Label.md:
           → PE nào = prediction-delta? (detection, Step 2)
           → PE nào = body-base reward? (evaluation, Step 5)
           → PE nào = dissonance / chunk-miss / SNC? (negative)
           → PE nào = body-feedback? (chung cả mechanism)
           → VTA delta nào → prediction-delta?
  Bước 3: THAY THẾ từng vị trí — kiểm tra câu vẫn mạch lạc
  Bước 4: VERIFY — grep PE / VTA delta → 0 kết quả (trừ citations)
  Bước 5: DONE — đánh dấu hoàn thành, chuyển file tiếp
```

---

## TRACKING

```
  Phase │ Status      │ Files Done │ Notes
  ──────┼─────────────┼────────────┼──────────
    1   │ ✅ DONE     │    9/9     │ 2026-05-12
    2   │ ✅ DONE     │    5/5     │ 2026-05-12 (WBK §2: 13 PE kept=clarification)
    3   │ ✅ DONE     │    4/4     │ 2026-05-12
    4   │ ✅ DONE     │   12/12    │ 2026-05-12 (incl. extra files found)
    5   │ ✅ DONE     │    7/7     │ 2026-05-12
    6   │ ✅ DONE     │    5/5     │ 2026-05-12
    7   │ ✅ DONE     │    2/2     │ 2026-05-12
    8   │ ✅ DONE     │    4/4     │ 2026-05-12
    9   │ ✅ DONE     │    9/9     │ 2026-05-12
   10   │ ✅ DONE     │    4/4     │ 2026-05-12
   11   │ ✅ DONE     │    3/3     │ 2026-05-12
    C   │ ✅ DONE     │    3/3     │ 2026-05-12 Cross-refs + vocab notes added
  ──────┼─────────────┼────────────┼──────────
  TOTAL │             │    0/63    │
```

---

> *Plan created 2026-05-12.*
> *Reference: Body-Feedback-Label.md v1.1 (532L).*
> *~63 files, ~266+ references, 12 phases.*
> *Chậm mà chắc. Từng file một.*
