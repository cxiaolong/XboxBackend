"""
用户自建的盒子分组表
每个用户创建（注册）后默认产生一个分组表group_username
"""
from .base_dao import BaseDao


class GroupDao(BaseDao):
    def __init__(self):
        super(GroupDao, self).__init__()

    def create_group_table(self, username):
        """
        创建一个分组表，可以是用户注册后自动创建，也可以是用户手动创建
        :param username:
        :return:
        """
        try:
            with self.conn.cursor() as cursor:
                sql = """CREATE TABLE IF NOT EXISTS group_%s(
        	                    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
        	                    group_name VARCHAR(20) NOT NULL,
        	                    comments VARCHAR(50)
        	                    )""" % username
                cursor.execute(sql)
        finally:
            self.close()

    def create_group(self, username, group_name):
        table_name = 'group_' + username
        try:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO {}(group_name) VALUES(%s)".format(table_name)
                cursor.execute(sql, group_name)
        finally:
            self.close()


    def search_group(self, table_name):
        try:
            with self.conn.cursor() as cursor:
                sql = 'SELECT group_name FROM %s' % table_name
                cursor.execute(sql)
                result = cursor.fetchall()
                group_list = [group[0] for group in result]
                return group_list
        finally:
            self.close()