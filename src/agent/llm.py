
import os

def llm_complete(prompt: str) -> str:
    """Placeholder LLM call. For demo/testing we avoid external calls.
    Replace with provider SDK (OpenAI, etc.) as needed.
    """
    if os.getenv("USE_FAKE_LLM", "1") == "1":
        return f"[FAKE_LLM_SUMMARY]\n{prompt[:120]}..."
    return "LLM disabled"
