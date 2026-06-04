---
title: Body-Feedback Label Convention — Vocabulary Reference
version: 2.1
created: 2026-05-12
rewritten: 2026-05-17 (v2.0 — FULL REWRITE: +Foundation terms, +Compiled/Fresh processing, +Entity-Compiled 3 subtypes, +Inter-Body interaction labels, +5-Channel, +3-cost, +2-Stream)
updated: 2026-05-25 (v2.1 — §4 +Evaluative/Direct-State Dissonance labels at Tier 2+3, parallel §3 Reward structure, Dissonance-Signal-Architecture v1.0 integration)
previous: v1.1 → backup/Body-Feedback-Label-v1.1-backup.md
status: REFERENCE v2.1
scope: |
  VOCABULARY REFERENCE: Quy ước label cho toàn bộ body-feedback system.
  Formalize 3-tier label system: General → Direction → Specific.
  File này = MUST-READ ngay sau Body-Feedback.md.
  Mọi file trong framework nên dùng vocabulary theo quy ước này.
  100% FRAMEWORK VOCABULARY — không dùng terminology ngoài framework.
  v2.0 MỞ RỘNG: 7 concept families (từ Inter-Body drill):
    ① Foundation terms (body-need, gap, gap direction, drive)
    ② Entity-Compiled 3 subtypes (positive/negative/mixed)
    ③ Compiled/Fresh processing labels (trục thật)
    ④ By-product match / Anti-match
    ⑤ 2-Stream Architecture (Hardware-Stream / Modeling-Stream)
    ⑥ 3 Independent Cost Sources
    ⑦ 5-Channel Input Vector
purpose: |
  Framework phân tích body-feedback qua 4 trục, 7-step mechanism,
  Evaluative/Direct-State, E₀→E₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles.
  v2.0: THÊM Foundation terms, Compiled/Fresh processing, Inter-Body interaction,
  Entity-Compiled multi-channel, 5-Channel Input, 3-cost.
  File này formalize vocabulary thống nhất cho TOÀN BỘ framework —
  bao gồm cả intra-body VÀ inter-body labels.
  Giải quyết:
    → "opioid confirm" chỉ cover Evaluative, bỏ sót Direct-State
    → "pleasant/discomfort" nhầm body-feedback (mechanism) với feeling (observation)
    → "Logic/Feeling" nhầm observer labels với mechanism labels
    → Thiếu vocabulary cho inter-body interaction
    → Foundation terms (body-need, gap) dùng khắp nơi nhưng chưa define
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — ngang hàng Body-Feedback-Mechanism.md.
  ĐỌC NGAY SAU Body-Feedback.md (entry point).
dependencies:
  - Body-Feedback.md v2.0 — §2 dual-pull, §4 4 trục, §5 3 nguồn, §6 Body-Feedback-Precondition
  - Body-Feedback-Mechanism.md v2.0 — §1 Body-Need aggregate, §2 2 sources, §3 3 dynamics
  - Reward-Signal-Architecture.md v2.0 — §1 Evaluative/Direct-State, §2 E₀→E₃, §4 5 Profiles
  - Dissonance-Signal-Architecture.md v1.0 — §1 Evaluative/Direct-State Dissonance, §2 E₀→E₃ dissonance, §3 Evaluative Gates
  - 03-Reward.md v1.1 — §2 7-step mechanism, §3 Body-Feedback-Precondition, Step 5 body-base check
  - Cortisol-Baseline.md v2.0 — §7.7 5 Roles
  - Valence-Propagation.md v2.0 — §3 Entity-Compiled, approach/avoidance tags
  - Inter-Body-Mechanism.md v1.0 — §3 Compiled/Fresh, §4 3-cost, §5 by-product match, §6 5-Channel, §7 PFC=Lawyer, §8 Entity-Compiled
  - By-Product-Gap-Resonance.md v1.0 — §2 2-Stream Architecture
  - Feeling.md v2.2 — PFC observation of body-feedback (khác tầng)
  - Gap-Direction.md v2.0 — gap has direction = f(surrounding chunks)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Feedback Label Convention — Vocabulary Reference

> **Framework phân tích body-feedback qua 4 trục, 7-step mechanism,**
> **Evaluative/Direct-State, E₀→E₃, 5 Profiles, 3 chunk dynamics, 5 cortisol Roles...**
>
> **THÊM: Foundation terms, Compiled/Fresh processing, Entity-Compiled 3 subtypes,**
> **By-product match, 2-Stream, 3-cost, 5-Channel Input Vector.**
>
> **Nhưng khi VIẾT/NÓI, labels CHƯA BAO GIỜ được formalize.**
>
> **File này: QUY ƯỚC LABEL cho toàn framework.**
> **100% framework vocabulary. Đọc ngay sau Body-Feedback.md.**

---

## Mục lục

- §0 — TẠI SAO CẦN FILE NÀY
- §1 — 3-TIER LABEL SYSTEM
- §2 — FOUNDATION: BODY-NEED + GAP + DRIVE (★ NEW v2.0)
- §3 — POSITIVE: BODY-BASE REWARD LABELS
- §4 — NEGATIVE: DISSONANCE LABELS
- §5 — DETECTION: PREDICTION-DELTA LAYER (RIÊNG BIỆT)
- §6 — NEUTRAL: BODY-FEEDBACK BASELINE
- §7 — COMPILED: VALENCE TAGS + ENTITY-COMPILED
- §8 — COMPILED/FRESH: PROCESSING LABELS (★ NEW v2.0)
- §9 — INTER-BODY: INTERACTION LABELS (★ NEW v2.0)
- §10 — OBSERVATION VS MECHANISM (KHÁC TẦNG)
- §11 — QUY TẮC SỬ DỤNG
- §12 — CROSS-REFERENCES

---

## §0 — TẠI SAO CẦN FILE NÀY

