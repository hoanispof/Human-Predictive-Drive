# Game Design Core Principles

> **Mục đích:** Nguyên lý GỐC tạo game chất lượng — cho TOÀN TEAM đọc được
> **Trạng thái:** DRAFT v1.0
> **Ngày:** 2026-03-16
> **Nguyên tắc:** Principles, không phải rules. Hiểu GỐC → apply linh hoạt.

---

## 1. Tại Sao Player Chơi Game?

```
Player mở game = TÌM CẢM GIÁC mà thực tế không cho đủ:

  Muốn chiến đấu    → game cho NGAY, an toàn
  Muốn khám phá     → game cho NGAY, rẻ
  Muốn làm anh hùng → game cho NGAY, không risk
  Muốn kết nối      → game cho NGAY, từ nhà
  Muốn giỏi lên     → game cho trong GIỜ, thay vì NĂM

  = Game là ĐƯỜNG TẮT đến cảm giác thỏa mãn
  = Chi phí thấp, phần thưởng nhanh, an toàn

⚠️ Nhưng cảm giác từ game < thực tế (simulation < reality)
  → Player BIẾT là game → cần game ĐỦ TỐT để body vẫn respond
  → Game tốt = body respond DÙ BIẾT là giả
  → Game tệ = body "kệ" → chán → quit
```

---

## 2. Ba Lớp Phần Thưởng — Nền Tảng Mọi Thứ

> Đây là framework cốt lõi nhất. MỌI quyết định design đều quy về đây.

### Lớp 1: FEEL — "Cảm nhận trực tiếp"

```
= Thứ player CẢM TRONG NGƯỜI ngay khi tương tác
= KHÔNG cần hiểu game, KHÔNG cần context
= Body respond trong < 1 giây

Gồm:

  A. GAMEPLAY FEEL (quan trọng nhất):
     → Impact: đấm/bắn/nhảy → "LỰC!" (body cảm nhận sức mạnh)
     → Responsiveness: bấm → phản hồi < 50ms → "NHANH!" (body cảm nhận kiểm soát)
     → Weight: vật lý, trọng lực feel đúng → "THẬT!" (body cảm nhận coherence)
     → Juice: particles, screen shake, camera → "WOW!" (body cảm nhận kích thích)

  B. VISUAL FEEL:
     → Color harmony, contrast, readability
     → KHÔNG CẦN realistic → cần HARMONIOUS (Minecraft xấu nhưng harmonious → ok)
     → Realistic nhưng uncanny → body REJECT (creepy)

  C. AUDIO FEEL:
     → Music: mood, rhythm, cảm xúc
     → SFX: feedback mỗi action (đấm có tiếng, nhặt item có tiếng)
     → Ambient: tạo immersion (rừng có tiếng chim, cave có tiếng vọng)
     → ⚠️ Audio = 50% of feel mà đa số dev IGNORE

TEST LỚP 1:
  → Cho người CHƯA BAO GIỜ chơi → chơi 30 giây → có CƯỜI hoặc "ồ" không?
  → Nếu có → Lớp 1 đủ mạnh
  → Nếu không → fix Lớp 1 TRƯỚC KHI làm gì khác
```

### Lớp 2: PROGRESS — "Muốn tiếp tục"

