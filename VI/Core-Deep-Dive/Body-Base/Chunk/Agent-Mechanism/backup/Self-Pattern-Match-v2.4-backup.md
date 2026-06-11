---
title: Self-Pattern-Match — Solo Forward Simulation Mechanism
version: 2.2
created: 2026-04-15
rewritten: 2026-04-24
updated: 2026-05-15 (v2.4 — §18 Late diagnosis re-compile + C-PTSD identity, Health Conditions Drill)
status: v2.3 — CORE MECHANISM FILE
supersedes:
  - backup/Self-Pattern-Match-v1.0-forward-backup.md (v1.0, 1518L)
  - Body-Base/Feeling/backup/Self-Pattern-Match.md (old inward-labeling definition)
parent: Agent-Mechanism.md (integration hub)
sibling: Pattern-Resonance.md (emergent mutual phenomenon)
scope: |
  Deep drill của Self-Pattern-Match mechanism.
  v2.0 KEY CHANGE: Tách rõ 2 FUNCTIONS bên trong SPM:
    F1 — Feeling: body-level simulation (agent cảm thấy thế nào?)
    F2 — Logic: chain prediction (agent sẽ hành xử thế nào?)
  + Context-dependent chunk selection (vô thức chọn chunks phù hợp agent/context)
  + Per-Agent Valence × 2 Functions = matrix quyết định toàn bộ output
  + Reversed mapping (Schadenfreude, sadism, professional SPM conflicts)
  + Schema fallback khi chunks thiếu ("phụ nữ khó hiểu" = SPM gap → schema thế chỗ)
purpose: |
  File NỀN TẢNG cho toàn bộ framework:
  ① SPM là CƠ CHẾ CHÍNH mà não dùng để interact với agents
  ② 2 Functions (F1+F2) giải thích TẠI SAO cùng 1 mechanism
     có thể tạo empathy LẪN strategic prediction LẪN Schadenfreude
  ③ Context-dependent selection giải thích TẠI SAO cùng 1 người
     ứng xử KHÁC NHAU với mẹ, bạn, kẻ thù
  ④ Per-Agent Valence quyết định F1/F2 fire HƯỚNG NÀO
position: |
  Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/ — supporting file cho Agent-Mechanism.md
  Sibling: Pattern-Resonance.md
  Downstream: Connection.md, Empathy.md, Status.md, toàn bộ observation files
dependencies:
  - Agent-Mechanism.md — integration hub, §5 preview
  - Pattern-Resonance.md — emergent mutual phenomenon
  - Chunk.md v2.0 — chunk substrate
  - Feeling.md v2.0 — PFC observation interface
  - Logic-Feeling.md — 2 processing modes parallel
  - Valence-Propagation.md v1.1 — per-entity valence, chain propagation
  - Empathy.md — SPM function applied to other agents
  - Cortisol-Baseline.md v2.0 — stress cascade, moral injury
  - Connection.md — 8 pathways, 3 generative primitives
  - Threat.md — NE cascade, PFC disconnect
sources_backup: |
  v1.0: Self-Pattern-Match.md (1518L, 2026-04-15) → backup/Self-Pattern-Match-v1.0-forward-backup.md
  v0: Self-Pattern-Match.md (inward-labeling) → Body-Base/Feeling/backup/Self-Pattern-Match.md
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Self-Pattern-Match — Solo Forward Simulation Mechanism

> Bạn thấy bạn thân khóc. Body bạn buồn nhẹ — DÙ bạn không bị gì.
> Đó là F1: body SIMULATE trạng thái người khác.
>
> Rồi bạn nghĩ: "bạn buồn vì chia tay → chắc muốn ai đó lắng nghe."
> Đó là F2: PFC CHAIN logic predict hành vi tiếp theo.
>
> 2 functions này chạy SONG SONG — gần như vô thức.
> Cùng 1 mechanism. Cùng 1 chunk library. Nhưng 2 OUTPUTS khác nhau:
> F1 cho body-level feeling. F2 cho behavioral prediction.
>
> Và TẤT CẢ phụ thuộc 1 biến số quyết định:
> Per-Agent Valence — body ĐÁNH GIÁ agent này thế nào?
>
> Valence dương: F1 = empathy (buồn cùng), F2 = giúp đỡ.
> Valence âm: F1 = REVERSED (sướng khi kẻ thù đau), F2 = tấn công.
> Valence cực âm: F1 BỊ TẮT = dehumanization. Chỉ còn F2 logic thuần.
>
> Đây là lý do CÙNG 1 CƠ CHẾ (SPM) có thể tạo empathy,
> Schadenfreude, strategic prediction, và dehumanization.
> Không phải 4 hệ thống khác nhau — là 1, với 2 functions × valence spectrum.
>
> File này: SPM LÀ GÌ, 2 functions hoạt động THẾ NÀO,
> TẠI SAO context thay đổi chunks, Per-Agent Valence quyết định HƯỚNG,
> 6 steps chi tiết, 5 pattern-types, phát triển, rèn luyện,
> và TẠI SAO hiểu SPM = hiểu phần lớn cách con người tương tác.

---

## Mục lục

- §0 — Abstract + Definition
- §1 — Position (v1 → v2: what changed)
- §2 — 2 FUNCTIONS: F1 Feeling + F2 Logic
- §3 — 6 STEPS (reframed qua 2 Functions)
- §4 — CONTEXT-DEPENDENT CHUNK SELECTION
- §5 — 5 PATTERN-TYPE MODALITIES
- §6 — 4 QUALITY AXES
- §7 — DEVELOPMENTAL BOOTSTRAP
- §8 — CALIBRATION + FEEDBACK LOOP
  - §8.1 — "Biết" = compiled prediction — cùng cơ chế, khác trải nghiệm
- §9 — THRESHOLD FAILURE + FALLBACK
- §10 — REVERSED MAPPING + PROFESSIONAL SPM
- §11 — USE CASES (reframed qua F1/F2 × Valence)
- §12 — ALEXITHYMIA + BIRD & COOK 2013
- §13 — ToM LITERATURE MAPPING
- §14 — TRAINING + CULTIVATION
- §15 — AI ERA IMPLICATIONS
- §16 — OPEN QUESTIONS
- §17 — HONEST ASSESSMENT
- §18 — CROSS-REFERENCES

---

## §0 — Abstract + Definition

### §0.1 — Definition

**Self-Pattern-Match (SPM)** = solo forward simulation mechanism.

**Nói đơn giản:** dùng cảm nhận bản thân để hiểu người khác — dựa trên dự đoán họ cũng giống mình một phần. Lặp lại đủ lâu → dự đoán trở thành tự động → cảm thấy như "biết" — nhưng cơ chế vẫn là dự đoán.

**Kỹ thuật:** não retrieve chunks từ self repertoire, apply làm template cho target entity, simulate trạng thái target, đọc output, và attribute cho target như prediction.

SPM fire trên GRADIENT agent-properties: càng agent-like → SPM càng rich (F1+F2 full). Ít agent-like → SPM degrade → fallback (schema → logic → physics). Chi tiết: §9.

**v2.0 KEY REFINEMENT**: SPM chạy 2 FUNCTIONS song song — chính là Logic-Feeling.md 2 processing modes DIRECTED AT entity prediction:
- **F1 — Feeling**: body fire bản sao yếu trạng thái target → body-level response THẬT
- **F2 — Logic**: PFC chain logic trên F1 output → predict hành vi target tiếp theo

2 functions dùng CHUNG chunk library, CHUNG 6 steps chuẩn bị. Nhưng OUTPUT khác: F1 cho body feeling, F2 cho behavioral prediction.

### §0.2 — One-paragraph summary

Self-Pattern-Match là cơ chế mình dùng mình làm template để đoán người khác. Không phải mind-reading trực tiếp, không phải hardware mirror module — là simulation-based inference dùng self-chunks làm building blocks. SPM chạy 2 functions song song: F1 simulate what target FEELS (body-level, near-automatic), F2 chain predict what target will DO (PFC-level, deliberate). Per-Agent Valence quyết định F1 fire HƯỚNG NÀO (empathy hay reversed) và F2 chain MỤC ĐÍCH NÀO (giúp hay đối phó). Context quyết định chunks NÀO được retrieve (vô thức tùy chọn — với mẹ khác với bạn bè khác kẻ thù). Khi chunks THIẾU cho target, não fallback xuống schema/logic thay thế.

### §0.3 — Central claims

```
⭐ 9 CLAIMS CỐT LÕI:

  1. SOLO + FORWARD: SPM chạy bên trong self, tạo prediction TRƯỚC verification
  2. CHUNK-SUBSTRATE: dùng cùng chunk library như mọi cognitive function khác
  3. ⭐ 2 FUNCTIONS: F1 Feeling (body simulate) + F2 Logic (PFC chain)
     — chạy SONG SONG mặc định, CÓ THỂ tách riêng với rèn luyện
  4. ⭐ CONTEXT-DEPENDENT: chunks được retrieve VÔ THỨC tùy agent + context
     — cùng 1 người ứng xử KHÁC với mẹ, bạn, kẻ thù, người lạ
  5. ⭐ VALENCE-GATED: Per-Agent Valence quyết định F1 fire hướng nào
     và F2 chain mục đích nào — empathy, strategic, hay dehumanize
  6. MULTI-MODAL: 5 Pattern-Type modalities
  7. QUALITY-VARIABLE: 4 axes quyết định output quality
  8. BIRD & COOK ARCHITECTURAL: self-awareness là prerequisite
  9. CALIBRATABLE: library refine qua feedback từ Pattern-Resonance
```

### §0.4 — Relationship với files khác

```
  Agent-Mechanism.md §5 = preview (high-level)
  Self-Pattern-Match.md (FILE NÀY) = deep drill (mechanism chi tiết)
  Pattern-Resonance.md = sibling (emergent mutual phenomenon)

  SPM = MECHANISM (cái mình chạy bên trong)
  PR = PHENOMENON (cái emerge giữa 2+ agents khi SPM cả 2 thành công)

  Reading flow:
    Chunk.md → Agent-Mechanism.md → Self-Pattern-Match.md → Pattern-Resonance.md
```

---

## §1 — Position: v1.0 → v2.0

### §1.1 — v1.0 là gì

v1.0 (1,518L, 2026-04-15): SPM như 1 process thống nhất — 6 steps, 5 pattern-types, 4 axes, developmental bootstrap, Bird & Cook, ToM literature, training, AI era.

v1.0 ĐÚNG ở phần lớn nội dung. Nhưng THIẾU tầng phân tích bên trong:
- Không tách rõ F1 (body simulate) vs F2 (logic chain)
- Không mô tả context-dependent chunk selection
- Không map Per-Agent Valence vào SPM output direction
- Không giải thích reversed mapping (Schadenfreude, sadism)
- Không phân tích professional SPM conflicts (moral injury)

### §1.2 — v2.0 thay đổi gì

```
⭐ 3 THAY ĐỔI CỐT LÕI:

  ① TÁCH 2 FUNCTIONS:
    v1.0: SPM = 1 process → 1 output (prediction)
    v2.0: SPM = 2 functions song song:
      F1 Feeling → body-level output (cảm nhận)
      F2 Logic → PFC-level output (predict hành vi)

  ② THÊM CONTEXT-DEPENDENT SELECTION:
    v1.0: Step 1 Retrieve có mention selection drivers — nhưng chưa rõ
    v2.0: Đặt riêng thành section chính — vô thức chọn chunks phù hợp
      mỗi context, mỗi agent, mỗi relationship

  ③ THÊM VALENCE × SPM MATRIX:
    v1.0: Không cover negative valence cases
    v2.0: Per-Agent Valence quyết định F1/F2 direction:
      positive → empathy + helping
      negative → reversed + strategic
      extreme negative → F1 suppress (dehumanize)
```

### §1.3 — Gì giữ từ v1.0

```
  GIỮ NGUYÊN (đã chất lượng):
    → 6-step mechanism (refine qua 2-function lens)
    → 5 Pattern-Type modalities
    → 4 quality axes
    → Developmental bootstrap (mother contingency, rouge test)
    → Calibration + feedback loop
    → Bird & Cook 2013 (decisive architectural)
    → ToM literature mapping
    → Training methods
    → AI era implications
    → Honest assessment framework

  RESTRUCTURE:
    → 6 steps: mỗi step annotate F1 role + F2 role
    → Fallback: thêm valence-driven cases
    → Use cases: reframe qua F1/F2 × valence
```

---

## §2 — 2 FUNCTIONS: F1 Feeling + F2 Logic

### §2.1 — F1: Body-level simulation

