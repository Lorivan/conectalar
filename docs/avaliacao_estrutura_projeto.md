# Avaliação da estrutura do projeto ConectaLar

## Visão geral da estrutura atual

O projeto está organizado de forma simples e funcional para um MVP Flask:

- `app/__init__.py`: inicialização da aplicação e banco.
- `app/routes.py`: rotas HTTP e regras de acesso.
- `app/models.py`: modelos SQLAlchemy.
- `app/templates/`: páginas HTML.
- `config.py`: configurações por variáveis de ambiente.
- `run.py`: ponto de entrada da aplicação.

Essa estrutura é válida para começo de projeto, mas há sinais de crescimento que justificam modularização.

## Pontos positivos

1. **Separação básica por responsabilidade** (rotas, modelos, templates).
2. **Uso de variáveis de ambiente** para dados sensíveis.
3. **Controle de acesso por perfil** (`sindico` x `morador`).
4. **Persistência relacional com SQLAlchemy**.

## Principais pontos de melhoria recomendados

### 1) Modularização por blueprints
Concentrar todas as rotas em um único arquivo (`app/routes.py`) dificulta evolução e testes.

**Sugestão:** dividir em blueprints:
- `app/auth/routes.py` (login/logout)
- `app/ocorrencias/routes.py`
- `app/usuarios/routes.py`
- `app/dashboard/routes.py`

### 2) Camada de serviços
Hoje as regras de negócio estão nas rotas (ex.: autenticação, atualização de status, cadastro).

**Sugestão:** criar `app/services/` para regras de domínio e manter rotas finas.

### 3) Camada de formulários e validação
A coleta dos dados via `request.form.get(...)` sem validação estruturada tende a gerar inconsistências.

**Sugestão:** usar Flask-WTF/Pydantic para validação de campos, tipos, tamanho e obrigatoriedade.

### 4) Migrações de banco
`db.create_all()` é útil em MVP, porém frágil para evolução controlada.

**Sugestão:** adotar Flask-Migrate/Alembic para versionamento de schema.

### 5) Estrutura de testes
Não há suíte de testes no repositório.

**Sugestão:** criar `tests/` com:
- testes unitários de serviços
- testes de integração de rotas críticas (login, autorização, criação de ocorrência)

### 6) Segurança e observabilidade
Recomendável reforçar:
- proteção CSRF em formulários
- limites e validação de entradas
- logging estruturado (trocar prints por logger)
- tratamento de erro com páginas/handlers dedicados

## Roadmap sugerido (incremental)

### Fase 1 (rápida)
- Introduzir blueprints sem alterar regras de negócio.
- Criar testes de fumaça (`/`, `/dashboard`, `/nova-ocorrencia`).
- Configurar logger básico.

### Fase 2 (estabilidade)
- Extrair serviços de autenticação, usuário e ocorrência.
- Adicionar Flask-Migrate.
- Adicionar validações de formulário.

### Fase 3 (escala)
- Implementar API REST (se necessário para app mobile/painel externo).
- Paginação, busca e filtros avançados.
- Observabilidade (logs + métricas de erro).

## Resultado esperado

Com essas melhorias, o projeto evolui de MVP acadêmico para uma base mais sustentável para manutenção contínua, com mais segurança, testabilidade e facilidade para novas funcionalidades.
