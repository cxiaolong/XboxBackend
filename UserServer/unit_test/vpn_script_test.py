import os


def get_vpn1_virtual_ip(certificate):
    r = os.popen('./getIp.sh -k %s' % certificate)
    vpn1_ip = r.read()
    r.close()
    return vpn1_ip


certificate = "VPN1_li188_client_2"
res = get_vpn1_virtual_ip(certificate)