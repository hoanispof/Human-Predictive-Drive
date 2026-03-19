# Team Workflow — Casual Game Studio

> **Mục đích:** Quy trình làm game cho studio casual. Tổng quát cho 1-50 người.
> **Đọc trước:** Core-Principles.md, Player-Psychology.md
> **Nguyên tắc:** Nhanh, linh hoạt, quality focus. Process TỐI THIỂU, output TỐI ĐA.

---

## 1. Studio Structure

### 1.1 Mô hình: Nhiều game song song, nhóm nhỏ

```
Casual game ≠ AAA:
  AAA:    1 game, 100+ người, 3-5 năm
  Casual: NHIỀU game SONG SONG, mỗi game 3-6 người, 1-6 tháng

Studio 20 người = 4-5 game song song
Studio 10 người = 2-3 game song song
Studio 3 người  = 1 game tại 1 thời điểm

Nhóm LINH HOẠT:
  → Xong game A → tách nhóm → ghép nhóm mới cho game E
  → Một số roles SHARED across games (sound, anim, QA)
  → Mỗi nhóm = micro-team, tự quản, ít dependency
```

### 1.2 Roles trong nhóm 3-6 người

```
CORE TEAM (mỗi game CẦN):

  ★ FEEL OWNER (1 người — quan trọng NHẤT)
    Chịu trách nhiệm: game feel ĐÚNG
    Làm gì:
      → Quyết định: "mechanic này feel sướng chưa?"
      → Chơi game LIÊN TỤC — body evaluate
      → Direct coder/artist: "tune thế nào cho đúng feel"
      → KHÔNG cần code giỏi — cần CẢM GIÁC game giỏi
    Ai có thể là Feel Owner:
      → Game designer có experience
      → Lead programmer có game sense
      → BẤT KỲ AI biết "feel đúng/sai" khi chơi
    ⚠️ Rule: Mỗi game PHẢI có 1 Feel Owner clear.
       Không rõ ai = game CHẮC CHẮN fail.

  CODER (1-2 người)
    Chịu trách nhiệm: implement + iteration nhanh
    Làm gì:
      → Code mechanics, systems, UI
      → Build live edit tools (sliders, hot reload) cho feel tuning
      → PHỤC VỤ Feel Owner: "thêm 2 frames hitstop" → làm ngay
    Ưu tiên: code CHẠY > code ĐẸP
      → Casual game: ship trong tháng, không maintain 5 năm
      → Refactor KHI CẦN, không refactor vì "nên"

  ARTIST (1-2 người)
    Chịu trách nhiệm: visual serve gameplay
    Làm gì:
      → Character, environment, UI, VFX
      → ART PHỤC VỤ FEEL, không phải showcase kỹ năng
    Ưu tiên: CLEAR > DETAILED
      → Player cần ĐỌNG nhanh: "đây là enemy, đây là item, đây là danger"
      → Casual art ĐẸP = harmonious, readable, consistent style
      → KHÔNG cần realistic — cần PHONG CÁCH nhất quán

SHARED (across games — lịch rõ ràng):

  SOUND (1 người cho 2-3 games)
    → SFX: impact, ambient, UI feedback
    → Music: mood, loop, transition
    → ⚠️ Sound = 50% of feel → bắt đầu SONG SONG với prototype, không để cuối
    → Schedule: calendar BLOCK rõ "tuần 1-2: game A, tuần 3: game B"

  ANIMATOR (1 người cho 2-3 games)
    → Character anim, VFX anim, UI motion
    → Casual: fewer frames but SNAPPY > many frames but slow
    → Anim serve feel: "attack frame 1-3 phải NHANH, impact frame 4"

  QA/TESTER (1-2 cho toàn studio)
    → Test FEEL trước, test bugs sau
    → Ideal tester: người CHƠI NHIỀU game → body calibrated
    → QA KHÔNG chỉ "tìm bug" → QA = "body check feel liên tục"
    → Mỗi tuần: chơi mỗi game 15 phút → báo cáo feel

OPTIONAL (khi studio lớn hơn):
  UA/Marketing (1-2 cho studio): user acquisition, store optimization
  Producer (1 cho studio): schedule, resource allocation, kill decisions
  Analytics (1 cho studio): metrics, A/B test, retention analysis
```

