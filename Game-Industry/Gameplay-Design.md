# Gameplay Design — Feel, Mechanics, Flow

> **Mục đích:** Hướng dẫn CỤ THỂ thiết kế gameplay feel + mechanics
> **Trạng thái:** DRAFT v1.0
> **Ngày:** 2026-03-16
> **Prerequisite:** Đọc Core-Principles.md + Player-Psychology.md trước
> **Đối tượng:** Developer, Game Designer, Lead — ai TRỰC TIẾP build gameplay

---

## 1. Gameplay Feel — Tại Sao Quan Trọng Hơn Mọi Thứ

```
Feel = body respond NGAY mỗi khi player tương tác

  60fps × input = 60 micro-reward MỖI GIÂY
  Player chơi 1 phút = 3,600 micro-samples → body evaluate → "sướng" hoặc "empty"
  → Player BIẾT game feel tốt/tệ TRONG 5 GIÂY (dù không giải thích được tại sao)
  → Body biết TRƯỚC brain: "tay sướng" trước "game hay"

Tại sao feel > mọi thứ khác:
  → Feel tốt + xấu → player VẪN chơi (Stickman, Minecraft, Tetris)
  → Feel tệ + đẹp → player QUIT sau 5 phút (nhiều AAA)
  → Feel = NỀN TẢNG, mọi thứ build ON TOP

"Game feel" (Steve Swink, 2008) mô tả hiện tượng.
File này giải thích CƠ CHẾ + CÁCH LÀM.
```

---

## 2. Năm Trụ Cột Của Feel

### Trụ 1: INPUT RESPONSE — "Bấm → Thấy Ngay"

```
= Thời gian từ input đến response (visual + audio)

  < 50ms:   player cảm "instant" — IDEAL
  50-100ms: noticeable nhưng chấp nhận — OK
  100-200ms: sluggish, "trôi", "nặng" — BAD
  > 200ms:  "lag", "broken" — UNPLAYABLE

Tại sao crucial:
  → Body CẦN feedback để confirm "TÔI đang kiểm soát"
  → Delay > 100ms → body disconnect: "không phải tôi điều khiển"
  → Giống gõ chữ mà hiện chậm 200ms → CỰC KHÓ CHỊU
  → Body biết CHÍNH XÁC timing action mình → expect feedback NGAY

Thực hiện:
  → Input polling MỖI FRAME (đừng buffer quá nhiều frames)
  → Animation START ngay frame input nhận
    → ĐỪNG chờ animation trước kết thúc mới bắt đầu animation mới
    → Cancel window: cho phép interrupt animation bằng input mới
  → Audio trigger NGAY khi input (không chờ animation reach hit frame)
  → Visual cue NGAY (flash, color shift) dù full animation chưa xong
  → Principle: "CUE trước ANIMATION" — body nhận signal TRƯỚC mắt thấy đầy đủ

Đo lường:
  → Dùng high-speed camera (240fps) quay tay bấm + screen response
  → Hoặc: in-game timer đo input frame → response frame
  → Target: ≤ 3 frames at 60fps (= 50ms)
```

### Trụ 2: IMPACT FEEDBACK — "Đánh → Thấy LỰC"

