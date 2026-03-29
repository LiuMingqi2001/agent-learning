from __future__ import annotations

from agents import Runner

from src.app_agents.triage_agent import build_triage_agent
from src.tracing.trace_logger import LocalTraceLogger


async def run_qa(user_input: str) -> str:
    trace = LocalTraceLogger()
    trace.write_event("user_input", {"text": user_input})

    agent = build_triage_agent()
    trace.write_event("agent_selected", {"agent": "Triage Agent"})

    result = await Runner.run(agent, user_input)

    final_output = str(result.final_output)
    trace.write_event(
        "final_output",
        {
            "output": final_output,
            "duration_ms": trace.elapsed_ms(),
        },
    )
    return final_output


async def run_qa_streamed(user_input: str) -> str:
    trace = LocalTraceLogger()
    trace.write_event("user_input", {"text": user_input})

    agent = build_triage_agent()
    trace.write_event("agent_selected", {"agent": "Triage Agent"})

    result = Runner.run_streamed(agent, user_input)

    async for event in result.stream_events():
        event_type = getattr(event, "type", type(event).__name__)

        payload = {
            "type": event_type,
            "repr": repr(event)[:1000],
        }

        # 尽量补一点更有用的信息，方便你读日志
        if event_type == "agent_updated_stream_event":
            payload["new_agent"] = getattr(getattr(event, "new_agent", None), "name", None)

        elif event_type == "run_item_stream_event":
            payload["name"] = getattr(event, "name", None)
            item = getattr(event, "item", None)
            payload["item_type"] = getattr(item, "type", None)

        trace.write_event("stream_event", payload)

    # 关键点：这里不要 await result
    # 流消费结束后，直接从 result 取最终输出
    final_output = str(result.final_output)

    trace.write_event(
        "final_output",
        {
            "output": final_output,
            "is_complete": getattr(result, "is_complete", None),
            "duration_ms": trace.elapsed_ms(),
        },
    )
    return final_output