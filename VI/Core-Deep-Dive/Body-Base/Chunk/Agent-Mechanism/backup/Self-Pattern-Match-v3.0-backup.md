---
title: Self-Pattern-Match — Solo Forward Simulation Mechanism
version: 3.0
created: 2026-04-15
rewritten: 2026-05-17 (v3.0 — Compiled/Fresh reframe, PFC=Lawyer, 3-cost, expert intuition)
previous_rewrite: 2026-04-24 (v2.0 — F1/F2 dual functions)
status: v3.0 — CORE MECHANISM FILE
supersedes:
  - backup/Self-Pattern-Match-v2.4-backup.md (v2.4, 2292L)
  - backup/Self-Pattern-Match-v1.0-forward-backup.md (v1.0, 1518L)
  - Body-Base/Feeling/backup/Self-Pattern-Match.md (old inward-labeling definition)
parent: Agent-Mechanism.md (integration hub)
sibling: By-Product-Gap-Resonance.md (emergent mutual phenomenon)
scope: |
  Deep drill của Self-Pattern-Match mechanism.
  v3.0 KEY CHANGE: F1/F2 reframe qua Compiled/Fresh axis:
    F1 — Compiled: body-level simulation (automatic, cost ≈ 0, Hebbian reinforced)
    F2 — Fresh: PFC draft prediction (deliberate, costly, mỗi lần = effort)
  "Feeling" và "Logic" = OBSERVER LABELS, không phải mechanism description.
  Inside body: chỉ có COMPILED ←→ FRESH spectrum.
  + Expert intuition = compiled, not bừa (shareable vs non-shareable compiled)
  + PFC = Lawyer not Judge → SPM accuracy caveat
  + 3 independent cost sources (PFC draft + Suppress + Uncertainty)
  + Per-domain SPM: cùng người, khác domain → khác compiled/fresh ratio
purpose: |
  File NỀN TẢNG cho toàn bộ framework:
  ① SPM là CƠ CHẾ CHÍNH mà não dùng để interact với agents
  ② 2 Functions (F1+F2) = Compiled/Fresh spectrum applied to agent prediction
  ③ Context-dependent selection giải thích TẠI SAO cùng 1 người
     ứng xử KHÁC NHAU với mẹ, bạn, kẻ thù
  ④ Per-Agent Valence quyết định F1/F2 fire HƯỚNG NÀO
position: |
  Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/ — supporting file cho Agent-Mechanism.md
  Sibling: By-Product-Gap-Resonance.md
  Downstream: Connection.md, Empathy.md, Status.md, toàn bộ observation files
dependencies:
  - Agent-Mechanism.md — integration hub, §5 preview
  - By-Product-Gap-Resonance.md v1.0 — emergent mutual phenomenon (2-Stream architecture)
  - Chunk.md v2.0 — chunk substrate
  - Feeling.md v2.0 — PFC observation interface
  - Logic-Feeling.md — 2 processing modes parallel
  - Valence-Propagation.md v2.0 — per-entity valence, Entity-Compiled, chain propagation
  - Body-Coupling.md v2.0 — coupling mechanism (builds ON SPM)
  - Body-Feedback-Mechanism.md v2.0 — 2-source model, chunk dynamics
  - Inter-Body-Mechanism.md v1.0 — Compiled/Fresh axis, 3-cost, by-product match, PFC=Lawyer
  - Empathy.md v2.2 — SPM function applied to other agents
  - Cortisol-Baseline.md v2.0 — stress cascade, moral injury
  - Connection.md v3.3 — 8 pathways, 3 generative primitives
  - Threat.md — NE cascade, PFC disconnect
sources_backup: |
  v2.4: Self-Pattern-Match.md (2292L, 2026-05-15) → backup/Self-Pattern-Match-v2.4-backup.md
  v1.0: Self-Pattern-Match.md (1518L, 2026-04-15) → backup/Self-Pattern-Match-v1.0-forward-backup.md
  v0: Self-Pattern-Match.md (inward-labeling) → Body-Base/Feeling/backup/Self-Pattern-Match.md
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Self-Pattern-Match — Solo Forward Simulation Mechanism

> Bạn thấy bạn thân khóc. Body bạn buồn nhẹ — DÙ bạn không bị gì.
> Đó là F1 (Compiled): body SIMULATE trạng thái người khác — automatic, gần vô thức.
>
> Rồi bạn nghĩ: "bạn buồn vì chia tay → chắc muốn ai đó lắng nghe."
> Đó là F2 (Fresh): PFC CHAIN draft predict hành vi tiếp theo — deliberate, tốn effort.
>
> 2 functions này chạy SONG SONG — gần như vô thức.
> Cùng 1 mechanism. Cùng 1 chunk library. Nhưng 2 OUTPUTS khác nhau:
> F1 cho body-level simulation. F2 cho behavioral prediction.
>
> "Feeling" và "Logic"? Chỉ là LABELS — observer gọi F1 là "cảm",
> gọi F2 là "nghĩ". Nhưng Einstein "cảm" toán = vì toán đã COMPILED.
> Therapist mới "nghĩ" cảm xúc = vì case mới còn FRESH.
> Trục thật: COMPILED ←→ FRESH. Content không quyết định.
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

---

## Mục lục

- §0 — Abstract + Definition
- §1 — Position (v2 → v3: what changed)
- §2 — 2 FUNCTIONS: F1 Compiled + F2 Fresh (★ REFRAMED)
- §3 — 6 STEPS (reframed qua Compiled/Fresh)
- §4 — CONTEXT-DEPENDENT CHUNK SELECTION
- §5 — 5 PATTERN-TYPE MODALITIES
- §6 — 4 QUALITY AXES
- §7 — DEVELOPMENTAL BOOTSTRAP
- §8 — CALIBRATION + FEEDBACK LOOP
  - §8.1 — "Biết" = compiled prediction — cùng cơ chế, khác trải nghiệm
- §9 — THRESHOLD FAILURE + FALLBACK
- §10 — REVERSED MAPPING + PROFESSIONAL SPM
- §11 — USE CASES (reframed qua Compiled/Fresh × Valence)
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

**v3.0 KEY REFRAME**: F1/F2 KHÔNG phải "Feeling/Logic" — là COMPILED/FRESH:
- **F1 — Compiled**: body-level simulation (automatic, cost ≈ 0, Hebbian reinforced)
- **F2 — Fresh**: PFC draft prediction (deliberate, costly, mỗi lần = effort)
- "Feeling" và "Logic" = OBSERVER LABELS, không phải cơ chế thật
- Inside body: chỉ có COMPILED ←→ FRESH spectrum (Inter-Body-Mechanism.md §3)
- Content (emotion hay reasoning) KHÔNG quyết định F1/F2
- COMPILATION LEVEL quyết định

### §0.2 — One-paragraph summary

Self-Pattern-Match là cơ chế mình dùng mình làm template để đoán người khác. Không phải mind-reading trực tiếp, không phải hardware mirror module — là simulation-based inference dùng self-chunks làm building blocks. SPM chạy 2 functions song song: F1 compiled body-level simulation (near-automatic, cost ≈ 0), F2 fresh PFC draft prediction (deliberate, costly). Observer gọi F1 là "cảm" và F2 là "nghĩ" — nhưng trục thật là COMPILED ←→ FRESH, không phải content. Einstein "cảm" toán vì toán đã compiled; therapist mới "nghĩ" cảm xúc vì case mới còn fresh. Per-Agent Valence quyết định F1 fire HƯỚNG NÀO (empathy hay reversed) và F2 chain MỤC ĐÍCH NÀO (giúp hay đối phó). Context quyết định chunks NÀO được retrieve (vô thức tùy chọn — với mẹ khác với bạn bè khác kẻ thù). Khi chunks THIẾU cho target, não fallback xuống schema/logic thay thế. PFC = Lawyer: SPM output qua PFC interpretation → stated reason có thể khác actual body-need.

### §0.3 — Central claims

```
⭐ 10 CLAIMS CỐT LÕI:

  1. SOLO + FORWARD: SPM chạy bên trong self, tạo prediction TRƯỚC verification
  2. CHUNK-SUBSTRATE: dùng cùng chunk library như mọi cognitive function khác
  3. ⭐ 2 FUNCTIONS: F1 Compiled (body simulate) + F2 Fresh (PFC draft)
     — chạy SONG SONG mặc định, CÓ THỂ tách riêng với rèn luyện
  4. ⭐ COMPILED/FRESH = REAL AXIS: "Feeling/Logic" = observer labels [v3.0]
     — content không quyết định F1/F2, compilation level quyết định
     — expert intuition = compiled, NOT bừa (Inter-Body-Mechanism.md §3.4)
  5. ⭐ CONTEXT-DEPENDENT: chunks được retrieve VÔ THỨC tùy agent + context
     — cùng 1 người ứng xử KHÁC với mẹ, bạn, kẻ thù, người lạ
  6. ⭐ VALENCE-GATED: Per-Agent Valence quyết định F1 fire hướng nào
     và F2 chain mục đích nào — empathy, strategic, hay dehumanize
  7. MULTI-MODAL: 5 Pattern-Type modalities
  8. QUALITY-VARIABLE: 4 axes quyết định output quality
  9. BIRD & COOK ARCHITECTURAL: self-awareness là prerequisite
  10. CALIBRATABLE: library refine qua feedback từ Resonance
```

### §0.4 — Relationship với files khác

