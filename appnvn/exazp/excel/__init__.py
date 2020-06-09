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
        # load work book by full path 
        wb = xw.Book(self.fpath)
        # set active workbook
        sht1 = wb.sheets.active
        # get name active workbook 
        active_sheet_name = wb.sheets.active.name
        # get dict 
        rel = credict(pathfull=self.fpath,
                    namesheet=self.sheetnametor,
                    engine="xlwings")
        #create dict with key is parent ma so 
        redic =rel.redictvaluesandvaluecol(columnumber=4)
        # return list maso parent not node in cell value 
        getvaluelist = rel.revaluerownotnone()
        # return list valie not none at D
        listvalueDnotnone = rel.revaluerownotnone(rangf="D7:D1000")
        # get dict ma so include same row
        dictms = rel.returndictvaluebyindexcolumnandrow(value_criteria_range =listvalueDnotnone)
        # return indext row and column
        indexrcevalu = [[cell.row,
                        cell.value] for rangecell in sht1.range[self.rangeg]\
                         for cell in rangecell  if  cell.value in getvaluelist]
        # set value to acitve sheet 
        for indexr, value_parent in indexrcevalu:
            valuearr = redic[value_parent]
            i = 0 
            for indexr in range(indexr,indexr + len(valuearr)):
                listothercell =dictms[valuearr[i]] 
                sht1.range(indexr + 1 ,indexcolumn).value = valuearr[i]
                sht1.range(indexr + 1 ,indexcolumn + 1).value = listothercell[0]
                sht1.range(indexr + 1 ,indexcolumn + 2).value = listothercell[1]
                sht1.range(indexr + 1 ,indexcolumn + 6).value = listothercell[2]
                i = i + 1
