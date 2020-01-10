from tkinter import *

Window = Tk()

def Open():
    New_Window = Tk()
    #You can edit here.
    New_Window.mainloop()

Btn1 = Button(text="Open", command=Open)
Btn1.pack()

Window.mainloop()