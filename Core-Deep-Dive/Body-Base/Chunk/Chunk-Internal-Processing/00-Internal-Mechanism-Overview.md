---
title: 00 — Internal Processing Mechanism Overview (F4 Sketch)
created: 2026-04-17 (N+6 session)
status: SKETCH v1.0 — overview trước khi drill chi tiết từng file
scope: F4 — Internal novel chunk formation + transformation mechanism
purpose: |
  Sketch toàn cảnh F4 TRƯỚC KHI drill F3.
  → Xác định rõ BOUNDARY giữa F3 (external install) và F4 (internal transform)
  → F3 viết SAU file này → biết chính xác cần hand-off gì
  → F4 drill chi tiết SAU KHI F3 hoàn thiện
parent: ../plan.md §3.3
dependencies:
  - F1 Child-Chunk-Development (substrate mechanism — COMPLETE)
  - F3 Chunk-External-Development (external install — PENDING)
  - Logic-Planning.md (Logic side đóng gói — COMPLETE)
  - Neural-Processing-Flow.md (hardware foundation — COMPLETE)
test_hypotheses: H2, H5, H6, H12
language: Tiếng Việt primary + English technical
---

# 00 — Internal Processing Mechanism Overview (F4 Sketch)

> **File này = SKETCH**, không phải drill chi tiết. Mục đích:
> 1. Map toàn bộ F4 territory
> 2. Xác định rõ boundary F3 ↔ F4
> 3. Chuẩn bị cho F3 biết cần hand-off gì
> 4. Chuẩn bị cho F4 drill sessions sau

---

## §0 — Vị trí trong framework

### §0.1 — 4-Folder Architecture

```
  ┌──────────────────────────────────────────────────────────────┐
  │ F1 Child-Chunk-Development ✅ COMPLETE                       │
  │ = HOW biology compiles raw input → chunks (substrate)        │
  │ = 12 files, ~11,596L, 7 Nút Thắt committed                  │
  ├──────────────────────────────────────────────────────────────┤
  │ F3 Chunk-External-Development ⏳ (thu gọn post-N+5 pivot)   │
  │ = HOW external source INSTALLS chunks (top-down)             │
  │ = co-attention, imitation, language, cultural transmission   │
  ├──────────────────────────────────────────────────────────────┤
  │ F4 Chunk-Internal-Processing 🎯 (file này = sketch)         │
  │ = HOW internal processing TRANSFORMS existing chunks         │
  │ = logical connection, feeling-intuition, decay, insight      │
  ├──────────────────────────────────────────────────────────────┤
  │ 99-Master-Synthesis (tích hợp tất cả)                        │
  └──────────────────────────────────────────────────────────────┘
```

### §0.2 — F4 trong 2-part model (Logic-Feeling)

```
⭐ N+5 PIVOT INSIGHT: "Con người thực sự chỉ có 2 phần: Logic và Feeling"

  F4 = NƠI LOGIC VÀ FEELING GẶP NHAU:

  LOGIC TERRITORY (trong F4):
    • Chunk-chunk logical connection (Thread 2)
    • Chain formation + anchor management (Thread 8)
    • Cognition upgrade via accumulated chunks (Thread 9)

  FEELING TERRITORY (trong F4):
    • Feeling-intuition gradient (Thread 3)
    • Right-wrong vague detection (Thread 10)
    • Insight emergence = body signal TRƯỚC logic (Thread mới)

  BRIDGE:
    • Logical connection cần body "vote" (feel "nối được" hay "không")
    • Insight = feel-first → logic sau
    • Vague = body biết nhưng logic chưa biết
    
  → F4 = territory quan trọng nhất cho CORE FRAMEWORK VALUE (hiểu Feeling)
  → Logic side đã đóng gói (Logic-Planning.md) → AI hỗ trợ
  → Feeling side CẦN hiểu sâu → F4 + Feeling deep dive
```

### §0.3 — F4 trong kiến trúc layer

