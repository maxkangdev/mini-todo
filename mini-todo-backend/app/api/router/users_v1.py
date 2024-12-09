from datetime import datetime

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlmodel import select
from starlette import status

from app.api.database import db_dependency
from app.api.models import User
from app.utils.password import hash_password

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    email: str
    created_at: datetime
    is_active: bool


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: db_dependency):
    statement = select(User).where(User.email == user.email)
    user_in_db = db.exec(statement).first()
    if user_in_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)  # Hash the password
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        username=user.username, email=user.email, created_at=new_user.created_at, is_active=new_user.is_active
    )


@router.get("/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int, db: db_dependency):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(username=user.username, email=user.email, created_at=user.created_at, is_active=user.is_active)


@router.get("/", response_model=UserResponse)
async def get_user(db: db_dependency, user_name: str = None, user_email: str = None):
    if user_name:
        statement = select(User).where(User.username == user_name)
    elif user_email:
        statement = select(User).where(User.email == user_email)
    else:
        raise HTTPException(status_code=400, detail="Provide either username or email")

    user = db.exec(statement).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(username=user.username, email=user.email, created_at=user.created_at, is_active=user.is_active)


@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db: db_dependency):
    user = db.get(User, user_id)

    if user:
        db.delete(user)
        db.commit()
    return UserResponse(username=user.username, email=user.email, created_at=user.created_at, is_active=user.is_active)
