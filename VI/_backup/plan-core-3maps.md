# Plan: Core v7.8 — Tách thành 3 Bản Đồ

> **Ngày tạo:** 2026-05-10
> **Trạng thái:** PLAN — chưa triển khai
> **Trigger:** Insight "máy tính có 3 loại bản đồ: hardware, software, user guide"
> **Mục tiêu:** Tách Core-v7.8-Draft.md (1,470L) thành 3 file riêng biệt,
> mỗi file phục vụ 1 góc nhìn khác nhau VỀ CÙNG HỆ THỐNG.
> **Nguyên tắc:** Chậm mà chắc. Chất lượng cao nhất. Mỗi session 1 file.

---

## §0 — TẠI SAO TÁCH 3 BẢN ĐỒ

### §0.1 Analogy gốc — máy tính

Máy tính luôn có 3 loại bản đồ cho 3 loại người:

| # | Chuyên gia | Bản đồ | Nội dung |
|---|---|---|---|
| 1 | Hardware engineer | Sơ đồ mạch | CPU, transistor, RAM, bus — CÁI GÌ ở ĐÂU |
| 2 | Software engineer | Code architecture | Functions, loops, algorithms — CHẠY THẾ NÀO |
| 3 | End user | User guide | Click Save, Ctrl+Z — DÙNG THẾ NÀO |

End user KHÔNG CẦN biết code hay mạch → vẫn dùng 100% phần mềm phức tạp.

### §0.2 Framework hiện tại — thiếu bản đồ thứ 3

Core-v7.8-Draft.md chứa 2 bản đồ (Hardware Map §1.2 + Software Map §1.3).
Tất cả application files (FLT, SAL, AI-Schema-Detection, Body-Personal-Optimization)
đều viết bằng ngôn ngữ MECHANISM → chưa có bản đồ thuần từ góc nhìn OBSERVER.

### §0.3 Ba bản đồ target

| # | Tên file | Góc nhìn | Đối tượng | Ngôn ngữ |
|---|---|---|---|---|
| 1 | Core-Hardware.md | CÁI GÌ ở ĐÂU | Neuroscience researcher | Giải phẫu, vùng não |
| 2 | Core-Software.md | CHẠY THẾ NÀO | Framework researcher | Mechanism, cycle, chunks |
| 3 | Core-Interface.md | QUAN SÁT + TƯƠNG TÁC THẾ NÀO | Mọi người | Observer experience |

3 bản đồ mô tả CÙNG hệ thống. Khác góc nhìn. Đọc độc lập được.

### §0.4 Tại sao tên "Interface"

- "Interface" phổ thông: ai cũng biết "user interface"
- Chính xác kỹ thuật: Feeling = interface giữa unconscious và PFC (established)
- Song song đẹp: Hardware Map / Software Map / Interface Map
- Không prescriptive (khác "Practice" hay "Guide")

---

## §1 — TRẠNG THÁI HIỆN TẠI

### §1.1 Core-v7.8-Draft.md (1,470L) — cấu trúc hiện tại

```
§0  — Tại sao v7.8 (~130L)           ← lịch sử, framing chung
§1.1 — Hai góc nhìn (~20L)           ← framing "cùng hệ thống"
§1.2 — Hardware Map (~80L)            ← sơ đồ A/B/C/D zones
§1.3 — Software Map (~80L)            ← sơ đồ cycle 7-step
§1.4 — Mapping table (~30L)           ← hardware ↔ software
§1.5 — Tại sao cycle (~25L)           ← so sánh v7.5 layers
§1.6 — So sánh 6-step loop (~15L)     ← complementary, not competing
§2  — Domain (~45L)                   ← môi trường thực
§3  — Body-Input L0+L1 (~110L)        ← circuit breaker + 17 inputs
§4  — Unconscious Processing (~250L)  ← chunks, body-feedback, cortisol, functions
§5  — Feeling bridge (~85L)           ← 7-layer, threshold, types
§6  — PFC (~110L)                     ← observer, orchestrate, hardware, activation
§7  — Body-Output (~30L)              ← motor, speech, expression
§8  — Observation Parameters (~90L)   ← tổng quan 14 parameters
§9  — Development (~70L)              ← chunk density trajectory
§10 — Timescales (~15L)               ← ms → decades
§11 — Key reframes (~45L)             ← 10 thay đổi từ v7.5
§12 — Honest assessment (~40L)        ← provides + NOT provides + open Qs
§13 — Cross-references (~80L)         ← 4 sections links
```

