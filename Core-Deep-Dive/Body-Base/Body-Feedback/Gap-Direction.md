---
title: Gap Direction — Body-Feedback Requires Directional Match
version: 2.0
created: 2026-04-27
rewritten: 2026-05-17 (v2.0 — FULL REWRITE: +By-product match connection, +2-Stream, +Compilable Architecture, +Compiled/Fresh note, +Inter-Body cross-refs, +Label v2.0 vocabulary)
previous: v1.1 → backup/Gap-Direction-v1.1-backup.md
status: v2.0 COMPLETE
scope: |
  CORE MECHANISM FILE: Gap trong chunk network có HƯỚNG CỤ THỂ.
  Gap direction = f(surrounding chunk network structure).
  Reward/dissonance KHÔNG chỉ phụ thuộc prediction error (Schultz 1997)
  mà còn phụ thuộc DIRECTION MATCH — stimulus phải khớp HƯỚNG cụ thể.
  "Chưa biết = không có gap" = foundational principle.
  Unified model: Tier 1-4 chunks cùng substrate, khác depth/origin.
  2-layer model: signal mechanism (Layer 1) × direction content (Layer 2).
  v2.0: Gap direction = WHY by-product match works (Inter-Body connection).
  v2.0: 2-Stream × gap direction. Compilable Architecture × gap direction.
  v2.0: Compiled/Fresh evaluation processing.
purpose: |
  Body-Feedback-Mechanism.md §3.3 define Chunk-Gap:
    "Structure predict C should exist → C chưa compile → HOLE"
  Nhưng §3.3 CHƯA formalize: C có HÌNH DẠNG CỤ THỂ.
  File này formalize:
  ① Gap direction = consequence tất yếu của "gap = hole in chunk network"
  ② "Chưa biết = không có gap" = genesis principle (khác H10 P2 diagnosis)
  ③ Reward = direction match quality (không chỉ "fill gap or not")
  ④ 2-layer model clarify tại sao Schultz 1997 "đúng nhưng chưa đủ"
  ⑤ Gap direction install, Background-Pattern constraint, implications
  ⑥ v2.0: Gap direction = THE MECHANISM underneath by-product match
     (Inter-Body-Mechanism.md §5.4 — B's output match A's gap DIRECTION)
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — ngang hàng Body-Feedback-Mechanism.md.
  Body-Feedback-Mechanism.md = WHAT gap is (chunk dynamics mechanism)
  Gap-Direction.md (FILE NÀY) = WHY gap has direction + evaluation implications
  03-Reward.md = WHEN reward fires (H10 preconditions + case analyses)
  BỔ SUNG nhau — KHÔNG THAY THẾ.
dependencies:
  - Body-Feedback-Mechanism.md v2.0 — §3.3 Chunk-Gap definition, Shift/Miss/Gap, §1 Body-Need aggregate
  - Body-Feedback.md v2.0 — H10 5 preconditions, dual-pull
  - Body-Feedback-Label.md v2.0 — vocabulary consistency, §2 Foundation terms
  - Inter-Body-Mechanism.md v1.0 — §2 Body-Need direction, §5 by-product match, §5.3 Full Chain
  - By-Product-Gap-Resonance.md v1.0 — §2 2-Stream Architecture, §1.5 by-product match
  - 03-Reward.md — Ô Tô Paradox C2.1-C2.5, Van Gogh gradient, H10 cases
  - Chunk.md v2.0 — chunk substrate, compile, activation dynamics
  - Background-Pattern.md v1.0 — Background-Pattern bias gap direction landscape
  - Novelty.md v1.0 — Chunk-Gap = novelty foundation
  - Schema.md v2.0 — observation parameter, §4 depth, §8 body baseline
  - Cortisol-Baseline.md v2.0 — amplifier, direction tag, novelty vs threat
  - Imagine-Final.md — preview mechanism, Gap→Miss transition
  - Connection.md v3.3 — giving reward, Self-Pattern-Modeling-mediated, altruism
  - Gratitude.md v1.0 — H10 applied to gifts, gap pre-requisite
  - Self-Pattern-Modeling v3.0 — Compiled/Fresh processing (Modeling-Stream mechanism)
  - Body-Base.md v3.1 — Compilable Architecture (3 foundations)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Gap Direction — Body-Feedback Requires Directional Match

> **Bố mua cho xe thời thượng nhất giới trẻ → intensely pleasant.**
> **Bố mua cho tên lửa (đắt hơn gấp ngàn lần) → confused.**
> **Bố mua cho xe cổ (đắt hơn, bố thích) → không thích.**
>
> **Cùng "bố mua cho." Cùng "đắt tiền." Cùng "xe."**
> **Nhưng reward CHỈ fire khi stimulus KHỚP HƯỚNG CỤ THỂ.**
>
> **E=mc² trình bày cho Einstein → intensely pleasant.**
> **E=mc² trình bày cho học sinh → "ồ, hay" nhưng không cảm gì.**
> **Cùng thông tin. Cùng "objective value." KHÁC reward hoàn toàn.**
>
> **Tại sao?**
>
> **Vì gap trong chunk network có HƯỚNG.**
> **Hướng = f(surrounding chunk network structure).**
> **Không có chunks xung quanh = không có bờ = không có hole = KHÔNG CÓ GAP.**
> **"Chưa biết = không có gap" = bạn KHÔNG THỂ thiếu thứ bạn không biết tồn tại.**
>
> **Prediction error (Schultz 1997) = cơ chế DETECT (có gì đó khác).**
> **Gap direction = NỘI DUNG predict (khác CÁI GÌ cụ thể).**
> **Cần CẢ HAI để giải thích tại sao reward là PERSONAL.**
>
> **v2.0: Gap direction = WHY by-product match works.**
> **B fill gap CỦA B → output → match A's gap DIRECTION → A reward.**
> **Direction mismatch = output vô dụng DÙ "tốt" theo objective measure.**
>
> **File này: Gap direction LÀ GÌ, TẠI SAO tất yếu,**
> **"Chưa biết = không có gap" hoạt động THẾ NÀO,**
> **TẠI SAO đây là chìa khóa hiểu reward mechanism,**
> **và v2.0: TẠI SAO đây là foundation cho inter-body by-product match.**

---

## Mục lục

- §0 — TẠI SAO CẦN FORMALIZE GAP DIRECTION
- §1 — DEFINITION
- §2 — PROOF: TẠI SAO GAP BUỘC PHẢI CÓ HƯỚNG
- §3 — "CHƯA BIẾT = KHÔNG CÓ GAP" (Foundational Principle)
- §4 — 4 PROPERTIES CỦA GAP DIRECTION
- §5 — UNIFIED DIRECTION MODEL (Tier 1-4)
- §6 — 2-LAYER MODEL: SIGNAL MECHANISM vs DIRECTION CONTENT
- §7 — GAP DIRECTION FORMATION
- §8 — GAP DIRECTION × EXTERNAL INSTALL
- §9 — GAP DIRECTION × BACKGROUND PATTERN
- §10 — ABSTRACT ACTIVITY × BODY-BASE
- §11 — EXAMPLES
- §12 — GAP DIRECTION × INTER-BODY: BY-PRODUCT MATCH + 2-STREAM (★ NEW v2.0)
- §13 — IMPLICATIONS
- §14 — OPEN QUESTIONS
- §15 — HONEST ASSESSMENT
- §16 — CROSS-REFERENCES

---

## §0 — TẠI SAO CẦN FORMALIZE GAP DIRECTION

### §0.1 — Framework hiện tại đã có gì

```
BODY-FEEDBACK-MECHANISM.MD §3.3 (Chunk-Gap):

  "Structure predict: nếu A và B đúng thì C phải tồn tại"
  "C CHƯA compile → HOLE trong network"
  "ACC detect inconsistency → body signal bứt rứt"
  
  → Definition ĐÃ ĐÚNG. Gap = hole where network predicts something.
  → §3.3 nói "C should exist" — nhưng CHƯA hỏi: C trông như thế nào?
  → CHƯA formalize: C có HÌNH DẠNG CỤ THỂ determined by A, B, và network


H10 5 PRECONDITIONS (Body-Feedback.md §6):

  P1: Schema pending (body-need gap open)
  P2: Chunks base adequate (đủ substrate decode)
  P3: prediction-delta threshold (biến động đủ lớn)
  P4: Goldilocks zone (40-70% match)
  P5: Chunk association tag (opioid vs cortisol)

  → P2 nói "chunks base inadequate → confused" — FAILURE MODE khi nhận stimulus
  → CHƯA nói: không có chunks = gap KHÔNG THỂ HÌNH THÀNH = desire chưa tồn tại
  → P4 nói "40-70% match" — NHƯNG match VỚI CÁI GÌ? 
    Với gap direction! (implicit, chưa explicit)


03-REWARD.MD §5.9 (Ô Tô Paradox):

  "Reward = personalized function F(object, person's chunks, pending, history)"
  "Reward is NOT intrinsic to object"

  → Kết luận ĐÚNG — nhưng CHƯA giải thích MECHANISM:
    Tại sao personalized? VÌ mỗi người có gap direction KHÁC.
```

### §0.2 — Cái gì THIẾU

```
⭐ FRAMEWORK HIỆN TẠI = ĐÚNG NHƯNG THIẾU 1 CHIỀU:

  ĐÃ CÓ (implicit):
    ✅ Gap = hole in network
    ✅ "Structure predict C" → C phải phù hợp A, B
    ✅ Reward = personalized
    ✅ Goldilocks zone (match range)

  THIẾU (chưa explicit):
    ❌ Gap có HÌNH DẠNG CỤ THỂ = f(surrounding chunk network)
    ❌ "Chưa biết = không có gap" = GENESIS principle (trước cả P1)
    ❌ Reward = DIRECTION MATCH quality (không chỉ "fill or not fill")
    ❌ Prediction error = signal, direction = content (2 layers phân biệt)
    ❌ Tất cả direction = chunk pattern direction (unified Tier 1-4)
    ❌ Gap direction có thể INSTALL từ bên ngoài (F3 for gaps)
    ❌ Background-Pattern CONSTRAIN gap direction landscape

  v2.0 — THIẾU THÊM 1 TẦNG (chưa có trong v1.0):
    ❌ Gap direction = WHY by-product match works (Inter-Body §5.4)
    ❌ B's output match A's gap DIRECTION → A reward
    ❌ Direction mismatch = ANTI-MATCH (not just no-match)
    ❌ 2-Stream connection: Hardware-Stream = hardware gap direction matched,
       Modeling-Stream = Self-Pattern-Modeling-mediated gap direction matched
    ❌ Compilable Architecture × gap direction: general-purpose reward =
       gap direction KHÔNG hardwired per-content → emerge from chunk network

  HẬU QUẢ CỦA THIẾU:
    → Khi nói "gap fill → reward" — thiếu giải thích 
      tại sao CÙNG gap mà fill KHÁC → reward KHÁC
    → Khi nói "reward = personalized" — thiếu MECHANISM underneath
    → Khi nói "P4 Goldilocks match" — thiếu specify match VỚI CÁI GÌ
    → Khi nói "by-product match" — thiếu giải thích TẠI SAO match/mismatch
    → = Framework mô tả ĐÚNG nhưng chưa GIẢI THÍCH tầng sâu nhất
```

### §0.3 — File này bổ sung gì

```
FILE NÀY:
  → KHÔNG sửa definitions hiện tại — chúng ĐÃ ĐÚNG
  → THÊM chiều mới: direction (content specificity)
  → FORMALIZE consequences tất yếu từ "gap = hole in network"
  → BRIDGE giữa: gap mechanism (§3.3) ↔ reward evaluation (H10) ↔ 
    personalized reward (03-Reward §5.9)
  → v2.0: BRIDGE giữa: gap direction ↔ by-product match ↔ 2-Stream
    (WHY inter-body reward works = output match gap DIRECTION)
  → = Missing explanatory layer giữa "chunks fire" và "reward fires"
```

---

## §1 — DEFINITION

### §1.1 — Gap Direction là gì

```
⭐ GAP DIRECTION = HÌNH DẠNG CỤ THỂ CỦA HOLE TRONG CHUNK NETWORK:

  Body-Feedback-Mechanism.md §3.3 define:
    Gap = hole in chunk network where structure predicts something missing

  Gap Direction = WHAT SPECIFICALLY is predicted missing:
    → Shape of the hole = constraints on what counts as valid fill
    → Determined by: surrounding chunks' content + links + density
    → Formal: Gap_Direction = f(surrounding_chunk_network_structure)

  VD:
    Network: [bạn bè có xe đẹp] + [đi chơi thoải mái] + [trông oai]
    → Predict: "nếu mình cũng có xe đẹp thời thượng → oai giống vậy"
    → Gap direction = "xe đẹp thời thượng giới trẻ"
    → KHÔNG phải "xe" chung chung
    → KHÔNG phải "phương tiện di chuyển"
    → KHÔNG phải "vật đắt tiền"
    → = Direction CỤ THỂ, phụ thuộc chunks CỤ THỂ xung quanh gap
```

### §1.2 — Phân biệt: Gap vs Gap Direction

```
⭐ GAP ≠ GAP DIRECTION:

  GAP (§3.3):
    → Binary question: có hole hay không?
    → Answer: có/không
    → Trigger: ACC detect inconsistency → body signal
    → = DETECTION mechanism

  GAP DIRECTION:
    → Shape question: hole hướng về đâu, chấp nhận fill nào?
    → Answer: specific set of constraints
    → Determine: which fills count as VALID → reward fires hay không
    → = EVALUATION mechanism

  CÙNG gap, KHÁC direction analysis:

    Einstein: Gap "unified physics" (binary: có)
    Direction: must reconcile Newton + Maxwell + be mathematically elegant
    → E=mc² MATCH direction → massive reward
    → Random formula MISS direction → no reward

    Con muốn xe: Gap "muốn xe" (binary: có)
    Direction: xe đẹp + thời thượng + bạn bè impressed + đi chơi được
    → Xe đúng ý MATCH → intensely pleasant
    → Xe cổ MISS direction (không thời thượng, bạn bè không impressed)
    → Tên lửa OUTSIDE direction entirely (không có chunks nào match)

  → Gap = "CÓ thiếu gì đó không?" (yes/no)
  → Gap Direction = "Thiếu CÁI GÌ CỤ THỂ?" (shape + constraints)
  → Body-feedback cần CẢ HAI: detect gap (§3.3) + evaluate direction match
```

### §1.3 — Relationship với §3.3

```
🟡 GAP DIRECTION KHÔNG THAY THẾ §3.3 — BỔ SUNG:

  §3.3 (Chunk-Gap mechanism):
    → HOW gap arises (network topology, ACC detection)
    → HOW gap transitions (Gap→Miss via Imagine-Final)
    → HOW gap drives behavior (novelty loop)
    → = MECHANISM layer

  Gap Direction (file này):
    → WHY gap has specific shape (surrounding chunk network)
    → WHY same gap accepts some fills but not others (direction match)
    → WHY reward magnitude varies (match quality)
    → = EVALUATION layer

  ANALOGY:
    §3.3 = "Hệ thống báo cháy HOẠT ĐỘNG thế nào" (mechanism)
    Gap Direction = "Cháy Ở ĐÂU và cần dập KIỂU GÌ" (content)
    → Cần CẢ HAI: detect + specify
```

### §1.4 — Gap Direction × By-Product Match (★ v2.0)

```
⭐ GAP DIRECTION = WHY BY-PRODUCT MATCH WORKS:

  Inter-Body-Mechanism.md §5.4 principle:
    Entity B fill gap CỦA B → output = by-product
    Khi by-product match gap direction CỦA A → A receives reward

  GAP DIRECTION IS THE MECHANISM UNDERNEATH:
    → "Match" = B's output KHỚP HƯỚNG CỤ THỂ của A's gap
    → "Mismatch" = B's output MISS hướng A's gap (no reward)
    → "Anti-match" = B's output CONFLICTS A's gap direction (friction)

  VÍ DỤ QUA LENS GAP DIRECTION:

    Tiền đạo → Hậu vệ:
      Hậu vệ A: gap "muốn đội thắng" → direction = "bàn thắng + phòng ngự"
      Tiền đạo B: fill gap CỦA B "muốn score" → output = bàn thắng
      B's output = bàn thắng → match A's direction "đội thắng"
      → A reward. B KHÔNG biết/cần biết A's gap direction.
      = By-product match VÌ directions tình cờ ALIGNED.

    Bố mua xe cổ cho con:
      Con A: gap direction = "xe đẹp thời thượng giới trẻ"
      Bố B: fill gap CỦA BỐ "muốn con vui" → output = xe cổ (bố's aesthetic)
      B's output = xe cổ → MISS A's direction (sai aesthetic)
      → A KHÔNG reward. Bố có ý tốt nhưng output MISS DIRECTION.
      = By-product MISMATCH vì bố's gap direction ≠ con's gap direction.

    CEO đổi mới ↔ nhân viên thích ổn định:
      Nhân viên A: gap direction = "stability, routine, predictable"
      CEO B: fill gap CỦA B "muốn growth" → output = change, disruption
      B's output = change → CONFLICTS A's direction (opposite to stability)
      → A NEGATIVE (active friction, not just no-match).
      = ANTI-MATCH: by-product actively conflicts gap direction.

  ⭐ TẠI SAO BY-PRODUCT MATCH XẢY RA ĐỦ THƯỜNG XUYÊN?
    → Species-level hardware overlap → gap directions PARTIALLY overlap
    → Cùng loài → cùng basic needs → basic gap directions SIMILAR
    → Culture/language = shared chunk install → shared gap directions
    → Self-selection: gravitate toward high match-rate partners
    → = Foundation cho Resonance (By-Product-Gap-Resonance v1.0 §1.5)

🟡 Gap direction as by-product match mechanism = framework synthesis.
   By-product match principle (Inter-Body §5.4) = 🟡 established logic.
   Species hardware overlap = 🟢 evolutionary biology.
```