```
  ┌─────────────────────────────────────────────────┐
  │  PLAN (chain labeled chunks → execute)           │  ← Logic-Planning.md ✅
  ├─────────────────────────────────────────────────┤
  │  LABEL (anchor cho chunk)                        │  ← F3 External ⏳
  ├─────────────────────────────────────────────────┤
  │  ⭐ CHUNK PROCESSING (transform existing chunks) │  ← F4 (file này) 🎯
  │    connect / decay / insight / vague / upgrade   │
  ├─────────────────────────────────────────────────┤
  │  CHUNK (compiled pattern)                        │  ← F1 ✅
  ├─────────────────────────────────────────────────┤
  │  FEELING (body-feedback processing)              │  ← Feeling deep ⏳
  ├─────────────────────────────────────────────────┤
  │  BODY-INPUT (raw sensory data)                   │  ← Neural-Processing-Flow ✅
  └─────────────────────────────────────────────────┘

  F4 = PROCESSING layer giữa compiled chunks và plan output.
  = Cái gì XẢY RA với chunks sau khi đã compile (F1) + đã install label (F3)?
  = Connect / Decay / Transform / Generate novel / Upgrade
```

---

## §1 — F4 là gì: Internal Processing definition

### §1.1 — Core definition

```
F4 = HOW INTERNAL PROCESSING TRANSFORMS EXISTING CHUNKS INTO NOVEL CHUNKS
     — without direct external shared template
     — using PFC hold + body feedback + chunk association

Mechanism chính:
  ① PFC hold 2+ chunks trong Working Memory (~3-5 slots)
  ② Check relationships: overlap? conflict? complement?
  ③ Body feedback: "nối được" / "sai sai" / "aha!"
  ④ Novel chunk emerges: new pattern compiled from combination
  ⑤ Seek label: articulate → anchor → dùng trong plan
```

### §1.2 — Phân biệt F3 vs F4

```
F3 (EXTERNAL INSTALL):
  Source:    người/sách/văn hóa/giáo dục cung cấp
  Direction: TOP-DOWN (nhận label → compile chunk)
  Example:   học label "gravity" → thả vật → thấy rơi → chunk compile
  Key:       chunk template có sẵn ở NGOÀI
  = Direction B (Logic-Planning.md §7.4)

F4 (INTERNAL TRANSFORM):
  Source:    bản thân tạo ra, không có template từ ngoài
  Direction: BOTTOM-UP (feel gì đó → tìm label)
  Example:   "sao sao ấy" về code → articulate → "à, God Object!"
  Key:       chunk MỚI sinh ra TRONG ĐẦU
  = Direction A (Logic-Planning.md §7.4)

OVERLAP:
  Cùng 1 case có thể là CẢ F3 lẫn F4:
  Einstein ĐỌC Newton (F3: external install Newtonian chunks)
  → NHIỀU NĂM suy nghĩ (F4: internal transform → aha relativity)
  → F3 cung cấp NGUYÊN LIỆU, F4 BIẾN ĐỔI nguyên liệu

⭐ F4 KHÔNG THỂ XẢY RA NẾU KHÔNG CÓ F1 + F3:
  → F1 compile raw chunks (substrate)
  → F3 install labels + external knowledge (library)
  → F4 transform library thành novel insights
  → "Creativity = novel recombination of existing chunks"
    (nothing comes from nothing — mọi insight build on existing chunks)
```

### §1.3 — Age-independence

```
F4 mechanism GIỐNG NHAU ở mọi lứa tuổi:

  Trẻ 2 tuổi: 2 chunks "con chó" + "cắn" → novel chunk "chó nguy hiểm"
  Học sinh:    "tam giác" + "Pytago" → novel chunk "tính cạnh huyền"
  Einstein:    "Maxwell" + "Galilean transform" → "conflict!" → novel chunk "spacetime"
  Nhạc sĩ:     melody A + harmony B → novel chunk "bài mới"

  = CÙNG mechanism: PFC hold → check → body vote → novel emerge
  = KHÁC: number of chunks + depth + domain sophistication
  = "Intelligence" ≠ better mechanism — "Intelligence" = more + deeper chunks
```

---

## §2 — 6 Processing Modes (toàn bộ threads trong F4)

### §2.1 — Logical Connection (Thread 2, H2 test)

