# Schema Atlas — Bản Đồ Schema + Domain Architecture

> **Trạng thái:** DRAFT — phân tích trục gom nhóm schema + domain
> **Ngày:** 2026-03-17
> **Mục đích:** Tìm kiến trúc khả thi cho "bản đồ" schema + domain
> **Reference:** Core-v7-UD.md, Component-Interaction-Map.md

---

## 1. Schema Axes — Trục Gom Nhóm Schema

### 1.0 Tại sao Schema KHÔNG THỂ phân tích chính xác?

```
"Sao không phân tích chính xác schema từng người đi?"
→ Câu hỏi tự nhiên. Câu trả lời: KHÔNG THỂ. Và đây là TẠI SAO:

1. SCHEMA = HỆ THỐNG TÍNH TOÁN CỦA NÃO (phần mềm cực kỳ phức tạp)
   → ~86 tỷ neurons × ~100 nghìn tỷ connections = hệ thống lớn nhất biết
   → Schema = PATTERNS trong hệ thống này → không thể đọc trực tiếp
   → Giống: biết máy tính có 1 tỷ transistor → KHÔNG đọc được mã nguồn từ transistor

2. SCHEMA = MULTI-MODAL (không chỉ "suy nghĩ")
   → Mỗi schema encoded ở NHIỀU modalities đồng thời:
     Verbal ("tôi biết..."), Visual (hình ảnh), Somatic (cơ thể cảm nhận),
     Motor (thói quen tay chân), Emotional (cảm xúc tự động)
   → Ngôn ngữ chỉ capture VERBAL modality = ~1/6 schema thật
   → "Sợ chết" = label ngôn ngữ cho thứ CỰC KỲ phức tạp bên dưới
   → 2 người cùng "sợ chết" → schema thật KHÁC HOÀN TOÀN:
     A: "sợ mất người thân đột ngột" (trauma-based, somatic: tim đập)
     B: "sợ tồn tại vô nghĩa" (existential, verbal: nghĩ nhiều)
     → Cùng label, khác gốc, khác treatment

3. SCHEMA SÂU = BODY ADAPTATION (không chỉ "trong não")
   → Schema sâu (L4-L5) ĐÃ embed vào CƠ THỂ:
     cortisol baseline, muscle tension, gut flora, sleep patterns,...
   → Scan não CHƯA đọc được body-embedded schemas
   → Chính người đó CŨNG không biết (unconscious + somatic)
   → → Cần thời gian QUAN SÁT DÀI + body awareness mới "chạm" được

4. SCHEMA THAY ĐỔI LIÊN TỤC (không tĩnh)
   → Schema = dynamic, thay đổi theo context, mood, thời gian
   → "Chụp" schema lúc NÀY → lúc SAU ĐÃ hơi KHÁC
   → Giống chụp ảnh sông: thấy nước nhưng nước ĐÃ chảy đi

5. KHOA HỌC HIỆN ĐẠI CHƯA ĐỦ CÔNG CỤ
   → fMRI: thấy VÙNG NÃO active, KHÔNG thấy schema content
   → EEG: thấy sóng não, KHÔNG thấy schema content
   → Behavioral tests: thấy OUTPUT, suy ngược PATTERN, KHÔNG thấy schema trực tiếp
   → → Tất cả hiện tại = ƯỚC LƯỢNG gián tiếp

VẬY FRAMEWORK LÀM GÌ ĐƯỢC?
  → KHÔNG phân tích chính xác schema (impossible hiện tại)
  → CÓ THỂ: nhận diện PATTERN (hành vi lặp lại = schema sâu biểu hiện)
  → CÓ THỂ: ước lượng NHÓM (schema thuộc trục nào, lớp nào)
  → CÓ THỂ: suggest HƯỚNG (có schema sâu ở vùng NÀY → fix body + therapy)
  → = CÔNG CỤ NAVIGATE, không phải GPS chính xác
  → = Tốt hơn "đoán mò" (hiện tại đa số) → nhưng chưa phải "chính xác tuyệt đối"

  → Hiện nay: hầu hết mọi người CẢM NHẬN + ĐOÁN MÒ về suy nghĩ mình
  → Framework: cho CẤU TRÚC để cảm nhận CÓ HƯỚNG + đoán CÓ CƠ SỞ
  → "Công thức, không đáp án" = cho tool để TỰ KHÁM PHÁ, không phải đọc xong biết hết
```

### 1.1 Tại sao cần gom nhóm?

```
Schema = muôn hình vạn trạng → không thể liệt kê hết
NHƯNG: có thể PHÂN LOẠI theo trục → thấy pattern → predict behavior

Câu hỏi: bao nhiêu trục? Trục nào?
→ Quá ít = mất nuance. Quá nhiều = không dùng được.
→ Cần: ÍT NHẤT trục, NHIỀU NHẤT predictive power.
```

### 1.2 Ba Trục Core (đủ ~80% predictive power)

