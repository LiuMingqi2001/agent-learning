# 工具 Schema 设计文档

## 1. 文档目标

本项目通过结构化 schema 约束工具参数输入，目标包括：

- 让工具调用更稳定
- 让参数可校验
- 让日志和调试更清晰
- 让项目便于扩展

---

## 2. 总体设计原则

### 2.1 参数尽量精简
每个工具只保留完成任务所需的最少参数，减少模型生成参数时出错的概率。

### 2.2 字段语义清晰
每个字段都提供明确 description，帮助模型正确理解参数含义。

### 2.3 禁止多余字段
schema 中设置 `additionalProperties: false`，防止模型传入无关字段。

### 2.4 先校验，后执行
工具执行前先使用 Pydantic 校验参数格式，避免非法输入进入工具层。

---

## 3. calculator

### 功能
执行数学表达式计算。

### Schema

```json
{
  "type": "object",
  "properties": {
    "expression": {
      "type": "string",
      "description": "需要计算的数学表达式，例如 12*(3+4)"
    }
  },
  "required": ["expression"],
  "additionalProperties": false
}
````

### 对应 Pydantic

* `CalculatorArgs`

### 设计理由

* 数学计算只需一个表达式字段
* 不把表达式拆成多个参数，降低复杂度

---

## 4. get_current_time

### 功能

获取当前时间。

### Schema

```json
{
  "type": "object",
  "properties": {
    "timezone": {
      "type": "string",
      "description": "IANA 时区名称，例如 Asia/Shanghai"
    }
  },
  "required": [],
  "additionalProperties": false
}
```

### 对应 Pydantic

* `TimeArgs`

### 设计理由

* 时区参数可选
* 若为空，则默认使用系统配置值

---

## 5. get_weather

### 功能

查询天气假数据。

### Schema

```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string",
      "description": "城市名称，例如 Chengdu"
    }
  },
  "required": ["city"],
  "additionalProperties": false
}
```

### 对应 Pydantic

* `WeatherArgs`

### 设计理由

* 当前仅做天气假数据查询器
* 城市名是唯一必要参数
* 后续可扩展更多字段

---

## 6. 错误处理策略

### 6.1 JSON 解析错误

如果模型返回的 arguments 不是合法 JSON，则不执行工具，直接返回结构化错误。

### 6.2 参数校验错误

如果字段缺失、类型错误或字段名不匹配，则由 Pydantic 拦截并返回错误信息。

### 6.3 工具执行错误

工具内部出现异常时，返回统一结构：

```json
{
  "ok": false,
  "tool_name": "tool_name",
  "error": "具体错误信息"
}
```

---

## 7. 后续优化方向

* 为数学表达式增加长度限制
* 为城市字段增加合法值枚举
* 为时区增加预检查
* 统一抽象工具基类

