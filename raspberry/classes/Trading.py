from models.Sensor import *
from datetime import datetime
import random
import requests

class Trading:
    def __init__(self):
        self.sensor = Sensor()

    def get_last_price(self):
        return self.sensor.last()

    def create_data(self, book_info):
        try:
            now = datetime.now()
            data = {
                'name': str(random.randint(1, 100)),
                'location': book_info['last'],
                'updated_at': now,
                'created_at': now
            }
            self.sensor.create(data)
        
        except Exception as e:
            print(f"AN ERROR OCURRED WHEN SAVING DATA: {e}")

    def get_daily_ema(self):
        return self.sensor.ema_daily()

    def get_request(self):
        response = requests.get("https://mecanicarubio.com/api/data/")
        return response.json()