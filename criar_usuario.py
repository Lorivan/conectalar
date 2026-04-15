from app import app, db
from app.models import Usuario

with app.app_context():
    # Verifica se já existe para não duplicar
    usuario_existente = Usuario.query.filter_by(email="admin@conectalar.com").first()

    if not usuario_existente:
        novo_usuario = Usuario(
            nome="Síndico Leonardo",
            email="admin@conectalar.com",
            senha="123",  # Para o MVP usaremos senha simples
            unidade="Administração",
            tipo="sindico"
        )
        db.session.add(novo_usuario)
        db.session.commit()
        print("Usuário 'admin@conectalar.com' criado com sucesso no banco!")
    else:
        print("O usuário já existe no banco de dados.")