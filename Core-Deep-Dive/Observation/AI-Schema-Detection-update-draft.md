---
title: AI-Schema-Detection Update Draft — Collective-Level Capabilities
version: draft-v2
created: 2026-05-18
refined: 2026-05-18 (v2: +scale-dependent model từ Collective-Arc-Dynamics §4.5, GAP 1 enriched, refs updated)
status: OUTLINE — chưa implement. Chờ collective files mature rồi quyết định.
purpose: |
  Liệt kê GAPs trong AI-Schema-Detection.md v2.0 liên quan collective-level.
  ⑧ hiện tại chỉ cover "Collective Chain Break Detection" (3 loại).
  CHƯA cover: arc shift (scale-dependent), coordination node, schema pressure, gap distribution.
  File này = PLAN cho future update. KHÔNG phải implementation.
  DECISION PENDING: expand ⑧ trong AI-Schema-Detection HOẶC tạo file mới riêng.
  draft-v2: Collective-Arc-Dynamics §4.5 đã clarify "arc không gãy — chỉ shift/disruption tại local scale"
  → GAP 1 enriched with 4-level spectrum + scale diagnosis.
depends_on_maturity:
  - Collective-Body.md v2.0 — ✅ stable
  - Collective-Arc-Dynamics.md v1.1 — §4.5 refined (scale-dependent disruption)
  - Coordination-Node.md v1.0 — mới 2026-05-18, chưa drill
  - Gap-Distribution-Profile.md v1.0 — mới 2026-05-18, chưa drill
  - Collective-Schema-Pressure.md v1.0 — stable nhưng chưa integrate vào AI detection
---

# AI-Schema-Detection Update Draft — Collective-Level Capabilities

> **STATUS: OUTLINE. Chờ collective files được drill + refine.**
> **Khi đủ mature → quyết định: expand §3 ⑧ hay tạo file mới.**

---

## §A — HIỆN TRẠNG: ⑧ ĐÃ COVER GÌ

```
AI-Schema-Detection.md v2.0 §3 ⑧:
  ✅ Collective Chain Break Detection (3 loại):
     ① Cost tăng: "mệt hơn trước"
     ② Link gãy: [đại học → việc tốt] trust collapse
     ③ Compound: cost + link + trust đồng thời
  ✅ Individual vs Collective attribution
  ✅ 3 Cấp tagging (⑨): Cấp 1/2/3
  ✅ Basic context check: "ngành đang restructure?"

  GIỚI HẠN HIỆN TẠI (line 806):
    "AI collective chain detection = CẦN context data đủ (không có = không detect)"
```

---

## §B — 5 GAPS CẦN BỔ SUNG

### GAP 1: Collective Arc SHIFT + Scale Diagnosis (not just "break")

