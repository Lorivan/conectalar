from app.models import Usuario
from tests.conftest import csrf_token, login


def test_cadastro_usuario_valido_persiste_no_banco(client, app, sindico):
    login(client)

    response = client.post(
        '/cadastro',
        data={
            'nome': 'Maria Moradora',
            'email': 'maria@example.com',
            'senha': '123456',
            'unidade': 'Casa 22',
            'tipo': 'morador',
            '_csrf_token': csrf_token(client),
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    with app.app_context():
        usuario = Usuario.query.filter_by(email='maria@example.com').first()
        assert usuario is not None
        assert usuario.nome == 'Maria Moradora'
        assert usuario.tipo == 'morador'


def test_cadastro_usuario_invalido_nao_persiste(client, app, sindico):
    login(client)

    response = client.post(
        '/cadastro',
        data={
            'nome': 'A',
            'email': 'email-invalido',
            'senha': '123',
            'unidade': '',
            'tipo': 'admin',
            '_csrf_token': csrf_token(client),
        },
    )

    assert response.status_code == 400
    assert 'Informe um e-mail válido.'.encode() in response.data
    with app.app_context():
        assert Usuario.query.filter_by(email='email-invalido').first() is None
