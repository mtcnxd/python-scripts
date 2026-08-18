from classes import Datalog, BitsoProcessor
from Exceptions import ApiException
from rich.console import Console

logger = Datalog('backup.log')
console = Console()
processor = BitsoProcessor()

if __name__ == "__main__":
	try:
		table = processor.table()
		console.print(table)

	except ApiException as error:
		logger.write(f"API Error: {error}")
		console.print(f"API Error: {error}")

	except Exception as error:
		logger.write(f"Global Error: {error}")
		console.print(f"Something went wrong: {error}")

	finally:
		logger.close()