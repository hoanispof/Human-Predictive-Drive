---
title: Love Romantic — Tình Yêu Đôi Lứa Qua Lens Framework v7.8
version: 2.2
created: 2026-03-29
rewritten: 2026-04-26
refined: 2026-05-11
status: RESEARCH FILE v2.2 — phân tích dựa trên framework v7.8 + established research
scope: |
  RESEARCH FILE: Phân tích tình yêu ĐÔI LỨA (romantic love) qua lens framework v7.8.
  Tình yêu = cơ chế GÌ, TẠI SAO evolution thiết kế vậy,
  CÁC GIAI ĐOẠN diễn ra thế nào, và MECHANISM map vào framework ra sao.
  v2.0 KEY CHANGES vs v1.0 (v7.5 era):
    ① Map vào 3 Generative Primitives (❶ Hardware × ❷ SPM F1/F2 × ❸ Valence)
    ② 2-Luồng Reward: L1 SPM-owned momentary + L2 Entity-owned structural
    ③ Body-Base Extension: partner → phần mở rộng body-base CỦA TÔI
    ④ Chunk dynamics: Shift/Miss/Gap/Compound cho mọi giai đoạn
    ⑤ 5 Cortisol Roles phân biệt rõ trong từng context
    ⑥ Cross-refs updated toàn bộ v7.8 files
  v2.2 ADDITIONS:
    ⑦ Type A/B Reward dimension mapped vào love (RSA v1.0)
    ⑧ Collective-Body cross-ref: societal schemas × partner selection
    ⑨ PFC-Configuration reference: limerence = Mode ③ Reconfigured
    ⑩ Renamed: Love-Analysis.md → Love-Romantic.md (phân biệt Love-Unified.md)
  ⚠️ File này giải thích MECHANISM — KHÔNG nói "tình yêu chỉ là hóa chất."
  Cơ chế ≠ trải nghiệm. Biết cơ chế giúp NAVIGATE, không giảm giá trị trải nghiệm.
purpose: |
  Research-level analysis: apply framework v7.8 vào hiện tượng phức tạp nhất
  con người trải nghiệm. Love = test case cho toàn bộ framework:
  connection, SPM, valence, chunk dynamics, cortisol, protect, meaning,
  obligation, gratitude — TẤT CẢ hội tụ.
  PHẠM VI: romantic love (đôi lứa). Mọi dạng love khác → Love-Unified.md.
position: |
  Research/ — analysis file, KHÔNG phải mechanism/observation file.
  Ngang hàng OCD-Analysis.md, Climate-Cognition.md, Love-Unified.md.
  Love-Romantic.md = romantic DEEP-DIVE. Love-Unified.md = ALL love types UNIFIED VIEW.
dependencies:
  - Connection.md v3.1 — 3 Generative Primitives, 8 pathways, §15 chunk dynamics
  - Agent-Mechanism.md — SPM mechanism, §12 body-need feeder, §12.2b 2-luồng
  - Self-Pattern-Match.md v2.1 — F1/F2, 5 Pattern-Types, 4 axes, reversed mapping
  - Pattern-Resonance.md — emergent mutual, 4 conditions, calibration loop
  - Valence-Propagation.md v1.4 — per-entity valence, §2 Body-Base Extension, chain
  - Body-Feedback-Mechanism.md v1.2 — Chunk-Shift/Miss/Gap, §4 Compound, §5 Baseline Shift
  - Reward-Signal-Architecture.md v1.0 — Type A/B, A Gates B, 5 Profiles
  - Cortisol-Baseline.md v2.0 — 5 Cortisol Roles §7.7, cascade, inertia, recovery asymmetry
  - Protect.md v1.0 — f(replaceability × attachment), loss aversion, vasopressin
  - Meaning.md v2.0 — 5 anchor types, anchor collapse
  - Obligation.md v1.0 — compiled prediction, relationship obligation
  - Gratitude.md v1.1 — Type A gratitude between partners
  - Empathy.md v2.0 — SPM F1 applied, 2-luồng organic, burnout
  - Status.md v2.0 — Resource Access Map, mutual status exchange
  - Autonomy-Hardware.md — efference copy, controllability
  - Autonomy.md — over-convergence penalty
  - PFC-Function.md v1.2 — 24 functions, HOLD + PROCESS
  - PFC-Configuration.md v1.0 — 6 modes, limerence = Mode ③ Reconfigured
  - Chunk.md v2.0 — compilation, substrate, hierarchy
  - Imagine-Final.md — reference pattern, 14 clarity levels
  - Feeling.md v2.1 — PFC observation interface, 7-layer fidelity, §6.5 Type A/B
  - Collective-Body.md v1.1 — Model 3 cấp, Type C compile, collective schemas
  - Clarification/Dopamine-Reward-Rejection.md — dopamine ≠ reward
  - OCD-Analysis.md v2.1 — serotonin × obsessive patterns (link limerence)
sources_backup: |
  v1.0 (2026-03-29, 969L, v7.5 era) → backup/Love-Analysis-v75-era.md
  v2.1 (2026-04-26, ~2,061L) → renamed from Love-Analysis.md
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Love Romantic — Tình Yêu Đôi Lứa Qua Lens Framework v7.8

> **2 người lạ gặp nhau. Body CẢ HAI bỗng fire đồng loạt.**
> **Dopamine: "CHÚ Ý NGƯỜI NÀY!" Oxytocin: "GẦN HƠN." Serotonin ↓: "KHÔNG NGỪNG NGHĨ."**
> **PFC: "... không thấy có gì sai cả."**
>
> Đây KHÔNG phải 1 cảm xúc. Là 1 DRIVE — cùng level với đói, khát (Fisher 2004 🟢).
> Evolution thiết kế: 2 người LẠ → ở CÙNG NHAU đủ lâu → giao phối → nuôi con.
> Cần: multi-channel activation (1 channel không đủ giữ).
> Cần: CÓ THỜI HẠN (sau khi con đủ lớn → không cần hijack nữa).
> Riêng con người: cần THÊM bước giảm PFC (vì PFC mạnh sẽ ĐÁNH GIÁ → có thể REJECT).
>
> Framework v7.8 giải thích TẤT CẢ giai đoạn này bằng 3 primitives:
> ❶ Hardware Social Drive × ❷ SPM (F1 Feeling + F2 Logic) × ❸ Per-Agent Valence.
> Limerence = ❶ FLOOD + ❷ COMPOSITE fire + ❸ SHIFT mạnh → Body-Base Extension compile.
> Attachment = ❶ maintenance + ❷ library SÂU + ❸ stable → L2 structural reward.
> Break-up = Body-Base Extension BỊ CẮT → compound grief 8 pathways.
>
> Biết cơ chế ≠ bớt yêu. Biết cơ chế = yêu + NAVIGATE được.

---

## Mục lục

- §0 — VỊ TRÍ + SCOPE
- §1 — TÌNH YÊU = CƠ CHẾ GÌ
- §2 — HORMONE COCKTAIL — CÁI GÌ XẢY RA TRONG NÃO
- §3 — MAP VÀO V7.8: 3 GENERATIVE PRIMITIVES × LOVE
- §4 — 2-LUỒNG REWARD: TẠI SAO "YÊU SÂU" KHÁC "THÍCH"
- §5 — PFC SELECTIVE BLINDNESS
- §6 — "CÀNG CẤM CÀNG YÊU" — ROMEO & JULIET EFFECT
- §7 — "CHỌN NHẦM" — TRAUMA CHUNKS × PARTNER SELECTION
- §8 — TỐI ƯU TRƯỚC — COMPILED RED/GREEN FLAGS
- §9 — LIMERENCE = GIFT + WINDOW + FUEL
- §10 — TRANSITION: LIMERENCE → ATTACHMENT
- §11 — BONDING LÂU DÀI — DUY TRÌ CONNECTION THẬT
- §12 — BREAK-UP: COMPOUND GRIEF QUA 8 PATHWAYS
- §13 — HONEST ASSESSMENT
- §14 — CROSS-REFERENCES + STATUS

---

## §0 — VỊ TRÍ + SCOPE

```
⭐ FILE NÀY TRONG FRAMEWORK:

  Research/ folder — PHÂN TÍCH, KHÔNG phải mechanism/observation.
  Apply toàn bộ framework v7.8 vào 1 hiện tượng cụ thể: tình yêu ĐÔI LỨA.

  LOVE = TEST CASE CHO FRAMEWORK:
    → Connection: 3 primitives ❶❷❸ fire TẤT CẢ ở max
    → SPM: F1+F2 composite fire MẠNH NHẤT con người trải nghiệm
    → Valence: neutral → strong positive → Body-Base Extension
    → Chunk dynamics: Shift + Miss + Gap + Compound — ĐỦ HẾT
    → Cortisol: 5 roles xuất hiện ở CÁC GIAI ĐOẠN KHÁC NHAU
    → Protect: partner = replaceability CỰC THẤP
    → Meaning: partner có thể trở thành Anchor-Schema
    → Obligation: relationship tạo obligation compound
    → Gratitude: Type A gratitude giữa partners
    → Autonomy: balance individual growth vs convergence
    → Type A/B Reward: love involve CẢ 2 (v2.2 — RSA v1.0)
    → Collective-Body: societal norms × partner selection (v2.2)

  PHÂN BIỆT:
    File NÀY: ROMANTIC love deep-dive qua framework lens
    Love-Unified.md: ALL love types unified view qua L2 mechanism
    Connection.md: mechanism file — 3 primitives, 8 pathways
    Empathy.md: observation parameter — SPM F1 output
    Protect.md: observation parameter — loss aversion mechanism
    = File này DÙNG các mechanism files, KHÔNG duplicate chúng


  QUY ƯỚC CONFIDENCE:
    🟢 Research support — peer-reviewed, replicated
    🟡 Framework synthesis — consistent với data, chưa mainstream term
    🔴 Hypothesis — testable prediction, chưa verified
```

---

## §1 — TÌNH YÊU = CƠ CHẾ GÌ

```
⭐ TÌNH YÊU = MULTI-SYSTEM ACTIVATION mạnh nhất mà evolution thiết kế:

  KHÔNG phải 1 cảm xúc → là 1 DRIVE (Fisher 2004 🟢):
    → Cùng level với đói, khát → KHÔNG thể "chọn" yêu hay không
    → Body fire TRƯỚC → PFC "giải thích" sau
    → = "Tại sao yêu?" → "vì yêu" = PFC verbalize CÁI body ĐÃ quyết
    → = Body CÓ Imagine-Final preview về partner:
        preview "tương lai CÓ NGƯỜI NÀY" → body pre-feel → approach
        (Imagine-Final.md §1: body preview ~20-60% fidelity)

  MỤC ĐÍCH EVOLUTION:
    → 2 người LẠ → ở lại CÙNG NHAU đủ lâu → giao phối → nuôi con sơ sinh
    → Cần: multi-system activation (1 system không đủ mạnh để giữ)
    → Cần: CÓ THỜI HẠN (sau khi con đủ lớn → không cần flood nữa)
    → Ở con người thêm: override PFC judgment
      (nếu PFC đánh giá kỹ → có thể reject bond trước khi pair bond compile)


  CƠ CHẾ GỐC — chung với ĐỘNG VẬT (🟢 Young & Wang 2004):

    PAIR BOND = oxytocin + vasopressin receptors ở REWARD AREAS:
      → Receptor density CAO → gần người kia = REWARD → pair bond
      → 🟢 Prairie vole: receptor density CAO → pair bond suốt đời
      → 🟢 Montane vole: receptor density THẤP → giao phối xong bỏ
      → = CÙNG loài, KHÁC receptor density = KHÁC hành vi
      → = Pair bond = HARDWARE (receptor distribution),
          KHÔNG phải "quyết định"

  RIÊNG CON NGƯỜI — thêm bước giảm PFC:

    Con người CÓ bonding mechanism giống động vật (oxytocin/vasopressin).
    NHƯNG con người CÓ PFC mạnh → PFC sẽ ĐÁNH GIÁ, CÂN NHẮC, có thể REJECT.
    Evolution giải quyết: reward flood → PFC TỰ GIẢM evaluate ở context partner.

    = Limerence = bonding mechanism (giống động vật)
                 + PFC tự giảm (RIÊNG con người, vì PFC mạnh sẽ cản)
    → = "Giảm PFC" KHÔNG TẠO RA tình yêu
    → = "Giảm PFC" BỎ RÀO CẢN để bonding HOẠT ĐỘNG

  SO SÁNH:
    Thiên nga: bonding = HARDWARE (receptor) → suốt đời, PFC yếu → không cần giảm
    Prairie vole: bonding = HARDWARE (receptor) → suốt đời, PFC yếu → không cần giảm
    Con người: bonding = HARDWARE + PFC tự giảm (vì PFC sẽ cản)
              → phase 1 TỰ ĐỘNG (limerence) → phase 2 CÓ CHỌN LỰC (PFC bật lại)
    → = LOÀI DUY NHẤT: phase 1 tự động + phase 2 CÓ THỂ CHỌN tiếp hay dừng


  3 GIAI ĐOẠN (Fisher 2004 🟢):

    ① LUST (ham muốn): testosterone + estrogen → "muốn gần"
    ② LIMERENCE (say đắm): dopamine ↑ + NE ↑ + serotonin ↓ + PFC ↓ → "ám ảnh + mù"
    ③ ATTACHMENT (gắn bó): oxytocin + vasopressin + PFC BẬT LẠI → "ở lại CÓ ĐÁNH GIÁ"
    → 3 giai đoạn CÓ THỂ overlap, KHÔNG nhất thiết tuần tự
    → Limerence = giai đoạn MẠNH NHẤT + NGẮN NHẤT + tạo "mù quáng"


  🟡 MAP V7.8 — LOVE QUA 3 GENERATIVE PRIMITIVES:

    (Chi tiết §3)

    ┌──────────┬────────────────────────┬───────────────────────────────┐
    │ Stage    │ 3 Primitives           │ Body-Base Extension           │
    ├──────────┼────────────────────────┼───────────────────────────────┤
    │ Lust     │ ❶ hardware ACTIVATE    │ Chưa                          │
    │          │ ❷ SPM thin fire        │                               │
    │          │ ❸ valence neutral→+    │                               │
    ├──────────┼────────────────────────┼───────────────────────────────┤
    │ Limerence│ ❶ hardware FLOOD       │ ĐANG compile:                 │
    │          │ ❷ SPM COMPOSITE max    │ partner → body-base extension │
    │          │ ❸ valence STRONG +     │ (quá trình GRADIENT)          │
    ├──────────┼────────────────────────┼───────────────────────────────┤
    │ Attach-  │ ❶ hardware MAINTAIN    │ ĐÃ compiled                   │
    │ ment     │ ❷ SPM library DEEP     │ (nếu match thật)              │
    │          │ ❸ valence STABLE       │ hoặc KHÔNG (nếu mismatch)     │
    └──────────┴────────────────────────┴───────────────────────────────┘

    → Limerence = giai đoạn Body-Base Extension COMPILE
    → Attachment BỀN = L2 structural đã compile THÀNH CÔNG
    → Attachment KHÔNG bền = L2 chưa compile → chỉ còn L1 → hết motivation
```

---

## §2 — HORMONE COCKTAIL — CÁI GÌ XẢY RA TRONG NÃO

### §2.1 — Limerence: 6 tháng → 3 năm

