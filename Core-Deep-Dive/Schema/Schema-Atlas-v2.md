# Schema Atlas v2 — Bản Đồ Schema

> **Trạng thái:** DRAFT — viết lại hoàn toàn theo Architecture v7.5
> **Ngày:** 2026-03-25
> **Mục đích:** Phân tích toàn diện Schema — patterns hành vi xuyên suốt Body→Imagine
> **Reference:** Architecture-v7.5-Draft.md, PFC-Analysis.md, Imagination-Analysis-v2.md,
> Change-Readiness.md, Modality-Analysis.md
> **⚠️ Mỗi phần riêng = established research, gom lại = framework hypothesis**

---

## 1. Schema Là Gì

```
DEFINE:
  Schema = PATTERN dao động neuron đã ổn định (compiled)
  → Nhóm neurons fire ĐỒNG BỘ theo pattern CỤ THỂ
  → Mỗi schema = 1 "bài nhạc" mà dàn neurons đã thuộc
  → Khi trigger → neurons TỰ fire theo pattern → hành vi TỰ ĐỘNG

  Ví dụ:
    "Đi bộ" = schema: motor neurons fire theo pattern bước chân đã compiled
    "Sợ chó" = schema: amygdala + somatic neurons fire pattern "threat" khi thấy chó
    "Nấu cơm" = schema: motor + visual + memory neurons fire pattern nấu
    "Tôi vô giá trị" = schema: deep compiled pattern ảnh hưởng MỌI hành vi

  Schema KHÔNG phải "suy nghĩ":
    → "Suy nghĩ" = verbal label (chữ trong đầu) = chỉ 1 PHẦN rất NHỎ
    → Schema = TOÀN BỘ pattern (body + motor + visual + somatic + emotional + verbal)
    → "Sợ chó" bằng LỜI = verbal
    → "Sợ chó" bằng BODY = tim đập, lùi bước, mồ hôi, cơ căng = schema THẬT

  Schema = SOFTWARE chạy trên HARDWARE (neurons):
    → Hardware = neurons + synapses + receptors (cố định, thay đổi chậm)
    → Software = patterns dao động (thay đổi được, compile/update)
    → Cùng hardware → KHÁC schema → KHÁC hành vi
    → = 2 người cùng não "giống nhau" → schemas KHÁC → sống KHÁC hoàn toàn

  METAPHOR ÂM NHẠC — hình dung cách schema tương tác:
    → Schema = bài nhạc (nhiều nhạc cụ chơi CÙNG LÚC = parallel)
    → Chunk = track nhạc cụ (guitar line, drum pattern = đơn vị ghép)
    → Cải tiến = đổi từng note → nghe lại → hay hơn? → giữ/bỏ
    → Trauma = bài nhạc kinh dị XEN VÀO bài đang nghe (cross-contamination)
    → Novelty = viết bài MỚI từ tracks có sẵn (cross-domain remix)
    → Schema tự chạy = earworm (bài dính trong đầu, không chủ động)
    → (Chi tiết + ví dụ: Schema-Example.md §7)
```

### 1.1 Chunk — Đơn Vị Nhỏ Nhất Của Schema

```
  Chunk = nhóm neurons NHỎ fire đồng bộ = 1 "mảnh" thông tin
  Schema = NHIỀU chunks kết nối = 1 pattern hoàn chỉnh

  Giống: chunk = GẠCH, schema = NGÔI NHÀ (nhiều gạch ghép lại)
  → 1 chunk: "màu đỏ" (visual neurons fire)
  → 1 chunk: "nóng" (somatic neurons fire)
  → 1 chunk: "nguy hiểm" (amygdala neurons fire)
  → Ghép: "lửa" = schema (3 chunks kết nối: đỏ + nóng + nguy hiểm)

  Chunk có thể MULTI-MODAL:
    → 1 chunk có thể fire ở NHIỀU vùng não cùng lúc
    → "Mẹ" = visual (mặt mẹ) + auditory (giọng mẹ) + somatic (ấm) + emotional (an toàn)
    → = 1 chunk nhưng TRẢI RỘNG nhiều modalities
    → Chunk càng nhiều modality → càng SÂU → càng khó mờ

  Chunk tạo từ 2 nguồn:
    → Vô thức: experience trực tiếp → neurons fire → chunk TỰ HÌNH THÀNH
    → PFC: imagine → draft → body check → chunk ĐƯỢC TẠO có chủ đích
    → Cả 2 đều tạo chunks → khác ở TỐC ĐỘ và CHẤT LƯỢNG
```

### 1.2 Schema KHÔNG THỂ Phân Tích Chính Xác

