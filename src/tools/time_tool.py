from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo


def run_time_tool(timezone_name: str = "Asia/Shanghai") -> dict[str, Any]:
    try:
        now = datetime.now(ZoneInfo(timezone_name))
        return {
            "ok": True,
            "tool_name": "get_current_time",
            "timezone": timezone_name,
            "iso_time": now.isoformat(),
            "formatted_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "weekday": now.strftime("%A"),
        }
    except Exception:
        return {
            "ok": False,
            "tool_name": "get_current_time",
            "error": f"无法获取时区 {timezone_name} 的当前时间。",
        }