```
🟢 LIMERENCE — MULTI-SYSTEM ACTIVATION ĐỒNG THỜI:

  TĂNG:

    DOPAMINE — VTA salience circuit CỰC MẠNH (VTA + caudate nucleus):
      → Dopamine = KHÔNG PHẢI reward → là signal "CHÚ Ý! QUAN TRỌNG!"
        (Dopamine-Reward-Rejection.md: dopamine = chuông cửa, KHÔNG phải quà)
      → Partner liên tục được đánh dấu = TOP PRIORITY trong attention
      → = Cùng vùng với cocaine, gambling (salience/motivation)
      → = "Nghiện người" = salience hijack — não KHÔNG NGỪNG chú ý partner
      🟢 Fisher, Aron et al. 2005 (fMRI)

    NOREPINEPHRINE — arousal + energy:
      → Tim đập, mất ngủ, hồi hộp, energy cao
      → = "Không ăn không ngủ được" = NE effect

    OXYTOCIN + VASOPRESSIN — bonding:
      → Chạm, ôm, sex → oxytocin spike
      → Vasopressin → "bảo vệ BOND NÀY"
        (Protect.md §4.1: vasopressin = defense side of bonding)

    CORTISOL — change-readiness amplifier:
      → Cortisol-Baseline.md §7.7 Role ① Compile Direction:
        chunks compile ở hướng APPROACH (novelty-flavored)
      → Yêu = BIẾN ĐỘNG CỰC LỚN → body fire cortisol amplify change
      → = "Yêu" ≠ "chỉ sướng" → body ĐANG ở trạng thái RECALIBRATE
      → Cortisol khi yêu ≠ cortisol khi sợ:
        YÊU: Role ① Compile Direction (APPROACH) + Role ② Holding ("muốn gặp")
        SỢ: Role ③ Threat-sustained (AVOIDANCE)
        = CÙNG hormone, KHÁC role, KHÁC direction

  GIẢM:

    SEROTONIN — GIẢM ~40% so với bình thường:
      → = CÙNG MỨC với OCD patients
      → = "Ám ảnh" về người kia = CƠ CHẾ OCD
      → = Nghĩ LIÊN TỤC, không dừng được = serotonin thấp
      🟢 Marazziti et al. 1999
      → Qua lens chunk dynamics (Body-Feedback-Mechanism.md):
        Serotonin ↓ → spreading activation LESS INHIBITED
        → Chunks về partner fire → cascade tới related chunks
        → MỖI chunk fire → spread tới thêm partner chunks → LOOP
        → = Obsessive thinking = UNINHIBITED SPREADING ACTIVATION

      ⭐ SEROTONIN ↓ = AMPLIFIER, KHÔNG PHẢI ROOT CAUSE:
        (Chi tiết: OCD-Analysis.md v2.1 §4.5)

        Root cause trong love = GENUINE UNCERTAINTY:
          → SPM library về partner gần TRỐNG (mới gặp)
          → Obligation chưa compile ("tôi phải trả GÌ để giữ?")
          → Có thể childhood SPM bias (§7.3)
        → Body ở trạng thái uncertainty THẬT
        → Serotonin ↓ = body's RESPONSE (giảm certainty bias = hợp lý)
        → Serotonin ↓ → AMPLIFY loop (spreading activation uninhibited)
        → = CONSEQUENCE + AMPLIFIER, không phải initiator

        Parallel cortisol (Cortisol-Baseline.md):
          "Cortisol = amplifier, NOT cause. Đau từ 3 nguồn KHÁC."
          "Serotonin = amplifier of uncertainty. Uncertainty từ nguồn KHÁC."

        🟢 Evidence support:
          → Love tự resolve 12-18 tháng: bond compile → uncertainty ↓
            → serotonin TỰ phục hồi (root resolved → amplifier follows)
          → SSRIs → bỏ → relapse ~80%: fix amplifier, không fix root
          → CBT → relapse chỉ ~20-30%: fix root (chunks) → stable

  OPIOID — BODY REWARD THẬT:
    → Gần partner: opioid release (body-need met — Connection §0)
    → Ôm, chạm, sex, eye contact: oxytocin → opioid cascade
    → Conversation resonance: Pattern-Resonance → SPM reward
    → = REWARD THẬT từ body, KHÔNG phải "ảo"
    → = Dopamine NÓI "chú ý!" → Opioid THÌ mới "thưởng thật"
      (03-Reward.md: dopamine = chuông cửa, opioid = quà thật)


  ⭐ TYPE A/B DIMENSION TRONG LOVE (v2.2 — RSA v1.0):

    Love reward KHÔNG đồng nhất — có 2 loại ORTHOGONAL:

    ┌──────────────────┬────────────────────────┬───────────────────────┐
    │ Love reward      │ Type A (Evaluative)    │ Type B (Direct State) │
    ├──────────────────┼────────────────────────┼───────────────────────┤
    │ Cơ chế           │ Opioid hedonic hotspot │ CT afferents,         │
    │                  │ qua chunk evaluation   │ eCB, body-state       │
    ├──────────────────┼────────────────────────┼───────────────────────┤
    │ Ví dụ            │ Conversation resonance │ Ôm, chạm, massage    │
    │                  │ Insight chung          │ Co-sleep, warmth      │
    │                  │ Praise, validation     │ Sex (B component)     │
    │                  │ Shared beauty          │ Eye contact (partial) │
    ├──────────────────┼────────────────────────┼───────────────────────┤
    │ Cần chunks?      │ YES — compiled library │ MINIMAL — hardware    │
    ├──────────────────┼────────────────────────┼───────────────────────┤
    │ Habituate?       │ CÓ — VTA adaptation    │ ÍT — sensor-level     │
    ├──────────────────┼────────────────────────┼───────────────────────┤
    │ Limerence effect │ PFC ↓ → A gate GIẢM   │ B VẪN full →          │
    │                  │ → evaluation yếu       │ touch CÒN MẠNH HƠN   │
    └──────────────────┴────────────────────────┴───────────────────────┘

    → A Gates B (RSA §3): Type A evaluation CAN amplify OR suppress Type B:
      Partner (trusted) → A amplifies B → touch compound pleasant
      Stranger → A overrides B → touch unpleasant DÙ CT fire
      (🟢 Löken 2009: CT afferents fire GIỐNG — khác biệt = A gate)

    → LIMERENCE: PFC giảm (§2.2) → A evaluation gate GIẢM:
      → Type B signals LESS GATED → touch/closeness feel MORE RAW + INTENSE
      → Type A signals LESS EVALUATED → "mọi thứ partner nói đều hay"
      → = Tại sao body contact CỰC MẠNH trong limerence

    → ATTACHMENT LÂU DÀI (§11): A habituates, B ÍT habituate:
      → Conversation novelty giảm → Type A reward giảm tự nhiên
      → Touch VẪN reward (CT hardware, RSA §1.4 evolutionary floor)
      → = Type B = "safe baseline reward" cho bonding lâu dài
      → = Tại sao physical affection DUY TRÌ bond khi novelty Type A giảm

    → L1/L2 (§4) ORTHOGONAL với A/B:
      L1 momentary chứa CẢ Type A moments + Type B moments
      L2 structural compile từ TÍCH LŨY cả A + B qua thời gian
      → 2 dimensions KHÁC NHAU, KHÔNG thay thế nhau

    (Chi tiết Type A/B: Reward-Signal-Architecture.md §1-§3)
```

### §2.2 — PFC + Amygdala GIẢM khi yêu — NHƯNG TẠI SAO?

```
🟢 ĐO ĐƯỢC (fMRI — không thể chối cãi):
  → Lateral PFC ↓ + amygdala ↓ KHI XEM ẢNH người yêu
    (Bartels & Zeki 2000, 2004; Fisher et al. 2005)
  → ⚠️ Đo TRONG CONTEXT "nhìn/nghĩ về partner" — KHÔNG phải 24/7
  → ⚠️ Người đang yêu VẪN làm việc bình thường, đánh giá đồng nghiệp OK
  → = PFC giảm CHỈ TRONG CONTEXT partner, không phải MỌI context

  → Serotonin ↓ ~40% (mãn tính — baseline thay đổi) → obsessive thinking
    (Marazziti 1999)
  → Oxytocin tiêm → amygdala giảm (Kirsch et al. 2005)


🟡 MAINSTREAM SUY ĐOÁN:
  → "Chemicals TRỰC TIẾP suppress PFC" — chemicals → ép tắt PFC
  → ⚠️ VẤN ĐỀ: hormones KHÔNG biết phân biệt schema
    → Hormones flood TOÀN BỘ não → không target "chỉ suy nghĩ về partner"
    → NẾU suppress toàn cục → sao vẫn làm việc bình thường ở công ty?
    → NẾU suppress toàn cục → sao chỉ "mù" về partner mà không mù mọi thứ?
    → = "Selective blindness" KHÓ GIẢI THÍCH bằng global chemical suppress


🟡 FRAMEWORK HYPOTHESIS — PFC TỰ GIẢM VÌ BODY SMOOTH:
  (Chi tiết §5)

  PFC KHÔNG BỊ ÉP TẮT — PFC TỰ GIẢM VÌ KHÔNG CÓ VIỆC:

    Khi ở cùng/nghĩ về partner:
      → ❶ Hardware FLOOD: social input MET ở tất cả channels
      → ❷ SPM fire COMPOSITE: body simulate partner → SMOOTH
      → ❸ Valence strong positive: MỌI channel body-base = rewarded
      → PFC nhận: "mọi kênh smooth, reward THẬT, RÕ RÀNG"
      → PFC reactive (PFC-Function.md §2): body smooth → PFC không được gọi
      → Không có compiled red flags fire → PFC: "không có data để nghi ngờ"
      → = PFC ĐÚNG dựa trên data hiện có — data KHÔNG ĐẦY ĐỦ thôi

    Khi ở công ty (context khác):
      → ❶ Hardware: social channels KHÁC hoạt động
      → ❷ SPM: fire trên đồng nghiệp (khác chunk library)
      → ❸ Valence: NEUTRAL/MIXED → PFC CÓ VIỆC evaluate
      → = PFC KHÔNG giảm ở context này → selective blindness TỰ NHIÊN

  TẠI SAO MODEL NÀY TỐT HƠN:
    → Giải thích selective blindness (chỉ mù về partner)
    → Giải thích vẫn function bình thường ở context khác
    → Chỉ cần 1 cơ chế (reward flood → PFC tự giảm)
    → Consistent với PFC reactive model (PFC-Function.md)

  ⭐ PFC-CONFIGURATION MODE (v2.2 — PFC-Configuration.md v1.0):

    Limerence = PFC Mode ③ RECONFIGURED (selective functional changes):
      → dlPFC (judgment): GIẢM ở context partner, VẪN hoạt động context khác
      → mPFC (self-reference): TĂNG (partner integrated vào self-model)
      → vmPFC (value): BIASED positive cho partner
      → OFC (reward): OVERACTIVE cho partner stimuli
      → = KHÔNG phải Mode ④ Disconnected (threat/trauma — global offline)
      → = KHÔNG phải Mode ① Normal (PFC bình thường)
      → = Mode ③: CHỌN LỌC — một số functions giảm, một số tăng
        (PFC-Configuration §3: 24 functions × 6 modes)

    SO SÁNH 3 "loss of self" liên quan love:
      Limerence: Mode ③ (judgment suppress, self-reference tăng)
      Heartbreak acute: Mode ④ Disconnected (nếu trauma-level)
      Attachment bền: Mode ① Normal (PFC bình thường, CÓ evaluate)


  ⭐ HỆ QUẢ — COMPILED CHUNKS VẪN CHẠY:

    PFC giảm ở context partner. NHƯNG compiled chunks (Chunk.md v2.0)
    tồn tại ở C+D zones → CHẠY Ở VÔ THỨC, KHÔNG CẦN PFC:

    → Red flags ĐÃ COMPILED → VẪN fire: body "KỲ KỲ"
    → Body "kỳ kỳ" = counter-evidence → PFC CÓ DATA để evaluate ngược
    → = Tại sao MỘT SỐ người vẫn detect bad partner dù đang limerence
    → = Và tại sao compile red flags TRƯỚC khi yêu = QUAN TRỌNG (§8)

    Nếu framework hypothesis đúng (PFC tự giảm, không bị ép):
      → Compiled red flags → fire → PFC CÓ DATA MỚI → PFC BẬT LẠI
      → = Compiled red flags CÓ THỂ KÉO PFC BẬT LẠI
      → = Đây là hy vọng lớn nhất cho "bảo vệ khi yêu"


  ⭐ VERIFICATION — so sánh PFC suppress THẬT (threat) vs limerence:

    PFC suppress THẬT (hổ nhảy ra / bị cướp cầm dao):
      → Amygdala fire CỰC MẠNH → cortisol + adrenaline SPIKE
      → PFC OFFLINE thật: KHÔNG tính toán, KHÔNG nói logic
      → Body tự động: chạy / đứng im / ngất
      → Scope: TOÀN BỘ cognitive offline
      → Thời gian: giây → phút (acute)
      → Cortisol Role ③ Threat-sustained: AVOIDANCE direction

    Limerence ("suppress"):
      → VẪN làm việc, VẪN lái xe, viết code, tính toán
      → CHỈ không evaluate PARTNER → mọi thứ khác OK
      → Scope: CHỈ 1 context (partner) → phần còn lại BÌNH THƯỜNG
      → Thời gian: tháng → năm (chronic)
      → Cortisol Role ① Compile Direction: APPROACH direction

    → = 2 trạng thái HOÀN TOÀN KHÁC NHAU
    → = NẾU limerence suppress PFC giống threat:
        → Người yêu KHÔNG THỂ làm việc → SAI
        → Người yêu fight/flight/freeze → SAI (thực tế: vui và hào hứng)
    → = Limerence KHÔNG suppress PFC giống threat
    → = PFC TỰ GIẢM (selective) ≠ PFC BỊ TẮT (global)


  ⚠️ NHƯNG: có thể CẢ HAI (chưa tách rõ):
    → Kirsch 2005: oxytocin tiêm → amygdala giảm → có vẻ DIRECT
    → Nhưng: oxytocin có thể tạo "safe feeling" → amygdala tự giảm
    → fMRI KHÔNG PHÂN BIỆT: "bị ép tắt" vs "không có việc" → nhìn GIỐNG
    → Cần study: tiêm oxytocin + cho xem red flags → amygdala fire hay không?
      → Fire: amygdala không bị ép → chỉ "không có việc" → framework đúng
      → Không fire: có direct suppress → mainstream đúng phần này
```

---

## §3 — MAP VÀO V7.8: 3 GENERATIVE PRIMITIVES × LOVE

```
⭐ CONNECTION V3.0 CUNG CẤP TẦNG SINH CHO LOVE:

  v7.5 (cũ): Love = "multi-channel hijack" (MÔ TẢ)
  v7.8 (mới): Love = ❶ × ❷ × ❸ fire ở MAX (PREDICT)

  3 Generative Primitives (Connection.md §3) PREDICT toàn bộ love behavior.
  Love = trường hợp CỰC ĐOAN của connection —
  tất cả 3 primitives fire ĐỒNG THỜI ở mức CAO NHẤT.
```

### §3.1 — Primitive ❶: Hardware Social Drive FLOOD

```
🟡 LIMERENCE = ❶ HARDWARE ĐƯỢC FEED Ở MỌI CHANNEL:

  ❶ Hardware Social Drive = body CẦN social input (Connection §3.1).
  Bình thường: ❶ được feed TỪNG PHẦN bởi NHIỀU agents.
  Limerence: 1 agent DUY NHẤT feed GẦN NHƯ TẤT CẢ:

  ┌──────────────────┬──────────────────────────┬───────────────────────┐
  │ Hardware channel  │ Feed bình thường         │ Feed khi limerence    │
  ├──────────────────┼──────────────────────────┼───────────────────────┤
  │ CT touch fibers  │ Ôm bạn bè (hiếm)        │ Ôm, chạm LIÊN TỤC   │
  │ (Löken 2009 🟢)  │                          │ → oxytocin FLOOD     │
  │ ⭐ = Type B reward│                          │ (RSA §1: hardware,   │
  │                  │                          │  ít habituate)        │
  ├──────────────────┼──────────────────────────┼───────────────────────┤
  │ Presence signal  │ Có người xung quanh      │ Partner = SOURCE ⑥   │
  │ (Coan 2015 🟢)   │ → cortisol ↓ nhẹ         │ → cortisol ↓↓ MẠNH  │
  ├──────────────────┼──────────────────────────┼───────────────────────┤
  │ Contingency      │ Bạn respond → satisfied  │ Partner respond MỌI  │
  │ (Tronick 1978🟢) │                          │ signal → OPTIMAL     │
  ├──────────────────┼──────────────────────────┼───────────────────────┤
  │ Social novelty   │ VTA fire nhẹ khi gặp lạ  │ VTA fire LIÊN TỤC   │
  │                  │                          │ (mọi thứ về partner  │
  │                  │                          │ đều "mới + hay")     │
  └──────────────────┴──────────────────────────┴───────────────────────┘

  → = 1 agent feed TẤT CẢ hardware channels mà bình thường cần NHIỀU agents
  → = Body PHÁT HIỆN: "agent NÀY = JACKPOT — feed mọi thứ cùng lúc"
  → = Salience CỰC CAO → VTA: "CHÚ Ý, KHÔNG ĐƯỢC MẤT AGENT NÀY"

  🟡 TẠI SAO HARDWARE PHÂN BIỆT "partner" vs "bạn thân":
    → Bạn thân: feed presence + contingency + novelty → ❶ MET PHẦN LỚN
    → Partner: feed TẤT CẢ trên + CT touch + sex + co-sleep + co-regulation
    → = Channels MÀ CHỈ intimate partner feed được
    → = Body CÓ channels RIÊNG cho intimate → giải thích tại sao
      "bạn thân" không thay thế "partner" ở body level
    → = Hardware design: BẮT BUỘC có 1 agent feed kênh intimate
```