```
⭐ FRAMEWORK CÓ MECHANISMS CHÍNH XÁC — THIẾU CONVENTION DÙNG LABEL:

  Body-feedback system có:
    → 4 trục phân loại orthogonal (Body-Feedback-Mechanism.md §0)
    → 7-step mechanism từ detection → reward (03-Reward.md §2)
    → Evaluative/Direct-State Reward distinction (Reward-Signal-Architecture.md §1)
    → E₀→E₃ complexity gradient + 5 Profiles
    → 3 chunk dynamics (Chunk-Shift/Miss/Gap)
    → 5 cortisol Roles (Cortisol-Baseline.md §7.7)

  v2.0 THÊM (từ Inter-Body drill):
    → Foundation terms: body-need, gap, gap direction, drive (Inter-Body §2)
    → Compiled/Fresh = trục processing thật (Inter-Body §3)
    → Entity-Compiled 3 subtypes (Inter-Body §8, Valence-Propagation v2.0 §3)
    → By-product match + Anti-match (Inter-Body §5.4)
    → 2-Stream Architecture (By-Product-Gap-Resonance v1.0 §2)
    → 3 Independent Cost Sources (Inter-Body §4)
    → 5-Channel Input Vector (Inter-Body §6)

  NHƯNG: chưa có quy ước DÙNG LABEL NÀO khi viết/nói.
  → Cùng 1 hiện tượng → dùng 5 từ khác nhau → mơ hồ


  4 VẤN ĐỀ CỤ THỂ:

  ① "OPIOID CONFIRM" CHỈ COVER EVALUATIVE REWARD:
    Evaluative Reward: μ-opioid → hedonic hotspot → ĐÚNG "opioid confirm"
    Direct-State Reward: CT afferents / endocannabinoid / thermoreceptor → KHÔNG opioid
    → Correct general label = "body-base reward" (cover CẢ Evaluative VÀ Direct-State)
    (Reward-Signal-Architecture.md §1.1)

  ② NHẦM LẪN BODY-FEEDBACK VỚI FEELING:
    Body-feedback = MECHANISM (signal từ body, chạy 24/7, 95% vô thức)
    Feeling = OBSERVATION (PFC quan sát body-feedback → 7-layer gradient)
    "Pleasant" = feeling label (PFC đã observe + label) — KHÔNG phải body-feedback label
    → §10 file này phân biệt rõ
    (Feeling.md v2.2)

  ③ "LOGIC / FEELING" NHẦM OBSERVER LABELS VỚI MECHANISM LABELS (v2.0 NEW):
    TRỤC THẬT bên trong = Compiled ←→ Fresh (compilation level)
    "Logic/Feeling" = observer perspective labels, KHÔNG phải mechanism
    → §8 file này formalize processing labels
    (Inter-Body-Mechanism.md §3)

  ④ FOUNDATION TERMS DÙNG KHẮP NƠI NHƯNG CHƯA DEFINE (v2.0 NEW):
    "body-need", "gap", "gap direction" = xuất hiện HÀNG TRĂM lần
    Nhưng chưa bao giờ được formalize ở 1 nơi duy nhất
    → §2 file này define foundation
    (Body-Feedback-Mechanism v2.0 §1, Inter-Body §2, Gap-Direction.md)


  ⭐ FILE NÀY GIẢI QUYẾT:
    → Formalize vocabulary thống nhất cho toàn framework
    → 3-tier system: cụ thể nhất có thể, chung nhất nếu bắt buộc
    → Foundation terms defined TRƯỚC → mọi section sau reference tới §2
    → Bao gồm CẢ intra-body VÀ inter-body vocabulary
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
      → Tier 3 chủ đạo. Chain trace rõ ràng.

    Người muốn hiểu / Research files:
      → Tier 2 chủ đạo: "body-base reward", "dissonance", "chunk-miss"
      → Đủ chính xác, đủ hiểu mechanism cơ bản

    General / overview:
      → Tier 1 khi cần: "body-feedback dương/âm"
      → Có thể drill sâu hơn nếu người đọc yêu cầu


  ÁP DỤNG CHO MỌI CATEGORY (§2-§9):
    Mỗi category đều có Tier 1/2/3 tương ứng.
    3-Tier logic = UNIVERSAL, áp dụng cho cả foundation, signal,
    processing, và inter-body labels.
```

---

## §2 — FOUNDATION: BODY-NEED + GAP + DRIVE (★ NEW v2.0)

