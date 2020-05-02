from tkinter import *
import tkinter as tk
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
from appnvn.atadctn.treectn import scbg
class incus(Frame):
    """ customer information"""
    def __init__(self,tktk = None,
                br_image = None,
                pathico = None,
                br_image_path = None,
                logoicon = None,
                bglb = "white",
                labelfont = ('times', 20),
                labelfont_sm = ('times', 16),
                padx = (10,0)
                ):
        
        Frame.__init__(self, tktk)
        self.tktk = tktk
        self.labelfont = labelfont
        self.labelfont_sm = labelfont_sm
        self.br_image_path  = br_image_path
        self.br_image = br_image
        self.logoicon = logoicon
        self.padx = padx
        self.pathico = pathico
        self.filewin = Toplevel(self.tktk)
        self.bglb = bglb
        
        gui (tktk=self.filewin,
                    pathico=self.pathico,
                    width=800,
                    height=800,
                    widthx="center",
                    widthy="center",
                    condv=2.7,
                    resizable=[True,True]).setcfbs()
        
        # set menu 
        menu (tktk=self.filewin).createmenu()

        #gui for data 
        self.sc  = scbg(parent = self.filewin,
                        cavheight=600,
                        cavwidth=600,
                        bg = "white", 
                        bgpr = "#5181a7")

        self.listFramevp = self.sc.framecv

        self.creategui()

    def creategui(self):
        """create gui for customer information"""
        #image logo
        row = 0
        logolbl = Label (self.listFramevp,
                        image = self.logoicon,
                        borderwidth=0,
                        compound="center",
                        highlightthickness = 0)

        logolbl.grid (row = row,pady = 10)
        
        #line 1
        ci = tk.Label(self.listFramevp,
                        text = "Customer info:"
                        )
        row = row + 1
        ci.grid(column = 0, 
                  row = row,
                  padx = self.padx,
                  sticky  = W)
        
        #Line 2
        row = row + 1
        cis = tk.Label(self.listFramevp,
                            text = "Thanks for your interest in getting a ATAD HOUSE"
                            )
        cis.grid(column = 0, 
                        row  = row ,
                        padx = self.padx,
                        sticky  = "w",
                        )

        #  full name
        row = row + 1
        fn = tk.Label(self.listFramevp,
                    text = "*Your Name:",
                    )
        fn.grid(column = 0, 
                  row = row,
                  pady = (10,0),
                  padx = self.padx,
                  sticky  = W)
        
        fn.config (bg = self.bglb)
        fn.config(font=self.labelfont_sm)
        row = row + 1
        fne = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        fne.grid(column = 0, 
                row  = row,
                sticky  = W,
                padx = self.padx,
                )

        #Address
        row = row + 1
        add = tk.Label(self.listFramevp,
                            text = "*Address:"
                            )
        add.grid(column = 0, 
                        row  = row ,
                        sticky  = "w",
                        padx = self.padx,
                        pady = (10,0)
                        )
        row = row + 1
        adde = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        adde.grid(column = 0, 
                row  = row,
                padx = self.padx,
                sticky  = W 
                )
        # Phone Number
        row = row + 1
        pn = tk.Label(self.listFramevp,text = "*Phone Number:",
                            )
        pn.grid(column = 0, 
                  row = row,
                  pady = (10,0),
                  padx = self.padx,
                  sticky  = W)

        pne = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        row = row + 1
        pne.grid(column = 0, 
                row  = row,
                padx = self.padx,
                sticky  = W,
                )

        #email 
        em = tk.Label(self.listFramevp,
                            text = "*Email:",
                            )
        row = row + 1
        em.grid(column = 0, 
                        row  = row ,
                        sticky  = "w",
                        padx = self.padx,
                        pady = (10,0),
                        )

        eme = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        row = row + 1
        eme.grid(column = 0, 
                row  = row,
                padx = self.padx,
                sticky  = W 
                )

        #Year of Birth
        yb = tk.Label(self.listFramevp,
                        text = "*Year of Birth:",
                        )
        row = row + 1
        yb.grid(column = 0, 
                  row = row,
                  pady = (10,0),
                  padx = self.padx,
                  sticky  = W)
        row = row + 1
        ybe = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        ybe.grid(column = 0, 
                row  = row,
                padx = self.padx,
                sticky  = W,
                )
        # config label
        labels = (ci,cis,fn,add,pn,em,yb)
        for label in labels:
            label.config (bg = self.bglb,
                            width=43,
                            font=self.labelfont,
                            anchor="w")
        # config entry 
        entrys = (fne,adde,pne,eme,ybe)
        for entry in entrys:
            entry.config(font=self.labelfont_sm,
                        bg = "azure2",
                        width=50,
                        bd = 1,
                        relief = SOLID)