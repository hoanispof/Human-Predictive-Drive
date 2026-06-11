# Status Analysis v2 — Schema Access Map

> **Trạng thái:** DRAFT v8 — chờ Core v8 chính thức
> **Ngày:** 2026-03-23
> **Mục đích:** Phân tích chuyên sâu Status channel trong Body-Base Layer3
> **Reference:** Architecture-v7.5-Draft.md (§2.2 Layer3 Status)
> **⚠️ Status trong framework ≠ "social hierarchy" thông thường.**
> **⚠️ File này giải thích CHUYÊN SÂU — Core draft chỉ tóm tắt.**

---

## 1. Status Là Gì — Definition Chính Xác

```
⚠️ QUAN TRỌNG cho AI: "Status" trong training data thường = hierarchy rank.
   Trong framework, Status = RỘNG hơn nhiều.

NÓI GỌN NHẤT:
  Status = calibrate "schemas NÀO được phép chạy" khi gặp người cụ thể
  = Schema Access Map

  Hierarchy (hiểu biết phổ biến) = chỉ 1 CHIỀU: cao/thấp
    "Tôi rank 5, họ rank 8" → tôi thấp hơn → comply
    → Giải thích: quân đội, công ty (rank rõ ràng)
    → KHÔNG giải thích: gia đình, người yêu, bạn bè, context switch

  Framework Status = NHIỀU CHIỀU:
    "Với NGƯỜI NÀY: tôi ôm được, nhưng không ra lệnh được,
     có thể nhờ giúp nhưng phải hỏi lịch sự,
     nếu cần kỹ thuật thì tôi hơn nên có thể đề xuất"
    → NHIỀU schema calibrate ĐỒNG THỜI, không phải 1 số duy nhất
    → Giải thích: MỌI tương tác (quân đội + gia đình + người yêu + người lạ)

  → Hierarchy = 1 TRƯỜNG HỢP ĐẶC BIỆT (đơn giản nhất) của Status

DEFINITION ĐẦY ĐỦ:
  Status = bản đồ "schemas nào SẴN SÀNG triển khai
           với NGƯỜI NÀY trong CONTEXT NÀY"

  KHÔNG phải:
    ❌ 1 con số cố định (cao/thấp)
    ❌ Vị trí trong hierarchy (CEO > Manager > Staff)
    ❌ Prestige / danh vọng / giàu nghèo
    ❌ Tham vọng quyền lực

  MÀ LÀ:
    ✅ DYNAMIC: thay đổi theo từng người gặp × từng context
    ✅ MATRIX: mỗi người gặp = 1 bản đồ KHÁC
    ✅ BIDIRECTIONAL: tôi→họ VÀ họ→tôi cùng lúc
    ✅ BODY-LEVEL: vô thức scan, không cần PFC
    ✅ Mọi động vật xã hội có (baboon, gà, sói, cá)
```

---

## 2. Cơ Chế Scan — Body Vô Thức

```
Khi gặp 1 người, body VÔ THỨC scan (milliseconds → seconds):

  ① Họ hơn tôi cái gì?
     → Sức mạnh? Skill? Kiến thức? Resource? Network?
     → = "Họ CÓ GÌ mà tôi cần/muốn"

  ② Tôi hơn họ cái gì?
     → Sức mạnh? Skill? Kiến thức? Resource?
     → = "Tôi CÓ GÌ mà họ cần/muốn"

  ③ Tôi có thể NHẬN gì từ họ?
     → Không cần trả gì? (tôi >> họ)
     → Phải trao đổi? (ngang hàng)
     → Phải xin? (tôi << họ)

  ④ Họ có thể NHẬN gì từ tôi?
     → Tôi có thể từ chối? (ngang/trên)
     → Tôi không thể từ chối? (dưới)

  ⑤ Có thể TRAO ĐỔI không?
     → "Tôi muốn ôm, họ cũng muốn" → schema "ôm" SẴN SÀNG
     → "Tôi muốn ôm, họ không muốn" → schema "ôm" BỊ BLOCK

  KẾT QUẢ SCAN = Schema Access Map:
    → Danh sách schemas SẴN SÀNG cho người này
    → Danh sách schemas BỊ BLOCK cho người này
    → = Status Position VỚI NGƯỜI NÀY (không phải chung chung)
```

