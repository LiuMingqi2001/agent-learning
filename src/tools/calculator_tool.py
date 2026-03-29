from __future__ import annotations

import ast
import operator as op
from typing import Any

from agents import function_tool


_ALLOWED_OPERATORS: dict[type[Any], Any] = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}


def _safe_eval(node: ast.AST) -> float:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ValueError("只允许数字常量。")

    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        operator_type = type(node.op)
        if operator_type not in _ALLOWED_OPERATORS:
            raise ValueError("不支持的运算符。")
        return float(_ALLOWED_OPERATORS[operator_type](left, right))

    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        operator_type = type(node.op)
        if operator_type not in _ALLOWED_OPERATORS:
            raise ValueError("不支持的一元运算符。")
        return float(_ALLOWED_OPERATORS[operator_type](operand))

    raise ValueError("非法表达式。")


def run_calculator(expression: str) -> dict[str, Any]:
    try:
        parsed = ast.parse(expression, mode="eval")
        result = _safe_eval(parsed.body)
        return {
            "ok": True,
            "tool_name": "calculator",
            "expression": expression,
            "result": result,
        }
    except Exception as e:  # noqa: BLE001
        return {
            "ok": False,
            "tool_name": "calculator",
            "expression": expression,
            "error": f"计算失败：{e}",
        }


@function_tool
def calculate(expression: str) -> str:
    """
    安全计算一个数学表达式，例如：
    2*(3+4), 3**2 + 5, 10/4
    """
    result = run_calculator(expression)
    if result["ok"]:
        return f"表达式 {result['expression']} 的结果为 {result['result']}。"
    return result["error"]