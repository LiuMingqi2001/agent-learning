from __future__ import annotations

from agents import Agent

from src.llm.provider import get_default_model
from src.tools.retrieval_tool import retrieve_project_notes


def build_retriever_agent() -> Agent:
    return Agent(
        name="Retriever Agent",
        instructions=(
            "你是一个检索 agent，负责从本地项目文档中查找信息。"
            "优先调用 retrieve_project_notes 工具。"
            "回答时先给出检索结论，再简要总结，不要展开过长分析。"
            "若检索不到内容，应明确说明未找到，而不是编造。"
        ),
        model=get_default_model(),
        tools=[retrieve_project_notes],
        handoff_description="适用于项目文档、学习笔记、本地知识说明等检索任务。",
    )