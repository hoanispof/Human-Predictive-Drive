---
title: Action-Space — Per-Person Capability Landscape Observation
version: 1.0
created: 2026-05-19
status: OBSERVATION FILE v1.0
scope: |
  OBSERVATION FILE: Mỗi người có 1 ACTION SPACE riêng —
  tổng thể khả năng available tại 1 thời điểm: biết gì, access gì,
  được phép gì, và NHẬN THỨC được bao nhiêu trong số đó.
  Action-Space KHÔNG phải per-gap property (Gap-Direction.md đã cover).
  Action-Space = AGGREGATE SUPPLY-SIDE property —
  nhìn TOÀN BỘ options landscape CỦA 1 NGƯỜI.
  Gap-Distribution-Profile = DEMAND side (tôi MUỐN gì).
  Action-Space (FILE NÀY) = SUPPLY side (tôi CÓ THỂ làm gì).
  HÀNH VI THỰC TẾ = f(Gap-Distribution × Action-Space).
  4 trục: ① Compiled Capacity × ② Resource Access × ③ Freedom × ④ Awareness.
  3 loại constraint: Blocked / Dependent / Invisible (invisible = nguy hiểm nhất).
  Positive/Negative spiral dynamics giữa 4 trục.
  Formation model parallel Gap-Distribution (collective infrastructure → social position → education → hardware).
purpose: |
  Gap-Distribution-Profile.md: DEMAND — gaps cluster ở đâu.
  CÁC FILE MECHANISM: per-concept (Status=resource, Autonomy=self-action, Obligation=cost...).
  FILE NÀY: AGGREGATE SUPPLY-SIDE VIEW:
    → Nhìn action space như PER-PERSON PROFILE
    → Bridge: capability concepts rải rác → unified supply-side observation
    → Observation tool: giúp NHÌN THẤY capability landscape hiện tại
    → Prediction tool: Gap-Distribution × Action-Space → behavioral prediction (4 quadrants)
    → Gap-Distribution × Action-Space = COMPLETE behavioral prediction framework
  = Missing aggregate view giữa "per-concept mechanism" và "aggregate behavior prediction"
position: |
  Core-Deep-Dive/Body-Base/Body-Feedback/ — cạnh Gap-Distribution-Profile.md.
  Gap-Distribution-Profile.md = DEMAND side (WHERE all gaps cluster).
  Action-Space.md (FILE NÀY) = SUPPLY side (WHAT options available).
  BỔ SUNG nhau — KHÔNG THAY THẾ. Đọc Gap-Distribution TRƯỚC file này.
dependencies:
  - Gap-Distribution-Profile.md v1.0 — sibling file, demand side, 4 trục, 4-tầng formation
  - Gap-Direction.md v2.0 — per-gap mechanism, "chưa biết = không có gap" (§5.3)
  - Status.md v2.1 — §1 Resource Access Map (trục ②)
  - Autonomy-Hardware.md v1.1 — §2 vmPFC/DRN controllability (trục ④ hardware)
  - Autonomy.md v1.1 — software development of autonomy (trục ④ software)
  - Compliance-Floor.md v2.0 — freedom constraints, 4-layer floor (trục ③)
  - Obligation.md v1.1 — obligation as constraint, 5-factor formula (trục ③)
  - Money-Analysis.md v1.0 — money = bridge technology (trục ②)
  - Inter-Body-Mechanism.md v1.0 — Architecture B, PFC=Lawyer, 3-cost model
  - Chunk.md v2.2 — sole substrate, compilation
  - Body-Feedback-Label.md v2.0 — vocabulary reference
  - Connection.md v4.0 — Dunbar layers (social capital)
  - Drill-Entity-Compiled-Capacity.md v1.0 — Dunbar layers, Depth × Breadth = constant
  - Domain-Mapping-Drive.md v1.0 — reward from PROCESS, threshold
  - Background-Pattern.md v1.1 — Background-Pattern self-reinforcing, identity lock
  - Self-Created-Threat.md v1.0 — 4 loại, awareness
  - Expansion-Saturation-Crisis.md v1.1 — Expansion→Discovery shift
research:
  - Sen 1999 (Nobel) — Capability Approach, development = freedom to achieve various lifestyles
  - Bandura 1977 — Self-efficacy, belief in capability → behavior prediction
  - Heckman 2006 — Early childhood intervention ROI = 7-10% annual
  - Kruger & Dunning 1999 — Competence ↔ self-assessment paradox (overestimate)
  - Maier & Seligman 2016 — Learned helplessness = DEFAULT, vmPFC learns "controllable"
  - Deci & Ryan 2000 — Self-Determination Theory, autonomy, competence, relatedness
  - Dunbar 1992, Zhou et al. 2005 — Social Brain Hypothesis, layered structure (~5/15/50/150)
  - Putnam 2000 — Social capital, bonding vs bridging
  - Bourdieu 1986 — 3 capitals, economic + social + cultural
  - Vroom 1964 — Expectancy Theory, behavior = f(expectancy × valence)
  - Kahneman & Deaton 2010 — Emotional well-being income plateau
  - Tedeschi & Calhoun 2004 — Post-traumatic growth
  - Chase & Simon 1973 — Expertise restructures perception
  - Dollard et al. 1939 — Frustration-aggression hypothesis
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Action-Space — Per-Person Capability Landscape Observation

> **2 người cùng muốn thoát nghèo. Cùng sống 1 xóm. Cùng 25 tuổi.**
> **Cùng gap. Cùng drive. Cùng body-need fire.**
>
> **Người A: biết tiếng Anh, có laptop, có bạn trong ngành IT,**
> **biết mình có thể học code.**
> **Người B: chỉ biết tiếng Việt, không có máy tính,**
> **chỉ biết hàng xóm, không biết "IT" là gì.**
>
> **CÙNG GAP. KHÁC hoàn toàn OPTIONS.**
> **Người A thấy 5 con đường. Người B thấy 0 con đường.**
>
> **Không phải B lười. Không phải B không muốn.**
> **B KHÔNG BIẾT CÓ CON ĐƯỜNG NÀO.**
>
> **Gap-Distribution-Profile: "Tôi MUỐN gì?" — demand side.**
> **File NÀY: "Tôi CÓ THỂ làm gì?" — supply side.**
>
> **Hành vi thực tế = f(muốn gì × có thể gì).**
> **Thiếu 1 = chỉ thấy nửa bức tranh.**
>
> **Và action space KHÔNG tự nhiên có.**
> **Nó được HÌNH THÀNH bởi: collective infrastructure → social position →**
> **education + gia đình → hardware + trải nghiệm.**
>
> **File này: nhìn action space như PROFILE cá nhân,**
> **HÌNH THÀNH từ đâu, QUAN SÁT bằng gì, và PREDICT được gì.**

---

## Mục lục

- §0 — VỊ TRÍ + SCOPE
- §1 — DEFINITION: Action-Space = Supply-Side Profile
- §2 — 4 TRỤC QUAN SÁT
- §3 — 3 LOẠI CONSTRAINT
- §4 — SPIRAL DYNAMICS
- §5 — FORMATION MODEL
- §6 — SHIFT MECHANISMS
- §7 — EXPANSION QUALITY: DEPTH-FIRST PRINCIPLE
- §8 — Gap-Distribution × Action-Space: BEHAVIORAL PREDICTION
- §9 — CASES
- §10 — RESEARCH ANCHORS
- §11 — HONEST ASSESSMENT
- §12 — OPEN QUESTIONS
- §13 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ + SCOPE

```
⭐ FILE NÀY TRONG FRAMEWORK:

  Core-Deep-Dive/Body-Base/Body-Feedback/ — OBSERVATION FILE.

  PHÂN BIỆT VỚI CÁC FILE GẦN:

    ┌──────────────────────────┬──────────────────────────────────────┐
    │ File                     │ Trả lời                              │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Gap-Distribution-        │ DEMAND: Gaps cluster ĐÂU?            │
    │ Profile.md v1.0          │ Per-person gap landscape.             │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ ⭐ FILE NÀY               │ SUPPLY: Options available ĐÂU?       │
    │ Action-Space.md          │ Per-person capability landscape.      │
    │                          │ Gap-Distribution × Action-Space = behavioral prediction.     │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Status.md v2.1           │ Resource Access Map (1 CHIỀU).        │
    │                          │ File này dùng ĐÓ + 3 trục nữa.      │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Autonomy-Hardware.md     │ TẠI SAO self-action = reward.         │
    │                          │ = 1 mechanism TRONG trục ④.           │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Obligation.md v1.1       │ Cost to MAINTAIN agent access.        │
    │                          │ = 1 constraint TRONG trục ③.          │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Compliance-Floor.md v2.0 │ Luật tối thiểu (LEGAL constraints).   │
    │                          │ = 1 constraint TRONG trục ③.          │
    └──────────────────────────┴──────────────────────────────────────┘

  → Status, Autonomy, Obligation, Compliance-Floor = per-concept DEEP.
  → File này = AGGREGATE view (toàn bộ supply-side landscape)
  → BỔ SUNG — không duplicate mechanism đã có.


SCOPE IN:
  ✅ Action space as per-person aggregate supply-side property
  ✅ 4 trục quan sát (Compiled Capacity, Resource Access, Freedom, Awareness)
  ✅ 3 loại constraint (Blocked, Dependent, Invisible)
  ✅ Positive/Negative spiral dynamics giữa 4 trục
  ✅ Formation model (Collective Infrastructure → Hardware)
  ✅ Shift mechanisms per trục
  ✅ Gap-Distribution × Action-Space behavioral prediction (4 quadrants)
  ✅ Cases: observable examples
  ✅ Sen's Capability Approach as research anchor

SCOPE OUT:
  ❌ Per-concept mechanism → Status.md, Obligation.md, etc.
  ❌ Per-gap mechanism → Gap-Direction.md
  ❌ Demand side → Gap-Distribution-Profile.md
  ❌ Prescribe "nên có action space thế nào" → framework = DESCRIPTIVE
  ❌ Per-era empirical data → application layer
```

---

## §1 — DEFINITION: Action-Space = Supply-Side Profile

### §1.1 — Từ per-concept đến aggregate

```
⭐ CÁC FILE MECHANISM MÔ TẢ PER-CONCEPT. FILE NÀY MÔ TẢ TOÀN BỘ SUPPLY-SIDE.

  Hiện tại, framework có:
    → Status.md: Resource Access Map (tôi access GÌ từ agent NÀO)
    → Autonomy.md: Xu hướng tự chủ (tôi prefer self-action bao nhiêu)
    → Obligation.md: Chi phí duy trì access (tôi trả GÌ cho access)
    → Compliance-Floor.md: Giới hạn luật pháp (tôi KHÔNG ĐƯỢC phép gì)
    → Chunk.md: Cơ chế tích lũy (chunks compile thế nào)
    → Entity-Compiled-Capacity: Dunbar ceiling (bao nhiêu relationships)

  File này ADD:
    → Mỗi người có KHÔNG GIAN KHẢ NĂNG tại mỗi thời điểm
    → Không gian này = TỔNG THỂ: biết gì + access gì + được phép gì + nhận thức gì
    → = AGGREGATE SUPPLY-SIDE PROPERTY
    → = PER-PERSON, PER-MOMENT, LUÔN THAY ĐỔI

  VÍ DỤ:
    Người A tại thời điểm T:
      Compiled Capacity: biết 3 ngôn ngữ, có bằng IT, 10 năm kinh nghiệm
      Resource Access: lương 50M/tháng, network 200 contacts, có nhà
      Freedom: tự do nghề nghiệp, không nợ, con đã lớn
      Awareness: biết mình có thể khởi nghiệp, biết market, biết rủi ro
      → Action-Space A: RẤT RỘNG — nhiều options available

    Người B tại thời điểm T:
      Compiled Capacity: hết lớp 9, biết trồng trọt, khỏe mạnh
      Resource Access: thu nhập 5M/tháng, biết hàng xóm, không có vốn
      Freedom: phải nuôi bố mẹ, nợ ngân hàng, 1 nghề duy nhất
      Awareness: không biết có scholarship, không biết có online courses
      → Action-Space B: RẤT HẸP — ít options available

  → A và B khác nhau KHÔNG phải vì IQ hay "ý chí"
  → Mà vì ACTION SPACE khác → options khác → hành vi khác → đời khác
```

