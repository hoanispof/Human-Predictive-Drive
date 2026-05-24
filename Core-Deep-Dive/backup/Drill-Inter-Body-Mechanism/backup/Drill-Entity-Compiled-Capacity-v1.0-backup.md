# Drill: Entity-Compiled Capacity — Depth × Breadth Tradeoff + Cost Scaling

> **Não chỉ chứa được ~5 Entity-Compiled sâu.**
> **~15 vừa. ~50 nông. ~150 active. Đó là CEILING.**
> **Không phải vì không muốn — vì KHÔNG ĐỦ CHUNKS.**
> **Depth × Breadth = constant. Luôn luôn.**

---

**Status**: v1.0 — Drill session 2026-05-18
**Mục tiêu**: Xác thực Entity-Compiled có CAPACITY CEILING, map Dunbar's layers vào framework, phân tích cost scaling khi agent khác nhau, kin vs friend cost, social portfolio tradeoff
**Phạm vi**: Dunbar research → Framework mapping → Cost per agent → Similar vs Different → Kin vs Friend → Filtering cost → Optimization
**Dependencies**: Valence-Propagation v2.0 §3, Drill-Entity-Compiled-Deep v1.4 §7-§8, Inter-Body-Mechanism v1.0 §8, Self-Pattern-Match v3.0 §2, By-Product-Gap-Resonance v1.0 §5

---

## Mục lục

- §1 — DUNBAR'S NUMBER: RESEARCH EVIDENCE
- §2 — FRAMEWORK MAPPING: TẠI SAO CÓ CEILING?
- §3 — COST SCALING: SIMILAR vs DIFFERENT AGENTS
- §4 — KIN vs FRIEND COST
- §5 — DEPTH × BREADTH = CONSTANT
- §6 — SOCIAL PORTFOLIO OPTIMIZATION
- §7 — INSIGHTS + GAPS
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES
- §10 — RESEARCH CITATIONS

---

## §1 — DUNBAR'S NUMBER: RESEARCH EVIDENCE

### §1.1 — Social Brain Hypothesis

```
🟢 Dunbar 1992, 1998 (Social Brain Hypothesis):
   Neocortex ratio × group size: r ≈ 0.9 across 38 primate genera
   = NÃO LỚN HƠN → XỬ LÝ NHIỀU RELATIONSHIPS HƠN
   Human neocortex predict: ~150 active relationships
   = CEILING — không phải preference, là CAPACITY LIMIT
```

### §1.2 — Layered structure (scaling ratio ≈ 3)

```
🟢 Zhou et al. 2005 (Proc. Royal Society B — empirical):

  ┌────────┬───────┬────────────────────────────────────────────┐
  │ Layer  │ Size  │ Emotional closeness                        │
  ├────────┼───────┼────────────────────────────────────────────┤
  │ S1     │  ~5   │ INTIMATE — "support clique"                │
  │        │       │ Daily/weekly contact. Deep emotional bond.  │
  │        │       │ Turn to in crisis. Grieve deeply if lost.  │
  ├────────┼───────┼────────────────────────────────────────────┤
  │ S2     │ ~15   │ CLOSE — "sympathy group"                   │
  │        │       │ Regular contact. Significant emotional.    │
  │        │       │ Know well. Would help in need.             │
  ├────────┼───────┼────────────────────────────────────────────┤
  │ S3     │ ~50   │ FRIENDS — "affinity group"                 │
  │        │       │ Occasional contact. Moderate closeness.    │
  │        │       │ Social events. Would attend wedding.       │
  ├────────┼───────┼────────────────────────────────────────────┤
  │ S4     │ ~150  │ ACTIVE — "Dunbar's number"                 │
  │        │       │ Know by name + context. Annual contact.    │
  │        │       │ Would invite to large party.               │
  ├────────┼───────┼────────────────────────────────────────────┤
  │ S5     │ ~500  │ KNOWN — acquaintances                      │
  │        │       │ Recognize face + name. Rare contact.       │
  ├────────┼───────┼────────────────────────────────────────────┤
  │ S6     │~1500  │ FACES — visual recognition only            │
  └────────┴───────┴────────────────────────────────────────────┘

  Scaling ratio ≈ 3 between layers (5→15→50→150→500→1500)
  = CONSISTENT across cultures, online + offline
```

### §1.3 — Empirical validation

