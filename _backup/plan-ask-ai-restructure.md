# Plan: Ask-AI Restructure — Mechanism Analysis + Operational Protocol

> **Ngày tạo:** 2026-05-11
> **Trạng thái:** Phase 0 ✅ + Phase 1 ✅ + Phase 2 ✅ + Phase 3 ✅ — ALL COMPLETE
> **Trigger:** Session phân tích "ví von" (analogy) mechanism → phát hiện:
>   ① Ask-AI folder cũ (3 files) dùng architecture "LENS per audience" → tạo bias
>   ② "Ví von" là mechanism quan trọng chưa formalize trong framework
>   ③ Knowledge transfer giữa different chunk networks = topic lớn hơn "ví von"
>   ④ Cần tách: mechanism analysis (framework) + operational protocol (application)
> **Nguyên tắc:** Chậm mà chắc. Chất lượng cao nhất. Mỗi session 1 file.

---

## §0 — TẠI SAO CẦN RESTRUCTURE

### §0.1 Vấn đề với architecture cũ

Ask-AI/ folder hiện tại có 3 files:
- Ask-AI.md (phổ thông) — 228L
- Ask-AI-Parent.md (phụ huynh) — translation layer riêng
- Ask-AI-Guide.md (hướng dẫn tạo thêm Ask-AI mới)

Architecture "LENS per audience" (Ask-AI-Guide.md §1):
```
Cùng DATA → KHÁC LENS → KHÁC output
Ask-AI.md (phổ thông) / Ask-AI-Parent.md (phụ huynh) / Ask-AI-Leader.md (quản lý)
```

**VẤN ĐỀ TỪ FRAMEWORK PERSPECTIVE:**

① Mỗi LENS = pre-install gap direction vào AI:
  → Ask-AI-Parent.md bias AI hướng "mọi thứ liên quan con cái"
  → Parent hỏi "tôi stress quá" → AI trả lời bias về stress nuôi con
  → Nhưng thực tế stress có thể do công việc, relationship, sức khỏe
  → = F3 External Install CHÍNH LENS vào AI → AI bị constrain

② Người thật KHÔNG fit gọn vào 1 category:
  → Parent cũng là employee, cũng là individual, cũng là friend
  → Pre-configured lens = giả định 1 identity duy nhất
  → Framework nói: mỗi người = chunk landscape UNIQUE, không thể categorize

③ Framework hiện tại ĐÃ ĐỦ ĐẦY ĐỦ tham số:
  → 14+ observation parameters, 3 Core maps, ~60 mechanism files
  → AI CÓ THỂ detect chunk landscape người hỏi VÀ adapt dynamically
  → KHÔNG CẦN pre-configured lens — cần PROTOCOL detect + adapt

→ GIẢI PHÁP: 1 file Ask-AI.md KHÔNG có domain bias + AI tự detect/adapt.

### §0.2 Vấn đề chưa formalize: Knowledge Transfer Mechanism

00-External-Mechanism.md cover 5 mechanism CƠ BẢN cho F3 External Install:
  ① Co-attention, ② Imitation, ③ Social referencing,
  ④ Label installation, ⑤ Cultural transmission

CHƯA COVER:
  ❌ HOW to optimize transfer khi sender và receiver có KHÁC chunk landscapes
  ❌ Analogy ("ví von") mechanism — tại sao hoạt động + tại sao nguy hiểm
  ❌ Gap Direction implications cho communication strategy
  ❌ Mini-gap chain theory — optimal sequencing for knowledge installation
  ❌ Audience chunk detection — WHY necessary + WHAT to detect
  ❌ Alternative to analogy: experience-based language (Core-Interface model)
  ❌ 2-force tension: [match user chunks] vs [present real mechanism]

→ CẦN FILE MỚI: phân tích mechanism truyền đạt giữa different chunk networks.

### §0.3 Hai files target

| # | Tên file | Vai trò | Góc nhìn | Đối tượng |
|---|---|---|---|---|
| 1 | 02-Cross-Network-Transfer.md | FRAMEWORK ANALYSIS | Mechanism | Bất kỳ ai cần hiểu cơ chế truyền đạt |
| 2 | Ask-AI.md | APPLICATION | Operational | AI trực tiếp khi tương tác với user |

Pattern giống: Schema.md (mechanism) ↔ AI-Schema-Detection.md (application)

### §0.4 Tại sao 2 files, không phải 1

| Tiêu chí | 1 file gộp | 2 files tách |
|---|---|---|
| Pattern framework | ❌ Trộn mechanism + instruction | ✅ Schema.md ↔ AI-Schema-Detection.md |
| Reusability | ❌ Chôn mechanism trong AI instruction | ✅ Education, therapy, communication reference |
| Ask-AI size | ❌ Quá dài | ✅ Gọn, focused |
| Depth analysis | ❌ Ép gọn, mất chất lượng | ✅ Phân tích đủ sâu |
| Audience | ❌ AI-only | ✅ Mechanism = researcher; Protocol = AI |

