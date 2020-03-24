from tkinter import *
import tkinter as tk
from PIL import ImageTk
from pynvn.path.ppath import PathFromFileNameAndDirpath
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
import os
# Class to create scrollbar 
class listFrame:
    def __init__(self,master):
        self.master = master
        #create vertical scrollbar 
        self.scroll = tk.Scrollbar (self.master )
        self.scroll.pack (side = tk.LEFT, 
                        fill = tk.Y)
    
class indatagui:
    def __init__(self,tktk = None,br_image = None,pathico = None):
         
        self.tktk = tktk
        self.filewin = Toplevel(self.tktk)

        #self.scroll = tk.Scrollbar (self.filewin)
        #self.scroll.pack (side = tk.LEFT,fill = tk.Y)

        #self.filewin = listFrame(master = self.filewin1 )
        #self.filewin.attributes('-alpha', 0.3)
        menu (tktk=self.filewin).createmenu()
        self.br_image = br_image
        self.pathico = pathico

        gui (tktk=self.filewin,
            pathico=self.pathico,
            width=1200,
            height=450,
            widthx=700,
            widthy=0,
            resizable=[TRUE,TRUE]).setcfbs()
            
        

        """

        lgbr = Label (self.filewin, image = self.br_image)
        lgbr.grid(row=0, column=0)
        
        root = Tk()

        manager = SlowCH_Manager(root)
        manager.grid(row=0,column=0)

        scroll = Scrollbar(root)
        scroll.grid(row=0,column=1,sticky=N+S)

        manager.config(yscrollcommand = scroll.set)
        scroll.config(command=manager.yview)
        manager.configure(scrollregion = manager.bbox("all"))
        """

        #self.container = Frame (self.filewin,bg = "cornflower blue")
        self.container = Frame (self.filewin)

        
        #self.scroll = tk.Scrollbar (self.container)
        #self.scroll.pack (side = RIGHT)
        


        self.container.grid(row=0,column=0)

        scroll = Scrollbar(self.filewin)
        scroll.grid(row=0,column=1,sticky=N+S)

        self.container.config(yscrollcommand = scroll.set)
        scroll.config(command=manager.yview)
        self.container.configure(scrollregion = self.container.bbox("all"))
        
        #self.container.grid (row=0, column=2)

        """
        lgbr1 = Label (self.container, image = self.br_image)
        #lgbr1.pack()
        lgbr1.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.container.place( x = 0, 
                           y = 0,
                           relwidth  = 1.0,
                           )
        """
        #self.container = listFrame(master = self.container)
    # create gui     
    def creategui(self):
        #create buttom for open file 
        #price 
        ######### colum 0 and 1
        price = tk.Label(self.container,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 0,pady = 30, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 0 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.container,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 1,pady = 30)

        #area m2
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 1,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.container,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 2,pady = 30)

        #many room
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 2,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.container,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 3,pady = 30)

        #many toilet
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 3,pady = 30,ipady=8)
        """
        ################################################# colum 2 and 3
        price = tk.Label(self.container,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 2, row = 0,pady = 30, padx = 10)

        #input price
        inputprice = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 3, row  = 0 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.container,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 2, row = 1,pady = 30)

        #area m2
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 3, row = 1,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.container,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 2, row = 2,pady = 30)

        #many room
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 3, row = 2,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.container,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 2, row = 3,pady = 30)

        #many toilet
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 3, row = 3,pady = 30,ipady=8)        

        """



        ######### colum 0 and 1
        price = tk.Label(self.container,text = "Price you can pay ?",
                            width = 40,
                            height = 2,
                            )
        price.grid(column = 0, row = 4,pady = 30, padx = 10,sticky  = SE)

        #input price
        inputprice = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        inputprice.grid(column = 1, row  = 4 ,pady = 30,padx = 10,ipady=8)
        
        #area 
        area = tk.Label(self.container,text = "How much house area do you want ?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 5,pady = 30)

        #area m2
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER
                            )
        aream.grid(column = 1, row = 5,pady = 30,ipady=8)

        #many room 
        area = tk.Label(self.container,text = "How many rooms do you want to house?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 6,pady = 30)

        #many room
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 6,pady = 30,ipady=8)

        #many toilet 
        area = tk.Label(self.container,text = "How many rooms do you want to toilet?",
                            width = 40,
                            height = 2,
                            )
        area.grid(column = 0, row = 7,pady = 30)

        #many toilet
        aream = tk.Entry(self.container,
                            width = 15,
                            justify=CENTER,
                            )
        aream.grid(column = 1, row = 7,pady = 30,ipady=8)
