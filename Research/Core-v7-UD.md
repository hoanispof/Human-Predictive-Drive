# Human Predictive Drive — Framework v7.0 UD-Centric DRAFT

> **Trạng thái:** DRAFT — phiên bản UD-centric, song song với Core-v7-Draft-Good.md (PE-centric)
> **Ngày:** 2026-03-15
> **Khác biệt với PE-centric:**
> - Nguyên lý cốt lõi: "Não = máy mong muốn" thay vì "Não = máy dự đoán"
> - PE (Prediction Error) → UD (Unconscious Desire fulfillment signal)
> - Prediction VẪN CÓ nhưng PHỤC VỤ desire, không phải mục đích tự thân
> - Dopamine = desire fulfillment signal, không phải surprise signal
>
> **⚠️ UD là GIẢ THIẾT — chưa validated.**
> File này tồn tại SONG SONG với PE-centric để so sánh.
> Chi tiết giả thiết UD: Research/UD-Hypothesis.md
>
> **Nguyên tắc:** Công thức, không đáp án. Mô hình, không dogma.
> **Quy ước:** 🟢 Nghiên cứu vững | 🟡 Suy luận có cơ sở | 🔴 Giả thuyết

---

## 1. Tổng Quan

Framework mô tả **CƠ CHẾ** tạo động lực và hành vi con người.

**Nguyên lý cốt lõi (UD-centric):**

```
CŨ (PE): Não = máy dự đoán. Predict → Error → Update.
MỚI (UD): Não = máy mong muốn. Desire → Seek → Fulfill → Update.

Vô thức cố ĐỒNG BỘ chính nó
  → Phát sinh DESIRE (mong muốn kết quả cụ thể)
  → PFC phục vụ: giả lập HOẶC hành động thực tế
  → Kết quả feedback → vô thức evaluate: "match desire?"
    → YES → Experience/Connection fire → sướng → desire fulfilled
    → NO  → UD âm → thử cách khác → loop
    → PARTIAL → Dopamine signal "gần đúng, tiếp tục"

Prediction VẪN CÓ — nhưng prediction PHỤC VỤ desire:
  → Predict chính xác = tìm fulfillment HIỆU QUẢ hơn
  → Predict sai = KHÔNG fulfill = UD âm = update prediction
  → Learning = cải thiện prediction để SERVE desire tốt hơn
```

```
Container + 3 tầng + Domain:

  MÔI TRƯỜNG (Container)  — bao quanh, cung cấp stimuli + context cho UD
  ┌─ CON NGƯỜI ─────────────────────────────────────────────────────┐
  │  T1: HARDWARE   — Não predict + Cơ thể trả thưởng (ground truth) │
  │  T2: SOFTWARE   — SCHEMA tạo desire states, PFC serve desire     │
  │  T3: HÀNH VI    — execute strategy để FULFILL desire             │
  └─────────────────────────────────────────────────────────────────┘
  DOMAIN (chiều ngang)  — desire match domain = effective, mismatch = fail

"Công thức, không đáp án:" Framework cho CÔNG THỨC — ai có biến số cụ thể thì tính.
KHÔNG PHẢI personality test. Phổ liên tục, per domain, thay đổi theo thời gian.

UD = THAM SỐ GỐC DUY NHẤT:
  Mọi thứ trong framework PHỤC VỤ UD:
    Experience/Connection (opioid/oxytocin) = PHƯƠNG TIỆN fulfill desire
    Dopamine = SIGNAL "desire approaching/matched" (infrastructure)
    Serotonin = AMPLIFIER (mạnh hơn khi status tốt)
    PFC = CÔNG CỤ giả lập + hành động (servant of UD)
    Schema = CẤU TRÚC vô thức tạo ra desire
    Hành vi = OUTPUT để fulfill desire trong thực tại
  Tất cả serve 1 thứ: VÔ THỨC CỐ ĐỒNG BỘ CHÍNH NÓ
```

---

## 2. Kiến Trúc Container + 3 Tầng + Domain

> Cùng kiến trúc với PE-centric. Khác ở LUỒNG VẬN HÀNH bên trong.

```
╔══════════════════════════════════════════════════════════════════╗
║  MÔI TRƯỜNG (Container — bao quanh con người)                   ║
║  Vật chất · Kết nối · Văn hóa · Kinh tế · Thời đại             ║
║  → Cung cấp stimuli + context cho UD evaluation                 ║
║  ← Bị THAY ĐỔI bởi T3 (hành vi fulfill desire)                 ║
║                                                                  ║
║  ┌────────────────────────────────────────────────────────────┐  ║
║  │  CON NGƯỜI (Internal system)                               │  ║
║  │                                                            │  ║
║  │  🧬 T1: HARDWARE (Não + Cơ thể — Nền tảng)                │  ║
║  │  "Não predict + cơ thể trả thưởng — desire hình thành ở cả 2"│  ║
║  │  ┌─ Lớp 1: SOURCE (nơi desire sống) ──────────────────┐   │  ║
║  │  │ 😌 Experience (opioid) · 🤝 Connection (oxytocin)        │  ║
║  │  │ = 2 nguồn DESIRE duy nhất                           │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Lớp 2: AMPLIFIER (signal + khuếch đại) ───────────┐  │  ║
║  │  │ 💡 Novelty (dopamine) · Status (serotonin)            │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Lớp 3: MODULATOR (fine-tuning) ───────────────────┐   │  ║
║  │  │ Cortisol · NE · Vasopressin · Prolactin · Endo-CB   │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Parameters ────────────────────────────────────────┐   │  ║
║  │  │ WM Capacity · Threshold · UD Sensitivity             │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Processing Infrastructure ──────────────────────────┐  │  ║
║  │  │ PFC (arbitrator) · Amygdala · BG · DMN · Insula · ACC │  │  ║
║  │  │ PFC = trọng tài phân xử giữa schemas, không tự compute│  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │                                                            │  ║
║  │          ↓ desire states formed                            │  ║
║  │                                                            │  ║
║  │  🧠 T2: SOFTWARE (Nhận thức — Nội tại)                    │  ║
║  │  "Não xây dựng gì — SCHEMA tạo desire, PFC serve desire"  │  ║
║  │  ┌─ Predictive-Chunks ──────────────────────────────────┐  │  ║
║  │  │ Đơn vị prediction. Multi-modal. PHỤC VỤ desire.      │  │  ║
║  │  └──────────────┬───────────────────────────────────────┘  │  ║
║  │                 │ kết nối → ý nghĩa → desire states       │  ║
║  │  ┌──────────────▼───────────────────────────────────────┐  │  ║
║  │  │ Schema = connections → model → DESIRE STATES          │  │  ║
║  │  │ Schema không đồng bộ → desire XUẤT HIỆN               │  │  ║
║  │  │ Schema đồng bộ → desire FULFILLED → bình an           │  │  ║
║  │  └──────────────┬───────────────────────────────────────┘  │  ║
║  │  ┌──────────────▼───────────────────────────────────────┐  │  ║
║  │  │ Drive: DRIVE = UD fulfillment expected − Cost         │  │  ║
║  │  │ PFC giả lập → vô thức evaluate → match? → execute    │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │  ┌─ Emotion ───────────────────────────────────────────┐   │  ║
║  │  │ READOUT of UD state (cross-cutting signal)           │  │  ║
║  │  │ Vui=Pres(+) · Buồn=Pres(−)+Des(+,blocked) · Lo=Des(−) │  │  ║
║  │  └──────────────────────────────────────────────────────┘  │  ║
║  │                                                            │  ║
║  │          ↓ decision (serve desire)                         │  ║
║  │                                                            │  ║
║  │  👁️ T3: HÀNH VI (Output — Quan sát được)                  │  ║
║  │  "Não làm gì — EXECUTE strategy để fulfill desire"        │  ║
║  │  = f(T1 × T2 × Môi Trường)                                │  ║
║  │  3 con đường fulfill:                                      │  ║
║  │    A. Imagination (giả lập — nhanh, UD fulfillment nhẹ)    │  ║
║  │    B. Reality (hành động thật — mạnh, tốn effort)          │  ║
║  │    C. External Validation (được xác nhận — mạnh nhất)      │  ║
║  │  → Kết quả → feedback → UD update                         │  ║
║  │                                                            │  ║
║  └────────────────────────────────────────────────────────────┘  ║
║                                                                  ║
║  DOMAIN: desire match domain = effective. Mismatch = fail → learn║
╚══════════════════════════════════════════════════════════════════╝
```

