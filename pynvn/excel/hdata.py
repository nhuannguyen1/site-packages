from pynvn.path.ppath import refullpath
from pynvn.excel import (
                        repathlinkexcel,
                        relistsheet,
                        )

from pynvn.excel import col2num
from pynvn.string import sepnumberandstrfromstr
class hexcel_sep:
    """copy excel to excel"""
    def __init__(self,wsheet = None,
                    wsheet_AZ30 = None,
                    dpath = None,
                    namefile = None,
                    dicrowconf = None
                ):
                self.dpath = dpath
                self.wsheet = wsheet
                self.namefile = namefile
                self.fpath = refullpath(dirpath=self.dpath,
                                        filename=self.namefile)
                self.mcol = self.wsheet.max_column
                self.mrow = self.wsheet.max_row
                self.wsheet_AZ30 = wsheet_AZ30

                self.__azb30_starcolumn = col2num(dicrowconf["azb30_starcolumn"])
                self.__azb30_rowhm = int(dicrowconf["azb30_rowhm"])
                self.__azb30_maxrowhm = int(dicrowconf["azb30_maxrowhm"])
                self.__azb30_startrowhm = int(dicrowconf["azb30_startrowhm"])
                self.__azb60_startrowhm = int(dicrowconf["azb60_startrowhm"])
                self.__azb60_msdforkct = (dicrowconf["azb60_msdforkct"])
                self.__azb60_dongia = col2num(dicrowconf["azb60_dongia"])
                self.__hm_rangege = (dicrowconf["hm_rangege"])
                self.numberhm = int(sepnumberandstrfromstr(self.__hm_rangege)[1])
                print ("self.numberhm",self.numberhm)
    def habz30 (self):
        """handling data azb-30 sheet"""
        lsheetnames = relistsheet(self.fpath)
        for k in range (self.__azb30_starcolumn ,self.mcol):
            hmname =  self.wsheet.cell(row=self.__azb30_rowhm , 
                                        column=k).value

            if hmname in lsheetnames:

                self.fomuluasfcol(k,hmname=hmname)

    def fomuluasfcol (self,k,hmname = None ):
        """fomulas for column follow index"""
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        for i in range(self.__azb30_startrowhm,self.__azb30_maxrowhm):
            valuene = '=SUMPRODUCT(--({0}!$B${4}:$B${3}<>"")*({0}!$B${4}:$B${3}={1}!C{2})*{0}!$I${4}:$I${3})'.format(pfile,
                                                                                        "'" + "AZB-30" + "'",
                                                                                        i,
                                                                                        self.mrow,
                                                                                        self.numberhm)

            self.wsheet.cell(row=i, 
                            column=k).value = valuene

    def habz60 (self,wsheet_AZ30):
        """handling data azb-60 sheet"""
        # list all sheet name from file path 
        lsheetnames = relistsheet(self.fpath)
        lsheet = self.listsheetnameinexsting(listnames=lsheetnames,wsheet_AZ30=wsheet_AZ30)
        for i in range(self.__azb60_startrowhm,self.mrow):
            sumvalue = ""
            for hmname in lsheet:
                valuesum = self.valuecolsheet(i = i ,hmname=hmname)
                sumvalue = sumvalue + "+" +  valuesum
            self.wsheet.cell(row=i,column=self.__azb60_dongia).value =  "=" + sumvalue 
    
    def valuecolsheet (self,i = 1,hmname = None):
        """fomulas for column follow index"""
        valuechek = self.wsheet.cell(row=i,column=3).value 
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        if str(valuechek)[:2] != self.__azb60_msdforkct:

            valueeee = 'SUMIF({0}!$BC:$BC,C{1},{0}!$CA:$CA) + SUMIF({0}!$BC:$BC,C{1},{0}!$CB:$CB)'.format(pfile,i)
        else:
            valueeee = 'SUMIF({0}!$BC:$BC,C{1},{0}!$CC:$CC) + SUMIF({0}!$BC:$BC,C{1},{0}!$CD:$CD)'.format(pfile,i) 

        return valueeee

    def listsheetnameinexsting (self, listnames, wsheet_AZ30):
        
        return [wsheet_AZ30.cell(row=self.__azb30_rowhm,column=k).value for k in range (self.__azb30_starcolumn ,self.mcol) if wsheet_AZ30.cell(row=self.__azb30_rowhm,column=k).value in listnames]

    def returnlistvaluebycolumnindex (self):

        return [cell.value for row in ws.iter_rows('C{}:C{}'.format(ws.min_row,ws.max_row)) for cell in row ]

        