---
title: "Quote Analysis — Work: Move Fast and Break Things"
version: 1.0
created: 2026-05-23
status: v1.0 COMPLETE
scope: |
  QUOTE ANALYSIS: "Move fast and break things.
  The idea is that if you never break anything, you're probably not moving fast enough."
  — Mark Zuckerberg, IPO Letter (Feb 1, 2012). Internal motto since ~2006.
  Changed to "Move fast with stable infrastructure" — F8 conference, April 30, 2014.
  Framework giải mã: TẠI SAO câu này đúng (mechanism), KHI NÀO nó sai,
  TẠI SAO Zuckerberg TỰ thay đổi nó, CÁCH calibrate.
purpose: |
  File trước: Goal+Why (external→team), Hungry+Foolish (internal→self).
  File NÀY: engineering CULTURE — organizational level.
  Unique: quote có LIFECYCLE (sinh→thịnh→tự thay đổi).
  Framework giải thích cả lifecycle — TẠI SAO chính người tạo ra motto lại đổi nó.
  = Stress test cho framework: predict transition, not just explain quote.
position: |
  Research/Quote-Analysis/ — cùng folder Work-Goal-And-Why.md, Work-Stay-Hungry-Stay-Foolish.md.
dependencies:
  Mechanism:
    - PFC-Operations.md v1.0 — §2 Hold+Suppress, §5 Compiled Quality, §9 PFC Budget
    - Background-Pattern.md v2.0 — §6 Triple Bias, §2 Depth×Density
    - Cortisol-Baseline.md v2.1 — §3.3 Direction-At-Compile, §3.4 7 Modes, §7 Novelty vs Threat
    - Drive.md v1.2 — §2 PFC 6 Modes (Drive-PFC-Spinning, Drive-PFC-Resolve)
  Dynamics:
    - Novelty.md v1.2 — §1 VTA+prediction-delta, §1.4 Combinatorial space
    - Gap-Direction.md v2.0 — §3 "Chưa biết = không có gap", §1.4 By-product match
    - Body-Feedback-Mechanism.md v2.0 — §3.2 Chunk-Miss, §3.3 Chunk-Gap
    - Boredom.md v2.0 — §0 Dissonance + Imagine-Final mờ
  Entity:
    - Entity-Access.md v1.2 — Gradient Mức 0-5, trust dynamics
    - Entity-Compiled.md v1.0 — Hub-and-Spoke, formation
  Other:
    - Self-Created-Threat.md v1.0 — §1 PFC-to-Body trust-compile
    - Gap-Body-Need.md v1.0 — §9 ENGINE/ROAD/VEHICLE
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Quote Analysis — Work: Move Fast and Break Things

> **"Move fast and break things.**
> **The idea is that if you never break anything,**
> **you're probably not moving fast enough."**
>
> — Mark Zuckerberg, IPO Letter cho nhà đầu tư (Feb 1, 2012).
> Mục "The Hacker Way" — 1 trong 5 core values.
> Internal motto từ ~2006, treo poster tại mọi văn phòng Facebook.
>
> Thay đổi thành: **"Move fast with stable infrastructure"**
> — F8 Developer Conference, April 30, 2014.
> Lý do Zuckerberg nêu: tốn thời gian fix bugs hơn build features mới.
>
> 🟢 Verified source: Zuckerberg IPO Letter (CNN Money, Feb 2012),
> F8 2014 Keynote (TechCrunch). Jonathan Taplin (2017) phê phán.

---

## Mục lục

- §0 — TẠI SAO PHÂN TÍCH QUOTE NÀY
- §1 — GIẢI MÃ: "MOVE FAST"
- §2 — GIẢI MÃ: "BREAK THINGS"
- §3 — KẾT HỢP: FAST × BREAK TRONG GIAI ĐOẠN ĐẦU
- §4 — LIFECYCLE: TẠI SAO ZUCKERBERG TỰ THAY ĐỔI
- §5 — FAILURE MODES: KHI NÀO QUOTE SAI HOẶC NGUY HIỂM
- §6 — CALIBRATION: CÁCH APPLY KHÔNG CỨNG NHẮC
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §0 — TẠI SAO PHÂN TÍCH QUOTE NÀY

