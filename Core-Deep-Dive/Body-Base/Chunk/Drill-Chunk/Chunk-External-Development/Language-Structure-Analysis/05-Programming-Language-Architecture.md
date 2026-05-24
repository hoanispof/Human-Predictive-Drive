---
title: Programming Language Architecture — Cấu trúc ngôn ngữ lập trình
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — tài liệu tham khảo, đọc nghiền ngẫm
scope: Programming languages như communication format — bạn BIẾT code, file này "mổ xẻ" CẤU TRÚC HỆ THỐNG
purpose: Nhìn programming language từ góc ĐỘ LANGUAGE ARCHITECTURE — so sánh với natural language, math, music, visual
parent: ../../plan.md (F3 Chunk-External-Development)
language: Tiếng Việt primary + English technical + code examples
note: Viết cho người ĐÃ BIẾT code (game dev) — KHÔNG dạy syntax, focus vào KIẾN TRÚC
---

# Programming Language Architecture — Cấu trúc ngôn ngữ lập trình

> **Mục đích**: Bạn code hàng ngày. File này KHÔNG dạy code — mà "mổ xẻ" programming language như 1 HỆ THỐNG NGÔN NGỮ. Khi bạn viết `if (x > 0) return x;` — bạn đang dùng 1 communication format có cấu trúc riêng. File này phân tích CẤU TRÚC ĐÓ và so sánh với natural language, math, music, visual.
>
> **Unique property**: Programming language = **EXECUTABLE communication format** — format DUY NHẤT mà machine có thể THỰC THI, không chỉ "hiểu".

---

## MỤC LỤC

- §1 — "Từ vựng" code: Các thành phần cơ bản
- §2 — "Ngữ pháp" code: Syntax rules
- §3 — Paradigms: Nhiều "phương ngữ" tư duy
- §4 — Type systems: Phân loại data
- §5 — Hierarchy: Token → Expression → Statement → Function → Module → System
- §6 — So sánh: Code vs Natural Language vs Math vs Music vs Visual
- §7 — Điểm ĐỘC ĐÁO: Executable + Precise + Composable
- §8 — Lịch sử phát triển
- §9 — Framework lens + Câu hỏi mở

---

## §1 — "Từ vựng" code: Các thành phần cơ bản

### §1.1 — Keywords = "Từ chức năng" (function words)

```
Mỗi language có bộ KEYWORDS cố định — không thể dùng làm tên biến:

C#/Java:        if, else, for, while, return, class, new, void, int, string,
                public, private, static, try, catch, switch, case, break,...

Python:         if, else, for, while, return, def, class, import, from,
                try, except, with, as, yield, lambda, pass, None,...

JavaScript:     if, else, for, while, return, function, const, let, var,
                class, new, this, async, await, typeof, instanceof,...

Rust:           if, else, for, while, return, fn, struct, impl, enum,
                match, let, mut, pub, use, mod, trait, async, await,...

SỐ LƯỢNG KEYWORDS:
  C:          32 keywords
  Python:     35 keywords
  Java:       50 keywords
  C#:         79 keywords
  C++:        95 keywords
  Rust:       39 keywords

SO SÁNH:
  Vietnamese: ~5,000-10,000 từ thường dùng
  Math:       ~150 ký hiệu
  Music:      12 nốt + ~30 ký hiệu
  Code:       30-100 keywords + UNLIMITED user-defined names
              → Keywords ÍT nhưng user names KHÔNG GIỚI HẠN

⭐ CODE = KEYWORDS (cố định, ít) + USER NAMES (tự đặt, vô hạn)
  → Giống: grammar (cố định) + vocabulary (mở rộng)
  → Keywords = closed class (giới từ, liên từ)
  → User names = open class (danh từ, động từ)
```

### §1.2 — Identifiers = "Danh từ + Động từ" (user-defined names)

