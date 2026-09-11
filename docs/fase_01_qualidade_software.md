# Fase 1 — Planejamento da Avaliação e Melhoria da Qualidade

**Projeto extensionista:** Avaliação e Melhoria da Qualidade do Sistema ConectaLar para Gestão de Demandas Condominiais

**Software avaliado:** ConectaLar

**Situação deste documento:** planejamento inicial; as informações institucionais marcadas como **[confirmar]** dependem de validação com a instituição parceira.
**Versão:** 0.1 — 11/09/2026

## 1. Controle de versões

| Versão | Data | Descrição | Evidência |
| --- | --- | --- | --- |
| 0.1 | 11/09/2026 | Estruturação do diagnóstico, requisitos, métricas, riscos, plano de garantia e sprints iniciais. | Este documento versionado no Git. |

## 2. Instituição parceira e projeto

### 2.1 Identificação da instituição

| Campo | Informação |
| --- | --- |
| Instituição parceira | Condomínio Casas Flamboyant |
| Município | Anápolis — GO |
| Endereço | **[confirmar com a instituição; não registrar dados pessoais desnecessários]** |
| Representante | **[confirmar]** |
| Cargo | **[confirmar]** |
| Contato institucional | **[confirmar; manter fora de repositório público se for dado pessoal]** |

O condomínio representa o contexto de uso do ConectaLar: moradores registram demandas e a administração as acompanha e trata. A finalidade do projeto neste semestre não é reiniciar o desenvolvimento do produto, mas avaliar de forma rastreável se a versão existente oferece qualidade suficiente para esse fluxo e realizar melhorias justificadas por evidências.

### 2.2 Caracterização contextualizada

O público direto é formado por moradores e pela administração/síndico. O serviço apoiado pelo sistema é o registro, acompanhamento e atualização de reclamações, solicitações e comentários relativos ao condomínio. Antes do ConectaLar, a comunicação era descentralizada, com conversas e mensagens em canais como WhatsApp e registros não padronizados. A instituição se relaciona ao projeto como beneficiária e fonte de validação do fluxo real de gestão de demandas.

### 2.3 Objetivo geral

Aumentar a confiança no uso do ConectaLar por meio de um ciclo de diagnóstico, testes, correções e revalidação de qualidades prioritárias: adequação funcional, usabilidade, confiabilidade, segurança, desempenho e manutenibilidade.

### 2.4 Objetivos específicos

1. Caracterizar a versão atual do software e seu ambiente de avaliação.
2. Definir requisitos de qualidade mensuráveis e testes associados.
3. Confirmar, com evidências reproduzíveis, os fluxos de autenticação, autorização, persistência e consulta de ocorrências.
4. Registrar problemas já observados e riscos futuros, priorizando-os por impacto e probabilidade.
5. Corrigir itens priorizados e executar testes de regressão antes da entrega final.

## 3. Caracterização do software avaliado

O **ConectaLar** é um sistema web MVP para centralizar a gestão de ocorrências condominiais. Ele permite autenticação, diferenciação entre os perfis `síndico` e `morador`, cadastro de usuários por síndico, abertura de ocorrências por usuários autenticados, atualização de status pelo síndico e consulta das ocorrências em dashboard com busca, filtro e paginação.

| Aspecto | Caracterização atual |
| --- | --- |
| Tecnologias | Python, Flask, SQLAlchemy, PostgreSQL como banco-alvo, Jinja2, Bootstrap e pytest. |
| Arquitetura | App factory, blueprints por domínio, modelos relacionais, serviços e utilitários. |
| Dados principais | Usuários e ocorrências, relacionados pelo autor da ocorrência. |
| Segurança existente | Hash de senha, sessão, autorização por perfil, CSRF em requisições mutáveis e `SECRET_KEY` obrigatória em produção. |
| Evidência automatizada atual | Suíte pytest com 18 cenários coletados na linha de base desta fase. |
| Limites conhecidos | Não há anexos, notificações, comentários, histórico de auditoria, recuperação de senha, API pública nem suporte multi-condomínio. |

**Linha de base:** a caracterização é uma fotografia inicial, não uma declaração de que o software está livre de defeitos. O resultado dos testes e da revisão nas próximas sprints definirá o estado efetivamente validado.

