# Human Predictive Drive — Framework Động Lực Con Người v7.0 DRAFT

> **Trạng thái:** DRAFT — chưa thay thế Core.md v6.0
> **Ngày:** 2026-03-15
> **Thay đổi chính so với v6.0:**
> - Kiến trúc **Container + 3 Tầng + Domain ngang:**
>   Môi Trường (Container) → T1 Hardware → T2 Software → T3 Hành Vi
> - Môi Trường = Container bao quanh con người (không phải tầng trong pipeline)
> - Hardware + Software + Hành Vi = CON NGƯỜI (internal system, liền mạch)
> - Domain = chiều ngang xuyên suốt (benchmark/luật chơi, không phải tầng)
> - Hardware bổ sung: Processing Infrastructure (brain regions + PFC as conductor)
> - Schema tách rõ khỏi chunks (schema = connections, chunks = units)
> - Emotion = cross-cutting signal (readout, không phải component mới)
>
> **Nguyên tắc:** Công thức, không đáp án. Mô hình, không dogma.
> **Quy ước:** 🟢 Nghiên cứu vững | 🟡 Suy luận có cơ sở | 🔴 Giả thuyết
>
> **⚠️ LƯU Ý QUAN TRỌNG:**
> Framework này **MỚI** — chưa có trong tài liệu học thuật chính thống.
> Mức tin cậy: "speculative unified framework, internally consistent, empirically uninvestigated."
> Framework hiện ở Level 2 trên scientific ladder (internally consistent, chưa tested).

---

## Mục Lục

