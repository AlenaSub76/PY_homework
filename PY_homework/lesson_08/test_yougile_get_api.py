from YouGileAPI import YouGileAPI

api = YouGileAPI()


def test_get_project_id_positive():
    # Создание проекта
    response = api.create_project("Проверка связи")
    assert response.status_code == 201

    # Получение проекта по ID
    response_body = response.json()
    project_id = response_body["id"]
    response = api.get_project(project_id)
    assert response.status_code == 200

    # Проверка ID проекта
    response_body = response.json()
    assert response_body["id"] == project_id

    # Удаление проекта
    response = api.delete_project(project_id)
    assert response.status_code == 200


def test_get_project_negative():
    # Создание проекта
    response = api.create_project("Проверка связи")
    assert response.status_code == 201

    # Попытка получить проект с некорректным ID
    invalid_project_id = "парарпапрап"
    response_id = api.get_project(invalid_project_id)
    assert response_id.status_code == 404

    # Удаление созданного проекта
    response_body = response.json()
    project_id = response_body["id"]
    response = api.delete_project(project_id)
    assert response.status_code == 200
