from fastapi.testclient import TestClient


def test_root_should_return_welcome_message(client: TestClient):
    response = client.get('/')

    assert response.json() == {
        'message': 'welcome to open feature service api v1'
    }


def test_healthcheck_should_return_ok_message(client: TestClient):
    response = client.get('/healthcheck')

    assert response.json() == {'status': 'ok'}
