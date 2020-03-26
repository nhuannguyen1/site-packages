from tkinter import *
import tkinter as tk
from PIL import ImageTk
from pynvn.path.ppath import PathFromFileNameAndDirpath
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
import os
from tkinter import ttk

class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='brown'):
        Frame.__init__(self, parent)
        
        self.pack(expand=True, fill=BOTH) 

        self.__add_scroll_bars() 

        self.__create_canvas()        
        # create gui for sw
        self.__gui_input()

    def AuxscrollFunction(self,event):
        #You need to set a max size for frameTwo. Otherwise, it will grow as needed, and scrollbar do not act
        self.canv.configure(scrollregion=self.canv.bbox("all"),width=600,height=500)
        #self.canvas = canv
    def __add_scroll_bars(self):
        # add scroll bars
        self.hbar=Scrollbar(self,orient=HORIZONTAL)
        self.hbar.pack(side=BOTTOM,fill=X)
        self.vbar=Scrollbar(self,orient=VERTICAL)
        self.vbar.pack(side=RIGHT,fill=Y)
    def __gui_input(self):
      
        price = tk.Label(self.listFrame,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 0,pady = 30, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 0 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.listFrame,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 1,pady = 30)
        #area m2
        aream = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 1,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.listFrame,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 2,pady = 30)

        #many room
        aream = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 2,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.listFrame,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 3,pady = 30)

        #many toilet
        aream = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 3,pady = 30,ipady=8)


        ######### colum 0 and 1
        price = tk.Label(self.listFrame,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 4,pady = 30, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 4 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.listFrame,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 5,pady = 30)

        #area m2
        aream = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 5,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.listFrame,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 6,pady = 30)

        #many room
        aream = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 6,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.listFrame,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 7,pady = 30)

        #many toilet
        aream = tk.Entry(self.listFrame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 7,pady = 30,ipady=8)
  
    def __create_canvas(self):
        # create white area in the window for plotting
        # width and height are only the visible size of the white area, scrollregion is the area the user can see by scrolling
        self.canv = Canvas(self,bg='#FFFFFF',width=500,height=500,scrollregion=(0,0,600,600))
        self.listFrame=Frame(self.canv)
        self.canv.create_window((10,10),window=self.listFrame,anchor='nw')
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH) 

        # with this command the window is filled with the canvas
        self.canv.pack(side=LEFT)

        # position and size of the canvas is used for configuration of the scroll bars
        self.canv.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # add command to the scroll bars to scroll the canvas
        self.hbar.config(command = self.canv.xview)
        self.vbar.config(command = self.canv.yview)
    
class indatagui:
    def __init__(self,tktk = None,
                br_image = None,
                pathico = None):
         
        self.tktk = tktk

        self.br_image = br_image

        self.pathico = pathico

        self.filewin = Toplevel(self.tktk)

        gui (tktk=self.filewin,
                    pathico=self.pathico,
                    width=700,
                    height=450,
                    widthx=700,
                    widthy=0,
                    resizable=[True,True]).setcfbs()
        # set menu 
        menu (tktk=self.filewin).createmenu()
        ScrolledCanvas(self.filewin)
 
