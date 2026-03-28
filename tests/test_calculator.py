from src.tools.calculator_tool import run_calculator


def test_calculator_add():
    result = run_calculator("1+2")
    assert result["ok"] is True
    assert result["result"] == 3.0


def test_calculator_complex():
    result = run_calculator("2*(3+4)")
    assert result["ok"] is True
    assert result["result"] == 14.0


def test_calculator_zero_division():
    result = run_calculator("1/0")
    assert result["ok"] is False
    assert "除零" in result["error"]