---

## 3. Status Gap → 3 Modes Tương Tác

```
STATUS QUYẾT ĐỊNH MỌI TƯƠNG TÁC — từ ôm tới chiến tranh:

  ┌──────────────────────────────────────────────────────────┐
  │ Status gap           │ Mode          │ Schema sẵn sàng   │
  ├──────────────────────┼───────────────┼────────────────────┤
  │ TÔI >> HỌ (gap lớn) │ LẤY           │ Ra lệnh, kiểm soát│
  │                      │               │ lấy mà không trả  │
  │                      │               │ Ví dụ: lãnh chúa, │
  │                      │               │ hổ ăn nai          │
  ├──────────────────────┼───────────────┼────────────────────┤
  │ TÔI ≈ HỌ (ngang)    │ TRAO ĐỔI      │ Negotiate, cùng   │
  │                      │               │ cho nhau           │
  │                      │               │ Ví dụ: người yêu  │
  │                      │               │ ôm ↔ được ôm,     │
  │                      │               │ thương mại         │
  ├──────────────────────┼───────────────┼────────────────────┤
  │ TÔI << HỌ (gap lớn) │ COMPLY        │ Xin, tuân theo,   │
  │                      │               │ cho mà không đòi   │
  │                      │               │ Ví dụ: nô lệ,     │
  │                      │               │ nhân viên mới      │
  └──────────────────────┴───────────────┴────────────────────┘

  ⚠️ "Tấn công" KHÔNG phải drive riêng:

    Con hổ đuổi nai:
      → Hổ KHÔNG "tấn công" — hổ "ĂN"
      → Status: nai << hổ → schema "lấy (ăn)" sẵn sàng
      → Giống người hái quả — không ai gọi "tấn công cây"

    Người ăn thịt/rau:
      → Status: động vật/cây << người → schema "lấy" bình thường
      → Không cần "attack drive" riêng

    2 đội quân đánh nhau:
      → Cả 2 nghĩ mình mạnh hơn (status gap KHÔNG RÕ)
      → → Tranh giành = CALIBRATE status bằng conflict
      → Kẻ thắng: schema access TOÀN MỞ → lấy tất cả
      → Kẻ thua: schema access TOÀN ĐÓNG → mất tất cả

    Thế giới hiện đại:
      → Tranh giành bằng RULES (luật, thị trường, đấu thầu)
      → Thay vì bạo lực → cùng function, khác method
      → Kiện tụng = "chiến tranh" qua luật sư
      → Cạnh tranh thương mại = "chiến tranh" qua sản phẩm

  → "Tấn công" = extreme case: status gap CỰC LỚN → schema "lấy" KHÔNG BỊ CẢN
  → KHÔNG cần attack channel riêng — Status COVER toàn bộ spectrum:
    LẤY ←→ TRAO ĐỔI ←→ COMPLY
```

---

## 4. Status Position vs Aspiration — Tách 2 Tham Số

```
Tại sao CẦN 2 tham số (giữ từ v7, vẫn đúng):

  POSITION = "tôi ĐANG ở đâu" (cảm nhận hiện tại):
    → Serotonin baseline = chemical đánh dấu vị trí
    → Ổn định, thay đổi chậm
    → Body-level (vô thức biết)
    → THUỘC Body-Base Layer3 ✅

  ASPIRATION = "tôi MUỐN ở đâu" (mong muốn):
    → Schema predict "nên ở vị trí X"
    → Có thể thay đổi nhanh (so sánh MXH → aspiration tăng vọt)
    → PFC-level (imagine + compare)
    → THUỘC Imagine layer:
      Status-Drive: aspiration > position → "muốn lên" (Novelty-Schema)
      Status-Threat: aspiration > position → "sợ tụt" (Threat-Schema)

  GAP = Aspiration - Position:
    Gap > 0: drive (chase hoặc anxiety, tùy Change-Readiness mode)
    Gap ≈ 0: content (thỏa mãn)
    Gap < 0: "quá nhiều" → có thể CHO BỚT (Chouinard pattern)

  6 CASES VERIFY (từ v1, vẫn đúng):
    CEO chase thêm:        Position CAO + Aspiration CAO HƠN → gap > 0 ✅
    Người nghèo thỏa mãn:  Position THẤP + Aspiration THẤP → gap ≈ 0 ✅
    Khoe MXH:              Position VỪA + Aspiration CAO → gap → khoe ✅
    Tỷ phú cho hết:        Position CAO + Aspiration THẤP → gap < 0 → cho ✅
    Tự tin nội tại:        Position VỪA + Aspiration = Position → gap = 0 ✅
    Công nhân vui vẻ:      Position THẤP + Aspiration THẤP → gap ≈ 0 ✅
```

