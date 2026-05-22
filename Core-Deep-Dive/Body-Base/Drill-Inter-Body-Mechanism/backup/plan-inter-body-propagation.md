# Plan: Inter-Body Drill → Core Framework ALL REWRITE

> **Ngày tạo:** 2026-05-16
> **Cập nhật:** 2026-05-17 v11.0 — ALL PHASES COMPLETE. Phase 20b Entity-compiled propagation.
> **Trạng thái:** ✅✅ COMPLETE — ALL 31 PHASES DONE
> **Source:** Architecture-Summary.md v1.1 (8 principles, 6 rounds drill, 2,259L + 409L)
> **Mục tiêu:** 19 mechanism rewrites + 1 verification + 1 content fix + 7 observation + 4 research = 30 phases
> **Nguyên tắc:** Chậm mà chắc. Chất lượng cao nhất. Core quality → application quality.
> **v10.0 changes (từ v9.0):**
>   ① MERGE Phase 20b+20c → Phase 20b (core+inner files only)
>   ② DEFER research F1/F2 + 4-tier fixes sang Phase 28-31 (fix cùng content refine, tránh double-touching)
>   ③ CLEANUP §10/§12 stale content (Phase 8-19 ĐÃ DONE, Phase 20 scope THỰC TẾ)
> **FULL SCOPE (v9.0→v10.0):**
>   Tầng 5b: F1/F2 + 4-tier + WBK §refs — CORE FILES ONLY (Phase 20b, ~13 files)
>   Tầng 6: Observation parameter cascade (Phase 21-27, 14 files)
>   Tầng 7: Research/Application cascade + F1/F2/4-tier absorption (Phase 28-31, ~10 files)
>   Tổng ~35 files cần fix/refine. ~85 files OK. ~120 active files audited.

---

## §0 — TẠI SAO VIẾT MỚI TOÀN BỘ

### Drill tạo ra 8 nguyên tắc mới:
- ① Body-Need = 2-source aggregate (hardware + chunk dynamics)
- ② General-Purpose Reward (Architecture B — HOW not WHAT)
- ③ Social = Architecture Requirement (4 reasons, NOT luxury)
- ④ By-Product Match (B fill gap CỦA B → output match A → A reward)
- ⑤ 3 Independent Cost Sources (PFC draft + Suppress + Uncertainty)
- ⑥ Compiled vs Fresh = Real Axis (NOT Feeling/Logic content)
- ⑦ Input Channel Control = Power (5 channels)
- ⑧ Domain Reality = Final Arbiter (ALWAYS)

### Concepts mới chưa tồn tại trong framework:
- 5-Channel Input Vector model
- PFC = Lawyer not Judge
- Entity-Compiled reframe (positive/negative/mixed)
- 3-Layer Evolution model (hardware → compiled → cultural)
- Inter-Body Full Chain (detect → evaluate → extend → outcome → compile/dissolve)
- Body-Need 7 properties + 4 immediacy types

### Tại sao REWRITE thay vì refine?
- Insights lần này thay đổi CÁCH NHÌN nền tảng (2-source model, Compiled/Fresh axis)
- Refine nhỏ = bolted-on, inconsistent tone, thiếu narrative flow
- Viết mới = đảm bảo mỗi file internally coherent với bức tranh mới
- Files trung tâm ảnh hưởng 50+ files downstream → chất lượng gốc = quan trọng nhất
- Body-Base.md có L3 inconsistency phải fix → rewrite cho clean
- Agent-Mechanism.md vẫn DRAFT v1.0 → phải rewrite
- Các file khác (SPM, Resonance, Connection, BFM) = opportunity nâng cấp narrative flow

---

## §0b — REWRITE PRINCIPLES (rút từ Phase 1-2 thực tế)

> Nguyên tắc này áp dụng cho TẤT CẢ phases. Rút từ kinh nghiệm thực tế viết
> Phase 1 (Inter-Body-Mechanism.md) và Phase 2 (Body-Feedback-Mechanism.md v2.0).

### Nguyên tắc chất lượng

```
① QUALITY > BREVITY
   File nền tảng chấp nhận DÀI HƠN nếu chi tiết quan trọng.
   Chỉ bỏ dư thừa THẬT SỰ (lặp ý, tangential, verbose không thêm insight).
   KHÔNG bỏ vì "tiết kiệm lines" — framework này cần depth.
   Phase 2: v1.3 = 1,289L → v2.0 = 1,519L (tăng do thêm content MỚI, giữ core).

② 100% RESEARCH CITATIONS GIỮ NGUYÊN
   KHÔNG BAO GIỜ bỏ research citation.
   Citations = FOUNDATION — mỗi citation bỏ = mất trust.
   Kiểm tra: v_old research count = v_new research count (tối thiểu).
   Phase 2: 30+ citations v1.3 → 30+ citations v2.0 (100% preserved).

③ VÍ DỤ SIGNATURE GIỮ NGUYÊN
   Framework có "signature examples" (100k, Chị-A/B, Einstein, phản bội).
   Những ví dụ này = identity → GIỮ NGUYÊN hoặc NÂNG CẤP, không bỏ.
   Ví dụ mới THÊM VÀO bên cạnh, không THAY THẾ.

④ HONEST ASSESSMENT PHẢI UPDATE
   Mỗi rewrite: thêm 🟡 cho concepts mới, thêm ⚠ cho limitations mới.
   KHÔNG chỉ copy §assessment cũ — phải reflect nội dung v_new.
```

### Nguyên tắc quy trình

```
⑤ BACKUP TRƯỚC KHI VIẾT
   v_old → backup/filename-v_old-backup.md TRƯỚC KHI bắt đầu viết.
   Không bao giờ overwrite mà không backup.

⑥ ĐỌC KỸ TRƯỚC KHI VIẾT (multi-file)
   Đọc file hiện tại (v_old) TOÀN BỘ.
   Đọc TẤT CẢ files dependencies liên quan.
   Đọc drill sources (Architecture-Summary, Inter-Body §relevant).
   Đọc Framework-Label.md (vocabulary consistency).
   PHÂN TÍCH trước: đâu tốt, đâu thiếu, đâu thừa → rồi mới viết.

⑦ NEW CONTENT INTEGRATE ORGANIC
   Concepts mới KHÔNG bolted-on (thêm 1 block cuối file).
   Concepts mới PHẢI weave vào narrative flow tự nhiên.
   Ưu tiên: NEW section ở đúng vị trí logic > append cuối.
   Phase 2: §1 Body-Need (NEW) đặt TRƯỚC §2 2-sources → frames context.

⑧ STRUCTURE CÓ THỂ THAY ĐỔI
   Không cứng theo v_old structure.
   Merge sections nếu overlap (Phase 2: old §6+§7 → new §6).
   Split sections nếu quá dài (Phase 2: old §3.3 Gap → 4 sub-sections).
   Rename/reorder nếu narrative flow tốt hơn.

⑨ VIẾT SECTION-BY-SECTION
   Chia thành phases nhỏ: mỗi phase = 1-3 sections.
   Viết xong phase → review → tiếp phase sau.
   Cho phép đọc thêm files GIỮA các phases nếu cần.

⑩ CROSS-REFS PHẢI UPDATE
   Thêm Inter-Body-Mechanism.md ref (Phase 1 output).
   Update file version numbers trong cross-refs.
   Kiểm tra: mọi cross-ref trong v_old vẫn valid trong v_new.
```

### Checklist per file (áp dụng trước + sau mỗi rewrite)

```
TRƯỚC VIẾT:
  □ Đã backup v_old?
  □ Đã đọc v_old toàn bộ?
  □ Đã đọc dependencies liên quan?
  □ Đã đọc drill sources cho file này?
  □ Đã phân tích: đâu tốt / đâu thiếu / đâu thừa?
  □ Đã xác định structure v_new?

SAU VIẾT:
  □ ALL research citations từ v_old preserved?
  □ ALL signature examples preserved?
  □ NEW content integrate organic (không bolted-on)?
  □ Honest Assessment updated?
  □ Cross-refs updated (incl. Inter-Body ref)?
  □ Vocabulary consistent với Framework-Label.md v3.0?
  □ Changelog ở cuối file rõ ràng?
```

---

## §1 — DEPENDENCY CHAIN + THỨ TỰ VIẾT (v5.0 EXPANDED)

> **v5.0 mở rộng:** Rà soát 2026-05-17 phát hiện 10 file core CẦN REWRITE.
> v4.0 = 8 files. v5.0 += Logic-Feeling-Balance v2.0 + Neural-Processing-Flow v2.0.
> Files core = nền tảng framework, ảnh hưởng trực tiếp chất lượng mở rộng.
> Refine nhỏ = bolted-on. Rewrite = internally coherent.
> Mỗi file xứng đáng 1 session riêng, đầu tư hết năng lực.

