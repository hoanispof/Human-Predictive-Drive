---
title: Hardware Calibration — Nhận Diện + Điều Chỉnh Per-Individual
version: 1.1
created: 2026-04-03 (DRAFT) → 2026-05-11 (v1.0 rewrite)
updated: 2026-05-25 (v1.1 — MODERATE REFINE)
status: v1.1 APPLICATION
scope: |
  Per-hardware calibration THỰC HÀNH —
  từ "tại sao cần per-individual" → "LÀM THẾ NÀO nhận diện + điều chỉnh"
  TẦNG 4 — Applications, KHUNG per-individual (brain-based).
  v1.1 KEY CHANGES:
    - Connection v3.1→v5.0: DIM 5 Social Processing updated (Self-Pattern-Modeling v3.1)
    - Agent-Mechanism v1.0→v2.1: Self-Pattern-Modeling v3.1 (1 mechanism × 3 dimensions)
    - +Hardware-Subsidy: observation includes subsidy response per hardware
    - +Compiled Quality Dimension: observe compile QUALITY (genuine/schema/threat)
    - +Body-Feedback-Label 3-tier: observation methodology precision
    - +PFC Budget: calibration = PFC cost → session constraint
    - +Gap-Distribution-Profile: per-individual gap landscape observation
    - +Dissonance-Signal-Architecture: Evaluative vs Direct-State in miscalibration
    - +Entity-Access + Entity-Compiled: teacher-student relationship calibration lens
    - All dependency versions updated
purpose: |
  BRIDGE giữa brain mechanism và practical education.
  Core-Hardware (PARAMETERS) → File này (observe + calibrate) → Education-System v3.0 (apply).
  "Chuyển hardware specs thành ACTIONABLE observation + adjustment"
  ⚠️ File này = DURABLE NHẤT trong folder (brain-based → decades).
  ⚠️ Nhận diện ≠ dán nhãn. Continuous, multi-dimensional, evolving.
position: |
  Applications/Education-System/ — TẦNG 4.
  ĐỌC SAU: Education-System.md v3.0 (WHERE to apply calibration).
  ĐỌC TRƯỚC: Curriculum-Framework.md v2.0 (WHAT to calibrate for).
previous: backup/v1.0/Hardware-Calibration.md (1,538L, v1.0, 2026-05-11)
dependencies:
  core-hardware:
    - Core-Hardware.md v1.0 — 4 zones A/B/C/D, hardware profiles
    - PFC-Hardware.md v1.1 — DRD4, COMT — individual parameters
    - Modality.md v1.0 — 6 encoding channels
    - Cortisol-Baseline.md v2.1 — amplifier, 5 Roles, direction > level
    - Body-Base.md v3.1 — Model 3+1, interoception, Compilable Architecture
  core-mechanism:
    - Connection.md v5.0 — 3 Generative Primitives, Resonance Decline, 4-Layer Sustainability
    - Agent-Mechanism.md v2.1 — Self-Pattern-Modeling v3.1 integration hub
    - Entity-Valence-Dynamics.md v1.0 — Hardware-Subsidy spectrum per entity
    - PFC-Operations.md v1.1 — PFC Budget, Compiled Quality Dimension
  body-feedback:
    - Body-Feedback-Label.md v2.1 — 3-tier vocabulary, observation precision
    - Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State distinction
    - Gap-Distribution-Profile.md v1.1 — per-individual gap landscape
    - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State Reward
  agent-entity:
    - Entity-Compiled.md v1.0 — formation 40→200h, Hub-and-Spoke
    - Entity-Access.md v1.2 — gradient Mức 0-5
    - Coordination-Node.md v1.2 — teacher as coordination node
    - Self-Pattern-Modeling.md v3.1 — 1 mechanism × 3 dimensions
  education-foundation:
    - Education-Mechanism.md v2.0 — HOW: Cost Formula, Direction > Level
    - Education-System.md v3.0 — WHERE: per-stage, teacher role, ENGINE/ROAD/VEHICLE
    - Connection-Education.md v1.0 — WHO: 5 trụ social interaction education
  application:
    - Sensitivity-Classification.md v1.0 — 3 hardware sensitivity groups
    - PFC-Configuration.md v1.0 — 6 dynamic modes
    - Simulation-Engine.md v1.1 — AI calibration support
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Neuroscience mechanism | 🟡 Framework inference | 🔴 Hypothesis
---

# Hardware Calibration — Nhận Diện + Điều Chỉnh Per-Individual

> **⚠️ File này = DURABLE NHẤT trong folder (brain-based → decades).**
> **⚠️ Nhận diện ≠ dán nhãn. Continuous, multi-dimensional, evolving.**
> **Quy ước:** 🟢 Neuroscience mechanism (verified) | 🟡 Framework inference (derived) | 🔴 Hypothesis

---

## Mục lục

0. Mục đích — Tại sao cần file này
1. "Hardware" là gì trong context education
2. Observable indicators — Đo qua hành vi
3. Calibration per major dimensions
4. Neurodiversity — Hardware variation, not "disorder"
5. Common miscalibrations — Labels sai phổ biến
6. Practical calibration process — Quy trình thực hành
7. Honest Assessment + Kết nối

---

## 0. TẠI SAO CẦN FILE NÀY

```
NGHỊCH LÝ CỦA "ONE SIZE FITS ALL":

  Education-Mechanism.md v2.0 §2.3 (Cost Formula):
    → cost ≈ f(chunk_gap × hardware_mismatch × direction)
    → Cùng content + KHÁC hardware → KHÁC cost hoàn toàn
    → "One size fits all" = chỉ FIT average → bỏ lại cả hai đầu

  Education-System.md v3.0 đã nói:
    → §2: per-hardware bắt đầu identify Stage 2 (6-12)
    → §3: hardware tendencies RÕ hơn Stage 3 (12-18)
    → §7: teacher skill #1 = NHẬN DIỆN per learner

  NHƯNG: "nhận diện" = NÓI DỄ, LÀM KHÓ
    → Nhận diện CÁI GÌ? (hardware dimensions nào?)
    → Nhận diện BẰNG GÌ? (không thể scan não)
    → Nhận diện ĐỂ LÀM GÌ? (adjust thế nào?)
    → = File này trả lời 3 câu hỏi đó


FILE NÀY = BRIDGE GIỮA:

  Core-Hardware.md v1.0       →  File này  →  Education-System.md v3.0
  PFC-Hardware.md v1.1           (HOW to     (WHERE to apply
  (hardware PARAMETERS            observe +    calibration
   = cái NÃO CÓ)                 calibrate)   trong system)

  = "Chuyển hardware specs thành ACTIONABLE observation + adjustment"


3 NGUYÊN TẮC CỐT LÕI:

  ① NHẬN DIỆN ≠ DÁN NHÃN
     → "Con là kiểu somatic" = LABEL → schema cứng → self-fulfilling prophecy
     → "Hiện tại con respond tốt hơn với hands-on" = OBSERVATION → flexible
     → Sự khác biệt: label = FIXED / observation = EVOLVING
     → Brain đang develop (đặc biệt 0-25) → tendencies CÓ THỂ shift

  ② LIÊN TỤC, KHÔNG 1 LẦN
     → Test 1 lần (IQ test, personality test) = SNAPSHOT → misleading
     → Brain thay đổi: puberty shift, environment shift, experience shift
     → = Cần OBSERVE liên tục + UPDATE liên tục
     → = "Chẩn đoán liên tục" giống bác sĩ theo dõi bệnh nhân

  ③ MULTI-DIMENSIONAL, KHÔNG SINGLE SCORE
     → IQ = 1 số → collapse mọi dimension → miss PHẦN LỚN information
     → Hardware = NHIỀU dimensions đồng thời (§1)
     → Cùng 1 learner: somatic-dominant + high-VTA + low-cortisol-sensitivity
       = PROFILE, không phải SCORE
     → = "Bản đồ" per-individual, không phải "điểm" per-individual


  v1.1 BỔ SUNG — 2 LENS XUYÊN SUỐT:

  ④ HARDWARE-SUBSIDY (Entity-Valence-Dynamics.md v1.0 §5):
     → Per-hardware: cách learner RESPOND với subsidy KHÁC
     → Parent subsidy (MAX) → learner nào body "nhận" mạnh → faster compile
     → Teacher subsidy (MODERATE) → per-hardware sensitivity → adjust subsidy quality
     → Observation: KHÔNG CHỈ observe 6 DIM → observe subsidy RESPONSE nữa

  ⑤ COMPILED QUALITY (PFC-Operations v1.1):
     → Observe compile SUCCESS chưa đủ → observe compile QUALITY
     → Genuine-compiled (approach tag, self-reinforcing) = MỤC TIÊU
     → Schema-compiled (neutral, fragile) = TẠM CHẤP NHẬN
     → Threat-compiled (avoidance tag, "giỏi nhưng ghét") = 🔴 RED FLAG
     → Calibration: hardware mismatch → threat compile → adjust TRƯỚC KHI compile
```

---

## 1. "HARDWARE" LÀ GÌ TRONG CONTEXT EDUCATION