---

## 2. Game Lifecycle — Từ Ý Tưởng Tới Ship

### Phase 0: Concept (1-3 ngày)

```
Ai:     Feel Owner + 1 người brainstorm
Input:  Ý tưởng core mechanic
Do:     Trả lời 1 câu: "Player sẽ CẢM GÌ khi chơi?"
        → KHÔNG phải "game về gì" → mà "FEEL gì?"

        Ví dụ:
          ❌ "Game về stickman đánh nhau" (mô tả, không feel)
          ✅ "Player cảm giác ĐẤM MẠNH, enemy ngã PHÊ" (feel target)

          ❌ "Game puzzle xếp hình" (mô tả)
          ✅ "Player cảm giác THÔNG MINH khi chain combo dài" (feel target)

Output: 1 câu feel target + core mechanic sketch (có thể vẽ tay)
Gate:   Feel Owner + 1 người: "feel này HẤP DẪN?"
          YES → Phase 1
          NO  → concept khác (cost: 1-3 ngày — chấp nhận được)
```

### Phase 1: Feel Prototype (1-2 tuần)

```
Ai:     Feel Owner + 1 Coder
Input:  Core mechanic + feel target
Do:
  → 1 screen. 1 character. 1 mechanic. Grey box.
  → KHÔNG có: menu, UI, level, art, sound, progression
  → CHỈ CÓ: input → action → feedback
  → Focus 100%: tune feel
    - Input response (< 50ms)
    - Impact feedback (hitstop + shake + SFX placeholder + VFX)
    - Weight/physics
    - Rhythm
  → Build LIVE EDIT TOOLS ngày đầu:
    Sliders cho: hitstop, shake, speed, gravity, knockback
    → Iteration 10x nhanh hơn hardcode

Output: 30 giây gameplay loop — playable prototype
Gate:   ★ QUAN TRỌNG NHẤT TRONG TOÀN BỘ QUY TRÌNH ★

        FEEL TEST:
          Cho 3-5 người NGOÀI team chơi 30 giây. KHÔNG giải thích gì.
          Chỉ quan sát REACTION:

          😄 Cười / "nữa đi!" / body react (nghiêng người, tay siết)
            → ✅ PASS — feel ĐÚNG

          😐 "Ừm..." / thờ ơ / đặt điện thoại xuống
            → ❌ TUNE thêm — feel CHƯA đúng

          Tune → test lại. Max 2 vòng tune (1 tuần mỗi vòng).
          Sau 2 tuần: pass hoặc KILL. Không negotiate.

⚠️ Rule cứng: 2 tuần max cho Phase 1.
   Feel chưa đúng sau 2 tuần = MECHANIC sai (không phải tuning sai)
   → Kill concept → Phase 0 mới
   Cost: 2 tuần × 2 người = chấp nhận được
   → KILL SỚM = tiết kiệm cho studio
```

### Phase 2: Content Prototype (2-4 tuần)

```
Ai:     Full core team (3-4 người) + shared roles bắt đầu
Input:  Feel prototype đã PASS
Do:
  → 5-10 levels, enemy variety, basic progression
  → Art direction (placeholder → style guide, chưa cần final art)
  → Sound prototype: SFX quan trọng (impact, UI), music draft
  → Difficulty curve: teach → develop → mini-boss

  ⚠️ RULE VÀNG: Mỗi feature mới → test: "feel CÒN sướng?"
     Feature phá feel → REMOVE hoặc redesign
     → Feel > Feature. KHÔNG compromise feel cho feature.

Output: 10 phút gameplay — playable start-to-"end"
Gate:
  Option A (mobile): CPI test
    → Chạy ads test → Cost Per Install < $0.30-0.50? → market interest
    → CPI cao → concept khó attract → xem xét kill hoặc pivot

  Option B (tất cả): Internal play session
    → Team + 5-10 người ngoài chơi 30 phút
    → "Chơi lần 2?" "Chơi lần 3?"
    → YES → retention ok → Phase 3
    → NO → tune hoặc KILL

  Cost nếu kill: 1 tháng × 3-4 người = đáng kể nhưng chấp nhận được
  → TỐT HƠN: kill ở Phase 2 > ship game tệ ở Phase 4
```

