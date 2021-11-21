from flask import request, abort
from werkzeug.utils import secure_filename

from dao.hezi_dao import HeziDao

import os


# from login.login_authentication_utility import authentication
from . import certification_bp


@certification_bp.route('/hezi/vpn2/upload/', methods=['GET'])
# @authentication
def query_vpn2():
    SN = request.args.get('SN')
    PWD = request.args.get('PWD')

    dao = HeziDao()
    hezi = dao.find_by_id(id=SN)
    print(hezi)
    if not hezi or hezi.get('password') != PWD:
        abort(400)

    vpn2_count = hezi.get('vpn2_count')
    print(vpn2_count)
    if vpn2_count == 1:
        return 'VPN2_Recv', 200
    else:
        return 'Wait_VPN2', 200



@certification_bp.route('/hezi/vpn2/upload/', methods=['POST'])
# @authentication
def upload_vpn2():
    SN = request.args.get('SN')
    PWD = request.args.get('PWD')

    f = request.files.get('upload')
    vpn2_nums_str = request.form.get('vpn2_nums')
    print(type(vpn2_nums_str))
    # vpn2_nums = int(vpn2_nums_str)
    if f is None:
        return 'Upload failed', 400
    # 将传输的数字写入数据库
    dao = HeziDao()
    # dao.update_vpn2_nums(SN, vpn2_nums)

    # base_dir = os.path.dirname(__file__)
    # upload_path = os.path.join(base_dir, '/static/file/uploads', secure_filename(f.filename))
    # f.save(upload_path)
    root_source = '/root/OpenVPN/VPN1_li188/VPN2/'
    # filename = 'test1.ovpn'
    f.save(root_source+secure_filename(f.filename))
    return 'OK', 200

