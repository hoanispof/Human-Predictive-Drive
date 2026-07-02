# Plan: Domain Interaction Restructure

> **Trạng thái:** IN PROGRESS — 3/5 files done, 2 remaining
> **Ngày:** 2026-04-12
> **Mục đích:** Restructure phần Domain Interaction trong framework.
> Thêm Object-Agent, Logic-Modeling, Valence, Emergent Patterns vào core.
> Redefine Empathy và Connection trong bức tranh mới.
> **Nguồn gốc:** 2 sessions phân tích sâu (2026-04-12):
>   Session 1: Object-Agent, Logic-Modeling, Mirror analysis
>   Session 2: Valence, Empathy cases, Connection cases, Domain Interaction synthesis
> **Nguyên tắc:** Chậm mà chắc. Mỗi file = chất lượng core. 2 triệu năm tiến hóa, vài tiếng thêm là xứng đáng.

---

## 1. TẠI SAO CẦN RESTRUCTURE

### Phát hiện chính qua 2 sessions:

1. **Object-Agent** = 2 classification modes cơ bản của não (Spelke 2007, VTC eLife 2019)
   → Mọi entity trong domain đều bị classify: Object hoặc Agent
   → Hardware-level binary (VTC), nhưng schema CAN override

2. **Logic-Modeling** = 2 processing modes (framework framing, gần Kahneman dual-process)
   → Logic = rules-based, anchor. Modeling = simulation-based, explore
   → 2 cặp INDEPENDENT: Object-Agent × Logic-Modeling = 2×2 matrix

3. **Valence** = cách body đánh giá MỌI entity trong domain
   → Multi-channel (L0-L3 impact), dynamic, stored in schema
   → Object valence (đơn giản) vs Agent valence (phức tạp, reciprocal)

4. **Empathy = KHÔNG phải mechanism riêng biệt**
   → Empathy = CÁCH agent processing hoạt động
   → Mirror = mechanism agent processing DÙNG để đọc state
   → Không cần system tách rời — là một phần của domain interaction

5. **Connection = KHÔNG phải channel/layer riêng**
   → Connection = emergent PATTERN từ sustained positive agent interaction
   → Nhưng AGENT INPUT = body-base need THẬT (Social Baseline Theory, Coan)
   → Body-base need (mere presence, calibration) + compiled meta-drive (specific bonds)

6. **Agent input = body-base need** (evidence 🟢):
   → Social Baseline Theory: não DEFAULT giả định có agent gần
   → Mere Presence Effect: chỉ có agent gần → brain auto-recalibrate
   → Romanian orphans: thiếu sustained agent input → brain DAMAGE
   → Solitary confinement: crash trong NGÀY dù L1 met
   → Agent input spectrum: mere presence → observation → light interaction → deep bond

7. **"Cho đi" không vô tư tuyệt đối**
   → Mọi case đều có body-base reward (mirror + status + connection)
   → Drive cho đi DỪNG khi schema gốc bị vi phạm hoặc body-base thiếu

8. **Smooth melody ≠ mục tiêu. Domain mapping chính xác = mục tiêu**
   → Gương = smooth nhưng zero domain expansion → chán
   → Agent = unpredictable, rich input → best domain mapping tool

### Hệ quả: framework cần THÊM tầng Domain Interaction

Hiện tại framework mô tả:
- Body-Base (L0-L3) → tốt
- Schema system → tốt
- Imagine-Final → tốt
- Cortisol-Baseline → tốt

THIẾU: cách con người TƯƠNG TÁC VỚI DOMAIN (giữa body-base needs và action)

---

## 2. FILE PLAN — TẠO MỚI, BACKUP, GIỮ NGUYÊN

### 2.1 FILES TẠO MỚI (trong Domain/)

```
Core-Deep-Dive/Domain/
├── Domain-Interaction.md     ← [1] Overview toàn bộ hệ thống
├── Object-Agent.md           ← [2] Classification modes
├── Valence.md                ← [3] Cách body đánh giá entities
├── Emergent-Patterns.md      ← [4] Connection, Enemy, Nurturing,...
└── Domain-Mechanisms.md      ← [5] Mirror + mechanisms phục vụ DI
```

### 2.2 FILES BACKUP (chuyển vào backup/)