---

## 5. Being Seen — Calibrate Status Đúng Thực Tế

```
"Người khác BIẾT ĐÚNG tôi làm được gì"

  Being Seen = calibrate schema access map cho CHÍNH XÁC:
    → Map chính xác = hợp tác HIỆU QUẢ (biết ai cho gì, nhận gì)
    → Map sai = frustrate (bị đánh giá thấp) hoặc bị lợi dụng (bị đánh giá cao)

  Ví dụ:
    "Anh làm được, chỉ chưa phải bây giờ, em hiểu cho"
    = Muốn map ĐÚNG: "anh CÓ capacity, đang bận"
    = Nếu em không hiểu → map sai: "anh không làm được" → schema bị block sai
    = Em rời đi → mất cơ hội trao đổi tương lai → thiệt cho cả hai

  Trong nhóm:
    Mỗi người BIẾT nhau → maps CHÍNH XÁC → hợp tác TỐT
    Ai đó bị hiểu sai → map sai → hợp tác KÉM + frustrate

  → Being Seen = STATUS CALIBRATION function
  → Thuần Status (calibrate position đúng thực tế)
  → Không phải Connection (không cần "thân" — chỉ cần "biết đúng")
```

---

## 6. Belonging — Cached Status Maps

```
"Nhóm quen = status maps ĐÃ CALIBRATE sẵn"

  2 FUNCTIONS:

  ① CACHE — giảm scan cost:
     Gặp người trong nhóm: map CÓ SẴN → không scan → THOẢI MÁI
     Gặp người ngoài nhóm: phải scan → TỐN ENERGY → MỆT
     → Belonging = "tiết kiệm energy calibrate"
     → Mất belonging = mất cache → phải scan MỌI NGƯỜI → kiệt sức
     → = Giải thích: người mới chuyển trường/công ty = MỆT (scan liên tục)

  ② BACKING — tăng confidence:
     Thuộc nhóm = có thế lực hỗ trợ → status maps RỘNG HƠN
     → "Tôi có nhóm hỗ trợ" → dám mở schema → tự tin hơn
     → Mất nhóm → mất backing → schema thu hẹp → mất tự tin
     → = Giải thích: bị loại khỏi nhóm = đau (status maps bị thu hẹp đáng kể)

  Ví dụ nhà thờ:
    Cha Sứ > Ông Trùm > tín hữu ngang nhau
    → Status maps DEFINED SẴN → vào nhà thờ = không scan → thoải mái
    → Ai đọc kinh nhiều → status tăng nhẹ trong context nhà thờ
    → Nhưng: RA KHỎI nhà thờ → status map KHÁC (context switch)

  Ví dụ đàn khỉ:
    → Mỗi con biết rank mọi con khác → maps SẴN → TIẾT KIỆM
    → Con mới gia nhập → phải scan + fight → TỐN ENERGY → rồi settle
    → Sau khi settle → cache → thoải mái
```

---

## 7. Status Flexibility — Mỗi Người Khác Nhau