```
TỪ CORE FRAMEWORK — hardware = specs cơ bản của não:
  (ref: Core-Hardware.md v1.0 §5-§6 — "Hardware sets RANGE, chunks choose POSITION")

  Hardware = cái não ĐÃ CÓ khi bắt đầu learn
    → Set RANGE khả năng → experience chọn VỊ TRÍ trong range
    → ≠ "Năng lực cố định" → = "phạm vi + xu hướng"
    → VD: DRD4-7R = VTA detect chunk LỚN → RANGE sẵn hướng novelty-seeking
      → KHÔNG có nghĩa "chắc chắn ADHD" → = tendency, environment quyết định biểu hiện

  Hardware = GENETICS × DEVELOPMENT × ENVIRONMENT
    → Genetics: DNA set RANGE (VD: COMT Val/Met, DRD4 length, MAO-A activity)
    → Development (0-6): Child-Dev bộ 4 → wiring TRONG range
    → Environment: ongoing → influence VỊ TRÍ trong range
    → = 3 yếu tố → UNIQUE per individual


6 HARDWARE DIMENSIONS ẢNH HƯỞNG LEARNING:

  ┌─────────────────────────────────────────────────────────────────┐
  │ DIM 1: MODALITY BALANCE                                        │
  │   (ref: Modality.md v1.0 — 6 encoding channels)               │
  │                                                                 │
  │   Con người encode/process qua NHIỀU modality:                 │
  │     Visual, Auditory, Somatic/Motor, Emotional                 │
  │     + Communication (label, transfer, compress)                │
  │                                                                 │
  │   Mỗi người: TỈ LỆ KHÁC → ảnh hưởng cách HỌC:               │
  │     Somatic-dominant: body "hiểu" trước PFC                   │
  │       → Hands-on learning = FAST / Lecture = SLOW              │
  │     Visual-dominant: "thấy" = "hiểu"                          │
  │       → Diagram, video, spatial = FAST / Text-only = SLOW     │
  │     Auditory-dominant: "nghe" = processing chính              │
  │       → Discussion, podcast = FAST / Silent reading = SLOW    │
  │     Verbal-dominant: language = compression tool chính         │
  │       → Reading, writing, labels = FAST / Non-verbal = SLOW   │
  │                                                                 │
  │   ⚠️ KHÁC "learning styles" (debunked):                       │
  │     "Learning styles" claim: MỖI NGƯỜI chỉ học tốt 1 style   │
  │     Hardware: mỗi người có DOMINANT modality NHƯNG             │
  │       multi-modal = better FOR ALL (Mechanism v2.0 §2.3)            │
  │     = Không phải "chỉ dạy theo style" → mà "biết dominant     │
  │       → leverage dominant + SUPPLEMENT với các modality khác"  │
  │                                                                 │
  │   🟢 Modality differences = well-established neuroscience      │
  │   🟡 "Dominant modality ảnh hưởng learning efficiency"         │
  │      = framework inference — logical, chưa fully proven        │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │ DIM 2: VTA THRESHOLD / NOVELTY SEEKING                         │
  │   (ref: PFC-Hardware.md v1.1 §4 — DRD4 Chunk Threshold,       │
  │    Observation/Novelty.md v1.0)                                │
  │                                                                 │
  │   VTA = novelty detector → dopamine → "muốn explore tiếp"    │
  │   DRD4 variant ảnh hưởng VTA chunk detection size:            │
  │     7R: detect biến động LỚN → cần NHIỀU novelty để engage   │
  │     4R: detect biến động NHỎ → engage với ROUTINE cũng được  │
  │                                                                 │
  │   SPECTRUM cho education:                                      │
  │     HIGH-VTA (7R-like):                                        │
  │       → Cần VARIETY, novelty, change → dễ chán routine        │
  │       → Strength: explore nhanh, creative, adaptable           │
  │       → Risk: "không tập trung" = LABEL phổ biến nhất         │
  │       → Calibration: rotation format, shorter segments,        │
  │         project-based, cho phép movement                       │
  │                                                                 │
  │     LOW-VTA (4R-like):                                         │
  │       → Comfortable với routine, structure, depth              │
  │       → Strength: focus sâu, systematic, reliable              │
  │       → Risk: "boring" environment = CŨNG engage (less visible)│
  │       → Calibration: structured learning, sequential depth,    │
  │         routine = OK, sudden change = disruptive               │
  │                                                                 │
  │   🟢 DRD4 variants + VTA dopamine = established               │
  │   🟡 Educational implications = derived                        │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │ DIM 3: CORTISOL SENSITIVITY / STRESS RESPONSE                  │
  │   (ref: Cortisol-Baseline.md v2.1 — amplifier, 5 Roles)       │
  │                                                                 │
  │   Cortisol = change-readiness AMPLIFIER (không phải "stress    │
  │   hormone" — Cortisol v2.1 reframe)                            │
  │   Baseline set bởi: genetics + early environment (0-6)         │
  │     → Child-Dev: attachment quality → cortisol baseline        │
  │                                                                 │
  │   SPECTRUM:                                                    │
  │     HIGH baseline (dễ stress):                                 │
  │       → Ít pressure THÊM = đã vượt optimal → PFC suppress     │
  │       → PFC Mode: dễ shift sang Reallocation/Reconfigured     │
  │         (PFC-Configuration.md — cortisol push mode shift)      │
  │       → Calibration: LOWER pressure, MORE recovery, safe space │
  │       → ⚠️ "Yếu đuối" = LABEL SAI → = cortisol đã CAO sẵn  │
  │                                                                 │
  │     LOW baseline (resilient):                                  │
  │       → Chịu được MORE challenge → thậm chí CẦN challenge     │
  │       → Calibration: moderate-high challenge OK, routine = bored│
  │       → ⚠️ "Quá thoải mái" có thể = cortisol quá thấp        │
  │         → cũng sub-optimal (inverted-U — Cortisol v2.1 §3)    │
  │                                                                 │
  │   ⚠️ Cortisol baseline CÓ THỂ SHIFT (chậm — weeks/months)    │
  │     → Environment thay đổi → baseline thay đổi                │
  │     → = Không phải "fixed" → nhưng shift CHẬM                 │
  │                                                                 │
  │   🔗 Sensitivity-Classification.md v1.0:                       │
  │     3 groups: High-Signal / Medium / Low-Signal hardware       │
  │     → High-Signal person + moderate pressure = already HIGH    │
  │     → Low-Signal person + moderate pressure = vừa đủ           │
  │     → = CÙNG pressure level, KHÁC hardware → KHÁC response    │
  │                                                                 │
  │   🟢 Cortisol baseline, HPA axis = well-established           │
  │   🟡 Per-individual calibration for education = derived        │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │ DIM 4: PFC DEVELOPMENT PACE                                    │
  │   (ref: PFC-Hardware.md v1.1 §1-§3, Core-Hardware.md §2)      │
  │                                                                 │
  │   PFC mature ~25 tuổi TRUNG BÌNH → nhưng PACE khác per person │
  │   PFC-Quality + Clear Speed (COMT) = khác per individual       │
  │     (PFC-Hardware.md v1.1: COMT Val/Val = clear nhanh,         │
  │      Met/Met = clear chậm nhưng focus tốt hơn)                │
  │                                                                 │
  │   SPECTRUM:                                                    │
  │     FAST PFC development:                                      │
  │       → Abstract thinking SỚM hơn average                     │
  │       → Sustained attention SỚM hơn                            │
  │       → Risk: "gifted" label → bored khi pace quá chậm        │
  │       → Calibration: cho abstract SỚM hơn, depth SỚM hơn     │
  │                                                                 │
  │     SLOW PFC development (BÌNH THƯỜNG — not deficit):          │
  │       → Cần CONCRETE lâu hơn trước abstract                   │
  │       → Sustained attention NGẮN hơn → cần breaks nhiều hơn   │
  │       → Risk: "kém" label → thật ra = PFC chưa ready          │
  │       → Calibration: concrete → abstract DẦN DẦN, patience    │
  │         → "Chờ não ready" ≠ "không dạy" → = dạy ĐÚNG LEVEL   │
  │                                                                 │
  │   COMT Val/Met variant (PFC-Hardware.md v1.1 §3):             │
  │     Val/Val: PFC clear NHANH → good under stress, less focus   │
  │     Met/Met: PFC clear CHẬM → better sustained focus, stress-  │
  │              vulnerable                                         │
  │     → ẢNH HƯỞNG: cách learner perform under exam pressure     │
  │       vs cách perform trong calm environment = CÓ THỂ KHÁC    │
  │                                                                 │
  │   🟢 PFC development timeline, COMT variants = established    │
  │   🟡 Educational pace adjustment = derived                     │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │ DIM 5: SOCIAL PROCESSING NEEDS                                 │
  │   (ref: Connection.md v5.0, Agent-Mechanism.md v2.1 — Self-Pattern-Modeling v3.1)     │
  │                                                                 │
  │   Social brain = oxytocin circuits, Self-Pattern-Modeling v3.1  │
  │   (1 mechanism × 3 dimensions — simulate others' states),      │
  │   Hardware-Subsidy (social buffering), status hierarchy         │
  │   → ảnh hưởng cách learn TRONG NHÓM                           │
  │                                                                 │
  │   SPECTRUM:                                                    │
  │     HIGH social needs:                                         │
  │       → Learn tốt TRONG NHÓM → peer collaboration = boost     │
  │       → Social approval = bridge MẠNH                          │
  │       → Isolation = cortisol source → hại learning             │
  │       → Self-Pattern-Modeling active → learn qua observe + simulate others            │
  │       → Hardware-Subsidy cao → peer presence = subsidy SOURCE  │
  │       → Calibration: group work, peer teaching, collaborative  │
  │                                                                 │
  │     LOW social needs:                                          │
  │       → Learn tốt SOLO hoặc 1-on-1 → group = distracting     │
  │       → Internal processing = CÁCH learn chính                 │
  │       → Social pressure = cortisol source → hại learning       │
  │       → Calibration: quiet space, mentor 1-on-1, solo projects │
  │                                                                 │
  │   ⚠️ Social needs ≠ social skills                             │
  │     → Low social needs ≠ "anti-social" → = prefers different   │
  │       learning CONTEXT, có thể social skills TUYỆT VỜI        │
  │                                                                 │
  │   🟡 Social learning spectrum = framework application          │
  └─────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │ DIM 6: BODY-BASE DOMINANCE                                     │
  │   (ref: Body-Base.md v3.1 — Compilable Architecture,            │
  │    interoception)                                               │
  │                                                                 │
  │   Body-base = "gut feeling", interoception, somatic processing │
  │   Body-Base v3.1: "Body evaluates PATTERNS, not reality"      │
  │   → Body phản ứng TRƯỚC, PFC observe SAU                      │
  │   Mỗi người: body signal MẠNH/YẾU khác nhau                  │
  │                                                                 │
  │   SPECTRUM:                                                    │
  │     HIGH body-base (body "biết" trước PFC):                   │
  │       → "Gut feeling" MẠNH, interoception RÕ                  │
  │       → Learn qua EXPERIENCE trước → verbalize SAU            │
  │       → "Hiểu bằng body trước, giải thích bằng lời sau"      │
  │       → Calibration: experiential first, verbal second         │
  │                                                                 │
  │     LOW body-base (PFC "biết" trước body):                    │
  │       → Rational processing dominant                            │
  │       → Learn qua LOGIC trước → experience verify SAU         │
  │       → "Hiểu bằng lời trước, confirm bằng body sau"         │
  │       → Calibration: concept first, application second          │
  │                                                                 │
  │   🟡 Body-base spectrum = framework concept                    │
  │      Interoception differences = 🟢 established                │
  └─────────────────────────────────────────────────────────────────┘


TỔNG HỢP — HARDWARE PROFILE = 6 DIMENSIONS:

  ┌────────────────────────┬──────────────────────────────────┐
  │ Dimension              │ Spectrum                          │
  ├────────────────────────┼──────────────────────────────────┤
  │ ① Modality balance     │ somatic ← → verbal/visual       │
  │ ② VTA threshold        │ high (novelty) ← → low (routine)│
  │ ③ Cortisol sensitivity │ high (sensitive) ← → low (resilient)│
  │ ④ PFC development pace │ fast ← → slow (BOTH = normal)   │
  │ ⑤ Social processing    │ high (group) ← → low (solo)     │
  │ ⑥ Body-base dominance  │ high (body-first) ← → low (PFC-first)│
  └────────────────────────┴──────────────────────────────────┘

  = 6 dimensions × SPECTRUM mỗi dimension = UNIQUE per individual
  = ≠ "4 kiểu người" (MBTI-style) → = CONTINUOUS, multi-dimensional
  = ≠ IQ (1 số) → = PROFILE (bản đồ)
  = ≠ Fixed → = EVOLVING (đặc biệt 0-25, nhưng cả sau đó)

  ⚠️ 6 dimensions này = framework selection — KHÔNG claim đây là
     TẤT CẢ dimensions relevant cho education. Có thể thiếu.
     Nhưng: 6 này = ACTIONABLE cho education calibration.

  🔗 V7.8 CONNECTION — Evaluative/Direct-State Reward (Reward-Signal-Architecture v2.0):
     → Hardware profile ảnh hưởng CẢ 2 loại reward:
       Evaluative (opioid): per-hardware khác ngưỡng "đáng"
       Direct-State (hardware-direct): per-hardware khác loại body signal
     → Somatic-dominant: Direct-State reward qua MOVEMENT mạnh
     → Verbal-dominant: Evaluative reward qua UNDERSTAND mạnh
     → = Calibration cần biết: reward TYPE nào dominant cho learner NÀY

  🔗 CROSS-CUTTING LENS 1 — Hardware-Subsidy (Entity-Valence-Dynamics.md v1.0 §5):
     → Per-hardware: cách learner RESPOND với subsidy từ người khác = KHÁC
     → Parent (MAX subsidy): high body-base learner "nhận" oxytocin qua touch MẠNH hơn
     → Teacher (MODERATE subsidy): social-dominant learner → teacher presence = boost LỚN
     → AI (NONE subsidy): per-hardware ĐỀU thiếu → nhưng high-social thiếu NHẤT
     → = Observe: learner NÀY respond với subsidy TYPE nào? → adjust per DIM

  🔗 CROSS-CUTTING LENS 2 — Compiled Quality Dimension (PFC-Operations v1.1):
     → 6 DIM observation + 1 quality check: cái đã compile = GENUINE hay THREAT?
     → Genuine-compiled: approach tag, tự reinforce, per-domain → MỤC TIÊU
     → Schema-compiled: neutral, fragile, per-context → chấp nhận tạm
     → Threat-compiled: avoidance tag, locked, "giỏi nhưng ghét" → 🔴 RED FLAG
     → Hardware mismatch kéo dài → threat compile → "giỏi" trên điểm nhưng ghét domain
     → = Observe: learner approach hay avoid domain NÀY? → quality check TRƯỚC depth check
```

