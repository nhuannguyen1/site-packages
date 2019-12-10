import tkinter as tk
from tkinter import filedialog
from typing import Container
import TextGetDataFromExcel
import TextGetDataFromExcel_ReadExcel
import os
# function to export excel
class GuiTk (tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.title ("Data Processing")
        large_font = ('Verdana',20)

        button = tk.Button(text = "Open File",
                    width = 10, height = 2,command = self.mfileopen)
        button.grid(row = 0,
                    column = 0,
                    columnspan = 2,
                    sticky = "we")

        self.entry_content = tk.StringVar()
        self.output = tk.Entry(self, 
                        textvariable = self.entry_content,
                        width = 20,
                        font = large_font,
                        selectborderwidth = 10,
                        bg = "yellow")
        self.output.grid(row = 0,
                    column = 3,
                    columnspan = 5
                    )
        
        Buttom_ExportToCSV  = tk.Button (self,
                                        text = "ExportToCSV",
                                        command = self.ExportToCsv
                                        )
        
        Buttom_ExportToCSV.grid(row = 1,
                                column = 4,
                                columnspan = 1,
                                sticky = "we"
                                )
        
        Buttom_ExportToExcel  = tk.Button (self,
                                text = "ExportToExcel",
                                command = self.ExportToExcel)
        
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
    
    def ExportToExcel(self):
        path = self.entry_content.get()
        TextGetDataFromExcel.CreateFileExcel(path)

    def ExportToCsv(self):
        path = self.entry_content.get()
        TextGetDataFromExcel_ReadExcel.CreateFileCSV(path)

    def mfileopen(self):
        files = filedialog.askdirectory()
        self.output.insert(tk.END,files)
    def retrieve_input(self):
        inputValue = self.output.get()
        return inputValue    
class GuiTk_Child (GuiTk):
    def __init__(self):
        GuiTk.__init__(self) 
    def retrieve_input(self):
        inputValue = self.output.get()
        return inputValue
app = GuiTk_Child()
inputValue = app.retrieve_input()
app.mainloop()