```
Mỗi người calibrate STATUS rộng/hẹp KHÁC NHAU khi switch context:

  ỔN ĐỊNH CAO (serotonin baseline ổn):
    → Ở đâu cũng gần GIỐNG (tự tin hoặc rụt rè)
    → Switch context → status map thay đổi ÍT
    → Calibrate range HẸP
    → Ưu: predictable, ít stress khi đổi context
    → Nhược: có thể không adapt đủ (tự tin ở chỗ nên khiêm nhường)
    → Ví dụ: "người này ở đâu cũng tự tin giống nhau"

  DAO ĐỘNG MẠNH (serotonin baseline dao động):
    → Mỗi context → status map thay đổi ĐÁNG KỂ
    → Calibrate range RỘNG
    → Ưu: adapt tốt theo context
    → Nhược: energy tốn nhiều, stress khi switch nhanh
    → Ví dụ: ở công ty rất tự tin (sếp) → ở nhà rụt rè (vợ dominant)

  PHỔ BIẾN: somewhere in between
    → Có baseline ổn định + calibrate VỪA cho từng context
    → Giống: thân nhiệt ổn 37°C nhưng DA adjust theo môi trường
    → Mỗi context = 1 vùng calibrate riêng
      (nhà thờ: khiêm nhường | công ty: competitive | nhà: thoải mái)
```

---

## 8. Switch Context ≠ Calibrate Status — 3 Layers Khác Nhau

```
⚠️ QUAN TRỌNG: Dễ nhầm "switch context" = "calibrate status". Thực tế = 3 THỨ KHÁC NHAU:

  ① SEROTONIN BASELINE (Status nền):
     → Ổn định, carry across ALL contexts
     → KHÔNG tốn PFC
     → = "Nhìn chung tôi tự tin thế nào"
     → Thay đổi CHẬM (tuần → tháng)
     → Ví dụ: được khen ở cty → về nhà VẪN tự tin
              bị mắng ở nhà → lên lớp VẪN thiếu tự tin

  ② STATUS PER-CONTEXT (maps đã quen):
     → Mỗi context quen = 1 compiled map
     → Switch giữa maps quen = PFC load compiled → TỐN ÍT
     → Ở cty: map A | ở nhà: map B | ở nhà thờ: map C
     → Vài context quen = GẦN NHƯ FREE (giống lái xe đường quen)
     → Ví dụ: từ cty về nhà → PFC switch nhanh, vì đã quen cả 2

  ③ STATUS CONTEXT MỚI (chưa có map):
     → Gặp nhóm mới, job mới, nước mới
     → PFC phải DRAFT map mới → TỐN NHIỀU
     → Cortisol tăng (uncertainty) cho tới khi map compiled
     → = "Mệt khi đi chỗ mới" = PFC drafting status maps liên tục
     → Ví dụ: ngày đầu đi làm = mệt vì scan mọi người

  CHỒNG LÊN NHAU:
    Switch context (PFC function): load map khác → nhanh nếu quen
    Status nền (serotonin): carry theo → không đổi
    Calibrate mới (PFC + time): nếu context mới → tốn đáng kể

    → Người chuyển trường: switch context (PFC)
      + calibrate TOÀN BỘ maps mới (PFC heavy)
      + serotonin baseline carry (có thể thấp nếu bị bully trước)
      = TRIPLE cost → cực mệt → giải thích "trầm cảm khi chuyển trường"
```

---

## 8.5 Serotonin Ratchet — Chỉ Muốn Lên, Kháng Xuống

```
🟢 Serotonin có xu hướng HOMEOSTASIS ĐẶC BIỆT:

  ① ỔN ĐỊNH (mặc định):
     Serotonin baseline CỐ GIỮ mức hiện tại
     → Tránh dao động → tránh tốn PFC recalibrate
     → = "Tôi biết mình ở đâu, giữ nguyên"

  ② SẴN SÀNG TĂNG (khi có cơ hội):
     Cơ hội → serotonin TĂNG nhanh:
       Được khen → tăng
       Đối thủ mất → "vị trí trống" → tăng
       Thắng competition → tăng
     → 🟢 Sapolsky: khỉ alpha chết → khỉ beta serotonin TĂNG NGAY
     → = Luôn sẵn sàng "lấp chỗ trống" phía trên

  ③ KHÁNG GIẢM (khi bị threat):
     Bị hạ status → body KHÁNG trước khi chấp nhận:
       Denial: "không, tôi vẫn giỏi"
       Rationalize: "họ không hiểu tôi"
       Fight back: "tôi sẽ chứng minh"
     → Serotonin chỉ GIẢM khi bằng chứng QUÁ NHIỀU
     → = Mất rank = body KHÁNG → rồi mới chấp nhận → rồi mới adjust

  → = RATCHET EFFECT: dễ lên, khó xuống
  → Giải thích:
    CEO bị sa thải: denial lâu, khó chấp nhận → vì serotonin KHÁNG giảm
    Người mới giàu: adjust NHANH (serotonin sẵn sàng tăng)
    Người mới nghèo: adjust CHẬM (serotonin kháng giảm) → đau khổ kéo dài
```