```
THỨ TỰ VIẾT (từ foundation lên, 20 phases, 5 tầng):

═══════════════════════════════════════════════════════
  TẦNG 0: DRILL SOURCE-OF-TRUTH (Phase 1-3) ✅ DONE
═══════════════════════════════════════════════════════

  Phase 1: Inter-Body-Mechanism.md (NEW)          ✅ DONE (1,500L)
    ↓ source-of-truth cho drill insights mới

  Phase 2: Body-Feedback-Mechanism.md v2.0        ✅ DONE (1,519L)
    ↓ nền tảng chunk dynamics + 2-source + Body-Need aggregate

  Phase 3: Valence-Propagation.md v2.0            ✅ DONE (1,871L)
    ↓ defines L1/L2, per-entity valence, Entity-Compiled

═══════════════════════════════════════════════════════
  TẦNG 0b: CORE MECHANISM REWRITE (Phase 4-7) ✅ DONE
═══════════════════════════════════════════════════════

  Phase 4: Body-Base.md v3.0→v3.1                  ✅ DONE (1,297L)
    ↓ entry point, L3 fix, 3 foundations, Architecture B
    ↓ v3.1: §7 REWRITE 4-Tier→2-Tier+2-Pathway (Why-Body-Knows v1.1)

  Phase 5: Body-Coupling.md v2.0                  ✅ DONE (1,544L)
    ↓ coupling mechanism, Entity-Compiled subtypes, MIXED

  Phase 6: SPM v3.0                               ✅ DONE (2,614L)
    ↓ core mechanism, Compiled/Fresh reframe

  Phase 7: Resonance v3.1                 ✅ DONE (1,540L)
    ↓ 2-Stream Architecture, by-product match, mutual

═══════════════════════════════════════════════════════
  TẦNG 1: BODY-FEEDBACK FOLDER REBUILD (Phase 8-11)
  Vocabulary anchor + mechanism + synthesis
═══════════════════════════════════════════════════════

  Phase 8: Framework-Label v2.0               ✅ DONE (1,118L)
    ↓ VOCABULARY ANCHOR — formalizes ALL new terms
    ↓ +§2 Foundation (body-need, gap, gap direction, drive, body-feedback)
    ↓ +Entity-Compiled subtypes, +Compiled/Fresh labels
    ↓ +By-product match/anti-match, +2-Stream, +3-cost, +5-Channel
    ↓ Dependencies: BFM v2.0 ✅, VP v2.0 ✅, Inter-Body ✅

  Phase 9: Gap-Direction v2.0                     ✅ DONE (2,681L)
    ↓ Gap direction = core cho by-product match
    ↓ +§1.4 By-product match, +§5.5 Compiled/Fresh, +§12 Inter-Body NEW
    ↓ +2-Stream connection, +Architecture B, +3-cost, +5-Channel
    ↓ Dependencies: BFM v2.0 ✅, Label v2.0 ✅

  Phase 10: Reward-Signal-Architecture v2.0       ✅ DONE (1,986L)
    ↓ +§0.3 Architecture B connection (WHY Type A complex)
    ↓ +§1.7 Compiled/Fresh × A₀→A₃ mapping
    ↓ +§2.3 compilation depth note, +§8.1 domain verification
    ↓ +§11.2 new 🟡 items, +§12 cross-refs updated (Phase 1-9)
    ↓ Dependencies: BFM v2.0 ✅, Gap-Direction v2.0 ✅

  Phase 11: Body-Feedback.md v2.0                 ✅ DONE (892L)
    ↓ Entry point synthesis — folder 6→10 files, ~16,500L
    ↓ +§1.1 complete listing, +§1.2 3-tier reading guide
    ↓ +§1.3 Architecture B framing, +Compiled/Fresh, +domain arbiter
    ↓ +§6 H10×Type A/B, +§9 expanded, +§10 Phase 1-10 cross-refs
    ↓ Dependencies: Label v2.0 ✅, Gap v2.0 ✅, RSA v2.0 ✅

═══════════════════════════════════════════════════════
  TẦNG 2: PROCESSING & OBSERVATION (Phase 12-15)
  Central reference + processing modes + hardware flow
═══════════════════════════════════════════════════════

  Phase 12: Feeling.md v3.0                       ✅ DONE (2,122L)
    ↓ +§0 Architecture B connection (WHY feeling = general-purpose)
    ↓ +§2.3 Layer 7 PFC=Lawyer (structural bias, Gazzaniga+Haidt)
    ↓ +§2.5 NEW Compiled/Fresh × 7-Layer mapping (compilation = real axis)
    ↓ +§3.4 NEW PFC=Lawyer formal section (3 research citations added)
    ↓ +§5.2 Body-Need 2-source aggregate framing
    ↓ +§6.5 RSA v2.0 + Architecture B cross-ref
    ↓ +§8.3 Domain=Arbiter formal + Dual Check
    ↓ +§12 (24🟢+21🟡+8🔴), +§13 Inter-Body+BF sections
    ↓ Dependencies: RSA v2.0 ✅, BFM v2.0 ✅, Inter-Body v1.0 ✅

  Phase 13: Logic-Feeling v2.0                    ✅ DONE (1,572L)
    ↓ ★★★ MOST DRILL IMPACT — FULL REWRITE
    ↓ §1 NEW: Compiled/Fresh = primary axis (6 sub-sections)
    ↓ §2 NEW: Logic/Feeling = observer labels (shareability-based)
    ↓ §3 REFRAME: +3-cost, +Dual Check, +1B danger
    ↓ §4 RENAME: Compiled Anchor ↔ Fresh Explore, +Domain verify
    ↓ §5: +Case 6 "1B trap: overprotected child" (drilled 2026-05-17)
    ↓ §6-§8: preserved (parallel, modality, object-agent 5 sub-cases)
    ↓ +PFC=Lawyer, +Domain=Arbiter, +Shareable/Non-shareable
    ↓ 19 research citations. Einstein Hadamard preserved.
    ↓ Dependencies: Inter-Body §3 ✅, Feeling v3.0 ✅

  Phase 14: Logic-Feeling-Balance v2.0            ✅ DONE (1,612L)
    ↓ §0.2 NEW: Compiled/Fresh reframe note
    ↓ §1.1: Updated terminology (Compiled/Fresh)
    ↓ §1.2: +Architecture B (WHY uncertainty structural)
    ↓ §1.4 NEW: "Balance = Compiled×Domain cycle" (drill ⑧ RESOLVED)
    ↓ §3.2: +1B trap explicit (overprotected child, echo chamber)
    ↓ §10: ELEVATED — drill ⑧ formal, PFC=Lawyer, Dual Check
    ↓ §12: +3🟢 +6🟡, §14: cross-refs updated
    ↓ ALL philosophical content preserved (§2-§9, §11)
    ↓ Dependencies: Logic-Feeling v2.0 ✅, Inter-Body v1.0 ✅

  Phase 15: Neural-Processing-Flow v2.0           ✅ DONE (1,270L)
    ↓ §0: +Architecture B (WHY this hardware = general-purpose)
    ↓ §5.5 NEW: Compiled/Fresh PHYSICAL level (LTP+myelin=fast, novel=slow)
    ↓ §6.1: +PFC=Lawyer elevated (Gazzaniga+Haidt+Nisbett&Wilson)
    ↓ §8.3: +5-Channel Input Vector mapping
    ↓ §10.3 FIX: "L3 operators" → "Observation parameters" (v7.8)
    ↓ §11: +6🟢 +5🟡, §12 NEW cross-refs, §13 status
    ↓ ALL hardware content preserved (35+6=41 citations)
    ↓ Dependencies: Feeling v3.0 ✅, Logic-Feeling v2.0 ✅, Inter-Body ✅

═══════════════════════════════════════════════════════
  TẦNG 3: INTEGRATION HUB (Phase 16-17)
  Integration + observation parameter
═══════════════════════════════════════════════════════

  Phase 16: Agent-Mechanism v2.0               ✅ DONE (1,956L)
    ↓ Integration hub — FULL REWRITE from DRAFT v1.0 (2,690L → 1,956L)
    ↓ §5 SPM preview: F1=Compiled, F2=Fresh (not Feeling/Logic)
    ↓ §6 Resonance preview: 2-Stream Architecture, by-product match, SPM NOT required
    ↓ +Architecture B (§0.2, §2.6, §3.4, §11.4, §12.1b, §13.1)
    ↓ +PFC=Lawyer §3.6, +3-cost §5.3+§12.4, +Domain=Arbiter throughout
    ↓ +Compiled/Fresh §3.2+§5.2+§7.5, +2-Stream §6.2+§9.1
    ↓ 28+ citations (ALL preserved + 8 added). 18 gradient cases.
    ↓ Dependencies: SPM v3.0 ✅, Resonance v3.1 ✅, VP v2.0 ✅, BC v2.0 ✅

  Phase 17: Connection v4.0                    ✅ DONE (2,324L)
    ↓ SURGICAL upgrade from v3.3 (2,004L → 2,324L, +320L)
    ↓ §0.0b NEW: Architecture B — Social = Requirement (4 reasons)
    ↓ §3.1: +2-source social need (hardware + compiled baseline)
    ↓ §3.2: +Compiled/Fresh terminology (F1=Compiled, F2=Fresh)
    ↓ §4.2 ★ REWRITTEN: 2-Stream Architecture, by-product match,
      anti-match, per-pair topology, conditions broadened, PFC=Lawyer
    ↓ §4.3: +3-cost model (3 independent sources)
    ↓ §10.2: +3-cost explains trục ③
    ↓ §11: +5-Channel Input Vector
    ↓ §16.5: +PFC=Lawyer (mask/amplify/mislabel) + Domain=Arbiter
    ↓ §17: +6🟢 +13🟡 +1🔴. §18: ALL versions updated
    ↓ ALL 22+ original citations preserved + 6 new added
    ↓ Dependencies: Agent v2.0 ✅, SPM v3.0 ✅, Resonance v3.1 ✅

═══════════════════════════════════════════════════════
  TẦNG 4: META & COLLECTIVE (Phase 18-19)
  User bổ sung insights, cần foundation stable
═══════════════════════════════════════════════════════

  Phase 18: Why-Body-Knows v1.0→v1.1                ✅ DONE (1,273L)
    ↓ META FOUNDATION — FULL REWRITE from DRAFT (411L → 958L)
    ↓ §0: Thesis + Architecture B (WHY calibration needed)
    ↓ §1: Coherence evaluation + Type A₀→A₃ + H10 + Compiled/Fresh + PFC=Lawyer
    ↓ §2: Music signature case (ALL 7 citations preserved + terminology fixed)
    ↓ §3: 4-tầng calibration + 3-Layer Evolution reconciliation + Social accelerator
    ↓ §4 NEW: Compiled/Fresh = "biết" (Shareable/Non-shareable, Expert=compiled)
    ↓ §5 NEW: Vòng Tròn formalized (spiral not circular, bootstrap, grounding)
    ↓ §6: 3 failure modes + PFC=Lawyer + Dual Check (4-case matrix)
      + Circuit Breaker + AI amplification risk
    ↓ §7 NEW: Architecture B connection (meta-explanation)
    ↓ §8: 19🟢 + 12🟡 + 4🔴. §9: ALL versions updated
    ↓ 19 research citations (7 preserved + 12 added)
    ↓ Dependencies: RSA v2.0 ✅, Body-Base v3.0 ✅, Inter-Body ✅

  Phase 19: Collective-Body v2.0                   ✅ DONE (1,651L)
    ↓ SURGICAL upgrade from v1.2 (1,389L → 1,651L, +262L)
    ↓ §0: +Architecture B (WHY collective = requirement, 4 reasons)
    ↓ §2.5 ★★ NEW: "Cá Nhân Detect Collective Gap" (~120L)
      Gap-direction × collective data → match → "opportunity detected"
      4 cases: Einstein (conflict), Huang (30yr), học sinh (trust proxy), người đi làm
      Threshold→rush→saturate. "Visionary=compiled deeper." "Đam mê=gap formed."
    ↓ §3.1: +By-product match at collective scale
    ↓ §5.1: +PFC=Lawyer at collective + Domain=Arbiter
    ↓ §9: +8🟡 +1🔴. §10: ALL versions updated + changelog
    ↓ ALL 18+ citations preserved + 2 new added
    ↓ Dependencies: Connection v4.0 ✅, Body-Base v3.0 ✅, Gap-Direction v2.0 ✅

═══════════════════════════════════════════════════════
  TẦNG 5: VERIFICATION (Phase 20)
  Terminology propagation + cross-check
═══════════════════════════════════════════════════════

  Phase 20: Terminology propagation + verification     ✅ DONE
    ↓ ✅ Cross-ref audit: 19 files checked, issues found + fixed
    ↓ ✅ 4-tier → 2-tầng: LFB v2.1, BF v2.0a, Collective-Body, 01-File-Index
    ↓ ✅ Stale versions fixed: ~50+ refs across 12 files
    ↓ ✅ Body-Base v3.0→v3.1 propagated to ALL active files
    ↓ ✅ Why-Body-Knows v1.0→v1.1 propagated
    ↓ ✅ 4-tier→2-tầng CONTENT FIX (28 edits, 7 files):
    ↓    Cortisol-Baseline §1.3 REWRITE (2-tầng+2-đường model chi tiết)
    ↓    + AI-Schema-Detection (2), 01-Foundation §4 full reframe (14),
    ↓    + 03-Reward §6.5 Van Gogh (1), 04-Integration H10 (1),
    ↓    + 00-Chunk-System-Sketch EN+VI (2)
    ↓ ✅ Full framework audit: ~120 active files assessed
    ↓    → 14 observation files cần Tầng 6 cascade (below)
    ↓    → ~85 files OK (scope independent, no changes needed)
    ↓ NOTE: Version refs trong non-rewritten files = deferred (không ảnh hưởng nội dung)

═══════════════════════════════════════════════════════
  TẦNG 5b: CONTENT FIX — CORE + INNER FILES (Phase 20b)
  v10.0: MERGED 20b+20c, deferred research fixes sang Tầng 7
═══════════════════════════════════════════════════════

  Phase 20b: F1/F2 + 4-tier + WBK §refs + Entity-compiled   ✅ DONE (2026-05-17)
    ↓ ✅ F1/F2 mechanism label: 4 core files ALREADY CLEAN (fixed in Phase 6-17)
    ↓ ✅ 4-tier→2-tầng: Ask-AI L661 fixed (only stale instance found)
    ↓   Core-Software, Natural-Dev, Child-Dev-Mechanism = already clean
    ↓ ✅ WBK §refs: ALL 8 files already correct (§3, §6) — fixed in earlier phases
    ↓ ✅ Entity-owned → Entity-compiled: 14 stale instances across 10 files
    ↓   Connection v4.0 (2), Agent-Mechanism v2.0 (2+F1 label fix),
    ↓   Core-Software (1), Compliance-Floor (2), Love-Unified (1),
    ↓   Religion (1), Idol (2), Money-Analysis (1), 01-File-Index (1),
    ↓   Addiction-Analysis (1)
    ↓ ✅ Verification: "Entity-owned" as mechanism label = ZERO in active files

═══════════════════════════════════════════════════════
  TẦNG 6: OBSERVATION LAYER CASCADE (Phase 21-27)
  Drill insights → observation parameter files
═══════════════════════════════════════════════════════

  Phase 21: Empathy.md v2.1→v3.0               ✅ DONE (2026-05-17)
    ↓ Highest-impact observation. +2-Stream, +by-product match,
    ↓ +Architecture B, +PFC=Lawyer, +Domain=Arbiter
    ↓ Dependencies: Connection v4.0 ✅, Resonance v3.1 ✅, SPM v3.0 ✅

  Phase 22: Gratitude.md v1.1→v2.0              ✅ DONE (2026-05-17)
    ↓ Highest-integration (9 components). +Architecture B,
    ↓ +by-product match, +PFC=Lawyer, +2-tầng, +Domain=Arbiter
    ↓ Dependencies: Connection v4.0 ✅, Empathy (P21)

  Phase 23: Obligation.md v1.0→v1.1             ✅ DONE (2026-05-17)
    ↓ Exchange = by-product match core case.
    ↓ +by-product match, +Architecture B, +PFC=Lawyer
    ↓ Dependencies: Status v2.0, Gratitude (P22)

  Phase 24: Status.md v2.0→v2.1                 ✅ DONE (2026-05-17)
    ↓ Status = resource access map trong general-purpose system.
    ↓ +Architecture B, +Compiled/Fresh, +PFC=Lawyer
    ↓ Dependencies: Agent-Mechanism v2.0 ✅

  Phase 25: Drive+Novelty+Threat v1.1 (triple)  ✅ DONE (2026-05-17)
    ↓ Drive +78L, Novelty +73L, Threat +103L (total +254L)
    ↓ +Architecture B, +Compiled/Fresh, +PFC=Lawyer(Threat), +Domain=Arbiter(Drive), +2-tầng(Novelty)
    ↓ Dependencies: BFM v2.0 ✅, Feeling v3.0 ✅

  Phase 26: Protect+Meaning+Boredom v1.1/v2.1    ✅ DONE (2026-05-17)
    ↓ Protect +85L, Meaning +84L, Boredom +63L (total +232L)
    ↓ +Architecture B (all 3), +Compiled/Fresh (Protect+Boredom), +Domain=Arbiter (Meaning)
    ↓ Agent.md→Agent-Mechanism.md (Protect), version refs updated (all 3)

  Phase 27: Autonomy.md + Autonomy-Hardware.md   ✅ DONE (2026-05-17)
    ↓ Autonomy +24L, AH +21L (total +45L)
    ↓ +Architecture B (both), +IBM/BFL cross-refs, Agent.md→Agent-Mechanism.md (Autonomy)
    ↓ Observation versions updated

═══════════════════════════════════════════════════════
  TẦNG 7: RESEARCH/APPLICATION CASCADE (Phase 28-31)
  Core insights → research + application files
  v10.0: HẤP THỤ F1/F2 + 4-tier fixes từ cũ Phase 20b/20c
═══════════════════════════════════════════════════════

  Phase 28: Love-Romantic.md v2.3→v2.4          ✅ DONE (2026-05-17)
    ↓ F1/F2 label fix (L86, L547) + Compiled/Fresh note + Entity-Compiled (3 refs)
    ↓ +§3.2b 2-Stream Resonance model × love (~50L: table + 4 hướng reinterpretation)
    ↓ +§5.1 PFC=Lawyer (~20L: biện hộ + compound mechanism)
    ↓ +by-product match language woven into 2-Stream
    ↓ Dependencies ~20 files updated + cross-refs §14 refreshed
    ↓ Resonance section refs fixed (§7.8→§5, §7.9→§10, §6.4→§8, §7.10→§3)
    ↓ +4🟡 Honest Assessment. Total ~+120L.

  Phase 29: Uncanny-Valley.md v1.0→v1.1         ✅ DONE (2026-05-17)
    ↓ F1/F2 label fix (7 occurrences: L96-97, L319, L328, L341, L1006-1007)
    ↓ +§2.2 Compiled/Fresh terminology note block (~10L)
    ↓ Dependencies 10 files updated (SPM v3.0, BFM v2.0, Connection v4.0, VP v2.0, etc.)
    ↓ +Inter-Body-Mechanism.md v1.0 as DRILL SOURCE
    ↓ §10 cross-refs: all version numbers added/updated + DRILL SOURCE block
    ↓ +1🟡 Honest Assessment (Compiled/Fresh reframe)
    ↓ Closing quote updated with F1/F2 Compiled/Fresh language
    ↓ Total ~+54L.

  Phase 30: Social-Calibration.md + AI-Self-Model.md  ✅ DONE (2026-05-17)
    ↓ Social-Cal v1.0→v1.1: F1/F2 fix (L679) + 4-tier→2-Tier+2-Pathway (5 blocks)
    ↓ + 11 dep versions updated + DRILL SOURCE block + +1🟡 + changelog
    ↓ AI-SM v2.0→v2.1: Body-Base §6→§7 (8 refs) + 4-tier→2-Tier content rewrite
    ↓ Total: ~50L added across both files

  Phase 31: Remaining Research refines            ✅ DONE (2026-05-17)
    ↓ Love-Unified v1.2, Religion v2.4, Idol v2.2, Alzheimer v1.2, OCD fix
    ↓ F1/F2 fix + entity-compiled + VP §shift + 11 dep versions + Love-Romantic rename
```

### Tại sao thứ tự này?

**Bottom-up 5 tầng:** mỗi file khi viết, foundation ĐÃ hoàn thành.

- **Tầng 0 (Phase 1-7) ✅**: Drill source-of-truth + core mechanism rewrites
- **Tầng 1 — Label TRƯỚC NHẤT (Phase 8)**: Vocabulary anchor. Phase 1-7 đã define
  ALL new concepts → Label formalize tên gọi → MỌI file sau consistent.
- **Gap-Direction trước RSA (Phase 9→10)**: Gap direction = core cho by-product match.
  RSA references gap direction.
- **RSA trước Body-Feedback (Phase 10→11)**: RSA define Type A/B → Body-Feedback
  entry point references. User insight "Type B→A development" fit RSA.
- **Body-Feedback cuối folder (Phase 11)**: Entry point synthesis — cần TẤT CẢ files
  trong folder done.
- **Tầng 2 — Feeling → Logic-Feeling → Balance → NPF (Phase 12→15)**:
  Feeling v3.0 trước (central reference). Logic-Feeling v2.0 depends on Feeling
  (Compiled/Fresh reframe = MOST drill impact). Balance v2.0 = companion SAU LF
  (+hướng calibrate = domain feedback). NPF v2.0 = hardware flow cuối tầng
  (capture ALL processing understanding, Architecture B at hardware level).
- **Tầng 3 — Agent-Mechanism trước Connection (Phase 16→17)**: Connection references
  Agent-Mechanism. Agent = integration hub, cần all mechanism files ready.
- **Tầng 4 — Meta files cuối (Phase 18-19)**: Why-Body-Knows + Collective-Body = meta
  files. User cần thời gian phân tích + bổ sung insights. Foundation phải stable.
- **Tầng 5 — Verification cuối cùng (Phase 20)**: terminology propagation + full framework audit
- **Tầng 5b — Content fix CORE files (Phase 20b)**: F1/F2 + 4-tier + WBK §refs. v10.0: merged 20b+20c,
  research file fixes deferred sang Tầng 7 (tránh double-touching)
- **Tầng 6 — Observation Layer Cascade (Phase 21-27)**: drill insights → observation files
- **Tầng 7 — Research/App Cascade (Phase 28-31)**: content refine + hấp thụ F1/F2 + 4-tier fixes

---

## §1b — TẠI SAO TẦNG 6 (v8.0 audit findings)

### Phát hiện từ full framework audit (2026-05-17)

