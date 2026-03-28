from src.tools.weather_tool import run_weather_tool


def test_weather_tool_success():
    result = run_weather_tool("Chengdu")
    assert result["ok"] is True
    assert result["city"] == "Chengdu"


def test_weather_tool_not_found():
    result = run_weather_tool("Guangzhou")
    assert result["ok"] is False
    assert "未找到城市" in result["error"]