```
Core-Deep-Dive/backup/
├── Empathy-Mirror.md         ← Concepts absorbed vào Domain-Mechanisms + Emergent-Patterns
└── Connection.md             ← Concepts absorbed vào Emergent-Patterns
```

Lý do backup (KHÔNG xóa):
- Content vẫn có giá trị reference
- Nhiều file khác cross-ref tới chúng
- Có thể cần quay lại verify

### 2.3 FILES GIỮ NGUYÊN (có thể update cross-ref sau)

```
Core-Deep-Dive/
├── Logic-Modeling.md          ← GIỮ ở vị trí hiện tại, cross-ref từ Domain-Interaction
├── Drive/Drive.md             ← GIỮ — Drive = HOW drives combine → action. Khác Valence
├── Drive/Novelty.md           ← GIỮ
├── Drive/Threat.md            ← GIỮ
├── Cortisol-Baseline.md       ← GIỮ
├── Imagination/               ← GIỮ
├── Schema/                    ← GIỮ
├── Body-Base/                 ← GIỮ (có thể cần update nhỏ: agent input need)
└── Mirror-Empathy-Connection-Other/  ← GIỮ (research notes, analysis drafts)
```

### 2.4 FILES CẦN UPDATE NHỎ (sau khi tạo xong files mới)

- **Core-v7.5-Draft.md**: update §3.5 Empathy-Mirror section, thêm Domain Interaction reference
- **Logic-Modeling.md**: thêm cross-ref tới Domain-Interaction.md, Object-Agent.md
- **Body-Base files**: có thể cần thêm "agent input" vào L2 hoặc vị trí phù hợp

---

## 3. THỨ TỰ TRIỂN KHAI (nền trước, chi tiết sau)

### Phase 1: Domain-Interaction.md (NỀN — phải có trước)
- Scope: Overview toàn bộ Domain Interaction system
- Bao gồm: Flow Body→Classification→Processing→Valence→Drive→Action→Feedback
- Map nhanh sang 4 file chi tiết còn lại
- Cross-ref: Logic-Modeling.md, Drive.md, Body-Base
- Mức: DRAFT v0.5 — đủ để các file khác reference
- Ước lượng: quan trọng nhất, cần kỹ nhất

### Phase 2: Object-Agent.md (CLASSIFICATION — nền thứ 2)
- Scope: 2 classification modes chi tiết
- Bao gồm: Spelke evidence, VTC, schema override, developmental timeline,
  Object↔Agent flip examples, 2×2 matrix reference
- Cross-ref: Domain-Interaction.md, Logic-Modeling.md, Valence.md
- Mức: DRAFT v0.5
- Ước lượng: nhiều evidence có sẵn từ Mirror-Neuron-Analysis.md

### Phase 3: Valence.md (EVALUATION — nền thứ 3)
- Scope: Cách body đánh giá entities trong domain
- KHÔNG thay thế Drive.md — bổ sung mảnh còn thiếu
- Bao gồm: Valence profile (multi-channel), Object vs Agent valence,
  Valence update mechanism, Trust/Predictability/Replaceability,
  Cases phân tích (dao, mẹ, bạn B, Thiên Chúa, bụi cây VC)
- Cross-ref: Domain-Interaction.md, Object-Agent.md, Drive.md, Body-Base
- Mức: DRAFT v0.5
- Ước lượng: concept mới trong framework, cần cẩn thận

### Phase 4: Emergent-Patterns.md (PATTERNS — build trên 3 file trên)
- Scope: Các patterns emerge từ domain interaction
- Bao gồm:
  - Connection pattern: body-base need (agent input) + compiled meta-drive
    Agent input spectrum (Level 0-4), Virtual chunks, Calibration, Dunbar
    (absorb content từ Connection.md cũ, reframe)
  - Enemy/Threat pattern: sustained negative valence
  - Nurturing pattern: giving + vulnerability amplification
    (absorb content từ Empathy-Mirror.md §6, reframe)
  - "Cho đi" pattern: surplus + mirror reward (§6.5 Empathy-Mirror.md)
  - Dependency pattern: high positive + irreplaceable
  - Mixed valence: Love+Hate (mẹ case)
  - Group dynamics: amplification, replacement
  - Violation & recovery: khi pattern bị phá
