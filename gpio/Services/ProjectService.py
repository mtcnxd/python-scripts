from datetime import datetime
import requests
import json
import telegram_send
import asyncio

class ProjectService:
    def __init__(self):
        url = "http://www.mecanicarubio.com/api"
        
    def start(self, number) -> float:
        return number * 2.4
    
    def get_current_time(self):
        return datetime.now()
    
    def convert_to_json(self, data):
        return json.dumps(data)
    
    async def send_telegram(self, message):
        await telegram_send.send(messages=["Hola"])