```
QUOTE NÀY ĐẶC BIỆT SO VỚI 2 FILE TRƯỚC:

  ┌────────────────────┬──────────────┬──────────────────┬──────────────────┐
  │                    │ Goal + Why   │ Hungry + Foolish │ Fast + Break     │
  ├────────────────────┼──────────────┼──────────────────┼──────────────────┤
  │ Level              │ Team         │ Cá nhân          │ Tổ chức         │
  │ Hướng              │ Leader→team  │ Self→self        │ Culture→system   │
  │ Source             │ Floating     │ Verified (2005)  │ Verified (2012)  │
  │ Context            │ Management   │ Đối mặt cái chết│ IPO engineering  │
  │ Unique             │ Hidden step  │ PFC double cost  │ Có LIFECYCLE     │
  │ Framework focus    │ Anchor-Schema│ Gap Dynamics     │ Compiled Base    │
  │                    │ Valence chain│ Triple Bias      │ Lifecycle        │
  └────────────────────┴──────────────┴──────────────────┴──────────────────┘

  UNIQUE: Quote này có LIFECYCLE hoàn chỉnh:
    2006 → sinh (internal motto)
    2012 → thịnh (IPO letter, made public)
    2014 → TỰ THAY ĐỔI ("stable infrastructure")
    2017+ → phê phán rộng rãi (cautionary tale)

  Framework cần giải thích KHÔNG CHỈ tại sao quote đúng,
  mà TẠI SAO CHÍNH NGƯỜI TẠO RA NÓ đã thay đổi nó.
  = Nếu framework predict được transition → evidence MẠNH.
```

---

## §1 — GIẢI MÃ: "MOVE FAST"

### §1.1 — Move Fast = Giảm Evaluation Cycles của PFC

```
⭐ MAPPING CỐT LÕI:

  PFC-Operations.md §2.2:
    SUPPRESS = PFC actively block compiled pattern → cost ②.

  "Move fast" = GIẢM số evaluation cycles PFC chạy trước khi hành động:
    → "Đừng review 5 lần — ship rồi fix"
    → = Suppress caution checks → act sooner → more iterations/time.

  NHƯNG framework phân biệt 2 CONTEXT KHÁC CĂN BẢN:

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  CONTEXT A — EARLY STAGE (chưa có compiled caution):           │
  │    Caution patterns CHƯA TỒN TẠI.                             │
  │    "Chưa biết = không có gap" (Gap-Direction §3):              │
  │    → Bạn KHÔNG THỂ suppress cái chưa compile.                 │
  │    → "Move fast" = TRẠNG THÁI TỰ NHIÊN (cost ≈ 0).           │
  │    → Không cần effort → tự động nhanh.                        │
  │                                                                │
  │  CONTEXT B — MATURE STAGE (có compiled caution):               │
  │    Caution = genuine-compiled từ KINH NGHIỆM THẬT.            │
  │    → "Move fast" = PFC suppress genuine signal → cost ②.      │
  │    → Mất INFORMATION (caution = signal, §4.2).                │
  │    → Tốn PFC budget → outcomes có thể WORSE.                  │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘

  Quote KHÔNG phân biệt 2 context.
  Framework CHỈ RA: "move fast" ở Context A ≠ Context B.

  🟢 PFC suppress cost: Anderson & Green 2001
  🟡 Context A vs B distinction: framework synthesis
```

### §1.2 — Speed = Nhiều prediction-delta/Thời Gian = Nhanh Hơn Học

```
⭐ TẠI SAO "NHANH" TỐT HƠN "CHẬM" CHO LEARNING:

  Novelty.md §1: VTA detect prediction-delta trong chunk network.
    → Mỗi delta = 1 learning event (chunks update).
    → Nhanh hơn → nhiều actions → nhiều deltas → nhiều learning events.

  Gap-Direction.md §1: Reward = direction match quality.
    → Mỗi action test 1 gap direction → confirm hoặc update.
    → Nhanh hơn → test nhiều directions → tìm đúng direction SỚM hơn.

  "Move fast" works VÌ:
    Speed = TĂNG tần suất domain feedback.
    Domain feedback = arbiter DUY NHẤT (Drive.md §0).
    → Nhiều feedback/time = calibrate CHÍNH XÁC hơn/time.

  ANALOGY:
    Lái xe mới: lái 10km/ngày → 1 năm mới quen.
    Lái 100km/ngày → 1 tháng đã quen.
    Cùng learning mechanism. KHÁC tần suất feedback.

  🟢 Prediction error = learning signal: Schultz 1997
  🟡 Speed → feedback frequency → calibration: framework synthesis
```

### §1.3 — Fast + Direction ≠ Fast - Direction

