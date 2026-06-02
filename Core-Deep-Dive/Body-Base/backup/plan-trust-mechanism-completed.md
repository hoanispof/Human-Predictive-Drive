# Plan: Trust.md — Trust Mechanism File

## Goal
Tạo Trust.md v1.0 tại Body-Base/ — formalize trust mechanism từ Drill-Trust-Valence-Interaction.md v1.1.
Sau hoàn thành → drill file → backup/.

## Rationale
- Trust hiện KHÔNG CÓ file mechanism riêng
- VP §2: 4 dòng (meta-dimension). CB §5: ~200 dòng (bridge APPLICATION). CN §5: brief.
- Drill v1.1 (1,398L) chứa substantial mechanism content chưa formalize
- Pattern: EVD was split from VP khi grow too big. Trust tương tự.

## Location + Naming
- File: `Core-Deep-Dive/Body-Base/Trust.md`
- Cùng cấp: VP, EVD, Body-Coupling, Inter-Body-Mechanism
- Trust = meta-dimension trong valence profile → belongs near valence files

## Pre-Read (Cold Start)
Đọc trước khi bắt tay viết:
1. Drill-Trust-Valence-Interaction.md v1.1 (FULL — source chính)
2. VP §2 (lines 276-395) — trust current definition
3. CB §5.1-§5.3 (lines 901-1099) — trust bridge/hijack (giữ nguyên, chỉ add forward ref)
4. CN §5 (grep "§5") — trust cascade
5. Guilt Drill §6.1 (lines 440-563) — 5-nguồn trust maintenance model → absorb vào Trust.md
6. Gap-Body-Need §11 — verify 5-step entity-gap matching (trust + valence emerge)
7. Mayer et al. 1995 mapping — Authority/Competence/Intention ↔ Ability/Benevolence/Integrity

## Outline Trust.md v1.0

### Header (frontmatter)
- title: Trust — Compiled Prediction About Gap-Fill Reliability
- version: 1.0
- status: MECHANISM FILE v1.0
- scope: WHAT trust IS + HOW trust FORMS + HOW trust BEHAVES + relationship to valence
- dependencies: VP v4.1, EVD v1.1, CB v2.1, CN v1.2, GBN v1.0, Entity-Compiled v1.0, Obligation v1.2

### §0 — VỊ TRÍ TRONG FRAMEWORK (~30L)
- Trust = meta-dimension trong valence profile (VP §2 ④)
- Trust = only bridge individual↔collective (CB §5.1)
- Trust per-entity (not per-domain by default)
- File này = MECHANISM. CB §5 = COLLECTIVE APPLICATION. CN §5 = NODE APPLICATION.
- Diagram: position of Trust.md relative to VP, EVD, CB, CN

### §1 — TRUST LÀ GÌ (~80L)
- Definition: compiled prediction about entity's gap-fill RELIABILITY
- Source: Drill §2 + §5 (2 observations insight)
- Trust ≠ Valence distinction (2 chiều ĐỘC LẬP)
  - Valence = OUTCOME assessment (past/present)
  - Trust = PREDICTION meta-tag (future-oriented)
  - Cùng data source (gap-fill) → đo 2 thứ khác → tương quan BUT independent
- 3 Sub-dimensions: Authority × Competence × Intention
  - Map to Mayer et al. 1995: Ability × Benevolence × Integrity
  - Mỗi sub-dimension ĐỘC LẬP (case sếp: authority HIGH + competence LOW)
- Trust vs Predictability vs Dependency (3 meta-dimensions khác)

### §2 — TRUST FORMATION: 4 NGUỒN (~100L)
- Áp dụng VP §3 (4 nguồn valence) specifically cho trust:
  - ① Direct experience: entity fill gap ổn định → trust TĂNG dần (CHẬM, chính xác)
  - ② Observed experience: thấy entity reliable cho người khác → trust tăng
  - ③ Schema inheritance: collective install trust (nhanh, kém chính xác, CÙNG GÓI với valence)
  - ④ Context inference: context cues → trust infer (e.g., đồng phục → authority trust)
- Key: nguồn ③ install trust + valence CÙNG GÓI TRƯỚC khi verify
  - Trẻ tin thầy TRƯỚC khi đi học
  - KOL trust installed qua parasocial (nguồn ③) without domain check
- Source: Drill §5.1

### §3 — TRUST MAINTENANCE: 5 NGUỒN (~80L)
- Từ Guilt Drill §6.1 (absorb vào đây — đây là trust mechanism, không phải guilt mechanism)
- Trust depth = f(① routine + ② childhood + ③ community + ④ peak + ⑤ identity)
- Mỗi nguồn ĐỘC LẬP — trust = TỔNG HỢP
- Case "lòng thành là được": ① thấp nhưng ②③④⑤ đủ → trust vẫn deep
- Obligation = safety net design (cho worst case khi ②③④⑤ yếu)
- Source: Guilt Drill §6.1

