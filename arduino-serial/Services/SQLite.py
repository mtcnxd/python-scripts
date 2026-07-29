import sqlite3
import datetime

class SQLite:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_migrations()

    def __del__(self):
        self.connection.close()

    def create_migrations(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS temperature (
                id INTEGER PRIMARY KEY,
                time VARCHAR(50),
                temperature DECIMAL(10, 2),
                humidity DECIMAL(10, 2)
            )
        ''')

        self.connection.commit()

    def insert_data(self, count, value) -> None:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO temperature (time, temperature, humidity) VALUES (?, ?, ?)", (current_date, count, value))
        self.connection.commit()

    def query_fetch_all(self) -> list[dict]:
        self.cursor.execute("SELECT * FROM temperature")
        rows = self.cursor.fetchall()
        return rows

    def query_fetch_one(self, id) -> dict:
        self.cursor.execute("SELECT * FROM temperature WHERE id = ?", (id))
        row = self.cursor.fetchone()
        return row