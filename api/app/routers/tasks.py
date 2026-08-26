from fastapi import APIRouter, HTTPException

from ..data import TASKS, next_task_id
from ..models import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[Task])
def list_tasks():
    return TASKS


@router.post("", response_model=Task, status_code=201)
def create_task(payload: TaskCreate):
    task = Task(id=next_task_id(), **payload.model_dump())
    TASKS.append(task)
    return task


@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in TASKS:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.patch("/{task_id}", response_model=Task)
def update_task(task_id: int, payload: TaskUpdate):
    for index, task in enumerate(TASKS):
        if task.id == task_id:
            updated = task.model_copy(update=payload.model_dump(exclude_unset=True))
            TASKS[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(TASKS):
        if task.id == task_id:
            TASKS.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")