### §3.2 — Primitive ❷: SPM Composite Fire CỰC MẠNH

```
🟡 LIMERENCE = SPM FIRE Ở MỨC CAO NHẤT CON NGƯỜI TRẢI NGHIỆM:

  SPM (Self-Pattern-Match.md v2.1) = solo forward simulation.
  2 Functions: F1 Feeling + F2 Logic → chạy SONG SONG.

  BÌNH THƯỜNG: SPM fire trên 1-2 Pattern-Types, moderate depth.
  LIMERENCE: SPM fire COMPOSITE — TẤT CẢ 5 Pattern-Types cùng lúc:

  ┌──────────────────┬──────────────────────────────────────────┐
  │ Pattern-Type     │ Fire khi limerence                        │
  ├──────────────────┼──────────────────────────────────────────┤
  │ Affective        │ Body simulate partner emotions CỰC MẠNH  │
  │ (emotion chunks) │ → "buồn cùng, vui cùng" intensified      │
  ├──────────────────┼──────────────────────────────────────────┤
  │ Somatic          │ Body co-fire posture, breathing, rhythm   │
  │ (body state)     │ → interpersonal synchrony (Feldman 2007🟢)│
  ├──────────────────┼──────────────────────────────────────────┤
  │ Visual-symbolic  │ Replay hình ảnh partner LIÊN TỤC         │
  │                  │ → "nhìn thấy mặt khi nhắm mắt"          │
  ├──────────────────┼──────────────────────────────────────────┤
  │ Verbal-cognitive │ Inner dialogue simulate conversation     │
  │                  │ → "tưởng tượng nói gì khi gặp"          │
  ├──────────────────┼──────────────────────────────────────────┤
  │ Composite        │ TẤT CẢ fire cùng lúc → native mode      │
  │ (full blend)     │ → "nghĩ về partner" = ALL modalities    │
  └──────────────────┴──────────────────────────────────────────┘


  SPM LIBRARY BUILD CỰC NHANH:

    Limerence cung cấp 3 điều kiện TỐI ƯU cho library build:
    ① Salience CỰC CAO (VTA fire liên tục) → attention → chunks COMPILE
    ② Time investment CỰC LỚN (muốn ở cùng mọi lúc) → exposure tối đa
    ③ Feedback-rich (face-to-face, full channels) → calibration NHANH

    → SPM library về partner build NHANH HƠN BẤT KỲ ai khác
    → Trong vài tháng limerence: library depth ≈ bạn thân nhiều NĂM
    → = Limerence = TURBO cho SPM library compilation


  4 AXES ĐỀU CAO (Agent-Mechanism.md §7):

    ① Pattern-Type: COMPOSITE (tất cả modalities) → best case
    ② Depth: BUILD CỰC NHANH (salience + time + motivation)
    ③ Similarity: SAME SPECIES + usually same culture → HIGH
    ④ Feedback: REAL-TIME RICH (face-to-face, full expression) → HIGH

    → = ALL 4 axes HIGH = best-case SPM quality
    → = TẠI SAO limerence tạo cảm giác "HIỂU nhau sâu quá"
      (thực ra: SPM library build nhanh → prediction accuracy tạm CAO
       → nhưng calibration chưa đủ deep → có thể SAI ở edge cases)


  PATTERN-RESONANCE FIRE MẠNH:

    2 partners đều fire SPM composite lên NHAU → Pattern-Resonance emerge:
    → "Cùng tần số" = Pattern-Resonance thành công
    → "Hiểu nhau không cần nói" = composite SPM match
    → Pattern-Resonance reinforcement → "YÊU HƠN" (2 systems positive loop)

    NHƯNG: Pattern-Resonance khi limerence = BIASED:
    → SPM library build NHANH → nhưng CHƯA ĐỦ calibrated
    → PFC giảm → error correction yếu → false matches không bị detect
    → = "Tưởng hiểu" có thể ≠ "hiểu thật"
    → = Chỉ khi PFC bật lại (phase 3) mới biết Pattern-Resonance có THẬT không
```

### §3.3 — Primitive ❸: Valence Shift → Body-Base Extension

```
⭐ QUÁ TRÌNH CỐT LÕI: VALENCE NEUTRAL → BODY-BASE EXTENSION

  Đây là BƯỚC NHẢY CHẤT mà chỉ agent valence tạo được.
  (Valence-Propagation.md §2)

  GRADIENT — KHÔNG phải 1 bước nhảy đột ngột:

  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │  GIAI ĐOẠN 1 — NEUTRAL (trước gặp):                             │
  │    → Partner chưa tồn tại trong chunk network                   │
  │    → Valence profile: trống                                      │
  │    → Body-Base Extension: 0                                      │
  │                                                                 │
  │  GIAI ĐOẠN 2 — SHIFT POSITIVE (gặp + lust):                     │
  │    → VTA fire prediction delta (người mới + attractive)          │
  │    → Valence profile: L1 positive (pleasant presence)            │
  │    → Vài channel bắt đầu active                                 │
  │    → Body-Base Extension: 0 (chưa compile)                      │
  │                                                                 │
  │  GIAI ĐOẠN 3 — STRONG POSITIVE (limerence):                     │
  │    → Multi-channel flooding + SPM composite fire                 │
  │    → Valence profile: DENSE, NHIỀU channels đồng loạt positive   │
  │    → Chunks compile CỰC NHANH (salience + repetition + peak)    │
  │    → Body-Base Extension: ĐANG COMPILE                           │
  │    → Body BẮT ĐẦU treat partner channels AS own channels        │
  │    → "Partner buồn → TÔI buồn" = body CỰC KỲ reactive          │
  │                                                                 │
  │  GIAI ĐOẠN 4 — BODY-BASE EXTENSION (attachment):                 │
  │    → Partner đã compile SÂU (years × multi-modal × peak valence) │
  │    → Valence profile: STABLE positive across channels             │
  │    → Body-Base Extension: COMPILED                                │
  │    → "Partner's wellbeing = MY wellbeing" (STRUCTURAL)            │
  │    → KHÔNG phụ thuộc từng episode → SUSTAINED                    │
  │    → Mất partner = "PHẦN CỦA TÔI BỊ CẮT"                       │
  │    → = Grief ≠ "tiếc" → grief = body-base AMPUTATION             │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘


  ĐIỀU KIỆN COMPILE BODY-BASE EXTENSION (VP §2):

    ① Nhiều interaction tích lũy → valence compile SÂU
    ② Trust CAO + Replaceability THẤP + Dependency có
    ③ SPM fire THÀNH CÔNG nhiều lần → valence reinforce
    → Body DẦN DẦN treat agent channels AS own channels
    → = Quá trình COMPILE, không phải quyết định ý thức


  ⭐ INSIGHT V7.8: "YÊU SÂU" = BODY-BASE EXTENSION ĐÃ COMPILE

    Object strong positive (xe yêu thích): valence ++, NHƯNG:
      → Mất xe = tiếc (resource loss)
      → Xe KHÔNG BAO GIỜ = "phần của tôi" ở body level

    Partner strong positive: valence ++, VÀ:
      → Partner = body-base extension (structural)
      → Partner's channels ĐƯỢC body treat AS own channels
      → Con đói = TÔI đói. Partner đau = TÔI đau.
      → Mất partner = PHẦN CỦA TÔI BỊ CẮT
      → = Tại sao grief ≠ "tiếc" — grief = body-base amputation

    → Object KHÔNG BAO GIỜ tạo body-base extension (VP §2):
      Object KHÔNG fire SPM → không có L1 episodes tích lũy
      Object KHÔNG bidirectional → không mutual reinforcement
      Object DỄ thay thế → trust/dependency không compile đủ sâu
```

---

## §4 — 2-LUỒNG REWARD: TẠI SAO "YÊU SÂU" KHÁC "THÍCH"

```
⭐ 2-LUỒNG REWARD = KEY DISTINCTION TRONG LOVE:

  (Valence-Propagation.md §2 + Connection.md §3.3 + SPM v2.1 §2.1)

  Khi interact với partner, body nhận 2 LUỒNG reward ĐỒNG THỜI:
```

### §4.1 — Luồng 1: SPM-owned, Momentary

```
🟡 LUỒNG 1 = BODY-FEEDBACK TỪ MỖI LẦN SPM F1 FIRE:

  Mỗi episode tương tác → SPM F1 fire → body simulate partner state:
    → Partner vui → F1: body vui nhẹ → L1 POSITIVE
    → Partner stress → F1: body khó chịu → L1 NEGATIVE
    → Partner kể chuyện hay → F1: excited → L1 POSITIVE
    → Partner cáu gắt → F1: defensive → L1 NEGATIVE

  ĐẶC TÍNH:
    → MOMENTARY — fire TỪNG EPISODE, hết episode → hết signal
    → SPM-owned — thuộc về SPM mechanism, KHÔNG thuộc per-agent valence
    → Có thể POSITIVE hoặc NEGATIVE tùy episode
    → Tồn tại với MỌI agent (bạn bè, đồng nghiệp, người lạ)
    → KHÔNG riêng cho love — love CHỈ tăng INTENSITY

  TRONG LIMERENCE: L1 CỰC MẠNH vì:
    → SPM fire COMPOSITE (5 Pattern-Types) → L1 amplitude CAO
    → Salience CỰC CAO → body pay attention MỌI signal từ partner
    → = "Mỗi biểu cảm của partner đều ẢNH HƯỞNG MẠNH đến mình"
    → = L1 positive khi partner vui = EUPHORIA
    → = L1 negative khi partner buồn = ĐAU CỰC KỲ (dù mình không bị gì)
```

### §4.2 — Luồng 2: Entity-owned, Structural

```
🟡 LUỒNG 2 = COMPILED VALENCE → BODY-BASE EXTENSION:

  Khi partner ĐÃ COMPILE thành body-base extension:
    → L2 fire BẤT KỂ L1 positive hay negative
    → SUSTAINED — không phụ thuộc từng episode
    → "Partner's wellbeing = MY wellbeing" (STRUCTURAL)

  ĐẶC TÍNH:
    → STRUCTURAL — compiled vào baseline, CHẠY LIÊN TỤC
    → Entity-owned — thuộc per-agent valence, KHÔNG thuộc SPM
    → Luôn POSITIVE (vì extension = body-base MỞ RỘNG)
    → CHỈ AGENT — object không bao giờ tạo được (VP §2)
    → CẦN THỜI GIAN compile — KHÔNG có ngay từ đầu

  TRONG LIMERENCE → ATTACHMENT: L2 ĐANG COMPILE:
    → Limerence cung cấp điều kiện tối ưu cho L2 compile:
      Repetition CAO + saliency CAO + peak valence CAO + multi-modal + contingency
      (BFM §5 compile_rate formula — TẤT CẢ factors ĐỀU CAO khi limerence)
    → L2 compile = gradient: từ "thích" → "thân" → "body-base extension"
    → NẾU L2 compile XONG trước khi limerence hết → relationship BỀN
    → NẾU L2 CHƯA compile → limerence hết → chỉ còn L1 → hết motivation
```

### §4.3 — 2 Luồng Interaction: Tại Sao Love KHÁC BIỆT

```
⭐ 2 LUỒNG INDEPENDENT — CÓ THỂ CONFLICT:

  ┌────────────────────────────┬───────────┬───────────┬──────────────────┐
  │ Tình huống                 │ L1        │ L2        │ Kết quả          │
  ├────────────────────────────┼───────────┼───────────┼──────────────────┤
  │ Partner vui, date đẹp      │ POSITIVE  │ POSITIVE  │ COMPOUND joy     │
  │ → L1 + L2 cùng hướng      │           │           │ (gặp partner =   │
  │                            │           │           │  cực tốt)        │
  ├────────────────────────────┼───────────┼───────────┼──────────────────┤
  │ Partner ốm, mình chăm     │ NEGATIVE  │ POSITIVE  │ VẪN CHĂM         │
  │ → L1: simulate ốm = khó   │ (cost     │ (partner  │ (L2 > L1 cost)   │
  │ → L2: partner = body-base │  THẬT)    │ = body-   │ = "sacrifice     │
  │   extension → chăm = feed │           │ base ext) │   CÓ THỂ CHỊU"  │
  │   body-base MÌNH           │           │           │                  │
  ├────────────────────────────┼───────────┼───────────┼──────────────────┤
  │ Bạn mới quen ốm           │ NEGATIVE  │ ≈ 0       │ Giúp nhưng GIỚI │
  │ → L1: empathy cost        │ (cost     │ (chưa     │ HẠN (L1 cost    │
  │ → L2: chưa compile        │  THẬT)    │ compiled) │ KHÔNG bù)       │
  │   body-base extension      │           │           │ → Burnout nếu   │
  │                            │           │           │   kéo dài       │
  ├────────────────────────────┼───────────┼───────────┼──────────────────┤
  │ Partner gây đau liên tục  │ NEGATIVE  │ POSITIVE  │ CONFLICT kéo dài │
  │ → L1: cost MẠNH mỗi lần   │ (cost     │ (vẫn     │ "Yêu nhưng đau" │
  │ → L2: vẫn extension       │ CỰC LỚN) │ compiled) │ → toxic nếu L1  │
  │                            │           │           │   cost > L2     │
  │                            │           │           │   → "phải rời"   │
  └────────────────────────────┴───────────┴───────────┴──────────────────┘


  ⭐ GIẢI THÍCH 4 CÂU HỎI PHỔ BIẾN:

  Q: "Tại sao mẹ chăm con ốm mà không burnout?"
  A: L2 compiled CỰC MẠNH (con = body-base extension years deep)
     → L2 > L1 cost → VẪN CHĂM, VẪN có sense of purpose
     (so sánh: bác sĩ chăm bệnh nhân lạ → L2 ≈ 0 → burnout)

  Q: "Tại sao yêu sâu KHÁC thích?"
  A: "Thích" = L1 positive (mỗi episode reward). "Yêu sâu" = L2 compiled
     (structural, sustained). L2 tạo ra "yêu dù partner đang xấu tính"
     mà "thích" KHÔNG làm được.

  Q: "Tại sao biết người kia xấu mà vẫn không bỏ được?"
  A: L1 negative liên tục (PFC biết "xấu"). NHƯNG L2 đã compiled
     (body-base extension KHÔNG xóa được bằng PFC logic).
     L2 compiled = body-level, C+D zones. PFC chỉ observe, không delete.
     → Recovery cần L2 DẦN WEAKEN (no contact → chunks decay → L2 giảm).

  Q: "Tại sao chia tay người mình không yêu cũng buồn?"
  A: L2 có thể compile ở mức TRUNG BÌNH (habit, routine, presence signal)
     DÙ L1 không đặc biệt positive. Mất = Chunk-Miss ở compiled baseline.
     → "Không yêu" nhưng "quen" → mất = body dissonance THẬT.
```

