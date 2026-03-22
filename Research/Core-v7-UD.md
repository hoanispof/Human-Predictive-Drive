# Human Predictive Drive — Framework v7.0 UD-Centric DRAFT

> **Trạng thái:** DRAFT — phiên bản UD-centric, song song với Core-v7-Draft-Good.md (PE-centric)
> **Ngày:** 2026-03-15
> **Khác biệt với PE-centric:**
> - Nguyên lý cốt lõi: "Não = máy mong muốn" thay vì "Não = máy dự đoán"
> - PE (Prediction Error) → UD (Underlying Drive — drive NẰM DƯỚI mọi hành vi, mọi depth)
> - UD KHÔNG binary (conscious/unconscious) → GRADIENT theo schema depth + modality
> - Prediction VẪN CÓ nhưng PHỤC VỤ desire, không phải mục đích tự thân
> - Dopamine = desire fulfillment signal, không phải surprise signal
>
> **⚠️ UD là GIẢ THIẾT — chưa validated.**
> File này tồn tại SONG SONG với PE-centric để so sánh.
> Chi tiết giả thiết UD: Research/UD-Hypothesis.md
>
> **🔄 ĐỔI TÊN TRONG v8.0:**
> "UD" (Underlying Drive) sẽ đổi thành **"Schema-Drive"** trong phiên bản v8.0.
> Lý do: Schema-Drive CHÍNH XÁC hơn — mọi drive ĐỀU từ schema (không phải PFC, không phải "unconscious").
> Schema mạnh = drive mạnh. Schema xung đột = drive xung đột. PFC chỉ brake/workspace/translate.
> Hiện tại giữ "UD" trong draft → v8.0 sẽ search-replace + rename + review consistency 1 lần.
>
> **Nguyên tắc:** Công thức, không đáp án. Mô hình, không dogma.
> **Quy ước:** 🟢 Nghiên cứu vững | 🟡 Suy luận có cơ sở | 🔴 Giả thuyết

---

## 1. Tổng Quan

Framework mô tả **CƠ CHẾ** tạo động lực và hành vi con người.

**Nguyên lý cốt lõi (UD-centric):**

