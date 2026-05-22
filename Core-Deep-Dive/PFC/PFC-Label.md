---
title: PFC-Label Convention — Vocabulary Reference
version: 1.0
created: 2026-05-22
status: REFERENCE v1.0
scope: |
  VOCABULARY REFERENCE: Quy ước label cho toàn bộ PFC-related concepts.
  Formalize 3-tier label system: General → Direction → Specific.
  13 domain: Roles, Processing, Operations, Cost, Quality, Regions, Hardware,
  Simulation Engine, Cognitive Ops, Failure Modes, Observer/Mechanism, Deprecated.
  KHÔNG giải thích mechanism (source files làm việc đó).
  CHỈ formalize: LABEL NÀO, NGHĨA GÌ, KHI NÀO DÙNG.
purpose: |
  PFC vocabulary xuất hiện trong 78+ files nhưng CHƯA BAO GIỜ được formalize.
  Cùng 1 concept → 3-5 tên khác nhau → confusion.
  File này: VOCABULARY REFERENCE cho toàn bộ PFC-related labels.
  Companion của Body-Feedback-Label v2.0 (body-feedback vocabulary).
  BFL = body SIGNAL vocabulary. File này = PFC OPERATION vocabulary.
  Overlap ở BFL §8/§9C = bridge zone (cross-ref, không lặp).
position: |
  Core-Deep-Dive/PFC/ — ngang hàng PFC-Operations.md, Simulation-Engine.md.
  ĐỌC NGAY SAU PFC-Function.md (entry point) và PFC-Operations.md (mechanism).
dependencies:
  - PFC-Operations.md v1.0 — §2-§4 Hold/Suppress, §5 Quality, §9 Budget, §10 3-Cost
  - Simulation-Engine.md v1.0 — §1-§3 Engine/Components/Axes, §6 mPFC gradient
  - Logic-Feeling.md v2.1 — Compiled/Fresh spectrum, observer labels (companion)
  - PFC-Function.md v1.2 — 24 functions, 5 categories (companion)
  - PFC-Hardware.md v1.1 — COMT, DRD4, NE, capacity/quality
  - PFC-Hold-Dimensions.md — ~4±1 slots, interference limit
  - Body-Feedback-Label.md v2.0 — §8 Compiled/Fresh, §9C 3-cost (companion)
  - Ask-AI.md v3.1 — Dual Check: body=QC, domain=final arbiter
  - Autonomy-Hardware.md v1.1 — vmPFC/DRN, controllability
  - Cortisol-Baseline.md v2.1 — cortisol × PFC damage, NE α1
sources:
  - Drill-PFC-Label v1.0 (1,153L, 16 sections, 24 citations)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# PFC-Label Convention — Vocabulary Reference

> **PFC-related vocabulary xuất hiện trong 78+ files.**
> **Nhưng cùng 1 concept → 3-5 tên khác nhau → confusion.**
>
> **"Fresh" / "PFC-Fresh" / "draft" / "operation" = cùng 1 vùng concept, KHÁC level.**
> **"PFC" = Observer? Lawyer? Director? Universal Resource? = tùy context.**
>
> **File này: VOCABULARY REFERENCE cho toàn bộ PFC-related labels.**
> **KHÔNG giải thích mechanism (source files làm việc đó).**
> **CHỈ formalize: LABEL NÀO, NGHĨA GÌ, KHI NÀO DÙNG.**
>
> **Companion: Body-Feedback-Label v2.0 (body SIGNAL vocabulary).**
> **File này = PFC OPERATION vocabulary. Overlap ở BFL §8/§9C = bridge zone.**

---

## Mục lục

- §0 — TẠI SAO CẦN FILE NÀY
- §1 — 3-TIER LABEL SYSTEM + 4 VOCABULARY LEVELS
- §2 — PFC ROLE LABELS (5 vai trò tùy context)
- §3 — PROCESSING SPECTRUM: COMPILED ←→ FRESH (brief)
- §4 — PFC OPERATIONS: HOLD + SUPPRESS (labels)
- §5 — PFC COST LABELS (3-cost + budget)
- §6 — COMPILED QUALITY LABELS (genuine / schema / threat)
- §7 — PFC REGION LABELS (anatomy mapping)
- §8 — PFC HARDWARE LABELS (individual differences)
- §9 — SIMULATION ENGINE LABELS (1 engine, 3 components)
- §10 — PFC COGNITIVE LABELS (spotlight, narrative, labeling, check)
- §11 — PFC FAILURE MODES (5 patterns)
- §12 — OBSERVER vs MECHANISM (Logic/Feeling vs Compiled/Fresh)
- §13 — DEPRECATED TERMS + STANDARDIZATION
- §14 — USAGE RULES
- §15 — HONEST ASSESSMENT
- §16 — CROSS-REFERENCES
- §17 — RESEARCH CITATIONS

---

## §0 — TẠI SAO CẦN FILE NÀY

```
⭐ PFC VOCABULARY = PHÂN TÁN + KHÔNG NHẤT QUÁN:

  VẤN ĐỀ 1 — CÙNG CONCEPT, NHIỀU TÊN:
    "Fresh" / "PFC-Fresh" / "draft" / "Fresh processing" = 4 labels
    cho concept PROCESSING CHƯA COMPILED.
    → File nào dùng tên nào? Không ai biết.

  VẤN ĐỀ 2 — CÙNG TỪ, KHÁC LEVEL:
    "Fresh" = TRẠNG THÁI trên spectrum (position)
    "PFC operations" = HÀNH ĐỘNG (HOLD + SUPPRESS)
    "draft" = hành động CỤ THỂ (1 loại HOLD)
    → 3 level khác nhau dùng lẫn lộn → confuse.

  VẤN ĐỀ 3 — PFC CÓ NHIỀU VAI TRÒ:
    Observer (Feeling.md), Lawyer (PFC-Operations.md §10),
    Director (Neural-Processing-Flow),
    Universal Resource (PFC-Operations.md §9),
    Quality Controller (Ask-AI v3.1 §6.1)
    → Vai trò nào áp dụng khi nào?

  VẤN ĐỀ 4 — PFC FILES PHÂN TÁN:
    PFC-Function.md, PFC-Hardware.md, PFC-Development.md,
    PFC-Hold-Dimensions.md, PFC-Configuration.md,
    PFC-Operations.md, Simulation-Engine.md,
    Logic-Feeling.md, Logic-Feeling-Balance.md
    → 9+ files riêng về PFC → vocabulary nào ở file nào?

  VẤN ĐỀ 5 — OVERLAP VỚI BODY-FEEDBACK-LABEL:
    BFL §8 đã cover Compiled/Fresh processing labels.
    BFL §9C đã cover 3-cost sources.
    → File này BỔ SUNG (PFC operations, roles, regions, hardware),
    KHÔNG lặp.


  ⭐ FILE NÀY GIẢI QUYẾT:
    → Formalize vocabulary cho TOÀN BỘ PFC-related concepts
    → Standardize: 1 label duy nhất cho 1 concept
    → Deprecate: "draft" standalone, "PFC-Fresh" redundant (§13)
    → 3-tier system: consistent với Body-Feedback-Label
    → Phân biệt rõ LEVEL: state / action / sub-action / role
```

---

## §1 — 3-TIER LABEL SYSTEM + 4 VOCABULARY LEVELS

