from datetime import datetime, timedelta

from app import db


# Função que pega a hora global e diminui 3 horas (Fuso de Brasília)
def hora_brasilia():
    return datetime.utcnow() - timedelta(hours=3)


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    unidade = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(20), default='morador')
    ocorrencias = db.relationship('Ocorrencia', backref='autor', lazy=True)


class Ocorrencia(db.Model):
    __tablename__ = 'ocorrencias'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=hora_brasilia)
    status = db.Column(db.String(20), default='Pendente')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
