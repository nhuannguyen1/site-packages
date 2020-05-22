from tkinter import (Frame,
                    Tk,
                    ttk,
                    messagebox,
                    PhotoImage
                    )
import tkinter as tk
from appnvn.atadctn.treectn import scbg,cvframeg
from pynvn.caculate.cacul_cavas import placereccenter

import re
from PIL import ImageTk
from pynvn.caculate.ratio import ratio

from pynvn.caculate.coord_point import coordp

from pynvn.caculate.area import area

from pynvn.cavas_drawing.buttondr import crebutton
from pynvn.cavaszm.cavaszm import zmcv
import string

from pynvn.nsew.nsew import directnmwe

from pynvn.cavas_write.writetext import writetext

from pynvn.cavas_dim.cavas_dim import dimrec

from pynvn.cavas_drawing.draw import dcavas

from pynvn.iter import bidirectional_iterator

import os

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
                self.frameaa = [40,0,670,700,"azure"]
                self.frameab = [0,700,750,50,"azure"]
                self.frameac = [0,0,40,700,"azure"]
                self.framead = [710,0,40,700,"azure"]

                pathimage = r"D:\5.ATADRD\CTNATAD\clayout"
                os.chdir(pathimage)
                self.imgs = os.listdir(pathimage)
                self.bd = bidirectional_iterator(self.imgs)
                
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
                                command = lambda: self.pre_img(),
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                # cavas d
                self.canvasad =  self.sc.canvasd

                crebutton(self.canvasad,
                                crwidth=self.framead[2]/2, 
                                crheight=self.framead[3]/2, 
                                image = self.imagenextlayout,
                                bg = "azure",
                                command = lambda: self.next_img(),
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                self.pattern = re.compile("[0-9]")
                # create frawing  
                self.createdrawing()

                # create buttom previuos
                crebutton(self.canvasab,
                                crwidth=self.frameb[2]/2-30, 
                                crheight=20, 
                                image = self.imagepre,
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)

                # create buttom next
                crebutton(self.canvasab,
                                crwidth=self.frameb[2]/2+ 30, 
                                crheight=20, 
                                image = self.imagenext,
                                command = lambda: self.next_img(),
                                bg = "azure",
                                activebackground = "#33B5E5",
                                relief = tk.FLAT)
                self.next_img()


        def createdrawing (self, colorroad = "#c49b65",*args,**kwargs):
                """Drawing layout follow customer"""
                # create dim for h 
                height_p  = self.height - self.w_front - self.w_back
                width_p = self.width - self.w_left - self.w_right

                plc = placereccenter(info_height_k= height_p,
                                        info_width_k= width_p,
                                        info_width_P =self.frameaa[2],
                                        info_height_p=self.frameaa[3]
                                        )
                
                # top left
                self.leftpoint = plc.pointleftrec()
                # top right
                self.rightpoint = plc.pointrightrec()
                self.centerp = plc.pointcenterofparent()

                dcavas(cavas=self.canvasaa,
                        topp=self.leftpoint,
                        bottomp=self.rightpoint).drec(fill = "#c49b65")
                # dim for item all
                self.coord = coordp(topleftp=self.leftpoint,
                                        bottomrightp=self.rightpoint,
                                        rev_direction="left",
                                        dis_dim=self.dis_dim)

                self.centerp = self.coord.centerpoinparent()
                sepk = self.coord.pointstartend()
                ct2p = self.coord.centertowpoint()

                # create rectangle 
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
                self.coord.rev_direction = "top"
                coordse = self.coord.pointstartend()
                ct2p = self.coord.centertowpoint()
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
                                topleftkid=self.leftpoint,
                                toprightkid= self.rightpoint,
                                centerpoint = self.centerp).warea()
                # create direction nwse
                nsew = directnmwe(canvasb = self.canvasaa,
                                height = self.height- self.w_front - self.w_back, 
                                width = self.width - self.w_left - self.w_right,
                                dis_direc = self.dis_direc * 2.3, 
                                leftpoint= self.leftpoint, 
                                rightpoint=self.rightpoint)
                nsew.nsew(font = ('times', 16),
                                fill = "black")
                self.value_dis = nsew.revalue_dis()
        def next_img(self):
                """ next value """
                self.createdrawing()
                #bd = bidirectional_iterator(self.imgs)
                self.fileimage=self.bd.next()
                zmcv(cavas=self.canvasaa,
                                isimage=True,
                                centerp=self.centerp,
                                imagepath=self.fileimage,
                                frameb=self.frameaa,
                                value_dis=self.value_dis
                                )

        def pre_img(self):
                """ previous value """
                self.createdrawing()
                self.fileimage=self.bd.prev()
                zmcv(cavas=self.canvasaa,
                                isimage=True,
                                centerp=self.centerp,
                                imagepath=self.fileimage,
                                frameb=self.frameaa,
                                value_dis=self.value_dis
                                )

