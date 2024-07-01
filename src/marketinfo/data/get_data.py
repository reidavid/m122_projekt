import requests
import json


class GetData:
    def __init__(self):
        with open("C:/Users/rda.ADEON/Documents/git/module/m122_proj/src/CREDENTIALS.json") as f:
            d = json.load(f)

        api_key = d['SECRET_KEY']
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

        self.formatted_data = ""

        for currency in data['data']:
            self.formatted_data += f"Name: {currency['name']}/n"
            self.formatted_data += f"Symbol: {currency['symbol']}/n"
            self.formatted_data += f"Price: {currency['quote']['CHF']['price']:.2f} CHF/n"
            self.formatted_data += f"Volume Change in last 24h: {currency['quote']['CHF']['volume_change_24h']:.2f} CHF/n"
            self.formatted_data += f"% Change in last 24h: {currency['quote']['CHF']['percent_change_24h']:.2f} CHF/n"
            self.formatted_data += f"% Change in last month: {currency['quote']['CHF']['percent_change_30d']:.2f} CHF/n"
            self.formatted_data += f"Market cap: {currency['quote']['CHF']['market_cap']:.2f} CHF/n"
            self.formatted_data += f"Circulating supply: {currency['circulating_supply']:.2f} CHF/n"
            self.formatted_data += '---/n'
