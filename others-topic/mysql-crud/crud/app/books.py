from .database import connect_db

def create_books(title, author_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author_id) VALUES (?,?)', (title, author_id))
    conn.commit()
    conn.close()

def update_books(book_id, new_title):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title = ? WHERE id = ?', (new_title, book_id))
    conn.commit()
    conn.close()

def delete_book_by_id(author_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE author_id = ?', (author_id,))
    conn.commit()
    conn.close()