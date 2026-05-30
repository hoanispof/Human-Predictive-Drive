# Plan: NT-Label Rename — NT1-NT7 → Descriptive Names

```
Status:    ⛔ SUPERSEDED → plan-chunk-refine/plan-A-nt-label-rename.md
Created:   2026-05-30
Scope:     ~50 active files, ~395 occurrences (67 files incl. backup)
Approach:  Phase S1 cross-file NTs → S2 local NTs → S3 verify
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\bNT[1-7]\b" = 0 trong active non-whitelist files
Related:   H11 (= NT5, 556 occ) + H12 (145 occ) — CHUNG plan hoặc RIÊNG
Old plan:  Core-Deep-Dive/backup/plan_rename-abbreviation/plan-nt-label-rename.md
```

---

## §0 — TẠI SAO ĐỔI TÊN

```
  VẤN ĐỀ 1: "NT" GÂY NHẦM VỚI "NEUROTRANSMITTER"
    → NT = "New Thesis" (thesis mới từ Chunk drill)
    → Neuroscience: "NT" = viết tắt chuẩn cho "neurotransmitter"
    → NT7 liên quan cortisol → người đọc tưởng "Neurotransmitter 7 = cortisol"
    → Sai: cortisol là HORMONE, không phải neurotransmitter
    → Gây hiểu nhầm nghiêm trọng cho reader mới + expert audience

  VẤN ĐỀ 2: NT LABELS VÔ NGHĨA CHO READER MỚI
    → "NT7" — ai biết thesis gì?
    → Phải tra 99-Master-Synthesis.md hoặc Chunk.md
    → "Direction-At-Compile" — tự giải thích ngay

  VẤN ĐỀ 3: NT LÀ PROVENANCE MARKERS, KHÔNG PHẢI CONCEPT NAMES
    → NT labels gốc từ Chunk drill (99-Master-Synthesis.md)
    → Đã lan ra ~50 active files → thành concept names de facto
    → Giống H10 trước khi đổi thành Body-Feedback-Precondition

  VẤN ĐỀ 4: VI PHẠM FRAMEWORK RULE
    → "KHÔNG viết tắt concept" — rule bắt buộc
    → NT1-NT7 = viết tắt concept → phải đổi
```

---

## §1 — BẢNG ĐỊNH NGHĨA NT1-NT7

```
  Source: 99-Master-Synthesis.md (definition file)

  ┌──────┬────────────┬───────────────────────────┬──────────────────────────────────────┐
  │ #    │ Confidence │ Tên mới (đề xuất)         │ Nghĩa                                │
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT1  │ 🟢         │ Compile-Gradient          │ Compilation is gradient, not         │
  │      │            │                           │ discrete. Proto-chunks = weak chunks │
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT2  │ 🟡🟢       │ Compile-4-Channel         │ 4-channel × 5-parameter rate         │
  │      │            │                           │ formula for compilation               │
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT3  │ 🟡         │ Emergent-Binding          │ Multi-modal binding = 4 concurrent   │
  │      │            │                           │ mechanisms. No single binder module   │
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT4  │ 🟢         │ PFC-From-Birth            │ PFC hardware online from prenatal.   │
  │      │            │                           │ Developmental behavior = chunks-     │
  │      │            │                           │ missing, NOT hardware-missing          │
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT5  │ 🟡         │ Receptive-Productive-Gap  │ = H11. Productive bundle ≈ 3×        │
  │      │            │                           │ receptive. Rename cùng H11            │
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT6  │ 🟡         │ Label-As-Handle           │ Verbal labels = retrieval path +     │
  │      │            │                           │ symbolic compression. NOT 5th modality│
  ├──────┼────────────┼───────────────────────────┼──────────────────────────────────────┤
  │ NT7  │ 🟡🟢       │ Direction-At-Compile      │ Body-state DIRECTION (novelty vs     │
  │      │            │                           │ threat) determines chunk association  │
  │      │            │                           │ tag at compile time                    │
  └──────┴────────────┴───────────────────────────┴──────────────────────────────────────┘

  ⚠️ Tên mới từ plan cũ (2026-05-23). CẦN REVIEW lại trước khi thực hiện:
    → Tên có tự giải thích đủ không?
    → Có collision với concept names hiện tại không?
    → Có quá dài không?
```

---

## §2 — SCOPE PHÂN TÍCH

```
  TỔNG: 67 files, ~395 occurrences
  ACTIVE (non-backup): ~50 files
  BACKUP: ~17 files (SKIP — không edit)

  PHÂN BỔ THEO NT:
    NT7: nhiều nhất cross-file (Cortisol-Baseline 19 occ, Protect, Quote-Analysis, Logic-Planning)
    NT4: Core-Hardware, Core-Software (cross-file)
    NT6: Modality, Feeling files (cross-file)
    NT1-NT3: chủ yếu trong Chunk/ ecosystem (local)
    NT5: = H11 (cross với Chunk/ và Child-Dev files)

  TOP FILES BY COUNT:
    99-Master-Synthesis.md    — 49 occ (DEFINITION FILE)
    Chunk.md                  — 28 occ
    Cortisol-Baseline.md      — 19 occ
    01b-Chunk-Activation.md   — 17 occ
    Feeling-Literacy-Draft.md — 14 occ
    Feeling-Mech-Deep-Draft.md — 11 occ
    01c-Chunk-Discovery.md    — 10 occ
    10-F1-Synthesis EN+VI     — 9+11 occ
    03-Chain-Anchor-Decay.md  — 9 occ
```

