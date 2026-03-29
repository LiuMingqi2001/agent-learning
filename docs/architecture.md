# Agent 结构图

```mermaid
flowchart TD
    U[用户输入] --> T[Triage Agent]

    T -->|工具调用| C[Calculator Tool]
    T -->|工具调用| TI[Time Tool]
    T -->|工具调用| W[Weather Tool]

    T -->|handoff| E[Explainer Agent]
    T -->|handoff| R[Retriever Agent]

    R -->|调用| RT[Retrieval Tool]

    C --> T
    TI --> T
    W --> T
    E --> T
    RT --> R
    R --> T

    T --> O[最终输出]
    T --> L[本地 Trace 日志]