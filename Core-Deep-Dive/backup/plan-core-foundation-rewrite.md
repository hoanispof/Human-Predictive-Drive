# Plan: Core Foundation Files Rewrite v2
# Viết mới các file nền tảng — đồng bộ với toàn bộ drill + cascade đã hoàn thành

> **Ngày tạo:** 2026-05-24
> **Mục đích:** Tạo 1 file mới + rewrite 6 file core foundation — những file đầu tiên reader tiếp cận framework.
> Sau 28+ session drill, ~130+ files, ~35,000+ lines — các file nền tảng này lạc hậu nghiêm trọng.
> **Phương pháp:** Mỗi session = 1 file. Phân tích kỹ trước → lựa chọn phương án → viết mới.
> **Nguyên tắc:** Chậm mà chắc. Chất lượng cao nhất.
> **Thứ tự logic:** Collective.md (NEW) → Domain/ folder (foundation concepts) → PFC/ → Observation/ → Core-Software cuối (BẢN ĐỒ vẽ sau khi khảo sát xong).

---

## Tổng quan 7 sessions — thứ tự triển khai

| Session | File | Type | Lines | Version | Tình trạng | Folder |
|---------|------|------|-------|---------|------------|--------|
| 0 | Collective/Collective.md | **NEW** | ~500-700 | — | CHƯA TỒN TẠI — integration hub | Collective/ |
| 1 | Domain/Domain.md | REWRITE | ~487 | v1.0 | SƠ KHAI, thiếu domain types | Domain/ |
| 2 | Domain/Drill-Emergent-Pattern.md | REWRITE | ~1,302 | v1.2 | SUPERSEDED — giữ/bỏ/thu gọn? | Domain/ |
| 3 | Domain/Conflict-Dynamics.md | REWRITE | ~546→621 | v1.1→v2.0 | ✅ DONE 2026-05-24 | Domain/ |
| 4 | PFC/Imagination/Imagination.md | REWRITE | ~610→793 | v1.0→v2.0 | ✅ DONE 2026-05-24 | PFC/ |
| 5 | Observation/Liking-Wanting.md | REWRITE | ~1,037→1,205 | v1.1→v2.0 | ✅ DONE 2026-05-24 | Observation/ |
| 6 | Core-Software.md | REWRITE | ~1,408→1,732 | v1.0→v2.0 | ✅ DONE 2026-05-24 | Root |

**Tại sao thứ tự này:**
- **Collective.md ĐẦU TIÊN** — file MỚI, cần plan riêng (Collective/plan-collective-overview.md). Collective ảnh hưởng cá nhân sâu, nhiều file rewrite sau sẽ reference. Folder DUY NHẤT thiếu integration hub.
- Domain/ folder tiếp theo (3 files liên tiếp) — foundation concepts, không switch context
- Core-Software CUỐI CÙNG — file này là BẢN ĐỒ tóm tắt mọi file khác. Vẽ bản đồ SAU khi đã khảo sát xong địa hình. Tránh phải revisit khi các file kia thay đổi.

---

## SESSION 0: Collective.md — NEW FILE

> **Plan riêng:** Collective/plan-collective-overview.md (phân tích chi tiết)

### Tóm tắt
- Collective/ folder có 5 files nhưng KHÔNG có entry point — folder DUY NHẤT thiếu hub
- Collective-Body.md = de facto start nhưng là MECHANISM file, không phải overview
- "Collective ảnh hưởng cá nhân thế nào" = content CHƯA tập trung ở đâu

### Unique contribution của Collective.md
- §0: Collective là gì (emergent, KHÔNG phải entity riêng)
- §1: Bridge Body-Base → Collective (Compilable Architecture)
- §2: 5 con đường collective ảnh hưởng cá nhân (trust compile, "behaves like domain", schema inheritance, status access, system compilation)
- §3: Folder architecture + reading flow (5 files)
- §4: Collective × Key Concepts (Technology×Scale, By-Product-Scale L3, Hardware Subsidy per scale)
- §5: Individual vs Collective — ranh giới (khác SCALE, không khác RANK)

### Mục tiêu
- ~500-700L, hub role, KHÔNG repeat mechanism từ sub-files
- §2 (5 con đường) = unique contribution quan trọng nhất

---

## Context: Domain/ folder hiện tại (6 files)

