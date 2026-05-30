# Giáo Dục Việt Nam — Tình Trạng Hiện Tại

> **Phiên bản:** v2.0 (rewrite — re-based trên Education-Mechanism.md v1.0)
> **Ngày cập nhật:** 2026-05-11
> **Mục đích:** Snapshot giáo dục VN hiện tại + đánh giá qua Mechanism lens
> **Vị trí:** TẦNG 5 — Country/VN (File 1/3 — data + analysis)
> **Phụ thuộc:**
>   Education-Mechanism.md v1.0 (8 nguyên lý arc design — LENS ĐÁNH GIÁ),
>   Domain-Knowledge-Map.md v1.0 (3-tier domain taxonomy),
>   Education-System.md v2.0 (hệ thống tối ưu — IDEAL để so sánh),
>   Hardware-Calibration.md v1.0 (per-individual — lens nhận diện),
>   Era-Analysis-2025.md v2.0 (context thời đại),
>   Cortisol-Baseline.md v2.0 (amplifier reframe, 5 Roles),
>   Core-Software.md v1.0 (cycle-based architecture),
>   Core-Hardware.md v1.0 (4 zones A/B/C/D),
>   Reward-Signal-Architecture.md v1.0 (Evaluative/Direct-State reward)
> **Bản trước:** backup/v1.0/Country/VN/VN-Education-Status.md (1,316L, DRAFT, 2026-04-03, based on old "10 NL")
> **Thay đổi chính v2.0:**
>   - Re-base: "10 NL" (Education-Principles.md) → Education-Mechanism.md v1.0 (8 nguyên lý + bridge + system)
>   - Re-organize §1: từ NL1-NL10 tuần tự → 3 nhóm theo Mechanism structure
>   - Add: v7.8 concepts (approach/avoidance tags, 3 ORIGIN threat, 4 nguồn fill, Evaluative/Direct-State, chunk compilation levels)
>   - Update: tất cả cross-refs → current file paths
>   - Data giữ nguyên (2022-2025, vẫn current)
> **⚠️ Data = 2022-2025. Giáo dục VN đang cải cách (GDPT 2018) → landscape ĐANG thay đổi.**
> **⚠️ Analysis qua framework = LENS, không phải VERDICT. Cần chuyên gia local validate.**
> **Quy ước:** 🟢 Data/fact (verified sources) | 🟡 Framework analysis (derived) | 🔴 Hypothesis

---

## Mục lục

0. Tổng quan hệ thống
1. Đánh giá qua Education-Mechanism lens (CORE SECTION)
2. Điểm mạnh đang có
3. Điểm yếu cần cải thiện
4. Data + Evidence
5. Gap analysis: Hiện tại vs Ideal
6. Honest Assessment

---

## 0. TỔNG QUAN HỆ THỐNG

```
CẤU TRÚC — HỆ THỐNG 5-4-3: 🟢

  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │  Mầm non         3-5 tuổi      3 năm (không bắt buộc)    │
  │  Tiểu học        6-10 tuổi     5 năm (Grade 1-5)         │
  │  THCS            11-14 tuổi    4 năm (Grade 6-9)         │
  │  THPT            15-17 tuổi    3 năm (Grade 10-12)       │
  │  Đại học / CĐ    18+ tuổi     3-6 năm                   │
  │                                                            │
  │  Tổng giáo dục phổ thông: 12 NĂM                         │
  │  Quản lý: Bộ Giáo dục và Đào tạo (MOET / Bộ GD&ĐT)     │
  │                                                            │
  └────────────────────────────────────────────────────────────┘


QUY MÔ — NĂM HỌC 2024-2025: 🟢

  ┌───────────────────────────────────┬────────────────────────┐
  │ Chỉ số                            │ Số liệu               │
  ├───────────────────────────────────┼────────────────────────┤
  │ Tổng cơ sở giáo dục               │ ~53,979                │
  │ Tổng học sinh (tất cả cấp)        │ ~25,255,000            │
  │ Tổng giáo viên + nhân viên        │ ~1,660,000             │
  │ Giáo viên trực tiếp giảng dạy    │ ~1,251,000             │
  │ Thiếu giáo viên                   │ ~102,000-120,000       │
  │ Đại học                            │ 243 (176 công, 67 tư) │
  │ Sinh viên đại học                  │ ~2,069,000             │
  └───────────────────────────────────┴────────────────────────┘

  Sources: vietnam.vn 2024-2025, MOET reports, Statista 2024


TỈ LỆ BIẾT CHỮ + NHẬP HỌC: 🟢

  Biết chữ người lớn (15+):        ~96.1% (World Bank, 2022)
  Biết chữ thanh niên (15-24):     ~99.0% (UNESCO, 2022)

  Nhập học ròng tiểu học:           ~99.4%
  Nhập học ròng THCS:               ~90%
  Nhập học ròng THPT:               ~77%
  Nhập học thô đại học:             ~42.2% (World Bank, 2022)

  → Tiểu học gần như TOÀN DÂN
  → Drop-off rõ ở THPT (~77%) và đặc biệt ethnic minorities (~55-60%)


NGÂN SÁCH GIÁO DỤC: 🟢

  ┌──────────┬──────────┬───────────────────────┐
  │ Năm      │ % GDP    │ % Chi ngân sách       │
  ├──────────┼──────────┼───────────────────────┤
  │ 2013     │ 5.70%    │ ~20%                  │
  │ 2019     │ 4.20%    │ 16.28%                │
  │ 2020     │ 4.04%    │ 14.47%                │
  │ 2021     │ 3.57%    │ 14.82%                │
  │ 2022     │ 2.89%    │ 15.45%                │
  └──────────┴──────────┴───────────────────────┘

  → GIẢM MẠNH: 5.7% GDP (2013) → 2.89% (2022) = gần một nửa
  → Thấp hơn trung bình thế giới (~4.15% GDP)
  → NHƯNG: hiệu quả chi tiêu CAO (World Bank: VN = efficient spender)
  → So sánh khu vực: Hàn Quốc 5.81%, Malaysia 4.26%,
    Philippines 3.87%, VN 2.89%, Singapore 2.82%

  Sources: World Bank, Trading Economics


CẢI CÁCH GẦN ĐÂY — CHƯƠNG TRÌNH GDPT 2018: 🟢

  Nền tảng: Nghị quyết 29 (2013) — "đổi mới CĂN BẢN, TOÀN DIỆN"

  THAY ĐỔI CỐT LÕI:
    ✓ Từ TRUYỀN THỤ kiến thức → phát triển NĂNG LỰC (competency-based)
    ✓ "Một chương trình, NHIỀU bộ sách" (chấm dứt độc quyền 1 bộ SGK)
    ✓ Tăng quyền tự chủ cho trường + giáo viên
    ✓ Môn tích hợp ở THCS (Khoa học tự nhiên, Khoa học xã hội)
    ✓ Môn tự chọn ở THPT (học sinh chọn hướng)

  5 PHẨM CHẤT: yêu nước, nhân ái, chăm chỉ, trung thực, trách nhiệm
  3 NĂNG LỰC CHUNG: tự chủ + tự học, giao tiếp + hợp tác, giải quyết vấn đề + sáng tạo

  TRIỂN KHAI:
    2020-2021: Lớp 1
    2021-2022: Lớp 2, 6
    2022-2023: Lớp 3, 7, 10
    2023-2024: Lớp 4, 8, 11
    2024-2025: Lớp 5, 9, 12 → HOÀN THÀNH toàn bộ 12 khối

  → Năm 2024-2025 = NĂM ĐẦU TIÊN toàn bộ 12 lớp dùng CT mới

  THÁCH THỨC TRIỂN KHAI:
    ⚠️ Giáo viên chưa sẵn sàng (đào tạo theo mô hình cũ)
    ⚠️ Thiếu sách giáo khoa (TP.HCM thiếu 7,053 bộ SGK)
    ⚠️ Thiếu cơ sở vật chất (phòng lab, IT, thiết bị) ở vùng xa
    ⚠️ Thiếu GV cho môn mới: tiếng Anh, Tin học, Âm nhạc, Mỹ thuật, môn tích hợp

  Sources: MOET, Cogent Education 2025, World Bank ICR, IJLTER


GIÁO VIÊN — DATA NỔI BẬT: 🟢

  LƯƠNG:
    → Giáo viên mới vào nghề 5 năm: lương THẤP HƠN trung bình lao động
    → Trung bình lao động VN 2024: 7.7 triệu VND/tháng (~304 USD)
    → GV mới: ~6.5-8 triệu VND/tháng (sau bảo hiểm)

  TALIS 2024 (OECD survey — data RẤT ĐÁNG CHÚ Ý):

    ┌────────────────────────────────────┬────────┬───────────┐
    │ Chỉ số                             │ VN     │ OECD TB   │
    ├────────────────────────────────────┼────────┼───────────┤
    │ Hài lòng nghề nghiệp              │ 97%    │ 89%       │
    │ Xã hội coi trọng nghề GV          │ 92%    │ 22%       │
    │ Chính sách lắng nghe ý kiến GV    │ 87%    │ 16%       │
    │ GV là lựa chọn nghề đầu tiên      │ 91%    │ 58%       │
    │ Hài lòng với lương                 │ 58%    │ 39%       │
    │ Stress do công việc               │ 4%     │ 19%       │
    │ Dự định rời nghề trong 5 năm      │ <6%    │ varies    │
    │ Đã sử dụng AI trong giảng dạy    │ 64%    │ 36%       │
    └────────────────────────────────────┴────────┴───────────┘

  NGHỊCH LÝ: Lương thấp + thiếu 102,000 GV
    NHƯNG: hài lòng 97%, xã hội tôn trọng 92%, chỉ <6% muốn rời nghề
    → Vấn đề = THU HÚT người MỚI vào nghề, không phải GIỮ CHÂN người CŨ

  Sources: OECD TALIS 2024 Vietnam Country Note, vietnam.vn, Statista


PISA — BIỂU ĐỒ THAY ĐỔI: 🟢

  ┌──────┬───────┬──────────┬──────────┬─────────────────────────┐
  │ Năm  │ Toán  │ Đọc hiểu │ Khoa học │ So với OECD TB           │
  ├──────┼───────┼──────────┼──────────┼─────────────────────────┤
  │ 2012 │ 511   │ 508      │ 528      │ +17 / +12 / +27         │
  │ 2015 │ 495   │ 487      │ 525      │ +5  / -6  / +32         │
  │ 2018 │ 496   │ 505      │ 543      │ +7  / +18 / +54 ⚠️     │
  │ 2022 │ 469   │ 462      │ 472      │ -3  / -14 / -13         │
  └──────┴───────┴──────────┴──────────┴─────────────────────────┘

  ⚠️ 2018: VN thi trên giấy (các nước khác thi máy) → OECD không đưa
    VN vào bảng xếp hạng chính thức do vấn đề so sánh

  2022: Giảm MẠNH so với 2018, nhưng:
    → VN vẫn xếp THỨ 2 Đông Nam Á (sau Singapore)
    → Singapore: 575/543/561
    → VN: 469/462/472
    → Malaysia: 409/388/416
    → Thái Lan: 394/379/409
    → Indonesia: 366/359/383

  LƯU Ý QUAN TRỌNG:
    → Một số học giả đặt câu hỏi về kết quả VN 2012-2018
    → Sample coverage có thể loại trừ HS yếu (out of school)
    → Có thể inflate scores 50-60 điểm (FFT Education Datalab)
    → 2022 toàn cầu đều giảm (COVID effect)

  Sources: OECD PISA 2022, Vietnam News, FFT Education Datalab
```