```
⭐ F1 = FEELING FUNCTION:

  DEFINITION:
    F1 là phần SPM mà body THẬT SỰ fire bản sao yếu trạng thái target.
    Body MÌNH respond — biochemistry THẬT, không phải tưởng tượng.

  CƠ CHẾ:
    Retrieve chunks about target (Step 1-3 chung)
      ↓
    Body fire template as-if-self-were-target (Step 4)
      ↓
    Body respond: opioid / cortisol / oxytocin / NE / VTA
      ↓
    PFC observe body response (Step 5) → "feeling about target's state"

  OUTPUT: Body-level response
    → "Bạn buồn → tôi buồn nhẹ" = F1 output
    → "Con ăn ngon → tôi sướng" = F1 output
    → "Kẻ thù đau → tôi... sướng?" = F1 output (reversed — §10)

  ĐẶC TÍNH:
    ① NEAR-AUTOMATIC — PFC gần như không tham gia
       → Affective F1: milliseconds (fastest)
       → Somatic F1: seconds
       → Cognitive F1: seconds to minutes
    ② BODY-LEVEL — biochemistry THẬT (Empathy.md §4.2)
       → Không phải "tưởng tượng" hay "cognitive thuần"
       → Body MÌNH genuinely responds (slight sadness, tension, warmth)
    ③ KHÔNG THỂ TẮT HOÀN TOÀN
       → Vì Step 4 = body-level event
       → CÓ THỂ DAMPEN (qua valence, schema, training)
       → KHÔNG THỂ ELIMINATE (trừ dehumanize → F1 suppress)
    ④ BIẾN THIÊN INTENSITY
       → Zero (không hợp tính, không muốn) → rất mạnh (hợp tính + deep chunks)
       → "Hợp tính" = Pattern-Resonance Baseline cao (Pattern-Resonance.md §7.8)
       → GRADIENT liên tục, KHÔNG cố định

  ⭐ F1 = "LUỒNG 1" TRONG CONNECTION CONTEXT (Connection.md §3.3):

    F1 body-feedback = Luồng 1 (momentary, per-episode):
      = Body response TẠI KHOẢNH KHẮC simulate target state
      = Có thể POSITIVE (bạn vui → vui lây) hoặc NEGATIVE (con ốm → khó chịu)
      = Cost THẬT: mỗi F1 firing = biochemistry thật → tích lũy = fatigue

    Luồng 1 tồn tại CÙNG LÚC với Luồng 2 (Entity-owned structural):
      = Luồng 2 = compiled per-agent valence → agent = body-base extension
      = SUSTAINED, KHÔNG phụ thuộc F1 output mỗi episode
      = Thuộc về entity valence (Valence-Propagation.md §2), KHÔNG thuộc SPM

    2 luồng INDEPENDENT → có thể CONFLICT:
      → Mẹ chăm con ốm: F1/L1 negative + L2 positive → vẫn chăm
      → Bác sĩ + bệnh nhân: F1/L1 negative + L2 ≈ 0 → burnout (§10.4)
      → Bạn kể vui: F1/L1 positive + L2 positive → compound reward

    → F1 cost tích lũy + L2 bù không đủ = MORAL INJURY (§10.4)

  🟢 Singer 2004: shared activation areas khi observe others' emotions
  🟢 Empathy.md §4.2: empathy = biochemistry THẬT trong body MÌNH
  🟡 F1 as distinct function = framework synthesis, consistent với dual-process
  🟡 F1 = Luồng 1 framing: Connection.md §3.3
```

### §2.2 — F2: Logic chain prediction

```
⭐ F2 = LOGIC FUNCTION:

  DEFINITION:
    F2 là phần SPM mà PFC chain logic trên F1 output (hoặc trực tiếp
    trên retrieved chunks) để predict hành vi target tiếp theo.
    "Target feel X → target thường do Y → kết quả Z → plan cho tôi."

  CƠ CHẾ:
    F1 output available (body response observed)
      ↓
    PFC chain: "target feel X" (from F1 or from logic inference)
      ↓
    PFC chain: "khi feel X → target thường hành xử Y"
      ↓
    PFC chain: "hành xử Y → kết quả Z cho tôi"
      ↓
    PFC chain: "vậy tôi nên action A để optimize outcome"

  OUTPUT: Behavioral prediction + action plan
    → "Bạn buồn → bạn cần an ủi → tôi nên hỏi thăm" = F2 output
    → "Sếp giận → sếp sẽ la → tôi nên tránh" = F2 output
    → "Đối thủ yếu → sẽ phòng thủ → tôi nên tấn công" = F2 output

  ĐẶC TÍNH:
    ① DELIBERATE — PFC PHẢI tham gia (sequential processing)
       → Slower: seconds to minutes
       → Consume glucose + neurotransmitters (PFC resource)
       → 🟢 Gailliot & Baumeister 2007: cognitive effort = metabolic cost
    ② CÓ THỂ CHẠY KHÔNG CẦN F1
       → Thuần logic: "theo quy tắc, con gái thì dịu dàng" (schema thế chỗ)
       → NHƯNG accuracy GIẢM khi thiếu F1 input (miss feeling-level data)
    ③ CÓ THỂ BỊ TẮT KHI F1 QUÁ MẠNH
       → Cảm xúc quá mạnh → PFC disconnect (Arnsten 2009: α1 NE)
       → "Giận quá mất khôn" = F1 overwhelm → F2 offline
    ④ CÓ THỂ OVERRIDE F1
       → Training: "tôi biết mình buồn lây, nhưng bây giờ cần logic"
       → Professional mode: bác sĩ, therapist, negotiator

  🟢 Dual Process Theory (Kahneman 2011): System 1 ≈ F1, System 2 ≈ F2
  🟢 Logic-Feeling.md: 2 processing modes song song cho mọi entity
  🟡 F2 as distinct function within SPM = framework synthesis
```

### §2.3 — Song song mặc định, tách riêng khi rèn luyện

```
⭐ F1 + F2 CHẠY SONG SONG:

  DEFAULT MODE — hầu hết tương tác hàng ngày:

    Thấy bạn buồn
      → F1: body fire sadness nhẹ (milliseconds)
      → F2: "bạn buồn → cần an ủi → hỏi thăm" (seconds)
      → CẢ HAI chạy ĐỒNG THỜI
      → Cost THẤP vì chia sẻ Step 1-3 (retrieve + template + project)

    Nghe sếp nói "meeting gấp"
      → F1: body fire tension nhẹ (detect sếp's urgency)
      → F2: "sếp gấp → deadline → chuẩn bị tài liệu"
      → Combined output: vừa cảm nhận urgency vừa plan

    Thấy con khóc
      → F1: body fire distress MẠNH (baby schema → empathy amplify)
      → F2: "con đói hay đau → check → action"
      → F1 MẠNH hơn F2 ở đây → hành động NHANH, logic SAU


  TẠI SAO SONG SONG MÀ KHÔNG TUẦN TỰ:

    Nếu F1 → rồi mới F2 (tuần tự):
      → Chậm — mất thêm thời gian sequence
      → Trong context nguy hiểm → chậm = chết
    Nếu F1 + F2 cùng lúc (song song):
      → Nhanh — body feel + PFC plan ĐỒNG THỜI
      → Hành động chính xác + nhanh
    → Evolution select SONG SONG vì survival advantage

    🟢 Logic-Feeling.md §5: "Logic và Feeling chạy SONG SONG cho MỌI entity"
    🟡 "Song song mặc định" = framework claim, consistent với dual-process


  TÁCH RIÊNG — KHI NÀO VÀ TẠI SAO:

    F1 và F2 CÓ THỂ tách riêng vì chúng chạy ở TẦNG KHÁC:
      → F1 = body-level (amygdala, insula, body signals) → gần automatic
      → F2 = PFC-level (prefrontal cortex, working memory) → deliberate
      → = 2 hệ thống KHÁC NHAU xử lý CÙNG input

    Training cho phép DAMPEN 1 function:
      → Therapist training: dampen F2, enhance F1 → "chỉ lắng nghe"
      → Poker training: dampen F1, enhance F2 → "cold reading"
      → Meditation: tách F1 ra observe riêng → metacognitive awareness
      → Professional: modulate tỉ lệ F1/F2 tùy context

    NHƯNG: không thể TẮT 100% F1:
      → F1 = body-level event → body PHẢI respond
      → Chỉ có thể DAMPEN (via schema, training, valence)
      → Chỉ TẮT hoàn toàn khi DEHUMANIZE (F1 suppress — §10)
      → = Tại sao bác sĩ VẪN mệt dù "không suy nghĩ nhiều"
      → = Tại sao therapist cần supervision (F1 cost tích lũy)
```

### §2.4 — 3 Modes

```
⭐ 3 MODES CỦA SPM — TỈ LỆ F1/F2:

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MODE A — FEELING-DOMINANT (F1 >>> F2)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    F1 fire FULL, F2 bị giảm hoặc tạm ngưng.
    "Chỉ cảm nhận, không plan."

    Khi nào:
      → Therapeutic listening: therapist "chỉ ở đó" với client
      → Ngồi cạnh bạn đang khóc — không nói gì, chỉ feel cùng
      → Xem phim buồn — body fire, PFC không plan hành động
      → Nghe nhạc — body respond, không cần logic
      → Lần đầu gặp em bé — body fire nurturing, chưa plan

    Đặc điểm:
      → Body response MẠNH, conscious logic GIẢM
      → "Nói chuyện mà quên hết thời gian" = F1 dominant, F2 suspend
      → Empathy ở purest form — cảm mà không tính
      → Cost: F1 cost tích lũy (empathy fatigue nếu kéo dài)
      → Benefit: connection DEEP nhất, trust build nhanh nhất

    🟢 Gendlin 1978: Focusing = intentional F1-dominant processing
    🟢 Rogers client-centered therapy = F1-dominant listening


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MODE B — LOGIC-DOMINANT (F2 >>> F1)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    F2 fire FULL, F1 bị DAMPEN (không thể tắt 100%).
    "Cold reading — phân tích mà không bị cuốn."

    Khi nào:
      → Poker player đọc đối thủ: predict behavior, suppress empathy
      → Bác sĩ phẫu thuật: biết bệnh nhân đau, không bị lung lay
      → Negotiator: simulate opponent's position, keep distance
      → Chess: predict opponent's moves, pure logic
      → Interrogator: predict prisoner's response, minimize empathy cost

    Đặc điểm:
      → PFC dominant, body response DAMPENED
      → "Biết bạn buồn nhưng bây giờ cần tập trung" = F2 override F1
      → Accuracy CÓ THỂ giảm (miss feeling-level data)
      → Cost: PFC resource depletion (glucose + neurotransmitter)
      → ⚠️ F1 VẪN FIRE NHẸ — không thể tắt hoàn toàn
        → Tích lũy → moral injury, empathy fatigue, burnout

    🟢 Kahneman System 2 = deliberate, effortful
    🟡 "F1 vẫn fire nhẹ" = framework claim, consistent với perpetrator trauma


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MODE C — COMBINED (F1 ≈ F2) — DEFAULT
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    F1 + F2 cùng fire, balance tùy context.
    "Vừa hiểu vừa plan" = social interaction bình thường.

    Khi nào:
      → Hầu hết tương tác hàng ngày
      → Nói chuyện với bạn: feel + plan response
      → Họp nhóm: đọc room + contribute logic
      → Dạy học: cảm nhận student's confusion + explain

    Đặc điểm:
      → Balance tự nhiên — không cần ý thức điều chỉnh
      → Tỉ lệ F1/F2 SHIFT tự động tùy context:
        → Bạn bắt đầu khóc → F1 TĂNG tự động
        → Sếp hỏi deadline → F2 TĂNG tự động
      → = Logic-Feeling.md: "cả 2 chạy song song, tỉ lệ tự adjust"
      → Most EFFICIENT mode — evolution default

    🟢 Logic-Feeling.md §5: parallel processing natural default
    🟡 Combined mode as default = framework synthesis


  ⭐ BẢNG TỔNG HỢP 3 MODES:

    ┌─────────────┬───────────────┬───────────────┬──────────────────┐
    │ Mode        │ F1 (Feeling)  │ F2 (Logic)    │ Best for         │
    ├─────────────┼───────────────┼───────────────┼──────────────────┤
    │ A: Feeling  │ FULL          │ Dampened      │ Deep empathy,    │
    │    dominant │               │               │ therapy, music   │
    ├─────────────┼───────────────┼───────────────┼──────────────────┤
    │ B: Logic    │ Dampened      │ FULL          │ Strategy, poker, │
    │    dominant │ (vẫn fire nhẹ)│               │ surgery, chess   │
    ├─────────────┼───────────────┼───────────────┼──────────────────┤
    │ C: Combined │ Active        │ Active        │ Daily social,    │
    │ (default)   │               │               │ teaching, work   │
    └─────────────┴───────────────┴───────────────┴──────────────────┘

    → Mode KHÔNG cố định — shift tự động hoặc deliberate
    → Rèn luyện = tăng khả năng CHỌN mode phù hợp context
    → "Social intelligence" = biết khi nào dùng mode nào
```

### §2.5 — Per-Agent Valence × 2 Functions = Matrix quyết định

