from app import db
from sqlalchemy import text


def test_app_factory_responde_healthcheck(client):
    response = client.get('/healthz')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}


def test_banco_em_teste_executa_consulta(app):
    with app.app_context():
        resultado = db.session.execute(text('SELECT 1')).scalar()

    assert resultado == 1
