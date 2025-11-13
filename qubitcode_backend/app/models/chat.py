from app import db
from datetime import datetime

class Chat(db.Model):
    """聊天会话模型"""
    __tablename__ = 'chats'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(100), unique=True, nullable=False)  # 会话ID
    user_ip = db.Column(db.String(45), nullable=True)  # 用户IP
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 关联消息
    messages = db.relationship('ChatMessage', backref='chat', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Chat {self.session_id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'user_ip': self.user_ip,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'message_count': len(self.messages)
        }

class ChatMessage(db.Model):
    """聊天消息模型"""
    __tablename__ = 'chat_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_user = db.Column(db.Boolean, nullable=False)  # True为用户消息，False为AI回复
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ChatMessage {self.id}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'chat_id': self.chat_id,
            'content': self.content,
            'is_user': self.is_user,
            'created_at': self.created_at.isoformat()
        }