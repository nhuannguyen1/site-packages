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
                        crwidth = 500,
                        crvheight = 500, 
                        scrollbarr = True,
                        bg = "deep sky blue"):
        #tk.Tk.__init__(self, listFrame)
        self.listFrame = listFrame
        self.cavwidth = cavwidth
        self.cavheight =cavheight
        self.crwidth = crwidth
        self.crvheight = crvheight
        self.scrollbarr = scrollbarr
        self.bg = bg
        Frame.__init__(self, listFrame)
        
    def createy1(self): 
        self.canvas = tk.Canvas(self.listFrame,
                                width=self.cavwidth,
                                height=self.cavheight, 
                                borderwidth=0, 
                                scrollregion= [0,0,1600,1000],
                                background= self.bg)   
                                                                    #place canvas on self
        self.listFramevp = tk.Frame(self.canvas, 
                                    background="deep sky blue",
                                    bd = 0)    
                                                                    #place a frame on the canvas, this frame will hold the child widgets 
        if self.scrollbarr ==True:
            self.vsb = tk.Scrollbar(self.listFrame, 
                                    orient="vertical", 
                                    command=self.canvas.yview)  
                                                                        #place a scrollbar on self 
            self.canvas.configure(yscrollcommand=self.vsb.set)            #attach scrollbar action to scroll of canvas

            self.vsb.pack(side="right",
                        fill="y") 
        elif  self.scrollbarr == 2:

            self.vsbv = tk.Scrollbar(self.listFrame, 
                                    orient="vertical", 
                                    command=self.canvas.yview)  
            
            self.vsbh = tk.Scrollbar(self.listFrame,
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
                                                        anchor="sw")                    #add view port frame to canva
        
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
                 scrollin = True,
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

        self.scrollin = scrollin

        self.hcreatewd = hcreatewd
        self.wcreatewd = wcreatewd


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
        self.canv = Canvas(self,bg='deep sky blue',
                          width=self.canvwidth,
                          height=self.canvheight,
                          scrollregion= [0,0,1600,1000])

        # frame to input 
        self.listFrame = cvframe(cavas=self.canv,
                                createwdy=self.createwdy,
                                createwdx=self.createwdx).rtframecv()
        #event to result
        self.listFrameevent = cvframe(cavas=self.canv,
                                        createwdy=530,
                                        createwdx=10).rtframecv()
        #image 
        self.frameimage = cvframe(cavas=self.canv,
                                    createwdy=10,
                                    createwdx=550).rtframecv()

        # print quotation 
        self.framequotation = cvframe(cavas=self.canv,
                                    createwdy=530,
                                    createwdx=550).rtframecv()

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

    def Frames(self):
      return self.listFrame

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
    def __init__(self,cavas = None,anchor = "nw", createwdx = 10,createwdy = 10):
        self.cavas = cavas
        self.anchor = anchor
        self.createwdx = createwdx
        self.createwdy = createwdy
    
    def rtframecv(self):
        self.listFrame =Frame(self.cavas)
        self.cavas.create_window((self.createwdx ,
                                self.createwdy),
                                window=self.listFrame,
                                anchor=self.anchor)
        return self.listFrame

