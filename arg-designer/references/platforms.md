# Platforms Reference

Platform-specific guidance for ARG deployment and content delivery.

## Table of Contents
1. [Communication Platforms](#communication-platforms)
2. [Content Hosting](#content-hosting)
3. [Interactive Systems](#interactive-systems)
4. [Social Media](#social-media)
5. [Physical/Hybrid](#physicalhybrid)
6. [Platform Selection Matrix](#platform-selection-matrix)

---

## Communication Platforms

### Discord

**Use Cases**:
- Character interactions
- Community hub
- Real-time events
- Role-based content gating

**Setup Pattern**:
```
Server Structure:
├── #welcome (pinned rules, context)
├── #general (community chat)
├── #puzzle-discussion (spoiler-tagged)
├── #media-archive (solved content)
├── #character-appearances (controlled by PM)
└── Voice channels for live events
```

**ARG Techniques**:
- Character account joins, posts, disappears
- Roles unlock channels (progression)
- Bot-mediated puzzles
- Webhook messages for "system" communications
- Hidden channels discovered through puzzle solutions

**Considerations**:
- Moderation burden is high
- Bot development may be required
- Server can be reported (backup plan needed)
- Discord rate limits affect some puzzle types

### Telegram

**Use Cases**:
- Broadcast announcements
- Character communications
- Bot-driven interactions
- International accessibility

**Setup Pattern**:
```
Channel/Group Structure:
├── Public Channel (broadcast only)
├── Community Group (discussion)
└── Bot DMs (individual interactions)
```

**ARG Techniques**:
- Character channels for "leaked" communications
- Scheduled messages for time-based reveals
- Bot conversations for branching dialogue
- Stickers/media for visual clues

**Considerations**:
- Less moderation tools than Discord
- Excellent for mobile-first audiences
- Bot API very capable
- International popularity

### IRC/Matrix

**Use Cases**:
- Retro aesthetic
- Technical audience
- High anonymity needs
- Extended text-based interaction

**ARG Techniques**:
- Character bots
- Topic strings with clues
- Scheduled channel messages
- Private messages for individual puzzles

---

## Content Hosting

### Static Websites

**Use Cases**:
- Corporate fronts
- Character personal sites
- Document repositories
- Interactive puzzles

**Setup Pattern**:
```
Recommended Stack:
├── Static hosting (Netlify, Vercel, GitHub Pages)
├── Custom domain ($10-15/year)
├── SSL certificate (free via Let's Encrypt)
└── Basic analytics (privacy-respecting)
```

**ARG Techniques**:
- Hidden pages (/secret, /truth)
- Source code comments
- robots.txt misdirection
- Progressive revelation (time-based unlocks)
- Cookies for state management

**Considerations**:
- Full control over content
- No platform risk
- Requires some technical skill
- Hosting costs (usually minimal)

### Pastebin/GitHub Gists

**Use Cases**:
- "Leaked" documents
- Code fragments
- Anonymous drops
- Quick content deployment

**ARG Techniques**:
- Unlisted pastes (URL is password)
- Syntax highlighting for code clues
- Revision history as clue trail
- Expiring pastes for urgency

**Considerations**:
- May be removed for TOS violations
- Limited formatting
- Reliable and fast
- Anonymous posting possible

### YouTube

**Use Cases**:
- Found footage
- Character vlogs
- "Corporate" videos
- Audio spectrograms

**Setup Pattern**:
```
Channel Strategy:
├── In-world branding
├── Playlists for organization
├── Cards/End screens for connections
├── Community tab for interactions
└── Premiere for live events
```

**ARG Techniques**:
- Unlisted videos (URL discovery)
- Frame-embedded clues
- Description text hiding
- Premiere chat for live interaction
- Audio spectrogram images

**Considerations**:
- Algorithmic suppression of "weird" content
- Copyright claims if using music
- Comments need moderation
- Excellent discoverability potential

---

## Interactive Systems

### Twilio (Phone/SMS)

**Use Cases**:
- Interactive voice response (IVR)
- SMS puzzle systems
- Character phone lines
- Voicemail drops

**Setup Pattern**:
```python
# Basic IVR Structure
from twilio.twiml.voice_response import VoiceResponse, Gather

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    gather = Gather(num_digits=1, action='/handle-key')
    gather.say("Press 1 for archives. Press 2 for emergency.")
    response.append(gather)
    return str(response)
```

**ARG Techniques**:
- Multi-level IVR menus
- DTMF password entry
- SMS response systems
- Voicemail callbacks
- Dynamic content based on caller input

**Considerations**:
- Cost per call/SMS (~$0.01-0.03)
- Phone number required (~$1/month)
- Country restrictions may apply
- Excellent immersion factor

### Email Systems

**Use Cases**:
- Character correspondence
- Automated responses
- Drip campaigns
- Document delivery

**Setup Pattern**:
```
Email Setup:
├── Domain email (character@harmony.example.com)
├── Autoresponder for initial contact
├── Drip campaign for progression
└── Manual responses for key interactions
```

**ARG Techniques**:
- Character email addresses
- Autoresponders with clues
- Scheduled email "leaks"
- Reply-based interactions
- Attachment puzzles

**Considerations**:
- Spam filter issues
- Deliverability requires proper setup
- Manual response burden
- Very personal feeling

### Custom Web Apps

**Use Cases**:
- Interactive puzzles
- State-tracked experiences
- Complex branching
- Player progression systems

**Technologies**:
```
Simple: Static HTML + JavaScript
Medium: Flask/Node.js with database
Complex: Full web framework with auth
```

**ARG Techniques**:
- Cookie/session-based progression
- User accounts for persistent state
- API integrations
- Real-time multiplayer elements

---

## Social Media

### Twitter/X

**Use Cases**:
- Character voices
- Real-time events
- Breadcrumb trails
- Community engagement

**Setup Pattern**:
```
Account Strategy:
├── Consistent posting schedule
├── In-character voice always
├── Engage with community (in character)
├── Media posts with hidden clues
└── Thread narratives
```

**ARG Techniques**:
- Character accounts
- Threads for storytelling
- Media attachments (images with stego)
- Polls for community decisions
- Scheduled tweets

**Considerations**:
- Account suspension risk
- Algorithmic suppression
- Fast-moving, requires monitoring
- Excellent for virality

### Instagram

**Use Cases**:
- Visual storytelling
- Character lifestyle
- Image-based puzzles
- Location tagging

**ARG Techniques**:
- Stories for ephemeral content
- Alt text hiding
- Geotag clues
- Reel narratives
- Carousel puzzles

### TikTok

**Use Cases**:
- Found footage style
- Character POV
- Young audience reach
- Viral potential

**ARG Techniques**:
- "Accidental" recordings
- Duet/stitch mechanics
- Sound-based clues
- Comment interactions

### Reddit

**Use Cases**:
- Long-form text
- Community building
- "Organic" discovery
- Archive-friendly

**ARG Techniques**:
- Posts to relevant subreddits
- Character AMAs
- Document drops
- r/nosleep style narratives

---

## Physical/Hybrid

### Print Materials

**Use Cases**:
- Event handouts
- Mailed packages
- Public placement
- Tactile puzzles

**Types**:
- Business cards
- Posters/flyers
- Letters/documents
- Props and artifacts

**Distribution**:
- Events/conventions
- Dead drops
- Direct mail
- Retail placement

### Geocaching

**Use Cases**:
- Location-based puzzles
- Physical artifact discovery
- Community coordination
- Local events

**Setup**:
- Weatherproof containers
- GPS coordinates as puzzle output
- Multiple cache chains
- Maintenance plan

### QR Code Placement

**Use Cases**:
- Bridge digital/physical
- Public discovery
- Event integration
- Easy access point

**Best Practices**:
- Test scanning at various distances
- Include manual URL option
- Weatherproof if outdoor
- Track scans for analytics

---

## Platform Selection Matrix

### By Audience Type

| Audience | Primary Platforms | Secondary |
|----------|-------------------|-----------|
| Gamers | Discord, Twitch, Reddit | Twitter |
| Tech-savvy | GitHub, IRC, custom sites | Discord |
| General public | YouTube, Instagram, TikTok | Twitter |
| Horror fans | YouTube, Reddit, Discord | Podcasts |
| Music fans | YouTube, SoundCloud, Bandcamp | Twitter |

### By Interactivity Level

| Level | Platforms |
|-------|-----------|
| Passive viewing | YouTube, podcasts, static sites |
| Light interaction | Social media, Discord |
| Active participation | Twilio, email, custom apps |
| Physical | Geocaching, events, mail |

### By Technical Skill Required

| Skill Level | Platforms |
|-------------|-----------|
| Low | Social media, YouTube, Pastebin |
| Medium | Discord bots, static websites |
| High | Twilio, custom apps, infrastructure |

### By Budget

| Budget | Approach |
|--------|----------|
| Free | Social media, GitHub Pages, Discord |
| Low ($0-50/mo) | Custom domain, Twilio basic, email |
| Medium ($50-200/mo) | Multiple phone numbers, hosting, tools |
| High ($200+/mo) | Custom development, multiple platforms |
