
import os
from dotenv import load_dotenv
from QAtable import QATable

load_dotenv()
db = QATable(os.getenv("QA_TABLE"))


# 1. Добавить в таблицу Teacher нового учителя
def test_insert():
    # получаем максимальный teacher_id из БД
    my_t_id = db.get_max_id()

    # создаем учителя
    params = {
              't_id': my_t_id,
              'email': 'dfgh@wait.com',
              'group_id': 76
    }
    db.create_teacher(params)

    # проверяем создание учителя по всем параметрам
    check_sql = db.check_teacher(params)
    assert check_sql == 1

    # удаление учителя
    db.delete_by_id(my_t_id)


# 2. Изменение данных учителя
def test_update():
    # получаем максимальный teacher_id из БД
    my_t_id = db.get_max_id()

    # создаем учителя
    params = {
              't_id': my_t_id,
              'email': 'dfgh@wait.com',
              'group_id': 76
    }
    db.create_teacher(params)

    # изменение данных учителя
    new_params = {
                't_id': my_t_id,
                'email': 'dfghf@wait.com',
                'group_id': 5555
                }
    db.edit_data(new_params)

    # проверяем изменение данных учителя по его ID
    rows = db.select_by_id(my_t_id)

    assert len(rows) == 1
    assert rows[0]["group_id"] == new_params['group_id']

    # удаление учителя
    db.delete_by_id(my_t_id)


# 3. Удаление учителя
def test_delete():
    # получаем максимальный teacher_id из БД
    my_t_id = db.get_max_id()

    # создаем учителя
    params = {
              't_id': my_t_id,
              'email': 'dfgh@wait.com',
              'group_id': 76
    }
    db.create_teacher(params)

    # удаление учителя
    db.delete_by_id(my_t_id)

    # Проверяем, что удаленная компания не находится по id
    rows = db.check_delete(my_t_id)
    assert len(rows) == 0, f"Учитель с id {my_t_id} все еще находится в базе"
