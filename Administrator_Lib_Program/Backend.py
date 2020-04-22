import tkinter
import sqlite3
from tkinter import messagebox, ttk
from datetime import datetime
import cv2
import json
import urllib.request
class functionality():
  def __init__(self, mainicon, database):
    self.iconpath = mainicon
    self.dataPath = database
    self.first = True
    
    # For search results
    self.tree, self.resultFrame, self.searchWindow = None, None, None

  def createBook(self, IdEntry, BookEntry, locationEntry, genreEntry, LNEntry, quantityEntry, descEntry):
    #---------------------------------Grabs all info needed for new book--------------------#
    conn = sqlite3.connect(self.dataPath)
    cursor = conn.cursor()
    name = BookEntry.get()
    location = locationEntry.get()
    genre = genreEntry.get()
    LN = LNEntry.get()
    quantity = quantityEntry.get()
    Id = IdEntry.get()
  #-------------------------------Inserts all of that data into the database------------------#
    try:
      addTuple = [(int(Id)), (str(name)), (str(LN)), (str(genre)), (str(location)), (quantity), (descEntry.get())]
    except ValueError:
      messagebox.showerror("Insufficient Data", "Insufficient data for newly added book")
      return 
    cursor.execute('INSERT INTO Library VALUES (?,?,?,?,?,?,?)', addTuple)
    conn.commit()
    messagebox.showinfo("Success", "Book successfully added")
    BookEntry.delete(0, 'end')
    locationEntry.delete(0, 'end')
    genreEntry.delete(0, 'end')
    LNEntry.delete(0, 'end')
    quantityEntry.delete(0, 'end')
    conn.close()


  def selectItem(self, event):
    # All other values of the book
    try:
      curItem = self.tree.selection()[0]
    except IndexError:
      messagebox.showerror("Selection Error", "Please select a search result")
    valueTuple = self.tree.item(curItem)['values']
    title, author, genre, desc = valueTuple[1], valueTuple[2], valueTuple[3], valueTuple[6]
    if event.num == 1:
      messagebox.showinfo(f"Description of {title}", desc)
    return title, author, genre, desc
    



  def searchBook(self, BookName, AuthName, searchContainer):
    conn = sqlite3.connect(self.dataPath)
    cursor = conn.cursor()
    name = BookName.get()
    AuthorName = AuthName.get()
  #-----------------------------------------Initialising the search window--------------------#
    self.searchWindow = tkinter.Toplevel()
    self.resultFrame = tkinter.Frame(self.searchWindow)
    self.tree = ttk.Treeview(self.resultFrame, height = 10,
                            column = ( "column 1", "column 2", "column 3", "column 4", "column 5", "column 6"),
                            show = 'headings' )
    self.searchWindow.title("Search Results")
    self.searchWindow.iconbitmap(self.iconpath)
    self.resultFrame.grid(column=5)
    self.tree.grid(columnspan=6)
    self.tree.heading('#1', text = "id", anchor = tkinter.CENTER )
    self.tree.heading('#2', text = 'Book Name', anchor = tkinter.CENTER )
    self.tree.heading('#3', text = "Author Name", anchor = tkinter.CENTER )
    self.tree.heading('#4', text = "Genre", anchor = tkinter.CENTER )
    self.tree.heading('#5', text = "Location", anchor = tkinter.CENTER )
    self.tree.heading('#6', text = "Available", anchor = tkinter.CENTER )
  #------------------------------------------Finds data in database ---------------------------#
    if len(name) != 0 and len(AuthorName) == 0:
      query = "SELECT * FROM Library WHERE BookName=?"
      params = (name,)
    elif len(name) == 0 and len(AuthorName) != 0:
      query = "SELECT * FROM Library WHERE AuthorName=?"
      params = (AuthorName,)
    elif len(name) != 0 and len(AuthorName) != 0:
      query = "SELECT * FROM Library WHERE BookName=? AND AuthorName=?"
      params = (name, AuthorName)
    else:
      query = "SELECT * FROM Library"
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
    self.tree.bind('<Double-Button-1>', self.selectItem)
    searchContainer.destroy()




  def delete(self, Id, container):
#------------------------------------------Grabs data to be deleted---------------------------#
    try:
      int(Id.get())
      delId = Id.get()
#------------------------------------------------Main Code------------------------------------#    
      conn = sqlite3.connect(self.dataPath)
      cursor = conn.cursor()
      cursor.execute("DELETE FROM Library WHERE ID = ?", (delId,))
