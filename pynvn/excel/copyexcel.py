from tkinter import messagebox
from pynvn.path.ppath import getdirpath,ExtractFileNameFromPath
from pynvn.excel import col2num,colnum_string, repathlinkexcel
import xlwings as xw 
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.string.slist import returnlist_from_listinstr
from pynvn.string.slist import str_returnliststr
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
        print("sheet name" ,self.__namesheet)
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

        if self.__namesheet == "AZB-20":
            recor_l_lint = int(self.dictconf["zab20_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab20_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab20_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb20_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab20_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab20_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab20_dup"].replace(":", ","))
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

        if self.__namesheet == "AZB-40":
            recor_l_lint = int(self.dictconf["zab40_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab40_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab40_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb40_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab40_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab40_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab40_dup"].replace(":", ","))
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
        if self.__namesheet == "AZB-50":
            recor_l_lint = int(self.dictconf["zab50_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab50_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab50_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb50_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab50_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab50_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab50_dup"].replace(":", ","))
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

        if self.__namesheet == "AZB-60":
            recor_l_lint = int(self.dictconf["zab60_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab60_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab60_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb60_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab60_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab60_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab60_dup"].replace(":", ","))
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

        if self.__namesheet == "AZB-70":
            recor_l_lint = int(self.dictconf["zab70_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab70_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab70_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb70_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab70_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab70_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab70_dup"].replace(":", ","))
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

        if self.__namesheet == "AZB-80":
            recor_l_lint = int(self.dictconf["zab80_recor_l1"])
            valueim = returnlist_from_listinstr(self.dictconf["zab80_valueim"].replace(":", ","))
            valuehavechild = returnlist_from_listinstr(self.dictconf["zab80_valuehavechild"].replace(":", ","))
            msstr =self.dictconf["azb80_ms"]
            forbydup = returnlist_from_listinstr(self.dictconf["zab80_forbydup"].replace(":", ","))
            locuseformulas = returnlist_from_listinstr(self.dictconf["zab80_locuseformulas"].replace(":", ","))
            col_dup = returnlist_from_listinstr(self.dictconf["zab80_dup"].replace(":", ","))
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
        self.__copyxw.close()
        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()