```
🟢 Hill & Dunbar 2003 (Human Nature):
   Christmas card study: mean network = 124.9, max ≈ 153.5
   = REAL ceiling, not just theory

🟢 Roberts et al. 2009 (Social Networks) ★ KEY:
   ⭐ NEGATIVE CORRELATION: network size ↑ → emotional closeness ↓
   = Người có NHIỀU BẠN → mỗi bạn NÔNG HƠN
   = Người có ÍT BẠN → mỗi bạn SÂU HƠN
   = DEPTH × BREADTH = CONSTANT (finite resource tradeoff)

🟢 Sutcliffe et al. 2012 (JASSS):
   Computational model validated: investment in strong ties best reproduces
   observed layer structure. Outer layers decay faster.
   = Maintaining close relationships = DISPROPORTIONATE investment

🟢 Roberts & Dunbar 2011 (Personal Relationships, N=251):
   Larger kin network → longer intervals since last contact
   = Nhiều quan hệ → ÍT thời gian cho mỗi quan hệ
   ★ Kin cost < Friend cost (kin có hardware scaffold — §4)
```

---

## §2 — FRAMEWORK MAPPING: TẠI SAO CÓ CEILING?

### §2.1 — Dunbar layers = Entity-Compiled depth gradient

```
⭐ MAPPING VÀO FRAMEWORK:

  ┌────────┬───────┬──────────────────────────────────────────┐
  │ Layer  │ Size  │ Framework mechanism                      │
  ├────────┼───────┼──────────────────────────────────────────┤
  │ S1 ~5  │  ~5   │ Entity-Compiled DEEP                     │
  │        │       │ SPM F1 compiled (cost ≈ 0)               │
  │        │       │ Hub-and-Spoke FULL (all modalities)       │
  │        │       │ Body-base extension (VP §3)               │
  │        │       │ Transactive Memory active                │
  ├────────┼───────┼──────────────────────────────────────────┤
  │ S2 ~15 │ ~15   │ Entity-Compiled MODERATE                 │
  │        │       │ SPM F1 compiled per-domain               │
  │        │       │ Hub-and-Spoke PARTIAL (some modalities)   │
  │        │       │ Body-feedback on interaction (not 24/7)  │
  ├────────┼───────┼──────────────────────────────────────────┤
  │ S3 ~50 │ ~50   │ Entity-Compiled SHALLOW                  │
  │        │       │ SPM: F1 basic + F2 for novel situations  │
  │        │       │ Schema-level: face+name+context+valence  │
  │        │       │ Some compiled interaction patterns        │
  ├────────┼───────┼──────────────────────────────────────────┤
  │ S4 ~150│ ~150  │ SPM Fresh only (F2 per interaction)      │
  │        │       │ Schema: face+name+role                    │
  │        │       │ No body-base extension                    │
  │        │       │ Interaction = costly each time            │
  ├────────┼───────┼──────────────────────────────────────────┤
  │ S5 ~500│ ~500  │ Schema only (face+name, no SPM)          │
  │        │       │ Recognition only                          │
  ├────────┼───────┼──────────────────────────────────────────┤
  │ S6 ~1500│~1500 │ Visual recognition only                  │
  │        │       │ Fusiform face area pattern                │
  └────────┴───────┴──────────────────────────────────────────┘
```

### §2.2 — 3 cơ chế tạo ceiling

```
⭐ CEILING VÌ 3 RESOURCE GIỚI HẠN:

① CHUNK LIBRARY PER AGENT = FINITE:
   Mỗi Entity-Compiled = chunk assembly (Hub-and-Spoke):
     Visual chunks (mặt, dáng) + auditory (giọng, cách nói)
     + motor (cách tương tác) + trait knowledge (mPFC: "họ là ai")
     + episodic (hippocampus: kỷ niệm) + valence (amygdala: đánh giá)

   MỖI AGENT S1 = HÀNG NGHÌN chunks compiled
   5 agents × nghìn chunks = TENS OF THOUSANDS dedicated chunks
   + cross-links between agents → exponential complexity
   Brain total capacity = FINITE → ceiling

② MAINTENANCE COST (3-cost scales):
   Entity-Compiled cần MAINTAIN:
     → Regular interaction → keep chunks active (Hebbian: use or lose)
     → Update knowledge (agent THAY ĐỔI → chunks phải update)
     → Conflict resolution (3-cost khi mismatch occurs)

   Cost per agent ≈ SIMILAR across layers (tradeoff frequency × depth):
     S1: cost LOW per interaction (F1 compiled) BUT frequent (daily)
     S3: cost HIGH per interaction (F2 fresh) BUT infrequent (monthly)
     Total metabolic budget ≈ similar → finite budget → finite agents

③ INTERFERENCE BETWEEN MODELS:
   2 agents GIỐNG NHAU: shared chunks reusable → interference LOW
   2 agents RẤT KHÁC: unique chunks per agent → interference HIGH
   Risk: dùng SAI model cho SAI agent
   = "Nhầm cách nói chuyện với mẹ sang bạn" = context-switching error
   → More diverse agents → MORE distinct models → MORE switching cost
```