```
⭐ DRIVE §2 — PFC 6 MODES:

  Drive-PFC-Spinning: PFC 30-50% active nhưng KHÔNG hiệu quả.
    = "Bận nhưng không biết đang làm gì."
    = Thiếu matching chunks → PFC scan nhưng không lock target.
    = FAST nhưng NOWHERE.

  Drive-PFC-Resolve: PFC 20-40% nhưng RẤT hiệu quả.
    = Đủ chunks → gap direction RÕ → action MATCH → reward fire.
    = FAST VÀ PRODUCTIVE.

  "Move fast and break things" CHỈ work ở Drive-PFC-Resolve:
    → Có hướng (gap direction rõ) → speed = tăng feedback → learn fast.
    → Không có hướng → speed = burn PFC budget → no learning.

  Facebook 2006: Zuckerberg CÓ hướng rõ ("connect people").
    → Drive-PFC-Resolve: fast + direction = productive.
  Startup mới KHÔNG có hướng: "move fast" = Drive-PFC-Spinning.
    → Fast nhưng nowhere = waste.

  🟡 Drive-PFC-Spinning/Resolve mapping: framework synthesis (Drive.md §2)
```

---

## §2 — GIẢI MÃ: "BREAK THINGS"

### §2.1 — Break = Prediction-Delta = Learning Signal

```
⭐ FRAMEWORK REFRAME: "BREAK" KHÔNG PHẢI CHI PHÍ — LÀ CƠ CHẾ:

  Novelty.md §1.1: VTA fire khi detect prediction-delta.
    → Delta > 0 (positive): pattern mới → approach
    → Delta < 0 (negative): pattern tệ hơn expected → dissonance

  "Break things" = TẠO negative prediction-delta:
    → Expected: code works → Actual: code breaks → delta < 0
    → Body-Feedback-Mechanism §3.2: Chunk-Miss = negative delta
    → Body signal "bứt rứt" → PFC attend → update chunks

  FRAMEWORK INSIGHT:
    Breaking = FORCED chunk network update.
    NOT breaking = prediction CONFIRMED = delta = 0 = NO UPDATE.
    → "If you never break anything" = zero delta = zero learning.
    → Zuckerberg's logic ĐÚNG ở level mechanism.

  NHƯNG:
    Statement "probably not moving fast enough" ASSUMES:
    ① Learning = primary goal (true for early stage)
    ② Cost of break < value of learning (true when compiled base LOW)
    Cả 2 assumptions THAY ĐỔI khi system matures (§4).

  🟢 VTA prediction-delta: Schultz 1997
  🟢 Error-driven learning: Rescorla & Wagner 1972
  🟡 "Break = forced update" framing: framework synthesis
```

### §2.2 — Cùng Break, Khác Direction Tag → Khác Suốt Đời

```
⭐ CORTISOL-BASELINE §3.3 (Direction-At-Compile) — COMPILE-TIME VARIABLE:

  Chunks compile tại MOMENT cortisol fires.
  Body state direction tại moment đó = LOCK IN vào chunk.
  = Compile-time variable — sau khi compile, tag PERMANENT.

  CÙNG sự kiện "server sập":

  Founder A (approach body state):
    → Cortisol moderate + curiosity + opioid preview.
    → Chunk [server sập] compile với APPROACH TAG.
    → 10 năm sau: "bugs are fun, let's fix" → genuine-compiled.

  Employee B (threat body state):
    → Cortisol moderate + NE + fear ("bị đuổi?").
    → Chunk [server sập] compile với AVOIDANCE TAG.
    → 10 năm sau: "sợ deploy, check 10 lần" → threat-compiled.

  → CÙNG event. CÙNG cortisol level. KHÁC direction.
  → = "Move fast and break things" tạo approach tag cho founder
      nhưng có thể tạo avoidance tag cho team members.

  ⭐ INSIGHT:
    Culture "move fast" CHỈ healthy khi body state = novelty direction.
    Nếu team ĐÃ mệt/sợ → mỗi "break" compile AVOIDANCE tag.
    → Functional nhưng GHÉT work → "giỏi nhưng ghét."

  🟢 Cortisol direction tag: Chunk.md §2.4 Direction-At-Compile
  🟡 Direction tag per person within same event: framework synthesis
```

### §2.3 — Break × Compile Depth: Early Cheap, Late Expensive