```
⭐ PER-AGENT VALENCE QUYẾT ĐỊNH F1/F2 FIRE HƯỚNG NÀO:

  (Valence-Propagation.md §1-§2: valence = body's evaluation per entity)

  Per-Agent Valence = body đã compiled đánh giá: agent NÀY ảnh hưởng
  body channels CỦA TÔI thế nào? Positive ↔ Negative ↔ Mixed.
  DYNAMIC — thay đổi qua experience.

  Valence KHÔNG phải input cho SPM — valence GATE cho SPM.
  Valence quyết định: F1 fire theo hướng nào, F2 chain mục đích nào.


  ┌──────────────────┬────────────────────┬────────────────────┬─────────────────┐
  │ Per-Agent Valence │ F1 (Feeling)       │ F2 (Logic)         │ SPM overall     │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ STRONG POSITIVE  │ Empathy FULL       │ Help/connect       │ Connection      │
  │ (bạn thân, mẹ)  │ Their joy=my joy   │ "Giúp gì được?"    │ drive           │
  │                  │ Their pain=my pain │ "Làm sao an ủi?"   │                 │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ MILD POSITIVE    │ Empathy nhẹ        │ Social navigate    │ Approach        │
  │ (người quen, VN  │ Warmth nhẹ        │ "Nên ứng xử sao?" │ moderate        │
  │  du lịch thân    │                    │                    │                 │
  │  thiện)          │                    │                    │                 │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ NEUTRAL          │ Surface scan       │ Objective assess   │ Cautious        │
  │ (người lạ, China │ Nhẹ hoặc zero     │ "Người này thế nào"│ observe         │
  │  du lịch neutral)│                    │                    │                 │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ MILD NEGATIVE    │ Discomfort nhẹ     │ Avoid/defend       │ Caution +       │
  │ (bạn hay trêu,   │ Body tension      │ "Tránh hay đối     │ avoidance       │
  │  chó từng cắn)  │ Empathy GIẢM      │  phó thế nào?"     │                 │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ STRONG NEGATIVE  │ ⭐ REVERSED        │ Strategic/hostile   │ Strategic       │
  │ (kẻ thù, lừa     │ Their pain=MY     │ "Tấn công thế nào?"│ attack or       │
  │  đảo, quân địch) │ REWARD            │ "Phòng thủ sao?"   │ deliberate      │
  │                  │ (Schadenfreude)    │ "Kiện ra tòa?"     │ avoidance       │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ EXTREME NEGATIVE │ ⭐ F1 SUPPRESS     │ Logic THUẦN        │ Dehumanize      │
  │ (dehumanized     │ SPM tắt           │ "Object, ko người" │ = object        │
  │  target)         │ Không simulate    │ Mechanical predict  │ treatment       │
  └──────────────────┴────────────────────┴────────────────────┴─────────────────┘


  ⭐ VALENCE LÀ GATE, KHÔNG PHẢI INPUT:

    Input cho SPM = target cues (nhìn, nghe, context)
    Gate cho SPM = compiled valence toward target

    Cùng 1 target cue (người khóc):
      → Valence positive (bạn thân khóc) → F1 empathy + F2 help
      → Valence neutral (người lạ khóc) → F1 nhẹ + F2 assess
      → Valence negative (kẻ thù khóc) → F1 reversed + F2 exploit

    → CÙNG cue, CÙNG mechanism, KHÁC output — vì KHÁC valence


  ⭐ VALENCE DYNAMIC — THAY ĐỔI QUA EXPERIENCE:

    (Valence-Propagation.md §3)

    Du lịch Việt Nam: neutral → positive (người thân thiện)
      → SPM shift: surface → approach → empathy nhẹ → giving reward
    Du lịch Brazil: neutral → NEGATIVE (bị cướp)
      → SPM shift: surface → threat predict → avoid → fear
    Du lịch Trung Quốc: neutral → neutral (safe nhưng không warm)
      → SPM shift: surface → surface (không change)

    → Valence UPDATE liên tục qua interaction
    → SPM output THAY ĐỔI theo valence update
    → = Tại sao "ấn tượng đầu tiên" quan trọng
      (valence compile NHANH, ảnh hưởng SPM DÀI HẠN)

    🟢 Fear conditioning: one-trial learning (LeDoux 1996)
    🟢 Evaluative conditioning: valence transfer qua association (De Houwer 2007)


  ⭐ SPECIAL CASE — MIXED VALENCE:

    Mẹ: L1++ (cho ăn, ôm) NHƯNG autonomy-- (ép học, cấm chơi)
      → F1: vừa warmth vừa tension (mixed body signal)
      → F2: vừa "nghe lời" vừa "tìm cách thoát"
      → = Drive.md §3 Conflict: 2 signals cùng mạnh, ngược hướng
      → = Tại sao relationship phức tạp nhất = relationship có mixed valence

    Sếp: status++ (access career) NHƯNG threat++ (có thể đuổi)
      → F1: vừa respect vừa anxiety
      → F2: vừa "impress" vừa "tự bảo vệ"
      → = Tại sao "work relationship" mệt: mixed valence → F1/F2 conflict

    → Mixed valence = F1 fire CONFLICTING signals + F2 chain MULTIPLE plans
    → = Cost TĂNG (PFC phải hold multiple drafts — PFC-Hold-Dimensions.md)
    → = Tại sao "quan hệ phức tạp" = exhausting


  ⭐ VALENCE CÓ 2 VAI TRÒ — GATE + STRUCTURAL DRIVE:

    VAI TRÒ 1 — GATE cho SPM (mô tả ở trên):
      Valence quyết định F1 fire HƯỚNG NÀO, F2 chain MỤC ĐÍCH NÀO.
      = Ảnh hưởng TỪNG EPISODE SPM fire.

    VAI TRÒ 2 — TẠO BODY-BASE EXTENSION khi strong positive:
      Khi valence STRONG POSITIVE + compiled SÂU (nhiều interaction):
        → Agent TRỞ THÀNH phần mở rộng body-base
        → Agent's wellbeing = MY wellbeing (structural)
        → = "Luồng 2" reward — SUSTAINED, BẤT KỂ F1/L1 output mỗi episode
        → = Valence-Propagation.md §2: Body-Base Extension dimension

    Vai trò 1 = ảnh hưởng SPM (Luồng 1 direction)
    Vai trò 2 = tạo structural drive NGOÀI SPM (Luồng 2)
    → 2 vai trò CÙNG TỒN TẠI, từ CÙNG 1 valence compiled

    Ví dụ: Con ruột
      Vai trò 1: valence ++ → F1 empathy FULL, F2 help/connect (gate SPM)
      Vai trò 2: valence compiled CỰC SÂU → con = body-base extension
        → Chăm con ốm DÙ F1/L1 negative (structural drive > momentary cost)

    🟡 2 vai trò valence = framework synthesis
    Chi tiết: Connection.md §3.3, Agent-Mechanism.md §12.2b
```

---

## §3 — 6 STEPS (reframed qua 2 Functions)

### §3.1 — Overview

```
⭐ 6 STEPS — CÙNG CƠ CHẾ NHƯ V1.0, NHƯNG ANNOTATE F1/F2:

  Mỗi step: vai trò cho F1 (Feeling) + vai trò cho F2 (Logic)
  Steps 1-3 = CHUẨN BỊ (chung cho cả 2 functions)
  Step 4 = F1 CORE (body simulate)
  Step 5 = BRIDGE (PFC observe → feed cả F1 lẫn F2)
  Step 6 = F2 CORE (attribute + chain logic)

  ┌──────────────────────────────────────────────────────────────┐
  │ Target detected                                              │
  │      ↓                                                       │
  │ [1] RETRIEVE — select chunks từ self repertoire              │
  │      ↓                                                       │
  │ [2] TEMPLATE MATCH — position chunks as self-as-target       │
  │      ↓                                                       │
  │ [3] PROJECTION — apply template onto target                  │
  │      ↓                                                       │
  │ [4] SIMULATION — fire template ← ⭐ F1 CORE (body fire)     │
  │      ↓                                                       │
  │ [5] OUTPUT READ — PFC observe ← BRIDGE (F1 → F2 handoff)   │
  │      ↓                                                       │
  │ [6] ATTRIBUTION — assign + chain ← ⭐ F2 CORE (logic chain) │
  └──────────────────────────────────────────────────────────────┘

  Steps có thể chạy parallel, semi-conscious, hoặc compressed.
  6 steps là analytical scaffolding, không claim serial execution.
```

### §3.2 — Step 1: Retrieve

```
🟡 RETRIEVE: Brain select chunks từ self repertoire có thể relevant cho target.

  F1 role: retrieve chunks CẢM (emotion, sensation) → sẽ dùng simulate feeling
  F2 role: retrieve chunks LOGIC (rules, patterns, history) → sẽ dùng chain predict

  SELECTION DRIVERS:
    → Target cues: facial expression, posture, vocal tone, context, speech content
      → Cues prime chunks matching similar patterns self đã experience
    → Task context: đang predict gì?
      → Emotion → affective chunks ưu tiên (F1 heavy)
      → Action → somatic + cognitive chunks (F2 heavy)
      → Strategy → logic + history chunks (F2 dominant)
    → ⭐ Per-Agent Valence GATE (§2.5):
      → Positive valence → retrieve empathy-relevant chunks
      → Negative valence → retrieve threat/strategic chunks
      → Mixed valence → retrieve CONFLICTING chunks (costly)
    → Self modality bias (Logic-Feeling.md §6):
      → Verbal-dominant → retrieve verbal chunks faster
      → Somatic-dominant → retrieve affective/somatic chunks faster
    → Schema priors: schemas linking target to categories bias retrieval
    → Recency + salience: recently experienced → activate easier
    → Emotional state: current affect gates accessible chunks
      → "State-dependent retrieval" 🟢

  ⭐ CONTEXT-DEPENDENT SELECTION (chi tiết §4):
    Cùng 1 người (tôi), khác agent → Step 1 retrieve KHÁC NHAU:
      → Với mẹ: retrieve "ngoan, nhà cửa, nghe lời"
      → Với bạn: retrieve "thoải mái, sở thích, mày tao"
      → Với sếp: retrieve "chuyên nghiệp, cẩn thận, status scan"
    → VÔ THỨC — PFC không cần decide — compiled selection
```

### §3.3 — Step 2: Template match

```
🟡 TEMPLATE MATCH: Retrieved chunks được position thành self-template.

  "Đây là cách TÔI sẽ feel/react nếu TÔI ở vị trí target."

  F1 role: template position affective/somatic chunks → ready to FIRE
  F2 role: template position logic/behavioral chunks → ready to CHAIN

  VARIATIONS:
    → Strong match (high similarity): template fit trực tiếp
      Bạn thân cùng tuổi, cùng experience → template chính xác
    → Weak match (lower similarity): template cần adjust
      Người khác giới, khác văn hóa → template approximate
    → Compound template: multiple templates retrieved, best-fit selected
      Expert psychologist → blend nhiều templates cho accuracy

  ⚠️ SIMILARITY THRESHOLD:
    Below threshold → template match FAIL entirely
    → Mouse, insect: no viable mapping → fallback Layer 1+2
    → Cục đá: no agent template → pure logic (§9)
```

### §3.4 — Step 3: Projection

```
🟡 PROJECTION: Self-template được apply LÊN target.

  "Target's internal state SHOULD match template CỦA TÔI."
  = Hypothesis assembly, NOT validated prediction.

  F1 role: "target ĐANG FEEL giống tôi sẽ feel trong tình huống này"
  F2 role: "target SẼ HÀNH XỬ giống tôi sẽ hành xử trong tình huống này"

  PROJECTION ERRORS (common):
    → Self-centeredness: assume target giống mình hơn thực tế
    → Stereotype bias: project group template lên individual
      → "Con gái thì dịu dàng" = schema projection, không phải SPM
    → Current-state bias: project own current mood bất kể target cues
      → Tôi đang vui → assume bạn cũng đang vui
    → Cultural projection: dùng own cultural chunks cho cross-cultural target

  → Projection SAI rất phổ biến — đây là lý do cần FEEDBACK (§8)
```

### §3.5 — Step 4: Simulation — F1 CORE

```
⭐ SIMULATION: Template FIRE — body THẬT SỰ respond.

  ĐÂY LÀ F1 CORE — nơi body-level simulation xảy ra.

  F1 (chính): Body fire template as-if-self-were-target
    → Affective chunks fire → slight sadness, joy, fear, anger...
    → Somatic chunks fire → tension, relaxation, pain echo...
    → = REAL body-level event (Empathy.md §4.2)
    → = Biochemistry THẬT: opioid, cortisol, oxytocin, NE
    → = Tại sao empathy CÓ COST thật

  F2 (phụ): Logic chunks fire → anticipatory chains begin
    → "Nếu tôi feel X → tôi thường do Y" chains start forming
    → Runs in background while F1 dominates Step 4
    → Fully activates at Step 6

  INTENSITY BIẾN THIÊN:
    → Zero (không hợp tính, SPM suppress, dehumanize)
    → Nhẹ (người lạ, surface scan)
    → Moderate (người quen, compiled chunks)
    → Strong (bạn thân, deep chunks + high similarity)
    → Very strong (mẹ thấy con đau, baby schema × deep compiled)
    → = GRADIENT liên tục, KHÔNG binary

  PATTERN-TYPE variation (§5):
    → Affective simulation: fire emotion chunks (fastest)
    → Somatic simulation: fire body state chunks
    → Visual-symbolic simulation: fire spatial/logic chunks
    → Verbal-cognitive simulation: fire inner speech chunks
    → Composite: multiple types blend (richest)

  🟢 Singer 2004: shared activation areas
  🟢 Dimberg 2000: facial EMG mimicry = automatic, 300ms


  ⚠️ SELF-TEMPLATE ≠ EMPATHY (Drill-L2 §3.2C — GAP-C4):

    F1 fire dùng SELF-TEMPLATE (compiled chunks CỦA MÌNH).
    Output phụ thuộc depth/content CỦA template, KHÔNG phải target's actual state.

    "Tức hơn chính nó" = COMPOUND 2 NGUỒN:
      Nguồn 1: Empathy × L2 — anger VÌ target (SPM trên target)
      Nguồn 2: Self-template — anger TỪ own compiled patterns
        (bất công → fire OWN injustice chunks → body respond TỪ mình)
      → PFC mix 2 nguồn → misattribute HẾT cho "empathy"

    VERIFY: người lạ trên mạng bị bất công → VẪN tức dù L2 ≈ 0
      = self-template thuần (Nguồn 2 alone, Nguồn 1 ≈ 0)

    HỆ QUẢ:
      → F1 output CÓ THỂ > target's actual experience
      → "Mẹ đau hơn con" = self-template (mẹ's compiled chunks) > con's actual pain
      → PFC label "empathy" = partial truth. Full mechanism = empathy + self-template.

    → Chi tiết L2 × SPM: Body-Coupling §1.4 Kênh C
    🟡 Self-template ≠ empathy distinction = Drill-L2 insight
```

### §3.6 — Step 5: Output read — BRIDGE

```
⭐ OUTPUT READ: PFC observe simulation output.

  ĐÂY LÀ BRIDGE — nơi F1 output chuyển thành F2 input.

  F1 → PFC: "body tôi đang respond thế này" (feeling observation)
    → Rich self-chunks → precise: "ambivalent gratitude tinged with guilt"
    → Thin self-chunks (alexithymia) → diffuse: "just feels bad"
    → No labels → unreadable: "something, but can't name it"

  PFC → F2: "based on body response + logic → target đang feel X"
    → F1 output becomes INPUT cho F2 chain ở Step 6
    → = HANDOFF point: feeling → logic can use

  ⚠️ BIRD & COOK BOTTLENECK (§12):
    → Step 5 REQUIRES self-awareness
    → Alexithymia = poor self-chunk labels → Step 5 FAILS
    → F1 vẫn fire (Step 4) nhưng PFC cannot READ output
    → → F2 thiếu input → prediction kém
    → = Tại sao alexithymia → empathy deficit (upstream bottleneck)
    → 🟢 Bird & Cook 2013: alexithymia drives empathy deficit, NOT autism

  Feeling.md v2.0 §3: "PFC observation of body-chunk interaction"
  = Step 5 chính là Feeling mechanism applied to SPM context
```

### §3.7 — Step 6: Attribution — F2 CORE

