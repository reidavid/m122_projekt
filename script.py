import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# creates SMTP session
s = smtplib.SMTP('smtp-mail.outlook.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("m122dn@outlook.com", "SiXwm3mjSPb9GBJ")

# create a message
msg = MIMEMultipart()
msg['From'] = "m122dn@outlook.com"
msg['To'] = "neviomarzo.07@gmail.com"
msg['Subject'] = "Information Crypto"

# body of the email
body = "This is Crypto information."

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# sending the mail
s.sendmail(msg['From'], msg['To'], msg.as_string())

# terminating the session
s.quit()
