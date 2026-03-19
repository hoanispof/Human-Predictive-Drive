# Player Psychology — Player Muốn Gì?

> **Mục đích:** Hiểu player THẬT SỰ muốn gì → design ĐÚNG THỨ
> **Trạng thái:** DRAFT v1.0
> **Ngày:** 2026-03-16
> **Prerequisite:** Đọc Core-Principles.md trước
> **Nguyên tắc:** Player KHÔNG phải "types" — player là MIX of desires

---

## 1. Frameworks Hiện Có — Tốt Nhưng Chưa Đủ

```
Bartle (1996): Achiever, Explorer, Socializer, Killer
  → Tốt cho MUD/MMO. Quá đơn giản cho modern games.
  → "Killer" = thích PvP → nhưng TẠI SAO? Không trả lời.

Quantic Foundry: Action, Social, Mastery, Achievement, Immersion, Creativity
  → Tốt hơn Bartle. Data-driven. Nhưng vẫn = categories.
  → Player có thể Mastery CAO + Social CAO → profile KHÔNG fit 1 label.

Self-Determination Theory (SDT): Autonomy, Competence, Relatedness
  → Academic robust. Nhưng quá abstract cho design decisions.
  → "Player cần autonomy" → ok, nhưng CỤ THỂ làm gì?

VẤN ĐỀ CHUNG:
  → Phân loại player thành TYPES → oversimplify
  → Cùng "type" nhưng KHÁC lý do → cần design KHÁC
  → Cùng player, khác LÚC → khác "type" → model không capture
```

### Approach mới: 8 Desire Channels

```
Thay vì phân loại player → mô tả player bằng DESIRE PROFILE:
  = 8 channels, mỗi player = MIX riêng (0-5 mỗi channel)
  = Cùng player có thể KHÁC profile theo thời điểm
  = KHÔNG có types — có PROFILES

8 channels chia 3 nhóm (map với 3 Lớp trong Core-Principles):
  FEEL channels (Lớp 1):     Impact · Beauty · Comfort · Thrill
  PROGRESS channels (Lớp 2): Discovery · Mastery · Collection
  MEANING channels (Lớp 3):  Connection
```

---

## 2. FEEL Channels — Cảm Nhận Trực Tiếp (Lớp 1)

### CH1: IMPACT — "Tôi muốn cảm nhận SỨC MẠNH"

```
Desire: body cảm nhận LỰC — đánh, bắn, nổ, phá hủy, speed
  → Bàn tay grip controller mạnh hơn. Hít vào. Cười.
  → = Primal satisfaction từ "tôi TÁC ĐỘNG lên thế giới"

Design cần:
  → Screen shake (proportional to impact)
  → SFX: bass hit, crunch, explosion (audio feedback NGAY)
  → Animation: weight, follow-through, enemy react (body confirms impact)
  → Physics: ragdoll, destruction, particles (world RESPONDS)
  → Input → Output < 50ms (body feels IN CONTROL)

Player Impact cao:
  → Chơi: FPS, fighting, hack&slash, racing
  → Test game bằng: "đánh/bắn có SƯỚNG không?"
  → Bỏ game nếu: combat feel "bông" (no weight), "trôi" (no impact)
  → Ở lại nếu: mỗi hit → body "BỒM!" → satisfied

Player Impact thấp:
  → Ok với auto-battle, turn-based, point & click
  → Impact không phải priority → design cho channels khác

Ví dụ benchmark:
  Impact●●●●●: DOOM Eternal, Devil May Cry, game stickman fighter
  Impact●●●○○: Zelda, Minecraft (có nhưng không primary)
  Impact●○○○○: Animal Crossing, Stardew (gần không có)
```

### CH2: BEAUTY — "Tôi muốn cảm nhận VẺ ĐẸP"