---

## 1. ĐÁNH GIÁ QUA EDUCATION-MECHANISM LENS (CORE SECTION)

```
MỤC ĐÍCH SECTION NÀY:

  Education-Mechanism.md v1.0 = LENS đánh giá:
    §2: 8 nguyên lý arc design (brain-based, valid mọi era)
    §3: Bridge + Motivation (4 nguồn fill, 3 ORIGIN threat)
    §1 + §4: System-level (tension cá nhân × xã hội, AI-assisted, education ≠ school)

  Section này áp dụng lens ĐÓ vào giáo dục VN hiện tại.

  TỔ CHỨC THEO 3 NHÓM:
    §1.1 — Arc Design (8 nguyên lý) → đánh giá per nguyên lý
    §1.2 — Bridge + Motivation → đánh giá strategy hiện tại
    §1.3 — System-Level → đánh giá cấu trúc hệ thống

  KÝ HIỆU:
    ○  = Align (hệ thống ĐANG làm đúng theo nguyên lý)
    △  = Partial (một phần align, đang chuyển đổi)
    ✗  = Violate (hệ thống đang ĐI NGƯỢC nguyên lý)
    →  = Hướng cải cách (GDPT 2018 đang hướng tới)

  ⚠️ Đánh giá = SIMPLIFIED → thực tế PHỨC TẠP hơn nhiều
  ⚠️ 🟡 Framework analysis — logical nhưng chưa validated as evaluation tool
```

### §1.1 — ARC DESIGN: 8 Nguyên Lý

```
NGUYÊN LÝ 1: DIRECTION > LEVEL (Mechanism §2.2)
  "Cách dạy tạo approach-tag hay avoidance-tag cho domain?"

  ĐÁNH GIÁ: ✗ (threat-heavy → avoidance-tagged)

  HIỆN TRẠNG:
    Hệ thống tạo AVOIDANCE-TAG phổ biến:
    → Phạt điểm kém → "toán = sợ" (avoidance-tagged suốt đời)
    → So sánh công khai → "học = shame risk" (threat-path)
    → Thi cử áp lực → "kiến thức = để thi" (survival mode)
    → "Khổ trước sướng sau" → normalize threat-path learning

    Approach-path HIẾM:
    → Ít trải nghiệm hands-on (curiosity → approach-tag)
    → Ít "aha!" moments trong lớp (lecture-dominant)
    → Play + exploration bị cắt (tiểu học: 5-7 trang BT/ngày)

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.2: "Cùng nội dung, khác cách dạy → khác tag → khác SUỐT ĐỜI"
    → VN: phần lớn domains được dạy qua threat-path
    → Chunks COMPILE (PISA scores OK) nhưng với AVOIDANCE-TAG
    → = "Biết toán nhưng ghét toán" = common outcome
    → = Giải thích tại sao 60% SV làm trái ngành: avoidance-tagged
      domains → body pull AWAY khi không còn bridge bắt buộc

  EVIDENCE:
    🟢 57.8% HS sợ sai trong lớp (ResearchGate)
    🟢 56.6% sợ trình bày ý tưởng kém
    🟢 80% THPT ngủ <7h → học trong trạng thái cortisol cao
    🟡 Avoidance-tag dẫn tới rời bỏ domain = framework prediction,
       consistent với 60% trái ngành data
```

```
NGUYÊN LÝ 2: MINIMIZE COST PER STUDENT (Mechanism §2.3)
  "Arc có tối ưu cost cho student NÀY hay one-size cho tất cả?"

  ĐÁNH GIÁ: ✗ (one-size-fits-all → hardware mismatch phổ biến)

  HIỆN TRẠNG:
    Cost formula: cost ≈ f(chunk_gap × hardware_mismatch × direction)
    → VN: hardware_mismatch = CAO (1 method cho 40-69 HS/lớp)
    → Somatic-dominant student + verbal lecture = mismatch → cost CAO
    → Visual-dominant student + text-only = mismatch → cost CAO
    → CÙNG bài, KHÁC hardware → KHÁC cost hoàn toàn → one-size = sub-optimal

  EVIDENCE:
    🟢 Lớp thực tế: 40-69 HS/lớp (King's Think Tank 2025)
    🟢 Thiếu 102,000+ GV (MOET 2025)
    🟢 HS/GV tiểu học: 23.3:1 (Statista 2024)
    🟢 HS kém bị label "lười" thay vì "hardware mismatch"
      (Hardware-Calibration.md v1.0 §5 — miscalibration patterns)
    🟢 Ethnic minority dropout: 2x Kinh, late enrollment: 5x

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.3: "one-size-fits-all LUÔN sub-optimal"
    → VN: GV 50 HS → KHÔNG THỂ calibrate per-hardware dù muốn
    → Labels "giỏi/kém" = theo method-fit, KHÔNG theo capability
    → Structural barrier: class size + teacher shortage + no calibration training
    → GDPT 2018 hướng tới "phát triển năng lực CÁ NHÂN" — ý đúng,
      nhưng structural barriers chưa giải quyết
```

```
NGUYÊN LÝ 3: PREREQUISITE CHECK (Mechanism §2.4)
  "Có verify chunks nền trước khi bắt đầu arc mới?"

  ĐÁNH GIÁ: △ (curriculum có sequence, nhưng cứng)

  HIỆN TRẠNG:
    → Curriculum sequence: tiểu học → THCS → THPT = có hierarchy
    → Phân loại theo TUỔI, không theo compiled-chunks
    → HS 12 tuổi thiếu prerequisite phân số → VẪN phải học đại số
    → "Không hiểu" thường = thiếu prerequisite, bị label "kém"
    → GDPT 2018: tăng flexibility nhưng vẫn age-based progression

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.4: "Thiếu prerequisite → arc fail → body overwhelm
      → avoidance-tag tích lũy"
    → VN: prerequisite check KHÔNG xảy ra per-student
    → Ai lọt lưới → tích lũy gaps → snowball effect
    → = 1 trong 3 nguyên nhân "ghét toán" (Mechanism §2.4 ví dụ):
      ① Avoidance-tagged (dạy sai direction)
      ② Thiếu prerequisite → overwhelm → avoidance tích lũy
      ③ Hardware mismatch (cần visual, dạy verbal)
    → VN system không phân biệt 3 nguyên nhân → label chung "kém"
```

```
NGUYÊN LÝ 4: MINI-ARCS + VALLEY (Mechanism §2.5)
  "Bài học có chia nhỏ, mỗi phần có 'aha'? Có chuẩn bị cho valley?"

  ĐÁNH GIÁ: ✗ (lecture blocks, ít valley awareness)

  HIỆN TRẠNG:
    → Lecture-dominant: thầy nói → trò nghe → làm bài → chấm điểm
    → Tiết học 45 phút = 1 block, ít cấu trúc mini-arc
    → "Aha!" moments hiếm — vì: transmit knowledge ≠ design for discovery
    → Valley awareness: HS + GV + PH KHÔNG biết "giữa arc khó nhất — bình thường"
    → Khi HS gặp khó khăn giữa chừng → bị label "lười" / "thiếu cố gắng"
      thay vì "đang ở valley — cần bridge tạm"

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.5: "Arc dài + không reward giữa = body bỏ cuộc"
    → VN: school year = long arc, kỳ thi = only reward signal
    → Giữa kỳ = valley → HS cần bridge MẠN NHẤT ở đây
    → Nhưng: bridge VN TĂNG ĐỀU (pressure constant) thay vì
      TĂNG ở valley + GIẢM sau aha
    → "Normalize dissonance" (meta-skill quý nhất — Mechanism §2.5)
      = gần như KHÔNG ĐƯỢC DẠY ở VN
```

