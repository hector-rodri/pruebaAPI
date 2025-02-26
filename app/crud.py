from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate


def get_tasks(db: Session):
    """
    Input:
        db: database session
    Output:
        List all tasks
    """
    # TODO: El vostre codi va aqui
    pass


def create_tasks(db: Session, task: TaskCreate):
    """
    Input:
        db: database session
    Output:
        Return the new task
    """
    # TODO: El vostre codi va aqui
    pass

def update_task(db: Session, task_id: int, task_data: dict):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None  # Si no existe la tarea, devolvemos None
    
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