| File | Version | Status | Cần rewrite? |
|------|---------|--------|-------------|
| Domain.md | v1.0 | SƠ KHAI | ✅ SESSION 1 |
| Drill-Emergent-Pattern.md | v1.2 | SUPERSEDED | ✅ SESSION 2 |
| Conflict-Dynamics.md | v2.0 | ✅ DONE 2026-05-24 | ✅ SESSION 3 |
| Discovery-vs-Expansion.md | v1.0 | Cascade refine 2026-05-23 | ❌ OK |
| Knowledge-Flow.md | v1.0 | Cascade refine 2026-05-23 | ❌ OK |
| Domain-Mapping-Drive.md | v2.0 | Cascade refine 2026-05-23, ~3,666L | ❌ OK |

→ 3/6 files cần rewrite. 3/6 đã qua cascade, chất lượng tạm ổn.

---

## Context: Domain/ folder hiện tại (6 files)

| File | Version | Status | Cần rewrite? |
|------|---------|--------|-------------|
| Domain.md | v1.0 | SƠ KHAI | ✅ SESSION 1 |
| Drill-Emergent-Pattern.md | v1.2 | SUPERSEDED | ✅ SESSION 2 |
| Conflict-Dynamics.md | v2.0 | ✅ DONE 2026-05-24 | ✅ SESSION 3 |
| Discovery-vs-Expansion.md | v1.0 | Cascade refine 2026-05-23 | ❌ OK |
| Knowledge-Flow.md | v1.0 | Cascade refine 2026-05-23 | ❌ OK |
| Domain-Mapping-Drive.md | v2.0 | Cascade refine 2026-05-23, ~3,666L | ❌ OK |

→ 3/6 files cần rewrite. 3/6 đã qua cascade, chất lượng tạm ổn.

---

## SESSION 1: Domain.md → v2.0

### Tại sao ưu tiên 1
- File cổ nhất (2026-03-30) — foundation concept "thực tế bên ngoài human"
- File nhỏ (~487L) = warm-up tốt trước các file phức tạp hơn
- Domain types mới sẽ được reference bởi Core-Software, Conflict-Dynamics, và nhiều file khác

### Phân tích hiện trạng

**Phần HAY — giữ + phát triển:**
- §1 "Phản chiếu, không nhìn trực tiếp" — epistemological framing rất đẹp (gió + lá bay)
- §2 8 đặc điểm domain — vẫn đúng, cần enrich
- §2.1 3-nguồn constraint (Physics/Hardware/Collective) — HAY NHẤT, cần trở thành trục chính
- §3 Scarcity = Engine — vẫn đúng, overlap Conflict-Dynamics §7

**Phần THIẾU — cần thêm:**
- [ ] **Domain Types phân loại** — bạn đề cập nhưng chưa tồn tại:
  - Reality Domain (vật lý, sinh học — feedback tức thì, objective, không phụ thuộc observer)
  - Abstract Domain (toán, logic — internal consistency, con người PHÁT HIỆN không TẠO RA)
  - Abstract-Dynamic Domain (xã hội, thị trường, văn hóa — abstract + THAY ĐỔI theo participants)
  - → Kết nối 3-nguồn constraint với domain types:
    Physics → Reality Domain
    Hardware → constraint chung mọi domain type
    Collective → tạo ra Abstract-Dynamic Domain
- [ ] **Dual Check principle** — body = quality controller, domain = final arbiter (Ask-AI v3.1)
- [ ] **Domain × Gap system** — "chưa biết = không có gap" áp dụng cho domain mapping
- [ ] **Domain × Compiled/Fresh** — compiled domain knowledge vs fresh exploration
- [ ] **Domain × Entity-Access** — mỗi entity = 1 cửa sổ vào domain
- [ ] **Domain × Simulation-Engine** — PFC simulate domain outcomes
- [ ] **Domain × Satiation** — mapping-drive satiation ≠ consumption satiation

**Phần CẦN LÀM RÕ scope — tránh trùng file khác:**
- §3 Scarcity = Engine → trùng Conflict-Dynamics.md §7. Giữ ngắn ở Domain.md, detail ở Conflict.
- Domain-Mapping-Drive.md v2.0 (~3,666L) đã cover "WHY map domain" rất sâu → Domain.md KHÔNG cần repeat, chỉ cần cross-ref
- §4 Imagine-Final × Domain → thin. Giữ brief, detail ở Imagine-Final.md v3.0

### Phương án rewrite

**Đề xuất: Phương án B — Rewrite toàn bộ, restructure**

