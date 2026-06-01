# Plan 3/3: Compile Architecture Refine — Education-System/

> **Created:** 2026-06-01
> **Trigger:** Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0 → reframes chưa lan tới Education-System
> **Scope:** 8 files trong Education-System/ → refine (chủ yếu cross-ref + terminology)
> **Depends:** ⚠️ Plan 1 (Child-Dev/) + Plan 2 (Education-Mechanism/) PHẢI hoàn thành trước
> **Approach:** Rà soát + refine. APPLICATION LAYER → changes nhẹ hơn Plan 1-2.

---

## Context: Tại sao Plan 3 đứng sau Plan 1+2

```
Education-System/ = TẦNG 4 APPLICATION LAYER:
  → Reference Child-Dev-Mechanism.md (Tier 1) → phải xong Plan 1
  → Reference Education-Mechanism.md (Tier 3) → phải xong Plan 2
  → Application files KHÔNG define mechanism — chỉ ÁP DỤNG

Khi Plan 1+2 xong:
  → Mechanism files đã reframe → "Compile Architecture (1E+3M)"
  → Plan 3 update references + add compile type awareness per stage
```

---

## File 1: Education-System.md v3.0 → v3.1 ★★★

**Current:** 1,627L | **Target:** ~1,710L (+83L)

```
FRONTMATTER:
  + dependencies: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Child-Dev-Mechanism.md → v2.2, Education-Mechanism.md → v2.1

§1 (ADD ~30L): Compile Architecture awareness
  → Education = guided compile optimization
  → 1 Engine + 3 Modulators → education DESIGN modulators, KHÔNG thay engine
  → Trust Compile = primary education pathway → cần design transition to Experience
  → Cross-ref: Compile-Taxonomy.md v3.0 §4

§2 (ADD ~20L per stage): Per-Stage Compile Type awareness
  Trong mô tả per-stage, thêm note:
  → Stage 2 (6-12): Trust Compile dominant (teacher install)
    + Experience verify (practice, projects)
  → Stage 3 (12-18): Trust → Experience transition critical
    + Expertise Compile seeds (depth domains)
  → Stage 4 (18+): Expertise Compile dominant
    + Trust Compile for new domains

§7 (ADD ~30L): Teacher Role × Critical Asymmetry
  → Teacher Entity-Valence path > Teacher PFC instruction path
  → = "Thầy/cô mà học sinh TIN = value compile approach"
  → = "Thầy/cô giải thích hay = content compile OK, value có thể neutral"
  → = Entity-Access Mức 3-4 + Critical Asymmetry = most effective teaching
  → Cross-ref: Compile-Taxonomy.md v3.0 §7

CROSS-REFERENCES:
  "§2 4+1 Compile" → "§2 Compile Architecture"
  + Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0

BACKUP: v3.0 → backup/
```

---

## File 2: Curriculum-Framework.md v2.1 → v2.2 ★★★

**Current:** 990L | **Target:** ~1,032L (+42L)

```
§2 (ADD ~20L): Foundation Delivery × Compile Type
  Per-domain compile type notes:
  → Literacy: Trust Compile dominant + Experience verify
  → Numeracy: DANGER — Trust avoidance tag phổ biến → need Experience first
  → Somatic: Experience ~99%
  → Social: Trust 30% + Experience 70%
  → Creative: Experience dominant — Trust Compile can KILL
  → Meta-learning: Trust for strategies + Experience for self-observation

§4 (ADD ~20L): Sequencing × Multi-Stream
  → Per-stage: VALUE stream positive BEFORE content volume increases
  → Stage 2: VALUE stream priority
  → Stage 3: CONTENT volume can increase IF value stream approach
  → = Sequencing = VALUE stream first, CONTENT stream second

CROSS-REFERENCES:
  "§2 4+1 compile" → "§2 Compile Architecture"
  + Compile-Taxonomy.md v3.0

BACKUP: v2.1 → backup/
```

---

## File 3: 00_Overview.md v2.1 → v2.2 ★★

**Current:** 380L | **Target:** ~395L (+15L)

```
CROSS-REF UPDATE:
  "Child-Development-Mechanism.md v2.0 — khung nguyên lý (4+1 compile,
    approach/avoidance, cortisol, sensitive periods)"
  → "Child-Development-Mechanism.md v2.2 — khung nguyên lý
    (Compile Architecture 1E+3M, approach/avoidance, cortisol, sensitive periods)"

  + Compile-Taxonomy.md v3.0 vào dependency section
  + Compile-Sleep.md v1.0 vào dependency section
```

