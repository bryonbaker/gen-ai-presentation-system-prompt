# Presentation Generator — System Prompt

Use these instructions to generate a branded PowerPoint presentation on any topic using the Red Hat template.

## Quick Start

Paste the following into Claude Code along with your content:

```
Generate a PowerPoint presentation using the system in:
/home/bryon/Documents/FinOS/gen-ai-presentation-system-prompt/

Template: /home/bryon/Documents/FinOS/0 - clean template.pptx
Output: /home/bryon/Documents/FinOS/<presentation-name>.pptx

Topic: <your topic>
Audience: <your audience>

Content:
<paste your slide content here>
```

## How It Works

1. You provide the **topic, audience, and slide content** (text outline)
2. Claude generates a Python script using `python-pptx` and the Red Hat template
3. The script uses the **shared helper library** (`presentation_helpers.py`) for consistent styling
4. The script is executed in a Python virtual environment at `/home/bryon/Documents/FinOS/.venv`
5. Output is a `.pptx` file ready to open in PowerPoint or LibreOffice Impress

## Files in This Directory

| File | Purpose |
|------|---------|
| `INSTRUCTIONS.md` | This file — how to use the system |
| `STYLE_GUIDE.md` | Visual design rules and slide type specifications |
| `presentation_helpers.py` | Python helper library with all shared functions and constants |
| `example_slides.py` | Reference examples for every slide type |

## Workflow

### Step 1: Write your content as a text outline

Write your presentation as a structured text outline. For each slide, specify:
- **Slide type** (see `STYLE_GUIDE.md` for available types)
- **Title and subtitle**
- **Body content** (bullets, cards, table data, etc.)
- **Speaker notes** (key message + 5-7 talking points)

### Step 2: Ask Claude to generate the presentation

Provide the content outline and reference these instructions. Claude will:
1. Import `presentation_helpers.py` for all styling functions
2. Generate a Python script specific to your content
3. Run it in the existing venv at `/home/bryon/Documents/FinOS/.venv`
4. Produce the `.pptx` output file

### Step 3: Iterate

You can ask Claude to:
- Add, remove, or reorder slides
- Update speaker notes
- Change card layouts or colors
- Insert new slide types

## Important Notes

- Always use the **virtual environment** at `/home/bryon/Documents/FinOS/.venv` (it has `python-pptx` installed)
- Always use the **template file** at `/home/bryon/Documents/FinOS/0 - clean template.pptx`
- The template uses layout index `[70]` (BLANK) for all content slides — shapes are added programmatically
- Slide dimensions are **10" x 5.625"** (widescreen)
- All fonts must be from the **Red Hat font family** (Display, Text, Mono)
- Every slide must have **speaker notes** with a key message and 5-7 talking points
- Section transition slides must have a **section heading** — never leave them blank
