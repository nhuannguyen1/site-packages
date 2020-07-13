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

def hchildsheet(startrow = 1,
                col_key_msa = None,
                pfile = None, 
                columnlra = None,
                max_row = 100, 
                max_col = 20, 
                lcolumnformulas = None, 
                valueim = None,
                sheet_des = None,
                sheet_copy = None, 
                col_dup = None,
                lvaluehavechild = None,
                max_row_allsheet= 1000,
                formulasfor_col_dup = None):
    for abccol in lcolumnformulas:
        indexcol = col2num(abccol) -  col2num(col_key_msa)  + 1
        fomularex = "=IFERROR(VLOOKUP({1}{0},{2}!${1}${0}:${4}${6},{7},FALSE),{8})".format(startrow,
                                                                                        col_key_msa,
                                                                                        pfile,
                                                                                        col_key_msa,
                                                                                        columnlra[1],
                                                                                        startrow,
                                                                                        max_row_allsheet,
                                                                                        indexcol,
                                                                                        0
                                                                                        )
        sheet_des.range("{0}{1}".format(abccol,
                                        startrow)).value = fomularex
        vtformulas = sheet_des.range("{0}{1}".format(abccol,
                                                    startrow)).formula
        sheet_des.range("{0}{1}:{0}{2}".format(abccol,
                                                startrow,
                                                max_row)).formula = vtformulas

        for numberint in valueim:
            ms_des = cellcoordbyvalue(max_row=max_row_allsheet,
                                        min_row=1,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_des,
                                        valuetofile=numberint
                                        )
            ms_copy = cellcoordbyvalue(max_row=max_row_allsheet,
                                        min_row=1,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_copy,
                                        valuetofile=numberint)
            sheet_des.range("{0}{1}".format(abccol,
                                            ms_des[0])).value =sheet_copy.range("{0}{1}".format(abccol,
                                                                                                ms_copy[0])).value
    
    for count,eles in enumerate(col_dup,0):
        vtformulas = sheet_des.range("{0}{1}".format(eles,startrow + 1)).formula
        lindexrow = lcellindexbyvalue(max_row=max_row_allsheet,
                                        min_row=startrow,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_des,
                                        lvalue=lvaluehavechild
                                        )
        for index in lindexrow:
            """
            cprangesamesheet(sheet=sheet_des,
                            rangetocopy="{0}{1}".format(eles,startrow + 1),
                            rangetopaste="{0}{1}".format(eles,index))
            """
            sheet_des.range("{0}{1}".format(eles,index)).formula = formulasfor_col_dup[count].format(index)
    """        
    for eles in col_dup:
        # get value at start row from copy file to des
        sheet_des.range("{0}{1}".format(eles,
                                        startrow + 1)).value = sheet_copy.range("{0}{1}".format(eles,
                                                                                                startrow + 1)).formula
        vtformulas = sheet_des.range("{0}{1}".format(eles,
                                                    startrow + 1)).formula
        sheet_des.range("{0}{1}:{0}{2}".format(eles,
                                                startrow + 1,
                                                max_row)).formula = vtformulas
        lindexrow = lcellindexbyvalue(max_row=max_row_allsheet,
                                        min_row=startrow,
                                        max_col=col_key_msa,
                                        min_col=col_key_msa,
                                        sheet=sheet_des,
                                        lvalue=valueim
                                        )
        print (lindexrow,valueim)
        lindexrow = lindexrow + [max_row_allsheet]
        listpair = pairiterationlist(lindexrow)
        for pe in listpair:
            row_u,row_b = pe
            sheet_des.range("{0}{1}".format(eles,row_u)).value = "=SUBTOTAL(9,{0}{1}:{0}{2})".format(eles,row_u + 1,row_b - 1)
        
    """
