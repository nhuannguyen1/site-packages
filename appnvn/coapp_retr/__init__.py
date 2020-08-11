from pynvn.csv.todict import dict_str_fromlist
from pynvn.excel import (sheet_by_namesheet,
                        activesheet)
import xlwings as xw
from tkinter import messagebox
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.write import hvalues_in_cell,hrangesheet
from pynvn.excel import col2num,book_by_path
from appnvn.coapp_retr.copyrange import cpfromtem
class rapp:
    """ fill the formulas into excel file """
    def __init__(self, retr_path = None,
                        retr_sheetname =None, 
                        fuction = None,
                        pathconf = None,
                        path_exell_tem = None
                        ):
        self.__dictconf = dict_str_fromlist(path=pathconf)
        self.__path_exell_tem = path_exell_tem
        self.__retr_sheetname = retr_sheetname
        self.__fuction = str(fuction).lower()

        if retr_sheetname == "Active Sheet":
            self.__ws_retr = activesheet()
            print (self.__ws_retr)
        else:
            self.__ws_retr = sheet_by_namesheet(path=retr_path,
                                                namesheet=retr_sheetname)
    def ft_tool(self):
        lfuns = filterlistbylstr(liststr=list(self.__dictconf.keys()),
                                            criteria_is_not=True,
                                            criteria=["sub_"],
                                            upper = False
                                            ) 
        
        mydictfun = {
                    "copy_from_tem":(lambda: self.__copy_from_tem()),
                    }        
        
        if self.__fuction == "config":

            for lfun in lfuns:

                mydictfun[lfun]()
        else:
             mydictfun[self.__fuction]()

    def __copy_from_tem(self):
        mrange = self.__dictconf["copy_from_tem"]
        startcopyrange = self.__dictconf["sub_copy_from_tem_startcopyrange"]
        startpasterange = self.__dictconf["sub_copy_from_tem_startpasterange"]
        namesheet_tem = self.__dictconf["sub_copy_from_tem_namesheet_tem"]
        print (startcopyrange,startpasterange,namesheet_tem)
        self.wb_tem =book_by_path(path=self.__path_exell_tem,
                                        namesheet=namesheet_tem,visible = False)
        
        cpfromtem(range_copy=range_copy,
                    range_paste=range_des,
                    clear_rcopy_after_copy=False,
                    ws_des=self.__ws_retr,
                    ws_tem=self.wb_tem,
                    usinglocinexcel=False,
                    ) if mrange == "yes" else False