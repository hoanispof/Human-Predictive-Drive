# Parameters Review — Tham Số Cần Phân Tích Sâu

> **Trạng thái:** DRAFT — ghi nhận các tham số chưa rõ ràng
> **Ngày:** 2026-03-15
> **Mục đích:** Xác định tham số nào giữ, bỏ, hoặc chuyển vị trí
> **Reference:** Core-v7-UD.md §4.2 (Parameters) + §4.3 (Processing Infrastructure)

---

## 1. Tổng Quan Tham Số Hiện Tại

```
ĐÃ RÕ RÀNG (không cần review):
  ✅ WM Capacity — hardware, fixed, đo được (digit span, N-back)
  ✅ Threshold — decompose xong (hardware + schema_pressure − suppression)
  ✅ UD Decay Rate (③) — rõ cơ chế (pre-simulation → desire giảm)
  ✅ Baseline Drive — ghi rõ emergent metric, không phải parameter
  ✅ Schema Ceiling — ghi rõ emergent metric
  ✅ PFC Activation Level — ghi rõ dynamic state, không phải parameter

CẦN PHÂN TÍCH SÂU:
  🟡 ① Amplitude — có trùng Threshold không?
  🟡 ② Precision — có trùng PFC Activation không?
  🟡 ④ Generalization — rõ concept, mờ mechanism
  🟡 ③ UD Decay Rate — rõ nhất nhưng cần clarify hardware vs software
```

---

## 2. ① Amplitude — Giữ, Bỏ, hay Merge?

### 2.1 Định nghĩa hiện tại

```
Amplitude = "volume UD signal" — cùng desire, khác reaction intensity
Ví dụ: 2 người cùng được khen → 1 người rất vui, 1 người vui nhẹ
```

### 2.2 Vấn đề: Có trùng Threshold không?

```
Threshold: mức UD fulfillment TỐI THIỂU để "đủ"
  → Threshold cao → cần NHIỀU để thỏa mãn → "ít phản ứng" với stimulus nhỏ
  → Threshold thấp → cần ÍT → "phản ứng mạnh" với stimulus nhỏ

Amplitude: volume UD signal
  → Amplitude cao → phản ứng MẠNH
  → Amplitude thấp → phản ứng NHẸ

Trông giống: Threshold thấp ≈ Amplitude cao?
  → Nếu đúng → Amplitude = 1/Threshold → TRÙNG → bỏ Amplitude
```

### 2.3 Phân tích: Có case nào Amplitude ≠ 1/Threshold không?

```
CASE A: Threshold THẤP + Amplitude THẤP — có tồn tại không?
  = Dễ thỏa mãn (threshold thấp) nhưng phản ứng nhẹ (amplitude thấp)
  = "Hài lòng dễ, nhưng không hào hứng gì lắm"
  = Có thể: người bình thản, contentment mà không euphoria
  → CÓ VẺ TỒN TẠI → 2 parameter KHÁC NHAU?

CASE B: Threshold CAO + Amplitude CAO — có tồn tại không?
  = Khó thỏa mãn (threshold cao) nhưng khi thỏa mãn thì CỰC sướng
  = "Khó tính nhưng khi đúng ý thì PHẢN ỨNG MẠNH"
  = Có thể: nghệ sĩ, perfectionist — threshold cao cho chất lượng,
    nhưng khi gặp masterpiece → overwhelmed
  → CÓ VẺ TỒN TẠI → 2 parameter KHÁC NHAU?

CASE C: Threshold CAO + Amplitude THẤP
  = Khó thỏa mãn + phản ứng yếu khi thỏa mãn
  = "Khó chiều + không biết enjoy"
  = Có thể: anhedonia? Depression? Burnout?
  → HOẶC: đây là bệnh lý, không phải variation bình thường?

CASE D: Threshold THẤP + Amplitude CAO
  = Dễ thỏa mãn + phản ứng mạnh
  = "Vui với mọi thứ, hay phấn khích"
  = Có thể: trẻ con? Người lạc quan tự nhiên?
  → CÓ VẺ TỒN TẠI
```

### 2.4 Kết luận tạm

