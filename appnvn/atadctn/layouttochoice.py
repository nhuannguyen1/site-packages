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
from pynvn.cavaszm.cavaszm import zmcv
import string

from pynvn.nsew.nsew import directnmwe

from pynvn.cavas_write.writetext import writetext

from pynvn.cavas_dim.cavas_dim import dimrec

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
                        imagenextlayout = None, 
                        imageprelayout = None,
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
                self.imagenextlayout = imagenextlayout
                self.imageprelayout = imageprelayout
                 # set back area
                self.w_front =  w_front
                self.w_back =  kwargs["w_back"]
                self.w_left =  kwargs["w_left"]
                self.w_right =  kwargs["w_right"]
                # traffice around
                self.wr_front =  kwargs["wr_front"]
                self.wr_back =  kwargs["wr_back"]
                self.wr_left=  kwargs["wr_left"]
                self.wr_right= kwargs["wr_right"]

                self.dis_r = kwargs["dis_r"]
                self.dis_dim = self.dis_r/3
                self.dis_direc = kwargs["dis_direc"]
                self.frameb = frameb 
                self.w_buttoncavas = 50
                self.frameaa = [40,0,670,700,"yellow"]
                self.frameab = [0,700,750,50,"azure"]
                self.frameac = [0,0,40,700,"azure"]
                self.framead = [710,0,40,700,"azure"]

                self.sc = scbg(parent = self,
                                cavheight=self.frameb[3],
                                cavwidth=self.frameb[2],
                                bg = "aquamarine2", 
                                bgpr = "#5b9bd5",
                                isonlyaframe= False,
                                framea = self.frameaa, 
                                frameb =self.frameab,
                                framec =self.frameac,
                                framed = self.framead,
                                frameaincavas=True, 
                                framebincavas=True,
                                framecincavas=True, 
                                framedincavas= True
                                )
                # cavas a
                self.canvasaa = self.sc.canvasa

                # cavas b
                self.canvasab = self.sc.canvasb
        
                # cavas c 
                self.canvasac = self.sc.canvasc
                crebutton(self.canvasac,
                                crwidth=self.frameac[2]/2, 
                                crheight=self.frameac[3]/2, 
                                image = self.imageprelayout,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                # cavas d
                self.canvasad =  self.sc.canvasd

                crebutton(self.canvasad,
                                crwidth=self.framead[2]/2, 
                                crheight=self.framead[3]/2, 
                                image = self.imagenextlayout,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                self.pattern = re.compile("[0-9]")
                # create frawing  
                self.createdrawing()
                # scale, move in cavas 

                zmcv(cavas=self.canvasaa,
                                frameb=self.frameaa,
                                value_dis=self.value_dis,
                                distancezx= -self.frameaa[0])

                crebutton(self.canvasab,
                                crwidth=self.centerp[0]-30, 
                                crheight=20, 
                                image = self.imagepre,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                crebutton(self.canvasab,
                                crwidth=self.centerp[0]+ 30, 
                                crheight=20, 
                                image = self.imagenext,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

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
                                        
                self.centerp = self.coord.centerpoinparent()
                sepk = self.coord.pointstartendk()
                ct2p = self.coord.centertowpointk()

                # create dim for h 
                height_p  = self.height - self.w_front - self.w_back
                drh = dimrec (cavas=self.canvasaa,
                                locationarrow=sepk,
                                locationtext=ct2p,
                                text= str(height_p),
                                angle= 90)
                # arrow
                drh.createarrow()
                #text 
                drh.createtext()
                # create dim for W 
                width_p = self.width - self.w_left - self.w_right
                self.coord.rev_direction = "top"
                coordse = self.coord.pointstartendk()
                ct2p = self.coord.centertowpointk()
                drw = dimrec (cavas=self.canvasaa,
                                locationarrow=coordse,
                                locationtext=ct2p,
                                text= str(width_p)
                                )
                # arrow
                drw.createarrow()
                #text 
                drw.createtext()
                #dim for top
                #caculate for area 
                writetext(canvas=self.canvasaa,
                                topleftkid=self.topleftkid,
                                toprightkid= self.toprightkid,
                                centerpoint = self.coord.centerpointkid()).warea()
                # create direction nwse
                
                nsew = directnmwe(canvasb = self.canvasaa,
                                height = self.height- self.w_front - self.w_back, 
                                width = self.width - self.w_left - self.w_right,
                                dis_direc = 600, 
                                leftpoint= self.topleftkid, 
                                rightpoint=self.toprightkid)
                nsew.nsew(font = ('times', 16),
                                fill = "black")
                
                self.value_dis = nsew.revalue_dis()

        def createrectang_area(self,topleftpoint = None, 
                                toprightpoint = None, 
                                fill = "yellow",
                                alpha=0.5 ):
                """ create rectangle of area """
                self.rrectangle_wd = self.canvasaa.create_rectangle (*topleftpoint,
                                                                        *toprightpoint,
                                                                        fill=fill)
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

        def createreck (self,**kwargs):
                """Create rectangle of widget kid"""
                try:

                        self.canvasaa.delete(self.rrectangle_kid ) # remove
                except:

                        pass

                self.rrectangle_kid = self.canvasaa.create_rectangle (*self.topleftkid,
                                                                        *self.toprightkid,
                                                                        fill="#e79c2b")