## 4. Diagnóstico inicial da qualidade

O problema de negócio original — registros dispersos e sem padronização — justifica a existência do sistema. Na disciplina atual, a pergunta de avaliação passa a ser: **o ConectaLar registra, protege, recupera e apresenta essas demandas com qualidade suficiente para o uso proposto?**

Há indícios positivos já implementados: testes de autenticação, autorização, persistência, validações, busca, paginação, CSRF e healthcheck. Também existe histórico de dificuldades de autenticação, integridade/persistência, renderização, imports, app factory, blueprints e integração entre frontend, backend e banco. Esse histórico será usado como fonte de hipóteses de teste, nunca como prova de que uma falha ainda existe.

## 5. Requisitos de qualidade e métricas

| ID | Requisito de qualidade | Métrica/critérios mensuráveis | Método de verificação | Resultado esperado |
| --- | --- | --- | --- | --- |
| RQ01 | **Adequação funcional:** o sistema deve executar os fluxos críticos conforme suas regras. | Proporção de cenários críticos aprovados; ocorrência inicia como `Pendente`; só status permitidos são aceitos. | T02, T03 e T04. | 100% dos cenários críticos planejados aprovados. |
| RQ02 | **Usabilidade:** usuário deve conseguir registrar uma ocorrência sem impedimento. | Taxa de conclusão; número de impedimentos; mensagens de erro compreensíveis. | T01 com roteiro de tarefa e registro de observações. | Ao menos 90% das tarefas concluídas sem ajuda; nenhum impedimento bloqueante aberto. |
| RQ03 | **Segurança:** ações e dados administrativos devem respeitar autenticação, autorização e integridade da requisição. | Rotas protegidas bloqueiam acesso sem sessão; morador não altera status nem gerencia usuários; POST sem CSRF é rejeitado. | T03 e testes de regressão. | 100% das tentativas não autorizadas bloqueadas. |
| RQ04 | **Confiabilidade:** operações válidas devem persistir e dados inválidos/falhas não devem deixar estado parcial. | Registro válido recuperável; inválido não persistido; rollback confirmado em falha simulada. | T02 e T04. | 100% dos cenários de persistência aprovados. |
| RQ05 | **Desempenho:** consultas usuais devem responder adequadamente no ambiente de avaliação. | Tempo de resposta de dashboard e abertura de ocorrência, medido em pelo menos 10 repetições por cenário. | T05 com dados fictícios documentados. | Percentil 95 até 2 s no ambiente de teste; resultados comparáveis e registrados. |
| RQ06 | **Manutenibilidade:** alterações e testes devem ser localizáveis e executáveis. | Suíte executa em comando único; responsabilidades críticas estão separadas; documentação de execução atualizada. | T06, revisão de estrutura e Git. | Suíte aprovada e documentação reproduzível. |

> As metas de RQ02 e RQ05 são critérios iniciais de avaliação. Caso a instituição, a turma ou o ambiente imponham condições diferentes, a alteração deverá ser registrada com justificativa e versão.

## 6. Problemas e riscos de qualidade

### 6.1 Problemas observados historicamente ou confirmados na linha de base

| ID | Tipo | Descrição e origem | Impacto | Situação nesta fase | Prioridade |
| --- | --- | --- | --- | --- | --- |
| PQ01 | Histórico | Incompatibilidades de autenticação após mudança de mecanismo de hash foram relatadas em evoluções anteriores. | Usuário pode não acessar o sistema. | Revalidar por T03; não assumir recorrência. | Alta |
| PQ02 | Histórico | Problemas de persistência/integridade e de carregamento de variáveis em rotas foram tratados em sprints anteriores. | Registro pode não ser criado ou exibido corretamente. | Revalidar por T02 e T04. | Alta |
| PQ03 | Confirmado por revisão documental | A alteração de status é exposta por rota `GET`, embora modifique estado. | Uma navegação/acesso indevido pode disparar mudança de estado. | Investigar e corrigir se confirmado no código vigente. | Alta |

### 6.2 Riscos futuros