```
⭐ QUY TẮC CHỌN TIER (tương tự Body-Feedback-Label §1):

  Tier 3 (CỤ THỂ NHẤT) > Tier 2 (DIRECTION) > Tier 1 (CHUNG NHẤT)

  → Khi biết CỤ THỂ PFC đang làm gì → dùng Tier 3:
    "dlPFC HOLD new pattern → ① PFC draft cost"

  → Khi biết DIRECTION nhưng không specific → dùng Tier 2:
    "Fresh processing" / "HOLD" / "SUPPRESS"

  → Khi CHỈ BIẾT PFC involved → dùng Tier 1:
    "PFC processing" / "PFC cost"


  AUDIENCE-APPROPRIATE:

    Chuyên gia / deep analysis:
      → Tier 3 chủ đạo. Region + operation + cost traced.

    Người muốn hiểu / Research files:
      → Tier 2 chủ đạo: "Fresh processing", "HOLD", "suppress cost"
      → Đủ chính xác, đủ hiểu mechanism cơ bản.

    General / overview:
      → Tier 1 khi cần: "PFC đang xử lý" / "PFC tốn"
      → Có thể drill sâu hơn nếu cần.


  4 LEVEL CỦA PFC VOCABULARY:

    ┌────────────────────────────────────────────────────┐
    │ LEVEL 1 — ROLES (PFC "là" gì trong context đó):   │
    │   Observer, Lawyer, Director, Universal Resource,  │
    │   Quality Controller                               │
    │                                                    │
    │ LEVEL 2 — STATES (vị trí trên spectrum):           │
    │   Compiled ←→ Fresh                                │
    │                                                    │
    │ LEVEL 3 — OPERATIONS (PFC làm gì):                 │
    │   HOLD = amplify new                               │
    │   SUPPRESS = block existing                        │
    │                                                    │
    │ LEVEL 4 — SUB-OPERATIONS (cụ thể):                 │
    │   "draft novel path" = specific HOLD action         │
    │   "inhibit compiled response" = specific SUPPRESS   │
    └────────────────────────────────────────────────────┘

  ⚠️ KHÔNG trộn level:
    ✗ "PFC-Fresh operation" (trộn state với operation)
    ✓ "Fresh processing requires HOLD operation" (phân biệt)
    ✗ "draft" standalone (mơ hồ — state? action? output?)
    ✓ "PFC HOLD draft novel path" (operation + sub-action rõ ràng)
```

---

## §2 — PFC ROLE LABELS

```
⭐ PFC CÓ 5 VAI TRÒ TÙY CONTEXT — DÙNG ĐÚNG VAI TRÒ:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Role Label              │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ ① PFC = Observer        │ PFC QUAN SÁT body-feedback output.       │
  │                         │ Reactive, KHÔNG generative.              │
  │                         │ ~5% decisions, 95% body tự xử lý.       │
  │                         │ "Đọc output, không tạo output."          │
  │                         │ Dùng: khi nhấn mạnh PFC KHÔNG điều      │
  │                         │ khiển mà chỉ quan sát.                   │
  │                         │ (Feeling.md, PFC-Function.md §1)         │
  │                         │                                          │
  │ ② PFC = Lawyer          │ PFC tạo narrative CHO body-base.         │
  │                         │ Post-hoc justification. Confabulation.   │
  │                         │ KHÔNG neutral judge — biện hộ cho body.  │
  │                         │ Body-need fire TRƯỚC → PFC justify SAU.  │
  │                         │ Dùng: khi phân tích PFC narrative ≠      │
  │                         │ actual body-need.                        │
  │                         │ (PFC-Operations.md §10, Gazzaniga)       │
  │                         │                                          │
  │ ③ PFC = Director        │ PFC điều hướng, KHÔNG compute trực tiếp. │
  │   (Orchestrator)        │ Bias spreading activation. Chọn hướng.   │
  │                         │ "Đạo diễn chỉ hướng, diễn viên tự diễn."│
  │                         │ Dùng: khi nhấn mạnh PFC chỉ BIAS,       │
  │                         │ không thực hiện computation.             │
  │                         │ (Neural-Processing-Flow)                 │
  │                         │                                          │
  │ ④ PFC = Universal       │ PFC budget = FINITE, SHARED cho TẤT CẢ. │
  │   Resource              │ Learning, SPM, decisions, suppress,      │
  │                         │ social, self-monitor, Imagine-Final.     │
  │                         │ Mệt ở work → SPM cho con YẾU.           │
  │                         │ Dùng: khi phân tích PFC budget trade-off │
  │                         │ giữa các hoạt động.                     │
  │                         │ (PFC-Operations.md §9)                   │
  │                         │                                          │
  │ ⑤ PFC = Quality         │ Dual Check: body = quality controller,   │
  │   Controller            │ domain = final arbiter.                  │
  │                         │ PFC check body output VỚI domain reality.│
  │                         │ DUY NHẤT system có thể check domain.     │
  │                         │ Dùng: khi nhấn mạnh PFC verify function. │
  │                         │ (Ask-AI v3.1 §6.1)                      │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ 5 roles KHÔNG MÂU THUẪN — cùng 1 PFC, KHÁC GÓC NHÌN:
     Observer = perspective (PFC đọc gì)
     Lawyer = output quality (PFC justify cho ai)
     Director = mechanism (PFC tác động thế nào)
     Universal Resource = resource constraint (PFC bị giới hạn sao)
     Quality Controller = verification function (PFC check gì)

  ⚠️ ĐỪNG dùng "PFC = controller" hay "PFC = boss":
     PFC KHÔNG điều khiển body. Body xử lý 95% tự động.
     PFC chỉ BIAS direction + OBSERVE output.
```

---

## §3 — PROCESSING SPECTRUM: COMPILED ←→ FRESH

> PFC-Operations.md v1.0 §1 = full treatment.
> Body-Feedback-Label v2.0 §8 = cùng labels phía body.
> Section này = BRIEF label reference.

```
⭐ TRỤC THẬT CỦA PROCESSING = COMPILATION LEVEL:

  COMPILED ─────────────────────────────────────── FRESH
  (automatic)                                    (PFC-mediated)
  body-direct                                    deliberate
  cost ≈ 0                                      cost > 0
  "cảm thấy biết"                               "phải nghĩ ra"
  Hebbian reinforced                            mỗi lần = effort mới


  ┌─────────┬─────────────────────────┬──────────────────────────────────┐
  │ Tier    │ Label                   │ Nghĩa                           │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ processing              │ Chung nhất. PFC involved.        │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ Compiled processing     │ Automatic. Body-direct. Cost ≈ 0.│
  │         │ Fresh processing        │ PFC-mediated. Deliberate.        │
  │         │ Semi-compiled           │ Mixed: phần compiled, phần fresh.│
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ Fresh → Compiled        │ LEARNING: lặp lại + verify OK.  │
  │ (trans.)│ (learning)              │ = "Logic → feeling" (observer).  │
  │         │ Compiled → Fresh        │ DISRUPTION: context mới, error.  │
  │         │ (disruption)            │ = "Feeling → logic" (observer).  │
  └─────────┴─────────────────────────┴──────────────────────────────────┘

  ⚠️ "Compiled/Fresh" = TRỤC MECHANISM. "Logic/Feeling" = OBSERVER LABELS.
     Khi phân tích mechanism: BẮT BUỘC dùng Compiled/Fresh.
     Khi mô tả cho người ngoài: "Logic/Feeling" OK (nhưng biết là approximate).

  ⚠️ Spectrum, KHÔNG binary:
     Mỗi chunk nằm SOMEWHERE trên spectrum.
     "Expert partially stuck" = compiled phần quen, fresh phần mới.

  (Body-Feedback-Label §8 = CÙNG labels. PFC-Operations.md §1 = SOURCE.)
```