```
= Body cảm nhận TÁC ĐỘNG của action lên thế giới game

5 LAYERS — càng nhiều layer → feel càng mạnh:

  LAYER A — HITSTOP (freeze frame):
    → Game DỪNG 2-5 frames (~33-83ms) tại moment of impact
    → Tạo cảm giác "NẶNG", "LỰC" — pause nhấn mạnh khoảnh khắc
    → Không có hitstop → đánh "xuyên qua" → nhẹ, không feel
    → Player KHÔNG BIẾT có hitstop → nhưng body BIẾT
    → Ví dụ: Street Fighter (3-8 frames), God of War, Stickman fighter

    Implementation:
      → On hit: Time.timeScale = 0 (hoặc 0.05) trong N frames
      → Hoặc: chỉ freeze ATTACKER + TARGET, world vẫn chạy
      → Heavy hit = nhiều frames hơn. Light hit = ít frames.
      → ⚠️ Hitstop ĐỘC LẬP với damage calculation (feel ≠ mechanics)

  LAYER B — SCREEN SHAKE:
    → Camera rung proportional với force
    → Implementation: random offset X,Y trong range, decay over frames

    Guidelines:
      Light hit:  shake 2-3px, 3-4 frames, quick decay
      Medium hit: shake 4-6px, 5-7 frames, medium decay
      Heavy hit:  shake 8-12px, 8-12 frames, slow decay
      Explosion:  shake 15-20px, 15-20 frames, rumble decay

    → ⚠️ Option toggle cho accessibility (motion sickness)
    → ⚠️ Quá nhiều shake liên tục → numbing → giảm impact CỦA mỗi shake
    → Save strong shake cho BIG moments

  LAYER C — SFX (audio feedback):
    → MỖI HIT = audio feedback RIÊNG
    → ⚠️ Audio CÓ THỂ = 50% of impact feel

    Guidelines:
      → Pitch variation: random ±5-15% mỗi hit (không lặp → natural)
      → Layer sounds: impact + reaction + environment
        Ví dụ hit: "thud" (impact) + "ugh" (reaction) + "echo" (environment)
      → Bass = power. Crunch = damage. Thud = blunt. Slice = sharp.
      → Heavy hit = thêm sub-bass rumble (feel ở BỤng, không chỉ tai)
      → Kill/final hit = SPECIAL sound (confirm "xong!" → satisfaction burst)

    Test: TẮT audio → chơi → feel GIẢM bao nhiêu %?
      Nếu > 30% → audio đang carry feel → audio ĐÚNG
      Nếu < 10% → audio chưa đủ → invest thêm

  LAYER D — VFX (visual effects):
    → Particles, flashes, trails tại hit point

    Guidelines:
      → Hit flash: enemy flash WHITE 1-2 frames (confirm "hit landed")
      → Particles: sparks/blood/debris AT hit point (direction = force direction)
      → Weapon trail: arc trail theo swing path (visual of motion)
      → Speed lines: khi fast attack (communicate speed)
      → Damage numbers: optional (CÓ confirm damage, NHƯNG có thể clutter)

    → VFX = EYES confirm, SFX = EARS confirm → CẢ HAI = body FULLY confirm

  LAYER E — REACTION (enemy/world response):
    → Enemy/world BỊ ẢNH HƯỞNG visually bởi action
    → = PROOF action có EFFECT (body: "tôi TÁC ĐỘNG được!")

    Guidelines:
      → Knockback: enemy bị đẩy lùi (proportional force)
      → Stagger: enemy animation bị interrupt → flinch/stagger
      → Ragdoll: enemy chết → physics ragdoll (SATISFYING)
        → ⚠️ Ragdoll = PEAK Layer E: body thấy full physics response
        → Game stickman: enemy ragdoll = Layer E PERFECT → carry toàn bộ feel
      → Environment: wall crack, objects scatter, ground dent
      → Proportional: light hit = flinch. Heavy hit = send flying.

CÔNG THỨC IMPACT:
  Total Impact = Hitstop × Shake × SFX × VFX × Reaction

  → MULTIPLICATIVE, không additive:
    5 layers đều ●●● = feel CỰC MẠNH (3×3×3×3×3)
    3 layers ●●●●● + 2 layers ○ = feel THIẾU (5×5×5×0×0 = 0)
  → MỖI layer đều phải CÓ, không cần PERFECT — cần PRESENT
  → Thiếu 1 layer → toàn bộ impact GIẢM đáng kể

CHECKLIST per action:
  □ Hitstop? (frames?)
  □ Screen shake? (intensity? duration?)
  □ SFX? (pitch variation? layers?)
  □ VFX? (flash? particles? trail?)
  □ Reaction? (knockback? stagger? ragdoll?)
  → Nếu thiếu bất kỳ → thêm → test lại
```

### Trụ 3: WEIGHT / PHYSICS — "Thế Giới Có Trọng Lượng"

