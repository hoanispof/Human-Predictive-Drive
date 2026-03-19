# Visual & Audio Design — Serve the Feel

> **Mục đích:** Nguyên lý thiết kế visual + audio phục vụ gameplay feel.
> **Đọc trước:** Core-Principles.md (3 lớp reward), Gameplay-Design.md (feel tuning)
> **Ai đọc:** Artist, Sound Designer, Feel Owner, Animator
> **Nguyên tắc gốc:** Visual + Audio = Lớp 1 body reward. PHỤC VỤ feel, không showcase kỹ năng.

---

## 1. Nguyên Lý Gốc

### 1.1 Visual + Audio = 50% of Feel

```
Player cảm nhận game qua:
  MẮT (visual):  ~35% of feel
  TAI (audio):   ~35% of feel
  TAY (input):   ~30% of feel

  → Visual + Audio = ~70% of total feel
  → Nhưng thường: 80% budget cho visual, 5% cho audio, 15% cho gameplay
  → = MẤT CÂN BẰNG → feel bị lệch

  Test đơn giản:
    TẮT audio → chơi → feel GIẢM bao nhiêu %?
    → Nếu giảm > 30% → audio đang contribute đúng
    → Nếu giảm < 10% → audio chưa serve feel (phải fix)

    ĐỔI art thành grey box → chơi → feel GIẢM bao nhiêu %?
    → Nếu gameplay VẪN sướng → art đang DECORATE, chưa SERVE feel
    → Nếu gameplay MẤT hẳn → art đang SERVE feel đúng
```

### 1.2 SERVE, không SHOWCASE

```
Artist giỏi MUỐN vẽ đẹp → tự nhiên
Nhưng: đẹp ≠ serve feel

  ❌ Art showcase: "Nhìn tôi vẽ đẹp!" → player: "ồ đẹp" → 5 giây → quên → chơi game
  ✅ Art serve:    "Art giúp player CẢM gameplay" → body respond ĐÚNG → feel MẠNH hơn

Ví dụ:
  Enemy design:
    ❌ Showcase: enemy chi tiết, nhiều texture, animation phức tạp → đẹp nhưng CHẬM read
    ✅ Serve: enemy silhouette RÕ, color CONTRAST background, size = threat level
             → player ĐỌNG ngay → body react NHANH → feel responsive

  Environment:
    ❌ Showcase: background hyper-detailed → player MẤT focus vào gameplay
    ✅ Serve: background SET MOOD, không distract → player focus foreground
             → depth of field: foreground sharp + background blur

  VFX:
    ❌ Showcase: particles everywhere, bloom max, screen covered
    ✅ Serve: VFX confirm ACTION → hit = spark TẠI hit point → body "LỰC!"
             Proportional: light hit = small VFX. Heavy = big VFX.
```

### 1.3 Quy tắc vàng

```
1. READABILITY > BEAUTY
   → Player phải ĐỌC ĐƯỢC game state trong < 0.5 giây
   → Đẹp nhưng đọc chậm = feel chậm = bad

2. CONSISTENCY > FIDELITY
   → Style nhất quán (dù simple) > realistic nhưng lộn xộn
   → Minecraft: pixel consistent → brain accept → immersion
   → Bad: realistic character + cartoon background → brain reject

3. CONTRAST = INFORMATION
   → Player = SÁNG, Enemy = TỐI (hoặc ngược lại — pick one)
   → Interactive = SATURATED, Background = DESATURATED
   → Danger = RED, Safe = BLUE/GREEN (universal)
   → Feedback = HIGH CONTRAST (white flash khi hit)

4. MOTION = FEELING
   → Static art KHÔNG tạo feel → MOTION tạo feel
   → Squash-stretch: jump → body feel "weight"
   → Anticipation: attack wind-up → body feel "POWER coming"
   → Follow-through: attack recovery → body feel "committed"
   → 12 principles of animation → 3 quan trọng nhất cho game: squash, anticipation, follow-through

5. AUDIO TRƯỚC HOẶC SONG SONG, KHÔNG SAU
   → Audio prototype CÙNG LÚC với feel prototype
   → Placeholder SFX ngày 1 > final SFX tháng 3
   → Feel tune với audio → feel tune ĐÚNG hơn
   → Feel tune không audio → tune LẠI khi có audio → waste
```

---