```
"Sao không phân tích chính xác schema từng người đi?"
→ KHÔNG THỂ. Tại sao:

  ① 86 tỷ neurons × ~100 nghìn tỷ connections = hệ thống quá lớn
     → Schema = patterns TRONG hệ thống này → không đọc trực tiếp
     → Giống: biết có 1 tỷ transistor → KHÔNG đọc được mã nguồn

  ② Schema = MULTI-MODAL (không chỉ "suy nghĩ")
     → Mỗi schema encoded ở NHIỀU modalities đồng thời
     → Ngôn ngữ chỉ capture verbal = ~1/6 schema thật
     → 2 người cùng "sợ chết" → schema thật KHÁC HOÀN TOÀN:
       A: "sợ mất người thân" (somatic: tim đập, trauma-based)
       B: "sợ vô nghĩa" (verbal: nghĩ nhiều, existential)

  ③ Schema SÂU = BODY ADAPTATION
     → Schema sâu ĐÃ embed vào body: cortisol baseline, muscle tension,
       gut state, sleep pattern → chính người đó CŨNG không biết

  ④ Schema THAY ĐỔI LIÊN TỤC → "chụp" lúc này → lúc sau đã khác

  ⑤ Khoa học hiện đại CHƯA ĐỦ CÔNG CỤ
     → fMRI thấy vùng não, KHÔNG thấy schema content
     → Behavioral tests thấy output, suy ngược pattern

  VẬY FRAMEWORK LÀM GÌ?
    → KHÔNG phân tích chính xác (impossible)
    → CÓ THỂ: nhận diện PATTERN (hành vi lặp lại = schema biểu hiện)
    → CÓ THỂ: ước lượng NHÓM (schema thuộc layer nào, channel nào)
    → CÓ THỂ: suggest HƯỚNG (body fix trước, rồi schema tự adjust)
    → = CÔNG CỤ NAVIGATE, không phải GPS chính xác
    → = "Công thức, không đáp án" — tool để TỰ KHÁM PHÁ
```

---

## 2. Schema Hình Thành — 2 Con Đường

```
Schema hình thành qua 2 con đường — CẢ HAI cần thiết:

CON ĐƯỜNG 1 — VÔ THỨC TỰ BUILD (không cần PFC):
  = Association learning: stimulus → body respond → schema TỰ ĐỘNG hình thành

  Ví dụ:
    Chạm lửa → nóng → schema "lửa = đau" (1 lần = đủ)
    Trẻ 3-4 tuổi build 160+ strategies MÀ PFC chỉ ~20%
    "Gut feeling" về người lạ → body evaluate → schema form VÔ THỨC

  Đặc điểm:
    → NHANH (1 experience CÓ THỂ đủ, đặc biệt nếu emotional mạnh)
    → KHÔNG TỐN PFC effort
    → NHƯNG: chỉ từ TRẢI NGHIỆM TRỰC TIẾP (phải tự gặp/làm/thấy)
    → Scope: TRONG domain đã trải nghiệm → KHÓ cross-domain

  Evidence: trẻ 0-4 tuổi PFC gần zero → VẪN build schemas phức tạp ✅


CON ĐƯỜNG 2 — PFC DRAFT + COMPILE (imagine):
  = PFC imagine scenario → body simulate → body check → compile nếu ok

  Ví dụ:
    "Nếu nói thẳng với sếp → sẽ thế nào?" → PFC simulate → decide
    Einstein thought experiment "cưỡi tia sáng" → draft → test → insight
    Lập kế hoạch → PFC draft nhiều scenario → chọn tốt nhất

  Đặc điểm:
    → CHẬM hơn (PFC draft → test → route = nhiều steps)
    → TỐN PFC effort (working memory load)
    → NHƯNG: từ IMAGINE — không cần trải nghiệm trực tiếp
    → PREDICT XA hơn (simulate tương lai)
    → AN TOÀN hơn (simulate hậu quả TRƯỚC)
    → CROSS-DOMAIN possible (PFC connect nhiều vùng)
    → Và: MỞ ACCESS domain trial-error KHÔNG THỂ tới
      (E=mc² không thể ra từ trial-error → chỉ imagine tới được)

  Evidence: người trưởng thành plan + predict = PFC active (fMRI) ✅


CẢ HAI CẦN MẠNH — thiếu 1 = bottleneck:
  Vô thức mạnh + PFC yếu: nhiều schemas cơ bản + ÍT predict xa
    → "Giỏi tay nhưng thiếu plan"
  PFC mạnh + vô thức yếu: draft hay nhưng KHÔNG verify
    → "Plan giỏi nhưng xa rời thực tế"
  CẢ HAI mạnh: nền RỘNG (vô thức) + đỉnh CAO (PFC) = expert/genius

GRADIENT hình thành (không binary):
  100% vô thức: reflex (chạm nóng → rụt) → trẻ sơ sinh
  Chủ yếu vô thức: thói quen (đi làm → quen đường) → daily
  50/50: skill mới (lái xe: PFC guide → vô thức compile) → learning
  Chủ yếu PFC: plan phức tạp (framework, kinh doanh) → expert
  100% PFC: KHÔNG TỒN TẠI (PFC luôn cần vô thức compute)


⚠️ VÔ THỨC RÁP BẰNG CHUNKS CÓ SẴN — KHÔNG PHÂN BIỆT TỐT/XẤU:

  Khi schema MỚI hình thành (vô thức = chính):
    → Vô thức tìm chunks KHỚP NHẤT với input hiện tại → RÁP
    → KHÔNG filter: chunk "tốt" hay chunk "trauma"
    → Chỉ care: pattern MATCH hay không → MATCH = dùng
    → = Chunks trauma CÓ THỂ bị ráp vào schema mới MÀ KHÔNG BIẾT

  Ví dụ — tình yêu (chi tiết: Schema-Example.md §1):
    Body feel "hồi hộp" khi gặp crush
    → Vô thức tìm chunk KHỚP "hồi hộp":
      Chunk [mẹ yêu → ấm → hồi hộp vui] → match ✅ (lành mạnh)
      Chunk [bố bỏ → sợ → hồi hộp sợ] → CŨNG match ✅ (trauma)
    → Vô thức KHÔNG phân biệt → ráp cả 2 vào schema tình yêu
    → = "Hồi hộp vì thích" vs "hồi hộp vì sợ bị bỏ" = CÙNG body sensation
    → = Schema tình yêu VÔ TÌNH chứa trauma chunks

  → = Schema mới KHÔNG BAO GIỜ "thuần khiết"
  → = Luôn ráp từ chunks CÓ SẴN → bao gồm CẢ trauma nếu có
  → = Đây là lý do "mỗi người yêu KHÁC dù gặp CÙNG người"
  → = Và lý do "luôn chọn nhầm người" = vô thức dùng trauma chunks match


⚠️ SCHEMA CŨ VÔ TÌNH ẢNH HƯỞNG SCHEMA MỚI (cross-contamination):

  Schema KHÔNG tồn tại RIÊNG LẺ → CHIA CHUNKS với schema khác:
    → Chunk [hồi hộp] thuộc NHIỀU schemas: tình yêu + sợ bị bỏ + gặp người mới
    → Khi schema tình yêu fire → chunk [hồi hộp] fire
    → Chunk [hồi hộp] CŨNG thuộc schema [sợ bị bỏ] → schema đó CŨNG fire nhẹ
    → = Cross-contamination: fire schema A → schema B CŨNG fire (vì shared chunks)

  Hệ quả:
    → Yêu (schema A) → hồi hộp → [sợ bị bỏ] (schema B) TỰ fire
    → = "Đang yêu mà TỰ NHIÊN lo lắng" = KHÔNG phải vô cớ
    → = Schema B (trauma) fire QUA shared chunk với schema A (tình yêu)
    → PFC: có thể NHẬN RA ("à, đây là lo từ trauma cũ") → override
    → PFC: có thể KHÔNG nhận ra → đổ lỗi cho người yêu → conflict

  → = Mọi schema đều CÓ THỂ ảnh hưởng lẫn nhau QUA shared chunks
  → = Trauma schemas ĐẶC BIỆT dễ contaminate vì:
    ① Compiled SÂU (emotional weight lớn → synapses mạnh)
    ② Chunks rộng (sợ, hồi hộp, bất an = chunks PHỔ BIẾN → shared nhiều)
    ③ Amygdala reinforce (cortisol kéo dài → amygdala mạnh → fire dễ)
  → = Trauma = "ô nhiễm" DỄ NHẤT cho schemas mới
  → (Chi tiết ví dụ: Schema-Example.md §1.4 và §1.7)
```