```
  Agent-Mechanism.md §5 = preview (high-level)
  Self-Pattern-Match.md (FILE NÀY) = deep drill (mechanism chi tiết)
  By-Product-Gap-Resonance.md = sibling (emergent mutual phenomenon)

  SPM = MECHANISM (cái mình chạy bên trong)
  Resonance = PHENOMENON (cái emerge giữa 2+ entities khi mutual by-product match)
     Resonance v1.0: 2 streams — Stream 1 (hardware, không cần SPM) + Stream 2 (SPM mutual)
     SPM = Stream 2 ENGINE (tạo deepest Resonance) nhưng Resonance tồn tại cả khi không có SPM

  Inter-Body-Mechanism.md = SOURCE cho Compiled/Fresh axis (§3),
    3-cost model (§4), By-Product Match (§5.4), PFC=Lawyer (§7)

  Reading flow:
    Inter-Body-Mechanism.md → Chunk.md → Agent-Mechanism.md
    → Self-Pattern-Match.md → By-Product-Gap-Resonance.md
```

---

## §1 — Position: v2.4 → v3.0

### §1.1 — v2.4 đúng gì

v2.4 (2,292L): SPM với 2 Functions F1/F2, context-dependent selection, valence gate, reversed mapping, professional SPM, moral injury, strategic SPM, Bird & Cook decisive evidence.

v2.4 ĐÚNG ở toàn bộ mechanism. F1/F2 model, 6 steps, valence gate, reversed mapping, professional conflicts, developmental bootstrap, calibration — TẤT CẢ giữ nguyên.

### §1.2 — v3.0 thay đổi gì

```
⭐ 5 THAY ĐỔI v3.0:

  ① F1/F2 REFRAME → COMPILED/FRESH:
    v2.4: F1 = "Feeling Function", F2 = "Logic Function"
    v3.0: F1 = Compiled body-level simulation, F2 = Fresh PFC draft
    "Feeling" và "Logic" = observer labels → content không quyết định
    Consistent with Inter-Body-Mechanism.md §3 (Compiled/Fresh axis)

  ② EXPERT INTUITION = COMPILED, NOT BỪA [NEW]:
    "Logic" = compiled chunks SHAREABLE (deterministic domain)
    "Intuition" = compiled chunks NOT EASILY SHAREABLE (probabilistic domain)
    Khác shareability, KHÔNG khác quality of processing
    Inter-Body-Mechanism.md §3.4

  ③ PFC = LAWYER NOT JUDGE [NEW]:
    SPM output đi qua PFC interpretation
    PFC build narrative AFTER body-need — accuracy spectrum
    Stated reason cho SPM output có thể khác actual body-need
    Inter-Body-Mechanism.md §7

  ④ 3-COST MODEL REFERENCE [NEW]:
    Interaction cost = ① PFC draft + ② Suppress + ③ Uncertainty
    3 nguồn INDEPENDENT — tổng quyết định sustainability
    Enriches moral injury analysis, professional SPM analysis
    Inter-Body-Mechanism.md §4

  ⑤ PER-DOMAIN SPM [STRENGTHENED]:
    Cùng người, khác domain → khác compiled/fresh ratio
    Einstein: toán = F1 dominant (compiled), tâm lý = F2 dominant (fresh)
    "Logic vs Feeling" debate = artifact of different compilation levels
```

### §1.3 — Gì giữ từ v2.4

```
  GIỮ NGUYÊN (đã chất lượng):
    → 6-step mechanism (update labels)
    → 5 Pattern-Type modalities
    → 4 quality axes
    → Developmental bootstrap (mother contingency, rouge test)
    → Calibration + feedback loop
    → Bird & Cook 2013 (decisive architectural)
    → ToM literature mapping
    → Reversed mapping (Schadenfreude, sadism, dehumanization)
    → Professional SPM + moral injury (2-luồng)
    → Strategic SPM (poker face, fake cues, meta-SPM)
    → Training methods
    → AI era implications
    → Honest assessment framework
    → ALL 30+ research citations
```

---

## §2 — 2 FUNCTIONS: F1 Compiled + F2 Fresh (★ REFRAMED)

### §2.0 — Compiled/Fresh = Trục thật (★ v3.0 core reframe)

```
⭐ TRỤC THẬT CỦA SPM: COMPILATION LEVEL — KHÔNG PHẢI CONTENT

  FRAMEWORK v2.4 NÓI:
    F1 = "Feeling" (body-level, automatic)
    F2 = "Logic" (PFC chain, deliberate)

  v3.0 REFRAME:
    F1 = COMPILED processing (automatic, body-feedback direct, cost ≈ 0)
    F2 = FRESH PFC draft (deliberate, costly, not yet compiled)

  → "Feeling" và "Logic" = LABELS from OBSERVER perspective
  → Inside body: chỉ có COMPILED ←→ FRESH spectrum
  → Content (emotion/reasoning) KHÔNG quyết định F1/F2
  → COMPILATION LEVEL quyết định

  EVIDENCE (content ≠ processing level):

    ① Einstein + toán quen = COMPILED:
       Nội dung = toán ("logic"). Nhưng compiled → automatic → "cảm thấy"

    ② Người lạ thử đoán cảm xúc stranger = FRESH:
       Nội dung = emotion ("feeling"). Nhưng fresh → deliberate → "phải suy luận"

    ③ Chef nếm → biết ngay thiếu muối = COMPILED:
       Nội dung = phức tạp. Nhưng compiled → near-instant → "trực giác"

    ④ Therapist gặp case mới = FRESH:
       Nội dung = tâm lý ("feeling"). Nhưng fresh → PFC draft → "phải phân tích"

  → TRỤC:
    COMPILED ────────────────────────────── FRESH
    (automatic)                            (PFC draft)
    body-direct                            PFC-mediated
    cost ≈ 0                               cost > 0
    "cảm thấy"                            "nghĩ ra"
    tức thời                               cần thời gian
    Hebbian reinforced                     mỗi lần = effort

  TRANSITION (both directions):

    FRESH → COMPILED (Learning):
      Lặp lại + verify → Hebbian strengthen → automatic
      Einstein: toán FRESH (tuổi nhỏ) → COMPILED (adult)
      Bạn thân: F2 predict (mới quen) → F1 simulate (đã compiled)

    COMPILED → FRESH (Unlearning / Re-learning):
      Disrupted (error, trauma, context change) → phải FRESH lại
      Lost trust: COMPILED positive disrupted → FRESH re-evaluate
      Late diagnosis: COMPILED self-blame → FRESH re-compile (§18)

  🟡 F1/F2 = Compiled/Fresh reframe = framework synthesis.
     Consistent with Kahneman System 1/2, expertise research (Klein 1998).
  Source: Inter-Body-Mechanism.md §3
```

### §2.1 — F1: Compiled body-level simulation

```
⭐ F1 = COMPILED SIMULATION:

  DEFINITION:
    F1 là phần SPM mà body THẬT SỰ fire bản sao yếu trạng thái target.
    Body MÌNH respond — biochemistry THẬT, không phải tưởng tượng.
    "Compiled" = đã qua Hebbian reinforcement → near-automatic.

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
       → "Hợp tính" = Resonance Baseline cao (By-Product-Gap-Resonance.md §4)
       → GRADIENT liên tục, KHÔNG cố định
    ⑤ COST ≈ 0 PER FIRING (compiled) [v3.0]
       → Compiled = Hebbian reinforced → body fire tự động
       → Không cần PFC draft → không tiêu glucose cho processing
       → NHƯNG: biochemistry thật → MỖI firing = slight body cost (fatigue)
       → → Tích lũy nhiều episode = empathy fatigue (dù cost per episode ≈ 0 PFC)

  ⭐ F1 = "LUỒNG 1" TRONG CONNECTION CONTEXT (Connection.md §3.3):

    F1 body-feedback = Luồng 1 (momentary, per-episode):
      = Body response TẠI KHOẢNH KHẮC simulate target state
      = Có thể POSITIVE (bạn vui → vui lây) hoặc NEGATIVE (con ốm → khó chịu)
      = Cost THẬT: mỗi F1 firing = biochemistry thật → tích lũy = fatigue

    Luồng 1 tồn tại CÙNG LÚC với Luồng 2 (Entity-Compiled structural):
      = Luồng 2 = compiled per-agent valence → agent = body-base extension
      = SUSTAINED, KHÔNG phụ thuộc F1 output mỗi episode
      = Thuộc về entity valence (Valence-Propagation.md v2.0 §3), KHÔNG thuộc SPM

    2 luồng INDEPENDENT → có thể CONFLICT:
      → Mẹ chăm con ốm: F1/L1 negative + L2 positive → vẫn chăm
      → Bác sĩ + bệnh nhân: F1/L1 negative + L2 ≈ 0 → burnout (§10.4)
      → Bạn kể vui: F1/L1 positive + L2 positive → compound reward

    → F1 cost tích lũy + L2 bù không đủ = MORAL INJURY (§10.4)

  🟢 Singer 2004: shared activation areas khi observe others' emotions
  🟢 Empathy.md §4.2: empathy = biochemistry THẬT trong body MÌNH
  🟡 F1 as compiled simulation = framework synthesis, consistent với dual-process
  🟡 F1 = Luồng 1 framing: Connection.md §3.3
```

### §2.2 — F2: Fresh PFC draft prediction