```
Nếu Case A và Case B tồn tại → Amplitude ≠ Threshold → GIỮ cả hai
Nếu KHÔNG tồn tại → Amplitude = 1/Threshold → BỎ Amplitude

⚠️ CẦN THÊM PHÂN TÍCH:
  → Amplitude có thể là HARDWARE (receptor sensitivity)?
  → Threshold hardware = D2 receptor DENSITY
  → Amplitude = receptor SENSITIVITY (khác density)
  → Density ≠ Sensitivity? Cần neuroscience check

  → Hoặc: Amplitude = EMOTIONAL REACTIVITY (Amygdala sensitivity)
  → Threshold = REWARD SYSTEM requirement (dopamine system)
  → 2 hệ thống KHÁC NHAU → 2 parameters KHÁC NHAU?

STATUS: 🟡 CÓ VẺ NÊN GIỮ nhưng cần redefine rõ hơn
  Đề xuất tạm:
    Threshold = dopamine system requirement (bao nhiêu để "đủ")
    Amplitude = emotional reactivity (phản ứng MẠNH cỡ nào khi có signal)
    → 2 hệ thống khác nhau → giữ cả hai
    → Nhưng cần verify bằng neuroscience
```

---

## 3. ② Precision — Giữ, Bỏ, hay Merge?

### 3.1 Định nghĩa hiện tại

```
Precision = "UD signal đáng tin cỡ nào trước khi act"
Ví dụ: cùng nghe tin "công ty sắp layoff"
  → Precision cao: chờ confirm → rồi mới react
  → Precision thấp: react NGAY → panic/action trước khi verify
```

### 3.2 Vấn đề: Có trùng PFC Activation không?

```
PFC Activation: PFC đang AVAILABLE bao nhiêu %
  → PFC cao → cẩn thận, deliberate → "trông như precision cao"
  → PFC thấp → impulsive, automatic → "trông như precision thấp"

Precision: UD signal đáng tin cỡ nào
  → Precision cao → cần NHIỀU evidence trước khi act
  → Precision thấp → act trên LITTLE evidence

Trông giống: PFC Activation cao ≈ Precision cao?
  → Nếu đúng → Precision = PFC state → TRÙNG → bỏ Precision
```

### 3.3 Phân tích: Có case nào Precision ≠ PFC Activation không?

```
CASE A: PFC CAO + Precision THẤP — có tồn tại không?
  = PFC available (không mệt, không stress) nhưng VẪN act nhanh trên ít evidence
  = "Tỉnh táo nhưng impulsive BY NATURE"
  = Có thể: ADHD? DRD4 7-repeat? Novelty-seeking trait?
  → CÓ VẺ TỒN TẠI → Precision CÓ THỂ là trait riêng

CASE B: PFC THẤP + Precision CAO — có tồn tại không?
  = PFC mệt nhưng VẪN cẩn thận, chờ evidence
  = "Mệt nhưng vẫn systematic"
  = Khó tưởng tượng? Vì precision cần PFC resource?
  → CÓ VẺ KHÔNG TỒN TẠI → Precision PHỤ THUỘC PFC?

CASE C: Cùng người, ngủ đủ vs thiếu ngủ
  = Ngủ đủ: PFC cao + precision trông cao
  = Thiếu ngủ: PFC thấp + precision trông thấp
  → Precision THAY ĐỔI theo PFC state → KHÔNG phải trait?
  → → Gợi ý: Precision = PFC-dependent, không phải independent parameter
```

### 3.4 Nhưng: có BASELINE precision không?

```
Cùng PFC level (cả 2 ngủ đủ, khỏe mạnh):
  Người A: vẫn cẩn thận, check nhiều lần → baseline precision CAO
  Người B: vẫn act nhanh, ít check → baseline precision THẤP

  → CÓ THỂ: Precision = Hardware BASELINE (trait)
             + PFC Activation MODULATE (state)
  → Giống Threshold: hardware floor + software/state ảnh hưởng

  → Precision_observed = Precision_baseline (trait) × PFC_activation (state)
  → PFC thấp → precision giảm bất kể baseline
  → PFC cao → precision = baseline (trait thể hiện)
```

### 3.5 Kết luận tạm

