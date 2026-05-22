---
title: Background Pattern — Accumulated Chunk Bias Invisible to PFC
version: 1.1
created: 2026-04-27
updated: 2026-05-15 (v1.1 — §2.4 Alzheimer clinical validation, §4.2 Glymphatic, Health Conditions Drill cross-refs)
status: v1.1 COMPLETE
scope: |
  NEW CONCEPT: Background Pattern = accumulated chunk-network pattern
  hình thành qua experience + sleep gist extraction qua THỜI GIAN DÀI.
  Link density cao tới mức THẤM VÀO mọi chunk mới.
  PFC KHÔNG THỂ observe trực tiếp (quá phân tán).
  BIAS mọi processing: SPM, body-feedback, chunk activation.
  Chunk-level mechanism UNDERNEATH Body Baseline State (Schema.md §8).
  Cùng mechanism cho trauma, expertise, culture, personality.
purpose: |
  Schema.md §4.1 define schema depth = f(repetitions × modalities × emotional weight).
  Nhưng depth CHỈ LÀ 1 CHIỀU. File này formalize CHIỀU THỨ 2: Link Density.
  2D model (Compile Depth × Link Density) giải thích:
  ① Tại sao chronic childhood trauma khó chữa hơn isolated trauma event
  ② Tại sao cultural patterns persistent dù mỗi chunk nhẹ
  ③ Tại sao expert "biết mà không nói được"
  ④ Tại sao "biết nhưng không cảm được"
  ⑤ Tại sao therapy cần years, không weeks
position: |
  Core-Deep-Dive/Body-Base/Chunk/ — cùng cấp Chunk.md, 09-Learning-Cycle.md.
  Background Pattern = chunk-level mechanism, KHÔNG phải observation parameter.
  Đặt trong Chunk/ vì: mechanism hoàn toàn về chunks (link density, activation,
  sleep consolidation). Cross-cuts F1/F3/F4 giống Learning-Cycle.md.
  REFERENCES Schema.md §4 (extends depth model) + §8 (explains body baseline).
  REFERENCES Anchor-Schema.md (BP constrains which anchors feel viable).
  Background Pattern = chunk mechanism UNDERNEATH body baseline state.
dependencies:
  - Schema.md v2.0 — schema = observation parameter, §4 depth, §8 body baseline
  - Chunk.md v2.0 — chunk substrate, §4 activation dynamics, §2 compile
  - Chunk-Activation-Dynamics.md (01b) — probability, re-linking, trigger surface
  - Chunk-Discovery-Lifecycle.md (01c) — convergence zone, 1A/1B, gist
  - Learning-Cycle.md (09) — 6+1 sleep mechanisms, gist extraction, SHY
  - Body-Feedback-Mechanism.md — Chunk-Shift/Miss/Gap, compound
  - Self-Pattern-Match.md v2.1 — F1/F2, context-dependent chunk selection
  - Cortisol-Baseline.md v2.0 — amplifier, PFC damage, self-reinforcing
  - Anchor-Schema.md v1.2 — sync point, trust, 4 nguồn fill
  - Valence-Propagation.md v1.2 — per-entity valence, chain propagation
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Background Pattern — Accumulated Chunk Bias Invisible to PFC

> **Bạn lớn lên trong nhà bố mẹ strict 15 năm.**
> **Không có 1 event nặng nào. Không có trauma kiểu bị chó cắn.**
> **Nhưng 15 năm × hàng nghìn micro-events = MỌI chunk bạn compile**
> **đều có link NGẦM tới pattern [effort → not enough].**
>
> **30 tuổi: thành công, lương cao, mọi người khen.**
> **PFC: "tôi biết mình ok." Body: "chưa đủ."**
> **"Biết nhưng không cảm được" = PFC updated, Background Pattern CHƯA.**
>
> **Cùng cơ chế tạo:**
> **— Trauma: [effort → not enough] (threat direction)**
> **— Expertise: [code pattern → sẽ bug] (novelty direction)**
> **— Culture: [nói thẳng → gây phiền] (shared context)**
> **— Personality: "tôi là người X" (PFC label cho Background Pattern)**
>
> **File này: Background Pattern LÀ GÌ, HOW hình thành,**
> **TẠI SAO PFC không thấy, TẠI SAO khó thay đổi,**
> **và HOW resolution thực sự hoạt động.**

---

## Mục lục

- §0 — TẠI SAO CẦN CONCEPT MỚI
- §1 — DEFINITION
- §2 — 2D MODEL: COMPILE DEPTH × LINK DENSITY
- §3 — FORMATION MECHANISM
- §4 — SLEEP = ACCELERATOR, NOT SOLVER
- §5 — TẠI SAO PFC KHÔNG THỂ OBSERVE
- §6 — BACKGROUND PATTERN × SPM
- §7 — BACKGROUND PATTERN × BODY-FEEDBACK
- §8 — BACKGROUND PATTERN × CORTISOL (Self-Reinforcing Loop)
- §9 — EXAMPLES
- §10 — RESOLUTION PATHWAYS (incl. §10.4 BP Conflict — Invisible Conflict)
- §11 — RELATIONSHIP WITH EXISTING CONCEPTS
- §12 — OPEN QUESTIONS
- §13 — HONEST ASSESSMENT
- §14 — CROSS-REFERENCES

---

## §0 — TẠI SAO CẦN CONCEPT MỚI

```
FRAMEWORK HIỆN TẠI ĐÃ CÓ:

  Schema.md §4.1 — Depth Gradient:
    DEPTH = f(số lần lặp × số modality × emotional weight)
    → Nông / Giữa / Sâu
    → 1D model: depth CHỈ LÀ 1 CHIỀU

  Chunk-Activation-Dynamics.md §4 — Trigger Surface:
    → Trigger surface = total entry points có thể activate chunk
    → f(modalities, connections, emotional intensity, generality)
    → Trauma = large trigger surface + threat direction

  Schema.md §8 — Body Baseline State:
    → Cortisol baseline, opioid tone, muscle tension,...
    → "Khi không có gì xảy ra, cơ thể TÔI feel thế nào?"
    → NHƯNG: tại sao body baseline LÀ NHƯ VẬY? → CHƯA GIẢI THÍCH


FRAMEWORK CHƯA CÓ:

  ❌ CHIỀU THỨ 2: Link Density
     → Pattern tồn tại ĐỦ LÂU → chunks MỚI link vào → pattern PHÂN TÁN
     → KHÁC compile depth: không phải mạnh per-chunk, mà RỘNG across chunks
     → Trigger surface §4 nói size TẠI THỜI ĐIỂM compile
     → Chưa formalize: trigger surface TĂNG TRƯỞNG QUA THỜI GIAN

  ❌ GIẢI THÍCH TẠI SAO body baseline:
     → Body baseline = PHYSICAL REFLECTION của chunk-level pattern
     → Cortisol baseline CAO vì pattern [threat] chạy nền → cortisol sustained
     → Chunk-level mechanism UNDERNEATH body baseline → CHƯA CÓ FILE

  ❌ PHÂN BIỆT 2 KIỂU "SÂU":
     → Bị chó cắn: compile depth CAO, link density THẤP → manageable
     → Bị mẹ mắng 10 năm: compile depth VỪA, link density CỰC CAO → cực khó
     → 1D model KHÔNG phân biệt được 2 cases này

  ❌ TẠI SAO sleep KHÔNG giải quyết chronic patterns:
     → SHY prune weak links → NHƯNG chronic pattern links SURVIVE (daily reinforced)
     → Gist extraction ABSTRACT pattern → pattern CÒN TỔNG QUÁT HƠN
     → Sleep = accelerator cho pattern, NOT solver
```

---

## §1 — DEFINITION

### §1.1 — Background Pattern là gì

```
⭐ BACKGROUND PATTERN = ACCUMULATED CHUNK-NETWORK PATTERN:

  Hình thành qua:
    → Experience lặp lại trong CÙNG CONTEXT qua THỜI GIAN DÀI
    → Sleep gist extraction abstract hóa qua hàng nghìn đêm
    → Active consolidation transfer từ hippocampus sang neocortex
    → Link density tăng dần khi chunks MỚI link vào pattern

  Đặc điểm:
    ① PHÂN TÁN: không có 1 chunk trung tâm, không có boundary rõ
    ② INVISIBLE TO PFC: quá rộng để PFC observe như 1 đơn vị
    ③ BIAS MỌI THỨ: mọi chunk mới fire đều có xác suất link tới pattern
    ④ NEOCORTEX-EMBEDDED: đã transfer sâu, không còn hippocampal-dependent
    ⑤ KHÔNG PHẢI META-CHUNK: không fire as one — mà INFLUENCE tất cả
    ⑥ KHÔNG PHẢI SCHEMA: schema = named, bounded, PFC observable
       Background Pattern = unnamed, unbounded, PFC invisible

  = "Trọng lực" của chunk system:
    → Không thấy trọng lực trực tiếp
    → Chỉ thấy HIỆU ỨNG của nó trên mọi vật
    → Background Pattern = chunk-level "trọng lực"
      mà mọi processing chịu ảnh hưởng
```

