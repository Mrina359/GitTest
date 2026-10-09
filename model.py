from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "A task from Marina"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Updated task from Marina"
            }
        }


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Example 1 from Marina!"},
                    {"item": "Example 2 from Marina!"}
                ]
            }
        }