class DefaultConfig(object):
    """默认配置"""
    SECRET_KEY = 'beikeda1950tumuyuziyuananquangongchengcxl'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    HOST_URL = '39.96.113.207'
    SQL_URL = ''
    REDIS_URL = ''


class ProductionConfig(DefaultConfig):
    DEBUG = False