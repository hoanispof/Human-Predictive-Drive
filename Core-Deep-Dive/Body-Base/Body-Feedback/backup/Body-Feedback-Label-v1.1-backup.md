---
title: Body-Feedback Label Convention — Vocabulary Reference
version: 1.1
created: 2026-05-12
refined: 2026-05-12 (v1.1 — pure framework vocabulary, prediction-delta, no external terminology)
status: REFERENCE v1.1
scope: |
  VOCABULARY REFERENCE: Quy ước label cho toàn bộ body-feedback system.
  Formalize 3-tier label system: General → Direction → Specific.
  File này = MUST-READ ngay sau Body-Feedback.md.
  Mọi file trong framework nên dùng vocabulary theo quy ước này.
  100% FRAMEWORK VOCABULARY — không dùng terminology ngoài framework.
purpose: |
  Framework phân tích body-feedback qua 4 trục, 7-step mechanism,
  Type A/B, A₀→A₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles.
  Nhưng labels CHƯA BAO GIỜ được formalize.
  File này giải quyết: formalize vocabulary thống nhất cho toàn framework.
  Giải quyết 2 vấn đề cụ thể:
    → "opioid confirm" chỉ cover Type A, bỏ sót Type B
    → "sướng/khó chịu" nhầm body-feedback (mechanism) với feeling (observation)
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — ngang hàng Body-Feedback-Mechanism.md.
  ĐỌC NGAY SAU Body-Feedback.md (entry point).
dependencies:
  - Body-Feedback.md v1.1 — §2 dual-pull, §4 4 trục, §5 3 nguồn, §6 H10
  - Body-Feedback-Mechanism.md v1.2 — §2 2 sources, §3 3 dynamics, §4 compound
  - Reward-Signal-Architecture.md v1.0 — §1 Type A/B, §2 A₀→A₃, §4 5 Profiles
  - 03-Reward.md v1.1 — §2 7-step mechanism, §3 H10, Step 5 body-base check
  - Cortisol-Baseline.md v2.0 — §7.7 5 Roles
  - Valence-Propagation.md v1.4 — approach/avoidance tags
  - Feeling.md v2.0 — PFC observation of body-feedback (khác tầng)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Label Convention — Vocabulary Reference

> **Framework phân tích body-feedback qua 4 trục, 7-step mechanism,**
> **Type A/B, A₀→A₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles...**
>
> **Nhưng khi VIẾT/NÓI, labels CHƯA BAO GIỜ được formalize.**
>
> **File này: QUY ƯỚC LABEL cho toàn framework.**
> **100% framework vocabulary. Đọc ngay sau Body-Feedback.md.**

---

## Mục lục

- §0 — TẠI SAO CẦN FILE NÀY
- §1 — 3-TIER LABEL SYSTEM
- §2 — POSITIVE: BODY-BASE REWARD LABELS
- §3 — NEGATIVE: DISSONANCE LABELS
- §4 — DETECTION: PREDICTION-DELTA LAYER (RIÊNG BIỆT)
- §5 — NEUTRAL: BODY-FEEDBACK BASELINE
- §6 — COMPILED: VALENCE TAGS
- §7 — OBSERVATION VS MECHANISM (KHÁC TẦNG)
- §8 — QUY TẮC SỬ DỤNG
- §9 — CROSS-REFERENCES

---

## §0 — TẠI SAO CẦN FILE NÀY

