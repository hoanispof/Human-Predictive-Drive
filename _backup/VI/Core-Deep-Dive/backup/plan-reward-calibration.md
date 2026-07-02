# Plan: Reward-Calibration.md

> **Ngày tạo plan:** 2026-05-10
> **Mục đích:** Plan chi tiết để session sau triển khai Reward-Calibration.md
> **Nguyên tắc:** Observation file — giúp NHẬN DIỆN, không prescribe

---

## 1. VỊ TRÍ TRONG FRAMEWORK

```
Reward-Calibration.md trả lời câu hỏi MỚI:

  03-Reward.md:           KHI NÀO reward fires? (H10, 5 preconditions)
  RSA:                    Reward fire CHẤT LƯỢNG thế nào? (Type A/B, 5 Profiles)
  Gap-Direction.md:       TẠI SAO reward personal? (gap có hướng)
  Gratitude.md §3-4:      Anti-habituation + baseline shift
  Education-Mechanism §3: Bridge (external reward) trong giáo dục

  Reward-Calibration.md:  BAO NHIÊU reward là ENOUGH cho gap NÀY,
  (FILE MỚI)              người NÀY, context NÀY?
                          Và chuyện gì xảy ra khi quá ít / quá nhiều?

  = CALIBRATION question — tương tự Cortisol-Baseline.md
    (không phải cortisol per se mà calibration of amplifier)
```

**Folder:** Core-Deep-Dive/Body-Base/Body-Feedback/
(ngang hàng RSA, Gap-Direction, BFM)

**KHÔNG PHẢI:** Applications file. Đây là MECHANISM observation — calibration
là property CỦA reward system, không phải application bên ngoài.

---

## 2. CORE THESIS

```
⭐ REWARD CÓ GOLDILOCKS PER-GAP:

  Quá ít reward cho gap → gap chưa fill → dissonance kéo dài
  Vừa đủ reward cho gap → gap fill + approach tag + chunk compile
  Quá nhiều reward cho gap → NHIỀU cơ chế hại (§4)

  VÀ: Goldilocks KHÔNG CỐ ĐỊNH:
  → Khác per-person (hardware: COMT × DRD4 × receptor sensitivity)
  → Khác per-gap-type (Shift vs Miss vs Gap — 3 dynamics khác nhau)
  → Khác per-context (cortisol state, existing chunks, relationship)
  → Khác per-time (threshold adapt, baseline shift, development stage)

  → KHÔNG THỂ prescribe "cho X reward" → chỉ có thể OBSERVE + ADJUST
  → = Dynamic equilibrium, không phải fixed formula
```

---

## 3. CẤU TRÚC FILE (~1,200-1,500 dòng dự kiến)

### §0 — VỊ TRÍ + SCOPE (~80L)
- File này vs 5 file liên quan (bảng phân biệt)
- Observation file = giúp nhìn thấy, KHÔNG prescribe
- Scope: reward calibration = property of reward system
- Reader flow: đọc SAU 03-Reward + RSA

### §1 — CORE: REWARD CÓ GOLDILOCKS PER-GAP (~120L)
- Thesis: reward amount có sweet spot per gap
- "Chưa biết = không có gap" (Gap-Direction.md) → reward cho thứ chưa có gap = WASTED
- 3 zones: Under / Match / Over
- Ví dụ mở đầu: đường (ít = nhạt, vừa = ngon, nhiều = ngấy)
  = A₀ hardware level. Cùng pattern ở MỌI loại reward.

### §2 — 3 GAP TYPES × REWARD MATCH (~200L)
Map 3 chunk dynamics (BFM) × reward phù hợp:

