---
title: 00 — Tổng Quan Hệ Thống Chunk — Giới Thiệu Nhẹ + Kiến Trúc 3 Lớp
file: 00-Chunk-System-Sketch-VI.md
source: 00-Chunk-System-Sketch.md (bản gốc tiếng Anh)
phase: F1 foundation (file đầu tiên trong 3 file nền tảng, trước 01 PFC reframe + 02 Womb-Birth baseline)
parent: plan.md (F1 v3)
session: N+4a
scope: File định hướng nhẹ. Không phân tích mới. Tổng hợp kiến trúc 3 lớp + cách chia 4-folder mechanism + đóng góp từ các sub-folder đã drilled (N+1 H8, N+2 H9, N+3 H10). Định hướng reader trước khi vào 01 + 02 + body-input arcs.
status: DRAFT N+4a P1 — sẵn sàng để user review
reading_order: ĐỌC TRƯỚC TIÊN trong chuỗi F1 sub-folder
language: Tiếng Việt primary + English technical terms
translation_note: Bản dịch tiếng Việt hoàn chỉnh. Giữ nguyên thuật ngữ kỹ thuật tiếng Anh, citation, tên file, parameter, emoji.
---

# 00 — Tổng Quan Hệ Thống Chunk

> **File này là ĐỊNH HƯỚNG**, không phải phân tích sâu. Mục đích: đưa reader vào F1 với mental model đầy đủ về kiến trúc 3 lớp (Body-Feedback L1 / Chunk System L2 / Feeling L3) + cách chia 4-folder mechanism + đóng góp từ N+1/N+2/N+3 đã drilled + sứ mệnh F1 v3. Nội dung sâu bắt đầu ở [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) và [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md).
>
> **Style**: Tiếng Việt primary + English technical terms. 🟢 Có bằng chứng nghiên cứu / 🟡 Suy luận framework / 🔴 Giả thuyết. "Imagine-Final" không viết tắt. Xưng hô "bạn-tôi".
>
> **Nguyên tắc meta của drill**: "Chậm mà chắc, không tiết kiệm bước nào."

---

## §0 — Tóm Tắt

Drill F1 Child-Chunk-Development hướng tới mục tiêu hình thức hóa **cơ chế compile chunk từ substrate** trong giai đoạn phát triển 0-24 tháng tuổi, thông qua 6 body-input arcs (visual / auditory / motor / interoceptive / social / verbal) và event-inference methodology (quan sát events → suy luận trạng thái chunks, không overclaim PFC developmental timeline). File này là file nền tảng đầu tiên trong cấu trúc 12 file — giới thiệu kiến trúc 3 lớp (Body-Feedback ✅ đã drilled / Chunk System 🎯 hiện tại / Feeling ⏳ tương lai), cách chia 4-folder mechanism của Chunk-Analysis (Child F1 / External F3 / Internal F4 / Master 99), 3 sub-folder đã drilled cung cấp bằng chứng substrate (Learning-Cycle H8, Agent H9, Body-Feedback H10), và sứ mệnh F1 v3 với PFC hardware reframe + đóng góp framework PFC-Inference Ladder. Không có phân tích mới ở file này — thuần tổng hợp, chỉ đường cho reader đến nội dung sâu ở 01-08.

---

## §1 — Bản Đồ Kiến Trúc 3 Lớp

### §1.1 — Tầm nhìn phân lớp của user (đã cam kết)

```
LỚP 3: HỆ THỐNG FEELING                                        ⏳ Tương lai
         ───────────────────────────────────────────
         Giao diện quan sát của PFC. Đọc các tín hiệu
         upstream tích hợp qua chunks. Gradient 7 lớp
         (Thô → Tích hợp → Nhận ra → Quan sát →
         Xác vị → Gán nhãn → Giải thích). Folder
         4-file đã hoàn thành tại Body-Base/Feeling/.

         CẦN: cơ chế phát triển cho sự xuất hiện Lớp 3-7.
         Đang chờ drill Chunk System để cung cấp.
         ───────────────────────────────────────────
LỚP 2: HỆ THỐNG CHUNK                                           🎯 Hiện tại
         ───────────────────────────────────────────
         Chunks = dữ liệu. Vô thức (~95%) + PFC (~5%) là
         các operator. 4 cơ chế compile: lặp lại (LTP)
         / đỉnh cảm xúc / multi-modal / sleep consolidation.
         Schemas = mạng chunks có purpose.

         CHIA thành 4 folder theo loại cơ chế:
         - F1 Child-Chunk-Development (substrate)  🎯 N+4
         - F3 Chunk-External-Development (+Language) ⏳ N+5-7
         - F4 Chunk-Internal-Processing            ⏳ N+8-9
         - 99-Master-Synthesis                     ⏳ N+10+
         ───────────────────────────────────────────
LỚP 1: BODY-FEEDBACK                                             ✅ Xong N+3
         ───────────────────────────────────────────
         Tín hiệu cơ thể thô. Sensors + insula + ACC
         tích hợp upstream. Lớp 1-2 của mô hình 7 lớp.
         Bất biến qua các giai đoạn phát triển (tín hiệu
         thô không đổi — cùng ghrelin, nociceptor, cortisol).
         5 điều kiện tiên quyết (H10) cho signal → feeling
         có ý thức.
         ───────────────────────────────────────────
```

### §1.2 — Tại sao thứ tự lớp quan trọng

Lớp 1 (Body-Feedback) cung cấp **nền tảng**. Không có body sensors kích hoạt → không có nguyên liệu thô để chunks hình thành. Body-Feedback-Draft N+3 đã drilled thiết lập: body-inputs adaptive baseline, lớp L0-L2 pre-PFC, 5 điều kiện tiên quyết cho signal → feeling có ý thức xuất hiện.

Lớp 2 (Chunk System) vận hành **trên** nền tảng Lớp 1. Chunks compile từ các pattern body-feedback lặp lại. Không có chunks → không có truy xuất, không có liên kết, không có dự đoán. F1-F4 drill Chunk System qua 4 loại cơ chế.

Lớp 3 (Feeling System) vận hành **trên** chunks Lớp 2. Chunks cho phép PFC gán nhãn + giao diện quan sát ở Lớp 3-7 của mô hình 7 lớp. Không có chunks Lớp 2 → Feeling System ở lại Lớp 3-4 mờ nhạt (phổ alexithymia). Feeling folder đã hoàn thành tại `Body-Base/Feeling/` — đang chờ drill chunk system để cung cấp cơ chế phát triển.