---

## §2 — PROOF: TẠI SAO GAP BUỘC PHẢI CÓ HƯỚNG

### §2.1 — Logical necessity

```
⭐ GAP DIRECTION = CONSEQUENCE TẤT YẾU, KHÔNG PHẢI ASSUMPTION:

  Từ §3.3: Gap = HOLE in chunk network
  
  BƯỚC 1 — Hole tồn tại VÌ CÓ BỜ:
    → Hole trong tường: tồn tại vì có tường XUNG QUANH
    → Xóa tường → không còn hole → chỉ còn không gian trống
    → Hole in chunk network: tồn tại vì có CHUNKS xung quanh
    → Xóa surrounding chunks → không còn hole → chỉ "chưa biết"
    → = HOLE VÀ BỜ KHÔNG THỂ TÁCH RỜI

  BƯỚC 2 — Bờ có hình dạng → hole có hình dạng:
    → Bờ = surrounding chunks có CONTENT cụ thể
    → Content chunks: [A], [B], [A→B links], [A→? predictions]
    → Hole phải COMPATIBLE với bờ → hole có HÌNH DẠNG = f(bờ)
    → = Gap direction = shape of hole determined by surrounding chunks

  BƯỚC 3 — "Structure predict C" → C có constraints:
    → A và B là chunks CỤ THỂ (Newton mechanics, Maxwell electromagnetism)
    → "Nếu A và B → C" = C phải COMPATIBLE với cả A và B
    → C KHÔNG phải "bất kỳ thứ gì" — C phải:
      ⓐ Giải quyết inconsistency giữa A và B
      ⓑ Không phá vỡ connections hiện có
      ⓒ Fit vào network topology hiện tại
    → = C có CONSTRAINTS = gap có DIRECTION

  KẾT LUẬN:
    Gap direction = LOGICAL NECESSITY từ "gap = hole in chunk network"
    KHÔNG CẦN thêm mechanism mới
    KHÔNG CẦN thêm assumption mới
    Chỉ cần FORMALIZE consequence đã implicit trong §3.3
```

### §2.2 — Puzzle analogy

```
🟡 MẢNH PUZZLE THIẾU:

  Bức puzzle 1000 mảnh, còn thiếu 1 mảnh:
    → Mảnh thiếu có HÌNH DẠNG = f(hình dạng mảnh xung quanh)
    → Mảnh thiếu có MÀU SẮC = f(màu sắc mảnh xung quanh)
    → Mảnh thiếu có VỊ TRÍ = xác định bởi topology puzzle
    → = Mảnh BẤT KỲ không khớp — chỉ 1 mảnh ĐÚNG mới fill gap

  Chunk network Y HỆT:
    → Gap có "shape" = constraints từ surrounding chunks
    → Gap có "content direction" = what missing pattern should look like
    → Gap có "position" = where in network topology
    → = Chunk BẤT KỲ không fill — chỉ chunk ĐÚNG HƯỚNG mới fill

  NHƯNG khác puzzle ở 2 điểm quan trọng:

    ① Chunk gap: direction có RANGE (Goldilocks zone)
       → Nhiều fills CÓ THỂ match ở các mức khác nhau
       → Partial fill → partial reward (mini-arc)
       → = Gap direction = shape + range, không phải exact single answer

    ② Chunk gap: fill THAY ĐỔI BỜ → thay đổi GAP TIẾP THEO
       → Puzzle: fill 1 mảnh → bức tranh rõ hơn nhưng mảnh khác KHÔNG đổi
       → Chunk gap: fill 1 gap → NEW chunks compile → network GROW
         → detect NEW inconsistencies → NEW gaps emerge
       → = Mỗi fill CÓ THỂ tạo thêm gaps mới (§7.5 oscillation dynamics)
       → VD: Einstein fill special relativity → new chunks 
         → detect "gravity chưa fit" → NEW gap "general relativity"
       → = Gap landscape DYNAMIC, không phải static puzzle
```

### §2.3 — Counter-test: có gap KHÔNG CÓ hướng được không?

```
🟡 TEST: TÌM VÍ DỤ GAP KHÔNG CÓ DIRECTION:

  THỬ: "Tôi thấy thiếu gì đó nhưng không biết thiếu gì"
    → Felt sense (Gendlin 1978): body detect trước PFC verbal
    → NHƯNG: body VẪN có direction — chỉ PFC chưa articulate
    → Proof: khi tìm đúng → body NHẬN RA ("à, đây rồi!")
    → Nếu gap thật sự không có direction → body không thể "nhận ra"
    → = Gap direction TỒN TẠI ở body level, PFC có thể CHƯA biết

  THỬ: "Tôi chán nhưng không biết muốn gì"
    → Boredom = Chunk-Miss (Body-Feedback-Mechanism.md §3.2 variant ⓑ)
    → KHÔNG phải Chunk-Gap — đây là missing ACTIVITY patterns
    → Nếu thử nhiều thứ → khi gặp đúng → body reward → "à, muốn cái này!"
    → = Direction tồn tại (compiled baseline patterns) nhưng PFC chưa label

  THỬ: "Tôi curious về tất cả mọi thứ" (general curiosity)
    → Novelty.md §5 (DRD4 breadth): high breadth = 
      nhiều gaps NHỎ across domains
    → Mỗi gap NHỎ VẪN CÓ direction riêng
    → "Curious tất cả" = NHIỀU directed gaps, không phải 1 undirected gap
    → = Aggregate of many directed gaps ≠ one directionless gap

  KẾT LUẬN: Không tìm được ví dụ gap KHÔNG có direction.
  → Gap luôn có direction — PFC có thể chưa biết direction (implicit)
  → = Direction là property INEVITABLE, không phải optional
```

---

## §3 — "CHƯA BIẾT = KHÔNG CÓ GAP" (Foundational Principle)

### §3.1 — Principle statement

```
⭐⭐ FOUNDATIONAL PRINCIPLE:

  "CHƯA BIẾT = KHÔNG CÓ GAP"

  Formal:
    Chunks_related_to_X = ∅ → Gap_about_X = IMPOSSIBLE
    
  In words:
    Bạn KHÔNG THỂ thiếu thứ bạn không biết tồn tại.
    Gap CẦN surrounding chunks để TỒN TẠI.
    Không có chunks xung quanh = không có bờ = không có hole = không có gap.
    = Desire KHÔNG tự nhiên có — desire = f(chunks accumulated)

  VD ngắn:
    → Người chưa biết iPhone tồn tại: không muốn iPhone
    → Người chưa biết cờ vua: không muốn bàn cờ đẹp
    → Học sinh chưa biết vật lý sâu: không có gap về unified physics
    → Dân bản địa chưa biết laptop: concept không tồn tại = impossible gap
```

### §3.2 — Khác gì H10 P2?

```
⭐ "CHƯA BIẾT = KHÔNG GAP" ≠ H10 P2:

  H10 P2 (Chunks Base Adequate):
    → WHEN: Nhận stimulus → chunks thiếu → confused → no reward
    → QUESTION: "Tại sao không reward KHI NHẬN?"
    → = DIAGNOSIS — giải thích failure mode khi stimulus ĐÃ ĐẾN
    → VD: Con nhận tranh Van Gogh → "chả hiểu" → P2 fail

  "Chưa biết = không có gap":
    → BEFORE: Trước khi bất kỳ stimulus nào đến
    → QUESTION: "Tại sao KHÔNG MUỐN ngay từ đầu?"
    → = GENESIS — giải thích tại sao desire CHƯA TỒN TẠI
    → VD: Con CHƯA BAO GIỜ muốn tranh Van Gogh (gap không tồn tại)

  2 CÂU HỎI KHÁC NHAU, 2 TẦNG KHÁC NHAU:

    ┌────────────────────────────────────────────────────────────────┐
    │                                                                ���
    │  TẦNG 1 — GENESIS ("Chưa biết = không gap"):                  │
    │    Chunks about X = ∅ → Gap about X = impossible               │
    │    → Desire KHÔNG TỒN TẠI                                     │
    │    → TRƯỚC CẢ P1 (schema pending)                              │
    │    → Trả lời: TẠI SAO không muốn                              │
    │                                                                │
    │  TẦNG 2 — DETECTION (H10 P1-P5):                               │
    │    Gap TỒN TẠI → stimulus đến → H10 check                     │
    │    → P1: gap open? P2: decode được? P3: delta đủ?             │
    │    → P4: match range? P5: tag phù hợp?                        │
    │    → Trả lời: TẠI SAO reward fires hay không fires            │
    │                                                                │
    │  = TẦNG 1 quyết định gap CÓ HÌNH THÀNH KHÔNG                  │
    │  = TẦNG 2 quyết định reward CÓ FIRE KHÔNG (khi gap đã có)     │
    │  = "Chưa biết = không gap" là PREREQUISITE cho toàn bộ H10    │
    │                                                                │
    └────────────────────────────────────────────────────────────────┘
```

### §3.3 — Ví dụ chi tiết

```
🟡 VÍ DỤ: IPHONE CHO EM BÉ 3 TUỔI

  Em bé 3 tuổi:
    Chunks about smartphone: ≈ 0
    Chunks about apps, social media, camera: ≈ 0
    → Không có bờ → không có hole → không có gap
    → "Muốn iPhone" = IMPOSSIBLE desire
    → Nhận iPhone → curiosity (bấm → đèn sáng = sensory novelty)
    → NHƯNG: không có "pleasant vì có iPhone" — gap đó KHÔNG TỒN TẠI

  Teenager 16 tuổi:
    Chunks: [bạn bè có iPhone] + [chụp ảnh đẹp] + [MXH] + [status]
    → BỜ phong phú → HOLE rõ ràng: "mình chưa có iPhone"
    → Gap direction: "iPhone mới, model đẹp, dùng được MXH + camera"
    → Nhận iPhone đúng model → gap fill → pleasant
    → Nhận Nokia 1100 → cùng "phone" nhưng MISS direction → not pleasant

  → CÙNG vật (iPhone). KHÁC gap structure → KHÁC reward hoàn toàn.


🟡 VÍ DỤ: E=MC² CHO CÁC TRÌNH ĐỘ KHÁC NHAU

  Học sinh phổ thông:
    Chunks physics: F=ma, vài công thức cơ bản
    Chunks "unified framework": ≈ 0
    → Không có gap về unified physics — concept CHƯA TỒN TẠI
    → Nghe E=mc² → "ồ, hay" → MỨC label (mild novelty)
    → KHÔNG body-level reward vì KHÔNG CÓ GAP để fill

  Sinh viên mới biết quantum (label, chưa học kỹ):
    Chunks: labels [quantum], [relativity], [wave-particle]
    → Chunks NÔNG — label without depth
    → Gap TỒN TẠI nhưng NÔNG (network sparse → prediction yếu)
    → Nghe giải thích E=mc² → "ồ, vậy đó" → mild satisfaction
    → KHÔNG "intensely pleasant" vì gap nông + direction mờ

  Einstein (so sánh):
    Chunks: YEARS of deep physics (Newton + Maxwell + thought experiments)
    → Gap MASSIVE: "unified framework MUST exist" → direction CỰC RÕ
    → Direction: must reconcile Newton AND Maxwell AND be elegant
    → Gap open YEARS → Gap→Miss transition → compound signal
    → Derive E=mc² → match direction PERFECTLY → compound 3 dynamics:
      Chunk-Gap fill + Chunk-Miss reverse + Chunk-Shift self-schema
    → = "Intensely pleasant"

  ┌─────────────────────┬─────────────┬─────────────┬────────────────────┐
  │                     │ Học sinh    │ Sinh viên   │ Einstein           │
  ├─────────────────────┼─────────────┼─────────────┼────────────────────┤
  │ Chunks physics      │ Minimal     │ Labels only │ Years deep         │
  │ Gap exists?         │ ❌ Không    │ ✅ Nông     │ ✅ Massive         │
  │ Gap direction       │ N/A         │ Mờ, sparse  │ Cực rõ, rich       │
  │ E=mc² match?       │ N/A         │ Partial     │ Perfect            │
  │ Reward              │ Mild novelty│ Mild satis. │ Intensely pleasant │
  └─────────────────────┴─────────────┴─────────────┴────────────────────┘

  → CÙNG thông tin (E=mc²) → KHÁC reward HOÀN TOÀN
  → Reward = f(gap direction match), KHÔNG f(information value)
```

### §3.4 — Hệ quả của principle

```
⭐ 5 HỆ QUẢ QUAN TRỌNG:

  ① DESIRE KHÔNG TỰ NHIÊN — DESIRE ĐƯỢC XÂY DỰNG:
     → Trẻ sơ sinh: chỉ có Tier 1 gaps (hunger, warmth, contact)
     → Mọi desire khác = chunks accumulate → gap hình thành
     → "Tôi muốn X" = "chunks về X đã compile đủ để tạo gap"
     → = Desire is CONSTRUCTED, not innate (ngoại trừ Tier 1)

  ② EDUCATION CẦN BUILD CHUNKS TRƯỚC:
     → Trình bày đáp án TRƯỚC khi student có gap = không reward
     → Phải build chunks TRƯỚC → gap tự hình thành → THEN present answer
     → = "Không thể cho đáp án khi chưa có câu hỏi"
     → = Giải thích tại sao learning by doing > lecture

  ③ MARKETING = GAP INSTALLATION:
     → Ads build chunks: "người đẹp dùng sản phẩm X" + "lifestyle cool"
     → Chunks compile → gap hình thành: "nếu mình cũng có X..."
     → Product fills gap → reward → purchase
     → = Hiểu marketing qua gap direction mechanism

  ④ THERAPY PHẢI MAP GAP LANDSCAPE:
     → Client "muốn hạnh phúc nhưng không biết muốn gì cụ thể"
     → = Fuzzy gap direction (network sparse hoặc conflicted)
     → Therapy: help build chunks → gap direction SHARPEN → action possible
     → Hoặc: identify Background-Pattern constraining gap landscape

  ⑤ CROSS-CULTURAL DIFFERENCES = DIFFERENT GAP LANDSCAPES:
     → Culture A: chunks about X phong phú → gaps about X active
     → Culture B: chunks about X = ∅ → no gaps about X
     → = "Giá trị văn hóa" = shared gap landscape
     → = Tại sao "happiness" KHÁC nhau giữa cultures
```

---

## §4 — 4 PROPERTIES CỦA GAP DIRECTION

### §4.0 — Tổng quan

```
⭐ GAP DIRECTION CÓ 4 PROPERTIES QUAN SÁT ĐƯỢC:

  ┌────────────────────────────────────────────────────────────────┐
  │                                                                │
  │  ① DIRECTION (hướng): toward WHAT specific fill                │
  │  ② SPECIFICITY (độ rõ): constraints narrow hay broad           │
  │  ③ DEPTH (độ sâu): surrounding network → signal strength       │
  │  ④ RANGE (phạm vi): Goldilocks zone within direction           │
  │                                                                │
  │  4 properties INDEPENDENT — combine to determine:              │
  │  → WHICH fills the gap accepts                                 │
  │  → HOW STRONG the gap signal fires                             │
  │  → HOW MUCH reward when filled                                 │
  │                                                                │
  └────────────────────────────────────────────────────────────────┘
```

### §4.1 — Direction (hướng: toward what)

