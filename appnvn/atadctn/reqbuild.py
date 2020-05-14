from tkinter import (Frame,
                    Tk,
                    Toplevel,
                    StringVar,
                    IntVar,
                    Radiobutton
                    )
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.menu import menu
from appnvn.atadctn.treectn import (scbg,
                                        createcroll,
                                        cvframe)
from pynvn.caculate.cacul_cavas import (placereccenter,
                                        setbackdimention,
                                        create_poly_from_tleft_bright)

import re

from pynvn.caculate.ratio import ratio

from pynvn.caculate.coord_point import coordp

from pynvn.caculate.area import area
import string
class reqbuild(Frame):
        """Customer information"""
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
                        imagepre = None
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
                self.imagepre = imagepre
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
                self.cavheight_width = [1200,750]
                self.framea = [0,0,450,750,"white"]
                self.frameb = [450,0,750,750,"aquamarine2"]

                self.sc = scbg(parent = self.filewin,
                                cavheight=self.cavheight_width[1],
                                cavwidth=self.cavheight_width[0],
                                bg = "aquamarine2", 
                                bgpr = "#5181a7",
                                isonlyaframe= False,
                                framea = self.framea, 
                                frameb = self.frameb 
                                )
        
                self.height = 6000
                self.width = 7000
                # set back area
                self.w_front =  500
                self.w_back =  500
                self.w_left =  500
                self.w_right =  1000
                # traffice around
                self.wr_front =  1000
                self.wr_back =  1200
                self.wr_left=  1300
                self.wr_right= 500
                self.dis_r = 1000
                self.dis_dim = self.dis_r/3
                self.dis_direc = 400
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
                #windows scroll
                self.canvasb.bind("<MouseWheel>",self.zoomer)
                # This is what enables using the mouse:
                self.canvasb.bind("<ButtonPress-1>", self.move_start)
                self.canvasb.bind("<B1-Motion>", self.move_move)
                #self.createdrawing()
                self.pattern = re.compile("[0-9]")
                self.createdrawing()
                # scale in cavas 
                self.minradio = ratio(real_w=self.frameb[2],
                                        real_h=self.frameb[3],
                                        w = self.value_dis * 2,
                                        h = self.value_dis * 2).reratiomin()

                self.canvasb.scale("all",self.frameb[2]/2, 
                                        self.frameb[3]/2, 
                                        self.minradio/1.1, 
                                        self.minradio/1.1)

        def creategui(self):
                """Create gui for customer information"""
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

                self.entryw.insert(tk.END, self.width)
                self.entryw.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                #Width label
                self.lbw = tk.Label(self.listFramevp,
                        text = "Width",
                        )
                self.lbw.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
               # height entry 
                self.entryh = tk.Entry(self.listFramevp,
                                        width = 10,
                                        validate="focusout",
                                        validatecommand=vcmd,
                                        invalidcommand=self.print_error)
                self.entryh.insert(tk.END, self.height)
                self.entryh.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                #height label
                self.lbh = tk.Label(self.listFramevp,
                        text = "Height",
                        )
                self.lbh.grid(column = 2, 
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
                self.etf.insert(tk.END, self.w_front)
                
                self.lbf = tk.Label(self.listFramevp,
                        text = "Front",
                        )
                self.lbf.grid(column = 3, 
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
                self.etb.insert(tk.END, self.w_back)
                
                self.lbb = tk.Label(self.listFramevp,
                        text = "Back",
                        )
                self.lbb.grid(column = 3, 
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
                self.etl.insert(tk.END, self.w_left)
                
                self.lbl = tk.Label(self.listFramevp,
                        text = "Left",
                        )
                self.lbl.grid(column = 3, 
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
                self.etr.insert(tk.END, self.w_right)
                
                self.lbr = tk.Label(self.listFramevp,
                        text = "Right",
                        )
                self.lbr.grid(column = 3, 
                        row = row,
                        sticky  = "w")     
        
                ############traffic 
                row = row + 1
                lb1 = tk.Label(self.listFramevp,
                                text = "Traffic Around:",
                                )
                lb1.grid(column = 0, 
                        row = row,
                        padx = self.padx,
                        sticky  = "e")
                # width of before 
                self.et1 = tk.Entry(self.listFramevp,
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error
                                )
                self.et1.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                self.et1.insert(tk.END, self.wr_front)
                #Width of before label 
                self.lbwf = tk.Label(self.listFramevp,
                        text = "W_Font",
                        )
                self.lbwf.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
               # height of entry back 
                self.et2 = tk.Entry(self.listFramevp,
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error)
                self.et2.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                self.et2.insert(tk.END, self.w_back)
                #height of entry After label
                self.lbwb = tk.Label(self.listFramevp,
                        text = "W_Back",
                        )
                self.lbwb.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
                #height of Left entry
                self.et3 = tk.Entry(self.listFramevp,
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error)
                self.et3.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                self.et3.insert(tk.END, self.wr_left)
                #height of  Left label
                self.lbwl = tk.Label(self.listFramevp,
                        text = "W_Left",
                        )
                self.lbwl.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
                #height of right entry
                self.et4 = tk.Entry(self.listFramevp,
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error)
                self.et4.grid(column = 1,
                        row = row,
                        sticky  = "w")
                self.et4.insert(tk.END, self.wr_right)
                #height of  right label
                self.lbwr = tk.Label(self.listFramevp,
                        text = "W_Right",
                        )
                self.lbwr.grid(column = 2, 
                        row = row,
                        sticky  = "w")

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
                        sticky  = "w"
                        )

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
                        sticky  = "w"
                        )

                #height of  Left label
                lb10 = tk.Label(self.listFramevp,
                        text = "Bedroom",
                        )
                lb10.grid(column = 2, 
                        row = row,
                        sticky  = "w"
                        )

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
                        sticky  = "w"
                        )
                row += 1
                # next and previous buttons
                btnext = tk.Button(self.listFramevp,
                                        image = self.imagepre,
                                        bg = "white",
                                        activebackground = "#33B5E5", 
                                        relief = tk.FLAT
                                        )
                btnext.grid(column = 1,
                                row = row,
                                columnspan = 1,
                                sticky  = "w",
                                )

                btpre = tk.Button(self.listFramevp,
                                        image  = self.imagenext,
                                        bg = "white",
                                        activebackground = "#33B5E5", 
                                        relief = tk.FLAT
                                        )
                btpre.grid(column = 1,
                                row = row,
                                sticky  = "e"
                                )

                """ set confg for all (label, combo, entry)"""
                # config label

                labels = (self.lbw,self.lbh,self.lbf,
                        self.lbb,self.lbl,self.lbl,arealb,
                        sbs,self.lbr,add,lb1,self.lbwf,
                        self.lbwb,self.lbwl,self.lbwr,lb6,rb1,
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
                                self.etf,self.etb,
                                self.etl,self.etr,
                                self.adde,self.et1,self.et2,
                                self.et3,self.et4,et5,
                                et6,et7,et8)
                for entry in entrys:
                        entry.config(font=self.labelfont_sm,
                                        bg = "white",
                                        relief = tk.SOLID)
        
        def some_callback(self,event): # note that you must include the event as an arg, even if you don't use it.
                """Delete value defaut entry"""
                self.adde.delete(0, "end")
                return None

        def createdrawing (self, colorroad = "#c49b65"):
                """Drawing layout follow customer"""
                plc = placereccenter(info_height_k= self.height,
                                        info_width_k= self.width,
                                        info_width_P =self.frameb[2],
                                        info_height_p=self.frameb[3]
                                        )
                # top left
                self.leftpoint = plc.pointleftrec()
                # top right
                self.rightpoint = plc.pointrightrec()

                # create rectangle parent
                self.createrecp()
                """set back road  """
                
                plcn = setbackdimention(w_front=self.w_front,
                                        w_back=self.w_back,
                                        w_left=self.w_left,
                                        w_right=self.w_right,
                                        topleftpoint_p=self.leftpoint,
                                        bottomrightpoint_p=self.rightpoint 
                                        )

                self.topleftkid = plcn.topleftpoint()
                self.toprightkid = plcn.toprightpoint()

                # create rectangle kid
                self.createreck()

                # create road for front 
                rf = create_poly_from_tleft_bright(topleftpoint_p=self.leftpoint,
                                                        bottomrightpoint_p=self.rightpoint,
                                                        w_front_r= self.wr_front,
                                                        w_back_r=self.wr_back,
                                                        w_left_r=self.wr_left,
                                                        w_right_r=self.wr_right,
                                                        dis_r=self.dis_r )
                rfa = rf.roadfront()

                #create front of road
                self.createfront(rfa,fill = colorroad)
                tlrf = rf.toprandbottoml_roadfront()

                # create road for back 
                rba  =rf.roadback()
                self.createback(rba,fill = colorroad)

                # create top left and bottom  back of road 
                tlrb = rf.toprandbottoml_roadback()

                # create road for left
                rbl  =rf.roadleft()
                self.createleft(rbl,fill = colorroad)

                tlrl = rf.toprandbottoml_roadleft()

                # create road for right
                rbr  =rf.roadright()
                self.createright(rbr,fill = colorroad)
                tlrr = rf.toprandbottoml_roadright()
                
                self.canvasb.pack(fill = tk.BOTH,
                                 expand = True)

                # dim for item all
                self.coord = coordp(topleftp=self.leftpoint,
                                bottomrightp=self.rightpoint,
                                rev_direction="left",
                                topleftk=self.topleftkid,
                                bottomrightk=self.toprightkid,
                                dis_dim=self.dis_dim)

                # create dim for h 
                self.dimforh()

                #dim for top
                self.dimforw()

                #dim for setback front
                self.dimforsbf()

                #dim for setback back 
                self.dimforsbb()

                #dim for setback left 
                self.dimforsbl()

                #dim for setback right 
                self.dimforsbr()
                
                # dim for road front
                self.dimforroadfront(tlrf=tlrf)
                # dim for road back
                self.dimforroadback (tlrb=tlrb)
                
                # dim for road left
                self.dimforroadleft(tlrl=tlrl)

                # dim for road right
                self.dimforroadright(tlrr=tlrr)

                #caculate for area 
                self.cacularea()

                # create direction nwse
                self.directnmwe(font =('times', 16), fill = "black")
        def validate_username(self, index, username):
                """validate user name """
                self.getparameter()
                self.createdrawing()
                self.currentsize()
                return self.pattern.match(username) is not None
        def print_error(self):
                print("Invalid username character, only input number")
        
        def createrectang_area(self,topleftpoint = None, 
                                toprightpoint = None, 
                                fill = "yellow",
                                alpha=0.5 ):

                """ create rectangle of area """
                self.rrectangle_wd = self.canvasb.create_rectangle (*topleftpoint,
                                                                        *toprightpoint,
                                                                        fill=fill)

        #windows zoom
        def zoomer(self,event):
                if (event.delta > 0):
                        self.canvasb.scale("all",
                                                self.frameb[2]/2, 
                                                self.frameb[3]/2, 1.1, 1.1)
                elif (event.delta < 0):
                        self.canvasb.scale("all", 
                                                self.frameb[2]/2, 
                                                self.frameb[3]/2, 0.9, 0.9)
                        self.canvasb.configure(scrollregion = self.canvasb.bbox("all"))
                
        #move
        def move_start(self, event):
                self.canvasb.scan_mark(event.x, event.y)
        def move_move(self, event):
                self.canvasb.scan_dragto(event.x, event.y, gain=1)
        def getparameter(self):                                                
                # width and height of parent area
                
                try:
                        self.height = float(self.entryh.get())
                except:
                        messagebox.showerror("Error",
                                                "check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbh["text"]))
                
                try:
                        self.width =float(self.entryw.get()) 
                except:
                        messagebox.showerror("Error",
                                                "check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbw["text"]))
                
                # set distance of road and rec
                self.dis_r = max([self.height,self.width])/4
                # set distance of dim 
                self.dis_dim = self.dis_r/2.5
                #set distace of direction 
                self.dis_direc = self.dis_dim
                # set back area
                try:
                        self.w_front =  float(self.etf.get())
                except:
                        messagebox.showerror("Error",
                                                "check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbf["text"]))

                try:
                        self.w_back =  float(self.etb.get())
                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbb["text"]))
                
                try:
                        self.w_left =  float(self.etl.get())
                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                 can not string".format(self.lbl["text"]))
                
                try:
                        self.w_right =  float(self.etr.get())

                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbr["text"]))          
                # traffice around
                try:
                        self.wr_front =  float(self.et1.get())
                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                 can not string".format(self.lbwf["text"])) 
                
                try:
                        self.wr_back =  float(self.et2.get())
                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbwb["text"])) 
                
                try:
                        self.wr_left=  float(self.et3.get())
                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                can not string".format(self.lbwl["text"])) 

                try:
                        self.wr_right=  float(self.et4.get())
                except:
                        messagebox.showerror("Error","check your input {0},\
                                                \nCharacters input must be numbers\
                                                 can not string".format(self.lbwr["text"]))                    
        def reratio (self):
                """ caculate ratio of window"""
                try:
                        self.minradio = ratio(real_w=self.frameb[2],
                                        real_h=self.frameb[3],
                                        w = self.value_dis * 2 ,
                                        h =self.value_dis * 2).reratiomin()
                except:
                        messagebox.showerror("Eror", "check ratio of class ratio" )

        def currentsize (self):
                """ Current size to setup when event"""
                self.reratio()
                self.canvasb.scale("all",
                                self.frameb[2]/2, 
                                self.frameb[3]/2, 
                                self.minradio/1.1, 
                                self.minradio/1.1)

        def createrecp (self):
                """Create rectangle of widget parent"""
                try:

                        self.canvasb.delete(self.rectangle_wd ) # remove
                except:
                        pass
                # create rectange of parent 
                self.rectangle_wd = self.canvasb.create_rectangle (*self.leftpoint,
                                                                        *self.rightpoint,
                                                                        fill="yellow")
        def createreck (self,**kwargs):
                """Create rectangle of widget kid"""
                try:

                        self.canvasb.delete(self.rrectangle_kid ) # remove
                except:

                        pass

                self.rrectangle_kid = self.canvasb.create_rectangle (*self.topleftkid,
                                                                        *self.toprightkid,
                                                                        fill="#e79c2b")
        
        def createfront(self,rfa,**kwargs):
                """Create front road"""
                if  int(self.wr_front) != 0:
                        try:

                                self.canvasb.delete(self.crrf ) # remove
                        except:
                                pass                

                        self.crrf = self.canvasb.create_polygon(*rfa,**kwargs)

        def createback(self,rfa,**kwargs):
                """create back road"""
                if  int(self.wr_back) != 0:
                        try:

                                self.canvasb.delete(self.ra ) # remove
                        except:
                                pass                

                        self.ra = self.canvasb.create_polygon(*rfa,**kwargs)

        def createleft(self,rfa,**kwargs):
                """create left road"""
                if  int(self.wr_left) != 0:
                        try:

                                self.canvasb.delete(self.rf ) # remove
                        except:
                                pass                

                        self.rf = self.canvasb.create_polygon(*rfa,**kwargs)

        def createright(self,rfa,**kwargs):
                """create right road"""
                if  int(self.wr_right) != 0:
                        try:
                                self.canvasb.delete(self.rr ) # remove
                        except:
                                pass                

                        self.rr = self.canvasb.create_polygon(*rfa,**kwargs)
        
        def dimforh(self,**kwargs):
                try:

                        self.canvasb.delete(self.rll ) # remove
                except:
                        pass

                coordse = self.coord.pointstartend()

                self.rll = self.canvasb.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both")
                # create text 

                try:

                        self.canvasb.delete(self.cvt ) # remove
                except:
                        pass

                coordtext =self.coord.centertowpoint()

                self.cvt = self.canvasb.create_text(*coordtext, 
                                                        anchor="n",
                                                        text =str(self.height), 
                                                        angle=90)
        def dimforw(self,**kwargs):
                try:
                        self.canvasb.delete(self.dfwl ) # remove
                except:
                        pass
                self.coord.rev_direction = "top"
                coordse = self.coord.pointstartend()

                self.dfwl = self.canvasb.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                # create text 
                try:

                        self.canvasb.delete(self.dfwt ) # remove
                except:
                        pass
                coordtext =self.coord.centertowpoint()

                self.dfwt = self.canvasb.create_text(*coordtext, 
                                                        anchor="n",
                                                        text =str(self.width), 
                                                        angle=0)

        def dimforsbf (self,**kwargs):
                
                try:
                        self.canvasb.delete(self.dfsbfl ) # remove
                except:
                        pass
                self.coord.dis_dim = self.width/2
                dfsbfl = self.coord.fronttowpoint()
                #coordse = coord.pointstartend()

                self.dfsbfl = self.canvasb.create_line(*dfsbfl,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.dfsbft ) # remove
                except:
                        pass
                coordf =self.coord.fronttowpointcenter()
                if  int(self.w_front) != 0 :
                        self.dfsbft = self.canvasb.create_text(*coordf, 
                                                                anchor="s",
                                                                text =str(self.w_front), 
                                                                angle=90)      
        
        def dimforsbb (self,**kwargs):
                
                try:

                        self.canvasb.delete(self.dfsbbl) # remove
                except:
                        pass
                sbb = self.coord.backtowpoint()

                self.dfsbbl = self.canvasb.create_line(*sbb,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.dfsbbt ) # remove
                except:
                        pass
                coordf =self.coord.backtowpointcenter()

                if  int(self.w_back) != 0 :

                        self.dfsbbt = self.canvasb.create_text(*coordf, 
                                                                anchor="s",
                                                                text =str(self.w_back), 
                                                                angle=90)

        def dimforsbl(self,**kwargs):

                try:
                        self.canvasb.delete(self.dfsbl ) # remove
                except:
                        pass
                self.coord.dis_dim = self.height / 2
                sbl = self.coord.lefttowpoint()

                self.dfsbl = self.canvasb.create_line(*sbl,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )

                # create text 
                try:
                        self.canvasb.delete(self.dfsbt ) # remove
                except:
                        pass
        
                coordl =self.coord.lefttowpointcenter()

                if  int(self.w_left) != 0 :

                        self.dfsbt = self.canvasb.create_text(*coordl, 
                                                                anchor="s",
                                                                text =str(self.w_left), 
                                                                angle=0)
        
        def dimforsbr(self,**kwargs):

                try:
                        self.canvasb.delete(self.dfsbrl ) # remove
                except:
                        pass
                sbr = self.coord.righttowpoint()
                #coordse = coord.pointstartend()

                self.dfsbrl = self.canvasb.create_line(*sbr,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.dfsbrt ) # remove
                except:
                        pass
                coordr =self.coord.righttowpointcenter()

                if  int(self.w_right) != 0 :

                        self.dfsbrt = self.canvasb.create_text(*coordr, 
                                                                anchor="s",
                                                                text =str(self.w_right), 
                                                                angle=0)

        def dimforroadfront(self,tlrf,**kwargs):

                if  int(self.wr_front) != 0 :
                        coordf = coordp(topleftp=tlrf[0],
                                        bottomrightp=tlrf[1],
                                        rev_direction="left",
                                        dis_dim =30)
                        try:

                                self.canvasb.delete(self.dfrf ) # remove
                        except:
                                pass
                        coordf.dis_dim = - self.width / 2
                        coordse = coordf.pointstartend()

                        self.dfrf = self.canvasb.create_line(*coordse,
                                                                fill = "red",
                                                                arrow = "both")

                        # create text 
                        try:

                                self.canvasb.delete(self.tfrf ) # remove
                        except:
                                pass
                        coordtext =coordf.centertowpoint()

                        self.tfrf = self.canvasb.create_text(*coordtext, 
                                                                anchor="n",
                                                                text =str(self.wr_front), 
                                                                angle=90)
        
        def dimforroadback(self,tlrb,**kwargs):
                """ dim for road back """
                if  int(self.wr_back) != 0 :
                        coordf = coordp(topleftp=tlrb[0],
                                        bottomrightp=tlrb[1],
                                        rev_direction="left",
                                        dis_dim=30)
                        try:

                                self.canvasb.delete(self.dfrb ) # remove
                        except:
                                pass
                        coordf.dis_dim =  self.width / 2
                        coordse = coordf.pointstartend()
                

                        self.dfrb = self.canvasb.create_line(*coordse,
                                                                fill = "red",
                                                                arrow = "both")

                        # create text 
                        try:

                                self.canvasb.delete(self.tfrb ) # remove
                        except:
                                pass
                        coordtext =coordf.centertowpoint()

                        self.tfrb = self.canvasb.create_text(*coordtext, 
                                                                anchor="n",
                                                                text =str(self.wr_back), 
                                                                angle=90)

        def dimforroadleft(self,tlrl,**kwargs):
                """ dim for road left """
                if  int(self.wr_left) != 0 :
                        coordf = coordp(topleftp=tlrl[0],
                                        bottomrightp=tlrl[1],
                                        rev_direction="top",
                                        dis_dim=30)
                        try:

                                self.canvasb.delete(self.dfrl ) # remove
                        except:
                                pass
                        coordf.dis_dim = - self.height / 2
                        coordse = coordf.pointstartend()
                

                        self.dfrl = self.canvasb.create_line(*coordse,
                                                                fill = "red",
                                                                arrow = "both")

                        # create text 
                        try:

                                self.canvasb.delete(self.tfrl ) # remove
                        except:
                                pass
                        coordtext =coordf.centertowpoint()

                        self.tfrl = self.canvasb.create_text(*coordtext, 
                                                                anchor="n",
                                                                text =str(self.wr_left), 
                                                                angle=0)

        def dimforroadright(self,tlrr,**kwargs):
                """ dim for road right """
                if  int(self.wr_right) != 0 :
                        coordf = coordp(topleftp=tlrr[0],
                                        bottomrightp=tlrr[1],
                                        rev_direction="top",
                                        dis_dim=30)
                        try:

                                self.canvasb.delete(self.dfrr ) # remove
                        except:
                                pass
                        coordf.dis_dim = self.height / 2
                        coordse = coordf.pointstartend()
                

                        self.dfrr = self.canvasb.create_line(*coordse,
                                                                fill = "red",
                                                                arrow = "both")
                        # create text 
                        try:

                                self.canvasb.delete(self.tfrr ) # remove
                        except:
                                pass
                        coordtext = coordf.centertowpoint()

                        self.tfrr = self.canvasb.create_text(*coordtext, 
                                                                anchor="n",
                                                                text =str(self.wr_right), 
                                                                angle=0)
        
        def cacularea(self,**kwargs):
                """ caculate area """

                are_k = area(topleftpoint= self.topleftkid, 
                                bottomrightpoint=self.toprightkid).areafromtopbottompoint()

                """ create dim for road """

                # create text 
                try:
                        self.canvasb.delete(self.tca ) # remove
                except:
                        pass
                coordrcenter = self.coord.centerpointkid()

                self.tca = self.canvasb.create_text(*coordrcenter, 
                                                        anchor="center",
                                                        text ="Area to build: {}".format(are_k), 
                                                        angle=0,
                                                        **kwargs)
        
        def directnmwe(self,**kwargs ):
                """ create text direction nmwe"""

                self.value_dis = max ([self.height/2 + self.dis_r + self.wr_front + self.dis_direc, 
                                self.height/2 + self.dis_r + self.wr_back + self.dis_direc,
                                self.width/2 + self.dis_r + self.wr_left + self.dis_direc,
                                self.width/2 + self.dis_r + self.wr_right + self.dis_direc
                                ])

                cp = coordp(topleftp=self.leftpoint,
                                bottomrightp=self.rightpoint,
                                dis_direc= self.dis_direc)

                fpc = cp.centerpoinparent()

                frontp = [fpc[0],fpc[1] - self.value_dis]
                backp = [fpc[0],fpc[1] + self.value_dis]

                leftp = [fpc[0] - self.value_dis ,fpc[1]]
                rightp = [fpc[0] + self.value_dis ,fpc[1]]

                # create text front
                try:
                        self.canvasb.delete(self.frf ) # remove
                except:
                        pass

                self.frf = self.canvasb.create_text(*frontp, 
                                                        anchor="center",
                                                        text ="Front", 
                                                        angle=0,
                                                        **kwargs)
                # create text back
                try:
                        self.canvasb.delete(self.frb ) # remove
                except:
                        pass

                self.frb = self.canvasb.create_text(*backp, 
                                                        anchor="center",
                                                        text ="Back", 
                                                        angle=0,
                                                        **kwargs)
                # create text left
                try:
                        self.canvasb.delete(self.frl ) # remove
                except:
                        pass

                self.frl = self.canvasb.create_text(*leftp, 
                                                        anchor="center",
                                                        text ="Left", 
                                                        angle=0,
                                                        **kwargs)
                # create text right 
                try:
                        self.canvasb.delete(self.frr ) # remove
                except:
                        pass

                self.frr = self.canvasb.create_text(*rightp, 
                                                        anchor="center",
                                                        text ="Right", 
                                                        angle=0,
                                                        **kwargs)
        