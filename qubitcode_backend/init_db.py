"""
数据库初始化脚本
用于创建数据库表和初始数据
"""

from app import create_app, db
from app.models.contact import Contact
from app.models.pricing import Pricing
from app.models.chat import Chat, ChatMessage
import json

def init_database():
    """初始化数据库"""
    app = create_app()
    
    with app.app_context():
        # 创建所有表
        db.create_all()
        print("数据库表创建成功!")
        
        # 添加初始定价方案
        if Pricing.query.count() == 0:
            # 基础版
            basic_plan = Pricing(
                name="基础版",
                price=0,
                currency="CNY",
                period="月",
                description="适合个人用户和小型项目",
                features=json.dumps([
                    "每月1000次对话",
                    "基础代码生成",
                    "社区支持",
                    "基础模型访问"
                ]),
                is_popular=False
            )
            
            # 专业版
            pro_plan = Pricing(
                name="专业版",
                price=99,
                currency="CNY",
                period="月",
                description="适合专业开发者和小团队",
                features=json.dumps([
                    "每月10000次对话",
                    "高级代码生成",
                    "优先技术支持",
                    "高级模型访问",
                    "代码审查功能",
                    "团队协作工具"
                ]),
                is_popular=True
            )
            
            # 企业版
            enterprise_plan = Pricing(
                name="企业版",
                price=299,
                currency="CNY",
                period="月",
                description="适合大型企业和团队",
                features=json.dumps([
                    "无限对话次数",
                    "企业级代码生成",
                    "专属技术支持",
                    "定制模型访问",
                    "高级代码审查",
                    "完整团队协作",
                    "私有部署选项",
                    "API访问权限",
                    "定制化服务"
                ]),
                is_popular=False
            )
            
            db.session.add(basic_plan)
            db.session.add(pro_plan)
            db.session.add(enterprise_plan)
            db.session.commit()
            print("初始定价方案添加成功!")
        
        print("数据库初始化完成!")

if __name__ == '__main__':
    init_database()