```
IDENTIFIERS = tên do programmer đặt

  Variables (biến):     playerHealth, enemyCount, isAlive, deltaTime
  Functions (hàm):      CalculateDamage(), SpawnEnemy(), SaveGame()
  Classes (lớp):        Player, Enemy, GameManager, UIController
  Constants:            MAX_HEALTH, GRAVITY, PI

NAMING CONVENTIONS (quy ước đặt tên) = "register" trong natural language:

  camelCase:       playerHealth        → C#, Java, JavaScript (variables)
  PascalCase:      PlayerController    → C#, Java (classes, methods)
  snake_case:      player_health       → Python, Rust, C (variables)
  SCREAMING_SNAKE: MAX_HEALTH          → hầu hết languages (constants)
  kebab-case:      player-health       → CSS, HTML attributes, Lisp

→ Naming convention = SOCIAL CONTRACT giữa programmers
→ Giống: "anh/em" trong Vietnamese = social convention
→ Phá convention → code chạy ĐÚNG nhưng đọc KHÓ CHỊU (sao sao ấy!)

⭐ GOOD NAMING = cực kỳ quan trọng:
  ❌ int a = b * c;                        (a, b, c = ?)
  ✅ int damage = baseDamage * multiplier;  (rõ ràng!)

  → Code CHẠY giống nhau. Nhưng COMMUNICATION khác hoàn toàn.
  → "Code is read more than written" = code là COMMUNICATION FORMAT
  → Good naming = good verbal labels (retrieval path + compression)
```

### §1.3 — Operators = "Động từ" (actions on data)

```
ARITHMETIC (giống math):
  +  -  *  /  %  **         cộng, trừ, nhân, chia, modulo, power

COMPARISON (giống math relations):
  ==  !=  <  >  <=  >=      bằng, không bằng, nhỏ hơn, lớn hơn,...

LOGICAL (giống math logic):
  &&  ||  !                  AND, OR, NOT
  (Python: and, or, not)

ASSIGNMENT (KHÔNG CÓ trong math!):
  =   +=  -=  *=  /=        gán, cộng-gán, trừ-gán,...

  ⭐ DẤU "=" TRONG CODE vs MATH:
  Math:  x = 5         → "x BẰNG 5" (sự thật, không thay đổi)
  Code:  x = 5         → "GÁN 5 vào x" (hành động, thay đổi state)
  Code:  x = x + 1     → "lấy x cũ, cộng 1, gán lại vào x" 
                          → Math: x = x + 1 → VÔ NGHĨA (không x nào bằng x+1)
  → Đây là KHÁC BIỆT CĂN BẢN giữa math (declarative) và code (imperative)

BITWISE (chỉ code có):
  &  |  ^  ~  <<  >>        AND, OR, XOR, NOT, left-shift, right-shift
  → Thao tác trực tiếp trên BITS (0 và 1)
  → Game dev dùng: bitmask flags, hash functions, color manipulation

MEMBER ACCESS:
  .   (dot)                  player.health, gameObject.transform.position
  ->  (arrow, C/C++)         ptr->value
  ::  (scope, C++/Rust)      std::cout, Vec::new()
  
  → Đây là thứ CHỈ CODE CÓ: truy cập vào CẤU TRÚC DỮ LIỆU lồng nhau
  → "player.inventory.items[0].name" = 4 lớp sâu, 1 dòng code
```

### §1.4 — Literals = "Danh từ cụ thể" (concrete values)

```
NUMBER LITERALS:
  42          integer
  3.14        float/double
  0xFF        hexadecimal (255) — game dev: color codes
  0b1010      binary (10)
  1_000_000   with separator (1 triệu, dễ đọc)

STRING LITERALS:
  "Hello World"          regular string
  'a'                    single character
  `Hello ${name}`        template literal (JS) — mix text + code
  @"C:\path\file"        verbatim string (C#) — no escape
  """multi-line
  string"""              multi-line (Python)

BOOLEAN LITERALS:
  true / false           (hoặc True/False trong Python)

SPECIAL LITERALS:
  null / None / nil      "không có gì" (khác 0, khác "", khác false!)
  undefined              "chưa gán" (JavaScript)
  []                     empty array/list
  {}                     empty object/dict

→ Code có NHIỀU LOẠI "nothing" hơn natural language:
  Vietnamese: "không có gì" = 1 concept
  Code: null ≠ undefined ≠ 0 ≠ "" ≠ false ≠ [] ≠ {}
  → Mỗi "nothing" KHÁC NHAU! → nguồn bug kinh điển
```

---

## §2 — "Ngữ pháp" code: Syntax rules

### §2.1 — Control flow = "Cấu trúc câu"