---

## 2. OBSERVABLE INDICATORS — ĐO QUA HÀNH VI

```
CORE CHALLENGE:

  → KHÔNG THỂ scan não learner → KHÔNG đo hardware TRỰC TIẾP
  → PHẢI đo qua BEHAVIOR indicators
  → Behavior = OUTPUT của hardware × environment × experience
  → = NOISY signal → cần TRIANGULATION + LIÊN TỤC


NGUYÊN TẮC OBSERVATION:

  ① ĐO BEHAVIOR, KHÔNG ĐÁN NHÃN:
     → "Trẻ đứng dậy thường xuyên trong lớp" = observation
     → "Trẻ hyperactive" = label
     → Observation = DATA → có thể interpret nhiều cách
     → Label = CONCLUSION → đóng khung interpretation
     → = Giữ ở level OBSERVATION cho đến khi pattern RÕ

  ② NHIỀU NGUỒN (triangulation):
     → Teacher observe: trong class, structured context
     → Parent observe: ở nhà, unstructured context
     → Self-report: khi learner đủ lớn (~10+ → tăng dần)
     → AI data: learning pattern, pace, error pattern (era-specific)
     → = 1 source = biased / 3+ sources = PATTERN emerge

  ③ LIÊN TỤC, KHÔNG 1 LẦN:
     → Observation tuần 1 ≠ tuần 10 (adjustment period)
     → Stage 2 observation ≠ Stage 3 (puberty shift)
     → = "Album ảnh" (many snapshots over time) > "1 ảnh chụp"

  ④ PER-CONTEXT:
     → Cùng learner: behavior KHÁC trong math vs art vs recess
     → Hardware dimensions CÓ THỂ express KHÁC per domain
     → = Observe PER CONTEXT, không generalize từ 1 context

  ⑤ 3-TIER PRECISION (Body-Feedback-Label v2.1 §1):
     → Observation description cần ĐỦ cụ thể cho context:
       Tier 1 (general): "trẻ có body-feedback âm" → quá mờ, chỉ dùng ban đầu
       Tier 2 (direction): "trẻ thể hiện dissonance khi ngồi yên lâu" → ĐỦ cho observation log
       Tier 3 (specific): "high-VTA, somatic-dominant, cortisol tăng khi routine" → hypothesize stage
     → Education observation: Tier 2 chủ đạo, Tier 3 khi enough data triangulated
     → ⚠️ Tier 3 nghe cụ thể → DỄ trở thành LABEL → dùng CẨN THẬN


PER-DIMENSION: CÁI GÌ OBSERVE, KHI NÀO, THẾ NÀO:

  DIM 1 — MODALITY BALANCE:
  ┌────────────┬───────────────────────────────────────────────────┐
  │ Tuổi       │ Observable indicators                             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 3-6        │ Play preference: build (somatic) vs draw (visual) │
  │            │ vs talk (verbal) vs listen (auditory)             │
  │            │ → Observe TRONG FREE PLAY (không structured)      │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 6-12       │ Learning response: engage NHẤT khi hands-on vs   │
  │            │ khi diagram vs khi discussion vs khi reading?     │
  │            │ Recall: nhớ tốt nhất cái THẤY vs NGHE vs LÀM?   │
  │            │ Expression: thể hiện hiểu biết bằng gì tốt nhất?│
  ├────────────┼───────────────────────────────────────────────────┤
  │ 12-18      │ Self-report: "tôi hiểu nhất khi..."             │
  │            │ Study habits: tự chọn method nào?                 │
  │            │ Project output: chọn express bằng format nào?     │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 18+        │ Self-awareness: "tôi biết tôi learn best khi..."│
  │            │ Meta-learning: tự adjust method per content       │
  └────────────┴───────────────────────────────────────────────────┘

  DIM 2 — VTA THRESHOLD:
  ┌────────────┬───────────────────────────────────────────────────┐
  │ Tuổi       │ Observable indicators                             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 3-6        │ Attention span per activity: ngắn + đổi liên tục │
  │            │ (high-VTA) vs dài + focus sâu (low-VTA)          │
  │            │ Reaction to new toys vs familiar toys              │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 6-12       │ Classroom: restless khi routine (high) vs         │
  │            │ comfortable with routine (low)                    │
  │            │ Engagement pattern: excited by NEW → drop → NEW   │
  │            │ vs steady engagement with SAME topic              │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 12-18      │ Interest pattern: many shallow interests (high)   │
  │            │ vs few deep interests (low)                       │
  │            │ Response to repetition: frustrated (high) vs      │
  │            │ comfortable/preferred (low)                       │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 18+        │ Self-awareness + career pattern                   │
  └────────────┴───────────────────────────────────────────────────┘

  DIM 3 — CORTISOL SENSITIVITY:
  ┌────────────┬───────────────────────────────────────────────────┐
  │ Tuổi       │ Observable indicators                             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 3-6        │ Separation anxiety level, reaction to new people  │
  │            │ Recovery time after upset (nhanh vs chậm)         │
  │            │ Sleep disruption frequency                         │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 6-12       │ Test anxiety: freeze, cry, stomach ache (high)    │
  │            │ vs calm/excited (low)                             │
  │            │ Response to criticism: collapse vs shrug           │
  │            │ Physical signs: nail biting, stomach issues        │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 12-18      │ Exam performance vs daily performance (gap = high)│
  │            │ Social anxiety signals                             │
  │            │ Self-report: "tôi lo lắng khi..."                │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 18+        │ Performance under pressure pattern                │
  │            │ Recovery needs after stressful periods             │
  └────────────┴───────────────────────────────────────────────────┘

  DIM 4 — PFC DEVELOPMENT PACE:
  ┌────────────┬───────────────────────────────────────────────────┐
  │ Tuổi       │ Observable indicators                             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 3-6        │ Rule-following ability, impulse control level     │
  │            │ Abstract vs concrete play (pretend = early PFC)   │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 6-12       │ Abstract concept grasp: quick (fast) vs needs     │
  │            │ concrete first (normal/slow)                      │
  │            │ Sustained attention: 20+ min (fast) vs 10 min     │
  │            │ Working memory: multi-step instructions           │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 12-18      │ Hypothetical reasoning: "what if..." thinking     │
  │            │ Planning ability: short-term vs long-term          │
  │            │ Self-regulation: emotion + impulse control         │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 18+        │ Mostly mature — individual differences in         │
  │            │ PFC efficiency under load                          │
  └────────────┴───────────────────────────────────────────────────┘

  DIM 5 — SOCIAL PROCESSING:
  ┌────────────┬───────────────────────────────────────────────────┐
  │ Tuổi       │ Observable indicators                             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 3-6        │ Parallel play vs interactive play preference      │
  │            │ Group size comfort: 1-2 vs 5+ friends             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 6-12       │ Group work: energized (high) vs drained (low)    │
  │            │ Recess behavior: group games vs solo/small pair    │
  │            │ Learning context: discuss = understand vs          │
  │            │ quiet = understand                                 │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 12-18      │ Study preference: group vs solo                   │
  │            │ Presentation: energized vs anxious                 │
  │            │ Peer influence: high (conform) vs low (independent)│
  ├────────────┼───────────────────────────────────────────────────┤
  │ 18+        │ Work style: collaborative vs independent          │
  └────────────┴───────────────────────────────────────────────────┘

  DIM 6 — BODY-BASE DOMINANCE:
  ┌────────────┬───────────────────────────────────────────────────┐
  │ Tuổi       │ Observable indicators                             │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 3-6        │ "Gut reactions": strong body signals (stomach,    │
  │            │ fidgeting) khi uncomfortable                      │
  │            │ Learn by doing first vs observing first            │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 6-12       │ "I just feel it" vs "I can explain why"          │
  │            │ Physical responses to new content: engaged body   │
  │            │ (lean forward, move) vs still processing          │
  │            │ Decision making: "feels right" vs "makes sense"   │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 12-18      │ Self-report: "tôi cảm nhận trước khi hiểu" vs   │
  │            │ "tôi hiểu trước khi cảm nhận"                    │
  │            │ Creative process: body-driven vs concept-driven    │
  ├────────────┼───────────────────────────────────────────────────┤
  │ 18+        │ Self-awareness about processing style             │
  └────────────┴───────────────────────────────────────────────────┘


TRIANGULATION — CÁCH COMBINE DATA:

  Teacher observe:   "Trong class, trẻ A engage nhất khi hands-on"
  Parent observe:    "Ở nhà, A luôn tháo đồ chơi ra rồi ráp lại"
  Self-report (10+): "Em thích làm hơn là nghe"
  AI data:           "A completes 2x faster in interactive vs reading tasks"
  → PATTERN: somatic-dominant → confidence HIGH

  Teacher observe:   "Trẻ B rất restless, khó ngồi yên"
  Parent observe:    "B cũng vậy ở nhà, nhưng chơi Lego 2 tiếng"
  → PATTERN: HIGH-VTA (cần novelty) + BUT CÓ THỂ focus khi ENGAGED
  → ≠ "ADHD" automatically → = needs novelty + interest-matched content
  → = Thêm data trước khi conclude

  ⚠️ CONFLICT giữa sources = THÔNG TIN QUAN TRỌNG:
    → Teacher: "B không tập trung" / Parent: "B focus tốt ở nhà"
    → = Environment difference → class environment = mismatch
    → ≠ "B có vấn đề" → = "class format cần adjust cho B"


  🟡 Toàn bộ observation framework = derived application
     Observable indicators = logical nhưng chưa validated as diagnostic tool
     Dùng as GUIDE, không phải as CLINICAL ASSESSMENT
```