### 2.5 Schema Dừng Thế Nào — 3 Loại Body Signal

```
Schema KHÔNG dừng bằng 1 cơ chế duy nhất — có 3 loại signal KHÁC NHAU:

  ① SATISFACTION SIGNAL ("đủ rồi") — VÔ THỨC tự dừng:
     → Body confirm: body-need ĐÃ MET → signal fire
     → VÔ THỨC nhận → schema auto DỪNG
     → ⭐ PFC KHÔNG BIẾT signal tồn tại → PFC chỉ thấy KẾT QUẢ "hết muốn"
     → Ví dụ: ăn no → "tự nhiên hết muốn ăn" (PFC không quyết → body tự dừng)
     → Ví dụ: ngủ đủ → "tự nhiên tỉnh dậy" (body tự biết → PFC không set alarm)
     → = Body quyết "đủ" → schema dừng → PFC chỉ observe kết quả
     → Rõ nhất ở PULL channels: no, thoải mái, đủ ôm = rõ "đủ"
     → Mơ hồ ở PUSH channels: "đủ an toàn chưa?" = khó xác định → khó dừng

  ② BODY-REWARD ("sướng") — CẢ HAI biết, PFC CHỌN:
     → Body reward (opioid/oxytocin) → CẢ vô thức VÀ PFC nhận
     → Vô thức: auto drive "thêm!" (ăn ngon → ăn tiếp tự động)
     → PFC: observe → CHỌN: "sướng, nhưng NÊN tiếp không?"
     → = PFC = trọng tài cho reward → "ăn thêm hay dừng?"
     → Ví dụ: ăn ngon → PFC: "ngon nhưng đang diet → dừng" (override)
     → Ví dụ: scroll MXH → PFC: "hay nhưng phải làm → dừng" (override)

  ③ BODY-PAIN ("đau/khó chịu") — CẢ HAI biết, PFC CHỌN:
     → Body pain (nociception/mismatch) → CẢ vô thức VÀ PFC nhận
     → Vô thức: reflex TRƯỚC PFC (rút tay, 50ms)
     → PFC: observe → CHỌN: "đau, nhưng NÊN: sửa? chịu? chạy? đổi context?"
     → = PFC = trọng tài cho pain → "chịu đau hay tìm cách khác?"

  TÓM GỌN:
    Satisfaction: VÔ THỨC tự xử → PFC không biết → healthy khi ĐỂ YÊN
    Reward: CẢ HAI biết → PFC chọn → healthy khi PFC WISE
    Pain: CẢ HAI biết → PFC chọn → healthy khi PFC có OPTIONS

  ⚠️ PFC CÓ THỂ OVERRIDE Satisfaction (disconnect mechanism):
    → Body: "đủ rồi" → PFC: "CHƯA! deadline/ngon/thêm!"
    → = PFC override "hết muốn" → schema FORCE tiếp dù body nói đủ
    → = Quên ăn vì deadline, ăn quá no vì ngon, scroll MXH quá giờ
    → = Spectrum override: nhẹ (quên ăn) → nặng (anorexia, tử vì đạo)
    → (Chi tiết: Architecture-v7.5-Draft.md §2.5 Priority Exceptions)

  ⚠️ "LẮNG NGHE BODY" = gì chính xác?
    → KHÔNG phải "nghe Satisfaction Signal" (PFC không nghe được)
    → MÀ LÀ: tôn trọng KẾT QUẢ "hết muốn" → ĐỪNG override
    → = "Hết muốn ăn → DỪNG" thay vì "hết muốn nhưng ngon → ăn thêm"
    → = Meditation practice: nhận ra "hết muốn" → không thêm → không override
    → (Chi tiết: Body-Listening.md)
```