```
┌──────────────┬─────────────────────────────┬──────────────────────────┐
│ Gap Type     │ Nature                      │ Reward Match             │
├──────────────┼─────────────────────────────┼──────────────────────────┤
│ Chunk-Shift  │ Context đổi → baseline đổi  │ RE-ANCHOR reward:        │
│              │ "Chuyển nhà, đổi việc"      │ giúp build baseline MỚI  │
│              │ (BFM §3.1)                  │ = Type B effective       │
│              │                             │ (body-state, grounding)  │
├──────────────┼─────────────────────────────┼──────────────────────────┤
│ Chunk-Miss   │ Expected X, got <X          │ COMPENSATE reward:       │
│              │ "Kỳ vọng lương cao, được ít" │ fill delta OR adjust    │
│              │ (BFM §3.2)                  │ expectation              │
│              │                             │ = Type A evaluative      │
│              │                             │ ⚠️ fill delta vs adjust  │
│              │                             │ expectation = 2 paths    │
├──────────────┼─────────────────────────────┼──────────────────────────┤
│ Chunk-Gap    │ Structure predict C → C     │ EXPLORATION reward:      │
│              │ chưa compile → hole         │ bridge qua exploration   │
│              │ "Chưa biết, muốn biết"      │ = VTA delta (novelty)   │
│              │ (BFM §3.3)                  │ + opioid khi fill        │
│              │                             │ = Profile ② Coherence    │
└──────────────┴─────────────────────────────┴──────────────────────────┘
```

- Sai loại reward cho sai gap = WASTED hoặc HẠI
- VD: Chunk-Miss (kỳ vọng lương) mà cho Type B (massage) = sai gap
- VD: Chunk-Gap (muốn hiểu) mà cho tiền = sai gap (tiền ≠ coherence reward)

### §3 — GOLDILOCKS ZONE: 3 TRẠNG THÁI (~200L)

**Under-reward** (quá ít cho gap):
- Gap chưa fill → dissonance KÉO DÀI
- Cortisol Role ② Holding: amplifier đồng hành arc chưa resolve
- Direction: có thể shift approach → avoidance nếu kéo dài
- VD: lương quá thấp vs năng lực → cortisol sustained → leave hoặc burnout

**Match** (vừa đủ cho gap):
- Gap fill + VTA delta + opioid confirm
- Chunk compile với approach tag
- Body state: brief positive → reset → sẵn sàng gap tiếp
- VD: lương match năng lực + recognition đúng lúc → drive ổn định

**Over-reward** (quá nhiều cho gap — §4 sẽ chi tiết):
- GAP ĐÃ FILL nhưng reward VẪN ĐẾN → surplus
- Surplus reward = KHÔNG CÓ gap để match → vào đâu?
- → Threshold adaptation, baseline shift, dependency, v.v. (§4)

### §4 — OVER-REWARD: 6 CƠ CHẾ HẠI (~300L) ← PHẦN MỚI NHẤT

```
6 CƠ CHẾ:

① THRESHOLD ADAPTATION (Gratitude §4 + old RE §1.4):
  Reward liên tục → baseline TĂNG → cùng reward = PE giảm → cần NHIỀU HƠN
  = Hedonic treadmill. Cơ chế: VTA delta GIẢM vì baseline đã shift
  VD: Lương tăng → adapt → lương mới = bình thường → cần tăng NỮA
  VD: Đường ngọt → adapt → cần NGỌT HƠN
  🟢 Brickman & Campbell 1971, Frederick & Loewenstein 1999

② OVERJUSTIFICATION (Education-Mechanism §3, old RE §9.3):
  External reward MẠNH HƠN internal PE → não chỉ track external
  Rút external → PE = 0 → dừng hành vi DÙ trước đó thích
  VD: Cho tiền vẽ → hết tiền → không vẽ nữa (DÙ trước đó tự vẽ)
  🟢 Deci 1971, Lepper 1973

③ BRIDGE DEPENDENCY (Education-Mechanism §3.4):
  Nguồn ④ dominate quá lâu → ①②③ KHÔNG emerge
  Rút bridge = anchor crash
  VD: Trẻ chỉ học khi có kẹo → không kẹo = không học
  VD: Nhân viên chỉ làm vì bonus → không bonus = không effort

④ BASELINE SHIFT (Gratitude §4):
  Gift/reward habituate → CÙng reward = PE ≈ 0
  "Quen rồi" = baseline đã TĂNG → mất reward = PE ÂM (dù trước đó = bonus)
  VD: Xe công ty → quen → mất xe = đau (dù trước đó = thưởng)

⑤ COMPETENCE-REWARD MISMATCH:
  Reward VÀ competence lệch → dissonance KHÁC:
  - Reward > competence: imposter feeling + xung quanh adjust ngược
    ("trời ko chịu đất thì đất phải chịu trời")
    Status.md: Resource Access Map bị lệch → social recalibration
  - Competence > reward: undervalued → leave hoặc resentment
  = Dynamic equilibrium: 2 bên adjust liên tục

⑥ A/B IMBALANCE:
  Quá nhiều Type A evaluative → mất khả năng Type B simple pleasures
  "Giàu nhưng không biết vui" = A₃ threshold CAO + B bị neglect
  Ngược: quá nhiều Type B → thiếu depth → "vui nhưng trống rỗng"
  = A/B ratio cần BALANCE, không maximize 1 loại
```

