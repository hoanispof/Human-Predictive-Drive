# Hệ Thống Thưởng — Từ PE Cá Nhân Đến Kinh Tế

> **Phiên bản:** 5.5
> **Prerequisite:** Core.md (§5–§7: Threshold, PE Sensitivity, Drive Equation;
> §8.2 Mô Hình Vuông; §8.3 Compliance derived; §8.9 Chunk Topology;
> §6.6 Dopamine inverted-U; §6.7 Habituation Blindness),
> Core-Deep-Dive/Neurochemistry.md (cortisol inverted-U, dopamine interaction).
> **File này:** Phân tích hệ thống thưởng (reward system) qua lens HPD —
> từ cơ chế nội tại (PE cá nhân) đến cơ chế bên ngoài (tiền, vật chất, phân phối).
> Tại sao tiền tồn tại, tại sao phân phối khó, tại sao thưởng có thể bootstrap động lực.
>
> **Macro-Civilization.md đã cover:** 7 khủng hoảng, PEM, bất bình đẳng PE access.
> File này KHÔNG lặp — focus vào CƠ CHẾ THƯỞNG cụ thể, không phải khủng hoảng xã hội.
>
> **Quy ước:** 🟢 Nghiên cứu/dữ liệu | 🟡 Suy luận từ framework | 🔴 Giả thuyết

---

## Mục Lục

