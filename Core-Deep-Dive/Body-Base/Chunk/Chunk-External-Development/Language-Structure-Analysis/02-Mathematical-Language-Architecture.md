---
title: Mathematical Language Architecture — Cấu trúc ngôn ngữ toán học
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — tài liệu tham khảo, đọc nghiền ngẫm
scope: Toán học như 1 hệ thống "ngôn ngữ" — ký hiệu, cú pháp, cấu trúc, so sánh với natural language
purpose: Hiểu toán không phải để "giải bài" mà để thấy kiến trúc của nó như 1 communication format
parent: ../../plan.md (F3 Chunk-External-Development)
language: Tiếng Việt primary + English technical + ký hiệu toán
note: Viết cho người DÙNG toán hàng ngày nhưng chưa từng "mổ xẻ" cấu trúc của nó
---

# Mathematical Language Architecture — Cấu trúc ngôn ngữ toán học

> **Mục đích**: Bạn dùng toán mỗi ngày (tính tiền, đo lường, code game physics,...) nhưng chưa bao giờ nhìn toán như 1 HỆ THỐNG NGÔN NGỮ. File này "mổ xẻ" cấu trúc toán — không phải để giải bài, mà để thấy toán là 1 communication format có "từ vựng", "ngữ pháp", "câu", "đoạn văn" riêng.
>
> **So sánh với file 01**: File 01 phân tích natural language (Việt/Anh/Trung). File này phân tích mathematical language. Cả 2 đều là Communication Modality formats — nhưng kiến trúc RẤT KHÁC nhau.
>
> **Cách đọc**: Đọc từng phần, nghiền ngẫm. Không cần biết giải toán cao cấp — file focus vào CẤU TRÚC, không focus vào KỸ NĂNG GIẢI.

---

## MỤC LỤC

- §1 — "Từ vựng" toán: Các loại ký hiệu
  - §1.1 Numbers — Hệ thống số
  - §1.2 Variables — Biến
  - §1.3 Operators — Phép toán
  - §1.4 Relations — Quan hệ
  - §1.5 Grouping — Dấu ngoặc
  - §1.6 Functions — Hàm
  - §1.7 Constants — Hằng số đặc biệt
  - §1.8 Logic symbols — Ký hiệu logic
  - §1.9 Set theory — Ký hiệu tập hợp
  - §1.10 Calculus — Ký hiệu giải tích
  - §1.11 Bảng tổng hợp "từ vựng" toán
- §2 — "Ngữ pháp" toán: Cú pháp biểu thức
  - §2.1 Biểu thức = "câu" toán
  - §2.2 Thứ tự phép toán = "ngữ pháp" toán
  - §2.3 Infix, Prefix, Postfix — 3 cách viết cùng 1 ý
  - §2.4 Nesting — Lồng nhau (recursion)
  - §2.5 Phương trình = "câu khẳng định"
  - §2.6 Bất phương trình = "câu so sánh"
  - §2.7 Hệ phương trình = "đoạn văn"
- §3 — Hierarchy: Từ → Biểu thức → Phương trình → Chứng minh → Lý thuyết
- §4 — Các "domain" toán và ký hiệu riêng
  - §4.1 Số học (Arithmetic)
  - §4.2 Đại số (Algebra)
  - §4.3 Hình học (Geometry)
  - §4.4 Giải tích (Calculus)
  - §4.5 Xác suất & Thống kê
  - §4.6 Logic
  - §4.7 Đại số tuyến tính (Linear Algebra)
- §5 — So sánh: Toán vs Natural Language
- §6 — Toán trong thực tế: Cách expert THỰC SỰ dùng toán
- §7 — Lịch sử phát triển ký hiệu toán
- §8 — Framework lens + Câu hỏi mở

---

## §1 — "Từ vựng" toán: Các loại ký hiệu

Natural language có danh từ, động từ, tính từ,... Toán cũng có "từ loại" riêng:

### §1.1 — Numbers (Số) = "Danh từ" của toán

Số = đối tượng cơ bản nhất, tương đương danh từ trong natural language.

```
SỐ TỰ NHIÊN (Natural numbers — ℕ):
  0, 1, 2, 3, 4, 5, ...
  → Đếm vật: "có 3 con chó" → 3 ∈ ℕ
  → Cổ nhất: từ khi con người biết đếm (~40,000 năm?)

SỐ NGUYÊN (Integers — ℤ):
  ..., -3, -2, -1, 0, 1, 2, 3, ...
  → Thêm số ÂM: "nợ 5 triệu" → -5
  → ℤ từ tiếng Đức "Zahlen" = "số"
  → Phát minh: ~600 CN (Ấn Độ, Brahmagupta)

SỐ HỮU TỈ (Rational numbers — ℚ):
  1/2, 3/4, -2/3, 0.75, 1.333...
  → Mọi số viết được dạng p/q (phân số)
  → ℚ từ "Quotient" = "thương"
  → Phát minh: ~1500 TCN (Ai Cập, Rhind Papyrus)

SỐ VÔ TỈ (Irrational numbers):
  √2 = 1.41421356..., π = 3.14159265..., e = 2.71828182...
  → KHÔNG viết được dạng phân số
  → Số thập phân vô hạn KHÔNG tuần hoàn
  → Phát minh √2 (shock!): ~500 TCN (Hy Lạp, Pythagoras)
    → Truyền thuyết: Hippasus chứng minh √2 vô tỉ → bị ném xuống biển
       vì phá vỡ niềm tin "mọi thứ là tỉ lệ số nguyên"

SỐ THỰC (Real numbers — ℝ):
  Tất cả số trên trục số: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
  → Gồm cả hữu tỉ + vô tỉ
  → Hình dung: mỗi ĐIỂM trên đường thẳng = 1 số thực

SỐ PHỨC (Complex numbers — ℂ):
  a + bi, trong đó i = √(-1)
  → Ví dụ: 3 + 2i, -1 + 0.5i
  → i² = -1 (căn bậc 2 của -1 — "impossible" nhưng hữu ích!)
  → Dùng nhiều trong: điện tử, vật lý lượng tử, game (quaternion cho 3D rotation!)
  → Phát minh: ~1545 (Cardano, giải phương trình bậc 3)

HÌNH DUNG: Các tầng số lồng nhau
  ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ
  │    │    │    │    │
  │    │    │    │    └── Số phức (thêm chiều "ảo")
  │    │    │    └── Số thực (lấp đầy trục số)
  │    │    └── Số hữu tỉ (phân số)
  │    └── Số nguyên (thêm số âm)
  └── Số tự nhiên (đếm)

  → Mỗi tầng = MỞ RỘNG tầng trước để giải quyết vấn đề mới:
    "3 - 5 = ?" → cần ℤ (số âm)
    "1 ÷ 3 = ?" → cần ℚ (phân số)
    "√2 = ?"    → cần ℝ (số vô tỉ)
    "√(-1) = ?" → cần ℂ (số phức)
```

### §1.2 — Variables (Biến) = "Đại từ" của toán

```
BIẾN = ký hiệu đại diện cho số CHƯA BIẾT hoặc số BẤT KỲ
  → Giống "đại từ" trong natural language: "nó" thay cho danh từ cụ thể

QUY ƯỚC THƯỜNG DÙNG:
  x, y, z         = biến chưa biết (unknown) — giải phương trình để tìm
  a, b, c         = hệ số / hằng số đã biết (parameters)
  n, m, k         = số nguyên (thường dùng cho đếm, index)
  i, j            = chỉ số vòng lặp (index) — game dev quen cái này!
  t               = thời gian (time)
  f, g, h         = hàm (function)
  θ (theta)       = góc (angle)
  Δ (delta)       = thay đổi / chênh lệch ("delta x" = x thay đổi bao nhiêu)
  Σ (sigma)       = tổng (sum)
  ε (epsilon)     = số rất nhỏ (gần 0)
  ∞ (infinity)    = vô cùng

VÍ DỤ:
  "x + 3 = 7"    → x = đại từ, thay cho số 4 (chưa biết, cần tìm)
  "cho mọi n"    → n = đại từ, thay cho "số nguyên bất kỳ"
  "f(x) = x²"   → x = input bất kỳ, f = hàm bình phương

SO SÁNH VỚI NATURAL LANGUAGE:
  Natural:  "NÓ ăn cơm"       → "nó" = đại diện cho ai đó (cần context)
  Toán:     "x + 3 = 7"       → "x" = đại diện cho số nào đó (cần giải)

  Natural:  "MỌI NGƯỜI đều ăn" → "mọi người" = tất cả
  Toán:     "∀x: x + 0 = x"   → "∀x" = "cho mọi x" = tất cả số
```