---

## §3 — COST SCALING: SIMILAR vs DIFFERENT AGENTS

### §3.1 — Similar agents = optimize

```
⭐ BẠN NÓI: "agents có tính cách gần giống → cost chunks predict THẤP hơn"

  CƠ CHẾ:
  2 agents GIỐNG NHAU:
    → SHARED chunks reusable (visual style, speech pattern, values)
    → SPM template GIỐNG → predict cả 2 bằng SIMILAR model
    → Total unique chunks THẤP hơn → fits within budget easier
    → Context-switching cost THẤP (models overlap)

  2 agents RẤT KHÁC:
    → ÍT shared chunks → total unique chunks PER AGENT cao
    → SPM template KHÁC → 2 DISTINCT models phải maintain
    → Total cost CAO + interference risk
    → Context-switching cost CAO

  → "Bạn thân na ná giống nhau" = KHÔNG phải coincidence
  → = OPTIMIZATION: self-select similar → maximize depth within budget
  → 🟢 Byrne 1971 (Similarity-Attraction): confirmed empirically
```

### §3.2 — 3 strategies

```
  STRATEGY A — ÍT AGENT, SÂU (introvert pattern):
    Ít S1-S2 agents, all deep Entity-Compiled
    Total chunks: MODERATE (few × deep)
    Interference: LOW (few models to switch between)
    Resonance quality: HIGH per pair (Stream 2 compiled)
    Cost: LOW per interaction (F1 dominant)
    Risk: HIGH if lose 1 agent (small network = fragile)

  STRATEGY B — NHIỀU AGENT GIỐNG, MEDIUM (selective extrovert):
    Many agents but SIMILAR type → shared chunks
    Total chunks: MODERATE (many × shallow BUT reusable)
    Interference: LOW-MEDIUM (similar models)
    Resonance quality: MEDIUM per pair
    Cost: MEDIUM (some F1, some F2)
    Risk: LOW (redundancy in network)

  STRATEGY C — NHIỀU AGENT KHÁC, NÔNG (networking):
    Many agents, DIVERSE types
    Total chunks: HIGH (many × diverse = unique per agent)
    Interference: HIGH (switching between very different models)
    Resonance quality: LOW per pair (mostly F2 Fresh, costly)
    Cost: HIGH per interaction
    Risk: LOWEST (maximum redundancy)
    ⚠️ Entity-Compiled depth = NECESSARILY shallow

  → Mỗi người = MIX of strategies, tends toward 1
  → Hardware + Background Pattern BIAS which strategy feels "natural"
```

---

## §4 — KIN vs FRIEND COST

```
⭐ KIN (gia đình) VÀ FRIEND (bạn bè) = KHÁC CƠ CHẾ:

  🟢 Roberts & Dunbar 2011: kin cost < friend cost (empirically confirmed)

  TẠI SAO KIN COST THẤP HƠN:

  ① EVOLUTION HARDWARE SUBSIDY:
     Kin = evolution-protected Entity-Compiled:
       Oxytocin system (mẹ-con): compile NHANH, habituation CHẬM
       Kin recognition (genetic similarity detection): MHC, phenotype matching
       Hamilton's rule (kin selection): inclusive fitness → bias toward kin
     → Hardware đã TRƯỚC trả 1 phần cost → PFC cost GIẢM

  ② KHÔNG CẦN CHỌN (given, not selected):
     Bạn bè: phải F2 evaluate → select → invest → hope for match
     Kin: GIVEN → no selection cost → start compiling immediately
     → Skip bước evaluate → save total cost

  ③ SHARED HARDWARE OVERLAP (genetic):
     Con ~50% DNA từ mỗi parent → hardware overlap CAO
     → SPM F1 template accuracy CAO by default
     → Enhancer (a) free → Stream 2 potential higher at start

  ④ OBLIGATORY SCAFFOLD:
     🟢 Roberts & Dunbar 2011: kin có "obligatory scaffolding"
     → Social norms + family structure MAINTAIN connection
     → Even without active investment → kin bond persists longer
     → Friends WITHOUT active investment → DECAY
     → = Friends need MORE active cost to maintain same level

  NHƯNG — NUANCE:
     Kin = GIVEN → có thể KHÔNG match (bố mẹ strict khác tính con)
     → Hardware subsidy OFFSET some mismatch cost
     → NHƯNG: extreme mismatch → kin bond = Outcome B "compiled suppress"
     → = Mixed Entity-Compiled (VP §3.2 ③) — vừa thương vừa giận
```

