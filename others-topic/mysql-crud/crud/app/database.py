import sqlite3

def connect_db():
    conn = sqlite3.connect('data/library.db')
    return conn

def create_table(conn):
    cussor = conn.cursor()
    cussor.execute('CREATE TABLE IF NOT EXISTS AUTHORS (id INTEGER PRIMARY KEY, name TEXT NOT NULL)')
    cussor.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author_id INTEGER, FOREign KEY (author_id) REFERENCES authors(id))')
    conn.commit()