```
① DEPTH (surface → deep):
   = Schema ảnh hưởng RỘNG cỡ nào? Khó thay đổi cỡ nào?

   Surface: "trời mưa mang ô" → 1 context, đổi dễ
   Mid:     "phải luôn productive" → cross-context, đổi khó
   Deep:    "tôi vô giá trị" → MỌI context, đổi cực khó

   Predictive power: ★★★★★ (CAO NHẤT)
   → Deep schema predict hành vi ACROSS contexts
   → Biết L5 schema = predict phần lớn behavior patterns
   → Clinical validated: Beck's core beliefs (deep) vs automatic thoughts (surface)

② VALENCE — ⚠️ REFRAME: KHÔNG CÓ "schema âm" — chỉ có XUNG ĐỘT:

   CŨ (đơn giản hóa): Schema "dương" (tốt) vs Schema "âm" (xấu)
     → Gợi ý: có schema BẨM SINH xấu → phải fix
     → SAI: MỌI schema đều hình thành ĐỂ PHỤC VỤ body → luôn "dương" ban đầu

   MỚI (chính xác): MỌI schema đều DRIVE DƯƠNG (phục vụ body)
     → "Kiềm chế lời nói" = DƯƠNG khi ở nhà bố mẹ strict (bảo vệ body)
     → "Mở lòng giao tiếp" = DƯƠNG khi ở công ty supportive (serve connection)
     → CÙNG schema → KHÁC context → từ "dương" THÀNH "âm"
     → = Schema KHÔNG có dấu cố định → CONTEXT cho dấu

   "ĐAU TÂM LÝ" = gì?
     KHÔNG phải: "có schema xấu"
     MÀ LÀ: XUNG ĐỘT giữa schemas tại context hiện tại

     3 loại xung đột gây đau:

     Loại 1 — 2 schemas CÙNG context, KHÁC hướng:
       "Muốn ăn" + "muốn giảm cân" → CẢ 2 dương riêng → xung đột CÙNG LÚC
       → Ăn = guilt. Không ăn = thèm. CẢ 2 lựa chọn đều đau.
       → = Đau từ CONFLICT, không từ schema "xấu"

     Loại 2 — Schema ĐÚNG context CŨ, SAI context MỚI (OUTDATED):
       "Tiết kiệm từng đồng" — gia đình TỪNG nghèo → schema BẢO VỆ body ✅
       → Lớn lên, lương ổn → VẪN tiết kiệm cực đoan → không dám ăn ngon, du lịch
       → Schema "tiết kiệm" ĐÚNG khi nghèo → OUTDATED khi đã ổn định
       → = Schema KHÔNG sai → context ĐÃ ĐỔI → schema chưa UPDATE
       → = "Outdated" không phải "âm" — từng rất tốt, giờ lệch context

     Loại 3 — NHIỀU schemas ĐÚNG riêng, TỔNG THỂ xung đột:
       "Career" + "family" + "self-care" + "social" = TẤT CẢ dương
       → NHƯNG: 24h KHÔNG đủ cho tất cả → PHẢI chọn → mất cái nào = đau
       → Không schema nào sai → chỉ KHÔNG ĐỦ resource cho tất cả
       → = "Đời phức tạp" = nhiều drives dương CẠNH TRANH resource hữu hạn

   CƠ CHẾ ĐAU — Vector Conflict:
     Mọi schema PUSH body theo hướng riêng:
       Schema A: +5 hướng TRÁI
       Schema B: +3 hướng PHẢI
       → Body chỉ đi ĐƯỢC 1 hướng → PFC phải chọn
       → Schema bị chặn VẪN CHẠY → tốn energy → đau
       → ĐAU ∝ |force_A − force_B| khi NGƯỢC hướng
       → ĐAU CỰC ĐẠI khi 2 forces GẦN BẰNG NHAU (indecision, paralysis)
       → ĐAU GIẢM khi 1 force THẮNG RÕ (dù phải sacrifice cái kia)
       → "Quyết định xong DÙ SAI cũng nhẹ hơn KHÔNG quyết định"

   Predictive power: ★★★★☆ (CAO) — reframe: predict CONFLICT PATTERN
     → Nhiều schemas outdated → nhiều xung đột → predict anxiety, avoidance
     → Schemas aligned trong context → predict: initiative, flow, wellbeing
     → "Hạnh phúc" = schemas ALIGNED + context MATCH → coherence HIGH
     → "Đau" = schemas CONFLICT + context MISMATCH → coherence LOW

   IMPLICATIONS cho therapy:
     → KHÔNG "fix schema xấu" (không có schema xấu)
     → MÀ: "resolve XUNG ĐỘT" hoặc "UPDATE schema cho context MỚI"
     → Hoặc: "change CONTEXT" để match schemas hiện có
     → Hoặc: "build BRIDGE schema" (1 schema linh hoạt cho nhiều contexts)
     → = Reframe hoàn toàn: không ai "hỏng" → chỉ "chưa aligned"

   ⚠️ VẪN DÙNG "âm/dương" trong framework để ĐƠN GIẢN HÓA khi cần:
      "Schema âm" = shorthand cho "schema XUNG ĐỘT trong context hiện tại"
      "Schema dương" = shorthand cho "schema ALIGNED trong context hiện tại"
      → Biết rõ: bản chất = conflict/aligned → nhưng viết gọn "âm/dương" cho nhanh

   ⚠️ SCHEMA SÂU: buộc phải TRADE-OFF giữa vô thức vs ý thức:
      Schema surface (L1-L2): PFC switch linh hoạt → nhiều schemas ok
      Schema sâu (L4-L5): BODY EMBEDDED → chỉ 1 deep-state tại 1 lúc
      → Body chỉ có 1 (cortisol không vừa cao vừa thấp, vai không vừa gồng vừa thả)
      → = KHÔNG THỂ tối ưu maxsetting CẢ vô thức lẫn ý thức

      2 chiến lược, mỗi cái có trade-off:

      Strategy A — "Vô thức maxsetting" (1 schema sâu thống nhất):
        → 1 deep schema → body ỔN ĐỊNH → energy cho DEPTH
        → Ưu: sâu, authentic, tiết kiệm, body nhẹ
        → Nhược: ít linh hoạt, miss context không match
        → Phù hợp: vmPFC mạnh, ACC mạnh, người cần depth > breadth

      Strategy B — "Ý thức maxsetting" (2-3 schemas sâu, PFC switch):
        → PFC FORCE switch schema sâu per context
        → Ưu: linh hoạt, tận dụng nhiều context, đa năng
        → Nhược: PFC drain, body toggle mệt, identity risk, nông hơn A
        → Phù hợp: dlPFC mạnh, mPFC mạnh, người cần breadth > depth

      → Giới hạn não bộ: KHÔNG THỂ cả 2 max → phải chọn → tùy hardware profile
      → Không có "tối ưu chung" — chỉ có "tối ưu cho MÌNH"

   ⚠️ CƠ CHẾ GỐC: Vô thức KHÔNG CÓ nút switch:
      Vô thức chạy TẤT CẢ schemas đã train — không tắt được.
      PFC chỉ có thể CHẶN output, KHÔNG THỂ TẮT schema.

      Khi 2 schemas sâu XUNG ĐỘT:
        Schema A: vô thức CHẠY (tốn energy)
        Schema B: vô thức CHẠY (tốn energy)
        PFC: CHẶN 1 cái (tốn energy THÊM)
        → 3 hệ thống TỐN energy → net output chỉ 1 schema → LÃNG PHÍ × 2
        → = CPU chạy 100% nhưng 2 processes FIGHT nhau → output thấp

      Giải thích:
        "Mệt dù không làm gì" = schemas conflict NGẦM, PFC chặn LIÊN TỤC
        "Depression mệt nằm cả ngày" = vô thức VẪN chạy schemas conflict
        "Burnout mệt dù đã nghỉ" = schema "phải productive" VẪN CHẠY + PFC cố relax
        → KHÔNG phải "nghỉ không đúng cách" → mà "vô thức KHÔNG NGHỈ"

      → Não DESIGNED cho 1 luồng schema thống nhất (100,000 năm evolution)
      → Hiện đại: nhiều context xung đột → ép multi-schema → stress
      → Giải pháp bền vững: BUILD schema bridge (1 schema cho nhiều contexts)
        thay vì MAINTAIN nhiều schemas sâu xung đột

   ⚠️ HƯỚNG CHAIN phụ thuộc IMAGINATION MODALITY:
      Verbal dominant → chain DỌC (sequential, within-domain) → specialist
      Somatic dominant → chain NGANG (pattern match, cross-domain) → improviser
      Mixed/balanced → T-shaped (sâu 1 + rộng vài)
      → Modality = hardware tendency → school train verbal → majority = dọc
      → Chi tiết: Imagination-Analysis.md §9

③ ACTIVATION (always-on ↔ trigger-based):
   = Schema chạy KHI NÀO?

   Always-on:     "tôi là nam" → background, luôn active
   Frequent:      "phải productive" → most contexts, auto-activate
   Trigger-based: "gặp sếp → formal" → chỉ active khi trigger
   Dormant:       "kỹ năng xe đạp" → chỉ khi cần, compiled trong BG

   Predictive power: ★★★★☆ (CAO)
   → Always-on schemas = PERSISTENT influence → predict daily patterns
   → Trigger schemas = SITUATIONAL → predict specific situations
   → Biết schemas nào always-on → biết "người này CĂN BẢN thế nào"
```