Cấu trúc mới dự kiến:
```
§0 — Thesis: Domain = thực tế bên ngoài, chỉ biết qua phản chiếu
§1 — Epistemology: phản chiếu, không nhìn trực tiếp (giữ từ v1.0)
§2 — 3 Domain Types (Reality / Abstract / Abstract-Dynamic) ← NEW
§3 — 8 Đặc điểm domain (giữ + enrich từ v1.0)
§4 — 3-Nguồn Constraint × Domain Types (integrate §2.1 cũ) ← UPGRADED
§5 — Domain × Framework Concepts (Dual Check, Gap, Compiled/Fresh, Simulation-Engine, Satiation)
§6 — Honest Assessment
§7 — Open Questions
§8 — Cross-References
```

### Mục tiêu v2.0
- Domain types rõ ràng — reader biết 3 loại domain
- 3-nguồn constraint tích hợp hữu cơ vào domain types
- Dual Check principle rõ ràng
- Cascade concepts tích hợp hữu cơ, không bolted-on
- Scope rõ: KHÔNG trùng Domain-Mapping-Drive (WHY map) hay Conflict-Dynamics (conflict formula)

---

## SESSION 2: Drill-Emergent-Pattern.md — QUYẾT ĐỊNH + TRIỂN KHAI

### Tại sao ưu tiên 2
- Cùng Domain/ folder — làm liền sau Domain.md
- Câu hỏi lớn cần quyết định: giữ/bỏ/thu gọn?

### Phân tích content overlap chi tiết

| Section | Lines | Status | Đã supersede bởi | Còn giá trị unique? |
|---------|-------|--------|-------------------|---------------------|
| §1 Meta-frame | ~60L | OK | — | ✅ "Emergent pattern là gì" = unique framing |
| §2 Connection | ~0L | ✅ MOVED | Connection.md v5.0 | ❌ Đã tách |
| §3 Enemy | ~115L | ⚠️ | Rải rác | ✅ Chưa có file riêng cover đầy đủ |
| §4 Nurturing | ~90L | ⚠️ | Connection v5.0 + Bond-Architecture | 🟡 Baby schema + 4 yếu tố mirror → partial unique |
| §5 "Cho đi" | ~170L | ⚠️ | Obligation + Protect §7 | 🟡 "3 violation tests" unique, còn lại trùng |
| §6 Dependency | ~100L | ❌ | Entity-Access-Excess v1.0 | ❌ Hoàn toàn superseded |
| §7 Mixed Valence | ~75L | ❌ | Valence-Propagation v3.0 | ❌ VP v3.0 sâu hơn nhiều |
| §8 Group | ~85L | ⚠️ | Collective/ (5 files) + By-Product-Scale | ❌ Collective/ cover tốt hơn |
| §9 Violation | ~140L | ⚠️ | Anchor-Schema-Extreme-Example | ✅ Schema-level analysis unique |
| §10-11 | ~200L | — | — | Assessment + cross-refs |

**Kết luận: ~60% content đã superseded.** Còn giá trị unique ở §1, §3, §9 (và partial §4, §5).

### Phương án

**Đề xuất: Phương án B — THU GỌN (~400-600L)**

Giữ:
- §1 Emergent Patterns là gì — meta-frame (~60L, enrich)
- §3 Enemy/Threat Pattern — chưa có nơi nào cover đầy đủ (~100L, rewrite v7.8)
- §4 Nurturing — trim, giữ baby schema + 4 yếu tố, cross-ref Bond-Architecture (~60L)
- §9 Violation & Recovery — schema-level analysis unique (~120L, rewrite v7.8)
- Mỗi section khác → 5-10 lines tóm tắt + cross-ref file chuyên sâu

Bỏ (cross-ref thay thế):
- §6 Dependency → "See Entity-Access-Excess.md v1.0"
- §7 Mixed Valence → "See Valence-Propagation.md v3.0 §mixed"
- §8 Group → "See Collective/ folder (5 files)"

### Mục tiêu
- File gọn, không trùng lặp
- Phần còn lại = chất lượng v7.8 (Self-Pattern-Modeling thay mirror, signal strength thay layer priority)
- Cross-refs chính xác sang file chuyên sâu
- Thuộc Domain/ (origin of patterns, not scale)

---

## SESSION 3: Conflict-Dynamics.md → v2.0

### Tại sao ưu tiên 3
- Cùng Domain/ folder — hoàn thành 3/3 Domain/ rewrites
- Foundation vững (Overlap × Scarcity × Commitment) — chủ yếu enrichment

