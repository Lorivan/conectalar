from tests.conftest import login


def test_login_valido_redireciona_para_dashboard(client, sindico):
    response = login(client)

    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']


def test_login_invalido_mostra_mensagem(client, sindico):
    response = login(client, senha='senha-errada')

    assert response.status_code == 200
    assert 'Email ou senha inválidos'.encode() in response.data


def test_dashboard_sem_sessao_redireciona_para_login(client):
    response = client.get('/dashboard')

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/')
