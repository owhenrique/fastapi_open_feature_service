from http import HTTPStatus

from src.app.core.exceptions import CustomException


class FeatureFlagAlreadyExistsException(CustomException):
    code = HTTPStatus.BAD_REQUEST
    message = 'feature flag already exists'


class FeatureFlagNotFoundException(CustomException):
    code = HTTPStatus.NOT_FOUND
    message = 'feature flag not found'