```
AUDIT ~120 active files → 3 nhóm rõ ràng:

  ① 19 MECHANISM FILES (Phase 1-19) = ✅ CHẤT LƯỢNG CAO
     Tích hợp ĐẦY ĐỦ: Architecture B, Compiled/Fresh, PFC=Lawyer,
     by-product match, 2-Stream, 2-tầng, Domain=Arbiter, Entity-Compiled,
     5-Channel Input Vector.

  ② 14 OBSERVATION FILES = 🔴🟡 THIẾU DRILL INSIGHTS
     Viết trước drill session (2026-04-18 → 2026-04-25).
     Zero hoặc gần-zero new concepts.
     Reader đọc Connection v4.0 → đọc Empathy v2.1 = THẤY INCONSISTENCY.

  ③ ~85 FILES = ⚪ OK (scope independent)
     Schema, Feeling sub-files, Melody Lens, PFC hardware,
     Clarification, Domain, Child-Chunk-Dev, Chunk-Internal/External.
     Scope KHÔNG overlap drill insights → KHÔNG CẦN thay đổi.

INSIGHT THEN CHỐT:
  Mechanism layer = NỀN TẢNG → đã rewrite.
  Observation layer = NƠI READER GẶP FRAMEWORK → chưa cascade.
  → Tầng 6 = cascade drill insights sang observation files.
```

### Nguyên tắc Tầng 6

```
① REFINE, KHÔNG REWRITE (trừ Empathy + Gratitude)
   Observation files core framing ĐÃ ĐÚNG. Cần THÊM concepts, KHÔNG xây lại.
   Empathy + Gratitude = exceptions (nhiều concepts → cần restructure).

② SURGICAL ADDITIONS
   Mỗi file: thêm 1-3 sections MỚI + enrich 2-3 sections CŨ.
   KHÔNG rewrite sections đã tốt. KHÔNG thay đổi structure trừ khi cần.

③ CONCEPTS THEO PRIORITY
   Mỗi observation file KHÔNG CẦN tất cả 9 concepts.
   Chỉ integrate concepts RELEVANT cho scope của file đó:
     Empathy: 2-Stream + by-product + PFC=Lawyer + Arch-B + Domain-Arbiter
     Status:  Arch-B + Compiled/Fresh + PFC=Lawyer
     Boredom: Arch-B + Compiled/Fresh (light)

④ MUST PRESERVE
   100% research citations. ALL signature examples.
   Honest Assessment UPDATE. Cross-refs UPDATE.
```

---

## §2 — PHASE 1: Inter-Body-Mechanism.md (NEW ~1,500L)

### Vai trò
- File MỚI — source-of-truth cho toàn bộ drill insights
- "Missing file" mà framework ngầm hiểu nhưng chưa formalize
- Các files khác cross-ref tới file này cho concepts mới (5-channel, 3-cost, PFC=Lawyer...)

### Location
`Core-Deep-Dive/Body-Base/Drill-Inter-Body-Mechanism/Inter-Body-Mechanism.md`

### Content structure (~1,500L)
```
HEADER + OPENING QUOTE (~60L)

§0 — THESIS + POSITION (~80L)
  WHY 2+ body-bases interact. Position: mechanism file.

§1 — 3 NỀN TẢNG HARDWARE (~120L)
  ① General-Purpose Reward  ② Compilation  ③ Social Hardware
  → Architecture B = combination. Research citations.

§2 — BODY-NEED: 2-Source Aggregate (~130L)
  Hardware/Sensory + Chunk Dynamics. Complexity spectrum.
  Cross-cutting: Observation Params + State Modifiers.
  7 properties. 4 immediacy types.

§3 — COMPILED vs FRESH: Real Axis (~100L)
  NOT Feeling/Logic → Compilation Level.
  Transition both ways. "Logic" = observer label.

§4 — 3 INDEPENDENT COST SOURCES (~100L)
  ① PFC Draft  ② Suppress  ③ Uncertainty.
  Sustainability = f(cost × freq ÷ reward).

§5 — INTER-BODY FULL CHAIN (~150L)
  Detect → Evaluate → Extend → Outcome → Compile/Dissolve.
  By-Product Match principle. Entry points.

§6 — 5-CHANNEL INPUT VECTOR (~120L)
  Ch1-Ch5. Dominant → direction. Absent → vulnerability.
  INPUT CHANNEL CONTROL = POWER.

§7 — PFC = LAWYER not Judge (~80L)
  Narrative AFTER body-need. Accuracy spectrum.
  Both PFCs lawyering in interaction.

§8 — ENTITY-COMPILED (~100L)
  Reframe Entity-Owned → Entity-Compiled.
  3 subtypes. Entity-Compiled vs Obligation = independent.

§9 — 3-LAYER EVOLUTION (~100L)
  Hardware / Compiled / Cultural. Boost features. Money = bridge.

§10 — HUMAN ↔ AI (~60L)
  Current: tool. Amplifier đúng/sai. Dual Check. Future: speculative.

§11 — HONEST ASSESSMENT (~100L)
  🟢 13 items. 🟡 14 items. 🔴 7 items.

§12 — CROSS-REFERENCES + RESEARCH (~100L)
  Full citation table (~20 citations).
```

### Must read: Architecture-Summary v1.1 ✅, Drill v1.6 ✅, BFM v1.3 ✅, Body-Coupling v1.1 ✅
### Must preserve: ALL research citations from Architecture-Summary §XVI

---

## §3 — PHASE 2: Body-Feedback-Mechanism v1.3 → v2.0 REWRITE (~1,000L)

### Tại sao viết mới?
- File nền tảng: defines 2-source model + 3 chunk dynamics → 20+ files reference
- v1.3 đã solid nhưng THIẾU: Body-Need aggregate, complexity spectrum, cross-cutting clarification
- Rewrite = opportunity tích hợp organic thay vì bolted-on sections

### Key changes v1.3 → v2.0
1. **Body-Need aggregate concept** (NEW section): 7 properties, 4 immediacy types, PFC không luôn biết
2. **Complexity spectrum** within chunk dynamics: Simple → Social → Meta (cùng mechanism, khác substrate)
3. **Cross-cutting clarification**: Observation parameters + State modifiers = NOT sources
4. **Tầng ③ collapse**: Imagine-Final, Obligation, Identity, Status = cùng Gap/Miss/Shift, khác substrate level
5. Updated cross-refs to Inter-Body-Mechanism.md

### Must preserve from v1.3
- §2 2-source model (Sensory-Driven / Pattern-Driven) — EXPAND, not replace
- §3 3 chunk dynamics (Shift/Miss/Gap) — keep core, add complexity spectrum
- §4 Compound mechanism — keep
- §5 Quality Baseline Shift — keep
- §8 Research anchors (Crespi 1942, Schultz 1997, Berridge 2003, Amsel, Flaherty 1996) — ALL preserved
- §9 Honest assessment — update with new 🟡 items

### Must read before writing
- BFM v1.3 full file (~850L) ✅ partially read
- Architecture-Summary §II (2-source model refined)
- Drill §13 (Body-Need source taxonomy refinement)
- Framework-Label.md v3.0 (vocabulary consistency)

---

## §3b — PHASE 3: Valence-Propagation v1.4 → v2.0 REWRITE (~1,400L) ★ NEW

### Tại sao viết mới?
- Defines L1/L2 distinction → SPM, Connection, Empathy, Agent-Mechanism ALL reference VP
- "Entity-Owned" → "Entity-Compiled" = NOT just terminology — CONCEPTUAL change:
  - v1.4: L2 = "Entity-Owned" (implies only positive)
  - v2.0: L2 = "Entity-Compiled" = 3 subtypes (positive/negative/mixed)
  - Mixed = MOST COMMON (drill §11.10) → VP must define this
- Structural issues: §5b bolted-on, §2↔§4 discontinuity → rewrite for clean narrative
- VP defines vocabulary that 20+ files use → source must be highest quality

### Key changes v1.4 → v2.0
1. **L2 reframe**: "Entity-Owned" → "Entity-Compiled" throughout
   - NEW: 3 subtypes (positive-dominant, negative-dominant, mixed)
   - Mixed = most common (càng gần lâu → càng nhiều channels cả + và -)
   - "Vừa thương vừa giận" = NORMAL, not pathological
2. **§2 Body-Base Extension REWRITE**: integrate Entity-Compiled subtypes organically
3. **§4-§5 Propagation RESTRUCTURE**: merge §5b into §5 cleanly (remove bolted-on feel)
4. **3-cost annotation**: valence propagation has cost implications (PFC draft for novel chains)
5. **Cross-ref updates**: VP → Body-Coupling v2.0 (mechanism), Inter-Body §8 (Entity-Compiled)
6. **Narrative flow**: WHY valence exists → HOW per-entity → HOW propagates → CASES

### Must preserve from v1.4
- §1 Per-entity valence system — keep core
- §2 Body-Base Extension dimension — keep + EXPAND with Entity-Compiled
- §3 Valence flip mechanism — keep
- §6 Case analyses (Miep Gies etc.) — keep ALL (excellent quality)
- §7 PFC Blindness — keep
- ALL research citations
- 2-luồng model (L1/L2) — keep mechanism, UPDATE terminology

### Must read before writing
- VP v1.4 full file (~1,600L)
- Inter-Body §8 (Entity-Compiled)
- Body-Coupling v1.1 (current, for overlap check)
- Drill §11.10 (Entity-Compiled detail) + §11.11 (mixed valence case)

---

## §4 — PHASE 4: Body-Base.md v2.1 → v3.0 REWRITE (~2,200L)

### Tại sao viết mới?
- ENTRY POINT cho toàn bộ framework (~60+ files) → chất lượng CỰC quan trọng
- L3 inconsistency (Protect = "operator" ≠ "observation parameter") → phải fix structural
- Missing: 2-source body-need model, 3 hardware foundations, Architecture B
- v2.1 structure (§0-§11) mostly solid nhưng §0 + §1.2 cần rewrite → better rewrite whole

### Key changes v2.1 → v3.0
1. **§0 Layer stack FIX**: Remove "L3 Novelty/Status/Protect (operators)" → reframe
   - Protect = observation parameter (cross-cutting), NOT operator
   - Novelty/Status = PFC-mediated drives (keep as "operators" nhưng Protect removed)
2. **§1.2 L3 REWRITE**: Clarify what L3 actually is post-drill
3. **NEW: 3 Hardware Foundations** (General-Purpose Reward, Compilation, Social Hardware)
4. **NEW: Architecture B framing** (humans = general-purpose, trade-off = long childhood)
5. **NEW: Body-Need 2-source model** (brief, reference BFM v2.0 + Inter-Body §2)
6. **Compiled/Fresh axis note** (reference Inter-Body §3)
7. Updated cross-refs to all new file versions

### Must preserve from v2.1
- §2 Core Principle: Body Evaluates Patterns, Not Reality — keep (strong, Drill §21)
- §3 Unified Model 3+1 (Vô thức/PFC/Trust/External) — keep (Drill §23)
- §4 Body Compile (PFC=Director, Body=Compiler) — keep + enhance
- §5 L0-L1 detailed (17 inputs, 3 nhóm) — keep
- §6 4-Tier Calibration — keep
- §7 Circuit Breaker — keep
- All research citations (Treisman 1977, Berridge 2003, Damasio 1994, etc.)

### Must read before writing
- Body-Base.md full file (~2,000L)
- Protect.md §0 (confirm observation parameter)
- BFM v2.0 (by then complete)
- Inter-Body-Mechanism.md (by then complete)

---

## §4b — PHASE 5: Body-Coupling v1.1 → v2.0 REWRITE (~1,600L) ★ NEW

### Tại sao viết mới?
- Defines HOW body deeply couples with entities → Agent-Mechanism, Connection, Love files reference
- Entity-Compiled subtypes maps DIRECTLY to coupling outcomes:
  - Extension = positive-compiled
  - Entanglement = negative-compiled  
  - Mixed coupling = MISSING in v1.1 (currently only Extension/Entanglement/Neutral)
- "Mixed" = MOST COMMON outcome (drill §11.10) → v1.1 THIẾU analysis quan trọng nhất
- VP v2.0 will redefine Entity-Compiled → Body-Coupling must match
- 2D model (Depth×Direction) = excellent foundation → rewrite PRESERVES and ENRICHES

### Key changes v1.1 → v2.0
1. **Mixed coupling = NEW major outcome**: Not just Extension/Entanglement/Neutral
   - Per-CHANNEL valence profile (positive on some, negative on others)
   - "Vừa thương vừa giận mẹ" = normal multi-channel compile (drill §11.11)
   - Oscillation by state/context → NOT flip-flop
   - Developmental complexity gradient: trẻ simpler → adult maximum mixed
2. **Entity-Compiled terminology**: consistent with VP v2.0
3. **2D model EXTENDED**: Depth × Direction + Channel complexity dimension
4. **Loss dynamics for MIXED coupling**: Complex grief (relief + pain simultaneously)
   - Currently §6 covers loss → ADD mixed-loss as distinct pattern
5. **Parent-child coupling trajectory**: Con 0-5 (①positive) → 5-12 (③mixed emerge) → Adolescence (③peak) → Adult (possible ①shift)
6. **Cross-refs**: VP v2.0, Inter-Body §8, Agent-Mechanism v2.0

### Must preserve from v1.1
- §2 2D Model (Depth × Direction) — keep, EXTEND
- §3 3 Phase Model — keep (strong)
- §4-§6 Dynamics (deepen/weaken/collapse/shift/loss) — keep + enrich with mixed
- §2.5 System Compilation (6 mechanisms) — keep (novel)
- Compile_rate: |peak_valence| insight — keep
- Smoothing + Anti-Smoothing — keep
- ALL research citations + folk wisdom unification
- "Trống Rỗng" 7-component model (§6.8) — keep (excellent)

### Must read before writing
- Body-Coupling v1.1 full file (~1,534L)
- VP v2.0 (by then complete — Entity-Compiled defined)
- Inter-Body §8 (Entity-Compiled overview)
- Drill §11.10-§11.11 (Entity-Compiled detail + vợ chồng mixed case)
- Love-Unified v1.1 (observation companion — check overlap)

---

## §5 — PHASE 6: SPM v2.4 → v3.0 REWRITE (~2,000L)

### Tại sao viết mới?
- Core mechanism file: F1/F2 defined here → affects Resonance, Connection, Empathy, Agent-Mechanism
- Drill reveals F1/F2 = SPECIAL CASE of Compiled/Fresh spectrum → fundamental reframe
- Current v2.4 frames F1="Feeling", F2="Logic" → v3.0 reframes F1="Compiled simulation", F2="Fresh PFC draft"
- PFC=Lawyer insight affects SPM accuracy analysis
- "Expert intuition = compiled, not bừa" needs integration

### Key changes v2.4 → v3.0
1. **F1/F2 REFRAME**: F1 = Compiled body-level simulation, F2 = Fresh PFC draft
   - "Feeling" and "Logic" = OBSERVER LABELS, not mechanism description
   - SPM's F1/F2 = special case of broader Compiled/Fresh axis (Inter-Body §3)
   - Inside body: only compiled ←→ fresh spectrum
2. **Expert intuition section**: "Shareable compiled" vs "Non-shareable compiled" (Drill §11.22)
   - Toán compiled = shareable → "logic" label. Tâm lý compiled = non-shareable → "intuition" label
   - CƠ CHẾ GIỐNG → khác shareability, NOT quality
3. **PFC=Lawyer implication**: SPM accuracy = f(PFC accuracy) → PFC may rationalize SPM output
4. **3-cost model reference**: Interaction cost = PFC draft + Suppress + Uncertainty
5. **Per-domain SPM**: same person, different domain → different F1/F2 ratio
6. Updated cross-refs

### Must preserve from v2.4
- §2 F1/F2 dual functions — keep mechanism, reframe labels
- §3-§4 Context-dependent selection — keep (strong)
- §5-§8 Per-Agent Valence, 6 steps, 5 Pattern-Types — keep
- §10 Reversed mapping (Schadenfreude, sadism) — keep
- §11-§14 Professional SPM, development, training, failure — keep
- §18 Late diagnosis re-compile (Health Conditions Drill) — keep
- ALL research citations

