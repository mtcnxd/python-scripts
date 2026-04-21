from apis import Bitso, Telegram
from services import BitsoService
from Helpers import *
#import logging

bitso = Bitso()
trading = BitsoService()

#logging.basicConfig(
#    filename='logs/output.log',
#    level=logging.INFO,
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#)
if __name__ == "__main__" :
    #logger = logging.getLogger(__name__)
    book_info = bitso.get_book_info("btc_usdt")

    if book_info is None:
        Telegram().send_message(f"Error: No se pudo obtener la informacion del book")
        #logger.info(f"Error: No se pudo obtener la informacion del book")
        exit(1)

    last_price = trading.get_last_price()
    daily_ema = trading.get_daily_ema()

    percentage = calculate_percentage(book_info['last'], last_price['location'])

    #logger.info(f"Last price: {to_currency(last_price['location'])}")
    #logger.info(f"Current price: {to_currency(book_info['last'])}")
    #logger.info(f"Daily AVG: {to_currency(daily_ema['avg'])}")
    #logger.info(f"Percentage: {to_percentage(percentage)}")

    trading.create_data(book_info)

    Telegram().send_message(f"Current price: *{to_currency(book_info['last'])}* \n"
                            f"Last price *{to_currency(last_price['location'])}* \n"
                            f"Daily AVG: *{to_currency(daily_ema['avg'])}* \n"
                            f"The change represents: *{to_percentage(percentage)}*")