```
CŨ (PE): Não = máy dự đoán. Predict → Error → Update.
  → SAI ở chỗ: thông tin MỚI bất kỳ ≠ reward
  → "Nước sôi 100°C" = mới → nhưng body: KHÔNG GÌ (nếu không cần biết)

MỚI (Schema-Drive): Schema phát hiện body CẦN gì → MONG MUỐN cụ thể → DRIVE hành vi đáp ứng.

  Schema = model thế giới, LIÊN TỤC tính toán (vô thức)
  → Schema tự phát hiện: "body CẦN gì / MUỐN gì lúc này?"
  → Output = MONG MUỐN CỤ THỂ (không mơ hồ, không static)
  → Mong muốn = NGUỒN GỐC mọi drive, mọi hành vi
  → Có thể là: giải quyết vấn đề, tìm trải nghiệm, kết nối, hiểu biết, hoàn thiện,...

  Luồng:
  → Schema phát hiện mong muốn → brain DRIVE tìm cách đáp ứng
  → PFC phục vụ: giả lập (preview) HOẶC hành động thực tế
  → Kết quả → body evaluate: "đáp ứng ĐÚNG mong muốn không?"
    → ĐÚNG → body reward (opioid/oxytocin) → mong muốn fulfilled → sướng
    → KHÔNG ĐÚNG → body ignore hoặc reject → thử cách khác → loop
    → GẦN ĐÚNG → dopamine signal "gần rồi, tiếp tục!"
    → KHÔNG LIÊN QUAN → body ignore hoàn toàn (dù info MỚI 100%)

  → "Sướng" KHÔNG đến từ thông tin MỚI → đến từ thông tin ĐÁP ỨNG mong muốn schema
  → Info + schema đang muốn = reward. Info + schema không muốn = zero.
  → "Đồng bộ" = TẤT CẢ schemas KHÔNG CÒN mong muốn xung đột = bình an

  Prediction VẪN CÓ — nhưng prediction PHỤC VỤ tìm cách đáp ứng:
  → Predict chính xác = tìm cách đáp ứng mong muốn NHANH hơn
  → Predict sai = đáp ứng SAI = body reject = update prediction
  → Learning = cải thiện prediction để ĐÁP ỨNG mong muốn HIỆU QUẢ hơn

  VÒNG PHẢN HỒI 2 CHIỀU (Schema ↔ Body Feedback Loop):
  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  Body-need ──→ Schema DRIVE hành vi ──→ Body trải nghiệm   │
  │      ↑                                        │             │
  │      │          Body đánh giá: "đủ chưa?"     ↓             │
  │      │                                        │             │
  │      └──── Satisfaction Signal ←── Body xác nhận "đủ"       │
  │            (body báo schema dừng)                            │
  │                                                             │
  │  → Schema-Drive mới nổi lên → loop tiếp                    │
  └─────────────────────────────────────────────────────────────┘

  ASYMMETRY quan trọng:
    DRIVE:    Schema → Body  (schema ĐIỀU KHIỂN body — phức tạp, nhiều kênh)
    SATISFY:  Body → Schema  (body BÁO schema đủ rồi — đơn giản, 1 signal)

    Chiều DRIVE (Schema → Body) = phức tạp:
      Schema "muốn X" → kéo ĐỒNG THỜI nhiều hệ thống:
        Hormone (cortisol, dopamine, NE → urgency + motivation)
        Motor (plan + thực hiện chuyển động)
        Attention (visual/auditory shift tới target)
        Memory (recall thông tin liên quan)
        PFC (plan strategy, simulate options)
        Autonomic (nhịp tim, tiêu hóa, hô hấp adjust)
      → Giống KÉO DÂY CON RỐI — nhiều dây cùng lúc, mỗi dây 1 hệ thống
      → KHÔNG phải 1 tín hiệu → mà là ORCHESTRATION phức tạp

    Chiều SATISFY (Body → Schema) = đơn giản hơn:
      Body xác nhận "đủ" → release signal (prolactin candidate)
      → 1 MESSAGE rõ: "dừng"
      → Schema nhận → drive GIẢM → hành vi dừng

    → 2 chiều NGƯỢC NHAU, 2 NGUỒN KHÁC NHAU, 2 ĐỘ PHỨC TẠP KHÁC NHAU
    → Schema KHÔNG TỰ biết đủ — phải CHỜ body báo (signal đơn giản)
    → Body KHÔNG TỰ drive — phải CHỜ schema điều khiển (orchestration phức tạp)
    → KHÔNG chiều nào tự đủ — cả hai PHỤ THUỘC lẫn nhau
    → Đây là lý do giữ tên "Satisfaction Signal" (body phát, đơn giản)
      thay vì "Schema-Satisfaction" (sai nguồn phát)

  SHORTHAND:
    Drive ↔ Satisfy = 2 chiều của loop
    Drive   = gọn cho Schema-Drive         (schema → body, phức tạp)
    Satisfy = gọn cho Satisfaction Signal   (body → schema, đơn giản)
    → Dùng shorthand khi nói về LOOP, overview
    → Dùng tên đầy đủ khi PHÂN TÍCH cơ chế chi tiết
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
    Serotonin = AMPLIFIER (Status Position — "cửa" mở/đóng cho schemas)
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
║  │  ┌─ Hardware Parameter ─────────────────────────────────┐   │  ║
║  │  │ WM Capacity (workspace size, fixed, đo được)         │  │  ║
║  │  │ PFC Activation Level (dynamic state: sleep/stress/..)│  │  ║
║  │  │ Emergent: Threshold · Baseline Drive · Decay Rate    │  │  ║
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

"Chán" decompose thành 5 loại (KHÁC nhau → KHÁC xử lý):
  Type A — Fulfilled Done:   mong muốn ĐÃ ĐÁP ỨNG đủ → body satisfied → move on tự nhiên
    Ví dụ: biết nước sôi 100°C → xong → tìm cái mới
    Cảm giác: nhẹ nhàng, "ok xong". FIX: không cần — lành mạnh ✅

  Type B — Over-Fulfilled:   body ĐÃ ĐỦ nhưng BỊ ÉP thêm → body PHẢN ĐỐI
    Ví dụ: ăn no rồi mà ép ăn tiếp → buồn nôn. Nghe bài chán mà lặp → stress.
    Cảm giác: khó chịu, muốn DỪNG. FIX: DỪNG + REST + nghe body nói "đủ"

  Type C — Hijacked Empty:   dopamine (Lớp 2) chạy mà opioid (Lớp 1) = 0 → TRỐNG RỖNG
    Ví dụ: scroll MXH 2 tiếng → dừng → "mình vừa làm gì?" → trống
    Cảm giác: trống rỗng, hối hận. FIX: thay dopamine loop bằng Lớp 1 thật
    → Chi tiết: Addiction-Analysis.md

  Type D — Stagnant Restless: body CÒN MUỐN nhưng domain KHÔNG CÒN gì mới → bức bối
    Ví dụ: expert ĐÃ biết gần hết → "muốn cái gì mới mà không biết cái gì"
    Cảm giác: bức bối, restless. FIX: explore domain MỚI hoặc đào SÂU hơn

  Type E — Suppressed:       desire CÓ nhưng bị SCHEMA khác ÉP IM → mệt ngầm
    Ví dụ: muốn sáng tạo nhưng schema "phải productive" suppress → mệt mà không biết tại sao
    Cảm giác: mệt mãn tính, "chán" mà không rõ chán CÁI GÌ. FIX: nhận diện desire bị suppress

  → PE cũ: cả 5 = "PE=0" → cùng label → SAI treatment
  → Framework: 5 loại KHÁC → 5 treatments KHÁC → chính xác hơn

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
║                                                      ║
║  ⚠️ 2 cách nhìn body CẦN gì (bổ sung, không trùng): ║
║  Layer1-Channels.md: 10 sub-channels CHI TIẾT         ║
║    = Góc HARDWARE: Opioid (E1-E5) + Oxytocin (C1-C5) ║
║    = "Body reward CHÍNH XÁC từ channel NÀO?"          ║
║  Body-Needs.md: 6 nhóm nhu cầu TỔNG QUÁT             ║
║    = Góc ỨNG DỤNG: Basics + Connection + Experience    ║
║      + Progress + Meaning + Regulation                 ║
║    = "Cuộc sống CẦN gì tổng thể?"                     ║
║  → Layer1 = zoom in Lớp 1 (2 kênh → 10 sub-channels)  ║
║  → Body-Needs = zoom out (Lớp 1 + Lớp 2 + meta → 6)   ║
╠══════════════════════════════════════════════════════╣
║  LỚP 2: AMPLIFIER — "Signal + khuếch đại"           ║
║                                                      ║
║  NOVELTY (dopamine)        STATUS POSITION (serotonin)║
║  "Desire matched!"         "Tôi ở vị trí NÀY"       ║
║  Detect + signal           Amplify MỌI channel       ║
║  Mở rộng tìm kiếm         Mở/đóng "cửa" cho schemas ║
║                                                      ║
║  Status = 2 THAM SỐ (tách):                          ║
║    Position (serotonin): "đang ở đâu" → AMPLIFY      ║
║      → Cao: nhiều schemas "dám" drive → hành vi RỘNG ║
║      → Thấp: ít schemas "dám" → hành vi HẠN CHẾ     ║
║    Aspiration (schema): "muốn ở đâu" → DRIVE         ║
║      → Gap = Aspiration − Position → drive chase      ║
║      → Gap=0: content. Gap>0: chase. Gap<0: imposter  ║
║      → Aspiration NẰM TRONG Schema-Drive (không riêng)║
║    → Chi tiết: Status-Analysis.md                     ║
║                                                      ║
║  Dopamine = IMAGINE PREDICT SIGNAL + NHIÊN LIỆU SÁNG TẠO:║
║    Fire khi imagine predict "TỐT HƠN cho body"       ║
║    Suppress khi predict "TỆ HƠN"                     ║
║    = Hệ thống 1 (IMAGINE) trong Reward Dual System:  ║
║      Imagine predict → dopamine → DRIVE hành vi       ║
║      → Reality → Body confirm (Satisfaction Signal = Hệ thống 2)║
║      → Body feedback → imagine CALIBRATE → chính xác ║
║    BUILD schema: explore, learn, connect, imagine     ║
║    ≠ "surprise signal" (RPE)                          ║
║    ≠ "desire fulfillment signal" (UD cũ — chưa đủ)   ║
║    = "prediction improvement signal" (Reward Dual)    ║
║    → Chi tiết: Reward-Dual-System.md                  ║
║                                                      ║
║  ⚠️ Dopamine + Cortisol BỔ SUNG nhau:                ║
║    Dopamine = BUILD schema (sáng tạo, học, explore)   ║
║    Cortisol = EXECUTE schema (triển khai hành vi thật)║
║    Chỉ Dopamine: "nghĩ hay nhưng chả làm"            ║
║    Chỉ Cortisol: "làm cật lực nhưng không sáng tạo"  ║
║    Cả 2 vừa đủ: "nghĩ hay VÀ làm thật" = productive ║
║                                                      ║
║  ⚠️ Novelty:                                         ║
║    Framework TREAT as channel (predictive power)      ║
║    Bản chất: có thể là infrastructure                 ║
║    Test: Novelty → cảm xúc GÌ? → luôn opioid/oxy    ║
║    → Xem UD-Hypothesis.md §Q-NEW-7                   ║
╠══════════════════════════════════════════════════════╣
║  LỚP 3: MODULATOR — "Fine-tuning"                   ║
║                                                      ║
║  Cortisol = "NHIÊN LIỆU kích hoạt schema triển khai":║
║    Vừa đủ: schema KÍCH HOẠT + PFC VẪN available      ║
║            = productive (vừa drive vừa có trọng tài)  ║
║    Quá thấp: schema KHÔNG có động lực triển khai      ║
║              = stagnant (biết nhưng không làm)        ║
║    Quá cao: PFC BỊ SỤP + schema mạnh nhất AUTO-WIN   ║
║             = burnout (làm mà không hiệu quả)        ║
║    → Sweet spot: Yerkes-Dodson (vừa đủ áp lực)       ║
║    → Chi tiết: Drive-Optimization.md §9 (3 Layers)   ║
║                                                      ║
║  NE = "spotlight attention":                          ║
║    Tăng → focus HẸP + SÂU vào schema đang active     ║
║    Không chọn schema → AMPLIFY schema đang dominant   ║
║    + Cortisol: focus + urgent = "cày xuyên đêm"      ║
║    − Cortisol: focus + bình tĩnh = flow state        ║
║                                                      ║
║  Vasopressin = "lính gác bảo vệ bond":               ║
║    Oxytocin TẠO connection → Vasopressin BẢO VỆ      ║
║    Ai đe dọa bond → vasopressin → defensive/aggress  ║
║    Ghen tuông, territorial, protective = vasopressin  ║
║    Hardware: AVPR1A gene → sensitivity khác per person ║
║                                                      ║
║  "Satisfaction Signal" = cơ chế body báo "ĐỦ RỒI":   ║
║    Desire fulfill → body release signal → "đủ rồi"   ║
║    ⚠️ Prolactin = candidate CHÍNH (proven: sex, food) ║
║    ⚠️ Có thể CÒN hormone khác tham gia (chưa biết hết)║
║    ⚠️ Framework bind CHỨC NĂNG (báo đủ), KHÔNG bind   ║
║       1 hormone → đúng bất kể hormone nào thực hiện   ║
║    = TRIGGER chuyển GĐ3(Sướng) → GĐ4(Ok) trong cycle ║
║    Multi-channel fulfill (E+C): signal MẠNH → dừng DỄ ║
║    Single dopamine loop: signal YẾU → khó dừng       ║
║    Addiction = Satisfaction Signal BỊ BYPASS → "không dừng"║
║    Hardware (~50%) + Context (~50%)                   ║
║                                                      ║
║  Endocannabinoid = "giảm xóc body":                  ║
║    DAMPEN negative signals (cortisol, pain)           ║
║    Exercise → endo-CB release → "runner's high"       ║
║    Stress buffer: giảm impact → body SMOOTH hơn       ║
║    Thiếu exercise → endo-CB thấp → mọi stress MẠNH hơn║
║    → Tại sao tập thể dục = NỀN TẢNG: maintain shock absorber║
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

  ⚠️ Threshold: xem EMERGENT METRICS bên dưới (không phải parameter cố định)
    → Threshold = per domain, emergent từ schema profile
    → Chi tiết: Research/Threshold-Analysis.md

  ⚠️ UD Sensitivity (v6 cũ: 4 sub-parameters) — TẤT CẢ ĐÃ BỎ:
    ① Amplitude → BỎ: = emergent (xem "Cường Độ Phản Ứng" bên dưới)
    ② Precision → BỎ: = emergent từ schema quality × conflict level × PFC state
    ③ Decay Rate → BỎ: = emergent (xem "Tốc Độ Quen" bên dưới)
    ④ Generalization → BỎ: = spreading activation mechanism, implicit trong schema
    → UD Sensitivity KHÔNG còn là parameter category
    → Mỗi "sub" = emergent từ components KHÁC đã có trong framework

EMERGENT METRICS — Observable, KHÔNG set trực tiếp, thay đổi INPUTS → metrics tự đổi:

  Threshold → v8: "Satisfaction Threshold" — "dễ thỏa mãn hay khó thỏa mãn?"
    = DYNAMIC per (person × domain × mục tiêu × thời điểm)
    = KHÔNG phải 1 số — là EMERGENT từ nhiều thành phần:
      Satisfaction Signal capacity: hardware "báo đủ" dễ fire hay khó (Neurochemistry Lớp 3)
      Schema suppress: "thôi kệ" defense → ÉP đủ dù body CHƯA đủ (Schema-Atlas §6.3)
      Schema drive: "phải đạt!" push → ÉP threshold lên (Schema-Drive)
      Pressure + Challenge: cortisol/dopamine → suppress/boost Satisfaction Signal
      Channel count: multi-channel → signal dễ fire → threshold GIẢM tạm
      Body baseline carry: hormone nền MANG THEO khi switch context
    = "Dễ thỏa mãn" CÓ THỂ: Satisfaction Signal đủ thật ✅ HOẶC schema chặn desire ❌
    = "Khó thỏa mãn" CÓ THỂ: signal khó fire ✅ HOẶC schema push quá ❌
    = → Phân biệt: "đủ thật" vs "ép đủ" → xem Schema-Diagnostic.md
    → Chi tiết: Research/Threshold-Analysis.md

    ⚠️ V8.0: CÂN NHẮC bỏ "Threshold" như tên tham số riêng
    → Vì: emergent từ quá nhiều thành phần → không đo được → gây hiểu lầm "1 số"
    → THAY BẰNG: mô tả trực tiếp thành phần (Satisfaction Signal + schema + pressure/challenge)
    → Giống: Amplitude, Precision ĐÃ BỎ vì emergent → Threshold CŨNG emergent

  Baseline Drive — mức drive nền
    = f(Threshold × Schema × Environment) — KẾT QUẢ, không phải INPUT
    UD deficit kéo dài → baseline GIẢM → apathy
    UD surplus → baseline TĂNG → bồn chồn
    "Chán" = desire hiện tại < threshold

  Schema Ceiling — phức tạp tối đa có thể xây
    = f(WM × knowledge × time × domain) — KẾT QUẢ, không phải INPUT
    Thay đổi WM (khó), knowledge (học), time (kinh nghiệm) → ceiling tự đổi

  ⚠️ HAI METRIC MỌI NGƯỜI HAY HỎI (emergent, KHÔNG phải parameter đơn):

  "Cường Độ Phản Ứng" (tên cũ: Amplitude)
    = "Cùng stimulus, tại sao NGƯỜI NÀY react mạnh hơn NGƯỜI KIA?"
    = EMERGENT từ NHIỀU yếu tố đồng thời:
      → Hardware receptor: DRD4 variant → receptor nhạy/kém nhạy (PFC-Analysis §8)
      → Schema depth: schema SÂU match → reward MẠNH (Modality-Analysis §3)
      → Schema relevance: stimulus ĐÚNG mong muốn schema → reward MẠNH
      → Body state: cortisol thấp (relaxed) → PFC available → feel RÕ
    → KHÔNG có 1 số đại diện → phải xem TẤT CẢ yếu tố cùng lúc
    → Ước lượng: quan sát reactions across nhiều situations → pattern → estimate

  "Tốc Độ Quen" (tên cũ: Decay Rate)
    = "Tại sao NGƯỜI NÀY chán nhanh hơn NGƯỜI KIA?"
    = Tốc độ chuyển GĐ3(Sướng) → GĐ4(Ok) → GĐ5(Chán) trong 5 giai đoạn cycle (§5.2)
    = EMERGENT từ NHIỀU yếu tố:
      → Hardware receptor: COMT Val/Val → dopamine clear NHANH → chán nhanh (PFC-Analysis §8)
      → Hardware enzyme: MAO-A high → dopamine+serotonin clear NHANH → reward shorter
      → Modality count: chunk encoded nhiều modality → quen CHẬM (nhiều chỗ chưa "done")
      → Schema importance: schema SÂU → mong muốn LỚN → fulfill LÂU → quen CHẬM
      → Context novelty: context MỚI → cycle RESET (dù cùng schema)
    → KHÔNG có 1 số đại diện → phải xem hardware + schema + context
    → Ước lượng: quan sát bao lâu từ "thích" → "ok" → "chán" per domain
    → "Chán nhanh" = HARDWARE VARIANT (gen), KHÔNG phải "lỗi" (PFC-Analysis §8)

  → Cả 2 metric trên = OBSERVABLE nhưng KHÔNG SET trực tiếp
  → Thay đổi inputs (fix schema, match environment, hardware = gen = khó đổi)
    → metrics TỰ thay đổi theo
```

