import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """基础配置类"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost/qubitcode'
    
    # API配置
    API_VERSION = os.environ.get('API_VERSION') or 'v1'
    API_PREFIX = os.environ.get('API_PREFIX') or '/api'
    
    # 跨域配置
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS') or '*'
    
    # 日志配置
    LOG_LEVEL = os.environ.get('LOG_LEVEL') or 'INFO'
    LOG_FILE = os.environ.get('LOG_FILE') or 'logs/app.log'
    
    # 聊天配置
    MAX_MESSAGE_LENGTH = int(os.environ.get('MAX_MESSAGE_LENGTH', 10000))
    MAX_SESSIONS_PER_IP = int(os.environ.get('MAX_SESSIONS_PER_IP', 10))

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False

class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}