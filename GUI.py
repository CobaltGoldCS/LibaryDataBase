import tkinter
import sqlite3

#Defines the container for the GUI
container = tkinter.Tk()
container.title('AAI Library')
#Menubar
menuBar = tkinter.Menu(container)
#menuBar.add_cascade(Label="Search", command=)

bookFrame = tkinter.Frame(container)
bookFrame.pack(side= "top")
#Need to figure out the class stuff in python so I can understand why this doesnt work for me
addButton = tkinter.Button(bookFrame, text="Add a book", )
addButton.pack(side="Left")
container.mainloop()