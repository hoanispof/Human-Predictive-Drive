# Drill: Compile Architecture — 1 Engine + 3 Modulators

> **Session**: 2026-06-01
> **Trigger**: Phân tích Trust Compile → phát hiện ALL compile = 1 engine
> **Method**: Edge case testing × 8 + cross-file verification × 10+ files
> **Status**: DRILL (phân tích sâu, chưa propagate vào framework files)

---

## MỤC LỤC

- §1 — UNIFYING PRINCIPLE: All Compile = Exposure → Hebbian
- §2 — ENGINE A: Exposure → Hebbian → Compile
- §3 — MODULATOR B: Entity-Valence Bias (Automatic)
- §4 — SOURCE C: 3 Exposure Channels (Song Song)
- §5 — MODULATOR D: PFC Hold + Suppress (Deliberate)
- §6 — MULTI-STREAM COMPILE: Đồng Thời Nhiều Stream
- §7 — FEEDBACK LOOPS: Tương Tác Giữa Components
- §8 — 3 COMPILE TYPES = MODULATOR CONFIGURATIONS
- §9 — EVOLUTIONARY GRADIENT: Modulators Qua Tiến Hóa
- §10 — EDGE CASES VERIFIED (8+)
- §11 — OPEN QUESTIONS
- §12 — IMPLICATIONS CHO FRAMEWORK
- §13 — CROSS-REFERENCES + CITATIONS

---

## §1 — UNIFYING PRINCIPLE: All Compile = Exposure → Hebbian

```
⭐⭐⭐ INSIGHT CỐT LÕI CỦA SESSION NÀY:

  TẤT CẢ compile đều đi qua 1 con đường duy nhất:

    EXPOSURE → HEBBIAN STRENGTHENING → COMPILED CHUNK

  Không có "trust compile mechanism" riêng.
  Không có "expertise compile mechanism" riêng.
  Không có "experience compile mechanism" riêng.

  CHỈ CÓ 1 ENGINE.

  3 Compile Types hiện tại (Experience / Expertise / Trust)
  = LABELS cho DOMINANT MODULATOR CONFIGURATION,
  KHÔNG phải 3 cơ chế riêng biệt.


  TẠI SAO:

  ① Hebbian = cơ chế wiring DUY NHẤT của neurons:

     "Neurons that fire together wire together" (Hebb 1949)
     LTP = Long-Term Potentiation (Bliss & Lømo 1973)
     LTD = Long-Term Depression (Dudek & Bear 1992)

     Không có cơ chế thứ 2.
     Trust KHÔNG tạo connections mới theo cách khác.
     PFC KHÔNG wire patterns theo cách khác.
     TẤT CẢ đều qua LTP/LTD.


  ② Exposure = điều kiện CẦN cho Hebbian:

     Neurons chỉ fire together khi được ACTIVATED.
     Activation = exposure (tiếp xúc với pattern).
     Không exposure → không activation → không Hebbian → không compile.

     Exposure có thể từ NHIỀU NGUỒN (§4), nhưng cơ chế SAU exposure
     luôn là cùng 1: Hebbian strengthening.


  ③ Mọi thứ KHÁC = modulators TRƯỚC hoặc TRONG quá trình exposure:

     Entity-Valence → tự động amplify/suppress exposure tới certain patterns
     PFC → chủ động amplify/suppress exposure tới certain patterns
     Sources → kênh CUNG CẤP exposure (external, internal, automatic)

     Modulators THAY ĐỔI:
       - CƯỜNG ĐỘ exposure (amplify/suppress)
       - HƯỚNG exposure (approach/avoidance)
       - NGUỒN exposure (external/internal)
       - CHẤT LƯỢNG exposure (multi-modal/single-modal)

     Modulators KHÔNG THAY ĐỔI:
       - CƠ CHẾ compile (luôn Hebbian)


  ANALOGY:

    Engine ô tô = luôn đốt xăng (1 cơ chế).
    Ga / phanh / tay lái = modulators (thay đổi tốc độ + hướng).
    Đường / cao tốc / đường đất = sources (nơi xe chạy).

    Xe "chạy nhanh" vs "chạy chậm" vs "rẽ phải"
    = KHÔNG PHẢI 3 loại động cơ khác nhau.
    = CÙNG 1 động cơ, KHÁC modulators.

    3 Compile Types = cùng 1 Hebbian engine, khác modulator configs.


  🟢 Hebbian learning: Hebb 1949 (foundational)
  🟢 LTP discovery: Bliss & Lømo 1973
  🟢 LTD: Dudek & Bear 1992
  🟡 "1 engine + 3 modulators" unification: framework synthesis (session 2026-06-01)
```

### §1.1 — Tại sao framework CHƯA nhìn ra điều này

```
🟡 NGUYÊN NHÂN:

  Compile-Taxonomy.md v2.0 organize theo OUTPUT (3 types KHÁC NHAU):
    Experience = "body trải nghiệm trực tiếp"
    Expertise = "PFC-directed qua nhiều năm"
    Trust = "trusted source install"

  Đúng ở level description. SAI ở level mechanism.

  Giống như phân loại:
    "đi bộ" vs "chạy" vs "leo núi" = 3 loại di chuyển KHÁC NHAU.
    Nhưng mechanism = CÁC CƠ co rút (1 mechanism).
    Khác = speed, direction, terrain (modulators).

  Framework focus vào KHÁC BIỆT giữa 3 types (§2.4 bảng so sánh).
  Session này focus vào ĐIỂM CHUNG: tất cả đều qua exposure → Hebbian.


  CÓ THỂ RECONCILE:

  Compile-Taxonomy v2.0 KHÔNG SAI — nó describe patterns ĐÚNG.
  Nhưng organizing principle CẦN SHIFT:

    v2.0: "3 separate types" (taxonomy-first)
    → v3.0: "1 engine + modulator configurations" (mechanism-first)

  Content GIỐNG, organizing principle KHÁC.
  §1 (3 constraints) → KEEP 100%.
  §2 (3 types) → REFRAME as modulator configs.
  §3-§7 → KEEP + enrich.
```

---

## §2 — ENGINE A: Exposure → Hebbian → Compile

```
⭐ ENGINE A = CƠ CHẾ COMPILE DUY NHẤT:

  ┌───────────────────────────────────────────────────┐
  │                ENGINE A                            │
  │                                                   │
  │  [Exposure] → [Neural Activation] → [Hebbian]     │
  │       ↓              ↓                  ↓          │
  │  Pattern tiếp   Neurons fire      LTP/LTD         │
  │  xúc với brain  together          strengthen/      │
  │                                   weaken           │
  │                        ↓                           │
  │                 [Compiled Chunk]                    │
  │                 (auto-fire khi                      │
  │                  triggered)                        │
  └───────────────────────────────────────────────────┘

  Engine A luôn hoạt động GIỐNG NHAU bất kể:
    - Ai cung cấp exposure (mẹ, thầy, tự mình, reality)
    - Exposure từ đâu (external body-input, PFC imagination, spontaneous)
    - Có trust hay không (trust chỉ AMPLIFY, không thay đổi mechanism)
    - PFC có tham gia hay không (PFC chỉ DIRECT, body vẫn compile)
```

### §2.1 — compile_rate formula: exposure là tham số FIRST

```
🟢🟡 compile_rate ≈ f(exposure × saliency × contingency
                     × peak_valence × multi_modal_richness)

  (Chunk.md §2.2 — 5-parameter compile rate formula)


  PHÂN TÍCH TỪ GÓC ĐỘ ENGINE:

  ① EXPOSURE = tham số FIRST (điều kiện CẦN):
     Không exposure → compile_rate = 0, bất kể các tham số khác.
     Exposure = số lần pattern được activate.
     = Repetition (Chunk.md §2.1 ①) chính là "nhiều exposure."

  ② 4 tham số còn lại = QUALITY DIMENSIONS của exposure:
     Saliency = exposure nổi bật đến mức nào
     Contingency = exposure có predictable association không
     Peak valence = exposure có emotional peak không (→ 1 lần đủ compile)
     Multi-modal richness = exposure qua bao nhiêu kênh cùng lúc

  → 4 COMPILE MECHANISMS (Chunk.md §2.1) = 4 cách TĂNG exposure quality:
     ① Repetition = tăng exposure QUANTITY
     ② Emotional peak = tăng peak_valence (1 lần = nhiều lần thường)
     ③ Multi-modal = tăng multi_modal_richness
     ④ Sleep = replay = THÊM exposure cycles offline (§11 Drill-Compile-Sleep)


  IMPLICATION:

  Engine A KHÔNG phân biệt nguồn exposure.
  Experience exposure, Trust-amplified exposure, PFC-directed exposure
  = ĐỀU feed vào CÙNG 1 formula.

  Sự khác biệt giữa 3 Compile Types = khác MODULATORS,
  không phải khác engine.


  🟢 5-parameter compile rate: Chunk.md §2.2 (cross-state validated)
  🟢 LTP frequency-dependent: Bliss & Lømo 1973
  🟢 Emotional peak = amygdala-mediated LTP: McGaugh 2004
  🟡 4 quality dimensions interpretation: framework synthesis
```

### §2.2 — Chunk.md §1.1 "NO SOURCE TAG" = evidence cho 1 engine

