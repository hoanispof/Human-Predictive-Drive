---
title: Mathematical Language Architecture
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — reference document, read for deep understanding
scope: Mathematics as a "language" system — notation, syntax, structure, compared to natural language
purpose: Understand math not as "solving problems" but as seeing its architecture as a communication format
parent: ../../plan.md (F3 Chunk-External-Development)
language: English primary + mathematical notation
note: Written for people who USE math daily but have never "dissected" its structure
---

# Mathematical Language Architecture

> **Purpose**: You use math every day (calculating prices, measuring, game physics code...) but have never viewed math as a LANGUAGE SYSTEM. This file "dissects" math's structure — not to solve problems, but to see math as a communication format with its own "vocabulary", "grammar", "sentences", and "paragraphs".
>
> **Comparison with file 01**: File 01 analyzed natural language (Vietnamese/English/Chinese). This file analyzes mathematical language. Both are Communication Modality formats — but the architectures are VERY DIFFERENT.
>
> **How to read**: Read each section, reflect. No need to know advanced math — this file focuses on STRUCTURE, not on SOLVING SKILLS.

---

## TABLE OF CONTENTS

- §1 — Math "Vocabulary": Types of Symbols
  - §1.1 Numbers — Number System
  - §1.2 Variables
  - §1.3 Operators
  - §1.4 Relations
  - §1.5 Grouping — Brackets
  - §1.6 Functions
  - §1.7 Constants — Special Constants
  - §1.8 Logic Symbols
  - §1.9 Set Theory Symbols
  - §1.10 Calculus Symbols
  - §1.11 Summary Table: Math "Vocabulary"
- §2 — Math "Grammar": Expression Syntax
  - §2.1 Expression = Math's "Sentence"
  - §2.2 Operator Precedence = Math's "Grammar"
  - §2.3 Infix, Prefix, Postfix — 3 Ways to Write the Same Thing
  - §2.4 Nesting — Recursion
  - §2.5 Equation = "Declarative Sentence"
  - §2.6 Inequality = "Comparative Sentence"
  - §2.7 System of Equations = "Paragraph"
- §3 — Hierarchy: Symbol → Expression → Equation → Proof → Theory
- §4 — Math "Domains" and Their Notation
  - §4.1 Arithmetic
  - §4.2 Algebra
  - §4.3 Geometry
  - §4.4 Calculus
  - §4.5 Probability & Statistics
  - §4.6 Logic
  - §4.7 Linear Algebra
- §5 — Comparison: Math vs Natural Language
- §6 — Math in Practice: How Experts ACTUALLY Use Math
- §7 — History of Mathematical Notation
- §8 — Framework Lens + Open Questions

---

## §1 — Math "Vocabulary": Types of Symbols

Natural language has nouns, verbs, adjectives... Math has its own "word types" too:

### §1.1 — Numbers = Math's "Nouns"

Numbers = the most basic objects, equivalent to nouns in natural language.

```
NATURAL NUMBERS (ℕ):
  0, 1, 2, 3, 4, 5, ...
  → Counting objects: "there are 3 dogs" → 3 ∈ ℕ
  → Oldest: since humans began counting (~40,000 years ago?)

INTEGERS (ℤ):
  ..., -3, -2, -1, 0, 1, 2, 3, ...
  → Adds NEGATIVE numbers: "owe 5 million" → -5
  → ℤ from German "Zahlen" = "numbers"
  → Invented: ~600 CE (India, Brahmagupta)

RATIONAL NUMBERS (ℚ):
  1/2, 3/4, -2/3, 0.75, 1.333...
  → All numbers writable as p/q (fraction)
  → ℚ from "Quotient"
  → Developed: ~1500 BCE (Egypt, Rhind Papyrus)

IRRATIONAL NUMBERS:
  √2 = 1.41421356..., π = 3.14159265..., e = 2.71828182...
  → CANNOT be written as a fraction
  → Infinite decimal expansion, NON-REPEATING
  → Discovery of √2 (shock!): ~500 BCE (Greece, Pythagoras)
    → Legend: Hippasus proved √2 is irrational → thrown into the sea
       for shattering the belief that "all things are ratios of integers"

REAL NUMBERS (ℝ):
  All numbers on the number line: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
  → Includes both rational + irrational
  → Visualize: every POINT on a straight line = 1 real number

COMPLEX NUMBERS (ℂ):
  a + bi, where i = √(-1)
  → Example: 3 + 2i, -1 + 0.5i
  → i² = -1 (square root of -1 — "impossible" but incredibly useful!)
  → Used extensively in: electronics, quantum physics, games (quaternions for 3D rotation!)
  → Invented: ~1545 (Cardano, solving cubic equations)

VISUALIZING: Nested Number Layers
  ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ
  │    │    │    │    │
  │    │    │    │    └── Complex (adds imaginary dimension)
  │    │    │    └── Reals (fill the number line)
  │    │    └── Rationals (fractions)
  │    └── Integers (adds negatives)
  └── Naturals (counting)

  → Each layer = EXTENDS the previous to solve new problems:
    "3 - 5 = ?" → need ℤ (negatives)
    "1 ÷ 3 = ?" → need ℚ (fractions)
    "√2 = ?"    → need ℝ (irrationals)
    "√(-1) = ?" → need ℂ (complex)
```

### §1.2 — Variables = Math's "Pronouns"

```
VARIABLES = symbols standing for UNKNOWN or ARBITRARY numbers
  → Like pronouns in natural language: "it" substitutes for a specific noun

COMMON CONVENTIONS:
  x, y, z         = unknown variables — solve equations to find them
  a, b, c         = known coefficients / constants (parameters)
  n, m, k         = integers (often used for counting, index)
  i, j            = loop index — game devs know this well!
  t               = time
  f, g, h         = functions
  θ (theta)       = angle
  Δ (delta)       = change / difference ("delta x" = how much x changes)
  Σ (sigma)       = sum
  ε (epsilon)     = very small number (near 0)
  ∞ (infinity)    = infinity

EXAMPLES:
  "x + 3 = 7"    → x = pronoun, stands for number 4 (unknown, need to find)
  "for all n"    → n = pronoun, stands for "any integer"
  "f(x) = x²"   → x = any input, f = squaring function

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  "IT eats rice"       → "it" = represents someone/something (needs context)
  Math:     "x + 3 = 7"         → "x" = represents some number (needs solving)

  Natural:  "EVERYONE eats"     → "everyone" = all
  Math:     "∀x: x + 0 = x"    → "∀x" = "for all x" = all numbers
```

