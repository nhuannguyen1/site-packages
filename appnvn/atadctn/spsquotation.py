from tkinter import *
import tkinter as tk
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
from tkinter import ttk
from appnvn.atadctn.treectn import (createcroll,
                                    ScrolledCanvas,
                                    cvframe,
                                    treescrollbar
                                    )
from tkintertable import TableCanvas, TableModel
def createData(rows=20, cols=15):
        """Creare random dict for test data"""

        data = {}
        names = list (range(0,20))
        colnames = ["B","C","D","E","F","G","M","N","H","J","L","K","Q","W","E","R","T","Y","U","I","O","P","AB","BC","MB","KL","AC"]
        
        for n in names:
                data[n]={}
                data[n]['A'] = ""
                
        for c in range(0,cols):
                colname=colnames[c]
                i=0
                for n in names:
                        data[n][colname] = ""
                        i+=1
        return data
        
class spreadsheetgui(Frame):
    def __init__(self,tktk = None,
                br_image = None,
                pathico = None,
                br_image_path = None):

        Frame.__init__(self, tktk)
        self.tktk = tktk

        self.br_image_path  = br_image_path

        self.br_image = br_image

        self.pathico = pathico

        self.filewin = Toplevel(self.tktk)

        gui (tktk=self.filewin,
                    pathico=self.pathico,
                    width=1280,
                    height=1024,
                    widthx=300,
                    widthy=0,
                    resizable=[True,True]).setcfbs()
        # set data
        """
        data = {'rec1j': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
       'rec2111': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}
        } 
        """
        data = createData()
        menu (tktk=self.filewin).createmenu()

        tframe = Frame(self.filewin)
        tframe.pack(fill = X, expand = True,side = BOTTOM)
        table = TableCanvas(tframe,data=data)
        table.show()
        
        tframep = Frame(self.filewin)
        tframep.pack(fill = X, expand = True,side = TOP)
        greenbutton = Button(tframep, text="green", fg="green")
        greenbutton.pack( )