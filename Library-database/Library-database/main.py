import sqlite3
conn = sqlite3.connect('lib_database')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Library
(BookTitle text, LN text, Genre text, Location text, Quantity tinyint )''')
choice = input("Do you want to add to library database(1)")
if choice == 1:
    addBook = input("Bookname: ")
    addLN = input("Author's last name: ")
    addGenre = input("Genre of the book: ")
    addLocation = input("Where is this book found?: ")
    addQuantity = input("How many copies of this book do you have?: ")
    addTuple = (addBook, addLN, addGenre, addLocation, addQuantity)
    cursor.execute('''INSERT INTO Library)

