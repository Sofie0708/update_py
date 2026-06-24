"""
ATIVIDADE AULA 11 — Models por cenário (1,0 ponto)

Aluno: Sofie Cirino e Castro
Cenário escolhido (A, B ou C): B
  A = Locadora de veículos
  B = Cinema
  C = Troca de figurinhas Copa do Mundo

Renomeie este arquivo para: models_cenario_SEU_CENARIO.py
"""

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ModeloBase(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    data_criacao = db.Column(
        db.DateTime, default=datetime.now, nullable=False
    )
    data_atualizacao = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )


# =============================================================================
# TODO ALUNO: crie pelo menos 3 tabelas abaixo, todas herdando ModeloBase
# Use db.ForeignKey("nome_tabela.id") para ligar as tabelas
# Use db.relationship() para navegar entre elas
# =============================================================================


class Filme(ModeloBase):
    __tablename__ = "filmes"

    titulo = db.Column(db.String(150), nullable=False)
    duracao_min = db.Column(db.Integer, nullable=False) 
    classificacao = db.Column(db.String(5), nullable=False)

    sessoes = db.relationship("Sessao", back_populates="filme")


class Sessao(ModeloBase):
    __tablename__ = "sessoes"

    filme_id = db.Column(db.Integer, db.ForeignKey("filmes.id"), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey("salas.id"), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    filme = db.relationship("Filme", back_populates="sessoes")
    sala = db.relationship("Sala", back_populates="sessoes")
    ingressos = db.relationship("Ingresso", back_populates="sessao")


class Sala(ModeloBase):
    __tablename__ = "salas"

    numero = db.Column(db.Integer, nullable=False, unique=True)
    capacidade = db.Column(db.Integer, nullable=False)

    sessoes = db.relationship("Sessao", back_populates="sala")


class Ingresso(ModeloBase):
    __tablename__ = "ingressos"

    sessao_id = db.Column(db.Integer, db.ForeignKey("sessoes.id"), nullable=False)
    assento = db.Column(db.String(10), nullable=False)
    nome_comprador = db.Column(db.String(120), nullable=False)

    sessao = db.relationship("Sessao", back_populates="ingressos")
