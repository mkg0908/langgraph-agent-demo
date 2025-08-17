
from fastapi import FastAPI
from pydantic import BaseModel
from src.agent.flow import build_graph, run_workflow

app = FastAPI(title="LangGraph Agent Demo")

class AnalyzeRequest(BaseModel):
    doc: str
    policy: str = "MUST encrypt data at rest"

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    g = build_graph()
    result = run_workflow(g, {"doc": req.doc, "policy": req.policy})
    return result
