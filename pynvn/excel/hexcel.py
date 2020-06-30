import openpyxl as xl
import xlwings as xw
from tkinter import messagebox
from pynvn.excel.hdata import hexcel_sep
from pynvn.path.ppath import getdirpath,refullpath
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.excel import col2num

class hexcel_child:
    """copy excel to excel"""
    def __init__(self,
                    pathtocopy= None,
                    namesheetchild = "AZB",
                    pathconf = None
                ):
        self.pathtocopy = pathtocopy
        self.namesheetchild = namesheetchild
        self.dicrowconf = returndictrowforcsv(path=pathconf)
        self.__namefile=self.dicrowconf["khns_namfile"]
        self.__Getlistsheet()
    def __Getlistsheet(self):
        self.__app = xw.App(visible=False)
        self.__wb1  = xw.Book(self.pathtocopy)
        self.names = self.__wb1.sheets
        self.lsheetname = [sheet.name for sheet in self.names]
        self.__ws1 = self.__wb1.sheets[self.names[0]] 
        self.__wsname = self.__ws1.name
        #max row ws1
        self.rows = self.__ws1.api.UsedRange.Rows.count
        #max colum ws1
        self.cols = self.__ws1.api.UsedRange.Columns.count
        # check name sheet (have to have AZB)
        if self.namesheetchild  in self.__wsname:
            pass
        else:
            messagebox.showerror("error", 
                                "Name sheet must start \
                                from symbols {}...".format(self.namesheetchild))

        self.__dirpath = getdirpath(self.pathtocopy)

        self.__fpath = refullpath(dirpath=self.__dirpath,
                                        filename=self.__namefile)
        
        self.__wbthns  = xw.Book(self.__fpath)
    def runaz30azb60(self):
        """ run AZB30 and run AZB60"""
        if (self.lsheetname[0] == "AZB-30" or  self.lsheetname[0] == "AZB-60"):
            exelh = hexcel_sep(wsheet=self.__ws1,
                                dpath=self.__dirpath,
                                namefile=self.__namefile,
                                dicrowconf = self.dicrowconf,
                                wbnsct=self.__wbthns
                                )
            if self.lsheetname[0] == "AZB-30":                                    
                exelh.habz30()
            else:
                try:
                    pathh = refullpath(dirpath=self.__dirpath,filename="AZB30.xlsx")
                    self.wbazb30  = xw.Book(pathh)
                    #self.sheetwbazb30 = self.__wbazb30.sheets["AZB-30"]
                except:
                    messagebox.showerror("error",
                                        "check dirpath 1 {} and file name {}".format(self.__dirpath,
                                                                                    "AZB30.xlsx"))
                try:
                    nsazb = self.wbazb30.sheets["AZB-30"]
                    exelh.habz60(wsheet_AZ30=nsazb)
                except:
                    messagebox.showerror("error",
                                        "check dirpath {} and file name {}".format(self.__dirpath,
                                                                                    "AZB30.xlsx"))
            try:
                self.__wb1.save()
            except:
                messagebox.showerror("error",
                                    "Check path for Pfile {}".format(self.pathtocopy))
        else:
            messagebox.showerror ("error", 
                                    "No sheet name AZB-30 or AZB-60, recheck file again")
        self.__wbthns.close()
        try:
            self.__wbazb30.close()
        except:
            pass
        self.__wb1.close()
        self.__app.quit()