### §1.2 Application files hiện có (mảnh của Interface Map)

| File | Vị trí | Góc nhìn | Ghi chú |
|---|---|---|---|
| Body-Personal-Optimization.md | Body-Base/backup/ | OBSERVER | 445L, 5 principles. Đang ở backup |
| AI-Schema-Detection.md §7 | Observation/ | HYBRID | Self-Drill Mode, guardrails |
| Logic-Feeling-Balance.md | PFC/ | OBSERVER | Meta-principle, 1,433L |
| Somatic-Articulation-Loop.md §6 | PFC/Imagination/ | HYBRID | AI as catalyst, implications |
| Feeling-Literacy-Training.md | Feeling/ | MECHANISM→OBSERVER | 5-stage training, §5.6 Natural Discovery |
| Ask-AI/ | Ask-AI/ | OBSERVER | Translation layer cho end users |

→ Nội dung observer TỒN TẠI nhưng RẢI RÁC trong các file mechanism.
→ Core-Interface.md sẽ THỐNG NHẤT góc nhìn observer thành 1 bản đồ.

---

## §2 — KẾ HOẠCH THỰC THI

### §2.1 Thứ tự và lý do

```
Phase 0: Backup                       ← di chuyển Core-v7.8-Draft.md → _backup/
Phase 1: Core-Software.md             ← FOUNDATION — Interface phụ thuộc vào nó
Phase 2: Core-Hardware.md             ← Extract + enrich, ngắn nhất
Phase 3: Core-Interface.md            ← Viết MỚI, dựa trên Software đã hoàn thành
Phase 4: Cross-reference updates      ← Cập nhật các file khác tham chiếu Core Draft
```

**Tại sao thứ tự này:**
- Software = foundation (mechanism). Interface = derived (observer translation).
  Giống phát triển phần mềm: backend trước, UI sau.
- Hardware = stable, brief. Có thể làm nhanh giữa Software và Interface.
- Interface = VIẾT MỚI, cần foundation vững nhất → cuối cùng.

### §2.2 Mỗi session 1 file

- Session A: Triển khai Core-Software.md (nặng nhất, restructure)
- Session B: Triển khai Core-Hardware.md (nhẹ, extract) — có thể gộp nếu đủ context
- Session C: Triển khai Core-Interface.md (novel nhất, cần attention cao nhất)
- Session D: Cross-reference updates (scan toàn bộ framework)

---

## §3 — PHASE 0: BACKUP

### Actions:
- [ ] Move `Core-v7.8-Draft.md` → `_backup/Core-v7.8-Draft-pre-3maps.md`
- [ ] Giữ nguyên nội dung, không sửa — pure backup

---

## §4 — PHASE 1: Core-Software.md

### §4.1 Mục tiêu

Bản đồ phần mềm: MÔ TẢ CHI TIẾT NHẤT cách hệ thống CHẠY.
Cycle flow, chunk dynamics, body-feedback, feeling bridge, PFC, observation parameters.
Ngôn ngữ: mechanism + framework synthesis.
Đối tượng: người muốn HIỂU WHY hệ thống hoạt động như vậy.

### §4.2 Nguồn nội dung — cái gì GIỮ, cái gì BỎ, cái gì THÊM

