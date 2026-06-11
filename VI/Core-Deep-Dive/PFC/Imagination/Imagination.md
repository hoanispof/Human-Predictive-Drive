---
title: Imagination — Hệ Thống Giả Lập Của PFC (Process + Overview)
version: 2.0
created: 2026-04-19
rewritten: 2026-05-24 (v2.0 — REWRITE. +§0 Position/Folder Map, +COMT/DRD4×Modalities, +Compiled/Fresh, +AI era expanded, +Dual Check. All cross-refs modernized. v1.0→backup)
previous: v1.0 → backup/Imagination-v1.0.md
status: MECHANISM v2.0
scope: |
  2 CHỨC NĂNG:
  ① OVERVIEW: Entry point cho Imagination/ folder. Map tất cả files + Simulation-Engine.
  ② UNIQUE PROCESS DETAILS: Content KHÔNG có ở files khác:
     Simulation fidelity (cortisol > opioid), 5 Modalities × Hardware (COMT/DRD4),
     7 Cortisol × Imagine modes (IDLE→CRASH), Disconnect mechanism,
     Override body spectrum, 3 cách dùng (Visualization/Worry/Daydream).
  KHÔNG CHỨA (đã có ở files khác):
     Engine architecture → Simulation-Engine.md v1.0
     Lifecycle 5 phases → Imagine-Final.md v3.0 §5
     Gradient 5 levels → Imagine-Final.md v3.0 §6
     Reflection vs Rumination → Simulation-Engine.md §9
     Chunks chi tiết → Imagine-Final.md v3.0 §6.2
purpose: |
  Simulation-Engine.md = SHARED ENGINE underneath tất cả applications (ARCHITECTURE).
  Imagine-Final.md = APPLICATION-2: future simulation (PRODUCT).
  File NÀY = PROCESS + OVERVIEW: HOW PFC uses engine, fidelity, modes, modalities.
  = "Phòng thí nghiệm" — HOW brain runs simulations, WITH WHAT fidelity, IN WHICH modes.
  Process GENERATE Product. Product khi RELOAD → quay lại Process (refine).
position: |
  Core-Deep-Dive/PFC/Imagination/ — entry point cho folder.
  ENGINE at Simulation-Engine.md (PFC/). PRODUCT at Imagine-Final.md (Imagination/).
  QUALITY CHECK at Imagine-Final-Evaluation.md. BODY→EXPLICIT at Somatic-Articulation-Loop.md.
dependencies:
  pfc:
    - Simulation-Engine.md v1.0 — 1 engine, 3 components, 3 axes (ARCHITECTURE)
    - PFC-Function.md v1.2 — 24 functions, Imagination = function ⑩ (PROCESS)
    - PFC-Hardware.md v1.1 — COMT clear speed, DRD4 threshold (§3-§4)
    - PFC-Development.md v1.0 — Learning trajectory (chunks accumulate)
    - PFC-Hold-Dimensions.md v1.0 — 4±1 slots = workspace constraint
  imagination:
    - Imagine-Final.md v3.0 — APPLICATION (constructive future simulation, PRODUCT)
    - Imagine-Final-Evaluation.md v1.2 — Quality (Domain Fit × Hardware Fit)
    - Somatic-Articulation-Loop.md v1.0 — Body-knowledge → explicit-knowledge
  body:
    - Cortisol-Baseline.md v2.1 — Amplifier, direction > level, cortisol × modes
    - Body-Feedback-Mechanism.md v2.0 — 2 sources, chunk dynamics, Body-Need
    - Chunk.md v2.3 — Chunk substrate, compile mechanism
    - Feeling.md v3.0 — PFC observation interface, feeling ≠ emotion
    - Inter-Body-Mechanism.md v2.0 — Compilable Architecture, Compiled/Fresh axis
    - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State reward
  agent:
    - Self-Pattern-Modeling.md v3.1 — APPLICATION-1 on Simulation-Engine
  observation:
    - Boredom.md v2.0 — No Imagine-Final = "chán", gap-body-need threshold
  application:
    - Ask-AI.md v3.1 — Dual Check: body = quality controller, domain = final arbiter
    - Anchor-Schema.md v1.0 — Sync point, Trust, anchor diversity
sources:
  - Imagination.md v1.0 DRAFT (610L, 2026-04-19) — content source
  - Simulation-Engine.md v1.0 — architecture reference
  - Imagine-Final.md v3.0 — application reference
  - plan-imagination-rewrite.md — rewrite plan
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Imagination — Hệ Thống Giả Lập Của PFC

> **Imagination = PFC function ⑩ (PROCESS category, PFC-Function.md v1.2 §3).**
>
> PFC mở workspace → set HƯỚNG →
> B+C areas RUN simulation (thử kết nối, thử pattern) →
> Body RESPOND (preview 20-60% fidelity so với thật) →
> PFC nhận KẾT QUẢ → evaluate → quyết định thử thật hay không.
>
> = "Phòng thí nghiệm" test ý tưởng TRƯỚC KHI tốn resource thật.
>
> **PROCESS (file này) ↔ PRODUCT (Imagine-Final.md v3.0)**
> Process GENERATE Product. Product khi RELOAD → quay lại Process (refine).
>
> **Engine:** Simulation-Engine.md v1.0 = KIẾN TRÚC (1 engine, 3 components, 3 axes).
> File này = HOW PFC DÙNG engine: fidelity, modes, modalities.

---

## Mục lục

- §0 — Thesis + Position + Folder Map
- §1 — 2 Giá Trị Cốt Lõi: Tại Sao Imagine Tồn Tại
- §2 — Simulation Fidelity (Body Phản Ứng Thật)
- §3 — 5 Modalities × Hardware (COMT/DRD4)
- §4 — Cortisol × 7 Imagine Modes
- §5 — 3 Cách Dùng: Visualization / Worry / Daydream
- §6 — Imagine Có Thể SAI + Override Body
- §7 — Imagination × AI Era
- §8 — Honest Assessment
- §9 — Cross-References