### Must read before writing
- SPM v2.4 full file (~1,948L)
- Inter-Body §3 (Compiled/Fresh)
- BFM v2.0 (by then complete)
- Drill §11.20 (F1/F2 reframe detail)
- Drill §11.22 (expert intuition)

---

## §6 — PHASE 5: Resonance v2.0 → v3.0 REWRITE (~1,800L)

### Tại sao viết mới?
- v2.0 vừa rewrite (2026-05-16) với WHY foundation → solid base
- NHƯNG: drill insights AFTER v2.0 rewrite thêm critical concepts:
  - By-product match = should be §1 CORE (hiện chỉ referenced, chưa explicit mechanism)
  - 3-cost model = sustainability analysis mạnh hơn
  - PFC=Lawyer = both PFCs may be "lawyering" → affects mutual Resonance assessment
  - Input channel control → manipulation relationship analysis
- Viết mới v3.0 = integrate ALL drill insights organically (không phải bolt-on)
- SPM v3.0 (Compiled/Fresh reframe) sẽ ready → Resonance v3.0 consistent

### Key changes v2.0 → v3.0
1. **§1 By-Product Match EXPLICIT**: elevate from implication → core mechanism explanation
   - B fill gap CỦA B → output = by-product → match A → A reward
   - Mutual = Resonance. One-way = parasocial. Diagram.
2. **3-cost model integration**: F1+F1 (≈0), F1+F2 (moderate), F2+F2+suppress (burnout)
   - Sustainability spectrum with 3-cost formula
3. **PFC=Lawyer in Resonance context**: stated reason ≠ actual body-need → deep friendship = calibrate
4. **Input channel control**: manipulation relationships, parasocial online
5. **Updated F1/F2 → Compiled/Fresh** (consistent with SPM v3.0 reframe)
6. **Twin + Autism cases** enhanced with 3-cost analysis

### Must preserve from v2.0
- §1 Foundation: 3 principles "riêng 100%" — keep (core)
- §2 F1/F2 quality tiers — keep, UPDATE terminology
- §3 Divergence spectrum + double empathy — keep
- §4 Resonance Baseline "hợp tính" — keep
- §5-§7 Conditions, Detection, Feedback loop — keep (Bird & Cook 2013 MUST preserve)
- §8 Cases — keep strongest, update with 3-cost annotations
- §9 Obligation-trapped — keep (very deep)
- ALL research citations (30+ citations)
- SPM accuracy = f(chunk library overlap) equation

### Must read before writing
- Resonance v2.0 full file (~1,700L)
- SPM v3.0 (by then complete)
- Inter-Body §4-§5 (3-cost, by-product match)
- Drill §2.4 (by-product match detail)

---

## §7 — PHASE 8: Framework-Label v1.1 → v2.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- VOCABULARY ANCHOR cho toàn framework → khi framework thêm ~6 concept families mới,
  file NÀY phải reflect. Refine nhỏ = patchy. Rewrite = internally coherent.
- Hiện v1.1 cover: reward/dissonance/prediction-delta/baseline/valence tags (5 categories)
- THIẾU: Entity-Compiled subtypes, Compiled/Fresh labels, by-product match/anti-match,
  2-Stream, 3-cost, 5-Channel Input Vector
- Cross-refs lỗi thời: BFM v1.2→v2.0, VP v1.4→v2.0

### Key changes v1.1 → v2.0
1. **§6 Entity-Compiled EXPAND**: approach/avoidance + 3 subtypes (positive/negative/mixed)
   - "Vừa thương vừa giận" = NORMAL multi-channel compile → cần label convention
   - Per-entity compiled profile vs momentary valence
2. **NEW: Compiled/Fresh processing labels**: trục thật (Inter-Body §3)
   - Compiled processing (automatic, body-direct, cost≈0)
   - Fresh PFC draft (deliberate, costly, not yet compiled)
   - Logic/Feeling = observer labels (reference, NOT mechanism labels)
3. **NEW: Inter-body interaction labels**: by-product match, anti-match,
   Stream 1/Stream 2, 3-cost components, 5-Channel Input Vector
4. **§2-§5 UPDATE**: integrate new terminology where needed
5. **Cross-refs all updated** to Phase 1-7 rewrite versions

### Must preserve from v1.1
- §1 3-Tier Label System (General → Direction → Specific) — CORE, keep
- §2 Positive labels (reward, Type A/B, opioid, CT, eCB, A₀-A₃, Profiles) — keep ALL
- §3 Negative labels (dissonance, threat, chunk dynamics, cortisol Roles) — keep ALL
- §4 Detection labels (prediction-delta, DRD4, PFC spotlight) — keep
- §5 Neutral (baseline, habituated) — keep
- §7 Observation vs Mechanism distinction — keep (CORE)
- §8 Quy tắc sử dụng — keep + EXPAND for new terms

### Must read before writing
- Label v1.1 full file (532L)
- Inter-Body-Mechanism.md §3 (Compiled/Fresh), §4 (3-cost), §5 (by-product match),
  §6 (5-Channel), §7 (PFC=Lawyer), §8 (Entity-Compiled)
- VP v2.0 §2 (Entity-Compiled defined)
- Resonance v3.1 §2 (2-Stream Architecture, anti-match)
- BFM v2.0 (vocabulary consistency check)

---

## §7b — PHASE 9: Gap-Direction v1.1 → v2.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- Gap direction = CORE cho by-product match (B's output phải match A's gap DIRECTION)
- v1.1 solid nhưng chưa connect: by-product match, 2-Stream, Inter-Body
- 2,154L — file dài, nhiều content → rewrite = opportunity tích hợp organic
- By-product match + gap direction = CÙ MỘT narrative (output match direction)

### Key changes v1.1 → v2.0
1. **By-product match connection** (NEW): gap direction = WHY by-product match works
   - B fill gap CỦA B → output = by-product → match A's gap DIRECTION → A reward
   - Direction mismatch = no reward DÙ có output (anti-match case)
2. **2-Stream connection** (NEW): Stream 1 = unidirectional direction match,
   Stream 2 = mutual SPM-mediated direction matching
3. **Architecture B note**: general-purpose reward = gap direction KHÔNG hardwired
   per-content → emerge from chunk network
4. **Inter-Body cross-ref** (NEW): Inter-Body §5 (Full Chain), §2 (Body-Need direction)
5. **Label v2.0 vocabulary consistency** throughout
6. **Cross-refs updated** to all Phase 1-7 versions

### Must preserve from v1.1
- §0 TẠI SAO FORMALIZE — keep (strong opening)
- §1 DEFINITION — keep core, ADD by-product match connection
- §2 PROOF — keep (4 proofs, tight logic)
- §3 "CHƯA BIẾT = KHÔNG CÓ GAP" — keep (foundational principle)
- §4 4 PROPERTIES — keep
- §5 UNIFIED DIRECTION MODEL (Tier 1-4) — keep + ADD Compiled/Fresh note
- §6 2-LAYER MODEL — keep (strong)
- §7-§9 Formation + External Install + Background Pattern — keep
- §10 Abstract Activity × Body-Base — keep
- §11 EXAMPLES — keep ALL (22 examples confirmed)
- §15 Autism Special Interests (v1.1 addition) — keep
- ALL research citations

### Must read before writing
- Gap-Direction v1.1 full file (2,154L)
- Inter-Body §2 (Body-Need direction), §5 (by-product match + Full Chain)
- Resonance v3.1 §2 (2-Stream Architecture — Stream 1 = directional match)
- Label v2.0 (by then complete — vocabulary consistency)
- BFM v2.0 §3.3 (Chunk-Gap definition)

---

## §7c — PHASE 10: Reward-Signal-Architecture v1.0 → v2.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- Type A/B = ORTHOGONAL dimension → referenced by Label, Feeling, Body-Feedback, Why-Body-Knows
- v1.0 solid nhưng missing: Compiled/Fresh connection, Architecture B framing, Inter-Body ref
- User insight: "Evolution body phát triển từ sơ sinh (chủ yếu Type B) tới trưởng thành
  (Type A dày đặc). Càng verify domain thì độ chính xác càng cao" → enriches §8 Development

### Key changes v1.0 → v2.0
1. **Compiled/Fresh note**: Type A = compiled evaluation (chunk library needed),
   Type B = hardware direct (minimal compilation)
2. **§8 Development ENRICHED**: Type B→A development trajectory
   - Sơ sinh: Type B dominant (touch, warmth — hardware)
   - Phát triển: Type A gradually compiles (evaluation grows with chunks)
   - Trưởng thành: Type A dày đặc + Type B vẫn nền tảng
   - Domain verification → accuracy tăng dần
3. **Architecture B connection**: general-purpose reward = WHY Type A possible
   (Architecture A species → only hardware-specific, ≈ Type B only)
4. **Inter-Body cross-ref** (NEW): Inter-Body §1 (Architecture B), §2 (Body-Need)
5. **Label v2.0 vocabulary consistency**
6. **Cross-refs updated**: BFM v2.0, VP v2.0, Gap-Direction v2.0

### Must preserve from v1.0
- §1 Type A/B distinction (core) — keep, ADD Compiled/Fresh note
- §1.2-§1.6 (orthogonal, H10×A/B, floor, multi-role, BFM mapping) — keep ALL
- §2 A₀→A₃ complexity gradient — keep (strong)
- §3 A Gates B — keep
- §4 5 Profiles — keep ALL
- §5-§6 Temporal Stack, Conditional Interaction — keep
- §7 State Dependence (Cabanac refined) — keep
- §9 Evidence (naltrexone table) — keep ALL research
- §10 5 Forces Holding Model — keep
- ALL research citations (115+ from drill source)

### Must read before writing
- RSA v1.0 full file (1,864L)
- Inter-Body §1 (Architecture B), §2 (Body-Need)
- Inter-Body §3 (Compiled/Fresh — for Type A/B connection)
- Label v2.0 (by then complete)
- Why-Body-Knows.md (current — check what RSA can feed to it)

---

## §7d — PHASE 11: Body-Feedback.md v1.1 → v2.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- Entry point / synthesis cho TOÀN BỘ Body-Feedback/ folder
- Folder đã rebuild: BFM v2.0 ✅, Label v2.0 (Phase 8), Gap-Direction v2.0 (Phase 9),
  RSA v2.0 (Phase 10) → entry point PHẢI reflect bức tranh mới
- v1.1 references BFM v1.0 (obsolete), missing Inter-Body concepts entirely
- Narrative flow cần update: H10, chunk dynamics, folder reading guide

### Key changes v1.1 → v2.0
1. **§1 Folder overview UPDATE**: reflect all new file versions in folder
2. **§4 Chunk Dynamics UPDATE**: integrate Compiled/Fresh terminology
3. **§6 H10 UPDATE**: note Type A/B H10 differences (from RSA v2.0)
4. **Inter-Body cross-ref** (NEW): architecture B → why body feedback exists
5. **Reading guide UPDATE**: Label v2.0 position, new reading order
6. **ALL cross-refs**: BFM v1.0→v2.0, Label v1.1→v2.0, Gap v1.0→v2.0, RSA v1.0→v2.0
7. **Narrative flow**: WHY body feedback → WHAT kinds → HOW works → WHERE to read more

### Must preserve from v1.1
- §2 Dual-Pull Architecture — keep (unique contribution)
- §3 Interface Loop 6-Step — keep (unique contribution)
- §5 3 Nguồn Khó Chịu — keep (unique contribution)
- §6 H10 definitive reference — keep + UPDATE
- §7 Unique Case Analyses — keep ALL
- §8 Trauma Loop + Hedonic Trap — keep (unique mechanisms)
- §9 Absorbed Content Map — keep
- ALL research citations

### Must read before writing
- Body-Feedback v1.1 full file (707L)
- BFM v2.0, Label v2.0, Gap-Direction v2.0, RSA v2.0 (all by then complete)
- Inter-Body §1-§2 (Architecture B, Body-Need)
- 01-Foundation through 04-Integration (check for consistency)

---

## §7e — PHASE 12: Feeling.md v2.2 → v3.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- Central reference cho feeling system — 1,905L, referenced by many files
- Missing: PFC = Lawyer (CRITICAL for §2 Layer 7 Explanation),
  Compiled/Fresh note, RSA v2.0 connection
- v2.2 solid core nhưng rewrite = opportunity tích hợp organic thay vì bolt-on
- Feeling × Compiled/Fresh interaction = important (expert feeling = compiled processing)

### Key changes v2.2 → v3.0
1. **PFC = Lawyer** (NEW for Feeling context): Layer 7 Explanation = PFC lawyering
   - PFC "giải thích" feeling = stated reason ≠ actual body-need
   - "Tôi buồn vì X" → thật ra body respond vì Y → PFC tìm X post-hoc
   - Deepens §2 Layer 7 analysis significantly
2. **Compiled/Fresh note** for §8 Feeling Quality:
   - Expert feeling = COMPILED (not mystical intuition)
   - Beginner "logic" about feelings = FRESH PFC draft
   - Quality = f(compilation level × chunk library)
3. **RSA v2.0 cross-ref** for §6 Reward: Type A/B reward in feeling context
   - Type A reward → PFC observes clearly (Layer 4-6)
   - Type B reward → PFC observes vaguely (Layer 2-3)
4. **Inter-Body cross-ref** (NEW): §1 Architecture B, §3 Compiled/Fresh
5. **All cross-refs updated** to Phase 1-11 versions

### Must preserve from v2.2
- §0 Position — keep
- §1 Definition (formal, 3 properties, disclaimers) — keep (excellent quality)
- §2 7-Layer Fidelity Gradient — keep + ENRICH Layer 7 with PFC=Lawyer
- §3 Core Claim — keep
- §4 Signal Integration (3 hubs) — keep
- §5 8-Step Operational Flow — keep
- §6 Reward — keep + ADD Type A/B cross-ref
- §7 Gradient (H5, convergence) — keep
- §8 Quality — keep + ADD Compiled/Fresh note
- §9 Feeling Loop + Bridge — keep
- §10 Literacy + Training — keep
- §11 Evolutionary — keep
- §3.3 Alexithymia (v2.2 addition) — keep
- ALL research citations (25+)
- ALL companion file references

### Must read before writing
- Feeling.md v2.2 full file (1,905L)
- Inter-Body §3 (Compiled/Fresh), §7 (PFC=Lawyer)
- RSA v2.0 (by then complete — Type A/B)
- Label v2.0 (by then complete — vocabulary)
- Logic-Feeling.md v1.0 (current — check interface for v2.0 consistency)

---

## §7f — PHASE 13: Logic-Feeling v1.0 → v2.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- ★★★ MOST DRILL IMPACT — Inter-Body §3 nói rõ "TRỤC THẬT = Compiled vs Fresh,
  KHÔNG PHẢI Feeling vs Logic"
- File hiện tại (DRAFT v1.0, 2026-04-13) dùng "Logic vs Feeling" làm 2 processing modes
  → drill chứng minh đó chỉ là OBSERVER LABELS, không phải mechanism description
- Logic-Feeling = file DUY NHẤT về processing modes → phải reflect bức tranh mới
- Rewrite = fundamental reframe, không thể refine

### Key changes v1.0 → v2.0
1. **§0-§1 REFRAME**: Logic/Feeling = observer labels → Compiled/Fresh = trục thật
   - §NEW: Compiled/Fresh spectrum definition (from Inter-Body §3)
   - Logic = what observers call "shareable compiled" or "fresh PFC processing"
   - Feeling = what observers call "non-shareable compiled" or "body-direct"
   - Labels USEFUL for communication but MISLEADING for mechanism