### §1.3 — Tại sao chia thành lớp thay vì xử lý như một thể thống nhất

Tinh chỉnh framework 2026-04: insight của user từ session Pattern-Match (`project_pattern_match_insights.md`) đã tách **Body-Feedback** (Lớp 1-2 thô, bất biến) khỏi **Feeling** (Lớp 3-7 giao diện quan sát PFC, có thể huấn luyện). Trước khi tách này, các trường hợp dissonance/reward lẫn lộn "tín hiệu cơ thể" với "feeling" — không thể giải thích alexithymia, trường hợp Van Gogh, hedonic adaptation, sự tồn tại của trauma.

Chunk System nằm **giữa** hai lớp này như cơ chế vận hành. Chunks cho phép Feeling Lớp 3-7 xuất hiện. Chunks tích lũy từ lặp lại Body-Feedback + đỉnh cảm xúc + multi-modal binding + sleep consolidation.

**Sứ mệnh drill F1**: hình thức hóa sự xuất hiện Lớp 2 từ substrate Lớp 1, qua developmental arc 0-24 tháng. Điều này hoàn thành cầu nối substrate mà Feeling folder cần.

**Cross-ref**: [Body-Feedback-Draft/01-Foundation.md §5](../Body-Feedback-Draft/01-Foundation.md) cho sự phân biệt kiến trúc body-feedback vs feeling + clarity gradient 7 lớp.

---

## §2 — Chunk Là Gì (Tóm Tắt)

### §2.1 — Định nghĩa cốt lõi (Schema/Chunk.md §1)

🟢 **Chunk = nhóm neurons đã wire together → fire thành 1 đơn vị** (Hebb 1949, Hebbian LTP).

```
CHƯA compiled: 3 nhóm riêng lẻ (visual + auditory + meaning)
              → PFC phải hold cả 3 → tốn 3 dimensions

ĐÃ compiled:   1 unit wired → fire 1 lần = biết hết
              → = "Chunk" = gói đã nén
              → Tốn 1 dimension
```

**Chunk vs Schema**:
- **Chunk** = nguyên tử (1 đơn vị, không có purpose riêng)
- **Schema** = phân tử (mạng chunks liên kết → có purpose/function)

**Chunk multi-modal** — trải rộng nhiều vùng vỏ não: VD chunk "mẹ" = mặt (visual) + giọng (auditory) + ôm (somatic) + ấm (emotional). Kích hoạt 1 phần (nghe giọng) → kéo cả chunk kích hoạt (nhớ mặt, nhớ ôm). 🟢 Distributed representations (Rumelhart & McClelland 1986).

### §2.2 — 4 cơ chế compile (Chunk.md §2)

🟡 **4 cách chunks được compile**:

| # | Cơ chế | Tốc độ | Ví dụ | Anchor nghiên cứu |
|---|---|---|---|---|
| ① | **Lặp lại (LTP)** | Chậm nhưng bền | Kích hoạt pattern 50+ lần → connections strengthen | 🟢 Bliss & Lømo 1973 |
| ② | **Đỉnh cảm xúc** | 1 lần đủ | Amygdala + NE → wire cực nhanh | 🟢 Brown & Kulik 1977 flashbulb |
| ③ | **Multi-modal binding** | Mạnh mỗi lượt | Visual + auditory + somatic + motor cùng fire | 🟡 Liên kết cross-cortex |
| ④ | **Sleep consolidation** | Offline | Hippocampus replay → strengthen hoặc prune | 🟢 Walker 2017 |

**Phát hiện dự kiến từ drill F1**: Infant chunks dùng cả 4 cơ chế song song, với phân bố khác nhau qua developmental arc:
- **0-3 tháng**: Sleep consolidation chiếm ưu thế (ngủ 16+ giờ/ngày)
- **3-12 tháng**: Multi-modal binding chiếm ưu thế (social smile, joint attention)
- **12-24 tháng**: Lặp lại + vocabulary spurt
- **Xuyên suốt**: Đỉnh cảm xúc đan xen (các khoảnh khắc flashbulb)

Drill home: [09-Event-Chunks-Inference-Matrix.md](09-Event-Chunks-Inference-Matrix.md) cho cross-tabulation.

### §2.3 — Vòng đời chunk (genesis → decay → reconsolidate, không xóa)

🟡 **Các giai đoạn vòng đời**:

1. **Genesis** — compile lần đầu từ 1 trong 4 cơ chế
2. **Consolidation** — sleep replay + re-exposure strengthen
3. **Connection** — chunks wire với các chunks khác → schemas xuất hiện
4. **Retrieval** — spreading activation kích hoạt chunk (Collins & Loftus 1975)
5. **Reconsolidation** — khi chunk được nhớ lại, tạm thời unstable → cửa sổ modify → re-compile (Nader 2000)
6. **Decay** — không dùng → retrieval path yếu → "quên" (Ebbinghaus 1885, savings in relearning)
7. **⚠️ Không xóa** — không có cơ chế unwire. Chunks chỉ strengthen/weaken/modify, không delete. "Bỏ thói cũ" = compile chunk mới đủ mạnh đè chunk cũ.

**Focus F1**: Giai đoạn 1-3 (genesis + consolidation + connection) trong developmental arc 0-24 tháng. Giai đoạn 4-7 phần lớn cross-cutting hoặc ngoài cửa sổ F1.

**Cross-ref**: [Schema/Chunk.md](../../Schema/Chunk.md) §1-§2 cho phần trình bày đầy đủ.

### §2.4 — Tách biệt Vô thức + PFC (Chunk.md §3)

🟡 Claim kiến trúc quan trọng:

> **Chunk = DỮ LIỆU. 2 operator làm việc với cùng database**:
> - **Vô thức = OPERATOR CHÍNH (~95%)** — compile, chạy schemas tự động, đánh giá qua body signals, xử lý nền
> - **PFC = OPERATOR PHỤ (~5%)** — tìm kiếm, giữ, định hướng, tạo (draft), chỉnh sửa — nhưng quyết định HƯỚNG

**Vô thức có thể**: phát hiện body state, compile patterns từ experience, chạy schemas, đánh giá qua reward/dissonance, tạo Imagine-Final ở mọi quy mô, kiểm tra sự khớp giữa Imagine-Final và body-base.

**Vô thức KHÔNG thể**: kiểm tra độ chính xác domain, mô phỏng tương lai, so sánh với ký ức. Vô thức **chỉ đo body-base** → body pleasant → vô thức "OK" → dù domain có thể sai (nghiện, limerence, comfort zone).