### §1.2 — Action-Space as distribution (không phải single point)

```
⭐ MỖI NGƯỜI = 1 DISTRIBUTION, KHÔNG PHẢI 1 ĐIỂM:

  GIỐNG Gap-Distribution §1.2 — Action-Space KHÔNG NÊN được mô tả 1 từ:
    KHÔNG NÊN: "Người này có action space rộng" (oversimplification)
    NÊN: "Người này có capacity SÂU ở IT, resource access TRUNG BÌNH,
          freedom CAO, awareness HẸP ngoài domain"

  Action-Space có "PROFILE":
    → 4 trục INDEPENDENT — combine tạo unique per-person profile
    → Có trục RỘNG (nhiều options), có trục HẸP (ít options)
    → Mỗi trục có VÙNG mạnh và VÙNG yếu
    → VD: Einstein 1905 — capacity CỰC SÂU (physics) + resource HẸP (clerk)
         + freedom OK (có thời gian rảnh) + awareness CAO (biết mình giỏi physics)

  Action-Space LUÔN THAY ĐỔI:
    → Mỗi ngày compile thêm chunks → trục ① expand
    → Kiếm/tiêu tiền → trục ② dao động
    → Luật thay đổi, nghĩa vụ thêm/bớt → trục ③ shift
    → Gặp người mới, đọc sách, nghe podcast → trục ④ có thể đột ngột expand
    → = Dynamic, per-moment, KHÔNG cố định

  Action-Space TỰ MÌNH KHÔNG NHẬN THỨC HẾT:
    → PFC = Lawyer (Inter-Body-Mechanism §7): tự đánh giá capability = BIASED
    → Trục ④ (Awareness) chuyên mô tả gap giữa ACTUAL và PERCEIVED
    → = Chỉ QUAN SÁT ĐƯỢC, không ĐO CHÍNH XÁC (giống Gap-Distribution §1.2)
```

### §1.3 — Gap-Distribution × Action-Space = Behavioral Prediction

```
⭐⭐ HÀNH VI THỰC TẾ = f(Gap-Distribution × Action-Space):

  Gap-Distribution (demand): "Tôi MUỐN gì?" → gaps cluster ở đâu
  Action-Space (supply): "Tôi CÓ THỂ gì?" → options available ở đâu
  Behavior: GIAO CỦA HAI — chỉ nơi gap VÀ option GẶP NHAU → action

  4 QUADRANTS:

    ┌────────────────────────────┬──────────────────────────────────┐
    │ Gap-Distribution CAO + Action-Space CAO           │ Gap-Distribution CAO + Action-Space THẤP                │
    │                            │                                  │
    │ = ACTIVE PURSUIT           │ = FRUSTRATION / STUCK            │
    │ Muốn + có thể → hành động │ Muốn + không thể → đau khổ      │
    │ VD: Nhà nghiên cứu có lab │ VD: Nghệ sĩ nghèo muốn vẽ      │
    │ VD: Doanh nhân có vốn      │ nhưng phải đi làm công nhân     │
    │ → Productive, tự tin       │ → Chronic dissonance, có thể     │
    │                            │   learned helplessness            │
    ├────────────────────────────┼──────────────────────────────────┤
    │ Gap-Distribution THẤP + Action-Space CAO          │ Gap-Distribution THẤP + Action-Space THẤP               │
    │                            │                                  │
    │ = DRIFT / WASTE            │ = SIMPLE / TRAPPED               │
    │ Có thể + không muốn       │ Không muốn + không thể           │
    │ → KHÔNG DRIVE              │ → Narrow life, stable nhưng hẹp  │
    │ VD: Con nhà giàu, có mọi  │ VD: Nông dân vùng sâu — ít gap, │
    │ điều kiện nhưng "chán"     │ ít option, cuộc sống đơn giản   │
    │ → Trúng số case            │ → Bình yên HOẶC invisible trap  │
    │ → "Giàu nhưng không biết  │                                  │
    │    muốn gì"               │                                  │
    └────────────────────────────┴──────────────────────────────────┘

  ⭐ QUADRANT QUAN TRỌNG NHẤT: Gap-Distribution CAO + Action-Space THẤP
    → Đây là SUFFERING quadrant
    → Body fire gap THẬT (demand có) nhưng KHÔNG CÓ CÁCH FILL (supply thiếu)
    → = Chronic cortisol holding (Cortisol-Baseline §7: Role ② sustained)
    → = Nếu kéo dài → learned helplessness (Maier & Seligman 2016)
    → = Education + resource access = 2 levers chính để move sang Q1

  ⭐ Gap-Distribution VÀ Action-Space ẢNH HƯỞNG LẪN NHAU:
    → Action-Space expand → domains mới accessible → chunks mới → gaps MỚI HÌNH THÀNH → Gap-Distribution shift
    → Gap-Distribution shift → drive mới → effort build capacity → Action-Space expand
    → = FEEDBACK LOOP — không 1 chiều
    → Education chính yếu = expand Action-Space ④ (awareness) → trigger feedback loop


🟡 Gap-Distribution × Action-Space 4-quadrant model = framework synthesis
🟢 Behavior = f(capability × motivation): Vroom 1964 Expectancy Theory
🟢 Frustration when blocked: Dollard et al. 1939
```

---

## §2 — 4 TRỤC QUAN SÁT

### §2.0 — Tổng quan

```
⭐ 4 TRỤC ORTHOGONAL — MỖI TRỤC MÔ TẢ KHÍA CẠNH KHÁC CỦA ACTION SPACE:

  ┌────────────────┬──────────────────┬──────────────────────────────────┐
  │ Trục           │ Question         │ Observable proxy                  │
  ├────────────────┼──────────────────┼──────────────────────────────────┤
  │ ① Compiled     │ Tôi BIẾT gì,    │ Skills, education, languages,    │
  │   Capacity     │ LÀM ĐƯỢC gì?    │ years experience, certifications │
  ├────────────────┼──────────────────┼──────────────────────────────────┤
  │ ② Resource     │ Tôi ACCESS      │ Income, savings, network size,    │
  │   Access       │ được GÌ?        │ tools, social capital             │
  ├────────────────┼──────────────────┼──────────────────────────────────┤
  │ ③ Freedom      │ Tôi ĐƯỢC PHÉP   │ Legal constraints, obligations,   │
  │                │ làm gì?         │ dependencies, social norms        │
  ├────────────────┼──────────────────┼──────────────────────────────────┤
  │ ④ Awareness    │ Tôi BIẾT mình   │ Self-assessment accuracy,         │
  │                │ có thể gì?      │ domain exposure, meta-cognition   │
  └────────────────┴──────────────────┴──────────────────────────────────┘

  4 trục INDEPENDENT — combine to create unique per-person profile.
  → ① nói CÓ GÌ. ② nói ACCESS GÌ. ③ nói ĐƯỢC PHÉP GÌ. ④ nói BIẾT GÌ VỀ CHÍNH MÌNH.

  SO SÁNH VỚI Gap-Distribution 4 TRỤC:
    Gap-Distribution: ① WHERE gaps ② WHY there ③ HOW shaped ④ HOW STABLE
    Action-Space:  ① WHAT can do ② WHAT can access ③ WHAT allowed ④ WHAT aware of

  Gap-Distribution = DEMAND → "landscape muốn gì"
  Action-Space = SUPPLY → "landscape có thể gì"
```

### §2.1 — Trục ① Compiled Capacity (biết gì, làm được gì)

```
⭐ COMPILED CAPACITY = TỔNG CHUNKS: KNOWLEDGE + SKILLS + PHYSICAL ABILITY:

  DEFINITION:
    → "Kho vũ khí" sẵn có tại thời điểm T
    → = Tổng thể chunks đã compile: domain knowledge, motor skills, languages,
        social skills, physical fitness, professional expertise
    → = f(years exposure × domain fit × compile depth)

  2 CHIỀU CON:

    DEPTH (sâu trong 1 domain):
      → Years of deliberate practice/exposure → chunks compile deep
      → Deep = see patterns others miss (Chase & Simon 1973)
      → Deep = high reward when gap fill (compound effect)
      → VD: chess master 20 năm, surgeon 15 năm, physicist 30 năm

    BREADTH (rộng nhiều domain):
      → Exposure nhiều domain → chunks compile across
      → Breadth = versatility, bridge function
      → Breadth = more options per situation
      → VD: T-shaped designer, polyglot, generalist manager

    DEPTH × BREADTH ≈ CONSTANT (Drill-Entity-Compiled-Capacity §5):
      → Finite compilation resource — deep 1 domain = less cho domains khác
      → = Tradeoff, KHÔNG phải failure
      → Specialist: narrow-deep. Generalist: broad-shallow. T-shaped: hybrid.


  ⭐ INVISIBLE BOUNDARY — QUAN TRỌNG NHẤT:

    "Chưa biết = không có gap" (Gap-Direction §5.3) applies DIRECTLY:
      → Compiled Capacity = BOTH năng lực thực VÀ ranh giới nhận thức
      → Không biết Python tồn tại → không có gap "muốn học Python"
                                   → không có option "dùng Python giải bài"
      → = INVISIBLE CONSTRAINT (§3.3): không biết option tồn tại → NO FEELING

    DISTINCTION QUAN TRỌNG:
      → Năng lực THỰC (compiled chunks) = trục ① → measurable
      → Nhận thức về năng lực = trục ④ → perception gap
      → Trục ① và ④ LIÊN QUAN nhưng KHÁC:
        ① "tôi biết code Python" (fact)
        ④ "tôi biết rằng tôi biết code Python" (meta-awareness)
        ④ "tôi KHÔNG biết rằng Go language tồn tại" (invisible boundary)


  OBSERVABLE PROXIES:
    → Education level, certifications, years of experience
    → Skills demonstrated (not just claimed)
    → Languages spoken, tools mastered
    → Physical ability, health status
    → = Proxy — mỗi proxy chỉ capture MỘT phần

🟢 Expertise restructures perception: Chase & Simon 1973
🟢 Depth × Breadth tradeoff: Roberts et al. 2009 (Dunbar relationship layers)
🟢 "Chưa biết = không có gap": Gap-Direction §5.3 (established framework principle)
```

### §2.2 — Trục ② Resource Access (tiếp cận được gì)