```
🟢 KEY EVIDENCE: COMPILED CHUNKS KHÔNG CÓ TAG NGUỒN GỐC:

  Chunk.md §1.1: "Body treats trust-compiled = experience-compiled"

  Nếu có 3 mechanisms KHÁC NHAU → kỳ vọng chunks CÓ tag mechanism.
  Nhưng KHÔNG: chunks từ experience = chunks từ trust = chunks từ PFC-directed
  = BÌNH ĐẲNG trong body.

  TẠI SAO: vì tất cả đều qua CÙNG 1 engine (Hebbian LTP).
  Product GIỐNG NHAU → mechanism GIỐNG NHAU.

  Analogy: nước từ mưa, từ sông, từ giếng = CÙNG H₂O.
  Không ai phân biệt "nước mưa" vs "nước sông" trong cơ thể.
  Vì quá trình hấp thụ (engine) = GIỐNG NHAU.

  → "NO SOURCE TAG" KHÔNG phải limitation.
  → Nó là CONSEQUENCE của 1 engine: products luôn identical.


  🟢 No source tag: Chunk.md §1.1 (established in framework)
  🟢 Source monitoring errors: Johnson et al. 1993 (reality monitoring framework)
  🟡 No source tag = 1-engine consequence: framework synthesis
```

---

## §3 — MODULATOR B: Entity-Valence Bias (Automatic)

```
⭐ MODULATOR B = ENTITY-VALENCE BIAS:

  ┌───────────────────────────────────────────────────┐
  │             MODULATOR B                            │
  │                                                   │
  │  Entity-Compiled per-entity:                       │
  │    Structural Valence Profile × Trust dimension    │
  │                                                   │
  │  OPERATES:                                        │
  │    ① AMPLIFY compile rate cho positive entities    │
  │    ② SUPPRESS compile rate cho negative entities   │
  │    ③ BIAS attention tới trusted sources AUTO       │
  │                                                   │
  │  COST: ≈ 0 (compiled, automatic)                   │
  │  SPEED: fast (subcortical, pre-PFC)                │
  │  OVERRIDE PFC: CÓ THỂ (Entity-Valence → PFC)      │
  └───────────────────────────────────────────────────┘


  CƠ CHẾ CHI TIẾT:

  Entity-Valence-Dynamics.md §1:
    Structural Valence = INSIDE Entity-Compiled, slow, accumulated
    Current Valence = outside, fast, per-moment

  Trust = VALENCE META-DIMENSION (Valence-Propagation §2):
    Trust KHÔNG phải hệ thống riêng biệt.
    Trust = 1 chiều TRONG valence profile per-entity.
    Trust MODULATE CƯỜNG ĐỘ các channels KHÁC:
      Trust HIGH → mọi valence từ entity NÀY MẠNH hơn
      Trust LOW → mọi valence từ entity NÀY YẾU hơn
    = Trust = MULTIPLIER cho toàn bộ profile.
```

### §3.1 — Trust = AMPLIFIER, không phải GATE

```
⭐⭐ REFRAME QUAN TRỌNG:

  HIỆN TẠI (Chunk.md §2.3 line 288):
    "TRUST = GATE CHO EXTERNAL INSTALL"
    → Binary: có trust → compile. Không trust → không compile.

  VẤN ĐỀ:
    Entity-Access.md §2: gradient Mức 0-5 per-entity.
    Mức 0 (stranger) → Mức 5 (self/child).
    = GRADIENT, KHÔNG PHẢI binary gate.

  RECONCILE:

    Trust = AMPLIFIER (gradient), KHÔNG PHẢI gate (binary).

    ┌────────────┬──────────────────────────────────┐
    │ Mức 0      │ Multiplier ≈ 0 → compile rate    │
    │ (stranger) │ CỰC THẤP từ entity này           │
    │            │ (LOOKS like gate = off)           │
    ├────────────┼──────────────────────────────────┤
    │ Mức 1      │ Multiplier thấp → compile rate    │
    │ (acquaint) │ thấp (cần NHIỀU exposure bù)      │
    ├────────────┼──────────────────────────────────┤
    │ Mức 2-3    │ Multiplier trung bình → compile   │
    │ (friend)   │ rate bình thường                  │
    ├────────────┼──────────────────────────────────┤
    │ Mức 4      │ Multiplier cao → compile rate     │
    │ (partner)  │ CAO (ít exposure vẫn compile)     │
    ├────────────┼──────────────────────────────────┤
    │ Mức 5      │ Multiplier MAX → compile rate     │
    │ (self/     │ CỰC CAO                          │
    │  child)    │ (1-2 lần exposure = compile sâu)  │
    └────────────┴──────────────────────────────────┘

    "Gate" = limit case CỦA amplifier khi multiplier → 0.
    Gate behavior ĐÚNG ở Mức 0. Nhưng KHÔNG đúng cho toàn bộ spectrum.
    "Amplifier" bao hàm cả gate behavior + gradient behavior.


  VÍ DỤ KIỂM CHỨNG:

    Mẹ nói "học đi con" → trust Mức 4-5 → amplifier CAO
    → Ít exposure (mẹ nói VÀI LẦN) đã compile [học → tốt]

    Người lạ nói "bạn nên học nghề A" → trust Mức 0-1 → amplifier THẤP
    → Exposure NHIỀU (nghe NHIỀU người nói) MỚI compile
    → Hoặc: social proof (quantity) bù cho individual trust thấp

    Bạn thân nói "thử nhạc jazz đi" → trust Mức 2-3 → amplifier TRUNG BÌNH
    → Vài lần exposure + positive experience → compile [jazz → thú vị]

    → Gradient behavior. KHÔNG binary.


  TERMINOLOGY CẦN UPDATE:
    Chunk.md §2.3: "gate" → "amplifier" (hoặc "gradient multiplier")
    Compile-Taxonomy §2.3 line 329: "gate cho toàn bộ quá trình" → reframe


  🟢 Entity-Access gradient Mức 0-5: Entity-Access.md §2
  🟢 Trust = valence meta-dimension: Valence-Propagation §2
  🟡 Trust = amplifier (not gate): framework synthesis (session 2026-06-01)
  🟡 Gate = limit case of amplifier: framework synthesis
```

### §3.2 — Modulator B hoạt động TRƯỚC PFC

```
🟡 ENTITY-VALENCE BIAS = PRE-PFC, AUTOMATIC:

  Timeline khi nhận exposure từ entity:

    t₀:   Exposure arrives (body-input hoặc internal)
    t₁:   Entity recognized → Entity-Compiled activates
           (~100ms, subcortical + fusiform)
    t₂:   Structural Valence loaded → trust multiplier applied
           = Modulator B ACTIVATED
    t₃:   PFC receives ALREADY-MODULATED signal
           (~200ms+, prefrontal cortex)
    t₄:   PFC CÓ THỂ override (Hold/Suppress)
           nhưng CẦN EFFORT (Modulator D cost)

  → Entity-Valence bias đã SHAPE exposure TRƯỚC KHI PFC nhận.
  → PFC chỉ CÓ THỂ override SAU ĐÓ, VỚI cost.

  IMPLICATION:
    "Ghét giáo viên → khó học" = Modulator B suppress TRƯỚC PFC.
    PFC CAN override (Hold: "tập trung vào bài"), nhưng cost ① PFC draft.
    = Tại sao "muốn con hay chữ thì yêu lấy thầy":
      Nếu Entity-Valence positive cho thầy → Modulator B amplify AUTO
      → PFC KHÔNG CẦN override → cost ≈ 0 → learn easier.


  🟢 Amygdala/subcortical response ~100ms: established neuroscience
  🟢 PFC response ~200ms+: LeDoux 1996
  🟡 Entity-Valence pre-PFC timing model: framework synthesis
```

### §3.3 — Trust amplifies VALUE install, KHÔNG phải content compile

```
⭐ PHÂN BIỆT QUAN TRỌNG:

  Trust amplifies VALUE compile (giá trị đánh giá):
    Mẹ nói "học là tốt" → trust Mức 5 → [học = tốt] compile NHANH (value)

  Trust KHÔNG amplify CONTENT compile (kiến thức):
    Trẻ bị ép học → KHÔNG trust "học là tốt"
    NHƯNG vẫn compile nội dung bài toán qua exposure trực tiếp
    → Content compiles từ Experience (Engine A), KHÔNG cần trust


  2 STREAM CHẠY SONG SONG:

    Stream 1 — CONTENT: exposure trực tiếp với nội dung
      → Engine A (Hebbian) → compile kiến thức
      → Trust KHÔNG ảnh hưởng (content compile = Experience)

    Stream 2 — VALUE: exposure với đánh giá (tốt/xấu/thú vị/nguy hiểm)
      → Engine A (Hebbian) + Modulator B (trust amplify/suppress)
      → Trust AMPLIFY value install → compile giá trị NHANH/CHẬM


  VÍ DỤ — TRẺ BỊ ÉP HỌC:

    Content stream: ngồi học → exposure với kiến thức → Hebbian
      → compile [2+2=4], [từ vựng mới], [công thức hoá]
      → = Experience Compile (Engine A, Source C1 external)
      → Trust KHÔNG cần — body tiếp xúc trực tiếp

    Value stream: bị mẹ mắng khi không học
      → compile [không học → nguy hiểm → tránh] (threat direction)
      → = Experience Compile direction avoidance
      → Trust cho "mẹ" CÓ THỂ cao nhưng trust cho "học = tốt" THẤP
      → Value tag = AVOIDANCE, không phải APPROACH

    Entity stream: mẹ ép → Entity-Valence update
      → [mẹ + học] → mixed valence (mẹ = trust nhưng ép = negative)
      → = Entity-Valence compile (Engine A + Modulator B)

    → Cùng 1 tình huống: 3 streams, 3 modulator configs KHÁC NHAU.
    → Chi tiết multi-stream: §6.


  🟡 Trust scope = value not content: framework synthesis (session 2026-06-01)
  🟡 Multi-stream parallel: framework synthesis
  🟢 Hebbian indifferent to source: established neuroscience
```

