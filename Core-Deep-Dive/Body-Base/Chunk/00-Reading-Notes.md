---
title: Reading Notes — Chunk Deep Analysis
created: 2026-04-14
session: Phase 1 (Discovery + Reading Pass)
status: Synthesis of files read, threads-to-coverage mapping, emergent hypotheses
scope: Foundation for plan.md (master) + Grammar-Scaffolding/plan.md (sub)
language: Tiếng Việt primary + English technical terms
---

# 00 — Reading Notes

> **Mục đích file này**: Consolidate findings từ Phase 1 reading pass. Làm nền cho `plan.md` (master plan) và `Grammar-Scaffolding/plan.md` (sub-plan).
>
> **KHÔNG phải analysis file**. KHÔNG commit kết luận. CHỈ map những gì đã có trong framework + những gì còn gap.
>
> **Bối cảnh session**: Sau Feeling Deep Analysis session (2026-04-14), user raised 6 threads mới + 5 directions từ session trước + 1 architectural shift hypothesis: **"Chunk có thể là substrate; Feeling là interface/view lên Chunk"**. File này là Phase 1 output của drill Chunk-Analysis.

---

## §1 — Scope của Phase 1 Reading

### §1.1 Files đọc trong Phase 1 này (session hiện tại)

| # | File | Location | Lines đọc | Mức độ |
|---|---|---|---|---|
| 1 | Chunk.md | `Schema/` | 429 (full) | Đọc toàn bộ |
| 2 | Chunk-Practical.md | `Schema/` | ~270 | Đọc toàn bộ |
| 3 | Chunk-Search-Advanced.md | `Schema/` | ~220 (full) | Đọc toàn bộ |
| 4 | Schema.md | `Schema/` | ~400 trên ? | Phần đầu |
| 5 | Object-Agent.md | `Domain/` | 581 (full) | Đọc toàn bộ |
| 6 | Connection.md | `Core-Deep-Dive/` (root) | ~400 | Phần đầu §1-§7.5 |
| 7 | Modality-Analysis.md | `Core-Deep-Dive/` (root) | ~680 | Phần §1-§12 |

### §1.2 Files carried from session trước (Feeling Deep-Analysis-Draft)

Đã đọc trong session trước, không cần re-read trừ khi phát hiện gap:

- `Feeling.md` (1262L), `Feeling-Sources.md`, `Feeling-Accuracy.md`, `Feeling-Research.md`
- `Self-Pattern-Match.md` (outline), `Pattern-Resonance.md` (outline), `Feel-Development.md` (outline)
- `Logic-Feeling.md` (1762L) — relevant cho thread 2
- `Empathy-Mirror.md`, `Mirror-Neuron-Analysis.md`
- `Imagine-Final.md`, `Anchor-Schema.md`
- `Somatic-Articulation-Loop.md`

### §1.3 Files CHƯA đọc nhưng có thể relevant (deferred)

- `Schema.md` phần còn lại (§3.4+)
- `Schema-Operations.md` — schema operations chi tiết
- `Schema-Example.md` — examples
- `Anchor-Schema-Example.md` + `Anchor-Schema-Extreme-Example.md`
- `Body-Base/Body-Input-Enumeration.md` — substrate
- `backup/Chunk-Patterns.md` — may have old chunk framing
- `Imagination-Analysis-v2.md`
- `Domain/Valence.md`, `Domain/Domain-Interaction.md` — Object-Agent context

Defer: đọc theo nhu cầu khi drill từng theme, không cần upfront.

---

## §2 — File-by-file Key Findings

### §2.1 — Chunk.md (Schema/Chunk.md, 429 lines)

**Framework position**: DRAFT 2026-03-28. CORE mechanism file cho chunk system.

**Core definitions đã commit**:

- **Chunk = nhóm neurons WIRE TOGETHER fire thành 1 UNIT** (Hebb 1949)
- **Chunk vs Schema**: Chunk = ATOM (no purpose), Schema = MOLECULE (linked chunks với PURPOSE/FUNCTION)
- **Chunk MULTI-MODAL**: 1 chunk có thể span nhiều cortex (visual + auditory + somatic + emotional cho "mẹ")
- **Chunk HIERARCHY**: Meta-chunks chứa sub-chunks (expert lái xe = 1 meta-chunk thay vì 4 separate)

**4 compile mechanisms (§2)** — thread 7 (chunk genesis) partial answer:

1. **REPETITION** — 50+ lần → Hebbian LTP (Bliss & Lømo 1973)
2. **EMOTIONAL PEAK** — 1 lần đủ via amygdala + NE (Brown & Kulik 1977 flashbulb)
3. **MULTI-MODAL** — nhiều kênh cùng lúc, experience > imagine
4. **SLEEP CONSOLIDATION** — hippocampus replay (Walker 2017)

**Decay + reconsolidation**:
- KHÔNG có cơ chế unwire chủ động — chunk chỉ STRENGTHEN / WEAKEN / MODIFY
- Recall → tạm thời unstable → modify window (Nader 2000)
- "Quên" = retrieval path yếu, không phải delete
- Chunks sâu (childhood, emotional) ≈ không decay

**Operator model (§3)**:
- **Vô thức = OPERATOR CHÍNH (~95%)**: compile, run, evaluate, process nền
- **PFC = OPERATOR PHỤ (~5%)**: search, hold, create, modify, direct
- Limits: Vô thức chỉ đo body-base, PFC đo domain
- → Trực tiếp liên quan Feeling Deep Analysis Theme A (bidirectional architecture)

**PFC Search 4 modes (§4)**: QUICK SEARCH / BODY NOVELTY / LOOSE HOLD / ACTIVE LOCK
- Cortisol = amplifier (không phải driver)
- Spreading activation (Collins & Loftus 1975)

**Attention = query design (§6)**: PFC hold 4 search terms, nhưng CHỌN terms nào quyết định hit
- Emotional tags = search term ngầm từ amygdala

**Research đã cite trong Chunk.md**:
🟢 Hebb 1949, Bliss & Lømo 1973, Brown & Kulik 1977, Nader 2000, Chase & Simon 1973, Miller 1956, Cowan 2001, Collins & Loftus 1975, de Groot 1946, Klein 1998, Rumelhart & McClelland 1986, Walker 2017, Ebbinghaus 1885, Zeigarnik 1927.

**Đánh giá cho Chunk-Analysis drill**:
- **Phần này đã rất vững chắc**. Không cần rewrite.
- Cần **extend** ở: chunk genesis flow chi tiết (raw sensation → proto-chunk threshold), chunk chain dynamics without anchor, chunk upgrade mechanism.

---

### §2.2 — Chunk-Practical.md (Schema/Chunk-Practical.md, ~270 lines)

**Framework position**: DRAFT 2026-03-28. Ứng dụng + 4 failure modes.

**Key content**:

- **External tools** (§1): body external memory, người khác = external search engine, AI = external verbalizer, sách/video = chunk injection, experience = multi-modal injection
- **Chunk transfer A → B** (§2): abstraction cao → transfer dễ. Polymath vs specialist.
- **Chunk interference** (§3): thói cũ vs mới = 2 chunks fight, Wood & Neal 2007
- **4 failure modes** (§4):
  - Rumination (search loop stuck at local minimum) — Nolen-Hoeksema 2000
  - Active schema lock ("vừa chơi vừa lo") — Zeigarnik
  - Đầu trống (3 nguyên nhân: cortisol thấp / PFC mệt / terms mơ hồ)
  - Analysis paralysis (Schwartz 2004)
  - Brain fog (infrastructure — ngủ, ăn, inflammation)

**Đánh giá**:
- **Practical layer đầy đủ**. Không phải trọng tâm drill này.
- Chỉ reference khi cần (ví dụ thread 8 "decay without anchor" có thể connect với "brain fog + forgetting path weakening").

---

### §2.3 — Chunk-Search-Advanced.md (Schema/Chunk-Search-Advanced.md, ~220 lines)

**Framework position**: DRAFT 2026-03-28. Deep mechanism của search.

**⭐ Key finding cho thread 2 (liên kết)**:

> **§2 — "Aha!" = Link MỚI Giữa Chunks CŨ**
>
> "Aha KHÔNG phải tạo chunk MỚI — mà NỐI chunks cũ THEO CÁCH MỚI"
> - 2+ chunks đã tồn tại → chưa bao giờ linked → bỗng connection FOUND
> - Body-Reward CỰC: dopamine + opioid + cortisol DROP
> - 🟢 Gamma burst (Kounios & Beeman 2009)

**Đây là partial answer cho thread 2 ở layer "dynamic insight"**. Nhưng user's thread 2 ngoài dynamic aha còn có **static logical linking** ("2 chunk có nối được không về mặt logic") — đây vẫn là gap.

**Các mechanism khác**:
- **§1 Resonance signal vs noise** — PFC hold → spreading activation → chunks đúng → signal, chunks sai → noise. Cortisol × chunks matrix.
- **§3 Tip of the tongue** — chunk tồn tại nhưng retrieval path yếu (Brown & McNeill 1966)
- **§4 Incubation hold** — DMN tiếp tục process khi PFC offline (Walker 2017, Wagner 2004)
- **§5 Priming** — môi trường = passive primer (Meyer & Schvaneveldt 1971)
- **§6 Emotional tags** — amygdala tag → hidden search term (Schwarz & Clore 1983, Bower 1981)