### §1.3 — Operators (Phép toán) = "Động từ" của toán

```
PHÉP TOÁN = hành động thực hiện lên số, tương đương ĐỘNG TỪ trong natural language

ARITHMETIC (Số học cơ bản):
  +    cộng (addition)          3 + 2 = 5
  -    trừ (subtraction)        7 - 4 = 3
  ×    nhân (multiplication)    3 × 4 = 12    (cũng viết: 3·4 hoặc 3*4)
  ÷    chia (division)          12 ÷ 3 = 4    (cũng viết: 12/3)
  ^    lũy thừa (exponent)     2³ = 8         (2 mũ 3 = 2×2×2)
  √    căn (root)              √9 = 3         (căn bậc 2 của 9)
  !    giai thừa (factorial)   5! = 120        (5×4×3×2×1)
  %    phần trăm (percent)     50% = 0.5
  mod  phần dư (modulo)        7 mod 3 = 1    (7 chia 3 dư 1 — game dev dùng nhiều!)

ALGEBRA (Đại số):
  Σ    tổng (summation)        Σᵢ₌₁ⁿ i = 1+2+3+...+n
  Π    tích (product)          Πᵢ₌₁ⁿ i = 1×2×3×...×n = n!
  |x|  giá trị tuyệt đối      |-5| = 5, |3| = 3
  ⌊x⌋  floor (làm tròn xuống) ⌊3.7⌋ = 3
  ⌈x⌉  ceiling (làm tròn lên) ⌈3.2⌉ = 4

SO SÁNH VỚI NATURAL LANGUAGE:
  Natural:  "Tôi  ĂN   cơm"        → ĂN = động từ (hành động)
  Toán:     "3    +     2    = 5"   → + = "động từ" (hành động cộng)

  Natural:  Có nhiều loại động từ (ăn, chạy, nghĩ, yêu, sợ,...)
  Toán:     Có ít "động từ" hơn nhưng mỗi cái CỰC KỲ CHÍNH XÁC
            (+ luôn nghĩa cộng, không bao giờ nghĩa khác)
```

### §1.4 — Relations (Quan hệ) = "Liên từ so sánh" của toán

```
RELATIONS = ký hiệu thể hiện QUAN HỆ giữa 2 biểu thức

  =     bằng (equal)              3 + 2 = 5
  ≠     không bằng (not equal)    3 ≠ 4
  <     nhỏ hơn (less than)       2 < 5
  >     lớn hơn (greater than)    7 > 3
  ≤     nhỏ hơn hoặc bằng        x ≤ 10
  ≥     lớn hơn hoặc bằng        y ≥ 0
  ≈     xấp xỉ (approximately)   π ≈ 3.14
  ∝     tỉ lệ (proportional)     F ∝ ma (lực tỉ lệ khối lượng × gia tốc)
  ≡     đồng nhất / đồng dư      a ≡ b (mod n)
  ~     tương đương (varies)      f(x) ~ g(x)

⭐ DẤU "=" TRONG TOÁN vs TRONG CODE:
  Toán:  x = 5      → "x BẰNG 5" (khẳng định sự thật)
  Code:  x = 5      → "GÁN 5 vào x" (hành động thay đổi)
  Code:  x == 5     → "x CÓ BẰNG 5 KHÔNG?" (kiểm tra)

  → Game dev quen "=" là gán. Toán dùng "=" là khẳng định.
  → Đây là nguồn confuse kinh điển giữa math và programming.
```

### §1.5 — Grouping (Nhóm) = "Dấu câu" của toán

```
DẤU NGOẶC = kiểm soát THỨ TỰ xử lý, tương đương dấu câu trong natural language

  ( )    ngoặc tròn (parentheses)       (3 + 2) × 4 = 20
  [ ]    ngoặc vuông (brackets)          [a + b] × c
  { }    ngoặc nhọn (braces)            {1, 2, 3} = tập hợp
  | |    giá trị tuyệt đối / norm       |x| = absolute value

THỨ TỰ ƯU TIÊN (nếu KHÔNG có ngoặc):
  1. ( ) ngoặc                         ← ưu tiên cao nhất
  2. ^ lũy thừa
  3. × ÷ nhân chia                     ← từ trái qua phải
  4. + - cộng trừ                      ← từ trái qua phải, ưu tiên thấp nhất

VÍ DỤ — cùng 1 phép tính, KHÁC NGOẶC = KHÁC KẾT QUẢ:
  3 + 2 × 4   = 3 + 8   = 11    (nhân trước)
  (3 + 2) × 4 = 5 × 4   = 20    (ngoặc trước, rồi nhân)

SO SÁNH VỚI NATURAL LANGUAGE:
  Natural:  Dấu phẩy, dấu chấm, ngoặc = kiểm soát cách HIỂU câu
            "Ăn bạn ơi" vs "Ăn, bạn ơi!" ← dấu phẩy đổi nghĩa hoàn toàn!
  Toán:     Dấu ngoặc = kiểm soát cách TÍNH biểu thức
            3+2×4 vs (3+2)×4 ← ngoặc đổi kết quả hoàn toàn!

  → Cả 2 hệ thống: dấu câu/ngoặc = CONSTRAINT cách parser xử lý
```

### §1.6 — Functions (Hàm) = "Máy xử lý" — input vào, output ra

```
HÀM = "máy" nhận INPUT, cho OUTPUT theo quy tắc cố định

CÚ PHÁP: f(x) = biểu thức chứa x
  → f = tên hàm
  → x = input (argument)
  → biểu thức = quy tắc xử lý
  → f(x) = output

HÀM CƠ BẢN:

  Hàm tuyến tính:    f(x) = 2x + 3
    f(0) = 3, f(1) = 5, f(10) = 23
    → Input × 2, rồi cộng 3

  Hàm bậc 2:         f(x) = x²
    f(0) = 0, f(2) = 4, f(-3) = 9
    → Input nhân chính nó (bình phương)

  Hàm lượng giác:
    sin(θ)   = đối / huyền     (tỉ lệ cạnh tam giác vuông — game dev dùng RẤT NHIỀU!)
    cos(θ)   = kề / huyền
    tan(θ)   = đối / kề = sin(θ)/cos(θ)

    Ví dụ game dev:
      Nhân vật quay 45° và đi tới 10 đơn vị:
      dx = 10 × cos(45°) ≈ 7.07    (dịch chuyển theo x)
      dy = 10 × sin(45°) ≈ 7.07    (dịch chuyển theo y)
      → sin/cos = "dịch angle thành tọa độ x,y"

  Hàm logarithm:
    log₁₀(100) = 2    vì 10² = 100    ("10 mũ mấy = 100?" → 2)
    log₂(8)    = 3    vì 2³ = 8       ("2 mũ mấy = 8?" → 3)
    ln(e)      = 1    vì e¹ = e       (ln = log tự nhiên, cơ số e)

    → log = PHÉP NGƯỢC của lũy thừa
    → Game dev dùng: log₂(n) = complexity thuật toán binary search

  Hàm mũ (exponential):
    eˣ      (e ≈ 2.71828, "số Euler")
    2ˣ      (tăng gấp đôi mỗi bước)

    → Tăng trưởng mũ: 2⁰=1, 2¹=2, 2²=4, 2³=8, 2¹⁰=1024, 2²⁰=1,048,576
    → Game dev: 2ⁿ = kích thước texture, memory allocation

SO SÁNH VỚI NATURAL LANGUAGE:
  Natural:  Câu = Subject + Verb + Object
  Toán:     Expression = Function(Argument) = Result
            f(x) = y tương đương "hàm f XỬ LÝ input x, cho ra y"

  Natural language functions (metaphor):
    "dịch(câu tiếng Việt)" = câu tiếng Anh
    "nấu(nguyên liệu)" = món ăn
    → Mọi PROCESS có input + output = function!
```

