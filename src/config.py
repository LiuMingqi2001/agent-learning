import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    provider: str = os.getenv("PROVIDER", "qwen")
    model: str = os.getenv("MODEL", "qwen-turbo")
    api_key: str = os.getenv("API_KEY", "")
    base_url: str = os.getenv(
        "BASE_URL",
        "https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    use_chat_completions: bool = os.getenv("USE_CHAT_COMPLETIONS", "0") == "1"
    disable_tracing: bool = os.getenv("DISABLE_TRACING", "1") == "1"
    timezone: str = os.getenv("TIMEZONE", "Asia/Shanghai")
    default_weather_city: str = os.getenv("WEATHER_CITY", "Chengdu")


def get_settings() -> Settings:
    return Settings()