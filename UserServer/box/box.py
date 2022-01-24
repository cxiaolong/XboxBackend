from . import box_bp
from flask import request
from flask import jsonify
from flask import g

from dao.box_dao import BoxDao


# 测试
@box_bp.route('/', methods=['GET'])
def test():
    return 'OK'


# 添加盒子
@box_bp.route('/add/', methods=['POST'])
def add():
    SN = request.get_json('SN')
    password = request.get_json('password')
    group = request.get_json('group')
    note = request.get_json('note')
    user_id = request.get_json('user_id')
    print(SN, password, group)

    if not all([SN, password, group]):
        return jsonify('缺少必传参数'), 404
    #
    # # 盒子认证
    # box_dao = BoxDao()
    # box = box_dao.find_by_SN(SN=SN)
    # if box.get('password') != password:
    #     return jsonify('验证错误'), 404
    # if box.get('SN'):
    #     return jsonify('盒子已被其他用户绑定')
    # if box.get('status') == 0:
    #     return jsonify('当前盒子不在线'), 404
    # # 数据库录入盒子的操作过程
    # # username = g.username
    # box.update_by_user(SN=SN, user_id=user_id, group_name=group)
    return jsonify('bind success'), 200
