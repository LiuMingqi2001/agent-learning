from pydantic import BaseModel, Field


class TimeArgs(BaseModel):
    timezone: str | None = Field(
        default=None,
        description="IANA 时区名称，例如 Asia/Shanghai。可为空。"
    )