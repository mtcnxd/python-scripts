import sqlite3

class DataBaseLite:
    def __init__(self):
        self.connection = sqlite3.connect('bitso_data.db')
        self.cursor = self.connection.cursor()

    def __del__(self):
        print(f"Connection closed")
        self.close()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bitso_data (
                id INTEGER PRIMARY KEY,
                price FLOAT,
                created_at DATE NOT NULL
            )
        ''')
        self.commit_changes()

    def commit_changes(self):
        self.connection.commit()

    def insert_data(self, data):
        price = data['price']
        created_at = data['created_at']
        self.cursor.execute("INSERT INTO bitso_data (price, created_at) VALUES (?, ?)", (price, created_at))

    def query_data(self):
        self.cursor.execute("SELECT * FROM bitso_data")
        return self.cursor.fetchall()

    def last(self):
        self.cursor.execute("SELECT * FROM bitso_data ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()

    def close(self):
        self.connection.close()