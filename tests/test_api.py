from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_update_task():
    response = client.post("/tasks", json={"title": "Tarea inicial", "description": "Descripción inicial"})
    assert response.status_code == 200
    task = response.json()
    task_id = task["id"]

    update_data = {"title": "Tarea actualizada", "description": "Descripción actualizada", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    updated_task = response.json()

    assert updated_task["title"] == "Tarea actualizada"
    assert updated_task["description"] == "Descripción actualizada"
    assert updated_task["completed"] is True


def test_delete_task():
    response = client.post("/tasks", json={"title": "Tarea a eliminar", "description": "Descripción de la tarea"})
    assert response.status_code == 200
    task = response.json()
    task_id = task["id"]


    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Tasca eliminada"}



    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Tasca no trobada"}


def test_create_task():

    task_data = {"title": "Nueva tarea", "description": "Descripción de la nueva tarea"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    created_task = response.json()

    assert created_task["title"] == task_data["title"]
    assert created_task["description"] == task_data["description"]
    assert created_task["completed"] is False  
    assert "id" in created_task  


def test_get_tasks():

    client.post("/tasks", json={"title": "Tarea 1", "description": "Descripción 1"})
    client.post("/tasks", json={"title": "Tarea 2", "description": "Descripción 2"})


    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()

    assert len(tasks) >= 2

    titles = [task["title"] for task in tasks]
    assert "Tarea 1" in titles
    assert "Tarea 2" in titles

