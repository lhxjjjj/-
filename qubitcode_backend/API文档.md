# QubitCode API 文档

## 概述

QubitCode API 提供了联系表单处理、定价方案管理和聊天功能的RESTful接口。

## 基础信息

- **基础URL**: `http://localhost:5000/api`
- **API版本**: v1
- **数据格式**: JSON
- **字符编码**: UTF-8

## 通用响应格式

成功响应：
```json
{
    "success": true,
    "data": {},
    "message": "操作成功"
}
```

错误响应：
```json
{
    "success": false,
    "error": "错误信息",
    "message": "操作失败"
}
```

## 联系表单 API

### 提交联系表单

**POST** `/api/contact/submit`

**请求体**：
```json
{
    "name": "张三",
    "email": "zhangsan@example.com",
    "company": "示例公司",
    "phone": "13800138000",
    "subject": "咨询产品",
    "message": "我想了解更多关于QubitCode的信息"
}
```

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "张三",
        "email": "zhangsan@example.com",
        "company": "示例公司",
        "phone": "13800138000",
        "subject": "咨询产品",
        "message": "我想了解更多关于QubitCode的信息",
        "created_at": "2023-01-01T12:00:00",
        "is_processed": false
    },
    "message": "联系表单提交成功"
}
```

### 获取联系表单列表

**GET** `/api/contact/list`

**查询参数**：
- `page`: 页码（默认：1）
- `per_page`: 每页数量（默认：10）
- `processed`: 是否已处理（可选）

**响应**：
```json
{
    "success": true,
    "data": {
        "contacts": [
            {
                "id": 1,
                "name": "张三",
                "email": "zhangsan@example.com",
                "company": "示例公司",
                "phone": "13800138000",
                "subject": "咨询产品",
                "message": "我想了解更多关于QubitCode的信息",
                "created_at": "2023-01-01T12:00:00",
                "is_processed": false
            }
        ],
        "total": 1,
        "pages": 1,
        "current_page": 1
    },
    "message": "获取联系表单列表成功"
}
```

### 获取联系表单详情

**GET** `/api/contact/{contact_id}`

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "张三",
        "email": "zhangsan@example.com",
        "company": "示例公司",
        "phone": "13800138000",
        "subject": "咨询产品",
        "message": "我想了解更多关于QubitCode的信息",
        "created_at": "2023-01-01T12:00:00",
        "is_processed": false
    },
    "message": "获取联系表单详情成功"
}
```

### 标记联系表单为已处理

**PUT** `/api/contact/{contact_id}/process`

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "张三",
        "email": "zhangsan@example.com",
        "company": "示例公司",
        "phone": "13800138000",
        "subject": "咨询产品",
        "message": "我想了解更多关于QubitCode的信息",
        "created_at": "2023-01-01T12:00:00",
        "is_processed": true
    },
    "message": "联系表单已标记为已处理"
}
```

### 删除联系表单

**DELETE** `/api/contact/{contact_id}`

**响应**：
```json
{
    "success": true,
    "message": "联系表单删除成功"
}
```

## 定价方案 API

### 获取所有定价方案

**GET** `/api/pricing/plans`

**响应**：
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "基础版",
            "price": 0,
            "currency": "CNY",
            "period": "月",
            "description": "适合个人用户和小型项目",
            "features": [
                "每月1000次对话",
                "基础代码生成",
                "社区支持",
                "基础模型访问"
            ],
            "is_popular": false,
            "is_active": true,
            "created_at": "2023-01-01T12:00:00",
            "updated_at": "2023-01-01T12:00:00"
        },
        {
            "id": 2,
            "name": "专业版",
            "price": 99,
            "currency": "CNY",
            "period": "月",
            "description": "适合专业开发者和小团队",
            "features": [
                "每月10000次对话",
                "高级代码生成",
                "优先技术支持",
                "高级模型访问",
                "代码审查功能",
                "团队协作工具"
            ],
            "is_popular": true,
            "is_active": true,
            "created_at": "2023-01-01T12:00:00",
            "updated_at": "2023-01-01T12:00:00"
        },
        {
            "id": 3,
            "name": "企业版",
            "price": 299,
            "currency": "CNY",
            "period": "月",
            "description": "适合大型企业和团队",
            "features": [
                "无限对话次数",
                "企业级代码生成",
                "专属技术支持",
                "定制模型访问",
                "高级代码审查",
                "完整团队协作",
                "私有部署选项",
                "API访问权限",
                "定制化服务"
            ],
            "is_popular": false,
            "is_active": true,
            "created_at": "2023-01-01T12:00:00",
            "updated_at": "2023-01-01T12:00:00"
        }
    ],
    "message": "获取定价方案列表成功"
}
```