### §1.3 — Operators = Math's "Verbs"

```
OPERATORS = actions performed on numbers, equivalent to VERBS in natural language

ARITHMETIC (Basic):
  +    addition          3 + 2 = 5
  -    subtraction       7 - 4 = 3
  ×    multiplication    3 × 4 = 12    (also written: 3·4 or 3*4)
  ÷    division          12 ÷ 3 = 4    (also written: 12/3)
  ^    exponent          2³ = 8        (2 to the power 3 = 2×2×2)
  √    root/square root  √9 = 3        (square root of 9)
  !    factorial          5! = 120      (5×4×3×2×1)
  %    percent           50% = 0.5
  mod  modulo (remainder) 7 mod 3 = 1  (7 divided by 3, remainder 1 — game devs use this a lot!)

ALGEBRA:
  Σ    summation         Σᵢ₌₁ⁿ i = 1+2+3+...+n
  Π    product           Πᵢ₌₁ⁿ i = 1×2×3×...×n = n!
  |x|  absolute value    |-5| = 5, |3| = 3
  ⌊x⌋  floor (round down) ⌊3.7⌋ = 3
  ⌈x⌉  ceiling (round up) ⌈3.2⌉ = 4

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  "I EAT rice"              → EAT = verb (action)
  Math:     "3  +  2  = 5"           → + = "verb" (action of adding)

  Natural:  Many types of verbs (eat, run, think, love, fear...)
  Math:     FEWER "verbs" but each one is EXTREMELY PRECISE
            (+ always means addition, never anything else)
```

### §1.4 — Relations = Math's "Comparison Conjunctions"

```
RELATIONS = symbols expressing the RELATIONSHIP between 2 expressions

  =     equal                      3 + 2 = 5
  ≠     not equal                  3 ≠ 4
  <     less than                  2 < 5
  >     greater than               7 > 3
  ≤     less than or equal to      x ≤ 10
  ≥     greater than or equal to   y ≥ 0
  ≈     approximately              π ≈ 3.14
  ∝     proportional to            F ∝ ma (force proportional to mass × acceleration)
  ≡     identical / congruent      a ≡ b (mod n)
  ~     approximately equivalent   f(x) ~ g(x)

⭐ THE "=" SIGN IN MATH vs IN CODE:
  Math:  x = 5      → "x EQUALS 5" (statement of fact)
  Code:  x = 5      → "ASSIGN 5 to x" (action that changes state)
  Code:  x == 5     → "DOES x EQUAL 5?" (check/comparison)

  → Game devs know "=" as assignment. Math uses "=" as assertion.
  → This is the classic source of confusion between math and programming.
```

### §1.5 — Grouping = Math's "Punctuation"

```
BRACKETS = control PROCESSING ORDER, equivalent to punctuation in natural language

  ( )    parentheses         (3 + 2) × 4 = 20
  [ ]    square brackets     [a + b] × c
  { }    curly braces        {1, 2, 3} = a set
  | |    absolute value / norm  |x| = absolute value

OPERATOR PRECEDENCE (when NO brackets):
  1. ( ) brackets                  ← HIGHEST priority
  2. ^ exponent
  3. × ÷ multiplication, division  ← left to right
  4. + - addition, subtraction     ← left to right, LOWEST priority

EXAMPLE — same operation, DIFFERENT BRACKETS = DIFFERENT RESULTS:
  3 + 2 × 4   = 3 + 8   = 11    (multiply first)
  (3 + 2) × 4 = 5 × 4   = 20    (brackets first, then multiply)

COMPARISON WITH NATURAL LANGUAGE:
  Natural: Commas, periods, brackets = control how sentences are UNDERSTOOD
           "Let's eat, friend!" vs "Let's eat friend!" ← comma changes meaning completely!
  Math:    Brackets = control how expressions are COMPUTED
           3+2×4 vs (3+2)×4 ← brackets change the result completely!

  → Both systems: punctuation/brackets = CONSTRAINT on how the parser processes
```

### §1.6 — Functions = "Processing Machines" — Input In, Output Out

```
FUNCTION = a "machine" that receives INPUT and gives OUTPUT according to a fixed rule

SYNTAX: f(x) = expression containing x
  → f = function name
  → x = input (argument)
  → expression = processing rule
  → f(x) = output

BASIC FUNCTIONS:

  Linear function:       f(x) = 2x + 3
    f(0) = 3, f(1) = 5, f(10) = 23
    → Input × 2, then add 3

  Quadratic function:    f(x) = x²
    f(0) = 0, f(2) = 4, f(-3) = 9
    → Input multiplied by itself (squared)

  Trigonometric functions:
    sin(θ)   = opposite / hypotenuse  (right triangle ratio — game devs use this A LOT!)
    cos(θ)   = adjacent / hypotenuse
    tan(θ)   = opposite / adjacent = sin(θ)/cos(θ)

    Game dev example:
      Character turns 45° and moves 10 units:
      dx = 10 × cos(45°) ≈ 7.07    (displacement along x)
      dy = 10 × sin(45°) ≈ 7.07    (displacement along y)
      → sin/cos = "translate angle into x,y coordinates"

  Logarithm:
    log₁₀(100) = 2    because 10² = 100    ("10 to what power = 100?" → 2)
    log₂(8)    = 3    because 2³ = 8       ("2 to what power = 8?" → 3)
    ln(e)      = 1    because e¹ = e       (ln = natural log, base e)

    → log = INVERSE of exponentiation
    → Game dev use: log₂(n) = complexity of binary search algorithm

  Exponential function:
    eˣ      (e ≈ 2.71828, "Euler's number")
    2ˣ      (doubles each step)

    → Exponential growth: 2⁰=1, 2¹=2, 2²=4, 2³=8, 2¹⁰=1024, 2²⁰=1,048,576
    → Game dev: 2ⁿ = texture size, memory allocation

COMPARISON WITH NATURAL LANGUAGE:
  Natural: Sentence = Subject + Verb + Object
  Math:    Expression = Function(Argument) = Result
           f(x) = y means "function f PROCESSES input x, yields y"

  Natural language functions (metaphor):
    "translate(Vietnamese sentence)" = English sentence
    "cook(ingredients)" = dish
    → Any PROCESS with input + output = a function!
```

