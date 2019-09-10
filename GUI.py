import tkinter
import sqlite3





class functionality():
  def createBook(self, BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry):
    conn = sqlite3.connect('lib_database')
    cursor = conn.cursor()
    name = BookEntry.get()
    location= locationEntry.get()
    genre=genreEntry.get()
    LN = LNEntry.get()
    quantity = quantityEntry.get()
    addTuple = [(str(name)), (str(LN)), (str(genre)), (str(location)), (str(quantity))]
    cursor.execute('INSERT INTO Library VALUES (?,?,?,?,?)', addTuple)
    conn.commit()



class menu():
  def mainMenu(self):
    container = tkinter.Tk()
    container.title("AAI Library")
    mainFrame = tkinter.Frame(container)
    mainFrame.grid(column = 3)
  def addMenu(self):
    #--------------------------------------------Defines the container for the GUI-----------------------------------------------------
    container = tkinter.Tk()
    container.title('Add a Book to the database')
    #--------------Menubar
    menuBar = tkinter.Menu(container)
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
    addButton = tkinter.Button(bookFrame, padx=10, pady=10, bd=2, text= "Add Book", command=functionality.createBook(BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry))
    addButton.grid(row=6, column=1)
    container.mainloop()
self = None
menu.addMenu(self)




    








