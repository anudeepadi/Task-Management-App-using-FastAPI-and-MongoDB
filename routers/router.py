from fastapi import APIRouter, Response, status
from fastapi.security import OAuth2PasswordBearer
from schemas.schema import TaskSchema, TaskDeleteSchema
from database.db import get_task, get_tasks, create_task, update_complete, delete_task, delete_all, add_multiple
from models.model import TaskModel, CreateTaskModel, UpdateTaskModel, DeleteTaskModel
from typing import List

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/", status_code=201)
async def create_new_task(task: CreateTaskModel):
    return create_task(task)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_tasks():
    return get_tasks()


@router.get("/{id}", status_code=200)
async def get_task_by_id(id: int):
    if get_task(id) == None:
        return {"error": "There is no task with that id"}
    return get_task(id)


@router.delete("/{id}", status_code=204)
async def delete_task_by_id(id):
    return delete_task(id)


@router.put("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_task_by_id(id: int, task: UpdateTaskModel, response: Response):
    if get_task(id) == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "There is no task with that id"}
    return update_complete(id, task.title, task.is_completed)

@router.post("/add_multiple_tasks", status_code=201)
async def add_multiple_tasks(tasks: List[TaskSchema]):
    return add_multiple(tasks)


@router.delete("/delete_all_tasks", status_code=204)
async def delete_all_tasks(tasks: List[TaskDeleteSchema]):
    return delete_all(tasks)