```
Desire: body cảm nhận aesthetic pleasure — visual, audio, atmosphere
  → Mắt mở to. Thở chậm. "Wow, đẹp quá..."
  → = Thưởng thức nghệ thuật qua interactive medium

Design cần:
  → Art direction NHẤT QUÁN (style > fidelity)
  → Color palette CÓ CHỦ ĐÍCH (mood, readability, harmony)
  → Music ĐÚNG mood (enhance không overwhelm)
  → Environmental storytelling (thế giới CÓ ĐỜI SỐNG riêng)
  → Moments of AWE: đỉnh núi, sunset, vista reveal

Player Beauty cao:
  → Screenshot mọi góc. Walk around ngắm. Tắt HUD.
  → Đánh giá game BẰNG trailer aesthetic TRƯỚC gameplay
  → Chịu gameplay vừa NẾU đẹp (Journey, Gris = gameplay đơn giản + beauty)

Player Beauty thấp:
  → "Graphics doesn't matter" = THẬT SỰ (với họ)
  → Minecraft, Dwarf Fortress, ASCII roguelike = ok
  → Design cho channels khác, visual = minimum readable

⚠️ BEAUTY ≠ REALISM:
  → Realistic nhưng uncanny = body REJECT
  → Stylized nhưng harmonious = body ACCEPT
  → Budget thấp: chọn STYLE rõ > chọn realistic nửa vời
```

### CH3: COMFORT — "Tôi muốn cảm nhận AN TOÀN, thoải mái"

```
Desire: body cảm nhận warm, safe, nurturing — thư giãn
  → Vai thả lỏng. Thở đều. Miệng hơi cười.
  → = "Tổ ấm" trong game — nơi KHÔNG CÓ THREAT

Design cần:
  → Predictable: player biết expect gì (không jump scare, không sudden death)
  → Nurturing: trồng cây, nuôi thú, nấu ăn, xây nhà
  → Routine: daily cycle, seasonal cycle, repeatable actions
  → Gentle feedback: soft sounds, warm colors, rounded shapes
  → NO FAIL STATE hoặc fail = nhẹ (mất 1 ít, không mất tất cả)

Player Comfort cao:
  → Chơi: Stardew Valley, Animal Crossing, Cozy Grove, Spiritfarer
  → Chơi ĐỂ THƯ GIÃN, không phải để challenge
  → Tránh: horror, permadeath, competitive, time pressure
  → "Game = ngôi nhà thứ 2" — nơi an toàn

Player Comfort thấp:
  → "Boring, cần ACTION!" = comfort không register
  → Predictable = chán (cần CH4 Thrill thay vì CH3 Comfort)

⚠️ COMFORT ĐANG GROW:
  → Cozy game = fastest growing genre (~2020+)
  → Burnout xã hội tăng → desire comfort tăng → market RỘNG
  → Underserved: nhiều dev chase "hard" games, ít dev chase "warm" games
```

### CH4: THRILL — "Tôi muốn cảm nhận KÍCH THÍCH, nguy hiểm"

```
Desire: body cảm nhận adrenaline — tim đập, palms sweat, edge of seat
  → Ngón tay siết. Nín thở. Jump scare → la hét → CƯỜI
  → = Rollercoaster trong game — nguy hiểm giả, kích thích thật

Design cần:
  → Uncertainty: KHÔNG BIẾT sắp xảy ra gì
  → High stakes: mất NHIỀU nếu fail (permadeath, rank loss)
  → Tension build: slow → build → CLIMAX → release
  → Audio: heartbeat, silence before jump, sudden loud
  → Near-death moments: "SUÝT CHẾT!" = peak thrill
  → Scarcity: limited resources, limited lives, limited time

Player Thrill cao:
  → Chơi: horror, battle royale, roguelike permadeath, speedrun
  → MUỐN gần chết → "clutch moment" = ĐỈNH CAO experience
  → Seek: adrenaline → body respond → "ALIVE!"
  → Chán nếu: quá safe, quá dễ đoán

Player Thrill thấp:
  → Tránh: horror, permadeath, competitive ranked
  → "Stress game = stress thật" → không vui → quit

⚠️ THRILL ≠ DIFFICULTY:
  → Khó + fair = mastery (CH6). Khó + unfair = frustrating.
  → Thrill = UNCERTAINTY + STAKES, không chỉ "khó"
  → Easy game CÓ THỂ thrilling (Among Us = dễ + thrilling vì social uncertainty)
```

---

## 3. PROGRESS Channels — Muốn Tiếp Tục (Lớp 2)

### CH5: DISCOVERY — "Tôi muốn TÌM cái mới"

