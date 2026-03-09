# Hóa Chất Thần Kinh — Chi Tiết Sinh Học

> **Vai trò:** File VERIFY — đọc khi muốn hiểu CƠ SỞ SINH HỌC của framework.
> **Không cần đọc file này để HIỂU framework** — Core.md đã đủ.
> **Đọc khi:** muốn verify "tại sao framework nói vậy?", muốn hiểu cơ chế sâu,
> hoặc muốn biết gen/đo lường/can thiệp sinh học.
>
> **Prerequisite:** Đã đọc Core.md §3-6.
>
> **⚠️ Quy ước v5.5:**
> Compliance = QUAN HỆ (chunk alignment với reference group), không phải thuộc tính cá nhân.
> 4 pattern (Soldier/Architect/Improviser/Drifter) = nhãn mô tả, không phải cơ chế.
> CƠ CHẾ = predictive-chunk configuration (depth × source × sync) — xem Core.md §6.0.
> **Quy ước:** 🟢 Nghiên cứu vững | 🟡 Suy luận có cơ sở | 🔴 Giả thuyết

---

## Mục Lục

1. [Kênh Gốc vs Phụ Gia — Tiêu Chuẩn Phân Biệt](#1-phân-biệt)
2. [Dopamine — Hệ Thống "Muốn" (Novelty Channel)](#2-dopamine)
3. [Opioid — Hệ Thống "Thích"](#3-opioid)
4. [Oxytocin — Hệ Thống "Kết Nối"](#4-oxytocin)
5. [Serotonin — Lọc Vị Thế](#5-serotonin)
6. [Cortisol/GABA — Trục An Toàn](#6-cortisol) *(bao gồm §6.11 Sequential Defense)*
7. [Norepinephrine — Volume](#7-ne)
8. [Vasopressin — Bảo Vệ Gắn Bó](#8-vasopressin)
9. [Prolactin — Phanh + Giả Thuyết Healthy/Pathological](#9-prolactin)
10. [Ma Trận Tương Tác](#10-tương-tác)
11. [Đo Lường + Gen Markers](#11-đo-lường)
12. [Can Thiệp Sinh Học](#12-can-thiệp)

---

## 1. Kênh Gốc vs Phụ Gia — Tiêu Chuẩn Phân Biệt

🟡 Tiêu chuẩn phân biệt rõ ràng (nhắc lại từ Core.md §3):

```
KÊNH GỐC = TẠO RA trạng thái động lực hoặc thỏa mãn MỚI.
  Khi bắn: bạn MUỐN / THÍCH / CẦN KẾT NỐI.
  Không có kênh gốc = không có động lực = amotivation.
  Test: block kênh → MẤT 1 loại PE hoàn toàn.

PHỤ GIA = ĐIỀU CHỈNH cách kênh gốc hoạt động.
  Không tạo "muốn/thích/kết nối" — thay đổi cường độ/hướng/lọc.
  Phụ gia 1 mình không tạo hành vi — cần kênh gốc để có thứ điều chỉnh.
  Test: block phụ gia → kênh gốc VẪN CÒN nhưng biểu hiện KHÁC.
```

**Tại sao 3 kênh, không hơn?**

🟡 Ba kênh = 3 hệ thần kinh RIÊNG BIỆT, block 1 không ảnh hưởng 2 cái kia:

```
Bằng chứng tách biệt (Berridge & Robinson, 1998, 2016):
  MUỐN nhưng không THÍCH = có (nghiện: dopamine cao, opioid tolerance)
  THÍCH nhưng không MUỐN = có (bất ngờ dễ chịu: opioid bắn, dopamine không)
  KẾT NỐI nhưng không MUỐN/THÍCH = có (mẹ chăm con ốm 3h sáng:
    oxytocin kéo, nhưng không "muốn" thức, không "thích" mệt)

→ 3 hệ hoạt động ĐỘC LẬP = 3 kênh gốc riêng biệt.
→ CÓ THỂ có kênh thứ 4 chưa phát hiện? Có thể. Framework mở cho bổ sung.
```

---

## 2. Dopamine — Hệ Thống "Muốn" (Novelty Channel)

### 2.1 Cơ Chế Cốt Lõi

```
🟢 Hệ dopamine mesolimbic — bảo tồn từ côn trùng đến người.

Dopamine = TÍN HIỆU PREDICTION ERROR (PE), KHÔNG PHẢI "hormone hạnh phúc."
  Thưởng > kỳ vọng → dopamine BẮN (positive PE) → MUỐN thêm → approach
  Thưởng = kỳ vọng → dopamine ỔN ĐỊNH → quen → giảm dần (habituation)
  Thưởng < kỳ vọng → dopamine SỤT (negative PE) → thất vọng → rút lui

🟢 Schultz et al. (1997): ghi trực tiếp neuron dopamine ở khỉ, confirm PE mechanism.
🟢 Kang et al. (2009): curiosity kích hoạt caudate nucleus (dopamine-rich area).

QUAN TRỌNG: Dopamine bắn cho DỰ ĐOÁN thưởng, KHÔNG PHẢI thưởng thực tế.
  Người đầu bếp nhìn nguyên liệu → dopamine (dự đoán món ngon)
  Ăn xong → opioid (thích), KHÔNG PHẢI dopamine.
  → "Muốn" (dopamine) ≠ "Thích" (opioid). Phân biệt cốt lõi.
```

### 2.2 Tonic vs Phasic — Hai Chế Độ

```
🟢 Cohen, McClure & Yu (2007):

TONIC dopamine (baseline ổn định):
  → Exploitation / Deepen mode
  → PE từ tinh chỉnh prediction ĐÃ CÓ
  → Ổn định, bền, PE nhỏ nhưng liên tục
  → Trong framework: DEEPEN axis (Core.md §6.2)

PHASIC dopamine (burst đột ngột):
  → Exploration / Explore mode
  → PE từ prediction HOÀN TOÀN MỚI
  → Lớn, mãnh liệt, nhưng habituate nhanh
  → Trong framework: EXPLORE axis

Tỷ lệ tonic/phasic khác per người:
  DRD4 7-repeat → phasic dominant → explore nhiều → PE Sensitivity cao
  DRD4 4-repeat → tonic dominant → deepen nhiều → PE Sensitivity thấp hơn
  🟢 Ebstein et al. (1996): DRD4 7-repeat ↔ novelty-seeking.
```

### 2.3 Tại Sao Gọi "Novelty Channel" Thay Vì "Dopamine Channel"

```
🟡 Dopamine CŨNG tham gia opioid pathway và oxytocin pathway.
  Nhưng NOVELTY-specific PE = dopamine AS KÊNH GỐC (source PE chính).

Người Novelty channel mạnh:
  PE chính từ: hiểu thứ mới, phát hiện pattern, giải puzzle, xây hệ thống
  Biểu hiện: tò mò, khám phá, "ồ hóa ra thế!", "sao nó hoạt động?"
  Gen tendency: DRD4 7-repeat, COMT Val/Val (fast metabolism → need more stim)
  Threshold interaction: Novelty + threshold cao → "câu đố dễ không thú vị"
    = PE nhỏ < threshold → không register
```

### 2.4 Dopamine × Threshold: D2 Receptor Density

```
🟢 Volkow et al. (2002):
  D2 receptor density CAO → nhạy dopamine → threshold THẤP → PE nhỏ đủ
  D2 receptor density THẤP → ít nhạy → threshold CAO → cần PE lớn

Đây là CƠ SỞ SINH HỌC của Threshold (Core.md §5.2):
  D2 cao = "dễ hài lòng" = threshold thấp
  D2 thấp = "khó hài lòng" = threshold cao

Calibrate (chậm):
  MXH, drug, dopamine flooding liên tục → D2 DOWN-REGULATE → threshold TĂNG
  Thiền, nature, dopamine fasting → D2 UP-REGULATE (chậm) → threshold GIẢM
  🟢 Volkow et al. (2001): substance use → D2 giảm → reward sensitivity giảm.
```

### 2.5 Dopamine Inverted-U — 3 Tầng

🟡 Cortisol có inverted-U (§6). Dopamine CÓ inverted-U riêng — quyết định **depth vs breadth**.
Tổng quan: Core.md §6.6. Dưới đây là cơ chế chi tiết 3 tầng.

```
TẦNG 1 — OVERJUSTIFICATION (external reward ghi đè internal PE):

🟢 Deci (1971), Lepper, Greene & Nisbett (1973):
  Trẻ vẽ vì thích (internal PE: novelty + opioid) → cho thưởng sticker
  → Dopamine shift: PE source chuyển từ PROCESS (tonic) sang REWARD (phasic)
  → Ngừng thưởng → phasic PE mất → tonic PE đã bị ghi đè → NGỪNG VẼ LUÔN

Cơ chế chính xác:
  External reward = phasic DA burst MẠNH hơn tonic DA từ process
  → Prediction update: "vẽ = để được sticker" (thay vì "vẽ = hay")
  → Khi sticker mất → prediction fail → negative PE → avoidance
  → Internal PE (tonic) ĐÃ BỊ OVERWRITE, không tự phục hồi ngay

Trong framework:
  = Reward dosage quá cao → prediction ngắn KHÓA prediction xa (Core.md §6.3)
  = Source shift: INTERNAL → EXTERNAL, không tự shift ngược dễ
  ⚠️ Hệ thống giáo dục phần lớn = overjustification machine
    (điểm, xếp hạng, phạt = external reward/punishment liên tục)
```

```
TẦNG 2 — ADDICTION (D2 down-regulation vòng xoáy):

🟢 Volkow et al. (2001, 2002): substance use → D2 receptor DOWN-REGULATE
  → Cần liều CAO hơn → D2 giảm thêm → vòng xoáy

Cơ chế chính xác:
  Dopamine flooding liên tục (substance, gambling, MXH extreme)
  → Post-synaptic neuron tự bảo vệ: GIẢM D2 receptor
  → Cùng lượng dopamine → PE signal YẾU hơn → threshold TĂNG
  → Cần stimulus MẠNH hơn → dopamine flood thêm → D2 giảm thêm
  → Anhedonia: PE từ nguồn BÌNH THƯỜNG gần zero (ăn ngon, gặp bạn, thiên nhiên)

Trong framework:
  = Threshold bị NHÂN TẠO đẩy lên → PE deficit mãn tính
  = Cực phải inverted-U: dopamine quá cao → hệ thống TỰ PHÁ
  = Drifter INDUCED: không phải hardware Drifter, mà D2 bị phá → chunks không form
```

```
TẦNG 3 — IMPROVISER TRAP (phasic > tonic, chưa pathological):

⚠️ TẦNG TINH VI NHẤT — không gây hại rõ, khó detect.

Cơ chế:
  Dopamine hơi cao (DRD4 novelty tendency + môi trường giàu stimulus)
  → Phasic DA (explore) LUÔN nhỉnh hơn tonic DA (deepen) ở mỗi decision point:

    Decision point: "tiếp tục deepen domain hiện tại" vs "thử domain mới"
      Deepen: tonic DA = PE nhỏ, chậm, steady (tinh chỉnh prediction đã có)
      Explore: phasic DA = PE burst, instant, mãnh liệt (prediction hoàn toàn mới)
      → Khi phasic baseline hơi cao: explore THẮNG mỗi lần
      → Tích lũy: LUÔN explore, KHÔNG BAO GIỜ deepen đủ sâu

  Kết quả observable:
    Biết nhiều domain, giỏi chút mỗi cái, "đa tài"
    Nhưng chunks KHÔNG KỊP SYNC (PE Sensitivity cao → nhảy trước khi sync)
    → Improviser STABLE — không phải "chọn" Improviser, mà bị KHÓA ở Improviser

  Tại sao khó detect:
    Không pathological (D2 vẫn bình thường, không addiction)
    Trông TÍCH CỰC (năng động, sáng tạo, linh hoạt)
    Chỉ thấy qua THỜI GIAN: "10 năm qua biết 20 thứ, giỏi 0 thứ"
    → Khác Improviser TỰ NHIÊN (chọn breadth vì phù hợp hardware)
       với Improviser BỊ KHÓA (muốn depth nhưng phasic luôn thắng)

  Differentiator:
    Improviser tự nhiên: KHÔNG CẢM THẤY thiếu depth — breadth = PE source chính
    Improviser bị khóa: CẢM THẤY "sao mình không bao giờ đào sâu được" — biết cần depth
      nhưng mỗi lần ngồi xuống deepen → novelty mới xuất hiện → switch
      = awareness có, execution bị dopamine override

🟢 Liên hệ: Cohen, McClure & Yu (2007) — tonic/phasic ratio = exploit/explore.
  Tầng 3 = tonic/phasic ratio bị LỆCH vĩnh viễn về phasic, chưa đến mức pathological.
```

```
TÓM TẮT — DOPAMINE INVERTED-U 3 TẦNG:

              ┌─────────────────────────────────────────┐
              │          DOPAMINE INVERTED-U             │
              │                                         │
  Depth/      │            ╱╲                            │
  Output      │           ╱  ╲  ← TỐI ƯU               │
  Quality     │          ╱    ╲   (tonic/phasic          │
              │         ╱      ╲   cân bằng)             │
              │        ╱        ╲                        │
              │       ╱    T3    ╲                       │
              │      ╱  Improviser╲                      │
              │     ╱    trap      ╲  T2                 │
              │ T1 ╱                ╲ Addiction           │
              │   ╱                  ╲                   │
              └─────────────────────────────────────────┘
                Thấp ──────────────────────────── Cao
                        Dopamine Level

  T1 (trái): Overjustification — external reward ghi đè internal PE
  T2 (phải): Addiction — D2 down-regulate → vòng xoáy
  T3 (giữa-phải): Improviser trap — phasic nhỉnh tonic → breadth khóa depth
     ⚠️ T3 nằm GIỮA optimal và pathological — vùng "trông ổn nhưng bị khóa"

SONG SONG VỚI CORTISOL INVERTED-U:
  Cortisol inverted-U → approach vs avoidance (HƯỚNG hành vi)
  Dopamine inverted-U → depth vs breadth (ĐỘ SÂU hành vi)
  Hai inverted-U INDEPENDENT, cùng shape chunk config per domain.
  → Đọc Core.md §6.6 cho tổng quan.
```

---

## 3. Opioid — Hệ Thống "Thích"

### 3.1 Cơ Chế Cốt Lõi

```
🟢 Hệ opioid nội sinh (μ-opioid receptors).
🟢 Berridge & Robinson (1998, 2016): "wanting" (dopamine) vs "liking" (opioid) = 2 hệ RIÊNG.

Opioid = TÍN HIỆU "THÍCH" — đánh giá trải nghiệm ĐANG XẢY RA.
  Dopamine: "tôi DỰ ĐOÁN sẽ hay" (TRƯỚC trải nghiệm)
  Opioid: "đang hay THẬT" (TRONG trải nghiệm)

Bằng chứng tách biệt:
  Block dopamine: chuột KHÔNG TÌM đường nhưng vẫn biểu cảm "thích" khi được cho.
  Block opioid: chuột VẪN TÌM đường nhưng NHĂN MẶT khi nếm.
  → Muốn ≠ Thích. Hoạt động ĐỘC LẬP.

Opioid bắn SAU ĐAU: endorphin release after effort/pain.
  Runner's high = endorphin + endocannabinoid sau vận động mạnh.
  "No pain no gain" = opioid REWARD cần pain TRIGGER trước.
  → Không phải "thích đau" — thích OPIOID RELEASE sau đau.
```

### 3.2 Opioid Trong Framework

```
🟡 Người Opioid channel mạnh:
  PE chính từ: trải nghiệm giác quan, mỹ cảm, craft, sensory richness
  Biểu hiện: thưởng thức, tạo tác, "đẹp quá!", chất lượng > số lượng
  Gen: OPRM1 variants → sensitivity khác nhau

  Nghệ sĩ thị giác: opioid từ MÀU SẮC, texture
  Đầu bếp: opioid từ MÙI VỊ, presentation
  Nhạc sĩ: opioid từ ÂM THANH, harmony
  → Cùng Opioid channel, khác DOMAIN giác quan

Opioid vs Novelty — khác biệt cốt lõi:
  Novelty: PE từ HIỂU (cognitive) — "ồ hóa ra thế!"
  Opioid: PE từ CẢM NHẬN (sensory) — "đẹp quá, hay quá!"
  MIX: Jobs = Novelty + Opioid (phát minh ĐẸP)
```

### 3.3 Nghiện: Opioid Pathway Bị Hijack

```
🟢 Nghiện = "muốn" cực mạnh (dopamine) + "thích" đã giảm (opioid tolerance).

  Lần đầu: dopamine (muốn) + opioid (thích) = PEAK
  Lần 10: dopamine VẪN CAO + opioid GIẢM (tolerance) = muốn nhưng ít thích
  Lần 100: dopamine CỰC CAO (wanting sensitization) + opioid THẤP = MUỐN CỰC nhưng KHÔNG THÍCH

→ Nghiện khổ sở vì: MUỐN mà không THỎA MÃN.
→ Framework: threshold BỊ NÂNG (D2 giảm) + PE source THU HẸP (chỉ còn 1)
  → Mọi PE source khác < threshold → chỉ substance mới đủ → bẫy.
```

---

## 4. Oxytocin — Hệ Thống "Kết Nối"

### 4.1 Cơ Chế Cốt Lõi

```
🟢 Young & Wang (2004): oxytocin + pair bonding ở prairie voles.
🟢 Warneken & Tomasello (2006): trẻ 14-18 tháng TỰ PHÁT giúp đỡ — trước ngôn ngữ.

Oxytocin = TÍN HIỆU "KẾT NỐI" — bắn khi gắn bó xảy ra hoặc được kỳ vọng.

Vòng lặp dương:
  Kết nối (ôm, nhìn mắt, giúp, tin tưởng)
  → Oxytocin bắn → Ấm áp, an toàn
  → Muốn kết nối thêm → Hành động kết nối
  → Oxytocin bắn thêm → Loop

→ "Mẹ yêu con ngay từ đầu": da kề da → oxytocin flood → bond NGAY.
→ "Quen lâu → gắn hơn": mỗi interaction → oxytocin tích lũy → bond sâu.
```

### 4.2 Mặt Tối: In-Group / Out-Group

```
🟢 De Dreu et al. (2010): Oxytocin TĂNG gắn bó TRONG nhóm, CÓ THỂ tăng thù địch NGOÀI nhóm.

Oxytocin KHÔNG phải "hormone yêu thương universal":
  TRONG nhóm: tin tưởng, hợp tác, hy sinh
  NGOÀI nhóm: ngờ vực, cạnh tranh, phân biệt

→ Framework: Oxytocin channel = nền tảng sinh học cho BỘ LẠC.
  Tôn giáo, team, fandom, quốc gia = dựa trên oxytocin in-group.
→ "Phân biệt phe phái" có CƠ SỞ SINH HỌC. Hiểu cơ chế → can thiệp tốt hơn.
```

### 4.3 Trauma Bonding + Attachment Styles

```
🟢 Trauma bonding: stress + gắn bó = oxytocin + cortisol CÙNG LÚC.
  Người gây đau + người an ủi = CÙNG 1 NGƯỜI → bond CỰC MẠNH + CỰC ĐỘC.
  → Không phải "yêu sai người" — là oxytocin bị hijack bởi cortisol cycle.

🟢 Attachment style (Bowlby, 1969): kinh nghiệm gắn bó sớm CALIBRATE hệ oxytocin suốt đời.
  Secure attachment → oxytocin system healthy → trust dễ
  Avoidant attachment → oxytocin system SUPPRESS → "không cần ai"
  Anxious attachment → oxytocin system HYPERACTIVE → "cần quá mức"
  → Không phải "tính cách" — là CALIBRATION hệ oxytocin từ bối cảnh sớm (Tầng -1).
```

---

## 5. Serotonin — Lọc Vị Thế

### 5.1 Cơ Chế

```
🟢 Raleigh et al. (1991): khỉ vervet — con đầu đàn serotonin CAO NHẤT.
  Mất vị trí → serotonin SỤT. Cho serotonin → TỰ TIN HƠN (không có vị trí thật).
  → Serotonin ĐO cảm nhận vị trí trong hierarchy, BẤT KỂ vị trí thật.

🟢 5-HTTLPR gen: biến thể ngắn → NHẠY hơn với tín hiệu xã hội.
```

### 5.2 Serotonin = Bộ Lọc Đặt Lên MỌI Kênh Gốc

```
Sensitivity CAO: mọi hành vi bị lọc qua "người khác nghĩ gì?"
  Novelty + serotonin nhạy = tò mò nhưng chỉ thứ "ấn tượng"
  Opioid + serotonin nhạy = thưởng thức nhưng chọn thứ "flex được"
  Oxytocin + serotonin nhạy = giúp đỡ nhưng cần "người khác biết"

Sensitivity THẤP: bộ lọc BIẾN MẤT → hành vi thuần kênh gốc.
  "Không quan tâm người khác nghĩ gì" = serotonin sensitivity thấp.
```

### 5.3 Serotonin × Compliance + Serotonin ≠ "Hạnh Phúc"

```
🟡 Serotonin sensitivity = thiên hướng EXTERNAL compliance:
  Nhạy hierarchy → nhạy authority → thiên tuân thủ → external compliance.
  Ít nhạy → ít quan tâm authority → thiên tự quyết → internal compliance.
  → Là THIÊN HƯỚNG, không quyết định. Kinh nghiệm + domain override được.

Serotonin ≠ "hormone hạnh phúc." Đúng hơn: "MÌNH ỔN TRONG HIERARCHY."
  Serotonin cao → không cần so sánh → PE từ kênh gốc KHÔNG BỊ LỌC → "hạnh phúc" gián tiếp.
  Serotonin thấp → so sánh liên tục → PE bị lọc/giảm → "bất hạnh" gián tiếp.
→ Serotonin không TẠO hạnh phúc — nó BỎ RÀO CẢN cho hạnh phúc từ kênh gốc.

🟢 SSRIs (tăng serotonin): giảm lo âu xã hội → confirm serotonin ↔ vị thế.
```

### 5.4 Cơ Chế Lọc Chính Xác — Tại Tầng Appraisal

```
🔴 Giả thuyết cơ chế (compatible với Scherer 2001, Appraisal Theory):

Serotonin filter KHÔNG block PE trực tiếp.
Thay vào đó: filter hoạt động tại bước APPRAISAL vô thức (~200ms trước wanting kích hoạt).

Chuỗi đầy đủ khi serotonin nhạy:
  PE bắn (dự đoán sai/mới) → Appraisal vô thức →
    Câu hỏi "Relevance to social position?" ĐƯỢC HỎI to:
    "Cái này có liên quan đến vị trí/ấn tượng xã hội của mình không?"
    → Nếu KHÔNG → PE bị giảm weight → wanting không bật mạnh
    → Nếu CÓ → PE đi qua → wanting bật

Khi serotonin CAO (cảm thấy ổn trong hierarchy):
  Câu hỏi "social relevance?" IM LẶNG → PE từ kênh gốc không bị chặn → wanting bật thẳng.
  → Đây là cơ chế CHÍNH XÁC cho "serotonin bỏ rào cản cho hạnh phúc từ kênh gốc" (§5.3).

Khi serotonin THẤP (cảm thấy bất an trong hierarchy):
  Câu hỏi "social relevance?" ồn ào liên tục → PE bị evaluate qua social lens TRƯỚC → wanting bị gián đoạn.
  → Người cảm thấy "chỉ thích thứ flex được / chỉ muốn giúp khi người khác biết" = §5.2 mô tả.

⚠️ Phân biệt quan trọng:
  PE VẪN BẮN dù serotonin thấp → não NHẬN THẤY stimulus.
  Nhưng appraisal gate block wanting activation → "biết là thú vị, nhưng không thấy muốn."
  Này là cơ chế sâu hơn §5.2 (filter cường độ) — là filter ở bước QUYẾT ĐỊNH có wanting hay không.

⚠️ Chưa có nghiên cứu trực tiếp link serotonin ↔ Scherer appraisal dimensions.
   Compatible với: serotonin ↔ social cognition (§5.1), SSRIs giảm lo âu xã hội = giảm
   "social relevance check" liên tục, và lý thuyết appraisal (Scherer 2001).
```

---

## 6. Cortisol/GABA — Trục An Toàn ↔ Hành Động

### 6.1 Hai Receptor: MR vs GR — Chìa Khóa Inverted-U

```
🟢 Cortisol tác động qua 2 RECEPTOR KHÁC NHAU trong não (de Kloet et al., 1998, 2005):

MR (Mineralocorticoid Receptor) — ÁI LỰC CAO (Kd ~0.5 nM):
  ~80-90% bão hòa ở mức cortisol BÌNH THƯỜNG (baseline)
  Vùng: hippocampus, PFC (layer II/III, V), lateral septum
  Chức năng: duy trì trạng thái "proactive/approach" — SẴN SÀNG hành động
    → Tăng glutamate trong PFC → working memory TỐT (non-genomic, nhanh)
    → Đánh giá rủi ro, linh hoạt hành vi, thăm dò môi trường
  → MR = "chế độ sẵn sàng" — CẦN cortisol baseline để NÃO HOẠT ĐỘNG BÌNH THƯỜNG.
  🟢 Karst et al. (2005): membrane MR tăng xác suất phóng glutamate presynaptic.

GR (Glucocorticoid Receptor) — ÁI LỰC THẤP (Kd ~5-10 nM, thấp hơn MR ~10x):
  Chỉ ~10-20% bão hòa ở baseline. TĂNG MẠNH khi cortisol TĂNG (stress, circadian peak).
  Vùng: KHẮP NÃO — hippocampus, PFC, amygdala, VTA, NAc, hypothalamus
  Chức năng THAY ĐỔI THEO MỨC BÃO HÒA:
    ~50-70% bão hòa (moderate): TĂNG CƯỜNG — tập trung, ghi nhớ, consolidation
    ~100% bão hòa (high): ỨC CHẾ — PFC suy giảm, amygdala chiếm ưu thế
    Mãn tính 100%: DOWNREGULATE — GR tự giảm nhạy (qua FKBP5) → vòng xoáy âm
  🟢 FKBP5: GR kích hoạt → FKBP5 tăng → FKBP5 ức chế GR → feedback âm ở cấp tế bào.
    FKBP5 rs1360780 T allele: phản ứng cortisol MẠNH hơn, recovery CHẬM hơn
    → Yếu tố gen MẠNH NHẤT cho rối loạn stress (Binder et al., 2004, 2008).
```

### 6.2 Đường Cong Chữ U Ngược (Inverted-U)

```
🟢 Hiệu suất / Động lực KHÔNG tỉ lệ thuận hay nghịch với cortisol.
  Mà theo ĐƯỜNG CONG CHỮ U NGƯỢC (Yerkes-Dodson + MR:GR balance):

   Hiệu suất
        ↑
        |        ★ TỐI ƯU
        |       / \
        |      /   \
        |     /     \
        |    /       \
        |   /         \
        +------------------→ Cortisol
      Thấp    Vừa     Cao

  MỨC THẤP (MR ~80%, GR ~10%):
    PFC ổn định nhưng không enhanced. DA baseline.
    Hành vi: bình thường, không đặc biệt năng động.
    Ví dụ: ngày nghỉ, không deadline, không áp lực.

  MỨC VỪA (MR ~100%, GR ~50-70%) — ★ VÙNG TỐI ƯU:
    PFC TĂNG CƯỜNG (non-genomic MR: glutamate↑, working memory↑).
    DA TĂNG (GR trong VTA kích thích DA neurons — xem §6.4).
    NE + cortisol synergy: focused attention.
    → DRIVE CAO + PFC ONLINE → hiệu quả nhất.
    Ví dụ: deadline khả thi, thử thách vừa sức, thi đấu.

  MỨC CAO (MR ~100%, GR ~100% → downregulate):
    PFC ỨC CHẾ: REDD1↑ → mTORC1↓ → spine loss, dendritic retraction.
    DA GIẢM: TH↓, D1/D2↓, phasic DA bằng phẳng.
    Amygdala PHÌNH: dendritic expansion → hyperreactive.
    → DRIVE SỤP + PFC OFFLINE → amygdala chiếm ưu thế.
    Ví dụ: stress mãn tính, nợ nần, sếp toxic, bệnh nặng.

🟢 Lupien et al. (2007): 10mg hydrocortisone cải thiện working memory; 40mg làm suy giảm.
🟢 Shields et al. (2016, meta-analysis, 95 studies): confirm inverted-U — moderate enhance, high impair.

→ QUAN TRỌNG: cortisol KHÔNG PHẢI "xấu."
  Cortisol = CÔNG CỤ hai lưỡi. Mức vừa = TĂNG CƯỜNG. Mức cao = PHÁ HỦY.
  Mục tiêu: TỐI ƯU cortisol (giữ ở vùng giữa), KHÔNG PHẢI loại bỏ cortisol.
```

### 6.3 Ba Biến Quyết Định: Dose × Duration × Controllability

```
🟡 Vị trí trên inverted-U = f(liều, thời gian, khả năng kiểm soát):

LIỀU LƯỢNG (DOSE):
  Moderate → ascending limb → DRIVE.
  High → descending limb → PARALYSIS.
  → Nhưng "moderate" vs "high" KHÁC NHAU mỗi người (xem §6.7).

THỜI GIAN (DURATION):
  Cấp tính (phút→giờ): cortisol TĂNG dopamine trực tiếp (§6.4).
    GR trong VTA → tyrosine hydroxylase↑ → DA synthesis↑.
    CRH (trước cortisol) → CRH-R1 trong VTA → DA neurons excited.
    → "Wanting" tăng, incentive salience tăng.
    → Xong stressor → cortisol hạ → PFC phục hồi.
  Mãn tính (ngày→tháng): cortisol GIẢM dopamine (§6.5).
    TH↓, D1/D2↓, CRH-R1→CRH-R2 switch (excite→inhibit).
    Phasic DA bằng phẳng → anhedonia.
    🟢 Epigenetic: DNMT3a↑ → methylation TH promoter → DA BỊ TẮT bền vững.
    → KHÔNG THỂ "muốn" dù biết nên muốn. Không phải lười — là sinh hóa.

KHẢ NĂNG KIỂM SOÁT (CONTROLLABILITY) — BIẾN QUAN TRỌNG NHẤT:
  🟢 Maier & Seligman (2016): "Bất lực" = phản ứng MẶC ĐỊNH của não.
    Não phải HỌC rằng tình huống kiểm soát được.
    vmPFC học "kiểm soát được" → ức chế phản ứng bất lực (qua DRN).
    Stress kiểm soát được → cortisol moderate → ascending limb.
    Stress KHÔNG kiểm soát → cortisol MAX → descending limb → bất lực.

  CƠ CHẾ: cortisol mãn tính → vmPFC teo (dendritic retraction)
    → MẤT khả năng nhận biết "kiểm soát được"
    → Bất lực TỔNG QUÁT HÓA sang cả tình huống kiểm soát được
    → "Learned helplessness" = vmPFC KHÔNG CÒN hoạt động đúng.

  FRAMEWORK: "Action Clarity" ≈ controllability + available action path.
    Biết phải làm gì + tin mình CÓ THỂ làm → cortisol giữ moderate → DRIVE.
    Không biết làm gì + tin mình BẤT LỰC → cortisol leo → PARALYSIS.
    → Đây là tại sao CUNG CẤP ACTION PATH = can thiệp cortisol hiệu quả.
```

### 6.4 Cortisol × Dopamine: Tại Sao Acute Cortisol TẠO Động Lực

```
🟢 Cortisol cấp tính TĂNG CƯỜNG hệ dopamine (Piazza & Le Moal, 1996, 1997):

CƠ CHẾ TRỰC TIẾP:
  1. GR trong VTA → tăng TH (tyrosine hydroxylase) → DA synthesis↑
  2. GR → modulat ion channels → tăng burst firing VTA DA neurons
  3. CRH (trước cortisol) → CRH-R1 trên VTA DA neurons → kích thích trực tiếp
     🟢 Wanat et al. (2008): CRH excites VTA DA neurons via CRH-R1
  4. Cortisol → tăng DA release trong NAc (microdialysis confirm)
     Bị chặn bởi GR antagonist (RU486) → confirm GR-mediated.

KẾT QUẢ:
  Cortisol moderate → DA↑ trong NAc → "wanting" TĂNG (Berridge's incentive salience)
  + PFC online (moderate GR) → goal-directed behavior TĂNG
  + NE đồng thời từ LC → attention narrowing (Easterbrook, 1959)
  → = TRẠNG THÁI "DEADLINE PRODUCTIVE" — tập trung, năng động, hiệu quả.

→ QUAN TRỌNG cho framework: cortisol-driven và dopamine-driven KHÔNG ĐỐI LẬP hoàn toàn.
  Cortisol moderate = TĂNG dopamine. Chúng CỘNG TÁC ở mức vừa.
  Chỉ khi cortisol CAO thì chúng mới đối lập (cortisol ức chế DA).
  → Core.md §6.4 "cortisol-driven vs dopamine-driven" cần hiểu là PHỔ, không binary.
```

### 6.5 Cortisol Mãn Tính: Tại Sao Stress Dài Giết Động Lực

```
🟢 Cortisol mãn tính = NGƯỢC HOÀN TOÀN với cấp tính:

NÃO BỊ THAY ĐỔI CẤU TRÚC:
  PFC: dendritic retraction ở layer II/III (Radley et al., 2004, 2006).
    → Working memory↓, cognitive flexibility↓, top-down control↓.
    REDD1↑ → mTORC1↓ → giảm protein synthesis → spine loss.
    BDNF↓ (epigenetic: HDAC↑ tại BDNF promoter IV).
  Hippocampus: atrophy CA3, neurogenesis↓ ở dentate gyrus.
    🟢 Sapolsky (2004): cortisol mãn tính → atrophy hippocampus. Đo được trên MRI.
    → Hippocampus = phanh HPA axis. Hippocampus teo → CÒN ÍT PHANH HƠN → vòng xoáy.
  Amygdala: dendritic EXPANSION ở BLA (Vyas et al., 2002). Ngược với PFC!
    → BDNF TĂNG ở amygdala (khác PFC — coregulator khác nhau).
    → Hyperreactive: threshold kích hoạt GIẢM → mọi thứ đều "đe dọa."

DA BỊ ỨC CHẾ:
  TH↓ → ít DA synthesis. D1/D2 receptor↓ ở NAc và PFC.
  CRH-R1→CRH-R2 switch ở VTA: acute excite → chronic INHIBIT DA neurons.
  Phasic DA bằng phẳng (tonic DA có thể duy trì) → anhedonia.
  🟢 Epigenetic: DNMT3a↑ ở NAc → methylation promoter genes liên quan reward
    (LaPlant et al., 2010). Thay đổi BỀN VỮNG — không tự hồi.

HÀNH VI:
  Goal-directed → habitual/compulsive (Schwabe & Wolf, 2009):
    mPFC (goal-directed) yếu + dorsolateral striatum (habitual) mạnh lên
    → Hành vi "tự động" không nhạy với hậu quả. Giống nghiện cấu trúc.
  vmPFC→DRN yếu → serotonin DRN hyperactive → behavioral inhibition.
  → "Thiếu ý chí" = PFC bị cortisol mãn tính PHÁ, KHÔNG PHẢI tính cách.
  → Depression, anxiety, burnout = biểu hiện cortisol mãn tính.
  → Architect + cortisol mãn tính → biểu hiện như Soldier pattern (amotivation).

→ Cortisol mãn tính = "NÚT RESET VỀ SOLDIER PATTERN" (Core.md §4):
  Stress đủ mạnh, đủ lâu → BẤT KỲ AI cũng temporary chunk config external.
  Đây là TẠI SAO hạ cortisol = BƯỚC 1 mọi can thiệp (Core.md §11.3).
  Nhưng mục tiêu KHÔNG PHẢI "cortisol = 0" → mục tiêu = VÙNG TỐI ƯU trên inverted-U.
```

### 6.6 Tại Sao Cortisol Drive Tồn Tại — Thiết Kế Tiến Hóa + Mismatch

```
🟢 Dopamine = PE signal → CẦN prediction error để fire (Schultz 1997).
  Điều này tạo 5 LỖ HỔNG mà cortisol BUỘC PHẢI lấp:

1. HABITUATION GAP:
   PE = kết quả − dự đoán. Kết quả đã biết → PE = 0 → dopamine im lặng.
   Ăn cơm lần 1000: không PE. Nhưng vẫn CẦN ĂN.
   Cortisol (đói = homeostasis deficit) drive ĂN dù không có PE.
   → Mọi nhu cầu sinh tồn LẶP LẠI (ăn, ngủ, uống, giữ ấm) cần cortisol drive.

2. SPEED GAP:
   Dopamine-driven → qua PFC → 500ms+. Hổ xuất hiện cần phản ứng <200ms.
   Cortisol/adrenaline → amygdala trực tiếp → bypass PFC → nhanh, thô, nhưng SỐNG.
   🟢 LeDoux (1996): amygdala "low road" = thalamus→amygdala, bỏ qua cortex.

3. BOOTSTRAP GAP:
   Dopamine PE cần MODEL (dự đoán) trước để so sánh. Sơ sinh KHÔNG CÓ model.
   Cortisol drive (đói→khóc, lạnh→khóc) giữ sơ sinh sống ĐỦ LÂU
   để dopamine system xây model đầu tiên.
   → Cortisol = drive MẶC ĐỊNH trước khi prediction system online.

4. UNKNOWN-UNKNOWN GAP:
   Dopamine chỉ fire khi có prediction để so sánh. Threat hoàn toàn mới
   (chưa có model) → dopamine IM LẶNG → không phản ứng.
   Amygdala + cortisol fire ở UNCERTAINTY bản thân nó → phản ứng cái chưa biết.
   🟢 LeDoux (1996): amygdala phản ứng với novelty TRƯỚC khi cortex đánh giá.

5. COLLECTIVE GAP: 🟡
   Dopamine drive = cá nhân (chase PE riêng). Nhóm cần người làm việc
   PE thấp (gác đêm, dọn dẹp) → dopamine không drive ai làm.
   Cortisol (social pressure, sợ bị trục xuất khỏi nhóm) → collective action.
   → Đây là Soldier Gravity (Core.md §9) ở cấp TIẾN HÓA.

→ Dopamine thuần = "sướng hơn" nhưng CHẾT SỚM HƠN.
  Tiến hóa tối ưu cho SỐNG SÓT + SINH SẢN, không cho thoải mái.
```

```
🟡 Cortisol được thiết kế cho CHU KỲ SAVANNA (200.000 năm chọn lọc):

THIẾT KẾ GỐC:
  Threat CỤ THỂ (hổ, rắn, kẻ thù) → cortisol spike (phút)
  → Action path RÕ (chạy hoặc đánh)
  → Resolution RÕ (sống/chết — trong phút)
  → Recovery (nghỉ, gắn bó nhóm → oxytocin → cortisol hạ)
  → ★ Chu kỳ: SPIKE → ACTION → RESOLUTION → RECOVERY → BASELINE

4 CƠ CHẾ AN TOÀN BỊ PHÁ BỞI MÔI TRƯỜNG HIỆN ĐẠI:

1. ACUTE → CHRONIC: threat savanna = phút. Nợ/job insecurity = tháng→năm.
   Cortisol thiết kế cho PHÚT, bị chạy THÁNG → GR bão hòa liên tục → §6.5.
   🟢 Allostatic load (McEwen, 1998): tích lũy stress = hao mòn hệ thống.

2. ACTION PATH BỊ XÓA: "hổ → chạy" (rõ). "Kinh tế suy thoái → ???" (không rõ).
   Cortisol + action path = DRIVE. Cortisol − action path = HELPLESSNESS (§6.3).
   Threat TRỪU TƯỢNG hiện đại (AI thay thế, biến đổi khí hậu) không có action path.

3. RECOVERY BỊ XÓA: savanna có nhịp ngày/đêm, mùa stress/nghỉ.
   Hiện đại: alarm → tin tức → công việc → MXH → lo lắng → 24/7 không ngắt.
   Cortisol circadian rhythm bị phá: blue light → melatonin↓ → cortisol không hạ khi ngủ.

4. THREAT NHÂN TẠO: so sánh xã hội 150 người (savanna) vs TRIỆU (MXH).
   🟡 Serotonin hierarchy filter (§5) thiết kế cho nhóm nhỏ → quá tải khi scale triệu.
   Tin tức = hàng chục threat mới/NGÀY → cortisol spike không resolution liên tục.

→ EVOLUTIONARY MISMATCH: phần cứng 200.000 năm ↔ môi trường 250 năm (công nghiệp).
  Cortisol KHÔNG sai thiết kế — bị chạy NGOÀI THÔNG SỐ thiết kế.
  Kết nối PEM (Core-Deep-Dive/Society-Dynamics.md §9): mismatch không chỉ prediction — CẢ cortisol system.
  → Giống động cơ thiết kế 6.000 rpm bị chạy 15.000 rpm liên tục — SẼ hỏng.
```

### 6.7 Bốn Kịch Bản Cortisol × Hành Vi

```
🟡 Framework tổng hợp — 4 kịch bản cortisol trong cuộc sống:

KỊCH BẢN 1: DEADLINE PRODUCTIVE
  Cortisol: moderate, cấp tính.
  Controllability: CAO (biết phải làm gì, deadline khả thi).
  MR saturated, GR ~50-70%.
  → VTA DA↑ → NAc "wanting"↑ → PFC tăng cường → focused action.
  → Ví dụ: viết bài trước 6h chiều, chuẩn bị thuyết trình tuần sau.

KỊCH BẢN 2: CHRONIC PARALYSIS
  Cortisol: high, mãn tính.
  Controllability: THẤP (nợ nần, sếp toxic — không biết thoát cách nào).
  GR saturated → downregulated.
  → PFC teo + DA blunted + amygdala phì đại → bất lực tổng quát.
  → Ví dụ: "biết phải làm nhưng không thể bắt đầu" — mỗi ngày.

KỊCH BẢN 3: CORTISOL TREADMILL
  Cortisol: moderate→high, DAO ĐỘNG giữa cấp tính và mãn tính.
  Controllability: TẠM (mỗi deadline kiểm soát được, nhưng LIÊN TỤC không nghỉ).
  → Mỗi deadline = acute burst → DRIVE → hoàn thành.
  → Nhưng baseline DẦN TĂNG (allostatic load — McEwen, 1998).
    GR dần downregulate (FKBP5↑) → cần cortisol CAO HƠN cho cùng effect.
    = TOLERANCE (cơ chế GIỐNG nghiện — cần liều cao hơn).
  → Cuối cùng: crash = burnout. Baseline quá cao, PFC teo, DA blunted.
  → Ví dụ: startup founder 80h/tuần — productive 2 năm rồi sụp.
  🟡 Framework: "Cortisol treadmill" = Soldier pattern liên tục, cortisol-driven,
    KHÔNG chuyển sang dopamine-driven → tưởng "đam mê" nhưng thực ra "sợ dừng."
  → Cấu trúc = NGHIỆN STRESS (Koob model): chi tiết Research/Mismatch-Patterns.md P1.

KỊCH BẢN 4: OVERWHELM FREEZE
  Cortisol: SPIKE CAO + KHÔNG CÓ ACTION PATH.
  Controllability: cảm nhận = ZERO.
  → GR bão hòa 100% ngay lập tức → PFC collapse (Arnsten model).
  → Amygdala hijack → freeze/panic.
  → Behavioral shift: goal-directed → habitual (tự động, không suy nghĩ).
  → Ví dụ: nhận 20 email urgent cùng lúc + không biết bắt đầu từ đâu.
  → CAN THIỆP: cung cấp 1 action step RÕ RÀNG = khôi phục controllability.

→ KỊCH BẢN 1-4 áp vào predictive-chunk patterns (v5.5: nhãn mô tả, không phải cơ chế):
  Kịch bản 1 (deadline productive) = chunks external + cortisol moderate + DA cộng tác.
  Kịch bản 2 (chronic paralysis) = chunks external bị ép + cortisol mãn tính → DA tắt.
  Kịch bản 3 (treadmill) = chunks external duy trì bằng cortisol → burnout trajectory.
  Kịch bản 4 (overwhelm freeze) = bất kỳ ai khi cortisol spike + no action path.
  → Chi tiết Phase Model (4 pha × 4 biến thể × thời gian): Core-Deep-Dive/Chunk-Patterns.md §1.6.
```

### 6.8 Khác Biệt Cá Nhân: Cortisol Phenotype

```
🟢 Phản ứng cortisol KHÁC NHAU RẤT LỚN giữa các cá nhân:

GEN:
  FKBP5 (rs1360780 T allele): cortisol response MẠNH hơn, recovery CHẬM hơn.
    + Early life adversity → demethylation intron 7 → FKBP5 tăng bền vững
    → HPA axis dysregulated SUỐT ĐỜI. Gene × Environment interaction.
  NR3C1 (GR gene): BclI, ER22/23EK → sensitivity khác nhau.
  NR3C2 (MR gene): -2 C/G, I180V → threshold appraisal khác nhau.

EARLY LIFE PROGRAMMING:
  🟢 Weaver et al. (2004): chăm sóc tốt → demethylation GR promoter ở hippocampus
    → GR nhiều → HPA feedback tốt → cortisol THẤP hơn suốt đời.
    Adversity → GR methylated → HPA dysregulated → cortisol CAO hơn suốt đời.
  🟢 McGowan et al. (2009): child abuse → tăng methylation NR3C1 ở hippocampus (người).
  → Framework: THRESHOLD (Core.md §5) có CƠ SỞ SINH HỌC từ early life GR programming!
    Threshold cao/thấp KHÔNG CHỈ là "tính cách" — có nền tảng epigenetic.

3 PHENOTYPE CHÍNH:
  HIGH REACTOR: cortisol response lớn. Dễ đạt optimal zone (tốt).
    Nhưng cũng dễ "vượt" → lo âu, overwhelm. Risk: anxiety disorders.
    → Framework: PE Sensitivity cao (Core.md §5.3) có thể map vào đây.

  LOW REACTOR: cortisol response nhỏ. CẦN stimulus mạnh (deadline) mới đạt optimal.
    "Lười" bề mặt = chưa đủ cortisol cho ascending limb.
    Resilient hơn với stress cao. Risk: thiếu urgency trong tình huống cần.
    → Framework: "Cần deadline mới làm được" = low reactor, KHÔNG PHẢI lười.

  BLUNTED RESPONSE: ~20-30% người hầu như không tăng cortisol với stressor chuẩn.
    → Coping hiệu quả, HOẶC GR feedback quá mạnh, HOẶC appraisal "không đe dọa."
    → Một số liên quan psychopathy (low cortisol reactivity = ít nhạy hậu quả).

HABITUATION vs SENSITIZATION:
  🟢 Cùng stressor lặp lại → cortisol GIẢM (habituation). Adaptive.
  Stressor MỚI liên tục → cortisol có thể TĂNG (sensitization). Maladaptive.
  Sau stress mãn tính → HPA axis sensitized: stressor NHỎ → response QUÁ LỚN.
  → "Dễ nổi nóng / hoảng loạn vì chuyện nhỏ" = HPA sensitization, không phải yếu đuối.
```

### 6.9 GABA: Đối Trọng Tự Nhiên

```
🟢 GABA = chất ức chế CHÍNH của hệ thần kinh = "phanh tự nhiên."

Cortisol/GABA = TRỤC:
  Cortisol >> GABA → LO ÂU → phòng thủ → prediction ngắn → external compliance.
  GABA >> Cortisol → BÌNH TĨNH → PFC mở → prediction xa → internal có thể.
  CÂN BẰNG = VÙNG TỐI ƯU trên inverted-U → hiệu suất cao nhất.

GABA tự nhiên vs nhân tạo:
  Rượu, thuốc an thần = GABA agonist → "bình tĩnh giả" → GABA tolerance → NGHIỆN.
    → Giống opioid: bypass → tolerance → allostatic shift.
  Thiền, hít thở sâu = GABA tự nhiên → bình tĩnh thật → cortisol giảm bền.
    → Xây prediction skill (control breathing = controllable stressor = MR/GR optimize).
  Tập thể dục = cortisol CẤP TÍNH (acute) → rồi cortisol HẠ → GABA tăng.
    → "Tập thể dục cho HPA axis" = giữ flexibility của inverted-U.
    → Giống F6 tôn giáo: kiêng nhịn = acute controllable stress → flexibility.

→ Framework: can thiệp GABA = ĐƯA VỀ VÙNG TỐI ƯU, không phải "loại bỏ cortisol."
```

### 6.10 Cortisol × Nghiện + Hành Vi Cưỡng Chế

```
🟢 Koob & Le Moal (2008): CRH trong extended amygdala = trung tâm "mặt tối" nghiện.

CƠ CHẾ:
  Sử dụng chất: DA spike → nhưng ĐỒNG THỜI HPA axis activated (cortisol↑).
  Cai (withdrawal): DA↓↓ DƯỚI baseline + CRH↑ trong CeA/BNST → dysphoria cực.
    CRH ở đây KHÔNG PHẢI từ HPA axis — từ CRH neurons LOCAL trong extended amygdala.
    → Anxiety, irritability, craving = CRH-driven.
  Tái nghiện (relapse): stress = trigger MẠNH NHẤT.
    CRH release → VTA DA excited (CRH-R1) → cue-induced DA → craving → relapse.
    Cortisol potentiate cue-induced craving (fMRI confirm).

ALLOSTATIC SHIFT (Koob):
  Qua nhiều chu kỳ dùng→cai:
    DA system downregulate (D2↓ ở NAc). "Bright side" TỐI DẦN.
    CRH/cortisol "anti-reward" system upregulate. "Dark side" SÁNG DẦN.
    → Hedonic set-point DỊCH CHUYỂN: bình thường = dysphoria.
    → Dùng chất KHÔNG CÒN để "sướng" — mà để "bình thường."
    = TOLERANCE + DEPENDENCY cấu trúc.

→ Framework: nghiện = cortisol/CRH chiếm ưu thế + DA suy kiệt.
  12-step + spiritual recovery = cung cấp external structure (Soldier Gravity) +
    prediction xa (meaning) + community (oxytocin) → giảm CRH → phục hồi DA dần.
  → Xem Research/Religion.md §10 (Opioid Crisis ↔ Religion Decline).

HÀNH VI CƯỠNG CHẾ (không phải chất):
  🟢 Schwabe & Wolf (2009): stress mãn tính → goal-directed chuyển sang habitual.
    mPFC (goal-directed, model-based) yếu + dorsolateral striatum (habitual, model-free) mạnh.
  → Ăn cưỡng chế, cờ bạc, MXH compulsive = CƠ CHẾ TƯƠNG TỰ:
    Ban đầu goal-directed (vì thích) → stress → habitual (tự động, không nhạy outcome).
    → KHÔNG CẦN chất hóa học ngoại sinh. Cortisol mãn tính ĐỦ để tạo compulsive behavior.
```

### 6.11 Repetitive Behavior — Sequential Defense Under Cortisol

> Não có hệ phòng thủ SEQUENTIAL chống lại cortisol/uncertainty.
> Cortisol tăng → não tuyển dụng mạch ĐƠN GIẢN trước, PHỨC TẠP sau.
> Đây là TÍNH NĂNG bình thường. Chỉ trở thành bệnh lý khi hardware lỗi + cortisol mãn tính.
> **Phân tích toàn phổ (stimming → ritual → OCD):** Research/Mismatch-Patterns.md §P12.

```
MÔ HÌNH THỐNG NHẤT — SEQUENTIAL CIRCUIT RECRUITMENT:

  ┌────────────────────────────────────────────────────────────────────┐
  │ Cortisol       │ Circuit recruited │ Behavior   │ Outcome         │
  │────────────────│──────────────────│────────────│─────────────────│
  │ Thấp           │ Không cần         │ Không có   │ Bình thường     │
  │ Moderate       │ Tuyến 1 (additive)│ Stimming   │ Arousal ↓ → ok  │
  │ Cao (ngắn)     │ Tuyến 1 đủ        │ Stimming+  │ Arousal ↓ → ok  │
  │ Cao (dài)      │ Tuyến 1 KHÔNG đủ  │ → Tuyến 2  │ Ritual → done   │
  │ Mãn tính       │ Tuyến 2 quá tải   │ → Lỗi      │ OCD (nếu hw lỗi)│
  └────────────────────────────────────────────────────────────────────┘

TUYẾN 1 — STIMMING (arousal homeostasis):
  Mạch: cerebellum, proprioceptive, additive channels (NE/Cortisol)
  3 sub-functions đồng thời: calming (↓) + activating (↑) + micro-reward
  + Motor surplus discharge (xả motor → PFC focus tốt hơn)
  ~100% dân số. Habituate thành habit nếu lặp đủ lâu.
  🟢 Mohiyeddini 2013, Sarver 2015, Zentall & Zentall 1983

TUYẾN 2 — RITUAL (WM management):
  Mạch: OFC → basal ganglia → dlPFC → endpoint "done" signal
  Verbal (cấp 2): "ổn rồi" × 3 → done | near-universal
  Somatic (cấp 3): đặt cốc x lần → somatic resonance → done | underreported
  🔴 Cực kỳ phổ biến — xã hội normalize verbal, giấu somatic.
  🟢 Boyer & Liénard 2006, Hatzigeorgiadis 2011, Eilam 2012

BRIDGE: cortisol DURATION quyết định tuyến nào được tuyển dụng.
  Ngắn hạn → tuyến 1 đủ → recovery. Kéo dài → tuyến 2 được tuyển.
  Biến cá nhân: PE Sensitivity, cortisol baseline, PFC capacity, processing channel.

KHI TUYẾN 2 HỎNG → OCD:
  Hardware: OFC/dlPFC ratio lỗi (double failure) + cortisol mãn tính + uncertainty trừu tượng
  → Endpoint không đạt → loop automated → OCD.
  → Chi tiết đầy đủ: Research/Mismatch-Patterns.md §P12.
```

---

## 7. Norepinephrine (NE) — Volume

### 7.1 Cơ Chế

```
🟢 NE = chất khuếch đại — TĂNG cường độ TÍN HIỆU từ mọi kênh khác.

NE không tạo "muốn/thích/kết nối" — nó tăng VOLUME:
  Novelty + NE cao = tò mò MÃH LIỆT, hyperfocus → Van Gogh
  Novelty + NE thấp = tò mò NHẸ NHÀNG, bền bỉ → Darwin
  Opioid + NE cao = cảm nhận MÃNH LIỆT, ecstatic
  Opioid + NE thấp = cảm nhận NHẸ, pleasant
  Cortisol + NE cao = lo âu DỮ DỘI, panic
  Cortisol + NE thấp = lo âu NHẸ, unease

→ NE giải thích khác biệt TRONG cùng mode:
  Hai Architect cùng internal + high structure:
    NE cao: passionate, intense → Van Gogh
    NE thấp: calm, methodical → Darwin
  Cùng kênh gốc, cùng chunk config (external/internal), khác VOLUME.
```

### 7.2 NE × PE Sensitivity

```
🟡 NE cao TƯƠNG QUAN với PE Sensitivity cao:
  Signal mạnh → phản ứng mạnh → nhưng CŨNG habituate nhanh hơn
  → NE cao → amplitude cao + quen nhanh = PE Sensitivity cao

→ PE Sensitivity trong Core.md §5.3 có CƠ SỞ SINH HỌC từ NE + DRD4.
```

### 7.2b PE Sensitivity — Neurochemistry Basis (v6.0)

🟡 Core.md §5.3 gộp PE Sensitivity thành 1 tham số cho ứng dụng.
→ **Chi tiết đầy đủ 4 sub-mechanisms + encoding modality: PE-Sensitivity.md**
→ Section này giữ phần NEUROCHEMISTRY thuần (①②③). Sub ④ (generalization scope) và encoding modality xem PE-Sensitivity.md §5-7.
→ 3 sub-mechanisms dưới đây = CƠ SỞ SINH HỌC cho tham số PE Sensitivity. Gộp khi ứng dụng, tách khi phân tích sâu.

```
SUB 1 — AMPLITUDE (hóa học, hardware):
  = "Volume" tín hiệu dopamine khi PE xảy ra.
  Cùng PE, người này phản ứng MẠNH hơn người kia.
  Quyết định bởi:
    D2 receptor density (🟢 Volkow 2002): nhiều D2 → nhạy hơn với DA
    COMT Val/Met (🟢 Egan 2001): Met/Met → DA ở synapse lâu → signal dài
    NE level (§7.2): NE cao → khuếch đại tất cả tín hiệu
  → Hardware, thay đổi rất chậm (trừ D2 downregulate từ flooding).

SUB 2 — PRECISION WEIGHTING (processing, hardware + software):
  = Não đánh giá PE ĐÁNG TIN cỡ nào TRƯỚC KHI trả thưởng.
  🟢 Precision weighting trong predictive coding (Feldman & Friston 2010):
    Não gán trọng số (precision) cho mỗi PE → quyết định mức DA response.
    Precision CAO → "PE này đáng tin" → thưởng NHANH, MẠNH
    Precision THẤP → "PE này cần kiểm thêm" → thưởng CHẬM, từ từ

  → Sensitivity CAO = gán precision nhanh → "cái này hay!" → DA fire ngay
    = Phát hiện mới → sướng NGAY → threshold tạm thỏa mãn → nhảy domain (Improviser)
  → Sensitivity THẤP = gán precision thận trọng → "có vẻ hay, cần kiểm..."
    = Phát hiện mới → đối chiếu kỹ → thưởng DẦN DẦN khi confirm thêm (Architect)
    = Đối chiếu ít → thưởng ít. Đối chiếu thêm + confirm → thưởng thêm.
    → Buộc ở lại domain ĐỦ LÂU để collect đủ reward → chunks sync tự nhiên.

  → Có phần hardware (neural circuit), có phần software (training thay đổi được).

SUB 3 — HABITUATION RATE (learning, synaptic plasticity):
  = Tốc độ update prediction model → PE BIẾN MẤT khi model đã cập nhật.
  Update NHANH → PE "cháy" nhanh → cần PE mới sớm
  Update CHẬM → PE "cháy" chậm → cùng domain vẫn có PE lâu
  → Liên quan tới synaptic plasticity rate, BDNF, NMDA receptor function.

TẠI SAO GỘP CHO ỨNG DỤNG:
  3 sub-mechanism CÙNG HƯỚNG: cao-cao-cao hoặc thấp-thấp-thấp (tương quan).
  Người amplitude cao THƯỜNG precision nhanh VÀ habituate nhanh.
  → Gộp thành 1 tham số "PE Sensitivity" = mất ít precision, đủ cho predict hành vi.
  → Tách khi cần: phân tích sâu, can thiệp chính xác, hoặc edge case (amplitude cao
    nhưng precision thận trọng = Architect intense — NE cao + precision thấp).
```

### 7.3 Profile Nguy Hiểm: NE Cao + GABA Thấp

```
🟡 NE cao + GABA thấp = MỌI THỨ mãnh liệt + KHÔNG CÓ PHANH:
  Sáng tạo CỰC → nhưng cũng lo âu CỰC
  PE CỰC → nhưng cũng cortisol CỰC
  → Stereotype "nghệ sĩ điên" = NE cao + GABA thấp + Opioid/Novelty channel.
  → Van Gogh: intense + uncontrolled → output CỰC + suffer CỰC.
```

---

## 8. Vasopressin — Bảo Vệ Gắn Bó

```
🟢 Young & Wang (2004): vasopressin = MẶT PHÒNG THỦ của oxytocin.
  Oxytocin: "yêu" → gắn bó, tin tưởng
  Vasopressin: "bảo vệ cái mình yêu" → canh giữ, ghen tuông, territorial

🟢 Prairie vole: block vasopressin → VẪN gắn bó nhưng KHÔNG bảo vệ bạn đời.
→ Vasopressin MỘT MÌNH không tạo gắn bó — chỉ bảo vệ gắn bó ĐÃ CÓ.

Biến thiên:
  Vasopressin CAO: bảo vệ mạnh, ghen tuông, kiểm soát
  Vasopressin THẤP: gắn bó nhưng ít bảo vệ, dễ buông

→ Giải thích người YÊU THƯƠNG + KIỂM SOÁT:
  Oxytocin cao + vasopressin cao = "yêu nhiều, giữ chặt"
  KHÔNG mâu thuẫn — là 2 hệ bổ sung cùng mạnh.
```

---

## 9. Prolactin — Phanh + Giả Thuyết Healthy/Pathological

### 9.1 Cơ Chế

```
🟢 Prolactin = tín hiệu "ĐỦ RỒI, DỪNG."
  Bắn sau thỏa mãn: sau orgasm, sau ăn no, sau cho con bú.
  Ức chế dopamine TRỰC TIẾP → "không muốn thêm nữa."

Prolactin = ĐỐI TRỌNG dopamine (Core.md §4):
  Dopamine = ga (muốn thêm)
  Prolactin = phanh (đủ rồi)

  Prolactin cao → dễ thỏa mãn, biết dừng → LÀNH MẠNH
  Prolactin thấp → không dừng được, luôn muốn thêm → DỄ NGHIỆN

★ Prolactin = VÔ THỨC hoàn toàn. Không ai "quyết định" release prolactin.
  Dopamine tăng → prolactin bị ức chế (tuberoinfundibular pathway).
  Dopamine hạ → prolactin được giải phóng. Negative feedback TỰ ĐỘNG.
  → "Biết dừng" prolactin-driven ≠ "ý chí." Là THERMOSTAT, không phải quyết định.
  → Cái xã hội gọi "ý chí tốt" thường = prolactin cao + GABA cao + threshold thấp
    (3 hệ VÔ THỨC) chứ KHÔNG PHẢI PFC executive override (ý thức, tốn năng lượng, depletable).

🟢 BẰNG CHỨNG TRỰC TIẾP — Parkinson drugs:
  Dopamine agonists (pramipexole, ropinirole) → tăng DA → HẠ prolactin.
  🟢 Weintraub et al. (2010): 13.6% bệnh nhân Parkinson dùng DA agonist
    phát triển impulse control disorders (cờ bạc, mua sắm, hypersexuality).
  → CÙNG NGƯỜI: trước thuốc = "tự chủ", sau thuốc = "mất kiểm soát."
  → KHÔNG PHẢI thay đổi tính cách — là prolactin BỊ HẠ bởi thuốc.
  Antipsychotics (block DA) → TĂNG prolactin → ít impulsive nhưng cũng anhedonia.
  → Prolactin CŨNG có inverted-U: quá ít = không dừng, quá nhiều = không muốn gì.
```

### 9.2 🟡 Giả Thuyết: Lành Mạnh vs Bệnh Lý = Prolactin

```
🟡 "Lành mạnh" hay "bệnh lý" CÓ THỂ không thuộc tính kênh gốc —
   (nâng từ 🔴→🟡: Weintraub 2010 confirm DA agonist → impulse control disorders)
   mà là thuộc tính PROLACTIN:

  Novelty + Prolactin bình thường = tò mò, biết dừng → lành mạnh
  Novelty + Prolactin thấp = tò mò KHÔNG DỪNG, quên ăn ngủ → "ám ảnh"

  Opioid + Prolactin bình thường = thưởng thức, biết đủ → lành mạnh
  Opioid + Prolactin thấp = KHÔNG BAO GIỜ đủ → nghiện cảm giác

  Serotonin nhạy + Prolactin bình thường = so sánh nhẹ, kiểm soát được
  Serotonin nhạy + Prolactin thấp = KHÔNG BAO GIỜ đủ vị thế → kiệt sức

→ NẾU ĐÚNG: "chữa" hành vi bệnh lý KHÔNG CẦN thay kênh gốc (impossible)
  — chỉ cần điều chỉnh PROLACTIN (possible: thiền, mindfulness, exercise, thuốc).

→ Tesla: Prolactin thấp (suy đoán) → không dừng phát minh → output CỰC
  nhưng không dừng để ăn/ngủ/quan hệ → "bệnh lý" hay "thiên tài"? = CÙNG CƠ CHẾ.
```

---

## 10. Ma Trận Tương Tác

### 10.1 Phụ Gia × Kênh Gốc

```
🟡 Mỗi ô = cách phụ gia ảnh hưởng kênh gốc:

           │ Dopamine/Novelty │ Opioid          │ Oxytocin         │
───────────┼──────────────────┼─────────────────┼──────────────────┤
Serotonin  │ LỌC: PE bị      │ LỌC: cảm nhận  │ LỌC: gắn bó     │
           │ filter qua       │ bị filter qua   │ bị filter qua    │
           │ "ấn tượng?"      │ "flex được?"    │ "người khác      │
           │                  │                 │ thấy không?"     │
───────────┼──────────────────┼─────────────────┼──────────────────┤
Cortisol   │ ỨC CHẾ: giảm    │ ỨC CHẾ: giảm   │ ỨC CHẾ: giảm    │
           │ drive, PFC yếu,  │ cảm nhận,      │ trust, rút lui   │
           │ prediction ngắn  │ anhedonia       │ xã hội           │
───────────┼──────────────────┼─────────────────┼──────────────────┤
NE         │ KHUẾCH ĐẠI:     │ KHUẾCH ĐẠI:    │ KHUẾCH ĐẠI:     │
           │ tò mò mãnh liệt │ cảm nhận        │ gắn bó intense   │
           │ / nhẹ nhàng      │ intense / nhẹ   │ / nhẹ nhàng      │
───────────┼──────────────────┼─────────────────┼──────────────────┤
Vasopressin│ (ít tương tác    │ (ít tương tác   │ BỔ SUNG: bảo vệ │
           │ trực tiếp)       │ trực tiếp)      │ gắn bó đã có    │
───────────┼──────────────────┼─────────────────┼──────────────────┤
Prolactin  │ ỨC CHẾ: phanh   │ (ít tương tác   │ (ít tương tác    │
           │ dopamine trực    │ trực tiếp)      │ trực tiếp)       │
           │ tiếp             │                 │                  │
───────────┴──────────────────┴─────────────────┴──────────────────┘
```

### 10.2 Bốn Cascade Quan Trọng Nhất

```
CASCADE 1 — CORTISOL DOMINATES (stress mode):
  Cortisol ↑ → PFC ↓ → Dopamine ↓ → Oxytocin ↓ → chỉ còn survival
  → Mọi kênh gốc BỊ ỨC CHẾ → "không muốn gì, không thích gì, không kết nối"
  → Đây là DEPRESSION ở mức sinh hóa.

CASCADE 2 — DOPAMINE + OPIOID SYNERGY (flow state):
  Novelty PE + Opioid pleasure + cortisol thấp + NE vừa đủ
  = "FLOW" (Csikszentmihalyi) = drive equation TỐI ƯU tạm thời.

CASCADE 3 — OXYTOCIN + SEROTONIN SYNERGY (belonging):
  Gắn bó (oxytocin) + vị trí ổn (serotonin) + cortisol thấp
  = "THUỘC VỀ" — community PE = oxytocin + serotonin CÙNG LÚC.

CASCADE 4 — THRESHOLD SPIRAL (addiction path):
  Dopamine flooding → D2 down-regulate → threshold ↑
  → Cần nhiều hơn → flooding thêm → D2 giảm thêm → threshold ↑↑
  → Bẫy: threshold tăng liên tục → chỉ 1 source đủ → nghiện.
```

---

## 11. Đo Lường + Gen Markers

### 11.1 Có Thể Đo

```
🟢 TRỰC TIẾP (lab):
  D2 receptor density: PET scan (Volkow et al.)
  Cortisol: xét nghiệm máu/nước bọt (cortisol sáng, cortisol 24h)
  Serotonin metabolites: 5-HIAA trong nước tiểu/CSF
  Oxytocin: blood plasma levels (nhưng ĐỘ TIN CẬY tranh cãi)

🟢 GEN (genotyping):
  DRD4: 7-repeat → novelty-seeking, PE sensitivity cao
  COMT: Val/Val → dopamine metabolize nhanh → cần stim nhiều hơn
  DAT1: dopamine transporter → ảnh hưởng baseline dopamine
  OPRM1: opioid receptor sensitivity
  OXTR: oxytocin receptor → attachment tendency
  5-HTTLPR: serotonin transporter → sensitivity xã hội

🟡 GIÁN TIẾP (observation — phương pháp framework dùng):
  Kênh gốc: quan sát PE source tự nhiên (Emergence Phase — Core.md §11)
  Threshold: mức phức tạp tự chọn khi tự do
  Sensitivity: tốc độ chán / cần mới
  Compliance pattern: chunk alignment với reference group (quan hệ, không phải thuộc tính)
  → Không cần lab — observation đủ cho APPLICATION (cần lab để VERIFY).
```

### 11.2 Giới Hạn Đo Lường

```
🔴 KHÔNG THỂ đo TRỰC TIẾP:
  - Threshold CỤ THỂ (chỉ estimate từ behavior)
  - PE Sensitivity CON SỐ (chỉ relative: cao/thấp)
  - Chunk config pattern CHÍNH XÁC (emergent, thay đổi per context)
  - Kênh gốc MIX RATIO (chỉ estimate dominant channel)

→ Framework ACKNOWLEDGE giới hạn:
  Lab đo PHẦN CỨNG (gen, receptor density)
  Observation đo BIỂU HIỆN (behavior, preference)
  Cả hai CẦN nhau: lab alone không predict behavior, observation alone không explain mechanism.
```

---

## 12. Can Thiệp Sinh Học

### 12.1 Interventions Có Bằng Chứng

```
🟢 HẠ CORTISOL (ưu tiên #1 — Core.md §11.3):
  Thiền mindfulness → cortisol giảm + PFC tăng (Tang et al., 2015)
  Tập thể dục aerobic → cortisol giảm + BDNF tăng
  Ngủ đủ → cortisol reset hàng ngày
  Nature exposure → cortisol giảm (Bratman et al., 2015)
  Social support → cortisol giảm (oxytocin buffer)
  LOẠI BỎ nguồn stress (sếp toxic, nợ, quan hệ toxic) → GIẢM MẠNH NHẤT
    → Can thiệp ĐƠN GIẢN NHẤT nhưng thường BỊ BỎ QUA.

🟢 TĂNG DOPAMINE (cẩn thận — dễ overshoot):
  Cold exposure → dopamine tăng tạm (Šrámek et al., 2000)
  Exercise → dopamine + serotonin
  Novelty exposure → phasic dopamine
  ⚠️ Dopamine flooding (drugs, gambling, MXH) → D2 down → threshold TĂNG → BẪY

🟢 TĂNG SEROTONIN:
  Exercise → serotonin tăng
  Sunlight → serotonin synthesis
  Social status cải thiện → serotonin tăng tự nhiên 🟡
  SSRIs → serotonin tăng (thuốc, cần bác sĩ)

🟢 TĂNG OXYTOCIN:
  Physical touch → oxytocin
  Eye contact → oxytocin
  Helping others → oxytocin
  Group rituals (hát chung, thiền chung, cầu nguyện) → oxytocin synchronized 🟡

🟡 HẠ THRESHOLD:
  Dopamine fasting (giảm stimulation) → D2 up-regulate (chậm, tuần→tháng)
  Thiền → sensitivity tăng → cùng PE nhỏ → register nhiều hơn
  Nature → reset baseline tạm
  ⚠️ Threshold KHÔNG HẠ NGAY — calibrate CHẬM (tuần đến tháng).
```

### 12.2 Mapping Can Thiệp → Framework

```
🟡 Can thiệp ĐÚNG THỨ TỰ (matching Core.md §11.3):

BƯỚC 1: Hạ cortisol → PFC phục hồi → chunk config tự nhiên nổi lên
  → PHẢI LÀM TRƯỚC. Cortisol cao → mọi can thiệp khác BỊ CHẶN.

BƯỚC 2: Sửa schema (tâm lý, không thuần sinh hóa)
  → Schema thay đổi → prediction thay đổi → sinh hóa downstream thay đổi.

BƯỚC 3: Tăng PE source (per kênh gốc phù hợp)
  → Novelty: exposure thứ mới + đúng threshold
  → Opioid: trải nghiệm giác quan chất lượng
  → Oxytocin: kết nối + community

BƯỚC 4: Bảo vệ PE (tránh threshold tăng, tránh overjustification)

BƯỚC 5: Calibrate threshold (dopamine fasting nếu cần, thiền, nature)

BƯỚC 6: Nhận diện chunk config thật PER DOMAIN → thiết kế environment phù hợp
  → KHÔNG THỂ LÀM BƯỚC 6 TRƯỚC BƯỚC 1 (cortisol cao → chunk config GIẢ)
```

---

## Kết Nối

| Muốn hiểu thêm | Đọc file |
|-----------------|----------|
| Framework tổng quan | Core.md |
| Predictive-chunk config (depth × source × sync) | Core.md §6.0 |
| 4 pattern chi tiết + variants | Core-Deep-Dive/Chunk-Patterns.md |
| Soldier gravity + xã hội | Core-Deep-Dive/Society-Dynamics.md |
| Giáo dục qua framework lens | Applications/Education.md |
| Tôn giáo qua framework lens | Research/Religion.md |
| Ví dụ đối chiếu | Validation/Examples.md |
| Nhân vật lịch sử | Validation/Characters-Historical.md |

---

## Nguồn Tham Khảo

### Kênh gốc
- Schultz et al. (1997) — Dopamine = PE signal 🟢
- Kang et al. (2009) — Curiosity caudate nucleus 🟢
- Berridge & Robinson (1998, 2016) — Wanting vs liking 🟢
- Young & Wang (2004) — Oxytocin + pair bonding 🟢
- Warneken & Tomasello (2006) — Prosocial behavior trẻ em 🟢
- De Dreu et al. (2010) — Oxytocin in-group/out-group 🟢

### Phụ gia
- Raleigh et al. (1991) — Serotonin + hierarchy 🟢
- Arnsten (2009) — Cortisol ức chế PFC 🟢
- Sapolsky (2004) — Cortisol mãn tính + hippocampus 🟢
- LeDoux (1996) — Amygdala "low road" + fear processing 🟢
- McEwen (1998) — Allostatic load 🟢
- Ebstein et al. (1996) — DRD4 + novelty-seeking 🟢
- Cohen, McClure & Yu (2007) — Tonic/phasic dopamine 🟢
- Bowlby (1969) — Attachment theory 🟢

### Threshold + Measurement
- Volkow et al. (2001, 2002) — D2 receptor + reward sensitivity 🟢
- Egan et al. (2001) — COMT + working memory 🟢

### Prolactin
- Weintraub et al. (2010) — DA agonists → impulse control disorders (13.6%) 🟢

### Can thiệp
- Tang et al. (2015) — Thiền + PFC 🟢
- Bratman et al. (2015) — Nature exposure + cortisol 🟢
- Šrámek et al. (2000) — Cold exposure + dopamine 🟢
- Lally et al. (2010) — Habit formation 🟢

---

> *Neurochemistry Deep-Dive — v5.5*
> *File VERIFY: chi tiết sinh học cho framework.*
> *Đọc Core.md trước. Đọc file này khi muốn hiểu CƠ SỞ SINH HỌC.*