```
TỪ CORE DRAFT:                         → CORE-SOFTWARE:
──────────────                          ────────────────
§0 Tại sao v7.8 (130L)                 → RÚT GỌN (~30-40L framing)
                                           "File này là 1 trong 3 bản đồ"
                                           + brief v7.5→v7.8 transition
§1.1 Hai góc nhìn (20L)                → REWRITE → "Ba góc nhìn" (~20L)
                                           Giới thiệu 3 maps concept
§1.2 Hardware Map (80L)                 → BỎ → goes to Core-Hardware.md
§1.3 Software Map diagram (80L)         → GIỮ — mở đầu file
§1.4 Mapping table (30L)                → GIỮ — cross-reference tới Hardware
§1.5 Tại sao cycle (25L)               → GIỮ
§1.6 So sánh 6-step (15L)              → GIỮ hoặc rút gọn
§2 Domain (45L)                         → GIỮ
§3 Body-Input (110L)                    → GIỮ
§4 Unconscious Processing (250L)        → GIỮ + potentially IMPROVE
§5 Feeling bridge (85L)                 → GIỮ
§6 PFC (110L)                           → GIỮ (bỏ §6.3 hardware → Core-Hardware)
§7 Body-Output (30L)                    → GIỮ
§8 Observation Parameters (90L)         → GIỮ (mechanism definitions)
§9 Development (70L)                    → GIỮ
§10 Timescales (15L)                    → GIỮ
§11 Key reframes (45L)                  → GIỮ hoặc rút gọn
§12 Honest assessment (40L)             → GIỮ
§13 Cross-references (80L)              → CẬP NHẬT (thêm Hardware + Interface)
```

### §4.3 Cải tiến khi restructure

Cơ hội improve, KHÔNG chỉ copy-paste:

1. **Framing mới**: "1 trong 3 bản đồ" thay vì "2 góc nhìn"
2. **§0 rút gọn**: chỉ giữ lý do v7.8 + design principles, bỏ chi tiết lịch sử
3. **§4 Unconscious**: cập nhật với insights từ Drill S1-S12
   - Compile Taxonomy reference rõ hơn
   - Body-Feedback Mechanism (4th axis) reference
   - Reward-Signal-Architecture Type A/B integration
4. **§6.3 PFC Hardware**: bỏ → Core-Hardware (chỉ giữ PFC functional)
5. **§8 Observation Parameters**: cập nhật bảng với Gratitude, Obligation đã thêm v0.2
6. **§13 Cross-references**: thêm Core-Hardware + Core-Interface
7. **Metadata**: v0.3, ngày mới, status update

### §4.4 Cấu trúc dự kiến Core-Software.md

```
Metadata (status, date, dependencies, 3-maps framing)
§0  — Ba bản đồ + Tại sao cycle-based (~50L)
§1  — Software Map diagram + Cycle architecture (~120L)
      §1.1 Ba góc nhìn (brief intro)
      §1.2 Software Map (sơ đồ cycle)
      §1.3 Mapping tới Hardware (table)
      §1.4 Tại sao cycle, không layers
§2  — Domain (~45L)
§3  — Body-Input L0+L1 (~100L)
§4  — Unconscious Processing (~250L, improved)
      §4.1 Chunk-System
      §4.2 Body-Feedback
      §4.3 Cortisol amplifier
      §4.4 Functions trên chunks
§5  — Feeling bridge (~85L)
§6  — PFC functional (~80L, bỏ hardware specs)
§7  — Body-Output (~30L)
§8  — Observation Parameters (~90L, updated)
§9  — Development trajectory (~70L)
§10 — Multiple timescales (~15L)
§11 — Key reframes từ v7.5 (~45L)
§12 — Honest assessment (~40L)
§13 — Cross-references (~80L, updated)
```

**Ước lượng:** ~900-1100 dòng

### §4.5 Files cần đọc trước khi triển khai Phase 1

