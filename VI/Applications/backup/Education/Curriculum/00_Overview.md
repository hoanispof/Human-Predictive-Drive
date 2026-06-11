# Kiến Trúc Chương Trình Học — Tổng Quan

> **Phiên bản:** 5.5
> **Prerequisite:** Core.md (§8 Mô Hình Vuông, §8.2 Depth Composite, §8.9 Chunk Topology),
> Applications/Education.md (§5 Chunk Topology, §6 Depth = Learning Stages),
> Applications/Education/00_Overview.md (§1 Reframe, §2 Nguyên Lý, §5 Gợi ý sơ bộ).
> **File này:** Tổng quan kiến trúc chương trình học qua framework lens.
> Mỗi phần chính = 1 file chi tiết riêng (sẽ xây dần).
>
> **Câu hỏi gốc:** "Kiến thức nền tảng mà hầu hết học sinh nên biết là gì?
> Kiến trúc chương trình học tổng thể nên thiết kế như thế nào?"
>
> **⚠️ QUY ƯỚC ĐỌC (v5.5):**
> Soldier, Architect, Improviser, Drifter = 4 NHÃN MÔ TẢ, KHÔNG phải 4 kiểu người.
> CƠ CHẾ = predictive-chunk configuration (source × depth per domain).
>
> **Quy ước:** 🟢 Nghiên cứu/dữ liệu | 🟡 Suy luận từ framework | 🔴 Giả thuyết

---

## Mục Lục

