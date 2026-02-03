# Connectors Reference

Methods for linking ARG puzzle elements together in cohesive chains.

## Table of Contents
1. [Connector Types](#connector-types)
2. [Output → Input Patterns](#output--input-patterns)
3. [Confirmation Mechanisms](#confirmation-mechanisms)
4. [Branching and Gating](#branching-and-gating)
5. [Chain Design Principles](#chain-design-principles)

---

## Connector Types

### Direct Connectors
The output of puzzle A is directly usable as input for puzzle B.

| Type | Example | Flow |
|------|---------|------|
| URL reveal | Decode cipher → get URL | Text → Navigation |
| Password | Solve puzzle → archive password | Text → Access |
| Coordinates | Decode location → GPS point | Numbers → Location |
| Phone number | Hidden number → call it | Numbers → Audio |
| Username/handle | Discover name → find account | Text → Profile |
| Email address | Reveal email → send message | Text → Communication |
| File path | Decode path → access file | Text → Content |

### Indirect Connectors
The output requires interpretation or combination before use.

| Type | Example | Flow |
|------|---------|------|
| Keyword for cipher | Find word → use as Vigenère key | Text → Decode key |
| Combination elements | Collect 3 numbers → form code | Multiple → Single |
| Reference lookup | Get page number → find in book | Number → Text |
| Image identification | Decode location name → find image of it | Text → Visual |
| Time-based | Decode time → watch at that timestamp | Number → Event |

### Contextual Connectors
Understanding from one puzzle provides context for another.

| Type | Example | Flow |
|------|---------|------|
| Character knowledge | Learn character name → recognize elsewhere | Narrative → Recognition |
| Pattern recognition | See cipher style → recognize in new puzzle | Method → Application |
| Story context | Understand plot → interpret cryptic message | Narrative → Meaning |
| Symbol system | Learn symbol meanings → decode new message | System → Translation |

---

## Output → Input Patterns

### Text Outputs

**Text → URL**
```
Puzzle output: "Find the truth at harmony dot example dot com"
→ Navigate to harmony.example.com
```

**Text → Password**
```
Puzzle output: "WINTERMUTE"
→ Enter as archive password
```

**Text → Search Term**
```
Puzzle output: "Operation Midnight Sun"
→ Search for associated content
```

**Text → Username**
```
Puzzle output: "@dr_harmony_jones"
→ Find social media account
```

### Numeric Outputs

**Numbers → Phone**
```
Puzzle output: "5 5 5 0 1 2 3"
→ Call (555) 012-3
```

**Numbers → Coordinates**
```
Puzzle output: "34.0522 -118.2437"
→ GPS location (Los Angeles)
```

**Numbers → Date/Time**
```
Puzzle output: "03:14:15"
→ Watch video at 3:14:15 timestamp
```

**Numbers → Combination**
```
Puzzle output: "7-23-42"
→ Use as lock combination
```

### Visual Outputs

**Image → Location**
```
Puzzle output: Photo of landmark
→ Identify and visit/research location
```

**Image → QR Code**
```
Puzzle output: QR code revealed
→ Scan for URL/text
```

**Pattern → Template**
```
Puzzle output: Grid pattern
→ Apply to another puzzle as overlay
```

### Audio Outputs

**Audio → Transcription**
```
Puzzle output: Voicemail message
→ Transcribe and analyze text
```

**Audio → DTMF**
```
Puzzle output: Phone tones in recording
→ Decode to phone number
```

**Audio → Spectrogram**
```
Puzzle output: Mysterious audio
→ View in spectrogram for image
```

---

## Confirmation Mechanisms

Players need feedback that they're on the right track.

### Explicit Confirmation
| Method | Description |
|--------|-------------|
| Success message | "Access granted" or similar |
| New content unlock | Next puzzle becomes available |
| Character response | NPC acknowledges progress |
| Platform notification | Discord role, email reply |

### Implicit Confirmation
| Method | Description |
|--------|-------------|
| Content makes sense | Decoded text is coherent |
| Matches pattern | Fits established puzzle style |
| Connects to narrative | Relates to known story elements |
| Community consensus | Others confirm same solution |

### Confirmation Design

**Too Much Confirmation**: Breaks TINAG, removes mystery
```
BAD: "Congratulations! You solved level 1!"
```

**Too Little Confirmation**: Players unsure if correct
```
BAD: No response, no new content, nothing changes
```

**Just Right**: Organic confirmation within fiction
```
GOOD: Decoded message leads to working phone number
GOOD: Character account posts something new
GOOD: Archive extracts successfully
```

---

## Branching and Gating

### Linear Structure
```
A → B → C → D → E
```
- Simple to design
- Clear progression
- Can feel railroaded

### Hub Structure
```
    B
    ↑
A → HUB → C
    ↓
    D
```
- Central location with multiple paths
- Player choice in order
- All paths lead to same next stage

### Parallel Tracks
```
A1 → B1 → C1 ↘
                → MERGE → D
A2 → B2 → C2 ↗
```
- Multiple simultaneous paths
- Different skills/approaches
- Convergence point

### Gating Mechanisms

**Knowledge Gates**: Must have solved previous puzzle
```
"What was the name of Harmony's dog?"
→ Answer from earlier content
```

**Time Gates**: Content releases at scheduled time
```
"The next message arrives at midnight"
→ Real-time waiting
```

**Community Gates**: Requires collective action
```
"When 100 people call, the message changes"
→ Coordination needed
```

**Collection Gates**: Need multiple pieces
```
"Combine all four code fragments"
→ Parts from different puzzles
```

---

## Chain Design Principles

### The Puzzle Chain Formula

```
[CONTENT] → [HIDING] → [DISCOVERY] → [DECODE] → [CONNECT] → [NEXT]
```

Example chain:
```
Story fragment
  ↓ [HIDING: Spectrogram]
Audio file posted on SoundCloud
  ↓ [DISCOVERY: Trailhead points to account]
Players find audio
  ↓ [DECODE: View in Audacity]
Image reveals phone number
  ↓ [CONNECT: Call number]
Twilio IVR gives password
  ↓ [NEXT]
Password opens encrypted ZIP with next story fragment
```

### Difficulty Curve Patterns

**Ramping**: Each puzzle slightly harder
```
Difficulty: 1 → 2 → 3 → 4 → 5
Best for: Training players, building skills
```

**Wave**: Hard puzzles followed by easier ones
```
Difficulty: 2 → 4 → 2 → 5 → 3
Best for: Preventing fatigue, maintaining engagement
```

**Plateau**: Consistent difficulty with spikes
```
Difficulty: 3 → 3 → 3 → 5 → 3 → 3
Best for: Climactic moments, boss battles
```

### Chain Quality Checklist

**Flow**:
- [ ] Each puzzle has clear output
- [ ] Output usable as input for next
- [ ] No dead ends without intentional gating
- [ ] Confirmation at each step

**Balance**:
- [ ] Difficulty progression makes sense
- [ ] Mix of puzzle types
- [ ] Different skill requirements
- [ ] Rest points between hard puzzles

**Narrative**:
- [ ] Each step reveals story
- [ ] Connections feel organic
- [ ] TINAG maintained throughout
- [ ] World-building through puzzles

**Technical**:
- [ ] All platforms accessible
- [ ] Backups for third-party services
- [ ] Solutions documented
- [ ] Testing completed

### Common Chain Mistakes

**Orphaned Outputs**:
- Puzzle produces result with no use
- Players confused about purpose
- Fix: Every output should connect somewhere

**Logic Leaps**:
- Solution requires unjustified assumption
- Players stuck without clear direction
- Fix: Breadcrumb hints, multiple approaches

**Skill Cliffs**:
- Sudden dramatic difficulty spike
- Players abandon at chokepoint
- Fix: Gradual ramping, bypass options

**Single Point of Failure**:
- One platform down = entire ARG broken
- No alternative paths
- Fix: Redundancy, multiple entry points

---

## Quick Reference: Connector Selection

| Puzzle Output | Good Connectors | Avoid |
|---------------|-----------------|-------|
| Single word | Password, keyword, username | Too ambiguous |
| Long text | Search clue, cipher key, narrative | Direct URL (breaks) |
| Number sequence | Phone, coordinates, date | Arbitrary meaning |
| Image | Location ID, overlay, QR | Requires specific app |
| Audio | Spectrogram, transcript, DTMF | Obscure formats |
| URL | Navigation, redirect | Link rot |
| File | Contains next puzzle | Format compatibility |
