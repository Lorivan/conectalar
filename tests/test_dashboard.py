from tests.conftest import csrf_token, login


def _criar_ocorrencias(client, quantidade):
    for idx in range(quantidade):
        client.post(
            '/nova-ocorrencia',
            data={
                'titulo': f'Problema {idx}',
                'descricao': f'Descricao detalhada do problema {idx} para teste de paginacao.',
                '_csrf_token': csrf_token(client),
            },
            follow_redirects=False,
        )


def test_dashboard_filtra_por_texto(client, sindico):
    login(client)
    _criar_ocorrencias(client, 3)

    response = client.get('/dashboard?q=Problema+1')

    assert response.status_code == 200
    assert b'Problema 1' in response.data
    assert b'Problema 2' not in response.data


def test_dashboard_paginacao(client, sindico):
    login(client)
    _criar_ocorrencias(client, 12)

    r1 = client.get('/dashboard?pagina=1')
    r2 = client.get('/dashboard?pagina=2')

    assert r1.status_code == 200
    assert r2.status_code == 200
    assert b'Problema 11' in r1.data
    assert b'Problema 1' in r2.data