**Master Formula (UD-centric):**
```
Hành Vi (T3) = Strategy to FULFILL Desire (T2)
               using Hardware (T1)
               within Environment (Container)
               constrained by Domain (benchmark)

Luồng:
  Vô thức (T1+T2) → desire hình thành (schema không đồng bộ)
  → PFC (T1-não) predict: "hành vi nào tốt cho CƠ THỂ?"
    → PFC mạnh: predict dài hạn (sustainable body reward)
    → PFC yếu: default schema mạnh nhất (short-term body reward)
  → Giả lập trước (optional): body respond NHẸ → preview → decide
  → Execute (T3) trong Container
  → CƠ THỂ (T1-body) nhận kết quả THỰC TẾ → opioid/oxytocin respond
  → Body signal LÊN não: "tốt/không tốt" (ground truth)
  → Schema update based on BODY response → loop
  → Domain = benchmark: match domain = body reward effective
```

### 1.1 UD Vocabulary — Thay thế "PE" bằng thuật ngữ chính xác

```
THAY VÌ 1 từ "PE" gánh 7 nghĩa, UD dùng NHIỀU từ:

  UD Signal:      Dopamine fire (desire approaching/matched)
  UD per schema:  desire state CỦA 1 schema cụ thể
  UD State:       {Present, Desire, Coherence} aggregate tổng thể
    Present:      hiện tại đang trải nghiệm gì (+/0/−) ↔ Experience/Connection
    Desire:       tương lai mong muốn gì (+/0/−/blocked) ↔ Novelty seeking
    Coherence:    schemas đồng hướng hay conflict (high/low)
  UD Arbitration: PFC phân xử giữa schemas → chọn schema → Drive
                  PFC mạnh: predict xa, fair. PFC yếu: loudest wins.
  UD Drive:       KẾT QUẢ arbitration → motivation cho hành vi cụ thể
  UD Readout:     Emotion = đọc UD State ra conscious

"Chán" decompose thành 3 loại:
  Type A — Content:   desire fulfilled đủ → BÌNH AN (không cần can thiệp)
  Type B — Restless:  desire CÓ nhưng targetless → cần explore
  Type C — Suppressed: desire CÓ nhưng Lớp 2 broken → cần fix Lớp 2

"Đồng bộ chunk xấu":
  PE: predicted correct → PE = 0 → nên bình thường? ❌
  UD: desire VIOLATED → Present(−) → buồn/đau ✅
      Nếu desire VẪN active + blocked → buồn (muốn nhưng không được)
      Nếu desire dead → đau (chịu vậy)

→ Chi tiết: UD-Hypothesis.md §4.7 + §4.9
```

---

## 3. Môi Trường: Container

> Giữ nguyên từ PE-centric — Container model không phụ thuộc PE hay UD.

```
VẬT CHẤT · KẾT NỐI · VĂN HÓA · KINH TẾ · THỜI ĐẠI

Tác động lên mỗi tầng:
  → T1: stress → cortisol → desire priority shift
  → T2: giáo dục → chunks → schema → desire states
  → T3: context → hành vi NÀO available để fulfill

UD-specific insight:
  Môi trường = NGUỒN NGUYÊN LIỆU cho desire fulfillment
  Môi trường giàu → nhiều con đường fulfill → UD dễ đáp ứng
  Môi trường nghèo → ít con đường → UD khó đáp ứng → cortisol
  → "Thiết kế môi trường" = tạo nhiều con đường fulfill nhất có thể
```

---

## 4. T1: Hardware — Não + Cơ Thể (Nơi Desire Hình Thành + Trả Thưởng)

### 4.1 Neurochemistry 3 Lớp

```
╔══════════════════════════════════════════════════════╗
║  LỚP 1: SOURCE — "Con người muốn gì?"               ║
║                                                      ║
║  EXPERIENCE (opioid)       CONNECTION (oxytocin)     ║
║  Desire về CẢM NHẬN        Desire về GẮN BÓ          ║
║  taste, beauty, warmth,    connection, belonging,     ║
║  coherence, pleasure       understanding, being seen  ║
║                                                      ║
║  = 2 nguồn DESIRE duy nhất                           ║
║  = CẢM NHẬN CƠ THỂ — nơi THỰC SỰ trả thưởng        ║
║    (opioid/oxytocin receptors: não + ruột + da + cơ)  ║
║  = Body = người ĐÁNH GIÁ cuối cùng (ground truth)    ║
║  = PFC chỉ PREDICT, body mới CONFIRM reward          ║
║  = Giả lập (imagination) → body respond NHẸ (preview)║
║    Thực tế (reality) → body respond MẠNH (confirm)   ║
║  = Mọi hành vi cuối cùng serve 1 trong 2 (hoặc cả 2)║
╠══════════════════════════════════════════════════════╣
║  LỚP 2: AMPLIFIER — "Signal + khuếch đại"           ║
║                                                      ║
║  NOVELTY (dopamine)        STATUS (serotonin)        ║
║  "Desire matched!"         "Tôi ở vị trí tốt!"      ║
║  Detect + signal           Multiply + stabilize      ║
║  Mở rộng tìm kiếm         Củng cố confidence        ║
║                                                      ║
║  Dopamine = UD SIGNAL:                                ║
║    Fire khi desire approaching/matched                ║
║    Suppress khi desire NOT matched                    ║
║    ≠ "surprise signal" (RPE)                          ║
║    = "desire fulfillment signal" (UD)                 ║
║                                                      ║
║  ⚠️ Novelty:                                         ║
║    Framework TREAT as channel (predictive power)      ║
║    Bản chất: có thể là infrastructure                 ║
║    Test: Novelty → cảm xúc GÌ? → luôn opioid/oxy    ║
║    → Xem UD-Hypothesis.md §Q-NEW-7                   ║
╠══════════════════════════════════════════════════════╣
║  LỚP 3: MODULATOR — "Fine-tuning"                   ║
║                                                      ║
║  Cortisol: desire "an toàn" PRIORITY shift           ║
║  NE: arousal → detect match NHANH hơn                ║
║  Vasopressin: desire "bảo vệ gắn bó"                ║
║  Prolactin: "đủ rồi" signal                          ║
║  Endocannabinoid: relaxation modulation              ║
║                                                      ║
║  → Tác động QUA Lớp 1+2, không tạo desire riêng     ║
╚══════════════════════════════════════════════════════╝
```

