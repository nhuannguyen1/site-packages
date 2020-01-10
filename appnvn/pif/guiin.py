from tkinter import *
import tkinter as tk
bd = 1
def genbutton(frame,controller):
        #Export to excel 
        Buttom_ExportToExcel  = tk.Button (frame,
                                           text = "ExportToExcel",
                                           width = 5
                                           )
        Buttom_ExportToExcel.grid(row = 6,
                                column = 2,
                                columnspan = 2,
                                sticky="we"
                                )
        # quit 
        buttom_quit = tk.Button (frame,
                                text = "Exit",
                                width = 11,
                                command = frame.quit
                                )
        buttom_quit.grid(row = 7, 
                        column = 2,
                        columnspan = 2,
                        sticky="we"
                        )

def plceprenext(frame,controller,ar1,ar2):
        # prevous
        buttom_Pre = tk.Button (frame,
                                text = "Pre",
                                width = 5,
                                command=lambda: controller.show_frame(ar1)
                                )
        buttom_Pre.grid(row = 99, column = 2,sticky="e")
        #buttom_Pre.place(relx = 0.3, rely = 0.80) 
        """
        buttom_Pre = tk.Label (frame,
                                text = "",
                                width = 5,
                                )
        buttom_Pre.grid(row = 5, column = 6,sticky="e")
        """

        # next
        buttom_next = tk.Button (frame,
                                text = "Next",
                                width = 5,
                                command=lambda: controller.show_frame(ar2)
                                )
        buttom_next.grid(row = 99, column = 3, sticky="w")
        #buttom_next.place(relx = 0.7, rely = 0.80) 
        #Export to excel 
        Buttom_ExportToExcel  = tk.Button (frame,
                                           text = "ExportToExcel",
                                           width = 5
                                           )
        Buttom_ExportToExcel.grid(row = 100,
                                column = 2,
                                columnspan = 2,
                                sticky="we"
                                )
        # quit 
        buttom_quit = tk.Button (frame,
                                text = "Exit",
                                width = 11,
                                command = frame.quit
                                )
        buttom_quit.grid(row = 101, 
                        column = 2,
                        columnspan = 2,
                        sticky="we"
                        )

