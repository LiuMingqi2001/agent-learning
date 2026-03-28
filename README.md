# agent-learning

一个用于系统学习 Agent 开发的渐进式项目。

当前项目包含两个阶段：

- **第一阶段**：最小 LLM 调用脚本 `hello_llm.py`
- **第二阶段**：支持单轮 tool calling 的最小 Agent `main.py`

---

## 1. 项目目标

通过逐步迭代，掌握以下能力：

- LLM API 基础调用
- 日志、配置、异常处理
- Responses API 基础
- tool/function calling
- 结构化 schema 设计
- 工具结果回传模型
- 最小 Agent 骨架搭建

---

## 2. 当前项目结构

```bash
agent-learning/
├─ src/
│  ├─ main.py
│  ├─ config.py
│  ├─ logger.py
│  ├─ hello_llm.py
│  ├─ llm/
│  │  └─ client.py
│  ├─ agent/
│  │  └─ tool_agent.py
│  ├─ schemas/
│  │  ├─ calculator_schema.py
│  │  ├─ time_schema.py
│  │  └─ weather_schema.py
│  └─ tools/
│     ├─ calculator_tool.py
│     ├─ time_tool.py
│     └─ weather_tool.py
├─ tests/
│  ├─ test_calculator.py
│  ├─ test_time_tool.py
│  └─ test_weather_tool.py
├─ scripts/
├─ data/
├─ docs/
│  ├─ tool_schema_design.md
│  └─ tool_calling_policy.md
├─ logs/
├─ README.md
├─ requirements.txt
└─ .env
````

---

## 3. 第一阶段：最小 LLM 调用

入口文件：

```bash
python -m src.hello_llm
```

功能：

* 输入一个问题
* 调用模型返回答案
* 记录日志
* 作为项目最小基线版本存在

---

## 4. 第二阶段：最小 Tool Agent

入口文件：

```bash
python -m src.main
```

功能：

* 用户问数学题时调用计算器
* 用户问当前时间时调用时间工具
* 用户问天气时调用天气假数据工具
* 其他问题直接回答
* 工具参数经过 schema 校验
* 工具结果回传模型，由模型生成最终回答
* 工具失败时进行降级处理

---

## 5. 安装与运行

### 5.1 创建虚拟环境

```bash
conda create -n agent-learning python=3.11 -y
conda activate agent-learning
```

或：

```bash
python -m venv .venv
```

Windows 激活：

```bash
.venv\Scripts\activate
```

Linux / macOS 激活：

```bash
source .venv/bin/activate
```

### 5.2 安装依赖

```bash
pip install -r requirements.txt
```

### 5.3 配置 `.env`

你可以直接创建 `.env` 文件，内容参考：

```env
PROVIDER=openai
MODEL=gpt-4.1-mini
API_KEY=your_api_key_here
BASE_URL=
TEMPERATURE=0
TIMEZONE=Asia/Shanghai
```

### 5.4 运行第一阶段

```bash
python -m src.hello_llm
```

### 5.5 运行第二阶段

```bash
python -m src.main
```

---

## 6. 示例问题

### 数学计算

* `123*(45+6) 等于多少？`
* `帮我算一下 2 的 10 次方`

### 时间查询

* `现在几点了？`
* `帮我查一下 Asia/Tokyo 当前时间`

### 天气查询

* `成都天气怎么样？`
* `Beijing weather?`

### 普通问答

* `什么是 tool calling？`
* `为什么 Agent 开发不能只靠 prompt？`

---

## 7. 为什么这里要用工具，不直接让模型算

像数学计算、当前时间、天气查询这类任务具有以下特点：

* 对结果正确性要求高
* 部分信息依赖实时状态
* 更适合通过确定性工具完成

因此本项目中：

* 模型负责理解意图和组织语言
* 工具负责提供高确定性或实时结果

这样做能提高准确率、可控性和可解释性。

---

## 8. 工具失败时怎么降级

本项目遵循以下原则：

1. 工具失败时不伪造结果
2. 返回结构化错误信息
3. 让模型基于错误信息生成用户可理解的说明

例如：

* 计算器表达式非法 -> 提示检查表达式格式
* 时区无效 -> 提示无法获取该时区当前时间
* 城市不在天气假数据中 -> 提示当前支持的城市范围

---

## 9. 输入格式错了怎么处理

每个工具在执行前都经过 Pydantic schema 校验：

* 字段缺失
* 字段类型错误
* 参数命名错误

都会被拦截并返回结构化错误，而不会直接导致主流程崩溃。

---

## 10. 当前学习成果对应关系

### 第 1 周

* 最小 API 调用
* 日志
* 配置管理
* 项目结构初始化

### 第 2 周

* Responses API 基础
* tool calling
* schema 设计
* 工具回传模型
* 单 Agent + 单轮工具调用 demo

---

## 11. 后续扩展方向

* 增加更多工具
* 支持多轮工具调用
* 接入真实天气 API
* 增加 FastAPI 服务层
* 增加测试覆盖率
* 增加更精细的工具路由逻辑
---

