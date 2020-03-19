
import tkinter as tk
from tkinter import *
from tkinter import ttk
class menu:
    def __init__(self,tktk = None):
    # set logo and title 
        self.tktk = tktk
    def createmenu (self):
        menubar = Menu(self.tktk)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", 
                            command=lambda: self.donothing())
        filemenu.add_command(label="Open", 
                            command=lambda: self.donothing())                                                                                                                   
        filemenu.add_command(label="Save", 
                            command=lambda: self.donothing())
        filemenu.add_command(label="Backup", 
                            command=lambda: self.donothing())
        filemenu.add_command(label="Close", 
                            command=lambda: self.donothing())

        filemenu.add_separator()

        filemenu.add_command(label="Exit", 
                            command=self.tktk.quit)
        menubar.add_cascade(label="Option", 
                            menu=filemenu)

        self.tktk.config(menu=menubar)