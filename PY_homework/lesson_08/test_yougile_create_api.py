from YouGileAPI import YouGileAPI

api = YouGileAPI()


def test_create_project_positive():
    title = "Итоговый проект"

    # Создание проекта
    response = api.create_project(title)
    print(response.text)
    assert response.status_code == 201

    # Получение проекта по ID для проверки
    response_body = response.json()
    project_id = response_body["id"]
    response = api.get_project(project_id)
    assert response.status_code == 200

    # Проверка названия проекта
    response_body = response.json()
    assert response_body["title"] == title

    # Удаление созданного проекта
    response = api.delete_project(project_id)
    assert response.status_code == 200


def test_create_project_negative():
    # Создание проекта с пустым названием
    project_title = ""
    response = api.create_project(project_title)
    print(response.text)
    assert response.status_code == 400
