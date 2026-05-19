# Sprint 4 — Execução realizada

## Entregas implementadas

### P0
- Validação de ocorrência: título mínimo de 3 caracteres e descrição mínima de 10 caracteres; bloqueio de persistência quando inválido.
- Validação de cadastro de usuário: nome, e-mail, senha, unidade e tipo válidos; bloqueio de persistência quando inválido.

### P1
- Tratamento de erros: remoção de `print`, uso de `logger.exception` e mensagens seguras ao usuário.
- Testes automatizados com cobertura de app factory, login, autorização, cadastro e ocorrência.
- Dashboard com busca textual (`q`) e paginação (`pagina`, 10 itens por página).

### P2
- Base para migrações criada com Flask-Migrate/Alembic e instruções de uso em `migrations/README.md`.
- Padronização de timezone: persistência em UTC no banco e formatação para BRT na camada de exibição.

## Evidências de aceite
- `pytest` executa localmente com sucesso.
- Cadastros/ocorrências inválidos retornam HTTP 400 e não persistem.
- Dashboard mantém usabilidade com maior volume via busca e paginação.