## 2. Visual Design

### 2.1 Art Style cho Casual Game

```
Casual game art KHÁC AAA art:

  AAA: realistic, detailed, mọi pixel quan trọng
  Casual: CLEAR, FAST READ, consistent style

  3 nguyên tắc casual art:

  A. SIMPLIFY SHAPE → silhouette test:
     → Tô đen nhân vật → VẪN nhận ra? → ✅ design đúng
     → Tô đen → "cái gì thế?" → ❌ shape không rõ → redesign
     → Casual player KHÔNG zoom in → họ thấy SILHOUETTE + COLOR

  B. COLOR = FUNCTION:
     → Player: 1 màu rõ (blue/white/bright)
     → Enemy: 1 màu rõ KHÁC player (red/dark/contrasting)
     → Collectible: 1 màu rõ KHÁC enemy (gold/yellow/glowing)
     → Background: MUTED (low saturation, low detail)
     → → Mọi visual information = COLOR CODING
     → Player brain: 0.1 giây decode "blue = me, red = danger, gold = grab"

  C. SIZE = IMPORTANCE:
     → Boss: LỚN → body respond "THREAT!"
     → Reward: SÁNG + MOTION (glowing, spinning)
     → UI: NHỎ NHẤT có thể → gameplay CHIẾM screen
     → Casual: screen nhỏ (mobile) → mỗi pixel PHẢI có lý do
```

### 2.2 Animation Principles cho Feel

```
Casual animation: FEWER frames but SNAPPY > MANY frames but slow

  ATTACK ANIMATION:
    Frame 1-2: WIND-UP (anticipation — body "chuẩn bị!")
    Frame 3:   IMPACT (snap to hit pose — body "ĐÁNH!")
    Frame 4-5: FOLLOW-THROUGH (settle — body "committed")
    → TOTAL: 5 frames có thể ĐỦ cho casual
    → ⚠️ Frame 3 (impact) là QUAN TRỌNG NHẤT → snap, không ease

  MOVEMENT:
    Idle: subtle breathing → "sống"
    Run: tilt forward + dust particles → "nhanh"
    Jump: squash on ground → stretch in air → squash on land → "weight"
    Stop: slide 2-3 frames → "momentum"

  ENEMY HIT REACTION:
    Frame 1: white flash (0.05s — "hit registered!")
    Frame 2-4: knockback direction (body thấy "force transfer")
    Frame 5+: recovery hoặc ragdoll (body thấy "consequence")
    → ⚠️ Ragdoll physics = feel bonus CỰC LỚN với effort thấp
    → Stickman game: ragdoll = "phê mắt" → chính là Lớp 1 visual opioid

  JUICE (micro-animations làm game "sống"):
    → Screen shake: proportional to impact (xem Gameplay-Design.md §2)
    → Camera zoom: slight zoom on heavy hit → "DRAMATIC"
    → Particle burst: mỗi impact → particles từ point of contact
    → UI bounce: score pop → scale up → scale down → "satisfying"
    → → Juice = KHÔNG tốn art effort nhiều nhưng TĂNG feel đáng kể
    → → Programmer có thể implement juice WITHOUT artist
```

### 2.3 UI Design cho Casual

```
UI casual: ÍT NHẤT CÓ THỂ

  RULE: Nếu bỏ UI element → player VẪN chơi được → BỎ element đó

  Cần:
    → Score/progress: nhỏ, góc màn hình
    → Health (nếu có): visual trên character (flash red) > health bar
    → Input hint (đầu game): fade sau 3 giây

  Không cần:
    → Minimap (casual = simple level)
    → Complex HUD (casual ≠ simulation)
    → Tutorial text (dạy bằng gameplay, xem Gameplay-Design.md)

  MENU:
    → Start screen: 1-2 tap để vào game (KHÔNG 5 screens)
    → Settings: basic (sound on/off, language)
    → ⚠️ MỌI giây player KHÔNG CHƠI = potential drop
    → → Tối thiểu hóa time-to-play
```

---

## 3. Audio Design

### 3.1 Audio = Body Reward Trực Tiếp