- Cross-ref: Domain-Interaction.md, Valence.md, Connection.md (backup ref)
- Mức: DRAFT v0.5
- Ước lượng: file LỚN NHẤT — absorb 2 files cũ + nhiều cases mới

### Phase 5: Domain-Mechanisms.md (MECHANISMS — hỗ trợ)
- Scope: Các mechanisms phục vụ domain interaction
- Bao gồm:
  - Mirror mechanism: agent processing's state-reading
    3 mechanisms (pattern matching → agent modeling → schema simulation)
    (absorb core concepts từ Empathy-Mirror.md §1-§3 + Mirror-Neuron-Analysis.md)
  - Imagine-Final trong domain interaction context
  - Schema trong domain interaction context
  - Feedback loop: Body receives → update valence → loop
- Cross-ref: Domain-Interaction.md, Empathy-Mirror.md (backup ref),
  Mirror-Neuron-Analysis.md, Imagine-Final.md
- Mức: DRAFT v0.5
- Ước lượng: tổng hợp nhiều file, cần kỹ

### Phase 6: Backup + Cross-reference update
- Chuyển Empathy-Mirror.md → backup/
- Chuyển Connection.md → backup/
- Update cross-refs trong các file còn lại
- Update Core-v7.5-Draft.md nếu cần
- Update memory file

---

## 4. NGUYÊN TẮC VIẾT MỖI FILE

### Chất lượng:
- Mỗi file = framework-quality, KHÔNG phải notes
- Follow conventions: 🟢 Research | 🟡 Framework reasoning | 🔴 Hypothesis
- Có §0 Position in framework (vị trí trong kiến trúc)
- Có Honest Assessment (cái gì chưa chắc, cái gì cần verify thêm)
- Có Cross-references (link rõ ràng tới files liên quan)

### Phong cách:
- Giống format Logic-Modeling.md (đã được approve chất lượng)
- Code blocks cho diagrams và structured content
- Cases/ví dụ thực tế minh họa mỗi concept
- Không quá dài — đủ sâu nhưng focused

### Verify:
- Mỗi claim có confidence level (🟢/🟡/🔴)
- Cross-check với evidence đã thu thập qua 2 sessions
- Không sáng tạo thêm concepts — chỉ organize và clarify cái đã phân tích

---

## 5. DEPENDENCIES GIỮA CÁC FILES

```
Domain-Interaction.md (overview)
    ├── Object-Agent.md (classification)
    │       └── references Logic-Modeling.md (processing)
    ├── Valence.md (evaluation)
    │       └── references Object-Agent.md + Body-Base + Drive.md
    ├── Emergent-Patterns.md (patterns)
    │       └── references Valence.md + Object-Agent.md + Body-Base
    └── Domain-Mechanisms.md (mechanisms)
            └── references Object-Agent.md + Valence.md + Imagination/ + Schema/
```

→ Phải viết THEO THỨ TỰ: 1→2→3→4→5 (file sau reference file trước)

---

## 6. RISK & MITIGATION

| Risk | Mitigation |
|------|-----------|
| Files mới conflict với files cũ chưa update | Backup cũ, update cross-ref ở Phase 6 |
| Concepts bị duplicate giữa files mới | Mỗi file có scope RÕ, overlap → cross-ref |
| Quality giảm vì viết nhiều files liền | 1 file/phase, verify trước khi sang file tiếp |
| Connection.md content bị mất | Backup giữ nguyên, absorb key concepts vào Emergent-Patterns |
| Core-v7.5 bị outdated | Update NHỎ ở Phase 6, không refactor Core lớn lần này |

---

## 7. THÀNH CÔNG = GÌ?

Sau khi hoàn thành tất cả phases:

1. ✅ Có bộ 5 files Domain Interaction chất lượng core
2. ✅ Empathy được redefine: CÁCH agent processing hoạt động (không phải system riêng)
3. ✅ Connection được redefine: emergent pattern + body-base agent input need
4. ✅ Object-Agent, Valence = concepts MỚI integrated vào framework
5. ✅ Mọi file cross-ref chặt chẽ, không conflict
6. ✅ Files cũ backup an toàn, content không mất
7. ✅ Framework có thể giải thích: tình yêu, ghét, cho đi, sợ hãi, nhóm bạn,
   bụi cây Việt Cộng, Mother Teresa, người ăn xin, mẹ ép học,...
   = TẤT CẢ từ CÙNG 1 bộ cơ chế (Object-Agent × Logic-Modeling × Valence × Body-Base)

