import openpyxl as xl
from tkinter import messagebox
from pynvn.path.ppath import refullpath
from pynvn.excel import returnsheet,repathlinkexcel,relistsheet

class hexcel:
    """copy excel to excel"""
    def __init__(self,wsheet = None,
                    dpath = None,
                    namesheet = "TONG HOP HM",
                    namefile = None,
                    keyhm = "HM."
                ):
                self.dpath = dpath
                self.wsheet = wsheet
                self.namesheet = namesheet
                self.namefile = namefile
                self.keyhm = keyhm
                self.fpath = refullpath(dirpath=self.dpath,
                                        filename=self.namefile)
                print ("self.fpath",self.fpath )

    def habz30 (self):
        """handling data azb-30 sheet"""
        # return name sheet for link fomular
        #pfile = repathlinkexcel(dpath=self.dpath,namefile=self.namefile,namesheet=self.namesheet )
        # return list of list 
        lsheetnames = relistsheet(self.fpath)
        print ("lsheetnames",lsheetnames)
        for lsheet in lsheetnames:
            if self.keyhm in lsheet:
                pfile = repathlinkexcel(dpath=self.dpath,namefile=self.namefile,namesheet=lsheet)

                print ("pfile",pfile)
                stt = "'" + "AZB-30" + "'"
                print ("stt",stt)

                valuene = '=SUMPRODUCT(({0}!A38:A61={1}!C16)*{0}!I38:I61)'.format(pfile,stt)


                print ("valuene",valuene)

                self.wsheet["J16"].value = valuene