- [ ] Core-v7.8-Draft.md (full) — nguồn chính
- [ ] plan-core-3maps.md (file này) — plan
- [ ] Compile-Taxonomy.md — verify §4.1 references
- [ ] Reward-Signal-Architecture.md — verify Type A/B integration
- [ ] PFC-Configuration.md — verify PFC functional updates
- [ ] Body-Feedback-Mechanism.md — verify 4th axis reference

### §4.6 Quality checklist Phase 1

- [ ] Mọi nội dung hardware-specific đã chuyển sang Core-Hardware
- [ ] §0 framing rõ ràng: "1 trong 3 bản đồ"
- [ ] Cycle diagram giữ nguyên chất lượng
- [ ] §4 improved với insights gần đây (không chỉ copy)
- [ ] Mapping table hardware ↔ software vẫn có (cross-reference)
- [ ] §13 cross-refs updated
- [ ] Đọc lại toàn file — flow tự nhiên, không có "lỗ hổng" từ extract

---

## §5 — PHASE 2: Core-Hardware.md

### §5.1 Mục tiêu

Bản đồ phần cứng: MÔ TẢ CƠ BẢN các thành phần vật lý.
Vùng não, kết nối, timing, specs cá nhân.
Ngôn ngữ: giải phẫu thần kinh, neuroscience research.
Đối tượng: chuyên gia muốn VERIFY framework bằng fMRI, lesion studies.

### §5.2 Nguồn nội dung

```
TỪ CORE DRAFT:                         → CORE-HARDWARE:
──────────────                          ────────────────
§1.2 Hardware Map diagram (80L)         → GIỮ — lõi của file
§3.2 17 receptor categories             → EXTRACT phần hardware specs
§6.3 PFC Hardware Profile               → MOVE vào đây
§1.4 Mapping table                      → REFERENCE (full table ở Software)

TỪ CÁC FILE KHÁC:
Neural-Architecture.md (nếu có)         → REFERENCE
PFC-Hardware sections                   → EXTRACT relevant parts
Body-Input-Enumeration.md               → REFERENCE receptor details
```

### §5.3 Cấu trúc dự kiến Core-Hardware.md

```
Metadata (status, date, framing)
§0  — Ba bản đồ + File này mô tả gì (~20L)
§1  — Hardware Map diagram (~80L)
      Sơ đồ A/B/C/D zones (giữ từ Core Draft §1.2)
§2  — PFC Reach Gradient (~30L)
      A→B strong, A→C variable, A→D weak
§3  — Timing Hierarchy (~20L)
      D ~50ms → C ~12ms → B ~150ms → A ~200ms+
§4  — Receptor System Overview (~40L)
      17 categories brief (full detail → Body-Input-Enumeration.md)
§5  — Hardware Profile — Individual Specs (~60L)
      WM capacity, COMT, DRD4, MAO-A, Modality Balance
      (move từ §6.3 Core Draft)
§6  — Hardware Sets Range, Chunks Choose Position (~20L)
      Key principle: hardware ≠ destiny
§7  — Cross-references (~30L)
      → Core-Software.md (mechanism)
      → Core-Interface.md (observer view)
      → Body-Input-Enumeration.md (17 inputs detail)
      → Neural-Architecture.md (deeper hardware)
```

**Ước lượng:** ~300-400 dòng — NGẮN NHẤT trong 3 file, intentionally brief.

### §5.4 Files cần đọc trước khi triển khai Phase 2

- [ ] Core-v7.8-Draft.md §1.2 + §6.3 (từ backup) — nguồn chính
- [ ] Core-Software.md (vừa hoàn thành Phase 1) — verify không trùng
- [ ] Body-Input-Enumeration.md §1-§2 (brief) — receptor detail level

### §5.5 Quality checklist Phase 2

- [ ] Sơ đồ A/B/C/D giữ nguyên chất lượng (hoặc cải thiện)
- [ ] Không trùng lặp nội dung với Core-Software
- [ ] Brief + focused — đúng vai trò "reference cho chuyên gia"
- [ ] PFC hardware specs đầy đủ (từ §6.3)
- [ ] Cross-references tới 2 file kia

