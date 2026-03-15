# Human Predictive Drive — Framework Động Lực Con Người v7.0-DRAFT

> **Phiên bản:** 7.0-DRAFT (Kiến trúc mới: Container + 3 Tầng + Domain)
> **Nguyên tắc:** Công thức, không đáp án. Mô hình, không dogma.
> **Quy ước:** 🟢 Nghiên cứu vững | 🟡 Suy luận có cơ sở | 🔴 Giả thuyết
> **Trạng thái:** DRAFT — đang refine, chưa thay thế Core.md v6.0
>
> **⚠️ LƯU Ý:**
> Framework ở mức **Level 2** trên scientific ladder:
> Internally consistent, chưa empirically validated.
> Các thành phần riêng lẻ (PE, dopamine, schema) có research base.
> Kiến trúc tổng thể + cách kết hợp = synthesis mới, chưa test.

---

## Mục Lục

0. [Tổng Quan](#0-tổng-quan)
1. [Kiến Trúc Tổng Thể](#1-kiến-trúc-tổng-thể)
2. [Môi Trường (Container)](#2-môi-trường-container)
3. [T1: Hardware — Nền Tảng Sinh Hóa](#3-t1-hardware)
4. [T2: Software — Nhận Thức Nội Tại](#4-t2-software)
5. [T3: Hành Vi — Output Quan Sát Được](#5-t3-hành-vi)
6. [Domain — Quy Luật Nền](#6-domain)
7. [Luồng Xử Lý + Feedback Loops](#7-luồng-xử-lý)
8. [Emergence Phase + Can Thiệp](#8-emergence)
9. [Câu Hỏi Mở + Gaps](#9-câu-hỏi-mở)
10. [Thay Đổi v6 → v7](#10-thay-đổi)

---

## 0. Tổng Quan

Framework mô tả **CƠ CHẾ** tạo động lực và hành vi con người.

**Nguyên lý cốt lõi:** Não = hệ thống desire + prediction.
Vô thức có **desire** (mong muốn) liên tục — khi thực tế **match** desire → dopamine fire → hành vi.
🟢 Nền tảng: Schultz 1997 (PE), Berridge 1998 (wanting/liking), Panksepp 1998 (SEEKING).
🟡 Mở rộng: Unconscious Desire (UD) — desire fulfillment thay vì prediction error.
→ Chi tiết: Research/UD-Hypothesis.md

Não mã hóa dự đoán thành **predictive-chunks** — đơn vị dự đoán nhỏ nhất.
Chunks kết nối với nhau tạo thành **schema** — hệ thống có ý nghĩa.
Schema chạy trên **hardware** sinh hóa, trong **môi trường** cụ thể, sinh ra **hành vi** quan sát được.

**"Công thức, không đáp án":** Framework cho CÔNG THỨC để tính, không cho đáp án sẵn.
Giống F=ma: không nói "vật rơi nhanh bao nhiêu" — ai có biến số cụ thể thì tính được.

**KHÔNG PHẢI personality test.** Không có 4 loại người.
Mô Hình Vuông (Source × Depth) = phổ liên tục, đánh giá per domain, thay đổi theo thời gian.

---

## 1. Kiến Trúc Tổng Thể

> **KHUNG CHÍNH** — Container model: Con người sống TRONG môi trường.
> Hardware + Software + Hành Vi = CON NGƯỜI (internal system).
> Môi Trường = CONTEXT bao quanh, feed vào + bị thay đổi bởi con người.
> Domain = QUY LUẬT NỀN xuyên suốt.

```
╔══════════════════════════════════════════════════════════════════╗
║  MÔI TRƯỜNG (Container — bao quanh con người)                   ║
║  Vật chất · Kết nối · Văn hóa · Kinh tế · Thời đại             ║
║  → Feed vào TẤT CẢ tầng: T1 + T2 + T3                          ║
║  ← Bị THAY ĐỔI bởi T3 (hành vi)                                ║
║                                                                  ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │  CON NGƯỜI (Internal system)                               │  ║
║  │                                                            │  ║
║  │  T1: HARDWARE (Sinh hóa — Nền tảng)                       │  ║
║  │  "Não được trang bị gì"                                    │  ║
║  │  Neurochemistry (3 lớp) · Parameters · Processing Infra     │  ║
║  │  Đặc điểm: Gen quy định · Thay đổi chậm (năm-thập kỷ)    │  ║
║  │                                                            │  ║
║  │          ↓ set phạm vi + process signals                   │  ║
║  │                                                            │  ║
║  │  T2: SOFTWARE (Nhận thức — Nội tại)                        │  ║
║  │  "Não xây dựng gì từ hardware × môi trường"                │  ║
║  │  Chunks · Schema · Drive Equation · Emotion (readout)      │  ║
║  │  Đặc điểm: Learned · Mỗi người KHÁC · Thay đổi liên tục  │  ║
║  │                                                            │  ║
║  │          ↓ decision                                        │  ║
║  │                                                            │  ║
║  │  T3: HÀNH VI (Output — Quan sát được)                      │  ║
║  │  "Não làm gì"                                             │  ║
║  │  = f(T1 × T2 × Môi Trường)                                │  ║
║  │  Đặc điểm: Observable · Measurable · Predictable           │  ║
║  │                                                            │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  ← T3 thay đổi Môi Trường (hành vi tác động ra ngoài)          ║
║  → Môi Trường feed ngược vào T1, T2 (continuous loop)           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

  DOMAIN (quy luật nền — xuyên suốt Container + Con Người):
  Objective (vật lý) · Abstract (toán/logic) ·
  Intersubjective (xã hội) · Subjective (trải nghiệm)
  → Benchmark: schema đúng/sai = match domain hay không
```

**Master Formula (v7):**
```
Hành Vi = f(Hardware × Software × Môi Trường)

Trong đó:
  Hardware  = Neurochemistry (3 lớp) × Parameters × Processing Infrastructure
              Lớp 1 Source (Opioid + Oxytocin)
              × Lớp 2 Amplifier (Dopamine + Serotonin)
              × Lớp 3 Modulator (Cortisol, NE, Vasopressin, Prolactin, Endocannabinoid)
  Software  = Chunks × Schema × Drive Equation
  Môi Trường = Vật chất × Kết nối × Văn hóa × Kinh tế × Thời đại

  Software = f(Hardware × Môi Trường × Thời gian)
  → Software PHỤ THUỘC cả Hardware lẫn Môi Trường
  → Đây là tầng tạo INDIVIDUALITY (cùng hardware, cùng môi trường → vẫn khác software)

  Vị trí trên Mô Hình Vuông (Source × Depth) per domain = pattern quan sát T3
```

**Tại sao Container model:**
```
v6: Bối cảnh = Tầng -1 (1 layer trong pipeline)
v7: Môi Trường = Container (bao quanh toàn bộ pipeline)

Lý do thay đổi:
  1. Môi Trường tác động lên TẤT CẢ tầng, không chỉ 1
     - T1: stress → cortisol tăng, dinh dưỡng → brain development
     - T2: giáo dục → chunks input, văn hóa → schema installed
     - T3: context quyết định hành vi NÀO được execute
  2. Hardware + Software + Hành Vi = CON NGƯỜI (internal, liền mạch)
     Môi Trường = NGOÀI con người (external)
     → Xỏ cái ngoài vào giữa 3 cái trong = phá coherence
  3. "Con người sống trong môi trường" = đúng trực giác
     "Con người đi qua bối cảnh rồi tới phần cứng" = lệch
```

---

## 2. Môi Trường (Container)

Môi Trường KHÔNG phải bước trong pipeline — là BỐI CẢNH bao quanh.
Giống nước với cá: nước ảnh hưởng MỌI THỨ của cá, nhưng không phải bộ phận của cá.

### 2.1 Các thành phần

```
VẬT CHẤT:    Nhà ở, thành phố, thiên nhiên, công cụ, thời tiết
KẾT NỐI:     Gia đình, bạn bè, đồng nghiệp, cộng đồng, MXH
VĂN HÓA:     Ngôn ngữ, giá trị, chuẩn mực, tôn giáo, thể chế
KINH TẾ:      Tài nguyên, thu nhập, cơ hội, áp lực tài chính
THỜI ĐẠI:     Công nghệ available, thông tin, thị trường lao động
```

### 2.2 Môi Trường tác động lên mỗi tầng

```
→ T1 Hardware:
  Stress mãn tính → cortisol baseline tăng
  Dinh dưỡng → brain development (đặc biệt trẻ em)
  Chất kích thích → thay đổi threshold, sensitivity
  Ô nhiễm → hardware damage

→ T2 Software:
  Giáo dục → chunks input (external knowledge)
  Văn hóa → schema installed ("đàn ông phải...", "gia đình là...")
  Người xung quanh → shape schema sâu (L4-L5 trong Beck's model)
  MXH → threshold tăng (dopamine flooding)

→ T3 Hành Vi:
  Context quyết định hành vi NÀO available
  Ở nhà → nói thẳng. Ở công ty → nói vòng. Cùng software, khác output.
  Có công cụ → hành vi mới possible (internet → learn anything)
```

### 2.3 Bottleneck Analysis

```
Cùng 1 đứa trẻ (hardware GIỐNG HỆT):

Đặt ở thành phố (môi trường giàu):
  → chunks PHONG PHÚ, schema RỘNG → hành vi đa dạng

Đặt ở núi rừng (môi trường nghèo):
  → chunks HẠN CHẾ, schema HẸP → hành vi giới hạn hơn
  → Nhưng SÂU hơn trong domain khác (sinh tồn, tự nhiên)

→ Hardware tốt + Môi trường nghèo: Bottleneck = MÔI TRƯỜNG
→ Hardware hạn chế + Môi trường giàu: Bottleneck = HARDWARE
→ Cả hai tốt: SOFTWARE quality quyết định (individuality)
→ Cả hai hạn chế: Double bottleneck → hành vi bị giới hạn nặng
```

### 2.4 External Chunk Pressure (trước: Soldier Gravity)

Lực kéo CÓ HỆ THỐNG của cấu trúc xã hội làm mọi người di chuyển về phía EXTERNAL
trên Mô Hình Vuông. Không phải conspiracy — là population dynamics thuần túy.

```
4 lực kéo:
  LỰC 1 — Demand:      50-60% cần structure rõ → thị trường phục vụ majority
  LỰC 2 — Selection:    Institution cần vận hành → tuyển người follow quy trình
  LỰC 3 — Feedback:     Soldier vận hành thành công → structure REINFORCED
  LỰC 4 — Socialization: 12-16 năm giáo dục train external pattern

Anti-Pressure:
  Crisis → structure cũ sụp → cơ hội innovation
  Technology → phá monopoly → internal có platform
  Education (đúng thiết kế) → xây chunk internal từ nhỏ

→ Chi tiết: Core-Deep-Dive/Society-Dynamics.md
```

### 2.5 Source Ratio Shift Per Thời Đại

```
Thiên hướng (gen): ~constant qua thời kỳ
Biểu hiện (environment × hardware): CÓ THỂ shift mạnh

| Thời đại           | External biểu hiện | Internal biểu hiện |
|---------------------|--------------------|--------------------|
| Săn bắn hái lượm    | ~40-50%            | ~35-40%            |
| Phong kiến           | ~70-80%            | ~15-20%            |
| Công nghiệp          | ~60-70%            | ~22-27%            |
| Hậu công nghiệp      | ~50-60%            | ~30-37%            |
| AI Era               | ~40-50%?           | ~35%? Drifter tăng?|

→ Chi tiết: Core-Deep-Dive/Society-Dynamics.md
```

---

## 3. T1: Hardware — Nền Tảng Sinh Hóa

"Não được trang bị gì" — gen quy định phần lớn, thay đổi chậm.

### 3.1 Neurochemistry — Kiến Trúc 3 Lớp

Hệ thần kinh hóa học được tổ chức thành 3 lớp chức năng:

```
╔══════════════════════════════════════════════════════╗
║  LỚP 1: NGUỒN (Source) — "Con người muốn gì?"       ║
║  = 2 nguồn DESIRE duy nhất                          ║
║  Mọi thứ con người muốn → cuối cùng về 1 hoặc cả 2 ║
║                                                      ║
║  😌 OPIOID — Desire về CẢM NHẬN                     ║
║     Taste, beauty, warmth, coherence, pleasure       ║
║     "Đẹp quá!" = Opioid. Runner's high = endorphin. ║
║     🟢 Berridge & Robinson, 1998. Gen: OPRM1.        ║
║                                                      ║
║  🤝 OXYTOCIN — Desire về GẮN BÓ                     ║
║     Connection, belonging, being understood          ║
║     Gắn bó lành mạnh VÀ không lành mạnh (trauma).   ║
║     Mặt tối: in-group → CÓ THỂ tăng thù địch out.  ║
║     🟢 Young & Wang, 2004. Gen: OXTR.                ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  LỚP 2: KHUẾCH ĐẠI (Amplifier) — "Mạnh thế nào?"   ║
║  = 2 amplifier MẠNH NHẤT, ảnh hưởng hành vi rõ nhất ║
║                                                      ║
║  💡 DOPAMINE (Novelty) — "Desire vừa được match!"    ║
║     Detect + signal + mở rộng tìm kiếm               ║
║     PE ∝ desire fulfilled − pre-simulated             ║
║     Explore (domain mới) + Deepen (kết nối mới)      ║
║     🟢 Schultz et al., 1997. Gen: DRD4, COMT, DAT1. ║
║                                                      ║
║     🟡 GHI CHÚ BẢN CHẤT:                             ║
║     Dopamine có thể là INFRASTRUCTURE (công tắc),    ║
║     không phải SOURCE (nguồn điện).                  ║
║     Test: Novelty detect → cảm xúc GÌ xuất hiện?    ║
║       "Aha!" → SƯỚNG (opioid)                       ║
║       "Người mới hay!" → ẤM (oxytocin)              ║
║       → Novelty LUÔN dẫn tới opioid/oxytocin        ║
║       → Novelty ALONE = trung tính, không có valence ║
║     Tuy nhiên: Novelty CỰC KỲ quan trọng cho       ║
║     predict hành vi → GIỮA vị trí Amplifier hàng đầu║
║     → Chi tiết: Research/UD-Hypothesis.md §Q-NEW-7   ║
║                                                      ║
║  ⚖️ SEROTONIN (Status) — "Tôi ở vị trí tốt!"        ║
║     MULTIPLIER trên tất cả, không tạo desire riêng.  ║
║     Cao → confident, ổn định. Thấp → so sánh, bất mãn║
║     ⚠️ "Nghiện địa vị" = nghiện multi-channel BURST  ║
║        mà status mang lại, không phải nghiện status.  ║
║     🟢 Raleigh et al., 1991.                         ║
║                                                      ║
╠══════════════════════════════════════════════════════╣
║  LỚP 3: ĐIỀU CHỈNH (Modulator) — "Fine-tuning"     ║
║  = Tác động QUA lớp 1 + 2, không tạo desire riêng   ║
║                                                      ║
║  🛡️ CORTISOL/GABA — Phanh / threat signal            ║
║     Inverted-U: moderate = drive tối ưu.             ║
║     Cao mãn tính = PFC sụp → Soldier pattern.       ║
║     3 biến: liều, thời gian, controllability.        ║
║     → Tác động: suppress opioid + oxytocin + dopamine║
║     🟢 de Kloet 1998; Maier & Seligman 2016.         ║
║                                                      ║
║  ⚡ NE (Norepinephrine) — Arousal / alertness         ║
║     Khuếch đại ATTENTION → giúp dopamine detect.    ║
║     → Tác động chủ yếu qua Lớp 2 (dopamine).       ║
║                                                      ║
║  🔒 VASOPRESSIN — Territorial / protective            ║
║     Mặt phòng thủ: "bảo vệ cái mình yêu."          ║
║     → Tác động qua Lớp 1 (oxytocin).                ║
║                                                      ║
║  🍼 PROLACTIN — Nurturing / brake ("đủ rồi")         ║
║     Đối trọng dopamine (gas vs brake).               ║
║     Post-satisfaction: supplement opioid.             ║
║     → Tác động qua Lớp 1 (opioid) + Lớp 2 (dopamine)║
║                                                      ║
║  🌿 ENDOCANNABINOID — Relaxation / reward modulation  ║
║     Runner's high, chill, pain modulation.           ║
║     → Tác động qua Lớp 1 (opioid).                  ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

→ Chi tiết: Core-Deep-Dive/Neurochemistry.md
→ Giả thiết Novelty = infrastructure: Research/UD-Hypothesis.md §Q-NEW-7
```

```
⚠️ LƯU Ý QUAN TRỌNG VỀ DOPAMINE/NOVELTY:

  TRÌNH BÀY (practical, cho predict hành vi):
    Novelty ở Lớp 2 Amplifier — đầu tiên, phổ biến nhất
    → Vì predictive power cực cao: novelty-seeking = observable
    → Và tầm quan trọng TĂNG theo thời đại (AI era → more domains → more novelty)

  BẢN CHẤT (neuroscience, behind the scenes):
    Dopamine có thể là INFRASTRUCTURE — signal "desire matched"
    → Opioid + Oxytocin = 2 nguồn desire DUY NHẤT
    → Dopamine = công tắc (detect + signal), không phải nguồn điện
    → Serotonin = biến áp (amplify), không phải nguồn điện

  → Trình bày ≠ Bản chất, và điều đó OK
  → Giống vật lý dạy Newton trước, Einstein sau
  → Chi tiết phân tích: Research/UD-Hypothesis.md
```

### 3.3 Parameters — Tham Số Nền

```
📦 CAPACITY — Trần chunk complexity:
  PFC + Working Memory = ceiling cho chunk phức tạp nhất có thể xây.
  Capacity ≠ Activation Level:
    Capacity (trần) = hardware ceiling. Gen. Thay đổi rất chậm.
    Activation Level = % Capacity ĐANG DÙNG. Thay đổi liên tục.
    Cortisol modulate Activation, KHÔNG modulate Capacity.
  🟢 Miller 1956, Cowan 2001.

📏 THRESHOLD — ★ THAM SỐ QUAN TRỌNG NHẤT:
  Mức PE tối thiểu để cảm thấy "đủ."
  Thấp → chunk nhỏ đủ PE → dễ hài lòng.
  Cao → buộc xây chunk lớn hơn HOẶC tự tạo (internal).
  Calibrate CHẬM: MXH → threshold TĂNG. Thiền, tự nhiên → threshold GIẢM.
  🟢 Volkow et al. (2002).

📡 PE SENSITIVITY — Cách não xử lý PE:
  4 sub-mechanisms:
    ① Amplitude — volume tín hiệu DA
    ② Precision weighting — PE đáng tin cỡ nào
    ③ PE Decay Rate — tốc độ chunk "cháy" PE (per channel)
    ④ Generalization scope — chán 1 chunk hay chán cả loại
  → Chi tiết: Core-Deep-Dive/PE-Sensitivity.md

🔋 BASELINE DRIVE — Luôn > 0, adaptive:
  PE deficit kéo dài → baseline GIẢM → apathy.
  PE surplus kéo dài → baseline TĂNG → bồn chồn.
  "Chán" = PE hiện tại < baseline hiện tại.

★ BỘ BA DỰ ĐOÁN:
  Threshold × PE Sensitivity × Kênh gốc = predict phần lớn hành vi.
```

### 3.4 Processing Infrastructure — Vùng Não + PFC as Conductor

🟡 Section mới v7. Quan trọng cho hiểu cách T2 Software thực sự chạy.

```
VÙNG NÃO CHÍNH:
  PFC (Prefrontal Cortex):   Điều phối, working memory, inhibition
  Amygdala:                  Threat detection, emotional tagging
  Hippocampus:               Memory formation, context association
  Basal Ganglia:             Habit formation, procedural learning
  Cerebellum:                Motor automation, timing
  ACC (Anterior Cingulate):  Conflict monitoring, error detection
  Insula:                    Body awareness, "tôi đang cảm thấy gì?"
  DMN (Default Mode Network): Self-referential, "tôi là ai?"
  Temporal Cortex:           Semantic memory, categories
```

```
⚠️ PFC = CONDUCTOR (Nhạc trưởng), KHÔNG PHẢI processor:

  PFC KHÔNG "nghĩ ra" — PFC "nhận kết quả từ vô thức và điều phối":
    - Set INTENTION / QUESTION (đặt câu hỏi)
    - HOLD vấn đề trong working memory (giữ đủ lâu)
    - EVALUATE kết quả (đúng/sai, dùng/bỏ)
    - INHIBIT output không phù hợp (chặn hành vi, không chặn suy nghĩ)
    - SEQUENCE các bước (làm gì trước, gì sau)

  PFC KHÔNG LÀM:
    - Compute kết quả (vô thức làm)
    - Control nội dung suy nghĩ ("đừng nghĩ voi hồng" → vẫn nghĩ)
    - Quyết định trước khi vô thức compute (Libet 1983: brain decides ~500ms trước PFC)

  Bằng chứng:
    🟢 Libet (1983): readiness potential trước conscious decision
    🟢 Gazzaniga: split-brain → PFC tạo story giải thích, không ra lệnh
    🟢 Expert bypass: grandmaster cờ vua → PFC THẤP, BG+temporal HIGH
    🟢 Amygdala reacts ~12ms, PFC ~200-500ms → sợ trước khi biết tại sao

  Ví dụ không thể phủ nhận:

    NÓI MỘT CÂU: "Hôm nay trời đẹp quá"
      PFC contribution: CHỈ CÓ INTENTION ("nói gì đó về thời tiết")
      Toàn bộ từ ngữ, ngữ pháp, intonation: VÔ THỨC generate
      Thử predict câu tiếp theo TRƯỚC KHI nói → không được
      → Câu được generate real-time bởi vô thức

    NHẬN MẶT MẸ:
      ~100ms: BIẾT đây là mẹ (fusiform face area)
      ~300ms: PFC bắt đầu process
      → Nhận ra TRƯỚC KHI PFC kịp "nghĩ"
      → Tốc độ phản hồi cho thấy PFC không phải nơi nhận dạng

    "ĐỪNG NGHĨ TỚI CON VOI HỒNG":
      PFC ra lệnh "đừng" → hình ảnh VẪN XUẤT HIỆN
      → Content generation = VÔ THỨC, PFC chỉ inhibit OUTPUT

    EUREKA MOMENT:
      Nghĩ 2 tiếng không ra. Đi tắm. BỐP — đáp án xuất hiện.
      → Đáp án đến KHI PFC KHÔNG active
      → Computation xảy ra ở NƠI KHÁC

    TÍNH 8×9:
      Case A — đã thuộc bảng cửu chương:
        "72" XUẤT HIỆN trong ý thức. PFC NHẬN kết quả. Không tính.

      Case B — tính thủ công (8+8+8+8+8+8+8+8+8):
        Mỗi bước: "8+8=?" → "16" XUẤT HIỆN → PFC không tính
        PFC chỉ: HOLD kết quả tạm + SEQUENCE bước tiếp theo
        = Quản lý dự án, không phải thợ xây

      Case C — trẻ con tính 3+4:
        Đếm ngón tay: 1,2,3...4,5,6,7
        Mỗi số tiếp theo: "sau 5 là..." → "6" XUẤT HIỆN
        PFC không tính. Retrieve từ chuỗi đã học.
        Trẻ chưa "hiểu" 3 nghĩa là gì — chỉ thuộc chuỗi (âm thanh, hình ảnh, ý nghĩa,...)
        Sau khi lặp đủ nhiều: 3+4→7 chunk lại → BG store → lần sau xuất hiện ngay

  ⚠️ INSIGHT: Không có level nào PFC thực sự COMPUTE.
  → Đếm = retrieve chuỗi đã thuộc
  → Cộng = đếm = retrieve
  → Nhân = cộng lặp = đếm lặp = retrieve lặp
  → Tất cả arithmetic cuối cùng = MEMORY RETRIEVAL, không phải computation
  → PFC chỉ QUẢN LÝ quy trình retrieve

  Tổng hợp — pattern không thể phủ nhận:

    1. PFC set INTENTION / QUESTION
    2. Vô thức COMPUTE
    3. Kết quả XUẤT HIỆN trong conscious
    4. PFC EVALUATE kết quả (đúng/sai, dùng/bỏ)

    PFC KHÔNG BAO GIỜ ở bước 2.

    Ý thức = Giám đốc ngồi trong phòng:
      → Đặt câu hỏi cho team (intention)
      → Team đi làm (unconscious compute)
      → Team mang kết quả lại (result appears)
      → Giám đốc approve/reject (evaluate)
      → Giám đốc NGHĨ mình thông minh
      → Nhưng thực ra team làm hết

    ⚠️ Nhưng giám đốc KHÔNG vô dụng:
      Team GIỎI = nỗ lực ĐIỀU PHỐI của giám đốc từ nhỏ đến lớn.
      Giám đốc chọn team nào được thuê (attention allocation),
      quyết định project nào ưu tiên (goal setting),
      evaluate kết quả và redirect (quality control).
      Team giỏi CẦN giám đốc giỏi, và ngược lại.
```

```
ENCODING MODALITY — Schema encoded ở NHIỀU vùng não:

  Verbal:    Broca + Wernicke → conscious nhất (nói ra được)
  Visual:    Visual cortex → semi-conscious (thấy nhưng khó mô tả)
  Somatic:   Insula + Somatosensory → thường VÔ THỨC (body feels)
  Motor:     Motor cortex + BG + Cerebellum → vô thức khi compiled
  Emotional: Amygdala + Insula → phần lớn VÔ THỨC

  Mỗi modality = vùng não RIÊNG, xử lý RIÊNG.
  1 schema có thể encoded ở NHIỀU modalities đồng thời.

  Ví dụ schema "phải tự lực":
    Verbal:    "Tôi phải tự làm" (articulate được)
    Somatic:   Cổ họng thắt khi sắp nhờ ai (khó articulate)
    Emotional: Shame khi dependent (fast, trước verbal)
    Visual:    Flash image: bố mắng "sao yếu vậy?"
    Motor:     Tay rụt lại khi sắp với tới

  → Tại sao "biết nhưng không làm được":
    Talk therapy target VERBAL encoding → PFC update → "biết"
    Nhưng Somatic + Emotional + Motor CHƯA update → "không làm được"
    → Schema encoded ở N modalities = cần sửa ở N modalities

  → Difficulty to change ∝ (số modalities × số brain regions) encoded
    PFC chỉ access trực tiếp VERBAL modality
    Các modality khác cần intervention riêng phù hợp:
      EMDR → visual + somatic
      Somatic Experiencing → body directly
      Exposure therapy → motor + emotional
      Psychedelic-assisted → nhiều modalities cùng lúc
```

```
MULTI-REGION PROCESSING — Schema sâu = nhiều vùng não:

  Schema surface (#01-15 trong 50-schema analysis):
    → 1-2 vùng dominant (Basal Ganglia, Temporal)
    → Sửa dễ: chỉ cần update 1-2 vùng

  Schema deep (#31-50):
    → 3-4 vùng đồng thời (DMN + Amygdala + Insula + ACC)
    → Sửa khó: update 1 vùng → các vùng khác giữ version cũ → revert

  → "Deep schema khó sửa" KHÔNG phải vì "sâu"
  → Mà vì PHÂN TÁN qua nhiều vùng não đồng thời
```

---

## 4. T2: Software — Nhận Thức Nội Tại

"Não xây dựng gì" — learned qua experience, mỗi người KHÁC nhau.
Software = f(Hardware × Môi Trường × Thời gian).
Tầng tạo INDIVIDUALITY: cùng hardware + cùng môi trường → vẫn khác software.

### 4.1 Predictive-Chunks — Đơn Vị Cơ Bản

```
Chunk = đơn vị dự đoán nhỏ nhất của não.
  🟢 Miller (1956): WM ~7±2 chunks. Cowan (2001): ~4 items.

  Muôn hình vạn trạng:
    "Trời mưa → mang ô" = 1 chunk
    "F=ma" = 1 chunk
    "Mẹ tôi yêu tôi" = 1 chunk
    "Guitar Am→C→G→F" = 1 chunk (sau khi compiled)

  2 trục chính:
    SOURCE: external (copy từ bên ngoài) ←→ internal (tự xây)
    DEPTH:  composite parameter gồm 4 sub:
      ① Chunk quality — prediction accuracy
      ② Connectivity (sync) — mức liên kết giữa chunks
      ③ Cluster formation — chunks tổ chức thành cụm domain
      ④ Cluster maturity — cụm domain ổn định bao lâu

  Multi-modal encoding:
    Mỗi chunk có thể encoded ở nhiều modalities (verbal, somatic, visual, motor, emotional)
    → Across nhiều brain regions đồng thời (xem §3.4)

  Per domain:
    Cùng 1 người có chunk config KHÁC NHAU giữa các domain.
    Lập trình viên: deep + internal ở coding, shallow + external ở nấu ăn.
```

### 4.2 Schema — Kết Nối Chunks → Ý Nghĩa

```
Schema = kết nối giữa chunks tạo thành hệ thống có ý nghĩa.
  🟢 Piaget (1952), Beck (1967): Schema theory.

  Schema ≠ chunk đơn lẻ.
  Schema = PATTERN OF CONNECTIONS giữa chunks.
  → Giống: chunks = từ, schema = câu/đoạn văn/bài luận.

  4 schema nền ảnh hưởng MỌI prediction:
    1. Schema bản thân:   "tôi giỏi/kém" → prediction confidence nền
    2. Schema thế giới:   "thế giới an toàn/nguy hiểm" → prediction cost nền
    3. Schema người khác: "người khác đáng tin/không" → external source nền
    4. Schema tương lai:  "tương lai kiểm soát được/không" → prediction horizon nền

  Schema override:
    Schema đủ mạnh CÓ THỂ override survival instinct.
    🟢 Swann et al. (2012): identity fusion → lính chết cho đồng đội.
    Cơ chế: schema THAY ĐỔI phép tính drive equation, không phải "dũng cảm."
    Chi tiết competition model: Core.md v6 §7.4.

  Schema lifecycle: Explore → Deepen → Connect → Monitor.
    Mỗi phase cần PFC KHÁC LOẠI (không phải ít hơn).
    Chi tiết: Core.md v6 §6.1.

  ⚠️ SCHEMA — CÒN ĐANG NGHIÊN CỨU:
    Schema có thể decompose thành nhiều lớp (surface → deep).
    Nền tảng: Beck (3 tầng), Friston (continuous hierarchy).
    Framework đang explore: 3 clusters vs 4 layers vs gradient.
    Ranh giới giữa các lớp = gradient, không discrete.
    Schema map theo VÙNG NÃO (5 processing systems), không chỉ theo "depth."
    → Chi tiết: Research/Component-Interaction-Map.md §9.
```

### 4.3 Drive Equation

```
DRIVE = Prediction Reward − Prediction Cost

  Reward = desire fulfillment dự kiến × confidence × source channel match
         + urgency bonus (cortisol moderate → DA↑)
  Cost   = effort (PFC load) + threat (cortisol cao)
         + social cost + opportunity cost

Drive lấy input XUYÊN TẦNG:
  T1 (hardware state): cortisol level, dopamine level, energy
  T2 (predictions): schema predict PE dự kiến, confidence
  Container (môi trường): threat thực tế, social context, opportunity
  → Kết quả Drive = INTERNAL (không ai thấy từ bên ngoài)
  → Drive → T3 Hành Vi (execute action)

⚠️ Cortisol xuất hiện Ở CẢ HAI VẾ:
  Moderate cortisol → REWARD (urgency bonus, DA tăng)
  High cortisol → COST (threat, PFC ức chế)

"Biết mà không làm" = Reward (yếu) − Cost (mạnh) < 0.
  KHÔNG phải thiếu ý chí — là drive equation âm.
  Can thiệp: tăng reward HOẶC giảm cost.

→ Chi tiết: Core.md v6 §7.
```

### 4.4 Emotion — Readout Signal (Cross-cutting)

🟡 Section mới v7.

```
Cảm xúc KHÔNG phải tầng riêng — là SIGNAL chạy GIỮA các tầng:
  T1 generate (Amygdala, Insula, dopamine system)
  T2 interpret (schema label: "tôi đang sợ")
  Container trigger (môi trường tạo stimulus)
  T3 express (biểu hiện ra ngoài)

Emotion = READOUT của PE system:
  Mỗi cảm xúc = 1 signal cụ thể về trạng thái PE.

  6 chiều xác định emotion:
    1. Kênh nào dominant (dopamine/opioid/oxytocin/cortisol)
    2. PE dấu gì (+/–/mixed)
    3. Thời gian (quá khứ/hiện tại/tương lai)
    4. Schema depth (surface → deep)
    5. Certainty (confident/uncertain)
    6. Intensity (nhẹ/mạnh)

  Ví dụ mapping:
    Lo âu = predict PE ÂM trong tương lai + uncertain
    Hy vọng = predict PE DƯƠNG trong tương lai + uncertain
    → Cùng cơ chế, ngược dấu

    Guilt = schema HÀNH VI bị violated (L3-L4) → "tôi LÀM sai"
    Shame = schema SELF bị violated (L4-L5) → "tôi SAI"
    → Cùng cơ chế, khác depth

    Xúc động = deep schema CONFIRMED → opioid + body response
    Awe = deep schema OVERWHELMED → schema EXPANDED
    → Cùng deep trigger, khác direction

    Chán = PE ≈ 0 → đây chính là PE Decay Rate observable
    Tuyệt vọng = KHÔNG CÒN predict PE dương NÀO trong tương lai

→ Chi tiết: Research/Emotion-Map.md
```

---

## 5. T3: Hành Vi — Output Quan Sát Được

"Não làm gì" — output cuối cùng, observable.

### 5.1 Hành Vi = f(T1 × T2 × Môi Trường)

```
Hành vi KHÔNG phải software:
  Software = prediction, model, internal
  Hành vi = THỰC HIỆN prediction, external, observable
  Cùng software → KHÁC hành vi tùy môi trường:
    Schema "muốn nói thật" + ở nhà → nói thẳng
    Schema "muốn nói thật" + ở công ty → nói vòng

Ba tầng hành vi:
  REFLEX (<200ms):        Bẩm sinh. Rụt tay, giật mình.
  PREDICTION ACTIVE:      PFC quyết định. Tốn năng lượng.
  PREDICTION TỰ ĐỘNG:    Myelinate. Lái xe, workflow quen. Nhẹ.
  🟢 Myelinate: 2-8 tháng (Lally et al., 2010).
  Người lớn: ~70% tự động, ~20% active, ~10% reflex.
```

### 5.2 Mô Hình Vuông — Diagnostic Lens cho Hành Vi

```
Mô Hình Vuông = LENS để quan sát pattern hành vi.
Không phải cơ chế — là NHÃN MÔ TẢ vị trí trên phổ liên tục.

                      ARCHITECT
              ┌─────────────────────┐
              │                     │
  IMPROVISER  │   Phổ liên tục     │  SOLDIER
              │   per domain        │
              │                     │
              └─────────────────────┘
                      DRIFTER

  X: Internal ←── SOURCE ──→ External
  Y: Shallow ──── DEPTH ──→ Deep

  4 nhãn = 4 CẠNH (extreme positions), không phải 4 kiểu người.
  Mỗi person × domain = 1 VỊ TRÍ bên trong hình vuông.
  Vị trí KHÁC NHAU per domain. THAY ĐỔI theo thời gian.

→ Chi tiết: Core.md v6 §8.
```

### 5.3 Feedback Loops

```
T3 → Container (Môi Trường):
  Hành vi THAY ĐỔI môi trường: xây nhà, nói chuyện, viết sách
  → Môi trường mới → feed mới cho T1 + T2

T3 → T2 (Software):
  Kết quả hành vi → update schema: "cách này đúng/sai"
  = Learning loop. PE từ kết quả → chunk mới hoặc update chunk cũ.
  ⚠️ Schema override HÀNH VI nhưng KHÔNG override ENCODING:
    Van Gogh vẽ dù đói (schema drive) + GHI {vẽ = đói, khổ} (encoding vẫn chạy)
    → Output CÓ + chunk tiêu cực CŨNG CÓ → burnout tích lũy.

T3 → T1 (Hardware) — dài hạn:
  Usage mãn tính thay đổi hardware:
    Tập gym → cơ bắp + neuroplasticity
    Stress kéo dài → cortisol baseline tăng
    MXH liên tục → threshold tăng (D2 downregulate)
    Thiền → cortisol giảm, attention circuits strengthened
```

---

## 6. Domain — Quy Luật Nền

```
Domain KHÔNG phải tầng — là CHIỀU NGANG xuyên suốt.
= "Luật chơi" mà mọi tầng đều tuân theo.

4 loại Domain:
  Objective:       Vật lý, hóa, sinh — tồn tại khách quan
  Abstract:        Toán, logic — consistent, verify được
  Intersubjective: Xã hội, chính trị — shared nhưng mutable
  Subjective:      Nghệ thuật, trải nghiệm — real nhưng cá nhân

Domain xuyên suốt:
  T1 tuân theo domain sinh học (não = vật chất, tuân theo vật lý/hóa)
  T2 cố MODEL domain (schema = bản đồ, domain = lãnh thổ)
  Container tuân theo domain (nước vẫn sôi dù không ai biết)
  T3 hiệu quả khi match domain (hành vi đúng = đúng quy luật)

  → Schema đúng domain = hành vi hiệu quả → PE dương → reinforce
  → Schema sai domain = hành vi thất bại → PE âm → update (hoặc không)

Domain KHÔNG tương tác trực tiếp lên người:
  "Nước sôi ở 100°C" = domain rule
  → CHỈ KHI bỏ tay vào nước sôi (hành vi + môi trường) → rule manifest
  → Domain tương tác QUA môi trường, không trực tiếp

  → Domain = class definition, Môi trường = object instance
```

---

## 7. Luồng Xử Lý + Feedback Loops

### 7.1 Pipeline chính (Real-time)

```
Mỗi khoảnh khắc:

Container (stimulus đến)
  → T1 Hardware (nhận signal: mắt/tai → Amygdala route → dopamine fire)
    → T2 Software (chunks activate → schema predict → drive tính → decision)
      → T3 Hành Vi (execute action)
        → Container (bị thay đổi)
          → T1 → T2 → T3 → ... loop

⚠️ Phần lớn loop này là VÔ THỨC.
PFC (trong T1) chỉ can thiệp khi: MỚI / KHÓ / CONFLICT.
Routine processing: Amygdala + BG + Temporal tự handle.
```

### 7.2 Development pipeline (Cả đời)

```
Container (nuôi dưỡng, giáo dục, văn hóa)
  → T1 Hardware (phát triển não: gen × dinh dưỡng × stress)
    → T2 Software (build chunks + schema từ T1 × Container × time)
      → T3 Hành Vi (thay đổi Container cho thế hệ sau)

Tốc độ thay đổi:
  Container:  giây → ngày (stimulus liên tục)
  T1 Hardware: năm → thập kỷ (gen + aging + chronic usage)
  T2 Software: giờ → năm (surface chunks nhanh, deep schema chậm)
  T3 Hành Vi:  ms → giây (real-time output)
  Domain:      ít thay đổi (vật lý constant, xã hội chậm)
```

### 7.3 Cortisol × Dopamine — 2 Hệ Cân Bằng Riêng

```
HAI INVERTED-U SONG SONG:

  CORTISOL INVERTED-U — HƯỚNG hành vi (approach ↔ avoidance)
  DOPAMINE INVERTED-U — ĐỘ SÂU hành vi (depth ↔ breadth)

  Hai hệ INDEPENDENT nhưng có cross-talk:
    Cortisol moderate → DA TĂNG (cộng tác)
    Cortisol cao mãn tính → DA GIẢM (ức chế)

→ Chi tiết: Core.md v6 §6.4, Neurochemistry.md §6.
```

---

## 8. Emergence Phase + Can Thiệp

### 8.1 Ba Giai Đoạn

```
Bỏ prediction ngắn bắt buộc → External Pressure GIẢM → config thật NỔI LÊN:

  GĐ 1 — RECOVERY (1-4 tuần):   Hạ cortisol. PFC bắt đầu bình thường.
  GĐ 2 — HABITUATION (4-12 tuần): PE ngắn hạn cạn. Bồn chồn.
  GĐ 3 — EMERGENCE (3+ tháng):   Chunk config thật lộ ra.
```

### 8.2 Thứ Tự Can Thiệp — 6 Bước

```
1. TỐI ƯU CORTISOL → PFC hoạt động bình thường
2. SỬA SCHEMA (4 schema nền)
3. XÂY prediction xa + giảm cost
4. BẢO VỆ prediction xa (tránh overjustification)
5. CALIBRATE threshold
6. NHẬN DIỆN chunk config thật PER DOMAIN

→ Bước 1 luôn ĐẦU TIÊN. Không skip.
```

---

## 9. Câu Hỏi Mở + Gaps

### 9.1 Câu hỏi từ v6 (chưa giải quyết)

```
- Threshold range thay đổi bao nhiêu? Bao lâu để calibrate?
- Chunk depth per domain: đo bằng gì chính xác?
- True vs Forced external: diagnostic protocol qua chunk config?
- Generalization scope (④): encoding modality → ④ confirm?
- Prolactin hypothesis: healthy/pathological boundary?
```

### 9.2 Câu hỏi mới từ v7

```
Q-NEW-1: Schema decomposition — 3 clusters vs 4 layers vs gradient?
  Beck có 3 tầng. Friston có continuous hierarchy.
  50-schema analysis gợi ý 3-4 clusters + gradient bên trong.
  → Cần thêm phân tích.

Q-NEW-2: Schema map theo vùng não — 5 processing systems:
  H(Habit), K(Knowledge), R(Reactive), E(Executive), I(Identity)
  Mỗi schema = profile trên 5 systems, không phải 1 vị trí trên 1 trục.
  → Cần validate thêm.

Q-NEW-3: PFC as conductor — implications cho can thiệp:
  Nếu PFC chỉ điều phối → "nghĩ khác" (CBT) chỉ update verbal modality.
  Cần multi-modal intervention cho deep schema change.
  → Cần cross-reference với clinical evidence.

Q-NEW-4: Emotion as PE readout — cảm xúc = điểm trên 6-dimensional space?
  Nếu đúng → mọi cảm xúc đều derivable từ PE system.
  → Cần thêm ví dụ + counterexamples.

Q-NEW-5: Sync ngang vs Sync dọc — 2 loại khác nhau:
  Sync ngang: chunks within domain (đã có trong Depth ②)
  Sync dọc: coherence giữa schema layers
  → Collapse pattern phụ thuộc sync dọc, không phải Mô Hình Vuông position.

Q-NEW-6: External knowledge sync hiệu quả hơn:
  External = pre-structured (đã được tổ chức sẵn) → lower barrier to sync.
  Internal = raw, unorganized → higher barrier nhưng higher differentiation.
  → Expert lifecycle: external foundation → internal differentiation.

Q-NEW-7: Novelty — Channel gốc hay Infrastructure (PE detection system)?
  Dopamine đang gánh HAI vai trò:
    1. PE SIGNAL MECHANISM: fire cho prediction error ở MỌI channel (infrastructure)
    2. NOVELTY REWARD: "aha!" moment, cognitive newness (channel?)

  Bằng chứng cho INFRASTRUCTURE:
    - Berridge: dopamine = wanting, NOT liking → drive, không phải reward
    - Chặn dopamine → wanting MẤT cho TẤT CẢ channel, không chỉ novelty
    - Novelty-seeking có thể = threshold cao + sensitivity cao (không cần channel riêng)

  Bằng chứng cho CHANNEL:
    - "Pure cognitive novelty" khó giải thích chỉ bằng opioid
    - DRD4 variations → genuinely different novelty response
    - Chặn dopamine → novelty PE MẤT HOÀN TOÀN (pass channel test)

  Có thể: Dopamine = DUAL ROLE (infrastructure + channel)
  Giống PFC: vừa là hardware (brain region) vừa là conductor (function)

  SIMPLE TEST — Novelty detect → cảm xúc GÌ xuất hiện?
    "Aha! Hiểu rồi!"        → SƯỚNG (opioid)
    "Wow chỗ này đẹp!"       → SƯỚNG (opioid)
    "Ôi gặp người này hay!"  → ẤM (oxytocin)
    "Món này ngon lạ!"        → SƯỚNG (opioid)
    → Novelty LUÔN dẫn tới opioid hoặc oxytocin hoặc cả hai
    → Chưa bao giờ novelty dẫn tới cảm xúc KHÔNG thuộc 2 kênh này

    Ngược lại: Novelty detect nhưng KHÔNG kích channel:
    "Cái mới nhưng xấu"      → GHÉT (opioid âm)
    "Cái mới nhưng đe dọa"   → SỢ (cortisol)
    "Cái mới nhưng nhàm"     → PE ≈ 0
    → Novelty ALONE = trung tính, KHÔNG có valence riêng
    → Cần opioid/oxytocin để có DẤU (+/–)

    → Gợi ý mạnh: Novelty = DETECTION (công tắc), không phải SOURCE (nguồn điện)
    → Xác thực được bằng fMRI: novelty stimulus → opioid circuits có co-fire không?

  ⚠️ GHI CHÚ THỰC DỤNG:
  Dù Novelty là channel hay infrastructure, framework VẪN NÊN giữ Novelty
  như channel gốc vì:
    1. Tác dụng lớn nhất để predict hành vi (novelty-seeking = observable, measurable)
    2. Con người có xu hướng Novelty MẠNH HƠN theo thời đại
       (săn bắn → nông nghiệp → công nghiệp → thông tin → AI)
       Càng nhiều domain available → càng nhiều cơ hội cho novelty PE
    3. Bỏ Novelty khỏi channel → framework mất predictive power đáng kể
    4. Dù cơ chế thực sự là infrastructure, BIỂU HIỆN vẫn như channel
       → Cho mục đích predict hành vi, treat as channel = hữu ích hơn
  → Tạm giữ Novelty = channel gốc. Ghi nhận dual-role nature.
  → Revisit khi có thêm evidence tách biệt.
```

---

## 10. Thay Đổi v6 → v7

```
THAY ĐỔI CẤU TRÚC:

  v6 Tầng -1 (Bối cảnh)     → v7 Container (Môi Trường bao quanh)
  v6 Tầng 0 (Phần cứng)     → v7 T1 Hardware (giữ + thêm Processing Infra)
  v6 Tầng 1A (Nhận thức)    → v7 T2 Software (giữ + thêm Emotion readout)
  v6 Tầng 1B (Drive)        → v7 T2 Software > Drive Equation (gộp vào T2)
  v6 Tầng 2 (Hành vi)       → v7 T3 Hành Vi (giữ + thêm Feedback Loops)
  (mới)                      → v7 Domain (chiều ngang, tách riêng)

THÊM MỚI:

  §3.4 Processing Infrastructure:
    - 10 vùng não chính + chức năng
    - PFC as Conductor (không phải processor)
    - 5 ví dụ không thể phủ nhận
    - Encoding Modality (multi-modal schema)
    - Multi-region processing

  §4.4 Emotion:
    - Emotion = PE readout signal (cross-cutting)
    - 6 chiều xác định emotion
    - Mapping cảm xúc → channels × schema depth × thời gian

  §6 Domain:
    - Tách Domain khỏi Môi Trường
    - 4 loại domain
    - Domain = benchmark, không phải tầng

  §7 Luồng Xử Lý:
    - Real-time pipeline + Development pipeline
    - Tốc độ thay đổi per tầng

GIỮ NGUYÊN (reference Core.md v6):

  - 3 Kênh gốc (Novelty, Opioid, Oxytocin) — §3.1
  - 5 Phụ gia — §3.2
  - 3 Tham số + Baseline Drive — §3.3
  - Predictive-Chunk Configuration — §4.1
  - Schema (4 nền + override + lifecycle) — §4.2
  - Drive Equation — §4.3
  - Mô Hình Vuông (Source × Depth) — §5.2
  - External Chunk Pressure — §2.4
  - Emergence Phase + Can thiệp — §8
  - Calibration Notes — (tích hợp vào các section tương ứng)

CẦN REFINE THÊM (chưa ổn định):

  - Schema layers: 3? 4? 5? gradient? → §9.2 Q-NEW-1
  - Schema × Brain regions mapping → §9.2 Q-NEW-2
  - Parameters: Capacity/Threshold/Sensitivity — cần review
    có đủ/thừa/cần thêm parameter nào không
  - Emotion Map: bổ sung thêm emotions + verify mapping
```

---

> **Bước tiếp theo:**
> 1. Review draft này — xem có miss gì quan trọng từ Core v6 không
> 2. Refine schema section khi có thêm phân tích
> 3. Tạo Schema-Architecture.md cho deep-dive schema layers + brain mapping
> 4. Khi draft ổn định → merge vào Core.md chính thức, update file phụ