---

## §1 — TRẠNG THÁI HIỆN TẠI

### §1.1 Ask-AI/ folder (sẽ backup)

```
Ask-AI/Ask-AI.md        — 228L — wrapper cho phổ thông
Ask-AI/Ask-AI-Parent.md — ~120L — wrapper riêng phụ huynh
Ask-AI/Ask-AI-Guide.md  — ~80L  — guide tạo thêm wrapper

ĐÁNH GIÁ:
  ✅ Ngôn ngữ đời thường, warm, thực tế
  ✅ Ví dụ tốt (lười, buồn, con cãi)
  ✅ Hỏi ngược khi thiếu info
  ✅ Phong cách không phán xét

  ❌ Architecture "LENS per audience" → bias
  ❌ Không detect chunk landscape người hỏi
  ❌ Không có theory về analogy, mini-gap, pacing
  ❌ Bảng thuật ngữ cứng → thiếu linh hoạt
  ❌ Reference files cũ (Research/ folder, Core-v7-UD.md)
  ❌ Không tích hợp v7.8 (Core 3-Maps, chunk dynamics, Gap Direction)

→ Giữ TINH THẦN (warm, thực tế, hỏi ngược, không phán xét)
→ Thay architecture + nâng cấp mechanism-based protocol
```

### §1.2 Files liên quan trong framework (đã đọc session này)

| File | Vai trò | Liên quan thế nào |
|---|---|---|
| Gap-Direction.md | "Chưa biết = không gap" + 4 properties + External Install | CỐT LÕI cho tại sao "nói ≠ hiểu" |
| 01b-Chunk-Activation-Dynamics.md | Competitive re-linking | Shift cost khi đổi analogy |
| 00-External-Mechanism.md | 5 F3 mechanisms + Education = batch install | Foundation, file mới EXTENDS |
| 01c-Chunk-Discovery-Lifecycle.md | Macro lifecycle accumulate → label → plan | Model cho conversation flow |
| Core-Interface.md v1.0 | Experience-based language model | ALTERNATIVE to analogy |
| Feeling-Literacy-Training.md | 5-stage training, natural discovery 3 conditions | Model cho progressive learning |
| SAL §5 | AI as articulation catalyst | AI role + guardrails |
| AI-Schema-Detection.md §7-§8 | Self-drill + AI Trust Guardrails | Guardrails cho Ask-AI |
| Core-Software.md | Mechanism source of truth | What Ask-AI translates |
| Logic-Feeling-Balance.md | Meta-principle: neither 100% accurate | Closing principle |

---

## §2 — KẾ HOẠCH THỰC THI

### §2.1 Thứ tự và lý do

```
Phase 0: Backup                           ← Move Ask-AI/ → Ask-AI/_backup/
Phase 1: 02-Cross-Network-Transfer.md     ← MECHANISM ANALYSIS (novel nhất)
Phase 2: Ask-AI.md                        ← APPLICATION (reference Phase 1)
Phase 3: Cross-reference updates          ← 01-File-Index, metadata
```

**Tại sao thứ tự này:**
- Phase 1 = mechanism TRƯỚC → Phase 2 reference mechanism = chính xác hơn
- Giống plan-core-3maps: Software (mechanism) trước → Interface (application) sau
- Phase 1 = nặng nhất, novel nhất, cần attention cao nhất
- Phase 2 = dựa trên Phase 1 + tinh thần file cũ, nhẹ hơn

### §2.2 Mỗi session 1 file

- Session A: Triển khai 02-Cross-Network-Transfer.md (nặng nhất, mechanism synthesis)
- Session B: Triển khai Ask-AI.md (application, reference Phase 1)
- Session C: Cross-reference updates (nhẹ, scan framework)

---

## §3 — PHASE 0: BACKUP

### Actions:
- [x] Create folder Ask-AI/_backup/ (nếu chưa có) ✅ 2026-05-11
- [x] Copy Ask-AI.md → Ask-AI/_backup/Ask-AI-v1.md ✅ 2026-05-11
- [x] Copy Ask-AI-Parent.md → Ask-AI/_backup/Ask-AI-Parent-v1.md ✅ 2026-05-11
- [x] Copy Ask-AI-Guide.md → Ask-AI/_backup/Ask-AI-Guide-v1.md ✅ 2026-05-11

→ Giữ nguyên nội dung — pure backup, reference khi cần.

---

## §4 — PHASE 1: 02-Cross-Network-Transfer.md

### §4.1 Mục tiêu