### §1.7 — Constants = Math's "Proper Nouns"

```
CONSTANTS = SPECIFIC numbers with proper names because they are too important / appear too frequently

  π (pi)     ≈ 3.14159265...    Ratio of circumference to diameter
                                 → Appears EVERYWHERE: circles, waves, oscillations, probability
                                 → Game dev: rotation, circular motion, wave patterns

  e (Euler)  ≈ 2.71828182...    Base of the natural logarithm
                                 → Continuous growth: compound interest, radioactive decay
                                 → eˣ = the ONLY function whose derivative = itself

  φ (phi)    ≈ 1.61803398...    Golden ratio
                                 → (1 + √5) / 2
                                 → Appears in: architecture, art, nature (shells, flowers)

  i          = √(-1)            Imaginary unit
                                 → i² = -1
                                 → Game dev: quaternion uses i, j, k for 3D rotation

  ∞          = infinity          Not a number, but a CONCEPT
                                 → "larger than every number"
                                 → Used in: limits, integrals, series

COMPARISON:
  Natural language "proper nouns": Hanoi, Einstein, Everest — names FOR SPECIFIC THINGS
  Math constants:                  π, e, φ — names FOR SPECIFIC NUMBERS that appear everywhere
```

### §1.8 — Logic Symbols = "Conjunctions" + "Negation" + "Quantifiers"

```
LOGIC = a system of PRECISE reasoning, foundation for all mathematical proof

LOGICAL CONNECTIVES:
  ∧   AND          p ∧ q = "p AND q are both true"
  ∨   OR           p ∨ q = "p OR q (or both) is true"
  ¬   NOT          ¬p = "p is NOT true"
  →   IMPLIES      p → q = "IF p THEN q"
  ↔   IFF          p ↔ q = "p is TRUE if and only if q is TRUE"

QUANTIFIERS:
  ∀   FOR ALL       ∀x: x + 0 = x    "for ALL x, x plus 0 equals x"
  ∃   EXISTS        ∃x: x² = 4       "there EXISTS x such that x² = 4" (x = 2 or -2)
  ∄   DOES NOT EXIST  ∄x: x² = -1 (∈ℝ) "NO real x exists such that x² = -1"

COMBINED EXAMPLE:
  ∀x ∈ ℝ: x² ≥ 0
  = "For ALL real x: x squared is GREATER THAN OR EQUAL TO 0"
  = "The square of any real number is non-negative"

  ∃x ∈ ℤ: (x > 0) ∧ (x < 1)
  = "There EXISTS an integer x such that: x > 0 AND x < 1"
  = "Is there any integer greater than 0 and less than 1?"
  → Answer: NO (∄) — no integer exists between 0 and 1

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  "if it rains THEN I stay home"   → AND, OR, IF...THEN, NOT
  Math:     "if p is true THEN q is true" = p → q    → ∧, ∨, →, ¬

  Natural:  "EVERYONE eats" / "SOMEONE eats"
  Math:     "∀x: f(x)" / "∃x: f(x)"

  → SAME type of concept (and, or, not, all, exists)
  → Math: PRECISE (unambiguous)
  → Natural: FLEXIBLE (can be ambiguous, polysemous)

  Ambiguity example in natural language:
    "I see someone" = ∃x: I see x (OK)
    "Everyone sees" = ∀x: x sees (?) or ∃x: everyone sees x (?)
    → Natural language IS AMBIGUOUS! Math IS NOT: must write ∀ or ∃ explicitly
```

### §1.9 — Set Theory Symbols = "Groups" + "Membership"

```
SET = a group of elements

  {1, 2, 3}          set containing 1, 2, 3
  ∅ or {}             empty set (containing nothing)
  ∈                   element of         3 ∈ {1,2,3} = "3 IS IN {1,2,3}"
  ∉                   not an element of  4 ∉ {1,2,3}
  ⊂                   subset             {1,2} ⊂ {1,2,3}
  ∪                   union              {1,2} ∪ {2,3} = {1,2,3}
  ∩                   intersection       {1,2} ∩ {2,3} = {2}
  \                   set difference     {1,2,3} \ {2} = {1,3}
  |A|                 cardinality (size)  |{1,2,3}| = 3 (has 3 elements)

COMPARISON WITH CODE (game devs know this):
  Set   ↔ HashSet, Set, List (unique)
  ∈     ↔ contains(), includes(), in
  ∪     ↔ union(), concat() + unique
  ∩     ↔ intersection(), filter()
  |A|   ↔ .length, .count, .size
```

### §1.10 — Calculus Symbols = "Change" + "Accumulation"

```
CALCULUS = mathematics of CHANGE and ACCUMULATION
  → Invented by Newton + Leibniz ~1687
  → Foundation of: physics, engineering, economics, machine learning

DERIVATIVE — "rate of change at a point":
  f'(x) or df/dx or dy/dx

  Meaning: if f(x) = vehicle position at time x
    → f'(x) = vehicle VELOCITY at time x (rate of change of position)
    → f''(x) = vehicle ACCELERATION (rate of change of velocity)

  Examples:
    f(x) = x²          → f'(x) = 2x
    (position = x²)       (velocity = 2x: increases steadily)

    f(x) = 3x + 5      → f'(x) = 3
    (position = 3x+5)     (velocity = 3: constant, uniform)

  Game dev use of derivatives:
    position' = velocity (velocity = derivative of position)
    velocity' = acceleration (acceleration = derivative of velocity)
    → Physics engine: each frame computes position += velocity × dt

INTEGRAL — "accumulated sum":
  ∫ f(x) dx = area under the graph of f(x)

  Meaning: if f(x) = vehicle velocity
    → ∫ f(x) dx = DISTANCE TRAVELED (accumulated velocity over time)

  Notation:
    ∫₀¹⁰ v(t) dt = distance traveled from t=0 to t=10
    (integral of velocity from 0 to 10 seconds = total distance)

  Game dev use of integrals (often hidden):
    position = ∫ velocity dt     → each frame: pos += vel × deltaTime
    velocity = ∫ acceleration dt → each frame: vel += acc × deltaTime
    → Euler integration — this IS discrete integration!

LIMIT:
  lim(x→a) f(x) = "what value does f(x) approach as x APPROACHES a"

  Example:
    lim(x→0) sin(x)/x = 1    (as x approaches 0, sin(x)/x approaches 1)

  → Limits are the FOUNDATION of both derivatives and integrals
  → Derivative = limit of the ratio of change as the interval approaches 0
  → Integral = limit of the sum of areas as divisions become infinitely small

DERIVATIVE + INTEGRAL = 2 SIDES OF THE SAME COIN:
  Derivative: know TOTAL → find RATE OF CHANGE at each point
  Integral:   know RATE OF CHANGE → find accumulated TOTAL
  → Fundamental Theorem of Calculus: ∫ f'(x) dx = f(x) + C
  → "Integration is the inverse of differentiation"
```

