---
title: Musical Notation Architecture
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — reference document, read for deep understanding
scope: Music as a "language" system — notation, syntax, structure, compared to natural language and math
purpose: Understand music notation as a communication format — what does it encode that natural language and math CANNOT
parent: ../../plan.md (F3 Chunk-External-Development)
language: English primary + music notation
note: Written for people who LISTEN to music daily but have never "dissected" its notation structure
---

# Musical Notation Architecture

> **Purpose**: You listen to music every day but may never have viewed music notation as a LANGUAGE SYSTEM. This file "dissects" the structure — not to teach music, but to see music as a communication format that encodes what natural language and math CANNOT: **temporal-affective patterns** (emotionally structured patterns through time).
>
> **Comparison with previous files**: 01 = natural language (broadest). 02 = math (most precise). This file = music (most temporal-affective).

---

## TABLE OF CONTENTS

- §1 — Music "Vocabulary": Basic Components
  - §1.1 Pitch — Music's "Nouns"
  - §1.2 Duration — Music's "Tense"
  - §1.3 Rhythm — "Grammar of Time"
  - §1.4 Dynamics — Music's "Voice Volume"
  - §1.5 Harmony — "Context"
  - §1.6 Melody — "The Story"
  - §1.7 Timbre — "Sound Color"
- §2 — Music "Grammar": How to Combine
  - §2.1 Scale — "Permitted Vocabulary"
  - §2.2 Key — The Musical "Language"
  - §2.3 Counterpoint + Voice Leading — "Multi-Voice Grammar"
- §3 — Hierarchy: Note → Motif → Phrase → Section → Piece
- §4 — The Notation System: Staff Notation
- §5 — Comparison: Music vs Natural Language vs Math
- §6 — What Music Encodes That Other Formats CANNOT
- §7 — History of Development
- §8 — Framework Lens + Open Questions

---

## §1 — Music "Vocabulary": Basic Components

### §1.1 — Pitch = Music's "Nouns" — WHAT IT'S ABOUT

```
PITCH = how high or low a sound is

12 NOTES in 1 octave:
  C  C#  D  D#  E  F  F#  G  G#  A  A#  B
  (Do Dó# Re Re# Mi Fa Fa# Sol Sol# La La# Si)

  → After B loops back to C (one octave higher): C₃ → C₄ → C₅
  → Piano has ~88 keys = ~7 octaves
  → Human hearing range: ~20 Hz (extremely low) → ~20,000 Hz (extremely high)

⭐ WHY 12 NOTES?
  → Frequency ratio: each note is × ¹²√2 ≈ 1.0595 higher than the previous
  → 12 notes × ¹²√2 = ×2 → octave = double the frequency
  → A₄ = 440 Hz, A₅ = 880 Hz (exactly double)
  → The 12-note equal temperament system was standardized ~1600s (Bach era)

NAMING SYSTEMS:
  Letter system (English/International):  C D E F G A B
  Solfège system (Italian/Vietnamese):    Do Re Mi Fa Sol La Si
  Number system (MIDI):                   60 62 64 65 67 69 71   (C₄ = 60)
  → Game devs know MIDI numbers: every note = 1 integer
```

### §1.2 — Duration = Music's "Tense" — HOW LONG

```
DURATION = how long a note lasts

  𝅝   Whole note      = 4 beats
  𝅗𝅥   Half note       = 2 beats
  ♩   Quarter note    = 1 beat
  ♪   Eighth note     = 1/2 beat
  ♬   Sixteenth note  = 1/4 beat

  → Each level = HALVES the previous (1 → 1/2 → 1/4 → 1/8 → 1/16)
  → BINARY system — just like computers!

ADDITIONAL:
  Dot:   ♩. = 1 + 1/2 = 1.5 beats     (adds half the note's value)
  Tie:   ♩‿♩ = 1 + 1 = 2 beats         (links 2 notes of the same pitch)
  Rest:  𝄾 = silence for 1 beat        (DON'T PLAY — but SILENCE IS ALSO MUSIC!)

⭐ "Silence is also music" — Debussy
  → Rest = "nothing" chunk — but CRITICAL for rhythm
  → Like: the spaces between words are CRITICAL for reading comprehension
```

### §1.3 — Rhythm = "Grammar of Time"

