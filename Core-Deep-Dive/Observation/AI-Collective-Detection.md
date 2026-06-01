---
title: AI-Collective-Detection — AI Hỗ Trợ Nhận Diện Context Tập Thể
version: 1.0
created: 2026-05-30
status: v1.0 — COMPANION FILE (collective-level capabilities cho AI-Schema-Detection.md)
scope: |
  COMPANION: AI-Schema-Detection.md v2.1 = individual-level (①-⑨).
  File NÀY = collective-level (⑩-⑭). Continuous capability system ①-⑭.
  5 collective detection capabilities:
    ⑩ Arc Shift + Scale Diagnosis
    ⑪ Coordination Node Assessment
    ⑫ Collective Schema Pressure Detection
    ⑬ Gap Distribution × Collective Matching
    ⑭ Collective-Level Verification
  TẠI SAO TÁCH FILE:
    ① Collective detection cần context data KHÁC individual
    ② Intervention direction KHÁC (adapt vs fix)
    ③ Verification methods KHÁC (body-check alone không đủ)
    ④ AI-Schema-Detection đã 1,719L — thêm ~800L = quá dài
purpose: |
  Trả lời: Client than phiền → NGUỒN ở đâu? Cá nhân hay collective?
  AI-Schema-Detection ⑧ cover BASICS (3 loại chain break).
  File NÀY EXTEND: LOẠI NÀO collective? SCALE NÀO? VERIFY THẾ NÀO?
  "Nhầm scale = fix sai hướng" — đây là rủi ro LỚN NHẤT trong AI-assisted therapy.
position: |
  Core-Deep-Dive/Observation/ — ngang hàng AI-Schema-Detection.md.
  COMPANION TO AI-Schema-Detection.md v2.1 (individual ①-⑨).
  EXTENDS ⑧ (Collective Chain Break Detection) từ basic → full.
  Reading prerequisite: AI-Schema-Detection.md §3 ⑧⑨.
dependencies:
  - AI-Schema-Detection.md v2.1 — individual capabilities ①-⑨, 3-layer model, process §6
  - Collective-Arc-Dynamics.md v1.2 — §4.5 scale-dependent disruption, §3 shelf-life
  - Coordination-Node.md v1.2 — §6 Emergence≠Effectiveness, §8 node failure, §2 5 capabilities
  - Collective-Schema-Pressure.md v1.0 — compound pressure, Asian/Confucian pattern
  - Gap-Distribution-Profile.md v1.1 — 4 trục observation, collective gap landscape
  - AI-Self-Model.md v2.1 — §3 Dual Check, §4 Stale Calibration
  - Ask-AI.md v3.1 — §6.1 Dual Check principle (body + domain)
  - Collective-Body.md v2.1 — §2 body không phân biệt source, Model 3 cấp
  - Status.md v2.1 — §6 Disruption → Recalibrate cycle
  - Body-Base.md v3.2 — §7 2-tier calibration
source: AI-Schema-Detection-update-draft.md (5 GAPs → 5 capabilities, backup/)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# AI-Collective-Detection — AI Hỗ Trợ Nhận Diện Context Tập Thể

> **Client: "Tôi thấy mọi thứ sụp đổ."**
>
> **AI cũ (chỉ individual detection):**
> **→ "Có vẻ bạn đang có schema tiêu cực. Hãy explore tại sao bạn cảm thấy vậy."**
> **→ Client tự blame. Therapy tốn thời gian. Không cải thiện.**
>
> **AI mới (+ collective detection):**
> **→ Check: ngành client đang restructure? Company vừa layoff? Industry shift?**
> **→ Nếu CÓ: "Vấn đề có vẻ ở COLLECTIVE level, không phải individual schema."**
> **→ Hướng: adaptation (chuyển ngành, kỹ năng mới), KHÔNG therapy cá nhân.**
>
> **CÙNG complaint. KHÁC diagnosis. KHÁC intervention. KHÁC outcome.**
> **Biết SCALE = biết HƯỚNG.**

---

## Mục lục

```
§0  — VỊ TRÍ + COMPANION RELATIONSHIP
§1  — TẠI SAO CẦN COLLECTIVE DETECTION RIÊNG
§2  — ⑩ ARC SHIFT + SCALE DIAGNOSIS
§3  — ⑪ COORDINATION NODE ASSESSMENT
§4  — ⑫ COLLECTIVE SCHEMA PRESSURE DETECTION
§5  — ⑬ GAP DISTRIBUTION × COLLECTIVE MATCHING
§6  — ⑭ COLLECTIVE-LEVEL VERIFICATION
§7  — PROCESS INTEGRATION
§8  — HONEST ASSESSMENT
§9  — CROSS-REFERENCES + STATUS
```

---