### Phân tích hiện trạng

**Phần VỮNG — giữ:**
- §1 Formula Overlap × Scarcity × Commitment — proven, clear
- §2 Khác biệt ≠ Xung đột — insight quan trọng
- §3 Giống nhau → Xung đột — paradox similarity
- §4 Perceived vs Actual scarcity — biến quan trọng nhất
- §5 Multi-scale — cùng formula, khác tham số
- §6 Chiến lược giải quyết — phá 1/3 điều kiện

**Phần CẦN ĐỒI MỚI:**
- [ ] Reference "Empathy-Mirror.md §6.5" → superseded. Dùng Self-Pattern-Modeling + By-Product-Gap-Resonance
- [ ] Imagine-Final chưa cập nhật v3.0 boundary (constructive simulation ONLY, ≠ hardware prediction)
- [ ] §11 cascade additions (Entity-Access, Simulation-Engine, Satiation) — tích hợp hữu cơ vào body text
- [ ] §5 Multi-scale — enrich với Collective/ folder (Coordination-Node, Collective-Body)
- [ ] §7 Scarcity engine — connect Gap-Distribution-Profile (supply side), Action-Space (capability)
- [ ] Domain types mới (Session 1) → conflict khác nhau ở Reality vs Abstract-Dynamic domain
- [ ] Old "L0>L1>L2>L3" language → signal strength
- [ ] Dùng "Imagine-Final" nhưng chưa phân biệt compiled vs constructive

### Phương án

**Đề xuất: Update in-place — giữ cấu trúc, enriched content**

Formula giữ nguyên. Sections giữ nguyên. Nội dung bên trong updated:
- References modernized
- Cascade concepts woven in (không bolted-on ở cuối)
- Domain types × conflict (Reality conflict vs Abstract-Dynamic conflict)
- Multi-scale enriched

### Mục tiêu v2.0
- Formula giữ nguyên (đã proven, đã consistent)
- All references current
- Cascade concepts tích hợp hữu cơ (xóa §11 cascade section riêng → weave vào body)
- Cross-refs chính xác

### ✅ DONE | 2026-05-24 | v1.1→v2.0 (~621L, was 546L)
- +§4.1 Domain Types × conflict (Reality resolve nhanh / Abstract-Dynamic persist)
- §11 cascade dissolved vào §1 (Entity-Access), §4 (Simulation-Engine), §5 (Collective), §6 (Satiation), §7 (Self-Pattern-Modeling)
- "Empathy-Mirror" → Self-Pattern-Modeling + By-Product-Gap-Resonance
- "melody" → gap-distribution (chính xác hơn cho competition context)
- Section numbering PRESERVED (§1-§10) — §4.1 subsection, §7 stays §7
- All references modernized, v1.1→backup

---

## SESSION 4: Imagination.md → v2.0

### Tại sao ưu tiên 4
- Chuyển sang PFC/ folder
- Vẫn DRAFT — file DUY NHẤT chưa bao giờ finalize

### Phân tích hiện trạng + scope với file liên quan

**3 file, 3 góc nhìn cùng hệ thống Simulation:**

| File | Góc nhìn | Status | Focus |
|------|----------|--------|-------|
| Simulation-Engine.md v1.0 | ARCHITECTURE | ✅ Done 2026-05-22 | 1 engine, 3 components, 3 axes |
| Imagine-Final.md v3.0 | PRODUCT | ✅ Done 2026-05-22 | Constructive simulation OUTPUT |
| **Imagination.md** | **PROCESS** | ✅ v2.0 | HOW PFC uses engine, fidelity, modes |

→ Imagination.md = PROCESS view. Scope rõ: KHÔNG trùng ENGINE (architecture) hay PRODUCT (output).

**Phần HAY — giữ + reframe:**
- §1 2 giá trị (nhanh hơn + mở access) — insight mạnh, link Simulation-Engine
- §2 Fidelity (body phản ứng thật, cortisol > opioid) — unique, quantified
- §3 5 Modalities (visual/auditory/somatic/motor/emotional) — unique, link COMT/DRD4
- §5 Cortisol × 7 modes (IDLE→CRASH) — unique, cross-ref Cortisol-Baseline
- §6 3 cách dùng (Visualization/Worry/Daydream) — practical

