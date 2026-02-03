# Cipher Reference

Complete reference for ciphers commonly used in ARGs, organized by difficulty.

## Table of Contents
1. [Difficulty 1: Beginner](#difficulty-1-beginner)
2. [Difficulty 2: Intermediate](#difficulty-2-intermediate)
3. [Difficulty 3: Advanced](#difficulty-3-advanced)
4. [Difficulty 4: Expert](#difficulty-4-expert)
5. [Encoding Methods](#encoding-methods)
6. [Cipher Chaining](#cipher-chaining)

---

## Difficulty 1: Beginner

### Caesar Cipher
**Shift each letter by fixed amount**
- Implementation: `chr((ord(c) - 65 + shift) % 26 + 65)`
- ROT13 is Caesar with shift=13 (self-reciprocal)
- Hint patterns: "Shift your perspective", "13 steps forward"
- Tools: dcode.fr/caesar-cipher, CyberChef

### Atbash Cipher
**Mirror alphabet (A↔Z, B↔Y)**
- Implementation: `chr(155 - ord(c))` for uppercase
- Biblical origin provides narrative opportunities
- Hint patterns: "The last shall be first", "Mirror mirror"

### Reverse Text
**Simple backwards reading**
- Word-level vs character-level reversal
- Often combined with other methods
- Hint patterns: "Look back", "Reflect"

### Letter-Number Substitution
**A=1, B=2, C=3...**
- Variants: A=0 (programmer style), A=01 (padded)
- Phone keypad: 2=ABC, 3=DEF, etc.
- ASCII values for technical narratives

---

## Difficulty 2: Intermediate

### Vigenère Cipher
**Polyalphabetic with keyword**
- Each letter shifted by corresponding keyword letter
- Keyword often hidden elsewhere in ARG
- Kasiski examination can break if keyword reused
- Hint patterns: "The key is in the name", keyword hidden in previous puzzle

### Rail Fence Cipher
**Zigzag pattern across rails**
- 2-rail: alternating letters
- 3+ rails: wave pattern down and up
- Visualize: write diagonally, read horizontally
- Hint patterns: "Take the scenic route", "Zigzag"

### Morse Code
**Dots and dashes**
- Audio: short/long tones, taps, flashes
- Visual: binary patterns, on/off lights in video
- Variants: Fractionated Morse, inverted
- International vs American Morse

### Binary/Octal/Hex
**Number system encoding**
- Binary: 8 bits per ASCII character
- Octal: 3 digits per character (000-177)
- Hex: 2 digits per character (00-FF)
- Often hidden in "technical" documents

### Pigpen Cipher
**Geometric symbol substitution**
- Tic-tac-toe grids with dots
- Visual, works in images/drawings
- Freemason association for historical narratives

---

## Difficulty 3: Advanced

### Playfair Cipher
**5x5 grid, digraph substitution**
- Uses keyword to generate grid
- I/J combined, pairs of letters
- Rules: same row→shift right, same column→shift down, rectangle→swap corners
- Hint patterns: "Play fair", "Two by two"

### Nihilist Cipher
**Polybius square + keyword addition**
- Convert to 2-digit numbers via Polybius
- Add keyword numbers (mod arithmetic)
- Soviet/Cold War narrative potential

### Book Cipher
**Page/line/word references**
- Requires specific edition of text
- Format: page-line-word or page-line-character
- The book becomes the key
- Hint patterns: Reference to specific book in narrative

### Columnar Transposition
**Write in rows, read by column order**
- Keyword determines column read order
- Double transposition for added security
- Hint patterns: "Reorder your thoughts", "Columns of information"

### Substitution with Frequency Analysis
**Custom alphabet mapping**
- Solve with letter frequency (ETAOIN SHRDLU)
- Can use symbols, numbers, or invented alphabets
- Zodiac Killer style ciphers

---

## Difficulty 4: Expert

### Enigma-Style Rotors
**Multiple substitution layers with rotation**
- Simulated rotor machines
- Reflector creates reciprocal property
- Historical WWII narrative connection

### One-Time Pad (Simulated)
**Truly random key as long as message**
- Provide key separately in ARG
- Unbreakable if key truly random and single-use
- XOR operation for digital implementation

### Bifid/Trifid Ciphers
**Polybius coordinates combined**
- Split coordinates, recombine
- Fractionation obscures frequency

### Steganographic Ciphers
**Hidden within other content**
- First letters of words/sentences (acrostic)
- Nth word/letter selection
- Bacon's cipher (two typefaces)
- Null cipher (specific word positions)

### Multi-Layer Custom
**Combine multiple methods**
- ARG-specific invented systems
- Requires discovery of encoding method
- "Cicada 3301" style novel cryptography

---

## Encoding Methods

### Base64
**6-bit groups to printable ASCII**
- Padding: = or == at end
- Recognizable: A-Z, a-z, 0-9, +, /
- Variant: URL-safe Base64 (- and _ instead of + and /)

### Base32
**5-bit groups, uppercase only**
- Characters: A-Z, 2-7
- More padding than Base64
- Often used in TOTP codes

### URL Encoding
**Percent-encoding for URLs**
- %20 = space, %2F = /
- Double-encoding for extra obscurity

### HTML Entities
**Character references in HTML**
- Named: `&amp;` Numbered: `&#65;`
- Hide in web page source

### Unicode Tricks
**Zero-width characters**
- ZWSP (U+200B), ZWNJ (U+200C), ZWJ (U+200D)
- Invisible in rendered text
- Binary data in character sequence

---

## Cipher Chaining

### Effective Chains (increasing difficulty)
1. `Reverse → Caesar` (Difficulty: 1.5)
2. `Base64 → Caesar` (Difficulty: 2)
3. `Morse → Vigenère` (Difficulty: 3)
4. `ROT13 → Base64 → Vigenère` (Difficulty: 3.5)
5. `Binary → Rail Fence → Book Cipher` (Difficulty: 4)

### Chain Design Principles
- Each layer should have discoverable hint
- Total difficulty = hardest layer + 0.5 per additional layer
- Avoid repetition of same cipher type
- Consider solver fatigue

### Example Chain (from real ARG)
```
Original: HARMONY_KEY
↓ ROT13
UNEZBAL_XRL
↓ Base64
VU5FWkJBTFlfWFJM
↓ Hide in Pastebin
https://pastebin.com/abc123
```

### Hint Layering
For chain `A → B → C`:
- Clue 1: Hints at method A
- Intermediate result: Contains hint for method B
- Clue 2 (separate location): Hints at method C

---

## Quick Identification Guide

| Pattern | Likely Cipher |
|---------|---------------|
| All uppercase, shifted | Caesar |
| Letters + Numbers only | Base64 or Hex |
| Only 0s and 1s | Binary |
| Dots and dashes | Morse |
| Geometric symbols | Pigpen |
| Paired letters (XZ, QX) | Playfair |
| Numbers in pairs (11-55) | Polybius/Nihilist |
| Repeating pattern length | Vigenère (key length) |
| Random appearance, equal frequency | Strong substitution |