```
NGUYÊN LÝ 5: IMAGINE-FINAL BEFORE CONTENT (Mechanism §2.6)
  "Student có thấy 'tại sao' trước 'cái gì'?"

  ĐÁNH GIÁ: ✗

  HIỆN TRẠNG:
    "Cứ học đi" = approach phổ biến nhất
    → HS học 12 năm → mục tiêu duy nhất rõ ràng: THI ĐỖ ĐẠI HỌC
    → "Tại sao học?" → "Để thi" / "Để có bằng" / "Để có việc"
    → Imagine-Final phổ biến nhất: NARROW + EXTERNAL
      → Narrow: "thi đỗ → bằng → việc → tiền"
      → External: từ gia đình + xã hội, không từ learner

  EVIDENCE:
    🟢 60% SV tốt nghiệp làm việc KHÔNG liên quan ngành học (Saigoneer)
    🟢 100,000+ cử nhân thất nghiệp hàng năm
    🟢 Thi tốt nghiệp THPT = DUAL PURPOSE (vừa tốt nghiệp vừa xét ĐH)
    → Stakes CỰC CAO cho 1 kỳ thi → "học để thi" là rational response

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.6: Imagine-Final = "body simulate future state"
    → VN: Imagine-Final = "bố mẹ simulate CỦA HỌ → inject vào con"
    → = Nguồn ④ External Inject (Mechanism §3.1) dominate
      thay vì nguồn ① PFC tự xây
    → Imagine-Final-Evaluation.md: 4 góc quality
      → VN pattern: thường rơi vào "Mismatch" (Domain ✓ + Hardware ✗)
      = "nghề có thật, nhưng KHÔNG phù hợp hardware EM"
    → 60% trái ngành = EVIDENCE cho Mismatch at population scale
```

```
NGUYÊN LÝ 6: FEEDBACK LOOP (Mechanism §2.7)
  "Arc có feedback liên tục hay set-and-forget?"

  ĐÁNH GIÁ: ✗ → △ (đang cải cách)

  HIỆN TRẠNG:
    → Feedback = chủ yếu ĐIỂM SỐ (correctness, không phải progress)
    → GV → HS: "đúng/sai" > "em đang ở đâu, cần gì tiếp"
    → HS → GV: feedback MUTED (hierarchy + face-saving → HS không dám nói)
    → 57.8% HS sợ sai → feedback bị CHẶN từ phía HS

  GDPT 2018 — cải cách:
    → Tiểu học: đánh giá phát triển (qualitative — Circular 30/22)
    → Process assessment tăng 30% → 50% (2025)
    → Hướng ĐÚNG: feedback liên tục thay vì 1 kỳ thi cuối

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.7: "Arc quá dễ = boring / quá khó = overwhelm"
    → Feedback loop = mechanism DETECT + ADJUST liên tục
    → VN: feedback loop BỊ CHẶN 2 CHIỀU:
      → GV → HS: chỉ correctness, không progress
      → HS → GV: hierarchy suppress honest signal
    → GDPT 2018 cải thiện chiều GV→HS (qualitative assessment)
    → Nhưng chiều HS→GV (honest signal) vẫn bị văn hóa cản
```

```
NGUYÊN LÝ 7: CONSOLIDATION = PHẦN CỦA EDUCATION (Mechanism §2.8)
  "Ngủ + nghỉ + spacing có được tôn trọng?"

  ĐÁNH GIÁ: ✗ (THIÊN QUÁ TẢI — sleep deprived, no spacing)

  HIỆN TRẠNG:
    → 80% HS THPT ngủ <7h/ngày
    → 90% quy thiếu ngủ = ôn thi
    → 12-15 giờ học/ngày cho lớp 12 (trường + thêm + bài tập)
    → Homework: HS lớp 2: 5-7 trang/ngày → 19h-22h chưa xong
    → Cramming (nhồi nhét) = norm → spacing gần như KHÔNG CÓ
    → "Khổ trước sướng sau" = cultural permission cho overwork

  EVIDENCE:
    🟢 80% THPT ngủ <7h (VnExpress)
    🟢 Giờ học thêm ~6h/tuần = 3x quốc tế cho GDP VN (PISA 2012)
    🟢 HS lớp 9 TP.HCM: học thêm MỖI TỐI trừ Chủ nhật → xong 23h

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.8: "Sleep consolidation: learning HAPPENS during sleep"
    → Homework NHIỀU → thiếu ngủ → consolidation BỊ CẮT
    → = "Học mà không nhớ" → cần học THÊM → thiếu ngủ THÊM → vòng xoáy
    → Spacing (5 lần × 5 ngày > 25 lần × 1 ngày) gần như KHÔNG ÁP DỤNG
    → Cortisol-Baseline.md v2.0: sleep = cortisol repair time
    → Ngủ <7h = cortisol recovery BỊ CẮT → tích lũy → chronic
```

```
NGUYÊN LÝ 8: ASSESS DEPTH, NOT SURFACE (Mechanism §2.9)
  "Đánh giá chunk compilation depth hay chỉ correctness?"

  ĐÁNH GIÁ: ✗ → △ (đang cải cách)

  HIỆN TRẠNG:
    Surface assessment = DOMINANT
    → Multiple choice phổ biến → đo stage ① RECOGNIZE
    → "Thuộc bài" > "hiểu bài" → recall > explain
    → Bằng cấp = proxy cho năng lực → system reward surface

  4 STAGES DEPTH (Mechanism §2.9, mapped to chunk compilation):
    ① RECOGNIZE → "nghe quen" (proto-chunk)       ← VN assess CHỦ YẾU ở đây
    ② EXPLAIN → "nói lại được" (compiled)          ← ít
    ③ APPLY → "dùng trong context mới" (compiled+linked) ← rất hiếm
    ④ CREATE/TRANSFER → "kết hợp tạo mới" (meta-chunk) ← gần như không

  CẢI CÁCH 2025:
    → Process assessment: 30% → 50% (tăng weight quá trình)
    → Tiểu học: đã chuyển sang đánh giá phát triển (qualitative)
    → ĐH: tự chủ tuyển sinh → đa dạng hóa (phỏng vấn, portfolio, IELTS...)

  EVIDENCE:
    🟢 PISA 2022: 72% HS đạt Level 2+ Toán (basics OK)
    🟢 NHƯNG: chỉ 5% Level 5-6 Toán, 1% Level 5+ Đọc hiểu
    → = System TỐT ở stage ①, YẾU ở stage ③④

  QUA FRAMEWORK LENS: 🟡
    → "Assessment drives learning" → assess surface → learn surface
    → Reward-Signal-Architecture.md v1.0: Evaluative reward (opioid)
      chỉ fire khi depth THẬT SỰ compile → multiple choice = không trigger
    → = HS KHÔNG nhận reward signal cho deep learning
    → CẢI CÁCH GDPT 2018 = hướng đúng, nhưng "process assessment"
      vẫn có thể = "surface assessment nhiều lần" nếu chất lượng không đổi
```

```
TỔNG KẾT 8 NGUYÊN LÝ ARC DESIGN: 🟡

  ┌────┬──────────────────────────────┬──────────┬────────────┐
  │ #  │ Nguyên lý                    │ Đánh giá │ Xu hướng   │
  ├────┼──────────────────────────────┼──────────┼────────────┤
  │ 1  │ Direction > Level            │ ✗        │ Chưa có ═  │
  │ 2  │ Minimize cost per student    │ ✗        │ Rất chậm ↑ │
  │ 3  │ Prerequisite check           │ △        │ Ổn định ═  │
  │ 4  │ Mini-arcs + valley           │ ✗        │ Chưa có ═  │
  │ 5  │ Imagine-Final before content │ ✗        │ Chưa có ═  │
  │ 6  │ Feedback loop                │ ✗ → △    │ Cải cách ↑ │
  │ 7  │ Consolidation                │ ✗        │ Chưa rõ ═  │
  │ 8  │ Depth assessment             │ ✗ → △    │ Cải cách ↑ │
  └────┴──────────────────────────────┴──────────┴────────────┘

  → 6/8 nguyên lý: ✗ (violate)
  → 2/8: đang chuyển đổi (feedback + depth — GDPT 2018)
  → Nguyên lý 1 (Direction > Level) = QUAN TRỌNG NHẤT + CHƯA CÓ cải cách
```

### §1.2 — BRIDGE + MOTIVATION

