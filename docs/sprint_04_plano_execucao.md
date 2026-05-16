# Sprint 4 — Plano operacional para deixar a entrega pronta

**Objetivo:** aproveitar a preparação da documentação da Sprint 3 para já deixar a Sprint 4 pronta como evolução técnica e funcional do ConectaLar.

## 1. Meta da Sprint 4

Entregar uma versão mais robusta do sistema, com evidências organizadas, validações mínimas, testes automatizados iniciais e melhoria na confiabilidade dos fluxos de usuários e ocorrências.

## 2. Backlog recomendado

| Prioridade | História/Tarefa | Descrição | Critério de aceite |
| --- | --- | --- | --- |
| P0 | Organizar evidências finais | Padronizar prints, consultas SQL e roteiro de apresentação | Pasta de evidências preenchida e documentada |
| P0 | Validar formulário de ocorrência | Exigir título e descrição válidos antes de gravar | Dados vazios não são persistidos e exibem mensagem amigável |
| P0 | Validar cadastro de usuário | Exigir nome, e-mail, senha, unidade e tipo válido | Cadastro inválido não grava no banco |
| P1 | Melhorar tratamento de erros | Remover `print` e evitar exibir erro técnico para usuário | Logs usam logger e tela mostra mensagem segura |
| P1 | Criar testes automatizados | Cobrir app factory, login, autorização, cadastro e ocorrência | `pytest` executa com sucesso localmente |
| P1 | Melhorar dashboard | Adicionar busca/paginação ou filtro adicional por texto/data | Listagem permanece utilizável com mais registros |
| P2 | Criar migração inicial | Preparar Flask-Migrate/Alembic para versionar schema | Migração inicial documentada e executável |
| P2 | Padronizar timezone | Persistir datas em UTC e formatar para exibição | Data consistente no banco e na tela |

## 3. Ordem de execução sugerida

### Etapa 1 — Fechamento da entrega Sprint 3

- Revisar `docs/sprint_03_documentacao_entrega.md`.
- Coletar evidências mínimas: tela, banco, commits e estrutura modular.
- Confirmar que a aplicação sobe localmente.

### Etapa 2 — Robustez de entrada de dados

- Criar validações simples para cadastro de usuário.
- Criar validações simples para ocorrência.
- Garantir que mensagens de erro sejam claras e não técnicas.

### Etapa 3 — Testes mínimos

- Adicionar configuração de testes com banco isolado em SQLite.
- Testar criação do app.
- Testar login com usuário válido/inválido.
- Testar proteção de rota sem sessão.
- Testar criação de ocorrência autenticada.

### Etapa 4 — Preparação de demonstração

- Atualizar matriz de rastreabilidade com novos commits.
- Gerar prints finais.
- Executar roteiro de apresentação do início ao fim.
- Registrar comandos e resultados usados na validação.

## 4. Definição de pronto

A Sprint 4 estará pronta quando:

- [ ] documentação da Sprint 3 estiver enviada;
- [ ] evidências estiverem organizadas por sprint;
- [ ] validações server-side impedirem dados vazios/inválidos;
- [ ] erros técnicos não aparecerem para o usuário final;
- [ ] testes automatizados mínimos existirem e passarem;
- [ ] matriz de rastreabilidade estiver atualizada com os commits da Sprint 4;
- [ ] roteiro de demonstração puder ser executado sem improviso.

## 5. Comandos de validação recomendados

```bash
python -m compileall app config.py run.py criar_usuario.py
```

```bash
git log --oneline --name-only --max-count=15
```

```bash
git status --short
```

```bash
curl -i http://127.0.0.1:5000/healthz
```

## 6. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Faltar evidência visual no envio da Sprint 3 | Avaliação considerar entrega incompleta | Usar checklist e nomear prints de forma padronizada |
| Banco local diferente do banco demonstrado | Dificuldade de comprovar persistência | Registrar ambiente usado e anexar consultas SQL |
| Novas melhorias quebrarem fluxo existente | Atraso na Sprint 4 | Fazer mudanças pequenas e testar após cada commit |
| Falta de rastreabilidade | Dificuldade de defender a entrega | Atualizar matriz de commits a cada funcionalidade |
