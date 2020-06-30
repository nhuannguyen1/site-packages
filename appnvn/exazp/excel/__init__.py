from tkinter import messagebox
from pynvn.excel import returnsheetbyname,mrowandmcolum,col2num
import openpyxl as xl
from pynvn.excel.crelistadict import credict
import xlwings as xw 
from pynvn.string  import sepnumberandstrfromstr
from pynvn.excel import convertrangaphatonunber,returnrangelastcolumn,col2num
from pynvn.csv.rcsv import returndictrowforcsv
from pynvn.string import no_accent_vietnamese
from pynvn.excel.path import returnactivewbpath
from pynvn.list.str import converlistinstrtolist
from pynvn.csv.tolist import convertcsvtolist 
from pynvn.path.ppath import refullpath,parentdirectory
class hexcel:
    """hading data excel for azzbbb"""
    def __init__ (self, fpath = None,
                        pathconf = None
                        ):
        dicrowconf = returndictrowforcsv(path=pathconf)
        self.__fpath = fpath
        dirparhconf = parentdirectory(pathconf)
        self.__sheetnametor=dicrowconf["khns_sheetnamekhns"]
        self.__rangeg =dicrowconf["hm_rangege"]
        self.__mvt = int(dicrowconf["khns_mavatu"])
        self.__khns_ndcv = int(dicrowconf["khns_noidungcongviec"])
        self.__khns_dvt = int(dicrowconf["khns_dvt"])
        self.__khns_dvt = int(dicrowconf["khns_muchaophi"])
        self.__hm_mvt = int(dicrowconf["hm_mvt"])
        self.__hm_ndcv = int(dicrowconf["hm_noidungcongviec"])
        self.__hm_dvt = int(dicrowconf["hm_dvt"])
        self.__hm_dgth = int(dicrowconf["hm_dgth"])
        self.__hm_ttnt = int(dicrowconf["hm_ttnt"])
        self.__hm_startrowvalue = int(dicrowconf["hm_startrowvalue"])
        self.__hm_vta = dicrowconf["hm_vt"]
        self.__hm_nca = dicrowconf["hm_nc"]
        self.__hm_mtca = dicrowconf["hm_mtc"]
        self.__hm_tha = dicrowconf["hm_th"]

        self.__hm_vt =col2num (dicrowconf["hm_vt"]) 
        self.__hm_nc =col2num (dicrowconf["hm_nc"]) 
        self.__hm_mtc =col2num (dicrowconf["hm_mtc"])
        self.__hm_th =col2num (dicrowconf["hm_th"])
        self.__valuenotnone =dicrowconf["valuenotnone"]
        self.__dictvalue =dicrowconf["dictvalue"]
        # csv for dict 
        self.pathtovalue = refullpath(dirparhconf,self.__dictvalue)
        # csv for value 
        self.valuenotnone = refullpath(dirparhconf,self.__valuenotnone)
        self.__khns_rangenumbermct_ptvt =dicrowconf["khns_rangenumbermct_ptvt"]
        self.__returnothervalue()

    def __returnothervalue(self):
        # return active workbook 
        self.__fpath = returnactivewbpath()
        # load work book by full path 
        wb = xw.Book(self.__fpath)
        # set active workbook
        self.sht1 = wb.sheets.active
        self.sheetnameactive = wb.sheets.active.name
        # get set thvt 
        self.thvt = wb.sheets[self.__sheetnametor]
        
        # find last row
        self.m_row = self.sht1.range('A' + str(self.sht1.cells.last_cell.row)).end('up').row + 5

        self.rangegc = returnrangelastcolumn(stringrang=self.__rangeg,
                                                        lrow=self.m_row)

    def gdatafromothersheet (self,
                            realtime = True):
        """ get data from mothers sheet """
        #create dict with key is parent ma vat tu 
        redic = converlistinstrtolist(path=self.pathtovalue)
        # return list ma cong tac not node in cell value of ptvl
        getvaluelist = convertcsvtolist(path=self.valuenotnone)
        # return index row and value of active sheet  ma cong tac
        indexrcevalu = [[cell.row,
                        cell.value] for rangecell in 
                        self.sht1.range(self.rangegc)
                        for cell in rangecell  if  cell.value
                        in getvaluelist]
        # set value to acitve sheet 
        for indexr, value_parent in indexrcevalu:
            # get noi dung cong viec 
            value_parent_h = no_accent_vietnamese(value_parent)
            valuearr = redic.get(value_parent_h,[[indexr,"Kiem tra ma cong tac"]])
            index1, value1 = valuearr[0]
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
                                                                                icolumn=self.__khns_dvt)
                self.sht1.range(indexrk + 1 ,self.__hm_ttnt).value = '=I{0}*H{1}'.format(indexr,
                                                                                indexrk + 1)
                i = i + 1
    def listothercell (self,irow,icolumn):
        """ return value of column sheet ptvl1"""
        valuebycolr = self.thvt.range(irow,icolumn).value 
        return valuebycolr

    def valuehangmucforthvt(self):
        lrow = self.sht1.range('BC' + str(self.sht1.cells.last_cell.row)).end('up').row
        # column vt
        self.sht1.range(self.__hm_startrowvalue,self.__hm_vt).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$L$8:$L${0})".format(lrow,
                                                                                                                    self.__sheetnametor,
                                                                                                                    self.__hm_startrowvalue,
                                                                                                                    "'" + self.sheetnameactive + "'")
        vtformulas = self.sht1.range(self.__hm_startrowvalue,self.__hm_vt).formula
        self.sht1.range("{0}{1}:{0}{2}".format(self.__hm_vta,self.__hm_startrowvalue,lrow)).formula = vtformulas
        # column nc
        self.sht1.range(self.__hm_startrowvalue,self.__hm_nc).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$M$8:$M${0})".format(lrow,
                                                                                                                    self.__sheetnametor,
                                                                                                                    self.__hm_startrowvalue,
                                                                                                                    "'" + self.sheetnameactive + "'")
        ncformulas = self.sht1.range(self.__hm_startrowvalue,self.__hm_nc).formula
        self.sht1.range("{0}{1}:{0}{2}".format(self.__hm_nca,self.__hm_startrowvalue,lrow)).formula = ncformulas
        # column mtc 
        self.sht1.range(self.__hm_startrowvalue,self.__hm_mtc).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$N$8:$N${0})".format(lrow,
                                                                                                            self.__sheetnametor,
                                                                                                            self.__hm_startrowvalue,
                                                                                                            "'" + self.sheetnameactive + "'")
        mtcformulas = self.sht1.range(self.__hm_startrowvalue,self.__hm_mtc).formula
        self.sht1.range("{0}{1}:{0}{2}".format(self.__hm_mtca,self.__hm_startrowvalue,lrow)).formula = mtcformulas    
         
        # column sum
        self.sht1.range(self.__hm_startrowvalue,self.__hm_th ).value = "=SUM(BF{0}:BH{0})".format(self.__hm_startrowvalue)

        sumformulas = self.sht1.range(self.__hm_startrowvalue,self.__hm_th).formula
        self.sht1.range("{0}{1}:{0}{2}".format(self.__hm_tha,self.__hm_startrowvalue,lrow)).formula = sumformulas           