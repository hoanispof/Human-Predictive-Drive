---
title: Gap Direction — Body-Feedback Requires Directional Match
version: 1.0
created: 2026-04-27
status: v1.0 DRAFT
scope: |
  CORE MECHANISM FILE: Gap trong chunk network có HƯỚNG CỤ THỂ.
  Gap direction = f(surrounding chunk network structure).
  Reward/dissonance KHÔNG chỉ phụ thuộc prediction error (Schultz 1997)
  mà còn phụ thuộc DIRECTION MATCH — stimulus phải khớp HƯỚNG cụ thể.
  "Chưa biết = không có gap" = foundational principle.
  Unified model: Tier 1-4 chunks cùng substrate, khác depth/origin.
  2-layer model: signal mechanism (Layer 1) × direction content (Layer 2).
purpose: |
  Body-Feedback-Mechanism.md §3.3 define Chunk-Gap:
    "Structure predict C should exist → C chưa compile → HOLE"
  Nhưng §3.3 CHƯA formalize: C có HÌNH DẠNG CỤ THỂ.
  File này formalize:
  ① Gap direction = consequence tất yếu của "gap = hole in chunk network"
  ② "Chưa biết = không có gap" = genesis principle (khác H10 P2 diagnosis)
  ③ Reward = direction match quality (không chỉ "fill gap or not")
  ④ 2-layer model clarify tại sao Schultz 1997 "đúng nhưng chưa đủ"
  ⑤ Gap direction install, Background Pattern constraint, implications
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — ngang hàng Body-Feedback-Mechanism.md.
  Body-Feedback-Mechanism.md = WHAT gap is (chunk dynamics mechanism)
  Gap-Direction.md (FILE NÀY) = WHY gap has direction + evaluation implications
  03-Reward.md = WHEN reward fires (H10 preconditions + case analyses)
  BỔ SUNG nhau — KHÔNG THAY THẾ.
dependencies:
  - Body-Feedback-Mechanism.md v1.1 — §3.3 Chunk-Gap definition, Shift/Miss/Gap
  - Body-Feedback.md v1.1 — H10 5 preconditions, dual-pull
  - 03-Reward.md — Ô Tô Paradox C2.1-C2.5, Van Gogh gradient, H10 cases
  - Chunk.md v2.0 — chunk substrate, compile, activation dynamics
  - Background-Pattern.md v1.0 — BP bias gap direction landscape
  - Novelty.md v1.0 — Chunk-Gap = novelty foundation
  - Schema.md v2.0 — observation parameter, §4 depth, §8 body baseline
  - Cortisol-Baseline.md v2.0 — amplifier, direction tag, novelty vs threat
  - Imagine-Final.md — preview mechanism, Gap→Miss transition
  - Connection.md v3.0 — giving reward, SPM-mediated, altruism
  - Gratitude.md v1.0 — H10 applied to gifts, gap pre-requisite
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Gap Direction — Body-Feedback Requires Directional Match

