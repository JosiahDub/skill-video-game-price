# built-in
import json
# 3rd party
import requests
# Our local stuff
from config import API_KEY


class PriceGuide:
    def __init__(self):
        self.product_api = 'https://www.pricecharting.com/api/product'
        self.search_api = 'https://www.pricecharting.com/api/products'

    def search_games(self, query):
        result = requests.get(self.search_api, params={'t': API_KEY,
                                                       'q': query})
        try:
            content = json.loads(result.content.decode("utf-8"))["products"]
        except json.decoder.JSONDecodeError:
            # Probably a bad url
            content = []
        except KeyError:
            # No match
            content = []
        return content

    def game_info(self, query):
        result = requests.get(self.product_api, params={'t': API_KEY,
                                                        'q': query})
        try:
            content = json.loads(result.content.decode("utf-8"))
        except json.decoder.JSONDecodeError:
            # Probably a bad url
            content = {}
        else:
            if content["status"] != "success":
                content = {}
        return content
