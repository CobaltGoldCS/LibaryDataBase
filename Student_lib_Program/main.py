import tkinter
import sqlite3
from tkinter import messagebox, ttk
from pathlib import Path
class Mainclass():

    def __init__(self, mainicon, database):
        self.iconpath= mainicon
        self.dataPath = database
        self.functionality = functionality(self.iconpath, self.dataPath)
    
    def searchMenu(self):
        #Defining container
        searchContainer= tkinter.Tk()
        searchContainer.iconbitmap(str(self.iconpath))
        searchContainer.title("Search For a book")
        searchFrame = tkinter.Frame(searchContainer)
        searchFrame.grid(column=2)
        #Text Labels
        bookLabel = tkinter.Label(searchFrame, text="Book")
        bookLabel.grid(row=1)
        AuthLabel = tkinter.Label(searchFrame, text="Author Name")
        AuthLabel.grid(row=2)
        #User input widgets
        bookSearch = tkinter.Entry(searchFrame)
        bookSearch.grid(row=1, column=1)
        AuthSearch = tkinter.Entry(searchFrame)
        AuthSearch.grid(row=2, column=1)
        #Button + functionallity
        searchButton = tkinter.Button(searchFrame, text= "Search for Book", command= lambda: self.functionality.searchBook(bookSearch, AuthSearch, searchContainer), width = 40)
        searchButton.grid(row=3,columnspan=2)
        searchContainer.mainloop()

class functionality():
  def __init__(self, mainicon, database):
    self.iconpath= mainicon
    self.dataPath = database

  def selectItem(self, event):
    #------When an item is selected in the search output section, this is collected---------#
    curItem = self.tree.selection()[0]
    valueTuple = self.tree.item(curItem)['values']
    messagebox.showinfo("AAI Library", valueTuple[1]+ " by "+ valueTuple[2] + ' can be found in '+  valueTuple[4])

  def searchBook(self, BookName, AuthName, searchContainer):
    conn = sqlite3.connect(self.dataPath)
    cursor = conn.cursor()
    name = BookName.get()
    AuthorName = AuthName.get()
#-----------------------------------------Initialising the search window--------------------#
    self.searchWindow = tkinter.Tk()
    self.resultFrame = tkinter.Frame(self.searchWindow)
    self.tree = ttk.Treeview(self.resultFrame,height=10, column=("column 1", "column 2", "column 3", "column 4", "column 5", "column 6"), show='headings')
    self.searchWindow.title("Search Results")
    self.searchWindow.iconbitmap(self.iconpath)
    self.resultFrame.grid(column=5)
    self.tree.grid(columnspan=6)
    self.tree.heading('#1', text = "id", anchor= tkinter.CENTER)
    self.tree.heading('#2', text = 'Book Name', anchor= tkinter.CENTER)
    self.tree.heading('#3', text="Author Name", anchor= tkinter.CENTER)
    self.tree.heading('#4', text="Genre", anchor= tkinter.CENTER)
    self.tree.heading('#5', text="Location", anchor= tkinter.CENTER)
    self.tree.heading('#6', text="Available", anchor= tkinter.CENTER)
#------------------------------------------Finds data in database ---------------------------#
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
      query="SELECT * FROM Library"
      params = None
#---------------------------------Shows all of the data asked for ----------------------------#
    records = self.tree.get_children()
    for element in records:
      self.tree.delete(element)
    if params != None:
      db_rows = cursor.execute(query, params)
    else:
      db_rows = cursor.execute(query)
    for row in db_rows:
      self.tree.insert("", tkinter.END, values=row)
    conn.close()  
    self.tree.grid()
#-----------------Binds the selectItem function when the user selects an item-----------------#
    self.tree.bind('<ButtonRelease-1>', self.selectItem) 


if __name__ == "__main__":
    run = Mainclass((Path.cwd() / 'icons' / 'mag.ico'), (Path.cwd() / 'library_database.db'))
    run.searchMenu()