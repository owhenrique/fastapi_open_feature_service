import uuid
from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app.api.feature_flags.domain.feature_flag_models import (
    FeatureFlag,
)
from src.app.api.feature_flags.schemas.feature_flag_schemas import (
    FeatureFlagResponseSchema,
)


def test_create_should_return_created_and_feature_flag(client: TestClient):
    payload = {
        'name': 'test-feature-flag-blue',
        'technical_key': 'tff001',
        'operational_status': 'off',
    }

    response = client.post('/feature-flags/', json=payload)

    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert 'id' in data


def test_create_should_return_bad_request_and_already_exists_exception(
    client: TestClient, feature_flag: FeatureFlag
):
    payload = {
        'name': 'test-feature-flag-red',
        'technical_key': 'tff001',
        'operational_status': 'off',
    }

    response = client.post('/feature-flags/', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'feature flag already exists'}


def test_read_all_should_return_ok_and_feature_flags_list(
    client: TestClient, feature_flag: FeatureFlag
):
    feature_flag_schema = FeatureFlagResponseSchema.model_validate(
        feature_flag
    ).model_dump(mode='json')
    response = client.get('/feature-flags/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'feature_flags': [feature_flag_schema]}


def test_read_should_return_ok_and_feature_flag(
    client: TestClient, feature_flag: FeatureFlag
):
    feature_flag_schema = FeatureFlagResponseSchema.model_validate(
        feature_flag
    ).model_dump(mode='json')
    response = client.get(f'/feature-flags/{feature_flag.id}')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == feature_flag_schema


def test_read_should_return_not_found(client: TestClient):
    random_uuid = uuid.uuid4()
    response = client.get(f'/feature-flags/{random_uuid}')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'feature flag not found'}


def test_update_should_return_ok_and_feature_flag(
    client: TestClient, feature_flag: FeatureFlag
):
    payload = {
        'name': 'another-test-feature-flag-red',
        'technical_key': 'another-tf00',
        'operational_status': 'on',
    }

    response = client.put(f'/feature-flags/{feature_flag.id}', json=payload)

    feature_flag_schema = FeatureFlagResponseSchema.model_validate(
        feature_flag
    ).model_dump(mode='json')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == feature_flag_schema
    data = response.json()
    assert data['name'] == 'another-test-feature-flag-red'


def test_update_should_return_not_found(client: TestClient):
    random_uuid = uuid.uuid4()
    payload = {
        'name': 'another-test-feature-flag-red',
        'technical_key': 'another-tf00',
        'operational_status': 'on',
    }
    response = client.put(f'/feature-flags/{random_uuid}', json=payload)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'feature flag not found'}


def test_update_name_already_exists_should_return_bad_request(
    client, feature_flag: FeatureFlag
):
    payload = {
        'name': 'test-feature-flag-red',
        'technical_key': 'another-tf00',
        'operational_status': 'on',
    }

    response = client.put(f'/feature-flags/{feature_flag.id}', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'feature flag already exists'}


def test_update_technical_key_already_exists_should_return_bad_request(
    client: TestClient, feature_flag: FeatureFlag
):
    payload = {
        'name': 'another-test-feature-flag-red',
        'technical_key': 'tff00',
        'operational_status': 'on',
    }

    response = client.put(f'/feature-flags/{feature_flag.id}', json=payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json() == {'detail': 'feature flag already exists'}


def test_delete_should_return_no_content(
    client: TestClient, feature_flag: FeatureFlag
):
    response = client.delete(f'/feature-flags/{feature_flag.id}')

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_delete_should_return_not_found(client: TestClient):
    random_uuid = uuid.uuid4()

    response = client.delete(f'/feature-flags/{random_uuid}')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'feature flag not found'}
