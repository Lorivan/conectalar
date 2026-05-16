# Sprint 3 — Documentação para envio da avaliação

**Data limite planejada para envio:** 17/05/2026  
**Projeto:** ConectaLar — Sistema de Gestão Condominial  
**Objetivo deste documento:** consolidar, em um único material de envio, as evidências solicitadas na avaliação da Sprint 3 e preparar a transição direta para a Sprint 4.

## 1. Resumo da entrega

A Sprint 3 deve ser apresentada como a etapa em que o projeto deixou de ser apenas um MVP funcional e passou a demonstrar três pontos avaliáveis:

1. **Estrutura modular do projeto**, com separação por domínios usando blueprints Flask.
2. **Persistência dos dados no banco**, com usuários e ocorrências gravados por SQLAlchemy.
3. **Rastreabilidade entre funcionalidade, commit e evidência**, permitindo verificar o que foi entregue, onde foi alterado e como comprovar.

## 2. Estrutura modular do projeto

O projeto está organizado em módulos por responsabilidade. Essa estrutura facilita manutenção, testes, evolução e apresentação técnica.

```text
app/
├── __init__.py          # Criação da aplicação, banco, blueprints, CSRF, healthcheck e handlers
├── models.py            # Modelos persistidos no banco: Usuario e Ocorrencia
├── auth/                # Login, logout e sessão
├── dashboard/           # Painel, filtros, contadores e ordenação
├── ocorrencias/         # Criação e atualização de ocorrências
├── usuarios/            # Cadastro e listagem de usuários
├── services/            # Regras reutilizáveis de negócio/segurança
├── utils/               # Decorators de acesso e proteção CSRF
├── templates/           # Páginas HTML
└── static/              # Arquivos estáticos
```

### 2.1 Evidência técnica da modularização

| Módulo | Responsabilidade | Evidência no código |
| --- | --- | --- |
| `app/__init__.py` | Inicializa a aplicação, registra blueprints e configura recursos globais | `create_app()` e `app.register_blueprint(...)` |
| `app/auth/routes.py` | Login, logout e criação de sessão | Rotas `/` e `/logout` |
| `app/dashboard/routes.py` | Dashboard, filtro por status, ordenação e contadores | Rota `/dashboard` |
| `app/ocorrencias/routes.py` | Registro de ocorrência e alteração de status | Rotas `/nova-ocorrencia` e `/atualizar-status/<id>/<status>` |
| `app/usuarios/routes.py` | Cadastro e listagem de usuários | Rotas `/cadastro` e `/usuarios` |
| `app/models.py` | Entidades persistidas no banco | Classes `Usuario` e `Ocorrencia` |
| `app/services/auth_service.py` | Hash e verificação de senha | `gerar_hash_senha()` e `verificar_senha()` |
| `app/utils/auth.py` | Controle de autenticação e autorização | `login_obrigatorio` e `sindico_obrigatorio` |
| `app/utils/csrf.py` | Proteção CSRF para formulários | Token CSRF e validação em requisições mutáveis |

## 3. Comprovação de persistência dos dados

A persistência deve ser comprovada mostrando que os dados cadastrados pela interface são gravados no banco e continuam disponíveis após reiniciar a aplicação.

### 3.1 Fluxo recomendado para demonstrar persistência

| Ordem | Ação | Resultado esperado | Evidência para anexar |
| --- | --- | --- | --- |
| 1 | Iniciar a aplicação | Sistema disponível no navegador | Print do terminal ou tela inicial |
| 2 | Fazer login como síndico/admin | Dashboard carregado | `02-dashboard-inicial.png` |
| 3 | Cadastrar um morador | Usuário criado com sucesso | `03-cadastro-usuario.png` |
| 4 | Consultar tabela `usuarios` | Usuário aparece no banco | `04-sql-usuarios.png` |
| 5 | Criar uma ocorrência | Ocorrência aparece no dashboard | `05-nova-ocorrencia.png` |
| 6 | Consultar tabela `ocorrencias` com join em `usuarios` | Ocorrência aparece relacionada ao autor | `06-sql-ocorrencias.png` |
| 7 | Reiniciar a aplicação e acessar novamente | Dados continuam disponíveis | `07-dashboard-pos-reinicio.png` |