```
4 NGUỒN FILL (Mechanism §3.1, Anchor-Schema.md §3)
  "Anchor học tập được fill từ nguồn nào?"

  ĐÁNH GIÁ: ✗ (nguồn ④ External Inject dominant 12+ năm)

  4 NGUỒN VÀ STATUS TẠI VN:

    ① PFC Imagine-Final (self-directed): YẾU
       → HS KHÔNG tự xây Imagine-Final → gia đình + xã hội inject
       → "Tại sao học?" → "Vì bố mẹ nói" (nguồn ④, không phải ①)

    ② Hippocampus Experience: YẾU
       → Ít trải nghiệm hands-on (lecture-dominant)
       → Ít "tôi ĐÃ LÀM, tôi biết feel thế nào"
       → Trải nghiệm = "thi rồi, biết sợ" → avoidance memory

    ③ Compiled Routines: VỪA
       → "Học bài → làm bài tập" = compiled routine
       → Nhưng: routine = TASK (làm gì), không = MOTIVATION (tại sao)

    ④ External Inject (bridges): DOMINANT
       → Điểm số: 12 năm liên tục
       → Xếp hạng: trong lớp, trường, tỉnh, quốc gia
       → Gia đình: "bố mẹ vất vả vì con" = guilt bridge
       → Khen/phạt: labels "giỏi/kém" suốt 12 năm
       → Học thêm: +6h/tuần bridge NGOÀI trường

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §3.4: Healthy trajectory = ④ giảm dần, ①②③ take over
    → VN: ④ TĂNG DẦN (lớp 1 → 12: bridge ESCALATING)
    → = NGƯỢC hoàn toàn healthy trajectory
    → Khi ra đời 18+ → nguồn ④ rút đột ngột → anchor crash
    → = Quarter-life crisis mechanism (Mechanism §3.4)
    → 60% trái ngành = evidence cho anchor crash + motivation collapse


3 ORIGIN THREAT TAXONOMY (Mechanism §3.3)
  "Pressure từ đâu? Domain, Peer, hay Imposed?"

  ĐÁNH GIÁ: ✗ (Imposed dominant, Domain + Peer suppressed)

  3 LOẠI THREAT VÀ STATUS TẠI VN:

    TYPE 1 — DOMAIN (từ reality): BỊ GIẢM
       → Bài toán khó, thí nghiệm fail = ít (lecture-dominant → ít hands-on)
       → Play + exploration bị cắt → ít domain challenge tự nhiên
       → Education action: cần TĂNG domain exposure

    TYPE 2 — PEER (từ bạn bè): BỊ KIỂM SOÁT QUÁ MỨC
       → Face-saving → HS không dám tranh luận
       → Collectivism → harmony > honest conflict
       → Bullying: 73.9% (Đà Nẵng THCS) → peer NEGATIVE có, peer GROWTH ít
       → Education action: cần cho phép healthy peer conflict

    TYPE 3 — IMPOSED (từ authority): DOMINANT
       → GV mắng, phạt điểm, đọc điểm kém công khai
       → PH dọa, so sánh, guilt: "bố mẹ vất vả"
       → Thi cử áp lực: 1 kỳ thi quyết định tương lai
       → Xếp hạng toàn trường → shame risk
       → = Imposed threat = nguồn cortisol LỚN NHẤT

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §3.3: "Cùng cortisol level, khác ORIGIN → khác hoàn toàn"
    → Domain moderate → resilience + competence
    → Peer moderate → social skill + emotional intelligence
    → Imposed moderate → anxiety + learned helplessness
    → VN: shield HS khỏi Domain + Peer (helicopter pattern)
          → TĂNG Imposed (ép học, điểm, so sánh)
    → = NGƯỢC hoàn toàn healthy pattern
    → = Nghịch lý hiện đại (Mechanism §3.3): ít domain challenge + nhiều imposed threat


BRIDGE RÚT DẦN? (Mechanism §3.1-§3.4)
  "Bridge có phase out hay permanent?"

  ĐÁNH GIÁ: ✗ (permanent + ESCALATING)

  HIỆN TRẠNG:
    → Điểm số: từ lớp 1 đến lớp 12, suốt 12 năm
    → Lớp 1-5: áp lực vừa → Lớp 6-9: tăng → Lớp 10-12: CỰC ĐẠI
    → Học thêm: 70-92% HS tham gia → bridge THÊM ngoài trường
    → "Học sinh giỏi/tiên tiến" = labels suốt 12 năm
    → Gia đình: guilt bridge KHÔNG rút → thậm chí TĂNG theo stakes

  CẢI CÁCH GDPT 2018:
    → Tiểu học: Thông tư 30/2014 + 22/2016 → qualitative assessment
    → Process assessment tăng 30% → 50%
    → Hướng ĐÚNG: giảm weight kỳ thi cuối

  QUA FRAMEWORK LENS: 🟡
    → Bridge lý tưởng: NHỎ NHẤT có thể → đợi ①②③ take over → phase out
    → VN: bridge = "thuốc quá liều" (Mechanism §3.1)
      → Kill intrinsic, tạo dependency
    → Bridge NGOÀI hệ thống (học thêm, gia đình) = KHÔNG ai quản lý
    → = Cả 2 lý do bridge fail: quá nhiều (overdose) + không rút (chronic)
```

### §1.3 — SYSTEM-LEVEL

```
FOUNDATION BREADTH (Mechanism §1.2 + DKM v1.0 §1)
  "Foundation cover mấy domain trong 6 Foundation Domains?"

  ĐÁNH GIÁ: ○ / △ (MẠNH 2/6, YẾU 4/6)

  6 FOUNDATION DOMAINS (Domain-Knowledge-Map.md v1.0 §1):
    ① Cognitive (tư duy, logic)                  → VN: ○ MẠNH
    ② Linguistic (ngôn ngữ, đọc viết)            → VN: ○ MẠNH
    ③ Social-Emotional (cảm xúc, quan hệ)        → VN: ✗ YẾU
    ④ Physical-Somatic (vận động, cơ thể)        → VN: △ VỪA
    ⑤ Creative-Aesthetic (sáng tạo, thẩm mỹ)    → VN: ✗ YẾU
    ⑥ Meta-Cognitive (học cách học)               → VN: ✗ YẾU

  → Foundation = STRENGTH LỚN NHẤT — nhưng LỆCH
  → Literacy 96.1%, PISA basics > OECD → cognitive + linguistic = EXCELLENT
  → Emotional regulation, creative thinking, meta-learning = gần không dạy

  QUA FRAMEWORK LENS: 🟡
    → "Foundation" trong Mechanism = RỘNG hơn "foundation" truyền thống
    → VN mạnh foundation TRÍ TUỆ, nhưng foundation CẢM XÚC + META = yếu
    → GDPT 2018: "tự chủ + tự học" (meta-cognitive) → HƯỚNG ĐÚNG
    → Nhưng: chưa có method rõ ràng để dạy meta-cognitive explicitly


PER-HARDWARE CALIBRATION (Mechanism §2.3 + Hardware-Calibration.md v1.0)
  "Có adjust per individual hay one-size-fits-all?"

  ĐÁNH GIÁ: ✗ (điểm YẾU rõ nhất)

  HIỆN TRẠNG:
    → 1 chương trình, 1 tốc độ, 1 phương pháp cho tất cả
    → Phân loại theo TUỔI, không theo hardware
    → Lớp 40-69 HS → GV KHÔNG THỂ observe per-individual
    → Không có calibration training cho GV
    → Ethnic minority: 2x dropout, 5x late enrollment

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §2.3: cùng content + khác hardware → khác cost
    → Hardware-Calibration.md v1.0: 6 dimensions observable per-individual
    → VN: GV không được training nhận diện 6 dimensions
    → AI CÓ THỂ giúp (per-individual tracking) nhưng:
      → 71% GV thiếu cơ sở hạ tầng số (TALIS 2024)
      → Digital divide: richest 95% internet vs poorest 18%
    → = NL mấu chốt cho True-Fit, hiện gần như KHÔNG CÓ


CÁ NHÂN × XÃ HỘI TENSION (Mechanism §1.3)
  "Balance individual-society hay nghiêng 1 bên?"

  ĐÁNH GIÁ: ✗ (nghiêng XÃ HỘI)

  HIỆN TRẠNG:
    → "Nghề hot" > "con muốn gì"
    → 5 phẩm chất GDPT 2018 mở đầu = "yêu nước" (xã hội → cá nhân)
    → Gia đình quyết định hướng đi nhiều hơn bản thân HS
    → 60% SV trái ngành = chọn theo xã hội, không theo hardware

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §1.3: tension = CẤU TRÚC, không giải được, chỉ BALANCE
    → VN: society CẦN >>> individual MUỐN
    → Forced-Fit rate cao → lãng phí talent + burnout + mental health
    → Mechanism §1.3 nhận diện 3 era patterns:
      → Pre-industrial: per-individual nhưng hạn chế access
      → Industrial: scalable nhưng one-size (← VN đang ở đây)
      → AI era: potential per-individual AT SCALE (← VN chưa tới)


EDUCATION = ECOSYSTEM (Mechanism §1.4 + §4)
  "Learning xảy ra ở đâu — chỉ school hay 4 kênh?"

  ĐÁNH GIÁ: ✗ → △

  HIỆN TRẠNG:
    → "Con đi học" = "con đi trường" = ĐỒNG NHẤT
    → Learning ngoài trường: 92% HS học thêm → nhưng = MORE OF SAME
    → Học thêm ≠ "mở rộng learning context" — = "thêm school-style learning"
    → EdTech: 100+ startups, AI market $24M → growing nhưng chủ yếu
      = digitize school format, không reimagine learning

  QUA FRAMEWORK LENS: 🟡
    → Mechanism §1.4: "Não KHÔNG biết đang ở trường — chỉ biết
      có compile chunks không"
    → Education = 4 kênh (Education-System.md v2.0 §9):
      School + Family + Self-directed + AI
    → VN: school + tutoring (= more school) = 90%+ learning time
    → Self-directed learning = rất ít (HS KHÔNG CÓ TIME)
    → AI: 64% GV đã dùng → ahead of OECD → potential cao
    → = System concentrate learning vào 1 FORMAT (school)


ADAPTABILITY (DKM §2 + Era-Analysis v2.0)
  "Build adaptability hay chỉ specific knowledge?"

  ĐÁNH GIÁ: ✗ → △ (đang chuyển đổi)

  HIỆN TRẠNG:
    → "Thuộc bài" = measure thành công
    → Rote memorization embedded trong culture
    → "Biết nhiều" > "biết học" → knowledge > meta-learning
    → Era-Analysis v2.0 §5: "biết HỎI" > "biết" trong AI era

  GDPT 2018:
    → "Tự chủ + tự học" + "giải quyết vấn đề" = năng lực chung
    → Hướng adaptability → nhưng implementation mới 5 năm

  EVIDENCE:
    🟢 1% Level 5+ Đọc hiểu (OECD: 7%) → depth thinking rất ít
    🟢 60% SV trái ngành → knowledge specific → không transfer
    🟢 41% nhà tuyển dụng không tuyển đủ ứng viên đạt yêu cầu

  QUA FRAMEWORK LENS: 🟡
    → DKM §2: 6 Era-Specific domains (AI Literacy, Data Thinking, etc.)
    → VN: vẫn optimize cho knowledge retention → sai hướng cho AI era
    → "Meta-learning" gần như KHÔNG ĐƯỢC DẠY explicitly
    → GDPT 2018 = mục tiêu đúng, phương pháp chưa đủ
```

