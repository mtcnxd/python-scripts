import json
import asyncio
import requests

class ApiService:
    def __init__(self):
        self.base_url = "https://edomains.com/"

    def get(self, endpoint, data) -> dict:
        response = requests.post(self.base_url + endpoint, json=data)

        if response is None:
            raise Exception("No response from server")

        return response.json()