Phân tích mechanism: HOW knowledge transfers between minds with DIFFERENT chunk landscapes.
Includes: analogy mechanism, risks, alternatives, mini-gap theory, audience detection.
Ngôn ngữ: mechanism + framework synthesis (như các file Core-Deep-Dive khác).
Đối tượng: researcher, educator, therapist, anyone studying knowledge transfer.

### §4.2 Vị trí trong framework

```
Core-Deep-Dive/Body-Base/Chunk/Chunk-External-Development/
  00-External-Mechanism.md — WHAT mechanisms exist (5 basic)
  01-External-Synthesis.md — Verdicts + output contracts
  02-Cross-Network-Transfer.md — HOW to OPTIMIZE transfer (file MỚI)

RELATIONSHIP:
  00 cover: CO-ATTENTION + IMITATION + SOCIAL REF + LABEL INSTALL + CULTURAL
  02 cover: WHEN sender ≠ receiver chunk landscape → optimization strategy
  00 = FOUNDATION mechanisms
  02 = STRATEGY layer sử dụng foundation mechanisms

  00 §7 "Education = Batch Direction B" → 02 EXTENDS: HOW to make Direction B effective
  00 §5 "Abstract + External Labels" → 02 EXTENDS: analogy = special case
```

### §4.3 Nguồn nội dung — cái gì MỚI, cái gì TỔNG HỢP

```
NỘI DUNG MỚI (phân tích + formalize):
  ★ Analogy ("ví von") at chunk level — cross-domain mapping mechanism
  ★ 3 risks: direction mismatch, shift cost, false specificity
  ★ When analogy works vs fails — structural similarity criterion
  ★ Double unknown problem (người nghe chưa biết cả analogy domain)
  ★ Mini-gap chain theory — optimal sequencing for knowledge installation
  ★ 2-force tension: [match user chunks] vs [present real mechanism]
  ★ Audience chunk detection protocol
  ★ Experience-based language as ALTERNATIVE to analogy

TỔNG HỢP/CONNECT (từ existing files, KHÔNG copy — rethink trong context mới):
  → Gap-Direction §3: "chưa biết = không gap" applied to communication
  → Gap-Direction §4: 4 properties → 4 properties of ANALOGY evaluation
  → Gap-Direction §7.5: oscillation dynamics → mini-gap chain
  → Gap-Direction §8: external install → gap install via presentation
  → 01b §3: competitive re-linking → shift cost mechanism
  → Core-Interface model: experience-based language → alternative strategy
  → 00-External-Mechanism §7: Education = batch Direction B → extension
  → FLT §3: 5-stage training → model for progressive knowledge building
  → SAL §5: AI as catalyst → AI role in knowledge transfer
```

### §4.4 Cấu trúc dự kiến 02-Cross-Network-Transfer.md

