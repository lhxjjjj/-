from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config.config import config

# 初始化扩展
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    """应用工厂函数"""
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(config[config_name])
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # 注册蓝图
    from app.routes.contact import contact_bp
    from app.routes.pricing import pricing_bp
    from app.routes.chat import chat_bp
    
    app.register_blueprint(contact_bp, url_prefix=f"{app.config['API_PREFIX']}/contact")
    app.register_blueprint(pricing_bp, url_prefix=f"{app.config['API_PREFIX']}/pricing")
    app.register_blueprint(chat_bp, url_prefix=f"{app.config['API_PREFIX']}/chat")
    
    # 根路由
    @app.route('/')
    def index():
        return {"message": "QubitCode API Server", "version": app.config['API_VERSION']}
    
    # 健康检查
    @app.route('/health')
    def health_check():
        from datetime import datetime
        return {"status": "healthy", "timestamp": datetime.now().isoformat()}
    
    return app