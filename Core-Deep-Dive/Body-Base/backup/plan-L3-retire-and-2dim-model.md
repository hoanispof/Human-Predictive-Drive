# Plan: Retire L3 + Formalize 2-Dimension Body-Feedback Model

## STATUS: ✅✅ ALL PHASES COMPLETE

## Created: 2026-05-29

---

## §0 — BỐI CẢNH + LÝ DO

### Vấn đề gốc

Body-Base.md v3.0 (2026-05-16) đã retire L3:
- L3 "PFC Drives" → PFC-mediated OPERATORS on L1 substrate
- Protect → observation parameter, KHÔNG phải operator
- Body-Base.md v3.3 đã hoàn tất reframe

NHƯNG: 16 file khác vẫn reference "L0-L1-L3" hoặc "L3" cũ.
Tổng ~40+ chỗ cần sửa.

### Phân tích kiến trúc

L3 cũ gộp SAI 2 concept khác loại:
- Novelty, Status → PFC-mediated operators (shift L1 baselines)
- Protect, Mastery → observation parameters (named patterns at output)

Cả hai KHÔNG phải "body channels" cùng loại với L0/L1.

### Mô hình đúng: 2 chiều orthogonal

```
CHIỀU 1: SUBSTRATE (body monitors CÁI GÌ?)
  L0 = Alive threshold (binary)
  L1 = 17 body-input substrates (graded, adaptive baseline)

CHIỀU 2: SIGNAL PROCESSING (body tạo signal KIỂU GÌ?)
  Direct-State = hardware pathways, from birth, no evaluation
  Evaluative = compiled patterns, develops with age, E₀→E₃

MỐI QUAN HỆ:
  L0 → chỉ tạo Direct-State signals
  L1 → tạo CẢ HAI (VD: temperature = Direct-State, food eval = Evaluative)

OUTPUT (observation layer):
  PFC observe signals → đặt tên: Status, Protect, Novelty, Mastery, etc.
  = Observation parameters — KHÔNG phải channels hay layers
```

### Replacement patterns

| Cũ (L3) | Mới |
|---|---|
| "L0-L1-L3" | "L0+L1 substrate" hoặc "L0+L1" |
| "L3 Pattern: novelty, mastery, status, protect" | "observation parameters (emerge from evaluative processing on L0+L1)" |
| "L3 Novelty" / "L3 Status" | "Novelty" / "Status" (observation parameter) |
| "L3 drives" | "PFC-mediated operators on L1" (Novelty, Status) hoặc "observation parameters" (Protect, Mastery) |
| "L3 channels" | bỏ — thay bằng mô hình 2 chiều (substrate × processing type) |
| "L0/L1/L3 taxonomy" | "L0+L1 substrate + observation parameters" |
| "L0/L1/L3 channels được FEED đủ?" | "body-base substrate (L0+L1) + observation parameters được feed đủ?" |

---

## §1 — SCOPE: 16 FILES, ~40+ EDITS

### Tier 1 — FOUNDATIONAL (thay đổi ở đây → ảnh hưởng cascade)

| # | File | L3 refs | Mức độ thay đổi | Nội dung |
|---|------|---------|-----------------|----------|
| 1 | Valence-Propagation.md v4.0 | 5 | **REWRITE §1 "body channels"** | YAML dep (L25), §0 (L99), §1 def (L199-202, L273) |
| 2 | Cortisol-Baseline.md v2.1 | 5 | **REFINE 5 chỗ** | YAML (L32-33), §2 table (L115), §4 note (L205), §15 cross-ref (L3269) |
| 3 | Entity-Valence-Dynamics.md v1.0 | 1 | YAML dep fix | L25 |

### Tier 2 — SIGNAL/FEELING FILES

| # | File | L3 refs | Mức độ | Nội dung |
|---|------|---------|--------|----------|
| 4 | Body-Feedback-Label.md v2.1 | 1 | Cross-ref table fix | L1133 |
| 5 | Feeling.md v3.0 | 1 | Source list fix | L826 |
| 6 | Feeling-Mechanism-Deep-Draft.md | 1 | Single line fix | L394 |
| 7 | 02-Dissonance.md | 1 | Framework mapping fix | L316 |

### Tier 3 — IMAGINATION FILES (nặng nhất)