### §1.2 — Phân biệt với các concept đã có

```
┌─────────────────────┬─────────────────────────────────────────────┐
│ Concept             │ Khác Background Pattern thế nào             │
├─────────────────────┼─────────────────────────────────────────────┤
│ Chunk               │ Chunk = atom. BP = emergent property        │
│                     │ từ NHIỀU atoms linked over time             │
├─────────────────────┼─────────────────────────────────────────────┤
│ Meta-chunk          │ Meta-chunk: fire AS ONE (compact, PFC sees) │
│                     │ BP: KHÔNG fire as one (distributed, PFC     │
│                     │ cannot see)                                 │
├─────────────────────┼─────────────────────────────────────────────┤
│ Schema              │ Schema: named, bounded, PFC observable      │
│                     │ BP: unnamed, unbounded, PFC invisible       │
│                     │ Schema = tên gọi pattern. BP = pattern      │
│                     │ quá phân tán để đặt tên chính xác          │
├─────────────────────┼─────────────────────────────────────────────┤
│ Anchor-Schema       │ Anchor: ACTIVE sync point (vô thức CHỌN)   │
│                     │ BP: PASSIVE background (tồn tại liên tục)  │
│                     │ Anchor = nhạc trưởng chọn bài              │
│                     │ BP = acoustic của phòng nhạc (luôn có,     │
│                     │ ảnh hưởng mọi bài, không ai chọn)          │
├─────────────────────┼─────────────────────────────────────────────┤
│ Trigger Surface     │ TS: size TẠI THỜI ĐIỂM compile             │
│ (01b §4)            │ BP: TS TĂNG TRƯỞNG qua thời gian           │
│                     │ TS = snapshot. BP = accumulated TS growth   │
├─────────────────────┼─────────────────────────────────────────────┤
│ Body Baseline State │ BBS (Schema.md §8): PHYSICAL layer          │
│                     │ BP: CHUNK-LEVEL mechanism underneath BBS    │
│                     │ BBS = cortisol cao. BP = TẠI SAO cortisol  │
│                     │ cao (pattern threat chạy nền)               │
├─────────────────────┼─────────────────────────────────────────────┤
│ Convergence Zone    │ CZ (01c §2.3): intersection of activation  │
│ (01c)               │ paths — pre-label, SPECIFIC location       │
│                     │ BP: ACCUMULATED background — no specific    │
│                     │ location, everywhere at once                │
├─────────────────────┼─────────────────────────────────────────────┤
│ 1A/1B Selection     │ 1A/1B: STRATEGY (test against what?)       │
│ Pressure (01c §4)   │ BP: SUBSTRATE (what biases the testing?)   │
│                     │ BP threat → bias toward 1B (avoid real-    │
│                     │ check vì dissonance intolerable)            │
└─────────────────────┴─────────────────────────────────────────────┘

⭐ TEST — "Bỏ concept Background Pattern → mất gì?"
  → Mất: giải thích tại sao 1D depth KHÔNG ĐỦ
  → Mất: mechanism underneath body baseline
  → Mất: phân biệt isolated trauma vs chronic pattern
  → Mất: tại sao sleep reinforces (không solves) chronic patterns
  → Mất: tại sao therapy cần years
  → = Background Pattern THÊM explanatory power mà framework CHƯA CÓ
```

---

## §2 — 2D MODEL: COMPILE DEPTH × LINK DENSITY

### §2.1 — Hai chiều độc lập

```
⭐ SCHEMA DEPTH CÓ 2 CHIỀU ĐỘC LẬP:

  CHIỀU 1 — COMPILE DEPTH (đã có, Schema.md §4.1):
    = Mỗi chunk wired MẠNH cỡ nào
    = f(emotional peak × multi-modal × repetition per-chunk)
    → Bị chó cắn: 1 event × emotional peak × multi-modal = HIGH depth
    → Học bài chán: nhiều lần × no emotion × single modal = LOW depth
    → = HOW STRONGLY each chunk is wired

  CHIỀU 2 — LINK DENSITY (concept mới):
    = Pattern linked với BAO NHIÊU chunks khác qua thời gian
    = f(duration × ongoing experience × context consistency × sleep cycles)
    → 10 năm sống cùng context: HIGH density (thousands of linked chunks)
    → 1 event isolated: LOW density (few linked chunks)
    → = HOW WIDELY the pattern is connected

  ĐỘC LẬP: có thể có bất kỳ combination nào:
    → High Depth + Low Density: bị chó cắn 1 lần
    → High Depth + High Density: childhood chronic abuse
    → Low Depth + Low Density: "trời mưa mang ô"
    → Low Depth + High Density: cultural "ngại gây phiền"
```

### §2.2 — 4 Quadrants

```
                    Link Density (thấm rộng)
                    LOW                        HIGH
                 ┌──────────────────┬──────────────────┐
    Compile      │                  │                  │
    Depth   HIGH │  ISOLATED EVENT  │  CHRONIC DEEP    │
    (sâu)        │                  │                  │
                 │  Bị chó cắn      │  Childhood abuse │
                 │  Tai nạn giao    │  + neglect 10yr  │
                 │  thông           │                  │
                 │                  │  Expert + trauma │
                 │  PFC CÓ THỂ see │  compound (war   │
                 │  → CAN label    │  veteran 5 years)│
                 │  → CAN target   │                  │
                 │  Reconsolidation │  PFC CANNOT see  │
                 │  CAN access     │  fully           │
                 │                  │  Reconsolidation │
                 │  Therapy: weeks  │  unclear         │
                 │  to months       │  Therapy: YEARS  │
                 │                  │                  │
                 │  = MANAGEABLE    │  = HARDEST       │
                 ├──────────────────┼──────────────────┤
            LOW  │                  │                  │
                 │  SURFACE RULE    │  BACKGROUND      │
                 │                  │  PATTERN         │
                 │  "Trời mưa       │  Cultural:       │
                 │   mang ô"        │  "ngại gây phiền"│
                 │  "Ctrl+S save"   │  Attachment:     │
                 │                  │  "không cần ai"  │
                 │  PFC sees easily │  Expert intuition│
                 │  Change: days    │  "implicit bias" │
                 │                  │                  │
                 │  = TRIVIAL       │  PFC CANNOT see  │
                 │                  │  fully           │
                 │                  │  Change: YEARS   │
                 │                  │  (new environment│
                 │                  │  + sustained)    │
                 │                  │                  │
                 │                  │  = INVISIBLE     │
                 │                  │  BUT PERVASIVE   │
                 └──────────────────┴──────────────────┘

⭐ KEY INSIGHT:
  → Quadrant dưới phải (Low Depth + High Density) gần như
    KHÔNG ĐƯỢC nhận diện trong mainstream psychology
  → Không phải "trauma" (không có event nặng)
  → Không phải "personality disorder" (không dysfunction rõ)
  → Chỉ là: "tôi vốn vậy" → = PFC label cho Background Pattern
  → Therapy truyền thống (target specific memories) KHÔNG effective
    cho quadrant này vì KHÔNG CÓ specific memory để target

🟡 2D model = framework synthesis — components established, integration novel
🟢 Each quadrant maps to known clinical categories
🔴 Exact boundary giữa quadrants = gradient, not discrete
```

### §2.3 — Có cần trục thứ 3?

```
🟡 TRỤC THỨ 3 TIỀM NĂNG — DIRECTION (Novelty vs Threat):

  Direction (Chunk.md §2.4 NT7) xác định VALENCE của pattern:
    → Novelty direction: pattern = expertise, positive intuition
    → Threat direction: pattern = trauma, avoidance, anxiety
    → Mixed: pattern có cả hai (cultural patterns = mixed)

  Direction KHÔNG PHẢI trục thứ 3 ĐỘC LẬP:
    → Direction attached TO mỗi chunk link (NT7 compile tag)
    → Mỗi link TRONG pattern có direction RIÊNG
    → Background Pattern TỔNG THỂ = weighted average of all link directions
    → → Direction = PROPERTY of pattern, NOT independent axis

  FRAMEWORK POSITION:
    → 2D model (Depth × Density) ĐỦ cho phân loại
    → Direction = thuộc tính BỔ SUNG, không phải trục phân loại
    → Nhưng direction QUYẾT ĐỊNH outcome:
      same Depth × Density + threat = chronic anxiety
      same Depth × Density + novelty = deep expertise
```

