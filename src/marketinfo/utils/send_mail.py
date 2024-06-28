import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json


class SendMail:
    def __init__(self, data):

        with open("C:/Users/reich/IdeaProjects/m122_projekt/src/CREDENTIALS.json") as f:
            d = json.load(f)

        email_address = d['EMAIL_ADDRESS']
        email_password = d['EMAIL_PASSWORD']
        recipient_address = d['RECIPIENT_ADDRESS']

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
        msg['Subject'] = "Hier sind deine Krytpo Informationen"

        # body of the email
        body = data
        msg.attach(MIMEText(body, 'plain'))

        # send mail
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
