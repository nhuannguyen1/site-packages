from tkinter import messagebox
from pynvn.path.ppath import getdirpath,refullpath
from pynvn.excel import col2num,colnum_string
import xlwings as xw 
from pynvn.csv.rcsv import returndictrowforcsv
from appnvn.exazp.excel.itemhm import azb10,azb30
from pynvn.string.slist import str_returnliststr
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
                    namesheet = "AZB-30"
                ):
        # call dict 
        dictconf = returndictrowforcsv(path=pathconf)
        # return list sheet excel to handling 
        listsheetex = dictconf["sheetnamechild"]
        listsheetex = str_returnliststr(listsheetex)

        self.__namesheet = namesheet
        self.__pathdes = pathdes
        self.__pathtocopy = pathtocopy
        self.app = xw.App(visible=False)
        self.desxw = xw.Book(pathdes)
        self.copyxw = xw.Book(pathtocopy)
        self.ws1 = self.copyxw.sheets[self.__namesheet]
        #max row ws1
        self.rows = self.ws1.api.UsedRange.Rows.count
        #max colum ws1
        self.cols = self.ws1.api.UsedRange.Columns.count
        zab30_recor_l = dictconf["zab30_recor_l1"]
        self.__zab30_valuelastrow = dictconf["zab30_valuelastrow"]
        try:
            self.__zab30_valuelastrow = float(self.__zab30_valuelastrow)
        except:
            pass
        self.__azb30_ms =col2num(dictconf["azb30_ms"]) 
        self.__zab30_recor_l_lint = returnseplistintbbystr(zab30_recor_l)
        self.__listmaxrc = self.__zab30_recor_l_lint + [self.rows]

        colunsande = [colnum_string(1),
                    colnum_string(self.cols)]
        self.__listrange = pairlistandlist(listm=self.__listmaxrc,
                                            list_str=colunsande)
    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        # delete sheetname if extsting
        try:
            self.desxw.sheets[self.__namesheet].delete()
            self.desxw.save()
        except:
            pass
        # copy sheet name
        self.ws1.api.Copy(Before=self.desxw.sheets["Sheet1"].api)
        # convert value range in sheet 
        for rangele in self.__listrange:
            my_values = self.copyxw.sheets[self.__namesheet].range(rangele).options(ndim=2).value 
            self.desxw.sheets[self.__namesheet].range(rangele).value = my_values
        # delete empty cell
        delrowbyindexcell(incolumndel= self.__azb30_ms,
                            valueofindexcoldel=None,
                            wb=self.desxw,
                            namesheet=self.__namesheet,
                            startrow=self.__zab30_recor_l_lint[0],
                            endrow=self.rows,
                            valuetoendrow=self.__zab30_valuelastrow
                            )
        self.copyxw.close()
        self.desxw.save()
        self.desxw.close()
        self.app.quit()