class pjfinfo (tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.width = 15
        #label in infomation tab 
        self.lbinf = Label(self,
                            text = "GENNERAL",
                            width = self.width, 
                            bg = "yellow",
                            fg="black"
                            )
        self.lbinf.config(font=("Times New Roman", 15))
        self.lbinf.grid(row = 0, columnspan = 6,sticky = "ew")

        #self.geometry ("650x300")
        self.proname = Label(self,
                            text = "Project Name",
                            width = self.width, 
                            bg = "sky blue",
                            fg="black"
                            )
        self.proname.grid(row = 1, column = 0)

        self.entryproname = Entry(self,
                                    bd = bd,
                                    width = 20,
                                    justify = CENTER)
        self.entryproname.grid(row = 1, column = 1)

        #Quote Code
        self.quacodenname = Label(self,
                                    text = "Quote Name",
                                    width = self.width,
                                    bg = "sky blue",
                                    fg="black")
        self.quacodenname.grid(row = 1, column = 2)
        self.quacode = Entry(self,
                            bd = bd,
                            width = 20,
                            justify = CENTER)
        self.quacode.grid(row = 1, column = 3)
        #write sale man 
        self.salemanname = Label(self,
                                text = "Sale Man", 
                                bg = "sky blue",
                                width = self.width,
                                fg="black")
        self.salemanname.grid(row = 1, column = 4)
        self.saleman = Entry(self,
                            bd = bd,
                            width = 20,
                            justify = CENTER)
        self.saleman.grid(row = 1, column = 5)
        
        # line 2
        #contract no
        
        self.ContractNolb = Label(self, 
                                  text = "Contract No.",
                                  width = self.width, 
                                  bg = "sky blue",
                                  fg="black")
        self.ContractNolb.grid(row = 2, column = 0)
        self.ContractNo = Entry(self,
                                bd = bd,
                                width = 20,
                                justify = CENTER)
        self.ContractNo.grid(row = 2, column = 1)
        #Quote Rev No. 
        self.quoterevnoname = Label(self, 
                                    text = "Quote Rev No.",
                                    width = self.width, 
                                    bg = "sky blue",
                                    fg="black")
        self.quoterevnoname.grid(row = 2, column = 2)
        self.quoterevno = Entry(self,
                                bd = bd,
                                width = 20,
                                justify = CENTER
                                )
        self.quoterevno.grid(row = 2, column = 3)
        #Sales office
        self.salesofficename = Label(self, 
                                    text = "Sales Office.",
                                    width = self.width, 
                                    bg = "sky blue",
                                    fg="black")
        self.salesofficename.grid(row = 2, column = 4)
        self.salesoffice = Entry(self,
                                bd = bd,
                                width = 20,
                                justify = CENTER)
        self.salesoffice.grid(row = 2, column = 5)
        # line 3
        #SAP No.
        self.sapnolb = Label(self,
                             text = "SAP No.",
                             width = self.width, 
                             bg = "sky blue",
                             fg="black",
                             justify = CENTER)
        self.sapnolb.grid(row = 3, column = 0)
        self.sapno = Entry(self,
                            bd = bd,
                            width = 20,
                            justify = CENTER)
        self.sapno.grid(row = 3, column = 1)
        #Quote Rev Date. 
        self.quoterevdatelb = Label(self, 
                                text = "Quote Rev Date",
                                width = self.width, 
                                bg = "sky blue",
                                fg="black"
                                )
        self.quoterevdatelb.grid(row = 3, column = 2)
        self.quoterevdate = Entry(self,
                                    bd = bd,
                                    width = 20,
                                    justify = CENTER
                                    )
        self.quoterevdate.grid(row = 3, column = 3)
        #Sales team
        self.salesteamlb = Label(self, 
                                text = "Sales team",
                                width = self.width, 
                                bg = "sky blue",
                                fg="black"
                                )
        self.salesteamlb.grid(row = 3, column = 4)
        self.salesteam = Entry(self,
                                bd = bd,
                                width = 20,
                                justify = CENTER
                                )
        self.salesteam.grid(row = 3, column = 5)
        # line 4
        #PIF number.
        self.PIFnumberlb = Label(self, 
                                text = "PIF number",
                                width = self.width, 
                                bg = "sky blue",
                                fg="black",
                              )
        self.PIFnumberlb.grid(row = 4,column = 0)
        self.PIFnumbername = Entry(self,
                                    bd = bd,
                                    width = 12,
                                    justify = CENTER)
        self.PIFnumbername.grid(row = 4,
                                column = 1, 
                                columnspan = 1,
                                sticky = "w"
                                )
        #Rev. 
        self.revlb = Label(self, 
                            text = "Rev",
                            width = 2, 
                            bg = "sky blue",
                            fg="black"
                            )
        self.revlb.grid(row = 4, 
                        column = 1,
                        sticky = "e",
                        ipadx = 15
                        )
        self.rev = Entry(self,
                            bd = bd,
                            width = 7,justify = CENTER)
        self.rev.grid(row = 4, column = 2,sticky = "w")
        #Support Sale name
        self.supportsalenamelb = Label(self, 
                                        text = "SSD name",
                                        width = 9, 
                                        bg = "sky blue",
                                        fg="black")
        self.supportsalenamelb.grid(row = 4, 
                                    column = 2,
                                    sticky = "e",
                                    ipadx = 1)
        self.supportsalename = Entry(self,
                                    bd = bd,justify = CENTER
                                    )
        self.supportsalename.grid(row = 4, 
                                    column = 3
                                    )
        #Project Enginneer
        self.projectenginneerlb = Label(self, 
                                        text = "Project Enginneer",
                                        width = self.width, 
                                        bg = "sky blue",
                                        fg="black"
                                        )
        self.projectenginneerlb.grid(row = 4, column = 4)

        self.projectenginneer = Entry(self,
                                        bd = bd,
                                        width = 20,
                                        justify = CENTER
                                        )
        self.projectenginneer.grid(row = 4, 
                                    column =5
                                    )

        plceprenext(self,self.controller,geninfor,revhis)

class revhis (tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.width = 15
        self.controller = controller
        self.num_rows = 1
        self.new_row()
        self.createRow_button = tk.Button(self, text='Add New', command=self.new_row)
        self.createRow_button.grid(row = 17, column = 0)

    def new_row(self):
        self.num_rows += 1
        self.lbinf = Label(self,
                            text = "I.REVISION HISTORY 1",
                            width = self.width, 
                            bg = "yellow",
                            fg="black"
                            )
        self.lbinf.config(font=("Times New Roman", 15))
        self.lbinf.grid(row = 0, 
                        columnspan = 10,
                        sticky = "ew")

        self.no = Label(self,
                            text = "NO.",
                            width = 3, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1, column = 0)
        self.noin = Entry(self,
                            bd = bd,
                            width = 4,
                            justify = CENTER).grid(row = self.num_rows, column = 0)

        self.revision = Label(self,
                            text = "REVISION",
                            width = 10, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,column = 1)
        self.revisionin = Entry(self,
                            bd = bd,
                            width = 5,
                            justify = CENTER
                            ).grid(row = self.num_rows, column = 1)

        self.datarev = Label(self,
                            text = "Date Rev.",
                            width = 9, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,column = 2)

        self.datarevin = Entry(self,
                            bd = bd,
                            width = 9,
                            justify = CENTER).grid(row = self.num_rows, column = 2) 
        
        self.datarev = Label(self,
                            text = "Date Rev.",
                            width = 9, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1, column = 3)
        self.datarevin = Entry(self,
                            bd = bd,
                            width = 4,
                            justify = CENTER).grid(row = self.num_rows, column = 3)  
        
        self.Section = Label(self,
                            text = "Section",
                            width = self.width, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,column = 4)
        self.Sectionin = Entry(self,
                            bd = bd,
                            width = self.width,
                            justify = CENTER
                            ).grid(row = self.num_rows, column = 4) 

        self.Page = Label(self,
                            text = "Page",
                            width = 6, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,column = 5)
        self.Pagein = Entry(self,
                            bd = bd,
                            width = 6,
                            justify = CENTER
                            ).grid(row = self.num_rows, column = 5) 

        self.changedcontents = Label(self,
                            text = "Changed Contents",
                            width = 34, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,column = 6)

        self.changedcontentsin = Entry(self,
                            bd = bd,
                            width = 34,
                            justify = CENTER).grid(row = self.num_rows, column = 6) 

        self.Namedept = Label(self,
                            text = "Name/ Dept.",
                            width = 10, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,
                                column = 7)
        self.changedcontentsin = Entry(self,
                            bd = bd,
                            width = 10,
                            justify = CENTER).grid(row = self.num_rows, column = 7)

        plceprenext(self,self.controller,pjfinfo,geninfor)

class geninfor (tk.Frame):
     def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.width = 15
        self.controller = controller
        #label in infomation tab 
        self.lbinf = Label(self,
                            text = "II. GENERAL INFORMATIONS",
                            width = self.width, 
                            bg = "yellow",
                            fg="black"
                            )
        self.lbinf.config(font=("Times New Roman", 15))
        self.lbinf.grid(row = 0, columnspan = 10,sticky = "ew")
        #Line 1
        self.sttsl = Label(self,
                            text = "1 Site location",
                            width = 15, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 1, column = 0)
        self.sttslin = Entry(self,
                            bd = bd,
                            width = 39,
                            justify = CENTER).grid(row = 1, column = 2,sticky="we")
        
        self.sttps = Label(self,
                            text = "10 Project scope",
                            width = 30, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 1, column = 3,columnspan = 2,sticky="we")
        self.rd = Label(self,
                            text = "15 Require document",
                            width = 20, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 1, column = 5,columnspan = 2,sticky="ew")
        var1 = IntVar()
        var2 = IntVar()
        
        #Line 2
        self.sttsl = Label(self,
                            text = "2 Country",
                            width = 15, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 2, column = 0,sticky="we")

        self.sttslin = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 2, column = 2,sticky="we")

        self.sttps1cb = Checkbutton(self, text="Design", variable=var1).grid(row=2, column = 3,padx = 3,sticky="w")

        self.degn = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 2, column = 4)

        self.sttdegn = Checkbutton(self, text="Quotation", variable=var2).grid(row=2, column = 5,padx = 3,sticky="w")
        self.quain = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 2, column = 6,sticky="we")
        #line 3
        self.sttsl = Label(self,
                            text = "3 Project sector",
                            width = 15, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 3, column = 0,sticky="we")

        self.sttslin = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 3, column = 2,sticky="we")

        self.sttps1cb = Checkbutton(self, text="Fabrication", variable=var1).grid(row=3, column = 3,padx = 3)

        self.degn = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 3, column = 4)

        self.sttdegn = Label(self, text="Quote. form").grid(row=3, column = 5,padx = 6)
        self.quain = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 3, column = 6,sticky="we")

        #plceprenext(self,self.controller,revhis,pjfinfo)
        #line 4
        self.sttsl = Label(self,
                            text = "4 Customer type",
                            width = 15, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 4, column = 0,sticky="we")

        self.sttslin = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 4, column = 2,sticky="we")

        self.sttps1cb = Checkbutton(self, text="Fabrication", variable=var1).grid(row=4, column = 3,padx = 3)

        self.degn = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 4, column = 4)

        self.sttdegn = Checkbutton(self, text="Column reaction", variable=var2).grid(row=4, column = 5,padx = 3,sticky="w")
        self.quain = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 4, column = 6,sticky="we")
        #line 5
        self.sttsl = Label(self,
                            text = "5 Confidence factor",
                            width = 15, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 5, column = 0,sticky="we")

        self.sttslin = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 5, column = 2,sticky="we")

        self.sttps1cb = Checkbutton(self, text="Fabrication", variable=var1).grid(row=5, column = 3,padx = 3)

        self.degn = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 5, column = 4)

        self.sttdegn = Checkbutton(self, text="Column reaction", variable=var2).grid(row=5, column = 5,padx = 3,sticky="w")
        self.quain = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 5, column = 6,sticky="we")
        #line 6
        self.sttsl = Label(self,
                            text = "6 Confidence factor",
                            width = 15, 
                            bg = "sky blue",
                            fg="black",
                            anchor='w'
                            ).grid(row = 6, column = 0,sticky="we")

        self.sttslin = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 6, column = 2,sticky="we")

        self.sttps1cb = Checkbutton(self, text="Fabrication", variable=var1).grid(row=5, column = 3,padx = 3)

        self.degn = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 6, column = 4)

        self.sttdegn = Checkbutton(self, text="Column reaction", variable=var2).grid(row=6, column = 5,padx = 3,sticky="w")
        self.quain = Entry(self,
                            bd = bd,
                            width = 30,
                            justify = CENTER).grid(row = 6, column = 6,columnspan = 2,sticky="we")
        plceprenext(self,self.controller,revhis,pjfinfo)