```
⭐ RESOURCE ACCESS = STATUS.MD RESOURCE ACCESS MAP MỞ RỘNG:

  DEFINITION:
    → Status.md §1: "ai cho tôi lấy gì không cần đánh"
    → File này REFRAME: resource access = TẤT CẢ tài nguyên có thể mobilize
    → = KHÔNG CHỈ social status — bao gồm material + social + knowledge access

  3 LOẠI RESOURCE:

    MATERIAL (vật chất):
      → Tiền, tài sản, tools, thiết bị, workspace
      → Money = bridge technology (Money-Analysis §1.2):
        → Standardize cross-domain costs
        → Convert implicit → explicit obligation
        → Scale community exchange
      → = Options mà TIỀN MUA ĐƯỢC

    SOCIAL CAPITAL (mạng lưới):
      → Ai sẵn sàng giúp? → Dunbar layers (Entity-Compiled-Capacity §1.2)
        S1 ~5: intimate — sẵn sàng giúp vô điều kiện
        S2 ~15: close — giúp khi được nhờ
        S3 ~50: friends — giúp trong khả năng
        S4 ~150: active — giới thiệu, thông tin
      → Network BREADTH + DIVERSITY (Putnam 2000):
        Bonding capital: mạng lưới GIỐNG mình → support emotional
        Bridging capital: mạng lưới KHÁC mình → access domains mới
      → = Options mà NETWORK MỞ ĐƯỢC

    KNOWLEDGE ACCESS (tiếp cận kiến thức):
      → Internet, thư viện, mentor, peer group
      → KHÁC trục ①: đây là ACCESS (có thể tiếp cận), không phải COMPILED (đã biết)
      → VD: có internet = access TIỀM NĂNG (nhưng chưa compile)
      → VD: có mentor = access HƯỚNG DẪN (accelerate compile)
      → = Options mà INFRASTRUCTURE CHO PHÉP


  ⭐ TIỀN = MULTIPLIER CHO TRỤC ②, KHÔNG PHẢI TẤT CẢ:
    → Tiền MUA ĐƯỢC material resource → trục ② expand
    → Tiền MUA ĐƯỢC social access phần nào (events, clubs) → trục ② partial
    → Tiền KHÔNG MUA ĐƯỢC compiled capacity → trục ① cần TIME
    → Tiền KHÔNG MUA ĐƯỢC freedom trực tiếp → trục ③ cần legal/social change
    → Tiền KHÔNG MUA ĐƯỢC awareness → trục ④ cần exposure + meta-cognition
    → = Money important nhưng NOT sufficient cho full Action-Space expansion

  ⭐ DIMINISHING RETURNS (Kahneman & Deaton 2010):
    → $0 → $30K/year: massive Action-Space expansion (survival → options)
    → $30K → $100K: moderate expansion (comfort → more options)
    → $100K → $1M: marginal expansion (premium access)
    → $1M+: near-zero expansion (luxury ≠ more options)
    → = Resource access có CEILING — more money ≠ proportionally more Action-Space


  OBSERVABLE PROXIES:
    → Income, savings, assets
    → Network size + diversity
    → Access to mentors, experts
    → Infrastructure available (internet, library, transport)

🟢 Status = Resource Access Map: Status.md §1 (established framework)
🟢 Social capital: Putnam 2000, Bourdieu 1986
🟢 Income ↔ well-being plateau: Kahneman & Deaton 2010
🟢 Dunbar layers: Zhou et al. 2005
```

### §2.3 — Trục ③ Freedom (mức độ tự do hành động)

```
⭐ FREEDOM = CONSTRAINT BÊN NGOÀI: CÁI GÌ CẢN TRỞ TÔI DÙNG ① VÀ ②:

  DEFINITION:
    → Compliance-Floor.md: "tự do = default, luật = ngoại lệ"
    → Trục này: TỔNG THỂ constraint BÊN NGOÀI đang hạn chế options
    → = Biết (①) + Có (②) + ĐƯỢC PHÉP (③) = option thực sự available

  4 NGUỒN CONSTRAINT:

    LEGAL (luật pháp):
      → Compliance-Floor 4-layer: body-base + chunks + melody space + collective
      → "Không được giết, trộm, lừa, xâm phạm" → appropriate constraints
      → "Không được kinh doanh không phép" → bureaucratic constraint
      → "Không được rời nước" (một số regime) → oppressive constraint
      → = Constraint CẦN THIẾT (protect others) + EXCESS (limit freedom quá mức)

    SOCIAL NORMS (chuẩn mực xã hội):
      → "Con gái không nên làm kỹ sư" (nhiều xã hội)
      → "Phải cưới trước 30" (Collective-Schema-Pressure)
      → KHÔNG phải luật nhưng FUNCTIONING NHƯ LUẬT:
        Vi phạm → social punishment (Collective-Body §2: compile paths)
      → = Invisible constraint khi chưa awareness, visible khi awareness tăng

    OBLIGATIONS (nghĩa vụ):
      → Obligation.md: compiled prediction about cost to maintain access
      → "Phải nuôi bố mẹ" → constrain career options
      → "Nợ ngân hàng" → constrain spending/risk-taking
      → "Phải giữ job vì gia đình" → constrain exploration
      → = Obligation REDUCE freedom NHƯNG provide access (tradeoff)

    DEPENDENCY (phụ thuộc):
      → Trẻ em: phụ thuộc bố mẹ → freedom ≈ 0 (appropriate, developmental)
      → Nhân viên: phụ thuộc boss → freedom trong work = limited
      → Nợ nần: phụ thuộc chủ nợ → freedom = constrained
      → = Dependency = INVERSE of autonomy (Autonomy.md §3.1)


  ⭐ PHYSICAL CONSTRAINT = EDGE CASE:

    Người bình thường hiện đại ≈ KHÔNG bị giới hạn vật lý:
      → Xem video biển = có chunks về biển (dù nông hơn thợ lặn)
      → Internet + travel = access gần như mọi domain
      → = Mọi thứ = patterns trong não

    KHI physical constraint CÓ (tù, bệnh nặng, khuyết tật nghiêm trọng):
      → Crush trục ② (resource access) xuống ≈ 0
      → Crush trục ③ (freedom) xuống ≈ 0
      → Trục ① (capacity) VẪN CÒN (biết vẫn biết)
      → Trục ④ (awareness) VẪN CÒN (biết vẫn biết mình có thể)
      → = Đã capture trong 4 trục — KHÔNG cần trục 5

    VD: Stephen Hawking — ①④ rất cao, ②③ bị crush bởi ALS
      NHƯNG: technology (wheelchair, voice synthesizer) = partial restore ②③
      → = Physical constraint ≈ crash ②③ nhưng technology có thể partially compensate


  OBSERVABLE PROXIES:
    → Legal status (citizen, visa, undocumented)
    → Debt level, financial obligations
    → Family obligations (dependent parents, children)
    → Social norm pressure (cultural context)
    → Physical freedom (health, mobility, location)

🟢 Development = freedom: Sen 1999 (Capability Approach)
🟢 Compliance Floor = harm principle: Mill 1859
🟡 4 nguồn constraint = framework synthesis (integrating multiple files)
```

### §2.4 — Trục ④ Awareness (nhận thức về action space CỦA MÌNH)

```
⭐⭐ AWARENESS = GAP GIỮA ACTUAL ACTION SPACE VÀ PERCEIVED ACTION SPACE:

  DEFINITION:
    → Trục ①②③ mô tả ACTION SPACE THỰC TẾ (objective)
    → Trục ④ mô tả BẠN BIẾT BAO NHIÊU VỀ CHÍNH MÌNH (subjective)
    → Gap giữa actual và perceived = OBSERVATION TARGET CỦA TRỤC NÀY

  PFC = LAWYER (Inter-Body-Mechanism §7):
    → PFC KHÔNG phải thẩm phán trung lập
    → PFC = luật sư cho body-base: tạo narrative defend action body ĐÃ muốn
    → → Self-assessment = BIASED — luôn luôn
    → = Tại sao trục ④ TÁCH khỏi ①②③


  3 TRẠNG THÁI:

    UNDER-ESTIMATE: "tôi không thể" nhưng thực ra CÓ THỂ
      → Learned helplessness: vmPFC teo → DRN không bị suppress →
        default "bất lực" KHÔNG ĐƯỢC override (Maier & Seligman 2016)
      → Compiled suppress: "tự làm = bị phạt" đã compile từ thơ ấu
        (Autonomy.md §1.2: Bé B bị quát khi thử)
      → → Actual Action-Space rộng hơn perceived Action-Space → options BỎ QUA
      → → Body VẪN fire reward cho self-action (hardware) nhưng
        software override → "biết nên tự làm nhưng không dám"

    ACCURATE: nhận thức ≈ thực tế — HIẾM
      → Cần: domain exposure rộng + meta-cognition + feedback từ domain
      → = "Biết mình biết gì, biết mình KHÔNG biết gì" (Socrates paradox)
      → = Optimal nhưng ASYMPTOTIC — không ai 100% accurate

    OVER-ESTIMATE: "tôi chắc chắn được" nhưng THIẾU chunks
      → Dunning-Kruger 1999: low competence + low meta-cognition →
        "tôi giỏi" (vì chưa biết mình thiếu gì)
      → Freshly graduated: "4 năm đại học = expert" → reality shock
      → → Perceived Action-Space rộng hơn actual Action-Space → TRY nhưng FAIL → recalibrate
      → → Failure = PAINFUL nhưng = recalibration mechanism


  ⭐⭐ INVISIBLE CONSTRAINT: ĐẶC BIỆT QUAN TRỌNG

    Awareness trục ④ kết nối với §3.3 (Invisible constraint):

    Không biết option TỒN TẠI = KHÔNG CÓ GAP CHO NÓ:
      → Không biết có scholarship → không apply → opportunity missed
      → Không biết có online learning → không học → capacity stuck
      → Không biết có career path X → không pursue → life path limited

    KHI awareness TĂNG → invisible TRỞ THÀNH visible:
      → "Ồ có cách này sao" → option SUDDENLY available
      → 1 cuộc trò chuyện → 1 cuốn sách → 1 video → trục ④ expand ĐỘT NGỘT
      → = CHEAPEST to expand (không cần years) nhưng HARDEST to trigger
        (vì invisible = không biết cần tìm gì)

    EDUCATION = CHUYỂN INVISIBLE → VISIBLE:
      → Education KHÔNG chỉ dạy skill (trục ①)
      → Education CHÍNH YẾU MỞ MẮT (trục ④):
        "À, có domain này tồn tại. Có career này tồn tại."
      → → Invisible constraint → Blocked/Dependent → SOLVABLE
      → → = TẠI SAO education = most powerful intervention


  OBSERVABLE PROXIES:
    → Mức độ match giữa self-assessment và external assessment
    → Response khi gặp new information: "ồ, có thể thế này sao?" = expanding
    → Domain exposure breadth (biết bao nhiêu fields TỒN TẠI)
    → Willingness to seek feedback + update self-model

🟢 Dunning-Kruger 1999: low competence → overestimate
🟢 Maier & Seligman 2016: learned helplessness = DEFAULT, vmPFC learns controllable
🟢 Bandura 1977: self-efficacy → behavior prediction
🟡 Invisible constraint taxonomy = framework synthesis
```

### §2.5 — 4 trục kết hợp — Examples