---

## §6 — PHASE 3: Core-Interface.md

### §6.1 Mục tiêu

Bản đồ giao diện: MÔ TẢ TRỰC QUAN NHẤT cách QUAN SÁT và TƯƠNG TÁC với hệ thống.
Từ góc nhìn PFC (observer) — KHÔNG dùng jargon mechanism.
Ngôn ngữ: trải nghiệm hàng ngày, practical, ai cũng hiểu.
Đối tượng: BẤT KỲ AI muốn hiểu và làm việc với hệ thống body-brain của mình.

### §6.2 Nguyên tắc thiết kế Interface Map

1. **KHÔNG dùng jargon**: "chunk compile" → "brain ghi nhớ sâu"
   "VTA delta" → "brain phát hiện cái mới"
   "spreading activation" → "1 ý kéo theo ý khác"
2. **Tổ chức theo CÁI NGƯỜI THẤY**: không theo mechanism flow
3. **Mỗi mục = 1 observable pattern + ý nghĩa thực tế + cái có thể làm**
4. **KHÔNG prescriptive**: "đây là công cụ, đây là cách chúng hoạt động"
   KHÔNG nói "bạn nên sống thế nào"
5. **Descriptive, không clinical**: consistent với framework principle §12.2
6. **Self-contained**: đọc được KHÔNG CẦN Software hay Hardware

### §6.3 Cách Interface Map KHÁC Software Map

Cùng 1 truth, khác ngôn ngữ hoàn toàn:

```
SOFTWARE MAP:                              INTERFACE MAP:
──────────                                 ─────────────
"Body-Feedback dual-pull:                  "Khi cảm thấy mâu thuẫn giữa
Hardware pull vs Domain pull"               'muốn thoải mái' và 'biết nên 
                                            thay đổi' → 2 lực kéo tự nhiên,
                                            không phải lỗi"

"7-layer fidelity gradient,                "Label đầu tiên bạn gắn cho
L6-L7 lossy"                               cảm xúc thường THIẾU CHÍNH XÁC.
                                            Trước khi label, hold ở
                                            'có cái gì đó' → chính xác hơn"

"Chunk compile qua repetition              "Học thứ mới → lúc đầu khó chịu
+ emotional peak + multi-modal              → lặp lại + ngủ đủ → dần tự nhiên.
+ sleep consolidation"                      Đó là quá trình bình thường"

"PFC effectiveness =                       "Bình tĩnh KHÔNG phải vì ý chí mạnh
f(compiled chunks)"                         — mà vì đã có kinh nghiệm compiled
                                            cho tình huống đó"

"H10: 5 preconditions                      "Đọc sách hay mà 'chẳng thấm'?
ALL required for signal"                    Có thể thiếu 1 trong 5 điều kiện:
                                            chưa cần / chưa đủ nền / quá quen
                                            / quá lạ / đã ghét sẵn"
```

### §6.4 Cấu trúc dự kiến Core-Interface.md