---

## §4 — PFC OPERATIONS: HOLD + SUPPRESS

> PFC-Operations.md v1.0 §2-§4 = full mechanism.
> Section này = LABEL reference only.

```
⭐ PFC CÓ 2 OPERATIONS TRÊN SPECTRUM:

  ┌─────────┬─────────────────────────┬──────────────────────────────────┐
  │ Tier    │ Label                   │ Nghĩa                           │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ PFC operation           │ Chung nhất. PFC đang hành động. │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ HOLD (= PFC Amplify)    │ Amplify pattern mới/yếu.        │
  │         │                         │ CAN compile → sustainable.       │
  │         │                         │ Cost: ① PFC draft.               │
  │         │                         │ Region: dlPFC, FEF.              │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ SUPPRESS (= PFC Inhibit)│ Block pattern đã compiled.       │
  │         │                         │ CANNOT compile "not" → unsust.   │
  │         │                         │ Cost: ② Suppress (efference).    │
  │         │                         │ Region: rIFG, vlPFC.             │
  └─────────┴─────────────────────────┴──────────────────────────────────┘

  ⚠️ HOLD ≠ SUPPRESS — KHÁC CĂN BẢN:

    ┌──────────────┬────────────────────┬────────────────────┐
    │              │ HOLD               │ SUPPRESS            │
    ├──────────────┼────────────────────┼────────────────────┤
    │ Direction    │ BOOST new          │ BLOCK existing      │
    │ Body feels   │ "Effort" (neutral) │ "Not being me"      │
    │ Compile?     │ CAN compile new    │ Cannot compile "not"│
    │ Sustainable  │ Yes (→compile→free)│ No (cost persists)  │
    │ Cost source  │ ① PFC draft       │ ② Efference mismatch│
    └──────────────┴────────────────────┴────────────────────┘


  4 TỔ HỢP:

    ① Hold only       — Học mới, không xung đột. Cost: ①. DỄ NHẤT.
    ② Hold + Suppress — Học mới ĐỒNG THỜI block cũ. Cost: ① + ②. DOUBLE.
                         3 outcomes: A (genuine shift), B (compiled suppress),
                         C (failure/burst). (PFC-Operations.md §4)
    ③ Suppress only   — Block mà không thay thế. Cost: ②. TỆ NHẤT.
                         Wegner ironic process: rebound.
    ④ Neither         — Compiled chạy tự động. Cost: ≈ 0. Không PFC.

  (PFC-Operations.md §2-§4 = SOURCE mechanism chi tiết.)
```

---

## §5 — PFC COST LABELS

> PFC-Operations.md v1.0 §9-§10 = full mechanism.
> Body-Feedback-Label v2.0 §9C = cùng labels phía body.
> Section này = LABEL reference only.

```
⭐ 3 INDEPENDENT COST SOURCES + BUDGET:

  ┌─────────┬─────────────────────────┬──────────────────────────────────┐
  │ Tier    │ Label                   │ Nghĩa                           │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ PFC cost                │ Chung nhất. PFC đang tốn.       │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 2  │ ① PFC draft cost        │ Metabolic cost từ HOLD.          │
  │         │                         │ f(chain_length × novelty).       │
  │         │                         │ GIẢM DẦN khi compile (→ ≈ 0).   │
  │         │                         │ Region: dlPFC, FEF.              │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ ② Suppress cost         │ Efference mismatch từ SUPPRESS.  │
  │         │                         │ f(intensity × duration).         │
  │         │                         │ KHÔNG GIẢM (pattern vẫn fire).   │
  │         │                         │ = "Not being me" feeling.        │
  │         │                         │ Region: rIFG, vlPFC.             │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ ③ Uncertainty cost      │ Multiple options, none compiled. │
  │         │                         │ Hold open → cortisol.            │
  │         │                         │ f(options × time × stakes).      │
  │         │                         │ GIẢM khi commit (chọn 1 → hold).│
  │         │                         │ Region: ACC (conflict).          │
  ├─────────┼─────────────────────────┼──────────────────────────────────┤
  │ TIER 1  │ PFC budget              │ TỔNG resource PFC có thể dùng.  │
  │ (system)│ (= Universal Resource)  │ FINITE. SHARED cho MỌI hoạt     │
  │         │                         │ động: learning, SPM, decisions,  │
  │         │                         │ suppress, social, self-monitor,  │
  │         │                         │ Imagine-Final.                   │
  │         ├─────────────────────────┼──────────────────────────────────┤
  │         │ Total cost              │ = ① + ② + ③ cộng lại.           │
  └─────────┴─────────────────────────┴──────────────────────────────────┘

  ⚠️ 3 cost sources INDEPENDENT (xuất hiện riêng lẻ hoặc cùng lúc):
     Chỉ ① = learn something new (effort nhưng ổn)
     Chỉ ② = suppress something old (mệt và unsustainable)
     ① + ② = thay đổi thói quen (double cost — WHY change is hard)
     ① + ② + ③ = đổi career lúc chưa biết đi đâu (TRIPLE — max load)

  ⚠️ PFC budget GIẢM bởi:
     Fatigue (end of day), Cortisol (stress), Sleep deprivation,
     Illness, Chronic suppress (accumulated ② cost)
     → "Mệt ở work → SPM cho con YẾU" = budget ĐÃ HẾT, không phải lazy.

  ⚠️ ① CAN GIẢM (compile → automatic). ② CANNOT GIẢM (pattern stays).
     → Long-term: HOLD-heavy strategies >> SUPPRESS-heavy strategies.

  (PFC-Operations.md §9-§10 = SOURCE. BFL §9C = CÙNG labels.)
```

---

## §6 — COMPILED QUALITY LABELS

> PFC-Operations.md v1.0 §5 = full mechanism.
> Section này = LABEL reference only.

```
⭐ COMPILED CHUNKS CÓ QUALITY DIMENSION — PHÂN BIỆT 3 LOẠI:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Genuine-compiled        │ Body reward THẬT confirmed → compile.    │
  │                         │ → approach tag.                          │
  │                         │ → SPM EXPANSIVE (rich body data).        │
  │                         │ VD: Mẹ thích nấu ăn → genuine compiled  │
  │                         │ hiểu "ngon = gì" → creative SPM cho con.│
  │                         │ Dùng: khi compiled qua trải nghiệm thật │
  │                         │ + body confirm.                          │
  │                         │                                          │
  │ Schema-compiled         │ PFC / obligation / social compliance.    │
  │                         │ → neutral tag.                           │
  │                         │ → SPM LIMITED (narrow, rule-based).      │
  │                         │ VD: "Ai cũng học" → compile HOW TO do   │
  │                         │ nhưng KHÔNG compile WHY body likes.      │
  │                         │ Dùng: khi compiled qua rule/schema,      │
  │                         │ không phải body engagement.              │
  │                         │                                          │
  │ Threat-compiled         │ Forced / threat / bị ép → compile.       │
  │                         │ → avoidance tag.                         │
  │                         │ → SPM BIASED (fear-based patterns).      │
  │                         │ VD: Bị đánh → compile "đừng nói ý kiến" │
  │                         │ → SPM: predict người khác sẽ phạt.       │
  │                         │ Dùng: khi compiled dưới áp lực/đe dọa.  │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⭐ QUALITY = COMPILE-TIME LOCK:
    Tag (approach/neutral/avoidance) được gắn LÚC COMPILE.
    Sau compile → tag KHÔNG ĐỔI.
    Cùng kiến thức, cùng level compiled — KHÁC quality → KHÁC suốt đời.

  ⚠️ CÙNG OUTPUT, KHÁC QUALITY:
    Genuine-compiled "biết nấu soup" ≠ Schema-compiled "biết nấu soup"
    Genuine: body data rich → CAN generalize → creative
    Schema: rule data only → CANNOT generalize → repeat same

  ⚠️ 3 quality types KHÔNG đổi được → phải BUILD NEW (genuine) bên cạnh.
    "Fix" threat-compiled ≠ xóa → compile THÊM genuine pattern mới.

  (PFC-Operations.md §5 = SOURCE chi tiết.)
```