```
⭐ F2 = FRESH PFC DRAFT:

  DEFINITION:
    F2 là phần SPM mà PFC chain draft trên F1 output (hoặc trực tiếp
    trên retrieved chunks) để predict hành vi target tiếp theo.
    "Fresh" = chưa compiled → PFC phải draft mỗi lần = costly.
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
    ⑤ COST > 0 MỖI LẦN (fresh) [v3.0]
       → Mỗi F2 chain = PFC draft = metabolic cost THẬT
       → Cost = f(chain_length × novelty_degree)
       → Inter-Body-Mechanism.md §4.2: PFC Draft Cost = Source ①
       → Compiled F2 chains (bạn thân patterns) → cost GIẢM
       → Novel F2 chains (stranger patterns) → cost CAO
       → → F2 cost + F1 cost = INDEPENDENT (2 nguồn khác nhau)

  ⭐ F2 CÓ THỂ TRANSITION THÀNH F1 (Fresh → Compiled):
    F2 chain lặp lại đủ nhiều → Hebbian → automatic → trở thành F1
    = "Logic trở thành feeling" cho person đó, ở domain đó
    VD: therapist mới: F2 dominant (analyze mỗi case) → experienced: F1 dominant
    VD: bạn mới: F2 predict → bạn thân: F1 "biết" (§8.1)

  🟢 Dual Process Theory (Kahneman 2011): System 1 ≈ F1, System 2 ≈ F2
  🟢 Logic-Feeling.md: 2 processing modes song song cho mọi entity
  🟡 F2 as fresh PFC draft within SPM = framework synthesis
```

### §2.3 — Song song mặc định, tách riêng khi rèn luyện

```
⭐ F1 + F2 CHẠY SONG SONG:

  DEFAULT MODE — hầu hết tương tác hàng ngày:

    Thấy bạn buồn
      → F1 (Compiled): body fire sadness nhẹ (milliseconds)
      → F2 (Fresh): "bạn buồn → cần an ủi → hỏi thăm" (seconds)
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
⭐ 3 MODES CỦA SPM — TỈ LỆ F1/F2 (Compiled/Fresh):

  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MODE A — COMPILED-DOMINANT (F1 >>> F2)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    F1 fire FULL, F2 bị giảm hoặc tạm ngưng.
    "Chỉ cảm nhận, không plan."

    Khi nào:
      → Therapeutic listening: therapist "chỉ ở đó" với client
      → Ngồi cạnh bạn đang khóc — không nói gì, chỉ feel cùng
      → Xem phim buồn — body fire, PFC không plan hành động
      → Nghe nhạc — body respond, không cần draft
      → Lần đầu gặp em bé — body fire nurturing, chưa plan

    Đặc điểm:
      → Body response MẠNH, conscious logic GIẢM
      → "Nói chuyện mà quên hết thời gian" = F1 dominant, F2 suspend
      → Empathy ở purest form — cảm mà không tính
      → Cost: F1 body cost tích lũy (empathy fatigue nếu kéo dài)
      → Benefit: connection DEEP nhất, trust build nhanh nhất

    🟢 Gendlin 1978: Focusing = intentional F1-dominant processing
    🟢 Rogers client-centered therapy = F1-dominant listening


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MODE B — FRESH-DOMINANT (F2 >>> F1)
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
         + ② Suppress cost: override F1 compiled response (Inter-Body §4.3)
         → = 2 independent cost sources cùng lúc
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
    │ Mode        │ F1 (Compiled) │ F2 (Fresh)    │ Best for         │
    ├─────────────┼───────────────┼───────────────┼──────────────────┤
    │ A: Compiled │ FULL          │ Dampened      │ Deep empathy,    │
    │    dominant │               │               │ therapy, music   │
    ├─────────────┼───────────────┼───────────────┼──────────────────┤
    │ B: Fresh    │ Dampened      │ FULL          │ Strategy, poker, │
    │    dominant │ (vẫn fire nhẹ)│               │ surgery, chess   │
    ├─────────────┼───────────────┼───────────────┼──────────────────┤
    │ C: Combined │ Active        │ Active        │ Daily social,    │
    │ (default)   │               │               │ teaching, work   │
    └─────────────┴───────────────┴───────────────┴──────────────────┘

    → Mode KHÔNG cố định — shift tự động hoặc deliberate
    → Rèn luyện = tăng khả năng CHỌN mode phù hợp context
    → "Social intelligence" = biết khi nào dùng mode nào

  ⭐ 3-COST ANNOTATION PER MODE [v3.0]:
    (Inter-Body-Mechanism.md §4: 3 nguồn cost INDEPENDENT)

    Mode A: ① PFC draft ≈ 0 + ② Suppress ≈ 0 + ③ Uncertainty varies
      → Total cost LOW (nhưng F1 body cost tích lũy nếu kéo dài)
    Mode B: ① PFC draft CAO + ② Suppress CAO + ③ Uncertainty varies
      → Total cost HIGHEST → burnout risk
    Mode C: ① PFC draft moderate + ② Suppress ≈ 0 + ③ varies
      → Total cost MODERATE → sustainable
```

### §2.5 — Per-Agent Valence × 2 Functions = Matrix quyết định

```
⭐ PER-AGENT VALENCE QUYẾT ĐỊNH F1/F2 FIRE HƯỚNG NÀO:

  (Valence-Propagation.md v2.0 §1-§3: valence = body's evaluation per entity)

  Per-Agent Valence = body đã compiled đánh giá: agent NÀY ảnh hưởng
  body channels CỦA TÔI thế nào? Positive ↔ Negative ↔ Mixed.
  DYNAMIC — thay đổi qua experience.

  Valence KHÔNG phải input cho SPM — valence GATE cho SPM.
  Valence quyết định: F1 fire theo hướng nào, F2 chain mục đích nào.


  ┌──────────────────┬────────────────────┬────────────────────┬─────────────────┐
  │ Per-Agent Valence │ F1 (Compiled)      │ F2 (Fresh)         │ SPM overall     │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ STRONG POSITIVE  │ Empathy FULL       │ Help/connect       │ Connection      │
  │ (bạn thân, mẹ)  │ Their joy=my joy   │ "Giúp gì được?"    │ drive           │
  │                  │ Their pain=my pain │ "Làm sao an ủi?"   │                 │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ MILD POSITIVE    │ Empathy nhẹ        │ Social navigate    │ Approach        │
  │ (người quen)     │ Warmth nhẹ        │ "Nên ứng xử sao?" │ moderate        │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ NEUTRAL          │ Surface scan       │ Objective assess   │ Cautious        │
  │ (người lạ)       │ Nhẹ hoặc zero     │ "Người này thế nào"│ observe         │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ MILD NEGATIVE    │ Discomfort nhẹ     │ Avoid/defend       │ Caution +       │
  │ (bạn hay trêu)   │ Body tension      │ "Tránh hay đối     │ avoidance       │
  │                  │ Empathy GIẢM      │  phó thế nào?"     │                 │
  ├──────────────────┼────────────────────┼────────────────────┼─────────────────┤
  │ STRONG NEGATIVE  │ ⭐ REVERSED        │ Strategic/hostile   │ Strategic       │
  │ (kẻ thù, lừa đảo)│ Their pain=MY    │ "Tấn công thế nào?"│ attack or       │
  │                  │ REWARD             │ "Phòng thủ sao?"   │ avoidance       │
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

    (Valence-Propagation.md v2.0 §3)

    Du lịch Việt Nam: neutral → positive (người thân thiện)
      → SPM shift: surface → approach → empathy nhẹ → giving reward
    Du lịch Brazil: neutral → NEGATIVE (bị cướp)
      → SPM shift: surface → threat predict → avoid → fear

    → Valence UPDATE liên tục qua interaction
    → SPM output THAY ĐỔI theo valence update
    → = Tại sao "ấn tượng đầu tiên" quan trọng
      (valence compile NHANH, ảnh hưởng SPM DÀI HẠN)

    🟢 Fear conditioning: one-trial learning (LeDoux 1996)
    🟢 Evaluative conditioning: valence transfer qua association (De Houwer 2007)


  ⭐ SPECIAL CASE — MIXED VALENCE (Body-Coupling.md v2.0 §2.4):

    Mẹ: L1++ (cho ăn, ôm) NHƯNG autonomy-- (ép học, cấm chơi)
      → F1: vừa warmth vừa tension (mixed body signal)
      → F2: vừa "nghe lời" vừa "tìm cách thoát"
      → = Mixed coupling = PHỔ BIẾN NHẤT
      → = Tại sao relationship phức tạp nhất = relationship có mixed valence

    Sếp: status++ (access career) NHƯNG threat++ (có thể đuổi)
      → F1: vừa respect vừa anxiety
      → F2: vừa "impress" vừa "tự bảo vệ"
      → = Tại sao "work relationship" mệt: mixed valence → F1/F2 conflict

    → Mixed valence = F1 fire CONFLICTING signals + F2 chain MULTIPLE plans
    → = 3-cost ALL apply: ① PFC hold multiple drafts + ② Suppress some signals
      + ③ Uncertainty high (which signal to trust)
    → = Tại sao "quan hệ phức tạp" = HIGHEST cost (Inter-Body §4.5)


  ⭐ VALENCE CÓ 2 VAI TRÒ — GATE + STRUCTURAL DRIVE:

    VAI TRÒ 1 — GATE cho SPM:
      Valence quyết định F1 fire HƯỚNG NÀO, F2 chain MỤC ĐÍCH NÀO.
      = Ảnh hưởng TỪNG EPISODE SPM fire.

    VAI TRÒ 2 — TẠO BODY-BASE EXTENSION khi strong positive:
      Khi valence STRONG POSITIVE + compiled SÂU (nhiều interaction):
        → Agent TRỞ THÀNH phần mở rộng body-base
        → Agent's wellbeing = MY wellbeing (structural)
        → = "Luồng 2" reward (Entity-Compiled) — SUSTAINED
        → = Valence-Propagation.md v2.0 §3: Entity-Compiled 3 subtypes

    Vai trò 1 = ảnh hưởng SPM (Luồng 1 direction)
    Vai trò 2 = tạo structural drive NGOÀI SPM (Luồng 2)
    → 2 vai trò CÙNG TỒN TẠI, từ CÙNG 1 valence compiled

    🟡 2 vai trò valence = framework synthesis
    Chi tiết: Connection.md §3.3, Valence-Propagation.md v2.0 §3
```

