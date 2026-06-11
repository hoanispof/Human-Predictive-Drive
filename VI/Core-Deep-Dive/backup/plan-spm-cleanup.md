# Plan: SPM → Self-Pattern-Modeling Cleanup

## STATUS: ✅✅ ALL COMPLETE (2026-05-23, 1 session)

## Mục tiêu
Thay thế TẤT CẢ viết tắt `SPM` → `Self-Pattern-Modeling` trong toàn bộ production files.
Tuân thủ convention: KHÔNG viết tắt concept. SPM collision với Statistical Parametric Mapping.

## Replacement Rules
1. `SPM` → `Self-Pattern-Modeling` (standalone, trong mọi context)
2. `SPM-owned` → `Self-Pattern-Modeling-owned` (giữ hyphenated)
3. `SPM-driven` → `Self-Pattern-Modeling-driven`
4. `pre-SPM` → `pre-Self-Pattern-Modeling`
5. `proto-SPM` → `proto-Self-Pattern-Modeling`
6. `SPMs` → `Self-Pattern-Modeling` (bỏ plural)
7. Tables: inline expand, chấp nhận lệch nhẹ cho complex tables

## RESULTS

| Phase | Scope | Replacements | Files |
|---|---|---|---|
| S1 | Agent-Mechanism/ folder | 723 | 12 |
| S2 | Observation/ folder | 483 | 13 |
| S3 | Body-Base root + Body-Feedback/ + Melody/ | 229 | 18 |
| S4 | PFC/ + Collective/ | 189 | 11 |
| S5 | Other Core-Deep-Dive + Outside (Education, etc.) | 96 | 21 |
| S6 | Research/ folder (ALL sub-folders) | 748 | 30 |
| **TOTAL** | | **2,468** | **105** |

## FINAL VERIFY
- Grep `\bSPM\b` across ALL production files = **0 remaining**
- 105 files with SPM = all in `backup/`, `_backup/`, `Drill-*`, or `plan-*` (frozen, skip)
- 2 meta-references fixed: "abbreviation SPM giữ nguyên" → updated text
- ASCII box tables: inline expand, cosmetic overflow accepted

## Convention Update
**PERMANENT**: KHÔNG viết tắt concept. Ngoại lệ DUY NHẤT: thuật ngữ học thuật mainstream (PFC, VTA, vmPFC, DRN) + labels (M1-M4, H1-H12).
**SPM REMOVED** from exception list — it was framework-created, NOT mainstream.