### Phase 3: Production (4-12 tuần)

```
Ai:     Full team (4-6 người)
Input:  Content prototype đã PASS
Do:
  → Full content: all levels, final art, final sound, UI polish
  → Monetization: ads integration, IAP nếu có
  → Performance: FPS stable, loading time, memory
  → Bug fixing, edge cases
  → Store assets: icon, screenshots, description

  ⚠️ Weekly feel check: mỗi tuần CHƠI game → "vẫn sướng?"
  ⚠️ Feature freeze: điểm nào đó → KHÔNG thêm feature mới
     → Chỉ fix + polish
  ⚠️ Feature creep là KẺ THÙ:
     "Thêm shop!"  → Test feel impact trước
     "Thêm PvP!"   → Có đủ resource không? Feel có bị pha loãng?
     "Thêm story!"  → Casual player có cần story không?
     → Default: KHÔNG thêm. Chỉ thêm nếu pass feel test.

Output: Shippable game
Gate:   Soft launch (limited market — 1-2 quốc gia nhỏ)
  Metrics target (mobile casual):
    D1 retention > 40%
    D7 retention > 15%
    Session time > 5 phút average
    Ad revenue per DAU đủ cover UA cost

    PASS → Phase 4 (global launch)
    FAIL → tune (max 2-4 tuần) → retest → pass hoặc KILL
```

### Phase 4: Scale + Live (ongoing)

```
Ai:     Core team (giảm) + marketing
Input:  Soft launch PASS
Do:
  → Global launch
  → UA: marketing, user acquisition
  → Live ops (nếu F2P): events, content updates, seasonal
  → Monitor: retention, revenue, player feedback
  → ⚠️ KHÔNG phá feel vì metrics:
     "Thêm interstitial ads" → test feel impact → nếu feel giảm → ĐỪNG
     "Force tutorial" → test → nếu player bỏ → ĐỪNG
     Revenue quan trọng NHƯNG feel damage = long-term revenue GIẢM

  Khi game STABLE:
    → Core team giảm còn 1-2 (maintenance)
    → Còn lại → ghép nhóm mới → game tiếp
    → Feel Owner có thể chuyển sang game mới hoặc ở lại monitor

Output: Revenue + player satisfaction
```

---

## 3. Kill Criteria — Khi Nào Dừng Game