### §2.6 — Expert Intuition = Compiled, Not Bừa (★ v3.0 NEW)

```
⭐ "LOGIC" vs "INTUITION" = NAMING ARTIFACT, NOT MECHANISM DIFFERENCE

  (Inter-Body-Mechanism.md §3.4)

  TOÁN HỌC:
    Compiled chunks: 2+2=4 (SHARED, mọi người giống nhau)
    Reproduce: chuyên gia A và B cùng kết quả (verifiable)
    Global label: "LOGIC" (vì shared + reproducible)

  TÂM LÝ HỌC:
    Compiled chunks: patterns from 1,000+ cases (RIÊNG mỗi chuyên gia)
    Reproduce: chuyên gia A và B CÓ THỂ khác kết luận (different cases)
    Global label: "INTUITION / CẢM NHẬN" (vì not perfectly reproducible)

  BÊN TRONG: CƠ CHẾ GIỐNG HỆT
    Toán gia: years compile → chunks fire fast → "thấy" lời giải
    Therapist: years compile → chunks fire fast → "thấy" pattern
    CẢ HAI = compiled automatic processing = F1 in their domain.

  KHÁC BIỆT:
    Toán: subject = DETERMINISTIC → compiled chunks CONVERGE
    Tâm lý: subject = PROBABILISTIC + INDIVIDUAL → compiled chunks DIVERGE
    → KHÔNG phải chuyên gia tâm lý "bừa"
    → Domain không deterministic → compiled patterns RIÊNG là LEGITIMATE
    → Domain reality = patient outcomes = final arbiter (as always)

  FRAMEWORK REFRAME:
    "Logic"     = compiled chunks SHAREABLE (deterministic domain)
    "Intuition" = compiled chunks NOT EASILY SHAREABLE (probabilistic domain)
    KHÁC: shareability. KHÔNG KHÁC: quality of processing.

  SPM IMPLICATION:
    SPM trên người (probabilistic target) → compiled = "intuition" label
    SPM trên bài toán (deterministic) → compiled = "logic" label
    CÙNG F1 compiled processing → KHÁC domain → KHÁC social label
    → "Người đó rất logic" = "compiled chunks CỦA HỌ shareable"
    → "Người đó rất nhạy cảm" = "compiled chunks CỦA HỌ not easily shareable"
    → CẢ HAI = compiled quality → đều = expert in their domain

  🟢 Expert intuition = compiled patterns (Kahneman 2011, Klein 1998)
  🟡 "Shareable vs non-shareable" as organizing principle = framework synthesis
  Source: Inter-Body-Mechanism.md §3.4
```

### §2.7 — Per-Domain SPM: cùng người, khác domain → khác ratio (★ v3.0 STRENGTHENED)

```
⭐ CÙNG 1 NGƯỜI → KHÁC DOMAIN → KHÁC F1/F2 (COMPILED/FRESH) RATIO:

  SPM quality KHÔNG CỐ ĐỊNH per person — phụ thuộc DOMAIN:

  EINSTEIN:
    Toán/Vật lý: F1 dominant (compiled SÂU) → "cảm thấy" lời giải
    Tâm lý con người: F2 dominant (thin chunks) → phải "suy luận"
    Chính trị: F2 dominant (ít experience) → deliberate reasoning
    → Einstein "feeling person" ở physics, "thinking person" ở politics

  THERAPIST GIỎI:
    Tâm lý: F1 dominant (1,000+ cases compiled) → "thấy" pattern ngay
    Toán: F2 dominant (thin chunks) → phải "nghĩ"
    → Therapist "feeling person" ở psych, "thinking person" ở math

  CÙNG DOMAIN, KHÁC PERSON:
    Cả Einstein và therapist đều "feeling" ở domain MÌNH (compiled)
    Cả Einstein và therapist đều "thinking" ở domain KHÁC (fresh)
    → "Feeling person" vs "Thinking person" = CỐ ĐỊNH? KHÔNG.
    → = f(compilation level ở domain ĐANG HOẠT ĐỘNG)

  HỆ QUẢ:
    → "Logic vs Feeling" personality debate = partially artifact:
       People who compiled DIFFERENT domains → different default mode VISIBLE
    → Introvert: compiled social chunks ÍT → F2 dominant ở social → "logical person"
    → Extrovert: compiled social chunks NHIỀU → F1 dominant ở social → "feeling person"
    → NHƯNG: introvert CÓ THỂ F1 dominant ở domain riêng (coding, music, art)
    → = Per-domain, KHÔNG per-person (trừ structural hardware bias — Logic-Feeling.md §6)

  🟡 Per-domain SPM ratio = framework synthesis, consistent with expertise research
  🟡 "Logic/Feeling personality = partially artifact" = testable claim
```

---

## §3 — 6 STEPS (reframed qua Compiled/Fresh)

### §3.1 — Overview

```
⭐ 6 STEPS — CÙNG CƠ CHẾ NHƯ v2.4, UPDATE LABELS v3.0:

  Mỗi step: vai trò cho F1 (Compiled) + vai trò cho F2 (Fresh)
  Steps 1-3 = CHUẨN BỊ (chung cho cả 2 functions)
  Step 4 = F1 CORE (body simulate — compiled)
  Step 5 = BRIDGE (PFC observe → feed cả F1 lẫn F2)
  Step 6 = F2 CORE (attribute + chain draft — fresh)

  ┌──────────────────────────────────────────────────────────────┐
  │ Target detected                                              │
  │      ↓                                                       │
  │ [1] RETRIEVE — select chunks từ self repertoire              │
  │      ↓                                                       │
  │ [2] TEMPLATE MATCH — position chunks as self-as-target       │
  │      ↓                                                       │
  │ [3] PROJECTION — apply template onto target                  │
  │      ↓                                                       │
  │ [4] SIMULATION — fire template ← ⭐ F1 CORE (compiled fire) │
  │      ↓                                                       │
  │ [5] OUTPUT READ — PFC observe ← BRIDGE (F1 → F2 handoff)   │
  │      ↓                                                       │
  │ [6] ATTRIBUTION — assign + chain ← ⭐ F2 CORE (fresh draft) │
  └──────────────────────────────────────────────────────────────┘

  Steps có thể chạy parallel, semi-conscious, hoặc compressed.
  6 steps là analytical scaffolding, không claim serial execution.
```

### §3.2 — Step 1: Retrieve

```
🟡 RETRIEVE: Brain select chunks từ self repertoire có thể relevant cho target.

  F1 role: retrieve chunks CẢM (emotion, sensation) → sẽ dùng simulate
  F2 role: retrieve chunks LOGIC (rules, patterns, history) → sẽ dùng chain draft

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
      → Mixed valence → retrieve CONFLICTING chunks (costly — 3-cost ALL apply)
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

### §3.5 — Step 4: Simulation — F1 CORE (Compiled)

```
⭐ SIMULATION: Template FIRE — body THẬT SỰ respond.

  ĐÂY LÀ F1 CORE — nơi compiled body-level simulation xảy ra.

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

    → Chi tiết L2 × SPM: Body-Coupling.md v2.0 §1.4
    🟡 Self-template ≠ empathy distinction = Drill-L2 insight
```

### §3.6 — Step 5: Output read — BRIDGE

```
⭐ OUTPUT READ: PFC observe simulation output.

  ĐÂY LÀ BRIDGE — nơi F1 (compiled) output chuyển thành F2 (fresh) input.

  F1 → PFC: "body tôi đang respond thế này" (feeling observation)
    → Rich self-chunks → precise: "ambivalent gratitude tinged with guilt"
    → Thin self-chunks (alexithymia) → diffuse: "just feels bad"
    → No labels → unreadable: "something, but can't name it"

  PFC → F2: "based on body response + logic → target đang feel X"
    → F1 output becomes INPUT cho F2 chain ở Step 6
    → = HANDOFF point: compiled simulation → fresh draft can use

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

### §3.7 — Step 6: Attribution — F2 CORE (Fresh) + PFC=Lawyer

```
⭐ ATTRIBUTION + CHAIN: PFC assign output TO target + chain draft.

  ĐÂY LÀ F2 CORE — nơi fresh PFC draft prediction xảy ra.

  F2 (chính):
    ATTRIBUTION: "target feels/wants/will X" (assign prediction to target)
      ↓
    CHAIN DRAFT: "target feels X → target thường do Y"
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

  ⭐ PFC = LAWYER NOT JUDGE [v3.0]:
    (Inter-Body-Mechanism.md §7)

    PFC KHÔNG phải judge trung lập — PFC = LAWYER cho body-need.
    PFC build narrative AFTER body-need đã fire.
    SPM output đi qua PFC → PFC có thể:
      → RATIONALIZE: "tôi giúp vì tốt bụng" (thật: L2 structural drive)
      → CONFABULATE: "tôi ghét vì lý do X" (thật: compiled valence negative)
      → JUSTIFY: "tôi không empathize vì đúng" (thật: F1 suppress schema)

    → Stated reason cho SPM output ≠ actual body-need driving output
    → Accuracy spectrum: awareness ++ → PFC honest hơn
    → Klein 1998: expert narrative AFTER decision, NOT before
    → Gazzaniga (split-brain): PFC confabulate reasons for body-driven actions

    ⚠️ IMPLICATION cho Resonance:
      CẢ HAI PFCs trong interaction đều "lawyering"
      → Person A's PFC rationalize A's SPM output
      → Person B's PFC rationalize B's SPM output
      → Deep friendship = calibrate qua body-feedback, KHÔNG qua stated reasons
      → = Tại sao "hành động nói nhiều hơn lời nói"

    🟢 Gazzaniga (split-brain): PFC interpreter module
    🟢 Haidt 2001: moral reasoning = post-hoc justification
    🟡 PFC=Lawyer as SPM caveat = framework synthesis
    Source: Inter-Body-Mechanism.md §7

  🟡 Framework note: Step 6 = where SPM becomes ACTIONABLE
     Steps 1-5 = internal processing. Step 6 = decision bridge.
```

