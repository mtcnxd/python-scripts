import requests
from Exceptions import ApiException

class Bitso:
    def __init__(self):
        self.url = "https://api-stage.bitso.com/api/v3/ticker"

    def get_ticker(self) -> dict:
        response = requests.get(self.url)

        if not response:
            raise ApiException("Endpoint connection failed")

        return response.json()

    def get_book_info(self, book) -> dict:
        response = self.get_ticker()

        for books in response['payload']:
            if books['book'] == book:
                return books

        raise ApiException(f"Book {book} not found")
