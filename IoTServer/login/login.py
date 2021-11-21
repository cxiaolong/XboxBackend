from flask import request, redirect, abort, g, send_from_directory

from setting import DevelopmentConfig
from . import login_bp
# from .login_authentication_utility import authentication

from dao.hezi_dao import HeziDao


@login_bp.route('/', methods=['GET'])
def index():
    return 'OK'


@login_bp.route('/hezi/login/', methods=['POST'])
# @authentication
def login():
    data_dict = eval(request.data.decode())

    dao = HeziDao()  # 实例化数据库查询对象
    g.serial_number = data_dict.get('SN')
    g.pwd = data_dict.get('PWD')

    hezi = dao.find_by_id(id=g.serial_number)
    if not hezi or hezi.get('password') != g.pwd:
        abort(400, 'Connection_Refused')

    if hezi.get('is_bind') == 0:
        return 'Bind_Null', 200
    g.sn = g.serial_number
    return 'Bind_Success', 200


@login_bp.route('/hezi/is_bind/', methods=['GET', 'POST', 'DELETE'])
# @authentication
def vpn1_is_bind():
    SN = request.args.get('SN')
    PWD = request.args.get('PWD')
    try:
        dao = HeziDao()  # 实例化数据库查询对象
        hezi = dao.find_by_id(id=SN)
        if not hezi or hezi.get('password') != PWD:
            abort(400, 'Connection_Refused')

        if hezi.get('is_bind') == 1:
            return 'Bind_Success', 200
        return 'Bind_Null', 200
    except:
        return 'Forbidden', 403