```
TIME SIGNATURE = defines the temporal structure

  4/4  = 4 beats per bar, quarter note = 1 beat
         → THE MOST COMMON. Pop, rock, classical all use it.
         → "Common time" — written as C

  3/4  = 3 beats per bar → WALTZ feel (1-2-3, 1-2-3)
  6/8  = 6 eighth notes per bar → compound feel (1-2-3-4-5-6)
  2/4  = 2 beats → march feel (1-2, 1-2)
  5/4  = 5 beats → uncommon, e.g. "Take Five" (Dave Brubeck)
  7/8  = 7 eighth notes → Balkan music, progressive rock

TEMPO (Speed):
  Largo       = very slow (~40-60 BPM)
  Adagio      = slow (~60-80 BPM)
  Andante     = walking pace (~80-100 BPM)
  Moderato    = moderate (~100-120 BPM)
  Allegro     = fast (~120-160 BPM)
  Presto      = very fast (~160-200 BPM)

  BPM = Beats Per Minute
  → Game devs know: frame rate analogy. 120 BPM ≈ 2 beats/second
  → Rhythm game: timing window typically ±50ms per beat

⭐ RHYTHM = structure that NATURAL LANGUAGE LACKS:
  → A written sentence has NO fixed beat (flexible timing)
  → Music HAS a fixed beat (rigid timing) — that's why music "pulls you in"
  → Beat = expectation pattern: brain PREDICTS the next beat → VTA dopamine alert
    when prediction confirmed → opioid (coherence reward) on pattern match
    (⚠️ Dopamine = alert/salience. Opioid = actual pleasure. Ref: 03-Reward.md)
```

### §1.4 — Dynamics = Music's "Voice Volume" — LOUD or SOFT

```
DYNAMICS = volume / intensity

  ppp   pianississimo    = extremely soft
  pp    pianissimo       = very soft
  p     piano            = soft
  mp    mezzo-piano      = moderately soft
  mf    mezzo-forte      = moderately loud
  f     forte            = loud
  ff    fortissimo       = very loud
  fff   fortississimo    = extremely loud

  crescendo   (cresc.) <   = getting louder
  decrescendo (decresc.) > = getting softer
  sforzando   (sfz)        = sudden loud accent

→ Dynamics = EMOTIONAL INTENSITY
→ pp → ff = from a whisper to a shout
→ Crescendo = emotional build-up → climax
→ Natural language HAS dynamics but does NOT encode them precisely in writing
```

### §1.5 — Harmony = "Context" — Multiple Notes SIMULTANEOUSLY

```
CHORD = multiple notes played SIMULTANEOUSLY

Basic chords (triads):
  C major:      C - E - G     → sounds BRIGHT, HAPPY
  C minor:      C - Eb - G    → sounds DARK, SAD
  C diminished: C - Eb - Gb   → sounds TENSE
  C augmented:  C - E - G#    → sounds UNSTABLE, STRANGE

⭐ Major vs Minor:
  → Differ by only 1 NOTE (E vs Eb — a semitone apart)
  → Yet the EMOTION is COMPLETELY DIFFERENT (happy vs sad)
  → This is what math and natural language CANNOT encode directly:
    "A gentle sadness" = 3 words in natural language, IMPRECISE description
    Cm chord = 3 notes, encodes that EMOTION precisely

CHORD PROGRESSION:
  I - V - vi - IV  (example in C major: C - G - Am - F)
  → This is the MOST COMMON progression in pop music
  → "Let It Be", "No Woman No Cry", "Someone Like You",...
  → HUNDREDS of songs use the SAME 4 chords, different melodies + lyrics

  V → I  = Resolution — sounds "done", "home"
  IV → V = Build-up — sounds "incoming", "anticipating"
  vi     = Relative minor — sounds "gently sad", "reflective"

→ Chord progression = EMOTIONAL ARC encoded into harmonic structure
→ This is an EMOTIONAL STRUCTURE that only music encodes directly
```

### §1.6 — Melody = "The Story" — Notes Through Time

```
MELODY = a sequence of single notes over time forming a "musical sentence"

Properties:
  Contour (shape):  ascending, descending, flat, rise-then-fall...
  Range:            from the lowest to the highest note
  Intervals:        the distance between consecutive notes

  → Melody = combined chain of pitch + rhythm
  → Like: a "sentence" = combined chain of words + grammar

⭐ MELODY = WHAT PEOPLE REMEMBER:
  → Ask "how does that song go?" → people SING THE MELODY (not the chords)
  → Melody = "foreground" layer
  → Harmony = "background" layer (provides emotional context)
  → Rhythm = "skeleton" (holds the structure together)
```

### §1.7 — Timbre = "Sound Color" — WHO Plays It