```
⭐ DIRECTION = CÁI GÌ CỤ THỂ mà network predict missing:

  Direction trả lời: "Thiếu CÁI GÌ?"
  = Content dự đoán = what the gap POINTS TOWARD

  VD — Xe:
    Network: [bạn bè có xe đẹp] + [oai] + [đi chơi] + [aesthetic hiện đại]
    → Direction: "xe đẹp thời thượng giới trẻ"
    → KHÔNG phải "xe" (quá rộng)
    → KHÔNG phải "phương tiện" (quá abstract)
    → KHÔNG phải "xe cổ đắt tiền" (sai aesthetic direction)
    → = Direction CỤ THỂ, phụ thuộc chunks CỤ THỂ đã compile

  VD — Einstein:
    Network: [Newton mechanics] + [Maxwell electromagnetism] + [conflict]
    → Direction: "unified framework reconciling BOTH + elegant"
    → KHÔNG phải "random formula" (miss direction)
    → KHÔNG phải "chọn 1 bỏ 1" (violate network structure)
    → = Direction = WHAT specifically resolves the inconsistency

  VD — Đang khát nước:
    Body-state: dehydration sensors fire → [khát] chunks activate
    → Direction: "nước" (Tier 1 evolutionary specific)
    → KHÔNG phải "đồ ăn" (different body-need direction)
    → Tier 1 direction: cực specific, universal, genes determined

  ⭐ DIRECTION CHANGE:
    → Direction CAN change khi chunk network grow:
      Ban đầu: "muốn xe" (broad) → biết thêm models → "muốn model X" (narrow)
    → Direction CAN split:
      "Muốn xe" → biết thêm → "muốn xe thể thao" + "muốn xe tiện dụng"
    → = Direction = DYNAMIC, evolves with chunk network
```

### §4.2 — Specificity (độ rõ: narrow vs broad)

```
⭐ SPECIFICITY = CONSTRAINTS CHẶT hay LỎNG:

  Specificity trả lời: "Bao nhiêu fills ĐƯỢC CHẤP NHẬN?"
  = Resolution of gap direction

  NARROW SPECIFICITY (constraints chặt):
    → Collector: "con tem cụ thể, năm cụ thể, quốc gia cụ thể"
    → Chỉ 1 fill ĐÚNG → match/mismatch rõ ràng
    → Reward: VERY HIGH khi match (rare fill found)
    → Risk: VERY LOW chance of fill → frustration

  BROAD SPECIFICITY (constraints lỏng):
    → "Muốn đi du lịch đâu đó" → nhiều destinations match
    → Nhiều fills acceptable → dễ match hơn
    → Reward: MODERATE per fill (less specific = less gap closure)
    → Benefit: flexible, adaptable

  SPECIFICITY = f(chunk network resolution):
    → Chunks ÍT về topic → gap direction BROAD (mờ, ít constraints)
    → Chunks NHIỀU về topic → gap direction NARROW (rõ, nhiều constraints)
    → VD: mới biết cờ vua → "muốn bàn cờ đẹp" (broad)
    → VD: chơi 10 năm → "muốn bàn cờ gỗ ebony, quân weighted, 
      Staunton pattern, 3.75 inch king" (narrow)

  SPECIFICITY × REWARD:
    → Narrow match → HIGH reward (rare + precise gap fill)
    → Broad match → MODERATE reward per fill
    → Narrow mismatch → HIGH dissonance (close but wrong)
    → Broad mismatch → MODERATE dissonance
    → VD: Muốn xe đỏ, được xe xanh (narrow miss: 90% match → 
      reward CÓ nhưng "nhưng...")
```

### §4.3 — Depth (độ sâu: signal strength)

```
⭐ DEPTH = SURROUNDING NETWORK → SIGNAL STRENGTH:

  Depth trả lời: "Gap signal MẠNH bao nhiêu?"
  = f(surrounding network size × density × time pending)

  NÔNG (network sparse):
    → Vài chunks liên quan → bờ mỏng → hole nhỏ
    → Body signal: nhẹ, dễ bỏ qua
    → VD: mới biết về topic → mild curiosity
    → VD: sinh viên nghe label "quantum" → shallow interest

  SÂU (network dense):
    → Nhiều chunks liên quan → bờ dày → hole lớn + rõ
    → Body signal: MẠNH, persistent, hard to ignore
    → VD: Einstein years of physics → massive gap signal → CAN'T ignore
    → VD: collector 20 năm thiếu 1 item → obsessive drive

  DEPTH × TIME PENDING:
    → Gap mới mở → signal vừa → CÓ THỂ fade nếu không reinforced
    → Gap open YEARS → Gap→Miss transition (§3.3 ①)
      → Signal COMPOUND: gap + miss + cortisol holding
    → = Depth × Time = COMPOUND signal strength

  DEPTH × REWARD MAGNITUDE:
    → Shallow gap fill → mild reward → "ồ, hay"
    → Deep gap fill → massive reward → "eureka!" "intensely pleasant!"
    → 🟡 Reward ∝ Gap_depth × Fill_match_quality
    → = Giải thích tại sao Einstein's E=mc² >> student's "ồ hay"
    → = CÙNG thông tin, KHÁC depth → KHÁC reward magnitude

  🟢 REFERENCE:
    → Gap decomposition mini-arc (§3.3): deeper gap = more mini-arcs needed
    → Effort-proportional reward (03-Reward.md §4.7)
    → Progress principle (Amabile & Kramer 2011): deeper gap = 
      more powerful "small wins"
```

### §4.4 — Range (phạm vi: Goldilocks within direction)

```
⭐ RANGE = NOT "MORE = BETTER" — BELL CURVE WITHIN DIRECTION:

  Range trả lời: "Fill bao nhiêu là TỐI ƯU?"
  = Goldilocks zone WITHIN gap direction (connect H10 P4)

  FRAMEWORK HIỆN TẠI (H10 P4):
    → "40-70% match" = Goldilocks
    → Too alien (<20%): "lạ quá" → confusion
    → Too familiar (>90%): "biết rồi" → habituation
  
  GAP DIRECTION EXTENDS:
    → Match HƯỚNG ĐÚNG nhưng MAGNITUDE sai → CŨNG miss
    → "More" within correct direction ≠ "better"

  VD — Massage:
    Direction: relaxation (Tier 1 body-need)
    Range: nhẹ → ok → pleasant → hơi đau → ĐAU
    = Bell curve: optimal pressure zone, beyond = nociception
    = Within correct direction, MAGNITUDE vượt range → negative

  VD — Khen:
    Direction: recognition of effort (self-schema relevant)
    Range: "Làm tốt đấy" ✅ → "Rất giỏi" ✅✅ → 
           "Thiên tài" ⚠️ → "Einstein thứ 2" ❌
    = Beyond range: P4 violated (mismatch self-schema)
    = Khen vẫn "đúng hướng" nhưng MAGNITUDE quá lớn → body reject

  VD — Tiền thưởng:
    Direction: resource reward (body-need met)
    Range: 1 triệu ✅ → 10 triệu ✅✅ → 100 triệu ⚠️ → 1000 tỷ ❌
    = 1000 tỷ: đúng direction (tiền) nhưng VƯỢT range
    = Body: "không tin" → P4 violated (too alien for self-schema)

  VD — Gia vị đồ ăn:
    Direction: taste reward (Tier 1)
    Range: nhạt → vừa → ngon → quá mặn/cay → PAIN
    = Tier 1 range: evolutionary calibrated optimal zone
    = x10 gia vị: đúng direction (taste) nhưng VƯỢT range → nociception

  ⭐ RANGE = MULTI-DIMENSIONAL:
    → Body evaluate NHIỀU chiều ĐỒNG THỜI
    → VD: Áo lụa tơ tằm:
      Texture: mềm ✅ + Temperature: mát ✅ + Breathability: thoáng ✅
      = Match nhiều chiều → reward
    → VD: Túi nilon:
      Texture: mềm ✅ + Temperature: nóng ❌ + Breathability: blocked ❌
      = Match 1 chiều, violate nhiều chiều → net negative
    → = Range is PER-DIMENSION, body compute NET across all dimensions

  RANGE × SPECIFICITY:
    → Narrow specificity + narrow range = VERY hard to satisfy
      (collector muốn item cụ thể, condition perfect)
    → Broad specificity + broad range = EASY to satisfy
      (muốn đi chơi đâu đó, thời tiết tạm ổn)
    → = Specificity × Range = "khó tính" spectrum
```

### §4.5 — 4 Properties kết hợp

```
🟡 BẢNG TỔNG HỢP:

  ┌──────────────┬──────────────┬──────────────┬───────────────┐
  │ Property     │ Question     │ Determines   │ VD            │
  ├──────────────┼──────────────┼──────────────┼───────────────┤
  │ Direction    │ Thiếu CÁI GÌ│ Which fills  │ "xe đẹp thời  │
  │              │ cụ thể?      │ valid        │ thượng"       │
  ├──────────────┼──────────────┼──────────────┼───────────────┤
  │ Specificity  │ Constraints  │ How many     │ Broad: "xe"   │
  │              │ chặt/lỏng?   │ fills match  │ Narrow: "xe   │
  │              │              │              │ model X đỏ"   │
  ├──────────────┼──────────────┼──────────────┼───────────────┤
  │ Depth        │ Signal mạnh  │ Reward       │ Shallow: mild │
  │              │ bao nhiêu?   │ magnitude    │ Deep: massive │
  ├──────────────┼──────────────┼──────────────┼───────────────┤
  │ Range        │ Bao nhiêu    │ Optimal zone │ Massage:      │
  │              │ là tối ưu?   │ for fill     │ nhẹ→đau      │
  └──────────────┴──────────────┴──────────────┴───────────────┘

  Reward = f(Direction_match × Specificity_fit × Depth × Range_within)
  
  → Direction wrong → no reward (xe cổ cho teen)
  → Direction right + Specificity miss → partial reward (xe xanh thay đỏ)
  → Direction right + Depth shallow → mild reward (student nghe E=mc²)
  → Direction right + Range exceeded → diminished/negative (khen quá lớn)
  → ALL match → maximum reward (xe đúng ý cho teen, E=mc² cho Einstein)
```

---

## §5 — UNIFIED DIRECTION MODEL (Tier 1-4)

### §5.1 — Tất cả direction = chunk pattern direction

```
⭐⭐ USER'S KEY INSIGHT: KHÔNG PHẢI 2 LOẠI DIRECTION — TẤT CẢ LÀ PATTERNS

  Sensory input vào não:
    Da tiếp xúc lụa → mechanoreceptors fire → neural signal
    → Somatosensory cortex → PATTERN
    → Pattern match compiled patterns → body-feedback

  Compiled patterns TỪ EVOLUTION = CHUNKS:
    → Genes wire connections sẵn (Tier 1)
    → Millions of years: [smooth+breathable+cool] wired CỰC SÂU
    → Universal across humans (chung evolutionary history)
    → NHƯNG VẪN LÀ CHUNKS — cùng substrate, cùng rules

  Compiled patterns TỪ EXPERIENCE = CHUNKS:
    → Personal experience wire connections (Tier 2-4)
    → Years-decades: [xe đẹp+oai+friends approve] compiled
    → Personal/cultural (khác mỗi người)
    → CŨNG LÀ CHUNKS — cùng substrate, cùng rules

  → CHỈ CÓ 1 LOẠI DIRECTION: chunk pattern direction
  → Khác biệt: ORIGIN + DEPTH + UNIVERSALITY
  → KHÔNG phải "hardware" vs "software" — tất cả chunks
  → Consistent với "chunks = sole substrate" (Chunk.md v2.0 §1)

  v2.0 CONNECTION — COMPILABLE ARCHITECTURE:
    → Compilable Architecture (Body-Base.md v3.1, Inter-Body §1):
      general-purpose reward + compilation + social hardware
    → Gap directions KHÔNG hardwired per-content (Hardwired Architecture species)
    → Gap directions EMERGE from accumulated chunk network
    → = WHY gap direction is PERSONAL (not species-fixed)
    → = WHY gap direction CHANGES (chunks accumulate → direction evolves)
    → Hardwired Architecture (insects): gap directions = FIXED (genes specify)
      → Bee: "find flower with X wavelength" = hardwired direction
    → Compilable Architecture (humans): gap directions = COMPILED
      → Human: "find car that matches MY aesthetic" = compiled direction
    → = Compilable Architecture × gap direction = foundation cho DIVERSITY of desires
```

### §5.2 — 4 Tiers of direction origin

```
🟡 DIRECTION ORIGIN = 4 TIERS (Chunk.md §2 calibration hierarchy):

  TIER 1 — EVOLUTIONARY (genes compile):
    → Origin: millions of years natural selection
    → Depth: CỰC SÂU (hardwired, universal)
    → Examples: hunger, thirst, pain, temperature, touch comfort
    → "Chưa biết = không gap": KHÔNG ÁP DỤNG thông thường
      → Genes ĐÃ "biết sẵn" → trẻ sơ sinh VẪN có gap (hunger)
      → = Species đã "experience" millions years → genes carry knowledge
    → Modifiable: CỰC KHÓ (requires evolutionary timescale)
    → VD: Lụa tơ tằm → da cảm nhận TRỰC TIẾP → reward
      dù chưa từng mặc (Tier 1 chunks already know "smooth = good")

  TIER 2 — DEVELOPMENTAL (childhood compile):
    → Origin: childhood experience (0-18)
    → Depth: SÂU (compiled during critical periods)
    → Examples: attachment style, cultural norms, language
    → "Chưa biết = không gap": ÁP DỤNG HOÀN TOÀN
    → Modifiable: KHÓ (Background-Pattern territory)
    → VD: Trẻ lớn lên thấy bạn bè có xe → gap hình thành

  TIER 3 — CULTURAL (shared compile):
    → Origin: cultural exposure, education, social
    → Depth: TRUNG BÌNH (compiled qua repeated cultural input)
    → Examples: "xe cổ = giá trị" (collector culture), jazz appreciation
    → "Chưa biết = không gap": ÁP DỤNG HOÀN TOÀN
    → Modifiable: MODERATE (exposure + time)
    → VD: Bố thích xe cổ (Tier 3 collector culture) → 
      gap direction khác con (Tier 2-3 youth culture)

  TIER 4 — LEARNED (individual compile):
    → Origin: deliberate learning, expertise
    → Depth: VARIABLE (tùy effort × time × emotional weight)
    → Examples: physics expertise, programming skill, art training
    → "Chưa biết = không gap": ÁP DỤNG HOÀN TOÀN
    → Modifiable: DỄ NHẤT (build chunks → gap direction shifts)
    → VD: Einstein physics chunks (Tier 4) → gap direction "unified physics"
```

### §5.3 — Tier 1 đặc biệt: genes = pre-installed chunks

```
⭐ TIER 1 CÓ KHÁC BIỆT QUAN TRỌNG:

  "Chưa biết = không có gap" principle nói:
    Không có chunks → không có bờ → không có hole → không có gap

  NHƯNG Tier 1: genes PRE-INSTALL chunks:
    → Trẻ sơ sinh CHƯA experience sữa mẹ → NHƯNG VẪN có gap (hunger)
    → Chưa experience áo ấm → NHƯNG VẪN có gap (cold discomfort)
    → = "Cá nhân chưa biết" nhưng "species đã biết"
    → Genes carry evolutionary knowledge as PRE-COMPILED chunks

  REFINE PRINCIPLE cho Tier 1:
    Original: "Chưa biết = không có gap"
    Refined: "Chưa biết VÀ genes chưa wire = không có gap"
    → Tier 1: genes wire → gap exists without personal experience
    → Tier 2-4: genes KHÔNG wire → gap CẦN personal/cultural experience
    → = 2 nguồn "biết": evolutionary (genes) + experiential (chunks)

  TẠI SAO REFINE NÀY QUAN TRỌNG:
    → Giải thích silk example: lần đầu mặc VẪN pleasant 
      (Tier 1 chunks "biết sẵn" smooth = good)
    → Giải thích food: lần đầu ăn ngon VẪN biết ngon 
      (Tier 1 taste receptors calibrated)
    → Giải thích: tại sao Tier 1 gaps UNIVERSAL nhưng 
      Tier 2-4 gaps PERSONAL
    → = Tier 1 = shared species knowledge. 
      Tier 2-4 = individual accumulated knowledge.
```

### §5.4 — Bảng so sánh unified

