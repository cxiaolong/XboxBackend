import random
import re

import redis
from flask import request, jsonify, redirect

from setting import config_dict
from celery_tasks.sms.tasks import send_sms_code
from celery_tasks.email_active.tasts import send_email_active
from . import register_bp
from dao.user_dao import UserDao


# 测试
@register_bp.route('/', methods=["GET"])
def test():
    return "OK"


@register_bp.route('/', methods=["POST"])
def user_register():
    """
    用户注册
    :return:
    """
    username = request.form.get("username")
    password = request.form.get("password")
    password_repeat = request.form.get("password_repeat")
    mobile = request.form.get("mobile")
    email = request.form.get("email")
    verify_code = request.form.get("verify_code")

    if not all([username, password, password_repeat, mobile]):
        return jsonify(msg='缺少必传参数'), 403
        # 判断用户名是否是2-20个字符
    if not re.match(r'^[a-zA-Z0-9_-]{2,20}$', username):
        return jsonify(msg='请输入5-20个字符的用户名'), 403
        # 判断密码是否是8-20个数字
    if not re.match(r'^[0-9A-Za-z]{8,20}$', password):
        return jsonify(msg='请输入8-20位的密码'), 403
        # 判断两次密码是否一致
    if password != password_repeat:
        return jsonify(msg='两次输入的密码不一致'), 403
        # 判断手机号是否合法
    if not re.match(r'^1[3-9]\d{9}$', mobile):
        return jsonify(msg='请输入正确的手机号码'), 403
    # 判断手机号是否已经存在
    # if User.objects.filter(mobile=mobile).count() > 0:
    #     return http.HttpResponseForbidden('手机号存在')

    redis_conn = redis.StrictRedis(host=config_dict['dev_config'].REDIS_URL, port=config_dict['dev_config'].REDIS_PORT)
    verify_code_server = redis_conn.get('sms_%s' % mobile) or redis_conn.get("email_%s" % email)
    # 判断验证码是否过期
    if verify_code_server is None:
        return jsonify(msg='短信验证码已失效'), 403
    if verify_code_server != verify_code:
        return jsonify(msg="注册失败")
    # TODO 注册逻辑数据库的业务
    user_dao = UserDao()
    try:
        user_dao.create_user(username=username, password=password, mobile=mobile, email=email)
    except Exception as e:
        print(e)
        return jsonify(msg='服务器故障'), 500

    # TODO 状态保持

    return jsonify(msg='OK'), 200

    # redis_conn = get_redis_connection('verify_code')  # 建立与redis数据库的连接对象
    # sms_code_server = redis_conn.get('sms_%s' % mobile)
    # if sms_code_server is None:
    #     return jsonify(msg='短信验证码已失效')
    #     return render(request, 'register.html', {'sms_code_errmsg': '短信验证码已失效'})
    # if sms_code_client != sms_code_server.decode():
    #     return render(request, 'register.html', {'sms_code_errmsg': '账号或密码错误'})

    # try:
    #     user = User.objects.create_user(username=username, password=password, mobile=mobile)
    # except DatabaseError as e:
    #     print(e)
    #     return render(request, 'register.html', {'register_errmsg': '注册失败'})
    #
    #     # 登入用户，实现状态保持
    # login(request, user)
    #
    # # 响应结果：重定向到首页
    # # reverse('contents:index') == '/'
    # response = redirect(reverse('contents:index'))
    # # 用户注册后用户名写入cookie，有效期15天
    # response.set_cookie('username', user.username, max_age=15 * 24 * 3600)
    # return response
    # 响应结果：重定向到创建VPN服务
    response = redirect('/CertificationDownloadAndUpload/generate_verification/')
    return response



@register_bp.route('/sms/<mobile>', methods=['GET'])
def send_sms(mobile):
    """发送短信验证码"""
    if not re.match(r'^1[3-9]\d{9}$', mobile):
        return jsonify(msg='请输入正确的手机号码'), 403

    # 连接Redis数据库
    redis_conn = redis.StrictRedis(host=config_dict['dev_config'].REDIS_URL, port=config_dict['dev_config'].REDIS_PORT)

    # 60s内不允许重复发送短信验证码
    send_flag = redis_conn.get("sms_%s" % mobile)
    if send_flag:
        return jsonify(msg="发送验证码过于频繁"), 400

    # 生成短信验证码
    sms_code = '%06d' % random.randint(0, 999999)

    # 利用celery异步发送短信验证码
    send_sms_code(mobile=mobile, sms_code=sms_code)
    # send_sms_code.delay(mobile=mobile, sms_code=sms_code)

    # 将短信验证码存入redis
    redis_conn.setex("sms_%s" % mobile, 60, sms_code)

    return 'OK'


@register_bp.route('/email/<email_count>', methods=['GET'])
def send_email(email_count):
    """邮箱发送验证码"""
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email_count):
        return jsonify(msg="请输入正确的邮箱"), 403

        # 连接Redis数据库
    redis_conn = redis.StrictRedis(host=config_dict['dev_config'].REDIS_URL, port=config_dict['dev_config'].REDIS_PORT)

    # 60s内不允许重复发送邮箱验证码
    send_flag = redis_conn.get("email_%s" % email_count)
    if send_flag:
        return jsonify(msg="发送验证码过于频繁"), 400

    # 生成验证码
    code = '%06d' % random.randint(0, 999999)

    # 利用celery异步发送短信验证码
    send_email_active(recipients=email_count, code=code)
    # send_email_active.delay(recipients=email_count, code=code)

    # 将邮箱验证码存入redis
    redis_conn.setex("email_%s" % email_count, 60*5, code)

    return 'OK'