```
= Thứ giữ player QUAY LẠI chơi tiếp
= Cần 1 chút thời gian để kick in (giây → phút)

Gồm:

  A. NOVELTY (Mới lạ):
     → New levels, enemies, mechanics, areas, items
     → "Level tiếp có gì?" = anticipation → drive quay lại
     → ⚠️ Novelty ALONE = scroll MXH (hấp dẫn nhưng trống rỗng)
     → Novelty phải PHỤC VỤ Lớp 1 (level mới = feel MỚI, không chỉ skin mới)

  B. MASTERY (Giỏi lên):
     → Skill curve: player GIỎI HƠN qua thời gian
     → "Lần trước chết, lần này clear!" = CẢM GIÁC MẠNH NHẤT trong Lớp 2
     → Vì mastery CÓ Lớp 1 component (body CẢM satisfaction thật khi giỏi lên)
     → Dark Souls, Celeste, game đối kháng = mastery-driven

  C. STATUS (Vị trí):
     → Rank, leaderboard, achievements, rare items
     → "Tôi top 100!" → tất cả cảm giác MẠNH hơn (amplify)
     → ⚠️ CÓ THỂ addictive nếu STATUS trở thành MỤC ĐÍCH thay vì FEEL
     → Competitive games: LoL, Valorant = status mạnh

  D. PROGRESSION (Tiến triển):
     → Level up, unlock, skill tree, gear
     → Mỗi unlock = micro-reward → drive tiếp
     → ⚠️ NGUY HIỂM nhất nếu dùng THAY Lớp 1:
       Progression + gameplay tệ = GRIND (muốn nhưng không vui = addiction pattern)
       Progression + gameplay hay = ENGAGING (muốn VÀ vui = healthy)

TEST LỚP 2:
  → TẮT hết progression → player VẪN muốn chơi?
  → Nếu có → Lớp 1 đủ, Lớp 2 chỉ bonus (HEALTHY)
  → Nếu không → game PHỤ THUỘC Lớp 2 = fragile, có thể addictive
```

### Lớp 3: MEANING — "Nhớ mãi"

```
= Thứ player MANG THEO sau khi tắt game
= Cần thời gian dài (phút → giờ → ngày)

Gồm:

  A. NARRATIVE (Câu chuyện):
     → Story tạo CONTEXT → gameplay có Ý NGHĨA
     → Giết monster without story = lặp lại
     → Giết monster TO SAVE VILLAGE = anh hùng
     → Player KHÓC khi NPC chết = deep feel (Lớp 1 qua Lớp 3)

  B. SOCIAL (Kết nối):
     → "Chơi với bạn tôi" = connection THẬT (không chỉ game mechanic)
     → Guild memories, raid memories = bonds THẬT
     → Player quit game nhưng NHỚ MÃI vì NGƯỜI, không vì game
     → = STRONGEST retention (social > content > mechanics)
     → Tại sao WoW, FFXIV, Dota2 sống 10-20 năm: COMMUNITY

  C. IDENTITY (Bản thân):
     → "Tôi là healer", "tôi là builder" = game thành MỘT PHẦN identity
     → Mạnh nhưng ⚠️: quit = mất identity → nên có ranh giới

TEST LỚP 3:
  → Player chơi xong 1 tháng → nhắc lại → MẮT SÁNG hay "ừ, game đó à"?
  → Mắt sáng → Lớp 3 strong → game "huyền thoại"
  → "Ừ" → Lớp 3 yếu → game "cũng được nhưng quên rồi"
```

### Quan hệ 3 Lớp

```
╔═══════════════════════════════════════════════════════════╗
║  Lớp 1: FEEL          "Sao chơi sướng vậy?"              ║
║  = NỀN TẢNG           Player ở lại VÌ FEEL                ║
║  = Build FIRST                                            ║
║                                                           ║
║  Lớp 2: PROGRESS      "Muốn chơi tiếp!"                  ║
║  = DRIVE              Player quay lại VÌ PROGRESS          ║
║  = Build ON TOP of Lớp 1                                  ║
║                                                           ║
║  Lớp 3: MEANING       "Game hay nhất đời tôi"             ║
║  = MEMORY             Player NHỚ MÃI VÌ MEANING           ║
║  = Build LAST (hoặc không — không phải game nào cũng cần)  ║
╚═══════════════════════════════════════════════════════════╝

PHẢI build THEO THỨ TỰ: Lớp 1 → Lớp 2 → Lớp 3
  Lớp 1 yếu + Lớp 2 mạnh = GRIND (nhiều content nhưng chơi chán)
  Lớp 1 mạnh + Lớp 2 yếu = FUN nhưng NGẮN (sướng nhưng hết nhanh)
  Lớp 1 mạnh + Lớp 2 mạnh = ENGAGING (sướng VÀ muốn tiếp)
  Lớp 1 + 2 + 3 mạnh = LEGENDARY (sướng + muốn + nhớ mãi)

⚠️ Không phải game nào cũng cần cả 3:
  Casual game: Lớp 1 đủ (Tetris, Flappy Bird, Stickman Fighter)
  Mid-core: Lớp 1 + 2 (Clash Royale, roguelikes)
  Hardcore: Lớp 1 + 2 + 3 (Zelda, Elden Ring, FFXIV)
```