---

## §7 — PFC REGION LABELS

```
⭐ CÁC VÙNG PFC VÀ MAPPING TRONG FRAMEWORK:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Region Label            │ Framework mapping + khi nào dùng         │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ dlPFC                   │ Working memory. Planning. Cognitive      │
  │ (dorsolateral PFC)      │ control. ~4±1 dimensions.                │
  │                         │ = HOLD operation hub.                    │
  │                         │ Dùng: khi trace HOLD to specific region. │
  │                         │                                          │
  │ vlPFC                   │ Response inhibition. Rule maintenance.   │
  │ (ventrolateral PFC)     │ = SUPPRESS operation hub.                │
  │                         │ Dùng: khi trace SUPPRESS to region.      │
  │                         │                                          │
  │ vmPFC                   │ Emotion regulation. Somatic bridge.      │
  │ (ventromedial PFC)      │ Amygdala connection (uncinate fasciculus)│
  │                         │ Controllability: vmPFC suppress DRN.     │
  │                         │ Cortisol damage → vmPFC weaken →         │
  │                         │ DRN regain → learned helplessness.       │
  │                         │ Dùng: khi trace emotion regulation,      │
  │                         │ autonomy, controllability.               │
  │                         │ (Autonomy-Hardware.md v1.1)              │
  │                         │                                          │
  │ mPFC                    │ Self-model. Social cognition. DMN hub.   │
  │ (medial PFC)            │ Simulation Engine Component 3:           │
  │                         │   Ventral = self + close others          │
  │                         │   Dorsal = dissimilar others             │
  │                         │ = GRADIENT (not binary).                 │
  │                         │ Entity-Compiled = migration from         │
  │                         │ dorsal → ventral.                        │
  │                         │ Dùng: khi trace SPM, self-model,         │
  │                         │ social prediction.                       │
  │                         │ (Simulation-Engine.md v1.0 §6)           │
  │                         │                                          │
  │ rIFG                    │ Inhibitory control hub.                  │
  │ (right inferior         │ Specific region WITHIN vlPFC area.       │
  │  frontal gyrus)         │ = SUPPRESS execution point.              │
  │                         │ Dùng: khi need precise anatomy label.    │
  │                         │ (Aron 2007)                              │
  │                         │                                          │
  │ ACC                     │ Conflict monitoring. Error detection.    │
  │ (anterior cingulate     │ PFC/limbic OVERLAP (not pure PFC).       │
  │  cortex)                │ = ③ Uncertainty cost detector.           │
  │                         │ Fires khi multiple options conflict.     │
  │                         │ Dùng: khi trace conflict/uncertainty.    │
  │                         │                                          │
  │ OFC                     │ Value computation. Reward expectation.   │
  │ (orbitofrontal cortex)  │ Integrates reward history.               │
  │                         │ Dùng: khi trace value judgment.          │
  │                         │                                          │
  │ FEF                     │ Attention direction. Eye movement.       │
  │ (frontal eye fields)    │ = HOLD attention component.              │
  │                         │ Dùng: khi trace attention allocation.    │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ KHOẢNG CÁCH TỪ REGION → FRAMEWORK CONCEPT:
    Region = physical structure. Framework concept = functional label.
    MAPPING có thể KHÔNG 1:1 (1 region → nhiều functions, 1 function → nhiều regions).
    Dùng region labels khi CẦN precision. Framework labels khi ANALYZE.

  ⚠️ Dùng TIER 2 (HOLD/SUPPRESS) thay vì Tier 3 (dlPFC/rIFG) trong HẦU HẾT cases.
    Region labels chỉ cần khi:
    → Research citation (cần specify anatomy)
    → Neural damage analysis (lesion → which function lost)
    → Cross-reference neuroscience literature
```

---

## §8 — PFC HARDWARE LABELS

```
⭐ INDIVIDUAL DIFFERENCES — TẠI SAO CÙNG 24 FUNCTIONS MÀ OUTPUT KHÁC:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ PFC hardware            │ Innate specs: wiring, receptors,         │
  │                         │ connection density. = CÁI KHÔNG ĐỔI     │
  │                         │ (hoặc đổi cực chậm).                    │
  │                         │ Dùng: general term cho individual diff.  │
  │                         │ (PFC-Hardware.md v1.1)                   │
  │                         │                                          │
  │ PFC quality             │ Chất lượng workspace PER-SLOT:           │
  │ (= PFC-Quality)         │ ① Resolution (rõ hay mờ)                │
  │                         │ ② Noise filter (giữ sạch dù nhiễu)     │
  │                         │ ③ Retrieval (lấy chunk nhanh/đúng)      │
  │                         │ ④ Compression (compile chặt hơn)        │
  │                         │ Dùng: khi phân tích chất lượng xử lý.   │
  │                         │                                          │
  │ PFC clear speed         │ COMT-dependent. Tốc độ xóa draft cũ.   │
  │ (= COMT clear)          │ Val/Val: FAST = "Improviser"             │
  │                         │   (flexible, switch nhanh, unstable).    │
  │                         │ Met/Met: SLOW = "Specialist"             │
  │                         │   (focused, deep, incremental).          │
  │                         │ Val/Met: intermediate.                   │
  │                         │ Dùng: khi phân tích tốc độ xử lý.       │
  │                         │ (PFC-Hardware.md §3)                     │
  │                         │                                          │
  │ PFC slots               │ ~4±1 dimensions (NOT separate boxes).    │
  │ (= working memory       │ Interference limit (physics constraint). │
  │  dimensions)            │ SỐ slots GIỐNG MỌI NGƯỜI (hardware).    │
  │                         │ CHẤT LƯỢNG per-slot khác (PFC quality).  │
  │                         │ Compiled chunks: pyramidal stacking →    │
  │                         │ expert fit MORE trong cùng slots.        │
  │                         │ Dùng: khi phân tích working memory.      │
  │                         │ (PFC-Hold-Dimensions.md)                 │
  │                         │                                          │
  │ DRD4 filter             │ Receptor threshold cho prediction-delta. │
  │ (= chunk threshold)     │ 4R: sensitive (small delta detected).    │
  │                         │ 7R: coarse (only large delta).           │
  │                         │ Dùng: khi phân tích sensitivity.         │
  │                         │ (PFC-Hardware.md §4)                     │
  │                         │                                          │
  │ NE α2/α1                │ PFC circuit breaker under stress.        │
  │ (= stress threshold)    │ Normal: α2 (low NE) → PFC functions.    │
  │                         │ Stress: α1 (high NE) → PFC DISCONNECT.  │
  │                         │ Individual threshold varies.             │
  │                         │ Dùng: khi phân tích PFC under stress.    │
  │                         │ (PFC-Hardware.md §6, Arnsten 2009)       │
  │                         │                                          │
  │ MAO-A                   │ Mood stability (TOÀN NÃO, not PFC-only).│
  │ (= mood stability)      │ Serotonin + dopamine + NE metabolism.    │
  │                         │ Dùng: khi phân tích emotional stability. │
  │                         │ (PFC-Hardware.md §5)                     │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ "Improviser" vs "Specialist" = KHÔNG TỐT/XẤU — chỉ KHÁC profile.
  ⚠️ PFC capacity GIẢM bởi: age, cortisol, fatigue, sleep deprivation.
     Observed capacity = hardware ceiling × current state.
  ⚠️ "IQ" KHÔNG DÙNG trong framework — quá crude.
     Dùng: PFC quality + clear speed + DRD4 + compiled chunks = richer model.
```

