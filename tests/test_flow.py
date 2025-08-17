
from src.agent.flow import build_graph, run_workflow

def test_simple_policy_check():
    g = build_graph()
    doc = "All customer data MUST be encrypted at rest. Backups MUST be taken daily."
    out = run_workflow(g, {"doc": doc, "policy": "MUST encrypt data at rest"})
    assert "summary" in out
    assert isinstance(out["summary"]["count"], int)