---

## 8.6 Quân Đội = Status Optimization System

```
Quân đội = THIẾT KẾ STATUS hiệu quả nhất loài người đã tạo:

  VẤN ĐỀ trong đời thường:
    → Gặp người mới → scan → calibrate → TỐN PFC
    → Status không rõ → xung đột → tốn thời gian + energy
    → 100 người lạ → 100 lần calibrate → CỰC TỐN

  QUÂN ĐỘI GIẢI QUYẾT:

  ① PHÂN CẤP RÕ RÀNG (quân hàm — visual symbol):
     → NHÌN là biết status NGAY → PFC cost ≈ ZERO
     → Đời thường: gặp lạ → 5-30 giây scan
     → Quân đội: nhìn quân hàm → 0.5 giây → DONE

  ② TUÂN THỦ TUYỆT ĐỐI (schema FIXED per rank):
     → Cấp dưới: comply → luôn đúng → PFC không cần draft
     → Cấp trên: ra lệnh → luôn đúng → PFC không cần negotiate
     → = Compiled schema per rank → vô thức execute

  ③ TÔN TRỌNG TUYỆT ĐỐI (không challenge):
     → Rank cao: serotonin stable → assured
     → Rank thấp: BIẾT RÕ vị trí → không bất an
     → "Biết rõ ở đâu" = THOẢI MÁI hơn "không biết"
     → Uncertainty = tốn PFC + cortisol | Certainty = tiết kiệm

  ④ LÝ DO RÕ RÀNG (Coherence satisfied):
     → Rank cao vì kinh nghiệm + training → hiểu được → chấp nhận dễ

  KẾT QUẢ:
    Đời thường: ~50% PFC bandwidth tốn cho social status calibration
    Quân đội: ~5% PFC cho status (pre-defined) → 95% cho TASK
    → = PFC FREED UP cho chiến thuật, chiến lược, problem-solve
    → = Đây là lý do quân đội HIỆU QUẢ trong crisis

  MỞ RỘNG — cùng principle ở MỌI NƠI:
    Đồng phục trường học: giảm status noise (giàu/nghèo)
    Dress code công ty: giảm visual status competition
    Áo lễ nhà thờ: flatten status (ngang nhau trước Chúa)
    → = TẤT CẢ nhằm GIẢM PFC cost cho status calibration
```

---

## 9. Status × Layer Interaction

```
Status AMPLIFY access toàn bộ Body-Base:

  Status CAO (với người đối diện) → maps MỞ:
    L2 Experience: dám thử món mới, dám đi nơi mới
    L2 Connection: dám gần, dám ôm, dám eye contact
    L3 Mastery: dám thử skill khó (không sợ fail)
    L3 Coherence: dám hỏi "tại sao?" (không sợ bị coi ngu)
    L3 Protect: dám giữ (không sợ bị lấy lại)
    → = Mọi schema SẴN SÀNG → body-need DỄ meet

  Status THẤP (với người đối diện) → maps ĐÓNG:
    L2 Experience: không dám (sợ "không xứng")
    L2 Connection: rụt rè (sợ bị reject)
    L3 Mastery: sợ fail (không dám thử)
    L3 Coherence: sợ hỏi (sợ bị coi ngu)
    L3 Protect: không dám giữ (sợ conflict)
    → = Schemas BỊ BLOCK → body-need KHÓ meet

  → Status = AMPLIFIER cho MỌI channel
  → Nhưng: per-person × per-context (không phải global)
```

---

## 9.5 Status Thực Tế — Nhóm 5-20 Người Quen

