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
from pynvn.excel import openexcelbyxl,listsheetofwb
from appnvn.exazp.conf import hconfazb
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.excel.Fill_formula import fformulas
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
            height=420, 
            widthx=420, 
            widthy=0,
            resizable=[True,True],
            title= "FAPP").setcfbs()

        self.sc  = scbg(parent = self.root,
                        cavheight=250,
                        cavwidth=365,
                        isonlyaframe= False,
                        bg = "#e6ecf5",
                        bgpr = "#5b9bd5",
                        framea = [0,0,365,250,"#e6ecf5"],
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
                        text = "Retrieve Path:", 
                        width = 10,
                        font =large_font,
                        bg = "#e6ecf5",)
        repath.grid(row = 1,
                    column = 0,
                    sticky =  tk.W,
                    padx = (5,0)
                    )
        
        self.output1 = tk.Entry (self.framea, 
                                font = large_font,
                                justify=tk.CENTER,
                                width = 20,
                                relief = tk.SOLID,                              
                                bg = "yellow",
                              )
        self.output1.grid(row = 2,
                        column = 0,
                        padx = (5,0)
                        )
        
        button = tk.Button(self.framea,
                            height = 1,
                            width = 2,
                            bd = 1,
                            command = lambda: self.mfileopend(outputtk=self.output1,
                                                                combopc=self.combopc)
                            )
        button.grid(row = 2,
                    column = 1,
                    sticky = "we"
                    )

        lsheets = None
        self.pc = tk.StringVar() 
        self.combopc =  ttk.Combobox(self.framea, 
                                textvariable = self.pc,
                                width = 20,
                                values = ["Active Sheet","Select Sheet Name"],
                                state="readonly",
                                justify='center'
                                )

        self.combopc.grid(column = 2, 
                            row = 2,
                            padx = (10,0)
                            ) 

        self.combopc.bind("<<ComboboxSelected>>",
                            self.selected_rev)
        self.combopc.current(1)

        # destination 
        repathdes = tk.Label(self.framea,
                        text = "Destination Path:", 
                        font =large_font,
                        bg = "#e6ecf5",)
        repathdes.grid(row = 3,
                    column = 0,
                    sticky =  tk.W,
                    pady = (5,0),
                    padx = (5,0)
                    )
        
        self.repathdes = tk.Entry (self.framea, 
                                font = large_font,
                                justify=tk.CENTER,
                                relief = tk.SOLID,                               
                                bg = "yellow",
                              )
        self.repathdes.grid(row = 4,
                        column = 0,
                        sticky =  tk.EW,
                        padx = (5,0)
                        )
        
        buttondes = tk.Button(self.framea,
                            height = 1,
                            width = 4,
                            bd = 1,
                            command = lambda: self.mfileopend(outputtk=self.repathdes,
                                                            combopc=self.combo_des)
                            )
        buttondes.grid(row = 4,
                    column = 1,
                    sticky = "we"
                    )

        self.pc_des = tk.StringVar() 
        self.combo_des =  ttk.Combobox(self.framea, 
                                textvariable = self.pc_des,
                                width = 15,
                                values = ["Active Sheet","Select Sheet Name"],
                                state="readonly",
                                justify='center'
                                )
        self.combo_des.grid(column = 2, 
                            row = 4,
                            sticky =  tk.EW,
                            padx = (10,0)
                            ) 
        
        self.combo_des.current(1)

        self.combo_des.bind("<<ComboboxSelected>>",self.selected_des)


        func = tk.Label(self.framea,
                        text = "Function Excel:", 
                        font =large_font,
                        bg = "#e6ecf5",)
        func.grid(row = 5,
                    column = 0,
                    sticky =  tk.W,
                    padx = (5,0)
                    )
        self.pc_fun = tk.StringVar() 
        lfun = ["Select Function In Excel"] + list(returndictrowforcsv(self.pathconfig).keys())
        self.combo_fun =  ttk.Combobox(self.framea, 
                                textvariable = self.pc_fun,
                                width = 15,
                                values = lfun,
                                state="readonly",
                                justify='center'
                                )
        self.combo_fun.grid(column = 0, 
                                row = 6,
                                columnspan = 3,
                                sticky = tk.EW,
                                padx = (5,0)
                                ) 
                           
        self.combo_fun.current(0)

        self.combo_fun.bind("<<ComboboxSelected>>",
                            self.selected_des)

        button_open = tk.Button(self.framea,
                            height = 1,
                            width = 8,
                            text = "Open_Conf",
                            bd = 1,
                            command = lambda: openexcelbyxl(self.pathconfigexell)
                            )
        button_open.grid(row = 7,
                    column = 0,
                    sticky = "w",
                    padx = (5,0)
                    )

        button_conf = tk.Button(self.framea,
                            height = 1,
                            width = 8,
                            text = "Up_Conf",
                            bd = 1,
                            command = lambda: hconfazb(pathconf=self.pathconfig,
                                                    pathexconf=self.pathconfigexell).convertocsv()
                            )
        button_conf.grid(row = 7,
                        column = 2,
                        sticky = "e"
                        )

        run = tk.Button(self.framea,
                            height = 1,
                            width = 4,
                            text = "Run",
                            bd = 1,
                            command = lambda: fformulas(retr_path=getpathfromtk(self.output1),
                                                        des_path=getpathfromtk(self.repathdes),
                                                        retr_sheetname=self.pc.get(),
                                                        des_sheetname=self.pc_des.get(),
                                                        fuction= self.pc_fun.get(),
                                                        pathconf=self.pathconfig
                                                        ).filltoexcell()
                            )
        run.grid(row = 9,
                        column = 1,
                        sticky = "e"
                        )
                

        run = tk.Button(self.framea,
                            height = 1,
                            width = 4,
                            text = "Quit",
                            bd = 1,
                            command = self.root.quit
                            )
        run.grid(row = 10,
                        column = 1,
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