### 4.3 Processing Infrastructure

```
PFC = DRAFT + TEST + ROUTE + BRAKE + TRANSLATOR 🔴
  → 🔴 HYPOTHESIS (working model) — mỗi component có evidence riêng 🟢,
    nhưng narrative tổng thể chưa proven. Xem PFC-Analysis.md §7 cho 5 kịch bản + tests.
  → PFC KHÔNG compute from scratch → PFC DRAFT + HỎI vùng chuyên gia + ROUTE kết quả
  → Vô thức + vùng chuyên gia: compute per expertise → GỬI feedback về PFC
  → PFC tổng hợp feedback → route (pass/fail) + brake + translate
  → Body (opioid/oxytocin) = người ĐÁNH GIÁ cuối cùng (ground truth)
  → Chi tiết: Research/PFC-Analysis.md

  PFC = 5 FUNCTIONS:

  ① DRAFT — Tạo schema tạm (nhanh, thô, linh hoạt)
    → PFC neurons "mixed selectivity" → tái cấu trúc CỰC NHANH
    → Tạo pattern TẠM trong workspace → "sketch" → chưa hoàn chỉnh
    → Tại sao nhanh: 1 PFC neuron respond NHIỀU thứ cùng lúc → linh hoạt
    → Tại sao thô: WM limited (4±1) → sketch, không painting
    → Discard DỄ: mixed selectivity → reset nhanh → thử draft KHÁC

  ② TEST — Gửi draft cho vùng chuyên gia evaluate
    → Draft → gửi Amygdala ("nguy hiểm?") + Body/Insula ("body thích?")
      + Temporal ("match knowledge?") + BG ("match habit?")
    → Các vùng CHUYÊN GIA compute per expertise → GỬI feedback về PFC
    → PFC KHÔNG compute → PFC HỎI + nhận feedback + tổng hợp

  ③ ROUTE — Quyết định pass/fail → compile hoặc discard
    → Feedback tốt: draft pass → compile DẦN xuống BG/Temporal (sâu hơn)
    → Feedback xấu: draft fail → discard → thử draft KHÁC
    → Lặp: draft → test → pass → compile → RỜI PFC → vùng sâu TỰ chạy → PFC freed
    → = "Học" = draft nhiều lần → compile → "không nghĩ nữa" = schema đã rời PFC

  ④ BRAKE — Chặn output schema không phù hợp (VETO)
    → Schemas fire TỰ ĐỘNG (~50ms) → body ĐÃ bắt đầu react
    → PFC nhận SAU (~200-500ms) → CHẶN hành vi TIẾP THEO nếu cần
    → KHÔNG tắt schema (schema VẪN chạy bên trong) → chỉ chặn OUTPUT
    → = Trẻ chờ marshmallow = brake ĐỦ. Trẻ ăn ngay = brake CHƯA đủ.
    → = "Kiềm chế" = brake LIÊN TỤC body đã activated → TỐN energy → MỆT
    → KHÔNG CÓ schema predict hậu quả → brake KHÔNG biết chặn gì
      → Trẻ đánh nhau = THIẾU schemas hậu quả, không phải PFC yếu

  ③ TRANSLATOR — Dịch kết quả vô thức thành ngôn ngữ (post-hoc)
    → Vô thức quyết định → PFC NHẬN → dịch thành lời giải thích
    → "Tại sao tôi làm vậy?" = PFC TẠO lý do SAU KHI vô thức đã chọn
    → Lý do có thể ĐÚNG hoặc SAI (post-hoc rationalization — Gazzaniga)
    → Trẻ 3-4: chain 160+ strategies nhưng KHÔNG verbalize → translator chưa develop
    → Người lớn: chain + verbalize → TƯỞNG PFC tạo strategy → thực ra PFC chỉ dịch

  PFC KHÔNG làm (evidence):
    ❌ Tạo strategy (trẻ 3-4 tạo 160+ strategies mà PFC ~20% → vô thức tạo)
    ❌ Chain schemas (spreading activation tự động, không cần PFC)
    ❌ Evaluate (body evaluate qua somatic markers — Damasio)
    ❌ Khởi tạo hành vi (Libet: quyết định 350ms TRƯỚC PFC aware)
    ❌ Tắt schema (chặn OUTPUT, schema VẪN chạy → tốn energy đôi)

  ⚠️ "PFC tính toán" thực ra = gì?
    "Đấm → bị phạt → mất việc":
      → 3 schemas ĐÃ CÓ → spreading activation TỰ chain
      → PFC: HOLD workspace cho chain xảy ra + NHẬN kết quả cuối
      → PFC KHÔNG nối → associations TỰ nối → PFC chỉ GIỮA space + NHẬN
      → TRÔNG NHƯ "PFC tính toán" → thực ra "PFC mở phòng, vô thức họp"

  THỨ TỰ thực tế (Libet 1983):
    1. Schemas fire TỰ ĐỘNG (~50ms) → body BẮT ĐẦU react
       (tim đập, cortisol, muscle — TRƯỚC khi PFC biết)
    2. Vô thức chain associations → propose options
    3. PFC NHẬN signal (~200-500ms) → workspace hold options
    4. Body evaluate options (somatic markers → "cái nào feel right?")
    5. PFC: BRAKE output schema có body response âm
    6. Schema còn lại → execute → body nhận kết quả thật
    7. Body feedback → schema update → loop
    8. PFC: TRANSLATE ("tôi chọn vì...") → post-hoc rationalization

    → "Giữ bình tĩnh" KHÔNG phải "không phản ứng"
    → = Body ĐÃ phản ứng + PFC BRAKE hành vi tiếp + body DẦN hạ

  DUAL MODE (tùy schema maturity):
    Schema MỚI: PFC = WORKSPACE mode (hold space, effortful, conscious)
      → Vô thức compute trong workspace → PFC sustain → chậm, mệt
    Schema CŨ (compiled): PFC = BRAKE-ONLY mode (veto nếu cần, nhẹ)
      → Schema fire auto → PFC chỉ brake nếu bất thường → nhanh, nhẹ
    Học = chuyển từ WORKSPACE → BRAKE-ONLY (PFC freed dần)
    Expert = gần hết schemas ở BRAKE-ONLY → PFC gần rảnh

  Developmental evidence (hỗ trợ mạnh nhất):
    0-4 tuổi: PFC ~20% → VẪN chain 160+ strategies (vô thức) ✅
    4-7 tuổi: PFC ~40% → brake bắt đầu (marshmallow) + translator bắt đầu ✅
    7-12 tuổi: PFC ~60% → workspace mở → "trông như tính toán" ✅
    13-18 tuổi: PFC ~80% → workspace rộng nhưng body connection chưa đủ ✅
    25+: PFC ~100% → full workspace + brake + translator + body connected ✅

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

Modality Channels — NỀN TẢNG encoding cho chunks + schemas:

  2 LOẠI KHÁC BẢN CHẤT:

  5 Experience Modalities (encode TRẢI NGHIỆM — DATA gốc):
    Visual · Auditory · Somatic · Motor · Emotional
    → Mỗi vùng não xử lý 1 modality RIÊNG
    → Body cảm nhận → não lưu → DATA gốc cho mọi hiểu biết
    → MỌI sinh vật có thần kinh đều có (mức độ khác nhau)

  1 Communication Modality (encode LABELS — INDEX):
    Verbal / Gesture / Writing / Drawing / Video / ...
    → KHÔNG encode experience → encode REFERENCES tới experience
    → 3 functions: LABEL (compress chunk) + TRANSFER (share) + GHÉP (combine labels)
    → CHỈ NGƯỜI có ở mức phức tạp → EVOLUTIONARY ADVANTAGE
    → "Nghĩ bằng lời" = verbal NARRATE kết quả vô thức → KHÔNG phải verbal "nghĩ"

  1 chunk/schema có thể encoded ở NHIỀU modalities đồng thời
  Modality = NỀN TẢNG → Chunks build TRÊN modality → Schema build TRÊN chunks

  Modality Count = DEPTH (đo được):
    → 1 modality = SURFACE → dễ learn, dễ forget, dễ change
    → 5 experience modalities = DEEP → khó learn, khó forget, khó change
    → "Schema sâu" = LITERALLY encoded ở NHIỀU NƠI trong não + body
    → Communication labels = NÔNG (hướng đúng, fidelity thấp)
    → Experience encoding = SÂU (body respond thật, fidelity cao)

  Experience Modality Dominant = HƯỚNG TƯ DUY:
    → Somatic dominant → chain NGANG (pattern match, improviser)
    → Visual-spatial dominant → chain NGANG (structural match)
    → Motor dominant → chain DỌC (sequential skills)
    → Communication dominant → chain DỌC (verbal narrate sequential)
    → Mixed → T-shaped (sâu 1 + rộng vài)

  Implications cho UD:
    → Desire fulfilled ở 1 modality ≠ fulfilled ở tất cả
    → "Biết nhưng không làm được" = verbal label fixed, body experience chưa
    → Fix = fix ở ĐÚNG modality: CBT (verbal labels), Exposure (somatic+emotional), Practice (motor)
    → Match therapy modality với chunk modality profile → effective

→ Chi tiết modality: Research/Modality-Analysis.md
→ Chi tiết PFC: Research/PFC-Analysis.md
```

