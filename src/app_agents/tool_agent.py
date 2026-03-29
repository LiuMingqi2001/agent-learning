import json
import logging
from typing import Any

from pydantic import ValidationError

from src.config import get_settings
from src.llm.client import LLMClient
from src.schemas.calculator_schema import CalculatorArgs
from src.schemas.time_schema import TimeArgs
from src.schemas.weather_schema import WeatherArgs
from src.tools.calculator_tool import run_calculator
from src.tools.time_tool import run_time_tool
from src.tools.weather_tool import run_weather_tool


SYSTEM_PROMPT = """
你是一个支持单轮工具调用的智能助手。

请严格遵守以下规则：
1. 当用户要求明确数学计算时，优先调用 calculator 工具。
2. 当用户询问当前时间、现在几点、今天几号、某时区当前时间时，调用 get_current_time 工具。
3. 当用户询问某个城市天气时，调用 get_weather 工具。
4. 对于普通知识问答、概念解释、开放性讨论，不调用工具，直接回答。
5. 如果工具执行失败，不允许编造工具结果，必须如实说明失败原因。
6. 工具参数必须严格符合 schema。
""".strip()


class ToolAgent:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger
        self.client = LLMClient()
        self.settings = get_settings()

        self.tools_schema: list[dict[str, Any]] = [
            {
                "type": "function",
                "function": {
                    "name": "calculator",
                    "description": "用于执行数学表达式计算，适合高确定性算术任务。",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "数学表达式，例如 12*(3+4)",
                            }
                        },
                        "required": ["expression"],
                        "additionalProperties": False,
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_current_time",
                    "description": "用于获取当前时间，可以指定时区。",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "timezone": {
                                "type": "string",
                                "description": "IANA 时区名称，例如 Asia/Shanghai",
                            }
                        },
                        "required": [],
                        "additionalProperties": False,
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "用于查询天气信息。本项目当前使用本地假数据。",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": "城市名称，例如 Chengdu、Beijing、Shanghai",
                            }
                        },
                        "required": ["city"],
                        "additionalProperties": False,
                    },
                },
            },
        ]

    def run(self, user_query: str) -> str:
        self.logger.info("收到用户问题：%s", user_query)

        messages: list[dict[str, Any]] = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
        ]

        try:
            response = self.client.create_chat_completion(
                messages=messages,
                tools=self.tools_schema,
            )
            self.logger.info("首次模型响应：\n%s", self.client.dump_response(response))

            function_calls = self.client.extract_function_calls(response)

            if not function_calls:
                direct_answer = self.client.extract_text(response)
                self.logger.info("未触发工具调用，直接回答：%s", direct_answer)
                return direct_answer or "模型未返回有效内容。"

            # 把 assistant 的完整 tool_call 消息加回 messages
            assistant_message = self._build_assistant_tool_call_message(response)
            messages.append(assistant_message)

            # 执行工具，并把 role=tool 的结果回填
            for call in function_calls:
                tool_message = self._handle_function_call(call)
                messages.append(tool_message)

            followup_response = self.client.create_chat_completion(
                messages=messages,
                tools=self.tools_schema,
            )
            self.logger.info("工具回传后的模型响应：\n%s", self.client.dump_response(followup_response))

            final_answer = self.client.extract_text(followup_response)
            return final_answer or "工具执行完成，但模型未生成最终回答。"

        except Exception as e:
            self.logger.exception("Agent 执行失败：%s", e)
            return "系统执行失败，请检查日志。"

    def _handle_function_call(self, call: dict[str, Any]) -> dict[str, Any]:
        name = call["name"]
        call_id = call["id"]
        raw_arguments = call["arguments"]

        self.logger.info(
            "触发工具调用：name=%s, call_id=%s, arguments=%s",
            name,
            call_id,
            raw_arguments,
        )

        try:
            arguments = json.loads(raw_arguments)
        except json.JSONDecodeError:
            tool_result = {
                "ok": False,
                "tool_name": name,
                "error": "工具参数不是合法 JSON。",
            }
            return self._build_tool_message(call_id, tool_result)

        try:
            if name == "calculator":
                parsed = CalculatorArgs(**arguments)
                tool_result = run_calculator(parsed.expression)

            elif name == "get_current_time":
                parsed = TimeArgs(**arguments)
                timezone_name = parsed.timezone or self.settings.timezone
                tool_result = run_time_tool(timezone_name)

            elif name == "get_weather":
                parsed = WeatherArgs(**arguments)
                tool_result = run_weather_tool(parsed.city)

            else:
                tool_result = {
                    "ok": False,
                    "tool_name": name,
                    "error": f"未知工具：{name}",
                }

        except ValidationError as e:
            tool_result = {
                "ok": False,
                "tool_name": name,
                "error": "工具参数校验失败。",
                "details": e.errors(),
            }
        except Exception as e:
            tool_result = {
                "ok": False,
                "tool_name": name,
                "error": f"工具执行异常：{str(e)}",
            }

        self.logger.info("工具执行结果：%s", tool_result)
        return self._build_tool_message(call_id, tool_result)

    @staticmethod
    def _build_tool_message(call_id: str, result: dict[str, Any]) -> dict[str, Any]:
        return {
            "role": "tool",
            "tool_call_id": call_id,
            "content": json.dumps(result, ensure_ascii=False),
        }

    @staticmethod
    def _build_assistant_tool_call_message(response: Any) -> dict[str, Any]:
        message = response.choices[0].message
        tool_calls = getattr(message, "tool_calls", None) or []

        assistant_message: dict[str, Any] = {
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": [],
        }

        for tool_call in tool_calls:
            assistant_message["tool_calls"].append(
                {
                    "id": tool_call.id,
                    "type": tool_call.type,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
            )

        return assistant_message