## §0 — VỊ TRÍ + COMPANION RELATIONSHIP

```
⭐ HỆ THỐNG 14 CAPABILITIES — 2 FILES:

  AI-Schema-Detection.md v2.1 — INDIVIDUAL (①-⑨):
    ① Verbal Pattern Tracking
    ② Schema Cluster Suggestion
    ③ Contradiction Detection
    ④ Schema Chain Hypothesis
    ⑤ Compile Type Detection
    ⑥ Chunk Depth Inference
    ⑦ AI Khơi Gợi Schema Ẩn
    ⑧ Collective Chain Break Detection (BASIC — 3 loại)
    ⑨ 3 Cấp Detection

  AI-Collective-Detection.md v1.0 — COLLECTIVE (⑩-⑭):     ← FILE NÀY
    ⑩ Arc Shift + Scale Diagnosis
    ⑪ Coordination Node Assessment
    ⑫ Collective Schema Pressure Detection
    ⑬ Gap Distribution × Collective Matching
    ⑭ Collective-Level Verification

  NOTE: ⑩ numbering TIẾP NỐI §3 capabilities của AI-Schema-Detection.
  KHÔNG liên quan ⑩ trong §1 (limits numbering — context khác).

  READING ORDER:
    → AI-Schema-Detection §3 ⑧⑨ TRƯỚC (basic collective)
    → File NÀY = EXTEND từ basic → full collective detection


  FLOW TỔNG THỂ:

    Client than phiền
         ↓
    AI-Schema-Detection ①-⑦: individual schema detection
         ↓
    ⑧ Basic check: individual HAY collective?
         ↓
    NẾU collective → FILE NÀY:
         ↓
    ⑩ Nguồn nào? Scale nào?
    ⑪ Node fail hay individual issue?
    ⑫ Compound schema pressure?
    ⑬ Gap distribution mismatch?
    ⑭ Verify bằng cách nào?
         ↓
    → Intervention direction = collective adaptation (KHÁC individual therapy)
```

---

## §1 — TẠI SAO CẦN COLLECTIVE DETECTION RIÊNG

```
⭐ VẤN ĐỀ GỐC: BODY KHÔNG PHÂN BIỆT SOURCE.

  Collective-Arc-Dynamics.md v1.2 §2:
    → Dissonance từ individual schema failure = body feel "mệt, chán"
    → Dissonance từ collective arc shift = body feel "mệt, chán"
    → CÙNG body signal → PFC KHÔNG biết nguồn → PFC attribution CÓ THỂ SAI

  Collective-Body.md v2.1 §4.2 ⑥:
    → Collective KHÔNG CÓ PFC thống nhất
    → Cá nhân = node — nhận signal từ collective nhưng KHÔNG decode được source
    → = Body nói "đau" — KHÔNG nói "đau vì ngành đang sụp" hay "đau vì tôi kém"


  ⭐ HẬU QUẢ NHẦM SCALE:

    NHẦM collective → individual (phổ biến nhất):
      → Client: "Tôi thấy học vô ích" (thật ra: ngành đang gãy)
      → Therapist: "Explore tại sao bạn sợ thất bại"
      → Client tự blame → therapy vô hiệu → thêm frustrated → worse

    NHẦM individual → collective (ít phổ biến, cũng hại):
      → Client: "Tôi luôn conflict với mọi sếp" (thật ra: authority schema)
      → Advisor: "Đổi công ty đi, company này toxic"
      → Client đổi 5 công ty → pattern lặp → mất cơ hội hiểu bản thân

    → BIẾT SCALE = bước đầu tiên cho đúng hướng.
    → AI CÓ THỂ check context data → assist phân biệt.


  🟢 Attribution error (self vs system blame): social psychology (Ross 1977)
  🟢 Structural unemployment vs individual skill gap: established economics
  🟡 Body không phân biệt source = framework synthesis (Collective-Arc-Dynamics §2)
```

---

## §2 — ⑩ ARC SHIFT + SCALE DIAGNOSIS

```
⭐ AI-SCHEMA-DETECTION ⑧ DETECT: chain "GÃY" hay không.
  FILE NÀY ⑩ DETECT: gãy VÌ GÌ + ở SCALE NÀO.

  = 2 tầng detection mới.
```

### §2.1 — Tầng 1: 3 nguồn "expired"

