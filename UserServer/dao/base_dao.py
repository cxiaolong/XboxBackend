import configparser
import pymysql


class BaseDao:
    """定义Dao基类"""

    def __init__(self):
        """实例初始化时连接数据库"""
        self.config = configparser.ConfigParser()
        self.config.read('config.ini', encoding='utf-8')

        # 读取数据库配置
        host = self.config['db']['host']
        user = self.config['db']['user']
        port = self.config.getint('db', 'port')  # 读取整数port数据
        password = self.config['db']['password']
        database = self.config['db']['database']
        charset = self.config['db']['charset']

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