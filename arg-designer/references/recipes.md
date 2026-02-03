# Recipe Examples

Complete puzzle chain examples from real ARGs and design templates.

## Table of Contents
1. [Classic ARG Examples](#classic-arg-examples)
2. [Template Recipes](#template-recipes)
3. [Build-Your-Own Patterns](#build-your-own-patterns)
4. [Difficulty Calibration](#difficulty-calibration)

---

## Classic ARG Examples

### I Love Bees (2004)

**Campaign**: Xbox/Halo 2 marketing ARG

**Trailhead Chain**:
```
Xbox ad → Distorted URL visible → ilovebees.com
   ↓
Corrupted website → Hidden text in HTML
   ↓
GPS coordinates → Public payphones
   ↓
Scheduled calls → Audio recordings
   ↓
Collective puzzle solving → Story revelation
```

**Key Techniques**:
- Mass coordination (community answer phones)
- Real-world locations
- Time-based progression
- Corrupted website aesthetic

---

### Year Zero (2007)

**Campaign**: Nine Inch Nails album ARG

**Physical → Digital Flow**:
```
Concert t-shirt → Hidden text (highlighted letters)
   ↓
URL revealed → In-world resistance website
   ↓
USB drives left at concerts → MP3s + hidden data
   ↓
Spectrogram in audio → Image clues
   ↓
Phone numbers in songs → IVR system
```

**Key Techniques**:
- Album artwork integration
- Concert distribution
- Spectrogram hiding
- Dystopian corporate websites
- Found USB drives

---

### Cicada 3301 (2012-2014)

**Discovery Chain**:
```
4chan image post → Steganography extraction
   ↓
Hidden text → Book cipher (requires specific book)
   ↓
Decoded text → Phone number
   ↓
Voicemail → Another cipher + coordinates
   ↓
Physical posters (14 countries) → QR codes
   ↓
Tor hidden services → Advanced cryptography
```

**Key Techniques**:
- Layered steganography
- Book ciphers
- Global physical distribution
- Progressive difficulty escalation
- Anonymity/Tor integration

---

### Marble Hornets (2009-2014)

**YouTube Series Structure**:
```
Entry #1 (video) → Creepy found footage
   ↓
Comments hint at totheark channel
   ↓
totheark response videos → Visual puzzles
   ↓
Audio distortion → Spectrogram messages
   ↓
Twitter accounts → Real-time interaction
```

**Key Techniques**:
- Found footage format
- Secondary antagonist channel
- Long-form narrative
- Minimal but impactful interactivity
- Community theory-building

---

### The Sun Vanished (2018-ongoing)

**Twitter Thread ARG**:
```
Tweet: "The sun didn't rise this morning" → Establishes premise
   ↓
Photo/video tweets → Visual evidence
   ↓
Community questions → Character responses
   ↓
Phone number in video → Voicemail clues
   ↓
Coordinates → Google Maps discoveries
```

**Key Techniques**:
- Real-time Twitter narrative
- Responsive to community
- Multimedia integration
- Sustained long-term engagement

---

## Template Recipes

### Recipe 1: The Document Drop

**Premise**: Leaked corporate documents reveal dark secrets

```
TRAILHEAD: Reddit post "found this in a dumpster"
   ↓ [Platform: Reddit, Imgur]
STAGE 1: Scanned documents with redacted text
   → Adjust brightness to see through redactions
   ↓ [Hiding: Image adjustment]
STAGE 2: Visible text contains cipher
   → Decode Vigenère (key hidden in letterhead)
   ↓ [Cipher: Vigenère]
STAGE 3: Decoded message reveals email address
   → Email to character gets autoresponse
   ↓ [Platform: Email]
STAGE 4: Autoresponse has attachment
   → Password-protected ZIP
   ↓ [Connector: Password]
STAGE 5: Password from combining previous clues
   → ZIP contains next document + audio
   ↓ [Content: Multi-format]
```

**Difficulty**: Medium | **Duration**: 1-2 weeks | **Budget**: Low

---

### Recipe 2: The Phone Trail

**Premise**: Mysterious voicemails lead deeper into conspiracy

```
TRAILHEAD: QR code in YouTube video description
   ↓ [Platform: YouTube → Web]
STAGE 1: QR leads to static website with phone number
   → Call number, hear IVR menu
   ↓ [Platform: Twilio]
STAGE 2: IVR requires numeric password
   → Password hidden in website source code
   ↓ [Hiding: HTML comments]
STAGE 3: Correct password plays voicemail
   → Message contains Morse code beeps
   ↓ [Cipher: Morse]
STAGE 4: Morse decodes to "PRESS STAR 73"
   → Unlocks new IVR branch
   ↓ [Connector: Phone menu]
STAGE 5: New branch reveals location + time
   → Next stage is time-gated
   ↓ [Gate: Time-based]
```

**Difficulty**: Medium-Hard | **Duration**: 2-3 weeks | **Budget**: Medium ($5-20/month for Twilio)

---

### Recipe 3: The Social Media Investigation

**Premise**: Character's social accounts tell disturbing story

```
TRAILHEAD: Character mentions @suspicious_account
   ↓ [Platform: Twitter/Instagram]
STAGE 1: Account has cryptic posts with images
   → EXIF data contains coordinates
   ↓ [Hiding: Metadata]
STAGE 2: Coordinates lead to unlisted YouTube video
   → Video has spectrogram hidden in audio
   ↓ [Platform: YouTube → Audacity]
STAGE 3: Spectrogram shows Discord invite code
   → Join server as "archived" member
   ↓ [Platform: Discord]
STAGE 4: Discord has hidden channel accessed by role
   → Role given for solving puzzle posted in #general
   ↓ [Gate: Puzzle-solve]
STAGE 5: Hidden channel has final narrative reveals
   ↓ [Content: Story conclusion]
```

**Difficulty**: Medium | **Duration**: 1-3 weeks | **Budget**: Free

---

### Recipe 4: The Cipher Chain

**Premise**: Intercepted coded messages must be decrypted

```
TRAILHEAD: Pastebin link discovered in game files
   ↓ [Platform: Pastebin]
STAGE 1: Base64 encoded text
   → Decode to get ciphertext
   ↓ [Encoding: Base64]
STAGE 2: Ciphertext is Caesar cipher (shift 13)
   → Decodes to: "THE KEY IS HARMONY"
   ↓ [Cipher: ROT13]
STAGE 3: Another Pastebin with Vigenère cipher
   → Use "HARMONY" as key
   ↓ [Cipher: Vigenère]
STAGE 4: Decoded text is book cipher reference
   → Requires specific public domain book
   ↓ [Cipher: Book cipher]
STAGE 5: Book cipher reveals URL to next stage
   ↓ [Connector: URL]
```

**Difficulty**: Hard | **Duration**: 1 week | **Budget**: Free

---

### Recipe 5: The Found Footage Trail

**Premise**: Disturbing videos appear on anonymous channel

```
TRAILHEAD: "Found this channel" post on horror subreddit
   ↓ [Platform: Reddit → YouTube]
STAGE 1: YouTube videos with glitchy footage
   → Frame-by-frame analysis reveals hidden frames
   ↓ [Hiding: Frame insertion]
STAGE 2: Hidden frame contains partial URL
   → Combine URLs from multiple videos
   ↓ [Connector: URL fragments]
STAGE 3: Complete URL leads to Dropbox folder
   → Contains audio file
   ↓ [Platform: Dropbox]
STAGE 4: Audio played backwards reveals message
   → Message includes phone number
   ↓ [Hiding: Reversed audio]
STAGE 5: Phone number leads to voicemail
   → Voicemail is character in distress
   ↓ [Platform: Twilio/Google Voice]
```

**Difficulty**: Medium | **Duration**: 2-4 weeks | **Budget**: Low

---

## Build-Your-Own Patterns

### The Basic Framework

```
[HOOK] → [DISCOVERY] → [PUZZLE] → [REWARD] → [NEXT HOOK]
```

Fill in each component:

| Component | Options |
|-----------|---------|
| HOOK | Social post, video, website, physical item |
| DISCOVERY | Source code, metadata, visual analysis, audio analysis |
| PUZZLE | Cipher, steganography, logic puzzle, coordination |
| REWARD | Story content, character interaction, new access |
| NEXT HOOK | URL, phone, coordinates, username |

### Connector Chains

**Easy Chain** (Difficulty 1-2):
```
QR Code → Website → HTML Comment → URL → New Website
```

**Medium Chain** (Difficulty 2-3):
```
Video → Spectrogram → Image → EXIF GPS → Location Name → Social Account
```

**Hard Chain** (Difficulty 3-4):
```
Document → Caesar Cipher → Base64 → Vigenère → Book Cipher → Final Text
```

**Expert Chain** (Difficulty 4-5):
```
Image LSB → Binary → Custom Cipher → Phone IVR → Multi-choice → Coordinates → Physical Drop
```

---

## Difficulty Calibration

### Player Skill Assumptions by Level

**Level 1 (Casual)**:
- Can view source code
- Knows to adjust image brightness
- Can Google cipher names
- Has basic social media accounts

**Level 2 (Engaged)**:
- Familiar with common ciphers
- Can use Audacity for spectrograms
- Will check metadata with online tools
- Willing to make phone calls

**Level 3 (Experienced)**:
- Knows steganography concepts
- Can write simple scripts
- Familiar with ARG conventions
- Will coordinate with community

**Level 4 (Expert)**:
- Can crack unknown ciphers
- Reverse engineering capability
- Deep technical knowledge
- Persistent over long time

### Time Estimates by Puzzle Type

| Puzzle Type | Solo Time | Community Time |
|-------------|-----------|----------------|
| View source | 2-5 min | <1 min |
| Simple cipher | 10-30 min | 5-15 min |
| Spectrogram | 15-45 min | 10-20 min |
| Complex cipher chain | 1-4 hours | 30-60 min |
| Steganography | 30 min - 2 hours | 15-45 min |
| Coordination puzzle | N/A | 1-12 hours |

### Stuck Prevention

**Early Warning Signs**:
- No progress for 2x expected time
- Community frustration visible
- Wrong solution paths being explored
- Decreased engagement

**Intervention Options**:
1. Hint via character account (in-world)
2. New related content that illuminates
3. Community manager nudge (soft out-of-world)
4. Time-based unlock (automatic)

**Hint Progression**:
```
Wait time → Subtle hint → Clearer hint → Solution-adjacent → Answer
   ↑           ↑             ↑                ↑              ↑
 2 hours    4 hours       8 hours        12 hours      24 hours
```