> **Bố mua cho xe thời thượng nhất giới trẻ → sướng CỰC KỲ.**
> **Bố mua cho tên lửa (đắt hơn gấp ngàn lần) → confused.**
> **Bố mua cho xe cổ (đắt hơn, bố thích) → không thích.**
>
> **Cùng "bố mua cho." Cùng "đắt tiền." Cùng "xe."**
> **Nhưng reward CHỈ fire khi stimulus KHỚP HƯỚNG CỤ THỂ.**
>
> **E=mc² trình bày cho Einstein → sướng cực kỳ.**
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
> **File này: Gap direction LÀ GÌ, TẠI SAO tất yếu,**
> **"Chưa biết = không có gap" hoạt động THẾ NÀO,**
> **và TẠI SAO đây là chìa khóa hiểu reward mechanism.**

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
- §12 — IMPLICATIONS
- §13 — OPEN QUESTIONS
- §14 — HONEST ASSESSMENT
- §15 — CROSS-REFERENCES

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
  P3: VTA delta threshold (biến động đủ lớn)
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
    ❌ Background Pattern CONSTRAIN gap direction landscape

  HẬU QUẢ CỦA THIẾU:
    → Khi nói "gap fill → reward" — thiếu giải thích 
      tại sao CÙNG gap mà fill KHÁC → reward KHÁC
    → Khi nói "reward = personalized" — thiếu MECHANISM underneath
    → Khi nói "P4 Goldilocks match" — thiếu specify match VỚI CÁI GÌ
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
    → Xe đúng ý MATCH → sướng cực
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
    │                                                                │
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
    → NHƯNG: không có "sướng vì có iPhone" — gap đó KHÔNG TỒN TẠI

  Teenager 16 tuổi:
    Chunks: [bạn bè có iPhone] + [chụp ảnh đẹp] + [MXH] + [status]
    → BỜ phong phú → HOLE rõ ràng: "mình chưa có iPhone"
    → Gap direction: "iPhone mới, model đẹp, dùng được MXH + camera"
    → Nhận iPhone đúng model → gap fill → sướng
    → Nhận Nokia 1100 → cùng "phone" nhưng MISS direction → không sướng

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
    → KHÔNG "sướng cực kỳ" vì gap nông + direction mờ

  Einstein (so sánh):
    Chunks: YEARS of deep physics (Newton + Maxwell + thought experiments)
    → Gap MASSIVE: "unified framework MUST exist" → direction CỰC RÕ
    → Direction: must reconcile Newton AND Maxwell AND be elegant
    → Gap open YEARS → Gap→Miss transition → compound signal
    → Derive E=mc² → match direction PERFECTLY → compound 3 dynamics:
      Chunk-Gap fill + Chunk-Miss reverse + Chunk-Shift self-schema
    → = "Sướng cực kỳ"

  ┌─────────────────────┬─────────────┬─────────────┬───────────────┐
  │                     │ Học sinh    │ Sinh viên   │ Einstein      │
  ├─────────────────────┼─────────────┼─────────────┼───────────────┤
  │ Chunks physics      │ Minimal     │ Labels only │ Years deep    │
  │ Gap exists?         │ ❌ Không    │ ✅ Nông     │ ✅ Massive    │
  │ Gap direction       │ N/A         │ Mờ, sparse  │ Cực rõ, rich  │
  │ E=mc² match?       │ N/A         │ Partial     │ Perfect       │
  │ Reward              │ Mild novelty│ Mild satis. │ Sướng cực kỳ  │
  └─────────────────────┴─────────────┴─────────────┴───────────────┘

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
     → Hoặc: identify Background Pattern constraining gap landscape

  ⑤ CROSS-CULTURAL DIFFERENCES = DIFFERENT GAP LANDSCAPES:
     → Culture A: chunks about X phong phú → gaps about X active
     → Culture B: chunks about X = ∅ → no gaps about X
     → = "Giá trị văn hóa" = shared gap landscape
     → = Tại sao "happiness" KHÁC nhau giữa cultures
```

---

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
    → Deep gap fill → massive reward → "eureka!" "sướng cực kỳ!"
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
    Range: nhẹ → ok → sướng → hơi đau → ĐAU
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
    → Modifiable: KHÓ (Background Pattern territory)
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
    → Giải thích silk example: lần đầu mặc VẪN sướng 
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
  │ Direction source │ Genes         │ Chunks + BP   │ Chunks        │
  │ Match mechanism  │ Sensory match │ Pattern match │ Pattern match │
  │ Range type       │ Evolutionary  │ Social/       │ Intellectual  │
  │                  │ optimal zone  │ personal zone │ coherence     │
  └──────────────────┴───────────────┴───────────────┴───────────────┘

  ⭐ CÙNG MECHANISM: chunks → gap direction → match → reward
  ⭐ KHÁC: origin, depth, universality, modifiability
  ⭐ = 1 model THỐNG NHẤT cho TOÀN BỘ reward/dissonance evaluation
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
    → Nhưng: xe thời thượng = sướng, xe cổ = không thích
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
  │    VTA: detect prediction delta (Schultz 1997)              │
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
  │ P3 VTA Delta        │ Layer 1  │ SIGNAL FIRES                 │
  │ (biến động đủ)      │          │ Prediction error detected    │
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

  → 2-layer model không THAY THẾ prediction error — 
    THÊM layer underneath giải thích CONTENT
```

