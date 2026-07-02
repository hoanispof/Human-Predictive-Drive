# PLAN: Percentage (%) Refinement Across Framework

created: 2026-05-30
status: ✅✅ ALL COMPLETE (Core + Research/ + Applications/ audit)

---

## NGUYÊN TẮC MỚI CHO % USAGE

### Rule 1 — CITED RESEARCH (GIỮ nguyên)
% đi kèm citation 🟢 → GIỮ NGUYÊN.
VD: "Brain = 2% body mass, 20% energy (Raichle & Gusnard 2002)" → giữ.

### Rule 2 — LOGICAL/STRUCTURAL (GIỮ nguyên)
% dùng như logical statement, không phải measurement.
VD: "Cả hai đều không 100%", "100% body-need-driven" → giữ.

### Rule 3 — GRADIENT/SCALE MODELS (GIỮ + disclaimer)
% tạo phổ liên tục để trực quan hóa concept.
VD: Imagine-Final 5 levels (0-100%), Feeling 7-layer fidelity.
→ GIỮ phổ, thêm note "illustrative gradient, not measured values" nếu chưa có.

### Rule 4 — FRAMEWORK ESTIMATES (GIỮ + disclaimer)
% framework TỰ ĐẶT mà không có evidence → GIỮ NGUYÊN + thêm disclaimer nếu thiếu.
VD: "~90%" → giữ, nhưng đảm bảo section/file có disclaimer nearby.
**Quyết định 2026-05-30:** User chọn giữ TẤT CẢ %, chỉ thêm disclaimer where missing.

### Disclaimer patterns đã dùng trong framework:
- `"% = calibration anchor, KHÔNG phải đo lường"` (Feeling.md)
- `"exact % = guess, không có measurement"` (Anchor-Schema.md)
- `"calibration anchor, không đo chính xác"` (Neural-Processing-Flow.md)
→ Dùng pattern phù hợp nhất cho từng context.

### Bảng chuyển đổi qualitative (REFERENCE ONLY — không áp dụng systematic):
| Range       | Replacement term        | Notes                          |
|-------------|-------------------------|--------------------------------|
| ~95-100%    | nearly all              | Chỉ dùng khi cần diễn đạt     |
| ~80-95%     | vast majority           | Không dùng để thay thế %       |
| ~60-80%     | majority                |                                |
| ~40-60%     | roughly half            |                                |
| ~20-40%     | substantial minority    |                                |
| ~5-20%      | minority / small portion|                                |
| ~1-5%       | very few                |                                |
| <1%         | extremely rare          |                                |

---

## SCOPE

### SKIP hoàn toàn:
- Tất cả backup/ folders (~160+ files)
- Plan files (plan-*.md) — chỉ internal reference
- File-Index (01-File-Index.md) — auto-reflect framework files
- Draft files (Feel-Example-Draft*.md) — raw working material

### AUDIT + REFINE:
~65 active files, ~470+ occurrences of %

---

## PHASE A — AUDIT (Rà soát + Phân loại)

Mỗi file: đọc context từng %, phân loại vào 1 trong 4 rule, ghi kết quả vào plan này.
Format: `[RULE#] line:count — mô tả ngắn`

### A1 — CORE FOUNDATIONAL (ưu tiên cao nhất)
Các file định nghĩa vocabulary/principle → ảnh hưởng cascading.