### §1.11 — Summary Table: Math "Vocabulary"

| Math Symbol Type | Natural Language Equivalent | Example | Estimated Count |
|---|---|---|---|
| Numbers | Specific nouns | 1, 2, π, e, √2 | ∞ (infinite number types) |
| Variables | Pronouns | x, y, n, θ | ~30 commonly used |
| Operators | Verbs | +, -, ×, ÷, ^, √, Σ, ∫ | ~30 commonly used |
| Relations | Comparison conjunctions | =, <, >, ≤, ≈, ∈ | ~15 |
| Grouping (brackets) | Punctuation | (, ), [, ], {, } | 6 |
| Functions | Processing machine / Verb phrase | sin, cos, log, f(x) | ~20 standard + infinite custom |
| Constants | Proper nouns | π, e, φ, i, ∞ | ~10 important ones |
| Logic | Connectives + Negation + Quantifiers | ∧, ∨, ¬, →, ∀, ∃ | ~10 |
| Set Theory | Groups + Membership | ∈, ⊂, ∪, ∩, ∅ | ~10 |
| Calculus | Change + Accumulation | d/dx, ∫, lim | ~5 core symbols |
| **TOTAL** | | | **~150 commonly used symbols** |

```
Comparison:
  Vietnamese vocabulary:  ~5,000-10,000 commonly used words (adult)
  English vocabulary:     ~5,000-10,000 commonly used words
  Math "vocabulary":      ~150 commonly used symbols

  → Math vocabulary is FAR SMALLER
  → But each symbol is FAR MORE PRECISE
  → Trade-off: BREADTH (small) vs PRECISION (extremely high)
```

---

## §2 — Math "Grammar": Expression Syntax

### §2.1 — Expression = Math's "Sentence"

```
EXPRESSION = combination of numbers + variables + operators according to rules
  → Equivalent to a "sentence" in natural language

Expression examples:
  3 + 2                           = simple expression
  x² + 2x + 1                    = algebraic expression
  sin(θ) × cos(θ)                = trigonometric expression
  Σᵢ₌₁ⁿ (2i + 1)                = summation expression
  ∫₀^π sin(x) dx                 = integral expression

TREE STRUCTURE (like natural language):
  Expression: (3 + 2) × (x - 1)

      [×]
     /   \
   [+]   [-]
   / \   / \
  3   2 x   1

  → Expression tree = like a syntax tree in natural language
  → Root node = last operation performed
  → Leaves = numbers / variables
```

### §2.2 — Operator Precedence = Math's "Grammar"

```
BODMAS / PEMDAS = the basic "grammar rules" of math:

  B/P — Brackets / Parentheses  ( )     ← HIGHEST priority
  O/E — Orders / Exponents      ^, √
  DM  — Division, Multiplication ÷, ×   ← left to right
  AS  — Addition, Subtraction    +, -   ← left to right, LOWEST priority

EXAMPLE: "WRONG DUE TO MISUNDERSTANDING GRAMMAR":
  2 + 3 × 4 = ?

  ❌ Wrong:   (2 + 3) × 4 = 20    (left to right, ignoring precedence)
  ✅ Correct:  2 + (3 × 4) = 14   (× before +)

  → Like "Let's eat, friend" vs "Let's eat friend" — ignoring rules = completely wrong interpretation

DETAILED COMPARISON:
  Natural language: word order + grammar rules → determine meaning
  Math:             operator precedence + brackets → determine result

  Natural language: rules HAVE EXCEPTIONS (irregular verbs, idioms...)
  Math:             rules have NO EXCEPTIONS (always consistent, 0 exceptions)
  → This is why math is PRECISE: 0 ambiguity, 0 exceptions
```

### §2.3 — Infix, Prefix, Postfix — 3 Ways to Write the Same Thing

```
Math can write the same operation in 3 DIFFERENT WAYS:

INFIX (middle) — the COMMON WAY:
  3 + 2        (operator IN THE MIDDLE of 2 operands)
  x × y
  a - b

PREFIX (before) — also called Polish notation:
  + 3 2        (operator BEFORE operands)
  × x y
  - a b
  → Advantage: NO BRACKETS NEEDED!
  → + × 3 2 5 = + (× 3 2) 5 = + 6 5 = 11
  → Used in: Lisp programming language

POSTFIX (after) — also called Reverse Polish:
  3 2 +        (operator AFTER operands)
  x y ×
  a b -
  → Advantage: NO BRACKETS NEEDED! + easy for stack machines
  → 3 2 × 5 + = (3 × 2) + 5 = 6 + 5 = 11
  → Used in: HP calculators, Forth programming, stack-based VMs

MORE COMPLEX EXAMPLE: (3 + 2) × (7 - 4)

  Infix:    (3 + 2) × (7 - 4)        = needs BRACKETS
  Prefix:   × + 3 2 - 7 4            = NO brackets needed!
  Postfix:  3 2 + 7 4 - ×            = NO brackets needed!

⭐ GAME DEVS KNOW:
  Shader language, stack VM: often uses postfix implicitly
  Expression parser: convert infix → postfix (Shunting Yard algorithm)
  Abstract Syntax Tree: represents expressions as a tree (all 3 notations are equivalent)

COMPARISON WITH NATURAL LANGUAGE:
  Natural language also has different "word orders":
    SVO (Vietnamese/English/Chinese): "I eat rice"  = Subject Verb Object = INFIX style
    SOV (Japanese/Korean):            "I rice eat"  = Subject Object Verb = POSTFIX style!
    VSO (Arabic):                     "Eat I rice"  = Verb Subject Object = PREFIX style!

  → SAME STRUCTURE, different order!
```

