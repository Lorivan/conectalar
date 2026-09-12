# Relatório para o Grupo — Fase 1

## Avaliação e Melhoria da Qualidade do Sistema ConectaLar

**Disciplina:** Qualidade de Software

**Instituição parceira:** Condomínio Casas Flamboyant — Anápolis/GO

**Software avaliado:** ConectaLar

**Data:** 11 de setembro de 2026
**Versão:** 1.0

---

## 1. Mensagem principal para a equipe

Neste semestre, o ConectaLar não será apresentado apenas como um sistema a ser desenvolvido. O sistema já existente será o **objeto de avaliação** da disciplina. Portanto, nosso foco passa a ser identificar, medir, corrigir e validar aspectos da qualidade do software.

Em vez de perguntar somente **“qual funcionalidade vamos criar?”**, vamos trabalhar com a pergunta: **“o ConectaLar resolve a demanda do condomínio com qualidade, segurança, confiabilidade e facilidade de uso?”**

O título sugerido para o projeto é:

> **Avaliação e Melhoria da Qualidade do Sistema ConectaLar para Gestão de Demandas Condominiais**

## 2. O que já temos e podemos reaproveitar

O trabalho anterior fornece uma base importante para esta nova etapa:

- instituição parceira: Condomínio Casas Flamboyant;
- problema original: demandas de moradores registradas de maneira descentralizada, por conversas e mensagens não padronizadas;
- sistema ConectaLar já desenvolvido, com login, perfis, cadastro de usuários, ocorrências, dashboard, busca, paginação e persistência;
- arquitetura Flask com banco de dados e testes automatizados;
- histórico real de problemas e correções relacionados a autenticação, banco de dados, rotas, renderização, validações e integração entre frontend e backend;
- documentação e histórico de commits no Git.

Não devemos copiar o relatório antigo como se este semestre fosse mais uma fase de desenvolvimento. Ele será usado como **evidência histórica e ponto de partida** para avaliar o software atual.

## 3. O que muda neste semestre

| Antes — Programação Web | Agora — Qualidade de Software |
| --- | --- |
| Construir o sistema | Avaliar e melhorar o sistema existente |
| Requisitos funcionais e não funcionais | Requisitos de qualidade com métricas |
| Sprints de desenvolvimento | Sprints de diagnóstico, teste, correção e validação |
| Trello de tarefas de desenvolvimento | Kanban de atividades de qualidade |
| Git principalmente para código | Git para código, testes, documentação e evidências |
| MVP como produto final | Melhoria comprovada e validação da qualidade |

## 4. Cadeia de trabalho que será usada

Cada atividade deve seguir uma cadeia rastreável:

```text
Problema ou risco
        ↓
Requisito de qualidade
        ↓
Métrica ou critério mensurável
        ↓
Teste
        ↓
Resultado registrado
        ↓
Correção ou melhoria, quando necessária
        ↓
Nova validação
```

Exemplo: se o morador não conseguir finalizar o cadastro de uma ocorrência, registraremos a dificuldade como evidência de usabilidade, definiremos a melhoria necessária e repetiremos o teste após a correção.

## 5. Qualidades prioritárias do ConectaLar

| ID | Qualidade | Pergunta que precisamos responder | Como será avaliada inicialmente |
| --- | --- | --- | --- |
| RQ01 | Adequação funcional | Os fluxos críticos executam as regras esperadas? | Testes de cadastro, ocorrência e status. |
| RQ02 | Usabilidade | Um morador consegue registrar e localizar uma ocorrência sem impedimentos? | Roteiro de tarefa e registro de dificuldades. |
| RQ03 | Segurança | Cada perfil acessa somente o que pode acessar? | Testes de login, autorização e CSRF. |
| RQ04 | Confiabilidade | Dados válidos persistem e erros não deixam dados parciais? | Testes de integração, validação e rollback. |
| RQ05 | Desempenho | Dashboard e cadastro respondem dentro de um tempo aceitável? | Medições repetidas em ambiente declarado. |
| RQ06 | Manutenibilidade | O sistema pode ser testado e evoluído sem dificuldade excessiva? | Revisão de estrutura, testes e documentação. |

## 6. Pontos que exigem atenção

Os seguintes itens devem ser investigados na primeira sprint. Eles não significam que o software está “ruim”; são oportunidades concretas de avaliação e melhoria.

