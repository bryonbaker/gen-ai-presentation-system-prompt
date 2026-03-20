#!/usr/bin/env python3
"""
Example slides demonstrating every slide type available in the presentation system.

Run this to generate a reference deck showing all available layouts:
    source /home/bryon/Documents/FinOS/.venv/bin/activate
    python3 example_slides.py
"""

import sys
sys.path.insert(0, '/home/bryon/Documents/FinOS/gen-ai-presentation-system-prompt')

from presentation_helpers import *

OUTPUT = '/home/bryon/Documents/FinOS/example_slides.pptx'

prs = create_presentation()


# ============================================================
# EXAMPLE 1: Title Splash (Red Background)
# ============================================================
slide = make_title_splash(
    prs,
    title="Presentation Title",
    subtitle="A subtitle that describes the presentation\nin one or two lines",
    meta_lines=[
        "Based on: Source Document or Research Paper",
        "Author or Organisation (Year)"
    ]
)
set_notes(slide,
    "KEY MESSAGE: Introduce the topic.\n\n"
    "- Talking point 1\n"
    "- Talking point 2\n"
    "- Talking point 3\n"
    "- Talking point 4\n"
    "- Talking point 5"
)


# ============================================================
# EXAMPLE 2: Section Transition
# ============================================================
slide = make_section_slide(
    prs,
    number=1,
    title="Section Title Goes Here",
    subtitle="A brief description of what this section covers"
)
set_notes(slide,
    "KEY MESSAGE: Transition to the next section.\n\n"
    "- Preview what this section covers\n"
    "- Why it matters to the audience\n"
    "- What they should pay attention to\n"
    "- How it connects to the previous section\n"
    "- What comes next"
)


# ============================================================
# EXAMPLE 3: Content Slide with Two-Column Cards
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Section Name",
    title="Two-column card layout",
    subtitle="Use this for comparing or contrasting two concepts."
)

col_w = Inches(4.3)
col_h = Inches(2.5)

make_card(slide, Inches(0.6), Inches(1.8), col_w, col_h,
          "Left Card Title",
          ["First bullet point", "Second bullet point", "Third bullet point"],
          border_color=RH_RED, title_color=RH_RED)

make_card(slide, Inches(5.1), Inches(1.8), col_w, col_h,
          "Right Card Title",
          ["First bullet point", "Second bullet point", "Third bullet point"],
          border_color=RH_ORANGE, title_color=RH_ORANGE)

set_notes(slide,
    "KEY MESSAGE: Compare two concepts side by side.\n\n"
    "- Left card: explain the first concept\n"
    "- Right card: explain the second concept\n"
    "- Highlight the key differences\n"
    "- Explain why the comparison matters\n"
    "- Transition to the next slide"
)


# ============================================================
# EXAMPLE 4: Content Slide with Three-Column Cards
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Section Name",
    title="Three-column card layout",
    subtitle="Use this for three related categories or capabilities."
)

card_w = Inches(2.9)
card_h = Inches(2.2)
gap = Inches(0.15)
start_left = Inches(0.6)

make_card(slide, start_left, Inches(1.8), card_w, card_h,
          "Category One",
          ["Point A", "Point B", "Point C"],
          border_color=RH_RED, title_color=RH_RED)

make_card(slide, start_left + card_w + gap, Inches(1.8), card_w, card_h,
          "Category Two",
          ["Point A", "Point B", "Point C"],
          border_color=RH_ORANGE, title_color=RH_ORANGE)

make_card(slide, start_left + 2 * (card_w + gap), Inches(1.8), card_w, card_h,
          "Category Three",
          ["Point A", "Point B", "Point C"],
          border_color=RH_GREEN, title_color=RH_GREEN)

# Callout at the bottom
add_callout(slide, "A summary statement or key takeaway for the audience.")

set_notes(slide,
    "KEY MESSAGE: Present three related categories.\n\n"
    "- Category one explanation\n"
    "- Category two explanation\n"
    "- Category three explanation\n"
    "- How they relate to each other\n"
    "- Key takeaway in the callout"
)


# ============================================================
# EXAMPLE 5: Content Slide with Four Cards (2x2 Grid)
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Section Name",
    title="Four-card grid layout",
    subtitle="Use for four risk categories, quadrants, or related concepts."
)

card_w = Inches(4.3)
card_h = Inches(1.6)
left1 = Inches(0.6)
left2 = Inches(5.1)
top1 = Inches(1.8)
top2 = Inches(3.5)

make_card(slide, left1, top1, card_w, card_h,
          "Top Left", ["Bullet one", "Bullet two"],
          border_color=RH_RED, title_color=RH_RED)
make_card(slide, left2, top1, card_w, card_h,
          "Top Right", ["Bullet one", "Bullet two"],
          border_color=RH_ORANGE, title_color=RH_ORANGE)
make_card(slide, left1, top2, card_w, card_h,
          "Bottom Left", ["Bullet one", "Bullet two"],
          border_color=RH_PURPLE, title_color=RH_PURPLE)
make_card(slide, left2, top2, card_w, card_h,
          "Bottom Right", ["Bullet one", "Bullet two"],
          border_color=RH_GRAY_200, title_color=RH_BLACK)

set_notes(slide, "KEY MESSAGE: Present four related concepts in a grid.\n\n"
    "- Top left explanation\n- Top right explanation\n"
    "- Bottom left explanation\n- Bottom right explanation\n"
    "- How they connect")


# ============================================================
# EXAMPLE 6: Content Slide with Colored Background Cards
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Section Name",
    title="Colored background cards",
    subtitle="Use for emphasis or to highlight key questions."
)

card_w = Inches(2.9)
card_h = Inches(2.0)
gap = Inches(0.15)
start_left = Inches(0.6)

# Red card
shape = add_rounded_rect(slide, start_left, Inches(1.9), card_w, card_h,
                          RH_RED_LIGHT, RH_RED)
tb = add_textbox(slide, start_left + Pt(14), Inches(1.9) + Pt(14),
                 card_w - Pt(28), card_h - Pt(28))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "Question One?", FONT_DISPLAY, Pt(16), RH_BLACK,
         bold=True, alignment=PP_ALIGN.CENTER)
add_paragraph(tf, "Supporting detail text here.", FONT_TEXT, Pt(12), RH_BODY,
              alignment=PP_ALIGN.CENTER, space_before=Pt(10))

# Orange card
x2 = start_left + card_w + gap
shape = add_rounded_rect(slide, x2, Inches(1.9), card_w, card_h,
                          RH_ORANGE_LIGHT, RH_ORANGE)
tb = add_textbox(slide, x2 + Pt(14), Inches(1.9) + Pt(14),
                 card_w - Pt(28), card_h - Pt(28))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "Question Two?", FONT_DISPLAY, Pt(16), RH_BLACK,
         bold=True, alignment=PP_ALIGN.CENTER)
add_paragraph(tf, "Supporting detail text here.", FONT_TEXT, Pt(12), RH_BODY,
              alignment=PP_ALIGN.CENTER, space_before=Pt(10))

# Green card
x3 = x2 + card_w + gap
shape = add_rounded_rect(slide, x3, Inches(1.9), card_w, card_h,
                          RH_GREEN_LIGHT, RH_GREEN)
tb = add_textbox(slide, x3 + Pt(14), Inches(1.9) + Pt(14),
                 card_w - Pt(28), card_h - Pt(28))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "Question Three?", FONT_DISPLAY, Pt(16), RH_BLACK,
         bold=True, alignment=PP_ALIGN.CENTER)
add_paragraph(tf, "Supporting detail text here.", FONT_TEXT, Pt(12), RH_BODY,
              alignment=PP_ALIGN.CENTER, space_before=Pt(10))

set_notes(slide, "KEY MESSAGE: Pose three key questions.\n\n"
    "- Question one context\n- Question two context\n"
    "- Question three context\n- How the presentation answers them\n"
    "- Transition to solutions")


