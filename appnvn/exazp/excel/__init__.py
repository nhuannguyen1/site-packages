from tkinter import messagebox
from pynvn.excel import returnsheetbyname,mrowandmcolum,col2num
import openpyxl as xl
from pynvn.excel.crelistadict import credict
import xlwings as xw 
from pynvn.string  import sepnumberandstrfromstr
from pynvn.excel import convertrangaphatonunber,returnrangelastcolumn,col2num
from pynvn.csv.rcsv import returndictrowforcsv
class hexcel:
    """hading data excel for azzbbb"""
    def __init__ (self, fpath = None,
                        sheetnametor="PTVT1", 
                        rangeg ="A501:A1000",
                        pathconf = None
                        ):
        dicrowconf = returndictrowforcsv(path=pathconf)
        self.__fpath = fpath
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
        self.__hm_vt =col2num (dicrowconf["hm_vt"]) 
        self.__hm_nc =col2num (dicrowconf["hm_nc"]) 
        self.__hm_mtc =col2num (dicrowconf["hm_mtc"])
        
        self.__khns_rangenumbermct_ptvt =dicrowconf["khns_rangenumbermct_ptvt"]
        
        self.__returnothervalue()
    def __returnothervalue(self):
        try:
            self.__fpath = xw.books.active.fullname
            #self.m_row, self.m_col = mrowandmcolum(self.__fpath)
        except:
            messagebox.showerror ("Error",
                                        "Not yet open file excel")
        
        # load work book by full path 
        wb = xw.Book(self.__fpath)
        # set active workbook
        self.sht1 = wb.sheets.active
        self.sheetnameactive = wb.sheets.active.name
        # get set thvt 
        self.thvt = wb.sheets[self.__sheetnametor]
        # find last row
        self.m_row = self.thvt.range('D' + str(self.sht1.cells.last_cell.row)).end('up').row + 5

        self.rangegc = returnrangelastcolumn(stringrang=self.__rangeg,
                                                        lrow=self.m_row)

    def gdatafromothersheet (self,
                            realtime = True):
        """ get data from mothers sheet """
        # get dict 
        rel = credict(pathfull=self.__fpath,
                    namesheet=self.__sheetnametor,
                    engine="xlwings",
                    rangea=self.__khns_rangenumbermct_ptvt)
        #create dict with key is parent ma vat tu 
        redic =rel.redictvaluesandvaluecol(columnumber=self.__mvt)
        # return list ma cong tac not node in cell value of ptvl
        getvaluelist = rel.revaluerownotnone()
        # return index row and value of active sheet  ma cong tac
        indexrcevalu = [[cell.row,
                        cell.value] for rangecell in self.sht1.range(self.rangegc) for cell in rangecell  if  cell.value in getvaluelist]
        # set value to acitve sheet 
        for indexr, value_parent in indexrcevalu:
            # get noi dung cong viec 
            valuearr = redic[value_parent]
            index1, value1 = valuearr[0]
            self.sht1.range(indexr,self.__hm_ndcv).value  =  rel.listothercell(irow =index1-2,
                                                                                    icolumn=self.__khns_ndcv)
            # get don vi
            self.sht1.range(indexr,self.__hm_dvt).value  =  rel.listothercell(irow =index1 - 2,
                                                                        icolumn=self.__khns_dvt)
            # get value sum if 
            self.sht1.range(indexr,self.__hm_ttnt).value =  '=SUMIF($BC:$BC,A{},$BL:$BL)'.format (indexr)            
            i = 0 
            for indexrk in range(indexr,indexr + len(valuearr)):
                index, value = valuearr[i]
                self.sht1.range(indexrk + 1 ,self.__hm_mvt).value = value
                self.sht1.range(indexrk + 1 ,self.__hm_ndcv).value = rel.listothercell(irow =index,
                                                                                            icolumn=self.__khns_ndcv)
                self.sht1.range(indexrk + 1 ,self.__hm_dvt).value = rel.listothercell(irow =index,
                                                                                icolumn=self.__khns_dvt)
                self.sht1.range(indexrk + 1 ,self.__hm_dgth).value = rel.listothercell(irow =index,
                                                                                icolumn=self.__khns_dvt)
                self.sht1.range(indexrk + 1 ,self.__hm_ttnt).value = '=I{0}*H{1}'.format(indexr,
                                                                                indexrk + 1)
                i = i + 1
    def valuehangmucforthvt(self):
        lrow = self.sht1.range('BC' + str(self.sht1.cells.last_cell.row)).end('up').row
        for index in range(8, lrow + 1):
            self.sht1.range(index,self.__hm_vt).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$L$8:$L${0})".format(self.m_row,
                                                                                                                    self.__sheetnametor,index,
                                                                                                                    "'" + self.sheetnameactive + "'")
            self.sht1.range(index,self.__hm_nc).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$M$8:$M${0})".format(self.m_row,
                                                                                                                    self.__sheetnametor,
                                                                                                                    index,
                                                                                                                    "'" + self.sheetnameactive + "'")
            self.sht1.range(index,self.__hm_mtc).value = "=SUMIF({1}!$C$8:$C${0},{3}!BC{2},{1}!$N$8:$N${0})".format(self.m_row,
                                                                                                            self.__sheetnametor,
                                                                                                            index,
                                                                                                            "'" + self.sheetnameactive + "'")
            