### 1.3 Schema trong không gian 3 trục

```
           DEEP
            ↑
            │   "tôi vô giá trị"
            │         ●(âm, always-on)
            │
            │              "phải productive"
            │                   ●(âm, always-on)
            │
            │   "thế giới an toàn"
            │         ◆(dương, always-on)
            │
     ÂM ────┼──────────────── DƯƠNG ──→ VALENCE
            │
            │   "gặp sếp nói formal"
            │         ○(neutral, trigger)
            │
            │   "trời mưa mang ô"
            │         ○(neutral, trigger)
            ↓
         SURFACE

  ● = always-on, âm    → NGUY HIỂM NHẤT (persistent negative)
  ◆ = always-on, dương → TỐT NHẤT (persistent positive)
  ○ = trigger-based     → TRUNG TÍNH (situational)

  VÙNG NGUY HIỂM: Deep × Âm × Always-on (góc trên-trái, ●)
    → Persistent negative influence across ALL contexts
    → Ví dụ: "tôi vô giá trị" → mọi thứ filtered qua lens này
    → = Target #1 cho therapy/self-improvement

  VÙNG TỐT NHẤT: Deep × Dương × Always-on (góc trên-phải, ◆)
    → Persistent positive influence across ALL contexts
    → Ví dụ: "thế giới an toàn, tôi có giá trị" → resilience
    → = Mục tiêu build/maintain

  VÙNG TRUNG TÍNH: Surface × any × Trigger (dưới, ○)
    → Functional, practical, ít ảnh hưởng tổng thể
    → = Đa số schemas hàng ngày nằm ở đây
```

### 1.4 Năm Trục Bổ Sung (cho phân tích sâu hơn — ~95% understanding)

```
④ CONSCIOUSNESS (biết → không biết):
   Conscious:   "tôi biết tôi sợ rắn" → articulate được
   Unconscious: "không biết sao ghét commitment" → không articulate
   → Useful cho therapy: unconscious schema = fix target
   → "Biết nhưng không làm" = conscious schema ≠ unconscious schema

⑤ CHANNEL (Experience → Connection):
   Experience-oriented: "đẹp quan trọng" → serve opioid
   Connection-oriented: "gia đình trên hết" → serve oxytocin
   Both: "chia sẻ bữa ăn với người thân" → serve cả 2
   → Predict LOẠI hành vi (seek beauty vs seek people)

⑥ SOURCE (internal → external):
   Internal: "tôi thấy vậy" → tự suy luận
   External: "mọi người nói vậy" → learned/culture
   → Predict flexibility (internal dễ đổi vì "của mình")
   → ĐÃ CÓ trong Mô Hình Vuông

⑦ DOMAIN attachment (attached → floating):
   Attached: "tôi giỏi code" → gắn domain cụ thể
   Floating: "tôi giỏi" → không gắn domain → vague
   Cross:    "hệ thống cần feedback" → apply nhiều domains
   → Floating schemas = unstable (không verify được)
   → Attached schemas = testable (domain confirm/deny)
   → Cross schemas = L4 meta-schema (giá trị cao nhất)

⑧ VÙNG NÃO dominant (processing):
   BG-dominant:       habit (compiled, automatic)
   Amygdala-dominant: threat/safety (fast, emotional)
   DMN-dominant:      identity (self-referential)
   Temporal-dominant: knowledge (semantic, factual)
   PFC-dependent:     planning (deliberate, effortful)
   → Useful cho treatment match: fix ở ĐÚNG vùng não
   → CBT → PFC/Temporal. Exposure → Amygdala. Habit change → BG.
```

### 1.5 Ví dụ: Profile 1 người qua 3 trục core

```
Giả sử phân tích 1 CEO:

  DEEP × ÂM × ALWAYS-ON:
    "Dừng lại = thất bại" → drive mãn tính, burnout risk
    "Phải hơn đối thủ" → competitive anxiety
    → Predict: workaholism, khó relax, so sánh liên tục

  DEEP × DƯƠNG × ALWAYS-ON:
    "Tôi có thể vượt qua mọi thứ" → resilience, self-efficacy
    → Predict: bounce back từ failure, initiative cao

  MID × ÂM × TRIGGER:
    "Bị chỉ trích → phản biện ngay" → defense khi challenged
    → Predict: defensive trong meetings, khó nhận feedback

  → NET: dương schemas MẠNH (self-efficacy) nhưng ÂM schemas CŨNG mạnh (competitive)
  → = Drive CAO + Burnout risk CAO → cần Lớp 1 maintenance
  → = Threshold composite: hardware vừa + schema_pressure CAO → threshold observed CAO
```

---

## 2. Domain Architecture — Cấu Trúc "Lãnh Thổ"

### 2.1 Trục gom nhóm Domain

