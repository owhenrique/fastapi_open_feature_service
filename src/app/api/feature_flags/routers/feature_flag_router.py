from http import HTTPStatus
from uuid import UUID

from fastapi import HTTPException
from fastapi.routing import APIRouter

from src.app.api.feature_flags.exceptions.feature_flag_exceptions import (
    FeatureFlagAlreadyExistsException,
    FeatureFlagNotFoundException,
)
from src.app.api.feature_flags.schemas.feature_flag_schemas import (
    FeatureFlagCreateSchema,
    FeatureFlagResponseSchema,
    FeatureFlagsResponseSchema,
)
from src.app.api.feature_flags.services.feature_flag_services import (
    FeatureFlagService,
)
from src.app.core.database import DBSession

router = APIRouter(prefix='/feature-flags', tags=['Feature Flags'])


@router.post(
    '/', response_model=FeatureFlagResponseSchema, status_code=HTTPStatus.OK
)
async def create_flag(request: FeatureFlagCreateSchema, session: DBSession):
    try:
        return FeatureFlagService(session).create(request)
    except FeatureFlagAlreadyExistsException as error:
        raise HTTPException(status_code=error.code, detail=error.message)


@router.get(
    '/', response_model=FeatureFlagsResponseSchema, status_code=HTTPStatus.OK
)
def read_flags(session: DBSession):
    return FeatureFlagService(session).read_all()


@router.get(
    '/{feature_flag_id}',
    response_model=FeatureFlagResponseSchema,
    status_code=HTTPStatus.OK,
)
def read_flag(feature_flag_id: UUID, session: DBSession):
    try:
        return FeatureFlagService(session).read_one(feature_flag_id)
    except FeatureFlagNotFoundException as error:
        raise HTTPException(status_code=error.code, detail=error.message)
