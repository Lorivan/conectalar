# Sprint 4 — Execução realizada

**Objetivo:** registrar o que foi efetivamente executado na Sprint 4 para transformar o plano em entrega técnica verificável.

## 1. Entregas implementadas

| Item | Status | Evidência técnica |
| --- | --- | --- |
| Validações server-side de usuário | Concluído | `app/services/validation_service.py` e `app/usuarios/routes.py` |
| Validações server-side de ocorrência | Concluído | `app/services/validation_service.py` e `app/ocorrencias/routes.py` |
| Tratamento seguro de erros | Concluído | Uso de `current_app.logger.exception(...)` e mensagens amigáveis |
| Testes automatizados mínimos | Concluído | Pasta `tests/` com 10 testes automatizados |
| Dependência de testes | Concluído | `pytest` incluído em `requirements-dev.txt`, sem alterar o `requirements.txt` legado |
| Evidência de execução | Concluído | `pytest -q` com 10 testes passando |

## 2. Validações entregues

### Usuário

- Nome obrigatório com pelo menos 3 caracteres.
- E-mail obrigatório em formato válido.
- Senha obrigatória com pelo menos 6 caracteres.
- Unidade obrigatória.
- Tipo restrito a `morador` ou `sindico`.
- E-mail duplicado bloqueado antes da persistência.

### Ocorrência

- Título obrigatório com pelo menos 3 caracteres.
- Título limitado a 100 caracteres.
- Descrição obrigatória com pelo menos 10 caracteres.
- Status restrito aos valores válidos do domínio.

## 3. Testes automatizados entregues

| Arquivo | Cobertura |
| --- | --- |
| `tests/test_app.py` | Healthcheck e consulta básica no banco de teste |
| `tests/test_auth.py` | Login válido, login inválido e proteção de rota sem sessão |
| `tests/test_usuarios.py` | Cadastro válido persistido e cadastro inválido bloqueado |
| `tests/test_ocorrencias.py` | Ocorrência válida persistida, ocorrência inválida bloqueada e autorização por perfil |

## 4. Resultado dos testes

```text
10 passed, 1 warning
```

A única advertência vem do uso atual de `datetime.utcnow()` no modelo, já registrado como melhoria futura para padronização de timezone.

## 5. Critérios de pronto atendidos

- [x] Validações server-side implementadas para usuário e ocorrência.
- [x] Tratamento de erro sem vazamento de exceção técnica para usuário.
- [x] Testes automatizados mínimos criados e passando.
- [x] Dependência `pytest` adicionada ao projeto em `requirements-dev.txt`.
- [x] Persistência validada por testes de criação de usuário e ocorrência.
- [x] Autorização de perfil validada em teste automatizado.

## 6. Pendências recomendadas para próxima evolução

- Coletar prints reais da aplicação em execução para anexar à entrega acadêmica.
- Executar consultas SQL no PostgreSQL usado na demonstração e salvar os prints em `docs/evidencias/sprint-04/`.
- Corrigir a advertência de timezone migrando de `datetime.utcnow()` para datas timezone-aware.
- Avaliar Flask-Migrate/Alembic para migrações versionadas de banco.
- Adicionar paginação/busca no dashboard se o volume de ocorrências crescer.