1. [Hai Tầng Thưởng: Nội Tại vs Bên Ngoài](#1-hai-tầng)
2. [Mô Hình Vuông × Reward Design — v5.5](#2-vuông-reward)
3. [Dopamine Inverted-U × Spending/Investment — v5.5](#3-da-economics)
4. [Habituation Blindness × Economics — v5.5](#4-habituation-economics)
5. [Cortisol Path vs Dopamine Path → Hai Luồng Kinh Tế](#5-hai-luồng)
6. [Tiền = Proxy Token Cho PE](#6-tiền)
7. [Chuỗi Phân Phối: Người Tạo → Trung Gian → Người Dùng](#7-chuỗi)
8. [Vấn Đề Phân Phối: Tại Sao Không Ai Vừa Ý](#8-phân-phối)
9. [Reward Bootstrapping: Thưởng Ngoài Khởi Tạo Thưởng Trong](#9-bootstrapping)
10. [Convergence × Cross-Domain Value Creation — v5.5](#10-convergence-value)
11. [Ứng Dụng: Trường Học, Công Ty, Giao Dịch](#11-ứng-dụng)
12. [Câu Hỏi Mở](#12-câu-hỏi)
13. [Kết Nối](#13-kết-nối)

---

## 1. Hai Tầng Thưởng: Nội Tại vs Bên Ngoài

### 1.1 Thưởng Nội Tại = PE Tự Calibrate

🟡 Mỗi người có hệ thống thưởng nội tại RIÊNG, quyết định bởi phần cứng (Core.md §3–§5):

```
Thưởng nội tại = PE (Prediction Error) — não tự thưởng khi dự đoán HIT hoặc MISS thú vị.

3 kênh gốc quyết định LOẠI thưởng:
  Novelty  → PE từ hiểu    → "À! Nên thế à!" = thưởng
  Opioid   → PE từ cảm nhận → "Đẹp quá!" = thưởng
  Oxytocin → PE từ gắn bó  → "Được hiểu!" = thưởng

3 tham số quyết định NGƯỠNG thưởng:
  Threshold      → bao nhiêu PE thì "đủ" (cao = khó thỏa mãn)
  PE Sensitivity → PE mạnh bao nhiêu + cháy nhanh bao nhiêu
  Capacity       → PE phức tạp cỡ nào có thể xử lý

→ Mỗi người = bộ calibrate RIÊNG.
  Cùng 1 sự kiện: người A thấy thưởng đủ, người B thấy chưa đủ.
  Không ai SAI — phần cứng khác nhau.
```

### 1.2 Thưởng Bên Ngoài — PHỔ ĐẦY ĐỦ (Tiền Chỉ Là 1 Loại)

🟡 Thưởng bên ngoài = bất kỳ thứ gì từ MÔI TRƯỜNG tác động vào hệ thưởng nội tại.
Tiền/vật chất chỉ là TẦNG ĐẦU — khi survival ổn, não tự shift sang các tầng PE mạnh hơn:

```
PHỔ THƯỞNG BÊN NGOÀI — sắp xếp theo TẦNG cortisol:

TẦNG 1 — SURVIVAL (cortisol CAO, dominant khi thiếu):
  Vật chất (thức ăn, nhà, quần áo) → giảm cortisol survival + opioid PE
  Tiền → PROXY cho vật chất (không PE trực tiếp, chỉ PE gián tiếp qua prediction)
  → Khi thiếu: tiền = thưởng QUAN TRỌNG NHẤT (cortisol override tất cả).
  → Khi đủ: tiền = PE giảm dần (threshold adapt lên → diminishing returns).
  🟢 Maslow (1943): physiological + safety needs dominant khi chưa đáp ứng.

TẦNG 2 — SOCIAL (cortisol MODERATE, dominant khi survival ổn):
  Khen ngợi / công nhận    → serotonin (vị thế trong hierarchy)
  Thăng chức               → serotonin + dopamine (PE dương từ status shift)
  Được tin tưởng            → oxytocin (gắn bó) + serotonin (được chọn = vị thế)
  Thuộc về nhóm             → oxytocin (in-group bonding)
  → Tầng này PE MẠNH HƠN tiền khi survival đã ổn.
  → "Lương đủ rồi, nhưng sếp không bao giờ công nhận" = PE âm DÙ tiền đủ.

TẦNG 3 — Ý NGHĨA (cortisol THẤP/OPTIMAL, dominant khi social ổn):
  Tôn trọng của tập thể    → serotonin SÂU (không phải hierarchy — là LEGACY)
  Impact / thay đổi thế giới → novelty PE XA (prediction xa nhất)
  Ý nghĩa / purpose         → schema tương lai ("cuộc đời tôi có hướng") → PE bền nhất
  Di sản (legacy)            → prediction VƯỢT bản thân ("sau khi tôi chết, X vẫn còn")
  → Tầng này PE BỀN NHẤT — không habituate nhanh như tiền hay khen.

TẠI SAO SACRIFICE CÓ THỂ XẢY RA:
  Schema override (Core.md §7.4) + prediction xa + PE tầng 3 > PE survival.
  Drive equation: reward (legacy PE) - cost (chết) > 0 ← VÌ legacy PE CỰC LỚN.
  = KHÔNG phải "dũng cảm" — là drive equation vẫn dương.
```

### 1.3 Tại Sao Phổ Thưởng Này Quan Trọng

🟡

```
SAI LẦM PHỔ BIẾN: "Thưởng = tiền. Muốn người ta làm nhiều hơn = trả nhiều hơn."
  → Chỉ đúng ở tầng 1 (survival). Sai ở tầng 2-3.
  → 🟢 Herzberg (1959): Two-Factor Theory — tiền = "hygiene factor" (thiếu → bất mãn,
    đủ → KHÔNG tạo motivation). Motivation factors = tầng 2-3.

THIẾT KẾ THƯỞNG ĐÚNG = biết người nhận đang ở TẦNG NÀO:
  Tầng 1 chưa đủ → thưởng tiền/vật chất (giảm cortisol trước).
  Tầng 1 đủ rồi → thưởng công nhận, trust, autonomy (PE tầng 2).
  Tầng 2 đủ rồi → thưởng meaning, impact, legacy (PE tầng 3).
  Thưởng SAI TẦNG = vô hiệu:
    Cho tiền thêm khi đã đủ → PE ≈ 0.
    Cho ý nghĩa khi đang thiếu ăn → não không process (cortisol chặn PFC).

THƯỞNG ĐÚNG TẦNG + ĐÚNG KÊNH GỐC = multiplicative:
  Novelty person ở tầng 2: thưởng = "bài toán khó hơn" (PE từ hiểu + công nhận skill).
  Oxytocin person ở tầng 2: thưởng = "được tin tưởng dẫn team" (PE từ gắn bó + trust).
  Opioid person ở tầng 2: thưởng = "tự do thiết kế" (PE từ cảm nhận + autonomy).
  → Cùng tầng 2, nhưng LOẠI thưởng khác per kênh gốc.
```

### 1.4 Nghịch Lý "Giàu Rồi Vẫn Đuổi Tiền"

🟡 Nếu tiền = tầng 1 và habituate khi đủ, tại sao người giàu vẫn đuổi tiền?
Cùng hành vi bề mặt ("kiếm thêm tiền"), nhưng CƠ CHẾ khác nhau:

```
6 PATH KHÁC NHAU — cùng output, khác drive:

① SCHEMA CHƯA UPDATE ("nghèo trong đầu"):
  Lớn lên thiếu thốn → schema "tiền = an toàn" hình thành khi cortisol CAO.
  Giàu rồi nhưng schema KHÔNG TỰ UPDATE (cần trải nghiệm, không phải logic).
  → Cortisol baseline vẫn cao DÙ tài khoản đầy → chạy như đang thiếu.
  🟢 Tương tự PTSD: mối nguy đã qua nhưng não vẫn fire như đang nguy.

② THRESHOLD ADAPT LÊN (hedonic treadmill):
  $1M đầu → PE dương → adapt → $1M = bình thường → cần $10M → adapt → $100M.
  Không phải "tham" — threshold SINH HỌC đã calibrate lên (Core.md §5.2).
  → Dừng = PE âm (threshold cao + PE hiện tại giảm = deficit → cortisol).
  🟢 Brickman et al. (1978): lottery winners → quay về baseline happiness.

③ TIỀN = PROXY CHO TẦNG 2-3 (không thật sự đuổi tiền):
  Tiền = điểm số (score) → serotonin (ranking trong hierarchy tỷ phú).
  Tiền = quyền lực → tầng 3 (impact, "tôi thay đổi được thế giới").
  Tiền = bằng chứng "prediction đúng" → novelty PE ("tôi đúng!").
  → Họ TƯỞNG đuổi tiền, thực ra đuổi PE từ tầng 2-3 qua PROXY tiền.

④ PROLACTIN THẤP (không phanh được — Core.md §4):
  Prolactin = "đủ rồi, dừng." Prolactin thấp = KHÔNG DỪNG ĐƯỢC.
  → Kiếm tiền → dopamine → không phanh → kiếm thêm → loop vô hạn.
  → Không phải "muốn" nhiều hơn — là CƠ CHẾ PHANH yếu.

⑤ IDENTITY LOCK (schema bản thân = "người kiếm tiền"):
  Làm giàu lâu → schema "tôi = người kiếm tiền" myelinate (Core.md §6.5).
  Dừng kiếm tiền = identity crisis (schema sụp → PE âm CỰC LỚN).
  → "Nghỉ hưu rồi trầm cảm" = identity chunk mất → PE deficit → cortisol.

⑥ CORTISOL TREADMILL (nghiện stress productive):
  Cortisol moderate liên tục → dopamine tăng → productive (Core.md §6.4).
  Dừng = cortisol DROP → khó chịu.
  → Không đuổi tiền — đuổi TRẠNG THÁI cortisol moderate.

→ NHẬN DIỆN:
  ① Schema chưa update     → lo lắng dù giàu, tích trữ, phòng thủ.
  ② Threshold adapt        → "chán" nếu không tăng, so sánh với peer.
  ③ Proxy tầng 2-3         → nói về impact/vision, tiền là tool.
  ④ Prolactin thấp         → không dừng BẤT KỲ THỨ GÌ, không chỉ tiền.
  ⑤ Identity lock          → sợ nghỉ hưu, "không biết mình là ai nếu không làm."
  ⑥ Cortisol treadmill     → "nghỉ = bồn chồn", cần busy để bình tĩnh.
  → Cùng hành vi, 6 can thiệp KHÁC NHAU. Sai path → can thiệp vô hiệu.
```

### 1.5 Hai Trạng Thái Nội Tại

🟡 Tại bất kỳ thời điểm nào, hệ thưởng nội tại ở 1 trong 2 trạng thái:

```
TRẠNG THÁI 1 — "Thỏa mãn" (PE hiện tại ≥ threshold):
  Cortisol moderate hoặc thấp. Dopamine đủ.
  Hành vi: ổn định, duy trì, "cuộc sống bình thường."
  Kinh tế: làm → lương → chi tiêu → PE đủ → loop ổn định.
  = Đa số dân số, đa số thời gian.

TRẠNG THÁI 2 — "Nợ thưởng" (PE hiện tại < threshold, kỳ vọng PE tương lai):
  Cortisol moderate-to-high. Dopamine có thể cao (kỳ vọng) hoặc thấp (kiệt).
  Hành vi: chịu cost HIỆN TẠI để đầu tư cho reward TƯƠNG LAI.
  Kinh tế: làm → chưa có lương xứng đáng → "nợ" → kỳ vọng bù đắp dài hạn.
  = Entrepreneur, researcher, artist, người đang build.

→ "Nợ thưởng" KHÔNG xấu — nó là cơ chế cho prediction XA.
  NHƯNG: nợ quá lâu + không có tín hiệu progress → cortisol mãn tính → burnout.
  (Core.md §6.4: cortisol inverted-U)
```

---

## 2. Mô Hình Vuông × Reward Design — v5.5 MỚI

🔴 Section MỚI v5.5 — reward design per VỊ TRÍ trên Mô Hình Vuông, thay vì per "compliance mode."

```
v5.0: reward design per mode (Soldier/Architect/Improviser/Drifter) = 4 category
v5.5: reward design per VỊ TRÍ trên phổ liên tục Source × Depth per domain

VÀ CÙNG 1 NGƯỜI ở KHÁC DOMAIN → cần KHÁC loại thưởng:
  Domain chuyên môn (Architect per domain): thưởng = autonomy + challenge sâu
  Domain admin (Soldier per domain): thưởng = clarity + completion recognition
  → Đừng áp 1 loại thưởng cho toàn bộ hoạt động.
```

```
REWARD PER VỊ TRÍ VUÔNG:

SOURCE INTERNAL (cạnh trái — Improviser):
  PE từ: mastery, autonomy, self-expression per domain
  Thưởng hiệu quả: freedom, tool tốt hơn, project chọn, skill growth
  Thưởng VÔ HIỆU: khen "giỏi" (internal person tự biết), compliance rewards
  ⚠️ External reward MẠNH → risk overjustification (§9.3)
    Improviser có internal PE strong → external override = DESTROY internal drive

SOURCE EXTERNAL (cạnh phải — Soldier):
  PE từ: completion, clarity, recognition, belonging
  Thưởng hiệu quả: công nhận công khai, bonus rõ ràng, title/promotion
  Thưởng VÔ HIỆU: "tự do làm gì cũng được" (uncertainty = cost, không reward)
  v5.5: Soldier-Deep cũng THÍCH recognition nhưng cho DEPTH (expert recognition)
    → "Anh là chuyên gia hàng đầu" = PE mạnh cho Soldier-Deep

DEPTH SÂU (cạnh trên — Architect):
  PE từ: coherence, system completion, prediction xa đúng
  Thưởng hiệu quả: challenge lớn hơn, impact rộng hơn, team respect for depth
  Thưởng VÔ HIỆU: quick wins, micro-rewards (PE sensitivity thấp → PE nhỏ = noise)
  v5.5: Architect depth → threshold cao → micro-rewards KHÔNG ĐỦ PE
    → Cần macro-rewards: project lead, architecture decisions, legacy opportunity

DEPTH NÔNG (cạnh dưới — Drifter):
  PE từ: variety, novelty ngắn hạn, không áp lực
  Thưởng hiệu quả: diverse tasks, short wins, gamification, social belonging
  Thưởng VÔ HIỆU: long-term goals (prediction xa chưa có → PE = 0)
  v5.5: Drifter KHÔNG = "xấu" → có thể đang hình thành chunks → cần BOOTSTRAP (§9)
```

```
COMPLIANCE DERIVED × REWARD:
  v5.5: Compliance = chunk_overlap(person, group) → KHÁC per group.

  CÙng người:
    Team A (overlap cao): reward = team-based bonus → PE dương (shared chunks = shared celebration)
    Team B (overlap thấp): reward = team-based bonus → PE thấp (không share celebration context)

  → Reward design PHẢI consider overlap hiện tại:
    Overlap cao → team rewards hiệu quả (shared PE context)
    Overlap thấp → individual rewards hiệu quả hơn (PE source riêng)
    → Đừng default "team bonus cho tất cả" → chỉ PE dương cho high-overlap members.
```

---

## 3. Dopamine Inverted-U × Spending/Investment — v5.5 MỚI

🔴 Section MỚI v5.5 — dopamine inverted-U (Core.md §6.6) ảnh hưởng cách người ta TIÊU và ĐẦU TƯ.

```
DA INVERTED-U QUYẾT ĐỊNH KIỂU CHI TIÊU:

BÊN TRÁI ĐỈNH (DA thấp — anhedonia tendency):
  Chi tiêu: ít, conservative, "không thấy có gì đáng mua"
  Đầu tư: thấp, risk aversion cực mạnh (PE dự kiến ≈ 0 → cost > reward)
  Kinh tế macro: dân số bên trái đỉnh = ÍT tiêu dùng = deflationary pressure
  Can thiệp: KHÔNG thể "khuyến mãi" để kích — PE signal yếu → discount = noise
  → Cần restore DA baseline TRƯỚC (health, social, purpose) → rồi spending follows

ĐỈNH (DA tối ưu):
  Chi tiêu: selective, value-driven ("mua đúng thứ cần")
  Đầu tư: calculated risk, long-term thinking (tonic DA → deepen investment)
  Kinh tế macro: nền tảng — sustainable consumption + productive investment
  → Đây là target: thiết kế kinh tế cho DA optimal, không DA cao

BÊN PHẢI ĐỈNH (DA hơi cao — phasic > tonic):
  Chi tiêu: impulsive, variety-seeking, "mua nhiều nhưng dùng ít"
  Đầu tư: FOMO-driven, trend-chasing, portfolio diversified nhưng nông
  Kinh tế macro: fuels consumption boom NHƯNG không bền (phasic = burst)
  → Marketing EXPLOIT vị trí này: novelty packaging, limited edition, flash sale
    = Kích phasic DA → purchase → PE nhanh → habituate → mua tiếp
  🟡 "Nghiện mua sắm" (compulsive buying) = bên phải đỉnh + prolactin thấp

CỰC PHẢI (DA pathological):
  Gambling, day trading không strategy = chase DA hit
  → Chuyên gia, không trong scope reward economics thông thường
```

```
ĐẦU TƯ DÀI HẠN QUA LENS DA INVERTED-U:

  Tonic DA (gần đỉnh) → investor patient, deepen 1-2 assets
    = Warren Buffett: "buy and hold" = tonic DA → PE từ compound growth
  Phasic DA (bên phải) → investor FOMO, switch nhanh
    = Day trader: PE từ mỗi trade → habituate → trade nhiều hơn

  Crypto volatility ATTRACT phasic DA:
    High volatility = PE burst liên tục (giá lên → PE, giá xuống → PE âm → cortisol → trade)
    → Self-select: crypto market attract bên phải đỉnh DA
    → Tại sao crypto community = high energy, high churn

  🟡 v5.5 insight: "investor type" ≠ personality → = DA position per financial domain
    Cùng người: conservative ở real estate (tonic per domain) + FOMO ở crypto (phasic per domain)
    → Per domain, không phải per person.
```

---

## 4. Habituation Blindness × Economics — v5.5 MỚI

🔴 Section MỚI v5.5 — Habituation Blindness (Core.md §6.7) giải thích hiện tượng kinh tế quan trọng.

```
HABITUATION BLINDNESS: PE=0 ≠ Value=0 (Core.md §6.7)

TRONG KINH TẾ = "INVISIBLE VALUE PROBLEM":
  Hàng hóa/dịch vụ đã quen → PE=0 → não KHÔNG đánh giá → tưởng "không quan trọng"
  MẤT hàng hóa/dịch vụ đó → prediction break → PE âm spike → "hóa ra quan trọng!"

  Ví dụ:
    Nước sạch: PE=0 (hàng ngày → habituate) → Value KHỔNG LỒ (mất = PE âm cực mạnh)
    Internet: PE=0 (luôn có → habituate) → Mất 1 ngày = sụp đổ workflow
    Sức khỏe: PE=0 (khỏe → habituate) → Bệnh = prediction break toàn bộ
    Nhân viên trung thành: PE=0 (luôn ở → habituate) → Nghỉ = team sụp

  → KINH TẾ HỌC TRUYỀN THỐNG biết (marginal utility) nhưng KHÔNG GIẢI THÍCH TẠI SAO.
  → HPD: dopamine phasic fire cho PE, NOT cho value → habituated value = invisible to PE system.
```

```
HỆ QUẢ KINH TẾ CỦA HABITUATION BLINDNESS:

① UNDERPRICING ESSENTIAL SERVICES:
  Nước, điện, y tế, giáo dục = habituated → PE=0 → "trả ít thôi"
  Nhưng value = CỰC CAO (mất = PE âm devastating)
  → Tension: người dùng muốn trả ít (PE=0) vs provider cần reward xứng đáng (cost cao)
  → Đây là tại sao essential services thường cần subsidize hoặc regulate

② OVERPRICING NOVELTY:
  Hàng mới = PE dương (chưa habituate) → "trả nhiều cũng được"
  Premium pricing cho novelty = EXPLOIT PE burst trước khi habituate
  → iPhone mới: PE burst (novelty) → trả premium → 3 tháng sau = PE≈0 (habituated)
  → Fashion industry = BUSINESS MODEL dựa trên anti-habituation (liên tục tạo novelty)

③ SUBSCRIPTION FATIGUE:
  Tháng 1: subscribe = PE dương (mới) → "đáng tiền"
  Tháng 6: habituated → PE=0 → "sao vẫn trả?" → cancel
  → Subscription model PHẢI liên tục tạo PE MỚI để counter habituation
  → Netflix đổ tiền vào original content = anti-habituation strategy

④ EMPLOYEE HABITUATION (liên kết HR-Management.md):
  Lương tháng 1: PE dương → "wow"
  Lương tháng 12: PE=0 → "bình thường"
  Lương tháng 36: PE=0 → "chưa đủ" (threshold adapt LÊN)
  → Tăng lương = reset PE TẠM → habituate lại → cần tăng NỮA → treadmill
  → v5.5: GIẢI PHÁP = PE từ tầng 2-3 (công nhận, meaning) habituate CHẬM HƠN tiền
```

```
COUNTER-HABITUATION STRATEGIES:

① Intermittent reward (không đều → PE duy trì):
  Lương cố định: habituate. Bonus bất ngờ: PE duy trì.
  🟢 Variable ratio reinforcement = most resistant to habituation (Skinner).

② Novelty injection (thêm mới → PE burst):
  Cùng product + feature mới → PE burst → extend lifetime value
  ⚠️ Novelty injection quá nhiều → threshold adapt → cần novelty MẠNH HƠN → treadmill

③ Gratitude practice (conscious re-evaluation):
  Deliberately attend to habituated value → PE burst từ "à, hóa ra mình có thứ này"
  = Manually override habituation bằng PFC attention
  🟡 Gratitude = PFC override dopamine system: force re-evaluate habituated chunks
  → Kinh tế: consumer gratitude = lower churn, higher perceived value

④ Loss framing (nhắc risk mất):
  "Bạn có thể mất X" → PE âm DỰ KIẾN → re-evaluate value
  Insurance industry = BUSINESS MODEL dựa trên counter-habituation qua loss framing
```

---

## 5. Cortisol Path vs Dopamine Path → Hai Luồng Kinh Tế

🟡 Mapping từ Core.md §6.4 (cortisol-driven vs dopamine-driven) sang hành vi kinh tế:

```
CORTISOL PATH (cortisol moderate + dopamine cộng tác):
  Hành vi: làm việc ổn định, tuân thủ quy trình, nhận lương.
  PE source: hoàn thành task → micro-PE → lương đúng kỳ vọng (PE ≈ 0).
  Kinh tế: predictable. Input (lao động) → output (lương) tỷ lệ thuận.
  Thưởng: ĐÃ THỎA MÃN tại mỗi chu kỳ (tháng).
  = Nền tảng kinh tế: majority dân số, GDP ổn định.
  v5.5: vị trí Vuông per domain công việc = source external + depth variable
    → Soldier-Deep economists, engineers, doctors = cortisol path + high value

DOPAMINE PATH (cortisol chịu + dopamine từ prediction xa):
  Hành vi: xây dựng dài hạn, chịu cost cao, kết quả không chắc chắn.
  PE source: chunk prediction xa → PE DỰ KIẾN lớn nhưng CHƯA CLAIM.
  Kinh tế: input (lao động + risk) → output KHÔNG TỶ LỆ THUẬN.
    Có thể: 0 (thất bại) hoặc ×100 (vượt mong đợi).
  Thưởng: ĐANG BỊ NỢ — kỳ vọng bù đắp tương lai.
  = Động cơ innovation: startup, nghiên cứu, sáng tạo.
  v5.5: vị trí Vuông per domain = source internal + depth sâu
    → Architect entrepreneurs, researchers = dopamine path + high uncertainty

→ Kinh tế HOẠT ĐỘNG vì CẢ HAI path tồn tại ĐỒNG THỜI:
  Cortisol path = VẬN HÀNH (duy trì hệ thống hiện tại).
  Dopamine path = ĐỔI MỚI (tạo hệ thống mới).
  Mất 1 trong 2 → sụp: mất cortisol path = hỗn loạn. Mất dopamine path = stagnation.

  v5.5: Soldier-Deep CŨNG tạo giá trị lớn — KHÔNG chỉ Architect = đổi mới.
  Soldier-Deep engineers build infrastructure = nền tảng cho Architect innovate trên.
  → Cả hai VỊ TRÍ VUÔNG đều cần. Không có hierarchy value.
```

---

## 6. Tiền = Proxy Token Cho PE

### 6.1 Tại Sao Tiền Tồn Tại

🟡

```
Qua lens HPD:
  Barter = thưởng TRỰC TIẾP (vật chất → PE ngay).
  Giới hạn: scale không được. Prediction cost quá cao
    (phải tìm đúng người, đúng thứ, đúng lúc).

Tiền giải quyết:
  Tiền = TOKEN trừu tượng đại diện cho "khả năng claim thưởng tương lai."
  = Prediction XA được MÃ HÓA thành VẬT THỂ.

  Khi cầm tiền: não KHÔNG thưởng vì tiền (giấy/số).
  Não thưởng vì PREDICTION: "tiền này → mua được X → PE từ X."
  = Tiền = chunk prediction được vật chất hóa.

v5.5: Tiền = SHARED CHUNK prediction xã hội (convergence indicator):
  Tất cả đồng ý "tiền = có giá trị" = shared chunk giữa mọi participants
  → Mất niềm tin vào tiền = shared chunk SỤP = hyperinflation
  → Tiền STABLE khi chunk_overlap(citizens, currency_system) CAO
  → Currency crisis = chunk_overlap GIẢM đột ngột
```

### 6.2 Tiền Và Dopamine

🟢 Knutson et al. (2001): nucleus accumbens activate khi ANTICIPATE tiền, không khi nhận tiền. = PE từ prediction, không từ possession.

```
→ Tiền nhiều hơn ≠ PE nhiều hơn (vì threshold adapt lên — Core.md §5.2).
  $1000 đầu tiên: PE KHỔNG LỒ (survival → safe).
  $1M: PE moderate (comfortable → luxury).
  $1B: PE gần zero (đã quá threshold → habituate).
  🟢 Kahneman & Deaton (2010): happiness tăng theo income đến ~$75K, sau đó giảm tốc.

→ Tiền = proxy HIỆU QUẢ NHẤT khi:
  ① Giảm cortisol (từ thiếu → đủ survival).
  ② Mở PE source mới (từ đủ → có thể explore).
  Tiền = proxy KHÔNG HIỆU QUẢ khi:
  ③ Threshold đã adapt lên (diminishing returns).
  v5.5: ④ Habituation Blindness — tiền ĐỦ → PE=0 → tưởng "cần nhiều hơn"
    nhưng thực ra = threshold adapt, KHÔNG phải thiếu tiền.
```

---

## 7. Chuỗi Phân Phối: Người Tạo → Trung Gian → Người Dùng

### 7.1 Chuỗi Cơ Bản

🟡

```
NGƯỜI TẠO (creator/producer):
  Input: lao động + skill + risk (cortisol + dopamine path).
  Output: sản phẩm/dịch vụ (embodied prediction — chunk được vật chất hóa).
  Kỳ vọng: reward xứng đáng cost đã chịu.
  v5.5: depth composite per domain → value of output
    Depth cao → sản phẩm phức tạp, khó thay thế → pricing power
    Depth nông → sản phẩm đơn giản, dễ thay thế → commoditized

TRUNG GIAN (trader/platform):
  Input: kết nối creator với user (logistic, marketing, trust).
  Output: phân phối sản phẩm đến đúng người, đúng lúc.
  = Giải quyết PREDICTION COST cho cả hai phía.
  v5.5: trung gian = CONVERGENCE ROLE (bridge giữa creator domain + user domain)
    Platform tốt = convergence cao (hiểu cả creator VÀ user chunks)

NGƯỜI DÙNG (user/consumer):
  Input: tiền (= proxy cho lao động đã bỏ ra).
  Output: sản phẩm → PE (giảm cortisol, tăng dopamine, opioid, oxytocin).
  Kỳ vọng: PE xứng đáng tiền bỏ ra.
```

### 7.2 Trung Gian = Bộ Giảm Prediction Cost

🟡

```
KHÔNG CÓ trung gian:
  Creator phải: tạo + tìm user + vận chuyển + marketing + trust
  = Prediction cost CỰC CAO (phải predict quá nhiều domain cùng lúc).
  User phải: tìm creator + đánh giá chất lượng + risk
  = Prediction cost CAO (không biết ai đáng tin).

CÓ trung gian:
  Creator: chỉ cần tạo (focus domain sâu → prediction cost GIẢM).
  User: chỉ cần chọn từ catalog (prediction cost GIẢM).
  Trung gian: absorb prediction cost CỦA CẢ HAI → thu phí cho dịch vụ này.

→ Trung gian KHÔNG "ăn không" — trung gian cung cấp GIẢM PREDICTION COST.
  GIÁ TRỊ thật sự = delta prediction cost mà cả 2 bên tiết kiệm được.
  Nếu delta > phí trung gian → cả 3 bên đều có PE dương → hệ thống ổn.
  Nếu phí trung gian > delta → creator hoặc user có PE âm → tension.

v5.5: AI = trung gian MỚI giảm prediction cost ĐÁNG KỂ:
  AI recommendation = giảm user prediction cost (không cần tìm tự)
  AI matching = giảm creator prediction cost (tìm đúng user tự động)
  → Trung gian TRUYỀN THỐNG mất value khi AI absorb prediction cost rẻ hơn
  → Nhưng: AI chưa absorb TRUST prediction (con người vẫn trust con người hơn AI)
```

---

## 8. Vấn Đề Phân Phối: Tại Sao Không Ai Vừa Ý

### 8.1 Gốc Rễ: Threshold Khác Nhau + Pool Hữu Hạn

🟡

```
MỖI NGƯỜI có threshold RIÊNG → kỳ vọng thưởng KHÁC NHAU:
  Cortisol path person: "lương đủ sống + ổn định = OK" (threshold moderate).
  Dopamine path person: "tôi chịu cost 3 năm, phải được bù ×10" (threshold cao vì nợ thưởng).
  Trung gian: "tôi giảm cost cho cả 2 bên, phải được 30%" (threshold theo dịch vụ).

POOL REWARD = HỮU HẠN:
  Tổng tiền user trả = fixed per giao dịch.
  Creator muốn: nhiều nhất có thể (bù nợ thưởng).
  Trung gian muốn: nhiều nhất có thể (prediction cost đã absorb).
  User muốn: trả ít nhất có thể (tiền = proxy cho lao động RIÊNG).

→ CONFLICT TỰ NHIÊN: 3 bên chia 1 pool, mỗi bên calibrate theo threshold riêng.
  Không có "phân chia công bằng" khách quan — vì "công bằng" = subjective per threshold.

v5.5: Compliance derived applies ở đây:
  "Công bằng" = chunk_overlap(person.fairness_chunks, group.fairness_chunks)
  → Cùng 1 phân chia, người A thấy "fair" (overlap cao với norm), người B thấy "unfair" (overlap thấp)
  → Conflict không phải vì "ai tham" → vì fairness chunks KHÁC NHAU.
```

### 8.2 Tại Sao "Ai Cũng Muốn Nhiều Hơn"

🟡

```
Threshold ADAPT LÊN (Core.md §5.2):
  Được $X lần đầu → PE dương → adapt → lần sau $X = PE ≈ 0 → cần $X+.
  = Hedonic treadmill áp dụng cho KINH TẾ.

"Nợ thưởng" tích lũy:
  Dopamine path person chịu cost NHIỀU NĂM → "nợ thưởng" tích lũy → kỳ vọng lớn.
  Nhưng: thị trường trả theo GIỚI HẠN THỊ TRƯỜNG, không theo nợ cá nhân.
  → Gap giữa kỳ vọng nội tại vs reality → frustration phổ biến nhất ở creator.

Trung gian accumulate:
  Trung gian scale được (1 platform, triệu giao dịch).
  Creator không scale tuyến tính (1 người, output giới hạn).
  → Trung gian % nhỏ × volume lớn = tổng reward >>> creator.
  🟢 Ví dụ: App Store 30%, YouTube 45% ad revenue → creator frustration.

v5.5: ECP (External Chunk Pressure — Core.md §9) APPLY ở đây:
  Majority follow market norm (ECP) → trả "market rate" = external chunks
  Creator depth cao + internal source → kỳ vọng reward > market rate
  → Tension = GAP giữa internal valuation vs external market chunks
```

### 8.3 Khi Nào Phân Phối "Đủ Tốt"

🟡

```
Không có "perfect" — chỉ có "đủ tốt" = PE ≥ 0 cho TẤT CẢ bên:

① Creator: reward ≥ cost đã chịu (ít nhất = survival + moderate PE).
② Trung gian: reward ≥ cost vận hành.
③ User: PE từ sản phẩm ≥ tiền bỏ ra (perceived value > price).

→ Giao dịch ổn định khi: ①+②+③ đồng thời PE ≥ 0.
→ Giao dịch sụp khi: bất kỳ bên nào PE âm dai dẳng.
  Creator PE âm → ngừng tạo → supply giảm.
  User PE âm → ngừng mua → demand giảm.
  Trung gian PE âm → ngừng vận hành → kết nối mất.
```

---

## 9. Reward Bootstrapping: Thưởng Ngoài Khởi Tạo Thưởng Trong

### 9.1 Cơ Chế

🟡

```
BƯỚC 1: External reward giảm cortisol cho task mới.
  Task mới = prediction cost cao (không biết làm, sợ sai).
  External reward (kẹo, tiền, khen) → giảm cortisol → PFC mở → DÁM THỬ.

BƯỚC 2: Thử → kết quả → PE nội tại hình thành.
  Làm bài toán → đúng → PE dương từ Novelty ("À, ra thế!").
  = PE NỘI TẠI, không liên quan external reward nữa.

BƯỚC 3: PE nội tại → chunk hình thành.
  "Toán → đúng → sướng" = chunk prediction mới.
  Chunk này TỰ DUY TRÌ (không cần kẹo nữa).

BƯỚC 4: Chunk tích lũy → internal drive.
  Nhiều chunk "toán → sướng" → drive tự thân → "thích toán" = THẬT.
  External reward đã HOÀN THÀNH vai trò bootstrap → có thể rút dần.

→ External reward = CATALYST.
  Catalyst khởi tạo quá trình. Quá trình tự duy trì SAU KHI catalyst rút.

v5.5: Bootstrapping = DI CHUYỂN trên Mô Hình Vuông:
  Trước bootstrap: domain mới → cạnh dưới/phải (Drifter/Soldier — nông, external)
  Bootstrap thành công → chunks build → di chuyển LÊN TRÊN (depth tăng)
  Bootstrap + source shift → di chuyển LÊN + SANG TRÁI (internal + deep)
  → Bootstrapping = ASSISTED MOVEMENT trên Mô Hình Vuông per domain.
```

### 9.2 Điều Kiện Thành Công

🟡

```
① NGƯỠNG PHÙ HỢP (Goldilocks):
  Task quá dễ → PE ≈ 0 → chunk không hình thành.
  Task quá khó → PE âm + cortisol cao → avoidance chunk.
  Task VỪA ĐỦ KHÓ → PE dương optimal → chunk "thú vị" hình thành.
  🟢 Vygotsky (1978): Zone of Proximal Development = vùng Goldilocks cho prediction.

② EXTERNAL REWARD GIẢM DẦN (fading):
  Giữ external reward quá lâu → Overjustification Effect.
  🟢 Deci (1971): trẻ được tiền để chơi → khi hết tiền → NGỪNG chơi.
  → External reward = scaffolding: dựng lên → xây xong → THÁO.

③ CHANNEL MATCH (Core.md §6.3):
  External reward phải CÙNG KÊNH hoặc ít nhất KHÔNG BLOCK kênh gốc.
  Cho kẹo (opioid) để học toán (novelty) → OK nếu kẹo không quá mạnh.
  Cho iPad (novelty flooding) để học toán → BẪY (threshold adapt lên → toán = nhạt).

④ CONTROLLABILITY:
  Người nhận thưởng phải cảm thấy KẾT QUẢ do MÌNH tạo ra.
  "Làm đúng → được thưởng" = controllable → schema "nỗ lực = đền đáp."
  "Thưởng random" = uncontrollable → không hình thành chunk hữu ích.
  🟢 Maier & Seligman (2016): controllability = biến quan trọng nhất.

v5.5 THÊM:

⑤ DA INVERTED-U POSITION:
  Bên trái đỉnh → bootstrap KHÓ (PE signal yếu → external reward cũng ít PE)
  Đỉnh → bootstrap TỐI ƯU (PE signal vừa đủ → external catalyst → internal PE)
  Bên phải đỉnh → bootstrap KHÁC KIỂU: PE burst → chunk hình thành NHƯNG nông
    → Cần SLOWER bootstrap (chống explore quá nhanh) để chunks DEEPEN
```

### 9.3 Khi Bootstrapping Thất Bại

🟡

```
OVERJUSTIFICATION (thưởng quá nhiều/lâu):
  External reward MẠNH HƠN internal PE → não chỉ track external.
  Rút external → PE = 0 → dừng hành vi.
  = "Làm vì tiền" THAY THẾ "làm vì thích" → khi hết tiền → hết làm.
  v5.5: ĐẶC BIỆT NGUY HIỂM cho source internal (Improviser/Architect per domain):
    Internal PE VỐN MẠNH → external override = DESTROY source internal
    → Di chuyển TỪ TRÁI SANG PHẢI trên Mô Hình Vuông (internal → external)
    → Mất internal drive = RẤT KHÓ khôi phục.

THRESHOLD MISMATCH (task sai ngưỡng):
  Quá dễ: PE = 0 dù có thưởng.
  Quá khó: cortisol > reward → avoidance.

PUNISHMENT CONTAMINATION (phạt kèm thưởng):
  Thưởng khi đúng + phạt khi sai → cortisol spike khi sai → avoidance chunk.
  Nếu phạt > thưởng (về PE) → net = avoidance.
  = "Sợ sai" > "thích đúng" → PE nội tại KHÔNG HÌNH THÀNH.

SOCIAL COMPARISON (thưởng tạo so sánh):
  "Em được 1, bạn được 3" → serotonin PE âm → cortisol → override thưởng.
  = External reward TẠO THÊM social cost → net PE có thể ÂM.

v5.5 THÊM:
HABITUATION TRAP (thưởng quá predictable):
  Thưởng cùng loại, cùng lượng, cùng timing → habituate → PE=0
  → Bootstrapping fail vì external reward BẢN THÂN đã habituate
  → Counter: variable reward (timing, type, amount) → PE duy trì
```

---

## 10. Convergence × Cross-Domain Value Creation — v5.5 MỚI

🔴 Section MỚI v5.5 — Convergence (Core.md §8.9) giải thích tại sao một số người/công ty tạo giá trị VƯỢT TRỘI.

```
CONVERGENCE = SHARED CHUNKS ACROSS DOMAIN CLUSTERS (Core.md §8.9)

TRONG KINH TẾ: convergence CAO = cross-domain value creation:

  Creator convergence THẤP (Improviser per domain):
    Giỏi 1 domain → value = market rate domain đó
    Nhiều domain nhưng rời rạc → value = sum of individual domain values
    = LINEAR value creation

  Creator convergence CAO (Cross-domain Architect):
    Shared chunks across domains → CREATE VALUE Ở GIAO ĐIỂM
    Value ở giao điểm > sum of parts (vì KHÔNG AI KHÁC ở giao điểm đó)
    = EXPONENTIAL value creation (scarcity at intersection)

  Ví dụ:
    Programmer + Designer = "full-stack" = premium nhẹ
    Programmer + Designer + Business + Psychology = "product visionary"
      = Premium CỰC CAO vì intersection = hiếm
    → Steve Jobs: tech × design × business × psychology = UNIQUE intersection
    → Value = scarcity at convergence point, KHÔNG phải depth per domain alone
```

```
CONVERGENCE × CAREER VALUE:

  Junior: depth nông, convergence thấp → commoditized → market rate
  Mid: depth sâu 1 domain, convergence thấp → specialist → premium per domain
  Senior specialist: depth CỰC SÂU 1 domain → rare specialist → high premium
  Senior generalist (convergence CAO): depth sâu + shared chunks → UNIQUE → highest premium

  🟡 "T-shaped" người: 1 domain sâu + nhiều domain nông = convergence TRUNG BÌNH
  "π-shaped" người: 2 domain sâu + shared chunks = convergence CAO
  "Comb-shaped" người: nhiều domain sâu + shared chunks = convergence CỰC CAO (rare)

  → Career strategy qua v5.5:
    Phase 1: deepen 1 domain (build depth → move UP trên Mô Hình Vuông)
    Phase 2: explore adjacent domain (risk: breadth dilute depth)
    Phase 3: find shared chunks between domains (convergence BUILD)
    Phase 4: leverage convergence for unique value creation

  ⚠️ Phase 2-3 = DIP in apparent value (chưa giỏi domain mới)
  → Người bên phải DA đỉnh SKIP phase này vì PE giảm → stay Phase 1 forever
  → Người gần đỉnh DA SURVIVE dip vì tonic DA sustain → reach Phase 4
```

```
COMPANY CONVERGENCE:

  Single-domain company: compete on depth (quality, efficiency)
  Cross-domain company: compete on convergence (unique combination)

  Apple: design × tech × retail × ecosystem = convergence CAO → moat = intersection
  Google: data × AI × search × advertising = convergence CAO
  → Moat KHÔNG chỉ = depth per domain → moat = convergence (intersection rarity)

  v5.5 insight: company hiring for convergence = hiring bridge roles (HR-Management.md §5)
  → PM, product managers, directors = convergence roles
  → Value = BRIDGE between domain teams, không phải depth per domain
```

---

## 11. Ứng Dụng (Sketch)

### 11.1 Trường Học

```
HIỆN TẠI (source external optimized):
  Thưởng: điểm số (external, serotonin-based: so sánh thứ bậc).
  Phạt: điểm kém, mắng (cortisol).
  → Bootstrap THẤT BẠI cho nhiều học sinh:
    External reward (điểm) không match kênh gốc.
    Phạt > thưởng → avoidance chunk cho subject.
    "Ghét toán" = avoidance chunk đã hình thành, RẤT KHÓ gỡ.

THIẾT KẾ TỐT HƠN (v5.5):
  ① Task = Goldilocks per student (adaptive difficulty).
  ② Thưởng = PE nội tại TỪ TASK, không từ điểm số.
  ③ External reward = scaffolding, giảm dần.
  ④ KHÔNG phạt sai → feedback: "predict chưa đúng, thử lại."
  ⑤ Social comparison tối thiểu (không xếp hạng công khai).
  v5.5: ⑥ Consider DA position per student: bên phải đỉnh cần slower scaffolding
  v5.5: ⑦ Habituation counter: vary reward type, not just amount
  → Chi tiết: Education.md.
```

### 11.2 Công Ty

```
LƯƠNG = external reward cho lao động:
  Lương đủ → cortisol giảm → PFC mở → bootstrap PE nội tại từ công việc.
  Lương thiếu → cortisol cao → PFC chặn → cortisol-driven → "làm cho xong."

THƯỞNG HIỆU QUẢ (v5.5):
  ① Tiền = baseline (giảm cortisol, KHÔNG tạo drive dài hạn).
  ② PE nội tại từ công việc = drive thật sự (autonomy, mastery, purpose).
     🟢 Deci & Ryan (2000): SDT align với HPD —
       Autonomy = controllability. Mastery = PE deepen. Purpose = prediction xa.
  ③ Thưởng tiền cho task sáng tạo → CÓ THỂ overjustify.
     Thưởng tiền cho task routine → OK (không có internal PE để suppress).

  v5.5 THÊM:
  ④ Thưởng PER VỊ TRÍ VUÔNG per domain (§2) — không 1 size fits all.
  ⑤ Counter habituation: vary bonus type + timing.
  ⑥ Consider DA position: burnout (cortisol) ≠ boredom (DA) → giải pháp KHÁC.
  ⑦ Compliance derived: team-based reward chỉ PE dương khi overlap cao.
  → Chi tiết: HR-Management.md.
```

### 11.3 Giao Dịch — Khi Nào Cả Hai Bên "Sướng"

```
Giao dịch thỏa mãn = CẢ HAI bên PE ≥ 0:
  Bên bán: tiền nhận ≥ cost (vật chất + prediction cost + nợ thưởng tích lũy).
  Bên mua: PE từ sản phẩm ≥ PE từ tiền bỏ ra (opportunity cost).

NEGOTIATION qua lens PE:
  Mỗi bên có threshold RIÊNG → "giá hợp lý" = SUBJECTIVE.
  Thương lượng = tìm điểm mà CẢ HAI threshold được đáp ứng.
  Nếu không tồn tại điểm đó (threshold overlap = 0) → không giao dịch.

v5.5: Negotiation = PREDICTION GAME + COMPLIANCE DYNAMICS:
  chunk_overlap(buyer, seller) CAO → easier negotiation (shared "fair" concept)
  chunk_overlap THẤP → harder negotiation (different "fair" chunks)
  → Cross-cultural trade difficulty = different fairness chunks per culture

Giao dịch lặp lại (B2B, subscription):
  Cần PE dương CẢ HAI bên qua NHIỀU chu kỳ.
  Threshold adapt lên → phải tăng giá trị hoặc giảm cost per chu kỳ.
  v5.5: + habituation counter needed → vary value delivery
  = Tại sao loyalty khó: threshold + habituation = double pressure.
```

---

## 12. Câu Hỏi Mở

| # | Câu hỏi | Ưu tiên | Confidence |
|---|---------|---------|------------|
| 1 | Tiền = "shared chunk prediction xã hội"? Hyperinflation = chunk sụp? | Cao | 🟡 |
| 2 | Crypto = chunk prediction MỚI? Volatility = chunk chưa stabilize? | TB | 🔴 |
| 3 | UBI: cortisol floor (bootstrap) hay threshold trap (overjustification)? | Cao nhất | 🔴 |
| 4 | AI giảm prediction cost → value lao động shift → convergence = new premium? | Cao nhất | 🟡 |
| 5 | Inflation = threshold xã hội adapt lên? | TB | 🔴 |
| 6 | Bất bình đẳng inverted-U? Optimal inequality level? | Cao | 🔴 |
| 7 | DA inverted-U predict consumer behavior accurately? | Cao | 🟡 |
| 8 | Habituation Blindness → design "gratitude economics"? | TB | 🔴 |
| 9 | Convergence premium: measurable? How much vs depth premium? | Cao | 🟡 |
| 10 | Reward bootstrapping: optimal fading schedule per DA position? | Cao | 🟡 |

---

## 13. Kết Nối

| Tham khảo | File | Mối liên hệ |
|-----------|------|-------------|
| Threshold adapt | Core.md §5.2 | Tại sao "ai cũng muốn nhiều hơn" |
| Cầu Nối vs Bẫy | Core.md §6.3 | External reward: bootstrap hay trap |
| Cortisol inverted-U | Core.md §6.4 | 2 path kinh tế |
| Dopamine inverted-U | Core.md §6.6 | Spending/investment behavior (§3) |
| Habituation Blindness | Core.md §6.7 | Invisible value problem (§4) |
| Drive Equation | Core.md §7 | Reward - cost per hành vi |
| Mô Hình Vuông | Core.md §8.2 | Reward design per vị trí (§2) |
| Compliance derived | Core.md §8.3 | Fairness = subjective per overlap |
| Chunk Topology | Core.md §8.9 | Convergence × value creation (§10) |
| ECP | Core.md §9 | Market norm pressure |
| Giáo dục | Applications/Education.md | Bootstrapping trong trường học |
| HR Management | Applications/HR-Management.md | Reward design trong công ty |
| Macro-Civilization | Research/Macro-Civilization.md | Bất bình đẳng PE access |
| Neurochemistry | Core-Deep-Dive/Neurochemistry.md | Cortisol × dopamine interaction |

---

> *Hệ Thống Thưởng — Framework v5.5*
> *3 sections MỚI v5.5: Mô Hình Vuông × Reward Design (per vị trí, per domain, compliance derived),*
> *Dopamine Inverted-U × Spending/Investment (DA position → consumer/investor behavior),*
> *Habituation Blindness × Economics (PE=0 ≠ Value=0, counter-habituation strategies),*
> *Convergence × Cross-Domain Value Creation (intersection scarcity, career strategy, company moat).*
> *Bootstrapping reframed: di chuyển trên Mô Hình Vuông per domain.*
> *6 paths "giàu rồi vẫn đuổi tiền" giữ nguyên (solid v5.0 insight).*
> *Prerequisite: Core.md §5-9, §6.6-6.7, §8.9.*