---

## §9 — SIMULATION ENGINE LABELS

> Simulation-Engine.md v1.0 = full architecture.
> Section này = LABEL reference only.

```
⭐ 1 ENGINE, 3 COMPONENTS, N APPLICATIONS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ Simulation Engine       │ General-purpose brain substrate.         │
  │                         │ DMN + mPFC + anterior insula +           │
  │                         │ hippocampus. Retrieve → recombine →      │
  │                         │ simulate → readout.                      │
  │                         │ Dùng: khi nói về shared substrate cho    │
  │                         │ SPM, Self-Obs, Imagine-Final, etc.       │
  │                         │                                          │
  │ Component 1:            │ Anterior insula. Đọc body signals.       │
  │ Interoception           │ "MÀN HÌNH" — readout device.             │
  │                         │ Unique cho self-target.                  │
  │                         │ Dùng: khi trace body-signal readout.     │
  │                         │                                          │
  │ Component 2:            │ DMN + hippocampus. Recombine chunks.     │
  │ Constructive Simulation │ "CPU + RAM" — processing engine.         │
  │                         │ Dùng: khi trace simulation generation.   │
  │                         │                                          │
  │ Component 3:            │ mPFC gradient. Ventral=self+close,       │
  │ Self/Other Model        │ Dorsal=distant. "BẢNG ĐIỀU KHIỂN" —     │
  │                         │ chọn simulation target.                  │
  │                         │ Dùng: khi trace target selection.        │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  3 AXES (coordinates):

    Trục A — Target:    Self ←→ Close Other ←→ Far Other.
                         Gradient ventral → dorsal mPFC.

    Trục B — Time:      Past ← Present → Future (+ Counterfact.)

    Trục C — Operation: Observe ← Simulate → Evaluate/Construct.


  NAMED APPLICATIONS = TỌA ĐỘ cụ thể trong 3D space:

    SPM                  = (Other, Present, Simulate).
    Self-Observation     = (Self, Present, Observe).
    Imagine-Final        = (Self, Future, Simulate).
    Memory recall        = (Self, Past, Observe).
    Counterfactual       = (Self, Alt-Past, Simulate).
    Empathy simulation   = (Other, Present, Observe+Simulate).

  ⚠️ Luyện 1 component = improve ALL applications (shared substrate).
  ⚠️ Hỏng 1 component = degrade ALL applications (alexithymia = proof).
  ⚠️ Named applications = POINTS — unnamed apps = equally real.

  (Simulation-Engine.md v1.0 = SOURCE chi tiết.)
```

---

## §10 — PFC COGNITIVE LABELS

```
⭐ VOCABULARY CHO SPECIFIC PFC COGNITIVE OPERATIONS:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Label                   │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ PFC spotlight           │ Attention allocation. = VOLUME INCREASE  │
  │ (= attention allocation)│ in target region, NOT command.           │
  │                         │ Bottom-up (dopamine) or top-down (PFC).  │
  │                         │ "Tăng volume, không ra lệnh tính toán." │
  │                         │ Dùng: khi mô tả PFC chọn chú ý cái gì. │
  │                         │ (PFC-Hardware.md, Neural-Processing-Flow)│
  │                         │                                          │
  │ PFC narrative           │ Post-hoc verbal explanation.             │
  │                         │ MAY confabulate (PFC = Lawyer).          │
  │                         │ Body-need fire TRƯỚC → PFC justify SAU.  │
  │                         │ = Feeling Layer 7 (Explained — lossy).   │
  │                         │ Dùng: khi phân tích explanation ≠ cause. │
  │                         │ (Logic-Feeling-Balance.md)               │
  │                         │                                          │
  │ Labeling                │ PFC gán verbal chunk (word) cho body     │
  │ (= verbal coding)       │ pattern. Fidelity GIẢM 40-80%.          │
  │                         │ "Sướng" = label CHO body-base reward —   │
  │                         │ lossy representation.                    │
  │                         │ Dùng: khi phân tích PFC label ≠ body    │
  │                         │ experience.                              │
  │                         │ (Feeling.md, Blackbox-Map.md)            │
  │                         │                                          │
  │ PFC check               │ PFC verify output with domain reality.   │
  │ (= domain verification) │ = Quality Controller function (§2 ⑤).   │
  │                         │ DUY NHẤT system kiểm tra domain.         │
  │                         │ Dual Check: body + domain = 2 layers.    │
  │                         │ Dùng: khi mô tả verification process.   │
  │                         │ (Ask-AI v3.1)                            │
  │                         │                                          │
  │ Working memory           │ PFC maintain chunks active.             │
  │ compression             │ BEFORE compile: 5 separate slots needed. │
  │                         │ AFTER compile: 1 meta-chunk slot.        │
  │                         │ Expert: pyramidal stacking → more chunks │
  │                         │ trong cùng ~4±1 slots.                   │
  │                         │ Dùng: khi phân tích expertise ≠ IQ.      │
  │                         │ (Neural-Processing-Flow.md)              │
  │                         │                                          │
  │ Somatic-Articulation    │ Recursive loop: body pattern → external  │
  │ Loop (SAL)              │ articulation → body verify → refine.     │
  │                         │ PFC seeks words to match body-known.     │
  │                         │ AI catalyst CAN accelerate loop.         │
  │                         │ Dùng: khi mô tả "biết mà chưa nói      │
  │                         │ được" → articulation process.            │
  │                         │ (Somatic-Articulation-Loop.md)           │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ PFC spotlight ≠ attention (chung):
     PFC spotlight = PFC's specific mechanism of amplification.
     Attention (chung) = umbrella term bao gồm cả bottom-up + top-down.

  ⚠️ PFC narrative ≠ PFC check:
     Narrative = EXPLAIN (may confabulate — Lawyer function).
     Check = VERIFY (against domain — Quality Controller function).
     Giải thích ≠ Kiểm tra. "Tại sao" ≠ "Đúng không."
```

---

## §11 — PFC FAILURE MODES

