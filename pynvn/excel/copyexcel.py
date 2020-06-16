import openpyxl as xl
from tkinter import messagebox
from pynvn.path.ppath import getdirpath,refullpath
from pynvn.excel import col2num
import xlwings as xw 
from pynvn.csv.rcsv import returndictrowforcsv
from appnvn.exazp.excel.itemhm import azb10

class cexcel:
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
        self.names = self.__wb1 .sheets
        self.__ws1 = self.__wb1 .sheets[self.names[0]] 
        self.__wsname = self.__ws1.name
        self.__wb2 = xw.Book(self.pathdes)
        #max row ws1
        self.rows = self.__ws1.api.UsedRange.Rows.count
        #max colum ws1
        self.cols = self.__ws1.api.UsedRange.Columns.count
        
        # sheet to destionation (mother file)
        self.__ws2 = self.__wb2 .sheets[self.__wsname]
        # check name sheet 
        if self.namesheetchild  in self.__wsname:
            pass
        else:
            messagebox.showerror("error", 
                                "Name sheet must start \
                                from symbols {}...".format(self.namesheetchild))

    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """
        azb_10 =azb10(dictconf=self.dicrowconf,
                        wsheetcopy=self.__ws1,
                        wsheetdes=self.__ws2,
                        mrowwscopy=self.rows,
                        mcolumnwscopy=self.cols).copysheettoexcelexist()

        self.__wb1.close()
        self.__wb2.save()
        self.__wb2.close()
        self.__app.quit()