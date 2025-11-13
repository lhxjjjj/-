from app import db
from datetime import datetime

class Pricing(db.Model):
    """定价方案模型"""
    __tablename__ = 'pricing_plans'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # 方案名称
    price = db.Column(db.Float, nullable=False)  # 价格
    currency = db.Column(db.String(10), default='CNY')  # 货币
    period = db.Column(db.String(20), nullable=False)  # 周期：月/年
    description = db.Column(db.Text, nullable=True)  # 描述
    features = db.Column(db.Text, nullable=False)  # 功能列表，JSON格式存储
    is_popular = db.Column(db.Boolean, default=False)  # 是否热门
    is_active = db.Column(db.Boolean, default=True)  # 是否启用
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Pricing {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'currency': self.currency,
            'period': self.period,
            'description': self.description,
            'features': self.features,
            'is_popular': self.is_popular,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }