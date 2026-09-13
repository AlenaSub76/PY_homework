from sqlalchemy import create_engine, text


class QATable:
    scripts = {
        "get max id": text('SELECT MAX(teacher_id) FROM teacher'),
        "create": text('INSERT INTO '
                       'teacher("teacher_id", "email", "group_id") '
                       'VALUES (:t_id, :email, :group_id)'),
        "check": text('SELECT COUNT(*) FROM teacher '
                      'WHERE teacher_id=:t_id AND email=:email '
                      'AND group_id=:group_id'),
        "delete by id": text('DELETE FROM teacher WHERE teacher_id = :t_id'),
        "edit data": text('UPDATE teacher SET group_id = :group_id '
                          'WHERE teacher_id = :t_id'),
        "select by id": text('SELECT * FROM teacher WHERE teacher_id = :t_id'),
        "check delete": text('SELECT * FROM teacher WHERE teacher_id = :t_id')
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_max_id(self):
        conn = self.db.connect()
        result = conn.execute(self.scripts["get max id"])
        my_t_id = (result.scalar() or 0) + 1
        # (result.scalar() or 0) + 1
        conn.close()
        return my_t_id

    def create_teacher(self, params):
        conn = self.db.connect()
        conn.execute(self.scripts["create"], params)
        conn.commit()
        conn.close()

    def check_teacher(self, params):
        conn = self.db.connect()
        result = conn.execute(self.scripts["check"], params).scalar()
        conn.close()
        return result

    def delete_by_id(self, my_t_id):  # удалить
        conn = self.db.connect()
        conn.execute(self.scripts["delete by id"], {"t_id": my_t_id})
        conn.commit()
        conn.close()

    def edit_data(self, new_params):
        conn = self.db.connect()
        conn.execute(self.scripts["edit data"], new_params)
        conn.commit()
        conn.close()

    def select_by_id(self, my_t_id):
        conn = self.db.connect()
        result = conn.execute(self.scripts["select by id"], {"t_id": my_t_id})
        rows = result.mappings().all()
        conn.close()
        return rows

    def check_delete(self, my_t_id):
        conn = self.db.connect()
        result = conn.execute(self.scripts["check delete"], {"t_id": my_t_id})
        rows = result.mappings().all()
        conn.close()
        return rows

