from .database import connect_db

def create_author(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO authors (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()