```
= Vật trong game CƯ XỬ đúng expectation cơ thể

Body có "internal physics model" từ sống trong thực tế:
  → Vật nặng rơi nhanh, bounce ít
  → Vật nhẹ bay xa, bounce nhiều
  → Jump có arc (parabolic), không linear
  → Landing CÓ impact (squash + SFX)

Match → body: "THẬT!" → trust game → immerse
Mismatch → body: "SAI!" → uncomfortable → disconnect

JUMP FEEL (quan trọng nhất cho platformer):
  → Coyote time: 5-8 frames sau khi rời edge VẪN CHO nhảy
    → Player CẢM "tôi bấm đúng" (dù technically đã rơi)
    → Body expect: "tôi ĐÃ ở edge → cho tôi nhảy" → game ĐỒNG Ý
  → Jump buffer: 5-8 frames TRƯỚC khi chạm đất, bấm jump VẪN REGISTER
    → Player bấm SỚM → game nhớ → chạm đất → nhảy NGAY
    → Không có → "tôi bấm rồi sao không nhảy?!" → frustrating
  → Variable jump height: giữ = nhảy cao, thả = nhảy thấp
    → Player CẢM control → body "TÔI quyết độ cao" → satisfaction
  → Jump arc: fast rise + slow fall (game feel convention ≠ real physics)
    → Real physics: symmetric arc → feel "floaty"
    → Game physics: fast up + hang + fast down → feel "snappy"
  → Landing: squat animation (2-3 frames) + dust particles + SFX
    → Confirm "đáp!" → body satisfaction → THẬT

MOVEMENT FEEL:
  → Acceleration curve: 0 → max speed trong 3-6 frames (snappy)
    → Quá nhanh (instant) → feel "twitchy"
    → Quá chậm (>10 frames) → feel "sluggish"
    → Sweet spot: 3-6 frames → "responsive nhưng có mass"
  → Deceleration: 2-4 frames stop (slight slide)
    → Instant stop → feel "robotic"
    → Too much slide → feel "on ice" → frustrating
  → Turn: snappy for action games, smooth for racing
    → Match genre expectation

CAMERA:
  → Follow player với SLIGHT lag (2-5 frames behind)
    → Camera = "observer", player = "actor" → feel "world has mass"
  → Look-ahead: camera SHIFT hướng player đang đi
    → Player thấy THÊM phía trước → feel "control", "informed"
  → Combat cam: zoom in khi action, zoom out khi overview
    → Tight = intimate. Wide = strategic.
```

### Trụ 4: RHYTHM & PACING — "Nhịp Điệu Game"

```
= Game có NHỊP → body sync vào → flow state

COMBAT RHYTHM:
  → Attack chain: light → light → heavy (nhịp 1-2-BOM)
  → Dodge: rhythmic window (dodge → wait → dodge khớp nhịp enemy attack)
  → Enemy patterns: ĐỌCĐ ĐƯỢC → counter đúng nhịp → SATISFYING
  → ⚠️ Game combat HAY = rhythm game ẩn (Bayonetta, DMC, Hades)

  Implementation:
    → Attack frames: start-up (anticipation) → active (hit) → recovery (cooldown)
    → Chain: recovery CỦA hit 1 = start-up CỦA hit 2 → SEAMLESS → feel "flow"
    → Rhythm break: heavy attack = LONG start-up → player CHỌN timing → strategic

SESSION PACING:
  → TENSION → BUILD → CLIMAX → RELEASE → REST → repeat
  → Giống nhạc: verse → chorus → bridge → chorus → outro

  Per session (30-60 phút):
    0-5 min:   Intro/safe area (low tension, orient)
    5-15 min:  Build (encounters ramp difficulty)
    15-25 min: Peak (hard encounters, boss approach)
    25-30 min: Boss fight (CLIMAX)
    30-35 min: Reward + rest (cutscene, loot, safe area)
    → Repeat hoặc natural endpoint → SAVE → quit satisfied

  ⚠️ REST POINTS QUAN TRỌNG:
    → All tension no rest = NUMBING (body adapt → stop feeling)
    → Rest = cho body RESET → next tension feel MẠNH hơn (contrast)
    → Dark Souls bonfires = rest point → LEGENDARY design vì CONTRAST:
      Danger danger danger → BONFIRE → "ah..." → danger danger → BONFIRE
      → Body cycle: stress → relief → stress → relief → ADDICTIVE RHYTHM
```

### Trụ 5: FEEDBACK CLARITY — "Biết Chuyện Gì Đang Xảy Ra"

```
= Mỗi thời điểm, player HIỂU: "đang làm gì? có effect gì?"

3 loại feedback:
  POSITIVE: "đúng rồi!" → reward sound + flash + particles
  NEGATIVE: "sai rồi!" → warning sound + red flash + screen tint
  NEUTRAL:  "đang ở đây" → ambient (footsteps, wind, environment)

Proportional feedback:
  Action nhỏ → feedback NHẸ (micro-sound, subtle flash)
  Action lớn → feedback MẠNH (explosion sound, big shake, big VFX)
  → Body calibrate: "action này QUAN TRỌNG hơn action kia" → understood

⚠️ THIẾU feedback = confusion:
  Player đánh → enemy KHÔNG phản ứng → "miss? bug? weak?" → confused → frustrated
  → MỌI action PHẢI có SOME feedback (dù miss cũng có "whoosh" sound)

⚠️ QUÁ NHIỀU feedback = noise:
  MỌI THỨ flash + ding + shake → body KHÔNG phân biệt → numb → feel MẠNH
  → Reserve STRONG feedback cho IMPORTANT moments
  → Quiet moments QUAN TRỌNG: contrast highlight big moments
```

