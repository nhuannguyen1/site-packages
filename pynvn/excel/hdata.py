from pynvn.path.ppath import refullpath
from pynvn.excel import (
                        repathlinkexcel,
                        relistsheet,
                        )

from pynvn.excel import col2num,colnum_string
from pynvn.string import sepnumberandstrfromstr
from pynvn.string.slist import returnseplistintbbystr
class hexcel_sep:
    """copy excel to excel"""
    def __init__(self,wsheet = None,
                    wsheet_AZ30 = None,
                    dpath = None,
                    namefile = None,
                    dicrowconf = None,
                    wbnsct = None
                ):
                self.dpath = dpath
                self.wsheet = wsheet
                self.namefile = namefile
                #max colum ws1
                self.mcol = self.wsheet.api.UsedRange.Columns.count
                #max row ws1
                self.mrow = self.wsheet.api.UsedRange.Rows.count
                self.wsheet_AZ30 = wsheet_AZ30
                self.__azb30_starcolumn = col2num(dicrowconf["azb30_starcolumn"])
                self.__azb30_rowhm = int(dicrowconf["azb30_rowhm"])
                self.__azb30_maxrowhm = int(dicrowconf["azb30_maxrowhm"])
                self.__azb30_startrowhm = int(dicrowconf["azb30_startrowhm"])
                self.__azb60_startrowhm = int(dicrowconf["azb60_startrowhm"])
                self.__azb60_msdforkct = (dicrowconf["azb60_msdforkct"])
                self.__azb60_dongia = col2num(dicrowconf["azb60_dongia"])
                self.__hm_rangege = (dicrowconf["hm_rangege"])

                self.__azb60_rangeketcauthep = (dicrowconf["azb60_rangeketcauthep"])

                self.rangese = returnseplistintbbystr(strint=self.__azb60_rangeketcauthep)

                self.numberhm = int(sepnumberandstrfromstr(self.__hm_rangege)[1])
                self.__wb1  = wbnsct
                
    def habz30 (self):
        """handling data azb-30 sheet"""
        lsheetnames = [sheet.name for sheet in self.__wb1.sheets ]
        for k in range (self.__azb30_starcolumn ,self.mcol):
            hmname =  self.wsheet.range(self.__azb30_rowhm , 
                                        k).value
            if hmname in lsheetnames:
                self.fomuluasfcol(k,hmname=hmname)

    def fomuluasfcol (self,k,hmname = None ):
        """fomulas for column follow index"""
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        
        self.wsheet.range(self.__azb30_startrowhm,k).value = "=SUMIFS({0}!$I${4}:$I${3},{0}!$B${4}:$B${3},C{2})".format(pfile,
                                                                "'" + "AZB-30" + "'",
                                                                self.__azb30_startrowhm,
                                                                self.mrow,
                                                                self.numberhm
                                                                )

        vtformulas = self.wsheet.range(self.__azb30_startrowhm,k).formula
        ka = colnum_string(k)
        self.wsheet.range("{0}{1}:{0}{2}".format(ka,self.__azb30_startrowhm,self.__azb30_maxrowhm)).formula = vtformulas
    def habz60 (self,wsheet_AZ30):
        """handling data azb-60 sheet"""
        # list all sheet name from file path 
        lsheetnames =  [sheet.name for sheet in self.__wb1.sheets ]
        lsheet = self.listsheetnameinexsting(listnames=lsheetnames,wsheet_AZ30=wsheet_AZ30)
        for i in range(self.__azb60_startrowhm,self.mrow - 1):

            sumvalue = ""
            for hmname in lsheet:
                valuesum = self.valuecolsheet(i = i ,hmname=hmname)
                sumvalue = sumvalue + "+" +  valuesum
            self.wsheet.range(i,self.__azb60_dongia).value =  "=" + sumvalue 
    
    def valuecolsheet (self,i = 1,hmname = None):
        """fomulas for column follow index"""
        valuechek = self.wsheet.range(i,3).value 
        pfile = repathlinkexcel(dpath=self.dpath,
                                namefile=self.namefile,
                                namesheet=hmname)
        if str(valuechek)[:2] != self.__azb60_msdforkct:
            valueeee = 'SUMIF({0}!$BC:$BC,C{1},{0}!$CA:$CA) + SUMIF({0}!$BC:$BC,C{1},{0}!$CB:$CB)'.format(pfile,i)
        else:
            valueeee = 'SUMIF({0}!$BC:$BC,C{1},{0}!$CC:$CC) + SUMIF({0}!$BC:$BC,C{1},{0}!$CD:$CD)'.format(pfile,i) 
        return valueeee

    def listsheetnameinexsting (self, listnames, wsheet_AZ30):
        return [wsheet_AZ30.range(self.__azb30_rowhm,
                                k).value for k in range (self.__azb30_starcolumn,
                                                                self.mcol) if wsheet_AZ30.range(self.__azb30_rowhm,
                                                                                                k).value in listnames]
    def returnlistvaluebycolumnindex (self):

        return [cell.value for row in ws.iter_rows('C{}:C{}'.format(ws.min_row,ws.max_row)) for cell in row ]