```
TRỤC A: OBJECTIVITY (khách quan → chủ quan)
  = Domain này VERIFY được cỡ nào?

  Objective:       Vật lý, Hóa, Toán → test = cùng kết quả
  Intersubjective: Xã hội, Kinh tế, Luật → đồng thuận nhưng CÓ THỂ đổi
  Subjective:      Nghệ thuật, Trải nghiệm → cá nhân, không verify cho người khác

  Impact:
    Objective → schema ĐÚNG/SAI rõ → feedback nhanh → learn nhanh
    Subjective → schema "đúng cho tôi" → feedback mờ → learn chậm
    → Tại sao science TIẾN NHANH, art TIẾN CHẬM (khác feedback clarity)

TRỤC B: SCOPE (hẹp → rộng → meta)
  = Domain này COVER bao nhiêu?

  Narrow:  "cách nấu phở" → 1 skill cụ thể
  Medium:  "ẩm thực Việt Nam" → nhiều skills liên quan
  Broad:   "food science" → cross nhiều cuisine + chemistry
  Meta:    "cách học bất kỳ skill nào" → domain VỀ domains

  Impact:
    Narrow expert = deep nhưng limited (thợ)
    Meta expert = shallow mỗi cái nhưng CROSS (framework builder)
    → Framework này = meta-domain ("domain about human behavior")

TRỤC C: STABILITY (ổn định → thay đổi)
  = Domain này đổi NHANH cỡ nào?

  Eternal:   Vật lý, Toán → F=ma vẫn đúng sau 300 năm
  Stable:    Sinh học, Y học → đổi chậm (thập kỷ)
  Dynamic:   Công nghệ, Thị trường → đổi nhanh (năm)
  Volatile:  Trend, MXH, Thời trang → đổi cực nhanh (tuần-tháng)

  Impact:
    Schema cho eternal domain → build 1 lần, dùng mãi
    Schema cho volatile domain → update LIÊN TỤC → tốn resource
    → Đầu tư learn eternal domain = ROI dài hạn CAO NHẤT
```

### 2.2 Domain Clusters — 6 nhóm chính

```
CLUSTER 1: NATURAL (tự nhiên, objective)
  Vật lý · Hóa · Sinh · Toán · Logic
  Properties: Eternal-Stable · Objective · Verify dễ
  Schema quality: đúng/sai RÕ RÀNG
  Learning: build → test vs domain → clear feedback → improve

CLUSTER 2: HUMAN (con người, intersubjective)
  Tâm lý · Xã hội · Kinh tế · Chính trị · Luật · Giáo dục
  Properties: Stable-Dynamic · Intersubjective · Verify vừa
  Schema quality: "đúng PHẦN NÀO" + context-dependent
  Learning: build → test → feedback MỜ → slower improve

CLUSTER 3: APPLIED (ứng dụng, mix)
  Engineering · Y khoa · Lập trình · Kiến trúc · Nông nghiệp
  Properties: Dynamic · Mix objective + intersubjective
  Schema quality: "works or doesn't" (pragmatic)
  = GIÁ TRỊ THỰC TIỄN CAO NHẤT — domain "làm được việc"

CLUSTER 4: CREATIVE (sáng tạo, subjective)
  Nghệ thuật · Âm nhạc · Văn học · Design · Game
  Properties: Dynamic-Volatile · Subjective · Verify khó
  Schema quality: "tôi thấy đẹp" ≠ "bạn thấy đẹp"
  Learning: build → test vs AUDIENCE response → feedback chậm + noisy

CLUSTER 5: META (domain về domains)
  Triết học · Nhận thức luận · Systems thinking · Framework building
  Properties: Eternal (nếu đúng) · Cross mọi cluster
  Schema quality: "cách mọi thứ hoạt động ở mức tổng quát"
  = HIẾM NGƯỜI nhưng HIGH IMPACT
  = Framework này = Cluster 5 sản phẩm

CLUSTER 6: PERSONAL (cá nhân)
  Relationship · Parenting · Self-care · Finance cá nhân
  Properties: Stable nhưng PERSONAL (mỗi người khác)
  Schema quality: "cách TÔI sống" (domain riêng)
  = Domain DÙNG NHIỀU NHẤT mà ít người coi là "domain"
  = Thường learn bằng trial-and-error (không ai dạy systematic)
```

### 2.3 Domain = Graph, không phải Tree

```
Domain KHÔNG xếp hierarchical đơn giản → là GRAPH (mạng lưới):

  Nodes = domain cụ thể
  Edges = liên quan (chia sẻ concepts, methods, hoặc subject matter)

  HUB NODES (liên quan NHIỀU domains):
    Toán:         foundation cho Physics, CS, Economics, Engineering,...
    Vật lý:       foundation cho Chemistry, Engineering, Cosmology,...
    Logic:        foundation cho Math, CS, Philosophy, Law,...
    Psychology:   liên quan Neuroscience, Education, Marketing, Game Design,...

    → HUBs = domains có TRANSFER VALUE cao nhất
    → Learn hub → apply ở NHIỀU domain khác → ROI cao

  BRIDGE NODES (nối 2+ clusters):
    Bioinformatics = Biology ∩ CS
    Behavioral Economics = Psychology ∩ Economics
    Game Design = Psychology ∩ Art ∩ CS
    Framework này = Psychology ∩ Neuroscience ∩ Philosophy ∩ Game Design

    → BRIDGES = nơi INNOVATION xảy ra
    → Cross-domain thinker = sống ở bridges → hiếm + valuable
    → Einstein: Physics ↔ Philosophy bridge
    → Framework author: Game Design ↔ Psychology ↔ Neuroscience bridge
```

---

## 3. Schema × Domain — Cách Gắn Nhau

### 3.1 Ba loại gắn kết

```
TYPE 1: Schema IN domain (phổ biến nhất)
  "Python dùng indentation" IN domain "Programming"
  = Schema CHỈ có nghĩa TRONG domain đó
  = Domain thay đổi/biến mất → schema mất giá trị
  → Đa số L1-L2 schemas thuộc loại này

TYPE 2: Schema ACROSS domains (cross-domain transfer)
  "Hệ thống phải có feedback loop" ACROSS Engineering + Biology + Management
  = Schema ĐÚNG ở NHIỀU domains (pattern phổ quát)
  = = L4 meta-schema — giá trị CAO vì transferable
  = Framework building = TẬP HỢP type 2 schemas

TYPE 3: Schema ABOUT domain (meta)
  "Domain vật lý = objective, verify được" ABOUT Physics
  = Schema VỀ domain, không phải TRONG domain
  = Metacognition: "tôi biết domain này hoạt động thế nào"
  = Cluster 5 (Meta Domains) chuyên sản xuất type 3
```

### 3.2 Schema Quality = Domain Match

```
Schema CHÍNH XÁC khi MATCH domain:
  "Nước sôi ở 100°C" × Physics = MATCH ✅ → schema tốt
  "Nước sôi ở 50°C" × Physics = MISMATCH ❌ → schema sai

Schema KHÔNG GẮN domain = ungrounded:
  "Tôi giỏi" (không specify domain nào) → vague, không test được
  "Tôi giỏi code" (gắn domain Programming) → test được → grounded

→ Schema grounded (gắn domain + test) = KNOWLEDGE
→ Schema ungrounded (không gắn hoặc chưa test) = BELIEF
→ Upgrade path: belief → attach domain → test → knowledge (hoặc discard)
→ Framework: started as belief → đang test vs domain → dần thành knowledge (nếu match)
```