### §2.4 — Nesting — Recursion

```
MATH ALLOWS INFINITE NESTING (recursion):

  f(g(h(x)))           = function inside function inside function
  ((a + b) × (c - d))  = brackets inside brackets
  Σᵢ₌₁ⁿ (Σⱼ₌₁ᵐ aᵢⱼ)  = sum inside sum (matrix!)

  → LIKE natural language: clauses inside clauses
  Natural: "I think [that you know [that she said [that...]]]"
  Math:    f(g(h(x))) = f contains g contains h contains x

⭐ RECURSION DEPTH:
  Natural language: humans struggle after ~3-4 levels of nesting
    "The house [THAT [the girl [THAT [the man THAT I know] loves] built]] is beautiful"
    → 3 levels of relative clauses = VERY HARD to follow when heard

  Math: also struggles with deep nesting, BUT:
    → Uses INTERMEDIATE VARIABLES to flatten:
    Instead of: f(g(h(x)))
    Write:      a = h(x), b = g(a), c = f(b)
    → SAME as refactoring in code!

  Code: recursion depth = stack depth
    → Too deep → stack overflow
    → Flatten with intermediate variables = SAME technique as in math
```

### §2.5 — Equation = "Declarative Sentence"

```
EQUATION = expression = expression
  → Asserts: "left side EQUALS right side"

  x + 3 = 7           → "x plus 3 EQUALS 7" → solve: x = 4
  x² - 4 = 0          → "x² minus 4 EQUALS 0" → solve: x = ±2
  y = 2x + 1          → "y EQUALS 2x plus 1" → describes a straight line

"SOLVING AN EQUATION" = FINDING THE VALUE of the variable that makes the assertion TRUE:
  x + 3 = 7
  x = 7 - 3           (move to other side, change sign)
  x = 4               (the answer)
  Check: 4 + 3 = 7 ✅

COMPARISON:
  Natural: "SOMEONE eats rice"  → find: WHO?  → "I eat rice"
  Math:    "x + 3 = 7"          → find: x?    → "x = 4"
  → BOTH = finding MISSING INFORMATION to make the sentence COMPLETE
```

### §2.6 — Inequality = "Comparative Sentence"

```
INEQUALITY = expression related to expression (using <, >, ≤, ≥)
  → Asserts a RELATIONSHIP rather than EQUALITY

  x + 3 > 7           → "x plus 3 IS GREATER THAN 7"
  x > 4               → any x greater than 4 satisfies it
  → Result = a SET (many answers), not a single number

  0 ≤ x ≤ 1           → "x lies between 0 and 1" (including 0 and 1)
  → Describes a RANGE — game devs know: clamp(x, 0, 1)
```

### §2.7 — System of Equations = "Paragraph"

```
SYSTEM OF EQUATIONS = multiple equations simultaneously, with shared variables
  → Equivalent to a "paragraph" (multiple linked sentences)

  ┌ x + y = 10         sentence 1: x plus y equals 10
  └ x - y = 4          sentence 2: x minus y equals 4

  Solving: from 2 sentences → find x AND y:
    Add the two equations: 2x = 14 → x = 7
    Substitute: 7 + y = 10 → y = 3
    → x = 7, y = 3

  → Like natural language:
    "You and I have 10 apples total.
     I have 4 more than you.
     How many does each person have?"
    → SAME problem, different encoding (verbal vs math notation)
```

---

## §3 — Hierarchy: Symbol → Expression → Equation → Proof → Theory

```
LEVEL 1 — SYMBOL = "Word"
  3, x, +, =, sin, π
  → Smallest atom, with independent meaning

LEVEL 2 — EXPRESSION = "Phrase"
  3x + 2, sin(θ), x² - 4
  → Combines symbols according to rules

LEVEL 3 — EQUATION / STATEMENT = "Sentence"
  x² - 4 = 0
  ∀x ∈ ℝ: x² ≥ 0
  → Asserts something (true or false)

LEVEL 4 — PROOF = "Paragraph / Argument"
  "Let x² = 4.
   Since x² = 4, then x = √4 = ±2.
   Check: 2² = 4 ✅, (-2)² = 4 ✅.
   Therefore x = 2 or x = -2. QED."
  → Chain of logically linked statements → leads to conclusion

LEVEL 5 — THEOREM = "Paper"
  Pythagorean Theorem: a² + b² = c² (for right triangles)
  → Statement ALREADY PROVEN, reusable forever
  → Equivalent to a compiled "knowledge chunk" — retrieve instantly

LEVEL 6 — THEORY = "Book / System"
  Euclidean Geometry, Calculus, Linear Algebra, Group Theory...
  → System of MANY linked theorems
  → Equivalent to "schema" / "domain knowledge" in the framework

FRAMEWORK MAPPING:
  Level 1 Symbol      ↔ Chunk (atom)
  Level 2 Expression  ↔ Compound Chunk (small molecule)
  Level 3 Equation    ↔ Chunk chain (statement)
  Level 4 Proof       ↔ Schema (organized argument, purposeful)
  Level 5 Theorem     ↔ Compiled meta-chunk (instant retrieval)
  Level 6 Theory      ↔ Domain knowledge (full schema system)

⭐ EXPERT MATHEMATICIAN:
  → Seeing "x² + 2x + 1" → INSTANTLY recognizes = (x+1)²
  → Level 2 expression HAS BEEN COMPILED into a Level 5 pattern (meta-chunk)
  → Like an expert chess player seeing the board → pattern recognized instantly
  → "Computing quickly" = COMPILED PATTERN MATCH, not step-by-step calculation
```

---

## §4 — Math "Domains" and Their Notation

Each branch of math = 1 "dialect" with its own notation + conventions:

### §4.1 — Arithmetic — The Most Fundamental

```
Symbols: +, -, ×, ÷, =, <, >, ()
Objects: Specific numbers (1, 2, 3, 0.5, -7...)
Examples: 3 + 2 = 5, 12 ÷ 4 = 3, 7 × 8 = 56

Equivalent: "everyday language" — everyone uses it
Learned from: ~age 5-6
Applications: calculating prices, measuring, counting
```

### §4.2 — Algebra — Adding VARIABLES

