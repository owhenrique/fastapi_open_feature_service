from typing import Annotated

from fastapi import Depends

from app.api.v1.feature_flags.repositories.flag_repository import (
    FlagRepository,
)

RepositoryDep = Annotated[FlagRepository, Depends()]
