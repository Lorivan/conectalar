from app import app, db
from app.models import Usuario

with app.app_context():
    Usuario.query.delete()
    db.session.commit()
    print("Usuários apagados!")