### 创建定价方案

**POST** `/api/pricing/plans`

**请求体**：
```json
{
    "name": "新方案",
    "price": 199,
    "currency": "CNY",
    "period": "月",
    "description": "方案描述",
    "features": [
        "功能1",
        "功能2"
    ],
    "is_popular": false
}
```

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 4,
        "name": "新方案",
        "price": 199,
        "currency": "CNY",
        "period": "月",
        "description": "方案描述",
        "features": [
            "功能1",
            "功能2"
        ],
        "is_popular": false,
        "is_active": true,
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00"
    },
    "message": "定价方案创建成功"
}
```

### 获取单个定价方案

**GET** `/api/pricing/plans/{plan_id}`

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "基础版",
        "price": 0,
        "currency": "CNY",
        "period": "月",
        "description": "适合个人用户和小型项目",
        "features": [
            "每月1000次对话",
            "基础代码生成",
            "社区支持",
            "基础模型访问"
        ],
        "is_popular": false,
        "is_active": true,
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00"
    },
    "message": "获取定价方案详情成功"
}
```

### 更新定价方案

**PUT** `/api/pricing/plans/{plan_id}`

**请求体**：
```json
{
    "name": "更新的方案",
    "price": 299,
    "currency": "CNY",
    "period": "年",
    "description": "更新的描述",
    "features": [
        "更新的功能1",
        "更新的功能2"
    ],
    "is_popular": true
}
```

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "更新的方案",
        "price": 299,
        "currency": "CNY",
        "period": "年",
        "description": "更新的描述",
        "features": [
            "更新的功能1",
            "更新的功能2"
        ],
        "is_popular": true,
        "is_active": true,
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T13:00:00"
    },
    "message": "定价方案更新成功"
}
```

### 删除定价方案

**DELETE** `/api/pricing/plans/{plan_id}`

**响应**：
```json
{
    "success": true,
    "message": "定价方案删除成功"
}
```

### 比较定价方案

**GET** `/api/pricing/compare`

**查询参数**：
- `plans`: 方案ID列表，用逗号分隔（例如：1,2,3）

**响应**：
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "基础版",
            "price": 0,
            "currency": "CNY",
            "period": "月",
            "description": "适合个人用户和小型项目",
            "features": [
                "每月1000次对话",
                "基础代码生成",
                "社区支持",
                "基础模型访问"
            ],
            "is_popular": false,
            "is_active": true
        },
        {
            "id": 2,
            "name": "专业版",
            "price": 99,
            "currency": "CNY",
            "period": "月",
            "description": "适合专业开发者和小团队",
            "features": [
                "每月10000次对话",
                "高级代码生成",
                "优先技术支持",
                "高级模型访问",
                "代码审查功能",
                "团队协作工具"
            ],
            "is_popular": true,
            "is_active": true
        },
        {
            "id": 3,
            "name": "企业版",
            "price": 299,
            "currency": "CNY",
            "period": "月",
            "description": "适合大型企业和团队",
            "features": [
                "无限对话次数",
                "企业级代码生成",
                "专属技术支持",
                "定制模型访问",
                "高级代码审查",
                "完整团队协作",
                "私有部署选项",
                "API访问权限",
                "定制化服务"
            ],
            "is_popular": false,
            "is_active": true
        }
    ],
    "message": "定价方案比较成功"
}
```

## 聊天功能 API

### 创建聊天会话

**POST** `/api/chat/session`

