import openpyxl as xl
from tkinter import messagebox
from pynvn.excel.hdata import hexcel_sep
from pynvn.path.ppath import getdirpath,refullpath
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.excel import col2num
class hexcel_child:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                    pathdes= None, 
                    pathtocopy= None,
                    namesheetchild = "AZB",
                    pathconf = None
                ):
        self.sheetname = sheetname
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy
        self.namesheetchild = namesheetchild
        self.dicrowconf = returndictrowforcsv(path=pathconf)
        self.__namefile=self.dicrowconf["khns_namfile"]
        self._Getlistsheet()
    def _Getlistsheet(self):
        self.dirpath = getdirpath(self.pathtocopy)
        self.wb1 = xl.load_workbook(filename=self.pathtocopy)
        self.names = self.wb1.sheetnames
        self.ws1 = self.wb1[self.names[0]]
        # check name sheet 
        if self.namesheetchild  in self.names[0]:
            pass
        else:
            messagebox.showerror("error", 
                                "Name sheet must start \
                                from symbols {}...".format(self.namesheetchild))
    def runaz30azb60(self):
        """ run AZB30 and run AZB60"""
        if (self.names[0] == "AZB-30" or  self.names[0] == "AZB-60"):

            exelh = hexcel_sep(wsheet=self.ws1,
                        dpath=self.dirpath,
                        namefile=self.__namefile,
                        dicrowconf = self.dicrowconf)
            if self.names[0] == "AZB-30":                                    
                exelh.habz30()
            else:
                try:
                    wbazb30 = xl.load_workbook(filename=refullpath(dirpath=self.dirpath,
                                                                    filename="AZB30.xlsx"),
                                                                    )
                except:
                    messagebox.showerror("error",
                                        "check dirpath {} and file name {}".format(dirpath,
                                                                                    filename))
                try:
                    nsazb = wbazb30["AZB-30"]
                except:
                    messagebox.showerror("error",
                                        "check dirpath {} and file name {}".format(dirpath,
                                                                                    filename))

                exelh.habz60(wsheet_AZ30=nsazb)
            try:
                self.wb1.save(self.pathtocopy)
            except:
                messagebox.showerror("error",
                                    "Check path for Pfile {}".format(self.pathtocopy))
        else:
            messagebox.showerror ("error", 
                                    "No sheet name AZB-30 or AZB-60, recheck file again")
