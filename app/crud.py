from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session):

    return db.query(Task).all()


def create_tasks(db: Session, task: TaskCreate):
    
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_tasks(db: Session, task_id: int, task_update: TaskUpdate):
    """
    Input:
        db: database session
    Output:
        Updated some task fields
    """
    # TODO: El vostre codi va aqui
    pass


def delete_tasks(db: Session, task_id: int):
    """
    Input:
        db: database session
    Output:
        Return delete task
    """
    # TODO: El vostre codi va aqui
    pass