```
⭐ FRAMEWORK PREDICT: CHI PHÍ BREAK = f(COMPILED BASE):

  Background-Pattern §2.1 — 2D Model:
    Compile Depth = mỗi chunk wired MẠNH cỡ nào
    Link Density = pattern linked với bao nhiêu chunks khác

  EARLY STAGE (compiled base LOW):
    → Ít chunks compiled → ít links → ít dependencies
    → Break 1 feature → ảnh hưởng FEW patterns
    → Cost ≈ low → rollback easy → learn fast

  MATURE STAGE (compiled base HIGH):
    → Nhiều chunks compiled → nhiều links → nhiều dependencies
    → Break 1 feature → cascade qua ENTIRE network
    → Cost ≈ high → rollback HARD → damage > learning

  VÍ DỤ:
    Facebook 2006: 1M users, small codebase.
      → Break login flow → 1M users confused → fix in hours.
      → Learning value > disruption cost.

    Facebook 2014: 1.2B users, massive infrastructure.
      → Break login flow → 1.2B users disrupted → support tickets cascade.
      → Disruption cost >> learning value.

  → Chi phí break TĂNG exponentially với compiled base.
  → = TẠI SAO quote đúng EARLY và sai LATE (§4).

  🟡 Cost = f(compiled base): framework synthesis
```

---

## §3 — KẾT HỢP: FAST × BREAK TRONG GIAI ĐOẠN ĐẦU

```
⭐⭐ TẠI SAO "MOVE FAST AND BREAK THINGS" TỐI ƯU CHO EARLY STAGE:

  5 ĐIỀU KIỆN ĐỒNG THỜI (chỉ CÓ ở early stage):

  ① LOW COMPILED BASE — ÍT THỨ ĐỂ BREAK:
     "Chưa biết = không có gap" (Gap-Direction §3).
     Caution gaps CHƯA TỒN TẠI → impossible to suppress.
     → "Move fast" = trạng thái TỰ NHIÊN, cost ≈ 0.

  ② CHEAP ERRORS — HỌC NHANH:
     Ít compiled value → mỗi break phá ÍT → rollback dễ.
     → prediction-delta per break = HIGH learning, LOW cost.
     → = MAXIMUM learning rate per unit of disruption.

  ③ NO BACKGROUND PATTERN — KHÔNG CÓ TRIPLE BIAS:
     Background-Pattern §6: Triple Bias (Retrieval + Template + Interpretation)
     CHỈ fire khi có compiled expert patterns.
     → Early: CHƯA CÓ → road OPEN → creativity possible.
     → = "Foolish" miễn phí (PFC-Operations §2.3: không cần suppress).

  ④ PFC BUDGET FULL — TOÀN BỘ CHO LEARNING:
     Không suppress caution → cost ② = 0.
     → PFC budget TOÀN BỘ available cho Hold (learning).
     → = Engine running + road open + fuel full.

  ⑤ COMPILABLE ARCHITECTURE SERVED — NOVELTY DRIVE SATISFIED:
     Boredom §0: general-purpose system CẦN fresh input.
     "Move fast and break things" = abundant prediction-deltas.
     → VTA fire liên tục → architecture B happy → drive sustained.

  → = ENGINE/ROAD/VEHICLE (Gap-Body-Need §9):
    ENGINE: novelty drive (VTA active, approach tag).
    ROAD: open (no Background-Pattern blocking).
    VEHICLE: PFC budget full (no suppress cost).
    = Tất cả 3 yếu tố OPTIMAL cùng lúc → maximum exploration.

  Facebook 2006-2012 = example:
    Small team, few users, fresh domain, Mark had CLEAR direction.
    "Move fast and break things" KHÔNG phải slogan — là REALITY.
    Mỗi break = learning → product-market fit → growth.
```

---

## §4 — LIFECYCLE: TẠI SAO ZUCKERBERG TỰ THAY ĐỔI

### §4.1 — Compiled Base Tăng → Chi Phí Break Tăng

```
⭐ FACEBOOK 2014 — 5 ĐIỀU KIỆN §3 KHÔNG CÒN:

  ① Compiled base = MASSIVE (1.2B users, billions of data points).
  ② Errors = EXPENSIVE (mỗi bug → millions affected).
  ③ Background-Pattern = STRONG (team có expert patterns, biases).
  ④ PFC budget = STRETCHED (suppress caution cost ② tăng dần).
  ⑤ Compilable Architecture = SERVED bằng cách KHÁC (mature product = stable).

  Zuckerberg tại F8 2014:
    "We were spending more time fixing bugs than building new features."
    = Prediction: break cost > learning value = FLIP POINT.
    = Framework: compiled base đã cross threshold →
      mỗi break phá giá trị tích lũy > giá trị learning thu được.
```

### §4.2 — Compiled Caution = GENUINE Signal

```
⭐⭐ KEY INSIGHT:

  PFC-Operations §5 — 3 loại Compiled Quality:
    Genuine-compiled: body THẬT SỰ trải nghiệm → multi-sensory, approach tag.
    Schema-compiled: PFC logic "biết nên" → single-channel, flat.
    Threat-compiled: bị ép → avoidance tag, functional nhưng ghét.

  Senior engineer 2014 (8 năm experience):
    → Nói "đừng push Friday" = GENUINE-COMPILED từ real incidents.
    → Caution này là INFORMATION: body đã trải nghiệm lỗi → compiled approach.
    → Direction tag = APPROACH toward quality (không phải avoidance từ sợ).
    → = Signal: "tôi BIẾT cái này sẽ break VÌ ĐÃ THẤY."

  "Move fast" suppress caution này = suppress GENUINE information:
    → Mất signal body đã compile qua years.
    → Outcomes WORSE (break things body ĐÃ BIẾT sẽ break).
    → = Suppress expertise = đi ngược framework prediction.

  PHÂN BIỆT:
    ┌────────────────────┬──────────────────────┬──────────────────────┐
    │                    │ SUPPRESS NÊN         │ SUPPRESS KHÔNG NÊN  │
    ├────────────────────┼──────────────────────┼──────────────────────┤
    │ Loại caution       │ Schema/Threat        │ Genuine              │
    │ Source             │ "Nghe nói nguy hiểm" │ "Đã thấy nó break"  │
    │ Direction tag      │ Avoidance (sợ)       │ Approach (hiểu)      │
    │ Information value  │ Low (secondhand)     │ High (firsthand)     │
    │ Suppress outcome   │ Try → learn          │ Lose signal → worse  │
    └────────────────────┴──────────────────────┴──────────────────────┘

  🟡 Genuine caution as signal vs obstacle: framework synthesis
```

### §4.3 — Entity-Access Dependencies: Phá Patterns Người Khác

```
⭐ ENTITY-ACCESS §1.2 — USERS LÀ ENTITIES:

  Mỗi user build entity-access relationship với Facebook:
    → Compiled routines: login → feed → post → check notifications.
    → Entity-access gradient: Mức 2-4 (daily habit, identity connection).
    → Body BASELINE ĐÃ COMPILE quy trình này.

  "Break things" khi users ở Mức 3-4:
    → Thay đổi interface → compiled routines BỊ PHÁ.
    → Body-Feedback-Mechanism §3.2: Chunk-Miss → dissonance.
    → Gap-Direction §1.4: output "new interface" CONFLICT direction "stable routine."
    → = ANTI-MATCH (active friction, không chỉ no-match).
    → Protect fires: "cái CỦA TÔI bị phá" → loss aversion ~2×.

  CÒN developers (API consumers):
    → Compiled code DEPEND on stable API.
    → "Break" API = break THEIR compiled patterns.
    → Trust violation → entity-compiled damage → churn.

  → "Break things" ở early stage: break YOUR prototype → you learn.
  → "Break things" ở mature stage: break OTHERS' compiled patterns → trust violation.

  🟢 Loss aversion: Kahneman & Tversky 1979
  🟡 Entity-access disruption at scale: framework synthesis
```

### §4.4 — "Move Fast WITH Stable Infrastructure" = Framework-Aligned

```
⭐ TRANSITION = FRAMEWORK PREDICTION:

  "Move fast with stable infrastructure" (Zuckerberg 2014):
    → Speed THROUGH compiled quality, not through destruction.
    → Build stable foundation → iterate WITHIN → still fast, less breaking.
    → = Compiled caution INTEGRATED as signal, not suppressed.

  Framework mapping:
    → "Stable infrastructure" = compiled base ĐƯỢC TÔN TRỌNG.
    → "Move fast" = speed vẫn có, nhưng TRÊN NỀN ổn định.
    → = PFC Hold new patterns (cost ①) TRÊN compiled foundation.
    → KHÔNG CẦN Suppress compiled caution (cost ② = 0).
    → = Quay lại trạng thái tối ưu: Hold only (PFC-Operations §3 Tổ hợp ①).

  ⭐ FRAMEWORK PREDICT CHÍNH XÁC:
    Low compiled → break cheap → learn fast → motto đúng.
    Compiled TĂNG → break expensive → motto tốn hơn có ích.
    Compiled HIGH → break phá giá trị > tạo learning → motto SAI.
    → Transition = INEVITABLE cho bất kỳ system nào tích lũy compiled value.

  Zuckerberg KHÔNG CẦN biết framework để đi tới kết luận này.
  Domain feedback (years of bugs, user complaints) = arbiter thật.
  Framework chỉ GIẢI THÍCH tại sao domain feedback DẪN TỚI kết luận đó.

  🟡 Lifecycle prediction: framework synthesis (post-hoc, but precise match)
```

