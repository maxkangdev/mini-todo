from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

from app.config.settings import db_settings


# Create the engine
engine = create_engine(db_settings.DATABASE_URL, echo=False)


def get_session():
    with Session(engine) as session:
        yield session


db_dependency = Annotated[Session, Depends(get_session)]