```
TỔNG KẾT TOÀN BỘ §1 — BẢNG ĐÁNH GIÁ: 🟡

  ┌──────────────────────────────────────┬──────────┬────────────┐
  │ Đánh giá                             │ Status   │ Xu hướng   │
  ├──────────────────────────────────────┼──────────┼────────────┤
  │ ARC DESIGN (Mechanism §2):           │          │            │
  │  ① Direction > Level                │ ✗        │ ═          │
  │  ② Minimize cost per student         │ ✗        │ ↑ chậm     │
  │  ③ Prerequisite check               │ △        │ ═          │
  │  ④ Mini-arcs + valley               │ ✗        │ ═          │
  │  ⑤ Imagine-Final before content     │ ✗        │ ═          │
  │  ⑥ Feedback loop                    │ ✗ → △    │ ↑          │
  │  ⑦ Consolidation                    │ ✗        │ ═          │
  │  ⑧ Depth assessment                 │ ✗ → △    │ ↑          │
  ├──────────────────────────────────────┼──────────┼────────────┤
  │ BRIDGE + MOTIVATION (Mechanism §3):  │          │            │
  │  4 nguồn fill: ④ dominant           │ ✗        │ ═          │
  │  3 ORIGIN: Imposed dominant          │ ✗        │ ═          │
  │  Bridge phase-out                    │ ✗        │ ↑ nhẹ      │
  ├──────────────────────────────────────┼──────────┼────────────┤
  │ SYSTEM-LEVEL (Mechanism §1+§4+DKM): │          │            │
  │  Foundation breadth                  │ ○ / △    │ ═          │
  │  Per-hardware calibration            │ ✗        │ ↑ chậm     │
  │  Individual × Society               │ ✗        │ ↑ chậm     │
  │  Education ecosystem                 │ ✗ → △    │ ↑          │
  │  Adaptability                        │ ✗ → △    │ ↑          │
  └──────────────────────────────────────┴──────────┴────────────┘


PATTERN: 🟡

  → MẠNH: Foundation breadth ở cognitive + linguistic
  → ĐANG CẢI CÁCH: Feedback, Depth assessment, Ecosystem, Adaptability
    (GDPT 2018 targeting ĐÚNG)
  → CHƯA CÓ CHUYỂN BIẾN: Direction > Level, Imagine-Final,
    Mini-arcs, Consolidation, 3 ORIGIN, 4 nguồn fill
    → = Các khái niệm v7.8 MỚI — chưa có trong discourse GD VN
  → CẦN STRUCTURAL CHANGE: Per-hardware calibration, I×S balance
    → = Budget + class size + cultural shift

  GDPT 2018 đang TARGET ĐÚNG nhiều vấn đề (feedback, depth, adaptability,
  ecosystem). Nhưng: Mechanism lens THÊM nhiều dimensions mà GDPT 2018
  CHƯA COVER: direction > level, 3 ORIGIN threat, 4 nguồn fill, mini-arcs.
  = Bổ sung, không mâu thuẫn.
```

---

## 2. ĐIỂM MẠNH ĐANG CÓ

```
MỤC ĐÍCH:
  → Từ §0 (data) + §1 (Mechanism analysis) → VN ĐANG LÀM TỐT gì?
  → Strengths = NỀN TẢNG để build on, không phải "ok rồi bỏ qua"
  → 🟡 Analysis tổng hợp từ data + framework lens
```

```
STRENGTH 1: FOUNDATION LITERACY + NUMERACY

  VN = VƯỢT TRỘI so với GDP level ở foundation basics

  → Literacy 96.1% người lớn, 99% thanh niên = top khu vực
  → Primary enrollment ~99.4% = gần toàn dân
  → PISA 2012-2018: consistently outperform OECD average ở basics
  → PISA 2022: vẫn xếp thứ 2 Đông Nam Á (sau Singapore)
  → Khoảng cách VN-Malaysia/Thailand/Indonesia = RẤT LỚN

  TẠI SAO STRENGTH:
    → Foundation = BASE → mọi thứ khác build on top
    → 2/6 Foundation Domains (DKM §1) = EXCELLENT
    → VN "efficient spender" (World Bank) — ít tiền, kết quả foundation tốt
    → Cultural factor: "đọc thông viết thạo" = value sâu

  RISK:
    → Budget giảm 5.7% → 2.89% GDP → foundation có thể suy giảm
    → Teacher shortage 102K+ → ảnh hưởng quality
    → PISA 2022 giảm = tín hiệu cảnh báo sớm?


STRENGTH 2: GIÁO VIÊN — TÔN TRỌNG XÃ HỘI + HÀI LÒNG NGHỀ (TALIS 2024)

  Data TALIS 2024 = ĐIỂM SÁNG NHẤT, độc đáo toàn cầu

  → 92% xã hội tôn trọng (OECD: 22% = 4x ít hơn!)
  → 97% hài lòng nghề nghiệp (OECD: 89%)
  → 91% chọn GV là nghề đầu tiên (OECD: 58%)
  → <6% dự định rời nghề, stress chỉ 4% (OECD: 19%)
  → 64% đã dùng AI = ahead of OECD

  TẠI SAO STRENGTH:
    → GV = vai trò quan trọng nhất trong hệ thống
      (Education-System.md v2.0 §7 — Teacher as Calibrator)
    → GV hài lòng + tôn trọng = NỀN TẢNG cho mọi reform
    → VN: GV SẴN SÀNG → platform cho training upgrade
    → Trust ĐÃ CÓ → chỉ cần add skills, không cần build trust

  RISK:
    → Lương thấp → không thu hút người MỚI giỏi vào nghề
    → 102K+ thiếu → overload GV hiện tại
    → Xã hội TÔN TRỌNG nhưng không TRẢ LƯƠNG tương xứng


STRENGTH 3: GDPT 2018 — HƯỚNG CẢI CÁCH ĐÚNG

  → Competency-based thay vì knowledge-based → ĐÚNG HƯỚNG
  → "Một chương trình, nhiều bộ sách" = tăng diversity
  → Tăng tự chủ GV + trường → hướng per-individual
  → Môn tự chọn THPT = bước đầu choice
  → Assessment reform (process 50%) → hướng depth
  → 2024-2025 = hoàn thành rollout 12/12 lớp

  TẠI SAO STRENGTH:
    → Chứng minh: VN CÓ KHẢ NĂNG reform ở cấp hệ thống
    → Direction đúng → vấn đề = execution + depth
    → Qua Mechanism lens: GDPT 2018 address §2.7 (feedback),
      §2.9 (depth), §1.4 (adaptability) → đúng hướng

  RISK:
    → Reform trên giấy ≠ reform trong lớp học
    → GV chưa sẵn sàng → "dạy mới bằng cách cũ"
    → Thiếu cơ sở vật chất → chênh lệch urban-rural tăng


STRENGTH 4: FAMILY INVOLVEMENT CAO (CULTURAL)

  → 66% HS nói áp lực phụ huynh = nguồn stress chính
    → = Phụ huynh QUAN TÂM (dù direction cần cải thiện)
  → Chi tiêu gia đình: 42-43% chi phí GD = từ gia đình
  → "Học để đổi đời" = strong family Imagine-Final
  → Extended family network = support system

  TẠI SAO STRENGTH:
    → Family = 1 trong 4 kênh ecosystem (Education-System.md v2.0 §9)
    → Involvement CAO = NỀN TẢNG → chỉ cần REDIRECT
    → Từ nguồn ④ pressure → environment designer (Education-System v2.0 §8)
    → Nhiều nước phát triển MƠ ƯỚC có family involvement level này

  RISK:
    → Involvement CAO + wrong direction = damage CAO
    → Áp lực gia đình = Imposed threat (3 ORIGIN Type 3) lớn nhất
    → "Đầu tư" = chủ yếu TIỀN, ít TIME cho emotional support


STRENGTH 5: EFFICIENCY — LÀM NHIỀU VỚI ÍT

  → GDP per capita ~4,536 USD (2024) — lower-middle income
  → NHƯNG: PISA scores vượt nhiều nước giàu gấp 5-10x
  → Budget 2.89% GDP — dưới trung bình thế giới
  → World Bank xếp VN = "efficient education spender"
  → Literacy 96%+ — tương đương upper-middle income

  QUA FRAMEWORK LENS: 🟡
    → Efficiency = strength khi resources limited
    → Nhưng: efficiency CÓ THỂ = "squeeze max from people"
    → = HS + GV overwork → scores cao BẰNG workload cao
    → = "Efficient" nhưng cost = wellbeing
    → = PISA paradox: same machinery drives ACHIEVEMENT + MENTAL HEALTH CRISIS
```

---

## 3. ĐIỂM YẾU CẦN CẢI THIỆN

```
MỤC ĐÍCH:
  → Từ §1 (Mechanism analysis) → ưu tiên điểm yếu theo IMPACT
  → Ưu tiên: cái nào gây DAMAGE nhiều nhất + cải thiện được?
  → 🟡 Framework analysis — priority ranking = subjective judgment
```