---

## 8. SESSION TRACKING

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Domain-Interaction.md | ✅ Done | v0.5 DRAFT — overview complete |
| Phase 2: Object-Agent.md | ✅ Done | v0.5 DRAFT — classification + evidence + dev timeline + override |
| Phase 3: Valence.md | ✅ Done | v0.5 DRAFT — multi-channel valence + 7 cases + dynamics |
| Phase 4: Emergent-Patterns.md | ✅ Done | v0.5 DRAFT — 11 sections, §0-§11, absorb Connection.md + Empathy-Mirror.md §6-§8.5 |
| Phase 5: Domain-Mechanisms.md | ⬜ Pending | Xem REFINED outline §10 bên dưới |
| Phase 6: Backup + Cross-ref | ⬜ Pending | Cuối cùng |

---

## 9. OUTLINE: Emergent-Patterns.md (Phase 4 — FILE LỚN NHẤT)

> File này ABSORB content từ Connection.md + Empathy-Mirror.md
> Cần viết kỹ nhất — là nơi empathy/connection được REDEFINE trong framework

### Cấu trúc đề xuất:

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  Bước sau Valence: khi domain interaction LẶP LẠI → patterns EMERGE
  Patterns = COMPILED valence relationships, stored in schema

§1 — EMERGENT PATTERNS LÀ GÌ
  Define: KHÔNG pre-designed, EMERGE từ repeated interaction
  Không có module "connection" hay "enemy" riêng
  = Kết quả tự nhiên của Valence × Time × Context

§2 — CONNECTION PATTERN (section LỚN NHẤT)
  ├── 2.1 Agent Input = Body-Base Need (PHÁT HIỆN MỚI)
  │   → Social Baseline Theory (Coan) — brain defaults to social
  │   → Mere Presence Effect — passive recalibration
  │   → Romanian orphans — agent deprivation = brain damage
  │   → Solitary confinement — crash trong ngày
  │   → Harlow — touch/presence ≠ food
  │   → Agent input spectrum 5 levels (mere presence → deep bond)
  │
  ├── 2.2 Connection = Sustained Mutual Positive Valence
  │   → Define: 2 agents, positive valence multi-channel, sustained
  │   → Absorb Connection.md §1-§2: emergent giữa melodies, force multiplier
  │
  ├── 2.3 Virtual Chunks — dùng chunks người khác
  │   → Absorb Connection.md §3
  │   → Case nhóm bạn: A learning chunks, C strength chunks
  │   → Trust = bandwidth cho virtual chunks
  │
  ├── 2.4 Melody Calibration — 2 melodies tune nhau
  │   → Absorb Connection.md §4
  │   → Error correction, convergence, dual check, complementary
  │   → Case: ngại nói chuyện → chơi bạn hay nói → tự bon mồm
  │
  ├── 2.5 Co-regulation
  │   → Absorb Empathy-Mirror.md §7
  │   → Presence = channel riêng
  │   → Social buffering
  │
  ├── 2.6 Dunbar Limits
  │   → Absorb Connection.md §5
  │   → 5/15/50/150 — time × attention = bottleneck
  │
  └── 2.7 Distance Spectrum
      → Absorb Connection.md §6
      → Gặp trực tiếp > video > voice > text > ảnh > nhớ

§3 — ENEMY / THREAT PATTERN
  → Sustained NEGATIVE valence (agent hoặc object)
  → Cases: kẻ thu thuế, chuột, gián, kẻ thù chiến tuyến
  → Bẫy gai, bom = object mang ý đồ agent
  → Bụi cây Việt Cộng = object reclassify thành potential agent
  → Dehumanization = agent→object flip cho phép tiêu diệt

§4 — NURTURING PATTERN
  → Absorb Empathy-Mirror.md §6
  → = "Cho đi" + vulnerability AMPLIFICATION
  → Mirror × vulnerability cues × perceived ability × existing channels
  → 10 tình huống verify (mẹ chăm con, người lớn thấy baby, mẹ VN chăm bộ đội,...)
  → Nurturing = EMERGENT, không phải channel mới