### 4.2 Parameters

```
WM CAPACITY — Working Memory slots (HARDWARE, FIXED)
  = Bao nhiêu chunks giữ CÙNG LÚC trong đầu (~4±1 items)
  = Gen quy định ~70%, training ảnh hưởng ít
  = ĐO ĐƯỢC: digit span test, N-back test
  → WM cao → giữ nhiều chunks → schema phức tạp hơn POSSIBLE
  → WM thấp → chunking quan trọng hơn (nén thông tin để fit)
  → WM cao ≠ schema phức tạp (cần thêm software + time)

  ⚠️ Schema Ceiling = emergent metric, KHÔNG phải parameter:
    Schema_ceiling = f(WM × knowledge × time × domain)
    = KẾT QUẢ, không phải INPUT — giống Baseline Drive
    = Thay đổi inputs → ceiling tự thay đổi

THRESHOLD — Mức UD fulfillment tối thiểu để "đủ" (COMPOSITE)
  Threshold_observed = Threshold_hardware + Schema_pressure − Schema_suppression

  Threshold_hardware:  D2 receptors, genetic (T1, cố định ~)
  Schema_pressure:     Schema âm đẩy threshold LÊN (T2, SỬA ĐƯỢC)
                       "Phải hơn người khác", "dừng = thất bại",...
  Schema_suppression:  Resign kéo threshold XUỐNG — FAKE contentment (T2, cần phát hiện)
                       "Mặc kệ, cố gì cũng vô ích"

  → Fix schema pressure → threshold TỰ GIẢM → dễ thỏa mãn → hạnh phúc hơn
  → Accept hardware floor → match environment phù hợp
  → Phát hiện suppression → unlock hidden desire → fix đúng hướng

  ⚠️ Cùng "threshold cao" nhưng KHÁC nguyên nhân → KHÁC treatment:
    Hardware cao → match environment (nghệ sĩ cần art, không cần therapy)
    Schema pressure → fix schema (CEO cần therapy, không cần art)
    Suppression → unlock trước, fix sau

  → Chi tiết: Research/Threshold-Analysis.md

UD SENSITIVITY — Cách não respond UD signal (≈ PE Sensitivity)
  4 sub-mechanisms:
    ① Amplitude:      volume UD signal (cùng desire, khác reaction)
    ② Precision:      UD signal đáng tin cỡ nào trước khi act
    ③ UD Decay Rate:  tốc độ desire "hết hứng" sau fulfillment
                      = pre-simulation tăng → remaining desire GIẢM
    ④ Generalization: fulfill desire A → desire tương tự B có giảm?

  ⚠️ ③ UD Decay Rate giải thích TRỰC TIẾP hơn PE Decay Rate:
    PE: "chunk mất PE vì đã predict" (tại sao predict = boring?)
    UD: "desire mất vì đã pre-simulated đủ" (clear: simulate = partially fulfill)
    → UD cho mechanism RÕ RÀNG hơn cho habituation

BASELINE DRIVE — Observable metric (EMERGENT, không phải parameter input)
  = f(Threshold × Schema × Environment) — KẾT QUẢ, không phải INPUT
  UD deficit kéo dài → baseline GIẢM → apathy
  UD surplus → baseline TĂNG → bồn chồn
  "Chán" = desire hiện tại < threshold (không có gì đáng fulfill)
  → Đo được (quan sát hành vi) nhưng KHÔNG SET trực tiếp
  → Thay đổi inputs (fix schema, match environment) → baseline TỰ THAY ĐỔI
```

### 4.3 Processing Infrastructure

