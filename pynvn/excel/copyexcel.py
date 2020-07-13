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
        self.dictconf = returndictrowforcsv(path=pathconf)
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
        # list sheet name 
        listsheetex = str_returnliststr(self.dictconf["listsheetnamechild"].replace(":", ","))
        # name sheet 
        self.__namesheet = self.ws1.name
        # check name sheet name 
        if self.__namesheet not in listsheetex:
            messagebox.showerror("error", "name sheet {0} of workbook{1} not valid, its \
                                    name is AZB-NN".format(self.__namesheet,pathtocopy))
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
            recor_l_lint = int(self.dictconf["zab10_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab10_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab10_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb10_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab10_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab10_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab10_dup"].replace(":", ","))
            # max row sheet des
            self.m_row = sheet_des.range(msstr + str(sheet_des.cells.last_cell.row)).end('up').row
            hchild = hchildsheet(startrow=recor_l_lint,
                        col_key_msa=msstr,
                        pfile=pfile,
                        columnlra=self.colunsande,
                        max_row=self.m_row,
                        lcolumnformulas = locuseformulas,
                        valueim=valueim,
                        sheet_des =sheet_des,
                        sheet_copy=sheet_copy,
                        col_dup=col_dup,
                        max_row_allsheet=self.rows,
                        lvaluehavechild=valuehavechild,
                        formulasfor_col_dup = forbydup)
            # copy formulas to another sheet 
            hchild.tranderdatasheettosheet()
            # keep value at msp
            hchild.returnvaluekeyim()
            # change value at col index
            hchild.hdataatdupcolumn()
        if self.__namesheet == "AZB-30":
            recor_l_lint = int(self.dictconf["zab30_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab30_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab30_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb30_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab30_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab30_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab30_dup"].replace(":", ","))
            # max row sheet des
            self.m_row = sheet_des.range(msstr + str(sheet_des.cells.last_cell.row)).end('up').row
            hchild = hchildsheet(startrow=recor_l_lint,
                            col_key_msa=msstr,
                            pfile=pfile,
                            columnlra=self.colunsande,
                            max_row=self.m_row,
                            lcolumnformulas = locuseformulas,
                            valueim=valueim,
                            sheet_des =sheet_des,
                            sheet_copy=sheet_copy,
                            col_dup=col_dup,
                            max_row_allsheet=self.rows,
                            lvaluehavechild=valuehavechild,
                            formulasfor_col_dup = forbydup)
            # copy formulas to another sheet 
            hchild.tranderdatasheettosheet()
        self.__copyxw.close()
        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()