---

## 3. Sáu Nguyên Lý Thiết Kế

### Nguyên lý 1: FEEL FIRST — Lớp 1 trước mọi thứ

```
"Nếu gameplay không sướng → thêm gì cũng vô ích"

Thực hiện:
  → Prototype SỚM: 1 screen, 1 mechanic → feel test
  → Tuning feel là VIỆC ĐẦU TIÊN, không phải cuối cùng
  → Đừng polish graphics trước khi feel đúng
  → Đừng thêm features trước khi core loop sướng

Ví dụ:
  ✅ Game stickman: đấm sướng + ngã phê → XẤU vẫn chơi
  ❌ Game AAA: đẹp siêu thực + combat nhàm → VIRAL rồi CHẾT

Test: "30-second test"
  → Cho người mới chơi 30 giây core mechanic
  → Cười / "ồ!" / muốn thử lại → PASS
  → "Ừm..." / đặt xuống → FAIL → fix feel trước
```

### Nguyên lý 2: PROGRESS PHỤC VỤ FEEL — Không thay thế

```
"Lớp 2 là LÝ DO để player trải nghiệm Lớp 1 THÊM, không phải THAY"

Đúng:
  → New level = new CÁCH trải nghiệm feel quen thuộc
  → Unlock weapon = feel MỚI (not just damage số)
  → Level up = KHÓA MỚI hơn → khó hơn → mastery feel MẠNH hơn

Sai:
  → Grind 100 level để unlock 1 skin → progression thay feel
  → Daily login bonus → FOMO drive, không phải feel drive
  → Gacha/lootbox → slot machine drive, không phải gameplay drive

Test: "Progression off test"
  → Tắt tất cả progression (level, unlock, achievement)
  → Player VẪN chơi? → Lớp 1 đủ mạnh ✅
  → Player quit ngay? → Game phụ thuộc Lớp 2 ⚠️ → cần fix Lớp 1
```

### Nguyên lý 3: REWARD TIMING — 3 layers đồng thời

```
"Player cần reward ở 3 timescale cùng lúc"

  < 1 giây:  Lớp 1 — mỗi input = feel (đấm → crunch, nhảy → whoosh)
  giây → phút: Lớp 2a — mỗi encounter = progress (clear room, kill boss)
  phút → giờ:  Lớp 2b — mỗi session = achievement (clear level, unlock area)
  giờ → ngày:  Lớp 3 — mỗi session cluster = meaning (story progress, skill growth)

  ⚠️ Thiếu bất kỳ layer nào → gap → player disengage:
    Thiếu < 1 giây: "chán, gameplay nhàm" → quit trong phút
    Thiếu giây-phút: "sướng tay nhưng... rồi sao?" → quit trong giờ
    Thiếu giờ-ngày: "vui nhưng không nhớ" → quit trong tuần
```

### Nguyên lý 4: DIFFICULTY = FEEL MANAGEMENT

```
"Khó vừa đủ = sướng nhất"

  Quá dễ: Lớp 1 mất (feel bị predictable → body chán)
  Quá khó: Lớp 1 mất (feel bị block → body frustrate → quit)
  Vừa đủ: Lớp 1 liên tục (challenge ≈ skill → body reward mỗi lúc → FLOW)

Flow zone:
  ┌─────────────────────────────┐
  │         QUÁ KHÓ             │
  │      (frustration)          │
  │  ┌───────────────────────┐  │
  │  │      FLOW ZONE        │  │
  │  │  Challenge ≈ Skill    │  │
  │  │  = SWEET SPOT         │  │
  │  └───────────────────────┘  │
  │         QUÁ DỄ              │
  │       (boredom)             │
  └─────────────────────────────┘

Thực hiện:
  → Difficulty tăng DẦN (không nhảy bậc)
  → Cho player THẤY giỏi lên (mastery feedback rõ ràng)
  → Death = "gần được!" (motivate) không phải "impossible" (frustrate)
  → Optional difficulty: easy cho casual, hard cho hardcore (cùng Lớp 1 feel)
```

