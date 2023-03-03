import smtplib, ssl
from os import getenv


def send_email(msg='Subject: Test\n\n', to=f'{getenv("EMAIL2")}'):
    host = 'smtp.gmail.com'
    port = 465

    username = getenv('PYEMAIL')
    pw = getenv('PYPW')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as mailserver:
        mailserver.login(username, pw)
        mailserver.sendmail(username, to, msg)


if __name__ == '__main__':
    message = "Subject: Test2\n\nTest"
    send_email(msg=message)