```
⭐ THUẬT NGỮ NỀN TẢNG — MỌI SECTION SAU REFERENCE TỚI ĐÂY:

  ┌─────────────────────────────────────────────────────────────────┐
  │ CONCEPTUAL FLOW:                                                 │
  │                                                                  │
  │   body-base (system)                                             │
  │       ↓ tạo ra                                                   │
  │   body-need (aggregate trạng thái CẦN)                           │
  │       ↓ bao gồm                                                 │
  │   gap + gap direction (specific chunks missing + hướng)          │
  │       ↓ sinh ra                                                  │
  │   drive (đẩy hành vi fill gap)                                   │
  │       ↓ được monitor bởi                                        │
  │   body-feedback (signal từ body về current state — FILE NÀY)    │
  │                                                                  │
  └─────────────────────────────────────────────────────────────────┘


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A) BODY-BASE (hệ thống):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ body-base               │ TOÀN BỘ hệ thống: hardware + compiled   │
  │                         │ + social. = "Cơ thể-nền" bao gồm mọi   │
  │                         │ thứ body đã tích lũy + đang vận hành.   │
  │                         │ Compilable Architecture: general-purpose reward + │
  │                         │ compilation + social hardware.           │
  │                         │ Dùng: khi nói về HỆ THỐNG tổng thể.    │
  │                         │ (Body-Base.md v3.1, Inter-Body §1)      │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  B) BODY-NEED (aggregate trạng thái CẦN):

  ┌─────────┬─────────────────────┬──────────────────────────────────────┐
  │ Tier    │ Label               │ Nghĩa + khi nào dùng                │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 1  │ body-need           │ TỔNG HỢP trạng thái CẦN hiện tại.   │
  │ (chung) │                     │ Aggregate TẤT CẢ signals đang đòi   │
  │         │                     │ body đáp ứng.                        │
  │         │                     │ KHÔNG phải 1 signal đơn → là TỔNG.   │
  │         │                     │ Exist TRƯỚC PFC awareness.           │
  │         │                     │ Dùng: khi nói chung "body cần gì."  │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 2  │ hardware body-need  │ Nguồn ①: Sensory-Driven.            │
  │ (source)│                     │ Homeostatic + nociceptive + hormonal.│
  │         │                     │ KHÔNG cần compiled chunks.           │
  │         │                     │ VD: đói, khát, đau, lạnh.           │
  │         │                     │ Dùng: khi body-need từ hardware.     │
  │         │                     │                                      │
  │         │ pattern body-need   │ Nguồn ②: Chunk Dynamics/Pattern.    │
  │         │                     │ Gap / Miss / Shift (+ Compound).     │
  │         │                     │ REQUIRES compiled chunks.            │
  │         │                     │ VD: nhớ bạn, career gap, identity.  │
  │         │                     │ Dùng: khi body-need từ chunk fire.   │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ (specific gaps)     │ Specific gap + direction cụ thể.    │
  │ (cụ thể)│                     │ VD: "gap survival [direction: food]" │
  │         │                     │ VD: "gap mastery [direction: toán]"  │
  │         │                     │ VD: "gap connection [direction: bạn  │
  │         │                     │      thân A]"                        │
  │         │                     │ Dùng: khi trace được gap CỤ THỂ.    │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ Body-need LUÔN TỒN TẠI (không bao giờ = 0)
  ⚠️ Body-need = MULTIPLE cùng lúc (parallel)
  ⚠️ Body-need CÓ PRIORITY (intensity × urgency × state)
  ⚠️ PFC KHÔNG LUÔN BIẾT body-need (exist trước awareness)
  ⚠️ 2 nguồn KHÔNG loại trừ — 1 event kích hoạt CẢ ①+②
  (Inter-Body §2, Body-Feedback-Mechanism v2.0 §1)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  C) GAP + GAP DIRECTION (specific missing + hướng):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ gap                     │ Chunk SHOULD exist but MISSING.          │
  │                         │ Network predict chunk C → C absent.      │
  │                         │ = Component CỤ THỂ trong body-need.      │
  │                         │ Dùng: khi nói "thiếu gì đó cụ thể."    │
  │                         │                                          │
  │ gap direction           │ HƯỚNG gap points = f(surrounding chunks).│
  │                         │ Chỉ fill ĐÚNG HƯỚNG mới → reward.       │
  │                         │ Mỗi người có direction RIÊNG.            │
  │                         │ "Chưa biết = không có gap" (chưa có     │
  │                         │ surrounding chunks → chưa có direction). │
  │                         │ Dùng: khi nói HOW gap cần được fill.    │
  │                         │ (Gap-Direction.md v2.0)                  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ gap ≠ body-need:
     Gap = 1 specific chunk missing (component)
     Body-need = AGGREGATE tất cả gaps + hardware signals (tổng)
     1 body-need có thể chứa NHIỀU gaps song song
  ⚠️ "Chưa biết = không có gap" — gap CHỈ tồn tại khi surrounding chunks
     ĐÃ compile. Trẻ không có gap "vật lý lượng tử" vì chưa có substrate.
  ⚠️ Gap direction = TẠI SAO by-product match works:
     B's output match A's gap DIRECTION → A reward.
     Direction mismatch → no reward DÙ CÓ output.


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  D) DRIVE (đẩy hành vi):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ drive                   │ Lực đẩy HÀNH VI từ body-need.            │
  │                         │ = Output behavioral từ body-need →       │
  │                         │ → hành động fill gap.                    │
  │                         │ Dùng: khi nói "cái gì ĐẨY hành vi."    │
  │                         │                                          │
  │ drive direction         │ = gap direction expressed as behavior.   │
  │                         │ Drive HƯỚNG TỚI (approach) hoặc         │
  │                         │ NÉ KHỎI (avoidance).                    │
  │                         │ Dùng: khi nói HƯỚNG hành vi.            │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ drive ≠ body-need:
     Body-need = STATE (trạng thái CẦN — internal)
     Drive = OUTPUT (lực đẩy hành vi — toward action)
     Body-need → drive (nhưng PFC có thể suppress drive → cost ②)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  E) BODY-FEEDBACK (signal domain — umbrella term FILE NÀY):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ body-feedback           │ TẤT CẢ signal từ body về current state. │
  │                         │ UMBRELLA TERM cho mọi thứ file này mô   │
  │                         │ tả. Chạy 24/7. 95% vô thức.            │
  │                         │ Bao gồm: reward, dissonance, prediction-│
  │                         │ delta, baseline, valence tags...         │
  │                         │ ≠ Feeling (feeling = PFC OBSERVE body-  │
  │                         │ feedback — khác tầng, xem §10).         │
  │                         │ Dùng: khi nói chung "body gửi signal."  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ body-feedback MONITOR body-need:
     Body-need = CẦN gì. Body-feedback = body BÁO CÁO gì.
     Reward = "gap đang được fill" (positive feedback)
     Dissonance = "gap CHƯA fill / bị block" (negative feedback)
     → Body-feedback = COMMUNICATION CHANNEL, body-need = CONTENT
```

---

## §3 — POSITIVE: BODY-BASE REWARD LABELS

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
  │ TIER 2  │ body-base reward    │ Body xác nhận chunk khớp body-need   │
  │ (type)  │                     │ (§2). Cả Evaluative + Direct-State.  │
  │         │                     │ Dùng: khi biết rõ body confirm.      │
  │         │                     │                                      │
  │         │ reward              │ Viết tắt của body-base reward.       │
  │         │                     │ Dùng: khi context ĐÃ RÕ là          │
  │         │                     │ body-feedback (không nhầm sang khác).│
  │         │                     │                                      │
  │         │ Evaluative Reward    │ Evaluative confirm. Opioid-based.    │
  │         │                     │ Cần Body-Feedback-Precondition full. Chunk library rich.    │
  │         │                     │ Dùng: khi biết rõ là evaluative.     │
  │         │                     │                                      │
  │         │ Direct-State Reward  │ Direct state confirm. Non-opioid.    │
  │         │                     │ Hardware-based. Ít habituate.        │
  │         │                     │ Dùng: khi biết rõ là body-state.     │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ μ-opioid confirm    │ Evaluative. Hedonic hotspot pathway. │
  │ (cụ thể)│                     │ Dùng: khi trace chain tới NAcc/VP.   │
  │         │                     │                                      │
  │         │ CT afferent reward  │ Direct-State. Touch comfort pathway.  │
  │         │                     │ ~1-10cm/s optimal (Löken 2009).      │
  │         │                     │                                      │
  │         │ endocannabinoid     │ Direct-State. Exercise/runner's high.│
  │         │ reward              │ CB1 pathway (Fuss 2015).             │
  │         │                     │                                      │
  │         │ E₀ / E₁ / E₂ / E₃  │ Evaluative complexity gradient.      │
  │         │                     │ E₀=hardware, E₃=expert evaluation.   │
  │         │                     │ (Reward-Signal-Architecture §2)      │
  │         │                     │                                      │
  │         │ Profile ①-⑤         │ 5 "hương vị" reward.                 │
  │         │                     │ Sensory/Coherence/Social/Relief/     │
  │         │                     │ Preview.                             │
  │         │                     │ (Reward-Signal-Architecture §4)      │
  │         │                     │                                      │
  └─────────┴─────────────────────┴──────────────────────────────────────┘

  ⚠️ "opioid confirm" → CHỈ dùng khi nói CỤ THỂ về Evaluative pathway
  ⚠️ "reward" nói chung → luôn bao gồm CẢ Evaluative VÀ Direct-State
  ⚠️ Nhớ: reward = body confirm "gap đang fill đúng direction" (§2C)
     ≠ prediction-delta (detection signal — §5)
