# Reward Dual System — Hai Hệ Thống Phần Thưởng

> **Trạng thái:** DRAFT — Giả thiết suy luận, chưa validated
> **Ngày:** 2026-03-21
> **Mục đích:** Giải thích TẠI SAO con người có 2 hệ thống reward khác nhau,
> tại sao Prediction Error (RPE) không đủ cho con người, và luồng tương tác chi tiết
> **Reference:** Core-v7-UD.md, Prolactin-Analysis.md, Neurochemistry-v8-Draft.md
> **⚠️ Đây là SUY LUẬN — khác với nghiên cứu gốc RPE (Schultz 1997)**

---

## 1. Vấn Đề Với Prediction Error (PE)

```
Schultz (1997) — Prediction Error:
  "Dopamine fire khi THỰC TẾ khác DỰ ĐOÁN" (error)
  → Positive PE: thực tế TỐT HƠN dự đoán → dopamine fire
  → Zero PE: thực tế ĐÚNG dự đoán → dopamine = 0
  → Negative PE: thực tế TỆ HƠN dự đoán → dopamine suppress

  → ĐÚNG cho: dopamine neuron (level đơn lẻ) ✅
  → ĐÚNG cho: AI/AlphaGo (TD Learning) ✅
  → KHÔNG ĐỦ cho: con người (complex behavior) ❌

TẠI SAO KHÔNG ĐỦ — 3 hiện tượng PE KHÔNG giải thích:

  ① "Về quê vẫn vui" — dự đoán ĐÚNG, PE = 0 → nên BÌNH THƯỜNG
     Thực tế: về quê VẪN VUI dù biết trước mọi thứ → vui từ đâu?
     → PE miss: body reward (opioid warmth, oxytocin connection) KHÔNG cần surprise

  ② "Cơm mẹ nấu ngon hơn nhà hàng" — nhà hàng PE CAO hơn (novel)
     Thực tế: cơm mẹ NGON HƠN dù predict ĐÚNG HẾT → vì body reward THẬT (multi-channel)
     → PE miss: multi-channel body fulfill > single-channel surprise

  ③ "Đọc lại sách hay vẫn enjoy" — predict 100% ĐÚNG → PE = 0
     Thực tế: VẪN enjoy → vì body desire beauty/coherence RENEW mỗi lần
     → PE miss: body desire TÁI TẠO → không phụ thuộc surprise

  → PE MÔ TẢ dopamine neuron behavior → ĐÚNG
  → PE GIẢI THÍCH human behavior → KHÔNG ĐỦ
  → Cần: thêm HỆ THỐNG KHÁC bên cạnh dopamine PE
```

---

## 2. Hai Hệ Thống Reward