```
⭐ 5 FAILURE PATTERNS — LABEL ĐỂ NHẬN DIỆN:

  ┌─────────────────────────┬──────────────────────────────────────────┐
  │ Failure Label           │ Nghĩa + khi nào dùng                    │
  ├─────────────────────────┼──────────────────────────────────────────┤
  │                         │                                          │
  │ ① Lawyer failure        │ PFC narrative ≠ body truth.              │
  │   (confabulation)       │ PFC justify body-need bằng logic SAI.    │
  │                         │ "Tôi buồn vì XYZ" → thật ra body mệt + │
  │                         │ hungry + stressed → bất kỳ trigger nào   │
  │                         │ cũng → PFC gắn nhãn sai.                │
  │                         │ Dùng: khi explanation ≠ actual cause.    │
  │                         │                                          │
  │ ② Philosopher trap      │ PFC imagine extensively nhưng NEVER      │
  │                         │ check domain → confident but WRONG.      │
  │                         │ "Nghĩ nhiều quá" mà không verify.        │
  │                         │ Dùng: khi phân tích excessive reasoning  │
  │                         │ without domain feedback.                 │
  │                         │ (Discovery-vs-Expansion.md)              │
  │                         │                                          │
  │ ③ Budget overload       │ PFC budget exceeded → quality DROPS      │
  │   (depletion)           │ ACROSS ALL activities.                   │
  │                         │ "Mệt ở work → SPM cho con yếu."         │
  │                         │ KHÔNG phải "lazy" — PFC budget = finite. │
  │                         │ Dùng: khi phân tích performance drop     │
  │                         │ after sustained PFC use.                 │
  │                         │                                          │
  │ ④ Suppress escalation   │ Too many domains suppressed →            │
  │   (→ learned            │ reward pathways THU HẸP → cortisol ↑ →  │
  │    helplessness)        │ vmPFC structural damage → DRN regain →   │
  │                         │ passive for EVERYTHING.                  │
  │                         │ Compiled suppress = DOOR closed.          │
  │                         │ Enough doors → room DARK.                │
  │                         │ Dùng: khi trace từ local suppress →      │
  │                         │ global helplessness.                     │
  │                         │ (PFC-Operations.md §8)                   │
  │                         │                                          │
  │ ⑤ Cortisol disconnect   │ Chronic cortisol → NE α1 activate →     │
  │   (PFC offline)         │ PFC DISCONNECT from body signals.         │
  │                         │ "Rage mode" / "freeze" / "numb."         │
  │                         │ PFC literally OFFLINE — not "weak will." │
  │                         │ Dùng: khi PFC KHÔNG FUNCTION             │
  │                         │ (stress/trauma response).                │
  │                         │ (PFC-Hardware.md §6, Arnsten 2009)       │
  │                         │                                          │
  └─────────────────────────┴──────────────────────────────────────────┘

  ⚠️ Failure modes = NHẬN DIỆN, không phải ĐỔ LỖI:
     "PFC failed" = structural/resource explanation, NOT moral judgment.
     Understanding failure mode → target intervention correctly.
```

---

## §12 — OBSERVER vs MECHANISM LABELS

> Logic-Feeling.md v2.1 = full treatment.
> Body-Feedback-Label v2.0 §10 = cùng distinction phía body.
> Section này = BRIEF reference.

```
⭐ "LOGIC/FEELING" vs "COMPILED/FRESH" — 2 TẦNG KHÁC NHAU:

  ┌──────────────────┬───────────────────────────────────────────────┐
  │ Tầng             │ Labels + khi nào dùng                         │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ MECHANISM        │ Compiled / Fresh.                              │
  │ (trục thật)      │ = Processing level BÊN TRONG body.            │
  │                  │ Content (emotion/reasoning) KHÔNG quyết định. │
  │                  │ COMPILATION LEVEL quyết định.                  │
  │                  │ Dùng: MỌI deep analysis, research, mechanism  │
  │                  │ files. BẮT BUỘC.                               │
  ├──────────────────┼───────────────────────────────────────────────┤
  │ OBSERVATION      │ Logic / Feeling.                               │
  │ (observer labels)│ = OBSERVER perspective — người ngoài nhìn vào.│
  │                  │ "Logic" = compiled chunks SHAREABLE            │
  │                  │   (deterministic: toán, vật lý).               │
  │                  │ "Intuition"/"Feeling" = compiled chunks        │
  │                  │   NOT EASILY SHAREABLE                         │
  │                  │   (probabilistic: tâm lý, inter-personal).    │
  │                  │ BÊN TRONG: cơ chế GIỐNG HỆT. Khác:           │
  │                  │ SHAREABILITY, không phải quality.              │
  │                  │ Dùng: mô tả cho người ngoài. Overview files.  │
  └──────────────────┴───────────────────────────────────────────────┘


  QUY TẮC SỬ DỤNG:

  ┌────────────────────────────┬───────────────────────────────────────┐
  │ Context                    │ Label phù hợp                         │
  ├────────────────────────────┼───────────────────────────────────────┤
  │ Phân tích mechanism:       │ Compiled / Fresh (ĐÚNG)               │
  │ Research / deep analysis:  │ Compiled / Fresh (BẮT BUỘC)           │
  │ Mô tả cho người thường:   │ Logic / Feeling (OK, approximate)     │
  │ Observation parameter file:│ Logic-Feeling (tên file, convention)  │
  │ Nói chung "con người":    │ "Con người 100% feeling ở tầng nền"   │
  │                            │ = mọi output = body-feedback           │
  └────────────────────────────┴───────────────────────────────────────┘

  ⚠️ KHÔNG NÓI "feeling phản đối logic":
    → NÓI "compiled pattern conflict với fresh processing"
    → Vì BÊN TRONG không có "feeling" vs "logic" — chỉ có compilation levels.

  ⚠️ "Trực giác" = compiled processing (CẢ toán CẢ cảm xúc):
    Chef biết thiếu muối = trực giác = COMPILED (not "feeling only")
    Einstein "thấy" lời giải = trực giác = COMPILED (not "logic only")

  (Logic-Feeling.md v2.1 = SOURCE. BFL §10 = CÙNG distinction.)
```

---

## §13 — DEPRECATED TERMS + STANDARDIZATION

