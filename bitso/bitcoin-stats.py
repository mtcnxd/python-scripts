from classes import Datalog, BitsoProcessor
from Exceptions import ApiException
from rich.console import Console

logger = Datalog('backup.log')
console = Console()
processor = BitsoProcessor()

def init():
	try:
		console.print("SELECT AN OPTION:\n")
		console.print("[1] Create currency")
		console.print("[2] Bitcoin stats")
		console.print("[3] Close program")
		option = input("OPCION:")

		match option:
			case '1':
				values = {
					"price" : input("Price: "),
					"book" : input("Book: ")
				}

				currency = processor.set_currency(values)
				console.print(f"Currency created successfully:\n" 
							  f"Price: ${currency.price}\n"
							  f"Book: {currency.book}\n", style="green")
				return

			case '2':
				table = processor.table()
				console.print(table)
				return

			case '3':
				exit(1)
				return

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