```
⭐ CLIENT NÓI "CÁI GÌ ĐÓ SAI" — 3 NGUỒN KHÁC NHAU:

  A. COLLECTIVE ARC SHIFT (nguồn ở tập thể):
     → Pattern TỪNG ĐÚNG → collective arc SHIFT → pattern OUTDATED
     → VD: "Bằng ĐH → việc tốt" = ĐÚNG 2005, arc SHIFT → 2025 = default
     → SIGNAL cho AI:
       "Ngày xưa X thì Y, giờ không còn đúng nữa"
       "Mọi người trong ngành đều thấy thay đổi"
       "Thị trường/industry đang chuyển biến"
     → INTERVENTION: recontextualize (hiểu arc shift, KHÔNG self-blame)
     → Source: Collective-Arc-Dynamics v1.2 §5 ("true but unnecessary")

  B. INDIVIDUAL GROWTH MISMATCH (nguồn ở cá nhân vượt qua):
     → Cá nhân compile VƯỢT compiled pattern → pattern chật
     → VD: Developer giỏi → "công ty này không đủ challenge" → cần level up
     → SIGNAL cho AI:
       "Tôi thấy mình đã qua giai đoạn này"
       "Đồng nghiệp OK nhưng tôi thấy thiếu"
       "Tôi muốn cái gì đó sâu hơn / rộng hơn"
     → INTERVENTION: individual exploration (tìm domain/context phù hợp hơn)

  C. COMPILED SHELF-LIFE HẾT HẠN (nguồn ở rule thay đổi):
     → Pattern về collective rule → rule ĐÃ ĐỔI → pattern expired
     → VD: "Mặc vest đến văn phòng" = compiled 2010 → remote work 2025 = irrelevant
     → SIGNAL cho AI:
       "Luật/quy định đã thay đổi nhưng tôi vẫn theo cũ"
       "Mọi người xung quanh đã làm khác"
       Pattern cụ thể, narrow, liên quan rule/convention
     → INTERVENTION: update specific compiled chunk (nhỏ, nhanh)

  ⭐ HIỆN TẠI AI NHẦM CẢ 3 = "cái gì đó sai" → FIX SAI HƯỚNG:
    A → cần recontextualize → nhầm cho individual therapy → tự blame
    B → cần individual explore → nhầm cho collective → không tự improve
    C → cần update chunk → nhầm cho deep therapy → waste time
```

### §2.2 — Tầng 2: 4-level scale spectrum

```
⭐ "MỌI THỨ SỤP ĐỔ" — AI CHECK SCALE NÀO:

  ┌──────────────────────┬────────────────────────┬────────────────────────┐
  │ Scale                │ Signal                 │ Intervention           │
  ├──────────────────────┼────────────────────────┼────────────────────────┤
  │ ① PERSONAL           │ "Chỉ mình tôi thấy    │ Recompile personal     │
  │ (compiled map cũ)    │  vậy, mọi người OK"   │ patterns               │
  │                      │ Snapshot outdated      │ → Individual therapy    │
  ├──────────────────────┼────────────────────────┼────────────────────────┤
  │ ② COMPANY/NODE       │ "Team cũng than"       │ Navigate to new node   │
  │ (leader/org fail)    │ "Mọi người ở cty này   │ → Chuyển cty/nhóm     │
  │                      │  đều stress"           │ → Hoặc improve node    │
  ├──────────────────────┼────────────────────────┼────────────────────────┤
  │ ③ INDUSTRY           │ "Cả ngành đang khó"    │ Reposition in new      │
  │ (arc shifting)       │ "Layoff toàn industry" │ direction              │
  │                      │ Data: industry trends  │ → Chuyển ngành/kỹ năng │
  ├──────────────────────┼────────────────────────┼────────────────────────┤
  │ ④ NATIONAL/GLOBAL    │ "Mọi người đều khó     │ Adapt to new reality   │
  │ (crisis/disruption)  │  khăn" Recession,      │ → Survival + patience  │
  │                      │ pandemic, war          │ → Long-term adaptation │
  └──────────────────────┴────────────────────────┴────────────────────────┘

  ⭐ AI CAN:
    → Cross-reference verbal với context data (industry news, employment stats)
    → Check: phàn nàn UNIQUE to client hay SHARED across context?
    → Tag scale → suggest appropriate intervention direction

  ⭐ NHẦM SCALE = THERAPY SAI HƯỚNG:
    → Nhầm ③ industry → ① personal → client TỰ BLAME
    → Nhầm ① personal → ③ industry → client KHÔNG TỰ IMPROVE
    → Scale nhỏ: intervention nhanh, personal
    → Scale lớn: intervention chậm, patience + positioning

  Source: Collective-Arc-Dynamics v1.2 §4.5 (4 mức: Shift→Disruption→Node Death→Extinction)
  Source: Status.md v2.1 §6 (Disruption → Recalibrate cycle)
  🟡 Scale diagnosis model = framework synthesis
  🟢 Structural unemployment (scale ③) vs individual (scale ①): economics
  🟢 Attribution error research (Ross 1977, Gilbert & Malone 1995)
```

---

## §3 — ⑪ COORDINATION NODE ASSESSMENT