```
CON NGƯỜI có 2 hệ thống reward SONG SONG:

╔═══════════════════════════════════════════════════════════════╗
║  HỆ THỐNG 1 — IMAGINE REWARD (dự đoán, nhanh)                ║
║                                                               ║
║  Engine: Dopamine (VTA → Nucleus Accumbens)                   ║
║  Trigger: Imagine system predict "cái này TỐT HƠN cho body"  ║
║  Timing: TRƯỚC hành vi (predict → drive → thực hiện)          ║
║  Tốc độ: NHANH (simulate trong đầu, không cần thực tế)        ║
║  Độ chính xác: CÓ THỂ SAI (imagine ≠ reality)                ║
║  Chức năng: DRIVE hành vi ("đi làm cái này!")                 ║
║  Tương đương AI: Value Network predict (trước khi đi nước)    ║
║                                                               ║
║  Ví dụ:                                                       ║
║    "Nếu đun nước → ăn được → body ok!" → dopamine → drive đun ║
║    "Nếu hỏi AI → hiểu thêm → coherence!" → dopamine → drive  ║
║    "Nếu scroll thêm → có thể hay!" → dopamine → drive scroll  ║
╠═══════════════════════════════════════════════════════════════╣
║  HỆ THỐNG 2 — BODY REWARD (xác nhận, chậm)                   ║
║                                                               ║
║  Engine: Prolactin (Pituitary) + Opioid/Oxytocin (body-wide)  ║
║  Trigger: Body THẬT SỰ nhận reward → evaluate "đủ chưa?"     ║
║  Timing: SAU hành vi (thực hiện → body nhận → evaluate)       ║
║  Tốc độ: CHẬM (phải trải nghiệm thật)                        ║
║  Độ chính xác: CAO NHẤT (body = ground truth)                 ║
║  Chức năng: CONFIRM + CALIBRATE ("đúng thật! đủ rồi!")        ║
║  Tương đương AI: Actual Result (sau khi đi nước → biết thắng) ║
║                                                               ║
║  Ví dụ:                                                       ║
║    Đun được nước → ăn thật → body: "sướng!" + prolactin "đủ"  ║
║    Hiểu insight → coherence THẬT → body: "à ha!" + prolactin  ║
║    Scroll 1 tiếng → body: "...nhận gì thật?" → prolactin = 0  ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 3. Tại Sao 2 Hệ Thống — Evolutionary

```
ĐỘNG VẬT ĐƠN GIẢN (chỉ Hệ thống 2 — Body):
  Body cần → thử → kết quả → body learn
  = Mỗi lần học = PHẢI trải nghiệm thật → CHẬM + NGUY HIỂM
  Ví dụ: "lửa nóng?" → chạm → bỏng → learn
  → Cost: bỏng tay mỗi lần learn → expensive

ĐỘNG VẬT CÓ PFC SƠ KHAI (cả 2 hệ thống — nhưng imagine thô):
  Body cần → imagine THÔ ("giống lần trước?") → thử cẩn thận → body learn
  = Imagine = nhớ lại → predict → GIẢM cost
  Ví dụ: chuột thấy mèo lần trước → imagine "mèo = nguy" → TRÁNH
  → Cost giảm: không cần bị cắn lần 2

CON NGƯỜI (cả 2 hệ thống — imagine CỰC TINH VI):
  Body cần → imagine SIMULATE chi tiết → predict → dopamine DRIVE
  → Thực hiện CÓ CHỌN LỌC → body confirm → calibrate imagine
  = Imagine simulate 100 kịch bản → chọn 1 → thử 1 → learn từ 1
  → Cost giảm ×100: chỉ thử 1/100 → 99 kịch bản KHÔNG cần thử thật

  Ví dụ: "muốn qua sông"
    Động vật: thử bơi → chết hoặc sống → learn
    Người: imagine "cầu?" → "bè?" → "thuyền?" → chọn tốt nhất → thử 1 → ok
    → = Imagine (dopamine) SAVE cost → Body (prolactin) CONFIRM kết quả

  → HỆ THỐNG 1 (imagine) = TIẾT KIỆM chi phí thử sai
  → HỆ THỐNG 2 (body) = GROUND TRUTH xác nhận kết quả
  → CẢ HAI CÙNG CẦN: imagine predict → body confirm → imagine calibrate → chính xác dần
```

---

## 4. Dopamine = "Predict Improvement", KHÔNG phải "Predict Error"

```
SCHULTZ gọi: "Prediction Error" → gợi ý: SẢI LỆCH bất kỳ = dopamine
  → Error KHÔNG CÓ CHIỀU (error = khác, không biết tốt hay xấu)
  → NHƯNG: dopamine CHỈ fire khi KHÁC + TỐT HƠN → có CHIỀU

