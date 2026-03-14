from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas import TaskCreate
from backend.models import Task
from backend.dependencies import get_db
from backend.auth_middleware import get_current_user

router = APIRouter()

@router.post("/tasks")
def create_task(task: TaskCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)):

    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=1
    )

    db.add(new_task)
    db.commit()

    return {"message": "Task created"}


@router.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    tasks = db.query(Task).filter(Task.user_id == user["user_id"]).all()

    return tasks