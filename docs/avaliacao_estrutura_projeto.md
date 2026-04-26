# Avaliação da estrutura atual do ConectaLar (branch atual)

## 1) Diagnóstico objetivo da estrutura

Com base no código desta branch, o projeto já evoluiu além do MVP inicial e hoje possui:

- **Factory de aplicação Flask** (`create_app`) com registro de blueprints por domínio (`auth`, `dashboard`, `ocorrencias`, `usuarios`).
- **Camadas iniciais separadas** para utilitários de autenticação (`app/utils/auth.py`) e serviços (`app/services/auth_service.py`).
- **Modelagem simples e direta** com SQLAlchemy para `Usuario` e `Ocorrencia`.
- **Frontend server-side** por templates Jinja2 (sem API REST pública).

### Estrutura atual (resumo)

```text
app/
  __init__.py          # app factory, db.init, register blueprints, create_all
  models.py            # entidades Usuario/Ocorrencia
  auth/routes.py       # login/logout
  dashboard/routes.py  # listagem e métricas de ocorrências
  ocorrencias/routes.py# criação/atualização de status
  usuarios/routes.py   # cadastro/listagem de usuários
  services/auth_service.py
  utils/auth.py
  templates/
config.py
run.py
docs/
```

## 2) Pontos fortes já presentes

1. **Modularização por blueprint** já implantada, facilitando crescimento por domínio.
2. **Fallback de banco em `config.py`** para SQLite local, útil para desenvolvimento rápido.
3. **Tratamento básico de erros de banco** com rollback em rotas críticas.
4. **Hash de senha com compatibilidade legada** no serviço de autenticação.

## 3) Riscos e lacunas para robustez

### 3.1 Banco e ciclo de deploy
- O uso de `db.create_all()` no startup reduz controle de evolução de schema.
- Falta trilha de migração/versionamento de banco.

**Impacto:** maior risco em produção, especialmente com múltiplos ambientes (dev/homolog/prod).

### 3.2 Acoplamento Web + Regra de negócio
- Ainda há regra de negócio dentro das rotas (validação de status, montagem de entidades, fluxos de autorização).
- Não existe uma camada de casos de uso/serviços por domínio (além de auth).

**Impacto:** dificulta testes unitários e reaproveitamento para API mobile.

### 3.3 Ausência de API para cliente mobile
- O projeto está orientado a HTML renderizado no servidor.
- Não há versionamento de API, serialização de resposta nem contrato público.

**Impacto:** aplicativo mobile exigirá duplicação de regras ou criação urgente de backend API depois.

### 3.4 Segurança/observabilidade
- Sessão baseada em cookie atende web, mas não é ideal como base para mobile.
- Não há evidência de logs estruturados, rastreabilidade por request-id, nem monitoramento de erro.

**Impacto:** operação e suporte escalam mal quando aumentar número de usuários.

### 3.5 Qualidade e governança técnica
- Não há pasta de testes automatizados versionada na branch.
- Não há padrão de DTO/schema para entrada/saída de dados.

**Impacto:** regressão frequente e baixa previsibilidade de entrega.

## 4) Recomendações priorizadas para preparar Web + Mobile

## Prioridade 1 (fundação — curto prazo)

1. **Adotar migrações com Flask-Migrate/Alembic**
   - Remover dependência de `db.create_all()` para evolução de schema.
   - Criar fluxo padrão: `flask db migrate` + `flask db upgrade`.

2. **Criar camada de aplicação (use cases/services por domínio)**
   - `app/services/ocorrencias_service.py`
   - `app/services/usuarios_service.py`
   - Rotas ficam finas (somente HTTP e apresentação).

3. **Adicionar suíte de testes mínima**
   - Testes de autenticação, autorização e fluxo de ocorrência.
   - Testes de serviço independentes de template.

4. **Introduzir validação de entrada padronizada**
   - Flask-WTF para web forms.
   - Marshmallow/Pydantic para payloads de API.

## Prioridade 2 (habilitar mobile sem quebrar web)

1. **Criar API versionada (`/api/v1`) em blueprints próprios**
   - Ex.: `app/api/v1/auth.py`, `app/api/v1/ocorrencias.py`, `app/api/v1/usuarios.py`.

2. **Definir estratégia de autenticação para mobile**
   - JWT (access + refresh) para app mobile.
   - Manter sessão cookie para web tradicional (transição gradual).

3. **Padronizar contratos de resposta**
   - Envelopes consistentes (`data`, `error`, `meta`).
   - Códigos HTTP e mensagens previsíveis.

4. **Documentar API com OpenAPI/Swagger**
   - Viabiliza integração mais rápida do time mobile.

## Prioridade 3 (escala e operação)

1. **Observabilidade**
   - Logging estruturado (JSON), correlation/request id, captura de exceções.

2. **Controle de configuração por ambiente**
   - `config/dev.py`, `config/test.py`, `config/prod.py`.

3. **Paginação/filtros server-side e indexação de banco**
   - Preparar consultas para crescimento de dados de ocorrências.

4. **Pipeline de qualidade (CI)**
   - lint + testes + checagem de segurança.

## 5) Proposta de arquitetura-alvo (incremental)

```text
app/
  __init__.py
  models/
    usuario.py
    ocorrencia.py
  web/
    auth/routes.py
    dashboard/routes.py
    usuarios/routes.py
    ocorrencias/routes.py
  api/
    v1/
      auth/routes.py
      usuarios/routes.py
      ocorrencias/routes.py
      schemas/
  services/
    auth_service.py
    usuarios_service.py
    ocorrencias_service.py
  repositories/
  utils/
migrations/
tests/
```

> Observação: não precisa fazer big-bang. A evolução pode ser por estrangulamento, mantendo rotas web existentes e introduzindo API aos poucos.

## 6) Plano de execução em 30/60/90 dias

### 0–30 dias
- Migrar para Alembic.
- Criar testes essenciais.
- Extrair serviços de `usuarios` e `ocorrencias`.

### 31–60 dias
- Publicar `/api/v1` com login + CRUD de ocorrências.
- Definir contratos e documentação OpenAPI.
- Implementar JWT para mobile.

### 61–90 dias
- Completar observabilidade e CI robusta.
- Otimizar consultas, paginação e índices.
- Preparar versão beta integrada com app mobile.

## 7) Conclusão executiva

A base atual está **boa para continuidade do produto web**, pois já tem blueprints e organização inicial.
Para ficar realmente robusta e pronta para um novo app mobile, o passo mais importante é **separar melhor regra de negócio e exposição HTTP**, junto com **migração de banco + API versionada + testes**.

Esse conjunto reduz risco técnico e permite escalar o backend para dois clientes (web e mobile) sem duplicar lógica.
