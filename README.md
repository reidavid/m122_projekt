# CryptoAnalytics

[LOGO]

# TOC

[TOC]

# Projektangaben

## Auftraggeber

Parisi Corrado

## Projektbeginn

14.06.2024

## Projektende/-abgabe

08.07.2024

## Beschreibung

Zeigt mithilfe der CoinMarketCap API verschiedene Marktdaten einer Kryptowährung der Wahl an.

## Projektteam

- Marzo Nevio
- Reichlin David

## Annahmen und Beschränkungen

- Anzahl der API Abfragen auf 10'000 beschränkt
- Keine kostenpflichtige API Services

## Terminvorgaben

| Datum           | Meilenstein                             |
|-----------------|-----------------------------------------|
| 14.06.          | Abgabe Projektantrag                    |
| 28.06.          | Abgabe Design (Aktivitätsdiagramm)      |
| 12.06. / 19.06. | Projektdemo & Abgabe Code mit Kommentar |
| 12.06. / 19.06. | Abgabe: Testbericht und Dokumentation   |

# Dependencies

- [wkhtmltopdf](https://wkhtmltopdf.org/)

# Features

- Kriegt verschiedene Kryptowährung-Informationen mit der CoinMarketAPI.
- Versendet Daten per Mail an benutzerdefinierte Empfänger.
- Daten die per Mails verschickt werden, werden formatiert für leserlichkeit und Übersicht.
- Mails können an mehreren Empfängern versendet werden.
- Wichtige Daten / Credentials werden extern gespeichert.
- Die Anzahl Währungen, von denen Daten geholt werden, kann mit Parametern angepasst werden.

# Showcase

Crypto Analytics benutzt die CoinMarketCap API, um aktuelle Informationen der Kryptowährungen anzuzeigen. Diese werden
dann formatiert und per Mail versendet.

Die Mail sieht wie folgt aus:

| ![KryptoInfo.png](src/assets/img/KryptoInfo.png) |
|:------------------------------------------------:|
|               Krypto Informationen               |

# Code

## Struktur

```
C:.
|   main.py
|   tree.txt
|   __init__.py
|   
+---assets
|   |   css.css
|   |   [LOGO]
|   |   
|   \---img
|           KryptoInfo.png
|           
+---log
|       error.log
|       log.log
|       __init__.py
|       
+---marketinfo
|   |   __init__.py
|   |   
|   \---data
|   |   |   get_data.py
|   |   |   __init__.py
|   |   |   
|   |           
|   \---main
|   |   |   main_app.py
|   |   |   __init__.py
|   |   |   
|   |           
|   \---utils
|   |   |   convert_pdf.py
|   |   |   logging.py
|   |   |   send_mail.py
|   |   |   __init__.py
|           
\---test
|       %tmp.txt
|       apitestscript.py
|       asdf.pdf
|       button_test.py
|       convert_pdf.py
|       dirtest.py
|       main_app.py
|       window.py
|       __init__.py
```

## Ausführung

### Main

Zur Ausführung wird ein ganz einfaches Skript benutzt, welches die Klasse [MainApp](#main_app) ausführt

```python
from marketinfo.main.main_app import MainApp

if __name__ == "__main__":
    MainApp()
```

### Main App

Hier werden alle benötigten Klassen / Funktionen für das Programm aufgerufen. Zusätzlich werden die Credentials in einer
externen JSON-Datei gespeichert und hier abgelesen, sodass ihre Werte weitergegeben werden können.

Auch wird ein Parameter (sys.argv) abgelesen und als "limit" an [GetData](#daten-einholen) weitergegeben. Limit
bezeichnet die Anzahl der
Kryptowährungen, von denen Informationen geholt werden.

```python
import json
from ..data.get_data import GetData
from ..utils.send_mail import SendMail
from ..utils.convert_pdf import ConvertPDF
from ..utils.logging import InitLog


class MainApp:
    def __init__(self):
        # Logging Initialisieren
        logger = InitLog().logger

        try:
            logger.info("Versuche, Daten aus CREDENTIALS.json auszulesen")
            with open("CREDENTIALS.json") as f:
                cred = json.load(f)
        except FileNotFoundError:
            logger.error('CREDENTIALS.json Datei nicht gefunden')
        except:
            logger.error('Daten von Credentials lesen ist fehlgeschlagen')

        # API Call mit externer JSON Datei und Skriptparameter als Limit
        data = GetData(cred, sys.argv[1]).formatted_data

        SendMail(cred, data)
        ConvertPDF(data)
```

## Daten

### Daten einholen

Mithilfe der CoinMarketCap API werden allesamt Daten der Kryptowährungen eingeholt. Zusätzlich werden diese in
HTML-Format formatiert und als Variable gespeichert, sodass sie in der [SendMail](#mail-senden)
und [ConvertPDF](#pdf-konvertieren) Klassen verwendet werden
können.

```python
import requests
from ..utils.logging import *


class GetData:
    def __init__(self, cred, limit=None):
        if limit is None:
            limit = 10

        logger = InitLog().logger

        api_key = cred['SECRET_KEY']
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        parameters = {
            'start': '1',
            'limit': limit,
            'convert': 'CHF'
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }

        try:
            response = requests.get(url, headers=headers, params=parameters)
        except requests.exceptions.ConnectionError:
            logger.error(f"API request an {url} fehlgeschlagen")

        data = response.json()

        self.formatted_data = ""  # wird in Mail und PDF benutzt

        self.FormatData(data)

    def FormatData(self, data):
        self.formatted_data += "<h1>Hier sind deine Krypto Informationen</h1>"

        for currency in data['data']:
            self.formatted_data +=
            f"""
                <table>
                    <tr>
                        <th>Name</th>
                        <td>{currency['name']}</td>
                    </tr>
                    <tr>
                        <th>Symbol</th>
                        <td>{currency['symbol']}</td>
                    </tr>s
                    <tr>
                        <th>Price</th>
                        <td>{currency['quote']['CHF']['price']:.2f} CHF</td>
                    </tr>
                    <tr>
                        <th>Volume Change in the last 24h</th>
                        <td>{currency['quote']['CHF']['volume_change_24h']:.2f} CHF</td>
                    </tr>
                    <tr>
                        <th>% Change in the last 24h</th>
                        <td>{currency['quote']['CHF']['percent_change_24h']:.2f} CHF</td>
                    </tr>
                    <tr>
                        <th>% Change in the last month</th>
                        <td>{currency['quote']['CHF']['percent_change_30d']:.2f} CHF</td>
                    </tr>
                    <tr>
                        <th>Market Cap</th>
                        <td>{currency['quote']['CHF']['market_cap']:.2f} CHF</td>
                    </tr>
                    <tr>
                        <th>Circulating Supply</th>
                        <td>{currency['circulating_supply']:.2f} CHF</td>
                    </tr>
                </table>
                """
```

## Dienstprogramme

### Mail senden

Mit dem SMTP Server von Gmail wird die Mail, die von [GetData](#daten-einholen) eingeholt und als HTML formatiert
werden. Die E-Mail Addresse, Passwort und Empfänger Addresse werden in der JSON-Datei bei [MainApp](#main_app)
eingeholt.

```python
import smtplib
from ..utils.logging import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    def __init__(self, cred, data):
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

        # send mail
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()
```

### Logging

Dieser Code bezeichnet eine einfache Logging Funktion, die Error Nachrichten in einer Datei speichert und sonstige
Nachrichten in einer andere. Diese Files befinden sich unter dem Ordner "log".

```python
import logging
import sys
import os


class InitLog:
    def __init__(self):
        # LOG-Files erstellen, falls nicht vorhanden
        if not os.path.exists("src/log/log.log"):
            with open("src/log/log.log", "w"): pass
        if not os.path.exists("src/log/error.log"):
            with open("src/log/error.log", "w"): pass

        # Configure logging
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[
                                logging.FileHandler("src/log/log.log"),
                                logging.StreamHandler(sys.stdout)
                            ])

        # Configure error logging
        error_handler = logging.FileHandler("src/log/error.log")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(error_handler)

        # Logger erstellen
        self.logger = logging.getLogger(__name__)
```

### PDF konvertieren

Mit diesem Code werden die in HTML formatierten Daten in [GetData](#daten-einholen) zu einem PDF gemacht mit der library
pdfkit. Hierfür wird wkhtmltopdf benötigt, ein webkit welches HTML zu PDF rendern kann. Damit diese Umwandlung
erfolgreich ist, sollte der absolute Pfad von wkhtmltopdf eingegeben werden.

```python
import pdfkit
from ..utils.logging import *


class ConvertPDF:
    def __init__(self, data):
        logger = InitLog().logger

        self.pdf = "_test.pdf"
        css = "assets/css.css"

        # Pfad zu wkhtmltopdf
        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        # PDF erstellen
        try:
            pdfkit.from_string(data, self.pdf, configuration=config, css=css)
        except:
            logger.error("Failed to convert String to PDF")
```

# License

Dieses Programm steht unter der [GNU General Public License v3.0](LICENSE)