---

## §0 — Thesis + Position + Folder Map

### §0.1 — Core thesis

```
⭐⭐ IMAGINATION = KHÁC BIỆT DEFINING CỦA CON NGƯỜI:

  ① MỌI sinh vật có body-feedback (cảm nhận, phản ứng)
  ② MỘT SỐ sinh vật có basic prediction (cortisol + đồ thị đơn)
  ③ CHỈ CON NGƯỜI có CONSTRUCTIVE SIMULATION:
     = Build scenario MỚI từ chunks đã có → test TRƯỚC KHI thử thật
     = Vì: PFC đủ mạnh + Compilable Architecture đủ sâu
     = Cross-domain, multi-step, abstract → KHÔNG domain nào có thể trial-error tới

  2 GIÁ TRỊ CỐT LÕI (chi tiết §1):
    Giá trị 1: NHANH HƠN — test rẻ trong đầu, thử đắt ngoài chỉ cái đã lọc
    Giá trị 2: MỞ ACCESS — domain body KHÔNG BAO GIỜ chạm (trừu tượng, lý thuyết)

  PROCESS FILE — 5 unique contributions KHÔNG có ở files khác:
    ① Simulation fidelity — body phản ứng thật với imagine (§2)
    ② 5 Modalities × Hardware — COMT/DRD4 tạo khác biệt cá nhân (§3)
    ③ 7 Cortisol × Imagine modes — IDLE → CRASH spectrum (§4)
    ④ 3 Cách dùng — Visualization/Worry/Daydream (§5)
    ⑤ Override body — imagine suppress body signals (§6)
```

### §0.2 — Position trong architecture

```
  VỊ TRÍ:

  ★ Simulation-Engine.md v1.0 = ENGINE ARCHITECTURE
    │  (1 engine, 3 components, 3 axes — SHARED substrate)
    │
    ├── ★ Imagination.md v2.0 (FILE NÀY) = PROCESS + OVERVIEW
    │     HOW PFC dùng engine: fidelity, modes, modalities
    │     Entry point cho Imagination/ folder
    │
    ├── Imagine-Final.md v3.0 = APPLICATION-2 (PRODUCT)
    │     CONSTRUCTIVE FUTURE SIMULATION output
    │     Lifecycle 5 phases, Gradient 5 levels, 3D quality
    │     Ranh giới: Hardware prediction ≠ Imagine-Final
    │
    ├── Imagine-Final-Evaluation.md v1.2 = QUALITY CHECK
    │     Domain Fit × Hardware Fit → 4 góc đánh giá
    │
    └── Somatic-Articulation-Loop.md v1.0 = BODY → EXPLICIT
          Body-knowledge → explicit-knowledge mechanism ("bịa" = body knows)

  READING ORDER:
    Người mới: Imagination.md (NÀY) → Imagine-Final.md → Evaluation
    Người quen: Simulation-Engine.md (ARCHITECTURE) → files cụ thể
```

---

## §1 — 2 Giá Trị Cốt Lõi: Tại Sao Imagine Tồn Tại