| ID | Risco | Probabilidade | Impacto | Prioridade | Tratamento planejado |
| --- | --- | --- | --- | --- |
| RS01 | Evoluções de modelo de banco gerarem incompatibilidades sem migrações versionadas aplicadas. | Média | Alto | Alta | Validar estratégia de migração e registrar procedimento de atualização. |
| RS02 | Crescimento de ocorrências degradar consultas e paginação. | Média | Médio | Média | Medir T05 com massa de dados fictícia e registrar limite do ambiente. |
| RS03 | Configuração incorreta de segredos ou ambiente reduzir segurança operacional. | Baixa/Média | Alto | Alta | Revisar variáveis de ambiente, não versionar segredos e testar configuração de produção. |
| RS04 | Regressões em regras de acesso após mudanças futuras. | Média | Alto | Alta | Manter testes automatizados de autenticação/autorização na regressão. |
| RS05 | Evidências com dados pessoais ou credenciais serem expostas. | Média | Alto | Alta | Usar dados fictícios, ocultar informações e revisar anexos antes de publicar. |

## 7. Plano de Garantia da Qualidade

### 7.1 Escopo

Serão avaliados os fluxos de login, autorização por perfil, cadastro de usuário, abertura de ocorrência, atualização de status, persistência, dashboard e configuração básica da aplicação. Ficam fora do escopo desta fase os recursos que o MVP não implementa, como anexos, notificações, API pública e multi-condomínio, exceto quando constituírem risco documentado.

### 7.2 Estratégias

- **Teste automatizado:** proteger regras críticas e regressões em nível de rota, serviço e banco de testes.
- **Teste manual de usabilidade:** observar tarefa roteirizada de criação e consulta de ocorrência, com consentimento e sem dados pessoais no relatório.
- **Revisão de código/configuração:** verificar autorização, mutações HTTP, variáveis de ambiente, tratamento de erros e documentação.
- **Teste de desempenho controlado:** medir rotas críticas em ambiente declarado, com massa fictícia e método repetível.
- **Rastreabilidade:** cada card, teste, defeito e correção indicará RQ/MQ/PQ/RS relacionado, commit e evidência.

### 7.3 Plano de testes inicial

| ID | Relacionado | Tipo | Objetivo e escopo | Resultado esperado |
| --- | --- | --- | --- | --- |
| T01 | RQ02 | Usabilidade manual | Usuário executa login, cria ocorrência e localiza-a no dashboard. | Conclusão conforme meta de MQ02; dificuldades registradas. |
| T02 | RQ01, RQ04, PQ02 | Integração/persistência | Criar usuário e ocorrência válidos; consultar estado e relação autor-ocorrência. | Dados persistidos e recuperáveis; status inicial correto. |
| T03 | RQ03, PQ01, RS04 | Segurança/autorizações | Testar login válido/inválido, acesso sem sessão, ações de morador e CSRF. | Acesso indevido bloqueado; fluxo autorizado preservado. |
| T04 | RQ01, RQ04 | Validação e regressão | Submeter dados inválidos e simular falha de persistência. | HTTP/feedback adequado; nenhum dado inválido ou parcial persistido. |
| T05 | RQ05, RS02 | Desempenho | Medir dashboard e criação de ocorrência com massa fictícia declarada. | P95 dentro do critério ou gargalo documentado e priorizado. |
| T06 | RQ06, RS01, RS03 | Revisão técnica | Revisar estrutura, dependências, configuração, migrações e instruções de execução. | Achados registrados, priorizados e com decisão de tratamento. |

### 7.4 Ferramentas e tecnologias

| Finalidade | Ferramenta/recurso |
| --- | --- |
| Código, documentação e rastreabilidade | Git e repositório do projeto |
| Testes automatizados | Python e pytest |
| Aplicação de teste | Flask test client / execução local controlada |
| Banco de teste | SQLite em memória para suíte; PostgreSQL quando for necessária evidência de ambiente-alvo |
| Avaliação manual | Navegador e roteiro de tarefa |
| Medição | Script/comando versionado a ser definido na Sprint 1; registrar máquina, banco, massa de dados e repetições |
| Gestão visual | Quadro Kanban de qualidade (Trello ou equivalente) |

## 8. Ambiente e recursos de avaliação

