# Sprint 4 — Plano de finalização, evidências e rastreabilidade

**Objetivo:** transformar os pontos observados na avaliação da Sprint 3 em entregáveis objetivos para a Sprint 4, com documentação técnica suficiente para demonstrar arquitetura modular, persistência real dos dados e rastreabilidade entre funcionalidade, commit e evidência.

## 1. Diagnóstico executivo

A avaliação da Sprint 3 apontou três lacunas de apresentação e comprovação, não necessariamente ausência total de implementação:

1. **Mostrar a estrutura modular do projeto:** o projeto já utiliza `Blueprints` por domínio, mas essa organização precisa estar explicitada em um artefato de entrega.
2. **Comprovar a persistência dos dados no banco:** o código já persiste usuários e ocorrências via SQLAlchemy, porém a banca precisa de evidências reproduzíveis, como prints, comandos SQL e roteiro de teste.
3. **Relacionar cada funcionalidade ao respectivo commit e evidência:** o histórico Git contém commits relevantes, mas falta uma matriz de rastreabilidade que conecte funcionalidade, arquivo, commit e evidência esperada.

## 2. Melhorias necessárias para alcançar o objetivo da Sprint 4

| Prioridade | Melhoria | Por que é necessária | Entregável esperado |
| --- | --- | --- | --- |
| Alta | Publicar uma visão modular do projeto | Facilita a avaliação da arquitetura e demonstra separação de responsabilidades | Diagrama/árvore de módulos + tabela de responsabilidades |
| Alta | Criar roteiro de comprovação de persistência | Mostra que os dados não ficam apenas em memória/sessão | Evidência com cadastro, criação de ocorrência e consulta no banco |
| Alta | Criar matriz funcionalidade × commit × evidência | Garante rastreabilidade e facilita auditoria acadêmica | Tabela com funcionalidade, commit, arquivos e evidências |
| Média | Padronizar pasta de evidências | Evita prints soltos e nomes inconsistentes | Estrutura `docs/evidencias/sprint-04/` |
| Média | Definir critérios de aceite da Sprint 4 | Evita entrega subjetiva | Checklist de pronto com validação objetiva |
| Média | Complementar testes manuais com comandos técnicos | Reforça confiança na entrega | Comandos SQL, `git log`, execução local e healthcheck |

## 3. Sugestão de evolução do sistema para a Sprint 4

A recomendação técnica é que a Sprint 4 não tente apenas "tirar prints" para a avaliação. Ela deve consolidar o MVP em uma entrega demonstrável, rastreável e mais confiável. A evolução sugerida é organizar a sprint em quatro frentes complementares: documentação/evidências, confiabilidade técnica, melhorias funcionais de alto valor e preparação para produção assistida.

### 3.1 Objetivo macro da Sprint 4

**Objetivo recomendado:** entregar uma versão do ConectaLar que consiga demonstrar, de ponta a ponta, que a arquitetura está modularizada, que usuários e ocorrências são persistidos no banco, que as principais funcionalidades são rastreáveis no Git e que os fluxos críticos têm critérios de aceite verificáveis.

### 3.2 Backlog priorizado

| Prioridade | Item de evolução | Descrição objetiva | Critério de aceite | Evidência esperada |
| --- | --- | --- | --- | --- |
| P0 | Evidenciar arquitetura modular | Mostrar a separação por blueprints, serviços, utilitários, modelos e templates | Documento com árvore modular e responsabilidades por módulo revisado | Print/trecho da árvore de pastas e seção de responsabilidades |
| P0 | Comprovar persistência real | Executar cadastro de usuário, criação de ocorrência e atualização de status com consulta direta no banco | O mesmo dado exibido na tela aparece em consulta SQL após reiniciar a aplicação | Prints das telas + consulta SQL em `usuarios` e `ocorrencias` |
| P0 | Fechar rastreabilidade por commit | Relacionar cada funcionalidade entregue ao commit, arquivos alterados e evidência | Matriz revisada com commits atuais e evidências coletadas | Tabela de rastreabilidade preenchida |
| P1 | Adicionar validações server-side | Validar campos obrigatórios, tamanho mínimo e status permitido antes de persistir | Formulários rejeitam dados inválidos com mensagem amigável | Teste manual com dados inválidos + print da mensagem |
| P1 | Criar testes automatizados mínimos | Cobrir app factory, login, autorização de síndico, criação de ocorrência e dashboard | Testes executam localmente e passam | Saída do `pytest` anexada |
| P1 | Padronizar tratamento de erros de cadastro | Substituir `print` por `app.logger` e mensagens seguras ao usuário | Erro técnico não vaza para tela e é registrado em log | Evidência de erro controlado |
| P2 | Melhorar listagens | Adicionar busca/filtro/paginação no dashboard e usuários | Listagens continuam usáveis com muitos registros | Print com filtro/paginação funcionando |
| P2 | Preparar migrações versionadas | Iniciar Flask-Migrate/Alembic para evoluir schema sem depender de `create_all` | Migração inicial criada e documentada | Arquivos de migração + comando documentado |

