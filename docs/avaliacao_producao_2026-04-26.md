# Avaliação de prontidão para produção — ConectaLar

**Data da análise:** 26/04/2026  
**Escopo:** revisão técnica do código atual (Flask + SQLAlchemy), sem acesso a logs/infra de produção.

## Resumo executivo

O sistema está funcional para MVP, com boas bases como separação por blueprints, uso de hash de senha e controle de acesso por perfil. Contudo, ainda há riscos relevantes para operação em produção contínua (segurança, governança de banco, observabilidade e execução).

**Classificação geral atual:** 🟡 **produção assistida** (adequado para uso controlado), mas **não ideal para escala/ambiente crítico** sem ajustes.

## Pontos fortes identificados

- Estrutura modular por domínio com blueprints (`auth`, `dashboard`, `ocorrencias`, `usuarios`).
- Sessão e autorização por tipo de usuário (`morador`/`sindico`).
- Hash de senha com compatibilidade entre legado bcrypt e padrão Werkzeug.
- Tratamento básico de erro transacional em operações de escrita (rollback em exceções SQLAlchemy).

## Riscos e lacunas por prioridade

## 🔴 Alta prioridade (corrigir antes de ampliar uso)

1. **`SECRET_KEY` insegura por fallback padrão em código**
   - Hoje existe chave estática como fallback em `config.py`.
   - Impacto: sessões podem ser comprometidas em ambientes mal configurados.
   - Recomendação: tornar `SECRET_KEY` obrigatória em produção e falhar startup se ausente.

2. **Criação de schema com `db.create_all()` no startup**
   - O boot tenta alterar schema automaticamente.
   - Impacto: deriva de schema, risco operacional e ausência de histórico/auditoria.
   - Recomendação: substituir por migrações versionadas (Alembic/Flask-Migrate) e remover `create_all` do boot.

3. **Execução com `debug=True` no ponto de entrada**
   - `run.py` sobe com debug habilitado.
   - Impacto: exposição de informações sensíveis e comportamento inadequado em produção.
   - Recomendação: parametrizar por ambiente (`FLASK_ENV`/`DEBUG`) e usar WSGI server (gunicorn/uwsgi).

4. **Ausência de proteção CSRF em formulários POST**
   - Formulários usam `request.form` diretamente.
   - Impacto: vulnerabilidade a ataques CSRF.
   - Recomendação: Flask-WTF com CSRF global e tokens em todos os forms.

## 🟠 Média prioridade (estabilidade e manutenção)

1. **Validação de entrada limitada**
   - Campos de cadastro/ocorrência não têm validação centralizada de formato/tamanho.
   - Recomendação: schemas/forms com validações server-side e mensagens padronizadas.

2. **Ausência de testes automatizados**
   - Não há suíte de testes no repositório.
   - Recomendação: iniciar com testes de autenticação/autorização, fluxo de ocorrência e permissões.

3. **Observabilidade mínima**
   - Sem padrão de logs estruturados, correlação de request, métricas e healthcheck.
   - Recomendação: logging JSON, endpoint `/healthz`, tracking de erros (ex.: Sentry).

4. **Timezone manual (`utcnow() - 3h`)**
   - Ajuste de fuso é fixo no modelo.
   - Recomendação: salvar UTC puro no banco e converter no front/visualização.

## 🟡 Baixa prioridade (melhoria contínua)

1. **Padronização de respostas de autorização**
   - `sindico_obrigatorio` retorna string simples `403`.
   - Recomendação: template de erro e resposta consistente.

2. **Escalabilidade de listagens**
   - Listas sem paginação no dashboard/usuários.
   - Recomendação: paginação + filtros + índices no banco conforme consultas reais.

## Plano de evolução recomendado (curto prazo)

### Sprint 1 — Hardening de produção (1 semana)
- Remover `SECRET_KEY` default e exigir variável em produção.
- Remover `db.create_all()` de runtime e introduzir migrações.
- Desligar `debug=True` por default e configurar execução WSGI.
- Adicionar CSRF global.

### Sprint 2 — Confiabilidade (1–2 semanas)
- Implementar testes automatizados (happy path + autorização).
- Criar healthcheck, logging estruturado e handler global de erro.
- Padronizar validações de entrada.

### Sprint 3 — Escala funcional (2 semanas)
- Paginação e filtros avançados para dashboard/listagem de usuários.
- Ajustes de performance orientados por consulta (índices, profiling).
- Backlog de UX e notificações.

## Critérios de pronto para “produção robusta”

- [ ] Migrações versionadas ativas e sem `create_all` no boot.
- [ ] Segredos obrigatórios por ambiente e rotação definida.
- [ ] CSRF habilitado em todos os formulários mutáveis.
- [ ] Testes mínimos cobrindo autenticação e autorização.
- [ ] Observabilidade básica (logs + healthcheck + erro centralizado).
- [ ] Deploy sem debug, por servidor WSGI e configuração por ambiente.

---

Se você quiser, no próximo passo eu transformo este diagnóstico em um **plano de execução técnico com tarefas priorizadas por impacto x esforço** (já quebrado em issues).
