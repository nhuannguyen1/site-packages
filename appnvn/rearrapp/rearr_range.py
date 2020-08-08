import xlwings as xw 
from tkinter import messagebox
from pynvn import dict_from_csv2col
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.copy_move_paste import co_paste_move_range
from pynvn.excel import activesheet,open_wb_byxl,listsheet_by_wb
from pynvn import dict_from_csv2col
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
                        sheet_name = self.__dictconf["sub_sheetname"]
                        range_copy = self.__dictconf["sub_range_copy"]
                        range_des = self.__dictconf["sub_range_des"]
                        if mrange == "yes":
                            if sheet_name == "active":
                                ac_sheet = wb.sheets.active
                                co_paste_move_range(sheet_copy=ac_sheet,
                                                    sheet_des=ac_sheet,
                                                    range_copy=range_copy,
                                                    range_paste=range_des,
                                                    clear_rcopy_after_copy=true
                                                    )
                            else:
                                for sheetname in listsheet_by_wb(wb):
                                    if sheet_name in sheetname:
                                        wsheet = wb.sheets[sheetname]
                                        co_paste_move_range(sheet_copy=wsheet,
                                                            range_copy=range_copy,
                                                            sheet_des=wsheet,
                                                            range_paste=range_des,
                                                            clear_rcopy_after_copy=True
                                                            )
                            
                            """
                            else:
                                messagebox.showerror("Error","recheck name key {0} in directory {1}".format("sub_sheetname",self.__pathconf))
                            """
                        
                wb.save()
                wb.app.quit()       