### §2.4 — Alzheimer clinical validation: "last in first out" (v1.1)

```
🟢 ALZHEIMER DATA VALIDATES 2D MODEL:

  Alzheimer-Analysis §5-§6, §17: Alzheimer phá chunk substrate → reveal pattern:
    → Chunks compile NÔNG mất TRƯỚC (recent, episodic)
    → Chunks compile SÂU kháng SAU CÙNG (childhood, procedural)
    → = "Last in first out" = Ribot's Law (1881) at mechanism level

  VALIDATE COMPILE DEPTH (§2.1 CHIỀU 1):
    → 5 overdetermined mechanisms predict cùng pattern (Chunk.md §5.4)
    → = Compile depth DIRECTLY PREDICTS resistance to substrate damage
    → = CLINICAL CONFIRMATION: depth ≠ just theoretical construct

  VALIDATE LINK DENSITY (§2.1 CHIỀU 2):
    → Cultural patterns (Low Depth + HIGH Density) = RESISTANT
      Music preservation: distributed multi-region → Alzheimer phá muộn
      Religious patterns: 6+ memory systems × high density → survive longest
    → Isolated memories (depth, LOW density) = VULNERABLE
    → = Link density INDEPENDENTLY predicts resistance (orthogonal to depth)

  "ARCHITECTURE DETERMINES PATTERN, NOT CAUSE" (Alzheimer §17.3):
    → Bất kỳ nguyên nhân nào (amyloid, tau, vascular, inflammation)
      → CÙNG pattern suy thoái: nông trước, sâu sau
    → Pattern = f(kiến trúc não), KHÔNG phải f(nguyên nhân cụ thể)
    → = "Dù lửa bắt đầu từ đâu, tòa nhà sụp từ tầng cao nhất."
    → Applied to 2D model: depth × density = architecture → predicts erosion

  ALZHEIMER = "KHẢO CỔ SỐNG" (Alzheimer §17.1):
    → Alzheimer strips recent overlay → reveals Background Pattern underneath
    → "Personality changes" ở Alzheimer = NOT personality changing, but BP EXPOSED
    → = Clinical data CONFIRMS: BP = neocortex-embedded, resistant

  🟢 Terry 1991: r=0.96 synapse loss × cognitive decline
  🟢 Reisberg 2002: retrogenesis = reverse developmental order
  🟢 Bartzokis 2004: myelination order predicts vulnerability
  🟡 2D model validation from Alzheimer data = framework synthesis
  → Chi tiết: Alzheimer-Analysis.md §5-§6, §17
```

---

## §3 — FORMATION MECHANISM

### §3.1 — Chỉ có 1 cơ chế: tích lũy tự nhiên

```
⭐ BACKGROUND PATTERN HÌNH THÀNH QUA 1 CƠ CHẾ DUY NHẤT:

  TÍCH LŨY TỰ NHIÊN + SLEEP GIST EXTRACTION:

    ① Experience trong CONTEXT → chunks compile
       (Chunk.md §2: 4 compile mechanisms)

    ② Mỗi chunk compile trong CONTEXT đang có background state
       → 01b §2.2 factor ⑤ CONTEXT MATCH: chunk link tới context
       → 01b §2.2 factor ⑥ EMOTIONAL STATE MATCH: chunk link tới body state
       → = Chunks MỚI TỰ ĐỘNG link tới pattern đang active ở background

    ③ Sleep: gist extraction abstract patterns từ specific events
       (Learning-Cycle §4.6: shared features STRENGTHEN, details FADE)
       → Sau 1 năm: GIST [effort → not enough] emerge from thousands of events
       → Detail MỜ: ai mắng, lúc nào, vì gì → QUÊN
       → Gist CÒN: [nỗ lực → không đủ] → MẠNH DẦN

    ④ Active consolidation TRANSFER pattern sang neocortex
       (Learning-Cycle §4.3: hippocampus → neocortex qua SWS)
       → Năm 1-2: hippocampus-dependent (có thể disrupt)
       → Năm 3-5: dần transfer
       → Năm 5+: neocortex-embedded = HẠ TẦNG

    ⑤ Chu trình tự cường hóa:
       → Pattern embedded → BIAS context cho chunks mới → chunks MỚI link vào
       → → Pattern CÒN MẠNH HƠN → bias CÒN MẠNH HƠN → ...
       → = Snowball effect


  PFC CÓ THỂ KHỞI ĐỘNG, NHƯNG KHÔNG PHẢI CƠ CHẾ RIÊNG:

    Imagine-Final + Luyện tập:
      → PFC tạo Imagine-Final → hold attention → direct experience
      → Chunks compile HƯỚNG VỀ Imagine-Final
      → Ban đầu: PFC hold tốn energy ("phải cố gắng")
      → Đủ chunks: spreading activation TỰ BIAS → PFC release
      → Pattern tự vận hành = BACK TO tích lũy tự nhiên (①→⑤)
      → = PFC SEED quá trình tự nhiên, không phải cơ chế khác
      → = "Lúc đầu cố gắng học, lúc sau tự nhiên thấy mọi thứ liên quan"

    TRANSITION POINT:
      → PFC hold → enough chunks → spreading activation tự bias
      → = Pattern ĐỦ link density → TỰ SUSTAIN không cần PFC
      → = Giống lăn tuyết: PFC push ban đầu, sau đó tuyết TỰ lăn
      → = Expert formation: 10 năm deliberate → intuition tự nhiên

  → = THỰC CHẤT CHỈ CÓ 1 CƠ CHẾ: tích lũy tự nhiên + sleep consolidation
  → = Imagine-Final/luyện tập = PFC ACCELERATE quá trình tự nhiên
  → = Không có Imagine-Final → phải ĐỢI experience tự tích lũy
  → = Có Imagine-Final → FILTER experience → accumulate NHANH HƠN
```

### §3.2 — Link Density growth over time

```
🟡 LINK DENSITY TĂNG TRƯỞNG CỤ THỂ:

  T=0 (event gốc): Pattern compile
    → Link density: LOW (few connected chunks)
    → Trigger surface: SMALL (limited entry points)

  T=1 year: Pattern vẫn active (context chưa đổi)
    → ~365 đêm gist extraction → abstract pattern emerge
    → Chunks mới compile trong year → nhiều có link ngầm
    → Link density: MODERATE (hundreds of connected chunks)
    → Trigger surface: GROWING

  T=5 years: Pattern embedded
    → Active consolidation → neocortex-embedded
    → Gist CỰC abstract (detail gốc đã fade)
    → Thousands of chunks compiled DURING pattern active → link ngầm
    → Link density: HIGH (thousands of connected chunks)
    → Trigger surface: LARGE (many entry points across domains)

  T=15 years: Background Pattern complete
    → Pattern = BACKGROUND (không còn foreground)
    → PFC không observe (đã habituate — VTA không fire cho baseline)
    → MẠNH bằng TỔNG HỢP link density, không phải per-chunk depth
    → Link density: VERY HIGH
    → Trigger surface: PERVASIVE

  ⭐ TĂNG TRƯỞNG = NOT LINEAR:
    → Ban đầu: chậm (ít chunks, ít links)
    → Giữa: accelerate (snowball — more links → more bias → more links)
    → Sau: plateau (saturation — hầu hết relevant chunks đã link)
    → = Sigmoid curve
```

---

## §4 — SLEEP = ACCELERATOR, NOT SOLVER

### §4.1 — 6 mechanisms × Background Pattern

