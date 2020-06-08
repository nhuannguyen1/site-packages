from tkinter import messagebox
from pynvn.excel import returnsheetbyname
import openpyxl as xl
from pynvn.excel.crelistadict import credict
import xlwings as xw 


class hexcel:
    """hading data excel for azzbbb"""
    def __init__ (self, fpath = None,
                        sheetnametor="PTVT1", 
                        rangeg ="A501:A700",
                        sheetnametow=None ):

        self.fpath = fpath
        self.sheetnametor=sheetnametor
        self.rangeg = rangeg
        self.sheetnametow=sheetnametow

    def tohlitemsheet (self, indexcolumn = 2):
        """ return item value cell of A38:A60 """
        self.gdatafromothersheet(realtime = False)
        wb1.save(self.fpath)

    def gdatafromothersheet (self,realtime = True,indexcolumn = 2):
        """ get data from mothers sheet """
        if realtime:
            try:
                self.fpath = xw.books.active.fullname
            except:
                messagebox.showerror ("Error","Not yet open file excel")

        # return sheet name
        wb1 = xl.load_workbook(filename=self.fpath,
                            read_only=True)

        ptvl = wb1[self.sheetnametor]
        ptvl = returnsheetbyname(path=self.fpath,
                                sheetname=self.sheetnametor)

        wb = xw.Book(self.fpath)
        sht1 = wb.sheets.active
        active_sheet_name = wb.sheets.active.name
        # get dict 
        rel = credict(wsheet=ptvl,
                    pathfull=self.fpath,
                    namesheet=self.sheetnametor)

        redic =rel.redictvaluesandvaluecol()
        # content job
        ndcv = rel.redictvaluesandvaluecol(columnumber=5)
        # unit
        unit1 = rel.redictvaluesandvaluecol(columnumber=6)
        # khoi luong
        kl = rel.redictvaluesandvaluecol(columnumber=7)
        # muc hao phi
        mhp = rel.redictvaluesandvaluecol(columnumber=8)

        getvaluelist = rel.revaluerownotnone()
        #active wsheet
        wsheet = wb1[active_sheet_name]

        for rangecell in wsheet[self.rangeg]:
            i = 0
            
            for cell in rangecell:
                cevalu =  cell.value


                indexr,cevalu = [cell.row,cevalu] if cevalu in getvaluelist

                if cevalu in getvaluelist:





                    indexr = cell.row
                    #key
                    arr = redic[cevalu]
                    # noi dung cong viec
                    ndcvcontent = ndcv[cevalu]
                    # unit
                    uni = unit1[cevalu]
                    # khoi luong
                    klv = kl[cevalu]
                    # muc hao phi
                    mhpv = mhp[cevalu]
                    if realtime == False:
                        sht1 = wsheet
                    for indexr in range(indexr,indexr + len (arr)):
                        sht1.range(indexr + 1 ,indexcolumn).value = arr[i]
                        sht1.range(indexr + 1 ,indexcolumn + 1).value = ndcvcontent[i]
                        sht1.range(indexr + 1 ,indexcolumn + 2).value = uni[i]
                        sht1.range(indexr + 1 ,indexcolumn + 6).value = mhpv[i]
                        i = i + 1
