
# LangGraph Agent Demo

A minimal, production-minded example of a **multi-step AI agent** using a graph workflow.
The demo shows how to parse a document, check it against a simple policy, and return a structured summary.
It also includes a tiny FastAPI service so you can run the workflow over HTTP.

## Features
- Multi-step workflow (parse → check → summarize) with explicit state passing
- Pluggable LLM interface with a **FakeLLM** (no API keys required)
- FastAPI endpoint (`/analyze`) that runs the workflow
- Unit test for the workflow logic
- Dockerfile for containerizing the service

## Tech
- Python 3.10+
- Optional: `langgraph` for real graph composition (code will fall back to a simple runner if not installed)
- FastAPI (web), Pydantic (validation), pytest (tests)