```
QUESTION: Khi PFC hold chunk A + chunk B, cái gì xảy ra?

USER'S FORMULATION (verbatim):
  "2 chunk sẽ cho cảm giác chúng nối với nhau, PFC hold và chúng có nối 
   được với nhau không, nhưng não bộ không phải là 2 cục noron nối với nhau, 
   mà là pattern fire ở nhiều vùng não, và pattern nào đó được coi là 1 chunk"

MECHANISM (to drill):
  ① PFC hold chunk A (pattern fire in WM)
  ② PFC hold chunk B (pattern fire in WM)
  ③ OVERLAP CHECK: A và B share neurons/areas?
     → Nhiều overlap = "liên quan" (spreading activation — Collins & Loftus 1975)
     → Ít overlap = "không liên quan"
     → Conflict overlap = "mâu thuẫn"
  ④ BODY VOTE: "nối được" feel (smooth) vs "không" feel (resistance)
  ⑤ OUTPUT: verbal articulation "A liên quan B qua X"

H2 TEST: Thread 2 = 4th connection type?
  Type 1: Shared contamination (Schema.md §2 — A contaminate B qua shared context)
  Type 2: Aha moment (Chunk-Search-Advanced §2 — sudden strong link)
  Type 3: Compile meta-chunk (Chunk.md §2 — A+B compile thành AB)
  Type 4 (H2): Static logical linking (PFC intentional — hold A+B, check link)

  → H2 claim: Type 4 is DISTINCT mechanism
  → Drill cần: formalize mechanism, test against other 3 types

EXAMPLES (from user):
  • Nhà thờ ↔ bạn (bạn đi lễ cùng mình) = shared context → type 1 or 4?
  • Mẹ ↔ cô giáo (mẹ gọi điện mắng vì điểm thấp) = multiple connection types
```

### §2.2 — Feeling-Intuition Gradient (Thread 3, H5 test)

```
QUESTION: Feeling và intuition CÙNG mechanism hay KHÁC mechanism?

USER'S FORMULATION:
  "Feeling = cảm nhận vật lý body-base, intuition = cảm nhận imagine?"
  "Thật ra 2 cái này không rõ ràng"

SPECTRUM (to drill):

  ┌─────────────────────────────────────────────────────────────────┐
  │  CLEAR                                                   VAGUE │
  │  ←─────────────────────────────────────────────────────────→   │
  │                                                                │
  │  Body signal     Feeling    Gut     Intuition   Hunch  Premon- │
  │  (đau, đói)      (buồn)   feeling   (linh     (ngờ   ition    │
  │                            (bụng)    cảm)      ngợ)           │
  │                                                                │
  │  Source: BODY    Source: BODY+PFC    Source: PFC+WEAK BODY     │
  │  Speed: FAST     Speed: MEDIUM      Speed: SLOW (search)      │
  │  Label: EASY     Label: MEDIUM      Label: HARD (articulable?)│
  │  Trust: HIGH     Trust: MEDIUM      Trust: VARIABLE           │
  └─────────────────────────────────────────────────────────────────┘

H5 TEST: "Lờ mờ = multi-weak-signal convergence"
  → Intuition = NHIỀU weak signals cùng converge → body sense "gì đó"
  → Feeling = FEW strong signals → body sense RÕ
  → CÙNG mechanism (PFC observe body-base), KHÁC signal profile

EXPERT VS BEGINNER (Klein 1998):
  Expert: "gut feeling" → ĐÚNG (many compiled chunks fire weakly in parallel)
  Beginner: "gut feeling" → OFTEN WRONG (few chunks, confabulation)
  → Expertise = more chunks → better multi-signal convergence → better intuition

CONNECTION TO FEELING SIDE:
  ⭐ Thread 3 = TRỰC TIẾP core framework value
  → Hiểu gradient này = hiểu KHI NÀO trust feeling, khi nào verify
  → AI era: AI verify logic, human trust feeling → complementary
  → Gendlin Focusing: TRAINING ở lại vùng "lờ mờ" → dần rõ (L3 → L6)
```

### §2.3 — Chain + Anchor Dynamics (Thread 8, H6 test)

