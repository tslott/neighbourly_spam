import os
import getpass
from smtplib import SMTP
from email.message import EmailMessage


def send_message():

    # Create EmailMessage
    msg = EmailMessage()
    msg['Subject'] = 'Klump'
    msg['From'] = os.environ['EMAIL_ADDRESS']
    msg['To'] = os.environ['TARGET_EMAIL_ADDRESS']
    msg.set_content('Hejsa din klump')

    # Connect to SMTP server and send email
    # with SMTP('localhost', 1025) as smtp:
    with SMTP('asmtp.yousee.dk', port=587) as smtp:
        smtp.login(
            user=os.environ['EMAIL_ADDRESS'],
            password=getpass.getpass(prompt='Password: ', stream=None)
        )
        smtp.send_message(msg)

    print('Email sent')

    return True


if __name__ == '__main__':

    send_message()