```
WEAKNESS 1 [CRITICAL]: THREAT-DOMINANT LEARNING — DIRECTION SAI

  ĐÂY LÀ VẤN ĐỀ NGHIÊM TRỌNG NHẤT — v7.8 INSIGHT MỚI

  DATA:
    → 22.8% trầm cảm, 26.3% ý tưởng tự tử (HS 13-17 tuổi)
    → 80% THPT ngủ <7h / 90% do ôn thi
    → 12-15 giờ học/ngày cho lớp 12
    → 4.1 giờ/ngày mạng xã hội → 50% có psychological distress

  FRAMEWORK v7.8 REFRAME: 🟡
    → TRƯỚC v7.8: "cortisol quá cao" (cần giảm cortisol)
    → SAU v7.8: "direction SAI" (cần đổi path, không chỉ giảm level)
    → Cortisol-Baseline.md v2.0: cortisol = AMPLIFIER, không phải "stress hormone"
    → Vấn đề KHÔNG CHỈ "áp lực nhiều" → mà "áp lực TỪ ĐÂU"

    3 ORIGIN analysis:
    → Domain threats (reality challenge): BỊ GIẢM → cần TĂNG
    → Peer threats (social challenge): BỊ KIỂM SOÁT → cần MODERATE
    → Imposed threats (authority): DOMINANT → cần GIẢM MẠNH

    → Cùng cortisol level nhưng:
      → Domain moderate → resilience + competence
      → Imposed moderate → anxiety + learned helplessness
    → VN: Imposed dominant → chunks compile AVOIDANCE-TAG
    → = "Biết nhưng ghét" = common outcome

  TẠI SAO CRITICAL:
    → Direction sai → mọi chunk compile = avoidance-tagged
    → 12 năm avoidance-tagged learning = SABOTAGE lifelong relationship với domain
    → Ngủ <7h = cortisol recovery BỊ CẮT → amplification tích lũy
    → 26.3% ý tưởng tự tử = KHÔNG THỂ chấp nhận được


WEAKNESS 2 [HIGH]: ONE-SIZE-FITS-ALL — KHÔNG PER-HARDWARE

  DATA:
    → Lớp 40-69 HS, 1 GV, 1 method, 1 tốc độ
    → Thiếu 102,000+ GV → overload GV hiện tại
    → Không có calibration training cho GV
    → Ethnic minorities: 2x dropout, 5x late enrollment
    → Rural: 50% thiếu tech cơ bản

  TẠI SAO HIGH:
    → Per-hardware = điều kiện cho True-Fit (Education-System.md v2.0 §7)
    → Không per-hardware → cost formula (Mechanism §2.3) = maximum mismatch
    → HS khác hardware + cùng method → labels sai ("giỏi/kém")
    → = Vòng tròn: budget ↓ → teacher ↓ → class size ↑ → quality ↓


WEAKNESS 3 [HIGH]: IMAGINE-FINAL SAI HƯỚNG + NARROW

  DATA:
    → 60% SV trái ngành
    → 100,000+ cử nhân thất nghiệp
    → 41% nhà tuyển dụng không tuyển đủ

  TẠI SAO HIGH:
    → Imagine-Final = narrow ("thi đỗ → bằng → việc") + external (gia đình inject)
    → Imagine-Final-Evaluation.md: VN pattern = "Mismatch" quadrant dominant
    → 12 năm học theo HƯỚNG SAI → waste at population scale
    → Không có process giúp HS self-build Imagine-Final
      (navigate 4 góc quality — Mechanism §2.6)


WEAKNESS 4 [MEDIUM]: BRIDGE PERMANENT + ESCALATING

  DATA:
    → 92% HS đi học thêm (trung bình 6h/tuần = 3x quốc tế)
    → 42-43% chi phí GD gia đình = cho học thêm
    → GV cố tình dạy ít → bán content ở học thêm

  FRAMEWORK REFRAME: 🟡
    → Bridge = "thuốc" (Mechanism §3.1): đúng liều → chữa bệnh / quá liều → ngộ độc
    → VN: bridge = quá liều + không ngưng → "ngộ độc bridge"
    → 4 nguồn fill: nguồn ④ dominate 12+ năm → ①②③ suppressed
    → Rút bridge đột ngột (ra đời 18+) → anchor crash → quarter-life crisis


WEAKNESS 5 [MEDIUM]: SURFACE ASSESSMENT

  DATA:
    → PISA 2022: 1% Level 5+ Đọc hiểu (OECD: 7%)
    → 5% Level 5-6 Toán (OECD: 9%)

  CẢI CÁCH ĐANG DIỄN RA (GDPT 2018):
    → Process assessment 30% → 50%, qualitative tiểu học
    → Hướng ĐÚNG, cần thời gian + depth quality

  FRAMEWORK REFRAME: 🟡
    → 4 stages depth (Mechanism §2.9):
      VN assess chủ yếu stage ① (recognize) → miss ②③④
    → Reward-Signal-Architecture v1.0: Evaluative reward chỉ fire khi depth THẬT SỰ compile
    → Multiple choice = KHÔNG trigger Evaluative → HS thiếu reward signal cho deep learning


WEAKNESS 6 [STRUCTURAL]: RURAL-URBAN + ETHNIC GAP

  DATA:
    → THPT enrollment: urban 82.4% vs rural 74.1%
    → Internet: richest 95% vs poorest 18%
    → 3 triệu+ DTTS không biết đọc viết (2023)
    → DTTS dropout: 2x Kinh, late enrollment: 5x

  TẠI SAO STRUCTURAL:
    → Vượt ngoài giáo dục → poverty, geography, language, infrastructure
    → Reform ưu tiên urban → rural hưởng lợi SAU + ÍT
    → = 2 VN education: (1) urban = "hệ thống có vấn đề"
      (2) rural DTTS = "chưa có hệ thống đầy đủ"
    → Foundation breadth (DKM §1): 3M+ illiterate = foundation CHƯA CÓ
```

```
TỔNG KẾT ĐIỂM YẾU — ƯU TIÊN: 🟡

  ┌───────────┬──────────────────────────────────────┬─────────────────┐
  │ Mức độ    │ Vấn đề                                │ Mechanism ref   │
  ├───────────┼──────────────────────────────────────┼─────────────────┤
  │ CRITICAL  │ Threat-dominant learning (direction)  │ §2.2 + §3.3    │
  │ HIGH      │ One-size-fits-all (hardware mismatch) │ §2.3            │
  │ HIGH      │ Imagine-Final sai hướng + narrow     │ §2.6 + §3.1    │
  │ MEDIUM    │ Bridge permanent + escalating         │ §3.1-§3.4      │
  │ MEDIUM    │ Surface assessment                    │ §2.9            │
  │ STRUCTURAL│ Rural-urban + ethnic gap              │ DKM §1, §2.3   │
  └───────────┴──────────────────────────────────────┴─────────────────┘

  NHẬN XÉT: 🟡
    → CRITICAL (direction): v7.8 reframe — KHÔNG CHỈ "giảm áp lực"
      mà "đổi NGUỒN áp lực" (Imposed → Domain)
    → Nhiều weaknesses LIÊN KẾT:
      threat-dominant (§2.2) ← bridge permanent (§3.1) ← surface assessment (§2.9)
      one-size (§2.3) → Imagine-Final sai (§2.6) → 60% trái ngành
```

---

## 4. DATA + EVIDENCE — TỔNG HỢP THEO CHỦ ĐỀ

```
MỤC ĐÍCH:
  → Tất cả data đã dùng trong §0-§3 → tổng hợp có hệ thống
  → Organized per topic → dễ tra cứu, dễ verify
  → 🟢 Data — all from verified sources
```