```
⭐⭐ TERMS TO DEPRECATE + REPLACEMENTS:

  ┌─────────────────────┬─────────────────────┬──────────────────────────┐
  │ DEPRECATED          │ THAY THẾ            │ LÝ DO                    │
  ├─────────────────────┼─────────────────────┼──────────────────────────┤
  │                     │                     │                          │
  │ "PFC-Fresh"         │ "Fresh processing"  │ Redundant. Fresh ĐÃ      │
  │                     │ hoặc "Fresh"        │ implies PFC involvement. │
  │                     │                     │ "PFC-Fresh" = nói 2 lần. │
  │                     │                     │                          │
  │ "draft" (standalone │ STATE: "Fresh       │ "draft" mơ hồ — state?  │
  │  noun)              │  processing"        │ action? output?          │
  │                     │ ACTION: "HOLD" hoặc │ Trộn 3 levels.           │
  │                     │  "PFC HOLD"         │ Dùng "draft" CHỈ KHI     │
  │                     │ SPECIFIC: "PFC draft│ là VERB + object:        │
  │                     │  novel path"        │ "PFC draft novel path."  │
  │                     │                     │                          │
  │ "thinking" (as      │ "Fresh processing"  │ "Thinking" mơ hồ —      │
  │  mechanism label)   │                     │ cả compiled intuition    │
  │                     │                     │ cũng "thinking" theo     │
  │                     │                     │ nghĩa rộng.             │
  │                     │                     │                          │
  │ "willpower"         │ "PFC budget" hoặc   │ "Willpower" implies      │
  │                     │ "SUPPRESS capacity" │ moral quality.           │
  │                     │                     │ PFC budget = structural  │
  │                     │                     │ resource, not virtue.    │
  │                     │                     │                          │
  │ "self-control"      │ "Active SUPPRESS"   │ Specify: active vs       │
  │ (without specifying │ hoặc "Compiled      │ compiled suppress.       │
  │  which type)        │  SUPPRESS"          │ Khác mechanism, khác     │
  │                     │                     │ cost, khác sustainability.│
  │                     │                     │                          │
  │ "PFC controls       │ "PFC biases/directs"│ PFC KHÔNG control body.  │
  │  body"              │                     │ PFC bias direction.      │
  │                     │                     │ ~95% tự động.            │
  │                     │                     │                          │
  │ "conscious          │ "Deliberate" hoặc   │ "Conscious" misleading — │
  │  processing"        │ "Fresh processing"  │ compiled CAN also be     │
  │                     │                     │ "conscious" (aware of    │
  │                     │                     │ compiled output).        │
  │                     │                     │                          │
  └─────────────────────┴─────────────────────┴──────────────────────────┘


  ⭐ STANDARDIZED TERMS (DÙNG NHẤT QUÁN):

  ┌────────────────────────────┬─────────────────────────────────────────┐
  │ Concept                    │ STANDARD LABEL                          │
  ├────────────────────────────┼─────────────────────────────────────────┤
  │ Spectrum position:         │ "Compiled" / "Fresh" / "Semi-compiled"  │
  │ PFC actions on spectrum:   │ "HOLD" / "SUPPRESS" / "PFC operations"  │
  │ What PFC does during HOLD: │ "PFC draft novel path" (verb + object)  │
  │ Cost from HOLD:            │ "① PFC draft cost"                      │
  │ Cost from SUPPRESS:        │ "② Suppress cost"                       │
  │ Cost from indecision:      │ "③ Uncertainty cost"                     │
  │ Total resource:            │ "PFC budget"                             │
  │ Individual differences:    │ "PFC hardware" (general)                │
  │ Processing speed:          │ "PFC clear speed" / "COMT"              │
  │ Sensitivity:               │ "DRD4 filter"                            │
  │ Attention mechanism:       │ "PFC spotlight"                          │
  │ Post-hoc explanation:      │ "PFC narrative"                          │
  │ Verbal coding:             │ "Labeling" (with fidelity loss noted)    │
  │ Domain verification:       │ "PFC check" / "Dual Check"              │
  │ Shared substrate:          │ "Simulation Engine"                      │
  │ Compile quality:           │ "Genuine/Schema/Threat-compiled"         │
  │ Observer-level labels:     │ "Logic/Feeling" (with disclaimer)        │
  │ Mechanism-level labels:    │ "Compiled/Fresh" (BẮT BUỘC for analysis)│
  └────────────────────────────┴─────────────────────────────────────────┘
```

---

## §14 — USAGE RULES

```
⭐ QUY TẮC TỔNG HỢP:

  ① DÙNG ĐÚNG LEVEL:
     State → "Fresh" / "Compiled" (vị trí trên spectrum)
     Operation → "HOLD" / "SUPPRESS" (hành động PFC thực hiện)
     Sub-operation → "PFC draft novel path" (verb + object cụ thể)
     Role → "Observer" / "Lawyer" / "Director" / etc. (tùy context)
     ✗ KHÔNG trộn: "PFC-Fresh operation" (trộn state + operation)

  ② COMPILED/FRESH CHO MECHANISM, LOGIC/FEELING CHO OBSERVATION:
     Deep analysis: "compiled conflict fresh" (ĐÚNG)
     ✗ "feeling phản đối logic" (SAI ở mechanism level)
     Overview/mô tả: "Logic vs Feeling" (OK, approximate)

  ③ CỤ THỂ COST SOURCE:
     ✗ "PFC mệt" (quá chung — mệt vì gì?)
     ✓ "① PFC draft cost cao vì learning mới"
     ✓ "② Suppress cost vì phải kìm nén"
     ✓ "① + ② double cost vì thay đổi thói quen"

  ④ SPECIFY SUPPRESS TYPE:
     ✗ "đang suppress" (active hay compiled?)
     ✓ "Active suppress — PFC đang actively block"
     ✓ "Compiled suppress — đã compile thành meta-pattern"

  ⑤ PFC BUDGET TRADE-OFF:
     Khi phân tích "tại sao performance giảm":
     → Check: PFC budget đã dùng cho gì trước đó?
     → "Mệt ở work → SPM cho con yếu" = ④ Universal Resource

  ⑥ ĐỪNG ĐỔ LỖI — GIẢI THÍCH MECHANISM:
     ✗ "Không có ý chí" (moral judgment)
     ✓ "PFC budget depleted" hoặc "② suppress cost unsustainable"
     ✗ "Lazy"
     ✓ "Compiled suppress → reward pathways thu hẹp → flat affect"

  ⑦ REGION LABELS CHỈ KHI CẦN:
     Hầu hết cases → dùng Tier 2 (HOLD/SUPPRESS/PFC budget)
     Region (dlPFC/rIFG) → chỉ khi citation/anatomy/damage analysis

  ⑧ ROLE LABEL TÙY CONTEXT:
     Mô tả observation → PFC = Observer
     Phân tích narrative bias → PFC = Lawyer
     Giải thích mechanism → PFC = Director
     Budget trade-off → PFC = Universal Resource
     Verification → PFC = Quality Controller
     ĐỪNG dùng cùng lúc nhiều roles (confusing) — chọn 1 phù hợp nhất.

  ⑨ RELATIONSHIP VỚI BODY-FEEDBACK-LABEL:
     BFL §8 đã cover Compiled/Fresh processing labels.
     BFL §9C đã cover 3-cost labels.
     → File này BỔ SUNG: operations, roles, regions, hardware, failure modes.
     → KHÔNG lặp content — cross-reference.
     → 2 files cùng dùng → nhất quán vocabulary.
```

---

## §15 — HONEST ASSESSMENT

```
WHAT THIS FILE DOES WELL:

  ✓ Formalize 78+ files' PFC vocabulary thành 1 reference
  ✓ 3-tier system consistent với Body-Feedback-Label v2.0
  ✓ 4 vocabulary levels (Role/State/Operation/Sub-operation) phân biệt rõ
  ✓ 5 PFC roles với context rules
  ✓ Deprecated terms với replacements cụ thể
  ✓ Cross-ref strategy: BỔ SUNG, không lặp PFC-Operations / Sim-Engine / BFL


WHAT REMAINS UNCERTAIN:

  ? Region-to-function mapping có thể KHÔNG 1:1 — framework simplifies.
    Neuroscience vẫn đang refine các mapping này.

  ? "~4±1 slots" — số chính xác đang được debate.
    Framework dùng như approximate guide, không phải absolute.

  ? Ego depletion (glucose model) — R9 Hagger 2016 replication mixed.
    Framework dùng "PFC budget" như resource metaphor, không claim
    chuyên biệt về glucose mechanism.

  ? PFC narrative confabulation — extent varies by individual.
    Framework dùng "PFC = Lawyer" như tendency, không phải 100% confab.


WHAT THIS FILE DOES NOT COVER:

  ✗ Mechanism chi tiết (→ PFC-Operations.md v1.0)
  ✗ Simulation Engine architecture (→ Simulation-Engine.md v1.0)
  ✗ Compiled/Fresh full spectrum (→ Logic-Feeling.md v2.1)
  ✗ Body-feedback vocabulary (→ Body-Feedback-Label v2.0)
  ✗ PFC 24 functions catalog (→ PFC-Function.md v1.2)
  ✗ PFC development trajectory (→ PFC-Development.md)
  ✗ PFC hardware individual differences mechanism (→ PFC-Hardware.md v1.1)
```

