from __future__ import annotations

from openai import AsyncOpenAI

from agents import (
    set_default_openai_api,
    set_default_openai_client,
    set_tracing_disabled,
)

from src.config import get_settings
from src.logger import setup_logger


logger = setup_logger("provider")


def build_openai_client() -> AsyncOpenAI:
    settings = get_settings()

    if not settings.api_key:
        raise ValueError("未检测到 API_KEY，请检查 .env 配置。")

    client = AsyncOpenAI(
        api_key=settings.api_key,
        base_url=settings.base_url,
    )
    return client


def setup_provider() -> None:
    """
    初始化 Agents SDK 运行环境。
    固定使用 Qwen 作为 OpenAI-compatible provider。
    """
    settings = get_settings()

    client = build_openai_client()
    set_default_openai_client(client)

    # 这里告诉 app_agents SDK 使用 openai-compatible chat/responses 接口
    set_default_openai_api("chat_completions" if settings.use_chat_completions else "responses")

    if settings.disable_tracing:
        set_tracing_disabled(True)
        logger.info("官方 tracing 已关闭，当前使用本地日志记录调用过程。")
    else:
        logger.info("官方 tracing 已开启。若 provider 非 OpenAI，可能需要额外 tracing export key。")


def get_default_model():
    """
    直接返回模型名，让 SDK 使用默认 provider/client 去解析。
    这是当前版本下最稳的写法。
    """
    settings = get_settings()
    return settings.model
