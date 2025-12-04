from fastapi.testclient import TestClient

from src.app.main import app


def test_healthcheck_should_return_ok_message():
    client = TestClient(app)

    response = client.get('/healthcheck')

    assert response.json() == {'status': 'ok'}