```
GIÁ TRỊ 1 — NHANH HƠN (domain body TIẾP XÚC ĐƯỢC):

  Không imagine: muốn nấu ngon → nấu 999 lần dở → lần 1000 ngon
  Có imagine: imagine 20 công thức → body simulate vị → chọn 3 → nấu thật 3 lần
  = Test RẺ trong đầu, thử ĐẮT ngoài thật chỉ cái đã lọc.

  PFC GIẢM VÒNG body-check THẬT cần thiết:
    Không PFC:        50-1000 vòng thật → 1 kết quả tốt
    Có PFC:           10-100 imagine + 1-5 thật → 1 kết quả tốt
    PFC + chunks sâu: ít imagine + 1-2 thật → xong
    PFC + AI:         5-20 imagine + 1-2 thật → xong
  → = "Xe hơi nhanh hơn đi bộ" → cùng tới đích, khác tốc độ

  🟢 Evidence:
    Motor imagery → muscle activation thật (Jeannerod 2001)
    Mental rehearsal → performance improvement (sport psychology)
    Sleep replay → consolidate + optimize patterns (Wilson & McNaughton 1994)
    Planning → reduce errors (executive function literature)


GIÁ TRỊ 2 — MỞ ACCESS (domain body KHÔNG BAO GIỜ tới):

  Có những domain mà thử vô hạn lần thật = VẪN KHÔNG tới:
    E=mc²: không hành động trial-error nào cho ra công thức này
    → Dù 8 tỷ người × triệu năm = VẪN KHÔNG
    → Vì: E=mc² nằm ở domain TRỪU TƯỢNG → body KHÔNG tiếp xúc trực tiếp
    (Chi tiết Abstract Domain: Domain.md v2.0 §2)

  Imagine MỞ ACCESS bằng:
    ① Cross-domain: kết nối chunks TỪ NHIỀU domain → pattern MỚI
       E=mc² = mechanics + electromagnetism + thought experiment
       → KHÔNG domain nào riêng lẻ chứa → NẰM Ở GIAO ĐIỂM
    ② Abstract layer: test CÁI KHÔNG THỂ LÀM thật
       Einstein: "nếu tôi CƯỠI trên tia sáng?" → KHÔNG THỂ thử thật
    ③ Multi-step chain: chain 100 bước logic TRONG ĐẦU
       Trial-error: phải thử TỪNG BƯỚC thật (100 thử thật)
       Imagine: chain 100 bước = 1 lần imagine → test kết quả

  → = "Tàu vũ trụ tới nơi xe hơi KHÔNG BAO GIỜ tới"
  → TẤT CẢ domain "không thể chạm" → CHỈ imagine tới được
  → = Vật lý lý thuyết, toán cao cấp, triết học, tương lai xa
  → = Đây là tại sao CON NGƯỜI khác MỌI sinh vật


⭐ Imagine ĐỒNG THỜI build chunks ở B areas:

  Khi PFC imagine → KHÔNG CHỈ "test ý tưởng":
    → PFC spotlight B areas liên quan → neurons fire THEO HƯỚNG PFC chỉ
    → B neurons ĐỒNG THỜI tạo kết nối MỚI theo simulate
    → = 2 OUTPUT song song từ 1 quá trình imagine:
      Output 1: ý tưởng được test (lọc options sai)
      Output 2: chunks ở B areas được pre-build (chuẩn bị execute)

  → Imagine XONG → B areas ĐÃ CÓ SẴN patterns mới
  → Thực hiện THẬT → B areas CHỈ CẦN chạy patterns đã tạo → NHANH
  → = "Cảm thấy làm được" = B areas ĐÃ SẴN SÀNG
  → = "Mơ mộng" KHÔNG vô ích — NẾU có HƯỚNG (body-need drive)
  → 🟢 Pascual-Leone 1995: 5 ngày imagine chơi piano → cortical map
     MỞ RỘNG THẬT dù chưa chạm piano

  🟡 Framework: imagine = test + pre-build CÙNG LÚC
     (mỗi phần established riêng, gom lại = novel integration)


⭐ CHUNKS = NGUYÊN LIỆU CHO IMAGINE:

  Imagine = PFC draft + B+C simulate
  Simulate BẰNG GÌ? → Bằng CHUNKS ĐÃ CÓ (compiled ở B areas)
  → Không có chunks → imagine NGHÈO ("không nghĩ ra gì")
  → Chunks đủ → imagine PHONG PHÚ → novelty flow possible
  → Chunks nhiều + đa domain → cross-domain insight → breakthrough
  → "Không có ý tưởng" ≠ thiếu creativity = thiếu CHUNKS (nguyên liệu)

  COMPILED vs FRESH chunks × imagine:
    Compiled chunks: retrieval NHANH, auto → imagine MƯỢT, flow dễ
      = Expert pianist imagine nhạc: chunks piano đã compiled → chảy tự nhiên
    Fresh chunks: PFC PHẢI hold → imagine CHẬM, effortful
      = Người mới imagine nhạc: phải recall từng nốt → workspace đầy nhanh

  ⭐ CÁCH tích lũy chunks ẢNH HƯỞNG CHẤT LƯỢNG imagine:
    Chunks tích lũy bằng THREAT → gắn cortisol → dùng chunk → body nhớ cortisol
      → Imagine dùng chunks này = KHÔNG PLEASANT → khó flow
      → = "Giỏi toán nhưng GHÉT toán" = chunks ok, association xấu
    Chunks tích lũy bằng NOVELTY → gắn curiosity/opioid → body nhớ pleasant
      → Imagine dùng chunks này = PLEASANT → dễ flow
    → = Education: threat vs novelty → ảnh hưởng SUỐT ĐỜI imagine quality
  (Chi tiết chunk dynamics: Chunk.md v2.3, Imagine-Final.md v3.0 §6.2)


CẢ HAI CẦN NHAU — PFC + Body:
  CHỈ PFC: simulate → "logic đúng!" → nhưng chưa check domain thật → có thể SAI
    = "Philosopher trap" — nghĩ hay nhưng không thử → không biết sai
  CHỈ Body: thử → fail → thử → fail → chậm cực kỳ
    = Trial-error primitive — hoạt động nhưng tốn
  PFC + Body = TỐI ƯU:
    PFC imagine → lọc options sai (rẻ) → Body thử thật → confirm (chắc)
  (Dual Check: Ask-AI.md v3.1 §6.1 — body = quality controller, domain = final arbiter)
```

---

## §2 — Simulation Fidelity (Body Phản Ứng Thật)

