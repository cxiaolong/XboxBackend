import os
from flask import jsonify
from flask import request
from flask import send_from_directory

from . import vpn_bp


# test
@vpn_bp.route('/', methods=['GET'])
def index():
    return 'Hello'


# get vpn1 or vpn2 certificate
@vpn_bp.route('/', methods=['POST'])
def get_certificate():
    vpn_type = request.args.get('vpn')
    username = request.get_json().get('username')
    password = request.get_json().get('password')

    # TODO 验证用户名和密码的逻辑
    if username != 'li188' or password != '123':
        return jsonify(msg='用户名或密码错误'), 404

    vpn1_path = "/root/OpenVPN/VPN1_{}/client_configs/files/".format(username)
    vpn2_path = "/root/OpenVPN/VPN1_{}/VPN2/".format(username)

    # TODO 获取具体vpn证书的逻辑
    vpn1_certificate = "VPN1_{}_client_10.ovpn".format(username)
    vpn2_certificate = "VPN1_{}_client_10.ovpn".format(username)

    if vpn_type == "1":
        directory = vpn1_path
        filename = vpn1_certificate
    else:
        directory = vpn2_path
        filename = vpn2_certificate

    assert os.path.exists(directory), "'{}' does not exists".format(directory)

    response = None
    try:
        response = send_from_directory(directory=directory, filename=filename)
    except Exception as e:
        print(e)

    response.headers['my-custom-header'] = 'my-custom-status-0'
    return response if response else ('error', 500)