---

## §5 — PFC SELECTIVE BLINDNESS

```
⭐ ĐÂY LÀ HYPOTHESIS MẠNH NHẤT CỦA FILE:

  "PFC GIẢM KHI YÊU" — mainstream nói chemicals ép tắt.
  Framework nói: PFC TỰ GIẢM vì body smooth trong context partner.

  (§2.2 đã trình bày chi tiết cơ chế + verification)

  SECTION NÀY: deep drill vào HỆ QUẢ THỰC TẾ.
```

### §5.1 — PFC "Mù" có CHỌN LỌC

```
🟡 SELECTIVE BLINDNESS — MÙ CHỈ VỀ PARTNER:

  Nếu PFC bị "tắt" (suppress thật):
    → Phải mù MỌI THỨ → người yêu KHÔNG THỂ đi làm
    → NHƯNG: người yêu VẪN đi làm, VẪN đánh giá đồng nghiệp, VẪN logic

  Nếu PFC "tự giảm vì smooth" (framework):
    → Chỉ mù ở CONTEXT partner (body smooth → PFC không được gọi)
    → Ở context KHÁC: PFC bình thường (body có dissonance → PFC hoạt động)
    → = SELECTIVE — chính xác match observation

  MAP VÀO PFC-FUNCTION.MD:
    PFC 24 functions × 5 categories (OBSERVE → HOLD → PROCESS → ORCHESTRATE → STRATEGIC)
    → Limerence: PFC VẪN chạy TẤT CẢ 24 functions ở mọi context KHÁC
    → CHỈ ở context partner: OBSERVE nhận "smooth" → PROCESS "không cần evaluate"
    → = PFC ĐÚNG quy trình — chỉ data input KHÔNG ĐẦY ĐỦ
```

### §5.2 — Compiled Chunks = Hệ Thống Bảo Vệ

```
🟡 COMPILED RED FLAGS VẪN CHẠY DÙ PFC GIẢM:

  PFC operate ở A zone (prefrontal cortex).
  Compiled chunks tồn tại ở C+D zones (subcortical + peripheral).
  PFC giảm ≠ C+D zones giảm.

  ┌──────────────────────────────────────────────────────────────┐
  │ RED FLAGS CHỈ Ở PFC (đọc list, biết lý thuyết):              │
  │   → PFC giảm → red flags MẤT                                 │
  │   → "Biết" partner kiểm soát nhưng KHÔNG feel sai            │
  │                                                               │
  │ RED FLAGS ĐÃ COMPILED (trải nghiệm, feel, body đã lưu):     │
  │   → PFC giảm → red flags VẪN FIRE ở C+D zones               │
  │   → Body "kỳ kỳ" khi partner kiểm soát → PFC CÓ DATA MỚI    │
  │   → PFC: "body đang signal gì đó" → BẬT evaluate LẠI        │
  │                                                               │
  │ = COMPILED RED FLAGS CÓ THỂ KÉO PFC BẬT LẠI                 │
  │ = Red flags ở body level > red flags ở PFC level              │
  └──────────────────────────────────────────────────────────────┘

  TESTABLE PREDICTION 🔴:
    → So sánh 2 nhóm: có "trải nghiệm" red flags vs chỉ "đọc" red flags
    → Nhóm trải nghiệm → detect bad partner NHANH HƠN khi đang limerence
    → Vì: chunks compiled → fire ở C+D → không cần PFC
```

### §5.3 — Tại Sao Có Người "Tỉnh" Sớm Hơn

```
🟡 INDIVIDUAL VARIATION TRONG "MÙ":

  Người A: limerence 6 tháng → "tỉnh" → thấy red flags
  Người B: limerence 3 năm → vẫn "mù"
  TẠI SAO?

  3 factors quyết định tốc độ "tỉnh":

  ① COMPILED RED FLAG LIBRARY DEPTH:
    → Nhiều trải nghiệm (bị lừa, quan sát bạn bè, nghe kể, đọc sách)
    → Chunks compiled SÂU → fire MẠNH dù PFC giảm → "tỉnh" sớm
    → Ít trải nghiệm → chunks thin → không đủ mạnh override body smooth

  ② SPM LIBRARY CALIBRATION:
    → SPM library về partner CÓ được calibrate bởi Pattern-Resonance không?
    → Nếu CÓ external feedback (bạn bè nhận xét) → calibrate nhanh
    → Nếu CÁCH LY (cắt bạn bè) → SPM library drift → "mù" lâu hơn
    → ⚠️ Isolate partner khỏi bạn bè = CẮT feedback loop =
      TẠI SAO toxic partners thường isolate

  ③ BODY-BASE EXTENSION DEPTH:
    → L2 compiled CỰC SÂU → body RESIST "tỉnh" (vì tỉnh = mất body-base ext)
    → L2 compiled NHẸ → "tỉnh" dễ hơn (ít cost)
    → = Tại sao relationship SÂU khó bỏ HƠN relationship NÔNG
      dù CẢ HAI có red flags tương đương
```

---

## §6 — "CÀNG CẤM CÀNG YÊU" — ROMEO & JULIET EFFECT

```
🟢 "Romeo and Juliet Effect" (Driscoll et al. 1972):
  → Parental interference tương quan với increased romantic love
  → 🟢 Reactance theory (Brehm 1966): bị cấm → muốn HƠN
  → 🟢 Misattribution of arousal (Dutton & Aron 1974):
    body KHÔNG phân biệt "hồi hộp vì sợ" vs "hồi hộp vì yêu"
  → ⚠️ Effect KHÔNG robust ở mọi trường hợp (Sinclair et al. 2015)
```

### §6.1 — 4 Amplifiers qua lens v7.8

```
🟡 4 AMPLIFIERS — TẠI SAO "CẤM = YÊU MẠNH HƠN":

  ① PROTECT FIRE (Protect.md):
     → Ai cấm relationship = THREAT tới bond
     → Protect formula: f(replaceability × attachment)
     → Partner bị cấm = replaceability PERCEIVED cực thấp
       (bị cấm → "khó có lại" → replaceability ↓↓)
     → Vasopressin TĂNG → "phải BẢO VỆ bằng mọi giá"
       (Protect.md §4.1)
     → = Chưa cấm: "tôi thích" → Bị cấm: "tôi thích + PHẢI GIỮ"

  ② CORTISOL Role ③ Threat-sustained:
     → Bị cấm = threat chưa hết → cortisol sustained
     → CỘNG VỚI salience (dopamine) limerence đang có sẵn
     → Body NHẦM: "hồi hộp vì bị cấm" = "yêu MẠNH hơn"
       (Misattribution of arousal — Dutton & Aron 1974 🟢)
     → = Tim đập hơn, intense hơn → feel = "yêu HƠN"

  ③ "US VS THEM" Connection acceleration:
     → 2 người CHỐNG LẠI thế giới cùng nhau
     → Connection §14: shared adversity × HIGH EMOTION =
       chunks compile CỰC NHANH
     → Oxytocin từ "chúng ta vs mọi người" = bonding TURBO
     → = "Trốn cùng nhau" = shared experience cực mạnh
       → L2 body-base extension compile NHANH HƠN bình thường

  ④ REACTANCE ("trái cấm"):
     → Bị cấm → MUỐN HƠN (mọi thứ, không chỉ tình yêu)
     → = Protect + Novelty-drive CÙNG fire → motivation CỰC MẠNH


  TỔNG HỢP — limerence bị cấm vs bình thường:

    Bình thường:
      Dopamine ↑ + NE ↑ + Serotonin ↓ + Oxytocin ↑ → PFC ↓
      L1 momentary reward + L2 đang compile

    Bị cấm — THÊM:
      + Protect ↑↑ (vasopressin, loss aversion amplified)
      + Cortisol Role ③ Threat-sustained ↑↑
      + Us-vs-them bonding turbo ↑↑
      + Reactance motivation ↑↑
      = Intensity ×2-3 lần + L2 compile NHANH HƠN + PFC GIẢM HƠN
      = "MÙ" hơn, "NGHIỆN" hơn, "SAY" hơn bình thường
```

### §6.2 — Sau khi amplifiers hết

```
🟡 KHI GIA ĐÌNH CHẤP NHẬN / HẾT CẤM:

  Amplifiers TẮT:
    → Protect: hết threat → vasopressin GIẢM
    → Cortisol Role ③: hết → nhưng Role ④ Inertia CÓ THỂ kéo dài
    → Us-vs-them: hết kẻ thù chung → bonding turbo TẮT
    → Reactance: không còn cấm → "trái cấm" hết hấp dẫn

  CÒN LẠI: chỉ limerence bình thường (cũng sẽ hết trong 1-3 năm)
  VÀ: compatibility THẬT — chưa bao giờ được test đúng cách
    (vì PFC bị DOUBLE suppress suốt quá trình)


  ⭐ INSIGHT CỐT LÕI:

    Cái TĂNG khi bị cấm: intensity CẢM XÚC (hormone amplified)
    Cái KHÔNG TĂNG: compatibility THẬT (SPM library accuracy)
    Cái GIẢM: khả năng ĐÁNH GIÁ (PFC double suppress)

    → "Yêu MẠNH hơn" ≠ "Yêu ĐÚNG hơn"
    → Intensity ≠ Quality
    → Qua lens valence: amplifiers tăng VALENCE CHAIN LENGTH
      nhưng KHÔNG tăng compatibility (SPM calibration accuracy)
    → = CẤM → HIGH RISK hơn bình thường
```

---

## §7 — "CHỌN NHẦM" — TRAUMA CHUNKS × PARTNER SELECTION

```
🟡 "TẠI SAO HAY YÊU NHẦM NGƯỜI?" — FRAMEWORK GIẢI THÍCH:

  3 nguồn chunk ẢNH HƯỞNG partner selection (trước PFC kịp đánh giá):
    ① Individual compiled: trải nghiệm CÁ NHÂN (§7.1-§7.2)
    ② Childhood SPM bias: bố mẹ strict → SPM threat-biased (§7.3)
    ③ Collective installed: xã hội → schema "partner lý tưởng" (§7.4 — v2.2)
  → Body fire TRƯỚC PFC → limerence GIẢM PFC → TRIPLE BLIND có thể
```

### §7.1 — Vô thức chọn TRƯỚC PFC

```
🟡 CHUNK PROCESSING (C+D ZONES) EVALUATE TRƯỚC PFC:

  Gặp người mới → compiled chunks fire TRƯỚC PFC kịp đánh giá:
    → Chunks "hấp dẫn" = compiled từ experience + genetics → "thích"
    → Chunks "an toàn" = compiled từ childhood attachment → "quen"
    → Chunks "kích thích" = compiled từ past relationships → "hào hứng"

  PFC nhận signal TỪ body → bắt đầu attend → nhưng CHƯA quyết.
  Body lead, PFC follow — ở bước đầu.
  = "Thích ngay" = chunks fire ngay, KHÔNG phải PFC chọn.
```

### §7.2 — Trauma chunks làm lệch

```
🟡 TRAUMA CHUNKS TẠO "QUEN" GIẢ DẠNG "THÍCH":

  Bố hay la mắng → chunk [la mắng + tình thương] compiled CÙNG NHAU.
  Gặp người hay la mắng → body feel "QUEN" → NHẦM thành "THÍCH."
  = "Trauma feel" giả dạng "love feel" — body KHÔNG PHÂN BIỆT ĐƯỢC.

  CƠ CHẾ QUA CHUNK DYNAMICS (BFM):
    → Childhood: caregiver la mắng + sau đó ôm = emotional peak
    → 2 chunks compile CÙNG NHAU (Hebbian: neurons fire together wire together)
    → Pattern: [conflict → intensity → reconciliation] = compiled baseline
    → Adult: gặp partner có pattern giống → chunks FIRE → body: "QUEN"
    → "Quen" ở body level = Chunk-Match (pattern nhận diện thành công)
    → Body KHÔNG check: "quen LÀ TỐT hay quen LÀ HẠI?"
    → Đó là VIỆC CỦA PFC → nhưng limerence GIẢM PFC → NHẦM kéo dài

  VÔ THỨC KHÔNG TỰ PHÁT HIỆN "NHẦM":
    → C+D zones CHỈ đo: "pattern này có MATCH compiled hay không?"
    → C+D zones KHÔNG check: "match này CÓ TỐT cho tôi hay không?"
    → = Compiled chunks ĐÚNG ở mức pattern-match (body THẬT SỰ feel quen)
    → = Compiled chunks SAI ở mức domain (quen ≠ hợp, comfortable ≠ healthy)
    → = PFC là HỆ THỐNG DUY NHẤT check domain accuracy
    → = Nhưng limerence TẮT PFC → không còn ai check → "nhầm" kéo dài


  LIMERENCE LÀM MẠNH THÊM:
    → Đã chọn nhầm (vô thức) → limerence FLOOD thêm
    → = Nhầm + mù = DOUBLE blind
    → Chỉ thấy khi tỉnh (phase 3) → có thể đã quá sâu
      (L2 body-base extension đã compile → khó bỏ ở body level)
```

### §7.3 — SPM childhood bias: RỘNG hơn trauma