```
⭐ SLEEP HOÀN THIỆN BACKGROUND PATTERN, KHÔNG GIẢI QUYẾT:

  MECHANISM 1 — SHY (Synaptic Homeostasis):
    🟢 Tononi & Cirelli 2003, 2014

    SHY = global downscale → prune weak, preserve strong.

    Cho ISOLATED event (bị chó cắn):
      → Trauma links STRONG (emotional peak) → survive SHY
      → NHƯNG: competing positive links CŨNG survive nếu reinforced
      → Qua nhiều đêm: emotional decoupling + competing links → MANAGEABLE

    Cho BACKGROUND PATTERN (chronic):
      → Pattern links reinforced DAILY (vì đang sống trong context đó)
      → SHY prune COMPETING links (random, unused) → pattern tương đối MẠNH HƠN
      → = SHY tạo RATCHET EFFECT: mỗi đêm, pattern tương đối mạnh thêm
      → 🟡 Pattern SURVIVE SHY + GET RELATIVELY STRONGER


  MECHANISM 5 — EMOTIONAL DECOUPLING (REM):
    🟢 Walker 2017, van der Helm 2011

    REM reduce emotional charge của memories.

    Cho ISOLATED event:
      → Emotional tag giảm qua mỗi đêm REM
      → Sau weeks-months: "nhớ nhưng không đau lắm" → ✓

    Cho BACKGROUND PATTERN:
      → REM reduce emotional tag tonight
      → Tomorrow: SAME CONTEXT → emotional tag RE-ADD
      → Emotional decoupling CANNOT KEEP UP với daily reinforcement
      → 🟡 Net effect: minimal reduction for active patterns


  MECHANISM 6 — GIST EXTRACTION:
    🟢 Payne 2009, Stickgold 2013, Tamminen 2010

    Sleep extract abstract patterns from specific events.

    ⭐ GIST EXTRACTION = CƠ CHẾ CHÍNH tạo Background Pattern:

    Thousands of specific events:
      → "Mắng vì điểm kém" (detail: lớp, test, điểm 7)
      → "Mắng vì chưa dọn nhà" (detail: bếp, chổi, 3h chiều)
      → "Mắng vì đi chơi về muộn" (detail: bạn, công viên, 8h)

    Mỗi đêm gist extraction:
      → Shared feature across ALL events: [effort → not enough → punished]
      → Unique detail FADE: ai, khi nào, context gì → MỜ DẦN
      → Gist STRENGTHEN: [effort → not enough] → CÒN MÃI

    Sau 10 năm × ~3,650 đêm:
      → Pattern ĐÃ abstract tới mức:
        ① KHÔNG CÒN gắn với context cụ thể (mẹ, nhà, trường)
        ② ĐÃ TRỞ THÀNH "rule tổng quát" trong vô thức
        ③ APPLY cho MỌI context mới (công việc, tình yêu, sáng tạo)
        ④ PFC KHÔNG THỂ trace back nguồn (detail đã fade)

    → 🟡 Gist extraction = cơ chế CHÍNH hình thành Background Pattern


  MECHANISM 3 — ACTIVE CONSOLIDATION:
    🟢 Born & Wilhelm 2012, Squire 1992

    Memory transfer: hippocampus → neocortex.

    → Năm 1-3: pattern hippocampus-dependent → reconsolidation CÓ THỂ access
    → Năm 3-5: DẦN transfer sang neocortex
    → Năm 5+: neocortex-embedded → reconsolidation unclear
    → = Pattern trở thành HẠ TẦNG — giống OS kernel

    → 🟡 Active consolidation EMBED pattern sâu hơn qua thời gian


  TỔNG HỢP — Sleep loop cho Background Pattern:

    Mỗi đêm:
      SHY: prune competitors → pattern tương đối mạnh hơn ✗ (cho resolution)
      Emotional decoupling: overwhelmed by daily re-add ✗
      Gist extraction: ABSTRACT pattern → MORE generalized ✗
      Active consolidation: EMBED deeper into neocortex ✗
      Replay: re-fire pattern-related sequences → STRENGTHEN ✗
      REM creative linking: NEW links form TO pattern ✗

    → 🟡 SLEEP HOÀN THIỆN Background Pattern, KHÔNG giải quyết nó
    → = Sleep = factory line producing + refining the pattern
    → = Resolution requires DIFFERENT mechanism (§10)
```

### §4.2 — Glymphatic: physical cleaning requires REAL sleep (v1.1)

```
🟢 SLEEP = CONSOLIDATION + PHYSICAL CLEANING (Alzheimer-Analysis §11):

  §4.1 nói sleep consolidation cho BP (gist extraction, SHY, replay).
  §4.2 thêm: sleep CŨNG dọn rác VẬT LÝ cho chunk SUBSTRATE.

  Xie 2013 (Science): glymphatic system = brain's cleaning crew
    → Sleep: interstitial space tăng ~60%
    → CSF flows qua perivascular channels, carries waste (amyloid, tau)
    → Clearance ~2× faster khi ngủ vs thức

  Hauglund et al. 2025 (Cell 188(3):606-622):
    → NE oscillations (~50s cycle) PUMP CSF qua brain
    → NE waves → blood vessel contraction → rhythmic CSF flow
    → = STRONGEST predictor of glymphatic clearance during NREM

  ⚠️ ZOLPIDEM WARNING:
    → Zolpidem suppress NE oscillations ~50% → glymphatic flow giảm >30%
    → = Thuốc ngủ CHO NGỦ nhưng KHÔNG DỌN RÁC
    → = "Mắt nhắm mà chổi không quét"
    → Sedation ≠ restorative sleep

  CONNECTS TO BACKGROUND PATTERN:
    → §4.1: sleep = accelerator cho BP FORMATION (consolidation, gist)
    → §4.2: sleep = protector cho BP SUBSTRATE (glymphatic cleaning)
    → Chronic mất ngủ → consolidation off + cleaning off
    → = BP formation CÓ THỂ continue (daily experience compile)
    → = NHƯNG substrate DAMAGE accumulates → chunks CÓ THỂ degrade
    → = Long-term: sleep protects INFRASTRUCTURE mà BP sits on

  🟢 Xie 2013, Hauglund 2025, Shokri-Kojori 2018 (1 đêm → 5% amyloid↑)
  🟡 Glymphatic × BP substrate protection = framework synthesis
```

---

## §5 — TẠI SAO PFC KHÔNG THỂ OBSERVE

```
🟡 5 LÝ DO PFC KHÔNG THỂ OBSERVE BACKGROUND PATTERN:

  ① HABITUATION — VTA không fire cho baseline:
     → VTA detect DELTA (thay đổi), KHÔNG detect CONSTANT
     → Background Pattern = constant → VTA habituate → PFC không nhận alert
     → Giống: không nghe tiếng quạt chạy cho tới khi quạt TẮT
     → 🟢 Habituation (Thompson & Spencer 1966)

  ② QUÁ PHÂN TÁN — không có boundary:
     → Schema: PFC observe chunk network CÓ BOUNDARY → label "schema X"
     → Background Pattern: KHÔNG CÓ boundary (link tới mọi thứ)
     → PFC không thể "chụp" toàn bộ → chỉ thấy HIỆU ỨNG cục bộ
     → Schema.md §6.1: PFC thấy output → suy ngược pattern → gọi "schema"
     → Background Pattern quá rộng → PFC không suy ngược nổi

  ③ GIST ĐÃ ABSTRACT — không còn detail:
     → Detail gốc (ai, khi nào, context gì) đã fade qua gist extraction
     → PFC recall cần detail → nhưng detail KHÔNG CÒN
     → = "Tôi biết có gì đó sai nhưng không nhớ vì sao"
     → = Somatic-Articulation-Loop: body biết trước PFC có từ

  ④ ĐƯỢC LABEL THÀNH "IDENTITY":
     → PFC observe pattern effects → label: "tôi là người cẩn thận"
     → Label THAY THẾ investigation: "vì tôi vốn vậy" = stop searching
     → = PFC label Background Pattern → ĐÓNG inquiry
     → = Self-referencing: 01c §4 1B (test against existing chunks)
     → = "Personality" = PFC label cho Background Pattern

  ⑤ COMPOUND — pattern fire CÙNG event khác:
     → Body-Feedback-Mechanism §4: nhiều dynamics fire đồng thời
     → Background Pattern fire CÙNG sensory input + other chunks
     → PFC nhận COMPOUND signal → attribute cho EVENT, không cho pattern
     → VD: sếp nhắc sửa slide → khóc → PFC: "sếp harsh"
     → Thật: sếp neutral + Background Pattern [not enough] compound → khóc
     → PFC misattribute vì không thấy Background Pattern layer
```

---

## §6 — BACKGROUND PATTERN × SPM

```
⭐ SPM (Self-Pattern-Match) DÙNG CHUNG CHUNK LIBRARY:

  SPM = solo forward simulation mechanism
  SPM fire 2 functions: F1 (body simulate) + F2 (logic predict)
  SPM dùng CHUNG chunk library → CHỊU BIAS từ Background Pattern

  VÍ DỤ — Attachment pattern [người khác = không đáng tin]:

    SPM fire cho NGƯỜI MỚI:
      F1 (Feeling): retrieve chunks "người" → ĐÃ BỊ BIAS
        → Body simulate: "người này sẽ disappoint"
        → Output: body ALERT nhẹ → DÙ người mới hoàn toàn tốt

      F2 (Logic): PFC chain predict
        → "Người này tốt → NHƯNG → rồi sẽ thay đổi"
        → "NHƯNG" = Background Pattern fire [anyone → will disappoint]
        → PFC KHÔNG biết "nhưng" đến từ đâu

    APPLY CHO MỌI AGENT:
      → Bạn bè: "cẩn thận, đừng tin quá"
      → Đồng nghiệp: "chắc có ý đồ"
      → Romantic partner: "rồi sẽ bỏ mình"
      → Therapist: "therapist này cũng sẽ judge mình"
      → = PERVASIVE — mọi relationship bị bias

  VÍ DỤ — Expert pattern [code structure → will bug]:

    SPM fire cho CODE MỚI:
      F1: body simulate running code → "cái gì đó sai"
      F2: PFC chain → "if concurrent here → race condition"
      → = Background Pattern (novelty direction) → ACCURATE intuition

  → SPM.md §4: context-dependent chunk selection
  → Background Pattern BIAS chunk selection cho MỌI context
  → = Không chỉ bias perception — bias CƠ CHẾ CHÍNH interact với agents
```