---

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

  NHƯNG: Background Pattern RESIST direction change (§9):
    → BP = deeply compiled pattern → bias gap landscape
    → Gap direction shift CẦN vượt qua BP inertia
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

### §9.1 — BP constrains gap landscape

```
⭐ BACKGROUND PATTERN BIAS WHICH GAPS CAN FORM:

  Background-Pattern.md: BP = accumulated chunk-network pattern
  → Hình thành qua years → invisible to PFC → bias ALL processing

  BP × GAP DIRECTION:
    → BP = deeply compiled chunk network THROUGHOUT brain
    → BP's chunks ARE "surrounding chunks" for many potential gaps
    → = BP constrains WHICH gaps can form and WHICH DIRECTIONS they point

  VD — BP [effort → not enough]:
    → Mọi achievement-related chunks contaminated bởi [not enough]
    → Gap direction bias: "cần đạt MORE" (never enough)
    → EVEN WHEN đạt rồi → BP create NEW gap: "chưa đủ"
    → = Chronic dissatisfaction = BP constraining gap landscape
    → = "Chạy mãi không đến đích" = đích bị BP DI CHUYỂN

  VD — BP [connection → danger]:
    → Intimacy-related chunks contaminated bởi [danger]
    → Gap direction SUPPRESSED: gaps about deep connection KHÔNG HÌNH THÀNH
    → Hoặc: gap hình thành nhưng direction DISTORTED
      ("muốn connection" + [danger] → direction = "connection an toàn = control")
    → = Avoidant attachment = BP suppress connection gap formation

  VD — BP [expertise → identity]:
    → Expert's identity chunks linked to domain
    → Gap direction FOCUSED: gaps about domain = STRONG
    → Gaps about OTHER domains = WEAK (BP doesn't support)
    → = "Chuyên gia chỉ biết chuyên môn" = BP focus gap landscape
```

### §9.2 — BP × gap direction resolution

