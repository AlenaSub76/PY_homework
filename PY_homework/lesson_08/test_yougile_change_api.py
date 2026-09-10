from YouGileAPI import YouGileAPI
import requests  # используется для обновления проекта без токена (напрямую)

api = YouGileAPI()


def test_change_project_positive():
    # Создание проекта
    response = api.create_project("Автоматизация")
    assert response.status_code == 201

    response_body = response.json()
    project_id = response_body["id"]

    # Изменение названия проекта
    new_title = "Автоматизация Python"
    response = api.change_project(project_id, new_title)
    assert response.status_code == 200

    # Проверка изменения названия
    response = api.get_project(project_id)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["title"] == new_title
    print(response_body["title"])

    # Удаление проекта
    response = api.delete_project(project_id)
    assert response.status_code == 200


def test_change_project_negative_1():
    # Создание проекта
    response = api.create_project("Автоматизация")
    assert response.status_code == 201

    response_body = response.json()
    project_id = response_body["id"]

    # Обновление проекта без токена (напрямую через requests)
    url = f"{api.base_url}projects/{project_id}"
    headers_without_token = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer'
    }
    project_new = {"title": "Автоматизация"}
    response = requests.put(url, headers=headers_without_token,
                            json=project_new)
    assert response.status_code == 401

    # Удаление проекта
    response = api.delete_project(project_id)
    assert response.status_code == 200


def test_change_project_negative_2():
    # Создание проекта
    response = api.create_project("Автоматизация")
    assert response.status_code == 201

    response_body = response.json()
    project_id = response_body["id"]

    # Попытка обновления с пустым ID
    empty_project_id = ""
    response_up = api.change_project(empty_project_id, "Автоматизация Python")
    assert response_up.status_code == 404

    # Удаление проекта
    response = api.delete_project(project_id)
    assert response.status_code == 200
