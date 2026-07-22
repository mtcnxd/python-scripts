from Bitso import Bitso
from Datalog import Datalog
from datetime import datetime
import time

bitso = Bitso()

if __name__ == "__main__":
	while True:
		try:
			current_time = datetime.now().strftime("%H:%M:%S")
			book_info = bitso.get_book_info("btc_usdt")
			Datalog.write(f"{current_time} => Current price: {book_info['last']}")

			print(f"Current time: {current_time} => Current BTC price: {book_info['last']}")

		except Exception as error:
			print(f"Something went wrong: {error}")

		finally:
			time.sleep(30)