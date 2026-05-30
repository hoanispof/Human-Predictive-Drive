# Plan: L3 Retire — Phase 2: Research + Public-Plan Files

## STATUS: ✅✅ ALL COMPLETE — Phase 1-8 ALL DONE 2026-05-29

## Created: 2026-05-29

## Liên kết: [Phase 1 plan](plan-L3-retire-and-2dim-model.md) — ✅✅ COMPLETE (Core-Deep-Dive/ ~29 files, ~115 edits)

---

## §0 — BỐI CẢNH

Phase 1 chỉ cover **Core-Deep-Dive/** files. Rà soát toàn bộ framework phát hiện **14 file ACTIVE** trong **Research/** và **Public-Plan/** vẫn dùng "L3" body-base cũ (~83 refs).

### Mô hình đúng (recap từ Phase 1)

```
CHIỀU 1: SUBSTRATE
  L0 = Alive threshold (binary)
  L1 = 17 body-input substrates (graded, adaptive baseline)

CHIỀU 2: SIGNAL PROCESSING
  Direct-State = hardware pathways, from birth
  Evaluative = compiled patterns, develops with age

OUTPUT (observation layer):
  PFC observe → đặt tên: Status, Protect, Novelty, Mastery, etc.
  = Observation parameters — KHÔNG phải channels, layers, hay drives
```

### L3 cũ dùng SAI ở Research/ files theo 3 pattern

| Pattern | Files | Ý nghĩa thực | Replacement |
|---------|-------|---------------|-------------|
| **"L3 novelty/status/protect"** | Love-Unified, Birth-Rate files, Theme-E, Arms-Race | Observation parameters | Drop "L3" prefix, thêm "(evaluative)" khi cần |
| **"L0→L1→L3→PFC"** | Parkinson, Alzheimer | Braak staging mapping | "L0 substrate → L1 substrate → modulatory operators → PFC" |
| **"L3 controllable vs L1-L2"** | Self-Created-Threat, Work-Adversity | PFC-level vs body-compiled | "PFC-level (controllable) vs body-compiled (uncontrollable)" |

### ⚠️ OUT OF SCOPE — L2 refs

Nhiều file Research/ cũng dùng "L2" (Quality layer — đã remove trước L3). VD: "L2-L3 connection" trong Birth-Rate files. Plan này CHỈ fix L3. L2 sẽ được note nhưng KHÔNG sửa (cần plan riêng nếu muốn).

### ⚠️ OUT OF SCOPE — "Body-Base.md v2.0" stale version refs

Nhiều file reference "Body-Base.md v2.0" (current = v3.3). Đây là version bump riêng, KHÔNG thuộc L3 retire scope. Chỉ sửa KHI ref đi kèm "L0/L1/L3" text.

---

## §1 — REPLACEMENT PATTERNS

### Pattern A: Drop "L3" prefix (most common)

```
CŨ: "L3 Status", "L3 Novelty", "L3 Mastery", "L3 Protect", "L3 meaning"
MỚI: "Status", "Novelty", "Mastery", "Protect", "meaning"
     + thêm "(evaluative)" hoặc "(observation parameter)" khi cần phân biệt

CŨ: "L3 Pattern: novelty, mastery, status, protect"
MỚI: "Observation parameters (evaluative): novelty, mastery, status, protect"

CŨ: "body-base channels (Body-Base.md):" + L0/L1/L3 list
MỚI: "body-base (Body-Base.md v3.3):" + L0/L1 substrate + observation parameters
```

### Pattern B: Braak staging mapping

```
CŨ: "L0→L1→L3→PFC"
MỚI: "L0 substrate → L1 substrate → modulatory operators → PFC"

CŨ: "Stage 3-4 │ L3 drives + execution"
MỚI: "Stage 3-4 │ Modulatory operators + execution"

CŨ: "Body-Base.md v2.0 — L0/L1/L3, body evaluates patterns"
MỚI: "Body-Base.md v3.3 — L0+L1 substrate, body evaluates patterns"

CŨ: "Body-Base.md v2.0 §5: L0 (Alive) → L1 (body-inputs) → L3 (drives)"
MỚI: "Body-Base.md v3.3: L0 (Alive) + L1 (body-inputs) substrate + observation parameters"
```

### Pattern C: PFC-level vs body-compiled (Self-Created-Threat specific)

```
CŨ: "L3 (PFC)" / "L3 controllable"
MỚI: "PFC-level" / "PFC-level (controllable)"

CŨ: "L1-L2 (compiled)" / "L1-L2 uncontrollable"
MỚI: "Body-compiled" / "Body-compiled (uncontrollable)"

CŨ: "L3 compile thành L1-L2"
MỚI: "PFC-level compile thành body-level"

CŨ: "§4 — BẬT/TẮT: TẠI SAO L3 CONTROLLABLE, L1-L2 KHÔNG"
MỚI: "§4 — BẬT/TẮT: TẠI SAO PFC-LEVEL CONTROLLABLE, BODY-COMPILED KHÔNG"

CŨ: "Nếu L3: người đó TỰ CHỌN căng"
MỚI: "Nếu PFC-level: người đó TỰ CHỌN căng"

CŨ: "RISK: L3 CÓ THỂ COMPILE THÀNH L1-L2"
MỚI: "RISK: PFC-LEVEL CÓ THỂ COMPILE THÀNH BODY-LEVEL"
```

---

## §2 — PHASES

### Phase 1 — Core-Deep-Dive Remaining (3 files, ~11 refs) — ✅✅ DONE 2026-05-29

**Mục tiêu**: Dọn 3 file drill còn sót từ Phase 1.

**Tasks**:
- [x] 1.1: **00-Reading-Notes.md** (Drill-Feeling-Knowning/) — 7 refs (plan gốc nói 2, audit phát hiện 5 thêm)
  - L140: "L3 Mastery/Meaning/Status" → "Mastery/Meaning/Status (evaluative)" ✅
  - L238: "L3: meaning schema" → "Evaluative: meaning schema" ✅ (MISSED in original plan)
  - L879: "(L1 + L2 + L3 valid feelings)" → "(body-state + novelty + meaning — valid feelings)" ✅ (MISSED)
  - L961: "layers (L0, L1, L2, L3)" → "body-base levels (substrate AND evaluative)" ✅ (MISSED)
  - L1557: "L3 threats (status, role)" → "evaluative threats (status, role)" ✅ (MISSED)
  - L1568: "L3 threats" → "evaluative threats" ✅ (MISSED)
  - L1676: "L3 status mild" → "status mild (evaluative)" ✅

- [x] 1.2: **05-Theme-E-Empathy-Giving.md** (Drill-Feeling-Knowning/) — 3 refs (plan gốc nói 2)
  - L752: "L3 status" → "status, evaluative" ✅
  - L772: "L3 hit" → "status hit" ✅ (MISSED in original plan)
  - L892: "L3 status" → "status, evaluative" ✅

- [x] 1.3: **99-Overview-Synthesis.md** (Drill-Feeling-Knowning/) — 1 ref (NEW file, không có trong plan gốc)
  - L603: "L3 hit" → "status hit" ✅

**Verification**: Grep "L3" → Drill-Feeling-Knowning/ → 0 active body-base refs ✅

---

### Phase 2 — Neurodegeneration (2 files, ~11 refs) — ✅✅ DONE 2026-05-29

**Mục tiêu**: Fix Braak staging mapping trong Parkinson + Alzheimer.

**Tasks**:
- [x] 2.1: **Parkinson-Analysis.md** — 9 refs, Pattern B ✅ (v1.1→v1.2)
- [x] 2.2: **Alzheimer-Analysis.md** — 2 refs, Pattern B ✅ (v1.2→v1.3)

**Verification**: Grep Neurodegeneration/ → chỉ còn changelog refs ✅

---

### Phase 3 — Love-Unified (1 file, ~11 refs) — ✅✅ DONE 2026-05-29

**Tasks**:
- [x] 3.1: **Love-Unified.md** — 11 refs, Pattern A ✅ (v2.0→v2.1)

**Verification**: Grep → chỉ còn changelog ref ✅

---

### Phase 4 — Birth-Rate-Decline (4 files, ~16 refs) — ✅✅ DONE 2026-05-29

**Tasks**:
- [x] 4.1: **01_South-Korea_Analysis.md** — 5 refs ✅
- [x] 4.2: **06_Israel_Analysis.md** — 8 refs ✅
- [x] 4.3: **05_Finland_Analysis.md** — 2 refs ✅
- [x] 4.4: **09_Vietnam_Analysis.md** — 1 ref ✅

**Verification**: Grep Birth-Rate-Decline/ → 0 L3 refs ✅

---

### Phase 5 — Education-Arms-Race (1 file, ~4 refs) — ✅✅ DONE 2026-05-29

**Tasks**:
- [x] 5.1: **Education-Arms-Race.md** — 4 refs ✅

**Verification**: Grep → 0 L3 refs ✅

---

### Phase 6 — Self-Created-Threat + Work-Adversity (2 files, ~32 refs) — ✅✅ DONE 2026-05-29

**Tasks**:
- [x] 6.1: **Self-Created-Threat.md** — ~22 refs, Pattern C ✅ (v1.0→v1.1)
- [x] 6.2: **Work-Adversity-Fear-Cluster.md** — ~12 refs, Pattern C+A ✅

**Verification**: Grep → chỉ còn changelog refs ✅

---

### Phase 7 — Public-Plan + File-Index (2 files, ~5 refs) — ✅✅ DONE 2026-05-29

**Tasks**:
- [x] 7.1: **summary-paper-outline.md** — 3 refs ✅
- [x] 7.2: **01-File-Index.md** — 2 refs ✅ (Parkinson + Self-Created-Threat descriptions updated)

---

### Phase 8 — FINAL VERIFICATION — ✅✅ PASS 2026-05-29

- [x] 8.1: Grep `\bL3\b` body-base patterns → **0 active refs** ✅
- [x] 8.2: Grep "L0/L1/L3" → **0 active refs** (chỉ changelog + plan) ✅
- [x] 8.3: Grep "L1-L2" body-base → **0 active refs** in Self-Created-Threat + Work-Adversity ✅
- [x] 8.4: Grep "L3 novelty|L3 status|L3 mastery" → **0 active refs** ✅
- [x] 8.5: Plan status → ✅✅ ALL COMPLETE ✅

---

## §3 — L3 KHÁC CONCEPT — ĐÃ VERIFY, KEEP

Những file dùng "L3" cho concept KHÁC body-base — KHÔNG sửa:

| File | L3 = concept gì | Loại |
|------|------------------|------|
| Religion.md L1275 | L3 institutional (~150+) | Scale model |
| Connection-Education.md L1588 | L3 institutional | Scale model |
| Collective-Body.md | L3 institutional | Scale model |
| Coordination-Node.md | L3 institutional | Scale model |
| By-Product-Scale.md | L3 institutional | Scale model |
| Uncanny-Valley.md L539+ | L3 Self-Pattern-Modeling | Perception levels |
| Child-Development-Mechanism.md L354 | L3: Crude response | Development ladder |
| 09-Event-Chunks-Inference-Matrix.md | L3 development stage | Development ladder |
| Domain-Knowledge-Map.md L792 | literacy L3 | Development level |
| Cortisol-Baseline.md L694 | micro (L3) intensity | Intensity gradient |
| Core-Software.md L1386 | "L3 Drives COLLAPSED" | Historical note |
| Novelty.md L82 | "Core v7.5 (cũ)" | Historical marker |
| Threat.md L82, L88 | "Core v7.5 (cũ)" + "đã bỏ" | Historical marker |
| Body-Base.md L748 | "v2.1 gọi L3..." | Historical note |

---

## §4 — NGUYÊN TẮC

1. **Pattern C (PFC-level/body-compiled) = terminology MỚI chưa dùng ở Phase 1** — cần verify sau khi Self-Created-Threat xong rằng terminology consistent với Core-Deep-Dive/ files
2. **L2 refs = OUT OF SCOPE** — note nhưng KHÔNG fix (cần plan riêng)
3. **Version bump CHỈ cho files có substantive changes** (Parkinson, Self-Created-Threat, Love-Unified). Cross-ref-only fixes = không cần version bump
4. **01-File-Index.md fix CUỐI CÙNG** — vì nó mirror description của các file khác
5. **Nội dung khoa học KHÔNG ĐỔI** — chỉ thay framework terminology

---

## §5 — ƯỚC LƯỢNG

| Phase | Files | Refs | Mức độ | Sessions |
|-------|-------|------|--------|----------|
| Phase 1 | 2 | ~4 | Nhẹ | Cùng session Phase 2 |
| Phase 2 | 2 | ~11 | Trung bình | 1 session (gộp Phase 1) |
| Phase 3 | 1 | ~11 | Trung bình | 1 session (gộp Phase 4) |
| Phase 4 | 4 | ~16 | Nhẹ mỗi file | 1 session (gộp Phase 3) |
| Phase 5 | 1 | ~4 | Nhẹ | Cùng session Phase 4 |
| Phase 6 | 2 | ~32 | **Nặng** | 1 session riêng |
| Phase 7 | 2 | ~5 | Nhẹ | Cùng session Phase 6 |
| Phase 8 | 0 | 0 | Verify | Cuối cùng |
| **TỔNG** | **14 files** | **~83 refs** | | **~3 sessions** |

**Đề xuất grouping sessions**:
- Session A: Phase 1 + 2 (Core-Deep-Dive remaining + Neurodegeneration) — ~15 refs
- Session B: Phase 3 + 4 + 5 (Love-Unified + Birth-Rate + Education) — ~31 refs
- Session C: Phase 6 + 7 + 8 (Self-Created-Threat + Work-Adversity + Public-Plan + Verify) — ~37 refs

---

## §6 — RISKS

1. **Self-Created-Threat §4 "PFC-level vs body-compiled"**: Terminology mới — cần verify rằng "body-compiled" KHÔNG conflict với Compile-Taxonomy.md (Compile Type A/B/C). "Body-compiled" ở đây = compiled THÀNH body-level response, không phải Compile Type. Context khác nên OK, nhưng verify.

2. **Birth-Rate files "L2-L3"**: L2 cũng outdated nhưng OUT OF SCOPE. Fix L3 mà giữ L2 có thể tạo inconsistency tạm thời. Chấp nhận — plan riêng cho L2 nếu cần.

3. **Love-Unified channel table**: Structure table sẽ thay đổi — cần preserve alignment cho readability.

4. **01-File-Index.md**: Long lines khó edit — cần đọc toàn bộ line trước khi sửa.

---

## §7 — CHANGELOG

| Date | Phase | Status | Notes |
|------|-------|--------|-------|
| 2026-05-29 | Plan | CREATED | 14 files, ~83 refs identified from full framework audit |
| 2026-05-29 | Phase 1 | ✅ DONE | 3 files (was 2), 11 refs (was 4). +5 missed in 00-Reading-Notes, +1 in 05-Theme-E, +1 new file 99-Overview-Synthesis |
| 2026-05-29 | Phase 2 | ✅ DONE | 2 files, 11 refs. Parkinson v1.2, Alzheimer v1.3 |
| 2026-05-29 | Phase 3 | ✅ DONE | Love-Unified v2.1. 11 refs, channel table restructured |
| 2026-05-29 | Phase 4 | ✅ DONE | 4 Birth-Rate files, 16 refs. "L2-L3"→connection/evaluative |
| 2026-05-29 | Phase 5 | ✅ DONE | Education-Arms-Race, 4 refs. L1/L3→substrate/evaluative |
| 2026-05-29 | Phase 6 | ✅ DONE | Self-Created-Threat v1.1 (~22 refs) + Work-Adversity (~12 refs). Pattern C: L3→PFC-level, L1-L2→body-compiled |
| 2026-05-29 | Phase 7 | ✅ DONE | summary-paper-outline (3 refs) + 01-File-Index (2 refs) |
| 2026-05-29 | Phase 8 | ✅ PASS | FINAL VERIFICATION: 0 active body-base L3 refs in entire framework |
