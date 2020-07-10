from tkinter import messagebox
from pynvn.path.ppath import getdirpath,refullpath
from pynvn.excel import col2num,colnum_string
import xlwings as xw 
from pynvn.csv.rcsv import returndictrowforcsv
from appnvn.exazp.excel.itemhm import azb10,azb30
from pynvn.string.slist import returnseplistintbbystr,str_seplistintbbystr
from pynvn.excel import delrowbyindexcell
from pynvn.list.flist import pairlistandlist
class cexcel_re:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                    pathdes= None, 
                    pathtocopy= None,
                    namesheetchild = "AZB",
                    pathconf = None
                ):
        self.dicrowconf = returndictrowforcsv(path=pathconf)
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy
        self.namesheetchild = namesheetchild
        self.__Getlistsheet()
    def __Getlistsheet(self):
        self.__app = xw.App(visible=False)
        self.__wb1  = xw.Book(self.pathtocopy)
        self.names = self.__wb1.sheets
        self.__ws1 = self.__wb1.sheets[self.names[0]] 
        self.__wsname = self.__ws1.name
        self.__wb1.close()
        self.__app.quit()
        # check name sheet 
        if self.namesheetchild  in self.__wsname:
            pass
        else:
            messagebox.showerror("error", 
                                "Name sheet must start \
                                from symbols {}...".format(self.namesheetchild))

    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        if self.__wsname == "AZB-10":
            azb10(dictconf=self.dicrowconf,
                        wsheetcopy=self.__ws1,
                        wsheetdes=self.__ws2,
                        mrowwscopy=self.rows,
                        mcolumnwscopy=self.cols).copysheettoexcelexist()

        if self.__wsname == "AZB-30":
            azb30(dictconf=self.dicrowconf,
                        pathdes=self.pathdes,
                        pathtocopy=self.pathtocopy
                        ).copysheettoexcelexist()
    
