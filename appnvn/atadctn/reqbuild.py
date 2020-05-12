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
                                        setbackdimention,create_poly_from_tleft_bright)

import re

from pynvn.caculate.ratio import ratio

from pynvn.caculate.coord_point import coordp

from pynvn.caculate.area import area

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
                self.frameb =  [450,0,750,720,"aquamarine2"]
                self.sc = scbg(parent = self.filewin,
                                cavheight=self.cavheight_width[1],
                                cavwidth=self.cavheight_width[0],
                                bg = "white", 
                                bgpr = "#5181a7",
                                isonlyaframe= False,
                                framea =[0,0,450,720,"aquamarine2"], 
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
                #windows scroll
                self.canvasb.bind("<MouseWheel>",self.zoomer)
                # This is what enables using the mouse:
                self.canvasb.bind("<ButtonPress-1>", self.move_start)
                self.canvasb.bind("<B1-Motion>", self.move_move)
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
                self.et1 = tk.Entry(self.listFramevp,
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error
                                )
                self.et1.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                self.et1.insert(tk.END, 150)
                #Width of before label 
                lb2 = tk.Label(self.listFramevp,
                        text = "W_Font",
                        )
                lb2.grid(column = 2, 
                        row = row,
                        sticky  = "w")
                row += 1
               # height of entry after 
                self.et2 = tk.Entry(self.listFramevp,
                                width = 10,
                                validate="focusout",
                                validatecommand=vcmd,
                                invalidcommand=self.print_error)
                self.et2.grid(column = 1, 
                        row = row,
                        sticky  = "w")
                self.et2.insert(tk.END, 150)
                #height of entry After label
                lb3 = tk.Label(self.listFramevp,
                        text = "W_Back",
                        )
                lb3.grid(column = 2, 
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
                self.et3.insert(tk.END, 150)
                #height of  Left label
                lb4 = tk.Label(self.listFramevp,
                        text = "W_Left",
                        )
                lb4.grid(column = 2, 
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
                self.et4.insert(tk.END, 150)
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
                """delete value defaut entry"""
                self.adde.delete(0, "end")
                return None

        def createdrawing (self, colorroad = "#c49b65"):
                """drawing layout follow customer"""
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
                # create rectange of parent 
                self.rectangle_wd = self.canvasb.create_rectangle (*self.leftpoint,
                                                                        *self.rightpoint,
                                                                        fill="blue")
                
                # set back road 
                
                plcn = setbackdimention(w_front=self.w_front,
                                        w_back=self.w_back,
                                        w_left=self.w_left,
                                        w_right=self.w_right,
                                        topleftpoint_p=self.leftpoint,
                                        bottomrightpoint_p=self.rightpoint 
                                        )

                topleftkid = plcn.topleftpoint()
                toprightkid = plcn.toprightpoint()

                try:

                        self.canvasb.delete(self.rrectangle_kid ) # remove
                except:

                        pass

                self.rrectangle_kid = self.canvasb.create_rectangle (*topleftkid,
                                                                        *toprightkid,
                                                                        fill="#e79c2b")
                self.dis_r = 100
                # create road for front 
                rf = create_poly_from_tleft_bright(topleftpoint_p=self.leftpoint,
                                                        bottomrightpoint_p=self.rightpoint,
                                                        w_front_r= self.wr_front,
                                                        w_back_r=self.wr_back,
                                                        w_left_r=self.wr_left,
                                                        w_right_r=self.wr_right,
                                                        dis_r=self.dis_r )
                rfa = rf.roadfront()

                # create top left and bottom right of road 
                tlrf = rf.toprandbottoml_roadfront()
                
                try:

                        self.canvasb.delete(self.rf ) # remove
                except:
                        pass                


                self.rf = self.canvasb.create_polygon(*rfa, 
                                                        fill = colorroad
                                                        )

                # create road for back 
                rba  =rf.roadback()
                # create top left and bottom  back of road 
                tlrb = rf.toprandbottoml_roadback()
                
                try:

                        self.canvasb.delete(self.rba ) # remove
                except:
                        pass                


                self.rba = self.canvasb.create_polygon(*rba, 
                                                        fill = colorroad)

                self.canvasb.pack(fill = tk.BOTH,
                                 expand = True)

                # create road for left
                rbl  =rf.roadleft()

                tlrl = rf.toprandbottoml_roadleft()
                
                try:

                        self.canvasb.delete(self.rbl ) # remove
                except:
                        pass                


                self.rbl = self.canvasb.create_polygon(*rbl, 
                                                        fill =colorroad)

                self.canvasb.pack(fill = tk.BOTH,
                                 expand = True)

                # create road for right
                rbr  =rf.roadright()
                tlrr = rf.toprandbottoml_roadright()
                
                try:

                        self.canvasb.delete(self.rbr ) # remove
                except:
                        pass                


                self.rbr = self.canvasb.create_polygon(*rbr, 
                                                        fill = colorroad)

                self.canvasb.pack(fill = tk.BOTH,
                                 expand = True)


                """ dim for all"""
                coord = coordp(topleftp=self.leftpoint,
                                bottomrightp=self.rightpoint,
                                rev_direction="left",
                                topleftk=topleftkid,
                                bottomrightk=toprightkid,
                                dis_dim=30)
                #dim for left
                
                try:

                        self.canvasb.delete(self.rll ) # remove
                except:
                        pass

                coordse = coord.pointstartend()

                self.rll = self.canvasb.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both")
                # create text 

                try:

                        self.canvasb.delete(self.cvt ) # remove
                except:
                        pass


                coordtext =coord.centertowpoint()

                self.cvt = self.canvasb.create_text(*coordtext, anchor="n",text =str(self.hr), angle=90)

                #dim for top
                try:

                        self.canvasb.delete(self.rlr ) # remove
                except:
                        pass
                coord.rev_direction = "top"
                coordse = coord.pointstartend()

                self.rlr = self.canvasb.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                # create text 
                try:

                        self.canvasb.delete(self.cvtt ) # remove
                except:
                        pass
                coordtext =coord.centertowpoint()

                self.cvtt = self.canvasb.create_text(*coordtext, anchor="n",text =str(self.wr), angle=0)

                """ dim for setback front """
                
                try:

                        self.canvasb.delete(self.ftp ) # remove
                except:
                        pass
                coord.dis_dim = self.w/2
                ftp = coord.fronttowpoint()
                #coordse = coord.pointstartend()

                self.ftp = self.canvasb.create_line(*ftp,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.tcf ) # remove
                except:
                        pass
                coordf =coord.fronttowpointcenter()

                self.tcf = self.canvasb.create_text(*coordf, anchor="s",text =str(self.w_frontr), angle=90)

                #dim for setback back 
                
                try:

                        self.canvasb.delete(self.sbb ) # remove
                except:
                        pass
                sbb = coord.backtowpoint()
                #coordse = coord.pointstartend()

                self.sbb = self.canvasb.create_line(*sbb,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.tcb ) # remove
                except:
                        pass
                coordf =coord.backtowpointcenter()

                self.tcb = self.canvasb.create_text(*coordf, anchor="s",text =str(self.w_backr), angle=90)

                #dim for setback left 
                
                try:

                        self.canvasb.delete(self.sbl ) # remove
                except:
                        pass
                coord.dis_dim = self.h / 2
                sbl = coord.lefttowpoint()
                #coordse = coord.pointstartend()

                self.sbl = self.canvasb.create_line(*sbl,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.tcl ) # remove
                except:
                        pass
                coordl =coord.lefttowpointcenter()


                self.tcl = self.canvasb.create_text(*coordl, anchor="s",text =str(self.w_leftr), angle=0)

                #dim for setback right 
                
                try:

                        self.canvasb.delete(self.sbr ) # remove
                except:
                        pass
                sbr = coord.righttowpoint()
                #coordse = coord.pointstartend()

                self.sbr = self.canvasb.create_line(*sbr,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                
                # create text 
                try:

                        self.canvasb.delete(self.tcr ) # remove
                except:
                        pass
                coordr =coord.righttowpointcenter()

                self.tcr = self.canvasb.create_text(*coordr, 
                                                        anchor="s",
                                                        text =str(self.w_rightr), 
                                                        angle=0)

                # dim for road front
                coordf = coordp(topleftp=tlrf[0],
                                bottomrightp=tlrf[1],
                                rev_direction="left",
                                dis_dim =30)
                try:

                        self.canvasb.delete(self.dfrf ) # remove
                except:
                        pass
                coordf.dis_dim = -  self.w / 2
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

                self.tfrf = self.canvasb.create_text(*coordtext, anchor="n",text =str(self.wr_frontr), angle=90)
                
                # dim for road back
                coordf = coordp(topleftp=tlrb[0],
                                bottomrightp=tlrb[1],
                                rev_direction="left",
                                dis_dim=30)
                try:

                        self.canvasb.delete(self.dfrb ) # remove
                except:
                        pass
                coordf.dis_dim =  self.w / 2
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

                self.tfrb = self.canvasb.create_text(*coordtext, anchor="n",text =str(self.wr_backr), angle=90)

                
                # dim for road left
                coordf = coordp(topleftp=tlrl[0],
                                bottomrightp=tlrl[1],
                                rev_direction="top",
                                dis_dim=30)
                try:

                        self.canvasb.delete(self.dfrl ) # remove
                except:
                        pass
                coordf.dis_dim = - self.h / 2
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

                self.tfrl = self.canvasb.create_text(*coordtext, anchor="n",text =str(self.wr_leftr), angle=0)
                
                # dim for road right
                coordf = coordp(topleftp=tlrr[0],
                                bottomrightp=tlrr[1],
                                rev_direction="top",
                                dis_dim=30)
                try:

                        self.canvasb.delete(self.dfrr ) # remove
                except:
                        pass
                coordf.dis_dim = self.h / 2
                coordse = coordf.pointstartend()
               

                self.dfrr = self.canvasb.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both")

                # create text 
                try:

                        self.canvasb.delete(self.tfrr ) # remove
                except:
                        pass
                coordtext =coordf.centertowpoint()

                self.tfrr = self.canvasb.create_text(*coordtext, anchor="n",text =str(self.wr_rightr), angle=0)


                #caculate for area 
                are_k = area(topleftpoint= topleftkid, 
                                bottomrightpoint=toprightkid).areafromtopbottompoint()




                """ create dim for road """

                # create text 
                try:
                        self.canvasb.delete(self.tca ) # remove
                except:
                        pass
                coordrcenter = coord.centerpointkid()

                self.tca = self.canvasb.create_text(*coordrcenter, 
                                                        anchor="center",
                                                        text ="Area to build: {}".format(are_k), 
                                                        angle=0)


        def validate_username(self, index, username):
                """validate user name """
                # get parameter setback width 
                try:
                                                
                        # width and height of parent area
                        self.hr = float(self.entryh.get())
                        self.wr =float(self.entryw.get()) 
                        # set back area
                        self.w_frontr =  float(self.etf.get())
                        self.w_backr =  float(self.etb.get())
                        self.w_leftr =  float(self.etl.get())
                        self.w_rightr =  float(self.etr.get())
                        # traffice around
                        self.wr_frontr =  float(self.et1.get())
                        self.wr_backr =  float(self.et2.get())
                        self.wr_leftr=  float(self.et3.get())
                        self.wr_rightr=  float(self.et4.get())
                        try:
                                self.maxradio = ratio(real_w=self.frameb[2],
                                                real_h=self.frameb[3],
                                                w = self.wr + self.w_leftr + self.w_rightr + self.wr_leftr + self.wr_rightr + 200,
                                                h = self.hr + self.w_frontr + self.w_backr + self.wr_frontr + self.wr_backr + 200).reratiomax()
                        except:
                                messagebox.showerror("Eror", "check ratio of class ratio" )
                        # width and height of parent area
                        self.h = self.hr / self.maxradio
                        self.w =self.wr / self.maxradio
                        # set back area
                        self.w_front =  self.w_frontr / self.maxradio
                        self.w_back =  self.w_backr / self.maxradio
                        self.w_left =   self.w_leftr / self.maxradio
                        self.w_right =  self.w_rightr / self.maxradio
                        # traffice around
                        self.wr_front =  self.wr_frontr / self.maxradio
                        self.wr_back =  self.wr_backr  / self.maxradio
                        self.wr_left =  self.wr_leftr / self.maxradio
                        self.wr_right = self.wr_rightr / self.maxradio
                except:
                        messagebox.showerror("Eror", "check value of entry" )
                self.createdrawing()
                return self.pattern.match(username) is not None

        def print_error(self):
                print("Invalid username character")
        
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
                        self.canvasb.scale("all", event.x, event.y, 1.1, 1.1)
                elif (event.delta < 0):
                        self.canvasb.scale("all", event.x, event.y, 0.9, 0.9)
                        self.canvasb.configure(scrollregion = self.canvasb.bbox("all"))
                
        #move
        def move_start(self, event):
                self.canvasb.scan_mark(event.x, event.y)
        def move_move(self, event):
                self.canvasb.scan_dragto(event.x, event.y, gain=1)