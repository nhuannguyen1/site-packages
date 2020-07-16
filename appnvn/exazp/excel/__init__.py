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

class hexcel:
    """hading data excel for azzbbb"""
    def __init__ (self, fpath = None,
                        pathconf = None
                        ):
        dicrowconf = returndictrowforcsv(path=pathconf)
        self.__fpath = fpath
        dirparhconf = parentdirectory(pathconf)
        self.__sheetnametor=dicrowconf["khns_sheetnamekhns"]
        self.__namefile=dicrowconf["khns_namfile"]
        self.__rangeg =dicrowconf["hm_rangege"]

        self.__rangeintct = returnseplistintbbystr(self.__rangeg)

        self.__rangestrct = returnliststr_from_str(self.__rangeg)

        self.__mvt = int(dicrowconf["khns_mavatu"])
        self.__khns_ndcv = int(dicrowconf["khns_noidungcongviec"])
        self.__khns_dvt = int(dicrowconf["khns_dvt"])

        self.__khns_muchaophi = (dicrowconf["khns_muchaophi"])
        self.__khns_muchaophi_int = col2num(self.__khns_muchaophi)

        self.__hm_mvt = int(dicrowconf["hm_mvt"])
        self.__hm_ndcv = int(dicrowconf["hm_noidungcongviec"])
        self.__hm_dvt = int(dicrowconf["hm_dvt"])

        self.__hm_dgth_str = (dicrowconf["hm_dgth"])

        self.__hm_dgth = col2num(self.__hm_dgth_str)

        self.__hm_ttnt_str = (dicrowconf["hm_ttnt"])
        self.__hm_ttnt = col2num(self.__hm_ttnt_str)

        self.__hm_startrowvalue = int(dicrowconf["hm_startrowvalue"])
        self.__hm_vta = dicrowconf["hm_vt"]
        self.__hm_nca = dicrowconf["hm_nc"]
        self.__hm_mtca = dicrowconf["hm_mtc"]
        self.__hm_tha = dicrowconf["hm_th"]

        self.__hm_ct = dicrowconf["hm_ct"]
        self.__hm_ct_int = col2num(self.__hm_ct)

        self.__hm_vt =col2num (dicrowconf["hm_vt"]) 
        self.__hm_nc =col2num (dicrowconf["hm_nc"]) 
        self.__hm_mtc =col2num (dicrowconf["hm_mtc"])
        self.__hm_th =col2num (dicrowconf["hm_th"])
        self.__valuenotnone =dicrowconf["valuenotnone"]
        valueall =dicrowconf["valueall"]
        self.__dictvalue =dicrowconf["dictvalue"]
        # csv for dict 
        self.pathtovalue = refullpath(dirparhconf,self.__dictvalue)
        # csv for value 
        self.valuenotnone = refullpath(dirparhconf,self.__valuenotnone)
        # path all value 
        self.pathvalueall = refullpath(dirparhconf,valueall)

        self.__khns_rangenumbermct_ptvt =dicrowconf["khns_rangenumbermct_ptvt"]
        # hangmuccongtac 
        self.__hm_startpasterange = dicrowconf["hm_startpasterange"]
        self.__startpasterange = returnseplistintbbystr(self.__hm_startpasterange)
        self.__hm_congtac = dicrowconf["hm_congtac"]

        # return list ma cong tac not node in cell value of ptvl by csv
        self.getvaluelist = convertcsvtolist(path=self.valuenotnone)
        # return all value from csv 
        self.getallvalue = convertcsvtolist(path=self.pathvalueall)

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
        # return list of cong tac
        """
        listofcongtac = self.sht1.range("{0}{1}:{0}{2}".format(self.__hm_congtac,self.__startpasterange[0] + 2,self.m_row)).value
        self.listofcongtac  = list(set(listofcongtac))
        """

        rangea = "{0}{1}:{0}{2}".format(self.__hm_congtac,self.__startpasterange[0] + 2,self.m_row)
        self.listofcongtac  =  listbyrangeremoveduplicate(sheetexcel=self.sht1,rangea=rangea)

    def gdatafromothersheet (self,
                            realtime = True):
        """ get data from mothers sheet """
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

        """
        # return index row and value of active sheet  ma cong tac
        indexrcevalu = [[cell.row,
                        cell.value] for rangecell in 
                        self.sht1.range(self.rangegc)
                        for cell in rangecell  if  cell.value
                        in self.getvaluelist]

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
                                                                                icolumn=self.__khns_muchaophi_int )

                self.sht1.range(indexrk + 1 ,self.__hm_ttnt).value = '=L{0}*K{1}'.format(indexr,
                                                                                indexrk + 1)
                i = i + 1
        """
    def listothercell (self,irow,icolumn):
        """ return value of column sheet ptvl1"""
        valuebycolr = self.thvt.range(irow,icolumn).value 
        return valuebycolr

    def valuehangmucforthvt(self):
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