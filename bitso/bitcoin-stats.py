from classes import Datalog, BitsoProcessor
from Exceptions import ApiException
from rich.console import Console

logger = Datalog('backup.log')
console = Console()
processor = BitsoProcessor()

def init():
	try:
		table = processor.table()
		console.print(table)

		currencies = ['bitcoin', 'etherium', 'bat', 'solana', 'litecoin', 'dutch']

		for currency in currencies:
			currency = processor.set_currency({
				'price': '100',
				'book': currency + '_mxn'
			})

			# console.print(currency.price)

	except ApiException as error:
		logger.write(f"API Error: {error}")
		console.print(f"API Error: {error}")

	except Exception as error:
		logger.write(f"Global Error: {error}")
		console.print(f"Something went wrong: {error}")

	finally:
		logger.close()
		exit(1)


if __name__ == '__main__':
	init()