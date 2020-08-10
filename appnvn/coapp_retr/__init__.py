from pynvn.csv.todict import dict_str_fromlist
from pynvn.excel import (sheet_by_namesheet,
                        activesheet)
import xlwings as xw
from tkinter import messagebox
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.write import hvalues_in_cell,hrangesheet
from pynvn.excel import col2num
class rapp:
    """ fill the formulas into excel file """
    def __init__(self, retr_path = None,
                        retr_sheetname =None, 
                        fuction = None,
                        pathconf = None,
                        ):
        self.dictconf = dict_str_fromlist(path=pathconf)
        self.__retr_sheetname = retr_sheetname
        self.__fuction = str(fuction).lower()

        if retr_sheetname == "Active Sheet":
            self.__ws_retr = activesheet()
        else:
            self.__ws_retr = sheet_by_namesheet(path=retr_path,
                                                namesheet=retr_sheetname)
    def ft_tool(self):
        lfuns = filterlistbylstr(liststr=list(self.dictconf.keys()),
                                            criteria_is_not=True,
                                            criteria=["sub_"],
                                            upper = False
                                            ) 
        
        mydictfun = {
                    "copyfromtem":(lambda: self.__copyfromtem()),
                    }        
        
        if self.__fuction == "config":

            for lfun in lfuns:

                mydictfun[lfun]()
        else:
             mydictfun[self.__fuction]()

    def __copyfromtem(self):
        cyesornot = self.dictconf["copyfromtem"]
        startcopyrange = self.dictconf["sub_copyfromtem_startcopyrange"]
        startpasterange = self.dictconf["sub_copyfromtem_startpasterange"]
        hrangesheet(rmrange=rmrange,
                    ws=self.__ws_retr,
                    option_fun="copyfromtem",
                    feature_fun="copyfromtem",
                    value_to_end=None,
                    valuetodelete=valuetodel,
                    using_value_to_end=False
                    ) if cyesornot[0] =="yes" else False  

def noneinlist_str(n):
    """ Evel str "None" None """
    return eval(n) if n=="None" else n