---

## §3 — QUYẾT ĐỊNH CẦN TRƯỚC KHI THỰC HIỆN

```
  ❓ Q1: DRILL FILES — KEEP hay RENAME?
    Tiền lệ H10: Drill-Body-Feedback/ (4 files) GIỮA H10 + forward pointer
    NT case KHÁC: ~30 drill files dùng NT labels NHIÈU (hàng trăm occ)
    → Option A: KEEP NT in drill files + forward pointer (như H10)
    → Option B: RENAME TẤT CẢ kể cả drill files
    → Option C: RENAME cross-file + KEEP local Chunk-Internal/External drill files
    → ⚠️ Option A/C = ~20 files rename, Option B = ~50 files rename

  ❓ Q2: 99-MASTER-SYNTHESIS.MD — vai trò gì?
    → File này là DEFINITION file cho toàn bộ H1-H12, NT1-NT7
    → Nếu Option A: thêm mapping table NT→new name, giữ NT labels
    → Nếu Option B: rename all NT→new names, giữ lại "formerly NT7" notes

  ❓ Q3: H11 + H12 — CHUNG PLAN hay RIÊNG?
    → H11 = NT5 (Receptive-Productive-Gap): 556 occ, 38 files
    → H12: 145 occ, 24 files (chủ yếu Chunk-Internal drill)
    → Option: Include H11+H12 in this plan (comprehensive)
    → Option: NT chỉ, H11+H12 plan riêng
    → ⚠️ Nếu chung: total ~1,100 occ, ~70+ files

  ❓ Q4: plan-abbreviation-backlog.md — CẬP NHẬT
    → Hiện tại liệt kê "NT7" là "Label hệ thống" (acceptable)
    → Nếu rename → xóa NT7 khỏi exception list
    → Cũng xóa luôn nếu rename toàn bộ NT1-NT7

  ❓ Q5: TÊN MỚI — REVIEW LẠI
    → Plan cũ đề xuất 7 tên (§1 ở trên)
    → Cần verify: có collision với concept names hiện tại không?
    → Cần verify: tên có đủ rõ ràng cho reader mới không?
    → Đặc biệt: "Compile-4-Channel" vs "Compile-Rate-Formula"?
```

---

## §4 — PHASES (dự kiến, tùy Q1-Q5)

```
  PHASE S1: CROSS-FILE NTs (high priority)
    → NT7 (Direction-At-Compile): ~6 files ngoài Chunk/
    → NT4 (PFC-From-Birth): ~2 files ngoài Chunk/
    → NT6 (Label-As-Handle): ~4 files ngoài Chunk/
    → ~12 files, ~50 occ
    → 1 session

  PHASE S2: LOCAL NTs (Chunk/ ecosystem)
    → NT1, NT2, NT3 in Chunk.md + Chunk-Internal + Chunk-External
    → NT5 = H11 (nếu include, thêm ~556 occ)
    → ~20-30 files, ~200-300 occ
    → 2-3 sessions (tùy Option A/B/C)

  PHASE S3: DEFINITION FILES + CROSS-REFS
    → 99-Master-Synthesis.md: mapping table hoặc full rename
    → 01-File-Index.md: update descriptions
    → plan-abbreviation-backlog.md: remove NT exceptions
    → 1 session

  PHASE S4: VERIFICATION SWEEP
    → grep "\bNT[1-7]\b" = 0 in active non-whitelist files
    → Spot-check 10+ files
    → Redundancy check (e.g., "Direction-At-Compile direction")
    → 1 session

  TỔNG: ~4-6 sessions (tùy scope Q1-Q5)
```

---

## §5 — RISK + COLLISION CHECK

```
  ⚠️ COLLISION RISK:
    → "\bNT[1-7]\b" — word boundary → SAFE, ít collision
    → "NT" inside words? Unlikely ("NTrk" etc. not in framework)
    → NT5 = H11: rename cả hai cùng lúc tránh inconsistency

  ⚠️ REDUNDANCY RISK:
    → "NT7 direction tag" → "Direction-At-Compile direction tag" (redundant)
    → CẦN review context sau mỗi replace, bỏ phần mô tả thừa

  ⚠️ NEW NAME COLLISION:
    → "Compile-Gradient" — có file nào tên tương tự?
    → "PFC-From-Birth" — có trùng PFC-Development.md concept?
    → CẦN grep new names trước khi bắt đầu

  ⚠️ SO SÁNH VỚI H10 RENAME:
    → H10: ~92 files, ~900 edits → 3 sessions rename + 2 sessions audit
    → NT1-7: ~50 files, ~395 occ (nhỏ hơn H10)
    → Nếu include H11+H12: ~70 files, ~1,100 occ (lớn hơn H10)
```

---

## §6 — LIÊN QUAN

```
  ✅ DONE: H10 → Body-Feedback-Precondition (CLOSED 2026-05-30)
  🔲 PENDING: H11 → Receptive-Productive-Gap (556 occ, 38 files)
  🔲 PENDING: H12 → ? (145 occ, 24 files, chưa có tên mới)
  🔲 PENDING: Generic Label Audit Plans 4-10 (~7,600+ occ)
  📋 Old plans: Core-Deep-Dive/backup/plan_rename-abbreviation/
     → plan-nt-label-rename.md (source for §1 names)
     → plan-h-label-rename.md (H10 done, H11+H12 pending)
```