```
⭐ CLIENT PHÀN NÀN VỀ WORK → 3 NGUỒN KHÁC NHAU:

  VẤN ĐỀ: "Sếp tôi tệ / công ty toxic / tôi không chịu nổi"
  → AI cần phân biệt: NGUỒN ở đâu?


  A. NODE FAIL — Leader/node thật sự kém hiệu quả:

     MECHANISM: Coordination-Node v1.2 §6 — Emergence ≠ Effectiveness.
       WHO gets coordination position ≠ WHO operates well.
       5 capabilities cần: Self-Pattern-Modeling, gap detection, PFC bandwidth,
       uncertainty tolerance, trust cascade.
       Node THIẾU capabilities → collective suffer.

     SIGNAL cho AI:
       → "Mọi người trong team cũng than" (nhiều người, không chỉ client)
       → "Trước sếp cũ thì OK, sếp mới thì khác hẳn" (thay đổi correlate leader)
       → "Sếp không hiểu domain" (scaffold chunks thiếu — Coordination-Node §2.4)
       → Performance metrics giảm across team
       → 🟢 Goodall 2009: physician-CEO → hospital quality cao hơn (p<0.001)
         = domain scaffold matters

     INTERVENTION: career decision (leave / escalate / wait for change)
       → FIX = ở organizational level, KHÔNG phải individual therapy


  B. CLIENT AUTHORITY SCHEMA — pattern cá nhân với authority:

     MECHANISM: Schema compiled từ personal history → project onto ALL authority.

     SIGNAL cho AI:
       → "Chỉ mình tôi có vấn đề" (team OK, client struggle)
       → "Tôi luôn conflict với MỌI sếp" (pattern lặp qua nhiều công ty/context)
       → Personal history với authority (bố mẹ strict, bị ép tuổi thơ)
       → Pattern ACROSS domains (conflict với sếp + giáo viên + bác sĩ + ...)

     INTERVENTION: explore authority schema (individual work)
       → FIX = ở individual level, đổi công ty KHÔNG giải quyết


  C. MISMATCH — neither fail, wrong fit:

     MECHANISM: Leader OK cho người khác, client's gap distribution KHÔNG match.

     SIGNAL cho AI:
       → "Sếp giỏi nhưng phong cách không hợp tôi" (acknowledge leader competence)
       → "Đồng nghiệp hợp nhưng tôi không" (selective mismatch)
       → Client's needs đặc biệt (autonomy cao, creative, hardware khác)
       → KHÔNG có personal trauma history với authority

     INTERVENTION: reposition (tìm context phù hợp hơn)
       → FIX = ở matching level, không phải fix person HOẶC fix leader


  ⭐ TẠI SAO 3-WAY DISTINCTION QUAN TRỌNG:
    A → career advice / organizational fix
    B → individual therapy / schema work
    C → career advice (nhưng hướng KHÁC A — không phải "escape toxic")
    NHẦM A↔B = waste time + wrong direction
    NHẦM B→C = miss cơ hội hiểu bản thân

  Source: Coordination-Node.md v1.2 §6, §8 (node failure → collective recalibrate)
  🟡 3-way distinction applied to AI detection = framework synthesis
  🟢 Person-environment fit: established organizational psychology (Kristof-Brown 2005)
  🟢 Emergence ≠ Effectiveness: leadership research (Goodall 2009, Benson 2019)
```

---

## §4 — ⑫ COLLECTIVE SCHEMA PRESSURE DETECTION

