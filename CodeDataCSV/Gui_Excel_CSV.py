import tkinter as tk
import os
from tkinter import filedialog
from appnvn.eximexcsv import (extoex,
                              extocsv)
from pynvn.csv.tocsv import wrcsv
from appnvn.eximexcsv import templatexc
from pynvn.path.ppath import PathSteel
from tkinter import messagebox
# function to export excel
class GuiTk (tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__()
        # set title 
        self.title ("Data Processing")
        # set window icon
        self.iconbitmap('clienticon.ico')
        # set font for tk 
        large_font = ('Verdana',10)
        #create buttom for open file 
        button = tk.Button(text = "input file",
                            width = 10,
                            height = 2,
                            command = self.mfileopen
                            )
        button.grid(row = 0,
                    column = 0,
                    columnspan = 2,
                    sticky = "we"
                    )

        # create output text, it is used to save directory 
        self.output = tk.Text (self, 
                                width = 60,
                                height = 2,
                                font = large_font,
                                selectborderwidth = 10,
                                bg = "yellow"
                              )

        
        self.output.grid(row = 0,
                        column = 3,
                        columnspan = 5
                        )

        button = tk.Button(text = "output file",
                            width = 10,
                            height = 2,
                            command = self.mfileopenout
                            )
        button.grid(row = 1,
                    column = 0,
                    columnspan = 2,
                    sticky = "we"
                    )

        self.outputfile = tk.Text (self, 
                                    width = 60,
                                    height = 2,
                                    font = large_font,
                                    selectborderwidth = 10,
                                    bg = "yellow"
                                  )
        self.outputfile.grid(row = 1,
                            column = 3,
                            columnspan = 5
                            )

        # create button to export to csv 
        Buttom_ExportToCSV  = tk.Button (self,
                                        text = "ExportToCSV",
                                        command = self.ExportToCsv
                                        )
        
        Buttom_ExportToCSV.grid(row = 2,
                                column = 4,
                                columnspan = 1,
                                sticky = "we"
                                )
        # create button to export to excel 
        Buttom_ExportToExcel  = tk.Button (self,
                                           text = "ExportToExcel",
                                           command = self.ExportToExcel
                                           )
        
        Buttom_ExportToExcel.grid(row = 2,
                                 column = 5,
                                 columnspan = 1,
                                 sticky = "we"
                                 )
        #quit widget  
        buttom_quit = tk.Button (self,
                                text = "Exit",
                                width = 20,
                                command = self.quit)

        buttom_quit.grid(row = 3,
                        column = 4,
                        columnspan = 2,
                        )
        # get path csv to retrive path 
        self.pathtow = PathSteel(modulename =templatexc,
                             FileName ='path.csv')\
                            .getpathmodule()

        # set value defaut for output 
        wcsvt = wrcsv(pathtow = self.pathtow).ReDtallrowbyIndx(1)
        self.outputfile.insert(tk.END,
                               wcsvt[1])

        self.output.insert(tk.END,
                            wcsvt[0])

    #export to excel 
    def ExportToExcel(self):
        pathinout = self.repathinout()
        extoex.CreateFileExcel(*pathinout)

    # export to csv 
    def ExportToCsv(self):
        pathinout = self.repathinout()
        extocsv.CreateFileCSV(*pathinout)

    # return path in and path out 
    def repathinout(self):
        pathin = self.output.get("1.0",
                                "end - 1 chars")
        pathout = self.outputfile.get("1.0",
                                "end - 1 chars")
        try:
            if (os.path.exists(pathin) == False or 
                os.path.exists(pathout) == False):
                messagebox.showinfo("directory", "directory not found for option")
            else: 
                lines = [["pathin","pathout"],
                        [pathin,pathout]]
                wcsvt = wrcsv(self.pathtow,*lines).savevaltocsv()
                return [pathin,pathout]
        except:
            messagebox.showinfo ("directory", "recheck file path from Gui")

    # open file follow directory 
    def mfileopen(self):
        files = filedialog.askdirectory()
        self.output.insert(tk.END,
                            files)
        
    # open file out put 
    def mfileopenout(self):
        files = filedialog.askdirectory()
        self.outputfile.insert(tk.END,
                                files)

    # retrieve data from input 
    def retrieve_input(self):
        inputValue = self.output.get("1.0",
                                    tk.END)
        return inputValue    

class GuiTk_Child (GuiTk):
    def __init__(self):
        GuiTk.__init__(self) 
        
    def retrieve_input(self):
        inputValue = self.output.get("1.0",
                                    tk.END)
        return inputValue
app = GuiTk_Child()
inputValue = app.retrieve_input()
app.mainloop()