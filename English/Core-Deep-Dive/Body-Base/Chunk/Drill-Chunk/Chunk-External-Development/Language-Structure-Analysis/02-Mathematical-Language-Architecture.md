---
title: Mathematical Language Architecture — Mathematics as a Language System
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — read and study at leisure
scope: Mathematics as a language system — symbols, syntax, structure, comparison with natural language
purpose: Understand math not to "solve problems" but to see its architecture as a communication format
parent: ../../plan.md (F3 Chunk-External-Development)
language: English
source_version: Vietnamese v1.0
english_created: 2026-06-06
note: Written for those who USE math daily but have never "dissected" its structure
---

# Mathematical Language Architecture — Mathematics as a Language System

> **Purpose**: You use math every day (calculating prices, measuring, coding game physics,...) but have never looked at math as a LANGUAGE SYSTEM. This file "dissects" the structure of math — not to solve problems, but to reveal math as a communication format with its own "vocabulary", "grammar", "sentences", and "paragraphs".
>
> **Comparison with file 01**: File 01 analyzes natural language (Vietnamese/English/Chinese). This file analyzes mathematical language. Both are Communication Modality formats — but with VERY DIFFERENT architectures.
>
> **How to read**: Read each section at leisure. No need to know advanced math — this file focuses on STRUCTURE, not on PROBLEM-SOLVING SKILL.

---

## TABLE OF CONTENTS

- §1 — Mathematical "vocabulary": Types of symbols
  - §1.1 Numbers — Number systems
  - §1.2 Variables
  - §1.3 Operators
  - §1.4 Relations
  - §1.5 Grouping
  - §1.6 Functions
  - §1.7 Constants — Special constants
  - §1.8 Logic symbols
  - §1.9 Set theory symbols
  - §1.10 Calculus symbols
  - §1.11 Summary table: mathematical "vocabulary"
- §2 — Mathematical "grammar": Expression syntax
  - §2.1 Expression = mathematical "sentence"
  - §2.2 Operator precedence = mathematical "grammar"
  - §2.3 Infix, Prefix, Postfix — 3 ways to write the same thing
  - §2.4 Nesting (recursion)
  - §2.5 Equation = "statement sentence"
  - §2.6 Inequality = "comparison sentence"
  - §2.7 System of equations = "paragraph"
- §3 — Hierarchy: Symbol → Expression → Equation → Proof → Theory
- §4 — Mathematical domains and their notation
  - §4.1 Arithmetic
  - §4.2 Algebra
  - §4.3 Geometry
  - §4.4 Calculus
  - §4.5 Probability & Statistics
  - §4.6 Logic
  - §4.7 Linear Algebra
- §5 — Comparison: Math vs Natural Language
- §6 — Math in practice: How experts ACTUALLY use math
- §7 — History of mathematical notation
- §8 — Framework lens + Open questions

---

## §1 — Mathematical "vocabulary": Types of symbols

Natural language has nouns, verbs, adjectives,... Math also has its own "parts of speech":

### §1.1 — Numbers = The "Nouns" of Math

Numbers = the most basic objects, equivalent to nouns in natural language.

```
NATURAL NUMBERS (ℕ):
  0, 1, 2, 3, 4, 5, ...
  → Counting objects: "3 dogs" → 3 ∈ ℕ
  → Oldest: since humans learned to count (~40,000 years ago?)

INTEGERS (ℤ):
  ..., -3, -2, -1, 0, 1, 2, 3, ...
  → Adds NEGATIVE numbers: "in debt by 5" → -5
  → ℤ from German "Zahlen" = "numbers"
  → Invented: ~600 CE (India, Brahmagupta)

RATIONAL NUMBERS (ℚ):
  1/2, 3/4, -2/3, 0.75, 1.333...
  → Any number expressible as p/q (fraction)
  → ℚ from "Quotient"
  → Invented: ~1500 BCE (Egypt, Rhind Papyrus)

IRRATIONAL NUMBERS:
  √2 = 1.41421356..., π = 3.14159265..., e = 2.71828182...
  → CANNOT be expressed as a fraction
  → Infinite decimal with NO repeating pattern
  → Discovery of √2 (shock!): ~500 BCE (Greece, Pythagoreans)
    → Legend: Hippasus proved √2 is irrational → was thrown into the sea
       for shattering the belief "all things are ratios of integers"

REAL NUMBERS (ℝ):
  All numbers on the number line: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ
  → Includes both rational + irrational
  → Visualize: every POINT on a line = 1 real number

COMPLEX NUMBERS (ℂ):
  a + bi, where i = √(-1)
  → Examples: 3 + 2i, -1 + 0.5i
  → i² = -1 (square root of -1 — "impossible" but useful!)
  → Used in: electronics, quantum physics, games (quaternions for 3D rotation!)
  → Invented: ~1545 (Cardano, solving cubic equations)

VISUALIZATION: Nested number layers
  ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ
  │    │    │    │    │
  │    │    │    │    └── Complex numbers (add the "imaginary" dimension)
  │    │    │    └── Real numbers (fill the number line)
  │    │    └── Rational numbers (fractions)
  │    └── Integers (add negatives)
  └── Natural numbers (counting)

  → Each layer = EXTENDS the previous layer to solve new problems:
    "3 - 5 = ?"   → needs ℤ (negatives)
    "1 ÷ 3 = ?"   → needs ℚ (fractions)
    "√2 = ?"      → needs ℝ (irrationals)
    "√(-1) = ?"   → needs ℂ (complex)
```

### §1.2 — Variables = The "Pronouns" of Math

```
VARIABLE = symbol representing an UNKNOWN number or ANY number
  → Like a "pronoun" in natural language: "it" stands for a specific noun

COMMON CONVENTIONS:
  x, y, z         = unknown variables — solve equations to find them
  a, b, c         = known coefficients / parameters
  n, m, k         = integers (often for counting, indexing)
  i, j            = loop indices — familiar to any game developer!
  t               = time
  f, g, h         = functions
  θ (theta)       = angle
  Δ (delta)       = change / difference ("delta x" = how much x changed)
  Σ (sigma)       = sum
  ε (epsilon)     = very small number (close to 0)
  ∞ (infinity)    = infinity

EXAMPLES:
  "x + 3 = 7"    → x = pronoun, stands for the number 4 (unknown, must find)
  "for all n"     → n = pronoun, stands for "any integer"
  "f(x) = x²"   → x = any input, f = squaring function

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  "IT eats rice"      → "it" = stands for someone/something (needs context)
  Math:     "x + 3 = 7"        → "x" = stands for some number (must solve)

  Natural:  "EVERYONE eats"     → "everyone" = all
  Math:     "∀x: x + 0 = x"   → "∀x" = "for all x" = all numbers
```