CHÍNH XÁC HƠN: dopamine = "Prediction Improvement Signal"
  = Imagine predict: "cái này TỐT HƠN hiện tại cho body"
  → TỐT HƠN → dopamine fire → DRIVE hành vi
  → TỆ HƠN → dopamine suppress → TRÁNH
  → GIỐNG → dopamine baseline → bình thường

  "Error" = khác (không biết tốt xấu) → TÊN SAI
  "Improvement" = tốt hơn cho body → TÊN ĐÚNG

  VÀ: Schultz thí nghiệm ĐƠNG GIẢN (khỉ + nước):
    "Tốt hơn" = nhiều nước hơn → RÕ RÀNG → "error" ≈ "improvement" (trùng)
    → Ở level đơn giản: 2 tên cho CÙNG KẾT QUẢ → không phân biệt được

  Với người PHỨC TẠP:
    "Tốt hơn" = imagine PREDICT body reward → KHÔNG rõ ràng như "nhiều nước"
    → "Error" = khác → có thể khác MÀ TỆ → dopamine KHÔNG fire → "error" SAI
    → "Improvement" = tốt hơn cho body → dopamine fire → ĐÚNG
    → → Ở level phức tạp: 2 tên cho KẾT QUẢ KHÁC → phân biệt ĐƯỢC

  → PE (Prediction Error) = OK cho simple cases (khỉ, AI)
  → PI (Prediction Improvement) = CHÍNH XÁC HƠN cho complex cases (người)
  → PI = PE + CHIỀU (improvement vs deterioration) + BODY REFERENCE (tốt cho body)
```

---

## 5. Luồng Chi Tiết — Từ Body-Need Tới Hành Vi

```
LUỒNG ĐẦY ĐỦ:

  ① Body có NHU CẦU (body-need active)
     → Cortisol/NE: activation energy → "cần làm gì đó"
     → Schema liên quan ACTIVATE

  ② Imagine SIMULATE các options
     → PFC workspace MỞ → vô thức chain schemas → multiple scenarios
     → Imagine evaluate MỖI scenario: "cái nào TỐT HƠN cho body?"
     → Scenario TỐT NHẤT → dopamine fire → DRIVE hành vi

  ③ Hành vi THỰC HIỆN (reality test)
     → Schema execute → tác động reality/domain
     → Body NHẬN kết quả THẬT (opioid/oxytocin nếu tốt)

  ④ Body EVALUATE (ground truth check)
     → "Body-need fulfilled chưa?"
     → ĐỦ → prolactin release (Satisfaction Signal) → schema DỪNG
     → CHƯA ĐỦ → prolactin = 0 → schema TIẾP TỤC → loop ②-③

  ⑤ Imagine CALIBRATE (learn từ body feedback)
     → Body nói "tốt!" → imagine: "predict ĐÚNG → tăng confidence cho scenario này"
     → Body nói "không!" → imagine: "predict SAI → giảm confidence → thử khác"
     → = Imagine NGÀY CÀNG chính xác qua mỗi cycle body feedback
     → = "Kinh nghiệm" = imagine ĐÃ calibrate bởi NHIỀU body feedbacks

LUỒNG ĐƠN GIẢN HÓA:
  Body cần → Imagine predict (dopamine) → Thực hiện → Body confirm (prolactin) → Imagine learn
       ↑                                                                              ↓
       └──────────────────── body-need MỚI hoặc CÒN ←────────────────────────────────┘
```

---

## 6. So Sánh Trực Tiếp: AlphaGo vs Con Người

```
                        AlphaGo                 CON NGƯỜI
─────────────────────────────────────────────────────────────
Predict system          Value Network           Imagine (PFC + vô thức)
Predict signal          Number (win %)          Dopamine (body sẽ TỐT?)
Drive                   Policy Network select   Schema-Drive execute
Reality test            Đi nước → kết quả       Hành vi → body nhận
Evaluate result         Win/Lose (binary)       Prolactin (đủ/chưa — gradient)
Learn/Update            Gradient descent         Schema update + imagine calibrate
"Đủ rồi" (stop)        Programmer set           Prolactin (Satisfaction Signal)
Body                    ❌ KHÔNG CÓ             ✅ Lớp 1 opioid/oxytocin
Desire                  ❌ Objective function    ✅ Body-need (6 nhóm)
Multi-objective         ❌ 1 loss                ✅ Nhiều schemas conflict
Modality                ❌ 1 (numbers)           ✅ 6 modalities
─────────────────────────────────────────────────────────────
RPE đủ giải thích?      ✅ 100%                  🔴 ~30% (chỉ simple cases)