---

## 3. CALIBRATION PER MAJOR DIMENSIONS

```
MỤC ĐÍCH SECTION NÀY:
  → §1 = CÁI GÌ (6 dimensions)
  → §2 = CÁCH NHẬN DIỆN (observe)
  → §3 = LÀM GÌ VỚI DATA ĐÓ (adjust)
  → = "Biết learner A = somatic-dominant + high-VTA → ADJUST thế nào?"


NGUYÊN TẮC CALIBRATION:

  ① ADJUST METHOD, KHÔNG ADJUST STANDARD
     → Depth target = GIỐNG cho tất cả (Mechanism v2.0 §2.9)
     → CÁCH đạt depth = KHÁC per hardware
     → "Mọi người đều phải biết đọc → CÁCH HỌC đọc = khác"

  ② LEVERAGE STRENGTH, SUPPLEMENT WEAKNESS
     → Dominant modality = CON ĐƯỜNG NHANH → dùng đó làm primary
     → Non-dominant = vẫn develop → nhưng SUPPLEMENT, không force primary
     → VD: somatic-dominant → learn math qua manipulatives (leverage)
       → rồi DẦN DẦN connect với abstract notation (supplement)

  ③ ADJUST DEGREES, KHÔNG SWITCH CATEGORIES
     → Không phải "learner A = Type X → program X"
     → Mà: "learner A thiên somatic → THÊM 20% hands-on, GIẢM 20% lecture"
     → = Fine-tuning, không phải overhaul
     → = Trong CÙNG classroom → differentiate, không separate

  ④ PFC BUDGET CONSTRAINT (PFC-Operations v1.1):
     → Calibration = PFC COST cho teacher: observe + hypothesize + test = shared PFC budget
     → 40 students × 6 DIM = 240 "knobs" → IMPOSSIBLE track all → PRIORITIZE
     → Start: identify EXTREME positions (5-6 students) → adjust TRƯỚC
     → Session design: high-PFC calibration (1-on-1) cần giới hạn thời lượng
     → Per-student: calibration activities cũng tốn PFC CỦA LEARNER → dosing matters

  ⑤ CALIBRATE SUBSIDY, KHÔNG CHỈ CONTENT (Entity-Valence-Dynamics.md v1.0 §5):
     → Teacher = MODERATE Hardware-Subsidy source cho learner
     → Per-hardware: cách learner "nhận" subsidy = KHÁC → adjust CÁCH tương tác
     → High body-base learner: physical proximity subsidy MẠNH hơn verbal praise
     → High social learner: group belonging = subsidy SOURCE → isolate = withdraw subsidy
     → = Adjust cả CONTENT (method/format) VÀ RELATIONSHIP (subsidy quality)

  ⑥ GAP LANDSCAPE NAVIGATION (Gap-Distribution-Profile v1.1):
     → Mỗi learner = 1 gap landscape riêng (4 trục: domain/origin/depth/stability)
     → Calibration = giúp learner NAVIGATE gap landscape, không ép 1 landscape
     → Per-hardware: gap landscape EVOLVES theo DIM profile
       → High-VTA: gap landscape = rộng + nông → cần guide DEPTH per domain
       → Low-VTA: gap landscape = hẹp + sâu → cần guide BREADTH exposure
     → = "Bản đồ gap" per-individual bổ sung "bản đồ hardware"
```

### DIM 1 — Modality Balance: Calibration

```
SOMATIC-DOMINANT LEARNER:

  Adjust Learning Method:
    → Primary channel: hands-on, building, movement, physical exploration
    → "Hiểu toán" = cắt pizza, dùng blocks, đo vật thật → RỒI abstract
    → "Hiểu lịch sử" = roleplay, visit, tạo model → RỒI đọc sách
    → Lab work, maker space, physical experiments = LEARNING TIME (không phải "giải lao")

  Adjust Assessment:
    → Demonstration ("chỉ cách con làm") > written test
    → Build/make something > write essay
    → Oral + show > silent written

  Adjust Bridge:
    → Physical accomplishment = strong bridge ("con ĐÃ LÀM ĐƯỢC cái này")
    → Movement breaks = NOT punishment → = RESET for somatic brain
    → Sitting still for 45 min = TORTURE cho somatic-dominant → = environment mismatch

  ⚠️ Sai lầm phổ biến:
    → "Ngồi im mới là học" → somatic-dominant KHÔNG learn khi sit still
    → "Hiếu động" = label → thật ra = somatic brain ĐANG CẦN input


VERBAL/VISUAL-DOMINANT LEARNER:

  Adjust Learning Method:
    → Primary channel: reading, diagrams, discussion, written analysis
    → Abstract concepts = CÓ THỂ tiếp cận SỚM hơn (PFC leverage verbal)
    → Verbal: lecture + discussion CÓ THỂ effective
    → Visual: diagrams, mind maps, video, spatial organization

  Adjust Assessment:
    → Written analysis, essays, verbal explanation = NATURAL
    → Nhưng: vẫn NÊN include experiential component (multi-modal = better for all)

  ⚠️ Sai lầm phổ biến:
    → System hiện tại = DESIGNED cho verbal/visual → nhóm này "giỏi" = confirmation bias
    → "Giỏi" ≠ "hardware fit system" → = "system fit hardware CỦA HỌ"
```

### DIM 2 — VTA Threshold: Calibration

```
HIGH-VTA LEARNER (novelty-seeking):

  Adjust Learning Method:
    → Format rotation: đổi format mỗi 15-20 phút
    → Project-based: mỗi project = NOVELTY source
    → Choice: cho chọn CÁCH approach task → novelty từ autonomy
    → Movement: physical + mental variety → VTA fire
    → Gamification: CÓ THỂ work → nhưng ⚠️ inflation risk (Mechanism v2.0 §3.1)

  Adjust Environment:
    → ĐỪNG ép sit still quá lâu → cho phép movement
    → Variety trong daily schedule → NOT same routine every day
    → Multiple projects CÙNG LÚC có thể OK (≠ "không tập trung")

  Adjust Bridge:
    → Curiosity = STRONG natural bridge → leverage
    → "Next thing" = natural reward → cho biết "sau này sẽ..."
    → Routine rewards = HABITUATE nhanh → vary rewards

  ⚠️ Common confusion:
    → High-VTA + boring environment = RESTLESS → label "ADHD"
    → Nhưng: high-VTA ≠ ADHD (ADHD = clinical, high-VTA = hardware tendency)
    → Many "ADHD" students = high-VTA + MONOTONOUS environment → mismatch
    → = Adjust environment TRƯỚC → nếu vẫn struggle → clinical assessment


LOW-VTA LEARNER (routine-comfortable):

  Adjust Learning Method:
    → Structured, sequential, predictable → COMFORTABLE
    → Deep dive: single topic for extended time = ENGAGING
    → Routine = OK → không cần đổi format liên tục
    → Clear expectations, step-by-step progression

  Adjust Environment:
    → Predictable schedule → LOW anxiety
    → Sudden change = DISRUPTIVE → prepare in advance

  Adjust Bridge:
    → Progress tracking = motivating (see advancement over time)
    → Mastery milestones = strong bridge
    → ≠ "Boring" → = "thorough"

  ⚠️ Common confusion:
    → Low-VTA + high-novelty environment = OVERWHELMED → label "anxious"
    → System biased toward variety → low-VTA = "không hòa nhập"
```

### DIM 3 — Cortisol Sensitivity: Calibration

```
HIGH CORTISOL SENSITIVITY:

  Adjust Pressure Level:
    → LOWER pressure than class average
    → Safe to fail: "sai = learn, không phải sai = punish"
    → Direction > Level (Mechanism v2.0 §2.2): LUÔN novelty-direction cho nhóm này
    → Prepare for changes: warn before transitions
    → Recovery time: MORE breaks, MORE downtime

  Adjust Assessment:
    → Low-stakes, frequent → NOT high-stakes, rare
    → Take-home options when possible
    → Oral in private > presentation in front of class
    → ⚠️ Exam performance ≠ actual knowledge (cortisol suppress PFC)
      → NẾU exam score << daily performance → cortisol issue, NOT knowledge issue
      → PFC Mode: Reallocation (PFC-Configuration.md) → performance DROP dưới capacity

  Adjust Bridge:
    → Imposed adult threat (Mechanism v2.0 §3.3 Type 3) = TUYỆT ĐỐI TRÁNH
    → Safety + curiosity = primary bridges
    → Social pressure = CŨNG là cortisol source → careful with group competition

  ⚠️ QUAN TRỌNG:
    → "Yếu đuối" = LABEL SAI → = cortisol baseline ĐÃ CAO
    → "Cần nghiêm hơn để rèn" = NGƯỢC LẠI → thêm pressure = thêm damage
    → Giải pháp: HẠ cortisol TRƯỚC → learning SẼ improve TỰ NHIÊN


LOW CORTISOL SENSITIVITY (resilient):

  Adjust Pressure Level:
    → CAN handle more challenge → thậm chí CẦN challenge
    → Too comfortable = cortisol quá thấp → bored
    → Moderate competition CÓ THỂ motivate
    → Deadlines, public milestones = OK

  ⚠️ Risk: "vì chịu được" ≠ "nên đè mạnh"
    → Resilient ≠ invincible → vẫn có inverted-U peak
    → Adjust = moderate-high, NOT maximum
```

### DIM 4 — PFC Development Pace: Calibration