---

## 5. T2: Software — Schema Tạo Desire, PFC Serve Desire

### 5.1 Predictive-Chunks — Phục Vụ Desire

```
Chunks = đơn vị prediction. ENCODED trên modalities. Muôn hình vạn trạng.

UD reframe:
  Chunks KHÔNG tồn tại "vì prediction" — tồn tại vì SERVE DESIRE
  → Não build chunks ĐỂ fulfill desire hiệu quả hơn
  → Chunks chính xác = tìm fulfillment nhanh hơn
  → Chunks sai = tìm sai → UD âm → update chunks

Modality Profile — mỗi chunk có "bộ encoding" riêng:
  → Chunk đơn giản: 1-2 modalities (verbal: "nước sôi 100°C") → NÔNG, dễ sửa
  → Chunk phức tạp: 4-6 modalities (verbal+visual+somatic+emotional+motor) → SÂU, khó sửa
  → Depth ≈ Modality Count (đo được conceptually)
  → Sửa chunk = phải sửa ở MỌI modality đã encode → nhiều modality = nhiều effort
  → Chi tiết: Research/Modality-Analysis.md §3

Source: external (copy) ←→ internal (tự xây)
Depth: composite (modality count × connectivity × cluster × maturity)
Per domain: cùng 1 người, khác config per domain

2 con đường hình thành schema:
  Con đường 1: VÔ THỨC tự build (association learning — nhanh, từ experience trực tiếp)
  Con đường 2: PFC draft + compile (simulate trước — chậm, predict xa, cross-domain)
  CẢ HAI cần mạnh: vô thức = NỀN (rộng) + PFC = ĐỈNH (sâu, xa)
  → Chi tiết: Schema-Atlas.md §5.2.1
```

