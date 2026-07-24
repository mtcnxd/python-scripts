import sqlite3

class DataBaseLite:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY,
                name VARCHAR(50),
                value VARCHAR(50)
            )
        ''')
        self.connection.commit()

    def insert_data(self, name, value):
        self.cursor.execute("INSERT INTO settings (name, value) VALUES (?, ?)", (name, value))
        self.connection.commit()

    def query_fetch_all(self):
        self.cursor.execute("SELECT * FROM settings")
        rows = self.cursor.fetchall()
        return rows

    def query_fetch_one(self, id):
        self.cursor.execute("SELECT * FROM settings WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        return row

    def delete_by_id(self, id):
        self.cursor.execute("DELETE FROM settings WHERE id = ?", (id,))
        self.connection.commit()
        return True

    def close(self):
        self.connection.close()