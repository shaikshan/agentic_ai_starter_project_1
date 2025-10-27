# Agentic AI — Individual Assignment Report

## 1. Overview

This project demonstrates a **multi-agent AI system (Agentic AI)** that performs an end-to-end **research-to-article pipeline**.  
The system automates topic research, article writing, and critique using specialized AI agents orchestrated together.

The key goal is to simulate a self-improving workflow where multiple AI agents collaborate to generate high-quality, factually grounded content with minimal human intervention.

**GitHub Repository:** [https://github.com/shaikshan/agentic_ai_starter_project_1](https://github.com/shaikshan/agentic_ai_starter_project_1)

---

## 2. Architecture

### 2.1 System Overview

The architecture is modular and agent-oriented.  
Each agent is designed to perform a specific cognitive task in the research–writing–critique pipeline.

User → Orchestrator → ResearchAgent → WriterAgent → CriticAgent → Final Output


### 2.2 Components

#### 🧭 Orchestrator (`orchestrator.py`)
- Acts as the central controller.
- Takes a user topic input.
- Sequentially triggers each agent.
- Logs and saves outputs in `/outputs/final_article.txt`.
- Handles the iterative loop between **Writer** and **Critic** if improvement cycles are enabled.

#### 🔍 ResearchAgent (`agents/researchagent.py`)
- Uses **Wikipedia API** and web requests to gather information.
- Summarizes 4–6 sources with URLs and concise explanations.
- Outputs structured data (list of dicts).

#### ✍️ WriterAgent (`agents/writeragent.py`)
- Uses the **OpenAI GPT-4o-mini model** through the latest OpenAI SDK (`openai>=1.0.0`).
- Takes the research snippets as input and generates a **700–1200 word article** with citations.
- Implements prompt engineering for structured and coherent writing.

#### 🧩 CriticAgent (`agents/criticagent.py`)
- Acts as an **editor**.
- Analyzes the draft for:
  - Factual accuracy
  - Coherence and flow
  - Tone/style consistency
  - Missing or incorrect citations
- Produces both a **critique summary** and an **improved article** version.

#### 🧠 Utilities
- **Logger (`utils/logger.py`)**: Logs all steps with timestamps.
- **Outputs Directory**: Stores all intermediate and final outputs.

---

## 3. Design Decisions

### 3.1 Agentic Workflow
The system follows a *pipeline-based agent orchestration pattern*:
1. **Research** gathers context.
2. **Writer** transforms it into a coherent draft.
3. **Critic** performs evaluation and refinement.

This structure promotes **separation of concerns**, allowing each agent to evolve independently.

### 3.2 Language Model & API
- Chosen Model: `gpt-4o-mini` (for speed, cost, and reasoning balance)
- SDK: `openai>=1.0.0` new API with `OpenAI()` client
- Optional RAG (Retrieval-Augmented Generation) considered for future extension.

### 3.3 Logging & Traceability
Every step (topic entry, research, drafting, critique, completion) is logged with timestamps.
This makes the pipeline transparent and reproducible.

### 3.4 Streamlit Integration
To enhance interactivity, a **Streamlit app (`app.py`)** was added:
- User inputs a topic through the web interface.
- Displays:
  - Collected research sources
  - Drafted article
  - Critique report
  - Improved final output
- Saves final results automatically to `/outputs`.

---

## 4. Implementation Details

### 4.1 Environment Setup
```bash
conda create -n venv python=3.10
conda activate venv
pip install -r requirements.txt
```
### 4.2 API Configuration
```bash
setx OPENAI_API_KEY "your_api_key_here"
```
or using a .env file:

```.env
OPENAI_API_KEY=your_api_key_here
```
### 4.3 Running the Application

- Command line:
    ```bash
    python orchestrator.py
    ```
- Streamlit web interface:
    ```bash
    streamlit run app.py
    ```

Author: Shaik Roshan Zameer
Course: Agentic AI — Individual Assignment
Date: October 2025

