from pydantic import BaseModel, Field


class WeatherArgs(BaseModel):
    city: str = Field(
        ...,
        description="城市名称，例如 Chengdu、Beijing、Shanghai"
    )