# Reward Channels — Draft Kiến Trúc Mới Cho Predictive-Drive

> **Trạng thái:** DRAFT — phác thảo kiến trúc mới, chưa quyết
> **Ngày:** 2026-03-23
> **Mục đích:** Tạo bảng reward channels tối ưu cho PREDICT hành vi con người
> **Nguyên tắc:** Focus vào "con người muốn gì → sẽ làm gì",
> KHÔNG cố nhồi toàn bộ hormone/mechanism vào 1 bảng
> **⚠️ File này là WORKSPACE — cần somatic confirm trước khi áp dụng.**

---

## 1. Tại Sao Chuyển Từ "Hormone Layers" Sang "Reward Channels"

```
VẤN ĐỀ:
  Não = mạng lưới đa chiều (có thể >3 chiều)
  Bảng 2D không thể chứa hết
  Cố nhồi mọi thứ vào 1 kiến trúc = rối + không dùng được

GIẢI PHÁP:
  Chọn GÓC NHÌN phù hợp với MỤC ĐÍCH framework

  Mục đích: Human-Predictive-Drive
    → Predict HÀNH VI con người
    → Cần biết: con người MUỐN GÌ → sẽ LÀM GÌ
    → Focus: REWARD CHANNELS = yếu tố quyết định chính

  Bảng hormone (Neurochemistry): vẫn giữ ở file riêng
    → Chi tiết mechanism cho ai muốn hiểu SÂU
    → Không nhồi vào Core

  Core chỉ cần:
    → Có N kênh reward
    → Mỗi kênh = 1 loại "sướng" (hoặc "tránh khổ")
    → Kênh nào đang thiếu → schema drive hành vi tìm
    → = Predict hành vi = biết kênh nào đang thiếu
```

---

## 2. Bảng Reward Channels

```
NGUYÊN TẮC PHÂN KÊNH:
  → Mỗi kênh = 1 loại REWARD KHÁC NHAU mà body nhận ra
  → Mỗi kênh = body FEEL khác nhau (somatic check được)
  → Mỗi kênh thiếu = HÀNH VI KHÁC NHAU (predict được)
  → Bao gồm cả "reward vì KHÔNG bị phạt" (threat-compensation)

2 NHÓM CHÍNH:

  PULL REWARDS (kéo tới — "muốn"):
    Body kéo về phía reward
    Có reward = sướng
    Thiếu reward = thèm, buồn, trống

  PUSH REWARDS (đẩy khỏi — "phải tránh"):
    Body đẩy khỏi punishment
    Tránh được = nhẹ nhõm
    Không tránh được = đau, sợ, lo
```

### 2.1 PULL Rewards — "Sướng vì ĐƯỢC"

