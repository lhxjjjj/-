@echo off
echo QubitCode 后端服务启动脚本
echo ============================

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未找到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

REM 检查虚拟环境是否存在
if not exist "venv" (
    echo 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
echo 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
echo 安装依赖包...
pip install -r requirements.txt

REM 检查环境变量文件
if not exist ".env" (
    echo 创建环境变量文件...
    copy .env.example .env
    echo 请编辑 .env 文件配置数据库连接信息
    pause
)

REM 初始化数据库
echo 初始化数据库...
python init_db.py

REM 启动应用
echo 启动应用...
python app.py

pause