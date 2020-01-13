import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from pynvn.path.ppath import (getpathfromtk,
                                PathSteel,
                                ExtractFileNameFromPath,
                                PathFromFileNameAndDirpath,
                                abspath,
                                getdirpath,
                                ExtractFileNameFromPath,
                                getfilenamewoexten,
                                credirfol)
from tkinter import messagebox
from datetime import datetime
from appnvn.balstock.dataexc import comparetwofile
import pandas as pd
def donothing(root):
    filewin = Toplevel(root)
    filewin.title (
                    "ATAD STEEL STRUCTURE CORPORATION"
                    )

    button = Button(filewin, text="Do nothing button")

    button.pack()

pathinoutgl = ""
pathinout = None
filename1 = ""

def createmenu (root):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", 
                            command=donothing)
        filemenu.add_command(label="Open", 
                            command=donothing)
        filemenu.add_command(label="Save", 
                            command=donothing)
        filemenu.add_command(label="Backup", 
                            command=lambda: donothing(root))
        filemenu.add_command(label="Close", 
                            command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", 
                            command=root.quit)
        menubar.add_cascade(label="Option", 
                            menu=filemenu)

        root.config(menu=menubar)
def getdirpathfromorigin(output1):
        # Get path full 
        global pathinout
        pathinout = getpathfromtk(output1)
        filename =ExtractFileNameFromPath(pathinout)
        filename1 = getfilenamewoexten(filename)
        # get dirpath from full path
        dn = getdirpath(pathinout)

        ps = PathSteel(dir_path =dn,FileName = filename1 + ".csv")
        pathf = ps.refpath()
        return  pathf

def donothing(root):
        filewin = Toplevel(root)

        columns = ("#1","#2")

        tree = ttk.Treeview(filewin,
                                show = "headings",
                                columns = columns)

        tree.heading("#1", text="Name User")
        tree.heading("#2", text="Time")

        ysb = ttk.Scrollbar(filewin, orient=tk.VERTICAL,
        command=tree.yview)

        tree.configure(yscroll=ysb.set)

        pathf = getdirpathfromorigin(output1)
     
        dtpd = pd.read_csv(pathf,usecols=[0, 1], header=None)

        sh = dtpd.shape
        
        for ix in range(sh[0]):
            k = dtpd.iloc[ix] 
            k1 = k.values.tolist()
            tree.insert("", tk.END, 
                            values=k1)

        tree.grid(row=0, 
                    column=0)

        ysb.grid(row=0, 
                column=1, 
                sticky=tk.N + tk.S)

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        button = Button(filewin, text="DownLoad")
        button.grid(row = 1,
                    column = 0,
                    sticky = "we"
                    )

        tree.column("#1",anchor=tk.CENTER)
        tree.column("#2",anchor=tk.CENTER)
        tree.bind("<<TreeviewSelect>>", print_selection(tree,event))
        #button.pack()

def print_selection(tree):
    for selection in tree.selection():
        item = tree.item(selection)
        last_name, first_name = item["values"][0:2]
        text = "Selection: {}, {}"
        print(text.format(last_name, first_name))

def setcfbs (root):
        root.iconbitmap('clienticon.ico')
        root.title (
                    "ATAD STEEL STRUCTURE CORPORATION"
                    )
        root.configure(background='khaki1')

