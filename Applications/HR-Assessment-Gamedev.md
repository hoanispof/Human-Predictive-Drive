# Hệ Thống Đánh Giá Nhân Sự — Game Dev Studio

> **Dựa trên:** Framework Động Lực v5.5 (Core.md) + Quản Lý Nhân Sự (HR-Management.md)
> **Prerequisite:** Core.md (Mô Hình Vuông §8.2, Depth composite §8.9, Compliance derived §8.3,
> Drive Equation §7, Dopamine inverted-U §6.6, Habituation Blindness §6.7),
> Applications/HR-Management.md (6 tệp, Chunk Config Card §15).
> **Ngành cụ thể:** Game Development (adapt được cho ngành sáng tạo khác)
> **Trạng thái:** Thiết kế ban đầu — cần test thực tế + calibrate
> **Nguyên tắc thiết kế:**
> - Câu hỏi tự nhiên, thân thiện → ứng viên thoải mái → trả lời thật
> - Tự chọn câu trả lời → câu nào họ chọn = data về chunk config per domain
> - AI phân tích kèm framework → nhất quán, không bias cá nhân
> - Ongoing assessment → chunk profile chính xác dần theo thời gian
>
> **Lưu ý:** Pattern = nhãn mô tả per domain, không phải kiểu người.
>
> **⚠️ QUY ƯỚC ĐỌC (v5.5):**
> Compliance = CHỈ SỐ PHÁI SINH (chunk_overlap giữa person.chunks và group.chunks), không phải thuộc tính.
> 4 nhãn (Soldier/Architect/Improviser/Drifter) = vị trí trên Mô Hình Vuông Source × Depth, per domain.
> CƠ CHẾ = predictive-chunk configuration (depth composite × source per domain).
> Depth = tham số gộp (4 sub-parameters: quality, connectivity, cluster formation, convergence).
> Sync = emerge từ depth đủ cao, KHÔNG phải trục riêng.

---

## Mục lục

