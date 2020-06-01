import openpyxl as xl
from tkinter import messagebox
from pynvn.path.ppath import refullpath
from pynvn.excel import returnsheet

class hexcel:
    """copy excel to excel"""
    def __init__(self,wsheet = None,
                    fpath = None
                ):
                self.fpath = fpath
                self.wsheet = wsheet
                

    def habz30 (self):
        """handling data azb-30 sheet"""
        # return sheet to get data
        gsheet = returnsheet(path=self.fpath ,namesheet="TONG HOP HM")
        print ("gsheet",gsheet)

        #=SUMIFS('[KE HOACH NGAN SACH.xlsm]TONG HOP HM'!$I$933:$I$1413,'[KE HOACH NGAN SACH.xlsm]TONG HOP HM'!$A$933:$A$1413,$C16,'[KE HOACH NGAN SACH.xlsm]TONG HOP HM'!$B$933:$B$1413,J$3)

        self.wsheet.cell(row = 16, column = 9).value = '=SUMIFS({}!$I$933:$I$1413,{}!$A$933:$A$1413,$C16,{}!$B$933:$B$1413,J$3)'.format(gsheet)

        