```
Audio vào NÃO qua con đường KHÁC visual:
  Visual: mắt → visual cortex → conscious processing → respond (~200ms)
  Audio: tai → auditory cortex → emotional centers → respond (~100ms)

  → Audio NHANH HƠN visual → body respond TRƯỚC
  → Audio = FIRST body reward khi action xảy ra
  → → SFX hit PHẢI trước hoặc cùng lúc visual hit → feel "snappy"
  → → SFX SAU visual → feel "laggy" dù cùng frame

Tại sao audio quan trọng hơn mọi người nghĩ:
  → Tắt nhạc phim kinh dị → hết sợ (audio = 80% horror feel)
  → Tắt nhạc game → feel GIẢM 30-50%
  → Thay SFX tốt → cùng visual nhưng feel TĂNG đáng kể
  → → Audio = investment THẤP, return CAO nhất per effort
```

### 3.2 SFX Design — Feedback Sound

```
MỖI action = MỖI sound riêng biệt:

  IMPACT SFX (quan trọng nhất):
    → Light hit: "tap" — short, light, low bass
    → Medium hit: "thwack" — medium, some bass
    → Heavy hit: "BOOM" — long, heavy bass, satisfying
    → → Pitch variation ±10% random mỗi hit → natural, không repetitive
    → → Layer: transient (attack) + body (sustain) + tail (release)
    → → Bass = power. Crunch = damage. Thud = weight.

  MOVEMENT SFX:
    → Jump: "whoosh" (short)
    → Land: "thud" (proportional to height)
    → Walk/Run: footsteps (surface-dependent nếu có budget)
    → Dash: "swoosh" (fast, air displacement)

  UI SFX:
    → Button press: "click" (subtle, satisfying)
    → Score: "ding" / "chime" (rewarding)
    → Error: "buzz" (soft, not punishing)
    → Level complete: "fanfare" (celebratory, 1-2 giây)

  AMBIENT:
    → Background loop: mood-setting, LOW volume, không distract
    → Environment hints: wind, crowd, fire → immersion

⚠️ CÓ THỂ TỰ TẠO:
  → Tools: sfxr/jsfxr (free, retro SFX), Audacity (edit), Freesound (library)
  → Placeholder: TẠO NGAY ngày 1 → iterate
  → Final: sound designer polish hoặc tìm high-quality assets
  → → Placeholder NGÀY 1 > Final THÁNG 3 (feel tune CẦN audio sớm)
```

### 3.3 Music Design

```
Music ROLE trong game:

  MOOD: Set emotional context
    → Action music → body "sẵn sàng!" (arousal tăng)
    → Calm music → body "thoải mái" (arousal giảm)
    → Tension music → body "cẩn thận!" (cortisol nhẹ)
    → → Music = EMOTIONAL PRIMER cho gameplay

  PACING: Reinforce rhythm
    → Fast tempo → gameplay feel fast
    → Slow tempo → gameplay feel strategic
    → Drop/buildup → CONTRAST → body feel "đỉnh điểm!" → climax
    → → Music tempo NÊN match gameplay pace

  REWARD: Audio reward cho achievement
    → Boss clear: music swell + victory motif
    → Level complete: satisfying resolution chord
    → Game over: soft, not punishing (player đã bực rồi → đừng bực thêm)

MUSIC LOOP:
  Casual game: nhạc loop liên tục
  → Loop point: tìm điểm nhạc tự nhiên để loop (không jump audible)
  → Duration: 60-120 giây loop (ngắn hơn = repetitive, dài hơn = memory)
  → Variation: subtle layer thêm/bớt khi gameplay intensity thay đổi (nếu có budget)

⚠️ LICENSING:
  → Royalty-free music: nhiều nguồn chất lượng (Epidemic Sound, Artlist, free alternatives)
  → ĐỪNG dùng copyrighted music (trừ khi music game với API hợp pháp)
  → Composer hire: có thể thuê per-track, giá thay đổi nhiều
```

---

## 4. Visual-Audio COUPLING — Khi Visual và Audio Phối Hợp

### 4.1 Nguyên lý Coupling

