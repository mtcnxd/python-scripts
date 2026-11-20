from multiprocessing.util import log_to_stderr
from classes import DataBaseLite, Bitso
from rich.table import Table
from rich.panel import Panel
from datetime import datetime
from Protocols.Currency import Currency

class BitsoProcessor:
	def __init__(self):
		self.sqllite = DataBaseLite()
		self.bitso = Bitso()

		# Create DB tables
		self.sqllite.create_tables()

		# Private Properties
		self._ticker = self.bitso.get_ticker()
		self._total = 0.0

	def get_balance(self) -> list:
		response = self.bitso.get_balance()

		result = []
		for currency in response['balances']:
			if float(currency['total']) > 0.001:
				book_info = next(
					(item for item in self._ticker if item['book'] == f"{currency['currency']}_mxn"), None
				)

				if book_info is None:
					continue

				result.append({
					'currency': currency['currency'],
					'amount' : currency['total'],
					'value' : float(book_info['last']) * float(currency['total'])
				})

		return result

	def set_currency(self, values: dict) -> Currency:
		currency = Currency()
		currency.set_price(values['price'])
		currency.set_book(values['book'])
		return currency

	def get_table_info(self) -> dict:
		book_info = next(
			(item for item in self._ticker if item['book'] == 'btc_usdt'), None
		)

		if book_info is None:
			raise Exception("Response does not have selected book")

		current_price = book_info['last']
		last_price = self.sqllite.last()

		self.sqllite.insert_data({
			'price': current_price,
			'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		})

		self.sqllite.commit_changes()

		return {
			'current_price': {
				"price": current_price,
				"time" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			},
			'last_price': {
				"price": last_price[1],
				"time" : last_price[2]
			}
		}

	def table_ticker(self) -> Table:
		table_info: dict = self.get_table_info()

		last_price = float(table_info['last_price']['price'])
		current_price = float(table_info['current_price']['price'])

		table: Table = Table()

		table.add_column("Name", style="dim")
		table.add_column("Value")
		table.add_column("Date Time")

		table.add_row("Current Price", 
			self._to_currency(current_price),
			table_info['current_price']['time']
		)
		
		table.add_row("Last Price", 
			self._to_currency(last_price),
			table_info['last_price']['time']
		)

		change : float = (current_price - last_price)
		percentage: float = (change / last_price) * 100

		table.add_row("Change", 
			self._to_currency(change),
			self._to_percentage(percentage),
			style="red" if change < 0 else "green"
		)

		return table

	def table_balance(self) -> Table:
		balances: list = self.get_balance()

		table: Table = Table()

		table.add_column("Currency")
		table.add_column("Amount", style="green")
		table.add_column("Value")

		for balance in balances:
			self._total = self._total + float(balance['value'])
			table.add_row(balance['currency'], balance['amount'], self._to_currency(balance['value']))

		return table

	def get_total(self) -> Panel:
		return Panel(self._to_currency(self._total), title="Total", subtitle="Total Value of all Currencies")

	def _to_currency(self, value: str) -> str:
		converted = float(value)
		return f"${converted:,.2f}"

	def _to_percentage(self, value) -> str:
		converted = float(value)
		return f"{converted:,.2f}%"
