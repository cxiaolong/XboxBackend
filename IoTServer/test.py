import pymysql


# conn = pymysql.connect(
#             host='39.96.113.207',
#             user='root',
#             port=3306,
#             password='20700702',
#             database='iot_hezi',
#             charset='utf8'
#         )
#
# sql = 'select serial_number,vpn2_count from hezi where serial_number=%s'
# with conn.cursor() as cursor:
#     cursor.execute(sql, 'IOT0001')
#     result = cursor.fetchone()
#     print(result)


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


class HeziDao(BaseDao):
    def __init__(self):
        super().__init__()

    def find_vpn2_count(self):
        vpn2 = None
        try:
            id = 'IOT0001'
            sql = 'update hezi set vpn2_count=%d where serial_number=' + id % (4)
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
        #         result = cursor.fetchone()
        #         print(result)
        #
        #         if result:
        #             vpn2 = {
        #                 'serial_number': result[0],
        #                 'vpn2_count': result[1],
        #             }
        except Exception as e:
            print(e)
        # # finally:
        # #     self.close()
        # return vpn2


if __name__ == '__main__':
    hezi_dao = HeziDao()
    vpn2 = hezi_dao.find_vpn2_count()