---

## §5 — FAILURE MODES: KHI NÀO QUOTE SAI HOẶC NGUY HIỂM

### §5.1 — 5 Failure Modes

```
⭐ FAILURE 1 — SPEED AS IDENTITY (Background-Pattern Lock-In):

  "Move fast" lặp lại đủ lâu → compile vào Background-Pattern.
  → Triple Bias fires (Background-Pattern §6):
    Retrieval: "chúng tôi luôn ship nhanh" fire trước evaluation.
    Template: "tôi là người nhanh" → project onto everyone.
    Interpretation: "delay = xấu" → miss genuine caution signals.
  → PFC INVISIBLE (Background-Pattern §5): person KHÔNG BIẾT mình biased.
  → "Sao anh bảo tôi chậm lại? Tốc độ là giá trị của chúng tôi!"
  → = Schema-compiled speed: identity, not tool. CAN'T slow down.


⭐ FAILURE 2 — BREAK OTHERS' THINGS (Entity-Access Damage):

  Early: break prototype → bạn learn.
  Mature: break production → USERS chịu consequences.
  → Entity-access disruption at scale = trust violation.
  → Facebook privacy scandals = "move fast and break [users' privacy]."
  → Users' compiled trust (entity-access Mức 3-4) = BROKEN.
  → Protect mechanism fires → backlash → regulation.


⭐ FAILURE 3 — FAST WITHOUT DIRECTION (Drive-PFC-Spinning):

  Speed + no gap direction = Drive-PFC-Spinning.
  PFC 30-50% active nhưng KHÔNG hiệu quả.
  = "Chạy nhanh nhưng không biết đi đâu."
  → PFC budget burn → fatigue → capacity GIẢM.
  → WORSE than slow-with-direction (Drive-PFC-Resolve).
  → Ví dụ: startup pivot liên tục, ship features nobody wants.


⭐ FAILURE 4 — SKIP DOMAIN FEEDBACK (Compile Wrong Patterns Deeply):

  Fast iteration WITHOUT checking results:
  → Compile wrong patterns SÂUNHANH (Cortisol §3.5).
  → Genuine-compiled... nhưng sai hướng.
  → "Chúng tôi ship 10 features/tuần" — nhưng sai 8.
  → Schema-compiled speed: fast at producing WRONG things.
  → Drive.md §0: "Domain feedback = arbiter DUY NHẤT."
  → Speed without feedback = velocity without direction.


⭐ FAILURE 5 — CHRONIC CRISIS MODE (Cortisol → PFC Damage):

  "Move fast and break things" = perpetual crisis:
  → Break → fix → break → fix → cortisol CHRONIC.
  → Cortisol-Baseline §9: PFC damage timeline:
    8 weeks chronic → hippocampus dendrite retraction.
    Sustained → PFC structural damage (McEwen 2007).
  → PFC damage → LESS capacity for fresh processing.
  → = Chronic breaking → LESS ABILITY to move fast later.
  → = Self-defeating loop: fast now → damage → slow later.

  🟢 Chronic cortisol → PFC damage: McEwen 2007
```

---

## §6 — CALIBRATION: CÁCH APPLY KHÔNG CỨNG NHẮC

