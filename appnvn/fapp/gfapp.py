from tkinter import Button, Frame,messagebox
import os
from appnvn.atadctn.icontt import gui
import tkinter as tk
from tkinter import filedialog
from pynvn.path.ppath import getpathfromtk
from appnvn.atadctn.treectn import scbg
from pathlib import Path
from PIL import ImageTk
from pynvn.path.ppath import (refullpath,
                            listfileinfolder
                            )
from appnvn.atadctn.treectn import scrollbarvn
from pynvn.checklb.checkb import ChecklistBox
from pynvn.excel.copyexcel import cexcel
from pynvn.excel.hexcel import hexcel_child
from pynvn.excel.lexcel import listexcel
from appnvn.exazp.excel import hexcel
from pynvn.list.flist import filterlistbylstr
from appnvn.exazp.sdata.sdata import covertcsvexcel
from appnvn.exazp.excel.crangeactive import crangeactive
from appnvn.exazp.excel.hhm import hdatahm
from pynvn.excel import openexcelbyxl
from appnvn.exazp.conf import hconfazb
from pynvn.excel import closeallfileexcel
class gapp:
    """ return azbg gui """
    def __init__ (self,
                root=None,
                imagelogopath =None,
                pathconfig = None,
                pathconfigexell = None,
                imagelogo = None,
                ):
        self.root = root 
        self.imagelogopath =imagelogopath
        self.pathconfig = pathconfig
        self.pathconfigexell = pathconfigexell
        self.imagelogo = imagelogo
        self.guiforgd()
    def guiforgd(self):
        """Create interface for software"""
        gui (tktk=self.root,
            pathico=None,
            width=700,
            height=700, 
            widthx=420, 
            widthy=0,
            resizable=[True,True],
            title= "FAPP").setcfbs()

        self.sc  = scbg(parent = self.root,
                        cavheight=420,
                        cavwidth=500,
                        isonlyaframe= False,
                        bg = "#e6ecf5",
                        bgpr = "#5b9bd5",
                        framea = [0,0,500,420,"#e6ecf5"],
                        )
        large_font = ("times new roman",12)
        large_font_1 = ("times new roman",17)
        lb = tk.Label(self.root,
                    text = "Mr.Nhuần - nguyenvannhuan90123@gmail.com",
                    font = large_font,bg ="#5b9bd5")
        lb.place(relx = 0.5, 
                rely = 0.87, 
                anchor = tk.CENTER
                )
            
        self.framea = self.sc.framea

        lbt = tk.Label (self.framea, 
                        bg = "#e6ecf5" ,
                        text = "Input your information",
                        font =large_font_1,
                        )
        lbt.grid(row = 0,
                    column = 0,
                    columnspan = 6,
                    sticky = tk.EW
                    )
        # path to folder child
        repath = tk.Label(self.framea,
                        text = "Retrieve path:", 
                        width = 10,
                        font =large_font,
                        bg = "#e6ecf5",)
        repath.grid(row = 1,
                    column = 0,
                    sticky =  tk.W
                    )
        self.output1 = tk.Entry (self.framea, 
                                font = large_font,
                                justify=tk.CENTER,
                                width = 20,
                                relief = tk.SOLID,
                                bg = "yellow"
                              )
        self.output1.grid(row = 1,
                        column = 1,
                        )
        
        button = tk.Button(self.framea,
                            height = 1,
                            width = 4,
                            bd = 1,
                            )
        button.grid(row = 1,
                    column = 2,
                    sticky = "we"
                    )

        repath = tk.Label(self.framea,
                        text = "Sheet name:", 
                        width = 10,
                        font =large_font,
                        bg = "#e6ecf5",)
        repath.grid(row = 1,
                    column = 3,
                    sticky =  tk.W
                    )
        self.output1 = tk.Entry (self.framea, 
                                font = large_font,
                                justify=tk.CENTER,
                                width = 10,
                                relief = tk.SOLID,
                                bg = "yellow"
                              )
        self.output1.grid(row = 1,
                        column = 4,
                        )







root = tk.Tk ()
obj = gapp(root)
root.mainloop()