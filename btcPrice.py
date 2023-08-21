import requests
import json
import pyttsx3

class CoinDesk:
    def __init__(self):
        self.engine = pyttsx3.init()

    def get_btc_price(self):
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = json.loads(response.text)
        btc_price = data['bpi']['USD']['rate']
        btc_price = int(float(btc_price.replace(',', '')))
        self.engine.say('Bitcoin price is {}'.format(btc_price))
        print('Bitcoin price is {}'.format(btc_price))
        self.engine.runAndWait()

coin_desk = CoinDesk()
coin_desk.get_btc_price()