```
Desire: "có gì ở đằng sau góc kia?" — anticipation + reveal
  → Mắt mở to. Lean forward. "Ooh, what's that?"
  → = Tò mò được thỏa mãn liên tục

Design cần:
  → World variety: mỗi area KHÁC nhau (visual, mechanic, enemy, music)
  → Secrets: hidden rooms, easter eggs, optional paths
  → Fog of war: chưa explore = mystery → explore = reveal → satisfy
  → Mechanics unfold: game DẠY mechanic mới qua GAMEPLAY, không qua tutorial
  → Surprises: subvert expectation (tưởng A hóa B → "ồ!")

Player Discovery cao:
  → Mở MỌI GÓC map. Tìm MỌI secret. Thử MỌI path.
  → Ignore main quest → explore side areas
  → "Map còn chỗ tối → PHẢI ĐI"

Player Discovery thấp:
  → Follow marker, skip exploration, "chỉ cần main quest"
  → Discovery = "lạc đường" → frustrating

⚠️ DISCOVERY HABITUATE:
  → Secret lần 1 = wow. Secret lần 10 = expected.
  → CẦN variety: mỗi secret KHÁC loại (item, lore, mechanic, visual)
  → CẦN pacing: không quá dày (overwhelm) không quá thưa (boring between)
```

### CH6: MASTERY — "Tôi muốn GIỎI LÊN"

```
Desire: "lần trước thua, lần này THẮNG" — skill growth THẤY ĐƯỢC
  → Nắm tay. "YES!" Gật đầu. Body respond satisfaction THẬT.
  → = Cảm giác MỌI NGƯỜI muốn nhưng thực tế khó có:
    Thực tế: giỏi lên mất NĂM. Game: giỏi lên trong GIỜ.

Design cần:
  → Fair difficulty: thua vì PLAYER SAI, không vì GAME không fair
  → Clear feedback: player BIẾT sai ở đâu → sửa được → giỏi hơn
  → Skill ceiling CAO: luôn có thể giỏi HƠN (không cap nhanh)
  → Practice pays off: lặp lại = tốt hơn (measurable improvement)
  → "Almost!" moments: gần thắng = motivate HƠN thắng dễ

Player Mastery cao:
  → Replay boss 50 lần, enjoy CẢ KHI THUA
  → "Thua vì mình chưa giỏi, không phải game sai" = accept + improve
  → Seek: game KHÓ, không phải game DỄ
  → Benchmark: Dark Souls, fighting games, rhythm games, speedrun

Player Mastery thấp:
  → Thua 3 lần → "game khó quá" → quit hoặc cần easy mode
  → Mastery = frustration (desire impact/comfort/discovery thay thế)

⚠️ MASTERY CÓ Lớp 1 COMPONENT (khác Discovery/Collection):
  → Khi clear hard boss: body THẬT SỰ feel satisfaction (opioid real)
  → Mastery = strongest Lớp 2 vì NÓ BƠM Lớp 1
  → → Game mastery-driven = retention CAO NHẤT nếu difficulty ĐÚNG
```

### CH7: COLLECTION — "Tôi muốn THU THẬP, hoàn thiện"

```
Desire: "thêm 1 cái nữa!" + "100% completed!" — accumulation + completion
  → Check list. Đếm. "Còn 3 cái nữa là đủ!"
  → = Satisfaction từ ORDER + COMPLETION

Design cần:
  → Clear list: player BIẾT còn thiếu gì (checklist, pokédex, achievement)
  → Variety in collection: mỗi item CÓ GIÁ TRỊ riêng (không chỉ số)
  → Completion reward: đạt 100% → something special
  → Progress visible: "72/100" → thấy TIẾN rõ ràng
  → Rarity tiers: common → rare → legendary → emotional value KHÁC nhau

Player Collection cao:
  → 100% completion. Every achievement. Every collectible.
  → "Còn 1 item nữa" = DRIVE mạnh (completion anxiety)
  → Benchmark: Pokémon ("gotta catch 'em all"), completionist gamers

Player Collection thấp:
  → "Đủ rồi, không cần hết" → main quest done = done
  → Collection = "grind" → boring

⚠️ COLLECTION CÓ THỂ EXPLOIT:
  → Gacha = collection desire + random reward = ADDICTIVE
  → FOMO limited items = collection desire + scarcity = MANIPULATIVE
  → Ethical: collection via GAMEPLAY (find, earn). Unethical: collection via MONEY (pay, gamble).
```