---

## 3. Difficulty Design — Flow Zone

### 3.1 Nguyên lý: Challenge ≈ Skill → Flow

```
  ┌─────────────────────────────────────┐
  │           ANXIETY                   │
  │         (quá khó)                   │
  │   ┌─────────────────────────────┐   │
  │   │         FLOW ZONE           │   │
  │   │    Challenge ≈ Skill        │   │
  │   │    = ĐỈNH CAO experience    │   │
  │   └─────────────────────────────┘   │
  │          BOREDOM                    │
  │        (quá dễ)                     │
  └─────────────────────────────────────┘

Flow = player đang ở RANH GIỚI giữa "gần thua" và "có thể thắng"
  → Body: ACTIVATED nhưng không OVERWHELMED
  → Mind: FOCUSED nhưng không STRESSED
  → Time: "biến mất" (flow = mất nhận thức thời gian)
```

### 3.2 Difficulty Curve — 3 Phases

```
PHASE 1: TEACH (5-10% game time)
  → Introduce 1 mechanic / 1 thời điểm
  → Player gần KHÔNG THỂ chết
  → Mục đích: build FEEL cho core mechanic

  ⚠️ DẠY BẰNG GAMEPLAY, không bằng text:
    → Hố ở trước → player PHẢI nhảy → HỌC nhảy
    → Enemy yếu → player ĐẤM → HỌC combat
    → Locked door + key nearby → player TÌM key → HỌC puzzle pattern
    → Body learn NHANH hơn text (somatic > verbal encoding)

  → "Tutorial level" tốt nhất = player KHÔNG BIẾT đang tutorial
  → Super Mario 1-1 = PERFECT teach level (60+ năm vẫn benchmark)

PHASE 2: DEVELOP (70-80% game time)
  → Combine mechanics (nhảy + đánh, đánh + dodge, dodge + timing)
  → Difficulty tăng DẦN (gradient, KHÔNG bậc thang)
  → New enemy patterns → player ADAPT + IMPROVE

  Death frequency sweet spot:
    0 deaths per section → QUÁ DỄ → chán → tăng difficulty
    1-3 deaths per section → "gần được!" → TỐI ƯU → retry với hope
    5+ deaths per section → "impossible!" → frustration → giảm difficulty

  "Gần được!" = STRONGEST motivator:
    → Health bar enemy gần hết + player chết = "LẦN SAU CHẮC CHẮN!"
    → = Mastery desire APPROACHING fulfillment → dopamine → retry
    → Khác "impossible": enemy full HP + player die instantly = "KỆ" → quit

PHASE 3: MASTER (10-20% game time)
  → Endgame: TẤT CẢ mechanics combine
  → Player bây giờ GIỎI → feel POWERFUL (payoff từ Phase 2)
  → Boss cuối: test TOÀN BỘ skills → clear = "TÔI LÀM ĐƯỢC!" = PEAK feel
  → Optional: harder modes, speedrun, challenge rooms (cho CH6 Mastery players)
```

### 3.3 Death & Failure Design

```
Death NÊN là:
  ✅ LEARNING TOOL: "à, cần dodge cái đó" → informative
  ✅ NHANH reload: < 3 giây → không break flow
  ✅ Progress giữ LẠI phần lớn: checkpoint gần → không discourage
  ✅ "Almost!" feel: health bar gần → "lần sau được!" → motivate
  ✅ Clear reason: player BIẾT tại sao chết → có thể improve

Death KHÔNG NÊN là:
  ❌ Mất 1 GIỜ progress → rage quit (punishment > learning)
  ❌ Loading 30 giây → break flow → mất feel → quit
  ❌ Unclear death: "sao tôi chết??" → frustration (feedback clarity fail)
  ❌ Cheap death: unavoidable, unfair → "game SAI, không phải TÔI sai" → quit
  ❌ Permadeath KHÔNG có meta-progress → loss > learning → most players quit
```

