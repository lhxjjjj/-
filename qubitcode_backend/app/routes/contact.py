from flask import Blueprint, request, jsonify
from app.models.contact import Contact
from app import db
from datetime import datetime
import uuid

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/submit', methods=['POST'])
def submit_contact():
    """提交联系表单"""
    try:
        data = request.get_json()
        
        # 验证必填字段
        if not data or not all(k in data for k in ('name', 'email', 'subject', 'message')):
            return jsonify({'error': '缺少必填字段'}), 400
        
        # 创建联系记录
        contact = Contact(
            name=data['name'],
            email=data['email'],
            company=data.get('company', ''),
            phone=data.get('phone', ''),
            subject=data['subject'],
            message=data['message']
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return jsonify({
            'message': '联系表单提交成功',
            'contact_id': contact.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'提交失败: {str(e)}'}), 500

@contact_bp.route('/list', methods=['GET'])
def get_contacts():
    """获取联系表单列表"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        is_processed = request.args.get('is_processed', None, type=bool)
        
        # 构建查询
        query = Contact.query
        
        if is_processed is not None:
            query = query.filter(Contact.is_processed == is_processed)
        
        # 分页
        contacts = query.order_by(Contact.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'contacts': [contact.to_dict() for contact in contacts.items],
            'total': contacts.total,
            'pages': contacts.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'获取失败: {str(e)}'}), 500

@contact_bp.route('/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    """获取单个联系表单详情"""
    try:
        contact = Contact.query.get_or_404(contact_id)
        return jsonify(contact.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': f'获取失败: {str(e)}'}), 500

@contact_bp.route('/<int:contact_id>/mark-processed', methods=['PUT'])
def mark_processed(contact_id):
    """标记联系表单为已处理"""
    try:
        contact = Contact.query.get_or_404(contact_id)
        contact.is_processed = True
        db.session.commit()
        
        return jsonify({
            'message': '已标记为处理完成',
            'contact': contact.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'更新失败: {str(e)}'}), 500

@contact_bp.route('/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """删除联系表单"""
    try:
        contact = Contact.query.get_or_404(contact_id)
        db.session.delete(contact)
        db.session.commit()
        
        return jsonify({'message': '联系表单已删除'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'删除失败: {str(e)}'}), 500