```
NEW SYMBOLS: x, y, z (variables), aₙ (sequences), Σ (sum), Π (product)
Objects: Expressions with variables, equations, systems of equations
Example:
  ax² + bx + c = 0 (quadratic equation)
  → Solution: x = (-b ± √(b²-4ac)) / 2a (quadratic formula — 1 compiled meta-chunk!)

Equivalent: "language of abstraction" — talks about PATTERNS instead of specific numbers
Learned from: ~age 11-12
Applications: everywhere — physics, engineering, economics, game programming

⭐ The Jump from Arithmetic → Algebra:
  Arithmetic: "3 + 2 = 5"           (SPECIFIC)
  Algebra:    "a + b = b + a"        (GENERAL — true for ALL numbers)
  → This is the first time math talks about PATTERN rather than instance
  → Like: "a specific dog" → "ALL dogs" (∀ dog)
```

### §4.3 — Geometry — Adding SHAPE + SPACE

```
NEW SYMBOLS: ∠ (angle), ⊥ (perpendicular), ∥ (parallel), △ (triangle),
             π (circumference/radius), r (radius), A (area), V (volume)

Key formulas:
  Circle circumference: C = 2πr
  Circle area:          A = πr²
  Pythagorean:          a² + b² = c² (right triangle)
  Triangle area:        A = ½ × base × height

Equivalent: "language of space" — describes shape + position
Learned from: ~age 9-10 (basic), ~14-15 (proofs)

⭐ SPECIAL: Geometry = VISUAL + SYMBOLIC combined
  → Must see SHAPES + read NOTATION simultaneously
  → 2 encodings at once: L2 visual + L2 math notation
  → This is why geometry "feels different" from algebra: needs spatial reasoning
  → Game dev: collision detection, ray casting, mesh geometry
```

### §4.4 — Calculus — Adding INFINITY + CONTINUITY

```
NEW SYMBOLS: lim, dx, dy, d/dx, ∫, ∂ (partial derivative), ∞

Key formulas:
  Derivative:  d/dx [xⁿ] = n·xⁿ⁻¹
  Integral:    ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C
  Chain rule:  d/dx [f(g(x))] = f'(g(x)) · g'(x)

Equivalent: "language of change" — describes continuous variation
Learned from: ~age 17-18 (university)

⭐ Calculus = THE BIGGEST LEAP in math:
  Before calculus: math talked about SPECIFIC NUMBERS + FIXED PATTERNS
  Calculus:        math talks about CHANGE + ACCUMULATION + INFINITY
  → Opened up: physics (Newton), engineering, economics, ML
  → Game dev: physics integration, smooth animation, bezier curves
```

### §4.5 — Probability & Statistics — Adding UNCERTAINTY

```
NEW SYMBOLS: P(A) (probability), E[X] (expected value), σ (standard deviation),
             μ (mean), Var(X) (variance), n! (factorial), C(n,k) (combinations)

Key formulas:
  P(A) = number of favorable outcomes / total outcomes
  P(A∩B) = P(A) × P(B)    (if A, B are independent)
  E[X] = Σ xᵢ × P(xᵢ)    (expected value = weighted average)

Equivalent: "language of uncertainty" — talks about the NOT-YET-CERTAIN
Learned from: ~age 15-16 (basic), ~18+ (advanced)

⭐ Game dev use: random loot, damage variance, matchmaking, gacha probability
  Example: P(legendary drop) = 0.01 = 1%
  → After 100 opens: expected value E = 100 × 0.01 = 1 legendary
  → But NOT guaranteed — could be 0, could be 3 (variance!)
```

### §4.6 — Logic — Adding PROOF + REASONING

```
NEW SYMBOLS: ∧ (and), ∨ (or), ¬ (not), → (implies), ↔ (iff),
             ∀ (for all), ∃ (exists), ⊢ (provable), ⊨ (satisfies)

Equivalent: "language of rigorous reasoning" — talks about TRUE/FALSE
Learned from: ~age 18+ (discrete math, philosophy)

⭐ Logic = FOUNDATION for:
  → Mathematical proof: every proof = a chain of logic
  → Programming: if/else, boolean, conditional = logic
  → AI: logical reasoning, constraint satisfaction
  → Database: SQL WHERE clause = logic predicate
```

### §4.7 — Linear Algebra — Adding VECTORS + MATRICES

```
NEW SYMBOLS: v⃗ (vector), A (matrix), det(A) (determinant),
             A⁻¹ (inverse), Aᵀ (transpose), λ (eigenvalue)

Matrix example:
  A = [1  2]    vector: v⃗ = [3]
      [3  4]              [5]

  A × v⃗ = [1×3 + 2×5] = [13]
           [3×3 + 4×5]   [29]

Equivalent: "language of spatial transformation" — rotate, scale, stretch, project
Learned from: ~age 18+ (university)

⭐ GAME DEVS USE THIS A LOT:
  → Transform matrix: position, rotation, scale
  → Camera matrix: world → view → projection
  → Shader: every vertex transform = matrix multiplication
  → Physics: inertia tensor = matrix
  → ML/AI: neural network = layers of matrix multiplication

  Game dev example:
  Rotating point (x,y) by angle θ:
  [x'] = [cos(θ)  -sin(θ)] [x]
  [y']   [sin(θ)   cos(θ)] [y]

  → 1 matrix multiplication = 1 rotation
  → Stacking matrices = stacking multiple transformations
  → This is why GPUs exist: hardware built for fast matrix multiplication
```

---

## §5 — Comparison: Math vs Natural Language

| Feature | Natural Language (Vietnamese/English/Chinese) | Mathematical Language |
|---|---|---|
| **"Vocabulary"** | ~5,000-10,000 common words | ~150 common symbols |
| **Ambiguity** | ⭐ YES (polysemous, context-dependent) | ❌ NO (1 symbol = 1 precise meaning) |
| **Exceptions** | ⭐ MANY (irregular verbs, idioms...) | ❌ NONE (0 exceptions) |
| **Recursion** | 3-4 levels max (humans struggle) | Infinite (theoretical), flatten with intermediate variables |
| **Precision** | Low-Medium (approximate description) | ⭐ EXTREMELY HIGH (absolute precision) |
| **Breadth** | ⭐ EXTREMELY BROAD (can describe anything) | NARROW (only quantity + relation + structure) |
| **Shareability** | Requires shared language | ⭐ GLOBAL (math notation identical worldwide) |
| **Learning curve** | ~3-5 years to master L1 | ~12-15 years (arithmetic → calculus) |
| **Cultural variation** | ⭐ VERY LARGE (Viet ≠ Eng ≠ Chinese) | ALMOST NONE (~minor notation differences) |
| **Emotional content** | ⭐ RICH (love, hate, sadness...) | ❌ NONE |
| **Social content** | ⭐ RICH (formal, intimate, distant...) | ❌ NONE |
| **Topics** | Everything | Quantity, structure, space, change |
| **Evolution speed** | Fast (new words every year) | Slow (new symbols every decade/century) |
| **"Native speaker"** | All children | NONE — must be learned formally |