```
A. HỌC SINH + SỨC KHỎE TÂM THẦN

  ┌────────────────────────────────────────────┬──────────┬────────────┐
  │ Chỉ số                                     │ Số liệu  │ Nguồn/Năm  │
  ├────────────────────────────────────────────┼──────────┼────────────┤
  │ Trầm cảm HS THCS (13-17 tuổi)             │ 22.8%    │ PMC 2020   │
  │ Ý tưởng tự tử HS (13-17, Cần Thơ)         │ 26.3%    │ PMC 2020   │
  │ Ý tưởng tự tử nữ vs nam                   │ 21.4%/   │ UNICEF VN  │
  │                                             │ 7.9%     │            │
  │ HS THPT ngủ <7 giờ/ngày                    │ 80%      │ VnExpress  │
  │ HS quy thiếu ngủ = ôn thi                  │ 90%      │ VnExpress  │
  │ Áp lực phụ huynh = nguồn stress chính      │ 66%      │ PMC 2024   │
  │ HS tham gia học thêm (Huế, THCS)           │ 92.1%    │ PMC 2024   │
  │ Academic stress score (baseline → 3 năm)   │ 46.4→    │ PMC 2024   │
  │                                             │ 53.5/80  │ (Huế)     │
  │ Giờ học lớp 12 (trường + thêm + BT)        │ 12-15h/  │ VnExpress  │
  │                                             │ ngày     │            │
  │ Thanh niên 14-24 dùng MXH/ngày             │ 4.1h     │ BMC 2025   │
  │ MXH users có psychological distress         │ 50%      │ BMC 2025   │
  │ Bullying trong năm qua (Đà Nẵng, THCS)    │ 73.9%    │ ResGate    │
  │ Tỉ lệ tự tử (toàn bộ dân số)              │ 7.3/     │ WHO 2021   │
  │                                             │ 100K     │            │
  │ 1/5 HS cần hỗ trợ tâm lý, chỉ 8.4% tiếp  │          │ UNICEF/    │
  │ cận được                                    │          │ V-NAMHS    │
  └────────────────────────────────────────────┴──────────┴────────────┘


B. GIÁO VIÊN

  ┌────────────────────────────────────────────┬──────────┬────────────┐
  │ Chỉ số                                     │ Số liệu  │ Nguồn/Năm  │
  ├────────────────────────────────────────────┼──────────┼────────────┤
  │ Tổng GV giảng dạy                          │~1,251K   │ Statista24 │
  │ Thiếu GV                                   │ 102-120K │ MOET 24-25│
  │ GV nghỉ/rời nghề (2022-2023)               │ 19,300+  │ vietnam.vn │
  │ GV từ chức (08/2023-04/2024)               │ 7,215    │ vietnam.vn │
  │ HS/GV tiểu học                              │ 23.3:1   │ Statista24 │
  │ HS/GV THPT                                  │ 20.3:1   │ Statista24 │
  │ Lớp thực tế (Hà Nội, max)                  │ 60-69 HS │ KingsTT 25│
  │ Lương GV mới vào nghề                       │ 6.5-8M   │ vietnam.vn │
  │                                             │ VND/th   │            │
  │ TB lương lao động VN 2024                   │ 7.7M     │ VNPlus    │
  │                                             │ VND/th   │            │
  │ Hài lòng nghề nghiệp                       │ 97%      │ TALIS 24   │
  │ Xã hội tôn trọng nghề GV                   │ 92%      │ TALIS 24   │
  │ Stress công việc                            │ 4%       │ TALIS 24   │
  │ Đã dùng AI trong giảng dạy                 │ 64%      │ TALIS 24   │
  │ Thiếu cơ sở hạ tầng số                     │ 71%      │ TALIS 24   │
  │ Dự định rời nghề trong 5 năm               │ <6%      │ TALIS 24   │
  └────────────────────────────────────────────┴──────────┴────────────┘


C. HỌC THÊM (PRIVATE TUTORING)

  ┌────────────────────────────────────────────┬──────────┬────────────┐
  │ Chỉ số                                     │ Số liệu  │ Nguồn/Năm  │
  ├────────────────────────────────────────────┼──────────┼────────────┤
  │ Tỉ lệ HS học thêm (THPT, 2014)            │ 69.7%    │ PMC/WB 18  │
  │ Tỉ lệ HS học thêm (THCS, Huế, 2024)       │ 92.1%    │ PMC 2024   │
  │ Phụ huynh cho con học thêm                 │ 77%      │ EDT 2018   │
  │ Giờ học thêm / tuần (trung bình)           │ ~6h      │ PISA 2012  │
  │ So sánh quốc tế (expected for VN hours)    │ ~2h      │ PISA 2012  │
  │ Chi phí THCS / tháng                        │ ≥300K    │ vn.vn 24   │
  │                                             │ VND      │            │
  │ Chi phí THPT / tháng                        │ 400-500K │ vn.vn 24   │
  │                                             │ VND      │            │
  │ % chi phí GD gia đình = học thêm           │ 42-43%   │ PMC/WB 18  │
  │ Giàu chi gấp nghèo cho tutoring            │ 30x      │ PMC/WB 18  │
  │ Gia đình nghèo: % thu nhập cho HT lớp 12  │ ~50%     │ SciDirect  │
  │ PH cho rằng HT ảnh hưởng xấu sức khỏe    │ 49%      │ SciDirect21│
  └────────────────────────────────────────────┴──────────┴────────────┘


D. PISA + KẾT QUẢ HỌC TẬP

  ┌────────────────────────────────────────────┬──────────┬────────────┐
  │ Chỉ số                                     │ Số liệu  │ Nguồn/Năm  │
  ├────────────────────────────────────────────┼──────────┼────────────┤
  │ PISA 2022 Toán                              │ 469      │ OECD       │
  │ PISA 2022 Đọc hiểu                         │ 462      │ OECD       │
  │ PISA 2022 Khoa học                          │ 472      │ OECD       │
  │ Level 2+ Toán (vs OECD)                    │ 72%/69%  │ OECD       │
  │ Level 2+ Đọc (vs OECD)                     │ 77%/74%  │ OECD       │
  │ Level 2+ KH (vs OECD)                      │ 79%/76%  │ OECD       │
  │ Level 5-6 Toán (vs OECD)                   │ 5%/9%    │ OECD       │
  │ Level 5+ Đọc (vs OECD)                     │ 1%/7%    │ OECD       │
  │ SES giải thích variation (Toán)            │ 14.6%    │ OECD       │
  │ Xếp hạng 2022 (Toán/Đọc/KH)              │ 31/34/37 │ OECD       │
  │                                             │ /81      │            │
  └────────────────────────────────────────────┴──────────┴────────────┘

  Pattern QUAN TRỌNG: 🟡
    → Level 2+ (basics): VN = TỐT HƠN OECD → foundation STRONG
    → Level 5+ (deep): VN = THẤP HƠN NHIỀU OECD → depth WEAK
    → = System TỐT ở stage ① (recognize), YẾU ở stage ③④ (apply, create)
    → = Mechanism prediction confirmed: surface assessment → surface learning


E. CHÊNH LỆCH + TIẾP CẬN

  ┌────────────────────────────────────────────┬──────────┬────────────┐
  │ Chỉ số                                     │ Số liệu  │ Nguồn/Năm  │
  ├────────────────────────────────────────────┼──────────┼────────────┤
  │ Enrollment THPT: urban vs rural            │82.4%/    │ KingsTT 25│
  │                                             │74.1%     │            │
  │ Internet tại nhà: richest vs poorest       │ 95%/18%  │ UNESCO     │
  │ Ethnic minority: % dân số                  │ ~14%     │ GPE        │
  │ Ethnic minority: % người nghèo            │ 73%      │ GPE 2016   │
  │ Ethnic minority: hoàn thành THPT           │ 55-60%   │ KingsTT 25│
  │ Ethnic minority: dropout vs Kinh           │ 2x       │ Borgen     │
  │ Ethnic minority: late enrollment vs Kinh   │ 5x       │ Borgen     │
  │ Ethnic minority illiterate                  │ 3M+      │ KingsTT 25│
  │ VN language use at home (ethnic minority)  │ 5%       │ Springer   │
  │ Rural students thiếu tech cơ bản           │ ~50%     │ UNESCO 23  │
  │ Central Highlands GV shortage              │ 6,500+   │ KingsTT 25│
  │ HS/máy tính (national)                     │ ~3:1     │ UNESCO     │
  │ Internet penetration (toàn quốc)           │ 79.1%    │ DataRep 24│
  └────────────────────────────────────────────┴──────────┴────────────┘


F. ĐẠI HỌC + VIỆC LÀM

  ┌────────────────────────────────────────────┬──────────┬────────────┐
  │ Chỉ số                                     │ Số liệu  │ Nguồn/Năm  │
  ├────────────────────────────────────────────┼──────────┼────────────┤
  │ Số ĐH                                      │ 243      │ MOET 25    │
  │                                             │(176C/67T)│            │
  │ Enrollment thô ĐH                          │ 42.2%    │ WB 2022    │
  │ SV tốt nghiệp làm trái ngành              │ ~60%     │ Saigoneer  │
  │ Cử nhân thất nghiệp / năm                 │ 100K+    │ Saigoneer  │
  │ Nhà tuyển dụng không đủ ứng viên đạt CL   │ 41%      │ BritCouncil│
  │ ĐH VN trong QS World Rankings 2025        │ 6        │ QS         │
  │ ĐH VN trong QS Asia Rankings 2025         │ 17       │ QS         │
  │ ĐH VN trong THE World Rankings 2025       │ 9        │ THE        │
  │ EdTech startups                             │ 100+     │ VNPlus     │
  │ AI education market VN (2024)              │ $24M     │ IMARC      │
  │ AI education market VN (projected 2033)    │ $508M    │ IMARC      │
  │ MOET target: EdTech in public schools      │ 80%      │ Austrade   │
  │                                             │ by 2027  │            │
  └────────────────────────────────────────────┴──────────┴────────────┘
```

---

## 5. GAP ANALYSIS: HIỆN TẠI VS IDEAL

```
MỤC ĐÍCH:
  → IDEAL = Education-System.md v2.0 §0 (Imagine-Final hệ thống tối ưu)
  → HIỆN TẠI = §0-§4 data
  → GAP = khoảng cách CỤ THỂ per dimension
  → 🟡 Framework analysis — gap identification = derived, not verified
```