### §5 — DYNAMIC EQUILIBRIUM: TẠI SAO KHÔNG THỂ PRESCRIBE (~200L)

- Reward calibration = perception-action cycle giữa reward-giver và receiver
- Sếp ↔ nhân viên: 2 bên adjust liên tục, KHÔNG có điểm cố định
- Bố mẹ ↔ con: bridge ↔ response ↔ adjust
- Xã hội ↔ cá nhân: obligation ↔ autonomy ↔ adjust
- Logic-Feeling-Balance.md parallel: KHÔNG THỂ prescribe balance
  cho cái đang dao động → infinite regress
- Domain feedback = trọng tài duy nhất (mỗi người tự calibrate)
- File này giúp NHẬN DIỆN trạng thái → KHÔNG nói "làm gì"

### §6 — OBSERVABLE INDICATORS (~200L) ← THỰC HÀNH
Qua giao tiếp + hành vi, CÓ THỂ quan sát (xác suất, không chắc chắn):

```
UNDER-REWARD SIGNALS:
- Verbal: "không xứng đáng", "chán", "thiếu"
- Behavior: effort giảm, tìm nguồn khác, avoidance tích lũy
- Body: cortisol sustained visible (mệt mỏi, ngủ kém, irritable)

MATCH SIGNALS:
- Verbal: ít nói về reward (habituated = invisible — Gratitude §4!)
- Behavior: ổn định, drive tự duy trì, approach tags visible
- Body: baseline stable

OVER-REWARD SIGNALS:
- Threshold adapt: "chưa đủ" DÙ objective cao + peer comparison
- Overjustification: "không ai trả thì không làm" cho thứ TỪNG thích
- Dependency: panic khi bridge giảm, KHÔNG có internal drive
- Mismatch: imposter feeling, hoặc xung quanh resentment
- A/B imbalance: "giàu nhưng buồn" (A excess) hoặc "vui nhưng trống" (B excess)

⚠️ QUAN SÁT ≠ CHẨN ĐOÁN:
- Observable = xác suất, không chắc chắn
- Cùng behavior có thể = nhiều nguyên nhân khác nhau
- AI-Schema-Detection.md: 3-tầng model áp dụng
  (AI observe + Expert verify + Self confirm)
```

### §7 — TYPE A/B × CALIBRATION (~150L)
- Type A: conditional, threshold ADAPT, CẦN anti-habituation
  → Goldilocks phức tạp hơn (P1-P5 all required)
- Type B: hardware-based, threshold ÍT adapt, RELIABLE
  → Goldilocks đơn giản hơn (body-state range)
  → "Safe baseline reward" khi A exhausted
- A Gates B implication: A calibration ẢNH HƯỞNG B experience
  → Over-calibrate A → block B → "giàu nhưng không thấy vui"

### §8 — REWARD-ECONOMICS INSIGHTS GIỮA LẠI (~150L)
Từ Reward-Economics.md cũ, insights VẪN ĐÚNG qua v7.8 lens:

- 6 paths "giàu rồi vẫn đuổi tiền" → map sang v7.8 mechanisms:
  ① Schema chưa update = Background-Pattern.md (compiled deep, invisible)
  ② Threshold adapt = §4① (hedonic treadmill)
  ③ Proxy tầng 2-3 = RSA 5 Profiles (đuổi Profile ②③, không phải ①)
  ④ Prolactin thấp = PFC-Hardware (receptor system)
  ⑤ Identity lock = Meaning §3.3 IDENTITY type anchor
  ⑥ Cortisol treadmill = Cortisol-Baseline §7.7 Role ④ Inertia

