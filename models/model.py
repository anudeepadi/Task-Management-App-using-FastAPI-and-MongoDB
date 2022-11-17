from pydantic import BaseModel
from typing import Optional

class TaskModel(BaseModel):
    title: str
    is_completed: Optional[bool] = False

class CreateTaskModel(BaseModel):
    title: str

class UpdateTaskModel(BaseModel):
    title: str
    is_completed: bool

class DeleteTaskModel(BaseModel):
    id: int