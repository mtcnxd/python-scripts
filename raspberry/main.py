from apis.Bitso import Bitso
from apis.Telegram import Telegram
from classes.Trading import Trading
from Helpers import *

bitso = Bitso()
trading = Trading()

if __name__ == "__main__" :
    book_info = bitso.get_book_info("btc_usdt")
    last_price = trading.get_last_price()
    daily_ema = trading.get_daily_ema()

    percentage = calculate_percentage(book_info['last'], last_price['location'])

    print(f"Last price: {to_currency(last_price['location'])}")
    print(f"Current price: {to_currency(book_info['last'])}")
    print(f"Daily AVG: {to_currency(daily_ema['avg'])}")
    print(f"Percentage: {to_percentage(percentage)}")
    
    trading.create_data(book_info)

    Telegram().send_message(f"Current price: *{to_currency(book_info['last'])}* \n"
                            f"Last price *{to_currency(last_price['location'])}* \n"
                            f"Daily AVG: *{to_currency(daily_ema['avg'])}* \n"
                            f"The change represents: *{to_percentage(percentage)}*")