### 3.3 Sequência recomendada de execução

1. **Dia 1 — Fechamento de arquitetura e evidências:** revisar esta documentação, completar a matriz de commits e criar a pasta final de evidências.
2. **Dia 2 — Persistência ponta a ponta:** executar o fluxo completo no sistema, coletar prints e consultas SQL, reiniciar a aplicação e provar que os dados permanecem no banco.
3. **Dia 3 — Qualidade mínima:** implementar validações server-side e testes automatizados dos fluxos críticos.
4. **Dia 4 — Ajustes de robustez:** padronizar logs, remover mensagens técnicas da interface e revisar configurações de ambiente.
5. **Dia 5 — Ensaio de apresentação:** rodar o sistema do zero, seguir o roteiro de evidências e garantir que cada funcionalidade tenha commit e prova associada.

### 3.4 Resultado esperado ao final da Sprint 4

Ao final da Sprint 4, a entrega deve permitir responder objetivamente às três perguntas da avaliação:

- **Onde está a modularização?** Na estrutura por blueprints/domínios, serviços, utilitários e modelos documentada neste guia.
- **Como sei que os dados persistem?** Pelo fluxo tela → banco → reinicialização → consulta SQL, com prints e queries salvos como evidência.
- **Qual commit prova cada funcionalidade?** Pela matriz de rastreabilidade que liga funcionalidade, hash do commit, arquivos e evidência coletada.

## 4. Estrutura modular atual do projeto

```text
conectalar/
├── app/
│   ├── __init__.py              # App factory, registro de blueprints, CSRF, healthcheck e handlers de erro
│   ├── models.py                # Modelos persistidos: Usuario e Ocorrencia
│   ├── auth/                    # Login e logout
│   │   └── routes.py
│   ├── dashboard/               # Painel, filtros, contadores e ordenação de ocorrências
│   │   └── routes.py
│   ├── ocorrencias/             # Registro e atualização de status de ocorrências
│   │   └── routes.py
│   ├── usuarios/                # Cadastro e listagem de usuários
│   │   └── routes.py
│   ├── services/                # Regras reutilizáveis, como hash/verificação de senha
│   │   └── auth_service.py
│   ├── utils/                   # Autorização, login obrigatório e CSRF
│   │   ├── auth.py
│   │   └── csrf.py
│   ├── templates/               # Telas HTML do sistema
│   └── static/                  # Arquivos estáticos
├── config.py                    # Configuração por ambiente e banco
├── run.py                       # Ponto de execução local
├── criar_usuario.py             # Script auxiliar para usuário inicial
└── docs/                        # Documentação técnica, avaliação e evidências
```

### 3.1 Responsabilidades por módulo

| Módulo | Responsabilidade | Evidência no código |
| --- | --- | --- |
| `app/__init__.py` | Inicializa o Flask, configura banco, registra blueprints, ativa CSRF, expõe `/healthz` e handlers de erro | `create_app()` e `app.register_blueprint(...)` |
| `app/auth/routes.py` | Autenticação, sessão e logout | Rotas `/` e `/logout` |
| `app/dashboard/routes.py` | Dashboard, filtro por status, contadores e ordenação | Rota `/dashboard` |
| `app/ocorrencias/routes.py` | Criação de ocorrência e atualização de status pelo síndico | Rotas `/nova-ocorrencia` e `/atualizar-status/<id>/<status>` |
| `app/usuarios/routes.py` | Cadastro e listagem de usuários por perfil autorizado | Rotas `/cadastro` e `/usuarios` |
| `app/models.py` | Mapeamento relacional e persistência das entidades | Tabelas `usuarios` e `ocorrencias` |
| `app/services/auth_service.py` | Hash e verificação de senha | Funções `gerar_hash_senha` e `verificar_senha` |
| `app/utils/auth.py` | Decorators de autenticação e autorização | `login_obrigatorio` e `sindico_obrigatorio` |
| `app/utils/csrf.py` | Proteção CSRF para requisições mutáveis | Geração e validação de token |


