# Plan: Action-Space.md + Pattern-Resonance v4.0 Rewrite

> **Mục tiêu**: Tạo file Action-Space.md MỚI + Rewrite Pattern-Resonance v4.0.
> **Nguyên tắc**: Chậm mà chắc. Chất lượng > tốc độ. Mỗi session = 1 focus.
> **Nguồn**: Session drill 2026-05-19. Phân tích toàn diện Tool/Agent processing,
>   resonance definition, action space concept, observation axes.
> **Cập nhật**: Mỗi session có thể sửa plan theo tiến trình thực tế.

---

## TỔNG QUAN KIẾN TRÚC

```
GAP-DISTRIBUTION-PROFILE = DEMAND side: "Tôi MUỐN gì?"
ACTION-SPACE             = SUPPLY side: "Tôi CÓ THỂ LÀM gì?"

HÀNH VI THỰC TẾ = f(Gap Distribution × Action Space)
  → Có gap + có option → ACTION
  → Có gap + không option → STUCK / frustration
  → Có option + không gap → KHÔNG drive → không action

PATTERN-RESONANCE = OBSERVATION khi 2 entities tương tác:
  → Mỗi entity có Gap Distribution + Action Space RIÊNG
  → By-product output mỗi bên match gap bên kia → RESONANCE
  → Action Space quyết định: resonance genuine (có choice) hay forced (không choice)

THỨ TỰ:
  ① Action-Space.md TRƯỚC (supply side — foundation cho PR trục ⑤)
  ② Pattern-Resonance v4.0 SAU (reference Action-Space)
```

---

## PHASE 1: Action-Space.md v1.0

### Mục tiêu
- File OBSERVATION MỚI: "Không gian khả năng của 1 người tại 1 thời điểm"
- Sibling của Gap-Distribution-Profile.md (cùng folder Body-Feedback/)
- GDP = demand side (gaps cluster ở đâu). AS = supply side (options available ở đâu).
- 4 trục quan sát, parallel với GDP 4 trục.

### Vị trí
- Core-Deep-Dive/Body-Base/Body-Feedback/Action-Space.md
- Cạnh Gap-Distribution-Profile.md

### 4 Trục Quan Sát (đã drill kỹ session 2026-05-19)

```
TRỤC ① — COMPILED CAPACITY (năng lực đã compile):
  = Tổng chunks: knowledge + skills + physical ability
  = "Kho vũ khí" sẵn có
  = 2 chiều con: Depth (sâu trong 1 domain) × Breadth (rộng nhiều domain)
  
  QUAN TRỌNG:
    → "Chưa biết = không có gap" (Gap-Direction §5.3)
    → Trục này = BOTH năng lực thực VÀ ranh giới nhận thức
    → Invisible constraint: không biết option tồn tại → không có gap cho nó
    → ≠ bị chặn (frustration). = VÔ HÌNH (no feeling at all)

  REFERENCE: Gap-Direction §5.3, Domain-Mapping-Drive §5

TRỤC ② — RESOURCE ACCESS (tài nguyên tiếp cận):
  = Status.md Resource Access Map: "ai cho tôi lấy gì không cần đánh"
  = Material (tiền, tools) + Social capital (network, ai sẵn sàng giúp)
  = Money = bridge technology mở rộng fill options (Money-Analysis)

  REFERENCE: Status.md §1, Money-Analysis, Connection (Dunbar layers)

TRỤC ③ — FREEDOM (mức độ tự do hành động):
  = Constraint BÊN NGOÀI: luật + norms + obligations + dependency
  = Compliance-Floor: "tự do = default, luật = ngoại lệ"
  
  3 LOẠI CONSTRAINT KHÁC CĂN BẢN:
    BLOCKED: biết option, KHÔNG ĐƯỢC phép → frustration
    DEPENDENT: biết option, CHƯA ĐỦ resource → chấp nhận tạm
    INVISIBLE: KHÔNG BIẾT option tồn tại → không cảm gì (NGUY HIỂM NHẤT)

  VỀ VẬT LÝ: Không cần trục riêng. Người bình thường hiện đại ≈ không bị
  giới hạn vật lý. Mọi thứ = pattern trong não. Xem video biển = có chunks
  về biển (dù không sâu bằng thợ lặn). Physical constraint (tù, bệnh nặng)
  = edge case → crush trục ② và ③ xuống ≈ 0. Đã capture.

  REFERENCE: Compliance-Floor, Obligation, Autonomy-Hardware §5

TRỤC ④ — AWARENESS (nhận thức về action space CỦA MÌNH):
  = Gap giữa ACTUAL space và PERCEIVED space
  = PFC = Lawyer → person có thể sai về chính mình

  3 TRẠNG THÁI:
    UNDER-ESTIMATE: "không thể" nhưng thực ra có thể
      → Learned helplessness (vmPFC teo), compiled suppress ("tự làm = bị phạt")
      → 🟢 Maier & Seligman 2016, Bandura 1977 self-efficacy
    ACCURATE: hiếm, optimal
    OVER-ESTIMATE: "chắc chắn được" nhưng thiếu chunks
      → 🟢 Dunning-Kruger 1999

  REFERENCE: Autonomy-Hardware §2 (vmPFC/DRN), PFC=Lawyer (Gazzaniga)
```