class delivery (tk.Frame):
     def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        self.width = 15
        self.controller = controller
        #label in infomation tab 
        self.lbinf = Label(self,
                            text = "III.DELIVERY",
                            width = self.width, 
                            bg = "yellow",
                            fg="black"
                            )
        self.lbinf.config(font=("Times New Roman", 10))
        self.lbinf.grid(row = 0, columnspan = 10,sticky = "ew")

        self.no = Label(self,
                            text = "NO.",
                            width = 4, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1, column = 0)
        self.noin = Entry(self,
                            bd = 5,
                            width = 4,
                            justify = CENTER).grid(row = 2, column = 0)

        self.revision = Label(self,
                            text = "REVISION",
                            width = 10, 
                            bg = "sky blue",
                            fg="black"
                            ).grid(row = 1,column = 1)
        self.revisionin = Entry(self,
                            bd = 5,
                            width = 5,
                            justify = CENTER).grid(row = 2, column = 1)
        plceprenext(self,self.controller,pjfinfo,geninfor)
class erection (tk.Frame):
        def __init__(self,parent, controller):
            tk.Frame.__init__(self,parent)
            self.width = 15
            self.controller = controller
            #label in infomation tab 
            self.lbinf = Label(self,
                                text = "IV. ERECTION",
                                width = self.width, 
                                bg = "yellow",
                                fg="black"
                                )
            self.lbinf.config(font=("Times New Roman", 15))
            self.lbinf.grid(row = 0, columnspan = 10,sticky = "ew")

            self.no = Label(self,
                                text = "NO.",
                                width = 4, 
                                bg = "sky blue",
                                fg="black"
                                ).grid(row = 1, column = 0)
            self.noin = Entry(self,
                                bd = 5,
                                width = 4,
                                justify = CENTER).grid(row = 2, column = 0)

            self.revision = Label(self,
                                text = "REVISION",
                                width = 10, 
                                bg = "sky blue",
                                fg="black"
                                ).grid(row = 1,column = 1)
            self.revisionin = Entry(self,
                                bd = 5,
                                width = 5,
                                justify = CENTER).grid(row = 2, column = 1)
            plceprenext(self,self.controller,pjfinfo,geninfor)