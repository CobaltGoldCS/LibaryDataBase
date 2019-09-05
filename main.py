import sqlite3

conn = sqlite3.connect('lib_database')
cursor = conn.cursor()
#cursor.execute('''CREATE TABLE Library (Bookname text, Auth text, Genre text, Location text, Quantity tinyint)''')
def main():
    """Where all magic happens folks"""
    choice = input("Add (1), find (2)?: ")
    if choice == "1":
        addBook = input("Bookname: ")
        addLN = input("Author's last name: ")
        addGenre = input("Genre of the book: ")
        addLocation = input("Where is this book found?: ")
        addQuantity = input("How many copies of this book do you have?: ")
        addTuple = [(addBook), (addLN), (addGenre), (addLocation), (addQuantity)]
        cursor.execute('''INSERT INTO Library (Bookname, Auth, Genre, Location, Quantity) VALUES (?,?,?,?,?)''', addTuple,)
        conn.commit()
        print("Done, thank you")
        conn.close()
    # Still needs to use print to show the obtained information
    elif choice == "2":
        print("How do you want to search?\n")
        choice2 = input("Last name(1), Book name(2), Genre(3), or all(4): ")
        if choice2 == "1":
            addLN = input("Author's last name: ")
            cursor.execute('SELECT * FROM Library WHERE Auth=?', (addLN,))
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        if choice2 == "2":
            addBook = input("Bookname: ")
            cursor.execute('SELECT * FROM Library WHERE Bookname=?', (addBook,))
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        if choice2 == "3":
            addGenre = input("Genre of the book: ")
            cursor.execute('SELECT * FROM Library WHERE Genre=?', (addGenre,))
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
        if choice2 == "4":
            cursor.execute('SELECT * FROM Library')
            rows = cursor.fetchall()
            for row in rows:
                print(rows)
    # This deletes a book you search for with Bookname
    elif choice ==  "3":
      delete = input("Which book do you want to delete?: ")
      cursor.execute("DELETE FROM Library WHERE Bookname=?", (delete,))
      conn.commit()
      print(delete, "deleted, thank you.")
      conn.close()


    else:
        print("Error")
        main()


main()