class cexcel:
    """copy excel to excel"""
    def __init__(self,
                    pathconf = None,
                    pathdes= None, 
                    pathtocopy= None,
                    namesheetk = "AZB"
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
        colunsande = [colnum_string(1),
                    colnum_string(self.cols)]
        # azb30
        zab30_recor_l = dictconf["zab30_recor_l1"]
        self.__zab30_recor_l_lint = returnseplistintbbystr(zab30_recor_l)
        self.__listmaxrc = self.__zab30_recor_l_lint + [self.rows]
        # ms azb30
        self.__azb30_ms =col2num(dictconf["azb30_ms"])

        self.__zab30_valuelastrow = dictconf["zab30_valuelastrow"]
        try:
            self.__zab30_valuelastrow = float(self.__zab30_valuelastrow)
        except:
            pass
        
        self.__listrange = pairlistandlist(listm=self.__listmaxrc,
                                            list_str=colunsande)
        # azb10
        zab10_recor_l = dictconf["zab10_recor_l1"]
        self.__zab10_recor_l_lint = returnseplistintbbystr(zab10_recor_l)
        self.__listmaxrcazb10 = self.__zab10_recor_l_lint + [self.rows]
        # ms azb10
        self.__azb10_ms =col2num(dictconf["azb10_ms"]) 

        self.__listrangeazb10 = pairlistandlist(listm=self.__listmaxrcazb10,
                                            list_str=colunsande)


        self.__zab10_valuelastrow = dictconf["zab10_valuelastrow"]
        try:
            self.__zab10_valuelastrow = float(self.__zab10_valuelastrow)
        except:
            pass

        # azb60
        zab60_recor_l = dictconf["zab60_recor_l1"]
        self.__zab60_recor_l_lint = returnseplistintbbystr(zab60_recor_l)
        self.__listmaxrcazb60 = self.__zab60_recor_l_lint + [self.rows]
        # ms azb60
        self.__azb60_ms =col2num(dictconf["azb60_ms"]) 

        self.__listrangeazb60 = pairlistandlist(listm=self.__listmaxrcazb60,
                                            list_str=colunsande)

        self.__zab60_valuelastrow = dictconf["zab60_valuelastrow"]
        try:
            self.__zab60_valuelastrow = float(self.__zab60_valuelastrow)
        except:
            pass

        # azb50
        zab50_recor_l = dictconf["zab50_recor_l1"]
        self.__zab50_recor_l_lint = returnseplistintbbystr(zab50_recor_l)
        self.__listmaxrcazb50 = self.__zab50_recor_l_lint + [self.rows]
        # ms azb50
        self.__azb50_ms =col2num(dictconf["azb50_ms"]) 

        self.__listrangeazb50 = pairlistandlist(listm=self.__listmaxrcazb50,
                                            list_str=colunsande)

        self.__zab50_valuelastrow = dictconf["zab50_valuelastrow"]
        try:
            self.__zab50_valuelastrow = float(self.__zab50_valuelastrow)
        except:
            pass

        # azb40
        zab40_recor_l = dictconf["zab40_recor_l1"]
        self.__zab40_recor_l_lint = returnseplistintbbystr(zab40_recor_l)
        self.__listmaxrcazb40 = self.__zab40_recor_l_lint + [self.rows]
        # ms azb40
        self.__azb40_ms =col2num(dictconf["azb40_ms"]) 

        self.__listrangeazb40 = pairlistandlist(listm=self.__listmaxrcazb40,
                                            list_str=colunsande)

        self.__zab40_valuelastrow = dictconf["zab40_valuelastrow"]
        try:
            self.__zab40_valuelastrow = float(self.__zab40_valuelastrow)
        except:
            pass

        # azb70
        zab70_recor_l = dictconf["zab70_recor_l1"]
        self.__zab70_recor_l_lint = returnseplistintbbystr(zab70_recor_l)
        self.__listmaxrcazb70 = self.__zab70_recor_l_lint + [self.rows]
        # ms azb70
        self.__azb70_ms =col2num(dictconf["azb70_ms"]) 

        self.__listrangeazb70 = pairlistandlist(listm=self.__listmaxrcazb70,
                                            list_str=colunsande)

        self.__zab70_valuelastrow = dictconf["zab70_valuelastrow"]
        try:
            self.__zab70_valuelastrow = float(self.__zab70_valuelastrow)
        except:
            pass


        # azb80
        zab80_recor_l = dictconf["zab80_recor_l1"]
        self.__zab80_recor_l_lint = returnseplistintbbystr(zab80_recor_l)
        self.__listmaxrcazb80 = self.__zab80_recor_l_lint + [self.rows]
        # ms azb80
        self.__azb80_ms =col2num(dictconf["azb80_ms"]) 

        self.__listrangeazb80 = pairlistandlist(listm=self.__listmaxrcazb80,
                                            list_str=colunsande)

        self.__zab80_valuelastrow = dictconf["zab80_valuelastrow"]
        try:
            self.__zab80_valuelastrow = float(self.__zab80_valuelastrow)
        except:
            pass


        # sheet name of azb 
        self.__namesheet = self.ws1.name
    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        # delete sheetname if extsting
        try:
            self.__desxw.sheets[self.__namesheet].delete()
            self.__desxw.save()
        except:
            pass
        # copy sheet name
        self.ws1.api.Copy(Before=self.__desxw.sheets["Sheet1"].api)
        # convert value range in sheet 
        if self.__namesheet == "AZB-30":
            for rangele in self.__listrange:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
        
            delrowbyindexcell(incolumndel= self.__azb30_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab30_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab30_valuelastrow
                            )
        if self.__namesheet == "AZB-10":
            for rangele in self.__listrangeazb10:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
            delrowbyindexcell(incolumndel= self.__azb10_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab10_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab10_valuelastrow
                            )
        if self.__namesheet == "AZB-60":
            for rangele in self.__listrangeazb60:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
            delrowbyindexcell(incolumndel= self.__azb60_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab60_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab60_valuelastrow
                            )
        if self.__namesheet == "AZB-50":
            for rangele in self.__listrangeazb50:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
            delrowbyindexcell(incolumndel= self.__azb50_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab50_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab50_valuelastrow
                            )        

        if self.__namesheet == "AZB-40":
            for rangele in self.__listrangeazb40:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
            delrowbyindexcell(incolumndel= self.__azb40_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab40_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab40_valuelastrow
                            )        

        if self.__namesheet == "AZB-70":
            for rangele in self.__listrangeazb70:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
            delrowbyindexcell(incolumndel= self.__azb70_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab70_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab70_valuelastrow
                            )   

        if self.__namesheet == "AZB-80":
            for rangele in self.__listrangeazb80:
                my_values = self.__copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
                self.__desxw.sheets[self.__namesheet].range(rangele).value = my_values
            # delete empty cell
            delrowbyindexcell(incolumndel= self.__azb80_ms,
                            valueofindexcoldel=None,
                            wb=self.__desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab80_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab80_valuelastrow
                            )   
        self.__copyxw.close()
        self.__desxw.save()
        self.__desxw.close()
        self.__app.quit()