### Interaction Giữa 4 Trục (POSITIVE + NEGATIVE SPIRAL)

```
① → ②: Knowledge mở rộng resource access (biết tiếng Anh → thị trường rộng)
② → ①: Resource mở rộng knowledge (có tiền → access giáo dục)
③ → ①②: Freedom ENABLES sử dụng ① và ② (bị giam → ①② vô nghĩa)
④ → ①②③: Awareness ACTIVATES tất cả (không biết mình có thể → stuck)

POSITIVE SPIRAL: ① ↗ → ② ↗ → ③ ↗ → ④ ↗ → ① ↗↗ ...
NEGATIVE SPIRAL: ① ↘ → ② ↘ → ③ ↘ → ④ ↘ → ① ↘↘ ...

"Poverty trap" = negative spiral CẢ 4 trục
"Privilege" = positive spiral CẢ 4 trục  
"Education" = intervention ở trục ① → kích hoạt positive spiral

🟢 Sen 1999 (Nobel): capability approach = freedom to achieve various lifestyles
🟢 Heckman 2006: early childhood intervention ROI = 7-10% annual
```

### Properties (parallel GDP §1.2)

```
① LUÔN THAY ĐỔI (dynamic): mỗi ngày compile thêm, resource tích/tiêu
② DAO ĐỘNG MẠNH: sáng vs chiều, stress vs relaxed → perceived space KHÁC
③ TỰ MÌNH KHÔNG NHẬN THỨC HẾT: PFC=Lawyer, invisible constraints/capabilities
④ CHỈ QUAN SÁT ĐƯỢC, KHÔNG ĐO CHÍNH XÁC: proxy only, not measurement
```

### Cases Cần Viết

```
CASE 1 — Einstein 25 tuổi: ① CAO (physics deep), ② THẤP (clerk), ③ OK, ④ CAO
  → Action space HẸP nhưng ĐỦ cho gap CỦA ÔNG (chỉ cần giấy bút)

CASE 2 — Công nhân nhà máy: ① HẸP, ② THẤP, ③ MODERATE, ④ THẤP
  → Gap Distribution narrow × Action Space narrow → hành vi narrow

CASE 3 — Sinh viên mới ra trường: ① MỚI, ② THẤP, ③ ĐANG MỞ, ④ ĐANG TÌM
  → "Tuổi 20s khủng hoảng" = action space đang mở nhưng gap distribution đang tìm center

CASE 4 — Trẻ bị bố mẹ ép: ① THẤP, ② DEPENDENT, ③ DEPENDENT, ④ INVISIBLE
  → Không biết cách sống khác → invisible constraint → không frustration → ở yên
  → KHI awareness tăng (lớn lên, gặp bạn, internet) → ① tăng → break possible

CASE 5 — Trúng số: ② BÙNG NỔ → action space expand đột ngột
  → Gap Distribution CHƯA kịp shift → "giàu nhưng không biết muốn gì"
```

### Research Anchors

```
🟢 Bandura 1977: Self-efficacy → behavior prediction
🟢 Sen 1999: Capability Approach → development = freedom
🟢 Heckman 2006: Early intervention ROI
🟢 Kruger & Dunning 1999: Competence ↔ self-assessment paradox
🟢 Maier & Seligman 2016: Learned helplessness → vmPFC damage
🟢 Deci & Ryan 2000 (SDT): Autonomy, competence, relatedness
🟡 4-trục model as unified framework = framework synthesis
```

### Actual Length: 1,729L (v1.0: 1,453L → +§7 Expansion Quality: 1,729L)

### Dependencies TO READ trước khi viết