```
QUESTION: Tại sao chunk cần anchor? Decay thế nào không có anchor?

USER'S FORMULATION (verbatim):
  "Tại sao phải có anchor verbal, hoặc hình ảnh, hoặc đồ vật, hoặc context, 
   ritual, để giữ chunk trong chuỗi chain"
  "Nếu chunk không thể gán anchor thì sẽ duy trì được dài không hay sẽ 
   dễ suy thoái và quên"

MECHANISM (to drill):
  ① CHAIN FORMATION: 2 chunks A→B fire together → strengthen A→B link
  ② ANCHOR = high-activation retrieval path:
     → Verbal label: "nhớ lại từ X" → chain fires → recall
     → Ritual action: "bắt tay" → social chunk fires
     → Visual cue: "biển hiệu" → location chunk fires
     → Object: "cái ly đó" → event chunk fires
     → Context: "căn phòng này" → memory chunk fires
  ③ WITHOUT ANCHOR: chunk still exists but NO retrieval path
     → Decay = NOT deletion — decay = WEAKENING of fire probability
     → Ebbinghaus 1885: exponential decay without rehearsal

H6 TEST: Decay follows Ebbinghaus without anchor?
  → Prediction: unanchored chunks show classic forgetting curve
  → Prediction: anchored chunks show plateau (retrieval prevents decay)
  → Anchor type ranking (to test): verbal > ritual > visual > object > context

ANCHOR-SCHEMA SYSTEM CONNECTION:
  → Anchor-Schema.md: 4 nguồn anchor (Trust, Sync, Schema, Verbal)
  → Logic-Planning.md §2: 3 tầng anchor (Individual / Group / Global)
  → F4 formalizes: anchor = RETRIEVAL PATH, không phải chunk content
  → Chunk vẫn TỒN TẠI khi mất anchor — chỉ KHÔNG TRUY CẬP ĐƯỢC
  → = "Cái tôi biết nhưng không nhớ ra" = chunk without active anchor
  → = Tip-of-tongue phenomenon (Brown & McNeill 1966)
```

### §2.4 — Right-Wrong Vague Detection (Thread 10, H5 support)

```
QUESTION: "PFC biết right-wrong lờ mờ" — mechanism CỤ THỂ là gì?

USER'S FORMULATION (from Feeling session):
  "PFC biết right-wrong lờ mờ" — vague detection

MECHANISM (to drill):
  ① CLEAR RIGHT-WRONG (đã cover Feeling Theme D):
     → Strong chunks fire → body signal rõ → "ĐÚNG" hoặc "SAI"
     → ACC detect NO conflict → "đúng" / ACC detect STRONG conflict → "sai"

  ② VAGUE RIGHT-WRONG (F4 territory):
     → Weak/partial chunks fire → body signal MỜ → "sao sao ấy"
     → ACC detect MILD conflict → alert nhưng KHÔNG rõ source
     → = "Có gì đó sai nhưng không biết cái gì"

  TWO POSSIBILITIES (H5):
     (a) Single weak signal: 1 chunk fire yếu → vague signal
     (b) Multi-weak-signal convergence: NHIỀU chunks fire yếu cùng lúc
         → converge → vague but DIRECTIONALLY correct
     → H5 claims (b) is primary mechanism for expert intuition

  TRAINING:
     → Gendlin Focusing: ở lại với "sao sao" → dần rõ
     → = PFC maintain attention on ACC mild alert → more chunks fire → clearer
     → = Somatic-Articulation Loop applied to vague detection
     → Expert: CAN dwell → signals clarify → ACCURATE gut feeling
     → Beginner: CANNOT dwell → jump to label too fast → INACCURATE

CONNECTION TO FRAMEWORK:
  ⭐ Vague detection = FEELING LITERACY core skill
  → Người có high vague detection skill → make better decisions
  → AI era: AI check logic (clear domain), human detect vague (body domain)
  → "Con người cần FEEL đúng" = INCLUDES vague detection
```

### §2.5 — Insight + Tacit Knowledge (H12 bridge)

