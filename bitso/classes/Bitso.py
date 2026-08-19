import requests
from Exceptions import ApiException

class Bitso:
    def __init__(self):
        self.base_url = "https://api-stage.bitso.com"

    def _get_ticker(self) -> dict:
        response = requests.get(f"{self.base_url}/api/v3/ticker")

        if not response:
            raise ApiException(f"Endpoint connection failed: {response.text}")

        return response.json()

    def get_book_info(self, book) -> dict:
        response = self._get_ticker()

        for books in response['payload']:
            if books['book'] == book:
                return books

        raise ApiException(f"Book {book} not found")

    def get_orders(self) -> dict:
        pass

    def get_trades(self) -> dict:
        pass