```

---

## §4 — NEGATIVE: DISSONANCE LABELS

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
  │         │ Evaluative          │ Compiled, conditional. dACC +        │
  │         │ Dissonance          │ anterior insula. PFC can modulate.   │
  │         │                     │ Develops with age + chunk library.   │
  │         │                     │ Dùng: khi biết rõ là evaluative      │
  │         │                     │ (social pain, moral injury, anxiety).│
  │         │                     │ (Dissonance-Signal-Architecture §1)  │
  │         │                     │                                      │
  │         │ Direct-State        │ Hardware, from birth. Nociceptors,   │
  │         │ Dissonance          │ thermoreceptors, visceral signals.   │
  │         │                     │ PFC minimal. Numbness-proof.         │
  │         │                     │ Dùng: khi biết rõ là body-state      │
  │         │                     │ (pain, hunger, temperature, itch).   │
  │         │                     │ (Dissonance-Signal-Architecture §1)  │
  │         │                     │                                      │
  ├─────────┼─────────────────────┼──────────────────────────────────────┤
  │         │                     │                                      │
  │ TIER 3  │ chunk-miss          │ Expected X, got <X. SNC mechanism.   │
  │ (cụ thể)│                     │ (Crespi 1942, Flaherty 1996)         │
  │         │                     │                                      │
  │         │ chunk-shift         │ Cùng chunks, KHÁC valence.           │
  │         │                     │ Context thay đổi → re-evaluate.      │
  │         │                     │                                      │
  │         │ chunk-gap           │ = gap (§2C) being DETECTED as        │
  │         │                     │ dissonance signal. C should exist     │
  │         │                     │ but missing → body fire signal.      │
  │         │                     │ (Gap-Direction.md: gap has direction) │
  │         │                     │                                      │
  │         │ SNC                 │ Successive Negative Contrast.        │
  │         │                     │ Specific chunk-miss: downshift       │
  │         │                     │ from high baseline → overreact.      │
  │         │                     │                                      │
  │         │ nociception         │ Tissue damage signal. Hardware.      │
  │         │                     │ A-delta + C fibers.                  │
  │         │                     │                                      │
  │         │ substance P /       │ Direct-State. Nociception pathway.   │
  │         │ CGRP / glutamate    │ Pain transmission A-delta + C fibers.│
  │         │                     │ (Dissonance-Signal-Architecture §1.6)│
  │         │                     │                                      │
  │         │ dACC activation     │ Evaluative. Social pain pathway.     │
  │         │                     │ 🟢 Eisenberger 2003 (Cyberball).     │
  │         │                     │ (Dissonance-Signal-Architecture §1.6)│
  │         │                     │                                      │
  │         │ CRH → amygdala      │ Evaluative. Anxiety/threat pathway.  │
  │         │                     │ HPA axis → cortisol cascade.         │
  │         │                     │ (Dissonance-Signal-Architecture §1.6)│
  │         │                     │                                      │
  │         │ E₀→E₃ dissonance   │ Evaluative complexity gradient       │
  │         │                     │ applied to dissonance direction.     │
  │         │                     │ E₀=bitter aversion (hardware).       │
  │         │                     │ E₃=moral injury (expert evaluation). │
  │         │                     │ (Dissonance-Signal-Architecture §2)  │
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

  ⚠️ Evaluative/Direct-State = ORTHOGONAL to source (dissonance/threat/recalibration)
     1 event có thể là BOTH "mismatch" (source) AND "Evaluative" (type)
     VD: bị phản bội = mismatch (source) + Evaluative Dissonance (type)
     VD: kim đâm = nociception (source) + Direct-State Dissonance (type)
     (Dissonance-Signal-Architecture.md §1 — parallel Reward-Signal-Architecture §1)
  ⚠️ Cortisol = AMPLIFIER, không phải SOURCE dissonance
     (Body-Feedback.md §5: cortisol injection → no pain)
  ⚠️ "Discomfort" = feeling label (PFC observe) ≠ dissonance (mechanism)
  ⚠️ chunk-gap (signal) vs gap (state):
     Gap (§2C) = STATE: chunk missing (có thể PFC không biết)
     Chunk-gap (§4 đây) = SIGNAL: body FIRE dissonance vì detect gap
     = Gap tồn tại → body detect → fire chunk-gap signal
```

---

## §5 — DETECTION: PREDICTION-DELTA LAYER (RIÊNG BIỆT)

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
    (Direct-State Reward có thể bypass prediction-delta — Reward-Signal-Architecture §1.3 Precondition-3)

    → ĐỪNG gộp prediction-delta với body-base reward
    → ĐỪNG gọi prediction-delta là "reward signal"
    → Detection (Step 2) ≠ Evaluation (Step 5)
```

---

## §6 — NEUTRAL: BODY-FEEDBACK BASELINE

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

  ⚠️ Connection to §2: body-need CÓ THỂ habituated:
     Gap "survival" fill mỗi ngày (lương) → habituated → brain ignore
     NHƯNG gap VẪN CÓ (mất lương → SNC → "hóa ra quan trọng!")
     = Body-need exists ≠ body-feedback fires
```

---

## §7 — COMPILED: VALENCE TAGS + ENTITY-COMPILED

