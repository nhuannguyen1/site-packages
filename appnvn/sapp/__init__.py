from pynvn.csv.todict import dict_str_fromlist
from pynvn.excel import (sheet_by_namesheet,
                        activesheet)
import xlwings as xw
from tkinter import messagebox
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.write import hvalues_in_cell
class sapp:
    """ fill the formulas into excel file """
    def __init__(self, retr_path = None,
                        retr_sheetname =None, 
                        fuction = None,
                        pathconf = None,
                        ):
        self.dictconf = dict_str_fromlist(path=pathconf)
        self.__retr_sheetname = retr_sheetname
        self.__fuction = fuction

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
        if self.__fuction == "Config":
            for lfun in lfuns:
                # remove  space 
                if lfun == "removespace":
                    cyesornot = self.dictconf["removespace"]
                    rmrange = self.dictconf["sub_removespace_range"]
                    rmtyle = self.dictconf["sub_removespace_style"]
                    hvalues_in_cell(rmrange=rmrange,
                                    option=rmtyle[0],
                                    ws=self.__ws_retr,option_fun="removespace") if cyesornot[0] =="yes" else False
                elif lfun == "capfs":
                    cyesornot = self.dictconf["removespace"]
                    rmrange = self.dictconf["sub_capfs_range"]
                    hvalues_in_cell(rmrange=rmrange,
                                    ws=self.__ws_retr,
                                    option_fun="capfs") if cyesornot[0] =="yes" else False