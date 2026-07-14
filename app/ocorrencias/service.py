from sqlalchemy.exc import SQLAlchemyError

from app.models import Ocorrencia
from app.ocorrencias.repository import OcorrenciaRepository
from app.services.validation_service import STATUS_OCORRENCIA_VALIDOS


class OcorrenciaPersistenceError(RuntimeError):
    """Erro de persistência do domínio de ocorrências."""


class OcorrenciaService:
    """Regras de negócio do domínio de ocorrências."""

    def __init__(self, repository: OcorrenciaRepository | None = None):
        self.repository = repository or OcorrenciaRepository()

    def registrar_ocorrencia(
        self,
        *,
        titulo: str,
        descricao: str,
        usuario_id: int,
    ) -> Ocorrencia:
        try:
            ocorrencia = self.repository.criar(
                titulo=titulo,
                descricao=descricao,
                usuario_id=usuario_id,
            )
            self.repository.salvar()
            return ocorrencia
        except SQLAlchemyError as exc:
            self.repository.desfazer()
            raise OcorrenciaPersistenceError('Falha ao registrar ocorrência.') from exc

    def atualizar_status(self, *, ocorrencia_id: int, novo_status: str) -> bool:
        if novo_status not in STATUS_OCORRENCIA_VALIDOS:
            return False

        ocorrencia = self.repository.buscar_por_id(ocorrencia_id)
        if not ocorrencia:
            return False

        try:
            ocorrencia.status = novo_status
            self.repository.salvar()
            return True
        except SQLAlchemyError as exc:
            self.repository.desfazer()
            raise OcorrenciaPersistenceError('Falha ao atualizar status da ocorrência.') from exc
