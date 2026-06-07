---
title: Musical Notation Architecture — Music as a Language System
created: 2026-04-16 (N+5 exploration session)
status: REFERENCE — read and study at leisure
scope: Music as a language system — notation, syntax, structure, comparison with natural language + math
purpose: Understand music notation as a communication format — what it encodes that natural language and math CANNOT
parent: ../../plan.md (F3 Chunk-External-Development)
language: English
source_version: Vietnamese v1.0
english_created: 2026-06-06
note: Written for those who LISTEN to music daily but have never "dissected" the structure of its notation
---

# Musical Notation Architecture — Music as a Language System

> **Purpose**: You listen to music every day but may have never looked at music notation as a LANGUAGE SYSTEM. This file "dissects" the structure — not to teach music theory, but to reveal music as a communication format that encodes something natural language and math CANNOT: **temporal-affective patterns** (emotional patterns over time).
>
> **Comparison with previous files**: File 01 = natural language (broadest). File 02 = math (most precise). This file = music (most temporally-affective).

---

## TABLE OF CONTENTS

- §1 — Musical "vocabulary": Core components
- §2 — Musical "grammar": How components combine
- §3 — Hierarchy: Note → Measure → Phrase → Section → Full piece
- §4 — The notation system: Staff notation
- §5 — Comparison: Music vs Natural Language vs Math
- §6 — What music encodes that other formats CANNOT
- §7 — History of development
- §8 — Framework lens + Open questions

---

## §1 — Musical "vocabulary": Core components

### §1.1 — Pitch = The "Noun" — WHAT IT REFERS TO

```
PITCH = how high or low a sound is

12 NOTES in 1 octave:
  C  C#  D  D#  E  F  F#  G  G#  A  A#  B
  Do Do# Re Re# Mi Fa Fa# Sol Sol# La La# Si

  → After B, returns to C (one octave higher): C₃ → C₄ → C₅
  → Piano has ~88 keys = ~7 octaves
  → Human hearing range: ~20 Hz (very low) → ~20,000 Hz (very high)

  ⭐ WHY 12 NOTES?
  → Frequency ratio: each note is × ¹²√2 ≈ 1.0595 above the previous
  → 12 notes × ¹²√2 = ×2 → one octave = double the frequency
  → A₄ = 440 Hz, A₅ = 880 Hz (exactly double)
  → 12-note equal temperament standardized ~1600s (Bach era)

NAMING SYSTEMS:
  Letter system (English/International): C D E F G A B
  Solmization (Italian/international):   Do Re Mi Fa Sol La Si
  Numeric (MIDI):                        60 62 64 65 67 69 71 (C₄ = 60)
  → Game devs know MIDI numbers: each note = 1 integer
```

### §1.2 — Duration = "Tense" — HOW LONG

```
DURATION = how long a note is held

  𝅝  Whole note     = 4 beats
  𝅗𝅥  Half note      = 2 beats
  ♩  Quarter note   = 1 beat
  ♪  Eighth note    = 1/2 beat
  ♬  Sixteenth note = 1/4 beat

  → Each level = HALVES the previous (1 → 1/2 → 1/4 → 1/8 → 1/16)
  → BINARY system — like computers!

ADDITIONAL SYMBOLS:
  Dotted note:   ♩.  = 1 + 1/2 = 1.5 beats (adds half of its own value)
  Tied note:      ♩‿♩ = 1 + 1 = 2 beats (connects 2 notes of the same pitch)
  Rest:           𝄾 = 1 beat of silence (NOT PLAYING — but SILENCE IS MUSIC TOO!)

  ⭐ "Silence is music" — Debussy
  → Rest = a "nothing" chunk — but ESSENTIAL to rhythm
  → Like: spaces between words are ESSENTIAL for reading comprehension
```

### §1.3 — Rhythm = "Grammar of time"

