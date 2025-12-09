from sqlmodel import Session

from app.api.feature_flags.domain.flag_model import Flag
from app.api.feature_flags.repositories.flag_repositorie import (
    FlagRepositorie,
)


def test_get_by_id_should_return_flag(session: Session, flag: Flag):
    db_flag = FlagRepositorie(session).get_by_id(flag.id)

    assert db_flag
    assert db_flag.name == flag.name
    assert db_flag.technical_key == flag.technical_key
    assert db_flag.operational_status == (flag.operational_status)
