from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.database import engine
from sqlmodel import SQLModel

from app.api.router.tasks_v1 import router as tasks_v1
from app.api.router.users_v1 import router as users_v1
from app.api.router.auth_v1 import router as auth_v1
from app.config.settings import db_settings, auth_settings

app = FastAPI()
SQLModel.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
def ping():
    return "pong"


@app.get("/settings")
def settings():
    return db_settings, auth_settings


app.include_router(tasks_v1, prefix="/api/v1/tasks", tags=["Todos"])
app.include_router(users_v1, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth_v1, prefix="", tags=["Auth"])