### 3.1 Gradient Depth (sâu → nông)

```
  Schema gradient từ BODY-NEED (sâu) → VALUES (giữa) → DOMAIN SKILLS (nông):

  SÂU (Body-need level):
    "Tôi cần an toàn" → ảnh hưởng MỌI context → khó thay đổi
    → Embedded trong body: cortisol baseline, muscle tension, gut state
    → Thay đổi: THÁNG → NĂM (phải thay đổi BODY, không chỉ "nghĩ khác")

  GIỮA (Values/Rules level):
    "Phải luôn productive" → cross-context → thay đổi khó
    → Compiled qua NHIỀU lần reinforce → synapse mạnh
    → Thay đổi: TUẦN → THÁNG (cần repeated experience mới)

  NÔNG (Domain skills):
    "Trời mưa mang ô" → 1 context → thay đổi dễ
    → Surface pattern → synapse nhẹ
    → Thay đổi: NGÀY (đổi context = đổi ngay)

  → Depth = f(số lần lặp × số modality × emotional weight)
  → Depth CAO = synapses MẠNH = khó sửa = ảnh hưởng RỘNG
  → Depth THẤP = synapses YẾU = dễ sửa = ảnh hưởng HẸP

  Ví dụ "trúng số" kiểm chứng gradient:
    Surface: "mai không đi làm" → ĐỔI NGAY ✅
    Mid: "tôi là người giàu" → vài tháng mới tin ⚠️
    Deep: "tôi vô giá trị" → VẪN CÒN dù giàu ❌
    Body: cortisol baseline VẪN CAO (5 năm stress → không reset vì trúng số) ❌
    → ~70% lottery winners quay về happiness baseline trong 1-2 năm 🟢
    → Vì: deep + body KHÔNG đổi → surface euphoria fades → deep PULL BACK
```

### 3.2 KHÔNG Có "Schema Âm" — Chỉ Có XUNG ĐỘT

