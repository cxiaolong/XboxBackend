from flask_mail import Message, Mail

from celery_tasks.main import celery_app
from flask import current_app


@celery_app.task(bind=True, name='send_email_active', retry_backoff=3)
def send_email_active(self, recipients, code):
    sender = current_app.config['MAIL_DEFAULT_SENDER']
    recipients = [recipients]
    mail = Mail(current_app)
    subject = "IoT系统-邮箱激活"
    html_body = '<p>尊敬的用户您好！</p>' \
                '<p>感谢您使用IoT系统，您的验证码为：%s，五分钟内有效。</p>' % code
    message = Message(recipients=recipients, subject=subject,  sender=sender, html=html_body, charset='utf8')
    try:
        mail.send(message)
    except Exception as e:
        self.retry(exc=e, max_retries=3)