```
QUESTION: Aha moment, tacit knowledge, và gap 2 liên quan thế nào?

AHA MOMENT (Chunk-Search-Advanced §2 + body-feedback):
  ① Chunks simmering in background (DMN active)
  ② Suddenly: strong connection fires → BURST of activation
  ③ VTA fires dopamine (SALIENCE ALERT — "biến động lớn!")
  ④ Schemas/dissonance resolved → body-need match → OPIOID = actual reward
     + if threat present: threat resolved → cortisol rút dần (additional relief)
     (⚠️ N+10 correction: dopamine ≠ reward. Opioid = reward. See 01 §1.2)
  ⑤ PFC observe: "à, A liên quan B qua C!"
  ⑥ Novel chunk compiles (emotional peak mechanism)
  
  → Aha = Type 2 connection (sudden strong link)
  → KHÁC Type 4 logical connection (intentional, gradual)
  → Aha cannot be forced — can only create CONDITIONS (incubation)

TACIT KNOWLEDGE (Polanyi 1966):
  "We can know more than we can tell"
  
  = Chunks compiled DEEP (nhiều modalities, nhiều repetitions)
  → Fire AS ONE → PFC observe KẾT QUẢ, không observe PROCESS
  → Expert "biết" answer → nhưng KHÔNG articulate được tại sao
  → = Klein 1998: firefighters "just know" which roof will collapse
  
  Mechanism: meta-chunks compiled so deep → PFC chỉ thấy output
  → Process INVISIBLE to PFC (runs in substrate, below observation)
  → = L1-L3 feeling territory (body biết, PFC chưa biết rõ)

GAP 2 — POST-VERBAL BYPASS (H12):
  ① Adult có label library (extensive vocabulary)
  ② Internal processing creates NOVEL chunk
  ③ PFC search library → NO fitting label exists
  ④ = "Gần đúng / hơi mâu thuẫn / concept mới chưa có từ"
  ⑤ Chunk persists via felt sense, description, metaphor
  ⑥ If shared → cultural pressure to coin new word
  ⑦ Language evolves

  H12 prediction: language evolution driven by gap 2 pressure
  → Recent examples: "gaslight" (verb), "doomscroll", "cancel culture"
  → Each = internal chunk EXISTED before word was coined
  → Word emerges BECAUSE community needs shared anchor

  ⭐ GAP 2 = Somatic-Articulation Loop in REVERSE:
  → Somatic-Articulation: individual chunk → find existing label
  → Gap 2: individual chunk → NO existing label → CREATE new label
  → = Language GROWS because internal processing OUTPACES existing vocabulary

CONNECTION TO FRAMEWORK:
  → H12 connects F3 (language evolution) ↔ F4 (internal insight)
  → Bidirectional: F3 installs labels → F4 uses → F4 creates novel → F3 language evolves
  → = "Chicken-egg" resolved: F1 substrate comes first, then F3↔F4 co-evolve
```

### §2.6 — Cognition Upgrade (Thread 9)

```
QUESTION: Có phải "nâng cấp nhận thức" là discrete jump hay gradient?

USER'S FORMULATION:
  "Lúc nào mình vui, lúc nào mình buồn → self-awareness"
  "Khi chunk tích lũy đủ lớn, chúng có thể đoán được chuyển động quả bóng, 
   nhưng tính cách của mẹ thì chuỗi chunk không đủ để đoán"

MECHANISM (to drill):
  ① Chunks accumulate (F1 + F3) → database grows
  ② At certain DATABASE SIZE thresholds → new CAPABILITY emerges
  ③ = Emergent property: enough bricks → can build bridge (not just wall)
  ④ = Phase transition in complex system (not biological maturation)

PIAGET RECONCILIATION:
  Piaget stages (sensorimotor → preoperational → concrete → formal):
  → Framework: KHÔNG phải hardware stages
  → = Chunk database size thresholds:
    Sensorimotor: body-input chunks compiling (F1 territory)
    Preoperational: enough labeled chunks for symbolic play
    Concrete: enough domain chunks for logic within domain
    Formal: enough meta-chunks for abstract logic across domains
  → Individual variation = different chunk accumulation RATES (not stages)

SELF-PATTERN-MATCH UPGRADE (cross-ref Agent/):
  → Self-Pattern-Match §5: 8 stages of self-model development
  → Each "upgrade" = accumulated self-related chunks reach new threshold
  → → meta-cognition = chunks ABOUT OWN CHUNKS (recursive)
  → → "Biết mình biết gì" = PFC observe own chunk library

WHY "UPGRADE" FEELS DISCRETE:
  → = Same as Nút Thắt 1 gradient verdict
  → Gradient accumulation → cross behavioral threshold → appears "sudden"
  → Parent observes: "hôm nay con HIỂU" → actually: gradient crossed threshold today
  → = "Aha" at individual level, "stage transition" at population level

STUCK COGNITION:
  → Some adults "stuck" at concrete operational
  → Framework: NOT hardware limit — CHUNKS MISSING in relevant domains
  → Remedy: install chunks (education, experience, exposure)
  → = "Nâng cấp nhận thức" = install more chunks + connect existing ones
  → ⭐ AI ERA: AI can help install chunks FASTER → cognition upgrade FASTER
     → But: upgrade PERCEPTION (body-base feel) still requires REAL EXPERIENCE
     → AI install labels (Direction B) → human must still FEEL (Direction A)
```

---

## §3 — Cross-Thread Connections

### §3.1 — How 6 modes connect