```
  MỌI schema đều hình thành ĐỂ PHỤC VỤ body → luôn "dương" ban đầu

  "Kiềm chế lời nói":
    = DƯƠNG khi ở nhà bố mẹ strict (BẢO VỆ body khỏi bị phạt)
    = "ÂM" khi ở công ty cần communicate (CẢN body kết nối)
    → CÙNG schema → KHÁC context → từ "dương" THÀNH "âm"
    → = Schema KHÔNG có dấu cố định → CONTEXT cho dấu

  "ĐAU TÂM LÝ" = gì?
    KHÔNG phải: "có schema xấu"
    MÀ LÀ: XUNG ĐỘT giữa schemas trong context hiện tại

    3 loại xung đột:

    Loại 1 — 2 schemas CÙNG context, KHÁC hướng:
      "Muốn ăn" + "muốn giảm cân" → CẢ 2 dương riêng → xung đột CÙNG LÚC
      → Ăn = guilt. Không ăn = thèm. CẢ 2 đều đau.

    Loại 2 — Schema ĐÚNG context CŨ, SAI context MỚI (OUTDATED):
      "Tiết kiệm từng đồng" → ĐÚNG khi nghèo → OUTDATED khi lương ổn
      → Schema KHÔNG sai → context ĐÃ ĐỔI → schema chưa UPDATE

    Loại 3 — NHIỀU schemas ĐÚNG riêng, TỔNG THỂ xung đột:
      "Career" + "family" + "self-care" = TẤT CẢ dương
      → 24h KHÔNG đủ cho tất cả → PHẢI chọn → mất cái nào = đau

  CƠ CHẾ ĐAU — Vector Conflict:
    Schema A: push body hướng TRÁI
    Schema B: push body hướng PHẢI
    → Body chỉ đi ĐƯỢC 1 hướng → PFC phải chọn
    → Schema bị chặn VẪN CHẠY → tốn energy → đau
    → ĐAU ∝ |force_A − force_B| khi NGƯỢC hướng
    → ĐAU CỰC ĐẠI khi 2 forces GẦN BẰNG (paralysis)
    → ĐAU GIẢM khi 1 force THẮNG RÕ (dù sacrifice)
    → "Quyết định xong DÙ SAI cũng nhẹ hơn KHÔNG quyết định"

  IMPLICATIONS:
    → KHÔNG "fix schema xấu" (không có schema xấu)
    → MÀ: "resolve XUNG ĐỘT" hoặc "UPDATE schema cho context MỚI"
    → Hoặc: "change CONTEXT" để match schemas hiện có
    → = Không ai "hỏng" → chỉ "chưa aligned"
```

### 3.3 Schema Activation — Khi Nào Fire

```
  Always-on:     "tôi là nam" → background, luôn active
  Frequent:      "phải productive" → most contexts, auto-activate
  Trigger-based: "gặp sếp → formal" → chỉ khi trigger
  Dormant:       "kỹ năng xe đạp" → compiled, chỉ khi cần

  → Always-on = PERSISTENT influence → predict daily patterns
  → Trigger = SITUATIONAL → predict specific situations
  → "Khi mệt thấy con người THẬT" = PFC offline → deep schema (always-on) LỘ RA
```

### 3.4 Schema Decay + Reactivation

```
  Compiled schema MỜ DẦN khi không dùng (tháng → năm):
    → Synapse YẾU DẦN (less reinforcement) → fire YẾU hơn + CHẬM hơn
    → Giống đường mòn: đi thường = rõ, không đi = cỏ lấp dần

  Gradient decay:
    NÔNG (ít lặp, ít modality): mờ NHANH (tháng)
      Ví dụ: lái xe số sàn bỏ 10 năm → vụng, nhớ lại 30 phút
    SÂU (nhiều lặp, nhiều modality, emotional): mờ CỰC CHẬM
      Ví dụ: tiếng mẹ đẻ → 50 năm VẪN nhớ
      🟢 Alzheimer's: mất schema MỚI trước, CŨ NHẤT mất SAU CÙNG

  Interference — schema mới ĐÈ schema cũ:
    → Schema đang dùng = reinforce → mạnh
    → Schema không dùng = không reinforce + bị schema mới chiếm synapse → yếu
    → Proactive: schema cũ CẢN schema mới ("quen số sàn → khó học tự động")
    → Retroactive: schema mới ĐÈ schema cũ ("quen tự động → quên số sàn")

  Reactivation — schema mờ CÓ THỂ phục hồi:
    → Synapse yếu nhưng VẪN CÒN → reactivate DỄ HƠN học mới
    → "Học lại" nhanh hơn "học lần đầu" = savings effect 🟢
    → Bơi sau 15 năm: học lần đầu 3 tháng → học lại 1-2 buổi
    → = Schema compiled = INVESTMENT dài hạn (não KHÔNG xóa, chỉ giảm priority)
```

### 3.5 Schema Xuyên Suốt Body → Imagine

```
  Trong Architecture v7.5:

  Schema KHÔNG thuộc riêng Body hay Imagine:
    → Schema chạy ở Body-Base (vô thức, compiled, automatic)
    → Schema chạy ở Imagine (PFC draft, simulate, conscious)
    → = XUYÊN SUỐT cả 2 layers

  Body-level schema (vô thức):
    → Compiled: fire tự động, không cần PFC
    → "Đi bộ" = motor schema compiled → chân TỰ bước
    → "Sợ chó" = amygdala schema → body TỰ lùi
    → NHANH + RẺ + chính xác (cho pattern đã quen)
    → NHƯNG: KHÔNG đổi được nhanh (compiled = cứng)

  Imagine-level schema (PFC):
    → Draft: PFC tạo schema TẠM → test → sửa → compile DẦN
    → "Nếu nói vậy → sếp react thế nào?" = PFC draft test
    → "Kiến trúc code nên thế nào?" = PFC draft evaluate
    → CHẬM + ĐẮT + có thể sai (draft = ước lượng)
    → NHƯNG: LINH HOẠT + predict xa + cross-domain

  Pipeline: Imagine draft → compile → Body execute:
    PFC draft schema mới → lặp lại → synapse mạnh dần → COMPILE → vô thức giữ
    → PFC FREED → draft cái mới
    → = PFC = nhà máy SẢN XUẤT schema → vô thức = kho CHỨA + VẬN HÀNH
```