```
🟡 KHÔNG CHỈ TRAUMA — BỐ MẸ STRICT CŨNG TẠO SPM BIAS:
  (Chi tiết: OCD-Analysis.md v2.1 §4.5b)

  §7.2 nói về trauma NẶNG (la mắng + bạo lực).
  NHƯNG case PHỔ BIẾN hơn: bố mẹ STRICT (nghiêm khắc, không nhất thiết abusive).


  ① SPM LIBRARY BUILD TỪ CAREGIVER (Connection §3.2, §7):

    Bé học SPM TRƯỚC TIÊN trên bố mẹ.
    Bố mẹ strict → bé đối mặt threat lặp lại từ close agent.
    Body PHẢI respond → nhưng CÓ 2 HƯỚNG KHÁC NHAU:

    → ≠ Trauma (§7.2): trauma = bạo lực → chunks = "close agent = ĐAU"
    → SPM bias = strict → chunks = "close agent = PHẢI XỬ LÝ"
      nhưng "xử lý" BẰNG CÁCH NÀO → phụ thuộc §7.3b (fork mechanism)


  ⭐ §7.3b — FORK MECHANISM: TẠI SAO CÙNG "STRICT" MÀ 2 HƯỚNG KHÁC NHAU

    CƠ CHẾ GỐC — vmPFC/DRN Controllability Learning
    (Autonomy-Hardware.md §2, 🟢 Maier & Seligman 2016):

      DRN (thân não) = DEFAULT PASSIVE (bất lực = mặc định)
      vmPFC LEARN "controllable" → inhibit DRN → active coping
      vmPFC learn PER DOMAIN (Autonomy-Hardware §2.2)

    PATH A — MONITOR (→ anxious attachment):
      Con thử predict mood bố mẹ → điều chỉnh hành vi → bố mẹ BỚT mắng
      → vmPFC detect: "hành động CỦA MÌNH → kết quả THAY ĐỔI"
      → vmPFC: "controllable!" → inhibit DRN → active coping
      → SPM F2 invest MẠNH HƠN NỮA → "phải đoán cho đúng"
      → SPM library build DEEP nhưng ở THREAT DIRECTION
        (Cortisol Role ① Compile Direction: AVOIDANCE)
      → Chunks = "close agent → PHẢI CANH CHỪNG"

    PATH B — WITHDRAW (→ avoidant attachment):
      Con thử predict mood bố mẹ → điều chỉnh hành vi → bố mẹ VẪN mắng
      → vmPFC KHÔNG detect controllability signal
      → DRN default WIN → passive coping → WITHDRAW
      → SPM F2 GIẢM invest → "đoán cũng vô ích" → disengage
      → SPM library về bố mẹ NGƯNG phát triển
      → Chunks = "close agent → KHÔNG ĐÁNG INVEST"
      ⚠️ SPM F1 VẪN fire (body vẫn simulate bố mẹ giận)
        → body VẪN chịu dissonance — chỉ là KHÔNG CỐ QUẢN LÝ nữa

    PATH C — OSCILLATE (→ disorganized attachment, Type D):
      Bố mẹ SWITCH: lúc consistent (monitor works) ↔ lúc arbitrary (monitor fails)
      → vmPFC KHÔNG ổn định → dao động giữa Path A và Path B
      → Con KHÔNG có stable coping strategy → chronic uncertainty ở chính cơ chế coping
      → = Damaging nhất: uncertainty × 2 (về bố mẹ + về CÁCH ứng phó)


  ⭐ §7.3c — 7 BIẾN SỐ QUYẾT ĐỊNH PATH NÀO:

    ┌───────────────────────┬─────────────────────────────────────────┐
    │ Biến số               │ Path A (monitor) vs Path B (withdraw)   │
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ① Parent consistency  │ Strict + consistent (luật rõ) → A       │
    │    (DOMAIN — quan     │ Strict + inconsistent (tâm trạng) → B   │
    │    trọng NHẤT)        │ Strict + oscillate → C (disorganized)   │
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ② PFC capacity        │ PFC cao → detect pattern tốt → A       │
    │    (hardware)         │ PFC thấp → detect kém → B              │
    │    ⚠️ cần KẾT HỢP ⑦  │ PFC cao + ⑦ thấp = VẪN KHÓ (xem dưới)│
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ③ Cortisol sensitivity│ Thấp → chịu stress lâu → A             │
    │    (hardware)         │ Cao → overwhelm nhanh → B              │
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ④ Connection ❶ drive  │ ❶ cao → withdrawal = ĐAU → push A     │
    │    (hardware)         │ ❶ thấp → withdrawal chịu được → B     │
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ⑤ Obligation compiled │ Mạnh ("phải ngoan") → bound engage → A │
    │                       │ Mỏng → ít ràng buộc → B dễ hơn        │
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ⑥ Other agents        │ Bố mẹ = nguồn DUY NHẤT → PHẢI → A    │
    │    available          │ Có ông bà/cô giáo → ❶ met khác → B    │
    ├───────────────────────┼─────────────────────────────────────────┤
    │ ⑦ Pattern-Resonance   │ Cao (hợp tính) → SPM rewarding → A    │
    │    Baseline           │ Thấp (khác tính) → SPM exhausting → B  │
    │    (RELATIONAL —      │ ⚠️ ẢNH HƯỞNG ① (xem dưới)             │
    │    property CỦA CẶP,  │ ⚠️ RELATIONAL: không phải property     │
    │    không phải cá nhân)│   của riêng con hay riêng bố mẹ       │
    └───────────────────────┴─────────────────────────────────────────┘


    ⭐ BIẾN ⑦ — PATTERN-RESONANCE BASELINE (MỚI):
    (Chi tiết: Pattern-Resonance.md §7.8)

      "Hợp tính" = Pattern-Resonance Baseline = mức độ Pattern-Resonance
      emerge TỰ NHIÊN giữa parent và child, TRƯỚC KHI effort nào can thiệp.

      3 THÀNH PHẦN:
        (a) Hardware parameter overlap: novelty, cortisol, ❶, processing tempo
        (b) Expression modality match: verbal ↔ verbal, somatic ↔ somatic
        (c) Domain chunk overlap: shared interests, shared rhythms

      TẠI SAO ⑦ QUAN TRỌNG CHO PATH A/B:

        ⑦ CAO (hợp tính parent):
          → SPM self-template MATCH parent by default
          → Predict parent → KẾT QUẢ ĐÚNG → reward signal
          → vmPFC: "controllable!" → active coping → Path A DỄ
          → THÊM: parent cũng SPM con DỄ → respond contingently
          → = POSITIVE CYCLE: hợp → hiểu → hợp hơn

        ⑦ THẤP (khác tính parent):
          → SPM self-template FAIL on parent
          → Predict parent → KẾT QUẢ SAI → error signal → mệt
          → vmPFC: unclear controllability → Path B DỄ
          → THÊM: parent cũng SPM con KHÓ → respond non-contingently
          → = NEGATIVE CYCLE: khác → không hiểu → khác hơn


    ⭐ ⑦ × ② INTERACTION (tại sao PFC alone không đủ):

      PFC = sức xử lý (hardware processing power)
      ⑦ = target DỄ process hay không (self-template accuracy)
      2 biến ĐỘC LẬP — cả 2 đều cần:

        PFC cao + ⑦ cao = BEST case: detect tốt + template match → Path A mạnh
        PFC cao + ⑦ thấp = PFC phải COMPENSATE bằng effortful adjustment
          → Vẫn có thể detect → nhưng EXHAUSTING → risk shift B over time
        PFC thấp + ⑦ cao = Template match DÙ PFC yếu → vẫn predict ĐƯỢC
          → Path A khả thi dù hardware không mạnh
        PFC thấp + ⑦ thấp = WORST case → Path B gần như chắc chắn


    ⭐ ⑦ ẢNH HƯỞNG ① (KHÔNG hoàn toàn độc lập):

      ⑦ thấp → parent frustrated (họ CŨNG không match con tự nhiên)
        → Parent frustration → LESS consistent → ① XẤU ĐI
        → = ⑦ thấp GÂY ① thấp — 2 biến COMPOUND

      ⑦ cao → parent dễ chịu (họ hiểu con tự nhiên)
        → Parent calm → MORE consistent → ① TỐT HƠN
        → = ⑦ cao HỖ TRỢ ① cao — 2 biến REINFORCE

      → Connection §7.1 (L2 strong + F1 weak) = CƠ CHẾ CỦA ĐIỀU NÀY:
        Parent yêu con (L2) nhưng KHÔNG simulate con đúng (F1 fail VÌ ⑦ thấp)


    ⭐ BIẾN THỂ: "FUNCTIONAL AVOIDANT" (khi ⑤ + ⑦ thấp):
    (Chi tiết: Pattern-Resonance.md §7.9)

      Khi obligation mạnh (⑤) + Pattern-Resonance Baseline thấp (⑦):
        → Con BUỘC engage (⑤) DÙ SPM fail (⑦)
        → Con SUPPRESS natural patterns + AMPLIFY/FABRICATE để "hợp"
        → BÊN NGOÀI: ngoan, hòa nhã, fulfill obligations
        → BÊN TRONG: withdraw + perform → no genuine engagement
        → = KHÁC Path A (genuinely invest SPM) VÀ KHÁC Path B (openly withdraw)
        → = Path NGẦM: behavioral presence, experiential absence
        → Chỉ PHÁT HIỆN khi obligation lifts (con trưởng thành, ra riêng)
          → "Tôi chưa bao giờ thực sự connect với bố mẹ"

      COST TÍCH LŨY:
        → Autonomy: "my natural pattern doesn't matter here" (Autonomy-Hardware §5)
        → Cortisol: forced interaction → holding → baseline shift
        → SPM library: build trên PERFORMED patterns → useless cho genuine
        → = Tại sao một số người "ngoan" childhood → adult DISTANCE với bố mẹ


    ⚠️ DOMAIN-SPECIFIC (vmPFC §2.2):
      Con có thể đi path KHÁC NHAU với BỐ vs MẸ:
      Monitor mẹ (⑦ cao hơn + predictable hơn) + Withdraw bố (⑦ thấp + unpredictable)
      = Per-agent strategy, KHÔNG phải global personality trait
      = ⑦ CÓ THỂ KHÁC NHAU với từng parent (vì relational property)

    ⚠️ DYNAMIC — PATH CÓ THỂ SHIFT:
      → A→B: con monitor → bố mẹ ngày càng erratic → monitoring fail → shift withdraw
      → B→A: con withdraw → bố mẹ escalate punishment → threat quá cao → buộc quay lại
      → ⑦ CŨNG SHIFT: con lớn → chunks thay đổi → có thể hợp hơn HOẶC khác hơn
        (puberty = hardware parameter shift → ⑦ thay đổi)
      → = Feedback loop giữa con và bố mẹ — KHÔNG cố định


  ② ADULT → MEET PARTNER → SPM FIRE CÙNG LIBRARY:

    PATH A (monitor) khi gặp partner:
      → SPM retrieve: "close agent → monitor mood liên tục"
      → "Partner yên lặng → giận? chán? sắp bỏ?"
        (thay vì neutral: "đang nghĩ việc khác")
      → = HYPER-MONITORING — không phải vì partner xấu
        mà vì SPM library compiled TỪ MÔI TRƯỜNG PHẢI monitor

    PATH B (withdraw) khi gặp partner:
      → SPM retrieve: "close agent → KHÔNG ĐÁNG invest"
      → Partner muốn gần → body: "nguy hiểm, sẽ bị tổn thương"
      → = EMOTIONAL DISTANCE — không phải vì "không yêu"
        mà vì SPM library compiled: deep engagement = UNCONTROLLABLE = ĐAU

    PATH C (oscillate) khi gặp partner:
      → Lúc muốn gần (❶ drive) ↔ lúc muốn xa (protect fire)
      → Partner confused: "sao lúc thân lúc lạnh?"
      → = "Hot-cold" pattern → partner uncertainty TĂNG → feedback loop


  ③ COMPOUND UNCERTAINTY (chủ yếu PATH A):
    → ① SPM uncertainty: "họ thật sự cảm thấy gì về tôi?"
      (SPM predict → kết quả KHÔNG RÕ → uncertainty)
    → ② Obligation uncertainty: "tôi phải trả GÌ để giữ?"
      (Obligation.md: obligation CHƯA COMPILE → Chunk-Gap)
    → 2 nguồn COMPOUND → serotonin ↓ MẠNH HƠN
    → = Limerence INTENSE hơn + KÉO DÀI hơn

    PATH B compound KHÁC:
    → Uncertainty THẤP hơn (vì không invest deep → ít data → ít predict)
    → NHƯNG ❶ drive VẪN CÓ (hardware) → Chunk-Gap: "muốn gần mà không dám"
    → = Limerence NGẮN hơn nhưng kèm approach-avoid conflict


  ④ MAP VÀO ATTACHMENT THEORY (🟢 Bowlby 1969):

    ┌───────────────────┬─────────────────────────────────────────────┐
    │ Attachment style   │ v7.8 mechanism                             │
    ├───────────────────┼─────────────────────────────────────────────┤
    │ Secure            │ vmPFC: "close agent = controllable"         │
    │                   │ SPM library: balanced, accurate              │
    │                   │ Adult: predict partner WELL → uncertainty ↓ │
    ├───────────────────┼─────────────────────────────────────────────┤
    │ Anxious (Path A)  │ vmPFC: "controllable IF I monitor HARD"     │
    │                   │ SPM library: deep BUT threat-biased         │
    │                   │ Adult: hyper-monitor → uncertainty chronic   │
    │                   │ → serotonin ↓ amplified → limerence OCD-like│
    ├───────────────────┼─────────────────────────────────────────────┤
    │ Avoidant (Path B) │ vmPFC: "close agent = UNCONTROLLABLE"       │
    │                   │ SPM library: thin (stopped investing)        │
    │                   │ Adult: WITHDRAW khi close → distance = safe │
    │                   │ → limerence ngắn + approach-avoid conflict  │
    ├───────────────────┼─────────────────────────────────────────────┤
    │ Disorganized (C)  │ vmPFC: UNSTABLE (lúc controllable lúc không)│
    │                   │ SPM library: deep BUT inconsistent           │
    │                   │ Adult: oscillate hot-cold → partner confused │
    │                   │ → most damaging pattern for cả 2 bên       │
    └───────────────────┴─────────────────────────────────────────────┘

    → Framework KHÔNG thay thế attachment theory → GIẢI THÍCH mechanism đằng sau
    → Labels = outcome descriptions. v7.8 = mechanism under the labels.
    → Quan trọng: attachment style KHÔNG CỐ ĐỊNH — vmPFC CÓ THỂ re-learn
      (Autonomy-Hardware §2.3: vmPFC recoverable, though slower than damage)

    ⚠️ "FUNCTIONAL AVOIDANT" (§7.3c) KHÔNG NẰM TRONG BẢNG TRÊN:
      → BỀ NGOÀI giống Secure hoặc Anxious (vẫn engage, vẫn fulfill)
      → BÊN TRONG giống Avoidant (đã withdraw — chỉ PERFORM)
      → = Attachment theory labels KHÔNG capture variant này
      → v7.8 mechanism: ⑤ obligation + ⑦ thấp → suppress + perform
      → Chi tiết: Pattern-Resonance.md §7.9


  ⚠️ KHÔNG CHỈ CHILDHOOD:
    → Partner genuinely unpredictable → SPM errors CAO vì PARTNER
    → = SAME mechanism, DIFFERENT source
    → Childhood bias + partner unpredictable = COMPOUND → worst case
    → Childhood secure + partner unpredictable = vẫn uncertainty nhưng NHẸ hơn
      (SPM library có baseline "close agent = AN TOÀN" → buffer)
```

### §7.4 — Collective-installed schemas × partner selection (v2.2)

```
🟡 TẦNG THỨ 3: XÃ HỘI INSTALL SCHEMA "PARTNER LÝ TƯỞNG"
  (Collective-Body.md v1.1 — Type C compile, Cấp 2 chains)

  §7.1-§7.3 = chunks compiled TỪ TRẢI NGHIỆM CÁ NHÂN.
  NHƯNG: nhiều chunks về "partner lý tưởng" = COLLECTIVE INSTALLED (Type C):

  ┌──────────────────────────┬────────────────────────────────────────┐
  │ Schema collective         │ Cơ chế install                        │
  ├──────────────────────────┼────────────────────────────────────────┤
  │ "Môn đăng hộ đối"        │ Gia đình + cộng đồng → lặp lại →     │
  │ (status match)            │ compile thành evaluation default      │
  ├──────────────────────────┼────────────────────────────────────────┤
  │ "Chồng cao hơn vợ"       │ Văn hóa + media → visual norm →      │
  │ (physical norms)          │ body-level "lạ" khi violate           │
  ├──────────────────────────┼────────────────────────────────────────┤
  │ "Phải cưới trước 30"     │ Social pressure → Obligation (Cấp 2   │
  │ (timeline pressure)       │ chain: tuổi → hết cơ hội → đau)      │
  ├──────────────────────────┼────────────────────────────────────────┤
  │ "Đàn ông phải kiếm hơn"  │ Status.md v2.0 Resource Access Map    │
  │ (economic norms)          │ → collective define "resource provider"│
  └──────────────────────────┴────────────────────────────────────────┘

  CƠ CHẾ (Collective-Body §2, §5):
    → Cá nhân COMPILE SHORT: [partner match norm → gia đình khen → ấm]
    → Collective HOLD LONG: [norm → acceptance → status → opportunity]
    → Individual chỉ cần TRUST collective cho phần dài
    → = Cá nhân KHÔNG ĐÁNH GIÁ norm — chỉ TRUST + follow

  TẠI SAO RELEVANT CHO PARTNER SELECTION:
    → Type C installed schemas fire TRƯỚC PFC (giống §7.1)
    → Gặp partner violate norm → body "kỳ kỳ" DÙ không biết tại sao
    → Gặp partner match norm → body "ổn" DÙ compatibility chưa rõ
    → = Collective schemas TẠO false positive ("match norm = hợp")
      VÀ false negative ("violate norm = không hợp")

  ⚠️ COLLECTIVE SCHEMAS KHÔNG SAI HAY ĐÚNG — là INSTALLED:
    → Một số norm correlate với compatibility thật (shared values)
    → Một số norm KHÔNG correlate (chiều cao, thu nhập, tuổi)
    → Body KHÔNG phân biệt → PFC cần evaluate → nhưng limerence GIẢM PFC
    → = Triple blind: trauma chunks (§7.2) + SPM bias (§7.3) + collective norm (§7.4)

  (Chi tiết: Collective-Body.md §2-§5, Compile-Taxonomy.md §3)
```

---

## §8 — TỐI ƯU TRƯỚC — COMPILED RED/GREEN FLAGS

```
🟡 PFC KHÔNG CHỌN YÊU AI — NHƯNG CÓ THỂ CHUẨN BỊ BỘ LỌC TỐT HƠN:
```

