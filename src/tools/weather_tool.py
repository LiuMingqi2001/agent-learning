from __future__ import annotations

from typing import Any

from agents import function_tool

from src.config import get_settings


def run_weather_tool(city: str | None = None) -> dict[str, Any]:
    """
    当前为演示版天气工具。
    第 3 周重点是 Agents SDK 的工具调用流程，因此这里返回固定格式的占位结果。
    后续可替换为真实天气 API。
    """
    settings = get_settings()
    city_name = city or settings.default_weather_city

    return {
        "ok": True,
        "tool_name": "get_weather",
        "city": city_name,
        "weather": "晴",
        "temperature_c": 23,
        "humidity": "48%",
        "note": "当前为演示版天气数据，后续可接入真实天气 API。",
    }


@function_tool
def get_weather(city: str = "Chengdu") -> str:
    """
    获取指定城市天气。
    当前返回演示版天气结果。
    """
    result = run_weather_tool(city)
    if result["ok"]:
        return (
            f"{result['city']} 当前天气：{result['weather']}，"
            f"温度约 {result['temperature_c']}°C，"
            f"湿度 {result['humidity']}。"
            f"{result['note']}"
        )
    return f"无法获取 {city} 的天气信息。"