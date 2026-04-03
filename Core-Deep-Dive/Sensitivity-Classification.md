# Sensitivity Classification — Phân Loại "Nhạy Cảm"

> **"Nhạy cảm" = 1 từ cho CẢ CHỤC thứ KHÁC NHAU.**
> Khác vùng não, khác receptor, khác nguyên nhân, khác biểu hiện.
> Gộp thành 1 từ = mất gần như toàn bộ thông tin.
>
> File này: PHÂN LOẠI theo 2 tầng (Sensor × Processing),
> để có CƠ SỞ quan sát. Không đo lường — chỉ cung cấp KHUNG.
> Nếu framework đúng, mọi người có thể dùng khung này để verify.

---

> **Trạng thái:** DRAFT — phân loại từ framework, chưa có thực nghiệm trực tiếp
> **Ngày:** 2026-04-02
> **Mục đích:** Tách "nhạy cảm" thành các thành phần ĐỘC LẬP, phân loại rõ ràng.
> Cung cấp khung để quan sát, không phải kết luận.
> **Reference:** Core-v7.5-Draft.md §1.5 (DRD4 Disturbance Threshold),
> Modality-Analysis.md (modality dominant), Attention-Spectrum.md (DRD4 spectrum)
> **⚠️ Phân loại = hypothesis — cần validate thực nghiệm**
> **⚠️ Rất khó đo lường hiện tại — file này = CƠ SỞ quan sát, không phải công cụ chẩn đoán**
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## 1. Vấn Đề — "Nhạy Cảm" Quá Chung

```
🟡 ĐỜI THƯỜNG GỌI "NHẠY CẢM" CHO TẤT CẢ:

  "Bạn ấy nhạy cảm lắm" → nghĩa là gì?
    → Dễ khóc? (emotional)
    → Sợ tiếng ồn? (auditory sensor)
    → Thấy lỗi logic nhanh? (pattern detection)
    → Dị ứng da? (skin receptor + sức khỏe)
    → Biết người khác đang buồn? (social/mirror)
    → Ngửi mùi nhạt? (olfactory sensor)
    → Đau răng khi uống nước lạnh? (nerve ending + sức khỏe)

  = 7 THỨ KHÁC NHAU HOÀN TOÀN
  = Khác VÙNG NÃO, khác RECEPTOR, khác NGUYÊN NHÂN
  = Gọi CÙNG 1 TỪ = vô dụng cho phân tích

  MAINSTREAM cũng gộp:
    → "Highly Sensitive Person" (Aron 1996) = gộp NHIỀU sensitivity
    → Hữu ích như NHÃN → nhưng không TÁCH rõ cơ chế
    → Framework cần TÁCH để predict chính xác hơn
```

---

## 2. Phân Loại — 2 Tầng: Sensor (Input) × Processing (Neurons)

```
🔴 HYPOTHESIS — khung phân loại:

  ⭐ MỌI "nhạy cảm" nằm ở 1 trong 2 tầng (hoặc CẢ HAI):

  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │  DOMAIN (thực tế bên ngoài)                                  │
  │       ↓ signal (ánh sáng, âm thanh, nhiệt, hóa chất,...)   │
  │                                                              │
  │  ┌─── TẦNG 1: SENSOR (cơ quan đầu vào) ───────────────┐    │
  │  │  Mắt (retina), Tai (cochlea), Da (receptors),        │    │
  │  │  Mũi (olfactory), Lưỡi (taste buds), Nội tạng,...    │    │
  │  │                                                       │    │
  │  │  Chất lượng: TỐT / TRUNG BÌNH / KÉM (sức khỏe)     │    │
  │  │  = Quyết định INPUT vào não nhiều/ít/méo              │    │
  │  └───────────────────────────────────────────────────────┘    │
  │       ↓ neural signal                                        │
  │  ┌─── TẦNG 2: PROCESSING (não xử lý) ─────────────────┐    │
  │  │  Visual cortex, Auditory cortex, Somatosensory,       │    │
  │  │  Limbic (emotion), Mirror neurons, VTA+PFC (pattern), │    │
  │  │  mPFC (social),...                                     │    │
  │  │                                                       │    │
  │  │  Chất lượng: DOMINANT / TRUNG BÌNH / YẾU              │    │
  │  │  = Quyết định PROCESS sâu/nông/chi tiết/thô           │    │
  │  └───────────────────────────────────────────────────────┘    │
  │       ↓ kết quả                                              │
  │  Body-base response (reward / dissonance / satisfaction)      │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘

  → = "Nhạy cảm" có thể ở TẦNG 1 (sensor) hoặc TẦNG 2 (processing) hoặc CẢ HAI
  → = PHẢI xác định TẦNG NÀO mới biết nguyên nhân + cách ứng xử
```

---

## 3. Tầng 1 — Sensor: 3 Mức Chất Lượng Per Channel