```
CONDITIONAL (rẽ nhánh):
  if (condition) {          Nếu (điều kiện) {
    doA();                    làm A;
  } else {                  } không thì {
    doB();                    làm B;
  }                         }

  switch (value) {          Chuyển (giá trị) {
    case 1: doA(); break;     trường hợp 1: làm A; dừng;
    case 2: doB(); break;     trường hợp 2: làm B; dừng;
    default: doC();           mặc định: làm C;
  }                         }

  → Giống natural language: "Nếu... thì... không thì..."
  → NHƯNG: code CHÍNH XÁC — condition = true/false, KHÔNG mơ hồ

LOOP (lặp):
  for (int i = 0; i < 10; i++) {    Với i từ 0 đến 9 {
    doSomething(i);                   làm gì đó(i);
  }                                 }

  while (isAlive) {                 Trong khi (còn sống) {
    update();                         cập nhật;
  }                                 }

  foreach (var item in list) {      Với mỗi item trong list {
    process(item);                    xử lý(item);
  }                                 }

  → Natural language: "lặp lại 10 lần" = mơ hồ (chính xác 10? khoảng 10?)
  → Code: "for i = 0; i < 10" = CHÍNH XÁC 10 lần, i = 0,1,2,...,9

EXCEPTION HANDLING (xử lý lỗi):
  try {                             Thử {
    riskyOperation();                 thao tác rủi ro;
  } catch (Exception e) {          } bắt lỗi (Exception e) {
    handleError(e);                   xử lý lỗi(e);
  } finally {                      } cuối cùng {
    cleanup();                        dọn dẹp;
  }                                 }

  → Natural language KHÔNG CÓ equivalent trực tiếp
  → "Thử cái này, nếu lỗi thì làm cái kia" = gần nhưng KHÔNG chính xác bằng
```

### §2.2 — Scope & Blocks = "Paragraphs" and "chapters"

```
BLOCK (khối) = { } — group statements

  → { } trong code = paragraph trong text
  → Mọi thứ TRONG { } = thuộc về nhau (scope)
  → Biến khai báo trong { } chỉ sống trong { } đó

SCOPE (phạm vi):
  {                         // outer scope
    int x = 10;             // x sống ở đây
    {                       // inner scope
      int y = 20;           // y sống ở đây
      x + y = 30;           // CẢ x VÀ y đều accessible
    }
    // y ĐÃ CHẾT. x vẫn sống.
    // x + y → ERROR! y không tồn tại nữa
  }

  → Scope = "context" — giống: ý nghĩa từ thay đổi theo context
    Natural: "bank" = bờ sông HAY ngân hàng? → context quyết định
    Code: biến "x" = CÁI NÀO? → scope quyết định (inner wins)
  → Code scope = CHÍNH XÁC (rules rõ ràng)
  → Natural context = MƠ HỒ (phải đoán)
```

### §2.3 — Syntax strictness = "0 tolerance for grammar errors"

```
NATURAL LANGUAGE — TOLERANT:
  "Toi an com" (thiếu dấu) → vẫn hiểu
  "I eated rice" (sai grammar) → vẫn hiểu
  "Rice I eat" (đảo trật tự) → vẫn hiểu
  → Human brain REPAIR errors automatically

CODE — ZERO TOLERANCE:
  pritn("hello")        → ERROR (typo: pritn thay vì print)
  if (x > 0             → ERROR (thiếu dấu ")")
  int x = "hello"       → ERROR (type mismatch)
  x = x +               → ERROR (thiếu operand)

  → 1 ký tự sai = KHÔNG CHẠY ĐƯỢC
  → Compiler/interpreter = parser CỰC STRICT
  → Đây là lý do code KHÓ hơn natural language:
    Natural language: 80% đúng = hiểu được
    Code: 99.99% đúng + 0.01% sai = KHÔNG chạy

⭐ NHƯNG: Modern tools giúp:
  → IDE: autocomplete, syntax highlight, error underline
  → Compiler: error messages chỉ chỗ sai
  → AI: suggest fix
  → Đây là "prosthetic L2" — tool hỗ trợ encoding layer
```

---

## §3 — Paradigms: Nhiều "phương ngữ" tư duy

Programming languages không chỉ khác syntax — chúng khác CÁCH NGHĨ (paradigm):

### §3.1 — Imperative (Mệnh lệnh) = "Làm cái này, rồi cái kia"

```
// C-style: TỪ TỪNG BƯỚC, NHƯ RECIPE
int sum = 0;
for (int i = 0; i < 10; i++) {
    sum += i;
}
// → "Bắt đầu từ 0. Lặp 10 lần. Mỗi lần cộng i vào sum."
// → Giống: recipe nấu ăn — step by step

→ GIỐNG natural language: "Đầu tiên... rồi... sau đó... cuối cùng..."
→ Dễ hiểu vì match cách con người NGHĨ về hành động tuần tự
→ Languages: C, Java, C#, Python, JavaScript (đa số)
```