### §1.7 — Constants (Hằng số) = "Tên riêng" của toán

```
HẰNG SỐ = số CỤ THỂ có tên riêng vì quá quan trọng / xuất hiện quá nhiều

  π (pi)     ≈ 3.14159265...    Tỉ lệ chu vi / đường kính hình tròn
                                 → Xuất hiện KHẮP NƠI: tròn, sóng, dao động, xác suất
                                 → Game dev: rotation, circular motion, wave patterns

  e (Euler)  ≈ 2.71828182...    Cơ số logarithm tự nhiên
                                 → Tăng trưởng liên tục: lãi kép, phân rã phóng xạ
                                 → eˣ = hàm DUY NHẤT mà đạo hàm = chính nó

  φ (phi)    ≈ 1.61803398...    Tỉ lệ vàng (golden ratio)
                                 → (1 + √5) / 2
                                 → Xuất hiện trong: kiến trúc, nghệ thuật, tự nhiên (vỏ ốc, hoa)

  i          = √(-1)            Đơn vị ảo (imaginary unit)
                                 → i² = -1
                                 → Game dev: quaternion dùng i, j, k cho 3D rotation

  ∞          = vô cùng          Không phải số, mà là CONCEPT
                                 → "lớn hơn mọi số"
                                 → Dùng trong: giới hạn, tích phân, series

SO SÁNH:
  Natural language "tên riêng": Hà Nội, Einstein, Everest — tên CHO 1 THỨ CỤ THỂ
  Math constants:               π, e, φ — tên CHO 1 SỐ CỤ THỂ xuất hiện khắp nơi
```

### §1.8 — Logic symbols = "Liên từ" + "Phủ định" + "Lượng từ"

```
LOGIC = hệ thống suy luận CHÍNH XÁC, nền tảng cho mọi chứng minh toán

LIÊN TỪ LOGIC (Logical connectives):
  ∧   AND (và)           p ∧ q = "p VÀ q đều đúng"
  ∨   OR (hoặc)          p ∨ q = "p HOẶC q (hoặc cả 2) đúng"
  ¬   NOT (phủ định)     ¬p = "p KHÔNG đúng"
  →   IMPLIES (suy ra)   p → q = "NẾU p THÌ q"
  ↔   IFF (khi và chỉ khi) p ↔ q = "p ĐÚNG khi và chỉ khi q ĐÚNG"

LƯỢNG TỪ (Quantifiers):
  ∀   FOR ALL (cho mọi)       ∀x: x + 0 = x    "với MỌI x, x cộng 0 bằng x"
  ∃   EXISTS (tồn tại)        ∃x: x² = 4        "TỒN TẠI x mà x² = 4" (x = 2 hoặc -2)
  ∄   NOT EXISTS              ∄x: x² = -1 (∈ℝ)  "KHÔNG tồn tại x thực mà x² = -1"

VÍ DỤ GHÉP:
  ∀x ∈ ℝ: x² ≥ 0
  = "Cho MỌI x thuộc số thực: x bình phương LỚN HƠN HOẶC BẰNG 0"
  = "Bình phương số thực nào cũng không âm"

  ∃x ∈ ℤ: (x > 0) ∧ (x < 1)
  = "Tồn tại x thuộc số nguyên mà: x > 0 VÀ x < 1"
  = "Có số nguyên nào lớn hơn 0 và nhỏ hơn 1 không?"
  → Câu trả lời: KHÔNG (∄) — vì không có số nguyên nào giữa 0 và 1

SO SÁNH VỚI NATURAL LANGUAGE:
  Natural:  "nếu trời mưa THÌ tôi ở nhà"       → VÀ, HOẶC, NẾU...THÌ, KHÔNG
  Toán:     "nếu p đúng THÌ q đúng" = p → q    → ∧, ∨, →, ¬

  Natural:  "MỌI NGƯỜI đều ăn" / "CÓ AI ĐÓ ăn"
  Toán:     "∀x: f(x)" / "∃x: f(x)"

  → CÙNG loại concept (và, hoặc, không, mọi, tồn tại)
  → Toán: CHÍNH XÁC (không mơ hồ)
  → Natural: LINH HOẠT (có thể mơ hồ, đa nghĩa)

  Ví dụ MƠ HỒ trong natural language:
    "Tôi thấy ai đó" = ∃x: tôi thấy x (OK)
    "Ai cũng thấy" = ∀x: x thấy (?) hay ∃x: mọi người thấy x (?)
    → Tiếng Việt MƠ HỒ! Toán KHÔNG MƠ HỒ: phải viết rõ ∀ hay ∃
```

### §1.9 — Set theory symbols = "Nhóm" + "Thuộc về"

```
TẬP HỢP (Set) = nhóm các phần tử

  {1, 2, 3}          tập hợp chứa 1, 2, 3
  ∅ hoặc {}           tập rỗng (không chứa gì)
  ∈                   thuộc (element of)        3 ∈ {1,2,3} = "3 THUỘC tập {1,2,3}"
  ∉                   không thuộc               4 ∉ {1,2,3}
  ⊂                   tập con (subset)          {1,2} ⊂ {1,2,3}
  ∪                   hợp (union)               {1,2} ∪ {2,3} = {1,2,3}
  ∩                   giao (intersection)       {1,2} ∩ {2,3} = {2}
  \                   hiệu (difference)         {1,2,3} \ {2} = {1,3}
  |A|                 lực lượng (cardinality)   |{1,2,3}| = 3 (có 3 phần tử)

SO SÁNH VỚI CODE (game dev quen):
  Set   ↔ HashSet, Set, List (unique)
  ∈     ↔ contains(), includes(), in
  ∪     ↔ union(), concat() + unique
  ∩     ↔ intersection(), filter()
  |A|   ↔ .length, .count, .size
```

### §1.10 — Calculus symbols = "Thay đổi" + "Tích lũy"

```
GIẢI TÍCH (Calculus) = toán học về SỰ THAY ĐỔI và TÍCH LŨY
  → Newton + Leibniz phát minh ~1687
  → Nền tảng của: vật lý, kỹ thuật, kinh tế, machine learning

ĐẠO HÀM (Derivative) — "tốc độ thay đổi tại 1 điểm":
  f'(x) hoặc df/dx hoặc dy/dx

  Ý nghĩa: nếu f(x) = vị trí xe tại thời điểm x
    → f'(x) = VẬN TỐC xe tại thời điểm x (tốc độ thay đổi vị trí)
    → f''(x) = GIA TỐC xe (tốc độ thay đổi vận tốc)

  Ví dụ:
    f(x) = x²          → f'(x) = 2x
    (vị trí = x²)         (vận tốc = 2x: tăng dần)

    f(x) = 3x + 5      → f'(x) = 3
    (vị trí = 3x+5)       (vận tốc = 3: không đổi, đều)

  Game dev dùng đạo hàm:
    position' = velocity (vận tốc = đạo hàm vị trí)
    velocity' = acceleration (gia tốc = đạo hàm vận tốc)
    → Physics engine: mỗi frame tính position += velocity × dt

TÍCH PHÂN (Integral) — "tổng tích lũy":
  ∫ f(x) dx = diện tích dưới đồ thị f(x)

  Ý nghĩa: nếu f(x) = vận tốc xe
    → ∫ f(x) dx = QUÃNG ĐƯỜNG đã đi (tích lũy vận tốc qua thời gian)

  Ký hiệu:
    ∫₀¹⁰ v(t) dt = quãng đường từ t=0 đến t=10
    (tích phân vận tốc từ 0 đến 10 giây = tổng quãng đường)

  Game dev dùng tích phân (thường ẩn):
    position = ∫ velocity dt     → mỗi frame: pos += vel × deltaTime
    velocity = ∫ acceleration dt → mỗi frame: vel += acc × deltaTime
    → Euler integration — chính là tích phân rời rạc!

GIỚI HẠN (Limit):
  lim(x→a) f(x) = "f(x) tiến tới giá trị gì khi x TIẾN GẦN a"

  Ví dụ:
    lim(x→0) sin(x)/x = 1    (khi x tiến gần 0, sin(x)/x tiến gần 1)

  → Giới hạn là NỀN TẢNG cho cả đạo hàm và tích phân
  → Đạo hàm = giới hạn tỉ lệ thay đổi khi khoảng cách tiến về 0
  → Tích phân = giới hạn tổng diện tích khi chia nhỏ vô hạn

ĐẠO HÀM + TÍCH PHÂN = 2 MẶT CỦA 1 ĐỒNG XU:
  Đạo hàm: biết TỔNG → tìm TỐC ĐỘ THAY ĐỔI tại mỗi điểm
  Tích phân: biết TỐC ĐỘ THAY ĐỔI → tìm TỔNG tích lũy
  → Fundamental Theorem of Calculus: ∫ f'(x) dx = f(x) + C
  → "Tích phân là phép ngược của đạo hàm"
```

### §1.11 — Bảng tổng hợp "từ vựng" toán

| Loại ký hiệu toán | Tương đương Natural Language | Ví dụ | Số lượng ước tính |
|---|---|---|---|
| Numbers (số) | Danh từ cụ thể | 1, 2, π, e, √2 | ∞ (vô hạn loại số) |
| Variables (biến) | Đại từ | x, y, n, θ | ~30 ký hiệu thường dùng |
| Operators (phép toán) | Động từ | +, -, ×, ÷, ^, √, Σ, ∫ | ~30 phép toán thường dùng |
| Relations (quan hệ) | Liên từ so sánh | =, <, >, ≤, ≈, ∈ | ~15 |
| Grouping (ngoặc) | Dấu câu | (, ), [, ], {, } | 6 |
| Functions (hàm) | Máy xử lý / Verb phrase | sin, cos, log, f(x) | ~20 cơ bản + vô hạn custom |
| Constants (hằng số) | Tên riêng | π, e, φ, i, ∞ | ~10 quan trọng |
| Logic (logic) | Liên từ + Phủ định + Lượng từ | ∧, ∨, ¬, →, ∀, ∃ | ~10 |
| Set theory (tập hợp) | Nhóm + Thuộc về | ∈, ⊂, ∪, ∩, ∅ | ~10 |
| Calculus (giải tích) | Thay đổi + Tích lũy | d/dx, ∫, lim | ~5 ký hiệu core |
| **TỔNG** | | | **~150 ký hiệu thường dùng** |

```
So sánh:
  Vietnamese vocabulary:  ~5,000-10,000 từ thường dùng (người trưởng thành)
  English vocabulary:     ~5,000-10,000 từ thường dùng
  Math "vocabulary":      ~150 ký hiệu thường dùng

  → Math vocabulary NHỎ HƠN RẤT NHIỀU
  → Nhưng mỗi ký hiệu CHÍNH XÁC HƠN RẤT NHIỀU
  → Trade-off: BREADTH (nhỏ) vs PRECISION (cực cao)
```

---

## §2 — "Ngữ pháp" toán: Cú pháp biểu thức

### §2.1 — Biểu thức (Expression) = "Câu" toán

```
BIỂU THỨC = tổ hợp numbers + variables + operators theo quy tắc
  → Tương đương "câu" trong natural language

Ví dụ biểu thức:
  3 + 2                           = biểu thức đơn giản
  x² + 2x + 1                    = biểu thức đại số
  sin(θ) × cos(θ)                = biểu thức lượng giác
  Σᵢ₌₁ⁿ (2i + 1)                = biểu thức tổng
  ∫₀^π sin(x) dx                 = biểu thức tích phân

CÂU TRÚC CÂY (giống natural language):
  Biểu thức: (3 + 2) × (x - 1)

      [×]
     /   \
   [+]   [-]
   / \   / \
  3   2 x   1

  → Cây biểu thức = giống cây cú pháp trong natural language
  → Node gốc = phép toán cuối cùng thực hiện
  → Lá = numbers / variables
```

### §2.2 — Thứ tự phép toán = "Ngữ pháp" toán

```
BODMAS / PEMDAS = "quy tắc ngữ pháp" toán cơ bản:

  B/P — Brackets / Parentheses  ( )     ← ưu tiên CAO NHẤT
  O/E — Orders / Exponents      ^, √
  DM  — Division, Multiplication ÷, ×   ← trái → phải
  AS  — Addition, Subtraction    +, -   ← trái → phải, ưu tiên THẤP NHẤT

VÍ DỤ "SAI VÌ KHÔNG HIỂU NGỮ PHÁP":
  2 + 3 × 4 = ?

  ❌ Sai: (2 + 3) × 4 = 20     (tính trái→phải, bỏ qua ưu tiên)
  ✅ Đúng: 2 + (3 × 4) = 14    (× trước +)

  → Giống "Ăn bạn ơi" vs "Ăn, bạn ơi" trong tiếng Việt:
    Bỏ qua quy tắc = hiểu SAI hoàn toàn

SO SÁNH CHI TIẾT:
  Natural language: word order + grammar rules → xác định nghĩa
  Math:             operator precedence + brackets → xác định kết quả

  Natural language: quy tắc CÓ NGOẠI LỆ (irregular verbs, idioms,...)
  Math:             quy tắc KHÔNG CÓ NGOẠI LỆ (luôn nhất quán, 0 exceptions)
  → Đây là lý do toán CHÍNH XÁC: 0 mơ hồ, 0 ngoại lệ
```

### §2.3 — Infix, Prefix, Postfix — 3 cách viết cùng 1 ý

```
Toán có thể viết cùng 1 phép tính theo 3 CÁCH KHÁC NHAU:

INFIX (giữa) — cách THƯỜNG DÙNG:
  3 + 2        (operator Ở GIỮA 2 operands)
  x × y
  a - b

PREFIX (trước) — còn gọi Polish notation:
  + 3 2        (operator TRƯỚC operands)
  × x y
  - a b
  → Ưu điểm: KHÔNG CẦN NGOẶC!
  → + × 3 2 5 = + (× 3 2) 5 = + 6 5 = 11
  → Dùng trong: Lisp programming language

POSTFIX (sau) — còn gọi Reverse Polish:
  3 2 +        (operator SAU operands)
  x y ×
  a b -
  → Ưu điểm: KHÔNG CẦN NGOẶC! + dễ cho stack machine
  → 3 2 × 5 + = (3 × 2) + 5 = 6 + 5 = 11
  → Dùng trong: HP calculator, Forth programming, stack-based VM

VÍ DỤ PHỨC TẠP HƠN: (3 + 2) × (7 - 4)

  Infix:    (3 + 2) × (7 - 4)        = cần NGOẶC
  Prefix:   × + 3 2 - 7 4            = KHÔNG cần ngoặc!
  Postfix:  3 2 + 7 4 - ×            = KHÔNG cần ngoặc!

⭐ GAME DEV BIẾT:
  Shader language, stack VM: thường dùng postfix ngầm
  Expression parser: convert infix → postfix (Shunting Yard algorithm)
  Abstract Syntax Tree: biểu diễn expression dạng cây (cả 3 notation tương đương)

SO SÁNH VỚI NATURAL LANGUAGE:
  Natural language cũng có "word order" khác nhau:
    SVO (Việt/Anh/Trung): "Tôi ăn cơm"     = Subject Verb Object = kiểu INFIX
    SOV (Nhật/Hàn):        "Tôi cơm ăn"     = Subject Object Verb = kiểu POSTFIX!
    VSO (Ả Rập):           "Ăn tôi cơm"     = Verb Subject Object = kiểu PREFIX!

  → CÙNG CẤU TRÚC, khác thứ tự!
```