```
PFC = TRỌNG TÀI phục vụ BODY (không phải decision-maker)
  → PFC KHÔNG tạo desire, KHÔNG trả thưởng, KHÔNG tự tính toán
  → PFC chỉ PHÂN XỬ: "schema nào → body reward tốt nhất?"
  → Body (opioid/oxytocin) = người ĐÁNH GIÁ cuối cùng (ground truth)
  → Chi tiết PFC sub-regions + profiles + training: Research/PFC-Analysis.md

  1. Body + vô thức: "có gì đó cần fulfill" (desire signal)
  2. PFC: predict strategy (hành vi nào → body reward?)
     → PFC mạnh: predict dài hạn (sustainable reward)
     → PFC yếu: default schema mạnh nhất (short-term reward)
  3. PFC: giả lập trước → body respond NHẸ (preview)
  4. PFC: execute hành vi thật
  5. Body: nhận kết quả → opioid/oxytocin respond (ground truth)
  6. Body signal lên não → schema update → PFC learn

  = GPS phục vụ XE:
    GPS (PFC) predict đường tốt nhất
    Xe (body) ĐI đường đó → CẢM NHẬN đường
    Đường tốt → xe êm (opioid) → GPS: "đường này tốt, nhớ"
    Đường xấu → xe xóc (cortisol) → GPS: "tránh đường này"
    GPS NGHĨ mình chọn đường — thực ra xe quyết định đường nào "tốt"

  PFC Activation Level — DYNAMIC STATE (không phải parameter):
    = PFC đang AVAILABLE bao nhiêu % TẠI THỜI ĐIỂM NÀY

    Ảnh hưởng bởi:
      Sleep:    đủ giấc → PFC 90%. Thiếu ngủ → PFC 40%
      Cortisol: stress → PFC GIẢM (resource bị chiếm bởi Amygdala)
      Glucose:  đói → PFC GIẢM. Ăn đủ → PFC available
      Alcohol:  say → PFC ~10% → mất inhibition + mất planning
      Fatigue:  mệt cuối ngày → PFC GIẢM dần
      Flow:     focus sâu → PFC TĂNG cho 1 task, GIẢM cho phần còn lại

    Ảnh hưởng tới UD:
      PFC cao → DELIBERATE choice → schema SÂU hơn có thể win
      PFC thấp → AUTOMATIC response → schema MẠNH NHẤT win (bất kể depth)
      → Giải thích: tại sao mệt → quyết định kém, ăn junk food, cãi nhau
      → Giải thích: Case 1 sáng thứ 2 — cùng người, khác PFC = khác hành vi

Amygdala: desire "an toàn" detector
  → OVERRIDE mọi UD khác khi survival threatened
  → ~12ms, bypass PFC → reflex zone (ngoài scope UD)
  → KHÔNG BAO GIỜ ngủ hoàn toàn → luôn active

BG (Basal Ganglia): habit executor
  → Compiled schemas → chạy KHÔNG cần PFC
  → PFC thấp → BG take over → habit-driven behavior
  → Tại sao mệt → quay về old habits

DMN (Default Mode Network): identity + self-reference
  → Schema "tôi là ai" → desire identity
  → Active khi PFC REST → rumination, self-reflection
  → Quá active → overthinking, anxiety

Insula: body state awareness
  → "Tôi đang cảm thấy gì?" → somatic UD signal
  → Đói, mệt, đau, arousal → feed vào UD evaluation

ACC (Anterior Cingulate Cortex): conflict monitor
  → "2 schemas đang conflict!" → signal cho PFC
  → ACC fire → cảm giác "lấn cấn", "không ổn"
  → = Coherence detector trong UD State

Hierarchy ưu tiên:
  SURVIVAL (Amygdala) > DESIRE (UD) > HABIT (BG) > CONSCIOUS (PFC)

Modality Channels — hardware infrastructure cho encoding:
  Verbal · Visual · Auditory · Somatic · Motor · Emotional
  → Mỗi vùng não xử lý 1 modality RIÊNG
  → 1 schema/desire có thể encoded ở NHIỀU modalities đồng thời

  Implications cho UD:
    → Desire fulfilled ở 1 modality ≠ fulfilled ở tất cả
    → "Biết nhưng không làm được" = verbal fulfilled, somatic chưa
    → Fix desire = fix ở ĐÚNG modality, không chỉ nói/nghĩ
    → CBT fix verbal. Exposure fix somatic + emotional. Practice fix motor.
    → Deep desire = encoded ở NHIỀU modalities → khó fix → cần NHIỀU approaches

→ Chi tiết PFC sub-regions + profiles + training: Research/PFC-Analysis.md
```

---

## 5. T2: Software — Schema Tạo Desire, PFC Serve Desire

### 5.1 Predictive-Chunks — Phục Vụ Desire

```
Chunks = đơn vị prediction. Multi-modal. Muôn hình vạn trạng.

UD reframe:
  Chunks KHÔNG tồn tại "vì prediction" — tồn tại vì SERVE DESIRE
  → Não build chunks ĐỂ fulfill desire hiệu quả hơn
  → Chunks chính xác = tìm fulfillment nhanh hơn
  → Chunks sai = tìm sai → UD âm → update chunks

Source: external (copy) ←→ internal (tự xây)
Depth: composite (quality × connectivity × cluster × maturity)
Per domain: cùng 1 người, khác config per domain
```

### 5.2 Schema = Connections → Desire States

```
Schema = kết nối chunks → ý nghĩa → DESIRE STATES

UD-centric definition:
  Schema KHÔNG CHỈ "model of reality"
  Schema = model of reality + DESIRE ABOUT reality

  Schema không đồng bộ → desire XUẤT HIỆN:
    "Tại sao cái này mâu thuẫn?" → UD coherence âm → phải giải quyết
    "Tôi muốn hiểu cái này" → UD mastery → seek fulfillment
    "Tôi muốn gần người này" → UD connection → seek proximity

  Schema đồng bộ → desire FULFILLED:
    "À, hiểu rồi!" → UD coherence fulfilled → opioid → sướng
    "Tôi làm được!" → UD mastery fulfilled → opioid → tự hào
    "Họ hiểu tôi!" → UD connection fulfilled → oxytocin → ấm

4 Schema Nền (UD reframe):
  1. Schema bản thân: "tôi có giá trị" → UD "being seen" baseline
  2. Schema thế giới: "an toàn" → UD "safety" baseline
  3. Schema người khác: "tin được" → UD "connection" baseline
  4. Schema tương lai: "kiểm soát được" → UD "agency" baseline
  → 4 schema = 4 UD BASELINES — set mức desire MẶC ĐỊNH

Schema Override Power:
  Schema cực mạnh CÓ THỂ override survival instinct
  UD explanation: desire meaning > desire survival
  → L5 meaning desire FULFILLED khi hy sinh → opioid
  → L1 survival desire VIOLATED → cortisol
  → Net: meaning > survival → hành vi (tử vì đạo, liệt sĩ)
  → Pre-installed TRƯỚC → ready khi UD âm xảy ra
```

### 5.3 Drive Equation — UD Version

```
DRIVE = PFC predict BODY REWARD − Cost

  PFC predict: "hành vi này → body (opioid/oxytocin) respond bao nhiêu?"

  UD_expected = Σ(desire_i × predicted_body_reward_i) − Σ(pre_simulated_i)

  desire_i:            body desire thứ i (opioid: cảm nhận / oxytocin: gắn bó)
  predicted_body_reward: PFC predict body sẽ reward bao nhiêu? (0→1)
  pre_simulated:        đã giả lập → body đã preview respond → giảm remaining

  Cost = effort (PFC load) + threat (cortisol) + social + opportunity

  PFC predict HORIZON quyết định hành vi:
    PFC yếu:      predict 5 phút  → chọn body reward NGAY (ăn junk, scroll MXH)
    PFC vừa:      predict 1 ngày  → balance ngắn/dài hạn
    PFC mạnh:     predict tháng/năm → chọn SUSTAINABLE body reward
    PFC cực mạnh: predict cả đời  → "legacy", "meaning" (L5 desire)

So sánh:
  PE-centric:  DRIVE = Surprise expected − Cost
  UD-centric:  DRIVE = Fulfillment expected − Cost

  Khác biệt ở edge cases:
    "Về quê" — PE: no surprise → drive low. UD: desire home fulfilled → drive HIGH ✅
    "Nghe nhạc lần 50" — PE: predicted → boring. UD: desire beauty renew → still enjoy ✅
    "Người thân tặng quà" — PE: expected → low. UD: desire connection fulfilled → HIGH ✅
```

### 5.4 "Biết Mà Không Làm" — UD Version