---

## §5 — DEPTH × BREADTH = CONSTANT

### §5.1 — Mathematical framing

```
⭐ CORE CONSTRAINT:

  TOTAL SOCIAL RESOURCE = FINITE
  = f(neocortex capacity × time available × metabolic budget)

  DEPTH per agent × NUMBER of agents ≈ CONSTANT

  VD (simplified):
    Budget = 100 units
    5 agents × 20 depth/agent = 100 (Strategy A)
    20 agents × 5 depth/agent = 100 (Strategy C)
    Can't: 20 agents × 20 depth/agent = 400 > budget

  IMPLICATION:
    → "Chơi với hàng chục, hàng trăm" → depth PHẢI giảm
    → "Chỉ 5 người" → depth CÓ THỂ rất cao
    → Social media "1000 friends" = 1000 × S5 Schema level
       Actual Entity-Compiled: vẫn ~5 intimate + ~15 close
    → Technology KHÔNG bypass brain capacity
       — chỉ thêm shallow layer (S5, S6)
```

### §5.2 — Khi nào constraint BINDING?

```
  KHÔNG phải lúc nào budget cũng dùng hết:

  CASE 1 — Under capacity:
    Hermit: 2 agents × 30 depth = 60 < budget
    → Còn resource nhưng KHÔNG invest (choice hoặc circumstance)

  CASE 2 — At capacity:
    Social butterfly: 150 agents at various depths = budget
    → Adding 1 more → MUST sacrifice depth somewhere
    → = WHY "new friend in, old friend out" pattern

  CASE 3 — Over capacity attempt:
    Celebrity/CEO: try 500+ active → budget VƯỢT
    → Result: burnout, shallow everywhere, relationship quality drops
    → = Social media managers, politicians: "know everyone, close to none"

  → Capacity tùy thuộc hardware:
    Extrovert: higher budget ceiling? → 🔴 unverified
    Introvert: lower budget ceiling? → 🔴 unverified
    Likely: SAME capacity, DIFFERENT cost per interaction
    → Introvert: cost/interaction HIGH → fewer interactions → fewer agents
    → Extrovert: cost/interaction LOW → more interactions → more agents
    → TOTAL DEPTH may be SIMILAR (same brain capacity, different distribution)
```

---

## §6 — SOCIAL PORTFOLIO OPTIMIZATION

### §6.1 — Framework language

```
🟡 SOCIAL PORTFOLIO = set of Entity-Compiled + active connections

  Mỗi connection = cost (3-cost model) + reward (Stream 1 + Stream 2)

  OPTIMIZE = maximize TOTAL reward within budget constraint

  FROM drill §10d:
    Roommate (non-close): HIGH cost, LOW reward = inefficient
    Close friend: LOW cost (compiled), HIGH reward = efficient
    → DROP low-efficiency → INVEST in high-efficiency
    → = "Fewer but deeper" = shift resource from breadth → depth
```

### §6.2 — "Duyên số" filtering cost (from Resonance-Definition §7)

```
  Tìm người "hợp" = sampling problem:
    → Gặp N entities → evaluate → filter → invest
    → COST: F2 evaluation + noise/hijack + resonance shift
    → BENEFIT: find match → deep Resonance → Entity-Compiled reward

  OPTIMAL SAMPLING ≠ maximum N:
    → Each sample = cost
    → False positives waste budget → reduce capacity for true match
    → True positive early → invest depth → compound returns

  → Body calibration quality = MODERATOR:
    Good calibration: few samples → find match → deep invest
    Poor calibration: many samples → many false positives → shallow
    → = WHY interoceptive awareness MATTERS for relationship quality
```

---

## §7 — INSIGHTS + GAPS

### §7.1 — Insights