### §1.3 — Operators = The "Verbs" of Math

```
OPERATOR = an action performed on numbers, equivalent to a VERB in natural language

ARITHMETIC (Basic):
  +    addition          3 + 2 = 5
  -    subtraction       7 - 4 = 3
  ×    multiplication    3 × 4 = 12    (also written: 3·4 or 3*4)
  ÷    division          12 ÷ 3 = 4    (also written: 12/3)
  ^    exponent          2³ = 8         (2 to the power 3 = 2×2×2)
  √    root              √9 = 3         (square root of 9)
  !    factorial         5! = 120        (5×4×3×2×1)
  %    percent           50% = 0.5
  mod  modulo            7 mod 3 = 1    (7 divided by 3 remainder 1 — game devs use this constantly!)

ALGEBRA:
  Σ    summation         Σᵢ₌₁ⁿ i = 1+2+3+...+n
  Π    product           Πᵢ₌₁ⁿ i = 1×2×3×...×n = n!
  |x|  absolute value    |-5| = 5, |3| = 3
  ⌊x⌋  floor (round down) ⌊3.7⌋ = 3
  ⌈x⌉  ceiling (round up) ⌈3.2⌉ = 4

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  "I    EAT  rice"      → EAT = verb (action)
  Math:     "3    +     2    = 5" → + = "verb" (the action of adding)

  Natural:  Many verb types (eat, run, think, love, fear,...)
  Math:     Fewer "verbs" but each is EXTREMELY PRECISE
            (+ always means addition, never anything else)
```

### §1.4 — Relations = Mathematical "Comparison Operators"

```
RELATIONS = symbols expressing the RELATIONSHIP between 2 expressions

  =     equal                  3 + 2 = 5
  ≠     not equal              3 ≠ 4
  <     less than              2 < 5
  >     greater than           7 > 3
  ≤     less than or equal     x ≤ 10
  ≥     greater than or equal  y ≥ 0
  ≈     approximately          π ≈ 3.14
  ∝     proportional           F ∝ ma (force proportional to mass × acceleration)
  ≡     identical / congruent  a ≡ b (mod n)
  ~     approximately equivalent  f(x) ~ g(x)

⭐ "=" IN MATH vs IN CODE:
  Math:  x = 5      → "x EQUALS 5" (asserting a fact)
  Code:  x = 5      → "ASSIGN 5 to x" (an action that changes state)
  Code:  x == 5     → "DOES x EQUAL 5?" (checking)

  → Game devs know "=" as assignment. Math uses "=" as assertion.
  → This is a classic source of confusion between math and programming.
```

### §1.5 — Grouping = Mathematical "Punctuation"

```
BRACKETS = control PROCESSING ORDER, equivalent to punctuation in natural language

  ( )    parentheses       (3 + 2) × 4 = 20
  [ ]    brackets          [a + b] × c
  { }    braces            {1, 2, 3} = set
  | |    absolute value / norm   |x| = absolute value

OPERATOR PRECEDENCE (when NO brackets):
  1. ( ) brackets                       ← HIGHEST priority
  2. ^ exponents
  3. × ÷ multiplication, division       ← left to right
  4. + - addition, subtraction          ← left to right, LOWEST priority

EXAMPLE — same numbers, DIFFERENT brackets = DIFFERENT result:
  3 + 2 × 4   = 3 + 8   = 11    (multiplication first)
  (3 + 2) × 4 = 5 × 4   = 20    (brackets first, then multiply)

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  Commas, periods, brackets = control how a sentence is UNDERSTOOD
            "Let's eat, mom!" vs "Let's eat mom!" ← punctuation completely changes meaning!
  Math:     Brackets = control how an expression is CALCULATED
            3+2×4 vs (3+2)×4 ← brackets completely change the result!

  → In both systems: punctuation/brackets = CONSTRAINT on how the parser processes
```

### §1.6 — Functions = "Processing machines" — input in, output out

```
FUNCTION = a "machine" that takes INPUT and produces OUTPUT following a fixed rule

SYNTAX: f(x) = expression containing x
  → f = function name
  → x = input (argument)
  → expression = processing rule
  → f(x) = output

BASIC FUNCTIONS:

  Linear function:    f(x) = 2x + 3
    f(0) = 3, f(1) = 5, f(10) = 23
    → Input × 2, then add 3

  Quadratic function: f(x) = x²
    f(0) = 0, f(2) = 4, f(-3) = 9
    → Input multiplied by itself (squared)

  Trigonometric functions:
    sin(θ)   = opposite / hypotenuse  (right triangle ratio — used CONSTANTLY in game dev!)
    cos(θ)   = adjacent / hypotenuse
    tan(θ)   = opposite / adjacent = sin(θ)/cos(θ)

    Game dev example:
      Character rotates 45° and moves forward 10 units:
      dx = 10 × cos(45°) ≈ 7.07    (displacement along x)
      dy = 10 × sin(45°) ≈ 7.07    (displacement along y)
      → sin/cos = "convert angle into x,y coordinates"

  Logarithmic functions:
    log₁₀(100) = 2    because 10² = 100    ("10 to what power = 100?" → 2)
    log₂(8)    = 3    because 2³ = 8       ("2 to what power = 8?" → 3)
    ln(e)      = 1    because e¹ = e       (ln = natural log, base e)

    → log = the INVERSE of exponentiation
    → Game devs use: log₂(n) = complexity of binary search algorithm

  Exponential function:
    eˣ      (e ≈ 2.71828, "Euler's number")
    2ˣ      (doubles at each step)

    → Exponential growth: 2⁰=1, 2¹=2, 2²=4, 2³=8, 2¹⁰=1024, 2²⁰=1,048,576
    → Game dev: 2ⁿ = texture size, memory allocation

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  Sentence = Subject + Verb + Object
  Math:     Expression = Function(Argument) = Result
            f(x) = y is equivalent to "function f PROCESSES input x, yielding y"

  Natural language functions (metaphor):
    "translate(Vietnamese sentence)" = English sentence
    "cook(ingredients)" = meal
    → Any PROCESS with input + output = a function!
```