§5 — "CHO ĐI" PATTERN
  → Absorb Empathy-Mirror.md §6.5
  → Body-Satisfaction + surplus + mirror reward > keep reward
  → KHÔNG vô tư tuyệt đối — luôn có body-base reward
  → 4 nguồn: mirror reward + status + connection + costly signal
  → Violation tests: khi nào "cho đi" DỪNG?
  → Cases: kẹo, mẹ VN chăm bộ đội, Mother Teresa, từ thiện, người ăn xin, share đồ

§6 — DEPENDENCY PATTERN
  → High positive valence + LOW replaceability
  → Không cắt được dù mixed valence (mẹ case)
  → Bạn B CẮT ĐƯỢC vì: low dependency + easy replace
  → Mẹ KHÔNG cắt vì: critical dependency + impossible replace
  → Withdrawal: mất dependency = melody crash

§7 — MIXED VALENCE (YÊU + GHÉT)
  → Multi-channel: positive channels + negative channels CÙNG LÚC
  → Mẹ: L1++ + autonomy-- = yêu VÀ ghét
  → Công việc: lương++ + stress-- 
  → BÌNH THƯỜNG cho agent phức tạp — không phải bất thường

§8 — GROUP DYNAMICS
  → Multi-agent amplification: novelty × mirror = reward amplified
  → Cases: đá bóng cùng, bàn tán cô giáo áo chấm đỏ, nhìn bạn nữ xinh
  → Virtual chunks pooling: mỗi người giỏi 1 thứ → nhóm giỏi tất cả
  → Replacement: agent trong nhóm CÓ THỂ thay thế (bạn khác cũng có chunks)
  → Nhóm tan khi: nhu cầu thay đổi, dissonance cá nhân, nhóm khác vui hơn

§9 — VIOLATION & RECOVERY
  → Khi pattern bị PHÁ
  → Investment × violation = impact
  → 3 responses: recalibrate (healthy) / overgeneralize (common) / collapse (deep)
  → Cases: tình yêu phản bội, công đức chùa + sư phạm giới, từ thiện phốt
  → Schema level quyết định impact: agent cụ thể < tổ chức < domain < worldview

§10 — HONEST ASSESSMENT

§11 — CROSS-REFERENCES
```

### Content sources cho Emergent-Patterns.md:
- **Connection.md** (backup): §1-§7 → absorb vào §2
- **Empathy-Mirror.md** (backup): §6 nurturing, §6.5 resource distribution, §7 melody sync, §8 fatigue → absorb vào §4, §5
- **Session 2 analysis**: valence cases, "cho đi" cases, violation tests → §3-§9
- **Domain-Interaction.md** §6: agent input spectrum → §2.1
- **10_Tương_tác.md**: sharing behavior reference → §5

---

## 10. REFINED OUTLINE: Domain-Mechanisms.md (Phase 5)

> Updated 2026-04-12 — refined sau khi hoàn thành Emergent-Patterns.md
> Lưu ý: nhiều content đã absorb vào EP.md → DM.md focus vào MECHANISM, không patterns

### Nguyên tắc key:
- Emergent-Patterns.md = WHAT patterns emerge (§4 đã có 4 mirror factors + cases)
- Domain-Mechanisms.md = HOW mechanisms work (chi tiết mechanism, KHÔNG duplicate cases)
- Tránh duplicate: reference EP.md cho cases/patterns, viết sâu mechanism ở đây

### Cấu trúc refined:

```
§0 — VỊ TRÍ TRONG FRAMEWORK
  Mechanisms = CÔNG CỤ phục vụ domain interaction
  Nằm NGANG với flow (Classify→Process→Evaluate→Drive→Action→Feedback)
  Hỗ trợ ở MỌI bước, cross-cutting

