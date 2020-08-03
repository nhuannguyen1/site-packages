from pynvn.excel import col2num,colnum_string, repathlinkexcel
from pynvn.csv.todict import returndictrowforcsv
from pynvn.excel import (sheet_by_namesheet,
                        activeworkbook_fullname,
                        activesheet_name,
                        activesheet)
import xlwings as xw
from tkinter import messagebox
from pynvn.string import removespace
class sapp:
    """ fill the formulas into excel file """
    def __init__(self, retr_path = None,
                        retr_sheetname =None, 
                        des_path = None,
                        des_sheetname =None,
                        fuction = None,
                        pathconf = None,
                        ):
        self.dictconf = returndictrowforcsv(path=pathconf)
        self.__retr_sheetname = retr_sheetname
        self.__des_path = des_path
        self.__des_sheetname = des_sheetname
        self.__fuction = fuction

        if retr_sheetname == "Active Sheet":
            retr_path = activeworkbook_fullname()
            retr_sheetname = activesheet_name()

        self.__pexcelretr = repathlinkexcel(usingfullname=True,
                                            fullname=retr_path,
                                            namesheet=retr_sheetname
                                            )
        if des_sheetname == "Active Sheet":
            self.__ws_des = activesheet()
        else:
            self.__ws_des = sheet_by_namesheet(path=des_path,
                                                namesheet=des_sheetname)
    def ft_tool(self):
        if self.__fuction == "config":