```
🟡 5 PROFILE EXAMPLES (simplified — reality = more nuanced):

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 1: "Einstein 25 tuổi"                                    │
  │ ① Capacity: CỰC SÂU (physics) + hẹp (ít domain khác)           │
  │ ② Resource: THẤP (clerk, lương thấp, ít network academic)       │
  │ ③ Freedom: MODERATE (có thời gian rảnh, không bị ép)            │
  │ ④ Awareness: CAO (biết mình giỏi physics, biết field cần gì)   │
  │                                                                   │
  │ ⭐ Action space HẸP nhưng ĐỦ cho gap CỦA ÔNG:                    │
  │ Chỉ cần giấy bút + thời gian + trí tuệ = ĐỦ cho physics       │
  │ → Gap-Distribution × Action-Space MATCH: abstract gap + abstract capacity = productive  │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 2: "Công nhân nhà máy VN"                                │
  │ ① Capacity: HẸP (1 skill chuyên môn, ít domain khác)            │
  │ ② Resource: THẤP (lương thấp, network hẹp, ít tools)            │
  │ ③ Freedom: MODERATE (tự do pháp lý, nhưng nợ + gia đình)       │
  │ ④ Awareness: THẤP (không biết options khác tồn tại)             │
  │                                                                   │
  │ ⭐ Action-Space HẸP × Gap-Distribution HẸP = life HẸP nhưng ỔN ĐỊNH:                    │
  │ Không frustration (vì không biết options khác) → invisible trap  │
  │ CẦN: education ④ → mở mắt → options visible → Gap-Distribution có thể shift  │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 3: "Sinh viên mới ra trường"                             │
  │ ① Capacity: MỚI (kiến thức academic, ít practical)               │
  │ ② Resource: THẤP (ít tiền, network = bạn học)                    │
  │ ③ Freedom: ĐANG MỞ (ít obligation, ít dependency)               │
  │ ④ Awareness: ĐANG TÌM (biết nhiều field nhưng chưa deep)       │
  │                                                                   │
  │ ⭐ Action-Space ĐANG EXPAND + Gap-Distribution ĐANG TÌM CENTER:                          │
  │ "Quarter-life crisis" = Action-Space mở nhưng Gap-Distribution chưa converge           │
  │ → Nhiều options nhưng không biết muốn gì → "khủng hoảng tuổi 20"│
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 4: "Trẻ bị bố mẹ ép"                                    │
  │ ① Capacity: THẤP (đang compile, ít experience)                  │
  │ ② Resource: DEPENDENT (hoàn toàn phụ thuộc bố mẹ)              │
  │ ③ Freedom: DEPENDENT (bố mẹ quyết tất cả)                      │
  │ ④ Awareness: INVISIBLE (không biết cách sống khác tồn tại)     │
  │                                                                   │
  │ ⭐ CẢ 4 TRỤC THẤP → ACTION SPACE ≈ 0:                            │
  │ Không frustration vì invisible constraint → không biết → ở yên  │
  │ KHI awareness tăng (lớn lên, gặp bạn, internet):               │
  │ ④ ↑ → thấy options → "tại sao mình bị ép?" → frustration BẮT ĐẦU│
  │ → Break possible NHƯNG trục ②③ vẫn dependent → conflict         │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 5: "Trúng số"                                            │
  │ ① Capacity: KHÔNG ĐỔI (tiền không mua skill)                    │
  │ ② Resource: BÙNG NỔ (tiền expand đột ngột)                     │
  │ ③ Freedom: TĂNG (ít dependency, ít obligation tài chính)        │
  │ ④ Awareness: KHÔNG ĐỔI (không biết làm gì với tiền)            │
  │                                                                   │
  │ ⭐ TRỤC ② BÙNG NỔ + TRỤC ①④ KHÔNG THEO KỊP:                      │
  │ Gap-Distribution CHƯA KỊP SHIFT → "giàu nhưng không biết muốn gì"           │
  │ Options expand đột ngột nhưng gaps vẫn ở body-domain            │
  │ → Over-consume body-domain fills → hedonic adaptation → empty   │
  │ Reward-Calibration §3.4: premature access → bypass process      │
  └───────────────────────────────────────────────────────────────────┘

  ⚠️ CÁC PROFILE NÀY LÀ SIMPLIFIED. Thực tế = nuanced hơn nhiều.
     Dùng để ILLUSTRATE trục, KHÔNG để categorize người.
```

---

## §3 — 3 LOẠI CONSTRAINT

### §3.0 — Tổng quan

```
⭐⭐ 3 LOẠI CONSTRAINT — KHÁC CĂN BẢN VỀ TRẢI NGHIỆM CỦA NGƯỜI TRONG CUỘC:

  Cùng 1 option bị thiếu. 3 lý do KHÁC NHAU. 3 trải nghiệm KHÁC NHAU.

  ┌────────────┬──────────────────┬──────────────┬──────────────────────┐
  │ Loại       │ Mechanism        │ Cảm giác     │ Observable           │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ BLOCKED    │ Biết option,     │ Frustration  │ "Tôi biết có cách   │
  │            │ KHÔNG ĐƯỢC phép  │ Tức giận     │ nhưng không được phép"│
  │            │ (trục ③ chặn)   │ Phản kháng   │ → Protest, circumvent│
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ DEPENDENT  │ Biết option,     │ Chấp nhận    │ "Tôi biết có cách   │
  │            │ CHƯA ĐỦ resource │ tạm thời     │ nhưng chưa đủ       │
  │            │ (trục ② thiếu)  │ Kế hoạch     │ điều kiện" → Plan    │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ INVISIBLE  │ KHÔNG BIẾT option│ KHÔNG CẢM GÌ │ Không có hành vi nào │
  │            │ tồn tại          │ (no gap)     │ liên quan đến option │
  │            │ (trục ④ = 0)    │ Bình yên giả │ → Silent absence     │
  └────────────┴──────────────────┴──────────────┴──────────────────────┘
```

### §3.1 — Blocked: biết nhưng không được phép

```
⭐ BLOCKED = FRUSTRATION:

  Mechanism:
    → Person BIẾT option X tồn tại (trục ④ có awareness)
    → Person CÓ capacity/resource cho X (trục ①② đủ)
    → NHƯNG trục ③ CHẶN: luật cấm, norm cấm, người khác ngăn
    → → Gap EXISTS + fill path EXISTS + BLOCKED = frustration

  VÍ DỤ:
    → Muốn kinh doanh nhưng luật cấm tư nhân (VN trước Đổi Mới)
    → Muốn học đại học nhưng "con gái không cần học" (norm)
    → Muốn ly hôn nhưng "nghĩ đến con" (obligation)
    → Muốn tham gia chính trị nhưng "không có background" (status gate)

  BODY RESPONSE:
    → Frustration = cortisol sustained (gap fire + fill path blocked)
    → Lâu dài: có thể → protest / circumvent / suppress
    → 🟢 Dollard et al. 1939: frustration → aggression hypothesis

  ⭐ BLOCKED = CÓ ENERGY → có thể RESOLVE:
    → Vì biết option + biết bị chặn → CÓ TARGET để giải quyết
    → Lobbying, advocacy, legal challenge, migration = strategies
    → = SOLVABLE (dù costly)
```

### §3.2 — Dependent: biết nhưng chưa đủ điều kiện

```
⭐ DEPENDENT = TEMPORARY ACCEPTANCE:

  Mechanism:
    → Person BIẾT option X tồn tại (trục ④ có awareness)
    → Person KHÔNG ĐỦ resource cho X (trục ② thiếu)
    → HOẶC chưa đủ capacity (trục ① thiếu)
    → → Gap EXISTS + fill path EXISTS + CHƯA ĐỦ CONDITIONS = acceptance tạm

  VÍ DỤ:
    → Muốn mở nhà hàng nhưng chưa đủ vốn → tiết kiệm → chờ
    → Muốn nghiên cứu PhD nhưng chưa đủ kiến thức → học thêm → chờ
    → Muốn rời nhà nhưng chưa đủ tuổi/thu nhập → build capacity → chờ

  BODY RESPONSE:
    → Cortisol MODERATE (gap fire + fill path known + timeline unclear)
    → PFC có thể PLAN: "nếu tôi tiết kiệm X tháng → đủ"
    → → Cortisol GIẢM khi plan exist (certainty ↑)

  ⭐ DEPENDENT = CÓ HƯỚNG → MOTIVATING:
    → Biết option + biết thiếu gì → CÓ DIRECTION để build
    → = Source of drive, not despair
    → Education, mentorship, resource building = strategies
    → = SOLVABLE given TIME
```

### §3.3 — Invisible: không biết option tồn tại

```
⭐⭐ INVISIBLE = NGUY HIỂM NHẤT — VÌ KHÔNG CÓ CẢM GIÁC GÌ:

  Mechanism:
    → Person KHÔNG BIẾT option X tồn tại (trục ④ = 0 cho X)
    → → "Chưa biết = không có gap" (Gap-Direction §5.3)
    → → KHÔNG CÓ GAP cho X → KHÔNG CÓ DRIVE hướng X
    → → KHÔNG CÓ FRUSTRATION → KHÔNG CÓ ENERGY ĐỂ TÌM
    → → = "BÌNH YÊN GIẢ" — không biết mình đang bị giới hạn

  VÍ DỤ:
    → Nông dân thế kỷ 18: không biết "quyền bầu cử" tồn tại → không đòi
    → Trẻ bị ép: không biết "trẻ em có quyền" → chấp nhận
    → Công nhân: không biết "online course miễn phí" tồn tại → không học
    → Người bệnh: không biết "liệu pháp X" tồn tại → không tìm

  BODY RESPONSE:
    → KHÔNG CÓ. Đây là VẤN ĐỀ.
    → Frustrated person TÌM giải pháp (energy có).
    → Dependent person BUILD toward giải pháp (direction có).
    → Invisible person KHÔNG LÀM GÌ — vì KHÔNG CÓ GAP.
    → = TẠI SAO invisible là NGUY HIỂM NHẤT:
      Blocked = đau → tìm cách
      Dependent = chờ → build
      Invisible = bình yên → stuck FOREVER (nếu không ai "mở mắt")

  ⭐ INVISIBLE → VISIBLE: MOMENT CỦA "Ồ":
    → 1 cuộc trò chuyện: "Bạn biết có scholarship du học không?"
      → ④ expand → gap HÌNH THÀNH → frustration/motivation BẮT ĐẦU
    → 1 cuốn sách: "Có career path này tồn tại"
      → ④ expand → new option VISIBLE → decision possible
    → Internet exposure: xem video về cuộc sống KHÁC
      → ④ expand → awareness: "cuộc sống có thể KHÁC thế này"
    → = CHEAPEST intervention (cost = 1 conversation)
      BUT HARDEST to trigger (invisible = can't search for what you don't know)

  ⭐ EDUCATION = ANTI-INVISIBLE MECHANISM:
    → Education KHÔNG CHỈ dạy skill (trục ①)
    → Education CHÍNH YẾU chuyển INVISIBLE → VISIBLE (trục ④)
    → → Options INVISIBLE → BLOCKED hoặc DEPENDENT
    → → BLOCKED/DEPENDENT = SOLVABLE (vì biết problem + direction)
    → → = TẠI SAO "giáo dục là nền tảng phát triển" (Sen 1999)

🟢 "Chưa biết = không có gap": Gap-Direction §5.3 (established)
🟢 Capability = opportunity set: Sen 1999 (Nobel)
🟡 Invisible constraint taxonomy + "bình yên giả" = framework synthesis
🔴 Invisible constraint = most dangerous (logical, untested empirically)
```

---

## §4 — SPIRAL DYNAMICS

### §4.1 — Positive spiral (privilege, compound advantage)

