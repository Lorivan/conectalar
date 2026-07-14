from app import db
from app.models import Ocorrencia


class OcorrenciaRepository:
    """Camada de acesso a dados para o domínio de ocorrências."""

    def buscar_por_id(self, ocorrencia_id: int) -> Ocorrencia | None:
        return db.session.get(Ocorrencia, ocorrencia_id)

    def criar(self, *, titulo: str, descricao: str, usuario_id: int) -> Ocorrencia:
        ocorrencia = Ocorrencia(
            titulo=titulo,
            descricao=descricao,
            usuario_id=usuario_id,
        )
        db.session.add(ocorrencia)
        return ocorrencia

    def salvar(self) -> None:
        db.session.commit()

    def desfazer(self) -> None:
        db.session.rollback()
