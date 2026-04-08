import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Transaction(BaseModel):
    date: str
    amount: float
    description: str
    category: str

@app.get("/transactions")
def read_transactions():
    return get_transactions()

@app.delete("/transactions/{id}")
def delete_transactions(id: int):
    return delete_transaction(id)

@app.post("/transactions")
def create_transactions(t: Transaction):
    return add_transaction(t.date, t.amount, t.description, t.category)

@app.put("/transactions/{id}")
def edit_transaction(id: int, t: Transaction):
    return update_transaction(id, t.date, t.amount, t.description, t.category)


def get_connection():
    return sqlite3.connect('finance.db')

def add_transaction(date, amount, description, category):
    connection = sqlite3.connect('finance.db')
    cursor = connection.cursor()
    sql = '''insert into transactions(date, amount, description, category)
    values (?,?,?,?)'''
    cursor.execute(sql, (date, amount, description, category))
    connection.commit()

def get_transactions():
    connection = sqlite3.connect('finance.db')
    cursor = connection.cursor()
    sql = '''select * from transactions'''
    cursor.execute(sql)
    connection.commit()
    return cursor.fetchall()

def delete_transaction(id):
    connection = sqlite3.connect('finance.db')
    cursor = connection.cursor()
    sql = '''delete from transactions
    where id = ?'''
    cursor.execute(sql, (id,))
    connection.commit()

def update_transaction(id, date, amount, description, category):
    connection = sqlite3.connect('finance.db')
    cursor = connection.cursor()
    sql = '''update transactions
    set date=?, amount=?, description=?, category=?
    where id = ?'''
    cursor.execute(sql, (date, amount, description, category, id))
    connection.commit()