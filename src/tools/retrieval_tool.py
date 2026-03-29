from __future__ import annotations

from pathlib import Path

from agents import function_tool


DOC_DIR = Path("docs")


def _search_in_file(file_path: Path, query: str) -> list[str]:
    matches: list[str] = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:  # noqa: BLE001
        return matches

    query_lower = query.lower()
    for line in content.splitlines():
        if query_lower in line.lower():
            line = line.strip()
            if line:
                matches.append(line)
    return matches


def run_retrieval(query: str) -> str:
    if not DOC_DIR.exists():
        return "未找到 docs 目录，无法进行本地检索。"

    all_hits: list[str] = []

    for file_path in DOC_DIR.rglob("*"):
        if file_path.is_file() and file_path.suffix in {".md", ".txt"}:
            hits = _search_in_file(file_path, query)
            for hit in hits[:5]:
                all_hits.append(f"[{file_path.name}] {hit}")

    if not all_hits:
        return f"未在本地文档中检索到与“{query}”直接相关的内容。"

    preview = "\n".join(all_hits[:10])
    return f"本地检索结果如下：\n{preview}"


@function_tool
def retrieve_project_notes(query: str) -> str:
    """
    从本地 docs 目录中检索与问题相关的内容。
    """
    return run_retrieval(query)