# Plan A: NT-Label Rename — NT1-NT7 → Descriptive Names

```
Status:      ✅ COMPLETE (2026-05-30, all 4 phases done in 1 session)
Created:     2026-05-30
Supersedes:  plan-nt-label-rename.md (root level, session trước)
Scope:       Track A — RENAME ONLY (không tạo file mới)
Depends:     KHÔNG. Chạy ĐỘC LẬP.
Verify:      grep "\bNT[1-7]\b" = 0 trong active non-whitelist files
Related:     plan-B-drill-to-framework.md (Track B, chạy SAU hoặc song song)
```

---

## §0 — TẠI SAO ĐỔI TÊN

```
  VẤN ĐỀ 1: "NT" GÂY NHẦM VỚI "NEUROTRANSMITTER"
    → NT = "Nút Thắt" / "New Thesis" (verdict từ Chunk drill)
    → Neuroscience: "NT" = viết tắt chuẩn cho "neurotransmitter"
    → NT7 liên quan cortisol → reader tưởng "Neurotransmitter 7 = cortisol"
    → Cortisol là HORMONE, không phải neurotransmitter → gây hiểu nhầm

  VẤN ĐỀ 2: NT LABELS VÔ NGHĨA CHO READER MỚI
    → "NT7" — ai biết thesis gì? Phải tra 99-Master-Synthesis.md
    → "Direction-At-Compile" — tự giải thích ngay

  VẤN ĐỀ 3: NT LÀ PROVENANCE MARKERS, KHÔNG PHẢI CONCEPT NAMES
    → NT gốc từ Chunk drill (99-Master-Synthesis.md)
    → Đã lan ra ~49 active files → thành concept names de facto
    → Nhưng Chunk.md v2.3 ĐÃ INTEGRATE tất cả concepts thành sections
    → NT labels giờ chỉ là alias thừa

  VẤN ĐỀ 4: VI PHẠM FRAMEWORK RULE
    → "KHÔNG viết tắt concept" — rule bắt buộc
    → NT1-NT7 = viết tắt concept → phải đổi
```

---

## §1 — PHÁT HIỆN QUAN TRỌNG: CHUNK.MD V2.3 ĐÃ COVER TẤT CẢ

```
  Session rà soát 2026-05-30 phát hiện:
    → Chunk.md v2.3 (1,665L, 14 sections) ĐÃ integrate toàn bộ NT concepts
    → Không cần tạo file mới trong Chunk/ cho rename
    → Cross-file references NÊN trỏ về Chunk.md §X thay vì dùng NT labels

  MAPPING NT → CHUNK.MD SECTIONS:
    NT1 (Compile-Gradient)       → Chunk.md §1.1 + §2
    NT2 (Compile-4-Channel)      → Chunk.md §2.1 + §2.2
    NT3 (Emergent-Binding)       → Chunk.md §1.2
    NT4 (PFC-From-Birth)         → Chunk.md §8.2 + PFC-Development.md
    NT5 (Receptive-Productive)   → Chunk.md §11.3 (= H11, scope riêng)
    NT6 (Label-As-Handle)        → Chunk.md §6
    NT7 (Direction-At-Compile)   → Chunk.md §2.4
```

---

## §2 — BẢNG TÊN MỚI (CONFIRMED)

```
  ┌──────┬────────────┬───────────────────────────┬────────────────────────┐
  │ #    │ Confidence │ Tên mới                   │ Chunk.md Section       │
  ├──────┼────────────┼───────────────────────────┼────────────────────────┤
  │ NT1  │ 🟢         │ Compile-Gradient          │ §1.1 + §2              │
  │ NT2  │ 🟡🟢       │ Compile-Rate-Formula      │ §2.1 + §2.2            │
  │ NT3  │ 🟡         │ Emergent-Binding          │ §1.2                   │
  │ NT4  │ 🟢         │ PFC-From-Prenatal         │ §8.2                   │
  │ NT5  │ 🟡         │ Receptive-Productive-Gap  │ §11.3 (= H11)         │
  │ NT6  │ 🟡         │ Label-As-Handle           │ §6                     │
  │ NT7  │ 🟡🟢       │ Direction-At-Compile      │ §2.4                   │
  └──────┴────────────┴───────────────────────────┴────────────────────────┘

  COLLISION CHECK: ✅ 0 COLLISION (verified 2026-05-30)
    → Tất cả 7 tên chỉ xuất hiện trong plan/backup files

  TÊN ĐÃ CHỐT (2026-05-30):
    → NT2: "Compile-Rate-Formula" ✅ (bao quát hơn "Compile-4-Channel")
    → NT4: "PFC-From-Prenatal" ✅ (chính xác hơn "PFC-From-Birth")
```

