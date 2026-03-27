import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


def setup_logger() -> logging.Logger:
    """配置日志。"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    logger = logging.getLogger("hello_llm")
    logger.setLevel(logging.INFO)

    # 避免重复添加 handler
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_dir / "hello_llm.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def main() -> None:
    # 读取 .env
    load_dotenv()

    logger = setup_logger()

    provider = os.getenv("PROVIDER", "").strip()
    model = os.getenv("MODEL", "").strip()
    api_key = os.getenv("API_KEY", "").strip()
    base_url = os.getenv("BASE_URL", "").strip()

    if not provider:
        logger.error("未检测到 PROVIDER。")
        print("错误：未检测到 PROVIDER。")
        return

    if not model:
        logger.error("未检测到 MODEL。")
        print("错误：未检测到 MODEL。")
        return

    if not api_key:
        logger.error("未检测到 API_KEY。")
        print("错误：未检测到 API_KEY。")
        return

    if not base_url:
        logger.error("未检测到 BASE_URL。")
        print("错误：未检测到 BASE_URL。")
        return

    logger.info("当前 Provider: %s", provider)
    logger.info("当前 Model: %s", model)
    logger.info("当前 Base URL: %s", base_url)

    client = OpenAI(
                    api_key=api_key,
                    base_url=base_url
                    )

    question = input("请输入你的问题：").strip()
    if not question:
        logger.warning("用户输入为空。")
        print("问题不能为空。")
        return

    logger.info("用户问题：%s", question)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
            timeout=60,
        )

        answer = response.choices[0].message.content

        logger.info("模型回答：%s", answer)
        print("\n模型回答：")
        print(answer)

    except Exception as e:
        logger.exception("调用 OpenAI 接口失败：%s", str(e))
        print(f"调用失败：{e}")


if __name__ == "__main__":
    main()