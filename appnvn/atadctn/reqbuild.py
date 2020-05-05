from tkinter import Frame,Tk,StringVar,Toplevel,IntVar,Radiobutton
import tkinter as tk
from tkinter import ttk
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
from appnvn.atadctn.treectn import scbg

class reqbuild(Frame):
        """ customer information"""
        def __init__(self,tktk = None,
                        br_image = None,
                        pathico = None,
                        br_image_path = None,
                        logoicon = None,
                        bglb = "white",
                        labelfont = ('times', 20),
                        labelfont_sm = ('times', 16),
                        padx = (10,0),
                        imagenext = None
                        ):
                self.tktk = tktk
                self.tktk.withdraw()
                Frame.__init__(self, tktk)
                
                self.labelfont = labelfont
                self.labelfont_sm = labelfont_sm
                self.br_image_path  = br_image_path
                self.br_image = br_image
                self.logoicon = logoicon
                self.padx = padx
                self.pathico = pathico
                self.filewin = Toplevel(self.tktk)
                self.bglb = bglb
                self.imagenext = imagenext

                gui (tktk=self.filewin,
                        pathico=self.pathico,
                        width=1800,
                        height=900,
                        widthx="center",
                        widthy="center",
                        condv=2.2,
                        resizable=[True,True]).setcfbs()
                
                # set menu 
                menu (tktk=self.filewin).createmenu()

                #gui for data 
                self.sc  = scbg(parent = self.filewin,
                                cavheight=600,
                                cavwidth=900,
                                bg = "white", 
                                bgpr = "#5181a7")

                self.listFramevp = self.sc.framecv

                self.canv =  self.sc.canvas

                self.creategui()

        def creategui(self):
                """create gui for customer information"""
                #image logo
                row = 0
                col = 0 
                logolbl = tk.Label (self.listFramevp,
                                image = self.logoicon,
                                borderwidth=0,
                                compound="center",
                                highlightthickness = 0)

                logolbl.grid (row = row,pady = 10,columnspan = 4)
                
                #line 1
                ci = tk.Label(self.listFramevp,
                                text = "Info house:"
                                )
                row = row + 1
                ci.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                
                #Line 2
                row = row + 1
                cis = tk.Label(self.listFramevp,
                                text = "Information of the house you want to build"
                                )
                cis.grid(column = 0, 
                                row  = row ,
                                padx = self.padx,
                                sticky  = "w",
                                columnspan = 4
                                )

                #  full name
                row = row + 1
                
                fn = tk.Label(self.listFramevp,
                        text = "*Your Name:",
                        )
                fn.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                
                fn.config (bg = self.bglb)
                fn.config(font=self.labelfont_sm)
                #row = row + 1
                col = col + 1
                fne = tk.Entry(self.listFramevp,
                                justify="left",
                                text = "Nguyen Van Nhuan"
                                )
                fne.grid(column = 1, 
                        row  = row,
                        columnspan = 3,
                        sticky  = "ew",
                        )

                # Phone Number
                row = row + 1
                pn = tk.Label(self.listFramevp,text = "*Phone Number:",
                                )
                pn.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")

                pne = tk.Entry(self.listFramevp,
                                justify="left",
                                text = "Nguyen Van Nhuan"
                                )
                pne.grid(column = 1, 
                        row  = row,
                        sticky  = "ew",
                        columnspan = 3,
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
                        )

                eme = tk.Entry(self.listFramevp,
                                justify="left",
                                text = "Nguyen Van Nhuan"
                                )
                eme.grid(column = 1, 
                        row  = row,
                        columnspan = 3,
                        sticky  = "ew" 
                        )
                # button next
                button1 = tk.Button(self.listFramevp, 
                                text = "Next",
                                bg = "azure2",
                                image = self.imagenext,
                                relief = tk.FLAT,
                                compound = tk.LEFT,
                                font = ("times new roman",20)
                                )
                row +=1
                button1.grid (column = 0, 
                                row = row,
                                columnspan = 4,
                                padx = self.padx,
                                pady = 10,
                                sticky  = "ew")
        
                # config label
                labels = (ci,cis,fn,pn,em)
                for label in labels:
                        label.config (bg = self.bglb,
                                        font=self.labelfont,
                                        anchor="w")
                        
                # config entry 
                entrys = (fne,pne,eme)
                for entry in entrys:
                        entry.config(font=self.labelfont_sm,
                                        bg = "white",
                                        relief = tk.SOLID)
                
        """delete value defaut entry """
        def some_callback(self,event): # note that you must include the event as an arg, even if you don't use it.
                self.adde.delete(0, "end")
                return None

