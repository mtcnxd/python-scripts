from select import select
from classes import Bitso, Datalog
from Exceptions import ApiException
from datetime import datetime
from time import sleep

bitso = Bitso()
datalog = Datalog('backup.log')

if __name__ == "__main__":
	while True:
		try:
			current_time = datetime.now().strftime("%H:%M:%S")

			book_info = bitso.get_book_info("btc_usdt")

			datalog.write(f"{current_time} => Current price: {book_info['last']}")

			print(f"Current time: {current_time} => Current BTC price: {book_info['last']}")

		except ApiException as error:
			print(f"API Error: {error}")

		except Exception as error:
			print(f"Something went wrong: {error}")
			datalog.write(f"Error: {error}")

		finally:
			datalog.close()
			sleep(10)