```
⭐ ATTRIBUTION + CHAIN: PFC assign output TO target + chain logic.

  ĐÂY LÀ F2 CORE — nơi logic chain prediction xảy ra.

  F2 (chính):
    ATTRIBUTION: "target feels/wants/will X" (assign prediction to target)
      ↓
    CHAIN LOGIC: "target feels X → target thường do Y"
      ↓
    PREDICT OUTCOME: "target do Y → kết quả Z cho tôi"
      ↓
    PLAN ACTION: "vậy tôi nên do A để optimize"

  F1 (phụ): Body tiếp tục respond nhẹ theo logic chain
    → "Tôi plan giúp bạn → body fire anticipatory reward nhẹ"
    → = Motivation signal: F1 reinforces (hoặc blocks) F2 plans

  VALENCE GATE Ở STEP 6:
    Per-Agent Valence quyết định F2 chain MỤC ĐÍCH NÀO:

    Positive: "bạn buồn → cần an ủi → tôi hỏi thăm"
      → F2 chain toward HELPING
    Negative: "đối thủ yếu → sẽ phòng thủ → tôi tấn công"
      → F2 chain toward EXPLOITING
    Neutral: "người lạ khó chịu → sẽ rời đi → tôi chờ"
      → F2 chain toward OBSERVING

  ATTRIBUTION ERRORS:
    → Over-confident: treat prediction as certainty
    → Insufficient adjustment: fail to correct for known differences
    → Projection-to-reality confusion: "what I'd feel" ≠ "what they feel"

  🟡 Framework note: Step 6 = where SPM becomes ACTIONABLE
     Steps 1-5 = internal processing. Step 6 = decision bridge.
```

### §3.8 — Time scale + consciousness

```
🟡 SPEED varies by Pattern-Type + depth + mode:

  ┌──────────────┬──────────┬──────────────┬──────────────────────┐
  │ Pattern-Type │ F1 speed │ F2 speed     │ Consciousness        │
  ├──────────────┼──────────┼──────────────┼──────────────────────┤
  │ Affective    │ ms       │ seconds      │ Mostly unconscious   │
  │ Somatic      │ seconds  │ seconds      │ Body-coupled         │
  │ Visual-symb. │ seconds  │ seconds      │ Semi-conscious       │
  │ Verbal-cog.  │ sec-min  │ sec-min      │ Mostly conscious     │
  │ Composite    │ blend    │ blend        │ Mixed                │
  └──────────────┴──────────┴──────────────┴──────────────────────┘

  F1 LUÔN nhanh hơn F2 (body-level before PFC-level)
  → = Tại sao "cảm trước, hiểu sau" (feel before think)
  → = Tại sao gut feeling đến TRƯỚC logic explanation

  UNCONSCIOUS SPM: automatic empathy, "gut feel," instant rapport
    → Hầu hết everyday agent-reading
  CONSCIOUS SPM: deliberate perspective-taking, negotiation analysis
    → Requires cognitive effort (PFC resource)
  SEMI-CONSCIOUS: rapid social reading with partial awareness
    → Most interpersonal moments

  Training (meditation, metacognition) → more process EXPLICIT
    → = Tăng khả năng correct + refine
```

---

## §4 — CONTEXT-DEPENDENT CHUNK SELECTION

### §4.1 — Vô thức tùy chọn chunks phù hợp

```
⭐ CÙNG 1 NGƯỜI, KHÁC CONTEXT → SPM TỰ CHỌN CHUNKS KHÁC:

  INSIGHT: Self-Pattern-Match KHÔNG dùng cùng 1 bộ chunks cho mọi agent.
  Mỗi khi gặp agent + context → Step 1 VÔ THỨC select bộ chunks PHÙ HỢP.

  CƠ CHẾ:
    Agent detected (VTC trigger — Agent-Mechanism.md §2)
      ↓
    Context assessed: ai đây + ở đâu + relationship gì + mục đích gì
      ↓
    Compiled patterns fire: "với AGENT NÀY trong CONTEXT NÀY → dùng chunks NÀY"
      ↓
    Step 1 Retrieve: select CỤ THỂ chunks phù hợp
      ↓
    SPM fire with SPECIFIC chunk set

  → COMPILED — không cần PFC deliberate mỗi lần
  → Giống Schema.md §1: "Schema = PATTERN dao động neuron đã ổn định"
  → Chunk selection patterns COMPILE qua repeated interaction
  → Tương tác 1000 lần với mẹ → brain biết "chunks nào work với mẹ"
```

### §4.2 — Ví dụ: mẹ vs bạn vs kẻ thù

```
⭐ CÙNG 1 NGƯỜI (TÔI) — KHÁC AGENT → KHÁC CHUNKS:

  VỚI MẸ:
    Context: gia đình, respect, hierarchy, closeness
    Chunks retrieved:
      → "Ngoan ngoãn, nghe lời" (behavioral pattern)
      → "Nghĩ tới việc nhà, quan tâm sức khỏe mẹ" (content)
      → "Xưng hô: con-mẹ" (linguistic chunks)
      → "Cẩn thận lời nói, không nói bậy" (filter)
    F1: fire respect + warmth (compiled từ years)
    F2: chain "mẹ cần gì → giúp" (helping orientation)

  VỚI NHÓM BẠN THÂN:
    Context: thoải mái, ngang hàng, sở thích chung
    Chunks retrieved:
      → "Thoải mái, tự do" (behavioral pattern)
      → "Sở thích chung, chuyện vui" (content)
      → "Xưng hô: mày-tao" (linguistic chunks)
      → "Nói bỗ bã vô tư, joke, troll" (no filter)
      → "Đề xuất tự do — nhưng không phải lúc nào cũng được chấp nhận"
    F1: fire casual warmth + fun (compiled)
    F2: chain "chơi gì tiếp → đề xuất → adjust" (peer negotiation)

  VỚI SẾP:
    Context: hierarchy nhưng khác mẹ — professional, status scan
    Chunks retrieved:
      → "Chuyên nghiệp, cẩn thận" (behavioral pattern)
      → "Report, deadline, achievement" (content)
      → "Xưng hô: em-anh/chị hoặc formal" (linguistic)
      → "Filter: không joke quá, không intimate quá" (social boundary)
    F1: fire mix respect + caution (status uncertainty)
    F2: chain "sếp cần gì → deliver → status maintain" (professional logic)

  VỚI KẺ THÙ:
    Context: threat, hostile, strategic
    Chunks retrieved:
      → "Cảnh giác, phòng thủ" (behavioral pattern)
      → "Điểm yếu, pattern hành vi đối thủ" (content)
      → "Xưng hô: lạnh, hoặc không xưng" (linguistic)
      → "Filter: không chia sẻ information" (protect)
    F1: fire tension + alertness (threat detection)
    F2: chain "kẻ thù sẽ làm gì → phòng thủ/tấn công" (strategic logic)

  → CÙNG 1 NGƯỜI (TÔI) — nhưng SPM output KHÁC HOÀN TOÀN
  → VÔ THỨC — PFC không cần "bây giờ mình phải ngoan nè"
  → COMPILED qua years of interaction → near-automatic selection
```

### §4.3 — Schema fallback khi chunks thiếu

```
⭐ KHI SPM CHUNKS THIẾU → SCHEMA VÀ LOGIC THẾ CHỖ:

  SPM quality phụ thuộc chunk library depth cho target.
  Khi library THIẾU → Step 1 Retrieve fail → brain FALLBACK.

  FALLBACK HIERARCHY:
    1. SPM with available chunks (best available)
    2. Schema template (group-level rules)
    3. Pure logic (deterministic prediction)
    4. Give up (avoid interaction)


  VÍ DỤ — "PHỤ NỮ KHÓ HIỂU":

    Đàn ông A nói: "Phụ nữ khó hiểu quá."
    Framework analysis:

    SPM chunks cho "phụ nữ" ở A:
      → Affective chunks: THIN (A ít tương tác sâu với phụ nữ)
      → Somatic chunks: THIN (khác cơ thể, ít shared experience)
      → Verbal-cognitive: MODERATE (giao tiếp surface OK)

    Step 1 Retrieve: chunks THIẾU → SPM fire COARSE
    Step 4 Simulation: F1 fire YẾU (thin library → simulation kém)
    Step 5 Output Read: "không rõ bạn C đang feel gì"

    FALLBACK → Schema: "con gái thì dịu dàng, nhạy cảm"
    FALLBACK → Logic: "vậy mình ứng xử thật nhẹ nhàng"

    Kết quả: prediction THƯỜNG SAI (schema ≠ cá nhân)
    → "Khó hiểu" = F1 prediction thường SAI → PFC label frustration
    → KHÔNG PHẢI phụ nữ "khó hiểu"
    → MÀ SPM library CỦA A cho phụ nữ = THIẾU
    → FIX: tương tác NHIỀU hơn → chunks THÊM → SPM accuracy TĂNG

    🟡 Framework claim: "khó hiểu" = confession about OWN library gap,
       not statement about target's nature


  VÍ DỤ — CROSS-CULTURAL:

    Người Việt gặp người Nhật:
      → SPM chunks cho "người Nhật" = THIẾU
      → Schema fallback: "lịch sự, kỷ luật, cúi đầu chào"
      → Logic: "nên cúi đầu, nói nhẹ"
      → Prediction: surface OK, deep MISS (miss nuances of Japanese social)

    Người Nhật gặp người Việt:
      → SPM chunks cho "người Việt" = THIẾU
      → Schema fallback: "thân thiện, ồn ào, flexible"
      → Prediction: surface OK, deep MISS

    → Cross-cultural miscommunication = BOTH sides have thin SPM libraries
    → FIX: time together → chunks build → SPM accuracy TĂNG for specific person
    → = Tại sao "sống ở nước ngoài" build empathy cross-cultural
```

### §4.4 — Einstein × Grossmann: cross-domain SPM qua chunk overlap

```
⭐ SPM WORKS KHI CHUNK OVERLAP ĐỦ — DÙ PEOPLE RẤT KHÁC:

  Einstein và Grossmann = rất khác nhau (personality, style, focus).
  NHƯNG cả 2 chia sẻ CHUNKS cốt lõi: vật lý + toán học.

  Einstein's SPM on Grossmann:
    Chunks retrieved: toán học, công thức, feeling khi stuck ở 1 bài toán
    F1: "Khi tôi đang suy nghĩ công thức → tôi muốn yên tĩnh,
         muốn có người trao đổi chunk" → simulate Grossmann CŨNG vậy
    F2: "Grossmann biết tensor calculus → tôi cần cái đó → hỏi"
    → SPM accurate VÌ chunk overlap ở domain ĐỦ

  Grossmann's SPM on Einstein:
    Chunks retrieved: vật lý lý thuyết, creative thinking patterns
    F1: "Khi tôi đang giải bài toán khó → feel challenge + excitement"
         → simulate Einstein CŨNG feel challenge khi thiếu math tool
    F2: "Einstein cần math tool mà ông ấy thiếu → tôi có → share"
    → SPM accurate VÌ chunk overlap + complementary

  Pattern-Resonance EMERGE:
    → CẢ HAI fire SPM toward nhau THÀNH CÔNG
    → F1 cả 2 phía: feel HIỂU nhau (shared feeling of intellectual work)
    → F2 cả 2 phía: plan COMPLEMENT nhau (physics + math)
    → PR emerge → trao đổi KÉO DÀI → collaboration SÂU
    → = Tại sao "đồng môn" feel close dù ít biết nhau PERSONALLY

  ⭐ QUY LUẬT: SPM không cần TOTAL overlap — cần DOMAIN-SPECIFIC overlap:
    → 5% overlap ở domain CRITICAL → SPM tốt ở domain đó
    → 95% overlap ở domain IRRELEVANT → SPM vẫn FAIL cho task hiện tại
    → = Giải thích tại sao:
      Bạn cùng nghề HIỂU nhau (domain overlap) dù personality KHÁC
      Bạn cùng tính nhưng KHÁC nghề → hiểu personal, MISS professional
      Vợ chồng nhiều năm → overlap RỘNG (personal + daily + emotional)
        → SPM accuracy CỰC CAO → "hiểu không cần nói"

  🟡 "Domain-specific overlap drives SPM quality" = framework synthesis
  🟢 Consistent: interpersonal synchrony research (Feldman 2007)
```

---

## §5 — 5 PATTERN-TYPE MODALITIES