### 5.2 Schema = Connections → Desire States

```
Schema = kết nối chunks → ý nghĩa → PHÁT HIỆN MONG MUỐN → DESIRE STATES

Schema-Drive definition:
  Schema = model of reality, LIÊN TỤC tính toán (vô thức)
  → Schema tự phát hiện: "body CẦN gì / MUỐN gì?"
  → Output = MONG MUỐN CỤ THỂ → drive hành vi đáp ứng
  → ĐÁP ỨNG = body reward. KHÔNG đáp ứng = body ignore/reject.

  → "Desire" KHÔNG mơ hồ → = mong muốn CỤ THỂ từ schema tại thời điểm đó
  → "Sướng" KHÔNG từ info mới → = info/trải nghiệm ĐÁP ỨNG mong muốn schema
  → Info + schema đang muốn = sướng. Info + schema không muốn = mệt (nạp vô ích).
  → Schema dynamic: mong muốn THAY ĐỔI liên tục tùy context + body state

  Mong muốn XUẤT HIỆN khi:
    "Tại sao cái này mâu thuẫn?" → muốn coherence → drive giải quyết
    "Tôi muốn hiểu cái này" → muốn mastery → drive tìm hiểu
    "Tôi muốn gần người này" → muốn connection → drive tìm gần
    "Tôi đói" → muốn ăn → drive tìm thức ăn
    "Tôi muốn nghe nhạc hay" → muốn trải nghiệm → drive tìm nhạc

  Mong muốn ĐƯỢC ĐÁP ỨNG → body reward:
    "À, hiểu rồi!" → coherence fulfilled → opioid → sướng
    "Tôi làm được!" → mastery fulfilled → opioid → tự hào
    "Họ hiểu tôi!" → connection fulfilled → oxytocin → ấm
    "Ngon!" → experience fulfilled → opioid → thỏa mãn

  5 GIAI ĐOẠN CYCLE (mọi domain, mọi mong muốn):
    GĐ1: Tò mò     — mong muốn MỚI xuất hiện → dopamine (drive tìm)
    GĐ2: Effort     — tìm kiếm/build schema → dopamine + cortisol (tốn công)
    GĐ3: Sướng      — ĐÁP ỨNG đúng mong muốn! → opioid FIRE → peak reward
    GĐ4: Bình thường — mong muốn ĐÃ đáp ứng → body "ok" → baseline
    GĐ5: Chán       — hết mong muốn domain này → drive giảm → tìm domain mới
    → LOOP: GĐ5 → GĐ1 mới (domain khác hoặc deeper cùng domain)
    → "Hạnh phúc bền" = NHIỀU domains, KHÁC giai đoạn, LUÔN có domain ở GĐ2-3

  SCHEMA GRADIENT — từ body đến domain:
    Schema = hệ thống function linh hoạt để BODY giao tiếp với DOMAIN
    CỰC SÂU: gom theo body-need (6 nhóm) → "cần gì?"
    CỰC NÔNG: gom theo domain → "trong domain này làm gì?"
    GIỮA: gradient bất kỳ (rules, strategies, habits) → muôn hình vạn trạng
    → MỌI schema-drive PHỤC VỤ body-needs → confirm 100%
    → Chi tiết: Schema-Atlas.md §6.5

4 Schema Nền (UD reframe):
  1. Schema bản thân: "tôi có giá trị" → UD "being seen" baseline
  2. Schema thế giới: "an toàn" → UD "safety" baseline
  3. Schema người khác: "tin được" → UD "connection" baseline
  4. Schema tương lai: "kiểm soát được" → UD "agency" baseline
  → 4 schema = 4 UD BASELINES — set mức desire MẶC ĐỊNH

⚠️ SCHEMA SÂU NHẤT = BODY BASELINE STATE (chỉ CÓ 1):
  → Tất cả L1-L5 schemas → build TRÊN 1 nền tảng: body baseline state
  → Body baseline = tổng hợp TOÀN BỘ cơ thể ở trạng thái nghỉ:
    cortisol baseline + opioid tone + oxytocin level + muscle tension
    + gut state + HRV + sleep quality + immune baseline
  → = "Khi không có gì xảy ra, cơ thể TÔI feel thế nào?"
  → CHỈ CÓ 1 (body = 1 → baseline = 1 → ground truth = 1)
  → 4 Schema Nền = VERBAL LABELS cho body baseline (interpretation)
  → Fix body baseline → 4 schema nền + MỌI schemas TỰ UPDATE
  → Fix verbal labels mà KHÔNG fix body → "biết mà không đổi"
  → → Nhóm 1 Body-Needs = fix body baseline = fix GỐC mọi thứ
  → Chi tiết: Research/Schema-Atlas.md §5

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

"Chán" decompose thành 5 loại (xem §1.1 cho chi tiết + fix mỗi loại):
  Type A: Fulfilled Done   (Present 0, Desire 0, Coh HIGH) → lành mạnh, move on
  Type B: Over-Fulfilled   (Present −, Desire 0, body reject) → cần DỪNG
  Type C: Hijacked Empty   (Present 0→−, Desire 0, Lớp 2 chạy Lớp 1 = 0) → cần Lớp 1 thật
  Type D: Stagnant Restless (Present 0, Desire +, context trống) → cần domain mới/deeper
  Type E: Suppressed       (Present −, Desire suppressed) → cần nhận diện desire bị ém
  → PE cũ: cả 5 = "PE=0". Framework: 5 loại khác → 5 treatments khác.

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

### 5.8 UD Arbitration — PFC Workspace + Brake + Translate

```
ĐỊNH NGHĨA:
  UD State = BẢNG TỶ SỐ (passive, mô tả trạng thái)
  UD Arbitration = quá trình PFC WORKSPACE + BRAKE → hành vi được chọn

  Schemas fire TỰ ĐỘNG → body react → vô thức chain (spreading activation)
  → PFC NHẬN proposals (~200-500ms) → WORKSPACE hold options
  → Body evaluate: somatic markers cho mỗi option ("feel right?")
  → PFC: BRAKE options có body response âm
  → Option còn lại → execute
  → PFC: TRANSLATE ("tôi chọn vì...") → post-hoc rationalization

  → PFC KHÔNG chọn → PFC CHẶN cái không nên → cái còn lại = "được chọn"
  → PFC KHÔNG evaluate → body evaluate → PFC nhận kết quả body
  → PFC KHÔNG chain → vô thức chain → PFC hold workspace cho chain xảy ra

