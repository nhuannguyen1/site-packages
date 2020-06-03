from pynvn.path.ppath import refullpath
from pynvn.excel import (
                        repathlinkexcel,
                        relistsheet,
                        )
class hexcel:
    """copy excel to excel"""
    def __init__(self,wsheet = None,
                    dpath = None,
                    namefile = None,
                ):
                self.dpath = dpath
                self.wsheet = wsheet
                self.namefile = namefile
                self.fpath = refullpath(dirpath=self.dpath,
                                        filename=self.namefile)
                self.mcol = self.wsheet.max_column
                self.mrow = self.wsheet.max_row

    def habz30 (self):
        """handling data azb-30 sheet"""
        lsheetnames = relistsheet(self.fpath)
        for k in range (10,self.mcol):
            hmname =  self.wsheet.cell(row=3, 
                                        column=k).value

            if hmname in lsheetnames:

                self.fomuluasfcol(k,hmname=hmname)

    def fomuluasfcol (self,k,starr=14,finshr = 474,hmname = None ):
        """fomulas for column follow index"""
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        for i in range(starr,finshr):
            valuene = '=SUMPRODUCT(({0}!$A$501:$A${3}={1}!C{2})*{0}!$I$501:$I${3})'.format(pfile,
                                                                                        "'" + "AZB-30" + "'",
                                                                                        i,
                                                                                        self.mrow)
            self.wsheet.cell(row=i, 
                            column=k).value = valuene