```
🟡 SO SÁNH 3 CASES QUA UNIFIED MODEL:

  ┌──────────────────┬───────────────┬───────────────┬───────────────┐
  │                  │ Silk (Tier 1) │ Xe (Tier 2-3) │ E=mc²(Tier 4)│
  ├──────────────────┼───────────────┼───────────────┼───────────────┤
  │ Chunk origin     │ Evolution     │ Experience +  │ Years study   │
  │                  │ (genes wire)  │ social context│ (deliberate)  │
  │ Depth            │ Cực sâu       │ Trung bình    │ Sâu (expert)  │
  │ Universality     │ ~Universal    │ Cultural/     │ Individual    │
  │                  │               │ generational  │               │
  │ Gap direction    │ Multi-dim     │ Specific      │ Specific      │
  │                  │ optimal space │ social object │ knowledge gap │
  │ "Chưa biết=     │ N/A (genes    │ ✅ Áp dụng   │ ✅ Áp dụng   │
  │   no gap"        │ pre-install)  │ hoàn toàn     │ hoàn toàn     │
  │ Modifiable?      │ Cực khó       │ Moderate      │ Yes (learn)   │
  │ Direction source │ Genes         │ Chunks + Background-Pattern   │ Chunks        │
  │ Match mechanism  │ Sensory match │ Pattern match │ Pattern match │
  │ Range type       │ Evolutionary  │ Social/       │ Intellectual  │
  │                  │ optimal zone  │ personal zone │ coherence     │
  └──────────────────┴───────────────┴───────────────┴───────────────┘

  ⭐ CÙNG MECHANISM: chunks → gap direction → match → reward
  ⭐ KHÁC: origin, depth, universality, modifiability
  ⭐ = 1 model THỐNG NHẤT cho TOÀN BỘ reward/dissonance evaluation
```

### §5.5 — Compiled/Fresh processing × gap direction (★ v2.0)

```
⭐ GAP DIRECTION EVALUATION = COMPILED HOẶC FRESH:

  (Inter-Body-Mechanism.md §3, Body-Feedback-Label.md v2.0 §8)

  COMPILED EVALUATION (body-direct, cost ≈ 0):
    → Expert in domain: compiled chunks match CHECK → automatic
    → Nghe E=mc² → body BIẾT match hay không (Einstein case)
    → Thấy xe → body BIẾT "đúng ý" hay không (teen case)
    → Speed: milliseconds. Accuracy: HIGH (nếu chunks phong phú)
    → = Gap direction match evaluated TRƯỚC PFC aware

  FRESH EVALUATION (PFC deliberate, costly):
    → Lĩnh vực mới: PFC phải BUILD match/mismatch assessment
    → Xem review xe → PFC process specs → "có match gap không?"
    → Speed: slow (seconds-minutes). Accuracy: VARIABLE.
    → = PFC TRY to evaluate — nhưng CÓ THỂ SAI (PFC=Lawyer, §7)

  SPECTRUM (không phải binary):
    → Full compiled: body knows instantly (expert + domain match)
    → Mostly compiled + some fresh: body guides + PFC fine-tunes
    → Mostly fresh: PFC lead + body gives vague signal
    → Full fresh: no compiled chunks → "không biết muốn gì"

  ⭐ TẠI SAO QUAN TRỌNG:
    → Expert's "feeling" about match = COMPILED evaluation (accurate, fast)
    → Beginner's "analysis" of match = FRESH evaluation (slow, uncertain)
    → "Trust your gut" = trust compiled evaluation (IF chunks phong phú)
    → "Think carefully" = use fresh evaluation (IF compiled insufficient)
    → = Dual Check (Ask-AI v3.1): body = quality controller, domain = arbiter

🟡 Compiled/Fresh evaluation spectrum = framework synthesis.
   Compiled processing = automatic = 🟢 (dual-process theory, Kahneman 2011).
   Fresh PFC processing = deliberate = 🟢 (working memory literature).
```

---

## §6 — 2-LAYER MODEL: SIGNAL MECHANISM vs DIRECTION CONTENT

### §6.1 — Tại sao cần 2 layers

```
⭐ PREDICTION ERROR (SCHULTZ 1997) ĐÚNG NHƯNG CHƯA ĐỦ:

  Schultz 1997:
    → VTA fires dopamine khi: actual > predicted
    → VTA suppress khi: actual < predicted
    → = Signal mechanism: body DETECT "có gì đó khác expected"
    → = GENERIC: "better/worse than expected" — nhưng 
      KHÔNG carry thông tin "khác CÁI GÌ cụ thể"

  CHƯA ĐỦ vì:
    → Cùng "actual > predicted" (positive prediction error)
    → Nhưng: xe thời thượng = pleasant, xe cổ = không thích
    → Cả 2 đều "better than expected" (bố mua xe bất ngờ)
    → Tại sao KHÁC reward? Vì DIRECTION KHÁC.

  CẦN THÊM LAYER 2:
    → Layer 1 cho biết: "có mismatch/match" (signal fires)
    → Layer 2 cho biết: "match CÁI GÌ cụ thể" (direction content)
    → Cần CẢ HAI để giải thích reward THỰC TẾ
```

### §6.2 — 2 Layers defined

```
⭐⭐ 2-LAYER MODEL:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  LAYER 1 — SIGNAL MECHANISM (HOW body detects):             │
  │                                                             │
  │    VTA: detect prediction-delta (Schultz 1997)              │
  │    ACC: detect inconsistency (Bush et al. 2000)             │
  │    = GENERIC mechanism: "có gì đó khác/thiếu/mâu thuẫn"    │
  │    = KHÔNG carry thông tin "khác CÁI GÌ"                   │
  │    = Hệ thống báo cháy: CHỈ báo "có cháy"                 │
  │                                                             │
  │  LAYER 2 — DIRECTION CONTENT (WHAT body expects):           │
  │                                                             │
  │    Chunk network structure: surrounding chunks define gap   │
  │    Gap direction: WHAT specifically is predicted missing     │
  │    Match quality: HOW well stimulus fits gap shape           │
  │    = PERSONAL: mỗi người có direction KHÁC                  │
  │    = Bản đồ ngôi nhà: CHỈ RÕ "cháy ở đâu, hướng nào"     │
  │                                                             │
  │  TOGETHER = COMPLETE EVALUATION:                             │
  │    Layer 1: "có cháy" (signal fires)                        │
  │    Layer 2: "cháy ở phòng bếp, cần nước" (direction match) │
  │    = Body detect + biết direction = reward hoặc dissonance  │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

  v2.0 NOTE — BY-PRODUCT MATCH × 2-LAYER MODEL:
    → Inter-body interaction:
      Layer 1: "B did something" (prediction-delta from B's action)
      Layer 2: "B's output match MY gap direction?" (direction evaluation)
    → By-product match = Layer 2 match positive
    → Anti-match = Layer 2 match NEGATIVE (conflicts direction)
    → No-match = Layer 1 fires but Layer 2 = neutral (irrelevant)
    → = 2-layer model giải thích tại sao cùng action của B →
      A1 reward, A2 no-match, A3 anti-match (khác gap direction)
```

### §6.3 — H10 reinterpretation qua 2 layers

```
⭐ H10 5 PRECONDITIONS = ĐÃ MÔ TẢ 2 LAYERS (chưa nói rõ):

  ┌─────────────────────┬──────────┬──────────────────────────────┐
  │ H10 Precondition    │ Layer    │ Function trong 2-layer model │
  ├─────────────────────┼──────────┼──────────────────────────────┤
  │ P1 Schema Pending   │ Layer 2  │ DIRECTION EXISTS             │
  │ (body-need gap)     │          │ Gap đã hình thành, có hướng  │
  │                     │          │ = Prerequisite cho evaluation │
  ├─────────────────────┼──────────┼──────────────────────────────┤
  │ P2 Chunks Base      │ Layer 2  │ DIRECTION CAN FORM           │
  │ (đủ substrate)      │          │ Đủ chunks = đủ bờ = có hole │
  │                     │          │ = Prerequisite cho P1        │
  ├─────────────────────┼──────────┼──────────────────────────────┤
  │ P3 Prediction-Delta  │ Layer 1  │ SIGNAL FIRES                 │
  │ (biến động đủ)      │          │ Prediction-delta detected    │
  │                     │          │ = Detection mechanism active  │
  ├─────────────────────┼──────────┼──────────────────────────────┤
  │ P4 Goldilocks       │ Layer 2  │ DIRECTION MATCH QUALITY      │
  │ (40-70% match)      │          │ Match VỚI gap direction      │
  │                     │          │ = Range property check        │
  ├─────────────────────┼──────────┼──────────────────────────────┤
  │ P5 Chunk Tag        │ Layer 2  │ DIRECTION VALENCE            │
  │ (opioid/cortisol)   │          │ Compiled association tag      │
  │                     │          │ = Reward or threat direction? │
  └─────────────────────┴──────────┴──────────────────────────────┘

  HIERARCHY RÕ HƠN:

    "Chưa biết = không gap"
        ↓ (prerequisite)
    P2: đủ chunks → direction CAN form
        ↓ (prerequisite)
    P1: gap direction EXISTS (pending active)
        ↓ (gap exists, now evaluate stimulus)
    P3: signal fires (Layer 1 — detection)
        ↓ (something detected)
    P4: direction match quality (Layer 2 — within range?)
        ↓ (match quality assessed)
    P5: valence tag check (Layer 2 — reward or threat?)
        ↓
    REWARD or DISSONANCE fires

  → "Chưa biết = không gap" = TẦNG 0 — trước cả H10
  → P2 → P1 = Layer 2 prerequisites (gap phải tồn tại)
  → P3 = Layer 1 (signal phải fire)
  → P4 → P5 = Layer 2 quality check
  → = H10 ĐÃ mô tả 2 layers — chỉ chưa PHÂN BIỆT 2 layers
```

### §6.4 — Tại sao 2-layer model hữu ích

```
🟡 GIẢI THÍCH HIỆN TƯỢNG MÀ 1-LAYER KHÔNG GIẢI THÍCH ĐƯỢC:

  ① "Cùng prediction error, khác reward":
    → Xe thời thượng và xe cổ: BOTH surprise (positive prediction error)
    → 1-layer: cả 2 nên reward → SAI
    → 2-layer: Layer 1 fire cho CẢ 2, nhưng Layer 2 chỉ match cho 
      xe thời thượng → ĐÚNG

  ② "Reward là personal":
    → 1-layer: prediction error = generic → should be universal → SAI
    → 2-layer: Layer 2 = chunk network = PERSONAL → reward personal → ĐÚNG

  ③ "More ≠ better":
    → 1-layer: larger prediction error = more reward → SAI
    → 2-layer: Layer 1 = larger delta, nhưng Layer 2 = out of range 
      → diminished/negative → ĐÚNG

  ④ "Biết nhưng không cảm":
    → PFC updated (Layer 1 acknowledged) nhưng 
      chunk network unchanged (Layer 2 direction same)
    → 1-layer: know = feel → SAI
    → 2-layer: Layer 1 (know) ≠ Layer 2 (feel direction) → 
      can diverge → ĐÚNG

  ⑤ "By-product match selective" (v2.0):
    → 1-layer: B did something unexpected → all observers reward → SAI
    → 2-layer: Layer 1 fires for all observers, nhưng Layer 2 (direction match)
      = DIFFERENT per observer → chỉ matching observers reward → ĐÚNG
    → = Giải thích tại sao cùng 1 action → người thích người ghét

  → 2-layer model không THAY THẾ prediction error — 
    THÊM layer underneath giải thích CONTENT
```

---

## §7 — GAP DIRECTION FORMATION

### §7.1 — Natural formation: chunks compile → gaps emerge

```
⭐ GAP DIRECTION HÌNH THÀNH TỰ NHIÊN KHI CHUNKS ACCUMULATE:

  FLOW:
    Experience → chunks compile → network grow → internal structure form
    → Structure predict "C should exist" → C chưa có → GAP with DIRECTION

  VD — Con thấy bạn có xe:
    ① Thấy bạn có xe đẹp → chunks compile: [bạn-có-xe] + [trông-oai]
    ② Nghe bạn kể đi chơi → chunks thêm: [đi-chơi-thoải-mái] + [tự-do]
    ③ Thấy bạn gái bạn impressed → chunks thêm: [xe → impressed]
    ④ Network predict: "nếu mình cũng có → oai + tự do + impressed"
    ⑤ Predict chưa thành hiện thực → GAP hình thành
    ⑥ Gap direction = f(tất cả chunks compiled): 
       "xe đẹp thời thượng giới trẻ"
    → KHÔNG CÓ BƯỚC NÀO CẦN PFC CHỦ ĐỘNG
    → Vô thức tự compile → gap tự emerge

  VD — Học sinh dần biết vật lý:
    ① Học Newton → chunks compile: [F=ma] + [gravity]
    ② Học Maxwell → chunks thêm: [electromagnetic waves] + [light]
    ③ Nếu giáo viên GIỎ → giới thiệu conflict: "Newton và Maxwell 
       mâu thuẫn về tốc độ ánh sáng"
    ④ Conflict chunks: [Newton ≠ Maxwell ở X]
    ⑤ Network predict: "phải có framework giải quyết"
    ⑥ Gap hình thành: direction = "giải mâu thuẫn Newton-Maxwell"
    → Gap CHỈ hình thành SAU KHI đủ chunks compile
    → Giáo viên DỞ skip conflict → student KHÔNG có gap → bài giảng boring

  FORMATION SPEED:
    → Emotional peak experience: 1 lần CÓ THỂ đủ
      (VD: thấy bạn lái xe oai → emotional → gap nhanh)
    → Neutral repeated experience: cần nhiều lần
      (VD: học physics dần dần → gap chậm)
    → = Chunk.md §2.2: compile rate = f(repetition × saliency × 
      peak_valence × multi_modal × contingency)
```

### §7.2 — Gap→Miss transition: direction SHARPENS

```
🟡 IMAGINE-FINAL PREVIEW LÀM DIRECTION RÕ HƠN:

  Body-Feedback-Mechanism.md §3.3 ①:
    Gap detected → PFC build Imagine-Final preview
    → Preview lặp → body compile preview thành baseline
    → Gap CHUYỂN thành Miss (body now EXPECTS cái chưa có)

  GAP DIRECTION PERSPECTIVE:
    → Ban đầu: gap direction MỜ (network sparse → shape vague)
    → Imagine-Final preview: ADD DETAIL to direction
      "Có xe" → "xe model X" → "xe model X màu đỏ" → "lái xe đi biển"
    → Mỗi preview cycle: direction SHARPEN (specificity tăng)
    → = Imagine-Final = direction refinement mechanism

  VD: "Muốn xe" evolution:
    Week 1: "muốn có xe đi lại" (broad direction)
    Week 4: "muốn xe thể thao, nhìn đẹp" (direction narrowing)
    Month 3: "muốn model X, màu đỏ, nội thất đen" (narrow direction)
    → Direction SHARPEN theo Imagine-Final preview iterations
    → Specificity tăng → range thu hẹp → khó satisfy hơn

  ⚠️ RISK: Over-specification
    → Preview lặp quá nhiều → direction CỰC narrow
    → Reality hiếm khi match 100% → "đạt rồi mà vẫn thiếu"
    → = §3.3 ⑦: "Kỳ vọng càng cao, thất vọng càng lớn"
    → = Direction over-specification = setup for disappointment
```

### §7.3 — Direction change: network grow → gap shape evolves

```
🟡 GAP DIRECTION KHÔNG CỐ ĐỊNH — EVOLVES VỚI NETWORK:

  Chunks MỚI compile → surrounding network thay đổi
  → Bờ thay đổi → hole shape thay đổi → direction evolves

  VD: "Muốn xe" → biết thêm → direction SHIFT:
    Phase 1: "xe đẹp thời thượng" (youth aesthetic)
    Phase 2: học về xe → biết xe cổ giá trị → chunks mới compile
    Phase 3: gap direction SHIFT: "xe cổ classic cũng đẹp"
    → = Education/exposure → direction shift POSSIBLE

  VD: Career gap direction evolution:
    Age 18: "muốn giàu" (broad, status-driven)
    Age 25: "muốn career có ý nghĩa" (direction shift via experience)
    Age 35: "muốn balance work-life" (direction shift via feedback)
    → Mỗi phase: chunks compile → gap direction evolves

  NHƯNG: Background-Pattern RESIST direction change (§9):
    → Background-Pattern = deeply compiled pattern → bias gap landscape
    → Gap direction shift CẦN vượt qua Background-Pattern inertia
    → = Tại sao career change ở 35 KHÓ HƠN ở 25
    → = Background-Pattern.md: resolution = years, not weeks
```

### §7.4 — Direction split: 1 gap → 2 sub-gaps

```
🟡 GAP CÓ THỂ SPLIT KHI NETWORK REFINE:

  Network grow → detect: "gap này thực ra = 2 gaps KHÁC NHAU"
  → 1 parent gap → 2+ child gaps, mỗi cái có direction riêng

  VD: "Muốn xe" splits:
    → "Muốn xe thể thao (đi chơi weekend)"
    → "Muốn xe tiện dụng (đi làm hàng ngày)"
    → = 2 functions, 2 contexts, 2 directions

  VD: Einstein "unified physics" splits:
    → "Special relativity" (uniform motion)
    → "General relativity" (gravity + acceleration)
    → Mỗi sub-gap có direction riêng, fill riêng

  = Gap decomposition (§3.3 mini-arc) CŨNG LÀ direction split:
    Big gap → mini gaps = big direction → sub-directions
    Mỗi sub-gap fill = mini reward
    All sub-gaps fill = compound reward
```