### §3.2 — Declarative (Khai báo) = "Tôi muốn CÁI NÀY, bạn lo cách làm"

```
// SQL: NÓI CẦN GÌ, KHÔNG NÓI LÀM THẾ NÀO
SELECT name FROM users WHERE age > 18 ORDER BY name;
// → "Lấy tên từ bảng users, điều kiện tuổi > 18, sắp theo tên"
// → KHÔNG nói: loop thế nào, compare thế nào, sort thế nào

// HTML/CSS: MÔ TẢ, KHÔNG COMMAND
<h1 style="color: red">Hello</h1>
// → "Heading 1, màu đỏ, nội dung Hello"
// → KHÔNG nói: vẽ pixel thế nào, font render thế nào

→ GIỐNG math: "x² + 2x + 1 = 0" (mô tả relationship, không nói cách giải)
→ Languages: SQL, HTML, CSS, Regex, Prolog
→ Game dev dùng: SQL cho database, CSS cho UI, shader language (partially)
```

### §3.3 — Functional (Hàm) = "Mọi thứ là function, no side effects"

```
// Haskell / functional style:
sum = foldl (+) 0 [0..9]
// → "sum = fold left (+) starting-from-0 over list [0..9]"
// → Mô tả TRANSFORMATION, không mô tả STEPS

// JavaScript functional:
const sum = [0,1,2,3,4,5,6,7,8,9].reduce((a, b) => a + b, 0);
// → "sum = reduce list bằng cách cộng từng cặp, bắt đầu từ 0"

KEY PROPERTIES:
  - Immutability: data KHÔNG THAY ĐỔI (tạo mới thay vì sửa)
  - Pure functions: cùng input → luôn cùng output (no side effects)
  - First-class functions: function = data (truyền qua, return, gán biến)

→ GIỐNG math HƠN: f(x) = x² → cùng x luôn ra cùng kết quả
→ Languages: Haskell, Erlang, Clojure, F#, (partly: JS, Python, Rust)
→ Game dev gặp: React (UI), Redux (state), shader math
```

### §3.4 — Object-Oriented (Hướng đối tượng) = "Mọi thứ là object có state + behavior"

```
// C# / Unity style:
class Enemy {
    public int health = 100;
    public float speed = 5f;
    
    public void TakeDamage(int amount) {
        health -= amount;
        if (health <= 0) Die();
    }
    
    public void Die() {
        // ...
    }
}

// Sử dụng:
Enemy goblin = new Enemy();
goblin.TakeDamage(30);  // goblin.health = 70

KEY PROPERTIES:
  - Encapsulation: data + behavior GÓI CHUNG (class)
  - Inheritance: class con KẾ THỪA class cha
  - Polymorphism: cùng method name, KHÁC behavior per class
  - Abstraction: ẩn chi tiết, lộ interface

→ GIỐNG natural language metaphor: "con goblin BỊ ĐÁNH, MẤT 30 máu, NẾU hết máu THÌ CHẾT"
→ OOP map TRỰC TIẾP vào cách con người nghĩ về "things with properties and actions"
→ Languages: Java, C#, C++, Python, JavaScript
→ Game dev: Unity (C#), Unreal (C++), Godot (GDScript) = OOP heavy
```

### §3.5 — So sánh paradigms

```
CÙNG 1 BÀI TOÁN: "Tính tổng 0+1+2+...+9"

Imperative:
  int sum = 0;
  for (int i = 0; i < 10; i++) sum += i;
  → "Bắt đầu 0, lặp 10 lần, cộng dần"

Declarative (SQL-like):
  SELECT SUM(value) FROM generate_series(0, 9);
  → "Lấy tổng của dãy 0 đến 9"

Functional:
  foldl (+) 0 [0..9]
  → "Fold list [0..9] bằng phép cộng, bắt đầu 0"

Mathematical:
  Σᵢ₌₀⁹ i = 45
  → "Tổng i từ 0 đến 9"

Natural language:
  "Cộng tất cả số từ 0 đến 9 lại"

→ 5 CÁCH KHÁC NHAU diễn đạt CÙNG 1 ý
→ Mỗi cách = 1 PARADIGM (cách nghĩ)
→ Imperative = recipe. Declarative = wish. Functional = transform. Math = define. NL = describe.
```

