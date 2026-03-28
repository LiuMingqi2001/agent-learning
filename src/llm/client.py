import json
from typing import Any

from openai import OpenAI

from src.config import get_settings


class LLMClient:
    def __init__(self) -> None:
        settings = get_settings()
        self.settings = settings

        client_kwargs: dict[str, Any] = {
            "api_key": settings.api_key,
        }
        if settings.base_url:
            client_kwargs["base_url"] = settings.base_url

        self.client = OpenAI(**client_kwargs)
        self.model = settings.model

    def simple_chat(self, user_query: str, system_prompt: str | None = None) -> str:
        prompt = system_prompt or "你是一个 helpful assistant。请直接回答用户问题。"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_query},
            ],
        )
        return self.extract_text(response)

    def create_chat_completion(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
    ) -> Any:
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
        }

        if tools:
            kwargs["tools"] = tools
            # MiniMax 文档里的 OpenAI SDK tool use 示例会配 reasoning_split
            kwargs["extra_body"] = {"reasoning_split": True}

        return self.client.chat.completions.create(**kwargs)

    @staticmethod
    def extract_text(response: Any) -> str:
        try:
            message = response.choices[0].message
            content = getattr(message, "content", None)

            if content is None:
                return ""

            if isinstance(content, str):
                return content.strip()

            # 兼容某些 content 为分块结构的情况
            if isinstance(content, list):
                texts: list[str] = []
                for item in content:
                    if isinstance(item, dict):
                        if item.get("type") in ("text", "output_text", "input_text"):
                            text_value = item.get("text", "")
                            if text_value:
                                texts.append(text_value)
                    else:
                        text_value = getattr(item, "text", None)
                        if text_value:
                            texts.append(text_value)
                return "\n".join(texts).strip()

            return str(content).strip()
        except Exception:
            return ""

    @staticmethod
    def extract_function_calls(response: Any) -> list[dict[str, Any]]:
        calls: list[dict[str, Any]] = []

        try:
            message = response.choices[0].message
            tool_calls = getattr(message, "tool_calls", None) or []

            for tool_call in tool_calls:
                function_obj = getattr(tool_call, "function", None)
                calls.append(
                    {
                        "id": getattr(tool_call, "id", ""),
                        "type": getattr(tool_call, "type", ""),
                        "name": getattr(function_obj, "name", ""),
                        "arguments": getattr(function_obj, "arguments", "{}"),
                    }
                )
        except Exception:
            pass

        return calls

    @staticmethod
    def dump_response(response: Any) -> str:
        try:
            return json.dumps(response.model_dump(), ensure_ascii=False, indent=2)
        except Exception:
            return str(response)