```
Visual + Audio CÙNG confirm 1 event = body reward × 2:

  TRIPLE CONFIRMATION:
    Player input (tay) + Visual feedback (mắt) + Audio feedback (tai)
    = 3 channels CÙNG nói "HIT!" = body: "CHẮC CHẮN xảy ra!" = SATISFYING

  Ví dụ:
    Bấm attack:
      TAY: rumble (nếu có)
      MẮT: hitstop + flash + particles
      TAI: "THWACK!"
      → 3 channels sync → body: "ĐẤM MẠNH!" → opioid micro-dose → feel ✅

    Chỉ visual, không audio:
      MẮT: hitstop + flash
      TAI: (im lặng)
      → 2/3 channels → body: "hình như đánh..." → feel GIẢM 40%

    Chỉ audio, không visual:
      MẮT: (không thay đổi)
      TAI: "THWACK!"
      → Body: "nghe có gì nhưng không thấy..." → confusing

  → SYNC là key: visual + audio CÙNG LÚC (±1 frame)
  → Audio TRƯỚC visual 1-2 frame: ok (audio nhanh hơn)
  → Audio SAU visual 3+ frame: KHÔNG ok (feel laggy)
```

### 4.2 Proportional Response

```
Action NHỎ → feedback NHỎ (visual + audio)
Action LỚN → feedback LỚN (visual + audio)

  Light attack:
    Visual: small flash, few particles
    Audio: soft "tap"
    Shake: 1-2px, 2 frames

  Heavy attack:
    Visual: big flash, many particles, screen crack?
    Audio: deep "BOOM" + bass
    Shake: 8-12px, 5 frames

  Critical/Special:
    Visual: FULL SCREEN flash + slow-motion + zoom
    Audio: layered impact + reverb + music swell
    Shake: heavy + camera zoom in/out

  → CONTRAST tạo feel:
    100 light hits → 1 heavy hit → heavy feel CỰC MẠNH (so với light)
    Nếu MỌI hit = heavy → numb → nothing feels heavy
    → → DYNAMICS quan trọng: quiet → loud, small → big, slow → fast
```

---

## 5. Music Game — Đặc Thù

> Section này dành cho game mà NHẠC là core experience, không chỉ background.
> Với game thường: bỏ qua section này.

### 5.1 Music Game = Audio PRIMARY, Visual SERVE

```
Game thường:  Gameplay → Visual → Audio (audio support)
Music game:   MUSIC → Gameplay → Visual (visual serve music)

  → MỌI visual element PHẢI khớp nhạc
  → Visual KHÔNG khớp nhạc = DECOUPLED = feel GIẢM mạnh
  → Test: tắt nhạc → chơi → NẾU vẫn chơi được → coupling CHƯA đủ
  → Ideal: tắt nhạc → game KHÔNG CÓ Ý NGHĨA → coupling ĐÚNG
```

### 5.2 5 Chiều Coherence (Music-Visual)

```
Chiều 1 — TIMING: visual event đúng beat/onset nhạc
  → Cơ bản nhất. Onset detection giải quyết.
  → Sai timing > 50ms → player CẢM "off beat" → feel hỏng

Chiều 2 — MUSICAL WEIGHT: event quan trọng = visual lớn
  → Downbeat + bass = visual LỚN. Hi-hat = visual NHỎ.
  → Không phải mọi note BẰNG NHAU → visual phải reflect importance

Chiều 3 — GROOVE: giữ syncopation, swing
  → Quantize quá strict → mất groove → nhạc feel "robot"
  → Cho phép micro-timing variation = nhạc feel "sống"

Chiều 4 — DYNAMIC ARC: visual intensity theo musical dynamics
  → Verse nhẹ → visual calm. Chorus mạnh → visual intense.
  → Build-up → visual tăng dần. Drop → visual BURST.

Chiều 5 — EMOTIONAL ACCENT: khoảnh khắc đặc biệt = visual đặc biệt
  → Bridge im lặng → visual im lặng (contrast)
  → Final chord → visual climax
  → Key change → visual color shift?

→ Casual hiện tại thường chỉ đạt chiều 1 (timing)
→ Chiều 2-5 = khoảng cách giữa "ok" và "WOW"
→ Chi tiết: Perceptual-Research/Music Cognition Research/
```

### 5.3 4 Cơ Chế Vô Thức (Music-Gameplay Coupling)