### §1.7 — Constants = Mathematical "Proper Nouns"

```
CONSTANT = a SPECIFIC number with a proper name because it's too important / appears too frequently

  π (pi)     ≈ 3.14159265...    Ratio of circumference to diameter of a circle
                                 → Appears EVERYWHERE: circles, waves, oscillations, probability
                                 → Game dev: rotation, circular motion, wave patterns

  e (Euler)  ≈ 2.71828182...    Base of natural logarithm
                                 → Continuous growth: compound interest, radioactive decay
                                 → eˣ = the ONLY function whose derivative equals itself

  φ (phi)    ≈ 1.61803398...    Golden ratio
                                 → (1 + √5) / 2
                                 → Appears in: architecture, art, nature (shells, flowers)

  i          = √(-1)            Imaginary unit
                                 → i² = -1
                                 → Game dev: quaternions use i, j, k for 3D rotation

  ∞          = infinity         Not a number, but a CONCEPT
                                 → "larger than any number"
                                 → Used in: limits, integrals, series

COMPARISON:
  Natural language "proper nouns": London, Einstein, Everest — names FOR 1 SPECIFIC THING
  Math constants:                  π, e, φ — names FOR 1 SPECIFIC NUMBER that appears everywhere
```

### §1.8 — Logic symbols = "Connectives" + "Negation" + "Quantifiers"

```
LOGIC = a system of PRECISE reasoning, the foundation of all mathematical proof

LOGICAL CONNECTIVES:
  ∧   AND         p ∧ q = "BOTH p AND q are true"
  ∨   OR          p ∨ q = "p OR q (or both) is true"
  ¬   NOT         ¬p = "p is NOT true"
  →   IMPLIES     p → q = "IF p THEN q"
  ↔   IFF (if and only if)  p ↔ q = "p is true IF AND ONLY IF q is true"

QUANTIFIERS:
  ∀   FOR ALL       ∀x: x + 0 = x    "for ALL x, x plus 0 equals x"
  ∃   EXISTS        ∃x: x² = 4        "there EXISTS x such that x² = 4" (x = 2 or -2)
  ∄   NOT EXISTS    ∄x: x² = -1 (∈ℝ)  "there is NO real x such that x² = -1"

COMBINED EXAMPLES:
  ∀x ∈ ℝ: x² ≥ 0
  = "For ALL x in the reals: x squared is GREATER THAN OR EQUAL TO 0"
  = "The square of any real number is non-negative"

  ∃x ∈ ℤ: (x > 0) ∧ (x < 1)
  = "There exists x in the integers such that: x > 0 AND x < 1"
  = "Is there an integer larger than 0 and smaller than 1?"
  → Answer: NO (∄) — there is no integer between 0 and 1

COMPARISON WITH NATURAL LANGUAGE:
  Natural:  "IF it rains THEN I stay home"     → AND, OR, IF...THEN, NOT
  Math:     "if p is true THEN q is true" = p → q    → ∧, ∨, →, ¬

  Natural:  "EVERYONE eats" / "SOMEONE eats"
  Math:     "∀x: f(x)" / "∃x: f(x)"

  → SAME type of concept (and, or, not, all, exists)
  → Math: PRECISE (no ambiguity)
  → Natural: FLEXIBLE (can be ambiguous, polysemous)

  Example of AMBIGUITY in natural language:
    "I see someone" = ∃x: I see x (OK)
    "Everyone sees" = ∀x: x sees (?) or ∃x: everyone sees x (?)
    → Natural language is AMBIGUOUS! Math is NOT: must explicitly write ∀ or ∃
```

### §1.9 — Set theory symbols = "Group" + "Membership"

```
SET = a group of elements

  {1, 2, 3}          set containing 1, 2, 3
  ∅ or {}             empty set (contains nothing)
  ∈                   element of         3 ∈ {1,2,3} = "3 BELONGS TO the set {1,2,3}"
  ∉                   not element of     4 ∉ {1,2,3}
  ⊂                   subset             {1,2} ⊂ {1,2,3}
  ∪                   union              {1,2} ∪ {2,3} = {1,2,3}
  ∩                   intersection       {1,2} ∩ {2,3} = {2}
  \                   difference         {1,2,3} \ {2} = {1,3}
  |A|                 cardinality        |{1,2,3}| = 3 (has 3 elements)

COMPARISON WITH CODE (familiar to game devs):
  Set   ↔ HashSet, Set, List (unique)
  ∈     ↔ contains(), includes(), in
  ∪     ↔ union(), concat() + unique
  ∩     ↔ intersection(), filter()
  |A|   ↔ .length, .count, .size
```

### §1.10 — Calculus symbols = "Change" + "Accumulation"

