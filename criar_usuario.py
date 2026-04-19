from app import app, db
from app.models import Usuario
import bcrypt

with app.app_context():

    # Apaga usuário antigo (resolve seu erro de bcrypt)
    Usuario.query.filter_by(email="admin@conectalar.com").delete()
    db.session.commit()

    senha_plana = "123"

    hash_senha = bcrypt.hashpw(
        senha_plana.encode('utf-8'),
        bcrypt.gensalt()
    )

    novo_usuario = Usuario(
        nome="Síndico Leonardo",
        email="admin@conectalar.com",
        senha=hash_senha.decode('utf-8'),
        unidade="Administração",
        tipo="sindico"
    )

    db.session.add(novo_usuario)
    db.session.commit()

    print("Usuário recriado com senha criptografada!")