### §2.4 — Nesting — Lồng nhau (Recursion)

```
TOÁN CHO PHÉP LỒNG VÔ HẠN (recursion):

  f(g(h(x)))           = hàm lồng hàm lồng hàm
  ((a + b) × (c - d))  = ngoặc lồng ngoặc
  Σᵢ₌₁ⁿ (Σⱼ₌₁ᵐ aᵢⱼ)  = tổng lồng tổng (matrix!)

  → GIỐNG natural language: câu lồng câu
  Natural: "Tôi nghĩ [rằng bạn biết [rằng cô ấy nói [rằng...]]]"
  Math:    f(g(h(x))) = f chứa g chứa h chứa x

⭐ RECURSION DEPTH:
  Natural language: con người struggle sau ~3-4 lớp lồng nhau
    "Cái nhà MÀ [cô gái MÀ [anh chàng MÀ [tôi quen] yêu] xây] đẹp"
    → 3 lớp mệnh đề quan hệ = RẤT KHÓ hiểu khi nghe

  Toán: cũng struggle với nesting sâu, NHƯNG:
    → Dùng BIẾN TRUNG GIAN để flatten:
    Thay vì: f(g(h(x)))
    Viết:    a = h(x), b = g(a), c = f(b)
    → GIỐNG refactoring trong code!

  Code: recursion depth = stack depth
    → Quá sâu → stack overflow
    → Flatten bằng intermediate variables = CÙNG kỹ thuật như toán
```

### §2.5 — Phương trình (Equation) = "Câu khẳng định"

```
PHƯƠNG TRÌNH = biểu thức = biểu thức
  → Khẳng định: "vế trái BẰNG vế phải"

  x + 3 = 7           → "x cộng 3 BẰNG 7" → giải: x = 4
  x² - 4 = 0          → "x² trừ 4 BẰNG 0" → giải: x = ±2
  y = 2x + 1          → "y BẰNG 2x cộng 1" → mô tả đường thẳng

"GIẢI PHƯƠNG TRÌNH" = TÌM GIÁ TRỊ biến làm câu khẳng định ĐÚNG:
  x + 3 = 7
  x = 7 - 3           (chuyển vế, đổi dấu)
  x = 4               (câu trả lời)
  Kiểm tra: 4 + 3 = 7 ✅

SO SÁNH:
  Natural:  "Ai ĐÓ ăn cơm" → tìm: AI? → "Tôi ăn cơm"
  Toán:     "x + 3 = 7"     → tìm: x?  → "x = 4"
  → CẢ 2 = tìm THÔNG TIN THIẾU để câu HOÀN CHỈNH
```

### §2.6 — Bất phương trình = "Câu so sánh"

```
BẤT PHƯƠNG TRÌNH = biểu thức quan hệ biểu thức (dùng <, >, ≤, ≥)
  → Khẳng định MỐI QUAN HỆ thay vì SỰ BẰNG NHAU

  x + 3 > 7           → "x cộng 3 LỚN HƠN 7"
  x > 4               → mọi x lớn hơn 4 đều thỏa mãn
  → Kết quả = TẬP HỢP (nhiều đáp án), không phải 1 số

  0 ≤ x ≤ 1           → "x nằm giữa 0 và 1" (bao gồm 0 và 1)
  → Mô tả KHOẢNG (range) — game dev quen: clamp(x, 0, 1)
```

### §2.7 — Hệ phương trình = "Đoạn văn"

```
HỆ PHƯƠNG TRÌNH = nhiều phương trình cùng lúc, cùng biến
  → Tương đương "đoạn văn" (nhiều câu liên kết)

  ┌ x + y = 10         câu 1: x cộng y bằng 10
  └ x - y = 4          câu 2: x trừ y bằng 4

  Giải: từ 2 câu → tìm x VÀ y:
    Cộng 2 vế: 2x = 14 → x = 7
    Thay vào: 7 + y = 10 → y = 3
    → x = 7, y = 3

  → Giống natural language:
    "Tôi và bạn có tổng cộng 10 quả táo.
     Tôi nhiều hơn bạn 4 quả.
     Hỏi: mỗi người có mấy quả?"
    → CÙNG BÀI TOÁN, chỉ khác encoding (verbal vs math notation)
```

---

## §3 — Hierarchy: Từ → Biểu thức → Phương trình → Chứng minh → Lý thuyết

```
LEVEL 1 — KÝ HIỆU (Symbol) = "Từ"
  3, x, +, =, sin, π
  → Atom nhỏ nhất, có nghĩa riêng

LEVEL 2 — BIỂU THỨC (Expression) = "Cụm từ"
  3x + 2, sin(θ), x² - 4
  → Kết hợp ký hiệu theo quy tắc

LEVEL 3 — PHƯƠNG TRÌNH / MỆNH ĐỀ (Equation / Statement) = "Câu"
  x² - 4 = 0
  ∀x ∈ ℝ: x² ≥ 0
  → Khẳng định điều gì đó (đúng hoặc sai)

LEVEL 4 — CHỨNG MINH (Proof) = "Đoạn văn / Luận điểm"
  "Cho x² = 4.
   Vì x² = 4, nên x = √4 = ±2.
   Kiểm tra: 2² = 4 ✅, (-2)² = 4 ✅.
   Vậy x = 2 hoặc x = -2. QED."
  → Chuỗi mệnh đề liên kết logic → dẫn đến kết luận

LEVEL 5 — ĐỊNH LÝ (Theorem) = "Luận văn"
  Pythagorean Theorem: a² + b² = c² (cho tam giác vuông)
  → Mệnh đề ĐÃ ĐƯỢC CHỨNG MINH, dùng lại được mãi mãi
  → Tương đương "knowledge chunk" đã compile — retrieve instant

LEVEL 6 — LÝ THUYẾT (Theory) = "Cuốn sách / Hệ thống"
  Euclidean Geometry, Calculus, Linear Algebra, Group Theory,...
  → Hệ thống NHIỀU định lý liên kết
  → Tương đương "schema" / "domain knowledge" trong framework

MAPPING VÀO FRAMEWORK:
  Level 1 Ký hiệu      ↔ Chunk (atom)
  Level 2 Biểu thức     ↔ Chunk compound (small molecule)
  Level 3 Phương trình   ↔ Chunk chain (statement)
  Level 4 Chứng minh     ↔ Schema (organized argument with purpose)
  Level 5 Định lý        ↔ Compiled meta-chunk (retrieve instant)
  Level 6 Lý thuyết      ↔ Domain knowledge (full schema system)

⭐ EXPERT MATHEMATICIAN:
  → Nhìn "x² + 2x + 1" → INSTANT nhận ra = (x+1)²
  → Level 2 expression ĐÃ COMPILE thành Level 5 pattern (meta-chunk)
  → Giống expert chess player nhìn bàn cờ → nhận ra pattern instant
  → "Tính toán nhanh" = PATTERN MATCH compiled, không phải tính step-by-step
```

---

## §4 — Các "domain" toán và ký hiệu riêng

Mỗi nhánh toán = 1 "phương ngữ" (dialect) với ký hiệu + quy ước riêng:

### §4.1 — Số học (Arithmetic) — nền tảng nhất

```
Ký hiệu: +, -, ×, ÷, =, <, >, ()
Đối tượng: Số cụ thể (1, 2, 3, 0.5, -7,...)
Ví dụ: 3 + 2 = 5, 12 ÷ 4 = 3, 7 × 8 = 56

Tương đương: "ngôn ngữ hàng ngày" — ai cũng dùng
Học từ: ~5-6 tuổi
Ứng dụng: tính tiền, đo lường, đếm
```

