from src.tools.calculator_tool import run_calculator
from src.tools.time_tool import run_time_tool
from src.tools.weather_tool import run_weather_tool


def test_run_calculator_success() -> None:
    result = run_calculator("2*(3+4)")
    assert result["ok"] is True
    assert result["result"] == 14.0


def test_run_calculator_fail() -> None:
    result = run_calculator("__import__('os').system('rm -rf /')")
    assert result["ok"] is False


def test_run_time_tool() -> None:
    result = run_time_tool("Asia/Shanghai")
    assert result["ok"] is True
    assert "formatted_time" in result


def test_run_weather_tool() -> None:
    result = run_weather_tool("Chengdu")
    assert result["ok"] is True
    assert result["city"] == "Chengdu"