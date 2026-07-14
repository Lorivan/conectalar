import pytest
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models import Ocorrencia
from app.ocorrencias.service import OcorrenciaPersistenceError, OcorrenciaService


class RepositoryComFalhaAoSalvar:
    def __init__(self):
        self.rollback_executado = False

    def criar(self, *, titulo, descricao, usuario_id):
        return Ocorrencia(titulo=titulo, descricao=descricao, usuario_id=usuario_id)

    def salvar(self):
        raise SQLAlchemyError('falha simulada')

    def desfazer(self):
        self.rollback_executado = True


def test_service_registra_ocorrencia(app, morador):
    service = OcorrenciaService()

    ocorrencia = service.registrar_ocorrencia(
        titulo='Interfone sem áudio',
        descricao='O interfone da unidade não está emitindo áudio corretamente.',
        usuario_id=morador.id,
    )

    assert ocorrencia.id is not None
    assert ocorrencia.status == 'Pendente'
    assert Ocorrencia.query.filter_by(titulo='Interfone sem áudio').count() == 1


def test_service_atualiza_status(app, morador):
    service = OcorrenciaService()
    ocorrencia = service.registrar_ocorrencia(
        titulo='Lâmpada queimada',
        descricao='A lâmpada do corredor do bloco principal está queimada.',
        usuario_id=morador.id,
    )

    status_atualizado = service.atualizar_status(
        ocorrencia_id=ocorrencia.id,
        novo_status='Resolvido',
    )

    assert status_atualizado is True
    assert db.session.get(Ocorrencia, ocorrencia.id).status == 'Resolvido'


def test_service_ignora_status_invalido(app, morador):
    service = OcorrenciaService()
    ocorrencia = service.registrar_ocorrencia(
        titulo='Porta desalinhada',
        descricao='A porta social está desalinhada e prendendo ao fechar.',
        usuario_id=morador.id,
    )

    status_atualizado = service.atualizar_status(
        ocorrencia_id=ocorrencia.id,
        novo_status='Cancelado',
    )

    assert status_atualizado is False
    assert db.session.get(Ocorrencia, ocorrencia.id).status == 'Pendente'


def test_service_desfaz_transacao_quando_persistencia_falha():
    repository = RepositoryComFalhaAoSalvar()
    service = OcorrenciaService(repository=repository)

    with pytest.raises(OcorrenciaPersistenceError):
        service.registrar_ocorrencia(
            titulo='Falha simulada',
            descricao='Descrição suficiente para acionar a persistência.',
            usuario_id=1,
        )

    assert repository.rollback_executado is True