**MÔI TRƯỜNG (Container)**
1. [Tổng Quan](#1-tổng-quan)
2. [Kiến Trúc Container + 3 Tầng + Domain](#2-kiến-trúc-container--3-tầng--domain)
3. [Môi Trường: Container Bao Quanh](#3-môi-trường-container-bao-quanh)

**T1: HARDWARE**
4. [Hardware: 3 Kênh Gốc](#4-hardware-3-kênh-gốc)
5. [Hardware: Phụ Gia](#5-hardware-phụ-gia)
6. [Hardware: Tham Số Nền](#6-hardware-tham-số-nền)
7. [Hardware: Processing Infrastructure](#7-hardware-processing-infrastructure)

**T2: SOFTWARE**
8. [Software: Predictive-Chunks](#8-software-predictive-chunks)
9. [Software: Schema](#9-software-schema)
10. [Software: Drive Equation](#10-software-drive-equation)

**T3: HÀNH VI**
11. [Hành Vi: Output Quan Sát Được](#11-hành-vi-output-quan-sát-được)

**DOMAIN (Chiều ngang)**
12. [Domain: Luật Chơi Xuyên Suốt](#12-domain-luật-chơi-xuyên-suốt)

**VẬN HÀNH**
13. [Feedback Loops — Container + 3 Tầng Tương Tác](#13-feedback-loops)
14. [Emotion — Cross-cutting Signal](#14-emotion)
15. [Calibration Notes](#15-calibration-notes)
16. [Giới Hạn + Câu Hỏi Mở](#16-giới-hạn--câu-hỏi-mở)
17. [Bản Đồ Files](#17-bản-đồ-files)
18. [Nguồn Tham Khảo](#18-nguồn-tham-khảo)

---

## 1. Tổng Quan

Framework mô tả **CƠ CHẾ** tạo động lực và hành vi con người — không phải phân loại tính cách.

**Nguyên lý cốt lõi:** Não = máy dự đoán. Mọi hành vi phức tạp = kết quả của hệ thống prediction.

```
Container + 3 tầng + Domain:

  MÔI TRƯỜNG (Container)  — bao quanh con người, feed vào TẤT CẢ tầng
  ┌─ CON NGƯỜI ─────────────────────────────────────────────────────┐
  │  T1: HARDWARE (sinh hóa)   — set PHẠM VI (gen, hóa chất, vùng não) │
  │  T2: SOFTWARE (nhận thức)  — set VỊ TRÍ trong phạm vi               │
  │  T3: HÀNH VI (output)      — KẾT QUẢ cuối cùng, observable          │
  └─────────────────────────────────────────────────────────────────┘
  DOMAIN (chiều ngang)         — LUẬT CHƠI xuyên suốt mọi tầng (benchmark)

Person-centric: Container(input) → T1(process) → T2(predict) → T3(output) → Container(thay đổi)

"Công thức, không đáp án:" Framework cho CÔNG THỨC để tính — ai có biến số cụ thể thì tính được.
KHÔNG PHẢI personality test. Không có 4 loại người. Phổ liên tục, per domain, thay đổi theo thời gian.
```

---

## 2. Kiến Trúc Container + 3 Tầng + Domain

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
║  │  🧬 T1: HARDWARE (Sinh hóa — Nền tảng)                    │  ║
║  │  "Não được trang bị gì"                                    │  ║
║  │  ┌─ Channels ───────────────────────────────────────────┐  │  ║
║  │  │ 💡 Novelty (DA)  ·  😌 Opioid  ·  🤝 Oxytocin       │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Additives ─────────────────────────────────────────┐  │  ║
║  │  │ Serotonin · Cortisol/GABA · NE · Vasopressin · Pro. │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Parameters ────────────────────────────────────────┐  │  ║
║  │  │ Capacity · Threshold · PE Sensitivity · Baseline    │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Processing Infrastructure ──────────────────────────┐  │  ║
║  │  │ PFC (conductor) · Amygdala · BG · DMN · Insula · ACC│  │  ║
║  │  │ → PFC = nhạc trưởng, KHÔNG phải nhạc công           │  │  ║
║  │  │ → Phần lớn computation = VÔ THỨC                     │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  Thay đổi: chậm (năm, thập kỷ). Giống ~95% mọi người.   │  ║
║  │                                                            │  ║
║  │          ↓ set phạm vi + process signals                   │  ║
║  │                                                            │  ║
║  │  🧠 T2: SOFTWARE (Nhận thức — Nội tại)                    │  ║
║  │  "Não xây dựng gì từ hardware × môi trường"               │  ║
║  │  ┌─ Predictive-Chunks ──────────────────────────────────┐  │  ║
║  │  │ Đơn vị nhỏ nhất. Multi-modal. Muôn hình vạn trạng.  │  │  ║
║  │  └──────────────┬───────────────────────────────────────┘  │  ║
║  │                 │ kết nối → ý nghĩa                        │  ║
║  │  ┌──────────────▼───────────────────────────────────────┐  │  ║
║  │  │ Schema = connections → model of reality               │  │  ║
║  │  │ NỘI TẠI, nhiều systems xử lý đồng thời               │  │  ║
║  │  │ Schema đủ mạnh CÓ THỂ override survival instinct     │  │  ║
║  │  └──────────────┬───────────────────────────────────────┘  │  ║
║  │  ┌──────────────▼───────────────────────────────────────┐  │  ║
║  │  │ Drive Equation: DRIVE = PE dự kiến − Cost             │  │  ║
║  │  │ → Input xuyên tầng: T1 + T2 + Container              │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  Thay đổi: liên tục (giờ → năm, tùy depth).              │  ║
║  │  Tạo INDIVIDUALITY.                                       │  ║
║  │                                                            │  ║
║  │          ↓ decision                                        │  ║
║  │                                                            │  ║
║  │  👁️ T3: HÀNH VI (Output — Quan sát được)                  │  ║
║  │  "Não làm gì"                                             │  ║
║  │  = f(T1 × T2 × Môi Trường)                                │  ║
║  │  Observable · Measurable · Predictable (mục tiêu FW)      │  ║
║  │  → THAY ĐỔI Môi Trường (Container)                        │  ║
║  │  → TẠO FEEDBACK cho T2 (update schema)                     │  ║
║  │  → THAY ĐỔI T1 (usage mãn tính)                           │  ║
║  │  → MỞ RỘNG Domain                                         │  ║
║  │  Thay đổi: real-time (ms → giây). Output cuối cùng.       │  ║
║  │                                                            │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  ← T3 thay đổi Môi Trường (hành vi tác động ra ngoài)          ║
║  → Môi Trường feed ngược vào T1, T2 (continuous loop)           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

  📐 DOMAIN (Chiều ngang — Luật Chơi Xuyên Suốt)
  "Thực tại tuân theo quy luật gì"

  Objective (vật lý) · Abstract (toán, logic)
  Intersubjective (xã hội) · Subjective (trải nghiệm)

  KHÔNG phải tầng — là BENCHMARK xuyên suốt:
    T1 tuân theo domain sinh học (con người không thể bay)
    T2 cố MODEL domain (schema = bản đồ, domain = lãnh thổ)
    Container TUÂN THEO domain (nước sôi 100°C dù không ai biết)
    T3 HIỆU QUẢ khi match domain (hành vi đúng = đúng quy luật)

  Thay đổi: không đổi hoặc rất chậm. BỊ MỞ RỘNG bởi T3.
```

**Tại sao Container model (không phải 4 tầng pipeline):**
```
v6:  Bối cảnh là Tầng -1 (1 bước trong pipeline)
v7a: Môi Trường là Tầng 2 (xỏ giữa Hardware và Software) → PHẢN TRỰC GIÁC
v7b: Môi Trường là Container (bao quanh toàn bộ) → ✅ CHÍNH XÁC

Lý do:
  1. Môi Trường tác động lên TẤT CẢ tầng, không chỉ 1
     → T1: stress → cortisol tăng; dinh dưỡng → brain development
     → T2: giáo dục → chunks input; văn hóa → schema installed
     → T3: context quyết định hành vi NÀO được execute
  2. Hardware + Software + Hành Vi = CON NGƯỜI (internal, liền mạch)
     Môi Trường = NGOÀI con người (external)
     → Xỏ cái ngoài vào giữa 3 cái trong = phá coherence
  3. "Con người sống TRONG môi trường" = đúng trực giác
     → Giống cá sống trong nước: nước ảnh hưởng mọi thứ nhưng không phải bộ phận của cá
```

**Master Formula (v7.0):**
```
Hành Vi (T3) = Software (T2) × Hardware (T1) × Môi Trường (Container)
               filtered by Domain (benchmark)

Luồng chính (person-centric):
  Container (input) → cung cấp stimulus, context → feed vào TẤT CẢ tầng
  T1 (process)      → detect, route, amplify/dampen signals
  T2 (predict)      → predict, evaluate, decide (phần lớn VÔ THỨC)
  T3 (output)       → execute action
  Container (changed) → môi trường thay đổi → feed lại → loop

  Domain xuyên suốt: mỗi bước tuân theo quy luật domain
    Schema đúng domain = T3 hiệu quả
    Schema sai domain = T3 thất bại → PE âm → T2 update
```

**So sánh v6.0 → v7.0:**
```
v6.0:                          v7.0:
T-1: Bối cảnh               → Container: Môi Trường (bao quanh, không phải tầng)
T0:  Phần cứng              → T1: Hardware (giữ + thêm Processing Infrastructure)
T1A: Chunks+Schema+Domain   → T2: Software: Chunks + Schema (TÁCH)
     (gộp chung)                   Domain → chiều ngang xuyên suốt
T1B: Drive                  → T2: Software: Drive Equation (giữ)
T2:  Hành vi                → T3: Hành Vi (output cuối cùng)
(không có)                   → Domain: chiều ngang (MỚI — benchmark)
```

---

## 3. Môi Trường: Container Bao Quanh

Môi Trường KHÔNG phải bước trong pipeline — là BỐI CẢNH bao quanh con người.
Giống nước với cá: nước ảnh hưởng MỌI THỨ của cá, nhưng không phải bộ phận của cá.

### 3.1 Các Thành Phần

```
VẬT CHẤT:    Nhà ở, thành phố, thiên nhiên, công cụ, thời tiết
KẾT NỐI:     Gia đình, bạn bè, đồng nghiệp, cộng đồng, MXH
VĂN HÓA:     Ngôn ngữ, giá trị, chuẩn mực, tôn giáo, thể chế
KINH TẾ:      Tài nguyên, thu nhập, cơ hội, áp lực tài chính
THỜI ĐẠI:     Công nghệ available, thông tin, thị trường lao động
```

### 3.2 Môi Trường Tác Động Lên Mỗi Tầng

```
→ T1 Hardware:
  Stress mãn tính → cortisol baseline tăng
  Dinh dưỡng → brain development (đặc biệt trẻ em)
  Chất kích thích → thay đổi threshold, sensitivity
  Ô nhiễm → hardware damage

→ T2 Software:
  Giáo dục → chunks input (external knowledge)
  Văn hóa → schema installed ("đàn ông phải...", "gia đình là...")
  Người xung quanh → shape schema sâu (trong Beck's model)
  MXH → threshold tăng (dopamine flooding)

→ T3 Hành Vi:
  Context quyết định hành vi NÀO available
  Ở nhà → nói thẳng. Ở công ty → nói vòng. Cùng software, khác output.
  Có công cụ → hành vi mới possible (internet → learn anything)

Cùng hardware + môi trường KHÁC = output hoàn toàn khác.
⚠️ Môi trường tuân theo Domain (luật chơi):
  Nước vẫn sôi 100°C dù không ai biết.
  → Môi trường = INSTANCE cụ thể của domain tại thời điểm này.
```

### 3.3 Bottleneck Analysis

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

### 3.4 External Chunk Pressure

```
= Lực kéo CÓ HỆ THỐNG của cấu trúc xã hội về phía external source.
  Không phải conspiracy — là population dynamics.

4 lực:
  1. Demand: 50-60% cần structure → thị trường phục vụ majority
  2. Selection: institution tuyển người follow quy trình
  3. Feedback: external thành công → structure reinforced
  4. Socialization: 12-16 năm giáo dục train external pattern

Anti-pressure:
  Crisis → structure sụp → cơ hội innovation
  Technology → phá monopoly → space cho internal
  Education (đúng thiết kế) → xây chunk internal từ nhỏ
```

### 3.5 Source Ratio Shift Per Thời Đại

```
Gen pool ~constant → tỉ lệ THIÊN HƯỚNG ≈ stable.
Biểu hiện thay đổi theo environment:
  Phong kiến: external ~70-80% (phá = chết)
  Công nghiệp: external ~60-70% (internal được thưởng)
  Hậu công nghiệp: external ~50-60% (internet mở space)
  AI Era: external ~40-50%? (AI phá routine → external mất PE source)
```

---

## 4. Hardware: 3 Kênh Gốc (Root Channels)

Kênh gốc = nguồn PE (Prediction Error / thưởng bất ngờ) MẠNH NHẤT tự nhiên. Gen quy định. Mỗi người = MIX, không phải 1 kênh duy nhất.

**Test:** Chặn kênh gốc → MẤT hoàn toàn 1 loại PE. Chặn phụ gia → kênh gốc vẫn CÓ nhưng biểu hiện KHÁC.

### 4.1 Novelty (Dopamine)

PE từ CHUNK MỚI — bất kỳ chunk nào chưa có trong hệ thống chunk của người đó.
"À! Nên thế à!" = Novelty PE.

🟢 Dopamine = prediction error signal (Schultz et al., 1997). Gen: DRD4, COMT, DAT1.

```
Chunk mới = bất kỳ prediction mới nào não chưa có:
  - Concept hoàn toàn mới (explore sang domain khác) = chunk mới ✅
  - Kết nối mới giữa concepts cũ (deepen trong domain) = chunk mới ✅
  - Hiểu sâu hơn cái đã biết sơ (refine chi tiết) = chunk mới ✅
  → Não KHÔNG phân biệt "mới ở đâu" — chỉ detect: predicted hay chưa?

PE ∝ chunk size: chunk mới kết nối càng NHIỀU chunk cũ → PE càng LỚN.
"Eureka moment" = 1 chunk mới giải đáp đồng loạt nhiều chunk cũ = PE cực lớn.
```

### 4.2 Opioid

PE từ CẢM NHẬN — màu sắc, âm thanh, kết cấu, mùi vị, vẻ đẹp, trải nghiệm giác quan.
"Đẹp quá!" = Opioid PE. Runner's high = endorphin sau đau.

🟢 Hệ opioid nội sinh, mu-receptor. "Liking" system (Berridge & Robinson, 1998). Gen: OPRM1.

### 4.3 Oxytocin

PE từ GẮN BÓ — kết nối, quan tâm, được hiểu, thuộc về.
Bao gồm cả gắn bó không lành mạnh (trauma bonding = oxytocin + cortisol đồng thời).

🟢 Feedback loop: kết nối → oxytocin → ấm áp → muốn kết nối thêm (Young & Wang, 2004). Gen: OXTR.

→ Chi tiết kênh + tương tác → Core-Deep-Dive/Neurochemistry.md

---

## 5. Hardware: Phụ Gia (Additives)

Phụ gia KHÔNG tạo PE trực tiếp — ĐIỀU CHỈNH cách kênh gốc vận hành.

| Phụ gia | Chức năng | Cao | Thấp |
|---------|----------|-----|------|
| Serotonin | Multiplier trên kênh gốc, lọc hierarchy | "Mình ổn" | So sánh, nhạy đánh giá |
| Cortisol/GABA | Trục an toàn ↔ hành động | Lo âu ↔ Bình tĩnh | Thiếu drive ↔ Không phanh |
| NE | Volume / cường độ | Mãnh liệt | Bình lặng |
| Vasopressin | Bảo vệ gắn bó | Bảo vệ, ghen | Dễ buông |
| Prolactin | Phanh ("đủ rồi") | Dễ dừng | Không dừng được |

```
⚠️ Serotonin ≠ channel, là MULTIPLIER:
  Serotonin = khuếch đại trên kênh gốc, không tạo PE độc lập.
  "Nghiện địa vị" = nghiện MULTI-CHANNEL PE BURST mà status mang lại.
  Strip hết kênh gốc → status alone không sustain.

⚠️ Cortisol = Inverted-U (QUAN TRỌNG):
  Quá thấp → PFC idle, không drive
  Moderate → PFC tối ưu, focused ★
  Quá cao  → PFC sụp, amygdala chiếm, freeze/trauma
  3 biến: liều, thời gian, controllability (quan trọng nhất)

  Cortisol × Dopamine = 2 hệ SONG SONG, không inverse:
    Cortisol moderate + Dopamine → flow dưới áp lực
    Cortisol cao mãn tính → ức chế DA → paralysis

⚠️ NE = Volume, không phải loại:
  Novelty + NE cao = tò mò DỮ DỘI (Van Gogh)
  Novelty + NE thấp = tò mò NHẸ NHÀNG (Darwin)
```

→ Chi tiết hóa chất + interaction → Core-Deep-Dive/Neurochemistry.md

---

## 6. Hardware: Tham Số Nền

### 6.1 Capacity — Trần Chunk Size

PFC + Working Memory = trần cho chunk phức tạp nhất có thể xây.

```
Capacity (trần)    = hardware ceiling. Gen + phát triển. Thay đổi rất chậm.
Activation (mức)   = % Capacity đang dùng. Thay đổi liên tục.
                     Modulated bởi: cortisol, ngủ, năng lượng, attention.

⚠️ "PFC yếu" = mơ hồ. Phân biệt:
  Capacity thấp    = hardware ceiling thấp (gen, brain damage)
  Activation thấp  = ceiling bình thường nhưng đang dùng ít (tạm thời)
```

### 6.2 Threshold — THAM SỐ QUAN TRỌNG NHẤT

Mức PE tối thiểu để cảm thấy "đủ" = minimum chunk size cần để thỏa mãn.

```
Threshold thấp → chunk nhỏ đủ PE → dễ hài lòng → external source thường đủ
Threshold cao  → chunk nhỏ KHÔNG ĐỦ → buộc chunk lớn / internal / deep domain

Calibrate CHẬM: MXH/dopamine flooding → threshold TĂNG. Thiền/fasting → GIẢM.
```

### 6.3 PE Sensitivity — Cách Não Xử Lý Tín Hiệu PE

```
4 sub-mechanisms:
  ① Amplitude     — volume tín hiệu DA (cùng chunk, khác người khác reaction)
  ② Precision     — PE đáng tin cỡ nào trước khi thưởng
  ③ PE Decay Rate — tốc độ chunk mất PE (EMERGENT, khác per kênh)
  ④ Generalization — habituate chunk A → chunk tương tự B có bị theo?

Sensitivity cao → phản ứng mạnh + quen nhanh → buộc explore
Sensitivity thấp → phản ứng nhẹ + quen chậm → deepen tự nhiên
```

⚠️ **Tham số nào cần refine thêm:**
- ③ PE Decay Rate: emergent metric, cần tách rõ hơn với channel anchoring
- ④ Generalization: liên quan encoding modality, cần verify
- Baseline Drive: đặt chung hay tách riêng? Hiện đặt trong §6 nhưng bản chất adaptive

→ Chi tiết 4 sub + encoding modality → Core-Deep-Dive/PE-Sensitivity.md

### 6.4 Bộ Ba Dự Đoán

```
Threshold × PE Sensitivity × Kênh gốc = DỰ ĐOÁN HẦU HẾT hành vi.
  Threshold   → chunk SIZE tối thiểu → quyết định SOURCE + DEPTH
  Sensitivity → chunk LIFESPAN + SCOPE → quyết định expression
  Kênh gốc    → chunk DOMAIN ưu tiên
```

### 6.5 Baseline Drive (Adaptive)

Não LUÔN chạy — baseline drive > 0 khi còn sống.
🟢 DMN active cả khi "không làm gì" (Raichle et al., 2001).

```
PE deficit kéo dài → baseline GIẢM → apathy
PE surplus kéo dài → baseline TĂNG → bồn chồn
"Chán" = PE hiện tại < baseline hiện tại
```

---

## 7. Hardware: Processing Infrastructure (MỚI trong v7.0)

### 7.1 Các Vùng Não Chính

```
Vùng não              │ Chức năng chính
══════════════════════╪════════════════════════════════════
PFC (Prefrontal)      │ CONDUCTOR: điều phối, chọn, ức chế, working memory
                      │ KHÔNG phải processor chính — xem §7.2
Amygdala              │ Threat/salience detection, emotional tagging
                      │ Phản ứng ~12ms (bypass PFC hoàn toàn)
Basal Ganglia         │ Habit formation, procedural learning, reward prediction
Hippocampus           │ Memory formation, context association
Cerebellum            │ Motor automation, timing, sequence precision
ACC (Anterior         │ Conflict monitoring, error detection
 Cingulate)           │ "Cái này đúng hay sai?"
Insula                │ Interoception, self-awareness, body signals
                      │ "Tôi đang cảm thấy gì?"
DMN (Default Mode     │ Self-referential thinking, rumination, narrative
 Network)             │ "Tôi là ai? Thế giới là gì?"
Temporal Cortex       │ Semantic memory, language, categories
Parietal Cortex       │ Spatial awareness, sensory integration
```

### 7.2 PFC = Conductor, Không Phải Processor

🟡 Insight quan trọng (supported by: Libet 1983, Gazzaniga split-brain, LeDoux 1996):

```
PFC KHÔNG "nghĩ ra" — PFC "điều phối và nhận kết quả":

  1. PFC set INTENTION / QUESTION (đặt câu hỏi)
  2. Vô thức COMPUTE (các vùng não khác xử lý)
  3. Kết quả XUẤT HIỆN trong ý thức (vô thức gửi lên)
  4. PFC EVALUATE (đúng/sai, dùng/bỏ)

Bằng chứng:
  - Libet (1983): brain activity trước conscious decision ~500ms
  - Nói 1 câu: từ tiếp theo XUẤT HIỆN, PFC không "chọn" từng từ
  - Eureka: đáp án đến khi PFC RELAXED (tắm, đi dạo), không khi cố nghĩ
  - "Đừng nghĩ tới con voi hồng" → hình ảnh VẪN xuất hiện bất chấp PFC

Ý thức = Giám đốc:
  → Đặt câu hỏi cho team (intention)
  → Team đi làm (unconscious compute)
  → Team mang kết quả lại (result appears in consciousness)
  → Giám đốc approve/reject (evaluate)
  → Giám đốc NGHĨ mình thông minh
  → Nhưng thực ra team làm hết
  → Team giỏi = nỗ lực điều phối của giám đốc từ nhỏ đến lớn
```

### 7.3 Encoding Modalities — Multi-Modal Processing

```
Modality           │ Vùng não chính         │ Conscious?
═══════════════════╪════════════════════════╪════════════
Verbal (ngôn ngữ)  │ Broca + Wernicke       │ Conscious nhất
Visual (hình ảnh)  │ Visual cortex          │ Semi-conscious
Auditory (âm thanh)│ Auditory cortex        │ Semi-conscious
Somatic (cơ thể)   │ Insula + Somatosensory │ Thường VÔ THỨC
Motor (vận động)   │ Motor + Cerebellum + BG│ Vô thức khi compiled
Emotional (cảm xúc)│ Amygdala + Insula      │ Phần lớn VÔ THỨC
```

```
⚠️ 1 schema có thể encoded ở NHIỀU modalities đồng thời:

  "Phải tự lực" encoded ở:
    Verbal:    "Tôi phải tự làm" (articulate được)
    Somatic:   Cổ họng thắt khi sắp nhờ ai (khó articulate)
    Emotional: Shame khi dependent (fast, trước verbal)
    Motor:     Tay rụt lại khi sắp với tới (automatic)

  → CBT sửa VERBAL → "biết nhờ ai là ok"
  → Nhưng Somatic + Emotional + Motor VẪN CÒN
  → = "Biết nhưng không làm được"
  → Schema encoded ở N modalities = cần sửa ở N modalities

  → Difficulty to change ≠ "depth"
    = SỐ MODALITIES × SỐ BRAIN REGIONS schema được encoded
    PFC chỉ trực tiếp access VERBAL — phần còn lại cần intervention riêng
```

→ Chi tiết brain regions + schema mapping → Research/Component-Interaction-Map.md §9.23

---

## 8. Software: Predictive-Chunks

### 8.1 Predictive-Chunk — Đơn Vị Nhỏ Nhất

🟢 Não mã hóa dự đoán theo chunk (Miller 1956, Cowan 2001).

```
Predictive-chunk = 1 prediction cụ thể mà não đã encode:
  "Lửa nóng" = 1 chunk
  "5 + 3 = 8" = 1 chunk (đã compiled, không cần tính)
  "Sếp cau mày = sắp bị mắng" = 1 chunk (learned pattern)

Đặc điểm:
  - ATOMIC: đơn vị nhỏ nhất, không phân chia thêm (ở level đó)
  - MULTI-MODAL: encoded across brain regions + modalities (§7.3)
  - MUÔN HÌNH VẠN TRẠNG: mỗi prediction = 1 chunk, vô số loại
  - CHUNKS NHỎ GOM THÀNH LỚN qua training (chunking process)

Source: external (copy từ bên ngoài) ←→ internal (tự xây)
```

### 8.2 Chunk Configuration Per Domain

```
2 trục chính:
  SOURCE: external ←→ internal
  DEPTH:  composite (quality + connectivity + cluster + maturity)

Per domain: Cùng 1 người có chunk config KHÁC NHAU giữa các domain.
→ KHÔNG THỂ gán 1 nhãn cho toàn bộ 1 người.

Depth sub-parameters:
  ① Chunk quality — prediction accuracy per chunk
  ② Connectivity (sync) — mức liên kết giữa chunks
  ③ Cluster formation — chunks tổ chức thành cụm
  ④ Cluster maturity — cụm ổn định bao lâu

SYNC = EMERGE từ depth đủ cao, không phải trục riêng.
```

### 8.3 Deepen vs Explore

```
DEEPEN: Chunk mới TRONG domain hiện có. PE từ kết nối sâu hơn.
EXPLORE: Chunk mới Ở domain mới. PE từ pattern chưa gặp.

Cả hai đều = tạo chunk MỚI. Khác ở ĐÂU chunk mới nằm.
Tỷ lệ deepen/explore ← PE Sensitivity ④ generalization scope.
```

---

## 9. Software: Schema

### 9.1 Schema = Connections Between Chunks → Meaning

🟢 Schema = mô hình tin vào (Piaget, 1952; Beck, 1967).

```
v7.0 definition:
  Schema = KẾT NỐI giữa các chunks tạo ra Ý NGHĨA
  Schema ≠ chunks (chunks = đơn vị, schema = connections)
  Schema ≠ domain (domain = thực tại, schema = MODEL của thực tại)
  Schema = NỘI TẠI — chỉ tồn tại trong não

Ví dụ:
  Chunk A: "bàn tay"
  Chunk B: "10"
  Schema:  "bàn tay có 10 ngón" = connection A↔B
  Domain:  bàn tay THẬT SỰ CÓ 10 ngón (thực tại bên ngoài)
  → Schema ĐÚNG = match domain. Schema SAI = không match domain.
  → Nhưng schema sai VẪN HOẠT ĐỘNG trong não (flat earth believers).
```

### 9.2 4 Schema Nền

```
1. Schema bản thân:   "tôi giỏi/kém" → prediction confidence nền
2. Schema thế giới:   "an toàn/nguy hiểm" → prediction cost nền
3. Schema người khác: "đáng tin/không" → external source nền
4. Schema tương lai:  "kiểm soát được/không" → prediction horizon nền
```

### 9.3 Schema Override Power

Schema cực mạnh CÓ THỂ override survival instinct.
🟢 Identity fusion (Swann et al., 2012): lính tự nguyện chết cho đồng đội.

```
Cơ chế: Pre-installed Counter-Signal
  Schema chuẩn bị TRƯỚC → khi PE âm hit → meaning PE dương fire song song
  → 2 signals chạy đồng thời: "đau" + "đây là con đường đúng"
  → Không suppress PE âm, cả hai đều được CẢM NHẬN
  → Yêu cầu: schema phải installed TRƯỚC khi PE âm xảy ra
```

### 9.4 Schema Architecture — Câu Hỏi Mở

⚠️ **Schema architecture đang được nghiên cứu.** Các insight hiện tại:

```
1. Schema KHÔNG xếp trên 1 trục "depth" tuyến tính
   → Schema được xử lý bởi NHIỀU brain systems đồng thời
   → "Difficulty to change" = số systems involved, không phải "depth"

2. Các Processing Systems xử lý schema (§7.1):
   - Habit system (BG): auto-patterns, compiled if-then
   - Knowledge system (Temporal): semantic, categorical
   - Reactive system (Amygdala+ACC): threat/reward, emotional
   - Executive system (PFC): planning, goal-holding, conscious
   - Identity system (DMN+Insula): self-referential, deepest

3. 1 schema có thể active ở NHIỀU systems đồng thời
   → Schema ở ít systems = dễ sửa
   → Schema ở nhiều systems = khó sửa (phải sửa ở TẤT CẢ systems)

4. Schema layers (research draft — chưa finalize):
   - Beck (1967): 3 tầng (automatic thoughts / intermediate / core beliefs)
   - Friston: continuous hierarchy (không discrete)
   - Framework v7 draft: ~3-4 clusters tự nhiên, ranh giới gradient
   → Cần nghiên cứu thêm. Xem Research/Component-Interaction-Map.md §9.
```

### 9.5 Schema Lifecycle

```
① Explore: thử nhiều domain → schema nhỏ rời rạc. PFC = navigator.
② Deepen:  đi sâu từng schema → hoàn thiện. PFC = builder.
③ Connect: kết nối schema → meta-schema. PFC = integrator.
④ Monitor: meta-schema automated → PFC = supervisor (low load).
```

→ Chi tiết schema analysis → Research/Component-Interaction-Map.md §9
→ Chi tiết schema navigation → Core-Deep-Dive/Schema-Navigation.md

---

## 10. Software: Drive Equation

### 10.1 Công Thức

```
DRIVE = Prediction Reward − Prediction Cost

  Reward = PE dự kiến × prediction confidence × kênh gốc match
         + urgency bonus (cortisol moderate → DA↑)
  Cost   = effort (PFC load) + threat (cortisol cao) + social cost + opportunity cost

Drive lấy input XUYÊN TẦNG:
  T1 (hardware state): cortisol level, dopamine level, energy
  T2 (predictions): schema predict PE dự kiến, confidence
  Container (môi trường): threat thực tế, social context, opportunity
  → Kết quả Drive = INTERNAL (không ai thấy từ bên ngoài)
  → Drive → T3 Hành Vi (execute action)
```

### 10.2 "Biết Mà Không Làm" — 2 Cơ Chế

```
Cơ chế 1 — Drive Equation âm:
  PE dự kiến nhỏ (đã biết kết quả) − Cost nguyên = DRIVE ÂM → không làm
  → Không phải "lười" — là math âm.
  → Can thiệp: tăng reward HOẶC giảm cost.

Cơ chế 2 — Multi-modal encoding mismatch (MỚI v7.0):
  Verbal encoding đã update ("tôi biết nên tập thể dục")
  Somatic + Emotional + Motor CHƯA update (vẫn "mệt, ghê")
  → PFC (verbal) nói "nên" nhưng các systems khác vẫn "không"
  → = "Biết nhưng KHÔNG THỂ" — verbal ≠ somatic
```

### 10.3 Schema Override — Competition Model

```
Override = CẠNH TRANH giữa 2 tín hiệu, không phải binary bật/tắt:
  Chunk library: {tình huống X = sợ} → amygdala → NÉ
  Schema:        {tình huống X = mục tiêu} → schema → LÀM
  → Tín hiệu MẠNH hơn thắng.

3 yếu tố quyết định:
  ① Độ mạnh schema (PFC investment, repetition, specificity)
  ② Độ mạnh chunks đối lập (amygdala tích lũy)
  ③ Tài nguyên PFC lúc đó (ngủ đủ → schema thắng; mệt → chunks thắng)
```

→ Chi tiết drive equation + modes → Core-Deep-Dive/Chunk-Patterns.md

---

## 11. Hành Vi: Output Quan Sát Được

### 11.1 Hành Vi = Giao Điểm Internal × External

```
Hành vi KHÔNG phải software:
  Software = prediction, model, internal
  Hành vi  = THỰC HIỆN prediction, external, observable

Hành vi thuộc output cuối cùng vì:
  - Người khác QUAN SÁT ĐƯỢC
  - Hành vi TẠO thay đổi trong môi trường (Container)
  - Hành vi TẠO feedback cho software (T2)
  - Cùng software + khác môi trường = khác hành vi
```

### 11.2 Mô Hình Vuông — Source × Depth Per Domain

```
                      ARCHITECT
              ┌─────────────────────┐
              │                     │
  IMPROVISER  │   Phổ liên tục     │  SOLDIER
              │   per domain        │
              │                     │
              └─────────────────────┘
                      DRIFTER

  X: Internal ←── SOURCE ──→ External
  Y: Shallow ──── DEPTH ────→ Deep

4 nhãn = 4 CẠNH (extreme positions), không phải 4 ô.
Mỗi person × domain = 1 vị trí bên trong hình vuông.
Vị trí THAY ĐỔI theo thời gian và training.
```

### 11.3 Ba Tầng Hành Vi

```
REFLEX (<200ms):         Bẩm sinh. Rụt tay, giật mình.
PREDICTION ACTIVE (PFC): Quyết định, giải quyết. Tốn năng lượng.
PREDICTION TỰ ĐỘNG:      Myelinate. Lái xe, workflow quen. Nhẹ.

~70% tự động, ~20% active, ~10% reflex (người lớn).
```

### 11.4 Emergence Phase — Nhận Diện Config Thật

```
Bỏ external pressure → chunk config thật nổi lên:
  GĐ 1 — RECOVERY (1-4 tuần): hạ cortisol, PFC phục hồi
  GĐ 2 — HABITUATION (4-12 tuần): PE ngắn cạn, "chán"
  GĐ 3 — EMERGENCE (3+ tháng): config thật lộ ra
```

### 11.5 Thứ Tự Can Thiệp — 6 Bước

```
1. TỐI ƯU CORTISOL (luôn bước 1 — cortisol cao chặn mọi thứ)
2. SỬA SCHEMA (4 schema nền)
3. XÂY prediction xa + cân bằng deepen/explore
4. BẢO VỆ prediction xa (tránh overjustification)
5. CALIBRATE threshold
6. NHẬN DIỆN chunk config thật per domain → thiết kế environment
```

### 11.6 Feedback Loops (từ T3)

```
T3 → Container (Môi Trường):
  Hành vi THAY ĐỔI môi trường: xây nhà, nói chuyện, viết sách
  → Môi trường mới → feed mới cho T1 + T2

T3 → T2 (Software):
  Kết quả hành vi → update schema: "cách này đúng/sai"
  = Learning loop. PE từ kết quả → chunk mới hoặc update chunk cũ.

T3 → T1 (Hardware) — dài hạn:
  Usage mãn tính thay đổi hardware:
    Tập gym → cortisol baseline giảm
    Stress kéo dài → cortisol baseline tăng
    Thiền → attention circuits strengthened

T3 → Domain (EXPANSION):
  Hành vi MỞ RỘNG domain
  Chế tạo máy bay → "bay" = domain mới cho loài người
  Viết framework → nếu đúng: domain tâm lý mở rộng
```

---

## 12. Domain: Luật Chơi Xuyên Suốt

### 12.1 Domain = Thực Tại Mà Chunks Phản Ánh

```
Domain KHÔNG phải tầng — là CHIỀU NGANG xuyên suốt Container + Con Người.
Domain = CÁC QUY LUẬT NGẦM mà thực tại tuân theo.
Domain KHÔNG tác động trực tiếp — tác động QUA môi trường.

Ví dụ:
  "Nước sôi ở 100°C" — rule này KHÔNG tác động gì tự thân
  → CHỈ KHI bỏ tay vào nước sôi (hành vi + môi trường)
    → rule mới MANIFEST thành hậu quả (bỏng)

→ Domain = class, Môi trường = object instance
→ Domain = luật chơi, Môi trường = bàn cờ hiện tại
```

### 12.2 Taxonomy Domain

```
4 loại (spectrum objectivity):
  Objective:       Vật lý, hóa, sinh — tồn tại khách quan
  Abstract:        Toán, logic, economics — consistent, verify được
  Intersubjective: Xã hội, chính trị, văn hóa — shared nhưng mutable
  Subjective:      Nghệ thuật, trải nghiệm — real nhưng cá nhân

⚠️ Não xử lý TẤT CẢ loại domain bằng CÙNG cơ chế
   (predictive-chunks + schema). Não không phân biệt.
```

### 12.3 Domain ↔ Container + 3 Tầng

```
Domain ↔ Container (Môi Trường):
  Môi trường TUÂN THEO domain. Nước sôi dù không ai biết.
  → Hiểu domain = predict môi trường tốt hơn

Domain ↔ T1 (Hardware):
  Giới hạn sinh học: con người KHÔNG thể bay, nghe sóng siêu âm,...
  Hardware tuân theo domain sinh học

Domain ↔ T2 (Software):
  Schema = BẢN ĐỒ. Domain = LÃNH THỔ.
  Schema đúng = match domain → hành vi hiệu quả
  Schema sai = không match → hành vi thất bại → PE âm → update
  → Schema SAI vẫn HOẠT ĐỘNG (flat earth believers) cho đến khi bị
    challenge bởi domain thực qua hành vi + kết quả

Domain ↔ T3 (Hành vi):
  Hành vi HIỆU QUẢ khi match domain
  Hành vi MỞ RỘNG domain (khám phá, phát minh, sáng tạo)
  → PhD = mở rộng domain qua internal contribution
```

---

## 13. Feedback Loops — Container + 3 Tầng Tương Tác

```
LOOP 1: Container → T2 (LEARNING)
  Môi trường → observe → chunks → schema
  "Thấy lửa nóng" → chunk "lửa = nóng" → store

LOOP 2: T2 → T3 → Container (ACTION)
  Schema predict → drive evaluate → hành vi → thay đổi môi trường
  "Predict cần nóc nhà" → xây → nóc XUẤT HIỆN trong môi trường

LOOP 3: Container → T1 (ADAPTATION — chậm)
  Môi trường mãn tính → thay đổi sinh hóa
  Stress kéo dài → cortisol baseline tăng
  MXH liên tục → threshold tăng (D2 downregulate)

LOOP 4: T1 → T2 (CONSTRAINT)
  Hardware set phạm vi cho Software
  Capacity → max chunk complexity
  Channels → loại PE nào mạnh nhất

LOOP 5: T3 → Domain (EXPANSION)
  Hành vi MỞ RỘNG domain
  Chế tạo máy bay → "bay" = domain mới cho loài người
  Viết framework → nếu đúng: domain tâm lý mở rộng

LOOP 6: T3 → T2 (FEEDBACK — qua kết quả)
  Hành vi → kết quả → PE (match prediction?) → update schema
  Hành vi thành công → PE dương → schema reinforced
  Hành vi thất bại → PE âm → schema updated/revised

LOOP 7: T3 → T1 (USAGE — rất chậm)
  Hành vi mãn tính → thay đổi hardware
  Tập gym mãn tính → cortisol baseline giảm
  Thiền mãn tính → PFC filter thay đổi
```

---

## 14. Emotion — Cross-cutting Signal

```
⚠️ Emotion KHÔNG phải thành phần mới cần thêm.
   Emotion = OBSERVABLE OUTPUT (readout) của PE × Schema × Channels.
   = Signal chạy GIỮA Container + 3 tầng, không thuộc riêng tầng nào:
     T1 generate (Amygdala, Insula, dopamine system)
     T2 interpret (schema label: "tôi đang sợ")
     Container trigger (môi trường tạo stimulus)
     T3 express (biểu hiện ra ngoài)

Emotion = Signal về trạng thái PE:
  - Kênh nào dominant (dopamine/opioid/oxytocin/cortisol)
  - PE dấu gì (+/–/mixed)
  - Thời gian (quá khứ/hiện tại/tương lai)
  - Schema depth (surface → deep)
  - Certainty + Intensity

Ví dụ:
  Lo âu  = predict PE ÂM trong tương lai (cortisol + amygdala)
  Hy vọng = predict PE DƯƠNG trong tương lai (dopamine + PFC)
  → Cùng cơ chế (future PE prediction), ngược dấu

  Shame  = "TÔI sai" (identity-level)
  Guilt  = "Tôi LÀM sai" (behavior-level)
  → Cùng cơ chế, khác depth

  Xúc động = deep schema CONFIRMED → opioid + oxytocin burst
  Bạn xúc động vì CÁI GÌ → cho biết deep schema của bạn LÀ GÌ
```

→ Chi tiết emotion map → Research/Emotion-Map.md

---

## 15. Calibration Notes

### 15.1 Threshold = Tham Số #1

```
Nếu chỉ biết 1 tham số → chọn Threshold.
Threshold quyết định: hài lòng hay không, prediction xa hay ngắn, mode nào emerge.
```

### 15.2 Cortisol Inverted-U Awareness

```
"Thiếu động lực" → cortisol ở đâu?
  Quá thấp: cần tăng challenge. Tối ưu: đừng thêm áp lực. Quá cao: hạ trước.
```

### 15.3 Multi-modal "Biết Nhưng Không Làm"

```
Verbal update ≠ full update.
Schema encoded ở nhiều modalities → cần intervention PHÙ HỢP modality.
  CBT → verbal. EMDR → visual + somatic. Exposure → motor + emotional.
```

### 15.4 Framework KHÔNG Phải

```
✗ Personality test (không có 4 loại người)
✗ Self-help (cho công thức, người dùng tự tính)
✗ Clinical tool (không thay thế chẩn đoán chuyên gia)
✗ Validated theory (internally consistent, empirically uninvestigated)
```

---

## 16. Giới Hạn + Câu Hỏi Mở

### 16.1 Câu Hỏi Kiến Trúc (MỚI v7.0)

| # | Câu hỏi | Ưu tiên |
|---|---------|---------|
| A1 | Schema architecture: bao nhiêu layers/clusters? Gradient hay discrete? | Cao |
| A2 | Schema ↔ Brain regions mapping: đã đúng hướng, cần verify chi tiết | Cao |
| A3 | "Difficulty to change" = f(number of modalities × brain regions)? Cần evidence | Cao |
| A4 | PFC as conductor: consensus trong neuroscience hay còn debate? | Cao |
| A5 | Domain taxonomy: 4 loại (objective/abstract/intersubjective/subjective) đủ? | TB |
| A6 | Container model: tốc độ thay đổi khác nhau (T1:năm, T2:giờ-năm, T3:ms) — evidence cho tách tầng? | TB |
| A7 | PE nằm ở INTERFACE giữa T2 và Container — cần formalize rõ hơn | Cao |
| A8 | Ý thức nằm ở đâu? PFC conductor (T1) đang monitor T2 (software) | TB |

### 16.2 Câu Hỏi Kế Thừa Từ v6.0

| # | Câu hỏi | Ưu tiên |
|---|---------|---------|
| 1 | Threshold range: thay đổi bao nhiêu? Bao lâu calibrate? | Cao |
| 2 | Chunk depth per domain: đo bằng gì? (proxy metrics?) | Cao |
| 3 | True vs Forced external: diagnostic protocol? | Cao |
| 4 | ③ PE Decay Rate: emergent metric — tách rõ hơn với channel anchoring | Cao |
| 5 | ④ Generalization: encoding modality → ④ confirm? | Cao |
| 6 | Prolactin hypothesis: healthy/pathological boundary ở đâu? | TB |

### 16.3 Câu Hỏi Mới Từ Research

| # | Câu hỏi | Ưu tiên |
|---|---------|---------|
| R1 | OCD = hardware (serotonin malfunction) — framework predict gì về OCD? | TB |
| R2 | Pseudo-sync vs true-sync (tín ngưỡng): có thể measure? | TB |
| R3 | Emotion spectrum: 6 chiều (channel/sign/time/depth/certainty/intensity) đủ? | TB |
| R4 | Tình yêu 3 giai đoạn: transition timing predictable? | Thấp |
| R5 | Novelty: channel gốc hay infrastructure (PE detection)? Simple test + fMRI verify | Cao |

---

## 17. Bản Đồ Files

```
Human Predictive Drive/
│
├── Core.md                         ← v6.0 (CURRENT — production)
├── Research/Core-v7-Draft.md       ← v7.0 DRAFT (kiến trúc Container)
├── Research/Core-v7-Draft-Good.md  ← ★ FILE NÀY (v7.0 DRAFT refined)
│
├── Core-Deep-Dive/                 ← Đào sâu per component
│   ├── Neurochemistry.md           ← Hardware: hóa chất chi tiết
│   ├── PE-Sensitivity.md           ← Hardware: PE Sensitivity 4 sub
│   ├── Chunk-Patterns.md           ← Software/Hành vi: 4 pattern deep-dive
│   ├── Schema-Navigation.md        ← Software: schema 6 levels, risks
│   ├── Society-Dynamics.md         ← Container: External Pressure × xã hội
│   ├── Compliance.md               ← Cross-layer: compliance v5.5
│   └── [MỚI] Schema-Architecture.md ← Software: schema layers, systems, encoding
│
├── Research/                       ← Nghiên cứu per topic
│   ├── Component-Interaction-Map.md ← ★ Interaction analysis + schema decomposition
│   ├── Emotion-Map.md              ← ★ Emotion mapping (PE × channels × brain)
│   ├── Layer-Architecture-Draft.md  ← Architecture analysis (v4)
│   ├── Religion.md                 ← Tôn giáo: 7 functions
│   ├── Mismatch-Patterns.md        ← OCD, burnout, open loops
│   ├── Depression-Predictive-Model.md ← Trầm cảm model
│   └── ...                         ← (other research files)
│
├── Applications/                   ← Ứng dụng thực tế
│   ├── Relationships.md
│   ├── HR-Management.md
│   ├── Education.md
│   └── ...
│
└── Validation/                     ← Kiểm chứng
    ├── Examples.md
    ├── Characters.md
    └── ...
```

---

## 18. Nguồn Tham Khảo

### Kênh gốc + Reward
- Schultz et al. (1997) — Dopamine = prediction error signal 🟢
- Berridge & Robinson (1998, 2016) — Wanting vs liking 🟢
- Young & Wang (2004) — Oxytocin + pair bonding 🟢
- De Dreu et al. (2010) — Oxytocin + in-group bias 🟢

### Phụ gia + Hardware
- Raleigh et al. (1991) — Serotonin + hierarchy 🟢
- Arnsten (2009) — Cortisol ức chế PFC 🟢
- Sapolsky (2004) — Stress + cortisol chronic 🟢
- Ebstein et al. (1996) — DRD4 7-repeat + novelty-seeking 🟢
- de Kloet et al. (1998) — Cortisol inverted-U 🟢

### Brain regions + Processing
- Libet (1983) — Readiness potential trước conscious decision 🟢
- Gazzaniga — Split-brain: PFC as narrator 🟢
- LeDoux (1996) — Amygdala low road, bypass PFC 🟢
- Kahneman (2011) — System 1 (fast) vs System 2 (slow) 🟢
- Raichle et al. (2001) — Default Mode Network 🟢

### Prediction + Schema + Chunks
- Friston (2010) — Free Energy Principle 🟢
- Rao & Ballard (1999) — Predictive coding 🟢
- Miller (1956), Cowan (2001) — Chunking + WM capacity 🟢
- Piaget (1952), Beck (1967) — Schema theory 🟢
- Hebb (1949) — Neural pathways 🟢
- Feldman & Friston (2010) — Precision weighting 🟢

### Schema layers + Therapy correspondence
- Beck (1967) — 3 cognitive levels (auto thoughts / intermediate / core) 🟢
- Young (1990s) — Schema Therapy for deep patterns 🟢
- Damasio (1994) — Somatic markers 🟢
- Marazziti et al. (1999) — Infatuation serotonin ≈ OCD levels 🟢

### Tổng hợp framework (confidence)
- Container model (Môi Trường bao quanh, không phải tầng pipeline) 🔴
- 3 tầng internal (Hardware → Software → Hành Vi) 🔴
- Domain = chiều ngang xuyên suốt (benchmark, không phải tầng) 🔴
- Schema = connections between chunks (tách khỏi chunks và domain) 🔴
- Domain nằm ngoài cả Container lẫn Con Người 🔴
- PFC as conductor (supported by evidence, framing = framework) 🟡
- Multi-modal encoding → difficulty to change 🟡
- Emotion = PE readout, cross-cutting signal 🟡
- 5 Processing Systems (H, K, R, E, I) 🔴

---

> *Human Predictive Drive — Framework Động Lực Con Người v7.0 DRAFT*
> *"Công thức, không đáp án. Mô hình, không dogma."*
> *Điểm xuất phát, không phải kết luận cuối cùng.*
