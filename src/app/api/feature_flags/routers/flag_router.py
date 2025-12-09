from http import HTTPStatus

from fastapi import HTTPException
from fastapi.routing import APIRouter

from app.api.feature_flags.exceptions.flag_exceptions import (
    FlagNameAlreadyExistsException,
    FlagNotFoundException,
    FlagTechnicalKeyAlreadyExistsException,
)
from app.api.feature_flags.schemas.flag_schemas import (
    FlagCreateSchema,
    FlagResponseSchema,
    FlagsResponseSchema,
    FlagUpdateSchema,
)
from app.api.feature_flags.services.flag_service import (
    FlagService,
)
from src.app.core.database import DBSession

router = APIRouter(prefix='/feature-flags', tags=['Feature Flags'])


@router.post(
    '/',
    response_model=FlagResponseSchema,
    status_code=HTTPStatus.CREATED,
)
def create_flag(flag: FlagCreateSchema, session: DBSession):
    try:
        return FlagService(session).create(flag)
    except (
        FlagNameAlreadyExistsException,
        FlagTechnicalKeyAlreadyExistsException,
    ) as error:
        raise HTTPException(status_code=error.code, detail=error.message)


@router.get('/', response_model=FlagsResponseSchema, status_code=HTTPStatus.OK)
def read_flags(session: DBSession):
    flags = FlagService(session).read_all()
    return {'flags': flags}


@router.get(
    '/{flag_technical_key}',
    response_model=FlagResponseSchema,
    status_code=HTTPStatus.OK,
)
def read_flag(flag_technical_key: str, session: DBSession):
    try:
        return FlagService(session).read_one(flag_technical_key)
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
    session: DBSession,
):
    try:
        return FlagService(session).update(flag_technical_key, flag)
    except (
        FlagNameAlreadyExistsException,
        FlagTechnicalKeyAlreadyExistsException,
        FlagNotFoundException,
    ) as error:
        raise HTTPException(status_code=error.code, detail=error.message)


@router.delete('/{flag_technical_key}', status_code=HTTPStatus.NO_CONTENT)
def delete_flag(flag_technical_key: str, session: DBSession):
    try:
        return FlagService(session).delete(flag_technical_key)
    except FlagNotFoundException as error:
        raise HTTPException(status_code=error.code, detail=error.message)
