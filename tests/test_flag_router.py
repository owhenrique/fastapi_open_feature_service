from http import HTTPStatus

from fastapi.testclient import TestClient

from app.api.feature_flags.domain.flag_model import Flag
from app.api.feature_flags.schemas.flag_schemas import FlagResponseSchema


def test_create_should_return_created_and_flag(client: TestClient):
    payload = {
        'name': 'test-flag-blue',
        'technical_key': 'tff001',
        'operational_status': 'off',
    }

    response = client.post('/feature-flags/', json=payload)

    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert 'id' in data


def test_create_should_return_bad_request_and_name_already_exists_exception(
    client: TestClient, flag: Flag
):
    payload = {
        'name': 'test-flag-red',
        'technical_key': 'tff001',
        'operational_status': 'off',
    }

    response = client.post('/feature-flags/', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'flag name already exists'}


def test_create_should_return_bad_request_and_t_k_already_exists_exception(
    client: TestClient, flag: Flag
):
    payload = {
        'name': 'test-flag-blue',
        'technical_key': 'tff00',
        'operational_status': 'off',
    }

    response = client.post('/feature-flags/', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'flag technical key already exists'}


def test_read_all_should_return_ok_and_flags_list(
    client: TestClient, flag: Flag
):
    flag_schema = FlagResponseSchema.model_validate(flag).model_dump(
        mode='json'
    )
    response = client.get('/feature-flags/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'flags': [flag_schema]}


def test_read_should_return_ok_and_flag(client: TestClient, flag: Flag):
    flag_schema = FlagResponseSchema.model_validate(flag).model_dump(
        mode='json'
    )
    response = client.get(f'/feature-flags/{flag.technical_key}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == flag_schema


def test_read_should_return_not_found(client: TestClient):
    response = client.get('/feature-flags/other-flag')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'flag not found'}


def test_update_should_return_ok_and_flag(client: TestClient, flag: Flag):
    payload = {
        'name': 'another-test-flag-red',
        'technical_key': 'another-tf00',
        'operational_status': 'on',
    }

    response = client.put(f'/feature-flags/{flag.technical_key}', json=payload)
    db_flag = response.json()

    flag_schema = FlagResponseSchema.model_validate(db_flag).model_dump(
        mode='json'
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == flag_schema
    assert flag.name == db_flag['name']


def test_update_should_return_not_found(client: TestClient):
    payload = {
        'name': 'another-test-flag-red',
        'technical_key': 'another-tf00',
        'operational_status': 'on',
    }
    response = client.put('/feature-flags/another-flag', json=payload)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'flag not found'}


def test_update_name_already_exists_should_return_bad_request(
    client, flag: Flag, another_flag: Flag
):
    payload = {
        'name': 'test-another-flag-red',
        'technical_key': 'tff00',
        'operational_status': 'on',
    }

    response = client.put(f'/feature-flags/{flag.technical_key}', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'flag name already exists'}


def test_update_technical_key_already_exists_should_return_bad_request(
    client, flag: Flag, another_flag: Flag
):
    payload = {
        'name': 'test-flag-red',
        'technical_key': 'another-tff00',
        'operational_status': 'on',
    }

    response = client.put(f'/feature-flags/{flag.technical_key}', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'flag technical key already exists'}


def test_delete_should_return_no_content(client: TestClient, flag: Flag):
    response = client.delete(f'/feature-flags/{flag.technical_key}')

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_should_return_not_found(client: TestClient):
    response = client.delete('/feature-flags/other-flag')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'flag not found'}