```
⭐⭐ 6 NGUYÊN TẮC CALIBRATION:

  ① DOMAIN MATURITY QUYẾT ĐỊNH CHI PHÍ BREAK:
    Startup mới: domain CHƯA BIẾT → compiled base ≈ 0 → break cheap.
    Product mature: domain ĐÃ BIẾT → compiled base HIGH → break expensive.
    Calibrate: cost of break = f(compiled base depth × density).
    Trước khi "move fast" — hỏi: "compiled base ở mức nào?"

  ② BREAK CỦA MÌNH, KHÔNG BREAK CỦA NGƯỜI KHÁC:
    Break prototype = bạn chịu → bạn learn.
    Break production = users chịu → bạn learn, họ bị hại.
    Entity-access gradient determines blast radius.
    Calibrate: "ai chịu hậu quả khi tôi break?"

  ③ SPEED CẦN FEEDBACK LOOP:
    Speed = velocity + direction + FEEDBACK.
    Iterate → check domain response → adjust → iterate.
    Speed WITHOUT feedback = nhanh mà sai hướng.
    Calibrate: "tôi có CHECK kết quả mỗi iteration không?"
    Domain feedback = arbiter DUY NHẤT (Drive.md §0).

  ④ COMPILED CAUTION GENUINE = SIGNAL, KHÔNG SUPPRESS:
    Caution từ genuine experience = approach-tagged information.
    Caution từ schema/threat = có thể cần examine.
    Test: "Caution này đến từ ĐÃ TRẢI NGHIỆM hay chỉ NGHE NÓI?"
    Genuine → respect. Schema/Threat → examine.
    Calibrate: KHÔNG suppress mọi caution — phân biệt source.

  ⑤ OSCILLATE: NHANH → ỔN ĐỊNH → NHANH LẠI:
    Permanent fast = PFC budget depleted → burnout.
    Permanent stable = no prediction-delta → stagnation.
    Cần OSCILLATE: explore (fast, fresh Fresh) → compile (stable, Compiled) → explore.
    = "Sprint → consolidate → sprint" (Agile ĐÚNG ở level mechanism).
    Calibrate: "đã compile xong chưa trước khi explore tiếp?"

  ⑥ PER-PERSON CALIBRATION (Novelty §5 — DRD4):
    DRD4 7R+: threshold CAO → deep focus → "fast" = deep iteration.
    DRD4 4R: threshold THẤP → broad awareness → "fast" = rapid pivots.
    Mỗi người "move fast" KHÁC NHAU.
    KHÔNG CÓ 1 cách "move fast and break things" universal.
    Calibrate: biết hardware preference → calibrate speed type.
```

---

## §7 — HONEST ASSESSMENT

```
⭐ FRAMEWORK GIẢI THÍCH ĐƯỢC GÌ:

  ✅ TẠI SAO "move fast" works (prediction-delta per time → learning rate)
  ✅ TẠI SAO "break things" works (forced chunk update → learning signal)
  ✅ TẠI SAO đúng ở EARLY stage (5 điều kiện đồng thời)
  ✅ TẠI SAO sai ở MATURE stage (compiled base cost > learning value)
  ✅ TẠI SAO Zuckerberg TỰ thay đổi (lifecycle = framework prediction)
  ✅ TẠI SAO cùng break, khác direction tag → khác suốt đời
  ✅ TẠI SAO "break others' things" nguy hiểm (entity-access anti-match)
  ✅ TẠI SAO "fast without direction" fail (Drive-PFC-Spinning)
  ✅ CÁCH calibrate (6 principles)

  ⚠️ CAVEATS:

  🟡 "Chi phí break = f(compiled base)" = framework synthesis.
     Consistent với organizational learning literature
     nhưng exact function chưa formalized.

  🟡 "Compiled caution = signal vs obstacle" = framework distinction.
     Consistent với expert intuition research (Klein 1998)
     nhưng genuine/schema/threat 3-way split trong CAUTION context
     chưa có specific study.

  🟡 "Zuckerberg's transition = framework prediction" = post-hoc.
     Framework GIẢI THÍCH WHY transition happened.
     NHƯNG: did not PREDICT it before it happened.
     = Post-hoc explanation, not pre-hoc prediction.
     Still valuable: explain > describe.

  🟡 "Drive-PFC-Spinning vs Drive-PFC-Resolve" = framework categories.
     Consistent với expertise research (Ericsson 1993)
     nhưng discrete modes vs continuous spectrum = simplification.

  🟡 "Direction tag in organizational context" = framework extension.
     Individual-level direction tag = established.
     Team-level direction tag (culture → individual compile) = plausible extension.

  🔴 "Optimal speed/caution ratio per domain maturity" = hypothesis.
     Framework says "ratio should shift" but CANNOT specify exact ratio.
     Domain feedback = only arbiter → no formula possible.

  🔴 "Breaking creates permanent direction tag in all team members" = hypothesis.
     Individual direction tag = established neuroscience.
     Organizational event → individual compile uniformly = untested assumption.
     Likely: DIFFERENT people compile DIFFERENT tags from SAME event.


  🟢 ESTABLISHED SUPPORT:
     Prediction-delta learning (Schultz 1997)
     Error-driven learning (Rescorla & Wagner 1972)
     PFC suppress cost (Anderson & Green 2001, Aron 2007)
     Chronic cortisol → PFC damage (McEwen 2007)
     Loss aversion (Kahneman & Tversky 1979)
     Expert intuition (Klein 1998, Chase & Simon 1973)
     PFC budget / cognitive resources (Baumeister 2007, Inzlicht 2014)
     Ego depletion debate (Hagger et al. 2016 → framework neutral)
     Confirmation bias (Nickerson 1998)
     Ironic process / rebound (Wegner 1987)


  FRAMEWORK vs RE-DESCRIPTION:

  Quote: "Move fast and break things" (WHAT to do).
  Framework: Compiled Base Cost + Direction Tag + Entity-Access + Lifecycle
    = WHY it works + WHEN it stops working + WHY Zuckerberg changed it
    + HOW to calibrate + 5 failure modes.
  = THÊM predictive power:
    ① PREDICT lifecycle (motto PHẢI thay đổi khi compiled base tăng)
    ② PREDICT failure modes (5 specific, with mechanisms)
    ③ EXPLAIN direction tag difference (cùng event, khác team member)
    ④ ADD entity-access dimension (others' patterns)
    ⑤ DISTINGUISH caution types (genuine signal vs schema fear)
  = Nếu CHỈ re-describe → không predict lifecycle.
  = Predict lifecycle = evidence cho explanation, không chỉ description.
```