---

## 4. MEANING Channels — Nhớ Mãi (Lớp 3)

### CH8: CONNECTION — "Tôi muốn GẮN BÓ"

```
Desire: "chơi VỚI ai đó" hoặc "care VỀ ai đó (NPC)" — social + emotional bond
  → Cười cùng nhau. Lo cho nhân vật. "Không muốn NPC này chết!"
  → = Connection THẬT dù qua medium ảo

2 sub-channels:

  CH8a: SOCIAL CONNECTION (người thật):
    → Co-op: "làm cùng nhau" → shared achievement
    → Guild/clan: "thuộc về nhóm" → identity + belonging
    → Communication: voice chat, emote, shared moments
    → Competition CÙNG bạn: "đánh nhau vui" → bonding qua rivalry
    → Design: multiplayer, community features, shared goals
    → = STRONGEST long-term retention (WoW 20 năm = vì FRIENDS)

  CH8b: CHARACTER CONNECTION (nhân vật ảo):
    → NPC có depth: backstory, personality, growth, vulnerability
    → Player CARE: quyết định ảnh hưởng NPC → emotional weight
    → "Khóc khi companion chết" = body respond THẬT dù NPC ảo
    → Design: branching dialogue, character arcs, meaningful choices
    → = Game trở thành "nhớ mãi" (Last of Us, Witcher, Undertale)

Player Connection cao:
  → Chơi VÌ NGƯỜI (friends hoặc NPCs), game là cái cớ
  → "Game hay nhất" thường = game có NGƯỜI hay nhất
  → Quit game nhưng nhớ MÃI characters/friends

Player Connection thấp:
  → Solo player. "Multiplayer annoying." "Skip dialogue."
  → Design cho channels khác (Impact, Mastery, Discovery)

⚠️ CONNECTION = KHÔNG MANIPULATE ĐƯỢC:
  → Fake social (bot comments, fake multiplayer) → player DETECT → trust broken
  → Real connection cần REAL investment (community management, quality writing)
  → Shortcut KHÔNG CÓ → nhưng reward = LỚNH NHẤT
```

---

## 5. Player Profile Tool — Thiết Kế Game Từ Đâu

### Bước 1: Xác định TARGET channels (2-3 primary)

```
Hỏi: "Game này cho PLAYER NÀO?"

KHÔNG hỏi: "nam 18-35" (demographic = vô nghĩa cho design)
HỎI:       "Impact●●●●● + Mastery●●●●● + Thrill●●●" (desire profile = actionable)

Ví dụ:
  "Action roguelike" → CH1(Impact)●●●●● CH4(Thrill)●●●● CH6(Mastery)●●●●
  "Cozy farm sim"    → CH2(Beauty)●●●● CH3(Comfort)●●●●● CH8(Connection)●●●
  "Story RPG"        → CH2(Beauty)●●●● CH5(Discovery)●●●● CH8(Connection)●●●●●
  "Competitive FPS"  → CH1(Impact)●●●●● CH4(Thrill)●●●●● CH6(Mastery)●●●●●
```

### Bước 2: Design DEEP cho primary channels

```
Rule: PRIMARY channels = ●●●●● (xuất sắc)
      SECONDARY channels = ●●●○○ (support, không cản)
      IGNORE channels = ○○○○○ (không phải game này)

Ví dụ "Action roguelike" (CH1 + CH4 + CH6):
  CH1 Impact: combat feel PHẢI perfect → 70% design effort
  CH4 Thrill: permadeath, random runs, near-death → 15% effort
  CH6 Mastery: skill ceiling, fair difficulty, clear feedback → 15% effort
  CH2 Beauty: đủ readable, style nhất quán → secondary, không focus
  CH8 Connection: optional co-op → nice to have, không priority

⚠️ KHÔNG design cho 8/8 channels:
  → Budget trải đều = MỌI channel mediocre = KHÔNG AI "wow"
  → Budget focus = 2-3 channels DEEP = target audience "GAME CỦA ĐỜI TÔI"
```

