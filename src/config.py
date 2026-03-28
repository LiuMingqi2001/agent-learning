import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    provider: str = os.getenv("PROVIDER", "openai")
    model: str = os.getenv("MODEL", "gpt-4.1-mini")
    api_key: str = os.getenv("API_KEY", "")
    base_url: str | None = os.getenv("BASE_URL") or None
    temperature: float = float(os.getenv("TEMPERATURE", "0"))
    timezone: str = os.getenv("TIMEZONE", "Asia/Shanghai")


def get_settings() -> Settings:
    settings = Settings()
    if not settings.api_key:
        raise ValueError("API_KEY 未配置，请检查 .env 文件。")
    return settings