---

## 4. Schema Override Body-Base — Spectrum

```
⭐ INSIGHT QUAN TRỌNG:

  Architecture priority: L0 Alive > L1 Survival > L2 Quality > L3 Pattern
  NHƯNG: Schema Imagine CÓ THỂ override priority NÀY

  CÙNG CƠ CHẾ, KHÁC MỨC ĐỘ — spectrum từ nhẹ tới cực đoan:

  Nhẹ (hàng ngày):
    → Đọc sách hay quên ăn: Novelty override L1 Nutrition
    → Scroll MXH tới 2h sáng: Novelty override L1 Sleep
    → Deadline quên ăn: Threat override L1 Nutrition
    → = Schema redirect attention → body signal BỊ IGNORE

  Trung bình:
    → Workaholic quên ngủ/gia đình: Threat-{Status} override L1+L2
    → Nghiện game bỏ bê body: Novelty override L1+L2
    → Diet cực đoan: Threat-{Status:body image} override L1 Nutrition

  Nặng:
    → Game tới chết (có cases thật): Novelty override L1 Survival
    → Anorexia tới chết: Threat-{Status} override L1
    → Cờ bạc phá sản: Novelty loop override L1+L2+L3

  Cực đoan:
    → Tử vì đạo: Schema "thiên đàng" override L0 Alive
    → Kamikaze: Schema "tổ quốc" override L0 Alive
    → Mẹ nhảy vào lửa cứu con: Protect(gene) override L0 Alive(thân)

  CƠ CHẾ — double suppress:
    ① Schema redirect attention (ignore body signal)
    ② Cortisol từ schema suppress body sensation (biochemistry)
    → Body GẦN NHƯ câm → schema chạy tự do

  → Priority L0>L1>L2>L3 = ĐÚNG khi hệ thống healthy
  → Schema CÓ THỂ phá priority BẤT KỲ LÚC NÀO
  → "Bug" cho cá nhân (quên ăn → hại body)
  → "Feature" cho gene/tập thể (hy sinh → gene survive)


"GIỌT NƯỚC TRÀN LY" — chunk swap trong schema mạnh:

  Schema đang active MẠNH (compiled months, cortisol duy trì):
    → Chunk [tôi cố được] giữ schema ở mode "chịu đựng"
    → Body: khó chịu nhưng CHƯA ĐAU (schema suppress)

  1 event NHỎ (sếp nhắc nhẹ):
    → Chunk swap: [tôi cố được] → [tôi có thể bị đuổi]
    → Schema CÙNG cường độ MẠNH → nhưng giờ ở mode "THREAT"
    → Toàn bộ energy schema → chạy threat → ĐAU CỰC LỚN
    → = Giọt nước NHỎ → ly ĐÃ ĐẦY + ly LỚN (schema mạnh) → TRÀN MẠNH
    → = "Tại sao khóc vì chuyện nhỏ?" = ly đã đầy từ TRƯỚC

  Spectrum phản ứng CÙNG sự kiện (sếp nhắc nhẹ):
    Người khỏe (ly trống): "ok, sửa" → nhẹ nhàng
    Người mệt 3 tháng (ly nửa): khó chịu 1 tiếng → ok
    Người mệt 12 tháng (ly gần đầy): lo lắng 1 ngày → khó ngủ
    Người burnout (ly đầy): KHÓC ngay tại chỗ
    Người burnout nặng (ly nứt): freeze / panic / có thể ngất
    → CÙNG giọt → KHÁC kết quả → vì LY khác nhau
```

---

## 5. Schema × Cortisol — Chunk Association