### 3.3 Domain thay đổi → Schema impact

```
Domain STABLE (vật lý): schema build 1 lần → dùng mãi
  → Invest learn physics = HIGH long-term ROI

Domain DYNAMIC (tech): schema cần update liên tục
  → Invest learn specific framework → MID ROI (sẽ outdated)
  → Invest learn META-skills (cách học) → HIGH ROI (transferable)

Domain DIES (COBOL, Flash): schema MẤT GIÁ TRỊ hoàn toàn
  → Expert domain chết = identity crisis ("tôi biết cái gì giờ?")
  → Type 2 schemas (cross-domain) VẪN CÒN giá trị → resilient
  → → Dạy META-SKILLS > dạy specific domain = future-proof
```

---

## 4. Ứng Dụng: Map Người Vào Schema × Domain

```
Method:
  1. Identify DEEP × ÂM × ALWAYS-ON schemas (nguy hiểm nhất)
  2. Identify DEEP × DƯƠNG × ALWAYS-ON schemas (strength)
  3. Map schemas vào domains (attached? floating? cross?)
  4. Check domain stability (eternal? volatile?)
  5. Check schema-domain MATCH (grounded? tested?)

Output:
  → Predict behavior patterns (từ deep always-on schemas)
  → Predict strengths + risks (từ valence ratio)
  → Predict career match (từ schema × domain mapping)
  → Predict growth path (từ domain stability + cross-domain potential)
```

---

## 5. Schema Depth = Body Adaptation — Tại Sao Lớp Sâu Khó Sửa

### 5.1 Hai lý do KHÁC NHAU

```
LÝ DO 1: PFC không REACH (cognitive inaccessibility)
  → L5 schema: unconscious → PFC không thấy → không sửa được
  → = ĐÚNG nhưng chỉ 1 phần

LÝ DO 2: CƠ THỂ ĐÃ ADAPT (somatic embedding) — QUAN TRỌNG HƠN
  → Schema sâu KHÔNG CHỈ "não nghĩ" → ĐÃ EMBED vào CƠ THỂ:
    Cortisol baseline SHIFT (tuyến thượng thận adapt)
    Muscle tension PATTERNS (vai gồng, hàm nghiến — mãn tính)
    Gut microbiome THAY ĐỔI (stress → gut flora khác → mood khác)
    Immune system THAY ĐỔI (chronic stress → inflammation)
    HRV (Heart Rate Variability) GIẢM (stress mãn tính)
    Sleep architecture THAY ĐỔI (cortisol → shallow sleep → less REM)

  → PFC nói "tôi ok rồi" (verbal, surface fix)
  → Body NÓI "KHÔNG, tôi VẪN stress" (somatic, deep VẪN CÒN)
  → Body THẮNG vì body = ground truth (Lớp 1 Source)
  → = "Biết nhưng không thay đổi" = verbal updated, body CHƯA
```

### 5.2 Hình thành schema sâu = quá trình body adapt

```
Ví dụ: Công việc chán → burnout trajectory

  Tháng 1:  "Chán, nhưng ok" → cortisol nhẹ → body adapt nhẹ
  Tháng 6:  "Mệt mỗi sáng" → cortisol tăng → vai gồng, ngủ kém
  Năm 1:    "Cáu gắt" → cortisol baseline ĐÃ SHIFT → body coi stress = "bình thường mới"
  Năm 3:    "Kiệt sức" → body TOÀN BỘ adapt theo stress → dù NGHỈ VIỆC body KHÔNG reset ngay

  → Schema sâu ≠ "thought pattern stuck"
  → Schema sâu = BODY ADAPTATION tích lũy
  → Sửa thought (PFC) → surface fix
  → Sửa body → deep fix (nhưng chậm — body adapt chậm cả 2 chiều)
```

### 5.3 Tốc độ thay đổi theo lớp — Ước lượng

```
Lớp schema    │ Tốc độ đổi │ Cần gì để đổi         │ Tiền/hoàn cảnh fix?
══════════════╪════════════╪═══════════════════════╪════════════════════
L1 Surface    │ Ngày       │ Đổi context            │ ✅ Ngay lập tức
L2 Domain     │ Tuần-tháng │ Repeated experience    │ ✅ Vài tuần
L3 Goals      │ Tháng      │ Sustained change       │ ⚠️ Partial
L4 Rules      │ Tháng-năm  │ Therapy + experience   │ ❌ Tiền không fix
L5 Identity   │ Năm+       │ Body-level change      │ ❌ Tiền KHÔNG fix
Body adapt    │ Tháng-năm  │ Body-level intervention│ ❌ Cần thời gian + practice

Ví dụ "trúng số" kiểm chứng:
  L1: ĐỔI NGAY ("mai không phải đi làm") ✅
  L2-L3: Vài tuần-tháng ("tôi là người giàu" dần tin) ⚠️
  L4-L5: KHÔNG ĐỔI ("tôi vô giá trị" VẪN CÒN dù giàu) ❌
  Body: cortisol baseline VẪN CAO (5 năm stress → không reset vì trúng số) ❌

  → ~70% lottery winners quay về happiness baseline trong 1-2 năm (research)
  → Vì: L4-L5 + body KHÔNG đổi → surface euphoria fades → deep schema PULL BACK
```

### 5.4 Sửa đúng lớp = sửa đúng MODALITY

```
Surface fix (L1-L3) — nhanh, tạm thời:
  Lời động viên (verbal):     PFC nhận → surface update → TẠM giảm áp lực
  Tình cảm người thân (oxy):  Lớp 1 Connection feed → DUY TRÌ nhưng không FIX gốc
  Đổi hoàn cảnh (context):    L1-L2 switch → MỚI nhưng body VẪN mang schema cũ theo
  Tiền (resource):             Giảm financial stress → L2-L3 → body stress KHÁC vẫn còn
  → TẤT CẢ = surface → body pull QUAY LẠI sau thời gian

Deep fix (L4-L5 + body) — chậm, bền vững:
  Exercise:              cortisol BURN daily → body RESET dần → FOUNDATION
  Sleep đủ:              consolidation + body repair → schema reprocess
  Nutrition:             gut-brain axis → mood baseline shift
  Somatic therapy:       body trực tiếp thả (muscle, breathing, touch)
                         → Body thả → schema sâu TỰ UPDATE (body = ground truth)
  EMDR:                  reprocess body memory → trauma schema loosen
  Psychedelic-assisted:  "flash firmware" tạm → window rewrite L5
                         (window NGẮN → cần therapeutic support)

  → Fix BODY trước → body calm → PFC available → therapy hiệu quả hơn
  → Fix BODY + therapy CÙNG LÚC → NHANH NHẤT
  → Fix CHỈ therapy (verbal) mà body CHƯA fix → chậm, relapse cao

⚠️ INSIGHT:
  "Tại sao cứ lặp đi lặp lại vấn đề cũ?"
  → Vì: surface đã fix (L1-L3) → body CHƯA fix → body PULL surface quay lại
  → Giải pháp: fix BODY (exercise, sleep, somatic) → rồi mới fix thought (therapy, coaching)
  → Thứ tự: Body → Mind, KHÔNG phải Mind → Body
  → Giống: sửa NỀN MÓNG trước, sơn TƯỜNG sau
```

