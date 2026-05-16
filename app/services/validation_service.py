import re
from dataclasses import dataclass, field

EMAIL_REGEX = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
TIPOS_USUARIO_VALIDOS = {'morador', 'sindico'}
STATUS_OCORRENCIA_VALIDOS = {'Pendente', 'Em Andamento', 'Resolvido'}


@dataclass
class ValidationResult:
    valido: bool
    dados: dict[str, str] = field(default_factory=dict)
    erros: list[str] = field(default_factory=list)


def _normalizar(valor: str | None) -> str:
    return (valor or '').strip()


def validar_usuario_form(form) -> ValidationResult:
    dados = {
        'nome': _normalizar(form.get('nome')),
        'email': _normalizar(form.get('email')).lower(),
        'senha': form.get('senha') or '',
        'unidade': _normalizar(form.get('unidade')),
        'tipo': _normalizar(form.get('tipo')) or 'morador',
    }

    erros = []
    if len(dados['nome']) < 3:
        erros.append('Informe um nome com pelo menos 3 caracteres.')
    if not EMAIL_REGEX.match(dados['email']):
        erros.append('Informe um e-mail válido.')
    if len(dados['senha']) < 6:
        erros.append('Informe uma senha com pelo menos 6 caracteres.')
    if not dados['unidade']:
        erros.append('Informe a unidade do morador.')
    if dados['tipo'] not in TIPOS_USUARIO_VALIDOS:
        erros.append('Tipo de usuário inválido.')

    return ValidationResult(valido=not erros, dados=dados, erros=erros)


def validar_ocorrencia_form(form) -> ValidationResult:
    dados = {
        'titulo': _normalizar(form.get('titulo')),
        'descricao': _normalizar(form.get('descricao')),
    }

    erros = []
    if len(dados['titulo']) < 3:
        erros.append('Informe um título com pelo menos 3 caracteres.')
    if len(dados['titulo']) > 100:
        erros.append('O título deve ter no máximo 100 caracteres.')
    if len(dados['descricao']) < 10:
        erros.append('Descreva a ocorrência com pelo menos 10 caracteres.')

    return ValidationResult(valido=not erros, dados=dados, erros=erros)