## 5. Comprovação de persistência no banco


A persistência deve ser demonstrada com uma sequência simples, reproduzível e documentada.

### 4.1 Preparação do ambiente

1. Subir o banco PostgreSQL configurado no `.env` ou usar a `DATABASE_URL` equivalente.
2. Garantir que a aplicação esteja apontando para o banco correto.
3. Executar a aplicação:

```bash
python run.py
```

4. Criar um usuário inicial, se necessário:

```bash
python criar_usuario.py
```

### 4.2 Roteiro de evidência funcional

| Passo | Ação | Resultado esperado | Evidência a salvar |
| --- | --- | --- | --- |
| 1 | Acessar a tela de login | Formulário de autenticação carregado | `01-login.png` |
| 2 | Entrar como síndico/admin | Redirecionamento para dashboard | `02-dashboard-inicial.png` |
| 3 | Cadastrar usuário morador | Mensagem de sucesso e usuário disponível no banco | `03-cadastro-usuario.png` |
| 4 | Criar uma ocorrência | Ocorrência aparece no dashboard | `04-nova-ocorrencia.png` |
| 5 | Alterar status da ocorrência | Status atualizado no dashboard | `05-status-atualizado.png` |
| 6 | Consultar o banco diretamente | Registros aparecem nas tabelas relacionais | `06-consulta-banco.png` |

### 4.3 Consultas SQL para comprovação

Execute as consultas abaixo no PostgreSQL após realizar o fluxo funcional:

```sql
SELECT id, nome, email, unidade, tipo
FROM usuarios
ORDER BY id DESC
LIMIT 5;
```

```sql
SELECT o.id,
       o.titulo,
       o.status,
       o.data_criacao,
       u.nome AS autor,
       u.unidade
FROM ocorrencias o
JOIN usuarios u ON u.id = o.usuario_id
ORDER BY o.id DESC
LIMIT 5;
```

```sql
SELECT status, COUNT(*) AS total
FROM ocorrencias
GROUP BY status
ORDER BY status;
```

### 4.4 Critério de aceite da persistência

A persistência estará comprovada quando houver:

- print da tela com o registro criado;
- print ou exportação da consulta SQL exibindo o mesmo registro;
- evidência de relacionamento entre `ocorrencias.usuario_id` e `usuarios.id`;
- registro permanecendo disponível após reiniciar a aplicação.


## 6. Matriz de rastreabilidade: funcionalidade × commit × evidência

> Observação: os hashes abaixo foram extraídos do histórico atual com `git log --oneline --name-only`. Se novos ajustes forem realizados na Sprint 4, inclua os novos commits nesta tabela antes da entrega final.

| Funcionalidade/entrega | Commit relacionado | Arquivos principais | Evidência recomendada |
| --- | --- | --- | --- |
| Modularização por blueprints e organização Sprint 3 | `f40dcb3` — `demandas sprint-3` | `app/__init__.py`, `app/dashboard/routes.py`, `app/ocorrencias/routes.py`, `app/usuarios/routes.py`, `run.py` | Print da árvore de pastas + trecho de registro de blueprints |
| Estabilização de rotas e tratamento de erros transacionais | `c40c307` — `fix: estabiliza rotas, app factory e tratamento de erros` | `app/auth/routes.py`, `app/ocorrencias/routes.py`, `app/usuarios/routes.py` | Demonstração de login, cadastro e ocorrência sem erro |
| Ajuste do app factory e inicialização | `073a6d9` — `correção init` | `app/__init__.py`, `app/utils/__init__.py`, `run.py` | Execução local da aplicação |
| Hardening de configuração para produção | `b18173d` — `feat: inicia hardening de configuração para produção` | `config.py`, `run.py`, `README.md` | Print/trecho das variáveis de ambiente e debug configurável |
| CSRF, healthcheck e handlers de erro | `1b0316c` — `feat: adiciona csrf, healthcheck e handlers de erro` | `app/__init__.py`, `app/utils/csrf.py`, `app/templates/error.html` | `GET /healthz`, formulário com token CSRF e página de erro |
| Redesenho visual do dashboard e telas | `8c6dc4f` — `feat: redesenha dashboard com sidebar e layout moderno` | `app/templates/base.html`, `app/templates/dashboard.html`, `app/templates/login.html` | Prints do dashboard, login e formulários |
| Correção de cadastro de usuário | `6f11878` — `erro cadastro de usuario` | `app/usuarios/routes.py` | Cadastro de usuário com sucesso + consulta SQL em `usuarios` |
| Ajuste final da tela de login | `1dbf48f` — `ajuste tela de login` | `app/templates/login.html` | Print da tela de login atualizada |
| Documentação de avaliação e prontidão | `600f1d2`, `4a5b8e7`, `7a074b6` — merges de avaliação | `docs/avaliacao_estrutura_projeto.md`, `docs/avaliacao_producao_2026-04-26.md` | Documentos anexados na entrega |