### §7.5 — Oscillation dynamics: fill tạo CẢ reward VÀ new dissonance

```
⭐⭐ MINI-FILL KHÔNG CHỈ GIẢM GAP — CÒN TẠO GAPS MỚI:

  HÌNH DUNG ĐƠN GIẢN (sai):
    Gap → fill → reward → smaller gap → fill → ... → gap = 0 → done
    = Linear giảm dần, cuối cùng xong

  HÌNH DUNG ĐÚNG:
    Gap → fill → reward + NEW CHUNKS COMPILE
    → New chunks = new BỜ → detect NEW inconsistencies
    → = THÊM dissonance (network LỚN HƠN → thấy NHIỀU HƠN)
    → Net: reward TỪ fill + dissonance TỪ new detections

  CƠ CHẾ:

    ① FILL: mini gap closed → chunks mới compile → opioid (reward) ✅
    ② GROW: new chunks = network expand → new bờ appear
    ③ DETECT: bigger network → detect inconsistencies CHƯA THẤY trước
    ④ NEW GAP: new inconsistency → new gap → new direction
    ⑤ OSCILLATION: reward (①) + dissonance (④) ĐỒNG THỜI

  PATTERN:
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  fill₁ → reward₁ + chunks₁ → detect new gap₂       │
    │  fill₂ → reward₂ + chunks₂ → detect new gap₃       │
    │  fill₃ → reward₃ + chunks₃ → detect new gap₄       │
    │  ...                                                │
    │  fillₙ → BREAKTHROUGH: many chunks suddenly UNIFY   │
    │       → COMPOUND reward (all accumulated gaps close) │
    │       → BUT: bigger network → detect NEXT-LEVEL gap │
    │       → LOOP CONTINUES at higher level               │
    │                                                     │
    └─────────────────────────────────────────────────────┘

  TREND qua process:
    → Reward per fill: TĂNG (each fill more chunks = more opioid)
    → Dissonance per detection: CŨNG TĂNG (network larger = bigger holes)
    → Total dissonance: TÍCH TỤ (many unresolved mini-inconsistencies)
    → Cho tới CRITICAL MASS: accumulated chunks suddenly cohere
    → = BREAKTHROUGH = compound resolution of ALL accumulated gaps

  VD — Einstein (chi tiết ở §10.4):
    Year 1-5: fill photoelectric → reward + new chunks 
      → detect "wave-particle duality mâu thuẫn" → new dissonance
    Year 5-10: fill special relativity → reward + new chunks
      → detect "gravity chưa fit" → more dissonance
    Year 10-15: accumulate tensor math + thought experiments
      → dissonance CỰC CAO (rất nhiều chunks giá trị chưa unified)
    November 1915: field equations → ALL accumulated chunks UNIFY
      → COMPOUND reward (years × massive network × all-at-once)

  ⭐ TẠI SAO BREAKTHROUGH REWARD CỰC LỚN:
    → Reward KHÔNG chỉ = "fill 1 gap"
    → Reward = resolve ALL accumulated mini-inconsistencies ĐỒNG THỜI
    → = Accumulated dissonance over YEARS → released IN ONE MOMENT
    → Compound: Gap fill + Miss reverse + Shift + Cortisol drop
    → = Tại sao "eureka" moments feel TRANSCENDENT

  ⚠️ RISK: Nếu breakthrough KHÔNG đến:
    → Accumulated dissonance keeps growing → no compound resolution
    → Cortisol holding → persistent → burnout
    → = Tại sao research CÓ THỂ destructive nếu gap too deep
    → VD: Einstein spent 30 years on unified field theory → never resolved
    → = Perpetual gap at too deep level → chronic dissonance

  🟢 REFERENCE:
    → Progress principle (Amabile & Kramer 2011): small wins sustain
    → Gap decomposition (§3.3 mini-arc): each mini fill = reward
    → Combinatorial explosion (Novelty.md §5): network grows → more combinations
```

---

## §8 — GAP DIRECTION × EXTERNAL INSTALL

### §8.1 — F3 applied to gap CREATION

```
⭐ CHUNK EXTERNAL INSTALL (F3) → GAP INSTALL:

  Chunk.md §2 F3: External Install = chunks installed từ bên ngoài
  (education, media, social influence, advertising)

  GAP DIRECTION PERSPECTIVE:
    → F3 install chunks XUNG QUANH → gap TỰ hình thành
    → External agent KHÔNG "cài gap trực tiếp"
    → External agent install CHUNKS → chunks tạo BỜ → hole emerge
    → = "Directed gap installation" = build surrounding chunks 
      sao cho gap hình thành với DIRECTION mong muốn

  CƠ CHẾ:
    ① Install chunks A, B: [sản phẩm X] + [người dùng X = cool]
    ② Chunks compile → network predict: "nếu mình cũng có X → cool"
    ③ Predict chưa thành → gap hình thành: direction = "sản phẩm X"
    ④ Sản phẩm X available → fills gap → reward → purchase
    → = Advertiser engineers gap direction TOWARD their product

  v2.0 NOTE — 5-CHANNEL INPUT VECTOR (Inter-Body §6):
    → Gap install qua CHANNEL nào?
    → Ch1 Hardware Sensory: product design triggers Tier 1 (beauty, texture)
    → Ch3 Compiled Chunks: brand awareness (repeated exposure → compiled)
    → Ch4 Entity Actions: influencer uses product → social proof
    → Ch5 PFC Active Chain: ad presents "logical argument" for need
    → = Marketing uses MULTIPLE channels simultaneously
    → = Most effective: Ch3+Ch4 (compiled + social) > Ch5 only (just logic)
```

### §8.2 — 4 hình thức gap install

```
🟡 4 HÌNH THỨC GAP INSTALL:

  ① ADVERTISING (thương mại):
     → Install chunks: [sản phẩm + lifestyle + social proof]
     → Gap direction: toward specific product
     → Fill: purchase product
     → Ethical? Depends on product quality vs gap promise
     → = Marketing 101: "create need" = install gap direction

  ② EDUCATION (giáo dục):
     → Install chunks: [knowledge base + conflict + curiosity]
     → Gap direction: toward understanding/skill
     → Fill: learning, practice, discovery
     → = Good teacher: build chunks FIRST → present challenge SECOND
     → = Bad teacher: present answer without gap → no reward → boring

  ③ SOCIAL MEDIA (xã hội):
     → Install chunks: [others' lives + comparison + lifestyle]
     → Gap direction: toward "lifestyle tôi chưa có"
     → Fill: consumption, travel, status display
     → ⚠️ Problematic: gap direction may be UNREALISTIC 
       (filtered reality → impossible Imagine-Final)
     → = Novelty.md §3: MXH hack phanh tự nhiên

  ④ CULTURE / RELIGION (văn hóa):
     → Install chunks: [shared values + rituals + meaning framework]
     → Gap direction: toward culturally-defined "good life"
     → Fill: following cultural path, rituals, community belonging
     → = Shared gap landscape = cultural identity
     → = Tại sao cultural values feel "natural" = 
       gaps installed early (Tier 2) → feel like Tier 1
```

### §8.3 — Ethical implications

```
🟡 GAP INSTALL ETHICS:

  GAP INSTALL ITSELF = NEUTRAL (tool, not inherently good/bad)

  ETHICAL khi:
    → Fill THẬT SỰ serve body-base (education → skills → resources)
    → Direction honest (product = what advertised)
    → Gap depth appropriate (not manufacturing desperation)

  PROBLEMATIC khi:
    → Fill KHÔNG serve body-base (addictive product, empty status)
    → Direction manipulated (filtered reality → impossible standard)
    → Gap depth artificially deepened (FOMO, scarcity tactics)
    → Exploit Tier 1 gaps (sex sells = hijack sexual gap for product)

  FRAMEWORK VIEW:
    → Hiểu gap install mechanism → hiểu TẠI SAO marketing works
    → Hiểu direction → hiểu TẠI SAO some products "feel right"
    → Hiểu "chưa biết = không gap" → hiểu TẠI SAO exposure matters
    → = Knowledge empowers BOTH creators AND consumers
```

---

## §9 — GAP DIRECTION × BACKGROUND PATTERN

### §9.1 — Background-Pattern constrains gap landscape

```
⭐ BACKGROUND PATTERN BIAS WHICH GAPS CAN FORM:

  Background-Pattern.md: Background-Pattern = accumulated chunk-network pattern
  → Hình thành qua years → invisible to PFC → bias ALL processing

  Background-Pattern × GAP DIRECTION:
    → Background-Pattern = deeply compiled chunk network THROUGHOUT brain
    → Background-Pattern's chunks ARE "surrounding chunks" for many potential gaps
    → = Background-Pattern constrains WHICH gaps can form and WHICH DIRECTIONS they point

  VD — Background-Pattern [effort → not enough]:
    → Mọi achievement-related chunks contaminated bởi [not enough]
    → Gap direction bias: "cần đạt MORE" (never enough)
    → EVEN WHEN đạt rồi → Background-Pattern create NEW gap: "chưa đủ"
    → = Chronic dissatisfaction = Background-Pattern constraining gap landscape
    → = "Chạy mãi không đến đích" = đích bị Background-Pattern DI CHUYỂN

  VD — Background-Pattern [connection → danger]:
    → Intimacy-related chunks contaminated bởi [danger]
    → Gap direction SUPPRESSED: gaps about deep connection KHÔNG HÌNH THÀNH
    → Hoặc: gap hình thành nhưng direction DISTORTED
      ("muốn connection" + [danger] → direction = "connection an toàn = control")
    → = Avoidant attachment = Background-Pattern suppress connection gap formation

  VD — Background-Pattern [expertise → identity]:
    → Expert's identity chunks linked to domain
    → Gap direction FOCUSED: gaps about domain = STRONG
    → Gaps about OTHER domains = WEAK (Background-Pattern doesn't support)
    → = "Chuyên gia chỉ biết chuyên môn" = Background-Pattern focus gap landscape
```

### §9.2 — Background-Pattern × gap direction resolution

```
🟡 THAY ĐỔI GAP LANDSCAPE CẦN THAY ĐỔI Background-Pattern:

  TẠI SAO KHÓ THAY ĐỔI:
    → Background-Pattern chunks = deeply compiled (years)
    → Background-Pattern chunks = bờ cũ → constrain gap direction CŨ
    → Install chunks MỚI → nhưng Background-Pattern chunks VẪN CÒN → conflict
    → = Gap direction shift bị Background-Pattern PULL BACK

  RESOLUTION (from Background-Pattern.md §10):
    → CANNOT fix Background-Pattern directly (too distributed, PFC invisible)
    → MUST build competing Background-Pattern → new chunks → new bờ → new gap directions
    → Takes YEARS (competing pattern must reach comparable density)
    → = Therapy = slowly build new chunk network → 
      new gap landscape emerges ALONGSIDE old one
    → Old Background-Pattern doesn't disappear — new Background-Pattern competes → probability shift

  VD:
    → Client Background-Pattern [effort → not enough]
    → Therapy: compile new chunks [effort → ok, rest ok, enough exists]
    → New chunks create new BỜ → new gaps possible:
      "muốn rest" (gap KHÔNG CÓ trước vì Background-Pattern suppress)
    → = Therapy = GAP LANDSCAPE EXPANSION via competing Background-Pattern
```

---

## §10 — ABSTRACT ACTIVITY × BODY-BASE

### §10.1 — The "hijack" question

```
⭐ "E=MC² PHỤC VỤ GÌ BODY-BASE?" — DEEP ANALYSIS:

  GIẢI THUYẾT: Abstract work (physics, art, math) dùng mechanism 
  evolved cho survival → body reward fires dù KHÔNG trực tiếp survival

  NHƯNG "HIJACK" GỢI Ý: mechanism bị dùng SAI, output KHÔNG serve body-base
  → Phân tích cho thấy: KHÔNG PHẢI "dùng sai" — là EXTENDED APPLICATION
```

### §10.2 — Evolution wired: inconsistency = danger

```
🟡 TIER 1 MECHANISM: INCONSISTENCY DETECTION

  Evolution selected:
    → Môi trường inconsistent = khó predict = nguy hiểm
    → Thú ăn thịt hành xử bất nhất → khó predict trajectory → dễ bị ăn
    → Genes wire: detect inconsistency → body discomfort → FIX IT → safety
    → = ACC (Anterior Cingulate Cortex) = inconsistency detector
    → 🟢 Bush, Luu, Posner 2000: ACC fires on conflict/error

  Mechanism properties:
    → KHÔNG phân biệt domain: ACC detect inconsistency BẤT KỲ
    → [con mồi đi lạ hướng] = inconsistency → body alert
    → [Newton ≠ Maxwell] = inconsistency → body alert
    → CÙNG ACC, CÙNG signal type
    → Body KHÔNG "biết" đây là physics — body chỉ biết "pattern không khớp"

  → = Tier 1 mechanism applied BEYOND original domain
  → Giống: hand evolved for grasping → ALSO used for writing, playing piano
  → = Extended application, NOT malfunction

  v2.0 NOTE — COMPILABLE ARCHITECTURE CONNECTION:
    → Compilable Architecture = general-purpose reward (Inter-Body §1)
    → General-purpose = SAME mechanism fires for ANY domain
    → = WHY abstract activity CAN fire body reward
    → Hardwired Architecture (insects): mechanism SPECIFIC per domain
      → Bee cannot feel "eureka" about physics
    → Compilable Architecture (humans): mechanism GENERAL
      → Human CAN feel "eureka" about abstract patterns
    → = Abstract gap fill is FEATURE of Compilable Architecture, not bug
```

### §10.3 — 2 con đường serve body-base

```
⭐ ABSTRACT ACTIVITY SERVE BODY-BASE QUA 2 CON ĐƯỜNG:

  CON ĐƯỜNG 1 — TRỰC TIẾP (internal state improve):
    → Inconsistency trong world model → body feels "unsafe" → cortisol
    → Resolve inconsistency → pattern coherent → body feels "safe" → opioid
    → = Body-base state THẬT SỰ improve:
      ✅ Cortisol giảm (inconsistency resolved)
      ✅ Opioid tăng (coherence reward)
      ✅ Sleep cải thiện (less pending → less cortisol holding)
    → = Body-base served TRỰC TIẾP, ĐỘC LẬP với outcome bên ngoài
    → = Einstein feel better NGAY KHI derive E=mc², trước khi anyone knows

  CON ĐƯỜNG 2 — GIÁN TIẾP (external outcome):
    → Abstract work → expertise → recognition → status → resources
    → Einstein: E=mc² → fame → academic position → resources → body-base
    → = NHƯNG đây là CONSEQUENCE, không phải REASON body reward fires
    → Body reward fires VÌ con đường 1 (gap fill)
    → Con đường 2 = bonus, thường arrives LATER

  TẠI SAO EVOLUTION KHÔNG "CẮT" ABSTRACT APPLICATION:
    → Vì: người giải abstract problems = SURVIVAL ADVANTAGE
    → Tool invention, strategic planning, prediction = abstract gap fill
    → Selection pressure: keep mechanism GENERAL → apply rộng
    → Restrict to survival-only → lose abstract capability → disadvantage
    → = "Feature, not bug" — generalizing gap detection = competitive edge
```

### §10.4 — Einstein full lifecycle (Gap Direction deep analysis)