---

## §4 — Type systems: Phân loại data

```
TYPE SYSTEM = cách code PHÂN LOẠI dữ liệu — giống CLASSIFIER trong Vietnamese!

PRIMITIVE TYPES (nguyên thủy):
  int         = số nguyên (42, -7, 0)
  float/double = số thực (3.14, -0.5)
  bool        = true/false
  char        = 1 ký tự ('a', '中', '😀')
  string      = chuỗi ký tự ("Hello World")

COMPOSITE TYPES (phức hợp):
  Array/List  = danh sách [1, 2, 3, 4, 5]
  Dictionary  = từ điển {"name": "player", "hp": 100}
  Tuple       = bộ (x, y, z) = (1.0, 2.5, 3.0)
  Set         = tập hợp {1, 2, 3} (no duplicates)

USER-DEFINED TYPES:
  class Enemy { int hp; float speed; }
  struct Vector3 { float x, y, z; }
  enum State { Idle, Walking, Attacking, Dead }

⭐ SO SÁNH VỚI VIETNAMESE CLASSIFIER:
  Vietnamese: "CON chó" → classifier "con" buộc phân loại ANIMATE
  Code:       "Enemy goblin" → type "Enemy" buộc phân loại CÓ hp, speed
  
  Vietnamese: "CÁI bàn" → classifier "cái" buộc phân loại INANIMATE
  Code:       "int count" → type "int" buộc phân loại SỐ NGUYÊN

  Vietnamese classifier: ~30 loại (con, cái, chiếc, tờ, quyển,...)
  Code type system: ~10 primitive + UNLIMITED user-defined
  → Code type system = CLASSIFIER SYSTEM on steroids

STATIC vs DYNAMIC typing:
  Static (C#, Java, Rust): PHẢI khai báo type TRƯỚC, compiler CHECK
    int x = 5;          // x là int, MÃIMÃI là int
    x = "hello";        // ❌ ERROR! int ≠ string

  Dynamic (Python, JS): type TỰ ĐỘNG, thay đổi được
    x = 5               # x là int BÂY GIỜ
    x = "hello"         # x giờ là string — OK!

  → Static = strict grammar (Latin, German case system)
  → Dynamic = flexible grammar (Vietnamese, Chinese — no type marking)
```

---

## §5 — Hierarchy: Token → Expression → Statement → Function → Module → System

```
LEVEL 1 — TOKEN = "Từ"
  42, x, +, if, "hello", ==
  → Atom nhỏ nhất mà lexer nhận biết

LEVEL 2 — EXPRESSION = "Cụm từ"  
  x + 3, player.health > 0, Math.Max(a, b)
  → Kết hợp tokens → tạo ra VALUE

LEVEL 3 — STATEMENT = "Câu"
  int x = 42;
  if (hp <= 0) Die();
  for (int i = 0; i < n; i++) Process(i);
  → Thực hiện ACTION (gán, rẽ nhánh, lặp)

LEVEL 4 — FUNCTION / METHOD = "Đoạn văn"
  void TakeDamage(int amount) {
      health -= amount;
      if (health <= 0) Die();
      PlayHitEffect();
  }
  → Nhóm statements có PURPOSE cụ thể

LEVEL 5 — CLASS / MODULE = "Chương"
  class Enemy {
      // properties + methods
      // = encapsulated unit of behavior
  }
  → Nhóm functions + data thành 1 unit có ý nghĩa

LEVEL 6 — PACKAGE / NAMESPACE = "Phần"
  namespace Game.Entities { ... }
  → Nhóm classes thành domain

LEVEL 7 — PROJECT / CODEBASE = "Cuốn sách"
  Solution / Repository
  → Toàn bộ hệ thống

LEVEL 8 — ECOSYSTEM = "Thư viện"
  npm, NuGet, pip, cargo — package managers
  → Cộng đồng code chia sẻ

MAPPING VÀO FRAMEWORK:
  Level 1 Token       ↔ Chunk (atom)
  Level 2 Expression  ↔ Chunk compound
  Level 3 Statement   ↔ Chunk chain
  Level 4 Function    ↔ Schema (organized, has purpose)
  Level 5 Class       ↔ Domain schema (encapsulated behavior)
  Level 6 Package     ↔ Domain knowledge
  Level 7 Codebase    ↔ Full domain system
  Level 8 Ecosystem   ↔ Community-shared knowledge (external-shared!)

⭐ CODE có NHIỀU levels hơn mọi format khác:
  Natural language: ~5 levels (word → phrase → sentence → paragraph → text)
  Math: ~6 levels (symbol → expression → equation → proof → theorem → theory)
  Music: ~6 levels (note → motif → phrase → section → form → opus)
  Code: 8 levels → PHỨC TẠP NHẤT trong tất cả communication formats
```

