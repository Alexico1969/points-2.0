import sqlite3
connection = sqlite3.connect('database/points.db', check_same_thread=False)
sql = connection.cursor()