| # | File | L3 refs | Mức độ | Nội dung |
|---|------|---------|--------|----------|
| 8 | Imagine-Final-Evaluation.md | ~15+ | **REWRITE §2B-ii** + scattered refs | Entire "Body-Base Channels" section uses L3 taxonomy |
| 9 | Imagine-Final.md v3.0 | 3 | Table + def fix | L185, L221-222 |

### Tier 4 — OTHER FILES

| # | File | L3 refs | Mức độ | Nội dung |
|---|------|---------|--------|----------|
| 10 | Neural-Processing-Flow.md v2.0 | 1 active | Single line fix | L750 (L3 in content despite fix note) |
| 11 | Collective-Body.md | 1 | Cross-ref fix | L144 |
| 12 | 09-Event-Chunks-Inference-Matrix.md | 1 | Cross-ref fix | L731 |
| 13 | 09-Event-Chunks-Inference-Matrix-VI.md | 1 | Cross-ref fix | L748 |

### Tier 5 — HISTORICAL NOTES (verify, likely keep as-is)

| # | File | L3 refs | Notes |
|---|------|---------|-------|
| 14 | Body-Base.md v3.3 | 2 | Already says "L3 CORRECTED in v3.0" — KEEP as historical |
| 15 | Drive.md | 1 | "Core v7.5 (cũ)" — KEEP as historical context |
| 16 | Novelty.md | 1 | "Core v7.5 (cũ)" — KEEP as historical context |
| 17 | Protect.md | 1 | "Core v7.5 (cũ)" — KEEP as historical context |
| 18 | Threat.md | 1 | "Core v7.5 (cũ)" — KEEP as historical context |
| 19 | Neural-Processing-Flow.md | 3 | Fix notes ("L3 operators → observation parameters") — KEEP |

### Deprecated source
- Body-Input-Enumeration.md → ALREADY in backup/ (L0/L1/L3 taxonomy source retired)

---

## §2 — PHASES

### Phase 0 — VERIFY + FORMALIZE (session này)

**Mục tiêu**: Xác nhận mô hình 2 chiều chính xác, KHÔNG có gaps.

**Tasks**:
- [ ] 0.1: Review Body-Base.md §5 (L0-L1 substrate) — xác nhận model hiện tại
- [ ] 0.2: Review Reward-Signal-Architecture §1 + Dissonance-Signal-Architecture §1 — xác nhận Direct-State/Evaluative đã formalize đủ
- [ ] 0.3: Xác nhận: L0+L1 substrate + Direct-State/Evaluative processing + observation parameters = COMPLETE model (không thiếu gì L3 từng cover)
- [ ] 0.4: Draft replacement text cho "body channels" definition (sẽ dùng trong VP §1)

**Verification checklist — L3 từng cover gì, mới cover ở đâu:**
- Novelty → Observation/Novelty.md (observation parameter) + Body-Base §5.3 (operator on L1)
- Status → Observation/Status.md (observation parameter) + Body-Base §5.3 (operator on L1)
- Protect → Observation/Protect.md (observation parameter, KHÔNG phải operator)
- Mastery → không có file riêng, nhưng = observation pattern of skill compilation depth

**Phase 0 FINDINGS (2026-05-29):**

✅ 0.1-0.2: Body-Base §5 + RSA §1 + DSA §1 confirmed — model đầy đủ.

✅ 0.3: Verification — L3 từng cover gì, mới cover ở đâu:
  - Novelty → Body-Base §5.3 (operator on L1) + Observation/Novelty.md ✅
  - Status → Body-Base §5.3 (operator on L1) + Observation/Status.md ✅
  - Protect → Observation/Protect.md (observation parameter, NOT operator) ✅
  - Mastery → không có file riêng, = observation pattern of skill compilation depth ✅
  → COMPLETE: mọi thứ L3 từng cover đã có home mới.

