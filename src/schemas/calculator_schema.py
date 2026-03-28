from pydantic import BaseModel, Field


class CalculatorArgs(BaseModel):
    expression: str = Field(
        ...,
        description="需要计算的数学表达式，例如 12*(3+4)"
    )