```
BODY THẬT SỰ PHẢN ỨNG với imagine — không phải metaphor:

  🟢 Research evidence:
    Fear imagine: cortisol + NE TĂNG thật, tim đập nhanh thật
    Sex imagine: body THẬT SỰ aroused (hormones, blood flow)
    Motor imagine: cơ ACTIVATE thật (đo được bằng EMG)
    Placebo: "thuốc giả" → body CHỮA thật (imagine "đã uống thuốc")
    Phim buồn: khóc THẬT dù BIẾT là phim

  → Imagine → body respond ở 20-60% fidelity so với thật
  → KHÔNG phải 100% (biết là tưởng tượng → body giảm)
  → NHƯNG đủ để: test ý tưởng + pre-build chunks + chuẩn bị hành động


⭐ FIDELITY KHÁC NHAU theo loại — CORTISOL BIAS:

  ┌─────────────────┬────────────┬────────────────────────────────┐
  │ Loại response   │ Fidelity   │ Giải thích                     │
  ├─────────────────┼────────────┼────────────────────────────────┤
  │ Cortisol        │ 40-70%     │ Imagine xấu → stress GẦN thật │
  │ (stress)        │ CAO NHẤT   │ Evolution: sợ sai > thích đúng │
  ├─────────────────┼────────────┼────────────────────────────────┤
  │ Opioid          │ 20-40%     │ Imagine tốt → pleasant NHẸ    │
  │ (pleasure)      │            │ "Preview" reward, không full    │
  ├─────────────────┼────────────┼────────────────────────────────┤
  │ Motor           │ 10-30%     │ Imagine hành động → cơ hơi     │
  │ (movement)      │            │ activate (measurable EMG)       │
  ├─────────────────┼────────────┼────────────────────────────────┤
  │ Oxytocin        │ 10-20%     │ Imagine ôm < ôm thật RẤT NHIỀU│
  │ (connection)    │            │ Cần body contact thật           │
  └─────────────────┴────────────┴────────────────────────────────┘

  ⭐ INSIGHT: Cortisol fidelity CAO HƠN opioid:
    → Imagine scenario XẤU → stress ~60% → ĐAU ĐÁNG KỂ
    → Imagine scenario TỐT → pleasant ~30% → PLEASANT NHẸ
    → = Body BIAS: simulate xấu → respond MẠNH. Simulate tốt → respond NHẸ.
    → Evolution: tránh chết (cortisol) > tìm pleasant (opioid)
    → = TẠI SAO WORRY DỄ HƠN VISUALIZATION:
      Worry: body respond MẠNH → loop MẠNH → dễ lặp
      Visualization: body respond NHẸ → loop YẾU → khó duy trì
      → "Lo lắng tự nhiên, lạc quan phải cố" = ĐÚNG biochemistry
    → Cortisol = amplifier (Cortisol-Baseline.md v2.1) → amplify cả IMAGINE response
    → Imagine tốt nhưng nếu cortisol baseline CAO → body vẫn đọc qua lens threat


FIDELITY THAY ĐỔI theo:
  Tuổi: trẻ ~80% (body chưa calibrate) → lớn ~30% (đã calibrate)
    → Trẻ 3 tuổi: sợ quái vật tưởng tượng = SỢ THẬT (80%)
  Modality: emotional > somatic > visual > motor > verbal
  Experience: đã trải qua thật → simulate CHÍNH XÁC hơn
  Training: visualization practice → fidelity TĂNG (athletes, meditators)

  ⭐ FIDELITY × COMPILED/FRESH:
    Compiled chunks → body đã calibrate fidelity → response CHÍNH XÁC hơn
    Fresh chunks → body chưa biết match reality thế nào → fidelity KHÔNG ỔN ĐỊNH
    → Expert imagine trong domain → fidelity ĐÁNG TIN
    → Newbie imagine trong domain → fidelity KHÔNG đáng tin
    (Inter-Body-Mechanism.md v2.0 §3: Compiled/Fresh axis)
```

---

## §3 — 5 Modalities × Hardware (COMT/DRD4)

```
Imagine KHÔNG chỉ "thấy hình trong đầu" — có 5 Experience + 1 Communication:

  ① VISUAL — thấy hình ảnh, cảnh, khuôn mặt:
     → B area: Visual cortex (CÙNG vùng xử lý nhìn thật)
     → PFC top-down spotlight → re-activate V1/V2 (~30-50% real activation)
     → 2 sub-types: sequential (flowchart) vs spatial (3D, cross-domain)
     → 2-5%: APHANTASIA — không visual imagine → BÙ bằng verbal/conceptual
     → 🟢 Kosslyn 1994, 2005; Pearson 2019

  ② AUDITORY — nghe âm thanh, giọng nói, nhạc trong đầu:
     → B area: Auditory cortex
     → "Inner voice" (self-talk), "Earworm" (bài hát stuck)
     → Beethoven điếc vẫn sáng tác = auditory imagine thuần

  ③ SOMATIC — cảm nhận body: đau, ấm, lạnh, áp lực:
     → B area: Insula + Somatosensory cortex
     → Ít người NHẬN RA đang dùng — nhưng RẤT phổ biến
     → CỰC NGANG: body detect pattern KHÔNG qua logic → ANY domain
     → "Cái này FEEL giống cái kia" → cross-domain pattern detection mạnh nhất

  ④ MOTOR — tưởng tượng hành động, cử động:
     → B area: Motor cortex + Cerebellum
     → 🟢 EMG measurable; Pascual-Leone 1995 (piano cortical map)
     → Athletes, dancers, surgeons: mental practice = proven improve

  ⑤ EMOTIONAL — cảm xúc giả lập:
     → C+B areas: Amygdala + Insula + dmPFC
     → Body KHÔNG hoàn toàn phân biệt emotional real vs imagined
     → Phim LÀM KHÓC dù BIẾT giả = emotional simulation bypass filter

  ⑥ VERBAL — inner monologue (COMMUNICATION, không phải Experience):
     → B area: Broca + Wernicke (language areas)
     → ⚠️ Verbal KHÔNG "tưởng tượng" → verbal NARRATE kết quả
     → 5 modalities gốc (①-⑤) = THẬT SỰ simulate (body respond)
     → Verbal (⑥) = DỊCH kết quả ra lời


⭐ MODALITY × HARDWARE (COMT/DRD4):

  COMT CLEAR SPEED (PFC-Hardware.md v1.1 §3) → SPECIALIST vs IMPROVISER:

  ┌──────────────────────────────────────────────────────────┐
  │ CỰC DỌC (deep, sequential):     CỰC NGANG (broad):    │
  │   Verbal ●●●●●                    Somatic ●●●●●        │
  │   Motor ●●●●                      Visual-spatial ●●●●  │
  │   Visual-seq ●●●●                 Emotional ●●●●       │
  └──────────────────────────────────────────────────────────┘

  Specialist (COMT Met/Met — draft giữ LÂU, ~60-70% dân số):
    → Dominant: verbal + motor (sequential processing)
    → Schema build: EXTERNAL-IN (nhận info → integrate → hiểu)
    → Chain DỌC → sâu trong 1 domain → expert
    → School MATCH → "học giỏi"
    → Imagine: INCREMENTAL — sửa trên nền draft cũ → deep, consistent

  Improviser (COMT Val/Val — draft clear NHANH, ~15-20% dân số):
    → Dominant: somatic + visual-spatial (pattern processing)
    → Schema build: INTERNAL-OUT (body feel → tìm info confirm)
    → Chain NGANG → across domains → connector
    → School KHÔNG match → "học khó" (cá bị bắt leo cây)
    → Imagine: FRESH REBUILD — workspace trống → draft hoàn toàn mới → creative

  Val/Met Heterozygous (~50%): context-dependent → FLEXIBLE

  ⭐ KEY INSIGHT (PFC-Hardware.md v1.1 §3):
    Val/Val "chán nhanh" = DRAFT CLEAR NHANH, không phải thiếu reward
    Met/Met "bám 1 thứ" = DRAFT CÒN, không phải thiếu curiosity
    → = HARDWARE quản lý DRAFT, không phải "ý chí" quản lý behavior

  DRD4 SENSITIVITY THRESHOLD (PFC-Hardware.md v1.1 §4):
    DRD4-7R (novelty-seeking variant — ~20% dân số):
      → Threshold CAO → cần novelty MẠNH hơn để activate imagine
      → Imagine MẠNH khi engage, nhưng KHÓ engage với novelty nhẹ
    DRD4-4R (typical — ~70%):
      → Threshold BÌNH THƯỜNG → engage dễ hơn, cường độ vừa
    → COMT × DRD4 = 2 trục INDEPENDENT → nhiều profiles khác nhau


  ⚠️ Profiles KHÔNG cố định:
    Train → TĂNG. Không dùng → GIẢM.
    School push verbal 12-16 năm → majority verbal dominant
    = Nhiều người "mất" visual/somatic vì school CHỈ train verbal
```

