from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    ultima_interacao = db.Column(db.String(100))
    pendencias = db.relationship('Pendencia', backref='cliente', lazy=True)
    incidentes = db.relationship('Incidente', backref='cliente', lazy=True)

class Pendencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    valor_pendente = db.Column(db.Float, nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Incidente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    tipo_incidente = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)