import requests

class Bitso:
    def __init__(self):
        self.url = "https://api-stage.bitso.com/api/v3/ticker"

    def get_ticker(self):
        response = requests.get(self.url)

        if not response:
            raise Exception("Something went wrong while fetching data")

        return response.json()

    def get_book_info(self, book):
        response = self.get_ticker()

        for books in response['payload']:
            if books['book'] == book:
                return books
