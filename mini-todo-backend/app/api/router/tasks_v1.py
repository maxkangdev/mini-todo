from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel
from sqlmodel import select

from app.api.database import db_dependency
from app.api.deps import user_dependency
from app.api.models import Task

router = APIRouter()


class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False
    due_at: datetime | None = None


class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool = False
    due_at: datetime | None = None


@router.post("/")
async def create_task(current_user: user_dependency, db: db_dependency, task: TaskCreate):
    db_task = Task(**task.model_dump(), user_id=current_user.get("id"))
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get("/")
async def get_tasks(current_user: user_dependency, db: db_dependency):
    tasks = db.exec(select(Task).where(Task.user_id == current_user["id"])).all()
    return tasks


@router.delete("/{task_id}")
async def delete_task(current_user: user_dependency, db: db_dependency, task_id: int):
    db_task = db.get(Task, task_id)

    assert db_task.user_id == current_user["id"]
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task


@router.put("/{task_id}")
async def update_task(current_user: user_dependency, db: db_dependency, task_id: int, task: TaskUpdate):
    db_task = db.get(Task, task_id)
    assert db_task.user_id == current_user["id"]

    db_task.title = task.title
    db_task.description = task.description
    db_task.completed = task.completed
    db_task.due_at = task.due_at

    db.commit()
    db.refresh(db_task)
    return db_task