```
Metadata (status, date, framing)

§0  — Ba bản đồ + File này dành cho ai (~30L)
      "Bạn không cần biết não hoạt động thế nào (Hardware)
       hay cơ chế chi tiết ra sao (Software).
       File này mô tả CÁI BẠN CÓ THỂ QUAN SÁT
       và CÁI BẠN CÓ THỂ LÀM VỚI NHỮNG QUAN SÁT ĐÓ."

§1  — Bạn có thể QUAN SÁT gì (~100L)
      Tất cả những gì "hiện lên" cho ý thức:
      
      §1.1 — Cảm giác cơ thể (đói, mệt, đau, ấm, lạnh,...)
      §1.2 — Cảm xúc (vui, buồn, giận, sợ, xấu hổ,...)
      §1.3 — Xu hướng/thôi thúc (muốn ăn, muốn tránh, muốn nói,...)
      §1.4 — "Lấn cấn" — tín hiệu "có gì đó không ổn" (rất quan trọng)
      §1.5 — Linh cảm / gut feeling ("tôi cảm giác nên làm X")
      §1.6 — Pattern lặp lại ("tôi luôn phản ứng như vậy khi...")
      §1.7 — Trạng thái nền (mood chung, năng lượng, hứng/chán)

§2  — Mỗi quan sát CÓ Ý NGHĨA gì (~120L)
      Practical meaning, KHÔNG phải mechanism:
      
      §2.1 — Thoải mái = hệ thống đang chạy trơn tru
      §2.2 — Khó chịu = 3 khả năng (đau thật / mismatch / đang học)
             → phân biệt 3 cái này = kỹ năng quan trọng nhất
      §2.3 — "Không cảm thấy gì" = KHÔNG phải không có tín hiệu
             → có thể là chưa nhạy đủ để nghe
      §2.4 — Label cảm thấy sai = bình thường (label luôn mất thông tin)
      §2.5 — Gut feeling = hệ thống đã tính toán xong,
             ý thức chỉ đang bắt kịp
      §2.6 — Thôi thúc mạnh = tín hiệu quan trọng,
             KHÔNG nên bỏ qua cũng KHÔNG nên tuân theo mù quáng
      §2.7 — Pattern lặp = kinh nghiệm đã "ghi sâu",
             thay đổi cần thời gian + kinh nghiệm mới
      §2.8 — Mâu thuẫn nội tâm = 2 lực kéo tự nhiên (thoải mái vs thay đổi),
             KHÔNG phải lỗi, KHÔNG phải yếu đuối

§3  — Ý thức CÓ THỂ làm gì (~100L)
      Khả năng thực tế của ý thức (PFC):

      §3.1 — Giữ chú ý (hold attention) → tín hiệu mờ trở nên rõ hơn
      §3.2 — Đặt mục tiêu (hold goal) → vô thức tự tìm cách thực hiện
      §3.3 — Thử diễn đạt khác (reframe) → xem body phản ứng thế nào
      §3.4 — Tưởng tượng kịch bản (imagine) → body đánh giá từng kịch bản
      §3.5 — Kiểm tra với thực tế (domain-check) → "smooth hay sai?"
      §3.6 — Thay đổi input (change environment) → body-input thay đổi
      §3.7 — Lặp lại (practice) → brain ghi nhớ sâu dần

§4  — Ý thức KHÔNG THỂ làm gì (~80L)
      Giới hạn thực tế — hiểu giới hạn = dùng tốt hơn:

      §4.1 — Không thể cảm nhận trực tiếp
             → phải nhận tín hiệu qua "cầu nối" (feeling)
      §4.2 — Không thể ép bản thân khi tín hiệu quá mạnh
             → đói cực → ăn ngấu, crush → ấp úng = BÌNH THƯỜNG
      §4.3 — Không thể ghi nhớ sâu bằng ý chí
             → phải lặp lại + ngủ đủ, ý chí chỉ giữ hướng
      §4.4 — Không thể biết hết body đang tính gì
             → ~95% xử lý là vô thức, ý thức chỉ thấy ~5%
      §4.5 — Không thể điều khiển chi tiết hành động
             → ý thức giữ "viết chữ X" → tay tự gõ phím

§5  — Các pattern phổ biến (~100L)
      Observable patterns mọi người thường gặp:

      §5.1 — Chu kỳ học: khó chịu → lặp lại + ngủ → tự nhiên hơn
      §5.2 — Quen dần (hedonic treadmill): mới = hay → quen = bình thường → cần mới hơn
      §5.3 — Chuyên gia linh cảm: "tôi biết nhưng không giải thích được"
             = brain đã ghi nhớ rất nhiều, ý thức chỉ thấy kết quả
      §5.4 — Kiệt sức (burnout): nỗ lực nhiều, return về ít → brain báo dừng
      §5.5 — "À ha!" moment: các mảnh kiến thức bỗng nối lại → reward mạnh
      §5.6 — Ảnh hưởng ngầm (background): mood/bias kéo dài
             mà không rõ nguồn → kinh nghiệm cũ đang ảnh hưởng ngầm
      §5.7 — Xung đột pattern: muốn 2 thứ mâu thuẫn cùng lúc
             → 2 bộ kinh nghiệm kéo 2 hướng
      §5.8 — Schema override: "biết sai nhưng vẫn tin"
             → kinh nghiệm cũ mạnh hơn logic mới, cần thời gian + kinh nghiệm thay thế

§6  — Làm việc với hệ thống (~100L)
      Không phải hướng dẫn "sống đúng cách" — là mô tả NGUYÊN TẮC HOẠT ĐỘNG
      để mỗi người tự áp dụng:

      §6.1 — Tin tín hiệu body ở giai đoạn trước khi label
             (label thêm → mất thông tin thêm)
      §6.2 — Khi rối: thay đổi input (đi ra ngoài, nói chuyện, làm việc khác)
             thay vì phân tích nội tâm mãi
      §6.3 — Ngủ = xử lý, không chỉ nghỉ ngơi
             → brain sắp xếp lại kinh nghiệm trong giấc ngủ
      §6.4 — Trải nghiệm = con đường DUY NHẤT để ghi nhớ sâu
             → đọc/nghe = hiểu, nhưng chưa "biết thật" cho tới khi trải nghiệm
      §6.5 — Phản ứng của người khác = kinh nghiệm CỦA HỌ
             → không phải lỗi của bạn (cũng không nên mặc kệ)
      §6.6 — "Lười" thường = mục tiêu sai, không phải ý chí yếu
             → body không thấy mục tiêu này kết nối với nhu cầu thật
      §6.7 — Thay đổi pattern cũ: xây pattern MỚI cạnh tranh
             → không thể "xóa" kinh nghiệm cũ, chỉ có thể xây mạnh hơn
      §6.8 — Giới hạn tự hiểu: nhiều thứ cần người khác hoặc AI hỗ trợ
             → "không ai là bác sĩ của chính mình" hoàn toàn

§7  — Quan hệ với 2 bản đồ kia + Cross-references (~40L)
      "Nếu muốn hiểu TẠI SAO → Core-Software.md
       Nếu muốn verify VỚI NGHIÊN CỨU → Core-Hardware.md
       File này = đủ để QUAN SÁT + TƯƠNG TÁC"
```

