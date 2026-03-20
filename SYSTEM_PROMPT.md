# System Prompt for Presentation Generation

Copy everything below the line and paste it as your first message in a new Claude Code session.

---

## Presentation generation instructions

I need you to generate a branded PowerPoint presentation. Before you start, read the following files to understand the style system:

1. `/home/bryon/Documents/FinOS/gen-ai-presentation-system-prompt/STYLE_GUIDE.md` — visual design rules, colors, fonts, and all available slide types
2. `/home/bryon/Documents/FinOS/gen-ai-presentation-system-prompt/presentation_helpers.py` — shared Python helper library (import this in your script)
3. `/home/bryon/Documents/FinOS/gen-ai-presentation-system-prompt/example_slides.py` — working code examples of every slide type

**Rules:**
- Use the template at `/home/bryon/Documents/FinOS/0 - clean template.pptx`
- Run all Python in the venv at `/home/bryon/Documents/FinOS/.venv` (has `python-pptx` installed)
- Import `presentation_helpers.py` using `sys.path.insert(0, '/home/bryon/Documents/FinOS/gen-ai-presentation-system-prompt')` then `from presentation_helpers import *`
- Use only Red Hat fonts: `Red Hat Display` (titles), `Red Hat Text` (body), `Red Hat Mono` (labels/code)
- Every slide must have speaker notes: `KEY MESSAGE:` line + 5-7 bullet talking points with specific references
- Section transition slides must always have a heading — never blank
- For section transitions use `make_section_slide()`, for content use `make_content_slide()`, for the title use `make_title_splash()`, for the end use `make_thank_you()`
- First draft the content as text in the chat for me to review. Only generate the PPTX after I approve.

**Output:** `<filename>.pptx` in `/home/bryon/Documents/FinOS/`

Here is my presentation:

**Topic:** [your topic]
**Audience:** [your audience]
**Output filename:** [filename.pptx]

**Content:**

[Paste your slide outline here. For each slide include:
- Slide type (title splash / section transition / content / dark message / thank you)
- Title and subtitle
- Body content (bullets, cards, comparisons, etc.)
- Any specific notes for the speaker]
