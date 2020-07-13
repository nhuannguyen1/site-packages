from tkinter import messagebox
from pynvn.path.ppath import getdirpath,refullpath,ExtractFileNameFromPath
from pynvn.excel import col2num,colnum_string, repathlinkexcel,relistsheet,delrowbyindexcell
import xlwings as xw 
from pynvn.csv.rcsv import returndictrowforcsv
from appnvn.exazp.excel.itemhm import azb10,azb30
from pynvn.string.slist import returnseplistintbbystr,str_seplistintbbystr,returnlist_from_listinstr
from pynvn.list.flist import pairlistandlist
from pynvn.string.slist import str_returnliststr
from pynvn.excel.openpyxl import returnloccellbyvalue
from pynvn.excel import cellcoordbyvalue,lcellindexbyvalue
from pynvn.list import pairiterationlist
from pynvn.excel.copypasteexell import cprangesamesheet
from appnvn.exazp.excel.hchildsheet import hchildsheet
class cexcel:
    """copy excel to excel"""
    def __init__(self,
                    pathconf = None,
                    pathdes= None, 
                    pathtocopy= None,
                ):
        # call dict 
        dictconf = returndictrowforcsv(path=pathconf)
        # return list sheet excel to handling 
        self.__pathdes = pathdes
        self.__pathtocopy = pathtocopy
        self.__app = xw.App(visible=False)
        self.__desxw = xw.Book(pathdes)
        self.__copyxw = xw.Book(pathtocopy)
        self.wsnames = self.__copyxw.sheets
        for namesheet in self.wsnames:
            if "AZB" in namesheet.name:
                self.ws1 = namesheet
                break
        #max row ws1
        self.rows = self.ws1.api.UsedRange.Rows.count
        #max colum ws1
        self.cols = self.ws1.api.UsedRange.Columns.count
        self.colunsande = [colnum_string(1),colnum_string(self.cols)]
        # azb10
        listsheetex = dictconf["listsheetnamechild"].replace(":", ",")
        listsheetex = str_returnliststr(listsheetex)

        zab10_recor_l = dictconf["zab10_recor_l1"]
        self.__zab10_recor_l_lint = returnseplistintbbystr(zab10_recor_l)
        # return list value key ms
        zab10_valueim = dictconf["zab10_valueim"].replace(":", ",")
        self.__zab10_valueim = returnlist_from_listinstr(zab10_valueim)

        zab10_valuehavechild = dictconf["zab10_valuehavechild"].replace(":", ",")
        self._zab10_valuehavechild = returnlist_from_listinstr(zab10_valuehavechild)
        # ms azb10
        self.__azb10_msstr =dictconf["azb10_ms"]

        zab10_forbydup =dictconf["zab10_forbydup"].replace(":", ",")
        self.__zab10_forbydup = returnlist_from_listinstr(zab10_forbydup)
        
        self.__azb10_mssint =col2num(dictconf["azb10_ms"]) 
        zab10_locuseformulas = dictconf["zab10_locuseformulas"].replace(":", ",")
        self.__zab10_locuseformulas = returnlist_from_listinstr(zab10_locuseformulas)
        zab10_dup = dictconf["zab10_dup"].replace(":", ",")
        self.__zab10_dup = returnlist_from_listinstr(zab10_dup)
        self.__namesheet = self.ws1.name
        # check name sheet name 
        if self.__namesheet not in listsheetex:
            messagebox.showerror("error", "name sheet {0} of workbook{1} not valid, its name is AZB-NN".format(self.__namesheet,pathtocopy))
    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        # get dir path 
        dirpath = getdirpath(self.__pathtocopy)
        # get extract file name from path 
        namefile = ExtractFileNameFromPath(self.__pathtocopy)
        pfile = repathlinkexcel(dpath=dirpath,
                                namefile=namefile,
                                namesheet=self.__namesheet)
        sheet_des = self.__desxw.sheets[self.__namesheet]
        sheet_copy = self.__copyxw.sheets[self.__namesheet]
        if self.__namesheet == "AZB-10":
            # max row sheet des
            self.m_row = sheet_des.range(self.__azb10_msstr + str(sheet_des.cells.last_cell.row)).end('up').row
            hchildsheet(startrow=self.__zab10_recor_l_lint[0],
                        col_key_msa=self.__azb10_msstr,
                        pfile=pfile,
                        columnlra=self.colunsande,
                        max_row=self.m_row,
                        lcolumnformulas = self.__zab10_locuseformulas,
                        valueim=self.__zab10_valueim,
                        sheet_des =sheet_des,
                        sheet_copy=sheet_copy,
                        col_dup=self.__zab10_dup,
                        max_row_allsheet=self.rows,
                        lvaluehavechild=self._zab10_valuehavechild,
                        formulasfor_col_dup = self.__zab10_forbydup )
        self.__copyxw.close()
        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()