```
⭐ 4 TRỤC TƯƠNG TÁC → POSITIVE SPIRAL:

  ① → ②: Knowledge MỞ RỘNG resource access
    → Biết tiếng Anh → thị trường rộng hơn → income + network
    → Biết luật → negotiate tốt hơn → access legal resources
    → Deep domain skill → high-value output → more money

  ② → ①: Resource MỞ RỘNG knowledge
    → Có tiền → access giáo dục → compile faster
    → Có network → mentors → compile guided → faster + deeper
    → Có tools → practice efficiently → compile better

  ③ → ①②: Freedom ENABLES sử dụng ① và ②
    → Tự do thời gian → dùng capacity CỦA MÌNH → build more
    → Tự do tài chính → invest resources → grow portfolio
    → = Bị giam → ①② vô nghĩa (capacity VẪN CÓ nhưng KHÔNG DÙNG ĐƯỢC)

  ④ → ①②③: Awareness ACTIVATES tất cả
    → Biết options tồn tại → tìm capacity, resource, freedom
    → Biết mình có thể → DÙNG ①②③ thay vì ignore
    → = Không biết mình có thể → stuck (dù ①②③ đủ)

  POSITIVE SPIRAL:
    ① ↗ → ② ↗ → ③ ↗ → ④ ↗ → ① ↗↗ → ② ↗↗ ...
    VD: Có education → có job → có tiền → có tự do → biết thêm options
        → education thêm → job tốt hơn → ...

  = "PRIVILEGE" = positive spiral CẢ 4 trục đồng thời
  = COMPOUND ADVANTAGE — mỗi trục reinforce trục khác

🟢 Heckman 2006: early childhood intervention compound returns
🟢 Bourdieu 1986: capital reproduction across generations
🟡 4-axis positive spiral = framework synthesis
```

### §4.2 — Negative spiral (poverty trap)

```
⭐ NGƯỢC LẠI → NEGATIVE SPIRAL:

  ① ↘ → ② ↘ → ③ ↘ → ④ ↘ → ① ↘↘ ...

  VD: Ít education → ít skill → ít income → ít freedom (nợ, phụ thuộc)
      → ít awareness (không biết options) → ít education thêm → ...

  = "POVERTY TRAP" = negative spiral CẢ 4 trục đồng thời
  = COMPOUND DISADVANTAGE — mỗi trục kéo trục khác xuống

  ⭐ INVISIBLE CONSTRAINT LÀM TRAP KÍN HƠN:
    → Negative spiral + invisible constraint = KHÔNG BIẾT MÌNH BỊ TRAP
    → Blocked: đau → tìm cách ra
    → Invisible: "cuộc sống mọi người đều thế" → ở yên → trap deepen

🟢 Poverty trap: established development economics concept
🟢 Compound disadvantage: Wilson 1987 (The Truly Disadvantaged)
🟡 4-axis negative spiral + invisible amplification = framework synthesis
```

### §4.3 — Intervention points

```
🟡 INTERVENTION PER TRỤC — ASYMMETRIC COST:

  ┌────────────┬──────────────────┬──────────────┬──────────────────────┐
  │ Trục       │ Intervention     │ Cost         │ Timeframe            │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ① Capacity │ Education,       │ HIGH         │ YEARS                │
  │            │ training, mentor │ (time+effort)│ (compile takes time) │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ② Resource │ Financial aid,   │ VARIABLE     │ IMMEDIATE-MEDIUM     │
  │            │ network access,  │ (depends on  │ (money = fast,       │
  │            │ infrastructure   │ amount)      │ network = slow)      │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ③ Freedom  │ Legal reform,    │ VERY HIGH    │ SYSTEMIC             │
  │            │ social change,   │ (collective  │ (generations)        │
  │            │ debt relief      │ action)      │                      │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ④ Awareness│ Exposure, travel │ CHEAPEST     │ SUDDEN POSSIBLE      │
  │            │ conversation,    │ (1 convo     │ (1 moment can change │
  │            │ internet, mentor │ can change)  │ everything)          │
  └────────────┴──────────────────┴──────────────┴──────────────────────┘

  ⭐ TRỤC ④ PARADOX:
    → Cheapest intervention WHEN IT WORKS
    → Hardest to TRIGGER: invisible = can't search for what you don't know
    → CẦN: external catalyst (teacher, friend, internet, mentor)
    → = TẠI SAO "gặp đúng người" can change a life

  ⭐ INTERVENTION TỐI ƯU = ④ + ① ĐỒNG THỜI:
    → Mở mắt (④) + build capacity (①) → feedback loop BẮT ĐẦU
    → Resource (②) follows as consequence
    → Freedom (③) may need systemic support
    → = Sen 1999: development = expanding capabilities (= expanding Action-Space)

🟢 Education as development: Sen 1999, Heckman 2006
🟡 Intervention per axis + ④ paradox = framework synthesis
```

---

## §5 — FORMATION MODEL

### §5.0 — Tổng quan: Action-Space hình thành từ đâu

```
⭐⭐ ACTION SPACE = f(4 TẦNG CHỒNG LÊN NHAU):
  (Parallel Gap-Distribution §4 — 4 tầng cho DEMAND, file này 4 tầng cho SUPPLY)

  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG 4: COLLECTIVE INFRASTRUCTURE (slowest, widest)             │
  │   Kinh tế, công nghệ, hệ thống nào TỒN TẠI?                   │
  │   → DEFINE: options nào AVAILABLE cho population                │
  │   → VN 1960: abstract-domain capacity gần như KHÔNG BUILD ĐƯỢC  │
  │     (chưa có đại học phổ cập, internet, global market)          │
  │   → VN 2026: internet + AI → options EXPAND cho mọi người      │
  │   → Silicon Valley: startup infrastructure → entrepreneurship   │
  │     options ABUNDANT                                             │
  └────────────────────────────┬────────────────────────────────────┘
                               ▼ filter qua social position
  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG 3: SOCIAL POSITION (medium, medium-wide)                   │
  │   Sinh ra ở đâu? Gia đình nào? Class nào?                      │
  │   → FILTER: ai ACCESS options nào trong population              │
  │   → Con nhà giàu: trục ② cao TỪ ĐẦU (inherited resources)    │
  │   → Con nhà nghèo: trục ② thấp → negative spiral risk         │
  │   → Con nhà có học: trục ①④ accelerated (guided compile)      │
  │   (Bourdieu 1986: economic + social + cultural capital reproduce)│
  └────────────────────────────┬────────────────────────────────────┘
                               ▼ shape qua education + family
  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG 2: EDUCATION + FAMILY (faster, narrower)                   │
  │   Trường nào? Bố mẹ dạy gì? Exposure domains nào?             │
  │   → BUILD: specific capacity + awareness + initial resources    │
  │   → Trường tốt → ① expand + ④ expand (exposure + meta-cog)   │
  │   → Bố mẹ encourage → ④ accurate, self-efficacy compile       │
  │   → Bố mẹ restrict → ④ under-estimate, learned helplessness   │
  │   → = "Vạch xuất phát" action space cho mỗi cá nhân            │
  └────────────────────────────┬────────────────────────────────────┘
                               ▼ interact with hardware
  ┌─────────────────────────────────────────────────────────────────┐
  │ TẦNG 1: HARDWARE + ACCUMULATED EXPERIENCE (fastest, narrowest)  │
  │   DRD4, COMT, health, direct experience, compile history        │
  │   → MODIFY: action space từ initial point                       │
  │   → Hardware bias: DRD4 breadth → explore more → ④ expand      │
  │   → Direct experience: try → fail/succeed → ①④ calibrate      │
  │   → Years of practice → ① deepen in specific domains           │
  │   → = Personal trajectory WITHIN social constraints             │
  └─────────────────────────────────────────────────────────────────┘

  4 TẦNG ĐỒNG THỜI, KHÔNG TÁCH RỜI.
  Mỗi tầng = constraint + install + opportunity.
  Output = THIS PERSON'S action space AT THIS MOMENT.

🟢 Social reproduction: Bourdieu 1986 (economic + social + cultural capital)
🟢 Early childhood ROI: Heckman 2006
🟡 4-tầng formation as parallel to Gap-Distribution = framework synthesis
```

---

## §6 — SHIFT MECHANISMS

### §6.1 — Trục ① (Capacity) shift: takes YEARS

```
⭐ COMPILED CAPACITY EXPAND = CHUNK COMPILATION:

  Mechanism:
    → Exposure → chunks accumulate → compile → capacity INCREASE
    → = SAME mechanism as gap formation (Gap-Direction §6)
    → Takes time: domain expertise = 5-10+ years deliberate practice

  CAN'T SHORTCUT:
    → Tiền mua courses nhưng KHÔNG mua compile time
    → AI accelerate learning nhưng KHÔNG skip compilation
    → = Chunks phải compile qua REPEATED EXPOSURE, not instantaneous

  ASYMMETRY: expand SLOWER than contract
    → Build: years of practice
    → Lose: disuse → decay (Chunk §3.3 anchor decay)
    → Health crisis → physical capacity crash FAST
    → = Build slow, lose fast = asymmetric risk

🟢 Deliberate practice: Ericsson 2006
🟢 Chunk compilation requires time: established cognitive science
```

### §6.2 — Trục ② (Resource) shift: VARIABLE

```
⭐ RESOURCE ACCESS CAN CHANGE FAST OR SLOW:

  FAST EXPAND:
    → Lottery, inheritance, sudden income
    → Meet influential person → network expand
    → Technology access (get smartphone → internet → world)

  SLOW BUILD:
    → Savings accumulate over years
    → Network build through repeated interactions
    → Career progression → income increase gradually

  FAST CRASH:
    → Job loss → income → 0
    → Divorce → network split
    → Economic crisis → savings destroyed
    → Health → medical cost → resource drain

  = MOST VOLATILE trục — subject to external events
```

### §6.3 — Trục ③ (Freedom) shift: DEPENDS ON EXTERNAL

```
⭐ FREEDOM SHIFT = LARGELY OUTSIDE INDIVIDUAL CONTROL:

  SYSTEMIC CHANGE:
    → Legal reform → population freedom ↑ (VN Đổi Mới 1986)
    → Social norm shift → invisible constraints ↓ (women's rights)
    → Technology → new freedoms (internet bypass information barriers)
    → = Individual BENEFIT from systemic change

  INDIVIDUAL CHANGE:
    → Pay off debt → financial freedom ↑
    → Children grow up → obligation reduce → freedom ↑
    → Leave toxic relationship → freedom ↑
    → = Possible but COSTLY (mode shift, access cost — Obligation §6)

  = Trục ③ = individual có LEAST CONTROL (so với ①②④)
```

### §6.4 — Trục ④ (Awareness) shift: SUDDEN POSSIBLE

```
⭐⭐ AWARENESS = TRỤC CÓ THỂ SHIFT ĐỘT NGỘT NHẤT:

  SUDDEN EXPAND:
    → 1 cuộc trò chuyện: "Bạn biết có career path này không?"
    → 1 cuốn sách: paradigm shift trong thinking
    → 1 chuyến đi: thấy cuộc sống KHÁC → "có thể thế này sao?"
    → Internet exposure: YouTube, social media → worlds unveiled
    → Mentor gặp đúng thời điểm: "bạn có khả năng này, bạn biết không?"

  PARADOX CỦA TRỤC ④:
    → CHEAPEST per unit: 1 cuộc nói chuyện = $0
    → HARDEST to trigger: invisible = can't search for what you don't know
    → CẦN EXTERNAL CATALYST: ai đó phải "mở mắt" cho bạn
    → AI ERA: AI có thể detect invisible constraints + suggest options
      → = New awareness catalyst at scale (AI-Schema-Detection §6 potential)

  AWARENESS EXPAND ≠ CAPACITY EXPAND:
    → ④ expand: "ồ, có Python tồn tại" = instant
    → ① expand: "tôi biết Python" = months/years of compile
    → = ④ MỞ CỬA, ① cần THỜI GIAN ĐI QUA CỬA
    → = TẠI SAO ④ + ① phải đi ĐỒNG THỜI cho effective intervention

🟡 Awareness sudden shift = framework synthesis
🟡 ④ paradox (cheapest + hardest) = framework insight
```

