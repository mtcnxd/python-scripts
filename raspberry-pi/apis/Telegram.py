import requests
import configs

class Telegram:
    def __init__(self):
        self.url = "https://api.telegram.org/" + configs.telegram_token + "/sendMessage"

    def send_message(self, message):
        try:
            response = requests.post(
                self.url,
                data={'chat_id': configs.chat_id, 'text':message, 'parse_mode':'Markdown'}
            )
            
            return response.json()
        
        except Exception as e:
            print(f"Telegram message error: {e}")
            return None