```
⭐ INSIGHT: cùng chunk, khác ASSOCIATION → khác SUỐT ĐỜI

  CORTISOL MODERATE + NOVELTY DRIVE (thích thú, tò mò):
    → Tìm thấy domain thú vị → đọc/thử → chunk NẠP
    → Chunk gắn với: curiosity + relief + "ồ hay!"
    → = Chunk gắn OPIOID (body reward khi hiểu/làm được)
    → Body-base: "chunk này cho tôi SƯỚNG" → sẵn sàng dùng lại
    → Ví dụ: Newton đọc physics vì TÒ MÒ → chunk gắn opioid → THÍCH dùng

  CORTISOL TỪ THREAT (sợ phạt, bị ép):
    → BỊ ÉP nạp chunk → chunk NẠP
    → Chunk gắn với: sợ + khó chịu + "phải làm"
    → = Chunk gắn CORTISOL (threat khi học)
    → Body-base: "chunk này gắn KHÓ CHỊU" → không muốn dùng lại
    → Ví dụ: học sinh bị ép học toán → chunk gắn cortisol → GHÉT toán

  → CÙNG kiến thức (toán vi phân) → KHÁC association → KHÁC khả năng dùng:
    Newton: nạp vì tò mò → chunk gắn opioid → THÍCH
    Học sinh: nạp vì sợ → chunk gắn cortisol → GHÉT
    → = Cùng chunk, khác "nhãn cảm xúc" → khác hành vi suốt đời

  MỌI HÀNH VI = MIX threat + novelty (tỉ lệ KHÁC NHAU):
    → KHÔNG CÓ hành vi nào THUẦN threat hay THUẦN novelty
    → Luôn là spectrum: 100% threat ←→ 100% novelty
    → Chunk association = TRUNG BÌNH weighted của tỉ lệ

    Threat NHẸ (60:40): "làm bài xong mới đi chơi"
      → Cortisol nhẹ + chút opioid (anticipate chơi)
      → Chunk: dễ update sau này ✅

    Threat NẶNG (95:5): "không học là ăn đòn, mỗi ngày"
      → Cortisol MẠNH + KHÔNG opioid
      → Chunk: gắn cortisol cực sâu → body PHẢN ĐỐI khi dùng
      → CỰC KHÓ update → body nhớ threat mỗi khi chunk fire ❌

  THREAT CHUNK CÓ GIÁ TRỊ — ở ngưỡng phù hợp:
    → Chunk từ threat NHẸ: nền tảng tốt, update DỄ
    → Chunk từ threat VỪA: nền tảng tốt, update ĐƯỢC (cần thời gian)
    → Chunk từ threat NẶNG: nền tảng CÓ nhưng body phản đối → KHÓ dùng
    → = Threat-learn VẪN CÓ GIÁ TRỊ nếu ĐÚNG NGƯỠNG
    → = Chi tiết: Change-Readiness.md §3.5, Education-AI-Era-Draft.md
```

---

## 6. Schema × Domain — Base → Shift → Check

```
⭐ UNIVERSAL OPTIMIZATION — cách schema tương tác domain:

  MỌI schema tương tác domain theo CÙNG 1 pattern:

  ① CÓ BASE ổn định (compiled pattern, quen thuộc):
     → Neurons fire ĐỀU → synapses MẠNH → "quen thuộc"
     → VTA: quen → KHÔNG fire (habituation) → PFC không chú ý

  ② SHIFT NHẸ từ base (thử cái mới, khác chút):
     → Cortisol kích thích → neurons THỬ pattern khác
     → VTA: detect BIẾN ĐỘNG → dopamine → PFC biết

  ③ BODY CHECK (domain reality test):
     → PFC spotlight → body-base evaluate:
       "Shift này KHỚP domain reality không?"
     → Khớp: "ngon/hay/đúng/vui" → opioid → ACCEPT → base UPDATE
     → Không khớp: "dở/chán/sai" → REJECT → quay về base cũ

  ④ NEW BASE (base đã update) → shift tiếp → check tiếp → ...
     → = LOOP: base → shift → check → accept/reject → new base

  Pattern NÀY chạy XUYÊN MỌI domain:
    Ăn: cơm quen (base) + món phụ mới (shift) + ngon không? (check) → update
    Nhạc: thể loại quen (base) + bài mới (shift) + hay không? (check) → update
    Học: kiến thức có (base) + info mới (shift) + đúng không? (check) → update
    Code: architecture có (base) + feature mới (shift) + work không? (check) → update
    Người: bạn quen (base) + gặp người mới (shift) + hợp không? (check) → update
    → = CÙNG mechanism vì CÙNG hardware (neurons + dopamine + opioid)

  → "Base" KHÔNG cố định → DỊCH DẦN qua hàng nghìn incremental shifts
  → = "Khẩu vị thay đổi" = base ĐÃ shift qua nhiều năm ăn + check
  → = Đây là ATTRACTOR PATTERN: "stable base + incremental shift + feedback check"
  → = Bất kỳ hệ thống nào có constraint "thích ứng + ổn định" → TỤ VỀ pattern này
```

---

## 7. Body Baseline State — Schema Sâu Nhất

```
  MỌI schema layers build TRÊN 1 nền tảng: body baseline state
  = Ground truth — PFC, verbal, logic đều THAM CHIẾU về đây

  Body Baseline State = trạng thái TỔNG THỂ body khi NGHỈ:
    Cortisol baseline:  mức stress nền
    Opioid tone:        mức pleasure nền
    Oxytocin level:     mức connection nền
    Muscle tension:     vai gồng? hàm nghiến? thả lỏng?
    Gut state:          tiêu hóa bình thường? IBS?
    Sleep architecture: deep sleep đủ? REM đủ?
    HRV:                heart rate variability
    Immune baseline:    inflammation mãn tính?

  = "Khi không có gì xảy ra, cơ thể TÔI feel thế nào?"
  = CHỈ CÓ 1 (body chỉ có 1: cortisol không vừa cao vừa thấp)

  Fix body baseline → MỌI schemas tự adjust (ground truth thay đổi)
  Fix schemas MÀ KHÔNG fix body → relapse (body PULL surface quay lại)

  → Thứ tự: Body → Mind, KHÔNG phải Mind → Body
  → = Sửa NỀN MÓNG trước, sơn TƯỜNG sau
  → "Biết nhưng không thay đổi" = verbal updated (PFC), body CHƯA (deep VẪN CÒN)

  3 ĐƯỜNG reverse-engineer body baseline:
    ① Observe behavior: "tôi hay LÀM GÌ khi stress?" → schema biểu hiện
    ② Observe body: "vai tôi THƯỜNG gồng hay thả?" → body state hiện tại
    ③ Self-identify conflicts: "tôi MUỐN gì nhưng KHÔNG LÀM?" → schema conflict
    → = Không cần biết CHÍNH XÁC schema → biết PATTERN = đủ navigate
```

