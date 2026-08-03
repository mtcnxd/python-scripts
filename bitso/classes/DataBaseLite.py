import sqlite3

class DataBaseLite:
    def __init__(self):
        self.connection = sqlite3.connect('bitso_data.db')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bitso_data (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        self.connection.commit()

    def insert_data(self, name, age):
        self.cursor.execute("INSERT INTO bitso_data (name, age) VALUES (?, ?)", (name, age))
        self.connection.commit()

    def query_data(self):
        self.cursor.execute("SELECT * FROM bitso_data")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.connection.close()