### 5.5 Context thay đổi vs Schema thay đổi — Phân biệt

```
Mọi người TRÔNG NHƯ thay đổi khi đổi context:
  Ở công ty: formal, kiềm chế
  Ở nhà: thoải mái, cáu gắt

THỰC RA: schema sâu KHÔNG đổi → chỉ OUTPUT khác:
  L5 "sợ bị đánh giá" = active Ở MỌI NƠI
    Công ty: suppress cáu gắt (PFC high) → formal = DEFENSE
    Nhà: release cáu gắt (PFC low) → cáu = ACCUMULATED TENSION
    → CẢ HAI driven bởi CÙNG L5 schema

STRESS TEST xác nhận:
  PFC mạnh (ngủ đủ, khỏe): giữ surface schema TỐT → "chuyên nghiệp"
  PFC yếu (mệt, stress, say): surface schema MỎNG → schema SÂU LỘ RA
  → "Khi mệt thấy con người THẬT" = PFC offline → body/deep schema take over
  → = Framework predict: PFC arbitrator mệt → schema mạnh nhất (sâu nhất) win

"Linh hoạt ở mọi context" — 2 loại:
  Type A: L5 "thế giới an toàn" → ở đâu cũng OK → linh hoạt từ BÌNH AN
  Type B: L5 "phải làm hài lòng" → ở đâu cũng adapt → linh hoạt từ LO ÂU
  Test: một mình, an toàn → A: vẫn thoải mái. B: bồn chồn.
  → TRÔNG GIỐNG ở surface → KHÁC HOÀN TOÀN ở deep
```

---

## 5. Body Baseline State — Schema Sâu Nhất, Chỉ Có 1

> MỌI schema layers (L1-L5) build TRÊN 1 nền tảng duy nhất: body baseline state.
> Đây là ground truth — PFC, verbal, logic đều THAM CHIẾU về đây.
> Fix body baseline → mọi schemas tự adjust. Fix schemas mà không fix body → relapse.

### 5.1 Định Nghĩa

```
Body Baseline State = trạng thái TỔNG THỂ cơ thể khi NGHỈ (không stimulus đặc biệt):

  Cortisol baseline:     mức stress nền (cao = luôn alert, thấp = relaxed)
  Opioid tone:           mức pleasure nền (cao = content, thấp = numb)
  Oxytocin level:        mức connection nền (cao = warm, thấp = isolated)
  Muscle tension:        pattern tension nền (vai gồng? hàm nghiến? thả lỏng?)
  Gut state:             tiêu hóa nền (bình thường? IBS? butterfly?)
  HRV:                   heart rate variability (cao = flexible, thấp = rigid)
  Sleep architecture:    chất lượng giấc ngủ nền (deep sleep đủ? REM đủ?)
  Immune baseline:       mức viêm nền (inflammation chronic?)

  = "Khi không có gì xảy ra, cơ thể TÔI feel thế nào?"
  = TẤT CẢ combine thành 1 TRẠNG THÁI DUY NHẤT
```

### 5.2 Tại Sao Chỉ Có 1?

```
1. Body CHỈ CÓ 1:
   → 1 hệ cortisol → 1 baseline level (không thể vừa cao vừa thấp)
   → 1 hệ opioid → 1 baseline tone
   → 1 hệ muscle → 1 tension pattern (vai không thể VỪA gồng VỪA thả)
   → = TOÀN BỘ combine → 1 state duy nhất tại mỗi thời điểm

2. MỌI schema THAM CHIẾU về cùng 1 baseline:
   → "Mở lòng ở công ty?" → body check baseline: "an toàn không?"
   → "Sợ giao tiếp?" → body check baseline: "thế giới nguy hiểm?"
   → CẢ HAI hỏi CÙNG 1 body → CÙNG answer → CÙNG ground truth

3. L1-L5 = VERBAL LABELS cho body baseline:
   → Body baseline: tense + guarded
   → L5 LABEL: "không ai đáng tin" (verbal interpretation)
   → L4 LABEL: "phải tự lực" (rule from interpretation)
   → L3 LABEL: "career = safety" (goal from rule)
   → → Labels có thể SAI (misinterpret) → nhưng body baseline = DATA gốc
```

### 5.3 Kiểm Chứng

```
CASE 1: Đổi context nhẹ (đi làm → về nhà)
  → Hành vi ĐỔI (formal → casual)
  → Body baseline: KHÔNG ĐỔI (người tense → VẪN tense ở cả 2)
  → ✅ 1 baseline, không đổi theo context nhẹ

CASE 2: Đổi context mạnh (chuyển thành phố, đổi cuộc sống)
  → Hành vi ĐỔI MẠNH
  → Body baseline: ĐỔI CHẬM (tháng → năm)
  → Tháng đầu: mang baseline CŨ theo → "đi đâu cũng mang theo mình"
  → 6+ tháng: baseline BẮT ĐẦU shift (body adapt môi trường mới)
  → ✅ 1 baseline, đổi CHẬM, không NGAY

CASE 3: Trauma đột ngột
  → Body baseline CÓ THỂ rewrite NGAY (hướng xấu):
    Trước: warm + safe → Sau: tense + hypervigilant
  → ✅ VẪN 1 baseline, chỉ bị REWRITE nhanh bởi extreme event

CASE 4: Bệnh lý thần kinh (bipolar)
  → Baseline SWING giữa extremes (mania ↔ depression)
  → TRÔNG NHƯ 2 baselines → thực ra 1 baseline ĐANG SWING
  → = VẪN 1 tại mỗi thời điểm → chỉ KHÔNG ỔN ĐỊNH
  → ✅ Bệnh lý = 1 baseline bị unstable, VẪN 1
```