# ============================================================
# EXAMPLE 7: Timeline / Lineage Slide
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Timeline",
    title="Timeline or progression",
    subtitle="Use for showing evolution or maturity stages."
)

stg_w = Inches(2.7)
stg_h = Inches(2.6)
stg_top = Inches(1.8)

# Stage 1
shape = add_rounded_rect(slide, Inches(0.6), stg_top, stg_w, stg_h, RH_WHITE, RH_GRAY_200)
tb = add_textbox(slide, Inches(0.6) + Pt(12), stg_top + Pt(10), stg_w - Pt(24), stg_h - Pt(20))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "2023", FONT_MONO, Pt(11), RH_ORANGE, bold=True)
add_paragraph(tf, "Stage One", FONT_DISPLAY, Pt(16), RH_BLACK, bold=True, space_before=Pt(4))
add_paragraph(tf, "Description of what happened.", FONT_TEXT, Pt(11), RH_BODY, space_before=Pt(8))
add_bullet(tf, "Key development", size=Pt(11))
add_bullet(tf, "Another milestone", size=Pt(11))

# Arrow
tb = add_textbox(slide, Inches(3.3), Inches(2.8), Inches(0.3), Inches(0.3))
set_text(tb.text_frame, "\u2192", FONT_TEXT, Pt(20), RH_DARK, alignment=PP_ALIGN.CENTER)

# Stage 2
shape = add_rounded_rect(slide, Inches(3.55), stg_top, stg_w, stg_h, RH_WHITE, RH_GRAY_200)
tb = add_textbox(slide, Inches(3.55) + Pt(12), stg_top + Pt(10), stg_w - Pt(24), stg_h - Pt(20))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "2024", FONT_MONO, Pt(11), RH_ORANGE, bold=True)
add_paragraph(tf, "Stage Two", FONT_DISPLAY, Pt(16), RH_BLACK, bold=True, space_before=Pt(4))
add_paragraph(tf, "Description of progress.", FONT_TEXT, Pt(11), RH_BODY, space_before=Pt(8))
add_bullet(tf, "Key development", size=Pt(11))
add_bullet(tf, "Another milestone", size=Pt(11))

# Arrow
tb = add_textbox(slide, Inches(6.25), Inches(2.8), Inches(0.3), Inches(0.3))
set_text(tb.text_frame, "\u2192", FONT_TEXT, Pt(20), RH_DARK, alignment=PP_ALIGN.CENTER)

# Stage 3 (highlighted)
shape = add_rounded_rect(slide, Inches(6.5), stg_top, stg_w, stg_h, RH_RED_LIGHT, RH_RED)
tb = add_textbox(slide, Inches(6.5) + Pt(12), stg_top + Pt(10), stg_w - Pt(24), stg_h - Pt(20))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "2025", FONT_MONO, Pt(11), RH_RED, bold=True)
add_paragraph(tf, "Stage Three", FONT_DISPLAY, Pt(16), RH_RED, bold=True, space_before=Pt(4))
add_paragraph(tf, "Current focus area.", FONT_TEXT, Pt(11), RH_BODY, space_before=Pt(8))
add_bullet(tf, "Key initiative", size=Pt(11))
add_bullet(tf, "Another initiative", size=Pt(11))

set_notes(slide, "KEY MESSAGE: Show a three-stage progression.\n\n"
    "- Stage 1 context\n- Stage 2 context\n- Stage 3 context (highlighted as current)\n"
    "- What each stage produced\n- Where the audience should focus")


# ============================================================
# EXAMPLE 8: Numbered Summary Cards
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Recommendations",
    title="Numbered summary cards",
    subtitle="Use for prioritised recommendations or action items."
)

items = [
    ("1", "First Priority", "Description of the first action item or recommendation with supporting detail.", RH_RED),
    ("2", "Second Priority", "Description of the second action item or recommendation with supporting detail.", RH_ORANGE),
    ("3", "Third Priority", "Description of the third action item or recommendation with supporting detail.", RH_GREEN),
]

