# ARG Skills for Claude

Skills for designing Alternate Reality Games (ARGs) with Claude.

## Installation

```bash
npx skills add https://github.com/greenie-neuko/arg-skills --skill arg-designer
```

## Available Skills

### arg-designer

Comprehensive ARG design toolkit for creating immersive puzzle experiences.

**Ciphers & Encoding (30+):**
- Beginner: Caesar, ROT13, Atbash, Reverse, A1Z26
- Intermediate: Vigenère, Rail Fence, Morse, Base64, Polybius, Pigpen
- Advanced: Playfair, Nihilist, Book Cipher, Baconian, Columnar Transposition
- Expert: XOR, Homophonic, Gematria Primus, Multi-layer custom systems

**Hiding Methods (60+):**
- Text: Unicode steganography, EXIF metadata, HTML comments, null bytes
- Image: LSB steganography, layer hiding, QR codes, brightness tricks
- Audio: Spectrograms, reversed audio, DTMF tones, phase cancellation
- Video: Frame insertion, subtitle tracks, timecode data
- File: Nested archives, polyglot files, alternate data streams

**Trailheads (40+):**
- Digital: Hidden pages, source code, 404 customization, robots.txt
- Physical: QR codes, geocaches, USB dead drops, event handouts
- Social: Character accounts, forum posts, "wrong number" contacts

**Design Theory:**
- TINAG (This Is Not A Game) philosophy
- Crimes Against Mimesis avoidance
- Puppetmaster role and real-time adaptation
- Player types (Organizers, Hunters, Detectives, Hackers, Collaborators)
- Difficulty curves (linear, wave, plateau)
- Hint systems and fatigue prevention
- Meta-puzzle structures and gating mechanics

**Case Studies:**
- I Love Bees (Halo 2 ARG)
- Cicada 3301
- Year Zero (Nine Inch Nails)
- The Beast
- Marble Hornets

**Included Scripts:**
- `cipher_tools.py` - Encode/decode 9 cipher types
- `steganography.py` - LSB image hiding, metadata, Unicode zero-width
- `spectrogram.py` - Convert images/text to audio spectrograms

**Recommended Tools:**
- dCode.fr, CyberChef, Boxentriq
- Binwalk, zsteg, Steghide, ExifTool
- Sonic Visualizer, Audacity

## Reference Files

| File | Content |
|------|---------|
| `ciphers.md` | 30+ ciphers with implementations |
| `hiding-methods.md` | 60+ techniques by content type |
| `trailheads.md` | 40+ entry point patterns |
| `connectors.md` | Puzzle linking methods |
| `platforms.md` | Discord, Twilio, YouTube setup |
| `design-principles.md` | TINAG, pacing, player types |
| `meta-puzzles.md` | Meta structures, gating, puzzle hunts |
| `recipes.md` | Complete chains from famous ARGs |

## Usage

Once installed, the skill triggers when you ask Claude about:
- Designing ARGs or puzzle trails
- Hiding messages with ciphers or steganography
- Creating trailheads and puzzle connections
- TINAG principles and ARG design theory
- Encoding/decoding specific cipher types
- Platform selection for ARG deployment

## License

MIT