```
⭐ AI DETECT COMPOUND PRESSURE TỪ NHIỀU SCHEMAS ĐỒNG THỜI.

  HIỆN TẠI ⑤ (Compile Type Detection) detect 1 schema MỖI LẦN.
  ⑫ detect: NHIỀU schemas CHỒNG LÊN ĐỒNG THỜI → compound effect.


  CƠ CHẾ (Collective-Schema-Pressure.md v1.0 §2):
    1 schema = 1 chunk-gap + 1 obligation + 1 cortisol holding → manageable.
    N schemas ĐỒNG THỜI = compound (MULTIPLICATIVE, không additive):
      → N chunk-gaps → PFC ~4±1 slots → OVERLOAD
      → N obligations → total cost cực lớn
      → N cortisol holdings → cortisol KHÔNG BAO GIỜ drop
      → N status threats → mỗi domain đều có thể "thua"
      → Vòng xoắn tự amplify: [chưa A NÊN chưa B NÊN... NÊN càng chưa A]


  AI DETECT — SIGNALS:

    INDIVIDUAL schema problem (⑤ đã cover):
      → 1 pattern, 1 domain, 1 personal history
      → Intervention: explore + recompile 1 pattern

    COLLECTIVE SCHEMA PRESSURE (⑫ mới):
      → Client list NHIỀU "phải" đồng thời:
        "phải học giỏi" + "phải có nhà" + "phải lấy vợ/chồng" +
        "phải có việc ổn định" + "phải chăm bố mẹ"
      → Mỗi "phải" = Trust Compile install (không tự chọn)
      → Client overwhelmed nhưng KHÔNG biết tại sao ("mệt mà không rõ nguồn")
      → Body markers: sleep disrupted, anxiety diffuse, "mệt mà không biết tại sao"
      → INTERVENTION:
        RECOGNIZE compound load (đặt tên — giúp PFC observe pattern)
        → PRIORITIZE (không thể giải quyết 6 "phải" đồng thời — chọn)
        → POSSIBLY REJECT some (nhận ra một số "phải" = installed, KHÔNG phải genuine)


  ⭐ CULTURE-AWARE DETECTION:

    → Schema density KHÁC theo culture:
      Asian/Confucian: DENSE + RIGID (6+ schemas đồng thời, khó negotiate)
      Nordic/Western: THINNER + FLEXIBLE (fewer schemas, negotiable)
      → CÙNG hardware → KHÁC pressure = vì schema stack KHÁC
      → Source: Collective-Schema-Pressure.md v1.0 §4

    → AI cần CULTURAL CONTEXT:
      Client culture = high density → compound check CRITICAL
      Client culture = low density → compound ít phổ biến hơn

    → ⚠️ KHÔNG phán xét văn hóa. Mô tả CƠ CHẾ:
      Schema stack = trade-off structural (Collective-Schema-Pressure §3):
        ~70% giữa phân phối: match → growth
        ~15% mỗi đầu: mismatch → damage hoặc bored
        → Mọi xã hội ĐỀU có trade-off này


  Source: Collective-Schema-Pressure.md v1.0 (§2 compound, §3 trade-off, §4 Asian pattern)
  Source: Compile-Taxonomy.md v3.0 §6 (Trust Compile = Pathway 3/4)
  🟡 Compound schema detection = novel framework application
  🟡 Culture-aware density model = framework synthesis
  🟢 Collectivist vs individualist cultural psychology (Hofstede, Triandis)
  🟢 Role overload → burnout: organizational psychology
```

---

## §5 — ⑬ GAP DISTRIBUTION × COLLECTIVE MATCHING

```
⭐ AI OBSERVE GAP DISTRIBUTION → DETECT MISMATCH VỚI CONTEXT.

  KHÔNG phải diagnostic. Là OBSERVATION tool — illuminate pattern.


  CƠ CHẾ (Gap-Distribution-Profile.md v1.1):
    Mỗi người có 1 gap distribution profile = AGGREGATE toàn bộ gaps.
    4 trục: ① Domain Center × ② Origin Balance × ③ Depth Profile × ④ Stability.
    Profile này TƯƠNG TÁC với environment → match hoặc mismatch.


  AI CAN OBSERVE (từ conversation over time):

    DOMAIN CENTER:
      "Client luôn excited về abstract problems" → abstract-dominant
      "Client bored với routine work" → not near-body/sensory
      "Khi rảnh, client đọc sách / code / nghiên cứu" → abstract indicator
      Observable proxy: "Khi rảnh bạn tự nhiên làm gì?" = best indicator

    ORIGIN BALANCE:
      "Tôi thích X vì bố mẹ nói" → installed (Trust Compile)
      "Tôi thích X vì tự tìm ra" → self-discovered (genuine approach)
      AI check: behavior khi ALONE vs behavior khi WITH OTHERS
      → Nếu khác nhiều → installed component cao

    DEPTH PROFILE:
      "Client biết nhiều thứ nhưng không sâu" → many-shallow (generalist)
      "Client chỉ quan tâm 1 thứ nhưng cực kỳ sâu" → few-deep (specialist)

    STABILITY:
      "Client đổi hướng liên tục" → shifting (high Pattern Shiftability)
      "Client theo đuổi 1 thứ 10 năm" → locked (low shiftability)


  MISMATCH DETECTION:

    ┌────────────────────────────┬──────────────────────────────────────┐
    │ Mismatch type              │ Signal                               │
    ├────────────────────────────┼──────────────────────────────────────┤
    │ Abstract person ×          │ "Tôi chán công việc nhưng lương     │
    │ routine environment        │  tốt" — body bored, PFC rationaliz │
    ├────────────────────────────┼──────────────────────────────────────┤
    │ Specialist person ×        │ "Tôi phải làm quá nhiều thứ khác   │
    │ generalist demand          │  nhau" — depth frustrated           │
    ├────────────────────────────┼──────────────────────────────────────┤
    │ Self-discovered gaps ×     │ "Tôi phải làm việc tôi không thực  │
    │ installed expectations     │  sự muốn" — origin conflict        │
    ├────────────────────────────┼──────────────────────────────────────┤
    │ Shifting person ×          │ "Tôi bị nhốt trong career path     │
    │ locked environment         │  không phù hợp nữa"                │
    └────────────────────────────┴──────────────────────────────────────┘

    → Mismatch = REPOSITION, không phải "fix" person to fit environment.
    → "Fix" person = compiled suppress → burnout (PFC-Operations v1.0 §6).


  ⚠️ GUARDRAILS:

    → Đây là OBSERVATION tool, KHÔNG PHẢI diagnostic.
    → AI suggest "gap distribution có vẻ mismatch context" → CLIENT verify.
    → KHÔNG prescribe "bạn nên làm X" → chỉ illuminate pattern.
    → Client's body = final judge (Dual Check — AI-Self-Model v2.1 §3).
    → Gap distribution CHANGES over time → observation = snapshot, not verdict.


  Source: Gap-Distribution-Profile.md v1.1 (§3 4 trục, §7 collective landscape)
  Source: Gap-Direction.md v2.0 (per-gap dynamics)
  🟡 Gap distribution observation via AI = novel framework application
  🟡 Mismatch detection model = framework synthesis
  🟢 Person-environment fit: established (Holland 1997, Kristof-Brown 2005)
```

