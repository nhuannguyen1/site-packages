from tkinter import messagebox
import re
def sepnumberandstrfromstr (sstr):
    """Splitting text and number in string"""
    # Splitting text and number in string 
    try:
        temp = re.compile("([a-zA-Z]+)([0-9]+)(\D)([a-zA-Z]+)([0-9]+)") 
        return temp.match(sstr).groups() 
    except:
        messagebox.showerror ("error input","Check your input {}, it must aann:aann".format(sstr))
def returnrangewolastrow(sstr):
    """Splitting text and number in string"""
    try:
        temp = re.compile("([a-zA-Z]+)([0-9]+)(\D)([a-zA-Z]+)") 
        return temp.match(sstr).group() 
    except:
        messagebox.showerror ("error input","Check your input {}, it must aann:aann".format(sstr))
