import pymysql


class BaseDao:
    """定义Dao基类"""

    def __init__(self):
        """实例初始化时连接数据库"""

        self.conn = pymysql.connect(
            host='39.96.113.207',
            user='root',
            port=3306,
            password='20700702',
            database='iot_hezi',
            charset='utf8'
        )

    def close(self):
        """关闭数据库连接"""
        self.conn.close()