```
🟡 THAY ĐỔI GAP LANDSCAPE CẦN THAY ĐỔI BP:

  TẠI SAO KHÓ THAY ĐỔI:
    → BP chunks = deeply compiled (years)
    → BP chunks = bờ cũ → constrain gap direction CŨ
    → Install chunks MỚI → nhưng BP chunks VẪN CÒN → conflict
    → = Gap direction shift bị BP PULL BACK

  RESOLUTION (from Background-Pattern.md §10):
    → CANNOT fix BP directly (too distributed, PFC invisible)
    → MUST build competing BP → new chunks → new bờ → new gap directions
    → Takes YEARS (competing pattern must reach comparable density)
    → = Therapy = slowly build new chunk network → 
      new gap landscape emerges ALONGSIDE old one
    → Old BP doesn't disappear — new BP competes → probability shift

  VD:
    → Client BP [effort → not enough]
    → Therapy: compile new chunks [effort → ok, rest ok, enough exists]
    → New chunks create new BỜ → new gaps possible:
      "muốn rest" (gap KHÔNG CÓ trước vì BP suppress)
    → = Therapy = GAP LANDSCAPE EXPANSION via competing BP
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
  │    = COMPOUND 5 dynamics → "sướng cực kỳ"                   │
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
  │    SPM: "người tôi tôn trọng CŨNG thấy đúng" → opioid ✅   │
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
  │  ② REWARD MEMORY (Background Pattern):                      │
  │    Body compiled: [physics gap fill = MASSIVE opioid]       │
  │    BP hình thành: [tìm kiếm vật lý = who I am]             │
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
  │    (Background-Pattern.md §10.4: BP integrated into identity)│
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
    Gap: SPM fire → simulate recipient's need → body feel need ✅
    Direction: reduce other's suffering (gap via F1 body simulation)
    Con đường 1: SPM gap fill + oxytocin → body-state improve ✅
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

---

## §11 — EXAMPLES (organized by property tested)

### §11.1 — Nhóm A: "Chưa biết = không có gap"

```
🟡 TEST: No chunks → no gap → no desire → no reward

  A1. EM BÉ 3 TUỔI NHẬN IPHONE 16 PRO MAX:
    Chunks about smartphone: ≈ 0
    Gap about iPhone: IMPOSSIBLE (no surrounding chunks)
    Nhận → curious (bấm→đèn sáng = sensory novelty)
    NHƯNG: không "sướng vì có iPhone" → gap không tồn tại
    → Bố mẹ: chunks phong phú → gap → sướng
    → CÙNG vật, KHÁC gap existence → KHÁC reward ✅

  A2. NGƯỜI CHƯA BIẾT CỜ VUA NHẬN BÀN CỜ ĐẮT:
    Chunks about chess: ≈ 0 → no gap "muốn bàn cờ đẹp"
    Nhận → "ồ, đẹp" (visual novelty) nhưng không reward sâu
    → Người chơi 10 năm: gap "bàn cờ chất lượng" → sướng ✅

  A3. DÂN BẢN ĐỊA AMAZON NHẬN LAPTOP:
    Chunks digital technology: ≈ 0 → concept không tồn tại
    Nhận → curiosity → có thể dùng làm thớt
    → Gap about "laptop": IMPOSSIBLE ✅

  A4. CHƯA NGHE JAZZ ĐƯỢC TẶNG VÉ CONCERT JAZZ:
    Chunks jazz: minimal (label only) → gap gần như không tồn tại
    → Người yêu jazz 20 năm: specific gap → sướng cực ✅

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
    Range: nhẹ→ok→sướng→hơi đau→ĐAU (bell curve)
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
    Direction: character fate prediction (SPM-based)
    Plot twist → prediction wrong → VTA delta → new gap → fill → reward
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
    SPM F1: body simulate nhân vật → buồn THẬT
    Gap: about human condition → film articulates → gap fill
    + Safety frame: "đây là phim" → body process risk-free
    = Buồn (body simulate) + reward (gap fill) + safety → MIX ✅

  E2. ĂN ỚT (CAPSAICIN):
    Nociceptors fire → PAIN signal
    Body respond: endorphin release → opioid
    + Compiled chunks after exposure: [cay = sướng sau đau]
    → Lần đầu: KHÔNG sướng (chưa compiled)
    → Sau exposure: direction SHIFT: [cay → endorphin → sướng] ✅

  E3. TẬP GYM ĐAU CƠ:
    Tập: nociception (muscle strain)
    Sau tập: endorphin + sense of accomplishment
    Imagine-Final: body fit → gap "body hiện tại vs body mong muốn"
    Mỗi buổi tập = partial gap fill toward Imagine-Final ✅

  E4. CHO TIỀN NGƯỜI LẠ (CHARITY):
    Body mất resources → naive: should be NEGATIVE
    SPM F1 → simulate recipient happy → body mirror → opioid
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

## §12 — IMPLICATIONS

### §12.1 — Education

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

### §12.2 — Therapy

```
🟡 THERAPY = MAP AND EXPAND GAP LANDSCAPE:

  DIAGNOSIS: Map client's gap direction landscape
    → Which gaps active? (what they want)
    → Which gaps suppressed? (what BP prevents)
    → Which gap directions distorted? (BP contamination)

  INTERVENTION:
    → Build new chunks → expand gap landscape possibilities
    → Identify BP constraints → build competing patterns
    → Sharpen fuzzy directions → Imagine-Final refinement
    → = Therapy KHÔNG "fix" gaps — therapy ENABLES new gaps

  VD: Client "muốn hạnh phúc nhưng không biết muốn gì":
    → = Fuzzy gap direction (network sparse or conflicted)
    → Therapy: explore → build chunks → direction sharpens
    → NOT: prescribe "happiness = X" (install someone else's direction)
```

