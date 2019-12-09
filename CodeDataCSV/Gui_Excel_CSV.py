import tkinter as tk
from tkinter import filedialog
from typing import Container
import TextGetDataFromExcel
import TextGetDataFromExcel_ReadExcel
import os
# function to export excel
def ExportToExcel():
    TextGetDataFromExcel.CreateFileExcel()
#function to define file open 

#Function to export Csv
def ExportToCsv():
    TextGetDataFromExcel_ReadExcel.CreateFileCSV()
"""
def CreateWWidget():
    root = TK.Tk()
    #write title on widget
    root.title ("Data Processing")
    root.geometry("400x400")
    root.resizable(width=True, height=True)
    frame1 = TK.Frame(root, bg='cyan',width=200, height=200, borderwidth=1, relief=TK.SUNKEN)
    frame1.grid(row = 0,
               column = 0,
               sticky="nsew")

    
    TK.Label(frame1, text = 'Model Dimensions').grid(row = 0, column = 0,columnspan = 1,sticky="w")
    TK.Label(frame1, text = 'Width:').grid(row = 1, column = 0)
    TK.Label(frame1, text = 'Length:').grid(row = 1, column = 1)
    
    frame2 = TK.Frame(root, bg='cyan',width=200, height=200, borderwidth=1, relief=TK.SUNKEN)
    frame2.grid(column=1, row=0, sticky="nsew")

    TK.Button(frame2, text="Simple button").grid(row = 0, column = 0)
    TK.Button(frame2, text="Simple button").grid(row = 0, column = 1)
    TK.Button(frame2, text="Simple button").grid(row = 1, column = 0)

    # Create buttom from Csv to get data 
    Buttom_ExportToCSV  = TK.Button (frame1,
                                text = "ExportToCSV",
                                command = ExportToCsv)
    
    Buttom_ExportToCSV.grid(row = 0,
                            column = 0,
                            columnspan= 10)
    
    # Create buttom from excel to get data 
    Buttom_ExportToExcel  = Button (root,
                                    text = "ExportToExcel",
                                    command = ExportToExcel)
    Buttom_ExportToExcel.grid(row = 1,
                            column = 0,
                            sticky = W+E)

    # quit widget 
    buttom_quit = Button (root,
                        text = "Exit",
                        command = root.quit)
    buttom_quit.grid(row = 2,
                    column = 0,
                    sticky = W+E)

    # open directory path to file
    button = Button(text = "open file",
                    width = 10,command = mfileopen)
    button.grid(row = 0,
                column = 4,
                sticky = W)
    # output 
    output = Text(root,width = 75,
                        height = 6,
                        wrap = WORD,
                        background = "yellow")
    output.grid(row = 5,
                column = 3,
                columnspan = 2,
                sticky = W)
                                                      
    root.mainloop()

CreateWWidget()
Buttom_ExportToCSV  = TK.Button (frame1,
                                text = "ExportToCSV",
                                command = ExportToCsv)
"""

class GuiTk (tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()

        self.title ("Data Processing")

        button = tk.Button(text = "Open File",
                    width = 10, height = 2,command = self.mfileopen)
        button.grid(row = 0,
                    column = 0,
                    columnspan = 2,
                    sticky = "we")

        self.output = tk.Text(self, 
                        height = 2,
                        wrap = tk.WORD,
                        background = "yellow")

        self.output.grid(row = 0,
                    column = 3,
                    columnspan = 5
                    )

        Buttom_ExportToCSV  = tk.Button (self,
                                        text = "ExportToCSV",
                                        command = ExportToCsv
                                        )
        
        Buttom_ExportToCSV.grid(row = 1,
                                column = 4,
                                columnspan = 1,
                                sticky = "we"
                                )
        
        Buttom_ExportToExcel  = tk.Button (self,
                                text = "ExportToExcel",
                                command = ExportToExcel)
        
        Buttom_ExportToExcel.grid(row = 1,
                                column = 5,
                                columnspan = 1,
                                sticky = "we"
                                )

        buttom_quit = tk.Button (self,
                        text = "Exit",
                        width = 20,
                        command = self.quit)

        buttom_quit.grid(row = 2,
                    column = 4,
                    columnspan = 2,
                    )

    def mfileopen(self):
        self.output.delete(0.0,tk.END)
        files = filedialog.askopenfile()
        self.output.insert(tk.END,files)

    def retrieve_input(self):
        inputValue = self.output.get("1.0","end-1c")
        return inputValue    
class GuiTk_Child (GuiTk):
    def __init__(self):
        GuiTk.__init__(self) 

    def retrieve_input(self):
        inputValue = self.output.get("1.0","end-1c")
        return inputValue
    
app = GuiTk_Child()
inputValue = app.retrieve_input()
print ("inputValue",inputValue)
app.mainloop()