### 5.4 Body Baseline Được Hình Thành Từ Đâu?

```
Hardware (gen): ~30-50%
  → Set RANGE (phạm vi baseline CÓ THỂ nằm trong)
  → Ví dụ: gen → cortisol range [2-8] → baseline NẰM TRONG khoảng này
  → KHÔNG vượt range → nhưng VỊ TRÍ trong range = experience quyết định

Early life (0-7 tuổi): ~30-40%
  → Set POSITION đầu tiên trong range
  → Tuổi thơ safe → baseline nằm ở THẤP trong range (relaxed)
  → Tuổi thơ trauma → baseline nằm ở CAO trong range (tense)
  → → Tại sao tuổi thơ QUAN TRỌNG NHẤT: set body baseline LẦN ĐẦU
  → → Và: 0-7 body CỰC malleable → position set RẤT sâu

Life experience (7+ tuổi): ~20-30%
  → SHIFT position chậm theo experience tích lũy
  → Môi trường safe dài → baseline shift XUỐNG (relaxed hơn)
  → Stress mãn tính → baseline shift LÊN (tense hơn)
  → → CÓ THỂ shift → nhưng CHẬM (tháng → năm)
  → → VÀ: bị giới hạn bởi range (gen set ceiling)
```

### 5.5 Implications

```
1. "Fix schema" THỰC RA = fix body baseline:
   → CBT fix verbal labels (L3-L5) → TẠM → body baseline PULL ngược về cũ
   → Somatic therapy fix body → L3-L5 TỰ UPDATE → BỀN
   → Exercise + sleep + nutrition fix body → FOUNDATIONAL
   → → Body-Needs Nhóm 1 = fix body baseline = fix GỐC mọi thứ

2. "Schema khó sửa" = body baseline khó shift:
   → Body baseline = TOÀN BỘ cơ thể adapt → shift = toàn bộ re-adapt → CHẬM
   → Verbal shift = NHANH (đổi label dễ)
   → Body shift = CHẬM (cortisol recalibrate, muscle retrain, gut rebuild)
   → → "Biết rồi mà vẫn khổ" = verbal ĐÃ shift, body CHƯA

3. Fix 1 body baseline → mọi schemas tự adjust:
   → Không cần fix 100 schemas riêng lẻ → fix NỀN → 100 schemas reinterpret
   → Body baseline shift relaxed → L5 tự: "à, thế giới ok hơn tôi tưởng"
   → → KHÔNG ai "nói" L5 đổi → L5 TỰ đổi vì DATA gốc (body) đã đổi
   → = "Đổi nền → đổi cả bức tranh"

4. "Đi đâu cũng mang theo mình" = mang theo body baseline:
   → Context đổi → hành vi đổi → body baseline CHƯA đổi → cùng pattern
   → CHỈ KHI context mới DUY TRÌ ĐỦ LÂU → body DẦN recalibrate
   → → "Chữa lành" KHÔNG phải 1 event → là THỜI GIAN ĐỦ LÂU trong context tốt
   → → Tại sao "nghỉ phép 2 tuần" KHÔNG fix burnout: body cần THÁNG, không phải TUẦN

5. ĐÚNG MỌI NGƯỜI: bất kỳ ai cũng chỉ có 1 body baseline:
   → Người hạnh phúc: baseline warm + relaxed + open → schemas build trên nền tốt
   → Người khổ: baseline tense + guarded + alert → schemas build trên nền xấu
   → Cùng event → KHÁC body baseline → KHÁC schema interpretation → KHÁC hành vi
   → → "Tại sao 2 người cùng hoàn cảnh mà khác nhau?" = KHÁC body baseline
```

### 5.6 Suy Ngược Body Baseline — 3 Con Đường Diagnostic

> Body baseline KHÔNG nhìn thấy trực tiếp (unconscious + somatic).
> PFC không thấy. Verbal không mô tả được. Scan chưa đọc được chi tiết.
> → PHẢI suy ngược từ cái NHÌN THẤY ĐƯỢC.

```
CON ĐƯỜNG 1 — Quan sát HÀNH VI lớp ngoài (observable behaviors)

  Hành vi lặp lại = schema lớp ngoài = TRIỆU CHỨNG của baseline:

    "Luôn đồng ý với mọi người"
      → Schema: "conflict = nguy hiểm"
      → Baseline gợi ý: cortisol cao khi confrontation
      → = "Thế giới sẽ hại nếu tôi không comply"

    "Luôn làm việc, không dừng"
      → Schema: "dừng = mất giá trị"
      → Baseline gợi ý: opioid CHỈ từ achievement, cortisol khi idle
      → = "Giá trị tôi = output"

    "Luôn kiểm tra 3 lần"
      → Schema: "phải kiểm soát"
      → Baseline gợi ý: cortisol cao + hypervigilant
      → = "Thế giới không an toàn nếu không kiểm soát"

  Phương pháp:
    → Liệt kê 5+ patterns hành vi lặp lại CỦA 1 NGƯỜI
    → Cluster: patterns nào chỉ CÙNG HƯỚNG?
    → Cùng hướng = POINTER tới baseline
    → 1 pointer: có thể sai (1 hành vi → nhiều nguyên nhân)
    → 5 pointers cùng hướng: baseline GẦN CHẮC CHẮN
    → → Càng nhiều pointer consistent → estimate càng chính xác
```

```
CON ĐƯỜNG 2 — Quan sát MÔI TRƯỜNG + HARDWARE → predict baseline

  Biết INPUT → predict OUTPUT (baseline):

    MÔI TRƯỜNG tuổi thơ (quan trọng nhất — set baseline lần đầu):
      Bố mẹ yêu thương + consistent → predict: baseline relaxed, warm
      Bố mẹ nghiêm ngặt + conditional love → predict: baseline tense, performance-driven
      Bố mẹ bỏ bê / absent → predict: baseline isolated, self-reliant
      Bố mẹ conflict / violent → predict: baseline hypervigilant, guarded

    HARDWARE profile (nếu estimate được):
      ACC cao + môi trường conflict → predict: baseline CỰC tense (detect × amplify)
      ACC cao + môi trường safe → predict: baseline ok (detect nhưng không có gì detect)
      vmPFC cao + môi trường safe → predict: baseline warm (body feel safety rõ)
      vmPFC cao + môi trường toxic → predict: baseline ĐAU SÂU (body feel pain rõ)
      → = Cùng môi trường + KHÁC hardware → KHÁC baseline → KHÁC schema

    MÔI TRƯỜNG hiện tại:
      Stress mãn tính (công việc, tài chính) → baseline shift LÊN (tense hơn)
      Safe + supportive (partner tốt, công việc match) → baseline shift XUỐNG (relaxed hơn)
      → Baseline HIỆN TẠI = tuổi thơ set + hardware + hiện tại SHIFT

  → Cross-reference: môi trường + hardware → predict baseline → check vs hành vi
  → Consistent? → estimate MẠNH. Inconsistent? → cần thêm data.
```