```
CALCULUS = mathematics of CHANGE and ACCUMULATION
  → Newton + Leibniz invented it ~1687
  → Foundation of: physics, engineering, economics, machine learning

DERIVATIVE — "rate of change at a single point":
  f'(x) or df/dx or dy/dx

  Meaning: if f(x) = position of a car at time x
    → f'(x) = VELOCITY of the car at time x (rate of position change)
    → f''(x) = ACCELERATION of the car (rate of velocity change)

  Examples:
    f(x) = x²          → f'(x) = 2x
    (position = x²)       (velocity = 2x: increasing)

    f(x) = 3x + 5      → f'(x) = 3
    (position = 3x+5)     (velocity = 3: constant, uniform)

  Game devs use derivatives:
    position' = velocity (velocity = derivative of position)
    velocity' = acceleration (acceleration = derivative of velocity)
    → Physics engine: each frame computes position += velocity × dt

INTEGRAL — "accumulated sum":
  ∫ f(x) dx = area under the graph of f(x)

  Meaning: if f(x) = velocity of a car
    → ∫ f(x) dx = DISTANCE traveled (accumulated velocity over time)

  Notation:
    ∫₀¹⁰ v(t) dt = distance from t=0 to t=10
    (integrate velocity from 0 to 10 seconds = total distance)

  Game devs use integrals (often implicitly):
    position = ∫ velocity dt     → each frame: pos += vel × deltaTime
    velocity = ∫ acceleration dt → each frame: vel += acc × deltaTime
    → Euler integration — this IS discrete integration!

LIMIT:
  lim(x→a) f(x) = "what value does f(x) approach as x APPROACHES a"

  Example:
    lim(x→0) sin(x)/x = 1    (as x approaches 0, sin(x)/x approaches 1)

  → Limits are the FOUNDATION for both derivatives and integrals
  → Derivative = limit of the rate of change as the interval approaches 0
  → Integral = limit of the sum of areas as the pieces become infinitely small

DERIVATIVE + INTEGRAL = 2 SIDES OF 1 COIN:
  Derivative: know the TOTAL → find RATE OF CHANGE at each point
  Integral: know the RATE OF CHANGE → find the accumulated TOTAL
  → Fundamental Theorem of Calculus: ∫ f'(x) dx = f(x) + C
  → "Integration is the inverse of differentiation"
```

### §1.11 — Summary table: Mathematical "vocabulary"

| Math symbol type | Natural language equivalent | Examples | Estimated count |
|---|---|---|---|
| Numbers | Concrete nouns | 1, 2, π, e, √2 | ∞ (infinite number types) |
| Variables | Pronouns | x, y, n, θ | ~30 commonly used |
| Operators | Verbs | +, -, ×, ÷, ^, √, Σ, ∫ | ~30 commonly used |
| Relations | Comparison connectives | =, <, >, ≤, ≈, ∈ | ~15 |
| Grouping | Punctuation | (, ), [, ], {, } | 6 |
| Functions | Processing machine / Verb phrase | sin, cos, log, f(x) | ~20 basic + unlimited custom |
| Constants | Proper nouns | π, e, φ, i, ∞ | ~10 important ones |
| Logic | Connectives + Negation + Quantifiers | ∧, ∨, ¬, →, ∀, ∃ | ~10 |
| Set theory | Group + Membership | ∈, ⊂, ∪, ∩, ∅ | ~10 |
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

## §2 — Mathematical "Grammar": Expression Syntax

### §2.1 — Expression = Mathematical "Sentence"

```
EXPRESSION = combination of numbers + variables + operators following rules
  → Equivalent to a "sentence" in natural language

Example expressions:
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

### §2.2 — Operator Precedence = Mathematical "Grammar"

```
BODMAS / PEMDAS = the foundational "grammar rule" of math:

  B/P — Brackets / Parentheses  ( )     ← HIGHEST priority
  O/E — Orders / Exponents      ^, √
  DM  — Division, Multiplication ÷, ×   ← left to right
  AS  — Addition, Subtraction    +, -   ← left to right, LOWEST priority

EXAMPLE: "WRONG BECAUSE OF MISSED GRAMMAR":
  2 + 3 × 4 = ?

  ❌ Wrong: (2 + 3) × 4 = 20     (left-to-right, ignoring precedence)
  ✅ Right: 2 + (3 × 4) = 14    (× before +)

  → Like "Let's eat mom!" vs "Let's eat, mom!" in English:
    Ignoring the rule = completely WRONG interpretation

DETAILED COMPARISON:
  Natural language: word order + grammar rules → determine meaning
  Math:             operator precedence + brackets → determine result

  Natural language: rules HAVE EXCEPTIONS (irregular verbs, idioms,...)
  Math:             rules HAVE NO EXCEPTIONS (always consistent, 0 exceptions)
  → This is why math is PRECISE: 0 ambiguity, 0 exceptions
```

### §2.3 — Infix, Prefix, Postfix — 3 ways to write the same thing

```
Math can write the same operation in 3 DIFFERENT WAYS:

INFIX (middle) — the STANDARD way:
  3 + 2        (operator IS BETWEEN 2 operands)
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
  → Advantage: NO BRACKETS NEEDED! + natural for stack machines
  → 3 2 × 5 + = (3 × 2) + 5 = 6 + 5 = 11
  → Used in: HP calculator, Forth programming, stack-based VM

COMPLEX EXAMPLE: (3 + 2) × (7 - 4)

  Infix:    (3 + 2) × (7 - 4)        = BRACKETS REQUIRED
  Prefix:   × + 3 2 - 7 4            = NO brackets needed!
  Postfix:  3 2 + 7 4 - ×            = NO brackets needed!

⭐ GAME DEV NOTE:
  Shader language, stack VM: often use postfix implicitly
  Expression parser: convert infix → postfix (Shunting Yard algorithm)
  Abstract Syntax Tree: represents expressions as a tree (all 3 notations equivalent)

COMPARISON WITH NATURAL LANGUAGE:
  Natural language also has different "word orders":
    SVO (Vietnamese/English/Chinese): "I eat rice"  = Subject Verb Object = INFIX style
    SOV (Japanese/Korean):            "I rice eat"  = Subject Object Verb = POSTFIX style!
    VSO (Arabic):                     "Eat I rice"  = Verb Subject Object = PREFIX style!
  → SAME STRUCTURE, different ordering!
```

### §2.4 — Nesting (Recursion)

```
MATH ALLOWS INFINITE NESTING (recursion):

  f(g(h(x)))           = function nested inside function inside function
  ((a + b) × (c - d))  = brackets nested inside brackets
  Σᵢ₌₁ⁿ (Σⱼ₌₁ᵐ aᵢⱼ)  = sum nested inside sum (matrix!)

  → LIKE natural language: clauses inside clauses
  Natural: "I think [that you know [that she said [that...]]]"
  Math:    f(g(h(x))) = f contains g contains h contains x

