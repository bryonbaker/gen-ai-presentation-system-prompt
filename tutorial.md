# Tutorial: Using Claude Code to Generate a Technical Presentation

This tutorial walks through a real working session where Claude Code was used to research a codebase, design a slide deck outline, iterate on it, and generate a branded PowerPoint presentation -- all from natural language instructions.

---

## Prerequisites

- [Claude Code](https://claude.ai/claude-code) CLI or desktop app
- A git repository containing the source material you want to present
- A PowerPoint template and generation system (this tutorial uses the `gen-ai-presentation-system-prompt` helper library with Red Hat branding)

---

## Step 1: Clone the Source Material and Understand the Codebase

The first instruction gives Claude Code a repository to clone and asks it to read all documentation to understand the structure.

### Instruction

> I am building a presentation that describes a demo environment. I want you to clone this repository and then read all of the content under docs to get an idea of the structure. I will then guide you on the content I want: https://github.com/rhoai-genaiops/lab-instructions.git

### What Claude Code Did

1. Cloned the repository with `git clone`
2. Used `Glob` to discover all markdown files under `docs/` (70+ files across 13 modules)
3. Spawned four parallel research agents to read all files simultaneously, covering:
   - Section 1 (AI Orientation) + sidebar + main README
   - Sections 2-4 (Linguistics, Ready to Scale 101, Ready to Scale 201)
   - Sections 5-7 (Grounded AI, Observability, Honor Code)
   - Sections 8-12, 15 (Agents, On-Prem, Optimization, MaaS, Fine-Tuning, Campus Setup)
4. Returned a structured summary of the entire repository: 13 modules, key tech stack, core patterns

### Key Technique

Using **parallel agents** to read a large codebase is dramatically faster than reading files sequentially. Each agent reads its assigned files independently and returns a summary. This keeps the main conversation context clean while gathering comprehensive information.

---

## Step 2: Define the Slide Content and Story

With the codebase understood, the next instruction specified exactly which slides to create and what story to tell.

### Instruction

> Okay. I want a slide deck that provides some key visualisations and in the order that they appear in the material.
> 1. I want an intro to the demo environment and subject of the demo
> 2. I want an overview of the key takeaways: GenAI Ops automating the evaluation of prompt changes and automation of evals when documents are updated in the RAG database. Automated pull requests when evals pass criteria.
> 3. A slide explaining system and user prompts
> 4. A slide explaining evals and the role of judge models and the rules the judge model is given to evaluate.
> 5. The role of synthetic data generation in generating evals.
> Build a story and outline the slide contents.

### What Claude Code Did

1. Re-read specific files related to the requested topics (evaluations, judge models, synthetic data, prompt engineering, feedback loops)
2. Searched for `judge_prompt`, `scoring_params`, and `llm-as-judge` references across the codebase to find exact configuration details
3. Drafted a 5-slide outline with:
   - Slide titles and content bullets
   - Visual suggestions for each slide
   - A narrative flow table showing the story arc
   - Specific code/config examples pulled from the actual repo

### Key Technique

Being **specific about what you want on each slide** gives Claude Code clear constraints. The numbered list with topic descriptions was enough for it to map each slide to the right source material and pull exact details (YAML configs, pipeline names, parameter values).

---

## Step 3: Save the Outline to a File

### Instruction

> write this outline in markdown format to a file.

### What Claude Code Did

Wrote the complete outline to `slide-deck-outline.md` using the `Write` tool.

---

## Step 4: Iterate -- Add Missing Content

After reviewing the outline, a gap was identified: the pipelines themselves weren't described in detail.

### Instruction

> I just realised I left out all of the description of the different pipelines. Add content describing the pipelines that are triggered through gitea commits and document uploads

### What Claude Code Did

1. Re-read the relevant pipeline documentation files:
   - `4-ready-to-scale-201/4-automate-with-tekton.md` (evaluation pipeline)
   - `5-grounded-ai/7-rag-tekton.md` (document ingestion pipeline)
   - `5-grounded-ai/4-rag-pipelines.md` (Kubeflow pipeline details)
   - `4-ready-to-scale-201/3-kubeflow-pipelines.md` (KFP setup)
2. Inserted two new slides (Slide 3: Eval Pipeline, Slide 4: Doc-Ingestion Pipeline) into the outline
3. Renumbered all subsequent slides (3->5, 4->6, 5->7)
4. Updated the narrative flow table at the bottom to reflect the new 7-slide structure

### Key Technique

**Iterative refinement** is natural in this workflow. You review the output, identify gaps, and ask for additions. Claude Code handles the insertion, renumbering, and consistency updates automatically.

---

## Step 5: Generate the PowerPoint

With the outline finalised, the final instruction pointed to a template system and asked for the actual PPTX file.

### Instruction

> Now I want you to generate a powerpoint presentation. In the directory "gen-ai-presentation-system-prompt" You will find a template for creating presentations. Read the file "SYSTEM_PROMPT.md" and generate follow the instructions to generate the presentation

### What Claude Code Did

1. Read three files to understand the presentation system:
   - `SYSTEM_PROMPT.md` -- rules and output format
   - `STYLE_GUIDE.md` -- brand colors, fonts, slide types, layout specs
   - `presentation_helpers.py` -- Python helper library (card builders, slide constructors)
   - `example_slides.py` -- working code examples of every slide type
2. Located the template file (`0 - clean template.pptx`) and checked for the Python venv
3. Created the venv and installed `python-pptx` (the venv didn't exist yet)
4. Wrote `generate_genai_demo.py` -- a 400+ line Python script that:
   - Maps each outline slide to the appropriate slide type (title splash, section transition, content, thank you)
   - Chooses the right layout for each slide's content (3-column cards, split layout, timeline, stacked layers)
   - Adds detailed speaker notes to every slide (KEY MESSAGE + 5-7 talking points)
   - Uses only Red Hat fonts and brand colors
5. Ran the script to produce `genai-demo.pptx` (13 slides)

### Key Technique

The **presentation helper system** is the critical enabler here. By providing Claude Code with:
- A style guide (what's allowed)
- A helper library (how to build it)
- Example code (what it looks like in practice)

...it can generate on-brand slides programmatically without any manual PowerPoint work. The helper library abstracts away the low-level `python-pptx` API and enforces consistency.

---

## Final Output: The Slide Deck Outline

The outline below was the approved content that was used to generate the final PowerPoint.

---

# GenAIOps: From Prompt to Production

## Slide Deck Outline

### Story Arc

The deck tells the story of moving from **manual AI experimentation** to a **fully automated GenAIOps lifecycle** -- where prompt changes are evaluated automatically, RAG document updates trigger re-evaluation, and production promotion happens through pull requests gated by eval results.

---

## SLIDE 1: Title / Intro to the Demo Environment

**Title:** "GenAIOps: From Prompt to Production"

**Content:**

- Setting: **Redwood Digital University** is building **Canopy**, an AI-powered educational assistant
- Canopy is powered by **Llama 3.2** running on **Red Hat OpenShift AI**
- Architecture stack: **Canopy UI** (Streamlit) → **Canopy Backend** (FastAPI) → **Llama Stack** → **vLLM** model serving
- Three environments managed through **GitOps** (Argo CD): Experiment → Test → Production
- All configuration (prompts, models, features) lives in **Git** as the single source of truth

**Visual suggestion:** Architecture diagram showing the three-layer stack (UI → Backend → Llama Stack → LLM) with the three environments side by side, connected by Git/Argo CD arrows.

---

## SLIDE 2: Key Takeaways -- The GenAIOps Automation Loop

**Title:** "The GenAIOps Lifecycle: Automate Everything After the Experiment"

**Content -- three automation triggers:**

1. **Prompt changes trigger evals automatically**
   - Developer updates system prompt in `values-test.yaml` → commits to Git
   - Git webhook fires → Tekton pipeline starts → Kubeflow eval pipeline runs
   - Results stored in MinIO and displayed in Prompt Tracker dashboard

2. **RAG document updates trigger evals automatically**
   - New document uploaded to MinIO `documents` bucket
   - MinIO webhook → Tekton pipeline → Kubeflow doc-ingestion pipeline (Docling + Milvus)
   - Backend repo auto-commits with new vector DB ID
   - That commit triggers the eval pipeline automatically

3. **Automated Pull Requests when evals pass**
   - After eval pipeline completes, a PR is auto-generated from test → prod
   - PR includes a link to evaluation results
   - Human reviews results and merges → Argo CD syncs to production

**Visual suggestion:** A circular flow diagram:

```
Prompt Change or Doc Upload
    → Git Commit
    → Tekton Pipeline
    → Kubeflow Evals
    → Results in MinIO / Prompt Tracker
    → Auto PR (test → prod)
    → Human Approves
    → Argo CD deploys to Prod
    → (loop back to observe)
```

---

## SLIDE 3: The Evaluation Pipeline -- Triggered by Prompt Changes

**Title:** "Every Prompt Change is Automatically Tested"

**Content:**

- **What triggers it:** A Git commit to the `backend` repo that changes `values-test.yaml` (the prompt config), or a commit to the `evals` repo (the test cases themselves)
- **How it's wired:** Gitea webhooks on both repos fire to a Tekton EventListener. The backend webhook has a filter so only changes to `values-test.yaml` trigger the pipeline.

- **The Tekton evaluation pipeline** (`canopy-evals-pipeline`) runs three steps:
  1. **Git Clone** -- pulls the latest eval test definitions from the `evals` repo
  2. **Kubeflow Pipeline trigger** -- starts the KFP evaluation pipeline, which:
     - Reads test cases from YAML (each folder = one feature, e.g. `Summary/`, `information-search/`, `student-assistant/`)
     - For each test: sends the prompt to the **Canopy Backend** in the test environment
     - Captures the generated answer
     - Passes generated answer + expected answer to the **LLM-as-Judge** via Llama Stack's `scoring.score()` API
     - Produces an HTML results report stored in MinIO (`test-results` bucket)
  3. **Auto-PR creation** -- raises a Pull Request from `test` to `prod` in the `backend` repo, with a link to the evaluation results

- **Where results are visible:**
  - **MinIO** `test-results` bucket: downloadable HTML report
  - **Prompt Tracker dashboard**: eval results attached to the Git commit that triggered them
  - **Gitea PR**: links to results in the PR description for human review

- **The human-in-the-loop moment:**
  - Reviewer checks the eval results via the PR link
  - If results look good → merge the PR → Argo CD syncs the new prompt to production
  - If results are poor → reject, iterate on the prompt, and push again (re-triggers the pipeline)

**Visual suggestion:** A left-to-right flow:

```
Developer changes prompt
    → git push (values-test.yaml)
    → Gitea webhook
    → Tekton Pipeline
        ├── git clone (evals repo)
        ├── Kubeflow Eval Pipeline
        │     ├── Send prompt to Backend (test)
        │     ├── Judge generated vs expected (LLM-as-Judge)
        │     └── Store HTML results in MinIO
        └── Create PR (test → prod)
    → Human reviews PR + results
    → Merge → Argo CD deploys to prod
```

---

## SLIDE 4: The Document Ingestion Pipeline -- Triggered by Uploads

**Title:** "New Documents Automatically Flow Into Production"

**Content:**

- **What triggers it:** A PDF uploaded to the MinIO `documents` bucket
- **How it's wired:** A MinIO webhook (`PUT - Object Uploaded` event on the `documents` bucket) fires to a Tekton EventListener

- **The Tekton doc-ingestion pipeline** (`canopy-doc-ingestion-pipeline`) orchestrates:
  1. **Triggers the Kubeflow doc-ingestion pipeline** (`document-intelligence-rag`), which:
     - Connects to **Docling** (an intelligent document processor that handles tables, formulas, multi-column layouts)
     - Processes the uploaded PDF into chunked markdown
     - Generates **embeddings** using `all-MiniLM-L6-v2` (384 dimensions, 512-token chunks)
     - Stores the embedded chunks in **Milvus** vector database (both test and prod instances)
     - Returns a new **vector DB collection ID**
  2. **Auto-commits to the `backend` repo** -- updates `values-test.yaml` with the new vector DB ID
  3. **That commit triggers the evaluation pipeline** (Slide 3) -- because the backend repo webhook detects a change to `values-test.yaml`

- **The chain reaction:**

  ```
  PDF uploaded to MinIO
      → MinIO webhook
      → Tekton doc-ingestion pipeline
      → Kubeflow: Docling → Embeddings → Milvus
      → Auto-commit new vector DB ID to backend repo
      → Gitea webhook fires (values-test.yaml changed)
      → Tekton eval pipeline runs (Slide 3)
      → Auto-PR with eval results
      → Human approves → Argo CD deploys to prod
  ```

- **Key pipeline parameters:**
  - `minio_bucket_name`: `documents`
  - `embedding_model`: `all-MiniLM-L6-v2`
  - `embedding_dimension`: `384`
  - `chunk_size_tokens`: `512`
  - `vector_provider`: `milvus`
  - `docling_service`: Docling v0.7.0 running as a KServe inference service on GPU

- **The human-in-the-loop moment:**
  - After the eval pipeline completes, a PR appears in the backend repo to update the vector DB ID in production
  - The PR description includes a link to the eval results
  - Reviewer checks whether the RAG evals pass with the new documents
  - If evals don't cover the new content yet, the reviewer can add new prompt/expected_result pairs to the `evals` repo and re-trigger

**Visual suggestion:** A pipeline diagram showing the two-stage chain:

```
Stage 1: Document Ingestion                    Stage 2: Evaluation (auto-triggered)
┌─────────────────────────────────────┐        ┌──────────────────────────────────┐
│ PDF → Docling → Embeddings → Milvus │ ──────→│ Eval tests → Judge → Results     │
│         (new vector DB ID)          │  auto  │         (HTML in MinIO)           │
│         (auto-commit to Git)        │ commit │         (PR: test → prod)         │
└─────────────────────────────────────┘        └──────────────────────────────────┘
```

---

## SLIDE 5: System Prompts and User Prompts

**Title:** "The Two Parts of Every LLM Interaction"

**Content:**

- **System Prompt** -- Sets the model's *behavior and persona*
  - Written by application owners, not end users
  - Automatically prepended to every interaction
  - Takes priority over user prompt instructions
  - Example: `"You are a helpful and patient tutor. Guide the user towards the correct answer without giving it straight up."`

- **User Prompt** -- The actual *question or task* from the user
  - Example: `"What is 5+5?"`

- **Combined into a single input:**

  ```
  [System] You are a helpful and patient tutor...
  [User] What is 5+5?
  ```

  The model has learned to treat these two parts differently.

- **Why this matters for GenAIOps:**
  - Prompts are stored in `values-test.yaml` / `values-prod.yaml` as versioned config
  - Loaded into the backend via ConfigMaps (no rebuild needed)
  - Every change goes through Git -- tracked, auditable, revertible
  - Small wording changes produce dramatically different outputs -- which is why we need automated evals

**Visual suggestion:** A diagram showing System Prompt + User Prompt merging into a single arrow entering the LLM box, with the output arrow coming out. Annotate the system prompt side with "Set by developers, versioned in Git" and the user prompt side with "From the end user."

---

## SLIDE 6: Evaluations and the LLM-as-Judge Pattern

**Title:** "Who Grades the AI? Another AI."

**Content:**

- **The evaluation structure** (YAML-based test cases):

  ```yaml
  tests:
    - prompt: "Describe the main learning outcomes..."
      expected_result: "Students will learn to design GenAI apps..."
  ```

  Each test defines an input prompt and what a good answer looks like.

- **The LLM-as-Judge pattern:**
  - A second LLM (the "judge model," also Llama 3.2) evaluates the application's answer against the expected answer
  - Configured via `scoring_params`:

    ```yaml
    scoring_params:
      "llm-as-judge::base":
        judge_model: llama32
        prompt_template: judge_prompt.txt
        type: llm_as_judge
        judge_score_regexes: ["Answer: (A|B|C|D|E)"]
    ```

  - The **judge prompt template** (`judge_prompt.txt`) gives the judge model its grading rubric -- rules for comparing the generated answer to the expected answer
  - The judge scores on a **letter grade scale (A-E)** extracted via regex
  - Additional scoring functions can be layered in (e.g., `basic::subset_of` for factual containment, `basic::tool_choice` for agent tool selection)

- **What gets evaluated:**
  - The **application backend** end-to-end (prompt + business logic + LLM response)
  - Test cases cover: summarization, RAG information search, agent tool selection
  - Speed testing via **GuideLLM**: TTFT, TPOT, throughput

- **Feedback-driven evals:**
  - User thumbs-down feedback is exported as new test cases
  - These become **regression tests** ensuring prompt improvements don't break previously working cases

**Visual suggestion:** A flow showing: Test Prompt → Backend (with system prompt) → LLM → Generated Answer. Then: Generated Answer + Expected Answer → Judge Model (with grading rubric) → Score (A-E). Annotate that both the application LLM and judge LLM can be the same model.

---

## SLIDE 7: Synthetic Data Generation for Evals and Fine-Tuning

**Title:** "Manufacturing Quality at Scale: Synthetic Data Generation"

**Content:**

- **The problem:** Good evaluation data (and training data) is expensive and manual to create
  - Evals need prompt + expected_result pairs that reflect real usage
  - Fine-tuning needs 500-1000+ high-quality examples
  - Manual creation doesn't scale

- **Synthetic Data Generation (SDG) approach:**
  - **Source documents** (e.g., course syllabi PDFs) are converted to markdown via **Docling**
  - An LLM generates question-answer pairs from the document content
  - These pairs become:
    - **Eval test cases** (prompt + expected_result in YAML)
    - **Training examples** for fine-tuning (e.g., Socratic tutor interactions)

- **Two uses of synthetic data in this environment:**

  1. **Generating eval test cases for RAG:**
     - Documents uploaded to vector DB are also used to generate prompt/expected_result pairs
     - These eval tests verify the RAG pipeline retrieves and summarizes correctly
     - Example from the course: 6 test cases generated from AI501 syllabus content

  2. **Generating training data for fine-tuning:**
     - SDG Hub generates Socratic tutor interaction examples from course materials
     - Used to LoRA fine-tune Qwen2-0.5B to behave as a Socratic tutor
     - Result: 800-token system prompt reduced to ~10 tokens (behavior baked into weights)

- **The virtuous cycle:**
  - User feedback (thumbs down) → new eval test cases
  - New documents → synthetic eval test cases
  - Both feed back into the automated pipeline

**Visual suggestion:** A funnel diagram: Source Documents (PDFs) → Docling (markdown) → LLM (synthetic generation) → branching into two paths: "Eval Test Cases (YAML)" and "Fine-Tuning Data (examples)". Below, show the feedback loop: User Feedback → Export → Additional Eval Test Cases → merged into the same pipeline.

---

## Overall Narrative Flow

| Slide | Story Beat |
|-------|-----------|
| 1 | "Here's what we built and where it runs" |
| 2 | "Here's the magic: everything after your first experiment is automated" |
| 3 | "When a developer changes a prompt, this pipeline tests it automatically" |
| 4 | "When new documents are uploaded, this pipeline ingests them and triggers evals" |
| 5 | "The thing we're automating around is the prompt -- here's how it works" |
| 6 | "How do we know if a prompt change is good? We use an LLM to judge the LLM" |
| 7 | "Where do all these test cases come from? We generate them synthetically -- and from real user feedback" |

The story progresses from **what** (the environment) → **why** (automation matters) → **how the pipelines work** (prompt evals, document ingestion) → **how prompts work** → **how we evaluate** → **how we scale evaluation data**.

---

## Summary: The Workflow Pattern

The pattern used in this tutorial is repeatable for any technical presentation:

1. **Research** -- Point Claude Code at source material (repos, docs, specs) and let it read everything
2. **Outline** -- Describe the slides you want in natural language with topic descriptions
3. **Iterate** -- Review the outline, identify gaps, ask for additions or changes
4. **Generate** -- Point to a template system and let Claude Code produce the final PPTX

Each step builds on the previous one. The key is providing clear constraints (what slides, what story, what audience) while letting Claude Code handle the research, content extraction, and code generation.