sc_left = Inches(0.6)
sc_w = Inches(8.8)
sc_h = Inches(0.9)
sc_top = Inches(1.8)

for i, (num, title, desc, color) in enumerate(items):
    y = sc_top + i * (sc_h + Pt(8))
    add_rounded_rect(slide, sc_left, y, sc_w, sc_h, RH_WHITE, color)

    tb = add_textbox(slide, sc_left + Pt(14), y + Pt(14), Pt(30), Pt(30))
    set_text(tb.text_frame, num, FONT_DISPLAY, Pt(22), color, bold=True)

    tb = add_textbox(slide, sc_left + Pt(50), y + Pt(8), sc_w - Pt(70), sc_h - Pt(16))
    tf = tb.text_frame
    tf.word_wrap = True
    set_text(tf, title, FONT_DISPLAY, Pt(14), RH_BLACK, bold=True)
    add_paragraph(tf, desc, FONT_TEXT, Pt(11), RH_BODY, space_before=Pt(4))

set_notes(slide, "KEY MESSAGE: Present three prioritised recommendations.\n\n"
    "- Priority 1 detail\n- Priority 2 detail\n- Priority 3 detail\n"
    "- Suggest starting with #1\n- How they build on each other")


# ============================================================
# EXAMPLE 9: Governance Stack (Layered Architecture)
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Architecture",
    title="Layered architecture diagram",
    subtitle="Use for governance stacks, infrastructure layers, or tiered systems."
)

stack_left = Inches(1.2)
stack_w = Inches(7.5)
layer_h = Inches(0.8)
gap = Pt(3)
stack_top = Inches(1.7)

layers = [
    ("TOP LAYER", "Application Layer", "Description of what sits at the top", RH_BLUE_LIGHT, RH_BLUE),
    ("MIDDLE LAYER", "Control Layer", "Description of controls and governance", RH_RED_LIGHT, RH_RED),
    ("LOWER LAYER", "Platform Layer", "Description of platform capabilities", RH_ORANGE_LIGHT, RH_ORANGE),
    ("FOUNDATION", "Infrastructure Layer", "Description of foundational components", RH_GREEN_LIGHT, RH_GREEN),
]

for i, (label, title, desc, bg, border) in enumerate(layers):
    y = stack_top + i * (layer_h + gap)
    add_rounded_rect(slide, stack_left, y, stack_w, layer_h, bg, border)

    tb = add_textbox(slide, stack_left + Pt(14), y + Pt(6), stack_w - Pt(28), Pt(14))
    set_text(tb.text_frame, label, FONT_MONO, Pt(8), border, bold=True)

    tb = add_textbox(slide, stack_left + Pt(14), y + Pt(20), stack_w - Pt(28), Pt(20))
    set_text(tb.text_frame, title, FONT_DISPLAY, Pt(13), RH_BLACK, bold=True)

    tb = add_textbox(slide, stack_left + Pt(14), y + Pt(40), stack_w - Pt(28), Pt(18))
    set_text(tb.text_frame, desc, FONT_TEXT, Pt(11), RH_BODY)

set_notes(slide, "KEY MESSAGE: Show a layered architecture.\n\n"
    "- Read from bottom to top\n- Each layer depends on the one below\n"
    "- Top layer explanation\n- Middle layer explanation\n"
    "- Lower layer explanation\n- Foundation explanation")


# ============================================================
# EXAMPLE 10: Simulated Table
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Comparison",
    title="Table layout",
    subtitle="Use for structured comparisons or classification data."
)

tbl_top = Inches(1.8)
tbl_left = Inches(0.6)
tbl_w = Inches(8.8)
row_h = Pt(32)

