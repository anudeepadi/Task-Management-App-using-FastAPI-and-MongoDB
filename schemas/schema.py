from pydantic import BaseModel
from typing import Optional


class TaskSchema(BaseModel):
    title: str
    is_completed: Optional[bool] = False

class TaskDeleteSchema(BaseModel):
    id: int

class TaskUpdateSchema(BaseModel):
    title: str
    is_completed: bool

class TaskDeleteAllSchema(BaseModel):
    id: int