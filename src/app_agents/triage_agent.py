from __future__ import annotations

from agents import Agent

from src.app_agents.explainer_agent import build_explainer_agent
from src.app_agents.retriever_agent import build_retriever_agent
from src.llm.provider import get_default_model
from src.tools.calculator_tool import calculate
from src.tools.time_tool import get_current_time
from src.tools.weather_tool import get_weather


def build_triage_agent() -> Agent:
    explainer_agent = build_explainer_agent()
    retriever_agent = build_retriever_agent()

    return Agent(
        name="Triage Agent",
        instructions=(
            "你是系统的主入口 agent，负责接收用户请求并做轻量路由。"
            "处理规则如下："
            "1. 数学计算问题，优先调用 calculate 工具；"
            "2. 当前时间、时区时间类问题，调用 get_current_time 工具；"
            "3. 天气问题，调用 get_weather 工具；"
            "4. 解释代码、解释报错、解释概念的问题，handoff 给 Explainer Agent；"
            "5. 项目文档、学习笔记、本地资料查询类问题，handoff 给 Retriever Agent；"
            "6. 普通知识问答可直接回答。"
            "不要无意义地频繁 handoff，也不要在可直接回答时强行调用工具。"
        ),
        model=get_default_model(),
        tools=[calculate, get_current_time, get_weather],
        handoffs=[explainer_agent, retriever_agent],
    )