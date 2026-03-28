from src.agent.tool_agent import ToolAgent
from src.logger import setup_logger


def main() -> None:
    logger = setup_logger("tool_agent")
    agent = ToolAgent(logger)

    print("=== tool_agent_basic ===")
    print("支持：数学计算 / 当前时间 / 天气假数据 / 普通问答")
    print("输入 quit / exit 退出。")

    while True:
        user_query = input("\n请输入问题：").strip()

        if user_query.lower() in {"quit", "exit"}:
            print("已退出。")
            break

        if not user_query:
            print("输入不能为空。")
            continue

        answer = agent.run(user_query)
        print(f"\n助手回答：{answer}")


if __name__ == "__main__":
    main()