✅ 0.4: Replacement text cho valence profile table (VP §2):
  OLD: "BODY-BASE CHANNELS: L0 Alive, L1 Body-inputs, L3 Pattern"
  NEW structure:
  ```
  SUBSTRATE ASSESSMENT (L0 + L1):
    L0 Alive:     safe ←→ dangerous
    L1 Body-inputs:
      Nutrition:   useful ←→ harmful
      Comfort:     pleasant ←→ unpleasant
      Sleep:       promoting ←→ disrupting
      Autonomy:    enabling ←→ constraining
      Social:      connecting ←→ isolating

  EVALUATIVE ASSESSMENT (compiled pattern evaluation):
      Novelty:     interesting ←→ boring
      Mastery:     enabling ←→ blocking
      Status:      elevating ←→ diminishing
      Protect:     safe ←→ threatening (my resources)
  ```
  → Substrate = L0+L1 hardware (Direct-State territory)
  → Evaluative = compiled patterns evaluate (Evaluative territory)
  → Observation parameter names KEPT — correctly placed as evaluation output
  → Social/connection stays under L1 (hardware social need, Coan 2015)
  → Status stays under Evaluative (requires compiled social comparison)

⚠️ SEPARATE ISSUE NOTED — Cortisol-Baseline L694:
  "Intensity: micro (L3) → mild (L2) → strong (L1) → emergency"
  Đây là intensity gradient (closeness to body core), KHÔNG phải body-base layers.
  L3 ở đây = PFC-level (abstract, micro). L1 = body-level (direct, strong).
  → KHÁC concept vs body-base L0/L1/L3.
  → KHÔNG sửa trong plan này (cần plan riêng nếu muốn cleanup L-overloading).
  → Chỉ NOTE trong Phase 1 task 1.3 để tránh sửa nhầm.

**Output**: Plan verified. Replacement text drafted. Phase 0 COMPLETE.

### Phase 1 — FOUNDATIONAL FILES (1 session, ~3 files)

**Mục tiêu**: Sửa 3 file nền tảng mà các file khác reference.

**Tasks**:
- [x] 1.1: **Valence-Propagation.md v4.0 → v4.1** ✅ (11 refs fixed, not 5)
  - YAML dep (L25): "Body-Base.md v2.1 — L0-L1-L3" → "Body-Base.md v3.3 — L0+L1 substrate"
  - §0 flow diagram (L99, L115): "L0-L3 channels" → "L0+L1 substrate"
  - §1 "body channels" definition (L199-202): REWRITE core definition
    - OLD: "Body channels = hệ thống L0-L1-L3: L0 Alive, L1 Body-inputs, L3 Pattern"
    - NEW: mô hình 2 chiều (substrate L0+L1 × evaluative assessment)
    - Observation parameters = named patterns at evaluative output, NOT channels
  - §2 valence profile TABLE (L266-286): **RESTRUCTURE**
    - OLD: "BODY-BASE CHANNELS: L0, L1 subs, L3 subs"
    - NEW: "SUBSTRATE ASSESSMENT (L0+L1)" + "EVALUATIVE ASSESSMENT"
    - Novelty/Mastery/Status/Protect → dưới "EVALUATIVE ASSESSMENT"
    - Social/connection → stays under L1 (hardware social need)
    - Text around table (L291-297): update "channel" refs
  - Version bump: v4.0 → v4.1

- [x] 1.2: **Entity-Valence-Dynamics.md v1.0 → v1.1** ✅ (2 refs fixed, not 1)
  - YAML dep: same fix as VP
  - Scan for any other L3 usage in body text

- [x] 1.3: **Cortisol-Baseline.md v2.1 → v2.2** ✅ (5 fixed, L694 intensity KEPT)
  - YAML deps (L32-33): remove L3 references
  - §2 table (L115): "L3 PFC drives" → "PFC-mediated operators / observation parameters"
  - §4 note (L205): "L0/L1/L3" → "L0+L1"
  - §15 cross-ref (L3269): update
  - ⚠️ L694: "micro (L3) → mild (L2) → strong (L1)" — ĐÂY LÀ INTENSITY GRADIENT
    (L3 = PFC-level abstract, L1 = body-level direct). KHÔNG phải body-base layers.
    KHÔNG SỬA trong plan này. Note cho plan riêng (L-overloading cleanup).

**Verification**: Grep "L3" across these 3 files → expect 0 active refs.

### Phase 2 — SIGNAL/FEELING FILES (1 session, ~4 files)

**Mục tiêu**: Sửa files thuộc body-feedback và feeling layers.

**Tasks**:
- [x] 2.1: **Body-Feedback-Label.md v2.1** ✅ — 1 cross-ref fix
- [x] 2.2: **Feeling.md v3.0** ✅ — 15 refs (not 1): L0-L3 shorthand→body-base, L2/L3 source→evaluative
- [x] 2.3: **Feeling-Mechanism-Deep-Draft.md** ✅ — 5 refs (not 1): same patterns as Feeling.md
- [x] 2.4: **02-Dissonance.md** ✅ — 8 refs (not 1): all "L3 status"→"status (observation parameter)"