```
Metadata (status, date, dependencies, scope, purpose)

§0  — TẠI SAO CẦN FILE NÀY (~40L)
      §0.1 — 00-External-Mechanism cover WHAT, file này cover HOW TO OPTIMIZE
      §0.2 — Gap: no file addresses communication across different chunk landscapes
      §0.3 — File này bổ sung gì

§1  — VẤN ĐỀ CỐT LÕI: "NÓI" ≠ "NGƯỜI NGHE HIỂU" (~80L)
      §1.1 — "Chưa biết = không có gap" applied to communication
             → Sender nói X → nhưng receiver không có chunks about X
             → Không có bờ → không có hole → không có gap → KHÔNG TIẾP NHẬN
      §1.2 — Tại sao chuyên gia cũng không tải nổi cross-domain dumps
             → VD: chuyên gia toán, dump hormone list → zero gap → zero reward
             → Chunks DOMAIN-SPECIFIC: math ≠ neuroscience ≠ psychology
      §1.3 — Hệ quả cho mọi communication: phải DETECT trước, BUILD chunks trước
      §1.4 — Connection tới existing framework: 
             → Gap-Direction §3 + §8, Education batch install (00 §7)

§2  — ANALOGY ("VÍ VON") MECHANISM (~120L)
      §2.1 — Analogy LÀ GÌ ở tầng chunk
             → Cross-domain chunk mapping: borrow chunks Domain A → scaffold Domain B
             → F3 install sử dụng BORROWED chunks làm bờ tạm
             → Gap direction hình thành từ Domain A, HƯỚNG VỀ Domain A
      §2.2 — TẠI SAO analogy hoạt động (khi nó hoạt động)
             → Bypass "chưa biết = không gap" bằng surrogate chunks
             → Người nghe ĐÃ CÓ chunks Domain A → bờ tạm → gap direction → "hiểu"
             → VD: "chunk network ≈ graph data structure" cho engineer
      §2.3 — CƠ CHẾ neural: activation pattern Domain A fire 
             → partial overlap với Domain B structure → "thấy tương tự"
      §2.4 — Analogy quality = f(structural_similarity × receiver_domain_A_depth)
             → Structural similarity CAO = analogy TỐT
             → Receiver biết Domain A SÂU = analogy EFFECTIVE hơn

§3  — 3 RISKS CỦA ANALOGY (~150L)
      §3.1 — RISK 1: Gap Direction Mismatch
             → Bờ tạm từ Domain A → gap direction HƯỚNG VỀ Domain A
             → Domain B thật có structure KHÁC → direction SAI
             → VD: "PFC = mẹ" → installs [PFC kiểm soát, yêu thương, biết tốt nhất]
                   PFC thật: reach limited, ~5% capacity, KHÔNG biết tốt nhất
             → Hệ quả: khi gặp mechanism thật → Chunk-Shift → dissonance
             → Formal: Gap_Direction_analogy ≠ Gap_Direction_real 
                       → mismatch cost khi upgrading

      §3.2 — RISK 2: Shift Cost (Competitive Re-linking)
             → PFC=mẹ → PFC=giám đốc: KHÔNG phải đổi label
             → Chunks xung quanh "mẹ" = [yêu thương, hy sinh, quyền tình cảm,...]
             → Chunks xung quanh "giám đốc" = [chiến lược, tổ chức, quyền chức vụ,...]
             → = 2 tệp chunks HOÀN TOÀN KHÁC → competitive re-linking (01b §3)
             → Mỗi shift = energy cost. Nhiều shifts = accumulated cost.
             → ⭐ KEY INSIGHT: Shift từ analogy → real CÓ THỂ KHÓ HƠN 
               so với học real từ đầu (phải đồng thời: phá cũ + xây mới + lọc đúng/sai)

      §3.3 — RISK 3: False Specificity
             → Analogy cung cấp Specificity từ Domain A (Gap-Direction §4.2)
             → Constraints này CÓ THỂ SAI cho Domain B
             → VD: "PFC = giám đốc" → installs constraint [ra lệnh → nghe]
                   PFC thật: vô thức KHÔNG nghe lệnh PFC (Core-Interface §4)
             → = Constraints sai → khi gặp thật → dissonance > cần thiết
             → Formal: Specificity_analogy installs WRONG constraints

      §3.4 — RISK 4: Double Unknown
             → Analogy chỉ work khi receiver CÓ chunks Domain A
             → Nếu receiver CŨNG chưa biết Domain A → 2 thứ mới cùng lúc
             → VD: "PFC = giám đốc" cho trẻ chưa biết giám đốc làm gì
             → = Body phải hình dung CẢ Domain A LẪN Domain B = overload
             → 01b §2: WM capacity ~3-5 items → 2 unknowns = near capacity

§4  — KHI NÀO ANALOGY NÊN DÙNG vs KHÔNG (~80L)
      §4.1 — CRITERIA: structural similarity
             → Dùng khi Domain A và Domain B share CẤU TRÚC (không chỉ surface)
             → "Chunk network ≈ graph" ✅ (nodes, edges, traversal = genuinely similar)
             → "PFC ≈ giám đốc" ⚠️ (surface similar, structure khác significantly)
      §4.2 — CRITERIA: endpoint vs stepping stone
             → Analogy là điểm CUỐI (người nghe không cần đi sâu hơn) → OK
             → Analogy là bước ĐỆM (sẽ cần upgrade) → DANGEROUS (shift cost)
      §4.3 — CRITERIA: marked approximate vs identity
             → "giống như... nhưng khác ở chỗ..." → safer (mark rõ ranh giới)
             → "PFC LÀ giám đốc" → dangerous (presented as identity)
      §4.4 — CRITERIA: receiver có Domain A hay không
             → Có → analogy works
             → Không → double unknown → harmful

§5  — ALTERNATIVE: EXPERIENCE-BASED LANGUAGE (~100L)
      §5.1 — Core-Interface.md model
             → File này translate TOÀN BỘ mechanism → ngôn ngữ TRẢI NGHIỆM
             → KHÔNG analogy, KHÔNG jargon → dùng chunks MỌI NGƯỜI ĐÃ CÓ
             → VD: "Bạn không quyết định nhịp tim, không chọn lúc nào đói"
                   = chunks observation-level (ai cũng có) → gap direction ĐÚNG
      §5.2 — Tại sao experience-based language tốt hơn analogy
             → Dùng chunks CHÍNH receiver → bờ THẬT (không borrowed)
             → Gap direction hướng ĐÚNG về mechanism thật
             → KHÔNG tạo false association → KHÔNG cần shift cost sau
             → Formal: Gap_Direction_experience ≈ Gap_Direction_real
      §5.3 — Limitation: experience-based language chậm hơn
             → Analogy "shortcut" → fast but risky
             → Experience-based = accurate but requires more building
             → Tradeoff: speed vs accuracy (context-dependent choice)
      §5.4 — So sánh 3 approaches (table):
             → Jargon: fast but "chưa biết = không gap" → fail
             → Analogy: medium, partial understanding, shift cost
             → Experience-based: slow, accurate, no shift cost

§6  — MINI-GAP CHAIN THEORY (~100L)
      §6.1 — Principle: mỗi đoạn = fill 1 gap NHỎ → tạo curiosity cho gap TIẾP
             → Gap-Direction §7.5 oscillation: fill₁ → reward₁ + new gap₂
             → Applied to presentation: each paragraph = 1 mini-arc
      §6.2 — Design: gap direction của mỗi đoạn phải ĐÚNG HƯỚNG
             → Mỗi fill → new chunks compile → new bờ → new gap
             → New gap phải point TOWARD real mechanism (not away)
      §6.3 — Pacing: vừa đủ → reward → curiosity → continue
             → Quá nhiều 1 lúc → overwhelm (WM capacity 3-5, 01b §2)
             → Quá ít → "mất hứng" (gap direction fade)
             → Goldilocks: enough for reward, enough for new gap
      §6.4 — Entry point: BẮT ĐẦU từ observation receiver ĐÃ CÓ
             → "chưa biết = không gap" → phải start from EXISTING chunks
             → Người thường: start từ observation hành vi hàng ngày
             → Expert: start từ domain-specific observation
      §6.5 — Progression: observation → pattern → mechanism (nếu muốn sâu hơn)
             → FLT §3: 5-stage = model cho progressive building
             → Mỗi stage = deeper chunks → richer gap landscape
      §6.6 — Conversation as Chunk Discovery Lifecycle (01c)
             → Mỗi lượt hỏi-đáp = 1 cycle: accumulate → vague → clarify → label
             → Conversation ITSELF là mechanism mà file này describe
      §6.7 — VD: chain cho "tại sao tôi lười?" 
             → (minh họa mini-gap chain implementation cụ thể)

§7  — AUDIENCE CHUNK DETECTION (~80L)
      §7.1 — TẠI SAO phải detect trước khi trình bày
             → Different chunk landscapes → different gap directions → 
               SAME content phải present KHÁC NHAU
             → Gap-Direction §3.3 table: học sinh vs sinh viên vs Einstein 
               nhận CÙNG E=mc² → KHÁC reward hoàn toàn
      §7.2 — DETECT CÁI GÌ
             → Profession → domain chunks estimate
             → Vocabulary used → label depth estimate (surface label vs deep chunk)
             → Questions asked → gap direction reveal
             → Emotional context → body-state affect presentation pacing
      §7.3 — 3 BROAD PROFILES (không phải category cứng — spectrum)
             → Profile A: Observation-dominant (người bình thường)
               Chunks: hành vi hàng ngày, trải nghiệm cá nhân
               Strategy: Core-Interface language, mini-gap chain, rare analogy
             → Profile B: Domain-expert (tâm lý học, giáo viên, bác sĩ)
               Chunks: behavioral chains OK, some mechanism, domain terminology
               Strategy: trực tiếp hơn, cẩn thận schema conflict
             → Profile C: Technical-expert (engineer, toán, khoa học)
               Chunks: formal structure, logic, nhưng low psychology/neuroscience
               Strategy: structural analogy CÓ THỂ, build psychology bottom-up
      §7.4 — KHÔNG FIX profile → update liên tục qua conversation
             → Người hỏi reveal chunks dần → AI adjust strategy
             → = Dynamic chunk landscape mapping (không static category)

§8  — 2-FORCE TENSION VÀ GIẢI PHÁP (~60L)
      §8.1 — Force 1: Match user chunks (comprehension + reward)
      §8.2 — Force 2: Present accurately (real understanding)
      §8.3 — Connection tới 2-Layer Model (Gap-Direction §6):
             → Layer 1 (Signal): phải trigger interest → cần recognizable
             → Layer 2 (Direction): gap phải hướng ĐÚNG về mechanism
      §8.4 — Resolution: mini-gap chain BẮT ĐẦU từ Force 1, DẪN DẮT tới Force 2
             → Start: match existing chunks (signal fires, interest triggered)
             → Progress: each fill → new chunks → gap shifts toward real mechanism
             → End: real understanding (or as deep as receiver wants to go)
      §8.5 — Khi 2 forces CONFLICT irreconcilable
             → Quá xa: receiver chunks ≪ required for mechanism
             → Solution: accept partial understanding, invite deeper exploration
             → "Muốn biết thêm không?" = respect body-base pacing

§9  — HONEST ASSESSMENT (~40L)
      §9.1 — File này PROVIDE
      §9.2 — File này KHÔNG PROVIDE
      §9.3 — OPEN QUESTIONS (research cần thêm)

§10 — CROSS-REFERENCES (~30L)
      → 00-External-Mechanism.md (foundation — 5 mechanisms)
      → Gap-Direction.md ("chưa biết = không gap", 4 properties, external install)
      → 01b-Chunk-Activation-Dynamics.md (competitive re-linking)
      → 01c-Chunk-Discovery-Lifecycle.md (macro lifecycle model)
      → Core-Interface.md (experience-based language model)
      → FLT (progressive building model)
      → SAL §5 (AI as catalyst)
      → AI-Schema-Detection.md §7-§8 (guardrails)
      → Ask-AI.md (application file — Phase 2)
```

