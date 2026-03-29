from src.app_agents.explainer_agent import build_explainer_agent
from src.app_agents.retriever_agent import build_retriever_agent
from src.app_agents.triage_agent import build_triage_agent


def test_build_explainer_agent() -> None:
    agent = build_explainer_agent()
    assert agent.name == "Explainer Agent"


def test_build_retriever_agent() -> None:
    agent = build_retriever_agent()
    assert agent.name == "Retriever Agent"


def test_build_triage_agent() -> None:
    agent = build_triage_agent()
    assert agent.name == "Triage Agent"