**Verification**: Grep "L3" across 4 files → expect 0 active refs.

### Phase 3 — IMAGINATION FILES (1 session, nặng nhất)

**Mục tiêu**: Rewrite §2B-ii trong Imagine-Final-Evaluation.md.

**Tasks**:
- [ ] 3.1: **Imagine-Final-Evaluation.md → version bump**
  - §2B-ii header: "L0/L1/L3 channels được FEED đủ?" → new framing
  - §2B-ii toàn bộ: rewrite using substrate + observation parameters
    - "L3 Status met" → "Status observation: resource access OK"
    - "L3 Novelty met" → "Novelty observation: prediction-delta feed OK"
    - "L3 channels" → "observation parameters"
  - §2B-ii CÁCH CHECK: update channel listing
  - YAML scope note (L35-37): update
  - Scattered refs in tree diagram (L846), tables, VD
  - ~15 edits tổng

- [ ] 3.2: **Imagine-Final.md v3.0 → v3.1**
  - L185: "Chunk-based (L3)" → "Chunk-based (observation parameters)"
  - L221-222: "L3 Novelty + Status" → "Novelty + Status"

**Verification**: Grep "L3" across 2 files → expect 0 active refs.

### Phase 4 — OTHER FILES (1 session, nhẹ)

**Mục tiêu**: Dọn dẹp remaining files.

**Tasks**:
- [x] 4.1: **Neural-Processing-Flow.md v2.0** ✅ — L750 (L2/L3 source numbering→descriptive)
- [x] 4.2: **Collective-Body.md** ✅ — L144 (L0-L1-L3→L0+L1). ⚠️ L3 institutional scale refs = DIFFERENT concept, KEPT.
- [x] 4.3: **09-Event-Chunks-Inference-Matrix.md** ✅ — L731 cross-ref. ⚠️ L3 development ladder = DIFFERENT concept, KEPT.
- [x] 4.4: **09-Event-Chunks-Inference-Matrix-VI.md** ✅ — L748 cross-ref. Same as 4.3.
- [x] 4.5: **Domain-Mapping-Drive.md** ✅ — L1512, L2406 "L3 status"→"status" (BONUS: not in original plan)
- [x] 4.6: **01-External-Synthesis.md** ✅ — L156, L164 "L2/L3"→"evaluative" (BONUS)
- [x] 4.7: **Knowledge-Flow.md** ✅ — L551 "L3"→"Evaluative" (BONUS)
- [x] 4.8: **Reward-Signal-Architecture.md** ✅ — L2004 cross-ref version fix (BONUS)

**Verification**: Grep "L3" across 4 files → expect 0 active refs.

### Phase 5 — HISTORICAL NOTES VERIFY (cuối session Phase 4)

**Mục tiêu**: Xác nhận Tier 5 files đã đúng format "cũ".

**Tasks**:
- [x] 5.1: Body-Base.md ✅ — ALL L3 refs = v2.1→v3.0 reframe history. CORRECT.
- [x] 5.2: Drive.md, Novelty.md, Protect.md, Threat.md ✅ — ALL "Core v7.5 (cũ)" properly marked.
  + Novelty.md L685 "(L3, controllable)" = active content → FIXED to "(PFC-mediated, controllable)"
- [x] 5.3: Neural-Processing-Flow.md ✅ — Fix notes L1023-1024 say "L3→observation parameters." CORRECT.
- [x] 5.4: Cortisol-Baseline.md L694 ✅ — "micro (L3)→mild (L2)→strong (L1)" = intensity gradient. KEPT.

**NO EDITS expected** — chỉ verify rằng historical context rõ ràng.

### Phase 6 — FINAL VERIFICATION (cuối cùng)

**Tasks**:
- [x] 6.1: Grep "L3" toàn bộ Core-Deep-Dive/ (exclude backup/) ✅ — DONE.
  Remaining L3 = DIFFERENT concepts (scale L3, development ladder L3, case numbering)
  + historical/correction notes. ALL Body-Base L3 refs cleaned.
