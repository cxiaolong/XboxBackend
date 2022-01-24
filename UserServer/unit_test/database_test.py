import pymysql
from collections import defaultdict

host = '127.0.0.1'
port = 3306
user = 'root'
password = '20700702'
database = 'iot_hezi'
charset = 'utf8'


class BaseDao:
    """定义Dao基类"""

    def __init__(self):
        """实例初始化时连接数据库"""

        self.conn = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database,
            charset=charset
        )

    def close(self):
        """关闭数据库连接"""
        self.conn.close()


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
                sql = 'INSERT INTO {}(group_name) VALUES(%s)'.format(table_name)
                cursor.execute(sql, group_name)
                cursor.execute(sql)
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
        except Exception as e:
            print(e)
        finally:
            self.close()


class BoxDao(BaseDao):
    def __init__(self):
        super(BoxDao, self).__init__()

    def create_box(self):
        pass

    def find_by_username(self, username):
        try:
            with self.conn.cursor() as cursor:
                sql = 'select serial_number,status,group_name,alias from box where username=%s'
                cursor.execute(sql, username)
                result = cursor.fetchall()

            if result:
                boxes_dict = defaultdict(list)
                for box in result:
                    boxes_dict[box[2]].append(box)
                    print(boxes_dict)
                return boxes_dict

        finally:
            self.close()


if __name__ == '__main__':
    group = GroupDao()
    # group.create_group_table(username='13956102941')
    # group.create_group(username='13956102941', group_name='南京地区')
    # group_list = group.search_group(table_name='group_13956102941')
    # print(group_list)
    box_dao = BoxDao()
    boxes_dict = box_dao.find_by_username(username='13956102941')
    print(dict(boxes_dict))