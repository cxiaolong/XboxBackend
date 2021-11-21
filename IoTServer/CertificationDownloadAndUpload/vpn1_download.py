from flask import request, g
from flask import send_from_directory
import os


# from login.login_authentication_utility import authentication
from . import certification_bp


# @certification_bp.route('/hezi/vpn1/download/', methods=['GET'])
# # @authentication
# def download():
#     SN = request.args.get('SN')
#     PWD = request.args.get('PWD')
#
#     # 'root/OpenVPN/VPN1_username/client_configs/files'
#     root_source = '/root/OpenVPN/VPN1_li188/client_configs/files/'
#     file_name = 'VPN1_li188_client_10.ovpn'
#     response = send_from_directory(directory=root_source+file_name, filename=file_name)
#     response.headers['my-custom-header'] = 'my-custom-status-0'
#     return response


@certification_bp.route('/hezi/vpn1/download/', methods=['GET'])
def get_vpn1():
    SN = request.args.get('SN')
    PWD = request.args.get('PWD')

    # 'root/OpenVPN/VPN1_username/client_configs/files'
    root_source = '/root/OpenVPN/VPN1_li188/client_configs/files/'
    file_name = 'VPN1_li188_client_10.ovpn'
    response = send_from_directory(directory=root_source, filename=file_name)
    response.headers['my-custom-header'] = 'my-custom-status-0'
    return response
