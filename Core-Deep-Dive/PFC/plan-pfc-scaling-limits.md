---
title: Plan — PFC Scaling Limits (Architecture Constraint)
version: 1.0
created: 2026-05-30
status: PLANNED
scope: |
  Thêm §3b vào PFC-Development.md: WHY PFC hit architecture ceiling.
  Framework hypothesis + neuroscience evidence.
  Connects encephalization reversal (§3) with Compiled/Fresh scaling insight.
purpose: |
  §3 hiện tại CÓ data (não giảm 10%) + 4 hypotheses WHY giảm.
  CHƯA CÓ: WHY PFC KHÔNG THỂ tăng thêm ở mức ARCHITECTURE.
  Insight mới: Compiled (parallel) scales well, Fresh (serial) scales poorly.
  = Evolution "biết" rằng giải pháp = compile more, not bigger PFC.
  = 5th hypothesis NỐI 4 cái cũ lại thành unified picture.
language: Tiếng Việt primary + English technical terms
---

# Plan — PFC Scaling Limits: Architecture Constraint

> **Core insight:** PFC = serial coordinator. Body-base = parallel processors.
> **Serial scales poorly. Parallel scales well.**
> **Evolution's solution: compile more, not bigger PFC.**
> **= Explains both WHY PFC peaked AND WHY brain shrinks.**

---

## OVERVIEW

```
  HIỆN TRẠNG (PFC-Development.md §3):
    ✅ Encephalization reversal data (30,000 năm, -10%)
    ✅ 4 hypotheses tại sao giảm
    ✅ Outsource trajectory (language → AI)
    ❌ CHƯA CÓ: WHY PFC cannot scale further (architecture level)
    ❌ CHƯA CÓ: Compiled/Fresh scaling asymmetry
    ❌ CHƯA CÓ: Wiring problem + conduction delay evidence
    ❌ CHƯA CÓ: Cross-species comparison (voi, cá voi)

  PLAN:
    Thêm §3b — PFC ARCHITECTURE CEILING (~50-60 dòng)
    Thêm vào §7 Honest Assessment
    Thêm vào §8 Cross-References
    Version bump v1.0 → v1.1

  NGUYÊN TẮC:
    ① Phân biệt rõ 🟢 (established neuroscience) vs 🟡 (framework synthesis)
    ② Research claims CẦN VERIFY trước khi viết
    ③ KHÔNG thay đổi 4 hypotheses cũ — THÊM 5th unifying perspective
    ④ Compact, targeted — không biến thành survey paper
```

---

## WHAT TO ADD

### §3b — PFC ARCHITECTURE CEILING: Why Fresh Cannot Scale