**Ước lượng:** ~800-1000 dòng → **THỰC TẾ: 1,435 dòng** (deeper analysis than estimated)
**STATUS:** ✅ COMPLETE — 2026-05-11

### §4.5 Files cần đọc trước khi triển khai Phase 1

```
ĐÃ ĐỌC SESSION NÀY (refresh overview trước khi viết):
  [x] Gap-Direction.md §0-§9 — core dependency
  [x] 01b-Chunk-Activation-Dynamics.md §1-§2 — competitive re-linking
  [x] 00-External-Mechanism.md §1-§8 — foundation
  [x] Core-Interface.md §0 — model language
  [x] Ask-AI.md (cũ) — tinh thần + ví dụ
  [x] 01c-Chunk-Discovery-Lifecycle.md §1 — macro lifecycle

CẦN ĐỌC THÊM KHI TRIỂN KHAI:
  [ ] 01b §3 — competitive re-linking DETAIL (shift cost mechanism)
  [ ] Gap-Direction §11 — examples (có thể reuse/reference)
  [ ] 01c §2-§3 — convergence zone + label prerequisite (cho §6)
  [ ] FLT §3 — 5-stage training DETAIL (cho §6.5 progression model)
  [ ] SAL §5 — AI era DETAIL (cho §8 AI role)
  [ ] Core-Interface.md §1-§6 — experience-based language DETAIL examples
  [ ] Background-Pattern.md §10 — BP constraint gap landscape (cho §7)
```

