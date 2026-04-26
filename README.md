# 🏢 ConectaLar - Sistema de Gestão Condominial

Bem-vindo ao **ConectaLar**!  
Este projeto é um MVP (Produto Mínimo Viável) desenvolvido como atividade de extensão para a disciplina de Programação Web Aplicada da UniEvangélica.

O sistema tem como objetivo **digitalizar e centralizar o registro de ocorrências** dos moradores do **Condomínio Casas Flamboyant**, trazendo mais organização, transparência e eficiência na comunicação com a administração.

---

## 🚀 Funcionalidades

### 🔐 Autenticação
- Login de usuários
- Senhas criptografadas com **bcrypt**
- Controle de sessão

### 👥 Gestão de Usuários
- Cadastro de moradores (apenas síndico)
- Listagem de usuários
- Controle de acesso por perfil (síndico/morador)

### 📋 Ocorrências
- Registro de ocorrências
- Visualização em painel
- Controle de status:
  - Pendente
  - Em Andamento
  - Resolvido

### 📊 Dashboard
- Ordenação por prioridade de status
- Filtro por status
- Cards com contadores (KPIs)
- Interface responsiva com Bootstrap

---

## 🛠 Tecnologias Utilizadas

- **Back-end:** Python 3.x, Flask  
- **Banco de Dados:** PostgreSQL, SQLAlchemy  
- **Front-end:** HTML5, CSS3, Bootstrap 5  
- **Segurança:** Bcrypt (hash de senhas)

---

## ⚙️ Como rodar o projeto

### 1. Pré-requisitos
- Python 3.8+
- PostgreSQL instalado

---

### 2. Configuração do ambiente

No terminal, dentro da pasta do projeto:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
3. Configuração do banco de dados

Crie um banco no PostgreSQL com o nome:

conecta

Crie um arquivo .env na raiz do projeto:

DB_USER=postgres
DB_PASSWORD=SUA_SENHA_AQUI
DB_HOST=localhost
DB_PORT=5432
DB_NAME=conecta
SECRET_KEY=uma_chave_segura_aqui
4. Execução
# Rodar o sistema
python run.py

# Criar usuário inicial (admin)
python criar_usuario.py

Acesse no navegador:

http://127.0.0.1:5000/
🔐 Usuário padrão
Email: admin@conectalar.com
Senha: 123
📈 Próximas melhorias
Filtro por data
Busca por palavra-chave
Paginação
Dashboard com gráficos
Notificações
API REST
👥 Equipe
Lorivan Lino de Abreu
Rafael Fortunato Rodrigues De Aquino
Stephanie Wolff Silva
Vinicius Maciel Azevedo
📌 Observações

Este projeto foi desenvolvido com foco em aprendizado prático e aplicação real de conceitos de desenvolvimento web, evoluindo de um MVP para uma base sólida de sistema.
---

## 🔒 Variáveis de ambiente para produção

Para executar em produção com segurança:

- `APP_ENV=production`
- `SECRET_KEY=<chave forte obrigatória>`
- `DEBUG=false`
- `AUTO_CREATE_DB=false`

> Em `APP_ENV=production`, a aplicação não inicia sem `SECRET_KEY` definida.

## 🩺 Observabilidade e segurança (implementado)

- Endpoint de saúde: `GET /healthz`
- Proteção CSRF habilitada para requisições mutáveis (`POST`, etc.)
- Páginas de erro padronizadas para `400`, `403`, `404` e `500`
