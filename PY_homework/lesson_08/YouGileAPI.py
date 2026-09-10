import requests
from dotenv import dotenv_values


class YouGileAPI:

    def __init__(self, token=None, user_id=None):
        self.base_url = "https://yougile.com/api-v2/"
        my_env = dotenv_values('.env')
        self.token = token if token else my_env.get('YOUGILE_TOKEN')
        self.user_id = user_id if user_id else my_env.get('YOUGILE_USER_ID')
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

    def create_project(self, title):
        """Создание нового проекта"""
        url = f"{self.base_url}projects"
        project = {
             "title": title,
             "users": {self.user_id: "worker"}}
        response = requests.post(url, headers=self.headers, json=project)
        return response

    def get_project(self, project_id):
        """Получение проекта по ID"""
        url = f"{self.base_url}projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def change_project(self, project_id, title):
        """Обновление проекта"""
        url = f"{self.base_url}projects/{project_id}"
        project = {"title": title}
        response = requests.put(url, headers=self.headers, json=project)
        return response

    def delete_project(self, project_id):
        """Удаление проекта"""
        url = f"{self.base_url}projects/{project_id}"
        project_del = {"deleted": True}
        response = requests.put(url, headers=self.headers, json=project_del)
        return response