```
GAP PER DIMENSION:

  ┌──────────────────────┬─────────────────────┬────────────────────────┐
  │ Dimension            │ IDEAL (Ed-System    │ VN HIỆN TẠI            │
  │ (Mechanism ref)      │ v2.0)               │ (data §0-§4)           │
  ├──────────────────────┼─────────────────────┼────────────────────────┤
  │                      │                     │                        │
  │ Direction (§2.2)     │ Approach-path:      │ Threat-path:           │
  │                      │ novelty + curiosity │ punishment + shame     │
  │ GAP: █████████░ 90%  │                     │                        │
  │                      │                     │                        │
  │ Per-hardware (§2.3)  │ Per-individual:     │ One-size-fits-all:     │
  │                      │ calibrate per HW    │ 1 GV / 50 HS          │
  │ GAP: █████████░ 90%  │                     │                        │
  │                      │                     │                        │
  │ Foundation (DKM §1)  │ 6 domains balanced  │ 2/6 strong, 4/6 weak  │
  │ GAP: █████░░░░░ 50%  │                     │                        │
  │                      │                     │                        │
  │ Imagine-Final (§2.6) │ Per-learner:        │ External + narrow:     │
  │                      │ self-built, 4 góc   │ "thi đỗ → bằng → việc"│
  │ GAP: █████████░ 90%  │                     │                        │
  │                      │                     │                        │
  │ Bridge (§3.1-§3.4)  │ Scaffolding:        │ Permanent + escalating:│
  │                      │ ④ → ①②③ transition │ ④ dominant 12+ năm     │
  │ GAP: ████████░░ 80%  │                     │                        │
  │                      │                     │                        │
  │ 3 ORIGIN (§3.3)     │ Domain + Peer HIGH  │ Imposed DOMINANT       │
  │                      │ Imposed LOW         │ Domain + Peer LOW      │
  │ GAP: █████████░ 90%  │                     │                        │
  │                      │                     │                        │
  │ Consolidation (§2.8) │ Sleep + spacing     │ 80% ngủ <7h           │
  │                      │ + recovery          │ Cramming = norm        │
  │ GAP: ████████░░ 80%  │                     │                        │
  │                      │                     │                        │
  │ Depth (§2.9)        │ 4 stages measured   │ Stage ① dominant       │
  │ GAP: ██████░░░░ 60%  │ (GDPT 2018 helping) │                        │
  │                      │                     │                        │
  │ Adaptability         │ Meta-learning:      │ Rote memorization:     │
  │ (DKM §2)            │ "learn how to learn"│ 1% depth readers       │
  │ GAP: ███████░░░ 70%  │ (GDPT 2018 helping) │                        │
  │                      │                     │                        │
  │ I×S Balance (§1.3)  │ Individual CÓ KHẢ   │ Society >>>            │
  │                      │ NĂNG + MUỐN +       │ Individual MUỐN        │
  │                      │ Society CẦN = match │ "Nghề hot" > sở thích  │
  │ GAP: ████████░░ 80%  │                     │                        │
  │                      │                     │                        │
  │ Ecosystem (§1.4+§4) │ 4 kênh balanced     │ School + tutoring      │
  │ GAP: ███████░░░ 70%  │                     │ = 90%+ learning time   │
  │                      │                     │                        │
  │ Teacher role         │ Calibrator:         │ Knowledge source:      │
  │ (Ed-System v2.0 §7) │ observe + adjust    │ lecture + transmit     │
  │ GAP: ███████░░░ 70%  │ (NHƯNG: hài lòng   │                        │
  │                      │ 97% = platform!)    │                        │
  │                      │                     │                        │
  │ Parent role          │ Environment         │ Pressure source:       │
  │ (Ed-System v2.0 §8) │ designer            │ "con phải giỏi"       │
  │ GAP: ███████░░░ 70%  │ (NHƯNG: involvement │                        │
  │                      │ cao = redirectable!) │                        │
  └──────────────────────┴─────────────────────┴────────────────────────┘


TỔNG QUAN GAP: 🟡

  Gaps LỚN NHẤT (80-90%):
    → Direction (90%): threat-path dominant → avoidance-tagged learning
    → Per-hardware (90%): structural (class size, teacher shortage)
    → Imagine-Final (90%): cultural (family-driven, credential culture)
    → 3 ORIGIN (90%): Imposed dominant, Domain+Peer suppressed
    → Bridge (80%): permanent + escalating → anchor dependency
    → Consolidation (80%): sleep deprivation, cramming culture
    → I×S Balance (80%): society >>> individual

  Gaps TRUNG BÌNH (50-70%):
    → Foundation (50%): strong in 2/6 domains (cognitive+linguistic)
    → Depth (60%): GDPT 2018 reform đang diễn ra
    → Adaptability (70%): GDPT 2018 targeting
    → Ecosystem (70%): AI emerging (64% GV đã dùng)
    → Teacher role (70%): willing workforce, needs retraining
    → Parent role (70%): high involvement, redirectable

  ĐIỂM SÁNG:
    → Foundation literacy/numeracy = gap NHỎ NHẤT
    → Teacher willingness = PLATFORM cho closing gaps
    → GDPT 2018 = đang close gaps ở depth + adaptability + feedback
    → Family involvement = redirectable (gap CÓ THỂ close nhanh NẾU redirect đúng)
    → AI adoption by teachers (64%) = ahead of OECD


  ⚠️ QUAN TRỌNG — GAP ≠ BLAME:
    → Gaps = khoảng cách giữa IDEAL (file lý thuyết) và REALITY
    → IDEAL = CHƯA CÓ NƯỚC NÀO đạt được (kể cả Finland)
    → Nhiều gaps = UNIVERSAL (mọi nước đều có), không riêng VN
    → Mục đích: NHẬN DIỆN → ưu tiên → cải thiện dần
```

---

## 6. HONEST ASSESSMENT

```
GIỚI HẠN CỦA PHÂN TÍCH NÀY:

  ① OUTSIDER BIAS:
    → Framework = built bởi 1 người (dù Vietnamese), từ góc nhìn researcher
    → Chưa validated bởi: GV VN, PH VN, HS VN, chuyên gia GD VN
    → Risk: oversimplify, romanticize problems, miss context quan trọng

  ② FRAMEWORK AS LENS — NOT TRUTH:
    → Education-Mechanism v1.0: 8 nguyên lý = DERIVED từ brain mechanism
    → Chưa validated as evaluation tool cho hệ thống giáo dục
    → Ví dụ: §2.2 (Direction > Level) → framework nói threat-path = xấu
      → Nhưng VN PISA scores CAO với threat-path → contradiction?
      → Có thể: scores ≠ deep learning (PISA Level 5+ data confirms)
      → Nhưng: CHƯA CHỨNG MINH hoàn toàn
    → Framework = 1 lens → cần NHIỀU lens khác

  ③ DATA QUALITY:
    → PISA: có thể sampling bias (exclude out-of-school students)
    → Mental health data: chủ yếu từ specific cities (không representative toàn quốc)
    → Private tutoring data: 2014 survey → có thể đã thay đổi
    → TALIS 2024: self-reported → social desirability bias
    → SỐ LIỆU TỪ NHIỀU NĂM KHÁC NHAU → snapshot KHÔNG đồng nhất

  ④ MISSING VOICES:
    → HS: data ABOUT them, không FROM them
    → GV: TALIS = survey → có thể khác thực tế lớp học
    → Ethnic minorities: data ít + có thể underreported

  ⑤ GDPT 2018 = ĐANG DIỄN RA:
    → 12/12 lớp mới hoàn thành rollout 2024-2025
    → = Chưa có data outcomes → đánh giá = quá sớm
    → Nhiều "weaknesses" CÓ THỂ đang được address

  ⑥ CULTURE ≠ PROBLEM:
    → File có thể tạo ấn tượng văn hóa VN = "xấu" cho GD
    → KHÔNG PHẢI: văn hóa = CONTEXT, có cả strengths + weaknesses
    → Family involvement, teacher respect, foundation emphasis = STRENGTHS
    → Chi tiết: xem VN-Cultural-Factors.md (File 2)


TÓM LẠI — CONFIDENCE LEVELS:

  ┌──────────────────────────────────┬────────────┬─────────────────────┐
  │ Phần                             │ Confidence │ Giải thích          │
  ├──────────────────────────────────┼────────────┼─────────────────────┤
  │ §0 Data (structure, numbers)     │ 🟢         │ Verified sources    │
  │ §1 Mechanism evaluation (new)   │ 🟡         │ Framework analysis  │
  │ §2 Strengths identification     │ 🟡         │ Data + interpretation│
  │ §3 Weakness prioritization      │ 🟡         │ Subjective ranking  │
  │ §4 Data tables                   │ 🟢         │ Sources cited       │
  │ §5 Gap analysis                  │ 🟡→🔴      │ Ideal = theoretical │
  │ §5 Gap percentages              │ 🔴         │ Rough estimates     │
  └──────────────────────────────────┴────────────┴─────────────────────┘


KHUYẾN NGHỊ ĐỌC:

  → ĐỌC NHƯ: "Education-Mechanism lens NHÌN VN thế nào" — 1 perspective
  → KHÔNG ĐỌC NHƯ: "VN education = thất bại"
  → CẦN BỔ SUNG: chuyên gia GD VN, GV thực tế, HS thực tế
  → CẦN CẬP NHẬT: khi GDPT 2018 có outcome data (~2027-2028)
  → TIẾP THEO: VN-Cultural-Factors.md → phân tích văn hóa
    → VN-Recommendations.md → hướng đi cụ thể
```

---

## KẾT NỐI

```
FILE NÀY KẾT NỐI VỚI:

  ← INPUT — NỀN TẢNG ĐÁNH GIÁ (5 tầng):

    TẦNG 1 — Core-Deep-Dive/:
      Core-Software.md v1.0 — cycle-based architecture
      Core-Hardware.md v1.0 — 4 zones A/B/C/D
      Cortisol-Baseline.md v2.0 — amplifier reframe, 5 Roles
      Imagine-Final.md — lifecycle 5 phases
      Reward-Signal-Architecture.md v1.0 — Evaluative/Direct-State reward
      Body-Feedback-Mechanism.md v1.2 — 2 sources × 3 dynamics
      Agent-Mechanism.md v1.0 — Self-Pattern-Modeling Compiled/Fresh

    TẦNG 2 — Research/Child-Development/:
      Child-Development-Mechanism.md — 4+1 compile, approach/avoidance
      Natural-Development.md — hardware at birth
      Skill-Introduction.md — 0-6 skill development

    TẦNG 3 — Research/Education/:
      Education-Mechanism.md v1.0 ⭐ — 8 nguyên lý + bridge + AI model
      Domain-Knowledge-Map.md v1.0 — 3-tier domain taxonomy
      Observation/Expansion-Saturation-Crisis.md v1.0 — grad unemployment

    TẦNG 4 — Applications/Education/:
      Education-System.md v2.0 — Imagine-Final ideal + constraints
      Hardware-Calibration.md v1.0 — per-individual dimensions
      Era-Analysis-2025.md v2.0 — era context 2025+
      Curriculum-Framework.md v2.0 — 3-tier curriculum + delivery

    TẦNG 5 — FOLDER NÀY:
      VN-Education-Status.md v2.0 ← FILE NÀY (data + mechanism evaluation)

  → OUTPUT (sẽ dùng file này):
    VN-Cultural-Factors.md — §1 analysis dùng data từ file này
    VN-Recommendations.md — §0 Imagine-Final + §1 priorities = based on gaps từ §5


  KEY TAKEAWAYS TO CARRY FORWARD:

    → Mechanism evaluation: 6/8 nguyên lý arc design = ✗ (violate)
    → v7.8 INSIGHT MỚI: direction SAI (không chỉ level cao)
      → 3 ORIGIN: Imposed dominant, Domain+Peer suppressed
      → 4 nguồn: ④ External dominant 12+ năm, ①②③ suppressed
    → CRITICAL: threat-dominant learning → avoidance-tagged chunks
    → STRENGTHS: foundation literacy, teacher platform (97% hài lòng),
      GDPT 2018 direction, family involvement (redirectable)
    → TOP GAPS: direction 90%, per-hardware 90%, Imagine-Final 90%, 3 ORIGIN 90%
    → GDPT 2018 = BỔ SUNG tốt (feedback + depth + adaptability)
      nhưng CHƯA COVER: direction, 3 ORIGIN, 4 nguồn, mini-arcs
```