### §4.2 — Đại số (Algebra) — thêm BIẾN

```
Ký hiệu MỚI: x, y, z (biến), aₙ (dãy), Σ (tổng), Π (tích)
Đối tượng: Biểu thức chứa biến, phương trình, hệ phương trình
Ví dụ:
  ax² + bx + c = 0 (phương trình bậc 2)
  → Nghiệm: x = (-b ± √(b²-4ac)) / 2a (công thức nghiệm — 1 compiled meta-chunk!)

Tương đương: "ngôn ngữ trừu tượng hóa" — nói về PATTERN thay vì số cụ thể
Học từ: ~11-12 tuổi
Ứng dụng: mọi nơi — physics, engineering, economics, game programming

⭐ Bước nhảy từ Arithmetic → Algebra:
  Arithmetic: "3 + 2 = 5" (CỤ THỂ)
  Algebra:    "a + b = b + a" (TỔNG QUÁT — đúng cho MỌI số)
  → Đây là lần đầu toán nói về PATTERN thay vì instance
  → Giống: "con chó cụ thể" → "MỌI con chó" (∀ dog)
```

### §4.3 — Hình học (Geometry) — thêm HÌNH + KHÔNG GIAN

```
Ký hiệu MỚI: ∠ (góc), ⊥ (vuông góc), ∥ (song song), △ (tam giác),
             π (chu vi/bán kính), r (bán kính), A (diện tích), V (thể tích)

Công thức quan trọng:
  Chu vi tròn:    C = 2πr
  Diện tích tròn: A = πr²
  Pythagorean:    a² + b² = c² (tam giác vuông)
  Diện tích tam giác: A = ½ × base × height

Tương đương: "ngôn ngữ không gian" — mô tả hình dạng + vị trí
Học từ: ~9-10 tuổi (cơ bản), ~14-15 (chứng minh)

⭐ ĐẶC BIỆT: Geometry = VISUAL + SYMBOLIC kết hợp
  → Phải nhìn HÌNH + đọc KÝ HIỆU đồng thời
  → 2 encoding cùng lúc: L2 visual + L2 math notation
  → Đây là lý do geometry "khác" algebra: cần spatial reasoning
  → Game dev quen: collision detection, ray casting, mesh geometry
```

### §4.4 — Giải tích (Calculus) — thêm VÔ CỰC + LIÊN TỤC

```
Ký hiệu MỚI: lim, dx, dy, d/dx, ∫, ∂ (đạo hàm riêng), ∞

Công thức quan trọng:
  Đạo hàm: d/dx [xⁿ] = n·xⁿ⁻¹
  Tích phân: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C
  Chain rule: d/dx [f(g(x))] = f'(g(x)) · g'(x)

Tương đương: "ngôn ngữ sự thay đổi" — mô tả biến đổi liên tục
Học từ: ~17-18 tuổi (đại học)

⭐ Calculus = BƯỚC NHẢY LỚN NHẤT trong toán:
  Trước calculus: toán nói về SỐ CỤ THỂ + PATTERN CỐ ĐỊNH
  Calculus: toán nói về SỰ THAY ĐỔI + TÍCH LŨY + VÔ CỰC
  → Mở ra: physics (Newton), engineering, economics, ML
  → Game dev dùng: physics integration, smooth animation, bezier curves
```

### §4.5 — Xác suất & Thống kê — thêm BẤT ĐỊNH

```
Ký hiệu MỚI: P(A) (xác suất), E[X] (kỳ vọng), σ (độ lệch chuẩn),
             μ (trung bình), Var(X) (phương sai), n! (giai thừa),
             (n choose k) = C(n,k) (tổ hợp)

Công thức quan trọng:
  P(A) = số kết quả thuận lợi / tổng số kết quả
  P(A∩B) = P(A) × P(B)    (nếu A, B độc lập)
  E[X] = Σ xᵢ × P(xᵢ)    (kỳ vọng = trung bình có trọng số)

Tương đương: "ngôn ngữ bất định" — nói về CÁI CHƯA CHẮC CHẮN
Học từ: ~15-16 tuổi (cơ bản), ~18+ (nâng cao)

⭐ Game dev dùng: random loot, damage variance, matchmaking, gacha probability
  Ví dụ: P(legendary drop) = 0.01 = 1%
  → Sau 100 lần mở: kỳ vọng E = 100 × 0.01 = 1 legendary
  → Nhưng KHÔNG chắc — có thể 0, có thể 3 (variance!)
```

### §4.6 — Logic — thêm CHỨNG MINH + SUY LUẬN

```
Ký hiệu MỚI: ∧ (và), ∨ (hoặc), ¬ (không), → (suy ra), ↔ (tương đương),
             ∀ (cho mọi), ∃ (tồn tại), ⊢ (chứng minh được), ⊨ (thỏa mãn)

Tương đương: "ngôn ngữ suy luận chặt chẽ" — nói về ĐÚNG/SAI
Học từ: ~18+ (discrete math, philosophy)

⭐ Logic = NỀN TẢNG cho:
  → Chứng minh toán: mọi chứng minh = chuỗi logic
  → Programming: if/else, boolean, conditional = logic
  → AI: logical reasoning, constraint satisfaction
  → Database: SQL WHERE clause = logic predicate
```

### §4.7 — Đại số tuyến tính (Linear Algebra) — thêm VECTOR + MATRIX

```
Ký hiệu MỚI: v⃗ (vector), A (matrix), det(A) (determinant),
             A⁻¹ (inverse), Aᵀ (transpose), λ (eigenvalue)

Ví dụ matrix:
  A = [1  2]    vector: v⃗ = [3]
      [3  4]              [5]

  A × v⃗ = [1×3 + 2×5] = [13]
           [3×3 + 4×5]   [29]

Tương đương: "ngôn ngữ biến đổi không gian" — xoay, co, dãn, chiếu
Học từ: ~18+ (đại học)

⭐ GAME DEV DÙNG RẤT NHIỀU:
  → Transform matrix: position, rotation, scale
  → Camera matrix: world → view → projection
  → Shader: mọi vertex transform = matrix multiplication
  → Physics: inertia tensor = matrix
  → ML/AI: neural network = layers of matrix multiplication

  Ví dụ game dev:
  Xoay điểm (x,y) 1 góc θ:
  [x'] = [cos(θ)  -sin(θ)] [x]
  [y']   [sin(θ)   cos(θ)] [y]

  → 1 matrix multiplication = 1 phép xoay
  → Ghép nhiều matrix = ghép nhiều phép biến đổi
  → Đây là lý do GPU sinh ra: hardware cho matrix multiplication nhanh
```

---

## §5 — So sánh: Toán vs Natural Language

| Đặc điểm | Natural Language (Việt/Anh/Trung) | Mathematical Language |
|---|---|---|
| **"Từ vựng"** | ~5,000-10,000 từ thường dùng | ~150 ký hiệu thường dùng |
| **Mơ hồ** | ⭐ CÓ (đa nghĩa, context-dependent) | ❌ KHÔNG (1 ký hiệu = 1 nghĩa chính xác) |
| **Ngoại lệ** | ⭐ NHIỀU (irregular verbs, idioms,...) | ❌ KHÔNG CÓ (0 ngoại lệ) |
| **Recursion** | 3-4 lớp max (con người struggle) | Vô hạn (lý thuyết), flatten bằng biến trung gian |
| **Precision** | Thấp-Trung (mô tả gần đúng) | ⭐ CỰC CAO (chính xác tuyệt đối) |
| **Breadth** | ⭐ CỰC RỘNG (mô tả mọi thứ) | HẸP (chỉ quantity + relation + structure) |
| **Shareability** | Cần cùng ngôn ngữ | ⭐ GLOBAL (ký hiệu toán giống nhau toàn cầu) |
| **Learning curve** | ~3-5 năm thành thạo L1 | ~12-15 năm (arithmetic → calculus) |
| **Cultural variation** | ⭐ RẤT LỚN (Việt ≠ Anh ≠ Trung) | GẦN NHƯ KHÔNG (~quy ước nhỏ khác) |
| **Emotional content** | ⭐ PHONG PHÚ (yêu, ghét, buồn,...) | ❌ KHÔNG CÓ |
| **Social content** | ⭐ PHONG PHÚ (kính, thân, xa,...) | ❌ KHÔNG CÓ |
| **Chủ đề** | Mọi thứ | Quantity, structure, space, change |
| **Evolution speed** | Nhanh (từ mới mỗi năm) | Chậm (ký hiệu mới mỗi thập kỷ/thế kỷ) |
| **"Native speaker"** | Mọi trẻ em | KHÔNG CÓ — phải học formal |