| # | File | Count | R1 | R2 | R3 | R4 | Meta | Status |
|---|------|-------|-----|-----|-----|-----|------|--------|
| 1 | Body-Base/Why-Body-Knows.md | 16 | 0 | 1 | 3 | 11 | 1 | ✅ NEED disclaimer |
| 2 | Body-Base/Body-Base.md | 16 | 1 | 0 | 0 | 12 | 3 | ✅ NEED disclaimer |
| 3 | Body-Base/Feeling/Feeling.md | 36 | 2 | 3 | 25 | 1 | 4 | ✅ HAS disclaimer |
| 4 | Body-Base/Feeling/Body-Knowing.md | 15 | 4 | 1 | 0 | 7 | 2 | ✅ NEED disclaimer |
| 5 | Body-Base/Valence-Propagation.md | 10 | 0 | 0 | 10 | 0 | 0 | ✅ CHECK disclaimer |
| 6 | Body-Base/Schema/Anchor-Schema.md | 16 | 0 | 2 | 4 | 7 | 3 | ✅ HAS disclaimer |
| 7 | Body-Base/Schema/Schema.md | 4 | 1 | 1 | 1 | 0 | 1 | ✅ OK (no R4) |
| 8 | Body-Base/Cortisol-Baseline.md | 5 | 4 | 0 | 1 | 0 | 0 | ✅ OK (no R4) |
| 9 | Body-Base/Body-Coupling.md | 4 | 2 | 0 | 0 | 1 | 1 | ✅ NEED disclaimer |
| 10 | Body-Base/Inter-Body-Mechanism.md | 6 | 0 | 4 | 0 | 0 | 2 | ✅ OK (no R4) |
| 11 | Body-Base/Entity-Valence-Dynamics.md | 7 | 7 | 0 | 0 | 0 | 0 | ✅ OK (100% cited) |
| 12 | Neural-Processing-Flow.md | 28 | 2 | 5 | 16 | 1 | 4 | ✅ HAS disclaimer |
| 13 | Neural-Architecture.md | 4 | 4 | 0 | 0 | 0 | 0 | ✅ OK (100% cited) |
| 14 | Blackbox-Map.md | 15 | 2 | 0 | 12 | 0 | 1 | ✅ HAS disclaimer |
| 15 | Modality.md | 4 | 3 | 0 | 0 | 1 | 0 | ✅ HAS flag |
| 16 | Auditory-Hardware.md | 1 | 0 | 0 | 0 | 0 | 1 | ✅ OK (meta only) |
| **Subtotal** | | **191** | **30** | **17** | **72** | **41** | **22** | **✅ AUDIT DONE** |

### A2 — PFC FOLDER
| # | File | Count | Status |
|---|------|-------|--------|
| 17 | PFC/Logic-Feeling-Balance.md | 35 | |
| 18 | PFC/Logic-Feeling.md | 11 | |
| 19 | PFC/PFC-Development.md | 16 | |
| 20 | PFC/PFC-Hardware.md | 9 | |
| 21 | PFC/PFC-Hold-Dimensions.md | 10 | |
| 22 | PFC/PFC-Label.md | 7 | |
| 23 | PFC/PFC-Function.md | 3 | |
| 24 | PFC/PFC-Configuration.md | 3 | |
| 25 | PFC/PFC-Operations.md | 1 | |
| 26 | PFC/Logic-Planning.md | 2 | |
| 27 | PFC/Attention-Spectrum.md | 4 | |
| 28 | PFC/Logic-Feeling-Failure-Examples.md | 5 | |
| **Subtotal** | | **106** | |

### A3 — IMAGINATION FOLDER
| # | File | Count | Status |
|---|------|-------|--------|
| 29 | PFC/Imagination/Imagine-Final.md | 21 | |
| 30 | PFC/Imagination/Imagine-Final-Evaluation.md | 18 | |
| 31 | PFC/Imagination/Imagination.md | 28 | |
| 32 | PFC/Imagination/Somatic-Articulation-Loop.md | 4 | |
| **Subtotal** | | **71** | |

### A4 — OBSERVATION FOLDER
| # | File | Count | Status |
|---|------|-------|--------|
| 33 | Observation/Drive.md | 30 | |
| 34 | Observation/Connection.md | 13 | |
| 35 | Observation/Threat.md | 12 | |
| 36 | Observation/AI-Schema-Detection.md | 10 | |
| 37 | Observation/Empathy.md | 10 | |
| 38 | Observation/Autonomy.md | 7 | |
| 39 | Observation/Status.md | 6 | |
| 40 | Observation/Gratitude.md | 5 | |
| 41 | Observation/Boredom.md | 2 | |
| 42 | Observation/Liking-Wanting.md | 2 | |
| 43 | Observation/Novelty.md | 2 | |
| 44 | Observation/Meaning.md | 1 | |
| **Subtotal** | | **100** | |

### A5 — AGENT-MECHANISM FOLDER
| # | File | Count | Status |
|---|------|-------|--------|
| 45 | Chunk/Agent-Mechanism/Entity-Access.md | 17 | |
| 46 | Chunk/Agent-Mechanism/Entity-Compiled.md | 12 | |
| 47 | Chunk/Agent-Mechanism/Resonance-Per-Entity.md | 11 | |
| 48 | Chunk/Agent-Mechanism/Self-Pattern-Modeling.md | 8 | |
| 49 | Chunk/Agent-Mechanism/Agent-Mechanism.md | 7 | |
| 50 | Chunk/Agent-Mechanism/By-Product-Gap-Resonance.md | 7 | |
| 51 | Chunk/Agent-Mechanism/Resonance-Sustainability.md | 5 | |
| 52 | Chunk/Agent-Mechanism/Entity-Access-Excess.md | 33 | |
| 53 | Chunk/Agent-Mechanism/Bond-Architecture.md | 2 | |
| **Subtotal** | | **102** | |