---

## §4 — SOURCE C: 3 Exposure Channels (Song Song)

```
⭐ EXPOSURE ĐẾN TỪ 3 KÊNH CHẠY SONG SONG:

  ┌───────────────────────────────────────────────────┐
  │ C1: EXTERNAL (body-input)                          │
  │                                                   │
  │   Sensory exposure từ environment:                 │
  │   Visual, auditory, tactile, olfactory, gustatory  │
  │   + Social: facial expressions, prosody, gestures  │
  │   + Actions: motor feedback, proprioception        │
  │                                                   │
  │   = Body-Feedback-Mechanism §1.2 ①                 │
  │     Hardware/Sensory-Driven (pre-chunk possible)   │
  │                                                   │
  │   ĐẶC ĐIỂM:                                       │
  │   - Multi-modal RICHEST (nhiều kênh nhất)          │
  │   - Direct = compile SÂU nhất                      │
  │   - KHÔNG cần PFC, KHÔNG cần compiled chunks       │
  │   - Available cho TẤT CẢ species                   │
  └───────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────┐
  │ C2: INTERNAL-DELIBERATE (PFC imagination/simulate) │
  │                                                   │
  │   PFC chủ động tạo internal exposure:              │
  │   Imagine scenario, nhẩm từ vựng, mental rehearsal │
  │   Thought experiment, planning, problem solving    │
  │   Deliberate recall, self-talk                     │
  │                                                   │
  │   = Simulation-Engine.md: Constructive Simulation  │
  │     (DMN + hippocampus: recombine chunks)          │
  │   = PFC-Operations §2.1: Hold = amplify pattern    │
  │                                                   │
  │   ĐẶC ĐIỂM:                                       │
  │   - Multi-modal NGHÈO hơn C1 (imagination < real)  │
  │   - NHƯNG: body REACT thật (nước bọt, tim đập)    │
  │   - Cần PFC budget (fatigable)                     │
  │   - Human-dominant (PFC developed)                 │
  │   - CÓ THỂ compile abstract domains (toán, lý)    │
  └───────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────┐
  │ C3: INTERNAL-AUTOMATIC (spontaneous chunk fire)    │
  │                                                   │
  │   Chunks đã compile TỰ fire (không PFC direct):    │
  │   Background-Pattern continuous activation         │
  │   Memory resurface (spontaneous recall)            │
  │   Association chains (chunk A → fire chunk B)      │
  │   Dream fragments carry-over                       │
  │   Earworms, intrusive thoughts, rumination         │
  │                                                   │
  │   = Body-Feedback-Mechanism §1.2 ②                 │
  │     Chunk Dynamics / Pattern-Driven                │
  │   = Background-Pattern.md: accumulated pattern     │
  │     fires continuously at baseline                 │
  │                                                   │
  │   ĐẶC ĐIỂM:                                       │
  │   - Cost ≈ 0 (automatic, no PFC)                   │
  │   - REQUIRES compiled chunks (chicken-egg: C1 → C3)│
  │   - Self-reinforcing: pattern fire → exposure      │
  │     → strengthen → fire MORE → snowball            │
  │   - Can be NEGATIVE (rumination, trauma replay)    │
  │   - Human-rich (complex chunk networks)            │
  └───────────────────────────────────────────────────┘
```

### §4.1 — 3 Sources chạy SONG SONG, tỉ lệ biến thiên

```
⭐ SONG SONG, KHÔNG LOẠI TRỪ:

  Mọi khoảnh khắc = C1 + C2 + C3 CÙNG active.
  Chỉ khác TỈ LỆ.


  ┌─────────────────────┬──────┬──────┬──────┐
  │ Tình huống          │  C1  │  C2  │  C3  │
  ├─────────────────────┼──────┼──────┼──────┤
  │ Bé 6 tháng chơi    │ 90%  │  2%  │  8%  │
  │ Trẻ bị ép học      │ 60%  │  5%  │ 35%  │
  │ Sinh viên đọc sách │ 40%  │ 40%  │ 20%  │
  │ Expert suy nghĩ    │ 10%  │ 60%  │ 30%  │
  │ Thiền định          │ 30%  │ 10%  │ 60%  │
  │ Nằm mơ (REM)       │  0%  │  0%  │100%  │
  │ Nấu ăn thường      │ 70%  │  5%  │ 25%  │
  │ Nhạc sĩ sáng tác   │ 20%  │ 40%  │ 40%  │
  └─────────────────────┴──────┴──────┴──────┘

  % = ƯỚC LƯỢNG minh hoạ, KHÔNG phải đo lường chính xác.

  NGUYÊN TẮC:
    - C1 cao khi tương tác trực tiếp với environment
    - C2 cao khi PFC deliberate (study, problem-solve, plan)
    - C3 cao khi chunk network rich + PFC relaxed (thiền, shower, rest)
    - Nằm mơ = C3 only (C1 blocked by thalamus, PFC offline)

  QUAN TRỌNG: tỉ lệ KHÔNG cố định.
  Trong 1 buổi học 2 tiếng, tỉ lệ C1:C2:C3 thay đổi LIÊN TỤC.
  Phút 1: C1 cao (nghe giảng). Phút 30: C2 cao (suy nghĩ bài tập).
  Phút 45: C3 cao (mind wandering). Phút 50: C1 cao lại (thầy hỏi).


  🟡 3-source parallel model: framework synthesis
  🟡 Percentage estimates: illustrative, not measured
  🟢 Mind wandering = DMN activation: Smallwood & Schooler 2006
  🟢 Dream = internal activation without external input: Hobson 2009
```

### §4.2 — C1 External: body-input exposure

```
🟢 C1 = EXPOSURE QUA SENSORY INPUT TỪ ENVIRONMENT:

  ĐẶC ĐIỂM NỔI BẬT:

  ① MULTI-MODAL RICHEST:
     5+ sensory channels đồng thời
     → compile_rate cao nhất (multi_modal_richness parameter)
     → VD: chạm lửa = visual + thermal + pain + smell + motor retract
     = Chunk.md §2.1 ③: multi-modal = compile mechanism mạnh

  ② DIRECT = CÓ domain feedback:
     Body test pattern AGAINST REALITY
     → Domain-Checked verification (Ask-AI.md §6.1)
     → SAI → prediction delta → body adjust
     → = Self-correcting (Reality = ultimate teacher)

  ③ KHÔNG CẦN PFC:
     Bé 6 tháng: PFC minimal → C1 dominant → still compiles
     Động vật: PFC limited → C1 = primary exposure source
     → C1 = phylogenetically OLDEST exposure channel

  ④ 5 EXTERNAL INSTALL MECHANISMS (Chunk.md §2.3):
     Co-attention, imitation, social referencing,
     label installation, cultural transmission
     → TẤT CẢ = variants of C1 (external → body-input)
     → Trust (Modulator B) AMPLIFY C1 từ trusted entities


  🟢 Multi-modal encoding superiority: established neuroscience
  🟢 Direct experience = strongest learning: Kolb 1984 (experiential learning)
  🟢 5 external install mechanisms: Chunk.md §2.3 (framework established)
```

### §4.3 — C2 Internal-Deliberate: PFC imagination

```
🟡🟢 C2 = PFC CHỦ ĐỘNG TẠO EXPOSURE NỘI BỘ:

  CƠ CHẾ:
    PFC activate Simulation-Engine (Simulation-Engine.md):
      ① Interoception: read body signals
      ② Constructive Simulation: recombine chunks → new scenarios
      ③ Self/Other Model: target simulation

    → Body REACT với simulation (PFC-Function ⑩):
      Imagine chanh → nước bọt THẬT
      Imagine chó cắn → tim đập THẬT
      Imagine giải bài → opioid THẬT (nhẹ hơn real)

    → Body react = body EXPOSURE (internal, không phải external)
    → Engine A (Hebbian) → compile

  VÍ DỤ C2 EXPOSURE:
    Nhẩm từ vựng tiếng Anh × 20 lần → repetition → compile
    Tưởng tượng tình huống presentation → mental rehearsal → compile
    Einstein thought experiment → imagine → body evaluate → compile
    Học tên "orange" → imagine quả cam → multi-modal internal → compile

  3 GIỚI HẠN (Compile-Taxonomy §5):
    ① Multi-modal nghèo hơn C1 (imagination < direct experience)
    ② Self-Referencing risk (test against SELF, not REALITY)
    ③ Intensity thấp hơn (opioid nhẹ hơn real experience)

  NHƯNG: C2 CÓ THỂ compile domains C1 KHÔNG THỂ:
    Abstract math, theoretical physics, philosophy, planning
    = Domains KHÔNG CÓ direct sensory input
    → C2 = ONLY exposure channel cho abstract domains
    → = Tại sao humans = species DUY NHẤT có toán, vật lý, triết học


  🟢 Mental rehearsal improves performance: Driskell et al. 1994 (meta-analysis)
  🟢 Motor imagery activates motor cortex: Jeannerod 2001
  🟢 Imagination → physiological response: established (salivation, HR)
  🟡 C2 as abstract domain exposure: framework synthesis
```

### §4.4 — C3 Internal-Automatic: spontaneous chunk fire