```
⭐ FRAMEWORK CÓ MECHANISMS CHÍNH XÁC — THIẾU CONVENTION DÙNG LABEL:

  Body-feedback system có:
    → 4 trục phân loại orthogonal (Body-Feedback-Mechanism.md §1)
    → 7-step mechanism từ detection → reward (03-Reward.md §2)
    → Type A/B reward distinction (Reward-Signal-Architecture.md §1)
    → A₀→A₃ complexity gradient + 5 Profiles
    → 3 chunk dynamics (Chunk-Shift/Miss/Gap)
    → 5 cortisol Roles (Cortisol-Baseline.md §7.7)

  NHƯNG: chưa có quy ước DÙNG LABEL NÀO khi viết/nói.
  → Cùng 1 hiện tượng → dùng 5 từ khác nhau → mơ hồ


  2 VẤN ĐỀ CỤ THỂ:

  ① "OPIOID CONFIRM" CHỈ COVER TYPE A:

    Type A reward: μ-opioid → hedonic hotspot → ĐÚNG "opioid confirm"
    Type B reward: CT afferents / endocannabinoid / thermoreceptor → KHÔNG opioid

    "Opioid confirm" dùng chung = bỏ sót Type B = mất nuance
    → Correct general label = "body-base reward" (cover CẢ A VÀ B)
    (Reward-Signal-Architecture.md §1.1)


  ② NHẦM LẪN BODY-FEEDBACK VỚI FEELING:

    Body-feedback = MECHANISM (signal từ body, chạy 24/7, 95% vô thức)
    Feeling = OBSERVATION (PFC quan sát body-feedback → 7-layer gradient)
    "Sướng" = feeling label (PFC đã observe + label)
    KHÔNG phải body-feedback label

    → Khác TẦNG: body-feedback → feeling (có thể không observe được)
    → §7 file này phân biệt rõ
    (Feeling.md v2.0)


  ⭐ FILE NÀY GIẢI QUYẾT:
    → Formalize vocabulary thống nhất cho toàn framework
    → 3-tier system: cụ thể nhất có thể, chung nhất nếu bắt buộc
    → Clear convention → quality cao hơn → nhận diện chính xác hơn
```

---

## §1 — 3-TIER LABEL SYSTEM

```
⭐ QUY TẮC CHỌN TIER:

  Tier 3 (CỤ THỂ NHẤT) > Tier 2 (DIRECTION) > Tier 1 (CHUNG NHẤT)

  → Khi chain TRACE ĐƯỢC → dùng Tier 3
    "chunk-miss → SNC → cortisol Role ② Holding"

  → Khi biết DIRECTION + CHARACTER nhưng chain phức → dùng Tier 2
    "body-base reward" / "dissonance" / "threat"

  → Khi CHỈ BIẾT body phản hồi +/- mà không specific hơn → dùng Tier 1
    "body-feedback dương" / "body-feedback âm"


  AUDIENCE-APPROPRIATE:

    Chuyên gia / deep analysis:
      → Tier 3 chủ đạo
      → Chain trace rõ ràng

    Người muốn hiểu / Research files:
      → Tier 2 chủ đạo: "body-base reward", "dissonance", "chunk-miss"
      → Đủ chính xác, đủ hiểu mechanism cơ bản

    General / overview:
      → Tier 1 khi cần: "body-feedback dương/âm"
      → Có thể drill sâu hơn nếu người đọc yêu cầu
```

---

## §2 — POSITIVE: BODY-BASE REWARD LABELS