```
TIMBRE = SOUND QUALITY — same note, different instrument = different feel

  Piano C₄         = sounds "clear, crisp, focused"
  Violin C₄        = sounds "smooth, vibrating, warm"
  Trumpet C₄       = sounds "bright, powerful, direct"
  Flute C₄         = sounds "clear, light, airy"
  Guitar C₄        = sounds "warm, round, intimate"
  Synthesizer C₄   = sounds "anything" (can create any timbre)

→ Timbre is NOT well-captured by notation (hard to write as symbols)
→ Only the instrument name is written: "Violin", "Flute", "Piano"
→ Game dev: timbre = sound design, waveform, ADSR envelope
→ This is a limitation of music notation: encodes pitch + rhythm well,
  encodes timbre ONLY indirectly (through instrument name)
```

---

## §2 — Music "Grammar": How to Combine

### §2.1 — Scale = "Permitted Vocabulary" for One Piece

```
From 12 notes, each piece selects 7 as its "vocabulary":

  C Major scale:    C D E F G A B     (all the white keys on piano)
  C Minor scale:    C D Eb F G Ab Bb  (3 notes different → COMPLETELY different feel)
  A Minor scale:    A B C D E F G     (same notes as C Major, but starting from A!)

  Pentatonic:       C D E G A         (5 notes — Chinese music, Celtic music, blues)
  Blues scale:      C Eb F F# G Bb   (adds the "blue note" F#)
  Whole tone:       C D E F# G# A#   (evenly spaced → sounds "hazy, floating")

→ Scale = permitted "vocabulary" set, like the vocabulary of a specific language
→ Major = "happy vocabulary", Minor = "sad vocabulary"
→ Pentatonic = "simple, universal vocabulary" (children's songs, folk music worldwide)
→ Playing a note OUTSIDE the scale = "grammatical error" (tension) or "creativity" (jazz)
```

### §2.2 — Key = The Musical "Language" of a Piece

```
KEY = scale + home note (tonic)

  Key of C Major = uses C Major scale, C is "home"
  Key of G Major = uses G Major scale (G A B C D E F#), G is "home"
  Key of A Minor = uses A Minor scale, A is "home"

KEY SIGNATURE:
  Written at the start of the score: how many # or b signs
  → Tells the reader WHICH notes this "language" uses

  0 sharps/flats  = C Major / A Minor
  1 #             = G Major / E Minor
  2 #             = D Major / B Minor
  ...
  1 b             = F Major / D Minor
  2 b             = Bb Major / G Minor
  ...

→ Total: 12 major keys + 12 minor keys = 24 musical "languages"
→ Modulation = "switching languages" mid-piece
  → Example: a song that shifts up a semitone in the final section = modulation up → feeling of "lift"
```

### §2.3 — Counterpoint + Voice Leading = "Multi-Voice Grammar"

```
COUNTERPOINT = multiple melodies SIMULTANEOUSLY, each with its own logic

  → Like: 2 people speaking at the same time, each SENTENCE has its own meaning,
    but COMBINED they sound beautiful
  → Bach = master of counterpoint: 2-4 simultaneous voices, each beautiful independently

VOICE LEADING = how to TRANSITION from one chord to the next
  → Each note in a chord moves the SHORTEST POSSIBLE distance to the next chord
  → "Smooth" transition = good voice leading
  → "Jumping around" = bad voice leading (sounds uncomfortable)

→ Counterpoint = the most complex "grammar" in music
→ Equivalent: writing a paragraph where EVERY HORIZONTAL LINE makes sense,
  AND every VERTICAL COLUMN also makes sense (acrostic poem × 4!)
```

---

## §3 — Hierarchy: Note → Motif → Phrase → Section → Piece