```
HIỆN TẠI: ⑧ detect chain BREAK (gãy, cost, compound)
THIẾU:
  ① Detect arc SHIFT (arc evolve, "true but unnecessary")
  ② Diagnose SCALE of disruption (personal → company → industry → national)
  ③ Phân biệt 3 nguồn "expired" khác nhau

SOURCE: Collective-Arc-Dynamics.md v1.1
  → §3: dependency ratio → shelf-life spectrum
  → §5: "True but unnecessary" = baseline vượt qua
  → §4.5 (NEW): 4 mức độ: Shift → Disruption → Node Death → Arc Extinction
  → §4.5: cá nhân experience "gãy" = 3 trường hợp khác nhau


  ⭐ AI CẦN 2 TẦNG DETECTION:

  TẦNG 1 — PHÂN BIỆT NGUỒN "EXPIRED":

    A. Pattern expired vì COLLECTIVE ARC SHIFT
       → "Bằng đại học từng = việc tốt" → arc shift → "bằng = default"
       → Intervention: recontextualize (hiểu arc shift, không self-blame)

    B. Pattern expired vì INDIVIDUAL growth mismatch
       → Cá nhân vượt qua compiled pattern → cần update
       → Intervention: individual exploration

    C. Pattern compile SHELF-LIFE hết hạn
       → Pattern về collective rule → collective rule ĐÃ ĐỔI
       → Intervention: update specific compiled chunk

    HIỆN TẠI AI NHẦM CẢ 3 = "cái gì đó sai" → fix SAI HƯỚNG


  TẦNG 2 — DIAGNOSE SCALE (Collective-Arc-Dynamics §4.5):

    Client: "mọi thứ sụp đổ" → AI check SCALE NÀO?

    ┌──────────────────────┬────────────────────┬──────────────────────┐
    │ Scale                │ Signal             │ Intervention         │
    ├──────────────────────┼────────────────────┼──────────────────────┤
    │ Personal             │ Snapshot outdated  │ Recompile personal   │
    │ (compiled map cũ)    │ "chỉ mình tôi"    │ patterns             │
    ├──────────────────────┼────────────────────┼──────────────────────┤
    │ Company/Node         │ Node failure       │ Navigate to new node │
    │ (leader/org fail)    │ "team cũng than"   │ (chuyển cty/nhóm)   │
    ├──────────────────────┼────────────────────┼──────────────────────┤
    │ Industry             │ Arc shifting       │ Reposition in new    │
    │ (ngành đang đổi)     │ "cả ngành khó"     │ direction            │
    ├──────────────────────┼────────────────────┼──────────────────────┤
    │ National/Global      │ Disruption         │ Adapt to new reality │
    │ (khủng hoảng/chiến   │ "mọi người đều     │ (survival + patience │
    │  tranh)              │  khó khăn"         │  + long-term)        │
    └──────────────────────┴────────────────────┴──────────────────────┘

    BIẾT scale = BIẾT intervention phù hợp
    NHẦM scale = therapy SAI HƯỚNG:
      → Nhầm industry shift → personal → client TỰ BLAME
      → Nhầm personal → industry → client KHÔNG TỰ IMPROVE
```

### GAP 2: Coordination Node Assessment

```
HIỆN TẠI: ⑧ KHÔNG mention coordination node quality
THIẾU: khi client phàn nàn về work → do NODE FAIL hay do CLIENT issue?

SOURCE: Coordination-Node.md v1.0
  → §6 Emergence ≠ Effectiveness
  → §8 Node Failure → 3 failure modes
  → §2 5 Capabilities of coordination node

AI CẦN PHÂN BIỆT:
  A. Leader FAIL (low effectiveness, high emergence)
     → Client frustration = VALID signal of node failure
     → Intervention: career decision (leave vs adapt), NOT self-fix

  B. Client AUTHORITY SCHEMA (individual issue)
     → Client pattern = resistance to ANY authority (personal history)
     → Intervention: explore authority schema, NOT blame leader

  C. MISMATCH (neither fail — wrong fit)
     → Leader OK for others, client's gap distribution doesn't match
     → Intervention: reposition, NOT fix either party

  SIGNALS CHO AI:
     → "Mọi người trong team cũng than" → likely node failure (A)
     → "Chỉ mình tôi có vấn đề" → likely individual (B) hoặc mismatch (C)
     → "Tôi luôn conflict với mọi sếp" → likely authority schema (B)
```

### GAP 3: Collective Schema Pressure Detection

```
HIỆN TẠI: ⑧ detect chain break nhưng KHÔNG detect schema PRESSURE
THIẾU: compound pressure từ nhiều schemas đồng thời

SOURCE: Collective-Schema-Pressure.md v1.0
  → Compound effect: 5 schemas simultaneous = overload
  → Asian/Confucian pattern density & rigidity
  → Body KHÔNG phân biệt source → all feel "real"

AI CẦN DETECT:
  → Client có NHIỀU "phải" đồng thời:
    "phải học giỏi" + "phải nghe lời" + "phải có nhà" + "phải lấy vợ/chồng"
    + "phải hiếu thảo"
  → Mỗi cái riêng = manageable
  → COMPOUND = overload → cortisol chronic → burnout/depression

  KHÁC VỚI individual schema:
    Individual schema = 1 pattern compiled từ personal experience
    Collective schema pressure = NHIỀU patterns installed bởi collective
    → Intervention KHÁC:
      Individual: explore + recompile 1 pattern
      Collective: RECOGNIZE compound load + prioritize + possibly reject some

  SIGNAL CHO AI:
    → Client list nhiều "obligations" → check compound load
    → Client culture = high schema density (Asian, Confucian, religious)
    → Client cortisol markers (sleep, anxiety, "mệt mà không biết tại sao")
```

