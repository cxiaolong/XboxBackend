import os


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
    # MAIL_USE_SSL = True
    # MAIL_PORT = 465  # 加密发邮件端口
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


# 定义字典，实现不同配置类的映射
config_dict = {
    'base_config': BaseConfig,
    'dev_config': DevelopmentConfig,
    'pro_config': ProductionConfig
}