```
  ┌────────────────────────────────────────────────────────────┐
  │                  F4 INTERNAL PROCESSING                     │
  │                                                            │
  │  LOGICAL CONNECTION ←──→ CHAIN + ANCHOR DYNAMICS           │
  │  (§2.1 — PFC hold 2      (§2.3 — how connections         │
  │   chunks, check link)      persist or decay)               │
  │         │                         │                        │
  │         ↕                         ↕                        │
  │  INSIGHT + TACIT ←──→ COGNITION UPGRADE                    │
  │  (§2.5 — novel           (§2.6 — accumulated              │
  │   chunk emerges)          chunks → new capability)         │
  │         │                         │                        │
  │         ↕                         ↕                        │
  │  FEELING-INTUITION ←──→ RIGHT-WRONG VAGUE                  │
  │  (§2.2 — body signal     (§2.4 — ACC mild                 │
  │   clarity spectrum)       conflict detection)              │
  │                                                            │
  │  TOP = LOGIC territory (verifiable, AI-assisted)           │
  │  BOTTOM = FEELING territory (body-based, human-only)       │
  │  MIDDLE = BRIDGE (where insight + upgrade happen)          │
  └────────────────────────────────────────────────────────────┘

CONNECTION LOGIC:
  • Logical connection (§2.1) CREATES chains → Chain dynamics (§2.3) determines persistence
  • Chains accumulate → Cognition upgrade (§2.6) emerges
  • Insight (§2.5) = SUDDEN connection → often BYPASSES gradual chain building
  • Feeling-intuition (§2.2) = EVALUATION mechanism for all other modes
  • Right-wrong vague (§2.4) = DETECTION mechanism that triggers search
  
  → ALL 6 modes USE feeling as feedback
  → NONE operates purely in logic territory
  → = "Even logical connection requires body vote" (user's insight)
```

### §3.2 — F4 ↔ Feeling connection

```
⭐ F4 = NƠI FRAMEWORK CORE VALUE THỂ HIỆN RÕ NHẤT:

  "Con người cần FEEL đúng → AI sẽ giúp PLAN đúng"

  F4 threads CHỨNG MINH tại sao feeling literacy QUAN TRỌNG:

  1. LOGICAL CONNECTION: body vote "nối được" hay "không"
     → Nếu feeling literacy thấp → accept wrong connections
     → Nếu feeling literacy cao → detect "sai sai" sớm

  2. INTUITION: multi-weak-signal convergence
     → Nếu feeling literacy thấp → bỏ qua gut feeling → miss insight
     → Nếu feeling literacy cao → dwell với signal → insight emerge

  3. VAGUE DETECTION: ACC mild conflict
     → Nếu feeling literacy thấp → "mọi thứ ok" (false ok)
     → Nếu feeling literacy cao → "có gì đó sai" → investigate

  4. INSIGHT: aha moment from body
     → Nếu feeling literacy thấp → aha nhưng không articulate được
     → Nếu feeling literacy cao → aha → articulate → dùng trong plan

  5. TACIT KNOWLEDGE: body biết, PFC chưa biết
     → Nếu feeling literacy thấp → body biết nhưng bỏ qua
     → Nếu feeling literacy cao → body biết → trust → act on it

  → FEELING LITERACY = skill set cho TẤT CẢ 5 internal processing modes
  → Training feeling literacy = training F4 capability
  → = Đây là lý do framework PHẢI hiểu Feeling sâu
```

---

## §4 — Dependencies + Input Contracts

### §4.1 — Từ F1 Child-Chunk-Development (COMPLETE)

```
F4 NHẬN từ F1:
  ① Chunk compile mechanism: 4 mechanisms + 5-parameter rate formula
  ② Proto-chunk gradient: strength-weighted, not discrete
  ③ H11: receptive trước productive (~6-12mo gap, ~1:3 ratio)
  ④ NT6: verbal-as-handle hybrid (not 5th modality, not constitutive)
  ⑤ NT3: multi-modal binding (4 concurrent mechanisms)
  ⑥ PFC-Inference Ladder: 5 levels + 10-marker catalog
  ⑦ Non-uniform progression: different arcs compile at different rates
  ⑧ NT7: body-state-at-compile determines chunk association

F4 KHÔNG re-derive:
  → Chunk compilation mechanism (F1 committed)
  → PFC hardware reframe (F1 committed)
  → Pre-verbal substrate (F1 committed)
```

### §4.2 — Từ F3 External-Development (PENDING → F4 waits)