O ambiente automatizado atual define `APP_ENV=testing`, `DATABASE_URL=sqlite:///:memory:`, `AUTO_CREATE_DB=true` e uma chave de teste, isolando a suíte de dados reais. O ambiente alvo utiliza PostgreSQL configurado por variáveis de ambiente. Evidências externas devem usar contas e registros fictícios; senhas, tokens, URLs privadas, endereço detalhado e contato pessoal não devem ser adicionados ao Git.

**Limitações conhecidas:** os resultados de desempenho em máquina local não representam, por si só, a capacidade de produção; a validação com a instituição depende de disponibilidade do representante e não deve ser simulada como observação real.

## 9. Kanban e backlog de qualidade

O quadro adotará as colunas **Backlog de Qualidade → Sprint Atual → Em Análise/Teste → Correção/Melhoria → Validação → Concluído**. Cada card deverá conter título, origem (RQ/MQ/PQ/RS), descrição, responsável, prioridade, sprint, critério de conclusão, checklist, link de commit e link/arquivo de evidência.

Backlog inicial:

| Card | Origem | Prioridade | Critério de conclusão |
| --- | --- | --- | --- |
| Q-01 — Executar linha de base de testes | RQ01/RQ03/RQ04 | Alta | Saída do pytest e versão do ambiente registradas. |
| Q-02 — Validar fluxo de ocorrência com instituição | RQ02 | Alta | Roteiro aplicado ou limitação formalmente registrada. |
| Q-03 — Revisar rota de atualização de status | PQ03/RQ03 | Alta | Decisão técnica registrada; se corrigida, teste de regressão aprovado. |
| Q-04 — Planejar massa e medição de desempenho | RQ05/RS02 | Média | Método, dados fictícios e critério documentados. |
| Q-05 — Revisar migrações e configuração | RQ06/RS01/RS03 | Alta | Achados, decisão e evidência registrados. |

Capturas do quadro deverão ser feitas no estado inicial e após cada uma das quatro sprints, sem expor dados pessoais.

## 10. Plano inicial das quatro sprints

| Sprint | Foco | Entregáveis/evidências | Critério de encerramento |
| --- | --- | --- | --- |
| 1 — Diagnóstico e linha de base | Confirmar caracterização, executar testes existentes, preparar roteiro de usabilidade, revisar PQ/RS. | Resultado da suíte, inventário de testes, quadro inicial, achados priorizados. | Diagnóstico rastreável aprovado pela equipe; backlog repriorizado. |
| 2 — Análise e correções | Investigar falhas priorizadas, especialmente mutação de status, configuração e persistência; implementar correções justificadas. | Cards, commits, testes novos/atualizados e evidência de correção. | Itens de maior prioridade validados ou justificados como pendentes. |
| 3 — Validação e regressão | Executar regressão, usabilidade e medição de desempenho; tratar efeitos colaterais. | Relatório de resultados, medições, feedback anonimizado e quadro atualizado. | Critérios mensuráveis avaliados e regressões críticas ausentes. |
| 4 — Avaliação final e entrega | Consolidar evidências, reexecutar fluxos críticos, diferenciar resultados técnicos de impacto institucional. | Relatório final, matriz de rastreabilidade, evidências organizadas e versão final no Git. | Entrega reproduzível, limitações declaradas e validação final registrada. |

## 11. Resultados, impacto e reflexão — critérios para a entrega final

A entrega final deverá separar claramente:

- **Resultado técnico observado:** por exemplo, teste de autorização aprovado, defeito corrigido ou tempo medido.
- **Impacto institucional observado:** mudança confirmada no processo de gestão pela instituição, quando houver evidência.
- **Impacto potencial:** redução esperada de perda de solicitações, centralização e maior transparência; deve ser identificado como potencial enquanto não houver observação suficiente.

Assim, a qualidade será demonstrada pela cadeia **requisito → métrica → teste → resultado → correção → nova validação**, e não apenas pela alegação de que o software está pronto.

## 12. Próximos passos imediatos

1. Confirmar os campos institucionais marcados como pendentes, respeitando privacidade.
2. Registrar a versão de ambiente e executar a linha de base com `pytest`.
3. Criar o quadro Kanban de qualidade e cadastrar os cards Q-01 a Q-05.
4. Definir responsável, participantes e consentimento para T01.
5. Abrir a Sprint 1 e registrar toda alteração em Git, com teste e evidência associados.
