"""
Iot盒子表
"""
from collections import defaultdict
from .base_dao import BaseDao


class BoxDao(BaseDao):
    def __init__(self):
        super(BoxDao, self).__init__()

    def create_box(self):
        pass

    def find_by_username(self, username):
        try:
            with self.conn.cursor() as cursor:
                sql = 'select serial_number,status,group_name,alias from hezi where username=%s'
                cursor.execute(sql, username)
                result = cursor.fetchall()

                if result:
                    boxes_dict = defaultdict(list)
                    for box in result:
                        boxes_dict[box[2]].append(box[0, 1, 3])
                        print(boxes_dict)
                    return boxes_dict

        finally:
            self.close()

    def find_by_SN(self, SN):
        box = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select password,user_id, status from hezi where serial_number=%s'
                cursor.execute(sql, SN)
                result = cursor.fetchone()

                if result:
                    box = {
                        'SN': SN,
                        'password': result[0],
                        'user_id': result[1],
                        'status': result[2],
                    }
        finally:
            self.close()
        return box

    def update_by_user(self, SN, user_id, group_name):
        try:
            with self.conn.cursor() as cursor:
                sql = 'update hezi set user_id=%s, group_name=%s where serial_number=%s'
                cursor.execute(sql, [user_id, group_name, SN])
        finally:
            self.close()