# Header
add_rect(slide, tbl_left, tbl_top, tbl_w, Pt(30), RH_GRAY_50, RH_RED)
tb = add_textbox(slide, tbl_left + Pt(10), tbl_top + Pt(4), Inches(2), Pt(22))
set_text(tb.text_frame, "COLUMN A", FONT_TEXT, Pt(10), RH_DARK, bold=True)
tb = add_textbox(slide, tbl_left + Inches(2.5), tbl_top + Pt(4), Inches(2.5), Pt(22))
set_text(tb.text_frame, "COLUMN B", FONT_TEXT, Pt(10), RH_DARK, bold=True)
tb = add_textbox(slide, tbl_left + Inches(5.5), tbl_top + Pt(4), Inches(3), Pt(22))
set_text(tb.text_frame, "COLUMN C", FONT_TEXT, Pt(10), RH_DARK, bold=True)

# Regular rows
rows = [
    ("Row 1", "Value A", "Description of row 1"),
    ("Row 2", "Value B", "Description of row 2"),
]
for i, (a, b, c) in enumerate(rows):
    y = tbl_top + Pt(32) + i * (row_h + Pt(2))
    add_rect(slide, tbl_left, y, tbl_w, row_h, RH_WHITE, RH_GRAY_200)
    tb = add_textbox(slide, tbl_left + Pt(10), y + Pt(6), Inches(2), Pt(20))
    set_text(tb.text_frame, a, FONT_TEXT, Pt(12), RH_BLACK, bold=True)
    tb = add_textbox(slide, tbl_left + Inches(2.5), y + Pt(6), Inches(2.5), Pt(20))
    set_text(tb.text_frame, b, FONT_TEXT, Pt(12), RH_BODY)
    tb = add_textbox(slide, tbl_left + Inches(5.5), y + Pt(6), Inches(3), Pt(20))
    set_text(tb.text_frame, c, FONT_TEXT, Pt(12), RH_BODY)

# Highlighted row
y = tbl_top + Pt(32) + 2 * (row_h + Pt(2))
add_rect(slide, tbl_left, y, tbl_w, row_h, RH_RED_LIGHT, RH_RED)
tb = add_textbox(slide, tbl_left + Pt(10), y + Pt(6), Inches(2), Pt(20))
set_text(tb.text_frame, "Row 3 (Best)", FONT_TEXT, Pt(12), RH_RED, bold=True)
tb = add_textbox(slide, tbl_left + Inches(2.5), y + Pt(6), Inches(2.5), Pt(20))
set_text(tb.text_frame, "Value C", FONT_TEXT, Pt(12), RH_RED)
tb = add_textbox(slide, tbl_left + Inches(5.5), y + Pt(6), Inches(3), Pt(20))
set_text(tb.text_frame, "Description of highlighted row", FONT_TEXT, Pt(12), RH_RED)

set_notes(slide, "KEY MESSAGE: Compare items in a structured table.\n\n"
    "- Row 1 explanation\n- Row 2 explanation\n"
    "- Row 3 is highlighted because...\n"
    "- What the comparison reveals\n- Key takeaway")


# ============================================================
# EXAMPLE 11: Two-Column Text + Cards
# ============================================================
slide = make_content_slide(
    prs,
    section_label="Detail",
    title="Split layout: text left, cards right",
    subtitle="Use when one side explains and the other provides examples."
)

# Left: text with bullets
tb = add_textbox(slide, Inches(0.6), Inches(1.8), Inches(4.5), Inches(2.5))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "Key capabilities", FONT_DISPLAY, Pt(15), RH_BLACK, bold=True)
p = add_bullet(tf, "", size=Pt(12), space_before=Pt(8))
p.clear()
add_bold_then_normal(p, "Capability one ", "with supporting context", size=Pt(12))
p = add_bullet(tf, "", size=Pt(12))
p.clear()
add_bold_then_normal(p, "Capability two ", "with supporting context", size=Pt(12))
p = add_bullet(tf, "", size=Pt(12))
p.clear()
add_bold_then_normal(p, "Capability three ", "with supporting context", size=Pt(12))

