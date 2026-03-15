# PE Sensitivity — Processing Pipeline Chi Tiết

> **Phiên bản:** 1.3 (Framework v6.0)
> **Vị trí:** Core.md §5.3 → file này (deep-dive)
> **Nguyên tắc:** Core.md gộp PE Sensitivity = 1 tham số (đủ cho ứng dụng).
> File này tách thành sub-mechanisms + encoding modality (cho phân tích sâu).
> **Quy ước:** 🟢 Nghiên cứu vững | 🟡 Suy luận có cơ sở | 🔴 Giả thuyết

---

## Mục Lục

1. [Tổng Quan](#1-tổng-quan)
2. [① Amplitude](#2-amplitude)
3. [② Precision Weighting](#3-precision-weighting)
4. [③ PE Decay Rate](#4-pe-decay-rate)
5. [④ Generalization Scope](#5-generalization-scope)
6. [Encoding Modality](#6-encoding-modality)
7. [Encoding Profile — Mỗi Người = Mix](#7-encoding-profile)
8. [Integration: Encoding × Generalization × Depth](#8-integration)
9. [Câu Hỏi Mở + Điều Kiện Verify](#9-câu-hỏi-mở)

---

## 1. Tổng Quan

PE Sensitivity = cách não XỬ LÝ tín hiệu PE (Prediction Error) từ chunk mới.

**Tại sao phức tạp:** PE Sensitivity không chỉ là "tốc độ chán." Nó bao trùm toàn bộ pipeline xử lý thông tin — từ nhận tín hiệu → đánh giá → học → phân loại → mã hóa. Đây là cơ chế não dùng để XÂY CHÍNH NÓ: mỗi chunk mới đi qua pipeline này trước khi trở thành một phần của network.

```
PROCESSING PIPELINE — mỗi chunk mới đi qua 4 bước:

Input: PE xảy ra (chunk mới hình thành, |actual − predicted| > 0)
  │
  ├─ ① AMPLITUDE — tín hiệu PE mạnh hay yếu?
  │     (hardware: DA receptor, NE level)
  │
  ├─ ② PRECISION WEIGHTING — PE đáng tin không? thưởng ngay hay kiểm thêm?
  │     (hardware + software: neural circuit + training)
  │
  ├─ ③ HABITUATION RATE — model cập nhật nhanh hay chậm?
  │     (learning: synaptic plasticity)
  │
  └─ ④ GENERALIZATION SCOPE — chunk này "giống" loại nào? generalize hay giữ riêng?
        (categorization: encoding modality quyết định)
        │
        └─ ENCODING MODALITY — mã hóa bằng cách nào?
              (somatic / spatial / verbal / motor / temporal / auditory)
  │
  Output: chunk được lưu vào network → Depth TĂNG (xem Core.md §8.9)
```

**Tại sao gộp cho ứng dụng:** 4 sub-mechanism THƯỜNG tương quan cùng hướng — người amplitude cao THƯỜNG precision nhanh, habituate nhanh, generalize rộng. Gộp thành 1 tham số "PE Sensitivity cao/thấp" = mất ít precision, đủ cho predict hành vi trong đa số trường hợp.

**Tại sao tách cho phân tích sâu:** Edge cases tồn tại — amplitude cao nhưng precision thận trọng = Architect intense (NE cao + precision thấp). Hoặc: habituation nhanh nhưng generalization hẹp = phenotype khác biệt (xem §5). Tách khi cần phân tích sâu, can thiệp chính xác, hoặc giải thích tại sao 2 người cùng "sensitivity cao" mà biểu hiện khác nhau.

---

## 2. ① Amplitude — Volume Tín Hiệu DA

🟡 (suy luận có cơ sở từ neurochemistry đã xác lập)

```
= "Volume" tín hiệu dopamine khi PE xảy ra.
  Cùng chunk mới, cùng PE, người A phản ứng MẠNH hơn người B.

Quyết định bởi (hardware, thay đổi rất chậm):
  D2 receptor density:  nhiều D2 → nhạy hơn với DA (🟢 Volkow 2002)
  COMT Val/Met:         Met/Met → DA ở synapse lâu → signal dài (🟢 Egan 2001)
  NE level:             NE cao → khuếch đại TẤT CẢ tín hiệu (xem Neurochemistry.md §7.2)

CAO: chunk mới → "WOW!" → PE signal mạnh → drive mạnh
     Ưu: drive lớn, engagement cao
     Nhược: dễ overwhelm, cần PE lớn hơn để duy trì (adaptation)

THẤP: chunk mới → "à, ok" → PE signal nhẹ → drive nhẹ nhàng
      Ưu: ổn định, không dễ overwhelm
      Nhược: cần tích lũy PE dần, drive nhỏ hơn per event

⚠️ Amplitude KHÔNG quyết định HƯỚNG (deep vs broad) — chỉ quyết định CƯỜNG ĐỘ.
   Hướng do ④ generalization scope quyết định.
```

**Thay đổi được không?** Rất chậm. D2 receptor density bị down-regulate bởi dopamine flooding (MXH, chất kích thích). Up-regulate chậm qua dopamine fasting, thiền, exercise. 🟢 Volkow et al. (2002).

---

## 3. ② Precision Weighting — Bộ Lọc Đáng Tin

🟡 (suy luận từ 🟢 Feldman & Friston 2010 — precision weighting trong predictive coding)

```
= Não đánh giá PE ĐÁNG TIN cỡ nào TRƯỚC KHI trả thưởng.
  Không phải mọi PE đều được thưởng ngay — não gán trọng số (precision) trước.

Precision CAO (gán nhanh, tin ngay):
  → "PE này đáng tin!" → DA fire NGAY → thưởng NHANH, MẠNH
  → Phát hiện mới → sướng NGAY → threshold tạm thỏa mãn
  → Thiên explore: sướng ngay = đủ, nhảy sang cái tiếp theo

Precision THẤP (gán chậm, cần kiểm thêm):
  → "PE này cần kiểm..." → DA fire CHẬM, DẦN DẦN khi confirm thêm
  → Phát hiện mới → đối chiếu kỹ → thưởng dần khi confirm
  → Thiên deepen: cần ở lại domain đủ lâu để collect đủ reward
  → Chunks sync tự nhiên (vì ở lâu)

⚠️ Precision weighting có phần hardware (neural circuit speed) VÀ phần software
   (training thay đổi được). Nhà khoa học luyện precision THẤP (thận trọng)
   qua training, không chỉ bẩm sinh.
```

**Interaction với ①:** Amplitude cao + Precision cao = PE mạnh VÀ tin ngay → drive cực lớn, nhảy nhanh (Improviser intense). Amplitude cao + Precision thấp = PE mạnh NHƯNG cần kiểm → Architect intense (NE cao, đào sâu mãnh liệt). Đây là edge case mà gộp 1 tham số sẽ bỏ sót.

---

## 4. ③ PE Decay Rate — Tốc Độ Chunk "Cháy"

🟡 Reframe từ "Habituation Rate".
   Cơ sở cũ (Thompson & Spencer 1966) nói về reflex-level habituation ở spinal circuits,
   không trực tiếp về chunk-level PE decay — bước suy luận cần ghi nhận.
   Xem Research-References/PE-Sensitivity/Thompson-Spencer-1966-habituation.md.

```
= Tốc độ 1 chunk CỤ THỂ mất PE, KHÁC NHAU per kênh.

NHANH: chunk mới hôm nay → "biết rồi" ngày mai
  → PE cháy nhanh → cần chunk MỚI sớm
  → Chunk LIFESPAN ngắn

CHẬM: chunk mới hôm nay → vẫn cho PE tuần sau
  → PE cháy chậm → cùng chunk vẫn thú vị lâu
  → Chunk LIFESPAN dài

⚠️ QUAN TRỌNG: "Tốc độ chán" observable = EMERGENT METRIC, không chỉ ③.
   Chunk lifespan thực tế phụ thuộc:
   (a) per-channel PE decay rate (③ — parameter này)
   (b) Channel Anchoring — số kênh đồng thời active trên chunk
       Multi-channel chunk sống LÂU HƠN single-channel
       (xem Layer-Architecture-Draft.md §6.1)
   (c) hedonic adaptation
   (d) complexity/renewal capacity của chunk
   → ③ chỉ là 1 THÀNH PHẦN của chunk lifespan, không phải toàn bộ.

Per-channel distinction:
  Wanting (DA) decay ≠ Liking (opioid) decay cho cùng chunk.
  Chunk có thể wanting-dead nhưng liking-alive (hoặc ngược lại).
  (Berridge 2009 — wanting/liking dissociation)

Cơ sở sinh học:
  Synaptic plasticity rate — tốc độ synapse thay đổi strength
  BDNF (Brain-Derived Neurotrophic Factor) — hỗ trợ plasticity
  NMDA receptor function — gate cho synaptic change
  → Hardware, nhưng KHÔNG hoàn toàn cố định (exercise, sleep ảnh hưởng)
  ⚠️ Cơ sở này dựa trên long-term plasticity (LTP/LTD),
     khác với "polysynaptic low-frequency depression" trong Thompson & Spencer.
     Bước nhảy suy luận cần ghi nhận.
```

**③ vs ④ — Tại sao cần phân biệt:**

```
③ = chunk A cháy nhanh hay chậm (per-chunk, temporal)
④ = chunk A cháy → chunk B (tương tự) có cháy theo không (cross-chunk, spatial)

③ chỉ nói: chunk này cụ thể mất PE nhanh/chậm cỡ nào
④ nói: habituation có LAN SANG các chunk tương tự không

2 cái KHÁC NHAU — ③ nhanh + ④ hẹp ≠ ③ nhanh + ④ rộng:
  ③ nhanh + ④ hẹp: chán chunk A nhanh, nhưng chunk B (tương tự) vẫn mới
    → Vẫn ở lại domain, chỉ cần instance khác → phenotype: "làm nhiều nhưng cùng loại"
  ③ nhanh + ④ rộng: chán chunk A nhanh VÀ cả loại A cũ
    → Phải sang domain khác → phenotype: explore liên tục
  ③ chậm + ④ hẹp: chunk A PE lâu, chunk B cũng PE lâu
    → Ở lại domain rất lâu, mỗi cái đều thú vị lâu → phenotype: deep specialist
  ③ chậm + ④ rộng: chunk A PE lâu, nhưng loại A đồng loạt cũ?
    → 🔴 Phenotype chưa rõ — cần data. Dự đoán: "biết nhiều lĩnh vực,
       mỗi cái biết lâu, nhưng không đào sâu vì cảm giác đã hiểu cả loại"
```

---

## 5. ④ Generalization Scope — Phạm Vi Lan Tỏa Habituation

🟡 (suy luận có cơ sở — logic framework, consistent với data quan sát, chưa có reference học thuật trực tiếp cho concept "generalization scope" trong PE sensitivity context)

### 5.1 Định Nghĩa

```
= Khi habituate chunk A, các chunk TƯƠNG TỰ B, C, D... có bị habituate theo không?

HẸP: habituate chunk A → chỉ chunk A mất PE. Chunk B (tương tự A) vẫn mới.
  → Mỗi instance trong cùng category = genuinely mới
  → Có thể ở lại 1 domain rất lâu vì mỗi instance khác nhau
  → Observable: "deep specialist", "10 năm cùng nghề không chán"

RỘNG: habituate chunk A → cả "loại giống A" mất PE đồng loạt.
  → 1 instance đại diện cho cả category → "biết rồi" cả loại
  → Phải sang category/domain KHÁC HẲN để có PE mới
  → Observable: "broad explorer", "chán nhanh cả lĩnh vực"
```

### 5.2 Tại Sao ④ Quan Trọng

```
④ giải thích câu hỏi mà ①②③ KHÔNG giải thích được:

CÂU HỎI: Tại sao 2 người cùng Novelty PRIMARY + Threshold cao + Capacity cao
          mà biểu hiện hoàn toàn khác nhau?
          Người A: deep specialist (1 domain, 10+ năm)
          Người B: broad explorer (nhảy domain liên tục)

TRƯỚC ④: "Sensitivity khác" — nhưng sensitivity nào? ①②③ đều nói về
          CƯỜNG ĐỘ và TỐC ĐỘ, không nói về PHẠM VI.

SAU ④: ④ hẹp → mỗi instance vẫn mới → ở lại domain → deep
        ④ rộng → cả loại cũ → phải sang domain mới → broad

→ "Thích cái mới" (broad) vs "thích đi sâu" (deep) = KHÔNG phải 2 loại Novelty.
  Cùng 1 kênh Novelty (chunk mới = PE), khác ④ generalization scope → khác expression.
  "Structural Novelty" vs "Creative Novelty" = NHÃN MÔ TẢ downstream,
  không cần parameter riêng cho Novelty sub-type.
```

### 5.3 Cơ Chế Dự Đoán: Encoding Modality → ④

```
🔴 GIẢ THUYẾT (logic mạnh, chưa verify đủ):

④ Generalization scope CÓ THỂ là hệ quả của ENCODING MODALITY —
cách não mã hóa chunk quyết định mức compression → quyết định generalization.

  Encoding compression CAO (vd: somatic/gestalt):
    Nhiều thứ khác nhau → cùng 1 representation (feeling/gestalt)
    → Chunk B "giống" chunk A ở level encoding → generalize → PE giảm
    → ④ RỘNG

  Encoding compression THẤP (vd: visual-spatial/detail):
    Nhiều thứ tương tự → khác representation (khác tọa độ, khác kết nối)
    → Chunk B ≠ chunk A ở level encoding → không generalize → PE giữ
    → ④ HẸP

→ Nếu đúng: ④ KHÔNG PHẢI parameter riêng, mà là HỆ QUẢ của encoding modality.
→ Chi tiết encoding modality: §6.
→ Cần thêm data để verify. Xem §9.
```

### 5.4 Lưu Ý

```
④ Generalization scope ≠ intelligence hay ability:
  ④ hẹp → KHÔNG có nghĩa "giỏi hơn" hay "tập trung hơn"
  ④ rộng → KHÔNG có nghĩa "nông" hay "thiếu kiên nhẫn"

  Đây là CÁCH NÃO PHÂN LOẠI thông tin, không phải chất lượng xử lý.
  Cả hai có ưu/nhược riêng:
    ④ hẹp: ưu = deep expertise. nhược = có thể miss cross-domain patterns
    ④ rộng: ưu = cross-domain transfer nhanh. nhược = khó accumulate depth per domain

④ có thể THAY ĐỔI được không?
  🔴 Chưa rõ. Nếu ④ = hệ quả encoding modality (hardware) → khó thay đổi.
  Nhưng nếu encoding modality = tỉ lệ sử dụng (software habit) → có thể shift dần.
  Cần research thêm.
```

---

## 6. Encoding Modality — Cách Não Mã Hóa Chunk

### 6.1 Định Nghĩa + Phân Biệt

```
Encoding modality = cách não LƯU TRỮ chunk (internal representation).
KHÔNG phải cách não NHẬN thông tin (sensory input).

Phân biệt:
  SENSORY INPUT (cách thông tin VÀO):
    Thị giác, thính giác, xúc giác, khứu giác, vị giác, nội cảm
    → Đây là KÊNH VÀO — mọi người đều có, hardware giác quan

  ENCODING MODALITY (cách thông tin được LƯU):
    Cùng 1 input (ví dụ: nghe bài giảng toán), người khác nhau
    LƯU bằng representation khác nhau:
      → Người A: "cảm giác" hiểu/không hiểu (somatic)
      → Người B: "hình ảnh" đồ thị, sơ đồ (visual-spatial)
      → Người C: "câu chữ" lặp lại trong đầu (verbal)
      → Người D: "viết tay" mới nhớ (motor)

  Sensory input → FEED INTO encoding modality
  Cùng input, khác encoding → khác representation → khác generalization

⚠️ "Encoding modality" KHÔNG phải "learning style" theo nghĩa giáo dục phổ thông.
   "Learning style" (visual learner, auditory learner...) đã bị bác bỏ như là
   phương pháp giảng dạy tối ưu (🟢 Pashler et al. 2008).
   Encoding modality ở đây = cách não REPRESENT thông tin nội bộ,
   không phải "dạy bằng hình thì học giỏi hơn."
   Sự khác biệt: encoding modality ảnh hưởng GENERALIZATION PATTERN,
   không phải learning EFFECTIVENESS.
```

### 6.2 4 Encoding Modality Chính

```
Câu hỏi phân biệt: "Khi bạn NGHĨ, bạn nghĩ bằng gì?"

4 modality = 4 cách não REPRESENT chunk:
  1. Somatic       — body state, gestalt, feeling
  2. Visual-Spatial — mental image, position, map
  3. Verbal         — inner speech, narrative, proposition
  4. Motor          — action sequence, movement pattern

Tại sao 4, không phải 6 hay 8?
  Auditory: có thể encode thành verbal (lời), spatial (vị trí âm trong không gian),
    hoặc somatic (feeling khi nghe). Chưa rõ auditory có phải modality RIÊNG
    cho lưu trữ thông tin chung, hay chỉ là sensory input. 🔴
  Temporal: thứ tự, nhịp, timing = CHIỀU ĐO cross-cutting, không phải modality riêng.
    Mọi modality đều có khía cạnh temporal (sequence of images, sequence of feelings,
    sequence of words, sequence of movements). 🔴
  → 4 modality chính = đủ cover cho phân tích hiện tại.
  → Có thể mở rộng nếu data cho thấy cần thêm.
```

### 6.3 Somatic — Cảm Giác Tổng Thể

🟢 Cơ sở thần kinh vững. 🟡 Dự đoán generalization = suy luận framework.

```
HỆ THẦN KINH:
  Anterior insula — hub tích hợp interoception (🟢 Craig 2002, 2009)
  Somatic marker pathway (🟢 Damasio 1994, somatic marker hypothesis)
  → Não tạo "body state representation" cho mỗi tình huống
  → Quyết định nhanh dựa trên feeling, TRƯỚC KHI logic kịp xử lý

ĐẶC ĐIỂM ENCODING:
  Representation: body state tổng thể (gestalt)
  Compression: CAO — nhiều input khác nhau → 1 feeling
  Tốc độ encode: NHANH — "tích hợp 1 phát"
  Detail: THẤP — giữ essence, bỏ specifics
  Retrieval: bằng FEELING ("cảm giác giống lần trước")
  Accuracy ban đầu: TRUNG BÌNH — nắm được essence nhưng bỏ sót specifics
  Refinement: CẦN KÊNH PHỤ — somatic compress 1 lần, khó tự rà lại
    → Không có "chi tiết" để đối chiếu lại → cần verbal/spatial bổ sung
    → Đây là modality DUY NHẤT cần nguồn bên ngoài để refine
    → "Lưu 1 phát" → cảm nhận đúng nhưng thiếu nuance

DỰ ĐOÁN GENERALIZATION (🟡):
  Compression cao → nhiều thứ khác nhau → cùng feeling → "biết rồi"
  → Generalization RỘNG
  → Ưu: xử lý nhanh, quyết định nhanh, cross-domain transfer nhanh
  → Nhược: dễ "đã cảm nhận rồi" → cần input mới liên tục

  Ưu/nhược cho Novelty expression:
    + Cross-domain: feeling mới ở domain mới = PE nhanh
    + Quyết định: "cảm giác đúng/sai" trước khi phân tích
    − Depth: cùng domain feeling "giống nhau" nhanh → PE giảm
    − Detail: bỏ sót chi tiết quan trọng (đã compress mất)

LĨNH VỰC THIÊN SOMATIC:
  Nghệ thuật (cảm xúc), kinh doanh (gut feeling), thể thao (body awareness),
  quan hệ (empathy), sáng tạo (intuition)
```

### 6.4 Visual-Spatial — Hình Ảnh + Vị Trí

🟢 Cơ sở thần kinh vững. 🟡 Dự đoán generalization = suy luận framework.

```
HỆ THẦN KINH:
  Posterior parietal cortex — spatial processing (🟢 Culham & Kanwisher 2001)
  Hippocampus — place cells, cognitive maps (🟢 O'Keefe & Nadel 1978)
  Visual cortex — mental imagery (🟢 Kosslyn 1994)
  → Não tạo "mental map" với tọa độ, vị trí, quan hệ không gian

ĐẶC ĐIỂM ENCODING:
  Representation: map/image với positions + relations
  Compression: THẤP — mỗi arrangement = unique configuration
  Tốc độ encode: CHẬM HƠN somatic — cần "sắp xếp" vào đúng vị trí
  Detail: CAO — giữ tọa độ, quan hệ, cấu trúc cụ thể
  Retrieval: bằng HÌNH ẢNH/VỊ TRÍ ("thấy lại" trong đầu, "nhớ nó nằm ở đâu")
  Accuracy ban đầu: CAO — giữ detail, ít mất thông tin
  Refinement: TỰ ITERATE — kiểm tra lại vị trí, cấu trúc, quan hệ trong đầu
    → Có "bản đồ" để đối chiếu → tự phát hiện lỗi/thiếu
    → Mỗi lần re-check = cơ hội tìm thêm connection mới
    → Chậm nhưng accumulate accuracy theo thời gian

SPATIAL BIỂU HIỆN KHÁC NHAU TÙY MIX (xem §7.2):
  Spatial = 1 modality, nhưng biểu hiện bị "nhuộm màu" bởi kênh khác trong mix.
  Motor fader cao → spatial thiên kinesthetic. Verbal cao → spatial thiên visual.
  Không có subtype — chỉ là mixing board ratio khác → output khác.

DỰ ĐOÁN GENERALIZATION (🟡):
  Compression thấp → mỗi instance = unique arrangement → "mới"
  → Generalization HẸP
  → Ưu: ở lại domain lâu, mỗi instance genuinely khác
  → Nhược: chậm hơn, cần thời gian sắp xếp, khó cross-domain transfer

  Ưu/nhược cho Novelty expression:
    + Depth: cùng domain, mỗi cấu trúc mới = genuinely mới → PE bền
    + Detail: thấy chi tiết, phát hiện pattern cụ thể
    − Breadth: domain mới cần thời gian xây map → cold start chậm
    − Speed: encode chậm hơn somatic → wave pattern (tích lũy → burst)

LĨNH VỰC THIÊN VISUAL-SPATIAL:
  Toán học (cấu trúc), kiến trúc, lập trình (mental model), cờ vua,
  khoa học (diagram, model), cartography, surgery
```

### 6.5 Verbal-Analytical — Lời Nói + Logic

🟢 Cơ sở thần kinh vững. 🟡 Dự đoán encoding characteristics = suy luận. 🔴 Dự đoán generalization = giả thuyết (chưa có data người verbal-dominant để verify).

```
HỆ THẦN KINH:
  Broca's area — speech production, syntax (🟢 Broca 1861)
  Wernicke's area — language comprehension (🟢 Wernicke 1874)
  Left hemisphere language network (🟢 lateralization research)
  Angular gyrus — semantic integration (🟢 Binder et al. 2009)
  → Não tạo "propositional representation" — câu, logic chain, narrative

ĐẶC ĐIỂM ENCODING:
  Representation: propositions, narratives, logical chains
  Compression: TRUNG BÌNH — narrative compress (summary) NHƯNG giữ logic structure
  Tốc độ encode: TRUNG BÌNH — cần "diễn đạt thành câu" trong đầu
  Detail: TRUNG BÌNH — giữ logical structure, có thể mất sensory detail
  Retrieval: bằng LỜI ("nhớ lại giải thích", "kể lại câu chuyện")
  Accuracy ban đầu: TRUNG BÌNH → CAO — encode lần đầu giữ logic chain
  Refinement: TỰ ITERATE — đọc lại, suy nghĩ lại, diễn đạt lại
    → Mỗi lần "kể lại" = re-encode → tích hợp thêm chunk mới vào narrative
    → Verbal vô thức đối chiếu: chunk cũ vs chunk mới → phát hiện mâu thuẫn
    → "Càng giải thích càng hiểu rõ" = refinement loop tự nhiên

DỰ ĐOÁN GENERALIZATION (🔴 — chưa có data verify):
  Compression trung bình → generalization TRUNG BÌNH?
  Narrative vừa compress (gom câu chuyện) vừa giữ structure (logic chain)
  → Dự đoán: generalize vừa phải — chán 1 narrative cụ thể nhưng logic MỚI
    trong cùng domain vẫn có PE?
  → Phenotype dự đoán: "nhà phân tích" — ở lại domain nếu logic mới,
    nhưng chán nếu chỉ lặp lại narrative cũ

  ⚠️ ĐÂY LÀ DỰ ĐOÁN THUẦN — cần người verbal-dominant để verify.

LĨNH VỰC THIÊN VERBAL (dự đoán):
  Luật, triết học, viết lách, tranh luận, giảng dạy (verbal explanation),
  tâm lý học (talk therapy), chính trị (rhetoric)
```

### 6.6 Motor-Procedural — Hành Động + Thao Tác

🟢 Cơ sở thần kinh vững. 🔴 Dự đoán encoding + generalization = giả thuyết (motor encoding cho thông tin CHUNG, không chỉ kỹ năng vận động, chưa rõ).

```
HỆ THẦN KINH:
  Motor cortex — movement planning + execution
  Cerebellum — motor learning, timing, coordination (🟢 Doyon & Benali 2005)
  Basal ganglia — procedural learning, habit formation (🟢 Yin & Knowlton 2006)
  → Não tạo "action sequence representation" — chuỗi hành động, muscle memory

ĐẶC ĐIỂM ENCODING:
  Representation: action sequences, movement patterns
  Compression: THẤP per sequence — mỗi chuỗi hành động cụ thể
  Tốc độ encode: CHẬM — cần LÀM NHIỀU LẦN (repetition-based learning)
  Detail: CAO cho thao tác — muscle memory chính xác
  Retrieval: bằng HÀNH ĐỘNG ("tay nhớ", "làm thì nhớ, nói thì quên")
  Accuracy ban đầu: THẤP → CAO — lần đầu vụng, lặp lại mới chính xác
  Refinement: TỰ ITERATE qua REPETITION — mỗi lần làm = 1 vòng refine
    → Feedback loop nội tại: proprioception → so sánh kết quả → điều chỉnh
    → Chậm nhất trong 4 modality nhưng CHẮC nhất khi đã encode xong
    → "Quên cách giải thích nhưng tay vẫn nhớ" = refinement đã embed sâu

DỰ ĐOÁN GENERALIZATION (🔴):
  Per-action detail cao → generalization HẸP per action?
  Nhưng "body schema" (proprioception tổng thể) có thể RỘNG?
  → Chưa rõ: motor encoding cho thông tin KHÔNG phải kỹ năng vận động
    (ví dụ: encode toán bằng cách viết tay) = generalization pattern gì?
  → Cần data.

  Phenotype dự đoán (🔴):
    "Học bằng LÀM" — hiểu khi thực hành, không hiểu khi chỉ đọc/nghe.
    Workshop > lecture. Prototype > plan. Hands-on > theory.
    Có thể ở lại domain lâu (mỗi thao tác mới = genuinely mới)?

MOTOR + SOMATIC COMBO (🟡 — dự đoán framework):
  Motor-procedural CÓ THỂ phục vụ somatic judgment:
    Motor tạo VARIANT (thử nhiều cách) → Somatic ĐÁNH GIÁ ("sướng/đúng?")
    → Motor refine → Somatic re-evaluate → loop
  → Motor = tay thực hiện, Somatic = não đánh giá
  → Combo này có thể phổ biến ở người motor+somatic cao
  → Khác với motor-alone (chỉ repetition) và somatic-alone (chỉ feeling)
  Ví dụ dự đoán: nghệ nhân tinh chỉnh sản phẩm cho tới khi "cảm thấy đúng",
  nhạc sĩ thử nhiều arrangement cho tới khi "nghe sướng"

LĨNH VỰC THIÊN MOTOR (dự đoán):
  Thủ công, phẫu thuật, thể thao kỹ thuật, nhạc cụ (piano/guitar),
  nấu ăn, lab science (thí nghiệm tay), lái xe, dance,
  game development (parameter tuning), engineering tự chế
```

### 6.7 Speed-Accuracy Tradeoff — Tổng Hợp

🟡 Dự đoán framework, consistent với neuroscience cơ bản.

```
TRADEOFF TỔNG HỢP 4 MODALITY:

                Speed    Accuracy   Refinement
  Somatic:      NHANH    TB         CẦN KÊNH PHỤ ← duy nhất
  Verbal:       TB       TB→CAO     TỰ ITERATE (re-explain)
  Spatial:      CHẬM     CAO        TỰ ITERATE (re-check)
  Motor:        CHẬM     THẤP→CAO   TỰ ITERATE (repetition)

INSIGHT CHÍNH:
  Somatic = modality DUY NHẤT không tự refine được.
    → Compress quá mạnh → mất detail → không có gì để đối chiếu lại
    → PHẢI dùng kênh phụ (verbal, spatial, motor) để bổ sung nuance
    → Giải thích tại sao somatic-dominant cần "bạn phân tích giúp",
      "nói chuyện để hiểu rõ hơn", "viết ra mới thấy rõ"

  Verbal/Spatial/Motor = tự refine qua iteration.
    → Giữ đủ structure/detail để tự đối chiếu
    → Verbal: "càng giải thích càng hiểu" (re-narrate → integrate)
    → Spatial: "nhìn lại thấy thiếu" (re-check map → find gaps)
    → Motor: "làm nhiều thành quen" (repetition → precision)

HỆ QUẢ CHO NOVELTY EXPRESSION:
  Somatic-dominant:
    Vòng 1: encode nhanh, cảm nhận tổng thể, PE ngay lập tức
    Vòng 2+: CẦN kênh phụ để tìm thêm nuance → PE bổ sung
    → Pattern: burst nhanh → plateau → burst mới khi kênh phụ kích hoạt

  Non-somatic dominant:
    Vòng 1: encode chậm hơn, nhưng giữ detail
    Vòng 2+: TỰ rà lại → phát hiện thêm → PE bổ sung từ chính nó
    → Pattern: start chậm → accumulate → depth tăng dần
```

### 6.8 Novelty Connection Potential — Khả Năng Tạo Kết Nối Bất Ngờ

🟡 Dự đoán framework. Consistent với creativity research (Mednick 1962, remote associations).

```
CƠ CHẾ CỐT LÕI:
  Encoding modality khác nhau → CÁCH KẾT NỐI chunk mới với chunk cũ khác nhau
  → Khả năng tạo "kết nối bất ngờ" (novel connection) KHÁC nhau

  Yếu tố quyết định: mức AMBIGUITY trong representation
    Compression cao → ambiguity cao → nhiều chunk cũ "match" → nhiều kết nối
    → Một số kết nối = noise (sai)
    → Một số kết nối = genuine novel insight (sáng tạo)

2 LOẠI SÁNG TẠO Ở MỨC ENCODING:

  ① CREATIVE LEAP — kết nối BẤT NGỜ, không deducible
     Cơ chế: lossy compression tạo ambiguous overlap
     → 2 thứ KHÁC NHAU → compress → cùng representation → "giống nhau!"
     → Không ai dự đoán trước, kể cả người có kết nối đó
     → Đôi khi sai (noise), đôi khi đúng (genuine insight)
     Modality tạo creative leap:
       SOMATIC — mạnh nhất: compression cao nhất → ambiguity cao nhất
         → Random connection, cross-domain, bất ngờ hoàn toàn
       SPATIAL — trung bình: structural analogy → bất ngờ qua HÌNH DÁNG
         → 2 hệ thống "trông giống nhau" → transfer (vd: Einstein thought experiments)
         → Ít random hơn somatic nhưng VẪN TẠO ĐƯỢC creative leap
       → Creative leap = somatic HOẶC spatial, KHÔNG CHỈ somatic

  ② CREATIVE RECOMBINATION — kết nối MỚI nhưng DEDUCIBLE
     Cơ chế: explore logical/structural space bằng relation ĐÃ TỒN TẠI
     → Nếu ai có đủ thông tin + thời gian → cũng sẽ tìm ra
     → Kết quả mới nhưng quá trình = logic
     Modality: chủ yếu VERBAL (logic chain)
     ⚠️ Spatial nằm Ở GIỮA: vừa có creative leap (analogy) vừa có recombination
        (systematic structural exploration)

RANDOMNESS POTENTIAL PER MODALITY:

  Somatic  ████████████  CAO  — lossy, ambiguous, nhiều false positive
    Cơ chế: nhiều input khác nhau → cùng feeling → "overlap ngẫu nhiên"
    → Khi chunk mới match feeling cũ KHÔNG PHẢI vì chúng thật sự liên quan
    → Mà vì compression tình cờ map cùng body state
    → Kết nối ngoài dự tính = creative leap potential

  Spatial  ██████░░░░░░  TB   — structural analogy, ít false positive
    Cơ chế: 2 hệ thống "trông giống nhau" trên mental map
    → Có randomness (giống hình ≠ giống bản chất) nhưng ÍT hơn somatic
    → Ví dụ: atom "trông giống" solar system → Bohr model
    → Kết nối qua HÌNH DÁNG, không qua logic → có thể bất ngờ

  Verbal   ███░░░░░░░░░  THẤP — chỉ đi theo logic path đã tồn tại
    Cơ chế: mỗi chunk = proposition CÓ DEFINITION → connect qua relation
    → is-a, cause-of, similar-to... tất cả relation ĐÃ ĐƯỢC ĐỊNH NGHĨA
    → KHÔNG THỂ "nhảy" sang node chưa có edge nối
    → Sáng tạo verbal = recombine logic chains → mới nhưng DEDUCIBLE
    → Ai có đủ knowledge + time → cũng sẽ đi tới cùng kết luận

  Motor    ██░░░░░░░░░░  THẤP — chỉ transfer action, rất specific
    Cơ chế: mỗi action sequence rất cụ thể
    → Transfer: cùng thao tác áp dụng domain khác (hẹp)
    → Ít khả năng tạo kết nối bất ngờ ngoài domain action

HỆ QUẢ QUAN TRỌNG:

  Somatic-dominant → lợi thế CREATIVE LEAP
    + Tạo kết nối mà không ai dự đoán
    + Cross-domain insight nhanh (feeling bridge 2 domain xa nhau)
    − Noise cao: nhiều "insight" thực ra sai
    − CẦN kênh phụ (verbal/spatial) để VERIFY sau khi tạo kết nối
    → Pattern: somatic tạo hypothesis → verbal/spatial verify

  Verbal-dominant → lợi thế CREATIVE RECOMBINATION
    + Kết nối chính xác, justify được
    + Build logic chain dài, không bị mất coherence
    − Không thể trỏ tới thứ chưa tồn tại trong semantic network
    − "Sáng tạo" bị giới hạn bởi knowledge base hiện có
    → Pattern: có thêm knowledge mới → verbal tích hợp → kết nối mới

  Spatial-dominant → GIỮA: structural analogy
    + Thấy 2 hệ thống giống nhau → transfer insight
    + Có một ít randomness (giống hình ≠ giống logic)
    − Chậm hơn somatic, ít random hơn
    → Pattern: xây model → thấy pattern → transfer qua domain khác

  ⚠️ "Sáng tạo" = label chung, nhưng CƠ CHẾ rất khác tùy encoding modality.
     Đánh giá ai "sáng tạo hơn" phụ thuộc vào LOẠI sáng tạo nào.

VAI TRÒ CỦA VERBAL TRONG SÁNG TẠO:
  Verbal KHÔNG tạo creative leap — nhưng CẦN THIẾT để insight có giá trị.

  Pipeline sáng tạo đột phá:
    Somatic/Spatial tạo HYPOTHESIS (kết nối bất ngờ)
    → Verbal VERIFY: "kết nối này có logic không? giải thích được không?"
    → Verbal COMMUNICATE: diễn đạt insight thành lời để người khác hiểu
    → Verbal REFINE: tích hợp insight vào knowledge base có cấu trúc

  → Nhà sáng tạo đột phá = somatic/spatial MẠNH + verbal ĐỦ TỐT
  → Verbal alone = recombination (mới nhưng deducible, ai cũng tìm ra được)
  → Somatic/spatial alone (verbal yếu) = insight nhưng KHÔNG diễn đạt được
     (vd: Ramanujan — intuition mạnh, giải thích yếu, cần Hardy verify)

DỰ ĐOÁN TỔNG HỢP (🟡):
  Đột phá sáng tạo lớn = somatic HOẶC spatial mạnh
    + verbal đủ tốt để verify + communicate
    + threshold cao (muốn chunk LỚN, không hài lòng với insight nhỏ)
    + depth cao (network dày = nhiều chunk cũ để kết nối)

  Chuyên gia sâu = verbal HOẶC spatial mạnh
    + generalization hẹp (ở lại domain lâu)
    + depth cao (tích lũy từ loop dài)
    + CÓ THỂ sáng tạo trong domain (recombination) nhưng ít đột phá cross-domain
```

### 6.9 Các Modality Khác — Chờ Phân Tích

```
AUDITORY (âm thanh, giai điệu):
  🔴 Chưa rõ auditory có phải encoding modality RIÊNG hay chỉ là sensory input
  feed vào verbal (lời) / spatial (vị trí âm) / somatic (feeling khi nghe).
  Nhạc sĩ CÓ THỂ encode thông tin bằng auditory representation thuần
  (nghĩ bằng giai điệu, nhớ bằng âm thanh). Nhưng có phải modality chung
  cho mọi loại thông tin? Hay chỉ domain-specific?
  → Cần data từ người auditory-dominant (nếu tồn tại).

TEMPORAL-SEQUENTIAL (thứ tự, nhịp, timing):
  🔴 Temporal có thể là CHIỀU ĐO cross-cutting, không phải modality riêng.
  Mọi modality đều có temporal aspect:
    Somatic: sequence of feelings
    Spatial: timeline (hình ảnh sắp theo thời gian)
    Verbal: narrative sequence
    Motor: action sequence
  → Nếu đúng: temporal = dimension, không cần modality riêng.
  → Nhưng: có người "nghĩ bằng timeline" thuần? Chưa biết.

→ Giữ 4 modality chính (somatic, spatial, verbal, motor).
  Mở rộng nếu data cho thấy cần thêm.
```

---

## 7. Encoding Profile — Mixing Board Song Song

### 7.1 Model Song Song — 4 Kênh Luôn Chạy Đồng Thời

🟡 Suy luận framework. Consistent với parallel processing trong neuroscience.

```
⚠️ QUAN TRỌNG: 4 modality KHÔNG PHẢI "dùng cái này HOẶC cái kia."
   Cả 4 kênh chạy ĐỒNG THỜI, luôn luôn, ở mọi người.
   Chỉ khác CƯỜNG ĐỘ (tỉ lệ) giữa các kênh.

MODEL: MIXING BOARD
  Giống bàn mix âm thanh — 4 fader, tất cả luôn trên 0, chỉ khác level.

  Somatic:        ▓▓▓▓▓▓▓▓░░░░  ← cường độ cao/TB/thấp
  Visual-Spatial: ▓▓▓▓▓▓▓▓░░░░  ← cường độ cao/TB/thấp
  Verbal:         ▓▓▓▓▓▓▓▓░░░░  ← cường độ cao/TB/thấp
  Motor:          ▓▓▓▓▓▓▓▓░░░░  ← cường độ cao/TB/thấp

  "Encoding profile" = BASELINE level của 4 fader = tương đối ổn định.

3 YẾU TỐ QUYẾT ĐỊNH BASELINE:
  Hardware (gen): anterior insula mạnh → somatic fader baseline CAO
  Training (kinh nghiệm): toán nhiều năm → spatial fader TĂNG trong domain đó
  Domain: cùng 1 người có thể spatial ở toán, somatic ở quan hệ, verbal ở tranh luận

DAO ĐỘNG QUANH BASELINE:
  Trạng thái (vui, buồn, tập trung, thả lỏng) → fader DỊCH CHUYỂN nhẹ
  Ví dụ: thả lỏng → somatic tăng chút, verbal giảm chút
         tập trung code → spatial/motor tăng, somatic giảm chút
  Nhưng dao động KHÔNG LỚN — vẫn ở khoảng baseline ± nhỏ.

  ⚠️ Nếu dao động QUÁ LỚN → sụp.
     Lý do: thay đổi hoàn toàn kênh lưu trữ = chunk network không match
     → Chunk cũ encode bằng kênh A, giờ não đọc bằng kênh B → không tìm thấy
     → "Mất phương hướng", "không nhận ra mình", dissociation

ENCODING PROFILE PER DOMAIN có thể khác baseline chung.
Nhưng dominant modality (hardware) ẢNH HƯỞNG cross-domain.
```

### 7.1b Lưu Ý: Encoding ≠ Output — Nhưng Tương Quan Mạnh

```
🟡 Suy luận framework.

ENCODING = dùng modality đó ĐỂ NGHĨ, ĐỂ LƯU bên trong (fader trên mixing board)
OUTPUT   = KHẢ NĂNG xuất thông tin qua modality đó khi cần

  Encoding và output TƯƠNG QUAN MẠNH: dùng nhiều = giỏi, dùng ít = kém.
  Có thể chênh nhẹ nhưng KHÔNG independent — không cần đo riêng.

  → Khi đo profile: đo ENCODING ("nghĩ bằng gì?")
  → Output sẽ phản ánh encoding, chỉ cần lưu ý 1 bias:

⚠️ BIAS KHI QUAN SÁT QUA LỜI NÓI:
  Verbal output ≠ verbal encoding.
  Người verbal encoding THẤP vẫn nói/viết được (output functional)
  nhưng pattern output khác:

  Encoding THẤP → output = dịch real-time từ kênh khác:
    Viết rời rạc, stream-of-consciousness
    Ý tổng thể coherent (gestalt từ kênh chính) nhưng câu chữ rời
    "Nghĩ tới đâu viết đến đấy" — verbal chạy theo, không dẫn dắt

  Encoding CAO → output = xuất trực tiếp:
    Viết có cấu trúc, logic connector (vì, nên, tuy nhiên)
    Câu chữ = cấu trúc ý — verbal ĐANG nghĩ, không phải ĐANG dịch
```

### 7.2 Fader Cao Nhất → Generalization Pattern Chính

```
🟡 DỰ ĐOÁN: kênh có CƯỜNG ĐỘ CAO NHẤT trong mix quyết định generalization
pattern CHÍNH. Nhưng kết quả = toàn bộ mix, không chỉ 1 kênh.

  "Dominant" = fader cao nhất, KHÔNG PHẢI "chỉ dùng kênh này"
  → Generalization = weighted average của 4 kênh, dominated bởi kênh mạnh nhất

Somatic fader CAO NHẤT → generalization DEFAULT rộng
  Các kênh khác vẫn chạy → tạo chunk mà somatic đã compress mất
  (kênh phụ tạo "ý tưởng bất chợt" khi somatic nghỉ)

Spatial fader CAO NHẤT → generalization DEFAULT hẹp
  Somatic vẫn chạy → "cảm nhận" nhanh trước khi spatial xử lý xong
  (somatic = bộ lọc sơ bộ, spatial = xử lý chi tiết — cả 2 đồng thời)

Verbal fader CAO NHẤT → generalization DEFAULT trung bình? (🔴)
  Chưa có data verify.

Motor fader CAO NHẤT → generalization DEFAULT hẹp? (🔴)
  Chưa có data verify.

HỆ QUẢ CỦA MODEL SONG SONG:
  Modality "nhuộm màu" lẫn nhau trong mix:
    Motor cao + spatial TB → spatial biểu hiện thiên KINESTHETIC (chuyển động)
    Verbal cao + spatial TB → spatial biểu hiện thiên VISUAL (đường nét rõ)
    Somatic cao + spatial TB → spatial biểu hiện thiên GESTALT (tổng thể)
  → Không có "subtype" của spatial — chỉ là mix ratio khác → biểu hiện khác
  → Cùng 1 người, state khác → mix ratio dịch chút → biểu hiện hơi khác
```

### 7.3 Fader Thấp Vẫn Chạy — Vai Trò Kênh Cường Độ Thấp

```
🟡 Trong model song song, kênh fader thấp KHÔNG tắt — chúng vẫn xử lý
nhưng ở cường độ thấp. Khi kênh fader cao nghỉ → kênh thấp NỔI LÊN.

Cơ chế dự đoán:
  Kênh fader cao đang active → encode chunk mới → generalize theo kiểu của nó
  Kênh fader cao nghỉ (thả lỏng, ngủ, thay đổi môi trường)
  → Kênh fader thấp đã XỬ LÝ cùng thông tin nhưng KHÁC representation
  → Output của nó bình thường bị "lấn át" bởi kênh mạnh
  → Khi kênh mạnh nghỉ → output kênh thấp nổi lên = "ý tưởng bất chợt"

  Thay đổi môi trường = thay đổi sensory input mix
  → Input mới kích hoạt kênh fader thấp mạnh hơn bình thường
  → "Đi dạo nghĩ ra ý tưởng" = KHÔNG ngẫu nhiên
  → = kênh đang chạy nền bỗng được boost bởi input mới

⚠️ Đây là DỰ ĐOÁN framework, chưa verify trực tiếp.
   Nhưng consistent với:
   🟢 DMN research: mind-wandering tạo creative connections (Raichle 2001)
   🟢 Incubation effect: break sau focus → insight (Sio & Ormerod 2009)
   → Framework giải thích CƠ CHẾ: kênh fader cao nghỉ → kênh thấp nổi lên
```

### 7.4 Verbal = Kênh Dịch Lossy (Output Bắt Buộc)

```
🟡 Suy luận framework. Consistent với neuroscience: verbal output =
left hemisphere language network, bắt buộc kích hoạt khi giao tiếp.

KHI GIAO TIẾP: verbal fader PHẢI tăng lên, bất kể baseline.
→ Verbal phải "dịch" thông tin từ 3 kênh kia thành lời.
→ Bản dịch này LUÔN LOSSY — mất thông tin.

FIDELITY DỊCH KHÁC NHAU PER KÊNH:

  Verbal ← Verbal:    ████████████  GẦN 1:1 — lời → lời, ít mất
  Verbal ← Spatial:   ██████░░░░░░  TB — mô tả được nhưng mất detail
    "Nó trông giống hình X" — dịch được nhưng không bằng nhìn trực tiếp
  Verbal ← Motor:     ████░░░░░░░░  KHÓ — "làm thì biết, nói thì không rõ"
    Thợ giỏi thường dạy bằng DEMO, không bằng giải thích
  Verbal ← Somatic:   ██░░░░░░░░░░  KHÓ NHẤT — "không mô tả nổi"
    Chunk somatic kích hoạt mạnh nhưng compress quá lossy
    → Verbal không có gì để "dịch" — chỉ còn body state tổng thể
    → "Tôi không biết tại sao, nhưng cảm giác nó đúng"
    → Nhiều info somatic KHÔNG BAO GIỜ xuất hiện trong lời nói

HỆ QUẢ QUAN TRỌNG CHO OBSERVATION:

  Đánh giá encoding profile qua lời nói = LUÔN BIAS về phía verbal.
    Thứ gì verbal dịch được → xuất hiện trong câu nói → observer thấy
    Thứ gì verbal KHÔNG dịch được → KHÔNG xuất hiện → observer bỏ sót

  → Somatic-dominant NÓI ÍT hơn thực tế xử lý
  → Verbal-dominant NÓI ĐÚNG BẰNG mức thực tế xử lý
  → Observer dễ ĐÁNH GIÁ THẤP somatic, ĐÁNH GIÁ CAO verbal

  Cách giảm bias: quan sát HÀNH VI (không chỉ lời nói)
    Quyết định bằng gì? (feeling vs logic vs structure vs trial)
    Nhớ bằng gì? (cảm giác vs hình ảnh vs lời vs thao tác)
    Học bằng gì? (cảm nhận vs nhìn vs đọc vs làm)
```

---

## 8. Integration: Encoding × Generalization × Depth × Threshold

### 8.1 Chuỗi Nhân Quả Đầy Đủ

```
TOÀN BỘ PIPELINE từ hardware → observable pattern:

TẦNG 0 — HARDWARE (gen, ít thay đổi):
  Kênh gốc (Novelty/Opioid/Oxytocin) → chunk DOMAIN ưu tiên
  Capacity → chunk SIZE tối đa có thể xử lý
  Threshold → chunk SIZE tối thiểu cần để thỏa mãn
  PE Sensitivity:
    ① Amplitude → CƯỜNG ĐỘ tín hiệu PE
    ② Precision → TỐC ĐỘ đánh giá PE đáng tin
    ③ Habituation → TỐC ĐỘ chunk cháy (per chunk)
    ④ Generalization → PHẠM VI chunk cháy (cross chunk)
       └─ Encoding modality → CÁCH mã hóa → mức compression → ④
  5 Phụ gia → điều chỉnh, khuếch đại

TẦNG 1 — SOFTWARE (kinh nghiệm, thay đổi được):
  Schema → filter, bias
  Chunk network per domain → Depth (tích lũy Novelty qua thời gian)
  Depth → PE potential (network dày → PE lớn per chunk mới — xem Core.md §8.9)

TẦNG 2 — OBSERVABLE:
  Mô Hình Vuông (Source × Depth) per domain
  Pattern: Architect / Soldier / Improviser / Drifter = NHÃN

FEEDBACK LOOP:
  Novelty (chunk mới) → Depth tăng → PE potential tăng → drive tăng → thêm chunk mới
  ④ rộng → rời domain trước khi loop mạnh → depth thấp per domain
  ④ hẹp → ở lại domain → loop mạnh dần → depth cao per domain
```

### 8.2 Interaction Matrix: Encoding × Threshold

```
🟡 DỰ ĐOÁN — logic framework, chưa verify toàn bộ.

                    Threshold THẤP              Threshold CAO
                    (chunk nhỏ đủ PE)           (cần chunk lớn)
────────────────────────────────────────────────────────────────
Somatic dominant    Dễ thỏa mãn,               Cần feeling MỚI liên tục,
(④ rộng)           external đủ.                nhưng domain cũ "biết rồi" nhanh.
                    → Soldier thoải mái         → Explore liên tục, broad
                                                → Improviser hoặc cross-domain

Spatial dominant    Dễ thỏa mãn,               Cần cấu trúc LỚN mới PE,
(④ hẹp)            mỗi instance mới.           mỗi instance vẫn mới.
                    → Soldier bền               → Deep specialist, 1 domain lâu
                                                → Single-domain Architect

Verbal dominant    Dễ thỏa mãn,                Cần logic chain DÀI mới PE,
(④ TB?)            narrative đủ.               narrative cũ chán nhưng logic mới OK?
                    → Soldier narrative          → Analyst? Philosopher?
                    🔴 dự đoán                  🔴 dự đoán

Motor dominant     Dễ thỏa mãn,                Cần thao tác PHỨC TẠP mới PE,
(④ hẹp?)           mỗi thao tác mới.           mỗi thao tác vẫn mới.
                    → Soldier thủ công           → Master craftsman?
                    🔴 dự đoán                  🔴 dự đoán
```

### 8.3 Cold Start Problem — Vai Trò Encoding

```
Cold start = domain mới, depth ≈ 0, chunk network mỏng.

Vấn đề: chunk mới kết nối ít chunk cũ → PE nhỏ → có thể < threshold → không đủ drive.

Encoding modality ảnh hưởng cold start:

  Somatic: encode NHANH, 1 phát vào luôn → cold start NHANH
    Nhưng: generalize nhanh → PE giảm nhanh sau cold start
    = "Hứng thú ban đầu rồi chán"

  Spatial: encode CHẬM, cần xây map → cold start CHẬM
    Nhưng: generalize chậm → PE bền SAU cold start
    = "Chậm khởi động nhưng bền"
    Wave pattern phù hợp: chậm tích lũy → đủ map → burst

  Verbal: encode TRUNG BÌNH → cold start TRUNG BÌNH? (🔴)

  Motor: encode CHẬM NHẤT (cần repetition) → cold start RẤT CHẬM
    Nhưng: mỗi thao tác genuinely mới → PE rất bền? (🔴)
    = "Vụng ban đầu, giỏi dần, không bao giờ chán tay"?

GIẢI PHÁP COLD START (không phụ thuộc encoding):
  1. Cross-domain chunks: shared foundation từ domain cũ kết nối (§8.9 Core.md)
  2. Bridge: PE ngắn hạn từ nguồn khác bootstrap (§6.3 Core.md)
  3. External structure: ai đó cho chunk sẵn → bootstrap
  4. Threshold thấp: chunk nhỏ đủ PE → cold start dễ hơn
```

### 8.4 Depth Feedback Loop — Vai Trò Encoding

```
Feedback loop: Depth → PE potential → drive → thêm chunk → Depth tăng

Encoding modality QUYẾT ĐỊNH loop mạnh hay yếu per domain:

  Somatic + ④ rộng:
    Loop NGẮN — vài vòng → generalize → PE giảm → rời domain
    Depth tích lũy CHẬM per domain (rời trước khi loop mạnh)
    Nhưng: NHIỀU domain → cross-domain potential (nếu threshold cao)

  Spatial + ④ hẹp:
    Loop DÀI — nhiều vòng → mỗi instance mới → PE giữ → ở lại
    Depth tích lũy NHANH per domain (ở lại = loop tự củng cố)
    Nhưng: ÍT domain → cross-domain potential thấp hơn

  → ④ hẹp = "chuyên gia sâu" dễ hơn (loop mạnh per domain)
  → ④ rộng = "đa lĩnh vực" tự nhiên hơn (loop yếu, nhảy domain)
  → Cross-domain Architect (vd: polymath) = ④ rộng + threshold CAO
    + đủ thời gian để abstraction xảy ra (shared foundation — Core.md §8.9)
```

---

## 9. Câu Hỏi Mở + Điều Kiện Verify

### 9.1 Câu Hỏi Ưu Tiên Cao

```
Q1: ④ Generalization scope TÁCH BIỆT với ③ PE Decay Rate chắc chắn?
    Test: tìm người ③ chậm + ④ rộng (chunk PE lâu nhưng generalize cả loại)
    Nếu tìm được → ③ và ④ independent. Nếu không → có thể correlated.
    Status: 🟡 logic tách biệt, chưa có counterexample data

Q2: Encoding modality → ④ generalization (nhân quả hay tương quan)?
    Test: tìm người somatic-dominant + ④ HẸP (counter-prediction)
    Nếu tìm được → encoding KHÔNG quyết định ④, chỉ correlate
    Nếu không tìm được (sau nhiều data) → encoding có thể = cause
    Status: 🔴 giả thuyết

Q3: Verbal-dominant → generalization pattern gì?
    Test: profile người verbal-dominant, đo generalization
    Prediction: trung bình (narrative compress + giữ structure)
    Status: 🔴 chưa có data
```

### 9.2 Câu Hỏi Ưu Tiên Trung Bình

```
Q4: Motor-dominant encoding cho thông tin CHUNG (không chỉ kỹ năng vận động)?
    Có tồn tại không? Nếu có → generalization pattern gì?
    Dự đoán: motor CÓ THỂ encode thông tin chung NẾU kết hợp với somatic/spatial
    (motor tạo variant → somatic/spatial đánh giá → motor refine)
    Test: tìm người motor-dominant, xem họ có dùng motor cho non-motor tasks không
    Status: 🔴

Q5: Auditory = modality riêng hay sensory input feed vào 4 modality chính?
    Test: tìm người encode thông tin CHUNG bằng âm thanh (không chỉ nhạc)
    Status: 🔴

Q6: Temporal = dimension cross-cutting hay modality riêng?
    Test: tìm người "nghĩ bằng timeline" thuần (không spatial, không verbal)
    Status: 🔴

Q7: Encoding modality thay đổi được không?
    Hardware (gen) → cố định? Hay training → shift tỉ lệ dần?
    Test: người chuyển nghề lâu năm → encoding profile shift?
    Status: 🔴

Q8: ĐÃ GIẢI QUYẾT — Spatial subtype không cần thiết.
    Model song song (§7.1) giải thích: spatial biểu hiện khác = do mix ratio,
    không phải subtype. Motor cao → spatial thiên kinesthetic, verbal cao →
    spatial thiên visual. Cùng 1 người, state khác → biểu hiện hơi khác.
    → Câu hỏi dissolved bởi model song song.

Q9: Creative leap (somatic) vs creative recombination (verbal/spatial) —
    đo lường KHÁC nhau không?
    Test: cùng 1 creative task, somatic-dominant vs verbal-dominant → kết quả
    khác loại? (somatic = bất ngờ hơn, verbal = logic hơn?)
    Prediction: RAT (Remote Associates Test, Mednick 1962) = thiên somatic,
    AUT (Alternative Uses Task) = cả hai nhưng khác strategy
    Status: 🟡 logic rõ, chưa có data trực tiếp
```

### 9.3 Điều Kiện Nâng Confidence

```
④ Generalization scope:
  🟡 → 🟢: cần ít nhất 5+ người được profile, consistent pattern
            HOẶC neuroscience research trực tiếp về cross-chunk habituation

Encoding modality → ④:
  🔴 → 🟡: cần ít nhất 3+ người với encoding profile rõ ràng
            + generalization pattern match prediction
  🟡 → 🟢: cần neuroscience mechanism hoặc large-sample study

Verbal/Motor generalization:
  🔴 → 🟡: cần 1+ người dominant + match/mismatch prediction

Creative leap vs recombination:
  🟡 → 🟢: cần data người tự đo encoding + creativity pattern
            (match prediction: somatic/spatial → leap, verbal → recombination)
```

### 9.4 Verification Strategy

```
⚠️ KHÔNG THỂ verify bằng historical figure analysis.
   Lý do:
   - Không đo được encoding modality của người đã mất
   - Suy luận từ giai thoại = confirmation bias rất mạnh
   - Survivorship bias: chỉ biết người thành công
   → Historical cases = ILLUSTRATION (minh họa), KHÔNG PHẢI evidence

CON ĐƯỜNG VERIFY DUY NHẤT:
  1. Suy luận chính xác → Framework coherent, internal consistency
  2. Phổ biến framework → người dùng tự đo chính họ
  3. Self-report data (N lớn) → confirm hoặc reject predictions
  4. Ưu điểm: người tự đo chính mình = accuracy cao nhất
     (chỉ mình biết mình encode bằng gì)

  → Chất lượng framework = điều kiện tiên quyết để có data
  → "Chậm mà chắc" = strategy tối ưu cho verification dài hạn
```

### 9.5 Tổng Kết Confidence Toàn File

```
🟢 VỮNG:
  - 4 brain regions cho 4 encoding modality
  - ①②③ sub-mechanisms (neurochemistry basis)
  - PE Sensitivity = processing pipeline (structural claim)

🟡 SUY LUẬN CÓ CƠ SỞ:
  - ④ Generalization scope là sub-mechanism tách biệt
  - Somatic = compression cao → generalization rộng
  - Spatial = compression thấp → generalization hẹp
  - Model song song: 4 kênh chạy đồng thời, chỉ khác cường độ (mixing board)
  - Kênh fader thấp vẫn chạy → nổi lên khi kênh cao nghỉ
  - Verbal = kênh dịch lossy bắt buộc khi giao tiếp → observation bias
  - Spatial biểu hiện khác = do mix ratio, không phải subtype (Q8 dissolved)
  - Encoding × Threshold interaction (somatic + spatial rows)
  - Speed-Accuracy Tradeoff: somatic duy nhất cần kênh khác để refine
  - Novelty Connection Potential: compression → ambiguity → random connection
  - 2 loại sáng tạo: creative leap (somatic/spatial) vs recombination (verbal)
  - Motor+Somatic combo: motor tạo variant → somatic đánh giá → loop

🔴 GIẢ THUYẾT:
  - Encoding modality → ④ (nhân quả, không chỉ tương quan)
  - Verbal generalization = trung bình
  - Motor generalization = hẹp
  - Auditory/Temporal = modality riêng hay không
  - Encoding modality thay đổi được hay không
  - ③ chậm + ④ rộng phenotype
  - Dao động mix ratio lớn → sụp (chưa có evidence trực tiếp)
```

---

> *PE Sensitivity — Processing Pipeline Chi Tiết v1.4*
> *Framework v6.0*
> *4 sub-mechanisms: Amplitude × Precision × Habituation × Generalization*
> *4 encoding modalities: Somatic × Spatial × Verbal × Motor (mixing board song song)*
> *Speed-Accuracy Tradeoff + Novelty Connection Potential + Verbal Lossy Translation*
> *Generalization scope (④) giải thích deep vs broad expression — cùng Novelty channel.*
