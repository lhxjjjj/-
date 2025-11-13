from flask import Blueprint, request, jsonify
from app.models.chat import Chat, ChatMessage
from app import db
from datetime import datetime
import uuid
import random

chat_bp = Blueprint('chat', __name__)

# 预设的AI回复
AI_RESPONSES = [
    "QubitCode可以帮助您处理各种编程任务，包括代码生成、调试和优化。",
    "我理解您的问题。让我为您提供一些解决方案。",
    "这是一个很好的问题！根据我的分析，我建议您考虑以下几点。",
    "QubitCode使用先进的AI技术，可以理解自然语言并生成高质量的代码。",
    "感谢您的提问！我会尽力为您提供最有帮助的回答。",
    "基于您的需求，我推荐以下方法来解决这个问题。",
    "QubitCode支持多种编程语言，包括Python、JavaScript、Java等。",
    "我已经分析了您的问题，这里是一些可能的解决方案。"
]

@chat_bp.route('/session', methods=['POST'])
def create_chat_session():
    """创建新的聊天会话"""
    try:
        # 生成唯一的会话ID
        session_id = str(uuid.uuid4())
        
        # 获取用户信息
        user_ip = request.remote_addr
        user_agent = request.headers.get('User-Agent', '')
        
        # 创建聊天会话
        chat = Chat(
            session_id=session_id,
            user_ip=user_ip,
            user_agent=user_agent
        )
        
        db.session.add(chat)
        db.session.commit()
        
        return jsonify({
            'message': '聊天会话创建成功',
            'session_id': session_id,
            'chat': chat.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'创建会话失败: {str(e)}'}), 500

@chat_bp.route('/session/<session_id>', methods=['GET'])
def get_chat_session(session_id):
    """获取聊天会话及其消息"""
    try:
        chat = Chat.query.filter_by(session_id=session_id).first_or_404()
        return jsonify(chat.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': f'获取会话失败: {str(e)}'}), 500

@chat_bp.route('/message', methods=['POST'])
def send_message():
    """发送消息并获取AI回复"""
    try:
        data = request.get_json()
        
        # 验证必填字段
        if not data or not all(k in data for k in ('session_id', 'message')):
            return jsonify({'error': '缺少必填字段'}), 400
        
        session_id = data['session_id']
        message_content = data['message']
        
        # 获取或创建聊天会话
        chat = Chat.query.filter_by(session_id=session_id).first()
        if not chat:
            return jsonify({'error': '会话不存在'}), 404
        
        # 保存用户消息
        user_message = ChatMessage(
            chat_id=chat.id,
            content=message_content,
            is_user=True
        )
        
        db.session.add(user_message)
        
        # 生成AI回复（这里使用简单的随机回复，实际应用中可以集成真正的AI模型）
        ai_response = random.choice(AI_RESPONSES)
        
        # 保存AI回复
        ai_message = ChatMessage(
            chat_id=chat.id,
            content=ai_response,
            is_user=False
        )
        
        db.session.add(ai_message)
        
        # 更新会话时间
        chat.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'message': '消息发送成功',
            'user_message': user_message.to_dict(),
            'ai_response': ai_message.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'发送消息失败: {str(e)}'}), 500

@chat_bp.route('/history/<session_id>', methods=['GET'])
def get_chat_history(session_id):
    """获取聊天历史记录"""
    try:
        chat = Chat.query.filter_by(session_id=session_id).first_or_404()
        
        # 获取分页参数
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 50, type=int)
        
        # 分页获取消息
        messages = ChatMessage.query.filter_by(chat_id=chat.id)\
            .order_by(ChatMessage.created_at.asc())\
            .paginate(page=page, per_page=per_page, error_out=False)
        
        return jsonify({
            'session_id': session_id,
            'messages': [message.to_dict() for message in messages.items],
            'total': messages.total,
            'pages': messages.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'获取历史记录失败: {str(e)}'}), 500

@chat_bp.route('/sessions', methods=['GET'])
def get_chat_sessions():
    """获取所有聊天会话列表（管理员功能）"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 20, type=int)
        
        # 分页获取会话
        sessions = Chat.query.order_by(Chat.updated_at.desc())\
            .paginate(page=page, per_page=per_page, error_out=False)
        
        return jsonify({
            'sessions': [session.to_dict() for session in sessions.items],
            'total': sessions.total,
            'pages': sessions.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'获取会话列表失败: {str(e)}'}), 500

@chat_bp.route('/session/<session_id>', methods=['DELETE'])
def delete_chat_session(session_id):
    """删除聊天会话及其所有消息（管理员功能）"""
    try:
        chat = Chat.query.filter_by(session_id=session_id).first_or_404()
        db.session.delete(chat)
        db.session.commit()
        
        return jsonify({'message': '聊天会话已删除'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'删除会话失败: {str(e)}'}), 500