```
F4 NHẬN từ F3:
  ① External install mechanism: how labels arrive on chunks
  ② H3 verdict: grammar = most optimized external anchor
  ③ H7 verdict: valence = chunk × schema interaction
  ④ Cultural transmission mechanism
  ⑤ Direction B pipeline: label-first → compile

F4 EXTENDS:
  → F3 installs chunks → F4 transforms installed chunks
  → F3 provides "library" → F4 provides "processing"
  → F3 Direction B (top-down) → F4 Direction A (bottom-up)
```

### §4.3 — Từ đã-drill sub-folders

```
  Learning-Cycle/ (N+1):
    → Learning mechanism = INPUT cho F4 (chunk formation incl. dissonance cycle)
    → Sleep consolidation details
  
  Agent/ (N+2):
    → Self-Pattern-Match §5: developmental bootstrap = cognition upgrade data
    → Pattern-Resonance: emergent mutual mechanism = social internal processing
  
  Body-Feedback-Draft/ (N+3):
    → H10 5-precondition model = EVALUATION framework cho F4 body votes
    → Dissonance-reward signal = FEEDBACK mechanism cho internal processing
```

### §4.4 — Từ Core framework files

```
  Logic-Feeling.md:       2 processing modes — F4 bridges both
  Feeling.md:             7-layer model — F4 operates in L3-L5 territory
  Somatic-Articulation:   Body→words transition — F4 uses for insight→label
  Neural-Processing-Flow: Hardware — F4 runs ON this hardware
  Chunk-Search-Advanced:  Aha mechanism §2 — F4 formalizes Type 2 connection
  Schema/Chunk.md:        4 compile mechanisms — F4 adds internal processing
  Schema/Schema.md §2:    3 connection types — H2 tests 4th type
```

---

## §5 — Hypotheses to test

```
┌─────────────────────────────────────────────────────────────────────────┐
│ #   │ Hypothesis                                          │ Status    │
├─────────────────────────────────────────────────────────────────────────┤
│ H2  │ Thread 2 = 4th connection type (static logical      │ ⏳ F4     │
│     │ linking, distinct from contamination/aha/meta-chunk) │ drill     │
├─────────────────────────────────────────────────────────────────────────┤
│ H5  │ "Lờ mờ" = multi-weak-signal convergence            │ ⏳ F4     │
│     │ (Thread 3 + 10 overlap)                              │ drill     │
├─────────────────────────────────────────────────────────────────────────┤
│ H6  │ Chunk decay without anchor follows Ebbinghaus.       │ ⏳ F4     │
│     │ Anchor type ranking: verbal > ritual > visual >      │ drill     │
│     │ object > context                                     │           │
├─────────────────────────────────────────────────────────────────────────┤
│ H12 │ Language evolution driven by gap 2 post-verbal       │ ⏳ F4     │
│     │ bypass pressure (bridge F3↔F4)                       │ drill     │
└─────────────────────────────────────────────────────────────────────────┘

Từ parent plan: H2 + H5 + H6 assigned F4. H12 bridge F3↔F4.
H3 + H4 + H7 assigned F3 (with brief F4 cross-ref where relevant).
```

---

## §6 — Drill File Sequence (plan cho sessions sau)

```
Chunk-Internal-Processing/
├── plan.md (existing stub → expand khi drill bắt đầu)
├── 00-Internal-Mechanism-Overview.md ✅ (file này — SKETCH)
│
│  [TO DRILL — 6 files]
├── 01-Chunk-Connection-Logical.md (~900-1200L)
│   — Thread 2 + H2 test
│   — 4th connection type formalization
│   — Spreading activation mechanism (Collins & Loftus 1975)
│   — Body vote mechanism for connection check
│
├── 02-Feeling-Intuition-Gradient.md (~900-1200L)
│   — Thread 3 + H5 test
│   — Spectrum formalization: body signal → feeling → intuition → hunch
│   — Expert vs beginner intuition (Klein 1998)
│   — Signal profile analysis (strong-few vs weak-many)
│   — Training: Gendlin Focusing as intuition training
│
├── 03-Chain-Anchor-Decay.md (~800-1100L)
│   — Thread 8 + H6 test
│   — Chain formation mechanism
│   — Anchor type ranking + evidence
│   — Ebbinghaus forgetting curve application
│   — Anchor-Schema cross-ref
│   — Tip-of-tongue + lost chunks
│
├── 04-Right-Wrong-Vague.md (~800-1100L)
│   — Thread 10 + H5 support
│   — ACC mechanism for vague detection
│   — Clear vs vague cases (bridge Feeling Theme D)
│   — Training vague detection
│   — Grammatical support ("hình như", "có vẻ")
│
├── 05-Insight-Tacit-Upgrade.md (~900-1200L)
│   — Aha mechanism + Polanyi tacit knowledge
│   — Gap 2 formalization + H12 verdict
│   — Cognition upgrade mechanism (Thread 9)
│   — Piaget reconciliation
│   — Einstein + game dev case studies
│
└── 06-Internal-Synthesis.md (~500-700L)
    — H2 + H5 + H6 + H12 verdicts
    — F4 framework contributions
    — Output contracts cho 99-Master-Synthesis
    — Bridge to Feeling deep dive
```

**Thay đổi từ stub plan:**
- Merged Thread 9 (Cognition Upgrade) + Insight + Tacit → 1 file `05-Insight-Tacit-Upgrade.md`
  (vì upgrade = accumulated chunks → threshold, cùng mechanism với insight)
- Old: 7 files. New: 6 files (merged 05+Thread 9)
- Tổng estimate: ~4800-6400L across 6 files

**Drill sessions**: 2 sessions (N+7, N+8 hoặc tùy tiến độ F3)
- Session A: 01 + 02 + 03 (logical + feeling + chain)
- Session B: 04 + 05 + 06 (vague + insight-upgrade + synthesis)

---

## §7 — Honest Assessment

```
═══════════════════════════════════════
🟢 WELL-GROUNDED (evidence strong)
═══════════════════════════════════════

  Ebbinghaus forgetting curve:          Ebbinghaus 1885, numerous replications
  Spreading activation:                  Collins & Loftus 1975, extensive support
  Expert intuition mechanism:            Klein 1998, Kahneman & Klein 2009
  Tacit knowledge concept:               Polanyi 1966, widely accepted
  ACC conflict detection:                Botvinick et al. 2004, established
  Aha/insight neuroscience:              Kounios & Beeman 2009, fMRI evidence
  Working memory limits:                 Cowan 2001, Miller 1956, extensive
  Gendlin Focusing:                      Gendlin 1978, clinical evidence


═══════════════════════════════════════
🟡 FRAMEWORK SYNTHESIS (plausible, novel)
═══════════════════════════════════════

  4th connection type (H2):              Framework distinction, needs formalization
  Multi-weak-signal convergence (H5):    Consistent with evidence, novel framing
  Anchor type ranking (H6):             Intuitive, needs systematic evidence
  Vague = ACC mild conflict:            Plausible, not directly tested
  Cognition upgrade = chunk threshold:  Consistent with developmental data, novel reframe
  Feeling literacy as F4 enabler:       Framework contribution, testable
  Direction A/B unified in F4:          Framework synthesis


═══════════════════════════════════════
🔴 SPECULATIVE (framework hypothesis)
═══════════════════════════════════════

  H12 gap 2 drives language evolution:   Plausible but hard to test directly
  Anchor ranking specific order:          Needs empirical comparison study
  Insight = Direction A exclusive:        May have Direction B component too
  "Intelligence = more chunks":           Oversimplification, useful as heuristic
```

---

## §8 — What F3 Needs to Hand Off to F4

```
⭐ F3 MUST DELIVER these as OUTPUT CONTRACTS cho F4:

  ① EXTERNAL INSTALL MECHANISM formalized:
     → How co-attention, imitation, label install works
     → F4 takes these as "how chunks GOT into library"
  
  ② H3 VERDICT (grammar = most optimized external anchor):
     → F4 uses this as given: language chunks are the richest external install
  
  ③ H7 VERDICT (valence = chunk × schema interaction):
     → F4 uses this: internal processing can CHANGE valence by changing schema context
  
  ④ CULTURAL TRANSMISSION mechanism:
     → F4 uses this: H12 language evolution is the REVERSE of cultural transmission
     → F3: culture → individual (install). F4: individual → culture (coin new word)
  
  ⑤ THREAD 1 + THREAD 9 positioning:
     → F3 briefly positions external component
     → F4 deeply drills internal component
     → Handoff boundary explicit

  ⑥ DIRECTION B pipeline detail:
     → F4 needs Direction B understood to contrast with Direction A
```

---

> **00-Internal-Mechanism-Overview.md — End of file (SKETCH v1.0).**
>
> F4 territory mapped. Boundaries with F3 explicit. Dependencies clear.
> This file will be UPDATED (not rewritten) when F4 drill begins.
> F3 files write NEXT, informed by this sketch.
>
> Phiên bản: Sketch v1.0, 2026-04-17.
