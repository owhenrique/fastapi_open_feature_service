from datetime import datetime
from http import HTTPStatus

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlmodel import Session, select

from app.api.schemas import (
    FeatureFlagCreateSchema,
    FeatureFlagResponseSchema,
    FeatureFlagsResponseSchema,
)
from app.models.feature_flag import FeatureFlag
from app.services.database import get_session

router = APIRouter(prefix='/flags', tags=['Feature Flags'])


@router.post(
    '/', response_model=FeatureFlagResponseSchema, status_code=HTTPStatus.OK
)
def create_flag(
    req: FeatureFlagCreateSchema, session: Session = Depends(get_session)
):

    statement = FeatureFlag(
        description=req.description,
        operational_status=req.operational_status,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    session.add(statement)
    session.commit()
    session.refresh(statement)

    return statement


@router.get(
    '/', response_model=FeatureFlagsResponseSchema, status_code=HTTPStatus.OK
)
def read_flags(session: Session = Depends(get_session)):
    statement = session.exec(select(FeatureFlag))

    return {'flags': statement}