```
STATUS: 🟡 PHỨC TẠP — có thể giữ nhưng cần redefine

  Option A: BỎ Precision — coi như = PFC Activation
    Ưu: đơn giản hơn
    Nhược: không giải thích tại sao cùng PFC level, khác cẩn thận

  Option B: GIỮ Precision = TRAIT (baseline)
    Precision_baseline = hardware tendency cẩn thận/impulsive
    PFC Activation = state modulate precision
    Ưu: giải thích individual differences
    Nhược: thêm parameter

  Option C: MERGE Precision vào UD Sensitivity tổng thể
    "Sensitivity" bao gồm cả "phản ứng nhanh/chậm" (precision)
    lẫn "phản ứng mạnh/yếu" (amplitude)
    → Sensitivity = {amplitude, precision, decay, generalization}
    → Giữ nhưng GHI RÕ: precision = trait × PFC state

  → Hiện tại đã ở Option C — có thể giữ nguyên, chỉ thêm note
```

---

## 4. ④ Generalization — Giữ, Bỏ, hay Redefine?

### 4.1 Định nghĩa hiện tại

```
Generalization = "fulfill desire A → desire tương tự B có giảm?"
Ví dụ: ăn phở ngon (fulfill) → muốn ăn bún bò (tương tự) có giảm?
```

### 4.2 Phân tích

```
Generalization TỐT (transfer learning):
  → Hiểu vật lý → dễ hiểu engineering (related domains)
  → UD: fulfill desire "hiểu vật lý" → desire "hiểu engineering" PARTIALLY fulfilled
  → = Positive transfer

Generalization XẤU (overgeneralization):
  → Bị chó cắn 1 lần → sợ TẤT CẢ chó (phobia)
  → UD: 1 bad experience → desire "an toàn" violated → generalize → ALL dogs = threat
  → = Overgeneralization

Generalization TRUNG TÍNH:
  → Ăn phở ngon → vẫn muốn bún bò (khác dish = khác desire)
  → Hoặc: ăn phở ngon → giảm muốn bún bò (đã no = biological, không phải generalization)
```

### 4.3 Vấn đề: Generalization là PARAMETER hay MECHANISM?

```
Parameter = đặc điểm CỐ ĐỊNH của 1 người → đo được
Mechanism = cách 1 PROCESS hoạt động → không phải số

Generalization có vẻ = MECHANISM hơn parameter:
  → Cách schema CONNECTIONS lan truyền
  → Schema A connected to B → fulfill A → partially fulfill B (via connection)
  → Schema A NOT connected to C → fulfill A → C unchanged
  → = Phụ thuộc SCHEMA STRUCTURE, không phải parameter cố định

  → Người có schema RỘNG (nhiều connections) → generalization CAO
  → Người có schema HẸP (ít connections) → generalization THẤP
  → → Generalization = EMERGENT từ schema structure?
  → → Giống Schema Ceiling: không phải parameter, là kết quả

NHƯNG:
  → Có người TENDENCY generalize nhiều (trait?)
  → Anxiety = overgeneralize BY DEFAULT (trait? hardware? Amygdala sensitivity?)
  → Autism spectrum = undergeneralize (trait? hardware? different wiring?)
  → → Có thể có HARDWARE component → baseline generalization trait
```

### 4.4 Kết luận tạm

```
STATUS: 🟡 CÓ THỂ CHUYỂN từ parameter sang mechanism

  Option A: GIỮ là sub-parameter của UD Sensitivity
    → Generalization rate = trait + schema structure
    → Đơn giản, vị trí hiện tại ok

  Option B: CHUYỂN sang MECHANISM trong T2 Software
    → Generalization = cách schema connections lan truyền
    → Không phải parameter cố định → thuộc về Software behavior
    → Hardware baseline (Amygdala, wiring) vẫn ở T1
    → Software manifestation ở T2

  Option C: SPLIT
    → Generalization_hardware = tendency (T1, trait)
    → Generalization_behavior = actual spreading (T2, mechanism)
    → Giống Threshold: hardware baseline + software influence

  → Cần phân tích thêm trước khi quyết định
```

---

## 5. ③ UD Decay Rate — Clarify Hardware vs Software

### 5.1 Định nghĩa hiện tại