```
SUMMARY:

Natural language:  BROAD + FLEXIBLE + AMBIGUOUS + EMOTIONAL
                   → Optimal for SOCIAL COMMUNICATION + ALL TOPICS

Math language:     NARROW + RIGID + PRECISE + UNEMOTIONAL
                   → Optimal for QUANTITY + STRUCTURE + PROOF

→ Neither is "better" — each is optimal for DIFFERENT PURPOSES
→ A doctor uses BOTH: natural language (speaking to patients) + math (calculating dosages)
→ A game dev uses BOTH: natural language (design documents) + math (physics, shaders)
```

---

## §6 — Math in Practice: How Experts ACTUALLY Use Math

### §6.1 — Beginner vs Expert Solving the Same Problem

```
PROBLEM: Solve the equation x² - 5x + 6 = 0

BEGINNER (step by step, heavy L3 processing):
  Step 1: Recall the quadratic formula: x = (-b ± √(b²-4ac)) / 2a   ← retrieve chunk
  Step 2: Identify a=1, b=-5, c=6                                    ← pattern match
  Step 3: Calculate b² = (-5)² = 25                                  ← calculate
  Step 4: Calculate 4ac = 4×1×6 = 24                                 ← calculate
  Step 5: Calculate Δ = 25 - 24 = 1                                  ← calculate
  Step 6: Calculate √Δ = √1 = 1                                      ← calculate
  Step 7: x₁ = (5+1)/2 = 3, x₂ = (5-1)/2 = 2                      ← calculate
  Step 8: Check: 9-15+6=0 ✅, 4-10+6=0 ✅                           ← verify

  → 8 steps, each = 1 chunk retrieve + apply
  → Heavy L3 processing, PFC works hard
  → Like a beginner making coffee: every step explicit

EXPERT (pattern match, light L3):
  Sees: x² - 5x + 6 = 0
  → INSTANT: "product 6, sum 5 → (x-2)(x-3) = 0 → x=2 or x=3"
  → 1 step only: pattern match → retrieve compiled solution
  → L1 → L4 (skip L2+L3 almost entirely)
  → Like an expert making coffee: hands work automatically

  Expert compiled meta-chunk: "ax²+bx+c with small Δ → try factoring first"
  → This is "experience" = compiled pattern from hundreds of similar problems
```

### §6.2 — "Computing" vs "Recognizing Patterns" — Both at Once

```
WHAT SCIENTISTS ACTUALLY DO when "calculating":

PHASE 1 — RECOGNITION (Pattern Match):
  Look at problem → recognize PROBLEM TYPE → retrieve relevant schema
  "Ah, this is an optimization problem" / "This is a differential equation"
  → L1 Pattern Match: compiled chunks fire

PHASE 2 — PLANNING (Imagine-Final):
  "Need: find minimum → derivative = 0 → solve → check"
  → L4 Plan: Imagine-Final forms (knows what the answer should look like)
  → Imagine-Final = "find the value of x where f(x) is smallest"

PHASE 3 — CHAIN STEPS (Build Arc):
  Step 1: compute f'(x)      → retrieve derivative rule + apply
  Step 2: solve f'(x) = 0   → retrieve algebra technique + apply
  Step 3: check f''(x)       → retrieve second derivative rule + check sign
  → L3 Sequential Chain: each step = retrieve chunk + apply

PHASE 4 — CHECKING (Evaluate):
  Substitute back → body feedback "correct" / "wrong, go back"
  → L0 → L1 feedback loop

→ "Computing" = MIX of:
  • PATTERN MATCH (recognize problem type — compiled, instant)
  • RETRIEVAL (recall formulas, rules — compiled chunks)
  • CHAIN (connect logical steps — L3 processing)
  • CALCULATE (compute specific numbers — L3 but often compiled for small numbers)

→ A "good at math" scientist = someone who has:
  • MANY compiled patterns (fast recognition)
  • MANY compiled rules (instant retrieval)
  • SMOOTH chain execution (steps connect fluidly)
  → NOT "calculates faster" — but "RECOGNIZES faster" + "CONNECTS more smoothly"
```

### §6.3 — Draft vs Presentation: 2 Different Modes

```
SCRATCH WORK (draft) — how scientists ACTUALLY solve:
  → Write chaotically, try this direction then that
  → Cross out, rewrite, sketch diagrams alongside
  → Use "..." to skip obvious steps
  → MIX: math notation + natural language + sketches + arrows
  → = L3 PROCESSING in progress, messy, exploratory

FORMAL PRESENTATION — after solving is done:
  → Rewrite neatly, each step clear
  → "Let... We have... Therefore... Thus..."
  → NO wrong paths, NO crossings-out
  → = COMPILED RESULT, clean, communicative

→ Like: email draft vs email sent
→ Like: prototype code vs production code
→ Process (messy) ≠ Product (clean)

⭐ INSIGHT: When reading a math textbook, you see the PRODUCT (polished presentation)
  → You assume mathematicians think in the same "straight line"
  → NOT SO! They also grope around, make mistakes, mess around — only the PRESENTATION is polished
  → The drafts of Euler, Gauss, Ramanujan: full of crossings-out, trial-and-error, sketches everywhere
```

---

## §7 — History of Mathematical Notation