**请求体**：
```json
{
    "user_ip": "192.168.1.1"
}
```

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "session_id": "abc123def456",
        "user_ip": "192.168.1.1",
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00",
        "message_count": 0
    },
    "message": "聊天会话创建成功"
}
```

### 获取聊天会话

**GET** `/api/chat/session/{session_id}`

**响应**：
```json
{
    "success": true,
    "data": {
        "id": 1,
        "session_id": "abc123def456",
        "user_ip": "192.168.1.1",
        "created_at": "2023-01-01T12:00:00",
        "updated_at": "2023-01-01T12:00:00",
        "message_count": 2
    },
    "message": "获取聊天会话成功"
}
```

### 发送消息

**POST** `/api/chat/message`

**请求体**：
```json
{
    "session_id": "abc123def456",
    "message": "你好，我想了解QubitCode的功能"
}
```

**响应**：
```json
{
    "success": true,
    "data": {
        "user_message": {
            "id": 1,
            "chat_id": 1,
            "content": "你好，我想了解QubitCode的功能",
            "is_user": true,
            "created_at": "2023-01-01T12:00:00"
        },
        "ai_response": {
            "id": 2,
            "chat_id": 1,
            "content": "您好！QubitCode是一款新一代智能对话系统，主要功能包括：\n\n1. 智能代码生成\n2. 代码审查与优化\n3. 技术问题解答\n4. 编程知识学习\n\n您想了解哪个方面的功能呢？",
            "is_user": false,
            "created_at": "2023-01-01T12:00:01"
        }
    },
    "message": "消息发送成功"
}
```

### 获取聊天历史记录

**GET** `/api/chat/history/{session_id}`

**查询参数**：
- `page`: 页码（默认：1）
- `per_page`: 每页数量（默认：20）

**响应**：
```json
{
    "success": true,
    "data": {
        "messages": [
            {
                "id": 1,
                "chat_id": 1,
                "content": "你好，我想了解QubitCode的功能",
                "is_user": true,
                "created_at": "2023-01-01T12:00:00"
            },
            {
                "id": 2,
                "chat_id": 1,
                "content": "您好！QubitCode是一款新一代智能对话系统，主要功能包括：\n\n1. 智能代码生成\n2. 代码审查与优化\n3. 技术问题解答\n4. 编程知识学习\n\n您想了解哪个方面的功能呢？",
                "is_user": false,
                "created_at": "2023-01-01T12:00:01"
            }
        ],
        "total": 2,
        "pages": 1,
        "current_page": 1
    },
    "message": "获取聊天历史记录成功"
}
```

### 获取会话列表

**GET** `/api/chat/sessions`

**查询参数**：
- `page`: 页码（默认：1）
- `per_page`: 每页数量（默认：10）

**响应**：
```json
{
    "success": true,
    "data": {
        "sessions": [
            {
                "id": 1,
                "session_id": "abc123def456",
                "user_ip": "192.168.1.1",
                "created_at": "2023-01-01T12:00:00",
                "updated_at": "2023-01-01T12:00:00",
                "message_count": 2
            }
        ],
        "total": 1,
        "pages": 1,
        "current_page": 1
    },
    "message": "获取会话列表成功"
}
```

### 删除会话

**DELETE** `/api/chat/session/{session_id}`

**响应**：
```json
{
    "success": true,
    "message": "会话删除成功"
}
```

## 错误代码

| 错误代码 | 描述 |
|---------|------|
| 400 | 请求参数错误 |
| 404 | 资源不存在 |
| 405 | 请求方法不允许 |
| 500 | 服务器内部错误 |

## 限制说明

- 聊天功能限制：每个会话最多100条消息
- 联系表单：每个IP每天最多提交5次
- API请求频率：每分钟最多100次请求

## 示例代码

### JavaScript (使用fetch)

```javascript
// 提交联系表单
fetch('/api/contact/submit', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        name: '张三',
        email: 'zhangsan@example.com',
        subject: '咨询产品',
        message: '我想了解更多关于QubitCode的信息'
    })
})
.then(response => response.json())
.then(data => console.log(data));

// 发送聊天消息
fetch('/api/chat/message', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        session_id: 'abc123def456',
        message: '你好，我想了解QubitCode的功能'
    })
})
.then(response => response.json())
.then(data => console.log(data));
```

### Python (使用requests)

```python
import requests

# 提交联系表单
response = requests.post(
    'http://localhost:5000/api/contact/submit',
    json={
        'name': '张三',
        'email': 'zhangsan@example.com',
        'subject': '咨询产品',
        'message': '我想了解更多关于QubitCode的信息'
    }
)
print(response.json())

# 发送聊天消息
response = requests.post(
    'http://localhost:5000/api/chat/message',
    json={
        'session_id': 'abc123def456',
        'message': '你好，我想了解QubitCode的功能'
    }
)
print(response.json())
```