"""
VPN2证书表
与盒子绑定，证书表表名为vpn2_boxId，boxId为盒子序列号
当盒子创建后，执行脚本默认生成固定数量（5）的VPN2证书
"""
from .base_dao import BaseDao


class VPN1Dao(BaseDao):
    def __init__(self):
        super(VPN1Dao, self).__init__()

    def create_vpn1_table(self, username, nums):
        """
        创建一个VPN1证书表，表中创建一个0-nums（nums默认为5）条的数据
        :param username:
        :return:
        """
        pass

