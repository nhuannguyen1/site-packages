#  write to excel 
import pandas as pd
import openpyxl as xl

class cexcel:
    """copy excel to excel"""
    def __init__(self,sheetname = None,
                             pathdes= None, 
                             pathtocopy= None, 
                             ):

        self.sheetname = sheetname
        self.pathdes = pathdes
        self.pathtocopy = pathtocopy

    def copysheettoexcelexist(self):
        """ copy sheet name  to excel existing """

        wb1 = xl.load_workbook(filename=self.pathtocopy)
        names = wb1.sheetnames
        ws1 = wb1.worksheets[0]
        wb2 = xl.load_workbook(filename=self.pathdes)
        ws2 = wb2.get_sheet_by_name(name = names[0]) 

        for i,row in enumerate(ws1.iter_rows()):
            for j,col in enumerate(row):
                ws2.cell(row=i+1,column=j+1).value = col.value
        wb2.save(self.pathdes)