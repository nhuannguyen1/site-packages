from os.path import dirname
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pynvn.path.ppath import getpathfromtk,PathSteel,ExtractFileNameFromPath,PathFromFileNameAndDirpath,retabspath,abspath,getdirpath
from datetime import datetime
from pynvn.csv.tocsv import wrcsv
from appnvn.balstock.dataexc import comparetwofile
from pynvn.csv.rcsv import rcsv
import pandas as pd
def donothing(root):
    filewin = Toplevel(root)
    filewin.title (
                    "ATAD STEEL STRUCTURE CORPORATION"
                    )

    button = Button(filewin, text="Do nothing button")

    button.pack()


pathinoutgl = ""
class bl (tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.setcfbs(self)
        self.container = tk.Frame(self)
        #container.config(anchor=CENTER)
        self.container.pack(side="top",
                        fill=Y, expand=YES)  

        self.frames = {}

        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Backup", command=lambda: self.donothing())
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Option", menu=filemenu)

        self.config(menu=menubar)

        for F in (nameuser, primaryc):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(nameuser)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def donothing(self):
        filewin = Toplevel(self)

        self.setcfbs(filewin)

        columns = ("#1","#2")

        self.tree = ttk.Treeview(filewin,show = "headings",columns = columns)
        self.tree.heading("#1", text="Name User")
        self.tree.heading("#2", text="Time")
        ysb = ttk.Scrollbar(filewin, orient=tk.VERTICAL,
        command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        # get path full from other class 
        pathinout = getpathfromtk(output1)
        # get dirpath from full path
        dn = getdirpath(pathinout)

        ps = PathSteel(dir_path =dn,FileName ="npandas.csv")
        pathf = ps.refpath()

        dtpd = pd.read_csv(pathf,usecols=[0, 1], header=None)

        sh = dtpd.shape
        
        for ix in range(sh[0]):
            k = dtpd.iloc[ix] 
            k1 = k.values.tolist()
            self.tree.insert("", tk.END, values=k1)

        self.tree.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        button = Button(filewin, text="DownLoad")
        button.grid(row = 1,
                    column = 0,
                    sticky = "we"
                    )
        self.tree.column("#1",anchor=tk.CENTER)
        self.tree.column("#2",anchor=tk.CENTER)
        #button.pack()
    def setcfbs (self, root):
        root.iconbitmap('clienticon.ico')
        root.title (
                    "ATAD STEEL STRUCTURE CORPORATION"
                    )
        root.configure(background='khaki1')
class nameuser(tk.Frame):
    def __init__(self,parent, controller):
        self.controller = controller
        tk.Frame.__init__(self,parent)
        self.inyname = Label(self,
                            text = "INPUT YOUR NAME",
                            width = 17, 
                            bg = "SteelBlue2",
                            fg="black"
                            )
        self.inynamein = Entry(self,
                                    width = 20,
                                    justify = CENTER)

        self.button = tk.Button(self, text="OK AND NEXT",
                            command=lambda: self.checkinputyourname())
        self.inyname.pack()
        self.inynamein.pack()
        self.button.pack()
    def checkinputyourname(self):
        global inynameing
        inynameing = self.inynamein.get()
        if inynameing is "":
            print ("Check your name input:")
        else:
            global dt_string
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
            self.controller.show_frame(primaryc)

class primaryc(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        large_font = ('Verdana',10)
        #create buttom for open file 
        button = tk.Button(self,text = "Directory file 1",
                            width = 10,
                            height = 2,
                            command = self.mfileopen
                            )
    
        button.grid(row = 0,
                    column = 0,
                    sticky = "we"
                    )

        # create output text, it is used to save directory 
        self.output1 = tk.Text (self, 
                                width = 60,
                                height = 2,
                                font = large_font,
                                selectborderwidth = 10,
                                bg = "yellow"
                              )

        self.output1.grid(row = 0,
                        column = 1,
                        )
        global output1 
        output1 = self.output1
        
        # open file 1 
        self.openfile = tk.Button(self,text = "OPEN FILE 1",
                            width = 10,
                            height = 2,
                            command = lambda: self.openfile1(self.output1)
                            )

        self.openfile.grid(row = 0,
                    column = 2,
                    sticky = "we"
                    )
        # syn on server 
        self.syn = tk.Button(self,text = "SYN",
                            width = 5,
                            height = 2,
                            command = lambda: self.synserverfileexc(self.pathinout)
                            )
        self.syn.grid(row = 0,
                    column = 3,
                    sticky = "we"
                    )    

        # start line 2
        button = tk.Button(self,text = "Directory file 2",
                            width = 10,
                            height = 2,
                            command = self.mfileopenout
                            )
        button.grid(row = 1,
                    column = 0,
                    sticky = "we"
                    )

        self.output2 = tk.Text (self, 
                                    width = 60,
                                    height = 2,
                                    font = large_font,
                                    selectborderwidth = 10,
                                    bg = "yellow"
                                   )
        self.output2.grid(row = 1,
                            column = 1,
                            )
        # syn on server 
        self.syn = tk.Button(self,text = "SYN",
                            width = 5,
                            height = 2,
                            command = lambda: self.synserverfileexc(self.pathinout)
                            )
        self.syn.grid(row = 1,
                    column = 3,
                    sticky = "we"
                    )    

        # open file 2
        button = tk.Button(self,text = "OPEN FILE 2",
                            width = 10,
                            height = 2,
                            command = lambda: self.openfile1(self.output2)
                            )
            
        button.grid(row = 1,
                    column = 2,
                    sticky = "we"
                    )    

        #quit widget  
        buttom_quit = tk.Button (self,
                                text = "Exit",
                                width = 20,
                                command = self.quit)

        buttom_quit.grid(row = 3,
                        column = 1,
                        )

    # open file follow directory 
    def mfileopen(self):
            files = filedialog.askopenfilename()
            self.output1.insert(tk.END,
                                files)
            
    # open file out put 
    def mfileopenout(self):
            files = filedialog.askopenfilename()
            self.output2.insert(tk.END,
                                    files)
    # Open file 1
    def openfile1 (self,output):
        # get path full
        self.pathinout = getpathfromtk(output)
        # save as file path from path original 
        pathst = PathSteel (pathorigrn = self.pathinout)
        pathst.saveasfiletopathAndopen()
    def synserverfileexc (self,pathtemp,indexcol = None):
        filenametemp = ExtractFileNameFromPath(path = pathtemp)

        dirname = abspath("")
        fullname = PathFromFileNameAndDirpath(dir_path = dirname,
                                            filename = filenametemp  )

        comparetwofile1 = comparetwofile(path_OLD = pathtemp,
                                        path_NEW = fullname,
                                        index_col = None,
                                        usernamein = inynameing,
                                         dt = dt_string)           
        comparetwofile1.excel_diff()
