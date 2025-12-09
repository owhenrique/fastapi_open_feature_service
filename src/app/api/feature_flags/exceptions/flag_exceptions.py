from http import HTTPStatus

from src.app.core.exceptions import CustomException


class FlagNameAlreadyExistsException(CustomException):
    code = HTTPStatus.BAD_REQUEST
    message = 'flag name already exists'


class FlagTechnicalKeyAlreadyExistsException(CustomException):
    code = HTTPStatus.BAD_REQUEST
    message = 'flag technical key already exists'


class FlagNotFoundException(CustomException):
    code = HTTPStatus.NOT_FOUND
    message = 'flag not found'