## 7. Estrutura recomendada para evidências da Sprint 4

Criar e preencher a seguinte estrutura durante a finalização:

```text
docs/evidencias/sprint-04/
├── 01-login.png
├── 02-dashboard-inicial.png
├── 03-cadastro-usuario.png
├── 04-nova-ocorrencia.png
├── 05-status-atualizado.png
├── 06-consulta-banco.png
├── 07-healthcheck.png
└── README.md
```

Conteúdo mínimo recomendado para `docs/evidencias/sprint-04/README.md`:

```markdown
# Evidências Sprint 4

- Data da coleta:
- Ambiente usado:
- Banco usado:
- Commit da entrega:
- Responsável pela coleta:

## Evidências

| Arquivo | O que comprova |
| --- | --- |
| 01-login.png | Tela inicial de autenticação |
| 02-dashboard-inicial.png | Acesso autenticado ao dashboard |
| 03-cadastro-usuario.png | Cadastro persistido de usuário |
| 04-nova-ocorrencia.png | Criação persistida de ocorrência |
| 05-status-atualizado.png | Atualização persistida do status |
| 06-consulta-banco.png | Consulta SQL comprovando persistência |
| 07-healthcheck.png | Saúde da aplicação e conexão com banco |
```


## 8. Critérios de pronto da Sprint 4



- [ ] README atualizado apontando para este documento de finalização.
- [ ] Estrutura modular explicada com árvore de pastas e responsabilidades.
- [ ] Aplicação executando localmente sem erro.
- [ ] Login validado com usuário existente.
- [ ] Cadastro de usuário executado e persistido no banco.
- [ ] Criação de ocorrência executada e persistida no banco.
- [ ] Atualização de status executada e persistida no banco.
- [ ] Consultas SQL salvas como evidência.
- [ ] Prints organizados em `docs/evidencias/sprint-04/`.
- [ ] Matriz funcionalidade × commit × evidência revisada com o último commit da entrega.
- [ ] Commit final criado com a documentação e ajustes finais da Sprint 4.


## 9. Recomendações técnicas para o próximo incremento

Após concluir a Sprint 4, as próximas melhorias técnicas recomendadas são:

1. **Migrações versionadas:** substituir criação automática de schema por Flask-Migrate/Alembic.
2. **Validação formal de formulários:** centralizar regras de obrigatoriedade, tamanho, formato de e-mail e status permitido.
3. **Testes automatizados:** criar testes de login, autorização de síndico, cadastro, criação de ocorrência e atualização de status.
4. **Paginação e busca:** evitar listagens grandes no dashboard e na tela de usuários.
5. **Logs estruturados:** registrar erros e operações críticas sem usar `print`.
6. **Padronização de timezone:** persistir datas em UTC e formatar para Brasília apenas na interface.


## 10. Comandos úteis para a apresentação




```bash
# Ver estrutura de alto nível do projeto
find app -maxdepth 2 -type f | sort
```

```bash
# Ver commits recentes com arquivos alterados
git log --oneline --name-only --max-count=12
```

```bash
# Ver status do repositório antes da entrega
git status --short
```

```bash
# Testar healthcheck com a aplicação em execução
curl -i http://127.0.0.1:5000/healthz
```

```bash
# Executar a aplicação localmente
python run.py
```
