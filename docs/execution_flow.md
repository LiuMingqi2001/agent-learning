# 执行流程

1. 用户输入问题
2. Triage Agent 接收请求并分析意图
3. 若属于数学、时间、天气类问题，则调用工具
4. 若属于解释类问题，则 handoff 给 Explainer Agent
5. 若属于检索类问题，则 handoff 给 Retriever Agent
6. 返回最终答案
7. 将执行过程写入本地 trace 日志

## 设计说明
本项目采用“单入口路由 agent + 专家子 agent + function tools”的轻量架构。

优点：
- 结构清晰
- 易于调试
- 适合学习 Agents SDK
- 方便后续扩展为多 agent 系统