## Install Instructions
To install all of the webcam/barcode stuff, change directories into the folder where the adminstrator program is kept,
then `pip install -r requirements.txt` in the terminal
If you want to move the files you must move the entire Library_Database folder and keep it in the same order,
unless you also want to change that. GO to __LaunchProgram.py__ and you can change the filepaths of the separate
icons/symbols



*This library system was built with simplicity in mind. There are added features that are more complex than that, however.*
*This was made with sqlite, so it will not work on  the web, and only one computer has access to it.*
# Part 1, GUI
class menu(builtins.object)
 ### menu(mainicon, database)
 |  Methods defined here:
 |  -------------
 |  __init__(self, mainicon, database)
 |      Initialize self.  See help(type(self)) for accurate signature. 
 |      Takes the database filepath, and the Main icon filepath
 |  __addMenu__(self)
 |      Menu built for Adding books to the sqlite database. Includes __Barcode__ integration and an __autofill__ feature
 |  __checkInMenu__(self)
 |      Menu for functionallity.checkIn
 |  __checkOutMenu__(self)
 |      Menu for functionallity.checkOut
 |  __deleteMenu__(self)
 |      Menu for deleting a book completely from the database
 |  __mainMenu__(self)
 |      The starting Menu for Administrators
 |  __searchMenu__(self)
 |      Menu for searching for books by Author and/or bookname
 
 |Data descriptors defined here:
 |  ----------------------------------------------------------------------
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  __weakref__
 |      list of weak references to the object (if defined)

### In-depth

The mainMenu will open all lower menus separately, to change that, you would
Implement a self.container variable so you could access everything in that container
SearchMenu alone can open two child containers, which are defined in the __backend__.

All of the menus have a few things in common.
1. They all have a _.mainloop_ function
2. They all define a _.Tk_ object
3. They all have the _label_, _button_, and _entrybox_ widgets
4. All of the widgets (with a few _exceptions_) are placed in the grid system
5. They all have an _iconpath_ defined for the icon of your choice

From tkinter docs, There are a few things that can explain the state and organisation of 
the GUI file in the application:

- Widgets must be defined before they can be used
- Then they must have a valid area to be attached to (frames)
- Widgets have to be attached with a line of code as well, I used .grid because it is easy
and fast to organize properly
- Treeview widget from ttk (___backend___)


# Part 2, Backend

class functionality(builtins.object)
### functionality(mainicon, database)
 |  Methods defined here:
 |--------------
 |  __init__(self, mainicon, database)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  __autoComplete__(self, isbn)
 |      Input a valid book ISBN and get a tuple with (theTitle, [List of author last names], Genre/Location)
 |  __autoFill__(self, isbn, bookEntry, Lnlist, LocationEntry, descEntry)
 |      Input an isbn and entryboxes, and the function call autoComplete and populate the entryboxes
 |  __barcodeScan__(self)
 |      Uses *opencv and zbar* to scan a barcode using a webcam, and returns the value scanned
 |  __checkIn__(self, idx, student)
 |      Deletes a book from the table *checked out*
 |  __checkOut__(self, idx, student)
 |      Adds a book to the table *checked out* with a date and studentID
 |  __createBook__(self, IdEntry, BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry, descEntry)
 |      Creates a new record for a book in the *Library* database
 |  __delete__(self, Id, container)
 |      Deletes a record from *Library* permanently 
 |  __quit__(self, container)
 |      Quits the program
 |  __searchBook__(self, BookName, AuthName, searchContainer)
 |      Searches for a book by ID, then displays all books by that ID
 |  __selectItem__(self, event)
 |      When an item is clicked in the ***searchBook Container***, this gets values, then displays then
 |  __showOut__(self, frame)
 |      Shows all of the records in the table *checked out*

 |  Data descriptors defined here:
 |  ----------------------------------------------------------------------
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  __weakref__
 |      list of weak references to the object (if defined)


### Organization of the backend
- To get the data from the entryboxes, we must call the .get method
- To execute statements in sqlite, a tuple/list is required, which is why we get
such code as this                                     
cursor.execute("DELETE FROM Library WHERE ID = ?", (delId,))
- The errors and info are mostly shown using *tk.messagebox*
- There are also a lot of checks for NULL values 

## Color scheme
Action Color (Main Buttons and stuff) #92e998
Contrast (Basic elements) #4cb2a2
Neutral (Background) #2e6e80




#### Sources 
[Tkinter Docs](https://docs.python.org/3/library/tk.html)
[Sqlite Docs](https://docs.python.org/3/library/sqlite3.html)
[Barcode Scanner](https://github.com/prash29/Barcode-Reader/blob/master/barcode.py)