### Nguyên lý 5: NATURAL ENDPOINTS — Chống vòng lặp vô tận

```
"Game tốt cho player DỪNG khi thỏa mãn, không giữ bằng mọi giá"

  CÓ endpoint:
    → Clear level → "nice!" → save → quit → nhớ tốt → mai chơi tiếp
    → Clear game → "wow, amazing!" → satisfied → recommend bạn bè
    → Session có cấu trúc: intro → build → climax → resolve → natural pause

  KHÔNG endpoint:
    → Infinite wave → "khi nào dừng?" → guilt khi quit
    → "Just one more" loop → 3 giờ trôi qua → trống rỗng
    → Daily login → "phải vào không mất streak" → FOMO, không phải fun

  ⚠️ "Player chơi lâu" ≠ "game hay"
    Player chơi 3 giờ + thỏa mãn + nhớ tốt > Player chơi 8 giờ + trống rỗng + guilt
    Retention metric CÓ THỂ misleading: giữ người bằng FOMO ≠ giữ bằng FEEL
```

### Nguyên lý 6: XẤU MÀ FEEL > ĐẸP MÀ EMPTY

```
"Visual fidelity KHÔNG tương quan với enjoyment.
 Feel fidelity TƯƠNG QUAN MẠNH với enjoyment."

Bằng chứng:
  Tetris (1984): pixel blocks → vẫn chơi 40 năm
  Minecraft (2011): pixel 3D → 300M copies
  Among Us (2018): MS Paint style → viral toàn cầu
  Flappy Bird (2013): 1 sprite, 1 color → hiện tượng
  Stickman fighters: hình que → vẫn chơi

  vs.

  Nhiều game AAA: photorealistic → viral rồi quên sau 2 tuần

  → "Đẹp" giúp FIRST IMPRESSION → download
  → "Feel" giữ PLAYER → retention
  → Đẹp + feel = best. Nhưng nếu phải chọn: feel > đẹp.

Budget guideline:
  70% effort → Feel (gameplay tuning, SFX, responsiveness)
  20% effort → Visual (đủ harmonious, không cần best)
  10% effort → Polish (UI, particles, edge cases)

  KHÔNG PHẢI:
  70% effort → Visual
  20% effort → Marketing
  10% effort → "Gameplay cũng ok rồi"
```

---

## 4. Ranh Giới: Engagement vs Addiction

```
ENGAGEMENT (lành mạnh):              ADDICTION (có hại):
─────────────────────────            ─────────────────────────
Chơi VÌ VUI (Lớp 1)                 Chơi VÌ SỢ MISS / SỢ TỤT (Lớp 2)
Dừng được khi cần                    KHÔNG dừng được dù muốn
Sau session: thỏa mãn               Sau session: trống rỗng + guilt
"Muốn chơi VÀ sướng khi chơi"       "Muốn chơi nhưng KHÔNG sướng"
Natural endpoints                    Infinite loops
Skill-based reward                   RNG/gacha reward
Player CHỌN quay lại                 Player BỊ BUỘC quay lại
Intrinsic: "vui quá!"               Extrinsic: "mất streak!", "daily bonus!"

Design patterns GÂY addiction (TRÁNH nếu muốn ethical):
  ❌ Variable reward schedule (gacha, lootbox = slot machine)
  ❌ FOMO mechanics (limited time, daily login streak)
  ❌ Social pressure ("bạn bạn đã chơi, bạn chưa!")
  ❌ Sunk cost exploit ("đã đầu tư X giờ, bỏ thì phí!")
  ❌ Artificial difficulty spike → IAP "giải cứu"
  ❌ Infinite scroll / autoplay / no natural pause

Design patterns TẠO engagement (DÙNG):
  ✅ Gameplay feel mạnh (Lớp 1 thật)
  ✅ Skill-based progression (mastery real)
  ✅ Natural session endpoints (clear level = pause)
  ✅ Content depth (replay vì FEEL khác, không vì FOMO)
  ✅ Optional social (có nếu muốn, không ép)
  ✅ Respect player time ("30 phút = 1 meaningful session")
```

---

## 5. Team Roles — Ai Sở Hữu Lớp Nào?

