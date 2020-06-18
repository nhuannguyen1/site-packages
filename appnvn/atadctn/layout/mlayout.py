import tkinter as tk # python 3
from appnvn.atadctn.treectn import scbg
from appnvn.atadctn.icontt import gui
from appnvn.atadctn.treectn import scrollbarvn
from pynvn.checklb.checkb import ChecklistBox
class mlayout(tk.Tk):
    """ config layout, add layout more from input user """
    def __init__(self, 
                    tktk = None,
                    pathicon =None,
                    *args,
                    labelfont = ('times', 20),
                    labelfont_sm = ('times', 16),
                    labelfont_botton = ('times', 11), 
                    pathclayout = None,
                    namequotation = "quotation.xlsx",
                    **kwargs):
       
        self.__tktk = tktk
        self.__labelfont = labelfont
        self.__labelfont_sm = labelfont_sm
        self.__pathclayout = pathclayout
        self.__labelfont_botton = labelfont_botton
        self.__filewin = tk.Toplevel(self.__tktk)
        self.__namequotation = namequotation
        gui (tktk=self.__filewin,
            pathico=pathicon,
            width=800,
            height=800,
            widthx="center",
            widthy="center",
            resizable=[True,True],
            condv=2.7
            )\
            .setcfbs()
        self.sc  = scbg(parent = self.__filewin,
                        cavheight=600,
                        cavwidth=600,
                        isonlyaframe= False,
                        bg = "#e6ecf5",
                        bgpr = "#5b9bd5",
                        framea = [0,0,470,120,"#e6ecf5"],
                        frameb = [0,120,470,100,"white"],
                        framec = [0,240,470,150,"#e6ecf5"]
                        )
        self.framea = self.sc.framea
        self.frameb = self.sc.frameb
        self.framec = self.sc.framec

        try: 
            self.scf.destroy()
        except:
            pass
        self.scf = scrollbarvn(parent=self.frameb,
                                bg = "white")
        self.scframe = self.scf.frame

        self.cb = ChecklistBox(parent=self.scframe,
                                width= 123,listsheetname=[""]
                                )

        self.__creategui()
    def __creategui(self):
        """ create to input size layout """
        sltt = tk.Label(self.framea,
                        text = "All layout of Container House",
                        font=self.__labelfont,
                        bg = "white",
                        )
        sltt.grid(column = 1, 
                        row = 0,
                        pady = 10,
                        sticky  = tk.W
                        )
        