⭐ RECURSION DEPTH:
  Natural language: humans struggle past ~3-4 nested layers
    "The house [that [the girl [that [the man [that I know] loved] built]] is beautiful]"
    → 3 nested relative clauses = VERY HARD to parse when spoken

  Math: also struggles with deep nesting, BUT:
    → Uses INTERMEDIATE VARIABLES to flatten:
    Instead of: f(g(h(x)))
    Write:      a = h(x), b = g(a), c = f(b)
    → SAME as refactoring in code!

  Code: recursion depth = stack depth
    → Too deep → stack overflow
    → Flatten with intermediate variables = THE SAME technique as math
```

### §2.5 — Equation = "Statement Sentence"

```
EQUATION = expression = expression
  → Asserts: "left side EQUALS right side"

  x + 3 = 7           → "x plus 3 EQUALS 7" → solve: x = 4
  x² - 4 = 0          → "x² minus 4 EQUALS 0" → solve: x = ±2
  y = 2x + 1          → "y EQUALS 2x plus 1" → describes a straight line

"SOLVING AN EQUATION" = FINDING the value of the variable that makes the assertion TRUE:
  x + 3 = 7
  x = 7 - 3           (transpose, change sign)
  x = 4               (answer)
  Check: 4 + 3 = 7 ✅

COMPARISON:
  Natural:  "SOMEONE ate" → find: WHO? → "I ate"
  Math:     "x + 3 = 7"  → find: x?   → "x = 4"
  → BOTH = finding MISSING INFORMATION to complete the statement
```

### §2.6 — Inequality = "Comparison Sentence"

```
INEQUALITY = expression in relation to expression (using <, >, ≤, ≥)
  → Asserts a RELATIONSHIP rather than EQUALITY

  x + 3 > 7           → "x plus 3 is GREATER THAN 7"
  x > 4               → any x greater than 4 satisfies it
  → Result = A SET (many answers), not 1 number

  0 ≤ x ≤ 1           → "x is between 0 and 1" (inclusive)
  → Describes a RANGE — game devs know: clamp(x, 0, 1)
```

### §2.7 — System of Equations = "Paragraph"

```
SYSTEM OF EQUATIONS = multiple equations simultaneously, with shared variables
  → Equivalent to a "paragraph" (multiple linked sentences)

  ┌ x + y = 10         sentence 1: x plus y equals 10
  └ x - y = 4          sentence 2: x minus y equals 4

  Solve: from 2 sentences → find x AND y:
    Add the 2 equations: 2x = 14 → x = 7
    Substitute: 7 + y = 10 → y = 3
    → x = 7, y = 3

  → Like natural language:
    "Together we have 10 apples.
     I have 4 more than you.
     How many does each of us have?"
    → THE SAME PROBLEM, only different encoding (verbal vs math notation)
```

---

## §3 — Hierarchy: Symbol → Expression → Equation → Proof → Theory

```
LEVEL 1 — SYMBOL = "Word"
  3, x, +, =, sin, π
  → Smallest atom, carries its own meaning

LEVEL 2 — EXPRESSION = "Phrase"
  3x + 2, sin(θ), x² - 4
  → Symbols combined following rules

LEVEL 3 — EQUATION / STATEMENT = "Sentence"
  x² - 4 = 0
  ∀x ∈ ℝ: x² ≥ 0
  → Asserts something (true or false)

LEVEL 4 — PROOF = "Paragraph / Argument"
  "Given x² = 4.
   Since x² = 4, we have x = √4 = ±2.
   Check: 2² = 4 ✅, (-2)² = 4 ✅.
   Therefore x = 2 or x = -2. QED."
  → Chain of logically linked statements → leads to conclusion

LEVEL 5 — THEOREM = "Essay/Thesis"
  Pythagorean Theorem: a² + b² = c² (for right-angled triangle)
  → A statement ALREADY PROVEN, usable forever
  → Equivalent to a compiled "knowledge chunk" — retrieve instantly

LEVEL 6 — THEORY = "Book / System"
  Euclidean Geometry, Calculus, Linear Algebra, Group Theory,...
  → A system of MANY interlinked theorems
  → Equivalent to "schema" / "domain knowledge" in the framework

MAPPING TO FRAMEWORK:
  Level 1 Symbol       ↔ Chunk (atom)
  Level 2 Expression   ↔ Chunk compound (small molecule)
  Level 3 Equation     ↔ Chunk chain (statement)
  Level 4 Proof        ↔ Schema (organized argument with purpose)
  Level 5 Theorem      ↔ Compiled meta-chunk (retrieve instantly)
  Level 6 Theory       ↔ Domain knowledge (full schema system)

⭐ EXPERT MATHEMATICIAN:
  → Sees "x² + 2x + 1" → INSTANTLY recognizes = (x+1)²
  → Level 2 expression COMPILED into Level 5 pattern (meta-chunk)
  → Like an expert chess player seeing the board → instantly recognizes patterns
  → "Calculating quickly" = PATTERN MATCHING against compiled chunks, not step-by-step calculation
```

---

## §4 — Mathematical Domains and Their Notation

Each branch of math = 1 "dialect" with its own symbols + conventions:

### §4.1 — Arithmetic — the most foundational

```
Symbols:  +, -, ×, ÷, =, <, >, ()
Objects:  Specific numbers (1, 2, 3, 0.5, -7,...)
Examples: 3 + 2 = 5, 12 ÷ 4 = 3, 7 × 8 = 56

Equivalent to: "everyday language" — everyone uses it
Learned from:  ~age 5-6
Applications:  calculating prices, measuring, counting
```

### §4.2 — Algebra — adds VARIABLES

```
NEW symbols:  x, y, z (variables), aₙ (sequence), Σ (sum), Π (product)
Objects:      Expressions with variables, equations, systems of equations
Examples:
  ax² + bx + c = 0 (quadratic equation)
  → Solution: x = (-b ± √(b²-4ac)) / 2a (quadratic formula — 1 compiled meta-chunk!)

Equivalent to: "language of abstraction" — speaks about PATTERNS instead of specific numbers
Learned from:  ~age 11-12
Applications:  everywhere — physics, engineering, economics, game programming

⭐ The leap from Arithmetic → Algebra:
  Arithmetic: "3 + 2 = 5" (SPECIFIC)
  Algebra:    "a + b = b + a" (GENERAL — true for ALL numbers)
  → This is the first time math speaks about PATTERNS rather than instances
  → Like: "a specific dog" → "EVERY dog" (∀ dog)