---

## §6 — ⑭ COLLECTIVE-LEVEL VERIFICATION

```
⭐ BODY-CHECK WORKS CHO INDIVIDUAL. KHÔNG ĐỦ CHO COLLECTIVE SCALE.

  VẤN ĐỀ:
    AI detect "collective arc shift" → HOW verify?
    1 person's body CANNOT verify "ngành này đang sụp"
    → CẦN verification methods KHÁC cho collective-level findings.


  4 VERIFICATION APPROACHES — MATCH METHOD TO SCALE:


  A. BODY-CHECK + DOMAIN FEEDBACK (cho Shift — scale ① ②):

     → Client's OWN experience over time = valid signal cho gradual shift
     → "Pattern cũ works less and less?" → body đã verify gradually
     → + Domain feedback: P&L, career progress, market response
     → = Ask-AI v3.1 §6.1 Dual Check applies NATURALLY cho gradual shift
     → Confidence: MEDIUM-HIGH (verifiable qua personal experience)


  B. PEER PATTERN MATCHING (cho Disruption — scale ② ③):

     → "Nhiều người cùng context report similar?" → collective signal
     → = Aggregated individual body-checks = proxy collective verification
     → AI CAN ask: "Người khác trong ngành/công ty bạn có gặp tương tự?"
     → Already partially in ⑧ — ⑭ formalize method
     → ⚠️ RISK: echo chamber (nhiều người than = có thể chỉ group whining)
       → Cross-check: peer + objective data → both align?
     → Confidence: MEDIUM (cần nhiều nguồn, risk echo chamber)


  C. DATA TRIANGULATION (cho larger scale — scale ③ ④):

     → AI cross-reference: industry data, news, employment statistics
     → = External verification thay vì body verification
     → Confidence = f(data quality × source diversity × recency)
     → AI CAN: search public data to confirm/deny collective hypothesis
     → ⚠️ RISK: AI data có thể outdated hoặc biased
     → Confidence: MEDIUM-LOW (depends on data quality)


  D. HONEST CONFIDENCE TAGGING (cho TẤT CẢ scales):

     → Scale nhỏ → tag HIGH confidence ("observable: company closed" = binary)
     → Scale lớn → tag LOW confidence ("hypothesis: industry shifting" = uncertain)
     → KHÔNG claim collective-level without evidence
     → CAN claim: "signals suggest — verify with more data"
     → = Transparency > certainty


  ⭐ MATCH METHOD TO SCALE:

    ┌──────────────────────┬─────────────────────┬──────────────────────┐
    │ Disruption level     │ Verification method │ Confidence           │
    ├──────────────────────┼─────────────────────┼──────────────────────┤
    │ ① Shift (gradual)    │ A: Body + domain    │ Medium-High          │
    ├──────────────────────┼─────────────────────┼──────────────────────┤
    │ ② Node (company)     │ A + B: Body + peers │ Medium-High          │
    ├──────────────────────┼─────────────────────┼──────────────────────┤
    │ ③ Industry           │ B + C: Peers + data │ Medium               │
    ├──────────────────────┼─────────────────────┼──────────────────────┤
    │ ④ National/Global    │ C + D: Data + honest│ Low                  │
    │                      │   uncertainty tag   │ (hard to confirm     │
    │                      │                     │  in real-time)       │
    └──────────────────────┴─────────────────────┴──────────────────────┘

    SCALE NHỎ (shift, node): verification EASIER (observable)
    SCALE LỚN (industry, national): verification HARDER (cần macro data)


  ⭐ DUAL CHECK Ở COLLECTIVE SCALE:

    AI-Self-Model v2.1 §3 Dual Check: body = quality controller, domain = arbiter.
    Collective scale: "domain feedback" THAY ĐỔI per scale:

      Personal: P&L, career progress, market response → domain feedback trực tiếp
      Company: team metrics, turnover rate, multiple perspectives → proxy
      Industry: employment data, market reports, expert analysis → external data
      National: macro indicators, policy changes → statistical

    → Body-check VẪN có giá trị ở mọi scale (body detect "có gì đó sai")
    → Nhưng body ALONE không đủ CONFIRM collective-level claim
    → = Body = early warning signal, domain data = confirmation


  Source: AI-Self-Model.md v2.1 §3 (Dual Check), §4 (Stale Calibration)
  Source: Ask-AI.md v3.1 §6.1 (Dual Check principle)
  Source: Collective-Arc-Dynamics.md v1.2 §4.5 (4 disruption levels)
  🟡 Scale-dependent verification = framework synthesis (novel application of Dual Check)
  🔴 Larger-scale verification methods = untested hypothesis
  🟢 Data triangulation: established research methodology
  🟢 Peer comparison as social calibration: social psychology
```