```
TRONG THẾ GIỚI HIỆN ĐẠI — status baseline KHÁC BIỆT NHỎ hơn tưởng:

  Thời cổ đại — gap CỰC LỚN:
    Lãnh chúa: kiểm soát mọi thứ → body state tự tin thật sự
    Nô lệ: không kiểm soát gì → body state sợ hãi thật sự
    → Status baseline KHÁC BIỆT lớn → biochemistry KHÁC thật

  Thế giới hiện đại — gap NHỎ hơn nhiều:
    ① Pháp luật flatten status thực tế:
       CEO không thể đánh nhân viên, tổng thống không lấy nhà bạn
       → Schema "lấy" bị BLOCK bởi luật → gap TRÊN GIẤY > gap CẢM NHẬN
    ② Ít tương tác trực tiếp cross-status:
       Bạn KHÔNG GẶP tổng thống → không ảnh hưởng gì
    ③ Basic needs MET cho đa số:
       Có ăn, có nhà → không "comply vì đói" → gap ít ảnh hưởng survival

  → Status THẬT SỰ CẢM NHẬN = từ NHÓM 5-20 NGƯỜI QUEN:
    Vợ/chồng, con, sếp trực tiếp, đồng nghiệp, bạn thân
    → ĐÂY mới là nơi status TÁC ĐỘNG hàng ngày
    → Bị vợ coi thường → status baseline GIẢM thật
    → Được sếp công nhận → status baseline TĂNG thật
    → = Status thực tế ≈ trung bình experience từ 5-20 người quen

  Hệ quả:
    "Giàu nhưng vợ coi thường" = status THẤP (within nhóm thân)
    "Nghèo nhưng gia đình tôn trọng" = status ỔN (within nhóm thân)
    → Thu nhập KHÔNG = status thực tế cảm nhận

  MXH — STATUS NOISE:
    MXH mở rộng "nhóm so sánh" từ 5-20 → HÀNG NGHÌN người
    → Thấy người khác "thành công" → aspiration TĂNG (Imagine layer)
    → Aspiration tăng → gap → Threat-{Status} → cortisol
    → Cortisol → suppress status baseline → vicious cycle
    → = MXH GIÁN TIẾP hạ status baseline QUA cortisol
    → Không phải trực tiếp — mà qua chuỗi: MXH → aspiration → threat → cortisol
```

---

## 10. Status × Cortisol — Khi Change-Readiness Cao

```
Cortisol cao → status SUPPRESS (quan sát được, hormone candidate chưa chắc):

  Cortisol    Status effect
  ─────────── ────────────────────────────
  Thấp        Status maps ỔN → body-need dễ meet
  Vừa         Status maps ỔN + ACTIVE calibrate tốt
  Cao         Status maps THU HẸP → "tôi kém" → rụt rè
  Rất cao     Status maps GẦN ĐÓNG → "vô giá trị" → isolate

  → Cortisol cao → Status suppress → body-need KHÓ meet
  → Body-need không met → cortisol tăng thêm → VICIOUS CYCLE
  → = "Thành công nhưng trống rỗng": Status Position cao (bên ngoài)
    nhưng cortisol cao → cảm nhận Status THẤP → maps thu hẹp
    → "Có mọi thứ nhưng không enjoy được"
```

---

## 10.5 Evidence Limitations — Thật Thà Về Research