```
⭐ REWARD = BODY-BASE CONFIRM SIGNAL (body xác nhận: chunk KHỚP body-need)

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Nghĩa + khi nào dùng                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-feedback dương │ Chung nhất. Body phản hồi tích cực. │
  │ (chung) │                     │ Không specify mechanism.             │
  │         │                     │ Dùng: khi chỉ biết body response +  │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ body-base reward    │ Body xác nhận chunk khớp body-need.  │
  │ (type)  │                     │ Cover CẢ Type A VÀ Type B.           │
  │         │                     │ Dùng: khi biết rõ body confirm.      │
  │         │                     │                                      │
  │         │ reward              │ Viết tắt của body-base reward.       │
  │         │                     │ Dùng: khi context ĐÃ RÕ là          │
  │         │                     │ body-feedback (không nhầm sang khác).│
  │         │                     │                                      │
  │         │ Type A reward       │ Evaluative confirm. Opioid-based.    │
  │         │                     │ Cần H10 full. Chunk library rich.    │
  │         │                     │ Dùng: khi biết rõ là evaluative.     │
  │         │                     │                                      │
  │         │ Type B reward       │ Direct state confirm. Non-opioid.    │
  │         │                     │ Hardware-based. Ít habituate.        │
  │         │                     │ Dùng: khi biết rõ là body-state.     │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ μ-opioid confirm    │ Type A. Hedonic hotspot pathway.     │
  │ (cụ thể)│                     │ Dùng: khi trace chain tới NAcc/VP.   │
  │         │                     │                                      │
  │         │ CT afferent reward  │ Type B. Touch comfort pathway.       │
  │         │                     │ ~1-10cm/s optimal (Löken 2009).      │
  │         │                     │                                      │
  │         │ endocannabinoid     │ Type B. Exercise/runner's high.      │
  │         │ reward              │ CB1 pathway (Fuss 2015).             │
  │         │                     │                                      │
  │         │ A₀ / A₁ / A₂ / A₃  │ Type A complexity gradient.          │
  │         │                     │ A₀=hardware, A₃=expert evaluation.   │
  │         │                     │ (Reward-Signal-Architecture §2)      │
  │         │                     │                                      │
  │         │ Profile ①-⑤         │ 5 "hương vị" reward.                 │
  │         │                     │ Sensory/Coherence/Social/Relief/     │
  │         │                     │ Preview.                             │
  │         │                     │ (Reward-Signal-Architecture §4)      │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ "opioid confirm" → CHỈ dùng khi nói CỤ THỂ về Type A pathway
  ⚠️ "reward" nói chung → luôn bao gồm CẢ Type A VÀ Type B
  ⚠️ Nhớ: reward = body-base confirm (Step 5) ≠ prediction-delta (Step 2)
```

---

## §3 — NEGATIVE: DISSONANCE LABELS

```
⭐ DISSONANCE = BODY SIGNAL "KHÔNG KHỚP" (mismatch / predicted harm / recalibration)

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Nghĩa + khi nào dùng                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-feedback âm    │ Chung nhất. Body phản hồi tiêu cực. │
  │ (chung) │                     │ Dùng: khi chỉ biết body response -  │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ dissonance          │ Body detect mismatch (schema ≠       │
  │ (type)  │                     │ reality). Drive giải quyết.          │
  │         │                     │ Dùng: khi biết rõ có mismatch.       │
  │         │                     │                                      │
  │         │ threat              │ Body predict tổn hại (predicted      │
  │         │                     │ harm). Drive né tránh.               │
  │         │                     │ Dùng: khi biết rõ anticipation harm. │
  │         │                     │ (Threat.md: 5 mức × 3 trục × 3 gốc) │
  │         │                     │                                      │
  │         │ recalibration       │ Neurons adjusting pattern.           │
  │         │ dissonance          │ Transient, tự giải khi adapt xong.   │
  │         │                     │ Dùng: khi discomfort từ learning/    │
  │         │                     │ adjusting (không phải mismatch/      │
  │         │                     │ threat).                             │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ chunk-miss          │ Expected X, got <X. SNC mechanism.   │
  │ (cụ thể)│                     │ (Crespi 1942, Flaherty 1996)         │
  │         │                     │                                      │
  │         │ chunk-shift         │ Cùng chunks, KHÁC valence.           │
  │         │                     │ Context thay đổi → re-evaluate.      │
  │         │                     │                                      │
  │         │ chunk-gap           │ C should exist but missing.          │
  │         │                     │ Network predict C → C absent.        │
  │         │                     │ (Gap-Direction.md: gap has direction) │
  │         │                     │                                      │
  │         │ SNC                 │ Successive Negative Contrast.        │
  │         │                     │ Specific chunk-miss: downshift       │
  │         │                     │ from high baseline → overreact.      │
  │         │                     │                                      │
  │         │ nociception         │ Tissue damage signal. Hardware.      │
  │         │                     │ A-delta + C fibers.                  │
  │         │                     │                                      │
  │         │ cortisol Role ①-⑤   │ Context-specific amplifier role:     │
  │         │                     │ ① Compile Direction                  │
  │         │                     │ ② Holding ("chưa xong")              │
  │         │                     │ ③ Threat-sustained (chronic)         │
  │         │                     │ ④ Inertia (nghiện productive)        │
  │         │                     │ ⑤ Silent (cao mà không cảm nhận)     │
  │         │                     │ (Cortisol-Baseline.md §7.7)          │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Cortisol = AMPLIFIER, không phải SOURCE dissonance
     (Body-Feedback.md §5: cortisol injection → no pain)
  ⚠️ "Khó chịu" = feeling label (PFC observe) ≠ dissonance (mechanism)
```

