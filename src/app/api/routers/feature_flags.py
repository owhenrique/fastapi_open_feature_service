from datetime import datetime
from http import HTTPStatus

from fastapi.routing import APIRouter
from sqlmodel import select

from app.api.schemas import FlagCreate, FlagRead, FlagsRead
from app.models.feature_flag import FeatureFlag
from app.services.database import session

router = APIRouter(prefix='/flags', tags=['Feature Flags'])


@router.post('/', response_model=FlagRead, status_code=HTTPStatus.OK)
def create_flag(req: FlagCreate):

    resource = FeatureFlag(
        description=req.description,
        operational_status=req.operational_status,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    session.add(resource)
    session.commit()

    return resource


@router.get('/', response_model=FlagsRead, status_code=HTTPStatus.OK)
def read_flags():
    resources = session.exec(select(FeatureFlag))

    print(resources)
    return {'flags': resources}