---

## File 4: Era-Analysis-2025.md v2.1 — cross-ref update ★

**Current:** 815L | **Target:** ~820L (+5L)

```
TERMINOLOGY:
  "Child-Dev-Mechanism v2.0 §2 — 4+1 kênh compile, 5-parameter formula"
  → "Child-Dev-Mechanism v2.2 §2 — Compile Architecture, 5-parameter formula"

  "Chunk compilation: vẫn cần repetition, emotion, multi-modal, sleep"
  → GIỮ NGUYÊN (đây là practical list, không phải architecture label)

CROSS-REFERENCES: + CT v3.0
```

---

## File 5: Hardware-Calibration.md v1.1 — cross-ref update ★

**Current:** 1,689L | **Target:** ~1,695L (+6L)

```
CROSS-REFERENCES:
  "§2 4+1 Compile" → "§2 Compile Architecture"
  + Compile-Taxonomy.md v3.0
  Update: Child-Dev-Mechanism.md v2.1 → v2.2
```

---

## File 6: VN-Education-Status.md v2.1 — cross-ref update ★

**Current:** 1,532L | **Target:** ~1,535L (+3L)

```
CROSS-REFERENCES:
  "Child-Development-Mechanism.md v2.0 — 4+1 compile, approach/avoidance"
  → "Child-Development-Mechanism.md v2.2 — Compile Architecture, approach/avoidance"
```

---

## File 7: VN-Recommendations.md v2.1 — cross-ref update ★

**Current:** 878L | **Target:** ~881L (+3L)

```
CROSS-REFERENCES:
  "Child-Development-Mechanism.md v2.1 — 4+1 compile, approach/avoidance"
  → "Child-Development-Mechanism.md v2.2 — Compile Architecture, approach/avoidance"
```

---

## File 8: VN-Cultural-Factors.md v2.1 — verify ★

**Current:** 1,225L | **Action:** Verify, likely zero changes

```
VERIFY:
  □ Check for any "4+1" references
  □ Check cross-refs point to correct versions
  □ Likely NO changes needed (cultural file, minimal mechanism refs)
```

---

## Thứ tự thực hiện

```
┌─────┬──────────────────────────────┬──────────┬──────────┐
│ #   │ File                         │ Lines +  │ Priority │
├─────┼──────────────────────────────┼──────────┼──────────┤
│  1  │ Education-System v3.1        │  +83L    │ ★★★     │
│  2  │ Curriculum-Framework v2.2    │  +42L    │ ★★★     │
│  3  │ 00_Overview v2.2             │  +15L    │ ★★      │
│  4  │ Era-Analysis-2025            │   +5L    │ ★       │
│  5  │ Hardware-Calibration         │   +6L    │ ★       │
│  6  │ VN-Education-Status          │   +3L    │ ★       │
│  7  │ VN-Recommendations          │   +3L    │ ★       │
│  8  │ VN-Cultural-Factors          │   ~0L    │ ★       │
├─────┼──────────────────────────────┼──────────┼──────────┤
│     │ TOTAL                        │ ~157L    │          │
└─────┴──────────────────────────────┴──────────┴──────────┘

File 1-2: content refine (1 session)
File 3-8: cross-ref batch (gộp cùng session File 1-2)
→ Plan 3 likely = 1 session total
```

---

## Tổng kết 3 Plans

```
┌─────────┬─────────────────┬──────────┬──────────┬──────────────────┐
│ Plan    │ Folder          │ Files    │ Lines +  │ Sessions ước     │
├─────────┼─────────────────┼──────────┼──────────┼──────────────────┤
│ Plan 1  │ Child-Dev/      │ 4 files  │ +540L    │ 2-3 sessions     │
│ Plan 2  │ Ed-Mechanism/   │ 7 files  │ +366L    │ 2-3 sessions     │
│ Plan 3  │ Ed-System/      │ 8 files  │ +157L    │ 1 session        │
├─────────┼─────────────────┼──────────┼──────────┼──────────────────┤
│ TOTAL   │ 3 folders       │ 19 files │ +1,063L  │ 5-7 sessions     │
└─────────┴─────────────────┴──────────┴──────────┴──────────────────┘

Dependency: Plan 1 → Plan 2 → Plan 3 (sequential, NOT parallel)
Mỗi plan compact session → bắt đầu plan tiếp với context sạch
```
