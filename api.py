from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Todo API",
    description="CRUD-приложение FastAPI. Создано: Ишмухаметова М.Р.",
    version="1.0.0",
)

app.include_router(todo_router)