```
┌─────────────┬────────────────┬────────────────┬────────────────┬────────────────┐
│ Kênh        │ Feel khi CÓ   │ Feel khi THIẾU │ Hành vi khi   │ Hormone chính  │
│             │ (body feel)    │ (body feel)    │ THIẾU (predict)│ (candidate)    │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ SENSORY     │ Ấm, ngon,     │ Tẻ nhạt, nhàm │ Tìm trải      │ Opioid         │
│ EXPERIENCE  │ sướng giác    │ body "đói"     │ nghiệm mới:   │ (mu-opioid)    │
│             │ quan, thỏa    │ trải nghiệm,  │ ăn ngon, du    │                │
│             │ mãn body      │ restless nhẹ   │ lịch, nhạc,    │                │
│             │               │                │ massage, sex   │                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ MASTERY     │ "Tôi làm      │ "Tôi vô dụng" │ Tìm thử thách │ Opioid +       │
│             │ được!", tự    │ bất lực,       │ vừa sức: game, │ Dopamine       │
│             │ hào, dòng     │ frustrated,    │ học skill mới, │ (completion    │
│             │ flow khi làm  │ chán kiểu      │ sửa đồ, code, │ reward)        │
│             │ tốt           │ stagnant       │ thể thao       │                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ CONNECTION  │ Ấm áp, an     │ Cô đơn, trống │ Tìm người:     │ Oxytocin       │
│             │ toàn, thuộc   │ vắng, body     │ gọi điện, gặp │                │
│             │ về, được      │ lạnh, co rúm   │ bạn, ôm, tâm  │                │
│             │ hiểu          │ trong          │ sự, group      │                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ NOVELTY     │ "Ồ thú vị!"  │ Chán, restless │ Tìm cái mới:  │ Dopamine       │
│             │ tò mò được    │ bồn chồn,     │ scroll MXH,    │ (phasic burst) │
│             │ thỏa mãn,    │ "muốn gì đó   │ khám phá, đọc, │                │
│             │ hào hứng      │ mà không biết" │ nơi mới, ý     │                │
│             │               │                │ tưởng mới      │                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ COHERENCE   │ "À, hiểu      │ Bối rối, khó  │ Tìm explanation│ Opioid +       │
│ (hiểu/ý    │ rồi!", mọi   │ chịu, "sao    │ hỏi tại sao,  │ Dopamine       │
│ nghĩa)     │ thứ khớp,    │ vô lý vậy?",  │ nghiên cứu,    │ (insight       │
│             │ hài lòng sâu │ bất an nền    │ xây framework, │ reward)        │
│             │               │                │ tôn giáo, triết│                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ AESTHETIC   │ Đẹp, rung     │ "Cuộc sống    │ Tìm cái đẹp:  │ Opioid         │
│ (thẩm mỹ)  │ động, body    │ xám xịt",     │ nghệ thuật,    │ (aesthetic     │
│             │ rùng mình     │ flat affect    │ thiên nhiên,   │ chills)        │
│             │ (chills)      │                │ design, thời   │                │
│             │               │                │ trang          │                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ COMFORT     │ Thoải mái,    │ Khó chịu body │ Tìm thoải mái:│ Opioid +       │
│ (thể chất) │ body ease,    │ đau mỏi,      │ nghỉ ngơi, tắm│ Endocannabinoid│
│             │ relaxed       │ căng, mệt     │ nóng, nằm, AC │                │
│             │               │                │ 20°C + chăn   │                │
└─────────────┴────────────────┴────────────────┴────────────────┴────────────────┘

  → 7 Pull channels
  → Map từ Layer1-Channels.md (E1-E5 + phần C)
  → Mỗi kênh: có thể FEEL bằng body (somatic check)
  → Mỗi kênh thiếu: PREDICT được hành vi tìm kiếm
```

### 2.2 CONNECTION Sub-channels — chi tiết hơn

```
┌─────────────┬────────────────┬────────────────┬────────────────┐
│ Sub-channel │ Feel khi CÓ   │ Feel khi THIẾU │ Hành vi khi   │
│             │               │                │ THIẾU          │
├─────────────┼────────────────┼────────────────┼────────────────┤
│ INTIMATE    │ Yêu thương    │ Cô đơn sâu,   │ Tìm partner,   │
│ (thân mật)  │ sâu, an toàn │ "không ai hiểu"│ tâm sự sâu     │
│             │ tuyệt đối    │                │                │
├─────────────┼────────────────┼────────────────┼────────────────┤
│ BELONGING   │ "Mình thuộc   │ Lạc lõng,      │ Tìm nhóm,      │
│ (thuộc về)  │ về đây"      │ outsider       │ cộng đồng,     │
│             │               │                │ team, club     │
├─────────────┼────────────────┼────────────────┼────────────────┤
│ BEING SEEN  │ "Họ hiểu      │ Invisible,     │ Chia sẻ, post  │
│ (được thấy) │ mình"        │ "không ai thấy"│ MXH, kể chuyện│
├─────────────┼────────────────┼────────────────┼────────────────┤
│ TOUCH       │ Ấm body,      │ "Skin hunger"  │ Ôm, massage,   │
│ (chạm)      │ an toàn vật lý│ cold body     │ thú cưng, chăn │
├─────────────┼────────────────┼────────────────┼────────────────┤
│ SHARED EXP  │ "Cùng trải    │ "Sướng mà     │ Rủ đi chơi,    │
│ (trải nghiệm│ nghiệm!"     │ không ai chia  │ xem phim cùng, │
│ chung)      │ nhân đôi joy │ sẻ = thiếu"   │ ăn cùng        │
└─────────────┴────────────────┴────────────────┴────────────────┘
```