```
Cơ chế 1 — Drive Equation âm:
  UD fulfillment expected THẤP (đã pre-simulated quá nhiều)
  − Cost nguyên vẹn = DRIVE ÂM → không làm
  → Can thiệp: tạo desire MỚI hoặc giảm cost

Cơ chế 2 — Multi-modal UD mismatch:
  Verbal desire fulfilled ("tôi biết nên tập")
  Somatic desire CHƯA ("cơ thể không muốn")
  → PFC (verbal) nói "nên" nhưng body nói "không"
  → = "Biết nhưng KHÔNG THỂ"
  → Can thiệp: fulfill ở somatic level (exposure, practice), không chỉ verbal
```

### 5.5 Emotion = UD Readout

```
Emotion = SIGNAL về trạng thái UD (không phải PE):

                    UD ÂM                    UD DƯƠNG
                    (desire unfulfilled)      (desire fulfilled)
                ┌────────────────────┬────────────────────┐
  TƯƠNG LAI     │ LO ÂU              │ HY VỌNG            │
  (predicted)   │ UD âm sắp tới      │ UD+ sắp tới        │
                ├────────────────────┼────────────────────┤
  HIỆN TẠI      │ SỢ, TỨC, BUỒN,    │ VUI, TỰ HÀO,      │
  (happening)   │ XẤU HỔ, GHEN       │ XÚC ĐỘNG, BIẾT ƠN  │
                ├────────────────────┼────────────────────┤
  QUÁ KHỨ       │ HỐI HẬN, TỘI LỖI  │ HOÀI NIỆM          │
  (remembered)  │ UD âm đã xảy ra    │ UD+ đã mất          │
                ├────────────────────┼────────────────────┤
  TOÀN BỘ       │ TUYỆT VỌNG         │ BÌNH AN / HẠNH PHÚC│
  (all futures) │ mọi UD = âm/zero   │ UD stable dương     │
                ├────────────────────┼────────────────────┤
  UD ≈ 0        │ CHÁN               │                    │
  (no desire)   │ không desire nào    │                    │
                └────────────────────┴────────────────────┘

⚠️ Table trên dùng "UD âm/dương" = view ĐƠN GIẢN (1 chiều).
   Xem §5.6 cho model chi tiết hơn: Present × Desire × Coherence (3 chiều).

UD-specific insights:
  Xúc động = deep desire CONFIRMED → opioid + oxytocin burst
  → Bạn xúc động vì CÁI GÌ → cho biết deep desire của bạn LÀ GÌ

  Confirmation bias = desire "schema đúng" → thích info CONFIRM
  → PE giải thích yếu (confirming = predicted = boring?)
  → UD giải thích trực tiếp (confirming = desire match → dopamine)
```

### 5.6 UD State — Trạng Thái Tổng Thể {Present, Desire, Coherence}

```
Nhiều schema chạy SONG SONG → nhiều UD SONG SONG → cần AGGREGATE.

UD State = trạng thái tổng thể = {Present, Desire, Coherence}

CHIỀU 1 — PRESENT (hiện tại):
  = Experience/Connection ĐANG được đáp ứng hay không?
  (+): đang tốt (ăn ngon, ôm người thân, yên tâm có người yêu)
  (0): bình thường, baseline (có oxy thở — không nghĩ tới)
  (−): đang bị vi phạm (đau, bị bỏ rơi, mất mát)

CHIỀU 2 — DESIRE (tương lai):
  = Vô thức MONG MUỐN / DỰ ĐOÁN gì?
  (+): mong gì tốt (desire approaching)
  (+, BLOCKED): muốn nhưng biết không được (buồn)
  (0): không mong gì (contentment hoặc apathy)
  (−): dự đoán xấu (lo âu)

CHIỀU 3 — COHERENCE (bổ sung):
  = Các schema đồng hướng hay xung đột?
  Cao: decisive, rõ ràng
  Thấp: conflicted, rối

Ma trận Present × Desire:

                 Desire (+)         Desire (0)         Desire (−)
                 (muốn thêm)       (không mong gì)    (dự đoán xấu)
              ┌─────────────────┬─────────────────┬─────────────────┐
Present (+)   │ HÁNG HÁI        │ THỎA MÃN        │ HẠNH PHÚC + LO │
(đang tốt)    │ excited          │ content          │ anxious joy    │
              ├─────────────────┼─────────────────┼─────────────────┤
Present (0)   │ MONG CHỜ         │ BÌNH THƯỜNG      │ LO ÂU          │
(bình thường) │ anticipation     │ neutral          │ anxiety        │
              ├─────────────────┼─────────────────┼─────────────────┤
Present (−)   │ BUỒN             │ ĐAU              │ TUYỆT VỌNG     │
(đang xấu)    │ sadness          │ pain             │ despair        │
              │ (muốn nhưng      │ (chịu vậy)       │ (xấu + sẽ      │
              │  không được)     │                  │  xấu hơn)      │
              └─────────────────┴─────────────────┴─────────────────┘

Neurochemistry map:
  Present    ↔ Experience + Connection hiện tại (Lớp 1 Source)
  Desire     ↔ Novelty seeking (Lớp 2 Amplifier)
  Coherence  ↔ Schema alignment (Software layer)

"Chán" decompose thành 3 loại:
  Type A: UD EXHAUSTED → bình an, đủ rồi (Present 0, Desire 0, Coherence HIGH)
  Type B: UD MISMATCH → restless, muốn thêm (Present 0, Desire +, context trống)
  Type C: UD SUPPRESSED → anhedonia (Present −, Desire suppressed, Novelty broken)
  → PE cũ: cả 3 = "PE=0". UD: 3 loại khác nhau → 3 treatments khác nhau.

Luồng:
  Schemas → UD per schema → UD State {Present, Desire, Coherence}
    ├→ Emotion: readout UD State ra conscious
    │   Vui = Present(+). Buồn = Present(−) + Desire(+, blocked).
    │   Lo = Desire(−). Chán = 3 types khác nhau.
    ├→ UD Arbitration: PFC phân xử giữa schemas (xem §5.8)
    │   PFC predict body reward per option → CHỌN schema → Drive
    │   Level 1 (PFC off): loudest wins. Level 2: short-term. Level 3: long-term.
    ├→ Drive per action: KẾT QUẢ arbitration → motivation cụ thể
    │   DRIVE = Desire(selected by arbitration) − Cost
    └→ Execute → Body respond → Schema update → loop

→ Chi tiết: UD-Hypothesis.md §4.8 + §4.9
```

### 5.7 UD State trong đời thường — Ví dụ minh họa

```
CASE 1: Sáng thứ 2 đi làm — Multi-schema conflict phổ biến nhất

  Schema A (career): "phải productive" → Desire(+)
  Schema B (comfort): "muốn ngủ thêm" → Present(+, giường ấm)
  Schema C (social): "sếp sẽ đánh giá" → Desire(−, threat)
  Schema D (identity): "tôi là người có trách nhiệm" → Desire(+)

  UD State: Present(+) × Desire(mixed) × Coherence(LOW)
  → Mâu thuẫn → khó chịu → ai thắng TÙY HÔM ĐÓ:
    Ngủ đủ → PFC available → Schema D win → dậy đi làm
    Thiếu ngủ → PFC yếu → Schema B win → snooze
  → Cùng người, cùng tình huống, KHÁC hành vi vì KHÁC PFC resource
```

