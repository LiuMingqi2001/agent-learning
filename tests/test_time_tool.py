from src.tools.time_tool import run_time_tool


def test_time_tool_success():
    result = run_time_tool("Asia/Shanghai")
    assert result["ok"] is True
    assert result["tool_name"] == "get_current_time"
    assert "formatted_time" in result


def test_time_tool_invalid_timezone():
    result = run_time_tool("Invalid/Timezone")
    assert result["ok"] is False
    assert "无法获取时区" in result["error"]