---

## §4 — DETECTION: PREDICTION-DELTA LAYER (RIÊNG BIỆT)

```
⭐ PREDICTION-DELTA = DETECTION LAYER — RIÊNG BIỆT KHỎI REWARD/DISSONANCE:

  Brain detect "CÓ BIẾN ĐỘNG so với prediction" → CHƯA biết tốt hay xấu.
  Reward/dissonance = bước SAU (Step 5: body-base check).
  2 layers KHÁC NHAU, KHÔNG gộp được.

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Nghĩa + khi nào dùng                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ prediction-delta    │ Brain detect biến động so với        │
  │         │                     │ prediction hiện tại. Dopamine alert. │
  │         │                     │ CHƯA biết tốt/xấu — chỉ "khác      │
  │         │                     │ baseline".                           │
  │         │                     │ = Step 2 trong 7-step mechanism.     │
  │         │                     │ Dùng: khi nói về detection signal.   │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ DRD4 filter         │ Receptor threshold cho prediction-   │
  │ (cụ thể)│                     │ delta:                               │
  │         │                     │ 4R=sensitive (small delta detected)  │
  │         │                     │ 7R=coarse (only large delta)         │
  │         │                     │ (PFC-Hardware.md: per-person)        │
  │         │                     │                                      │
  │         │ PFC spotlight       │ Step 4: PFC boost target region.     │
  │         │                     │ NE + ACh amplification.              │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⭐ CRITICAL DISTINCTION:

    Prediction-delta = "chuông cửa" (CÓ BIẾN ĐỘNG — chú ý!)
    Body-base reward = "quà đằng sau cửa" (chunk KHỚP body-need)

    Chuông cửa → KHÔNG phải quà. Quà → KHÔNG cần chuông cửa luôn.
    (Type B reward có thể bypass prediction-delta — RSA §1.3 P3)

    → ĐỪNG gộp prediction-delta với body-base reward
    → ĐỪNG gọi prediction-delta là "reward signal"
    → Detection (Step 2) ≠ Evaluation (Step 5)
```

---

## §5 — NEUTRAL: BODY-FEEDBACK BASELINE

```
⭐ BODY-FEEDBACK BASELINE = TRẠNG THÁI "ĐÃ QUEN":

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa                                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │ body-feedback baseline  │ Pattern lặp lại → brain habituated →     │
  │                         │ no prediction-delta → no alert.           │
  │                         │ = "Trạng thái bình thường mới."           │
  │                         │                                           │
  │ habituated              │ Cùng nghĩa, viết tắt. Dùng khi context  │
  │                         │ đã rõ là body-feedback.                  │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⭐ HABITUATED ≠ VALUE = 0:

    Oxy: habituated (hít thở hàng ngày) → VALUE = sống/chết
    Lương tháng: habituated (tháng nào cũng có) → VALUE = survival
    Nhân viên trung thành: habituated (luôn ở) → VALUE = team foundation

    → Habituated = no prediction-delta = brain KHÔNG alert
    → KHÔNG CÓ NGHĨA "không quan trọng"
    → CHỈ CÓ NGHĨA "brain không fire detection signal vì đã quen"
    → MẤT thứ đã habituated → prediction-delta ÂM (SNC) → dissonance
    → "Hóa ra quan trọng!" = habituated value bị INVISIBLE

    (Reward-Calibration.md §8.3)
```

---

## §6 — COMPILED: VALENCE TAGS

