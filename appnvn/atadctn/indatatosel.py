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
        self.canv = Canvas(self)
        self.canv.config(width=500, height=500)                
        self.canv.config(scrollregion=(0,0,400, 400))

        self.__add_scroll_bars() 



        self.__create_canvas()        
        """
        sbar = Scrollbar(self)
        sbar.config(command=self.canv.yview)                   
        self.canv.config(yscrollcommand=sbar.set)              
        sbar.pack(side=RIGHT, fill=Y) 
        """  
        self.listFrame=Frame(self.canv)
        self.canv.create_window((0,0),window=self.listFrame,anchor='nw')
        #self.listFrame.bind("<Configure>", self.AuxscrollFunction)
        self.canv.pack(side=LEFT, expand=YES, fill=BOTH) 
        # create gui for sw
        self.__gui_input()

    def AuxscrollFunction(self,event):
        #You need to set a max size for frameTwo. Otherwise, it will grow as needed, and scrollbar do not act
        self.canv.configure(scrollregion=self.canv.bbox("all"),width=600,height=500)
        #canv.bind('<Double-1>', self.onDoubleClick)       # set event handler
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
        self.canvas = Canvas(self.frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))

        # with this command the window is filled with the canvas
        self.canvas.pack(side=LEFT)

        # position and size of the canvas is used for configuration of the scroll bars
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)

        # add command to the scroll bars to scroll the canvas
        self.hbar.config(command = self.canvas.xview)
        self.vbar.config(command = self.canvas.yview)

class SlowCH_Manager(Canvas):
    """ 
    Manages a variable number of slow channel massages
    """
    def __init__(self,master=None,**kwargs):
        Canvas.__init__(self,master,**kwargs)
        self.frame = Frame(self)

        self.create_window(0,0,anchor=N+W,window=self.frame)
        self._init_entries()

    def _init_entries(self):
        """
        initialize the input area with labels and perhaps default values
        """
        """
        label_id  = Label(self.frame, text='message ID').grid(row = self.row, column = 1)
        label_msg = Label(self.frame, text='message data').grid(row = self.row, column = 2)
        self.row += 1
        """
        price = tk.Label(self.frame,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 0,pady = 30, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 0 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.frame,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 1,pady = 30)

        #area m2
        aream = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 1,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.frame,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 2,pady = 30)

        #many room
        aream = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 2,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.frame,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 3,pady = 30)

        #many toilet
        aream = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 3,pady = 30,ipady=8)


        ######### colum 0 and 1
        price = tk.Label(self.frame,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 4,pady = 30, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 4 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.frame,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 5,pady = 30)

        #area m2
        aream = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 5,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.frame,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 6,pady = 30)

        #many room
        aream = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 6,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.frame,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 7,pady = 30)

        #many toilet
        aream = tk.Entry(self.frame,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 7,pady = 30,ipady=8)
"""
class DoubleScrollbarFrame(ttk.Frame):

  def __init__(self, master, **kwargs):
    '''
      Initialisation. The DoubleScrollbarFrame consist of :
        - an horizontal scrollbar
        - a  vertical   scrollbar
        - a canvas in which the user can place sub-elements
    '''

    ttk.Frame.__init__(self,  master, **kwargs)

    # Canvas creation with double scrollbar
    self.hscrollbar = ttk.Scrollbar(self, orient = tk.HORIZONTAL)
    self.vscrollbar = ttk.Scrollbar(self, orient = tk.VERTICAL)
    self.sizegrip = ttk.Sizegrip(self)
    self.canvas = tk.Canvas(self, bd=0, highlightthickness=0,yscrollcommand = self.vscrollbar.set,xscrollcommand = self.hscrollbar.set)
    self.vscrollbar.config(command = self.canvas.yview)
    self.hscrollbar.config(command = self.canvas.xview)
    self.canvas.configure(scrollregion = self.canvas.bbox("all"))

  def pack(self, **kwargs):
    '''
      Pack the scrollbar and canvas correctly in order to recreate the same look as MFC's windows. 
    '''

    self.hscrollbar.pack(side=tk.BOTTOM, fill=tk.X, expand=tk.FALSE)
    self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y,  expand=tk.FALSE)
    self.sizegrip.pack(in_ = self.hscrollbar, side = tk.BOTTOM, anchor = "se")
    self.canvas.pack(side=tk.LEFT, padx=5, pady=5,
                                             fill=tk.BOTH, expand=tk.TRUE)

    ttk.Frame.pack(self, **kwargs)
    
  def get_frame(self):
    '''
      Return the "frame" useful to place inner controls.
    '''
    return self.canvas
"""
    
class indatagui:
    def __init__(self,tktk = None,br_image = None,pathico = None):
         
        self.tktk = tktk
        self.filewin = Toplevel(self.tktk)

        ScrolledCanvas(self.filewin)
        """
        self.manager = SlowCH_Manager(self.filewin)
        self.manager.grid(row=0,column=0)

        scroll = Scrollbar(self.filewin )
        scroll.grid(row=0,column=1,sticky=N+S)

        self.manager.config(yscrollcommand = scroll.set)
        scroll.config(command=self.manager.yview)
        self.manager.bind("<Configure>", self.AuxscrollFunction)
        """
