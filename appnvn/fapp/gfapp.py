from tkinter import Button, Frame,messagebox
import os
from appnvn.atadctn.icontt import gui
import tkinter as tk
from tkinter import filedialog,ttk
from pynvn.path.ppath import getpathfromtk
from appnvn.atadctn.treectn import scbg
from pathlib import Path
from PIL import ImageTk
from pynvn.path.ppath import (refullpath,
                            listfileinfolder,
                            mfileopen
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
from pynvn.excel import openexcelbyxl,listsheetofwb
from appnvn.exazp.conf import hconfazb
from pynvn.excel import closeallfileexcel
from pynvn.csv.rcsv import returndictrowforcsv
import re
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
        self.pattern = re.compile("^\w{0,10}")
    def guiforgd(self):
        """Create interface for software"""
        gui (tktk=self.root,
            pathico=None,
            width=700,
            height=320, 
            widthx=420, 
            widthy=0,
            resizable=[True,True],
            title= "FAPP").setcfbs()

        self.sc  = scbg(parent = self.root,
                        cavheight=200,
                        cavwidth=550,
                        isonlyaframe= False,
                        bg = "#e6ecf5",
                        bgpr = "#5b9bd5",
                        framea = [0,0,550,200,"#e6ecf5"],
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
                        fg = "black",
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
                    sticky =  tk.E
                    )
        
        self.output1 = tk.Entry (self.framea, 
                                font = large_font,
                                justify=tk.CENTER,
                                width = 20,
                                relief = tk.SOLID,                              
                                bg = "yellow",
                              )
        self.output1.grid(row = 1,
                        column = 1,
                        )
        
        button = tk.Button(self.framea,
                            height = 1,
                            width = 4,
                            bd = 1,
                            command = lambda: self.mfileopend(outputtk=self.output1,
                                                                combopc=self.combopc)
                            )
        button.grid(row = 1,
                    column = 2,
                    sticky = "we"
                    )

        repath = tk.Label(self.framea,
                        text = "Sheet name:", 
                        font =large_font,
                        bg = "#e6ecf5",)
        repath.grid(row = 1,
                    column = 3,
                    sticky =  tk.E
                    )
        lsheets = None
        self.pc = tk.StringVar() 
        self.combopc =  ttk.Combobox(self.framea, 
                                textvariable = self.pc,
                                width = 15,
                                values = ["Active Sheet",""],
                                state="readonly"
                                )
        self.combopc.grid(column = 4, row = 1) 
        self.combopc.bind("<<ComboboxSelected>>",self.selected_rev)
        # destination 
        repathdes = tk.Label(self.framea,
                        text = "Des path:", 
                        font =large_font,
                        bg = "#e6ecf5",)
        repathdes.grid(row = 2,
                    column = 0,
                    sticky =  tk.E,
                    pady = 10
                    )
        
        self.repathdes = tk.Entry (self.framea, 
                                font = large_font,
                                justify=tk.CENTER,
                                width = 20,
                                relief = tk.SOLID,                               
                                bg = "yellow",
                              )
        self.repathdes.grid(row = 2,
                        column = 1,
                        )
        
        buttondes = tk.Button(self.framea,
                            height = 1,
                            width = 4,
                            bd = 1,
                            command = lambda: self.mfileopend(outputtk=self.repathdes,
                                                            combopc=self.combo_des)
                            )
        buttondes.grid(row = 2,
                    column = 2,
                    sticky = "we"
                    )

        sndes = tk.Label(self.framea,
                        text = "Sheet name:", 
                        font =large_font,
                        bg = "#e6ecf5",)
        sndes.grid(row = 2,
                    column = 3,
                    sticky =  tk.E
                    )
        self.pc_des = tk.StringVar() 
        self.combo_des =  ttk.Combobox(self.framea, 
                                textvariable = self.pc_des,
                                width = 15,
                                values = ["Active Sheet",""],
                                state="readonly"
                                )
        self.combo_des.grid(column = 4, row = 2) 
        self.combo_des.bind("<<ComboboxSelected>>",self.selected_des)


        func = tk.Label(self.framea,
                        text = "Function:", 
                        font =large_font,
                        bg = "#e6ecf5",)
        func.grid(row = 3,
                    column = 1,
                    sticky =  tk.E
                    )
        self.pc_fun = tk.StringVar() 
        lfun = list(returndictrowforcsv(self.pathconfig).keys())
        print ("lfun",lfun)
        self.combo_fun =  ttk.Combobox(self.framea, 
                                textvariable = self.pc_fun,
                                width = 15,
                                values = lfun,
                                state="readonly"
                                )
        self.combo_fun.grid(column = 2, 
                                row = 3,
                                columnspan = 2,
                                sticky = tk.EW) 
                           
        self.combo_fun.bind("<<ComboboxSelected>>",
                            self.selected_des)

        button_open = tk.Button(self.framea,
                            height = 1,
                            width = 8,
                            text = "Open_Conf",
                            bd = 1,
                            command = lambda: openexcelbyxl(self.pathconfigexell)
                            )
        button_open.grid(row = 4,
                    column = 1,
                    sticky = "w"
                    )

        button_conf = tk.Button(self.framea,
                            height = 1,
                            width = 8,
                            text = "Up_Conf",
                            bd = 1,
                            command = lambda: hconfazb(pathconf=self.pathconfig,
                                                    pathexconf=self.pathconfigexell).convertocsv()
                            )
        button_conf.grid(row = 4,
                        column = 4,
                        sticky = "e"
                        )

        run = tk.Button(self.framea,
                            height = 1,
                            width = 8,
                            text = "Run",
                            bd = 1,
                            command = lambda: hconfazb(pathconf=self.pathconfig,
                                                    pathexconf=self.pathconfigexell).convertocsv()
                            )
        run.grid(row = 5,
                        column = 4,
                        sticky = "e"
                        )
                

        run = tk.Button(self.framea,
                            height = 1,
                            width = 8,
                            text = "Quit",
                            bd = 1,
                            command = self.root.quit
                            )
        run.grid(row = 6,
                        column = 4,
                        sticky = "e"
                        )





    def mfileopend(self,outputtk,combopc):
        mfileopen(outputtk)
        pathfilep = getpathfromtk(outputtk,
                                Warning_path_existing=False)
        lsheets  = listsheetofwb(pathfilep)
        try:
            combopc.config(values=["Active Sheet"] + lsheets)
        except:
            pass  
    def selected_rev(self,event):
        selected=self.pc.get()
        if selected == "Active Sheet":
            self.output1.config(state='disabled')
        else:
            self.output1.config(state='normal') 

    def selected_des(self,event):
        selected=self.pc_des.get()
        if selected == "Active Sheet":
            self.repathdes.config(state='disabled') 
        else:
            self.repathdes.config(state='normal') 

"""
root = tk.Tk ()
obj = gapp(root)
root.mainloop()
"""