### A6 — CHUNK + BODY-FEEDBACK FOLDERS
| # | File | Count | Status |
|---|------|-------|--------|
| 54 | Chunk/Chunk.md | 15 | |
| 55 | Chunk/Compile-Taxonomy.md | 21 | |
| 56 | Chunk/Background-Pattern.md | 5 | |
| 57 | Body-Feedback/Body-Feedback.md | 5 | |
| 58 | Body-Feedback/Reward-Signal-Architecture.md | 13 | |
| 59 | Body-Feedback/Hidden-Quality-Perception.md | 13 | |
| 60 | Body-Feedback/Gap-Direction.md | 12 | |
| 61 | Body-Feedback/Gap-Body-Need.md | 10 | |
| 62 | Body-Feedback/Gap-Distribution-Profile.md | 10 | |
| 63 | Body-Feedback/Body-Feedback-Label.md | 7 | |
| 64 | Body-Feedback/Body-Feedback-Precondition.md | 6 | |
| 65 | Body-Feedback/Body-Feedback-Mechanism.md | 3 | |
| 66 | Body-Feedback/Action-Space.md | 3 | |
| 67 | Body-Feedback/Reward-Calibration.md | 3 | |
| **Subtotal** | | **126** | |

### A7 — COLLECTIVE + DOMAIN FOLDERS
| # | File | Count | Status |
|---|------|-------|--------|
| 68 | Collective/Collective-Arc-Dynamics.md | 20 | |
| 69 | Collective/Collective-Body.md | 19 | |
| 70 | Collective/Coordination-Node.md | 16 | |
| 71 | Collective/Compliance-Floor.md | 4 | |
| 72 | Collective/Collective.md | 3 | |
| 73 | Domain/Domain-Mapping-Drive.md | 15 | |
| 74 | Domain/Discovery-vs-Expansion.md | 5 | |
| 75 | Domain/Drill-Emergent-Pattern.md | 4 | |
| 76 | Domain/Domain.md | 1 | |
| **Subtotal** | | **87** | |

