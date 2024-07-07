import smtplib
import os
from ..utils.logging import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class SendMail:
    def __init__(self, cred, data, attachment_path="/home/nevio/m122_projekt/src/_test.pdf"):
        logger = InitLog().logger

        try:
            logger.info("Getting Email Credentials...")
            email_address = cred['EMAIL_ADDRESS']
            email_password = cred['EMAIL_PASSWORD']
            recipient_address = cred['RECIPIENT_ADDRESS']
        except:
            logger.error("Email Credentials empty")

        # SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # security
        s.starttls()
        # Authentication
        try:
            logger.info("Authenticating...")
            s.login(email_address, email_password)
        except:
            logger.error("Authentication failed")

        # message
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = ", ".join(recipient_address)
        msg['Subject'] = "Hier sind deine Krypto Informationen"

        # body of the email
        body = data
        msg.attach(MIMEText(body, 'html'))

        # attach file
        if attachment_path:
            attachment = open(attachment_path, "rb")

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)

            # Extract filename from the path and use it in the header
            filename = os.path.basename(attachment_path)
            part.add_header('Content-Disposition', f'attachment; filename={filename}')

            msg.attach(part)

        # send mail
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
