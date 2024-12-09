from datetime import datetime
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = Field(default=True)


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    completed: bool
    due_at: datetime | None = None

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = None

    user_id: int | None = Field(default=None, foreign_key="user.id")