```

### §4.3 — Geometry — adds SHAPE + SPACE

```
NEW symbols: ∠ (angle), ⊥ (perpendicular), ∥ (parallel), △ (triangle),
             π (circumference/radius), r (radius), A (area), V (volume)

Key formulas:
  Circle circumference:  C = 2πr
  Circle area:           A = πr²
  Pythagorean:           a² + b² = c² (right triangle)
  Triangle area:         A = ½ × base × height

Equivalent to: "language of space" — describes shapes + positions
Learned from:  ~age 9-10 (basics), ~14-15 (proofs)

⭐ DISTINCTIVE: Geometry = VISUAL + SYMBOLIC combined
  → Must look at DIAGRAM + read SYMBOLS simultaneously
  → 2 encodings at once: L2 visual + L2 math notation
  → This is why geometry "feels different" from algebra: requires spatial reasoning
  → Game dev: collision detection, ray casting, mesh geometry
```

### §4.4 — Calculus — adds INFINITY + CONTINUITY

```
NEW symbols: lim, dx, dy, d/dx, ∫, ∂ (partial derivative), ∞

Key formulas:
  Derivative: d/dx [xⁿ] = n·xⁿ⁻¹
  Integral: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C
  Chain rule: d/dx [f(g(x))] = f'(g(x)) · g'(x)

Equivalent to: "language of change" — describes continuous variation
Learned from:  ~age 17-18 (university)

⭐ Calculus = THE BIGGEST LEAP in mathematics:
  Before calculus: math speaks about SPECIFIC NUMBERS + FIXED PATTERNS
  Calculus: math speaks about CHANGE + ACCUMULATION + INFINITY
  → Opened up: physics (Newton), engineering, economics, ML
  → Game dev: physics integration, smooth animation, bezier curves
```

### §4.5 — Probability & Statistics — adds UNCERTAINTY

```
NEW symbols: P(A) (probability), E[X] (expected value), σ (standard deviation),
             μ (mean), Var(X) (variance), n! (factorial),
             (n choose k) = C(n,k) (combinations)

Key formulas:
  P(A) = number of favorable outcomes / total outcomes
  P(A∩B) = P(A) × P(B)    (if A, B are independent)
  E[X] = Σ xᵢ × P(xᵢ)    (expected value = weighted average)

Equivalent to: "language of uncertainty" — speaks about WHAT IS NOT CERTAIN
Learned from:  ~age 15-16 (basics), ~18+ (advanced)

