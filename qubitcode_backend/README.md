# QubitCode 后端 API 服务

基于 Flask 和 MySQL 的 QubitCode 智能对话系统后端 API 服务。

## 功能特性

- ✅ 联系表单处理 API
- ✅ 定价方案管理 API
- ✅ 聊天功能 API
- ✅ 配置文件和环境变量管理
- ✅ 完整的 API 文档
- ✅ 详细的部署说明

## 技术栈

- **后端框架**: Flask
- **数据库**: MySQL
- **ORM**: SQLAlchemy
- **数据库迁移**: Flask-Migrate
- **API文档**: 自定义 Markdown 文档
- **环境配置**: python-dotenv

## 项目结构

```
qubitcode_backend/
├── app/                     # 应用主目录
│   ├── __init__.py         # 应用工厂函数
│   ├── models/             # 数据模型
│   │   ├── __init__.py
│   │   ├── contact.py      # 联系表单模型
│   │   ├── pricing.py      # 定价方案模型
│   │   └── chat.py         # 聊天功能模型
│   ├── routes/             # API 路由
│   │   ├── __init__.py
│   │   ├── contact.py      # 联系表单 API
│   │   ├── pricing.py      # 定价方案 API
│   │   └── chat.py         # 聊天功能 API
│   └── utils/              # 工具函数
│       └── __init__.py
├── config/                 # 配置文件
│   └── config.py           # 应用配置
├── migrations/             # 数据库迁移文件
├── logs/                   # 日志文件目录
├── app.py                  # 应用入口文件
├── init_db.py              # 数据库初始化脚本
├── setup_migrations.py     # 数据库迁移设置脚本
├── requirements.txt        # Python 依赖
├── .env                    # 环境变量配置
├── .env.example            # 环境变量示例
├── start.bat               # Windows 启动脚本
├── API文档.md              # API 文档
├── 部署说明.md              # 部署说明
└── README.md               # 项目说明
```

## 快速开始

### 1. 环境要求

- Python 3.8+
- MySQL 5.7+ / 8.0+

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env` 并配置数据库连接信息：

```bash
cp .env.example .env
```

编辑 `.env` 文件，设置以下变量：

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/qubitcode
```

### 4. 初始化数据库

```bash
python init_db.py
```

### 5. 启动应用

```bash
python app.py
```

或者使用 Windows 启动脚本：

```bash
start.bat
```

应用将在 `http://localhost:5000` 启动。

## API 文档

详细的 API 文档请参考 [API文档.md](API文档.md)

## 主要 API 端点

### 联系表单 API

- `POST /api/v1/contact/submit` - 提交联系表单
- `GET /api/v1/contact/list` - 获取联系表单列表
- `GET /api/v1/contact/{contact_id}` - 获取联系表单详情
- `PUT /api/v1/contact/{contact_id}/process` - 标记为已处理
- `DELETE /api/v1/contact/{contact_id}` - 删除联系表单

### 定价方案 API

- `GET /api/v1/pricing/plans` - 获取所有定价方案
- `POST /api/v1/pricing/plans` - 创建定价方案
- `GET /api/v1/pricing/plans/{plan_id}` - 获取单个定价方案
- `PUT /api/v1/pricing/plans/{plan_id}` - 更新定价方案
- `DELETE /api/v1/pricing/plans/{plan_id}` - 删除定价方案
- `GET /api/v1/pricing/compare` - 比较定价方案

### 聊天功能 API

- `POST /api/v1/chat/session` - 创建聊天会话
- `GET /api/v1/chat/session/{session_id}` - 获取聊天会话
- `POST /api/v1/chat/message` - 发送消息
- `GET /api/v1/chat/history/{session_id}` - 获取聊天历史记录
- `GET /api/v1/chat/sessions` - 获取会话列表
- `DELETE /api/v1/chat/session/{session_id}` - 删除会话

## 部署

详细的部署说明请参考 [部署说明.md](部署说明.md)

## 开发指南

### 数据库迁移

如果需要修改数据库结构，可以使用 Flask-Migrate 进行迁移：

```bash
# 生成迁移文件
flask db migrate -m "描述信息"

# 应用迁移
flask db upgrade
```

### 添加新的 API 端点

1. 在 `app/models/` 中定义数据模型
2. 在 `app/routes/` 中创建路由文件
3. 在 `app/__init__.py` 中注册蓝图

### 环境配置

项目支持多环境配置：

- `development` - 开发环境
- `production` - 生产环境
- `testing` - 测试环境

通过设置 `FLASK_ENV` 环境变量切换配置。

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request。

## 联系方式

- 邮箱：support@qubitcode.com
- 官网：https://qubitcode.com