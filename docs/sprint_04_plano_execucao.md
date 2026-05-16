# Sprint 4 — Plano de execução para entrega

**Objetivo do plano:** transformar os apontamentos da avaliação da Sprint 3 em uma execução prática para deixar a Sprint 4 pronta, com entregáveis verificáveis, evidências organizadas, melhorias técnicas priorizadas e roteiro de apresentação reproduzível.

**Contexto:** a documentação da Sprint 3 será enviada em **17/05/2026**. A Sprint 4 deve aproveitar essa base e evoluir o sistema para demonstrar maturidade técnica além da documentação: validação de dados, confiabilidade, testes mínimos, rastreabilidade e evidências finais.

## 1. Meta da Sprint 4

Entregar uma versão do ConectaLar que comprove, de forma prática e auditável:

1. que a estrutura modular do projeto está clara e sustentada por blueprints/domínios;
2. que usuários e ocorrências são persistidos no banco e continuam disponíveis após reinício da aplicação;
3. que cada funcionalidade relevante possui commit, evidência e critério de aceite;
4. que os fluxos críticos possuem validação mínima, tratamento seguro de erro e testes automatizados iniciais.

## 2. Escopo da Sprint 4

### 2.1 Dentro do escopo

- Finalizar a documentação e evidências derivadas da Sprint 3.
- Implementar validações server-side para cadastro de usuário e ocorrência.
- Melhorar tratamento de erros, removendo mensagens técnicas da interface e `print` em rota.
- Criar testes automatizados mínimos para fluxos críticos.
- Organizar prints, consultas SQL e evidências em pasta padronizada.
- Atualizar matriz de rastreabilidade com commits da Sprint 4.
- Ensaiar a apresentação final com roteiro de ponta a ponta.

### 2.2 Fora do escopo

- Reescrever a arquitetura inteira.
- Criar aplicativo mobile.
- Criar API REST completa.
- Implantar observabilidade avançada com métricas externas.
- Fazer refatorações grandes sem relação direta com a avaliação.

## 3. Backlog priorizado

| ID | Prioridade | Tarefa | Descrição | Critério de aceite | Evidência obrigatória |
| --- | --- | --- | --- | --- | --- |
| S4-01 | P0 | Fechar evidências da Sprint 3 | Revisar e anexar estrutura modular, consultas SQL, prints e matriz de commits | Material da Sprint 3 pronto para envio em 17/05/2026 | Documento e prints anexados |
| S4-02 | P0 | Validar cadastro de usuário | Exigir nome, e-mail, senha, unidade e tipo válido antes de persistir | Dados inválidos não são gravados e exibem mensagem amigável | Print de validação + commit |
| S4-03 | P0 | Validar ocorrência | Exigir título e descrição válidos antes de persistir | Ocorrência vazia não é gravada e usuário recebe feedback claro | Print de validação + commit |
| S4-04 | P0 | Comprovar persistência pós-reinício | Criar usuário/ocorrência, reiniciar app e consultar banco | Dados continuam disponíveis na tela e no banco | Print da tela + consulta SQL |
| S4-05 | P1 | Melhorar tratamento de erros | Trocar `print` por logger e evitar expor exceção técnica ao usuário | Falhas mostram mensagem segura e registram log técnico | Print/mensagem controlada + commit |
| S4-06 | P1 | Criar testes automatizados mínimos | Cobrir app factory, login, autorização, cadastro e ocorrência | `pytest` passa localmente | Saída do terminal |
| S4-07 | P1 | Melhorar listagem/dashboard | Avaliar busca, filtro adicional ou paginação simples | Dashboard continua usável com volume maior de ocorrências | Print do dashboard atualizado |
| S4-08 | P2 | Preparar migrações versionadas | Avaliar Flask-Migrate/Alembic e documentar caminho de adoção | Decisão técnica registrada, com ou sem implementação inicial | Nota técnica/commit |
| S4-09 | P2 | Atualizar rastreabilidade final | Relacionar cada entrega da Sprint 4 a commit e evidência | Matriz final sem lacunas | Tabela atualizada |
| S4-10 | P2 | Ensaio de apresentação | Executar roteiro completo sem improviso | Equipe consegue demonstrar do login à consulta SQL | Checklist marcado |

