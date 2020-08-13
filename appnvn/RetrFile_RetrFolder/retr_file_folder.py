from pynvn.csv.todict import dict_str_fromlist,dictfromcsv2col_evallist
from pynvn.excel import sheet_by_namesheet,activesheet,listsheet_by_wb
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.write import hvalues_in_cell,hrangesheet
from pynvn.excel import ws_by_namesheet,open_wb_by_xl,col2num,colnum_string, repathlinkexcel,cprange_2wb
from pynvn.path.ppath import (refullpath,
                            listfileinfolder
                            )
from pynvn.checklb.checkb import ChecklistBox
from pynvn.excel.copyexcel import cexcel
from tkinter import messagebox
from appnvn.exazp.excel.hchildsheet import hchildsheet
from pynvn.path.ppath import getdirpath,ExtractFileNameFromPath
import xlwings as xw
class rapp:
    """ fill the formulas into excel file """
    def __init__(self,path_des = None,
                    path_copy_dir = None,
                    fuction = None,
                    pathconf = None,
                    lsheet_ex = []
                    ):

        self.__path_copy_dir = path_copy_dir
        self.__lsheet_ex = lsheet_ex
        self.__dictconf = dictfromcsv2col_evallist(path=pathconf)
        self.__fuction = str(fuction).lower()         
        self.__app = xw.App(visible=True,
                            add_book=False
                            )
        self.__desxw = self.__app.books.open(fullname=path_des,
                                            update_links=False)

    def ft_tool(self):
        lfuns = filterlistbylstr(liststr=list(self.__dictconf.keys()),
                                criteria_is_not=True,
                                criteria=["sub_"],
                                upper = False
                                )
        mydictfun = {
                    "transfertoparent":(lambda: self.__transfertoparent()),
                    "transfertoparents":(lambda: self.__transfertoparents())

                    }        
        if self.__fuction == "config":
            for lfun in lfuns:
                mydictfun[lfun]()
        else:
             mydictfun[self.__fuction]()


    def __transfertoparent(self):
        lsheet =  self.__dictconf["listsheetname"]
        for name_ele_ex in self.__lsheet_ex:
            path_copy = refullpath(dirpath=self.__path_copy_dir,
                                            filename = name_ele_ex
                                            )
            copyxw = self.__app.books.open(fullname=path_copy ,
                                            update_links=False,                       
                                            read_only=False,
                                            ignore_read_only_recommended=False
                                            )
            ws_copy = retrive_sname_sheet(copyxw=copyxw,
                                        desxw=self.__desxw,
                                        lsheet=lsheet
                                        )
            continue if ws_copy ==None
            yerorno = self.__dictconf["transfertoparent"]
            recor_l_lint = int(self.__dictconf["sub_transfertoparent_recor_l1"])
            valueim = self.__dictconf["sub_transfertoparent_valueim"]
            valuehavechild = self.__dictconf["sub_transfertoparent_valuehavechild"]
            msstr =self.__dictconf["sub_transfertoparent_ms"]
            forbydup = self.__dictconf["sub_transfertoparent_forbydup"]
            locuseformulas = self.__dictconf["sub_transfertoparent_locuseformulas"]
            col_dup = self.__dictconf["sub_transfertoparent_dup"]
            # retrive sheet des and active
            self.__desxw.sheets[ws_copy.name].activate()
            hchildsheet(startrow=recor_l_lint,
                        col_key_msa=msstr,
                        max_row=m_row,
                        lcolumnformulas = locuseformulas,
                        valueim=valueim,
                        sheet_des =activesheet(),
                        sheet_copy=ws_copy,
                        col_dup=col_dup,
                        lvaluehavechild=valuehavechild,
                        formulasfor_col_dup = forbydup
                        ) if yerorno == "yes" else False
            copyxw.close()
            
        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()            

    def __transfertoparents(self):
        for name_ele_ex in self.__lsheet_ex:
            path_copy = refullpath(dirpath=self.__path_copy_dir,
                                    filename = name_ele_ex
                                    )

            copyxw = self.__app.books.open(fullname=path_copy ,
                                            update_links=False,                       
                                            read_only=False,
                                            ignore_read_only_recommended=False
                                            )

            ws_copy = retrive_sname_sheet(copyxw=copyxw,
                                        desxw=self.__desxw,
                                        lsheet=lsheet
                                        )

            continue if ws_copy ==None
            # column start and column end 
            col_start_end = [colnum_string(1),
                            colnum_string(ws_copy.api.UsedRange.Columns.count)]

            # retrive path link using for formulas 
            pfile = repathlinkexcel(dpath=self.__path_copy_dir,
                                    namefile=name_ele_ex,
                                    namesheet=ws_copy.name
                                    )

            yerorno = self.__dictconf["transfertoparent"]
            recor_l_lint = int(self.__dictconf["sub_transfertoparent_recor_l1"])
            valueim = self.__dictconf["sub_transfertoparent_valueim"]
            valuehavechild = self.__dictconf["sub_transfertoparent_valuehavechild"]
            msstr =self.__dictconf["sub_transfertoparent_ms"]
            forbydup = self.__dictconf["sub_transfertoparent_forbydup"]
            locuseformulas = self.__dictconf["sub_transfertoparent_locuseformulas"]
            col_dup = self.__dictconf["sub_transfertoparent_dup"]
            # retrive sheet des and active

            self.__desxw.sheets[ws_copy.name].activate()
            hchildsheet(startrow=recor_l_lint,
                        col_key_msa=msstr,
                        pfile=pfile,
                        columnlra=col_start_end,
                        lcolumnformulas = locuseformulas,
                        valueim=valueim,
                        sheet_des =activesheet(),
                        sheet_copy=ws_copy,
                        col_dup=col_dup,
                        lvaluehavechild=valuehavechild,
                        formulasfor_col_dup = forbydup
                        ) if yerorno == "yes" else False
            copyxw.close()
        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()

def retrive_sname_sheet(copyxw,desxw,lsheet):
    """ retrive sheet copy from sheet copy and sheet des"""
    for sheet in copyxw.sheets:
        if (sheet.name in lsheet and sheet.name in listsheet_by_wb(desxw)) :
            return sheet
            break
