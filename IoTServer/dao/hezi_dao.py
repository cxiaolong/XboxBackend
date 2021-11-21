from .base_dao import BaseDao


class HeziDao(BaseDao):
    """用户管理Dao"""
    def __init__(self):
        super().__init__()

    def find_by_id(self, id):
        hezi = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select serial_number,password,is_bind,vpn2_count from hezi where serial_number=%s'
                cursor.execute(sql, id)
                result = cursor.fetchone()

                if result:
                    hezi = {
                        'serial_number': result[0],
                        'password': result[1],
                        'is_bind': result[2],
                        'vpn2_count': result[3]
                    }
        finally:
            self.close()
        return hezi

    def find_owner_by_id(self, id):
        owner = None
        try:
            with self.conn.cursor() as cursor:
                sql = 'select serial_number,password,is_bind from hezi where serial_number=%s'
                cursor.execute(sql, id)
                result = cursor.fetchone()

                if result:
                    owner = {
                        'serial_number': result[0],
                        'password': result[1],
                        'is_bind': result[3]
                    }
        finally:
            self.close()
        return owner


    def update_vpn2_nums(self, id, vpn2_nums):
        try:
            with self.conn.cursor() as cursor:
                # sql = 'update hezi set vpn2_count=%d where serial_number='    + "'" + id + "'"
                sql = 'update hezi set vpn2_count=%d where serial_number=%s' % (vpn2_nums, "'" + id + "'")
                cursor.execute(sql)
        finally:
            self.close()


    def create(self, user):
        pass