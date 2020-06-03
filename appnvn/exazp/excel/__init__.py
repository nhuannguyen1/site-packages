from tkinter import messagebox
from pynvn.excel import returnsheetbyname
import openpyxl as xl
from pynvn.excel.crelistadict import credict
import xlwings as xw 
class hexcel:
    """hading data excel for azzbbb"""
    def __init__ (self, fpath = None,sheetnametor="PTVT1", rangeg ="A38:A60",sheetnametow=None  ):
        self.fpath = fpath
        self.sheetnametor=sheetnametor
        self.rangeg = rangeg
        self.sheetnametow=sheetnametow

    def tohlitemativesheet (self, indexcolumn = 2):
        """ update data from child file"""
        # return sheet name
        wb1 = xl.load_workbook(filename=self.fpath,read_only=True)
        ptvl = wb1[self.sheetnametor]
        ptvl = returnsheetbyname(path=self.fpath,sheetname=self.sheetnametor)
        wb = xw.Book(self.fpath)
        sht1 = wb.sheets.active
        # get dict 
        rel = credict(wsheet=ptvl)
        redic =rel.redictvaluesandvaluecol()
        # content job
        ndcv = rel.redictvaluesandvaluecol(columnumber=5)
        # unit
        unit1 = rel.redictvaluesandvaluecol(columnumber=6)
        # muc hao phi
        mhp = rel.redictvaluesandvaluecol(columnumber=8)
        getvaluelist = rel.revaluerownotnone()
        #active wsheet
        wsheet = wb1.active
        for row in wsheet[self.rangeg]:
            i = 0
            for cell in row:
                cevalu =  cell.value
                if cevalu in getvaluelist:
                    indexr = cell.row
                    #key
                    arr = redic[cevalu]
                    # noi dung cong viec
                    ndcvcontent = ndcv[cevalu]
                    # unit
                    uni = unit1[cevalu]
                    # muc hao phi
                    mhpv = mhp[cevalu]

                    for indexr in range(indexr,indexr + len (arr)):
                        sht1.range(indexr,indexcolumn).value = arr[i]
                        sht1.range(indexr,indexcolumn + 1).value = ndcvcontent[i]
                        sht1.range(indexr,indexcolumn + 2).value = uni[i]
                        sht1.range(indexr,indexcolumn + 6).value = mhpv[i]
                        i = i + 1

    def tohlitemsheet (self, indexcolumn = 2):
        """ return item value cell of A38:A60 """
        wb1 = xl.load_workbook(filename=self.fpath)
        ptvl = wb1[self.sheetnametor]
        # get dict 
        rel = credict(wsheet=ptvl)
        redic =rel.redictvaluesandvaluecol()

        # content job
        ndcv = rel.redictvaluesandvaluecol(columnumber=5)

        getvaluelist = rel.revaluerownotnone()
        #active wsheet
        wsheet = wb1[self.sheetnametow]
        for row in wsheet[self.rangeg]:
            i = 0
            for cell in row:
                cevalu =  cell.value
                if cevalu in getvaluelist:
                    indexr = cell.row
                    arr = redic[cevalu]
                    for indexr in range(indexr,indexr + len (arr)):
                        wsheet.cell (row = indexr,column = indexcolumn).value = arr[i]
                        i = i + 1
        wb1.save(self.fpath)
    
    def gdatafromothersheet (self,getvaluelist, realtime = True):
        # return sheet name
        wb1 = xl.load_workbook(filename=self.fpath,read_only=True)
        ptvl = wb1[self.sheetnametor]
        ptvl = returnsheetbyname(path=self.fpath,sheetname=self.sheetnametor)

        wb = xw.Book(self.fpath)
        sht1 = wb.sheets.active
        # get dict 
        rel = credict(wsheet=ptvl)
        redic =rel.redictvaluesandvaluecol()
        # content job
        ndcv = rel.redictvaluesandvaluecol(columnumber=5)
        # unit
        unit1 = rel.redictvaluesandvaluecol(columnumber=6)
        # muc hao phi
        mhp = rel.redictvaluesandvaluecol(columnumber=8)
        getvaluelist = rel.revaluerownotnone()
        #active wsheet
        wsheet = wb1.active
        for row in wsheet[self.rangeg]:
            i = 0
            for cell in row:
                cevalu =  cell.value
                if cevalu in getvaluelist:
                    indexr = cell.row
                    #key
                    arr = redic[cevalu]
                    # noi dung cong viec
                    ndcvcontent = ndcv[cevalu]
                    # unit
                    uni = unit1[cevalu]
                    # muc hao phi
                    mhpv = mhp[cevalu]
                    if 

                    for indexr in range(indexr,indexr + len (arr)):
                        sht1.range(indexr,indexcolumn).value = arr[i]
                        sht1.range(indexr,indexcolumn + 1).value = ndcvcontent[i]
                        sht1.range(indexr,indexcolumn + 2).value = uni[i]
                        sht1.range(indexr,indexcolumn + 6).value = mhpv[i]
                        i = i + 1

