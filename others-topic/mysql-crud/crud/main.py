from app.database import connect_db, create_table
from app.authors import create_author
from app.books import create_books, update_books, delete_book_by_id


def display_menu():
    print("choose an option:--")
    print("1, create authors")
    print("2, create books")
    print("3, update books")
    print("4, delete bookm by id")
    print("5, Exit the program")

def main():
    conn = connect_db()
    create_table(conn)

    while True:

        display_menu()
        choice  = input("enter you choice: ")

        if choice == '1':

            create_author("Akhil sharma")

        if choice == '2':

            create_books("sanathan dharma", 1)
            create_books("shikh dharm", 2)

        if choice == '3':
            book_id = int(input("enter you book id to update: "))
            new_title = input("enter you new title to update: ")

            update_books(book_id, new_title)

        if choice == '4':
            author_id = int(input("enter you book id to delete: "))
            delete_book_by_id(author_id)
        
        if choice == '5':
            print("Exiting the program")
            break
        
        else:
            print("Invalid choice!!")

    conn.close()

if __name__ == "__main__":
    main()