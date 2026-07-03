# 🦜 Agentic AI — LangChain · LangGraph · LangSmith

Companion code for the **Agentic AI** YouTube series by [@techfluencer-eval](https://www.youtube.com/@techfluencer-eval) — build real AI agents, hands-on, from scratch.

## Setup
1. Install [uv](https://docs.astral.sh/uv/).
2. Clone this repo, then:
   ```bash
   uv sync
   ```
3. Copy `.env.example` to `.env` and add your key:
   ```bash
   cp .env.example .env
   ```
   Works with **OpenAI** directly, or any **OpenAI-compatible** endpoint (e.g. Azure AI Foundry) via `OPENAI_BASE_URL`.

## Run
```bash
uv run lesson-01/main.py     # or lesson-02/main.py
```

## Lessons
- **Lesson 1 — Your first LangChain app** (`lesson-01/`): a chat model + your first LCEL chain (`prompt | model | parser`).
- **Lesson 2 — Messages & prompt templates** (`lesson-02/`): system/human messages, `ChatPromptTemplate`, few-shot, and `MessagesPlaceholder` (memory) — with the gotchas.
- _More lessons added as the series ships…_

## Stack
`langchain` · `langchain-openai` · `langgraph` · `langsmith` · Python 3.13 · uv

▶ Watch the series: https://www.youtube.com/@techfluencer-eval
