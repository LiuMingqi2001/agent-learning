from __future__ import annotations

from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

from agents import function_tool

from src.config import get_settings


def run_time_tool(timezone_name: str | None = None) -> dict[str, Any]:
    settings = get_settings()
    tz_name = timezone_name or settings.timezone

    try:
        now = datetime.now(ZoneInfo(tz_name))
        return {
            "ok": True,
            "tool_name": "get_current_time",
            "timezone": tz_name,
            "iso_time": now.isoformat(),
            "formatted_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "weekday": now.strftime("%A"),
        }
    except Exception:  # noqa: BLE001
        return {
            "ok": False,
            "tool_name": "get_current_time",
            "error": f"无法获取时区 {tz_name} 的当前时间。",
        }


@function_tool
def get_current_time(timezone_name: str = "Asia/Shanghai") -> str:
    """
    获取指定时区的当前时间。
    例如：Asia/Shanghai, Asia/Tokyo, UTC
    """
    result = run_time_tool(timezone_name)
    if result["ok"]:
        return (
            f"当前时区：{result['timezone']}；"
            f"时间：{result['formatted_time']}；"
            f"星期：{result['weekday']}。"
        )
    return result["error"]