```
UD Decay Rate = tốc độ desire "hết hứng" sau fulfillment
  = pre-simulation tăng → remaining desire GIẢM
  → Rõ nhất trong 4 sub-parameters
```

### 5.2 Cần clarify

```
Hardware component:
  → Receptor adaptation (neurotransmitter → receptor downregulate)
  → LTP/LTD (neural connection strengthen/weaken)
  → Dopamine system adaptation speed (fast adapter vs slow adapter)
  → = Gen quy định phần nào → trait

Software component:
  → Pre-simulation (tưởng tượng trước → desire giảm)
  → Schema update (đã fulfilled → schema mark "done")
  → Attention shift (PFC chuyển sang desire khác)
  → = Experience-driven → state

Ví dụ kiểm chứng:
  Trẻ con: decay rate THẤP (xem cùng phim 100 lần vẫn thích)
    → Hardware (immature receptor system)? Hay Software (ít pre-simulation capacity)?
    → Có lẽ CẢ HAI: hardware chưa mature + WM thấp → ít pre-simulate

  Người lớn chán nhanh vs chậm:
    → Hardware (fast adapter)? Hay Software (pre-simulate nhiều)?
    → Người thông minh chán nhanh hơn? (WM cao → pre-simulate nhanh → decay nhanh?)
    → → Gợi ý: Decay Rate LIÊN QUAN WM Capacity
    → → WM cao → simulate nhanh → desire giảm nhanh → chán nhanh
    → → Nhưng WM cao cũng → desire MỚI nhanh → bù lại

STATUS: 🟢 GIỮ — rõ nhất, chỉ cần ghi note "hardware + software component"
```

---

## 6. Tổng Kết Quyết Định

```
PARAMETER          │ STATUS    │ ĐỀ XUẤT TẠM        │ CẦN LÀM
════════════════════╪═══════════╪═════════════════════╪══════════════════
① Amplitude        │ 🟡 MỜ    │ GIỮ, redefine rõ    │ Verify: ≠ Threshold?
                   │           │ = emotional reactivity│ Check neuroscience
                   │           │ (Amygdala-based?)     │
────────────────────┼───────────┼─────────────────────┼──────────────────
② Precision        │ 🟡 MỜ    │ GIỮ dạng hiện tại   │ Clarify: trait
                   │           │ = trait × PFC state   │ vs PFC-dependent
                   │           │ (giữ trong Sensitivity)│
────────────────────┼───────────┼─────────────────────┼──────────────────
③ UD Decay Rate    │ 🟢 RÕ    │ GIỮ nguyên          │ Ghi note: hw + sw
                   │           │ = pre-simulation +    │ Liên quan WM?
                   │           │   receptor adaptation │
────────────────────┼───────────┼─────────────────────┼──────────────────
④ Generalization   │ 🟡 MỜ    │ Có thể CHUYỂN sang   │ Phân tích: param
                   │           │ mechanism (T2) hoặc   │ hay mechanism?
                   │           │ SPLIT hw + sw         │ Check autism/anxiety
────────────────────┼───────────┼─────────────────────┼──────────────────

KHÔNG GẤP: Không tham số nào ảnh hưởng kiến trúc tổng thể.
  → Kiến trúc Container + T1/T2/T3 + Domain STABLE bất kể quyết định
  → UD hypothesis STABLE bất kể sub-parameters
  → Có thể ngâm thêm, phân tích khi có case study cụ thể
```

---

## 7. Câu Hỏi Mở

```
P1: Amplitude có thể đo bằng gì? (physiological response to standard stimulus?)
P2: Precision baseline có tương quan với personality traits (Big Five Conscientiousness)?
P3: Generalization có thể predict bằng schema connection density?
P4: Decay Rate có tương quan với IQ/WM? (thông minh hơn → chán nhanh hơn?)
P5: Có sub-parameter nào KHÁC chưa được phát hiện?
    → Ví dụ: "Recovery Rate" = tốc độ hồi phục sau UD âm?
    → Hoặc: "Desire Generation Rate" = tốc độ tạo desire mới?
```

---

> *Parameters Review — DRAFT*
> *Mục đích: clarify trước khi quyết định giữ/bỏ/chuyển*
> *Không gấp — kiến trúc tổng thể không phụ thuộc kết quả review này*
