from sqlmodel import Session, create_engine

from app.settings.database import DatabaseSettings

settings = DatabaseSettings()  # type: ignore

engine = create_engine(settings.DATABASE_FILE_URL)


async def get_session():
    with Session(engine) as session:
        yield session