```
🟡 C3 = CHUNKS TỰ FIRE TẠO EXPOSURE KHÔNG CHỦ ĐÍCH:

  CƠ CHẾ:
    Compiled chunks tự activate (Hebbian: strong connections = low threshold)
    → Activation = exposure → CÓ THỂ strengthen further (Engine A)
    → KHÔNG cần PFC direct (≠ C2)
    → KHÔNG cần external input (≠ C1)

  NGUỒN C3:

    ① Background-Pattern continuous baseline:
       Background-Pattern.md: accumulated pattern fires LIÊN TỤC
       → Biases ALL processing (retrieval, template, interpretation)
       → Triple Bias = C3 exposure KHÔNG NGỪNG
       → VD: người lạc quan → positive patterns fire liên tục
             → exposure dương → reinforce → snowball

    ② Spontaneous memory resurface:
       Đi ngang quán cũ → chunk [quán + người yêu cũ] fire
       → Exposure lại với pattern cũ → CÓ THỂ strengthen
       → = Reconsolidation window risk (Nader 2000)

    ③ Association chains:
       Chunk A fire → linked chunk B fire → linked chunk C fire
       → Cascade = exposure sequence tự động
       → VD: nghe nhạc → nhớ kỷ niệm → nhớ người → nhớ mùi

    ④ Mind wandering:
       PFC release → DMN activate → chunks fire spontaneously
       → Smallwood & Schooler 2006: 30-50% waking time
       → = C3 exposure CHIẾM 30-50% thời gian thức

    ⑤ Intrusive patterns (negative C3):
       Trauma chunks: fire intensity cao, repetitive
       → Exposure → strengthen → fire MORE → vicious cycle
       → Rumination: C3 + partial C2 → strengthen worry patterns
       → = Tại sao "đừng nghĩ về nó" KHÔNG WORK (Wegner 1987)

  ĐẶC ĐIỂM C3:
    → Self-reinforcing: strong patterns fire → exposure → stronger → fire more
    → KHÔNG thể "tắt" (suppress = Modulator D, cost ②)
    → REQUIRES compiled chunks (C3 KHÔNG hoạt động ở newborn)
    → Background-Pattern = most pervasive C3 source


  🟢 Mind wandering 30-50%: Smallwood & Schooler 2006
  🟢 DMN activation during rest: Raichle et al. 2001
  🟢 Intrusive memories: Brewin et al. 2010
  🟢 Ironic process: Wegner 1987
  🟡 C3 as exposure source classification: framework synthesis
```

### §4.5 — C1+C2+C3 feed vào CÙNG Engine A

```
⭐ CONVERGENCE:

  C1 (external body-input)     ─┐
  C2 (PFC imagination)         ─┤→ Neural Activation → Engine A (Hebbian) → Compile
  C3 (spontaneous chunk fire)  ─┘

  Engine A KHÔNG phân biệt nguồn.
  Neurons fire together (bất kể trigger) → wire together.

  = Giải thích tại sao:
    Imagination CAN compile (C2 → Engine A)
    Rumination CAN strengthen worry (C3 → Engine A)
    Direct experience = MẠNH nhất (C1 multi-modal richness)
    BUT: accumulated C3 over years = CŨNG rất mạnh (Background-Pattern)


  PFC CÓ THỂ AMPLIFY cả C1 VÀ C2:

  PFC amplify C1:
    Chú ý nghe giảng (Hold) → C1 exposure TĂNG quality
    Chủ động đi thực hành (Change Environment) → C1 exposure MỚI

  PFC amplify C2:
    Nhẩm từ vựng (Hold + Imagination) → C2 exposure TĂNG repetition
    Thought experiment (Constructive Simulation) → C2 exposure MỚI

  PFC KHÔNG trực tiếp control C3:
    Background-Pattern fire tự động → PFC observe SAU
    Intrusive thoughts = C3 fire → PFC CAN suppress (cost ②)
    BUT: suppress C3 = Modulator D cost, KHÔNG tắt được C3 source

  → PFC = DIRECTOR cho C1+C2, OBSERVER cho C3.


  🟡 3-source convergence into 1 engine: framework synthesis
  🟢 PFC top-down attention modulation: Miller & Cohen 2001
  🟢 PFC cannot suppress intrusive thoughts permanently: Wegner 1987
```

---

## §5 — MODULATOR D: PFC Hold + Suppress (Deliberate)

```
⭐ MODULATOR D = PFC OPERATIONS:

  ┌───────────────────────────────────────────────────┐
  │             MODULATOR D                            │
  │                                                   │
  │  2 OPERATIONS (PFC-Operations.md §2):              │
  │                                                   │
  │  D1: HOLD = PFC Amplify                            │
  │    → Top-down signal → amplify target pattern      │
  │    → = TĂNG exposure quality cho specific pattern   │
  │    → CAN lead to compilation (positive trajectory) │
  │    → Cost: ① PFC draft (processing load)           │
  │    → Brain: dlPFC, FEF                             │
  │                                                   │
  │  D2: SUPPRESS = PFC Inhibit                        │
  │    → Inhibitory signal → block output route        │
  │    → = GIẢM exposure cho specific pattern           │
  │    → CANNOT compile "not" (only block, not build)  │
  │    → Cost: ② Efference mismatch                    │
  │    → Brain: rIFG, vlPFC                            │
  │                                                   │
  │  BOTH: finite budget, fatigable, evolutionary mới  │
  └───────────────────────────────────────────────────┘


  MODULATOR D TRONG COMPILE ARCHITECTURE:

  D1 HOLD = AMPLIFY EXPOSURE:
    PFC Hold pattern trong working memory
    → Pattern fire LIÊN TỤC (sustained activation)
    → = TĂNG exposure quantity + quality
    → Engine A (Hebbian) strengthen
    → Learning trajectory: Hold → compile → automatic → PFC release
    → = Compile-Taxonomy §5: "PFC-directed body compile"

  D2 SUPPRESS = REDUCE EXPOSURE (indirect):
    PFC block pattern output → pattern VẪNEXIST
    → NHƯNG: output blocked → pattern fire ÍT contexts
    → = GIẢM exposure cho pattern bị suppress
    → NHƯNG: pattern vẫn fire internally (C3)
    → Suppress ≠ delete. Suppress = block output route.


  4 TỔ HỢP D1 × D2 (PFC-Operations §3):

    ① Hold only → compile new (easiest path)
    ② Hold + Suppress → override old + build new (double cost)
    ③ Suppress only → block only, no replacement (ALWAYS fails — Wegner 1987)
    ④ Neither → compiled auto-fire (PFC not involved)


  ĐẶC BIỆT: Modulator D = ONLY MODULATOR CÓ COST:
    Modulator B (Entity-Valence): cost ≈ 0 (compiled, automatic)
    Modulator D (PFC Hold/Suppress): cost ① + ② (active, fatigable)
    → PFC budget = finite → Modulator D = TEMPORARY
    → Mục tiêu: D1 Hold → compile → release (transfer to automatic)
    → = Tại sao Expertise Compile = CHẬM NHẤT (PFC sustained cost × years)


  🟢 PFC Hold: Baddeley 2003, Miller & Cohen 2001, Curtis & D'Esposito 2003
  🟢 PFC Suppress: Anderson & Green 2001, Aron 2007
  🟢 Suppress always fails alone: Wegner 1987
  🟡 Hold/Suppress as modulator D in compile architecture: framework synthesis
```

### §5.1 — Modulator D × Modulator B interaction

```
🟡 PFC × ENTITY-VALENCE INTERACTION:

  CÓ THỂ CỘNG TÁC:
    Entity-Valence positive (B amplify) + PFC Hold (D1 amplify)
    = COMPOUND amplification → compile rate CỰC CAO
    VD: Thích toán (B+) + chăm chỉ practice (D1)
        → Expert mathematician trajectory

  CÓ THỂ CẠNH TRANH:
    Entity-Valence negative (B suppress) + PFC Hold (D1 amplify)
    = B pull down, D1 push up → NET effect depends on strength
    VD: Ghét giáo viên (B−) + PFC ép "phải nghe" (D1)
        → Compile CHẬM, cost CAO (PFC fight Entity-Valence)
        → = "Muốn con hay chữ thì yêu lấy thầy" (Vietnamese proverb)
        → Solution: make Entity-Valence positive (B+) → D1 freed → easy

  KHI B OVERRIDE D:
    Entity-Valence CỰC mạnh → PFC KHÔNG thể override
    VD: Phải nghe người mình GHÉT DEEPLY → PFC Hold FAILS
        → Entity-Valence (compiled, subcortical) > PFC (deliberate, cortical)
    = Entity-Access excess territory (Mức 5 negative)

  KHI D RESHAPE B (slowly):
    PFC tạo exposure mới (C2 imagination, C1 new environment)
    → New exposure → Engine A → GRADUALLY update Entity-Valence
    = PFC → Entity-Valence: INDIRECT (via exposure, slow)
    = Therapy mechanism: PFC direct new exposure → recompile Entity-Valence


  ⭐ ASYMMETRY:
    B → D: DIRECT, fast, can override (subcortical → cortical)
    D → B: INDIRECT, slow, via exposure (cortical → exposure → subcortical)
    = Chi tiết: §7 (Feedback Loops)


  🟡 B×D interaction model: framework synthesis
  🟢 Subcortical override cortical: LeDoux 1996
  🟢 Therapy = gradual recompilation: established CBT/exposure therapy
```

---

## §6 — MULTI-STREAM COMPILE: Đồng Thời Nhiều Stream

