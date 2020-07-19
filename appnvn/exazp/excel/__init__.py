from tkinter import messagebox
from pynvn.excel.crelistadict import credict
import xlwings as xw 
from pynvn.string  import sepnumberandstrfromstr
from pynvn.excel import convertrangaphatonunber,returnrangelastcolumn,colnum_string,returnsheetbyname,mrowandmcolum,col2num
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.string import no_accent_vietnamese
from pynvn.excel.path import returnactivewbpath
from pynvn.list.str import converlistinstrtolist
from pynvn.csv.tolist import convertcsvtolist 
from pynvn.path.ppath import refullpath,parentdirectory
from pynvn.string.slist import returnseplistintbbystr,returnliststr_from_str
from pynvn.excel.list import listbyrangeremoveduplicate
from appnvn.exazp.excel.crangeactive import crangeactive
from pynvn.csv.tolist import convertcsvto1list
from pynvn.path.ppath import refullpath,getdirpath
class hexcel:
    """hading data excel for azzbbb"""
    def __init__ (self, fpath = None,
                        pathconf = None,
                        pathconfigexcelcopy = None
                        ):
        self.pathconf = pathconf
        self.pathconfigexcelcopy = pathconfigexcelcopy
        self.dicrowconf = returndictrowforcsv(path=pathconf)
        self.__fpath = fpath
        dirparhconf = parentdirectory(pathconf)
        self.__sheetnametor=self.dicrowconf["khns_sheetnamekhns"]
        self.__namefile=self.dicrowconf["khns_namfile"]
        self.__rangeg =self.dicrowconf["hm_rangege"]

        self.__rangeintct = returnseplistintbbystr(self.__rangeg)

        self.__rangestrct = returnliststr_from_str(self.__rangeg)

        self.__mvt = int(self.dicrowconf["khns_mavatu"])
        self.__khns_ndcv = int(self.dicrowconf["khns_noidungcongviec"])
        self.__khns_dvt = int(self.dicrowconf["khns_dvt"])

        self.__khns_muchaophi = (self.dicrowconf["khns_muchaophi"])
        self.__khns_muchaophi_int = col2num(self.__khns_muchaophi)

        self.__hm_mvt = int(self.dicrowconf["hm_mvt"])
        self.__hm_ndcv = int(self.dicrowconf["hm_noidungcongviec"])
        self.__hm_dvt = int(self.dicrowconf["hm_dvt"])

        self.__hm_dgth_str = (self.dicrowconf["hm_dgth"])

        self.__hm_dgth = col2num(self.__hm_dgth_str)

        self.__hm_ttnt_str = (self.dicrowconf["hm_ttnt"])
        self.__hm_ttnt = col2num(self.__hm_ttnt_str)

        self.__hm_startrowvalue = int(self.dicrowconf["hm_startrowvalue"])
        self.__hm_vta = self.dicrowconf["hm_vt"]
        self.__hm_nca = self.dicrowconf["hm_nc"]
        self.__hm_mtca = self.dicrowconf["hm_mtc"]
        self.__hm_tha = self.dicrowconf["hm_th"]

        self.__hm_ct = self.dicrowconf["hm_ct"]
        self.__hm_ct_int = col2num(self.__hm_ct)

        self.__hm_vt =col2num (self.dicrowconf["hm_vt"]) 
        self.__hm_nc =col2num (self.dicrowconf["hm_nc"]) 
        self.__hm_mtc =col2num (self.dicrowconf["hm_mtc"])
        self.__hm_th =col2num (self.dicrowconf["hm_th"])
        self.__valuenotnone =self.dicrowconf["valuenotnone"]
        valueall =self.dicrowconf["valueall"]
        self.__dictvalue =self.dicrowconf["dictvalue"]
        # csv for dict 
        self.pathtovalue = refullpath(dirparhconf,self.__dictvalue)
        # csv for value 
        self.valuenotnone = refullpath(dirparhconf,self.__valuenotnone)
        # path all value 
        self.pathvalueall = refullpath(dirparhconf,valueall)

        self.__khns_rangenumbermct_ptvt =self.dicrowconf["khns_rangenumbermct_ptvt"]
        # hangmuccongtac 
        self.__hm_startpasterange = self.dicrowconf["hm_startpasterange"]
        self.__startpasterange = returnseplistintbbystr(self.__hm_startpasterange)
        self.__hm_congtac = self.dicrowconf["hm_congtac"]

        # return list ma cong tac not node in cell value of ptvl by csv
        self.getvaluelist = convertcsvtolist(path=self.valuenotnone)
        # return all value from csv 
        self.getallvalue = convertcsvtolist(path=self.pathvalueall)

   
        self.pathlsn = refullpath(dirpath=getdirpath(pathconf),
                                        filename=dictconf["listsheetnamehm"])

        copyhm = self.dicrowconf["copyhm"]
        try:                        
            self.lsheetname = convertcsvto1list(path=self.pathlsn)
        except:
            pass





        self.__returnothervalue()
        self.__returnlistcongtac()
    def __returnothervalue(self):
        # return active workbook 
        self.__fpath = returnactivewbpath(self.__namefile)
        # load work book by full path 
        wb = xw.Book(self.__fpath)
        # set active workbook
        self.sht1 = wb.sheets.active
        self.sheetnameactive = wb.sheets.active.name
        # get set thvt 
        self.thvt = wb.sheets[self.__sheetnametor]

        self.row_ptvt = self.thvt.api.UsedRange.Rows.count

        # find last row
        #self.m_row = self.sht1.range('A' + str(self.sht1.cells.last_cell.row)).end('up').row + 5
        self.m_row = self.sht1.api.UsedRange.Rows.count
        self.rangegc = returnrangelastcolumn(stringrang=self.__rangeg,
                                                        lrow=self.m_row)
    def __returnlistcongtac(self):
        """ return list of cong tac """
        rangea = "{0}{1}:{0}{2}".format(self.__hm_congtac,self.__startpasterange[0] + 2,self.m_row)
        self.listofcongtac  =  listbyrangeremoveduplicate(sheetexcel=self.sht1,rangea=rangea)

    def gdatafromothersheet (self,
                            realtime = True):
        """ get data from mothers sheet """
        # clear hm beforecopy
        #hm_startpasterange = self.dicrowconf["hm_startpasterange_bt"]
        #self.sht1.range(hm_startpasterange).api.Delete()
        crangeactive(pathconf=self.pathconf,
                    pathconfigexcelcopy=self.pathconfigexcelcopy).copyrangfromconf_bt()
        #create dict with key is parent ma vat tu 
        redic = converlistinstrtolist(path=self.pathtovalue)
        dem = 0
        cindex = self.__rangeintct[0] + 4
        for lct in self.listofcongtac:
            if lct in self.getvaluelist:
                rangea = "{0}{1}".format(self.__rangestrct[0],cindex)
                self.sht1.range(rangea).value = lct
                valuearr = redic[lct]
                index1, value1 = valuearr[0]
                indexr = cindex
                self.sht1.range(indexr,self.__hm_ndcv).value  =  self.listothercell(irow =index1-2,
                                                                                    icolumn=self.__khns_ndcv)
                # get don vi
                self.sht1.range(indexr,self.__hm_dvt).value  =  self.listothercell(irow =index1 - 2,
                                                                        icolumn=self.__khns_dvt)
                # get value sum if 
                self.sht1.range(indexr,self.__hm_ttnt).value =  '=SUMIF($BC:$BC,A{},$BL:$BL)'.format (indexr)            
                i = 0 
                for indexrk in range(indexr,indexr + len(valuearr)):
                    index, value = valuearr[i]
                    self.sht1.range(indexrk + 1 ,self.__hm_mvt).value = value
                    self.sht1.range(indexrk + 1 ,self.__hm_ndcv).value = self.listothercell(irow =index,
                                                                                            icolumn=self.__khns_ndcv)
                    self.sht1.range(indexrk + 1 ,self.__hm_dvt).value = self.listothercell(irow =index,
                                                                                icolumn=self.__khns_dvt)

                    self.sht1.range(indexrk + 1 ,self.__hm_dgth).value = self.listothercell(irow =index,
                                                                                icolumn=self.__khns_muchaophi_int )

                    self.sht1.range(indexrk + 1 ,self.__hm_ttnt).value = '=L{0}*K{1}'.format(indexr,
                                                                                indexrk + 1)
                    i = i + 1
                cindex = cindex + len(valuearr)+ 2

    def listothercell (self,irow,icolumn):
        """ return value of column sheet ptvl1"""
        valuebycolr = self.thvt.range(irow,icolumn).value 
        return valuebycolr

    def valuehangmucforthvt(self):
        """ value from hang muc for thvt """

        lrow =  self.sht1.range(self.__hm_ct + str(self.sht1.cells.last_cell.row)).end('up').row
        for index in range(self.__hm_startrowvalue, lrow + 1):
            if self.sht1.range(index,self.__hm_ct_int).value in self.getallvalue:
                self.sht1.range(index,self.__hm_vt).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$I$8:$I${0})".format(self.row_ptvt,
                                                                                                                    self.__sheetnametor,
                                                                                                                    index,
                                                                                                                    "'" + self.sheetnameactive + "'")
                self.sht1.range(index,self.__hm_nc).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$J$8:$J${0})".format(self.row_ptvt,
                                                                                                                    self.__sheetnametor,
                                                                                                                    index,
                                                                                                                    "'" + self.sheetnameactive + "'")
                self.sht1.range(index,self.__hm_mtc).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$K$8:$K${0})".format(self.row_ptvt,
                                                                                                            self.__sheetnametor,
                                                                                                            index,
                                                                                                            "'" + self.sheetnameactive + "'")
                self.sht1.range(index,self.__hm_th ).value = "=SUM(BF{0}:BH{0})".format(index)