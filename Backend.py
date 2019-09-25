import tkinter
import sqlite3
from functools import partial
from tkinter import messagebox, ttk
iconpath= r'C:\Users\Dylan\Downloads\LibaryDataBase-master\LibaryDataBase-master\mag.ico'
class functionality():
  
  
  
  def createBook(self, BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry):
    conn = sqlite3.connect('lib_database')
    cursor = conn.cursor()
    name = BookEntry.get()
    location= locationEntry.get()
    genre=genreEntry.get()
    LN = LNEntry.get()
    quantity = quantityEntry.get()
    cursor.execute("SELECT * FROM Library")
    rows = cursor.fetchall()
    id = 0
    print("All current info")
    for row in rows:
      id = id+1
      print(row)

    addTuple = [(int(id)), (str(name)), (str(LN)), (str(genre)), (str(location)), (quantity)]
    cursor.execute('INSERT INTO Library VALUES (?,?,?,?,?,?)', addTuple)
    conn.commit()
    messagebox.showinfo("Success", "Book successfully added")
    BookEntry.delete(0, 'end')
    locationEntry.delete(0, 'end')
    genreEntry.delete(0, 'end')
    LNEntry.delete(0, 'end')
    quantityEntry.delete(0, 'end')
    conn.close()
  
  
  
  def searchBook(self, BookName, AuthName):
    conn = sqlite3.connect('lib_database')
    cursor = conn.cursor()
    name = BookName.get()
    AuthorName = AuthName.get()
    searchWindow = tkinter.Tk()
    searchWindow.title("Search Results")
    searchWindow.iconbitmap(iconpath)
    resultFrame = tkinter.Frame(searchWindow)
    resultFrame.grid(column=5)
    
    tree= ttk.Treeview(resultFrame,height=10, column=("column 1", "column 2", "column 3", "column 4", "column 5"), show='headings')
    tree.grid(columnspan=5)
    tree.heading('#1', text = "id", anchor= tkinter.CENTER)
    tree.heading('#2', text = 'Book Name', anchor= tkinter.CENTER)
    tree.heading('#3', text="Author Name", anchor= tkinter.CENTER)
    tree.heading('#4', text="Genre", anchor= tkinter.CENTER)
    tree.heading('#5', text="Location", anchor= tkinter.CENTER)
    if len(name) != 0 and len(AuthorName) == 0:
      query = "SELECT * FROM Library WHERE BookName=?"
      params = (name,)
    elif len(name) == 0 and len(AuthorName) != 0:
      query = "SELECT * FROM Library WHERE AuthorName=?"
      params= (AuthorName,)
    elif len(name) != 0 and len(AuthorName) != 0:
      query = "SELECT * FROM Library WHERE BookName=? AND AuthorName=?"
      params= (name, AuthorName)
    else:
      query=None
      params=None
    records = tree.get_children()
    for element in records:
      tree.delete(element)
    if name != 'ALL':
      db_rows = cursor.execute(query, params)
    for row in db_rows:
      tree.insert("", tkinter.END, values=row)
    conn.close()  
    tree.grid()
  
  
  
  def delete(self, Book, Author, container):
    BookName = Book.get()
    AuthName = Author.get()
    bigTuple = (BookName, AuthName)
    conn = sqlite3.connect('lib_database')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Library WHERE BookName=? AND AuthorName=?", bigTuple,)
    sure = messagebox.askyesno("Are you sure", "Are you sure you want to delete this book?")
    if sure == True:
      conn.commit()
      messagebox.showinfo("Deleted", BookName+" deleted")
      conn.close()
    else:
      conn.close()
  
  def quit(self, container):
    container.destroy()