---

## §7 — BACKGROUND PATTERN × BODY-FEEDBACK

### §7.1 — Chunk-Miss liên tục

```
🟡 BACKGROUND PATTERN TẠO CHUNK-MISS BASELINE:

  Body-Feedback-Mechanism §3.2: Chunk-Miss = compiled baseline bị violate.

  Pattern [effort → not enough] compiled thành baseline:
    → Body expectation: "bất kỳ effort nào → sẽ không đủ"
    → = NEGATIVE PREDICTION wired as default

  Khi THÀNH CÔNG (objective):
    → Domain: "được khen, đạt KPI"
    → Normal: success > expected → positive delta → reward
    → NHƯNG: Background Pattern CŨNG fire: [chưa đủ]
    → Background Pattern: HIGH link density (thousands of supporting chunks)
    → New success: LOW link density (1 event, few chunks)
    → Background Pattern WIN → body vẫn [chưa đủ]
    → = Body-Feedback-Mechanism §3.2 variant ⓒ (vô thức)

  → = "Biết nhưng không cảm được" explained at mechanism level
```

### §7.2 — Compound amplification

```
🟡 BACKGROUND PATTERN = COMPOUND ENGINE:

  Body-Feedback-Mechanism §4: compound = nhiều dynamics cùng lúc.

  Event NHỎ (sếp nhắc sửa slide) + Background Pattern:

    Layer 1 — Sensory-Driven: nghe câu nói → chunks "feedback" fire
    Layer 2 — Chunk-Shift: [sếp] valence shift nhẹ (neutral → hơi threat)
    Layer 3 — Chunk-Miss: baseline [tôi làm đúng] bị violate
    Layer 4 — Background Pattern: [effort → not enough] fire CẢ MỘT MẠNG
    Layer 5 — SPM fire: F1 simulate "sếp nghĩ mình kém"

    → 5 layers compound → body-feedback CỰC LỚN so với event NHỎ
    → = Schema.md §5.4 "giọt nước tràn ly"
    → Background Pattern = lý do ly ĐÃ ĐẦY TỪ TRƯỚC

  Không có Background Pattern:
    → Layer 1 only → "ok, sửa" → 2 phút quên
```

---

## §8 — BACKGROUND PATTERN × CORTISOL (Self-Reinforcing Loop)

```
⭐ SELF-REINFORCING LOOP (threat-direction Background Pattern):

  ① Background Pattern (threat) chạy NỀN
     → Body interpret = "environment không an toàn" (dù thực tế an toàn)
     → HPA axis fire nhẹ → cortisol baseline ELEVATED
     → Cortisol-Baseline.md §7.7 Role ⑤ Silent Cortisol: sustained, PFC unaware

  ② Cortisol elevated → PFC LESS effective
     → Cortisol-Baseline.md §9: PFC damage timeline
     → PFC dendrite retraction → hold capacity GIẢM
     → LESS able to observe Background Pattern
     → LESS able to reality-check (1A → drift toward 1B)

  ③ PFC kém → chunks MỚI compile UNDER elevated cortisol
     → Chunk.md §2.4 NT7: threat-direction compile
     → Chunks mới CŨNG gắn threat association
     → = Chunks MỚI reinforce Background Pattern

  ④ Background Pattern MẠNH HƠN → cortisol baseline CÒN CAO HƠN
     → Back to ①

  = SELF-REINFORCING LOOP
  = Tại sao chronic ≠ acute:
    Acute: 1 event → cortisol spike → return → done
    Chronic: BP → sustained cortisol → PFC weakened → more threat compile → loop

  BREAK LOOP:
    → Phải intervene ở NHIỀU ĐIỂM CÙNG LÚC:
    ① Body: sleep + exercise + nutrition → lower cortisol physically
    ② Environment: new context → new chunks WITHOUT threat compile
    ③ PFC recovery: cortisol giảm → PFC recover → CÓ THỂ observe
    ④ Relationship: consistent safe agent → counter SPM bias
    → = COMBINATION intervention sustained qua MONTHS-YEARS
    → = Tại sao "chỉ suy nghĩ tích cực" KHÔNG đủ (verbal chunk only)
    → = Tại sao "chỉ tập thể dục" CŨNG KHÔNG đủ (body better, pattern unchanged)
    → Chi tiết: §10 Resolution Pathways
```

---

## §9 — EXAMPLES

### §9.1 — Chronic childhood stress (High Density + Moderate Depth)

```
  SETUP: Bố mẹ không bạo lực, không neglect — chỉ standards luôn cao hơn khả năng.
    → 8 điểm → "sao không 9?" Giúp nhà → "chưa đủ sạch."
    → Mỗi event: NHẸ. Không amygdala peak. Không trauma rõ.

  FORMATION:
    → Thousands of micro-events × 15 năm
    → Gist extract: [effort → not enough → punished]
    → Link density: CỰC CAO (mọi chunk school/home/self link tới)
    → Active consolidation: neocortex-embedded by age 10

  30 TUỔI:
    → Thành công, lương cao, được khen
    → PFC: "tôi biết mình ok"
    → Body: [chưa đủ] → cortisol nền → muscle tension → sleep disrupted
    → SPM cho mọi agent: "chắc họ cũng nghĩ mình chưa đủ tốt"

  TẠI SAO THERAPY KHÓ:
    → Không có "1 ký ức" để reconsolidate
    → Pattern = gist từ thousands of events → detail ĐÃ FADE
    → Neocortex-embedded → hippocampal-level intervention unclear
    → Phải BUILD background pattern mới qua years of new experience
```

### §9.2 — Cultural pattern (High Density + Low Depth)

```
  SETUP: "Người Nhật ngại gây phiền hà" (meiwaku)
    → Không ai DẠY cụ thể. Không 1 event nặng nào.
    → Millions of micro-interactions: mẹ xin lỗi thay, senpai handle giúp,
      TV shows model "sumimasen", neighbor giữ im lặng.

  FORMATION:
    → Mỗi interaction: 1 chunk NHẸ compile (low depth per chunk)
    → NHƯNG: shared context × 20 năm × xã hội reinforce
    → Gist extract: [hành động → có thể gây phiền → cẩn thận]
    → Link density: CỰC CAO (toàn bộ social chunks link tới)

  DI CƯ SANG NƯỚC KHÁC:
    → Context MỚI: cultural norms KHÁC
    → Body VẪN alert khi nói to trên tàu (Background Pattern fire)
    → PFC: "ở đây người ta nói to bình thường" (verbal chunk mới)
    → Body: VẪN khó chịu (Background Pattern >> 1 verbal chunk)
    → Qua 5-10 năm trong context mới: DẦN shift (new gist accumulate)
    → Nhưng stress → REVERT (old Background Pattern fire lại dưới PFC weakened)
```

### §9.3 — Expert intuition (High Density + Moderate Depth, novelty direction)

```
  SETUP: Programmer 20 năm kinh nghiệm.
    → Hàng chục nghìn chunks [code pattern → outcome]
    → Novelty-direction compile (curiosity, flow, opioid)

  FORMATION:
    → 20 năm × thousands of projects
    → Gist extract: [cấu trúc X → sẽ thành vấn đề]
    → Link density: CỰC CAO trong coding domain
    → Pattern = POSITIVE Background Pattern (novelty direction)

  NHÌN CODE MỚI:
    → Code mới, chưa từng thấy cụ thể
    → Body: "cái này sẽ bug" — PFC: "tôi... không giải thích được"
    → = Background Pattern fire → activate [bug prediction] chunks
    → CÓ THỂ partially verbalize: "code smell" → nhưng capture ~20%
    → Full pattern quá distributed → không label hết được

  KHÁC TRAUMA HOW:
    → Cùng mechanism: High Density + gist extraction + PFC partially invisible
    → KHÁC direction: novelty → approach, accurate, productive
    → = Chunk-Activation-Dynamics §4.3: "trauma = expertise = cùng cơ chế, khác hướng"
    → Applied at Background Pattern level: CONFIRMED
```