- Tiền = proxy token cho prediction (shared chunk prediction xã hội)
- Habituation Blindness × Economics (PE=0 ≠ Value=0)

### §9 — HONEST ASSESSMENT (~80L)
- 🟢🟡🔴 per section
- File này = OBSERVATION SYNTHESIS, không tạo mechanism mới
- Giá trị: tổng hợp insights từ ~8 files vào 1 góc nhìn calibration
- Risk: có thể simplify quá (reality = continuous, high-dimensional)
- Predictions testable

### §10 — CROSS-REFERENCES (~50L)
~15 files reference

---

## 4. DEPENDENCIES (cần đọc trước khi viết)

```
MUST READ (core mechanism cho content):
✅ 03-Reward.md — H10, 7-step, 7 cases (ĐÃ ĐỌC)
✅ Reward-Signal-Architecture.md — Type A/B, 5 Profiles, A Gates B (ĐÃ ĐỌC)
✅ Body-Feedback-Mechanism.md — 3 dynamics, 2 sources (ĐÃ ĐỌC)
✅ Gap-Direction.md — gap has direction, "chưa biết = không có gap" (ĐÃ ĐỌC)
✅ Gratitude.md — §3 anti-habituation, §4 baseline shift (ĐÃ ĐỌC header)
✅ Education-Mechanism.md §3 — bridge, 4 nguồn fill, overjustification (ĐÃ ĐỌC)
✅ Reward-Economics.md — insights cần giữ (ĐÃ ĐỌC TOÀN BỘ)

SHOULD READ (for cross-refs + examples):
□ Cortisol-Baseline.md §7.7 — 5 Cortisol Roles (Role ② ④ relevant)
□ Status.md — Resource Access Map (competence-reward mismatch)
□ Logic-Feeling-Balance.md — infinite regress parallel
□ PFC-Hardware.md v1.1 — COMT × Reward Pattern (per-person calibration)
□ Background-Pattern.md — invisible bias on gap direction
□ Connection.md §9 — calibration 2-chiều (dynamic equilibrium parallel)
```

---

## 5. NGUYÊN TẮC VIẾT

1. **Observation, KHÔNG prescribe** — giúp NHÌN THẤY reward state,
   không nói "cho bao nhiêu reward"
2. **Reference, không lặp** — H10, Type A/B, 3 dynamics đã có →
   reference section + line, không copy
3. **Ví dụ cụ thể** — mỗi mechanism cần ≥1 ví dụ đời thường
4. **6 cơ chế over-reward = phần MỚI nhất** — đây là giá trị chính
   của file (chưa tồn tại ở đâu trong framework)
5. **Dynamic equilibrium = thesis chính** — reward calibration
   KHÔNG CÓ điểm cố định → file PHẢN ÁNH điều này
6. **🟢🟡🔴 confidence tags** — per claim
7. **v7.8 aligned** — no old Core.md references

---

## 6. WHAT THIS FILE IS NOT

- ❌ KHÔNG phải "cách thiết kế reward" (prescriptive)
- ❌ KHÔNG phải economics file (Reward-Economics.md cũ)
- ❌ KHÔNG lặp H10 hay RSA (reference only)
- ❌ KHÔNG phải education file (Education-Mechanism §3 đã cover bridge)
- ❌ KHÔNG phải HR file (HR-Management.md = application layer)

---

## 7. SESSION SAU: EXECUTION ORDER

```
Phase 1: Đọc thêm SHOULD READ files (Cortisol §7.7, Status, Logic-Feeling-Balance,
         PFC-Hardware §3.4, Background-Pattern, Connection §9)
Phase 2: Viết §0-§1 (position + core thesis)
Phase 3: Viết §2-§3 (gap types × reward match + Goldilocks zone)
Phase 4: Viết §4 (6 cơ chế over-reward — phần lớn nhất + mới nhất)
Phase 5: Viết §5-§6 (dynamic equilibrium + observable indicators)
Phase 6: Viết §7-§10 (Type A/B calibration + economics insights + assessment + refs)
Phase 7: Review toàn bộ + update File Index
```

---

> *Plan ready. Compact session → Session sau triển khai từ plan.*
