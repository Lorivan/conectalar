# 🏢 ConectaLar - Sistema de Gestão Condominial

Bem-vindo ao repositório do **ConectaLar**! Este é um MVP (Produto Mínimo Viável) desenvolvido como projeto de extensão para a disciplina de Programação Web Aplicada da UniEvangélica.

O sistema digitaliza e centraliza o registro de ocorrências e reclamações dos moradores do **Condomínio Casas Flamboyant**.

## 🛠 Tecnologias Utilizadas
* **Back-end:** Python 3.x, Flask
* **Banco de Dados:** PostgreSQL, SQLAlchemy
* **Front-end:** HTML5, CSS3, Bootstrap 5

## ⚙️ Como rodar o projeto na sua máquina (Para Devs)

### 1. Pré-requisitos
* Python 3.8+ instalado.
* PostgreSQL instalado.

### 2. Configuração do Ambiente
Abra o terminal na pasta do projeto e execute:
```bash
# Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instalar bibliotecas
pip install -r requirements.txt
3. Banco de Dados
Crie um banco no PostgreSQL chamado conecta.

Crie um ficheiro .env na raiz com:

Snippet de código
DB_USER=postgres
DB_PASSWORD=SUA_SENHA_AQUI
DB_HOST=localhost
DB_PORT=5432
DB_NAME=conecta
SECRET_KEY=conectalar
4. Execução
Bash
# Rodar o sistema
python run.py

# Criar usuário inicial (Admin)
python criar_usuario.py
Acesse: http://127.0.0.1:5000/

👥 Equipe
Lorivan Lino de Abreu

Rafael Fortunato Rodrigues De Aquino

Stephanie Wolff Silva

Vinicius Maciel Azevedo


3. Guarda o ficheiro (**Ctrl + S**).
4. No terminal do PyCharm, envia a atualização para o GitHub:
```bash
git add README.md
git commit -m "Doc: Adicionando instruções de instalação"
git push origin main