```
⭐ SPM FIRE QUA 5 LOẠI CHUNKS KHÁC NHAU:

  Mỗi Pattern-Type = 1 kênh simulation riêng.
  F1 và F2 đều chạy qua TẤT CẢ 5 types — nhưng TỈ LỆ khác.

  ┌────────────────┬──────────────┬──────────────┬──────────────────────┐
  │ Pattern-Type   │ F1 role      │ F2 role      │ Connection type      │
  ├────────────────┼──────────────┼──────────────┼──────────────────────┤
  │ ① AFFECTIVE    │ Emotion sim  │ Emotion-based│ Cảm xúc              │
  │ (emotion)      │ Fastest, auto│ prediction   │ "Bạn buồn → tôi     │
  │                │              │              │  buồn → feel close"  │
  ├────────────────┼──────────────┼──────────────┼──────────────────────┤
  │ ② SOMATIC      │ Body state   │ Action-based │ Thể chất             │
  │ (body)         │ simulation   │ prediction   │ "Nhảy cùng → ăn ý"  │
  │                │              │              │  Sport, dance, craft │
  ├────────────────┼──────────────┼──────────────┼──────────────────────┤
  │ ③ VISUAL-      │ Pattern sim  │ Structure-   │ Trí tuệ              │
  │   SYMBOLIC     │              │ based predict│ "Hiểu nhau qua math" │
  │ (spatial/math) │              │              │  Einstein-Grossmann  │
  ├────────────────┼──────────────┼──────────────┼──────────────────────┤
  │ ④ VERBAL-      │ Inner speech │ Reasoning    │ Ngôn ngữ             │
  │   COGNITIVE    │ simulation   │ chain predict│ "Nói chuyện hợp"    │
  │ (language)     │              │              │  Philosophy, debate  │
  ├────────────────┼──────────────┼──────────────┼──────────────────────┤
  │ ⑤ COMPOSITE    │ ALL blend    │ ALL blend    │ Sâu nhất             │
  │ (tổng hợp)    │ Richest sim  │ Best predict │ Gia đình, bạn thân  │
  │                │              │              │ Vợ chồng lâu năm    │
  └────────────────┴──────────────┴──────────────┴──────────────────────┘


  ① AFFECTIVE — fastest, near-automatic:
    → Core: joy, sadness, fear, anger, disgust, surprise, love, shame, guilt...
    → Trigger: facial expression, vocal tone, body posture
    → F1: fire trong milliseconds, hardest to suppress
    → F2: "bạn đang angry → sẽ nói nặng lời → tránh"
    → Cross-species: chó cúp đuôi → affective SPM fire (dù PR không emerge)
    → Developmental priority: FIRST type to mature (14-24 tháng)
    → 🟢 Dimberg 2000: facial EMG mimicry, 300ms, pre-conscious

  ② SOMATIC — body-coupled, fast:
    → Core: tiredness, tension, pain, hunger, posture, movement quality
    → Trigger: target's observable body state, movement
    → F1: embodied understanding — "xem vận động viên → body tôi fire"
    → F2: "anh ấy mệt → sẽ chậm → tôi attack"
    → Expertise effect: expert watchers fire somatic MẠNH hơn novice
    → 🟢 Mirror system in motor cortex = learned somatic templates

  ③ VISUAL-SYMBOLIC — pattern completion, moderate speed:
    → Core: visual patterns, math, diagrams, algorithms, music notation
    → Trigger: shared problem with spatial/structural content
    → F1: "feel the math" — intuitive sense of solution (Hadamard/Einstein)
    → F2: "person X approach problem from angle A → predict next step"
    → Distinctive: enable deep connection WITHOUT personal history
    → = Tại sao "đồng nghiệp tech" feel close dù ít biết nhau personally

  ④ VERBAL-COGNITIVE — sequential, deliberate:
    → Core: inner speech, dialogue simulation, argumentation, narrative
    → Trigger: conversation, debate, text
    → F1: "feel" dialogue partner's reasoning rhythm
    → F2: "they argue X → counter-argument Y → predict response Z"
    → Slowest single-type, but most EXPLICIT (PFC-heavy)

  ⑤ COMPOSITE — richest, default cho deep relationships:
    → ALL types blend: affective + somatic + verbal + visual
    → Emerge NATURALLY trong gia đình, bạn thân, vợ chồng
    → = RICHEST simulation → HIGHEST fidelity SPM
    → = Tại sao "hiểu không cần nói" = composite compiled SÂU

  ⭐ MODALITY BIAS (Logic-Feeling.md §6):
    Mỗi người có bias toward specific Pattern-Types:
      → Verbal-dominant → seek verbal connection → gặp somatic-dominant → "không hợp"
      → Somatic-dominant → seek body-level connection → gặp verbal-dominant → "nói nhiều quá"
      → KHÔNG phải ai sai — fire KHÁC pattern-type → prediction-delta
      → = Tại sao "không hợp tính" thường = modality MISMATCH
```

---

## §6 — 4 QUALITY AXES

```
⭐ SPM OUTPUT QUALITY = f(4 AXES):

  (Agent-Mechanism.md §7)

  ┌────┬─────────────────┬────────────────────────────────────────────┐
  │ #  │ Axis            │ Ảnh hưởng F1 + F2                         │
  ├────┼─────────────────┼────────────────────────────────────────────┤
  │ ①  │ PATTERN-TYPE    │ Fire đúng loại chunks cho target cues?    │
  │    │ MATCH           │ F1: simulate đúng kênh cảm xúc?          │
  │    │                 │ F2: predict đúng loại behavior?            │
  │    │                 │ Mismatch → prediction-delta compound      │
  ├────┼─────────────────┼────────────────────────────────────────────┤
  │ ②  │ DEPTH           │ Quantity + specificity chunks về target?  │
  │    │                 │ Thin (stranger): 5-10 chunks → coarse     │
  │    │                 │ Deep (family): hundreds → high-fidelity    │
  │    │                 │ F1: deep = simulation CHÍNH XÁC            │
  │    │                 │ F2: deep = prediction CHÍNH XÁC            │
  ├────┼─────────────────┼────────────────────────────────────────────┤
  │ ③  │ SIMILARITY      │ Self-target template match quality?       │
  │    │                 │ High: cùng tuổi/văn hóa → template fit   │
  │    │                 │ Low: khác giới/species → approximate      │
  │    │                 │ Below threshold: FAIL → fallback §9       │
  ├────┼─────────────────┼────────────────────────────────────────────┤
  │ ④  │ FEEDBACK        │ Real-time calibration available?          │
  │    │                 │ Face-to-face: richest (facial+vocal+body) │
  │    │                 │ Text: reduced (verbal only)                │
  │    │                 │ None (imagined): ZERO → distortion risk   │
  │    │                 │ F1: feedback calibrate simulation REAL-TIME│
  │    │                 │ F2: feedback correct prediction ON-THE-FLY │
  └────┴─────────────────┴────────────────────────────────────────────┘

  ALL 4 axes phải meet MINIMUM threshold. 1 axis = 0 → Quality = 0:
    → High depth + zero feedback = parasocial distortion (celebrity fan)
    → High feedback + zero depth = rapid learning nhưng surface
    → High similarity + zero depth = projection (assume alike without data)

  🟡 4-axis model = framework synthesis
  🟢 Consistent: empathy research multidimensional (cognitive + affective + accuracy)
```

---

## §7 — DEVELOPMENTAL BOOTSTRAP

```
⭐ SPM KHÔNG PHẢI BẨM SINH — PHẢI BUILD QUA GIAI ĐOẠN:

  (Agent-Mechanism.md §13 — developmental timeline)


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  STAGE 0 — TRƯỚC SPM (0-6 tháng)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Có:
      → Arousal contagion (nghe khóc → khóc lây)
      → Preference cho human faces + voices
      → Hardware social drive (Connection.md ❶)
    Chưa có:
      → Self-awareness, self-chunks
      → Template formation, SPM firing
      → F1 và F2 đều CHƯA ONLINE

    🟢 Dondi 1999: newborn cry contagion = pattern matching, NOT SPM


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  STAGE 1-2 — MOTHER BOOTSTRAP (6-24 tháng) ← LOAD-BEARING
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    CƠ CHẾ:
      Infant có internal state (đói, mệt, vui)
        ↓
      Mẹ observe behavior + context
        ↓
      Mẹ interpret + label: "đói à con?"
        ↓
      Mẹ respond CONTINGENTLY (feed khi đói, comfort khi buồn)
        ↓
      Infant experience: state → label → response coupling
        ↓
      Self-chunk forms: "internal state NÀY = word NÀY = response NÀY"
        ↓
      Self-chunks accumulate → self-awareness emerges
        ↓
      SPM CÓ THỂ bắt đầu fire (rouge test milestone: 18-24 tháng)

    ⭐ CONTINGENCY QUAN TRỌNG HƠN PRESENCE:
      → Contingent: mẹ feed khi bé đói (match state)
      → Non-contingent: mẹ feed khi bé đã no (mismatch)
      → Contingent → self-chunks CHÍNH XÁC
      → Non-contingent → self-chunks CONFUSED
      → = Tại sao "có mẹ" ≠ "đủ" — cần mẹ RESPONSIVE

    🟢 Amsterdam 1972: rouge test 18-24 tháng (self-recognition)
    🟢 Svetlova 2010: empathic helping emerges 14-24 tháng
    🟢 Romanian orphanage: minimal contingency → persistent SPM deficits


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  STAGE 3 — OVER-APPLY + CALIBRATE (2-7 tuổi)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    SPM online → trẻ OVER-APPLY:
      → Attribute feelings cho búp bê, đồ vật (animism)
      → Expect mọi thứ respond emotionally
      → = SPM mới có → chưa biết BOUNDARY (agent vs non-agent)

    Calibration qua time:
      → Objects không reward SPM → giảm dần
      → Animals cho partial feedback → moderate
      → People cho rich feedback → strengthen
      → Gradually learn: agents vs non-agents

    Context-dependent selection BẮT ĐẦU COMPILE:
      → "Với mẹ → dùng chunks NÀY"
      → "Với bạn → dùng chunks KHÁC"
      → = §4 patterns bắt đầu hình thành

    🟢 Piaget 1929: animism in young children


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  STAGE 4 — FALSE BELIEF + COGNITIVE SPM (4-7 tuổi)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    → False belief task pass ~4 tuổi
    → = Cognitive SPM (verbal-cognitive Pattern-Type) mature
    → "Sally nghĩ marble ở A, dù thực tế ở B"
      = simulate Sally's KNOWLEDGE STATE khác own

    F1 + F2 relationship phát triển:
      → Trẻ bắt đầu TÁCH F1 và F2 (chưa deliberate)
      → "Bạn buồn" (F1) → "bạn sẽ không muốn chơi" (F2)
      → = Prediction chains LENGTHEN

    🟢 False belief task: Wimmer & Perner 1983


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  STAGE 5+ — LIFELONG REFINEMENT
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    SPM library CONTINUES to grow:
      → New relationships → new target-specific chunks
      → New experiences → broader template range
      → New domains → new Pattern-Types develop
      → Training → meta-awareness of own SPM process
      → Nhưng: base patterns COMPILED ở Stage 1-2 = HARDEST to change
        → = Tại sao childhood attachment = LONG-LASTING influence

    Context-dependent selection INCREASINGLY COMPILED:
      → Teenager: "phải ngoan với mẹ nhưng cool với bạn"
      → Adult: multiple role-specific SPM sets (parent, employee, friend, lover)
      → Expert: domain-specific SPM sets (therapist, negotiator, teacher)
```

---

## §8 — CALIBRATION + FEEDBACK LOOP

```
⭐ SPM LIBRARY KHÔNG TĨNH — REFINE QUA FEEDBACK:

  ┌─────────────────────────────────────────────────────────────────┐
  │  SPM fires prediction (F1 + F2)                                 │
  │       ↓                                                         │
  │  Interaction proceeds                                           │
  │       ↓                                                         │
  │  Outcome observed (target's actual behavior, response)          │
  │       ↓                                                         │
  │  Pattern-Resonance inferred retrospectively                     │
  │       ↓                                                         │
  │  Library UPDATE:                                                │
  │    - Confirmed chunks → STRENGTHENED                            │
  │    - Misfired chunks → WEAKENED                                 │
  │    - New chunks ADDED from observed target behavior             │
  │    - Context-selection patterns REFINED                         │
  │    - Retrieval heuristics IMPROVED                              │
  │       ↓                                                         │
  │  Next SPM on target: MORE ACCURATE (F1 + F2 đều cải thiện)    │
  └─────────────────────────────────────────────────────────────────┘


  TIME SCALES:
    Immediate (seconds-minutes): mid-conversation adjustment
      → "Misread tone → correct → adjust" = F1 recalibrate real-time
    Short-term (hours-days): post-conversation reflection
      → "Tưởng bạn vui nhưng thực ra stress" → F2 update
    Long-term (weeks-years): relationship history accumulates
      → Thousands of micro-calibrations → compiled model
      → Bạn thân 20 năm: SPM accuracy CỰC CAO

  F1-SPECIFIC CALIBRATION:
    → "Tôi simulate bạn buồn → thực tế bạn giận → F1 library UPDATE"
    → "Emotion mismatch → affective chunks về bạn REFINED"

  F2-SPECIFIC CALIBRATION:
    → "Tôi predict bạn sẽ rời đi → thực tế bạn ở lại → F2 logic UPDATE"
    → "Behavior mismatch → behavioral model về bạn REFINED"

  CONTEXT-SELECTION CALIBRATION:
    → "Tôi dùng formal chunks với sếp mới → sếp nói 'thoải mái đi'"
    → Context-selection pattern UPDATE: "với sếp NÀY → casual hơn"
    → = §4 patterns REFINE qua feedback


  ⚠️ LOOP FAILURE MODES:

    ① No feedback: parasocial distortion (rich library, no correction)
       → Celebrity fan: SPM on celebrity ← never corrected → distortion
    ② Misread feedback: systematic errors (alexithymia, trauma projection)
    ③ Schema suppress feedback: dehumanization (ignore target's signals)
    ④ Overwhelming feedback: overload → learning stalls
    ⑤ Delayed too long: drift compounds before correction

  🟢 Feedback-based learning: established across cognitive science
  🟡 F1/F2 separate calibration = framework synthesis
```

### §8.1 — "Biết" = compiled prediction — cùng cơ chế, khác trải nghiệm