### §6.5 — Crisis → collapse → rebuild

```
⭐ MAJOR CRISIS CÓ THỂ CRASH NHIỀU TRỤC ĐỒNG THỜI:

  VD: Mất việc + ly hôn + bệnh:
    ① → Capacity vẫn còn nhưng context-dependent (skill ở industry cũ)
    ② → Resource crash (income → 0, network split, medical cost)
    ③ → Freedom crash (debt, obligation, dependency tăng)
    ④ → Awareness CÓ THỂ TĂNG (crisis = "forced perspective shift")

  ⭐ CRISIS CÓ 2 MẶT:
    → CRASH: multiple trục ↘ đồng thời → negative spiral risk
    → RESET: ④ awareness tăng do forced exposure →
      "tôi đã sống SAI" → new direction possible
    → = Giống Gap-Distribution §3.4: "LOCKED + MISMATCHED → reality FORCES shift"
    → = Crisis = PAINFUL nhưng CAN lead to realignment

🟡 Crisis as reset mechanism = framework synthesis
🟢 Post-traumatic growth: Tedeschi & Calhoun 2004
```

---

## §7 — EXPANSION QUALITY: DEPTH-FIRST PRINCIPLE

### §7.1 — Core paradox: more awareness ≠ more capability

```
⭐⭐ NGHỊCH LÝ: MỞ RỘNG ACTION SPACE KHÔNG PHẢI LÚC NÀO CŨNG TỐT.

  §4 mô tả positive spiral: 4 trục tăng → compound advantage.
  §6 mô tả shift mechanisms: mỗi trục expand thế nào.
  NHƯNG: expand THẾ NÀO matters hơn expand BAO NHIÊU.

  VÍ DỤ:
    Người A: đọc nhiều, biết IT, finance, design, marketing, cooking,
    music... mỗi thứ học 1 tuần rồi nhảy sang thứ mới.
    → Trục ④ (awareness) RỘNG: biết 10 domains tồn tại
    → Trục ① (capacity) NÔNG: mỗi domain ≈ 0 khả năng thực thi
    → = BIẾT 100 CÁNH CỬA, MỞ ĐƯỢC 0

    Người B: cùng thời gian → compile SÂU 1 domain duy nhất (code).
    → Trục ④ HẸP: chỉ biết 1-2 domains
    → Trục ① SÂU: code proficient → CÓ THỂ thực thi
    → = BIẾT 2 CÁNH CỬA, MỞ ĐƯỢC 1

    AI LÀM ĐƯỢC NHIỀU HƠN?
    → Người B: ít options nhưng CÓ CAPACITY THẬT → hành động → reward → compound
    → Người A: nhiều options nhưng KHÔNG CAPACITY → paralysis → frustration

  ⭐ NGHỊCH LÝ CỦA AWARENESS:
    → Trục ④ expand → nhiều domain VISIBLE → nhiều gap HÌNH THÀNH
      (vì "biết domain tồn tại = gap bắt đầu form" — Gap-Direction §5.3 ngược)
    → Nhưng trục ① KHÔNG expand cùng tốc độ (compile takes YEARS — §6.1)
    → = Awareness MỞ NHANH, capacity build CHẬM
    → = Gap-Distribution expand (nhiều gap) + Action-Space mismatch (capacity nông) = FRUSTRATION
    → = WORSE than invisible constraint:
      Invisible: không biết → bình yên (§3.3)
      Broad-shallow: biết MỌI THỨ mình KHÔNG CÓ → chronic frustration

🟡 Awareness-capacity mismatch = framework synthesis
🟢 Choice overload → paralysis: Schwartz 2004, Iyengar & Lepper 2000
```

### §7.2 — Threshold as gate: "potential" vs "real" action space

```
⭐ KHÔNG PHẢI MỌI AWARENESS ĐỀU LÀ "REAL" ACTION SPACE:

  Domain-Mapping-Drive §2.3 + Gap-Distribution §6.1 established:
    → THRESHOLD = critical mass of chunks cần để gap FORM
    → BEFORE threshold: no gap → no drive → no reward → PFC phải ÉP mỗi lần
    → AFTER threshold: gap formed → drive → reward → SELF-SUSTAINING

  ÁP DỤNG VÀO ACTION SPACE:

    POTENTIAL Action-Space (pre-threshold):
      → Biết domain tồn tại (trục ④ có)
      → Nhưng chưa compile đủ chunks để THỰC THI (trục ① chưa đủ)
      → Mỗi lần muốn dùng → PFC phải DRAFT từ đầu → COSTLY
      → = "Biết có Python" nhưng chưa thể code Python
      → = Options VISIBLE nhưng NOT EXECUTABLE

    REAL Action-Space (post-threshold):
      → Đã compile đủ → gap formed → reward loop → self-sustaining
      → Dùng capacity này = LOW COST (compiled, automatic)
      → = "Biết Python VÀ code được Python"
      → = Options VISIBLE VÀ EXECUTABLE

  ⭐ ACTION SPACE QUALITY = POST-THRESHOLD / TOTAL AWARENESS:
    → Người A: 10 domains biết, 0 post-threshold → quality ≈ 0
    → Người B: 2 domains biết, 1 post-threshold → quality CAO
    → Người C: 10 domains biết, 3 post-threshold → quality TỐT (T-shaped)
    → = File này mô tả Action-Space SIZE (§2). Section này thêm Action-Space QUALITY.

🟢 Threshold → self-sustaining drive: Domain-Mapping-Drive §2.3
🟢 Deliberate practice → expertise: Ericsson 2006
🟡 Potential vs Real Action-Space = framework synthesis
```

### §7.3 — 4 Expansion Profiles

```
⭐ 4 PROFILES — TÙY DEPTH × BREADTH ALLOCATION:

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ SCATTERED EXPLORER   │ ④ broad + ① shallow EVERYWHERE              │
  │                      │                                              │
  │ Biết nhiều domain → 0 domain post-threshold                       │
  │ → No self-sustaining drive ở BẤT KỲ domain                        │
  │ → Choice overload: N options → PFC overload → can't commit         │
  │ → Mỗi domain: PFC phải ÉP → costly → burnout → nhảy domain mới   │
  │   → lặp lại → "cái gì cũng biết, cái gì cũng dở"                 │
  │                                                                    │
  │ Gap-Distribution §3.3: many-shallow. Domain-Mapping-Drive §2.3: dưới threshold TẤT CẢ.          │
  │ Schwartz 2004: paradox of choice.                                  │
  │                                                                    │
  │ ⚠️ TRAP: giống "học hỏi" nhưng thực ra = avoid depth              │
  │ (depth = PFC sustained effort = uncomfortable PRE-threshold)       │
  │ → Surface novelty reward per domain mới → nhảy domain =            │
  │   novelty loop ở meta-level                                        │
  └─────────────────────┴──────────────────────────────────────────────┘

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ DEEP SPECIALIST      │ ④ narrow + ① DEEP in 1                      │
  │                      │                                              │
  │ 1 domain post-threshold → Background-Pattern locked → self-sustaining drive        │
  │ → 5 mechanisms lock (Gap-Distribution §6.3): gap tự sinh, reward memory,        │
  │   identity locked, depth×specificity trap                          │
  │ → PRODUCTIVE + SUSTAINABLE nhưng VULNERABLE:                       │
  │   domain obsolete → capacity suddenly worthless                    │
  │   blind spots outside domain → missed opportunities               │
  └─────────────────────┴──────────────────────────────────────────────┘

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ T-SHAPED EFFECTIVE   │ ④ broad + ① DEEP in 1-2 + moderate 3-5      │
  │                      │                                              │
  │ Deep domain(s) = EXECUTION BASE (post-threshold, self-sustaining)  │
  │ Moderate domains = BRIDGE (enough chunks to communicate, direct)   │
  │ Broad awareness = SEE CONNECTIONS (④ informs ① direction)          │
  │                                                                    │
  │ KHÔNG THỬ EXECUTE Ở MỌI DOMAIN — execute ở deep,                  │
  │ observe + direct ở broad.                                          │
  │                                                                    │
  │ VD: Jensen Huang = deep semiconductor/AI + broad business/market   │
  │ VD: Designer = deep integration + moderate code + moderate art     │
  │ Gap-Distribution §3.3: T-shaped. Chase & Simon 1973: expertise + bridge.        │
  └─────────────────────┴──────────────────────────────────────────────┘

  ┌─────────────────────┬──────────────────────────────────────────────┐
  │ SERIAL DEPTH         │ ④ expanding + ① SEQUENTIAL deep              │
  │                      │                                              │
  │ Deep A → cross threshold → THEN explore B → deep B → THEN C       │
  │ Each depth BUILDS ON previous (transfer patterns, meta-skills)     │
  │ → Polymath pattern: depth → breadth FROM depth → new depth         │
  │                                                                    │
  │ REQUIRES: time (mỗi domain = years) + deliberate transition        │
  │ RARE nhưng powerful khi có: Leonardo, Elon Musk                    │
  │ (Musk: PayPal → SpaceX → Tesla = serial depth, not scatter)       │
  │                                                                    │
  │ ⭐ KEY: KHÔNG đồng thời shallow — SEQUENTIAL deep.                  │
  │ = Depth-first MỖI LẦN, nhưng NHIỀU LẦN qua đời.                  │
  └─────────────────────┴──────────────────────────────────────────────┘

  ⚠️ PROFILES = simplified. Most people = MIX, shift over time.
```

### §7.4 — Depth-first principle: roots before branches

```
⭐⭐ TẠI SAO DEPTH-FIRST = OPTIMAL EXPANSION STRATEGY:

  ① THRESHOLD = IGNITION POINT (Domain-Mapping-Drive §2.3):
    → Trước threshold: learning = PFC ÉP = costly = dễ bỏ
    → Sau threshold: learning = self-sustaining drive = FREE
    → = PHẢI vượt threshold ở ÍT NHẤT 1 domain trước khi mở rộng
    → = Không vượt threshold nào = every domain = costly = scattered

  ② BACKGROUND PATTERN = STABILIZER (Background-Pattern §8):
    → Compile deep → Background-Pattern forms "tôi = người domain X" → STABLE IDENTITY
    → Stable identity → explore outward = LOW RISK (anchor để trở về)
    → Không stable identity → explore = HIGH RISK (drift, no anchor)

  ③ DEPTH ENABLES BREADTH (transfer patterns):
    → Deep compile → meta-skills: "how to learn" not just "what I know"
    → Physics deep → transfer pattern recognition TO biology, economics
    → Code deep → transfer systematic thinking TO design, business
    → = Depth in 1 KHÔNG giới hạn ở 1 — nó ARM cho nhiều domains

  ④ REWARD MEMORY SUSTAINS (Gap-Distribution §6.3 ②):
    → Deep domain → body compiled: [deep gap fill = MASSIVE opioid]
    → Reward memory = FUEL cho continued effort
    → Scattered = no deep reward memory → no fuel → PFC phải supply mãi

  ⭐ ANALOGY — CÂY:
    → Rễ sâu + thân chắc → cành MỞ RỘNG an toàn → gió không đổ
    → Không rễ + cành khắp nơi → gió nhẹ → ĐỔ
    → Rễ = depth (post-threshold domain). Cành = breadth (awareness expand).
    → = ROOT-FIRST, THEN BRANCH.

🟢 Threshold → self-sustaining: Domain-Mapping-Drive §2.3, §5 (Einstein = 15-17 tuổi)
🟢 Background-Pattern self-reinforcing: Background-Pattern §8
🟢 Transfer of expertise: established cognitive science
🟡 Depth-first as optimal expansion strategy = framework synthesis
```

