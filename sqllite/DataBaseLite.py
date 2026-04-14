import sqlite3

class DataBaseLite:
    def __init__(self):
        self.connection = sqlite3.connect('my_database.db')
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

    def query_data(self):
        self.cursor.execute("SELECT * FROM weather")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.connection.close()