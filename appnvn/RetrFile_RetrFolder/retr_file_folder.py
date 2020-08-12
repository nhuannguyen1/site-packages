from pynvn.csv.todict import dict_str_fromlist,dictfromcsv2col_evallist
from pynvn.excel import sheet_by_namesheet,activesheet,listsheet_by_wb
from pynvn.list.flist import filterlistbylstr
from pynvn.excel.write import hvalues_in_cell,hrangesheet
from pynvn.excel import col2num,ws_by_namesheet,open_wb_by_xl
from pynvn.excel.copy_move_paste import cprange_2wb
from pynvn.path.ppath import (refullpath,
                            listfileinfolder
                            )

from pynvn.checklb.checkb import ChecklistBox
from pynvn.excel.copyexcel import cexcel
from tkinter import messagebox
from appnvn.exazp.excel.hchildsheet import hchildsheet
from pynvn.excel import col2num,colnum_string, repathlinkexcel
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
        self.__dictconf = dictfromcsv2col_evallist(path=pathconf)
        self.__fuction = str(fuction).lower()         
        self.__app = xw.App(visible=True,
                            add_book=False
                            )
        self.__desxw = self.__app.books.open(fullname=path_des,
                                            update_links=False)
        # list sheet of des workbook
        lsheet_des = listsheet_by_wb(self.__desxw)
        # retrive list sheet name  excel tranfer
        lsheet =  self.__dictconf["listsheetname"]
        self.ws_copy  = None
        for eleexcell in lsheet_ex:
            self.__path_copy = refullpath(dirpath=path_copy_dir,
                                            filename = eleexcell
                                            )
            self.__copyxw = self.__app.books.open(fullname=self.__path_copy ,
                                                    update_links=False,                       
                                                    read_only=False,
                                                    ignore_read_only_recommended=False
                                                    )
            self.wsnames = self.__copyxw.sheets
            for namesheet in self.wsnames:
                if (namesheet.name in lsheet and namesheet.name in lsheet_des) :
                    self.ws_copy = namesheet
                    #max row ws1
                    self.rows = self.ws_copy.api.UsedRange.Rows.count
                    #max colum ws1
                    self.cols = self.ws_copy.api.UsedRange.Columns.count
                    self.colunsande = [colnum_string(1),colnum_string(self.cols)]
                    break
            self.ft_tool() if self.ws_copy else  messagebox.showerror ("Error name sheet", 
                                                                        "None of Sheet are compatible,\
                                                                             recheck sheet name of wb {0}".format(self.__path_copy))

        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()


    def ft_tool(self):

        lfuns = filterlistbylstr(liststr=list(self.__dictconf.keys()),
                                criteria_is_not=True,
                                criteria=["sub_"],
                                upper = False
                                )
        mydictfun = {
                    "transfertoparent":(lambda: self.__transfertoparent()),
                    }        
        if self.__fuction == "config":
            for lfun in lfuns:
                mydictfun[lfun]()
        else:
             mydictfun[self.__fuction]()

    def __transfertoparent(self):
        # retrive sheet des
        self.__desxw.sheets[self.ws_copy.name].activate()
        sheet_des = activesheet()
        # retrive dir path or path to copy
        dirpath = getdirpath(self.__path_copy)
        # get extract file name from path 
        namefile = ExtractFileNameFromPath(self.__path_copy)
        pfile = repathlinkexcel(dpath=dirpath,
                                namefile=namefile,
                                namesheet=self.ws_copy.name)
        yerorno = self.__dictconf["transfertoparent"]
        recor_l_lint = int(self.__dictconf["sub_transfertoparent_recor_l1"])
        valueim = self.__dictconf["sub_transfertoparent_valueim"]
        valuehavechild = self.__dictconf["sub_transfertoparent_valuehavechild"]
        msstr =self.__dictconf["sub_transfertoparent_ms"]
        forbydup = self.__dictconf["sub_transfertoparent_forbydup"]
        locuseformulas = self.__dictconf["sub_transfertoparent_locuseformulas"]
        col_dup = self.__dictconf["sub_transfertoparent_dup"]
        # max row sheet des
        m_row = sheet_des.range(msstr + str(sheet_des.cells.last_cell.row)).end('up').row
        hchildsheet(startrow=recor_l_lint,
                    col_key_msa=msstr,
                    pfile=pfile,
                    columnlra=self.colunsande,
                    max_row=m_row,
                    lcolumnformulas = locuseformulas,
                    valueim=valueim,
                    sheet_des =sheet_des,
                    sheet_copy=self.ws_copy,
                    col_dup=col_dup,
                    max_row_allsheet=self.rows,
                    lvaluehavechild=valuehavechild,
                    formulasfor_col_dup = forbydup
                    ) if yerorno == "yes" else False
        self.__copyxw.close()

    def __transfertoparents(self):
        # retrive sheet des
        self.__desxw.sheets[self.ws_copy.name].activate()
        sheet_des = activesheet()
        # retrive dir path or path to copy
        dirpath = getdirpath(self.__path_copy)
        # retrive extract file name from path 
        namefile = ExtractFileNameFromPath(self.__path_copy)
        pfile = repathlinkexcel(dpath=dirpath,
                                namefile=namefile,
                                namesheet=self.ws_copy.name
                                )

        # max row sheet des
        m_row = sheet_des.range(msstr + str(sheet_des.cells.last_cell.row)).end('up').row
        hchildsheet(startrow=recor_l_lint,
                    col_key_msa=msstr,
                    pfile=pfile,
                    columnlra=self.colunsande,
                    max_row=m_row,
                    lcolumnformulas = locuseformulas,
                    valueim=valueim,
                    sheet_des =sheet_des,
                    sheet_copy=self.ws_copy,
                    col_dup=col_dup,
                    max_row_allsheet=self.rows,
                    lvaluehavechild=valuehavechild,
                    formulasfor_col_dup = forbydup
                    ) if yerorno == "yes" else False
        self.__copyxw.close()