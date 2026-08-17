from classes import DataBaseLite, Bitso
from rich.table import Table
from datetime import datetime

class BitsoProcessor:
	def __init__(self):
		self.sqllite = DataBaseLite()
		self.sqllite.create_table()
		self.bitso = Bitso()

	def current_price(self) -> dict:
		book_info = self.bitso.get_book_info("btc_usdt")
		
		if not book_info:
			raise Exception("Bitso API error")

		self.sqllite.insert_data({
			'price': book_info['last'],
			'created_at': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
		})

		self.sqllite.commit_changes()

		return self._to_currency(book_info['last'])

	def last_price(self):
		return self.sqllite.last()

	def _to_currency(self, value: str) -> str:
		converted = float(value)
		return f"${converted:,.2f}"

	def _to_percentage(self, value) -> str:
		converted = float(value)
		return f"{converted:,.2f}%"