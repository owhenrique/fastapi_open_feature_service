from typing import Annotated

from fastapi import Depends

from app.api.v1.feature_flags.services.flag_service import FlagService

ServiceDep = Annotated[FlagService, Depends()]