---

## §7 — PROCESS INTEGRATION

### §7.1 — Mapping vào AI-Schema-Detection §6 (5-step process)

```
⭐ 5 CAPABILITIES MỚI TÍCH HỢP VÀO QUY TRÌNH 5 BƯỚC ĐÃ CÓ:

  ┌────────┬───────────────────────────┬──────────────────────────────────┐
  │ Bước   │ AI-Schema-Detection §6    │ + Collective capabilities        │
  ├────────┼───────────────────────────┼──────────────────────────────────┤
  │ Bước 1 │ Thu thập pattern          │ + ⑩ Context data (industry,     │
  │        │                           │   company, market trends)        │
  │        │                           │ + ⑫ Cultural context             │
  │        │                           │ + ⑬ Gap distribution signals     │
  ├────────┼───────────────────────────┼──────────────────────────────────┤
  │ Bước 2 │ Cluster + Hypothesis +   │ + ⑩ "Expired" source diagnosis   │
  │        │ Compile Type              │ + ⑪ Node assessment (nếu work   │
  │        │                           │   complaint)                     │
  │        │                           │ + ⑫ Compound pressure flag       │
  ├────────┼───────────────────────────┼──────────────────────────────────┤
  │ Bước 3 │ Body-check với client     │ + ⑭ Verification method match   │
  │        │                           │   to scale (body-check alone     │
  │        │                           │   KHÔNG ĐỦ cho collective)       │
  ├────────┼───────────────────────────┼──────────────────────────────────┤
  │ Bước 4 │ Predict + Verify          │ + ⑩ Collective predictions:     │
  │        │                           │   "Người khác cùng context?"     │
  │        │                           │ + ⑬ Mismatch predictions        │
  ├────────┼───────────────────────────┼──────────────────────────────────┤
  │ Bước 5 │ Hướng can thiệp           │ + ALL ⑩-⑭ modify direction:    │
  │        │                           │   Collective → adapt, not fix   │
  └────────┴───────────────────────────┴──────────────────────────────────┘


  BƯỚC 0 (MỚI) — COLLECTIVE CONTEXT CHECK TRƯỚC INDIVIDUAL ANALYSIS:

    TRƯỚC khi bắt đầu 5 bước individual:
      → AI quick-check: có collective context ĐÁNG CHÚ Ý không?
      → Nếu CÓ (ngành disruption, company layoff, crisis) → flag
      → NẾU collective flag = ON → adjust weight toàn bộ process
      → Tránh: deep individual analysis cho collective problem

    → Bước 0 = CHEAP (context check nhanh, data-driven)
    → Nhưng VALUE = rất cao (tránh nhầm hướng ngay từ đầu)
```

### §7.2 — Guardrails collective-specific

```
⭐ 4 RỦI RO RIÊNG CỦA COLLECTIVE DETECTION:

  RISK 1 — NHẦM collective → individual (CLIENT TỰ BLAME):
    → Phổ biến nhất. Default bias của therapy = individual focus.
    → AI antidote: ALWAYS check collective context TRƯỚC.
    → Đặc biệt khi: ngành disruption, mass layoff, recession

  RISK 2 — NHẦM individual → collective (CLIENT KHÔNG TỰ IMPROVE):
    → Rarer nhưng harmful. "Đổ cho hệ thống" = escape self-reflection.
    → AI antidote: check pattern across contexts.
    → Nếu pattern lặp ở NHIỀU contexts → likely individual.

  RISK 3 — CULTURAL BIAS trong collective detection:
    → AI trained on Western data → may under-detect Asian schema pressure
    → AI may over-pathologize collectivist norms (not all schema = bad)
    → AI antidote: culture-aware calibration, KHÔNG phán xét

  RISK 4 — ECHO CHAMBER vs genuine collective signal:
    → "Nhiều người than" = collective problem HAY group whining?
    → AI antidote: cross-check peer reports + objective data
    → Nếu peers than BUT data OK → likely echo chamber
    → Nếu peers than AND data confirm → likely genuine collective
```