```
MUST READ:
  - Gap-Distribution-Profile.md (FULL — sibling file, parallel structure)
  - Status.md §1 (Resource Access Map definition)
  - Autonomy-Hardware.md §2 (vmPFC/DRN controllability)
  - Gap-Direction.md §5.3 ("chưa biết = không có gap")

SHOULD READ:
  - Compliance-Floor.md (Freedom constraints)
  - Obligation.md §1-§3 (obligation as constraint)
  - Money-Analysis.md (money = bridge technology)
  - Autonomy.md (software development of autonomy)
```

---

## PHASE 2: Pattern-Resonance v4.0 Rewrite

### Mục tiêu
- Rewrite từ v3.1 → v4.0 với insights MỚI từ session 2026-05-19
- Reference Action-Space.md (Phase 1 phải xong trước)

### Key Changes v3.1 → v4.0

```
① DEFINITION REFINED:
  Pattern-Resonance = sustained mutual phenomenon khi 2+ entities
  có gap riêng → tương tác → by-product output mỗi bên TÌNH CỜ
  match gap direction bên kia → CẢ 2 receive reward → duy trì proximity
  → resonance SUSTAINED.
  
  "Resonance" yêu cầu 2 HỆ THỐNG PATTERN ĐỘC LẬP tìm thấy alignment.
  1 hệ thống matching reality ≠ resonance (= prediction verified = general drive).
  Tool interaction: reward nhưng KHÔNG resonance (tool không có pattern system).

② TOOL-MODE vs AGENT-MODE (mới):
  = 2 chiều xử lý SONG SONG trong não, KHÔNG phải 2 loại entity
  
  Tool processing: predict OUTPUT/HÀNH VI → "nếu X thì Y"
  Agent processing: simulate TRẠNG THÁI BÊN TRONG → SPM fire
  
  Cùng 1 entity → não switch giữa 2 mode:
    Đồng nghiệp: Tool-mode khi làm việc, Agent-mode khi ăn trưa
    AI: Tool-mode "dịch câu này", Agent-mode "bạn hiểu tôi ghê"
    Người dùng như Tool (dehumanize): suppress Agent-mode → costly
  
  PR emerge CHỈ KHI Agent-mode active + mutual + entity có body-base

③ 5 TRỤC QUAN SÁT RESONANCE (mới):
  ① By-product match level (No / Partial / Full / Anti-match, per-domain)
  ② Processing mode (Tool×Agent intensity, Compiled×Fresh)
  ③ Gap quality (Approach ← → Avoidance) — approach = sustainable, avoidance = unstable
  ④ Stream type (Stream 1 hardware ← → Stream 2 SPM compiled)
  ⑤ Constraint context (Genuine / Constrained / Invisible) — reference Action-Space.md

④ GIỮA NGUYÊN TỪ v3.1:
  → 2-Stream model (Stream 1 hardware + Stream 2 SPM)
  → By-product match principle
  → PR Baseline ("hợp tính")
  → 4 conditions (revised v3.1)
  → Anti-match concept
  → Per-pair topology
  → Temporal dynamics (S1 habituates, S2 deepens)
  → PFC=Lawyer caveat
  → Bird & Cook feedback loop
  → Obligation-trapped
  → All cases (restructured)

⑤ CASES MỚI:
  → Worker + Boss: resonance qua lương, break khi predict không trả lương
  → Con thích học + Mẹ: easy resonance (both approach)
  → Con ghét học + Mẹ ép: unstable resonance (avoidance), break conditions
  → Đồng nghiệp quên tuột: Tool-mode dominant → no Entity-Compiled
  → Đồng nghiệp thành bạn thân: Agent-mode genuine → Entity-Compiled
  → Dehumanization (lãnh chúa-nô lệ): suppress Agent-mode → costly
  → Parasocial (AI, ảnh Đức Mẹ): projected Agent-mode, not mutual

⑥ TÊN GIỮ NGUYÊN: Pattern-Resonance
  → Mô tả HIỆN TƯỢNG (2 pattern systems resonate), không phải mechanism
  → By-product match = mechanism TRONG file, không cần trong tên
  → 50+ files cross-reference → rename = massive update cost
  → Definition bên trong = đủ chính xác
```

### Dependencies TO READ trước khi viết