```
⭐⭐ MỌI TÌNH HUỐNG = NHIỀU COMPILE STREAMS CHẠY ĐỒNG THỜI:

  Khi 1 event xảy ra, Engine A KHÔNG chạy 1 compile duy nhất.
  NHIỀU patterns được expose → NHIỀU Hebbian processes → ĐỒNG THỜI.


  4 COMPILE STREAMS CHÍNH:

  ┌─────────────────────────────────────────────────────────┐
  │ STREAM        │ WHAT COMPILES       │ MODULATOR DOMINANT │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ① CONTENT     │ Nội dung, kiến thức │ Engine A only       │
  │               │ Facts, skills       │ (Experience type)   │
  │               │ Procedures, data    │ Minimal B/D         │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ② VALUE       │ Đánh giá tốt/xấu   │ B (Entity-Valence)  │
  │               │ Approach/avoid tag  │ + A                 │
  │               │ "Cái này có tốt?"   │ Trust-amplified     │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ③ ENTITY      │ Entity-Valence      │ B (update weights)  │
  │               │ Trust update        │ + A                 │
  │               │ "Người này đáng     │ Per-entity compile  │
  │               │  tin đến mức nào?"  │                     │
  ├───────────────┼─────────────────────┼────────────────────┤
  │ ④ BEHAVIOR    │ Approach/avoidance  │ Direction-At-Compile│
  │               │ Motor-association   │ (Chunk §2.4)        │
  │               │ Habit formation     │ Valence direction   │
  └───────────────┴─────────────────────┴────────────────────┘


  VÍ DỤ 1 — TRẺ BỊ MẸ ÉP HỌC TOÁN:

    ① Content: [2+2=4], [phép nhân], [công thức]
       → Engine A qua C1 (ngồi đọc sách)
       → Modulator B: KHÔNG ảnh hưởng (content = direct exposure)
       → Compile type: Experience (direct)

    ② Value: [học = sợ bị mắng → tránh bị mắng → "phải làm"]
       → Engine A + context: threat direction
       → Modulator B: trust mẹ nhưng value = avoidance
       → Compile type: Experience (threat avoidance pathway ④)

    ③ Entity: [mẹ + ép] → Entity-Valence update
       → [mẹ] structural valence: mixed (yêu thương + ép buộc)
       → [học] valence: negative association (ép)
       → Compile type: Entity-Valence update (Engine A + Modulator B)

    ④ Behavior: [nghe mẹ → ngồi xuống → mở sách]
       → Motor-association compile: avoidance-driven habit
       → PFC KHÔNG cần (automatic compliance after repetition)


  VÍ DỤ 2 — SINH VIÊN THÍCH GIÁO SƯ, THÍCH MÔN HỌC:

    ① Content: [lý thuyết], [phương pháp], [thuật ngữ]
       → Engine A qua C1 (nghe giảng) + C2 (suy nghĩ bài tập)
       → Compile type: Experience + Expertise (PFC-directed)

    ② Value: [môn này = thú vị → approach]
       → Engine A + Modulator B (Entity-Valence positive cho GS)
       → Trust amplify: GS nói "phần này quan trọng" → body amplify
       → Compile type: Trust (B-dominant)

    ③ Entity: [giáo sư] → Entity-Valence STRENGTHEN positive
       → Trust tăng → future value amplification TĂNG
       → Virtuous loop: trust → amplify → positive experience → trust ↑

    ④ Behavior: [đến lớp đúng giờ → ngồi hàng đầu → hỏi câu hỏi]
       → Approach-driven habit compile
       → PFC minimal (automatic after few weeks)


  ⭐ KEY INSIGHT:

  Content stream LUÔN = Experience Compile (Engine A, direct exposure).
  Value stream = Trust-modulated (B amplify/suppress).
  Entity stream = Entity-Valence compile (update relationship weights).
  Behavior stream = Direction-At-Compile (approach/avoidance motor).

  → "Trust Compile" trong Compile-Taxonomy
     = chủ yếu VALUE stream (B-dominant), KHÔNG phải content.
  → Content VẪN compile qua Experience (Engine A alone).
  → = Tại sao trẻ bị ép học VẪN HỌC ĐƯỢC: content = Engine A.


  🟡 4-stream multi-stream model: framework synthesis (session 2026-06-01)
  🟡 Content always Experience: framework insight
  🟢 Hebbian concurrent: multiple patterns can strengthen simultaneously
  🟢 Direction-At-Compile: Chunk.md §2.4
```

---

## §7 — FEEDBACK LOOPS: Tương Tác Giữa Components

```
⭐⭐ CÁC COMPONENTS KHÔNG ĐỘC LẬP — CHÚNG TƯƠNG TÁC 2 CHIỀU:

  ┌─────────┐     ┌─────────────────┐     ┌──────────┐
  │  PFC    │ ←── │  ENGINE A       │ ──→ │  OUTPUT  │
  │ (Mod D) │     │  (Exposure →    │     │ (Compiled │
  │         │ ──→ │   Hebbian)      │     │  Chunks) │
  └────┬────┘     └───────┬─────────┘     └──────────┘
       │                  │
       │    ┌─────────────┴──────────┐
       │    │                        │
       ▼    ▼                        │
  ┌─────────────────┐    ┌──────────┴────────┐
  │  ENTITY-VALENCE │ ←→ │  SOURCES (C1+C2+C3)│
  │  (Mod B)        │    │                    │
  └─────────────────┘    └────────────────────┘
```

### §7.1 — PFC → Entity-Valence: INDIRECT (slow)

```
🟡 PFC KHÔNG THỂ TRỰC TIẾP THAY ĐỔI ENTITY-VALENCE:

  PFC không có đường dây trực tiếp xuống Entity-Compiled.
  PFC chỉ CÓ THỂ:

  ① Tạo exposure MỚI (C2 imagination hoặc C1 new environment):
     PFC imagine tình huống mới với entity
     → Body react → Engine A → Entity-Valence UPDATE
     → NHƯNG: cần NHIỀU exposure → CHẬM

  ② Hold new frame (reframe):
     PFC hold "nhìn nhận khác" → sustained exposure to new interpretation
     → Nếu lặp ĐỦ → Engine A compile new frame → Entity-Valence shift
     → = Therapy: CBT reframe = PFC create new C2 exposure

  ③ Change environment:
     PFC decide "gặp người này trong context mới"
     → C1 exposure mới → Engine A → Entity-Valence update


  TẤT CẢ 3 = INDIRECT: PFC → create exposure → Engine A → Entity-Valence.
  = CHẬM (weeks to months).
  = Tại sao therapy takes time.
  = Tại sao "biết người này tốt mà vẫn không thích" = Entity-Valence chưa update.


  🟢 CBT mechanism = exposure + reframe: Beck 1979
  🟢 Exposure therapy = gradual Entity-Valence update: Foa & Kozak 1986
  🟡 PFC → Entity-Valence = indirect: framework synthesis
```

### §7.2 — Entity-Valence → PFC: DIRECT (fast, can override)

```
🟡 ENTITY-VALENCE TÁC ĐỘNG TRỰC TIẾP LÊN PFC:

  Entity-Valence bias exposure TRƯỚC KHI PFC nhận thông tin (§3.2).
  → PFC receive ALREADY-BIASED input.

  3 cơ chế DIRECT:

  ① Attention bias:
     Entity-Valence positive → automatically DIRECT attention towards entity
     Entity-Valence negative → automatically DIRECT attention AWAY
     → PFC nhận input đã bị biased
     → PFC "suy nghĩ" nhưng trên DỮ LIỆU ĐÃ FILTERED

  ② Emotional override:
     Entity-Valence CỰC mạnh → emotional response → PFC DISRUPTED
     → Amygdala hijack (Goleman 1996 — nhưng mechanism = LeDoux 1996)
     → PFC capacity GIẢM khi emotional arousal CAO
     → = Entity-Valence can SHUT DOWN Modulator D

  ③ Motivation direction:
     Entity-Valence → approach/avoid drive → PFC CAN override
     NHƯNG: override cost ② efference mismatch
     → Sustained override = PFC budget exhaust → Entity-Valence WIN


  ⭐ ASYMMETRY SUMMARY:

    ┌──────────────────────┬──────────────────────────────┐
    │ PFC → Entity-Valence │ Entity-Valence → PFC         │
    ├──────────────────────┼──────────────────────────────┤
    │ INDIRECT             │ DIRECT                       │
    │ Via exposure (slow)  │ Via attention bias (fast)     │
    │ Weeks to months      │ Milliseconds                 │
    │ Needs PFC budget     │ Cost ≈ 0 (automatic)         │
    │ CAN be overridden    │ CAN override PFC             │
    │ = Therapy mechanism  │ = "First impression" power   │
    └──────────────────────┴──────────────────────────────┘

  → Entity-Valence có "advantage" trong tương tác với PFC.
  → Evolution reason: subcortical response = survival (nhanh hơn = sống sót).
  → PFC override = "deliberate override" = costly nhưng possible.
  → = Tại sao education khó, cult dễ:
      Cult: Entity-Valence positive (charisma) → amplify everything → easy install.
      Education: Entity-Valence neutral/negative → PFC must PUSH → costly.


  🟢 Emotional Stroop effect: attention bias documented
  🟢 Amygdala speed > PFC: LeDoux 1996
  🟢 PFC capacity reduced under stress: Arnsten 2009
  🟡 B→D direct vs D→B indirect asymmetry: framework synthesis
```

### §7.3 — "Muốn con hay chữ thì yêu lấy thầy" = Virtuous Loop

