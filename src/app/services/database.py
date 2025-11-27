from sqlmodel import Session, SQLModel, create_engine

from app.settings.database import DatabaseSettings

settings = DatabaseSettings()  # type: ignore

engine = create_engine(settings.DATABASE_FILE_URL, echo=True)

SQLModel.metadata.create_all(engine)

# flag = feature_flag.FeatureFlag(
#     description='hello world!',
#     operational_status=False,
#     created_at=datetime.now(),
#     updated_at=datetime.now()
# )
#
session = Session(engine)
#
# session.add(flag)
# session.commit()
