from .base_dao import BaseDao


class UserDao(BaseDao):
    """用户管理Dao"""
    def __init__(self):
        super().__init__()

    def find_by_username(self, username):
        user = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select user_id,username,mobile,email,password,is_admin from users where username=%s'
                cursor.execute(sql, username)
                result = cursor.fetchone()

                if result:
                    user = {
                        'user_id': result[0],
                        'username': result[1],
                        'mobile': result[2],
                        'email': result[3],
                        'password': result[4],
                        'is_admin': result[5]
                    }
        finally:
            self.close()
        return user

    def find_by_mobile(self, mobile):
        user = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select user_id,username,phone,email,password,is_admin from users where mobile=%s'
                cursor.execute(sql, mobile)
                result = cursor.fetchone()

                if result:
                    user = {
                        'user_id': result[0],
                        'username': result[1],
                        'mobile': result[2],
                        'email': result[3],
                        'password': result[4],
                        'is_admin': result[5]
                    }
        finally:
            self.close()
        return user

    def find_by_email(self, email):
        user = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select user_id,username,phone,email,password,is_admin from users where mobile=%s'
                cursor.execute(sql, email)
                result = cursor.fetchone()

                if result:
                    user = {
                        'user_id': result[0],
                        'username': result[1],
                        'mobile': result[2],
                        'email': result[3],
                        'password': result[4],
                        'is_admin': result[5]
                    }
        finally:
            self.close()
        return user

    def create_user(self, username, password, mobile, email):
        try:
            with self.conn.cursor() as cursor:
                sql = 'insert into users values(username=%s, password=%s, moble=%s, email=%s)'
                cursor.excute(sql, (username, password, mobile, email))
        except Exception as e:
            print(e)
        finally:
            self.close()