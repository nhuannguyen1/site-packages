import xlwings as xw
def returnactivewbpath ():
    """ return active workbook """
    try:
        fpath = xw.books.active.fullname
        return fpath
    except:
        messagebox.showerror ("Error",
                                        "Not yet open file excel")
     