---

## §4 — Cortisol × 7 Imagine Modes

```
CORTISOL BASELINE quyết định imagine ở MODE nào:

  ⚠️ Cortisol KHÔNG ép PFC imagine trực tiếp:
    Cortisol tăng → B+C neurons fire MẠNH HƠN (arousal)
    → B+C dao động → VTA detect biến động → dopamine → PFC THẤY
    → = Cortisol → B+C rung → VTA → PFC (GIÁN TIẾP)
    → Cortisol = AMPLIFIER (Cortisol-Baseline.md v2.1): khuếch đại signal,
      KHÔNG tạo signal. Direction (novelty vs threat) > Level.
    → Chi tiết VTA loop: PFC-Hardware.md v1.1 §7

  ┌─────────────┬────────────────────────┬────────────────────────┐
  │ Cortisol    │ Imagine MODE           │ Body State             │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Cực thấp    │ IDLE: imagine yếu      │ Body ok, thưởng thức  │
  │ (IDLE)      │ Chỉ react external     │ "Đời đẹp quá"         │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Thấp        │ LAZY: imagine nhẹ      │ Body ok, relaxed       │
  │ (LAZY)      │ PULL only, shallow     │ Game/MXH = external đủ │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Vừa         │ ACTIVE: imagine tốt    │ Body "cần tốt hơn"    │
  │ (ACTIVE)    │ Internal + External    │ = SWEET SPOT           │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Hơi cao     │ FOCUSED: imagine sâu   │ Body hơi căng          │
  │ (FOCUSED)   │ Novelty SÂU + HẸP     │ "Deadline tạo focus"   │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Cao         │ PUSH: thiên threat     │ Body căng              │
  │ (PUSH)      │ Novelty bị lấn        │ "Phải làm, không nghỉ" │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Rất cao     │ FREEZE: imagine loop   │ Mất ngủ, lo lắng      │
  │ (FREEZE)    │ Overthink, stuck       │ "Không nghĩ được gì"  │
  ├─────────────┼────────────────────────┼────────────────────────┤
  │ Cực cao     │ CRASH: imagine off     │ Body shutdown           │
  │ (CRASH)     │ PFC gần offline        │ Burnout                 │
  └─────────────┴────────────────────────┴────────────────────────┘

  ⭐ SWEET SPOT = ACTIVE/FOCUSED:
    Cortisol VỪA ĐỦ → neurons fire MẠNH + đa dạng → cross-connection → novelty
    NHƯNG: chưa đủ cao để suppress body-feedback → imagine VẪN nhận feedback
    → = Tối ưu: novelty CAO + body-check CÒN HOẠT ĐỘNG


2 NGUỒN TRIGGER IMAGINE:

  INTERNAL (cortisol baseline → B+C rung → novelty):
    → Cortisol đủ → neurons fire MẠNH + KHÁC → cross-connection tự xảy ra
    → = DEEP novelty: cross-domain, abstract, multi-step

  EXTERNAL (sensory input → trigger):
    → Cortisol CÓ THỂ thấp → nhưng input MỚI → VTA detect
    → = SHALLOW novelty thường (react to external)
    → CÓ THỂ trigger cortisol → dẫn tới deep novelty

  COMBINATION (phổ biến nhất):
    → External thú vị → cortisol nhẹ (curiosity) → internal rung → deeper
    → = "Thấy cái hay → tò mò → nghĩ sâu → insight"


⭐ DISCONNECT MECHANISM — imagine thoát khỏi body:

  Cortisol TĂNG DẦN:
    ① Body-need signal → imagine nhận → "body cần X" → tìm X
    ② Cortisol tăng → imagine MẠNH → TÌM tích cực
    ③ Cortisol tăng THÊM → body signal bị SUPPRESS (cortisol suppress cảm nhận)
    ④ Imagine KHÔNG NHẬN feedback "đủ chưa"
    ⑤ Imagine TIẾP TỤC (không có signal dừng)
    ⑥ Body bị bỏ quên → "ăn không ngon, ngủ không sâu, ôm không ấm"
    → = "Imagine hijack" = cortisol suppress body → imagine mất feedback → chạy mù
    → = Simulation-Engine chạy nhưng Interoception bị block (Simulation-Engine.md v1.0 §4)
    → Chi tiết cortisol mechanism: Cortisol-Baseline.md v2.1


VÒNG LẶP — virtuous vs vicious:

  VIRTUOUS: body-need met → cortisol giảm → body enjoy → imagine phục vụ body → body tốt hơn → ...
  VICIOUS: body-need KHÔNG met → cortisol tăng → body suppress → imagine mất feedback → body tệ hơn → ...
  → Chuyển VICIOUS → VIRTUOUS = CẮT vòng lặp:
    Bước 1: hạ cortisol (nghỉ, ngủ, exercise)
    Bước 2: body signal PHỤC HỒI
    Bước 3: imagine nhận feedback → phục vụ body lại
    → = "Chữa" = phục hồi FEEDBACK LOOP, không phải "sửa imagine"
    (Body-Feedback-Mechanism.md v2.0: body-feedback loop phụ thuộc cortisol state)
```

