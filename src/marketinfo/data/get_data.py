import requests
import json


class GetData:
    def __init__(self, cred, limit):
        api_key = cred['SECRET_KEY']
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

        parameters = {
            'start': '1',
            'limit': limit,
            'convert': 'CHF'  # Change the currency to CHF
        }

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }

        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        self.formatted_data = ""

        self.FormatData(data)

    def FormatData(self, data):

        self.formatted_data += "<body>"

        for currency in data['data']:
            self.formatted_data += \
                f"""
                <div style="padding:20px; color:powderblue; border-radius:25px;>
                    <h2>Name: {currency['name']}</h2>
                    <p><b>Symbol:</b> {currency['symbol']}</p>
                    <p><b>Price:</b> {currency['quote']['CHF']['price']:.2f} CHF</p>
                    <p><b>Volume Change in the last 24h:</b> {currency['quote']['CHF']['volume_change_24h']:.2f} CHF</p>
                    <p><b>% Change in the last 24h:</b> {currency['quote']['CHF']['percent_change_24h']:.2f} CHF</p>
                    <p><b>% Change in the last month:</b> {currency['quote']['CHF']['percent_change_30d']:.2f} CHF</p>
                    <p><b>Market Cap:</b> {currency['quote']['CHF']['market_cap']:.2f} CHF</p>
                    <p><b>Circulating Supply:</b> {currency['circulating_supply']:.2f} CHF</p>
                </div>
                """

        self.formatted_data += "</body>"
