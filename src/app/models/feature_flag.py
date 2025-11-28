from datetime import datetime

from sqlmodel import Field, SQLModel

from app.services.database import engine


class FeatureFlag(SQLModel, table=True):
    """
    Represents a flag to a feature in the aplication.

    Args:
        SQLModel: SQLModel is a library for interacting with SQL databases
        from Python code, with Python objects.
        table (bool, optional): This tells to SQLModel that this object is
        an relation (table). Defaults to True.

    Atributtes:
        id: Primary key
        description: A brief description to identify the feature
        operational_status: A boolean to tell if the feature is online
        created_at: Marks when FeatureFlag instance was created on the system
        updated_at: Marks when FeatureFlag instance was updated on the system
    """

    id: int | None = Field(default=None, primary_key=True)
    description: str
    operational_status: bool
    created_at: datetime
    updated_at: datetime


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