```
⭐ 2 TẦNG COMPILED VALENCE:

  TẦNG 1 — APPROACH / AVOIDANCE TAGS (đã tích lũy lên chunk):

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

    Reward / dissonance = MOMENTARY (đang xảy ra — §3/§4)
    Approach / avoidance = COMPILED (đã tích lũy qua nhiều experience)

    → "Tôi thích toán" = approach tag (compiled qua nhiều lần reward)
    → "Tôi đang vui vì giải được bài" = body-base reward (momentary)
    → 2 thứ KHÁC NHAU, dù liên quan

    → Approach tags = INPUT cho drive direction (§2D)
    → Reward/dissonance = INPUT cho compile approach/avoidance tags

  (Valence-Propagation.md v2.0: per-entity valence + chain propagation)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TẦNG 2 — ENTITY-COMPILED (body-base extension):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Entity-Compiled         │ Entity đã compile vào body-base ở        │
  │ (general)               │ STRUCTURAL level. Entity's state =       │
  │                         │ MY state. Per-channel valence profile.    │
  │                         │ Dùng: general term cho structural bond.  │
  │                         │ (Inter-Body §8, Valence-Propagation v2.0 §3)             │
  │                         │                                          │
  │ Entity-Compiled         │ Majority channels positive.              │
  │ positive-dominant       │ Presence = approach + reward.            │
  │                         │ Loss = grief (body-base amputation).     │
  │                         │ ≈ old "Entity-Owned" concept.            │
  │                         │ VD: bạn thân, con, mẹ healthy.          │
  │                         │                                          │
  │ Entity-Compiled         │ Majority channels negative.              │
  │ negative-dominant       │ Presence = threat/dissonance.            │
  │                         │ Loss = relief (or emptiness if obsess).  │
  │                         │ VD: bully, abuser, đối thủ obsessive.   │
  │                         │                                          │
  │ Entity-Compiled         │ Significant BOTH positive AND negative   │
  │ mixed                   │ channels CÙNG LÚC. ★ PHỔ BIẾN NHẤT.    │
  │                         │ Behavior oscillates by state/context.    │
  │                         │ Loss = complex grief (relief + pain).    │
  │                         │ VD: bố mẹ strict, vợ chồng conflict.    │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Entity-Compiled ≠ approach/avoidance tag:
     Approach/avoidance = Tầng 1 (per-chunk, đơn giản: +/-)
     Entity-Compiled = Tầng 2 (per-entity, multi-channel, structural)
     = BƯỚC NHẢY CHẤT: entity's state AFFECTS my body-base
     = Mất entity = body-base amputation (không chỉ "resource loss")

  ⚠️ Entity-Compiled ≠ Obligation:
     Entity-Compiled: "entity's state = MY state" (structural, automatic)
     Obligation: "predict cost to MAINTAIN access" (prediction, PFC-mediated)
     = 2 cơ chế INDEPENDENT — có thể high/low independently
     (Obligation.md v1.0 §2-§4)

  ⚠️ Mixed = PHỔ BIẾN NHẤT:
     Càng gần lâu → càng nhiều channels compile (cả + và -)
     "Thuần positive" = rare luxury of limited interactions
     "Vừa thương vừa giận" = NORMAL multi-channel compile, not pathological
```

---

## §8 — COMPILED/FRESH: PROCESSING LABELS (★ NEW v2.0)

```
⭐ TRỤC THẬT CỦA PROCESSING: COMPILATION LEVEL — KHÔNG PHẢI CONTENT

  "Logic" và "Feeling" = OBSERVER LABELS (mô tả cho người ngoài hiểu)
  BÊN TRONG BODY: chỉ có COMPILED ←→ FRESH spectrum
  Content (emotion/reasoning) KHÔNG quyết định processing level
  COMPILATION LEVEL quyết định

  (Inter-Body-Mechanism.md §3)

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Compiled processing     │ Automatic. Body-direct. Cost ≈ 0.       │
  │                         │ Hebbian reinforced qua nhiều lần.        │
  │                         │ "Cảm thấy" / "trực giác" / tức thời.   │
  │                         │ Dùng: khi processing KHÔNG cần PFC      │
  │                         │ draft (đã compile xong).                 │
  │                         │                                          │
  │                         │ VD: Einstein "thấy" lời giải toán       │
  │                         │ VD: Chef biết ngay thiếu muối           │
  │                         │ VD: Bạn thân biết ngay mood nhau        │
  │                         │                                          │
  │ Fresh processing        │ PFC draft. Deliberate. Cost > 0.         │
  │ (= Fresh PFC draft)     │ Mỗi lần = effort (chưa compile).        │
  │                         │ "Phải nghĩ" / "phải phân tích".         │
  │                         │ Dùng: khi PFC đang chain novel paths.    │
  │                         │                                          │
  │                         │ VD: Người mới học toán phải suy luận    │
  │                         │ VD: Therapist gặp case lạ phải phân tích│
  │                         │ VD: Người lạ phải đoán cảm xúc nhau    │
  │                         │                                          │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ TRANSITION LABELS:      │                                          │
  │                         │                                          │
  │ Fresh → Compiled        │ LEARNING: lặp lại + verify OK →         │
  │ (learning)              │ Hebbian strengthen → automatic.          │
  │                         │ = "Logic → feeling" (cho person đó).     │
  │                         │                                          │
  │ Compiled → Fresh        │ DISRUPTION: context mới, error detect → │
  │ (disruption)            │ phải re-evaluate deliberately.           │
  │                         │ = "Feeling → logic" (phải suy nghĩ lại).│
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘


  ⭐ "LOGIC" vs "FEELING" = OBSERVER LABELS — DÙNG KHI NÀO?

  ┌────────────────────────────┬───────────────────────────────────────┐
  │ Context                    │ Label phù hợp                         │
  ├────────────────────────────┼───────────────────────────────────────┤
  │ Phân tích mechanism:       │ Compiled / Fresh (ĐÚNG)               │
  │ Mô tả cho người thường:   │ Logic / Feeling (OK, nhưng biết là    │
  │                            │ observer labels, không phải mechanism) │
  │ Research / deep analysis:  │ Compiled / Fresh (BẮT BUỘC)           │
  │ Observation parameter:     │ Logic-Feeling (tên file, observation) │
  └────────────────────────────┴───────────────────────────────────────┘

  ⚠️ "Logic" = compiled chunks SHAREABLE (deterministic domain: toán, vật lý)
  ⚠️ "Intuition" = compiled chunks NOT EASILY SHAREABLE (probabilistic domain: tâm lý)
  ⚠️ BÊN TRONG: cơ chế GIỐNG HỆT. Khác: SHAREABILITY, không phải quality.
  ⚠️ RETIRED: "Con người 100% feeling ở tầng nền" — terminology collision.
     v4.0 framing: PFC = Lawyer + Learning Trajectory (Logic-Feeling.md v4.0 §4.3).
     = PFC serve body-base (Lawyer). Fresh → compile → Body-Knowing (Learning Trajectory).
     = Same insight, mechanism-level, không dùng từ "feeling" collision-prone.
```