⭐ Game dev uses: random loot, damage variance, matchmaking, gacha probability
  Example: P(legendary drop) = 0.01 = 1%
  → After 100 pulls: expected value E = 100 × 0.01 = 1 legendary
  → But NOT certain — could be 0, could be 3 (that's variance!)
```

### §4.6 — Logic — adds PROOF + REASONING

```
NEW symbols: ∧ (and), ∨ (or), ¬ (not), → (implies), ↔ (iff),
             ∀ (for all), ∃ (exists), ⊢ (provable), ⊨ (satisfies)

Equivalent to: "language of strict reasoning" — speaks about TRUE/FALSE
Learned from:  ~age 18+ (discrete math, philosophy)

⭐ Logic = FOUNDATION for:
  → Mathematical proof: every proof = a chain of logic
  → Programming: if/else, boolean, conditional = logic
  → AI: logical reasoning, constraint satisfaction
  → Database: SQL WHERE clause = logic predicate
```

### §4.7 — Linear Algebra — adds VECTORS + MATRICES

```
NEW symbols: v⃗ (vector), A (matrix), det(A) (determinant),
             A⁻¹ (inverse), Aᵀ (transpose), λ (eigenvalue)

Matrix example:
  A = [1  2]    vector: v⃗ = [3]
      [3  4]              [5]

  A × v⃗ = [1×3 + 2×5] = [13]
           [3×3 + 4×5]   [29]

Equivalent to: "language of spatial transformation" — rotate, contract, stretch, project
Learned from:  ~age 18+ (university)

⭐ GAME DEV USES CONSTANTLY:
  → Transform matrix: position, rotation, scale
  → Camera matrix: world → view → projection
  → Shader: every vertex transform = matrix multiplication
  → Physics: inertia tensor = matrix
  → ML/AI: neural network = layers of matrix multiplication

  Game dev example:
  Rotate point (x,y) by angle θ:
  [x'] = [cos(θ)  -sin(θ)] [x]
  [y']   [sin(θ)   cos(θ)] [y]

  → 1 matrix multiplication = 1 rotation
  → Chain multiple matrices = chain multiple transformations
  → This is why GPUs exist: hardware optimized for fast matrix multiplication
```

---

## §5 — Comparison: Math vs Natural Language

| Feature | Natural Language (Vietnamese/English/Chinese) | Mathematical Language |
|---|---|---|
| **"Vocabulary"** | ~5,000-10,000 commonly used words | ~150 commonly used symbols |
| **Ambiguity** | ⭐ YES (polysemous, context-dependent) | ❌ NO (1 symbol = 1 precise meaning) |
| **Exceptions** | ⭐ MANY (irregular verbs, idioms,...) | ❌ NONE (0 exceptions) |
| **Recursion** | 3-4 layers max (humans struggle) | Unlimited (theoretically), flatten via intermediate variables |
| **Precision** | Low-Medium (approximate descriptions) | ⭐ EXTREME (absolute precision) |
| **Breadth** | ⭐ EXTREMELY BROAD (describes everything) | NARROW (only quantity + relation + structure) |
| **Shareability** | Requires shared language | ⭐ GLOBAL (math symbols identical worldwide) |
| **Learning curve** | ~3-5 years to master L1 | ~12-15 years (arithmetic → calculus) |
| **Cultural variation** | ⭐ VERY LARGE (Vietnamese ≠ English ≠ Chinese) | NEARLY NONE (~minor notation conventions) |
| **Emotional content** | ⭐ RICH (love, hate, sadness,...) | ❌ ABSENT |
| **Social content** | ⭐ RICH (respectful, intimate, distant,...) | ❌ ABSENT |
| **Topics** | Everything | Quantity, structure, space, change |
| **Evolution speed** | Fast (new words every year) | Slow (new symbols every decade/century) |
| **"Native speaker"** | Every child | NONE — must be learned formally |

```
SUMMARY:

Natural language:  BROAD + FLEXIBLE + AMBIGUOUS + EMOTIONALLY RICH
                   → Optimized for SOCIAL COMMUNICATION + ALL TOPICS

Math language:     NARROW + RIGID + PRECISE + EMOTIONALLY ABSENT
                   → Optimized for QUANTITY + STRUCTURE + PROOF

→ Neither is "better" — each is optimized for a DIFFERENT PURPOSE
→ Doctors use BOTH: natural language (talking to patients) + math (calculating doses)
→ Game devs use BOTH: natural language (design doc) + math (physics, shaders)
```

---

## §6 — Math in Practice: How Experts ACTUALLY Use Math

### §6.1 — Beginner vs Expert solving the same problem

```
PROBLEM: Solve the equation x² - 5x + 6 = 0

BEGINNER (step by step, heavy L3 processing):
  Step 1: Recall quadratic formula: x = (-b ± √(b²-4ac)) / 2a   ← retrieve chunk
  Step 2: Identify a=1, b=-5, c=6                                ← pattern match
  Step 3: Calculate b² = (-5)² = 25                              ← calculate
  Step 4: Calculate 4ac = 4×1×6 = 24                             ← calculate
  Step 5: Calculate Δ = 25 - 24 = 1                              ← calculate
  Step 6: Calculate √Δ = √1 = 1                                  ← calculate
  Step 7: x₁ = (5+1)/2 = 3, x₂ = (5-1)/2 = 2                   ← calculate
  Step 8: Check: 9-15+6=0 ✅, 4-10+6=0 ✅                        ← verify

  → 8 steps, each step = 1 chunk retrieve + apply
  → Heavy L3 processing, PFC works hard
  → Like a beginner making coffee: each step explicit

EXPERT (pattern match, light L3):
  Sees: x² - 5x + 6 = 0
  → INSTANT: "product 6, sum 5 → (x-2)(x-3) = 0 → x=2 or x=3"
  → 1 step: pattern match → retrieve compiled solution
  → L1 → L4 (skip L2+L3 almost entirely)
  → Like an expert making coffee: hands do it automatically

  Expert compiled meta-chunk: "ax²+bx+c with small Δ → try factoring first"
  → This is "experience" = compiled pattern from hundreds of similar problems
```

### §6.2 — "Calculating" vs "Pattern-matching" — both at once

```
WHAT A SCIENTIST ACTUALLY DOES when "doing math":

PHASE 1 — RECOGNITION (Pattern Match):
  See the problem → recognize PROBLEM TYPE → retrieve relevant schema
  "Ah, this is an optimization problem" / "This is a differential equation"
  → L1 Pattern Match: compiled chunks fire

PHASE 2 — PLAN (Imagine-Final):
  "Need: find minimum → derivative = 0 → solve → check"
  → L4 Plan: Imagine-Final forms (know what the answer will look like)
  → Imagine-Final = "find the value of x at which f(x) is smallest"

PHASE 3 — CHAIN STEPS (Build Arc):
  Step 1: compute f'(x)      → retrieve derivative rule + apply
  Step 2: solve f'(x) = 0    → retrieve algebra technique + apply
  Step 3: check f''(x)       → retrieve second derivative rule + check sign
  → L3 Sequential Chain: each step = retrieve chunk + apply

PHASE 4 — EVALUATE:
  Substitute back → body feedback "correct" / "wrong, backtrack"
  → L0 → L1 feedback loop

→ "Doing math" = MIX of:
  • PATTERN MATCH (recognizing problem type — compiled, instant)
  • RETRIEVAL (recalling formulas, rules — compiled chunks)
  • CHAIN (linking logical steps — L3 processing)
  • CALCULATE (computing specific numbers — L3, often compiled for small numbers)

→ A "skilled mathematician" = someone who has:
  • MANY compiled patterns (fast recognition)
  • MANY compiled rules (instant retrieval)
  • FLUENT chaining (smooth step-linking)
  → NOT "calculates faster" — but "RECOGNIZES faster" + "CHAINS more smoothly"
```

### §6.3 — Draft vs Presentation: 2 different modes

```
SCRATCH WORK — how scientists ACTUALLY solve:
  → Writing freely, trying this direction then that
  → Crossing out, rewriting, drawing diagrams alongside
  → Using "..." to skip obvious steps
  → MIX: math notation + natural language + drawings + arrows
  → = L3 PROCESSING in action, messy, exploratory

FORMAL PRESENTATION — after the problem is already solved:
  → Written neatly, step by step in clear order
  → "Given... We have... Therefore... Thus..."
  → NO wrong directions, NO crossed-out work
  → = COMPILED RESULT, clean, communicative

→ Like: email draft vs email sent
→ Like: prototype code vs production code
→ Process (messy) ≠ Product (clean)

⭐ INSIGHT: When reading a math textbook, you see the PRODUCT (clean presentation)
  → You might assume mathematicians think in equally neat linear steps
  → NOT SO! They also grope around, try wrong paths, get messy — they just PRESENT cleanly afterward
  → The scratch work of Euler, Gauss, Ramanujan: full of crossings-out, wrong attempts, messy diagrams
```

---

## §7 — History of Mathematical Notation

```
TIMELINE — mathematical notation did NOT always exist. It had to be INVENTED over thousands of years:

~3000 BCE  Babylon: Base-60 numeral system (why an hour has 60 minutes, a circle 360°)
~1500 BCE  Egypt: Fractions, basic geometry (building pyramids required measurement)
~500 BCE   Greece: Proof-based geometry (Euclid), irrational numbers (Pythagorean shock)
~600 CE    India: ZERO invented (Brahmagupta) → changed EVERYTHING
                  Negative numbers, decimal system
~800 CE    Arabic: Al-Khwarizmi → "Algebra" (al-jabr = "restoration")
                  → The word "algorithm" also comes from Al-Khwarizmi's name!
~1200 CE   Fibonacci: Introduced Hindu-Arabic numerals (0-9) to Europe (replacing Roman numerals)
~1489      + and - : First appeared as symbols (Johannes Widmann, Germany)
~1557      = : Robert Recorde invented the equals sign (England)
           "Nothing is more equal than 2 parallel lines" — his reason for choosing ==
~1591      Viète: Used LETTERS for variables (a, b, c for knowns; x, y, z for unknowns)
           → BEFORE THIS: all equations written in WORDS (natural language!)
              "The square of the unknown plus five times the unknown equals six"
           → AFTER: x² + 5x = 6
           → ⭐ MAJOR LEAP: verbal → symbolic
~1614      Logarithm: John Napier invented it (Scotland)
~1637      Descartes: x,y coordinate system (Cartesian coordinates) → Geometry + Algebra UNIFIED
~1655      ∞ : John Wallis invented the infinity symbol
~1687      Newton + Leibniz: Calculus (derivatives, integrals)
           Leibniz: notation dx, dy, ∫ (integral = elongated S, from Latin "Summa" = sum)
           Newton: notation ẋ (dot notation — still used in physics)
~1734      Euler: e, i, f(x), Σ, π (many of the most familiar symbols = coined by Euler!)
~1821      Cauchy: ε-δ definition (rigorous limits)
~1847      Boole: Boolean algebra (AND, OR, NOT) → FOUNDATION for computers!
~1874      Cantor: Set theory {}, ∈, ⊂ → FOUNDATION for modern math
~1889      Peano: ∀, ∃ (logic quantifiers)
~1931      Gödel: Incompleteness theorems → "there exist TRUE statements that CANNOT be proven"
~1936      Turing: Turing machine → FOUNDATION for computer science

⭐ INSIGHTS FROM HISTORY:
  1. The "+" symbol is only ~500 years old. Before that, "plus" was written in WORDS.
  2. The "=" sign is only ~470 years old. Before that, "equals" was written in WORDS.
  3. Using x, y for variables is only ~430 years old. Before that, "unknown" was written in WORDS.
  4. ALL mathematics before ~1500 was written in NATURAL LANGUAGE!
     → Math notation = an INVENTION to compress + make precise what natural language
       struggled to express
     → Like: programming language = an invention to compress + make precise natural language
       for machines
  5. Each new symbol = 1 new chunk → allows MORE COMPLEX COMPRESSION + CHAINING
     → "+" compresses "the operation of addition" into 1 character
     → "∫" compresses "infinite sum of infinitesimally small areas" into 1 character
     → EACH NEW SYMBOL = 1 NEW LEVEL OF ABSTRACTION
```

---

## §8 — Framework Lens + Open Questions

### §8.1 — Math in the Processing Layers model

```
How math uses the Processing Layers:

L0 (Body Input):    Reading symbols on paper/screen (visual)
L1 (Pattern Match): Recognizing problem type, familiar patterns (compiled chunks)
L2 (Encoding):      Math notation format (x, +, =, ∫, Σ,...)
L3 (Processing):    Chain logic steps, calculate, prove
L4 (Plan/Execute):  Organize solution strategy, write result

Beginner math:  Heavy L2 (still learning notation) + Heavy L3 (step by step)
Expert math:    Light L2 (notation automatic) + Light L3 (pattern match skip)
                → L0 → L1 → L4 (routine-like, for familiar problems!)

⭐ Math expertise = COMPILE L2+L3 into L1 meta-chunks:
  "x² - 5x + 6 = (x-2)(x-3)" already compiled → SEE it and KNOW, no calculation needed
  Like: "3 × 7 = 21" compiled since age 8 → SEE it and KNOW
```

### §8.2 — Math vs Natural Language: Complementary formats

```
SAME IDEA, 2 ENCODINGS:

Math:     F = ma
Natural:  "Force equals mass times acceleration"

Math:     E = mc²
Natural:  "Energy equals mass times the speed of light squared"

Math:     ∫₀^∞ e^(-x²) dx = √π/2
Natural:  "The integral from 0 to infinity of e raised to the power of negative
           x squared equals the square root of pi divided by 2"
           → ~14 words of natural language = 1 line of math notation
           → Math COMPRESSION: ~14 words → 1 line

→ This is why math notation EXISTS:
  EXTREME COMPRESSION for quantity + relation
  But ONLY for quantity + relation — cannot compress emotions, social content, narrative
```

### §8.3 — Open questions

1. **Why do children EVERYWHERE learn arithmetic early (~age 5-6)?** Is number sense a "pre-verbal substrate" like the pre-verbal chunks in F1? (Research: Dehaene 1997 "The Number Sense" — a dedicated brain region for numbers: the Intraparietal sulcus.)

2. **Algebra = the first time math ABSTRACTS OVER INSTANCES** (from "3+2" to "a+b"). Is this a PFC-dependent transition? (Prediction: algebra difficulty correlates with PFC maturation timeline.)

3. **Why are proofs FAR HARDER than calculating?** Because proof = GENERATIVE (must CREATE new arguments), calculate = SEQUENTIAL (chain known steps). Proof ≈ L3 Generative pattern, calculate ≈ L3 Sequential pattern.

4. **Math anxiety = at the speech-act compile level?** (Per Convergence Point 7 discussion) Math anxiety ≠ "the number 3 tagged as threat" → "the number 3 is context-reusable". Math anxiety = "the act of doing math in a social context" tagged as threat (like speech-act level). Prediction: math anxiety only appears when there is SOCIAL EXPOSURE (tests, being called to the board), not when solving problems alone.

5. **New symbol = new chunk compression (§7 history).** Does the H12 language evolution driver apply to math notation? "Mathematician feels the need for a new symbol → coins it → community adopts it." Analogous to the H12 word-coining mechanism?

6. **Chinese math advantage?** Chinese number words are shorter than English (一二三四五六七八九十 = all monosyllabic). Working memory for Chinese speakers holds MORE NUMBERS per slot. Evidence: Chinese children calculate faster (Miller & Stigler 1987). → Handle size matters!

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
> Reference document from exploration session N+5. Read at leisure — especially §5 (comparison) and §6 (how experts actually use math).
>
> ✅ English primary throughout
>
> Version: v1.0, 2026-04-16.
