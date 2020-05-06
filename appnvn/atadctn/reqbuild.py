from tkinter import (Frame,
                    Tk,
                    Toplevel
                    )
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
                self.sc = scbg(parent = self.filewin,
                                cavheight=900,
                                cavwidth=1400,
                                bg = "white", 
                                bgpr = "#5181a7",
                                isonlyaframe= False,
                                framea =[10,10,900,500,"yellow"], 
                                frameb = [910,10,700,500,"white"]
                                )
                self.listFramevp = self.sc.framea
                self.listFramedr = self.sc.frameb
                self.canv =  self.sc.canvas
                self.creategui()
                self.createdrawing()

        def creategui(self):
                """create gui for customer information"""
                #image logo
                row = 0
                col = 0 
                
                #Line 2
                row = row + 1
                cis = tk.Label(self.listFramevp,
                                text = "Ask the house you want to build"
                                )
                cis.grid(column = 0, 
                                row  = row ,
                                padx = self.padx,
                                sticky  = "w",
                                columnspan = 4
                                )
                ####################################################area
                #  area
                row = row + 1

                arealb = tk.Label(self.listFramevp,
                        text = "*Area:",
                        )
                arealb.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")


                # Width entry 
                entryw = tk.Entry(self.listFramevp)
                entryw.grid(column = 1, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                #Width label
                wlb = tk.Label(self.listFramevp,
                        text = "Width:",
                        )
                wlb.grid(column = 2, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                row += 1
               # height entry 
                entryh = tk.Entry(self.listFramevp)
                entryh.grid(column = 1, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                #height label
                lbh = tk.Label(self.listFramevp,
                        text = "height:",
                        )
                lbh.grid(column = 2, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                



                ####################################################area

                # Setback space
                row = row + 1
                sbs = tk.Label(self.listFramevp,text = "Setback space:",
                                )
                sbs.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                # before 
                etb = tk.Entry(self.listFramevp,
                                justify="left",
                                )
                etb.grid(column = 2, 
                        row  = row,
                        sticky  = "ew",
                        )
                
                lbb = tk.Label(self.listFramevp,
                        text = "before",
                        )
                lbb.grid(column = 3, 
                        row = row,
                        sticky  = "w")
                        
                # after
                row += 1
                eta = tk.Entry(self.listFramevp,
                                justify="left",
                                )
                eta.grid(column = 2, 
                        row  = row,
                        sticky  = "ew",
                        )
                
                lba = tk.Label(self.listFramevp,
                        text = "After",
                        )
                lba.grid(column = 3, 
                        row = row,
                        sticky  = "w")

                # Left
                row += 1
                etl = tk.Entry(self.listFramevp,
                                justify="left",
                                )
                etl.grid(column = 2, 
                        row  = row,
                        sticky  = "ew",
                        )
                
                lbl = tk.Label(self.listFramevp,
                        text = "Left",
                        )
                lbl.grid(column = 3, 
                        row = row,
                        sticky  = "w")                        
                #right
                row += 1
                etr = tk.Entry(self.listFramevp,
                                justify="left",
                                )
                etr.grid(column = 2, 
                        row  = row,
                        sticky  = "ew",
                        )
                
                lbr = tk.Label(self.listFramevp,
                        text = "Right",
                        )
                lbr.grid(column = 3, 
                        row = row,
                        sticky  = "w")     
                

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
                labels = (wlb,lbh,cis,lbb,lba,lbl,lbl,em,arealb,sbs,lbr)
                for label in labels:
                        label.config (bg = self.bglb,
                                        font=self.labelfont,
                                        anchor="w")

                # config entry 
                entrys = (entryw,entryh,eme,etb,eta,etl,etr)
                for entry in entrys:
                        entry.config(font=self.labelfont_sm,
                                        bg = "white",
                                        relief = tk.SOLID)
                
        """delete value defaut entry """
        def some_callback(self,event): # note that you must include the event as an arg, even if you don't use it.
                self.adde.delete(0, "end")
                return None

        def createdrawing (self):
                #line 1
                row = 0 
                ci = tk.Label(self.listFramedr,
                                text = "Info house:"
                                )
                row = row + 1
                ci.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "w")
                
                #Line 2
                row = row + 1
                cis = tk.Label(self.listFramedr,
                                text = "Information of the house you want to build"
                                )
                cis.grid(column = 0, 
                                row  = row ,
                                padx = self.padx,
                                sticky  = "w",
                                columnspan = 4
                                )