### §3.8 — Time scale + consciousness

```
🟡 SPEED varies by Pattern-Type + depth + mode:

  ┌──────────────┬──────────┬──────────────┬──────────────────────┐
  │ Pattern-Type │ F1 speed │ F2 speed     │ Consciousness        │
  │              │(Compiled)│ (Fresh)      │                      │
  ├──────────────┼──────────┼──────────────┼──────────────────────┤
  │ Affective    │ ms       │ seconds      │ Mostly unconscious   │
  │ Somatic      │ seconds  │ seconds      │ Body-coupled         │
  │ Visual-symb. │ seconds  │ seconds      │ Semi-conscious       │
  │ Verbal-cog.  │ sec-min  │ sec-min      │ Mostly conscious     │
  │ Composite    │ blend    │ blend        │ Mixed                │
  └──────────────┴──────────┴──────────────┴──────────────────────┘

  F1 LUÔN nhanh hơn F2 (compiled before fresh draft)
  → = Tại sao "cảm trước, hiểu sau" (feel before think)
  → = Tại sao gut feeling đến TRƯỚC logic explanation
  → v3.0 reframe: "compiled fires before fresh drafts" = same observation, deeper lens

  UNCONSCIOUS SPM: automatic empathy, "gut feel," instant rapport
    → Hầu hết everyday agent-reading → F1 compiled dominant
  CONSCIOUS SPM: deliberate perspective-taking, negotiation analysis
    → Requires cognitive effort (PFC resource) → F2 fresh dominant
  SEMI-CONSCIOUS: rapid social reading with partial awareness
    → Most interpersonal moments → F1+F2 combined

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
    F1 (Compiled): fire respect + warmth (compiled từ years)
    F2 (Fresh): chain "mẹ cần gì → giúp" (helping orientation)

  VỚI NHÓM BẠN THÂN:
    Context: thoải mái, ngang hàng, sở thích chung
    Chunks retrieved:
      → "Thoải mái, tự do" (behavioral pattern)
      → "Sở thích chung, chuyện vui" (content)
      → "Xưng hô: mày-tao" (linguistic chunks)
      → "Nói bỗ bã vô tư, joke, troll" (no filter)
    F1 (Compiled): fire casual warmth + fun (compiled)
    F2 (Fresh): chain "chơi gì tiếp → đề xuất → adjust" (peer negotiation)

  VỚI SẾP:
    Context: hierarchy nhưng khác mẹ — professional, status scan
    Chunks retrieved:
      → "Chuyên nghiệp, cẩn thận" (behavioral pattern)
      → "Report, deadline, achievement" (content)
      → "Xưng hô: em-anh/chị hoặc formal" (linguistic)
      → "Filter: không joke quá, không intimate quá" (social boundary)
    F1 (Compiled): fire mix respect + caution (status uncertainty)
    F2 (Fresh): chain "sếp cần gì → deliver → status maintain" (professional)

  VỚI KẺ THÙ:
    Context: threat, hostile, strategic
    Chunks retrieved:
      → "Cảnh giác, phòng thủ" (behavioral pattern)
      → "Điểm yếu, pattern hành vi đối thủ" (content)
      → "Xưng hô: lạnh, hoặc không xưng" (linguistic)
      → "Filter: không chia sẻ information" (protect)
    F1 (Compiled): fire tension + alertness (threat detection)
    F2 (Fresh): chain "kẻ thù sẽ làm gì → phòng thủ/tấn công" (strategic)

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

    ⭐ PFC=Lawyer ở đây [v3.0]:
      PFC rationalize: "phụ nữ KHÓ HIỂU" (blame target)
      Thực tế: "SPM library CỦA TÔI thiếu" (library gap)
      = PFC lawyering cho body's frustration → blame external
      → Inter-Body-Mechanism.md §7

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
    F1 (Compiled): "Khi tôi đang suy nghĩ công thức → tôi muốn yên tĩnh,
         muốn có người trao đổi chunk" → simulate Grossmann CŨNG vậy
    F2 (Fresh): "Grossmann biết tensor calculus → tôi cần cái đó → hỏi"
    → SPM accurate VÌ chunk overlap ở domain ĐỦ

  Grossmann's SPM on Einstein:
    Chunks retrieved: vật lý lý thuyết, creative thinking patterns
    F1 (Compiled): "Khi tôi đang giải bài toán khó → feel challenge + excitement"
         → simulate Einstein CŨNG feel challenge khi thiếu math tool
    F2 (Fresh): "Einstein cần math tool mà ông ấy thiếu → tôi có → share"
    → SPM accurate VÌ chunk overlap + complementary

  Resonance EMERGE (Stream 2 — By-Product-Gap-Resonance v1.0 §2.2):
    → CẢ HAI fire SPM toward nhau THÀNH CÔNG → Stream 2 bidirectional sync
    → F1 cả 2 phía: feel HIỂU nhau (shared feeling of intellectual work)
    → F2 cả 2 phía: plan COMPLEMENT nhau (physics + math)
    → Stream 2 emerge → trao đổi KÉO DÀI → collaboration SÂU
    → = Tại sao "đồng môn" feel close dù ít biết nhau PERSONALLY
    NOTE: Resonance cũng tồn tại qua Stream 1 (hardware match) nhưng SPM tạo Stream 2 = deepest

  ⭐ QUY LUẬT: SPM không cần TOTAL overlap — cần DOMAIN-SPECIFIC overlap:
    → 5% overlap ở domain CRITICAL → SPM tốt ở domain đó
    → 95% overlap ở domain IRRELEVANT → SPM vẫn FAIL cho task hiện tại
    → = Giải thích tại sao:
      Bạn cùng nghề HIỂU nhau (domain overlap) dù personality KHÁC
      Bạn cùng tính nhưng KHÁC nghề → hiểu personal, MISS professional
      Vợ chồng nhiều năm → overlap RỘNG (personal + daily + emotional)
        → SPM accuracy CỰC CAO → "hiểu không cần nói"

  ⭐ CORE EQUATION (By-Product-Gap-Resonance.md §4 Divergence):
    SPM accuracy = f(chunk library overlap with target)
    → overlap CAO → F1 compiled mạnh + F2 draft chính xác → quality CAO

  🟡 "Domain-specific overlap drives SPM quality" = framework synthesis
  🟢 Consistent: interpersonal synchrony research (Feldman 2007)
```

---

## §5 — 5 PATTERN-TYPE MODALITIES

```
⭐ SPM FIRE QUA 5 LOẠI CHUNKS KHÁC NHAU:

  Mỗi Pattern-Type = 1 kênh simulation riêng.
  F1 (Compiled) và F2 (Fresh) đều chạy qua TẤT CẢ 5 types — nhưng TỈ LỆ khác.

  ┌────────────────┬──────────────┬──────────────┬──────────────────────┐
  │ Pattern-Type   │ F1 (Compiled)│ F2 (Fresh)   │ Connection type      │
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
    → Cross-species: chó cúp đuôi → affective SPM fire (Resonance Stream 1 emerge, Stream 2 limited)
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
    → Slowest single-type, but most EXPLICIT (PFC-heavy → F2 dominant)

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
  │ #  │ Axis            │ Ảnh hưởng F1 (Compiled) + F2 (Fresh)      │
  ├────┼─────────────────┼────────────────────────────────────────────┤
  │ ①  │ PATTERN-TYPE    │ Fire đúng loại chunks cho target cues?    │
  │    │ MATCH           │ F1: simulate đúng kênh cảm xúc?          │
  │    │                 │ F2: predict đúng loại behavior?            │
  │    │                 │ Mismatch → prediction-delta compound      │
  ├────┼─────────────────┼────────────────────────────────────────────┤
  │ ②  │ DEPTH           │ Quantity + specificity chunks về target?  │
  │    │                 │ Thin (stranger): 5-10 chunks → coarse     │
  │    │                 │ Deep (family): hundreds → high-fidelity    │
  │    │                 │ F1: deep = compiled simulation CHÍNH XÁC   │
  │    │                 │ F2: deep = fresh draft CHÍNH XÁC           │
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

    ⭐ Resonance Baseline × parent-child (Body-Coupling.md v2.0 §7):
      Baseline HIGH → contingent response → healthy SPM
      Baseline LOW → both frustrated → SPM chunk confusion compound

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
      → "Bạn buồn" (F1 compiled) → "bạn sẽ không muốn chơi" (F2 fresh)
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

    v3.0 note — FRESH → COMPILED lifecycle:
      → New domain: F2 dominant (fresh, effortful)
      → Practice: F2 chains → Hebbian → begin compiling
      → Expert: F1 dominant (compiled, automatic, "intuition")
      → = §2.6 expert intuition lifecycle
```

---

