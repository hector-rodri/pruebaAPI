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

def update_task(db: Session, task_id: int, task_data: dict):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None  # Si no existe la tarea, devolvemos Nonea
    
    for key, value in task_data.items():
        setattr(task, key, value)  # Actualizamos los datos
    
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None  # Si no existe, no hacemos nada
    
    db.delete(task)
    db.commit()
    return task_id  # Devolvemos el ID de la tarea eliminada
