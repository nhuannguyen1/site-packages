from tkinter import messagebox
import xlwings as xw
def returnactivewbpath (namefile):
    """ return active workbook """
    try:
        fpath = xw.books.active.fullname
        return fpath
    except:
        messagebox.showerror ("Error",
                                        "Not yet open file excel, open excel file {0}".format(namefile))
        