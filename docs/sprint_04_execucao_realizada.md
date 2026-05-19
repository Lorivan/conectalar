# Sprint 4 — Execução realizada

## Entregas implementadas

### P0
- Validação de ocorrência: título mínimo de 3 caracteres e descrição mínima de 10 caracteres; bloqueio de persistência quando inválido.
- Validação de cadastro de usuário: nome, e-mail, senha, unidade e tipo válidos; bloqueio de persistência quando inválido.

### P1
- Tratamento de erros: remoção de `print`, uso de `logger.exception` e mensagens seguras ao usuário.
- Testes automatizados com cobertura de app factory, login, autorização, cadastro e ocorrência.
- Dashboard com busca textual (`q`) e paginação (`pagina`, 10 itens por página).

### P2
- Base para migrações criada com Flask-Migrate/Alembic e instruções de uso em `migrations/README.md`.
- Padronização de timezone: persistência em UTC no banco e formatação para BRT na camada de exibição.

## Melhorias visuais realizadas no painel
- Refatoração dos 4 cards de resumo do topo (`Todas`, `Pendentes`, `Em Andamento`, `Resolvidos`) com layout moderno em fundo branco, sombras suaves, maior respiro interno e ícones com tons pastel discretos por status.
- Reestilização da coluna **Título** na tabela de ocorrências para reforçar hierarquia visual: título principal com alto contraste e subtítulo/descrição com fonte menor e cor cinza clara.
- Atualização das badges de status para formato **pill**, com bordas totalmente arredondadas, fundo pastel e texto em tom mais escuro da mesma paleta para melhor legibilidade.
- Padronização da coluna **Ações (Administração)** com botões consistentes entre estados, incluindo estado finalizado com aparência de botão desabilitado (cinza claro).
- Ajuste do botão **Sair** da topbar para estilo **ghost** (fundo transparente, borda fina cinza, texto cinza e ícone discreto), reduzindo distração visual.

## Evidências de aceite
- `pytest` executa localmente com sucesso.
- Cadastros/ocorrências inválidos retornam HTTP 400 e não persistem.
- Dashboard mantém usabilidade com maior volume via busca e paginação.