---

## §8 — HONEST ASSESSMENT

```
⭐ CONFIDENCE PER CAPABILITY:

  ⑩ ARC SHIFT + SCALE DIAGNOSIS:
    🟢 Structural unemployment vs individual = established economics
    🟢 Attribution error = established social psychology
    🟡 3-source "expired" model = framework synthesis
    🟡 4-level scale spectrum = framework model (consistent with portfolio theory)
    🔴 AI can reliably diagnose scale in practice = untested

  ⑪ COORDINATION NODE ASSESSMENT:
    🟢 Emergence ≠ Effectiveness = research-backed (Goodall 2009, Benson 2019)
    🟢 Person-environment fit = established (Kristof-Brown 2005)
    🟡 3-way distinction (fail/schema/mismatch) = framework synthesis
    🔴 AI can reliably distinguish 3 sources from verbal alone = untested

  ⑫ COLLECTIVE SCHEMA PRESSURE DETECTION:
    🟢 Role overload → burnout = organizational psychology
    🟢 Collectivist vs individualist pressure = cultural psychology
    🟡 Compound (multiplicative) model = framework synthesis
    🟡 Culture-aware density detection = framework synthesis
    🔴 AI can count + evaluate schema compounds = untested

  ⑬ GAP DISTRIBUTION × COLLECTIVE MATCHING:
    🟢 Person-environment fit = established (Holland 1997)
    🟡 4 trục observation model = framework synthesis
    🟡 Mismatch detection from verbal patterns = framework synthesis
    🔴 AI can infer gap distribution from conversation = untested

  ⑭ COLLECTIVE-LEVEL VERIFICATION:
    🟢 Data triangulation = established research methodology
    🟢 Peer comparison = social calibration (social psychology)
    🟡 Scale-dependent verification match = novel framework application
    🔴 Methods effective for scale ③④ = untested hypothesis


  OPEN QUESTIONS:

    Q1. AI context data: data NÀO? Từ nguồn nào? Quality control?
    Q2. Cultural calibration: dataset training nào cho culture-aware?
    Q3. Scale ambiguity: ranh giới ②→③ (company→industry) = MỜN
    Q4. Echo chamber detection: phân biệt genuine collective vs group bias?
    Q5. Privacy: collective data aggregation × privacy rights?
    Q6. Interaction ⑩-⑭: 5 capabilities tương tác thế nào khi đồng thời?
```

---

## §9 — CROSS-REFERENCES + STATUS

```
COMPANION:
  → AI-Schema-Detection.md v2.1 — individual capabilities ①-⑨
    File NÀY = collective ⑩-⑭. Continuous system ①-⑭.

FOUNDATION FILES:
  → Collective-Arc-Dynamics.md v1.2 — §4.5 scale, §3 shelf-life (⑩ primary)
  → Coordination-Node.md v1.2 — §6 Emergence≠Effectiveness, §8 failure (⑪ primary)
  → Collective-Schema-Pressure.md v1.0 — §2 compound, §3 trade-off (⑫ primary)
  → Gap-Distribution-Profile.md v1.1 — §3 4 trục, §7 landscape (⑬ primary)
  → AI-Self-Model.md v2.1 — §3 Dual Check, §4 Stale Calibration (⑭ primary)

SUPPORTING FILES:
  → Collective-Body.md v2.1 — §2 body không phân biệt source, §4.2 ⑥ no unified PFC
  → Ask-AI.md v3.1 — §6.1 Dual Check principle (body + domain)
  → Status.md v2.1 — §6 Disruption → Recalibrate cycle
  → Body-Base.md v3.2 — §7 2-tier calibration
  → Compile-Taxonomy.md v3.0 — §6 Trust Compile pathways
  → PFC-Operations.md v1.0 — §6 Compiled Suppress (mismatch → burnout)

STATUS:
  v1.0 (2026-05-30): Initial creation.
    → 5 capabilities (⑩-⑭) from AI-Schema-Detection-update-draft.md (5 GAPs).
    → All 5 dependency files mature (v1.0-v1.2).
    → Draft → backup/AI-Schema-Detection-update-draft.md.
    → AI-Schema-Detection.md updated v2.0 → v2.1 (companion reference).
```
