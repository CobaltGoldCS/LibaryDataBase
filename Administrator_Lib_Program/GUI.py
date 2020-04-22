import tkinter
import Backend
from pathlib import Path

# If you really need to change the files
iconpath = Path.cwd() / 'icons' / 'icon.ico'
mainicon = Path.cwd() / 'icons' / 'mag.ico'
datapath = Path.cwd() / 'library_database.db'
class menu():
  def __init__(self, searchicon, mainpath, database):
    self.iconpath = mainpath
    self.functionality = Backend.functionality(searchicon, database)

  def mainMenu(self):
    #Defining the container
    container = tkinter.Tk()
    container.iconbitmap(self.iconpath)
    container.title("AAI Library")
    container.minsize(300,100)
    mainFrame = tkinter.Frame(container, bg='white')
    mainFrame.grid(column = 2)
    
    #Buttons + functionality
    addMenuButton = tkinter.Button(mainFrame, command= self.addMenu, bg ="#2eb5d7", fg='#555555',
                                      text= "Add a book", height=3, width=20)
    deleteMenuButton = tkinter.Button(mainFrame, command= self.deleteMenu, bg ="#2eb5d7", fg='#555555',
                                      text= "Delete a Book", height=3, width=20)
    checkOutButton = tkinter.Button(mainFrame, command= self.checkOutMenu, bg ="#92e998", fg='#555555',
                                      text= "Check Out Book", height=3, width=20)
    checkInButton = tkinter.Button(mainFrame, command = self.checkInMenu, bg ="#92e998", fg='#555555',
                                      text = "Check In Book", height = 3, width = 20)
    searchMenuButton = tkinter.Button(mainFrame, command= self.searchMenu, bg ="#4cb2a2", fg="white",
                                      text= "Search for Book", height=3, width=20)
    quitMenuButton = tkinter.Button(mainFrame, command= lambda: self.functionality.quit(container), fg='white',
                                      bg ="#2e6e80", text= "Quit", height=3, width=20)
    
    
    searchMenuButton.grid(column=0, row=2)    
    addMenuButton.grid(row=0,column=0)
    checkOutButton.grid(row=1)
    checkInButton.grid(row = 1, column = 1)
    deleteMenuButton.grid(column=1, row=0)
    quitMenuButton.grid(row=2, column = 1)
    container.mainloop()
  
  
  def checkOutMenu(self):
    container=tkinter.Toplevel()
    container.iconbitmap(self.iconpath)
    container.title("Check out book")
    inputFrame= tkinter.Frame(container, bg = '#2e6e80')
    inputFrame.grid(column=2)
    #Text widgets
    idLabel = tkinter.Label(inputFrame, text="Book ID", bg = '#2e6e80', fg = '#BBBBBB')
    studentLabel = tkinter.Label(inputFrame, text="Student ID", bg = '#2e6e80', fg = '#BBBBBB')
    idLabel.grid(row=0)
    studentLabel.grid(row=1)
    #Input widgets
    idInput = tkinter.Entry(inputFrame, width = 30, bg = '#BBBBBB')
    studentInput = tkinter.Entry(inputFrame, width = 30, bg = '#BBBBBB')
    idInput.grid(column=1, row=0, columnspan=2, sticky = 'e')
    studentInput.grid(row=1, column=1, columnspan=2, sticky = 'e')
    scanStudent = tkinter.Button(inputFrame, text='Scan StudentID', width = 13, bg = '#4cb2a2', fg = 'white',
                                command= lambda: studentInput.insert(0, self.functionality.barcodeScan()))
    scanISBN = tkinter.Button(inputFrame, text='Scan ISBN', width = 13, bg = '#4cb2a2', fg = 'white',
                                command= lambda: idInput.insert(0, self.functionality.barcodeScan()))
    checkOut = tkinter.Button(inputFrame, text='Check Out', width = 13, bg = '#92e998', fg = '#555555',
                                command= lambda: self.functionality.checkOut(idInput, studentInput))
    scanStudent.grid(row=2, column=1)
    scanISBN.grid(row=2)
    checkOut.grid(row=2, column=2)
  def checkInMenu(self):
    win = tkinter.Toplevel()
    win.iconbitmap(self.iconpath)
    win.title("Check in book")
    inputFrame= tkinter.Frame(win, bg = '#2e6e80')
    inputFrame.grid(column=2)
    #Text widgets
    idLabel = tkinter.Label(inputFrame, text="Book ID", bg = '#2e6e80', fg = '#BBBBBB')
    studentLabel = tkinter.Label(inputFrame, text="Student ID", bg = '#2e6e80', fg = '#BBBBBB')
    idLabel.grid(row=0)
    studentLabel.grid(row=1)
    #Input widgets
    idInput = tkinter.Entry(inputFrame, width = 30, bg = '#BBBBBB')
    studentInput = tkinter.Entry(inputFrame, width = 30, bg = '#BBBBBB')
    idInput.grid(column=1, row=0, columnspan=2, sticky = 'e')
    studentInput.grid(row=1, column=1, columnspan=2, sticky = 'e')
    scanStudent = tkinter.Button(inputFrame, text='Scan StudentID', width = 13, bg = '#4cb2a2', fg = 'white',
                                command= lambda: studentInput.insert(0, self.functionality.barcodeScan()))
    scanISBN = tkinter.Button(inputFrame, text='Scan ISBN', width=13, bg = '#4cb2a2', fg = 'white',
                                command= lambda: idInput.insert(0, self.functionality.barcodeScan()))
    checkIn = tkinter.Button(inputFrame, text='Check in', width=13, bg = '#92e998', fg = '#555555',
                                command= lambda: self.functionality.checkIn(idInput, studentInput))
    show = tkinter.Button(inputFrame, text = 'Show checked out books', width = 42, bg = '#4cb2a2', fg = 'white',
                                command = lambda: self.functionality.showOut(win))
    
    scanStudent.grid(row=2, column=1)
    scanISBN.grid(row=2)
    checkIn.grid(row=2, column=2)
    show.grid(row = 3, columnspan=3)
  def deleteMenu(self):
    #Defining container
    container=tkinter.Toplevel()
    container.iconbitmap(self.iconpath)
    container.title("Delete a book")
    inputFrame= tkinter.Frame(container, bg = '#2e6e80')
    inputFrame.grid(column=2)
    #Text widget then entry
    IdLabel = tkinter.Label(inputFrame, text="Id", bg = '#2e6e80', fg = '#BBBBBB')
    IdLabel.grid(row=1)
    IdSearch = tkinter.Entry(inputFrame, width = 27, bg = '#BBBBBB')
    IdSearch.grid(row=1, column=1)
    #Button with function
    scanButton = tkinter.Button(inputFrame, text="Scan Barcode", width=15, bg = '#4cb2a2', fg = 'white', bd=2,
                                  command= lambda: IdSearch.insert(0, self.functionality.barcodeScan()))
    deleteButton = tkinter.Button(inputFrame, text="Delete book", width=22, bg = '#92e998', fg = '#555555', bd=2,
                                  command= lambda: self.functionality.delete(IdSearch, container))
    scanButton.grid(row=2, column=0)
    deleteButton.grid(row=2, column=1, columnspan=1)
  
  
  
  def searchMenu(self):
    #Defining container
    searchContainer= tkinter.Toplevel()
    searchContainer.iconbitmap(self.iconpath)
    searchContainer.title("Search For a book")
    searchFrame = tkinter.Frame(searchContainer, bg = '#2e6e80')
    searchFrame.grid(column=2)
    #Text Labels
    bookLabel = tkinter.Label(searchFrame, text="Book", bg = '#2e6e80', fg = '#BBBBBB')
    bookLabel.grid(row=1)
    AuthLabel = tkinter.Label(searchFrame, text="Author Name", bg = '#2e6e80', fg = '#BBBBBB')
    AuthLabel.grid(row=2)
    #User input widgets
    bookSearch = tkinter.Entry(searchFrame, bg = '#BBBBBB')
    bookSearch.grid(row=1, column=1, sticky = 'e')
    AuthSearch = tkinter.Entry(searchFrame, bg = '#BBBBBB')
    AuthSearch.grid(row=2, column=1, sticky = 'e')
    #Button + functionallity
    searchButton = tkinter.Button(searchFrame, text= "Search for Book", width=30, bg = '#92e998', fg = '#555555',
                                  command= lambda: self.functionality.searchBook(bookSearch, AuthSearch, searchContainer))
    searchButton.grid(row=3,column=0, columnspan=2)

  
  
  def addMenu(self):
    #--------------------------------------------Defines the container for the GUI-----------------------------------------------------
    container = tkinter.Toplevel()
    container.iconbitmap(self.iconpath)
    container.title('Add a Book to the database')
    #--------------Menubar
    #menuBar = tkinter.Menu(container)
    #menuBar.add_cascade(Label="Search", command=)
    #--------------------------------------------------------Defining the widgets--------------------------------------------------------
    bookFrame = tkinter.Frame(container, bg = '#2e6e80')
    bookFrame.grid(column = 2)
    bookFrame.pack()
    LabelID = tkinter.Label(bookFrame, text="ISBN", bg = '#2e6e80', fg = '#BBBBBB')
    LabelBook = tkinter.Label(bookFrame, text="Book's Name", bg = '#2e6e80', fg = '#BBBBBB')
    LabelLN = tkinter.Label(bookFrame, text="Author's Last Name", bg = '#2e6e80', fg = '#BBBBBB')
    labelGenre =  tkinter.Label(bookFrame, text="Book's Genre", bg = '#2e6e80', fg = '#BBBBBB')
    labelLocation = tkinter.Label(bookFrame, text="Book Location", bg = '#2e6e80', fg = '#BBBBBB')
    labelQuantity = tkinter.Label(bookFrame, text="Number of books in library", bg = '#2e6e80', fg = '#BBBBBB')
    descLabel = tkinter.Label(bookFrame, text="Description of the Book", bg = '#2e6e80', fg = '#BBBBBB')

    IdEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    BookEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    LNEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    genreEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    locationEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    quantityEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    descEntry = tkinter.Entry(bookFrame, width=25, bg = '#BBBBBB')
    #---------------------------------------------Defining locations for all of the widgets----------------------------------------------
    LabelID.grid(columnspan=2, sticky="w")
    LabelBook.grid(row=1, columnspan=2, sticky="w")
    LabelLN.grid(row=2, columnspan=2, sticky="w")
    labelGenre.grid(row=3, columnspan=2, sticky="w") 
    labelLocation.grid(row=4, columnspan=2, sticky="w")
    labelQuantity.grid(row=5, columnspan=2, sticky="w")
    descLabel.grid(row=6, columnspan=2, sticky="w")

    IdEntry.grid(row=0, column=1, columnspan=2, sticky="e")
    BookEntry.grid(row=1, column=1, columnspan=2, sticky="e")
    LNEntry.grid(row=2, column=1, columnspan=2, sticky="e")
    genreEntry.grid(row=3, column=1, columnspan=2, sticky="e")
    locationEntry.grid(row=4, column=1, columnspan=2, sticky="e")
    quantityEntry.grid(row=5, column=1, columnspan=2, sticky="e")
    descEntry.grid(row=6, column=1, columnspan=2, sticky="e")
    addButton = tkinter.Button(bookFrame, padx=10, bd=2, text= "Add Book",  bg = '#92e998', fg = '#555555',
                              command=lambda : self.functionality.createBook( IdEntry, BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry, descEntry))
    autofill = tkinter.Button(bookFrame, padx=10, bd=2, text= "Get Data from ISBN", width = 13, bg = '#4cb2a2', fg = 'white',
                              command=lambda : self.functionality.autoFill(IdEntry.get(), BookEntry, LNEntry, locationEntry, descEntry))
    scanBarcode = tkinter.Button(bookFrame, padx=10, bd=2, text='Scan Barcode', bg = '#4cb2a2', fg = 'white',
                              command= lambda: IdEntry.insert(0, self.functionality.barcodeScan())) 
    autofill.grid(row=7, column=0)
    scanBarcode.grid(row=7, column=1)
    addButton.grid(row=7, column=2)
    container.mainloop()
if __name__ == "__main__":
  run = menu(str(mainicon), str(iconpath), str(datapath))
  run.mainMenu()