---

## §5 — 3 Cách Dùng: Visualization / Worry / Daydream

```
CÙNG cơ chế imagine (Simulation-Engine) → 3 OUTPUT rất KHÁC:

① VISUALIZATION — imagine CÓ CHỦ ĐÍCH (giúp):
   → PFC hold scenario TỐT → body preview: opioid nhẹ + motor prepare
   → 🟢 Athletes: visualize thắng → motor cortex fire → performance↑
   → Phỏng vấn: imagine Q&A → chunks pre-build → tự tin hơn
   → Body respond: opioid NHẸ (30%) → dễ duy trì nhưng PHẢI CỐ GẮNG
   → Simulation-Engine: (Self, Future, Construct) → đúng APPLICATION Imagine-Final

② WORRY — imagine CHỐNG MÌNH (hại):
   → PFC hold scenario XẤU → body respond: cortisol THẬT
   → "Bị đuổi việc → hết tiền → vô gia cư" = body ĐAU dù chưa xảy ra
   → Body respond: cortisol MẠNH (60%) → loop TỰ DUY TRÌ → dễ lặp
   → Worry ≠ Planning:
     Planning: "bị đuổi → update CV, gọi 3 người" = ACTIONABLE → cortisol GIẢM
     Worry: "bị đuổi → CHẾT MẤT → ai thuê..." = EMOTIONAL LOOP → cortisol TĂNG MÃI
   → = Engine Use Quality: RUMINATION (Simulation-Engine.md v1.0 §9)

③ DAYDREAM — imagine TỰ DO (mixed):
   → PFC relax → DMN take over → B+C chain TỰ DO
   → CÓ THỂ: creativity, eureka → TỐT (cross-domain connection)
   → CÓ THỂ: escapism, sống trong đầu → XẤU (replacement cho reality)
   → Maladaptive daydreaming: daydream THAY THẾ reality → condition thật
   → = Engine ở mode AUTO (passive), output tuỳ thuộc cortisol state


TẠI SAO WORRY DỄ HƠN VISUALIZATION:
  → Worry: cortisol fidelity ~60% → body respond MẠNH → loop MẠNH
  → Visualization: opioid fidelity ~30% → body respond NHẸ → loop YẾU
  → = "Lo lắng tự nhiên, lạc quan phải cố gắng" = ĐÚNG biochemistry
  → Evolution: tránh chết > tìm pleasant → body THIÊN VỊ worry
  → = Cần TRAINING để visualization thắng worry
  (Chi tiết fidelity: §2. Cortisol bias: Cortisol-Baseline.md v2.1)
```

---

## §6 — Imagine Có Thể SAI + Override Body

```
IMAGINE KHÔNG HOÀN HẢO — 5 dạng SAI:

  ① Predict tương lai SAI → surprise
     (chunks thiếu, hoặc domain phức tạp hơn imagine)
  ② Chọn option SAI → regret
     (body simulate chưa đủ chính xác)
  ③ Hiểu người khác SAI → conflict
     (Self-Pattern-Modeling v3.1 = simulate, không phải biết → có thể hoàn toàn sai)
  ④ Hiểu mình SAI → self-deception
     (verbal narrate SAI → body signal bị ignore)
  ⑤ Translate SAI → miscommunication
     (lời = compressed → mất nuance → receiver reconstruct khác)

  → PFC MẠNH nhưng KHÔNG hoàn hảo → CẦN body check + domain check
  → DUAL CHECK (Ask-AI.md v3.1 §6.1):
    Body = quality controller (đúng ~90%, coherence check)
    Domain reality = final arbiter (evidence, kết quả thật)
    → Body YES + Domain NO = NGUY HIỂM NHẤT (amplification trap)


IMAGINE OVERRIDE BODY — spectrum từ nhẹ tới cực đoan:

  Cơ chế: Imagine suppress body signal (§4 disconnect mechanism)
  Cortisol HOẶC novelty MẠNH → body-feedback bị reduce → imagine không còn check
  Chỉ KHÁC MỨC ĐỘ:

  Nhẹ (hàng ngày):
    → Đọc sách hay quên ăn: Novelty override nutrition signal
    → Scroll MXH tới 2h sáng: Novelty override sleep signal

  Trung bình:
    → Workaholic quên ngủ/gia đình
    → Nghiện game bỏ bê body
    → Diet cực đoan (schema override body hunger)

  Nặng:
    → Game tới chết (có cases thật — body survival signals bị override hoàn toàn)
    → Anorexia tới chết (schema "gầy = đẹp" override nutrition survival)
    → Cờ bạc phá sản (reward prediction override resource protection)

  Cực đoan:
    → Tử vì đạo: chunks "thiên đàng" override body survival signals
    → Mẹ nhảy vào lửa cứu con: Protect override personal survival
    → = Compiled chunks MẠNH HƠN body survival → evolutionary "feature"
      cho phép hy sinh cá nhân → gene/tập thể survive

  → = "Bug" lớn nhất: imagine MẠNH ĐẾN MỨC suppress body signal
  → HOẶC "Feature": sacrifice cho mục đích lớn hơn bản thân


⭐ HARDWARE-FIRST HARM PATTERN (Anchor-Schema.md v1.0 lens):

  Override không chỉ "quên ăn 1 bữa" — có thể KHÓA LẠI thành pattern:
    ① Anchor chunks RẤT MẠNH (1 belief/goal dominate)
    ② Body CHẠY MƯỢT theo → compiled, không cần PFC check
    ③ Body skip giai đoạn → KHÔNG còn body-check
    ④ Chunks tự xác nhận → vòng lặp khép kín → INVISIBLE harm

  NGUY HIỂM vì: body KHÔNG kêu → KHÔNG phát hiện → damage âm thầm

  COUNTERMEASURE:
    Self-awareness (meta-cognition) = TỐT nhưng KHÔNG đủ
    → Cần thêm:
      BODY-LISTENING regular (khôi phục body-feedback sensitivity) +
      EXTERNAL FEEDBACK (người ngoài thấy điều mình không thấy) +
      ANCHOR DIVERSITY (đa anchor → không 1 anchor dominate) +
      DOMAIN CHECK (kiểm chứng thực tế — body check coherence, domain check truth)
    (Ask-AI.md v3.1 §6.1: Dual Check protocol)
```