2. **§2 "Tại sao cần cả 2" REFRAME**: qua lens Compiled/Fresh
   - Fresh CẦN PFC draft (costly, slow, but discoverable)
   - Compiled CẦN Hebbian history (automatic, but can't discover NEW)
   - → BOTH needed = BOTH compilation states needed for growth
3. **§3 Flow REFRAME**: Logic→Feeling = actually Fresh→Compiled transition
   - "Hiểu" = đã compiled. "Chưa hiểu" = still fresh PFC draft.
   - Transition = learning process, NOT mode switching
4. **PFC = Lawyer** (NEW §7): PFC explanation of processing = lawyering
   - "Tôi dùng logic" → thật ra body đã compiled, PFC claims credit
   - "Tôi dùng feeling" → thật ra PFC chưa compiled, labels as "intuition"
5. **"Shareable vs Non-shareable compiled"** (from Inter-Body §3.4):
   - Toán compiled = shareable → labeled "logic"
   - Tâm lý compiled = non-shareable → labeled "intuition"
   - CƠ CHẾ GIỐNG → khác shareability, NOT quality
6. **§5 Parallel processing UPDATE**: still valid, ADD Compiled/Fresh annotations
7. **§6 Modality bias UPDATE**: still valid, reframe as "compilation pathway bias"

### Must preserve from v1.0
- §2 WHY both needed — keep INSIGHT, reframe mechanism
- §3 Flow diagram — keep STRUCTURE, update labels
- §4 5 Cases — keep ALL (excellent quality):
  - Cortisol (correlation vs mechanism)
  - Newton→Einstein (scope expansion)
  - Dầu+Máy (cross-domain)
  - Táo+Chuối (abstraction)
  - Mẹ bảo học (destination vs journey)
  → Cases STILL VALID — reinterpret through Compiled/Fresh lens
- §5 Parallel processing + mix ratios — keep (user's refinement)
- §6 Modality bias — keep
- ALL research citations (Kahneman, Damasio, Gendlin, Craig, Gallese, Panksepp, Klein)
- Einstein primary source (Hadamard letter 1945) — MUST preserve
- Relationship conflict example (§6.2) — keep (excellent)

### Must read before writing
- Logic-Feeling v1.0 full file (1,779L)
- Inter-Body §3 (Compiled/Fresh — THE source for reframe)
- SPM v3.0 §1 (Compiled/Fresh in SPM context)
- Feeling v3.0 (by then complete — consistent interface)
- Logic-Feeling-Balance.md (meta-principle — check consistency)
- Logic-Feeling-Failure-Examples.md (18 examples — check compatibility)

---

## §7g — PHASE 14: Logic-Feeling-Balance v1.0 → v2.0 REWRITE ★ NEW IN v5.0

### Tại sao viết mới?
- META-PRINCIPLE companion cho Logic-Feeling.md — khi LF rewrite → Balance phải follow
- v1.0 (1,433L) nói "cả 2 không 100%, mỗi người tự calibrate" nhưng THIẾU HƯỚNG calibrate
- Drill ⑧ "Domain Reality = Final Arbiter" → GIẢI QUYẾT "hướng nào?"
- Insight mới: hướng = OUTWARD (toward domain), không phải INWARD (which tool to trust)
  → Biến file từ "bế tắc epistemological" thành "có lối ra qua domain feedback"

### Key changes v1.0 → v2.0
1. **HƯỚNG CALIBRATE = DOMAIN FEEDBACK** (★ breakthrough):
   - File cũ hỏi "tin cái nào?" → infinite regress
   - File mới: câu hỏi đúng = "tương tác domain NHIỀU CHƯA?"
   - Nhiều domain feedback → chunks compile CHÍNH XÁC hơn
   - → BOTH Compiled ("feeling") AND Fresh ("logic") IMPROVE
   - Direction = OUTWARD, không INWARD
2. **Compiled/Fresh reframe**:
   - Balance KHÔNG phải giữa Logic và Feeling (observer labels)
   - Balance = giữa Compiled (đã verify, automatic) và Fresh (chưa verify, costly)
   - Calibration = compile MORE from domain → accuracy tăng
3. **PFC = Lawyer**: §7 epistemological trap strengthened
   - PFC ACTIVELY lawyers, không chỉ "có thể sai"
   - "Tôi chọn X vì A" → thật ra body chọn → PFC tìm A post-hoc
4. **Architecture B**: structural WHY uncertainty
   - General-purpose → PHẢI learn from domain → inherently uncertain TỚI KHI compiled
   - Uncertainty = ARCHITECTURE COST of flexibility
5. **Dual Check** (Ask-AI v3.1):
   - Body = quality controller (coherent? fit chunks?)
   - Domain = final arbiter (worked? didn't work?)
   - 2 checks ĐỘC LẬP → maximize BOTH, not choose between them

### Must preserve from v1.0
- §1 Core principle (both not 100%, structural) — keep
- §2 Feeling = PRIMARY (closer to domain) — keep (CORE insight)
- §3-§5 Exceptions (evolution lag, correlation≠causation, etc.) — keep ALL
- §6-§7 Why rules fail + epistemological trap — keep + ENRICH with PFC=Lawyer
- §8 Describe vs Prescribe — keep distinction + ADD: "describe INCLUDES direction"
- §9 Human value (diversity = feature) — keep (strong)
- §10 Domain feedback — keep + ELEVATE to central answer (not just "arbiter")
- §11 Emergent — keep + ADD 3-Layer Evolution connection
- ALL research citations (Campbell, Popper, Page, Hayek, Taleb, Damasio)

### Must read before writing
- Logic-Feeling-Balance v1.0 full file (1,433L)
- Logic-Feeling v2.0 (by then complete — companion must be consistent)
- Inter-Body §3 (Compiled/Fresh), §7 (PFC=Lawyer), §10 (Human↔AI, Domain=Arbiter)
- Ask-AI v3.1 §6.1 (Dual Check model)
- Logic-Feeling-Failure-Examples.md (18 examples — check compatibility)

---

## §7h — PHASE 15: Neural-Processing-Flow v1.0 → v2.0 REWRITE ★ NEW IN v5.0

### Tại sao viết mới?
- HARDWARE FLOW file — mô tả con đường VẬT LÝ tín hiệu đi qua trong não
- DRAFT v1.0 (2026-04-17, 1,064L) — chưa bao giờ formalize
- Excellent research foundation (20+ 🟢 citations) nhưng chưa connect drill insights
- Missing: Architecture B (WHY this hardware), Compiled/Fresh (WHY compiled=fast),
  2-Source model connection, L3 operator fix, Inter-Body refs
- Hardware file = EXPLAIN tại sao Compiled nhanh (direct pathway) vs Fresh chậm (PFC mediated)
  → Compiled/Fresh AT HARDWARE LEVEL = powerful connection

### Key changes v1.0 → v2.0
1. **Architecture B connection** (NEW):
   - File mô tả WHAT hardware → v2.0 thêm WHY hardware = Architecture B
   - General-purpose reward + compilation + social hardware = 3 foundations
   - Hardware file EXPLAIN Architecture B at physical level
2. **Compiled/Fresh at hardware level** (NEW):
   - Compiled: direct pathway (sensor → cortex → body response), cost≈0
   - Fresh: PFC-mediated pathway (sensor → cortex → PFC draft → test → route), costly
   - Hardware EXPLAINS why Compiled faster: fewer nodes, fewer gates, direct
3. **2-Source model connection** (NEW):
   - Sensory-Driven = bottom-up pathway (§1-§3 trong file)
   - Pattern-Driven = top-down re-activation (§7 trong file)
   - BFM v2.0 2-source model = DESCRIBES what these pathways produce
4. **§10.3 L3 Operator FIX**:
   - "PROTECT OPERATOR" → Protect = observation parameter (Body-Base v3.0 fix)
   - Update terminology consistent với v3.0
5. **PFC = Lawyer strengthen**:
   - §6.1 function ⑤ "TRANSLATE" → explicit PFC=Lawyer frame
   - Post-hoc rationalization = hardware mechanism at vmPFC level
6. **Inter-Body cross-ref** (NEW):
   - 5-Channel Input Vector maps to hardware pathways described in §1
   - Mirror mechanisms (§8.3) → connect to Inter-Body §5 Full Chain
7. **Cross-refs updated** to ALL Phase 1-14 rewrite versions

### Must preserve from v1.0
- §1 Body Sensors (20+ types, 3 categories) — keep ALL (excellent enumeration)
- §2 Thalamus gateway + gating — keep (solid research)
- §3 Cortical 6-layer architecture — keep (Mountcastle)
- §4 Binding 5 mechanisms — keep ALL (excellent synthesis)
- §5 Chunk compilation (4 mechanisms) — keep + ADD Compiled/Fresh framing
- §6 PFC 5 functions — keep + STRENGTHEN ⑤ with PFC=Lawyer
- §7 Simulation top-down — keep + CONNECT to Pattern-Driven source
- §8 Feeling emergence — keep + UPDATE to match Feeling v3.0
- §9 Externalization loop — keep (solid)
- §10 Complete flow diagram — keep + UPDATE
- ALL 20+ research citations (Sherman, Mountcastle, Singer, Stein, Craig, Damasio, etc.)

### Must read before writing
- Neural-Processing-Flow v1.0 full file (1,064L)
- Inter-Body §1 (Architecture B), §3 (Compiled/Fresh), §6 (5-Channel)
- BFM v2.0 §2 (2-Source model — Sensory-Driven / Pattern-Driven)
- Body-Base v3.0 (L3 fix — operator terminology)
- Feeling v3.0 (by then complete — §8 must match)
- Logic-Feeling v2.0 (by then complete — §0 Processing Layer must match)

---

## §8a — PHASE 16: Agent-Mechanism v1.0 → v2.0 REWRITE (~1,600L)

### Tại sao viết mới?
- Still DRAFT v1.0 (ngày tạo 2026-04-15) — OLDEST core file, chưa bao giờ update
- Integration hub cho SPM + Resonance → SPM v3.0, Resonance v3.1 → previews outdated hoàn toàn
- Missing ALL drill concepts: by-product match, 5-channel, 3-cost, Entity-Compiled, PFC=Lawyer
- §12 body-need feeder = critical section, cần integrate by-product match + 3-cost

### Key changes v1.0 → v2.0
1. **§5-§6 SPM/Resonance previews REWRITE**: match SPM v3.0 + Resonance v3.1
   - SPM: Compiled/Fresh reframe, not "Feeling/Logic"
   - Resonance: by-product match, 2-Stream Architecture, cost sustainability
2. **§12 Body-need feeder REWRITE**: integrate by-product match
   - Entity B = source of by-product that may match my gap direction
   - 3-cost model for sustainability prediction
3. **NEW: Entity-Compiled concept** (from Drill §11.10)
   - Reframe Entity-Owned → Entity-Compiled
   - 3 subtypes: positive/negative/mixed (mixed = MOST COMMON)
4. **NEW: Inter-body chain reference** (brief, cross-ref Inter-Body §5)
5. **NEW: PFC=Lawyer note** in schema override section
6. **Updated metadata**: all dependencies, cross-refs to new versions

### Must preserve from v1.0
- §2 Reject binary Object-Agent — keep (foundational)
- §3 3-layer architecture — keep, update terminology
- §4 3-concept split (Self-Pattern/SPM/Resonance) — keep
- §7-§9 Quality axes, Pattern-Type, Gradient validation — keep
- §10-§11 Schema override, Schema-Linked — keep
- §13-§15 Development, Failure modes, Individual variation — keep
- ALL cases and research citations

### Must read before writing
- Agent-Mechanism.md full file (~1,200L estimated)
- SPM v3.0 (by then complete)
- Resonance v3.0 (by then complete)
- Inter-Body-Mechanism.md (by then complete)

---

## §8b — PHASE 17: Connection v3.3 → v4.0 REWRITE (~2,000L)

### Tại sao viết mới?
- Observation parameter file: answers "TẠI SAO connection?" → drill answers this DEEP
- v3.3 has 3 Generative Primitives (good) nhưng ❶ Hardware = shallow ("body cần social")
- Drill Q4 answer: 4 REASONS social = architecture requirement → much deeper
- By-product match + 3-cost + PFC=Lawyer → enrich analysis significantly
- SPM v3.0 + Resonance v3.0 + Agent v2.0 sẽ ready → cross-refs accurate

### Key changes v3.3 → v4.0
1. **❶ Hardware DEEP**: 4 reasons (survival math + compilation needs + reused circuits + default state)
   - Research: Eisenberger 2003, Panksepp 1998, Coan & Sbarra 2015
   - Social Baseline Theory: alone = deviation, social = default
2. **By-product match in connection context**: how 2 agents feed each other via by-products
3. **3-cost model for 8 pathways**: annotate each pathway with cost profile
4. **"Cô đơn" ENRICHED**: not just "❶ fire thiếu" → 5-channel analysis
5. **Updated SPM references**: Compiled/Fresh terminology (SPM v3.0)
6. **PFC=Lawyer in social**: stated reasons for seeking/avoiding connection ≠ actual
7. **Input channel control in relationships**: healthy (Ch1 rich) vs manipulative (Ch4 dominant)

### Must preserve from v3.3
- §3 3 Generative Primitives (❶ × ❷ × ❸) — keep FRAMEWORK, deepen ❶
- §4 F1/F2 resonance quality — keep, UPDATE terminology
- §5 8 reward pathways — keep, ADD cost annotations
- §6-§8 Capacity, calibration, distance — keep
- §9-§13 Chunk dynamics, types, development, culture — keep
- ALL research citations
- "Cô đơn" analysis — keep, enrich

### Must read before writing
- Connection v3.3 full file (~1,890L)
- SPM v3.0, Resonance v3.0, Agent v2.0 (all complete by then)
- Inter-Body §1 (3 foundations → ❶ Hardware deep)
- Drill §11.24 (Q4 answer: 4 reasons)

---

## §9 — PHASE 18: Why-Body-Knows DRAFT → v1.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- META file — "Tại sao framework HOẠT ĐỘNG?" = foundation argument cho TOÀN BỘ framework
- Vẫn DRAFT (2026-03-25) — CHƯA BAO GIỜ formalize, cũ nhất trong danh sách
- Missing: Architecture B, Compiled/Fresh insight, 3-Layer Evolution, Inter-Body refs
- References Core-v7.8-Draft.md (outdated file paths)
- User bổ sung insight: "Evolution body phát triển từ sơ sinh (chủ yếu Type B) tới
  trưởng thành (Type A dày đặc). Càng verify domain thì độ chính xác càng cao"

### Key changes DRAFT → v1.0
1. **Architecture B framing** (NEW): general-purpose reward = WHY body can learn ANY domain
   - Architecture A (insects): hardwired per-content → limited but fast
   - Architecture B (humans): general-purpose → flexible but needs compile time
   - → WHY body "biết" = architecture B + compilation + domain calibration
2. **3-Layer Evolution connection** (NEW): Inter-Body §9
   - Hardware layer (evolution) ≈ §4 Tầng 1
   - Compiled layer (development) ≈ §4 Tầng 2
   - Cultural layer (culture + AI) ≈ §4 Tầng 3-4
   - → SAME insight, different frame. Cross-ref for consistency.
3. **Type B→A development trajectory** (User insight + RSA v2.0):
   - Sơ sinh: primarily Type B (hardware → touch, warmth = ALWAYS available)
   - Phát triển: Type A compiles gradually (with chunk library growth)
   - Trưởng thành: Type A dày đặc + Type B vẫn nền tảng
   - "Càng verify domain → accuracy tăng" = compiled chunks → better body check
4. **Compiled/Fresh insight**: expert "feeling" = compiled (not mystical)
   - Body "biết" = body HAS COMPILED sufficient chunks
   - "Không biết" = still FRESH (PFC draft, uncertain)
5. **PFC = Lawyer note**: PFC explanation of "tại sao body biết" = lawyering
   - Body biết TRƯỚC. PFC giải thích SAU. Giải thích CÓ THỂ sai.
6. **Promote DRAFT → formal v1.0**: proper metadata, honest assessment, cross-refs

### Must preserve from DRAFT
- §1 3 Câu Hỏi Gốc — keep (excellent framing)
- §2 Nhạc mới hay (H10 walkthrough) — keep + UPDATE with RSA Type A/B
- §3 Pattern mới → reward (coherence check) — keep (solid)
- §4 4 tầng calibrate — keep + ADD 3-Layer Evolution cross-ref
- §5 3 loại sai (evolution lag, chunks nền sai, schema override) — keep
- §6 Vòng tròn hoàn chỉnh — keep + ENRICH
- ALL research citations (Zajonc, Berlyne, North/Hargreaves, Berridge, Schultz)

### Must read before writing
- Why-Body-Knows DRAFT full file (410L)
- Inter-Body §1 (Architecture B), §3 (Compiled/Fresh), §9 (3-Layer Evolution)
- RSA v2.0 (by then complete — Type A/B + development lifecycle)
- Body-Base v3.0 (entry point — check consistency)
- Label v2.0 (vocabulary)

---

## §9b — PHASE 19: Collective-Body v1.2 → v2.0 REWRITE ★ NEW IN v4.0

### Tại sao viết mới?
- Mechanism file about Individual ↔ Collective — 1,388L, cross-refs severely outdated
- References: Body-Base v2.0 (→v3.0), Body-Coupling v1.0 (→v2.0), VP v1.3 (→v2.0),
  Connection v3.1 (→v4.0) — FOUR major dependency updates
- Missing: Inter-Body cross-ref, Architecture B formal connection, Entity-Compiled,
  Compiled/Fresh note, PFC=Lawyer strengthening
- User bổ sung insight: "làm rõ hơn bằng cách nào cá nhân lại có thể detect được
  collective-gap" → NEW analysis section

### Key changes v1.2 → v2.0
1. **User insight: Individual detect collective-gap** (NEW analysis):
   - HOW: gap direction in individual's chunk network POINTS TO collective phenomena
   - Gap = f(surrounding chunks) → if chunks include collective knowledge → gap EMERGES
   - VD: economist's chunks → predict economic gap → detect collective-gap
   - Body mechanism SAME (chunk-gap). Content = collective level.
   - → NOT separate mechanism. = Same mechanism, collective-level substrate.
2. **Inter-Body-Mechanism.md cross-ref** (NEW): file mechanism about inter-body mà
   THIẾU reference tới formal inter-body mechanism file!
   - Architecture B → §1 collective = architecture requirement
   - By-product match → collective by-product patterns
   - 3-Layer Evolution → directly maps to Model 3 Cấp
3. **Architecture B formal connection**: general-purpose reward → WHY collective needed
   (Architecture B trade-off = long childhood → needs collective infrastructure)
4. **Entity-Compiled terminology**: VP refs update "Entity-Owned" → "Entity-Compiled"
5. **Compiled/Fresh note** for §2: compile SHORT = Compiled (automatic), fresh learning
   at individual level
6. **PFC = Lawyer strengthening**: §2 already says "PFC confabulate" → now use formal
   PFC=Lawyer frame (Inter-Body §7)
7. **ALL cross-refs updated**: Body-Base v3.0, Body-Coupling v2.0, VP v2.0, Connection v4.0

### Must preserve from v1.2
- §1 Model 3 Cấp — keep (CORE contribution)
- §2 Cấp 1 Individual (4 compile pathways) — keep (excellent)
- §3 Cấp 2 Collective (distributed infrastructure) — keep + ADD collective-gap detection
- §3.5 Dual-Pull Propagation (v1.2 addition) — keep (novel)
- §4 Global-Body Analogy (~70%/~30%) — keep
- §5 Trust = Bridge — keep (CORE)
- §6 System Compilation (6 mechanisms) — keep (novel)
- §7 Coupling Proxy — keep
- §8 Collective × AI era — keep
- §8.4 AI = trust entity loại mới (v1.1 addition) — keep
- §4.2 ⑨ Collective KHÔNG sleep (v1.1 addition) — keep
- ALL research citations (18+ 🟢)

### Must read before writing
- Collective-Body v1.2 full file (1,388L)
- Inter-Body §1 (Architecture B), §9 (3-Layer Evolution)
- Connection v4.0 (by then complete — collective connection refs)
- Body-Base v3.0 (Model 3+1 — consistency check)
- Gap-Direction v2.0 (by then complete — gap mechanism for collective-gap analysis)

---

## §10 — PHASE 20: Terminology Propagation + Cross-refs + Verification ✅ DONE

> **v10.0 NOTE:** Section này là PLAN GỐC cho Phase 20 (viết trước khi thực hiện).
> Phase 20 THỰC TẾ scope hẹp hơn dự kiến — xem ✅ DONE items ở §1 Tầng 5.
> Các items chưa hoàn thành đã DEFER sang Phase 20b (Tầng 5b) + Phase 21-31.

### ✅ ĐÃ HOÀN THÀNH trong Phase 20:
- 4-tier → 2-tầng: 7 files, 28 edits (Cortisol, AI-Schema, 01-Foundation, 03-Reward, 04-Integration, Chunk-Sketch EN+VI)
- Full framework audit: ~120 files assessed → phát hiện Tầng 5b + 6 + 7 cần thiết
- Version ref propagation: Body-Base v3.0→v3.1, WBK v1.0→v1.1

### ⏩ DEFERRED sang Phase 20b (Tầng 5b):
- F1/F2 mechanism label fix (core files): Connection, Compliance-Floor, Emergent-Patterns, Core-Software
- 4-tier fix (non-research): Ask-AI, Natural-Development, Child-Dev-Mechanism
- WBK §ref fixes: 8 files (01-Foundation, 02-Dissonance, Collective-Body, LFB, LF-Failure-Examples, Knowledge-Flow, Core-Software, Child-Dev-Mechanism)

### ⏩ DEFERRED sang Phase 21-31:
- Empathy + Gratitude F1/F2 → Phase 21-22
- Entity-Owned → Entity-Compiled terminology fixes → Phase 21-22 (Empathy, Gratitude, Obligation)
- Research file F1/F2 fixes → Phase 28-31 (Love-Romantic, Uncanny-Valley, Social-Cal, Alzheimer)
- Research file 4-tier fixes → Phase 30 (Social-Cal, AI-Self-Model)
- 01-File-Index update → Phase 20b (after content fixes)

### Verification checklist (deferred — verify AFTER Phase 31)
- [x] "Entity-Owned" appears NOWHERE in active framework (except backup/ + drill raw) ✅ VERIFIED 2026-05-17
- [x] "F1 Feeling / F2 Logic" appears NOWHERE as mechanism label ✅ VERIFIED 2026-05-17
- [x] "L3 operators: Protect" appears NOWHERE ✅ VERIFIED 2026-05-17
- [ ] Tất cả file versions internally consistent (partial — some stale deps remain)
- [ ] Cross-ref §numbers đúng across all files (partial — WBK+VP refs verified)
- [x] Terminology consistent với Framework-Label.md v3.0 ✅ Entity-compiled propagated

---

## §11 — ESTIMATED TIMELINE (v5.0)

```
═══════════════ TẦNG 0: DRILL SOURCE + CORE MECHANISM ═══════════════
Session 1:  Phase 1  — Inter-Body-Mechanism.md (NEW 1,500L)       ✅ DONE
Session 2:  Phase 2  — Body-Feedback-Mechanism v2.0 (1,519L)      ✅ DONE
Session 3:  Phase 3  — Valence-Propagation v2.0 (1,871L)          ✅ DONE
Session 4:  Phase 4  — Body-Base.md v3.1 (1,297L)                 ✅ DONE
Session 5:  Phase 5  — Body-Coupling v2.0 (1,544L)                ✅ DONE
Session 6:  Phase 6  — SPM v3.0 (2,614L)                          ✅ DONE
Session 7:  Phase 7  — Resonance v3.1 (1,540L)            ✅ DONE

═══════════ TẦNG 1: BODY-FEEDBACK FOLDER REBUILD ═══════════════════
Session 8:  Phase 8  — Framework-Label v2.0 (1,118L)          ✅ DONE
Session 9:  Phase 9  — Gap-Direction v2.0 (2,681L)                ✅ DONE
Session 10: Phase 10 — Reward-Signal-Architecture v2.0 (1,986L)   ✅ DONE
Session 11: Phase 11 — Body-Feedback.md v2.0 (892L)               ✅ DONE

═══════════ TẦNG 2: PROCESSING & OBSERVATION ═══════════════════════
Session 12: Phase 12 — Feeling.md v3.0 (2,122L)                   ✅ DONE
Session 13: Phase 13 — Logic-Feeling v2.0 (1,572L)                ✅ DONE
Session 14: Phase 14 — Logic-Feeling-Balance v2.0 (1,612L)        ✅ DONE
Session 15: Phase 15 — Neural-Processing-Flow v2.0 (1,270L)       ✅ DONE

═══════════ TẦNG 3: INTEGRATION HUB ════════════════════════════════
Session 16: Phase 16 — Agent-Mechanism v2.0 (1,956L)              ✅ DONE
Session 17: Phase 17 — Connection v4.0 (2,324L)                   ✅ DONE

═══════════ TẦNG 4: META & COLLECTIVE ══════════════════════════════
Session 18: Phase 18 — Why-Body-Knows v1.1 (1,273L)               ✅ DONE
Session 19: Phase 19 — Collective-Body v2.0 (1,651L)              ✅ DONE

═══════════ TẦNG 5: VERIFICATION ═══════════════════════════════════
Session 20: Phase 20 — Terminology + audit + 4-tier fix           ✅ DONE

═══════════ TẦNG 5b: CONTENT FIX — CORE FILES (v10.0 MERGED) ═══════
Session 21: Phase 20b — Entity-compiled propagation + verification (11 files, ~15 edits) ✅ DONE (2026-05-17)

═══════════ TẦNG 6: OBSERVATION LAYER CASCADE ══════════════════════
Session 22: Phase 21 — Empathy.md v3.0 (~200-300L additions)       ✅ DONE (2026-05-17)
Session 23: Phase 22 — Gratitude.md v2.0 (~200-300L additions)     ✅ DONE (2026-05-17)
Session 24: Phase 23 — Obligation.md v1.1 (~100-150L additions)    ✅ DONE (2026-05-17)
Session 25: Phase 24 — Status.md v2.1 (~100-150L additions)        ✅ DONE (2026-05-17)
Session 26: Phase 25 — Drive+Novelty+Threat v1.1 (+254L actual)    ✅ DONE (2026-05-17)
Session 27: Phase 26 — Protect+Meaning+Boredom v1.1/v2.1 (+232L)  ✅ DONE (2026-05-17)
Session 28: Phase 27 — Autonomy+Autonomy-Hw v1.1 (+45L actual)     ✅ DONE (2026-05-17)

═══════════ TẦNG 7: RESEARCH CASCADE (+F1/F2 +4-tier absorbed) ════
Session 29: Phase 28 — Love-Romantic v2.4 (+~120L: 2-Stream, PFC=Lawyer, F1/F2 fix, Entity-Compiled, ~20 dep updates) ✅ DONE (2026-05-17)
Session 30: Phase 29 — Uncanny-Valley v1.1 (+54L: F1/F2 fix 7x, context note, 10 dep updates, §10 cross-refs) ✅ DONE (2026-05-17)
Session 31: Phase 30 — Social-Cal v1.1 + AI-SM v2.1 (~50L: F1/F2 fix, 4-tier→2-Tier, 11+8 dep/ref updates) ✅ DONE (2026-05-17)
Session 32: Phase 31 — Love-Unified v1.2 + Idol v2.2 + Religion v2.4 + Alzheimer v1.2 + OCD fix (~90 edits: F1/F2, entity-compiled, VP §shift, 11 dep versions, Love-Romantic rename) ✅ DONE (2026-05-17)

Tầng 0-5:  ~31,000L across 20 sessions                    ✅ COMPLETE
Tầng 5b:   Entity-compiled + 4-tier + WBK, 1 session       ✅ COMPLETE
Tầng 6:    ~880-1,350L additions, 14 files, 7 sessions     ✅ COMPLETE
Tầng 7:    ~310-500L + F1/F2+4-tier, ~10 files, 4 sessions ✅ COMPLETE
Total:     30 phases, ~33,000L framework content, ~32 sessions
Nguyên tắc: chậm mà chắc, chất lượng cao nhất
```

### Backup strategy
- Mỗi REWRITE file: move v_old → backup/ TRƯỚC KHI viết mới
- Naming: `backup/FileName-vX.Y-backup.md`
- Giữ nguyên backup, không xóa

---

## §12 — MASTER CHECKLIST (v10.0 UPDATED)

### Phase 1-20: MECHANISM REWRITE + VERIFICATION ✅ ALL DONE

| # | Phase | File | Version | Lines | Status |
|---|---|---|---|---|---|
| 1 | Phase 1 | Inter-Body-Mechanism.md | NEW v1.0 | 1,500 | ✅ DONE |
| 2 | Phase 2 | Body-Feedback-Mechanism.md | v1.3→v2.0 | 1,519 | ✅ DONE |
| 3 | Phase 3 | Valence-Propagation.md | v1.4→v2.0 | 1,871 | ✅ DONE |
| 4 | Phase 4 | Body-Base.md | v2.1→v3.1 | 1,297 | ✅ DONE |
| 5 | Phase 5 | Body-Coupling.md | v1.1→v2.0 | 1,544 | ✅ DONE |
| 6 | Phase 6 | Self-Pattern-Match.md | v2.4→v3.0 | 2,614 | ✅ DONE |
| 7 | Phase 7 | By-Product-Gap-Resonance.md | v2.0→v3.1 | 1,540 | ✅ DONE |
| 8 | Phase 8 | Framework-Label.md | v1.1→v2.0 | 1,118 | ✅ DONE |
| 9 | Phase 9 | Gap-Direction.md | v1.1→v2.0 | 2,681 | ✅ DONE |
| 10 | Phase 10 | Reward-Signal-Architecture.md | v1.0→v2.0 | 1,986 | ✅ DONE |
| 11 | Phase 11 | Body-Feedback.md | v1.1→v2.0 | 892 | ✅ DONE |
| 12 | Phase 12 | Feeling.md | v2.2→v3.0 | 2,122 | ✅ DONE |
| 13 | Phase 13 | Logic-Feeling.md | v1.0→v2.0 | 1,572 | ✅ DONE |
| 14 | Phase 14 | Logic-Feeling-Balance.md | v1.0→v2.0 | 1,612 | ✅ DONE |
| 15 | Phase 15 | Neural-Processing-Flow.md | v1.0→v2.0 | 1,270 | ✅ DONE |
| 16 | Phase 16 | Agent-Mechanism.md | v1.0→v2.0 | 1,956 | ✅ DONE |
| 17 | Phase 17 | Connection.md | v3.3→v4.0 | 2,324 | ✅ DONE |
| 18 | Phase 18 | Why-Body-Knows.md | DRAFT→v1.1 | 1,273 | ✅ DONE |
| 19 | Phase 19 | Collective-Body.md | v1.2→v2.0 | 1,651 | ✅ DONE |
| 20 | Phase 20 | Terminology + audit | — | — | ✅ DONE |

### Phase 20b-31: ✅ ALL DONE (v11.0)

| # | Phase | Scope | Type | Status |
|---|---|---|---|---|
| 20b | Phase 20b | Entity-compiled propagation + verification (11 files) | Content fix | ✅ DONE |
| 21 | Phase 21 | Empathy.md v2.1→v3.0 | Major refine | ✅ DONE |
| 22 | Phase 22 | Gratitude.md v1.1→v2.0 | Major refine | ✅ DONE |
| 23 | Phase 23 | Obligation.md v1.0→v1.1 | Refine | ✅ DONE |
| 24 | Phase 24 | Status.md v2.0→v2.1 | Refine | ✅ DONE |
| 25 | Phase 25 | Drive+Novelty+Threat v1.1 (triple) | Refine | ✅ DONE |
| 26 | Phase 26 | Protect+Meaning+Boredom v1.1/v2.1 (triple) | Light refine | ✅ DONE |
| 27 | Phase 27 | Autonomy+AH v1.1 (pair) | Minor refine | ✅ DONE |
| 28 | Phase 28 | Love-Romantic v2.4 (+~120L) | Refine | ✅ DONE |
| 29 | Phase 29 | Uncanny-Valley v1.1 (+54L) | Refine | ✅ DONE |
| 30 | Phase 30 | Social-Cal v1.1+AI-SM v2.1 (~50L) | Refine | ✅ DONE |
| 31 | Phase 31 | Love-Unified+Idol+Religion+Alzheimer+OCD (~90 edits) | Refine | ✅ DONE |

### Final Verification Checklist (after Phase 31)
- [x] "Entity-Owned" appears NOWHERE in active framework (except backup/ + drill raw) ✅ VERIFIED 2026-05-17
- [x] "F1 Feeling / F2 Logic" appears NOWHERE as mechanism label ✅ VERIFIED 2026-05-17
- [x] "L3 operators: Protect" appears NOWHERE ✅ VERIFIED 2026-05-17
- [ ] Tất cả file versions internally consistent (partial — some stale deps remain)
- [ ] Cross-ref §numbers đúng across all files (partial — WBK+VP refs verified)
- [x] Terminology consistent với Framework-Label.md v3.0 ✅ Entity-compiled propagated

---

## §13 — FULL IMPACT MAP (v5.0 EXPANDED)

### Drill insights → file mapping

| Insight | Primary file (REWRITE Phase 1-19) | Secondary (P20) |
|---|---|---|
| ① Body-Need 2-source | BFM v2.0 ✅, Body-Base v3.0 ✅ | — |
| ② Architecture B | Inter-Body ✅, Body-Base ✅, RSA v2.0 (P10), Why-Body-Knows (P18), Collective-Body (P19), NPF v2.0 (P15) | — |
| ③ Social = Requirement | Inter-Body ✅, Connection v4.0 (P17), Collective-Body (P19) | — |
| ④ By-Product Match | Inter-Body ✅, Resonance v3.1 ✅, Agent v2.0 (P16), Gap-Direction v2.0 (P9) | Empathy |
| ⑤ 3 Cost Sources | Inter-Body ✅, Resonance v3.1 ✅, Label v2.0 (P8) | — |
| ⑥ Compiled/Fresh | Inter-Body ✅, SPM ✅, Resonance ✅, LF v2.0 (P13), LFB v2.0 (P14), Label (P8), Feeling (P12), RSA (P10), NPF (P15) | Research/ |
| ⑦ 5-Channel Vector | Inter-Body ✅, Connection v4.0 (P17), Label v2.0 (P8), NPF v2.0 (P15) | — |
| ⑧ Domain = Arbiter | Inter-Body ✅, LFB v2.0 (P14 — HƯỚNG calibrate!) | (many) |
| Entity-Compiled | Inter-Body ✅, VP ✅, Agent (P16), Label (P8), Collective-Body (P19) | Empathy, Gratitude, Obligation |
| PFC = Lawyer | Inter-Body ✅, SPM ✅, Resonance ✅, Feeling (P12), LF (P13), LFB (P14), NPF (P15), Why-Body-Knows (P18) | — |
| 3-Layer Evolution | Inter-Body ✅, Why-Body-Knows (P18), Collective-Body (P19) | — |
| 2-Stream Architecture | Resonance v3.1 ✅, Gap-Direction v2.0 (P9), Label v2.0 (P8) | — |
| L3 fix | Body-Base v3.0 ✅, NPF v2.0 (P15 — §10.3 operator fix) | — |
| Ben Franklin | Inter-Body ✅ | Obligation |
| Type B→A Development | RSA v2.0 (P10), Why-Body-Knows (P18) | — |
| Collective-Gap Detect | Collective-Body v2.0 (P19) | — |
| Calibration Direction | LFB v2.0 (P14 — domain=direction, not L/F ratio) | — |
| 2-Source at Hardware | NPF v2.0 (P15 — Sensory-Driven=bottom-up, Pattern-Driven=top-down) | — |
| Dual Check | LFB v2.0 (P14 — body=QC, domain=arbiter) | — |

---

## §14 — TẦNG 6: OBSERVATION LAYER CASCADE (Phase 21-27)

### §14.0 — Tại sao cascade cần thiết

```
Mechanism layer (Tầng 0-4) = NỀN TẢNG → ĐÃ REWRITE (Phase 1-19).
Observation layer = NƠI READER GẶP FRAMEWORK → CHƯA cascade.

VÍ DỤ INCONSISTENCY hiện tại:
  Connection v4.0 nói: "2-Stream Architecture: Stream 1 habituates, Stream 2 deepens"
  Empathy v2.1 nói: ... (KHÔNG MENTION 2-Stream, by-product match, Architecture B)
  → Reader đọc Connection → đọc Empathy → confused: "concepts này đi đâu?"

Observation files = PRIMARY INTERFACE cho reader:
  Reader hỏi "empathy là gì?" → đọc Empathy.md
  Reader hỏi "gratitude là gì?" → đọc Gratitude.md
  → Nếu observation files thiếu drill insights → reader THIẾU framework mới nhất.
```

### §14.1 — Nguyên tắc chung (áp dụng tất cả Phase 21-27)

```
TRƯỚC KHI VIẾT MỖI FILE:
  □ Đọc file hiện tại TOÀN BỘ
  □ Đọc 2-3 mechanism files dependencies (đã rewrite)
  □ Xác định: concepts NÀO relevant cho scope file này?
  □ Xác định: sections NÀO cần thêm/enrich vs giữ nguyên?

KHI VIẾT:
  □ Thêm concepts ORGANIC (weave vào narrative, không bolted-on)
  □ Giữ nguyên sections đã tốt
  □ Thêm NEW subsection ở đúng vị trí logic
  □ Update Honest Assessment (+🟡 items mới)
  □ Update cross-refs

SAU KHI VIẾT:
  □ ALL research citations preserved?
  □ ALL signature examples preserved?
  □ Honest Assessment updated?
  □ Vocabulary consistent với Framework-Label v2.0?
```

---

## §14.2 — PHASE 21: Empathy.md v2.1 → v3.0 MAJOR REFINE

### Tại sao?
- OBSERVATION FILE quan trọng nhất cho social mechanism
- Connection v4.0 (Phase 17) đã integrate 2-Stream, by-product match, PFC=Lawyer
- Empathy = "observable output of connection mechanism" → PHẢI reflect mechanism updates
- Có F1/F2 + 2-luồng nhưng THIẾU: Architecture B, 2-Stream Resonance, by-product match,
  PFC=Lawyer, Domain=Arbiter, 5-Channel, Compiled/Fresh axis

### Concepts cần integrate

```
① ARCHITECTURE B (WHY empathy = general-purpose)
  → Empathy KHÔNG phải "module riêng" hay "brain area"
  → Empathy = observable output khi general-purpose reward system
    process AGENT input qua SPM → body simulate → positive valence
  → Vị trí: thêm vào §0 hoặc §1 (foundation framing)

② 2-STREAM trong context empathy
  → Stream 1: "Thấy bé khóc → body co rúm" (hardware, automatic, unidirectional)
  → Stream 2: "Biết bạn buồn → respond → bạn feel → loop" (SPM mutual, bidirectional)
  → Empathy qua Stream 1 = automatic, habituates, không cần "hiểu"
  → Empathy qua Stream 2 = deep, grows, cần SPM compiled mutual
  → Vị trí: NEW §X hoặc enrich §3-§4

③ BY-PRODUCT MATCH trong empathy context
  → Empathy = response khi by-product match triggers body simulate
  → B fill gap CỦA B → output match A's SPM → A's body simulate B's state
  → False empathy: by-product match FAIL nhưng PFC=Lawyer fabricate
  → Vị trí: enrich §2 mechanism hoặc NEW subsection

④ PFC=LAWYER × empathy
  → PFC may report "tôi đồng cảm" nhưng body KHÔNG actually fire
  → "Virtue signaling" = PFC narrative without body-base empathy
  → PFC may SUPPRESS genuine empathy ("không nên thương kẻ thù")
  → Vị trí: enrich §8 hoặc NEW subsection

⑤ COMPILED/FRESH empathy
  → Compiled empathy: automatic response (mẹ-con, bạn thân lâu năm)
  → Fresh empathy: PFC draft (người lạ, cross-cultural, novel situation)
  → Expert therapist = compiled empathy cho nhiều patterns (cost ≈ 0)
  → Novice helper = fresh empathy cho mọi case (cost CAO → burnout)
  → Vị trí: enrich §5-§6 hoặc NEW §X

⑥ DOMAIN=ARBITER cho empathy
  → Empathy có thể SAI (body simulate sai state của người khác)
  → Domain reality = check cuối: hành động dựa trên empathy → domain feedback
  → Over-empathy: body simulate QUÁ MẠNH → overwhelm → paralysis
  → Vị trí: enrich §9 failures hoặc Honest Assessment
```

### Must preserve from v2.1
- §0 Opening (empathy = observable output of connection) — keep + ENHANCE
- §1-§2 Mechanism (SPM F1 + ❸ positive valence) — keep + ADD 2-Stream
- §3-§4 8 pathways — keep (already strong)
- §5-§6 Development + variation — keep + ADD Compiled/Fresh
- §7-§8 Practice, failures — keep + ADD PFC=Lawyer
- §9 Cross-species + non-verbal — keep + ADD Stream 1 framing
- §10 Burnout mechanism — keep + ENRICH with 3-cost
- §11 Honest Assessment — UPDATE with new 🟡
- ALL research citations (Ekman, Decety, Singer, de Waal, etc.)

### Must read before writing
- Empathy.md full file (~1,824L)
- Connection.md v4.0 §4.2 (2-Stream), §4.3 (3-cost)
- By-Product-Gap-Resonance.md v3.1 §2 (2-Stream model)
- Inter-Body-Mechanism.md §5 (by-product match), §7 (PFC=Lawyer)

---

## §14.3 — PHASE 22: Gratitude.md v1.1 → v2.0 MAJOR REFINE

### Tại sao?
- Gratitude = observation parameter TÍCH HỢP CAO NHẤT (9 components từ 9+ files)
- 9 components bao gồm SPM, Connection, Status, VP — tất cả ĐÃ REWRITE
- Zero new concepts hiện tại → GAP lớn nhất
- By-product match ĐẶC BIỆT relevant: gratitude = response khi NHẬN by-product từ agent

### Concepts cần integrate

```
① ARCHITECTURE B → gratitude = emergent từ general-purpose system (không phải special module)
② BY-PRODUCT MATCH → gratitude fire khi:
   Agent B's action fill gap CỦA B → by-product reach A → match A's gap → A reward
   + A DETECT source = B (source attribution) → gratitude toward B
③ PFC=LAWYER → "Cảm ơn xã giao" = PFC narrative, body KHÔNG fire
   → Genuine gratitude = body fire. False = PFC script only.
④ 2-TẦNG CALIBRATION → gratitude baseline = calibrated
   → Culture inject "phải biết ơn" = Đường 2b → compile → automatic
   → Direct experience "giúp đỡ thật" = Đường 2a → compile → deep
⑤ COMPILED/FRESH → compiled gratitude (automatic "cảm ơn") vs fresh (genuine appreciation)
⑥ DOMAIN=ARBITER → gratitude can be WRONG (grateful to manipulator)
```

### Must preserve from v1.1
- §1 Definition (observation parameter, emergent) — keep + ENHANCE
- §2 9 Prerequisites — keep ALL 9, ADD mechanism notes
- §3 Anti-Habituation (Variation + Comparison + Ritual) — keep (strong)
- §4 Baseline Shift conditions — keep
- §5 Gift-Obligation Spectrum — keep + ADD by-product match framing
- §6 "Cảm Ơn" = body-base tool — keep
- §7 Connection Maintenance — keep + ADD 2-Stream note
- §8 Cases — keep + ENRICH
- ALL research citations
- Tôn giáo discovery insight (empirical without mechanism)

### Must read before writing
- Gratitude.md full file (~1,542L)
- Connection.md v4.0 (3 Generative Primitives, 2-Stream)
- Empathy.md v3.0 (by then complete — empathy ⊂ gratitude prerequisites)
- Inter-Body-Mechanism.md §5 (by-product match)

---

## §14.4 — PHASE 23: Obligation.md v1.0 → v1.1 REFINE

### Tại sao?
- Exchange = BY-PRODUCT MATCH core application case
- Obligation v1.0 đã mô tả exchange mechanism TỐT nhưng thiếu explicit by-product match framing
- PFC=Lawyer relevant: rationalization about obligations

### Key additions (~100-150L)
```
① §0 hoặc §1: +Architecture B framing (obligation = tracking mechanism
   trong general-purpose system, not special social module)
② §2 hoặc §3: +By-product match explicit (exchange = mutual by-product matching)
   "Tôi làm A cho sếp (fill gap CỦA TÔI: salary) → by-product (work output)
    match gap CỦA SẾP (need work done) → sếp reward → exchange balanced"
③ §6 hoặc §7: +PFC=Lawyer (rationalize unfair obligation, suppress "should refuse")
④ §10: +Honest Assessment update (+🟡 by-product match framing)
⑤ Cross-refs update: Connection v4.0, Empathy v3.0, Gratitude v2.0
```

### Must preserve
- 4-stage formation mechanism — keep
- 5-factor formula + Status Gap multiplier — keep
- 6-type spectrum — keep
- Tiền = obligation technology — keep
- 3 cơ chế độc lập — keep
- Community O(1) scaling — keep
- ALL research citations

---

## §14.5 — PHASE 24: Status.md v2.0 → v2.1 REFINE

### Tại sao?
- Status = Resource Access Map → fits Architecture B (general-purpose system nên track resources)
- PFC=Lawyer relevant: status self-deception
- Compiled/Fresh relevant: compiled status assessments vs fresh evaluations

### Key additions (~100-150L)
```
① §0 hoặc §1: +Architecture B framing (status = resource access MAP
   emergent từ general-purpose system tracking what's available)
② §2 hoặc §3: +Compiled/Fresh status (compiled: "tôi = leader" automatic;
   fresh: novel social context → PFC evaluate → costly)
③ §5 hoặc §6: +PFC=Lawyer (status rationalization, "tôi xứng đáng" narrative)
④ §7 Honest Assessment update
⑤ Cross-refs update
```

### Must preserve
- Resource Access Map model — keep (core contribution)
- 3 modes (Lấy/Trao đổi/Comply) — keep
- Animal→human spectrum — keep
- Disruption cycle — keep
- ALL research citations

---

## §14.6 — PHASE 25: Drive + Novelty + Threat REFINE (triple)

### Tại sao triple?
- 3 files cùng scope level (Observation parameter), cùng era (v1.0, 2026-04-20)
- Cùng pattern thiếu: Architecture B + Compiled/Fresh
- Refine tương tự → batch hiệu quả hơn

### Drive.md v1.0 → v1.1 (~50-80L additions)
```
① +Architecture B: drive = architecture's way of mobilizing toward gap closure
② +Compiled/Fresh: compiled drive (automatic) vs fresh drive (deliberate pursuit)
③ +Domain=Arbiter note: drive direction can be wrong
```

### Novelty.md v1.0 → v1.1 (~50-80L additions)
```
① +Architecture B: novelty signal = general-purpose system detecting UNCOMPILED input
② +Compiled/Fresh: novel = BY DEFINITION fresh (not yet compiled)
   → Novelty signal = "switch to fresh processing mode"
③ +2-tầng note: what counts as "novel" = calibrated per individual
```

### Threat.md v1.0 → v1.1 (~50-80L additions)
```
① +Architecture B: threat = general-purpose system detecting GAP TOWARD LOSS
② +Compiled/Fresh: compiled threat (automatic avoidance, phobia)
   vs fresh threat (novel danger → PFC evaluate → costly)
③ +PFC=Lawyer: threat rationalization ("không sao đâu" khi body đang báo nguy)
```

### Must preserve (all 3 files)
- Core mechanism descriptions — keep
- NE cascade, 5-level spectrum (Threat) — keep
- Novelty loop, 2 modes (Novelty) — keep
- ALL research citations

---

## §14.7 — PHASE 26: Protect + Meaning + Boredom LIGHT REFINE (triple)

### Protect.md v1.0 → v1.1 (~30-50L)
```
① +Architecture B alignment: protect = observation khi general-purpose system
   detects ownership threat → loss aversion activates
② +Compiled/Fresh note: compiled protect (automatic loss aversion)
   vs fresh (novel threat to valued entity → PFC evaluate)
```

### Meaning.md v2.0 → v2.1 (~30-50L)
```
① +Architecture B alignment: meaning = life-level Anchor-Schema
   emergent từ general-purpose system's long-term pattern compilation
② +Domain=Arbiter: meaning can be WRONG (cult members find deep meaning)
```

### Boredom.md v1.0 → v1.1 (~30-50L)
```
① +Architecture B: boredom = signal khi general-purpose system
   has NO active gap to process (resources idle)
② +Compiled/Fresh note: over-compiled environment → no fresh input → boredom
```

---

## §14.8 — PHASE 27: Autonomy.md + Autonomy-Hardware.md MINOR REFINE

### Autonomy.md v1.0 → v1.1 (~20-30L)
```
① +Architecture B alignment note (brief, §0 or §1)
② Cross-refs update
```

### Autonomy-Hardware.md v1.0 → v1.1 (~20-30L)
```
① +Architecture B alignment note (brief, §0 or §1)
② Cross-refs update
```

---

## §14.9 — IMPACT MAP UPDATE (Tầng 6)

| Insight | Tầng 6 Observation Cascade |
|---|---|
| ① Architecture B | ALL 14 files (P21-P27) |
| ④ By-Product Match | Empathy (P21), Gratitude (P22), Obligation (P23) |
| ⑤ 3 Cost Sources | Empathy (P21 — burnout), Obligation (P23 — exchange cost) |
| ⑥ Compiled/Fresh | Empathy (P21), Gratitude (P22), Status (P24), Drive+Novelty+Threat (P25), Protect+Boredom (P26) |
| PFC = Lawyer | Empathy (P21), Gratitude (P22), Obligation (P23), Status (P24), Threat (P25) |
| Domain = Arbiter | Empathy (P21), Gratitude (P22), Meaning (P26) |
| 2-Stream | Empathy (P21), Gratitude (P22) |
| 2-Tầng Calibration | Gratitude (P22), Novelty (P25) |
| Entity-Compiled | (already in mechanism files — observation files reference, not define) |
| 5-Channel | Empathy (P21) |

---

## §14.10 — ESTIMATED EFFORT

```
Phase 21 (Empathy):       ~200-300L additions, moderate restructure    [1 session]
Phase 22 (Gratitude):     ~200-300L additions, moderate restructure    [1 session]
Phase 23 (Obligation):    ~100-150L additions, surgical                [½ session]
Phase 24 (Status):        ~100-150L additions, surgical                [½ session]
Phase 25 (D+N+T triple): ~150-240L additions total, 3 files           [1 session]
Phase 26 (P+M+B triple): ~90-150L additions total, 3 files            [½ session]
Phase 27 (A+AH):         ~40-60L additions total, 2 files             [¼ session]

TOTAL: ~880-1,350L additions across 14 files
       ~5-6 sessions estimated
       (vs Phase 1-19: ~19 sessions for ~30,000L)
```

---

## §15 — TẦNG 5b: CONTENT FIX — CORE FILES (Phase 20b, v10.0 MERGED)

### §15.0 — Tại sao cần Phase 20b (v10.0: merged 20b+20c, research deferred)

```
Deep audit (2026-05-17) phát hiện 3 lỗi NỘI DUNG nghiêm trọng
còn sót sau Phase 1-20:

① "F1 Feeling / F2 Logic" vẫn dùng NHƯ MECHANISM LABEL (10+ files)
   → Framework xác định: F1=Compiled, F2=Fresh (mechanism).
   → "Feeling/Logic" = OBSERVER LABELS ONLY (shareability-based).
   → Lỗi này ĐẶC BIỆT nghiêm trọng vì Compiled/Fresh axis
     là CORE INSIGHT của drill — nếu reader đọc "F1 Feeling"
     → hiểu sai mechanism → hiểu sai TOÀN BỘ framework.
   → THẬM CHÍ Connection v4.0 (đã REWRITE Phase 17) vẫn sót!

② "4-tier calibration" còn trong 6 files NGOÀI Core-Deep-Dive
   → Đã fix bên trong Core-Deep-Dive (Phase 20).
   → Nhưng Ask-AI, Core-Software, Research files chưa fix.
   → Reader đọc Ask-AI → thấy "4-tier" → conflict với WBK v1.1 "2-tầng".

③ "Why-Body-Knows §4/§5" section refs sai (8 files)
   → WBK v1.1 renumbered: §4→§3 (calibration), §5→§6 (failure modes).
   → 8 files vẫn trỏ đến section number CŨ.
   → Reader follow ref → đến section KHÁC → confused.

FIX TRƯỚC Tầng 6-7 vì: observation + research files REFERENCE core.
Nếu core labels sai → cascade sai → reader confused.
```

---

## §15.1 — PHASE 20b: MERGED CONTENT FIX (v10.0)

> v10.0: Merged old Phase 20b (F1/F2) + Phase 20c (4-tier + WBK §refs).
> Research file fixes (Love-Romantic, Uncanny-Valley, Social-Cal, AI-Self-Model, Alzheimer)
> → DEFERRED sang Phase 28-31 (fix cùng content refine, tránh double-touching).

### Vấn đề cốt lõi

```
CŨ (sai — vẫn tồn tại):
  "SPM chạy 2 functions: F1 Feeling (body simulate) + F2 Logic (PFC predict)"
  → Ngụ ý: F1 = Feeling, F2 = Logic LÀ cơ chế.

MỚI (đúng — đã establish trong SPM v3.0, Logic-Feeling v2.0):
  "SPM chạy 2 functions: F1 Compiled (body simulate, automatic) + F2 Fresh (PFC draft, costly)"
  → "Feeling" / "Logic" = OBSERVER LABELS khi PFC nhìn F1/F2 output.
  → CƠ CHẾ = Compiled ↔ Fresh spectrum.

WBK v1.1 renumbered:
  OLD §4 (calibration) → NEW §3 (2-TẦNG CALIBRATION + 2 ĐƯỜNG VÀO)
  OLD §5 (failure modes) → NEW §6 (KHI BODY SAI + DUAL CHECK)
```

### PART A: F1/F2 mechanism label fix (4 core files)

```
① Connection.md v4.0 (L90, L383)
  → "F1 Feeling + F2 Logic" → "F1 Compiled + F2 Fresh"
  → Context: §0 opening + §3 3 Generative Primitives
  → QUAN TRỌNG: Connection = GATEWAY file (reader đọc ĐẦU TIÊN)

② Compliance-Floor.md (L28)
  → dependency line: "F1 Feeling + F2 Logic" → add "(= F1 Compiled + F2 Fresh)"

③ Emergent-Patterns.md (L1204)
  → cross-ref line: same fix

④ Core-Software.md (L699)
  → "F1 Feeling (body simulate target) + F2 Logic (PFC chain predict)"
  → Rewrite with Compiled/Fresh + note observer labels

DEFERRED sang Phase 21-22: Empathy.md (L113, L858), Gratitude.md (L548)
DEFERRED sang Phase 28-31: Love-Romantic, Uncanny-Valley, Social-Cal, Alzheimer
```

### PART B: 4-tier → 2-tầng (4 non-research files)

```
① Ask-AI.md (L25, L703)
  → "4-tier calibration" → "2-tầng calibration (Darwinian + Hebbian)"

② Core-Software.md (L23, L311, L1352)
  → 3 places: deps line + WBK ref + closing ref
  → (cũng fix F1/F2 ở PART A ④ — touch 1 lần cho cả 2)

③ Natural-Development.md (L2024)
  → 1 place: body text

④ Child-Development-Mechanism.md (L1738)
  → 1 place: section with 4 tầng breakdown → rewrite to 2-tầng+2-đường
  → HEAVIEST fix (like Cortisol §1.3 rewrite done in Phase 20)

✅ DONE Phase 30: Social-Cal v1.1 (11 deps + 5 content blocks) + AI-SM v2.1 (8 refs)
```

### PART C: WBK §ref fixes (8 files)

```
① 01-Foundation.md (L110, L389→§6; L488→§6)
② 02-Dissonance.md (L409, L1587→§6)
③ Collective-Body.md (L379→§6)
④ Logic-Feeling-Balance.md (L430→§6; L444→§6; L1499→§3)
⑤ Logic-Feeling-Failure-Examples.md (L17, L53, L446, L788→§6)
⑥ Knowledge-Flow.md (L585→§3)
⑦ Core-Software.md (L311→§3) (also PART A+B)
⑧ Child-Development-Mechanism.md (L1738→§3) (also PART B)
```

### Thứ tự triển khai Phase 20b

```
Bước 1: Connection.md v4.0 — F1/F2 fix (GATEWAY, highest priority)
Bước 2: Core-Software.md — F1/F2 + 4-tier + WBK §ref (3 fixes, 1 file)
Bước 3: Compliance-Floor + Emergent-Patterns — F1/F2 fix (2 quick files)
Bước 4: Ask-AI — 4-tier fix
Bước 5: Natural-Development + Child-Dev-Mechanism — 4-tier fix
Bước 6: WBK §ref fixes — 6 remaining files (01-Foundation thru Knowledge-Flow)
Bước 7: 01-File-Index.md — update entries for Phase 1-20b

Estimated: ~50 surgical edits, 1 session
```

---

## §16 — TẦNG 7: RESEARCH/APPLICATION CASCADE (Phase 28-31, v10.0 UPDATED)

### §16.0 — Tại sao cần Tầng 7

```
Research/Application files = NƠI FRAMEWORK GẶP THẾ GIỚI THẬT.
  Love-Romantic → reader muốn hiểu tình yêu
  OCD-Analysis → reader muốn hiểu OCD
  Social-Calibration → reader muốn hiểu xã hội

Nếu observation layer (Tầng 6) updated nhưng research layer vẫn dùng
old mechanism labels → reader confused KHI ĐỌC ỨNG DỤNG.

NHƯNG: Research files = APPLICATION, không phải MECHANISM.
  → REFINE (thêm concepts relevant), KHÔNG full rewrite.
  → Chủ yếu: F1/F2 labels + Compiled/Fresh + by-product match (nếu relevant)
  → LIGHTER touch hơn Tầng 6.

v10.0: Mỗi research phase HẤP THỤ F1/F2 + 4-tier fixes từ cũ Phase 20b/20c.
  → Fix mechanism labels CÙNG LÚC content refine = touch 1 lần, consistency cao hơn.
```

### §16.1 — PHASE 28: Love-Romantic.md v2.3 → v2.4 REFINE

```
TẠI SAO:
  - Love-Romantic = MAJOR research file (~2,237L)
  - Dùng "F1 Feeling + F2 Logic" 2 places (L86, L547) → mechanism label sai
  - References SPM v2.1, VP v1.4, BFM v1.2 (all outdated versions)
  - Missing: 2-Stream Resonance framing (limerence = Stream 1 dominant;
    deep love = Stream 2 growth VƯỢT Stream 1 decline)
  - Missing: by-product match (love = sustained mutual by-product match)

KEY ADDITIONS (~100-150L):
  ① F1/F2 label fix (Compiled/Fresh)
  ② +§ or subsection: 2-Stream Resonance framing for love phases
  ③ +by-product match note for love formation
  ④ +PFC=Lawyer note (limerence = PFC rationalizes body response)
  ⑤ Honest Assessment update
```

### §16.2 — PHASE 29: Uncanny-Valley.md v1.0 → v1.1 REFINE

```
TẠI SAO:
  - Uncanny-Valley = SPM-based analysis (~1,457L)
  - F1/F2 label = CORE of analysis (4+ places, table headers)
  - Đây là file CẦN ĐỌC KỸ NHẤT trước khi fix
  - SPM context = central → Compiled/Fresh reframe changes narrative

KEY ADDITIONS (~80-120L):
  ① F1/F2 label fix throughout (CAREFUL — context matters)
  ② +Compiled/Fresh reframe in SPM analysis sections
  ③ +note: "Uncanny = Fresh processing FAILS to compile entity"
  ④ Honest Assessment update
```

### §16.3 — PHASE 30: Social-Calibration + AI-Self-Model REFINE (+absorbed fixes)

```
Social-Calibration.md v1.0 → v1.1 (~50-80L):
  ① F1/F2 label fix (L679) — absorbed từ cũ Phase 20b
  ② 4-tier→2-tầng fix (L44, L1692) — absorbed từ cũ Phase 20c
  ③ +Architecture B note for calibration system framing

AI-Self-Model.md v2.0 → v2.1 (~30-50L):
  ① 4-tier→2-tầng fix (L35, L1425, L1472) — absorbed từ cũ Phase 20c
  ② Light alignment with Dual Check concept
```

### §16.4 — PHASE 31: Remaining Research LIGHT REFINE

```
Love-Unified.md v1.1 → v1.2 (~30L):
  ① Light F1/F2 note if present
  ② Cross-refs alignment

Religion.md v2.3 → v2.4 (~20L):
  ① Light alignment notes
  ② Cross-refs

Idol-Phenomenon.md v2.1 → v2.2 (~20L):
  ① Light alignment notes

Alzheimer-Analysis.md v1.1 → v1.2 (~20L):
  ① F1/F2 label fix (L1593)
  ② Cross-refs

OCD/Autism/PTSD/Parkinson/Nicotine:
  → EVALUATE during Phase 31 — may not need changes
  → Health Conditions files = domain-specific, mechanism refs indirect
```

---

## §17 — UPDATED ESTIMATED EFFORT (v10.0)

```
═══════════ COMPLETED ═══════════════════════════════════
Phase 1-20:  19 rewrites + verification     ✅ ~31,000L    [20 sessions]

═══════════ TẦNG 5b: CONTENT FIX (v10.0 MERGED) ═══════
Phase 20b:   F1/F2+4-tier+WBK §refs        ~50 edits      [1 session]
             (core files only, research deferred sang Tầng 7)

═══════════ TẦNG 6: OBSERVATION CASCADE ═════════════════
Phase 21-22: Empathy + Gratitude (major)    ~400-600L      [2 sessions]
Phase 23-24: Obligation + Status            ~200-300L      [1 session]
Phase 25:    Drive+Novelty+Threat           ~150-240L      [1 session]
Phase 26:    Protect+Meaning+Boredom        ~90-150L       [½ session]
Phase 27:    Autonomy+AH                    ~40-60L        [¼ session]

═══════════ TẦNG 7: RESEARCH CASCADE (+absorbed fixes) ══
Phase 28:    Love-Romantic (+F1/F2 fix)     ~100-150L      [½ session]
Phase 29:    Uncanny-Valley (+F1/F2 fix)    ~80-120L       [½ session]
Phase 30:    Social-Cal+AI-SM (+F1/F2+4t)   ~80-130L       [½ session]
Phase 31:    Remaining (+Alz F1/F2)         ~50-100L       [½ session]

═══════════ TỔNG KẾT (v10.0) ═══════════════════════════
  Remaining: Phase 20b → Phase 31 = 11 work units
  Estimated: ~7 sessions (saved 1 session từ merge 20b+20c)
  Lines:     ~1,200-1,900L additions + ~50 content-fix edits
  Files:     ~35 files touched (mỗi file touch 1 LẦN duy nhất)
  Priority:  Phase 20b FIRST → Tầng 6 → Tầng 7
  Nguyên tắc: chậm mà chắc, chất lượng cao nhất
```