#------------------------------"Are you sure you want to delete this book?" messagebox--------#    
      sure = messagebox.askyesno("Are you sure", "Are you sure you want to delete this book?")
      if sure:
        conn.commit()
        messagebox.showinfo("Deleted", " Book deleted")
        conn.close()
      else:
        conn.close()
    except ValueError:
      messagebox.showerror("Invalid Value", "This value is unusable")
      raise Exception("Invalid value for ID")
  # When you need to check out a book
  def checkOut(self, idx, student):
    try:
      getID = int(idx.get())
      getStudent = int(student.get())
      date = datetime.today()
      strDate = date.strftime('%m-%d-%Y')
      dataTuple = (int(getID), int(getStudent), strDate)
      # Adds checked out book to the database
      with sqlite3.connect(self.dataPath) as conn:
        cursor = conn.cursor()
        if getID != None and getStudent != None:
          try:
            cursor.execute("INSERT INTO CheckedOut VALUES (?,?,?)", dataTuple)
          except ValueError:
            messagebox.showerror("Error", "invalid literal for int() with base 10")
          # Increments by -1 for quantity every checkout
          cursor.execute("SELECT Quantity FROM Library WHERE ID = ?", (getID,))
          bookCount = cursor.fetchone()
          if bookCount == None:
            messagebox.showerror("Error", "Invalid ID")
          else:
            print(bookCount)
            dataTuple = (bookCount[0]-1, getID)
            cursor.execute('''UPDATE Library
                          SET Quantity = ?
                          WHERE ID = ?''', dataTuple)
            messagebox.showinfo("Success", "Book Checked out")
        else: messagebox.showerror('Error', "No Input Detected")
    except ValueError:
      messagebox.showerror("Error", "invalid literal for int() with base 10")

  def checkIn(self, idx, student):
    try:
      getID = int(idx.get())
      getStudent = int(student.get())
      # Deletes checked out book
      if getID != None and getStudent != None:
        with sqlite3.connect(self.dataPath) as conn:
          cursor = conn.cursor()
          try: 
            cursor.execute("DELETE FROM CheckedOut WHERE ID = ? AND StudentID = ?", (getID, getStudent))
          except ValueError:
            messagebox.showerror("Error", "invalid literal for int() with base 10")
          # Increments by +1 for quantity every checkIN
          cursor.execute("SELECT Quantity FROM Library WHERE ID = ?", (getID,))
          bookCount = cursor.fetchone()
          print(bookCount)
          if bookCount != None:
            dataTuple = (bookCount[0]+1, getID)
            cursor.execute('''UPDATE Library
                          SET Quantity = ?
                          WHERE ID = ?''', dataTuple)
            messagebox.showinfo("Success", "Successfully Checked In {0}".format(getID))
          else: messagebox.showerror("Error", "No Books with that ID")
      else: messagebox.showerror("Error", "NULL Parameter")
    except ValueError:
      messagebox.showerror("Error", "invalid literal for int() with base 10")

  
  def showOut(self, frame):
    tree = ttk.Treeview(frame,height=10, column=("column 1", "column 2", "column 3"), show='headings')
    tree.heading("#1", text = "BookID", anchor = tkinter.CENTER)
    tree.heading("#2", text = "StudentID", anchor = tkinter.CENTER)
    tree.heading("#3", text = "Date", anchor = tkinter.CENTER)
    records = tree.get_children()
    for row in records:
      tree.delete(row)
    conn = sqlite3.connect(self.dataPath)
    curse = conn.cursor()
    curse.execute("SELECT * FROM CheckedOut")
    rows = curse.fetchall()
    for row in rows:
      tree.insert("", tkinter.END, values=row)
    treescroll = tkinter.Scrollbar(frame, orient = "vertical", command = tree.yview)
    treescroll.place(x=603, height=225, y = 96)


    tree.grid(row = 5)

  def barcodeScan(self):
    webcam = None
    if self.first:
      try:
        import pyzbar.pyzbar as pyzbar
        cap = cv2.VideoCapture(0)
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        webcam = True
      except (TypeError, ImportError):
        messagebox.showerror("Webcam Error", "Scan barcodes with usb scanner")
        webcam = False
      self.first = False


  # Mainloop for decoding and returning code from the barcode
    if webcam == True:
      print("True")
      while True:
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
  # Checks if there is any barcode with data on it, and destroys the windwo if it is
            if obj.data != None:
                cv2.destroyAllWindows()
                return str(obj.data.decode("utf-8"))
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
      messagebox.showinfo("Scan Now", "Click on the entrybox you want to scan for, scan your item, then repeat as needed")
      return input()
      

  def autoComplete(self, isbn):
      """Input a valid book ISBN and get a tuple with (theTitle, [List of author last names], Genre/Location) """
      base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

      with urllib.request.urlopen(base_api_link + str(isbn)) as f:
        text = f.read()
      decoded_text = text.decode("utf-8")
      obj = json.loads(decoded_text) # deserializes decoded_text to a Python object
      try:
        volume_info = obj["items"][0] 
      except KeyError:
        messagebox.showerror("Invalid ISBN", "This ISBN doesn't work, try another one.")
      authors = volume_info["volumeInfo"]["authors"]
      main_category = volume_info["volumeInfo"]["categories"][0]
      title = volume_info["volumeInfo"]["title"]
      Description =  volume_info["volumeInfo"]['description']
      authorLN = []
      for author in authors:
          authorLN.append(author.split(" ")[-1])
      return title, authorLN, main_category, Description
  def autoFill(self, isbn, bookEntry, Lnlist, LocationEntry, descEntry):
    data = self.autoComplete(isbn.strip())
    bookEntry.insert(0, data[0])
    if len(data[1]) > 1:
      entryString = ""
      numRuns = 0
      for name in data[1]:
        numRuns+=1
        if numRuns == len(data[1]):
          entryString = entryString + name
        else:
          entryString = entryString + name + ", "
      
      Lnlist.insert(0, entryString)
    else:
      Lnlist.insert(0, data[1])
    LocationEntry.insert(0, data[2])
    descEntry.insert(0, data[3])


  def quit(self, container):
    container.destroy()