**Phần CẦN ĐỔI MỚI:**
- [ ] §0 YAML + framing: "Process view of Simulation-Engine" — rõ ràng position
- [ ] §1 link Simulation-Engine: 2 giá trị = 2 use cases of the engine
- [ ] §3 5 Modalities × COMT/DRD4 hardware (PFC-Hardware.md)
- [ ] §4 Chunks = nguyên liệu → add Compiled/Fresh axis, Reward-Signal-Architecture
- [ ] §7 "L0 Alive" → signal strength language
- [ ] §8 AI era — quá sơ sài (~30L). Expand: AI × Simulation-Engine, AI as external chunk source, somatic check remains human-only, Ask-AI v3.1 dual check
- [ ] All cross-refs: outdated versions ("Core-v7.8-Draft.md", "Self-Pattern-Modeling.md v2.3")

### Phương án

**Đề xuất: Phương án A — Rewrite + reframe dưới Simulation-Engine**

Giữ Process focus. Cấu trúc mới dự kiến:
```
§0 — Position: Process view of Simulation-Engine
§1 — 2 Giá trị: nhanh hơn + mở access (reframe as engine use cases)
§2 — Simulation Fidelity (body phản ứng thật — keep + update)
§3 — 5 Modalities × Hardware (COMT/DRD4 link)
§4 — Chunks = nguyên liệu (+ Compiled/Fresh, RSA)
§5 — Cortisol × Modes (keep + update refs)
§6 — 3 Cách dùng (keep + update refs)
§7 — Sai + Override (signal strength language)
§8 — AI Era (EXPAND significantly)
§9 — Honest Assessment
§10 — Cross-References
```

### Mục tiêu v2.0
- Position rõ: Process view, KHÔNG trùng Engine (architecture) hay Imagine-Final (product)
- Simulation-Engine context tích hợp hữu cơ
- AI era substantive (~100-150L thay vì ~30L)
- All refs current

### ✅ DONE | 2026-05-24 | v1.0→v2.0 (~793L, was 610L)
- +§0 THESIS + POSITION + FOLDER MAP: entry point cho Imagination/ folder, architecture diagram
- §1 2 Giá Trị: reframe dưới Simulation-Engine, +Compiled/Fresh × chunks, +chunk association quality kept
- §2 Fidelity: +Cortisol = amplifier link, +Compiled/Fresh × fidelity (expert vs newbie)
- §3 5 Modalities: +COMT × specialist/improviser mapping, +DRD4 threshold, +COMT×DRD4 2-axis
- §4 Cortisol × 7 Modes: +Simulation-Engine disconnect (interoception blocked), +sweet spot insight
- §5 3 Cách Dùng: +Simulation-Engine application mapping, +Engine Use Quality cross-ref
- §6 Override: "L0 Alive"→body survival signals, +Dual Check (body + domain), +countermeasure expanded
- §7 AI Era EXPANDED (~30L→~70L): +AI×2 values, +chunks nền, +Dual Check×imagine, +AI amplify risk
- §8 Honest Assessment: +COMT/DRD4 entries, +Compiled/Fresh entry, +AI entries
- §9 Cross-Refs: COMPLETE REWRITE organized by folder, all versions current
- All outdated refs removed (Drive.md, Core-v7.8-Draft.md, old versions)
- v1.0→backup/Imagination-v1.0.md

---

## SESSION 5: Liking-Wanting.md → v2.0

### Tại sao ưu tiên 5
- Ổn nhất trong 6 file — bridge file mục đích rõ
- Cấu trúc tốt, chủ yếu enrichment

### Phân tích hiện trạng

**Phần VỮNG — giữ:**
- §0 Position + mục đích bridge — rõ ràng
- §1 Berridge recap — accurate
- §2 6 wanting mechanisms — cấu trúc tốt, well-argued
- §4 5 cases — case-based approach hay
- §5 Tại sao framework không dùng wanting/liking — solid argument

**Phần CẦN ENRICHMENT:**
- [ ] §3 Liking layers — **thiếu Reward-Signal-Architecture v2.0**:
  - Evaluative (opioid) vs Direct-State (non-opioid) distinction
  - Berridge "liking" ≈ Evaluative reward only
  - Direct-State = reward type mà Berridge CHƯA address (body-state change itself IS reward)
  - → Contribution LỚN NHẤT của rewrite
  - → Thêm §3.5 hoặc expand §3.4 với RSA framing
