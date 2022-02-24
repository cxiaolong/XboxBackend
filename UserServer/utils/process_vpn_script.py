import os


def make_vpn_server(u, p, n, m):
    """
    创建VPN1的服务
    :param u: 必传，用户名 
    :param p: 必传，VPN服务的端口号
    :param n: 必传，虚拟局域网网络号
    :param m: 虚拟局域网子网掩码
    :return: 
    """
    os.system('source make-openvpn-server.sh -u %s' )
    pass

def make_vpn_client(a, p, n):
    """
    
    :param a: 
    :param p: 
    :param n: 
    :return: 
    """
    pass


def clean_vpn_service(u):
    """

    :param u:
    :return:
    """
    pass


def get_vpn1_virtual_ip(certificate):
    r = os.popen('/root/cxl/project/UserServer/utils/getIp.sh -k %s' % certificate)
    vpn1_ip = r.read()
    r.close()
    return vpn1_ip