1. [Kiến trúc hệ thống đánh giá](#1-kiến-trúc)
2. [Mô Hình Vuông × Assessment — v5.5](#2-vuông-assessment)
3. [Depth Composite × Seniority Assessment — v5.5](#3-depth-seniority)
4. [Convergence × Bridge Role Detection — v5.5](#4-convergence-bridge)
5. [Dopamine Inverted-U × Assessment — v5.5](#5-da-assessment)
6. [Tệp A: Đánh giá vị trí Mô Hình Vuông](#6-tệp-a)
7. [Tệp B: Đánh giá nhận thức chuyên môn](#7-tệp-b)
8. [Tệp C: Đánh giá kỹ năng thực hành](#8-tệp-c)
9. [AI Analysis Protocol v5.5](#9-ai-protocol)
10. [Đánh giá ongoing](#10-ongoing)
11. [Chunk Config Card Output v5.5](#11-config-card)
12. [Đặc thù Game Dev](#12-game-dev)
13. [Somatic × Verbal — Domain-Specific Observation](#13-somatic-verbal)
14. [Lưu ý đạo đức + giới hạn](#14-đạo-đức)
15. [Câu hỏi mở](#15-câu-hỏi)

---

## 1. Kiến Trúc Hệ Thống

### Tổng quan v5.5

```
TUYỂN DỤNG (trước khi nhận)
├── Tệp A: Vị trí Mô Hình Vuông — 20 câu, chọn ≥5, trả lời tự do
│   → OUTPUT: vị trí Vuông per domain, PE source, threshold, depth estimate
├── Tệp B: Nhận thức chuyên môn — 10 câu per role
│   → OUTPUT: depth composite domain, convergence indicators, growth potential
├── Tệp C: Kỹ năng thực hành — portfolio + task nhỏ
│   → OUTPUT: skill level hiện tại, depth sub-params evidence
└── AI phân tích: A + B + C → Chunk Config Card v1

LÀM VIỆC (ongoing)
├── Quan sát giao tiếp team (chat, meeting, retrospective)
├── Quan sát hành vi (task nào enjoy, task nào avoid, burst vs đều)
├── 1-on-1 data
├── Compliance derived observation (chunk_overlap vs team hiện tại)
└── AI cập nhật: Chunk Config Card v2, v3... → chính xác dần
```

### Tại sao "tự chọn câu" = data

```
🔴 Câu nào họ CHỌN trả lời reveal VỊ TRÍ trên Mô Hình Vuông:

  Chọn câu về kỷ niệm vui → Opioid ưu thế (thích hồi tưởng trải nghiệm)
  Chọn câu về ý tưởng/khám phá → Novelty ưu thế (thích nói về hiểu biết)
  Chọn câu về người/team → Oxytocin ưu thế (thích nói về kết nối)
  Chọn câu về thành tích → PE từ vị thế
  Chọn câu về tự do/phá vỡ → source internal + threshold cao
  Chọn câu dễ/an toàn → source external hoặc cortisol sensitivity

  → Thứ tự ưu tiên chọn câu = thứ tự ưu tiên PE source
  → Câu nào BỎ QUA cũng là data (domain PE KHÔNG mạnh hoặc nhạy cảm)

v5.5 THÊM: ĐỘ DÀI + ĐỘ SÂU trả lời = depth composite estimate:
  Trả lời dài, nhiều connection giữa ý → depth cao, connectivity cao
  Trả lời dài nhưng liệt kê rời rạc → depth TB, connectivity thấp (đảo)
  Trả lời ngắn, abstract, chính xác → depth có thể cao (convergence indicator)
  Trả lời ngắn, bề mặt → depth nông
```

---

## 2. Mô Hình Vuông × Assessment — v5.5 MỚI

🔴 Section MỚI v5.5 — thay đổi TRIẾT LÝ đánh giá từ "gán 1 pattern" sang "xác định vị trí per domain."

```
v5.0: Assessment → output = 1 compliance mode (Soldier/Architect/Improviser/Drifter)
v5.5: Assessment → output = VỊ TRÍ trên Mô Hình Vuông × PER DOMAIN

  VÀ CÙNG 1 NGƯỜI có thể:
    Domain game design: Architect (internal + deep)
    Domain code: Soldier-Deep (external + deep = học từ sách/senior)
    Domain management: Drifter (chưa xây chunks)
    Domain nghệ thuật: Improviser (internal + domain islands)

  → Assessment phải TÁCH PER DOMAIN, không gán 1 nhãn cho toàn bộ.
```

```
DETECT VỊ TRÍ VUÔNG — MAPPING CÂU HỎI:

  TRỤC X (SOURCE — Internal vs External):
    Câu 8 "task không đồng ý": theo = external, đề xuất sửa = mixed, tự làm cách khác = internal
    Câu 9 "chi tiết vs mục tiêu": chi tiết = external, mục tiêu = internal
    Câu 11 "nguyên tắc sống": có + tự tạo = internal, có + từ người khác = external
    Câu 5 "tự học": chọn gì + tại sao + nguồn nào = source indicator

  TRỤC Y (DEPTH — composite):
    Câu 1 "hứng thú": mức chi tiết mô tả = chunk quality per domain
    Câu 12 "chính mình nhất": abstraction level = convergence indicator
    Câu 20 "game director": scope + detail + connection = depth composite
    Tệp B toàn bộ: nhận thức chuyên môn = depth domain cụ thể

  ⚠️ v5.5: Soldier-Deep = VỊ TRÍ HỢP LỆ (Core.md §8.2)
    Detect: source external + depth SÂU = biết nhiều + từ nguồn tin cậy + verify ít
    Ví dụ game dev: programmer follow clean code books 10 năm = Soldier-Deep ở architecture
    → KHÔNG nhầm với Soldier-Cortisol (external vì PFC bị chặn, hạ stress → shift)
```

```
COMPLIANCE DERIVED v5.5 — TRONG ASSESSMENT:

  KHÔNG hỏi "bạn compliance cao hay thấp."
  THAY VÀO ĐÓ: quan sát chunk_overlap với reference group cụ thể.

  Reference group = team/studio culture chunks:
    Studio A: "gameplay first" → ứng viên chunks "art first" → overlap THẤP
    Studio B: "art first" → CÙNG ứng viên → overlap CAO
    → CÙNG người, KHÁC studio, KHÁC compliance score.

  ĐÁNH GIÁ COMPLIANCE LÚC TUYỂN DỤNG:
    1. Define studio culture chunks (giá trị, cách làm việc, priority)
    2. Detect ứng viên chunks qua Tệp A + B
    3. Tính overlap → FIT prediction
    → Compliance = output, KHÔNG phải input đánh giá.
```

---

## 3. Depth Composite × Seniority Assessment — v5.5 MỚI

🔴 Section MỚI v5.5 — depth composite 4 sub-params predict seniority tốt hơn years kinh nghiệm.

```
v5.0: đánh giá seniority qua skill + kinh nghiệm + prediction depth chung
v5.5: đánh giá seniority qua 4 SUB-PARAMS of depth (Core.md §8.9):

  SUB 1 — CHUNK QUALITY (prediction accuracy):
    Junior: "game hay vì đồ họa đẹp" → prediction nông
    Mid: "game hay vì core loop tạo PE liên tục" → prediction sâu hơn
    Senior: "game hay vì 3 systems interact tạo emergent gameplay" → prediction sâu + chính xác
    → Detect qua Tệp B câu 1-5: mức chi tiết + accuracy phân tích game

  SUB 2 — CONNECTIVITY (chunk sync):
    Junior: liệt kê rời rạc ("code tốt, design ok, art đẹp")
    Mid: kết nối 2 domain ("code architecture ảnh hưởng iteration speed")
    Senior: kết nối nhiều domain ("architecture choice → iteration speed → design quality → player feel")
    → Detect qua cách GIẢI THÍCH: liệt kê vs narrative vs hệ thống

  SUB 3 — CLUSTER FORMATION:
    Junior: chunks rải rác, chưa tổ chức
    Mid: 1-2 cụm domain rõ (chuyên môn chính + phụ)
    Senior: cụm domain lớn, ổn định, có hierarchy
    → Detect qua Tệp B câu 9-10: "muốn học gì" = cụm nào đang hình thành

  SUB 4 — CONVERGENCE:
    Junior: mỗi domain = đảo riêng
    Mid: bắt đầu thấy pattern chung giữa 2 domain
    Senior: chunks abstract shared across domains → "first principles" trong game dev
    → Detect qua câu 20 "game director": mức tích hợp cross-domain

⚠️ "5 năm kinh nghiệm" KHÔNG = depth composite cao.
  5 năm repeat cùng tasks = cluster maturity NHƯNG chunk quality có thể thấp.
  2 năm diverse + deliberate = chunk quality + connectivity có thể CAO HƠN.
  → Depth composite > years of experience cho predict performance.
```

---

## 4. Convergence × Bridge Role Detection — v5.5 MỚI

🔴 Section MỚI v5.5 — detect convergence cho bridge roles (PM, Lead, Technical Director).

```
BRIDGE ROLES TRONG GAME DEV = cần convergence CAO (Core.md §8.9):
  PM: bridge giữa design + code + art + business
  Lead Programmer: bridge giữa architecture + team + timeline
  Technical Director: bridge giữa tech + design + production
  Game Director: bridge giữa TOÀN BỘ domains

DETECT CONVERGENCE QUA ASSESSMENT:

  Indicator 1 — Cross-domain vocabulary:
    Thấp: dùng jargon riêng per domain, không translate
    Cao: dùng concepts CHUNG giải thích nhiều domain
    → Detect qua Tệp B câu 2-3: giải thích game cho người không chơi

  Indicator 2 — Analogy frequency:
    Thấp: giải thích trong domain bằng ví dụ CỦA domain
    Cao: giải thích domain A bằng ví dụ domain B ("code architecture giống urban planning")
    → Analogies = evidence of shared chunks between clusters

  Indicator 3 — "Tại sao" depth:
    Thấp: "game X hay vì vui" (1 level why)
    Cao: "game X hay vì core loop → creates PE → trong context genre Y → fills gap Z" (multi-level)
    → Multi-level why = chunks connected across abstraction levels

  Indicator 4 — Problem framing:
    Thấp: "bug này ở function X" (domain-specific)
    Cao: "bug này là hệ quả của architecture decision Y ảnh hưởng team workflow Z" (cross-domain)
    → Cross-domain framing = convergence evidence

BRIDGE ROLE FIT MATRIX:
  Convergence CAO + source internal → Game Director, Creative Director
  Convergence CAO + source external → Producer (hiểu nhiều domain + theo process)
  Convergence CAO + depth SÂU → Technical Director
  Convergence THẤP → specialist role (không phải bridge) → OK, không phải "kém"
```

---

## 5. Dopamine Inverted-U × Assessment — v5.5 MỚI

🔴 Section MỚI v5.5 — detect vị trí trên dopamine inverted-U (Core.md §6.6).

```
VỊ TRÍ TRÊN DA INVERTED-U ẢNH HƯỞNG ASSESSMENT ACCURACY:

  BÊN TRÁI ĐỈNH (DA thấp — anhedonia risk):
    Assessment behavior: trả lời ngắn, flat, "không biết", ít hứng thú
    ⚠️ DỄ NHẦM: tưởng "prediction depth nông" nhưng thực ra PE signal yếu
    → Detect: hỏi về quá khứ hứng thú → nếu CÓ + bây giờ KHÔNG → DA shift
    Câu 19 "từng thích nhưng giờ không": frequency + pattern = DA indicator

  ĐỈNH (DA tối ưu):
    Assessment behavior: hứng thú VỪA ĐỦ, selective, depth CÓ per domain
    → Đây là baseline mong muốn — assessment data đáng tin nhất

  BÊN PHẢI ĐỈNH (DA hơi cao — phasic > tonic):
    Assessment behavior: trả lời NHIỀU câu, hào hứng, nhiều ý NHƯNG nông per ý
    ⚠️ DỄ NHẦM: tưởng "explore + threshold cao" nhưng thực ra phasic > tonic
    → Detect: hỏi "cái gì bạn ĐÃ stick với > 1 năm?" → ít/không = bên phải đỉnh
    → Game dev cụ thể: "prototype nhiều, ship ít" = Improviser-DA hoặc DA hơi cao

  CỰC PHẢI (DA pathological — không trong scope HR assessment):
    Chuyển chuyên gia.

ASSESSMENT CORRECTION KHI BIẾT DA POSITION:
  Bên trái: tăng câu hỏi về quá khứ (khi DA tốt hơn). Portfolio > interview data.
  Đỉnh: data đáng tin, proceed bình thường.
  Bên phải: discount "explore breadth" → check DEPTH thật sự. Portfolio depth > verbal excitement.
```

---

## 6. Tệp A: Đánh Giá Vị Trí Mô Hình Vuông

### Hướng dẫn cho ứng viên

```
"Chào bạn! Dưới đây là 20 câu hỏi. Bạn KHÔNG cần trả lời hết —
chọn TỐI THIỂU 5 câu mà bạn MUỐN trả lời nhất.

Không có câu trả lời đúng/sai. Chúng tôi muốn hiểu bạn hơn —
không phải đánh giá bạn. Trả lời càng tự nhiên, càng dài, càng tốt.
Viết như đang kể chuyện cho bạn bè nghe.

Bạn có thể trả lời bằng text, voice, hoặc video — tùy thích."
```

### 20 câu hỏi

**Nhóm 1 — PE Source + Threshold (câu 1-7):**

```
1. "Kể về một lần bạn CỰC KỲ hứng thú với thứ gì đó —
    hứng thú đến mức quên thời gian. Chuyện gì đã xảy ra?"
    → Detect: kênh gốc (hiểu/cảm nhận/người), threshold (phức tạp/đơn giản)
    v5.5: + depth estimate (mức chi tiết kể = chunk quality domain đó)

2. "Nếu có 1 năm không cần lo tiền, bạn sẽ làm gì?"
    → Detect: kênh gốc, threshold, source (internal choice khi cost = 0)
    v5.5: câu này detect SOURCE rõ nhất — không external pressure → hành vi = internal chunks

3. "Thứ gì khiến bạn CHÁN NHẤT? Mô tả cảm giác chán đó."
    → Detect: PE deficit trigger, threshold (chán vì gì = thiếu gì)
    v5.5: + dopamine inverted-U indicator (chán vì thiếu novelty vs chán vì PE signal yếu)

4. "Có game/phim/sách nào bạn quay lại nhiều lần không? Tại sao?"
    → Detect: deepen vs explore per domain
    v5.5: quay lại = depth (tonic DA), không quay lại = breadth (phasic DA)

5. "Lần cuối bạn TỰ HỌC thứ gì đó (không ai bắt). Học gì? Tại sao?"
    → Detect: kênh gốc + source (tự học = internal)
    v5.5: + depth composite — học sâu hay học rộng? = cluster formation indicator

6. "Mô tả ngày nghỉ LÝ TƯỞNG của bạn."
    → Detect: kênh gốc thuần (không bị nhiễu công việc)
    Explore (đi chơi mới) vs Deepen (hobby quen) vs Oxytocin (gặp người)

7. "Có kỷ niệm nào về game (chơi hoặc làm) khiến bạn nhớ mãi?"
    → Detect: PE source trong domain game cụ thể
    Moment of discovery (Novelty), beauty/feel (Opioid), co-op (Oxytocin)
```

**Nhóm 2 — Source + Depth (câu 8-13):**

```
8. "Khi phải làm task mà bạn KHÔNG ĐỒNG Ý cách làm, bạn thường xử lý sao?"
    → Detect: source per domain (external = theo, internal = tự sửa)
    v5.5: QUAN TRỌNG — câu này detect TRỤC X Mô Hình Vuông trực tiếp
    → Nhưng câu trả lời = PER BỐI CẢNH (cùng người khác domain → khác answer)

9. "Bạn thích được hướng dẫn CHI TIẾT hay chỉ biết mục tiêu rồi tự tìm cách?"
    → Detect: source preference per task type
    v5.5: "tùy" + giải thích = DEPTH cao + per domain awareness

10. "Kể về lần bạn THẤT BẠI ở thứ gì đó. Bạn nghĩ gì sau đó?"
    → Detect: schema tương lai + cortisol recovery speed
    v5.5: + "thử lại khác cách" = chunks internal đang build
           "thử lại cùng cách" = chunks external (theo best practice)
           "vô ích" = schema bi quan (depth nông hoặc DA thấp)

11. "Bạn có 'nguyên tắc sống' nào không? Nếu có, kể vài cái."
    → Detect: source + depth per life domain
    v5.5: nguyên tắc TỰ TẠO = chunks internal sâu
           nguyên tắc TỪ NGUỒN = chunks external (có thể deep nếu verify qua kinh nghiệm)
           → Cả hai đều hợp lệ. Soldier-Deep CÓ nguyên tắc mạnh + từ nguồn.

12. "Khi nào bạn cảm thấy MÌNH LÀ CHÍNH MÌNH nhất?"
    → Detect: PE source chính + vị trí "natural" trên Vuông
    v5.5: mức TRỪU TƯỢNG câu trả lời = convergence indicator
           Cụ thể ("khi code game") = domain-specific chunks
           Abstract ("khi tạo ra thứ gì đó có ý nghĩa") = convergence cao

13. "Có ai (thật hoặc fiction) mà bạn ngưỡng mộ không? Tại sao?"
    → Detect: schema lý tưởng = vị trí MÔ HÌNH VUÔNG họ MUỐN
    v5.5: admire independence = thiên internal
           admire mastery = thiên depth
           admire versatility = thiên breadth (DA phasic)
```

**Nhóm 3 — Team + Context + Áp lực (câu 14-20):**

```
14. "Mô tả team/nhóm LÝ TƯỞNG bạn muốn làm việc cùng."
    → Detect: PE source social + compliance expectation
    v5.5: "team mà ai cũng giỏi" = source external (benchmark external)
           "team mà ai cũng tự do" = source internal
           "team mà ai cũng support nhau" = oxytocin PE

15. "Khi team bất đồng ý kiến, bạn thường đóng vai gì?"
    → Detect: vị trí Vuông trong social domain
    v5.5: per DOMAIN — "tùy topic" = depth variable per domain = câu trả lời giá trị nhất

16. "Điều gì ở sếp/leader khiến bạn MUỐN làm việc cùng? Điều gì khiến bạn KHÔNG MUỐN?"
    → Detect: PE source từ authority + kill switch
    v5.5: "KHÔNG MUỐN" = predict compliance friction vs studio culture

17. "Bạn thích làm việc MỘT MÌNH hay CÙNG NGƯỜI? Tại sao?"
    → Detect: Oxytocin PE, source preference
    v5.5: "tùy task" + giải thích per domain = HIGH VALUE answer = depth + per domain awareness

18. "Deadline gấp + task khó. Bạn phản ứng thế nào?"
    → Detect: cortisol response, vị trí cortisol inverted-U (Core.md §6.4)
    v5.5: "áp lực = động lực" = cortisol moderate → DA ↑ (cộng tác)
           "stress" = cortisol cao → PFC ức chế
           → KHÔNG judge — mà BIẾT để giao task phù hợp

19. "Có thứ gì bạn đã từng RẤT THÍCH nhưng bây giờ KHÔNG THÍCH nữa?
    Tại sao thay đổi?"
    → Detect: habituation pattern (Core.md §6.7) + DA inverted-U indicator
    v5.5: habituation NHANH = PE Sensitivity cao → bên phải DA inverted-U
           habituation CHẬM = tonic DA ổn → gần đỉnh
           KHÔNG habituation = có thể Soldier-Deep (external + stable PE)

20. "Nếu bạn là game director, game đầu tiên bạn muốn làm là gì? Tại sao?"
    → CÂU QUAN TRỌNG NHẤT cho game dev — reveal GẦN NHƯ TẤT CẢ:
    v5.5 detect:
      Source: follow trend (external) vs innovation (internal)
      Depth: mức chi tiết mô tả = chunk quality game domain
      Convergence: mức tích hợp cross-domain (design + art + tech + business)
      Threshold: scope ambition
      DA position: "nhiều idea nhỏ" (phasic) vs "1 vision sâu" (tonic)
```

### Cách đọc — ngoài nội dung

```
DATA ẨN (không chỉ nội dung trả lời):

  CÂU NÀO HỌ CHỌN:
    5 câu đầu tiên = PE source TOP 5
    Câu nào bỏ qua = PE source KHÔNG quan trọng hoặc nhạy cảm
    Chọn > 5 câu = threshold cao (muốn thể hiện nhiều) hoặc DA hơi cao (phasic)
    Chọn đúng 5 = source external (follow instructions) hoặc depth cao (selective)

  VĂN PHONG:
    Dài, chi tiết, kể chuyện → depth sâu per domain đó + PE source match
    Ngắn, khô → depth nông HOẶC PE source yếu HOẶC DA thấp (anhedonia)
    Hài hước, casual → cortisol thấp, thoải mái
    Formal, cẩn thận → source external cao hoặc cortisol sensitivity
    v5.5: LIÊN KẾT giữa ý → connectivity. Liệt kê rời → đảo (Improviser indicator)

  THỨ TỰ TRẢ LỜI:
    Câu đầu tiên = PE source MẠNH NHẤT (não default = thứ quan trọng nhất)
    Câu cuối = PE source vẫn đủ mạnh nhưng không ưu tiên

  KHÔNG TRẢ LỜI CÂU NÀO VỀ:
    Thất bại (câu 10) = có thể cortisol sensitivity → chưa build resilience chunks
    Team (câu 14-15) = có thể PE source ≠ social
    Quy tắc (câu 8-9) = có thể nhạy cảm về authority/compliance
    → Không trả lời ≠ không quan trọng. Có thể = quá nhạy cảm → cần data ongoing.
```

---

## 7. Tệp B: Đánh Giá Nhận Thức Chuyên Môn

### Hướng dẫn

```
"Phần này giúp chúng tôi hiểu cách bạn NGHĨ về game/lĩnh vực chuyên môn.
Không có đúng/sai. Chọn câu nào bạn thấy thú vị nhất."
```

### B1: Nhận thức Game Design (cho mọi role game dev)

```
1. "Chọn 1 game bạn thích. Nếu phải sửa 1 thứ trong game đó, bạn sửa gì? Tại sao?"
   → Detect: chunk quality per game design domain
   v5.5: sửa mechanic = system thinking, sửa feel = opioid depth, sửa social = oxytocin depth
   + mức giải thích "tại sao" = connectivity (chunks liên kết hay rời rạc)

2. "Game nào bạn nghĩ THIẾT KẾ GIỎI nhất? Giải thích cho người không chơi game."
   → Detect: chunk quality + convergence (translate cross-domain = convergence evidence)
   v5.5: khả năng giải thích cho non-gamer = CONVERGENCE INDICATOR MẠNH NHẤT
   (phải dùng chunks abstract/shared, không jargon)

3. "Nếu phải dạy 1 người chưa biết gì về game dev, bạn dạy gì TRƯỚC TIÊN?"
   → Detect: chunk hierarchy trong domain (thứ tự priority)
   v5.5: dạy tool = chunks cụ thể (nông), dạy tư duy = chunks abstract (sâu)
   → Convergence: dạy principle > dạy tool = convergence cao

4. "Xu hướng game nào bạn nghĩ sẽ THẤT BẠI trong 5 năm tới? Tại sao?"
   → Detect: prediction xa trong domain + source (independent = internal)
   v5.5: contrarian + evidence-based = internal source + depth sâu
   contrarian + "vibes" = internal source + depth nông → cần verify

5. "Mô tả 1 cơ chế game (bất kỳ) mà bạn thấy THÔNG MINH. Giải thích tại sao thông minh."
   → Detect: chunk quality mechanics + depth
   v5.5: giải thích HOW = chunk quality. Giải thích WHY it works on player = convergence.
```

### B2: Nhận thức chuyên môn per role

**Cho DEV:**

```
6. "Khi code bạn viết BUG, quy trình debug trong đầu bạn như thế nào?"
   → Detect: depth composite per coding
   v5.5: systematic (source external = follow method) vs intuitive (source internal = gut)
   → Cả hai có thể DEEP — Soldier-Deep debugger vs Improviser debugger

7. "Có pattern/architecture nào bạn thích dùng? Tại sao?"
   → Detect: depth + source per coding domain
   v5.5: "thích vì sách X nói" = external + có thể deep
         "thích vì tự thấy hiệu quả qua N project" = internal + verified deep

8. "Bạn đọc code người khác thế nào? Thấy gì trước tiên?"
   → Detect: chunk quality + connectivity per code reading
   v5.5: "structure first" = cluster-level reading (depth cao)
         "bugs first" = chunk-level reading (quality cao, connectivity thấp hơn)
```

**Cho DESIGNER:**

```
6. "Khi bạn design 1 level/UI/character, bạn bắt đầu từ đâu?"
   → Detect: process + source preference
   v5.5: "reference/research" = external source start → có thể Soldier-Deep designer
         "feeling/sketch" = internal source start → Improviser/Architect

7. "Game nào có ART DIRECTION bạn thích nhất? Tại sao?"
   → Detect: opioid depth + chunk quality per visual domain

8. "Bạn xử lý feedback 'thiết kế này không ĐẸP' thế nào?"
   → Detect: cortisol response + source flexibility
   v5.5: "tìm hiểu tại sao" = depth building, "defensive" = cortisol high,
         "ok sửa theo" = external source, "giải thích vision" = internal + deep
```

**Cho ARTIST:**

```
6. "Style nào bạn GIỎI NHẤT? Style nào bạn MUỐN THỬ?"
   → Detect: depth (giỏi nhất) vs DA position (muốn thử)
   v5.5: giỏi nhiều style = breadth (DA phasic) vs master 1 style = depth (DA tonic)

7. "Khi tạo art cho game, bạn ưu tiên gì: đẹp, rõ ràng, hay mood?"
   → Detect: PE source per art output
   v5.5: "tùy game" = convergence cao (hiểu context > preference)

8. "Bạn lấy INSPIRATION từ đâu ngoài game?"
   → Detect: convergence indicator (cross-domain inspiration = shared chunks)
   v5.5: diverse sources + CONNECTED explanation = convergence CAO
         diverse sources + separate = breadth nhưng convergence THẤP
```

### Đánh giá depth growth potential

```
9. "Kỹ năng nào bạn MUỐN học thêm nhất trong 1 năm tới? Tại sao?"
   → Detect: cluster formation direction + growth authenticity
   v5.5: cụ thể + "vì tôi thấy gap" = depth-aware (cluster building ACTIVE)
         chung chung + "vì hot" = source external + depth nông
         cross-domain goal + explained = convergence growth potential

10. "Kỹ năng nào bạn biết mình YẾU nhưng CHƯA học? Tại sao chưa?"
    → Detect: self-awareness depth + prediction cost awareness
    v5.5: honest answer = depth cao (biết what chunks missing)
          "chưa có thời gian" = cost > reward (drive equation §7 negative)
          "không thích" = PE source mismatch (ok, không phải yếu kém)
```

---

## 8. Tệp C: Kỹ Năng Thực Hành

### C1: Portfolio review

```
"Gửi cho chúng tôi 1-3 thứ bạn đã làm mà bạn TỰ HÀO NHẤT.
Không cần hoàn chỉnh — demo, prototype, sketch, concept đều ok.
Kèm theo: giải thích bạn đã làm gì, tại sao, và nếu làm lại thì sửa gì."

ĐÁNH GIÁ PORTFOLIO qua v5.5:

  Depth Composite Evidence:
    Chunk quality → prediction accuracy visible trong output
    Connectivity → cách các phần liên kết với nhau
    Cluster formation → có chuyên sâu domain nào rõ?
    Convergence → cross-domain integration trong 1 project?

  Source Evidence:
    Follow trend rõ → source external per design domain
    Twist trên trend → mixed source (external reference + internal modification)
    Hoàn toàn mới → source internal per design domain
    ⚠️ v5.5: "follow trend" ≠ kém. Soldier-Deep following proven patterns = hợp lệ.

  "Nếu làm lại thì sửa gì":
    Sửa chi tiết → depth awareness (chunk quality)
    Sửa toàn bộ approach → explore awareness (cluster restructuring)
    "Không sửa gì" → cần verify: tự tin + depth cao HAY depth nông (không thấy)

  DA Inverted-U Evidence:
    Nhiều project nhỏ, đa dạng → bên phải đỉnh (phasic > tonic)
    Ít project, sâu, polished → gần đỉnh hoặc bên trái
    1 project lớn + nhiều iteration → tonic DA strong = Architect potential
```

### C2: Task nhỏ (optional)

```
"KHÔNG BẮT BUỘC. Nếu bạn muốn, thử 1 trong các task sau (30-60 phút):"

Cho DEV:
  "Làm 1 mini prototype: nhân vật nhảy qua chướng ngại vật. Tool tùy chọn.
   Không cần đẹp — cần CHƠI ĐƯỢC."
  → Detect: execution + priority hierarchy (gameplay first vs visual first)
  v5.5: CÁCH LÀM = data — systematic (external process) vs intuitive (internal chunks)

Cho DESIGNER:
  "Thiết kế 1 level tutorial cho game platformer đơn giản.
   Mô tả bằng sketch/text/sơ đồ — format tùy."
  → Detect: player empathy (convergence — understand player mind model)
  v5.5: tutorial teaches through EXPERIENCE (convergence cao) vs through TEXT (convergence thấp)

Cho ARTIST:
  "Vẽ 1 character cho game mobile RPG. Style tùy chọn.
   Kèm mood/inspiration board nếu muốn."
  → Detect: execution + aesthetic depth + process visibility
  v5.5: mood board diversity + COHERENCE = convergence trong visual domain
```

---

## 9. AI Analysis Protocol v5.5

### Prompt Template v5.5

```
PROMPT TEMPLATE:

"Dựa trên Framework Động Lực v5.5 (đính kèm Core.md), phân tích chunk config ứng viên sau:

[Dán toàn bộ câu trả lời Tệp A + B + C]

Phân tích qua v5.5:

1. VỊ TRÍ MÔ HÌNH VUÔNG per domain:
   - Domain game design: Source (internal←→external) × Depth (nông←→sâu)
   - Domain chuyên môn [role]: Source × Depth
   - Domain team/social: Source × Depth
   - Domain career/self: Source × Depth
   → evidence cho mỗi domain

2. DEPTH COMPOSITE (domain chính):
   - Sub 1 (chunk quality): nông / TB / sâu — evidence
   - Sub 2 (connectivity): thấp / TB / cao — evidence
   - Sub 3 (cluster formation): chưa / hình thành / mature — evidence
   - Sub 4 (convergence): thấp / TB / cao — evidence

3. PHẦN CỨNG:
   - Kênh gốc ưu thế: Novelty / Opioid / Oxytocin — evidence
   - Threshold: thấp / TB / cao — evidence
   - PE Sensitivity: thấp / TB / cao — evidence
   - DA inverted-U estimate: trái / đỉnh / phải — evidence

4. PE source chính — evidence
5. Kill switch (mất gì → nghỉ) — evidence
6. Tệp nhân sự (1-6 shortcut) — evidence

7. COMPLIANCE DERIVED:
   - chunk_overlap vs studio culture [mô tả] → estimate
   - chunk_overlap vs team hiện tại [mô tả] → estimate
   → ⚠️ compliance = DERIVED, nếu đổi team → có thể thay đổi

8. FIT:
   - Fit role [X]: ★★★★★ — evidence
   - Fit team [mô tả team]: ★★★★★ — evidence
   - Convergence → bridge role potential? (cho PM/Lead)

9. ⚠️ CẢNH BÁO:
   - Soldier-Cortisol vs Soldier thật? (cần ongoing verify)
   - Architect-Dormant? (cần emergence phase test)
   - DA position ảnh hưởng accuracy?

10. RECOMMENDATION + câu hỏi cần hỏi thêm khi phỏng vấn

OUTPUT: Chunk Config Card v5.5 + recommendation + follow-up questions"
```

### Data ẩn AI nên phân tích

```
NGOÀI NỘI DUNG, AI phân tích:

  □ Câu nào họ CHỌN → priority PE source
  □ Câu nào họ BỎ → PE source không mạnh hoặc nhạy cảm
  □ Câu nào trả lời DÀI NHẤT → depth sâu nhất per domain
  □ Văn phong → cortisol level, source, depth
  □ Thứ tự trả lời → priority
  □ Mức chi tiết → chunk quality
  □ Connections giữa ý → connectivity (sub 2)
  □ Cross-domain references → convergence (sub 4)
  □ Contradictions → schema conflict hoặc per-domain difference (v5.5: OK nếu khác domain)
  □ Abstract vs concrete language → convergence indicator
```

---

## 10. Đánh Giá Ongoing

### Nguồn data trong quá trình làm việc

```
NGUỒN 1 — Chat/Slack quan sát (tự nhiên, không ép):
  Chủ động chia sẻ idea → source internal + PE Novelty
  Hỏi ý kiến trước khi làm → source external per domain đó
  Chia sẻ cảm xúc/meme → Oxytocin PE + cortisol thấp
  Ít nói → KHÔNG ĐỦ DATA — có thể: Novelty solo, cortisol, source external cao
  Phản ứng khi thay đổi kế hoạch → source + depth (sâu = resist vì reasons, nông = ok cả hai)

  v5.5 THÊM:
  → Cross-domain chat (nói về art trong tech channel) = convergence indicator
  → "Này cái này giống concept kia" = shared chunks evidence
  → Reaction time khi task thay đổi = cluster maturity (mature = slower to pivot)

NGUỒN 2 — Meeting/retrospective:
  v5.5 reframe — KHÔNG phải "ai nói nhiều = mode nào":
  → Ai nói nhiều + LIÊN KẾT ý = depth + connectivity
  → Ai nói nhiều + LIỆT KÊ = breadth + connectivity thấp
  → Ai nói ít + CHÍNH XÁC = depth cao + source internal + cost social cao
  → Ai nói ít + follow = source external per domain meeting
  → Ai bridge ý A với ý B = convergence CAO (PM potential)

NGUỒN 3 — Hành vi làm việc:
  Task nào họ làm NHANH nhất → drive cao = PE source match per domain
  Task nào họ TRỐN/delay → drive thấp = PE source mismatch hoặc cost > reward
  Burst vs đều → DA position indicator (burst = phasic, đều = tonic)
  v5.5: CÙNG task ở domains khác nhau → per-domain vị trí Vuông
    Ví dụ: code prototype = BURST, code maintenance = DELAY → khác vị trí per domain

NGUỒN 4 — 1-on-1:
  v5.5 reframe:
  "Dạo này thế nào?" →
    "Ok" = data KHÔNG ĐỦ (không phải "ổn thật")
    Chi tiết về task = PE source = task domain
    Chi tiết về team = PE source = social domain
    Chi tiết về career = PE source = vị thế
    "Hơi chán" = PE deficit → detect: BURNOUT (cortisol) hay BOREDOM (DA) → giải pháp KHÁC
```

### Compliance derived — ongoing observation

```
v5.5 MỚI: COMPLIANCE ĐO ONGOING, KHÔNG GÁN LÚC TUYỂN DỤNG:

  Observe chunk_overlap VỚI TEAM CỤ THỂ qua thời gian:
    Tháng 1-3: overlap estimate sơ bộ
    Tháng 3-6: overlap ổn định → compliance score reliable
    Tháng 6+: nếu overlap THAY ĐỔI → team dynamics shift hoặc person chunks đang build

  ⚠️ Overlap TĂNG theo thời gian = BÌNH THƯỜNG (shared experiences build shared chunks)
  Overlap KHÔNG TĂNG sau 6 tháng = deep mismatch → consider team change, không phải người kém
```

### AI ongoing analysis template

```
HÀNG THÁNG: feed data mới vào AI

"Dựa trên Chunk Config Card hiện tại [vX] và data mới dưới đây,
cập nhật config:

[Data chat/meeting/hành vi/1-on-1 tháng qua]

v5.5 analysis:
  1. Vị trí Mô Hình Vuông per domain: thay đổi gì?
  2. Depth composite sub-params: growth ở sub nào?
  3. Convergence: tăng/giảm? (quan trọng cho bridge role track)
  4. Compliance derived vs team: overlap thay đổi?
  5. DA inverted-U: position shift? (burnout vs boredom detection)
  6. PE source shift? (domain thay đổi → vị trí Vuông thay đổi per domain)
  7. Early warning: PE deficit? Cortisol tăng? Habituation Blindness?
  8. Recommendation: điều chỉnh gì trong management?"
```

---

## 11. Chunk Config Card Output v5.5

```
⚠️ v5.5 REDESIGN: "Mode Card" v5.0 → "Chunk Config Card v5.5"
  Khớp template từ HR-Management.md §15, nhưng customize cho game dev.

╔═══════════════════════════════════════════════════════════╗
║  CHUNK CONFIG CARD v5.5 — [Tên] — [Role Gamedev]          ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  PHẦN CỨNG (quan sát):                                    ║
║    Kênh gốc ưu thế:    □ Novelty  □ Opioid  □ Oxytocin  ║
║    Threshold:            □ Thấp    □ TB      □ Cao       ║
║    PE Sensitivity:       □ Thấp    □ TB      □ Cao       ║
║    Dopamine inverted-U:  □ Trái    □ Đỉnh    □ Phải     ║
║                                                           ║
║  TỆP SHORTCUT: □ 1-Lương  □ 2-Ý nghĩa  □ 3-Kết nối     ║
║                □ 4-Career  □ 5-Enjoy    □ 6-Tự do        ║
║                                                           ║
║  MÔ HÌNH VUÔNG PER DOMAIN GAME DEV:                       ║
║                                                           ║
║    Domain chuyên môn [role]:  [vị trí: ___________]       ║
║    Domain game design chung:  [vị trí: ___________]       ║
║    Domain team/collab:        [vị trí: ___________]       ║
║    Domain tool/pipeline:      [vị trí: ___________]       ║
║    Convergence:               □ Thấp  □ TB  □ Cao        ║
║    Somatic:Verbal ratio:      [___:___] (domain-specific) ║
║                                                           ║
║  DEPTH COMPOSITE (domain chính):                           ║
║    Sub 1 (quality):      □ Nông  □ TB  □ Sâu            ║
║    Sub 2 (connectivity): □ Thấp  □ TB  □ Cao            ║
║    Sub 3 (clusters):     □ Chưa  □ Hình thành  □ Mature ║
║    Sub 4 (convergence):  □ Thấp  □ TB  □ Cao            ║
║    → Seniority ước tính: □ Junior  □ Mid  □ Senior       ║
║                                                           ║
║  QUẢN LÝ:                                                 ║
║    PE source chính:      _______________                  ║
║    Kill switch:          _______________                  ║
║    Giao việc style:      _______________                  ║
║    1-on-1 focus:         _______________                  ║
║    Áp lực tối ưu:        □ Thấp  □ TB  □ Cao            ║
║    Rủi ro chính:         □ Burnout  □ Boredom  □ Anhedonia║
║    ⚠️ KHÔNG:              _______________                  ║
║                                                           ║
║  GAME DEV SPECIFIC:                                        ║
║    Best phase:           □ Concept  □ Production  □ Polish║
║    Bridge potential:     □ Specialist  □ Semi  □ Bridge   ║
║    Prototype speed:      □ Thấp  □ TB  □ Cao             ║
║                                                           ║
║  COMPLIANCE (DERIVED v5.5):                                ║
║    vs Team hiện tại:     chunk_overlap = _____ → ___     ║
║    vs Studio culture:    chunk_overlap = _____ → ___     ║
║    → Nếu đổi team:      overlap có thể thay đổi         ║
║                                                           ║
║  CONFIDENCE: 🔴🟡🟢 (dựa trên bao nhiêu data)            ║
║  VERSION: v[X] — [Ngày]                                   ║
║  NEXT UPDATE: [khi nào]                                    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## 12. Đặc Thù Game Dev

### Game dev cần MIX vị trí Vuông đặc biệt

```
GAME = sản phẩm cần CẢ explore VÀ deepen VÀ feel VÀ teamwork:

  Concept/pre-production: cần source internal + threshold cao + explore
    → Người gần cạnh Architect/Improviser per game design domain lead.
    → Người gần cạnh Soldier support (research, reference gathering).

  Production: cần depth + process + consistency
    → Soldier-Deep per domain lead execution.
    → Architect define architecture → Soldier-Deep implement.
    → Improviser chuyển sang problem-solving per task, KHÔNG manage process.

  Polish: cần opioid depth + chi tiết + patience
    → Người depth cao + tonic DA (gần đỉnh/bên trái) lead polish.
    → Người phasic DA (bên phải đỉnh) có thể BỎ QUA phase này → BÌNH THƯỜNG.

  Launch + live ops: cần process + team + adapt
    → Source external (follow process) + oxytocin (team coordination) lead.
    → Convergence cao = hiểu cross-domain issues = PM value.

→ Game dev studio cần ĐỦ MIX vị trí Vuông, và BIẾT phase nào dùng ai lead.
→ v5.5: per PHASE × per DOMAIN = matrix phức tạp hơn v5.0 nhưng chính xác hơn.
```

### Đặc thù role × vị trí Vuông

```
PROGRAMMER:
  Thường: Novelty + depth per coding domain
  Vị trí Vuông phổ biến: Architect hoặc Soldier-Deep per architecture domain
  ⚠️ ép Soldier-Deep programmer vào innovation role = frustrated (depth external, không switch)
  ⚠️ ép Improviser programmer vào maintenance = boredom (DA phasic > tonic → PE chết)
  Tối ưu per phase:
    Architect-programmer → system design
    Soldier-Deep-programmer → implementation reliable
    Improviser-programmer → prototyping, experimentation

GAME DESIGNER:
  Thường: Novelty + Opioid mix
  Convergence quan trọng: design = BRIDGE domain (mechanic + feel + player psychology)
  → Convergence CAO = tốt cho designer (hiểu cross-domain impact of design decisions)
  ⚠️ Source internal pure + convergence thấp = idea nhiều, không integrate được = ship ít
  Tối ưu: Architect per game design domain (depth + source internal + convergence)

ARTIST:
  Thường: Opioid mạnh → aesthetic PE source
  Vị trí Vuông: variable — có Architect-artist (style system) VÀ Improviser-artist (style hopping)
  ⚠️ ép artist vào style không enjoy = opioid PE chết → output quality giảm
  v5.5: Soldier-Deep artist = follow art direction consistently = GIÁ TRỊ (không phải "thiếu sáng tạo")
  Tối ưu: match style preference → PE sustained → quality output

PRODUCER/PM:
  Thường: tệp 3 (kết nối) hoặc tệp 4 (career) hoặc tệp 1 (process)
  v5.5: CONVERGENCE = most important trait cho PM (§4)
  → PM convergence cao = bridge giữa domains → hiểu cross-domain issues
  → PM convergence thấp = project-manage by checklist → miss systemic issues
  ⚠️ Producer tệp 2 (ý nghĩa) + source internal = over-scope vì "phải hay hơn nữa"
  Tối ưu: producer BIẾT framework + convergence cao + adapt per team member

SOUND/MUSIC:
  Thường: Opioid CỰC MẠNH (auditory PE source) — somatic-primary
  Vị trí Vuông: thường Improviser hoặc Architect per sound domain
  → Specialist — convergence với game domains = bonus nhưng không bắt buộc
  Tối ưu: cho specialist focus, ít context switch → PE sustained
```

### Sinh viên mới ra trường vs Senior — v5.5

```
SINH VIÊN MỚI:
  Depth composite: nông (4 sub-params đều thấp) — BÌNH THƯỜNG, XÂY ĐƯỢC
  Source: chưa calibrate → vị trí Vuông ĐANG HÌNH THÀNH per domain mới
  v5.5: ĐỪNG gán vị trí Vuông CỨNG cho sinh viên — config đang forming

  ĐÁNH GIÁ ƯU TIÊN:
    1. Phần cứng: kênh gốc + threshold + PE sensitivity → thiên hướng NỀN (Core.md §8.6)
    2. DA inverted-U: predict explore/deepen tendency → growth trajectory
    3. Growth potential: domain nào họ TỰ CHỌN invest → PE source thật
    4. Skill hiện tại: tham khảo, KHÔNG quyết định (skill train 6 tháng, chunks thay đổi chậm hơn)

  → SINH VIÊN: hire PHẦN CỨNG + PE SOURCE, train DEPTH per domain

SENIOR:
  Depth composite: nên CAO ở domain chuyên môn. Sub 3-4 = differentiate mid vs senior.
  Vị trí Vuông: đã calibrate → predict được behavior per domain
  v5.5: THÊM assessment:
    Sub 4 convergence → predict bridge role potential
    Cluster maturity → predict flexibility khi pivot

  ĐÁNH GIÁ ƯU TIÊN:
    1. Depth composite per domain → verify seniority (sub-params > years)
    2. Convergence → bridge role fit? (cho lead/director position)
    3. Source per domain → fit culture? (compliance derived vs studio chunks)
    4. Schema tương lai: "nỗ lực = được đền đáp" hay cynical? (burnout history)
    5. Kill switch: biết để PHÒNG NGỪA
    6. DA inverted-U: still near peak? (long career + stable = good sign)

  → SENIOR: check DEPTH COMPOSITE + CONVERGENCE + FIT + SCHEMA
```

---

## 13. Somatic × Verbal — Domain-Specific Observation

```
⚠️ v5.5 CLARIFICATION: Somatic/Verbal KHÔNG phải trục cơ bản của Mô Hình Vuông.
  Somatic/Verbal = QUAN SÁT LEVEL (observable ratio trong 1 domain cụ thể).
  Không nằm trong 2 trục Source × Depth.
  Vẫn HỮU ÍCH cho game dev assessment vì output quality có thể khác.

TẠI SAO GIỮ TRONG GAMEDEV ASSESSMENT:
  Game dev output = CẢ FEEL (somatic) VÀ STRUCTURE (verbal):
    Animation quality → somatic evaluation
    Architecture decision → verbal evaluation
    Gameplay feel → somatic evaluation
    Systems design → verbal evaluation
  → Biết somatic:verbal ratio = biết CÁCH họ evaluate output per domain

DETECT SOMATIC (behavioral, không phải self-report):
  Test 1 — "Show don't tell":
    Cho xem 2 version animation/sound (1 polished, 1 chưa ổn)
    Hỏi "khác gì?" → Somatic: body language, struggle giải thích (chunks non-verbal)
                    → Verbal: list kỹ thuật ngay, structured (chunks verbal)
  Test 2 — "Fix this":
    Cho asset bị off tinh tế → đo tốc độ tìm ra vấn đề
    Somatic: gut check nhanh (giây). Verbal: systematic check (phút).
  Test 3 — "Tại sao thích?":
    Hỏi về work yêu thích → Somatic: pause dài, "không biết... nó đúng ấy"
                           → Verbal: structured answer ngay

SOMATIC:VERBAL RATIO PER ROLE (ước tính):
  Programmer: ~20-30 / 70-80 (verbal-primary OK, somatic bonus cho game feel code)
  Game Designer: ~50-60 / 40-50 (cần cả hai: somatic cho feel, verbal cho document)
  Artist: ~60-70 / 30-40 (somatic cho aesthetic, verbal cho style guide communication)
  Producer/PM: ~20-30 / 70-80 (verbal-primary preferred)
  Sound/Music: ~70-80 / 20-30 (somatic cao nhất)

v5.5: somatic:verbal ratio ghi trong Chunk Config Card nhưng là SUPPLEMENTARY DATA,
không phải core assessment. Core = vị trí Mô Hình Vuông per domain.
```

### Somatic-primary hiring — Cho studio cần gameplay feel quality

```
🔴 Section này specific cho studio mà lead là somatic-primary evaluator.
Chiến lược cho cấu hình team cụ thể, KHÔNG phải gamedev HR phổ biến.

KÊNH TÌM (nơi somatic + creative tụ lại):
  Game jam: tự filter (thích game + có output + self-driven)
  Portfolio platform: output = somatic evidence nhìn thấy trực tiếp
  Cộng đồng creative tool: người tự làm = opioid PE + self-driven
  → Scout qua OUTPUT, không qua CV

JD DESIGN CHO SOMATIC:
  JD truyền thống filter verbal-primary (đọc requirements → check list → apply)
  JD cho somatic = SHOW thay vì TELL:
    Video gameplay ngắn → "xem cái này, thấy gì?"
    Clip animation A vs B → "cái nào đúng hơn?"
    Sound design A vs B → "cái nào sướng hơn?"
  → JD chính nó = bước test đầu tiên (somatic tự bị hút, verbal tự filter ra)

ƯU TIÊN TRẺ + CHƯA KINH NGHIỆM cho somatic roles:
  v5.5 explanation: somatic = chunks non-verbal per domain
  Chưa kinh nghiệm → chunks non-verbal chưa bị override bởi verbal framework
  Đã kinh nghiệm → Soldier-Deep per verbal framework có thể SUPPRESS somatic chunks
  → Hire phần cứng somatic, train domain skill = strategy optimal cho studio somatic-first
  ⚠️ Không apply cho TẤT CẢ roles — chỉ roles mà somatic output = quality differentiator
```

---

## 14. Lưu Ý Đạo Đức + Giới Hạn

```
MINH BẠCH:
  □ Nói rõ: "Chúng tôi muốn hiểu bạn hơn để match đúng vị trí"
  □ KHÔNG NÓI: "Đây là bài test tâm lý" (vì không phải — là framework suy luận)
  □ Cho ứng viên BIẾT chunk config nếu họ muốn (sau khi hire)
  □ Config = TOOL hỗ trợ quản lý, KHÔNG PHẢI label cố định

GIỚI HẠN:
  □ Chunk Config Card = ESTIMATE, confidence thấp ban đầu → tăng dần
  □ Người có thể MASK (trả lời strategic) → cần ongoing data
  □ Vị trí Vuông THAY ĐỔI per domain + theo thời gian
  □ Đừng từ chối ứng viên CHỈ vì vị trí Vuông → check FIT, không judge VALUE
  □ Mismatch vị trí × role ≠ người kém → có thể role khác PHÙ HỢP
  □ v5.5: compliance = DERIVED → cùng người khác team = khác behavior → đừng gán "khó hợp tác"

KHÔNG DÙNG ĐỂ:
  ❌ Label cố định ("anh là Soldier, mãi là Soldier")
  ❌ Phân biệt đối xử ("depth nông không xứng lead" — depth XÂY ĐƯỢC)
  ❌ Thay thế phỏng vấn trực tiếp (data bổ sung, không thay thế)
  ❌ Đánh giá giá trị con người (chunk config ≠ giá trị)
  ❌ Judge "tệp thấp" vs "tệp cao" (6 tệp = shortcut, không có hierarchy)

PRIVACY v5.5:
  □ Ongoing observation (chat, meeting) → cần minh bạch với team
  □ "Framework giúp quản lý hiểu team tốt hơn" → ok
  □ "AI đang phân tích chat của bạn" → KHÔNG ok nếu không consent
  □ Aggregate data (team pattern) ok. Individual tracking without consent = ethical issue.
```

---

## 15. Câu Hỏi Mở

| # | Câu hỏi | Ưu tiên |
|---|---------|---------|
| 1 | 20 câu tệp A: đủ detect vị trí Vuông per domain? Cần thêm câu domain-specific? | Cao |
| 2 | AI analysis accuracy: test v5.5 prompt với bao nhiêu người để calibrate? | Cao nhất |
| 3 | Mask detection: v5.5 ongoing data tốt hơn v5.0 1-shot? Bao nhiêu? | Cao |
| 4 | Depth composite 4 sub-params: predict game dev seniority tốt hơn years? | Cao nhất |
| 5 | Convergence: predict PM/lead effectiveness trong game dev? | Cao |
| 6 | DA inverted-U position: detect qua assessment reliable? | Cao |
| 7 | Somatic detection: tests valid cross-culturally? | TB |
| 8 | Legal: privacy concern khi ongoing analyze chat team? | Cao |
| 9 | Remote game dev team: detect chunk config khó hơn bao nhiêu? | TB |
| 10 | Soldier-Deep vs Architect: differentiate trong game dev hiring? | Cao |

---

## 16. Kết Nối

| Tham khảo | File | Mối liên hệ |
|-----------|------|-------------|
| Framework cốt lõi | Core.md | Tất cả concepts |
| Mô Hình Vuông | Core.md §8.2 | Source × Depth per domain |
| Depth composite | Core.md §8.9 | 4 sub-params → seniority (§3) |
| Compliance phái sinh | Core.md §8.3 | Derived → hiring + ongoing |
| Dopamine inverted-U | Core.md §6.6 | Assessment accuracy (§5) |
| Habituation Blindness | Core.md §6.7 | Ongoing PE deficit detection |
| ECP | Core.md §9 | Tại sao external source phổ biến |
| 6 tệp nhân sự | HR-Management.md §2 | Tệp 1-6 chi tiết |
| Chunk Config Card | HR-Management.md §15 | Template gốc |
| Convergence × teams | HR-Management.md §5 | Bridge roles |
| Burnout vs Boredom | HR-Management.md §6 | DA-based diagnosis |
| 4 pattern chi tiết | Core-Deep-Dive/Chunk-Patterns.md | Variants, shift, phase model |
| Đồng nghiệp tương thích | Applications/Relationships.md | Team compatibility |
| Psychometrics | Research/Psychometrics-Mapping.md | Battery đo chunk config |

---

> *Hệ Thống Đánh Giá Nhân Sự — Game Dev Studio — Framework v5.5*
> *4 sections MỚI v5.5: Mô Hình Vuông × Assessment (vị trí per domain, Soldier-Deep hợp lệ),*
> *Depth Composite × Seniority (4 sub-params > years), Convergence × Bridge Roles (PM/Lead detection),*
> *Dopamine Inverted-U × Assessment (detect DA position, correct accuracy).*
> *Chunk Config Card v5.5 redesign: depth sub-params, convergence, compliance derived, game dev specific.*
> *AI prompt template v5.5: vị trí Vuông per domain, depth composite, compliance derived, DA position.*
> *Somatic/Verbal = domain-specific observation (supplementary, không phải core trục).*
> *Prerequisite: Core.md §5-8, §8.9, §6.6-6.7.*
