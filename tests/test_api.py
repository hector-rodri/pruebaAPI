from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_task():
    # Crear una tarea inicial para actualizar
    response = client.post("/tasks", json={"title": "Tarea inicial", "description": "Descripción inicial"})
    assert response.status_code == 200
    task = response.json()
    task_id = task["id"]


    # Actualizar la tarea
    update_data = {"title": "Tarea actualizada", "description": "Descripción actualizada", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    updated_task = response.json()


    # Verificar que los datos se hayan actualizado correctamente
    assert updated_task["title"] == "Tarea actualizada"
    assert updated_task["description"] == "Descripción actualizada"
    assert updated_task["completed"] is True


def test_delete_task():
    # Crear una tarea inicial para eliminar
    response = client.post("/tasks", json={"title": "Tarea a eliminar", "description": "Descripción de la tarea"})
    assert response.status_code == 200
    task = response.json()
    task_id = task["id"]


    # Eliminar la tarea
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Tasca eliminada"}


    # Verificar que la tarea ya no exista
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Tasca no trobada"}


def test_create_task():
    # Crear una nueva tarea
    task_data = {"title": "Nueva tarea", "description": "Descripción de la nueva tarea"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    created_task = response.json()


    # Verificar que los datos de la tarea creada sean correctos
    assert created_task["title"] == task_data["title"]
    assert created_task["description"] == task_data["description"]
    assert created_task["completed"] is False  # Por defecto, 'completed' debe ser False
    assert "id" in created_task  # Verificar que se genera un ID


def test_get_tasks():
    # Crear dos tareas para probar la obtención
    client.post("/tasks", json={"title": "Tarea 1", "description": "Descripción 1"})
    client.post("/tasks", json={"title": "Tarea 2", "description": "Descripción 2"})


    # Obtener todas las tareas
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()


    # Verificar que se devuelven al menos dos tareas
    assert len(tasks) >= 2


    # Verificar que las tareas creadas están en la lista
    titles = [task["title"] for task in tasks]
    assert "Tarea 1" in titles
    assert "Tarea 2" in titles