---

## §8 — CROSS-REFERENCES

```
MECHANISM:
  PFC-Operations.md v1.0 — §2 Hold+Suppress, §3 4 Tổ hợp (①=optimal),
    §5 Compiled Quality (genuine/schema/threat), §9 PFC Budget
  Background-Pattern.md v2.0 — §2 Depth×Density, §5 PFC invisible,
    §6 Triple Bias (Retrieval+Template+Interpretation)
  Cortisol-Baseline.md v2.1 — §3.3 Direction-At-Compile, §3.5 Novelty compile fast,
    §9 PFC damage timeline
  Drive.md v1.2 — §0 Domain=Arbiter, §1 Vô thức=Engine,
    §2 PFC 6 Modes (Drive-PFC-Spinning, Drive-PFC-Resolve)

DYNAMICS:
  Novelty.md v1.2 — §1 VTA+prediction-delta, §1.1 VTA mechanism,
    §1.4 Combinatorial space
  Gap-Direction.md v2.0 — §1 Definition (direction = f(surrounding chunks)),
    §1.4 By-product match/anti-match, §3 "Chưa biết = không có gap"
  Body-Feedback-Mechanism.md v2.0 — §3.2 Chunk-Miss (negative delta),
    §3.3 Chunk-Gap
  Boredom.md v2.0 — §0 Compilable Architecture cần input, Drive-PFC-Spinning territory
  Gap-Body-Need.md v1.0 — §9 ENGINE/ROAD/VEHICLE

ENTITY:
  Entity-Access.md v1.2 — Gradient Mức 0-5, entity-access disruption
  Entity-Compiled.md v1.0 — Formation, trust build (40-200h)

OTHER QUOTE ANALYSES:
  Work-Goal-And-Why.md v1.0 — External motivation (leader → team)
  Work-Stay-Hungry-Stay-Foolish.md v1.0 — Internal orientation (self → self)

RELATED RESEARCH:
  Schultz, W. (1997). Dopamine prediction-delta.
  Rescorla, R. A., & Wagner, A. R. (1972). Error-driven learning.
  Anderson, M. C., & Green, C. (2001). Suppressing unwanted memories (PFC cost).
  Aron, A. R. (2007). Inhibitory control (rIFG).
  McEwen, B. S. (2007). Chronic stress → PFC structural damage.
  Kahneman, D., & Tversky, A. (1979). Loss aversion (Prospect Theory).
  Klein, G. (1998). Expert intuition (Sources of Power).
  Chase, W. G., & Simon, H. A. (1973). Expert chunk patterns.
  Baumeister, R. F. (2007). Self-regulation resources.
  Inzlicht, M., & Schmeichel, B. J. (2012). Motivational shift account.
  Nickerson, R. S. (1998). Confirmation bias.
  Wegner, D. M. (1987). Ironic process theory.
  Ericsson, K. A. (1993). Deliberate practice.
```

---

*v1.0 — 2026-05-23*
*Framework v7.8 analysis. Verified source: Zuckerberg IPO Letter 2012, F8 2014.*