---

## §16 — CROSS-REFERENCES

```
  ┌──────────────────────────────────┬──────────────────────────────────────┐
  │ File                             │ Connection                           │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Body-Feedback-Label v2.0         │ COMPANION. §8 Compiled/Fresh labels. │
  │                                  │ §9C 3-cost labels. File này BỔ SUNG. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Operations.md v1.0           │ SOURCE: §2-§4 Hold/Suppress, §5     │
  │                                  │ Quality, §8 Compiled Suppress, §9   │
  │                                  │ Budget, §10 3-Cost. MECHANISM file. │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Simulation-Engine.md v1.0        │ SOURCE: §1-§3 Engine/Components/    │
  │                                  │ Axes. §6 mPFC gradient. §7          │
  │                                  │ Alexithymia. ARCHITECTURE file.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Logic-Feeling.md v2.1            │ Compiled/Fresh spectrum full         │
  │                                  │ treatment. Observer labels. SOURCE.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Function.md v1.2             │ 24 functions, 5 categories.         │
  │                                  │ SOURCE cho "WHAT PFC does."         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Hardware.md v1.1             │ COMT, DRD4, NE, capacity/quality.   │
  │                                  │ SOURCE cho §8 hardware labels.      │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Hold-Dimensions.md           │ ~4±1 slots. Interference limit.     │
  │                                  │ SOURCE cho "PFC slots" label.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ PFC-Development.md               │ PFC lifetime trajectory. Training.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Ask-AI.md v3.1                   │ Dual Check: body = QC, domain =    │
  │                                  │ final arbiter. SOURCE cho §2 ⑤.    │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Feeling.md v3.0                  │ PFC observation of body-feedback.   │
  │                                  │ 7-layer gradient. Layer 7 = lossy.  │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Neural-Processing-Flow.md        │ PFC = Director/Orchestrator.        │
  │                                  │ Working memory compression.         │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Somatic-Articulation-Loop.md     │ SAL: body → articulate → verify.   │
  │                                  │ PFC seeks words for body-known.     │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Autonomy-Hardware.md v1.1        │ vmPFC / DRN. Controllability.       │
  │                                  │ Compiled suppress → helplessness.   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Cortisol-Baseline.md v2.1        │ Cortisol × PFC damage. NE α1.      │
  │                                  │ SOURCE cho §11 failure ⑤.          │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Logic-Feeling-Balance.md         │ PFC = Lawyer. Domain = final arbiter│
  │                                  │ Meta-principle: neither 100%.       │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Discovery-vs-Expansion.md        │ Philosopher trap. PFC imagine       │
  │                                  │ without domain check.               │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Self-Pattern-Modeling.md v3.1    │ APPLICATION 1 on Simulation Engine. │
  │                                  │ SPM = (Other, Present, Simulate).   │
  ├──────────────────────────────────┼──────────────────────────────────────┤
  │ Imagine-Final.md v3.0            │ APPLICATION 3 on Simulation Engine. │
  │                                  │ Imagine-Final = (Self, Future,      │
  │                                  │ Construct).                         │
  └──────────────────────────────────┴──────────────────────────────────────┘
```

---

## §17 — RESEARCH CITATIONS

```
  ┌────┬──────────────────────────────────────────────┬─────────┬──────────┐
  │ #  │ Citation                                      │ Used in │ Evidence │
  ├────┼──────────────────────────────────────────────┼─────────┼──────────┤
  │ R1 │ Miller & Cohen 2001 — Integrative Theory PFC │ §4      │ 🟢      │
  │ R2 │ Baddeley 2003 — Working Memory                │ §4, §10 │ 🟢      │
  │ R3 │ Aron 2007 — rIFG Inhibitory Control           │ §4, §7  │ 🟢      │
  │ R4 │ Wegner 1987 — Ironic Process Mental Control   │ §4      │ 🟢      │
  │ R5 │ Kahneman 2011 — System 1/2                    │ §3      │ 🟢      │
  │ R6 │ Evans & Stanovich 2013 — Dual Process Theory  │ §3      │ 🟢      │
  │ R7 │ Klein 1998 — Naturalistic Decision Making     │ §3      │ 🟢      │
  │ R8 │ Gailliot & Baumeister 2007 — Glucose Depletion│ §5      │ 🟢      │
  │ R9 │ Hagger et al. 2016 — Ego Depletion Replication│ §5      │ 🟢      │
  │ R10│ Maier & Seligman 2016 — Controllability       │ §7, §11 │ 🟢      │
  │ R11│ McEwen 2007 — Cortisol vmPFC Damage           │ §7, §11 │ 🟢      │
  │ R12│ Arnsten 2009 — PFC NE α1 Disconnect           │ §8, §11 │ 🟢      │
  │ R13│ Gazzaniga — Split-Brain Confabulation          │ §2      │ 🟢      │
  │ R14│ Schacter & Addis 2007 — Constructive Simulation│ §9     │ 🟢      │
  │ R15│ Buckner & Carroll 2007 — Self-Projection       │ §9      │ 🟢      │
  │ R16│ Mitchell 2006 — mPFC Self/Other Gradient       │ §7, §9  │ 🟢      │
  │ R17│ Tamir & Mitchell 2010 — Ventral/Dorsal mPFC    │ §9      │ 🟢      │
  │ R18│ Bird & Cook 2013 — Alexithymia                 │ §9      │ 🟢      │
  │ R19│ Lombardo 2010 — Shared Circuits Self/Other     │ §9      │ 🟢      │
  │ R20│ Lally et al. 2010 — Habit Formation            │ §3      │ 🟢      │
  │ R21│ Chase & Simon 1973 — Expertise Chunking        │ §3, §10 │ 🟢      │
  │ R22│ Anderson & Green 2001 — Think/No-Think         │ §4      │ 🟢      │
  │ R23│ Curtis & D'Esposito 2003 — PFC Sustained Firing│ §4      │ 🟢      │
  │ R24│ Inzlicht & Schmeichel 2012 — Motivational Acct │ §5      │ 🟢      │
  └────┴──────────────────────────────────────────────┴─────────┴──────────┘
```

---

**END OF FILE — PFC-Label v1.0 (24 citations, 17 sections)**

> *PFC-Label Convention v1.0 — Vocabulary Reference.*
> *Companion to Body-Feedback-Label v2.0.*
>
> *§2 Roles: Observer / Lawyer / Director / Universal Resource / Quality Controller.*
> *§3 Spectrum: Compiled ←→ Fresh (TRỤC THẬT, not Logic/Feeling).*
> *§4 Operations: HOLD (amplify) / SUPPRESS (block) — 4 tổ hợp, 3 outcomes.*
> *§5 Cost: ① PFC draft + ② Suppress + ③ Uncertainty. Budget = finite, shared.*
> *§6 Quality: Genuine / Schema / Threat — compile-time lock.*
> *§7-§8 Regions + Hardware: dlPFC, vlPFC, vmPFC, mPFC, COMT, DRD4.*
> *§9 Simulation Engine: 1 engine, 3 components, 3 axes.*
> *§10-§11 Cognitive ops + Failure modes.*
> *§12 Observer vs Mechanism: Logic/Feeling ≠ Compiled/Fresh.*
> *§13 Deprecated: "PFC-Fresh", "draft" standalone, "willpower", "self-control" unspecified.*
> *§14 Rules: đúng level, đúng context, đừng đổ lỗi — giải thích mechanism.*
