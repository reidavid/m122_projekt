import requests
import json


class GetData:
    def __init__(self, cred, limit=10):
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

        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()

        self.formatted_data = ""  # wird in Mail und PDF benutzt

        self.FormatData(data)

    def FormatData(self, data):
        self.formatted_data += "<h1>Hier sind deine Krypto Informationen</h1>"

        for currency in data['data']:
            self.formatted_data += \
                f"""
                <table>
                    <tr>
                        <th>Name</th>
                        <td>{currency['name']}</td>
                    </tr>
                    <tr>
                        <th>Symbol</th>
                        <td>{currency['symbol']}</td>
                    </tr>
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