### 2.3 PUSH Rewards — "Nhẹ nhõm vì TRÁNH ĐƯỢC"

```
┌─────────────┬────────────────┬────────────────┬────────────────┬────────────────┐
│ Kênh        │ Feel khi      │ Feel khi ĐANG  │ Hành vi khi   │ Hormone chính  │
│             │ TRÁNH ĐƯỢC    │ BỊ threat      │ bị threat     │ (candidate)    │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ PHYSICAL    │ "An toàn!",   │ Đau, sợ hãi,  │ Chạy, né,      │ Cortisol drop  │
│ SAFETY      │ nhẹ nhõm,    │ body freeze/   │ đánh lại,      │ + Endorphin    │
│             │ cortisol drop │ fight/flight   │ ẩn nấp         │ (buffer pain)  │
│             │               │                │ REFLEX (50ms)  │ NE + Adrenaline│
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ SOCIAL      │ "Không bị     │ Xấu hổ, nhục, │ Comply, xin    │ Cortisol drop  │
│ SAFETY      │ ghét/bỏ rơi" │ body nóng mặt, │ lỗi, thay đổi │ + Serotonin    │
│             │ nhẹ nhõm,    │ co rúm, muốn  │ behavior để    │ recover        │
│             │ "vẫn OK"     │ biến mất       │ fit in, hoặc  │                │
│             │               │                │ rebel          │                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ STATUS      │ "Vẫn được     │ "Tôi kém hơn" │ Làm thêm,      │ Serotonin      │
│ PROTECTION  │ công nhận"    │ lo lắng vị trí│ chứng minh,    │ (maintain)     │
│             │ self-worth    │ bất an nền    │ compare, khoe  │ Cortisol       │
│             │ stable        │ cortisol nền   │ khoang, hoặc  │ (sustain worry)│
│             │               │                │ rút lui (avoid)│                │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ FUTURE      │ "Đã chuẩn bị │ Lo lắng mơ hồ │ Plan, tiết     │ Cortisol drop  │
│ SECURITY    │ đủ rồi",     │ "nếu...thì sao"│ kiệm, bảo hiểm│ khi plan xong  │
│             │ "sẽ ổn"      │ PFC loop không │ học thêm,      │ Cortisol       │
│             │ cortisol thấp │ dừng, mất ngủ │ hustle "phòng  │ sustain khi    │
│             │               │ anxiety        │ thân"          │ chưa plan      │
├─────────────┼────────────────┼────────────────┼────────────────┼────────────────┤
│ MORAL       │ "Tôi là người│ Guilt, shame,  │ Xin lỗi, sửa  │ Cortisol drop  │
│ INTEGRITY   │ tốt", lương  │ "tôi sai rồi" │ sai, hoặc      │ khi resolve    │
│             │ tâm yên      │ body nặng nề   │ rationalize    │ Opioid nhẹ     │
│             │               │ khó chịu ngực │ (tự biện minh) │ (relief)       │
└─────────────┴────────────────┴────────────────┴────────────────┴────────────────┘

  → 5 Push channels
  → Reward = ABSENCE of bad (nhẹ nhõm, cortisol giảm)
  → KHÔNG có opioid/oxytocin reward trực tiếp
  → Chỉ có cortisol DROP + relief
  → = Reward KHÁC CHẤT so với Pull (sướng vs nhẹ nhõm)

  ⚠️ Push channels = drive PHỔ BIẾN nhất hiện đại:
    → Hầu hết người đi làm = Status Protection + Future Security
    → Trẻ em bị ép học = Social Safety + Status Protection
    → Anxiety disorders = Future Security loop không dừng
    → "Hustle culture" = mix Status Protection + Future Security
    → = Xã hội hiện đại drive chủ yếu bằng PUSH, ít PULL
```