```
⭐ VIETNAMESE PROVERB = PERFECT ILLUSTRATION:

  "Muốn con hay chữ thì yêu lấy thầy"
  (Muốn con giỏi thì phải tôn trọng/quý thầy)

  MECHANISM:

  Step 1: Bố mẹ tạo Entity-Valence positive cho [thầy]
    Bố mẹ nói tốt về thầy → trẻ observe → trust inherit
    → Modulator B: [thầy] trust = Mức 3-4

  Step 2: Entity-Valence amplify AUTO
    Thầy nói → Modulator B amplify → value install NHANH
    → [học = tốt] compile qua Trust (B-dominant)
    → PFC KHÔNG CẦN override (cost ≈ 0)

  Step 3: Experience confirm
    Học → hiểu → opioid (Goldilocks) → positive experience
    → Engine A (Experience) confirm value installed by Trust
    → COMPOUND: Trust + Experience cùng hướng → pattern CỰC BỀN

  Step 4: PFC freed
    Vì Modulator B auto-amplify → PFC không cần Hold
    → PFC budget available cho LEARNING (C2 imagination, problem solving)
    → = Expertise Compile trajectory enabled

  Step 5: Entity-Valence UPDATE (positive spiral)
    Positive learning experience + thầy associated
    → Entity-Valence [thầy] STRENGTHEN positive
    → Next interaction: amplify EVEN MORE → spiral

  = VIRTUOUS LOOP:
    B positive → A compile easy → experience positive
    → B strengthen → A compile easier → experience more positive → ...


  NGƯỢC LẠI: Phụ huynh chê bai giáo viên

  Step 1: Entity-Valence negative cho [thầy]
  Step 2: Modulator B SUPPRESS value từ thầy
  Step 3: PFC phải OVERRIDE (Hold: "phải nghe thầy") → cost ①
  Step 4: PFC EXHAUSTED → learning IMPAIRED
  Step 5: Negative experience → Entity-Valence [thầy] WORSE → vicious cycle

  → Proverb = intuitive understanding of Modulator B × PFC interaction.


  🟡 Proverb as virtuous loop illustration: framework synthesis
  🟢 Positive teacher-student relationship → learning: established educational research
  🟢 Emotional context affects learning: Immordino-Yang & Damasio 2007
```

### §7.4 — Entity-Valence → Exposure selection: attention bias

```
🟡 ENTITY-VALENCE TỰ ĐỘNG CHỌN LỌC EXPOSURE:

  Entity-Valence positive → body tự động HƯỚNG attention tới entity
  → TĂNG C1 exposure từ entity đó
  → Engine A compile MORE patterns từ entity đó
  → = "Thích ai thì nghe theo người đó" = AUTOMATIC, không PFC

  Entity-Valence negative → body tự động TRÁNH exposure từ entity
  → GIẢM C1 exposure từ entity đó
  → Engine A compile LESS patterns từ entity đó
  → = "Ghét ai thì không muốn nghe" = AUTOMATIC, không PFC

  → MODULATOR B CONTROLS SOURCE SELECTION:
    Không chỉ amplify/suppress compile rate
    MÀ CÒN chọn lọc NGUỒN exposure (C1 nào được ưu tiên)

  → Feedback loop: B → chọn exposure → A compile → update B → ...

  = Tại sao "echo chamber" = self-reinforcing:
    B positive cho group A → attend to A → compile A's views
    → A's views compiled → B positive strengthen → attend MORE to A
    → Views from outside group B = low trust → low exposure → NOT compiled


  🟢 Confirmation bias: Nickerson 1998
  🟢 In-group favoritism: Tajfel 1979
  🟡 Entity-Valence → exposure selection loop: framework synthesis
```

---

## §8 — 3 COMPILE TYPES = MODULATOR CONFIGURATIONS

```
⭐⭐ REFRAME: 3 Types = 3 dominant modulator configurations CỦA CÙNG 1 ENGINE:


  ┌────────────────┬─────────┬──────────┬──────────┬──────────┐
  │ COMPILE TYPE   │ ENGINE  │ MOD B    │ SOURCES  │ MOD D    │
  │                │    A    │ (Entity- │ (C1/C2/  │ (PFC)    │
  │                │         │ Valence) │ C3)      │          │
  ├────────────────┼─────────┼──────────┼──────────┼──────────┤
  │ EXPERIENCE     │ ✅ Full  │ Minimal  │ C1       │ Minimal  │
  │ (~90%)         │         │ (direct  │ dominant │ (body    │
  │                │         │ verify)  │          │ direct)  │
  ├────────────────┼─────────┼──────────┼──────────┼──────────┤
  │ TRUST          │ ✅ Full  │ ⭐ HIGH  │ C1 from  │ Low      │
  │ (overlap)      │         │ (amplify │ trusted  │ (chọn    │
  │                │         │ value)   │ source   │ trust    │
  │                │         │          │          │ ai)      │
  ├────────────────┼─────────┼──────────┼──────────┼──────────┤
  │ EXPERTISE      │ ✅ Full  │ Low      │ C1+C2    │ ⭐ HIGH  │
  │ (~5%)          │         │ (self-   │ balanced │ (PFC     │
  │                │         │ verify)  │          │ direct   │
  │                │         │          │          │ years)   │
  └────────────────┴─────────┴──────────┴──────────┴──────────┘

  ENGINE A = LUÔN FULL. Không bao giờ khác.
  Sự khác biệt = MODULATOR nào DOMINANT.


  EXPERIENCE COMPILE = Engine A + minimal modulators:
    Direct exposure → Hebbian → compile.
    Entity-Valence: có thể tham gia nhưng KHÔNG dominant.
    PFC: KHÔNG cần (body direct).
    Sources: C1 dominant (body-input from reality).
    = "Thuần engine" — modulators ở mức background.

  TRUST COMPILE = Engine A + Modulator B dominant:
    Exposure từ trusted source → B amplify value install.
    Entity-Valence: DOMINANT (trust multiplier determines compile speed).
    PFC: chọn trust ai (nhưng không direct learning process).
    Sources: C1 từ trusted entity.
    = "Engine + auto-turbo from Entity-Valence."

  EXPERTISE COMPILE = Engine A + Modulator D dominant:
    PFC-directed exposure qua nhiều năm.
    Entity-Valence: low (self-verify via Domain-Checked).
    PFC: DOMINANT (direct attention, hold, imagine, domain-check).
    Sources: C1+C2 balanced (practice + imagination).
    = "Engine + manual turbo from PFC (costly, slow)."


  ⭐ 3 Types OVERLAP (Compile-Taxonomy §2.4 ⚠️):
    Không cộng thành 100% vì overlapping.
    VD: Trẻ học toán với giáo viên yêu thích
    = Experience (C1 direct) + Trust (B amplify GV) + Expertise (D1 Hold bài)
    = 3 types CÙNG LÚC, tỉ lệ khác nhau.


  TẠI SAO VẪN HỮU ÍCH GIỮ 3 LABELS:
    Dù mechanism = 1 engine, 3 labels vẫn USEFUL cho communication:
    - "Experience Compile" = nói nhanh: "engine dominant, direct"
    - "Trust Compile" = nói nhanh: "Entity-Valence dominant"
    - "Expertise Compile" = nói nhanh: "PFC dominant"
    = Labels cho DOMINANT CONFIG, không phải separate mechanisms.
    = Giống "đi bộ / chạy / leo núi" = useful labels dù cùng cơ mechanism.


  🟡 3 types as modulator configurations: framework synthesis (session 2026-06-01)
  🟡 Labels remain useful: framework convention
  🟢 Individual components established (see §2-§5 citations)
```

### §8.1 — 4 Compile Pathways cũng = modulator configs

```
🟡 4 PATHWAYS (Compile-Taxonomy §3) = ĐẶC THÙ hơn trong cùng framework:

  ① HARDWARE FIT = Experience (A + minimal B/D, C1, novelty direction)
  ② TRUST + MODERATE FIT = Trust+Experience (A + B + partial D, C1)
  ③ SOCIAL DEFAULT = Trust (A + B social proof, C1, minimal D)
  ④ THREAT AVOIDANCE = Experience (A + minimal B, C1, threat direction)

  4 pathways = 4 CONCRETE configurations khác nhau.
  Cùng engine. Khác dominants. Khác direction (approach vs avoidance).

  → Taxonomy KHÔNG thay đổi. Chỉ thay đổi GIẢI THÍCH:
    "4 pathways khác cơ chế" → "4 pathways = 4 configs của cùng 1 engine."
```

---

## §9 — EVOLUTIONARY GRADIENT: Modulators Qua Tiến Hóa