---

## §6 — So sánh: Code vs tất cả formats khác

| Đặc điểm | Natural Lang | Math | Music | Visual | ⭐ Code |
|---|---|---|---|---|---|
| **Encode chính** | Meaning | Quantity | Emotion×Time | Space | ⭐ BEHAVIOR (hành vi) |
| **Executable** | ❌ | ❌ | ❌ (cần performer) | ❌ | ⭐ YES (machine runs it) |
| **Precision** | Thấp | Cực cao | Cao (pitch) | Trung | ⭐ Cực cao (deterministic) |
| **Ambiguity** | Cao | Không | Trung | Trung | ⭐ KHÔNG (0 ambiguity) |
| **Error tolerance** | Cao | Thấp | Trung | Trung | ⭐ ZERO (1 lỗi = crash) |
| **Hierarchy depth** | ~5 levels | ~6 levels | ~6 levels | ~5 levels | ⭐ 8 levels |
| **Composability** | Thấp | Cao | Trung | Thấp | ⭐ CỰC CAO (function of function of...) |
| **State** | Narrative | Immutable | Temporal | Static | ⭐ MUTABLE STATE (thay đổi theo thời gian) |
| **Feedback loop** | ❌ | ❌ | ❌ | ❌ | ⭐ YES (code chạy → xem kết quả → sửa) |
| **Shareability** | Cần cùng ngôn ngữ | Global | Global | Global | Global (nhưng cần cùng language) |
| **Age** | ~100,000 năm | ~5,000 năm | ~40,000 năm | ~40,000 năm | ⭐ ~80 năm (1940s) |
| **"Native speaker"** | Mọi trẻ em | Không | Partial | Partial | ⭐ Không (phải học formal) |
| **Learning curve** | ~3-5 năm L1 | ~12-15 năm | ~5-10 năm | ~ngay (basic) | ~2-5 năm (productive) |

---

## §7 — Điểm ĐỘC ĐÁO: Executable + Precise + Composable

### §7.1 — EXECUTABLE: Format duy nhất machine CHẠY được

```
Natural language: "Sắp xếp danh sách theo thứ tự tăng dần"
  → Con người HIỂU → CON NGƯỜI thực hiện

Math: "sort(A) = permutation σ of A such that σ(i) ≤ σ(i+1) ∀i"
  → Con người HIỂU → CON NGƯỜI thực hiện (hoặc CHỨNG MINH)

Code: list.sort()
  → Machine HIỂU → MACHINE thực hiện
  → Chạy trên HÀNG TỈ thiết bị, CÙNG kết quả, KHÔNG mệt mỏi

⭐ Đây là SUPERPOWER của code: viết 1 lần → chạy HÀNG TỈ lần
  → Không format nào khác có property này
  → Natural language → ai viết thì chỉ người đọc hiểu
  → Code → ai viết thì HÀNG TỈ MACHINE hiểu VÀ THỰC HIỆN
```

### §7.2 — COMPOSABILITY: Function of function of function...

```
Code có khả năng COMPOSE (lồng nhau) cực mạnh:

  // Level 1: function đơn lẻ
  float Distance(Vector3 a, Vector3 b) { ... }
  
  // Level 2: compose functions
  Enemy FindNearest(Vector3 position, List<Enemy> enemies) {
    return enemies
      .Where(e => e.IsAlive())                    // filter
      .OrderBy(e => Distance(position, e.Position)) // sort by distance
      .FirstOrDefault();                            // take nearest
  }
  
  // Level 3: compose higher
  void AttackNearest() {
    var target = FindNearest(transform.position, allEnemies);
    if (target != null) Attack(target);
  }
  
  // Level 4: compose into system
  void Update() {
    if (Input.GetKeyDown("space")) AttackNearest();
  }

→ Mỗi level COMPOSE level dưới → ABSTRACTION TOWER
→ Giống: word → phrase → sentence → paragraph
→ NHƯNG code có thể compose SÂU HƠN RẤT NHIỀU (8 levels vs 5)
→ Đây là cách 1 game = HÀNG TRIỆU dòng code hoạt động:
  mỗi level chỉ cần hiểu level ngay dưới nó
```

