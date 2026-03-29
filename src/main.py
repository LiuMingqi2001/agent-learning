from __future__ import annotations

import asyncio

from src.llm.provider import setup_provider
from src.logger import setup_logger
from src.workflows.qa_workflow import run_qa_streamed


logger = setup_logger("main")


async def main() -> None:
    setup_provider()

    print("=== Agent Learning Week 3 Demo (Qwen + Agents SDK) ===")
    print("输入 quit 或 exit 退出。")

    while True:
        user_input = input("\n请输入问题：").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("已退出。")
            break

        if not user_input:
            print("输入不能为空。")
            continue

        try:
            answer = await run_qa_streamed(user_input)
            print("\n最终答案：")
            print(answer)
        except Exception as e:  # noqa: BLE001
            logger.exception("agent 运行失败")
            print(f"\n运行失败：{e}")


if __name__ == "__main__":
    asyncio.run(main())