1. **Autenticação:** confirmar que login e verificação de senha continuam compatíveis após mudanças anteriores.
2. **Persistência:** confirmar que usuários e ocorrências são salvos, recuperados e relacionados corretamente.
3. **Atualização de status:** revisar a rota que altera status para garantir que uma mudança de estado use método HTTP apropriado e continue protegida.
4. **Migrações de banco:** verificar como mudanças futuras no esquema serão controladas.
5. **Desempenho:** medir o dashboard com dados fictícios; não apenas afirmar que é rápido.
6. **Privacidade:** não publicar senhas, tokens, dados pessoais ou dados reais do condomínio em documentos, prints ou repositório.

## 7. Plano inicial das quatro sprints

| Sprint | Objetivo | Entregas esperadas |
| --- | --- | --- |
| Sprint 1 — Diagnóstico | Estabelecer linha de base e priorizar problemas/riscos. | Resultado dos testes existentes, quadro Kanban inicial, roteiro de usabilidade e backlog priorizado. |
| Sprint 2 — Análise e correções | Investigar falhas prioritárias e implementar melhorias justificadas. | Cards atualizados, commits, testes novos ou ajustados e evidências de correção. |
| Sprint 3 — Validação e regressão | Verificar se as correções resolvem o problema sem criar novos defeitos. | Testes de regressão, resultado da avaliação de usabilidade e medições de desempenho. |
| Sprint 4 — Entrega final | Consolidar resultados, evidências e impactos. | Relatório final, matriz de rastreabilidade, evidências organizadas e validação final. |

## 8. Organização sugerida no Kanban

O quadro do grupo deve conter as colunas:

```text
Backlog de Qualidade → Sprint Atual → Em Análise/Teste → Correção/Melhoria → Validação → Concluído
```

Todo card deve registrar: título, origem (requisito/problema/risco), responsável, prioridade, sprint, critério de conclusão, checklist, commit e evidência.

Cards iniciais sugeridos:

- **Q-01:** executar a linha de base dos testes automatizados;
- **Q-02:** validar o fluxo de registro de ocorrência com a instituição ou registrar a limitação de acesso;
- **Q-03:** revisar a atualização de status e sua autorização;
- **Q-04:** preparar massa de dados fictícia e método de medição de desempenho;
- **Q-05:** revisar migrações e configuração de ambiente.

## 9. Decisões que o grupo precisa confirmar

Antes de avançar, precisamos confirmar ou preencher:

| Item | Ação necessária | Responsável |
| --- | --- | --- |
| Endereço e representante da instituição | Confirmar com o Condomínio Casas Flamboyant e decidir se os dados podem constar no relatório. | **[definir]** |
| Contato institucional | Registrar somente se houver autorização; evitar contato pessoal em repositório público. | **[definir]** |
| Participantes do teste de usabilidade | Definir participantes, roteiro e consentimento. | **[definir]** |
| Responsáveis pelas sprints | Distribuir cards do Kanban entre os integrantes. | **[definir]** |
| Critério de desempenho | Confirmar se a meta inicial de P95 até 2 segundos é adequada ao ambiente da disciplina. | **[definir]** |

## 10. Próximas ações imediatas

1. Compartilhar este relatório e realizar uma reunião curta de alinhamento do grupo.
2. Criar o Kanban de qualidade com os cinco cards iniciais.
3. Executar a suíte de testes atual e salvar o resultado como linha de base.
4. Confirmar dados da instituição sem expor informações pessoais indevidamente.
5. Iniciar a Sprint 1, registrando no Git cada documentação, teste, correção e evidência.

---

## Como enviar este relatório aos colegas pelo Google Docs

1. No repositório, abra este arquivo: `docs/relatorio_fase_01_para_grupo.md`.
2. Copie todo o conteúdo a partir do título **“Relatório para o Grupo — Fase 1”**.
3. Crie um documento em [Google Docs](https://docs.new) e cole o conteúdo.
4. Ajuste o título, inclua os nomes da equipe e preencha apenas os campos marcados como **[definir]** ou **[confirmar]** depois da validação.
5. No Google Docs, selecione **Compartilhar** e conceda acesso de **Editor** aos colegas do grupo.
6. Para envio formal, use **Arquivo → Fazer download → PDF** ou **Microsoft Word (.docx)**.

> O documento técnico completo que fundamenta este resumo está em `docs/fase_01_qualidade_software.md`. Ele deve permanecer versionado no Git; o Google Docs deve ser usado para colaboração e revisão pelo grupo.