**PFC có thể (vô thức không)**: mô phỏng tương lai, so sánh ký ức, kiểm tra domain, chọn giữa các Imagine-Final cạnh tranh, tạo chunks đánh giá mới → nạp vào vô thức → cập nhật database.

**PFC KHÔNG thể (vô thức có)**: cảm trực tiếp (nhận từ cơ thể), xử lý 95% nền, compile tự động.

**Hàm ý cho F1**: Infant có cả PFC hardware + vô thức hoạt động từ thời thai nhi (theo reframe §1 dưới đây). Cái thiếu = **compiled chunks (nội dung)**. Chunks tích lũy qua experience → database vô thức phát triển → PFC có material để tìm kiếm/giữ/định hướng.

---

## §3 — Kiến Trúc 4-Folder Mechanism Của Chunk-Analysis

### §3.1 — Trục chia: loại cơ chế (KHÔNG phải tuổi hay chủ đề)

Chunk-Analysis master drill chia thành **4 folder** theo loại cơ chế:

```
Chunk-Analysis/
├── plan.md (master)
│
├── F1 Child-Chunk-Development/         🎯 N+4 hiện tại (folder này)
│   ├── 12 files body-input axis
│   ├── Cơ chế: substrate chunk compile từ body signals
│   ├── Test case: developmental arc 0-24 tháng (sạch nhất)
│   └── Hypotheses: H1 support + H11 formalization + đóng góp PFC-Inference Ladder
│
├── F3 Chunk-External-Development/      ⏳ N+5-N+7
│   ├── General files + Language/ sub-folder
│   ├── Cơ chế: chunks chia sẻ bên ngoài (language, grammar, abstract concepts)
│   ├── Test case: language acquisition + cognition upgrade
│   └── Hypotheses: H3 + H4 + H7 + H12 tentative
│
├── F4 Chunk-Internal-Processing/       ⏳ N+8-N+9
│   ├── 7 files
│   ├── Cơ chế: hình thành chunk nội bộ mới (logical, intuition, insight)
│   ├── Test case: adult cognition + expertise
│   └── Hypotheses: H2 + H5 + H6
│
└── 99-Master-Synthesis.md              ⏳ N+10+
    ├── Phán quyết cuối về tất cả hypotheses
    ├── Các cam kết kiến trúc
    └── Khuyến nghị commit cho framework
```

### §3.2 — Tại sao chia theo cơ chế, không theo tuổi

**Phương án bị loại**: Chia theo tuổi (0-2 tuổi / 3-6 tuổi / 7-12 tuổi / người lớn). Vấn đề: các cơ chế chồng lấp qua các độ tuổi. Cơ chế gán nhãn verbal hoạt động theo cùng một cách với đứa trẻ 2 tuổi học "đói" và người 40 tuổi học từ vựng tiếng Tây Ban Nha. Chia theo tuổi sẽ trùng lặp phân tích cơ chế.

**Chia theo cơ chế** nhóm các trường hợp theo **quá trình compile chunk đang làm gì**, bất kể khi nào nó xảy ra. Cửa sổ trẻ em 0-24 tháng đơn giản là **test case sạch nhất** cho cơ chế substrate (F1) vì: không có ngôn ngữ gây nhiễu, gradient phát triển rõ ràng, nhiều sự kiện quan sát được trên mỗi hệ thống body-input.

**Cross-ref**: Parent plan.md §3.1-§3.3 cho luận điểm kiến trúc đầy đủ.

### §3.3 — Các folder sẽ trả lời hypothesis nào

| # | Hypothesis | Nhà chính | Hỗ trợ từ |
|---|---|---|---|
| H1 | Chunk substrate cross-cutting | 99-Master-Synthesis | F1 + F3 + F4 (tất cả cung cấp bằng chứng) |
| H2 | Thread 2 = loại kết nối thứ 4 | F4 | — |
| H3 | Grammar-Scaffolding partial-embedded | F3/Language | F1 pre-verbal bridge |
| H4 | Abstract vs metaphysical = mã hóa modality | F3 | — |
| H5 | Vague = hội tụ multi-weak-signal | F4 | — |
| H6 | Chunk decay Ebbinghaus | F4 | Learning-Cycle (H8) |
| H7 | Valence = tương tác chunk × schema | F3 | — |
| **H8** | **Learning Dissonance Cycle** | **Learning-Cycle ✅** | **— (standalone N+1 drilled)** |
| **H9** | **Agent = Self-Pattern-Modeling thống nhất** | **Agent ✅** | **— (standalone N+2 drilled)** |
| **H10** | **Body Signal Precondition (5 điều kiện)** | **Body-Feedback-Draft ✅** | **— (standalone N+3 drilled)** |
| H11 | Receptive-Productive Asymmetry | F1 | 08-Verbal-Production-Arc §6 primary |
| H12 | Language evolution driver (post-verbal bypass) | F3/F4 | — |

**F1 trực tiếp giải quyết**: H1 (hỗ trợ qua bằng chứng substrate) + H11 (hình thức hóa trong 08) + PFC-Inference Ladder (đóng góp framework mới).

### §3.4 — Ý nghĩa "Child" (làm rõ tên folder)

**Tên folder "Child-Chunk-Development"** KHÔNG có nghĩa là "chunks đặc thù cho trẻ em". Nó có nghĩa là "**developmental arc như test case sạch nhất cho cơ chế hình thành substrate chunk**". Cơ chế substrate áp dụng cho mọi lứa tuổi — F1 chọn cửa sổ trẻ em 0-24 tháng vì:

1. **Không có ngôn ngữ gây nhiễu** — chunks verbal chưa tồn tại trong phần lớn cửa sổ 0-18 tháng, vì vậy chunks có thể được nghiên cứu độc lập với language scaffolding
2. **Gradient phát triển rõ ràng** — chunks tích lũy rõ ràng từng tuần, đo được qua developmental milestones
3. **Nhiều sự kiện quan sát được trên mỗi hệ thống body-input** — 30+ trường hợp trong `Feel-Example-Draft.md` §1-§3 cung cấp nền tảng thực nghiệm
4. **Bottleneck H10 P2 rõ ràng nhất** — Body-Feedback-Draft N+3 xác định "Chunks Base Adequacy" là keystone; cửa sổ 0-24 tháng cho thấy bottleneck này trực tiếp nhất