### Bước 3: Test bằng CHANNEL, không bằng FEATURE

```
KHÔNG hỏi: "feature X hay không?"
HỎI:       "feature X tăng PRIMARY channel nào?"

  Thêm leaderboard → tăng CH6 Mastery + CH7 Collection
    → NẾU primary channels có CH6/CH7 → thêm ✅
    → NẾU primary channels là CH3 Comfort → CONFLICT ❌ (leaderboard = stress)

  Thêm crafting → tăng CH5 Discovery + CH7 Collection + CH3 Comfort
    → NẾU primary là CH1 Impact → DILUTE ❌ (player muốn ĐÁNH, không craft)
    → NẾU primary là CH5+CH3 → ENHANCE ✅

  → Mỗi feature = phải biết CHANNEL NÀO nó serve
  → Feature không serve primary channel = CÂN NHẮC bỏ
```

---

## 6. Player Mood Shift — Cùng Người, Khác Lúc

```
⚠️ QUAN TRỌNG: Player profile KHÔNG CỐ ĐỊNH

Cùng 1 player, KHÁC thời điểm:

  Tối thứ 6 (mệt sau tuần làm):
    CH3(Comfort)●●●●● → muốn cozy game → Stardew

  Chiều chủ nhật (đã nghỉ đủ):
    CH1(Impact)●●●●● CH6(Mastery)●●●● → muốn challenge → Dark Souls

  Tối với bạn:
    CH8(Connection)●●●●● CH4(Thrill)●●● → muốn vui cùng → Among Us

IMPLICATIONS:
  → Game CÓ THỂ support NHIỀU moods (Minecraft: explore khi relax, build khi creative, fight khi energetic)
  → Hoặc game FOCUS 1 mood → marketing ĐÚNG timing
  → Cozy game ads: tối thứ 6 > sáng thứ 2
  → Competitive game ads: weekend afternoon > weeknight
```

---

## 7. Tại Sao "Game Cho Mọi Người" Thường Mid

```
Target 8/8 channels = SPREAD THIN:
  Mỗi channel: ●●○○○ → "cũng ok" → KHÔNG AI "wow!"
  Download: CAO (broad appeal)
  Retention: THẤP (không sâu channel nào → no one LOVES it)
  Word-of-mouth: THẤP ("cũng ok" không ai recommend)

Target 2-3 channels DEEP = FOCUSED:
  Primary channels: ●●●●● → "GAME CỦA ĐỜI TÔI!" (cho target audience)
  Download: THẤP HƠN (narrower appeal)
  Retention: CỰC CAO (deep channel match → player STAY)
  Word-of-mouth: CỰC CAO ("BẠN PHẢI CHƠI GAME NÀY!")

→ 100K players × love × recommend > 1M players × "ok" × forget
→ Indie philosophy: depth > breadth
→ Game stickman: CH1●●●●● ONLY → niche nhưng player QUAY LẠI vì FEEL ĐÚNG
```

---

## 8. Quick Reference — 8 Channels Summary

```
FEEL (Lớp 1):
  CH1 IMPACT:    "ĐẤM SƯỚNG!"     Body → lực, power, destruction
  CH2 BEAUTY:    "ĐẸP QUÁ!"       Body → aesthetic, atmosphere, art
  CH3 COMFORT:   "THƯ GIÃN..."     Body → warm, safe, nurturing
  CH4 THRILL:    "TIM ĐẬP!"       Body → adrenaline, risk, tension

PROGRESS (Lớp 2):
  CH5 DISCOVERY: "CÁI GÌ ĐÂY?"   Mind → explore, secrets, new
  CH6 MASTERY:   "TÔI LÀM ĐƯỢC!" Body+Mind → skill, improve, clear
  CH7 COLLECTION:"THÊM 1 CÁI!"   Mind → gather, complete, order

MEANING (Lớp 3):
  CH8 CONNECTION: "CÙNG NHAU!"    Heart → friends, characters, belong

Mỗi player = unique mix. Mỗi game = target 2-3 channels DEEP.
```

---

> *Player Psychology — DRAFT v1.0*
> *"Players are not types. Players are desire profiles."*
> *Dựa trên: Core-Principles.md + Human Predictive Drive Framework*
