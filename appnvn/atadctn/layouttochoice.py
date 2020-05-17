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
from appnvn.atadctn.treectn import scbg
from pynvn.caculate.cacul_cavas import (placereccenter,
                                        setbackdimention,
                                        create_poly_from_tleft_bright)

import re

from pynvn.caculate.ratio import ratio

from pynvn.caculate.coord_point import coordp

from pynvn.caculate.area import area

from pynvn.cavas_drawing.buttondr import crebutton
import string

class layoutchoice(tk.Frame):
        """Customer information"""
        def __init__(self,tktk = None,
                        canvasb = None,
                        controller= None,
                        bglb = "white",
                        labelfont = ('times', 20),
                        labelfont_sm = ('times', 16),
                        imagenext = None,
                        imagepre = None,
                        frameb = [450,0,750,750,"aquamarine2"],
                        cavheight_width = [1200,750],
                        w_front = 100,
                        *args,**kwargs):
                self.tktk = tktk
                tk.Frame.__init__(self, tktk)
                self.controller = controller
                self.labelfont = labelfont
                self.labelfont_sm = labelfont_sm
                self.bglb = bglb
                self.imagenext = imagenext
                self.imagepre = imagepre
                self.height = kwargs["height"]
                self.width = kwargs["width"]
                # set back area
                self.w_front = 0
                self.w_back =  0
                self.w_left =  0
                self.w_right = 0
                # traffice around
                self.wr_front = 0
                self.wr_back = 0
                self.wr_left= 0
                self.wr_right= 0
                self.dis_r = kwargs["dis_r"]
                self.dis_dim = self.dis_r/3
                self.dis_direc = kwargs["dis_direc"]
                self.bg_frameb = kwargs["bg_frameb"]
                self.frameb = frameb 
                self.w_buttoncavas = 50
                self.frameb = [450,0,750,750,"aquamarine2"]

                self.frameaa = [0,0,750,700,"pink"]
                self.frameab = [0,700,750,50,"white"]

                self.sc = scbg(parent = self,
                                cavheight=self.frameb[3],
                                cavwidth=self.frameb[2],
                                bg = "aquamarine2", 
                                bgpr = "#5b9bd5",
                                isonlyaframe= False,
                                framea = self.frameaa, 
                                frameb =self.frameab
                                )

                frameaa = self.sc.framea
                frameab = self.sc.frameb
                self.canvasaa = tk.Canvas(frameaa, 
                                        bg = "azure",
                                        borderwidth=0,
                                        highlightthickness=0)
                self.canvasaa.pack(fill = tk.BOTH, 
                                        expand = 1) 

                self.canvasab = tk.Canvas(frameab,
                                                bg = "azure",
                                                borderwidth=0,
                                                highlightthickness=0)
                self.canvasab.pack(fill = tk.BOTH, expand = 1) 
                crebutton(self.canvasab,
                                crwidth=750/2 - 30, 
                                crheight=0, 
                                image = self.imagepre,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                crebutton(self.canvasab,
                                crwidth=750/2 + 30, 
                                crheight=0, 
                                image = self.imagenext,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)
                # create cavas frameb 
                # create gui for input from customer 
                #windows scroll
                
                self.canvasaa.bind("<MouseWheel>",self.zoomer)
                # This is what enables using the mouse:
                self.canvasaa.bind("<ButtonPress-1>", self.move_start)
                self.canvasaa.bind("<B1-Motion>", self.move_move)
                self.pattern = re.compile("[0-9]")
                # create frawing  
                self.createdrawing()
                # scale in cavas 
                self.minradio = ratio(real_w=self.frameb[2],
                                        real_h=self.frameb[3],
                                        w = self.value_dis * 2,
                                        h = self.value_dis * 2).reratiomin()

                self.canvasaa.scale("all",self.frameb[2]/2, 
                                        self.frameb[3]/2, 
                                        self.minradio/1.1, 
                                        self.minradio/1.1)
        def createdrawing (self, colorroad = "#c49b65",*args,**kwargs):
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
                # set back road  """
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
                #caculate for area 
                self.cacularea()
                # create direction nwse
                self.directnmwe(font =('times', 16), fill = "black")

        def createrectang_area(self,topleftpoint = None, 
                                toprightpoint = None, 
                                fill = "yellow",
                                alpha=0.5 ):
                """ create rectangle of area """
                self.rrectangle_wd = self.canvasaa.create_rectangle (*topleftpoint,
                                                                        *toprightpoint,
                                                                        fill=fill)
        #windows zoom
        def zoomer(self,event):
                """windows zoom"""
                if (event.delta > 0):
                        self.canvasaa.scale("all",
                                                self.frameb[2]/2, 
                                                self.frameb[3]/2, 1.1, 1.1)
                elif (event.delta < 0):
                        self.canvasaa.scale("all", 
                                                self.frameb[2]/2, 
                                                self.frameb[3]/2, 0.9, 0.9)
                        self.canvasaa.configure(scrollregion = self.canvasaa.bbox("all"))
                
        #move
        def move_start(self, event):
                self.canvasaa.scan_mark(event.x, event.y)
        def move_move(self, event):
                self.canvasaa.scan_dragto(event.x, event.y, gain=1) 

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
                self.canvasaa.scale("all",
                                self.frameb[2]/2, 
                                self.frameb[3]/2, 
                                self.minradio/1.1, 
                                self.minradio/1.1)

        def createrecp (self):
                """Create rectangle of widget parent"""
                try:

                        self.canvasaa.delete(self.rectangle_wd ) # remove
                except:
                        pass
                # create rectange of parent 
                self.rectangle_wd = self.canvasaa.create_rectangle (*self.leftpoint,
                                                                        *self.rightpoint,
                                                                        fill="yellow")
        def createreck (self,**kwargs):
                """Create rectangle of widget kid"""
                try:

                        self.canvasaa.delete(self.rrectangle_kid ) # remove
                except:

                        pass

                self.rrectangle_kid = self.canvasaa.create_rectangle (*self.topleftkid,
                                                                        *self.toprightkid,
                                                                        fill="#e79c2b")
        
        def createfront(self,rfa,**kwargs):
                """Create front road"""
                if  int(self.wr_front) != 0:
                        try:

                                self.canvasaa.delete(self.crrf ) # remove
                        except:
                                pass                

                        self.crrf = self.canvasaa.create_polygon(*rfa,**kwargs)

        def createback(self,rfa,**kwargs):
                """create back road"""
                if  int(self.wr_back) != 0:
                        try:

                                self.canvasaa.delete(self.ra ) # remove
                        except:
                                pass                

                        self.ra = self.canvasaa.create_polygon(*rfa,**kwargs)

        def createleft(self,rfa,**kwargs):
                """create left road"""
                if  int(self.wr_left) != 0:
                        try:

                                self.canvasaa.delete(self.rf ) # remove
                        except:
                                pass                

                        self.rf = self.canvasaa.create_polygon(*rfa,**kwargs)

        def createright(self,rfa,**kwargs):
                """create right road"""
                if  int(self.wr_right) != 0:
                        try:
                                self.canvasaa.delete(self.rr ) # remove
                        except:
                                pass                

                        self.rr = self.canvasaa.create_polygon(*rfa,**kwargs)
        
        def dimforh(self,**kwargs):
                try:

                        self.canvasaa.delete(self.rll ) # remove
                except:
                        pass

                coordse = self.coord.pointstartend()

                self.rll = self.canvasaa.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both")
                # create text 

                try:

                        self.canvasaa.delete(self.cvt ) # remove
                except:
                        pass

                coordtext =self.coord.centertowpoint()

                self.cvt = self.canvasaa.create_text(*coordtext, 
                                                        anchor="n",
                                                        text =str(self.height), 
                                                        angle=90)
        def dimforw(self,**kwargs):
                try:
                        self.canvasaa.delete(self.dfwl ) # remove
                except:
                        pass
                self.coord.rev_direction = "top"
                coordse = self.coord.pointstartend()

                self.dfwl = self.canvasaa.create_line(*coordse,
                                                        fill = "red",
                                                        arrow = "both"
                                                        )
                # create text 
                try:

                        self.canvasaa.delete(self.dfwt ) # remove
                except:
                        pass
                coordtext =self.coord.centertowpoint()

                self.dfwt = self.canvasaa.create_text(*coordtext, 
                                                        anchor="n",
                                                        text =str(self.width), 
                                                        angle=0)
        
        def cacularea(self,**kwargs):
                """ caculate area """

                are_k = area(topleftpoint= self.topleftkid, 
                                bottomrightpoint=self.toprightkid).areafromtopbottompoint()

                """ create dim for road """

                # create text 
                try:
                        self.canvasaa.delete(self.tca ) # remove
                except:
                        pass
                coordrcenter = self.coord.centerpointkid()

                self.tca = self.canvasaa.create_text(*coordrcenter, 
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
                        self.canvasaa.delete(self.frf ) # remove
                except:
                        pass

                self.frf = self.canvasaa.create_text(*frontp, 
                                                        anchor="center",
                                                        text ="Front", 
                                                        angle=0,
                                                        **kwargs)
                # create text back
                try:
                        self.canvasaa.delete(self.frb ) # remove
                except:
                        pass

                self.frb = self.canvasaa.create_text(*backp, 
                                                        anchor="center",
                                                        text ="Back", 
                                                        angle=0,
                                                        **kwargs)
                # create text left
                try:
                        self.canvasaa.delete(self.frl ) # remove
                except:
                        pass

                self.frl = self.canvasaa.create_text(*leftp, 
                                                        anchor="center",
                                                        text ="Left", 
                                                        angle=0,
                                                        **kwargs)
                # create text right 
                try:
                        self.canvasaa.delete(self.frr ) # remove
                except:
                        pass

                self.frr = self.canvasaa.create_text(*rightp, 
                                                        anchor="center",
                                                        text ="Right", 
                                                        angle=0,
                                                        **kwargs)
