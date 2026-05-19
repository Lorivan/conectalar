# Migrações (Flask-Migrate / Alembic)

## Inicializar
```bash
flask db init
```

## Criar migração inicial
```bash
flask db migrate -m "initial schema"
```

## Aplicar migrações
```bash
flask db upgrade
```

> A aplicação já está preparada com `Flask-Migrate` via `migrate.init_app(app, db)`.