### §9.4 — Attachment style avoidant (High Density + Low-Moderate Depth)

```
  SETUP: Bố mẹ emotionally unavailable.
    → Không reject, không abuse — chỉ KHÔNG CÓ MẶT về cảm xúc.
    → Khóc → không ai đến. Vui → không ai chia sẻ.

  FORMATION:
    → Thousands of micro-absences × 10+ năm
    → Gist extract: [cần người → không có → tự handle]
    → KHÔNG có emotional peak → Low-Moderate depth per chunk
    → NHƯNG: link density CỰC CAO (mọi social chunk link tới)

  25 TUỔI:
    → PFC label: "tôi là người independent"
    → Background Pattern: [cần = không được đáp]
    → Partner muốn gần → body alert → pull away
    → PFC: "tôi cần space" (rationalize)
    → Thật: Background Pattern fire → SPM F1 simulate [sẽ bị bỏ] → avoidance

  TẠI SAO THERAPY PHẢI LÂU:
    → Therapist = new agent → SPM bias: "therapist cũng sẽ unavailable"
    → Phải: consistent presence × months → build NEW chunks về therapist
    → Dần: new chunks COMPETE với Background Pattern
    → Years: new Background Pattern [some people = available] accumulate
    → Old pattern VẪN CÒN nhưng tương đối yếu hơn
```

### §9.5 — "Luôn chọn nhầm người yêu" (mixed pattern)

```
  SETUP: Bố mẹ yêu nhưng unpredictable.
    → Hôm nay vui, mai gắt. Không biết hôm nay thế nào.

  FORMATION:
    → Gist extract: [yêu = hồi hộp + không biết hôm nay thế nào]
    → Background Pattern link với MỌI romance-related chunk

  20 TUỔI:
    → Gặp người ỔN ĐỊNH → body: "chán, không feel gì"
      (vì: KHÔNG match Background Pattern)
    → Gặp người UNPREDICTABLE → body: "ĐÂY LÀ YÊU!"
      (vì: MATCH Background Pattern → familiar → misinterpreted as attraction)
    → PFC: "mình cứ bị attracted người toxic"

  TẠI SAO THERAPY KHÓ:
    → [love = unpredictable] link với MỌI romance chunk (15+ năm)
    → Phải re-link tại NHIỀU entry points:
      body sensation khi gặp người mới,
      expectation khi texting,
      response khi partner consistent,...
    → Mỗi entry point = 1 re-linking effort
    → Tổng: hundreds of entry points → YEARS
```

---

## §10 — RESOLUTION PATHWAYS

### §10.1 — Tại sao không thể fix trực tiếp

```
⭐ BACKGROUND PATTERN KHÔNG THỂ RECONSOLIDATE TRỰC TIẾP:

  Reconsolidation (Nader 2000):
    → Trigger specific memory → window opens → modify → re-compile
    → 🟢 Effective cho hippocampal memories (individual episodes)

  Background Pattern:
    → KHÔNG CÓ "1 memory" cụ thể để trigger
    → Detail gốc ĐÃ FADE qua gist extraction
    → Pattern ĐÃ transfer sang neocortex
    → Reconsolidation cho neocortex-embedded patterns: 🟡 unclear

  Verbal intervention ("suy nghĩ tích cực"):
    → Install verbal chunk MỚI: "tôi xứng đáng"
    → 1 verbal chunk vs Background Pattern (thousands of chunks)
    → Link density: 1 vs thousands
    → Background Pattern WIN → verbal chunk = noise
    → = "Biết nhưng không cảm được"

  🟡 FRAMEWORK POSITION:
    → Không thể fix trực tiếp
    → Phải BUILD BACKGROUND PATTERN MỚI đủ mạnh để CẠNH TRANH
    → = Competitive re-linking (01b §3) nhưng ở SYSTEM LEVEL
```

### §10.2 — Build competing Background Pattern

```
⭐ RESOLUTION = BUILD ALTERNATIVE, NOT FIX ORIGINAL:

  CƠ CHẾ:
    ① Thay đổi ENVIRONMENT sustained (mới, an toàn, consistent)
    ② Chunks MỚI compile trong context MỚI (novelty direction)
    ③ Sleep gist-extract: gist MỚI from new experiences
       → VD: [effort → IS enough → appreciated]
    ④ Gist mới CẠNH TRANH với gist cũ [effort → not enough]
    ⑤ Qua MONTHS-YEARS: link density CỦA PATTERN MỚI tăng dần
    ⑥ Probability crossover: pattern mới > pattern cũ
    ⑦ Pattern cũ VẪN CÒN nhưng tương đối yếu hơn

  THỜI GIAN ESTIMATED:
    Low Density pattern: months (new environment sufficient)
    Moderate Density: 1-2 years
    High Density: 3-5+ years
    High Density + High Depth: 5-10+ years
    → = Tại sao "thay đổi tính cách" = years, not weeks

  THERAPY AS SYSTEMATIC CONSTRUCTION:
    → Therapy KHÔNG "fix" Background Pattern
    → Therapy TẠO CONDITIONS cho pattern mới hình thành:
      ① Safe environment (therapy room) → novel context → new chunks
      ② Consistent relationship (therapist) → counter [unreliable] SPM bias
      ③ Multi-entry-point: mỗi session trigger 1 góc → re-link tại góc đó
      ④ Sustained qua months-years → link density accumulate
      ⑤ Sleep consolidate giữa sessions → gist extract pattern mới
    → = Therapy = SYSTEMATIC competing Background Pattern construction
    → = Không phải "chữa" — mà "xây thay thế"

  ⚠️ PATTERN CŨ KHÔNG BAO GIỜ XÓA (Chunk.md §2.5):
    → Old Background Pattern VẪN tồn tại (neocortex-embedded)
    → Stress + PFC weakened → old pattern CÓ THỂ fire lại
    → = "Relapse khi mệt" — old links temporarily win
    → = "Functional resolution" — not deletion
    → = Đủ tốt: pattern mới dominant phần lớn thời gian
```

### §10.3 — Immigration as natural experiment

```
🟡 DI CƯ = NATURAL EXPERIMENT CHO BACKGROUND PATTERN CHANGE:

  Person: 20 năm trong culture A → di cư sang culture B
  Background Pattern: culture A patterns (high density, low depth)

  Year 1-2: ACUTE conflict
    → New experience CONFLICT với Background Pattern
    → Body: constant dissonance (culture shock)
    → PFC: "mọi thứ ở đây sai sai"

  Year 3-5: GRADUAL shift
    → New chunks compile in culture B context
    → Sleep gist-extract: new patterns FROM culture B
    → Background Pattern: old A + emerging B COMPETE
    → Body: "bớt lạ, nhưng chưa thoải mái hẳn"

  Year 5-10: NEW BACKGROUND PATTERN
    → Culture B patterns reach sufficient link density
    → Probability crossover: B > A for daily situations
    → BUT: stress → A fires lại ("thi thoảng thấy mình VN quá")
    → = Functional resolution — not replacement

  VỀ THĂM: test case
    → Return to culture A context → old Background Pattern REACTIVATE
    → Body: "quen thuộc" + "lạ lạ" (both patterns fire)
    → = Evidence: old pattern NEVER deleted, chỉ relatively weaker
    → 🟢 Context-dependent memory (Godden & Baddeley 1975)
```

### §10.4 — Background Pattern Conflict (Invisible Conflict)