§1 — MIRROR: CÁCH AGENT PROCESSING HOẠT ĐỘNG (section LỚN NHẤT)

  ├── 1.1 Mirror ≠ Module riêng — là BYPRODUCT của agent processing
  │   → Object processing: rules → predict (deterministic)
  │   → Agent processing: own-state mapping → predict (non-deterministic)
  │   �� Mirror = OUTPUT của agent processing, không phải system riêng
  │   → Giả thuyết framework: gần Heyes (learned), sâu hơn
  │     (Heyes: learned through association. Framework: learned VÌ agent = phi logic)
  │   → Evidence: VTC (eLife 2019), Spelke (2007), Heyes ASL theory
  │
  ├── 1.2 Ba Mechanisms (absorb Mirror-Neuron-Analysis.md — phần QUAN TRỌNG NHẤT):
  │   ① PATTERN MATCHING (limbic, near-innate, từ sinh)
  │     → Detect acoustic/visual pattern giống experience CỦA MÌNH
  │     → "Tiếng khóc → giống khi mình khóc → body react"
  │     → = Arousal contagion, NOT empathy. Pre-mirror.
  │     → Evidence: Dondi 1999, Vreden 2025 (cross-cultural thermal imaging)
  │
  │   ② AGENT MODELING (learned, build dần 6-24m+)
  │     → Brain build prediction model cho "vật thể phi logic"
  │     → Own-state mapping: "khi MÌNH vui → muốn chơi. Khi MẸ vui → mẹ chơi"
  │       → "MẸ có state riêng, state đó GI���NG cách MÌNH có state"
  │     → TRUE empathy begins here. Mirror proper.
  │     → Evidence: Warneken 2006/2007, rouge test 18-24m, Svetlova 2010
  │
  │   ③ SCHEMA SIMULATION (compiled, không cần input thật)
  │     → Agent model compiled SÂU → body respond KHÔNG CẦN agent thật
  │     → PFC tạo virtual agent (thần, người đã mất, "giọng lương tâm")
  │     → = Post-mirror — model đã compiled, không cần mirror nữa
  │     → Evidence: Piaget animism, religious neuroscience, placebo
  │
  │   → Mainstream gọi CẢ 3 là "mirror" → confusion
  │   → Tách: ① pre-mirror ② mirror proper ③ post-mirror
  │
  ├── 1.3 Developmental Timeline (absorb MNA timeline)
  │   → 0-6m: Pattern Matching only (contagious crying, social smile)
  │   → 6-12m: Social referencing → prediction tool (not yet empathy)
  │   → 12-24m: Agent Modeling comes online (self-recognition, empathic helping)
  │   → 2-7y: Animism (overgeneralize agent model) → refine boundary
  │   → Adult: All 3 + Schema Simulation compiled deep
  │   → Cộng đồng CÓ THỂ prevent refinement → animism giữ lại (tôn giáo)
  │
  ├── 1.4 Agency Spectrum (absorb MNA — from mẹ thật → cục đá)
  │   → Mẹ thật: Agent Modeling (real-time, full channels, mirror MẠNH NHẤT)
  │   → Người lạ: Agent Modeling (species overlap ~70-90%, mirror trung bình)
  │   → Chó: Cross-species learned (30K năm co-evolution, mirror có nhưng yếu hơn)
  │   → Video call: Truncated (60-70%, thiếu touch/smell/presence)
  │   → Tượng/ảnh thiêng: Schema Simulation (100% compiled, ZERO real mirror)
  │   → Mẫu ảnh cổ: Somatic trigger → compiled schema
  │   → ⭐ Body không phân biệt source — same output, different mechanism
  │     → = Tại sao tôn giáo WORK, placebo WORK, locket WORK
  │
  ├── 1.5 Mirror → Channel Conversion (absorb Empathy-Mirror.md §3)
  │   → 5-step: detect → mirror fire → bản sao yếu → feed channels → drive hoặc không
  │   → Signal CỦA MÌNH THẬT (biochemistry thật) dù nguồn từ mirror
  │   → Anterior insula: ~10-30% intensity (Singer 2004)
  │   → Cùng 3 body signals: Satisfaction / Reward / Dissonance
  │
  ├── 1.6 2-Tier Structure (absorb Empathy-Mirror.md §2)
  │   → Tầng 1: VÔ THỨC BASE — emotional contagion, luôn chạy, mọi đ���ng vật xã hội
  │   → Tầng 2: PFC EXTENSION — interpret + simulate sâu + chọn response
  │   → Parallel Imagine-Final: base vô thức + PFC extension
  │   → Empathy Ceiling: PFC dùng own chunks → approximate, never 100%
  │   → 3 overlap layers: species > culture > personal
  │
  ├── 1.7 Mirror Strength + Perceived Ability (brief → detail ở EP.md §4)
  │   → 4 factors: living × vulnerability × expressiveness × similarity
  │   → Perceived Ability = van điều khiển
  │   → Cases + detail: Emergent-Patterns.md §4 Nurturing
  │
  └── 1.8 Empathy Fatigue + Mirror Reward Override (brief → detail ở EP.md §5)
      → Fatigue: mirror liên tục → cortisol tích lũy → body CẮT mirror (defense)
      → 3 defenses: detachment, numbness, avoidance
      → Override: mirror reward quá mạnh → mask body-base deficit
      → Spectrum healthy → compulsive: Emergent-Patterns.md §5