```
FEEL OWNER (Creative Director / Lead Designer):
  → Sở hữu Lớp 1 — quyết định "game feel thế nào?"
  → Tune: impact, responsiveness, weight, juice
  → Test: 30-second test, play-test liên tục
  → KHÔNG AI thay được — cần CẢM gameplay, không chỉ BIẾT
  → = Vai trò quan trọng NHẤT

ARTIST (Visual Designer):
  → Phục vụ Lớp 1 visual: color, harmony, readability
  → KHÔNG chase "đẹp nhất có thể" → chase "đẹp PHỤC VỤ feel"
  → Screen shake 10% mạnh hơn → feel tăng → artist tune visual cho match
  → Artist SERVE feel, không phải feel serve art

AUDIO (Sound Designer):
  → Phục vụ Lớp 1 audio: SFX, music, ambient
  → 50% of feel → nên invest SỚM, không phải cuối
  → Mỗi action CẦN audio feedback (không có → body "trống")
  → Music set MOOD → cho phép Lớp 3 (narrative) kick in

PROGRAMMER:
  → Implement feel: frame timing, input handling, physics
  → Performance: lag = KILL feel (< 16ms frame time)
  → Tool: build tool cho feel owner TUNE nhanh (sliders, live edit)
  → Code quality phục vụ ITERATION SPEED, không phải perfection

GAME DESIGNER:
  → Sở hữu Lớp 2: progression, difficulty curve, content pacing
  → Design Lớp 2 PHỤC VỤ Lớp 1 (không phải thay thế)
  → Balance: quá dễ vs quá khó → tìm flow zone
  → Test: "progression off test" thường xuyên

NARRATIVE DESIGNER / WRITER:
  → Sở hữu Lớp 3: story, characters, meaning
  → Tạo CONTEXT cho gameplay → "tại sao player đang làm cái này?"
  → Không phải game nào cũng cần → nhưng NẾU CÓ → game level up đáng kể

COMMUNITY / MARKETING:
  → Marketing: bring players IN (promise phải MATCH feel thật)
  → Community: build Lớp 3 social (discord, events, guilds)
  → ⚠️ Marketing promise > feel thật = player THẤT VỌNG = reviews tệ
  → Honest marketing + strong feel = sustainable growth

QUALITY GATE — Quy trình:
  1. Feel prototype → test → PASS? → tiếp
  2. Visual + Audio polish feel → test → PASS? → tiếp
  3. Lớp 2 (progression) overlay → test → Lớp 1 vẫn đủ mạnh? → tiếp
  4. Lớp 3 (narrative/social) nếu cần → test → enhance feel? → tiếp
  5. Marketing → promise MATCH reality → launch

  ⚠️ MỌI bước đều quay lại Lớp 1 test:
    "Thêm feature X → feel CÒN sướng không?"
    Nếu không → feature X phá feel → remove hoặc fix
    Feel là vua. Mọi thứ phục vụ feel.
```

---

## 6. Case Studies Ngắn

### Tetris — Pure Lớp 1 (40 năm)
```
Lớp 1: ●●●●● (block drop + line clear + speed increase = feel PERFECT)
Lớp 2: ●●○○○ (score, speed tăng — minimal nhưng đủ)
Lớp 3: ○○○○○ (no story, no social)
→ Lớp 1 ALONE sustain 40 năm
→ Chứng minh: feel > mọi thứ khác
```

### Minecraft — Lớp 1 + Creative Freedom
```
Lớp 1: ●●●●○ (mine + build + explore feel satisfying)
Lớp 2: ●●●●● (infinite novelty — world generation + crafting)
Lớp 3: ●●●●● (social: multiplayer servers. Identity: builds = "tôi")
→ Xấu nhưng TẤT CẢ 3 lớp mạnh → game lớn nhất lịch sử
```

### Dark Souls — Lớp 1 Mastery
```
Lớp 1: ●●●●● (combat weight + responsiveness + impact PERFECT)
Lớp 2: ●●●●● (mastery curve: chết → học → clear = CỰC SƯỚNG)
Lớp 3: ●●●●○ (hidden lore + community + "I beat Dark Souls" identity)
→ KHÓ nhưng FAIR → mastery feel = strongest Lớp 2
```