### §4.6 Quality checklist Phase 1 — ✅ ALL PASSED 2026-05-11

- [x] Mọi claim grounded trong existing framework (không speculation) ✅
- [x] 4 analogy risks formally grounded (gap direction, re-linking, specificity, double unknown) ✅
- [x] Core-Interface model properly referenced as alternative ✅
- [x] Mini-gap chain theory connects to oscillation dynamics (§7.5) ✅
- [x] Audience profiles framework-grounded (không marketing personas) ✅
- [x] 2-force tension resolved via framework mechanism (không hand-waving) ✅
- [x] Mọi neuroscience claims tagged (🟢/🟡/🔴) ✅
- [x] Cross-references complete ✅
- [x] "Ví von" (analogy) trong file KHÔNG dùng để giải thích mechanism ✅
  → Meta-consistency: file phân tích risks of analogy PHẢI tự mình avoid analogy risks
- [x] Ví dụ DIVERSE: education, therapy, AI, daily communication, cross-cultural ✅

---

## §5 — PHASE 2: Ask-AI.md

### §5.1 Mục tiêu

Operational protocol: INSTRUCTION FILE cho AI khi tương tác với end users.
1 file duy nhất, KHÔNG domain-specific bias.
AI tự detect chunk landscape + adapt strategy + present via mini-gap chain.
References 02-Cross-Network-Transfer.md cho mechanism understanding.
Ngôn ngữ: instruction + examples.
Đối tượng: AI (Claude/GPT/etc.) khi được user load framework + Ask-AI.

### §5.2 Design principles

```
① 1 FILE, NO BIAS:
   → KHÔNG có lens pre-configured (không parent, không leader, không expert)
   → AI detect chunk landscape người hỏi VÀ adapt dynamically
   → = Framework principle: mỗi người unique, detect > categorize

② PROTOCOL, NOT RULES:
   → DETECT → ADAPT → PRESENT → ITERATE → DEEPEN
   → Flexible: protocol adapt theo conversation, không rigid rules

③ REFERENCE MECHANISM:
   → Ask-AI.md KHÔNG chứa mechanism analysis
   → Reference 02-Cross-Network-Transfer.md khi cần WHY
   → Keeps file focused + concise

④ GIỮ TINH THẦN CŨ:
   → Warm, thực tế, không phán xét
   → Hỏi ngược khi thiếu info
   → "Công cụ NAVIGATE, không phải GPS chính xác"
   → Upgrade: mechanism-based thay vì rule-based

⑤ TÍCH HỢP v7.8:
   → Reference Core 3-Maps (Software/Hardware/Interface)
   → Reference Core-Deep-Dive/ files (không Research/ folder cũ)
   → Tích hợp observation parameters (14+ tham số)
```