```
Casual game = volume business:
  10 prototypes → 3 pass feel → 1 thành công trên market
  → KILL NHANH = tiết kiệm resource = KỸ NĂNG QUAN TRỌNG NHẤT

╔══════════╦═════════════════════════════╦══════════════╦════════════╗
║ Phase    ║ Kill trigger                ║ Cost         ║ Pain level ║
╠══════════╬═════════════════════════════╬══════════════╬════════════╣
║ Phase 0  ║ Feel target không clear     ║ 1-3 ngày     ║ Không đau  ║
║ (concept)║ Quá giống game có sẵn       ║ × 2 người    ║            ║
╠══════════╬═════════════════════════════╬══════════════╬════════════╣
║ Phase 1  ║ Feel test FAIL 2 lần       ║ 1-2 tuần     ║ Hơi tiếc   ║
║ (feel)   ║ 2 tuần mà feel chưa đúng   ║ × 2 người    ║            ║
╠══════════╬═════════════════════════════╬══════════════╬════════════╣
║ Phase 2  ║ CPI quá cao                ║ 1 tháng      ║ Đáng kể   ║
║ (content)║ Retention test fail        ║ × 3-4 người  ║            ║
║          ║ Team không enjoy chơi       ║              ║            ║
╠══════════╬═════════════════════════════╬══════════════╬════════════╣
║ Phase 3  ║ Soft launch metrics fail   ║ 2-3 tháng    ║ Đau       ║
║ (prod)   ║ Tune không improve          ║ × 4-6 người  ║ TRÁNH     ║
║          ║ → Nên kill SỚM hơn          ║              ║ bằng kill ║
║          ║                             ║              ║ sớm hơn   ║
╚══════════╩═════════════════════════════╩══════════════╩════════════╝

NGUYÊN TẮC KILL:
  → Kill KHÔNG phải thất bại → Kill = LEARNED + resource freed
  → Mỗi kill = data: "mechanic X feel sai vì Y" → tránh lần sau
  → Studio thành công = kill 7/10 nhanh + ship 3/10 CHẤT LƯỢNG
  → Kill game TỆ > ship game TỆ (ship tệ = damage brand + team morale)

⚠️ SUNK COST FALLACY:
  "Đã làm 3 tháng, phải ship!" → SAI
  → 3 tháng ĐÃ MẤT bất kể ship hay không
  → Ship game tệ = MẤT THÊM: marketing cost + brand damage + team demoralize
  → Kill = MẤT ÍT HƠN: chỉ mất thời gian đã qua, FREE resource cho game tiếp

⚠️ "TEAM KHÔNG ENJOY CHỢ" = STRONG KILL SIGNAL:
  → Team chơi game mình mà CHÁN → player CHẮC CHẮN chán
  → Body check: nếu body MÌNH không reward → body PLAYER cũng không
  → Exception: game target audience KHÁC team (ví dụ: team nam làm game cho trẻ em)
    → Cần tester từ target audience, không dùng team body check
```

---

## 4. Ghép Nhóm — Team Chemistry

```
Sau khi game xong (ship hoặc kill) → nhóm TÁCH → ghép lại.

NGUYÊN TẮC:

  1. Feel Owner CHỌN TRƯỚC
     → Feel Owner = core. Game mới cần Feel Owner trước.
     → Feel Owner chọn (hoặc được assign) game concept
     → Feel Owner request coder/artist phù hợp

  2. Coder-Feel Owner CHEMISTRY là ưu tiên #1
     → Coder phải HIỂU Feel Owner muốn gì (thường không nói rõ được)
     → "Tune thêm chút" → coder BIẾT "chút" = bao nhiêu
     → Pair tốt: GIỮ pair qua nhiều games
     → Pair tệ: ĐỔI — chemistry > individual skill

  3. Người MUỐN > Người RẢNH
     → "Ai muốn làm game racing?" → volunteer > assign
     → Muốn = desire match → body reward → output tốt hơn
     → Bị assign nhưng không muốn → output kém → game kém

  4. ROTATE có chủ đích (mỗi 2-3 games)
     → Cùng pair mãi → habituate → fresh perspective giảm
     → Đổi pair → knowledge cross-pollinate → studio LEVEL UP
     → NHƯNG: đừng đổi GIỮA game → disruptive

  5. Shared roles: SCHEDULE RÕ
     → Sound cho 3 games: calendar BLOCK
     → "Tuần 1-2: game A SFX. Tuần 3: game B music."
     → KHÔNG: "khi nào rảnh thì làm" → bottleneck cho MỌI game
```

---

## 5. Communication — Ít nhưng đủ

### 5.1 Per Game (nhóm 3-6 người)

```
DAILY (< 5 phút, ASYNC — Discord/Slack):
  Mỗi người ghi:
    "Hôm qua: [xong gì]
     Hôm nay: [làm gì]
     Blocked: [cần gì]"
  → Không cần meeting. Text đủ. Reply nếu blocked.
  → ⚠️ 5 phút MAX viết. Viết dài = lãng phí.

WEEKLY (30 phút, SYNC — gặp hoặc call):
  Agenda cố định:
    1. CHƠI game (5 phút) — feel check: "đang sướng không?"
    2. Blocker review (10 phút) — ai stuck? cần gì?
    3. Tuần này focus (10 phút) — priority rõ ràng
    4. Open (5 phút) — ai có ý gì?
  → ⚠️ 30 phút MAX. Quá 30 phút = scope problem.
  → NẾU quá 30 phút → break out meeting riêng cho topic cụ thể

AD-HOC (bất kỳ lúc nào):
  → Feel Owner thấy vấn đề → message ngay → fix ngay
  → "Hitstop hơi dài, giảm 1 frame" → coder fix → test → 15 phút
  → KHÔNG đợi meeting → casual game = SPEED matters
```

