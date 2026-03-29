from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any


TRACE_LOG_PATH = Path("logs/agent_trace.log")
TRACE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


class LocalTraceLogger:
    def __init__(self) -> None:
        self.start_ts = time.time()

    def write_event(self, event_type: str, payload: dict[str, Any]) -> None:
        record = {
            "ts": time.strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": event_type,
            "payload": payload,
        }
        with TRACE_LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def elapsed_ms(self) -> int:
        return int((time.time() - self.start_ts) * 1000)