```
⭐⭐ EINSTEIN = CASE HOÀN HẢO ĐỂ TEST GAP DIRECTION MECHANISM:

  Tại sao case này quan trọng:
  → Process kéo dài DECADES → thấy rõ direction EVOLVES
  → Multiple mini-arcs → thấy oscillation dynamics
  → Breakthrough + post-breakthrough → thấy perpetual loop
  → Verify cascade → thấy reward tầng tầng
  → = Test TOÀN BỘ Gap Direction mechanism end-to-end


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 0 — GAP DIRECTION BAN ĐẦU: MỜ                       │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Chunks: [Newton mechanics] + [Maxwell electromagnetism]    │
  │  Conflict: "tốc độ ánh sáng không khớp giữa 2 framework"   │
  │                                                             │
  │  Gap direction:                                             │
  │    = "CÁI GÌ ĐÓ giải mâu thuẫn này"                       │
  │    = Direction MỜ: chỉ biết "cần cái gì đó"               │
  │    = KHÔNG biết hình dạng cụ thể (chưa biết E=mc² tồn tại) │
  │    = §4.2 Specificity: BROAD (constraints lỏng)             │
  │                                                             │
  │  Analogy: biết "mảnh puzzle thiếu" nhưng CHƯA biết          │
  │  bức tranh tổng thể → chỉ biết constraints từ mảnh xung    │
  │  quanh (must be compatible với Newton AND Maxwell)           │
  │                                                             │
  │  Body signal: mild dissonance — "something doesn't fit"     │
  │  Imagine-Final: fuzzy — "unified framework nào đó"          │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 1-3 — OSCILLATION: reward + new dissonance (§7.5)   │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  MINI-ARC 1 — Photoelectric effect (1905):                  │
  │    Fill: photon model giải photoelectric → opioid ✅         │
  │    New chunks: [photon] + [wave-particle duality]           │
  │    New inconsistency: "photon model ≠ Maxwell continuous"   │
  │    Net: reward + MORE dissonance                            │
  │    Direction SHIFT: "cần gì đó RỘNG HƠN chỉ photoelectric" │
  │                                                             │
  │  MINI-ARC 2 — Special relativity (1905):                    │
  │    Fill: time dilation, length contraction → opioid ✅✅     │
  │    New chunks: [spacetime] + [Lorentz] + [E=mc²]           │
  │    New inconsistency: "SR KHÔNG handle gravity"             │
  │    Net: bigger reward + BIGGER dissonance                   │
  │    Direction SHARPEN: "cần geometric theory of gravity"     │
  │                                                             │
  │  MINI-ARC 3 — Grossman collaboration (1912-1914):           │
  │    Fill: tensor calculus tools → opioid ✅ ("this might fit")│
  │    New chunks: [tensor calculus] + [Riemannian geometry]    │
  │    New inconsistency: "equations gần đúng nhưng CHƯA hoàn  │
  │      toàn khớp"                                             │
  │    Net: moderate reward + ACCUMULATED dissonance cực cao     │
  │                                                             │
  │  TREND qua Phase 1-3:                                       │
  │    → Network physics: GROWS massively mỗi year              │
  │    → Gap direction: SHARPENS (fuzzy → "geometric gravity")  │
  │    → Total dissonance: TÍCH TỤ (rất nhiều chunks giá trị   │
  │      nhưng CHƯA THỐNG NHẤT)                                │
  │    → Body state: persistent mild-to-moderate dissonance     │
  │      + cortisol holding + Imagine-Final lặp cưỡng bức       │
  │    → = Conditions for COMPOUND BREAKTHROUGH building        │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 4 — BREAKTHROUGH: November 1915                      │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Field equations hoàn chỉnh:                                │
  │    → 1 framework UNIFY tất cả accumulated chunks            │
  │    → KHÔNG chỉ fill 1 gap — resolve ALL accumulated        │
  │      mini-inconsistencies ĐỒNG THỜI                         │
  │                                                             │
  │  Tại sao reward CỰC LỚN:                                   │
  │    ① Chunk-Gap fill: unified framework found → opioid       │
  │    ② Chunk-Miss reverse: YEARS of "chưa tìm ra" → "ĐÂY RỒI"│
  │    ③ Chunk-Shift: self-schema "tôi = người giải được"       │
  │    ④ Cortisol DROP: years of holding signal → RELEASED      │
  │    ⑤ Accumulated inconsistencies: ALL resolved at once      │
  │    = COMPOUND 5 dynamics → "intensely pleasant"                   │
  │                                                             │
  │  ⭐ Reward ∝ accumulated_dissonance × time_pending           │
  │           × network_size × all-at-once_resolution           │
  │  = Years × massive network × compound                       │
  │  = COMPOUND EXPLOSION, not single fill                      │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 4.5 — VERIFY CASCADE: reward TẦNG TẦNG              │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  TẦNG 1 — Self-verify (logic cá nhân):                      │
  │    Einstein tự check equations → "toán đúng"                │
  │    Body: coherent internally → opioid ✅                     │
  │    NHƯNG: still uncertain → residual anxiety                │
  │                                                             │
  │  TẦNG 2 — Friend-verify (Grossman, Besso, Hilbert):        │
  │    Share → họ check → "hợp lý"                              │
  │    Self-Pattern-Modeling: "người tôi tôn trọng CŨNG thấy đúng" → opioid ✅   │
  │    Trust dimension tăng → residual anxiety giảm              │
  │                                                             │
  │  TẦNG 3 — Community-verify (publish, peer review):          │
  │    Paper → physics community gradually confirm logic        │
  │    Mỗi confirmation = thêm 1 layer reward                   │
  │    Trust dimension continues growing                         │
  │                                                             │
  │  TẦNG 4 — Empirical-verify (1919 eclipse, Eddington):      │
  │    Light bends EXACTLY as predicted → reality itself confirms│
  │    Trust dimension MAXIMIZED: "không cần nghi ngờ nữa"      │
  │    = PEAK reward (Phase 5 > Phase 4 vì Trust complete)      │
  │    (04-Integration.md §6.6: Trust dimension analysis)       │
  │                                                             │
  │  Mechanism mỗi tầng:                                        │
  │    ⓐ Residual uncertainty giảm → cortisol drop → relief     │
  │    ⓑ Trust dimension tăng (Anchor-Schema.md §2)             │
  │    ⓒ Self-schema reinforced: "tôi THẬT SỰ đúng"            │
  │    ⓓ Social reward: recognition, status (con đường 2)       │
  │    = Reward không phải 1 lần — là CASCADE qua nhiều tầng    │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘


  ┌─────────────────────────────────────────────────────────────┐
  │  PHASE 5 — "NGHIỆN": PERPETUAL PURSUIT                     │
  ├─────────────────────────────────────────────────────────────┤
  │                                                             │
  │  Sau general relativity:                                    │
  │    Network physics: CỰC LỚN (biggest ever for 1 person)    │
  │    → Network LỚN → detect NEW inconsistency:               │
  │      "General relativity ≠ quantum mechanics"               │
  │    → NEW GAP: "unified field theory"                        │
  │    → = §7.5 oscillation: fill → new chunks → new gap       │
  │                                                             │
  │  TẠI SAO KHÔNG THỂ DỪNG — 5 mechanisms lock:               │
  │                                                             │
  │  ① NEW GAP INEVITABLE:                                      │
  │    Network lớn hơn → detect inconsistency mới → gap mới    │
  │    Câu hỏi KHÔNG BAO GIỜ HẾT vì mỗi answer = thêm chunks │
  │    = thêm detection capability (Novelty.md §5 combinatorial)│
  │                                                             │
  │  ② REWARD MEMORY (Background-Pattern):                      │
  │    Body compiled: [physics gap fill = MASSIVE opioid]       │
  │    Background-Pattern hình thành: [tìm kiếm vật lý = who I am]             │
  │    Body BIẾT: effort trong domain → reward CỰC LỚN possible│
  │    = Drive cực mạnh vì reward history cực sâu               │
  │                                                             │
  │  ③ GAP→MISS TRANSITION:                                     │
  │    "Unified field theory" gap → Imagine-Final preview lặp   │
  │    Preview compile thành baseline → body EXPECTS resolution │
  │    Chưa resolution → Chunk-Miss LIÊN TỤC → cortisol hold   │
  │    = KHÔNG THỂ dừng nghĩ về nó                              │
  │                                                             │
  │  ④ IDENTITY LOCKED:                                          │
  │    Self-schema: "tôi = nhà vật lý tìm unified theory"      │
  │    DỪNG research = identity threat → massive dissonance     │
  │    (Background-Pattern.md §10.4: Background-Pattern integrated into identity)│
  │                                                             │
  │  ⑤ DEPTH × SPECIFICITY TRAP:                                │
  │    Network cực deep + cực specific → gap cực narrow         │
  │    Very few possible fills → persistent → perpetual drive   │
  │    Einstein spent 30 YEARS (1925-1955) — KHÔNG tìm ra       │
  │    = Gap too deep + too narrow → unresolvable within        │
  │      lifetime → chronic pursuit                             │
  │                                                             │
  │  "CƠN NGHIỆN" = CÙNG mechanism như addiction:               │
  │    ① Reward history compiled deep → body expect reward      │
  │    ② Gap persistent → cortisol holding → can't stop         │
  │    ③ Identity locked → stopping = self-schema threat        │
  │    ④ Network grows → more gaps → more drive                 │
  │    KHÁC addiction: abstract gap fill SERVE body-base         │
  │    Addiction: fill KHÔNG serve body-base                     │
  │    = Cùng mechanism, khác outcome = Feature vs Bug           │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘
```

### §10.5 — Other cases

```
🟡 CASES KHÁC — ABSTRACT ACTIVITY × BODY-BASE:

  HỌC SINH HỌC TỐI NGÀY:
    Gap: "tương lai tốt hơn" (Imagine-Final compiled)
    Direction: toward academic success → career → resources
    Con đường 1: mỗi bài học = mini gap fill → micro opioid ✅
    Con đường 2: grades → opportunities → body-base future ✅
    ⚠️ NẾU học dưới threat cortisol → Con đường 1 bị poison
      (chunks compile với cortisol tag → "ghét học" dù vẫn drive)

  ĐI TỪ THIỆN (CHỈ CHO ĐI):
    Gap: Self-Pattern-Modeling fire → simulate recipient's need → body feel need ✅
    Direction: reduce other's suffering (gap via Compiled body simulation)
    Con đường 1: Self-Pattern-Modeling gap fill + oxytocin → body-state improve ✅
    Con đường 2: community standing → access → body-base ✅
    + Self-schema shift: "tôi = generous" → chunks compile → reward
    + Connection pathway ④ (Connection.md §8): giving = reward pathway
    = MULTIPLE reward channels override resource loss

  NGHỆ SĨ SÁNG TÁC:
    Gap: aesthetic vision not yet realized (creative gap)
    Direction: specific artistic expression
    Con đường 1: each creative step = mini gap fill → opioid ✅
    Con đường 2: art → recognition → resources (IF successful) ⚠️
    ⚠️ Con đường 2 uncertain → many artists persist 
      VÌ con đường 1 đủ strong
    = Explain: "starving artist" = con đường 1 reward > resource loss

  GIẢI SUDOKU:
    Gap: each empty cell = mini gap (network predict specific number)
    Direction: VERY specific (number X in cell Y)
    Con đường 1: fill cell → micro opioid → fill all → compound ✅
    Con đường 2: minimal (no status, no resources from Sudoku)
    = Almost purely con đường 1 — demonstrates abstract gap fill
      serve body-base TRỰC TIẾP without external outcome
```

---

## §11 — EXAMPLES (organized by property tested)

### §11.1 — Nhóm A: "Chưa biết = không có gap"

```
🟡 TEST: No chunks → no gap → no desire → no reward

  A1. EM BÉ 3 TUỔI NHẬN IPHONE 16 PRO MAX:
    Chunks about smartphone: ≈ 0
    Gap about iPhone: IMPOSSIBLE (no surrounding chunks)
    Nhận → curious (bấm→đèn sáng = sensory novelty)
    NHƯNG: không "pleasant vì có iPhone" → gap không tồn tại
    → Bố mẹ: chunks phong phú → gap → pleasant
    → CÙNG vật, KHÁC gap existence → KHÁC reward ✅

  A2. NGƯỜI CHƯA BIẾT CỜ VUA NHẬN BÀN CỜ ĐẮT:
    Chunks about chess: ≈ 0 → no gap "muốn bàn cờ đẹp"
    Nhận → "ồ, đẹp" (visual novelty) nhưng không reward sâu
    → Người chơi 10 năm: gap "bàn cờ chất lượng" → pleasant ✅

  A3. DÂN BẢN ĐỊA AMAZON NHẬN LAPTOP:
    Chunks digital technology: ≈ 0 → concept không tồn tại
    Nhận → curiosity → có thể dùng làm thớt
    → Gap about "laptop": IMPOSSIBLE ✅

  A4. CHƯA NGHE JAZZ ĐƯỢC TẶNG VÉ CONCERT JAZZ:
    Chunks jazz: minimal (label only) → gap gần như không tồn tại
    → Người yêu jazz 20 năm: specific gap → intensely pleasant ✅

  KẾT LUẬN: Tất cả 4 cases confirm — no chunks = no gap = no reward
```

### §11.2 — Nhóm B: "Cùng vật, sai hướng"

```
🟡 TEST: Direction mismatch → no reward dù category match

  B1. THÍCH TOÁN, ĐƯỢC TẶNG SÁCH VĂN HỌC ĐẮT:
    Gap direction: "sách toán hay" (math chunks phong phú)
    Sách văn: category "sách" ✅ nhưng direction "toán" ❌
    → Mild appreciation nhưng không gap-fill reward ✅

  B2. ĐANG KHÁT NƯỚC, ĐƯỢC TẶNG ĐỒ ĂN NGON:
    Gap direction: "nước" (Tier 1 dehydration → specific)
    Đồ ăn: satisfy hunger nhưng MISS thirst direction
    → Body VẪN signal "khát" dù ăn no ✅

  B3. MUỐN XE ĐỎ, ĐƯỢC XE CÙNG MODEL MÀU XANH:
    Gap direction: model X + MÀU ĐỎ (narrow specificity)
    Xe xanh: match 90% nhưng miss 10% (color dimension)
    → Reward CÓ nhưng "nhưng..." feeling = partial direction match ✅

  B4. THÍCH PHỞ BÒ, ĐƯỢC MỜI PHỞ GÀ:
    Gap direction: "phở bò tái" (specific compiled preference)
    Phở gà: "phở" ✅ nhưng "bò tái" ❌
    → Reward partial + "tiếc" nhẹ (miss direction) ✅

  KẾT LUẬN: Direction match required — category match NOT sufficient
```

### §11.3 — Nhóm C: "More ≠ better" (range exceeded)

```
🟡 TEST: Correct direction but BEYOND range → diminished/negative

  C1. MASSAGE:
    Direction: relaxation (Tier 1)
    Range: nhẹ→ok→pleasant→hơi đau→ĐAU (bell curve)
    → Cực mạnh: đúng direction nhưng VƯỢT range → nociception ✅

  C2. ÂM NHẠC VOLUME:
    Direction: auditory enjoyment (Tier 1)
    Range: nhỏ→vừa→enjoy→exciting→ĐAU tai
    → Cực lớn: cochlear damage → nociception override ✅

  C3. TIỀN THƯỞNG:
    Direction: resource reward
    Range: 1tr→10tr→100tr→1000 tỷ
    → 1000 tỷ: "không tin" → P4 violated (mismatch self-schema) ✅

  C4. KHEN:
    Direction: recognition (self-schema relevant)
    Range: "tốt đấy"→"giỏi"→"thiên tài"→"Einstein thứ 2"
    → "Einstein thứ 2": body reject (mismatch self-schema quá lớn) ✅

  C5. ĂN KẸO:
    Direction: sweet taste (Tier 1)
    Range: 1 cái→5 cái→10 cái→100 cái
    → 100 cái: receptor saturation + nausea + blood sugar alarm ✅

  C6. GIA VỊ ĐỒ ĂN:
    Direction: taste enhancement (Tier 1)
    Range: nhạt→vừa→ngon→quá mặn/cay→PAIN
    → x10 gia vị: nociception override taste reward ✅

  KẾT LUẬN: Bell curve per dimension — more ≠ better, even in correct direction
```

### §11.4 — Nhóm D: "Abstract gap fill"

```
🟡 TEST: Abstract activity fills gap → body reward despite no direct survival value

  D1. GIẢI SUDOKU:
    Gap: each empty cell = mini gap, network predict specific number
    Direction: "số X ở ô Y" (very specific, very narrow)
    Fill each cell → micro opioid. Complete → compound reward.
    → Cho người không biết Sudoku → no chunks → no gap → no drive ✅

  D2. ĐỌC TIỂU THUYẾT:
    Gap: "chuyện gì xảy ra tiếp?" (plot creates directed gap)
    Direction: character fate prediction (Self-Pattern-Modeling-based)
    Plot twist → prediction wrong → prediction-delta → new gap → fill → reward
    → Tác giả = gap direction engineer (create→fill→create loop) ✅

  D3. SƯU TẦM TEM:
    Gap: "con tem X từ năm Y" (extremely narrow direction)
    Fill: find specific stamp → gap fill → opioid
    Complete set = all gaps closed = massive compound
    → Người ngoài: "mấy cái tem cũ" → no chunks → no gap → no reward ✅

  D4. CHƠI GAME RPG:
    Gap: quests, levels, items = engineered gap system
    Direction: game designers CREATE gap directions deliberately
    Level up → self-schema shift (avatar = proxy self) → reward
    → Game = artificial gap-direction factory ✅

  KẾT LUẬN: Abstract gaps use SAME mechanism — gap fill → opioid
  regardless of survival relevance
```

### §11.5 — Nhóm E: "Paradoxical reward"

