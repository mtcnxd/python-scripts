from classes import DataBaseLite, Bitso
from rich.table import Table
from datetime import datetime
from Protocols.Currency import Currency

class BitsoProcessor:
	def __init__(self):
		self.sqllite = DataBaseLite()
		self.sqllite.create_tables()
		self.bitso = Bitso()

	def set_currency(self, values: dict) -> Currency:
		currency = Currency()
		currency.set_price(values['price'])
		currency.set_book(values['book'])
		return currency

	def current_price(self) -> str:
		book_info = self.bitso.get_book_info("btc_usdt")
		
		if not book_info:
			raise Exception("Bitso API error")

		return book_info['last']

	def get_table_info(self) -> dict:
		current_price = self.current_price()
		last_price = self.sqllite.last()

		self.sqllite.insert_data({
			'price': current_price,
			'created_at': datetime.now().strftime("%H:%M:%S")
		})

		self.sqllite.commit_changes()

		return {
			'current_price': {
				"price": current_price,
				"time" : datetime.now().strftime("%H:%M:%S")
			},
			'last_price': {
				"price": last_price[1],
				"time" : last_price[2]
			}
		}

	def table(self) -> Table:
		table_info = self.get_table_info()

		table = Table()

		table.add_column("Name", style="dim")
		table.add_column("Value")
		table.add_column("Time")

		table.add_row("Current Price", 
			self._to_currency(table_info['current_price']['price']),
			table_info['current_price']['time'], 
			style="red"
			)
		
		table.add_row("Last Price", 
			self._to_currency(table_info['last_price']['price']),
			table_info['last_price']['time']
			)

		change = (float(table_info['current_price']['price']) - float(table_info['last_price']['price']))

		percentage = change / table_info['last_price']['price']

		table.add_row("Change from last price", 
			self._to_currency(change),
			self._to_percentage(percentage)
			)

		return table

	def _to_currency(self, value: str) -> str:
		converted = float(value)
		return f"${converted:,.2f}"

	def _to_percentage(self, value) -> str:
		converted = float(value)
		return f"{converted:,.2f}%"