# Presentation Style Guide

## Brand Colors

| Name | Hex | Usage |
|------|-----|-------|
| `RH_RED` | `#EE0000` | Primary accent, borders, highlights |
| `RH_BLACK` | `#151515` | Headings, titles |
| `RH_DARK` | `#292929` | Subtitles |
| `RH_BODY` | `#1F1F1F` | Body text |
| `RH_WHITE` | `#FFFFFF` | Backgrounds, text on dark/red |
| `RH_GRAY` | `#999999` | Muted text, version numbers |
| `RH_GRAY_200` | `#D2D2D2` | Default card borders |
| `RH_BLUE` | `#0066CC` | Informational accent |
| `RH_GREEN` | `#2E7D32` | Positive/success accent |
| `RH_ORANGE` | `#C65100` | Warning/attention accent |
| `RH_PURPLE` | `#5E35B1` | Tertiary accent |

### Light Backgrounds (for cards)

| Name | Hex | Pair with border |
|------|-----|-----------------|
| `RH_RED_LIGHT` | `#FCEAE9` | `RH_RED` |
| `RH_BLUE_LIGHT` | `#E3F2FD` | `RH_BLUE` |
| `RH_GREEN_LIGHT` | `#E8F5E9` | `RH_GREEN` |
| `RH_ORANGE_LIGHT` | `#FFF3E0` | `RH_ORANGE` |

## Fonts

| Font | Usage | Import |
|------|-------|--------|
| `Red Hat Display` | Titles, headings, card headers | Display font (bold, 800 weight) |
| `Red Hat Text` | Body text, bullets, subtitles | Text font (regular, 400-700 weight) |
| `Red Hat Mono` | Code, labels, dates, small tags | Monospace font |

## Slide Dimensions

- Width: **10 inches** (9,144,000 EMU)
- Height: **5.625 inches** (5,143,500 EMU)
- Standard content padding: **0.6 inches** from left, **0.4 inches** from top

## Slide Types

### 1. Title Splash (Red Background)

Full red background slide used for the first and last slides.

```
Background: RH_RED (full slide)
Title: Red Hat Display, 40pt, white, bold, centered
Divider: thin line, #FF9999, centered
Subtitle: Red Hat Text, 18pt, white, centered
Meta text: Red Hat Text, 11pt, #FFCCCC, centered
```

**When to use:** Opening slide, closing "Thank You" slide.

### 2. Section Transition

Two-panel slide with red left panel (40% width) and white right panel.

```
Left panel: RH_RED background, 40% width
Section number: Red Hat Display, 72pt, #FF6666, bold, right-aligned in left panel
Right panel: white background, 60% width
Title: Red Hat Display, 28pt, RH_BLACK, bold
Subtitle: Red Hat Text, 14pt, RH_DARK
```

**When to use:** Between major sections. Always include a section heading — never blank.

### 3. Content Slide (Standard)

White background with red left accent bar.

```
Red accent bar: 5pt wide, full height, left edge
Section label: Red Hat Text, 10pt, RH_RED, bold, uppercase, tracking 1.5px
Title: Red Hat Display, 26pt, RH_BLACK, bold
Subtitle: Red Hat Text, 14pt, RH_DARK
Content area: starts at ~1.8 inches from top
```

**When to use:** Most content slides. Body content varies by layout (see below).

### 4. Dark Message Slide

Full black background for high-impact statements.

```
Background: RH_BLACK (full slide)
Title: Red Hat Display, 26pt, white, bold, centered
Cards: dark gray (#252525) with #444444 borders
Card titles: Red Hat Display, 16pt, RH_RED, centered
Card text: Red Hat Text, 11pt, #BBBBBB, centered
Tagline: Red Hat Display, 20pt, RH_RED, bold, centered
Sub-tagline: Red Hat Text, 16pt, #999999, centered
```

**When to use:** Core message slide, key takeaway, closing statement before "Thank You".

## Content Layouts

### Cards (Rounded Rectangles)

Cards are the primary content container. Use `make_card()` for simple cards or build custom cards with `add_rounded_rect()` + text boxes.

```
Border: 1.5pt, colored border
Corner radius: default rounded rectangle
Padding: 14pt internal
Title: Red Hat Display, 14pt, colored (matches border), bold
Bullets: Red Hat Text, 11pt, RH_BODY
```

**Common card arrangements:**
- **Two-column:** `Inches(4.3)` wide, starting at `Inches(0.6)` and `Inches(5.1)`
- **Three-column:** `Inches(2.9)` wide, with `Inches(0.15)` gaps
- **Stacked:** full width `Inches(8.8)`, vertically stacked with `Pt(8)` gaps

### Callout Box

Left-bordered emphasis box at the bottom of a slide.

```
Red border: 4pt wide, RH_RED, left edge
Background: #F5F5F5
Text: Red Hat Text, 12-13pt, RH_BODY
Position: typically at Inches(4.2) from top, Inches(8.8) wide
```

### Table (Simulated)

Tables are built with rectangles and text boxes (not native PPTX tables).

```
Header row: #F5F5F5 background, RH_RED border, uppercase labels (10pt, bold)
Data rows: white background, RH_GRAY_200 border
Highlighted row: RH_RED_LIGHT background, RH_RED border, red text
```

### Governance Stack (Layered)

Vertically stacked rounded rectangles representing architecture layers.

```
Each layer: colored background (light), colored border, Inches(0.8) height
Label: Red Hat Mono, 8pt, colored, bold, uppercase
Title: Red Hat Display, 13pt, RH_BLACK, bold
Description: Red Hat Text, 11pt, RH_BODY
Stack from top to bottom with Pt(3) gaps
```

### Timeline / Lineage

Horizontal flow of connected boxes.

```
Boxes: Inches(2.7) wide, rounded rectangle, RH_GRAY_200 border
Active box: RH_RED_LIGHT background, RH_RED border
Arrows: unicode → character between boxes
Date: Red Hat Mono, 11pt, colored
Title: Red Hat Display, 16pt, bold
Description: Red Hat Text, 11pt
```

### Summary Cards (Numbered)

Vertically stacked cards with large numbers.

```
Card: full width, Inches(0.9) height, colored border
Number: Red Hat Display, 22pt, colored, bold
Title: Red Hat Display, 14pt, RH_BLACK, bold
Description: Red Hat Text, 11pt, RH_BODY
```

## Speaker Notes Format

Every slide must include speaker notes in this format:

```
KEY MESSAGE: <one sentence summary of the slide's purpose>

- <talking point 1 with specific references and data>
- <talking point 2>
- <talking point 3>
- <talking point 4>
- <talking point 5>
- <talking point 6 (optional)>
- <talking point 7 (optional)>
```

Rules for speaker notes:
- Start with `KEY MESSAGE:` followed by one clear sentence
- Include 5-7 bullet points
- Every factual claim must include a specific reference (model name, benchmark name, date, statistic)
- Section transition slides should preview what comes next
- Content slides should explain each visual element on the slide

## Template Details

- **Template file:** `0 - clean template.pptx`
- **Layout used:** Index `[70]` — BLANK layout (all shapes added programmatically)
- **Slide master:** Contains Red Hat branding elements
- All content is created using `python-pptx` shape and text box functions
- The template provides consistent slide numbering via the BLANK layout's placeholder
