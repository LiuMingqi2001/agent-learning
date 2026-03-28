import ast
import operator as op
from typing import Any


_ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


class CalculatorToolError(Exception):
    """计算器工具异常。"""


def _safe_eval(node: ast.AST) -> float:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise CalculatorToolError("表达式中包含非法常量。")

    if isinstance(node, ast.Num):  # 兼容旧写法
        return float(node.n)

    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        operator_type = type(node.op)
        if operator_type not in _ALLOWED_OPERATORS:
            raise CalculatorToolError("表达式中包含不支持的运算符。")
        return _ALLOWED_OPERATORS[operator_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        operator_type = type(node.op)
        if operator_type not in _ALLOWED_OPERATORS:
            raise CalculatorToolError("表达式中包含不支持的一元运算符。")
        return _ALLOWED_OPERATORS[operator_type](operand)

    raise CalculatorToolError("表达式格式非法。")


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
    except ZeroDivisionError:
        return {
            "ok": False,
            "tool_name": "calculator",
            "error": "除零错误，请检查表达式。",
        }
    except CalculatorToolError as e:
        return {
            "ok": False,
            "tool_name": "calculator",
            "error": str(e),
        }
    except Exception:
        return {
            "ok": False,
            "tool_name": "calculator",
            "error": "计算器执行失败，请检查输入表达式格式。",
        }