### A8 — MELODY LENS + CLARIFICATION + DRILLS (active)
| # | File | Count | Status |
|---|------|-------|--------|
| 77 | Melody Lens/Personal-Melody.md | 17 | |
| 78 | Melody Lens/Melody-Arc.md | 3 | |
| 79 | Clarification/Dopamine-Is-Not-Reward.md | 6 | |
| 80 | Clarification/Prediction-Error-Is-Not-Reward.md | 1 | |
| 81 | Feeling/Drill-Feeling-Knowning/99-Overview-Synthesis.md | 29 | |
| 82 | Feeling/Drill-Feeling-Knowning/01-Theme-A-Architecture.md | 11 | |
| 83 | Feeling/Drill-Feeling-Knowning/00-Reading-Notes.md | 42 | |
| 84 | Feeling/Drill-Feeling-Knowning/03-Theme-B-Verbal-Chain.md | 3 | |
| 85 | Body-Feedback/Drill-Body-Feedback/03-Reward.md | 38 | |
| 86 | Body-Feedback/Drill-Body-Feedback/01-Foundation.md | 28 | |
| 87 | Body-Feedback/Drill-Body-Feedback/04-Integration.md | 22 | |
| 88 | Body-Feedback/Drill-Body-Feedback/02-Dissonance.md | 19 | |
| 89 | Chunk/Drill-Chunk/01b-Chunk-Activation-Dynamics.md | 20 | |
| 90 | Chunk/Drill-Chunk/09-Learning-Cycle.md | 6 | |
| 91+ | Chunk/Drill-Chunk/Child-Chunk-Development/* | ~50 | |
| **Subtotal** | | **~295** | |

### A-TOTAL: ~65+ active files, ~880+ occurrences

---

## PHASE B — REFINE (Từng phần)

Sau khi audit xong mỗi group → phân tích + sửa.
Mỗi session: 1-2 groups tùy complexity.

### Session Plan:
**Approach mới (2026-05-30):** GIỮ TẤT CẢ % + thêm disclaimer where missing.
→ Phase B = chỉ tìm files/sections THIẾU disclaimer → thêm vào. Ít edit hơn dự kiến ban đầu.

| Session | Group | Phase A | Phase B | Notes |
|---------|-------|---------|---------|-------|
| S1 | A1: Core Foundational | ✅ DONE | ✅ DONE (6 edits) | 6 files thêm disclaimer |
| S2 | A2: PFC | ✅ DONE | ✅ DONE (7 edits) | LFB, LF, PFC-Fn, PFC-Label, LP, PFC-Config, LF-Fail |
| S3 | A3: Imagination | ✅ DONE | ✅ DONE (1 edit) | Đã có disclaimers tốt. +1 IF-Eval |
| S4 | A4: Observation | ✅ DONE | ✅ DONE (1 edit) | 11/12 đã có disclaimers. +1 Connection |
| S5 | A5: Agent-Mechanism | ✅ DONE | ✅ DONE (1 edit) | +Resonance-Per-Entity. R1 dominant |
| S6 | A6: Chunk+Body-Feedback | ✅ DONE | ✅ DONE (1 edit) | +GDP. 14/14 có disclaimers |
| S7 | A7: Collective+Domain | ✅ DONE | ✅ DONE (1 edit) | +CF. DMD đã có flag |
| S8 | A8: Melody+Drills+Others | ✅ DONE | ✅ DONE (0 edits) | All framework files disclaimed. Drills=working material skip |
| S9 | Cross-check + 01-File-Index | SKIP | — | Files đã tự-ref nhau, không cần thêm |

## ✅ FINAL SUMMARY

**Completed:** 2026-05-30

**Approach:** GIỮ TẤT CẢ % + thêm disclaimer where missing.

**Total edits:** 22 disclaimer additions across ~126 active files, ~1,990+ % occurrences.
- Core-Deep-Dive/: 18 edits (A1-A8)
- Non-Core-Deep-Dive/: 3 edits (Phase B extended)
- Research/: 0 edits (~53 files, ~860+ occ — predominantly R1)
- Applications/: 1 edit (Curriculum-Framework.md — tier allocation %)

**Finding:** Framework đã có disclaimer infrastructure TỐT (~83% files đã tự-flag).
Research/ + VN Application files = data-dominant (R1 cited). Only ~17% files cần thêm disclaimer note nhỏ.

**Key patterns added:**
- `⚠️ % = calibration anchor, KHÔNG phải đo lường chính xác`
- `⚠️ % = illustrative, không đo lường`
- `⚠️ Fill level % = calibration anchor`
- `⚠️ % overlap = calibration anchor`
- `⚠️ Coverage % = ước lượng chiến lược`

**Per-group summary:**
- A1 Core: 6 edits (Why-Body-Knows, Body-Base, Body-Knowing, VP, Body-Coupling, Anchor-Schema)
- A2 PFC: 7 edits (LFB, LF, PFC-Fn, PFC-Label, LP, PFC-Config, LF-Fail)
- A3 Imagination: 1 edit (IF-Evaluation)
- A4 Observation: 1 edit (Connection)
- A5 Agent-Mechanism: 1 edit (Resonance-Per-Entity)
- A6 Chunk+Body-Feedback: 1 edit (Gap-Distribution-Profile)
- A7 Collective+Domain: 1 edit (Compliance-Floor)
- A8 Melody+Drills: 0 edits (all disclaimed or working material)
- **Non-Core:** 3 edits (expert-verification-map.md, AI-Self-Model.md, Social-Calibration.md)

---

## PHASE R — RESEARCH/ AUDIT (2026-05-30)

**Scope:** Toàn bộ Research/ folder (~53 active files, ~860+ % occurrences).
**Result:** 0 edits needed.

| Cluster | Files | Occ | R1 | R2 | R3 | R4 | Disclaimer | Edits |
|---------|-------|-----|-----|-----|-----|-----|-----------|-------|
| R1 Health-Conditions | 12 | 310+ | 93%+ | <5% | <2% | 0% | ALL YES | 0 |
| R2 Birth-Rate-Decline | 9 | 300 | 63% | 23% | 10% | 4% | ALL YES | 0 |
| R3 Education+ChildDev | 11 | 191 | 40% | 27% | 9% | 20% | ALL YES* | 0 |
| R4 Global | 5 | 126 | 51%+ | 24%+ | 14% | <5% | ALL YES | 0 |
| R5 Remaining Research | 16+ | 130+ | 60%+ | 25%+ | 10% | <5% | ALL YES** | 0 |
| **TOTAL** | **~53** | **~860+** | | | | | | **0** |

*R3 Education: Domain-Knowledge-Map has `⚠️ % = APPROXIMATE` (line 783) + confidence metadata.
**R5: Quote-Analysis files + some smaller files have weaker formal disclaimers but all R4 content is either cross-references to already-disclaimed Core files or covered by 🟢/🟡/🔴 confidence metadata.

**Key finding:** Research/ files are predominantly R1 (cited clinical/demographic/neuroscience data). They already use the 🟢/🟡/🔴 confidence system in metadata headers. No additional disclaimers needed.

---

## PHASE APP — APPLICATIONS/ AUDIT (2026-05-30)

**Scope:** 8 active files (excluding backup/, plan files), 252 % occurrences.
**Result:** 1 edit.

| File | Occ | R1 | R2 | R3 | R4 | Disclaimer | Edit |
|------|-----|-----|-----|-----|-----|-----------|------|
| 00_Overview.md | 1 | 0 | 1 | 0 | 0 | N/A | — |
| Era-Analysis-2025.md | 2 | 2 | 0 | 0 | 0 | YES | — |
| Hardware-Calibration.md | 1 | 0 | 1 | 0 | 0 | N/A | — |
| Education-System.md | 11 | 0 | 2 | 9 | 0 | YES (🟢 PFC) | — |
| Curriculum-Framework.md | 15 | 0 | 1 | 1 | 13 | **ADDED** | ✅ 1 |
| VN-Cultural-Factors.md | 37 | 37 | 0 | 0 | 0 | YES (all R1) | — |
| VN-Recommendations.md | 22 | 18 | 2 | 0 | 1 | YES (STRONG) | — |
| VN-Education-Status.md | 163 | 150+ | 0 | 0 | 13 | YES (🟡 derived) | — |
| **TOTAL** | **252** | **207+** | **7** | **10** | **27** | | **1** |

**Edit:** Curriculum-Framework.md — added `⚠️ % = calibration anchor, KHÔNG phải đo lường chính xác` after tier allocation table (Foundation/Era/Per-hardware per stage).

**Key finding:** Applications/ is data-heavy (VN files ~82% R1 cited data from TALIS, PISA, World Bank). Education-System.md PFC gradient is 🟢 tagged. Only Curriculum-Framework.md had R4 tier allocation % without explicit disclaimer.

---

## TIẾN TRÌNH AUDIT

### A1 — Core Foundational ✅ AUDIT COMPLETE

**Tổng kết:** R1:30, R2:17, R3:72, R4:41, Meta:22 = 191 occ.

**3 R4 patterns chính:**
- Pattern A: `~90%/~10%` body accuracy (6+ instances, 4 files)
- Pattern B: `~95%/~5%` compiled/PFC split (6+ instances, 3 files)
- Pattern C: `~80%` compiled schemas dominant (7+ instances, 2 files)

**Files CẦN thêm disclaimer (Phase B):**
1. Why-Body-Knows.md — 11 R4, self-flags at Honest Assessment nhưng R4 instances ở các section khác chưa có disclaimer
2. Body-Base.md — 12 R4 (Pattern A+B+C), self-flags at lines 1312-1314
3. Body-Knowing.md — 7 R4, KHÔNG có disclaimer
4. Valence-Propagation.md — 10 R3, section flagged 🔴 HYPOTHESIS nhưng cần verify disclaimer
5. Body-Coupling.md — 1 R4 (`90% positive`), không disclaimer
6. Anchor-Schema.md — 7 R4, ĐÃ CÓ disclaimer (line 1651) nhưng R4 ở section xa

**Files ĐÃ ĐỦ disclaimer:** Feeling.md, Neural-Processing-Flow.md, Blackbox-Map.md, Modality.md
**Files KHÔNG CẦN sửa:** Schema.md, Cortisol-Baseline.md, Inter-Body-Mechanism.md, Entity-Valence-Dynamics.md, Neural-Architecture.md, Auditory-Hardware.md

---

## NOTES

- backup/ files: KHÔNG SỬA. Nếu active file đã sửa, backup giữ nguyên bản cũ.
- Drills: SỬA nhẹ hơn (chỉ sửa nếu drill content CÒN ĐƯỢC DÙNG bởi framework files). Nếu drill đã superseded → skip.
- Cascading: Khi sửa Core files (A1), cần check xem Observation/Domain files có quote % đó không → sửa đồng bộ.
- 01-File-Index.md: sửa CUỐI CÙNG, reflect state mới.