```
CASE 2: Lướt MXH lúc 11 đêm — Micro-desire loop

  Schema A: "nên ngủ" → Desire(+, sleep)
  Schema B: "thêm 1 post nữa" → micro-desire liên tục RENEW
  Schema C: "sợ miss gì đó" → Desire(−, FOMO)

  UD State: Present(0) × Desire(mixed, micro) × Coherence(LOW)
  → Mỗi scroll = micro UD fulfill → dopamine nhẹ → desire MỚI ngay
  → Không bao giờ "xong" vì desire RENEW mỗi post
  → PFC: "nên ngủ" nhưng THUA micro-dopamine loop
  → Tại sao mọi người BIẾT nên ngủ mà vẫn lướt = Drive Equation:
    micro-desire(liên tục) − cost(thấp, chỉ nằm cuộn) = DRIVE (+) mỗi post
    sleep desire(+) − cost(phải đặt điện thoại xuống) = DRIVE thấp hơn
```

```
CASE 3: Cãi nhau với người yêu xong im lặng — Multi-blocked desire

  Schema A (connection): desire ôm, làm hòa → Desire(+, BLOCKED bởi pride)
  Schema B (pride): "mình đúng" → Desire(+, win)
  Schema C (fear): "xin lỗi = yếu thế" → Desire(−, threat)
  Schema D (love): "mình yêu họ" → Present(−, đang thiếu connection)

  UD State: Present(−) × Desire(+, MULTI-BLOCKED) × Coherence(RẤT THẤP)
  → CỰC KHÓ CHỊU — muốn nhiều thứ MÂU THUẪN NHAU
  → Thường: ai có Schema C (fear) yếu hơn → nhượng bộ trước
  → Hoặc: đủ lâu → Present(−) tích lũy vượt Schema B → "thôi xin lỗi"
  → Tại sao cãi nhau lâu = KHỔ: Coherence thấp + Experience âm + Desire blocked
```

```
CASE 4: Cùng event, khác schema depth → khác hành vi

  Event: Bị sếp chê trước team

  Người A (schema sâu: "tôi có giá trị"):
    L5 stable → Experience baseline ok
    Surface: "sếp sai" → Desire(+, chứng minh)
    UD State: Pres(−, nhẹ) × Des(+, clear) × Coh(HIGH)
    → Motivated anger → hành vi: chứng minh sếp sai

  Người B (schema sâu: "tôi vô giá trị"):
    L5 bất ổn → Experience baseline đã thấp
    Surface: "sếp đúng, mình kém" → Desire(+, blocked)
    UD State: Pres(−, nặng) × Des(+, blocked) × Coh(LOW)
    → Depression trigger → hành vi: im lặng, tránh né

  → CÙNG event, KHÁC schema profile → KHÁC UD State → KHÁC hành vi
  → Không cần "personality type" — chỉ cần biết schema profile

INSIGHT: "Tính cách" = pattern ỔN ĐỊNH của schema + UD,
         không phải label cố định.
         Thay đổi schema → thay đổi UD pattern → thay đổi "tính cách"
```

### 5.8 UD Arbitration — PFC Phân Xử Giữa Các Schema

```
ĐỊNH NGHĨA:
  UD State = BẢNG TỶ SỐ (passive, mô tả trạng thái)
  UD Arbitration = TRỌNG TÀI (active, phân xử → quyết định hành vi)

  PFC = trọng tài giữa các schemas:
    → PFC KHÔNG có desire riêng
    → PFC nghe TẤT CẢ schemas → predict body reward mỗi option → PHÂN XỬ
    → Giống trọng tài: không đá bóng, chỉ phân xử ai thắng

LUỒNG HOÀN CHỈNH:
  Schemas → UD per schema → UD State (aggregate)
    → UD Arbitration (PFC predict + phân xử)
      → Drive (specific action)
        → T3 Hành Vi
          → Body respond (ground truth)
            → Schema update → loop

3 LEVELS CỦA UD ARBITRATION:

  LEVEL 1 — PFC OFFLINE (yếu/mệt/say/stress):
    → KHÔNG có arbitration thực sự
    → Schema MẠNH NHẤT tự win (loudest signal)
    → = Autopilot: BG (habit) hoặc Amygdala (threat) điều khiển
    → Ví dụ: mệt → ăn junk food (schema "ngon" loudest)
    → Ví dụ: say → nói thật (schema suppressed lúc tỉnh → release)

  LEVEL 2 — PFC MODERATE (bình thường):
    → PFC scan UD States → predict NGẮN-TRUNG HẠN
    → Chọn schema có predicted body reward CAO NHẤT trong 1 ngày-1 tuần
    → Suppress tạm schemas khác (tốn PFC resource)
    → Ví dụ: "đói nhưng deadline → làm xong rồi ăn ngon hẳn"

  LEVEL 3 — PFC STRONG (trained/rested/high capacity):
    → PFC scan UD States → predict DÀI HẠN (tháng-năm-đời)
    → Có thể CHỌN schema ÂM bây giờ vì DƯƠNG về sau
    → Có thể phân xử giữa nhiều options PHỨC TẠP + mâu thuẫn
    → Thậm chí: chọn điều CHÍNH MÌNH CŨNG THẤY ĐAU khi chọn
    → Ví dụ: nguyên thủ ra quyết định hy sinh chiến thuật
      Schema "bảo vệ quân": UD = −5
      Schema "cứu dân dài hạn": UD = +8
      → PFC predict: net body reward dài hạn (+4) > không hy sinh (−8)
      → CHỌN dù Experience NGAY = cực âm
      → = "Quyết định khó khăn" = Level 3 arbitration

PFC PREDICT HORIZON quyết định chất lượng arbitration:
  PFC yếu:       predict 5 phút → body reward NGAY
  PFC vừa:       predict 1 ngày → balance ngắn/dài
  PFC mạnh:      predict tháng/năm → sustainable reward
  PFC cực mạnh:  predict cả đời → legacy, meaning (L5 desire)

  → "Delayed gratification" KHÔNG phải "chịu khó"
  → = PFC predict CHÍNH XÁC rằng body reward DÀI HẠN > ngắn hạn
  → Marshmallow test: trẻ wait = PFC đủ mature predict xa
  → Trẻ không wait = PFC chưa đủ predict horizon

ARBITRATION vs SUPPRESSION — khác nhau:
  Arbitration: CHỌN schema A, schema B TẠM CHỜ (acknowledged, sẽ quay lại)
    → Cost: vừa phải, sustainable
    → Schema B biết "sẽ đến lượt" → UD âm nhẹ

  Suppression: CHỌN schema A, schema B BỊ ÉP IM (denied, pretend không có)
    → Cost: CAO, PFC resource bị tiêu hao liên tục
    → Schema B bị suppress → tích lũy → explosion hoặc burnout
    → Tại sao suppress MÃI → mệt: PFC resource FINITE

  → Trọng tài GIỎI: "B chờ, A đi trước, B sẽ đến lượt sau"
  → Trọng tài TỆ: "B câm đi!" → B tích lũy → nổ

  ⚠️ Journaling/therapy giúp: externalize schemas → PFC bớt giữ
     → Arbitration DỄ HƠN khi schemas được NHÌN THẤY rõ ràng
```