class indatagui(Frame):
    def __init__(self,tktk = None,
                br_image = None,
                pathico = None,
                br_image_path = None):

        Frame.__init__(self, tktk)
        self.tktk = tktk

        self.br_image_path  = br_image_path

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

        #gui for inputdata 
        self.sc  = ScrolledCanvas(self.filewin)
        self.listframeindata = self.sc.listFrame
        self.listFramevp =  createcroll(listFrame=self.listframeindata,
                                        cavheight=450).createy1()

        # gui for resurlt
        self.listframert =self.sc.listFrameevent
        self.listFramevp2 = createcroll(listFrame=self.listframert,
                                        cavheight=450).createy1()
        self.seleevent()

        #set frame image 
        self.listframefim = self.sc.frameimage
        self.listFramevp4 =createcroll(listFrame=self.listframefim,
                                        cavwidth=1300,
                                        cavheight=450,
                                        scrollbarr=False).createy1()
        self.addimage()

        # add quotation 
        self.framequation = self.sc.framequotation
        
        self.framequationin =createcroll(listFrame=self.framequation,
                                        cavwidth=1300,
                                        cavheight=450,
                                        scrollbarr=False).createy1()
        
        self.quotationforctn()
        
        self.canv = self.sc.returncavas()

        # add buttom next and previous
        self.buttomandnext()

        #create buttom "Next"
        self.createbutton()

    def buttomandnext (self):

        button1 = Button(self.canv, 
                        text = "<<", 
                        anchor = CENTER)
        button1.configure(width = 3, 
                            activebackground = "#33B5E5", 
                            relief = FLAT)
        button1_window = self.canv.create_window(1170, 480, 
                                                anchor=NW, 
                                                window=button1)
        button1 = Button(self.canv, 
                        text = ">>", 
                        anchor = CENTER)
        button1.configure(width = 3, 
                            activebackground = "#33B5E5", 
                            relief = FLAT)
        button1_window = self.canv.create_window(1210, 480, 
                                                anchor=NW, 
                                                window=button1)      

    def addimage(self):
        price = tk.Label(self.listFramevp4,
                            image = self.br_image_path,
                            bd = 0
                        )
        price.pack(fill=BOTH ,expand=YES)

    def seleevent(self):
            columns = ("#1", "#2", "#3")
            self.tree = ttk.Treeview(self.listFramevp2, 
                                    show="headings", 
                                    columns=columns)
            self.tree.heading("#1", text="Option")
            self.tree.heading("#2", text="Description")
            self.tree.heading("#3", text="Price")
            #self.tree.bind("<<TreeviewSelect>>", self.print_selection)

            self.tree.pack(expand=YES,fill=BOTH)

            self.tree.column("#1",
                            minwidth=0,
                            width=150, 
                            stretch=NO)
            self.tree.column("#2",
                            minwidth=0,
                            width=150, 
                            stretch=NO)

            self.tree.column("#3",
                            minwidth=0,
                            width=150, 
                            stretch=NO)
    
    # qotation for container 
    def quotationforctn(self):
            # frame to modify date, issue
            frame1 = Frame(self.framequationin) 
            frame1.pack(pady = (0,10)) 

            b1 = Label(frame1, text = "Project ID") 
            b1.grid (column = 0, row = 0,sticky = tk.W)

            entryeditor = tk.Entry(frame1,
                            width = 15,
                            justify=CENTER
                            )
            entryeditor.grid (column = 1, row = 0)
            

            b1 = Label(frame1, text = "Project Name") 
            b1.grid (column = 2, row = 0,sticky = tk.W)

            entryeditor = tk.Entry(frame1,
                            width = 15,
                            justify=CENTER
                            )
            entryeditor.grid (column = 3, row = 00)


            b1 = Label(frame1, text = "Person editor") 
            b1.grid (column = 4, row = 0)

            entryeditor = tk.Entry(frame1,
                            width = 15,
                            justify=CENTER
                            )
            entryeditor.grid (column = 5, row = 0)

            
            b1 = Label(frame1, text = "Date Release") 
            b1.grid (column = 6, row = 0)

            entryeditor = tk.Entry(frame1,
                            width = 15,
                            justify=CENTER
                            )
            entryeditor.grid (column = 7, row = 0)
            


            columns = ("#1", "#2", "#3","#4", "#5", "#6","#7")
            self.tree = ttk.Treeview(self.framequationin, 
                                    show="headings", 
                                    columns=columns)
            self.tree.heading("#1", text="NO.")
            self.tree.heading("#2", text="DESCRIPTION")
            self.tree.heading("#3", text="UNIT")
            self.tree.heading("#4", text="QUANTITY")
            self.tree.heading("#5", text="AMOUNT")
            self.tree.heading("#6", text="REMARK")
            self.tree.heading("#7", text="NOTE")

            xsb = ttk.Scrollbar(self.framequationin,
                                orient = tk.HORIZONTAL,
                                command = self.tree.xview)
            xsb.pack(side=BOTTOM,
                        fill=X)
            
            ysb = ttk.Scrollbar(self.framequationin,orient = tk.VERTICAL,command = self.tree.yview)

            ysb.pack(side=RIGHT,
                        fill=Y)

            self.tree.configure(xscroll = xsb.set,yscroll = ysb.set)
            #self.tree.bind("<<TreeviewSelect>>", self.print_selection)
            xsb.config(command = self.tree.xview)
            ysb.config(command = self.tree.yview)

            self.tree.pack(expand=YES,fill=BOTH,side = BOTTOM)

            self.tree.column("#1",
                            minwidth=0,
                            width=50, 
                            stretch=NO)
            self.tree.column("#2",
                            minwidth=0,
                            width=300, 
                            stretch=NO)

            self.tree.column("#3",
                            minwidth=0,
                            width=50, 
                            stretch=NO)
            self.tree.column("#4",
                            minwidth=0,
                            width=300, 
                            stretch=NO)
            self.tree.column("#5",
                            minwidth=0,
                            width=300, 
                            stretch=NO)
            self.tree.column("#6",
                            minwidth=0,
                            width=300, 
                            stretch=NO)
            self.tree.column("#7",
                            minwidth=0,
                            width=300, 
                            stretch=NO)

    def createbutton (self):

      button1 = Button(self.canv, 
                      text = "FIND", 
                      anchor = CENTER)
      button1.configure(width = 10, 
                        activebackground = "#33B5E5", 
                        relief = FLAT)
      button1_window = self.canv.create_window(180, 480, 
                                              anchor=NW, 
                                              window=button1)

    def creategui(self):      
        price = tk.Label(self.listFramevp,text = "Price you can pay ?",
                            width = 40,
                            height = 1,
                            )
        price.grid(column = 0, 
                  row = 0,
                  pady = 20, 
                  padx = 10,
                  sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, 
                        row  = 0 ,
                        pady = 20,
                        padx = 10,
                        ipady=2)
        
        #area 
        area = tk.Label(self.listFramevp,text = "How much house area do you want ?",
                            width = 40,
                            height = 1,
                            )
        area.grid(column = 0, 
                  row = 1,
                  pady = 20)
        #area m2
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, 
                  row = 1,
                  pady = 20,
                  ipady=2)

        #many room 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 1,
                            )
        area.grid(column = 0, 
                  row = 2,
                  pady = 20)

        #many room
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 2,
                  pady = 20,
                  ipady=2)

        #many toilet 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 1,
                            )
        area.grid(column = 0, 
                  row = 3,
                  pady = 20)

        #many toilet
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 3,
                  pady = 20,
                  ipady=2)


        ######### colum 0 and 1
        price = tk.Label(self.listFramevp,text = "Price you can pay ?",
                            width = 40,
                            height = 1,
                            )
        price.grid(column = 0, 
                    row = 4,
                    pady = 20, 
                    padx = 10,
                    sticky  = SE)

        #input price
        inputprice = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, 
                        row  = 4 ,
                        pady = 20,
                        padx = 10,
                        ipady=2)
        
        #area 
        area = tk.Label(self.listFramevp,text = "How much house area do you want ?",
                            width = 40,
                            height = 1,
                            )
        area.grid(column = 0, 
                  row = 5,
                  pady = 20)

        #area m2
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, 
                  row = 5,
                  pady = 20,
                  ipady=2)

        #many room 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 1,
                            )
        area.grid(column = 0, row = 6,pady = 20)

        #many room
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 6,
                  pady = 20,
                  ipady=2)

        #many toilet 
        area = tk.Label(self.listFramevp,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 1,
                            )
        area.grid(column = 0, 
                  row = 7,
                  pady = 20)

        #many toilet
        aream = tk.Entry(self.listFramevp,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, 
                  row = 7,
                  pady = 20,
                  ipady=2)