### 5.2 Studio-wide

```
BI-WEEKLY (30 phút, toàn studio):
  → Mỗi game: 3 phút update ("đang Phase mấy, kết quả gì")
  → Cross-learning: "game A phát hiện: enemy ragdoll nên dùng physics X"
  → Resource planning: ai rảnh tuần tới? game nào cần thêm người?
  → ⚠️ 30 phút cho CẢ studio. Nếu 5 games × 3 phút = 15 phút update + 15 phút discussion

MONTHLY (1 giờ, studio retrospective):
  → Games shipped/killed tháng này: learned gì?
  → Metrics review: game nào đang tốt? game nào cần tune?
  → Process review: quy trình có cần sửa?
  → ⚠️ Retrospective PHẢI có → không có = lặp lại sai lầm
```

### 5.3 Tool Stack

```
ĐỪNG dùng:                    DÙNG:
Jira (overkill)               Trello/Notion (simple board)
Confluence (overkill)          Google Docs/Notion (nhẹ)
Formal agile ceremonies        Lean: daily text + weekly 30min
Email (chậm)                   Discord/Slack (real-time)
Shared drive phức tạp          Google Drive đơn giản

Per game:
  → 1 Discord channel (communication)
  → 1 Trello board: Todo | Doing | Done (task tracking)
  → 1 Git repo (code + assets)
  → 1 Google Drive folder (docs, art source, builds)

Studio-wide:
  → 1 Discord server (channels per game + #general + #shipped + #killed)
  → 1 Notion/Doc: studio metrics, game status overview
  → Build system: auto-build on push → share APK/build qua Discord
```

---

## 6. Knowledge Transfer — Mọi Người Đọc Gì

```
ONBOARDING người mới (3 ngày):
  Ngày 1: Đọc Core-Principles.md + Team-Workflow.md (FILE NÀY)
  Ngày 2: Chơi 3 game studio đã ship → CẢM how studio makes games
  Ngày 3: Ghép vào team → observe → bắt đầu contribute
  → ⚠️ 3 NGÀY, không phải 3 tuần
  → Casual game = learn by DOING, không learn by reading

READING LIST theo role:

  Mọi người (bắt buộc):
    → Core-Principles.md — nền tảng
    → Player-Psychology.md — hiểu player
    → Team-Workflow.md — quy trình (file này)

  Feel Owner (bắt buộc):
    → Gameplay-Design.md — feel tuning, mechanics, loops
    → Player-Psychology.md deep read — 8 channels, profiles

  Coder (khuyên đọc):
    → Gameplay-Design.md §5 (Prototyping workflow)
    → Gameplay-Design.md §2 (Feel implementation)

  Artist (khi file sẵn sàng):
    → Visual-Audio.md — art serve feel, style guide principles

  Sound (khi file sẵn sàng):
    → Visual-Audio.md — SFX serve feel, audio feedback design

KNOWLEDGE SHARING liên tục:
  → #til (today-I-learned) channel trong Discord
  → Mỗi khi phát hiện gì hay: post 1-2 câu + screenshot/video
  → "Thêm camera lerp 0.1 → feel smooth hơn NHIỀU" [video]
  → → Studio accumulated knowledge → mọi game sau TỐT HƠN
```

---

## 7. Quality Gates — Checklist Per Phase