### 3.4 Dynamic Difficulty (optional)

```
= Game TỰ adjust difficulty theo player performance (INVISIBLE)

  Player chết nhiều → game nhẹ ĐI:
    → Enemy HP giảm 5-10%
    → Enemy attack frequency giảm
    → Pickup drop rate tăng

  Player clear dễ → game khó LÊN:
    → Enemy HP tăng
    → Enemy patterns phức tạp hơn
    → Resource scarcer

  ⚠️ PHẢI INVISIBLE:
    → Player BIẾT = "game thương hại tôi?" → feel BAD
    → Player KHÔNG biết = "game vừa đúng!" → feel GOOD
    → RE4, Left 4 Dead = dynamic difficulty HIDDEN → "sao game lúc nào cũng vừa?"

  Implementation:
    → Track: death count, clear time, health remaining per section
    → Adjust: ±5-15% per parameter (subtle, không dramatic)
    → Reset: mỗi session/level mới → recalibrate
    → ⚠️ KHÔNG adjust MID-ENCOUNTER (player đang focus → thấy)
    → Adjust BETWEEN encounters (player ở transition → không thấy)
```

---

## 4. Game Loop Design — Micro / Meso / Macro

### 4.1 Cấu trúc 3 Loop

```
3 loops lồng nhau — mỗi loop SERVE 1 reward timing:

╔═══════════════════════════════════════════════════════════════╗
║  META LOOP (ngày-tuần)                                        ║
║  = Tại sao quay lại NGÀY MAI?                                ║
║  Anticipation: "lần sau sẽ thử weapon mới / chapter mới"     ║
║                                                               ║
║  ┌─────────────────────────────────────────────────────────┐  ║
║  │  MACRO LOOP (30-90 phút)                                │  ║
║  │  = 1 SESSION — Tại sao chơi tiếp TIẾNG NỮA?            │  ║
║  │  Structure: INTRO → DEVELOP → CLIMAX → RESOLVE           │  ║
║  │                                                          │  ║
║  │  ┌───────────────────────────────────────────────────┐   │  ║
║  │  │  MESO LOOP (2-5 phút)                             │   │  ║
║  │  │  = 1 ENCOUNTER — Tại sao clear ROOM NỮA?          │   │  ║
║  │  │  Structure: TENSION → BUILD → CLIMAX → REWARD      │   │  ║
║  │  │                                                    │   │  ║
║  │  │  ┌─────────────────────────────────────────────┐   │   │  ║
║  │  │  │  MICRO LOOP (< 1 giây)                      │   │   │  ║
║  │  │  │  = 1 ACTION — input → feel                  │   │   │  ║
║  │  │  │  PHẢI sướng RIÊNG NÓ                        │   │   │  ║
║  │  │  └─────────────────────────────────────────────┘   │   │  ║
║  │  └───────────────────────────────────────────────────┘   │  ║
║  └─────────────────────────────────────────────────────────┘  ║
╚═══════════════════════════════════════════════════════════════╝
```

### 4.2 Mỗi Loop Chi Tiết

```
MICRO LOOP (< 1 giây — mỗi action):
  Input → Action → Feedback → FEEL reward

  = Core mechanic loop — PHẢI sướng RIÊNG NÓ
  = Không cần context, không cần story, không cần progression
  = Player lặp 1000 lần → VẪN sướng? → PASS

  Ví dụ:
    Bấm → đấm → enemy flinch + SFX + shake → SƯỚNG
    Bấm → nhảy → arc + landing + dust → SƯỚNG
    Click → block place → snap sound + visual → SƯỚNG (Minecraft)

MESO LOOP (2-5 phút — mỗi encounter):
  Start → multiple micro loops → clear → REWARD

  Structure: TENSION (enemy appear/challenge present)
           → BUILD (fighting/solving — multiple micro loops)
           → CLIMAX (last enemy / solution moment)
           → REWARD (item, XP, door opens, safe area)

  Mỗi meso loop = mini story arc
  Kết thúc meso → natural pause point ("save?", "continue?")

  Test: player muốn "1 room nữa"? → ✅ → meso loop design ĐÚNG

MACRO LOOP (30-90 phút — mỗi session):
  Start → multiple meso loops → boss/milestone → SAVE → satisfied quit

  Structure: INTRO (5min: orient, context)
           → DEVELOP (20min: multiple meso loops, ramp)
           → CLIMAX (10min: boss fight / major challenge)
           → RESOLVE (5min: reward, cutscene, safe area)
           → ENDPOINT → save → quit → "mai chơi tiếp!"

  ⚠️ NATURAL ENDPOINT crucial:
    CÓ endpoint → player quit SATISFIED → nhớ tốt → quay lại mai
    KHÔNG endpoint → player quit GUILTY → nhớ xấu → dần bỏ

META LOOP (ngày-tuần — across sessions):
  Session end → progress saved → NEW THING available next session

  Healthy meta:
    ✅ "Vừa unlock weapon mới → mai thử!" (anticipation)
    ✅ "Chapter 3 cliffhanger → phải biết tiếp!" (narrative hook)
    ✅ "Kỹ năng đang improve → muốn practice thêm" (mastery)

  Unhealthy meta:
    ❌ "Daily login 7 ngày → mất streak!" (FOMO)
    ❌ "Limited event 24h → phải chơi NGAY!" (artificial scarcity)
    ❌ "Stamina refill 8h → phải vào check!" (timer manipulation)
```