---

## §7 — Imagination × AI Era

```
AI THAY ĐỔI IMAGINE thế nào — cả 2 GIÁ TRỊ bị ảnh hưởng:

  TRƯỚC AI:
    Imagine quality = chunks TRONG ĐẦU × PFC quality
    → Phải TÍCH LŨY chunks TRƯỚC (10-20 năm học) → imagine SAU
    → = "Phải khổ trước, sáng tạo sau"

  VỚI AI:
    Imagine quality = chunks TRONG ĐẦU + chunks TỪ AI × PFC quality
    → Threshold chunks nội bộ GIẢM đáng kể
    → Trước: cần ~80% chunks trong đầu, 20% tra cứu
    → Với AI: cần ~20% chunks nền, 80% AI cung cấp real-time


⭐ AI × 2 GIÁ TRỊ CỐT LÕI:

  Giá trị 1 (NHANH HƠN) → AI TĂNG TỐC thêm:
    Trước AI: imagine 20 → chọn 3 → thử thật 3
    Với AI: AI generate 200 → imagine 10 promising → thử thật 1-2
    → AI mở rộng SEARCH SPACE → PFC vẫn FILTER + body vẫn CHECK
    → = Xe hơi → tàu tốc hành (nhưng VẪN cần tài xế = PFC + body)

  Giá trị 2 (MỞ ACCESS) → AI MỞ RỘNG nhưng KHÁC CHẤT:
    AI cho access TỚI INFO → nhưng KHÔNG cho access TỚI UNDERSTANDING
    → AI provide chunks → PFC recombine → body check
    → AI KHÔNG thay thế constructive simulation (brain vẫn phải BUILD)
    → = AI = kho nguyên liệu vô hạn. Brain = đầu bếp phải nấu.


⭐ VẪN CẦN CHUNKS NỀN (không thể zero):

  ① Để HIỂU câu trả lời AI (cần biết sơ sơ context)
  ② Để HỎI ĐÚNG CÂU ("asking right questions" = skill quan trọng nhất)
  ③ Để SOMATIC CHECK (AI trả lời → cần "feel" đúng/sai → cần chunks nền)
     → Somatic check = body-based quality controller → AI KHÔNG CÓ body
     → Người KHÔNG có chunks nền → KHÔNG detect được AI sai
     → = 🟡 Dangerous: AI tự tin + người thiếu chunks nền = accept mù

  SKILL QUAN TRỌNG NHẤT AI ERA:
    ❌ Memorize (AI nhớ hộ)
    ❌ Calculate (AI tính hộ)
    ❌ Search (AI tìm hộ)
    ✅ Ask right questions (cần chunks nền + intuition)
    ✅ Somatic check (body feel đúng/sai → AI KHÔNG CÓ body)
    ✅ Cross-domain connect ("cái này giống cái kia" → improviser advantage)


⭐ AI × DUAL CHECK (Ask-AI.md v3.1 §6.1):

  AI output = HYPOTHESIS, không phải sự thật
  → DUAL CHECK vẫn áp dụng cho AI-assisted imagine:

  ① Body check: AI cho ý tưởng → body feel thế nào? Smooth hay resistance?
     → Body đúng ~90% cho COHERENCE, nhưng KHÔNG check TRUTH
  ② Domain check: AI suggest → evidence thực tế? Kết quả thật?
     → Domain = final arbiter

  ⚠️ NGUY HIỂM RIÊNG CỦA AI × IMAGINE:
    AI confirm pattern → body coherence TĂNG → body YES mạnh hơn
    → NHƯNG domain reality KHÔNG thay đổi
    → = AI khuếch đại khoảng cách body-coherence ↔ domain-truth
    → Body YES + Domain NO = NGUY HIỂM NHẤT
    → Imagine + AI confirm → tự tin HƠN → nhưng SAI NHIỀU HƠN nếu thiếu domain check


IMAGINE SHIFT:
  Trước: "tôi biết gì? → remix" (limited by chunks)
  Giờ: "tôi hỏi gì? → AI cho chunks → tôi remix + body check + domain verify"
  → Từ "biết nhiều" → "hỏi đúng + feel đúng + kiểm chứng đúng"
```

---

## §8 — Honest Assessment

