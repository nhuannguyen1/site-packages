import xlwings as xw 
from pynvn import dict_from_csv2col
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.copy_move_paste import co_paste_move_range
from pynvn.excel import activesheet
class rearr_range:
    def __init__(self,lpath_excel =[],
                pathconf = None
                ):
        self.lpath_excel = lpath_excel
        self.dictconf = dict_from_csv2col(pathconf)

        lfuns = filterlistbylstr(liststr=list(self.dictconf.keys()),
                                            criteria_is_not=True,
                                            criteria=["sub_"],
                                            upper = False
                                            )
    
    def move_range(self):
        if self.__fuction == "config":
            for lfun in lfuns:
                # remove  space 
                if lfun == "move_range":
                    mrange = self.dictconf["move_range"]
                    Value_Conf_Loc = self.dictconf["sub_move_range_value_conf_Loc"]
                    sheet_name = self.dictconf["sub_sheetname"]
                    range_copy = self.dictconf["sub_range_copy"]
                    range_des = self.dictconf["sub_range_des"]
                    if mrange =="yes":
                        if sheet_name == "active":
                            acsheet = activesheet()
                            co_paste_move_range(sheet_copy=acsheet,
                                            sheet_des=acsheet
                                            )
        