```
⭐ DỰ ĐOÁN COMPILED → CẢM THẤY NHƯ "BIẾT" — VẪN CÙNG CƠ CHẾ:

  SPM LÀ DỰ ĐOÁN — LUÔN LUÔN. Nhưng trải nghiệm THAY ĐỔI theo mức compiled:

  ┌──────────────┬─────────────────────────┬───────────────────────────┐
  │ Mức compiled │ Trải nghiệm chủ quan    │ PFC nhìn thấy gì         │
  ├──────────────┼─────────────────────────┼───────────────────────────┤
  │ Chưa compiled│ "Đoán" — chậm, effortful│ Thấy process rõ          │
  │ (người lạ)   │ uncertain, ý thức       │ → "tôi đang cố hiểu"    │
  ├──────────────┼─────────────────────────┼───────────────────────────┤
  │ Compiled nhẹ │ "Cảm giác" — nhanh,    │ Thấy output, mờ process  │
  │ (người quen) │ semi-automatic          │ → "hình như hiểu"        │
  ├──────────────┼─────────────────────────┼───────────────────────────┤
  │ Compiled sâu │ "Biết" — instant,       │ CHỈ thấy output          │
  │ (bạn thân /  │ tự động, confident      │ Không thấy process       │
  │  gia đình)   │ = cảm giác "trust"      │ → gọi "tự nhiên"        │
  └──────────────┴─────────────────────────┴───────────────────────────┘

  BÊN TRONG: cùng 6 steps (Retrieve → Template → Project → Simulate → Read → Attribute).
  Khác: tốc độ + chunks đã compiled sâu + accuracy đã calibrate qua PR feedback.


  TẠI SAO PFC GỌI "TỰ NHIÊN":

    SPM compiled → chạy VÔ THỨC (§3.8) → PFC không thấy 6 steps
    → PFC chỉ thấy OUTPUT: "tôi hiểu người này" / "tôi hợp người này"
    → PFC KHÔNG thấy: hàng ngàn lần tương tác → calibrate → compile
    → PFC confabulate: "hợp tính", "duyên", "tự nhiên hiểu nhau"

    Đúng là "tự nhiên" — nhưng "tự nhiên" = compiled prediction chạy tự động.
    KHÔNG phải magic — là mechanism hoạt động đúng thiết kế.


  VÍ DỤ — "TỰ NHIÊN" MÀ THỰC RA LÀ COMPILED:

    ① "Tự nhiên chơi thân":
       PR Baseline cao (PR.md §7.8 "hợp tính") → SPM match dễ từ đầu
       → F1 reward → approach → lặp lại → compile
       PFC: "không biết tại sao, hợp nhau thôi"

    ② "Hiểu nhau không cần nói":
       SPM calibrate qua hàng ngàn interactions (§8)
       → Chunks sâu + chính xác → F1 instant + F2 predict đúng
       Thật ra: NÓI RẤT NHIỀU rồi → compile → bây giờ không cần nói

    ③ "Tự nhiên thấy thú vị → chơi → tình yêu":
       SPM baseline tốt → approach → tương tác → calibrate → compile
       → Valence strong positive → L2 build (body-base extension)
       PFC: "yêu tự nhiên" — "tự nhiên" = prediction compiled thành structural

    ④ "Mẹ biết con cần gì":
       20 năm SPM → chunks CỰC DEEP → F1 + F2 instant
       "Biết" = compiled prediction. SAI khi: con thay đổi mà chunks chưa update
       → §8 Loop Failure ①: no feedback → library không calibrate → prediction CŨ


  HỆ QUẢ:

    → "Biết" người khác KHÔNG CÓ đường tắt
       Chỉ có: predict → interact → feedback → calibrate → compile → "biết"
    → "Hợp tính" = compile NHANH (PR Baseline cao). Khác tốc độ, cùng cơ chế
    → Trust = compiled prediction đã proven reliable qua thời gian
    → Intuition về người = same mechanism với expert intuition (Klein 1998)

  🟢 Expert intuition = compiled pattern matching: Klein 1998, Chase & Simon 1973
  🟡 "Compiled SPM = biết" explicit framing = framework synthesis
  → Pattern-Resonance.md §7.8: "hợp tính" = PR Baseline
  → Compile-Taxonomy.md §2.2: "bác sĩ nhìn biết ngay" = same mechanism applied to domain
```

---

## §9 — THRESHOLD FAILURE + FALLBACK

```
⭐ SPM KHÔNG UNIVERSAL — FAIL THEO DỰ ĐOÁN ĐƯỢC:

  SPM FAIL khi BẤT KỲ 1 điều kiện nào:

  ① Similarity BELOW threshold:
     → Target quá khác self (côn trùng, vật vô tri)
     → No viable template → SPM cannot fire
  ② No retrievable chunks:
     → Novel situation, no matching self-experience
     → Library trống cho domain này
  ③ Pattern-Type mismatch:
     → Target cues không match available Pattern-Type
     → Verbal person gặp pure somatic target → miss
  ④ Active schema SUPPRESS (§10):
     → Layer 4 dehumanization → SPM blocked
     → Per-Agent Valence EXTREME negative → F1 suppress
  ⑤ Self-awareness failure:
     → Alexithymia → Step 5 output read fails (§12)
  ⑥ Attribution refusal:
     → Conscious rejection: "I refuse to empathize"
     → Therapeutic detachment (deliberate)


  FALLBACK HIERARCHY:

  ┌────┬───────────────────────────┬──────────────────────────────────┐
  │ #  │ Level                     │ Cơ chế                           │
  ├────┼───────────────────────────┼──────────────────────────────────┤
  │ 1  │ SPM with thin chunks      │ Best available simulation        │
  │    │                           │ F1 fire YẾU + F2 chain COARSE   │
  ├────┼───────────────────────────┼──────────────────────────────────┤
  │ 2  │ Schema template           │ Group-level rules thế chỗ        │
  │    │                           │ "Con gái thì dịu dàng" (§4.3)   │
  │    │                           │ F1 ≈ 0, F2 = schema rules       │
  ├────┼───────────────────────────┼──────────────────────────────────┤
  │ 3  │ Pure logic (mechanical)   │ Deterministic prediction         │
  │    │                           │ "Nếu A thì B" (rules, physics)  │
  │    │                           │ F1 = 0, F2 = logic thuần         │
  ├────┼───────────────────────────┼──────────────────────────────────┤
  │ 4  │ Avoid / give up           │ "Không hiểu → tránh xa"          │
  │    │                           │ F1 = 0, F2 = exit strategy       │
  └────┴───────────────────────────┴──────────────────────────────────┘


  KHI FALLBACK ĐỦ:
    → Target deterministic: physics, machines, well-understood biology
    → Rules compiled: mouse → hun khói → chạy (learned rule)
    → Routine situations: traffic, tools, daily objects
    → SPM không cần → waste effort

  KHI FALLBACK KHÔNG ĐỦ:
    → Target có intentionality: goals, preferences, decisions
    → State-dependent behavior: varies with mood, context
    → Reciprocal response: depends on self's actions
    → Strategic capacity: can deceive, plan, counter-plan
    → = Cần SPM HOẶC schema Mode 1/Mode 2 (Agent-Mechanism.md §10)

  HYBRID COMMON:
    → Real prediction often BLEND SPM + mechanical:
    → Negotiation: SPM "opponent wants X" + rule "opponent always does Y"
    → Dealing with pet: mechanical "dog runs khi mở cửa" + affective "dog seems excited"
    → = Most everyday = hybrid, adjusting blend per target + task
```

---

## §10 — REVERSED MAPPING + PROFESSIONAL SPM

### §10.1 — Schadenfreude: F1 REVERSED khi valence negative

```
⭐ KHI PER-AGENT VALENCE ÂM → F1 OUTPUT BỊ ĐẢO:

  BÌNH THƯỜNG (valence positive):
    SPM fire → F1 simulate target suffering
      → Body MÌNH fire discomfort nhẹ
      → = "Thấy bạn buồn → tôi buồn" = empathy negative
      → PFC: "bạn cần giúp"

  REVERSED (valence negative):
    SPM fire → F1 simulate target suffering
      → Body MÌNH fire REWARD thay vì discomfort
      → = "Thấy kẻ thù đau → tôi SƯỚNG" = Schadenfreude

  TẠI SAO REWARD KHI KẺ THÙ ĐAU?

    ① L0 Safety: kẻ thù yếu đi = AN TOÀN cho tôi TĂNG
       → Body detect safety increase → reward signal
    ② Justice schema: kẻ lừa đảo bị tù = fairness SATISFIED
       → Schema match → opioid release
    ③ Relative status: đối thủ yếu = vị trí tương đối TĂNG
       → Status.md: relative position matters → serotonin pathway
    ④ Prediction confirm: "thằng đó rồi cũng bị" = certainty reward
       → Prediction match → VTA satisfied

  → Schadenfreude KHÔNG phải "xấu tính"
  → = Body's NATURAL response khi threat source bị suy yếu
  → = Evolution: kẻ thù yếu = sinh tồn tốt hơn → body REWARD cho observation

  ⭐ F1 VẪN FIRE — KHÔNG PHẢI "KHÔNG CÓ EMPATHY":
    → SPM VẪN simulate target's suffering (Step 4 vẫn chạy)
    → NHƯNG valence gate ĐẢOHƯỚNG output interpretation
    → Cùng simulation, KHÁC interpretation
    → = Không phải 2 hệ thống khác nhau — 1 hệ thống, valence đảo hướng

  🟢 Takahashi 2009: ventral striatum activates khi misfortune befalls envied person
  🟢 Singer 2006: empathic response modulated by perceived fairness
  🟢 Cikara 2014: counter-empathy in competitive contexts
```

### §10.2 — Sadism: F1 reversed + active creation

```
⭐ SADISM ≠ DEHUMANIZATION — KHÁC CĂN BẢN:

  DEHUMANIZATION:
    → F1 SUPPRESS → target = object
    → SPM tắt → KHÔNG simulate suffering
    → Giết COLD — "không phải người" → no simulation → no feeling
    → = "Mày không phải người" (Connection.md §0.2)
    → Bandura 1999: Moral Disengagement

  SADISM:
    → F1 FIRE STRONG + REVERSED
    → Target PHẢI LÀ AGENT (nếu object → nothing to "enjoy")
    → Body simulate target suffering → REVERSED → REWARD
    → ACTIVE CREATION of suffering (thay vì chỉ observe)
    → = REQUIRES empathy mechanism HOẠT ĐỘNG (để simulate)
    → → Chỉ HƯỚNG output bị đảo

  ⚠️ INSIGHT: Sadism REQUIRES target remain AGENT:
    → Nếu target bị dehumanize → F1 suppress → no simulation
    → → No simulation → no enjoyment of suffering
    → → Sadist CẦN target PHẢN ỨNG (biểu hiện đau)
    → → = F1 input cần target's OBSERVABLE suffering
    → → = Dehumanized target → sadist MẤT reward source

  → Sadism = SPM intact + valence extreme negative + F1 reversed
  → Dehumanization = SPM suppress + valence extreme → object treatment
  → 2 paths KHÁC NHAU từ cùng extreme negative valence

  🟡 Framework claim — consistent nhưng sensitive topic
```

### §10.3 — Professional SPM conflicts

```
⭐ PROFESSIONAL ROLES YÊU CẦU SPM NHƯNG F1/F2 CONFLICT:

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CASE A — BÁC SĨ PHẪU THUẬT
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Required: F2 (logic) FULL — plan surgery steps precisely
    F1 cost: biết bệnh nhân đau → F1 fire empathy nhẹ → body discomfort
    Training: dampen F1 through professional detachment
    Risk: F1 cost tích lũy → burnout, compassion fatigue
    Recovery: supervision, peer support, rest


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CASE B — THERAPIST
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Required: F1 (feeling) HIGH — empathize deeply with client
    F2 supplementary: maintain therapeutic framework
    Risk: F1 OVERLOAD → empathy fatigue, secondary traumatization
    Training: supervision, self-care, deliberate F1/F2 balance
    🟢 Figley 2002: compassion fatigue in helping professionals


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CASE C — INTERROGATOR / QUAN PHỦ
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Required: BOTH F1 + F2 — must SIMULATE prisoner's response
    to predict which method effective

    4 Sub-cases tùy Per-Agent Valence:

    C1: Neutral valence (chỉ làm nhiệm vụ):
      → F1 fire empathy dissonance (simulate suffering → body cost THẬT)
      → F2 chain: "method X → response Y → information Z"
      → Cost: F1 tích lũy → ÁM ẢNH, PTSD, moral injury
      → 🟢 Litz 2009: moral injury in military personnel

    C2: Negative valence (thù hận thật):
      → F1 fire REVERSED (some reward from suffering)
      → F2 chain: strategic + hostile
      → Cost GIẢM so với C1 (reversed = less dissonance)
      → Nhưng VẪN tích lũy (body fire nhiều = mệt)

    C3: Dehumanized (target = not human):
      → F1 SUPPRESS → no simulation
      → F2 chỉ: mechanical logic "đánh bao nhiêu thì khai"
      → Cost THẤP NHẤT cho bản thân
      → NHƯNG predict KÉM hơn (miss psychological data)

    C4: Sadistic (enjoy suffering):
      → F1 fire STRONG + REVERSED → active reward
      → F2 chain: maximize suffering (NOT maximize information)
      → MỤC ĐÍCH LỆCH: từ "lấy lời khai" → "thỏa mãn reward"
      → = Professional failure — goal corruption


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CASE D — SOLDIER IN COMBAT
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Required: F2 (strategic) → predict enemy behavior
    F1 default: fire empathy on enemy (they're agents too)
    Training: partial dehumanize (schema "they're the enemy")
    → Reduce F1 cost during combat

    Post-combat: F1 REBOUNDS — suppressed empathy RETURNS
    → "Tôi đã giết người" = F1 re-fire on memories → guilt, PTSD
    → 🟢 Perpetrator trauma: documented across cultures
    → 🟢 Milgram 1963: extreme distress khi ordered to harm

    → = F1 KHÔNG THỂ suppress VĨNH VIỄN
    → = Schema suppress chỉ TẠM THỜI
    → = Khi schema weakens → F1 fire on compiled memories → PTSD
```

### §10.4 — Moral injury = F1 cost tích lũy

```
⭐ MORAL INJURY: F1 BỊ BUỘC FIRE TRÊN ACTIONS MÂU THUẪN VỚI VALUES:

  (Cortisol-Baseline.md v2.0 §9: stress cascade + long-term damage)

  CƠ CHẾ:
    Person performs action gây harm cho others
      ↓
    F1 fire on victim's suffering (automatic, cannot suppress 100%)
      ↓
    Body response: empathy dissonance (cortisol, guilt signals)
      ↓
    Schema conflict: "tôi là người tốt" vs "tôi vừa gây hại"
      ↓
    Repeated → F1 cost TÍCH LŨY → baseline shift UP
      ↓
    → Moral injury: cortisol baseline drift + identity schema damage

  KHÁC PTSD THÔNG THƯỜNG:
    PTSD: "tôi bị đe dọa" = threat TO self
    Moral injury: "tôi đã gây hại" = threat FROM self
    → Moral injury = F1 fire on OWN actions → self-as-threat

  AI AI CŨNG CÓ THỂ BỊ:
    → Soldier, interrogator (obvious)
    → Doctor who makes mistake → patient suffers → F1 on patient
    → Manager who fires employee → F1 on employee
    → Parent who punishes too harshly → F1 on child's suffering
    → = Any role requiring actions that cause others harm

  ⭐ 2-LUỒNG GIẢI THÍCH TẠI SAO CÙNG F1 COST → KHÁC OUTCOME:

    Moral injury / burnout KHÔNG CHỈ phụ thuộc F1 cost (Luồng 1).
    Còn phụ thuộc Luồng 2 (structural connection) CÓ BÙ hay KHÔNG:

    BÁC SĨ chăm bệnh nhân lạ:
      L1: F1 fire empathy dissonance LIÊN TỤC (negative)
      L2: ≈ 0 (bệnh nhân lạ → chưa compiled thành body-base extension)
      → F1 cost TÍCH LŨY, KHÔNG ĐƯỢC BÙ → burnout, moral injury

    MẸ chăm con ốm (CÙNG F1 cost):
      L1: F1 fire empathy dissonance LIÊN TỤC (negative)
      L2: STRONG positive (con = body-base extension)
      → F1 cost ĐƯỢC BÙ bởi L2 structural reward → KHÔNG burnout
      → Chăm con = feed body-base MÌNH (dù F1 output negative)

    → CÙNG mechanism (F1), CÙNG cost level → KHÁC outcome
    → Biến số quyết định: Luồng 2 có đủ bù Luồng 1 hay không
    → = Tại sao "người tận tụy với nghề" cần professional anchor
      (anchor schema = proxy L2 bù F1 cost — Connection.md §3.3)

    Chi tiết 2-luồng: Connection.md §3.3, Valence-Propagation.md §2,
    Agent-Mechanism.md §12.2b

  🟢 Litz 2009: moral injury — distinct from PTSD
  🟢 Perpetrator trauma research: established across contexts
  🟢 Milgram 1963: participants showed extreme distress
  🟢 Figley 2002: compassion fatigue in helping professionals
  🟡 F1 cost tích lũy as mechanism = framework synthesis
  🟡 L1/L2 compensation model = framework synthesis (Connection.md §3.3)
```

