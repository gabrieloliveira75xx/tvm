from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    __table_args__ = {'schema': 'chatbot_schema'}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    ultima_interacao = db.Column(db.String(100))

class Pendencia(db.Model):
    __tablename__ = 'pendencia'
    __table_args__ = {'schema': 'chatbot_schema'}
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('chatbot_schema.cliente.id'), nullable=False)
    valor_pendente = db.Column(db.Float, nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Incidente(db.Model):
    __tablename__ = 'incidente'
    __table_args__ = {'schema': 'chatbot_schema'}
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('chatbot_schema.cliente.id'), nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    tipo_incidente = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)