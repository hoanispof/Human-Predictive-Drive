# Plan R — Resonance Decline M1-M4 (SUPERSEDED)

```
Status:    📁 SUPERSEDED → xem Plan-R-v2-Reframe.md
Created:   2026-05-29
Superseded: 2026-05-29 (same session — reframe analysis revealed
            4 mechanisms → 2 Forces + 1 Fuel + Gap Drift)
Reason:    M3+M4 merged (không phân biệt được trong quan sát).
           Novelty = fuel/calibration, không phải mechanism.
           Plan R rename-only → Plan R-v2 conceptual rewrite.
Giữ lại:   File inventory (§4) vẫn hữu ích cho Plan R-v2.
```

---

## §1 — Hệ M-Label: Resonance Decline

Bond-Architecture.md §4 (lines 601-702) define 4 mechanisms:

```
  M1: Compiled suppress gap riêng — PFC suppress own drives → mất nguồn
      by-products. ★ STRONGEST. Accelerator cho M2+M3+M4.
  M2: Habituation (Weber-Fechner) — Cùng stimulus → VTA giảm fire → reward
      giảm. Hardware tự nhiên. ĐỘC LẬP.
  M3: Prediction completion — Self-Pattern-Modeling quá accurate → delta=0
      → hết novelty. Gap vẫn CÓ nhưng không fill MỚI.
  M4: Entity-Compiled saturation — Formation 40→200h diminishing returns.
      Ít chunks MỚI về partner. Plateau.
```

---

## §2 — Tên Mới

```
  ┌──────────┬─────────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới                 │ Dùng khi                         │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M1       │ Compiled-Suppress       │ Standalone / full context         │
  │ M2       │ Habituation             │ Standalone / full context         │
  │ M3       │ Prediction-Completion   │ Standalone / full context         │
  │ M4       │ Entity-Saturation       │ Standalone / full context         │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ Short    │ Suppress / Habituation  │ Trong formulas, tables khi       │
  │ forms    │ / Completion /          │ context ĐÃ RÕ                    │
  │          │ Saturation              │                                  │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ Grouped  │ 4 Decline mechanisms    │ Thay "M1-M4"                     │
  │          │ 4 Resonance-Decline     │ Thay "M1-M4 Resonance Decline"   │
  │          │ mechanisms              │                                  │
  └──────────┴─────────────────────────┴──────────────────────────────────┘

  ⭐ CAPITALIZED + HYPHENATED (concept names).
  ⭐ KHÔNG viết tắt thành CS/H/PC/ES.
```

---

## §3 — Replace Rules (per SAFE file)

### THỨ TỰ BẮT BUỘC:

```
  PHASE A — GROUPED LABELS (trước standalone):
    Pass 1:  "M1-M4"             → "4 Decline mechanisms" (context-specific)
    Pass 2:  "M1+M2+M3+M4"      → "Compiled-Suppress+Habituation+
                                     Prediction-Completion+Entity-Saturation"
    Pass 2b: "M2+M3+M4" / "M2-M4" → "Habituation+Prediction-Completion+
                                       Entity-Saturation"

  PHASE B — LABELED PATTERNS (tránh redundancy):
    Pass 3-4:  "M1 compiled suppress" / "M1 Compiled suppress"
               → "Compiled-Suppress"
    Pass 5-6:  "M2 habituation" / "M2 Habituation"
               → "Habituation"
    Pass 7-8:  "M3 prediction completion" / "M3 Prediction completion"
               → "Prediction-Completion"
    Pass 9-9b: "M4 Entity-Compiled saturation" / "M4 Entity-Saturation"
               / "M4 entity-compiled saturation"
               → "Entity-Saturation"

  PHASE C — STANDALONE (catch remaining):
    Pass 10: "M1" → "Compiled-Suppress"
    Pass 11: "M2" → "Habituation"
    Pass 12: "M3" → "Prediction-Completion"
    Pass 13: "M4" → "Entity-Saturation"

  ⚠️ Phase C chỉ SAU Plans L/E/F hoàn thành.
     Khi đó mọi M-labels không phải Decline đã được xóa/renamed.
```

### Compound patterns:

```
  "M1 ACCELERATE M2+M3+M4"
  → "Compiled-Suppress ACCELERATE Habituation+Prediction-Completion+Entity-Saturation"

  "M1 NHÂN M2+M3+M4"
  → "Compiled-Suppress NHÂN Habituation+Prediction-Completion+Entity-Saturation"

  "Fix M1" / "counter M1"
  → "Fix Compiled-Suppress" / "counter Compiled-Suppress"

  "M1 + M2"
  → "Compiled-Suppress + Habituation"

  "§4 — M1-M4"
  → "§4 — 4 RESONANCE-DECLINE MECHANISMS"

  "which M1-M4 attack?"
  → "which Decline mechanisms attack?"
```

---

## §4 — File Inventory

### Chi tiết: xem plan-m1-m4-rename.md §3.2 (NHÓM A: RENAME)