Cơ chế F1 hình thức hóa (substrate chunk compile từ body signals) hoạt động theo cùng cách trong học tập của người lớn — F1 chỉ dùng cửa sổ trẻ em như test bed sạch nhất.

---

## §4 — Đóng Góp Từ 3 Sub-Folder Đã Drilled

### §4.1 — Learning-Cycle (H8, N+1, 2026-04-14)

**Phạm vi**: Learning Dissonance Cycle — hình thức hóa cách một chunk đơn lẻ hoặc một liên kết chunk-chunk được compile, tinh chỉnh và tích hợp qua nhiều chu kỳ ngủ.

**Các claim chính**:
- Chu kỳ 8 giai đoạn: Draft → Kích hoạt + kiểm tra vô thức → Tín hiệu đồng thời (reward + fatigue + dissonance) → Nghỉ/ngủ → Tinh chỉnh đa cơ chế → Output → Thức → Lặp lại
- **6+1 cơ chế ngủ** riêng biệt (không phải một "consolidation" duy nhất): Synaptic Homeostasis (Tononi SHY), Hippocampal Replay, Active Systems Consolidation, REM Creative Linking, Emotional Decoupling, Gist Extraction, + tranh luận Dreaming-as-Simulation
- 3 tín hiệu đồng thời sau khi chunk kích hoạt: **Reward** (pattern giải quyết schema đang chờ) + **Fatigue** (chi phí chuyển hóa PFC) + **Dissonance** (pattern chưa smooth với các chunk lân cận)
- Giải quyết qua ngủ đa cơ chế → một đêm giảm tín hiệu → nhiều đêm → baseline shifts → chunk được tích hợp
- **Chi phí tỷ lệ với**: sự mới lạ × khoảng cách tích hợp × độ phức tạp schema hiện tại

**Đóng góp cho F1**: Cung cấp cơ chế offline cho chunk consolidation. Infant F1 0-3 tháng ngủ 16+ giờ/ngày — Learning-Cycle cho biết phần lớn chunk consolidation xảy ra trong giấc ngủ. Giấc ngủ REM thai nhi từ ~30 tuần cũng liên quan (F1 02-Womb-Birth §3.3 sẽ tham chiếu).

**Drill home cho F1**: Không re-drill. Cross-referenced trong phần "compile mechanisms" của mỗi file arc.

**File**: [../Learning-Cycle/Learning-Cycle.md](../Learning-Cycle/Learning-Cycle.md) (1556 dòng).

### §4.2 — Agent (H9, N+2, 2026-04-15)

**Phạm vi**: Cơ chế đọc-Agent thống nhất. Giải quyết 3 tension (binary vs spectrum / nhầm lẫn mirror / Agent function vs category).

**Các claim chính**:
- **Agent-reading = cơ chế Self-Pattern-Modeling** (solo, forward): PFC truy xuất self chunks khớp với entity mục tiêu → áp dụng như template → đọc output như dự đoán về trạng thái/hành vi/mong muốn của agent
- **Resonance = hiện tượng tương hỗ xuất hiện** (retrospective): khi 2+ agents' Self-Pattern-Modeling đồng thời kích hoạt thành công qua phản hồi giao tiếp
- Agent là **function chạy trên chunk substrate**, KHÔNG phải category riêng biệt hay hardware module → **hỗ trợ H1** (chunk substrate cross-cutting)
- Vận hành multi-modal (affective / somatic / visual-symbolic / verbal-cognitive / composite)
- Gradient chất lượng: Pattern-Type × Depth × Similarity × Feedback (4 trục)
- Thất bại ngưỡng → fallback dự đoán cơ học
- Schema override (Mode 1 / Mode 2) có thể thay thế hoàn toàn với agents tôn giáo/trừu tượng
- **Bị loại**: hardware mirror module, phân loại Object-Agent nhị phân, tách 2 lớp affective vs cognitive, Resonance như simulator solo
- **Được chấp nhận**: 🟢 Spelke core knowledge như innate triggers (biological motion, contingency, self-propelled), 🟢 Bird & Cook 2013 alexithymia drives empathy deficit

**Đóng góp cho F1**:
- **Developmental bootstrap** (Self-Pattern-Modeling §5): trạng thái Self-Pattern của infant xây dựng qua body-feedback + caregiver contingent response → cung cấp cơ chế cho social chunks trong [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md)
- **Giai đoạn Resonance** (0-3): cry contagion E9 (Giai đoạn 0) → smile contagion E13 (Giai đoạn 1) → egocentric empathy E26 (Giai đoạn 2) → mutual đầy đủ (người lớn) — liên quan đến F1 social arc + emotional interoceptive
- **Cảnh báo Alexithymia**: đọc bản thân kém → Self-Pattern-Modeling kém → social chunks kém. F1 phải bảo toàn interoception keystone (§5.4 Body-Feedback-Draft)