### §8.1 — Red flags: COMPILE vào body, không chỉ BIẾT ở PFC

```
🟡 NGUYÊN TẮC GỐC:

  "Biết red flags" ở PFC level = KHÔNG ĐỦ.
  Limerence giảm PFC → red flags ở PFC level MẤT.
  Cần: red flags COMPILED vào C+D zones → fire DÙ PFC giảm.

  CÁCH COMPILE (BFM §5 compile_rate formula):
    compile_rate ≈ f(repetition × saliency × peak_valence × multi_modal × contingency)

    → Repetition: nghe NHIỀU câu chuyện thật (bạn bè, sách, podcast)
    → Saliency: FEEL khi nghe (body phản ứng, không chỉ nghe suông)
    → Peak valence: emotional peaks khi nghe câu chuyện đau → compile MẠNH
    → Multi-modal: xem phim + nghe kể + đọc sách = nhiều kênh = compile sâu
    → Contingency: liên kết trực tiếp với hệ quả (biết người thật bị hại)

  CHUNKS CẦN COMPILE:
    → [Kiểm soát]: "phải hỏi ý tôi trước khi..." → body feel "CHẬT"
    → [Thiếu empathy]: không care cảm giác → body feel "LẠNH"
    → [Love bombing]: quá sớm, quá mạnh, quá "hoàn hảo" → body feel "LẠ"
    → [Pattern bạo lực]: la mắng → xin lỗi → lặp → body feel "SỢ nhưng quen"

  ⭐ TẠI SAO PHẢI COMPILE (không chỉ đọc list):
    → Limerence GIẢM PFC (§5) → red flags ở PFC MẤT
    → Red flags ĐÃ COMPILED → chạy ở C+D zones → KHÔNG CẦN PFC
    → = Hàng rào bảo vệ VẪN HOẠT ĐỘNG khi yêu
    → = "Chỉ đọc" red flags = KHÔNG ĐỦ → phải FEEL để compile
```

### §8.2 — Green flags: biết mình CẦN gì

```
🟡 GREEN FLAGS = BIẾT MELODY MÌNH → TÌM MELODY HỢP:

  Không phải "type" bề ngoài → mà PATTERN bên trong:
    → [Respect]: lắng nghe, care cảm giác → body feel "AN TOÀN"
    → [Consistency]: lời = hành động, qua thời gian → body feel "TIN ĐƯỢC"
    → [Growth]: sẵn sàng thay đổi, nhận sai → body feel "CÓ THỂ BUILD"
    → [Compatible rhythm]: tempo sống TƯƠNG TỰ → body feel "KHÔNG GƯỢNG"

  Green flags KHÁC per-person (tùy hardware + compiled chunks):
    → Novelty drive cao → cần partner CÓ THỂ explore cùng
    → Connection drive cao → cần partner PRESENT + attentive
    → = "Biết mình cần gì" = biết Imagine-Final MÌNH → tìm Imagine-Final HỢP
```

### §8.3 — Observer strategy: dùng SPM NGOÀI

```
🟡 LIMERENCE TẮT PFC CỦA BẠN → KHÔNG TẮT PFC BẠN BÈ:

  Bạn bè, gia đình = external SPM KHÔNG bị hijack:
    → "Mọi người thấy partner này thế nào?" = survey SPM không bị flood
    → Nếu NHIỀU observer nói "kỳ kỳ" → signal QUAN TRỌNG
      (SPM consensus — nhiều SPMs independent cùng signal = likely accurate)

  ⚠️ Observer cũng có BIAS:
    → Bố mẹ: schema "con phải chọn kiểu NÀY" → BIAS CỦA HỌ
    → Bạn: bias jealousy hoặc "thích hộ"
    → = Nghe NHIỀU observer, KHÔNG chỉ 1 → pattern rõ hơn

  ⚠️ ISOLATE = CẮT FEEDBACK LOOP:
    → Toxic partner isolate khỏi bạn bè = CẮT external SPM
    → = SPM library về partner chỉ có SELF input → open-loop → drift
    → = Pattern-Resonance.md §6.4: feedback loop broken → library distorted
    → = TẠI SAO isolation là red flag #1
```

### §8.4 — Imagine-Final = bộ lọc tự nhiên

```
🟡 IMAGINE-FINAL RÕ = BỘ LỌC THÊM CHO PARTNER:

  Người CÓ Imagine-Final rõ (biết mình muốn đi đâu):
    → Imagine-Final compiled SÂU vào body (Imagine-Final.md §1)
    → Gặp partner KHÔNG MATCH direction → body feel "lệch"
      DÙ ĐANG limerence
    → = Imagine-Final ở body-base level → limerence giảm PFC
      → NHƯNG Imagine-Final fire ở C+D → VẪN detect mismatch

  Người KHÔNG CÓ Imagine-Final (chưa biết mình muốn gì):
    → Không có bộ lọc direction → partner NÀO cũng "có thể hợp"
    → = DỄ bị limerence kéo vào bất kỳ ai trigger VTA

  → = Tìm Imagine-Final TRƯỚC khi yêu = tối ưu mạnh nhất
```

---

## §9 — LIMERENCE = GIFT + WINDOW + FUEL

```
🟡 LIMERENCE = WINDOW QUÝ GIÁ — ĐỪNG CHỐNG, ĐỪNG LÃNG PHÍ:

  ⭐ ĐỪNG CHỐNG LIMERENCE:
    → Limerence = biology, KHÔNG tắt được
    → Cố tắt = Chunk-Gap (muốn tắt ≠ thực tế vẫn fire) → mệt vì mismatch
      cortisol Role ② Holding đồng hành (amplifier, không phải cause)
    → = "Đang được tặng món quà → đừng từ chối"

  ⭐ ĐỪNG LÃNG PHÍ LIMERENCE:
    → Window 18 tháng → 3 năm = thời gian CẢ 2 MOTIVATED nhất
    → Cả 2 đều MUỐN invest → dùng motivation đó build NỀN TẢNG THẬT
    → Nếu chỉ enjoy hormone mà không build → hết limerence = TAY TRẮNG
      (L2 body-base extension CHƯA compile → không còn structural reward)
```

### §9.1 — Dùng limerence window build gì

```
🟡 4 THỨ CẦN BUILD TRONG WINDOW:

  ① SHARED EXPERIENCE CHUNKS — nền tảng connection thật:

    Connection §15 ①: repeated positive Pattern-Resonance → chunks STRENGTHEN.
    Trải nghiệm CÙNG NHAU: du lịch, nấu ăn, project chung, khó khăn chung.
    Mỗi experience = chunks CHUNG compile vào CẢ 2 người.

    → Limerence cho MOTIVATION → dùng motivation đó tạo SHARED CHUNKS
    → Khi hormone hết → shared chunks VẪN CÒN → connection VẪN CÓ
    → = L2 body-base extension compile SONG SONG với limerence
    → = Chunks chung càng NHIỀU → L2 càng SÂU → relationship càng BỀN


  ② COMMUNICATION PATTERNS — compile cách resolve xung đột:

    Trong limerence: ít xung đột (PFC giảm → mọi thứ đều ok).
    NHƯNG: vẫn CÓ khác biệt nhỏ → dùng window này TẬP resolve.

    Pattern cần compile:
      "khác ý → nói ra → lắng nghe → tìm giữa → resolve"
    = 1 Melody-Arc nhỏ (Melody-Arc.md: dissonance → compile → upgrade)

    → Khi hormone hết + xung đột THẬT → pattern ĐÃ COMPILED → auto-run
    → = "Couple giỏi xung đột" ≠ "couple ít xung đột"
      (Gottman 🟢: bền nhất = biết CÁCH xung đột + repair)


  ③ BIẾT SPM LIBRARY NGƯỜI KIA — dùng salience build depth:

    Limerence = salience CỰC CAO → attention CỰC CAO → TÒ MÒ cực mạnh.
    Dùng tò mò đó: hỏi SÂU, nghe SÂU, hiểu hardware + values + fears.

    = Build SPM library về partner (Agent-Mechanism §7.2: Depth axis):
      → Thin → Moderate → Deep → Deepest
      → Limerence window = cơ hội build Depth NHANH NHẤT
    → Khi hormone hết → đã HIỂU partner → đánh giá CHÍNH XÁC hơn


  ④ ENJOY TRỌN VẸN — trải nghiệm multi-system sync:

    Đồng bộ multi-system mạnh nhất đời → ENJOY trọn vẹn.
    Body rewards THẬT: opioid (reward thật), oxytocin (bonding).
    = 1 trong những trải nghiệm CAO NHẤT con người có thể có.
    = Enjoy NÓ — chỉ đừng NHẦM nó là VĨNH VIỄN.


  → = Limerence = GIFT + WINDOW + FUEL
  → = Gift: trải nghiệm tuyệt vời → enjoy
  → = Window: thời gian cả 2 motivated → build foundation
  → = Fuel: energy để invest → dùng cho SHARED CHUNKS + SPM DEPTH
```

---

## §10 — TRANSITION: LIMERENCE → ATTACHMENT

### §10.1 — Attachment ≠ "hết yêu" — khác LOẠI

```
🟡 BIẾT TRƯỚC: limerence SẼ giảm. Chuẩn bị TRƯỚC, không shock SAU.

  LIMERENCE:
    → ❶ hardware FLOOD + ❷ SPM composite MAX + ❸ valence STRONG +
    → L1 momentary CỰC MẠNH + L2 ĐANG compile
    → Dopamine salience CỰC CAO → mọi thứ về partner đều "mới"
    → Serotonin ↓ → obsessive thinking → KHÔNG NGỪNG nghĩ
    → = CỰC MẠNH, NGẮN, KHÔNG BỀN

  ATTACHMENT:
    → ❶ hardware MAINTAIN + ❷ SPM library DEEP + ❸ valence STABLE
    → L1 momentary moderate + L2 structural COMPILED
    → Dopamine về baseline → partner KHÔNG CÒN "mới" mỗi giây
    → Serotonin phục hồi → NGỪNG ÁM ẢNH
    → = NHẸ HƠN, SÂU HƠN, BỀN HƠN

  = KHÁC LOẠI, không phải "giảm bớt"
```

### §10.2 — Nhận biết đang chuyển

```
🟡 NHẬN BIẾT TRANSITION — BÌNH THƯỜNG, KHÔNG PHẢI "HẾT YÊU":

  → Nghĩ về partner ÍT hơn (serotonin phục hồi)
  → Bắt đầu thấy khuyết điểm (PFC bật lại → CÓ DATA để evaluate)
  → Không còn "tim đập" khi gặp (NE giảm, VTA habituated)
  → Muốn KHÔNG GIAN riêng nhiều hơn
    (Autonomy-Hardware.md: efference copy reward → body CẦN solo action)
  → = Não ĐANG CHUYỂN MODE, không phải "hết yêu"

  Cortisol Role ④ Inertia có thể xảy ra:
    → Limerence intense → hết → cortisol CHƯA về baseline → "chênh vênh"
    → "Chênh vênh" ≠ "hết yêu" → = cortisol inertia (Cortisol §2.3)
    → Kéo dài days → weeks → TỰ GIẢI khi body recalibrate
```

### §10.3 — Connection §12: Shared Imagine-Final quyết định bond

```
🟡 BOND BỀN HAY KHÔNG = SHARED IMAGINE-FINAL Ở TẦNG NÀO:

  (Connection.md §12)

  ┌──────────────────┬──────────────────────┬────────────────────────┐
  │ Imagine-Final    │ Dominant pathways    │ Bond characteristics    │
  │ tầng             │                      │                         │
  ├──────────────────┼──────────────────────┼────────────────────────┤
  │ Safety           │ Presence + co-reg    │ Ngắn hạn, tắt khi safe │
  │ Comfort          │ Mirror + validation  │ Chu kỳ: thiếu→seek→met │
  │ Growth           │ Challenge + shared   │ Bền nhất: đạt mốc →    │
  │                  │ arcs + novelty       │ Imagine-Final NÂNG CẤP │
  └──────────────────┴──────────────────────┴────────────────────────┘

  → Bond BỀN NHẤT khi shared Imagine-Final ở tầng growth
  → = 2 người CÙNG GROW → mỗi mốc = Chunk-Gap fill → shared opioid
  → = Novelty từ growth CÁ NHÂN mang vào relationship → VTA fire lại
```

### §10.4 — 4 hướng sau transition

```
🟡 SAU "TỈNH DẬY" — NHIỀU HƯỚNG:

  HƯỚNG A — "Hay thật" (attachment bền):
    → PFC đánh giá lại → "partner VẪN HỢP dù hết hormone"
    → L2 body-base extension ĐÃ compile → structural reward CÒN
    → Shared chunks SÂU + SPM library calibrated → connection THẬT
    → = Transition MƯỢT vào attachment bền

  HƯỚNG B — "Không match" (break up):
    → PFC đánh giá → "partner KHÁC cái tôi tưởng"
    → SPM library giờ có calibration data MỚI → thấy mismatch
    → Limerence che mismatch → giờ LỘ RA
    → = "Tôi yêu HÌNH ẢNH hormone tạo ra, không phải NGƯỜI THẬT"

  HƯỚNG C — "Quen + chán" (dead relationship):
    → Không lệch nhiều → NHƯNG ❶ hardware channels dần bị đói
    → Cả 2 nhịn nhu cầu → tưởng smooth → thực ra channels UNMET
    → Connection §16 Type 2: "cô đơn giữa đám đông"
      = ❶ hardware met (presence) + ❷ SPM mismatch (Pattern-Resonance fail)
    → = "Ở cùng nhưng CÔ ĐƠN"

  HƯỚNG D — "Drop" (toxic / trauma):
    → PFC bật lại → thấy red flags mà limerence đã che
    → HOẶC: partner thay đổi behavior sau khi "đã giữ được"
    → L1 negative liên tục > L2 structural → compound pain
    → = Cần EXIT (§12)
```

---

## §11 — BONDING LÂU DÀI — DUY TRÌ CONNECTION THẬT

```
🟡 GIAI ĐOẠN DÀI NHẤT + KHÓ NHẤT — không có hormone hỗ trợ tự động.
   Attachment CẦN EFFORT — nhưng effort có mechanism rõ ràng.
```

### §11.1 — Hiểu THẬT vs Hiểu GIẢ — qua 4 axes SPM

```
🟡 PHÂN BIỆT QUAN TRỌNG NHẤT CHO BONDING:

  🟢 Gottman: couples BỀN NHẤT ≠ ít xung đột → = biết CÁCH xung đột + repair
  🟢 Dana Jack 1991: self-silencing → tích lũy resentment → relationship chết từ trong

  HIỂU THẬT = SPM library DEEP + CALIBRATED:
    → 4 axes (SPM v2.1 §7): Pattern-Type composite + Depth deep +
      Similarity high + Feedback real-time
    → NÓI RA nhu cầu THẬT (dù gây dissonance nhẹ)
    → NGHE nhu cầu partner (dù không thích)
    → = Micro-dissonance → resolve → chunk UPGRADE → VTA fire
    → = KHÔNG THỂ CHÁN vì: partner luôn thay đổi → SPM cần UPDATE

  "HIỂU" GIẢ = SPM library STALE:
    → Biết hành vi, thói quen, sở thích (predict SURFACE)
    → NHƯNG cả 2 KHÔNG nói nhu cầu THẬT (sợ phá bond)
    → = SPM library KHÔNG update → drift từ reality
    → = Smooth VÌ TRÁNH, không phải vì harmony THẬT
    → = VTA không fire (không có prediction delta) → "chán"
```

### §11.2 — Nhịn vs Nói — body tích lũy