### Mobile Gacha Game — Lớp 2 Without Lớp 1
```
Lớp 1: ●●○○○ (gameplay repetitive, auto-battle)
Lớp 2: ●●●●● (gacha + collection + events + FOMO)
Lớp 3: ●●○○○ (waifu collection = shallow identity)
→ Revenue CAO (exploit Lớp 2) nhưng player TRỐNG RỖNG
→ "Tôi ghét game này nhưng không dừng được" = addiction, không phải engagement
→ ⚠️ Profitable ≠ Good game
```

### Stickman Fighter (game thực tế)
```
Lớp 1: ●●●●● (đấm sướng + ngã phê = pure feel)
Lớp 2: ●●○○○ (chọn level, ít progression)
Lớp 3: ○○○○○ (no story, no social)
→ Đồ họa xấu + code lởm + ADS nhiều → VẪN CHƠI
→ Vì: Lớp 1 CỰC MẠNH bù hết thiếu sót khác
→ = Proof: feel > đồ họa > marketing > content
→ Potential: thêm Lớp 2 (mastery curve, progression) + Lớp 3 (multiplayer)
  → có thể grow đáng kể MÀ KHÔNG mất Lớp 1
```

---

## 7. Checklist Nhanh — Mỗi Milestone

```
□ FEEL TEST (mỗi build):
  □ 30-second test: người mới → cười/wow?
  □ Mỗi input → audio + visual feedback < 50ms?
  □ Impact feel: đánh/bắn/nhảy CÓ "lực" không?
  □ Tắt progression → vẫn muốn chơi?

□ PROGRESS TEST (mỗi milestone):
  □ Difficulty curve: dễ → khó DẦN (không nhảy)?
  □ Mastery visible: player THẤY mình giỏi lên?
  □ Novelty: level mới = feel MỚI (không chỉ skin)?
  □ Natural endpoint: session có cấu trúc rõ ràng?

□ MEANING TEST (pre-launch):
  □ Sau 1 giờ chơi → player kể lại → có gì đáng nhớ?
  □ Social: có lý do chơi cùng nhau không?
  □ Identity: player có "tự hào" gì sau khi chơi?

□ ADDICTION CHECK (pre-launch):
  □ Có FOMO mechanics nào không? → remove hoặc soften
  □ Có variable reward / gacha / lootbox? → review necessity
  □ Player CÓ THỂ dừng tự nhiên? → endpoints rõ ràng?
  □ Promise marketing = feel thật?
```

---

## 8. Quy Tắc Vàng

```
1. FEEL IS KING — Mọi thứ phục vụ feel, không ngược lại
2. BUILD BOTTOM-UP — Lớp 1 → Lớp 2 → Lớp 3, theo thứ tự
3. TEST EARLY — 30 giây feel test quan trọng hơn 30 trang design doc
4. RESPECT PLAYER — Engagement, không phải addiction
5. UGLY + FUN > PRETTY + BORING — Đủ đẹp + cực vui > cực đẹp + tạm vui
6. LESS IS MORE — 1 mechanic hoàn hảo > 10 mechanics tạm được
```

---

## 9. File Map — Deep Dive

```
Game-Industry/
├── Core-Principles.md          ← ★ FILE NÀY — nền tảng
├── Player-Psychology.md        ← Player muốn gì? (profiles + motivations)
├── Gameplay-Design.md          ← Feel tuning, mechanics, flow design
├── Visual-Audio.md             ← Art + Sound phục vụ feel
├── Narrative-Design.md         ← Story + Characters + Meaning
├── Monetization-Ethics.md      ← Kiếm tiền ethical
├── Social-Multiplayer.md       ← Community + Multiplayer design
└── Team-Workflow.md            ← Quy trình team, roles, iteration

→ Tạo từng file KHI CẦN, không tạo trước
→ Core-Principles.md = đọc TRƯỚC MỌI THỨ
```

---

> *Game Design Core Principles — DRAFT v1.0*
> *"Feel is King. Build bottom-up. Respect your player."*
> *Dựa trên: Human Predictive Drive Framework v7.0*
