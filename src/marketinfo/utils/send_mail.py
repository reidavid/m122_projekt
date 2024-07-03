import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


class SendMail:
    def __init__(self, cred, data):

        email_address = cred['EMAIL_ADDRESS']
        email_password = cred['EMAIL_PASSWORD']
        recipient_address = cred['RECIPIENT_ADDRESS']

        # SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # security
        s.starttls()
        # Authentication
        s.login(email_address, email_password)

        # message
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = ", ".join(recipient_address)
        msg['Subject'] = "Hier sind deine Krypto Informationen"

        # body of the email
        body = data
        msg.attach(MIMEText(body, 'html'))

        # send mail
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