---

## 3. PREDICT — Cách Dùng Bảng

```
CÔNG THỨC DỰ ĐOÁN:

  ① Xác định kênh nào đang THIẾU (hoặc bị threat):
     → Quan sát hành vi HOẶC body feel
     → Kênh thiếu = body signal rõ (xem cột "Feel khi thiếu")

  ② Predict hành vi:
     → Kênh thiếu → schema seek reward ở kênh đó
     → Xem cột "Hành vi khi thiếu" → predict action

  ③ Predict intensity:
     → Thiếu 1 kênh = drive VỪA
     → Thiếu nhiều kênh = drive MẠNH + có thể chaotic
     → Thiếu + bị PUSH threat = drive CỰC MẠNH (survival mode)

VÍ DỤ PREDICT:

  Case 1: Nhân viên văn phòng
    → Thiếu: Novelty (công việc lặp lại), Mastery (không học gì mới)
    → Đang bị: Status Protection (sợ bị sa thải)
    → Predict: scroll MXH (Novelty fill), chuyện phiếm (Connection fill),
      vẫn đi làm (Status Protection drive), muốn nghỉ việc nhưng sợ (conflict)

  Case 2: Trẻ bị bắt học
    → Thiếu: Novelty (bài cũ nhàm), Sensory Experience (ngồi 1 chỗ)
    → Đang bị: Social Safety (sợ bị mắng), Status Protection (sợ điểm thấp)
    → Predict: ngồi học nhưng không tập trung (comply surface),
      mơ màng (Novelty tự tạo), vẽ bậy (Sensory/Novelty fill),
      stress nền (Social Safety + Status Protection liên tục)

  Case 3: Người vừa nghỉ hưu
    → Mất: Mastery (không còn công việc), Status (mất vai trò),
      Belonging (mất đồng nghiệp), Future Security (thu nhập giảm)
    → Predict: trầm cảm/mất phương hướng (nhiều kênh thiếu cùng lúc)
      HOẶC tìm hobby (Mastery fill), tham gia hội nhóm (Belonging fill),
      chăm cháu (Connection fill) — tùy schema có sẵn

  Case 4: Người nghiện game
    → Game cung cấp: Novelty ✅, Mastery ✅, Being Seen ✅ (rank),
      Shared Experience ✅ (guild), Status ✅ (leaderboard)
    → Game KHÔNG cung cấp: Sensory thật ❌, Touch ❌, Intimate ❌,
      Physical Safety KHÔNG bị threat ❌ (game an toàn)
    → Predict: chơi liên tục (5+ kênh được fill bởi game),
      bỏ bê body needs (thiếu nhưng không aware vì game fill imagine),
      cô đơn sâu dù có guild online (thiếu Touch + Intimate)
```

---

## 4. PULL vs PUSH — Tại Sao Quan Trọng

