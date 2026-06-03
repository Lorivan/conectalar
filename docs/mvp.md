# Documentação do MVP — ConectaLar

## 1. Produto Mínimo Viável desenvolvido

O **ConectaLar** é um MVP de sistema web para gestão condominial, criado para centralizar a comunicação entre moradores e administração do **Condomínio Casas Flamboyant**. A primeira versão prioriza o fluxo essencial do produto: autenticar usuários, registrar ocorrências do condomínio, acompanhar o andamento dessas solicitações e permitir que o síndico gerencie moradores e status dos chamados.

O MVP resolve o problema inicial de substituir controles manuais ou mensagens dispersas por um painel único, com dados persistidos em banco, regras básicas de acesso e uma interface responsiva para uso em navegador.

## 2. Funcionalidades entregues

### 2.1 Autenticação e sessão

- Tela de login na rota inicial (`/`).
- Validação de e-mail e senha cadastrados.
- Hash de senhas com `bcrypt`.
- Controle de sessão com identificação do usuário autenticado.
- Logout com limpeza da sessão.
- Redirecionamento para login quando o usuário tenta acessar páginas protegidas sem autenticação.

### 2.2 Controle de perfis

- Perfis de usuário: **síndico** e **morador**.
- Acesso restrito ao síndico para cadastro e listagem de moradores.
- Acesso restrito ao síndico para alteração de status das ocorrências.
- Bloqueio de ações administrativas para moradores, com resposta de acesso negado.

### 2.3 Gestão de moradores

- Cadastro de novos usuários/moradores pelo síndico.
- Campos principais: nome, e-mail, senha, unidade e tipo de usuário.
- Validação de dados obrigatórios, formato de e-mail, tamanho mínimo de senha e tipo de usuário permitido.
- Prevenção de cadastro duplicado por e-mail.
- Listagem de moradores cadastrados, ordenada por nome.

### 2.4 Registro e acompanhamento de ocorrências

- Cadastro de nova ocorrência por usuário autenticado.
- Campos principais: título e descrição.
- Associação da ocorrência ao usuário autor.
- Status inicial automático como **Pendente**.
- Atualização de status pelo síndico para:
  - **Pendente**;
  - **Em Andamento**;
  - **Resolvido**.
- Validação de título e descrição antes de persistir a ocorrência.

### 2.5 Dashboard operacional

- Painel principal de ocorrências na rota `/dashboard`.
- Cards com indicadores de quantidade por status.
- Total geral de ocorrências.
- Lista de ocorrências ordenada por prioridade de status e recência.
- Filtro por status.
- Busca textual por título ou descrição.
- Paginação com 10 ocorrências por página.
- Exibição de datas formatadas para o fuso de Brasília.

### 2.6 Segurança, validação e resiliência básica

- Proteção CSRF em requisições mutáveis.
- Páginas de erro padronizadas para `400`, `403`, `404` e `500`.
- Endpoint de saúde (`/healthz`) para verificar disponibilidade da aplicação e conexão com banco.
- Configurações por variáveis de ambiente.
- Exigência de `SECRET_KEY` em ambiente de produção.
- Tratamento de erros de banco com rollback em operações críticas.

## 3. Tecnologias utilizadas

### 3.1 Back-end

- **Python 3.x** como linguagem principal.
- **Flask** como framework web.
- **Flask Blueprints** para modularização por domínio:
  - autenticação;
  - dashboard;
  - ocorrências;
  - usuários.
- **SQLAlchemy / Flask-SQLAlchemy** para modelagem e acesso ao banco.
- **Flask-Migrate** opcional para migrações, quando disponível no ambiente.
- **python-dotenv** para carregamento de variáveis de ambiente.
- **Gunicorn** como servidor WSGI previsto para execução em produção.

### 3.2 Banco de dados

- **PostgreSQL** como banco-alvo da aplicação.
- **psycopg2-binary** como driver PostgreSQL.
- Modelo de dados com duas entidades principais:
  - `Usuario`;
  - `Ocorrencia`.

### 3.3 Front-end

- **HTML5** com templates **Jinja2**.
- **CSS3** customizado nos templates.
- **Bootstrap 5** para componentes visuais e responsividade.
- **Bootstrap Icons** para ícones da interface.

### 3.4 Segurança e qualidade

- **bcrypt** para hash e verificação de senhas.
- CSRF customizado com token de sessão.
- **pytest** para testes automatizados.

## 4. Páginas e rotas disponíveis

| Página / recurso | Rota | Método(s) | Acesso | Finalidade |
| --- | --- | --- | --- | --- |
| Login | `/` | `GET`, `POST` | Público | Autenticar usuário no sistema. |
| Logout | `/logout` | `GET` | Usuário autenticado | Encerrar sessão e retornar ao login. |
| Dashboard | `/dashboard` | `GET` | Usuário autenticado | Visualizar KPIs, filtros, busca, paginação e lista de ocorrências. |
| Nova ocorrência | `/nova-ocorrencia` | `GET`, `POST` | Usuário autenticado | Registrar uma nova ocorrência condominial. |
| Atualizar status | `/atualizar-status/<id>/<novo_status>` | `GET` | Síndico | Alterar o status de uma ocorrência existente. |
| Cadastro de usuário | `/cadastro` | `GET`, `POST` | Síndico | Cadastrar moradores ou usuários com perfil definido. |
| Lista de usuários | `/usuarios` | `GET` | Síndico | Consultar moradores/usuários cadastrados. |
| Saúde da aplicação | `/healthz` | `GET` | Técnico/monitoramento | Verificar se aplicação e banco respondem. |
| Páginas de erro | `400`, `403`, `404`, `500` | Conforme erro | Conforme contexto | Apresentar mensagens padronizadas de falha. |

## 5. Limitações do MVP

O MVP foi desenvolvido para validar o fluxo principal do produto e ainda não contempla todos os recursos esperados para uma solução condominial completa. As principais limitações são:

- Não há API REST pública para integração com aplicativos móveis ou sistemas externos.
- Não há anexos em ocorrências, como fotos, vídeos ou documentos.
- Não há notificações automáticas por e-mail, SMS, WhatsApp ou push.
- Não há histórico detalhado/auditoria de todas as mudanças realizadas em uma ocorrência.
- Não há comentários ou conversa dentro de cada ocorrência.
- Não há recuperação de senha automatizada para usuários finais.
- Não há tela administrativa avançada para edição, inativação ou exclusão de usuários.
- Não há dashboard com gráficos analíticos, tendências por período ou exportação de relatórios.
- Não há filtro por data implementado na interface principal.
- Não há suporte multi-condomínio; o MVP está direcionado ao contexto do Condomínio Casas Flamboyant.
- O cadastro inicial de administrador depende de script auxiliar e configuração manual do ambiente.
- A alteração de status usa rota `GET`; em uma evolução, deve ser migrada para `POST` ou `PATCH` com intenção explícita de mudança de estado.
- O sistema depende de configuração correta de variáveis de ambiente e banco PostgreSQL para execução fora do ambiente de testes.

## 6. Escopo recomendado para próximas evoluções

- Implementar recuperação de senha.
- Adicionar anexos às ocorrências.
- Criar histórico de movimentações por ocorrência.
- Adicionar comentários entre morador e administração.
- Implementar notificações automáticas.
- Criar filtros por data, unidade, morador e prioridade.
- Criar gráficos e relatórios exportáveis.
- Disponibilizar API REST autenticada.
- Melhorar a gestão administrativa de usuários.
- Evoluir o modelo para múltiplos condomínios.
