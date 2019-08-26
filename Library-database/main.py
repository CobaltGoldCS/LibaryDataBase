import sqlite3
conn = sqlite3.connect('lib_database')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE Library
(BookTitle text, LN text, Genre text, Location text, Quantity tinyint )''')
choice = input("Do you want to add to library database(1)")
if choice == 1:
 addBook = input("Bookname")
 addLN = input("Author's last name")
 
 cursor.execute()