### 3.2 Consultas SQL para anexar na avaliação

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

## 4. Matriz de rastreabilidade da Sprint 3

| Funcionalidade/entrega | Commit relacionado | Arquivos principais | Evidência para envio |
| --- | --- | --- | --- |
| Modularização por blueprints | `f40dcb3` — `demandas sprint-3` | `app/__init__.py`, `app/dashboard/routes.py`, `app/ocorrencias/routes.py`, `app/usuarios/routes.py` | Print da estrutura de pastas e tabela de responsabilidades |
| Estabilização de rotas e tratamento transacional | `c40c307` — `fix: estabiliza rotas, app factory e tratamento de erros` | `app/auth/routes.py`, `app/ocorrencias/routes.py`, `app/usuarios/routes.py` | Fluxo de login, cadastro e ocorrência funcionando |
| Correção de inicialização da aplicação | `073a6d9` — `correção init` | `app/__init__.py`, `app/utils/__init__.py`, `run.py` | Aplicação executando localmente |
| Hash/verificação de senha e serviços | `f40dcb3` — `demandas sprint-3` | `app/services/auth_service.py` | Login com senha válida e senha inválida |
| Dashboard com filtros e contadores | `f40dcb3`, `8c6dc4f` | `app/dashboard/routes.py`, `app/templates/dashboard.html` | Print do dashboard com cards e filtro por status |
| Cadastro de usuário | `6f11878` — `erro cadastro de usuario` | `app/usuarios/routes.py` | Usuário cadastrado e consulta SQL em `usuarios` |
| Registro de ocorrência | `f40dcb3` — `demandas sprint-3` | `app/ocorrencias/routes.py`, `app/templates/nova_ocorrencia.html` | Ocorrência criada e consulta SQL em `ocorrencias` |
| Segurança básica: CSRF, healthcheck e erros | `1b0316c` — `feat: adiciona csrf, healthcheck e handlers de erro` | `app/__init__.py`, `app/utils/csrf.py`, `app/templates/error.html` | Print de `/healthz` e formulários com token |

## 5. Checklist para envio em 17/05/2026

Antes de enviar a documentação da Sprint 3, validar os itens abaixo:

- [ ] Documento `docs/sprint_03_documentacao_entrega.md` revisado pela equipe.
- [ ] Prints salvos em `docs/evidencias/sprint-03/` ou anexados no ambiente de entrega da disciplina.
- [ ] Consulta SQL de `usuarios` anexada.
- [ ] Consulta SQL de `ocorrencias` anexada.
- [ ] Print da estrutura modular anexado.
- [ ] Matriz de rastreabilidade revisada com os commits finais.
- [ ] Aplicação demonstrada localmente antes do envio.
- [ ] Link do repositório/branch informado na entrega.

## 6. Roteiro rápido para apresentação

1. Abrir o projeto e mostrar a estrutura modular em `app/`.
2. Explicar que cada domínio possui seu blueprint: autenticação, dashboard, ocorrências e usuários.
3. Executar a aplicação e realizar login.
4. Cadastrar um usuário e mostrar a consulta SQL correspondente.
5. Criar uma ocorrência e mostrar a consulta SQL com `JOIN` no usuário autor.
6. Mostrar a matriz de rastreabilidade com commits e evidências.
7. Encerrar explicando que a Sprint 4 seguirá com validações, testes, logs, paginação e migrações.

## 7. Ponte para a Sprint 4

A Sprint 3 deve ser entregue como documentação de evidência. A Sprint 4 deve transformar essas evidências em maturidade técnica, atacando os próximos pontos:

- validação server-side dos formulários;
- testes automatizados dos fluxos críticos;
- tratamento de erro sem vazamento de mensagens técnicas;
- paginação/filtros para listagens;
- migrações versionadas de banco;
- roteiro final de demonstração com evidências organizadas.