```
🟡 2 loại reward KHÁC CHẤT:

  PULL reward khi đạt:
    → Opioid/Oxytocin release → body SƯỚNG
    → Satisfaction Signal CÓ THỂ fire → "đủ rồi"
    → = CÓ ĐIỂM DỪNG tự nhiên (body nói đủ)

  PUSH reward khi đạt:
    → Cortisol DROP → body NHẸ NHÕM
    → Satisfaction Signal KHÔNG rõ → "an toàn... nhưng bao lâu?"
    → = KHÔNG CÓ ĐIỂM DỪNG rõ ràng
    → Threat CÓ THỂ QUAY LẠI bất kỳ lúc nào
    → → PFC loop: "an toàn CHƯA? check lại... vẫn chưa chắc..."
    → → = Anxiety = PUSH reward loop KHÔNG DỪNG

  HỆ QUẢ:
    Người drive bởi PULL: có thể "đủ" → nghỉ → balance
    Người drive bởi PUSH: khó "đủ" → luôn cảnh giác → kiệt sức

  XÃ HỘI HIỆN ĐẠI:
    → PUSH drives chiếm ưu thế (deadline, competition, status, future worry)
    → PULL drives bị lấn át ("không có thời gian enjoy/connect")
    → = Cortisol baseline toàn cầu CAO
    → = Burnout, anxiety, depression tăng
    → Vì: PUSH không có Satisfaction Signal rõ → drive KHÔNG BAO GIỜ dừng

  PREDICT:
    Người drive chủ yếu bằng PULL → wellbeing TỐT hơn (có điểm dừng)
    Người drive chủ yếu bằng PUSH → wellbeing XẤU hơn (không có điểm dừng)
    → = Chuyển PUSH → PULL = cải thiện wellbeing
    → NHƯNG: xã hội + culture đang push PUSH (mâu thuẫn)
```

---

## 5. Satisfaction Signal — Hoạt Động Khác Nhau Theo Kênh

```
🟡 Không phải kênh nào cũng có Satisfaction Signal rõ:

  Satisfaction Signal RÕ (body nói "đủ" dễ):
    → Sensory: ăn no → đủ rõ ràng
    → Comfort: thoải mái → đủ rõ ràng
    → Touch: ôm đủ → đủ rõ ràng
    → Physical Safety: thoát nguy → đủ rõ ràng

  Satisfaction Signal MƠ HỒ (body nói "đủ" khó):
    → Novelty: bao nhiêu mới là "đủ mới"? → khó xác định
    → Mastery: giỏi cỡ nào là "đủ giỏi"? → khó xác định
    → Coherence: hiểu bao nhiêu là "đủ hiểu"? → khó xác định

  Satisfaction Signal GẦN NHƯ KHÔNG CÓ:
    → Status Protection: "an toàn" bao lâu? → PFC loop vô hạn
    → Future Security: "chuẩn bị đủ" chưa? → luôn có thể thêm
    → Social Safety: "họ có ghét mình không?" → check vô hạn

  → PULL channels: Satisfaction Signal hoạt động TỐT
  → PUSH channels: Satisfaction Signal hoạt động KÉM hoặc KHÔNG CÓ
  → = Confirm §4: PUSH drives không có điểm dừng tự nhiên
  → = Predict: người thiên về PUSH channels → overwork + anxiety
```

---

## 6. Status — Amplifier Đặc Biệt

```
🟡 Status KHÔNG phải reward channel thông thường:

  Status = AMPLIFY access tất cả channels khác:
    Status CAO → dễ access Sensory (tiền mua), Connection (người muốn gần),
      Novelty (cơ hội nhiều), Safety (ít bị threat)
    Status THẤP → khó access tất cả

  NHƯNG Status Aspiration Gap = TRIGGER cho Push channels:
    "Tôi chưa đủ tốt" → Status Protection drive
    "Nếu không cải thiện → hậu quả" → Future Security drive

  → Status = KHÔNG đặt trong bảng reward channels
  → Status = ĐẶT BÊN CẠNH bảng — amplify toàn bộ
  → Status Gap → feed vào Push channels (Status Protection, Future Security)

  Vị trí trong kiến trúc:
    ┌──────────────────────────────────────────┐
    │         STATUS (Amplifier)                │
    │  Position × Aspiration = access level     │
    │  Gap → trigger Push drives               │
    ├──────────────────────────────────────────┤
    │  PULL channels  │  PUSH channels         │
    │  (7 kênh)       │  (5 kênh)              │
    │  ↑ amplified    │  ← fed by status gap   │
    └──────────────────────────────────────────┘
```