```
MUST READ:
  - Pattern-Resonance v3.1 (FULL — base for rewrite)
  - Action-Space.md v1.0 (Phase 1 output — trục ⑤ reference)
  - Inter-Body-Mechanism Architecture-Summary (Tool/Agent/Compiled/Fresh context)

SHOULD READ:
  - Drill-Entity-Compiled-Deep v1.4 §10b (ma trận 2D), §10e (PR vs SPM axes)
  - Connection v4.0 §1-§3 (3 Generative Primitives)
  - Self-Pattern-Match v3.0 §0, §2 (SPM = Stream 2 engine)
  - Gap-Distribution-Profile §2 (spectrum context)
  - Obligation.md (obligation-trapped)
```

### Bài viết bố mẹ-con (research-preference/bo-me-va-con.txt)
- Nội dung: transcript về giao tiếp bố mẹ-con, 3 nguyên nhân con không tâm sự
- Giá trị: CASE STUDY cho PR v4.0 (parent-child resonance break mechanisms)
- Mapping vào framework:
  → Nguyên nhân 1: "nghe nhưng không lắng nghe" = PFC respond trước khi SPM complete
  → Nguyên nhân 2: "phán xét" = anti-match (parent by-product CONFLICTS child's gap "được hiểu")
  → Nguyên nhân 3: "lôi chuyện cũ" = compiled negative chunks fire → child learn "nói = unsafe"
  → 3 nguyên tắc giải pháp = restore Agent-mode genuine: NGHE (SPM complete) → KHÔNG phán xét (không anti-match) → KHÔNG so sánh (không compile negative)
- CÓ THỂ dùng làm case trong PR v4.0 hoặc Drill-Entity-Compiled

### Estimated Length: ~1,800-2,200L (tăng từ v3.1 ~1,600L)

---

## TRACKING

### Status Legend
```
⬜ = chưa bắt đầu
🟡 = đang drill/viết
✅ = hoàn thành
```

### Progress
```
PHASE 1: Action-Space.md v1.0
  ✅ Read dependencies (GDP full, Status §0-§1, Autonomy-HW §0-§2, Autonomy §0,
     Gap-Direction §5.3, Compliance-Floor §0-§2, Obligation §0-§3,
     Money-Analysis §1+§3, Entity-Compiled-Capacity §1-§2, File-Index)
  ✅ Draft structure + 4 trục (expanded beyond plan: +§3 Constraints, +§4 Spirals,
     +§5 Formation, +§6 Shift, +§7 GDP×AS prediction)
  ✅ Write cases (5 profiles §2.5 + 4 cases §8: bố-mẹ-con, 2 xã hội, Hawking, lifecycle)
  ✅ Write honest assessment + 14 research citations
  ✅ Cross-reference check (§12: 5 primary + 8 mechanism + 5 observation + 3 application)
  ✅ Finalize v1.0 — 1,453 lines (2026-05-19)
  ✅ ADD §7 "Expansion Quality: Depth-First Principle" — v1.0 → 1,729 lines
     (+§7.1 awareness paradox, §7.2 threshold gate, §7.3 4 profiles,
      §7.4 depth-first principle, §7.5 premature expansion, §7.6 self-calibration)
     Renumbered §7-§12 → §8-§13. +2 research (Schwartz+Ericsson). §10-§13 updated.

PHASE 2: Pattern-Resonance v4.0
  ⬜ Read dependencies
  ⬜ Draft new sections (Tool/Agent, 5 trục, new cases)
  ⬜ Restructure existing content
  ⬜ Write honest assessment update
  ⬜ Cross-reference check (50+ files reference PR)
  ⬜ Finalize v4.0

POST-WRITE: Cross-Reference Updates
  ⬜ Inter-Body-Mechanism: add Tool/Agent processing note
  ⬜ Connection v4.0: reference PR v4.0
  ⬜ Gap-Distribution-Profile: reference Action-Space sibling
  ⬜ Drill-Entity-Compiled-Deep: cross-ref PR v4.0 axes
  ⬜ plan-drill-completion.md: update Phase 5 (PR-Definition) → reference PR v4.0
```

### Estimated Sessions: 3-4
```
Session 1: ✅ Phase 1 (Action-Space.md v1.0) — DONE 2026-05-19 (1,453L)
Session 2: Phase 2 part A (PR v4.0 draft — new sections)
Session 3: Phase 2 part B (PR v4.0 restructure + finalize)
Session 4: Cross-reference updates (nếu cần, có thể merge vào Session 3)
```

---

## NGUYÊN TẮC

```
① MỖI SESSION: đọc lại plan → đọc dependencies → write → update plan
② QUALITY: drill kỹ, verify research, flag uncertainty level
③ ADAPTABLE: session có thể merge/tách theo tiến trình thực tế
④ CROSS-CHECK: content mới phải consistent với framework hiện tại
⑤ NO DUPLICATE: reference existing files, không viết lại content đã có
⑥ OUTPUT: mỗi session → file mới/updated + plan progress update
```

---

## KEY INSIGHTS TỪ SESSION 2026-05-19 (cold start reference)

### Insight 1: Tool-mode vs Agent-mode = 2 chiều xử lý SONG SONG
```
Mọi tương tác đều có 2 component:
  Tool processing: predict OUTPUT/HÀNH VI ("nếu X thì Y")
  Agent processing: simulate TRẠNG THÁI BÊN TRONG (SPM fire)
Cùng 1 entity → não switch/mix giữa 2 mode tùy goal, context, thời điểm.
Không phải 2 loại entity — là 2 chế độ xử lý CỦA NÃO.
```

### Insight 2: "Resonance" cần 2 hệ thống pattern độc lập
```
Vật lý: resonance = 2 hệ dao động độc lập tìm tần số chung.
Framework: PR = 2 body-base có gap riêng tìm by-product match.
1 hệ thống matching reality ≠ resonance (chỉ là prediction verified).
→ Tool interaction: reward, nhưng KHÔNG resonance (tool không có pattern system).
→ Agent interaction: CÓ THỂ resonance (nếu mutual + entity có body-base).
```

### Insight 3: Action Space = Supply-side complement cho Gap-Distribution
```
GDP (demand): TÔI MUỐN GÌ? → gaps cluster ở đâu?
AS (supply): TÔI CÓ THỂ LÀM GÌ? → options available ở đâu?
Behavior = f(GDP × AS). Thiếu 1 = chỉ thấy nửa bức tranh.
4 trục: ① Compiled Capacity ② Resource Access ③ Freedom ④ Awareness
```

### Insight 4: 3 loại constraint khác căn bản
```
BLOCKED: biết option, KHÔNG ĐƯỢC phép → frustration
DEPENDENT: biết option, CHƯA ĐỦ resource → chấp nhận tạm
INVISIBLE: KHÔNG BIẾT option tồn tại → KHÔNG CẢM GÌ (nguy hiểm nhất)
Invisible constraint ↔ "chưa biết = không có gap" (Gap-Direction §5.3)
Education = chuyển INVISIBLE → BLOCKED/DEPENDENT → solvable
```

### Insight 5: Physical constraint = edge case, không cần trục riêng
```
Người bình thường hiện đại ≈ không bị giới hạn vật lý.
Mọi thứ = pattern trong não. Xem video biển = có chunks (dù nông hơn thợ lặn).
Physical constraint (tù, bệnh nặng) → crush trục ② ③ xuống ≈ 0.
Đã capture trong 4 trục — không cần trục 5.
```

### Insight 6: Gap quality = approach vs avoidance (cho PR)
```
Approach: bạn chơi vui, con thích học → sustainable, positive spiral
Avoidance: con học để không bị đánh → unstable, break khi threat removed
Resonance quality = f(gap quality cả 2 bên):
  Approach + Approach = highest quality
  Avoidance + Avoidance = unstable
  Mix = phổ biến nhất
```

### Insight 7: Break conditions cho resonance
```
Break khi 1 bên: cost > capacity (compiled suppress collapse)
Break khi 1 bên: tìm được alternative (action space expand)
Break khi 1 bên: gap disappears (lottery, life change)
Break khi awareness tăng: invisible constraint → visible → "tôi có thể đi"
```

### Insight 8: Bài bố mẹ-con = case study valuable
```
3 nguyên nhân con không tâm sự:
  ① "Nghe nhưng không lắng nghe" = PFC respond trước SPM complete
  ② "Phán xét" = anti-match (parent by-product CONFLICTS child's gap "được hiểu")
  ③ "Lôi chuyện cũ" = compiled negative → child learn "nói = unsafe"
3 giải pháp = restore Agent-mode: NGHE → KHÔNG PHÁN XÉT → KHÔNG SO SÁNH
```

---

**Created**: 2026-05-19
**Last updated**: 2026-05-19 (Phase 1 COMPLETE)
**Next session**: Phase 2 — Pattern-Resonance v4.0 rewrite (read deps + draft new sections)