LUỒNG HOÀN CHỈNH:
  1. Schemas fire TỰ ĐỘNG (~50ms) → body react
  2. Vô thức chain (spreading activation) → propose multiple options
  3. PFC nhận (~200-500ms) → WORKSPACE hold options
  4. Body evaluate mỗi option (somatic markers)
  5. PFC: BRAKE options body không thích
  6. Option còn lại → Drive → T3 Hành Vi
  7. Body respond THẬT (ground truth) → Schema update → loop
  8. PFC: TRANSLATE kết quả thành lời (post-hoc)
      → Drive (specific action)
        → T3 Hành Vi
          → Body respond (ground truth)
            → Schema update → loop

3 LEVELS CỦA UD ARBITRATION:

  LEVEL 1 — PFC OFFLINE (yếu/mệt/say/stress):
    → Workspace ĐÓNG, Brake KHÔNG hoạt động
    → Schema MẠNH NHẤT tự win (loudest, không ai chặn)
    → = Autopilot: BG (habit) hoặc Amygdala (threat)
    → Ví dụ: mệt → ăn junk food (schema "ngon" loudest, brake off)
    → Ví dụ: say → nói thật (brake off → schema suppressed THOÁT)

  LEVEL 2 — PFC MODERATE (bình thường):
    → Workspace MỞ (nhỏ) → vô thức propose vài options
    → Body evaluate ngắn hạn (somatic: "cái nào feel ok?")
    → Brake HOẠT ĐỘNG: chặn options body không thích
    → Ví dụ: "đói nhưng deadline → body: làm xong rồi ăn ngon hẳn feel tốt hơn"

  LEVEL 3 — PFC STRONG (trained/rested/high capacity):
    → Workspace MỞ RỘNG → hold NHIỀU options phức tạp
    → Vô thức chain DÀI (spreading activation rộng hơn vì workspace lớn)
    → Body evaluate: somatic markers cho options DÀI HẠN
    → Brake: chặn options body predict âm DÀI HẠN (dù ngắn hạn dương)
    → Thậm chí: brake option DƯƠNG NGAY vì body predict âm về SAU
    → Ví dụ: nguyên thủ — workspace hold 5 schemas →
      vô thức chain hậu quả mỗi option → body evaluate mỗi chain →
      brake options net âm → option còn lại = "quyết định"
      → DÙ Experience NGAY = đau → body predict: dài hạn tốt hơn