```
⭐ APPROACH / AVOIDANCE = COMPILED RESULT (đã tích lũy lên chunk):

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ Label               │ Nghĩa                                        │
  ├─────────────────────┼──────────────────────────────────────────────┤
  │ approach tag        │ Valence DƯƠNG compiled lên chunk.             │
  │                     │ "Domain này → body-base reward" (đã verify).  │
  │                     │ Drive HƯỚNG TỚI domain/agent.                │
  │                     │                                               │
  │ avoidance tag       │ Valence ÂM compiled lên chunk.                │
  │                     │ "Domain này → dissonance" (đã verify).        │
  │                     │ Drive NÉ TRÁNH domain/agent.                  │
  └─────────────────────┴──────────────────────────────────────────────┘

  PHÂN BIỆT COMPILED vs MOMENTARY:

    Reward / dissonance = MOMENTARY (đang xảy ra ngay bây giờ)
    Approach / avoidance = COMPILED (đã tích lũy qua nhiều experience)

    → "Tôi thích toán" = approach tag (compiled qua nhiều lần reward)
    → "Tôi đang vui vì giải được bài" = body-base reward (momentary)
    → 2 thứ KHÁC NHAU, dù liên quan

    → Approach tags = INPUT cho tiếp tục hay dừng
    → Reward/dissonance = INPUT cho compile approach/avoidance tags

  (Valence-Propagation.md v1.4: per-entity valence + chain propagation)
```

---

## §7 — OBSERVATION VS MECHANISM (KHÁC TẦNG)

```
⭐ BODY-FEEDBACK ≠ FEELING — 2 TẦNG KHÁC NHAU:

  ┌──────────────────┬───────────────────────────────────────────────┐
  │ Tầng             │ Mô tả                                         │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ BODY-FEEDBACK    │ MECHANISM: signal từ body → chạy 24/7         │
  │ (mechanism)      │ 95% VÔ THỨC (PFC không quan sát được)         │
  │                  │ Labels: reward / dissonance / prediction-delta │
  │                  │ / chunk-miss / chunk-shift / chunk-gap / ...   │
  │                  │ = FILE NÀY mô tả vocabulary của tầng này      │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ FEELING          │ OBSERVATION: PFC quan sát body-feedback        │
  │ (observation)    │ 7-layer gradient (implicit → explicit)         │
  │                  │ Labels: "sướng" / "khó chịu" / "lờ mờ" / ... │
  │                  │ = Feeling.md v2.0 mô tả vocabulary của tầng   │
  │                  │ này                                            │
  └──────────────────┴───────────────────────────────────────────────┘

  ⚠️ NHẦM LẪN HAY GẶP:

    "Sướng" ≠ reward:
      → "Sướng" = PFC observation body-base reward
        (Layer 5-6: đã observe + label)
      → Reward có thể CHẠY mà PFC không observe
        (Layer 1-2: body signal nhưng PFC chưa thấy)
      → = Body-base reward XẢY RA mà không "cảm thấy sướng" (possible)

    "Khó chịu" ≠ dissonance:
      → "Khó chịu" = PFC observation dissonance signal
      → Dissonance chạy 24/7, PFC chỉ observe 1 phần nhỏ
      → = "Background Pattern" dissonance = invisible (BP.md)

  (Feeling.md v2.0: feeling = PFC observation body-feedback)
  (01-Foundation.md §5: 7-layer clarity gradient)
```

---

## §8 — QUY TẮC SỬ DỤNG

### §8.1 — Nguyên tắc chính

