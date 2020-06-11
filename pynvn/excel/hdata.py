from pynvn.path.ppath import refullpath
from pynvn.excel import (
                        repathlinkexcel,
                        relistsheet,
                        )
class hexcel:
    """copy excel to excel"""
    def __init__(self,wsheet = None,
                    wsheet_AZ30 = None,
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
                self.wsheet_AZ30 = wsheet_AZ30

    def habz30 (self):
        """handling data azb-30 sheet"""
        lsheetnames = relistsheet(self.fpath)
        print (lsheetnames)
        for k in range (10,self.mcol):
            hmname =  self.wsheet.cell(row=3, 
                                        column=k).value

            if hmname in lsheetnames:

                self.fomuluasfcol(k,hmname=hmname)

    def fomuluasfcol (self,k,starr=6,finshr = 282,hmname = None ):
        """fomulas for column follow index"""
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        for i in range(starr,finshr):
            valuene = '=SUMPRODUCT(--({0}!$B$501:$B${3}<>"")*({0}!$B$501:$B${3}={1}!C{2})*{0}!$I$501:$I${3})'.format(pfile,
                                                                                        "'" + "AZB-30" + "'",
                                                                                        i,
                                                                                        self.mrow)

            self.wsheet.cell(row=i, 
                            column=k).value = valuene

    def habz60 (self,wsheet_AZ30):
        """handling data azb-60 sheet"""
        # list all sheet name from file path 
        lsheetnames = relistsheet(self.fpath)
        lsheet = self.listsheetnameinexsting(listnames=lsheetnames,wsheet_AZ30=wsheet_AZ30)
        for i in range(6,self.mrow):
            sumvalue = ""
            for hmname in lsheet:
                valuesum = self.valuecolsheet(i = i ,hmname=hmname)
                sumvalue = sumvalue + "+" +  valuesum
            self.wsheet.cell(row=i,column=8).value =  "=" + sumvalue 
    
    def valuecolsheet (self,i = 1,hmname = None, namefiter = "62"):
        """fomulas for column follow index"""
        valuechek = self.wsheet.cell(row=i,column=3).value 
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        if str(valuechek)[:2] != namefiter:

            valueeee = 'SUMIF({0}!$BC:$BC,C{1},{0}!$CA:$CA) + SUMIF({0}!$BC:$BC,C{1},{0}!$CB:$CB)'.format(pfile,i)
        else:
            valueeee = 'SUMIF({0}!$BC:$BC,C{1},{0}!$CC:$CC) + SUMIF({0}!$BC:$BC,C{1},{0}!$CD:$CD)'.format(pfile,i) 

        return valueeee

    def listsheetnameinexsting (self, listnames, wsheet_AZ30):
        
        return [wsheet_AZ30.cell(row=3,column=k).value for k in range (10,self.mcol) if wsheet_AZ30.cell(row=3,column=k).value in listnames]

    def returnlistvaluebycolumnindex (self):

        return [cell.value for row in ws.iter_rows('C{}:C{}'.format(ws.min_row,ws.max_row)) for cell in row ]

        