```
⭐ MODULATORS ĐƯỢC THÊM QUA TIẾN HÓA — ENGINE CONSERVED:


  ┌──────────────────────────────────────────────────────────────┐
  │ SPECIES          │ ENGINE │ MOD B    │ SOURCES  │ MOD D      │
  │                  │   A    │ (Entity- │          │ (PFC)      │
  │                  │        │ Valence) │          │            │
  ├──────────────────┼────────┼──────────┼──────────┼────────────┤
  │ Côn trùng        │ ✅ A   │  —       │ C1 only  │  —         │
  │ (insects)        │ (basic │          │          │            │
  │                  │ Hebbian│          │          │            │
  ├──────────────────┼────────┼──────────┼──────────┼────────────┤
  │ Cá, bò sát       │ ✅ A   │ Basic B  │ C1 only  │  —         │
  │ (fish, reptiles) │        │ (simple  │          │            │
  │                  │        │ friend/  │          │            │
  │                  │        │ foe)     │          │            │
  ├──────────────────┼────────┼──────────┼──────────┼────────────┤
  │ Chó, mèo, hổ    │ ✅ A   │ B basic  │ C1 + C3  │ Basic D    │
  │ (social mammals) │        │ (attach- │ basic    │ (inhibi-   │
  │                  │        │  ment)   │          │ tory)      │
  ├──────────────────┼────────┼──────────┼──────────┼────────────┤
  │ Linh trưởng      │ ✅ A   │ B        │ C1 + C3  │ D          │
  │ (primates)       │        │ (social  │          │ (planning, │
  │                  │        │ complex) │          │ inhibit)   │
  ├──────────────────┼────────┼──────────┼──────────┼────────────┤
  │ Con người        │ ✅ A   │ B full   │ C1+C2+C3 │ D full     │
  │ (humans)         │        │ (deep    │ (full    │ (Hold +    │
  │                  │        │ Entity-  │ imagina- │ Suppress + │
  │                  │        │ Compiled,│ tion +   │ 5 roles)   │
  │                  │        │ Mức 0-5) │ C3 rich) │            │
  │                  │        │          │ + Sleep S│            │
  └──────────────────┴────────┴──────────┴──────────┴────────────┘


  PATTERN:
    Engine A = CONSERVED từ côn trùng đến người.
    Neurons fire together wire together = UNIVERSAL.

    Modulators = THÊM DẦN theo evolutionary complexity:
      Insects: A only (pure Hebbian, stimulus-response)
      Fish/reptiles: + basic Entity recognition (friend/foe)
      Social mammals: + attachment system + basic C3 + basic inhibition
      Primates: + complex social hierarchy + social learning
      Humans: + FULL PFC (5 roles) + C2 imagination + rich C3 + deep Entity-Compiled

    MỖI BƯỚC = THÊM MODULATOR, KHÔNG thay đổi ENGINE.


  ⭐ IMPLICATIONS:

  ① Dog training = pure Engine A + minimal B:
     Repetition × reward → Hebbian → compiled behavior.
     Trust = basic (owner bond). PFC = minimal.
     → Dog "learns" = Engine A with C1 exposure.

  ② Human education = Engine A + B + C2 + D:
     CÙNG engine + THÊM 3 modulators.
     → PHỨC TẠP hơn nhưng POWERFUL hơn.
     → = Tại sao only humans build civilization:
       C2 (imagination) → abstract knowledge
       B full (deep Entity-Compiled) → cultural transmission at scale
       D full (PFC 5 roles) → Expertise Compile possible

  ③ "Con người = động vật có thêm modulators":
     Engine = GIỐNG. Modulators = KHÁC.
     = Body-Base.md §2: "3 Hardware Foundations → Compilable Architecture."
     = Compilable Architecture = Engine A + full modulator suite.


  🟢 Hebbian learning conserved across species: established neuroscience
  🟢 PFC evolution in primates → humans: Semendeferi et al. 2002
  🟢 Attachment system mammals: Bowlby 1969
  🟡 Modulator additive evolution model: framework synthesis
```

---

## §10 — EDGE CASES VERIFIED (8+)

```
⭐ 8 EDGE CASES ĐÃ KIỂM CHỨNG TRONG SESSION:


  ① TRAUMA (single exposure, emotional peak):

     Situation: bị chó cắn 1 lần → phobia
     Architecture: Engine A qua peak_valence (1 lần = compile ngay)
       Source: C1 (external body-input, multi-modal intense)
       Modulator B: Entity-Valence [chó → nguy hiểm] COMPILE NGAY
       Modulator D: PFC KHÔNG tham gia (too fast, subcortical)
     → ✅ Architecture explains: extreme exposure quality = rapid compile


  ② CULT (Entity-Valence override PFC):

     Situation: cult leader install beliefs qua trust
     Architecture:
       Engine A: exposure to cult content (C1: meetings + C3: community)
       Modulator B: Entity-Valence cho leader CỰC CAO (charisma + isolation)
       Modulator D: PFC SUPPRESSED (B override D — §7.2)
       → B amplify ALL content from leader → value install deep
     → ✅ Architecture explains: B override D = cult mechanism


  ③ THERAPY (PFC-guided recompile qua new exposure):

     Situation: CBT reframe trauma
     Architecture:
       Engine A: new exposure (C2: imagination + C1: controlled real exposure)
       Modulator D: PFC Hold new frame (reframe)
       Modulator B: Entity-Valence gradually UPDATE (indirect D → B)
       → New exposure → Engine A → new chunk compile → compete with old
       → Reconsolidation window (Nader 2000): recall → modify → re-compile
     → ✅ Architecture explains: therapy = PFC create new exposure → Engine A


  ④ TRẺ BỊ ÉP HỌC (multi-stream, forced exposure):

     Situation: mẹ ép học, trẻ không muốn
     Architecture (4 streams — §6):
       Content: Engine A + C1 → compile kiến thức (Experience)
       Value: Engine A + avoidance direction → [học = tránh bị mắng]
       Entity: Modulator B → [mẹ + học] mixed valence
       Behavior: Engine A → compliance habit (avoidance-driven)
     → ✅ Architecture explains: multi-stream, content VẪN compile


  ⑤ "BIẾT MÀ KHÔNG LÀM" (PFC compiled ≠ body compiled):

     Situation: biết nên tập thể dục, nhưng không làm
     Architecture:
       Trust value installed: [tập = tốt] (B amplify từ society/doctor)
       Experience compiled: [sáng → ngủ → thoải mái] (Engine A direct)
       Engine A products CẠNH TRANH: Experience > Trust (multi-modal > verbal)
       PFC can Hold "phải tập" (D1) nhưng cost ①
       → PFC exhaust → Experience pattern WIN
     → ✅ Architecture explains: 2 compiled patterns compete, Experience > Trust


  ⑥ IMMERSION LANGUAGE LEARNING (C1 dominant, B minimal):

     Situation: sống ở nước ngoài, tự học ngôn ngữ qua immersion
     Architecture:
       Engine A: massive C1 exposure (hear, speak, read, interact)
       Modulator B: minimal (no specific trusted teacher)
       Modulator D: moderate (PFC notice + hold new patterns)
       Source: C1 dominant (external environment)
     → Compile = slow but DEEP (multi-modal + repetition)
     → ✅ Architecture explains: pure Engine A + C1 = immersion learning


  ⑦ EXPERT BLIND SPOT (D-compiled mạnh, B weak cho novice):

     Situation: expert giải thích cho novice, novice không hiểu
     Architecture:
       Expert: decades D-compiled → pyramidal compression → "thấy 4"
       Novice: chưa compiled → cần C1 + C2 exposure + time
       Modulator B cho novice: trust expert = possible
         NHƯNG: trust amplify VALUE, không amplify CONTENT
         Content vẫn cần Engine A + exposure + repetition
     → ✅ Architecture explains: trust ≠ understanding (§3.3)


  ⑧ "YÊU LẤY THẦY" (PFC → Entity-Valence virtuous loop):

     Situation: bố mẹ nói tốt về thầy → trẻ học tốt hơn
     Architecture (§7.3 full analysis):
       Modulator B: [thầy] positive → amplify value → compile [học = tốt]
       Experience confirm → B strengthen → PFC freed → Expertise possible
       = Virtuous loop: B+ → A easy → experience+ → B++ → ...
     → ✅ Architecture explains: proverb = B→A→B feedback loop


  ⭐ 8/8 EDGE CASES ĐỀU GIẢI THÍCH ĐƯỢC QUA ARCHITECTURE.
  Không có case nào CẦN "cơ chế compile riêng" ngoài Engine A.
  Modulators + Sources đủ giải thích MỌI variation.
```

---

## §11 — OPEN QUESTIONS

```
🔴 CÁC CÂU HỎI CHƯA CÓ ĐÁP ÁN:


  Q1: HEBBIAN RATE CÓ UNIFORM KHÔNG?

     Engine A (Hebbian) hoạt động GIỐNG NHAU ở mọi brain regions?
     Hay LTP rate KHÁC NHAU giữa cortical regions?
     Evidence gợi ý: hippocampal LTP ≠ cortical LTP (speed, stability)
     → Nếu KHÁC → Engine A có "regional variants"?
     → Ảnh hưởng gì tới compile architecture?

     🟢 LTP regional differences: established (hippocampal vs cortical)
     🔴 Implication cho compile architecture: chưa phân tích


  Q2: ENTITY-VALENCE AMPLIFICATION: LINEAR HAY THRESHOLD?

     Trust multiplier (Mức 0-5) tác động tuyến tính hay có threshold?
     Có thể: Mức 0→1 = jump lớn, Mức 1→2 = nhỏ hơn (logarithmic)?
     Hoặc: Mức 3→4 = jump lớn (attachment threshold)?
     → Entity-Access.md §2 chưa specify curve shape.

     🔴 Amplification curve shape: cần research


  Q3: C3 (SPONTANEOUS CHUNK FIRE) CÓ THỂ PFC-INFLUENCED KHÔNG?

     C3 = automatic. NHƯNG:
     PFC CÓ THỂ gián tiếp influence C3?
     VD: Meditation training → change C3 patterns?
     VD: Therapy → reduce intrusive C3?
     → Nếu CÓ: ranh giới C2/C3 KHÔNG hoàn toàn rõ ràng.

     🟡 Meditation changes DMN: Brewer et al. 2011
     🔴 C2/C3 boundary: cần clarify


  Q4: MULTI-STREAM COMPILE — CÁC STREAM CẠNH TRANH HAY CỘNG TÁC?

     4 streams (Content, Value, Entity, Behavior) chạy đồng thời.
     Chúng share neural resources? Hay independent?
     Nếu share: compile 1 stream → GIẢM resource cho stream khác?
     Nếu independent: tại sao overwhelm xảy ra?

     🔴 Stream resource competition: chưa phân tích kỹ


  Q5: SLEEP Ở ĐÂU TRONG ARCHITECTURE?

     Sleep = offline maintenance system ĐỘC LẬP (Component S).
     Nhưng tương tác với Engine A + Modulators:
       Replay = thêm C3 exposure → Engine A
       SHY = prune weak connections → modify compiled chunks
       Emotional decoupling → modify Modulator B values?
     → Chi tiết: Drill-Compile-Sleep.md (session riêng)

     🟡 Sleep as Component S: framework synthesis
     🟢 Sleep mechanisms: established (see Learning-Cycle.md §4)


  Q6: EVOLUTIONARY GRADIENT — CÓ INTERMEDIATE SPECIES NÀO PHẢN BÁC?

     Model §9 = simplified. Có species nào KHÔNG fit?
     VD: Octopus = distributed nervous system → Hebbian khác?
     VD: Corvids = tool use → C2-like without human PFC?
     → Cần review cross-species evidence.

     🔴 Cross-species verification: pending


  Q7: COMPILE_RATE FORMULA — EXPOSURE CÓ PHẢI LÀ MULTIPLICATIVE?

     Formula hiện tại: f(exposure × saliency × ...)
     → Nếu multiplicative: exposure = 0 → tất cả = 0 (✅ consistent)
     → Nhưng: có thể additive ở SOME parameters?
     → VD: peak_valence cực cao + exposure = 1 → compile ngay (trauma)
     → = peak_valence "bù" cho low repetition?

     🟡 Formula mathematical form: chưa xác nhận
     🟢 Emotional peak = rapid compile: McGaugh 2004
```

