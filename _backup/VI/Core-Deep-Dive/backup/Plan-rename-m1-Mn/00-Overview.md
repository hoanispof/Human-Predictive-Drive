# Plan-rename-m1-Mn — Tổng Quan

```
Status:    ✅✅ ALL DONE + FINAL VERIFY CLOSED (2026-05-29)
Scope:     7 hệ M-label → 4 plans rename (R/E/F/L) + 3 SKIP
Thứ tự:    L → E → F → R (ALL COMPLETE)
Gốc:       plan-m1-m4-rename.md (audit 2026-05-29) → tách thành 4 sub-plans
```

---

## §1 — 7 Hệ M-Label Trong Framework

```
┌─────┬──────────────────────────────────┬────────┬───────┬───────┬──────────┐
│  #  │ Hệ                              │ Labels │ Files │ ~Occ  │ Plan     │
├─────┼──────────────────────────────────┼────────┼───────┼───────┼──────────┤
│  ①  │ Resonance Decline                │ M1-M4  │ ~46   │ ~545  │ R (main) │
│  ②  │ Entity Profile Parameters        │ M1-M5  │ 1-2   │  ~80  │ E        │
│  ③  │ Firing: Tonic/Phasic/Comp/Casc   │ M1-M4  │ 2-3   │  ~20  │ F        │
│  ④  │ Firing: Structural/Shift/Peak/C  │ M1-M4  │   1   │  ~10  │ F (gộp)  │
│  ⑤  │ PFC Damage                       │ M1-M2  │   4   │  ~17  │ SKIP     │
│  ⑥  │ Micro Example Codes              │ M1-M5  │   1   │  ~11  │ SKIP     │
│  ⑦  │ Love Quality Dimensions          │ M1-M4  │   1   │   ~6  │ L        │
│  -  │ Motor Arc (V/A/M/B/I) + Quote    │ varies │  ~8   │  ~37  │ SKIP     │
└─────┴──────────────────────────────────┴────────┴───────┴───────┴──────────┘
```

---

## §2 — 4 Plans

```
Plan-L-Love-Quality.md       ⑦  1 file, ~6 occ     Nhỏ nhất. "Khởi động nhẹ."
Plan-E-Entity-Profile.md     ②  1-2 files, ~80 occ  Manual từng dòng. Kỹ năng phân biệt.
Plan-F-Firing-Modes.md       ③④ 3-4 files, ~30 occ  Conceptual + fix cross-refs SAI.
Plan-R-v2-Reframe.md         ①  ~46 files, ~545 occ  ★ REFRAME (not just rename).
  (SUPERSEDES Plan-R-Resonance-Decline.md)             4 mechanisms → 2 Forces + 1 Fuel.
                                                       M3+M4 merged → novelty threshold.
```

---

## §3 — Thứ Tự: L → E → F → R

### Tại sao thứ tự này?

Mỗi plan xoá M-labels của hệ mình → khi Plan R chạy, mọi M-label
còn lại trong repo = Resonance Decline → an toàn Phase C (standalone replace).

### Files MIXED (có >1 hệ M-label):

```
Love-Unified.md:
  §5 Quality Dims (Plan L) + §6.2 Decline (Plan R)
  → L chạy trước → xoá §5 → R chạy §6.2 an toàn

Resonance-Per-Entity.md:
  §3-§9 Entity Profile M1-M5 (Plan E) + §14+D3 Decline M1-M4 (Plan R)
  → E chạy trước → xoá Profile → R chạy Decline an toàn

Body-Base.md:
  §5.3 Firing Modes (Plan F) + dep-list Decline cross-refs (Plan R)
  → F chạy trước → xoá firing → R chạy decline refs an toàn

Discovery-vs-Expansion.md:
  Firing Modes all (Plan F) + dep-list Decline cross-refs (Plan R)
  → F chạy trước

Domain-Mapping-Drive.md:
  Firing Modes (Plan F) + dep-list Decline cross-refs (Plan R)
  → F chạy trước
```

### Workflow mỗi plan:

```
  1. Compact session (cold start)
  2. Đọc plan file → nắm scope + rules
  3. Thực hiện rename
  4. Verify (grep)
  5. Cập nhật status trong plan → ✅ DONE
```

---

## §4 — SKIP (Không Rename)

```
⑤ PFC Damage (M1 recovery / M2 wear):
  → Context riêng (Drill-Body-Feedback 01-04). Scope khác.

⑥ Micro Examples (M=Micro scale codes: M1-M5 / S1-S5 / D1-D5 / L1-L5 / X1-X5):
  → Naming convention phổ M→S→D→L→X. Rename sẽ phá convention.

Motor Arc (V1/A1/M1/B1/I1):
  → Modality code convention (Visual/Auditory/Motor/Body/Interoception).

Quote-Analysis (M1-M4 Meta-insights):
  → Local enumeration trong từng file. Không cross-file.

Lý do chung: Mỗi hệ dùng M-label hợp lệ trong context riêng,
KHÔNG gây nhầm lẫn với hệ khác khi đọc. Rename phá hỏng mà không có lợi.
```

---

## §5 — Relationship To plan-m1-m4-rename.md

```
plan-m1-m4-rename.md (Core-Deep-Dive/) = plan TỔNG HỢP ban đầu.
  - Created 2026-05-23, audited 2026-05-29
  - Phát hiện 6 hệ M-label (thiếu hệ ⑦ Love Quality)
  - File inventory chi tiết cho Resonance Decline

4 sub-plans trong folder này = AUTHORITATIVE (thay thế plan cũ).
plan-m1-m4-rename.md giữ làm THAM KHẢO (audit log, collision analysis).
```
