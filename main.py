import sqlite3
conn = sqlite3.connect('lib_database')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Library
(BookTitle text, LN text, Genre text, Location text, Quantity tinyint )''')
def main():
    choice = input("Do you want to add to library database(1), or find some book(2)?: ")
    if choice == 1:
        addBook = input("Bookname: ")
        addLN = input("Author's last name: ")
        addGenre = input("Genre of the book: ")
        addLocation = input("Where is this book found?: ")
        addQuantity = input("How many copies of this book do you have?: ")
        addTuple = (addBook, addLN, addGenre, addLocation, addQuantity)
        cursor.execute('INSERT INTO Library VALUES (?,?,?,?,?)', addTuple)
    elif choice == 2:
        print("How do you want to search?\n")
        choice2 = input("Author's last name(1), Book name(2), or Genre(3): ")
        if choice2 == 1:
            useAuth = input("Author's last name: ")
            cursor.execute('SELECT * FROM Library WHERE symbol=?', useAuth)
        if choice2 == 2:
            useBook = input("Book name: ")
            cursor.execute('SELECT * FROM Library WHERE symbol=?', useBook)
        if choice2 == 3:
            useGenre = input("Genre: ")
            cursor.execute('SELECT * FROM Library WHERE symbol=?', useGenre)
        else:
            print("Error")
            main()
    else:
        print("Error")
        main()