---

## §3 — SCOPE CHÍNH XÁC (verified 2026-05-30)

```
  TỔNG (all files):
    427 occurrences, 68 files

  BREAKDOWN:
    Plan files (SKIP):     32 occ, 1 file  (plan-nt-label-rename.md)
    Backup/plan (SKIP):    ~80 occ, ~18 files
    ACTIVE (to rename):    ~315 occ, ~49 files

  PER-NT ACTIVE:
    NT1:   ~29 occ,  8 files  │ Local (Chunk/ ecosystem)
    NT2:   ~28 occ,  8 files  │ Local (Chunk/ ecosystem)
    NT3:   ~41 occ, 11 files  │ Mostly local, 2-3 cross-file
    NT4:   ~25 occ,  8 files  │ 2-3 cross-file
    NT5:   ~11 occ,  5 files  │ Local (= H11)
    NT6:   ~90 occ, 24 files  │ ★ Nhiều cross-file
    NT7:  ~134 occ, 37 files  │ ★★ NHIỀU NHẤT

  CROSS-FILE vs CHUNK-LOCAL:
    Cross-file (ngoài Chunk/ ecosystem): ~107 occ, ~20 files
    Chunk-local (Drill-Chunk/ + Chunk.md):  ~208 occ, ~29 files
```

---

## §4 — QUYẾT ĐỊNH (đã phân tích, CẦN CHỐT)

```
  ✅ Q1: DRILL FILES — OPTION A: KEEP + FORWARD POINTER
    Lý do:
    → Drill files dùng NT labels chủ đích làm cross-references
    → Rename sẽ gây redundancy ("F1 Compile-Gradient (gradient)")
    → Tiền lệ H10: drill files tự nhiên dùng formal name,
      nhưng NT case KHÁC — NTs là index numbers trong drill
    → Scope giảm: ~20 files ~107 occ (thay vì ~49 files ~315 occ)
    Action:
    → Thêm mapping table ở đầu 99-Master-Synthesis.md
    → Thêm 1 forward pointer line ở đầu mỗi drill synthesis file

  ✅ Q2: 99-MASTER-SYNTHESIS.MD — MAPPING TABLE
    → Thêm table "NT1 = Compile-Gradient (→ Chunk.md §1.1)"
    → Giữ NT labels trong hypothesis table (là IDs)
    → Reader mới đọc mapping table trước → hiểu ngay

  ✅ Q3: H11 + H12 — RIÊNG
    → NT5 chỉ có 11 occ → rename nhẹ, include trong plan này
    → H11 (556 occ, 38 files) = plan RIÊNG
    → H12 (145 occ, 24 files) = plan RIÊNG
    → Thuộc Generic Label Audit scope

  ✅ Q4: plan-abbreviation-backlog.md — CẬP NHẬT SAU
    → Bước cuối: xóa NT7 (và tất cả NT) khỏi "Label hệ thống"

  ✅ Q5: TÊN MỚI — ĐÃ VERIFY
    → 0 collision confirmed
    → NT2 + NT4: cân nhắc alt names (see §2)
    → Còn lại: confirmed tốt
```

---

## §5 — PHASES