```
🟡 TEST: Reward ở chỗ naive model predict KHÔNG reward

  E1. XEM PHIM BUỒN → KHÓC → NHƯNG "HAY":
    Self-Pattern-Modeling Compiled: body simulate nhân vật → buồn THẬT
    Gap: about human condition → film articulates → gap fill
    + Safety frame: "đây là phim" → body process risk-free
    = Buồn (body simulate) + reward (gap fill) + safety → MIX ✅

  E2. ĂN ỚT (CAPSAICIN):
    Nociceptors fire → PAIN signal
    Body respond: endorphin release → opioid
    + Compiled chunks after exposure: [cay = pleasant sau đau]
    → Lần đầu: KHÔNG pleasant (chưa compiled)
    → Sau exposure: direction SHIFT: [cay → endorphin → pleasant] ✅

  E3. TẬP GYM ĐAU CƠ:
    Tập: nociception (muscle strain)
    Sau tập: endorphin + sense of accomplishment
    Imagine-Final: body fit → gap "body hiện tại vs body mong muốn"
    Mỗi buổi tập = partial gap fill toward Imagine-Final ✅

  E4. CHO TIỀN NGƯỜI LẠ (CHARITY):
    Body mất resources → naive: should be NEGATIVE
    Self-Pattern-Modeling Compiled → simulate recipient happy → body mirror → opioid
    + Connection pathway ④ (giving reward)
    + Self-schema: "tôi = generous" → positive shift
    + Community mechanism: giving → others value you → access
    = MULTIPLE reward channels > resource loss ✅

  KẾT LUẬN: Paradoxical rewards explained — multiple gaps/channels 
  interact, not just "stimulus → single response"
```

### §11.6 — Summary matrix

```
  ┌─────────┬───────────────────────────────────┬─────────────┐
  │ Nhóm    │ Test                              │ Confirmed?  │
  ├─────────┼───────────────────────────────────┼─────────────┤
  │ A (4)   │ No chunks → no gap → no reward    │ ✅ All 4    │
  │ B (4)   │ Wrong direction → no reward        │ ✅ All 4    │
  │ C (6)   │ Beyond range → diminished/negative │ ✅ All 6    │
  │ D (4)   │ Abstract gap fill → body reward    │ ✅ All 4    │
  │ E (4)   │ Paradoxical → multi-channel        │ ✅ All 4    │
  ├─────────┼───────────────────────────────────┼─────────────┤
  │ TOTAL   │ 22 examples tested                │ ✅ All 22   │
  └─────────┴───────────────────────────────────┴─────────────┘

  Không tìm được counter-example.
```

---

## §12 — GAP DIRECTION × INTER-BODY: BY-PRODUCT MATCH + 2-STREAM (★ NEW v2.0)

### §12.1 — Gap direction = foundation cho by-product match

```
⭐⭐ BY-PRODUCT MATCH CHỈ HOẠT ĐỘNG NẾU CÓ GAP DIRECTION:

  Inter-Body-Mechanism.md §5.4:
    "Entity B fill gap CỦA B → output = by-product"
    "Khi by-product match gap direction CỦA A → A receives reward"

  ANALYSIS QUA GAP DIRECTION:
    → "Match" = B's output fits THE SPECIFIC SHAPE of A's gap
    → KHÔNG phải "B did something nice" (vague)
    → = B's output match A's gap's DIRECTION + SPECIFICITY + RANGE
    → = Gap direction is THE EVALUATOR for by-product match

  TẠI SAO CẦN GAP DIRECTION ĐỂ HIỂU BY-PRODUCT MATCH:

    ① WITHOUT gap direction: "B output → A reward" = magic
       → Tại sao CÙNG output B → A1 reward, A2 nothing, A3 annoyance?
       → = Không có explanatory mechanism

    ② WITH gap direction: "B output match A's specific direction → A reward"
       → A1 reward: B's output match A1's gap direction ✅
       → A2 nothing: B's output irrelevant to A2's gap directions
       → A3 annoyance: B's output CONFLICTS A3's gap direction (anti-match)
       → = CLEAR mechanism. Testable. Per-person.

  VÍ DỤ TRIPLE-CASE:
    B = Ca sĩ hát live
    B's gap: "muốn thể hiện, muốn khán giả thích" → action = hát
    B's output = bài hát (by-product of filling B's gap)

    A1 (fan 10 năm): gap direction = "nghe bài Y live từ ca sĩ B"
      → Output match direction EXACTLY → massive reward ✅
    A2 (đi cùng bạn, không biết ca sĩ): gap direction ≠ music domain
      → Output = irrelevant → no gap-fill reward (maybe mild novelty)
    A3 (hàng xóm muốn yên tĩnh): gap direction = "quiet evening"
      → Output = loud music → CONFLICTS direction → annoyance (anti-match) ❌

    = CÙNG output (bài hát). 3 GAP DIRECTIONS khác nhau. 3 OUTCOMES khác nhau.
    = Gap direction = THE mechanism explaining selectivity of by-product match.


  ⭐ ANTI-MATCH = NOT JUST "NO MATCH" — ACTIVE DIRECTION CONFLICT:

    No-match: B's output irrelevant to A's gap (neutral — no reward, no harm)
      VD: ca sĩ hát → người không quan tâm → nothing happens
    
    Anti-match: B's output ACTIVELY OPPOSES A's gap direction
      VD: CEO đổi mới → nhân viên gap "ổn định" → change = THREATS stability
      VD: extrovert loud → introvert gap "quiet" → noise = CONFLICTS direction
      
    Anti-match is WORSE than no-match:
      → No-match = 0 reward (neutral)
      → Anti-match = NEGATIVE (active dissonance, threat signal)
      → = Output pushes A FURTHER from gap fill
      → = Body-feedback: dissonance + possible cortisol (if persistent)

🟡 Gap direction as by-product match foundation = framework synthesis.
   Each component established separately — integration = contribution.
```

### §12.2 — 2-Stream Architecture × Gap Direction

```
⭐ STREAM 1 VÀ STREAM 2 = 2 LOẠI GAP DIRECTION MATCH:

  (By-Product-Gap-Resonance.md v1.0 §2)

  STREAM 1 × GAP DIRECTION:
    = Hardware-level gap directions matched by EXISTENCE/THUỘC TÍNH

    Mechanism:
      Entity B TỒN TẠI / CÓ THUỘC TÍNH X
      → X match A's gap direction (hardware or compiled)
      → A reward fires
      B KHÔNG CẦN LÀM GÌ.

    Gap direction involved:
      → Tier 1 (hardware): baby schema, sexual attractiveness, voice timbre
      → Tier 2-3 (compiled): status patterns, aesthetic preferences
      → Direction evaluation: mostly COMPILED (automatic hardware check)

    Properties:
      → UNIDIRECTIONAL: A has gap, B's existence fills it. No loop.
      → HABITUATES: constant stimulus → Weber-Fechner → direction "tắt dần"
        (body adjusts baseline → same stimulus = smaller delta)
      → MULTI-CHANNEL: beauty + voice + smell = multiple directions matched

    VD:
      Chồng gap "aesthetic pleasure" → vợ xinh = Hardware-Stream match
      Mẹ gap "caregiving fulfillment" → bé cute (baby schema) = Hardware-Stream match
      Fan gap "novelty + beauty" → ca sĩ performance = Hardware-Stream match


  STREAM 2 × GAP DIRECTION:
    = Self-Pattern-Modeling-mediated gap directions matched by ACTIONS (mutual)

    Mechanism:
      A's Self-Pattern-Modeling detect B's state → A respond phù hợp
      → A's RESPONSE = by-product of A filling A's gap "hiểu B"
      → A's response match B's gap direction "được hiểu"
      → B reward → B respond → B's response match A's gap "được hiểu lại"
      → = MUTUAL by-product match via Self-Pattern-Modeling-mediated actions

    Gap direction involved:
      → Tier 2-4 (compiled): understanding, emotional resonance, shared meaning
      → Direction evaluation: Compiled (experts in each other) hoặc
        Fresh (still learning each other)

    Properties:
      → BIDIRECTIONAL: CẦN cả 2 match nhau's gap directions
      → ANTI-HABITUATION: Hebbian → more practice → better match → MORE reward
        (direction matching IMPROVES → reward INCREASES over time)
      → Can CHANGE gap direction: deep Modeling-Stream → A can help B see new gaps
        ("bạn thân nói 1 câu thay đổi cách nhìn" = install chunks → new direction)

    VD:
      Bạn thân A: gap "được hiểu mà không cần giải thích"
        → B Self-Pattern-Modeling compiled → respond EXACTLY matching → A massive reward
      Therapist: gap direction "help client see clearly"
        → Client Self-Pattern-Modeling reciprocate → therapist reward (mutual Modeling-Stream)


  TEMPORAL DYNAMIC:
    Hardware-Stream: PEAKS EARLY → habituates (hedonic treadmill)
    Modeling-Stream: ZERO at start → grows → deepens → can become STRONGEST

    Total direction-match reward = Hardware-Stream + Modeling-Stream (independent, parallel)
    Sustainable relationships: Modeling-Stream growth > Hardware-Stream decline
    Failing relationships: Hardware-Stream habituated + Modeling-Stream never developed

🟡 2-Stream × gap direction = framework synthesis.
   Hedonic adaptation (Hardware-Stream) = 🟢.
   Interpersonal synchrony (Modeling-Stream) = 🟢 (Feldman 2007, Coan & Sbarra 2015).
```

### §12.3 — Compilable Architecture × Gap Direction: general-purpose evaluation

```
⭐ COMPILABLE ARCHITECTURE = WHY GAP DIRECTION IS NOT FIXED:

  (Inter-Body-Mechanism.md §1, Body-Base.md v3.1)

  Hardwired Architecture (insects):
    → Hardwired reward: flower wavelength X → approach
    → Gap direction = FIXED by genes per species
    → ALL members = SAME gap directions (bee 1 = bee 2)
    → = CANNOT explain personal reward differences

  Compilable Architecture (humans):
    → General-purpose reward: ANY compiled gap fill → reward
    → Gap direction = EMERGED from accumulated chunk network
    → Each person = UNIQUE gap directions (different chunks compiled)
    → = EXPLAINS personal reward differences PERFECTLY

  IMPLICATIONS FOR INTER-BODY:
    → Compilable Architecture = WHY by-product match is SELECTIVE
      (mỗi người có different directions → different matches)
    → Compilable Architecture = WHY relationships are PERSONAL
      (my directions overlap SOME people, not others)
    → Compilable Architecture = WHY cultural bonding works
      (shared chunk install → shared directions → easier match)
    → Compilable Architecture = WHY diversity valuable
      (different directions → different outputs → richer by-product landscape)

  INTER-BODY CONSEQUENCE:
    → A and B have gap directions determined by THEIR chunk networks
    → Match probability = f(overlap in gap direction landscape)
    → Species hardware = SOME overlap guaranteed (Tier 1 shared)
    → Culture = ADDITIONAL overlap (Tier 2-3 shared install)
    → Personal experience = DIVERGENCE (Tier 4 individual)
    → = WHY "cùng nhóm nhưng KHÁC mức kết nối" = different Tier 4 overlap
```

### §12.4 — 3 Independent Cost Sources × Gap Direction

```
🟡 3-COST MODEL APPLIES TO GAP DIRECTION EVALUATION:

  (Inter-Body-Mechanism.md §4)

  KHI EVALUATE BY-PRODUCT MATCH:

    ① PFC DRAFT COST — "B's output match my direction không?"
       → If COMPILED: cost ≈ 0 (body knows instantly)
         VD: bạn thân nói → body BIẾT match hay không (milliseconds)
       → If FRESH: cost HIGH (PFC phải build evaluation)
         VD: stranger's proposal → PFC analyze fit (seconds-minutes)
       → = Expert in relationship → lower evaluation cost

    ② SUPPRESS COST — "Output miss my direction → must suppress reaction"
       → Anti-match → body fires dissonance → want to react (withdraw/fight)
       → Social context requires suppress → PFC override → glucose
       → VD: CEO change → employee SUPPRESS frustration daily = costly
       → = Chronic direction-mismatch + suppress = burnout trajectory

    ③ UNCERTAINTY COST — "Will B's output match my direction?"
       → Unknown entity: can't predict → cortisol
       → Known entity: predict accurately → low uncertainty
       → = WHY familiar = comfortable (direction-match predictable)
       → = WHY new = stressful even if ultimately good

  SUSTAINABILITY:
    → Low all 3 costs = sustainable interaction (bạn thân compiled)
    → High ① = new territory (learning phase — acceptable if temporary)
    → High ② = chronic mismatch (→ burnout, need to exit)
    → High ③ = instability (→ anxiety until resolved)
    → = Gap direction match QUALITY determines interaction sustainability
```

### §12.5 — Input Channel Control × Gap Direction

```
🟡 5-CHANNEL INPUT VECTOR DETERMINES WHICH GAP DIRECTIONS ACTIVATE:

  (Inter-Body-Mechanism.md §6)

  5 CHANNELS:
    Ch1: Hardware Sensory (visual, auditory, touch, smell, taste)
    Ch2: Body State (hunger, fatigue, hormone level)
    Ch3: Compiled Chunks (activated patterns from memory)
    Ch4: Entity Actions (other entities' observable behaviors)
    Ch5: PFC Active Chain (deliberate thoughts, plans, predictions)

  × GAP DIRECTION:
    → Gap direction activation DEPENDS on which channels active
    → Ch1 dominant (sensory-rich): Tier 1 gap directions activate
      VD: music concert → auditory → Tier 1 aesthetic gaps fire
    → Ch3 dominant (memory-triggered): Tier 2-4 gap directions activate
      VD: reunion → compiled friend-chunks fire → Modeling-Stream gaps activate
    → Ch4 dominant (entity-focused): by-product match evaluation active
      VD: observe B's actions → evaluate match/mismatch to my directions
    → Ch5 dominant (PFC-driven): abstract gap directions active
      VD: planning → Tier 4 career/knowledge gaps fire

  INTER-BODY APPLICATION:
    → Entity B primarily enters via Ch1 + Ch4 (perceive + observe actions)
    → WHICH gap directions B can match = limited by available channels
    → Text-only communication: Ch5 dominant, Ch1 minimal
      → Only match abstract/intellectual gap directions
    → In-person: Ch1 + Ch3 + Ch4 full → match wider range of directions
      → Hardware-Stream (Ch1: beauty, voice) + Modeling-Stream (Ch4: responsive actions)
    → = WHY in-person > text for deep bonding (more channels = more matches)

  MANIPULATION = CONTROL CHANNELS TO DISTORT GAP DIRECTION:
    → Propaganda: Ch4 (social proof) + Ch5 (arguments) → install specific direction
    → Advertising: Ch1 (beauty) + Ch4 (influencer) → associate product with direction
    → Gaslighting: Ch4 (entity actions) + Ch5 (reframe) → distort existing directions
    → = Power = control over WHICH directions get activated
    → = Inter-Body-Mechanism.md §6: "Input Channel Control = Power"
```

---

## §13 — IMPLICATIONS

### §13.1 — Education

```
🟡 GIÁO DỤC PHẢI BUILD CHUNKS TRƯỚC, PRESENT ANSWERS SAU:

  HIỆN TRẠNG PHỔ BIẾN:
    → Giáo viên trình bày đáp án → học sinh ghi nhận → test
    → = "Cho đáp án khi chưa có câu hỏi" → no gap → no reward → boring

  GAP DIRECTION APPROACH:
    ① Build chunks: giới thiệu concepts, examples, experiences
    ② Create conflict: show inconsistency, pose problem
    ③ Gap emerges: student FEELS "thiếu gì đó" (direction forms)
    ④ Present tools: guide toward answer (not give answer)
    ⑤ Student fills gap: discovery → opioid → intrinsic motivation
    → = Gap direction mechanism = natural curiosity driver
    → = "Build the question before giving the answer"
```

### §13.2 — Therapy

```
🟡 THERAPY = MAP AND EXPAND GAP LANDSCAPE:

  DIAGNOSIS: Map client's gap direction landscape
    → Which gaps active? (what they want)
    → Which gaps suppressed? (what Background-Pattern prevents)
    → Which gap directions distorted? (Background-Pattern contamination)

  INTERVENTION:
    → Build new chunks → expand gap landscape possibilities
    → Identify Background-Pattern constraints → build competing patterns
    → Sharpen fuzzy directions → Imagine-Final refinement
    → = Therapy KHÔNG "fix" gaps — therapy ENABLES new gaps

  VD: Client "muốn hạnh phúc nhưng không biết muốn gì":
    → = Fuzzy gap direction (network sparse or conflicted)
    → Therapy: explore → build chunks → direction sharpens
    → NOT: prescribe "happiness = X" (install someone else's direction)
```

### §13.3 — Marketing (ethical vs exploitative)