→ AlphaGo = Hệ thống 1 ONLY (predict + learn)
→ Con người = Hệ thống 1 (imagine predict) + Hệ thống 2 (body confirm)
→ RPE mô tả Hệ thống 1 → ĐÚNG
→ RPE MISS Hệ thống 2 → vì AI KHÔNG CÓ body
→ → RPE = đúng cho CƠ CHẾ dopamine neuron
→ → RPE = KHÔNG ĐỦ cho TOÀN BỘ human reward system
```

---

## 7. 3 Trạng Thái — Theo 2 Hệ Thống

```
TRẠNG THÁI 1: HEALTHY (imagine + body CÙNG hướng)
  Imagine predict: "cái này tốt cho body" → dopamine → drive
  Reality: body THẬT SỰ tốt → opioid/oxytocin + prolactin
  → Imagine CONFIRM → calibrate TỐT → predict CHÍNH XÁC HƠN
  → = "Làm cái mình thích VÀ body cũng thích" → sustainable
  Ví dụ: ăn ngon (imagine "ngon!" + body "ngon thật!") ✅

TRẠNG THÁI 2: NGHIỆN (imagine CHẠY, body KHÔNG reward)
  Imagine predict: "scroll thêm → sẽ hay!" → dopamine → drive
  Reality: body KHÔNG nhận gì thật → opioid = 0 → prolactin = 0
  → Imagine KHÔNG ĐƯỢC calibrate (không có body feedback RÕ)
  → Dopamine loop TỰ DUY TRÌ → body TRỐNG → "dừng → trống rỗng"
  → = "Imagine nói sẽ sướng → body nói KHÔNG có gì" → mismatch
  Ví dụ: scroll MXH (imagine "hay!" + body "...") ❌

TRẠNG THÁI 3: THIỀN SƯ (body DOMINANT, imagine QUIET)
  Imagine: GIẢM predict (không chase novelty) → dopamine THẤP
  Body: CẢM NHẬN trực tiếp (opioid/oxytocin từ hiện tại) → prolactin RÕ
  → Prolactin KHÔNG bị dopamine lấn → body NÓI "đủ" → NGHE ĐƯỢC
  → = "Không predict tương lai → CẢM NHẬN hiện tại → bình an"
  → = "Bình yên" = prolactin audible (không bị dopamine lấn)
  Ví dụ: ngồi uống trà (không imagine gì → body feel trà ấm → đủ → peace) ✅
```

---

## 8. Ứng Dụng — Predict Hành Vi

```
BIẾT 2 hệ thống → predict ĐÚNG HƠN:

  "Tại sao scroll mãi?" → Hệ thống 1 (imagine) chạy + Hệ thống 2 (body) = 0
    → Fix: body CẦN reward THẬT (gặp người, ăn ngon) → thay scroll

  "Tại sao biết sai vẫn làm?" → Hệ thống 1 predict "sẽ tốt" + Hệ thống 2 CHƯA feedback
    → Fix: TẠO body feedback sớm (thử nhỏ → body nói "ok" hoặc "không")

  "Tại sao chán dù có đủ?" → Hệ thống 2 prolactin BỊ LẤN bởi dopamine imagine
    → Fix: GIẢM dopamine noise → prolactin nổi lên → cảm nhận "đủ"

  "Tại sao thiền giúp?" → GIẢM Hệ thống 1 (imagine quiet) → Hệ thống 2 NGHE ĐƯỢC
    → = Train body awareness → prolactin audible → satisfaction THẬT
```

---

## 9. Evidence — Body THẬT SỰ Respond Với Imagination

> 2 hệ thống KHÔNG tách biệt — Imagine CÓ tương tác body THẬT.

### 9.1 Research Chứng Minh Body Respond Với Tưởng Tượng

```
5 LĨNH VỰC research PROVEN:

① Sexual imagination → body arousal ĐO ĐƯỢC:
  → Tưởng tượng sex → genital arousal THẬT (plethysmograph đo)
  → Heart rate TĂNG, blood pressure TĂNG, pupil DILATE
  → Body KHÔNG phân biệt imagine vs real ở mức autonomic
  → Research: Stock & Geer (1982), Laan & Everaerd (1995) 🟢

