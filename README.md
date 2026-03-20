# Overview

This repository enables you to "vibe clode" powerpoint presentations in a defined Red Hat style.

# Instructions
The system prompt is saved at:

  gen-ai-presentation-system-prompt/SYSTEM_PROMPT.md

  How to use it: Open the file, copy everything below the --- line, and paste it as your
  first message in a new Claude Code session. Then fill in the topic, audience, filename,
  and content at the bottom.

  The key things it tells Claude to do:
  1. Read the style guide, helpers, and examples before starting
  2. Import presentation_helpers.py rather than rewriting all the functions
  3. Draft content as text first for your review before generating the PPTX
  4. Include speaker notes on every slide with references
  5. Use the existing venv and template — no setup needed