---

## §9 — INTER-BODY: INTERACTION LABELS (★ NEW v2.0)

```
⭐ VOCABULARY CHO INTER-BODY INTERACTION (Inter-Body-Mechanism.md):

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  A) BY-PRODUCT MATCH / ANTI-MATCH (Inter-Body §5.4, By-Product-Gap-Resonance v1.0):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ by-product match        │ B fill gap CỦA B (§2C) → output =       │
  │                         │ by-product → match A's gap direction     │
  │                         │ → A receives reward.                     │
  │                         │ = Cơ chế NỀN TẢNG inter-body feed.      │
  │                         │ Dùng: khi mô tả HOW 2 entities feed.    │
  │                         │                                          │
  │ anti-match              │ By-product CONFLICT gap direction (§2C). │
  │                         │ Worse than no-match = ACTIVE friction.   │
  │                         │ VD: CEO đổi mới ↔ người thích an nhàn.  │
  │                         │ Dùng: khi by-product gây dissonance.     │
  │                         │                                          │
  │ mutual match            │ CẢ 2 receive reward từ interaction.      │
  │ (= Resonance)   │ A match B AND B match A.                 │
  │                         │ Dùng: khi cả 2 bên có by-product match. │
  │                         │                                          │
  │ one-way match           │ Chỉ 1 bên receive reward.               │
  │                         │ VD: parasocial, service asymmetric.      │
  │                         │ Dùng: khi match không mutual.            │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  B) 2-STREAM ARCHITECTURE (By-Product-Gap-Resonance v1.0 §2):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Hardware-Stream                │ Hardware/Unidirectional by-product match. │
  │ (hardware/unidirect.)   │ Reward từ EXISTENCE/thuộc tính bên kia. │
  │                         │ Không cần engagement ngược lại.          │
  │                         │ HABITUATES (Weber-Fechner).              │
  │                         │ Cảm RIÊNG (mỗi bên không biết bên kia). │
  │                         │ Dùng: khi reward từ presence/attribute.  │
  │                         │                                          │
  │ Modeling-Stream                │ Self-Pattern-Modeling compiled mutual (bidirectional).     │
  │ (Self-Pattern-Modeling mutual)            │ CẦN cả 2 engage Self-Pattern-Modeling → feedback loop.    │
  │                         │ 2 não ĐỒNG BỘ. Can CHANGE other's state.│
  │                         │ ANTI-HABITUATION (Hebbian → stronger).   │
  │                         │ Unsustainable if 1-sided.                │
  │                         │ Dùng: khi mô tả deep mutual connection. │
  │                         │                                          │
  │ Proto-Modeling-Stream          │ Modeling-Stream primitive (không full Self-Pattern-Modeling).     │
  │                         │ Mẹ-bé: contingent response.             │
  │                         │ Người-chó: associative matching.         │
  │                         │ Dùng: khi có mutual exchange nhưng       │
  │                         │ thiếu full Self-Pattern-Modeling bilateral.                │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  C) 3 INDEPENDENT COST SOURCES (Inter-Body §4):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ cost (general)          │ TOTAL COST = ① + ② + ③.                 │
  │                         │ Dùng: khi nói chung "interaction costly".│
  │                         │                                          │
  │ ① PFC draft cost        │ PFC chain novel paths → processing load.│
  │                         │ f(chain_length × novelty_degree).        │
  │                         │ = Fresh processing (§8) has COST.        │
  │                         │ Dùng: khi mô tả cognitive effort.        │
  │                         │                                          │
  │ ② suppress cost         │ Override compiled response → efference   │
  │                         │ mismatch → body resist → dissonance.     │
  │                         │ f(intensity × duration).                 │
  │                         │ = Body MUỐN X, bắt làm Y → mismatch.    │
  │                         │ Dùng: khi mô tả phải kìm nén.           │
  │                         │                                          │
  │ ③ uncertainty cost      │ Multiple options, none compiled → hold   │
  │                         │ open → cortisol. f(options×time×stakes). │
  │                         │ = Không biết đáp án → phải chờ → stress. │
  │                         │ Dùng: khi mô tả chưa chắc/không biết.   │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ 3 cost sources INDEPENDENT (có thể appear riêng lẻ hoặc cùng lúc)
  ⚠️ SUSTAINABILITY = f(total cost × frequency ÷ reward)
  ⚠️ Cost KHÔNG đến từ "dùng logic" per se — đến từ 3 nguồn cụ thể này
  ⚠️ Connection to §2: cost cao + body-need không được fill = unsustainable

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  D) 5-CHANNEL INPUT VECTOR (Inter-Body §6):

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Ch1 — Hardware Sensory  │ Domain reality input NOW.                │
  │                         │ Visual, auditory, tactile, olfactory.    │
  │                         │                                          │
  │ Ch2 — Body State        │ Internal homeostasis.                    │
  │                         │ Hormone, glucose, cortisol, fatigue.     │
  │                         │                                          │
  │ Ch3 — Compiled Chunks   │ Associative fire from past.              │
  │                         │ Memory, pattern, schema, habit loops.    │
  │                         │                                          │
  │ Ch4 — Entity Actions    │ What others DO/SAY.                      │
  │                         │ Words, facial expression, behavior.      │
  │                         │                                          │
  │ Ch5 — PFC Active Chain  │ Reasoning in progress.                   │
  │                         │ Ongoing cognitive process → feedback.    │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Channel DOMINANT → determines vulnerability:
     Ch1 dominant = grounded in reality (protected)
     Ch4 dominant = entity controls activation (vulnerable)
     Multiple channels CONFIRM = strong drive (hard to manipulate)
     Single channel ONLY = dangerous (scam, limerence)

  ⚠️ "Input Channel Control = Power":
     Ai control input channels CỦA NGƯỜI KHÁC = control hành vi
     (Scam: control Ch4 + amplify Ch2 + block Ch1 = victim follows)
  ⚠️ Connection to §2: 5 channels = 5 ways to ACTIVATE body-need

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  E) SUPPLEMENTARY LABELS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Compilable Architecture          │ Human system: general-purpose reward +   │
  │                         │ compilation + social hardware.           │
  │                         │ Trade-off: flexible but 15-20yr compile. │
  │                         │ (vs Hardwired Architecture: specific-reward)     │
  │                         │ Dùng: khi giải thích WHY human system.   │
  │                         │ (Inter-Body §1.2)                        │
  │                         │                                          │
  │ PFC = Lawyer            │ PFC tạo narrative CHO body-base.         │
  │                         │ NOT neutral judge — biện hộ cho client.  │
  │                         │ Body-need (§2) fire TRƯỚC → PFC justify. │
  │                         │ Dùng: khi phân tích PFC narrative ≠      │
  │                         │ actual body-need.                        │
  │                         │ (Inter-Body §7, Gazzaniga split-brain)   │
  │                         │                                          │
  │ Domain Reality          │ Final arbiter. CANNOT be permanently     │
  │ = Final Arbiter         │ fooled. Timeline varies (seconds→years). │
  │                         │ Dual Check: body=quality controller,     │
  │                         │ domain=final arbiter.                    │
  │                         │ Dùng: khi note "thực tế sẽ verify."     │
  │                         │ (Inter-Body §6.4, Ask-AI v3.1)          │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘
```