```
CON ĐƯỜNG 3 — Tự nhận diện mâu thuẫn (hardest nhưng deepest)

  Tự THẤY hành vi lớp ngoài XUNG ĐỘT → suy ngược:

    "Tôi BIẾT nên mở lòng nhưng KHÔNG THỂ"
      → Verbal: "mở lòng tốt" ✅ (schema lớp ngoài ĐÃ update)
      → Body: "mở lòng = nguy hiểm" ❌ (baseline CHƯA shift)
      → XUNG ĐỘT này = POINTER trực tiếp tới baseline
      → = "Biết mà không làm" = baseline ≠ verbal → baseline = ground truth

  Tại sao KHÓ:
    → Body baseline = DEFAULT → "tôi luôn vậy" → không thấy bất thường
    → = Cá không thấy nước (baseline = nước, cá = schemas lớp ngoài)
    → Cần MIRROR: therapist, partner, bạn thân, framework, context MỚI
    → Context MỚI đặc biệt hữu ích: baseline LỘ RA khi context KHÁC
      → Du lịch: "ở nhà tôi ok, đi xa bỗng thấy... relaxed hơn?"
        → = Baseline ở nhà TENSE → nhưng chưa bao giờ biết vì = default

  Framework GIÚP:
    → Cho NGÔN NGỮ mô tả cái body feel:
      Trước: "tôi khó chịu gì đó" (mơ hồ)
      Sau: "baseline cortisol cao + muscle tension + L5 'thế giới nguy hiểm'"
    → Có ngôn ngữ → PFC CÓ THỂ hold → workspace MỞ → vô thức process
    → = Framework = BRIDGE giúp verbal REACH somatic data
```

```
QUY TRÌNH TỔNG HỢP — DIAGNOSTIC BODY BASELINE:

  BƯỚC 1: Thu thập OBSERVABLE data
    → 5+ hành vi lặp lại (patterns)
    → Môi trường tuổi thơ + hiện tại
    → Hardware profile estimate (PFC sub-regions, modality dominant)
    → Body signals hiện tại (mệt? đau? mất ngủ? tension? gut?)

  BƯỚC 2: Suy ngược BODY BASELINE
    → Từ patterns hành vi → "baseline CÓ THỂ là..."
    → Từ môi trường → "baseline CÓ THỂ HÌNH THÀNH vì..."
    → Từ body signals → "baseline ĐANG thể hiện qua..."
    → Cross-check 3 sources → consistent? → baseline estimate

  BƯỚC 3: Xác định MISMATCH
    → Baseline hiện tại vs Context cần cho cuộc sống hiện tại
    → "Baseline tense" vs "context công ty safe" = mismatch → đau mãn tính
    → → Xung đột schemas lớp ngoài = TRIỆU CHỨNG, baseline = BỆNH

  BƯỚC 4: Fix BASELINE (không fix từng schema riêng lẻ)
    → Nhóm 1 Body-Needs TRƯỚC: sleep, nutrition, exercise
      → Cortisol giảm → baseline shift DẦN
    → Nhóm 2 Connection: 1 người intimate (therapist, partner, friend)
      → Oxytocin tăng → baseline shift DẦN
    → Somatic therapy: body-level processing (EMDR, somatic experiencing)
      → Muscle/trauma release → baseline shift TRỰC TIẾP
    → Context tốt DUY TRÌ ĐỦ LÂU (tháng → năm)
      → Body recalibrate → baseline shift → schemas TỰ UPDATE
    → → KHÔNG fix verbal labels trước (CBT alone = tạm)
    → → Fix BODY trước → verbal TỰ update → BỀN

  BƯỚC 5: Verify — baseline ĐÃ shift chưa?
    → Hành vi THAY ĐỔI TỰ NHIÊN? (không ép, tự đổi)
    → Body signals GIẢM? (ngủ tốt hơn, ít đau, ít tension)
    → Reaction khác trong context CŨ? ("gặp bố mẹ KHÔNG tense nữa")
    → NẾU có → baseline ĐÃ shift → maintain
    → NẾU chưa → chưa đủ thời gian HOẶC fix chưa đúng → adjust

  ⚠️ Timeline THỰC TẾ:
    Verbal label đổi: ngày → tuần (CBT fast)
    Body baseline shift: tháng → năm (body slow)
    → → "Tại sao therapy lâu" = verbal đổi NHANH, body đổi CHẬM
    → → "Tại sao relapse" = verbal ĐÃ đổi, body CHƯA → body pull ngược
    → → "Khi nào xong" = khi body baseline ĐÃ shift + maintained ĐỦ LÂU
```

---

## 6. Câu Hỏi Mở

```
S1: Có bao nhiêu "universal" schemas (gần ĐÚNG cho MỌI NGƯỜI)?
    → "Sợ chết" universal? Hay cultural? Hay mix?
    → Nếu có universal schemas → framework PREDICT mọi người được?

S2: Schema DENSITY per domain — đo được không?
    → "Người này có BAO NHIÊU schemas trong domain X?"
    → Proxy: vocabulary size? Problem-solving speed? Chunking level?

S3: Cross-domain schemas — tìm được không?
    → Type 2 schemas = GIÁ TRỊ CAO NHẤT
    → Tìm bằng cách: so sánh PATTERNS across domains → thấy overlap?
    → Framework building = exactly this process

S4: Domain Graph — ai đã map?
    → Wikipedia = partial map (articles = nodes, links = edges)
    → Academic disciplines = formal taxonomy (nhưng incomplete)
    → CÓ THỂ: overlay schema atlas lên domain graph → "ai biết gì, ở mức nào"

S5: Schema × Domain × UD:
    → Mỗi schema-domain pair có UD riêng?
    → "Tôi giỏi code" (schema) × "Programming" (domain) → UD mastery
    → "Tôi kém code" (schema) × "Programming" (domain) → UD frustration
    → → UD = f(schema valence × domain relevance × activation level)
    → Cần formalize?
```

---

> *Schema Atlas — DRAFT*
> *"Schema = bản đồ. Domain = lãnh thổ. Schema sâu = body adaptation."*
> *3 trục core (Depth × Valence × Activation) = 80% predictive power.*
> *Sửa schema sâu = sửa CƠ THỂ. Body → Mind, không phải Mind → Body.*