### §7.5 — Premature expansion (parallel Reward-Calibration §3.4)

```
⭐ PREMATURE EXPANSION = PARALLEL CỦA PREMATURE COMPILATION:

  Reward-Calibration §3.4 established:
    → Over-reward forces chunks compile BEFORE sufficient foundation
    → → Chunks skew from start → cascade

  PREMATURE EXPANSION = TƯƠNG TỰ:
    → Options VISIBLE trước khi capacity READY
    → → Gaps form (vì biết domain) BEFORE chunks sufficient
    → → TRY nhưng FAIL (vì nông) → compile: "domain này tôi dở"
    → → Skewed conclusion: "tôi không hợp" (thực ra: chưa ĐỦ chunks)
    → → Quit → next domain → repeat → "cái gì cũng thử, cái gì cũng bỏ"

  VÍ DỤ:
    → Sinh viên thử 5 ngành trong 2 năm: mỗi ngành < threshold →
      kết luận "tôi không có đam mê" → thực ra = chưa compile ĐỦ ở ngành NÀO
    → Person đọc self-help → biết 20 strategies → try each 1 tuần →
      none works → "self-help vô dụng" → thực ra = premature expansion
    → Người mới vào gym thử 10 môn/tháng → mỗi môn chưa đủ để thấy kết quả
      → "tập gym vô ích" → thực ra = chưa qua threshold ở BẤT KỲ môn nào

  ⭐ PHÂN BIỆT QUAN TRỌNG:
    → "Chán vì mismatch" (hardware thật sự không hợp) ≠ "Chán vì pre-threshold"
    → Cả 2 CẢM GIÁC GIỐNG NHAU: bored, drained, "không thích"
    → KHÁC: mismatch → càng compile càng DRAIN. Pre-threshold → sau threshold → ENJOY.
    → Domain-Mapping-Drive §2.3: "below threshold = learning feels like torture.
      Above threshold = learning feels like play."
    → = "Chưa thích ≠ không hợp. Có thể = chưa đủ chunks."

🟡 Premature expansion = framework synthesis (parallel Reward-Calibration §3.4)
🟢 Threshold ↔ enjoyment: Domain-Mapping-Drive §2.3
```

### §7.6 — Self-calibration: domain feedback = only arbiter

```
⭐ LÀM SAO BIẾT ĐANG EXPAND ĐÚNG HƯỚNG?

  Logic-Feeling-Balance.md: KHÔNG THỂ prescribe → domain feedback = only arbiter.
  ÁP DỤNG: KHÔNG THỂ prescribe expansion direction → chỉ OBSERVE signals.

  3 SIGNALS TỪ BODY (sau khi STAY ĐỦ LÂU — vượt hoặc gần threshold):

    ① APPROACH SIGNAL KHI ENGAGE:
      → Body approach (curious, energized) khi làm = domain FIT hardware
      → Body avoidance (bored, drained) khi làm = domain MISMATCH
      → ⚠️ PRE-THRESHOLD: cả 2 signals UNRELIABLE
        (chưa đủ chunks → no gap → "chán" có thể = chưa vượt threshold)
      → POST-THRESHOLD: signals RELIABLE (gap formed → body vote clear)

    ② COMPOUND REWARD OVER TIME:
      → Đúng hướng: reward per session TĂNG (deeper gap → bigger reward)
      → Sai hướng: reward per session GIẢM (shallow → habituate → chán)
      → = "Càng làm càng thích" = đúng. "Càng làm càng chán" = sai HOẶC chưa đủ.

    ③ TRANSFER PATTERNS EMERGE:
      → Đúng hướng: connections sang domains khác ("ồ physics giống economics")
      → = Depth ENRICHING breadth naturally
      → Sai hướng: isolated, no connections → narrow without bridge value

  ⭐ PRACTICAL OBSERVATION:
    → Thử domain → STAY ĐỦ LÂU (vượt threshold) → THEN evaluate
    → "Đủ lâu" ≈ tùy domain (code ~6-12 tháng, physics ~2-3 năm)
    → Evaluate: approach signal + compound reward + transfer patterns?
    → YES → go deeper (depth-first)
    → NO (after sufficient time) → pivot to different domain (KHÔNG scatter)
    → = FRAMEWORK KHÔNG prescribe ĐÚNG hướng nào. Chỉ mô tả HOW observe.

🟡 Self-calibration via body signals = framework synthesis
🟢 Logic-Feeling-Balance: domain feedback = only arbiter (established framework)
```

---

## §8 — Gap-Distribution × Action-Space: BEHAVIORAL PREDICTION (mở rộng §1.3)

```
⭐⭐ Gap-Distribution VÀ Action-Space ẢNH HƯỞNG LẪN NHAU — FEEDBACK LOOP:

  Action-Space → Gap-Distribution (supply shapes demand):
    → Action-Space expand → new domains accessible → new chunks compile → new gaps form → Gap-Distribution SHIFT
    → VD: Sinh viên vào lab → access new domain → chunks compile →
      gap "muốn nghiên cứu sâu hơn" HÌNH THÀNH → Gap-Distribution shift toward abstract
    → = Action space expand CREATES new demand

  Gap-Distribution → Action-Space (demand shapes supply):
    → Gap-Distribution shift → new gaps → drive to build capacity → Action-Space expand
    → VD: Gap "muốn code giỏi" → invest time learning → capacity ↑ → Action-Space expand
    → = Demand DRIVES supply expansion

  → = BIDIRECTIONAL FEEDBACK LOOP
  → = TẠI SAO initial conditions matter (Heckman 2006):
    Early Action-Space expand → early Gap-Distribution shift → early feedback loop → compound advantage
    Late Action-Space expand → late Gap-Distribution shift → late start → catching up = harder


  ⭐ Gap-Distribution × Action-Space MISMATCH = CORE OF MANY LIFE PROBLEMS:

    MISMATCH TYPE 1: "Muốn mà không thể"
      → Gap-Distribution: gap rõ + fire mạnh
      → Action-Space: options không đủ
      → = Chronic frustration → learned helplessness risk
      → Fix: expand Action-Space (education, resources, awareness)

    MISMATCH TYPE 2: "Có thể mà không muốn"
      → Action-Space: options abundant
      → Gap-Distribution: gaps không match options available
      → = Drift, waste, "bored despite having everything"
      → Fix: expose to new domains → Gap-Distribution shift → gaps match Action-Space

    ALIGNED: "Muốn VÀ có thể"
      → Gap-Distribution gaps match Action-Space options → action → reward → compound
      → = Most productive, most fulfilling
      → = "Flow state" prerequisites: skill ≈ challenge (Csikszentmihalyi 1990)


🟡 Gap-Distribution ↔ Action-Space bidirectional feedback = framework synthesis
🟢 Flow: skill ≈ challenge: Csikszentmihalyi 1990
🟢 Initial conditions compound: Heckman 2006
```

---

## §9 — CASES

### §8.1 — Case: Bố mẹ-con (bài bo-me-va-con.txt)

```
🟡 CASE FROM REAL CONVERSATION (research-preference/bo-me-va-con.txt):

  SITUATION: Con không tâm sự với bố mẹ. Tại sao?

  ACTION SPACE ANALYSIS CỦA CON:
    ① Capacity: CÓ words, CÓ experiences muốn chia sẻ
    ② Resource: CÓ bố mẹ available
    ③ Freedom: RESTRICTED bởi PAST EXPERIENCES:
       → Nói ra → bị phán xét (anti-match) → compiled: "nói = unsafe"
       → Nói ra → bị lôi chuyện cũ → compiled: "nói = bị đào lại"
       → Nói ra → bị ngắt → compiled: "ý kiến tôi không quan trọng"
    ④ Awareness: CON BIẾT mình bị restrict nhưng KHÔNG biết cách thoát

  → ③ (Freedom) BỊ COMPILED CONSTRAINT:
    → Action space "tâm sự" TECHNICALLY tồn tại (①②④ đủ)
    → NHƯNG trục ③ bị compiled constraint: "tâm sự = unsafe"
    → = Blocked constraint DO BỐ MẸ TẠO (dù vô ý)

  BỐ MẸ FIXES = EXPAND CON'S TRỤC ③:
    → Nghe con nói hết (KHÔNG ngắt) → ③ expand: "nói = safe"
    → Không phán xét → ③ expand: "nói = không bị attack"
    → Không lôi chuyện cũ → ③ expand: "nói ≠ bị nhắc lại all mistakes"
    → = RESTORE action space "tâm sự" bằng cách REMOVE compiled constraints

  ⭐ INSIGHT: constraint CÓ THỂ DO NGƯỜI KHÁC TẠO
    (dù vô ý, dù yêu thương, vẫn = constrain action space)
```

### §8.2 — Case: 2 xã hội — cùng population, khác collective Action-Space

```
🟡 COLLECTIVE ACTION SPACE CASE:

  VN NÔNG THÔN 1960:
    Population Action-Space: ① nông nghiệp chuyên sâu ② tự cung tự cấp
    ③ norms rất chặt ④ chỉ biết 1 cách sống
    → Action space POPULATION ≈ narrow, stable, invisible trap

  SILICON VALLEY 2026:
    Population Action-Space: ① multi-domain, deep tech ② VC funding, global network
    ③ liberal, few restrictive norms ④ exposure to MANY ways of living
    → Action space POPULATION ≈ wide, dynamic, visible options

  = CÙNG LOÀI. CÙNG HARDWARE. KHÁC COLLECTIVE INFRASTRUCTURE.
  = Collective infrastructure = TẦNG 4 trong Formation Model (§5)
  = Individual Action-Space = f(collective Action-Space × social position × education × hardware)
```

### §8.3 — Case: Stephen Hawking — physical constraint + technology

```
🟡 PHYSICAL CONSTRAINT CASE:

  BEFORE ALS:
    ①②③④ = normal range → standard academic Action-Space

  AFTER ALS (progressive):
    ① Capacity: INTACT (physics knowledge vẫn còn)
    ② Resource: CRASH partially (need care, cost high)
    ③ Freedom: CRASH (body = prison, mobility ≈ 0)
    ④ Awareness: INTACT (biết mình có thể contribute)

  TECHNOLOGY COMPENSATE:
    → Wheelchair: partially restore ③ (mobility)
    → Voice synthesizer: partially restore ② (communication → network → output)
    → Research assistants: partially restore ② (collaboration)
    → = Technology = partial Action-Space RESTORE for ②③

  ⭐ KEY INSIGHT: ①④ VẪN CÒN → Gap-Distribution VẪN fire →
    Frustration when ②③ blocked + awareness ④ rằng "tôi CÓ THỂ"
    → Technology bridge Gap-Distribution ↔ Action-Space gap
    → Hawking productive BECAUSE ①④ high + technology compensate ②③
```

### §8.4 — Case: Gap-Distribution × Action-Space mismatch qua đời người