```
PLACEMENT: sau §3 (encephalization reversal), trước §4 (learning trajectory).
Logic flow: §3 = não GIẢM (data) → §3b = WHY PFC CÓ CEILING (mechanism) → §4 = HOW learning works WITHIN ceiling.

CONTENT — 3 PHYSICAL CONSTRAINTS + 1 FRAMEWORK INSIGHT:

  ═══ CONSTRAINT 1: WIRING PROBLEM (strongest) ═══

  RESEARCH TO VERIFY:
    🟢 Changizi & Shimojo 2005 (Neuroscience Letters):
      As brain scales up, fraction of interconnectable neurons DECREASES.
      Mouse: ~40% neurons can connect to each other.
      Human: <1%.
      → Larger PFC = sees SMALLER fraction of total brain.
    🟢 Herculano-Houzel 2009, 2012:
      Primate brains scale more efficiently than rodent (denser packing).
      But still: white matter grows FASTER than gray matter as brain scales.
      → More wiring, less processing = diminishing returns.
    🟢 Bullmore & Sporns 2012 (Nature Reviews Neuroscience):
      "The economy of brain network organization."
      Brain networks trade off wiring cost vs processing efficiency.
      Long-range connections = expensive in space + energy.

  FRAMEWORK MAPPING:
    PFC = hub that needs connections to NHIỀU vùng.
    Thêm neurons PFC → thêm connections cần → thêm white matter.
    White matter tăng NHANH HƠN gray matter.
    → Diminishing returns: mỗi neuron thêm = contribute ÍT HƠN.


  ═══ CONSTRAINT 2: CONDUCTION DELAY ═══

  RESEARCH TO VERIFY:
    🟢 Myelinated axon max speed: ~120 m/s (established).
    🟢 Ringo et al. 1994 (Cerebral Cortex):
      As brain size increases, conduction delay increases.
      For brain 2× larger → ~40% longer round-trip.
      → Synchronization across regions becomes HARDER.
    🟢 Wang et al. 2008 (PNAS):
      Demonstrated that cortical thickness is partly constrained
      by conduction delay requirements.

  FRAMEWORK MAPPING:
    PFC cần tích hợp real-time từ nhiều vùng (Working Memory).
    Working memory window: ~hundreds of ms.
    Larger PFC = longer axons = signal arrives LATER.
    → Information may be "stale" before PFC finishes processing.
    → = WHY PFC "freshness" has temporal ceiling.


  ═══ CONSTRAINT 3: METABOLIC CEILING ═══

  RESEARCH TO VERIFY:
    🟢 Raichle & Gusnard 2002:
      Brain = 2% body mass, 20% energy consumption.
    🟢 Herculano-Houzel 2012:
      ~6 kcal/billion neurons/day.
      Human cortex ~16 billion neurons → ~86 kcal/day for cortex alone.
    🟢 Fonseca-Azevedo & Herculano-Houzel 2012 (PNAS):
      Great apes limited by caloric intake.
      Raw food → cannot support both large body + large brain.
      Cooking = SOLVED this for humans → allowed brain growth.
      But still: larger brain = more energy = less for body.

  FRAMEWORK MAPPING:
    PFC = most metabolically expensive region (fresh processing = highest glucose).
    Scaling PFC further → energy budget đè lên body-base.
    → Trade-off: bigger PFC ≠ better if body-base underfunded.


  ═══ FRAMEWORK INSIGHT: COMPILED SCALES, FRESH CANNOT ═══

  ⭐ THIS IS THE NOVEL FRAMEWORK CONTRIBUTION:

  Compiled (body-base) = parallel, distributed:
    → Each neuron cluster processes INDEPENDENTLY.
    → Adding more clusters = adding more workers doing independent tasks.
    → Cost per cluster: ~constant (compiled = automatic).
    → Communication: LOCAL (nearby clusters, short axons).
    → = SCALES WELL — like distributed computing.

  Fresh (PFC) = serial, centralized:
    → PFC must COORDINATE across distant regions.
    → Adding more PFC = adding more MANAGERS, not workers.
    → Each manager must communicate with ALL relevant workers.
    → Communication: LONG-RANGE (PFC ↔ distant regions).
    → Communication overhead grows FASTER than capacity.
    → = SCALES POORLY — like central server bottleneck.

  CROSS-SPECIES EVIDENCE:
    🟢 Herculano-Houzel 2014:
      Elephant brain: ~5 kg (3.5× human), ~257 billion neurons.
      BUT: ~98% in cerebellum (motor coordination for huge body).
      Cortex: ~5.6 billion neurons (vs human ~16 billion).
      → Elephant scaled body-base (parallel) WITHOUT scaling cortex proportionally.
      → = Evolution "chose" parallel scaling.

    🟢 Whale brain: even larger, SAME pattern.
      Large body → large cerebellum + body-base.
      Cortex ratio: LOWER than human.

  UNIFYING THE 4 HYPOTHESES (§3):
    Hypothesis ① Efficiency > Size = CONSISTENT (compile better, not bigger PFC).
    Hypothesis ② Externalization = CONSISTENT (outsource fresh to tools/society).
    Hypothesis ③ Self-domestication = brain shrinks because COMPILED social rules
      reduce need for fresh social processing.
    Hypothesis ④ Energy optimization = CONSISTENT (PFC is the most expensive part).

    → §3b = NOT a 5th hypothesis — it's the ARCHITECTURE EXPLANATION
      that UNIFIES why all 4 hypotheses work in the same direction.
    → Evolution's consistent strategy: COMPILE MORE, not BIGGER PFC.

  CONFIDENCE:
    🟢 Wiring problem, conduction delay, metabolic cost = established neuroscience.
    🟡 "Compiled scales, Fresh cannot" as UNIFYING explanation = framework synthesis.
    🟡 Cross-species as evidence for parallel > serial evolutionary strategy = synthesis.
    🔴 Exact PFC size ceiling quantification per species = untested.


  ═══ CONNECTIONS ═══

    → §3 encephalization reversal: §3b EXPLAINS why reversal is architecturally inevitable.
    → §3 outsource trajectory: outsourcing = evolution's RESPONSE to PFC ceiling.
    → §4 learning trajectory: Worker → Compiled = individual version of "compile more."
    → PFC-Operations §9.1: PFC budget = finite = CONSEQUENCE of ceiling.
    → PFC-Operations §9.3: 2-Mode engagement = HOW to work within ceiling
      (compiled analytical knowledge = bypass fresh limit).
    → Inter-Body-Mechanism: Compiled/Fresh axis = foundational distinction.
    → PFC-Operations §10: Compilable Architecture = evolution's solution to PFC ceiling.
```