---

## 7. Dopamine — Cross-cutting, Không Phải 1 Channel

```
🟡 Dopamine tham gia NHIỀU channels:

  Novelty channel: dopamine = CHÍNH (drive + reward)
  Mastery channel: dopamine tham gia (completion predict)
  Coherence channel: dopamine tham gia (insight reward)
  Status channel: dopamine tham gia (status gain predict)
  Mọi seeking behavior: dopamine = energy

  → Dopamine KHÔNG nằm ở 1 channel
  → Dopamine = SEEKING ENERGY cho MỌI channel đang active
  → + Dopamine = PRIMARY driver cho Novelty channel

  Tương tự:
    NE = ACTIVATION ENERGY cho mọi channel (gateway)
    Cortisol = SUSTAIN ENERGY cho Push channels (duy trì)
    Opioid = REWARD SIGNAL cho Pull channels (confirm)

  = 4 hormone CROSS-CUTTING — phục vụ mọi channel ở phase khác
  = KHÔNG đặt trong bảng channel — đặt ở layer bên dưới
```

---

## 8. Kiến Trúc Tổng Thể — Draft

```
🔴 DRAFT v0.2 — phác thảo:

  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │              STATUS (Amplifier + Trigger)                  │
  │     Position × Aspiration = access + push trigger          │
  │                                                            │
  ├────────────────────────────┬───────────────────────────────┤
  │                            │                               │
  │    PULL REWARD CHANNELS    │    PUSH REWARD CHANNELS       │
  │    ("sướng vì ĐƯỢC")       │    ("nhẹ vì TRÁNH ĐƯỢC")     │
  │                            │                               │
  │  ① Sensory Experience     │  ⑧ Physical Safety            │
  │  ② Mastery                │  ⑨ Social Safety              │
  │  ③ Connection (5 sub)     │  ⑩ Status Protection          │
  │  ④ Novelty                │  ⑪ Future Security            │
  │  ⑤ Coherence              │  ⑫ Moral Integrity            │
  │  ⑥ Aesthetic              │                               │
  │  ⑦ Comfort                │                               │
  │                            │                               │
  │  Reward: Opioid/Oxytocin  │  Reward: Cortisol DROP        │
  │  Satisfaction: RÕ          │  Satisfaction: MƠ HỒ/KHÔNG   │
  │  Có điểm dừng: CÓ         │  Có điểm dừng: KHÓ           │
  │                            │                               │
  ├────────────────────────────┴───────────────────────────────┤
  │                                                            │
  │              EXECUTION LAYER (cross-cutting)               │
  │                                                            │
  │  NE = Activation (gateway cho mọi hành vi)                │
  │  Dopamine = Seeking energy (amplify tìm kiếm)             │
  │  Adrenaline = Emergency energy (fight/flight)              │
  │  Cortisol = Sustain (duy trì drive kéo dài)               │
  │                                                            │
  ├────────────────────────────────────────────────────────────┤
  │                                                            │
  │              SCHEMA FRAME (xuyên suốt)                     │
  │                                                            │
  │  Schema detect body-need → fire drive ở channel tương ứng │
  │  Schema compiled = vô thức execute (Pull channels chủ yếu)│
  │  Schema draft = PFC engage (Novelty + Push channels)       │
  │  Schema gradient: body-need → values → domain skills       │
  │  Body Baseline State = ground truth                        │
  │                                                            │
  ├────────────────────────────────────────────────────────────┤
  │                                                            │
  │              FEEDBACK LOOP                                 │
  │                                                            │
  │  Drive → Behavior → Body Experience → Reward/Pain          │
  │  → Satisfaction Signal? → Schema update → Drive adjust     │
  │                                                            │
  │  Drive ↔ Satisfy:                                         │
  │    Drive: Schema → Body (phức tạp, orchestration)          │
  │    Satisfy: Body → Schema (đơn giản, 1 signal)            │
  │                                                            │
  └────────────────────────────────────────────────────────────┘
```