② Fear imagination → cortisol + stress response THẬT:
  → Tưởng tượng nhện (phobia) → body respond NHƯ thấy nhện thật
  → PTSD flashback: tưởng tượng trauma → cortisol spike + freeze THẬT
  → Body treat flashback NHƯ ĐANG XẢY RA
  → Research: Pitman et al. (1987), Shin & Liberzon (2010) 🟢

③ Food imagination → body CHUẨN BỊ ĐỒ ĂN:
  → Tưởng tượng chanh → nước miếng CHẢY (đo được)
  → Insulin CÓ THỂ tăng nhẹ (cephalic phase insulin response)
  → Body chuẩn bị ĐÓN THỨC ĂN dù CHƯA ăn
  → Research: Morewedge et al. (2010), Power & Schulkin (2009) 🟢

④ Motor imagination → cơ ACTIVATE NHẸ:
  → Tưởng tượng ném bóng → EMG detect: cơ tay ACTIVATE nhẹ
  → Ranganathan et al. (2004): tưởng tượng tập cơ 12 tuần
    → SỨC MẠNH TĂNG 35% (KHÔNG tập thật, CHỈ tưởng tượng!)
  → Motor cortex fire khi imagine → cơ respond → dù PFC brake output
  → Research: Yue & Cole (1992), Ranganathan et al. (2004) 🟢

⑤ Placebo = imagination → body HEAL THẬT:
  → Thuốc giả + bệnh nhân TIN → body respond: đau GIẢM, bệnh CẢI THIỆN
  → Opioid system FIRE khi placebo (body TỰ produce painkiller)
  → Imagination "sẽ khỏi" → body chemistry THAY ĐỔI THẬT
  → Research: Wager et al. (2004), Benedetti (2008) 🟢
```

### 9.2 Fidelity — Imagine Bao Nhiêu % So Với Thật

```
  Real experience:     body respond 100%
  Vivid imagination:   body respond ~20-60% (tùy modality + training)
  Vague imagination:   body respond ~5-15%
  No imagination:      body respond 0%

  THEO MODALITY:
    Emotional imagine: ~50-80% (MẠNH NHẤT — Amygdala KHÔNG phân biệt imagine vs real)
    Somatic imagine:   ~40-70% (mạnh nếu vmPFC mạnh)
    Visual imagine:    ~30-50%
    Motor imagine:     ~20-40%

  → Emotional scenarios → body respond GẦN NHƯ THẬT
  → Tại sao WORRY = body damage THẬT: imagine xấu × lặp lại = cortisol MÃN TÍNH
  → Tại sao VISUALIZATION = body benefit THẬT: imagine tốt × lặp = body prep
```

### 9.3 Implications Cho Reward Dual System

```
LUỒNG ĐẦY ĐỦ (update):

  1. Schema mong muốn: "muốn X"
  2. Imagine simulate: "nếu có X → thế nào?"
  3. Body PREVIEW respond: X → body respond 20-60% fidelity ← EVIDENCE MỚI
  4. Dopamine evaluate preview: "body SẼ thích!" → fire → DRIVE
  5. Execute hành vi trong reality
  6. Body FULL respond: 100% fidelity
  7. Satisfaction Signal: "đủ chưa?" → đủ → dừng

  → Bước 3 = BODY THẬT SỰ tham gia IMAGINE → không chỉ "trong đầu"
  → Body "nếm thử" (preview 20-60%) → decide → rồi "ăn thật" (reality 100%)
  → Imagine KHÔNG tách biệt body → imagine DÙNG body để evaluate