class bl (tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        setcfbs(self)
        self.container = tk.Frame(self)
        #container.config(anchor=CENTER)
        self.container.pack(side="top",
                        fill=Y, expand=YES)  

        createmenu(self)

        frame = nameuser(self.container, self)
        #self.frames[F] = frame
        frame.grid(row=0, 
                    column=0, 
                    sticky="nsew")
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    def donothing(self):
        filewin = Toplevel(self)

        columns = ("#1","#2")

        tree = ttk.Treeview(filewin,
                                show = "headings",
                                columns = columns)

        tree.heading("#1", text="Name User")
        tree.heading("#2", text="Time")

        ysb = ttk.Scrollbar(filewin, orient=tk.VERTICAL,
        command=tree.yview)

        tree.configure(yscroll=ysb.set)

        pathf = getdirpathfromorigin(output1)
     
        dtpd = pd.read_csv(pathf,usecols=[0, 1], header=None)

        sh = dtpd.shape
        
        for ix in range(sh[0]):
            k = dtpd.iloc[ix] 
            k1 = k.values.tolist()
            tree.insert("", tk.END, 
                            values=k1)

        tree.grid(row=0, 
                    column=0)

        ysb.grid(row=0, 
                column=1, 
                sticky=tk.N + tk.S)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        button = Button(filewin, text="DownLoad")
        button.grid(row = 1,
                    column = 0,
                    sticky = "we"
                    )

        tree.column("#1",anchor=tk.CENTER)
        tree.column("#2",anchor=tk.CENTER)
        tree.bind("<<TreeviewSelect>>", print_selection(tree,event))
        #button.pack()



class nameuser(tk.Frame):
    def __init__(self,parent, 
                controller):
        self.parent = parent
        self.controller = controller
        tk.Frame.__init__(self,
                        parent)

        self.inyname = Label(self,
                            text = "INPUT YOUR NAME",
                            width = 17, 
                            bg = "SteelBlue2",
                            fg="black"
                            )

        self.inynamein = Entry(self,
                                    width = 20,
                                    justify = CENTER)

        self.button = tk.Button(self, text="Next",
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
            global dt_string_sr
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
            dt_string_sr = now.strftime("%H%M%S%d%m%Y")
            self.controller.withdraw()
            filewin = Toplevel(self)
            #filewin.geometry("350x350")
            app = primaryc(filewin)

class primaryc:
    def __init__(self,master):
        self.master = master
        self.container = tk.Frame(self.master)
        self.container.pack()
        createmenu (self.master)
        large_font = ('Verdana',10)

        setcfbs(self.master)
        #create buttom for open file 
        button = tk.Button(self.container,text = "Directory file 1",
                            width = 10,
                            height = 2,
                            command = self.mfileopen
                            )
        button.grid(row = 0,
                    column = 0,
                    sticky = "we"
                    )

        self.master.protocol('WM_DELETE_WINDOW', self.doSomething)
        # create output text, it is used to save directory 
        self.output1 = tk.Text (self.container, 
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
        self.openfile = tk.Button(self.container,text = "OPEN FILE 1",
                            width = 10,
                            height = 2,
                            command = lambda: self.openfile1(self.output1)
                            )

        self.openfile.grid(row = 0,
                    column = 2,
                    sticky = "we"
                    )
        # syn on server 
        self.syn = tk.Button(self.container,text = "SYN",
                            width = 5,
                            height = 2,
                            command = lambda: self.synserverfileexc(self.pathinout)
                            )
        self.syn.grid(row = 0,
                    column = 3,
                    sticky = "we"
                    )    

        # start line 2
        button = tk.Button(self.container,text = "Directory file 2",
                            width = 10,
                            height = 2,
                            command = self.mfileopenout
                            )
        button.grid(row = 1,
                    column = 0,
                    sticky = "we"
                    )

        self.output2 = tk.Text (self.container, 
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
        self.syn = tk.Button(self.container,text = "SYN",
                            width = 5,
                            height = 2,
                            command = lambda: self.synserverfileexc(self.pathinout)
                            )
        self.syn.grid(row = 1,
                    column = 3,
                    sticky = "we"
                    )    

        # open file 2
        button = tk.Button(self.container,text = "OPEN FILE 2",
                            width = 10,
                            height = 2,
                            command = lambda: self.openfile1(self.output2)
                            )
            
        button.grid(row = 1,
                    column = 2,
                    sticky = "we"
                    )    

        #quit widget  
        buttom_quit = tk.Button (self.container,
                                text = "Exit",
                                width = 20,
                                command = self.container.quit)

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
        pathfulloutput = getpathfromtk(output1)

        filename =ExtractFileNameFromPath(pathfulloutput)
        filename1 = getfilenamewoexten(filename)

        dbk = credirfol(getdirpath(pathfulloutput),filename1)

        ps = PathSteel(dir_path =dbk,FileName = dt_string_sr + "_" + inynameing + "_" + filename)
        dbk1 = ps.refpath()

        #get path to orginal location with file name diff
        filenamewopath = getfilenamewoexten(filenametemp) + "_diff.xlsx"

        pathdiff = PathFromFileNameAndDirpath(dir_path = getdirpath(pathfulloutput),
                                            filename = filenamewopath)

        comparetwofile1 = comparetwofile(path_OLD = pathtemp,
                                        path_NEW = fullname,
                                        index_col = None,
                                        usernamein = inynameing,
                                        pathtcsvtosavedata = getdirpathfromorigin(output1),
                                        difpathtobk = dbk1,
                                        pathtorgindiff = pathdiff,
                                        dt = dt_string)           
        comparetwofile1.excel_diff()
    
    def doSomething(self):
        if messagebox.askyesno("Exit",
                                "Do you want to quit the application?"):
            self.master.quit()