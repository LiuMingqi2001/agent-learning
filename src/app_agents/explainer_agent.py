from __future__ import annotations

from agents import Agent

from src.llm.provider import get_default_model


def build_explainer_agent() -> Agent:
    return Agent(
        name="Explainer Agent",
        instructions=(
            "你是一个解释器 agent，负责解释代码、报错、技术概念、工具结果。"
            "回答应清晰、结构化、便于初学者理解。"
            "当用户提供代码时，优先说明代码功能、关键逻辑、执行流程和常见错误点。"
            "不要主动调用与解释无关的工具。"
        ),
        model=get_default_model(),
        handoff_description="适用于代码解释、报错分析、概念解释等请求。",
    )