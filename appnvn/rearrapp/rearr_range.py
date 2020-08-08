import xlwings as xw 
from tkinter import messagebox
from pynvn import dict_from_csv2col
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.copy_move_paste import co_paste_move_range
from pynvn.excel import activesheet,open_wb_byxl,listsheet_by_wb
from pynvn import dict_from_csv2col
from appnvn.rearrapp.mrange import hsheet_range
class rearr_range:
    def __init__(self,lpath_excel =[],
                pathconf = None,
                fuction = None
                ):
        self.__lpath_excel = lpath_excel
        self.__fuction = fuction
        self.__pathconf = pathconf
        self.__dictconf = dict_from_csv2col(pathconf)
        self.lfuns = filterlistbylstr(liststr=list(self.__dictconf.keys()),
                                            criteria_is_not=True,
                                            criteria=["sub_"],
                                            upper = False
                                            )
                                            
    def mrange(self):
        if self.__fuction == "config":
            for lexel in self.__lpath_excel:
                self.wb = open_wb_byxl(lexel)
                for lfun in self.lfuns:
                    if lfun == "move_range":
                        self.__move_range()
                    elif lfun == "mrange_by_cell":
                        self.__mrange_by_cell()
            
        self.wb.save()
        self.wb.app.quit()       

    def __move_range(self):
        mrange = self.__dictconf["move_range"]
        sheet_name = self.__dictconf["sub_move_range_sheetname"]
        range_copy = self.__dictconf["sub_move_range_range_copy"]
        range_des = self.__dictconf["sub_move_range_range_des"]
        hsheet_range(sheet_name=sheet_name,
                    wb=self.wb,
                    range_copy=range_copy,
                    range_paste=range_des,
                    clear_rcopy_after_copy=True
                    ) if mrange == "yes" else False                   
    def __mrange_by_cell(self):
        mrange = self.__dictconf["mrange_by_cell"]
        sheet_name= self.__dictconf["sub_mrange_by_cell_sheetname"]
        range_copy = self.__dictconf["sub_mrange_by_cell_loc_range_copy"]
        range_des = self.__dictconf["sub_mrange_by_cell_loc_range_des"]
        hsheet_range(sheet_name=sheet_name,
                    wb=self.wb,
                    range_copy=range_copy,
                    range_paste=range_des,
                    clear_rcopy_after_copy=True,
                    usinglocinexcel=True
                    ) if mrange == "yes" else False