| # | Insight | Confidence |
|---|---------|------------|
| I1 | Entity-Compiled has CAPACITY CEILING — brain capacity = finite resource | 🟢 Dunbar 1992 |
| I2 | Dunbar layers (~5/15/50/150) map to Entity-Compiled depth gradient | 🟢 Zhou 2005 |
| I3 | Depth × Breadth = constant (Roberts 2009: network size ↑ → closeness ↓) | 🟢 |
| I4 | 3 cơ chế tạo ceiling: chunk library finite + maintenance cost + interference | 🟡 |
| I5 | Similar agents = optimize (shared chunks → lower total cost) | 🟡 (🟢 Byrne 1971) |
| I6 | "Bạn thân na ná giống nhau" = optimization, không phải coincidence | 🟡 |
| I7 | 3 strategies: few+deep / many+similar / many+diverse — hardware biased | 🟡 |
| I8 | Kin cost < Friend cost (evolution hardware subsidy + obligatory scaffold) | 🟢 Roberts 2011 |
| I9 | Technology không bypass brain capacity — chỉ thêm shallow layers | 🟡 (🟢 Dunbar data) |
| I10 | Introvert/extrovert = same capacity, different cost per interaction | 🔴 hypothesis |
| I11 | Body calibration quality = moderator for social portfolio efficiency | 🟡 |

### §7.2 — Gaps

| # | Gap | Priority |
|---|-----|----------|
| G1 | Extrovert vs introvert: SAME capacity hay DIFFERENT? | HIGH |
| G2 | Entity-Compiled THRESHOLD: khi nào S4→S3→S2→S1 shift? | HIGH |
| G3 | Interference quantification: switching cost measurable? | MEDIUM |
| G4 | Social media + AI impact on Dunbar layers? | MEDIUM |
| G5 | Optimal portfolio composition: can framework predict? | LOW |

---

## §8 — HONEST ASSESSMENT

```
  🟢 STRONG EVIDENCE:
  - Dunbar's number + layer structure (Zhou, Hill, Sutcliffe)
  - Depth × Breadth tradeoff (Roberts 2009)
  - Kin cost < Friend cost (Roberts & Dunbar 2011)
  - Social Brain Hypothesis: neocortex ratio × group size (r≈0.9)
  - Similarity-attraction (Byrne 1971)

  🟡 FRAMEWORK SYNTHESIS:
  - Dunbar layers → Entity-Compiled depth gradient mapping
  - 3 cơ chế ceiling (chunk library + maintenance + interference)
  - 3 strategies (few+deep / many+similar / many+diverse)
  - Social portfolio optimization
  - Technology không bypass brain capacity
  - Similar agents = cost optimize

  🔴 HYPOTHESIS:
  - Introvert/extrovert = same capacity different cost
  - Entity-Compiled threshold (S4→S3 shift mechanism)
  - Interference quantification
```

---

## §9 — CROSS-REFERENCES

| File | Sections | Relationship |
|------|----------|-------------|
| Valence-Propagation v2.0 | §3 Entity-Compiled | DEFINES Entity-Compiled |
| Drill-Entity-Compiled-Deep v1.4 | §7 Transactive Memory, §10d Social Portfolio | Source insights |
| Inter-Body-Mechanism v1.0 | §8 Entity-Compiled, §4 3-cost | Mechanism foundation |
| By-Product-Gap-Resonance v1.0 | §5 Resonance Baseline | "Hợp tính" = Dunbar S1-S2 |
| Self-Pattern-Match v3.0 | §2 F1/F2 | SPM = cost driver per agent |
| Connection v4.0 | §6.8 Grief | Loss = capacity stranded |
| Background-Pattern v1.1 | §6 BP×SPM | Agent similarity = BP overlap |

---

## §10 — RESEARCH CITATIONS

| # | Citation | Used in | Evidence |
|---|----------|---------|----------|
| R1 | Dunbar 1992 — Social Brain Hypothesis | §1 | 🟢 Cross-primate |
| R2 | Dunbar 1998 — Grooming, Gossip, Evolution of Language | §1 | 🟢 |
| R3 | Zhou et al. 2005 (Proc. Roy. Soc. B) — Hierarchical layers | §1 | 🟢 |
| R4 | Hill & Dunbar 2003 (Human Nature) — Christmas card study | §1 | 🟢 |
| R5 | Roberts et al. 2009 (Social Networks) — Size ↔ Closeness tradeoff | §1, §5 | 🟢 |
| R6 | Roberts & Dunbar 2011 (Personal Relationships) — Kin vs Friend cost | §1, §4 | 🟢 |
| R7 | Sutcliffe et al. 2012 (JASSS) — Computational validation | §1 | 🟢 |
| R8 | Byrne 1971 — Similarity-Attraction | §3 | 🟢 |
| R9 | Hamilton 1964 — Inclusive Fitness / Kin Selection | §4 | 🟢 |
| R10 | Dunbar 2024 — Social Brain Hypothesis 30 Years On | §1 | 🟢 |

---

**END OF DRILL — v1.0 (11 insights, 5 gaps, 10 citations)**
