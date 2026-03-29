[//]: # (# agent-learning)

[//]: # ()
[//]: # (一个用于系统学习 Agent 开发的渐进式项目。)

[//]: # ()
[//]: # (当前项目包含两个阶段：)

[//]: # ()
[//]: # (- **第一阶段**：最小 LLM 调用脚本 `hello_llm.py`)

[//]: # (- **第二阶段**：支持单轮 tool calling 的最小 Agent `main.py`)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 1. 项目目标)

[//]: # ()
[//]: # (通过逐步迭代，掌握以下能力：)

[//]: # ()
[//]: # (- LLM API 基础调用)

[//]: # (- 日志、配置、异常处理)

[//]: # (- Responses API 基础)

[//]: # (- tool/function calling)

[//]: # (- 结构化 schema 设计)

[//]: # (- 工具结果回传模型)

[//]: # (- 最小 Agent 骨架搭建)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 2. 当前项目结构)

[//]: # ()
[//]: # (```bash)

[//]: # (agent-learning/)

[//]: # (├─ src/)

[//]: # (│  ├─ main.py)

[//]: # (│  ├─ config.py)

[//]: # (│  ├─ logger.py)

[//]: # (│  ├─ hello_llm.py)

[//]: # (│  ├─ llm/)

[//]: # (│  │  └─ client.py)

[//]: # (│  ├─ agent/)

[//]: # (│  │  └─ tool_agent.py)

[//]: # (│  ├─ schemas/)

[//]: # (│  │  ├─ calculator_schema.py)

[//]: # (│  │  ├─ time_schema.py)

[//]: # (│  │  └─ weather_schema.py)

[//]: # (│  └─ tools/)

[//]: # (│     ├─ calculator_tool.py)

[//]: # (│     ├─ time_tool.py)

[//]: # (│     └─ weather_tool.py)

[//]: # (├─ tests/)

[//]: # (│  ├─ test_calculator.py)

[//]: # (│  ├─ test_time_tool.py)

[//]: # (│  └─ test_weather_tool.py)

[//]: # (├─ scripts/)

[//]: # (├─ data/)

[//]: # (├─ docs/)

[//]: # (│  ├─ tool_schema_design.md)

[//]: # (│  └─ tool_calling_policy.md)

[//]: # (├─ logs/)

[//]: # (├─ README.md)

[//]: # (├─ requirements.txt)

[//]: # (└─ .env)

[//]: # (````)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 3. 第一阶段：最小 LLM 调用)

[//]: # ()
[//]: # (入口文件：)

[//]: # ()
[//]: # (```bash)

[//]: # (python -m src.hello_llm)

[//]: # (```)

[//]: # ()
[//]: # (功能：)

[//]: # ()
[//]: # (* 输入一个问题)

[//]: # (* 调用模型返回答案)

[//]: # (* 记录日志)

[//]: # (* 作为项目最小基线版本存在)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 4. 第二阶段：最小 Tool Agent)

[//]: # ()
[//]: # (入口文件：)

[//]: # ()
[//]: # (```bash)

[//]: # (python -m src.main)

[//]: # (```)

[//]: # ()
[//]: # (功能：)

[//]: # ()
[//]: # (* 用户问数学题时调用计算器)

[//]: # (* 用户问当前时间时调用时间工具)

[//]: # (* 用户问天气时调用天气假数据工具)

[//]: # (* 其他问题直接回答)

[//]: # (* 工具参数经过 schema 校验)

[//]: # (* 工具结果回传模型，由模型生成最终回答)

[//]: # (* 工具失败时进行降级处理)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 5. 安装与运行)

[//]: # ()
[//]: # (### 5.1 创建虚拟环境)

[//]: # ()
[//]: # (```bash)

[//]: # (conda create -n agent-learning python=3.11 -y)

[//]: # (conda activate agent-learning)

[//]: # (```)

[//]: # ()
[//]: # (或：)

[//]: # ()
[//]: # (```bash)

[//]: # (python -m venv .venv)

[//]: # (```)

[//]: # ()
[//]: # (Windows 激活：)

[//]: # ()
[//]: # (```bash)

[//]: # (.venv\Scripts\activate)

[//]: # (```)

[//]: # ()
[//]: # (Linux / macOS 激活：)

[//]: # ()
[//]: # (```bash)

[//]: # (source .venv/bin/activate)

[//]: # (```)

[//]: # ()
[//]: # (### 5.2 安装依赖)

[//]: # ()
[//]: # (```bash)

[//]: # (pip install -r requirements.txt)

[//]: # (```)

[//]: # ()
[//]: # (### 5.3 配置 `.env`)

[//]: # ()
[//]: # (你可以直接创建 `.env` 文件，内容参考：)

[//]: # ()
[//]: # (```env)

[//]: # (PROVIDER=openai)

[//]: # (MODEL=gpt-4.1-mini)

[//]: # (API_KEY=your_api_key_here)

[//]: # (BASE_URL=)

[//]: # (TEMPERATURE=0)

[//]: # (TIMEZONE=Asia/Shanghai)

[//]: # (```)

[//]: # ()
[//]: # (### 5.4 运行第一阶段)

[//]: # ()
[//]: # (```bash)

[//]: # (python -m src.hello_llm)

[//]: # (```)

[//]: # ()
[//]: # (### 5.5 运行第二阶段)

[//]: # ()
[//]: # (```bash)

[//]: # (python -m src.main)

[//]: # (```)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 6. 示例问题)

[//]: # ()
[//]: # (### 数学计算)

[//]: # ()
[//]: # (* `123*&#40;45+6&#41; 等于多少？`)

[//]: # (* `帮我算一下 2 的 10 次方`)

[//]: # ()
[//]: # (### 时间查询)

[//]: # ()
[//]: # (* `现在几点了？`)

[//]: # (* `帮我查一下 Asia/Tokyo 当前时间`)

[//]: # ()
[//]: # (### 天气查询)

[//]: # ()
[//]: # (* `成都天气怎么样？`)

[//]: # (* `Beijing weather?`)

[//]: # ()
[//]: # (### 普通问答)

[//]: # ()
[//]: # (* `什么是 tool calling？`)

[//]: # (* `为什么 Agent 开发不能只靠 prompt？`)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 7. 为什么这里要用工具，不直接让模型算)

[//]: # ()
[//]: # (像数学计算、当前时间、天气查询这类任务具有以下特点：)

[//]: # ()
[//]: # (* 对结果正确性要求高)

[//]: # (* 部分信息依赖实时状态)

[//]: # (* 更适合通过确定性工具完成)

[//]: # ()
[//]: # (因此本项目中：)

[//]: # ()
[//]: # (* 模型负责理解意图和组织语言)

[//]: # (* 工具负责提供高确定性或实时结果)

[//]: # ()
[//]: # (这样做能提高准确率、可控性和可解释性。)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 8. 工具失败时怎么降级)

[//]: # ()
[//]: # (本项目遵循以下原则：)

[//]: # ()
[//]: # (1. 工具失败时不伪造结果)

[//]: # (2. 返回结构化错误信息)

[//]: # (3. 让模型基于错误信息生成用户可理解的说明)

[//]: # ()
[//]: # (例如：)

[//]: # ()
[//]: # (* 计算器表达式非法 -> 提示检查表达式格式)

[//]: # (* 时区无效 -> 提示无法获取该时区当前时间)

[//]: # (* 城市不在天气假数据中 -> 提示当前支持的城市范围)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 9. 输入格式错了怎么处理)

[//]: # ()
[//]: # (每个工具在执行前都经过 Pydantic schema 校验：)

[//]: # ()
[//]: # (* 字段缺失)

[//]: # (* 字段类型错误)

[//]: # (* 参数命名错误)

[//]: # ()
[//]: # (都会被拦截并返回结构化错误，而不会直接导致主流程崩溃。)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 10. 当前学习成果对应关系)

[//]: # ()
[//]: # (### 第 1 周)

[//]: # ()
[//]: # (* 最小 API 调用)

[//]: # (* 日志)

[//]: # (* 配置管理)

[//]: # (* 项目结构初始化)

[//]: # ()
[//]: # (### 第 2 周)

[//]: # ()
[//]: # (* Responses API 基础)

[//]: # (* tool calling)

[//]: # (* schema 设计)

[//]: # (* 工具回传模型)

[//]: # (* 单 Agent + 单轮工具调用 demo)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (## 11. 后续扩展方向)

[//]: # ()
[//]: # (* 增加更多工具)

[//]: # (* 支持多轮工具调用)

[//]: # (* 接入真实天气 API)

[//]: # (* 增加 FastAPI 服务层)

[//]: # (* 增加测试覆盖率)

[//]: # (* 增加更精细的工具路由逻辑)

[//]: # (---)

[//]: # ()



---

# agent-learning

一个面向初学者的 **Agent 学习项目**，用于逐步实践以下核心能力：

* 基于 **OpenAI Agents SDK** 构建多 Agent 架构
* 使用 **tool calling** 实现计算、时间、天气、本地检索等能力
* 使用 **handoff** 实现主 Agent 到子 Agent 的任务转交
* 通过本地 trace 日志理解 Agent 的执行链路
* 基于 OpenAI-compatible 接口尝试接入第三方模型服务

当前项目使用 **Qwen API（OpenAI-compatible）** 进行接入，但项目整体架构仍然是**基于 OpenAI Agents SDK**设计与实现的。
项目当前重点在于：**学习 Agent 架构、工具调用、handoff 机制、日志排查方法，以及 OpenAI-compatible provider 接入实践。**

---

## 1. 项目目标

本项目不是一个完整的生产级 Agent 系统，而是一个循序渐进的学习项目。
通过本项目，你可以理解并实践：

1. 如何组织一个基础的 Agent 项目目录结构
2. 如何定义多个 Agent，并为不同任务分配职责
3. 如何为 Agent 挂载工具
4. 如何在多 Agent 之间进行 handoff
5. 如何记录 trace 日志，并分析 Agent 的执行过程
6. 如何将 OpenAI Agents SDK 与 OpenAI-compatible 模型服务结合使用

---

## 2. 当前功能概览

当前项目设计了以下 Agent 与工具能力：

### 2.1 Agent 结构

* **Triage Agent**

  * 系统主入口
  * 负责接收用户请求并进行轻量路由
  * 对计算、时间、天气问题优先调用工具
  * 对代码解释、报错分析等问题 handoff 给 Explainer Agent
  * 对项目文档、本地资料检索等问题 handoff 给 Retriever Agent 

* **Explainer Agent**

  * 负责解释代码、报错、技术概念、工具结果
  * 回答风格偏清晰、结构化、适合初学者 

* **Retriever Agent**

  * 负责从本地 `docs/` 目录检索学习资料或项目文档
  * 优先调用本地检索工具 `retrieve_project_notes` 

### 2.2 已实现工具

* **calculate**

  * 安全计算数学表达式，例如 `2*(3+4)`、`10/4` 等 

* **get_current_time**

  * 获取指定时区的当前时间，例如 `Asia/Shanghai`、`UTC` 等 

* **get_weather**

  * 当前为演示版天气工具，返回固定格式的占位数据，后续可替换为真实天气 API 

* **retrieve_project_notes**

  * 从本地 `docs/` 目录中检索 `.md` 或 `.txt` 文件内容 

### 2.3 工作流与日志

* 主入口为 `src/main.py`，负责接收用户输入并运行问答流程 
* 问答流程位于 `src/workflows/qa_workflow.py`，使用 `Runner.run()` / `Runner.run_streamed()` 执行 Agent 
* 本地 trace 日志由 `LocalTraceLogger` 写入 `logs/agent_trace.log`，用于分析一次请求的完整执行链路 

---

## 3. 项目目录结构

下面是推荐的项目组织方式：

```text
agent-learning/
├─ src/
│  ├─ app_agents/
│  │  ├─ triage_agent.py
│  │  ├─ explainer_agent.py
│  │  └─ retriever_agent.py
│  ├─ llm/
│  │  └─ provider.py
│  ├─ tools/
│  │  ├─ calculator_tool.py
│  │  ├─ time_tool.py
│  │  ├─ weather_tool.py
│  │  └─ retrieval_tool.py
│  ├─ tracing/
│  │  └─ trace_logger.py
│  ├─ workflows/
│  │  └─ qa_workflow.py
│  ├─ config.py
│  ├─ logger.py
│  └─ main.py
├─ docs/
├─ logs/
├─ .env
├─ requirements.txt
└─ README.md
```

---

## 4. 环境要求

建议使用：

* Python 3.10 及以上
* 已安装 `openai`
* 已安装 `python-dotenv`
* 已安装 OpenAI Agents SDK 相关依赖

如果你使用 Conda：

```bash
conda create -n agent-learning python=3.10 -y
conda activate agent-learning
```

---

## 5. 安装依赖

如果你已有 `requirements.txt`，直接安装：

```bash
pip install -r requirements.txt
```

如果你暂时没有完整依赖文件，至少需要保证安装了以下核心包：

```bash
pip install openai python-dotenv
```

以及你当前使用版本对应的 Agents SDK 包。

---

## 6. 配置 `.env`

项目通过 `.env` 读取模型服务配置。
当前默认使用 **Qwen OpenAI-compatible 接口**。

示例：

```env
PROVIDER=qwen
MODEL=qwen3-max
API_KEY=your_api_key
BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1

USE_CHAT_COMPLETIONS=0
DISABLE_TRACING=1
TIMEZONE=Asia/Shanghai
WEATHER_CITY=Chengdu
```

### 字段说明

* `PROVIDER`：当前 provider 名称，仅用于配置标识
* `MODEL`：模型名，例如 `qwen3-max`
* `API_KEY`：对应模型服务的 API Key
* `BASE_URL`：OpenAI-compatible 服务地址
* `USE_CHAT_COMPLETIONS`：

  * `0` 表示优先走 Responses 风格
  * `1` 表示优先走 Chat Completions 风格
* `DISABLE_TRACING`：

  * `1` 表示关闭官方 tracing，使用本地日志
* `TIMEZONE`：默认时区
* `WEATHER_CITY`：默认天气城市

---

## 7. 运行方式

在项目根目录运行：

```bash
python -m src.main
```

启动后，终端中输入问题即可，例如：

```text
2*(3+4) 等于多少
北京现在是几点
帮我解释下面的代码：print('hello world')
帮我检索 docs 里的学习笔记
```

---

## 8. 项目设计思路

### 8.1 Triage Agent 作为统一入口

`Triage Agent` 是系统主入口，它的职责不是完成所有任务，而是根据用户请求判断：

* 是否应该调用工具
* 是否应该直接回答
* 是否应该把任务转交给其他 Agent

当前规则主要包括：

1. 数学计算问题，调用 `calculate`
2. 当前时间、时区时间问题，调用 `get_current_time`
3. 天气问题，调用 `get_weather`
4. 解释代码、解释报错、解释概念的问题，handoff 给 `Explainer Agent`
5. 项目文档、本地资料检索类问题，handoff 给 `Retriever Agent`
6. 普通知识问答直接回答 

### 8.2 子 Agent 职责单一化

项目有意将不同任务拆分为不同 Agent：

* `Explainer Agent` 只负责解释类任务
* `Retriever Agent` 只负责检索类任务

这样做的目的是帮助学习者理解：
**Agent 并不一定是“一个万能助手”，而可以是多个职责清晰的小 Agent 协同完成任务。**

### 8.3 本地日志辅助理解 Agent 执行过程

项目中使用 `LocalTraceLogger` 将关键过程写入日志，包括：

* 用户输入
* 初始 Agent 选择
* stream 事件
* 最终输出

这样做的意义在于：

* 方便理解 Agent 的执行链路
* 方便排查 tool calling / handoff 问题
* 方便学习 SDK 在底层是如何推进流程的

---

## 9. 如何看日志

本项目调试时，最重要的日志文件是：

```text
logs/agent_trace.log
```

建议按一次请求的完整生命周期去看：

1. `user_input`
2. `agent_selected`
3. `stream_event`
4. `final_output`

### 重点关注的字段

* `event_type`
* `payload.type`
* `payload.name`
* `payload.new_agent`
* `payload.output`
* `payload.error`

### 常见判断方法

#### 看是否正确进入主 Agent

关注：

* `agent_selected`

#### 看是否触发工具调用

关注：

* `run_item_stream_event`
* `tool_called`
* `tool_output`

#### 看是否发生 handoff

关注：

* `handoff_requested`
* `handoff_occured`
* `agent_updated_stream_event`

#### 看参数是否正确

关注：

* `response.function_call_arguments.delta`
* `response.function_call_arguments.done`

#### 看最终是否成功回答

关注：

* `final_output.output`

如果 `final_output.output` 为空，通常说明执行链路中途失败，虽然流程结束了，但没有产出最终答案。

---

## 10. 当前已知问题：Qwen 与 Agents SDK 的兼容性限制

这是当前项目最重要的现实说明。

### 10.1 问题现象

当项目接入 **Qwen OpenAI-compatible 接口** 并使用 OpenAI Agents SDK 时：

* **普通单轮直接问答** 通常可以正常工作
* **一旦触发 tool calling 或 handoff**，后续续轮生成可能失败

在本项目的真实日志中，已经观察到两类典型失败：

#### 情况一：工具调用后失败

例如用户提问“北京现在是几点”，`Triage Agent` 已经成功调用 `get_current_time`，参数也已生成，但在工具输出之后，下一轮模型生成阶段失败，错误信息为：

* `tool must be one of user,assistant,system,function` 

#### 情况二：handoff 后失败

例如用户提问“帮我解释下面的代码：print('hello world')”，`Triage Agent` 已经成功 handoff 到 `Explainer Agent`，但切换后下一轮生成同样报错：

* `tool must be one of user,assistant,system,function` 

### 10.2 根因说明

从当前日志判断，问题不在于：

* 本地时间工具逻辑错误
* 本地计算工具逻辑错误
* `Triage Agent` 路由逻辑错误
* `Explainer Agent` 或 `Retriever Agent` 的基本设计错误

真正的问题在于：

**Qwen 当前这条 OpenAI-compatible 接口链路，对 OpenAI Agents SDK 自动生成的 tool / handoff 续轮消息协议兼容不完整。**

更具体地说：

* SDK 在 tool calling 或 handoff 之后，会继续组织一轮消息用于生成最终答案
* 在这个过程中，服务端校验消息角色时不接受 `role='tool'`
* 从而导致后续生成失败

### 10.3 这意味着什么

这意味着：

* **项目代码结构本身没有明显大问题**
* **核心问题是 provider 协议兼容性，而不是项目架构本身**
* 只要继续使用当前这条 Qwen 接口，SDK 的 `tools` 和 `handoffs` 能否完整跑通将受到限制

---

## 11. 如果换成 OpenAI 官方模型会怎样

如果将当前项目切换到 **OpenAI 官方模型与官方接口**，那么从当前项目代码结构来看：

* `Triage Agent` 的路由设计没有明显问题
* `Explainer Agent` 与 `Retriever Agent` 的职责划分没有明显问题
* `calculate`、`get_current_time`、`get_weather`、`retrieve_project_notes` 的工具设计作为学习项目是成立的
* `Runner.run()` / `Runner.run_streamed()` 的调用方式整体没有明显方向性错误
* trace 日志链路也已经基本具备排查价值

也就是说：

**如果换成 OpenAI 官方模型，本项目作为一个基于 SDK 的学习项目，整体上是可以继续沿用的，当前最主要的不稳定因素并不在项目自身，而在 Qwen 兼容接口与 SDK 的协议匹配度。**

---

## 12. 当前项目适合什么用途

当前阶段，这个项目非常适合：

* 学习 OpenAI Agents SDK 的基本结构
* 学习多 Agent 思维
* 学习 tool calling 与 handoff 的组织方式
* 学习如何设计本地 trace 日志
* 学习如何排查 Agent 执行链路
* 学习 OpenAI-compatible provider 接入时可能遇到的实际兼容性问题

但它**暂时不适合**直接作为一个稳定的、完全依赖 Qwen 接口的 SDK 多 Agent 工程模板投入长期使用。

---

## 13. 后续可改进方向

### 方向一：切换到 OpenAI 官方模型

这是最直接的方案。
如果你的目标是继续学习原生 SDK 的 tool calling 与 handoff，切换到 OpenAI 官方模型会更顺畅。

### 方向二：继续保留当前 SDK 版作为学习样例

即使当前 Qwen 下存在兼容性问题，这个项目仍然有学习价值。
它已经帮助你理解了：

* Agent 如何定义
* 工具如何挂载
* handoff 如何组织
* trace 日志如何排查

### 方向三：另做一个“手写路由版”

如果你的目标是先得到一个**稳定可运行版本**，可以单独保留一份“手写路由版”工作流，将：

* SDK 的自动 tools / handoffs
* 改为 Python 侧手动路由与函数调用

这样可以绕开 Qwen 当前接口的协议兼容问题。

---

## 14. 学习建议

推荐按下面顺序继续学习和迭代本项目：

1. 先理解当前 SDK 版目录结构
2. 通过日志看懂一次请求的完整执行链路
3. 理解 tool calling 与 handoff 的底层行为
4. 认识 OpenAI-compatible provider 不等于完全兼容 Agents SDK
5. 若继续深挖 SDK，用 OpenAI 官方模型验证项目链路
6. 若优先要“稳定运行”，另实现一版手写路由版

---

## 15. 总结

`agent-learning` 是一个以 **OpenAI Agents SDK** 为核心的学习项目。
它已经完成了从单 Agent 到多 Agent、从直接问答到工具调用、从功能实现到日志追踪的一套基础闭环。

当前项目在 **Qwen OpenAI-compatible 接口** 下暴露出的主要问题，不是项目架构设计错误，而是：

* **tool calling**
* **handoff**
* 以及它们后续续轮生成阶段

与当前 Qwen 接口的消息协议存在兼容性限制，导致部分链路无法完整跑通。

如果换成 **OpenAI 官方模型**，则从当前项目代码组织与执行链路来看，整体没有明显原则性问题，完全可以继续作为 SDK 学习项目向下扩展。

---