```
LEVEL 1 — NOTE = "Word"
  C₄ quarter note = Middle C, 1 beat
  → Smallest atom: pitch + duration

LEVEL 2 — MOTIF = "Phrase"
  Beethoven 5th: ♩♩♩𝅗𝅥 (da-da-da-DAAA)
  → 3-7 notes forming the smallest recognizable "musical idea"
  → Motif = the musical "DNA" — repeated and transformed throughout the piece

LEVEL 3 — PHRASE = "Sentence"
  Typically 4-8 bars
  → 1 musical "breath" — where a singer inhales, where a violinist changes bow direction
  → Has a "comma" (half cadence) or "period" (full cadence)

LEVEL 4 — SECTION = "Paragraph"
  A section (verse), B section (chorus), C section (bridge)
  → 2-4 phrases grouped into 1 section
  → Each has its own character: verse = storytelling, chorus = climax

LEVEL 5 — FORM = "Essay"
  Verse-Chorus:       ABABCB (most common pop song form)
  Sonata:             Exposition - Development - Recapitulation (classical)
  12-bar blues:       I-I-I-I-IV-IV-I-I-V-IV-I-V (blues/jazz)
  Rondo:              ABACADA (classical)
  Theme & Variations: A-A'-A''-A'''...

LEVEL 6 — OPUS / ALBUM = "Book"
  Symphony: 4 movements (each movement = its own form)
  Album: 10-15 pieces linked by theme
  Opera: 3-4 acts, each act has many scenes, each scene many arias

FRAMEWORK MAPPING:
  Level 1 Note        ↔ Chunk (atom)
  Level 2 Motif       ↔ Compound Chunk
  Level 3 Phrase      ↔ Chunk chain
  Level 4 Section     ↔ Schema
  Level 5 Form        ↔ Plan (goal structure: build → climax → resolve)
  Level 6 Opus/Album  ↔ Domain knowledge (full system)
```

---

## §4 — The Notation System: Staff Notation

```
STAFF = 5 horizontal lines — the "ruled paper" for music

  ───── F₅ (note on line 5)
  ───── D₅
  ───── B₄
  ───── G₄
  ───── E₄ (note on line 1)

  → Notes placed ON a line or IN a space = determines pitch
  → HIGHER on staff = HIGHER pitch
  → Treble clef (𝄞): for high notes (piano right hand, violin, voice)
  → Bass clef (𝄢): for low notes (piano left hand, cello, bass)

READ LEFT → RIGHT = TIME PASSING:
  → X axis = time (left = earlier, right = later)
  → Y axis = pitch (bottom = low, top = high)
  → This is a 2D CHART: pitch × time

NOTATION SYMBOLS:
  𝄞   Treble clef
  𝄢   Bass clef
  ♩   Quarter note
  ♪   Eighth note
  𝅝   Whole note
  𝄾   Quarter rest
  #   Sharp (raise by a semitone)
  b   Flat (lower by a semitone)
  ♮   Natural (cancels sharp/flat)
  𝄀   Barline
  𝄂   Double barline (end)

→ Staff notation = 2D CHART (pitch × time) + annotations (dynamics, tempo...)
→ Invented ~1000 CE (Guido d'Arezzo, Italy) — before this, music was entirely oral!
→ Staff notation is NOT perfect:
  ✅ Encodes WELL:     pitch, duration, dynamics, structure
  🟡 Encodes PARTIALLY: articulation, phrasing
  ❌ Encodes POORLY:   timbre, emotion, "feel", groove, microtiming
  → This is why: 2 pianists playing the SAME score sound DIFFERENT — notation doesn't capture everything
```

---

## §5 — Comparison: Music vs Natural Language vs Math

| Feature | Natural Language | Math | Music |
|---|---|---|---|
| **Primary Encoding** | Meaning (semantics) | Quantity + Relation | Temporal-Affective pattern |
| **"Vocabulary"** | ~5,000-10,000 words | ~150 symbols | 12 notes + duration + dynamics |
| **Ambiguity** | High (polysemous) | No | Medium (interpretive) |
| **Precision** | Low-Medium | Extremely high | High for pitch/rhythm, low for emotion |
| **Temporal structure** | Not fixed | No temporal dimension | ⭐ FIXED (beat, tempo) |
| **Emotional encoding** | Indirect (the word "sad") | None | ⭐ DIRECT (minor chord = sad) |
| **Multi-voice** | 1 idea at a time (sequential) | 1 equation at a time | ⭐ MULTIPLE voices simultaneously |
| **Shareability** | Requires shared language | Global | ⭐ Global (transcends language!) |
| **Body response** | Low-Medium | Low | ⭐ HIGH (rhythm → movement) |
| **Recursion** | 3-4 levels | Infinite | Limited (nested forms) |
| **Cultural variation** | Very large | Almost none | Medium (different scale systems) |
| **Training required** | No (L1 natural acquisition) | Yes (formal) | Partial (listening natural, playing requires study) |
| **Writing system** | ~5,000 years | ~3,000 years | ~1,000 years |
| **Age of system** | ~100,000+ years (spoken) | ~5,000 years (notation) | ~40,000+ years (singing/drumming) |

