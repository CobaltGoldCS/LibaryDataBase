import sqlite3
conn = sqlite3.connect('lib_database')
cursor = conn.cursor()
#Only works if your database is empty, otherwise throws up an error message, which is pretty annoying
#cursor.execute('''CREATE TABLE Library
#(BookTitle text, LN text, Genre text, Location text, Quantity tinyint )''')
def main():
    #This is basically all functionallity for everything 
    choice = input("Do you want to add to library database(1), or find some book(2)?: ")
    if choice == 1:
        addBook = input("Bookname: ")
        addLN = input("Author's last name: ")
        addGenre = input("Genre of the book: ")
        addLocation = input("Where is this book found?: ")
        addQuantity = input("How many copies of this book do you have?: ")
        addTuple = (addBook, addLN, addGenre, addLocation, addQuantity)
        cursor.execute('INSERT INTO Library VALUES (?,?,?,?,?)', addTuple)
    # Still needs to use print to show the obtained information
    elif choice == 2:
        print("How do you want to search?\n")
        choice2 = input("Author's last name(1), Book name(2), Genre(3), or all: ")
        if choice2 == 1:
            useAuth = input("Author's last name: ")
            cursor.execute('SELECT * FROM Library WHERE symbol=?', useAuth)
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        if choice2 == 2:
            useBook = input("Book name: ")
            cursor.execute('SELECT * FROM Library WHERE symbol=?', useBook)
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        if choice2 == 3:
            useGenre = input("Genre: ")
            cursor.execute('SELECT * FROM Library WHERE symbol=?', useGenre)
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        if choice ==4:
            cursor.execute('SELECT * FROM Library')
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        else:
            print("Error")
            main()
    else:
        print("Error")
        main()