```
FAST PFC (abstract early):

  Adjust Content Timing:
    → CÓ THỂ introduce abstract concepts SỚM hơn
    → Depth per domain CÓ THỂ push SỚM hơn
    → ⚠️ "Gifted" programs: cần DEPTH, không chỉ MORE content
      → Skip grade = more volume at same depth = MISS POINT
      → Better: same grade + deeper content + accelerated per domain

  Adjust Method:
    → Hypothetical reasoning, "what if", complex problems = ENGAGING
    → Concrete-only = BORING (PFC already ready for abstract)
    → Discussion, debate, independent research = LEVERAGE

  ⚠️ Risks:
    → "Easy" = bored → disengage → label "lazy" or "arrogant"
    → Social mismatch: cognitive advanced ≠ emotional advanced
      → May be doing calculus but still need emotional support of a 12-year-old


SLOW PFC (concrete longer — NORMAL, not deficit):

  Adjust Content Timing:
    → CONCRETE examples TRƯỚC abstract → LÂU hơn average
    → ⚠️ "Lâu hơn" ≠ "không thể" → = "cần thêm time + đúng method"
    → Manipulatives, visual aids, real-world examples = EXTENDED period

  Adjust Method:
    → Step-by-step, sequential → not "figure it out yourself" too early
    → More practice at each level before advancing
    → Multi-modal: if verbal doesn't work → try visual → try hands-on

  ⚠️ Risks:
    → "Kém" label = cortisol increase → PFC suppress MORE → vicious cycle
    → "Giữ lại lớp" = shame + cortisol → KHÔNG giải quyết root cause
    → Root cause: PFC chưa ready → WAIT + RIGHT METHOD, not punish
```

### DIM 5 — Social Processing: Calibration

```
HIGH SOCIAL NEEDS:

  Adjust Method:
    → Group work, pair work, peer teaching = LEVERAGE
    → Discussion-based learning = EFFECTIVE
    → Social recognition = strong bridge
    → Collaborative projects > solo assignments

  Adjust Environment:
    → Seating: groups/pairs > isolated desks
    → Peer interactions = LEARNING TIME, not distraction

  ⚠️ Risk: social = bridge → nếu peer group = negative influence
    → = Group composition MATTERS → intentional grouping


LOW SOCIAL NEEDS:

  Adjust Method:
    → Solo projects, independent research = EFFECTIVE
    → 1-on-1 with mentor > group discussion
    → Written communication > oral presentation (less social stress)
    → Deep focus time = PROTECTED (not interrupted by group activities)

  Adjust Environment:
    → Quiet space available → not FORCED into groups always
    → Choice: "group or solo?" → let learner choose when possible

  ⚠️ Risk: "anti-social" label → isolation → miss social SKILL development
    → Low social NEEDS ≠ no social SKILLS needed
    → Still NEED social skills → just learn them DIFFERENTLY (smaller doses, 1-on-1)
```

### DIM 6 — Body-Base Dominance: Calibration

```
HIGH BODY-BASE:

  Adjust Method:
    → Experience FIRST → theory SECOND
    → "Làm thử → rồi giải thích tại sao" > "Giải thích → rồi làm"
    → Physical engagement = PROCESSING (fidgeting CÓ THỂ = thinking)
    → Art, craft, sports, cooking = LEARNING CHANNELS, not extras

  Adjust Assessment:
    → "Show me" > "Tell me" > "Write it"
    → Performance, demonstration, creation = NATURAL assessment

  ⚠️ VN context: system = verbal-dominant → body-base learners = INVISIBLE
    → "Giỏi thể thao, kém học" = system ĐÁNH GIÁ SAI → not "kém" → "khác channel"


LOW BODY-BASE (PFC-first):

  Adjust Method:
    → Concept FIRST → application SECOND
    → Reading, analysis, logical reasoning = NATURAL
    → Still NEEDS experiential component (multi-modal = better for ALL)
      → But can START from concept → verify with experience

  ⚠️ Risk: PFC-first ≠ body-unaware → develop body-base AS SUPPLEMENT
    → May miss body signals (burnout, stress) because PFC overrides
    → = Teach body-awareness explicitly
```

```
TỔNG HỢP — CALIBRATION MATRIX:

  ┌──────────────┬──────────────────────┬──────────────────────┐
  │ Dimension    │ Adjust WHAT           │ Adjust HOW           │
  ├──────────────┼──────────────────────┼──────────────────────┤
  │ ① Modality   │ Input/output format  │ Match dominant →     │
  │              │                       │ supplement others    │
  │ ② VTA        │ Novelty/routine      │ Variety vs structure │
  │              │ balance               │ in daily schedule    │
  │ ③ Cortisol   │ Pressure level       │ Safe vs challenging  │
  │              │                       │ per individual       │
  │ ④ PFC pace   │ Abstract timing      │ Concrete → abstract  │
  │              │                       │ transition speed     │
  │ ⑤ Social     │ Group vs solo        │ Learning context     │
  │              │ balance               │ composition          │
  │ ⑥ Body-base  │ Experience vs concept │ Sequence: do-first   │
  │              │ sequence              │ vs think-first       │
  └──────────────┴──────────────────────┴──────────────────────┘

  = 6 "knobs" to turn per individual
  = KHÔNG phải 6 categories → = 6 CONTINUUMS
  = Adjust DEGREES, not PROGRAMS
  = Within SAME classroom → differentiate, not segregate

  + 3 CROSS-CUTTING ADJUSTMENTS (v1.1):
  = ④ PFC Budget: adjust session DOSING (teacher + learner PFC finite)
  = ⑤ Hardware-Subsidy: adjust RELATIONSHIP quality per hardware
  = ⑥ Gap Landscape: adjust NAVIGATION per-individual gap profile


  🟡 Calibration strategies = framework-derived
     Logical + consistent with mechanisms + aligned with differentiated instruction research
     Nhưng: chưa validated AS THIS SPECIFIC FRAMEWORK trong controlled studies
```

---

## 4. NEURODIVERSITY — HARDWARE VARIATION, NOT "DISORDER"

```
REFRAME CỐT LÕI:

  Neurodiversity = HARDWARE VARIATION trên cùng 6 dimensions
    → ADHD, ASD, Gifted, Dyslexia... = EXTREME positions trên spectrum
    → KHÔNG phải "bệnh" (trừ khi gây suffering) → = "cấu hình khác"
    → CÙNG principles, KHÁC calibration settings

  🔗 Sensitivity-Classification.md v1.0:
    → Tầng 1 = Sensory-Driven Direct-State input (hardware sensitivity)
    → Tầng 2 = Zone B/C processing (amplification)
    → Neurodivergent individuals: thường ở EXTREME sensitivity positions
    → = Hardware sensitivity × environment = thresholds KHÁC

  ⚠️ QUAN TRỌNG:
    → File này KHÔNG thay thế clinical diagnosis hoặc specialist
    → File = FRAMEWORK LENS → giúp HIỂU qua hardware mechanism
    → Clinical assessment = NEEDED cho intervention cụ thể
    → Framework + clinical = COMPLEMENT, không thay thế nhau

  ⚠️ THẬN TRỌNG:
    → "Neurodiversity = not disorder" KHÔNG có nghĩa "không cần support"
    → Extreme hardware positions = CẦN support NHIỀU HƠN average
    → "Variation, not disorder" = NHÌN KHÁC, không phải IGNORE difficulties
```

### ADHD — VTA + Cortisol Profile

```
QUA FRAMEWORK LENS 🟡:

  ADHD = extreme position trên DIM 2 (VTA) + có thể DIM 3 (cortisol):
    → Very high VTA threshold → detect biến động LỚN only
    → Routine, monotony = VTA KHÔNG fire → "không tập trung"
    → Nhưng: INTERESTING task = HYPERFOCUS (VTA fire mạnh khi match)
    → = Không phải "thiếu attention" → "attention CHỌN LỌC theo novelty threshold"

  🟢 Neuroscience basis:
    → DRD4-7R prevalence cao hơn trong ADHD population
    → Dopamine signaling differences = established
    → Executive function differences = established

  CALIBRATION cho ADHD (framework-based):
    → VTA dimension: EXTREME novelty needs
      → Format rotation NHIỀU hơn average (mỗi 10-15 phút)
      → Movement = ESSENTIAL (không phải optional)
      → Choice + autonomy → novelty từ control
      → Interest-based learning → VTA fire → CAN focus
    → Cortisol dimension: often ALSO sensitive
      → Imposed threat (Type 3) = ESPECIALLY harmful (double whammy)
      → Positive reinforcement = more effective (nhưng varies → inflation risk)
    → Assessment: varied formats, untimed options, movement-allowed
    → Bridge: curiosity >>> threat / short-term goals > long-term

  ⚠️ ADHD ≠ "chỉ cần environment tốt là hết"
    → Environment adjustment = HELP SIGNIFICANTLY
    → Nhưng: severe ADHD CÓ THỂ cần medication + specialist support
    → Framework = 1 lens → NOT complete treatment plan
    → = "Adjust environment FIRST → nếu insufficient → clinical support"
```

### ASD — Social Processing + Sensory Profile

```
QUA FRAMEWORK LENS 🟡:

  ASD = extreme position trên DIM 5 (social) + DIM 1 (modality/sensory):
    → Social processing: KHÁC (không thiếu, khác mechanism)
    → Self-Pattern-Modeling v3.1 (Agent-Mechanism.md v2.1): calibrated DIFFERENTLY
      → Không phải "thiếu empathy" → empathy QUA MECHANISM KHÁC
    → Sensory profile: often EXTREME sensitivity (hyper or hypo per modality)
    → = Social bridges (peer approval, group belonging) = WORK DIFFERENTLY
    → = Sensory environment = CRITICAL for learning capacity

  🟢 Neuroscience basis:
    → Social brain differences = established
    → Sensory processing differences = established
    → Self-Pattern-Modeling function differences = framework lens (replacing "mirror neuron" framing)

  CALIBRATION cho ASD (framework-based):
    → Social dimension: EXTREME (khác, không thiếu)
      → Solo/1-on-1 = PRIMARY learning context
      → Group work = CÓ THỂ nhưng STRUCTURED, predictable, PREPARED
      → Social bridges (peer approval) = WEAK → dùng bridge khác
      → Interest-based bridge = often VERY STRONG (special interests = VTA match)
    → Modality dimension: often EXTREME sensory sensitivity
      → Sensory audit of learning environment: lights, sounds, textures
      → Sensory overload = cortisol spike → PFC Mode shift (Reallocation/Reconfigured)
        → cannot learn
      → = CONTROL ENVIRONMENT FIRST → learning becomes POSSIBLE
    → Assessment: accommodate sensory + social needs
      → Written > oral presentation (if social anxiety)
      → Familiar environment > new environment
      → Clear, explicit instructions (implicit social cues = harder to read)

  ⚠️ ASD spectrum = WIDE → calibration varies ENORMOUSLY
    → "Level 1" (old Asperger's) → minimal adjustment needed
    → Higher support needs → significant environmental modification
    → = Per-individual within ASD population ALSO needed
```

### Gifted — Accelerated PFC

