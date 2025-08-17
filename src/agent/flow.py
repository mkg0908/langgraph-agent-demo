
from typing import Dict, Any, Callable

try:
    from langgraph.graph import StateGraph, END  # type: ignore
    HAS_LANGGRAPH = True
except Exception:
    HAS_LANGGRAPH = False
    END = "END"  # sentinel

def parse_doc(state: Dict[str, Any]) -> Dict[str, Any]:
    text = state.get("doc", "")
    state["clauses"] = [line.strip() for line in text.splitlines() if "MUST" in line.upper()]
    return state

def check_policy(state: Dict[str, Any]) -> Dict[str, Any]:
    policy = state.get("policy", "").lower()
    clauses = state.get("clauses", [])
    flags = []
    if "encrypt" in policy:
        for c in clauses:
            if "encrypt" not in c.lower():
                flags.append(c)
    state["flags"] = flags
    return state

def summarize(state: Dict[str, Any]) -> Dict[str, Any]:
    flags = state.get("flags", [])
    state["summary"] = {"violations": flags, "count": len(flags)}
    return state

def _build_langgraph():
    from langgraph.graph import StateGraph, END  # type: ignore
    g = StateGraph(dict)
    g.add_node("parse", parse_doc)
    g.add_node("check", check_policy)
    g.add_node("summarize", summarize)
    g.set_entry_point("parse")
    g.add_edge("parse", "check")
    g.add_edge("check", "summarize")
    g.add_edge("summarize", END)
    return g.compile()

def _build_fallback_graph():
    return ["parse", "check", "summarize"]

def build_graph():
    if HAS_LANGGRAPH:
        return _build_langgraph()
    return _build_fallback_graph()

def run_workflow(graph, state: Dict[str, Any]) -> Dict[str, Any]:
    if HAS_LANGGRAPH and hasattr(graph, "invoke"):
        return graph.invoke(state)
    steps = {
        "parse": parse_doc,
        "check": check_policy,
        "summarize": summarize,
    }
    sr = dict(state)
    for node in graph:
        sr = steps[node](sr)
    return sr