### §4 — TRUST DYNAMICS: ASYMMETRY (~80L)
- Build: CHẬM — months/years tích lũy qua multiple gap-fill outcomes
- Maintain: ỔN ĐỊNH — compiled = persistent, không cần reinforce mỗi ngày
- Collapse: CÓ THỂ NHANH — 1 betrayal = violent flip
- Asymmetry: build slow, destroy fast (Slovic 1993, Baumeister 2001)
- Analogy: trust ≈ khí hậu, valence ≈ nhiệt độ
- Source: Drill §4.1

### §5 — DEFAULT → CALIBRATED: 4 PHASES (~100L)
- Phase 1 — INSTALLED (0-6 tuổi): nguồn ③ install per-CATEGORY (tất cả thầy = tin)
- Phase 2 — DEFAULT OPERATION (6-15): installed HOẠT ĐỘNG NHƯ TRUTH, evolutionary functional
- Phase 3 — CALIBRATE (15+): direct experience override, trust SPLIT per-entity/per-domain
- Phase 4 — DOMAIN OVERRIDE (khi conflict sustained): domain = FINAL ARBITER
- Key: domain ≠ sole source (4 nguồn). Final arbiter KHI CONFLICT, nhưng nếu no conflict → installed persists
- KOL/propaganda exploit: install (nguồn ③) + no domain check → persist
- Source: Drill §5.1

### §6 — TRUST × VALENCE: 2 OBSERVATIONS CỦA CÙNG PROCESS (~100L)
- Cả 2 emerge từ entity × gap-fill interaction
- Valence: "entity fill gap TỐT hay XẤU?" (outcome per-interaction)
- Trust: "entity fill gap ỔN ĐỊNH và ĐÚNG không?" (aggregate prediction)
- Cùng data → cùng hướng → đồng biến TỰ NHIÊN
- NHƯNG đo 2 thứ khác → CÓ THỂ diverge
- Trust = ENHANCER cho resonance (amplify valence → probability condition ① tăng)
- Source: Drill §5

### §7 — 6 CO-OCCURRENCE MECHANISMS × 3 TẦNG (~120L)
- Tầng 1 Hardware: ① Resource Access Function + ② Learning Drive
- Tầng 2 Evaluative: ③ Smoothing/Halo + ④ Coherence Drive
- Tầng 3 Collective: ⑤ Trust Generalization + ⑥ Social Norm Install
- 3 tầng CỘNG DỒN → co-occurrence RẤT MẠNH
- Table tóm tắt 6 mechanisms
- Source: Drill §6

### §8 — BREAK CONDITIONS: KHI TRUST ≠ VALENCE (~80L)
- ① Direct experience override (harm > threshold)
- ② Domain-specific trust drop (calibration)
- ③ Betrayal / violent flip
- ④ Structural trust without choice (must trust + negative valence coexist)
- Threshold = f(harm intensity × duration)
- Source: Drill §10

### §9 — TRUST × POWER/STATUS (~60L)
- 4 mechanisms power → positive valence: resource + learning + coherence + install
- 4 mechanisms CỘNG DỒN → default positive toward authority
- Break: direct harm đủ mạnh + đủ lâu
- Source: Drill §8

### §10 — TRUST TRONG COORDINATION-NODE: POSITION vs PERSON (~60L)
- Trust POSITION (structural, per-role) vs Trust PERSON (experiential, per-individual)
- Khi aligned → ổn định. Khi diverge → dysfunction.
- "Biết sếp có quyền nhưng không giỏi" = position HIGH + person LOW
- Source: Drill §9

### §11 — CASES (~80L)
- Chọn 4-5 cases từ drill §11 (condensed, illustrative)
- Mẹ healthy / Sếp không giỏi / Thiên Chúa / KOL

### §12 — OPEN QUESTIONS (~40L)
- Chọn 4-5 most relevant từ drill §14
- Q: Trust formation speed per-dimension?
- Q: Trust ≠ formal condition cho resonance, nhưng de facto necessary?
- Q: Reliability vs Quality distinction?
- Q: Institutional vs individual trust hierarchy?

### §13 — HONEST ASSESSMENT (~40L)
- 🟢/🟡/🔴 per-section

### §14 — CROSS-REFERENCES (~40L)
- Citations (27 từ drill)
- Framework file references

## Estimated Output
- ~1,000-1,200 lines
- 14 sections + frontmatter

## Post-Creation Tasks
1. VP §2 → add note: "Trust mechanism detail: Trust.md v1.0"
2. CB §5.1 → add note: "Trust formation + dynamics: Trust.md v1.0"  
3. CN §5 → add note: "Position vs Person trust: Trust.md §10"
4. Verify drill §16 cross-refs covered

## Dependencies
- KHÔNG phụ thuộc Plan B (Guilt Distribution) — có thể triển khai song song
- Plan B §CB-5.4 sẽ reference Trust.md §3 (5-nguồn)
- Final: Drill file → backup/ (sau khi Plan B cũng hoàn thành)

## Phases
- Phase 1: Pre-read (7 targets above)
- Phase 2: Write Trust.md v1.0 (section by section, verify each vs drill + existing files)
- Phase 3: Update VP §2 + CB §5.1 + CN §5 (forward refs)
- Phase 4: Final review coherence