```
UNIQUE FEATURES OF MUSIC that the other 2 formats lack:

1. ⭐ TEMPORAL PRECISION: Music has an EXACT beat (±ms)
   → Natural language: flexible timing, no beat
   → Math: no temporal dimension
   → Music: 120 BPM = exactly 500ms per beat

2. ⭐ DIRECT EMOTIONAL ENCODING:
   → Natural language: "I am sad" = LABEL for an emotion (indirect)
   → Math: no emotional encoding
   → Music: Cm chord = DIRECTLY triggers a sad emotion (no label needed)

3. ⭐ MULTI-VOICE SIMULTANEOUS:
   → Natural language: only 1 idea at a time (sequential)
   → Math: only 1 equation at a time
   → Music: 4-part harmony = 4 "sentences" SIMULTANEOUSLY, each with independent meaning

4. ⭐ BODY ENTRAINMENT:
   → Listening to music → body AUTOMATICALLY sways with the beat
   → Nobody nods their head to a math equation
   → Nobody dances to a news broadcast
   → Music → motor cortex DIRECTLY (rhythm → movement coupling)

5. ⭐ CROSS-CULTURAL without translation:
   → Listen to Japanese music: you FEEL it even without knowing Japanese
   → Read a Japanese book: understand NOTHING without knowing the language
   → Music bypasses the language barrier → emotional content largely universal
```

---

## §6 — What Music Encodes That Other Formats CANNOT

### §6.1 — Emotional Arc (Emotional Trajectory)

```
A SONG = STRUCTURED EMOTIONAL TRAJECTORY:

  Intro:    quiet, anticipation          (pp, minor, slow)
  Verse 1:  storytelling, build          (mp, gradual)
  Chorus:   release, peak               (f, major, full band)
  Verse 2:  back to storytelling         (mp)
  Chorus:   higher peak                  (ff, key modulation up)
  Bridge:   tension, uncertainty         (new chords, unstable)
  Chorus:   FINAL PEAK                   (fff, full everything)
  Outro:    resolution, fade             (pp, return home)

→ This is an EMOTIONAL ARC = Imagine-Final lifecycle applied to feelings:
  Anticipation → Build → Peak → Resolution
→ Natural language CAN describe this arc
→ But music ENACTS it — listener EXPERIENCES the arc, not just reads about it
```

### §6.2 — Tension-Resolution

```
⭐ MUSIC'S CORE MECHANISM:

  TENSION:     V chord (dominant) — sounds "not done", "suspended"
  RESOLUTION:  I chord (tonic)    — sounds "complete", "home"

  Examples:
    G7 → C       (dominant 7th → tonic = classic resolution)
    Dm → G → C  (ii-V-I = tension build → resolution)

→ An entire piece of music = a chain of TENSION → RESOLUTION repeating
→ Like: storytelling = conflict → resolution
→ Like: Imagine-Final = gap → build → complete

→ But music encodes tension-resolution DIRECTLY into harmonic structure
→ Listener FEELS tension-resolution UNCONSCIOUSLY, no label needed
→ This is what natural language CANNOT DO:
  "I feel tense and then relieved" = LABEL
  V → I = EXPERIENCE
```

---

## §7 — History of Development

```
TIMELINE — music notation did NOT always exist. Oral music came first, notation came later:

~40,000 BCE  Bone flutes — oldest instruments ever found
~3,000 BCE   Egypt, Mesopotamia: complex instruments (harp, lyre, drum)
~500 BCE     Pythagoras: frequency ratios, system of intervals
~1000 CE     Guido d'Arezzo (Italy): INVENTED staff notation + solfège (Do-Re-Mi)
              → BEFORE THIS: music was 100% ORAL (40,000 years!)
              → AFTER: music could be WRITTEN DOWN + TRANSMITTED without in-person meeting
              → ⭐ Equivalent leap: inventing writing for language
~1600s       Equal temperament: 12 evenly-spaced notes → enables free key modulation (Bach)
~1700-1800s  Classical period: complex forms (sonata, symphony, concerto)
~1900s       Jazz: improvisation + complex harmony (chord extensions, altered scales)
~1950s       Rock & Roll: simplified harmony, emphasized rhythm + energy
~1960-70s    Electronic music: synthesizer → creates NEW timbres that never existed before
~1980s       MIDI: digital encoding of music = numbers (note, velocity, duration)
              → Game dev: MIDI = the way to encode music for computers
~2000s+      DAW (Digital Audio Workstation): FL Studio, Ableton, Logic
              → Anyone can make music — "democratization" of creation

⭐ INSIGHTS FROM HISTORY:
  1. Music (ORAL) is ~35,000 years older than written language
  2. Music notation (WRITTEN) is ~4,000 years younger than text writing
  3. This means: music existed for 39,000 years WITHOUT notation
     → Music = primarily ORAL/EXPERIENTIAL, notation = secondary tool
     → Unlike math: math notation = essential (without notation, calculus is impossible)
     → Unlike language: writing = important but language works fine without it
  4. MIDI (1980s) = first time music was encoded as NUMBERS
     → Computers can "read" and "play" music
     → Game music: from chiptune (NES) → orchestral (modern AAA)
```

