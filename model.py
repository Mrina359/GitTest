from pydantic import BaseModel,  ConfigDict

class Todo(BaseModel):
    model_config = ConfigDict(json_schema_extra={"example": {"id": 1, "item": "Example schema!"}})
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }

