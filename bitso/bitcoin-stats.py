from select import select
from classes import Bitso, Datalog
from Exceptions import ApiException
from datetime import datetime
from time import sleep
from rich.console import Console
from rich.table import Table

bitso = Bitso()
datalog = Datalog('backup.log')

console = Console()

def to_currency(value: str) -> str:
	converted = float(value)
	return f"${converted:,.2f}"

def to_percentage(value):
	converted = int(value)
	return f"{converted:,.2f}%"

if __name__ == "__main__":
	try:
		current_time = datetime.now().strftime("%d-%m-%Y / %H:%M:%S")

		book_info = bitso.get_book_info("btc_usdt")

		datalog.write(f"{current_time} => Current price: {book_info['last']}")

		price_formatted = to_currency(book_info['last'])

		table = Table()

		table.add_column("key", style="dim")
		table.add_column("value")

		table.add_row("Date time", current_time)
		table.add_row("Bitcoin price", price_formatted, style="bold blue")
		table.add_row("Change last hour", price_formatted)
		table.add_row("Change last 24 hour", price_formatted)

		console.print(table)

	except ApiException as error:
		console.print(f"API Error: {error}")

	except Exception as error:
		console.print(f"Something went wrong: {error}")
		datalog.write(f"Error: {error}")

	finally:
		datalog.close()