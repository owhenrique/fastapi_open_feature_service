from http import HTTPStatus

from fastapi import HTTPException
from fastapi.routing import APIRouter

from app.api.feature_flags.domain.feature_flag_exceptions import (
    FeatureFlagAlreadyExistsException,
)
from app.api.feature_flags.domain.feature_flag_schemas import (
    FeatureFlagCreateSchema,
    FeatureFlagResponseSchema,
    FeatureFlagsResponseSchema,
)
from app.api.feature_flags.feature_flag_services import FeatureFlagService
from app.core.database import DBSession

router = APIRouter(prefix='/feature-flags', tags=['Feature Flags'])


@router.post(
    '/', response_model=FeatureFlagResponseSchema, status_code=HTTPStatus.OK
)
async def create_flag(request: FeatureFlagCreateSchema, session: DBSession):
    try:
        return FeatureFlagService(session).create(request)
    except FeatureFlagAlreadyExistsException as e:
        raise HTTPException(status_code=e.code, detail=e.message)


@router.get(
    '/', response_model=FeatureFlagsResponseSchema, status_code=HTTPStatus.OK
)
def read_flags(session: DBSession):
    return FeatureFlagService(session).read_all()