**Ước lượng:** ~600-800 dòng

### §6.5 NỘI DUNG MỚI vs tổng hợp từ existing files

```
NỘI DUNG MỚI (viết từ đầu):
  - §0 framing "file này dành cho ai"
  - §1 observable patterns (rewrite từ góc observer)
  - §2 practical meanings (rewrite từ góc observer)
  - §3 ý thức CÓ THỂ (rewrite PFC capabilities)
  - §4 ý thức KHÔNG THỂ (rewrite PFC limits)
  - §5 common patterns (rewrite từ góc observer)
  - §6 working principles (synthesis từ nhiều file)

TỔNG HỢP/DỊCH TỪ (tham khảo, KHÔNG copy):
  - Software Map §5 (Feeling) → §1, §2
  - Software Map §6 (PFC) → §3, §4
  - FLT v1.1 (training) → §6.1, §6.4
  - Logic-Feeling-Balance (meta-principle) → §6.1, §6.2
  - SAL (articulation) → §6.8
  - Body-Personal-Optimization → §6 general
  - AI-Schema-Detection §7 (self-drill) → §6.8
  - Background-Pattern (invisible bias) → §5.6, §6.7
```

### §6.6 Files cần đọc trước khi triển khai Phase 3

- [ ] Core-Software.md (vừa hoàn thành) — source of truth
- [ ] Core-Hardware.md (vừa hoàn thành) — cross-reference
- [ ] Feeling-Literacy-Training.md §3, §5 — training perspective
- [ ] Logic-Feeling-Balance.md §1-§3 — meta-principle
- [ ] Somatic-Articulation-Loop.md §2, §6 — articulation insight
- [ ] Background-Pattern.md §9-§10 — invisible bias, competing pattern
- [ ] AI-Schema-Detection.md §7 — self-drill guardrails
- [ ] Ask-AI/Ask-AI.md — translation layer reference
- [ ] Body-Personal-Optimization.md (backup) — existing observer content

