from tkinter import *
import tkinter as tk
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
from appnvn.atadctn.treectn import scbg
from appnvn.atadctn.treectn import (createcroll,
                                    ScrolledCanvas,
                                    cvframe,
                                    treescrollbar
                                    )
class incus(Frame):
    """ customer information"""
    def __init__(self,tktk = None,
                br_image = None,
                pathico = None,
                br_image_path = None,
                bglb = "thistle1",
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
        self.padx = padx
        self.pathico = pathico
        self.filewin = Toplevel(self.tktk)
        self.bglb = bglb
        
        gui (tktk=self.filewin,
                    pathico=self.pathico,
                    width=1000,
                    height=700,
                    widthx="center",
                    widthy="center",
                    resizable=[True,True]).setcfbs()
        
        # set menu 
        menu (tktk=self.filewin).createmenu()

        #gui for data 
        self.sc  = scbg(parent = self.filewin,cavheight=1000,cavwidth=1000)
        self.listFramevp = self.sc.framecv
        """
         create frame from cavas
        self.listFramevp = createcroll(listFrame=self.listFramevp,
                                        cavwidth=600,
                                        cavheight=700,
                                        scrollbarr=False,bg="thistle1").createy1()
        """

        self.creategui()
        #elf.sc.conf()

    def creategui(self):
        """create gui for customer information"""
        #line 1
        ci = tk.Label(self.listFramevp,
                        text = "Customer info:"
                        )
        ci.grid(column = 0, 
                  row = 0,
                  padx = self.padx,
                  sticky  = W)

        #Line 2
        cis = tk.Label(self.listFramevp,
                            text = "Thanks for your interest in getting a ATAD HOUSE"
                            )
        cis.grid(column = 0, 
                        row  = 1 ,
                        padx = self.padx,
                        sticky  = "w",
                        )

        #  full name
        fn = tk.Label(self.listFramevp,
                    text = "*Your Name:",
                    )
        fn.grid(column = 0, 
                  row = 2,
                  pady = (10,0),
                  padx = self.padx,
                  sticky  = W)
        
        fn.config (bg = self.bglb)
        fn.config(font=self.labelfont_sm)

        fne = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        fne.grid(column = 0, 
                row  = 3,
                sticky  = W,
                padx = self.padx,
                )

        #Address
        add = tk.Label(self.listFramevp,
                            text = "*Address:"
                            )
        add.grid(column = 0, 
                        row  = 4 ,
                        sticky  = "w",
                        padx = self.padx,
                        pady = (10,0)
                        )

        adde = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        adde.grid(column = 0, 
                row  = 5,
                padx = self.padx,
                sticky  = W 
                )
        # Phone Number
        pn = tk.Label(self.listFramevp,text = "*Phone Number:",
                            )
        pn.grid(column = 0, 
                  row = 6,
                  pady = (10,0),
                  padx = self.padx,
                  sticky  = W)

        pne = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        pne.grid(column = 0, 
                row  = 7,
                padx = self.padx,
                sticky  = W,
                )

        #email 
        em = tk.Label(self.listFramevp,
                            text = "*Email:",
                            )
        em.grid(column = 0, 
                        row  = 8 ,
                        sticky  = "w",
                        padx = self.padx,
                        pady = (10,0),
                        )

        eme = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        eme.grid(column = 0, 
                row  = 9,
                padx = self.padx,
                sticky  = W 
                )

        #Year of Birth
        yb = tk.Label(self.listFramevp,
                        text = "*Year of Birth:",
                        )
        yb.grid(column = 0, 
                  row = 10,
                  pady = (10,0),
                  padx = self.padx,
                  sticky  = W)

        ybe = tk.Entry(self.listFramevp,
                        justify="left",
                        text = "Nguyen Van Nhuan"
                        )
        ybe.grid(column = 0, 
                row  = 11,
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
                        width=50)