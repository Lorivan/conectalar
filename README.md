# 🏢 ConectaLar - Sistema de Gestão Condominial

Bem-vindo ao **ConectaLar**!

Este projeto é um **MVP (Produto Mínimo Viável)** desenvolvido como atividade de extensão para a disciplina de Programação Web Aplicada da UniEvangélica.

O sistema tem como objetivo **digitalizar e centralizar o registro de ocorrências** dos moradores do **Condomínio Casas Flamboyant**, trazendo mais organização, transparência e eficiência na comunicação com a administração.

---

## 📌 MVP documentado

A documentação completa do Produto Mínimo Viável está disponível em:

- [`docs/mvp.md`](docs/mvp.md)

O documento descreve:

- funcionalidades entregues;
- tecnologias utilizadas;
- páginas e rotas disponíveis;
- limitações do MVP;
- escopo recomendado para próximas evoluções.

---

## 🚀 Funcionalidades

### 🔐 Autenticação

- Login de usuários.
- Senhas protegidas com **bcrypt**.
- Controle de sessão.
- Logout.
- Redirecionamento de usuários não autenticados para a tela de login.

### 👥 Gestão de usuários

- Cadastro de moradores e usuários pelo síndico.
- Listagem de usuários cadastrados.
- Controle de acesso por perfil (**síndico** e **morador**).
- Validação de nome, e-mail, senha, unidade e tipo de usuário.
- Prevenção de cadastro duplicado por e-mail.

### 📋 Ocorrências

- Registro de ocorrências por usuários autenticados.
- Associação da ocorrência ao usuário autor.
- Visualização das ocorrências no painel principal.
- Controle de status pelo síndico:
  - Pendente;
  - Em Andamento;
  - Resolvido.

### 📊 Dashboard

- Ordenação por prioridade de status.
- Filtro por status.
- Busca por título ou descrição.
- Paginação de ocorrências.
- Cards com contadores por status e total geral.
- Datas formatadas para o fuso de Brasília.
- Interface responsiva com Bootstrap.

### 🔒 Segurança e operação

- Proteção CSRF para requisições mutáveis.
- Endpoint de saúde: `GET /healthz`.
- Páginas de erro padronizadas para `400`, `403`, `404` e `500`.
- Configuração por variáveis de ambiente.
- Exigência de `SECRET_KEY` em produção.

---

## 🛠 Tecnologias utilizadas

- **Back-end:** Python 3.x, Flask, Flask Blueprints.
- **Banco de dados:** PostgreSQL, SQLAlchemy, Flask-SQLAlchemy, psycopg2.
- **Front-end:** HTML5, CSS3, Jinja2, Bootstrap 5, Bootstrap Icons.
- **Segurança:** bcrypt, CSRF customizado, controle de sessão Flask.
- **Configuração:** python-dotenv e variáveis de ambiente.
- **Produção:** Gunicorn.
- **Testes:** pytest.

---

## 🗺 Páginas disponíveis

| Página / recurso | Rota | Acesso |
| --- | --- | --- |
| Login | `/` | Público |
| Logout | `/logout` | Usuário autenticado |
| Dashboard | `/dashboard` | Usuário autenticado |
| Nova ocorrência | `/nova-ocorrencia` | Usuário autenticado |
| Atualizar status | `/atualizar-status/<id>/<novo_status>` | Síndico |
| Cadastro de usuário | `/cadastro` | Síndico |
| Lista de usuários | `/usuarios` | Síndico |
| Saúde da aplicação | `/healthz` | Técnico/monitoramento |

---

## ⚙️ Como rodar o projeto

### 1. Pré-requisitos

- Python 3.8+
- PostgreSQL instalado

### 2. Configuração do ambiente

No terminal, dentro da pasta do projeto:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Ativar ambiente (Linux/macOS)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configuração do banco de dados

Crie um banco no PostgreSQL com o nome:

```text
conecta
```

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=postgres
DB_PASSWORD=SUA_SENHA_AQUI
DB_HOST=localhost
DB_PORT=5432
DB_NAME=conecta
SECRET_KEY=uma_chave_segura_aqui
```

### 4. Execução

```bash
# Criar usuário inicial/admin, se necessário
python criar_usuario.py

# Rodar o sistema
python run.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000/
```

### 5. Usuário padrão de desenvolvimento

```text
E-mail: admin@conectalar.com
Senha: 123
```

---

## 🧪 Testes

Dependências de desenvolvimento/testes:

```bash
pip install -r requirements-dev.txt
```

Executar a suíte automatizada:

```bash
pytest
```

---

## 📚 Documentação das Sprints 3 e 4

Para responder aos pontos de melhoria da avaliação da Sprint 3 e preparar a Sprint 4, foram criados documentos de apoio com:

- documentação de envio da Sprint 3;
- visão da estrutura modular do projeto;
- roteiro para comprovar persistência no banco;
- matriz de rastreabilidade entre funcionalidade, commit e evidência;
- plano operacional para evoluir o sistema na Sprint 4.

Documentos:

- [`docs/sprint_03_documentacao_entrega.md`](docs/sprint_03_documentacao_entrega.md)
- [`docs/sprint_04_finalizacao_evidencias.md`](docs/sprint_04_finalizacao_evidencias.md)
- [`docs/sprint_04_plano_execucao.md`](docs/sprint_04_plano_execucao.md)
- [`docs/sprint_04_execucao_realizada.md`](docs/sprint_04_execucao_realizada.md)

---

## 🔒 Variáveis de ambiente para produção

Para executar em produção com segurança:

- `APP_ENV=production`
- `SECRET_KEY=<chave forte obrigatória>`
- `DEBUG=false`
- `AUTO_CREATE_DB=false`

> Em `APP_ENV=production`, a aplicação não inicia sem `SECRET_KEY` definida.

---

## 📈 Próximas melhorias

- Filtro por data.
- Upload de anexos nas ocorrências.
- Comentários e histórico de movimentações.
- Dashboard com gráficos.
- Notificações.
- API REST.
- Gestão administrativa avançada de usuários.
- Suporte a múltiplos condomínios.

---

## 👥 Equipe

- Lorivan Lino de Abreu
- Rafael Fortunato Rodrigues De Aquino
- Stephanie Wolff Silva
- Vinicius Maciel Azevedo

---

## 📌 Observações

Este projeto foi desenvolvido com foco em aprendizado prático e aplicação real de conceitos de desenvolvimento web, evoluindo de um MVP para uma base sólida de sistema.