---

## 6. T3: Hành Vi — Execute Strategy để Fulfill Desire

### 6.1 Hành Vi = Strategy Fulfillment

```
Hành vi KHÔNG phải "response to prediction error"
Hành vi = STRATEGY để FULFILL desire

3 con đường fulfill — khác nhau ở BODY RESPONSE fidelity:

  A. IMAGINATION (Con đường giả lập):
     → PFC tưởng tượng → body respond NHẸ (preview, ~20-40% fidelity)
     → Evolutionary advantage: test 100 scenarios × body preview → chọn 1
     → Nhanh, không tốn effort, giảm risk.
     → Limitation: body BIẾT là giả → reward không bền (= draft, chưa final)
     → Risk: over-simulate → body đã preview đủ → gặp thật hết hứng

  B. REALITY (Con đường thực tế):
     → Execute hành vi → body nhận kết quả THẬT → opioid/oxytocin MẠNH (~100%)
     → Multi-modal: da cảm nhận, mắt thấy, tai nghe → body TOÀN DIỆN respond
     → = Final version. Body confirm: "ĐÚNG, cái này tốt thật"
     → Tại sao thực tế > tưởng tượng: body fidelity 100% vs 20-40%

  C. EXTERNAL VALIDATION (Con đường xác nhận):
     → Người khác confirm → opioid (coherence) + oxytocin (connection) DOUBLE
     → Body nhận THÊM signal: "không chỉ tôi thấy đúng — DOMAIN cũng confirm"
     → Mạnh nhất vì: body reward từ 2 channels + external ground truth
     → Tại sao nhà khoa học cần publish, nghệ sĩ cần khán giả:
       body MUỐN reality confirm, không chỉ self-confirm

  Ideal cycle: A (preview) → B (confirm) → C (validate) = full body reward
```

### 6.2 Mô Hình Vuông — Giữ nguyên

```
Source × Depth per domain. 4 nhãn = 4 cạnh, không phải 4 ô.
UD không thay đổi Mô Hình Vuông — chỉ giải thích TẠI SAO:
  Architect = desire coherence deep → internal + deep
  Soldier = desire stability/safety → external + deep
  Improviser = desire novelty broad → internal + shallow
  Drifter = desire unfulfilled / no desire → any + shallow
```

### 6.3 Feedback Loops (UD version)

```
LOOP 1: Container → T2 (LEARNING — serve future desire better)
  Observe → chunks → schema update → better prediction → better fulfillment

LOOP 2: T2 → T3 → Container (ACTION — fulfill desire)
  Desire → strategy → hành vi → thay đổi môi trường → desire fulfilled/not

LOOP 3: Container → T1 (ADAPTATION — desire priority shift)
  Stress mãn tính → cortisol → desire "an toàn" priority TĂNG

LOOP 4: T1 → T2 (CONSTRAINT — set desire range)
  Hardware capacity → max desire complexity
  Channels → LOẠI desire nào mạnh nhất

LOOP 5: T3 → Domain (EXPANSION — mở rộng "luật chơi")
  Hành vi khám phá → domain mới → desire mới possible

LOOP 6: T3 → T2 (FEEDBACK — desire matched?)
  Kết quả → match desire? → YES: reinforce. NO: update strategy.

LOOP 7: T3 → T1 (USAGE — rất chậm)
  Hành vi mãn tính → hardware change → desire baseline shift
```

---

## 7. Domain — Giữ nguyên

```
Domain = chiều ngang xuyên suốt. KHÔNG phụ thuộc PE hay UD.
  Objective · Abstract · Intersubjective · Subjective

UD-specific:
  Schema = bản đồ. Domain = lãnh thổ.
  Desire match domain = effective fulfillment
  Desire mismatch domain = fail → UD âm → update schema → try again
  → Learning = improve map (schema) để find treasure (fulfillment) better
```

---

## 8. Thứ Tự Can Thiệp — UD Version

```
1. TỐI ƯU CORTISOL (luôn bước 1)
   → Cortisol cao → desire "an toàn" chiếm hết resource
   → Giảm cortisol = free resource cho desire khác

2. IDENTIFY DESIRE (MỚI — không có trong PE version)
   → "Bạn thực sự MUỐN gì?" (unconscious, không phải conscious want)
   → Desire nào đang unfulfilled MÃN TÍNH?
   → Desire nào đang fulfilled bởi proxy SAI? (ăn bù buồn = wrong channel)

3. SỬA SCHEMA (4 schema nền)
   → Schema sai → desire hướng SAI → fulfill không hiệu quả
   → "Tôi vô giá trị" → desire "chứng minh" mãn tính → never enough

4. CALIBRATE THRESHOLD (composite: hardware + schema_pressure − suppression)
   → Identify: threshold cao vì HARDWARE hay vì SCHEMA PRESSURE?
   → Hardware cao → match environment phù hợp (không cần fix)
   → Schema pressure → fix schema âm → threshold TỰ GIẢM
   → Phát hiện suppression (fake contentment) → unlock trước, fix sau
   → Chi tiết: Research/Threshold-Analysis.md

5. MATCH DESIRE × DOMAIN × ENVIRONMENT
   → Tìm domain mà desire TỰ NHIÊN match
   → Thiết kế environment có nhiều con đường fulfill
   → = "Đúng người, đúng việc, đúng chỗ"

6. TRAIN 3 CON ĐƯỜNG
   → A: Imagination → practice giả lập (visualization, planning)
   → B: Reality → stepped exposure (từ nhỏ → lớn)
   → C: Validation → build community, publish, share
```

---

## 9. PE vs UD — So Sánh Trực Tiếp

### 9.1 Điểm GIỐNG (PE = special case of UD)

```
Khi desire = simple + conscious:
  PE: expected juice → no surprise → dopamine = 0
  UD: expected juice → desire pre-simulated → remaining UD ≈ 0
  → CÙNG prediction, CÙNG result
  → Schultz monkey data: CONSISTENT với cả PE lẫn UD
  → KHÔNG phân biệt được bằng simple cases
```

### 9.2 Điểm KHÁC (UD predict tốt hơn ở complex cases)

