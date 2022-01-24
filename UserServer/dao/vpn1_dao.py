"""
VPN1证书表
与用户绑定，证书表表名为vpn1_username
当用户创建后，默认生成固定数量（10）的VPN1证书
"""
from .base_dao import BaseDao


class VPN1Dao(BaseDao):
    def __init__(self):
        super(VPN1Dao, self).__init__()

    def create_vpn1_table(self, username, nums):
        """
        创建一个VPN1证书表，表中创建一个0-nums（nums默认为10）条的数据
        :param username:
        :return:
        """
        pass