```
🔴 MỖI KÊNH INPUT có 3 mức — ĐỘC LẬP nhau:

  ┌──────────┬────────────────┬──────────────────┬────────────────────┐
  │ Channel  │ TỐT (nhạy thật)│ TRUNG BÌNH       │ KÉM (sức khỏe)    │
  ├──────────┼────────────────┼──────────────────┼────────────────────┤
  │ Mắt      │ Retina dense → │ Bình thường      │ Cận/viễn/loạn →    │
  │          │ thấy chi tiết  │                  │ input méo          │
  ├──────────┼────────────────┼──────────────────┼────────────────────┤
  │ Tai      │ Cochlea nhạy → │ Bình thường      │ Giảm thính lực →   │
  │          │ nghe tần rộng  │                  │ input thiếu        │
  ├──────────┼────────────────┼──────────────────┼────────────────────┤
  │ Da       │ Receptors dense│ Bình thường      │ Bệnh da/dị ứng →   │
  │          │ → feel chạm rõ │                  │ signal lỗi (ngứa)  │
  ├──────────┼────────────────┼──────────────────┼────────────────────┤
  │ Mũi      │ Olfactory tốt →│ Bình thường      │ Xoang/viêm →       │
  │          │ ngửi mùi nhạt  │                  │ kích thích giả     │
  ├──────────┼────────────────┼──────────────────┼────────────────────┤
  │ Lưỡi     │ Taste buds     │ Bình thường      │ Viêm/bệnh →        │
  │          │ nhiều → vị rõ  │                  │ mất vị/méo vị      │
  ├──────────┼────────────────┼──────────────────┼────────────────────┤
  │ Nội tạng │ Interoception  │ Bình thường      │ Rối loạn → signal   │
  │          │ rõ → biết đói/ │                  │ sai (IBS, tim      │
  │          │ no/mệt chính   │                  │ đập nhanh,...)     │
  │          │ xác            │                  │                    │
  └──────────┴────────────────┴──────────────────┴────────────────────┘

  ⭐ QUAN TRỌNG — "NHẠY" vs "KÉM" nhìn GIỐNG NHAU từ ngoài:

    Mũi THÍNH (sensor tốt): ngửi MÙI NHẠT mà người khác không ngửi → "nhạy"
    Mũi XOANG (sensor kém): KÍCH THÍCH bởi mùi bình thường → "nhạy"
    → Bên ngoài: CẢ HAI đều "phản ứng với mùi" → gọi "nhạy"
    → Bên trong: HOÀN TOÀN KHÁC — 1 cái DETECT tốt, 1 cái BỊ LỖI

    → = PHẢI phân biệt: "nhạy vì TỐT" vs "nhạy vì BỊ LỖI"
    → = Thuộc về y tế phân biệt — framework chỉ ĐÁNH DẤU cần tách
```

---

## 4. Tầng 2 — Processing: Modality Dominant × Vùng Não

```
🟡 CÙNG INPUT → KHÁC PROCESSING → KHÁC "NHẠY":

  ┌────────────────────┬───────────────────┬──────────────────────────┐
  │ Processing area    │ Khi DOMINANT      │ "Nhạy" biểu hiện         │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ Visual cortex      │ Process hình ảnh  │ Thấy chi tiết, màu sắc, │
  │                    │ chi tiết + sâu    │ layout, design rõ         │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ Auditory cortex    │ Process âm thanh  │ Phân biệt tone, pitch,  │
  │                    │ chi tiết + sâu    │ harmony, accent rõ        │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ Somatosensory      │ Process body      │ Feel nhiệt, chạm, nhịp, │
  │ cortex             │ signal chi tiết   │ đau, rung, flow rõ        │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ Limbic + Insula    │ Process emotion   │ Xúc động dễ, feel sâu,  │
  │                    │ chi tiết + sâu    │ empathy strong             │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ Mirror neurons     │ Simulate người    │ "Feel" người khác đang   │
  │                    │ khác chi tiết     │ gì, empathy hành vi       │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ VTA + PFC          │ Detect mismatch   │ Thấy mâu thuẫn, pattern │
  │ (Disturbance       │ giữa expectation  │ lỗi, "cái này SAI"       │
  │  Threshold)        │ vs reality        │ (Core §1.5: DRD4)        │
  ├────────────────────┼───────────────────┼──────────────────────────┤
  │ mPFC + Amygdala    │ Simulate social   │ "Họ nghĩ gì về tôi",    │
  │                    │ judgment          │ detect social threat       │
  └────────────────────┴───────────────────┴──────────────────────────┘

  → = MỖI VÙNG = 1 LOẠI "nhạy" RIÊNG → ĐỘC LẬP với nhau
  → = Có thể: somatosensory DOMINANT + visual YẾU
    → = "Nhạy" body signal + "không nhạy" hình ảnh
    → = Cùng 1 người, KHÁC nhạy cảm per channel

  ⭐ PROCESSING KHÁC SENSOR:
    → Sensor TỐT + processing YẾU = input rõ nhưng KHÔNG dùng hết
    → Sensor KÉM + processing MẠNH = input ít nhưng KHAI THÁC SÂU
    → = 2 tầng ĐỘC LẬP → kết hợp ra nhiều profiles khác nhau
```