- [ ] Cross-refs version cũ (Imagine-Final, Self-Pattern-Modeling, Connection — all outdated)
- [ ] §5.1 cascade additions — tích hợp sâu hơn vào body text
- [ ] §4 cases — update references, có thể thêm 1 case minh họa Evaluative vs Direct-State

### Phương án

**Đề xuất: Update in-place + RSA enrichment**

Giữ cấu trúc. Thêm RSA layer. Update refs.

### Mục tiêu v2.0
- RSA Evaluative/Direct-State = highlight contribution
- Cases enriched
- Cross-refs chính xác
- Giữ bridge file purpose — reader Berridge → framework

### ✅ DONE | 2026-05-24 | v1.1→v2.0 (~1,205L, was ~1,037L)
- +§3.5 NEW Layer 5: Evaluative vs Direct-State Reward (RSA v2.0 integration)
  - Berridge "liking" = chỉ Evaluative (opioid hedonic hotspot)
  - Direct-State = non-opioid, hardware, burnout-proof (CT, eCB, thermo)
  - 5 lý do quan trọng: naltrexone gap, daily blend, burnout backdoor, E₀→E₃, H10 mapping
  - Evaluative Gates Direct-State mechanism cross-ref
- §3.6 summary table updated (5 layers thay vì 4)
- §2.1 +Simulation-Engine v1.0 reference (engine RUNS the preview)
- §2.3 +Entity-Compiled v1.0 (entity-level momentum, formation 40→200h)
- §4.1 Rat +RSA lens (sugar = E₀ Evaluative, naltrexone = Evaluative-only test)
- §4.3 TikTok +RSA lens (100% Evaluative, 0% Direct-State → WHY "empty")
- §4.5c Studying Children +RSA lens (+Path C: Direct-State environment support)
- §5 4→5 lý do: +LÝ DO 4 Evaluative/Direct-State dimension missing
- §5 table "THAY CHO LIKING" +2 entries (Evaluative/Direct-State + E₀→E₃)
- §5 table "THAY CHO WANTING" +1 entry (Entity-Compiled momentum)
- §6 Honest Assessment +RSA entries (🟢 CT, eCB, naltrexone; 🟡 orthogonal framing, E₀→E₃)
- §7.1 Reading Guide expanded (+RSA, +Simulation-Engine, +Entity-Compiled)
- §7.2 Cross-refs COMPLETE REWRITE: organized by folder, all paths fixed, all versions current
- YAML header: version bump, +RSA + Simulation-Engine + Entity-Compiled + Bond-Arch + Gap-Body-Need deps
- All inline refs updated: Imagine-Final→v3.0, VP→v3.0, Feeling→v3.0, Novelty→v1.2, Threat→v1.2, BFM→v2.0

---

## SESSION 6: Core-Software.md → v2.0

### Tại sao CUỐI CÙNG
Core-Software = BẢN ĐỒ tóm tắt toàn bộ framework. Bản đồ vẽ SAU khi khảo sát xong:
- Session 1: Domain.md v2.0 → §2 Domain reference chính xác
- Session 2: Emergent-Patterns decision → cross-refs rõ
- Session 3: Conflict-Dynamics v2.0 → §2 domain dynamics đúng
- Session 4: Imagination.md v2.0 → §4/§6 PFC reference đúng
- Session 5: Liking-Wanting v2.0 → §4.2 reward reference đúng
→ Core-Software **chỉ cần phản ánh**, không cần đoán.

### Phân tích hiện trạng

**OUTDATED NGHIÊM TRỌNG — đây là file lạc hậu nhất trong framework:**

Refs cũ khắp nơi:
- Self-Pattern-Modeling v2.3 → v3.1
- Empathy v2.0 → v4.0
- Connection v3.1 → v5.0
- Valence-Propagation v1.4 → v3.0
- Body-Base v3.1 → v3.2
- Collective-Body v1.1 → v2.1
- Body-Coupling v1.1 → v3.0

§4.4 vẫn dùng "Self-Pattern-Match" (đã rename).

**Thiếu HOÀN TOÀN concept lớn từ 28-session drill:**