---

## §12 — IMPLICATIONS CHO FRAMEWORK

```
🟡 NẾU ARCHITECTURE NÀY ĐÚNG — IMPLICATIONS:


  ① COMPILE-TAXONOMY.md CẦN REWRITE:

     v2.0: "3 separate types" (taxonomy-first)
     → v3.0: "1 engine + modulator configurations" (mechanism-first)

     §1 (3 constraints): KEEP 100% — still valid.
     §2 (3 types): REWRITE → describe as modulator configs.
     §3 (4 pathways): KEEP + add modulator config description.
     §4 (5-step trust): REWRITE → trust = amplifier, not gate.
     §5 (PFC=Director): EXTEND → PFC as Modulator D.
     §6 (6 trade-offs): KEEP + minor refine.
     §7 (interactions): KEEP + add feedback loop details.
     NEW: Architecture overview, Multi-Stream, Evolutionary Gradient.
     NEW: Sleep Component S reference (→ Drill-Compile-Sleep.md).


  ② CHUNK.MD §2.3 TERMINOLOGY FIX:

     "TRUST = GATE CHO EXTERNAL INSTALL" (line 288)
     → "TRUST = AMPLIFIER (GRADIENT) CHO COMPILE RATE"
     → Consistent with Entity-Access Mức 0-5.
     → Gate = limit case of amplifier when multiplier → 0.


  ③ COMPILE-TAXONOMY §2.3: "GATE" → REFRAME:

     "Trust = gate cho toàn bộ quá trình" (line 329)
     → Trust = gradient multiplier (amplifier) cho VALUE install.
     → Content compile = Engine A alone (KHÔNG cần trust).


  ④ BODY-BASE.MD: COMPILABLE ARCHITECTURE = ENGINE + MODULATORS:

     Body-Base §2: "3 Hardware Foundations → Compilable Architecture"
     → Compilable Architecture = Engine A (Hebbian)
                                + Modulator B (Entity-Valence)
                                + Sources (C1+C2+C3)
                                + Modulator D (PFC)
     → Could add architecture summary in Body-Base.md.


  ⑤ NEW CONCEPT: MULTI-STREAM COMPILE:

     Chưa có trong framework.
     4 streams (Content, Value, Entity, Behavior) compile đồng thời.
     → Could add to Compile-Taxonomy v3.0 or separate file.


  ⑥ TRUST SCOPE CLARIFICATION:

     Trust amplifies VALUE install, NOT content compile.
     → Clarify in Chunk.md §2.3 + Compile-Taxonomy.
     → Resolves "trẻ bị ép học vẫn compile" edge case.


  ⭐ PROPAGATION SEQUENCE (after drill complete):

    Phase 1: Drill-Compile-Sleep.md (complete sleep analysis)
    Phase 2: Compile-Taxonomy.md v3.0 REWRITE
    Phase 3: Chunk.md §2.3 terminology fix
    Phase 4: Body-Base.md minor update (architecture summary)
    Phase 5: Cross-ref updates (6+ files)
```

---

## §13 — CROSS-REFERENCES + CITATIONS

### §13.1 — Framework files referenced

```
CORE FILES:
  Chunk.md v2.3 §1.1 — NO SOURCE TAG → 1-engine evidence
  Chunk.md v2.3 §2.1 — 4 compile mechanisms
  Chunk.md v2.3 §2.2 — compile_rate 5-parameter formula
  Chunk.md v2.3 §2.3 — Trust gate (→ NEEDS "amplifier" reframe)
  Chunk.md v2.3 §2.4 — Direction-At-Compile
  Chunk.md v2.3 §2.5 — Reconsolidation + no deletion

  Compile-Taxonomy.md v2.0 — 3 Compile Types + 6 trade-offs (→ NEEDS v3.0 rewrite)

  PFC-Operations.md v1.3 §2.1 — HOLD = PFC Amplify
  PFC-Operations.md v1.3 §2.2 — SUPPRESS = PFC Inhibit
  PFC-Operations.md v1.3 §2.3 — Hold ≠ Suppress table
  PFC-Operations.md v1.3 §3 — 4 combinations

  Entity-Valence-Dynamics.md v1.1 §1 — Structural vs Current Valence
  Entity-Valence-Dynamics.md v1.1 §2 — Entity-Compiled: Body-Base Extension
  Entity-Access.md v1.2 §2 — Mức 0-5 gradient

  Body-Feedback-Mechanism.md v2.1 §1.2 — 2 genuine sources (Hardware + Chunk Dynamics)
  Body-Feedback-Mechanism.md v2.1 §1.3 — Cross-cutting: NOT sources

  Simulation-Engine.md v1.1 §0 — 1 Engine, 3 Components, 3 Axes
  Background-Pattern.md v2.0 §1 — accumulated pattern, continuous firing
  Why-Body-Knows.md v1.2 §0 — 2-tầng calibration
  Body-Base.md v3.3 §2 — 3 Hardware Foundations → Compilable Architecture
  Body-Coupling.md v3.0 — Coupling mechanism

  Valence-Propagation.md v4.1 §2 — Trust = valence meta-dimension
  Learning-Cycle.md §4 — 6 sleep mechanisms (→ Drill-Compile-Sleep.md)
```

### §13.2 — Research citations

```
ESTABLISHED (🟢):
  Hebb 1949 — Hebbian learning ("fire together wire together")
  Bliss & Lømo 1973 — LTP discovery
  Dudek & Bear 1992 — LTD discovery
  McGaugh 2004 — Emotional arousal enhances memory consolidation
  Cowan 2001 — Working memory ~4±1 limit
  LeDoux 1996 — Amygdala fast pathway
  Arnsten 2009 — PFC impaired under stress
  Miller & Cohen 2001 — PFC top-down attentional control
  Baddeley 2003 — Working memory model
  Curtis & D'Esposito 2003 — PFC sustained firing = WM
  Anderson & Green 2001 — Think/No-Think paradigm
  Aron 2007 — rIFG inhibitory control
  Wegner 1987 — Ironic process theory (suppress → rebound)
  Nader 2000 — Reconsolidation
  Foa & Kozak 1986 — Exposure therapy
  Beck 1979 — CBT
  Jeannerod 2001 — Motor imagery
  Driskell et al. 1994 — Mental rehearsal meta-analysis
  Johnson et al. 1993 — Source monitoring / reality monitoring
  Smallwood & Schooler 2006 — Mind wandering
  Raichle et al. 2001 — DMN
  Brewin et al. 2010 — Intrusive memories
  Hobson 2009 — Dreaming
  Brewer et al. 2011 — Meditation changes DMN
  Nickerson 1998 — Confirmation bias
  Tajfel 1979 — Social identity / in-group favoritism
  Immordino-Yang & Damasio 2007 — Emotion and learning
  Kolb 1984 — Experiential learning theory
  Bowlby 1969 — Attachment theory
  Semendeferi et al. 2002 — PFC evolution in primates
  Cialdini 1984 — Social proof
  Boyd & Richerson 1985 — Cultural transmission
  Brown & Kulik 1977 — Flashbulb memories
  Skinner 1953 — Reinforcement
  Nisbett & Wilson 1977 — Confabulation
  Clark & Chalmers 1998 — Extended mind thesis
  Chase & Simon 1973 — Expert chess patterns
  Haier 1992 — Neural efficiency
  Ericsson et al. 1993 — Deliberate practice
  Bandura 1977 — Social learning theory
  Lupien et al. 2009 — Cortisol + cognitive load


FRAMEWORK SYNTHESIS (🟡):
  "1 engine + 3 modulators" unification — session 2026-06-01
  Trust = amplifier (not gate) — session 2026-06-01
  3-source parallel model (C1/C2/C3) — session 2026-06-01
  Multi-stream compile (4 streams) — session 2026-06-01
  Feedback loop asymmetry (B→D direct, D→B indirect) — session 2026-06-01
  Evolutionary modulator gradient — session 2026-06-01
  Content always Experience / Value trust-modulated — session 2026-06-01
  3 Compile Types = modulator configurations — session 2026-06-01
  Gate = limit case of amplifier — session 2026-06-01
```

---

> **NEXT**: Drill-Compile-Sleep.md (sleep = Component S, 6 mechanisms, offline maintenance)
> **THEN**: Compile-Taxonomy.md v3.0 REWRITE
> **THEN**: Chunk.md §2.3 terminology fix + propagation