### §5.3 Cấu trúc dự kiến Ask-AI.md

```
Metadata (version, date, scope)
Instruction header: "Kéo file này + toàn bộ folder Human-Predictive-Drive/ vào AI"

§0  — VAI TRÒ + PHẠM VI (~30L)
      AI = giúp người dùng HIỂU BẢN THÂN + HIỂU NGƯỜI KHÁC
      KHÔNG chẩn đoán. KHÔNG thay thế chuyên gia.
      = Compass, không phải GPS.

§1  — NGUYÊN TẮC CỐT LÕI (~40L)
      §1.1 — "Chưa biết = không gap" → phải detect trước, build trước
      §1.2 — Mini-gap chain: mỗi câu trả lời = fill 1 gap + mở 1 gap mới
      §1.3 — Experience-based language > analogy > jargon
      §1.4 — Body-base pacing: người đọc cần reward mỗi đoạn
      (Reference: 02-Cross-Network-Transfer.md cho mechanism chi tiết)

§2  — PROTOCOL: DETECT → ADAPT → PRESENT → ITERATE (~80L)
      §2.1 — DETECT: Câu hỏi đầu tiên
             → Hỏi nghề nghiệp, context, mong muốn
             → Qua câu hỏi của họ → hình dung chunk landscape
             → Vocabulary họ dùng → depth estimate
      §2.2 — ADAPT: Chọn strategy
             → Observation-dominant → Core-Interface language
             → Domain-expert → direct chains, cẩn thận schema conflict
             → Technical → structural models, build psychology bottom-up
      §2.3 — PRESENT: Trình bày
             → Bắt đầu từ observation THEY ALREADY HAVE
             → Mini-gap chain: mỗi đoạn fill 1 gap + curiosity cho gap tiếp
             → Ngôn ngữ: experience-based, KHÔNG jargon, analogy CẨN THẬN
      §2.4 — ITERATE: Hỏi lại
             → "Muốn biết thêm về phần nào?"
             → Update chunk landscape estimate qua câu trả lời
             → Adjust strategy nếu cần
      §2.5 — DEEPEN: Drill sâu dần (nếu user muốn)
             → observation → pattern → mechanism (nếu họ hỏi WHY)
             → Có thể dẫn tới Core-Software hoặc Core-Interface

§3  — NGÔN NGỮ + PHONG CÁCH (~50L)
      §3.1 — Ngôn ngữ experience-based (KHÔNG bảng thuật ngữ cứng)
             → Thay vì bảng "Dopamine → hứng thú": 
               dùng ngôn ngữ TRONG CONTEXT, adapt theo người hỏi
             → VD profile A: "hứng thú" → profile B: "dopamine-driven novelty signal"
      §3.2 — Phong cách warm + thực tế (giữ từ file cũ)
      §3.3 — Hỏi ngược khi thiếu info (giữ từ file cũ, upgrade protocol)
      §3.4 — KHÔNG phán xét + KHÔNG prescriptive (giữ)
      §3.5 — Analogy protocol:
             → Dùng KHI structural similarity cao VÀ người nghe biết Domain A
             → LUÔN mark approximate: "giống... nhưng khác ở..."
             → KHÔNG dùng khi stepping stone (sẽ cần upgrade)

§4  — VÍ DỤ CONVERSATIONS (~100L)
      §4.1 — Ví dụ: Người bình thường hỏi "tại sao tôi lười?"
             (Upgrade từ file cũ — thêm mini-gap chain)
      §4.2 — Ví dụ: Chuyên gia tâm lý hỏi về mechanism
             (MỚI — demonstrate adapt strategy)
      §4.3 — Ví dụ: Kỹ sư hỏi "não hoạt động thế nào?"
             (MỚI — demonstrate structural model approach)
      §4.4 — Ví dụ: Phụ huynh hỏi "con tôi hay cãi lại"
             (Upgrade từ file cũ — giữ tinh thần, upgrade mechanism)

§5  — GIỚI HẠN + KHI NÀO KHUYÊN CHUYÊN GIA (~40L)
      §5.1 — Framework = công cụ HIỂU, không phải CHẨN ĐOÁN
      §5.2 — Sức khỏe tâm thần nghiêm trọng → khuyên chuyên gia
      §5.3 — AI output = hypothesis, body-check mandatory
             (reference AI-Schema-Detection §8 guardrails)
      §5.4 — Honest about framework limits

§6  — CROSS-REFERENCES (~20L)
      → Core-Interface.md (observer perspective — recommend đọc trước)
      → Core-Software.md (mechanism — cho người muốn sâu hơn)
      → Core-Hardware.md (neuroscience — cho chuyên gia)
      → 02-Cross-Network-Transfer.md (mechanism truyền đạt)
      → AI-Schema-Detection.md (self-drill mode)
```

