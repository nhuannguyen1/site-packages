from tkinter import messagebox
import os
def listfolderofpfolder(folderchild):
    """ return list folder of parent folder"""
    os.chdir(folderchild)
    try:
        lfolderp = os.listdir(folderchild)

    except:
        messagebox.showerror ("Error"," No folder parent folder: {}".format(folderchild))
    return lfolderp