```
⭐ KHI 2+ BACKGROUND PATTERNS XUNG ĐỘT:

  KHÁC SCHEMA CONFLICT (Schema.md §5.1):

    Schema conflict:
      → PFC CÓ THỂ observe: "muốn ăn vs muốn giảm cân" → BIẾT RÕ
      → PFC CÓ THỂ chọn → pain = decision cost → "dù sai cũng nhẹ"
      → = VISIBLE CONFLICT → CAN RESOLVE by choosing

    Background Pattern conflict:
      → PFC KHÔNG THỂ observe (cả 2 pattern invisible)
      → PFC KHÔNG THỂ chọn (doesn't know conflict EXISTS)
      → Cả 2 BPs fire sub-threshold → compound dissonance
      → PFC chỉ thấy EFFECTS: mệt, rối, "torn" mà không biết vì sao
      → KHÔNG thể "quyết định xong cho nhẹ" (không biết quyết định GÌ)
      → = INVISIBLE CONFLICT → CANNOT RESOLVE DIRECTLY → CHRONIC DRAIN


  CƠ CHẾ — HOW 2 BPs FIRE ĐỒNG THỜI:

    VÍ DỤ: Người Việt làm việc ở công ty nước ngoài.

    BP-A (cultural, 20 năm): [tránh conflict, đừng nói thẳng, harmony]
      → Link density: CỰC CAO (school + family + social × 20 năm)

    BP-B (professional, 5 năm): [phải assertive, phải nói ý kiến]
      → Link density: MODERATE (workplace × 5 năm)

    EVENT: Meeting — sếp hỏi "có ý kiến gì không?"

      BP-A fires (sub-threshold):
        → Chunks [risk, im lặng an toàn, trước đây nói bị ignore] activate
        → Body: hơi co lại, throat tightens nhẹ

      BP-B fires (sub-threshold):
        → Chunks [phải contribute, career growth, professional respect] activate
        → Body: hơi ready to speak, leaning forward nhẹ

      COMPOUND (Body-Feedback-Mechanism §4):
        → Body nhận 2 signals NGƯỢC: co lại + ready to speak
        → Mỗi signal quá yếu để PFC isolate (background level)
        → PFC nhận: compound dissonance → "hơi mệt, hơi confused"
        → KHÔNG biết WHY → attribute cho "meeting draining"

    SAU MỖI MEETING:
      → Dissonance không resolve (conflict vẫn còn)
      → Accumulate × months → "burnout" ← thực chất = BP conflict drain

    CÙNG CƠ CHẾ CHO:
      → Người nhập cư: cultural BP × new culture BP
      → Phụ nữ hiện đại: traditional [chăm gia đình] × modern [career ambition]
      → Người chuyển ngành: old professional BP × new field BP
      → Người mới ra khỏi religion: faith BP × secular reasoning BP


  3 PROPERTIES MỚI (khác schema conflict):

    ① DIAGNOSIS IMPOSSIBLE TỪ BÊN TRONG:
       → Schema conflict: "tôi biết tôi đang phân vân giữa A và B"
       → BP conflict: "tôi mệt nhưng không biết vì sao"
       → External observer (therapist, bạn thân) CÓ THỂ detect
         qua behavior PATTERNS mà chủ nhân không thấy
       → Schema.md §6.3: "Người khác thấy pattern mà chủ nhân không thấy"

    ② "JUST CHOOSE" KHÔNG WORK:
       → Schema conflict: PFC decide → pain reduces
       → BP conflict: PFC CANNOT decide (không biết decide GÌ)
       → Resolution phải qua EXPERIENTIAL pathway (§10.4 dưới)
       → KHÔNG thể verbal/logical resolve (PFC tools don't reach BPs)

    ③ ENERGY DRAIN CONSTANT (24/7):
       → Schema conflict: drain khi ĐANG NGHĨ (active, occasional)
       → BP conflict: drain LIÊN TỤC (both patterns ALWAYS background)
       → = "Luôn mệt mà không có lý do rõ" = classic BP conflict signature
       → Misdiagnosed as: depression, burnout, thyroid, chronic fatigue
       → THẬT: invisible conflict consuming resources 24/7


  4 RESOLUTION PATHWAYS CHO BP CONFLICT:

    ① CONTEXT-GATING (phổ biến nhất, KHÔNG phải resolution thật):
       → 1 BP dominant trong 1 context (01b §2.2 factor ⑤ context match)
       → Tại office: BP-B wins (professional context reinforce)
       → Tại nhà bố mẹ: BP-A wins (family context reinforce)
       → = "Khác người ở chỗ làm vs ở nhà" → "code-switching"
       → Cost: mỗi lần switch context = energy drain (re-bias)
       → NOT resolution — chỉ MANAGEMENT (conflict vẫn tồn tại)

    ② INTEGRATION (khó, lâu, TRUE resolution):
       → Tạo BACKGROUND PATTERN MỚI that includes BOTH:
         VD: "assertive AND respectful" → chunks satisfy CẢ HAI
       → Cần: experience ĐỦ NHIỀU nơi cả 2 satisfied đồng thời
       → VD: học "nói thẳng mà diplomatic" → new chunks compile
       → New chunks: [express + maintain harmony] → NOT conflict
       → Qua years: new gist extract → integrated BP form
       → = TRUE RESOLUTION — nhưng requires specific experiences + years
       → = Tại sao người có MENTOR tốt resolve nhanh hơn
         (mentor MODEL integration → chunks compile từ observation)

    ③ ONE WINS (environment change permanently):
       → Rời context cũ completely → BP-A không reinforced → DẦN yếu
       → BP-B reinforced daily → dominant
       → Cost: mất connection cũ, possible regret
       → Stress → BP-A reactivate ("thi thoảng thấy mình quá VN")
       → Not ideal: suppress, not integrate

    ④ CHRONIC DRAIN (default nếu KHÔNG intervention):
       → Cả 2 BPs fire liên tục → compound dissonance sustained
       → Cortisol baseline elevated → PFC weaken → LESS able to detect
       → Self-reinforcing loop (§8) BUT WITH 2 SOURCES feeding into loop
       → Misattribute: "burnout", "tuổi", "thiếu ngủ", "depression"
       → = RẤT NHIỀU NGƯỜI ở state này mà không biết nguyên nhân


  🟡 FRAMEWORK POSITION:
    → BP conflict = Schema.md §5.1 mechanisms APPLIED ở invisible level
    → Property MỚI: invisible → cannot self-diagnose → chronic drain as default
    → Resolution: Integration (②) là pathway duy nhất THẬT SỰ resolve
    → Practical: therapist/mentor detect behavior contradictions → name conflict
      → then experiential work build integrated chunks
    → "Just choose" / "just relax" / "just decide" = USELESS cho BP conflict
```

---

## §11 — RELATIONSHIP WITH EXISTING CONCEPTS

```
⭐ BACKGROUND PATTERN BỔ SUNG FRAMEWORK — KHÔNG CONTRADICT:

  Schema.md §4.1 Depth Gradient:
    → EXTENDS: thêm chiều thứ 2 (Link Density)
    → "Schema sâu" (Schema.md) = High Compile Depth
    → Background Pattern = High Link Density (có thể Low Depth)
    → 2D model COMPLETE hơn 1D depth-only

  Schema.md §8 Body Baseline State:
    → EXPLAINS: body baseline TỒNTẠI vì Background Pattern
    → Body Baseline = physical layer (cortisol, tension, HRV)
    → Background Pattern = chunk-level mechanism UNDERNEATH

  Chunk-Activation-Dynamics §4 Trigger Surface:
    → EXTENDS: trigger surface GROWTH over time
    → 01b: trigger surface tại compile time
    → Background Pattern: trigger surface TÍCH LŨY qua years

  Learning-Cycle §4.6 Gist Extraction:
    → APPLIES: gist extraction = Background Pattern formation mechanism
    → Learning-Cycle: 1 learning cycle (days-weeks)
    → Background Pattern: thousands of learning cycles (years)

  01c §4 1A/1B Selection Pressure:
    → CONNECTS: Background Pattern (threat) bias toward 1B
    → Threat background → low dissonance tolerance → reject real-check
    → = 1B not by choice but by Background Pattern constraint

  Anchor-Schema.md:
    → INTERACTS: Anchor-Schema operate ON TOP of Background Pattern
    → Anchor-Schema = ACTIVE sync point (vô thức chọn)
    → Background Pattern = PASSIVE bias (luôn có, không chọn)
    → Background Pattern CAN CONSTRAIN which anchors feel viable
    → VD: pattern [effort → not enough] → ambitious anchor "feel wrong"

  "Giọt nước tràn ly" (Schema.md §5.4):
    → EXPLAINS: Background Pattern = lý do ly đã đầy
    → Event nhỏ = giọt cuối → body-feedback cực lớn
    → Không phải event lớn → compound với Background Pattern
```

---

## §12 — OPEN QUESTIONS