| Concept | Source file | Impact on Core-Software |
|---------|-----------|------------------------|
| Hardware Subsidy | VP v3.0 | §4 Unconscious: body subsidize entity processing |
| 3 Satiation Types | Gap-Body-Need v1.0 | §4.2 Body-Feedback: satiation dynamics |
| Entity-Access Mức 0-5 | EA v1.2 | §4.4 Functions: gradient model |
| Entity-Compiled | EC v1.0 | §4.4 Functions: how entities compile into body |
| Bond-Architecture | BA v1.0 | §4.4 Functions: 4 bond types |
| Simulation-Engine | Simulation-Engine v1.0 | §6 PFC: 1 engine not N modules |
| PFC-Operations | PFC-Ops v1.0 | §6 PFC: Hold/Suppress, Budget, Compiled Quality |
| RSA Evaluative/Direct-State | RSA v2.0 | §4.2 Body-Feedback: reward types |
| M1-M4 Decline | BPGR v1.4 | §4.4 Functions: resonance dynamics |
| Compiled Quality | PFC-Ops v1.0 | §4 Unconscious: genuine/schema/threat |
| By-Product-Scale | BS v1.0 | §4.4 Functions: pair/hub/institutional |
| Resonance-Sustainability | RS v1.0 | §4.4 Functions: 4-layer sustainability |
| Phantom 4-factor | EVD v2.0 | §4.4 Functions: entity loss |
| Domain Types | Domain v2.0 (Session 1) | §2 Domain: Reality/Abstract/Abstract-Dynamic |

### Phương án

**Đề xuất: Phương án B — Restructure**

File hiện tại 13 sections, cấu trúc OK nhưng nội dung outdated quá sâu → update in-place sẽ patch everywhere. Restructure cho phép tích hợp concept mới hữu cơ.

Cấu trúc mới dự kiến (draft — finalize đầu session):
```
§0 — Ba Bản Đồ + Tại Sao Cycle-Based (giữ, update)
§1 — Kiến Trúc Cycle: Software Map (giữ diagram, update concepts)
§2 — Domain (update với Domain Types từ Session 1)
§3 — Body-Input L0 + L1 (giữ, minor update)
§4 — Unconscious Processing (MAJOR rewrite: chunks + body-feedback + cortisol + functions)
     → 4.1 Chunk-System: add Entity-Compiled, Compiled Quality
     → 4.2 Body-Feedback: add RSA, Satiation Types, H10 updated
     → 4.3 Cortisol: minor update
     → 4.4 Functions: MAJOR — Simulation-Engine, Entity-Access, Bond-Arch, HwS, M1-M4
§5 — Feeling Bridge (update Compiled/Fresh framing)
§6 — PFC (MAJOR: Simulation-Engine, PFC-Operations, Budget)
§7 — Body-Output (minor update)
§8 — Observation Parameters (MAJOR: update table, add new params, correct versions)
§9 — Development (update Compilable Architecture framing)
§10 — Multiple Timescales (minor)
§11 — Key Reframes (update with post-drill reframes)
§12 — Honest Assessment (update)
§13 — Cross-References (ALL new versions)
```

### Mục tiêu v2.0
- Đồng bộ 100% với state hiện tại (~130+ files, ~35,000+ lines)
- Cycle diagram phản ánh Simulation-Engine, Entity system, Compiled/Fresh
- Observation Parameters table đầy đủ + version đúng
- Cross-refs ALL chính xác
- Tích hợp Domain Types từ Session 1
- File này = SINGLE ENTRY POINT cho reader mới vào framework

---

## Workflow mỗi session

```
PHASE 1 — PHÂN TÍCH (đầu session, ~20% thời gian)
  ① Re-read file hiện tại (full)
  ② Re-read 2-3 file liên quan quan trọng nhất (headers + key sections)
  ③ List vấn đề cụ thể (line numbers nếu cần)
  ④ Xác nhận phương án triển khai với user

PHASE 2 — VIẾT MỚI (~70% thời gian)
  ① Draft v2.0 theo phương án đã chọn
  ② Đảm bảo concept mới tích hợp hữu cơ (KHÔNG bolted-on)
  ③ Cross-refs chính xác (version numbers, file paths)
  ④ Honest Assessment cập nhật

PHASE 3 — VERIFY (~10% thời gian)
  ① Check consistency
  ② Update File-Index entry
  ③ v1.x → backup/ nếu cần
  ④ Update memory
```

---

## Concepts phải tích hợp khi rewrite

Danh sách concept từ drill + cascade mà các file cũ THIẾU:

| Concept | Source | Cần ở file nào |
|---------|--------|----------------|
| Domain Types (Reality/Abstract/Abstract-Dynamic) | NEW | Domain, Core-SW |
| Dual Check (body=QC, domain=arbiter) | Ask-AI v3.1 | Domain |
| Hardware Subsidy (spectrum per entity) | VP v3.0 | Core-SW |
| 3 Satiation Types (Cyclic/Tonic/Generative) | GBN v1.0 | Domain, CD, Core-SW |
| Entity-Access gradient Mức 0-5 | EA v1.2 | CD, Core-SW |
| Entity-Compiled (hub-and-spoke) | EC v1.0 | Core-SW |
| Bond-Architecture (1 mech × 4 bonds) | BA v1.0 | EP, Core-SW |
| Simulation-Engine (1 engine, 3 comp, 3 axes) | Simulation-Engine v1.0 | Imag, CD, Core-SW |
| PFC-Operations (Compiled/Fresh, Hold/Suppress) | PFC-Ops v1.0 | Imag, Core-SW |
| RSA (Evaluative/Direct-State) | RSA v2.0 | LW, Core-SW |
| M1-M4 Resonance Decline | BPGR v1.4 | EP, Core-SW |
| Compiled Quality (genuine/schema/threat) | PFC-Ops v1.0 | Core-SW |
| By-Product-Scale (Pair/Hub/Institutional) | BS v1.0 | EP, Core-SW |
| Resonance-Sustainability (4-Layer) | RS v1.0 | EP, Core-SW |
| Phantom 4-factor model | EVD v2.0 | Core-SW |
| Self-Pattern-Modeling v3.1 (Match→Modeling) | SPM v3.1 | ALL |

---

## Risk + mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Core-Software cuối → reader đọc file cũ trong 5 sessions | Thấp — file đã outdated rồi, không tệ hơn | Nếu cần: thêm note "v2.0 coming" ở đầu file |
| 1 session không đủ cho 1 file (đặc biệt Core-Software) | Trung bình | Split thành 2 sessions nếu cần. Core-SW có thể cần 1.5-2 sessions |
| Emergent-Patterns quyết định thu gọn → mất content | Thấp | Content đã superseded bởi file chuyên sâu. v1.2 → backup/ |
| Domain types mới → cần update nhiều file khác ngoài plan | Trung bình | Chỉ cần update cross-ref nhẹ ở file đã qua cascade. Không cần rewrite |

---

## Tracking

| Session | File | Type | Status | Date | Notes |
|---------|------|------|--------|------|-------|
| 0 | Collective.md | NEW | ✅ DONE | 2026-05-24 | ~813L. Integration hub. 5 con đường. |
| 1 | Domain.md | REWRITE | ✅ DONE | 2026-05-24 | v1.0→v2.0 (~712L). +3 Types, +Dual Check, +Gap/CF/Sat/Simulation-Engine/EA |
| 2 | Drill-Emergent-Pattern.md | REWRITE | ✅ DONE | 2026-05-24 | v1.2→v2.0 (~675L). THU GỌN ~48%. +Enemy/Nurturing/Violation kept. +3 superseded→cross-ref |
| 3 | Conflict-Dynamics.md | REWRITE | ✅ DONE | 2026-05-24 | v1.1→v2.0 (~621L). +§4.1 Domain Types×conflict. "Empathy-Mirror"→Self-Pattern-Modeling |
| 4 | Imagination.md | REWRITE | ✅ DONE | 2026-05-24 | v1.0→v2.0 (~793L). +COMT/DRD4, +AI era, +Dual Check, +Simulation-Engine |
| 5 | Liking-Wanting.md | REWRITE | ✅ DONE | 2026-05-24 | v1.1→v2.0 (~1,205L). +RSA Evaluative/Direct-State, +Simulation-Engine, +EC |
| 6 | Core-Software.md | REWRITE | ✅ DONE | 2026-05-24 | v1.0→v2.0 (~1,732L). FULL REWRITE. +14 concepts (Simulation-Engine, EC, EA, BA, HwS, 3 Sat, PFC-Ops, CQ, M1-M4, BS, RS, Phantom, Domain Types, Eval/DS). +16 version updates. +10 post-drill reframes (20 total). §13 organized by folder. |

---

> *"Foundation files = cửa ngõ vào framework.
> Sau 28+ session drill, cửa ngõ đã cũ kỹ trong khi bên trong đã renovate xong.
> Giờ là lúc xây lại cửa ngõ — từ Domain (nền), qua từng file, tới Core-Software (bản đồ) cuối cùng.
> Chậm mà chắc. Mỗi file = 1 session. Chất lượng cao nhất."*