### §10.5 — Strategic SPM: suppress cues + fake cues + meta-SPM

```
⭐ CHIẾN LƯỢC GIA DÙNG SPM × CHỐNG SPM ĐỒNG THỜI:

  INSIGHT: Đối thủ dùng F1 trên BẠN = simulate body-state bạn
  qua observable cues (mặt, giọng, posture, micro-expressions).
  → MANAGE observable cues = MANAGE đối thủ's SPM input.


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CHIẾN LƯỢC ① — POKER FACE: Giấu cues, chặn F1 đối thủ
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Cơ chế:
      → SUPPRESS observable body-state outputs (mặt, giọng, posture)
      → Đối thủ SPM Step 1: ít cues → ít chunks match → retrieve THIN
      → Đối thủ F1: simulation COARSE (thiếu input)
      → Đối thủ F2: prediction KÉM → plan sai → bất lợi

    Ví dụ:
      → Poker player: suppress micro-expressions → đối thủ đọc sai
      → Quan chức chính phủ: giữ vẻ bình thường trước camera
      → Tướng quân: bình tĩnh trước binh lính dù tình thế nguy hiểm
        → 2 mục đích: ① chặn SPM đối thủ ② ổn định F1 quân lính
           (lính SPM on tướng: "tướng bình tĩnh → an toàn" → cortisol giảm)

    Training:
      → Mode B (Logic-dominant) cho BẢN THÂN: suppress F1 output ra ngoài
      → Emotional regulation: không suppress FEELING, suppress BIỂU HIỆN
      → = Tại sao lãnh đạo giỏi "poker face" = compiled skill, KHÔNG phải cold

    ⚠️ NHƯNG: Micro-expressions VẪN LỌT:
      → F1 fire = body-level event → micro-expressions (~40ms) TỰ ĐỘNG lọt
      → Training giảm nhưng KHÔNG TẮT 100%
      → Expert reader (FBI, đối thủ kỳ cựu) CÓ THỂ detect micro-expression
      → = Tại sao "giấu hoàn toàn" gần như bất khả thi với expert observer
      → 🟢 Ekman 2003: micro-expressions leak even when suppressed
      → 🟢 Ekman & Friesen 1969: FACS — Facial Action Coding System


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CHIẾN LƯỢC ② — FAKE CUES: Cho đối thủ dùng SAI SPM
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Cơ chế:
      → Cố tình lộ trạng thái GIẢ (giả sợ, giả yếu, giả tức giận, giả bình thản)
      → Đối thủ SPM Step 1: retrieve chunks matching FAKE cues
      → Đối thủ F1: simulate trạng thái GIẢ → body respond → "ông ấy đang sợ"
      → Đối thủ F2: chain logic trên prediction SAI → plan SAI → bất lợi

    Ví dụ lịch sử:
      → "Thành không kế" (Tam Quốc): Gia Cát Lượng ngồi gảy đàn bình thản
        trên thành trống quân → Tư Mã Ý F1 fire: "bình thản = có kế"
        → F2: "có phục binh → rút" → thực tế: KHÔNG có quân
        → Tư Mã Ý SPM accuracy BỊ HACK qua fake cue + schema override
           ("Gia Cát Lượng luôn có kế" = schema amplify fake cue)
      → Bluff trong poker: giả confident khi bài yếu
      → Ngoại giao: giả cứng rắn khi thực tế sẵn sàng nhượng bộ

    TẠI SAO FAKE CUES HIỆU QUẢ:
      → F1 fire trên CUES, không phải BELIEFS
      → Dù đối thủ NGHI giả → F1 VẪN fire trên cues observable
      → F1 output conflicting: "cues nói X, logic nói có thể giả"
        → PFC phải hold 2 drafts → tốn resource → uncertainty TĂNG
      → = Fake cues HIỆU QUẢ ngay cả khi đối thủ biết CÓ THỂ giả
        → Vì F1 automatic → cannot unsee → phải EFFORT suppress

    🟢 DePaulo et al. 2003: meta-analysis — deception detection accuracy ≈ 54%
       (barely above chance → people BAD at detecting lies)
    🟢 Sun Tzu: "All warfare is based on deception" (~500 BCE)
    🟡 "Hack SPM input" = framework framing of established deception research


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CHIẾN LƯỢC ③ — META-SPM: SPM trên SPM process
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    CẤP ĐỘ CAO NHẤT: predict đối thủ đang dùng SPM NÀO trên mình,
    rồi manipulate input cho đối thủ.

    Cơ chế:
      → Level 1: "Tôi SPM on đối thủ" (đọc đối thủ)
      → Level 2: "Đối thủ SPM on tôi" (đối thủ đang đọc tôi)
      → Level 3: "Tôi predict đối thủ SPM on tôi THẾ NÀO"
        → = Meta-SPM: SPM on OPPONENT'S SPM PROCESS
      → Level 4: "Tôi control cues tôi lộ ra → control Level 2"
        → = Manipulate đối thủ's SPM input

    Ví dụ:
      → Poker: "Anh ấy nghĩ tôi đang bluff (Level 2) → vậy tôi sẽ
        thật sự có bài tốt lần này (control Level 2 → win)"
      → Ngoại giao: "Họ expect tôi nhượng bộ (Level 2) → tôi giả
        cứng rắn (fake cue) → họ nhượng bộ trước"
      → Binh pháp: "Địch nghĩ ta yếu (Level 2) → ta giả yếu thêm
        → địch tiến → phục kích"

    ĐÒI HỎI:
      → SPM quality CỰC CAO ở cả F1 lẫn F2
      → MODE SWITCHING nhanh: Mode B (suppress own) ↔ Mode C (read other)
      → Compiled chunks cho ĐỐI THỦ CỤ THỂ sâu
        → "Biết địch biết ta, trăm trận trăm thắng" (Tôn Tử)
          = SPM library depth cho đối thủ + self-awareness depth
      → PFC resource CỰC LỚN (hold multiple levels cùng lúc)
        → = Tại sao strategic thinking = EXHAUSTING
        → = Tại sao "người già dặn" (compiled meta-SPM) → less exhausting
           vì đã compiled → cost giảm

    🟢 Recursive Theory of Mind research: humans can reason about
       others' beliefs about beliefs (Level 2-3 common, Level 4+ rare)
    🟢 Diplomatic protocol: formal behavior REDUCES readable cues
       → designed to level playing field (mọi người cùng suppress)
    🟡 "Meta-SPM" = framework framing of recursive ToM


  ⭐ TỔNG HỢP 3 CHIẾN LƯỢC:

    ┌──────────────┬─────────────────────┬─────────────────────────────┐
    │ Chiến lược   │ SPM mechanism       │ Mục đích                    │
    ├──────────────┼─────────────────────┼─────────────────────────────┤
    │ ① Poker face │ Suppress OWN cues   │ Starve đối thủ's F1 input  │
    │              │ (Mode B on self)    │ → prediction coarse          │
    ├──────────────┼─────────────────────┼─────────────────────────────┤
    │ ② Fake cues  │ Feed WRONG cues     │ Đối thủ F1 fire on giả     │
    │              │ to đối thủ          │ → prediction SAI            │
    ├──────────────┼─────────────────────┼─────────────────────────────┤
    │ ③ Meta-SPM   │ SPM on opponent's   │ Predict + control đối thủ's│
    │              │ SPM process         │ entire SPM chain            │
    └──────────────┴─────────────────────┴─────────────────────────────┘

    → TẤT CẢ 3 dùng CÙNG mechanism (SPM F1/F2) — chỉ HƯỚNG khác:
      ① = SPM defense (chặn input)
      ② = SPM offense (feed wrong input)
      ③ = SPM meta (predict + control full chain)

    → "Chiến lược gia giỏi" = SPM quality CAO + compiled meta-SPM
    → "Người già dặn khó đọc" = compiled suppress + compiled meta-SPM
      → Cost đã giảm (compiled) → sustainable long-term
    → "Trẻ con dễ đọc" = chưa compiled suppress → cues lộ rõ
      → = Developmental: suppress skill COMPILE qua Stage 3-5 (§7)
```

---

## §11 — USE CASES (reframed qua F1/F2 × Valence)

```
⭐ SPM LÀ GENERAL-PURPOSE — KHÔNG CHỈ AGENT-READING:

  Cùng mechanism (6 steps + F1 + F2) — khác context → khác ứng dụng.

  ┌────┬────────────────────┬────────────────┬────────────────┬──────────────┐
  │ #  │ Use case           │ F1 role        │ F2 role        │ Key insight  │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 1  │ Empathy            │ DOMINANT       │ Support        │ Core use     │
  │    │ (feel with other)  │ Body simulate  │ Plan help      │ Empathy.md   │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 2  │ Teaching           │ Simulate       │ Plan explain   │ SPM on       │
  │    │                    │ student's      │ strategy       │ learner state│
  │    │                    │ confusion      │                │              │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 3  │ Negotiation        │ Simulate       │ Predict moves  │ Strategic    │
  │    │                    │ opponent's     │ Plan counter   │ F2 heavy     │
  │    │                    │ desires        │                │              │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 4  │ Self-planning      │ Simulate       │ Plan actions   │ SPM on       │
  │    │ (future self)      │ future self    │ for future     │ FUTURE SELF  │
  │    │                    │ feeling        │                │              │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 5  │ Fiction engage     │ DOMINANT       │ Plot predict   │ Library      │
  │    │ (novels, films)    │ Character sim  │                │ EXPANSION    │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 6  │ Moral reasoning    │ Simulate       │ Evaluate       │ F1 = moral   │
  │    │                    │ victim's pain  │ consequences   │ intuition    │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 7  │ Learning from      │ Simulate       │ Extract        │ Expert → SPM │
  │    │ models             │ expert's state │ technique      │ → chunk build│
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 8  │ Dialogue with      │ Simulate       │ Get "advice"   │ Mode 2       │
  │    │ internalized figure│ mentor's resp  │ from schema    │ (virtual)    │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 9  │ Schadenfreude      │ REVERSED       │ Exploit/       │ §10.1        │
  │    │ (enemy suffering)  │ Body reward    │ observe        │ Negative val │
  ├────┼────────────────────┼────────────────┼────────────────┼──────────────┤
  │ 10 │ Strategic defense  │ Simulate       │ Plan defense   │ §10.3 C1     │
  │    │ (military, legal)  │ threat assess  │ counter-move   │ Professional │
  └────┴────────────────────┴────────────────┴────────────────┴──────────────┘

  → TẤT CẢ 10 use cases dùng CÙNG 6 steps + F1 + F2
  → Chỉ KHÁC: valence gate + context → chunks KHÁC → output KHÁC
  → SPM = GENERAL-PURPOSE self-template simulator, NOT agent-only module

  🟡 Framework claim: "SPM general-purpose" = consistent với simulation theory
```

---

## §12 — ALEXITHYMIA + BIRD & COOK 2013

```
⭐ DECISIVE ARCHITECTURAL EVIDENCE:

  🟢 Bird & Cook 2013 (Translational Psychiatry):
     Empathy deficits attributed to autism ACTUALLY driven by
     ALEXITHYMIA (poor self-labeling), not autism per se.
     Autistic WITHOUT alexithymia → empathy INTACT.
     Alexithymic WITHOUT autism → empathy DEFICIT.

  IMPLICATION CHO 2 FUNCTIONS:

    Alexithymia → poor self-chunks
      ↓
    Step 1 Retrieve: thin chunks available
      ↓
    Step 4 F1: simulation POOR (thin template → coarse output)
      ↓
    Step 5 Bridge: PFC cannot READ F1 output (poor self-labels)
      ↓
    Step 6 F2: thiếu F1 input → prediction COARSE
      ↓
    → BOTH F1 AND F2 degraded — vì BOTH depend on self-chunk quality

  TẠI SAO DECISIVE:
    ① Alternative (hardware mirror module) PREDICTS:
       empathy should work even with alexithymia (hardware intact)
    ② OBSERVATION: alexithymia + empathy deficit
       → CONTRADICTS hardware module hypothesis
    ③ Framework PREDICTS: poor self-chunks → poor SPM → poor empathy
       → MATCHES observation exactly
    ④ Intervention follows: train self-awareness → SPM improves → empathy improves
       → CONFIRMED by meditation + focusing research

  ALEXITHYMIA SPECTRUM (not binary):
    → ~10% population clinically significant 🟢
    → Many more partial (thin chunks ở specific emotional domains)
    → Self-chunk library quality = continuous
    → = Tại sao "EQ" varies — not talent, but library DEPTH

  INTERVENTION:
    → 🟢 Focusing (Gendlin 1978): access felt sense
    → 🟢 Mindfulness of body: build interoceptive chunks
    → Emotional labeling therapy: explicit vocabulary practice
    → Body-based: yoga, somatic experiencing, breathwork
    → SUCCESS CRITERION: self-chunks improve → empathy improves AS SIDE EFFECT
```