§2 — IMAGINE-FINAL TRONG DOMAIN INTERACTION
  → Preview outcomes TRƯỚC hành động trong domain interaction context
  → "Nếu cho kẹo → bạn vui (mirror preview) → mirror reward (preview)"
  → Imagine-Final × Mirror = powerful: simulate CHO → preview MIRROR REWARD
  → Cases: tại sao body preview gặp bạn thân → opioid → "muốn gặp"
  → Connection × Imagine-Final per layer: reference Emergent-Patterns.md §2.2
  → Reference Imagine-Final.md — không duplicate core content

§3 — SCHEMA TRONG DOMAIN INTERACTION
  → Compiled valence profiles: "bạn B = L3 positive nhẹ" (stored)
  → Compiled agent models: "mẹ đang buồn VÌ..." (simulate from compiled data)
  → Schema inheritance: cộng đồng install valence ("rắn = nguy hiểm")
  → Schema override Object↔Agent: reference Object-Agent.md §4
  → Trade-off: inheritance NHANH nhưng KÉM chính xác (Valence.md §4)
  → Reference Schema/ files — không duplicate

§4 — FEEDBACK LOOP
  → Body receives Satisfaction/Reward/Dissonance từ domain interaction
  → 3 updates: reinforcement (confirm → stronger), revision (adjust), flip (dramatic)
  → Valence update → Schema update → LOOP lại Domain Interaction
  → Cases: Bạn B (neutral → positive → negative → cắt)
  → Nested loops: micro (1 interaction), meso (relationship), macro (worldview)
  → Reference Valence.md §5

§5 — "EMPATHY" REDEFINE (section QUAN TRỌNG — kết thúc toàn bộ restructure)
  → Mainstream "empathy" = tập hợp không rõ ràng:
    affective empathy + cognitive empathy + empathic concern
  → Framework mapping:
    "Affective empathy" = mirror mechanism (§1, tầng 1 vô thức)
    "Cognitive empathy" = agent modeling + PFC extension (§1, tầng 2)
    "Empathic concern" = nurturing/cho đi pattern (EP.md §4-§5)
    "Empathy fatigue" = mirror overload → defense (§1.8)
  → KHÔNG CẦN system "empathy" riêng:
    empathy = CÁCH agent processing TỰ NHIÊN hoạt động
    mirror = BYPRODUCT của agent processing
    nurturing, cho đi = EMERGENT PATTERNS từ mirror + valence
  → Tại sao redefine: giảm confusion, thống nhất cơ chế, parsimony
  → Empathy �� AI: AI excellent ở tầng 2 (PFC simulate), THIẾU tầng 1 (body mirror)
    → = AI NÓI đúng nhưng không FEEL → presence AI ≠ presence người

§6 — HONEST ASSESSMENT
§7 — CROSS-REFERENCES
```

### Content sources cho Domain-Mechanisms.md (refined):
- **Mirror-Neuron-Analysis.md** (CHÍNH): 3 mechanisms, developmental timeline, agency spectrum,
  evidence, arguments, Object-Agent connection, Einstein parallel
- **Empathy-Mirror.md** (backup): §1 define, §2 two tiers, §3 channel conversion,
  §4 vulnerability (brief), §5 perceived ability (brief), §8 fatigue, §9 AI
- **Imagine-Final.md**: reference only (§2)
- **Schema/**: reference only (§3)
- **Valence.md §5**: reference only (§4 feedback)
- **Emergent-Patterns.md**: reference §4 (nurturing cases), §5 (spectrum) — KHÔNG duplicate

### Estimated size: Trung bình (nhỏ hơn EP.md, lớn hơn Object-Agent.md)
### Risk: §1 Mirror rất dài — có thể cần chia sub-phases nếu session sau quá lớn