```
Khi visual-audio-motor CÙNG lock vào nhạc:

1. ENTRAINMENT — body sync vào beat
   → Tap timing = music timing → multi-system synchronization
   → Body tự nhiên "nhập" vào nhạc → immersion

2. AGENCY ILLUSION — "tôi tạo ra âm thanh"
   → Tap đúng lúc note vang → não nghĩ "tôi gây ra!"
   → Satisfying CỰC MẠNH (illusion of control over music)

3. TRIPLE CONFIRMATION — 3 channels confirm prediction
   → Visual + Motor + Auditory cùng confirm → reward × 3
   → Brain: "prediction ĐÚNG 3 lần!" → massive PE dương

4. VISUAL-AUDITORY BINDING — "nhìn thấy" nhạc
   → Object type khớp sound type → cross-modal binding
   → Bass = big object. Hi-hat = small object.
   → Brain MERGE visual + audio thành 1 experience

→ Tất cả VÔ THỨC → player chỉ cảm "sướng hơn" mà không biết tại sao
→ Mất 1 cơ chế → feel GIẢM mà player không articulate được
→ → Đây là tại sao music game coupling tốt → "addictive"
→ → Và coupling tệ → "off" nhưng player không nói rõ được
```

### 5.4 Difficulty = Musical Depth (không phải Speed)

```
❌ Tăng speed: 1.5x speed → pitch distortion + tempo shift + motor range vượt
   → Vô thức BỊ LỆCH dù ý thức nhận ra bài nhạc
   → User phản hồi tiêu cực rõ ràng

✅ Tăng musical layers:
   Easy:    objects khớp beat chính (kick, downbeat)
   Normal:  + vocal onset, bass line, snare
   Hard:    + hi-hat, synth detail, dynamic accent
   Expert:  + micro-rhythm, ghost notes, polyrhythm

   → Khó hơn = nghe SÂU hơn vào nhạc = appreciate nhạc HƠN
   → Player GIỎI LÊN = nghe nhạc TỐT HƠN → win-win
   → Yêu cầu: multi-layer audio detection (tách instruments)
```

---

## 6. Workflow — Art + Sound trong Game Pipeline

### 6.1 Khi nào bắt đầu

```
PHASE 1 (Feel Prototype):
  → Art: GREY BOX (shapes, no art)
  → Sound: PLACEHOLDER SFX (sfxr/free assets)
  → ⚠️ SFX placeholder PHẢI CÓ từ ngày 1
  → Feel tune VỚI audio → tune ĐÚNG hơn
  → Feel tune KHÔNG audio → tune sai → phải re-tune khi có audio

PHASE 2 (Content Prototype):
  → Art: ART DIRECTION (style guide, color palette, 1-2 key assets)
  → Sound: SFX PROTOTYPE (core actions: impact, jump, UI)
  → Music: MOOD REFERENCE (nhạc tham khảo, chưa cần original)

PHASE 3 (Production):
  → Art: FINAL ART (all assets, polish, consistency check)
  → Sound: FINAL SFX + MUSIC (all sounds, mix, master)
  → ⚠️ Art + Sound DEADLINE nên trước code deadline 1-2 tuần
  → → Cho thời gian integration + final feel check
```

### 6.2 Artist-Feel Owner Communication

```
Feel Owner KHÔNG nên nói: "Vẽ đẹp hơn" (vague, không actionable)
Feel Owner NÊN nói:
  → "Enemy cần đọc NHANH hơn — silhouette chưa clear ở distance"
  → "Hit flash CẦN thêm — body không thấy hit register"
  → "Background quá busy — player mất focus foreground"
  → "Color enemy quá giống player — confused khi combat đông"

  = FUNCTION feedback, không AESTHETIC feedback
  = "Cái này KHÔNG serve feel vì [lý do cụ thể]"

Artist feedback NGƯỢC Feel Owner:
  → "Style này cần thời gian X — timeline ok?"
  → "Nếu simplify ở đây → art process nhanh hơn → iteration nhiều hơn"
  → "Asset này dùng lại từ game trước → save thời gian"
  → = PRODUCTION feedback, giúp team ship nhanh hơn
```

### 6.3 Sound-Feel Owner Communication

```
Feel Owner NÊN provide:
  → Reference: "SFX giống game X khi đánh" (audio reference > text description)
  → Feel target: "phải nghe NẶNG, bass nhiều" hoặc "phải nghe NHANH, crisp"
  → Context: "SFX này chạy 20 lần/giây → cần ngắn, không annoying khi lặp"

Sound Designer deliver:
  → 3 variations per SFX (pitch/tone khác nhau) → Feel Owner chọn
  → ⚠️ SỚM: placeholder ngày đầu, improve dần
  → KHÔNG: 1 final version sau 2 tuần im lặng
```