**Đánh giá**:
- Aha = link mới giữa chunks cũ là **foundation đã có** cho thread 2. Cần **extend** sang layer static (không phải aha) + layer compile (logical connection trở thành new chunk).
- Thread 10 "right-wrong lờ mờ" có thể connect với resonance signal-to-noise (signal yếu = lờ mờ).

---

### §2.4 — Schema.md (Schema/Schema.md, phần đầu ~400 lines)

**Framework position**: DRAFT v2 2026-03-25 (Architecture v7.5)

**⭐ Critical findings**:

**§1.1 Chunk vs Schema** — đã quote trong Chunk.md nhưng ở đây chi tiết hơn:
- Chunk = atom. Schema = molecule.
- 3 trạng thái schema: COMPILED (auto-run) / ACTIVE (PFC đang dùng) / MONITOR (background alert)
- Chunks tạo từ 2 nguồn: vô thức (experience) HOẶC PFC (imagine → body check → compile)

**§2 — 2 con đường hình thành schema**:
1. **Vô thức tự build**: association learning, 1 experience đủ nếu emotional mạnh. Trẻ 3-4 tuổi PFC gần zero vẫn build 160+ strategies.
2. **PFC draft + compile**: imagine scenario → body simulate → check → compile nếu ok. Einstein thought experiment.

**⭐ §2 cross-contamination via shared chunks — PARTIAL THREAD 2**:

> "Schema KHÔNG tồn tại riêng lẻ → CHIA CHUNKS với schema khác"
>
> "Chunk [hồi hộp] thuộc nhiều schemas: tình yêu + sợ bị bỏ + gặp người mới"
>
> "Fire schema A → schema B CŨNG fire (vì shared chunks)"

**Đây là framework's implicit model của thread 2**: chunks kết nối qua việc **shared** giữa multiple schemas. Nhưng đây là **unintended side effect** (contamination), không phải **intentional logical linking** (user's "A liên quan B").

**§2.5 — 3 body signals kết thúc schema**:
- Satisfaction signal (vô thức tự dừng, PFC không biết)
- Body-reward (cả hai biết, PFC chọn)
- Body-pain (cả hai biết, PFC chọn)

**§3.1 depth gradient**: Body-need (sâu, tháng-năm) → Values (giữa, tuần-tháng) → Domain skills (nông, ngày)

**§3.2 — KHÔNG có "schema âm"** — chỉ có 3 loại xung đột:
- 2 schemas cùng context khác hướng (ăn + diet)
- Schema outdated (tiết kiệm lúc nghèo → khi lương ổn)
- Nhiều schemas đúng riêng nhưng tổng thể conflict (career + family + self-care)

**Đánh giá**:
- Chunk ↔ Schema relationship đã vững.
- **Shared chunks as connection mechanism** đã embedded (unintended contamination) — cần extend sang **intentional logical linking** (thread 2).
- Schema hình thành qua 2 paths là foundation cho thread 9 (cognition upgrade) — upgrade có thể = PFC path compile → feed back vào vô thức database.

---

### §2.5 — Object-Agent.md (Domain/Object-Agent.md, 581 lines, full)

**Framework position**: DRAFT v0.5 2026-04-12. File rất phát triển cho thread 5.

**⭐ Đã có trong framework**:

**§1 — 2 classification modes** (binary, hardware-level):

| OBJECT | AGENT |
|---|---|
| Deterministic | Non-deterministic |
| Tuân physics | Có mục tiêu riêng |
| Không state riêng | Có state (vui/buồn/đói) |
| Không reciprocate | Có reciprocate |
| Predictable, low novelty | Unpredictable, continuous novelty |

**§2 — Evidence**:
- 🟢 **Spelke Core Knowledge (2007)** — trẻ sơ sinh có innate distinction: Object (cohesion, continuity, contact) vs Agent (self-propelled, goal-directed, contingent)
- 🟢 **VTC neuroimaging (eLife 2019)** — Ventral Temporal Cortex có vùng riêng cho animate vs inanimate (hardware binary organization)
- 🟢 **Infant animate detection** — 9 tháng phân biệt motion pattern; face processing preference từ sơ sinh
- 🟢 **Piaget animism (1929)** — 2-7 tuổi overgeneralize agent

**⭐ §3 — Development timeline**:

| Giai đoạn | Tuổi | Trạng thái |
|---|---|---|
| **Hardware filter có sẵn** | 0-6 tháng | VTC binary filter hoạt động, chưa có agent MODEL |
| **Bắt đầu build agent model** | 6-12 tháng | Social referencing, 9.5-12mo helping behavior |
| **Agent model hình thành** | 14-24 tháng | Warneken & Tomasello 2006, 18-24mo mirror self-recognition (Amsterdam 1972) |
| **Overgeneralize rồi refine** | 2-7 tuổi | Animism phase, "ghế bị đau", "búp bê buồn" → 4-7yo refine |
| **Compiled + context-dependent** | Trưởng thành | Hardware filter + compiled schemas + context → classification cuối |

**⭐ §4 Schema override — bidirectional flip**:

**Object → Agent**: tượng Phật "Ngài", mẫu ảnh Đức Mẹ, cục đá được thờ, gấu bông "biết buồn", bụi cây chiến trường

**Agent → Object**: Meat Paradox (con bò → "beef"), Dehumanization (Grossman 1995), Medical dissociation, Sacred object disposal ritual

**§4 ⚠️ CONFLICT ở ranh giới** = evidence cho binary classification:
- Uncanny Valley (Mori 1970)
- Chân ếch co giật
- Live food
- Người trong coma

**§5 Agency spectrum** (hardware binary + schema overlay → perceived spectrum):

```
Mẹ thật → Người lạ → Chó (co-evolved 30k years) → Video call → Ảnh → Tượng thần → Mẫu ảnh → Cục đá thờ → Cục đá thường
```

Pattern: càng xuống → agent processing càng ít, compiled schema càng nhiều. Body respond CÙNG pathway bất kể source.

**§6 Object × Logic-Modeling 2×2 matrix**:

| | Logic | Modeling |
|---|---|---|
| **Object** | ⭐ Default (physics, math) | Insight mode (Einstein "cưỡi tia sáng") |
| **Agent** | ⚠️ Systematize (dehumanization nguy hiểm) | ⭐ Default (empathy, social predict) |

**Đánh giá cho thread 5**:
- **Coverage 85%**. Đã có: binary classification, Spelke, development timeline, schema override, agency spectrum.
- **Gap nhỏ còn thiếu**: User's new angle "trẻ con chưa phân loại, dùng toàn bộ não để tạo pattern cho mọi vật thể" — Object-Agent.md nói Spelke có innate distinction, nhưng user hypothesis nói ban đầu trẻ em dùng whole brain undifferentiated rồi mới học phân loại. **Đây là tension cần analysis**.
- **Extension cần thiết**: thread 11 "chunk-agent-schema → thiện cảm" — user's formulation "chunk kết nối với agent + kết nối với schema có ích cho bản thân → thiện cảm với agent đó" **chưa có trong Object-Agent.md**. Đây là compound mechanism mới.

---

### §2.6 — Connection.md (Core-Deep-Dive/Connection.md, ~400 lines đọc)

**Framework position**: DRAFT 2026-03-28.

**⚠️ Important disambiguation**: Connection.md nói về **inter-personal connection** (harmony giữa melodies), **KHÔNG** phải về chunk-chunk logical connection (thread 2).

**Key content**:

**§1 Connection = emergent property** (không phải L2 sub-channel):
- Không nằm trong melody nào → xuất hiện khi 2+ melodies tương tác
- Giống harmony trong nhạc
- Body drive connection giống drive đi tìm thức ăn

**§2 Amplify L0-L3**: Connection = force multiplier cho cả body-base (đàn bảo vệ, co-regulate, learn từ nhau, social calibrate)
- 🟢 Social Brain Hypothesis (Dunbar 1998)

**⭐ §3 — Virtual chunks (relevant cho thread 11)**:
- "Tôi không biết mài gỗ lấy lửa → bạn biết → CHÚNG TÔI có lửa"
- N người = access chunks cả nhóm
- **Virtual chunks cần TRUST** — bạn thân = access cao + reliable
- Civilization = mạng lưới virtual chunks

**§4 Melody calibration (4 functions)**:
1. Error correction
2. Convergence (emotional contagion — Hatfield 1994)
3. Dual real-check
4. Complementary

**§5 Dunbar's number** (~150, phân tầng: 5 / 15 / 50 / 150)

**§6 Distance spectrum** (fidelity × channels)

**§7 Contexts** (1 drive × N contexts)

**§7.5 Connection × Imagine-Final** — body preview "gặp người này → melody sẽ thế nào"