```
QUA FRAMEWORK LENS 🟡:

  Gifted = extreme position trên DIM 4 (PFC pace):
    → PFC develops FASTER → abstract thinking EARLIER
    → Working memory HIGHER → can handle complex problems EARLIER
    → ⚠️ Cognitive advanced ≠ emotionally advanced
    → = "13-year-old brain doing 18-year-old math but needing 13-year-old emotional support"

  CALIBRATION cho Gifted (framework-based):
    → PFC dimension: ACCELERATED
      → DEPTH not VOLUME: deeper content, not just more content
      → "Skip grade" = volume → MISS social-emotional development
      → "Enrich within grade" = depth + social → BETTER
      → Independent research, mentorship, advanced problems within domain
    → VTA dimension: often ALSO high (bored easily with routine content)
      → Novelty from DEPTH → "deeper = newer"
      → Challenge = bridge (moderate difficulty = VTA fire)
    → Social dimension: VARIES
      → Some = social, some = solo → per-individual
      → "Gifted program" grouping = CÓ THỂ help (intellectual peers)
    → Assessment: MUST measure DEPTH, not just speed
      → Fast correct answers = CHƯA ĐỦ → "can you CREATE something new?"

  ⚠️ Common mistakes:
    → "Gifted = don't need help" → WRONG → need DIFFERENT help
    → "Gifted = good at everything" → WRONG → can be VERY uneven profile
    → "Bored = lazy" → WRONG → bored = UNDER-STIMULATED (PFC not engaged)
    → "Just give harder work" → partial → need DEEPER, not just HARDER
```

### Learning Differences — Per-Mechanism Adjustment

```
QUA FRAMEWORK LENS 🟡:

  Learning differences = specific MECHANISM differences:

  DYSLEXIA:
    → Modality: visual-verbal PROCESSING difference (not "vision problem")
    → Phonological processing differs → reading acquisition = HARDER
    → Framework: DIM 1 (modality) extreme → verbal/written channel = SLOWER
    → Calibration:
      → Multi-sensory reading instruction (Orton-Gillingham approach)
        → 🟢 Evidence-based for dyslexia
      → Audio supplements for text-heavy content
      → Assessment: oral option, extra time for reading-based tasks
      → ⚠️ "Kém đọc" ≠ "kém hiểu" → depth CÓ THỂ cao nếu access đúng channel

  DYSCALCULIA:
    → Modality: number/quantity PROCESSING difference
    → Framework: specific chunk compilation difficulty for numerical domain
    → Calibration:
      → CONCRETE representations EXTENDED (manipulatives lâu hơn average)
      → Visual-spatial approaches cho number concepts
      → Step-by-step, explicit instruction
      → Assessment: process-focused (cách làm) > answer-focused

  DYSGRAPHIA:
    → Motor/writing PROCESSING difference
    → Framework: DIM 1 (motor modality) difference
    → Calibration:
      → Typing as alternative to handwriting
      → Oral assessment as alternative to written
      → Separate WRITING skill from THINKING skill in assessment


NGUYÊN TẮC CHUNG CHO MỌI LEARNING DIFFERENCES:

  ① CHANNEL KHÁC, KHÔNG PHẢI CAPACITY KHÁC
     → Dyslexia = "đọc KHÓ HƠN" ≠ "hiểu KÉM HƠN"
     → Dyscalculia = "toán KHÓ HƠN" ≠ "logic KÉM HƠN"
     → = BYPASS channel khó → ACCESS depth qua channel khác

  ② EARLY IDENTIFICATION = CRITICAL
     → Sớm phát hiện → sớm adjust → GIẢM gap
     → Muộn phát hiện → gap tích lũy → khó compensate
     → + LATE identification = years of "kém" label = cortisol damage ON TOP

  ③ EVIDENCE-BASED INTERVENTIONS EXIST
     → Dyslexia: multi-sensory instruction 🟢 evidence
     → = Framework ALIGNED with evidence-based practice → NOT replace it

  🟡 Neurodiversity section = framework lens application
     Consistent with established neurodiversity research
     nhưng KHÔNG thay thế clinical assessment + specialist intervention
     = "Hiểu QUA mechanism → inform APPROACH → specialist IMPLEMENT"
```

---

## 5. COMMON MISCALIBRATIONS — LABELS SAI PHỔ BIẾN

```
MỤC ĐÍCH:
  → Phần lớn "problem students" = MISCALIBRATED SYSTEM, không phải "broken student"
  → Section này: từ LABEL phổ biến → TRACE BACK về hardware mismatch
  → = "Chẩn đoán ngược" — hệ thống gán nhãn SAI → trẻ chịu hậu quả

  PATTERN:
    Label → (thật ra) → hardware dimension X + environment mismatch
    → Nếu adjust environment → "vấn đề" GIẢM hoặc BIẾN MẤT
    → = "Vấn đề" nằm ở CALIBRATION, không ở LEARNER
```

### "LƯỜI" (Lazy)

```
LABEL: "Con này lười, không chịu học"
FREQUENCY: CỰC phổ biến — gần như mọi culture

TRACE BACK — thật ra CÓ THỂ là:

  ① KHÔNG CÓ IMAGINE-FINAL (Mechanism v2.0 §2.6):
     → Trẻ không biết TẠI SAO phải học cái này
     → Body: "không thấy lý do → không có drive → tại sao phải effort?"
     → Fix: giúp trẻ THẤY "khi biết cái này → cuộc sống tôi thế nào"
     → ≠ "Ép chăm hơn" → = "cho thấy LÝ DO"

  ② BRIDGE SAI (Mechanism v2.0 §3):
     → Bridge hiện tại KHÔNG match hardware
     → VD: threat bridge cho trẻ high-cortisol → freeze → "lười"
     → VD: routine bridge cho trẻ high-VTA → bored → "lười"
     → Fix: đổi LOẠI bridge, không tăng LƯỢNG bridge

  ③ WRONG METHOD (Mechanism v2.0 §2.2 + §2.3):
     → Phương pháp không match hardware
     → VD: lecture-only cho trẻ somatic-dominant → not engaging → "lười"
     → VD: abstract too early cho trẻ slow-PFC → can't follow → give up → "lười"
     → Fix: adjust method per hardware

  ④ CORTISOL QUÁ CAO (Cortisol v2.1 — Role ④ Inertia):
     → Trẻ đã ở descending limb of inverted-U → PFC suppress
     → Biểu hiện: shutdown, withdrawal, "không muốn làm gì"
     → Trông giống "lười" → thật ra = FREEZE response
     → Fix: HẠ cortisol TRƯỚC → motivation sẽ return

  ⑤ FORCED-FIT STATE:
     → Direction SAI hardware → body: "đây không phải con đường của mình"
     → Resistance = body signal "mismatch" → label = "lười"
     → Fix: reassess direction, cho EXPLORE, tìm TRUE alignment

  = "LƯỜI" = CATCH-ALL LABEL cho MỌI loại miscalibration
  = Gần như KHÔNG BAO GIỜ đúng nguyên nhân là "learner thiếu ý chí"
  = FIX: trace back → tìm ROOT CAUSE per individual → adjust
```

### "KÉM" / "NGU" (Stupid / Slow)

```
LABEL: "Con này kém, không hiểu nổi"
FREQUENCY: Phổ biến — đặc biệt trong high-pressure systems

TRACE BACK:

  ① WRONG TIMING — PFC chưa ready (DIM 4):
     → Ép abstract khi PFC chưa đủ → "không hiểu"
     → Đặc biệt: toán abstract ở 6-8 tuổi → nhiều trẻ "ghét toán"
     → Thật ra: PFC cần CONCRETE lâu hơn → CHẬM hơn ≠ KÉM hơn
     → Fix: concrete examples → abstract DẦN DẦN, patience

  ② WRONG CHANNEL (DIM 1):
     → Content deliver qua verbal → trẻ somatic-dominant → "không hiểu"
     → Thật ra: CÓ THỂ hiểu NẾU deliver qua hands-on
     → Fix: multi-modal delivery, leverage dominant channel

  ③ MISSING PREREQUISITE (Mechanism v2.0 §2.4):
     → Chunk hierarchy: complex cần simple base → base YẾU → complex KHÔNG vào
     → "Không hiểu phân số" có thể = "chưa thật sự hiểu phép chia"
     → Fix: trace back foundation gaps → fill → rồi advance

  ④ CORTISOL-INDUCED PFC SUPPRESS (DIM 3):
     → High cortisol → PFC hoạt động DƯỚI capacity
     → Exam: cortisol spike → "không nhớ gì" → "kém"
     → Daily: chronic stress → PFC chronically suppressed → "kém LIÊN TỤC"
     → Fix: hạ cortisol → PFC RECOVER → performance TĂNG

  ⑤ LEARNING DIFFERENCE chưa identified (§4):
     → Dyslexia → "đọc kém" → label "kém" toàn diện
     → Thật ra: đọc = 1 channel → intelligence + depth = INTACT
     → Fix: identify specific difference → accommodate → ACCESS depth

  = "KÉM" = almost always ENVIRONMENT MISMATCH or MISSING SUPPORT
  = True "low capacity" = RẤT HIẾM → phần lớn = miscalibrated system
```

### "HIẾU ĐỘNG" / "KHÔNG TẬP TRUNG" (Hyperactive / Can't focus)

```
LABEL: "Con này hiếu động, không tập trung được"
FREQUENCY: Tăng mạnh gần đây — label ADHD tăng nhanh

TRACE BACK:

  ① HIGH-VTA + MONOTONOUS ENVIRONMENT (DIM 2):
     → VTA threshold cao → cần novelty → class monotone → restless
     → = Brain ĐANG TÌM novelty vì environment KHÔNG CUNG CẤP
     → Fix: format rotation, movement, variety, project-based

  ② SOMATIC-DOMINANT + SIT-STILL ENVIRONMENT (DIM 1):
     → Body CẦN movement để process → forced still → fidget, squirm
     → = Body ĐANG CỐ PROCESS nhưng bị restrict → "hiếu động"
     → Fix: movement breaks, hands-on learning, standing desks

  ③ ACTUAL ADHD (§4):
     → EXTREME VTA position → environment adjustment KHÔNG ĐỦ
     → = Clinical assessment needed → medication + specialist support
     → ⚠️ Nhưng: NHIỀU trẻ được diagnose ADHD = actually ① hoặc ②
       → Over-diagnosis = real problem trong nhiều countries

  ④ ANXIETY-DRIVEN (DIM 3):
     → High cortisol → can't focus vì brain ở threat mode
     → "Không tập trung" = actually "đang tập trung vào SURVIVAL"
     → Fix: address cortisol source → focus RETURNS

  = QUY TRÌNH ĐÚNG:
    → Step 1: adjust environment (novelty, movement, method) → observe
    → Step 2: nếu vẫn struggle → specialist assessment
    → Step 3: diagnosis + environment adjustment + medication nếu cần
    → ≠ "Label ADHD → medication" ngay từ đầu
```

### "KHÔNG CÓ ĐỘNG LỰC" (Unmotivated)