---

## §10 — OBSERVATION VS MECHANISM (KHÁC TẦNG)

```
⭐ BODY-FEEDBACK ≠ FEELING — 2 TẦNG KHÁC NHAU:

  ┌──────────────────┬───────────────────────────────────────────────┐
  │ Tầng             │ Mô tả                                         │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ BODY-FEEDBACK    │ MECHANISM: signal từ body → chạy 24/7         │
  │ (mechanism)      │ 95% VÔ THỨC (PFC không quan sát được)         │
  │                  │ Labels: body-need, gap, reward, dissonance,   │
  │                  │ prediction-delta, chunk-miss/shift/gap,       │
  │                  │ Compiled/Fresh, 3-cost, 5-Channel (§2-§9)    │
  │                  │ = FILE NÀY mô tả vocabulary của tầng này      │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ FEELING          │ OBSERVATION: PFC quan sát body-feedback        │
  │ (observation)    │ 7-layer gradient (implicit → explicit)         │
  │                  │ Labels: "pleasant" / "comfortable" /           │
  │                  │ "satisfied" / "vague" / "nagging unease" /     │
  │                  │ "discomfort" / "stuck" / "emptiness" /         │
  │                  │ "apathetic"                                    │
  │                  │ = Feeling.md v2.2 mô tả vocabulary của tầng   │
  │                  │ này                                            │
  └──────────────────┴───────────────────────────────────────────────┘

  ⚠️ NHẦM LẪN HAY GẶP:

    "Pleasant" ≠ reward:
      → "Pleasant" = PFC observation body-base reward
        (Feel-Location/Feel-Labeling: đã observe + label)
      → Reward có thể CHẠY mà PFC không observe
        (Feel-RawSignals/Feel-Integration: body signal nhưng PFC chưa thấy)
      → = Body-base reward XẢY RA mà không "cảm thấy pleasant" (possible)

    "Discomfort" ≠ dissonance:
      → "Discomfort" = PFC observation OF dissonance signal
      → Dissonance chạy 24/7, PFC chỉ observe 1 phần nhỏ
      → = "Background-Pattern" dissonance = invisible (Background-Pattern.md)

    "Trực giác" ≠ chỉ feeling:
      → "Trực giác" = compiled processing (§8: TOÀN BỘ: cả toán, cả cảm xúc)
      → Chef "biết" thiếu muối = trực giác = COMPILED (không phải "feeling only")
      → Trục thật: Compiled/Fresh — không phải Logic/Feeling content

  (Feeling.md v2.2: feeling = PFC observation body-feedback)
  (01-Foundation.md §5: 7-layer clarity gradient)
```

---

## §11 — QUY TẮC SỬ DỤNG

### §11.1 — Nguyên tắc chính

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

  ③ "reward" = body-base reward (CẢ Evaluative VÀ Direct-State):
     KHÔNG giới hạn vào opioid / Evaluative
     Direct-State (touch, exercise, warmth) = reward THẬT, ĐÚNG label

  ④ PHÂN BIỆT compiled (tags) vs momentary (signals):
     Approach/avoidance = đã tích lũy trên chunk (§7)
     Reward/dissonance = đang xảy ra ngay bây giờ (§3/§4)

  ⑤ PHÂN BIỆT mechanism (body-feedback) vs observation (feeling):
     Body-feedback labels: reward, dissonance, prediction-delta,...
     Feeling labels: "pleasant", "comfortable", "satisfied",
       "vague", "nagging unease", "discomfort",
       "stuck", "emptiness", "apathetic"
     KHÔNG dùng feeling labels thay body-feedback labels (§10)

  ⑥ DÙNG "Compiled/Fresh" khi phân tích mechanism:
     "Logic/Feeling" = ok cho mô tả bên ngoài (observer perspective)
     "Compiled/Fresh" = BẮT BUỘC cho deep analysis (mechanism level)
     KHÔNG nói "feeling phản đối logic" → nói "compiled conflict fresh" (§8)

  ⑦ 3-COST = 3 nguồn riêng, KHÔNG gộp:
     "Mệt" có thể = ① PFC draft, ② suppress, ③ uncertainty, hoặc COMBO
     Label CỤ THỂ nguồn cost → hiểu mechanism → biết cách giảm (§9C)

  ⑧ ENTITY-COMPILED ≠ APPROACH TAG:
     Approach tag = per-chunk, đơn giản (+/-) (§7 Tầng 1)
     Entity-Compiled = per-entity, multi-channel, structural (§7 Tầng 2)
     KHÔNG nói "approach tag toward mother"
     → nói "Entity-Compiled mixed (mother)"

  ⑨ BODY-NEED = nền, KHÔNG phải signal:
     Body-need (§2) = STATE (trạng thái CẦN — LUÔN tồn tại)
     Body-feedback = SIGNAL (body BÁO CÁO về state)
     KHÔNG nói "body-need fire" → nói "body-feedback fire vì body-need X"
     Body-need = CONTEXT, body-feedback = COMMUNICATION