```
TIME SIGNATURE = defines the temporal structure

  4/4  = 4 beats per measure, quarter note = 1 beat
         → MOST COMMON. Pop, rock, classical all use it.
         → "Common time" — written as C

  3/4  = 3 beats per measure → WALTZ rhythm (1-2-3, 1-2-3)
  6/8  = 6 eighth notes per measure → compound rhythm (1-2-3-4-5-6)
  2/4  = 2 beats → march (1-2, 1-2)
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
  → Game dev analogy: frame rate. 120 BPM ≈ 2 beats/second
  → Rhythm game: timing window typically ±50ms per beat

⭐ RHYTHM = a structure that NATURAL LANGUAGE LACKS:
  → Written text has NO fixed beat (flexible timing)
  → Music HAS a fixed beat (rigid timing) — this is why music "draws you in"
  → Beat = an expectation pattern: the brain PREDICTS the next beat
    → VTA dopamine alert on confirmed prediction → opioid (coherence reward)
      when pattern matches
    (⚠️ Dopamine = alert/salience. Opioid = actual pleasure. Ref: 03-Reward.md)
```

### §1.4 — Dynamics = "Volume" — LOUD or SOFT

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

  crescendo  (cresc.) <   = gradually getting louder
  decrescendo (decresc.) > = gradually getting softer
  sforzando (sfz)          = suddenly loud (strong accent)

→ Dynamics = EMOTIONAL INTENSITY
→ pp → ff = from whisper to shout
→ Crescendo = emotional build-up → climax
→ Natural language HAS dynamics but CANNOT notate them precisely
```

### §1.5 — Harmony = "Context" — multiple notes AT ONCE

```
CHORD = multiple notes played SIMULTANEOUSLY

Basic chords (triads):
  C major:      C - E - G    → sounds BRIGHT, HAPPY
  C minor:      C - Eb - G   → sounds DARK, SAD
  C diminished: C - Eb - Gb  → sounds TENSE
  C augmented:  C - E - G#   → sounds UNSTABLE, STRANGE

  ⭐ Major vs Minor:
  → Differ by ONLY 1 NOTE (E vs Eb — a half-step apart)
  → But the EMOTIONAL EFFECT is COMPLETELY DIFFERENT (happy vs sad)
  → This is what math and natural language CANNOT directly encode:
    "A feeling of mild sadness" = 5 words of natural language, imprecise description
    Cm chord = 3 notes, encodes that EMOTION precisely

CHORD PROGRESSION:
  I - V - vi - IV  (in C major: C - G - Am - F)
  → The MOST COMMON progression in pop music
  → "Let It Be", "No Woman No Cry", "Someone Like You",...
  → HUNDREDS of songs use the SAME 4 chords, with different melodies + lyrics

  V → I  = Resolution — sounds "finished", "home"
  IV → V = Build-up — sounds "about to arrive", "in anticipation"
  vi     = Relative minor — sounds "gently sad", "reflective"

→ Chord progression = EMOTIONAL ARC encoded in harmonic structure
→ This is an EMOTIONAL STRUCTURE that only music can encode directly
```

### §1.6 — Melody = "Story" — a sequence of notes over time

```
MELODY = a sequence of single notes over time forming a "musical sentence"

Properties:
  Contour:   rising, falling, flat, rising then falling,...
  Range:     from lowest to highest note
  Intervals: distance between successive notes

  → Melody = combined sequence of pitch + rhythm
  → Like: "sentence" = combined sequence of words + grammar

⭐ MELODY = WHAT PEOPLE REMEMBER:
  → Ask "how does that song go?" → people SING THE MELODY (not the chords)
  → Melody = the "foreground"
  → Harmony = the "background" (provides emotional context)
  → Rhythm = the "skeleton" (holds the structure)
```

### §1.7 — Timbre = "Unique voice" — WHO is playing

```
TIMBRE = the QUALITY of sound — same note, different instrument = different feeling

  Piano C₄         = sounds "clear, bright, clean"
  Violin C₄        = sounds "smooth, vibrant, warm"
  Trumpet C₄       = sounds "bright, strong, direct"
  Flute C₄         = sounds "clear, light, airy"
  Guitar C₄        = sounds "warm, round, intimate"
  Synthesizer C₄   = sounds "anything at all" (can produce any timbre)