```
🟡 LIFECYCLE Action-Space × Gap-Distribution TRAJECTORY:

  CHILDHOOD (0-12):
    Gap-Distribution: shifting, exploring → Action-Space: low all axes (dependent)
    → = MATCHED at LOW: few gaps, few options → appropriate
    → Parent's job: EXPAND child's Action-Space gradually (education, exposure)

  ADOLESCENCE (12-20):
    Gap-Distribution: rapid shift, identity → Action-Space: expanding but uneven (①②③ growing)
    → = MISMATCHED: gaps forming FASTER than Action-Space grows → frustration
    → "Muốn nhiều thứ nhưng chưa thể" = typical teen experience

  YOUNG ADULT (20-30):
    Gap-Distribution: converging → Action-Space: expanding fast (education complete, career starts)
    → = ALIGNMENT FORMING: Gap-Distribution direction + Action-Space capacity start matching
    → "Quarter-life crisis" = Gap-Distribution chưa converge + Action-Space expanding → too many options

  MID-ADULT (30-50):
    Gap-Distribution: mostly locked → Action-Space: high (peak career, resources, freedom)
    → = BEST MATCH: know what want + can do it → productive peak
    → Risk: locked Gap-Distribution + shifting reality → mid-life crisis

  LATE ADULT (50+):
    Gap-Distribution: anchor exhausted? → Action-Space: declining (health, retirement)
    → = POTENTIAL MISMATCH: gaps change + capacity reduces
    → Meaning §2.2: "trống rỗng" khi anchor gone + Action-Space narrow
```

---

## §10 — RESEARCH ANCHORS

```
⭐ 16 RESEARCH ANCHORS — SUPPORT CÁC CLAIMS CỤ THỂ:

  ┌─────────────────────────────┬──────────────────────────────────────────┐
  │ Claim                       │ Research                                  │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Development = expanding     │ 🟢 Sen 1999 (Nobel) — Capability         │
  │ capabilities (freedoms)     │ Approach                                  │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Self-efficacy → behavior    │ 🟢 Bandura 1977 — Self-Efficacy Theory   │
  │ prediction                  │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Early intervention has      │ 🟢 Heckman 2006 — 7-10% annual ROI      │
  │ compound returns            │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Low competence →            │ 🟢 Kruger & Dunning 1999 — metacognitive │
  │ overestimate capability     │ deficit                                   │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Helplessness = DEFAULT,     │ 🟢 Maier & Seligman 2016 — vmPFC learns │
  │ controllability LEARNED     │ "controllable", DRN default              │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Autonomy, competence,       │ 🟢 Deci & Ryan 2000 — Self-Determination │
  │ relatedness as basic needs  │ Theory                                    │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Social brain = capacity     │ 🟢 Dunbar 1992, Zhou et al. 2005 —       │
  │ ceiling ~150                │ Social Brain Hypothesis                   │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Social capital: bonding     │ 🟢 Putnam 2000 — Bowling Alone            │
  │ vs bridging                 │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ 3 capitals reproduce        │ 🟢 Bourdieu 1986 — economic, social,     │
  │ across generations          │ cultural capital                          │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Behavior = f(expectancy     │ 🟢 Vroom 1964 — Expectancy Theory        │
  │ × valence × instrumentality)│                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Post-traumatic growth       │ 🟢 Tedeschi & Calhoun 2004 —             │
  │ possible after crisis       │ (crisis → positive change)               │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Expertise restructures      │ 🟢 Chase & Simon 1973 — chess chunking   │
  │ perception                  │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Income ↔ well-being         │ 🟢 Kahneman & Deaton 2010 — emotional    │
  │ plateau ~$75K               │ well-being satiation                      │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Frustration → aggression    │ 🟢 Dollard et al. 1939 — frustration-    │
  │                             │ aggression hypothesis                     │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ More choices → more anxiety │ 🟢 Schwartz 2004 — Paradox of Choice     │
  │ less satisfaction           │ Iyengar & Lepper 2000 — jam study        │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Deliberate practice →       │ 🟢 Ericsson 2006 — expertise requires    │
  │ expertise                   │ sustained deep practice                   │
  └─────────────────────────────┴──────────────────────────────────────────┘
```

---

## §11 — HONEST ASSESSMENT

```
⭐ CONFIDENCE PER CONCEPT:

  🟢 ESTABLISHED (research confirmed):
    → Self-efficacy → behavior (Bandura 1977)
    → Learned helplessness = DEFAULT (Maier & Seligman 2016)
    → Dunning-Kruger effect (Kruger & Dunning 1999)
    → Social capital: bonding vs bridging (Putnam 2000)
    → Capital reproduction (Bourdieu 1986)
    → Early intervention compound returns (Heckman 2006)
    → Capability Approach (Sen 1999)
    → Dunbar layers (Zhou et al. 2005)
    → Post-traumatic growth (Tedeschi & Calhoun 2004)
    → Choice overload (Schwartz 2004, Iyengar & Lepper 2000)
    → Deliberate practice → expertise (Ericsson 2006)

  🟡 FRAMEWORK SYNTHESIS (consistent, testable, not mainstream term):
    → Action-Space as per-person aggregate supply-side property
    → 4-trục model (Compiled Capacity, Resource Access, Freedom, Awareness)
    → 3 loại constraint (Blocked, Dependent, Invisible)
    → Positive/Negative spiral dynamics
    → 4-tầng formation model (Collective → Hardware)
    → Gap-Distribution × Action-Space behavioral prediction (4 quadrants)
    → Expansion quality: Potential vs Real Action-Space (post-threshold ratio)
    → 4 expansion profiles (Scattered/Specialist/T-Shaped/Serial Depth)
    → Depth-first principle (threshold → anchor → expand)
    → Premature expansion parallel Reward-Calibration §3.4
    → Gap-Distribution ↔ Action-Space feedback loop
    → Shift mechanisms per trục (asymmetric costs)

  🔴 HYPOTHESIS (testable, not verified):
    → Invisible constraint = most dangerous (logical, untested empirically)
    → Trục ④ = cheapest + hardest intervention (plausible, no quantification)
    → Optimal Gap-Distribution × Action-Space alignment (may not exist — depends on context)
    → Shift velocity per trục (no data on actual speeds)
    → Technology compensate ②③ (Hawking = N=1, not generalizable)


  ⚠️ FILE NÀY = OBSERVATION SYNTHESIS:
    → Tổng hợp insights từ ~15 files vào 1 supply-side aggregate view
    → KHÔNG tạo mechanism mới — tổ chức lại qua per-person Action-Space lens
    → Giá trị: NHÌN THẤY capability landscape → understand + predict + intervene
    → KHÔNG prescribe → "nên có Action-Space thế nào" = mỗi người tự decide
    → Sen 1999: "mỗi người tự chọn life they have reason to value" = ĐỒNG Ý
```

---

## §12 — OPEN QUESTIONS

```
⭐ 6 CÂU HỎI MỞ CHO DRILL SAU:

  Q1: ACTION SPACE CÓ THỂ QUANTIFY KHÔNG?
    → Gap-Distribution Q1 (same challenge): multi-dimensional, changes over time
    → Possible: QUALITATIVE observation (4-trục describe) > number
    → Sen approach: "functionings" vs "capabilities" — capability = potential set
    → Research direction: capability index per-population?

  Q2: INVISIBLE CONSTRAINT CÓ THỂ DETECT BẰNG AI KHÔNG?
    → AI-Schema-Detection §6: AI detect collective schemas
    → Extension: AI detect invisible constraints per-person?
    → Challenge: invisible = person doesn't know → AI needs EXTERNAL data
    → Possible: compare person's behavior with population → detect "missing options"

  Q3: AI ERA SHIFT ACTION SPACE THẾ NÀO?
    → AI automate tasks → trục ① less important for some domains?
    → AI provide information → trục ④ expand for everyone?
    → AI create new options → trục ② expand?
    → = Uncertain — AI era = natural experiment

  Q4: Gap-Distribution × Action-Space ALIGNMENT = MEASURABLE?
    → If measurable: predict life satisfaction, productivity, mental health
    → Challenges: both Gap-Distribution and Action-Space are multi-dimensional → alignment = complex
    → Csikszentmihalyi flow: skill ≈ challenge → Gap-Distribution × Action-Space alignment = flow analog?

  Q5: COLLECTIVE ACTION SPACE CÓ "OPTIMAL" DISTRIBUTION?
    → Should society maximize AVERAGE Action-Space? Or MINIMIZE variance?
    → Rawls 1971: maximize minimum → focus on lowest Action-Space individuals
    → Framework: KHÔNG prescribe, nhưng can OBSERVE patterns

  Q6: INHERITANCE — ACTION SPACE TRUYỀN THẾ HỆ THẾ NÀO?
    → ① Capacity: education system + family invest
    → ② Resource: inheritance, network, social capital
    → ③ Freedom: legal rights, social position
    → ④ Awareness: family culture, exposure breadth
    → = 4 channels of transmission, ALL reproduce (Bourdieu)
    → = TẠI SAO social mobility = HARD
```

---

## §13 — CROSS-REFERENCES

```
⭐ PRIMARY (file này BUILD ON):
  → Gap-Distribution-Profile.md v1.0 — SIBLING file (demand side ↔ supply side)
  → Gap-Direction.md v2.0 — "chưa biết = không có gap" (invisible constraint)
  → Status.md v2.1 — §1 Resource Access Map (trục ②)
  → Autonomy-Hardware.md v1.1 — §2 vmPFC/DRN (trục ④ hardware)
  → Autonomy.md v1.1 — software development (trục ④ software)

⭐ MECHANISM (file này REFERENCE):
  → Inter-Body-Mechanism.md v1.0 — Architecture B, PFC=Lawyer, 3-cost
  → Compliance-Floor.md v2.0 — trục ③ legal constraints
  → Obligation.md v1.1 — trục ③ obligation constraints
  → Money-Analysis.md v1.0 — trục ② money = bridge technology
  → Chunk.md v2.2 — compilation mechanism (trục ①)
  → Background-Pattern.md v1.1 — §8 self-reinforcing loop (§7 depth-first anchor)
  → Connection.md v4.0 — Dunbar layers (trục ② social capital)
  → Drill-Entity-Compiled-Capacity.md v1.0 — Depth × Breadth = constant
  → Domain-Mapping-Drive.md v1.0 — §2.3 threshold, §5 Einstein pattern (§7 ignition)
  → Reward-Calibration.md v1.1 — §3.4 premature compilation (§7.5 parallel)
  → Logic-Feeling-Balance.md — domain feedback = only arbiter (§7.6)

⭐ OBSERVATION (file này CONNECT):
  → Meaning.md v2.1 — life-level anchor × action space alignment
  → Self-Created-Threat.md v1.0 — awareness of self-created constraints
  → Expansion-Saturation-Crisis.md v1.1 — collective Action-Space mismatch
  → Domain-Mapping-Drive.md v1.0 — reward from PROCESS (trục ① growth)
  → Reward-Calibration.md v1.1 — over-reward × premature access (trục ②)

⭐ APPLICATION:
  → By-Product-Gap-Resonance.md v1.0 — trục ⑤ Constraint context (Phase 2 reference)
  → Education-Mechanism.md — education as Action-Space intervention
  → AI-Schema-Detection.md v2.0 — AI detect invisible constraints (Q2)
```

---

**File version:** v1.0
**Created:** 2026-05-19
**Author context:** Drill session — Gap-Distribution demand side → Action-Space supply side.
Behavior = f(Gap-Distribution × Action-Space). Sen's Capability Approach as research anchor.
**Next potential:** v1.1 nếu drill thêm Q1-Q6, hoặc integrate vào
By-Product-Gap-Resonance v2.0 (Phase 2 — trục ⑤ Constraint context reference)