VÀ: 3 cách DÙNG imagination → body:

  WORRY (hại): imagine xấu → body respond cortisol THẬT → damage
    = "Tự đánh mình bằng tưởng tượng" → body KHÔNG biết là giả

  VISUALIZATION (lợi): imagine tốt → body respond opioid/motor prep → benefit
    = "Tự luyện bằng tưởng tượng" → body THẬT SỰ prep/compile

  DAYDREAM (mixed): imagine tự do → body respond tùy nội dung → mixed
    = "Brain explore tự do" → có thể tốt (creative) hoặc tệ (worry)

  → CÙNG mechanism → KHÁC hướng → KHÁC kết quả
  → Ai KIỂM SOÁT hướng imagination → dùng body response CÓ LỢI
  → Ai KHÔNG kiểm soát → imagination dùng NGƯỢC (worry loop)
  → Chi tiết: Body-Listening.md (cách kiểm soát) + Imagination-Analysis.md (cách hoạt động)
```

---

## 10. Giới Hạn + Honest Assessment (cập nhật)

```
ĐÃ CÓ CƠ SỞ (từ research):
  🟢 Dopamine = prediction signal (Schultz 1997) — proven
  🟢 Prolactin = satiation signal (Krüger 2003, Exton 2001) — proven
  🟢 Dopamine suppress prolactin (Ben-Jonathan 2001) — proven
  🟢 Partnered > solo prolactin (Brody 2006) — proven
  🟢 RPE = AI (TD Learning) — proven + operational

SUY LUẬN CỦA FRAMEWORK (chưa proven):
  🔴 "2 hệ thống song song" — suy luận, chưa ai frame CHÍNH XÁC như vậy
  🔴 "Dopamine = imagine predict improvement" — reframe RPE, chưa validated
  🔴 "Prolactin = Satisfaction Signal cho MỌI body-need" — extrapolate từ sex/food
  🔴 "Thiền = train nghe prolactin" — suy luận, chưa ai test trực tiếp
  🔴 "Scroll MXH = imagine loop, body = 0" — suy luận, consistent nhưng chưa measured
  🔴 "3 trạng thái (healthy/nghiện/thiền)" — framework classification, chưa validated

CÁCH XÁC THỰC:
  → fMRI: đo dopamine VÀ prolactin ĐỒNG THỜI trong cùng task → thấy 2 hệ thống?
  → Meditation study: đo prolactin sensitivity TRƯỚC/SAU meditation training?
  → MXH study: đo prolactin khi scroll vs khi gặp bạn → khác?
  → Block prolactin: behavior THAY ĐỔI gì ở non-sexual tasks?
  → → Tất cả TESTABLE → nhưng CHƯA AI test theo framework này
```

---

## 11. Câu Hỏi Mở (cập nhật)

```
RDS-1: Imagine system nằm Ở ĐÂU chính xác trong não?
  → PFC workspace? DMN? Hippocampus replay? Tất cả combine?
  → Có thể: DISTRIBUTED (không 1 vùng) → khó đo

RDS-2: Dopamine fire dựa trên imagine predict CỤ THỂ thế nào?
  → Imagine "tốt hơn" = vô thức evaluate → nhưng HOW?
  → Body PREVIEW (somatic markers — Damasio) → có thể = mechanism

RDS-3: Prolactin sensitivity có TRAIN được không?
  → Meditation → prolactin sensitivity TĂNG? → testable
  → Exercise → prolactin sensitivity THAY ĐỔI? → testable

RDS-4: "Prediction Improvement" có chính xác hơn "Prediction Error" thật không?
  → Cần: experiment TÁCH "error" vs "improvement" → 2 predict KHÁC nhau → test
  → Nếu improvement predict ĐÚNG HƠN error → PI > PE confirmed

RDS-5: Tại sao AI (không có body) VẪN hoạt động tốt chỉ với RPE?
  → Vì: AI KHÔNG CẦN body confirm → objective function = programmer set "body"
  → AI loss function = PROXY cho body → programmer = "thay body"
  → Con người: body = REAL → không cần programmer → TỰ evaluate
  → → AI + RPE work vì: programmer THAY body. Người + RPE miss vì: body TỰ LÀM.
```

---

> *Reward Dual System — DRAFT*
> *"Dopamine = imagine predict tốt hơn. Prolactin = body confirm đủ rồi."*
> *2 hệ thống song song. RPE mô tả hệ thống 1. Framework thêm hệ thống 2.*
> *Suy luận — cần xác thực.*
