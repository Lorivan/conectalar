# Evidências Sprint 4

Use esta pasta para armazenar os prints e registros técnicos coletados na finalização da Sprint 4.

## Identificação da coleta

- **Data da coleta:** preencher na entrega
- **Ambiente usado:** local / homologação / produção assistida
- **Banco usado:** PostgreSQL ou URL/instância configurada
- **Commit da entrega:** preencher após o commit final
- **Responsável pela coleta:** preencher na entrega

## Evidências esperadas

| Arquivo | O que comprova | Status |
| --- | --- | --- |
| `01-login.png` | Tela inicial de autenticação | Pendente |
| `02-dashboard-inicial.png` | Acesso autenticado ao dashboard | Pendente |
| `03-cadastro-usuario.png` | Cadastro persistido de usuário | Pendente |
| `04-nova-ocorrencia.png` | Criação persistida de ocorrência | Pendente |
| `05-status-atualizado.png` | Atualização persistida do status da ocorrência | Pendente |
| `06-consulta-banco.png` | Consulta SQL comprovando persistência em `usuarios` e `ocorrencias` | Pendente |
| `07-healthcheck.png` | Saúde da aplicação e conexão com banco | Pendente |

## Consultas recomendadas para o print do banco

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