```
🟡 NHỊN QUÁ MỨC → BODY PHẢN KHÁNG:

  (Body-Feedback-Mechanism.md §3.3 Chunk-Gap + §4 Compound)

  Mỗi lần nhịn (suppress nhu cầu) = Chunk-Gap PENDING trong network:
    → "Cần X nhưng chưa nói" = gap chưa resolve
    → Cortisol Role ② Holding ĐỒNG HÀNH: "pending, chưa xong" (amplifier)

  Nhịn CÙNG chuyện nhiều lần → Gap→Miss transition (§3.3):
    → PFC preview "nếu nói thì sẽ OK" lặp → compile thành expectation
    → Reality (vẫn không nói) < compiled baseline → Chunk-Miss
    → = Gap mơ hồ → Miss cụ thể, đau hơn

  NHIỀU nhu cầu nhịn = COMPOUND (§4):
    → Gap₁ + Gap₂ + ... + Gapₙ tồn tại ĐỒNG THỜI
    → Body-feedback = Σ (all active gaps/misses) — mỗi cái NHỎ, SUM lớn dần

  "Giọt nước tràn ly":
    → Gap cuối cùng (NHỎ) cộng vào Σ → VƯỢT threshold
    → + Possible Chunk-Shift: "partner KHÔNG care" (re-evaluate relationship)
    → = COMPOUND dynamics → body PHẢN KHÁNG (nổ, khóc, lạnh nhạt)
    → = KHÔNG phải vì chuyện NHỎ đó
      → mà vì TỔNG chunk-gaps/misses từ NHIỀU lần nhịn trước
    → (Cortisol = AMPLIFIER đồng hành, KHÔNG phải nguồn đau
       — Cortisol-Baseline.md §1: sustainer, not cause)

  NÊN NHỊN (tạm):
    → Khác biệt NHỎ, không ảnh hưởng body-base → để qua
    → Timing xấu (đang stress, mệt) → đợi lúc tốt hơn
    → = Nhịn = CHỌN THỜI ĐIỂM, không phải "giấu mãi"

  PHẢI NÓI:
    → Ảnh hưởng body-base CỦA MÌNH đáng kể → NÓI
    → Pattern LẶP LẠI → NÓI
    → Nhu cầu phát triển bị chặn → NÓI
    → = "Nhịn 1 lần = ok. Nhịn cùng chuyện 10 lần = PHẢI nói"
```

### §11.3 — Xung đột = calibrate (Gottman)

```
🟢 GOTTMAN "FOUR HORSEMEN" (4 dấu hiệu xung đột TỆ):
  → Criticism: "bạn LUÔN..." (tấn công identity)
  → Contempt: khinh thường, mỉa mai (TỆ NHẤT — #1 predictor ly hôn)
  → Defensiveness: "không phải lỗi tôi"
  → Stonewalling: im lặng, shut down

🟢 CÁCH XUNG ĐỘT TỐT (Gottman "repair attempts"):
  → Nói về HÀNH VI cụ thể, không tấn công IDENTITY
  → LẮNG NGHE trước khi phản bác
  → REPAIR: "tôi hiểu bạn thấy X" + "tôi cần Y" + "thử Z?"
  → KHÔNG CẦN đồng ý → CẦN cả 2 feel ĐƯỢC NGHE

🟡 QUA FRAMEWORK V7.8:
  → Xung đột = 2 SPM libraries có chunks KHÁC → predict khác → mismatch
  → Resolve = cả 2 SPM libraries UPDATE → calibrate → shared chunk MỚI
  → = Mỗi resolve = Connection §15 ①: chunks STRENGTHEN → bond MẠNH hơn
  → = Melody-Arc.md: dissonance → compile → melody upgrade
```

### §11.4 — Individual growth + Autonomy balance

```
🟡 RELATIONSHIP KHÔNG PHẢI TOÀN BỘ CUỘC SỐNG:

  🟢 Self-expansion theory (Aron & Aron 1986):
    Relationship thrives khi MỖI NGƯỜI VẪN GROW.
  🟢 Schnarch: passion lâu dài CẦN differentiation (giữ identity RIÊNG).

  Autonomy-Hardware.md:
    → Efference copy reward: self-action = better prediction = more opioid
    → Over-convergence → efference copy reward GIẢM → body penalizes
    → = "Sống hoàn toàn VÌ nhau" = mất efference copy variety
    → = Body signal: "CẦN LÀM GÌ ĐÓ RIÊNG"

  TỐI ƯU:
    → Mỗi người build growth ARC RIÊNG (career, hobby, learning)
    → CHIA SẺ cho nhau (SPM library UPDATE → novelty cho partner)
    → = Novelty từ BÊN NGOÀI → mang VÀO relationship → VTA fire
    → = "2 cây riêng, rễ CHUNG" → mỗi cây lớn → rễ CŨNG lớn
```

### §11.5 — Novelty injection + Deepen channels

```
🟢 Aron et al. 2000: hoạt động MỚI + THÁCH THỨC cùng nhau
   → relationship satisfaction TĂNG.

🟡 QUA FRAMEWORK:
  → VTA fire khi "KHÁC so với compiled baseline" (prediction delta)
  → Routine = habituate → VTA không fire → "chán"
  → Novelty cùng nhau = prediction delta MỚI → VTA fire → salience
  → = Giữ NOVELTY trong relationship = giữ VTA active

  DEEPEN CHANNELS — OXYTOCIN:
  → Limerence cho body reward TỰ ĐỘNG → attachment CẦN EFFORT:
    → Chạm: ôm, nắm tay, massage → oxytocin trực tiếp (CT fibers)
    → Eye contact: nhìn nhau lâu → oxytocin
    → Vulnerability: chia sẻ sâu → trust → oxytocin
    → Support: có mặt khi khó khăn → attachment STRENGTHEN
    → = Mỗi hành động NHỎ = 1 micro-dose oxytocin → tích lũy = bond BỀN

  ⭐ TYPE A/B × BONDING LÂU DÀI (v2.2):

    INSIGHT: 2 loại reward DECAY ở TỐC ĐỘ KHÁC NHAU:

    Type A rewards (evaluative): HABITUATE NHANH
      → Conversation → habituate → cần NOVELTY (Aron 2000 🟢)
      → Praise → habituate → cần GENUINE mới → cũ mất effect
      → = TẠI SAO "chán" dù partner tốt = Type A exhausted

    Type B rewards (direct state): HABITUATE CHẬM
      → Touch, ôm: CT afferents fire ĐỀU → ít giảm
      → Co-sleep, warmth: hardware → persistent
      → = "An toàn" physical khi ở cạnh = Type B VẪN CÒN
      → RSA §1.4: Type B = "evolutionary floor" — luôn available

    → OPTIMAL bonding = BOTH:
      Novelty (activities mới, growth) → giữ Type A fresh
      Physical affection (chạm, ôm, gần) → duy trì Type B baseline
      → Thiếu A: "chán" → thiếu salience
      → Thiếu B: "xa" → thiếu safety/warmth
      → Thiếu cả hai: relationship KHÔ (no reward either type)

    (Chi tiết: RSA §1.4 evolutionary floor, §8.1 A/B development)
```

### §11.6 — Persist vs Leave

```
🟡 KHÔNG CÓ CÔNG THỨC CHÍNH XÁC — nhưng có FRAMEWORK:

  CỐ GẮNG CÓ GIÁ TRỊ KHI:
    → SPM library depth CAO (hiểu nhau THẬT)
    → Xung đột về HÀNH VI, không phải VALUES GỐC
    → Cả 2 SẴN SÀNG repair (không contempt, không stonewalling)
    → Shared chunks SÂU (history, trust, L2 deep)
    → Shared Imagine-Final ở tầng Growth (Connection §12)

  NÊN DỪNG KHI:
    → SPM libraries MISMATCH ở values gốc (không thể calibrate)
    → 1 bên KHÔNG SẴN SÀNG repair (contempt mãn tính)
    → L1 negative liên tục > L2 structural
      (body-base extension ĐAU hơn FEED)
    → Body signal: "mệt và MUỐN THOÁT" (khác "mệt nhưng vẫn muốn cố")
    → = Body BIẾT trước PFC — lắng nghe body signal
```

---

## §12 — BREAK-UP: COMPOUND GRIEF QUA 8 PATHWAYS

```
🟡 BREAK-UP = NHIỀU CƠ CHẾ FIRE ĐỒNG THỜI → COMPOUND PAIN:
```

### §12.1 — Cơ chế: withdrawal + amputation + compound

```
🟢 Fisher 2010: rejected lovers fMRI = CÙNG PATTERN cocaine withdrawal.

🟡 QUA FRAMEWORK V7.8 — 3 tầng pain CHỒNG NHAU:

  TẦNG 1 — WITHDRAWAL (L1 momentary mất):
    → VTA VẪN fire salience ("chú ý partner!") → nhưng partner KHÔNG CÓ
    → Dopamine fire → KHÔNG ĐƯỢC reward → = withdrawal ĐÚNG NGHĨA
    → = "Muốn" mà "không có" = wanting without liking
      (Liking-Wanting.md: wanting = dopamine, liking = opioid)

  TẦNG 2 — AMPUTATION (L2 structural mất):
    → Partner = body-base extension → MẤT = "PHẦN CỦA TÔI BỊ CẮT"
    → Valence-Propagation.md §2: grief ≠ "tiếc" → grief = body-base amputation
    → Partner's channels KHÔNG CÒN được body treat as own → STRUCTURAL LOSS
    → = Tại sao grief ĐAU ở body level (physical pain pathways fire)
      🟢 Eisenberger 2003: social pain = physical pain regions

  TẦNG 3 — COMPOUND (Connection §15 ③):
    → 8 pathways (Connection.md §5) ĐỀU fire miss ĐỒNG THỜI:
      ① Mirror: SPM fire on memory → painful open-loop
      ② Co-regulation: cortisol TĂNG (mất social buffer)
      ③ Virtual chunks: mất access to partner's chunk library
      ④ Challenge: shared arcs ABANDONED → Chunk-Gap
      ⑤ Validation: "người biết TÔI nhất" → MẤT
      ⑥ Presence: physical presence ABSENT → ❶ hardware unmet
      ⑦ Shared experience: chunks fire → partner absent → Chunk-Miss
      ⑧ Schema provide: shared schemas ORPHANED

    → = COMPOUND: 8 Chunk-Miss CÙNG LÚC + 3 dynamics CHỒNG NHAU
    → Body-Feedback-Mechanism §4: compound = NHIỀU dynamics fire đồng thời
    → = "Đau chia tay" KHÔNG phải 1 nỗi đau → là 8+ nỗi đau COMPOUND
```

### §12.2 — Chunk dynamics chi tiết

```
🟡 3 CHUNK DYNAMICS (BFM §3) TRONG BREAK-UP:

  CHUNK-SHIFT (valence thay đổi):
    → Nếu bị phản bội: chunks về partner VẪN ĐÓ, valence FLIP
    → "Nhìn ảnh cũ mà đau" = content trigger → new valence → dissonance
    → 🟢 Extinction ≠ erasure (Bouton 2004): old valence suppressed, NOT deleted
    → = Memories VẪN CÓ → valence KHÁC → cùng content, khác feeling

  CHUNK-MISS (pattern absent):
    → Body compiled baseline CÓ partner → partner ABSENT → delta MẠNH
    → 🟢 Schultz 1997: actual < predicted → dopamine SUPPRESS → signal chủ động
    → 🟢 Crespi 1942 SNC: phản ứng MẠNH HƠN mức neutral (not just "thiếu")
    → Miss ở 8 channels → COMPOUND (Connection §15 ③)
    → Recovery: mỗi channel recalibrate KHÁC SPEED:
      ⑥ Presence: mất NGAY
      ① Mirror: giảm DẦN (SPM on memory yếu dần)
      ③ Virtual chunks: mất VĨNH VIỄN (trừ tìm source mới)
    → = Grief KHÔNG tuyến tính — có ngày dễ có ngày khó

  CHUNK-GAP (pattern chưa có):
    → "Tương lai không có partner" = Imagine-Final bị PHẢI rebuild
    → Gap giữa compiled Imagine-Final (CÓ partner) và reality (KHÔNG partner)
    → BFM §3.3: Gap → Miss transition:
      preview "tương lai CÓ partner" lặp → compile thành baseline →
      reality KHÔNG CÓ → = Chunk-Miss cụ thể
    → = "Kỳ vọng tương lai" compile thành "thiếu hiện tại"
```

### §12.3 — Protect × Love: loss aversion CỰC MẠNH

```
🟡 PROTECT.MD FORMULA APPLIED TO LOVE:

  Protect intensity = f(perceived replaceability × attachment chunks)

  Partner:
    → Attachment chunks: YEARS × multi-modal × emotional peaks = CỰC SÂU
    → Perceived replaceability: EXTREMELY LOW
      (unique person, unique history, unique compilation cost)
    → Protect §2.1: compilation cost = HIDDEN FACTOR
      "Gặp người khác possible. NHƯNG: compile lại attachment chunks?
       3-5 năm? More?" → body BIẾT chi phí → PFC thường KHÔNG

  → = Protect intensity MAXIMUM
  → = Tại sao body RESIST break-up dù PFC biết nên bỏ
  → = Body account for compilation cost, PFC thường doesn't
```

### §12.4 — Meaning crisis: anchor collapse

```
🟡 NẾU PARTNER = ANCHOR-SCHEMA → MẤT = MEANING DISRUPTED:

  Meaning.md v2.0: 5 types life-level anchor.
  Partner có thể trở thành:

    IDENTITY type: "Tôi là vợ/chồng của X" → mất X → "tôi là AI?"
    ROLE type: "Công việc tôi là chăm gia đình" → mất gia đình → role TRỐNG

  Anchor collapse (Meaning.md §2):
    → Anchor absent → chunks fragmentary → cacophony
    → = "Mất ý nghĩa" COMPOUND thêm trên grief
    → = Tại sao break-up CÓ THỂ trigger existential crisis

  KHÔNG phải mọi break-up = meaning crisis:
    → Partner KHÔNG phải anchor → grief nhưng meaning INTACT
    → Partner LÀ anchor DUY NHẤT → crisis
    → Partner là 1 trong NHIỀU anchors → grief nhưng có anchor khác hold
```

### §12.5 — Recovery: recalibrate, KHÔNG phải quên

```
🟡 RECOVERY = BODY RECALIBRATE TỪNG CHANNEL, KHÔNG PHẢI "QUÊN":

  Phase 1 — Withdrawal (tuần → vài tháng):
    → Body ĐANG withdrawal: salience + opioid + oxytocin giảm
    → Cortisol Role ③ Threat-sustained → ④ Inertia (event xong nhưng body chưa)
    → = "Không ăn, không ngủ, khóc liên tục" = hormone withdrawal + cortisol
    → = BÌNH THƯỜNG — body đang recalibrate, không phải "yếu"

  Phase 2 — Recalibrate (vài tháng → 1 năm):
    → Hormone DẦN về baseline
    → PFC bắt đầu process: "tại sao?" → schema mới compile
    → C+D zones: chunks về partner DẦN WEAKEN (use it or lose it)
    → Body-base tìm nguồn reward KHÁC (bạn bè, hoạt động)
    → Cortisol §2.4 Recovery asymmetry:
      damage NHANH (hours-days) → recovery CHẬM (weeks-years)
      → = "Just get over it" = ngộ nhận về evolutionary asymmetry

  Phase 3 — New baseline (tháng → năm):
    → Baseline MỚI hình thành — KHÔNG giống trước relationship
    → Chunks từ relationship VẪN CÓ (không xóa) → nhưng DẦN YẾU
    → SPM library từ relationship = KINH NGHIỆM → green/red flags updated
    → = Baseline sau drop KHÁC trước → có thể SÂU hơn (biết mình cần gì rõ hơn)

  TRIGGERS:
    → Nhạc, mùi, địa điểm, ngày kỷ niệm → chunks fire lại → đau lại
    → = Spreading activation (BFM §2.3 ⓔ): sensory trigger → cascade
    → DẦN YẾU theo thời gian → nhưng CÓ THỂ không mất hoàn toàn
    → = "10 năm sau nghe bài nhạc đó → vẫn nhói" = chunk compiled SÂU


  NO CONTACT — CHUNK DYNAMICS PERSPECTIVE:

    🟡 Framework: NO CONTACT trong phase 1-2 = OPTIMAL
    → Mỗi lần contact = chunks REACTIVATE → STRENGTHEN (thay vì weaken)
    → 🟢 Reconsolidation (Nader 2000): recalled memory malleable for window
      → nhưng nếu recall WITHOUT MODIFICATION → chunk REINFORCED
    → No contact = cho chunks NATURAL DECAY → recovery NHANH hơn
    → Sau phase 3: contact CÓ THỂ ok (chunks đã yếu đủ → không hijack)

  COMPOUND GRIEF WORST CASE — MẤT VỢ/CHỒNG (Connection §15):
    → 8 pathways ALL at MAXIMUM depth
    → + Status change + Protect violation
    → + Imagine-Final collapse + daily routine disrupted
    → + Meaning anchor collapse (nếu partner = anchor)
    → + Obligation dissolved (nếu có obligation compound)
    → = COMPOUND CHỒNG COMPOUND → grief CỰC NẶNG → cần NHIỀU NĂM
    → Recovery ≠ "quên" → "recalibrate TỪNG channel, ở TỐC ĐỘ KHÁC NHAU"
```

