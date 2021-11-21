from .base_dao import BaseDao


class UserDao(BaseDao):
    """用户管理Dao"""
    def __init__(self):
        super().__init__()

    def find_by_username(self, username):
        user = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select user_id,username,phone,password,is_admin from users where username=%s'
                cursor.execute(sql, username)
                result = cursor.fetchone()

                if result:
                    user = {
                        'user_id': result[0],
                        'username': result[1],
                        'phone': result[2],
                        'password': result[3],
                        'is_admin': result[4]
                    }
        finally:
            self.close()
        return user

    def create(self, user):
        pass