```
                        PE predict         UD predict         Thực tế
──────────────────────────────────────────────────────────────────────
Về quê (no novelty)     Boring (PE=0)      Warm (desire home)  Warm ✅UD
Nghe nhạc lần 50        Boring (predicted)  Still enjoy (renew) Still enjoy ✅UD
Người thân tặng quà     Low PE (expected)   High UD (desire)    High joy ✅UD
"Vừa ý" vs "khác ý"    Khác ý better       Vừa ý better       Vừa ý ✅UD
Confirmation bias       Boring (predicted)  Liked (desire match)Liked ✅UD
Comfort food khi buồn   Same (same food)    Better (desire↑)    Better ✅UD
Flow state              Boring? (PE low)    Great (continuous)  Great ✅UD
Cơm mẹ vs nhà hàng     Nhà hàng (novel)    Cơm mẹ (desire)    Cơm mẹ ✅UD
Đọc lại sách hay        Boring (known)      Still good (desire) Still good ✅UD

Tổng cases tested: 24+ (xem UD-Hypothesis.md §3.3)
  UD wins clearly:    18
  TIE:                 5
  PE wins:             0
  Both fail:           1
```

### 9.3 Điểm YẾU của UD (honest)

```
1. UNFALSIFIABLE risk: "sướng = desire matched, không sướng = not matched"
   → Cần SPECIFIC predictions khác PE → test được

2. "Unconscious desire" khó đo:
   → PE: actual − predicted = tính được
   → UD: desire strength? match degree? pre-simulated? → khó đo

3. Chưa có DIRECT neural evidence:
   → PE: Schultz record neurons, thấy PE pattern
   → UD: chưa ai record "desire fulfillment neurons"

4. Complexity: UD cần NHIỀU variables hơn PE
   → PE: 2 biến (actual, predicted)
   → UD: N biến (N desires × match × pre-simulated)
   → Simpler = better? (Occam's razor)

→ UD KHÔNG thay thế PE — UD MỞ RỘNG PE cho complex cases
→ PE vẫn đúng, vẫn hữu ích, vẫn là special case
→ UD thêm explanatory power ở chỗ PE yếu
```

---

## 10. UD Development — Toàn Bộ Cuộc Đời

```
Trẻ sơ sinh:
  UD: warmth (opioid) + connection (oxytocin)
  → Đơn giản, PFC chưa phát triển. 100% phụ thuộc caregiver.

Trẻ nhỏ (2-6):
  UD EXPAND — tò mò mọi thứ
  → Schema ít → nhiều thứ chưa đồng bộ → NHIỀU desire
  → Dopamine HIGH (liên tục "approaching match")
  → Tại sao trẻ con tò mò VÔ TẬN

Thiếu niên (12-18):
  UD identity + belonging + status
  → Status (serotonin) bắt đầu matter. Connection desire MẠNH.
  → L5 firmware LAST MAJOR REVISION

Trưởng thành:
  UD CHUYÊN SÂU — career, relationship, meaning
  → Schema stable → ít desire random, nhiều desire targeted
  → PFC mature → serve UD hiệu quả

Về già:
  UD GIẢM (nhiều schema đã đồng bộ)
  → Wisdom = nhiều desire fulfilled → bình an
  → Nostalgia = re-activate old desire → re-fulfill (imagination)
  → "Truyền lại" = external validation cuối đời

→ UD giải thích trajectory motivation CẢ ĐỜI bằng 1 cơ chế:
  Desire hình thành → seek fulfillment → đồng bộ → desire mới → loop
```

→ Chi tiết UD trong phát triển trẻ em: Research/UD-Parenting.md

---

## 11. Giới Hạn + Câu Hỏi Mở

### 11.1 UD-specific

```
U1: UD có thể operationalize (đo lường) được không?
    → Cần proxy: physiological, behavioral, neural
U2: UD vs RPE: experiment nào tách biệt 2 predictions?
    → 3 proposed experiments trong UD-Hypothesis.md §6.2
U3: "Unconscious desire" có nhiều layers không?
    → Biological (hunger) vs cognitive (coherence) vs social (belonging)
    → Interact thế nào?
U4: UD trong AI: máy có "desire" không?
    → Objective function ≈ desire? Loss minimization ≈ UD?
```

### 11.2 Kiến trúc (giữ từ PE-centric)

```
A1-A8: Giữ nguyên (không phụ thuộc PE hay UD)
Câu hỏi kế thừa: Giữ nguyên
```

---

## 12. File Map

```
Human Predictive Drive/
├── Core.md                              ← v6.0 (production, PE-based)
├── Research/
│   ├── Core-v7-Draft-Good.md            ← v7.0 DRAFT PE-centric
│   ├── Core-v7-UD.md                    ← ★ FILE NÀY — v7.0 DRAFT UD-centric
│   ├── UD-Hypothesis.md                 ← UD giả thiết chi tiết + 24 cases
│   ├── UD-Parenting.md                  ← UD trong phát triển trẻ em
│   ├── Threshold-Analysis.md            ← Threshold decompose + 6 cases
│   ├── Drive-Optimization.md           ← ★ Amplifier Trap + Sustainable Peak
│   ├── PFC-Analysis.md                 ← ★ PFC sub-regions + profiles + training
│   ├── Parameters-Review.md            ← Tham số cần clarify (①②③④)
│   ├── Component-Interaction-Map.md    ← Schema + brain analysis
│   ├── Emotion-Map.md                  ← Emotion mapping
│   └── ...
├── Core-Deep-Dive/                      ← Đào sâu per component
└── Validation/                          ← Kiểm chứng
```

---

## 13. References

```
UD-specific:
  Schultz (1997) — RPE: UD = superset, RPE = special case 🟢→🔴
  Berridge (1998) — Wanting vs Liking: UD builds ON wanting 🟢
  Panksepp (1998) — SEEKING system: aligned with UD 🟢
  Friston (2010) — Active Inference: UD ≈ conceptual version 🟢
  Damasio (1994) — Somatic markers: body knows desire first 🟢
  Bowlby (1958) — Attachment: UD calibration in childhood 🟢
  Ainsworth (1978) — 4 styles = 4 UD profiles 🟢→🔴

Framework-specific:
  UD hypothesis (desire > prediction for complex cases) 🔴
  Neurochemistry 3 lớp (Source/Amplifier/Modulator) 🔴
  3 con đường fulfill (Imagination/Reality/Validation) 🔴
  UD Parenting (attachment = UD calibration) 🔴
  Container model 🔴
  PFC as arbitrator OF desire (trọng tài, không phải nhạc trưởng) 🟡
```

---

> *Human Predictive Drive — v7.0 UD-Centric DRAFT*
> *"Não = máy mong muốn. Mọi hành vi = tìm kiếm fulfillment."*
> *UD = giả thiết. Song song với PE-centric. So sánh để refine.*