---

## UPDATES NEEDED

```
  §3b NEW — PFC Architecture Ceiling (~50-60 dòng)
  §7 Honest Assessment — add 🟢 + 🟡 entries for scaling constraints
  §8 Cross-References — add PFC-Operations §9, Inter-Body-Mechanism, Drill-Sound-Brain
  Version: v1.0 → v1.1
  Header: updated date + scope
  Footer: updated summary
```

---

## RESEARCH TO VERIFY BEFORE WRITING

```
  ⚠️ CẦN VERIFY trước khi viết (session sau):

  PRIORITY 1 (core claims):
  [ ] Changizi & Shimojo 2005 — wiring fraction decreases with brain size
  [ ] Ringo et al. 1994 — conduction delay scales with brain size
  [ ] Herculano-Houzel 2014 — elephant neuron counts (257B total, 5.6B cortex)
  [ ] Bullmore & Sporns 2012 — brain network economy

  PRIORITY 2 (supporting):
  [ ] Herculano-Houzel 2012 — metabolic cost per billion neurons
  [ ] Fonseca-Azevedo & Herculano-Houzel 2012 — caloric constraint + cooking
  [ ] Wang et al. 2008 — cortical thickness × conduction delay

  APPROACH:
    WebSearch verify mỗi paper: tồn tại? nội dung đúng? cited by?
    Nếu paper không tồn tại hoặc nội dung sai → loại hoặc thay thế.
    Framework synthesis claims = KHÔNG cần external verify (logic-based).
```

---

## CHECKLIST

```
  [x] Đọc PFC-Development.md v1.0 (563L) — ĐÃ ĐỌC
  [x] Verify research papers (7 papers, Priority 1+2) — ALL 7 VERIFIED
      Corrections: Changizi→Brain Behav Evol (not Neurosci Lett),
      Wang→J Neurosci (not PNAS), "40%/<1%"→scaling law N^(-0.16 to -0.21)
  [x] Xác định §3b placement + content final
  [x] Viết §3b PFC Architecture Ceiling (~115 lines, 3 constraints + framework insight)
  [x] Update §7 Honest Assessment (+7🟢, +4🟡, +1🔴)
  [x] Update §8 Cross-References (+5 entries for §3b connections)
  [x] Version bump → v1.1
```

---

> *Plan v1.0 — PFC Scaling Limits: Architecture Constraint.
> ✅✅ ALL COMPLETE (2026-05-30).
> PFC-Development.md v1.0 → v1.1 (563L → ~703L).
> §3b added: 3 physical constraints (wiring, delay, metabolic) + Compiled/Fresh scaling.
> 7 papers verified (3 corrections applied). §7 + §8 updated.
> Core insight: Compiled scales (parallel), Fresh cannot (serial).
> = Explains encephalization reversal + unifies 4 hypotheses.
> Bonus: §3b↔§4 same strategy different scale = novel parallel discovered.*