**Ước lượng:** ~400-500 dòng → **THỰC TẾ: 714 dòng** (thêm ví dụ #5 + protocol chi tiết hơn)
**STATUS:** ✅ COMPLETE — 2026-05-11

### §5.4 Files cần đọc trước khi triển khai Phase 2

```
  [x] 02-Cross-Network-Transfer.md (vừa hoàn thành Phase 1) — source of truth ✅
  [x] Ask-AI/_backup/Ask-AI-v1.md — tinh thần + ví dụ giữ lại ✅
  [x] Ask-AI/_backup/Ask-AI-Parent-v1.md — ví dụ parent giữ lại ✅
  [x] Core-Interface.md §0-§1 — observer language reference ✅
  [x] AI-Schema-Detection.md §7-§8 — guardrails ✅
  [x] SAL §5 — AI catalyst patterns (đọc thêm) ✅
  [x] Ask-AI-Guide-v1.md — architecture cũ reference ✅
```

### §5.5 Quality checklist Phase 2 — ✅ ALL PASSED 2026-05-11

- [x] 1 file, KHÔNG domain-specific bias (không parent lens, không expert lens) ✅
- [x] Protocol DETECT → ADAPT rõ ràng, AI có thể follow ✅
- [x] Ngôn ngữ adapt theo context (không bảng thuật ngữ cứng) ✅
- [x] Ví dụ conversations demonstrate ≥3 audience types ✅ (5 examples: A, B, C, Parent, Emotional)
- [x] Giới hạn clearly stated (framework ≠ chẩn đoán) ✅
- [x] Consistent với AI-Schema-Detection guardrails ✅
- [x] Reference 02-Cross-Network-Transfer cho mechanism (không chứa mechanism) ✅
- [x] Tinh thần file cũ preserved (warm, thực tế, hỏi ngược, không phán xét) ✅
- [x] References updated tới v7.8 (Core 3-Maps, không Research/ cũ) ✅

---

## §6 — PHASE 3: CROSS-REFERENCE UPDATES

### §6.1 Files cần update — ✅ ALL DONE 2026-05-11

```
  [x] Core-Deep-Dive/01-File-Index.md — thêm 02-Cross-Network-Transfer.md entry ✅
  [x] AI-Schema-Detection.md §10 — thêm APPLICATION references (Ask-AI v2.0 + 02-CNT) ✅
  [x] 00-External-Mechanism.md — thêm reference tới 02 ở footer ✅
  [x] Core-Interface.md §7.2 — thêm Ask-AI.md v2.0 reference ✅
  [—] 01-External-Synthesis.md — SKIP (commitment file, reference không cần thiết)
```

### §6.2 Scope

Phase 3 = nhẹ. Chủ yếu thêm references, không rewrite. ✅ DONE.

---

## §7 — RỦI RO VÀ MITIGATION

| Rủi ro | Mức | Mitigation |
|---|---|---|
| 02 trở thành "lý thuyết truyền thông" chung chung | CAO | Grounded trong chunk mechanism cụ thể. Mọi claim → framework reference |
| 02 dùng analogy để giải thích risks of analogy | TRUNG BÌNH | Meta-consistency check: file PHẢI tự avoid analogy. §4.6 checklist item |
| Ask-AI quá dài/phức tạp cho AI follow | TRUNG BÌNH | Target ~400-500L. Protocol simple: DETECT → ADAPT → PRESENT → ITERATE |
| Ask-AI trở thành prescriptive | THẤP | Inherit Core-Interface principle: mô tả, không ra lệnh |
| Overlap với existing files | THẤP | 02 = strategy layer (mới). Ask-AI = application (mới). Clear scope |
| Cross-references outdated | THẤP | Phase 3 scan |

---

## §8 — TỔNG KẾT

```
HIỆN TẠI:
  Ask-AI/ folder (3 files) = "LENS per audience" architecture → bias
  Framework THIẾU: knowledge transfer mechanism analysis

MỤC TIÊU:
  02-Cross-Network-Transfer.md (~800-1000L) = MECHANISM (tại sao nói ≠ hiểu)
  Ask-AI.md (~400-500L)                     = APPLICATION (protocol cho AI)

THỨ TỰ:
  Phase 0: Backup Ask-AI/ cũ
  Phase 1: 02-Cross-Network-Transfer.md (nặng nhất, mechanism synthesis)
  Phase 2: Ask-AI.md (application, reference Phase 1)
  Phase 3: Cross-reference updates

MỖI SESSION 1 FILE. CHẬM MÀ CHẮC.
```
