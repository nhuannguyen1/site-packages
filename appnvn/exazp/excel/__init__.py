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
                        ):
        self.fpath = fpath
        self.sheetnametor=sheetnametor
        self.rangeg = rangeg
    def tohlitemsheet (self, indexcolumn = 2):
        """ return item value cell of A38:A60 """
        self.gdatafromothersheet(realtime = False)
        wb1.save(self.fpath)
    def gdatafromothersheet (self,
                            realtime = True,
                            indexcolumn = 2):
        """ get data from mothers sheet """
        if realtime:
            try:
                self.fpath = xw.books.active.fullname
            except:
                messagebox.showerror ("Error",
                                        "Not yet open file excel")
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
        # return list ma cong tac not node in cell value of ptvl
        getvaluelist = rel.revaluerownotnone()
        # return index row and value of active sheet  (ma cong tac)
        indexrcevalu = [[cell.row,
                        cell.value] for rangecell in sht1.range(self.rangeg) for cell in rangecell  if  cell.value in getvaluelist]
        # set value to acitve sheet 
        for indexr, value_parent in indexrcevalu:
            # get noi dung cong viec 
            valuearr = redic[value_parent]
            print (valuearr,valuearr)
            index1, value1 = valuearr[0]
            sht1.range(indexr,indexcolumn + 1).value  =  rel.listothercell(irow =index1-2,icolumn=5)
            # get don vi
            sht1.range(indexr,indexcolumn + 2).value  =  rel.listothercell(irow =index1 - 2,icolumn=6)

            # get value sum if 
            sht1.range(indexr ,indexcolumn + 7).value =  '=SUMIF($BC:$BC,A{},$BL:$BL)'.format (indexr)
                                                       
            i = 0 
            for indexrk in range(indexr,indexr + len(valuearr)):
                index, value = valuearr[i]
                sht1.range(indexrk + 1 ,indexcolumn).value = value

                sht1.range(indexrk + 1 ,indexcolumn + 1).value = rel.listothercell(irow =index,icolumn=5)
                sht1.range(indexrk + 1 ,indexcolumn + 2).value = rel.listothercell(irow =index,icolumn=6)
                sht1.range(indexrk + 1 ,indexcolumn + 6).value = rel.listothercell(irow =index,icolumn=8)
                sht1.range(indexrk + 1 ,indexcolumn + 7).value = '=I{0}*H{1}'.format(indexr,indexrk + 1)
                i = i + 1
            