```
PHASE 0 → 1 GATE:
  □ Feel target: 1 câu mô tả CẢM GÌ (không phải game về gì)
  □ Core mechanic: sketch/mô tả rõ ràng
  □ Feel Owner assigned
  □ Coder assigned

PHASE 1 → 2 GATE: ★ CRITICAL ★
  □ Feel test: 3-5 người ngoài team đã chơi
  □ Reaction: TÍCH CỰC (cười, muốn chơi thêm, body react)
  □ Core feel: input response < 50ms
  □ Impact feedback: ít nhất 3/5 layers (hitstop, shake, SFX, VFX, reaction)
  □ Time: < 2 tuần từ start

PHASE 2 → 3 GATE:
  □ 10 phút gameplay playable
  □ Difficulty curve: dễ → khó dần (không spike)
  □ Art direction: consistent style (chưa cần final)
  □ Sound: SFX cho core actions (impact, UI, ambient)
  □ Internal test: 5+ người chơi 2+ lần
  □ CPI test pass (nếu mobile)
  □ Team vẫn enjoy chơi

PHASE 3 → 4 GATE:
  □ All content complete
  □ Bug count: 0 critical, < 5 major
  □ Performance: stable FPS, < 3s load time
  □ Monetization integrated + tested
  □ Store assets ready
  □ Soft launch: D1 > 40%, D7 > 15%
  □ Feel check FINAL: "game ĐANG sướng?" → YES

POST-SHIP (monthly):
  □ Metrics stable hoặc growing
  □ Player reviews: sentiment check
  □ Revenue covers UA cost
  □ Team morale: "proud of this game?" → YES
```

---

## 8. Anti-Patterns — Tránh

```
❌ "Thêm feature sẽ cứu game"
   → Feature KHÔNG cứu feel tệ. Fix feel trước.

❌ "Ship rồi fix sau"
   → First impression = chỉ có 1 lần. Ship tệ = player không quay lại.

❌ "Đã làm 3 tháng, phải ship"
   → Sunk cost. Kill game tệ > ship game tệ.

❌ "Mọi người đều là Feel Owner"
   → Không ai quyết = không ai chịu trách nhiệm = feel trôi.
   → 1 Feel Owner clear. Người khác GÓP Ý, Feel Owner QUYẾT.

❌ "Sound làm cuối"
   → Sound = 50% feel. Để cuối = 50% feel thiếu suốt process.
   → Sound prototype SONG SONG Phase 1-2.

❌ "Art phải đẹp trước"
   → Art đẹp + feel tệ = download cao + uninstall cao.
   → Feel đúng + art vừa = download vừa + retention cao.

❌ "Họp nhiều = team aligned"
   → Họp nhiều = DRAIN PFC = code/art ÍT hơn = game CHẬM hơn.
   → Async text + weekly 30min = ĐỦ.

❌ "Copy game trending"
   → Copy mechanic MÀ KHÔNG hiểu FEEL = fail.
   → Hiểu TẠI SAO game trending feel sướng → apply NGUYÊN LÝ, không copy features.

❌ "Metric quyết định tất cả"
   → Metric = feedback. Feel = foundation.
   → Metric xấu + feel tốt = tune monetization/UA, game CÓ THỂ cứu.
   → Metric xấu + feel tệ = kill.
```

---

## 9. Templates

### 9.1 Game Concept (1 trang)

```
Tên game:       _______________
Feel target:    "Player cảm giác _____ khi _____"
Core mechanic:  [1-2 câu mô tả]
Primary channels (Player-Psychology.md):
  CH___: _________ (primary)
  CH___: _________ (secondary)
Target audience: [ai sẽ THÍCH feel này?]
Reference games: [1-3 game có feel TƯƠNG TỰ]
Feel Owner:     _______________
Coder:          _______________
```

### 9.2 Weekly Meeting Agenda

```
Game: _________ | Phase: ___ | Tuần: ___

1. PLAY (5 min): chơi build mới → feel check
   Feel status: [đang sướng / cần tune / có vấn đề]

2. BLOCKERS (10 min):
   [Ai] blocked bởi [gì] → cần [gì] từ [ai]

3. THIS WEEK (10 min):
   Priority 1: __________
   Priority 2: __________
   Priority 3: __________

4. OPEN (5 min):
   Notes: _______________
```

---

> *Team Workflow — Casual Game Studio*
> *Nhanh, linh hoạt, quality focus.*
> *Feel trước, feature sau. Kill nhanh, ship chất lượng.*
