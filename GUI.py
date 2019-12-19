import tkinter
from Backend import functionality
from functools import partial
from sqlite3 import connect, Cursor
"""
TO DO list
- Beautify the GUI
- Reformat all code to use proper syntax for classes to get rid of partial
- Use cwd() to make code runnable on different computers OR put it in installation instructions

"""
conn = connect('lib_database')
cursor = conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS Library (Index int, Bookname text, AuthorName text, Genre text, Location text, Quantity tinyint)''')
conn.close()


iconPath = r'C:\Users\Dylan\Downloads\LibaryDataBase-master\LibaryDataBase-master\icon.ico'

class menu():
  
  
  
  def mainMenu(self):
    container = tkinter.Tk()
    container.iconbitmap(iconPath)
    container.title("AAI Library")
    container.minsize(300,100)
    mainFrame = tkinter.Frame(container)
    mainFrame.grid(column = 2)
    addAction_Arg = partial(menu.addMenu, self)
    searchAction_Arg = partial(menu.searchMenu, self)
    deleteAction_Arg = partial(menu.deleteMenu, self)
    quitAction_Arg = partial(functionality.quit, self, container)
    addMenuButton = tkinter.Button(mainFrame, command=addAction_Arg, text= "Add a book", height=3, width=20)
    searchMenuButton = tkinter.Button(mainFrame, command=searchAction_Arg, text= "Search for Book", height=3, width=20)
    deleteMenuButton = tkinter.Button(mainFrame, command=deleteAction_Arg, text= "Delete a Book", height=3, width=20)
    quitMenuButton = tkinter.Button(mainFrame, command=quitAction_Arg, text= "Quit", height=3, width=20)
    searchMenuButton.grid(column=1)    
    addMenuButton.grid(row=0,column=0)
    deleteMenuButton.grid(row=1,column=1)
    quitMenuButton.grid(row=1)
    container.mainloop()
  
  
  
  def deleteMenu(self):
    container=tkinter.Tk()
    container.iconbitmap(iconPath)
    container.title("Delete a book")
    inputFrame= tkinter.Frame(container)
    inputFrame.grid(column=2)
    bookLabel = tkinter.Label(inputFrame, text="Book")
    bookLabel.grid(row=1)
    bookSearch = tkinter.Entry(inputFrame)
    bookSearch.grid(row=1, column=1)
    AuthorLabel = tkinter.Label(inputFrame, text="Author's Last Name")
    AuthorLabel.grid(row=2)
    authorSearch = tkinter.Entry(inputFrame)
    authorSearch.grid(row=2, column=1)
    full_arg= partial(functionality.delete, self, bookSearch, authorSearch, container)
    deleteButton = tkinter.Button(inputFrame, text="Delete book", command= full_arg)
    deleteButton.grid(row=3, column=1)
  
  
  
  def searchMenu(self):
    container= tkinter.Tk()
    container.iconbitmap(iconPath)
    container.title("Search For a book")
    searchFrame = tkinter.Frame(container)
    searchFrame.grid(column=2)
    bookLabel = tkinter.Label(searchFrame, text="Book")
    bookLabel.grid(row=1)
    AuthLabel = tkinter.Label(searchFrame, text="Author Name")
    AuthLabel.grid(row=2)
    bookSearch = tkinter.Entry(searchFrame)
    bookSearch.grid(row=1, column=1)
    AuthSearch = tkinter.Entry(searchFrame)
    AuthSearch.grid(row=2, column=1)
    action_with_arg = partial(functionality.searchBook, None, bookSearch, AuthSearch)
    searchButton = tkinter.Button(searchFrame, text= "Search for Book", command=action_with_arg)
    searchButton.grid(row=3,column=1)

  
  
  def addMenu(self):
    #--------------------------------------------Defines the container for the GUI-----------------------------------------------------
    container = tkinter.Tk()
    container.iconbitmap(iconPath)
    container.title('Add a Book to the database')
    #--------------Menubar
    #menuBar = tkinter.Menu(container)
    #menuBar.add_cascade(Label="Search", command=)
    #--------------------------------------------------------Defining the widgets--------------------------------------------------------
    bookFrame = tkinter.Frame(container)
    bookFrame.grid(column = 2)
    bookFrame.pack()

    LabelBook = tkinter.Label(bookFrame, text="Book's Name")
    LabelLN = tkinter.Label(bookFrame, text="Author's Last Name")
    labelGenre =  tkinter.Label(bookFrame, text="Book's Genre")
    labelLocation = tkinter.Label(bookFrame, text="Book Location")
    labelQuantity = tkinter.Label(bookFrame, text="How many books does the Library have")

    BookEntry = tkinter.Entry(bookFrame)
    LNEntry = tkinter.Entry(bookFrame)
    genreEntry = tkinter.Entry(bookFrame)
    locationEntry = tkinter.Entry(bookFrame)
    quantityEntry = tkinter.Entry(bookFrame)
    #---------------------------------------------Defining locations for all of the widgets----------------------------------------------
    LabelBook.grid(row=1)
    LabelLN.grid(row=2)
    labelGenre.grid(row=3) 
    labelLocation.grid(row=4)
    labelQuantity.grid(row=5)

    BookEntry.grid(row=1, column=1)
    LNEntry.grid(row=2, column=1)
    genreEntry.grid(row=3, column=1)
    locationEntry.grid(row=4, column=1)
    quantityEntry.grid(row=5, column=1)
    action_with_arg = partial(functionality.createBook, None, BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry )
    addButton = tkinter.Button(bookFrame, padx=10, pady=10, bd=2, text= "Add Book", command=action_with_arg)
    addButton.grid(row=6, column=1)
    container.mainloop()
menu.mainMenu(None)
print("Program running beginning....")