```

### §11.2 — Ví dụ áp dụng

```
  VÍ DỤ 1: Lương tăng từ 10tr → 15tr

  TIER 2 (đủ cho Research files):
    "Body-need [survival] có gap [income].
     10tr → body-base reward (gap fill đúng direction) → habituated.
     15tr → prediction-delta nhỏ hơn → reward giảm (gap đã shrink)."

  TIER 3 (cho deep analysis):
    "Body-need [survival] có gap [income direction: ≥10tr/tháng].
     10tr (lần đầu):
       prediction-delta (mới) → DRD4 pass → PFC spotlight
       → body-base check: chunk [lương 10tr] khớp gap direction
       → Evaluative Reward
       → chunk compile: [lương 10tr = approach tag]
     10tr (tháng 12):
       habituated: cùng pattern → no prediction-delta → no alert
       → gap ĐÃ fill → body-feedback baseline
     15tr:
       prediction-delta (khác baseline 10tr) → body-base check
       → gap shrink (đã fill phần lớn) → reward giảm
       → = Diminishing returns = gap shrink over time"


  VÍ DỤ 2: Mẹ-con mâu thuẫn (inter-body):

  TIER 2:
    "Con: Entity-Compiled mixed (mother). Hardware-Stream habituated.
     Modeling-Stream có nhưng conflict direction.
     Cost: ② suppress cao (kìm nén) + ③ uncertainty (mẹ unpredictable).
     By-product: mẹ fill gap CỦA MẸ (dạy dỗ) → output anti-match
     con's gap direction (autonomy)."

  TIER 3:
    "Con: Entity-Compiled mixed [nutrition++, comfort++, autonomy--, status+/-]
     Body-need [autonomy] có gap [direction: tự quyết định].
     Mẹ nói 'phải học': Ch4 dominant → compiled chunks Ch3 fire
     [cấm đoán schema] → body-state Ch2 cortisol ↑
     → suppress cost ② (compiled muốn phản bác nhưng kìm)
     → uncertainty cost ③ (mẹ phạt hay thôi?)
     → dissonance: chunk-gap [autonomy direction blocked]
     By-product mechanism: Mẹ fill gap 'nuôi dưỡng tốt' (CỦA MẸ)
     → output = ép học → anti-match con's gap direction [tự do khám phá]
     PFC = Lawyer: con narrative 'mẹ không hiểu mình' (may be 0.3 accuracy)"
```

---

## §12 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback.md v1.1            │ ENTRY POINT. §4 4 trục. §6 Body-Feedback-Precondition.     │
  │                                  │ Đọc TRƯỚC file này.                 │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Mechanism.md v2.0  │ §1 Body-Need aggregate. §2 2 sources.│
  │                                  │ §3 3 dynamics. Tier 3 labels.        │
  │                                  │ SOURCE cho §2 Foundation.            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Inter-Body-Mechanism.md v1.0     │ §2 Body-Need. §3 Compiled/Fresh.    │
  │                                  │ §4 3-cost. §5 By-product match.     │
  │                                  │ §6 5-Channel. §7 PFC=Lawyer.        │
  │                                  │ §8 Entity-Compiled.                  │
  │                                  │ SOURCE cho §8+§9 file này.          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Gap-Direction.md v2.0            │ §1 Definition: gap = f(surrounding   │
  │                                  │ chunks). "Chưa biết = không gap."   │
  │                                  │ SOURCE cho §2C Foundation.           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Reward-Signal-Architecture.md    │ §1 Evaluative/Direct-State.          │
  │ v2.0                             │ §2 E₀→E₃. §4 5 Profiles.            │
  │                                  │ Tier 2-3 reward labels.              │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ 03-Reward.md v1.1                │ §2 7-step mechanism.                 │
  │                                  │ §3 Body-Feedback-Preconditions. Step 5 detail. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.0       │ §7.7 5 Roles. Amplifier, not cause. │
  │                                  │ Tier 3 dissonance labels.            │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Valence-Propagation.md v2.0      │ §3 Entity-Compiled (3 subtypes).     │
  │                                  │ Approach/avoidance tags.             │
  │                                  │ Compiled vs momentary distinction.   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ By-Product-Gap-Resonance.md v1.0        │ §2 2-Stream Architecture.            │
  │                                  │ Hardware-Stream/2/Proto labels defined.     │
  │                                  │ By-product match + anti-match.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Feeling.md v2.2                  │ PFC observation of body-feedback.    │
  │                                  │ 7-layer gradient. KHÁC TẦNG (§10).  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Base.md v3.3                │ L0+L1 substrate. Compilable Architecture.     │
  │                                  │ System-level context cho §2A.        │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Threat.md                        │ 5 mức × 3 trục × 3 nguồn.           │
  │                                  │ Tier 2 dissonance label: threat.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Ask-AI.md v3.1                   │ Dual Check: body = quality           │
  │                                  │ controller, domain = final arbiter.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Clarification/ folder            │ Bridge mainstream → framework.       │
  │                                  │ NƠI DUY NHẤT thảo luận terminology  │
  │                                  │ ngoài framework + tại sao framework │
  │                                  │ dùng label khác.                     │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

> *Body-Feedback Label Convention v2.0 — Vocabulary Reference.*
> *100% framework vocabulary.*
> *3-tier system: cụ thể nhất có thể, chung nhất nếu bắt buộc.*
>
> *§2 Foundation: body-need = aggregate CẦN. Gap = specific missing. Drive = push hành vi.*
> *§3-§6 Signals: reward / dissonance / prediction-delta / baseline.*
> *§7 Compiled: approach/avoidance tags + Entity-Compiled 3 subtypes.*
> *§8 Processing: Compiled/Fresh = trục thật (Logic/Feeling = observer labels).*
> *§9 Inter-Body: by-product match, 2-Stream, 3-cost, 5-Channel.*
> *§10 Distinction: body-feedback (mechanism) ≠ feeling (observation).*
>
> *Body-need = STATE. Body-feedback = SIGNAL. Gap direction = WHY match works.*
> *"Chuông cửa" ≠ "quà đằng sau cửa."*
