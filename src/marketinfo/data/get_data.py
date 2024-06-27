from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import *


class GetData:
    def __init__(self, cr):

        # Read API-Key
        with open('C:/Users/rda.ADEON/Documents/git/module/m122_proj/SECRET_KEY') as f:
            d = json.load(f)

        url = 'https://pro-api.coinmarketcap.com/cryptocurrency/listing/map'
        parameters = {
            # 'start': '1',
            # 'limit': '5000',
            # 'symbol': cr,
            # 'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': d['SECRET_KEY']
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            self.data = json.loads(response.text)
            print(self.data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
