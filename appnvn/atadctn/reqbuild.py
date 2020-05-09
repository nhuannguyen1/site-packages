from tkinter import (Frame,
                    Tk,
                    Toplevel,
                    StringVar,
                    IntVar,
                    Radiobutton
                    )
import tkinter as tk
from tkinter import ttk
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
from appnvn.atadctn.treectn import scbg,createcroll,cvframe
from pynvn.caculate.cacul_cavas import (placereccenter,
                                        setbackdimention)

import re

from pynvn.caculate.ratio import ratio

class reqbuild(Frame):
        """ customer information"""
        def __init__(self,tktk = None,
                        br_image = None,
                        pathico = None,
                        br_image_path = None,
                        logoicon = None,
                        bglb = "white",
                        labelfont = ('times', 20),
                        labelfont_sm = ('times', 16),
                        padx = (10,0),
                        imagenext = None,
                        ):
                self.tktk = tktk
                self.tktk.withdraw()
                Frame.__init__(self, tktk)
                
                self.labelfont = labelfont
                self.labelfont_sm = labelfont_sm
                self.br_image_path  = br_image_path
                self.br_image = br_image
                self.logoicon = logoicon
                self.padx = padx
                self.pathico = pathico
                self.filewin = Toplevel(self.tktk)
                self.bglb = bglb
                self.imagenext = imagenext
                gui (tktk=self.filewin,
                        pathico=self.pathico,
                        width=950,
                        height=950,
                        widthx="center",
                        widthy="center",
                        condv=2.2,
                        resizable=[True,True]).setcfbs()
                
                # set menu 
                menu (tktk=self.filewin).createmenu()

                #gui for data 
                self.cavheight_width = [1200,720]
                self.frameb =  [450,0,750,720,"white"]
                self.sc = scbg(parent = self.filewin,
                                cavheight=self.cavheight_width[1],
                                cavwidth=self.cavheight_width[0],
                                bg = "white", 
                                bgpr = "#5181a7",
                                isonlyaframe= False,
                                framea =[0,0,450,720,"yellow"], 
                                frameb = self.frameb 
                                )
        
                # create frame a
                self.listFramevp = self.sc.framea
                # create cavas framea 
                self.canv =  self.sc.canvas
                # create fameb
                self.listFramedr = self.sc.frameb
                # create cavas frameb 
                self.canvasb = tk.Canvas(self.listFramedr)
                # create gui for input from customer 
                self.creategui()
                #self.createdrawing()
                self.pattern = re.compile("^\w{0,10}$")

        def creategui(self):
                """create gui for customer information"""
                row = 0
                col = 0 
                # create title for window
                row = row + 1
                cis = tk.Label(self.listFramevp,
                                text = "Ask The House You Want To Build",
                                anchor="e",
                                font = self.labelfont,
                                bg = self.bglb
                                )
                cis.grid(column = 0, 
                                row  = row,
                                padx = self.padx,
                                columnspan = 4
                                )

                #set Address
                row = row + 1
                add = tk.Label(self.listFramevp,
                                text = "*Building Add:"
                                )
                add.grid(column = 0, 
                        row  = row ,
                        sticky  = "e",
                        padx = self.padx,
                        )

                """ using Combobox"""
                # set Province or city
                self.pc = tk.StringVar() 
                combopc =  ttk.Combobox(self.listFramevp, 
                                        textvariable = self.pc
                                        )
                combopc['values'] = ('Province/City',  
                                        'Dak Lak', 
                                        'Ho Chi Minh', 
                                        'Ha Noi', 
                                        'Dong Nai', 
                                        'Long An'
                                        )

                combopc.current(0)
                combopc.grid(column = 1,
                         row = row,
                         columnspan = 4,
                         sticky  = tk.EW) 

                # set District or Town
                self.dt = tk.StringVar() 
                combodt =  ttk.Combobox(self.listFramevp, 
                                        textvariable = self.dt
                                        )
                combodt['values'] = ('District/Town',  
                                        'Krong Buk', 
                                        'Buon Ho', 
                                        'Ehleo', 
                                        '1 District', 
                                        '2 District', 
                                        '3 District', 
                                        '4 District'
                                        ) 
                combodt.current(0)
                row = row + 1
                combodt.grid(column = 1, 
                                row = row, 
                                pady = 10,
                                columnspan = 4,
                                sticky  = tk.EW
                                ) 

                # set Ward/Village
                self.wv = tk.StringVar() 
                combowv =  ttk.Combobox(self.listFramevp, 
                                        textvariable = self.wv,
                                        style = 'custom.TCombobox'
                                        )
                combowv['values'] = ('Ward/Village',  
                                        'Cu pong', 
                                        'Chu Kpo'
                                     ) 
                combowv.current(0)
                row +=1
                combowv.grid(column = 1, 
                                row = row,
                                columnspan = 4,
                                sticky  = tk.EW
                                ) 

                v = StringVar(self.listFramevp, 
                                value='Address Street'
                                )
                self.adde = tk.Entry(self.listFramevp,
                                justify="left",
                                text = v
                                )
                self.adde.bind("<Button-1>", 
                                self.some_callback
                                )
                row +=1
                self.adde.grid(column = 1, 
                        row  = row,
                        sticky  = tk.EW,
                        pady = 10,
                        columnspan = 4
                        )

                #  area
                row = row + 1

                arealb = tk.Label(self.listFramevp,
                        text = "*Building Area:",
                        )
                arealb.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "e")
                vcmd = (self.register(self.validate_username), "%i", "%P")

                # Width entry 
                self.entryw = tk.Entry(self.listFramevp,
                                        width = 10,
                                        validate="focusout",
                                        validatecommand=vcmd,
                                        invalidcommand=self.print_error)

                self.entryw.insert(tk.END, 400)
                self.entryw.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                #Width label
                wlb = tk.Label(self.listFramevp,
                        text = "Width:",
                        )
                wlb.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
               # height entry 
                self.entryh = tk.Entry(self.listFramevp,
                                        width = 10,
                                        validate="focusout",
                                        validatecommand=vcmd,
                                        invalidcommand=self.print_error)
                self.entryh.insert(tk.END, 400)
                self.entryh.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                #height label
                lbh = tk.Label(self.listFramevp,
                        text = "Height:",
                        )
                lbh.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                
                # Setback space
                row = row + 1
                sbs = tk.Label(self.listFramevp,
                                text = "Sb Space:",
                                )
                sbs.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                # Front 
                self.etf = tk.Entry(self.listFramevp,
                                justify="left",
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error
                                )
                self.etf.grid(column = 2, 
                        row  = row,
                        sticky  = "w",
                        )
                # set defaut value for entry 
                self.etf.insert(tk.END, 100)
                
                lbb = tk.Label(self.listFramevp,
                        text = "Front",
                        )
                lbb.grid(column = 3, 
                        row = row,
                        sticky  = "w")
                        
                # Back
                row += 1
                self.etb = tk.Entry(self.listFramevp,
                                justify="left",
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error
                                )
                self.etb.grid(column = 2, 
                        row  = row,
                        sticky  = "w",
                        )
                # set defaut value for entry 
                self.etb.insert(tk.END, 100)
                
                lba = tk.Label(self.listFramevp,
                        text = "Back",
                        )
                lba.grid(column = 3, 
                        row = row,
                        sticky  = "w")

                # Left
                row += 1
                self.etl = tk.Entry(self.listFramevp,
                                justify="left",
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error
                                )
                self.etl.grid(column = 2, 
                        row  = row,
                        sticky  = "w",
                        )
                # set defaut value for entry 
                self.etl.insert(tk.END, 100)
                
                lbl = tk.Label(self.listFramevp,
                        text = "Left",
                        )
                lbl.grid(column = 3, 
                        row = row,
                        sticky  = "w")        

                #right
                row += 1
                self.etr = tk.Entry(self.listFramevp,
                                justify="left",
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error
                                )
                self.etr.grid(column = 2, 
                        row  = row,
                        sticky  = "w",
                        )
                # set defaut value for entry 
                self.etr.insert(tk.END, 100)
                
                lbr = tk.Label(self.listFramevp,
                        text = "Right",
                        )
                lbr.grid(column = 3, 
                        row = row,
                        sticky  = "w")     
        
                """Traffic"""
                row = row + 1
                lb1 = tk.Label(self.listFramevp,
                                text = "Traffic Around:",
                                )
                lb1.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "e")
                # width of before 
                et1 = tk.Entry(self.listFramevp,
                                width = 10)
                et1.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                #Width of before label 
                lb2 = tk.Label(self.listFramevp,
                        text = "W_Before",
                        )
                lb2.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
               # height of entry after 
                et2 = tk.Entry(self.listFramevp,
                                width = 10)
                et2.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                #height of entry After label
                lb3 = tk.Label(self.listFramevp,
                        text = "W_After",
                        )
                lb3.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
                #height of Left entry
                et3 = tk.Entry(self.listFramevp,
                                width = 10)
                et3.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                #height of  Left label
                lb4 = tk.Label(self.listFramevp,
                        text = "W_Left",
                        )
                lb4.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
                #height of right entry
                et4 = tk.Entry(self.listFramevp,
                                width = 10)
                et4.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                #height of  right label
                lb5 = tk.Label(self.listFramevp,
                        text = "W_Right",
                        )
                lb5.grid(column = 2, 
                        row = row,
                        sticky  = "w")

                """ design """
                # Traffic
                row += 1
                lb6 = tk.Label(self.listFramevp,
                                text = "*Type House:",
                                )
                lb6.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "e")
                
                var1 = IntVar()
                rb1 = Radiobutton(self.listFramevp,
                                        text = "Type 1",
                                        variable= var1)
                rb1.grid(column = 1,
                                row  = row,
                                 sticky = "w")

                row += 1
                var2 = IntVar()
                rb2 = Radiobutton(self.listFramevp,
                                text = "Type 2",
                                variable= var2)
                rb2.grid(column = 1,
                                row  = row,
                                sticky = "w")

                row += 1
                var3 = IntVar()
                rb3 = Radiobutton(self.listFramevp,
                                        text = "Type 3",
                                        variable= var3)
                rb3.grid(column = 1,
                                row  = row,
                                 sticky = "w")

                """Scale of ATAD house """
                row = row + 1
                lb7 = tk.Label(self.listFramevp,
                                text = "Util Quantum:",
                                )
                lb7.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "e")
                # width of before 
                et5 = tk.Entry(self.listFramevp,width = 10)
                et5.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                #Width of before label 
                lb8 = tk.Label(self.listFramevp,
                        text = "Toilet",
                        )
                lb8.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
               # height of entry after 
                et6 = tk.Entry(self.listFramevp,width = 10)
                et6.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                #height of entry After label
                lb9 = tk.Label(self.listFramevp,
                        text = "Bathroom",
                        )
                lb9.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
                #height of Left entry
                et7 = tk.Entry(self.listFramevp,width = 10)
                et7.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                #height of  Left label
                lb10 = tk.Label(self.listFramevp,
                        text = "Bedroom",
                        )
                lb10.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
                #height of right entry
                et8 = tk.Entry(self.listFramevp,width = 10)
                et8.grid(column = 1, 
                        row = row,
                        sticky  = "w")

                #height of  right label
                lb11 = tk.Label(self.listFramevp,
                        text = "Church",
                        )
                lb11.grid(column = 2, 
                        row = row,
                        sticky  = "w")

                """ set confg for all (label, combo, entry)"""
                # config label

                labels = (wlb,lbh,lbb,
                        lba,lbl,lbl,arealb,
                        sbs,lbr,add,lb1,lb2,
                        lb3,lb4,lb5,lb6,rb1,
                        rb2,rb3,lb7,lb8,lb9,
                        lb10,lb11)
                for label in labels:
                        label.config (bg = self.bglb,
                                        font=self.labelfont_sm,
                                        anchor="e")
                
                # config combo
                cobl = (combodt,combopc,combowv)
                for conb in cobl:
                        conb.config (font=self.labelfont_sm)

                # config entry 
                entrys = (self.entryw,self.entryh,
                        self.etf,self.etb,self.etl,self.etr,self.adde,
                        et1,et2,et3,et4,et5,et6,
                        et7,et8)
                for entry in entrys:
                        entry.config(font=self.labelfont_sm,
                                        bg = "white",
                                        relief = tk.SOLID)
        
        def some_callback(self,event): # note that you must include the event as an arg, even if you don't use it.
                """delete value defaut entry"""
                self.adde.delete(0, "end")
                return None

        def createdrawing (self):
                """frawing layout follow customer"""
                plc = placereccenter(info_height_k= self.h,
                                        info_width_k= self.w,
                                        info_width_P =self.frameb[2],
                                        info_height_p=self.frameb[3]
                                        )
                # top left
                self.leftpoint = plc.pointleftrec()
                # top right
                self.rightpoint = plc.pointrightrec()
                try:

                        self.canvasb.delete(self.rectangle_wd ) # remove
                except:
                        pass
                # createrectange of parent 
                self.rectangle_wd = self.canvasb.create_rectangle (*self.leftpoint,
                                                                        *self.rightpoint,
                                                                        fill="blue")

                """
                self.createrectang_area(topleftpoint=self.leftpoint,
                                        toprightpoint=self.rightpoint,
                                        fill="blue")
                """

                plcn = setbackdimention(w_front=self.w_front,
                                        w_back=self.w_back,
                                        w_left=self.w_left,
                                        w_right=self.w_right,
                                        topleftpoint_p=self.leftpoint,
                                        toprightpoint_p=self.rightpoint 
                                        )
                topleftkid = plcn.topleftpoint()
                toprightkid = plcn.toprightpoint()
                """
                self.createrectang_area(topleftpoint=topleftkid,
                                        toprightpoint=toprightkid,
                                        fill="yellow")
                """
                try:

                        self.canvasb.delete(self.rrectangle_kid ) # remove
                except:
                        pass
                self.rrectangle_kid = self.canvasb.create_rectangle (*topleftkid,
                                                                        *toprightkid,
                                                                        fill="yellow")
               
        
                self.canvasb.pack(fill = tk.BOTH, expand = True)

        def validate_username(self, index, username):
                """validate user name """
                self.h = float(self.entryh.get())
                self.w =float(self.entryw.get()) 

                maxradio = (ratio(real_w=self.frameb[2],real_h=self.frameb[3],w= self.w,h=self.w).reratiomax()) * 1.2
                self.h = self.h/maxradio
                self.w = self.w/maxradio

                # get parameter setback width 
                try: 
                        self.w_front =  float(self.etf.get())/maxradio
                        self.w_back =  float(self.etb.get())/maxradio
                        self.w_left =  float(self.etl.get())/maxradio
                        self.w_right =  float(self.etr.get())/maxradio
                except:
                        pass
                self.createdrawing()
                return self.pattern.match(username) is not None
        def print_error(self):
                print("Invalid username character")
        
        def createrectang_area(self,topleftpoint = None, toprightpoint = None, fill = "yellow",alpha=0.5 ):
                """ create rectangle of area """
                self.rrectangle_wd = self.canvasb.create_rectangle (*topleftpoint,
                                                                        *toprightpoint,
                                                                        fill=fill)

        #windows zoom
        def zoomer(self,event):
                if (event.delta > 0):
                self.canvasb.scale("all", event.x, event.y, 1.1, 1.1)
                elif (event.delta < 0):
                self.canvasb.scale("all", event.x, event.y, 0.9, 0.9)
                self.canvasb.configure(scrollregion = self.canvasb.bbox("all"))