from ronglian_sms_sdk import SmsSDK

from celery_tasks.main import celery_app
from . import constants


accId = '8aaf0708732220a60173b6f78b5542a6'
accToken = '02cfd485898847cca52798061c8703cf'
appId = '8a216da87ce04099017cfac0226105b4'


# 使用装饰器装饰异步任务，保证celery识别任务
@celery_app.task(bind=True, name='send_sms_code', retry_backoff=3)
def send_sms_code(self, mobile, sms_code):
    try:
        sdk = SmsSDK(accId, accToken, appId)
        interval = constants.SEND_SMS_CODE_INTERVAL // 60
        send_ret = sdk.sendMessage(tid=constants.SEND_SMS_TEMPLATE_ID, mobile=mobile, datas=[sms_code, interval])
        return send_ret
    except Exception as e:
        raise self.retry(exc=e, max_retries=3)