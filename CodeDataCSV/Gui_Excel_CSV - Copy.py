from tkinter import *
from tkinter import filedialog
import TextGetDataFromExcel
import TextGetDataFromExcel_ReadExcel
import os
import sys
# function to export excel
def ExportToExcel():
    TextGetDataFromExcel.CreateFileExcel()
#function to define file open 
def mfileopen():
    files = filedialog.askopenfile()
    output.insert(END,
                files)
    output.insert(END,
                files)
#Function to export Csv
def ExportToCsv():
    TextGetDataFromExcel_ReadExcel.CreateFileCSV()

root  = Tk ()
#write title on widget
root.title ("Data Processing")
# Create buttom from Csv to get data 
Buttom_ExportToCSV  = Button (root,
                                text = "ExportToCSV",
                                command = ExportToCsv)
Buttom_ExportToCSV.grid(row = 0,
                            column = 0,
                            sticky = W+E)

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