### GAP 4: Gap Distribution × Collective Matching

```
HIỆN TẠI: KHÔNG có
THIẾU: client's gap distribution vs collective need alignment

SOURCE: Gap-Distribution-Profile.md v1.0
  → 4 trục: Domain Center × Origin Balance × Depth Profile × Stability
  → Collective gap landscape: society optimize cho certain gap distributions
  → Mismatch = crisis (individual in wrong collective context)

AI CÓ THỂ:
  → Observe client's gap pattern (from conversation over time):
    "Client luôn excited về abstract problems"
    "Client bored với routine work"
    → Gap distribution: abstract-dominant

  → Check context: "client ở environment nào?"
    → Body-domain dominant workplace + abstract-dominant person = MISMATCH
    → Intervention: reposition, NOT "fix" person to fit environment

  LƯU Ý:
    → Đây là OBSERVATION tool, không phải diagnostic
    → AI suggest "gap distribution có vẻ mismatch context" → client verify
    → KHÔNG prescribe "bạn nên làm X" → chỉ illuminate pattern
```

### GAP 5: Collective-Level Verification — Scale-Dependent

```
HIỆN TẠI: body-check = individual body verify individual finding
THIẾU: HOW verify collective-level findings?

VẤN ĐỀ:
  → AI detect "collective arc shift" → HOW verify?
  → Individual body-check KHÔNG ĐỦ cho collective-level claims
  → 1 person's body CAN'T verify "ngành này đang sụp"

  ⭐ INSIGHT TỪ Collective-Arc-Dynamics §4.5: VERIFICATION SCALES WITH DISRUPTION LEVEL:

  ┌──────────────────┬──────────────────────────┬─────────────────────┐
  │ Disruption level │ Verification method       │ Confidence          │
  ├──────────────────┼──────────────────────────┼─────────────────────┤
  │ Shift            │ Body-check + domain       │ Medium-High         │
  │ (gradual)        │ feedback over time        │ (verifiable qua     │
  │                  │ "pattern cũ works less?"  │ personal experience)│
  ├──────────────────┼──────────────────────────┼─────────────────────┤
  │ Disruption       │ Peer pattern matching +   │ Medium              │
  │ (tạm thời)       │ data triangulation        │ (cần nhiều nguồn)  │
  │                  │ "nhiều người cùng than?"  │                     │
  ├──────────────────┼──────────────────────────┼─────────────────────┤
  │ Node Death       │ Observable fact           │ High                │
  │ (company die)    │ "công ty phá sản = fact"  │ (binary, rõ ràng)  │
  ├──────────────────┼──────────────────────────┼─────────────────────┤
  │ Arc Extinction   │ Historical / statistical  │ Low                 │
  │ (cực hiếm)       │ "ngành hoàn toàn biến    │ (rare, hard to     │
  │                  │  mất?" — cần data macro   │ confirm in real-time)│
  └──────────────────┴──────────────────────────┴─────────────────────┘

  → Scale NHỎ (shift, node death): verification EASIER (observable)
  → Scale LỚN (disruption, extinction): verification HARDER (cần macro data)


  4 APPROACHES (refined):

  A. BODY-CHECK + DOMAIN FEEDBACK (cho Shift):
     → Client's OWN experience over time = valid signal
     → "Pattern cũ works less and less?" → body đã verify gradually
     → + Domain feedback: P&L, career progress, market response
     → = Ask-AI Dual Check applies NATURALLY cho gradual shift

  B. PEER PATTERN MATCHING (cho Disruption):
     → "Nhiều người cùng context report similar?" → collective signal
     → = Aggregated individual body-checks = proxy collective verification
     → AI CAN ask: "người khác trong ngành bạn có gặp tương tự?"
     → Already partially in ⑧ — extend with explicit scale tagging

  C. DATA TRIANGULATION (cho larger scale):
     → AI cross-reference: industry data, news, employment statistics
     → = External verification thay vì body verification
     → Confidence = f(data quality × source diversity × recency)

  D. HONEST CONFIDENCE TAGGING (cho tất cả):
     → Scale nhỏ → tag HIGH confidence ("observable: company closed")
     → Scale lớn → tag LOW confidence ("hypothesis: industry shifting")
     → KHÔNG claim collective-level without evidence
     → CAN claim "signals suggest — verify with data"

  RECOMMENDATION: Match method to scale
    → Shift → A (body + domain)
    → Disruption → B + C (peer + data)
    → Node Death → fact check (binary)
    → Arc Extinction → C + D (macro data + honest uncertainty)
```

