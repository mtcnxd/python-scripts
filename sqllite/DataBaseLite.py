import sqlite3

class DataBaseLite:
    def __init__(self):
        self.connection = sqlite3.connect('my_database.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY,
                time TEXT NOT NULL,
                temperature INTEGER,
                humidity INTEGER,
                wind_speed INTEGER
            )
        ''')
        self.connection.commit()

    def insert_data(self, time, temperature, humidity, wind_speed):
        self.cursor.execute("INSERT INTO weather (time, temperature, humidity, wind_speed) VALUES (?, ?, ?, ?)", (time, temperature, humidity, wind_speed))
        self.connection.commit()

    def query_fetch_all(self):
        self.cursor.execute("SELECT * FROM weather")
        rows = self.cursor.fetchall()
        return rows

    def query_fetch_one(self, id):
        self.cursor.execute("SELECT * FROM weather WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        return row

    def delete_by_id(self, id):
        self.cursor.execute("DELETE FROM weather WHERE id = ?", (id,))
        self.connection.commit()
        return True

    def close(self):
        self.connection.close()