## §8 — CALIBRATION + FEEDBACK LOOP

```
⭐ SPM LIBRARY KHÔNG TĨNH — REFINE QUA FEEDBACK:

  ┌─────────────────────────────────────────────────────────────────┐
  │  SPM fires prediction (F1 compiled + F2 fresh)                  │
  │       ↓                                                         │
  │  Interaction proceeds                                           │
  │       ↓                                                         │
  │  Outcome observed (target's actual behavior, response)          │
  │       ↓                                                         │
  │  Resonance inferred retrospectively                     │
  │       ↓                                                         │
  │  Library UPDATE:                                                │
  │    - Confirmed chunks → STRENGTHENED (Hebbian → more compiled)  │
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
    → Repeated → affective SPM cho bạn NÀY → compiled → accurate

  F2-SPECIFIC CALIBRATION:
    → "Tôi predict bạn sẽ rời đi → thực tế bạn ở lại → F2 draft UPDATE"
    → "Behavior mismatch → behavioral model về bạn REFINED"
    → Repeated → behavioral prediction → compiled → accurate

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
  │              │ = F2 DOMINANT (fresh)   │                           │
  ├──────────────┼─────────────────────────┼───────────────────────────┤
  │ Compiled nhẹ │ "Cảm giác" — nhanh,    │ Thấy output, mờ process  │
  │ (người quen) │ semi-automatic          │ → "hình như hiểu"        │
  │              │ = F1+F2 COMBINED        │                           │
  ├──────────────┼─────────────────────────┼───────────────────────────┤
  │ Compiled sâu │ "Biết" — instant,       │ CHỈ thấy output          │
  │ (bạn thân /  │ tự động, confident      │ Không thấy process       │
  │  gia đình)   │ = F1 DOMINANT (compiled)│ → gọi "tự nhiên"        │
  └──────────────┴─────────────────────────┴───────────────────────────┘

  BÊN TRONG: cùng 6 steps (Retrieve → Template → Project → Simulate → Read → Attribute).
  Khác: tốc độ + chunks đã compiled sâu + accuracy đã calibrate qua Resonance feedback.


  TẠI SAO PFC GỌI "TỰ NHIÊN":

    SPM compiled → chạy VÔ THỨC (§3.8) → PFC không thấy 6 steps
    → PFC chỉ thấy OUTPUT: "tôi hiểu người này" / "tôi hợp người này"
    → PFC KHÔNG thấy: hàng ngàn lần tương tác → calibrate → compile
    → PFC confabulate: "hợp tính", "duyên", "tự nhiên hiểu nhau"

    Đúng là "tự nhiên" — nhưng "tự nhiên" = compiled prediction chạy tự động.
    KHÔNG phải magic — là mechanism hoạt động đúng thiết kế.

    ⭐ PFC = LAWYER ở đây [v3.0]:
      PFC narrative: "tôi và bạn HIỂU NHAU tự nhiên" (confabulate)
      Mechanism: 1,000+ interactions → compile → F1 compiled → instant
      PFC KHÔNG THẤY mechanism → rationalize = "duyên", "hợp tính"
      → Inter-Body-Mechanism.md §7


  VÍ DỤ — "TỰ NHIÊN" MÀ THỰC RA LÀ COMPILED:

    ① "Tự nhiên chơi thân":
       Resonance Baseline cao (By-Product-Gap-Resonance.md §4 "hợp tính") → SPM match dễ từ đầu
       → F1 reward → approach → lặp lại → compile
       PFC: "không biết tại sao, hợp nhau thôi"

    ② "Hiểu nhau không cần nói":
       SPM calibrate qua hàng ngàn interactions (§8)
       → Chunks sâu + chính xác → F1 instant + F2 predict đúng
       Thật ra: NÓI RẤT NHIỀU rồi → compile → bây giờ không cần nói

    ③ "Tự nhiên thấy thú vị → chơi → tình yêu":
       SPM baseline tốt → approach → tương tác → calibrate → compile
       → Valence strong positive → L2 build (Entity-Compiled)
       PFC: "yêu tự nhiên" — "tự nhiên" = prediction compiled thành structural

    ④ "Mẹ biết con cần gì":
       20 năm SPM → chunks CỰC DEEP → F1 + F2 instant
       "Biết" = compiled prediction. SAI khi: con thay đổi mà chunks chưa update
       → §8 Loop Failure ①: no feedback → library không calibrate → prediction CŨ


  HỆ QUẢ:

    → "Biết" người khác KHÔNG CÓ đường tắt
       Chỉ có: predict → interact → feedback → calibrate → compile → "biết"
    → "Hợp tính" = compile NHANH (Resonance Baseline cao). Khác tốc độ, cùng cơ chế
    → Trust = compiled prediction đã proven reliable qua thời gian
    → Intuition về người = same mechanism với expert intuition (Klein 1998)
    → v3.0: "biết" = compiled. "Đoán" = fresh. CƠ CHẾ GIỐNG — khác compilation level.

  🟢 Expert intuition = compiled pattern matching: Klein 1998, Chase & Simon 1973
  🟡 "Compiled SPM = biết" explicit framing = framework synthesis
  → By-Product-Gap-Resonance.md §4: "hợp tính" = Resonance Baseline
  → Compile-Taxonomy.md §2.2: "bác sĩ nhìn biết ngay" = same mechanism
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
    → NHƯNG valence gate ĐẢO HƯỚNG output interpretation
    → Cùng compiled simulation, KHÁC interpretation
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

    Required: F2 (fresh draft) FULL — plan surgery steps precisely
    F1 cost: biết bệnh nhân đau → F1 fire empathy nhẹ → body discomfort
    Training: dampen F1 through professional detachment
    Risk: F1 cost tích lũy → burnout, compassion fatigue
    Recovery: supervision, peer support, rest


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CASE B — THERAPIST
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Required: F1 (compiled) HIGH — empathize deeply with client
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

    → = F1 (compiled) KHÔNG THỂ suppress VĨNH VIỄN
    → = Schema suppress chỉ TẠM THỜI
    → = Khi schema weakens → F1 fire on compiled memories → PTSD
```

### §10.4 — Moral injury = F1 cost tích lũy + 3-cost model

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

  ⭐ 3-COST ANALYSIS [v3.0]:
    (Inter-Body-Mechanism.md §4: 3 nguồn cost INDEPENDENT)

    Moral injury = ALL 3 cost sources firing SIMULTANEOUSLY:
      ① PFC Draft: PFC process complex moral reasoning (high chain)
      ② Suppress: suppress F1 empathy response during action (chronic)
      ③ Uncertainty: "tôi đang đúng hay sai?" (unresolvable)
    → Total cost = ①+②+③ = CỰC CAO
    → Duration: chronic (daily/weekly) → UNSUSTAINABLE
    → = Tại sao moral injury = one of HIGHEST cost states

  ⭐ 2-LUỒNG GIẢI THÍCH TẠI SAO CÙNG F1 COST → KHÁC OUTCOME:

    Moral injury / burnout KHÔNG CHỈ phụ thuộc F1 cost (Luồng 1).
    Còn phụ thuộc Luồng 2 (Entity-Compiled structural) CÓ BÙ hay KHÔNG:

    BÁC SĨ chăm bệnh nhân lạ:
      L1: F1 fire empathy dissonance LIÊN TỤC (negative)
      L2: ≈ 0 (bệnh nhân lạ → chưa compiled thành body-base extension)
      → F1 cost TÍCH LŨY, KHÔNG ĐƯỢC BÙ → burnout, moral injury

    MẸ chăm con ốm (CÙNG F1 cost):
      L1: F1 fire empathy dissonance LIÊN TỤC (negative)
      L2: STRONG positive (con = body-base extension, Entity-Compiled positive)
      → F1 cost ĐƯỢC BÙ bởi L2 structural reward → KHÔNG burnout
      → Chăm con = feed body-base MÌNH (dù F1 output negative)

    → CÙNG mechanism (F1), CÙNG cost level → KHÁC outcome
    → Biến số quyết định: Luồng 2 có đủ bù Luồng 1 hay không
    → = Tại sao "người tận tụy với nghề" cần professional anchor
      (anchor schema = proxy L2 bù F1 cost — Connection.md §3.3)

    Chi tiết 2-luồng: Connection.md §3.3, Valence-Propagation.md v2.0 §3

  🟢 Litz 2009: moral injury — distinct from PTSD
  🟢 Perpetrator trauma research: established across contexts
  🟢 Milgram 1963: participants showed extreme distress
  🟢 Figley 2002: compassion fatigue in helping professionals
  🟡 F1 cost tích lũy as mechanism = framework synthesis
  🟡 L1/L2 compensation model = framework synthesis (Connection.md §3.3)
  🟡 3-cost applied to moral injury = framework synthesis [v3.0]
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
      → Đối thủ F1: compiled simulation COARSE (thiếu input)
      → Đối thủ F2: prediction KÉM → plan sai → bất lợi

    Ví dụ:
      → Poker player: suppress micro-expressions → đối thủ đọc sai
      → Tướng quân: bình tĩnh trước binh lính dù tình thế nguy hiểm
        → 2 mục đích: ① chặn SPM đối thủ ② ổn định F1 quân lính
           (lính SPM on tướng: "tướng bình tĩnh → an toàn" → cortisol giảm)

    ⚠️ NHƯNG: Micro-expressions VẪN LỌT:
      → F1 fire = body-level event → micro-expressions (~40ms) TỰ ĐỘNG lọt
      → Training giảm nhưng KHÔNG TẮT 100%
      → Expert reader CÓ THỂ detect micro-expression
      → 🟢 Ekman 2003: micro-expressions leak even when suppressed
      → 🟢 Ekman & Friesen 1969: FACS — Facial Action Coding System


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  CHIẾN LƯỢC ② — FAKE CUES: Cho đối thủ dùng SAI SPM
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Cơ chế:
      → Cố tình lộ trạng thái GIẢ (giả sợ, giả yếu, giả bình thản)
      → Đối thủ F1: simulate trạng thái GIẢ → body respond → prediction SAI
      → Đối thủ F2: chain logic trên prediction SAI → plan SAI → bất lợi

    Ví dụ lịch sử:
      → "Thành không kế" (Tam Quốc): Gia Cát Lượng ngồi gảy đàn bình thản
        → Tư Mã Ý F1: "bình thản = có kế" → F2: "có phục binh → rút"
        → Thực tế: KHÔNG có quân → SPM accuracy BỊ HACK qua fake cue

    TẠI SAO FAKE CUES HIỆU QUẢ:
      → F1 fire trên CUES, không phải BELIEFS
      → Dù đối thủ NGHI giả → F1 VẪN fire trên cues observable
      → PFC phải hold 2 drafts → tốn resource → uncertainty TĂNG
      → = Fake cues HIỆU QUẢ ngay cả khi đối thủ biết CÓ THỂ giả
        → 3-cost ③ Uncertainty TĂNG cho đối thủ [v3.0]

    🟢 DePaulo et al. 2003: deception detection accuracy ≈ 54% (near chance)
    🟢 Sun Tzu: "All warfare is based on deception" (~500 BCE)


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

    Ví dụ:
      → Poker: "Anh ấy nghĩ tôi đang bluff (Level 2) → vậy tôi sẽ
        thật sự có bài tốt lần này (control Level 2 → win)"
      → Binh pháp: "Địch nghĩ ta yếu → ta giả yếu thêm → phục kích"

    ĐÒI HỎI:
      → SPM quality CỰC CAO ở cả F1 lẫn F2
      → MODE SWITCHING nhanh: Mode B (suppress own) ↔ Mode C (read other)
      → Compiled chunks cho ĐỐI THỦ CỤ THỂ sâu
        → "Biết địch biết ta, trăm trận trăm thắng" (Tôn Tử)
      → PFC resource CỰC LỚN (hold multiple levels)
        → = Tại sao strategic thinking = EXHAUSTING
        → = Tại sao "người già dặn" (compiled meta-SPM) → less exhausting

    🟢 Recursive Theory of Mind research: humans can reason about
       others' beliefs about beliefs (Level 2-3 common, Level 4+ rare)
    🟢 Diplomatic protocol: formal behavior REDUCES readable cues


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

    → TẤT CẢ 3 dùng CÙNG mechanism (SPM F1/F2) — chỉ HƯỚNG khác
    → "Chiến lược gia giỏi" = SPM quality CAO + compiled meta-SPM
    → "Người già dặn khó đọc" = compiled suppress + compiled meta-SPM
    → "Trẻ con dễ đọc" = chưa compiled suppress → cues lộ rõ