---

## 5. Prototyping — Feel First Workflow

### 5.1 Quy trình 5 bước

```
BƯỚC 1: CORE MECHANIC PROTOTYPE (ngày 1-3)
  ────────────────────────────────────────
  → 1 screen. 1 character. 1 action.
  → Grey box / programmer art / basic shapes
  → KHÔNG có: menu, UI, progression, levels, art, story
  → CHỈ CÓ: input → action → feedback
  → Mục đích: "core action feel CÓ TIỀM NĂNG không?"

  Pass criteria: cho 3 người chơi 30 giây
    Cười / "ồ!" / muốn thử lại → PROCEED ✅
    "Ừm..." / đặt xuống → action chưa đúng → ITERATE

BƯỚC 2: FEEL TUNING (ngày 3-14) ← BƯỚC QUAN TRỌNG NHẤT
  ────────────────────────────────────────
  → Thêm 5 layers impact (hitstop, shake, SFX, VFX, reaction)
  → Tune physics (gravity, jump arc, momentum, friction)
  → Tune timing (input delay, animation speed, cancel windows)
  → MỖI NGÀY: tune → test → tune → test → tune → test
  → Micro-adjustments: "+2 frames hitstop" → test → "+1px shake" → test

  ⚠️ Dành NHIỀU NHẤT thời gian ở đây
  → Vội qua bước này = game feel tệ mãi mãi
  → "1 tuần tune feel > 1 tháng thêm content"

  TOOL CẦN BUILD TRƯỚC:
    → LIVE EDIT: thay đổi parameter → thấy NGAY (không recompile)
    → Sliders: hitstop, shake, knockback, speed, gravity, jump height,...
    → Record + replay: test → replay → adjust → replay → compare
    → ⚠️ Build TOOL này TRƯỚC khi build game → iteration nhanh 10x

BƯỚC 3: MICRO LOOP (tuần 2-3)
  ────────────────────────────────────────
  → Thêm 1 enemy (hoặc obstacle)
  → Player + enemy = core ENCOUNTER
  → Tune: enemy behavior, health, damage, patterns, reaction
  → Test: micro loop lặp 100 lần → VẪN sướng? → PROCEED

BƯỚC 4: MESO LOOP (tuần 3-5)
  ────────────────────────────────────────
  → Thêm level structure (rooms, sections, waves)
  → Pacing: tension → build → climax → reward per section
  → Test: 1 meso loop = 2-5 phút? Muốn "1 nữa"? → PROCEED

BƯỚC 5: MACRO + META (tuần 5+)
  ────────────────────────────────────────
  → Progression system, multiple levels, bosses, unlocks
  → Story elements nếu cần
  → Session structure: 30-90 phút → natural endpoint

  ⚠️ MỌI feature mới → test: "Lớp 1 feel CÒN sướng không?"
    → Feature ENHANCE feel → keep ✅
    → Feature NEUTRAL → cân nhắc (cần không?)
    → Feature PHÁ feel → remove ❌ hoặc redesign
    → FEEL là vua. Feature phục vụ feel.
```

### 5.2 Feel Tuning Parameter Sheet

