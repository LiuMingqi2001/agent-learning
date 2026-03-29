# Week 3 学习笔记：OpenAI Agents SDK

## 本周目标
基于 Qwen API 和 OpenAI Agents SDK，实现一个轻量级 agent 系统，具备以下能力：

- Agent 定义
- Tools 工具调用
- Handoffs 轻量路由
- Streaming 流式执行观察
- 本地 Trace 日志记录

## 当前系统结构
- Triage Agent：主路由
- Explainer Agent：负责解释代码、概念、报错
- Retriever Agent：负责本地文档检索

## 已接入工具
- calculate
- get_current_time
- get_weather
- retrieve_project_notes

## 当前 trace 策略
由于当前固定使用 Qwen 作为推理后端，本周优先使用本地 trace 日志。
日志文件路径：

`logs/agent_trace.log`

## 后续可扩展方向
- 接入真实天气 API
- 接入向量数据库，升级为正式 RAG
- 补充 OpenAI tracing export key，启用云端 traces dashboard
- 增加 guardrails
- 增加 session/memory