from flask import Blueprint, request, jsonify
from app.models.pricing import Pricing
from app import db
import json

pricing_bp = Blueprint('pricing', __name__)

@pricing_bp.route('/plans', methods=['GET'])
def get_pricing_plans():
    """获取所有定价方案"""
    try:
        plans = Pricing.query.filter_by(is_active=True).order_by(Pricing.price).all()
        
        return jsonify({
            'plans': [plan.to_dict() for plan in plans]
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'获取失败: {str(e)}'}), 500

@pricing_bp.route('/plans', methods=['POST'])
def create_pricing_plan():
    """创建定价方案（管理员功能）"""
    try:
        data = request.get_json()
        
        # 验证必填字段
        if not data or not all(k in data for k in ('name', 'price', 'period', 'features')):
            return jsonify({'error': '缺少必填字段'}), 400
        
        # 创建定价方案
        plan = Pricing(
            name=data['name'],
            price=float(data['price']),
            currency=data.get('currency', 'CNY'),
            period=data['period'],
            description=data.get('description', ''),
            features=json.dumps(data['features']) if isinstance(data['features'], list) else data['features'],
            is_popular=data.get('is_popular', False)
        )
        
        db.session.add(plan)
        db.session.commit()
        
        return jsonify({
            'message': '定价方案创建成功',
            'plan': plan.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'创建失败: {str(e)}'}), 500

@pricing_bp.route('/plans/<int:plan_id>', methods=['GET'])
def get_pricing_plan(plan_id):
    """获取单个定价方案"""
    try:
        plan = Pricing.query.get_or_404(plan_id)
        return jsonify(plan.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': f'获取失败: {str(e)}'}), 500

@pricing_bp.route('/plans/<int:plan_id>', methods=['PUT'])
def update_pricing_plan(plan_id):
    """更新定价方案（管理员功能）"""
    try:
        plan = Pricing.query.get_or_404(plan_id)
        data = request.get_json()
        
        # 更新字段
        if 'name' in data:
            plan.name = data['name']
        if 'price' in data:
            plan.price = float(data['price'])
        if 'currency' in data:
            plan.currency = data['currency']
        if 'period' in data:
            plan.period = data['period']
        if 'description' in data:
            plan.description = data['description']
        if 'features' in data:
            plan.features = json.dumps(data['features']) if isinstance(data['features'], list) else data['features']
        if 'is_popular' in data:
            plan.is_popular = data['is_popular']
        if 'is_active' in data:
            plan.is_active = data['is_active']
        
        db.session.commit()
        
        return jsonify({
            'message': '定价方案更新成功',
            'plan': plan.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'更新失败: {str(e)}'}), 500

@pricing_bp.route('/plans/<int:plan_id>', methods=['DELETE'])
def delete_pricing_plan(plan_id):
    """删除定价方案（管理员功能）"""
    try:
        plan = Pricing.query.get_or_404(plan_id)
        db.session.delete(plan)
        db.session.commit()
        
        return jsonify({'message': '定价方案已删除'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'删除失败: {str(e)}'}), 500

@pricing_bp.route('/compare', methods=['GET'])
def compare_plans():
    """比较定价方案"""
    try:
        # 获取所有激活的定价方案
        plans = Pricing.query.filter_by(is_active=True).order_by(Pricing.price).all()
        
        # 提取所有功能特性
        all_features = set()
        for plan in plans:
            features = json.loads(plan.features) if isinstance(plan.features, str) else plan.features
            all_features.update(features)
        
        # 构建比较表格
        comparison = {
            'plans': [plan.to_dict() for plan in plans],
            'features': sorted(list(all_features)),
            'comparison_table': []
        }
        
        # 为每个功能创建比较行
        for feature in comparison['features']:
            row = {'feature': feature}
            for plan in plans:
                features = json.loads(plan.features) if isinstance(plan.features, str) else plan.features
                row[plan.name] = feature in features
            comparison['comparison_table'].append(row)
        
        return jsonify(comparison), 200
        
    except Exception as e:
        return jsonify({'error': f'比较失败: {str(e)}'}), 500