```
LABEL: "Con này không có động lực học"
FREQUENCY: CỰC phổ biến — đặc biệt Stage 3 (12-18)

TRACE BACK:

  ① KHÔNG CÓ IMAGINE-FINAL — phổ biến NHẤT (Mechanism v2.0 §2.6):
     → "Tại sao phải học cái này?" → không ai trả lời THUYẾT PHỤC
     → Body: "không thấy đích → không có drive"
     → ≠ "Thiếu động lực" → = "THIẾU LÝ DO"
     → Fix: help build Imagine-Final — exposure, experience, discussion

  ② BRIDGE-DEPENDENT + BRIDGE RÚT (Mechanism v2.0 §3.4):
     → 12 năm "học vì điểm" → vào giai đoạn bridge giảm → motivation COLLAPSE
     → = "Động lực" thật ra = bridge (nguồn ④) → bridge rút → không còn gì
     → Fix: build intrinsic drive ①②③ (NÊN LÀM TỪ SỚM)

  ③ FORCED-FIT — direction KHÔNG match:
     → Hardware nói X, system ép Y → body resist → "không muốn"
     → = ĐÚNG: body ĐANG BÁO "đây không phải đường của mình"
     → Fix: reassess direction, cho EXPLORE alternatives

  ④ BURNOUT — cortisol overload sau nhiều năm:
     → High-pressure system → chronic cortisol → PFC exhaust → shutdown
     → Trông giống "unmotivated" → thật ra = "burned out"
     → Fix: recovery TRƯỚC → rồi mới rebuild direction

  = "UNMOTIVATED" = hầu luôn = system FAILED to provide:
    Imagine-Final (lý do) + đúng bridge + đúng direction + cortisol phù hợp
```

```
TỔNG HỢP — LABELS → ROOT CAUSES:

  ┌────────────────────┬───────────────────────────────────────────┐
  │ Label              │ Root causes (trace back)                  │
  ├────────────────────┼───────────────────────────────────────────┤
  │ "Lười"             │ No Imagine-Final / wrong bridge /         │
  │                    │ wrong method / cortisol / Forced-Fit      │
  ├────────────────────┼───────────────────────────────────────────┤
  │ "Kém/Ngu"          │ Wrong timing / wrong channel / missing    │
  │                    │ prerequisite / cortisol / unidentified LD │
  ├────────────────────┼───────────────────────────────────────────┤
  │ "Hiếu động"        │ High-VTA + monotone / somatic + sit /    │
  │                    │ actual ADHD / anxiety-driven              │
  ├────────────────────┼───────────────────────────────────────────┤
  │ "Không động lực"   │ No Imagine-Final / bridge-dependent /    │
  │                    │ Forced-Fit / burnout                      │
  └────────────────────┴───────────────────────────────────────────┘

  PATTERN: mỗi label = nhiều possible root causes
  → LABEL = KHÔNG GIÚP fix → chỉ ĐÓNG KHUNG learner
  → TRACE BACK = tìm root cause → CÓ THỂ fix
  → = "Đừng hỏi 'trẻ có VẤN ĐỀ gì' → hỏi 'system ĐANG MISS gì cho trẻ này'"


  🔗 DISSONANCE SIGNAL ARCHITECTURE LENS (v1.0):

  Mỗi miscalibration ở trên → tạo DISSONANCE. Nhưng loại nào?

  → Evaluative Dissonance (compiled, workable by REFRAME):
    "Lười" ①② = chưa có Imagine-Final, bridge sai → REFRAME direction/bridge = giải quyết
    "Kém" ③ = missing prerequisite → FILL prerequisite = unblock
    "Không động lực" ①②③ = thiếu lý do / bridge sai / Forced-Fit → REFRAME possible

  → Direct-State Dissonance (hardware, needs REST not reframe):
    "Lười" ④ = cortisol quá cao → body ĐANG CẦN recovery → reframe KHÔNG GIÚP
    "Kém" ④ = cortisol suppress PFC → REST trước, learn SAU
    "Không động lực" ④ = burnout → recovery TRƯỚC mọi thứ

  → COMPOUND (Evaluative + Direct-State cùng lúc):
    = Trường hợp KHÓ NHẤT: vừa thiếu direction VỪA body kiệt sức
    = PHẢI address Direct-State TRƯỚC (rest) → rồi mới Evaluative (reframe)
    = ≠ "Vừa nghỉ vừa thúc" → nghỉ TRƯỚC, thúc SAU

  → Teacher cần DISTINGUISH: learner đang Evaluative hay Direct-State?
    = Evaluative: "tôi không muốn" → CÓ THỂ discuss, explore, reframe
    = Direct-State: "tôi không thể" → CẦN rest, recovery, environment adjust
    = Body signals KHÁC: Evaluative = mental resistance / Direct-State = physical signs
```

---

## 6. PRACTICAL CALIBRATION PROCESS

```
MỤC ĐÍCH:
  → Step-by-step: từ "hiểu lý thuyết" → "LÀM trong thực tế"
  → QUY TRÌNH, không phải one-time action
  → = Continuous cycle: observe → hypothesize → test → adjust → monitor


5-STEP CALIBRATION CYCLE:

  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │   ① OBSERVE                                                     │
  │   ↓                                                              │
  │   ② HYPOTHESIZE                                                  │
  │   ↓                                                              │
  │   ③ TEST (small adjustment)                                      │
  │   ↓                                                              │
  │   ④ EVALUATE (did it help?)                                      │
  │   ↓                                                              │
  │   ⑤ ADJUST or KEEP                                               │
  │   ↓                                                              │
  │   → back to ① (continuous)                                       │
  │                                                                  │
  └──────────────────────────────────────────────────────────────────┘


STEP 1 — OBSERVE:
  → Dùng indicators từ §2 per dimension
  → Triangulation: teacher + parent + self-report (when old enough) + AI data
  → Duration: ≥ 2-4 tuần liên tục (không snapshot 1 ngày)
  → Record: ghi chú BEHAVIOR, không ghi LABEL
    → ✅ "A đứng dậy 6 lần trong 45 phút, engage mạnh khi hands-on"
    → ❌ "A hiếu động, không tập trung"

STEP 2 — HYPOTHESIZE:
  → Từ observation pattern → đoán hardware profile TẠM
  → VD: "A có thể: somatic-dominant + high-VTA + moderate cortisol"
  → ⚠️ Hypothesis, KHÔNG phải diagnosis → sẵn sàng sai
  → Có thể dùng 6-dimension checklist (§1) để estimate

STEP 3 — TEST (small adjustment):
  → Thử THAY ĐỔI NHỎ dựa trên hypothesis
  → VD hypothesis "A = somatic-dominant":
    → Test: cho A hands-on version của CÙNG bài → observe response
    → Nếu engagement TĂNG rõ → hypothesis likely đúng
    → Nếu KHÔNG đổi → hypothesis sai → thử dimension khác
  → ⚠️ Thay đổi NHỎ → một biến ĐỔI mỗi lần → biết CÁI GÌ tạo effect
  → ≠ "Thay đổi toàn bộ method cùng lúc" → không biết cái gì work

STEP 4 — EVALUATE:
  → Sau 1-2 tuần test → evaluate:
    → Engagement thay đổi? (observation)
    → Learning outcome thay đổi? (assessment — Mechanism v2.0 §2.9)
    → Trẻ tự report thay đổi? (when old enough)
  → Nếu POSITIVE → adjustment likely correct → continue
  → Nếu NEUTRAL → thử adjustment khác
  → Nếu NEGATIVE → revert + re-hypothesize

STEP 5 — ADJUST or KEEP:
  → Positive result → KEEP adjustment + refine
  → Continue observing → hardware profile EVOLVES
  → Mỗi semester / mỗi year: REVIEW full profile
  → Puberty (Stage 3): MAJOR re-observation needed (hormonal shift)


PER-STAGE TOOLS:

  ┌──────────┬─────────────────────────────────────────────────────┐
  │ Stage    │ Primary tools                                       │
  ├──────────┼─────────────────────────────────────────────────────┤
  │ 1 (0-6)  │ Parent observation (play, behavior, preferences)    │
  │          │ Pediatric milestones (developmental markers)        │
  │          │ ⚠️ No formal assessment → observe ONLY              │
  ├──────────┼─────────────────────────────────────────────────────┤
  │ 2 (6-12) │ Teacher observation (class behavior, engagement)    │
  │          │ Parent observation (home behavior, interests)        │
  │          │ Learning response data (which methods → engagement)  │
  │          │ AI tools: learning pace, error patterns (emerging)   │
  │          │ Self-report begins (~10+): "tôi thích khi..."      │
  ├──────────┼─────────────────────────────────────────────────────┤
  │ 3 (12-18)│ Above + self-assessment grows DOMINANT              │
  │          │ Interest mapping: "tôi engage NHẤT khi..."          │
  │          │ Meta-learning: "tôi học tốt nhất bằng cách..."     │
  │          │ ⚠️ REASSESS at puberty onset (profile có thể shift) │
  ├──────────┼─────────────────────────────────────────────────────┤
  │ 4 (18+)  │ Self-assessment = PRIMARY                           │
  │          │ Mentor feedback                                      │
  │          │ Performance data (real-world)                        │
  │          │ AI analytics (learning patterns, productivity)       │
  └──────────┴─────────────────────────────────────────────────────┘


ROLE COLLABORATION:

  → Teacher: observe trong class → note behavior patterns → TEST adjustments
  → Parent: observe ở nhà → share data với teacher → COMPLEMENT school obs
  → Learner (10+): self-report → grows to self-assessment → eventually SELF-CALIBRATE
  → AI tools: data patterns → flag anomalies → suggest adjustments (era-specific)
    → Mechanism v2.0 §4: AI = Layer 1 generate + flag, Teacher = Layer 2 calibrate
  → Specialist: khi standard adjustment KHÔNG ĐỦ → clinical assessment

  = TEAM EFFORT, không phải 1 person's job
  = Data SHARING giữa roles = CRITICAL (hiện tại gần như KHÔNG CÓ)


  🔗 ENTITY-ACCESS LENS (Entity-Access v1.2):
     Calibration accuracy = f(Entity-Access level between teacher and student):
     → Mức 0-1 (Tool/Familiar): learner = anonymous → calibration IMPOSSIBLE
       → "Lớp 40 người, không biết tên" → calibration chưa bắt đầu
     → Mức 2 (Predictable): teacher biết patterns → observation BẮT ĐẦU có ý nghĩa
       → Cần ~40-80h interaction → calibration cycle ① BẮT ĐẦU
     → Mức 3 (Influential): teacher influence learner's DIM expression → adjustment EFFECTIVE
       → Cần ~80-200h → calibration cycle ④⑤ mới thực sự work
     → Implication: short-term teacher (< 1 semester) = calibration stays SUPERFICIAL
     → = Hệ thống cần DESIGN cho teacher-student TIME đủ lâu

  🔗 ENTITY-COMPILED LENS (Entity-Compiled v1.0):
     → Teacher trở thành COMPILED ENTITY trong student's system (40→200h)
     → Compiled teacher → student's body RECOGNIZES patterns → subsidy EFFECTIVE
     → Teacher compiled model CỦA student cũng build dần → calibration ACCURATE hơn
     → Short rotation (mỗi năm đổi teacher) = Entity-Compiled chưa kịp form fully
       → Calibration data MẤT → teacher mới bắt đầu lại từ Mức 0
       → = Trade-off: rotation (avoid novelty saturation) vs continuity (Entity-Compiled forms)
     → Ideal: teacher-student relationship ≥ 2 năm cho calibration sâu


PRACTICAL CONSTRAINTS:

  → 1 teacher : 40 students → per-individual observation = KHÓ
    → Nhưng: KHÔNG CẦN chi tiết 6 dimensions cho tất cả ngay
    → Start: identify 5-6 students ở EXTREME positions → adjust TRƯỚC
    → Dần: mở rộng observation → per-individual profile builds over time
    → AI tools: CÓ THỂ automate phần data collection → teacher focus on interpretation

  → Parent không available / không cooperation
    → System phải COMPENSATE: teacher observation + AI data = enough to START
    → Parent data = BONUS, not prerequisite

  → Time constraints
    → Observation = embedded trong teaching (không phải THÊM việc)
    → "Trong khi dạy → OBSERVE: ai engage, ai not, khi nào, với format nào"
    → = Re-frame teaching: teaching = ALSO observing = ALSO calibrating


  🟡 Practical process = framework application
     Consistent with RTI (Response to Intervention) model 🟢
     và differentiated instruction research 🟢
     Nhưng: 6-dimension specific framework = chưa validated trong field
```

---

## 7. HONEST ASSESSMENT + KẾT NỐI

```
⭐ CÁI FILE NÀY CÓ THỂ LÀM:

  ✅ Define 6 hardware dimensions relevant cho education
     → Từ Core framework → translated sang observable dimensions
  ✅ Cung cấp observable indicators per dimension per age
     → Practical checklist cho teacher + parent
  ✅ Cung cấp calibration strategies per dimension
     → "Biết hardware A → adjust thế nào"
  ✅ Reframe neurodiversity qua hardware lens
     → ADHD, ASD, Gifted, Learning differences = hardware variation
  ✅ Expose common miscalibrations (labels sai)
     → "Lười", "kém", "hiếu động", "unmotivated" → trace back root causes
  ✅ Cung cấp practical 5-step calibration process
     → Observe → hypothesize → test → evaluate → adjust


⭐ CÁI FILE NÀY KHÔNG THỂ LÀM:

  ❌ Thay thế clinical diagnosis
     → File = framework LENS → ADHD/ASD/LD diagnosis = clinical specialist
  ❌ Cho biết hardware profile CHÍNH XÁC per individual
     → Observation = approximate, not precise → behavior = noisy signal
  ❌ Guarantee adjustment sẽ work
     → 5-step process = ITERATIVE → human complexity > any framework
  ❌ Work trong mọi context không cần adapt
     → 40 students/class ≠ 15 students/class → tools KHÁC
  ❌ Cover TẤT CẢ relevant dimensions
     → 6 dimensions = framework selection → CÓ THỂ thiếu


⭐ ĐỘ TIN CẬY:

  CAO 🟢→🟡:
    → §1: 6 dimensions based on established neuroscience mechanisms
      → Modality, VTA/DRD4, cortisol, PFC development, social brain = 🟢
      → Educational implications per dimension = 🟡
    → §4: Neurodiversity mechanisms (ADHD/dopamine, ASD/social, etc.) = 🟢
      → Framework interpretation = 🟡

  TRUNG BÌNH 🟡:
    → §2: Observable indicators = logical, consistent → chưa validated as protocol
    → §3: Calibration strategies = derived, consistent with differentiated instruction
    → §5: Miscalibrations = pattern analysis → needs prospective validation
    → §6: 5-step process = aligned with RTI model 🟢 → 6-dimension specific = 🟡
    → Hardware-Subsidy observation response = derived from Entity-Valence-Dynamics.md v1.0
    → Compiled Quality as observation lens = derived from PFC-Operations v1.1
    → Dissonance-Signal-Architecture miscalibration reframe (Evaluative vs Direct-State) = derived from Dissonance-Signal-Architecture v1.0
    → Entity-Access calibration accuracy model = derived from Entity-Access v1.2
    → Entity-Compiled teacher accuracy model = derived from Entity-Compiled v1.0
    → PFC Budget calibration constraint = derived from PFC-Operations v1.1
    → Gap-Distribution-Profile per-individual gap landscape = derived from Gap-Distribution-Profile v1.1
    → Body-Feedback-Label 3-tier observation precision = framework convention, logical

  THẤP HƠN 🔴:
    → "6 dimensions = ĐỦ cho education calibration" = claim chưa proven
    → Body-base dominance spectrum = framework concept, limited empirical support
    → Specific calibration recommendations = best guesses, not proven protocols
    → Gap landscape navigation per DIM = plausible framework inference


⭐ RỦI RO:

  ⚠️ OVER-SIMPLIFICATION:
     → 6 dimensions cho TOÀN BỘ human variation = simplified
     → Interaction GIỮA dimensions = complex (chưa model đầy đủ)
     → VD: high-VTA + high-cortisol = rất khác high-VTA + low-cortisol

  ⚠️ FALSE PRECISION:
     → Observable indicators CÓ THỂ tạo cảm giác "chính xác"
     → Thật ra: observation = NOISY, interpretation = SUBJECTIVE
     → = Dùng as GUIDE + ITERATE, không phải as DIAGNOSIS

  ⚠️ LABEL RISK (ironic):
     → File cảnh báo "đừng label" → nhưng 6 dimensions CÓ THỂ trở thành labels
     → "A là high-VTA" = new label → same problem
     → = LUÔN dùng: "hiện tại A RESPOND tốt hơn với..." (evolving)

  ⚠️ DURABILITY CLAIM:
     → File claim "durable nhất (decades)"
     → NHƯNG: neuroscience ĐANG advance → new dimensions có thể emerge
```

```
KẾT NỐI:

═══════════════════════════════════════════════════════
TẦNG 1 — CORE HARDWARE (6 DIM source mechanisms)
═══════════════════════════════════════════════════════

→ Core-Hardware.md v1.0 — 4 zones A/B/C/D, hardware profiles
  §5 "Hardware sets RANGE, chunks choose POSITION" = foundation cho toàn file.
→ PFC-Hardware.md v1.1 — DRD4, COMT — individual parameters
  DIM 2 (VTA/DRD4) + DIM 4 (PFC pace/COMT) → trực tiếp reference.
→ Modality.md v1.0 — 6 encoding channels → DIM 1 source.
→ Cortisol-Baseline.md v2.1 — amplifier, 5 Roles → DIM 3 source.
→ Body-Base.md v3.1 — Compilable Architecture, interoception → DIM 6 source.

═══════════════════════════════════════════════════════
TẦNG 1 — CORE MECHANISM (cross-cutting lenses)
═══════════════════════════════════════════════════════

→ Connection.md v5.0 — 3 Generative Primitives, Resonance Decline, 4-Layer → DIM 5 source.
→ Agent-Mechanism.md v2.1 — Self-Pattern-Modeling v3.1 integration hub.
→ Self-Pattern-Modeling.md v3.1 — 1 mechanism × 3 dimensions.
→ Entity-Valence-Dynamics.md v1.0 — Hardware-Subsidy spectrum (§5). ⭐ Cross-cutting lens.
→ PFC-Operations.md v1.1 — PFC Budget (§9), Compiled Quality Dimension (§5). ⭐ Cross-cutting lens.
→ Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State Reward.
→ Dissonance-Signal-Architecture.md v1.0 — Evaluative/Direct-State Dissonance. ⭐ §5 miscalibration.
→ PFC-Configuration.md v1.0 — 6 dynamic modes, cortisol push mode shift.
→ Sensitivity-Classification.md v1.0 — 3 hardware sensitivity groups.

═══════════════════════════════════════════════════════
TẦNG 1 — BODY-FEEDBACK + ENTITY (v1.1 enrichment)
═══════════════════════════════════════════════════════

→ Body-Feedback-Label.md v2.1 — 3-tier vocabulary, observation precision. ⭐ §2 methodology.
→ Gap-Distribution-Profile.md v1.1 — per-individual gap landscape. ⭐ §3 navigation.
→ Entity-Compiled.md v1.0 — formation 40→200h, Hub-and-Spoke. ⭐ §6 teacher accuracy.
→ Entity-Access.md v1.2 — gradient Mức 0-5. ⭐ §6 calibration accuracy.
→ Coordination-Node.md v1.2 — teacher as coordination node.
→ Simulation-Engine.md v1.1 — AI calibration support (3-layer).

═══════════════════════════════════════════════════════
TẦNG 2 — CHILD DEVELOPMENT (early hardware expression)
═══════════════════════════════════════════════════════

→ Child-Development-Mechanism.md v2.1 — phát triển 0-6
  §2 4+1 Compile, §3 Approach/Avoidance Tags, §8 Cortisol Baseline.
→ Natural-Development.md v2.1 — early hardware expression
→ Skill-Introduction.md v2.1 — early learning preferences visible

═══════════════════════════════════════════════════════
TẦNG 3 — EDUCATION RESEARCH (bộ 3)
═══════════════════════════════════════════════════════

→ Education-Mechanism.md v2.0 — ⭐ HOW: Cost Formula, Direction > Level, Bridge, Imagine-Final.
→ Domain-Knowledge-Map.md v2.0 — WHAT: bản đồ nhóm kiến thức.
→ Connection-Education.md v1.0 — WHO: 5 trụ social interaction education.
  (replaces Empathy-Education v2.0 → backup/)

═══════════════════════════════════════════════════════
TẦNG 4 — EDUCATION APPLICATIONS (system)
═══════════════════════════════════════════════════════

→ Education-System.md v3.0 — WHERE calibration fits trong system.
  §2-§4 per-stage, §7 Teacher role, ENGINE/ROAD/VEHICLE lens.
→ Era-Analysis-2025.md v2.0 — AI tools for calibration.
→ Curriculum-Framework.md v2.0 — WHAT to calibrate for.

═══════════════════════════════════════════════════════
TẦNG 5 — PER-COUNTRY
═══════════════════════════════════════════════════════

→ Country/VN/ files — cultural factors affecting observation + calibration.

═══════════════════════════════════════════════════════
FLOW
═══════════════════════════════════════════════════════

  Core (mechanism) → File này (observe + calibrate)
    → Education-System v3.0 (apply in system)
      → Curriculum (calibrate content)
        → Country files (cultural adjustment)

  = File này = BRIDGE giữa brain mechanism và practical education
  = Durable → update khi neuroscience advances
  = Per-individual → complements population-level system design
```
