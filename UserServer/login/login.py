from flask import jsonify
from flask import request

from . import login_bp

from dao.user_dao import UserDao


@login_bp.route('/', methods=['GET'])
def index():
    return 'Hello'


@login_bp.route('/', methods=['POST'])
# @authentication
def login():
    # TODO 如何区分邮箱登录和手机号登录以及用户名登录
    username = request.args.get('username')
    mobile = request.args.get('mobile')
    email = request.args.get('email')
    password = request.args.get('password')
    if not password:
        return jsonify('未填写密码'), 403
    if username:
        dao = UserDao()
        user = dao.find_by_username(username=username)
        if not user:
            return jsonify('该用户名未注册'), 403
        if password != user.get('password'):
            return jsonify('密码错误'), 403
        return user, 200
    elif mobile:
        dao = UserDao()
        user = dao.find_by_mobile(mobile=mobile)
        if not user:
            return jsonify('该手机号未注册'), 403
        if password != user.get('password'):
            return jsonify('密码错误'), 403
        return user, 200
    elif email:
        dao = UserDao()
        user = dao.find_by_email(email=email)
        if not user:
            return jsonify('该邮箱未注册'), 403
        if password != user.get('password'):
            return jsonify('密码错误'), 403
        return user, 200
    else:
        return




    # if username == 'admin' and password == '123':
    #     return 'Post Success'
    # else:
    #     abort(400)