```
TÓM LẠI:

Natural language:  RỘNG + LINH HOẠT + MƠ HỒ + CÓ CẢM XÚC
                   → Tối ưu cho GIAO TIẾP XÃ HỘI + MỌI CHỦ ĐỀ

Math language:     HẸP + CỨNG NHẮC + CHÍNH XÁC + KHÔNG CẢM XÚC
                   → Tối ưu cho QUANTITY + STRUCTURE + CHỨNG MINH

→ Không cái nào "tốt hơn" — mỗi cái tối ưu cho MỤC ĐÍCH KHÁC
→ Bác sĩ dùng CẢ HAI: natural language (nói với bệnh nhân) + math (tính liều thuốc)
→ Game dev dùng CẢ HAI: natural language (design document) + math (physics, shaders)
```

---

## §6 — Toán trong thực tế: Cách expert THỰC SỰ dùng toán

### §6.1 — Beginner vs Expert giải cùng 1 bài

```
BÀI TOÁN: Giải phương trình x² - 5x + 6 = 0

BEGINNER (step by step, heavy L3 processing):
  Bước 1: Nhớ công thức nghiệm: x = (-b ± √(b²-4ac)) / 2a     ← retrieve chunk
  Bước 2: Xác định a=1, b=-5, c=6                                ← pattern match
  Bước 3: Tính b² = (-5)² = 25                                   ← calculate
  Bước 4: Tính 4ac = 4×1×6 = 24                                  ← calculate
  Bước 5: Tính Δ = 25 - 24 = 1                                   ← calculate
  Bước 6: Tính √Δ = √1 = 1                                       ← calculate
  Bước 7: x₁ = (5+1)/2 = 3, x₂ = (5-1)/2 = 2                   ← calculate
  Bước 8: Kiểm tra: 9-15+6=0 ✅, 4-10+6=0 ✅                    ← verify

  → 8 bước, mỗi bước = 1 chunk retrieve + apply
  → Heavy L3 processing, PFC work hard
  → Giống beginner pha cà phê: từng bước rõ ràng

EXPERT (pattern match, light L3):
  Nhìn: x² - 5x + 6 = 0
  → INSTANT: "tích 6, tổng 5 → (x-2)(x-3) = 0 → x=2 hoặc x=3"
  → 1 bước duy nhất: pattern match → retrieve compiled solution
  → L1 → L4 (skip L2+L3 gần như hoàn toàn)
  → Giống expert pha cà phê: tay tự làm

  Expert compiled meta-chunk: "ax²+bx+c với Δ nhỏ → thử factoring trước"
  → Đây là "kinh nghiệm" = compiled pattern từ hàng trăm bài tương tự
```

### §6.2 — "Tính toán" vs "Nhớ pattern" — cả 2 cùng lúc

```
NHÀ KHOA HỌC THỰC SỰ LÀM GÌ khi "tính toán":

PHASE 1 — NHẬN DẠNG (Pattern Match):
  Nhìn bài toán → nhận ra LOẠI bài → retrieve relevant schema
  "À, đây là bài optimization" / "Đây là differential equation"
  → L1 Pattern Match: compiled chunks fire

PHASE 2 — LÊN PLAN (Imagine-Final):
  "Cần: tìm minimum → đạo hàm = 0 → giải → kiểm tra"
  → L4 Plan: Imagine-Final hình thành (biết đáp án trông thế nào)
  → Imagine-Final = "tìm được giá trị x mà f(x) nhỏ nhất"

PHASE 3 — CHAIN STEPS (Build Arc):
  Bước 1: tính f'(x)      → retrieve rule đạo hàm + apply
  Bước 2: giải f'(x) = 0  → retrieve algebra technique + apply
  Bước 3: kiểm tra f''(x) → retrieve rule đạo hàm bậc 2 + check sign
  → L3 Sequential Chain: mỗi bước = retrieve chunk + apply

PHASE 4 — KIỂM TRA (Evaluate):
  Thay ngược lại → body feedback "đúng rồi" / "sai rồi, quay lại"
  → L0 → L1 feedback loop

→ "Tính toán" = MIX của:
  • PATTERN MATCH (nhận dạng loại bài — compiled, instant)
  • RETRIEVAL (nhớ công thức, quy tắc — compiled chunks)
  • CHAIN (nối các bước logic — L3 processing)
  • CALCULATE (tính số cụ thể — L3 nhưng thường compiled cho số nhỏ)

→ Nhà khoa học "giỏi toán" = người có:
  • NHIỀU compiled patterns (nhận dạng nhanh)
  • NHIỀU compiled rules (retrieve instant)
  • THÀNH THẠO chain (nối bước mượt)
  → KHÔNG phải "tính nhanh hơn" — mà "NHẬN RA nhanh hơn" + "NỐI mượt hơn"
```

### §6.3 — Bản nháp vs Trình bày: 2 mode khác nhau

```
BẢN NHÁP (scratch work) — cách nhà khoa học THỰC SỰ giải:
  → Viết lung tung, thử hướng này hướng kia
  → Gạch bỏ, viết lại, vẽ hình bên cạnh
  → Dùng "..." thay bước hiển nhiên
  → MIX: math notation + natural language + hình vẽ + mũi tên
  → = L3 PROCESSING đang diễn ra, messy, exploratory

TRÌNH BÀY (formal presentation) — sau khi đã giải xong:
  → Viết lại gọn gàng, từng bước rõ ràng
  → "Cho... Ta có... Suy ra... Vậy..."
  → KHÔNG có hướng sai, KHÔNG có gạch bỏ
  → = COMPILED RESULT, clean, communicative

→ Giống: bản nháp email vs email gửi đi
→ Giống: prototype code vs production code
→ Process (messy) ≠ Product (clean)

⭐ INSIGHT: Khi đọc sách toán, bạn thấy PRODUCT (trình bày đẹp)
  → Tưởng nhà toán học nghĩ cũng "thẳng tắp" như vậy
  → KHÔNG! Họ cũng mò mẫm, thử sai, messy — chỉ TRÌNH BÀY đẹp sau
  → Bản nháp Euler, Gauss, Ramanujan: đầy gạch xóa, thử sai, vẽ hình lung tung
```

---

## §7 — Lịch sử phát triển ký hiệu toán