---

## 8. Sửa Đúng Lớp = Sửa Đúng Modality

```
  Surface fix (nhanh, TẠM thời):
    Lời động viên (verbal): PFC nhận → tạm nhẹ → body VẪN stress
    Đổi hoàn cảnh (context): L1-L2 switch → nhưng body mang schema cũ theo
    Tiền (resource): giảm financial stress → nhưng body stress KHÁC vẫn còn
    → TẤT CẢ surface → body PULL QUAY LẠI sau thời gian

  Deep fix (chậm, BỀN VỮNG):
    Sleep đủ: consolidation + body repair → FOUNDATION
    Exercise: cortisol burn + BDNF tăng → body RESET dần
    Nutrition: gut-brain axis → mood baseline shift
    Somatic therapy: body trực tiếp thả → schema sâu TỰ UPDATE
    → Fix BODY trước → body calm → PFC available → therapy hiệu quả

  → "Tại sao cứ lặp vấn đề cũ?" = surface fixed, body CHƯA
  → Fix body → rồi fix thought → ĐÚNG THỨ TỰ
```

---

## 9. Câu Hỏi Mở

```
S1: Schema "negative" có THẬT SỰ không tồn tại?
    → Framework: chỉ có conflict → nhưng: "tôi vô giá trị" LUÔN xung đột?
    → Có thể: schema sâu ALWAYS-ON "vô giá trị" = pseudo-negative
    → Vì: MỌI context đều conflict với nó → TRÔNG GIỐNG "always negative"
    → = Technically conflict → nhưng practically = negative everywhere

S2: Schema COMPILED có thể UNCOMPILE hoàn toàn?
    → Decay + interference = YẾU dần → nhưng BAO GIỜ = zero?
    → Likely: KHÔNG BAO GIỜ zero → chỉ YẾU cực → nhưng CÓ THỂ reactivate
    → = "Cai 10 năm vẫn có thể relapse" = schema CÒN dù cực yếu

S3: AI có thể detect schema không?
    → AI đọc TEXT output (verbal) → detect VERBAL schema
    → NHƯNG: verbal = ~1/6 schema thật → miss 5/6
    → CẦN: body data (HRV, cortisol, muscle tension) để detect SÂU
    → = Wearable + AI = CÓ THỂ detect schema SÂU hơn (tương lai)

S4: Schema × gene (epigenetics):
    → Trauma → cortisol high → epigenetic changes → di truyền 1-2 thế hệ?
    → = Schema "sợ" ở bố/mẹ → body state CON bị ảnh hưởng?
    → 🟢 Mouse studies: fear conditioning → offspring show fear response (Dias & Ressler 2014)
    → = Schema CÓ THỂ "di truyền" qua epigenetics (KHÔNG qua gene trực tiếp)
```

---

## 10. Kết Nối

```
→ Architecture-v7.5-Draft.md: Schema frame trong kiến trúc tổng thể
→ PFC-Analysis.md §1: PFC 5 functions (Draft+Test+Route+Brake+Translator)
→ PFC-Analysis.md §1.5: PFC = phòng thí nghiệm giả lập
→ PFC-Analysis.md §8: Cognitive Parameters (Capacity, Clear-Speed, Chunk-Size)
→ PFC-Analysis.md §8.3: VTA mechanism + cortisol calibration
→ Imagination-Analysis-v2.md: Imagine = hệ thống hỗ trợ schema shift
→ Change-Readiness.md: cortisol × schema (calibration energy + chunk association)
→ Modality-Analysis.md: modality encoding per schema
→ Status-Analysis-v2.md: Status = schema access map
→ Addiction-Analysis-v2.md: schema hijack
→ Body-Listening.md: cách nghe body baseline
→ Education-AI-Era-Draft.md: threat-learn vs novelty-learn chunks
→ Drive-Optimization.md §9: Pressure + Challenge + Autonomy
```

---

> *Schema Atlas v2 — "Schema = compiled neuron patterns. Chunk = atom of schema.
> KHÔNG có schema 'xấu' — chỉ có XUNG ĐỘT trong context cụ thể.
> Schema override body-base: spectrum từ quên ăn → tử vì đạo (cùng cơ chế).
> Cùng chunk + khác association (Novelty vs Threat) = khác hành vi SUỐT ĐỜI.
> Base → shift → check → accept/reject = universal optimization.
> Fix body TRƯỚC → schema tự adjust → ĐÚNG THỨ TỰ."*
