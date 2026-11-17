from classes import DataBaseLite, Bitso
from rich.table import Table
from datetime import datetime
from Protocols.Currency import Currency

class BitsoProcessor:
	def __init__(self):
		self.sqllite = DataBaseLite()
		self.sqllite.create_tables()
		self.bitso = Bitso()

	def get_balance(self) -> list:
		response = self.bitso.get_balance()
		return [
			{
				'currency': currency['currency'],
				'amount' : currency['total']
			}
			
			for currency in response['balances'] if float(currency['total']) > 0.001
		]

	def set_currency(self, values: dict) -> Currency:
		currency = Currency()
		currency.set_price(values['price'])
		currency.set_book(values['book'])
		return currency

	def current_price(self) -> str:
		book_info = self.bitso.get_ticker("btc_usdt")
		
		if not book_info:
			raise Exception("Bitso API error")

		return book_info['last']

	def get_table_info(self) -> dict:
		current_price = self.current_price()
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
		table_info = self.get_table_info()

		last_price = float(table_info['last_price']['price'])
		current_price = float(table_info['current_price']['price'])

		table = Table()

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

		for balance in balances:
			table.add_row(balance['currency'], balance['amount'])

		return table

	def _to_currency(self, value: str) -> str:
		converted = float(value)
		return f"${converted:,.2f}"

	def _to_percentage(self, value) -> str:
		converted = float(value)
		return f"{converted:,.2f}%"