```
  ── S1: Source + Agent-Mechanism (7 file, ~138 occ) ──
  Bond-Architecture.md              ~42  SOURCE DEFINITION
  By-Product-Gap-Resonance.md       ~43
  Agent-Mechanism.md                ~21
  Resonance-Sustainability.md       ~18
  Self-Pattern-Modeling.md          ~8
  By-Product-Scale.md               ~5
  Entity-Access.md                  ~1
  (Entity-Access-Calibration.md     ~2   verify)

  ── S2: Observation (5 file, ~140 occ) ──
  Boredom.md                        ~50  HEAVY
  Connection.md                     ~42  HEAVY
  Empathy.md                        ~28
  Status.md                         ~12
  Protect.md                        ~8

  ── S3: Body-Base + Core (~12 file, ~61 occ) ──
  Body-Coupling.md                  ~22
  Core-Software.md                  ~16
  Inter-Body-Mechanism.md           ~5
  Background-Pattern.md             ~4
  Chunk.md                          ~3
  Valence-Propagation.md            ~3
  Gap-Distribution-Profile.md       ~2
  Gap-Body-Need.md                  ~1
  Core-Hardware.md                  ~1
  Neural-Processing-Flow.md         ~1
  00-Parameter-Overview.md          ~1   verify
  (Collective-Body.md              ~2)
  (Coordination-Node.md            ~2)

  ── S4: Love + Index + Misc (~7 file, ~82 occ) ──
  Love-Unified.md                   ~30  ⚠️ MIXED (§5 handled by Plan L → safe)
  Love-Romantic.md                  ~29
  01-File-Index.md (CDD)            ~9
  Drill-Emergent-Pattern.md         ~3
  01-File-Index.md (Research)       ~2
  00-Glossary.md                    ~1   verify
  plan-tech-post.md                 ~1

  ── S5: Education-System (6 file, ~29 occ) ──
  Education-System.md               ~20
  Hardware-Calibration.md           ~3
  Curriculum-Framework.md           ~2
  00_Overview.md                    ~1
  VN-Recommendations.md            ~2
  VN-Education-Status.md           ~1

  ── S6: Education-Mech + Child-Dev (9 file, ~98 occ) ──
  Connection-Education.md           ~30  HEAVY
  Education-Mechanism.md            ~18
  Education-Arms-Race.md            ~13
  Domain-Knowledge-Map.md           ~9
  Expansion-Saturation-Crisis.md    ~2
  Money-Education.md                ~1
  Skill-Introduction.md             ~9
  Natural-Development.md            ~8
  Child-Development-Mechanism.md    ~8

  ── S7: Melody-Technology (3 file, ~33 occ) ──
  Religion.md                       ~17
  Idol-Phenomenon.md                ~10
  Melody-Technology-Overview.md     ~6
```

### Files MIXED (đã handled by earlier plans):

```
  Love-Unified.md: §5 Quality xong (Plan L) → §6.2+ = pure Decline → safe
  Resonance-Per-Entity.md: §3-§9 Profile xong (Plan E) → §14+ = pure Decline → safe
  Body-Base.md: §5.3 Firing xong (Plan F) → dep-list decline refs → safe
  Discovery-vs-Expansion.md: Firing xong (Plan F) → dep-list decline refs → safe
  Domain-Mapping-Drive.md: Firing xong (Plan F) → dep-list decline refs → safe
```

---

## §5 — Session Plan

```
  ┌─────┬──────────────────────────────────┬───────┬───────┐
  │ Ses │ Cluster                          │ Files │ ~Occ  │
  ├─────┼──────────────────────────────────┼───────┼───────┤
  │ R1  │ Source + Agent-Mechanism          │   7   │ ~138  │
  │ R2  │ Observation                      │   5   │ ~140  │
  │ R3  │ Body-Base + Core                 │  ~12  │  ~61  │
  │ R4  │ Love + Index + Misc              │   7   │  ~82  │
  │ R5  │ Education-System                 │   6   │  ~29  │
  │ R6  │ Education-Mech + Child-Dev       │   9   │  ~98  │
  │ R7  │ Melody-Technology                │   3   │  ~33  │
  ├─────┼──────────────────────────────────┼───────┼───────┤
  │     │ TOTAL                            │ ~49   │ ~581  │
  └─────┴──────────────────────────────────┴───────┴───────┘

  THỨ TỰ: R1 (source definition) trước → consumers R2-R7.
  Có thể gộp sessions nhỏ: R5+R7, hoặc R3+R4 nếu scope vừa.
```

---

## §6 — An Toàn

```
  ① TRƯỚC mỗi file: Read full context, xác nhận = pure Decline.
  ② Phase C (standalone M1→...) chỉ chạy khi:
     - File 100% pure Decline, HOẶC
     - Plans L/E/F đã xử lý hết M-labels khác
  ③ Files có dạng "M1." (dấu chấm) → có thể Entity Profile sót → check.
  ④ Sau mỗi file: grep "\bM[1-4]\b" = 0 (hoặc only false-positive SKIP).
  ⑤ KHÔNG replace_all "M1" toàn repo — chỉ per SAFE file.
  ⑥ Files SKIP (§3.3 plan-m1-m4-rename.md): TUYỆT ĐỐI KHÔNG ĐỘNG.
```

---

## §7 — Verify (Final)

```
  Sau TẤT CẢ 4 plans (L+E+F+R) hoàn thành:

  grep "\bM[1-4]\b" toàn Human-Predictive-Drive (exclude backup/_backup/VI/)
  → Remaining = CHỈ CÒN files SKIP:
     - Anchor-Schema-Example.md (Micro ⑥)
     - Quote-Analysis/ (Meta-insight)
     - Drill-Body-Feedback/ (PFC Damage ⑤)
     - Motor Arc codes
     - plan files (tham khảo)

  → Nếu phát hiện M-label ngoài SKIP list → BUG → investigate.
```