### §7.3 — MUTABLE STATE: Thứ mà math KHÔNG CÓ

```
Math: x = 5 → x LUÔN là 5 (immutable, eternal truth)
Code: x = 5 → x LÀ 5 BÂY GIỜ. Có thể đổi thành 10 SAU ĐÓ.

  int health = 100;        // health = 100 LÚC NÀY
  health -= 30;            // health = 70 SAU CÂU NÀY
  health -= 50;            // health = 20 SAU CÂU NÀY
  
  → State THAY ĐỔI theo thời gian = core property của code
  → Math KHÔNG CÓ concept này (equations are timeless)
  → Music CÓ thời gian nhưng KHÔNG CÓ mutable state
  → Code = UNIQUE: state × time × logic

⭐ GAME = STATE MACHINE:
  → Mọi game = giant mutable state (positions, health, inventory, score,...)
  → Mỗi frame: đọc input → update state → render
  → Code = NGÔN NGỮ DUY NHẤT mô tả được cái này chính xác
```

---

## §8 — Lịch sử phát triển

```
1843      Ada Lovelace: first algorithm (for Babbage's Analytical Engine)
            → Considered first programmer — TRƯỚC khi computer tồn tại!
1936      Alan Turing: Turing machine — theoretical foundation
1940s     Machine code: viết bằng SỐ (0s and 1s) trực tiếp
            → 10110000 01100001 = "move value to register"
            → KHÔNG AI muốn viết thế này
1950s     Assembly: mnemonic cho machine code
            → MOV AL, 61h = dễ đọc hơn binary
            → Vẫn rất low-level: 1 instruction = 1 machine operation
1957      FORTRAN (FORmula TRANslation): first high-level language
            → Viết công thức GIỐNG MATH: X = A + B * C
            → ⭐ BƯỚC NHẢY: từ "nói chuyện với machine" → "nói chuyện với math"
1958      LISP (LISt Processing): functional + AI language
            → (+ 3 (* 2 4)) = prefix notation = Polish notation
            → Parentheses everywhere → "Lost In Stupid Parentheses" joke
1959      COBOL: business language ("readable English")
            → MULTIPLY HOURS BY RATE GIVING GROSS-PAY
            → Đọc GIỐNG natural language — nhưng verbose
1964      BASIC: "beginner" language → democratize programming
1972      C: low-level power + high-level syntax → STILL ALIVE (Linux, embedded)
1983      C++: C + OOP → game development dominant (Unreal Engine)
1991      Python: "readable code" philosophy → AI/ML dominant
1995      Java: "write once run anywhere" → enterprise, Android
1995      JavaScript: web browser language → NOW everywhere
2000      C#: Microsoft's Java-killer → Unity game engine dominant
2010      Rust: memory safety without garbage collector → systems programming
2012      TypeScript: JavaScript + types → modern web dev
2020s     AI-assisted coding: GitHub Copilot, Claude, ChatGPT
            → ⭐ BƯỚC NHẢY: từ "human writes code" → "human describes, AI writes code"
            → Natural language → code translation (!!!)

⭐ PATTERN TỪ LỊCH SỬ:
  Machine code (1940s):  nói chuyện với MACHINE (binary)
  Assembly (1950s):      nói chuyện với MACHINE (readable)
  FORTRAN (1957):        nói chuyện với MATH (formula)
  COBOL (1959):          nói chuyện với ENGLISH (business)
  C (1972):              nói chuyện với HARDWARE (systems)
  OOP (1983):            nói chuyện với OBJECTS (metaphor thế giới thực)
  Python (1991):         nói chuyện với LOGIC (clean, readable)
  AI coding (2020s):     nói chuyện với NATURAL LANGUAGE → AI generates code

  → TREND: programming language ngày càng GẦN natural language hơn
  → Ultimate end: "nói cái bạn muốn" → machine tự code
  → Đây có phải "H12 for code"? Human cảm thấy gap → coin new language → community adopt
```

---

## §9 — Framework lens + Câu hỏi mở

### §9.1 — Code trong Processing Layers model