---

## 9. So Sánh Với Kiến Trúc Cũ

```
CŨ — 3 Lớp hormone:
  Lớp 1: Opioid + Oxytocin (Source)
  Lớp 2: Dopamine + Serotonin (Amplifier)
  Lớp 3: Cortisol, NE, ... (Modulator)
  → Focus: hormone → behavior
  → Ưu: đơn giản
  → Nhược: không rõ drive vs reward, thiếu Push channels

MỚI — Reward Channels:
  7 Pull + 5 Push + Status amplifier
  + Execution layer (NE, Dopamine, Adrenaline, Cortisol)
  + Schema frame + Feedback loop
  → Focus: reward → predict behavior
  → Ưu: predict được, phân biệt Pull/Push, có body feel check
  → Nhược: nhiều channels hơn (12 vs 5)

NHƯNG:
  → 12 channels = THỰC TẾ phức tạp hơn 5
  → 12 channels VẪN ĐƠN GIẢN hơn reality (não có hàng trăm sub-channels)
  → 12 channels = minimum viable model cho PREDICT

BACKWARD COMPATIBILITY:
  → 3 Lớp vẫn đúng cho REWARD MECHANISM (hormone nào fire khi nào)
  → Giữ ở Neurochemistry file
  → Core chuyển sang Reward Channels (predict-focused)
  → Không mâu thuẫn — 2 góc nhìn cho 2 mục đích khác nhau
```

---

## 10. Câu Hỏi Mở

```
🔴 Cần ngẫm:

  Q1: 7 Pull + 5 Push có đủ không? Có thừa không?
      → Aesthetic có phải channel riêng hay sub của Sensory?
      → Moral Integrity có phải channel riêng hay sub của Social Safety?

  Q2: Connection 5 sub-channels — cần tách riêng hay gom?
      → Gom = đơn giản hơn
      → Tách = chính xác hơn (mỗi sub feel KHÁC nhau)

  Q3: Mastery + Coherence — khác nhau thế nào?
      → Mastery = "tôi LÀM được"
      → Coherence = "tôi HIỂU được"
      → Có thể overlap — cần somatic check

  Q4: Bảng này có backward-compatible với 6 Body-Needs groups?
      → Body Basics ≈ Sensory + Comfort + Physical Safety
      → Connection ≈ Connection (5 sub)
      → Experience ≈ Sensory + Aesthetic
      → Mastery ≈ Mastery
      → Meaning ≈ Coherence
      → Regulation ≈ Comfort + Future Security?
      → Cần map kỹ hơn

  Q5: Game industry files cần update không?
      → 8 channels cũ → 12 channels mới?
      → Có thể giữ 8 (đủ cho game) + note 12 (full framework)

  → ĐỂ YÊN — ngẫm — quay lại khi somatic nói "khớp"
```

---

## 11. Kết Nối

```
→ Core-v7-UD.md: cần update nếu chuyển sang Reward Channels
→ Layer1-Channels.md: 10 sub-channels map vào Pull channels
→ Body-Needs.md: 6 groups → cần map sang 12 channels
→ Drive-Architecture-Draft.md: phân tích chi tiết hormone mechanism
→ Neurochemistry-v8-Draft.md: giữ 3 Lớp cho hormone detail
→ Threat-Drive-Analysis.md: chi tiết cho 5 Push channels
→ Status-Analysis.md: Status = Amplifier + Trigger
→ Prolactin-Analysis.md: Satisfaction Signal khác nhau theo channel
→ Addiction-Analysis.md: addiction = hijack channel
→ Game-Industry/Player-Psychology.md: 8 channels → update?
→ plan-update-v8.md: ghi note hướng restructure
```