# Right: stacked cards
make_card(slide, Inches(5.4), Inches(1.8), Inches(4.2), Inches(1.0),
          "Example A", ["Description of example A"],
          bg_color=RH_RED_LIGHT, border_color=RGBColor(0xF5, 0xC3, 0xC0))
make_card(slide, Inches(5.4), Inches(2.9), Inches(4.2), Inches(1.0),
          "Example B", ["Description of example B"],
          bg_color=RH_ORANGE_LIGHT, border_color=RGBColor(0xE0, 0xC5, 0xA0))
make_card(slide, Inches(5.4), Inches(4.0), Inches(4.2), Inches(1.0),
          "Example C", ["Description of example C"],
          bg_color=RH_GREEN_LIGHT, border_color=RGBColor(0xC3, 0xDF, 0xC0))

set_notes(slide, "KEY MESSAGE: Explain capabilities on the left, show examples on the right.\n\n"
    "- Capability one detail\n- Capability two detail\n"
    "- Example A explanation\n- Example B explanation\n"
    "- Example C explanation\n- Key takeaway")


# ============================================================
# EXAMPLE 12: Dark Message Slide
# ============================================================
slide = make_dark_slide(prs)

tb = add_textbox(slide, Inches(0.8), Inches(0.6), Inches(8.4), Inches(1.0))
tf = tb.text_frame
tf.word_wrap = True
set_text(tf, "A bold statement that\ncaptures the core message", FONT_DISPLAY,
         Pt(26), RH_WHITE, bold=True, alignment=PP_ALIGN.CENTER)

# Four pillars
pillars = [
    ("Pillar One", "Short description"),
    ("Pillar Two", "Short description"),
    ("Pillar Three", "Short description"),
    ("Pillar Four", "Short description"),
]

pillar_w = Inches(2.1)
pillar_h = Inches(1.4)
pillar_top = Inches(2.0)
pillar_gap = Inches(0.15)
pillar_left = Inches(0.55)

for i, (title, desc) in enumerate(pillars):
    x = pillar_left + i * (pillar_w + pillar_gap)
    add_rounded_rect(slide, x, pillar_top, pillar_w, pillar_h,
                     RGBColor(0x25, 0x25, 0x25), RGBColor(0x44, 0x44, 0x44))

    tb = add_textbox(slide, x + Pt(12), pillar_top + Pt(16),
                     pillar_w - Pt(24), pillar_h - Pt(32))
    tf = tb.text_frame
    tf.word_wrap = True
    set_text(tf, title, FONT_DISPLAY, Pt(16), RH_RED, bold=True, alignment=PP_ALIGN.CENTER)
    add_paragraph(tf, desc, FONT_TEXT, Pt(11), RGBColor(0xBB, 0xBB, 0xBB),
                  alignment=PP_ALIGN.CENTER, space_before=Pt(8))

tb = add_textbox(slide, Inches(1), Inches(3.8), Inches(8), Inches(0.6))
set_text(tb.text_frame, "A memorable closing line.", FONT_DISPLAY, Pt(20), RH_RED,
         bold=True, alignment=PP_ALIGN.CENTER)

set_notes(slide, "KEY MESSAGE: The single most important statement.\n\n"
    "- Pause and let the message land\n"
    "- Pillar one explanation\n- Pillar two explanation\n"
    "- Pillar three explanation\n- Pillar four explanation\n"
    "- The closing line reinforces the message")


# ============================================================
# EXAMPLE 13: Thank You
# ============================================================
slide = make_thank_you(prs, "Questions & Discussion")
set_notes(slide, "KEY MESSAGE: Close and open discussion.\n\n"
    "- Recap the key points\n"
    "- Suggested discussion questions\n"
    "- Offer to share resources\n"
    "- Next steps if applicable\n"
    "- Thank the audience")


# ============================================================
# SAVE
# ============================================================
prs.save(OUTPUT)
print(f"Example slides saved to: {OUTPUT}")
print(f"Total slides: {len(prs.slides)}")