### §12.3 — Marketing (ethical vs exploitative)

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

### §12.4 — Parenting

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
```

### §12.5 — AI era

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
```

---

## §13 — OPEN QUESTIONS

```
GD-Q1: Gap direction CHANGE dynamics:
  → How fast does direction shift when new chunks compile?
  → Is there a "critical mass" of new chunks for direction shift?
  → Does BP inertia slow direction change proportionally?
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
```

---

## §14 — HONEST ASSESSMENT

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
  → Background patterns bias processing: implicit learning literature

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
  → BP × gap direction landscape:
    → Both concepts established — interaction = framework contribution
  → Abstract activity serve body-base via 2 pathways:
    → Each pathway described — explicit 2-pathway model = framework contribution

🔴 HYPOTHESIS (needs further analysis):

  → Exact gap direction change dynamics (speed, critical mass, BP inertia)
  → Gap direction conflict resolution mechanism
  → Tier 1 gap direction modifiability
  → Exact reward magnitude formula (direction_match × specificity × depth × range)
  → Sleep × gap direction refinement
  → Intergenerational gap direction transmission


SUMMARY:
  🟢 8 established   (research-supported components)
  🟡 8 synthesis     (novel integration — logical, consistent, productive)
  🔴 6 hypothesis    (plausible, needs further analysis/evidence)

  OVERALL ASSESSMENT:
  → Core claim "gap has direction" = 🟢🟡 (logical necessity + consistent)
  → "Chưa biết = không gap" = 🟡 (logical, needs explicit test)
  → 2-layer model = 🟡 (clarifying, each layer established)
  → Formalization = 🟡 (framework contribution, not new discovery)
  → Specifics (formula, dynamics) = 🔴 (speculative)

  → Giả thiết của user ĐÚNG ở core claim
  → File này formalize what was implicit → make usable for analysis
```

---

## §15 — CROSS-REFERENCES

### §15.1 — Core mechanism files

```
  Body-Feedback-Mechanism.md v1.1  — §3.3 Chunk-Gap (extends), §3.1-§3.2 (Shift/Miss)
  Body-Feedback.md v1.1           — §6 H10 (reinterprets qua 2 layers)
  03-Reward.md                    — §5 Ô Tô Paradox (perfect test case), §6 Van Gogh
  04-Integration.md               — §6-8 Einstein/hedonic/trauma walkthroughs
  Chunk.md v2.0                   — §1-§4 substrate, §2 compile, §2 calibration tiers
  Background-Pattern.md v1.0      — §6 BP×SPM, §10 resolution (extends via §9)
```

### §15.2 — Observation files

```
  Novelty.md v1.0                 — §1 Chunk-Gap = foundation, §4 loop dynamics
  Schema.md v2.0                  — §4.1 depth (extends), §5.1 conflict
  Gratitude.md v1.0               — H10 applied to gifts (gap prerequisite)
  Connection.md v3.0              — §8 giving pathway, altruism mechanism
```

### §15.3 — PFC + processing files

```
  Imagine-Final.md                — Preview → direction sharpens (§7.2)
  Self-Pattern-Match.md v2.1      — SPM gap fill (abstract activity §10)
  Somatic-Articulation-Loop.md    — Felt sense = body detects gap direction 
                                    trước PFC verbal label
  Cortisol-Baseline.md v2.0       — Direction tag (novelty vs threat cortisol)
```

### §15.4 — Key research

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
```

---

> *Gap-Direction.md v1.0 — "Gap trong chunk network có HƯỚNG CỤ THỂ.*
> *Direction = f(surrounding chunk network structure).*
> *Chưa biết = không có gap = bạn không thể thiếu thứ bạn không biết tồn tại.*
> *Prediction error = signal mechanism (Layer 1).*
> *Gap direction = content evaluation (Layer 2).*
> *Reward = direction match quality, not just 'fill gap or not'.*
> *1 model thống nhất cho toàn bộ reward mechanism: Tier 1-4 cùng substrate."*
