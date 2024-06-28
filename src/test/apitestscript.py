import requests
import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Replace 'your_api_key' with your actual CoinMarketCap API key
api_key = 'e9c3db07-eb1b-42d4-81d5-517aab9e31fd'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start': '1',
    'limit': '10',
    'convert': 'CHF'  # Change the currency to CHF
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

response = requests.get(url, headers=headers, params=parameters)
data = response.json()

# Store the formatted string in a variable
formatted_data = ""

for currency in data['data']:
    formatted_data += f"Name: {currency['name']}\n"
    formatted_data += f"Symbol: {currency['symbol']}\n"
    formatted_data += f"Price: {currency['quote']['CHF']['price']:.2f} CHF\n"
    formatted_data += '---\n'

# Print the variable
print(formatted_data)

# E-Mail credentials (should be stored securely, not in plain text)
email_address = "m122projekt@gmail.com"
email_password = "vkkt syog uxnl gixq "
recipient_address = "neviomarzo.07@gmail.com"

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(email_address, email_password)

# create a message
msg = MIMEMultipart()
msg['From'] = email_address
msg['To'] = recipient_address
msg['Subject'] = "Test"

# body of the email
body = formatted_data

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# sending the mail
s.sendmail(msg['From'], msg['To'], msg.as_string())

# terminating the session
s.quit()