## 4. Cronograma sugerido

| Dia | Foco | Atividades | Saída esperada |
| --- | --- | --- | --- |
| D0 — 16/05/2026 | Preparação | Revisar documentação da Sprint 3 e este plano de Sprint 4 | Documentos revisados no repositório |
| D1 — 17/05/2026 | Envio Sprint 3 | Enviar documentação, prints e matriz de rastreabilidade da Sprint 3 | Sprint 3 entregue |
| D2 | Validações | Implementar validações de usuário e ocorrência | Formulários protegidos contra dados inválidos |
| D3 | Erros e testes | Ajustar logs/tratamento de erro e iniciar testes automatizados | Erros seguros e testes mínimos passando |
| D4 | Persistência e evidências | Executar fluxo tela → banco → reinício → banco | Evidências finais coletadas |
| D5 | Refinamento | Ajustar dashboard/listagens se houver tempo | Melhoria visual/funcional validada |
| D6 | Rastreabilidade | Atualizar matriz com commits da Sprint 4 | Tabela final revisada |
| D7 | Ensaio final | Rodar apresentação completa | Entrega pronta para demonstração |

## 5. Plano técnico de execução

### 5.1 Validações server-side

**Usuário:**

- `nome`: obrigatório, mínimo de 3 caracteres;
- `email`: obrigatório, formato básico de e-mail e unicidade no banco;
- `senha`: obrigatória, mínimo de 6 caracteres;
- `unidade`: obrigatória;
- `tipo`: aceitar apenas `sindico` ou `morador`.

**Ocorrência:**

- `titulo`: obrigatório, mínimo de 3 caracteres e limite coerente com o modelo;
- `descricao`: obrigatória, mínimo de 10 caracteres;
- `status`: manter somente valores válidos: `Pendente`, `Em Andamento`, `Resolvido`.

### 5.2 Tratamento de erros

- Não exibir exceções técnicas em `flash` para o usuário final.
- Substituir `print` por `current_app.logger.exception(...)` ou `current_app.logger.error(...)`.
- Manter `db.session.rollback()` em falhas de escrita.
- Padronizar mensagens amigáveis, por exemplo: “Não foi possível concluir a operação. Verifique os dados e tente novamente.”

### 5.3 Testes automatizados mínimos

Criar uma pasta `tests/` com, no mínimo:

| Arquivo sugerido | Cobertura esperada |
| --- | --- |
| `tests/conftest.py` | Configuração da aplicação em modo teste e banco isolado |
| `tests/test_app.py` | Criação do app e healthcheck |
| `tests/test_auth.py` | Login válido, login inválido e logout |
| `tests/test_autorizacao.py` | Acesso protegido sem sessão e restrição para síndico |
| `tests/test_ocorrencias.py` | Criação de ocorrência autenticada e persistência |
| `tests/test_usuarios.py` | Cadastro de usuário pelo síndico e validações |

## 6. Estratégia de commits e rastreabilidade

Cada entrega deve ter commit próprio para facilitar avaliação:

| Tipo de mudança | Padrão de commit sugerido |
| --- | --- |
| Validações | `feat: adiciona validacoes de formularios` |
| Tratamento de erro | `fix: padroniza tratamento de erros nas rotas` |
| Testes | `test: cobre fluxos criticos da sprint 4` |
| Evidências/documentação | `docs: atualiza evidencias da sprint 4` |
| Dashboard/listagem | `feat: melhora filtros do dashboard` |

Após cada commit, atualizar a matriz de rastreabilidade com:

- funcionalidade entregue;
- hash do commit;
- arquivos alterados;
- evidência visual ou técnica;
- responsável pela validação.

## 7. Coleta de evidências

Salvar evidências em `docs/evidencias/sprint-04/` ou anexá-las ao ambiente oficial de entrega com os mesmos nomes:

| Arquivo | O que comprova |
| --- | --- |
| `01-login.png` | Tela de login carregada |
| `02-dashboard-inicial.png` | Dashboard após autenticação |
| `03-validacao-cadastro.png` | Cadastro rejeitando dados inválidos |
| `04-cadastro-usuario.png` | Cadastro válido de usuário |
| `05-sql-usuarios.png` | Usuário persistido no banco |
| `06-validacao-ocorrencia.png` | Ocorrência rejeitando dados inválidos |
| `07-nova-ocorrencia.png` | Ocorrência válida no dashboard |
| `08-sql-ocorrencias.png` | Ocorrência persistida e relacionada ao usuário |
| `09-pos-reinicio.png` | Dados ainda disponíveis após reiniciar aplicação |
| `10-testes.png` | Execução dos testes automatizados |
| `11-healthcheck.png` | Endpoint `/healthz` funcionando |

## 8. Comandos de validação

```bash
python -m compileall app config.py run.py criar_usuario.py
```

```bash
pytest
```

```bash
git status --short
```

```bash
git log --oneline --name-only --max-count=20
```

```bash
curl -i http://127.0.0.1:5000/healthz
```

## 9. Roteiro de demonstração da Sprint 4

1. Mostrar documentação da Sprint 3 entregue e explicar como ela virou backlog da Sprint 4.
2. Mostrar a estrutura modular do projeto em `app/`.
3. Abrir a aplicação e fazer login.
4. Tentar cadastrar usuário inválido e demonstrar validação.
5. Cadastrar usuário válido e consultar no banco.
6. Tentar criar ocorrência inválida e demonstrar validação.
7. Criar ocorrência válida e consultar no banco com `JOIN` no usuário.
8. Reiniciar a aplicação e mostrar que os dados persistem.
9. Executar testes automatizados.
10. Mostrar matriz funcionalidade × commit × evidência.

## 10. Definição de pronto

A Sprint 4 estará pronta quando todos os itens abaixo estiverem concluídos:

- [ ] documentação da Sprint 3 enviada em 17/05/2026;
- [ ] backlog da Sprint 4 revisado pela equipe;
- [ ] validações server-side implementadas para usuário e ocorrência;
- [ ] tratamento de erro sem vazamento de exceção técnica para usuário;
- [ ] testes automatizados mínimos criados e passando;
- [ ] evidências visuais e SQL coletadas;
- [ ] dados comprovados após reinício da aplicação;
- [ ] matriz de rastreabilidade atualizada com commits da Sprint 4;
- [ ] roteiro de demonstração executado pelo menos uma vez;
- [ ] commit final e pull request criados.

## 11. Riscos e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Gastar a Sprint 4 apenas com documentação | Entrega fraca tecnicamente | Priorizar validações, testes e evidências práticas |
| Validações quebrarem fluxo existente | Atraso e retrabalho | Implementar uma validação por vez e testar manualmente |
| Testes exigirem refatoração maior | Atraso | Começar por testes de fumaça e fluxos principais |
| Banco demonstrado não ser o mesmo banco da aplicação | Evidência inconsistente | Registrar `.env`/ambiente usado e consultar o mesmo banco |
| Commits misturarem muitas mudanças | Rastreabilidade ruim | Fazer commits pequenos por tarefa |
| Falta de tempo para migrações | Entrega incompleta | Deixar migrações como P2 e documentar decisão técnica se não implementar |


## 12. Execução realizada

A execução técnica da Sprint 4 foi registrada em [`docs/sprint_04_execucao_realizada.md`](docs/sprint_04_execucao_realizada.md), incluindo validações implementadas, testes automatizados criados e resultado da execução.
