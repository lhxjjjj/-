"""
数据库迁移脚本
使用Flask-Migrate进行数据库版本控制
"""

from flask_migrate import init, migrate, upgrade
from app import create_app
import os

def setup_migrations():
    """设置数据库迁移"""
    app = create_app()
    
    with app.app_context():
        # 初始化迁移
        if not os.path.exists('migrations'):
            init()
            print("迁移目录初始化成功!")
        
        # 创建初始迁移
        migrate(message='Initial migration')
        print("初始迁移创建成功!")
        
        # 应用迁移
        upgrade()
        print("迁移应用成功!")

if __name__ == '__main__':
    setup_migrations()