WORKSPACE SIZE quyết định chất lượng arbitration:
  PFC yếu:       workspace NHỎ → vô thức chain NGẮN → options ÍT → body reward NGAY
  PFC vừa:       workspace VỪA → chain vừa → body evaluate ngắn-trung hạn
  PFC mạnh:      workspace RỘNG → chain DÀI → body evaluate dài hạn
  PFC cực mạnh:  workspace CỰC RỘNG → chain cực dài → "legacy", "meaning"

  → "Delayed gratification" KHÔNG phải "chịu khó"
  → = Workspace ĐỦ RỘNG cho vô thức chain DÀI → body evaluate: dài hạn TỐT HƠN
  → Marshmallow: trẻ chờ = workspace ĐỦ cho chain "chờ → 2 kẹo" → body: ok
  → Trẻ không chờ = workspace CHƯA ĐỦ → chỉ thấy "1 kẹo NGAY" → body: ăn

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

Domain = CỰC KỲ PHỨC TẠP → framework KHÔNG chứa domain data:
  → Domain = vô hạn sub-domains × vô hạn interactions → không gom hết
  → NHƯNG: domain data ĐÃ TỒN TẠI (sách, internet, research,...)
  → VÀ: AI đã train trên toàn bộ data đó → AI BIẾT domain rồi

  Division of labor:
    FRAMEWORK cho: BẢN ĐỒ THÔ — hướng nào, nhóm nào, cấu trúc tổng thể
    AI cho: TỪNG VỊ TRÍ CỤ THỂ — data chi tiết bất kỳ domain nào
    COMBINE: bản đồ CHỈ HƯỚNG → AI cung cấp CHI TIẾT → đến đúng nơi cần

  → Framework = BẢN ĐỒ THÔ (đường chính, khu vực, hướng đi)
  → AI = GOOGLE STREET VIEW (từng con đường, từng ngôi nhà, chi tiết)
  → Bản đồ thô ALONE: biết hướng nhưng thiếu chi tiết → dễ lạc ở ngã rẽ
  → Street View ALONE: thấy mọi thứ nhưng KHÔNG biết đi đâu → đi vòng vòng
  → Bản đồ + Street View: biết hướng + thấy chi tiết = ĐẾN NƠI

  → Hiện tại framework = bản đồ THÔ (có hướng, chưa chính xác tuyệt đối)
  → Nếu validated (fMRI, clinical test,...) → bản đồ CHÍNH XÁC dần
  → Không cần framework CHỨA domain → chỉ cần framework BIẾT CÁCH HỎI domain.
  → Chi tiết domain clusters: Schema-Atlas.md §4
  → Ứng dụng: Industry-Serve-BodyNeeds.md §10 (template phân tích ngành)
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