```
TIMELINE — math notation did NOT always exist. It had to be INVENTED over thousands of years:

~3000 BCE  Babylon: Base-60 number system (why there are 60 minutes, 360° in a circle)
~1500 BCE  Egypt: Fractions, basic geometry (needed to build pyramids)
~500 BCE   Greece: Geometric proof (Euclid), irrational numbers (Pythagoras shock)
~600 CE    India: ZERO invented (Brahmagupta) → changed EVERYTHING
                   Negative numbers, decimal system
~800 CE    Arabic: Al-Khwarizmi → "Algebra" (al-jabr = "restoration")
                   → The word "algorithm" also comes from Al-Khwarizmi's name!
~1200      Fibonacci: Introduced Hindu-Arabic numerals (0-9) to Europe (replacing Roman numerals)
~1489      + and - : First appeared as symbols (Johannes Widmann, Germany)
~1557      = : Robert Recorde invented the equals sign (England)
                "No two things are more equal than two parallel lines" — his reason for the symbol
~1591      Viète: Used LETTERS for variables (a, b, c for known; x, y, z for unknown)
                → BEFORE THIS: all equations written in WORDS (natural language!)
                   "The square of the unknown plus five times the unknown equals six"
                → AFTER: x² + 5x = 6
                → ⭐ THE BIG LEAP: from verbal → symbolic
~1614      Logarithm: John Napier invented (Scotland)
~1637      Descartes: x,y coordinate system (Cartesian coordinates) → Geometry + Algebra UNIFIED
~1655      ∞ : John Wallis invented the infinity symbol
~1687      Newton + Leibniz: Calculus (derivatives, integrals)
                Leibniz: notation dx, dy, ∫ (integral = elongated S for "Summa")
                Newton: ẋ notation (dot notation — still used in physics)
~1734      Euler: e, i, f(x), Σ, π (most familiar symbols = introduced by Euler!)
~1821      Cauchy: ε-δ definition (rigorous limits)
~1847      Boole: Boolean algebra (AND, OR, NOT) → FOUNDATION of computers!
~1874      Cantor: Set theory {}, ∈, ⊂ → FOUNDATION of modern math
~1889      Peano: ∀, ∃ (logic quantifiers)
~1931      Gödel: Incompleteness theorems → "there are TRUE statements that CANNOT be proven"
~1936      Turing: Turing machine → FOUNDATION of computer science

⭐ INSIGHTS FROM HISTORY:
  1. The "+" symbol is only ~500 years old. Before, "plus" was written in WORDS.
  2. The "=" sign is only ~470 years old. Before, "equals" was written in WORDS.
  3. Using x, y for variables is only ~430 years old. Before, "unknown" was written in WORDS.
  4. ALL math before ~1500 was written in NATURAL LANGUAGE!
     → Math notation = AN INVENTION to compress + make natural language precise
     → Like: programming language = an invention to compress + formalize natural language for machines
  5. Each new symbol = 1 new chunk → allows more complex COMPRESSION + CHAINING
     → "+" compresses "the act of addition" into 1 character
     → "∫" compresses "infinite sum of infinitely small areas" into 1 character
     → EACH NEW SYMBOL = 1 NEW LEVEL OF ABSTRACTION
```

---

## §8 — Framework Lens + Open Questions

### §8.1 — Math in the Processing Layers Model

```
How math uses the Processing Layers:

L0 (Body Input):    Reading symbols on paper/screen (visual)
L1 (Pattern Match): Recognizing problem type, familiar patterns (compiled chunks)
L2 (Encoding):      Math notation format (x, +, =, ∫, Σ...)
L3 (Processing):    Chain logic steps, calculate, prove
L4 (Plan/Execute):  Organize solution strategy, write result

Beginner math:  Heavy L2 (still learning notation) + Heavy L3 (step by step)
Expert math:    Light L2 (notation automatic) + Light L3 (pattern match skip)
                → L0 → L1 → L4 (like a routine, but only for familiar problems!)

⭐ Math expertise = COMPILE L2+L3 into L1 meta-chunks:
  "x² - 5x + 6 = (x-2)(x-3)" already compiled → see it and KNOW, no calculation needed
  Like: "3 × 7 = 21" compiled since age 8 → see it and KNOW
```

### §8.2 — Math vs Natural Language: Complementary Formats

```
SAME IDEA, 2 ENCODINGS:

Math:     F = ma
Natural:  "Force equals mass times acceleration"

Math:     E = mc²
Natural:  "Energy equals mass times the speed of light squared"

Math:     ∫₀^∞ e^(-x²) dx = √π/2
Natural:  "The integral from 0 to infinity of e to the power of negative x squared
           equals the square root of pi divided by 2"
           → ~14 words in natural language = 1 line of math notation
           → Math COMPRESSION: ~14 words → 1 line

→ This is why math notation EXISTS:
  EXTREME COMPRESSION for quantity + relation
  But ONLY for quantity + relation — cannot compress emotion, social dynamics, narrative
```

### §8.3 — Open Questions

1. **Why do children EVERYWHERE learn arithmetic early (~ages 5-6)?** Is number sense a "pre-verbal substrate" like pre-verbal chunks in F1? (Research: Dehaene 1997 "Number Sense" — dedicated brain area for numbers: Intraparietal sulcus.)

2. **Algebra = the first time math ABSTRACTS OVER INSTANCES** (from "3+2" to "a+b"). Is this a PFC-dependent transition? (Prediction: algebra difficulty correlates with PFC maturation timeline.)

3. **Why is proof/proving SO MUCH HARDER than calculating?** Because proof = GENERATIVE (must CREATE new argument), calculate = SEQUENTIAL (chain known steps). Proof ≈ L3 Generative pattern, calculate ≈ L3 Sequential pattern.

4. **Math anxiety = speech-act compile level?** (Per NT7 discussion) Math anxiety ≠ "the number 3 is tagged as threat" → "3 is used in all contexts, recyclable". Math anxiety = "the act of doing math in a social context" is tagged as threat (like the speech-act level). Prediction: math anxiety only appears with SOCIAL STAKES (tests, called to the board), not when solving alone.

5. **New symbol = new chunk compression** (§7 history). Does the H12 language evolution driver apply to math notation? "A mathematician feels the need for a new symbol → coins the symbol → community adopts." Like the H12 word coining mechanism?

6. **Chinese math advantage?** Chinese number words are shorter than English (一二三四五六七八九十 = monosyllabic). Working memory for Chinese speakers holds MORE NUMBERS per slot. Evidence: Chinese children calculate faster (Miller & Stigler 1987). → Handle size matters!

### §8.4 — References

| Author | Year | Work | Relevance |
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
> Reference document for exploration session N+5. Read for deep understanding, especially §5 (comparison table) and §6 (how experts actually use math).
>
> Version: v1.0, 2026-04-16.