```
⚠️ QUAN TRỌNG — tách rõ FUNCTION vs HORMONE:

  FUNCTION "Status = Schema Access Map" — CHẮC CHẮN CÓ:
    ✅ Quan sát được ở MỌI NGƯỜI: gặp người → body tự biết vị trí
    ✅ Quan sát được ở MỌI ĐỘNG VẬT xã hội: khỉ, gà, sói, cá
    ✅ Status thay đổi → behavior thay đổi → ai cũng trải nghiệm
    ✅ Somatic check: ai đọc cũng confirm "đúng, tôi cũng vậy"
    → = FUNCTION có thật, KHÔNG ai tranh cãi ✅

  HORMONE "Serotonin = hormone chính" — CHỈ LÀ CANDIDATE:

    Evidence CÓ (nhưng gián tiếp):
      🟢 Khỉ: rank correlate serotonin MÁU (Raleigh 1991)
         → NHƯNG: serotonin MÁU ≠ serotonin NÃO
         → 95% serotonin ở RUỘT → đo máu = đo ruột chủ yếu
      🟢 Khỉ: rank change → cortisol change (Sapolsky 30+ năm)
         → NHƯNG: đàn khỉ = 20-50 con, 1 hierarchy ĐƠN GIẢN
         → Người = hàng triệu, NHIỀU hierarchies chồng lấp
         → KHÔNG tương đương trực tiếp
      🟢 Người: rank công việc → health change (Whitehall Studies)
         → NHƯNG: KHÔNG đo serotonin — chỉ đo cortisol + health outcomes
      🟢 Người: SSRI (tăng serotonin) → tự tin hơn, social behavior đổi
         → Support serotonin liên quan → nhưng SSRI affect NHIỀU thứ

    Evidence THIẾU:
      ❌ Chưa có study đo serotonin NÃO trực tiếp ở người theo status
         (vì: đo serotonin não ở người sống = gần như impossible)
      ❌ Chưa có study so sánh serotonin: CEO vs nhân viên
      ❌ Serotonin máu ≈ serotonin não = chưa confirm
      ❌ Khỉ (20 con, 1 hierarchy) ≠ người (triệu, nhiều hierarchy)

  → Framework position:
    "Status FUNCTION = chắc chắn có (quan sát + somatic confirm)
     Serotonin = CANDIDATE hormone (evidence gián tiếp từ khỉ + SSRI)
     Có thể serotonin + hormone khác kết hợp
     Hormone chính xác = CHƯA PROVEN ở người
     FUNCTION name 'Status' dùng trong framework
     HORMONE name 'serotonin' chỉ ghi là candidate, không assert"

  → Giống Satisfaction Signal (prolactin = candidate, function = chắc chắn)
  → Framework bind vào FUNCTION, không bind vào hormone
  → Nếu research tương lai chứng minh hormone khác → function KHÔNG ĐỔI
```

---

## 10.6 Serotonin = Certainty BIAS Nền — PFC Quyết Định Thật Sự

```
⚠️ REFINE QUAN TRỌNG — serotonin KHÔNG "quyết định" schema nào chạy.

  CŨ (quá đơn giản):
    "Serotonin cao → tự tin → schema mở → triển khai"
    → Gợi ý: serotonin QUYẾT ĐỊNH → SAI

  MỚI (chính xác hơn):

  2 TẦNG KHÁC NHAU:

    TẦNG 1 — Serotonin nền (body-level, chậm, vô thức):
      = MỨC CHẮC CHẮN NỀN cho toàn hệ thống
      → Cao: body CẢM THẤY "nhìn chung ok" → BIAS tự tin nhẹ
      → Thấp: body CẢM THẤY "nhìn chung không chắc" → BIAS rụt rè nhẹ
      → Thay đổi CHẬM (tuần → tháng) theo experience tích lũy
      → = BIAS nền — KHÔNG PHẢI quyết định

    TẦNG 2 — PFC + Schema (imagine-level, nhanh, per-context):
      = QUYẾT ĐỊNH THỰC SỰ schema nào triển khai
      → PFC evaluate: "CỤ THỂ việc này, mình làm được không?"
      → Schema compiled: "đã làm 100 lần → chắc chắn" → auto
      → = OVERRIDE serotonin nền khi có data đủ

  TƯƠNG TÁC:
    Serotonin nền CAO + PFC chắc  → ✅✅ rất tự tin
    Serotonin nền CAO + PFC ko chắc → 🟡 dám thử (bias giúp)
    Serotonin nền THẤP + PFC chắc → ✅ vẫn làm (PFC override)
    Serotonin nền THẤP + PFC ko chắc → ❌ rụt rè (cả 2 block)

  VÍ DỤ — Người đang yêu:
    Serotonin nền: GIẢM (uncertainty love loop)

    Context yêu:
      PFC: "ko biết họ có thích mình không" → KHÔNG CHẮC
      + Serotonin nền thấp → BIAS rụt rè
      → ❌ Rụt rè, không dám hành động với người yêu

    Context cty:
      PFC: "việc này rõ ràng, mình làm 3 năm rồi" → CHẮC CHẮN
      + Serotonin nền thấp → BIAS rụt rè NHẸ
      + NHƯNG PFC override (data đủ mạnh)
      + THÊM: body đang hưng phấn vì yêu (dopamine, opioid) → energy CAO
      → ✅✅ Tự tin HƠN bình thường ở cty!
      → = Body hưng phấn + PFC chắc chắn = BOOST

    → = CÙNG người, CÙNG serotonin, KHÁC kết quả per-context
    → Vì: PFC certainty per-context + body state carry across contexts
    → = Serotonin là BIAS nền, PFC + body state QUYẾT ĐỊNH

  SEROTONIN CÓ NHIỀU FUNCTION (không chỉ Status):
    Function 1 — Certainty bias: mức chắc chắn NỀN
    Function 2 — Mood regulation: mood chung (irritable, calm)
    Function 3 — OCD link: uncertainty → check loop
    → 1 hormone → 3+ functions → THÊM lý do chỉ là CANDIDATE
    → Framework bind FUNCTION "certainty bias", không bind hormone
```