**Đánh giá**:
- Thread 2 (user's "liên kết") **KHÔNG** phải cùng thứ với Connection.md.
- User's thread 2 cần **concept mới**: "chunk-chunk logical linking" — khác với "chunk-chunk shared" (contamination), khác với "chunks linked by aha" (dynamic insight).
- Connection.md §3 virtual chunks có thể feed vào thread 11 (thiện cảm cơ chế) — chunks của mình + chunks của agent → thiện cảm related to "bạn có gì tôi cần".

---

### §2.7 — Modality-Analysis.md (Core-Deep-Dive/Modality-Analysis.md, ~680 lines)

**Framework position**: DRAFT 2026-03-18.

**⭐ Foundation cho nhiều threads**:

**§1 — 5 Experience + 1 Communication modality**:

**5 Experience modalities** (encode trải nghiệm trực tiếp):
- Visual (V1-V5, Fusiform)
- Auditory (auditory cortex, Wernicke)
- Somatic (Insula + somatosensory)
- Motor (motor cortex + cerebellum + BG)
- Emotional (amygdala + insula + limbic)

**1 Communication modality** (META-modality — labels + references):
- Verbal / Gesture / Writing / Drawing / Video / Code
- Vùng não: Broca + Wernicke + Arcuate fasciculus

**⭐ §2.0 — Communication Modality findings cho thread 6 (Grammar)**:

- **Thinking ≠ Language** — Fedorenko MIT 2011-2024: 2 networks tách biệt (language vs multiple demand/reasoning). Hỏng language → vẫn reasoning.
- **Verbal = COMMENTATOR** bóng đá, không phải người đá. Meditation dừng inner voice vẫn suy nghĩ.
- **⭐ Broca's area HANDLES SEQUENTIAL + HIERARCHICAL structure** — không chỉ language:
  - Action sequences (Fadiga et al.)
  - Musical syntax (Maess et al. 2001)
  - Grammatical hierarchy
- **4 functions of communication modality**: LABEL, TRANSFER, GHÉP, SEQUENCE

→ **Đây là foundation gần như trực tiếp cho thread 6 hypothesis** "grammar = scaffolding". Framework đã nói Broca handles hierarchical sequence processing including grammatical structure. Thread 6 chỉ cần extend sang specific claim: grammar categories = chunk taxonomy scaffolding.

**§2.1 Experience modalities detail**:
- Somatic: CROSS-DOMAIN mạnh nhất (body state abstract representation)
- Motor: domain-specific (skill tennis ≠ skill bơi)
- Emotional: fastest (~12ms amygdala)

**⭐ §3 Encode types table** — quan trọng cho thread 1 (trừu tượng vs siêu hình):

| Modality | Kiểu encode | Cấu trúc | Cross-domain |
|---|---|---|---|
| Visual | Discrete points + spatial relations | Hierarchical graph | Ngang filtered (structural match) |
| Auditory | Temporal patterns | Sequential timeline | Nhẹ |
| Motor | Action sequences | Procedural steps | Rất thấp |
| Emotional | Valence + intensity | Binary + analog | Ngang social |
| **Somatic** | **CONTINUOUS FIELD** | **Holistic analog** | **CỰC NGANG** (unfiltered body state) |
| Communication | Labels + references | Sequential symbolic | Ngang qua label combining |

→ **Visual = structural match (siêu hình hypothesis)**, **Somatic = body state match any domain (trừu tượng hypothesis)**. Thread 1 can be derived from this.

**⭐ §4 Chunk depth = Modality count** — directly thread 4:

| # Modalities | Depth | Example |
|---|---|---|
| 1 | Surface | "Nước sôi 100°C" (verbal only) |
| 2-3 | Medium | "Đèn đỏ dừng lại" |
| 4 | Deep | "Sợ chó" (visual + auditory + somatic + emotional) |
| 5-6 | Very deep | "Tôi vô giá trị" (all modalities) |

→ **Chunk với verbal chỉ = +1 modality label**. Chunk không có verbal có thể sâu hơn hoặc nông hơn tùy các modality khác. **Thread 4 đã có cơ sở**.

**§5 Modality interaction**: Reinforcement / Conflict / Compensation
- "Biết mà không làm" = verbal fixed (1 modality), somatic+emotional chưa (4-5) → 4 > 1

**§6 Modality × Therapy** — match therapy modality với chunk modality profile

**⭐ §7 — Modality development by age** (relevant cho thread 5 + agent question):

| Age | Dominant modalities |
|---|---|
| 0-2 | Somatic●●●●● + Emotional●●●●● (attachment) |
| 2-4 | + Motor + Visual (multi-modal explosion) |
| 4-7 | + Verbal (creativity peak, visual still strong) |
| 7-12 | Verbal TAKE OVER (school training) |
| 13-18 | Emotional SPIKE |
| 18+ | Verbal dominant (majority) |

→ **User's hypothesis "trẻ con dùng toàn bộ não làm pattern"** có thể refine: **trẻ 0-4 chỉ có somatic/emotional/motor/visual — verbal chưa có → chunks không có label**. Đây là giai đoạn "whole brain pattern" trước grammar scaffolding.

**§8 Modality → chain direction**:
- Verbal dominant → chain DỌC → specialist
- Somatic dominant → chain NGANG → improviser
- → Cross-domain

**§11 Concept-first vs Label-first** (direct cho thread 4):

- **Somatic-dominant**: cảm nhận concept TRƯỚC → label SAU (hoặc không cần)
- **Verbal-dominant**: label TRƯỚC → hiểu concept QUA label

**Đánh giá**:
- **Modality-Analysis.md là foundation nền tảng** cho threads 1, 3, 4, 6 — và bổ sung 5.
- Thread 6 (Grammar-Scaffolding) có phần §2.0 là near-direct foundation.
- Thread 1 (trừu tượng vs siêu hình) có thể derive từ §3 encode types (visual structural vs somatic field).
- Thread 4 (chunk verbal vs non-verbal) đã có rất nhiều ở §4 + §11.

---

## §3 — Cross-cutting Framework Insights

Synthesis findings vượt khỏi file đơn lẻ:

### §3.1 — Chunk architecture đã có nhưng phân tán

Chunk concept được describe ở 3 file chính + reference từ nhiều file khác:

- **Schema/Chunk.md** — core mechanism
- **Schema/Chunk-Practical.md** — ứng dụng
- **Schema/Chunk-Search-Advanced.md** — deep search
- **Schema/Schema.md §1.1** — vị trí trong Schema
- **Modality-Analysis.md §4** — depth via modality count
- **Domain/Object-Agent.md** — chunk classification (hardware binary + schema overlay)
- **Connection.md §3** — virtual chunks (external access)
- **Somatic-Articulation-Loop.md** — body knowledge → verbal label
- **Feeling/ folder** (Feeling Deep Analysis) — chunk như substrate cho PFC observation

**Architectural observation**: Chunk là **cross-cutting concept** — không đơn thuần là con của Schema. User's hypothesis "Chunk là substrate, Feeling là view lên Chunk" có basis nếu xem chunk không chỉ ở Schema/ mà ở MỌI layer.

### §3.2 — Ba loại "chunk connection" đã ngầm trong framework

Reading pass phát hiện **3 loại chunk connection khác nhau** tồn tại rải rác:

1. **Shared chunk (cross-contamination)** — Schema §2: 2 schemas share chunk → fire A triggers B. Passive, unintended.
2. **Aha = dynamic link** — Chunk-Search-Advanced §2: 2 chunks cũ chưa bao giờ linked → bỗng PFC find connection. Active, insight moment.
3. **Compile into meta-chunk** — Chunk §2: 4 sub-chunks [lái, phanh, mirror, signal] → 1 meta-chunk [LÁI XE]. Consolidation.

**User's thread 2 "liên kết logic"** có thể là **loại thứ 4**:
4. **Static logical linking** — 2 chunks PFC hold + ask "có nối được không?" → body/PFC check compatibility → output verbal "A liên quan B". Intentional, compile-time-ish.

→ **Thread 2 cần define rõ** loại connection nào, và mechanism ra sao.

### §3.3 — Verbal là "commentator" — foundation cho thread 4 + 6

Modality §2.0 commit rõ: **Verbal = commentator narrating unconscious thinking**, không phải thinking itself. Thinking ≠ language (Fedorenko 2011-2024 dissociable networks).

→ **Thread 4** (chunk verbal vs non-verbal): chunk không có verbal **vẫn là chunk thật**, chỉ thiếu label. Verbal label là 1 modality add-on, không phải điều kiện để chunk tồn tại.

→ **Thread 6** (Grammar-Scaffolding): Grammar là scaffolding cho **chunk labeling + chain sequencing**, không phải cho thinking. Broca xử lý sequential/hierarchical structure bao gồm ngữ pháp — đây là foundation đã có.

### §3.4 — Child development timeline nhất quán across files

Modality-Analysis §7 + Object-Agent.md §3 cho cùng một timeline ở 2 góc khác nhau:

| Age | Modality (Modality-Analysis) | Agent processing (Object-Agent) |
|---|---|---|
| 0-2 | Somatic + Emotional dominant, verbal chưa có | VTC binary filter hoạt động, chưa có agent model |
| 2-4 | Multi-modal explosion (motor, visual), verbal sơ khai | Build agent model (helping 12mo, mirror self-rec 18-24mo) |
| 4-7 | Verbal grows, visual still strong (creativity peak) | Animism phase (overgeneralize agent) + begin refine |
| 7-12 | Verbal take over (school) | Agent model compiled, context-dependent |

→ **Thread 5 refinement**: User's hypothesis "trẻ con dùng toàn bộ não" có thể map vào giai đoạn **0-2 somatic/emotional dominant + verbal absent**. Giai đoạn này chunks **không có label**, pattern dựa trên multi-modal experience. Thread 4 + 5 overlap ở đây.

### §3.5 — Schema/Chunk hình thành qua 2 con đường nhất quán

Chunk.md §2 + Schema.md §2 đều commit 2 paths:
- **Vô thức compile** qua experience (fast, from direct encounter)
- **PFC draft** qua imagine (slower, includes novel scenarios)

→ **Thread 7 (chunk genesis)** có foundation. Gap là: chi tiết flow "raw sensation → proto-chunk → labeled chunk" và threshold nào "chunk exists".

### §3.6 — Framework đã có "right-wrong detection" rải rác

Thread 10 (right-wrong lờ mờ):
- **Feeling Theme D** (session trước): Spelke VoE, Einstein Hadamard 1945, pattern match + ACC
- **Chunk-Search-Advanced §1**: Resonance signal vs noise — signal mạnh = "đúng rồi", noise = "rối"
- **Chunk-Search-Advanced §2**: Aha moment = pattern match breakthrough
- **Schema-Operations** (chưa đọc lại): body evaluate mechanism

→ **Gap**: Chưa có **unified model** cho "lờ mờ" specifically. Lờ mờ có thể = weak resonance signal (borderline threshold) hoặc multi-weak-signals convergence. Cần model riêng.

---

## §4 — Thread-to-Coverage Mapping

Re-map 11 threads với evidence từ Phase 1 reading.

### §4.1 — Coverage matrix

| # | Thread | Existing coverage | Gap | Priority |
|---|---|---|---|---|
| **1** | Trừu tượng vs siêu hình | Modality §3 encode types (visual structural vs somatic field), §8 chain direction | CHƯA có framing "trừu tượng" vs "siêu hình" explicit. Không có section riêng. | MEDIUM (có thể derive nhanh) |
| **2** | Liên kết chunk-chunk (logic) | Chunk-Search-Advanced §2 (aha dynamic), Schema §2 (shared contamination), Chunk §2 (compile meta-chunk) | **Gap: static logical linking như user formulate "A liên quan B"** — chưa có file/section | **HIGH** (concept mới) |
| **3** | Feeling vs intuition gradient | Feeling Deep Analysis (session trước): Feeling = PFC observation of body-base. Chunk-Search-Advanced §1 resonance signal | CHƯA unified "feeling vs intuition" framing. Cần decompose gradient trục. | HIGH |
| **4** | Chunk verbal vs non-verbal | Modality §4 depth, §11 concept-first vs label-first, §2.0 verbal as commentator, Somatic-Articulation-Loop | Partial — có foundation, cần synthesis section | MEDIUM |
| **5** | Agent question | **Object-Agent.md rất đầy đủ** — binary, Spelke, development 0-7, animism, schema override, agency spectrum | Small gap: "trẻ con dùng toàn bộ não làm pattern chưa phân loại" tension với Spelke innate. User's new angle. | MEDIUM (mostly covered) |
| **6** | Grammar-Scaffolding | Modality §2.0 (Broca handles hierarchical sequence), §8 chain direction | **Gap lớn** — specific claim "grammar categories = chunk taxonomy scaffolding" chưa có. Vietnamese classifier system chưa analyze. | **HIGH** (hypothesis cần file riêng) |
| **7** | Chunk genesis flow | Chunk §2 (4 compile mechanisms), Schema §2 (2 paths) | Flow chi tiết "raw → proto → chunk → labeled" + threshold chưa unified | HIGH |
| **8** | Chain + anchor decay dynamics | Anchor-Schema (session trước) + Chunk §2 decay + Zeigarnik | Decay curve **without anchor** chưa modeled. Anchor type ranking chưa có. | HIGH |
| **9** | Nâng cấp nhận thức | Self-Pattern-Match outline 8 stages, Feel-Example 9 categories, Schema §2 2 paths | Meta-mechanism cho upgrade chưa có | MEDIUM |
| **10** | Right-wrong lờ mờ | Feeling Theme D, Chunk-Search-Advanced §1 signal/noise | "Lờ mờ" specifically chưa modeled (weak signal? multi-weak convergence?) | MEDIUM |
| **11** | Chunk-agent-schema → thiện cảm | Feeling Theme E (compound valence), Object-Agent §5, Connection §3 virtual chunks | User's specific formulation "chunk ↔ agent + chunk ↔ schema useful → thiện cảm" chưa compile | MEDIUM |

### §4.2 — Counted

- **HIGH priority gaps**: 5 (threads 2, 3, 6, 7, 8)
- **MEDIUM priority**: 5 (threads 1, 4, 5, 9, 11)
- **LOW / no gap**: 1 (thread 10 mostly derivable)

### §4.3 — Ordering recommendation cho drill

Suggested drill order (based on dependency + user's flagged priority):

1. **Thread 5 extension** (Agent question — mostly covered, quick win, foundation cho 11)
2. **Thread 7** (Chunk genesis — foundation cho genesis flow)
3. **Thread 2** (Chunk-chunk linking — concept mới, foundation cho thread 6 + 9)
4. **Thread 4** (Chunk verbal vs non-verbal — synthesis của existing)
5. **Thread 6 Grammar-Scaffolding** (depends on threads 2 + 4)
6. **Thread 8** (Chain + anchor decay — builds on 2 + 7)
7. **Thread 3** (Feeling vs intuition gradient — depends on unified chunk model)
8. **Thread 11** (Thiện cảm refined — depends on 5 + agent extension)
9. **Thread 9** (Cognition upgrade — meta, depends on most)
10. **Thread 1** (Trừu tượng vs siêu hình — can emerge from modality analysis of chunk)
11. **Thread 10** (Right-wrong lờ mờ — can emerge from chunk resonance model)

→ **plan.md** sẽ propose concrete file sequence.

---

## §5 — Emergent Hypotheses từ Reading

Những ý tưởng nảy ra từ reading pass — chưa committed, chỉ để plan.md quyết định có drill không.

### §5.1 — H1: Chunk là substrate, không phải "data trong Schema"

**Bối cảnh**: Framework hiện tại đặt Chunk trong Schema/ folder, nói "Chunk = ATOM, Schema = MOLECULE". Cấu trúc này có nghĩa là "Chunk phục vụ Schema". Nhưng reading pass cho thấy chunk cross-cut:

- Chunk xuất hiện ở Schema, Domain (Object-Agent), Modality, Connection, Feeling, Imagination, Body-Base.
- User's hypothesis: "Feeling = PFC đọc body-base dựa trên chunk tích lũy. Chunk dùng để plan, giao tiếp, thiện cảm..."

**Nếu H1 đúng**: Chunk nên được promote từ "Schema sub-concept" thành "cross-cutting substrate". Schema/Chunk.md có thể giữ nguyên, nhưng cross-references toàn framework cần cập nhật.

**Status**: Chưa commit. Cần drill 99-Synthesis quyết định.

### §5.2 — H2: Thread 2 là loại chunk connection thứ 4

Framework có 3 loại chunk connection đã ngầm (§3.2). User's thread 2 là loại thứ 4: **static logical linking** (PFC hold A + B → ask "có liên quan không?" → body/PFC check → output "có" hoặc "không").

**Mechanism candidate**:
- PFC hold chunk A + chunk B
- Spreading activation từ cả 2 chunks
- Check overlap region (shared chunks, shared context, shared modality)
- Body-reward nếu overlap rõ → "có nối được"
- Body-dissonance nếu không overlap → "không liên quan"
- Output verbal: "A liên quan B qua X"

**Khác aha**: Aha = spontaneous discovery. Static linking = intentional check.

**Status**: Chưa commit. Drill thread 2 sẽ validate.

### §5.3 — H3: Grammar-scaffolding đã partial-embedded trong framework

Modality §2.0 đã commit: Broca handles sequential + hierarchical structure including grammatical hierarchy. Labels compress multi-modal chunks → PFC hold dễ hơn.

**Nếu H3 đúng**: Thread 6 không phải "thêm concept mới" mà là "extend existing" — specifically claim grammar categories (classifier, gender, case, tense, evidentiality) = chunk type taxonomy. Grammar = evolved external scaffolding cho chunk-chain được tập thể compile.

**Status**: Strong support từ Modality §2.0. Grammar-Scaffolding drill sẽ formalize.

### §5.4 — H4: Trừu tượng vs siêu hình = modality encoding difference

User hypothesis:
- Siêu hình = visual-heavy imagine, PFC hold nặng
- Trừu tượng = somatic hoặc multi-modal mix

Modality §3 encode types support partial:
- Visual = discrete structural match
- Somatic = continuous field, any-domain match

**Nếu H4 đúng**: Siêu hình (metaphysical) = imagine complex NEVER-SEEN things via **visual structural projection** (không gian, thời gian abstract, cosmic). Trừu tượng (abstract) = imagine NEVER-FELT things via **somatic cross-domain resonance** (justice, truth, beauty).

**Verbal categorization**: Siêu hình có labels mờ (God, infinity, soul). Trừu tượng có labels đa nguồn (công bằng = social + emotional + somatic + verbal converge).

**Status**: Plausible. Drill thread 1 sẽ test.

### §5.5 — H5: Lờ mờ = multi-weak-signal convergence

Thread 10. Chunk-Search-Advanced §1 cho framing signal vs noise. "Lờ mờ" có thể = **multiple weak signals converging** (không một signal đủ mạnh, nhưng cộng lại = ngưỡng detection).

**Contrast với aha**: Aha = 1 strong link fire rõ ngay. Lờ mờ = N weak hits convergence, PFC nhận dạng "có gì đó" nhưng chưa articulate.

**Status**: Candidate mechanism. Drill thread 10 sẽ test.

### §5.6 — H6: Chunk chain decay without anchor follows Ebbinghaus

Thread 8 (chain + anchor decay). Chunk.md §2 cite Ebbinghaus savings in relearning. Hypothesis: chunks không có anchor follow classical forgetting curve (exponential decay), anchored chunks bypass decay via re-trigger mechanisms (anchor re-fire chunk periodically).

**Anchor type ranking candidate**:
- Verbal anchor — mạnh nhất (linguistic compression + social reinforcement)
- Ritual anchor — mạnh (multi-modal + periodic fire)
- Visual anchor — medium (context trigger)
- Object anchor — medium (somatic trigger)
- Context anchor — weakest (requires environmental match)

**Status**: Hypothesis. Drill thread 8 sẽ test với memory research.

---

## §6 — Questions đã emerge từ reading

Open questions cần drill trả lời:

### §6.1 — Chunk definition questions

Q1. Threshold nào "chunk tồn tại"? Có phải khi N neurons fire đồng bộ k lần? (Chunk.md nói qualitative nhưng không quantify)

Q2. Chunk có thể có "proto-chunk" state không? (raw sensation + partial pattern, chưa compile đủ)

Q3. Chunks implicit vs explicit — framework distinguish không? (Modality §11 concept-first implicit; label-first explicit)

### §6.2 — Connection questions

Q4. Static logical linking (thread 2) — mechanism cụ thể? PFC hold A+B → check gì? (hypothesis §5.2 chưa test)

Q5. Shared chunk contamination (Schema §2) có cơ chế phân biệt intentional link vs accidental bleed không?

Q6. Aha vs static link vs compile — 3 mechanism tách biệt hay overlap?

### §6.3 — Agent + child questions

Q7. Spelke innate distinction vs user's "whole brain undifferentiated" — conflict hay complementary?

Q8. Gap giữa 6-12 tháng (bắt đầu agent model) và 18-24 tháng (mirror self-recognition) — cơ chế đang hình thành gì cụ thể?

Q9. "Chunk ↔ agent + chunk ↔ schema useful → thiện cảm" (thread 11) — là compound valence hay là mechanism riêng?

### §6.4 — Verbal + Grammar questions

Q10. Grammar categories (noun/verb/classifier/case) — tương ứng với chunk categories gì?

Q11. Vietnamese classifier system (con/cái/chiếc) — force animacy classification. Tương ứng với VTC binary Object-Agent không?

Q12. Pre-verbal chunks (0-2 tuổi) khác post-verbal chunks (4+) ở điểm nào ngoài label?

### §6.5 — Feeling-chunk interface questions

Q13. Feeling = PFC observation of body-base (Feeling Theme A). Body-base = sum of firing chunks? Hay body-base là layer riêng?

Q14. Intuition gradient (thread 3) — trục nào? (User propose "PFC chỉ đọc" vs "PFC tích cực dò tìm")

Q15. Lờ mờ right-wrong (thread 10) — là gradient của aha hay cơ chế riêng?

### §6.6 — Decay + anchor questions

Q16. Chunks không có anchor — decay curve nào? Exponential? Power law?

Q17. Re-anchoring chunk (đổi loại anchor) — có khả thi không? Mechanism?

Q18. Anchor strength hierarchy — verbal > ritual > visual > object > context? Hay khác?

### §6.7 — Cognition upgrade questions

Q19. "Nâng cấp" nhận thức — có moment discrete hay gradient liên tục?

Q20. Role của PFC vs vô thức trong upgrade?

Q21. Stuck ở stage nào do gì? (Modality balance? Missing anchor? Missing input?)

---

## §7 — Gap Analysis → File Proposals

Dựa trên thread-coverage mapping (§4) + emergent hypotheses (§5) + questions (§6), đề xuất file structure cho drill:

### §7.1 — Files cần tạo mới (novel content)

| File | Scope | Thread(s) primary | Thread(s) secondary |
|---|---|---|---|
| `01-Agent-Question-Extension.md` | Extend Object-Agent với user's new angles | 5 | 11 |
| `02-Chunk-Genesis.md` | Raw sensation → proto → chunk → labeled flow | 7 | 4, 9 |
| `03-Chunk-Connection-Logical.md` | Static logical linking mechanism (thread 2) | 2 | 6 |
| `04-Chunk-Verbal-Interface.md` | Verbal as modality add-on, concept vs label first | 4 | 6 |
| `05-Chunk-Chain-Anchor-Decay.md` | Anchor types, decay dynamics, re-anchoring | 8 | 7 |
| `06-Chunk-Feeling-Interface.md` | Feeling/intuition gradient from chunk layer | 3 | 10 |
| `07-Thien-Cam-Mechanism.md` | Chunk-agent-schema compound → thiện cảm | 11 | 5 |
| `08-Abstract-Metaphysical.md` | Trừu tượng vs siêu hình derived from modality | 1 | 4 |
| `09-Cognition-Upgrade.md` | Meta-mechanism for nhận thức upgrade | 9 | 7 |
| `10-Right-Wrong-Vague.md` | Lờ mờ detection via weak signal convergence | 10 | 3 |

### §7.2 — Sub-folder Grammar-Scaffolding/

| File | Scope |
|---|---|
| `Grammar-Scaffolding/plan.md` | Sub-plan riêng |
| `Grammar-Scaffolding/Grammar-Scaffolding.md` | Core hypothesis + construction grammar + linguistic relativity moderate + Vietnamese classifier case study |
| `Grammar-Scaffolding/(future).md` | Placeholder cho expand (classifier systems, evidentiality, bilingual, L2 acquisition...) |

### §7.3 — Synthesis file

| File | Scope |
|---|---|
| `99-Synthesis.md` | Cross-theme integration, architectural decisions (H1 chunk as substrate?), 5-10 meta-insights, open questions consolidation, framework update recommendations |

### §7.4 — Plan files

| File | Scope |
|---|---|
| `plan.md` | Master north star — scope, themes, drill order, reading list, phases, success criteria |
| `Grammar-Scaffolding/plan.md` | Sub-plan cho Grammar-Scaffolding riêng |

**Tổng số file dự kiến**: 10 analysis files + 2 plan files + 1 synthesis + 1 reading notes (file này) = **14 files** trong Chunk-Analysis folder.

---

## §8 — Recommendations cho Phase 2 (plan.md)

### §8.1 — Scope boundary recommendations

**IN scope của Chunk-Analysis drill**:
- 11 threads đã liệt kê
- Architectural question: chunk as substrate (H1)
- File proposals trong §7

**OUT of scope** (defer):
- Rewrite Schema/Chunk.md — nếu drill phát hiện cần update, feed back via recommendations, không edit trong drill này
- Rewrite Object-Agent.md — chỉ write Extension file, không edit trực tiếp
- Promote Chunk thành top-level — chỉ recommend trong 99-Synthesis, không execute
- Deep dive vào Logic-Feeling.md internals (đã cover session trước)
- Child development full file rewrite

### §8.2 — Drill order recommendation

Dựa trên dependency analysis §4.3, đề xuất **3 phases of drill**:

**Phase A — Foundation (threads 5, 7, 2)**:
- 01-Agent-Question-Extension (mostly covered, quick win, foundation)
- 02-Chunk-Genesis (genesis flow needed by others)
- 03-Chunk-Connection-Logical (concept mới, used by 4, 6, 11)

**Phase B — Core concepts (threads 4, 6, 8, 3)**:
- 04-Chunk-Verbal-Interface (synthesis)
- Grammar-Scaffolding/Grammar-Scaffolding.md (depends on 2 + 4)
- 05-Chunk-Chain-Anchor-Decay (builds on 2 + 7)
- 06-Chunk-Feeling-Interface (depends on unified chunk model)

**Phase C — Compound + meta (threads 11, 9, 1, 10)**:
- 07-Thien-Cam-Mechanism
- 09-Cognition-Upgrade
- 08-Abstract-Metaphysical
- 10-Right-Wrong-Vague
- 99-Synthesis

**Timeline estimate**: Mỗi file ~400-700 lines. 10 files × ~500 = 5000 lines. Grammar-Scaffolding có thể 600-900. Synthesis 1000+. **Total drill ~7000-9000 lines**. Tương đương Feeling Deep Analysis (~8070 lines) — **scale hợp lý**, 2-4 sessions to complete.

### §8.3 — Success criteria cho drill

- 11 threads có answer clear (even if hypothesis, not settled)
- 21+ open questions (§6) được address hoặc explicit defer với reason
- H1-H6 hypotheses có verdict (validated / refined / rejected / pending)
- Architectural recommendation trong 99-Synthesis: có nên promote Chunk thành top-level không?
- Framework update list: 5-10 specific updates đề xuất cho existing files (Chunk.md, Schema.md, Object-Agent.md, Modality-Analysis.md, Anchor-Schema.md, Feeling files)
- User's meta-signal "có gì đó còn thiếu" (session trước) được address: gap đã articulate được chưa?

### §8.4 — What plan.md should contain

- §0 Purpose + north star
- §1 11 threads decomposed with sub-questions
- §2 H1-H6 hypotheses to test
- §3 File sequence (3 phases)
- §4 Dependency graph
- §5 Reading list for each file
- §6 Open questions (from §6 here)
- §7 Success criteria
- §8 Stop points for user review

---

## §9 — Notes về methodology

### §9.1 — Language convention

Tiếng Việt primary cho framework concepts + English technical terms (Hebb, Spelke, Cowan, etc.). Giữ nguyên convention Feeling Deep Analysis session trước.

### §9.2 — Confidence marking

Tuân thủ framework convention:
- 🟢 Research support (cited study)
- 🟡 Framework suy luận (consistent với framework logic)
- 🔴 Hypothesis (speculative)

### §9.3 — No personal examples

Per `feedback_no_personal_info.md` rule: Framework examples chỉ dùng general situations hoặc public historical figures (Einstein, Archimedes, Spelke, etc.). KHÔNG dùng personal profile của user.

### §9.4 — Integration với Feeling Deep Analysis

File 99-Synthesis nên cross-reference Feeling Deep-Analysis-Draft output để không duplicate work. Specifically:
- Feeling Theme A (architecture) → feed Chunk feeling-interface
- Feeling Theme D (right-wrong) → feed thread 10
- Feeling Theme E (empathy giving) → feed thread 11

---

## §10 — Status + Next Step

### §10.1 — Phase 1 status

✅ Discovery complete — 7 files read in this session + files carried from Feeling session  
✅ Cross-cutting insights synthesized (§3)  
✅ Thread-to-coverage mapping (§4)  
✅ Emergent hypotheses (§5)  
✅ Open questions captured (§6)  
✅ File proposals (§7)  
✅ Recommendations for plan.md (§8)

### §10.2 — Next step

**Phase 2**: Write `plan.md` (master) dựa trên recommendations §8 của file này.  
**Phase 3**: Write `Grammar-Scaffolding/plan.md` (sub-plan).  
**Phase 4**: Stop for user review trước khi drill implementation.

**Stop point**: Không bắt đầu drill content cho bất kỳ thread nào trong session này. Session này chỉ là **planning session**. Drill implementation là sessions sau.

---

---

## §11 — Refinements after user feedback (Phase 2.5)

> Added after user review of Phase 2 output. Captures:
> (a) Discovery of `Domain/Valence.md` — foundation gần như trực tiếp cho thread 11
> (b) Thread 11 rename `Thien-Cam-Mechanism` → `Chunk-Valence`
> (c) New hypothesis H7 (valence = chunk × schema interaction, not chunk-intrinsic)
> (d) Thread 11 coverage jump 40% → 80%
> (e) 5 questions thêm (Q22-Q26)

### §11.1 — Domain/Valence.md discovered

File **không** đọc trong Phase 1 reading pass (vì focus on Chunk + Modality + Schema + Object-Agent), nhưng Valence.md là foundation trực tiếp cho thread 11 — user raise vấn đề "positive-negative feeling toward chunks" và Valence.md **đã define** concept này.

**Framework position**: `Core-Deep-Dive/Domain/Valence.md`, DRAFT v0.5, 2026-04-12. Đọc §0-§6 (~400 lines).

**Key commits đã có trong Valence.md**:

- **§1 Definition**: "Valence = đánh giá của body về cách 1 entity ảnh hưởng body channels"
- **§1 Multi-channel** — không phải 1 trục tốt/xấu. Mẹ = { L1++, L2++, L2autonomy--, L3+, L3novelty- } → "yêu và ghét cùng lúc"
- **§1 Dynamic** — dao lần đầu cắt { L0-- }, sau khi học { L1++ }
- **§1 Context-dependent** — quả bom trong tay đồng đội vs kẻ thù
- **§1 Stored in schema** — compile qua experience, gặp lại entity → valence load ngay
- **§2 Profile structure** — channels L0 Alive / L1 Survival / L2 Quality / L3 Pattern + meta-dimensions (Trust, Predictability, Replaceability, Dependency)
- **§3 Object vs Agent** — Object sparse + stable + one-way; Agent dense + dynamic + bidirectional + unpredictable
- **§4 4 formation sources**:
  1. Direct experience (most accurate, slowest)
  2. Observed experience (mirror, 10-30% intensity)
  3. Schema inheritance (fastest, may be wrong — foundation cho propaganda work)
  4. Context inference (modeling mode)
- **§5 Update mechanisms**:
  1. Reinforcement (compile deeper)
  2. Revision (gradual shift)
  3. Violent flip (betrayal, sacred desecration)
- **§5 Speed factors**: Intensity × Frequency × Recency
- **§5 Biases**: Negativity bias (🟢 confirmed psychology research), Confirmation bias
- **§6 Cases**: Dao, Mẹ, Bạn B bị cắt, Thiên Chúa

**Coverage với thread 11 user**: **~80%**. Core mechanism đã vững, không cần rewrite.

**Gap Valence.md chưa cover** (cần `07-Chunk-Valence.md` extend):

- ❌ **Aesthetic valence** (hoàng hôn đẹp, cục đá đẹp, bầu trời âm u không đẹp) — L3 experience/novelty có thể cover ngầm, nhưng chưa có section riêng
- ❌ **Disgust mechanism** (gián kinh tởm, nhà bừa bộn như bãi rác) — chưa có section, có thể là hệ thống riêng tách biệt với threat
- ❌ **Chunk-layer framing** — Valence.md dùng từ "entity", chưa tie specifically vào chunk layer
- ❌ **H7 chunk-in-schema context** (§11.3 dưới đây) — đây là concept **mới**, chưa có trong Valence.md
- ❌ **User's compound hypothesis** "chunk ↔ agent + chunk ↔ useful schema → positive valence toward agent" — formulation này chưa formalize trong Valence.md

### §11.2 — Thread 11 rename

**Old**: `07-Thien-Cam-Mechanism.md`
- Vietnamese-specific term
- Narrow scope (chỉ positive, chỉ agent)
- Không dùng framework's existing stable term

**New**: `07-Chunk-Valence.md`
- Dùng framework term **valence** (đã stable trong Valence.md)
- Covers positive + negative + neutral + mixed
- Covers object + agent + abstract
- Chunk-layer scope (extension, not rewrite)

**Rationale**:

> **"Thiện cảm" chỉ là điểm neo ban đầu để phát hiện ra suy nghĩ tích cực của con người** (user verbatim, Phase 2.5 feedback)
>
> → Thread 11 thực ra là về valence assignment tại chunk layer, với "thiện cảm" chỉ là 1 sub-case (positive valence toward agent).

**File proposal §7.1 updated**:

| # | File | Thread |
|---|---|---|
| 07 | ~~Thien-Cam-Mechanism.md~~ → **`07-Chunk-Valence.md`** | 11 |

**Global parameter stabilized**: **valence** (positive / negative / neutral / mixed × per channel × per context). Consistent usage across `Domain/Valence.md` + `Chunk-Analysis/07-Chunk-Valence.md` + any future references.

### §11.3 — New hypothesis H7: Valence emerges from chunk × schema interaction

**User's key insight** (Phase 2.5 feedback):

> "có thể một chunk cùng tích cực ở schema này nhưng tiêu cực ở schema khác"

**H7 statement**:

> **Valence không phải property cố định attach trực tiếp lên chunk. Valence emerge từ tương tác chunk × schema × context**. Cùng một chunk, khác schema context → valence khác nhau.

**Examples minh họa**:

| Chunk | Schema context | Valence |
|---|---|---|
| `[nói thẳng]` | "công việc hiệu quả" | positive (clarity, efficiency) |
| `[nói thẳng]` | "quan hệ xã giao" | negative (phá hòa khí) |
| `[nói thẳng]` | "đàm phán khó" | mixed (risk + honesty) |
| `[mẹ ép học]` | "được nuôi dưỡng" | positive (đầu tư tương lai) |
| `[mẹ ép học]` | "tự chủ cá nhân" | negative (mất quyền chọn) |
| `[con dao]` | "nấu ăn" | positive (utility) |
| `[con dao]` | "tự vệ" | positive (protection) |
| `[con dao]` | "an toàn cho trẻ em" | negative (danger) |
| `[con dao]` | "vết sẹo cũ" | negative (trauma trigger) |

**Compatible với Valence.md**:

- Valence.md §1 đã commit "context-dependent" via bom example (đồng đội vs kẻ thù)
- Valence.md §2 multi-channel profile có thể hiểu = **channels activate tùy schema**
- H7 extend cụ thể hơn: **which channels activate** = function của schema context currently firing

**Mechanism candidate** (sẽ drill trong `07-Chunk-Valence.md`):

```
1. Chunk fires (PFC hold hoặc vô thức trigger)
2. Current schema context active → filter chunk's multi-channel profile
3. Chỉ các channels relevant với schema purpose được weight
4. Body integrate weighted valences → emergent chunk-in-context valence
5. Output: approach / avoid / mixed / neutral (trong schema hiện tại)
```

**Implications nếu H7 đúng**:

- **Không có "chunk positive tuyệt đối"** — luôn là "chunk positive trong schema X"
- **Valence là relational property** (chunk × schema × context), không phải intrinsic
- **Giải thích "yêu và ghét cùng lúc"**: cùng chunk, 2+ schemas cùng active, conflicting valences
- **Foundation cho compound hypothesis**: user's "chunk ↔ agent + chunk ↔ useful schema → thiện cảm" = **2 schema contexts cùng active** (agent schema + self-benefit schema), cả 2 cho positive → compound positive
- **Foundation cho hatred mechanism**: agent schema + threat schema cùng active → compound negative
- **Foundation cho mixed feelings**: nutrition schema positive + autonomy schema negative → mixed toward mẹ
- **Link với Chunk.md §2 shared chunks**: chunk shared giữa schemas không chỉ triggers cross-fire mà còn **inherits conflicting valences** từ multi-schema membership

**Status**: Plausible, consistent với Valence.md's existing framing. Drill `07-Chunk-Valence.md` sẽ formalize + test mechanism.

**Note về architectural tension**: H7 có thể đòi hỏi refinement của Valence.md §1 "Stored in schema" statement. Valence.md hiện nói "valence stored in schema" (singular), H7 nói "chunk có multiple valence profiles tùy schema hosting". Có thể compatible nếu Valence.md "schema" = compound schema context. Sẽ clarify trong drill.

### §11.4 — Updated thread 11 coverage

| Metric | Before (§4.1) | After (§11) |
|---|---|---|
| Coverage | 40% (Feeling Theme E + Object-Agent + Connection virtual chunks) | **~80%** (Valence.md direct foundation) |
| Priority | MEDIUM | **LOW-MEDIUM** (focus on 4 specific gaps) |
| Gap type | Multiple — needed concept building | Focused — aesthetic + disgust + chunk-layer framing + H7 |

**Drill scope updated** cho `07-Chunk-Valence.md`:

1. **§1 Chunk-level framing** — Valence attaches tại chunk layer. Relationship chunk ↔ entity ↔ valence profile.
2. **§2 H7 chunk × schema interaction** — mechanism cho valence emerging từ context
3. **§3 Aesthetic valence** — hoàng hôn đẹp, cục đá đẹp. Pattern resonance? L3 experience channel extended?
4. **§4 Disgust mechanism** — gián, nhà bừa bộn. Evolutionary disease avoidance (Curtis, Rozin). Khác với fear/threat.
5. **§5 Trauma-derived negative valence** — chó cắn hồi nhỏ. Flashbulb (Brown & Kulik 1977) + extinction failure.
6. **§6 User's compound hypothesis** — "chunk ↔ agent + chunk ↔ useful schema → positive" decomposed: compound schema context activation.
7. **§7 Mixed valence cases** — yêu và ghét cùng lúc. Multi-schema concurrent activation.
8. **§8 Positive-Negative gradient** — 1 trục liên tục hay 2 hệ thống riêng? Neutral state nghĩa gì?
9. **§9 Cross-refs** — Feeling Theme E, Valence.md, Object-Agent §5, Chunk.md §2, Schema.md §2 shared chunks.
10. **§10 Framework update recommendations** — what to update in Valence.md based on drill findings.

### §11.5 — Questions added cho §6 (Q22-Q26)

**§11.5.1 Chunk vs entity framing**

**Q22**. Framework hiện tại dùng "entity" trong Valence.md, "chunk" trong Chunk.md. Cùng một thứ hay khác? Khi nào valence attach to entity, khi nào attach to chunk?

**Candidate answer**: Entity = external thing in world. Chunk = internal representation of entity in brain. Valence luôn attach to chunk (internal representation) — Valence.md's "entity" là shorthand cho "chunk representing that entity". Sẽ clarify trong drill.

**§11.5.2 Chunk × schema mechanism**

**Q23**. H7 mechanism: schema filter chunk channels — chi tiết operation thế nào? Ở level neurons, cái gì làm filtering?

**Candidate answer**: Schema active → certain neural ensembles are pre-activated → spreading activation từ chunk goes through pre-activated paths → channels tied to active schema fire stronger, channels tied to inactive schemas fire weaker. = Hebbian + context priming.

**§11.5.3 Aesthetic valence channel**

**Q24**. Aesthetic valence ("đẹp") — có channel riêng không, hay là emergent từ existing channels (L3 novelty + L2 experience + pattern resonance)?

**Candidate answer**: Không cần channel riêng. Aesthetic = pattern resonance firing L3 novelty (new pattern found) + L3 coherence (pattern fits) + L2 experience (processing pleasant). Valence.md §2 Profile có thể extend với "aesthetic sub-channel" hoặc map vào existing.

**§11.5.4 Disgust tách biệt với fear**

**Q25**. Disgust mechanism — là threat schema thông thường (L0 safety negative) hay hệ thống tách biệt?

**Candidate answer**: Tách biệt, evolutionary. Research: disgust có expression đặc thù (wrinkled nose, gag reflex), neural correlates khác fear (anterior insula vs amygdala), developmental timeline khác (disgust develops later ~4yo), moral disgust extension (Rozin et al.). Sẽ cite research trong drill.

**§11.5.5 Compound operation level**

**Q26**. User's compound hypothesis "chunk ↔ agent + chunk ↔ useful schema → positive valence" — mechanism operate at chunk layer hay schema layer?

**Candidate answer**: Schema layer qua H7. 2 schemas active cùng lúc (agent-tracking schema + self-benefit schema), cả 2 share chunk "this agent", cả 2 assign positive valence → compound → experienced as thiện cảm. Drill sẽ formalize.

### §11.6 — Architectural note cho 99-Synthesis

H7 nếu validated có implication architectural: **Valence.md có thể cần refactor** để explicit về "valence = chunk × schema interaction" thay vì "valence stored in schema" (current wording).

Drill recommendation sẽ include:
- Rename? Restructure? Add section?
- Update Valence.md §1 với H7
- Add "Chunk-Valence Interaction" section
- Update Valence.md §2 Profile framing

**Status**: Defer tới 99-Synthesis phase. Don't commit now.

---

## §12 — Final Status + Next Step (after Phase 2.5)

### §12.1 — Phase 1-2.5 status

✅ Phase 1: Discovery complete — 8 files read (7 Phase 1 + Valence.md Phase 2.5)
✅ Phase 2: 00-Reading-Notes.md written
✅ Phase 2.5: §11 refinements added based on user feedback

### §12.2 — Next step

**Phase 3**: Write `plan.md` (master) — incorporates all findings + H1-H7 hypotheses + 11 threads with file proposals + 3 drill phases + success criteria.

**Phase 4**: Write `Grammar-Scaffolding/plan.md` (sub-plan) — smaller scope, focused on thread 6 drill path.

**Phase 5**: Stop for user review before any drill implementation.

### §12.3 — Coverage summary (final)

| Priority | Count | Threads |
|---|---|---|
| HIGH gap | 4 | 2, 3, 6, 7, 8 (thread 3 still HIGH) |
| MEDIUM gap | 5 | 1, 4, 5, 9, 10 |
| LOW-MEDIUM | 1 | **11** (downgraded via Valence.md discovery) |

**Total drill estimate**: Slightly smaller than before vì thread 11 scope tighter. ~6500-8500 lines. 2-4 sessions.

### §12.4 — Hypotheses list (final)

| # | Hypothesis | Status |
|---|---|---|
| H1 | Chunk as substrate (not Schema sub-concept) | Pending 99-Synthesis |
| H2 | Thread 2 = 4th type of chunk connection (static logical linking) | Pending drill 03 |
| H3 | Grammar-scaffolding partial-embedded (Modality §2.0) | Strong support, pending formalization |
| H4 | Trừu tượng vs siêu hình = modality encoding difference | Plausible, pending drill 08 |
| H5 | Lờ mờ = multi-weak-signal convergence | Candidate, pending drill 10 |
| H6 | Chunk decay without anchor follows Ebbinghaus | Hypothesis, pending drill 05 |
| **H7** | **Valence emerges from chunk × schema interaction** (added Phase 2.5) | Consistent with Valence.md, pending drill 07 |

---

---

## §13 — Phase 5.5 update: Thread 12 added (Learning Dissonance Cycle)

> Added after Phase 5 user feedback. Captures: thread 12 origin, H8 hypothesis, Learning-Cycle sub-folder proposal, sleep multi-function research findings.

### §13.1 — Thread 12 origin

User raised in Phase 5.5: phenomenon of fatigue + mild dissonance khi tạo chunk mới hoặc kết nối 2 chunks mới — even when reward is present (sướng). Cycle resolves via sleep, eventually leading to baseline shift ("bình thường mới").

User's verbatim mechanism draft:

> "khi 2 chunk liên kết với nhau thì trước tiên chúng sẽ draft liên kết với nhau (tạm bằng bất kỳ nhánh noron nào có thể đang sẵn), rồi sau khi liên kết sẽ fire pattern coherence và vô thức check thấy pattern này solve được schema nào đó, thế là trả reward. nhưng pattern draft thì chưa chạy mượt lắm trên hardware, hoặc chưa nhất thiết phải mượt toàn bộ melody với các schema khác (nhìn theo melody lens), vậy thì nghỉ giải lao hoặc đi ngủ, và sau giấc ngủ, các pattern vẫn fire với nhau, liên kết được cắt tỉa và tạo kết nối tinh tế hơn, mượt mà đồng bộ giữa tất cả các schema hơn (mà vẫn giữ được kết nối giữa 2 chunk), vậy là sáng hôm sau thấy thoải mái hơn (ít mệt, ít dissonance khó chịu nhẹ hơn), và cũng thấy sướng rõ ràng hơn, cho tới khi melody shift hoàn toàn lên baseline mới và thấy trạng thái đó rất bình thường (bình thường mới)"

### §13.2 — Sleep multi-function research findings

User's deep follow-up question: "liệu ngủ chỉ đơn giản là cắt tỉa làm mượt liên kết, hay là vẫn có sự tái hiện toàn bộ context giả lập"

**Answer**: Sleep is **multi-functional**. At least 6 distinct mechanisms identified by research:

| # | Mechanism | Research | Function |
|---|---|---|---|
| 1 | Synaptic homeostasis (SHY) | 🟢 Tononi & Cirelli 2014 | Global synaptic downscaling — preserves signal-to-noise |
| 2 | Hippocampal replay | 🟢 Wilson & McNaughton 1994, O'Neill 2010 | Replay day's sequences 10-20x speed via sharp-wave ripples |
| 3 | Active systems consolidation | 🟢 Born & Wilhelm 2012 | New memories integrate with existing schemas (SWS) |
| 4 | REM creative linking | 🟢 Cai 2009, Wagner 2004 | Remote associates via REM, → aha next morning |
| 5 | Emotional decoupling | 🟢 Walker 2017 | REM reduces emotional charge, keeps content |
| 6 | Pattern extraction / gist | 🟢 Ji & Wilson 2007, Payne 2009 | Extract gist, lose surface details |
| 7 | Dreaming as simulation | 🟡 Revonsuo 2000, Hobson | Threat scenario rehearsal (debated) |

**User's intuition validated**: "tái hiện toàn bộ context giả lập + cắt tỉa + kết nối mới hạn chế + đảm bảo đồng bộ schemas" = research-confirmed combination of mechanisms 2 (replay), 1 (downscale), 4 (REM linking), 3 (integration). User's intuition covers ~70% of established research.

### §13.3 — H8 hypothesis added

> **H8 — Learning Dissonance Cycle**: Chunk formation + connection incur **concurrent reward + fatigue + mild dissonance**. Resolution via sleep-mediated **multi-mechanism consolidation** (homeostasis + replay + integration + creative linking + emotional decoupling + gist extraction), iterated until baseline shift. Cost scales with **novelty × integration distance × existing schema complexity**.

### §13.4 — Thread 12 sub-questions

- 12.1 Tại sao learning NEW chunks/connections tốn effort dù solve schema (rewarding)?
- 12.2 Sướng + mệt + dissonance đồng thời — 3 signals từ đâu, conflicting hay parallel?
- 12.3 Draft pattern "chưa smooth on hardware" — cơ chế cụ thể? (synaptic efficiency? myelination? network noise?)
- 12.4 Melody integration cost (schemas khác phải sync) — cơ chế?
- 12.5 Role của sleep vs waking rest — khác nhau thế nào?
- 12.6 Synaptic pruning during sleep — mất chunks nào, giữ chunks nào?
- 12.7 Cycle iteration count — sao một số thứ cần 1 đêm, một số cần nhiều tuần?
- 12.8 Baseline shift ("bình thường mới") — mechanism cho adaptation?
- 12.9 Exhaustion threshold — khi nào "mệt quá" stop productive learning?
- 12.10 Age effects — trẻ học dễ hơn người lớn — relate to cycle cost?
- 12.11 Expert vs beginner — reduced cycle cost or faster cycle?
- 12.12 Individual variation — sao một số người exhaust fast, một số chịu được long sessions?
- 12.13 Flow state vs struggle state — 2 modes khác nhau trong cycle?
- 12.14 Framework evolution case — user's own observation building framework

### §13.5 — Sub-folder Learning-Cycle/ proposal

**Scope assessment** (parallel với Grammar-Scaffolding analysis):

20 potential topics in full Learning-Cycle coverage:
1. Cycle core mechanism
2. Sleep consolidation multi-function (6 mechanisms)
3. Hippocampal replay detail
4. NREM vs REM functions
5. Synaptic homeostasis (SHY)
6. Active systems consolidation
7. Dreaming theories
8. Incubation + aha
9. Desirable difficulty + deliberate practice
10. Cognitive load theory
11. Flow vs struggle states
12. Exhaustion + burnout
13. Hedonic adaptation / baseline shift
14. Age effects on cycle
15. Developmental sleep
16. Meditation as alternative rest
17. DMN activity
18. Framework evolution case
19. Trauma processing (failed decoupling)
20. Creativity and sleep historical anecdotes

→ **Folder warranted** (20 topics > 1 file capacity), parallel with Grammar-Scaffolding decision.

**Folder name**: `Learning-Cycle/` (short, captures cyclical nature, sleep is sub-mechanism)

**Folder structure (Phase 5.5)**:
```
Chunk-Analysis/Learning-Cycle/
├── plan.md                              (sub-plan, parallel với Grammar-Scaffolding/plan.md)
└── (future expansion placeholders, not created now:)
    ├── Learning-Cycle.md                (core: cycle mechanism + sleep multi-function)
    ├── Sleep-Multi-Function.md          (deep dive 6 mechanisms)
    ├── Flow-vs-Struggle.md              (2 modes in cycle)
    ├── Baseline-Shift-Hedonic.md        (hedonic adaptation)
    └── Framework-Evolution-Case.md      (meta case study)
```

### §13.6 — Updated thread + hypothesis counts

| Metric | Phase 5 | Phase 5.5 |
|---|---|---|
| Threads | 11 | **12** |
| Hypotheses | 7 (H1-H7) | **8** (H1-H8) |
| Analysis files | 10 + Grammar-Scaffolding sub | **10 + Grammar-Scaffolding sub + Learning-Cycle sub** |
| Open questions | 26 (Q1-Q26) | **40** (Q1-Q26 + Q12.1-Q12.14) |
| Sub-folders | 1 (Grammar-Scaffolding) | **2 (+ Learning-Cycle)** |
| Drill estimate | 8200-11100 lines | **9500-12500 lines** |
| Sessions estimate | 3-5 | **4-6** |

### §13.7 — Drill order updated cho Phase C

```
Phase C — Compound + Meta:
07-Chunk-Valence
→ 08-Abstract-Metaphysical
→ Learning-Cycle/Learning-Cycle  ← NEW (between 08 và 09 — micro mechanism for upgrade)
→ 09-Cognition-Upgrade  (now builds on Learning-Cycle)
→ 10-Right-Wrong-Vague
→ 99-Synthesis
```

**Rationale cho position**: Learning-Cycle là **micro-mechanism** beneath upgrade. 09 Cognition-Upgrade là macro view (long-term cognitive development), Learning-Cycle là micro view (short-term learning cycle). Drill micro trước, then macro builds on top.

### §13.8 — Updated hypotheses list

| # | Hypothesis | Test file | Status |
|---|---|---|---|
| H1 | Chunk substrate cross-cutting | 99-Synthesis | Pending |
| H2 | Thread 2 = 4th chunk connection (static logical) | 03-Chunk-Connection-Logical | Pending |
| H3 | Grammar-scaffolding partial-embedded | Grammar-Scaffolding/Grammar-Scaffolding | Strong support |
| H4 | Trừu tượng vs siêu hình = modality difference | 08-Abstract-Metaphysical | Plausible |
| H5 | Lờ mờ = multi-weak-signal convergence | 10-Right-Wrong-Vague | Candidate |
| H6 | Decay without anchor follows Ebbinghaus | 05-Chunk-Chain-Anchor-Decay | Hypothesis |
| H7 | Valence = chunk × schema interaction | 07-Chunk-Valence | Consistent with Valence.md |
| **H8** | **Learning Dissonance Cycle (multi-mechanism consolidation, baseline shift)** | **Learning-Cycle/Learning-Cycle** | **Strong research base, mechanism mostly drafted** |

---

## §14 — Final status (after Phase 5.5)

### §14.1 — Phase 1-5.5 summary

✅ Phase 1: Discovery reading (8 files)
✅ Phase 2: 00-Reading-Notes.md written
✅ Phase 2.5: Valence.md discovery + thread 11 rename + H7
✅ Phase 3: Master plan.md written
✅ Phase 4: Grammar-Scaffolding/plan.md written
✅ Phase 5: First user review report
🔄 Phase 5.5: Thread 12 + H8 + Learning-Cycle sub-folder integration (in progress)

### §14.2 — Updated coverage

| Priority | Threads |
|---|---|
| HIGH gap | 2, 3, 6, 7, 8, **12** (6 threads) |
| MEDIUM | 1, 4, 5, 9, 10 (5 threads) |
| LOW-MEDIUM | 11 (1 thread) |

Thread 12 is **HIGH priority** because:
- Foundational for cognition (sleep is biological investment of 1/3 lifespan)
- Cross-cuts every chunk lifetime
- Strong research base (well-established)
- Framework gap is large (scattered, not unified)
- User's mechanism is already 70% complete

---

> **00-Reading-Notes.md — End of file (after §13 + §14).**
>
> Reading pass + Phase 2.5 + Phase 5.5 refinements complete. 8 files read, **8 hypotheses** listed, **40 open questions** captured, **10 analysis files + 2 sub-folders** + 1 synthesis proposed. Ready for plan.md §14 update + Learning-Cycle/plan.md creation.
