import os

from flask import Flask, current_app
from flask_mail import Message, Mail


class BaseConfig:
    """配置的基类"""
    SECRET_KEY = 'beikeda1950tumuyuziyuananquangongchengcxl'

    HOST_URL = '39.96.113.207'
    SQL_URL = ''
    REDIS_URL = '39.96.113.207'
    REDIS_PORT = 6379


class DevelopmentConfig(BaseConfig):
    """开发配置类"""
    DEBUG = True

    # 第三方SMTP服务
    MAIL_SERVER = 'smtp.163.com'  # 发邮件主机
    # MAIL_PORT = 25  # 发邮件端口
    MAIL_USE_SSL = True
    MAIL_PORT = 465  # 加密发邮件端口
    MAIL_USERNAME = 'RoseTech207@163.com'  # 发新服务器的用户名
    MAIL_PASSWORD = 'VHNNTUOPIBRBEULR'  # 客户端授权码
    MAIL_DEFAULT_SENDER = ('RoseTech207', 'RoseTech207@163.com')  # 默认的发信人


class ProductionConfig(BaseConfig):
    """生产类"""
    DEBUG = False
    """
    邮箱配置：
    export MAIL_USERNAME='你的邮箱账号'
    export MAIL_PASSWORD='客户端授权密码'
    如果想永久有效，把上面两句话加到配置文件中，mac(/.bash_profile)，linux(/.bashrc)
    """
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


# 定义字典，实现不同配置类的映射
config_dict = {
    'base_config': BaseConfig,
    'dev_config': DevelopmentConfig,
    'pro_config': ProductionConfig
}


def create_flask_app(config):
    """
    创建Flask应用
    :param config: 配置对象
    :return: Flask应用
    """
    app = Flask(__name__)
    app.config.from_object(config)

    app.config.from_envvar("PROJECT_SETTING", silent=True)
    return app


if __name__ == '__main__':
    app = create_flask_app(config=config_dict.get('dev_config'))
    code = '469271'
    subject = "IoT系统-邮箱激活"
    recipients = ['a18811732515@163.com']
    html_body = '<p>尊敬的用户您好！</p>' \
                '<p>感谢您使用IoT系统，您的验证码为：%s，一分钟内有效。</p>' % code
    sender = app.config['MAIL_DEFAULT_SENDER']

    # mail = Mail(current_app)
    mail = Mail(app)
    with app.app_context():
        message = Message(recipients=recipients, subject=subject,  sender=sender, html=html_body, charset='utf8')
        try:
            mail.send(message)
        except Exception as e:
            print(e)


    # def send_email_active(recipients, code):
    #     sender = current_app.config['MAIL_DEFAULT_SENDER']
    #     recipients = [recipients]
    #     mail = Mail(current_app)
    #     subject = "IoT系统-邮箱激活"
    #     html_body = '<p>尊敬的用户您好！</p>' \
    #                 '<p>感谢您使用IoT系统，您的验证码为：%s，一分钟内有效。</p>' % code
    #     message = Message(recipients=recipients, subject=subject, sender=sender, html=html_body, charset='utf8')
    #     try:
    #         mail.send(message)
    #     except Exception as e:
    #         # self.retry(exc=e, max_retries=3)
    #         print(e)
    # with app.app_context():
    #     send_email_active(recipients=recipients, code=code)
