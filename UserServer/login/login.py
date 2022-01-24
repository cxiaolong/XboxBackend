from flask import jsonify
from flask import request
from flask import g

from dao.user_dao import UserDao
from dao.group_dao import GroupDao
from . import login_bp


# test
@login_bp.route('/', methods=['GET'])
def index():
    return 'Hello'


# 用户登陆主逻辑
@login_bp.route('/', methods=['POST'])
# @authentication
def login():
    mobile = request.args.get('mobile')
    email = request.args.get('email')
    username = mobile or email
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
    g.username = username

    # TODO 查找该用户下盒子的分组信息
    # table_name = "group_" + username
    # group_dao = GroupDao()
    # group_list = group_dao.search_group(table_name=table_name)

    # TODO 查询该用户绑定的盒子信息，统计盒子总数，盒子状态


    stateInfo = None

    #  update info (消息推送，版本更新等）
    updateInfo = {
        "info": "None",
        "other": "none"
    }

    res = {'groupInfo': groupInfo, 'stateInfo': stateInfo, 'updateInfo': updateInfo}

    # elif mobile:
    #     dao = UserDao()
    #     user = dao.find_by_mobile(mobile=mobile)
    #     if not user:
    #         return jsonify('该手机号未注册'), 403
    #     if password != user.get('password'):
    #         return jsonify('密码错误'), 403
    #     return user, 200
    # elif email:
    #     dao = UserDao()
    #     user = dao.find_by_email(email=email)
    #     if not user:
    #         return jsonify('该邮箱未注册'), 403
    #     if password != user.get('password'):
    #         return jsonify('密码错误'), 403
    #     return user, 200
    #
    # res = {
    #     "groupInfo": [
    #         {
    #             "name": "WIFI版",
    #             "boxNum": 3,
    #             "Boxes": [
    #                 {
    #                     "Alias": "上海工厂",
    #                     "SN": "202201010001"
    #                 },
    #                 {
    #                     "Alias": "北京总部",
    #                     "SN": "202201010002"
    #                 },
    #                 {
    #                     "Alias": "长沙工厂",
    #                     "SN": "202201010003"
    #                 }
    #             ],
    #         },
    #         {
    #             "name": "4G版",
    #             "boxNum": 1,
    #             "Boxes": [
    #
    #                 {
    #                     "Alias": "北京总部",
    #                     "SN": "202201010004"
    #                 }
    #             ],
    #         }
    #     ],
    #     "stateInfo": {
    #         "alarm": 0,
    #         "alarmNum": 0,
    #         "allNum": 3,
    #         "onlineNum": 3
    #     },
    #     "updateInfo": {
    #         "info": "版本v0.1",
    #         "other": "测试版本"
    #     }
    # }
    #
    # return jsonify(msg=res), 200
