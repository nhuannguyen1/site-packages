from tkinter import *
import tkinter as tk
from PIL import ImageTk
from pynvn.path.ppath import PathFromFileNameAndDirpath
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
import os
from tkinter import ttk
class createcroll(Frame):
    def __init__ (self,listFrame = None, cavwidth = 430,cavheight = 430,crwidth = 500,crvheight = 500):
        #tk.Tk.__init__(self, listFrame)
        self.listFrame = listFrame
        self.cavwidth = cavwidth
        self.cavheight =cavheight
        self.crwidth = crwidth
        self.crvheight = crvheight
        Frame.__init__(self, listFrame)
        
    def createy1(self):
        self.canvas = tk.Canvas(self.listFrame,
                                width=self.cavwidth,
                                height=self.cavheight, 
                                borderwidth=10, 
                                background="deep sky blue")   
                                                                    #place canvas on self
        self.listFramevp = tk.Frame(self.canvas, 
                                    background="deep sky blue")    
                                                                    #place a frame on the canvas, this frame will hold the child widgets 

        self.vsb = tk.Scrollbar(self.listFrame, 
                                orient="vertical", 
                                command=self.canvas.yview)  
                                                                      #place a scrollbar on self 
        self.canvas.configure(yscrollcommand=self.vsb.set)            #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right",
                       fill="y")  
                                                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", 
                        fill="both", 
                        expand=True)    
                                                                 #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((self.crwidth,self.crvheight), 
                                  window=self.listFramevp, 
                                  anchor="nw",                    #add view port frame to canvas
                                  tags="self.viewPort")

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
                 scrolldownarr = (0,0,1000,1000),
                 createwdx = 10,
                 createwdy = 10,
                 hcreatewd = 0,
                 wcreatewd = 0,
                 color='brown'):

        Frame.__init__(self, parent)

        self.hbarori = hbarori
        self.hbarside = hbarside
        self.vbarori = vbarori
        self.vbarside = vbarside
        self.canvwidth = canvwidth
        self.canvheight = canvheight
        self.scrolldownarr = scrolldownarr
        self.createwdx = createwdx
        self.createwdy = createwdy

        self.hcreatewd = hcreatewd
        self.wcreatewd = wcreatewd


        self.pack(expand=True, 
                  fill=BOTH) 
        self.__add_scroll_bars() 
        self.__create_canvas()
        self.returnframe()

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
        self.canv = Canvas(self,bg='deep sky blue',
                          width=self.canvwidth,
                          height=self.canvheight,
                          scrollregion= self.scrolldownarr)
        # input data
        self.listFrame=Frame(self.canv)

        self.canv.create_window((self.createwdx ,
                                self.createwdy),
                                window=self.listFrame,
                                anchor='nw')
        # result
        self.listFrameevent=Frame(self.canv)

        self.canv.create_window((10 ,550),
                                window=self.listFrameevent,
                                anchor='nw')
        # list frame to get image 
        self.frameimage=Frame(self.canv)

        self.canv.create_window((550 ,10),
                                window=self.frameimage,
                                anchor='nw')

        self.canv.pack(side=LEFT,
                       expand=YES, 
                       fill=BOTH) 

        # position and size of the canvas is used for configuration of the scroll bars
        self.canv.config(xscrollcommand=self.hbar.set, 
                        yscrollcommand=self.vbar.set)

        # add command to the scroll bars to scroll the canvas
        self.hbar.config(command = self.canv.xview)
        self.vbar.config(command = self.canv.yview)

    def returnframe(self):
      return self.listFrame

    def returnframekid(self):
      return createcroll(listFrame=self.listFrame).createy1()

    def returnframekid2(self):
      return createcroll(listFrame=self.listFrameevent).createy1()

    def frameimagef (self):
        return createcroll(listFrame=self.frameimage).createy1()

    def returncavas (self):
      return self.canv


class indatagui(Frame):
    def __init__(self,tktk = None,
                br_image = None,
                pathico = None):
        Frame.__init__(self, tktk)
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
        sc = ScrolledCanvas(self.filewin)
        self.listFramevp = sc.returnframekid()

        self.listFramevp2 = sc.returnframekid2()

        #create buttom "Next"
        self.canv = sc.returncavas()
        self.createbutton()

        self.seleevent()

        #set frame image 
        self.listFramevp4 =sc.frameimagef()

        self.onlytest()
    def onlytest(self):
        price = tk.Label(self.listFramevp4,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, 
                  row = 0,
                  pady = 10, 
                  padx = 10,
                  sticky  = SE)

    def seleevent(self):
            columns = ("#1", "#2", "#3")
            self.tree = ttk.Treeview(self.listFramevp2, show="headings", columns=columns)
            self.tree.heading("#1", text="Option")
            self.tree.heading("#2", text="Description")
            self.tree.heading("#3", text="Price")
            self.tree.bind("<<TreeviewSelect>>", self.print_selection)
            self.tree.pack(expand=YES,fill=BOTH)
            self.tree.column("#1",minwidth=0,width=150, stretch=NO)
            self.tree.column("#2",minwidth=0,width=150, stretch=NO)
            self.tree.column("#3",minwidth=0,width=150, stretch=NO)
            
    def print_selection(self, event):
            for selection in self.tree.selection():
                item = self.tree.item(selection)
                last_name, first_name, email = item["values"][0:3]
                text = "Selection: {}, {} <{}>"
                print(text.format(last_name, first_name, email))
      
    def createbutton (self):

      button1 = Button(self.canv, 
                      text = "FIND", 
                      anchor = CENTER)
      button1.configure(width = 10, 
                        activebackground = "#33B5E5", 
                        relief = FLAT)
      button1_window = self.canv.create_window(190, 500, 
                                              anchor=NW, 
                                              window=button1)

    def creategui(self):      
        price = tk.Label(self.listFramevp,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, 
                  row = 0,
                  pady = 10, 
                  padx = 10,
                  sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, 
                        row  = 0 ,
                        pady = 10,
                        padx = 10,
                        ipady=2)
        
        #area 
        area = tk.Label(self.listFramevp,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, 
                  row = 1,
                  pady = 10)
        #area m2
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, 
                  row = 1,
                  pady = 10,
                  ipady=2)

        #many room 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, 
                  row = 2,
                  pady = 10)

        #many room
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 2,
                  pady = 10,
                  ipady=2)

        #many toilet 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, 
                  row = 3,
                  pady = 10)

        #many toilet
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 3,
                  pady = 10,
                  ipady=2)


        ######### colum 0 and 1
        price = tk.Label(self.listFramevp,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, 
                    row = 4,
                    pady = 10, 
                    padx = 10,
                    sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, 
                        row  = 4 ,
                        pady = 10,
                        padx = 10,
                        ipady=2)
        
        #area 
        area = tk.Label(self.listFramevp,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, 
                  row = 5,
                  pady = 10)

        #area m2
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, 
                  row = 5,
                  pady = 10,
                  ipady=2)

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
        aream.grid(column = 1, 
                  row = 6,
                  pady = 10,
                  ipady=2)

        #many toilet 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, 
                  row = 7,
                  pady = 10)

        #many toilet
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 7,
                  pady = 10,
                  ipady=2)
        #find
        find = Button(self.listFramevp,text = "FIND",
                            width = 10,
                            height = 2,
                            )
        find.grid(column = 0, 
                  row = 8,
                  pady = 10,
                  sticky  = E)