1. [Reframe: Chương Trình Học = Nguyên Liệu Cho Chunk Building](#1-reframe)
2. [Kiến Trúc Phân Tầng — 3+1 Tầng Kiến Thức](#2-phân-tầng)
3. [Tầng Nền Tảng — Kiến Thức Ai Cũng Cần](#3-nền-tảng)
4. [Tầng Khám Phá — Exposure Đa Domain](#4-khám-phá)
5. [Tầng Chuyên Sâu — Per Profile Pathway](#5-chuyên-sâu)
6. [Tầng Xuyên Suốt — Convergence & Meta-Cognition](#6-xuyên-suốt)
7. [Tái Cấu Trúc Môn Học — Gộp/Tách/Thêm/Bỏ](#7-tái-cấu-trúc)
8. [Phân Bổ Per Giai Đoạn Phát Triển](#8-per-giai-đoạn)
9. [So Sánh Với Chương Trình Hiện Tại (VN)](#9-so-sánh)
10. [File Map + Lộ Trình](#10-file-map)

---

## 1. Reframe: Chương Trình Học = Nguyên Liệu Cho Chunk Building

### 1.1 Từ "Dạy Kiến Thức" Sang "Thiết Kế Nguyên Liệu Chunk"

🟡

```
HIỂU TRUYỀN THỐNG:
  Chương trình học = DANH SÁCH kiến thức phải dạy
  → "Toán lớp 6 gồm: phân số, số thập phân, hình học cơ bản,..."
  → Thầy TRUYỀN → trò NHỚ → thi KIỂM TRA nhớ đúng không
  → Metric: coverage (dạy HẾT chương trình = thành công)

REFRAME QUA FRAMEWORK:
  Chương trình học = NGUYÊN LIỆU + TRÌNH TỰ cho chunk building
  → Kiến thức = raw material. MỤC TIÊU = chunks hình thành ở trẻ
  → Cùng nguyên liệu (phân số) nhưng CÁCH BUILD khác per profile
  → Metric: depth (chunks ĐÃ HÌNH THÀNH ở stage nào?)

  Applications/Education/00_Overview.md §1.1:
    "Kiến thức = NGUYÊN LIỆU cho chunks, không phải mục tiêu.
     Mục tiêu = con người có chunk config tối ưu per hardware."

KHÁC BIỆT THỰC TẾ:
  Truyền thống: "Dạy HẾT 12 chương" = thành công (dù trẻ quên 80%)
  Framework: "Trẻ BUILD được chunks Stage 2 ở 4 chương quan trọng"
             = thành công (dù chưa "cover" hết chương trình)

  → CHẤT LƯỢNG chunk > SỐ LƯỢNG kiến thức
  → Ít hơn nhưng sâu hơn > nhiều hơn nhưng nông
  → Finland đã chứng minh: ít homework, ít giờ học, PISA vẫn cao
    (00_Overview.md §9.5: depth reward Stage 2 = 8/10)
```

### 1.2 Criteria Chọn Kiến Thức — Framework Lens

🟡

```
CÂU HỎI CỐT LÕI: Kiến thức NÀO nên nằm trong chương trình?

CRITERIA TRUYỀN THỐNG (ẩn, không nói ra):
  ① "Truyền thống dạy gì thì tiếp tục dạy" (inertia)
  ② "Chuyên gia môn nào thì muốn dạy SÂU môn đó" (expert bias)
  ③ "Thi gì thì dạy đó" (test-driven)
  ④ "Nước khác dạy gì thì mình cũng dạy" (copy)
  → Kết quả: chương trình PHÌNH TO qua thập kỷ, ít khi BỎ, chỉ THÊM

CRITERIA FRAMEWORK — 4 câu hỏi per kiến thức:

  ❶ CHUNKS NÀO CUỘC SỐNG CẦN?
     "Nếu THIẾU chunk này → gặp vấn đề ở BẤT KỲ career/life path nào"
     → VÀO tầng NỀN TẢNG (ai cũng học)
     VD: literacy, numeracy, emotional regulation = AI CŨNG CẦN
     VD: chi tiết Hóa hữu cơ = CHỈ CẦN nếu theo ngành Hóa

  ❷ CHUNKS NÀO GIÚP NHẬN DIỆN KÊNH GỐC?
     "Kiến thức này cho trẻ EXPOSURE domain mới → PE lộ → kênh gốc lộ"
     → VÀO tầng KHÁM PHÁ (ai cũng trải nghiệm, nhưng không ép sâu)
     VD: thí nghiệm Hóa cơ bản = exposure (PE từ visual, surprise)
     VD: nhạc cụ, vẽ, code, thể thao = exposure kênh gốc tiềm năng

  ❸ CHUNKS NÀO XÂY DEPTH PER PROFILE?
     "Kiến thức này ĐÀO SÂU domain mà trẻ đã match hardware"
     → VÀO tầng CHUYÊN SÂU (per profile, tự chọn + guidance)
     VD: Hóa nâng cao cho trẻ match Hóa. Toán nâng cao cho trẻ match Toán.

  ❹ CHUNKS NÀO TẠO CONVERGENCE?
     "Kiến thức này = foundation chunk SHARED nhiều domain"
     → VÀO tầng XUYÊN SUỐT (xuyên môn, không phải môn riêng)
     VD: modeling, pattern recognition, systems thinking, logic

  → Kiến thức KHÔNG trả lời được CÂU NÀO trong 4 câu trên = LOẠI BỎ
  → Đây là cách "giảm tải" có CƠ SỞ, không phải "bỏ bừa"
```

---

## 2. Kiến Trúc Phân Tầng — 3+1 Tầng Kiến Thức

### 2.1 Tổng Quan Phân Tầng

🟡

```
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐   ║
║  │         TẦNG XUYÊN SUỐT: CONVERGENCE                       │   ║
║  │  Pattern recognition, Modeling, Systems thinking,           │   ║
║  │  Meta-cognition, Logic                                      │   ║
║  │  → KHÔNG phải môn riêng — xuyên suốt mọi tầng              │   ║
║  └────────────────────────────┬────────────────────────────────┘   ║
║                               │ (permeate)                         ║
║  ┌────────────────────────────▼────────────────────────────────┐   ║
║  │                                                             │   ║
║  │  TẦNG 3: CHUYÊN SÂU (per profile, per kênh gốc)            │   ║
║  │  Depth Stage 3-4. Tự chọn + guidance. ~30-50% thời lượng    │   ║
║  │  (tỉ lệ TĂNG DẦN theo tuổi: 0% ở tiểu học → 50% ở THPT)  │   ║
║  │                                                             │   ║
║  ├─────────────────────────────────────────────────────────────┤   ║
║  │                                                             │   ║
║  │  TẦNG 2: KHÁM PHÁ (exposure đa domain, tìm kênh gốc)      │   ║
║  │  Depth Stage 1-2. Rotation + hands-on. ~20-40% thời lượng   │   ║
║  │  (tỉ lệ GIẢM DẦN theo tuổi: 40% ở tiểu học → 10% ở THPT) │   ║
║  │                                                             │   ║
║  ├─────────────────────────────────────────────────────────────┤   ║
║  │                                                             │   ║
║  │  TẦNG 1: NỀN TẢNG (ai cũng cần, 100% học sinh)             │   ║
║  │  Depth Stage 2+. Core skills + knowledge. ~40-50% thời lượng│   ║
║  │  (tỉ lệ ỔN ĐỊNH, giảm nhẹ theo tuổi khi foundation xong)  │   ║
║  │                                                             │   ║
║  └─────────────────────────────────────────────────────────────┘   ║
║                                                                   ║
║  → Đọc từ dưới lên: Tầng 1 = nền → Tầng 2 = explore → Tầng 3    ║
║  → Tầng xuyên suốt KHÔNG đứng riêng, nó THẨM THẤU qua 3 tầng   ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 2.2 Logic Phân Tầng — Tại Sao 3+1?

🟡

```
CƠ SỞ FRAMEWORK:

  Core.md §8.2 — Depth composite:
    Chunks cần BUILD THEO THỨ TỰ: quality → connectivity → cluster → maturity
    → Không thể jump Stage 3 mà bỏ Stage 1-2
    → Tầng 1 (foundation, Stage 2) TRƯỚC → Tầng 3 (depth, Stage 3-4) SAU

  Core.md §8.9 — Chunk Topology:
    Convergence = shared abstract chunks cross-domain
    → Convergence KHÔNG PHẢI MÔN RIÊNG — nó là THUỘC TÍNH của chunk topology
    → Dạy convergence = dạy ở mức abstraction CAO trong MỌI MÔN
    → → "Tầng xuyên suốt" (không đứng riêng)

  Applications/Education/00_Overview.md §1.5 — 5 giai đoạn phát triển:
    2-6: exposure → kênh gốc lộ = Tầng 2
    6-12: foundation building = Tầng 1
    12-18: depth per match = Tầng 3
    → 3 tầng kiến thức MAP với 3 giai đoạn phát triển

TẠI SAO KHÔNG 2 TẦNG? 5 TẦNG?:
  2 tầng (nền + chuyên sâu) = THIẾU tầng Khám Phá
    → Trẻ chưa biết match ở đâu → ép chọn chuyên sâu sớm = đoán mò
  5 tầng = quá chi tiết → khó triển khai, boundary mờ
  3+1 = đủ để address 3 bài toán riêng biệt + convergence xuyên suốt

NGUYÊN LÝ: Trẻ nào cũng đi qua cả 3 tầng, nhưng:
  TỈ LỆ THỜI LƯỢNG thay đổi per tuổi + per profile
  Không phải "xong Tầng 1 rồi mới bắt đầu Tầng 2"
  → 3 tầng ĐỒNG THỜI, chỉ khác TỈ LỆ
```

### 2.3 Tỉ Lệ Thay Đổi Per Giai Đoạn

🟡

```
PHÂN BỔ THỜI LƯỢNG ƯỚC LƯỢNG:

  Giai đoạn     Tầng 1 (Nền)  Tầng 2 (Explore)  Tầng 3 (Depth)  Xuyên suốt
  ────────────────────────────────────────────────────────────────────────────
  2-6 tuổi      ~30%          ~60%               ~0%             ~10%
  6-9 tuổi      ~50%          ~35%               ~5%             ~10%
  9-12 tuổi     ~45%          ~25%               ~15%            ~15%
  12-15 tuổi    ~35%          ~15%               ~30%            ~20%
  15-18 tuổi    ~25%          ~10%               ~45%            ~20%
  18+ (ĐH)     ~10%          ~5%                ~65%            ~20%

  ⚠️ Tỉ lệ = ước lượng sơ bộ, cần calibrate per context.
  Xuyên suốt = KHÔNG riêng biệt, nó EMBED trong cả 3 tầng.
  % xuyên suốt = thời gian EXPLICIT cho cross-domain activities.

TREND:
  Tầng 1: giảm dần (foundation xong → maintenance)
  Tầng 2: giảm dần (kênh gốc đã lộ → ít cần explore thêm)
  Tầng 3: tăng dần (match đã rõ → depth tăng)
  Xuyên suốt: tăng dần (cần depth TRƯỚC mới convergence được)
```

---

## 3. Tầng Nền Tảng — Kiến Thức Ai Cũng Cần

> **File chi tiết:** `01_Foundation-Knowledge.md`
> **Đây là phần QUAN TRỌNG NHẤT — kiến thức nền quyết định "sàn" của toàn dân.**

### 3.1 Định Nghĩa Tầng Nền Tảng

🟡

```
TIÊU CHÍ VÀO TẦNG NỀN:
  Chunk này THIẾU → gặp vấn đề ở BẤT KỲ career path / life path nào
  → "Dù làm bác sĩ, thợ điện, nghệ sĩ, hay lập trình viên — đều CẦN"
  → Nếu chỉ cần cho 1 career path = KHÔNG phải nền tảng → Tầng 3

DEPTH TARGET: Stage 2 ("hiểu tại sao")
  → Tầng Nền KHÔNG cần Stage 3-4 (hệ thống, transfer) — đó là Tầng 3
  → Nhưng PHẢI vượt Stage 1 ("nhớ đúng") — nhớ mà không hiểu = quên
  → Stage 2 = hiểu đủ để DÙNG trong cuộc sống, không cần expert

PHÂN BIỆT NỀN TẢNG vs CHUYÊN SÂU:
  Toán: cộng trừ nhân chia, phân số, %, đồ thị cơ bản = NỀN TẢNG
  Toán: vi tích phân, đại số tuyến tính = CHUYÊN SÂU (chỉ ngành cần)
  Hóa: nguyên tử, phản ứng cơ bản, an toàn hóa chất = NỀN TẢNG
  Hóa: cân bằng oxi hóa khử nâng cao = CHUYÊN SÂU
  → Ranh giới = "cuộc sống thường ngày CẦN không?"
```

### 3.2 7 Nhóm Kiến Thức Nền Tảng

🟡

```
NHÓM 1 — NGÔN NGỮ & GIAO TIẾP (Language & Communication):
  ① Đọc hiểu: đọc và HIỂU văn bản đa dạng (tin tức, hợp đồng, hướng dẫn,...)
  ② Viết: diễn đạt ý rõ ràng bằng văn bản (email, báo cáo, đơn từ,...)
  ③ Nói/nghe: trình bày ý kiến, nghe hiểu, thảo luận
  ④ Ngoại ngữ: ít nhất 1 (tiếng Anh = thực tế nhất cho global access)
  → Depth target: Stage 2 (hiểu ngữ cảnh, sắc thái, không chỉ từ vựng)
  → Framework lens: literacy = FOUNDATION CHUNK cho MỌI domain khác
     Thiếu literacy → chunks MỌI domain bị chặn (không đọc được = không học được)

NHÓM 2 — TƯ DUY SỐ & LOGIC (Numeracy & Logical Thinking):
  ① Số học: 4 phép tính, phân số, %, tỉ lệ
  ② Thống kê cơ bản: trung bình, xác suất cơ bản, đọc biểu đồ
  ③ Hình học thực tế: đo đạc, diện tích, thể tích (đời thường)
  ④ Logic: suy luận, "nếu A thì B", phát hiện ngụy biện
  ⑤ Ước lượng: "con số này hợp lý không?" (Fermi estimation)
  → Depth target: Stage 2 (hiểu TẠI SAO, không chỉ tính đúng)
  → Framework lens: numeracy + logic = PREDICTION ENGINE cơ bản
     "Đoán xem kết quả hợp lý không" = chunk prediction ở mức số

NHÓM 3 — TƯ DUY KHOA HỌC (Scientific Thinking):
  ① Phương pháp khoa học: quan sát → giả thuyết → thí nghiệm → kết luận
  ② Nhân quả vs tương quan: "A xảy ra cùng B ≠ A GÂY RA B"
  ③ Khoa học tự nhiên cơ bản: vật lý (lực, năng lượng), hóa (chất, phản ứng),
     sinh (cơ thể, hệ sinh thái) — ở mức NGUYÊN LÝ, không chi tiết
  ④ Tư duy phản biện: đánh giá evidence, phân biệt quan điểm vs sự kiện
  → Depth target: Stage 2 (hiểu NGUYÊN LÝ, không nhớ chi tiết)
  → Framework lens: scientific thinking = META-CHUNK
     "Tôi KHÔNG CHẮC → tôi KIỂM TRA → tôi CẬP NHẬT" = prediction error loop
     = CƠ CHẾ CỐT LÕI của framework, dạy thành skill = dạy prediction engine

NHÓM 4 — HIỂU BẢN THÂN & CẢM XÚC (Emotional & Self Literacy):
  ① Nhận diện cảm xúc: "Tôi đang cảm thấy gì? Tại sao?"
  ② Quản lý cảm xúc cơ bản: cortisol ↑ → nhận biết → hạ (breathing, break,...)
  ③ Hiểu stress: "Áp lực vừa = tốt. Quá nhiều = PFC tắt." (inverted-U đơn giản)
  ④ Self-awareness cơ bản: "Tôi thích gì? Tôi giỏi gì? Tôi cần gì?"
  ⑤ Empathy cơ bản: "Người khác có cảm xúc KHÁC tôi = BÌNH THƯỜNG"
  → Depth target: Stage 2 (hiểu cơ chế, không chỉ "phải kiểm soát")
  → Framework lens: emotional literacy = TRỰC TIẾP từ framework
     Cortisol inverted-U, PE sensitivity, schema — dạy VERSION ĐƠN GIẢN
     = Trẻ hiểu CƠ CHẾ cảm xúc → tự calibrate → self-management
  → ⚠️ HIỆN TẠI: hầu hết hệ thống giáo dục KHÔNG DẠY hoặc dạy ở mức "đạo đức"
     "Phải ngoan, phải kiểm soát" = Stage 0 (ép behavior, không hiểu cơ chế)

NHÓM 5 — TÀI CHÍNH & KINH TẾ CƠ BẢN (Financial Literacy):
  ① Tiền: thu nhập, chi tiêu, tiết kiệm, nợ — cơ bản
  ② Lãi suất: "vay = trả nhiều hơn", lãi kép
  ③ Rủi ro: "đầu tư có thể MẤT", diversification cơ bản
  ④ Thuế: cơ bản (tại sao thuế tồn tại, thuế hoạt động thế nào)
  ⑤ Giá trị lao động: "thời gian = tài nguyên", opportunity cost
  → Depth target: Stage 2 (hiểu cơ chế, không chỉ "phải tiết kiệm")
  → Framework lens: financial literacy = PREDICTION về tương lai tài chính
     Thiếu chunks này → prediction tài chính SAI → cortisol mãn tính khi trưởng thành
  → ⚠️ HIỆN TẠI: hầu hết hệ thống giáo dục KHÔNG DẠY
     Kết quả: người trưởng thành không hiểu lãi kép, nợ, đầu tư = "mù tài chính"

NHÓM 6 — SỨC KHỎE & CƠ THỂ (Health Literacy):
  ① Cơ thể: các hệ cơ quan cơ bản, tại sao cơ thể hoạt động thế
  ② Dinh dưỡng: macro/micro nutrients, "ăn gì và tại sao"
  ③ Giấc ngủ: tại sao ngủ quan trọng, sleep hygiene cơ bản
  ④ Vận động: tại sao cần exercise, cơ chế cơ bản
  ⑤ Sức khỏe tâm thần: stress, anxiety, depression — nhận biết + cầu cứu
  ⑥ Sức khỏe sinh sản: cơ bản, evidence-based, không taboo
  → Depth target: Stage 2 (hiểu TẠI SAO, không chỉ "phải tập thể dục")
  → Framework lens: health = HARDWARE MAINTENANCE
     Framework nói hardware = nền tảng mọi thứ. Hiểu hardware = tối ưu hardware.
     Trẻ hiểu "ngủ ít → cortisol ↑ → PFC ↓ → học kém" = TỰ QUẢN LÝ
  → ⚠️ HIỆN TẠI: dạy rời rạc (Sinh học + Thể dục), thiếu integration

NHÓM 7 — KỸ NĂNG SỐ & CÔNG NGHỆ (Digital Literacy):
  ① Sử dụng công cụ số: máy tính, internet, ứng dụng cơ bản
  ② An toàn số: privacy, password, scam, misinformation
  ③ Tư duy thuật toán: "chia bài toán thành bước" (không cần code)
  ④ AI literacy: AI là gì, AI làm được/không làm được gì, dùng AI thế nào
  ⑤ Media literacy: phân biệt tin thật/giả, manipulation, filter bubble
  → Depth target: Stage 2 (hiểu cơ chế, không chỉ "biết dùng")
  → Framework lens: digital = ENVIRONMENT mới, cần chunks navigate
     Thiếu → bị manipulate (misinformation, scam, addiction)
     Thừa (flooding) → dopamine hijack → threshold ↑ → "chán mọi thứ"
  → ⚠️ Đang thay đổi NHANH → cần update liên tục (khác các nhóm khác)
```

### 3.3 Cái THIẾU Lớn Nhất Của Hệ Thống Hiện Tại

🟡

```
HIỆN TẠI DẠY TỐT (Nhóm 1-3 một phần):
  ✅ Ngôn ngữ: đọc viết cơ bản (nhưng thiếu critical reading)
  ✅ Số học: tính toán cơ bản (nhưng quá nặng chi tiết, thiếu ước lượng)
  ✅ Khoa học: kiến thức cơ bản (nhưng Stage 1 thuần, thiếu scientific thinking)

HIỆN TẠI THIẾU NGHIÊM TRỌNG (Nhóm 4-7):
  ❌ Nhóm 4 — Emotional Literacy: GẦN NHƯ KHÔNG CÓ
     GDCD dạy "đạo đức" (ép behavior) chứ không dạy "cơ chế cảm xúc"
     → Kết quả: người trưởng thành không biết TẠI SAO mình stress
  ❌ Nhóm 5 — Financial Literacy: KHÔNG CÓ
     → Kết quả: "mù tài chính" ở đa số dân số
  ❌ Nhóm 6 — Health Literacy: RỜI RẠC
     Sinh học dạy cơ thể (Stage 1). Thể dục = tập nhưng không giải thích.
     Sức khỏe tâm thần = TABOO.
     → Kết quả: không hiểu tại sao ngủ quan trọng, ăn gì tốt
  ❌ Nhóm 7 — Digital Literacy: LẠC HẬU
     Dạy "tin học" = dùng Word/Excel (skill cụ thể, không phải literacy)
     AI literacy = chưa có. Media literacy = chưa có.

HIỆN TẠI DẠY NHƯNG SAI TẦNG (nằm ở Nền nhưng nên ở Chuyên sâu):
  ⚠️ Hóa học chi tiết (cân bằng phương trình phức tạp)
     → 90% không bao giờ dùng → nên ở Tầng 3 (per profile)
  ⚠️ Vật lý chi tiết (điện trường, từ trường nâng cao)
     → 90% không bao giờ dùng → nên ở Tầng 3
  ⚠️ Sinh học chi tiết (chu trình Krebs, di truyền Mendel nâng cao)
     → 90% không bao giờ dùng → nên ở Tầng 3
  ⚠️ Toán nâng cao (giải tích, lượng giác nâng cao)
     → 80% không bao giờ dùng → nên ở Tầng 3
  → "QUÁ NẶNG" = vấn đề phân tầng SAI, không phải "kiến thức xấu"
     Kiến thức không sai — nó chỉ KHÔNG PHẢI NỀN TẢNG cho TẤT CẢ

→ Chi tiết phân tích per nhóm → 01_Foundation-Knowledge.md
```

---

## 4. Tầng Khám Phá — Exposure Đa Domain

🔴 *Ghi chú overview — file chi tiết sẽ xây sau*

```
MỤC ĐÍCH:
  Cho trẻ TRẢI NGHIỆM đủ domains để kênh gốc LỘ
  → "Trẻ nào match Hóa? Trẻ nào match Nhạc? Trẻ nào match Code?"
  → KHÔNG THỂ BIẾT nếu không cho THỬ

NGUYÊN LÝ:
  ① Exposure ≠ ép học: cho thử, KHÔNG ép sâu
     → PE lộ tự nhiên: trẻ hứng thú ở domain nào?
  ② Rotation: mỗi kỳ thử domain mới
     → Giảm Habituation Blindness (PE > 0 từ novelty)
  ③ Hands-on > lý thuyết:
     → Exposure qua LÀM (thí nghiệm, project, trải nghiệm)
     → Không qua ĐỌC/NGHE (nông, PE thấp, không lộ kênh gốc)
  ④ Quan sát PE indicator:
     → Giáo viên/phụ huynh quan sát: trẻ hứng thú ở đâu?
     → Data cho Tầng 1 (Nhận diện) — link sang Assessment

DOMAINS CẦN EXPOSURE:
  Sciences (Toán, Lý, Hóa, Sinh — ở mức trải nghiệm)
  Arts (Nhạc, Mỹ thuật, Kịch, Sáng tạo)
  Technology (Code cơ bản, Chế tạo, Digital creation)
  Social (Lịch sử qua storytelling, Địa lý qua explore)
  Physical (Thể thao đa dạng, Võ thuật, Nhảy)
  Nature (Thiên nhiên, Sinh thái, Nông nghiệp trải nghiệm)
  → Mỗi domain = 1 "cửa sổ" để kênh gốc LỘ

DEPTH TARGET: Stage 1-2 (biết + bắt đầu hiểu)
  → KHÔNG cần Stage 3-4 ở tầng này
  → Ép depth sâu ở tầng Khám Phá = KILL PE = ngược mục đích

→ Chi tiết → file riêng (sẽ xây sau)
```

---

## 5. Tầng Chuyên Sâu — Per Profile Pathway

🔴 *Ghi chú overview — file chi tiết sẽ xây sau*

```
MỤC ĐÍCH:
  Trẻ đã nhận diện domain match → ĐÀO SÂU
  → Depth Stage 3-4 (hệ thống + transfer)
  → Per profile: khác pathway, khác pace, khác format

NGUYÊN LÝ:
  ① Match TRƯỚC, depth SAU:
     → Không ép depth ở domain mismatch (= cortisol, PE âm)
     → Depth ở domain match = PE TỰ NHIÊN = chunks build nhanh
  ② Guidance, không ép:
     → Dựa trên nhận diện (Tầng 1) + PE indicators
     → Trẻ CHỌN + giáo viên GUIDE (không phải trẻ chọn bừa cũng ko giáo viên ép)
  ③ Per profile pathway:
     → External: structure rõ → depth dần (Soldier-Deep pathway)
     → Internal-deep: autonomy + "tại sao" → depth tự nhiên (Architect pathway)
     → Internal-explore: variety + depth selected → cross-domain (Improviser pathway)
     → Drifter: support + exposure tiếp → tìm match trước rồi depth sau

DEPTH TARGET: Stage 3-4 (hệ thống + transfer)
  → Đây là mục tiêu CUỐI CÙNG của giáo dục
  → "Expert = Stage 4 ở ít nhất 1 domain"

→ Liên quan chặt: Applications/Education/00_Overview.md §6 (Per Profile)
→ Chi tiết → file riêng (sẽ xây sau)
```

---

## 6. Tầng Xuyên Suốt — Convergence & Meta-Cognition

🔴 *Ghi chú overview — file chi tiết sẽ xây sau*

```
MỤC ĐÍCH:
  Xây FOUNDATION CHUNKS shared cross-domain
  → Convergence = shared abstract chunks → transfer TỰ NHIÊN
  → Meta-cognition = hiểu CÁCH MÌNH HỌC → self-calibrate

NGUYÊN LÝ:
  ① Không phải môn riêng — EMBED trong mọi môn:
     → Toán dạy modeling → Lý cũng dạy modeling → "ĐÂY LÀ CÙNG SKILL"
     → Giáo viên EXPLICIT link: "pattern này GIỐNG pattern hôm qua ở môn X"
  ② Cần depth TRƯỚC mới convergence:
     → Thứ tự: depth per domain → thấy pattern chung → convergence emerge
     → Cross-domain project mà mỗi domain nông = "nồi lẩu", không convergence
  ③ Meta-cognition = skill QUAN TRỌNG NHẤT không ai dạy:
     → "Tôi học kiểu nào tốt nhất?" (PE modality awareness)
     → "Tôi đang ở stage nào?" (self-assessment)
     → "Tôi cần gì để lên stage tiếp?" (self-directed growth)
     → = Framework VERSION ĐƠN GIẢN cho học sinh

5 CONVERGENCE SKILLS:
  ① Pattern Recognition: nhận ra pattern CHUNG giữa domains
  ② Modeling: mô hình hóa bài toán (abstract representation)
  ③ Systems Thinking: nhìn tổng thể, hiểu quan hệ giữa parts
  ④ Logic & Reasoning: suy luận, chứng minh, phát hiện lỗi
  ⑤ Meta-cognition: hiểu process HỌC của chính mình

→ Liên quan: Applications/Education.md §5 (Chunk Topology)
→ Chi tiết → file riêng (sẽ xây sau)
```

---

## 7. Tái Cấu Trúc Môn Học — Gộp/Tách/Thêm/Bỏ

🔴 *Ghi chú overview — file chi tiết sẽ xây sau*

```
ĐÂY LÀ PHẦN CẦN PHÂN TÍCH SÂU NHẤT — mỗi thay đổi ảnh hưởng toàn system.

GỢI Ý SƠ BỘ (từ Education/00_Overview.md §5.3):

  GỘP TIỀM NĂNG (shared foundation chunks):
    Toán + Lý + Hóa → "Sciences & Modeling"
    Sử + Địa + GDCD → "Human Systems"
    Văn + Ngoại ngữ → "Communication"
    → Logic: gộp = EXPLICIT hóa shared foundation → convergence TỰ NHIÊN

  TÁCH TIỀM NĂNG (quá quan trọng để embed):
    Emotional Literacy ← tách khỏi GDCD
    Systems Thinking ← tách khỏi Toán
    Creative Problem-Solving ← tách khỏi Công nghệ

  THÊM MỚI (cuộc sống cần, trường chưa dạy):
    Meta-cognition
    Financial Literacy
    Decision-making
    AI Literacy

  BỎ/GIẢM (sai tầng — chuyển sang Tầng 3):
    Chi tiết Stage 1 ở môn chuyên sâu cho học sinh không theo ngành đó

⚠️ CẨN THẬN:
  Gộp ≠ bỏ subject. Subject vẫn có thể tồn tại BÊN TRONG nhóm gộp.
  → "Sciences & Modeling" vẫn có Toán period, Lý period
  → Nhưng EXPLICIT dạy: "cùng dùng modeling" → convergence

→ Chi tiết per môn → file riêng (sẽ xây sau)
```

---

## 8. Phân Bổ Per Giai Đoạn Phát Triển

🔴 *Ghi chú overview — file chi tiết sẽ xây sau*

```
NGUYÊN LÝ: 7 nhóm nền tảng KHÔNG DẠY ĐỒNG ĐỀU qua mọi tuổi.

PHÂN BỔ SƠ BỘ:

  2-6 TUỔI (Mầm non):
    Focus: Nhóm 1 (ngôn ngữ cơ bản), Nhóm 4 (cảm xúc cơ bản), Nhóm 6 (cơ thể)
    Format: play-based, hands-on, không formal
    → "Học qua chơi" = exposure + foundation chunks tự nhiên

  6-9 TUỔI (Tiểu học đầu):
    Focus: Nhóm 1-2 (đọc viết, số học), Nhóm 3 (quan sát, thí nghiệm đơn giản)
    Bắt đầu: Nhóm 4 (nhận diện cảm xúc có hệ thống), Nhóm 7 (digital cơ bản)
    Format: mixed (structure + exploration)

  9-12 TUỔI (Tiểu học cuối):
    Mở rộng: tất cả 7 nhóm ở mức cơ bản
    Sâu hơn: Nhóm 2 (logic, ước lượng), Nhóm 3 (phương pháp khoa học)
    Bắt đầu: Nhóm 5 (financial literacy cơ bản)
    Format: foundation + bắt đầu explore chuyên sâu

  12-15 TUỔI (THCS):
    Sâu hơn: Nhóm 3 (tư duy phản biện), Nhóm 4 (quản lý stress, self-awareness)
    Mở rộng: Nhóm 5 (tài chính thực tế), Nhóm 7 (AI literacy, media literacy)
    → Puberty = emotional literacy CỰC KỲ QUAN TRỌNG ở giai đoạn này

  15-18 TUỔI (THPT):
    Depth Stage 2: Nhóm 5 (đầu tư, rủi ro), Nhóm 7 (AI application)
    Maintenance: Nhóm 1-3 (đã foundation, giữ + nâng)
    → Focus SHIFT sang Tầng 3 (chuyên sâu per match)

→ Chi tiết per giai đoạn → file riêng (sẽ xây sau)
```

---

## 9. So Sánh Với Chương Trình Hiện Tại (VN)

🔴 *Ghi chú overview — sẽ phân tích sâu khi đủ data*

```
SO SÁNH NHANH:

  Tiêu chí              VN hiện tại              Framework
  ──────────────────────────────────────────────────────────────
  Phân tầng             1 tầng (mọi thứ = nền)   3+1 tầng
  Depth target          Stage 1 (nhớ đúng)        Stage 2+ (hiểu)
  Nhóm 4 (Emotional)    ~0%                       Quan trọng
  Nhóm 5 (Financial)    0%                        Quan trọng
  Nhóm 7 (Digital/AI)   Lạc hậu                   Core skill
  Chi tiết chuyên sâu   Tầng nền (sai tầng)       Tầng 3 (đúng tầng)
  Convergence           ~0                         Tầng xuyên suốt
  Per profile           Không                      Tầng 3
  Tỉ lệ thay đổi       Cố định                    Thay đổi per tuổi
  Metric                Coverage (dạy hết SGK)     Depth (chunks formed)

⚠️ Đây KHÔNG phải "VN tệ" — hầu hết nước đều tương tự.
   Finland gần framework nhất nhưng CŨNG chưa có per-profile đầy đủ.
   VN có advantage: coverage CAO, literacy CAO → nền đã có, cần RESTRUCTURE.
```

---

## 10. File Map + Lộ Trình

### 10.1 File Map

```
Curriculum/
├── 00_Overview.md                 ← FILE NÀY (tổng quan kiến trúc)
├── 01_Foundation-Knowledge.md     → 7 nhóm kiến thức nền — phân tích sâu
│     Per nhóm: chunks cụ thể, depth target, format dạy,
│     so sánh vs hiện tại, evidence nếu có
│     (ƯU TIÊN — xây tiếp theo)
│
├── 02_Subject-Restructure_VN.md        → Gộp/tách/thêm/bỏ per môn (Việt Nam)
│     Per môn GDPT 2018: phân tích giữ/bỏ/chuyển tầng
│     Môn mới: thiết kế chi tiết
│     (Tương lai: _FI, _SG, _JP,... cho quốc gia khác)
│
├── (future) 03_Exploration-Layer.md    → Tầng Khám Phá chi tiết
│     Domains exposure, format rotation, PE tracking
│
├── (future) 04_Per-Stage-Design.md     → Phân bổ per giai đoạn
│     Per giai đoạn: tỉ lệ tầng, focus nhóm, format
│
└── (future) 05_Convergence-Skills.md   → Tầng xuyên suốt chi tiết
      5 convergence skills: dạy thế nào, embed thế nào
```

### 10.2 Lộ Trình Xây Dựng

```
PHASE 1 (hoàn thành):
  ✅ 00_Overview.md — file này

PHASE 2 (tiếp theo):
  □ 01_Foundation-Knowledge.md — 7 nhóm kiến thức nền, phân tích sâu
    → Ưu tiên CAO NHẤT vì đây là "sàn" của toàn dân

PHASE 3 (sau):
  ✅ 02_Subject-Restructure_VN.md — phân tích 12 môn GDPT 2018 + mapping
  □ 03-05 — xây khi overview đủ mature
```

---

> *Curriculum Overview v5.5*
> *Chương trình = nguyên liệu cho chunk building, không phải danh sách nhớ.*
> *3+1 tầng: Nền (ai cũng cần) + Khám Phá (tìm match) + Chuyên Sâu (depth) + Xuyên Suốt (convergence).*
> *7 nhóm nền tảng: 3 nhóm truyền thống (cần nâng depth) + 4 nhóm THIẾU (cần thêm).*
> *Depth target nền = Stage 2 (hiểu tại sao). Chi tiết chuyên sâu → Tầng 3 (per profile).*
