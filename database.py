import sqlite3

connection = sqlite3.connect('finance.db')
cursor = connection.cursor()
sql = '''CREATE TABLE if not exists transactions (
    id integer primary key autoincrement,
    date text,
    amount real,
    description text,
    category text);'''
cursor.execute(sql)
connection.commit()