### §6.7 Quality checklist Phase 3

- [ ] KHÔNG có jargon mechanism (chunk, compile, VTA, delta rule, spreading activation)
- [ ] Mọi concept đều diễn đạt bằng ngôn ngữ trải nghiệm
- [ ] Đọc được KHÔNG cần Software hay Hardware
- [ ] KHÔNG prescriptive — mô tả nguyên tắc, không ra lệnh
- [ ] Descriptive, không clinical
- [ ] Consistent với Software Map (cùng truth, khác ngôn ngữ)
- [ ] Mỗi mục có: observable pattern + ý nghĩa + khả năng tương tác
- [ ] Cross-references tới 2 file kia cho người muốn đi sâu hơn

---

## §7 — PHASE 4: CROSS-REFERENCE UPDATES

### §7.1 Files tham chiếu tới Core-v7.8-Draft.md

Cần scan và update references trong các file:
- [ ] 01-File-Index.md — thêm 3 file mới, bỏ Core-v7.8-Draft entry
- [ ] Các file Core-Deep-Dive reference "Core-v7.8-Draft.md" → update
- [ ] Metadata trong các file mechanism (Chunk.md, Body-Feedback.md, Feeling.md,...)
- [ ] plan-update-v8.md — update status

### §7.2 Scope

Phase 4 có thể scan nhanh bằng grep "Core-v7.8" trong toàn bộ framework.
Thay đổi nhỏ — chủ yếu rename references.

---

## §8 — RỦI RO VÀ MITIGATION

| Rủi ro | Mức | Mitigation |
|---|---|---|
| Interface Map trở thành simplified Software | CAO | §6.2 nguyên tắc + §6.3 so sánh. Luôn check: "observer CÓ NGHĨ như vậy không?" |
| Interface Map trở nên prescriptive | TRUNG BÌNH | §6.2 nguyên tắc #4 + #5. Mô tả công cụ, không ra lệnh |
| Software restructure mất content | THẤP | Backup ở _backup/. Checklist §4.6 |
| Cross-references outdated | THẤP | Phase 4 grep scan |
| File quá dài | TRUNG BÌNH | Target: Hardware ~300L, Software ~1000L, Interface ~700L |

---

## §9 — MEMORY UPDATE NEEDED

Sau khi plan hoàn thành, update MEMORY.md:
- [ ] Thêm entry cho project Core 3-Maps restructure
- [ ] Link tới plan file này

---

## §10 — TỔNG KẾT

```
HIỆN TẠI:
  Core-v7.8-Draft.md (1,470L) = 2 maps in 1 file, thiếu observer view

MỤC TIÊU:
  Core-Hardware.md  (~300-400L)  = CÁI GÌ ở ĐÂU (cho chuyên gia)
  Core-Software.md  (~900-1100L) = CHẠY THẾ NÀO (cho researcher)
  Core-Interface.md (~600-800L)  = QUAN SÁT + TƯƠNG TÁC (cho mọi người)

THỨ TỰ:
  Phase 0: Backup
  Phase 1: Software (restructure, nặng nhất)
  Phase 2: Hardware (extract, nhẹ nhất)
  Phase 3: Interface (viết mới, novel nhất)
  Phase 4: Cross-references

MỖI SESSION 1 FILE. CHẬM MÀ CHẮC.
```