→ Timbre is NOT well captured in notation (hard to write as symbols)
→ Only noted by naming the instrument: "Violin", "Flute", "Piano"
→ Game dev: timbre = sound design, waveform, ADSR envelope
→ This is a limitation of music notation: encodes pitch + rhythm well,
  encodes timbre ONLY indirectly (through instrument name)
```

---

## §2 — Musical "grammar": How components combine

### §2.1 — Scale = "Permitted vocabulary" for a given piece

```
From 12 notes, each piece selects 7 notes as its "vocabulary":

  C Major scale:    C D E F G A B     (all white keys on piano)
  C Minor scale:    C D Eb F G Ab Bb  (differs in 3 notes → COMPLETELY different feeling)
  A Minor scale:    A B C D E F G     (same notes as C Major, but starting from A!)

  Pentatonic:       C D E G A         (5 notes — Chinese music, Celtic, blues)
  Blues scale:      C Eb F F# G Bb    (adds the "blue note" F#)
  Whole tone:       C D E F# G# A#   (notes equally spaced → sounds "dreamy, floating")

→ Scale = a set of "permitted vocabulary", like the word bank of a specific language
→ Major = "happy vocabulary", Minor = "sad vocabulary"
→ Pentatonic = "simple, universal vocabulary" (children's songs, folk music worldwide)
→ Playing a note OUTSIDE the scale = "grammatical error" (tension) or "creative choice" (jazz)
```

### §2.2 — Key = The "language" of a piece

```
KEY = scale + root note (tonic)

  Key of C Major = uses C Major scale, C is "home" (the tonic)
  Key of G Major = uses G Major scale (G A B C D E F#), G is "home"
  Key of A Minor = uses A Minor scale, A is "home"

KEY SIGNATURE (written at the start of each staff):
  Shows how many # or b markings
  → Tells the reader which "language" (set of notes) this piece uses

  0 accidentals  = C Major / A Minor
  1 #            = G Major / E Minor
  2 #            = D Major / B Minor
  ...
  1 b            = F Major / D Minor
  2 b            = Bb Major / G Minor
  ...

→ Total: 12 major keys + 12 minor keys = 24 musical "languages"
→ Modulation (key change) = "switching languages" mid-piece
  → Example: final section of a song moves up a half-step = upward modulation → feeling of "exhilaration"
```

### §2.3 — Counterpoint + Voice Leading = "Multi-voice grammar"

```
COUNTERPOINT = multiple melodies SIMULTANEOUSLY, each with its own logic

  → Like: 2 people talking at the same time, EACH SENTENCE has its own meaning,
    but COMBINED they sound beautiful
  → Bach = master of counterpoint: 2-4 voices simultaneously, each beautiful on its own

VOICE LEADING = how to MOVE from one chord to the next
  → Each note in a chord moves the SHORTEST DISTANCE POSSIBLE to the next chord's note
  → "Smooth" transition = good voice leading
  → "Jumping around randomly" = bad voice leading (sounds uncomfortable)

→ Counterpoint = the most complex "grammar" in music
→ Equivalent to: writing a paragraph where EVERY LINE read horizontally makes sense,
  AND reading VERTICALLY also makes sense (acrostic poem × 4!)
```

---

## §3 — Hierarchy: Note → Measure → Phrase → Section → Full piece

```
LEVEL 1 — NOTE = "Word"
  C₄ quarter note = 1 C note, 1 beat
  → Smallest atom: pitch + duration

LEVEL 2 — MOTIF = "Phrase"
  Beethoven 5th: ♩♩♩𝅗𝅥 (da-da-da-DAAA)
  → 3-7 notes forming the smallest recognizable "musical idea"
  → Motif = the "DNA" of a piece — repeated and varied throughout

LEVEL 3 — PHRASE = "Sentence"
  Typically 4-8 measures
  → One "musical breath" — where a singer breathes, where a violinist changes bow direction
  → Has a "comma" (half cadence) or "period" (full cadence)

LEVEL 4 — PERIOD / SECTION = "Paragraph"
  A section (verse), B section (chorus), C section (bridge)
  → 2-4 phrases grouped into 1 section
  → Each has its own character: verse = storytelling, chorus = climax

LEVEL 5 — FORM = "Essay"
  Verse-Chorus:        ABABCB (most common pop song form)
  Sonata:              Exposition - Development - Recapitulation (classical)
  12-bar blues:        I-I-I-I-IV-IV-I-I-V-IV-I-V (blues/jazz)
  Rondo:               ABACADA (classical)
  Theme & Variations:  A-A'-A''-A'''... (theme with variations)

LEVEL 6 — OPUS / ALBUM = "Book"
  Symphony: 4 movements (each movement = its own form)
  Album: 10-15 pieces with linked themes
  Opera: 3-4 acts, each act has many scenes, each scene has multiple arias

MAPPING TO FRAMEWORK:
  Level 1 Note     ↔ Chunk (atom)
  Level 2 Motif    ↔ Chunk compound
  Level 3 Phrase   ↔ Chunk chain
  Level 4 Section  ↔ Schema
  Level 5 Form     ↔ Plan (goal structure: build → climax → resolve)
  Level 6 Opus     ↔ Domain knowledge (full system)
```

---

## §4 — The notation system: Staff notation

```
STAFF = 5 horizontal lines — the "ruled paper" of music

  ───── F₅ (note on line 5)
  ───── D₅
  ───── B₄
  ───── G₄
  ───── E₄ (note on line 1)

  → Notes placed ON a line or IN a space between lines = determines pitch
  → HIGHER on staff = HIGHER pitch
  → Treble clef (𝄞): for high notes (right hand of piano, violin, singers)
  → Bass clef (𝄢): for low notes (left hand of piano, cello, bass)

READ LEFT → RIGHT = TIME PASSING:
  → X axis = time (left = earlier, right = later)
  → Y axis = pitch (bottom = low, top = high)
  → This is a 2D GRAPH: pitch × time

SYMBOLS ON STAFF:
  𝄞  Treble clef
  𝄢  Bass clef
  ♩  Quarter note
  ♪  Eighth note
  𝅝  Whole note
  𝄾  Quarter rest
  #  Sharp (raise by a half-step)
  b  Flat (lower by a half-step)
  ♮  Natural (cancel a sharp or flat)
  𝄀  Barline (divides measures)
  𝄂  Double barline (end of piece)

→ Staff notation = 2D GRAPH (pitch × time) + annotations (dynamics, tempo,...)
→ Invented ~1000 CE (Guido d'Arezzo, Italy) — before that, music was transmitted orally!
→ Staff notation is NOT perfect:
  ✅ Encodes WELL: pitch, duration, dynamics, structure
  🟡 Encodes ADEQUATELY: articulation, phrasing
  ❌ Encodes POORLY: timbre, emotion, "feel", groove, microtiming
  → This is why: 2 pianists playing the SAME piece sound DIFFERENT — notation doesn't capture everything
```

---

## §5 — Comparison: Music vs Natural Language vs Math

| Feature | Natural Language | Math | Music |
|---|---|---|---|
| **Primary encoding** | Meaning (semantics) | Quantity + Relation | Temporal-Affective patterns |
| **"Vocabulary"** | ~5,000-10,000 words | ~150 symbols | 12 notes + duration + dynamics |
| **Ambiguity** | High (polysemous) | None | Medium (interpretive) |
| **Precision** | Low-Medium | Extreme | High for pitch/rhythm, low for emotion |
| **Temporal structure** | Not fixed | No temporal dimension | ⭐ FIXED (beat, tempo) |
| **Emotional encoding** | Indirect (word "sadness") | None | ⭐ DIRECT (minor chord = sadness) |
| **Multi-voice** | 1 idea at a time (sequential) | 1 equation at a time | ⭐ MANY voices simultaneously |
| **Shareability** | Requires shared language | Global | ⭐ Global (transcends language!) |
| **Body response** | Low-Medium | Low | ⭐ HIGH (rhythm → movement) |
| **Recursion** | 3-4 layers | Unlimited | Limited (nested forms) |
| **Cultural variation** | Very large | Nearly none | Moderate (differing scale systems) |
| **Requires training** | No (L1 natural) | Yes (formal) | Partial (listening natural, playing requires training) |
| **Writing system age** | ~5,000 years | ~3,000 years | ~1,000 years |
| **Age of system** | ~100,000+ years (spoken) | ~5,000 years (notation) | ~40,000+ years (singing/drumming) |

```
WHAT IS UNIQUE ABOUT MUSIC that the other 2 formats LACK:

1. ⭐ TEMPORAL PRECISION: Music has an EXACT beat (±ms)
   → Natural language: timing is flexible, no fixed beat
   → Math: no time dimension
   → Music: 120 BPM = exactly 500ms per beat

2. ⭐ DIRECT EMOTIONAL ENCODING:
   → Natural language: "I am sad" = a LABEL for emotion (indirect)
   → Math: encodes no emotion
   → Music: Cm chord = DIRECTLY triggers sadness (no label needed)

3. ⭐ MULTI-VOICE SIMULTANEITY:
   → Natural language: only 1 idea at a time (sequential)
   → Math: only 1 equation at a time
   → Music: 4-part harmony = 4 "sentences" SIMULTANEOUSLY, each meaningful on its own

4. ⭐ BODY ENTRAINMENT:
   → Hearing music → the body AUTOMATICALLY sways with the beat
   → Nobody reads an equation and nods their head in time
   → Nobody hears a news broadcast and dances
   → Music → motor cortex DIRECTLY (rhythm → movement coupling)

5. ⭐ CROSS-CULTURAL WITHOUT TRANSLATION:
   → Hear Japanese music: you can FEEL IT even without knowing Japanese
   → Read a Japanese book: you understand NOTHING without knowing the language
   → Music bypasses language barriers → emotional content is largely universal
```

---

## §6 — What music encodes that other formats CANNOT

### §6.1 — Emotional arc (affective trajectory)

```
A PIECE OF MUSIC = A STRUCTURED EMOTIONAL TRAJECTORY:

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
→ But music ENACTS it — the listener EXPERIENCES the arc, not just reads about it
```

### §6.2 — Tension-Resolution

```
⭐ THE CORE MECHANISM OF MUSIC:

  TENSION:     V chord (dominant) — sounds "unfinished", "suspended"
  RESOLUTION:  I chord (tonic)    — sounds "finished", "home"

  Example: G7 → C     (dominant 7th → tonic = classic resolution)
           Dm → G → C  (ii-V-I = tension build → resolution)

→ An entire piece of music = a repeated chain of TENSION → RESOLUTION
→ Like: storytelling = conflict → resolution
→ Like: Imagine-Final = gap → build → complete

→ But music encodes tension-resolution DIRECTLY into harmonic structure
→ The listener FEELS tension-resolution UNCONSCIOUSLY, without needing a label
→ This is what natural language CANNOT DO:
  "I feel tense and then relieved" = a LABEL
  V → I = an EXPERIENCE
```

---

## §7 — History of development

```
TIMELINE — musical notation was NOT always there. It had to be INVENTED:

~40,000 BCE  Bone flutes — oldest instruments found
~3,000 BCE   Egypt, Mesopotamia: complex instruments (harp, lyre, drum)
~500 BCE     Pythagoras: frequency ratios, system of intervals
~1000 CE     Guido d'Arezzo (Italy): INVENTED staff notation + solmization (Do-Re-Mi)
              → BEFORE THIS: music transmitted ENTIRELY ORALLY (40,000 years!)
              → AFTER THIS: music could be WRITTEN DOWN + TRANSMITTED without face-to-face contact
              → ⭐ Leap equivalent to: the invention of writing for language
~1600s       Equal temperament: 12 notes tuned equally → allows free key modulation (Bach)
~1700-1800s  Classical period: complex forms (sonata, symphony, concerto)
~1900s       Jazz: improvisation + complex harmony (chord extensions, altered scales)
~1950s       Rock & Roll: simplified harmony, emphasized rhythm + energy
~1960-70s    Electronic music: synthesizer → creates NEW timbres that never existed before
~1980s       MIDI: digital encoding of music = numbers (note, velocity, duration)
              → Game dev: MIDI = how music is encoded for computers
~2000s+      DAW (Digital Audio Workstation): FL Studio, Ableton, Logic
              → Anyone can create music — "democratization" of music creation

⭐ INSIGHTS FROM HISTORY:
  1. Music (ORAL) predates written language by ~35,000 years
  2. Music notation (WRITTEN) appeared ~4,000 years after text writing
  3. This means: music existed for 39,000 years WITH NO NOTATION
     → Music = primarily ORAL/EXPERIENTIAL, notation = secondary tool
     → Unlike math: math notation = essential (without notation, calculus is impossible)
     → Unlike language: writing = important but language functions fine without it
  4. MIDI (1980s) = the first time music was encoded as NUMBERS
     → Computers could "read" and "play" music
     → Game music: from chiptune (NES) → full orchestral (modern AAA)
```

---

## §8 — Framework Lens + Open Questions

### §8.1 — Music in the Processing Layers model

```
L0 (Body Input):    Hearing sound (auditory) + feeling the beat (somatic)
L1 (Pattern Match): Recognizing familiar melody, familiar chords, genre
L2 (Encoding):      Music notation format (notes, chords, key, tempo)
L3 (Processing):    Composing, arranging, improvising, analyzing
L4 (Plan/Execute):  Performing (playing music), composing (writing music)

LISTENER (passive):  L0 → L1 (pattern match) → emotional response
                     → DOES NOT NEED L2 or L3 to FEEL the music!
                     → This is a UNIQUE feature: music REQUIRES NO SYMBOL DECODING

PERFORMER (active):  L0 → L1 → L2 (read notation) → L3 (interpret) → L4 (play)
                     → NEEDS L2 (read notation) + L4 (motor skill)

COMPOSER (creative): L1 (inspiration) → L3 (compose, GENERATIVE) → L2 (encode) → L4 (write)
                     → NEEDS heavy L3 (creative processing)

⭐ A music LISTENER needs neither L2 (notation) nor L3 (analysis):
  → Infants at 6 months already respond to music (rhythm, contour, consonance)
  → Listener experience = L0 → L1 → emotional response (bypasses L2+L3)
  → This is something UNIQUE: you CANNOT "hear" a math equation and understand it
  → You CANNOT "hear" a Japanese sentence and understand it (without knowing the language)
  → You CAN "hear" Japanese music and FEEL IT (universal emotional encoding)
```

### §8.2 — Open questions

1. **Why does minor = sad, major = happy?** Is this innate or learned? Evidence: children as young as 4 already distinguish major/minor (Kastner & Crowder 1990). One possible mechanism: frequency ratios produce differing consonance/dissonance → different body responses → associations compiled early in development.

2. **Music + Memory**: why does hearing an old song trigger strong flashback memories? Possible mechanism: music encodes temporal-affective patterns → when replayed → re-activates the entire body state at the time of compilation. Like Convergence Point 7: body state at compile determines chunk association.

3. **Rhythm → Motor coupling**: why does music make us want to move? Auditory cortex → motor cortex connection is direct (Grahn & Brett 2007). Beat prediction = VTA dopamine alert → opioid reward when pattern matches. Movement synchronization = social bonding (Hove & Risen 2009).

4. **Game music**: why does adaptive music (dynamic soundtrack) increase immersion? Because the music's emotional arc SYNCS with the gameplay's emotional arc → reinforcement. A mismatch (happy music when dying, sad music when winning) → dissonance → breaks immersion.

5. **Music vs language evolution**: did music precede language (oral) or did they co-evolve? Musilanguage hypothesis (Brown 2000): a common ancestor → diverged into music (emotional) + language (semantic). Evidence: Broca's area processes BOTH music syntax and language syntax (Maess 2001).

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
> Music = communication format encoding temporal-affective patterns. Uniquely: the listener does NOT need to decode notation to feel the music. Cross-cultural without translation. Direct body entrainment.
>
> ✅ English primary throughout
>
> Version: v1.0, 2026-04-16.
