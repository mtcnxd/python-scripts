from classes import Datalog, BitsoProcessor
from Exceptions import ApiException
from time import sleep
from rich.console import Console
from rich.table import Table

logger = Datalog('backup.log')
console = Console()
procesor = BitsoProcessor()

if __name__ == "__main__":
	try:
		bitcoin_current = procesor.current_price()
		bitcoin_last = procesor.last_price()

		# print(bitcoin_last)

		table = Table()

		table.add_column("Name", style="dim")
		table.add_column("value")

		table.add_row("Date time", "")
		table.add_row("Current price", bitcoin_current, style="bold blue")
		table.add_row("Change last hour", bitcoin_current)
		table.add_row("Change last 24 hour", bitcoin_current)

		console.print(table)

	except ApiException as error:
		logger.write(f"API Error: {error}")
		console.print(f"API Error: {error}")

	except Exception as error:
		logger.write(f"Global Error: {error}")
		console.print(f"Something went wrong: {error}")

	finally:
		logger.close()