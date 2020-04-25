from tkinter import *
import tkinter as tk
from pynvn.path.ppath import PathFromFileNameAndDirpath
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
import os
from tkinter import ttk
class createcroll(Frame):
    def __init__ (self,listFrame = None, 
                        cavwidth = 430,
                        cavheight = 430,
                        crwidth = 30,
                        crvheight = 30, 
                        scrollbarr = True,
                        bg = "slate gray"):
        #tk.Tk.__init__(self, listFrame)
        self.listFrame = listFrame
        self.cavwidth = cavwidth
        self.cavheight =cavheight
        self.crwidth = crwidth
        self.crvheight = crvheight
        self.scrollbarr = scrollbarr
        self.bg = bg
        Frame.__init__(self, listFrame)
        self.pack(fill = BOTH)

    def createy1(self): 
        self.canvas = tk.Canvas(self,
                                width=self.cavwidth,
                                height=self.cavheight, 
                                borderwidth=0, 
                                background= self.bg)  #place canvas on self

        self.listFramevp = tk.Frame(self.canvas, 
                                    background=self.bg,
                                    bd = 0) #place a frame on the canvas, this frame will hold the child widgets 

        if self.scrollbarr ==True:
            self.vsb = tk.Scrollbar(self, 
                                    orient="vertical", 
                                    command=self.canvas.yview)  
                                                                        #place a scrollbar on self 
            self.canvas.configure(yscrollcommand=self.vsb.set)            #attach scrollbar action to scroll of canvas

            self.vsb.pack(side="right",
                        fill="y") 
        elif  self.scrollbarr == 2:

            self.vsbv = tk.Scrollbar(self, 
                                    orient="vertical", 
                                    command=self.canvas.yview)  
            
            self.vsbh = tk.Scrollbar(self,
                                    orient="horizontal", 
                                    command=self.canvas.xview)   #place a scrollbar on self 
                                                                        #place a scrollbar on self 

            self.canvas.configure(xscrollcommand=self.vsbh.set,yscrollcommand=self.vsbv.set)            #attach scrollbar action to scroll of canvas

            self.vsbv.pack(side="right",
                        fill="y") 
            self.vsbh.pack(side="bottom",
                        fill="x") 

        self.canvas.pack(side="left", 
                        fill="both", 
                        expand=True)    
                                                                 #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((self.crwidth,
                                                        self.crvheight), 
                                                        window=self.listFramevp, 
                                                        anchor="center")                    #add view port frame to canva
        
        self.listFramevp.bind("<Configure>", 
                              self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        
        self.canvas.bind("<Configure>",
                           self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None) 
        return self.listFramevp

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, 
                              width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.        
                              

class ScrolledCanvas(Frame):
    def __init__(self, parent=None,
                 hbarori =HORIZONTAL,
                 hbarside =BOTTOM,
                 vbarori = VERTICAL,
                 vbarside =RIGHT,
                 canvwidth = 900,
                 canvheight = 900,
                 scrolldownarr = [0,0,1000,1000],
                 createwdx = 10,
                 createwdy = 10,
                 hcreatewd = 0,
                 wcreatewd = 0,
                 scrollin = True,
                 framea_cw = [10,10],  # listframe 
                 frameb_cw = [10,525], # event
                 framec_cw = [520,10], # image 
                 framed_cw = [520,525],# quotion 
                 bg = "slate gray",
                 
                 color='brown'):

        Frame.__init__(self, parent)
        self.parent = parent
        self.hbarori = hbarori
        self.hbarside = hbarside
        self.vbarori = vbarori
        self.vbarside = vbarside
        self.canvwidth = canvwidth
        self.canvheight = canvheight
        self.scrolldownarr = scrolldownarr
        self.createwdx = createwdx
        self.createwdy = createwdy

        self.scrollin = scrollin

        self.hcreatewd = hcreatewd
        self.wcreatewd = wcreatewd
        self.framea_cw = framea_cw
        self.frameb_cw = frameb_cw
        self.framec_cw = framec_cw
        self.framed_cw = framed_cw
        self.bg = bg

        self.pack(expand=True, 
                  fill=BOTH) 

        self.__add_scroll_bars() 
        self.__create_canvas()

        self.__addcommmandscroll()

        #self.returnframe()
        

    def __add_scroll_bars(self):
        
        # add scroll bars
        self.hbar=Scrollbar(self,
                            orient=self.hbarori)
        self.hbar.pack(side=self.hbarside,
                      fill=X)
        self.vbar=Scrollbar(self,
                            orient=self.vbarori )
        self.vbar.pack(side=self.vbarside,
                        fill=Y)

       

    def __create_canvas(self):
        # create white area in the window for plotting
        # width and height are only the visible size of the white area, scrollregion is the area the user can see by scrolling
        self.canv = Canvas(self,bg=self.bg,
                          width=self.canvwidth,
                          height=self.canvheight,
                          scrollregion= [0,0,1600,1000])

        # frame to input 
        if self.framea_cw != NONE:
            self.framea = cvframe(cavas=self.canv,
                                    createwdy=self.framea_cw[1],
                                    createwdx=self.framea_cw[0]).rtframecv()
        #event to result
        if self.frameb_cw != NONE:
            self.frameb = cvframe(cavas=self.canv,
                                        createwdy = self.frameb_cw[1],
                                        createwdx = self.frameb_cw[0]).rtframecv()
        #image 
        if self.framec_cw != NONE:
            self.framec = cvframe(cavas=self.canv,
                                        createwdy=self.framec_cw[1],
                                        createwdx=self.framec_cw[0]).rtframecv()

        # print quotation 
        if self.framed_cw != NONE:
            self.framed = cvframe(cavas=self.canv,
                                        createwdy=self.framed_cw[1],
                                        createwdx=self.framed_cw[0]).rtframecv()

        self.canv.pack(side=LEFT,
                       expand=YES, 
                       fill=BOTH) 
    
    def __addcommmandscroll (self):
        # position and size of the canvas is used for configuration of the scroll bars
        self.canv.config(xscrollcommand=self.hbar.set, 
                        yscrollcommand=self.vbar.set)

        # add command to the scroll bars to scroll the canvas
        self.hbar.config(command = self.canv.xview)
        self.vbar.config(command = self.canv.yview)


    def returncavas (self):
      return self.canv
    
    @property
    def createwdxt(self):
        return self.createwdx
    @createwdxt.setter
    def createwdxt(self,createwdxname):
        self.createwdx = createwdxname
    
    @property
    def createwdyt(self):
        return self.createwdx

    @createwdyt.setter
    def createwdyt(self,createwdyname):
        self.createwdy = createwdyname

class cvframe:
    def __init__(self,cavas = None,
                    anchor = "nw", 
                    createwdx = 10,
                    createwdy = 10):
        self.cavas = cavas
        self.anchor = anchor
        self.createwdx = createwdx
        self.createwdy = createwdy
    
    def rtframecv(self):
        self.listFrame =Frame(self.cavas)
        self.cavas.create_window(self.createwdx,
                                self.createwdy,
                                window=self.listFrame,
                                anchor=self.anchor)
        return self.listFrame

class cvframeg:
    """using for gird return listframe"""
    def __init__(self,cavas = None,
                anchor = "nw",
                createwdx = 10,
                createwdy = 10,
                bg = "pink"):
        self.cavas = cavas
        self.anchor = anchor
        self.createwdx = createwdx
        self.createwdy = createwdy
        self.bg = bg
    
    def rtframecv(self):
        # creating canvas contents 

        self.framecv = Frame(self.cavas,
                            width=500,
                            height=500, 
                            background=self.bg) 
        """
        self.framecv.rowconfigure(0, 
                                weight=1) 

        self.framecv.columnconfigure(0, 
                                    weight=1) 
        """

        self.window = self.cavas.create_window((self.createwdx,
                                                self.createwdy), 
                                                anchor=self.anchor, 
                                                window=self.framecv) 
        return self.framecv
    def retwindow(self):
        return self.window

class treescrollbar:

    def __init__(self,frame = None,orienth = HORIZONTAL, orienthv = VERTICAL, tree = None):
        self.frame = frame
        self.orienth =orienth
        self.orienthv = orienthv
        self.tree = tree

    def treescrollbar2r(self):
            xsb = ttk.Scrollbar(self.frame,
                                orient =  self.orienth,
                                command = self.tree.xview)
            xsb.pack(side=BOTTOM,
                        fill=X)
            
            ysb = ttk.Scrollbar(self.frame,
                                orient = self.orienthv,
                                command = self.tree.yview)

            ysb.pack(side=RIGHT,
                        fill=Y)

            self.tree.configure(xscroll = xsb.set,
                                yscroll = ysb.set)

            xsb.config(command = self.tree.xview)
            ysb.config(command = self.tree.yview)


class AutoScrollbar(Scrollbar): 

    # Defining set method with all  

    # its parameter 

    def set(self, low, high): 

        if float(low) <= 0.0 and float(high) >= 1.0: 

            # Using grid_remove 

            self.tk.call("grid", "remove", self) 
            
        else: 

            self.grid() 

        Scrollbar.set(self, low, high) 
  
# creating tkinter window  

class scbg (tk.Frame):
    """ create AutoScrollbar follow gird """
    def __init__ (self,parent = None,
                        bg = "SteelBlue1",
                        framea_cw = [10,10],
                        cavwidth = 900,
                        cavheight = 900):
        self.bg = bg
        self.cavwidth = cavwidth
        self.cavheight =cavheight
        self.framea_cw = framea_cw
        super().__init__(parent,bg =self.bg)
        self.parent = parent
        self.pack(fill = BOTH, expand = True)
        self.add_scroll_bars()
        self.create_canvas()
        self.addcommmandscroll()
        self.conf()
    
    def add_scroll_bars(self):
        """add scroll bar """
        # Defining vertical scrollbar 
        self.verscrollbar = AutoScrollbar(self) 
        # Calling grid method with all its 
        # parameter w.r.t vertical scrollbar 
        self.verscrollbar.grid(row=0, column=1,sticky=N+S) 
        # Defining horizontal scrollbar 
        self.horiscrollbar = AutoScrollbar(self,orient=HORIZONTAL) 
        # Calling grid method with all its  
        self.horiscrollbar.grid(row=1, column=0, sticky=E+W) 

    def create_canvas(self):
        """Creating scrolled canvas """
        self.canvas = Canvas(self,
                            bg = "red",
                            width=self.cavwidth,
                            height=self.cavheight 
                            ) 
        self.canvas.grid(row=0, 
                        column=0, 
                        sticky=N+S+E+W) 

        # Making the canvas expandable 
        self.grid_rowconfigure(0, weight=1) 
        self.grid_columnconfigure(0, weight=1) 
        x0 = 0
        y0 = 0
        cvf = cvframeg(cavas=self.canvas,
                        createwdx=x0,
                        createwdy=y0)
        self.framecv = cvf.rtframecv()
        self.window = cvf.window

    def addcommmandscroll (self):
        """set and add scroll bar """
        self.canvas.config(xscrollcommand=self.horiscrollbar.set, 
                            yscrollcommand=self.verscrollbar.set)
        self.verscrollbar.config(command=self.canvas.yview) 
        self.horiscrollbar.config(command=self.canvas.xview) 

    def conf (self):
        """ Configuring canvas """  
        self.framecv.update_idletasks()
        self.framecv.bind("<Configure>",self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>",self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.window, 
                              width = canvas_width)            #whenever the size of the canvas changes alter the window region respectively.   
    
    def returnframe(self):
        """return framecv"""
        return self.framecv