```

---

## §11 — USE CASES (reframed qua Compiled/Fresh × Valence)

```
⭐ SPM LÀ GENERAL-PURPOSE — KHÔNG CHỈ AGENT-READING:

  Cùng mechanism (6 steps + F1 Compiled + F2 Fresh) — khác context → khác ứng dụng.

  ┌────┬────────────────────┬────────────────┬────────────────┬──────────────┐
  │ #  │ Use case           │ F1 (Compiled)  │ F2 (Fresh)     │ Key insight  │
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

  → TẤT CẢ 10 use cases dùng CÙNG 6 steps + F1 (Compiled) + F2 (Fresh)
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

  IMPLICATION CHO 2 FUNCTIONS (Compiled/Fresh):

    Alexithymia → poor self-chunks
      ↓
    Step 1 Retrieve: thin chunks available
      ↓
    Step 4 F1 (Compiled): simulation POOR (thin template → coarse output)
      ↓
    Step 5 Bridge: PFC cannot READ F1 output (poor self-labels)
      ↓
    Step 6 F2 (Fresh): thiếu F1 input → prediction COARSE
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
    → Framework EXTENDS: 5 Pattern-Types, 4 axes, Compiled/Fresh split, valence gate

  THEORY THEORY (Gopnik, Meltzoff):
    → "Understand others by applying THEORIES of how minds work"
    → Framework position: Theory = Layer 4 schema override (Mode 1)
    → NOT replacement — SUPPLEMENT for when SPM fails

  DUAL PROCESS (Kahneman):
    → System 1 (fast, automatic) ≈ F1 (Compiled simulation)
    → System 2 (slow, deliberate) ≈ F2 (Fresh PFC draft)
    → Framework COMPATIBLE — maps naturally
    → v3.0 EXTENDS: System 1/2 = compilation level, not content type

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
    ③ ⭐ 2 Functions F1/F2 = Compiled/Fresh (not in mainstream ToM)
    ④ ⭐ Valence gate determines direction (not in standard empathy research)
    ⑤ ⭐ Context-dependent selection (compiled, unconscious)
    ⑥ Bird & Cook as architectural (upstream bottleneck)
    ⑦ Schema override as third pathway (Mode 1/2)
    ⑧ Resonance as retrospective ground truth
    ⑨ ⭐ Expert intuition = compiled, not separate from "feeling" [v3.0]
    ⑩ ⭐ PFC = Lawyer caveat on all SPM output [v3.0]
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

  F1-SPECIFIC TRAINING (Compiled simulation enhancement):
    → Deep listening (Rogers client-centered): F1-dominant practice
    → Compassion meditation (Metta): positive F1 firing practice
    → Fiction engagement: simulate characters safely
    → Cross-cultural immersion: broaden template range

  F2-SPECIFIC TRAINING (Fresh draft improvement):
    → Perspective-taking exercises: deliberate "if I were them" reasoning
    → Strategic games: chess, negotiation practice
    → Post-interaction reflection: "what did I predict? what happened?"
    → Journaling: articulate predictions explicitly

  CONTEXT-SELECTION TRAINING:
    → Diverse social engagement: build more context-specific chunk sets
    → Role-play: practice switching between contexts deliberately
    → Travel: expose to unfamiliar social contexts → build new selection patterns

  MODE-SWITCHING TRAINING (§2.4):
    → Therapists: train Mode A (Compiled-dominant) deliberately
    → Negotiators: train Mode B (Fresh-dominant) deliberately
    → Leaders: train Mode C balance for optimal social navigation

  v3.0 NOTE — COMPILATION AS TRAINING GOAL:
    → Training = build F2 chains → compile → F1 (§2.6)
    → Expertise = compiled SPM in specific domain
    → "Natural talent" = partially Resonance Baseline (hardware overlap)
    → "Learned skill" = compiled through deliberate practice
    → Both produce SAME quality compiled processing

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
    → F1: thin input → thin simulation → thin compiled library build
    → F2: less calibration data → prediction accuracy stalls
    → DEVELOPMENTAL CONCERN: children raised screen-primary → thin SPM

  RISK 2 — Parasocial at scale:
    → SPM fire on celebrities, influencers, AI companions
    → Rich template building WITHOUT calibration → DISTORTION
    → AI companions: simulate social interaction convincingly
      → But AI doesn't SPM user back → one-way → distortion

  RISK 3 — AI-triggered SPM without agent reality:
    → Coherent AI responses trigger SPM even when user KNOWS AI isn't agent
    → SPM fires on CUES, not beliefs (same as §10.5 fake cues)
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
  11. Group-scale: can Resonance emerge beyond dyads?
  12. Schema fallback boundary: when does brain switch from thin SPM to schema?
  13. PFC=Lawyer extent: how much does PFC rationalization distort SPM output
      reporting? Can meta-awareness reduce distortion? [v3.0]
  14. 3-cost measurement: can PFC draft, suppress, and uncertainty costs be
      independently measured in SPM contexts? [v3.0]
  15. Per-domain compilation: can F1/F2 ratio be measured per domain per person?
      Would this resolve "logic vs feeling personality" debate? [v3.0]
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
    🟢 Expert intuition = compiled pattern matching (Klein 1998)
    🟢 Moral Disengagement / dehumanization (Bandura 1999)
    🟢 Romanian orphanage: bootstrap disruption evidence
    🟢 Cognitive effort = metabolic cost (Gailliot & Baumeister 2007)
    🟢 PFC disconnect under stress (Arnsten 2009)
    🟢 Split-brain interpreter (Gazzaniga)
    🟢 Moral reasoning as post-hoc (Haidt 2001)
    🟢 Fear conditioning one-trial (LeDoux 1996)
    🟢 Evaluative conditioning (De Houwer 2007)
    🟢 Micro-expression leakage (Ekman 2003)
    🟢 Deception detection ≈ chance (DePaulo et al. 2003)

  FRAMEWORK SYNTHESIS (🟡):

    🟡 2 Functions F1/F2: consistent with dual-process, novel framing
    🟡 ⭐ Compiled/Fresh as real axis (not Feeling/Logic content) [v3.0]
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
    🟡 ⭐ Expert intuition = compiled, not bừa (shareable vs non-shareable) [v3.0]
    🟡 ⭐ PFC=Lawyer caveat on SPM output [v3.0]
    🟡 ⭐ 3-cost model applied to moral injury / professional SPM [v3.0]
    🟡 ⭐ Per-domain SPM ratio (not per-person fixed) [v3.0]
    🟡 ⭐ "Logic/Feeling personality = partially artifact" [v3.0]
    🟡 L1/L2 compensation model (Connection.md §3.3)
    🟡 Self-template ≠ empathy distinction (Drill-L2)

  HYPOTHESIS (🔴):

    🔴 Precise F1/F2 neural dissociability
    🔴 Context-selection compilation mechanism
    🔴 Valence gate precise circuitry
    🔴 Training ceiling predictions
    🔴 AI library distortion long-term effects
    🔴 Quantitative axis interactions
    🔴 PFC=Lawyer distortion magnitude measurement [v3.0]
    🔴 3-cost independent measurement protocol [v3.0]
    🔴 Per-domain F1/F2 ratio measurement [v3.0]

  OVERALL CONFIDENCE:
    → Mechanism framing: 🟢 STRONG
    → 2 Functions model: 🟡 SOLID framework synthesis, testable
    → Compiled/Fresh reframe: 🟡 SOLID, extends Kahneman + Klein [v3.0]
    → Reversed mapping: 🟢 Strong research support for phenomenon
    → Professional conflicts: 🟢 Strong evidence, 🟡 framework mapping
    → PFC=Lawyer: 🟢 Evidence (Gazzaniga, Haidt), 🟡 framework application [v3.0]
    → Quantitative claims: 🔴 Pending measurement protocols
