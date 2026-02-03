# Hiding Methods Reference

60+ techniques for concealing content in ARGs, organized by content type.

## Table of Contents
1. [Text Hiding](#text-hiding)
2. [Image Hiding](#image-hiding)
3. [Audio Hiding](#audio-hiding)
4. [Video Hiding](#video-hiding)
5. [File/Document Hiding](#filedocument-hiding)
6. [Web/Digital Hiding](#webdigital-hiding)

---

## Text Hiding

### Metadata-Based
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| EXIF comments | 2 | Hide in image metadata fields | ExifTool |
| PDF metadata | 2 | Author, keywords, custom fields | PDF editors |
| Document properties | 1 | File properties in Office docs | Properties dialog |
| ID3 tags | 2 | MP3 metadata fields | Kid3, MP3Tag |

### Steganographic
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Zero-width characters | 4 | Unicode invisibles (ZWSP, ZWJ) | Custom scripts |
| Whitespace encoding | 3 | Spaces vs tabs as binary | Snow, stegsnow |
| Null byte injection | 4 | Hidden after null terminator | Hex editor |
| Homoglyph substitution | 3 | Similar-looking Unicode chars | Unicode tables |

### Structural
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Acrostic | 2 | First letters spell message | Manual |
| Nth word/letter | 2 | Every Nth element | Manual |
| Word count pattern | 3 | Sentence lengths encode data | Manual |
| Invisible ink (print) | 3 | UV-reactive or heat-reveal | Physical materials |

---

## Image Hiding

### Pixel-Level
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| LSB steganography | 3 | Least significant bit encoding | OpenStego, zsteg |
| Color channel hiding | 3 | Data in R, G, or B channel only | GIMP, ImageMagick |
| Alpha channel | 3 | Hidden in transparency layer | Image editors |
| Specific color values | 2 | Hex colors spell message | Color picker |

### Visual
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| QR codes | 1 | Embedded or hidden QR | QR generators |
| Micro text | 2 | Tiny text in image details | Zoom required |
| Layer hiding | 2 | Hidden layers in PSD/XCF | Photoshop, GIMP |
| Stereograms | 4 | Magic eye hidden images | Stereogram generators |

### Transformation
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Brightness adjustment | 2 | Reveal by adjusting levels | Any editor |
| Color inversion | 1 | Hidden in inverted image | Any editor |
| Histogram analysis | 4 | Data in pixel distribution | ImageMagick |
| Fourier transform | 5 | Frequency domain hiding | Python/MATLAB |

### Format-Specific
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| GIF frame hiding | 2 | Extra frames in animation | GIMP, ezgif |
| PNG chunks | 4 | Custom ancillary chunks | pngcheck, hex editor |
| JPEG comment | 2 | COM marker data | ExifTool |
| SVG embedded data | 3 | Hidden in XML structure | Text editor |

---

## Audio Hiding

### Spectrogram
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Image in spectrogram | 3 | Visual image when viewed | Audacity, Sonic Visualiser |
| Text in spectrogram | 3 | Text readable in frequency view | Audacity |
| QR in spectrogram | 4 | Scannable QR code | Custom generation |

### Temporal
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Reversed audio | 1 | Play backwards for message | Audacity |
| Speed manipulation | 2 | Slowed/sped content | Audacity |
| Silence patterns | 3 | Morse in pause lengths | Audio editor |
| DTMF tones | 2 | Phone dial tones | DTMF decoder |

### Steganographic
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| LSB audio | 4 | Least significant bit in samples | DeepSound, custom |
| Phase encoding | 5 | Data in phase relationships | Custom scripts |
| Echo hiding | 4 | Data in echo patterns | Research tools |
| Spread spectrum | 5 | Distributed across frequencies | Specialized tools |

### Layered
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Multi-track hiding | 2 | Separate audio track | DAW software |
| Phase cancellation | 3 | Remove known audio to reveal | Audacity |
| Frequency isolation | 3 | Message in specific band | EQ, filters |
| Binaural encoding | 4 | Left/right channel difference | Audacity |

---

## Video Hiding

### Frame-Based
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Single frame insert | 2 | Brief frame with content | Video editors |
| Frame differencing | 4 | Difference between frames | Python/OpenCV |
| Corrupted frames | 2 | Intentional "glitch" art | Hex editor |
| Timecode data | 3 | Hidden in timestamp metadata | MediaInfo |

### Track-Based
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Subtitle tracks | 2 | Hidden subtitle stream | MKVToolNix |
| Multiple audio | 2 | Secret audio track | Video editors |
| Chapter markers | 2 | Hidden chapter names | MKVToolNix |

### Visual
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Background elements | 1 | Hidden in scene details | Watch carefully |
| QR in frame | 2 | Brief QR code appearance | Frame-by-frame |
| Letter/number flash | 2 | Quick character displays | Frame-by-frame |
| Edge of frame | 2 | Content at video borders | Pan and scan |

---

## File/Document Hiding

### Archive Methods
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Nested archives | 2 | ZIP within ZIP within ZIP | Any archiver |
| Password patterns | 2 | Passwords from other puzzles | -- |
| File concatenation | 3 | Data appended after archive | Hex editor, cat |
| Polyglot files | 4 | Valid as multiple formats | Specialized tools |

### Office Documents
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| White text on white | 1 | Select all to reveal | Office apps |
| Tiny font | 1 | 1pt text hidden in document | Office apps |
| Hidden rows/columns | 1 | Excel hidden data | Unhide function |
| Comments/notes | 1 | Review mode comments | Office apps |

### Code/Data Files
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Comments in code | 1 | Hidden in source comments | Text editor |
| Unused variables | 2 | Variable names spell message | Code review |
| Log file entries | 2 | Fake log with real clues | Text editor |
| Config files | 2 | Hidden in configuration | Text editor |

---

## Web/Digital Hiding

### HTML/Source
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| HTML comments | 1 | `<!-- hidden -->` | View source |
| CSS hiding | 2 | display:none content | Inspect element |
| JavaScript vars | 2 | Hidden in scripts | Console, debugger |
| Data attributes | 3 | Custom data-* attributes | Inspect element |

### URL/Network
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| URL parameters | 2 | Query strings, fragments | Browser |
| Subdomains | 2 | secret.example.com | DNS lookup |
| robots.txt | 1 | Disallowed paths reveal | Direct access |
| .htaccess/hidden dirs | 3 | Directory enumeration | Dirbusting |

### Platform-Specific
| Method | Difficulty | Description | Tools |
|--------|------------|-------------|-------|
| Discord role colors | 2 | Hex codes in role colors | Discord |
| Social media alt text | 2 | Image descriptions | Platform tools |
| Pastebin raw URLs | 1 | Raw paste data | Direct URL |
| GitHub commit messages | 2 | Hidden in history | Git log |

---

## Method Selection Matrix

### By Solver Skill Level

**Beginner-Friendly** (casual players):
- View source, HTML comments
- Reversed audio
- White text on white
- Image brightness adjustment
- QR codes

**Intermediate** (experienced puzzlers):
- Spectrograms
- Base64/cipher chains
- EXIF metadata
- Layer hiding
- Nested archives

**Advanced** (dedicated hunters):
- LSB steganography
- Zero-width Unicode
- Phase cancellation
- Polyglot files
- Frame differencing

### By Required Tools

**No Special Tools**:
- HTML source, CSS inspect
- Audio reversal (VLC)
- Image adjustment (any editor)

**Free Tools Required**:
- Audacity (audio analysis)
- GIMP (image layers)
- ExifTool (metadata)
- 7-Zip (archives)

**Specialized Knowledge**:
- Hex editors
- Python scripting
- Frequency analysis
- Forensics tools