```
L0 (Body Input):    Đọc code trên screen (visual)
L1 (Pattern Match): Nhận ra patterns (design pattern, idiom, bug pattern)
L2 (Encoding):      Code format (syntax, types, paradigm)
L3 (Processing):    Design algorithm, debug, refactor, architect
L4 (Plan/Execute):  Write code, run, test, deploy

BEGINNER PROGRAMMER:
  Heavy L2 (still learning syntax) + Heavy L3 (plan each line)
  → Mỗi line code = conscious effort

EXPERT PROGRAMMER:
  Light L2 (syntax automatic) + L1 dominant (pattern match: "à, dùng observer pattern")
  → Nhìn bài toán → INSTANT nhận ra pattern → implement từ compiled meta-chunk
  → "Senior dev viết code ít hơn junior nhưng CODE TỐT HƠN"
    = senior đã compile meta-chunks → cần ít L3 processing

⭐ CODE REVIEW = L1 Pattern Match applied:
  Senior nhìn code → "sao sao ấy" → pattern mismatch signal
  → Giống: native speaker đọc "tôi xe đi" → "sao sao"
  → Cùng cơ chế: compiled template mismatch → body signal
```

### §9.2 — Code as EXTERNAL KNOWLEDGE system

```
⭐ KEY INSIGHT: Codebase = EXTERNAL KNOWLEDGE that is EXECUTABLE

  Natural language book: knowledge ĐỌC ĐƯỢC nhưng KHÔNG TỰ CHẠY
  Math textbook: knowledge ĐỌC ĐƯỢC nhưng KHÔNG TỰ CHẠY  
  Music score: knowledge ĐỌC ĐƯỢC nhưng CẦN PERFORMER
  Codebase: knowledge ĐỌC ĐƯỢC VÀ TỰ CHẠY

  → Codebase = "cuốn sách biết tự đọc chính mình"
  → Khi bạn deploy 1 app → bạn SHARE executable knowledge tới triệu users
  → Users KHÔNG CẦN hiểu code → nhưng NHẬN ĐƯỢC kết quả

  → Đây là communication format MẠNH NHẤT về impact:
    1 codebase → HÀNG TỈ executions → HÀNG TỈ users affected
    1 cuốn sách → HÀNG TRIỆU readers → mỗi người phải TỰ apply
```

### §9.3 — Câu hỏi mở

1. **Code = natural language evolution?** Trend: code ngày càng gần NL (COBOL → Python → AI coding). Tương lai: NL → code là seamless? Hoặc code vẫn cần riêng vì PRECISION requirement?

2. **Why do programmers THINK in code?** Senior devs report "thinking in code" — mental model IS the code structure. Vì compiled meta-chunks sâu đến mức L2 encoding = default thinking mode? Giống: bilingual người sometimes think in L2.

3. **Code quality = "good writing"?** "Clean code" (Martin 2008) = "code dễ đọc, dễ hiểu, dễ maintain." Giống: "good writing" = "text dễ đọc, rõ ý, mạch lạc." CÙNG principles: clarity, concision, structure, naming. → Cả 2 = communication craft.

4. **Open source = cultural-shared knowledge?** GitHub = thư viện toàn cầu of executable knowledge. Giống: library of books nhưng books TỰ CHẠY. → Open source = H7 (cultural transmission as chunks propagation) applied to code.

5. **Game dev = multi-format expert?** Game dev dùng: Code (logic) + Math (physics) + Visual (art, UI) + Music (audio) + Natural language (design docs, dialogue). → Game dev = rare profession requiring ALL 5 communication formats simultaneously.

### §9.4 — References

| Tác giả | Năm | Công trình | Liên quan |
|---|---|---|---|
| Turing, A. | 1936 | On Computable Numbers | Theoretical foundation |
| Knuth, D. | 1968-2011 | The Art of Computer Programming | CS fundamentals |
| Martin, R. (Uncle Bob) | 2008 | Clean Code | Code as communication |
| Gamma et al. | 1994 | Design Patterns (GoF) | Compiled solution patterns |
| Brooks, F. | 1975 | The Mythical Man-Month | Software engineering truths |
| Abelson & Sussman | 1985 | Structure and Interpretation of Computer Programs | Language architecture |
| Van Roy & Haridi | 2004 | Concepts, Techniques, and Models of Computer Programming | Paradigms |

---

> **05-Programming-Language-Architecture.md — End of file.**
>
> Code = communication format ĐỘC ĐÁO: EXECUTABLE + precise + composable + mutable state. Duy nhất trong tất cả formats mà machine có thể THỰC THI. 8 hierarchy levels — phức tạp nhất trong tất cả formats.
>
> Phiên bản: v1.0, 2026-04-16.
