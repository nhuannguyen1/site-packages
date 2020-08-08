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
    
    def move_range(self):
        if self.__fuction == "config":
            for lexel in self.__lpath_excel:
                wb = open_wb_byxl(lexel)
                for lfun in self.lfuns:
                    if lfun == "move_range":
                        mrange = self.__dictconf["move_range"]
                        Value_Conf_Loc = self.__dictconf["sub_move_range_value_conf_loc"]
                        sheet_name = self.__dictconf["sub_move_range_sheetname"]
                        range_copy = self.__dictconf["sub_move_range_range_copy"]
                        range_des = self.__dictconf["sub_move_range_range_des"]
                        hsheet_range(sheet_name=sheet_name,wb=wb) if mrange == "yes" else False
                    elif lfun == "mrange_by_cell":
                        sheet_name= self.__dictconf["sub_mrange_by_cell_sheetname"]
                        range_copy = self.__dictconf["sub_mrange_by_cell_loc_range_copy"]
                        range_des = self.__dictconf["sub_move_range_range_des"]
                        
                wb.save()
                wb.app.quit()       