---

## 11. Status Trong Tập Thể — Ảnh Hưởng Loài

```
Status KHÔNG CHỈ cá nhân — ảnh hưởng CẤU TRÚC TẬP THỂ:

  Bầy đàn động vật:
    → Status hierarchy = cấu trúc TỔ CHỨC tự nhiên
    → Mỗi con biết vị trí → behavior predictable → nhóm STABLE
    → Alpha bệnh/chết → hierarchy SỤP → chaos → re-calibrate → stable lại
    → = Status = "phần mềm tổ chức" cho tập thể

  Xã hội loài người:
    → Hierarchy phức tạp hơn (multi-context, multi-dimension)
    → Nhưng CÙNG function: status maps → organize collective behavior
    → Pháp luật = FORMALIZE status maps ("ai được gì, phải gì")
    → Dân chủ = FLATTEN status (giảm gap → trao đổi > lấy/comply)
    → Độc tài = WIDEN status gap (lãnh đạo >> dân → lấy > trao đổi)
    → Chiến tranh = CALIBRATE status giữa TẬP THỂ (ai mạnh hơn?)

  Tương lai (Human-AI-Future.md):
    → AI status so với con người? → quyết định tương tác thế nào
    → AI > người → schema "AI lấy" sẵn sàng? → nguy hiểm
    → AI = người → schema "trao đổi" → symbiosis
    → AI < người → schema "AI comply" → tool
    → = ĐÚNG Status framework — mở rộng cho AI relationship
```

---

## 12. Câu Hỏi Mở

```
  Q1: Status scan VÔ THỨC — cơ chế neural chính xác?
      → Amygdala? STS (Superior Temporal Sulcus)? FFA?
      → Research có nhưng chưa gom vào framework

  Q2: Status Flexibility — hardware hay training?
      → Serotonin receptor variants → hardware?
      → Childhood experience → training?
      → Có thể cả 2 (giống PFC: hardware set range, experience chọn vị trí)

  Q3: Online Status (MXH) — cùng mechanism?
      → Likes = status signal? → body respond tương tự face-to-face?
      → Có thể: WEAKER (không có body presence)
      → Nhưng: tích lũy NHIỀU signals → cortisol/serotonin shift THẬT

  Q4: Status ở người CHƯA BAO GIỜ gặp ai (hermit)?
      → Internalized status từ quá khứ → VẪN CÓ maps
      → Nhưng: không có calibration mới → maps CÓ THỂ drift
      → = Status CẦN social contact để maintain accuracy
```

---

## 13. Kết Nối

```
→ Architecture-v7.5-Draft.md: §2.2 Layer3 Status (tóm tắt)
→ Core-v7-UD.md: §4.1 Lớp 2 (v7, sẽ update)
→ Prolactin-Analysis.md: Satisfaction Signal MƠ HỒ cho Status
→ Drive-Optimization.md: Status × Pressure/Challenge
→ Addiction-Analysis.md: Status addiction (likes, fame)
→ Human-AI-Future.md: Status AI vs Human
→ Body-Needs.md: Status trong 6 groups
→ Macro-Civilization.md: Status ở quy mô văn minh
```