---

## 7. Common Mistakes

```
❌ "Art trước, gameplay sau"
   → Art đẹp + feel tệ = download cao + uninstall cao
   → Feel đúng + art vừa = retention cao
   → → Art PHỤC VỤ feel, không lead feel

❌ "Sound cuối cùng"
   → Sound = 50% feel → thiếu sound = feel thiếu 50% suốt development
   → → Placeholder SFX NGÀY 1

❌ "Realistic = tốt hơn"
   → Casual player: CLEAR > REALISTIC
   → Minecraft > photorealistic game nobody remembers
   → → Style consistency + readability > technical fidelity

❌ "Nhiều VFX = juicy"
   → Quá nhiều = noise → body numb → nothing stands out
   → → Proportional: small action = small VFX. BIG action = BIG VFX.
   → → CONTRAST tạo feel, không VOLUME

❌ "Nhạc hay = game hay"
   → Nhạc hay + decoupled gameplay = 2 trải nghiệm tách rời
   → Nhạc vừa + coupled gameplay = 1 trải nghiệm gắn kết
   → → COUPLING > QUALITY (cho music game)
   → → MOOD MATCH > HIT SONG (cho game thường)

❌ "Tham khảo game top chart → copy art style"
   → Copy STYLE mà không hiểu TẠI SAO style đó serve feel = fail
   → → Hiểu NGUYÊN LÝ (readability, contrast, proportion) → apply cho style RIÊNG

❌ "Artist tự quyết art direction"
   → Art direction PHẢI serve game feel → Feel Owner input REQUIRED
   → Artist THỰC HIỆN art direction, Feel Owner VALIDATE serve feel
   → Collaboration, không dictatorship
```

---

## 8. Checklist

```
ART CHECKLIST:
  □ Silhouette test pass (nhận ra character khi tô đen)
  □ Color coding clear (player ≠ enemy ≠ collectible ≠ background)
  □ Size = importance (boss > enemy > projectile)
  □ Background KHÔNG distract foreground gameplay
  □ Consistency: style đồng nhất across mọi asset
  □ Animation snappy: attack frame 1-3 nhanh, impact frame rõ
  □ Juice: flash, shake, particles cho core actions

SOUND CHECKLIST:
  □ Placeholder SFX từ Phase 1 (không đợi Phase 3)
  □ Impact SFX: mỗi hit type có sound riêng
  □ Pitch variation: ±10% random (không lặp exact)
  □ Proportional: light hit = soft SFX, heavy = loud + bass
  □ Audio sync: SFX đồng thời hoặc TRƯỚC visual (không SAU)
  □ Music mood match gameplay pacing
  □ Volume mix: SFX > Music > Ambient (gameplay feedback ưu tiên)

COUPLING CHECKLIST:
  □ Triple confirmation: input + visual + audio cho core actions
  □ Proportional response: action size = feedback size
  □ Mute test: tắt audio → feel giảm > 30%? (nếu có = audio đang work)
  □ Grey box test: bỏ art → feel vẫn sướng? (nếu có = gameplay solid)
```

---

## 9. Tools & Resources

```
ART TOOLS (free/low cost):
  → Aseprite: pixel art ($20, industry standard cho indie)
  → Krita: digital painting (free)
  → Blender: 3D (free) — nếu cần 3D assets
  → Spine: 2D animation ($70+) — nếu cần bone animation
  → DragonBones: 2D animation (free alternative)

SOUND TOOLS:
  → sfxr / jsfxr: retro SFX generator (free, web-based)
  → Audacity: audio editor (free)
  → FMOD / Wwise: audio middleware (free cho indie)
  → Freesound.org: CC sound library (free)
  → Epidemic Sound / Artlist: music library (subscription)

VFX / JUICE:
  → Particle systems: built into Unity/Godot/etc.
  → DOTween (Unity) / Tween library: animation easing
  → Screen shake: custom script (simple, high impact)
  → Post-processing: bloom, vignette, color grading (built-in)
```

---

> *Visual & Audio Design — Serve the Feel*
> *Art đẹp ≠ game hay. Art SERVE feel = game hay.*
> *Sound = 50% feel. Placeholder ngày 1, final tháng 3.*
> *Coupling > Quality. Readability > Beauty. Consistency > Fidelity.*