```
🟢 ESTABLISHED:
  Body responds to imagination (EMG, fMRI, hormones — multiple studies)
  Cortisol fidelity > opioid fidelity (threat bias — evolution literature)
  Motor imagery → cortical map changes (Pascual-Leone 1995)
  Visual imagine uses V1/V2 (Kosslyn 1994, 2005)
  Aphantasia exists (~2-5%, Pearson 2019)
  Mental rehearsal → performance improvement (sport psychology)
  Sleep replay consolidation (Wilson & McNaughton 1994)
  Worry = cortisol loop (anxiety research)
  Maladaptive daydreaming = recognized condition
  COMT Val/Val vs Met/Met = well-replicated (Egan 2001, multiple follow-ups)
  DRD4 variants → novelty sensitivity (Benjamin 1996, replicated)

🟡 FRAMEWORK SYNTHESIS:
  2 giá trị cốt lõi (nhanh hơn + mở access) — novel integration
  Imagine = test + pre-build CÙNG LÚC — novel framing
  Fidelity table (cortisol/opioid/motor/oxytocin %) — 🔴 exact % = estimated
  5 modality × specialist/improviser × COMT mapping — novel
  Cortisol × 7-level imagine modes — novel
  Disconnect mechanism (cortisol suppress → imagine hijack) — novel
  Override body spectrum (nhẹ → cực đoan) — novel integration
  Chunks association quality (threat-learn vs novelty-learn) — novel
  Fidelity × Compiled/Fresh chunks — novel
  Simulation-Engine context (architecture → process → product) — novel framing
  AI era: "biết nhiều → hỏi đúng + feel đúng + kiểm chứng đúng" — novel
  AI × Dual Check risk (AI amplify coherence ≠ truth) — novel

🔴 NEEDS MORE RESEARCH:
  Exact fidelity percentages per modality per individual
  Whether modality dominance is primarily genetic or training
  Quantitative chunk threshold for flow per domain
  Disconnect mechanism: at what cortisol level exactly?
  AI chunks effectiveness vs internal chunks for imagine quality
  COMT × DRD4 interaction effects on imagination specifically
  AI amplification effect on body-coherence ↔ domain-truth gap (measurable?)
```

---

## §9 — Cross-References

```
PFC FOLDER:
  Simulation-Engine.md v1.0 — ENGINE ARCHITECTURE: 1 engine, 3 components, 3 axes
  PFC-Function.md v1.2 §3 ⑩ — Imagination as 1 of 24 PFC functions
  PFC-Hardware.md v1.1 §3 — COMT clear speed (Improviser vs Specialist)
  PFC-Hardware.md v1.1 §4 — DRD4 chunk threshold (novelty sensitivity)
  PFC-Hardware.md v1.1 §7 — VTA detection loop (mechanism)
  PFC-Development.md v1.0 §4 — Learning trajectory (chunks accumulate → imagine richer)
  PFC-Hold-Dimensions.md v1.0 — 4±1 slots = workspace constraint for imagine

IMAGINATION FOLDER:
  Imagine-Final.md v3.0 — APPLICATION: constructive future simulation (PRODUCT)
  Imagine-Final-Evaluation.md v1.2 — Quality assessment (Domain × Hardware Fit → 4 góc)
  Somatic-Articulation-Loop.md v1.0 — Body-knowledge → explicit-knowledge mechanism

BODY-BASE:
  Cortisol-Baseline.md v2.1 — Cortisol = amplifier, direction > level, affects imagine mode
  Body-Feedback-Mechanism.md v2.0 — 2 sources, chunk dynamics, body-feedback readout
  Chunk.md v2.3 — Chunk substrate + compile mechanism
  Inter-Body-Mechanism.md v2.0 §3 — Compiled/Fresh axis
  Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State reward types

FEELING:
  Feeling.md v3.0 — PFC observation interface (broader than APPLICATION-3)
  Self-Observation.md v1.0 — APPLICATION-3: Self × Present × Observe

AGENT-MECHANISM:
  Self-Pattern-Modeling.md v3.1 — APPLICATION-1 on Simulation-Engine (simulate other)

OBSERVATION:
  Boredom.md v2.0 — No Imagine-Final = "chán", gap-body-need threshold

DOMAIN:
  Domain.md v2.0 §2 — 3 Domain Types (Reality / Abstract / Abstract-Dynamic)

APPLICATION:
  Ask-AI.md v3.1 §6.1 — Dual Check: body = quality controller, domain = final arbiter
  Anchor-Schema.md v1.0 — Sync point, Trust, anchor diversity

BACKUP:
  backup/Imagination-v1.0.md — v1.0 DRAFT source content (610L)
```

---

> **Imagination.md v2.0**
>
> Imagination = phòng thí nghiệm giả lập. Process view of Simulation-Engine.
> 2 giá trị: nhanh hơn (xe hơi) + mở access domain mới (tàu vũ trụ).
> Body phản ứng THẬT: cortisol 40-70% > opioid 20-40% → worry dễ hơn visualization.
> 5 modalities × COMT/DRD4 hardware: specialist (verbal/motor) vs improviser (somatic/visual-spatial).
> Chunks = nguyên liệu. Compiled → flow dễ. Threat-learn → khó flow. Novelty-learn → dễ flow.
> Cortisol × 7 modes: IDLE → SWEET SPOT → CRASH. Disconnect mechanism.
> 3 cách dùng: Visualization (opioid nhẹ) / Worry (cortisol mạnh) / Daydream (mixed).
> Override body: nhẹ (quên ăn) → cực đoan (tử vì đạo). Hardware-First Harm pattern.
> AI era: shift "biết nhiều" → "hỏi đúng + feel đúng + kiểm chứng đúng".
> Dual Check: body = quality controller, domain = final arbiter. AI amplify risk.
>
> Phiên bản: v2.0, 2026-05-24. Rewrite từ v1.0 DRAFT.