```
BP-Q1: Reconsolidation có apply cho neocortex-embedded patterns?
  → 🟡 Research gap — crucial cho resolution pathways
  → Nếu CÓ → therapy có thể direct modify
  → Nếu KHÔNG → chỉ có competitive re-linking (current position)

BP-Q2: Link Density có đo được (proxy) không?
  → Association fluency test? (name related concepts in X seconds)
  → Implicit Association Test (IAT)?
  → fMRI resting-state connectivity?
  → 🟡 Novel prediction — cần empirical testing

BP-Q3: ✅ RESOLVED — 2 Background Patterns xung đột thế nào?
  → Drilled trong §10.4: "Invisible Conflict"
  → Compound dynamics fire sub-threshold → PFC blind → chronic drain
  → 4 resolution pathways: context-gating / integration / one wins / chronic drain
  → Key insight: "just choose" KHÔNG work vì PFC cannot see conflict
  → Integration = only TRUE resolution (build BP that includes both)

BP-Q4: Có Background Pattern TỰ RESOLVE khi context thay đổi?
  → Di cư → old context gone → old pattern DẦN yếu?
  → Hay neocortex-embedded = persist regardless of context?
  → Immigration evidence (§10.3) suggests: DẦN yếu, nhưng never zero
  → 🟡 Consistent with competitive re-linking, cần longitudinal data

BP-Q5: Epigenetics × Background Pattern?
  → Trauma → cortisol high → epigenetic changes → 1-2 thế hệ?
  → 🟢 Dias & Ressler 2014: fear conditioning → offspring response
  → Background Pattern TRUYỀN qua behavior (F3 install) + có thể epigenetics?
  → 🟡 Plausible, mechanism unclear

BP-Q6: AI detect Background Pattern?
  → AI đọc text = detect verbal chunks (~1/6 total)
  → Background Pattern: per definition PFC invisible → verbal output THIẾU
  → CẦN: behavior pattern over TIME (longitudinal data)
  → 3 tầng: AI detect behavior pattern → Expert feel-check → Client body-verify
  → Extends AI-Schema-Detection.md
  → 🟡 Plausible but very early
```

---

## §13 — HONEST ASSESSMENT

```
═══════════════════════════════════════
🟢 ESTABLISHED (individual components)
═══════════════════════════════════════

  Synaptic Homeostasis (SHY):           Tononi & Cirelli 2003, 2014
  Gist extraction in sleep:             Payne 2009, Stickgold 2013
  Active systems consolidation:         Born & Wilhelm 2012, Squire 1992
  Emotional decoupling (REM):           Walker 2017, van der Helm 2011
  Hippocampal replay:                   Wilson & McNaughton 1994
  Context-dependent memory:             Godden & Baddeley 1975
  Mood-congruent memory:                Bower 1981
  Habituation:                          Thompson & Spencer 1966
  Competitive re-linking:               Nader 2000
  Stress-induced relapse:               Sinha 2001
  Spreading activation probability:     Collins & Loftus 1975
  Cortisol PFC damage:                  Arnsten 2009
  ACE dose-response:                    Felitti 1998
  Attachment styles persist:            Bowlby/Ainsworth, replicated extensively
  Implicit bias:                        Greenwald 1998, IAT literature
  Fear conditioning epigenetics:        Dias & Ressler 2014


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (novel integration)
═══════════════════════════════════════

  Background Pattern as unified concept:           Novel — components established
  2D model (Compile Depth × Link Density):        Novel — extends Schema.md §4
  Link Density as independent dimension:          Novel — trigger surface extended
  Sleep as accelerator (not solver) for chronic:  Novel integration of sleep mechanisms
  SHY ratchet effect for active patterns:         Novel application of SHY
  Gist extraction as BP formation mechanism:      Novel application of gist research
  Self-reinforcing cortisol loop:                 Novel integration of cortisol + BP
  SPM bias from Background Pattern:               Novel application of SPM mechanism
  Resolution = build competing BP:                Novel — extends competitive re-linking
  Immigration as natural experiment:              Novel framing, consistent with evidence
  Body Baseline = reflection of chunk BP:         Novel — explains Schema.md §8
  Invisible Conflict (BP × BP):                   Novel — extends Schema.md §5.1
  Integration as only true BP conflict resolution: Novel — experiential, not verbal
  Chronic drain = misdiagnosed BP conflict:       Novel clinical framing
  2D model validated by Alzheimer data (v1.1):   Alzheimer "last in first out" confirms depth + density
  "Architecture determines pattern" (v1.1):      Meta-principle from Alzheimer reverse-engineering lens
  Glymphatic × BP substrate protection (v1.1):   Sleep protects infrastructure BP sits on


═══════════════════════════════════════
🔴 SPECULATIVE
═══════════════════════════════════════

  Exact link density quantification:              Concept valid, numbers speculative
  Sigmoid growth curve:                           Plausible shape, not measured
  Neocortex-embedded reconsolidation:             Genuine research gap
  Resolution timelines (years):                   Approximate, highly individual
  2 Background Patterns conflict mechanism:       Not drilled
  Epigenetics transmission:                       Research early-stage
```

---

## §14 — CROSS-REFERENCES

### §14.1 — Core mechanism files

```
  HEALTH CONDITIONS DRILL (v1.1):
    Alzheimer-Analysis.md v1.1 — §5-§6 "last in first out" (→ §2.4),
                                  §11 sleep×glymphatic (→ §4.2),
                                  §17 reverse-engineering lens (→ §2.4)

  Chunk.md v2.2                  — chunk substrate, §2.4 NT7 direction, §4 activation, §5.4 compile depth
  Schema.md v2.0                 — §4 depth gradient (EXTENDED by §2 file này),
                                   §8 body baseline (EXPLAINED by file này)
  Chunk-Activation-Dynamics.md   — §4 trigger surface (EXTENDED: growth over time)
  Chunk-Discovery-Lifecycle.md   — §4 1A/1B (CONNECTED: BP bias toward 1B)
  Learning-Cycle.md              — §4.1 SHY, §4.6 gist extraction
                                   (APPLIED: BP formation mechanism)
  Body-Feedback-Mechanism.md     — §3.2 Chunk-Miss (APPLIED: continuous miss),
                                   §4 compound (APPLIED: BP as compound engine)
  Gap-Direction.md               — §9 BP constrains gap direction landscape
                                   (APPLIED: BP bias which gaps CAN form + directions)
  Self-Pattern-Match.md v2.1     — §4 context-dependent (APPLIED: BP bias SPM)
  Cortisol-Baseline.md v2.0      — §9 PFC damage (CONNECTED: self-reinforcing loop)
  Anchor-Schema.md v1.2          — §2 trust (INTERACTS: BP constrains anchors)
  Valence-Propagation.md v1.2    — valence per-entity (BP bias valence assignment)
```

### §14.2 — Observation parameter files

```
  Observation/Novelty.md         — novelty drive × BP interaction
  Observation/Threat.md          — threat cascade × BP self-reinforcing
  Observation/Boredom.md         — "chán" có thể = BP miss variant
  Observation/Connection.md      — attachment = social BP
  Observation/Status.md          — status drive × BP constraint
  Observation/Meaning.md         — meaning = life-level anchor × BP
  Observation/Autonomy.md        — autonomy = controllability × BP
```

### §14.3 — Application files

```
  AI-Schema-Detection.md         — BP detection qua AI (extended)
  Feeling-Literacy-Training.md   — training detect BP effects
  Research/Education/            — education × BP (threat-direction prevention)
```

### §14.4 — Academic references

```
  🟢 Tononi & Cirelli 2003, 2014   — Synaptic Homeostasis Hypothesis
  🟢 Payne 2009                     — Sleep gist extraction
  🟢 Stickgold 2013                 — Sleep abstracts rules
  🟢 Born & Wilhelm 2012            — Active systems consolidation
  🟢 Squire 1992                    — Hippocampus → neocortex transfer
  🟢 Walker 2017                    — Sleep emotional decoupling
  🟢 van der Helm 2011              — REM amygdala reduction
  🟢 Wilson & McNaughton 1994       — Hippocampal replay
  🟢 Nader 2000                     — Memory reconsolidation
  🟢 Collins & Loftus 1975          — Spreading activation
  🟢 Godden & Baddeley 1975         — Context-dependent memory
  🟢 Bower 1981                     — Mood-congruent memory
  🟢 Thompson & Spencer 1966        — Habituation
  🟢 Sinha 2001                     — Stress-induced relapse
  🟢 Arnsten 2009                   — Stress impairs PFC
  🟢 Felitti 1998                   — ACE dose-response
  🟢 Greenwald 1998                 — Implicit Association Test
  🟢 Dias & Ressler 2014            — Fear conditioning epigenetics
  🟢 Bowlby 1969 / Ainsworth 1978   — Attachment theory
  🟢 Maret 2011, Yang 2014          — Dendritic spine sleep turnover
```

---

> *Background-Pattern.md v1.1 — "Trọng lực của chunk system."*
>
> Background Pattern = accumulated chunk-network pattern
> hình thành qua experience + sleep gist extraction qua thời gian dài.
> 2D model: Compile Depth × Link Density.
> v1.1: Alzheimer "last in first out" validates 2D model. "Architecture determines pattern."
> Sleep = accelerator, NOT solver. Glymphatic = substrate protector (Hauglund 2025).
> PFC invisible. Bias mọi thứ. Cùng mechanism: trauma, expertise, culture.
> Resolution = build competing pattern, NOT fix original.
> "Biết nhưng không cảm được" = PFC updated, Background Pattern chưa.
>
> Phiên bản: v1.1, 2026-05-15.