### §12.6 — Hụt hẫng formula (updated)

```
🟡 CÔNG THỨC V7.8:

  Grief intensity = f(L2 compile depth × L1 withdrawal × Protect × Meaning loss)

  L2 compile depth: KHÔNG kiểm soát (body đã compile → không undo)
  L1 withdrawal: tỉ lệ thuận intensity limerence
  Protect: f(replaceability × attachment) — partner = CỰC CAO
  Meaning loss: tùy partner có phải anchor hay không

  CÁI CÓ THỂ GIẢM:
    → Kỳ vọng vs Thực tế gap (BFM §3.3 ⑦):
      "Biết limerence sẽ giảm" → kỳ vọng match reality → hụt hẫng NHẸ hơn
    → SPM library calibration: biết partner THẬT (không phải hình ảnh hormone)
      → gap nhỏ → hụt hẫng NHẸ hơn
    → Multiple anchors: partner KHÔNG phải anchor DUY NHẤT
      → meaning loss GIẢM

  → = Biết cơ chế ≠ không đau
  → = Biết cơ chế = đau + HIỂU tại sao đau + BIẾT recovery là process
  → = "Biết sẽ tỉnh" + "chuẩn bị cho sau khi tỉnh" = tối ưu
```

---

## §13 — HONEST ASSESSMENT

### §13.1 — Established (🟢)

```
🟢 RESEARCH SUPPORT — peer-reviewed, replicated:

  → 3 giai đoạn tình yêu: lust, limerence, attachment (Fisher 2004)
  → fMRI: VTA + caudate active khi yêu (Fisher, Aron et al. 2005)
  → Serotonin giảm ~40% khi yêu ≈ OCD levels (Marazziti et al. 1999)
  → Limerence duration: 18 tháng → 3 năm (Tennov 1979, Fisher)
  → Love rejection = cocaine withdrawal pattern (Fisher 2010)
  → PFC + amygdala GIẢM khi xem ảnh partner (Bartels & Zeki 2000, 2004)
    ⚠️ Đo TRONG CONTEXT partner — fMRI không phân biệt "bị tắt" vs "không có việc"
  → Novel activities boost satisfaction (Aron et al. 2000)
  → Romeo & Juliet effect (Driscoll et al. 1972)
  → Misattribution of arousal (Dutton & Aron 1974)
  → Reactance theory (Brehm 1966)
  → Self-expansion theory (Aron & Aron 1986)
  → Four Horsemen predict divorce 90%+ (Gottman)
  → Pair bond = receptor distribution (Young & Wang 2004, prairie/montane vole)
  → Social pain = physical pain (Eisenberger 2003)
  → Social Baseline Theory (Coan 2015)
  → CT afferent fibers for social touch (Löken 2009)
  → Interpersonal synchrony (Feldman 2007)
  → Loss aversion ~2× (Kahneman & Tversky 1979)
  → Reconsolidation window (Nader 2000)
  → Extinction ≠ erasure (Bouton 2004)
  → Successive Negative Contrast (Crespi 1942, Flaherty 1996)
  → Reward prediction error (Schultz 1997)
  → Self-silencing → resentment (Dana Jack 1991)
  → Moral disengagement (Bandura 1999)
```

### §13.2 — Framework synthesis (🟡)

```
🟡 FRAMEWORK SYNTHESIS — consistent với data, chưa mainstream term:

  → "PFC tự giảm vì body smooth, KHÔNG bị ép tắt" (§2, §5):
     CHALLENGE mainstream. Giải thích selective blindness tốt hơn.
     Verification: threat suppress (global) vs limerence (selective) → KHÁC.
     Testable: tiêm oxytocin + red flags → amygdala fire?
     Parsimony: 1 cơ chế thay vì 2.

  → ⭐ "Serotonin ↓ = AMPLIFIER, not root cause" (§2.1):
     Parallel cortisol (already established). Root cause = genuine uncertainty
     (SPM incomplete + obligation unknown + possible childhood SPM bias).
     Evidence: love self-resolve (root fix → serotonin follows),
     SSRI relapse 80% (amplifier fix only), CBT relapse 20-30% (root fix).
     Cross-species support: OCD-Analysis §4.6.

  → ⭐ "SPM childhood bias → hyper-monitoring → compound uncertainty" (§7.3):
     Strict parents → SPM threat-biased → adult hyper-monitor partner.
     Maps to anxious attachment (Bowlby 🟢). Framework explains MECHANISM
     behind attachment label. Broader than trauma (§7.2) — includes
     strict/unpredictable parenting, not just abusive.

  → "Compiled chunks KÉO PFC BẬT LẠI" (§5.2):
     Nếu PFC tự giảm (không bị ép) → compiled red flags fire →
     body "kỳ" → PFC CÓ DATA → BẬT evaluate.

  → "3 Generative Primitives × Love" (§3):
     ❶ Hardware flood + ❷ SPM composite + ❸ Valence shift → Body-Base Extension.
     Consistent với neuroscience data. Chưa formalize thành model.

  → "2-Luồng Reward" (§4):
     L1 momentary + L2 structural. Giải thích "yêu sâu khác thích",
     "biết xấu mà không bỏ", "mẹ chăm con ốm không burnout".
     Consistent với Berridge wanting/liking distinction.

  → "Body-Base Extension" (§3.3):
     Partner → body-base extension. Grief = amputation.
     Consistent với social pain = physical pain (Eisenberger 2003).
     Extends existing data into mechanistic explanation.

  → "Compound grief 8 pathways" (§12.1):
     Break-up = 8 Chunk-Miss COMPOUND + Shift + Gap.
     Consistent với grief research. Framework adds mechanistic detail.

  → "Hụt hẫng = f(L2 depth × L1 withdrawal × Protect × Meaning)" (§12.6):
     Multi-factor formula. Consistent với data.
     Extends v1 formula: Intensity × (Kỳ vọng − Thực tế).

  → "Limerence = gift + window + fuel" (§9): reframe hữu ích, chưa formalize.
  → "Nhịn tích lũy chunk-gaps/misses → compound burst" (§11.2): consistent với Gottman demand-withdraw.
  → "Trauma chunks → partner selection" (§7): consistent với attachment theory + repetition compulsion.
  → "Isolate = cắt feedback loop" (§8.3): consistent với Pattern-Resonance calibration.
  → "No contact = cho chunks natural decay" (§12.5): consistent với reconsolidation theory.
  → "Romeo & Juliet = 4 amplifiers" (§6): consistent, extends reactance theory.
  → "5 Cortisol Roles trong love" (§2.1): framework taxonomy applied to love context.
  → "Autonomy balance" (§11.4): consistent với self-expansion theory.
```

### §13.3 — Hypothesis (🔴)

```
🔴 TESTABLE PREDICTIONS — chưa verified:

  → Compiled red flags vs "chỉ biết" red flags (§5.2):
     Prediction: người có TRẢI NGHIỆM red flags detect bad partner
     NHANH HƠN khi limerence vs người chỉ ĐỌC BIẾT.
     Test: longitudinal study, 2 groups, partner quality outcome.

  → PFC "tự giảm" vs "bị ép" — ultimate test (§2.2):
     Tiêm oxytocin + cho xem red flags → amygdala fire hay không?
     Fire = framework đúng. Không fire = mainstream đúng phần này.

  → L2 compile completion trước limerence hết → predict bond durability (§4.2):
     Measurable proxy: shared experience count × duration × novelty.
     Prediction: couples với L2 compiled = lower divorce rate.

  → ⭐ Serotonin amplifier test (§2.1):
     Đo serotonin transporter: anxious attachment vs secure attachment khi yêu.
     Prediction: anxious ↓ MẠNH HƠN (compound uncertainty → amplifier mạnh hơn).
  → ⭐ SPM childhood bias test (§7.3):
     Strict parenting history × limerence intensity × duration.
     Prediction: strict childhood → limerence INTENSE hơn + KÉO DÀI hơn
     (SPM threat-biased → hyper-monitor → serotonin ↓ amplified).

  → Limerence intensity có predict trước? (DRD4? receptor density?)
  → Attachment style (secure/anxious/avoidant) map vào 3 primitives thế nào?
  → "Shared chunks" có ĐO ĐƯỢC? (predict relationship durability?)
  → Optimal no-contact duration = f(limerence intensity × L2 depth)?
```

---

## §14 — CROSS-REFERENCES + STATUS

### §14.1 — Cross-references v7.8

```
MECHANISM FILES:
  → Body-Coupling.md v1.0 — coupling mechanism: 2D model, 3 Phase,
    extension/entanglement/neutral, system compilation, negative coupling
  → Connection.md v3.1 — 3 Generative Primitives, 8 pathways, §15 chunk dynamics
  → Agent-Mechanism.md — SPM hub, §12 body-need feeder, §12.2b 2-luồng
  → Self-Pattern-Match.md v2.1 — F1/F2, 5 Pattern-Types, 4 axes
  → Pattern-Resonance.md — mutual phenomenon, calibration loop, §7.8 PR Baseline
  → Valence-Propagation.md v1.4 — per-entity valence, §2 Body-Base Extension
  → Body-Feedback-Mechanism.md v1.2 — Chunk-Shift/Miss/Gap, §4 Compound
  → Reward-Signal-Architecture.md v1.0 — Type A/B, A Gates B, 5 Profiles (v2.2)
  → Chunk.md v2.0 — substrate, compilation, hierarchy
  → Compile-Taxonomy.md v1.1 — 3 Loại Compile A/B/C, 4 pathways (v2.2)
  → Cortisol-Baseline.md v2.0 — 5 Cortisol Roles §7.7, cascade, recovery asymmetry
  → PFC-Function.md v1.2 — 24 functions, reactive model
  → PFC-Configuration.md v1.0 — 6 modes, limerence = Mode ③ Reconfigured (v2.2)
  → Collective-Body.md v1.1 — Model 3 cấp, Type C compile, collective schemas (v2.2)

OBSERVATION PARAMETERS:
  → Protect.md v1.0 — f(replaceability × attachment), vasopressin, loss aversion
  → Meaning.md v2.0 — 5 anchor types, anchor collapse, Frankl reframe
  → Obligation.md v1.0 — relationship obligation, compiled prediction
  → Gratitude.md v1.1 — Type A gratitude, anti-habituation
  → Empathy.md v2.0 — SPM F1, burnout = f(L1/L2)
  → Status.md v2.0 — Resource Access Map, mutual status exchange
  → Autonomy-Hardware.md — efference copy reward
  → Autonomy.md — over-convergence penalty
  → Novelty.md — VTA prediction delta, habituation

CLARIFICATION FILES:
  → Dopamine-Reward-Rejection.md — dopamine ≠ reward
  → Cortisol-Amplifier-Not-Cause.md — cortisol ≠ "stress hormone"

RESEARCH FILES:
  → OCD-Analysis.md v2.1 — serotonin × obsessive patterns (link limerence)
  → Love-Unified.md v1.1 — ALL love types unified view qua L2

LENS FILES:
  → Imagine-Final.md — reference pattern, 14 clarity levels
  → Melody-Arc.md — dissonance → compile → upgrade
  → Feeling.md v2.1 — PFC observation interface, §6.5 Type A/B
```

### §14.2 — File status

```
⭐ STATUS:

  Version: v2.2 (refined from v2.1)
  Date: 2026-05-11
  Lines: ~2,200+
  Renamed: Love-Analysis.md → Love-Romantic.md (v2.2)
  Backup: backup/Love-Analysis-v75-era.md (969L, 2026-03-29)

  v2.0 CHANGES vs v1.0:
    ① REFRAMED: 3 Generative Primitives × Love (§3) — MỚI
    ② ADDED: 2-Luồng Reward (§4) — MỚI
    ③ ADDED: Body-Base Extension mechanism (§3.3) — MỚI
    ④ UPDATED: All terminology v7.5 → v7.8
    ⑤ UPDATED: 5 Cortisol Roles applied (§2.1)
    ⑥ STRENGTHENED: Break-up = compound grief 8 pathways (§12)
    ⑦ ADDED: Protect formula applied (§12.3)
    ⑧ ADDED: Meaning anchor collapse (§12.4)
    ⑨ UPDATED: All cross-references → v7.8 files
    ⑩ KEPT: Core research + PFC selective blindness hypothesis

  v2.1 ADDITIONS:
    ⑪ §2.1: Serotonin = AMPLIFIER, not root cause (parallel cortisol)
    ⑫ §7.3 NEW: SPM childhood bias (strict parents → threat-biased SPM
       → hyper-monitor → compound uncertainty → anxious attachment mechanism)
    ⑬ Updated Honest Assessment + Testable Predictions

  v2.2 ADDITIONS (2026-05-11):
    ⑭ RENAMED: Love-Analysis.md → Love-Romantic.md (phân biệt Love-Unified.md)
    ⑮ §2.1 NEW: Type A/B Reward dimension mapped vào love
       (RSA v1.0: touch = Type B, conversation = Type A, A Gates B × limerence)
    ⑯ §2.2 NEW: PFC-Configuration Mode ③ Reconfigured = limerence PFC state
    ⑰ §3.1: CT touch = Type B note trong Hardware channel table
    ⑱ §7.4 NEW: Collective-installed schemas × partner selection
       (Collective-Body v1.1: Type C compile, societal norms, triple blind)
    ⑲ §11.5 NEW: Type A/B × bonding lâu dài
       (A habituates nhanh, B ít habituate = maintenance reward)
    ⑳ §14: Cross-refs updated (VP v1.4, RSA v1.0, PFC-Configuration v1.0,
       Collective-Body v1.1, Love-Unified v1.1, Compile-Taxonomy v1.1)

  PENDING:
    → Cross-ref updates ở ~10+ files khác (Love-Analysis → Love-Romantic)
```

---

> *Love Romantic v2.2 — "Tình yêu = ❶ Hardware flood + ❷ SPM composite fire + ❸ Valence → Body-Base Extension.
> Limerence = GIFT + WINDOW + FUEL: enjoy + build L2 structural reward.
> L2 compile XONG = 'yêu sâu': partner's wellbeing = MY wellbeing (body-level, sustained).
> L2 CHƯA compile = 'thích': hết hormone → hết motivation.
> PFC TỰ GIẢM (Mode ③ Reconfigured) vì body smooth — compiled red flags VẪN bảo vệ.
> Reward trong love = Type A (evaluative, habituates) + Type B (direct, persists).
> Touch = Type B = safe baseline reward cho bonding lâu dài.
> Partner selection = triple blind: trauma chunks + SPM bias + collective norms.
> Serotonin ↓ = AMPLIFIER of uncertainty, NOT root cause — parallel cortisol.
> Break-up = compound: L1 withdrawal + L2 amputation + 8 pathway miss + Protect + Meaning.
> Recovery = recalibrate TỪNG channel ở TỐC ĐỘ KHÁC NHAU — không phải 'quên.'
> Biết cơ chế ≠ bớt yêu. Biết cơ chế = yêu + NAVIGATE được."*