```
Danh sách parameters CẦN tune (copy cho mỗi game):

CHARACTER:
  □ Move speed: ___ units/sec
  □ Acceleration: ___ frames to max
  □ Deceleration: ___ frames to stop
  □ Jump height: ___ units
  □ Jump rise time: ___ frames
  □ Jump fall multiplier: ___x gravity
  □ Coyote time: ___ frames
  □ Jump buffer: ___ frames
  □ Air control: ___%

COMBAT (nếu có):
  □ Attack startup: ___ frames
  □ Attack active: ___ frames
  □ Attack recovery: ___ frames
  □ Hitstop: ___ frames (per attack type)
  □ Screen shake: ___px, ___ frames (per attack type)
  □ Knockback: ___ units (per attack type)
  □ Cancel window: frame ___ to ___

CAMERA:
  □ Follow lag: ___ frames behind
  □ Look-ahead distance: ___ units
  □ Shake decay rate: ___%/frame
  □ Zoom range: ___x to ___x

AUDIO:
  □ Hit SFX pitch variation: ±___%
  □ Hit SFX layers: impact / reaction / environment
  □ Music volume relative to SFX: ___%
  □ Ambient presence: ___%

→ MỌI parameter = slider trong editor → tune REAL-TIME
→ MỖI parameter ghi VALUE + lý do chọn value đó
→ Compare: value trước → value sau → feel khác thế nào → WHY
```

---

## 6. Common Mistakes — Tránh

```
MISTAKE 1: "Thêm content để cứu feel tệ"
  → Feel tệ + 100 levels = 100 levels feel tệ
  → Fix feel TRƯỚC. Content chỉ AMPLIFY feel đã tốt.

MISTAKE 2: "Copy mechanics từ game hit"
  → Game hit có feel TỐT → copy mechanics KHÔNG copy feel
  → Feel = TUNING, không phải FEATURES
  → Phải TUNE riêng cho game mình → không shortcut

MISTAKE 3: "Polish cuối cùng"
  → "Làm xong hết rồi polish feel sau"
  → Thực tế: feel phải NGAY TỪ ĐẦU, polish = fine-tune
  → Nếu core feel SAI → polish không cứu được

MISTAKE 4: "Difficulty = content gate"
  → Làm khó ĐỂ player PHẢI chơi lâu hơn (stretch content)
  → Player: "game pad difficulty để kéo dài" → angry → quit
  → Difficulty phải = PLAYER GROWTH, không phải CONTENT PADDING

MISTAKE 5: "Feedback everywhere"
  → MỌI action → big SFX + big VFX + shake
  → = Noise → body numb → không phân biệt important vs trivial
  → Reserve BIG feedback cho BIG moments. Quiet for small.

MISTAKE 6: "Feel = particles + shake"
  → Thêm particles → "sao vẫn không feel?"
  → Vì THIẾU: hitstop, timing, weight, sound, reaction
  → Particles = 1/5 layers → cần TẤT CẢ 5

MISTAKE 7: "Skip prototyping"
  → "Biết rồi, cứ build full luôn"
  → 3 tháng build → feel tệ → phải rebuild
  → 3 ngày prototype → biết feel trước → save 3 tháng
```

---

## 7. Quick Reference — Per Genre

```
GENRE          │ CORE FEEL           │ PRIMARY CHANNELS   │ KEY MECHANIC
═══════════════╪═════════════════════╪════════════════════╪══════════════════
Platformer     │ Jump + Movement     │ CH1+CH5            │ Jump tuning
Fighter/Brawl  │ Hit impact + Combo  │ CH1+CH6            │ Hitstop + combo
FPS            │ Shoot + Aim         │ CH1+CH4+CH6        │ Recoil + hit confirm
RPG            │ Growth + Story      │ CH5+CH6+CH8        │ Level curve + narrative
Roguelike      │ Risk + Discovery    │ CH4+CH5+CH6        │ Permadeath + variety
Puzzle         │ "Aha!" + Clarity    │ CH5+CH6            │ Complexity curve
Cozy/Sim       │ Comfort + Routine   │ CH2+CH3+CH8        │ Gentle rhythm + social
Racing         │ Speed + Control     │ CH1+CH4            │ Drift feel + track design
Horror         │ Tension + Fear      │ CH4+CH2            │ Pacing + audio
Rhythm         │ Music + Timing      │ CH1+CH6            │ Input sync + music
Strategy       │ Plan + Outcome      │ CH5+CH6+CH7        │ Decision clarity
```

---

> *Gameplay Design — DRAFT v1.0*
> *"Feel is not a feature. Feel is the foundation."*
> *Dựa trên: Core-Principles.md + Player-Psychology.md*