```
TIMELINE — ký hiệu toán KHÔNG luôn tồn tại. Phải PHÁT MINH qua hàng nghìn năm:

~3000 TCN  Babylon: Hệ số đếm cơ số 60 (vì sao giờ có 60 phút, vòng tròn 360°)
~1500 TCN  Ai Cập: Phân số, hình học cơ bản (xây kim tự tháp cần đo đạc)
~500 TCN   Hy Lạp: Hình học chứng minh (Euclid), số vô tỉ (Pythagoras shock)
~600 CN    Ấn Độ: SỐ 0 phát minh (Brahmagupta) → thay đổi MỌI THỨ
                   Số âm, hệ thập phân
~800 CN    Ả Rập: Al-Khwarizmi → "Algebra" (al-jabr = "phục hồi")
                   → Từ "algorithm" cũng từ tên Al-Khwarizmi!
~1200      Fibonacci: Đưa số Hindu-Arabic (0-9) vào châu Âu (thay Roman numerals)
~1489      + và - : Lần đầu xuất hiện ký hiệu (Johannes Widmann, Đức)
~1557      = : Robert Recorde phát minh dấu bằng (Anh)
                "Không gì bằng nhau hơn 2 đường thẳng song song" — lý do ông chọn ==
~1591      Viète: Dùng CHỮ CÁI cho biến (a, b, c cho known; x, y, z cho unknown)
                → TRƯỚC ĐÓ: mọi phương trình viết bằng LỜI (natural language!)
                   "Bình phương của ẩn số cộng với năm lần ẩn số bằng sáu"
                → SAU ĐÓ: x² + 5x = 6
                → ⭐ BƯỚC NHẢY LỚN: từ verbal → symbolic
~1614      Logarithm: John Napier phát minh (Scotland)
~1637      Descartes: Hệ tọa độ x,y (Cartesian coordinates) → HÌnh học + Đại số HỢP NHẤT
~1655      ∞ : John Wallis phát minh ký hiệu vô cùng
~1687      Newton + Leibniz: Calculus (đạo hàm, tích phân)
                Leibniz: ký hiệu dx, dy, ∫ (integral = chữ S dài, "Summa")
                Newton: ký hiệu ẋ (dot notation — vẫn dùng trong vật lý)
~1734      Euler: e, i, f(x), Σ, π (nhiều ký hiệu quen thuộc nhất = Euler đặt!)
~1821      Cauchy: ε-δ definition (giới hạn chặt chẽ)
~1847      Boole: Đại số Boolean (AND, OR, NOT) → NỀN TẢNG cho computer!
~1874      Cantor: Set theory {}, ∈, ⊂ → NỀN TẢNG cho modern math
~1889      Peano: ∀, ∃ (lượng từ logic)
~1931      Gödel: Incompleteness theorems → "có mệnh đề ĐÚNG nhưng KHÔNG chứng minh được"
~1936      Turing: Turing machine → NỀN TẢNG cho computer science

⭐ INSIGHT TỪ LỊCH SỬ:
  1. Ký hiệu "+" chỉ mới ~500 năm. Trước đó viết "cộng" bằng LỜI.
  2. Dấu "=" chỉ mới ~470 năm. Trước đó viết "bằng" bằng LỜI.
  3. Dùng x, y cho biến chỉ mới ~430 năm. Trước đó viết "ẩn số" bằng LỜI.
  4. TOÀN BỘ toán trước ~1500 được viết bằng NATURAL LANGUAGE!
     → Math notation = PHÁT MINH để nén + chính xác hóa natural language
     → Giống: programming language = phát minh để nén + chính xác hóa natural language cho máy
  5. Mỗi ký hiệu mới = 1 chunk mới → cho phép COMPRESS + CHAIN phức tạp hơn
     → "+" compress "phép cộng" thành 1 ký tự
     → "∫" compress "tổng vô hạn các diện tích nhỏ" thành 1 ký tự
     → MỖI KÝ HIỆU MỚI = 1 LEVEL ABSTRACTION MỚI
```

---

## §8 — Framework lens + Câu hỏi mở

### §8.1 — Toán trong Processing Layers model

```
Toán sử dụng Processing Layers thế nào:

L0 (Body Input):    Đọc ký hiệu trên giấy/màn hình (visual)
L1 (Pattern Match): Nhận ra loại bài, pattern quen (compiled chunks)
L2 (Encoding):      Math notation format (x, +, =, ∫, Σ,...)
L3 (Processing):    Chain logic steps, calculate, prove
L4 (Plan/Execute):  Organize solution strategy, write result

Beginner math:  Heavy L2 (vẫn đang học ký hiệu) + Heavy L3 (từng bước)
Expert math:    Light L2 (notation tự động) + Light L3 (pattern match skip)
                → L0 → L1 → L4 (giống routine, chỉ với bài quen!)

⭐ Math expertise = COMPILE L2+L3 thành L1 meta-chunks:
  "x² - 5x + 6 = (x-2)(x-3)" đã compile → nhìn là BIẾT, không cần tính
  Giống: "3 × 7 = 21" đã compile từ lúc 8 tuổi → nhìn là BIẾT
```

### §8.2 — Toán vs Natural Language: Complementary formats

```
CÙNG 1 Ý, 2 ENCODING:

Math:     F = ma
Natural:  "Lực bằng khối lượng nhân gia tốc"

Math:     E = mc²
Natural:  "Năng lượng bằng khối lượng nhân bình phương vận tốc ánh sáng"

Math:     ∫₀^∞ e^(-x²) dx = √π/2
Natural:  "Tích phân từ 0 đến vô cùng của e mũ trừ x bình phương
           bằng căn pi chia 2"
           → 14 từ natural language = 1 dòng math notation
           → Math COMPRESSION: 14 words → 1 line

→ Đây là lý do math notation TỒN TẠI:
  COMPRESSION CỰC CAO cho quantity + relation
  Nhưng CHỈ cho quantity + relation — không compress được cảm xúc, xã hội, narrative
```

### §8.3 — Câu hỏi mở

1. **Tại sao trẻ em MỌI NƠI đều học arithmetic sớm (~5-6 tuổi)?** Có phải number sense là "pre-verbal substrate" giống chunks pre-verbal trong F1? (Research: Dehaene 1997 "Number Sense" — có vùng não riêng cho số: Intraparietal sulcus.)

2. **Algebra = lần đầu ABSTRACT OVER INSTANCES** (từ "3+2" sang "a+b"). Đây có phải PFC-dependent transition? (Prediction: algebra difficulty correlates với PFC maturation timeline.)

3. **Tại sao proof/chứng minh KHÓ HƠN RẤT NHIỀU so với calculate?** Vì proof = GENERATIVE (phải TẠO argument mới), calculate = SEQUENTIAL (chain steps đã biết). Proof ≈ L3 Generative pattern, calculate ≈ L3 Sequential pattern.

4. **Math anxiety = speech-act compile level?** (Per NT7 discussion earlier) Math anxiety ≠ "số 3 bị tag threat" → "số 3 dùng ở mọi context, recyclable". Math anxiety = "act of doing math in social context" bị tag threat (giống speech-act level). Prediction: math anxiety chỉ xuất hiện khi TÁC ĐỘNG XÃ HỘI (kiểm tra, bị gọi lên bảng), không khi giải toán 1 mình.

5. **Ký hiệu mới = chunk compression mới** (§7 lịch sử). H12 language evolution driver áp dụng cho math notation? "Nhà toán học cảm thấy cần ký hiệu mới → coin ký hiệu → community adopt." Giống H12 word coining mechanism?

6. **Chinese math advantage?** Chinese number words ngắn hơn English (一二三四五六七八九十 = monosyllabic). Working memory for Chinese speakers giữ được NHIỀU SỐ hơn per slot. Evidence: Chinese children calculate faster (Miller & Stigler 1987). → Handle size matters!

### §8.4 — References

| Tác giả | Năm | Công trình | Liên quan |
|---|---|---|---|
| Dehaene, S. | 1997 | The Number Sense | Number cognition neuroscience |
| Lakoff & Núñez | 2000 | Where Mathematics Comes From | Math as embodied cognition |
| Goldberg, A. | 1995 | Construction Grammar | Constructions = compiled templates |
| Miller & Stigler | 1987 | Chinese number word advantage | Cross-language math performance |
| Cajori, F. | 1928 | A History of Mathematical Notations | History of math symbols |
| Boyer, C. | 1991 | A History of Mathematics | Overview of math development |
| Euler, L. | 1748 | Introductio in analysin infinitorum | Origin of modern notation |
| Skemp, R. | 1976 | Relational vs Instrumental Understanding | Math learning theory |

---

> **02-Mathematical-Language-Architecture.md — End of file.**
>
> Tài liệu tham khảo cho exploration session N+5. Đọc nghiền ngẫm, đặc biệt §5 (so sánh) và §6 (expert thực sự dùng toán thế nào).
>
> Phiên bản: v1.0, 2026-04-16.