---

## §C — DECISION FRAMEWORK: EXPAND vs NEW FILE

```
KHI NÀO QUYẾT ĐỊNH:
  → Khi Coordination-Node.md + Gap-Distribution-Profile.md đã được drill
  → Khi có thêm cases thực tế test collective detection
  → Khi biết rõ: bao nhiêu content cần thêm

OPTION A: EXPAND AI-Schema-Detection §3
  → Thêm capabilities ⑩-⑭ (1 per gap above)
  → Pro: mọi AI capability trong 1 file
  → Con: file 1,709L → ~2,300L+ (hơi dài)
  → Phù hợp nếu: mỗi gap = ~100-150L (compact)

OPTION B: TẠO FILE MỚI
  → AI-Collective-Detection.md hoặc AI-Collective-Navigation.md
  → Pro: tách rõ individual vs collective AI capability
  → Con: 2 files → user phải đọc cả 2
  → Phù hợp nếu: mỗi gap = ~200-300L (cần depth)

OPTION C: HYBRID
  → AI-Schema-Detection: add brief NOTE ở ⑧ pointing to new file
  → New file: deep collective-specific capabilities
  → Pro: best of both (main file compact, detail separated)
  → Con: maintenance 2 files

TIÊU CHÍ QUYẾT ĐỊNH:
  → Nếu total new content < 500L → Option A (expand)
  → Nếu total new content 500-1000L → Option C (hybrid)
  → Nếu total new content > 1000L → Option B (separate file)
```

---

## §D — CROSS-REFERENCES

```
FILES CẦN ĐỌC TRƯỚC KHI IMPLEMENT:
  → AI-Schema-Detection.md v2.0 §3 ⑧⑨ — current collective capability
  → Collective-Arc-Dynamics.md v1.1 — §4.5 scale-dependent disruption (GAP 1 primary source)
  → Coordination-Node.md v1.0 — node assessment, 5 capabilities, Emergence≠Effectiveness (GAP 2)
  → Collective-Schema-Pressure.md v1.0 — compound pressure (GAP 3)
  → Gap-Distribution-Profile.md v1.0 — gap distribution, collective gap landscape (GAP 4)
  → Collective-Body.md v2.0 §4.2 ⑥ — no unified PFC, by-product match (GAP 5)
  → Ask-AI.md v3.1 §6.1 — Dual Check principle (body=QC, domain=arbiter)
  → Body-Base.md v3.1 §6 — domain feedback = final arbiter
  → Status.md v2.1 §6 — Disruption → Recalibrate cycle (GAP 1 + GAP 2)

NOTE: All Collective/ files now in Core-Deep-Dive/Collective/ (moved 2026-05-18)
```