---

## §13 — ToM LITERATURE MAPPING

```
🟡 SPM FRAMEWORK × MAINSTREAM THEORY OF MIND:

  SIMULATION THEORY (Goldman, Gallese):
    → "Understand others by SIMULATING their state using own machinery"
    → Framework ALIGNS: SPM = explicit 6-step simulation mechanism
    → Framework EXTENDS: 5 Pattern-Types, 4 axes, F1/F2 split, valence gate

  THEORY THEORY (Gopnik, Meltzoff):
    → "Understand others by applying THEORIES of how minds work"
    → Framework position: Theory = Layer 4 schema override (Mode 1)
    → NOT replacement — SUPPLEMENT for when SPM fails

  DUAL PROCESS (Kahneman):
    → System 1 (fast, automatic) ≈ F1 (body simulation)
    → System 2 (slow, deliberate) ≈ F2 (logic chain)
    → Framework COMPATIBLE — maps naturally

  FALSE BELIEF TASK (Wimmer & Perner 1983):
    → Pass ~4 years = cognitive SPM (verbal-cognitive Pattern-Type) matures
    → Earlier helping (14-24m) = affective SPM (pre-cognitive)

  PREDICTIVE PROCESSING (Friston):
    → SPM could be specific instance of general predictive processing
    → Self-template = prior model; feedback = error signal
    → Open question: distinct or subset? (§16)

  FRAMEWORK CONTRIBUTION beyond existing literature:
    ① Explicit 6-step mechanism (others describe outcomes, not steps)
    ② 5 Pattern-Type taxonomy (extends cognitive vs affective binary)
    ③ ⭐ 2 Functions F1/F2 (not in mainstream ToM literature)
    ④ ⭐ Valence gate determines direction (not in standard empathy research)
    ⑤ ⭐ Context-dependent selection (compiled, unconscious)
    ⑥ Bird & Cook as architectural (upstream bottleneck)
    ⑦ Schema override as third pathway (Mode 1/2)
    ⑧ Pattern-Resonance as retrospective ground truth
```

---

## §14 — TRAINING + CULTIVATION

```
⭐ SPM QUALITY LÀ TRAINABLE — EVIDENCE-BASED METHODS:


  FOUNDATION: Self-chunk training (upstream — Bird & Cook):
    → PHẢI rebuild self-chunks TRƯỚC → empathy improves AS SIDE EFFECT
    → 🟢 Focusing (Gendlin 1978): 6-step felt sense access
    → 🟢 Mindfulness of feelings: observe emotions without judgment
    → Emotional labeling therapy: explicit vocabulary practice
    → Body-based: yoga, tai chi, dance, somatic experiencing

  F1-SPECIFIC TRAINING:
    → Deep listening (Rogers client-centered): F1-dominant practice
    → Compassion meditation (Metta): positive F1 firing practice
    → Fiction engagement: simulate characters safely
    → Cross-cultural immersion: broaden template range

  F2-SPECIFIC TRAINING:
    → Perspective-taking exercises: deliberate "if I were them" reasoning
    → Strategic games: chess, negotiation practice
    → Post-interaction reflection: "what did I predict? what happened?"
    → Journaling: articulate predictions explicitly

  CONTEXT-SELECTION TRAINING:
    → Diverse social engagement: build more context-specific chunk sets
    → Role-play: practice switching between contexts deliberately
    → Travel: expose to unfamiliar social contexts → build new selection patterns

  MODE-SWITCHING TRAINING (§2.4):
    → Therapists: train Mode A (F1-dominant) deliberately
    → Negotiators: train Mode B (F2-dominant) deliberately
    → Leaders: train Mode C balance for optimal social navigation

  LIMITS:
    → Individual variation: some plateau early
    → Baseline self-chunk library depth matters
    → Trauma/dissociation may require specialized approaches
    → Ceiling unknown — framework doesn't claim unlimited improvement
```

---

## §15 — AI ERA IMPLICATIONS

```
⭐ DIGITAL ERA × SPM — RISKS + OPPORTUNITIES:

  RISK 1 — Screen replaces feedback-rich interaction:
    → Text/emoji/video = reduced Pattern-Type engagement
    → F1: thin input → thin simulation → thin library build
    → F2: less calibration data → prediction accuracy stalls
    → DEVELOPMENTAL CONCERN: children raised screen-primary → thin SPM

  RISK 2 — Parasocial at scale:
    → SPM fire on celebrities, influencers, AI companions
    → Rich template building WITHOUT calibration → DISTORTION
    → AI companions: simulate social interaction convincingly
      → But AI doesn't SPM user back → one-way → distortion

  RISK 3 — AI-triggered SPM without agent reality:
    → Coherent AI responses trigger SPM even when user KNOWS AI isn't agent
    → SPM fires on CUES, not beliefs
    → Long-term: library distortion (agents "feel like" AI)
    → 🟡 Agent-Mechanism.md §12.5-12.7: AI era concern

  OPPORTUNITY — Training at scale:
    → Meditation apps, journaling tools, AI-assisted therapy
    → SPM literacy taught explicitly
    → Cross-cultural exposure via media
    → → NET EFFECT unclear — tools exist but uptake varies

  ⭐ FRAMEWORK PREDICTION:
    → SPM mechanism becomes INCREASINGLY RELEVANT as AI interfaces with
      agent-reading at scale
    → Individual SPM literacy = critical skill for AI era
    → Society-level impact significant if unaddressed
```

---

## §16 — OPEN QUESTIONS

```
  1. F1/F2 dissociability: Are they truly separate processes or 1 process
     with different output channels? (framework claims 2 functions)
  2. Valence gate mechanism: precise neural implementation?
  3. Context-selection compilation: how many context-specific sets per person?
  4. Reversed mapping neuroscience: precise circuitry of Schadenfreude?
  5. Moral injury → PTSD: exact pathway from F1 cost to clinical disorder?
  6. SPM quality operationalization: how to measure directly?
  7. Training ceiling: practical upper limit?
  8. Cross-cultural bootstrap variation: systematic differences?
  9. Predictive processing integration: SPM as subset of general prediction?
  10. AI interaction: how sustained AI interaction affects human SPM library?
  11. Group-scale: can Pattern-Resonance emerge beyond dyads?
  12. Schema fallback boundary: when does brain switch from thin SPM to schema?
```

---

## §17 — HONEST ASSESSMENT

```
  ESTABLISHED (🟢):

    🟢 Bird & Cook 2013: alexithymia drives empathy deficit (decisive)
    🟢 Mother contingency + self-chunk formation (attachment research)
    🟢 Rouge test 18-24m: self-awareness milestone (Amsterdam 1972)
    🟢 Empathic helping 14-24m (Svetlova 2010)
    🟢 Facial EMG mimicry automatic 300ms (Dimberg 2000)
    🟢 Shared activation areas (Singer 2004)
    🟢 Social Baseline Theory (Coan 2015)
    🟢 Schadenfreude: ventral striatum activation (Takahashi 2009)
    🟢 Counter-empathy in competitive contexts (Cikara 2014)
    🟢 Empathy modulated by fairness (Singer 2006)
    🟢 Moral injury distinct from PTSD (Litz 2009)
    🟢 Perpetrator trauma (cross-cultural documentation)
    🟢 Milgram 1963: obedience + distress
    🟢 Meditation training improving emotional processing (Tang 2015)
    🟢 Focusing (Gendlin 1978): felt sense access
    🟢 Dual Process Theory (Kahneman 2011)
    🟢 Moral Disengagement / dehumanization (Bandura 1999)
    🟢 Romanian orphanage: bootstrap disruption evidence

  FRAMEWORK SYNTHESIS (🟡):

    🟡 2 Functions F1/F2: consistent with dual-process, novel framing
    🟡 6-step mechanism: novel formalization, conceptually coherent
    🟡 5 Pattern-Type taxonomy: extends cognitive/affective binary
    🟡 4 quality axes model
    🟡 Context-dependent chunk selection: consistent with schema research
    🟡 Per-Agent Valence as gate: consistent with empathy modulation research
    🟡 Reversed mapping mechanism: consistent with Schadenfreude research
    🟡 Sadism vs dehumanization distinction: logically coherent
    🟡 Professional SPM conflict model: consistent with burnout research
    🟡 Moral injury as F1 cost: consistent with Litz 2009 framework
    🟡 Schema fallback hierarchy: consistent with cognitive fallback research
    🟡 Domain-specific overlap drives SPM quality

  HYPOTHESIS (🔴):

    🔴 Precise F1/F2 neural dissociability
    🔴 Context-selection compilation mechanism
    🔴 Valence gate precise circuitry
    🔴 Training ceiling predictions
    🔴 AI library distortion long-term effects
    🔴 Quantitative axis interactions

  OVERALL CONFIDENCE:
    → Mechanism framing: 🟢 STRONG
    → 2 Functions model: 🟡 SOLID framework synthesis, testable
    → Reversed mapping: 🟢 Strong research support for phenomenon
    → Professional conflicts: 🟢 Strong evidence, 🟡 framework mapping
    → Quantitative claims: 🔴 Pending measurement protocols
```

---

## §18 — CROSS-REFERENCES

```
  PARENT + SIBLING:
    → Agent-Mechanism.md — integration hub, §5 SPM preview
    → Pattern-Resonance.md v1.1 — emergent mutual phenomenon (retrospective)
      §7.10 F1/F2 resonance quality: F1+F1 deep, F1+F2 functional, F2+F2 transactional

  MECHANISM FILES:
    → Chunk.md v2.0 — chunk substrate, compilation
    → Feeling.md v2.0 — PFC observation interface (Step 5 = Feeling applied)
    → Logic-Feeling.md — 2 processing modes, parallel, modality bias
    → Valence-Propagation.md v1.3 — per-entity valence, chain propagation
    → Body-Coupling.md v1.0 — coupling mechanism (builds ON SPM):
      SPM fire tích lũy → coupling compile → sustains independent of SPM
    → Body-Feedback-Mechanism.md — Chunk-Miss / Gap / Shift dynamics

  OBSERVATION FILES:
    → Connection.md — 3 generative primitives, 8 pathways, SPM × PR
    → Empathy.md — SPM function applied to other agents
    → Status.md v2.0 — Resource Access Map, status scan
    → Protect.md — ownership, loss aversion
    → Threat.md — NE cascade, PFC disconnect

  CORE:
    → Core-v7.8-Draft.md — cycle architecture
    → Cortisol-Baseline.md v2.0 — stress cascade, moral injury pathway

  APPLICATION:
    → Imagine-Final.md — imagination as simulator
    → Somatic-Articulation-Loop.md — body → words
    → AI-Schema-Detection.md — AI interaction × SPM

  RESEARCH ANCHORS:
    → Bird & Cook 2013 (decisive)
    → Singer 2004, 2006 (shared activation + fairness modulation)
    → Takahashi 2009, Cikara 2014 (Schadenfreude / counter-empathy)
    → Litz 2009 (moral injury)
    → Bandura 1999, Haslam 2006 (dehumanization)
    → Gendlin 1978 (Focusing)
    → Kahneman 2011 (Dual Process)

  STATUS:
    → v2.0 COMPLETE — rewrite từ v1.0 (1518L)
    → NEW: §2 (2 Functions F1/F2), §4 (Context-dependent selection),
      §10 (Reversed mapping + Professional SPM)
    → REFINED: §3 (6 steps qua F1/F2 lens), §5 (F1/F2 per type),
      §9 (valence-driven fallback), §11 (F1/F2 use cases)
    → KEPT: §5-§8 foundations, §12 Bird & Cook, §13 ToM, §14-§15
    → Backup: backup/Self-Pattern-Match-v1.0-forward-backup.md

  HEALTH CONDITIONS DRILL (v2.4):

    LATE DIAGNOSIS IDENTITY RE-COMPILE (ADHD + Autism):
      → ADHD-Observation.md §10, Autism-Observation.md §10:
        Late diagnosis → "SPM re-compile": entire self-model REFRAMES
        Past behaviors explained → chunks re-link → identity shift
      → SPM trước: "tôi lazy/weird" (chunks tagged self-blame)
      → SPM sau: "tôi ADHD/autistic" (chunks re-tagged = external cause)
      → = Massive Chunk-Shift (BFM §3.1): content unchanged, valence SHIFTS

    C-PTSD = SPM COMPILED UNDER CHRONIC THREAT (PTSD-Analysis §11):
      → Chronic threat → SPM compile "world = unsafe, self = broken"
      → ≠ single trauma PTSD (event-specific)
      → = DEVELOPMENTAL IDENTITY: SPM chunks compiled DURING formation
      → Background-Pattern.md §9.1: chronic childhood = high density BP
      → SPM × BP compound → "personality" (actually: threat-compiled SPM)

    Cross-refs:
      → ADHD-Observation.md v1.2 §10, Autism-Observation.md v1.0 §10
      → PTSD-Analysis.md v1.0 §11 (C-PTSD)
```

---

> *Bạn thấy bạn thân khóc → body bạn buồn nhẹ. Đó là F1.*
> *Bạn nghĩ: "bạn cần an ủi." Đó là F2.*
>
> *Bạn thấy kẻ thù gục ngã → body bạn... nhẹ nhõm. Vẫn F1 — nhưng REVERSED.*
> *Bạn nghĩ: "giờ mình an toàn hơn." Vẫn F2 — nhưng strategic.*
>
> *Cùng 1 mechanism. Cùng 6 steps. Cùng chunk library.*
> *Nhưng Per-Agent Valence đảo hướng mọi thứ.*
>
> *Và context quyết định chunks NÀO được fire:*
> *Với mẹ → ngoan. Với bạn → thoải mái. Với kẻ thù → cảnh giác.*
> *Vô thức. Compiled. Near-automatic.*
>
> *SPM không phải empathy module. Không phải agent-reading module.*
> *Là GENERAL-PURPOSE self-template simulator.*
> *Empathy, Schadenfreude, negotiation, teaching, fiction engagement —*
> *tất cả = cùng 1 mechanism, khác valence × context × mode.*
>
> *Hiểu SPM = hiểu phần lớn cách con người tương tác.*