```

---

## §18 — CROSS-REFERENCES

```
  PARENT + SIBLING:
    → Agent-Mechanism.md — integration hub, §5 SPM preview
    → By-Product-Gap-Resonance.md v1.0 — emergent mutual phenomenon (2-Stream architecture)
      §2 2-Stream Model: Stream 1 (hardware) + Stream 2 (SPM mutual)
      §3 Compiled/Fresh quality: Compiled+Compiled deep, Compiled+Fresh functional,
      Fresh+Fresh transactional (Stream 2 detail)

  MECHANISM FILES:
    → Inter-Body-Mechanism.md v1.0 — SOURCE cho:
      §3 Compiled/Fresh axis, §3.4 Shareable/Non-shareable compiled,
      §4 3-cost model, §5.4 By-Product Match, §7 PFC=Lawyer
    → Chunk.md v2.0 — chunk substrate, compilation
    → Feeling.md v2.0 — PFC observation interface (Step 5 = Feeling applied)
    → Logic-Feeling.md — 2 processing modes, parallel, modality bias
    → Valence-Propagation.md v2.0 — per-entity valence, Entity-Compiled, chain propagation
    → Body-Coupling.md v2.0 — coupling mechanism (builds ON SPM):
      SPM fire tích lũy → coupling compile → sustains independent of SPM
      §2.4 Mixed coupling, §7 Parent-child trajectory
    → Body-Feedback-Mechanism.md v2.0 — 2-source model, chunk dynamics, Body-Need
    → Body-Base.md v3.1 — entry point, 3 foundations

  OBSERVATION FILES:
    → Connection.md v3.3 — 3 generative primitives, 8 pathways, SPM × Resonance
      §3.3 2-luồng reward model (L1=SPM-momentary, L2=Entity-Compiled-structural)
    → Empathy.md v2.2 — SPM function applied to other agents
    → Status.md v2.0 — Resource Access Map, status scan
    → Protect.md v1.0 — ownership, loss aversion
    → Threat.md — NE cascade, PFC disconnect

  CORE:
    → Core-v7.8-Draft.md — cycle architecture
    → Cortisol-Baseline.md v2.0 — stress cascade, moral injury pathway

  APPLICATION:
    → Imagine-Final.md — imagination as simulator
    → Somatic-Articulation-Loop.md — body → words
    → AI-Schema-Detection.md v2.0 — AI interaction × SPM

  HEALTH CONDITIONS:
    → ADHD-Observation.md v1.2 §10 — late diagnosis SPM re-compile
    → Autism-Observation.md v1.0 §10 — late diagnosis identity re-compile
    → PTSD-Analysis.md v1.0 §11 — C-PTSD = SPM compiled under chronic threat

  RESEARCH ANCHORS (full alphabetical):
    → Amsterdam 1972 (rouge test)
    → Arnsten 2009 (PFC disconnect, α1 NE)
    → Bandura 1999 (moral disengagement, dehumanization)
    → Bird & Cook 2013 (alexithymia → empathy deficit — DECISIVE)
    → Chase & Simon 1973 (expert pattern matching)
    → Cikara 2014 (counter-empathy, competitive contexts)
    → Coan 2015 (Social Baseline Theory)
    → De Houwer 2007 (evaluative conditioning)
    → DePaulo et al. 2003 (deception detection ≈ 54%)
    → Dimberg 2000 (facial EMG mimicry, 300ms)
    → Dondi 1999 (newborn cry contagion)
    → Ekman 2003 (micro-expressions)
    → Ekman & Friesen 1969 (FACS)
    → Feldman 2007 (interpersonal synchrony)
    → Figley 2002 (compassion fatigue)
    → Gailliot & Baumeister 2007 (cognitive effort = metabolic cost)
    → Gazzaniga (split-brain interpreter module)
    → Gendlin 1978 (Focusing, felt sense)
    → Haidt 2001 (moral reasoning = post-hoc justification)
    → Kahneman 2011 (Dual Process, System 1/2)
    → Klein 1998 (expert intuition, recognition-primed decision)
    → LeDoux 1996 (fear conditioning, one-trial learning)
    → Litz 2009 (moral injury)
    → Milgram 1963 (obedience + distress)
    → Piaget 1929 (animism in young children)
    → Rogers (client-centered therapy)
    → Singer 2004, 2006 (shared activation + fairness modulation)
    → Svetlova 2010 (empathic helping 14-24m)
    → Takahashi 2009 (Schadenfreude, ventral striatum)
    → Tang 2015 (meditation + emotional processing)
    → Thomas & Chess 1977 (temperament, goodness-of-fit)
    → Wimmer & Perner 1983 (false belief task)

  STATUS:
    → v3.0 REWRITE — from v2.4 (2292L)
    → CORE CHANGE: F1/F2 reframed as Compiled/Fresh (not Feeling/Logic)
    → NEW: §2.0 (Compiled/Fresh axis), §2.6 (Expert intuition),
      §2.7 (Per-domain SPM), §3.7 PFC=Lawyer note,
      §10.4 3-cost enrichment
    → REFINED: ALL F1/F2 labels updated throughout,
      §8.1 PFC=Lawyer integration, §17 new 🟡/🔴 items
    → KEPT: §3-§16 mechanism core, all research citations (30+)
    → Backup: backup/Self-Pattern-Match-v2.4-backup.md
```

---

> *Bạn thấy bạn thân khóc → body bạn buồn nhẹ. Đó là F1 — COMPILED simulation.*
> *Bạn nghĩ: "bạn cần an ủi." Đó là F2 — FRESH PFC draft.*
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
> *"Feeling" hay "Logic"? Chỉ là label.*
> *Inside body: chỉ có compiled ←→ fresh.*
> *Einstein "cảm" toán. Therapist "nghĩ" cảm xúc.*
> *Cùng mechanism — khác compilation level.*
>
> *SPM không phải empathy module. Không phải agent-reading module.*
> *Là GENERAL-PURPOSE self-template simulator.*
> *Empathy, Schadenfreude, negotiation, teaching, fiction engagement —*
> *tất cả = cùng 1 mechanism, khác valence × context × compilation level.*
>
> *Hiểu SPM = hiểu phần lớn cách con người tương tác.*

---

## Changelog

```
v1.0 (2026-04-15): 1,518L. SPM as unified process — 6 steps, 5 pattern-types,
  4 axes, developmental, Bird & Cook, ToM, training, AI.

v2.0 (2026-04-24): 1,948L. REWRITE — F1 "Feeling" / F2 "Logic" dual functions,
  context-dependent selection, valence gate, reversed mapping, professional SPM,
  moral injury, strategic SPM (poker/fake/meta).

v2.1-v2.3: Refinements — Connection v3.0 cross-refs, 2-luồng reward model,
  Drill-L2 insights (self-template ≠ empathy), Entity-Compiled terminology.

v2.4 (2026-05-15): 2,292L. +§18 Late diagnosis re-compile (Health Conditions Drill),
  C-PTSD = SPM compiled under chronic threat.

v3.0 (2026-05-17): ~2,400L. REWRITE — Compiled/Fresh reframe:
  ★ F1/F2 reframed: F1 = Compiled simulation, F2 = Fresh PFC draft
    "Feeling/Logic" = observer labels, not mechanism description
    Consistent with Inter-Body-Mechanism.md §3 (Compiled/Fresh axis)
  ★ Expert intuition = compiled, not bừa (§2.6)
    Shareable vs non-shareable compiled. Klein 1998.
  ★ PFC = Lawyer not Judge (§3.7, §4.3, §8.1)
    Stated reason ≠ actual body-need. Gazzaniga, Haidt 2001.
  ★ 3-cost model enrichment (§2.4, §10.4, §10.5)
    PFC draft + Suppress + Uncertainty = independent cost sources.
  ★ Per-domain SPM (§2.7)
    Cùng người, khác domain → khác compiled/fresh ratio.
    "Logic/Feeling personality" = partially artifact.
  ★ Updated cross-refs to all v2.0/v3.0 file versions
  ★ 3 new open questions (§16): PFC-Lawyer, 3-cost measurement, per-domain
  ★ Honest assessment updated: 7 new 🟡, 3 new 🔴 items
  ★ Research citations: 30+ preserved, +Gazzaniga, +Haidt 2001, +Thomas & Chess 1977
  Backup: Self-Pattern-Match-v2.4-backup.md
```
