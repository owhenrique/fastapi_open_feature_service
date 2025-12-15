from http import HTTPStatus

from fastapi import HTTPException
from fastapi.routing import APIRouter

from app.api.v1.feature_flags.deps.service_dependency import ServiceDep
from app.api.v1.feature_flags.exceptions.flag_exceptions import (
    FlagNameAlreadyExistsException,
    FlagNotFoundException,
    FlagTechnicalKeyAlreadyExistsException,
)
from app.api.v1.feature_flags.schemas.flag_schemas import (
    FlagCreateSchema,
    FlagResponseSchema,
    FlagsResponseSchema,
    FlagUpdateSchema,
)

router = APIRouter(prefix='/feature-flags', tags=['Feature Flags'])


@router.post(
    '/',
    response_model=FlagResponseSchema,
    status_code=HTTPStatus.CREATED,
)
def create_flag(flag: FlagCreateSchema, service: ServiceDep):
    try:
        return service.create(flag)
    except (
        FlagNameAlreadyExistsException,
        FlagTechnicalKeyAlreadyExistsException,
    ) as error:
        raise HTTPException(status_code=error.code, detail=error.message)


@router.get('/', response_model=FlagsResponseSchema, status_code=HTTPStatus.OK)
def read_flags(service: ServiceDep):
    flags = service.read_all()
    return {'flags': flags}


@router.get(
    '/{flag_technical_key}',
    response_model=FlagResponseSchema,
    status_code=HTTPStatus.OK,
)
def read_flag(flag_technical_key: str, service: ServiceDep):
    try:
        return service.read_one(flag_technical_key)
    except FlagNotFoundException as error:
        raise HTTPException(status_code=error.code, detail=error.message)


@router.put(
    '/{flag_technical_key}',
    response_model=FlagResponseSchema,
    status_code=HTTPStatus.OK,
)
def update_flag(
    flag_technical_key: str,
    flag: FlagUpdateSchema,
    service: ServiceDep,
):
    try:
        return service.update(flag_technical_key, flag)
    except (
        FlagNameAlreadyExistsException,
        FlagTechnicalKeyAlreadyExistsException,
        FlagNotFoundException,
    ) as error:
        raise HTTPException(status_code=error.code, detail=error.message)


@router.delete('/{flag_technical_key}', status_code=HTTPStatus.NO_CONTENT)
def delete_flag(flag_technical_key: str, service: ServiceDep):
    try:
        return service.delete(flag_technical_key)
    except FlagNotFoundException as error:
        raise HTTPException(status_code=error.code, detail=error.message)