---

## 5. Tại Sao Cần Tách — Ví Dụ Thực Tế

```
🟡 CÙNG GỌI "NHẠY CẢM" — KHÁC HOÀN TOÀN:

  "Nhạy cảm tiếng ồn":
    A: Auditory cortex DOMINANT → nghe CHI TIẾT → tiếng ồn = quá nhiều data → mệt
    B: Cortisol CAO → noise threshold THẤP → tiếng ồn = trigger stress
    C: Tai bị viêm → nerve dễ kích thích → tiếng bình thường = đau
    → 3 người cùng "nhạy tiếng ồn" → 3 NGUYÊN NHÂN KHÁC → 3 CÁCH XỬ LÝ KHÁC:
      A: headphones noise-cancel (giảm input) hoặc chấp nhận (hardware)
      B: giảm cortisol gốc (ngủ đủ, bớt threat)
      C: chữa viêm tai (y tế)

  "Nhạy cảm cảm xúc":
    A: Limbic MẠNH → feel SÂU → xúc động vì PROCESS SÂU
    B: Cortisol CAO → threshold thấp → xúc động vì ĐÃ GẦN ngưỡng
    C: Trauma chunks → specific trigger → xúc động vì PATTERN fire
    → 3 nguyên nhân → 3 cách support KHÁC

  → = Không tách = "nhạy cảm, kệ đi" hoặc "nhạy cảm, sao yếu vậy"
  → = Tách ra = biết CHÍNH XÁC channel nào, tầng nào, nguyên nhân gì → FIX đúng
```

---

## 6. Honest Assessment

```
  ESTABLISHED (🟢):
    🟢 Sensory sensitivity varies per individual (genetics + health)
    🟢 Modality dominance = different cortical processing strength
       (visual vs auditory vs somatic — individual differences)
    🟢 "Highly Sensitive Person" (Aron 1996): ~15-20% population
       score high on Sensory Processing Sensitivity scale
    🟢 Interoception varies: some people detect internal signals better
       (heartbeat detection task — established measure)
    🟢 DRD4 variants affect novelty-seeking threshold (Core §1.5)

  FRAMEWORK SUY LUẬN (🟡):
    🟡 "2 tầng: Sensor × Processing": logical decomposition,
       consistent với neuroscience (receptor ≠ cortex processing).
       Chưa có study phân loại "nhạy cảm" theo ĐÚNG 2 tầng này.
    🟡 "3 mức sensor: tốt / trung bình / kém": simplified.
       Thực tế = gradient, không phải 3 bậc rời rạc.
    🟡 "Nhạy vì TỐT vs nhạy vì LỖI": phân biệt hữu ích,
       consistent với y khoa (pathological vs functional sensitivity).
    🟡 "Mỗi vùng processing = 1 loại nhạy riêng": consistent với
       modular brain theory, nhưng não KHÔNG hoàn toàn modular.

  HYPOTHESIS (🔴):
    🔴 Phân loại này = COMPLETE — chắc chắn CHƯA (luôn có thể thiếu)
    🔴 2 tầng = ĐỘC LẬP hoàn toàn — có thể có INTERACTION chưa biết
    🔴 Có thể dùng để PREDICT sensitivity per person — chưa test
```

---

## 7. Kết Nối

```
→ Core-v7.5-Draft.md §1.5: DRD4 Disturbance Threshold (pattern detection sensitivity)
→ Modality-Analysis.md: modality dominant (processing tầng 2)
→ Attention-Spectrum.md: DRD4 spectrum (novelty-seeking × sensitivity)
→ Cortisol-Baseline.md: cortisol noise che signal (ảnh hưởng sensitivity perceived)
→ Connection.md §4: melody calibration (mirror neurons × social sensitivity)
→ Boredom-Analysis.md §3: sensory channels đói (sensor input cần)
→ Personal-Melody.md §3: multi-modal sync (nhiều channels phối hợp)
```

---

> *Sensitivity Classification — "'Nhạy cảm' = 1 từ cho cả chục thứ khác nhau.
> Tầng 1 (Sensor): mắt, tai, da, mũi — TỐT / bình thường / KÉM (sức khỏe).
> Tầng 2 (Processing): visual, auditory, somatic, emotional, social, pattern — DOMINANT / yếu.
> 'Nhạy vì TỐT' ≠ 'nhạy vì LỖI' — nhìn ngoài GIỐNG, gốc KHÁC, fix KHÁC.
> Phải TÁCH mới biết: channel NÀO, tầng NÀO, nguyên nhân GÌ → xử lý ĐÚNG."*