```
  PHASE S1: CROSS-FILE RENAME (priority cao nhất)
    Scope: ~20 files, ~107 occ (NGOÀI Chunk/ ecosystem)
    Files:
      NT7 (~60 occ cross-file):
        Cortisol-Baseline.md (19), Background-Pattern.md (6),
        Feeling-Mech-Deep-Draft.md (7), Work-Adversity-Fear-Cluster.md (5),
        Work-Think-Act-Become-Cluster.md (5), Body-Feedback-Precondition.md (4),
        Protect.md (4), Work-Move-Fast-Break-Things.md (4),
        Feeling.md (3), Cortisol-Amplifier-Not-Cause.md (3),
        Feeling-Literacy-Training-Draft.md (4), Logic-Planning.md (2),
        Work-Chunk-Dependent-Visibility-Cluster.md (2),
        Work-Journey-Destination-Cluster.md (1), Schema.md (1),
        Neural-Processing-Flow.md (1), Body-Feedback-Mechanism.md (1),
        Mother-Optimization.md (1)
      NT6 (~17 occ cross-file):
        Modality.md (2), Logic-Planning.md (2),
        Feeling.md (5), Feeling-Mech-Deep-Draft.md (4),
        Feeling-Literacy-Training-Draft.md (10),
        Feeling-Chunk-Bridge-Draft.md (3), Feeling-Accuracy-Draft.md (2)
      NT4 (~4 occ cross-file):
        Core-Hardware.md (2), Neural-Architecture.md (1)
      NT3 (~2 occ cross-file):
        Neural-Processing-Flow.md (2)
    Approach:
      → Mỗi file: đọc context → replace NT→new name → review redundancy
      → "NT7 direction tag" → "Direction-At-Compile tag" (bỏ "direction" thừa)
      → "NT7 body-state-at-compile" → "Direction-At-Compile" (bỏ mô tả thừa)
    Sessions: 2-3

  PHASE S2: CHUNK.MD + DEFINITION FILES
    Scope: ~3 files
    Files:
      Chunk.md — thêm descriptive names vào section headings
        §2.4 "Body-state at compile" → "Direction-At-Compile (body-state direction)"
        §1.2 → "(Emergent-Binding)" note
        §6 → "(Label-As-Handle)" note
      99-Master-Synthesis.md — thêm mapping table + update references
      plan-abbreviation-backlog.md — xóa NT exceptions
    Sessions: 1

  PHASE S3: DRILL FILE FORWARD POINTERS
    Scope: ~2-3 synthesis files trong Drill-Chunk/
    Files:
      99-Master-Synthesis.md — mapping table (đã làm ở S2)
      10-F1-Synthesis.md — thêm note "NT7 = Direction-At-Compile"
      06-Internal-Synthesis.md — thêm note
      01-External-Synthesis.md — thêm note
    Approach:
      → Thêm 1 mapping block ở đầu mỗi synthesis file
      → KHÔNG rename NT labels trong body (giữ nguyên)
    Sessions: 1

  PHASE S4: VERIFICATION
    → grep "\bNT[1-7]\b" trên active non-whitelist files = 0
    → Whitelist: Drill-Chunk/ (toàn bộ), backup/, plan files
    → Spot-check 10+ files
    → Redundancy check (mô tả thừa sau rename)
    Sessions: 1

  TỔNG: 5-6 sessions
```

---

## §6 — RISK

```
  ⚠️ REDUNDANCY RISK (quan trọng nhất):
    → "NT7 direction" → "Direction-At-Compile direction" (thừa)
    → CẦN review context mỗi occurrence, bỏ phần mô tả trùng
    → Đây là lý do KHÔNG nên batch replace, phải đọc từng context

  ⚠️ CROSS-FILE CONSISTENCY:
    → Một số files dùng "NT7 body-state-at-compile" (có mô tả)
    → Một số chỉ dùng "NT7" (standalone)
    → Replace strategy khác nhau cho mỗi pattern

  ⚠️ REGRESSION: file đã rename xong bị edit bởi plan khác
    → Concept Cascade Refine Plan (27 files) có thể overlap
    → Coordinate: rename NTs TRƯỚC các plan khác touch same files
```

---

## §7 — LIÊN QUAN

```
  ✅ DONE:  H10 → Body-Feedback-Precondition (CLOSED 2026-05-30)
  🔲 THIS:  NT1-NT7 rename (plan này)
  🔲 NEXT:  plan-B-drill-to-framework.md (R-F1/R-F3 execution)
  🔲 LATER: H11 → Receptive-Productive-Gap (556 occ, 38 files)
  🔲 LATER: H12 → ? (145 occ, 24 files)
  🔲 LATER: Generic Label Audit Plans 4-10 (~7,600+ occ)
  📋 OLD:   plan-nt-label-rename.md (root level) — SUPERSEDED by this plan
```