```
🟡 HIỂU GAP INSTALL → HIỂU MARKETING:

  ETHICAL MARKETING:
    → Product THẬT SỰ fills genuine gap → honest direction install
    → VD: "Bạn có vấn đề X → sản phẩm solve X" → gap direction = X → fill = product

  EXPLOITATIVE MARKETING:
    → Create ARTIFICIAL gap → fill with unnecessary product
    → VD: "Bạn thiếu status" → install [status = product X] → purchase X
    → Gap was manufactured, not genuine body-need

  CONSUMER DEFENSE:
    → Recognize: "Am I buying because GAP is REAL or INSTALLED?"
    → "Chưa biết = không gap": before ad, I had NO desire → ad INSTALLED gap
    → = Awareness of mechanism = partial immunity
```

### §13.4 — Parenting

```
🟡 PARENTING: HIỂU CHILD'S GAP DIRECTION ≠ PARENT'S:

  Ô Tô Paradox (03-Reward.md §5):
    → Bố thích xe cổ (bố's gap direction)
    → Con thích xe thời thượng (con's gap direction)
    → Bố mua xe cổ cho con = fill BỐ'S gap, MISS con's gap

  PARENTING IMPLICATION:
    → "Perfect gift" = match CHILD's gap direction
    → Requires: understand child's chunk network → infer gap direction
    → CANNOT assume: "tôi thích → con cũng thích"
    → CAN help: build chunks cho con → gap direction develop naturally

  v2.0 NOTE — BY-PRODUCT MATCH IN PARENTING:
    → Parent fill parent's gap "nuôi con tốt" → output = choices
    → Output = by-product of parent's gap direction ("tốt" = parent's definition)
    → IF parent's "tốt" definition match child's gap directions → child thrives
    → IF parent's "tốt" = parent's projection → MISS child's directions
    → = Ô Tô Paradox = by-product mismatch in parent-child
    → Solution: Self-Pattern-Modeling toward child → detect CHILD's gap directions → adjust output
```

### §13.5 — AI era

```
🟡 AI CAN HELP IDENTIFY + ARTICULATE GAP DIRECTIONS:

  AI strengths aligned:
    → Gap direction often IMPLICIT (body knows, PFC can't articulate)
    → AI CAN detect patterns in behavior → infer gap direction
    → AI CAN suggest: "based on your interests, your gap might be..."
    → = AI as gap direction articulation assistant

  AI limitations:
    → AI CANNOT feel gap (no body-base)
    → AI CAN mis-infer direction (chunks insufficient)
    → AI suggestions MUST be body-checked by user
    → = 3-tầng (AI-Schema-Detection.md): AI detect → expert verify → 
      client body-check

  v2.0 NOTE — AI × BY-PRODUCT MATCH:
    → AI output = by-product of "fill user's query" (AI's "task")
    → User evaluate: "AI output match MY gap direction?"
    → Body-check: does answer FEEL right? (compiled evaluation)
    → Domain-check: does answer WORK? (reality arbiter)
    → = Dual Check applies to AI output exactly like human by-product
```

---

## §14 — OPEN QUESTIONS

```
GD-Q1: Gap direction CHANGE dynamics:
  → How fast does direction shift when new chunks compile?
  → Is there a "critical mass" of new chunks for direction shift?
  → Does Background-Pattern inertia slow direction change proportionally?
  → 🔴 No direct experimental data on direction shift rate

GD-Q2: Gap direction CONFLICT:
  → Can 2 gaps exist in same domain with DIFFERENT directions?
  → VD: "muốn xe thể thao" + "muốn xe tiện dụng" = 2 gaps compete?
  → How does body resolve when 2 gap directions pull OPPOSITE?
  → Connection to Schema.md §5.1 (schema conflict)?
  → 🔴 Needs further analysis

GD-Q3: Tier 1 gap direction MODIFIABILITY:
  → Can evolutionary gap directions be OVERRIDDEN?
  → VD: hunger gap direction → fasting practice override?
  → Or just: suppress signal temporarily, direction unchanged?
  → 🔴 Partially addressed by cultural practices (fasting, asceticism)

GD-Q4: Exact REWARD MAGNITUDE formula:
  → Reward = f(direction_match × specificity × depth × range)
  → But exact formula? Linear? Multiplicative? Threshold-based?
  → 🔴 Framework synthesis, not experimentally derived

GD-Q5: Gap direction × SLEEP:
  → Does sleep REFINE gap shape? (gist extraction → direction sharpen?)
  → Does sleep CREATE new gaps? (replay → detect new inconsistencies?)
  → Connection to Background-Pattern.md §4 (sleep = accelerator)?
  → 🟡 Plausible from existing sleep literature, not specifically tested

GD-Q6: Gap direction INHERITANCE across generations:
  → Can gap direction landscape be TRANSMITTED?
  → Via: parenting (chunk install) + culture (shared chunks) + epigenetics?
  → VD: family values = shared gap direction landscape?
  → 🟡 Cultural transmission established, epigenetic mechanism speculative

GD-Q7 (v2.0 NEW): By-product match OPTIMIZATION:
  → Can entities LEARN to produce by-products that match others' directions?
  → Modeling-Stream Self-Pattern-Modeling = exactly this (learn partner's direction → respond better)
  → Is there a "market" for direction-matching (economic analogy)?
  → 🟡 Self-Pattern-Modeling compilation = learning direction-matching (established)

GD-Q8 (v2.0 NEW): Anti-match ACCUMULATION:
  → Does repeated anti-match CHANGE gap directions?
  → VD: employee in toxic workplace → gap direction SHIFTS to "escape"?
  → Or: Background-Pattern forms around anti-match → direction DISTORTS?
  → 🔴 Plausible (chronic stress literature) but not specifically formalized
```

---

## §15 — HONEST ASSESSMENT

```
🟢 HIGH CONFIDENCE (established research supports):

  → Gap = hole in chunk network: established (Loewenstein 1994 information gap,
    Festinger 1957 cognitive dissonance, Kounios & Beeman 2009 aha moments)
  → Prediction error as signal mechanism: Schultz 1997
  → ACC conflict detection: Bush, Luu, Posner 2000
  → Reward is personalized: demonstrated across H10 cases (03-Reward §5)
  → Goldilocks zone: Berlyne 1960, 1971 (optimal arousal theory)
  → Hedonic adaptation (range): Brickman et al. 1978
  → External chunk install: established (education, advertising, social influence)
  → Background-Patterns bias processing: implicit learning literature
  → Interpersonal synchrony: Feldman 2007
  → Social co-regulation: Coan & Sbarra 2015

🟡 FRAMEWORK SYNTHESIS (novel integration of established components):

  → Gap direction as explicit property: LOGICAL CONSEQUENCE of "gap = hole"
    → Each component established — formalization = framework contribution
  → "Chưa biết = không có gap" as genesis principle:
    → Implicit in H10 P2 — explicit formulation = framework contribution
  → 2-layer model (signal vs content):
    → Each layer established individually — distinction = framework contribution
  → Unified direction model (Tier 1-4):
    → Each tier established — unified substrate = framework contribution
  → 4 properties (direction, specificity, depth, range):
    → Each observable — taxonomy = framework contribution
  → Gap direction install:
    → F3 established — application to gap creation = framework contribution
  → Background-Pattern × gap direction landscape:
    → Both concepts established — interaction = framework contribution
  → Abstract activity serve body-base via 2 pathways:
    → Each pathway described — explicit 2-pathway model = framework contribution
  → v2.0: Gap direction = by-product match foundation:
    → Gap direction + by-product match both established separately
    → Integration: "match = direction match" = logical, testable
  → v2.0: 2-Stream × gap direction:
    → Hardware-Stream = hardware direction match (unidirectional, habituates)
    → Modeling-Stream = Self-Pattern-Modeling direction match (mutual, deepens)
    → Each stream established — gap direction lens = framework contribution
  → v2.0: Compilable Architecture × gap direction diversity:
    → General-purpose reward → gap directions emerge from chunks (not hardwired)
    → = Explains personal reward differences
  → v2.0: 3-cost × gap direction evaluation:
    → Each cost established — application to direction evaluation = integration
  → v2.0: Compiled/Fresh gap direction evaluation:
    → Dual-process (compiled/fresh) = 🟢 — application to gap = synthesis

🔴 HYPOTHESIS (needs further analysis):

  → Exact gap direction change dynamics (speed, critical mass, Background-Pattern inertia)
  → Gap direction conflict resolution mechanism
  → Tier 1 gap direction modifiability
  → Exact reward magnitude formula (direction_match × specificity × depth × range)
  → Sleep × gap direction refinement
  → Intergenerational gap direction transmission
  → v2.0: By-product match optimization dynamics
  → v2.0: Anti-match accumulation and direction distortion


SUMMARY:
  🟢 10 established  (research-supported components)
  🟡 14 synthesis    (novel integration — logical, consistent, productive)
  🔴 8 hypothesis    (plausible, needs further analysis/evidence)

  OVERALL ASSESSMENT:
  → Core claim "gap has direction" = 🟢🟡 (logical necessity + consistent)
  → "Chưa biết = không gap" = 🟡 (logical, needs explicit test)
  → 2-layer model = 🟡 (clarifying, each layer established)
  → Formalization = 🟡 (framework contribution, not new discovery)
  → v2.0: By-product match × gap direction = 🟡 (logical integration)
  → v2.0: 2-Stream × gap direction = 🟡 (each component established)
  → Specifics (formula, dynamics) = 🔴 (speculative)

  → Giả thiết của user ĐÚNG ở core claim
  → File này formalize what was implicit → make usable for analysis
  → v2.0: CONNECT gap direction to inter-body framework (by-product match + 2-Stream)
```

---

## §16 — CROSS-REFERENCES

### §16.1 — Core mechanism files

```
  Body-Feedback-Mechanism.md v2.0  — §3.3 Chunk-Gap (extends), §3.1-§3.2 (Shift/Miss),
                                     §1 Body-Need aggregate
  Body-Feedback.md v2.0           — §6 H10 (reinterprets qua 2 layers)
  Body-Feedback-Label.md v2.0     — §2 Foundation terms, §4 dissonance labels,
                                     §8 Compiled/Fresh processing
  Inter-Body-Mechanism.md v1.0    — §2 Body-Need direction, §5 by-product match + Full Chain,
                                     §1 Compilable Architecture, §3 Compiled/Fresh, §4 3-cost,
                                     §6 5-Channel Input Vector
  03-Reward.md                    — §5 Ô Tô Paradox (perfect test case), §6 Van Gogh
  04-Integration.md               — §6-8 Einstein/hedonic/trauma walkthroughs
  Chunk.md v2.0                   — §1-§4 substrate, §2 compile, §2 calibration tiers
  Background-Pattern.md v1.0      — §6 Background-Pattern×Self-Pattern-Modeling, §10 resolution (extends via §9)
```

### §16.2 — Agent-Mechanism files

```
  By-Product-Gap-Resonance.md v1.0       — §2 2-Stream Architecture, §1.5 by-product match,
                                     §2.4 anti-match
  Self-Pattern-Modeling.md v3.0      — §1 Compiled/Fresh, Compiled/Fresh processing, Modeling-Stream mechanism
  Body-Coupling.md v2.0           — coupling direction, Entity-Compiled subtypes
  Valence-Propagation.md v2.0     — §3 Entity-Compiled (positive/negative/mixed)
```

### §16.3 — Observation files

```
  Novelty.md v1.0                 — §1 Chunk-Gap = foundation, §4 loop dynamics
  Schema.md v2.0                  — §4.1 depth (extends), §5.1 conflict
  Gratitude.md v1.0               — H10 applied to gifts (gap prerequisite)
  Connection.md v3.3              — §8 giving pathway, altruism mechanism
  Body-Base.md v3.1               — Compilable Architecture (3 foundations), entry point
```

### §16.4 — PFC + processing files

```
  Imagine-Final.md                — Preview → direction sharpens (§7.2)
  Somatic-Articulation-Loop.md    — Felt sense = body detects gap direction 
                                    trước PFC verbal label
  Cortisol-Baseline.md v2.0       — Direction tag (novelty vs threat cortisol)
  Ask-AI.md v3.1                  — Dual Check (body=quality controller, domain=arbiter)
```

### §16.5 — Key research

```
  🟢 Schultz, Dayan, Montague 1997 — reward prediction error (Layer 1)
  🟢 Bush, Luu, Posner 2000      — ACC conflict/error detection
  🟢 Loewenstein 1994             — information gap theory of curiosity
  🟢 Festinger 1957               — cognitive dissonance
  🟢 Kounios & Beeman 2009        — aha moments + ACC
  🟢 Gendlin 1978                 — felt sense (body detect before verbal)
  🟢 Berlyne 1960, 1971           — optimal arousal theory (Goldilocks)
  🟢 Brickman et al. 1978         — hedonic adaptation
  🟢 Amabile & Kramer 2011        — progress principle (mini-arc reward)
  🟢 Feldman 2007                 — interpersonal synchrony (Modeling-Stream)
  🟢 Coan & Sbarra 2015           — social co-regulation, social baseline theory
  🟢 Kahneman 2011                — dual-process (compiled/fresh parallel)
  🟢 Eisenberger 2003             — social pain = physical pain circuits
  🟢 Panksepp 1998                — social play reward = food reward circuits
```

### §16.6 — Health Conditions Drill (v1.1)

```
  AUTISM SPECIAL INTERESTS = CONCENTRATED GAP-DIRECTION:
    → Autism-Observation.md §6: Special Interests = same gap-direction mechanism, concentrated
    → Monotropic attention (Murray 2005) → gap-direction resources FOCUSED on 1-2 domains
    → "Feature not bug" — same Chunk-Gap drive, different DISTRIBUTION of attention
    → = Clinical validation: gap-direction explains WHY Special Interests are intensely rewarding
      (narrow gap + deep surrounding chunks → very specific direction → high reward on match)

  Cross-refs:
    → Autism-Observation.md v1.0 §6 (Special Interests mechanism)
    → ADHD-Observation.md v1.2 §4 (hyperfocus = related but different: dopamine-sustained)
```

---

> *Gap-Direction.md v2.0 — "Gap trong chunk network có HƯỚNG CỤ THỂ.*
> *Direction = f(surrounding chunk network structure).*
> *Chưa biết = không có gap = bạn không thể thiếu thứ bạn không biết tồn tại.*
> *Prediction error = signal mechanism (Layer 1).*
> *Gap direction = content evaluation (Layer 2).*
> *Reward = direction match quality, not just 'fill gap or not'.*
> *1 model thống nhất cho toàn bộ reward mechanism: Tier 1-4 cùng substrate.*
>
> *v2.0: Gap direction = WHY by-product match works.*
> *B fill gap CỦA B → output match A's gap DIRECTION → A reward.*
> *2-Stream: Hardware-Stream = hardware direction match. Modeling-Stream = Self-Pattern-Modeling mutual direction match.*
> *Compilable Architecture: gap directions EMERGE from chunks (not hardwired) = WHY personal."*

---

## CHANGELOG

```
v1.0 (2026-04-27):
  → File mới. Gap direction formalized. 4 properties. "Chưa biết = không gap."
  → 2-layer model. Unified Tier 1-4. 22 examples. Einstein full lifecycle.

v1.1 (2026-05-15):
  → §15 Autism Special Interests validation (Murray 2005).
  → Health Conditions Drill cross-refs (Autism-Observation, ADHD-Observation).

v2.0 (2026-05-17):
  → FULL REWRITE — Inter-Body Drill propagation (Phase 9).
  → NEW §1.4: Gap Direction × By-Product Match — gap direction = WHY match works.
  → NEW §5.5: Compiled/Fresh processing × gap direction evaluation.
  → NEW §6.2 addition: by-product match × 2-layer model connection.
  → NEW §6.4 ⑤: "by-product match selective" explained via 2-layer.
  → NEW §8.1 addition: 5-Channel Input Vector × gap install.
  → NEW §10.2 addition: Compilable Architecture connection (abstract = feature not bug).
  → NEW §12: Gap Direction × Inter-Body — CORE NEW SECTION (~250L):
    §12.1: Gap direction = foundation cho by-product match
    §12.2: 2-Stream Architecture × Gap Direction
    §12.3: Compilable Architecture × Gap Direction (general-purpose evaluation)
    §12.4: 3 Independent Cost Sources × Gap Direction
    §12.5: Input Channel Control × Gap Direction
  → §13.4: Parenting v2.0 note (by-product match in parent-child).
  → §13.5: AI era v2.0 note (AI × by-product match).
  → §14: +GD-Q7, +GD-Q8 (new open questions from inter-body connection).
  → §15: Honest Assessment UPDATE (+4🟡, +2🔴, +5🟢 research).
  → §16: Cross-refs updated to Phase 1-8 versions.
  → ALL 22 examples PRESERVED. ALL 9→14 research citations PRESERVED + EXPANDED.
  → Vocabulary consistent with Body-Feedback-Label.md v2.0.
  → v1.1 content: 100% PRESERVED + ENRICHED (no deletions).
```