```
⭐ CỤ THỂ NHẤT CÓ THỂ. CHUNG NHẤT NẾU BẮT BUỘC.

  ① Tier 3 > Tier 2 > Tier 1:
     Nếu biết chain → Tier 3 ("chunk-miss → SNC → cortisol Role ②")
     Nếu biết direction → Tier 2 ("body-base reward" / "dissonance")
     Nếu chỉ biết +/- → Tier 1 ("body-feedback dương/âm")

  ② KHÔNG gộp prediction-delta với body-base reward:
     "prediction-delta" = detection (Step 2)
     "body-base reward" = evaluation (Step 5)
     = 2 events KHÁC NHAU, CÓ THỂ xảy ra ĐỘC LẬP

  ③ "reward" = body-base reward (CẢ Type A VÀ Type B):
     KHÔNG giới hạn vào opioid / Type A
     Type B (touch, exercise, warmth) = reward THẬT, ĐÚNG label

  ④ PHÂN BIỆT compiled (tags) vs momentary (signals):
     Approach/avoidance = đã tích lũy trên chunk
     Reward/dissonance = đang xảy ra ngay bây giờ

  ⑤ PHÂN BIỆT mechanism (body-feedback) vs observation (feeling):
     Body-feedback labels: reward, dissonance, prediction-delta,...
     Feeling labels: "sướng", "khó chịu", "lờ mờ",...
     KHÔNG dùng feeling labels thay body-feedback labels
```

### §8.2 — Ví dụ áp dụng

```
  VÍ DỤ: Lương tăng từ 10tr → 15tr

  TIER 2 (đủ cho Research files):
    "10tr → body-base reward (gap survival fill) → habituated
     → 15tr → prediction-delta nhỏ hơn → reward giảm (gap đã shrink)"

  TIER 3 (cho deep analysis):
    "10tr (lần đầu):
       prediction-delta (mới) → DRD4 pass → PFC spotlight
       → body-base check: chunk [lương 10tr] khớp gap [survival]
       → body-base reward (Type A: evaluative)
       → chunk compile: [lương 10tr = approach tag]
     10tr (tháng 12):
       habituated: cùng pattern → no prediction-delta → no alert
       → gap survival ĐÃ fill → body-feedback baseline
     15tr:
       prediction-delta (khác baseline 10tr) → body-base check
       → gap survival nhỏ hơn (đã fill phần lớn) → reward giảm
       → = Diminishing returns = gap shrink"
```

---

## §9 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback.md v1.1            │ ENTRY POINT. §4 4 trục. §6 H10.     │
  │                                  │ Đọc TRƯỚC file này.                 │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Mechanism.md v1.2  │ §2 2 sources, §3 3 dynamics.        │
  │                                  │ Tier 3 labels (chunk-miss/shift/gap) │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Reward-Signal-Architecture.md    │ §1 Type A/B. §2 A₀→A₃. §4 5       │
  │ v1.0                             │ Profiles. Tier 2-3 reward labels.    │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ 03-Reward.md v1.1                │ §2 7-step mechanism.                 │
  │                                  │ §3 H10 preconditions. Step 5 detail. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.0       │ §7.7 5 Roles. Amplifier, not cause. │
  │                                  │ Tier 3 dissonance labels.            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Valence-Propagation.md v1.4      │ Approach/avoidance tags.             │
  │                                  │ Compiled vs momentary distinction.   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Feeling.md v2.0                  │ PFC observation of body-feedback.    │
  │                                  │ §7 distinction mechanism vs observe. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gap-Direction.md v1.0            │ "Chưa biết = không gap."             │
  │                                  │ Tier 3 label: chunk-gap + direction. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Threat.md                        │ 5 mức × 3 trục × 3 nguồn.           │
  │                                  │ Tier 2 dissonance label: threat.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Clarification/ folder            │ Bridge mainstream → framework.       │
  │                                  │ NƠI DUY NHẤT thảo luận terminology  │
  │                                  │ ngoài framework + tại sao framework │
  │                                  │ dùng label khác.                     │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

> *Body-Feedback Label Convention v1.1 — Vocabulary Reference.*
> *100% framework vocabulary.*
> *3-tier system: cụ thể nhất có thể, chung nhất nếu bắt buộc.*
> *Reward = body-base confirm signal (CẢ Type A VÀ Type B).*
> *Prediction-delta = detection (Step 2) ≠ body-base reward (Step 5).*
> *Body-feedback (mechanism) ≠ Feeling (PFC observation).*
> *"Chuông cửa" ≠ "quà đằng sau cửa."*
