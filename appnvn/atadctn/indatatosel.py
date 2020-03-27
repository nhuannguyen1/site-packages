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

        self.__create_new()

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
      
        price = tk.Label(self.listFramevp,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 0,pady = 10, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 0 ,pady = 10,padx = 10,ipady=2)
        
        #area 
        area = tk.Label(self.listFramevp,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 1,pady = 10)
        #area m2
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 1,pady = 10,ipady=2)

        #many room 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 2,pady = 10)

        #many room
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 2,pady = 10,ipady=2)

        #many toilet 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 3,pady = 10)

        #many toilet
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 3,pady = 10,ipady=2)


        ######### colum 0 and 1
        price = tk.Label(self.listFramevp,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 4,pady = 10, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 4 ,pady = 10,padx = 10,ipady=2)
        
        #area 
        area = tk.Label(self.listFramevp,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 5,pady = 10)

        #area m2
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 5,pady = 10,ipady=2)

        #many room 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 6,pady = 10)

        #many room
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 6,pady = 10,ipady=2)

        #many toilet 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 7,pady = 10)

        #many toilet
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 7,pady = 10,ipady=2)
        #find
        find = Button(self.listFramevp,text = "FIND",
                            width = 10,
                            height = 2,
                            )
        find.grid(column = 0, row = 8,pady = 10,sticky  = E)

        ########################################################################################3
        price = tk.Label(self.listFrame1,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 0,pady = 10, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFrame1,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 0 ,pady = 10,padx = 10,ipady=2)


  
    def __create_canvas(self):
        # create white area in the window for plotting
        # width and height are only the visible size of the white area, scrollregion is the area the user can see by scrolling
        self.canv = Canvas(self,bg='#FFFFFF',width=900,height=900,scrollregion=(0,0,1500,1000))
        self.listFrame1=Frame(self.canv)
        self.listFrame=Frame(self.canv)
        self.canv.create_window((10,10),window=self.listFrame,anchor='nw')
        self.canv.create_window((700,10),window=self.listFrame1,anchor='n')
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH) 

        # position and size of the canvas is used for configuration of the scroll bars
        self.canv.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # add command to the scroll bars to scroll the canvas
        self.hbar.config(command = self.canv.xview)
        self.vbar.config(command = self.canv.yview)
    def __create_new(self):
        self.canvas = tk.Canvas(listFrame, borderwidth=0, background="#ffffff")                            #place canvas on self
        self.listFramevp = tk.Frame(self.canvas, background="#ffffff")                                    #place a frame on the canvas, this frame will hold the child widgets 
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)                       #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)                                                #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                                               #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                                             #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.listFramevp, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None) 

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.                     
    
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
 