---

## §8 — Framework Lens + Open Questions

### §8.1 — Music in the Processing Layers Model

```
L0 (Body Input):    Hear sound (auditory) + feel beat in body (somatic)
L1 (Pattern Match): Recognize familiar melody, familiar chord, genre
L2 (Encoding):      Music notation format (notes, chords, key, tempo)
L3 (Processing):    Compose, arrange, improvise, analyze
L4 (Plan/Execute):  Perform (play music), compose (write music)

LISTENER (passive):  L0 → L1 (pattern match) → emotional response
                     → NO NEED for L2 or L3 to FEEL the music!
                     → This is what's UNIQUE: music does NOT REQUIRE symbol decoding

PERFORMER (active):  L0 → L1 → L2 (read notation) → L3 (interpret) → L4 (play)
                     → REQUIRES L2 (read notation) + L4 (motor skill)

COMPOSER (creative): L1 (inspiration) → L3 (compose, GENERATIVE) → L2 (encode) → L4 (write)
                     → REQUIRES heavy L3 (creative processing)

⭐ A music LISTENER needs neither L2 (notation) nor L3 (analysis):
  → 6-month-old infants already respond to music (rhythm, contour, consonance)
  → Listener experience = L0 → L1 → emotional response (bypass L2+L3)
  → This is UNIQUE: you CANNOT "listen" to a math equation and understand it
  → You CANNOT "listen" to a Japanese sentence and understand it (without knowing Japanese)
  → You CAN "listen" to Japanese music and FEEL it (universal emotional encoding)
```

### §8.2 — Open Questions

1. **Why does minor = sad, major = happy?** Innate or learned? Evidence: children as young as 4 distinguish major/minor (Kastner & Crowder 1990). Possible mechanism: different frequency ratios create different consonance/dissonance → different body response → association compiled early.

2. **Music + Memory**: why does an old song → strong memory flashback? Possible mechanism: music encodes a temporal-affective pattern → on replay → re-activates the full body state at the time of compilation. Like NT7: body state at compile determines chunk association.

3. **Rhythm → Motor coupling**: why does music make you want to move? Auditory cortex → motor cortex direct connection (Grahn & Brett 2007). Beat prediction = VTA dopamine alert → opioid reward on pattern match. Movement synchronization = social bonding (Hove & Risen 2009).

4. **Game music**: why does adaptive music (dynamic soundtrack) increase immersion? Because the music's emotional arc SYNCS with the gameplay emotional arc → reinforcement. Mismatch (happy music when you die, sad music when you win) → dissonance → breaks immersion.

5. **Music vs language evolution**: did music precede language (oral) or emerge simultaneously? Musilanguage hypothesis (Brown 2000): common ancestor → diverged into music (emotional) + language (semantic). Evidence: Broca's area processes BOTH music syntax and language syntax (Maess 2001).

### §8.3 — References

| Author | Year | Work | Relevance |
|---|---|---|---|
| Levitin, D. | 2006 | This Is Your Brain on Music | Music cognition overview |
| Huron, D. | 2006 | Sweet Anticipation | Expectation in music |
| Maess, B. et al. | 2001 | Musical syntax processed in Broca's area | Music-language neural overlap |
| Grahn, J. & Brett, M. | 2007 | Rhythm and beat perception | Auditory-motor coupling |
| Brown, S. | 2000 | Musilanguage hypothesis | Music-language common ancestor |
| Kastner & Crowder | 1990 | Major/minor perception in children | Early emotional encoding |
| Hove, M. & Risen, J. | 2009 | Synchrony and social bonding | Rhythm → social connection |
| Temperley, D. | 2001 | The Cognition of Basic Musical Structures | Computational music theory |

---

> **03-Musical-Notation-Architecture.md — End of file.**
>
> Music = communication format encoding temporal-affective patterns. Unique: listener does NOT NEED to decode notation to feel it. Cross-cultural without translation. Direct body entrainment.
>
> Version: v1.0, 2026-04-16.