- [x] 6.2: Grep "L0-L1-L3" ✅ — 0 active. Only in backup/ + plan + changelogs.
- [x] 6.3: Grep "L0/L1/L3" ✅ — 0 active. Only in backup/ + plan + changelogs.
- [x] 6.4: Spot-check VP §1-§2, Cortisol §2, IFE §2B-ii ✅ — verified during implementation.
- [x] 6.5: Plan status → COMPLETE ✅

---

## §3 — NGUYÊN TẮC THỰC HIỆN

1. **KHÔNG đổi tên L0, L1** — chúng vẫn chính xác (substrate layers)
2. **KHÔNG tạo "L3 mới"** — Evaluative là processing type, không phải substrate layer
3. **Giữ historical notes** — "Core v7.5 (cũ)" trong Observation/ files = context hữu ích
4. **Replacement text phải CHÍNH XÁC** — không chỉ delete L3, phải thay bằng mô hình đúng
5. **Version bump** cho mỗi file sửa (trừ minor cross-ref fixes)
6. **Body-Input-Enumeration.md** — đã ở backup/, KHÔNG cần sửa

---

## §4 — ƯỚC LƯỢNG

| Phase | Files | Edits | Sessions |
|-------|-------|-------|----------|
| Phase 0 | 0 (verify) | 0 | Cùng session plan |
| Phase 1 | 3 | ~15 | 1 session |
| Phase 2 | 4 | ~4 | 1 session (có thể gộp Phase 1) |
| Phase 3 | 2 | ~18 | 1 session |
| Phase 4 | 4 | ~4 | 1 session (có thể gộp Phase 3) |
| Phase 5 | 5 | 0 (verify) | Cuối Phase 4 |
| Phase 6 | 0 (verify) | 0 | Cuối cùng |
| **TỔNG** | **~13 files sửa** | **~41 edits** | **2-3 sessions** |

---

## §5 — RISKS + MITIGATION

1. **Cortisol-Baseline L694 "L3"**: Có thể là intensity level (micro/mild/strong/emergency), KHÔNG phải body-base layer → cần verify trước khi sửa
2. **Imagine-Final-Evaluation §2B-ii**: Section dùng L3 RẤT sâu trong logic phân tích → rewrite cần preserve analysis quality, chỉ thay terminology
3. **VP §1 "body channels"**: Đây là DEFINITION section → rewrite cần chính xác về mặt kiến trúc, tham chiếu đúng đến Body-Base v3.3 + Reward-Signal-Architecture
4. **Cross-file consistency**: Sau khi sửa, các file reference lẫn nhau phải coherent

---

## §6 — CHANGELOG

| Date | Phase | Status | Notes |
|------|-------|--------|-------|
| 2026-05-29 | Plan | CREATED | Initial plan based on analysis |
| 2026-05-29 | Phase 0 | COMPLETE | Model verified. VP §2 table restructure added. Cortisol L694 = separate issue (intensity, not layer). Replacement text drafted. |
| 2026-05-29 | Phase 1 | COMPLETE | VP v4.0→v4.1 (11 refs, not 5). EVD v1.0→v1.1 (2 refs, not 1). Cortisol v2.1→v2.2 (5 fixed, 1 KEPT intensity gradient). |
| 2026-05-29 | Phase 2 | COMPLETE | BFL (1 ref). Feeling.md (15 refs, not 1 — L0-L3 shorthand + L2/L3 source numbering). FMDD (5 refs). 02-Dissonance (8 refs). Total Phase 2: 29 edits vs planned 4. |
| 2026-05-29 | Phase 3 | COMPLETE | IFE v1.2→v1.3 (20 refs, not ~15). IF v3.0→v3.1 (3 refs). §2B-ii REWRITE complete. |
| 2026-05-29 | Phase 4 | COMPLETE | NPF (1 ref). CB (1 ref, ⚠️ L3 institutional=DIFFERENT). 09-ECI×2 (1 ref each, ⚠️ L3 ladder=DIFFERENT). +4 BONUS: DMD, ExtSynth, KF, RSA. |
| 2026-05-29 | Phase 5 | COMPLETE | ALL historical notes verified. Novelty.md L685 FIXED (active content). |
| 2026-05-29 | Phase 6 | COMPLETE | Final grep: 0 active Body-Base L3 refs. Remaining L3 = scale model / development ladder / case numbering (DIFFERENT concepts). Plan CLOSED. |