4. CALIBRATE SATISFACTION THRESHOLD (emergent: Satisfaction Signal + schema + pressure/challenge)
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
  → ⚠️ Learning reward = info GHÉP vào schema đang CHỜ → body reward
    Info + schema chờ = sướng. Info + không schema chờ = mệt.
    → Giáo dục tối ưu: tạo tò mò TRƯỚC → dạy SAU
    → Chi tiết: UD-Parenting.md §8

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

### 11.2 Tham số CHỈ ước lượng — KHÔNG THỂ chính xác tuyệt đối

```
⚠️ Framework = CÔNG CỤ NAVIGATE (bản đồ sơ), KHÔNG phải GPS chính xác.
Nhiều tham số BIẾT CÓ nhưng CHỈ ƯỚC LƯỢNG — không đo chính xác được:

1. Schema content: muôn hình vạn trạng → không liệt kê hết
   → Verbal mô tả ≈ 20% schema thật (multi-modal, chỉ verbal capture 1/6)
   → Mỗi người KHÁC → không có "danh sách schema chuẩn"
   → Chỉ có thể: nhận diện PATTERN + suy ngược + ước lượng nhóm

2. Body Baseline State: biết TỒN TẠI nhưng không đo trực tiếp
   → Tổng hợp toàn bộ cơ thể → không có 1 con số đại diện
   → Suy ngược từ: hành vi lặp + môi trường + body signals → ước lượng
   → Chi tiết: Schema-Atlas.md §5

3. Schema Depth (modality count): khái niệm rõ, đo thì không
   → Không scan được "chunk này encoded ở bao nhiêu modalities?"
   → Ước lượng: khó sửa cỡ nào → sâu cỡ đó. Body respond mạnh cỡ nào → sâu cỡ đó.

4. PFC Sub-region profile: ước lượng từ hành vi
   → fMRI đo vùng active nhưng KHÔNG đo "mạnh cỡ nào" per person
   → Ước lượng: behavior patterns + history + self-report
   → Chi tiết: PFC-Analysis.md §5

5. Modality Profile: self-report thiếu chính xác
   → Người somatic dominant: thường KHÔNG BIẾT mình somatic
   → "Bạn nghĩ bằng gì?" → majority trả lời "bằng lời" (verbal bias)
   → Chi tiết: Modality-Analysis.md §4

6. Threshold: composite 3 biến ước lượng
   → Hardware baseline + schema pressure − suppression → MỖI biến đều ước lượng
   → Chi tiết: Threshold-Analysis.md

7. Schema conflict intensity: predict HƯỚNG nhưng không predict ĐỘ
   → 2 schemas xung đột → biết ĐAU → không biết ĐAU BAO NHIÊU
   → Vector sum concept → nhưng không có SỐ chính xác

8. Drive Equation: conceptual, không tính ra SỐ
   → DRIVE = predicted body reward − cost → HƯỚNG đúng → SỐ không có
   → = Compass (hướng) không phải speedometer (số)

→ Framework cho: CẤU TRÚC + HƯỚNG + DIAGNOSTIC FRAMEWORK
→ Framework KHÔNG cho: SỐ CHÍNH XÁC + CHẨN ĐOÁN TUYỆT ĐỐI
→ = "Có bản đồ sơ" > "không có bản đồ" > "tưởng GPS mà thực ra sai"
→ HONEST hơn = HỮU ÍCH hơn (không overclaim → người dùng biết giới hạn)
```

### 11.3 Kiến trúc (giữ từ PE-centric)

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
│   ├── Core-v7-UD.md                    ← ★ FILE NÀY — v7.0 DRAFT (→ v8 Schema-Drive)
│   ├── Core-v7-Draft-Good.md            ← v7.0 DRAFT PE-centric (song song)
│   │
│   ├── ★ CORE THEORY:
│   ├── UD-Hypothesis.md                 ← Schema-Drive giả thiết + 24 cases + Einstein
│   ├── Schema-Atlas.md                  ← ★ Schema axes + body baseline + diagnostic
│   ├── Modality-Analysis.md             ← ★ 5 Experience + 1 Communication modality
│   ├── PFC-Analysis.md                  ← ★ Workspace+Brake+Translator + profiles
│   ├── Imagination-Analysis.md          ← Tưởng tượng + modality→chain direction
│   ├── Emotion-Map.md                   ← Cảm xúc map theo UD
│   ├── Threshold-Analysis.md            ← Threshold decompose (hw+schema+suppress)
│   ├── Parameters-Review.md             ← Tham số cần clarify
│   │
│   ├── ★ ỨNG DỤNG CÁ NHÂN:
│   ├── Body-Needs.md                    ← ★ 6 nhóm nhu cầu + tăng/giảm + diagnostic
│   ├── Body-Needs-ByAge.md              ← 6 nhóm theo độ tuổi
│   ├── Drive-Optimization.md            ← ★ Amplifier Trap + Sustainable Peak
│   ├── Addiction-Analysis.md            ← Nghiện: 3 nhóm + 4 giai đoạn + recovery
│   ├── UD-Parenting.md                  ← Phát triển trẻ em + attachment
│   ├── Hidden-Genius.md                 ← Tiềm năng ẩn + Einstein/Ramanujan/Tesla/Jobs
│   │
│   ├── ★ ỨNG DỤNG XÃ HỘI:
│   ├── Industry-Serve-BodyNeeds.md      ← ★ Phân tích ngành qua body-needs lens
│   │
│   ├── ★ LEGACY (từ phiên bản cũ, tham khảo):
│   ├── Component-Interaction-Map.md     ← Schema + brain analysis (v6-v7 early)
│   ├── Layer-Architecture-Draft.md      ← Kiến trúc cũ (tham khảo)
│   │
│   └── Meta-Impact/                     ← Vị trí framework trong học thuật
│       ├── Epistemological-Position.md
│       ├── Creator-Lens.md
│       └── Meta-Impact.md
│
├── Game-Industry/                        ← ★ ỨNG DỤNG GAME
│   ├── Core-Principles.md               ← Nguyên lý gốc (3 lớp reward)
│   ├── Player-Psychology.md             ← 8 channels player desire
│   ├── Gameplay-Design.md               ← Feel tuning + loops + difficulty
│   ├── Visual-Audio.md                  ← Art + sound serve feel
│   ├── Analytics-Guide.md               ← Đo lường + ABTest
│   ├── Monetization-Ethics.md           ← Kiếm tiền ethical
│   └── Team-Workflow.md                 ← Quy trình team casual game
│
├── Core-Deep-Dive/                       ← Đào sâu per component (v6)
└── Validation/                           ← Kiểm chứng (v6)
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