**Drill home cho F1**: Không re-drill. Cross-referenced trong [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §7.

**Files**: [../Agent/Agent.md](../Agent/Agent.md), [../Agent/Self-Pattern-Modeling.md](../Agent/Self-Pattern-Modeling.md), [../Agent/By-Product-Gap-Resonance.md](../Agent/By-Product-Gap-Resonance.md) (5754 dòng trên 4 files).

### §4.3 — Body-Feedback-Draft (H10, N+3, 2026-04-15)

**Phạm vi**: Kiến trúc body-feedback + 5 điều kiện tiên quyết cho signal fire + phân biệt 2 lớp body-feedback vs feeling + 2-tầng calibration (Darwinian + Hebbian) + tách biệt vô thức vs PFC.

**Các claim chính**:
- **H10 — Body Signal Precondition Hypothesis**: Body signal fires khi TẤT CẢ 5 điều kiện tiên quyết được thỏa mãn:
  1. **P1 Schema pending status** — schema đang chờ được fill/resolve/upgrade
  2. **P2 ⭐ Chunks Base Adequacy** — đủ chunks substrate để decode pattern
  3. **P3 prediction-delta threshold** — biến động đủ lớn cho VTA detect (dựa trên habituation)
  4. **P4 Goldilocks zone** — khớp 40-70% (không quá quen thuộc cũng không quá xa lạ)
  5. **P5 ⭐ Chunk association tag** — chunks fire có pattern liên kết được xác định bởi body state fingerprint trong thời gian compile: novelty-path body state (novelty cortisol + dopamine/opioid) → chunks gắn opioid → "thích dùng"; threat-path body state (threat cortisol + NE/adrenaline) → chunks gắn cortisol-avoidance → "tránh dùng". Xem [06a §7.0.1](06a-Interoceptive-Bladder-Keystone.md#§7.0.1) cho cơ chế được tinh chỉnh (cùng phân tử, body state khác nhau, kết quả ngược chiều).
- **Lớp body-feedback (L1-L2)** ≠ **Lớp Feeling (L3-L7)**:
  - Body-feedback: tín hiệu cơ thể thô, pre-verbal, tự động, bất biến qua phát triển
  - Feeling: quan sát PFC qua chunks, có thể huấn luyện, phát triển theo thời gian
- **Gradient clarity 7 lớp** (cùng cơ chế, cường độ tín hiệu khác nhau): Thô → Tích hợp → Nhận ra → Quan sát → Xác vị → Gán nhãn → Giải thích
- **Self-signal interoception keystone** (Body-Input-Enumeration §4.9): khả năng đọc nội trạng của cơ thể là điều kiện kiến trúc tiên quyết cho sự phát triển feeling layer
- **Gradient phát triển** (các ví dụ của user được ánh xạ): đái / đau / discomfort / buồn đều cho thấy Lớp 1-2 bất biến nhưng Lớp 3-7 compile dần dần qua tích lũy chunks + caregiver mirroring + language emergence
- **5 con đường huấn luyện** cho feeling layer: caregiver mirroring (thời thơ ấu) / tích lũy chunks / thiền / somatic therapy / Gendlin Focusing / + catalyst kỷ nguyên AI

**Đóng góp cho F1** ⭐ **KEYSTONE**:
- **P2 Chunks Base Adequacy = câu hỏi cơ chế trung tâm của F1**. N+3 xác định P2 là keystone developmental bottleneck nhưng chưa drill HOW chunks tích lũy. F1 trả lời điều này qua 12-file body-input axis drill.
- **Bladder gradient** (§5.5.1 của 01-Foundation): trẻ sơ sinh L1-L2 only → trẻ lớn chút post-hoc L3 → trẻ biết gọi L4-6 → người lớn full L7. ĐÂY chính là developmental arc đầy đủ mà F1 [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) sẽ deep-drill như phần trình bày "đơ mặt".
- **Critical period self-signal interoception**: nguồn gốc phát triển qua caregiver mirroring + secure attachment (Fonagy mentalizing). F1 phải bảo toàn điều này — [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) bao gồm mirroring scaffold, [06a + 06b] bao gồm sự xuất hiện interoception.
- **P5 Body state at compile** (được tinh chỉnh N+4c2-REV1, trước đây là "Cortisol tagging"): F1 cung cấp cơ chế critical period + sự phân biệt novelty vs threat cortisol + neural wear dimension + 4-threshold gradient + phân loại 3 cơ chế × 3 nguồn gốc (Nút Thắt 7 trong plan §0.6). Drill home [06a §7](06a-Interoceptive-Bladder-Keystone.md#§7) + các cam kết framework upstream [06a §7.0](06a-Interoceptive-Bladder-Keystone.md#§7.0).

**Files**: [../Body-Feedback-Draft/01-Foundation.md](../Body-Feedback-Draft/01-Foundation.md) + 02-Dissonance.md + 03-Reward.md + 04-Integration.md (9707 dòng trên 5 files).

### §4.4 — Triangulation của 3 hypotheses đã drilled

3 hypotheses đã drilled hội tụ về kiến trúc chunk substrate:

```
   H8 (Learning-Cycle)          H9 (Agent)              H10 (Body-Feedback)
   ──────────────────          ────────────            ───────────────────
   CÁCH chunks consolidate      chunks LÀM GÌ          KHI NÀO chunks fire
   (cơ chế offline)             trong social cognition   thành conscious feeling

   Chu kỳ 8 giai đoạn          Self-Pattern-Modeling       5 điều kiện tiên quyết
   6+1 cơ chế ngủ              như cơ chế solo          P2 Chunks Base Adequacy
   Baseline shift               Resonance         = keystone cho F1
                                hiện tượng tương hỗ

                               ↓  ↓  ↓

                      Cả 3 đều trỏ về H1 (chunk substrate
                      cross-cutting) — F1 cung cấp nền tảng
                      "HOW chunks FIRST compile" còn thiếu.
```

**Vị trí của F1**: F1 nằm ở **upstream** của cả 3 hypotheses đã drilled. F1 hỏi "**chunks compile như thế nào ngay từ đầu, ở cấp độ substrate, trước khi chúng có thể cycle (H8), trước khi chúng có thể mô hình hóa agents (H9), trước khi chúng có điều kiện tiên quyết cho feeling (H10)**". Cửa sổ phát triển 0-24 tháng được chọn vì substrate compile là rõ ràng nhất ở đó.

---

## §5 — Xem Trước Sứ Mệnh F1 v3

### §5.1 — Các cam kết (từ plan.md v3)

Drill F1 v3 (viết lại 2026-04-15 chuẩn bị N+4) cam kết 4 nguyên tắc kiến trúc thay thế cách tiếp cận top-down học thuật của v1:

1. **PFC Hardware Reframe** — PFC hoạt động từ thời thai nhi theo Huttenlocher/Grossmann/Werchan/Kouider/Doria + anchor Hodel 2018. Cái thiếu = chunks đã compiled (nội dung), không phải phần cứng PFC. Xem [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md).

2. **Body-Input Axis** — 6 hệ thống (visual / auditory / motor output / interoceptive / social / verbal), mỗi hệ thống có arc Connect → Read → Control. Đo được thông qua các events quan sát được theo từng giai đoạn phát triển. Thay thế các category cơ chế trừu tượng của v1. Insight của user (plan §0.5 Q7): "chỉ cần tập trung vào theo hướng body-input bé cần kết nối và đọc-hiểu, điều khiển, là có thể đo lường đc sự phát triển nhận thức khá chính xác".

3. **Event-Inference Methodology** — F1 claim observable events + suy luận trạng thái chunks, KHÔNG phải PFC developmental timeline. Mọi claim liên quan đến PFC đều mang qualifier 🟡 plausibility. Insight của user (plan §0.5 Q10): "câu hỏi không phải là ở giai đoạn nào có PFC. mà chúng ta chỉ cần liệt kê các event mà có khả năng có PFC. vì chúng ta không đo lường được PFC thực sự". Yếu hơn về mặt tri thức luận nhưng mạnh hơn về mặt khoa học.

4. **PFC-Inference Ladder** ⭐ **đóng góp framework mới** — bộ phân loại event 5 cấp hình thức hóa giả thuyết "đơ mặt" của user:
   - **L0** Phản xạ thuần túy (không cần chunks)
   - **L1** Phản ứng hậu kỳ (raw chunks đang compile, phản ứng sau event)
   - **L2** ⭐ **Kích hoạt Pattern-match** ("đơ mặt") — chunks fire theo antecedent, không có action intention
   - **L3** Phản ứng thô (partial action chunks)
   - **L4** Thực thi có phối hợp (full chunks stack)

   Reframe quan trọng: L2 KHÔNG phải là "PFC đang cố và thất bại". L2 LÀ "PFC pattern-match antecedent quen thuộc + chunk fire + biểu hiện ở cấp body, KHÔNG có action intention". Xem plan.md §0.7 để có phần trình bày đầy đủ.

### §5.2 — 7 Nút Thắt (convergence points)

Drill F1 có nhiều file nhưng hội tụ về **7 câu hỏi kiến trúc** phải được giải quyết (phán quyết hoặc pending-research) vào cuối F1:

1. **Phán quyết proto-chunk**: gradient vs rời rạc → drill home [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) §6 (phoneme gradient)
2. **Cơ chế P2 Chunks Base Adequacy** ⭐ **KEYSTONE** → drill home [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) §6
3. **Multi-modal binding khi mới sinh** → drill home [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6 (social smile E12)
4. **Đối chiếu PFC hardware × chunks missing** → drill home [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) + mỗi file arc
5. **Khoảng cách Receptive-Productive (H11)** → drill home [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §6 + [06a §8](06a-Interoceptive-Bladder-Keystone.md) anchor
6. **Cơ chế verbal-as-handle** → drill home [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §5
7. **Body state at compile** (tinh chỉnh N+4c2-REV1, trước đây là "Cortisol tagging critical period") → drill home [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) §7 (bao gồm §7.0 các cam kết framework upstream — novelty vs threat cortisol + neural wear + phân loại 3×3 + 4 threshold) + [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md) cross-validation 5-state

Mỗi phán quyết nút thắt được cam kết trong [10-F1-Synthesis.md](10-F1-Synthesis.md).

### §5.3 — Cấu trúc file (12 files)

```
Child-Chunk-Development/
├── plan.md (v3) + plan-v1-backup.md
├── 00-Chunk-System-Sketch.md              ← FILE NÀY (định hướng)
├── 01-PFC-Hardware-Reframe.md             (nền tảng — Nút Thắt 4)
├── 02-Womb-to-Birth-Baseline.md           (baseline)
├── 03-Visual-System-Arc.md                (Connect→Read→Control: mắt)
├── 04-Auditory-System-Arc.md              (⭐ Nút Thắt 1 primary — phoneme gradient)
├── 05-Motor-Output-Arc.md                 (Connect→Control: tay + locomotion)
├── 06a-Interoceptive-Bladder-Keystone.md  (⭐⭐ 4 Nút Thắt: 2 + 4 + 5 + 7)
├── 06b-Interoceptive-Other-States.md      (hunger + pain + thermal + emotional)
├── 07-Social-Recognition-Arc.md           (⭐ Nút Thắt 3 — social smile multi-modal)
├── 08-Verbal-Production-Arc.md            (⭐ Nút Thắt 5 + 6 — H11 formalization)
├── 09-Event-Chunks-Inference-Matrix.md    (cross-cutting synthesis)
└── 10-F1-Synthesis.md                     (7 phán quyết + khuyến nghị R-F1-*)
```

**Chia session** (theo "chậm mà chắc"):
- **N+4a** (hiện tại): 00 + 01 + 02 (nền tảng, ~2200-2800 dòng)
- **N+4b**: 03 + 04 + 05 (arc cảm giác + vận động, ~3000-3700 dòng)
- **N+4c**: 06a + 06b + 07 + 08 + 09 + 10 (interoceptive + social + verbal + synthesis, ~5100-6400 dòng)

---

## §6 — Công Việc Chờ Của F1 + Xem Trước Các Folder Khác

### §6.1 — F1 sẽ cung cấp gì

Vào cuối drill F1 (N+4a + N+4b + N+4c), các deliverables:

- ✅ Trình bày đầy đủ PFC hardware reframe với 5 pillars bằng chứng + anchor Hodel 2018
- ✅ Mô tả baseline womb-to-birth
- ✅ 6 phân tích body-input arc (visual, auditory, motor, interoceptive×2, social, verbal)
- ✅ 30+ events quan sát được được map vào các cấp PFC-Inference Ladder
- ✅ 7 phán quyết Nút Thắt (hoặc pending-research flags với các unknowns cụ thể)
- ✅ Tổng hợp bằng chứng substrate chunk H1 (cross-folder triangulation với H8/H9/H10)
- ✅ Hình thức hóa H11 Receptive-Productive Asymmetry với 7 dự đoán có thể falsify
- ✅ Đóng góp framework PFC-Inference Ladder (bộ phân loại event 5 cấp mới)
- ✅ Khuyến nghị cập nhật framework R-F1-* cho 99-Master-Synthesis

### §6.2 — F1 sẽ KHÔNG bao gồm

- **Nhận thức người lớn + chuyên môn** — thuộc về F4 Chunk-Internal-Processing
- **Khảo sát sâu ngữ pháp ngôn ngữ** — thuộc về F3/Language sub-folder
- **Khái niệm trừu tượng vs siêu hình** — thuộc về F3 (H4)
- **Claim đo lường PFC neural trực tiếp** — ngoài phạm vi phương pháp luận (event-inference only)
- **Ứng dụng lâm sàng** (sàng lọc tự kỷ, chẩn đoán chậm phát triển) — được tham chiếu ngắn gọn, không phải chủ đề chính
- **Khảo sát sâu biến thể liên văn hóa** — chỉ nguyên tắc chung

### §6.3 — Xem trước F3 (N+5-N+7)

**F3 Chunk-External-Development** xử lý chunks được chia sẻ bên ngoài — ngôn ngữ, ngữ pháp, khái niệm trừu tượng, nâng cấp nhận thức. Xây dựng trực tiếp trên các outputs của F1:
- Substrate pre-verbal (từ F1) → chunks verbal cài đặt lên trên
- Cơ chế multi-modal binding (từ F1 Nút Thắt 3) → ngôn ngữ như modality thứ 5 (hoặc symbolic compression overlay, phán quyết F1 Nút Thắt 6)
- Cơ chế Receptive-Productive H11 (từ F1) → mở rộng sang việc người lớn học ngoại ngữ

**F3 chứa Language/ sub-folder lồng ghép** (di chuyển từ Grammar-Scaffolding/ cũ, theo prep v2 N+4): 6 files bao gồm vocabulary / ngữ pháp / xác nhận anchor / relativity liên ngôn ngữ / tiến hóa ngôn ngữ / synthesis.

### §6.4 — Xem trước F4 (N+8-N+9)

**F4 Chunk-Internal-Processing** xử lý hình thành chunk nội bộ mới — kết nối logic, trực giác, insight, chuỗi + anchor decay. 7 files. Giải quyết H2 (loại kết nối thứ 4), H5 (hội tụ multi-weak-signal = "vague"), H6 (chunk decay Ebbinghaus). Cũng hình thức hóa H12 tentative (language evolution driver qua post-verbal bypass).

### §6.5 — 99-Master-Synthesis (N+10+)

Tích hợp cuối cùng của tất cả 4 sub-folder + bộ ba đã drilled (H8/H9/H10). Cung cấp:
- Phán quyết cuối cùng của tất cả 12 hypotheses
- Các cam kết kiến trúc (H1 substrate, dependencies feeling system)
- Khuyến nghị commit framework (bao gồm R-F1-* từ F1)
- Cầu nối với drill Feeling L3 tương lai (đã hoãn)

---

## §7 — Cách Đọc Phần Còn Lại Của F1 Sub-Folder

### §7.1 — Các đường đọc theo vai trò

**Nếu bạn đang drill F1 session tiếp theo (N+4b hoặc N+4c)**:
- Đọc plan.md §0 North Star + §0.5 user quotes + §0.6 Nút Thắt + §0.7 PFC Ladder trước
- Sau đó file này (00-Sketch) để làm mới mental model
- Sau đó các file arc liên quan (03-08) theo mục tiêu session
- Dùng 09-Event-Matrix như reference index

**Nếu bạn đang review phương pháp luận F1**:
- plan.md §0.3 event-inference methodology
- plan.md §0.7 PFC-Inference Ladder
- plan.md §4 design decisions
- File này §5 xem trước sứ mệnh F1 v3

**Nếu bạn đang tích hợp F1 vào 99-Master-Synthesis**:
- 10-F1-Synthesis.md (phán quyết + khuyến nghị R-F1-*)
- 09-Event-Chunks-Inference-Matrix.md (dữ liệu cấu trúc)
- File này §4 (triangulation các sub-folder đã drilled)

**Nếu bạn là reader mới muốn định hướng trong chunk system**:
- File này (00-Sketch) — định hướng reader
- Sau đó plan.md §0 cho sứ mệnh F1 cụ thể
- Sau đó [Schema/Chunk.md](../../Schema/Chunk.md) cho định nghĩa chunk nguyên tử

### §7.2 — Thứ tự dependency trong F1

```
00-Chunk-System-Sketch (định hướng)
       ↓
01-PFC-Hardware-Reframe (nền tảng cho suy luận PFC của mỗi arc)
       ↓
02-Womb-to-Birth-Baseline (trạng thái thai kỳ trước khi các arcs bắt đầu)
       ↓
03 Visual  ──┐
04 Auditory ─┤  song song, thứ tự linh hoạt
05 Motor    ─┤
06a Bladder ─┤  (keystone, làm cẩn thận)
06b Khác   ──┤
07 Social  ──┤
08 Verbal ───┘
       ↓
09-Event-Matrix (cross-cutting synthesis, tổng hợp 03-08)
       ↓
10-F1-Synthesis (phán quyết + khuyến nghị)
```

**Quy tắc**: 01 + 02 trước bất kỳ file arc nào. Bất kỳ file arc nào trước 09. 09 trước 10.

### §7.3 — Quy ước style (để tiếp tục drill)

- **Tiếng Việt primary + English technical terms**
- **Xưng hô bạn-tôi**
- **🟢 Nghiên cứu có căn cứ / 🟡 Suy luận framework / 🔴 Giả thuyết** — mọi claim chính đều được đánh dấu
- **"Imagine-Final" không bao giờ viết tắt**
- **KHÔNG có ví dụ cá nhân** — chỉ tình huống chung + nhân vật lịch sử công khai
- **Giữ nguyên quotes của user** (11 quotes trong plan.md §0.5)
- **Các claim liên quan đến PFC mang qualifier 🟡 plausibility** (event-inference methodology)
- **Phân loại cấp Ladder ở cấp event, không phải cấp tuổi**
- **Cross-references hai chiều** — nếu file A tham chiếu file B, file B (khi drilled) tham chiếu ngược lại file A
- **Mỗi file đứng độc lập về khả năng đọc** — mỗi file có §0 Abstract + §1 Position để reader mới định hướng
- **Đọc nghiên cứu theo yêu cầu** — đọc nghiên cứu theo từng file, không đọc hết trước

---

## §8 — Cross-References

### §8.1 — F1 nội bộ

- [plan.md](plan.md) — master F1 v3 plan (2429 dòng)
- [plan-v1-backup.md](plan-v1-backup.md) — v1 gốc được giữ lại
- [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) — file nền tảng (drill tiếp theo)
- [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) — file baseline (drill sau 01)
- 03-08 các file body-input arc — drill N+4b/c
- [09-Event-Chunks-Inference-Matrix.md](09-Event-Chunks-Inference-Matrix.md) — cross-cutting synthesis
- [10-F1-Synthesis.md](10-F1-Synthesis.md) — phán quyết cuối

### §8.2 — Các sibling Chunk-Analysis đã drilled

- [../Learning-Cycle/Learning-Cycle.md](../Learning-Cycle/Learning-Cycle.md) — H8 (1556 dòng)
- [../Agent/Agent.md](../Agent/Agent.md) — điểm vào H9
- [../Agent/Self-Pattern-Modeling.md](../Agent/Self-Pattern-Modeling.md) — drill sâu cơ chế solo H9
- [../Agent/By-Product-Gap-Resonance.md](../Agent/By-Product-Gap-Resonance.md) — H9 hiện tượng tương hỗ
- [../Body-Feedback-Draft/01-Foundation.md](../Body-Feedback-Draft/01-Foundation.md) — H10 foundation (7-layer model + §5)
- [../Body-Feedback-Draft/02-Dissonance.md](../Body-Feedback-Draft/02-Dissonance.md) — H10 các trường hợp dissonance
- [../Body-Feedback-Draft/03-Reward.md](../Body-Feedback-Draft/03-Reward.md) — H10 các trường hợp reward
- [../Body-Feedback-Draft/04-Integration.md](../Body-Feedback-Draft/04-Integration.md) — H10 tích hợp + P5 finalization

### §8.3 — Các sibling Chunk-Analysis chưa drilled

- [../plan.md](../plan.md) — master Chunk-Analysis plan (N+4 prep v3)
- [../Chunk-External-Development/plan.md](../Chunk-External-Development/plan.md) — F3 stub (N+5-N+7)
- [../Chunk-External-Development/Language/plan.md](../Chunk-External-Development/Language/plan.md) — Language sub-folder stub
- [../Chunk-Internal-Processing/plan.md](../Chunk-Internal-Processing/plan.md) — F4 stub (N+8-N+9)
- `99-Master-Synthesis.md` (chưa tạo) — N+10+ final

### §8.4 — Framework upstream

- [../../Schema/Chunk.md](../../Schema/Chunk.md) — định nghĩa chunk nguyên tử + 4 cơ chế compile + split vô thức/PFC
- [../../Schema/Schema.md](../../Schema/Schema.md) — schema là mạng chunks có purpose
- [../../Schema/Chunk-Search-Advanced.md](../../Schema/Chunk-Search-Advanced.md) — spreading activation, incubation, priming
- [../../Schema/Anchor-Schema.md](../../Schema/Anchor-Schema.md) — nguồn reward + dynamics tin tưởng
- [../../Schema/Personal-Melody.md](../../Schema/Personal-Melody.md) — cơ chế baseline shift
- [../../Imagination/PFC-Analysis.md](../../Imagination/PFC-Analysis.md) §4.0 REFRAME — anchor PFC hardware reframe
- [../../Imagination/Imagine-Final.md](../../Imagination/Imagine-Final.md) — tạo expectation pattern
- [../../Imagination/Somatic-Articulation-Loop.md](../../Imagination/Somatic-Articulation-Loop.md) — 3 trạng thái implicit → transitional → explicit
- [../../Body-Base/Feeling/](../../Body-Base/Feeling/) — Feeling folder 4-file hoàn chỉnh (L3 cross-ref tương lai)
- [../../Body-Base/Body-Parenting-Optimization.md](../../Body-Base/Body-Parenting-Optimization.md) §0 REFRAME NOTE

### §8.5 — Research anchors (xem trước)

**Cho PFC reframe (drilled trong 01)**:
- Huttenlocher 1979, Huttenlocher & Dabholkar 1997 (synaptogenesis)
- Grossmann 2013, Werchan et al. 2016, Farroni et al. 2002 (fNIRS infant PFC)
- Doria et al. 2010, Gao et al. 2009 (resting-state networks pre-birth)
- Yakovlev & Lecours 1967 (myelination)
- Kouider et al. 2013 (frontal consciousness signature 5mo)
- **Hodel 2018** (anchor reframe paper)

**Cho womb-birth (drilled trong 02)**:
- DeCasper & Spence 1986 (auditory learning trước sinh)
- Mehler 1988 (rhythm ngôn ngữ mẹ đẻ khi mới sinh)
- Morton & Johnson 1991 (CONSPEC template khuôn mặt bẩm sinh)
- Fantz 1961 (ưu tiên khuôn mặt khi mới sinh)

**Các citation tiếp theo** theo mỗi file body-input arc trong N+4b/c.

---

## §9 — Câu Hỏi Mở (được giải quyết ở 01-10)

Không có hành động ở cấp file này (tổng hợp thuần túy). Các câu hỏi sau được **chuyển tiếp** đến các file drill sâu:

1. **PFC hardware reframe thay đổi phương pháp luận F1 như thế nào cụ thể?** → [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) §6
2. **Trạng thái baseline thai kỳ cụ thể là gì?** → [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) §2-§5
3. **Tại sao interoception là keystone body-input?** → [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) §6 (liên kết P2)
4. **Làm thế nào chunks multi-modal binding mà không có coordinator?** → [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) §6 (social smile E12 + Nút Thắt 3)
5. **Nhãn verbal thêm gì vào các chunks đã có trước?** → [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §5 (Nút Thắt 6)
6. **Tại sao comprehension luôn đến trước production?** → [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) §6 (hình thức hóa H11)

---

## §10 — Trạng Thái + Bước Tiếp Theo

**Trạng thái**: 00-Sketch DRAFT hoàn chỉnh (~650 dòng mục tiêu, chức năng định hướng). Reader lúc này đã có mental model cho:
- Kiến trúc 3 lớp (Body-Feedback L1 ✅ / Chunk L2 🎯 / Feeling L3 ⏳)
- Cơ bản Chunk System (chunk là gì, 4 cơ chế compile, split vô thức/PFC)
- Kiến trúc 4-folder mechanism của Chunk-Analysis (F1/F3/F4/99)
- Đóng góp từ 3 sub-folder đã drilled (triangulation H8/H9/H10)
- Sứ mệnh F1 v3 (4 cam kết kiến trúc + 7 nút thắt + 12 files + 3-session split)
- Các đường đọc + quy ước style

**File tiếp theo**: [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) — drill sâu file nền tảng về reframe PFC hardware online vs thiếu nội dung compiled. ~800-1100 dòng mục tiêu. Phase F1-P2 trong chuỗi drill Session N+4a.

**Sau 01**: [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) — prenatal default smooth + first cry cascade + Q&A thực nghiệm từ user (§0.5 Q5-Q6 của plan). ~800-1000 dòng mục tiêu. Phase F1-P3.

**Sau 02**: Kết thúc Session N+4a (Phase F1-P4) — cập nhật parent plan.md trạng thái F1 (3 files drilled), cập nhật memory project_chunk_analysis.md, cập nhật NEXT-SESSION-DIRECTIONS.md cho N+4b (arc cảm giác + vận động). Sau đó compact + drill N+4b fresh.

---

> **00-Chunk-System-Sketch-VI.md — Kết thúc file.**
>
> Định hướng nhẹ hoàn chỉnh. Reader lúc này đã được trang bị mental model kiến trúc 3 lớp + xem trước sứ mệnh F1 v3. Tiến đến [01-PFC-Hardware-Reframe-VI.md](01-PFC-Hardware-Reframe-VI.md) để drill nền tảng sâu.
