import smtplib
from email.mime.text import MIMEText
from decouple import config

EMAIL_HOST_PASSWORD = 'vvtzumslzqlsyrks'


def send_mail(to, theme, message):
    """Функция по отправке сообщений пользователю"""
    file_content = message

    msg = MIMEText(file_content)
    msg['Subject'] = theme
    msg['From'] = 'yukiniora@yandex.ru'
    msg['To'] = to

    smtp_server = 'smtp.yandex.ru'
    smtp_port = 465
    smtp_username = 'yukiniora@yandex.ru'
    smtp_password = config('EMAIL_HOST_PASSWORD')

    s = smtplib.SMTP_SSL(smtp_server, smtp_port)
    s.login(smtp_username, smtp_password)
    s.sendmail('yukiniora@yandex.ru', [to], msg.as_string())

    s.quit()
