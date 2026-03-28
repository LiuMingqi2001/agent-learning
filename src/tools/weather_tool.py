from typing import Any


_FAKE_WEATHER_DB = {
    "chengdu": {
        "city": "Chengdu",
        "weather": "Cloudy",
        "temperature_c": 22,
        "humidity": 68,
    },
    "beijing": {
        "city": "Beijing",
        "weather": "Sunny",
        "temperature_c": 26,
        "humidity": 40,
    },
    "shanghai": {
        "city": "Shanghai",
        "weather": "Rainy",
        "temperature_c": 24,
        "humidity": 82,
    },
}


def run_weather_tool(city: str) -> dict[str, Any]:
    city_key = city.strip().lower()

    if city_key not in _FAKE_WEATHER_DB:
        return {
            "ok": False,
            "tool_name": "get_weather",
            "error": (
                f"未找到城市 {city} 的天气假数据。"
                f"当前仅支持：{', '.join(_FAKE_WEATHER_DB.keys())}"
            ),
        }

    weather_info = _FAKE_WEATHER_DB[city_key]
    return {
        "ok": True,
        "tool_name": "get_weather",
        **weather_info,
    }